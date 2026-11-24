#!/usr/bin/env python3
"""Byg Shahram_Ajloo_ARC_ProjektingeniorCO2.docx (brev + CV i ét dokument)."""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_ARC_ProjektingeniorCO2.docx"

doc = Document()
for s in doc.sections:
    s.top_margin = s.bottom_margin = Cm(2.0)
    s.left_margin = s.right_margin = Cm(2.0)

normal = doc.styles["Normal"]
normal.font.name = "Calibri"
normal.font.size = Pt(10.5)
normal._element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
pf = normal.paragraph_format
pf.space_before = Pt(0); pf.space_after = Pt(4); pf.line_spacing = 1.0

def _mkstyle(name, size, bold=False):
    st = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
    st.base_style = doc.styles["Normal"]
    st.font.name = "Calibri"; st.font.size = Pt(size); st.font.bold = bold
    st._element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    return st

st_name  = _mkstyle("CVName", 16, True)
st_h1    = _mkstyle("CVH1", 12, True)
st_job   = _mkstyle("CVJob", 10.5, True)
st_title = _mkstyle("LetterTitle", 11, True)
st_h1.paragraph_format.space_before = Pt(8); st_h1.paragraph_format.space_after = Pt(2)
st_job.paragraph_format.space_before = Pt(6); st_job.paragraph_format.space_after = Pt(1)
st_name.paragraph_format.space_after = Pt(1)
st_title.paragraph_format.space_after = Pt(6)

def para(text, bold_prefix=None, style=None, after=None):
    p = doc.add_paragraph(style=style)
    if bold_prefix:
        r = p.add_run(bold_prefix); r.bold = True
    if text:
        p.add_run(text)
    if after is not None:
        p.paragraph_format.space_after = Pt(after)
    return p

def bullet(text, bold_prefix=None):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.6)
    if bold_prefix:
        r = p.add_run(bold_prefix); r.bold = True
    p.add_run(text)
    return p

def job(org_line, bullets):
    para(None, style="CVJob", after=1).add_run(org_line)
    for b in bullets:
        bullet(b)

# ----------------------------- BREV -----------------------------
para("Måløv, den 23. november 2026", after=2)
para("Ansøgning som Projektingeniør til CO2-fangstanlægget, ARC", style="LetterTitle")
para("Kære ansættelsesudvalg", after=4)

para("Demonstrationsanlægget på Amager Bakke er bygget for at omsætte CO2-fangst "
     "til driftserfaring: 500 kilo CO2 i timen nu og grundlaget for de anlæg, der "
     "senere skal fange hundredetusindvis af tons i den grønne omstilling. Anlægget "
     "skal køre som et reelt "
     "procesanlæg i hverdagen med høj teknisk tilgængelighed og sikker og stabil "
     "drift, og erfaringerne fra driften er selve produktet, der bærer teknologien "
     "videre.")

para("Rollens opgave dækker hele kæden tæt på anlægget: daglig drift, overvågning "
     "og betjening, forebyggende og afhjælpende vedligehold og fejlfinding på "
     "mekaniske, elektriske og procesmæssige komponenter. Dertil planlægning og "
     "koordinering af vedligeholdsaktiviteter og tekniske arbejder, opfølgning på "
     "alarmer, driftsforstyrrelser og tekniske fejl, optimering og løbende "
     "forbedring af driften samt koordinering med leverandører, specialister og "
     "tekniske kolleger. Driften, vedligeholdet, ændringerne og erfaringerne skal "
     "dokumenteres, tests og forsøg skal køres ordentligt, og erfaringer og teknisk "
     "viden skal kunne "
     "overføres til fremtidige CO2-fangstanlæg.")

para("Jeg er maskinmester med elautorisation og har i over ti år stået for drift og "
     "vedligehold af procesanlæg, der ikke måtte stå stille. I Biofos førte jeg "
     "skifteholdsdrift døgnet rundt på et kritisk forsyningsanlæg med pumper, "
     "styring og SCADA: forebyggende vedligehold, alarmopfølgning og akut "
     "fejlfinding på tværs af mekanik, el og proces. Jeg har deltaget i tests og "
     "idriftsættelse af nye anlæg med FAT/SAT og kvalitetssikring, jeg arbejder "
     "struktureret og følger "
     "opgaverne helt til dørs med dokumentation, der kan bruges bagefter, og jeg er "
     "nysgerrig af natur: optimering og forbedringer er en del af mit daglige "
     "arbejde, senest et PDCA-program, der skar 40 procent af energiomkostningerne. "
     "Som professionel og aktiv Claude-koder med Python kan jeg gøre driftsdata og "
     "erfaringer systematiske, så de bliver til dokumentation og vidensdeling i "
     "stedet for glemte noter.")

para("Min plan for de første måneder er konkret. Efter 30 dage kender jeg anlægget "
     "udefra og indefra: proces og opbygning, SCADA og alarmer, "
     "vedligeholdsplanerne og sikkerhedsrutinerne, og jeg har været på gulvet med "
     "erfarne kolleger. Efter 60 dage driver jeg selv drift og vedligehold i fast "
     "rytme med fejlfinding, planlægning og dokumentation. Efter 90 dage ligger de "
     "første optimeringsforslag klar fra driften, og jeg har samlet erfaringerne, "
     "så de kan bruges på fremtidige anlæg.")

para("Jeg bor i Måløv med kort vej til Amager og kan tiltræde efter aftale. Lad os "
     "tale om, hvordan demonstrationsanlægget får den drift, der gør CO2-fangst til "
     "hverdag. Jeg kan træffes på +45 93 99 95 14.", after=6)

para("Med venlig hilsen", after=8)
para("Shahram Ajloo", after=0)
para("Elautoriseret maskinmester", after=0)
para("ajlooshahram@gmail.com · linkedin.com/in/shahramajloo", after=0)

# sideskift
br = doc.add_paragraph()
run = br.add_run()
br_el = run._r.makeelement(qn('w:br'), {qn('w:type'): 'page'})
run._r.append(br_el)

# ----------------------------- CV -----------------------------
para("Shahram Ajloo", style="CVName", after=1)
para("Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo", after=6)

para("Profil", style="CVH1")
para("Jeg driver procesanlæg sikkert og stabilt med høj teknisk tilgængelighed "
     "gennem systematisk vedligehold, fejlfinding og dokumentation, og kombinerer "
     "praktisk problemløsning med teknisk forståelse. Maskinmester med "
     "elautorisation og praktisk erfaring fra proces-, energi- og produktionsanlæg, "
     "hands-on og helt til dørs.")

para("Erfaring", style="CVH1")

job("ELOHVAC ApS · København · Ejer og elautoriseret maskinmester · maj 2023 – nu", [
    "Installation, service og idriftsættelse af el-tekniske anlæg, tavler, styring, "
    "fiber og PDS; forebyggende og afhjælpende vedligehold med kundedokumentation.",
    "Enterprise- og projektstyring: planlægning og koordinering af tekniske arbejder, "
    "underentreprenører, KS og afleveringsdokumentation med fuldt P&L-ansvar.",
    "AI-værktøjer i Python og Claude API til tilbudsberegning, tidsplaner, KS-tjeklister "
    "og KPI-dashboards har givet over 40 % produktivitetsløft.",
])

job("Data Power Consultant ApS · København · Medejer og CTO for AI-afdelingen · 2024 – nov. 2026 (sideløbende med ELOHVAC)", [
    "Ansvarlig for AI- og AI coding-afdelingen med 4-10 personer; implementering af "
    "tekniske og industrielle applikationer fra kravafdækning til idriftsættelse og overdragelse.",
    "AI som værktøj i ledelsesarbejdet: ledelsesrapportering, beslutningsoplæg og "
    "KPI-analyse med fast struktur.",
    "AI-assisteret softwareudvikling med fælles standarder for AI-output; kundeløsninger "
    "med LLM-API'er og AI-agenter.",
    "Matrixledelse af to sideløbende organisationer med én samlet plan. Selskabet er "
    "ophørt i november 2026, og i dag drives kun ELOHVAC.",
])

job("Novo Nordisk A/S · Kalundborg og Bagsværd · Senior idriftsættelsesingeniør og projektleder, elsystem · nov. 2022 – jul. 2024", [
    "Tests og idriftsættelse: FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA med accepttest og "
    "nul kritiske afvigelser ved aflevering; tværfaglig ledelse af 25 specialister.",
    "Porteføljeansvar for 37 samtidige anlægs- og CAPEX-projekter (DKK 2–10 mio. pr. stk.) "
    "med fremdrift, økonomi og risici på tværs af engineering, indkøb og anlæg.",
    "El-tekniske anlæg: tavler og styring, UPS, nød- og panikbelysning, ABA/ABV og PDS; "
    "fejlfinding med A3, 5xHvorfor og Ishikawa; SAP ERP og månedsrapportering.",
    "40 % reduktion af energiomkostninger gennem PDCA-program.",
])

job("Ventek-Air · København · Projekt- og værkstedsleder · jan. 2022 – nov. 2022", [
    "11 samtidige anlægsprojekter (DKK 2–10 mio.) fra specifikation til formel aflevering, "
    "med daglig ledelse af 14-mands team, kapacitets- og fremdriftsstyring.",
    "Udbud og tilbud, underentreprenører, aftalegrundlag, sikkerhedsdokumentation og "
    "afleveringspakker.",
    "Daglige tavlemøder og flaskehalsanalyser; standardiserede arbejdsgange med markant "
    "løft i leveringsevnen.",
])

job("Biofos (Lynetten) · København · Vedligeholdelses- og driftsleder · aug. 2017 – jan. 2022", [
    "Drift og vedligehold af kritisk forsyningsanlæg med pumper, HVAC, højspændingstavler "
    "og SCADA-overvågning: oppetid, forebyggende vedligehold og akut fejlfinding 24/7.",
    "5S, Standard Work og PDCA på værksted og lager; reservedelsflow og lagerstyring.",
    "Skifteholdsdrift: LOTO, risikovurdering, APV og nærved-hændelser.",
])

job("ARJ Engineering · Teheran · Elektromekaniker og produktionsteamleder · dec. 2003 – mar. 2010", [
    "Fejldiagnose og reparation af industrielle el- og mekaniske anlæg; rodårsagsanalyse "
    "og korrigerende handlinger.",
    "Ledelse af 12 mekanikere og teknikere i maskinværksted med vagtplanlægning og "
    "materialestyring på en produktionslinje med elektromotorer, pumper og dykpumper.",
])

para("Uddannelse", style="CVH1")
bullet("Dansk elautorisation LV/MV/HV som elautoriseret maskinmester, Sikkerhedsstyrelsen, maj 2023.")
bullet("B.Tech (EQF6), teknologiledelse og maskinteknik, Copenhagen School of Marine Engineering & Technology Management, 2017–2022.")
bullet("El- og maskinteknisk design, elteknik (EQF6), Tehran Technical University, 2000–2003; HF, VUC, 2012–2017.")
bullet("Køleteknik og klimaanlæg (AMU), Mercantec, 2021. STCW-certifikater, Søfartsstyrelsen, 2021–2023.")
bullet("PRINCE2, certificeret projektleder (AXELOS/PeopleCert).")
bullet("Lean og Six Sigma: DMAIC, 5S, PDCA, VSM, A3, Kaizen, Standard Work, SMED, TPM, 5xHvorfor, Ishikawa og FMEA, arbejdet med i praksis, ikke certificeret.")

para("Kompetencer", style="CVH1")
bullet("Drift og vedligehold: daglig drift, overvågning og betjening af procesanlæg; "
       "forebyggende og afhjælpende vedligehold, planlægning og koordinering af "
       "tekniske arbejder, opfølgning på alarmer og driftsforstyrrelser.")
bullet("Fejlfinding: mekaniske, elektriske og procesmæssige komponenter; "
       "rodårsagsanalyse med A3, 5xHvorfor og Ishikawa.")
bullet("Optimering: løbende forbedring af drift og funktion med PDCA og Lean; målte "
       "resultater på energi og produktivitet.")
bullet("Tests og dokumentation: FAT/SAT og idriftsættelse, tests og forsøg; "
       "dokumentation af drift, ændringer og erfaringer, vidensdeling og oplæring.")
bullet("El og proces: el-tekniske anlæg, tavler og styring, SCADA, pumper og regulering; "
       "elautoriseret maskinmester med praktisk erfaring fra proces-, energi- og "
       "produktionsanlæg.")
bullet("Digitalt: Microsoft Office (Excel og Power Query), Python, Claude API og Claude "
       "Code, professionel og aktiv AI- og Claude-koder, Power BI.")
bullet("Sprog: dansk som modersmål, engelsk i skrift og tale.")
bullet("Betingelser: kørekort B og egen bil; bopæl i Måløv med kort vej til Amager.")

# ----------------------------- KVALITETSKONTROL -----------------------------
full = "\n".join(p.text for p in doc.paragraphs)
banned = ["spearheaded", "leveraged", "passionate", "dynamic", "results-driven",
          "proven track record", "synergy", "cutting-edge", "innovative solutions",
          "seamlessly", "robust", "demonstrated ability", "fast-paced",
          "drevet", "lidenskabelig", "dynamisk", "synergi", "banebrydende",
          "sømløst", "ikke kun", "men også", "\u2014", "passion"]
hits = [w for w in banned if w.lower() in full.lower()]
jd_words = ["projektingeniør", "co2-fangst", "demonstrationsanlæg", "drift", "overvågning",
  "betjening", "forebyggende", "vedligehold", "fejlfinding", "mekaniske", "elektriske",
  "proces", "planlægning", "koordinering", "alarmer", "driftsforstyrrelser", "optimering",
  "forbedring", "leverandør", "specialister", "dokumentation", "tests", "forsøg",
  "erfaringer", "teknisk viden", "fremtidige", "maskinmester", "ingeniør", "tekniker",
  "procesanlæg", "energi", "produktionsanlæg", "praktisk", "teknisk forståelse",
  "struktureret", "ansvar", "helt til dørs", "nysgerrig", "teknisk tilgængelighed",
  "sikker og stabil", "amager", "arc", "vidensdeling", "hands-on", "grøn"]
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
print(f"Brev ~{lb:.1f}/{CAP:.0f} \u2192 {'OK 1 side' if lb < CAP - 1 else 'RISIKO'}")
print(f"CV   ~{cv:.1f}/{2 * CAP:.0f} \u2192 {'OK 2 sider' if cv < 2 * CAP - 2 else 'RISIKO'}")

doc.save(OUT)
print("Gemte", OUT)
