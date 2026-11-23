# -*- coding: utf-8 -*-
"""
build_Measure_FieldServiceEngineer.py
Ansøgning + CV i ét dokument: Field Service Engineer, Measure (Measureroad ApS), DTU Risø.
Dansk JD → dansk dokument. Format: Calibri 11 pt, 2 cm marginer, rigtige Word-punkter,
side 1 = ansøgning, sideskift, derefter CV (Profil, Erfaring, Uddannelse, Kompetencer).
Fakta udelukkende fra master/MASTER_RESUME_SHAHRAM_AJLOO.md + brugerbekræftelser 23.11.2026:
  - kun overførbar erfaring mht. laser/optik og kalibrering (påstås ikke)
  - rejsebetingelser accepteret (ca. 80 rejsedage/år, DTU Risø)
  - Windows og netværksfejlfinding er rutine
"""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK

OUT = "Shahram_Ajloo_Measure_FieldServiceEngineer_v2.docx"

FONT = "Calibri"
BODY = Pt(10.5)
SMALL = Pt(10)

doc = Document()

# --- Sideopsætning: A4, 2 cm marginer ---
for s in doc.sections:
    s.top_margin = s.bottom_margin = s.left_margin = s.right_margin = Cm(2.0)

# --- Grundstil ---
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

# sørg for at skrifttypen også gælder for komplekse scripts
from docx.oxml.ns import qn
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

para("Ansøgning som Field Service Engineer, Measure", bold=True, size=Pt(13),
     space_after=Pt(10))

para("”Just install, connect and Measure.” Tre ord på jeres hjemmeside. Bag dem "
     "ligger jobbet: systemet skal sidde rigtigt i kundens målevogn, måledataene "
     "skal holde, og kunden skal kunne køre videre med tillid til resultatet, "
     "uanset om vognen står i Roskilde eller i New Zealand.")

para("Kerneopgaven i stillingen er at være bindeled mellem Measures teknologi og de "
     "internationale kunder. En væsentlig del af arbejdet er installation og "
     "idriftsættelse af målesystemerne i specialindrettede målevogne og en grundig "
     "introduktion af kunderne til systemernes anvendelse. Dertil kommer teknisk "
     "support, fejlfinding og oplæring, og god service indebærer kommunikation og "
     "formidling af tekniske problemstillinger på en måde, kunderne forstår. Når "
     "elektronik, laseroptik, fiberoptik, "
     "sensorer, mekanik og software skal fungere sammen, findes fejlen ved at "
     "analysere måledata, grafer og logfiler systematisk, ikke ved at gætte.")

para("Jeg har elektronik og el i bunden. Jeg er elautoriseret maskinmester og "
     "har fulgt tekniske anlæg fra installation og test til idriftsættelse og drift "
     "hos kunden. På Novo Nordisk førte jeg 37 anlægs- og CAPEX-projekter gennem "
     "FAT/SAT og IQ/OQ/PQ med nul kritiske afvigelser ved aflevering. I ELOHVAC "
     "installerer og servicerer jeg el-, ventilations- og klimaanlæg, trækker fiber "
     "og PDS-kabler, og følger hvert anlæg, til det er afleveret, og kunden er "
     "introduceret i brugen af det. "
     "Fra driften af Lynetten har jeg erfaring med akut fejlfinding på kritisk udstyr "
     "med pumper, "
     "HVAC, højspændingstavler og SCADA, og fra værkstedet erfaring med "
     "rodårsagsanalyse på "
     "industrielle el- og mekaniske anlæg. A3, 5xHvorfor og Ishikawa er mine faste "
     "værktøjer, når en fejls årsag skal findes, også når der ikke står en færdig "
     "beskrivelse i en servicemanual.")

para("To ting supplerer billedet. Jeg er professionel og aktiv Claude-koder med "
     "Python og Claude API, og det får praktisk betydning her: logfiler og måledata "
     "kan gennemgås med små analyseværktøjer, og serviceprocedurer og teknisk "
     "dokumentation kan holdes ensartet og opdateret. Softwareopdateringer og "
     "fjernsupport er rutine, og Windows og netværksfejlfinding hører til min "
     "hverdag. Den direkte erfaring med laseroptik har jeg ikke endnu. Den tilegner "
     "jeg mig hos erfarne kolleger, og min erfaring med præcisionsarbejde på komplekse "
     "systemer er med fra dag ét.")

para("Min plan for de første måneder er konkret. I de første 30 dage lærer jeg "
     "teknologien sammen med kollegerne: produkter, montage, test og kalibrering i "
     "huset. Jeg holder et løbende notat over fejl og spørgsmål. Fra dag 30 til 60 "
     "står jeg for "
     "installationer og kundebesøg og lægger "
     "et udkast til installations- og serviceprotokol for målevognene, med fast "
     "gennemgang af måledata, grafer og logfiler efter hver installation. Fra dag 60 "
     "kører jeg selvstændige installationer og kundeoplæring, afleverer første "
     "forslag til serviceprocedurer og teknisk dokumentation, og bygger en prototype "
     "på et AI-assisteret værktøj til analyse af måledata og logfiler.")

para("Jeg er indstillet på rejseaktiviteten på ca. 80 dage om året med installationer "
     "og oplæring af en til to ugers varighed og weekendarbejde med afspadsering. "
     "Jeg bor i Måløv med kort vej til Risø. Lad os tage en samtale om, hvordan "
     "installation, support og kundeoplæring "
     "skal køre, inden målesæsonen går i gang. Jeg kan træffes på +45 93 99 95 14.")

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
para("Jeg leverer installation, idriftsættelse, fejlfinding, service og kundeoplæring "
     "på avancerede tekniske systemer, så udstyret fungerer optimalt hos kunden. "
     "Fejlfinding sker metodisk på tværs af elektronik, el, hardware og software med "
     "analyse af måledata, grafer og logfiler, og jeg er indstillet på stillingens "
     "internationale rejseaktivitet.")

# --- Erfaring ---
heading("Erfaring")

para("ELOHVAC ApS · København · Ejer og elautoriseret maskinmester · maj 2023 – nu",
     bold=True, space_after=Pt(2))
bullet("Installation, fejlfinding og forebyggende vedligehold på el-, ventilations- "
       "og klimaanlæg hos erhvervskunder, fra akutte udkald til afleveret anlæg med "
       "dokumentation.")
bullet("Idriftsættelse og aflevering med kundeintroduktion til anlæggets anvendelse, KS "
       "og afleveringsdokumentation; fiber og PDS, tavler og styring.")
bullet("Serviceaftaler med responstid og kvalitet som KPI og nul kritiske afvigelser; "
       "LOTO, APV og risikovurdering ved pladsopstart.")
bullet("Oplæring og daglig planlægning for 5 elektrikere og 3 lærlinge på skiftende "
       "byggepladser, med 1:1 og MUS.")
bullet("AI-værktøjer i Python og Claude API til tilbudsberegning, tidsplaner, "
       "KS-tjeklister og KPI-dashboards har givet over 40 % produktivitetsløft.")

para("Data Power Consultant ApS · København · Medejer og CTO for AI-afdelingen · "
     "2024 – nov. 2026 (sideløbende med ELOHVAC)", bold=True, space_after=Pt(2))
bullet("Ansvarlig for AI- og AI coding-afdelingen med 4-10 personer; implementering af "
       "tekniske og industrielle applikationer fra kravafdækning og arkitektur over "
       "integration til idriftsættelse og overdragelse.")
bullet("Kundeløsninger med LLM-API'er og AI-agenter fra proceskortlægning til "
       "produktionssat løsning; AI-assisteret softwareudvikling med fælles "
       "standarder for AI-output.")
bullet("AI coding til design af tekniske anlæg og industrielle komponenter: beregning, "
       "dimensionering og designvarianter med faglig validering af output.")
bullet("Matrixledelse af to sideløbende organisationer med én samlet plan og skriftlige "
       "prioriteringer. Selskabet er ophørt i november 2026, og i dag drives kun ELOHVAC.")

para("Novo Nordisk A/S · Kalundborg og Bagsværd · Senior idriftsættelsesingeniør og "
     "projektleder, elsystem · nov. 2022 – jul. 2024", bold=True, space_after=Pt(2))
bullet("Idriftsættelse af el-tekniske anlæg: 37 samtidige anlægs- og CAPEX-projekter "
       "(DKK 2–10 mio. pr. stk.) med fremdrift, økonomi og risici på tværs af "
       "engineering, indkøb og anlæg.")
bullet("FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA med nul kritiske afvigelser ved "
       "aflevering; tværfaglig ledelse af 25 højt specialiserede medarbejdere.")
bullet("Fejlfinding på tavler og styring, UPS, nød- og panikbelysning, ABA/ABV og PDS "
       "med A3, 5xHvorfor og Ishikawa; SAP ERP og månedsrapportering.")
bullet("40 % reduktion af energiomkostninger gennem PDCA-program.")

para("Ventek-Air · København · Projekt- og værkstedsleder · jan. 2022 – nov. 2022",
     bold=True, space_after=Pt(2))
bullet("11 samtidige anlægsprojekter (DKK 2–10 mio.) fra specifikation til formel "
       "aflevering, med daglig ledelse af 14-mands team, kapacitets- og "
       "fremdriftsstyring.")
bullet("Udbud og tilbud, underentreprenører, aftalegrundlag, sikkerhedsdokumentation "
       "og afleveringspakker.")

para("Biofos (Lynetten) · København · Vedligeholdelses- og driftsleder · "
     "aug. 2017 – jan. 2022", bold=True, space_after=Pt(2))
bullet("Kritisk el- og mekanisk drift med pumper, HVAC, højspændingstavler og SCADA: "
       "oppetid, forebyggende vedligehold og akut fejlfinding 24/7.")
bullet("5S, Standard Work og PDCA på værksted og lager; reservedelsflow og lagerstyring.")
bullet("Skifteholdsdrift med sikkerhedsdisciplin: LOTO, risikovurdering, APV og "
       "nærved-hændelser.")

para("ARJ Engineering · Teheran · Elektromekaniker og produktionsteamleder · "
     "dec. 2003 – mar. 2010", bold=True, space_after=Pt(2))
bullet("Fejldiagnose og reparation af industrielle el- og mekaniske anlæg; "
       "rodårsagsanalyse og korrigerende handlinger.")
bullet("Ledelse af 12 mekanikere og teknikere i maskinværksted med vagtplanlægning og "
       "materialestyring, på en produktionslinje med elektromotorer, pumper og "
       "dykpumper, og med ansvar på tværs af produktets livscyklus.")

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
bullet("Installation og idriftsættelse: montage, test, aflevering og kundeintroduktion; "
       "el-installationer, tavler og styring, fiber og PDS, UPS, ABA/ABV, nød- og "
       "panikbelysning.")
bullet("Fejlfinding og analyse: måledata, grafer og logfiler; rodårsagsanalyse med A3, "
       "5xHvorfor og Ishikawa; Windows, netværksfejlfinding og IT-værktøjer i "
       "dagligdagen.")
bullet("Software og AI: Python, Claude API og Claude Code, professionel og aktiv "
       "AI- og Claude-koder, Power BI, SAP ERP, Excel og Power Query; "
       "softwareopdateringer og fjernsupport.")
bullet("Ledelse og samarbejde: kunderelationer, oplæring og kundekontakt, 1:1 og MUS, "
       "tavlemøder, RACI, PRINCE2 og situationsbestemt ledelse (SLII).")
bullet("Arbejdsstil: selvstændig, struktureret og omhyggelig med sans for detaljer, "
       "udadvendt og serviceminded, og jeg står fast på mine faglige vurderinger.")
bullet("Sprog: dansk som modersmål, engelsk flydende i skrift og tale, persisk som "
       "modersmål.")
bullet("Betingelser: kørekort B; indstillet på ca. 80 rejsedage om året med "
       "internationale installationer og oplæring; bopæl i Måløv.")

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
words = len(full.split())
print("Ord i alt:", words)
print("Banned/em-dash hits:", hits if hits else "ingen")
