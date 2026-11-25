# -*- coding: utf-8 -*-
"""humaniser_check.py — håndhæver den bindende hovedregel om humaniserede resumeer.

Brugerens permanente hovedregel (25.11.2026):

    "ET HUMANISERET RESUME ER DET VIGTIGSTE FAKTOR TIL AT LAVE RESUMEER"

Reglen siger, at et resume skal kunne læses som skrevet og redigeret af et menneske,
før det har værdi. Alt andet i systemet (kravdækning, ATS, kultur, masterdesign) er
underordnet denne ene regel. Derfor findes den her som en **selvstændig, blokerende
gate**, der kan køres alene og som også kaldes fra `policy_check.py`.

Gate'en måler ikke "om teksten er god", men om den bærer de typiske tegn på
maskinel, skabelonagtig tekst:

  H1  Klischeer og skabelonmarkører      -> BLOKERENDE
  H2  Em dash                            -> BLOKERENDE
  H3  "ikke kun … men også"              -> BLOKERENDE
  H4  Adjektivstak (3+ i træk)           -> BLOKERENDE
  H5  Gentagne sætninger                 -> BLOKERENDE
  H6  Gentaget sætningsåbning (AI-parallelisme) -> ADVARSEL
  H7  Ensartethed i afsnitslængde         -> ADVARSEL
  H8  Sætningslængde uden variation       -> ADVARSEL
  H9  Selvcentrerede formuleringer       -> ADVARSEL
  H10 Menneskesproglige rødstøv (overskrifter, forbindelser) -> OPLYSNING

Brug:
    python3 scripts/humaniser_check.py <dokument.docx>
    python3 scripts/humaniser_check.py <dokument.docx> --json
    python3 scripts/humaniser_check.py <dokument.docx> --min-score 80
"""
import argparse
import json
import re
import statistics
import sys

import docx

# --------------------------------------------------------------------------
# H1 — klischeer og skabelonmarkører (blokerende)
# --------------------------------------------------------------------------
CLICHES = [
    # AI- og HR-sprogets faste floskler
    "spiller en afgørende rolle", "spiller en nøglerolle", "spiller en vigtig rolle",
    "i en verden hvor", "i en verden med", "i en verden af",
    "i dagens", "i dagens verden", "i dag' s", "i dag'",
    "det er ikke bare", "er ikke blot", "er ikke kun",
    "proaktivt og fleksibelt", "proaktiv og fleksibel",
    "en bred vifte af", "bred vifte af",
    "altid stræbt efter", "altid stræber efter",
    "uovertruffelig", "uovertruffeligt",
    "grundlæggende", "dybtgående", "gennemgående",
    "konkretisering", "konkretiseringsarbejde",
    "som en der", "som en som", "den type der",
    "løbende optimering", "kontinuerlig optimering",
    "høj grad af", "høj grad",
    "stolt af at", "stolthed over",
    "med stor glæde", "med stor passion", "brænder for",
    "det er min styrke", "min stærkeste side", "det er mig en ære",
    "jeg er en holdånd", "jeg er en holdspiller",
    "jeg holder højt på", "det driver mig", "det motiverer mig",
    "jeg er overbevisende", "jeg er dygtig til", "jeg er god til",
    "er en stærk kandidat", "en stærk kandidat", "stærk kandidat",
    "værdi for pengene", "rentabelt", "value for money",
    "en mulighed for at", "muligheden for at",
    "for at sikre",  # for hyppigt AI-signal, kun ved gentagen brug
]

# --------------------------------------------------------------------------
# H9 — selvcentrerede formuleringer (advarsel)
# --------------------------------------------------------------------------
SELF_CENTRED = [
    "min styrke", "min stærkeste", "min svaghed", "min motivation", "min ambition",
    "min personlige", "jeg er overbevisende", "jeg er dygtig", "jeg er god til",
    "jeg holder højt", "jeg brænder", "det er min", "jeg er stolt",
]

# --------------------------------------------------------------------------
# H4 — adjektivstak (3+ adjektiver i træk)
# --------------------------------------------------------------------------
ADJECTIVES = set("""
innovativ innovative fleksibel fleksibelt fleksible resultatorienteret proaktiv proaktivt
dedikeret dedikeret struktureret systematisk analytisk strategisk visionær visionært
skalerbar effektiv effektivt motiveret motiveret ansvarlig kvalitetsbevidst
løsningsorienteret samarbejdsvillig udadvendt initiativrig målbevidst energisk
kompetent erfaren dygtig stærk stærkt dygtige ambitiøs ambitiøse passioneret
selvsikker fleksibilitet fagligt faglig faglige fagkyndigt
""".split())

# Forbindelser, der typisk leder til en adjektivstak
STACK_JOIN = re.compile(r'\s*(?:,|;|og)\s+', re.IGNORECASE)


def doc_text(doc):
    """Hele dokumentets tekst: afsnit + tabelceller.

    En flettet celle (gridSpan) returneres af python-docx én gang pr. gridkolonne.
    Den skal kun læses én gang, ellers ligner banner-rækker gentagne sætninger.
    """
    parts = [p.text for p in doc.paragraphs]
    for t in doc.tables:
        for row in t.rows:
            seen = set()
            for c in row.cells:
                key = id(c._tc)
                if key in seen:
                    continue
                seen.add(key)
                parts.append(c.text)
    return "\n".join(parts)


def sentences(text):
    """Sætninger med rimelig dansk sætningsdeling."""
    out = []
    for block in text.split("\n"):
        block = block.strip()
        if not block:
            continue
        for s in re.split(r'(?<=[.!?])\s+', block):
            s = s.strip()
            if len(s) > 25:
                out.append(s)
    return out


def normalise(s):
    return re.sub(r'\s+', ' ', s.strip().lower())


def check(docx_path):
    doc = docx.Document(docx_path)
    text = doc_text(doc)
    low = text.lower()
    report = {"file": docx_path, "blocking": [], "warnings": [], "info": [], "stats": {}}

    # ---- H2 em dash -------------------------------------------------------
    # Em dash (—) er altid forbudt. En dash (–) er derimod korrekt i intervaller
    # ("2–10 mio.", "2024 – nu", "Dag 1–30") og kun et problem, når den bruges
    # som tankestreg mellem to ord.
    n_dash = text.count("—")
    report["stats"]["em_dash"] = n_dash
    if n_dash:
        report["blocking"].append(
            f"H2 em dash ({n_dash} stk.) — skriv en almindelig tankestreg "
            "(komma, bindestreg eller ny sætning)")
    # En dash i et interval ("2–10 mio.", "2024 – nu", "Dag 1–30") er korrekt.
    # En dash som tankestreg mellem to ord skal erstattes af komma eller ny sætning.
    stray = []
    for m in re.finditer(r'–', text):
        before = text[:m.start()].rstrip()
        after = text[m.end():].lstrip()
        if not before or not after:
            continue
        # interval: tal umiddelbart foran eller efter
        if before[-1].isdigit() or after[0].isdigit():
            continue
        # interval mellem årstal ("2000–2003") er allerede dækket ovenfor
        stray.append(text[max(0, m.start() - 30):m.end() + 30].replace("\n", " "))
    report["stats"]["en_dash_as_dash"] = len(stray)
    if stray:
        report["warnings"].append(
            f"H2 en dash brugt som tankestreg ({len(stray)} stk.) — brug komma "
            "eller del sætningen: " + " | ".join(stray[:2]))

    # ---- H3 "ikke kun … men også" ---------------------------------------
    m = re.search(r'ikke kun\b[^.]{0,90}?men også', low, re.IGNORECASE | re.DOTALL)
    if m:
        report["blocking"].append(
            f"H3 'ikke kun … men også' ({m.group(0)[:60]}…) — skriv den ene tank direkte")

    # ---- H1 klischeer -----------------------------------------------------
    found_cliche = []
    for c in CLICHES:
        if c in low:
            # "for at sikre" tælles kun, hvis det optræder mange gange
            if c == "for at sikre":
                if low.count(c) >= 3:
                    found_cliche.append(f"{c} (x{low.count(c)})")
                continue
            found_cliche.append(c)
    if found_cliche:
        report["blocking"].append(
            "H1 klischeer/skrabelonmarkører: " + "; ".join(found_cliche))

    # ---- H4 adjektivstak --------------------------------------------------
    # Fanger kæder som "innovativ, fleksibel og resultatorienteret", hvor
    # konjunktionen "og" ikke bryder optællingen.
    CONNECTORS = {"og", "samt", "ogsaa", "og_samt"}
    stacks = []
    for sent in sentences(text):
        toks = [t.strip('.,;:()').lower() for t in sent.split()]
        run = []
        for i, tok in enumerate(toks):
            if tok in ADJECTIVES:
                run.append(tok)
            elif tok in CONNECTORS and run and i + 1 < len(toks) \
                    and toks[i + 1] in ADJECTIVES:
                continue  # konjunktionen binder kæden sammen
            else:
                if len(run) >= 3:
                    stacks.append(" ".join(run))
                run = []
        if len(run) >= 3:
            stacks.append(" ".join(run))
    if stacks:
        report["blocking"].append(
            "H4 adjektivstak (3+ adjektiver i træk): " + " | ".join(stacks[:3]))

    # ---- H5 gentagne sætninger -------------------------------------------
    seen = {}
    for s in sentences(text):
        k = normalise(s)
        seen[k] = seen.get(k, 0) + 1
    dupes = [s for s, n in seen.items() if n > 1]
    if dupes:
        report["blocking"].append(
            "H5 gentagne sætninger: " + " | ".join(d[:70] for d in dupes[:3]))

    # ---- H6 gentaget sætningsåbning (AI-parallelisme) --------------------
    openers = {}
    for s in sentences(text):
        w = normalise(s).split()
        if len(w) >= 3:
            key = " ".join(w[:3])
            openers[key] = openers.get(key, 0) + 1
    repeated = sorted([(n, k) for k, n in openers.items() if n >= 3], reverse=True)
    if repeated:
        report["warnings"].append(
            "H6 gentaget sætningsåbning (AI-parallelisme): "
            + "; ".join(f"'{k}' x{n}" for n, k in repeated[:3]))

    # ---- H7 ensartethed i afsnitslængde ------------------------------------
    paras = [p.text.strip() for p in doc.paragraphs if len(p.text.strip()) > 120]
    if len(paras) >= 5:
        lens = [len(p) for p in paras]
        mean = statistics.mean(lens)
        spread = (max(lens) - min(lens)) / mean if mean else 0
        report["stats"]["paragraph_len_spread"] = round(spread, 2)
        report["stats"]["paragraphs"] = len(paras)
        if spread < 0.25:
            report["warnings"].append(
                f"H7 afsnittene er næsten lige lange (længdespredning {spread:.0%}) — "
                "menneskeskrevet tekst varierer i længde; bryt mønsteret")

    # ---- H8 sætningslængde uden variation --------------------------------
    sents = sentences(text)
    if sents:
        slens = [len(s.split()) for s in sents]
        sd = statistics.pstdev(slens)
        report["stats"]["sentence_len_sd"] = round(sd, 2)
        report["stats"]["sentences"] = len(sents)
    else:
        sd = 0.0
    if len(sents) >= 8:
        if sd < 5.0:
            report["warnings"].append(
                f"H8 sætningerne har næsten samme længde (spredning {sd:.1f} ord) — "
                "bland korte og lange sætninger som et menneske gør")

    # ---- H9 selvcentrerede formuleringer ----------------------------------
    self_hits = [w for w in SELF_CENTRED if w in low]
    if self_hits:
        report["warnings"].append(
            "H9 selvcentrerede formuleringer: " + "; ".join(self_hits))

    # ---- H10 rødstøv ------------------------------------------------------
    headings = []
    for p in doc.paragraphs:
        t = p.text.strip()
        if t and p.style.name.upper().startswith(("CVH", "HEAD", "TITLE", "LETTERTITLE")):
            headings.append(t)
    report["stats"]["headings"] = len(headings)
    report["info"].append(
        f"H10 {len(headings)} overskrifter i JD-sprog — kontrollér at ingen er "
        "skabelonmæssige eller overlapende")

    # ---- score ------------------------------------------------------------
    score = 100
    score -= 25 * len(report["blocking"])
    score -= 6 * len(report["warnings"])
    score = max(0, min(100, score))
    report["score"] = score
    report["ok"] = not report["blocking"] and score >= 60
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('docx_path')
    ap.add_argument('--json', action='store_true', help='maskinlæsbart output')
    ap.add_argument('--min-score', type=int, default=60,
                    help='mindste humaniseringsscore (default 60)')
    args = ap.parse_args()

    rep = check(args.docx_path)

    if args.json:
        print(json.dumps(rep, ensure_ascii=False, indent=2))
        return 0 if rep["ok"] else 1

    print(f"DOKUMENT   : {rep['file']}")
    print(f"HUMANISERING: score {rep['score']}/100")
    st = rep["stats"]
    print(f"  sætninger {st.get('sentences', 0)} · afsnit {st.get('paragraphs', 0)} · "
          f"sætningsspredning {st.get('sentence_len_sd', 0)} ord · "
          f"em dash {st.get('em_dash', 0)}")
    for b in rep["blocking"]:
        print(f"  ✗ {b}")
    for w in rep["warnings"]:
        print(f"  ! {w}")
    for i in rep["info"]:
        print(f"  · {i}")
    print()
    if rep["blocking"]:
        print("✗ Dokumentet er ikke humaniseret nok — ret de blokerende fund før commit.")
        return 1
    if rep["score"] < args.min_score:
        print(f"✗ Humaniseringsscore {rep['score']} under kravet ({args.min_score}).")
        return 1
    print("✓ Dokumentet er humaniseret: ingen skabelonmarkører, "
          "variation og egne formuleringer.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
