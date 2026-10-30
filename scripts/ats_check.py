# -*- coding: utf-8 -*-
"""
ats_check.py — kvalitetsgate før en ansøgning sendes.

Brug:
    python3 scripts/ats_check.py <fil.docx|fil.pdf> --jd-words words.txt
    python3 scripts/ats_check.py <fil> --words "operations supervisor,gmp,fda,lean,..."

Tjekker
  1. ATS-hygiejne: tekstbokse, spalter, billeder, sidehoved/-fod-tekst.
  2. Tabelregel: masterdesignet er tabelbaseret, så kravet er ikke "ingen tabeller" men
     "lineær læserækkefølge": ingen indlejrede tabeller, ingen gridSpan i datarækker,
     højst 2 kolonner i indholdstabeller, og al tekst ligger i body (ikke i shapes).
  3. Nøgleordsdækning mod JD-listen (case-insensitive, hele ord).
  4. Læsbar tekst i PDF-laget (ikke et billede) og sideantal.
  5. Kontaktoplysninger i brødteksten (mail + telefon).
Exitkode 1, hvis der er blokerende fejl.
"""
import argparse
import re
import sys


W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def _docx_body_text(root):
    """Læser body i dokumentets rækkefølge — også tekst inde i tabeller."""
    out = []

    def para_text(p):
        return "".join(t.text or "" for t in p.iter(W + "t"))

    def walk(el):
        for child in el:
            tag = child.tag
            if tag == W + "p":
                out.append(para_text(child))
            elif tag == W + "tbl":
                for tr in child.findall(W + "tr"):
                    cells = []
                    for tc in tr.findall(W + "tc"):
                        cells.append(" ".join(para_text(p)
                                              for p in tc.findall(W + "p")).strip())
                    out.append(" | ".join(c for c in cells if c))
            elif tag == W + "sdt":
                content = child.find(W + "sdtContent")
                if content is not None:
                    walk(content)

    walk(root)
    return "\n".join(out)


def docx_text(path):
    import docx
    from docx.oxml.ns import qn

    d = docx.Document(path)
    root = d.element.body
    text = _docx_body_text(root)

    # tabelstruktur: lineær læserækkefølge?
    nested = len(root.findall(".//" + W + "tc//" + W + "tbl"))
    wide, spanned = [], []
    for i, tbl in enumerate(root.iter(W + "tbl")):
        rows = tbl.findall(W + "tr")
        for r, tr in enumerate(rows):
            tcs = tr.findall(W + "tc")
            spans = [tc for tc in tcs if tc.find(W + "tcPr/" + W + "gridSpan") is not None]
            if spans and r > 1:
                spanned.append(i)
                break
        if len(rows) > 1 and len(tbl.findall(W + "tr")[1].findall(W + "tc")) > 2:
            wide.append(i)

    xml = root.xml
    textboxes = xml.count("<w:txbxContent")
    columns = 0
    for s in d.sections:
        cols = s._sectPr.find(qn("w:cols"))
        if cols is not None and int(cols.get(qn("w:num"), "1")) > 1:
            columns += 1
    header_footer = " ".join(
        p.text for s in d.sections
        for p in list(s.header.paragraphs) + list(s.footer.paragraphs)
    ).strip()
    images = xml.count("<pic:pic")
    return {
        "text": text,
        "tables": len(d.tables),
        "nested_tables": nested,
        "wide_tables": wide,
        "spanned_rows": spanned,
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
    return {"text": text, "tables": 0, "nested_tables": 0, "wide_tables": [],
            "spanned_rows": [], "textboxes": 0, "columns": 0,
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

    if info.get("nested_tables"):
        problems.append(f"{info['nested_tables']} indlejrede tabeller (bryder læserækkefølgen)")
    if info.get("wide_tables"):
        problems.append(f"tabel(ler) med >2 kolonner: nr. {info['wide_tables']}")
    if info.get("spanned_rows"):
        problems.append(f"gridSpan uden for banner-/hovedrække: tabel nr. {info['spanned_rows']}")
    if info.get("tables"):
        notes.append(f"{info['tables']} tabeller — masterdesign, lineær læserækkefølge "
                     f"(banner + 2 kolonner), accepteret")
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
    print(f"Tabeller/tekstbokse/spalter: {info['tables']}/{info['textboxes']}/{info['columns']}"
          f" — indlejrede/brede: {info.get('nested_tables', 0)}/{len(info.get('wide_tables', []))}")
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
