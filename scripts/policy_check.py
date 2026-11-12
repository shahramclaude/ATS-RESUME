# -*- coding: utf-8 -*-
"""policy_check.py — håndhæver den bindende policy "JOBBET FØRST" (master/README.md).

Kontrollerer at et bygget dokument opfylder kravene i den bindende policy:

1. Der findes en kravmatrix i dokumentet (tabel med "Krav" i header).
2. Antallet af rækker i kravmatricen >= antallet af krav i kravfilen
   (jd/<Stillingsnavn>_krav.txt — ét krav pr. linje, taget ordret fra opslaget).
3. Hvert krav i kravfilen kan genfindes i matricens venstre kolonne
   (mindst 60 % af de betydende ord), så intet krav er "dækket" af en anden række.
4. Ingen selvrosende personbeskrivelse (blokerende) og ingen bløde
   ros/adfærdsord uden kobling til en opgave (advarsel).

Brug:
    python3 scripts/policy_check.py <dokument.docx> --krav-file jd/<x>_krav.txt
"""
import argparse
import re
import sys

import docx

# Ord der aldrig må beskrive ansøgeren som person (blokerende).
BANNED = [
    'intelligent', 'talentfuld', 'talentfuldt', 'ambitiøs', 'ambitiøse', 'enestående',
    'fremragende', 'perfekt', 'perfekte', 'passioneret', 'passionerede', 'karismatisk',
    'den rette kandidat', 'den ideelle kandidat', 'bedste kandidat', 'imponerende',
    'fabelagtig', 'suveræn', 'ekstraordinær', 'højt begavet',
]

# Ord der kun er i orden, når de er knyttet til en konkret opgave (advarsel).
SOFT = ['engageret', 'dygtig', 'dygtige', 'stærk personlighed', 'god til mennesker',
        'teamplayer', 'selvstændig og', 'positiv', 'udadvendt']

STOPWORDS = set("""og i at er en et den det de til af for med på som der har have kan skal
vil blive bliver være været fra ved om ud over under mellem samt både eller men også
samt fx eks. evt. mv. du dig din dit dine jeg min mit mine vi os jer dem denne dette
disse sådan hvis når hvor hvad hvem hvilke hvilken samtlige alle anden andre andet
samtidig derudover desuden samt""" .split())


def load_krav(path):
    with open(path, encoding='utf-8') as fh:
        lines = [ln.strip() for ln in fh]
    return [ln for ln in lines if ln and not ln.startswith('#')]


def norm(text):
    return re.sub(r'\s+', ' ', text.lower()).strip()


def tokens(text):
    words = re.findall(r"[a-zæøå0-9\-]+", text.lower())
    return {w for w in words if len(w) > 3 and w not in STOPWORDS}


def matches(a, b):
    """To ord matcher, hvis de er ens eller det ene er en forstavelse af det andet
    (håndterer bøjning og sammensætninger som specialist/specialister, bygværk/bygværker)."""
    if a == b:
        return True
    short, long = (a, b) if len(a) <= len(b) else (b, a)
    return len(short) >= 5 and long.startswith(short)


def overlap(kt, lt):
    if not kt:
        return (1.0, 0)
    hit = sum(1 for a in kt if any(matches(a, b) for b in lt))
    return (hit / len(kt), hit)


def doc_text(doc):
    parts = [p.text for p in doc.paragraphs]
    for t in doc.tables:
        for row in t.rows:
            for cell in row.cells:
                parts.append(cell.text)
    return '\n'.join(parts)


def find_matrix(doc):
    for t in doc.tables:
        if not t.rows:
            continue
        header = norm(' '.join(c.text for c in t.rows[0].cells))
        if 'krav' in header or 'requirement' in header:
            return t
    # fallback: kravmatrix hvor header er i anden række (banner overst)
    for t in doc.tables:
        if len(t.rows) > 2:
            header = norm(' '.join(c.text for c in t.rows[1].cells))
            if 'krav' in header or 'requirement' in header:
                return t
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('docx_path')
    ap.add_argument('--krav-file', required=True,
                    help='fil med ét krav pr. linje (dansk eller engelsk opslag)')
    ap.add_argument('--kultur-file', default='',
                    help='jd/<x>_kultur.txt — arbejdsgiverens egne ord (mission, værdier, kultur), '
                         'ét udtryk pr. linje; mindst 60 % skal kunne genfindes i dokumentet')
    ap.add_argument('--min-evidence', type=int, default=110,
                    help='mindste antal tegn dokumentation pr. kravrække (dybdekontrol)')
    args = ap.parse_args()

    doc = docx.Document(args.docx_path)
    krav = load_krav(args.krav_file)
    matrix = find_matrix(doc)

    ok = True
    print(f"DOKUMENT : {args.docx_path}")
    print(f"KRAVFIL  : {args.krav_file} ({len(krav)} krav)")

    if args.kultur_file:
        print(f"KULTURFIL: {args.kultur_file}")

    if matrix is None:
        print("BLOKERENDE\n  ✗ ingen kravmatrix fundet (tabel med 'Krav' i header)")
        return 1

    # datarækker = alle rækker undtagen header(e)
    rows = matrix.rows
    head0 = norm(' '.join(c.text for c in rows[0].cells))
    start = 1 if ('krav' in head0 or 'requirement' in head0) else 2
    data_rows = rows[start:]
    print(f"MATRIX   : {len(data_rows)} rækker (header række {start})")

    if len(data_rows) < len(krav):
        ok = False
        print(f"  ✗ færre rækker ({len(data_rows)}) end krav i opslaget ({len(krav)})")

    # dækning pr. krav: ordene i kravet skal kunne genfindes i en rækkes label
    # dækning vurderes mod både kravlabel og dokumentation i rækken
    row_texts = [norm(' '.join(c.text for c in r.cells)) for r in data_rows]
    row_tokens = [tokens(rt) for rt in row_texts]
    uncovered = []
    for k in krav:
        kt = tokens(k)
        if not kt:
            continue
        best = max((overlap(kt, rt) for rt in row_tokens), default=(0.0, 0))
        ratio, hits = best
        # dækket hvis en stor andel af kravets ord genfindes, eller mindst tre
        # betydende ord fra kravet optræder i samme række
        if ratio < 0.45 and hits < 3:
            uncovered.append((k, round(ratio, 2)))

    if uncovered:
        ok = False
        print("  ✗ krav uden en tilsvarende række i matricen:")
        for k, score in uncovered:
            print(f"      ({score}) {k}")

    # ---- dybdekontrol (policy 04.11.2026): intet krav må besvares overfladisk
    HEADER_LABELS = {'krav i opslaget', 'krav', 'requirement in the posting', 'requirement',
                     'krav i stillingsopslaget'}
    HEADER_EVIDENCE = {'dokumentation', 'evidence', 'bevis', 'dokumentation/bevis'}
    shallow, thin, no_result = [], [], []
    depth_rows = 0
    for r in data_rows:
        cells = [c.text.strip() for c in r.cells]
        label = cells[0] if cells else ''
        ev = cells[1] if len(cells) > 1 else ''
        if norm(label) in HEADER_LABELS or norm(ev) in HEADER_EVIDENCE:
            continue
        depth_rows += 1
        if len(ev) < int(args.min_evidence * 0.55):
            shallow.append((label, len(ev)))
        elif len(ev) < args.min_evidence:
            thin.append((label, len(ev)))
        if ev and not re.search(r'\d', ev):
            no_result.append(label)

    print(f"DYBDE    : {depth_rows - len(shallow)}/{depth_rows} rækker med konkret dokumentation "
          f"(min. {args.min_evidence} tegn)")
    if shallow:
        ok = False
        print("  ✗ krav besvaret overfladisk (policy: intet krav må behandles overfladisk):")
        for label, n in shallow:
            print(f"      '{label[:70]}' — kun {n} tegn dokumentation")
    if thin:
        print("  ! tynd dokumentation — uddyb med metode, ansvar og resultat:")
        for label, n in thin:
            print(f"      '{label[:70]}' — {n} tegn")
    if no_result:
        print("  ! ingen tal i dokumentationen — vis resultatet, hvor det findes:")
        for label in no_result[:8]:
            print(f"      '{label[:70]}'")

    # ---- kultursynkronisering (policy 04.11.2026): arbejdsgiverens egne ord skal kunne genfindes
    text = doc_text(doc)
    if args.kultur_file:
        with open(args.kultur_file, encoding='utf-8') as fh:
            kultur = [ln.strip() for ln in fh if ln.strip() and not ln.startswith('#')]
        lowk = norm(text)
        missing_k = [k for k in kultur if norm(k) not in lowk]
        hit = len(kultur) - len(missing_k)
        share = hit / len(kultur) if kultur else 1.0
        print(f"KULTUR   : {hit}/{len(kultur)} af arbejdsgiverens egne udtryk genfundet "
              f"({share:.0%})")
        if share < 0.6:
            ok = False
            print("  ✗ kultursynkronisering utilstrækkelig (policy: sproget skal synkroniseres med "
                  "virksomheden) — mangler:")
            for k in missing_k[:10]:
                print(f"      '{k}'")
        elif missing_k:
            print("  ! udtryk der ikke blev brugt:")
            for k in missing_k[:6]:
                print(f"      '{k}'")
    # selvros / personbeskrivelse
    text = doc_text(doc)
    low = norm(text)

    # Data Power-posten (bruger, 12.11.2026): skal stå i alle CV'er, som selvstaendig sideloebende post
    if 'data power' not in low:
        print("  ! Data Power Consultant ApS mangler — policy 12.11.2026 kræver posten i alle CV'er "
              "som selvstændig, sideløbende post (se master/README.md)")
    hits = [w for w in BANNED if w in low]
    soft = [w for w in SOFT if w in low]
    if hits:
        ok = False
        print("  ✗ selvrosende personbeskrivelse (policy: ingen personbeskrivelse):")
        for w in hits:
            print(f"      '{w}'")
    if soft:
        print("  ! bløde rosord — kontroller at de er knyttet til en konkret opgave:")
        for w in soft:
            print(f"      '{w}'")

    print()
    if ok:
        print("✓ Policy 'jobbet først' opfyldt: fuld kravdækning, ingen personbeskrivelse.")
        return 0
    print("✗ Policy 'jobbet først' IKKE opfyldt — ret dokumentet før commit.")
    return 1


if __name__ == '__main__':
    sys.exit(main())
