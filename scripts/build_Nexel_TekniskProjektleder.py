# -*- coding: utf-8 -*-
"""
build_Nexel_TekniskProjektleder.py
Ansøgning + CV i ét dokument: Teknisk projektleder, Nexel (Mellem Kundeprojekter), Virum.
Dansk JD → dansk dokument. Format: Calibri 10,5 pt, 2 cm marginer, rigtige Word-punkter,
side 1 = ansøgning, sideskift, derefter CV (Profil, Erfaring, Uddannelse, Kompetencer).

Fakta udelukkende fra master/MASTER_RESUME_SHAHRAM_AJLOO.md + brugerbekræftelser:
  - 04.11.2026: direkte arbejde med 10/0,4 kV distributionsnet (generelt), mindst tre års
    erfaring med projektledelse og entreprisestyring (tilskrives ikke én arbejdsgiver)
  - 12.11.2026: akkord, opmåling, regulering og opgørelse
  - 23.11.2026 (denne stilling): arbejder efter stærkstrømsbekendtgørelsen i praksis;
    har arbejdet med AB 18, AB forenklet og DS 475; konkret erfaring med myndighedsbehandling;
    egen bil og 70% kontor i Virum accepteret.
"""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_Nexel_TekniskProjektleder.docx"

FONT = "Calibri"
BODY = Pt(10.5)
SMALL = Pt(10)

doc = Document()

for s in doc.sections:
    s.top_margin = s.bottom_margin = s.left_margin = s.right_margin = Cm(2.0)

normal = doc.styles["Normal"]
normal.font.name = FONT
normal.font.size = BODY
normal.paragraph_format.space_after = Pt(5)
normal.paragraph_format.line_spacing = 1.10

for st_name in ("List Bullet",):
    st = doc.styles[st_name]
    st.font.name = FONT
    st.font.size = BODY
    st.paragraph_format.space_after = Pt(1)
    st.paragraph_format.line_spacing = 1.06

for st in (normal, doc.styles["List Bullet"]):
    rpr = st.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = rpr.makeelement(qn("w:rFonts"), {})
        rpr.append(rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), FONT)


def para(text, bold=False, size=BODY, align=None, space_after=None,
         space_before=None, italic=False):
    p = doc.add_paragraph()
    if align is not None:
        p.alignment = align
    if space_after is not None:
        p.paragraph_format.space_after = space_after
    if space_before is not None:
        p.paragraph_format.space_before = space_before
    r = p.add_run(text)
    r.bold = bold
    r.italic = italic
    r.font.size = size
    r.font.name = FONT
    return p


def bullet(text):
    p = doc.add_paragraph(style="List Bullet")
    r = p.add_run(text)
    r.font.size = BODY
    r.font.name = FONT
    return p


def heading(text):
    return para(text, bold=True, size=Pt(11.5), space_before=Pt(8), space_after=Pt(3))


# ============================== SIDE 1: ANSØGNING ==============================

para("Måløv, den 23. november 2026", size=SMALL, space_after=Pt(10))

para("Ansøgning som Teknisk projektleder, Nexel", bold=True, size=Pt(13),
     space_after=Pt(8))

para("Kære David Jensen", space_after=Pt(8))

para("Udbygningen af elnettet i Storkøbenhavn er en del af den grønne omstilling, og "
     "den bliver til virkelighed projekt for projekt. I Mellem Kundeprojekter ligger "
     "der 20-25 af slagsen i porteføljen på "
     "én gang, fra kundetilslutninger til større infrastrukturprojekter og "
     "modernisering af netstationer. Fælles for dem er, at ansvaret først slipper, "
     "når distributionsanlægget er spændingssat og afleveret.")

para("Stillingens kerne er detailprojektering og entreprisestyring, der holder "
     "tidsplan og budget, mens bygherrer, rådgivere, byggepladsledere og "
     "elinstallatører alle trækker i samme retning. Dertil kommer "
     "myndighedsbehandling, kundedialoger, projektgennemgang, bygge- og statusmøder, "
     "tilsyn med entreprenørerne og en afslutning med slutafregning og aflevering. "
     "Når så mange projekter kører samtidig, er det porteføljen som helhed, der skal "
     "holdes i bevægelse, og strukturen i opfølgningen er selve opgaven.")

para("Jeg har el-teknikken i bunden og projekterne i hænderne. Jeg er maskinmester "
     "med dansk elautorisation, arbejder efter stærkstrømsbekendtgørelsen til daglig "
     "og har direkte erfaring med 10/0,4 kV distributionsnet. I Ventek-Air stod jeg "
     "for 11 samtidige anlægsprojekter fra specifikation til formel aflevering med "
     "udbud, underentreprenører, aftalegrundlag og afleveringspakker. I ELOHVAC "
     "driver jeg entrepriserne selv: tilbud og beregning, planlægning, akkord og "
     "opmåling, regulering af mer- og mindrearbejde og opgørelse. Hos Novo Nordisk "
     "førte jeg 37 samtidige anlægs- og CAPEX-projekter med SAP til økonomi og "
     "aktiv og månedsrapportering til ledelse og bygherre. Jeg har arbejdet efter "
     "AB 18 og AB forenklet, kender DS 475 for ledningsanlæg i jord, og "
     "myndighedsbehandling følger med entreprisestyringen.")

para("Problemløsningen sker hands-on: direkte til kollegaen, kunden eller "
     "entreprenøren med åben og ærlig kommunikation, og intet projekt slipper, før "
     "det er afleveret. Til porteføljestyringen bruger jeg strukturen bevidst: "
     "interessentkort, RACI og fast mødekadence, og jeg er professionel og aktiv "
     "Claude-koder med Python. Det "
     "betyder i praksis, at statusrapporter, tilsynsnotater og dokumentation kan "
     "holdes ensartet og opdateret, så tiden i stedet går til kunderne og i marken.")

para("Min plan for de første måneder er ligetil. Første 30 dage går med "
     "projektmodellen, designguiden og porteføljen: jeg lærer sagerne, "
     "interessenterne og entreprenørerne at kende sammen med kollegerne og lægger "
     "mit eget porteføljeoverblik for de 20-25 projekter. Fra dag 30 kører jeg egne "
     "projekter efter fast rytme med bygge- og statusmøder, tilsynsnotater og et "
     "skema for myndighedsspor og slutafregning. Fra dag 60 kører hele porteføljen "
     "efter samme rytme, og jeg afleverer første forslag til fælles arbejdsgange og "
     "vidensdeling på tværs af teamet, suppleret af en prototype på AI-assisteret "
     "månedsrapportering.")

para("Jeg har egen bil og kører gerne ud til sagerne i Storkøbenhavn, og der er kort "
     "vej fra Måløv til Virum. Lad os tage en samtale om, hvordan porteføljen skal "
     "styres fra nettilslutningsaftale til spændingssat anlæg. Jeg kan træffes på "
     "+45 93 99 95 14.")

para("Med venlig hilsen", space_before=Pt(6), space_after=Pt(10))
para("Shahram Ajloo", bold=True, space_after=Pt(0))
para("Elautoriseret maskinmester", space_after=Pt(0))
para("ajlooshahram@gmail.com · linkedin.com/in/shahramajloo", size=SMALL)

# ============================== SIDESKIFT → CV ==============================

p = doc.add_paragraph()
p.add_run().add_break(WD_BREAK.PAGE)

para("Shahram Ajloo", bold=True, size=Pt(15), align=WD_ALIGN_PARAGRAPH.CENTER,
     space_after=Pt(0))
para("Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo",
     size=SMALL, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=Pt(8))

# --- Profil ---
heading("Profil")
para("Jeg leverer detailprojektering, projektledelse og entreprisestyring af 10/0,4 kV "
     "anlægsprojekter fra nettilslutningsaftale til spændingssat og afleveret anlæg. "
     "Porteføljen holdes i mål med fast struktur for økonomi, tidsplan, tilsyn og "
     "dokumentation, og jeg er vant til mange samtidige projekter og tæt dialog med "
     "bygherrer, rådgivere og entreprenører.")

# --- Erfaring ---
heading("Erfaring")

para("ELOHVAC ApS · København · Ejer og elautoriseret maskinmester · maj 2023 – nu",
     bold=True, space_after=Pt(2))
bullet("Entreprise- og projektstyring: tilbud og beregning, planlægning, "
       "materialestyring, underentreprenører, KS og afleveringsdokumentation med "
       "fuldt P&L-ansvar.")
bullet("Akkord og opmåling: akkordbreve, opmåling, regulering af mer- og "
       "mindrearbejde og opgørelse.")
bullet("Installation og idriftsættelse af el-tekniske anlæg, tavler, styring, fiber "
       "og PDS til afleveret anlæg med kundedokumentation.")
bullet("Personaleledelse af 5 elektrikere og 3 lærlinge med planlægning, 1:1, MUS og "
       "oplæring.")
bullet("AI-værktøjer i Python og Claude API til tilbudsberegning, tidsplaner, "
       "KS-tjeklister og KPI-dashboards har givet over 40 % produktivitetsløft.")

para("Data Power Consultant ApS · København · Medejer og CTO for AI-afdelingen · "
     "2024 – nov. 2026 (sideløbende med ELOHVAC)", bold=True, space_after=Pt(2))
bullet("Ansvarlig for AI- og AI coding-afdelingen med 4-10 personer; implementering af "
       "tekniske og industrielle applikationer fra kravafdækning til idriftsættelse "
       "og overdragelse.")
bullet("AI som værktøj i ledelsesarbejdet: ledelsesrapportering, beslutningsoplæg og "
       "KPI-analyse med fast struktur.")
bullet("AI-assisteret softwareudvikling med fælles standarder for AI-output; "
       "kundeløsninger med LLM-API'er og AI-agenter.")
bullet("Matrixledelse af to sideløbende organisationer med én samlet plan. Selskabet "
       "er ophørt i november 2026, og i dag drives kun ELOHVAC.")

para("Novo Nordisk A/S · Kalundborg og Bagsværd · Senior idriftsættelsesingeniør og "
     "projektleder, elsystem · nov. 2022 – jul. 2024", bold=True, space_after=Pt(2))
bullet("Porteføljeansvar for 37 samtidige anlægs- og CAPEX-projekter (DKK 2–10 mio. "
       "pr. stk.) med fremdrift, økonomi og risici på tværs af engineering, indkøb "
       "og anlæg.")
bullet("FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA med nul kritiske afvigelser ved "
       "aflevering; tværfaglig ledelse af 25 højt specialiserede medarbejdere.")
bullet("El-tekniske anlæg: tavler og styring, UPS, nød- og panikbelysning, ABA/ABV og "
       "PDS; fejlfinding med A3, 5xHvorfor og Ishikawa; SAP ERP og månedsrapportering.")
bullet("40 % reduktion af energiomkostninger gennem PDCA-program.")

para("Ventek-Air · København · Projekt- og værkstedsleder · jan. 2022 – nov. 2022",
     bold=True, space_after=Pt(2))
bullet("11 samtidige anlægsprojekter (DKK 2–10 mio.) fra specifikation til formel "
       "aflevering, med daglig ledelse af 14-mands team, kapacitets- og "
       "fremdriftsstyring.")
bullet("Udbud og tilbud, underentreprenører, aftalegrundlag, sikkerhedsdokumentation "
       "og afleveringspakker.")
bullet("Daglige tavlemøder og flaskehalsanalyser; standardiserede arbejdsgange med "
       "markant løft i leveringsevnen.")

para("Biofos (Lynetten) · København · Vedligeholdelses- og driftsleder · "
     "aug. 2017 – jan. 2022", bold=True, space_after=Pt(2))
bullet("Drift af kritisk forsyningsanlæg med pumper, HVAC, højspændingstavler og "
       "SCADA: oppetid, forebyggende vedligehold og akut fejlfinding 24/7.")
bullet("5S, Standard Work og PDCA på værksted og lager; reservedelsflow og lagerstyring.")
bullet("Skifteholdsdrift: LOTO, risikovurdering, APV og nærved-hændelser.")

para("ARJ Engineering · Teheran · Elektromekaniker og produktionsteamleder · "
     "dec. 2003 – mar. 2010", bold=True, space_after=Pt(2))
bullet("Fejldiagnose og reparation af industrielle el- og mekaniske anlæg; "
       "rodårsagsanalyse og korrigerende handlinger.")
bullet("Ledelse af 12 mekanikere og teknikere i maskinværksted med vagtplanlægning og "
       "materialestyring på en produktionslinje med elektromotorer, pumper og "
       "dykpumper.")

# --- Uddannelse ---
heading("Uddannelse")
bullet("Dansk elautorisation LV/MV/HV som elautoriseret maskinmester, Sikkerhedsstyrelsen, "
       "maj 2023.")
bullet("B.Tech (EQF6), teknologiledelse og maskinteknik, Copenhagen School of Marine "
       "Engineering & Technology Management, 2017–2022.")
bullet("El- og maskinteknisk design, elteknik (EQF6), Tehran Technical University, "
       "2000–2003; HF, VUC, 2012–2017.")
bullet("Køleteknik og klimaanlæg (AMU), Mercantec, 2021. STCW-certifikater, "
       "Søfartsstyrelsen, 2021–2023.")
bullet("PRINCE2, certificeret projektleder (AXELOS/PeopleCert).")
bullet("Lean og Six Sigma: DMAIC, 5S, PDCA, VSM, A3, Kaizen, Standard Work, SMED, TPM, "
       "5xHvorfor, Ishikawa og FMEA, arbejdet med i praksis, ikke certificeret.")

# --- Kompetencer ---
heading("Kompetencer")
bullet("Projektering og entreprisestyring: detailprojektering, tilbud, akkord og "
       "opmåling, slutafregning, tilsyn, underentreprenører, KS og aflevering; "
       "AB 18, AB forenklet og DS 475.")
bullet("El og forsyning: 10/0,4 kV distributionsnet, kabellægning, fiber og PDS, "
       "tavler og styring; stærkstrømsbekendtgørelsen og DS/HD 60364; erfaring fra "
       "energibranchen.")
bullet("Myndighedsbehandling og tilladelser i forbindelse med anlægsprojekter.")
bullet("Økonomi og styring: budget, fremdrift og risici, SAP ERP, månedsrapportering "
       "og P&L.")
bullet("Projektværktøjer: PRINCE2, RACI, interessentanalyse, tavlemøder og Kanban.")
bullet("Digitalt: Python, Claude API og Claude Code, professionel og aktiv AI- og "
       "Claude-koder, Power BI; AI-assisteret rapportering og dokumentation.")
bullet("Sprog: dansk som modersmål, engelsk i skrift og tale.")
bullet("Betingelser: kørekort B og egen bil; bopæl i Måløv med kort vej til Virum.")

doc.save(OUT)
print("Gemte", OUT)

# ---------------- kvalitetskontrol ----------------
full = "\n".join(p.text for p in doc.paragraphs)
banned = ["spearheaded", "leveraged", "passionate", "dynamic", "results-driven",
          "proven track record", "synergy", "cutting-edge", "innovative solutions",
          "seamlessly", "robust", "demonstrated ability", "fast-paced",
          "drevet", "lidenskabelig", "dynamisk", "synergi", "banebrydende",
          "sømløst", "ikke kun", "men også", "—"]
hits = [w for w in banned if w.lower() in full.lower()]
jd_words = ["detailprojektering", "entreprisestyring", "projektledelse", "portefølje",
  "10/0,4 kV", "nettilslutningsaftale", "distributionsanlæg", "netstationer",
  "kundetilslutning", "infrastrukturprojekter", "modernisering", "interessenter",
  "myndighedsbehandling", "kundedialoger", "bygherrer", "rådgivere", "byggepladsledere",
  "elinstallatører", "projektgennemgang", "bygge- og statusmøder", "tilsyn",
  "entreprenører", "slutafregning", "aflevering", "projektmodel", "designguide",
  "hands-on", "afleveret", "overblik", "kommunikation", "stærkstrømsbekendtgørelsen",
  "SAP", "AB 18", "AB forenklet", "DS 475", "kørekort B", "dansk", "engelsk",
  "energibranchen", "el-teknisk", "maskinmester", "grøn", "vidensdeling", "kabellægning"]
missing = [w for w in jd_words if w.lower() not in full.lower()]
print("Ord i alt:", len(full.split()))
print("Banned/em-dash hits:", hits if hits else "ingen")
print("Manglende JD-ord:", missing if missing else "ingen")

brk = next(i for i, p in enumerate(doc.paragraphs)
           if 'w:br' in p._p.xml and 'page' in p._p.xml)
CAP = 257 / 4.15
def chunk_lines(chunk):
    tot = 0
    for p in chunk:
        t = p.text
        if not t.strip():
            continue
        cpl = 88 if p.style.name == "List Bullet" else 95
        lines = max(1, -(-len(t) // cpl))
        sa = p.paragraph_format.space_after.pt if p.paragraph_format.space_after else 5
        sb = p.paragraph_format.space_before.pt if p.paragraph_format.space_before else 0
        tot += lines + (sa + sb) / 6
    return tot
ps = doc.paragraphs
lb = chunk_lines(ps[:brk])
cv = chunk_lines(ps[brk + 1:])
print(f"Brev ~{lb:.1f}/{CAP:.0f} → {'OK 1 side' if lb < CAP - 1 else 'RISIKO'}")
print(f"CV   ~{cv:.1f}/{2 * CAP:.0f} → {'OK 2 sider' if cv < 2 * CAP - 2 else 'RISIKO'}")
