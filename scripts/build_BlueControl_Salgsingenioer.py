#!/usr/bin/env python3
"""Byg Shahram_Ajloo_BlueControl_SalgsingenioerTeknikSaelger.docx (brev + CV i ét dokument)."""
import re
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_BlueControl_SalgsingenioerTeknikSaelger.docx"

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

st_name   = _mkstyle("CVName", 16, True)
st_h1     = _mkstyle("CVH1", 12, True)
st_job    = _mkstyle("CVJob", 10.5, True)
st_title  = _mkstyle("LetterTitle", 11, True)
for s_ in (st_h1,):
    s_.paragraph_format.space_before = Pt(8); s_.paragraph_format.space_after = Pt(2)
st_job.paragraph_format.space_before = Pt(6); st_job.paragraph_format.space_after = Pt(1)
st_name.paragraph_format.space_after = Pt(1)
st_title.paragraph_format.space_after = Pt(6)

def para(text, bold_prefix=None, style=None, after=None, align=None):
    p = doc.add_paragraph(style=style)
    if bold_prefix:
        r = p.add_run(bold_prefix); r.bold = True
    if text:
        p.add_run(text)
    if after is not None:
        p.paragraph_format.space_after = Pt(after)
    if align:
        p.alignment = align
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
        if isinstance(b, tuple):
            bullet(b[1], bold_prefix=b[0])
        else:
            bullet(b)

# ----------------------------- BREV -----------------------------
para("Måløv, den 23. november 2026", after=2)
para("Ansøgning som Salgsingeniør/teknisk sælger, Blue Control", style="LetterTitle")
para("Kære Gert Vesterlund", after=4)

para("På et lille dansk vandværk er ønsket det samme hver dag: så der næsten "
     "altid er vand i hanerne. Men anlæggene bliver ældre, beredskabsbekendtgørelsen "
     "stiller nye krav til beredskabsplan, cybersikkerhed og fysisk sikring, og der "
     "er stadig flere opgaver på de små og mellemstore værker. Blue Controls svar er "
     "ét samlet SRO-anlæg på standardkomponenter, der giver overblik over indvinding, "
     "filtrering, udpumpning "
     "og rapportering, og den tryghed skal kunne forklares, så både driftslederen og "
     "bestyrelsen på værket mærker værdien.")

para("Rollens opgave er at bygge relationer og tillid: identificere og kontakte "
     "nye vandværker og forsyningsselskaber, holde kundemøder og rådgive om de rette "
     "tekniske løsninger, følge salgsprocessen fra første gennemgang på værket til "
     "løsningsforslag med komponentliste, pris og tidsplan og følge tilbuddet til "
     "dørs. Dertil messer og kundearrangementer, bidrag til salgsindsatsen og "
     "markedspositionen, tæt sparring med dig om forretningen og på sigt "
     "projektledelse af udvalgte kundeløsninger. Teknikken er ikke til pynt: den "
     "skal omsættes til værdi for det enkelte værk.")

para("Jeg er maskinmester med elautorisation og elektriker i bunden, og jeg har "
     "stået for drift af forsyningsanlæg med pumper, styring, overvågning og SCADA "
     "døgnet rundt. Det betyder, at jeg kan tale anlæg med driftslederen og gevinst "
     "med bestyrelsen i samme møde. Opsøgende salg har jeg selv stået for: "
     "identificeret og kontaktet nye kunder og bygget kundeporteføljen op fra bunden, "
     "og jeg har "
     "fulgt tilbud hele vejen til aftale med beregning, tilbudsdokumentation og "
     "kundedialog. Som professionel og aktiv Claude-koder med Python kan jeg samle "
     "tilbuddene i faste skabeloner og udvikle beregningsmodeller, der gør det nemt "
     "for kunden at se økonomien i at investere i et nyt anlæg.")

para("Min plan for de første måneder er konkret. Første 30 dage går med produktet "
     "og markedet: BC 7000 og BC 9000, gennemgangsmetoden og de fire løfter, "
     "samtaler med kollegerne og de første ture ud på værkerne sammen med dig eller "
     "salgschefen. Fra dag 30 tager jeg selv fat i kunderne ud fra projekt- og "
     "aktivitetslisterne, holder møder, skriver de første tilbud og lægger et enkelt "
     "pipeline-overblik med fast opfølgning. Fra dag 60 kører min egen "
     "kundeportefølje, og jeg afleverer et forslag til, hvordan AI kan gøre "
     "tilbudsgangen hurtigere og mere ensartet, så tiden går til kunderne.")

para("Jeg bor i Måløv, har kørekort og bil, og der er kort vej til Birkerød; "
     "hjemmearbejde efter aftale passer mig fint. Lad os tage en samtale om, "
     "hvordan salget til de danske vandværker skal bygges op i fællesskab. Jeg kan "
     "træffes på +45 93 99 95 14.", after=6)

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
para("Shahram Ajloo", style="st_name" if False else "CVName", after=1)
para("Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo", after=6)

para("Profil", style="CVH1")
para("Jeg hjælper tekniske virksomheder med at finde, vinde og fastholde kunder, så "
     "komplekse løsninger bliver forklaret enkelt og solgt med et tilbud, der holder "
     "hele vejen. Maskinmester med elautorisation, praktisk SCADA- og "
     "automationsbaggrund fra forsyningssektoren og erfaring med opsøgende salg, "
     "kundedialog og tilbudsberegning.")

para("Erfaring", style="CVH1")

job("ELOHVAC ApS · København · Ejer og elautoriseret maskinmester · maj 2023 – nu", [
    "Tilbud, beregning og kundedialog: tilbud fra specifikation og kundebesøg til "
    "aftale, med nysalg og opfølgning hele vejen til aflevering og kundeintroduktion.",
    "Enterprise- og projektstyring: planlægning, materialestyring, underentreprenører, "
    "KS og afleveringsdokumentation med fuldt P&L-ansvar.",
    "Installation og idriftsættelse af el-tekniske anlæg, tavler, styring, fiber og "
    "PDS til afleveret anlæg med kundedokumentation.",
    "Personaleledelse af 5 elektrikere og 3 lærlinge med planlægning, 1:1, MUS og oplæring.",
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
    "Porteføljeansvar for 37 samtidige anlægs- og CAPEX-projekter (DKK 2–10 mio. pr. stk.) "
    "med fremdrift, økonomi og risici på tværs af engineering, indkøb og anlæg.",
    "FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA med nul kritiske afvigelser ved aflevering; "
    "tværfaglig ledelse af 25 højt specialiserede medarbejdere.",
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
    "Drift af kritisk forsyningsanlæg med pumper, HVAC, højspændingstavler og SCADA: "
    "oppetid, forebyggende vedligehold og akut fejlfinding 24/7.",
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
bullet("Salg og kunderelationer: opsøgende salg og kanvas med identificering og kontakt af "
       "nye kunder, egen kundeportefølje, kundekontakt, kundemøder og rådgivning, tilbud "
       "og forhandling, salgsprocesser fra første kontakt til aftale; nysalg og kundeudvikling.")
bullet("Teknik: SRO/SCADA, drift og idriftsættelse, pumper, regulering og optimering, "
       "el-tekniske anlæg, tavler og styring, automation; erfaring fra forsyningssektoren "
       "og teknisk salg og rådgivning.")
bullet("Formidling: komplekse emner forklaret enkelt, teknisk rådgivning, kundeintroduktion "
       "og oplæring.")
bullet("Økonomi: tilbudsberegning, budget, business cases og investeringsoverslag.")
bullet("Digitalt: Microsoft Office (Excel og Power Query) og andre digitale værktøjer: "
       "Python, Claude API og Claude Code, professionel og aktiv AI- og Claude-koder, Power BI.")
bullet("Sprog: dansk som modersmål, engelsk i skrift og tale.")
bullet("Betingelser: kørekort B og egen bil; bopæl i Måløv med kort vej til Birkerød; "
       "hjemmearbejde efter aftale.")

# ----------------------------- KVALITETSKONTROL -----------------------------
full = "\n".join(p.text for p in doc.paragraphs)
banned = ["spearheaded", "leveraged", "passionate", "dynamic", "results-driven",
          "proven track record", "synergy", "cutting-edge", "innovative solutions",
          "seamlessly", "robust", "demonstrated ability", "fast-paced",
          "drevet", "lidenskabelig", "dynamisk", "synergi", "banebrydende",
          "sømløst", "ikke kun", "men også", "\u2014"]
hits = [w for w in banned if w.lower() in full.lower()]
jd_words = ["salgsingeniør", "teknisk sælger", "relation", "tillid", "kundekontakt",
  "opsøgende", "kundemøde", "rådgiv", "tilbud", "salgsprocess", "dørs", "messer",
  "kundearrangement", "salgsindsats", "markedsposition", "projektledelse", "vandværk",
  "forsyningsselskab", "tekniske løsninger", "komplekse", "microsoft office",
  "digitale værktøjer", "dansk", "engelsk", "sro", "scada", "styring", "overvågning",
  "optimering", "automation", "forsyning", "teknisk salg", "fællesskab", "birkerød",
  "hjemmearbejde", "tryghed", "overblik", "standardkomponent", "kundedialog",
  "omsættes", "værdi", "gennemgang", "løsningsforslag", "komponentliste", "sparring",
  "forretning", "maskinmester", "kørekort", "kanvas"]
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
