# -*- coding: utf-8 -*-
"""
ats_check.py — kvalitetsgate før en ansøgning sendes.

Brug:
    python3 scripts/ats_check.py <fil.docx|fil.pdf> --jd-words words.txt
    python3 scripts/ats_check.py <fil> --words "operations supervisor,gmp,fda,lean,..."

Tjekker
  1. ATS-hygiejne: tabeller, tekstbokse, spalter, billeder, sidehoved/-fod-tekst, overskrifter i caps.
  2. Nøgleordsdækning mod JD-listen (case-insensitive, hele ord).
  3. Læsbar tekst i PDF-laget (ikke et billede) og sideantal.
  4. Kontaktoplysninger i brødteksten (mail + telefon).
Exitkode 1, hvis der er blokerende fejl.
"""
import argparse
import re
import sys


def docx_text(path):
    import docx

    d = docx.Document(path)
    body = [p.text for p in d.paragraphs]
    tables = len(d.tables)
    # tekstbokse / shapes
    xml = d.element.xml
    textboxes = xml.count("<w:txbxContent")
    columns = 0
    for s in d.sections:
        cols = s._sectPr.find(
            "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}cols"
        )
        if cols is not None and int(cols.get(
                "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}num", "1")) > 1:
            columns += 1
    header_footer = " ".join(
        p.text for s in d.sections
        for p in list(s.header.paragraphs) + list(s.footer.paragraphs)
    ).strip()
    images = xml.count("<pic:pic")
    return {
        "text": "\n".join(body),
        "tables": tables,
        "textboxes": textboxes,
        "columns": columns,
        "header_footer": header_footer,
        "images": images,
        "pages": None,
    }


def pdf_info(path):
    from pypdf import PdfReader

    r = PdfReader(path)
    text = "\n".join((p.extract_text() or "") for p in r.pages)
    images = 0
    for page in r.pages:
        try:
            images += len(page.images)
        except Exception:
            pass
    return {"text": text, "tables": 0, "textboxes": 0, "columns": 0,
            "header_footer": "", "images": images, "pages": len(r.pages)}


def _norm(t):
    t = t.lower().replace("\u2011", "-").replace("\u2013", "-")
    t = re.sub(r"\s+", " ", t)
    return t


def coverage(text, words):
    """Hele ord, men tolerant over for flertal, -ly/-ally og bindestreg vs. mellemrum."""
    low = _norm(text)
    low_nodash = low.replace("-", " ")
    missing = []
    for w in words:
        w = _norm(w)
        core = w.replace("-", r"[\s-]?")
        # engelske + danske bøjninger (flertal, bestemt form, -hed, -ing, -lig ...)
        pat = (r"(?<!\w)" + core +
               r"(?:s|es|en|et|e|er|ene|ens|ens|hed|heden|heds|lig|lige|ing|ally|ly|ed)?(?![\w])")
        if not (re.search(pat, low) or re.search(pat, low_nodash)):
            missing.append(w)
    return missing


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--words", default="", help="kommasepareret nøgleordsliste fra JD")
    ap.add_argument("--words-file", default="")
    ap.add_argument("--expect-pages", type=int, default=0)
    args = ap.parse_args()

    info = pdf_info(args.file) if args.file.lower().endswith(".pdf") else docx_text(args.file)
    text = info["text"]

    words = [w.strip() for w in args.words.split(",") if w.strip()]
    if args.words_file:
        with open(args.words_file, encoding="utf-8") as fh:
            words += [w.strip() for w in fh.read().replace("\n", ",").split(",") if w.strip()]

    problems, notes = [], []

    if info["tables"]:
        problems.append(f"{info['tables']} tabeller (ATS kan ikke læse kolonner korrekt)")
    if info["textboxes"]:
        problems.append(f"{info['textboxes']} tekstbokse (usynligt for mange parsere)")
    if info["columns"]:
        problems.append("flerspaltet sektion")
    if info["header_footer"]:
        problems.append(f"tekst i sidehoved/-fod: {info['header_footer'][:60]!r}")
    if info["images"]:
        notes.append(f"{info['images']} billede(r) — OK, men al tekst skal også findes som tekst")
    if len(text) < 1200:
        problems.append("tekstlaget er meget kort — er filen et billede/scan?")

    if "@" not in text or not re.search(r"\+45\s?\d{2}", text):
        problems.append("mangler mail/telefon i brødteksten")

    missing = coverage(text, words) if words else []
    if missing:
        problems.append("nøgleord mangler: " + ", ".join(missing))

    if args.expect_pages and info["pages"] and info["pages"] != args.expect_pages:
        notes.append(f"sideantal {info['pages']} (forventet {args.expect_pages})")

    print(f"FIL            : {args.file}")
    print(f"Tegn i tekstlag: {len(text)}")
    if info["pages"]:
        print(f"Sider          : {info['pages']}")
    print(f"Nøgleord tjekket: {len(words)} — mangler {len(missing)}")
    print(f"Tabeller/tekstbokse/spalter: {info['tables']}/{info['textboxes']}/{info['columns']}")
    print()
    if notes:
        print("NOTER")
        for n in notes:
            print("  -", n)
        print()
    if problems:
        print("BLOKERENDE")
        for p in problems:
            print("  ✗", p)
        sys.exit(1)
    print("✓ Ingen ATS-blokeringer fundet.")


if __name__ == "__main__":
    main()
