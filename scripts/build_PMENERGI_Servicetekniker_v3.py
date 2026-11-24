#!/usr/bin/env python3
"""Byg Shahram_Ajloo_PMENERGI_Servicetekniker.docx (brev + CV i ét dokument).
Servicetekniker, PM ENERGI A/S, Hedehusene.
23.11.2026: praktisk erfaring med dieselmotorer og generatoranlæg bekræftet ja (upinnet).
23.11.2026 (v2): ELOHVAC lukket nov. 2026; Data Power fortsætter med samme stilling +
AI-ansvar (CTO + elautoriseret maskinmester, el-teknik og ventilation); hele pakken med P&L,
personaleledelse (5+3) og akkord/opmåling følger med. Data Power først, ELOHVAC som historik.
23.11.2026 (v3): kandidaten er ikke længere medejer i Data Power; titlen er CTO for
AI-afdelingen og elautoriseret maskinmester med ansvar for el-teknik og ventilation.
"""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_PMENERGI_Servicetekniker_v3.docx"

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
para("Ansøgning som Servicetekniker til afdelingen i Hedehusene", style="LetterTitle")
para("Kære PM ENERGI", after=4)

para("Nødstrøm skal virke den dag, den bliver brug for: anlægget skal starte "
     "automatisk, når strømmen falder ud, og kunden skal kunne stole på, at nogen "
     "har styr på motor, styring og service hele vejen. Jeres 24-timers vagtordning "
     "og garanti for, at nødstrømmen altid er der, hviler på teknikere, der kan "
     "kontrollere og prøvekøre store generatorinstallationer, fejlsøge systematisk "
     "på el-diagrammer og styretavler og tage det forebyggende servicearbejde lige "
     "så alvorligt som akutte udkald, og jeres kunder har sjældent standardbehov. "
     "Jeg er maskinmester med håndværksmæssig baggrund som elektromekaniker, og jeg "
     "har praktisk kendskab til og interesse for dieselmotorer, generatorer og "
     "elektriske styringer.")

para("Opgaverne på Sjælland og Fyn matcher det, jeg har gjort i praksis. "
     "Systematisk fejlsøgning på el-diagrammer og styretavler har været en fast del "
     "af arbejdet fra fejldiagnose og reparation af industrielle el- og mekaniske "
     "anlæg i ARJ Engineering over el-tekniske anlæg med tavler og styring, UPS og "
     "ABA/ABV hos Novo Nordisk til installation, service og forebyggende "
     "vedligehold af el, ventilations- og klimaanlæg i ELOHVAC; samme type "
     "opgaver fortsætter nu hos Data Power Consultant ApS. Kontrol, "
     "prøvekørsel og afprøvning før aflevering kender jeg fra tests og "
     "idriftsættelse med FAT/SAT og IQ/OQ og accepttest uden kritiske afvigelser, "
     "og når fejlen skal findes og ikke gættes, arbejder jeg med rodårsagsanalyse "
     "i A3, 5xHvorfor og Ishikawa.")

para("Kunden er i centrum i det servicearbejde, jeg kender: jeg har været i "
     "servicevirksomhed med faste kunder, aftaler og opfølgning på responstid, "
     "kvalitet og leveringsevne, og jeg ved, at klar kommunikation undervejs er "
     "det, der skaber det langsigtede samarbejde og kundetilfredsheden. Jeg er en "
     "holdspiller, der bidrager til arbejdsmiljøet med godt humør, og jeg trives "
     "med selvstændigt ansvar i komplekse situationer, hvor overblik og struktur "
     "er afgørende, og med den flade struktur, hvor en idé bliver til handling, og "
     "hvor man siger det, hvis man ser en fejl eller har en idé til forbedring. "
     "Kvalitetsbevidsthed, dokumentation og en fleksibel tilgang til løsning og koordinering af opgaver er en "
     "selvfølge i mit arbejde.")

para("De første 30 dage vil jeg tage godt imod introduktion og sidemandsoplæring "
     "og komme med ud på anlæggene, så jeg lærer kunderne, serviceaftalerne og "
     "anlæggene at kende. Derefter tager jeg selvstændigt serviceopgaver med "
     "kontrol, prøvekørsel, fejlsøgning og forebyggende service, og i løbet af de "
     "første tre måneder vil jeg bidrage med forslag til, hvordan service og "
     "procedurer kan blive bedre, og dele viden med kollegerne.")

para("Jeg har kørekort B og er vant til at være ude hos kunderne, og servicebilen "
     "passer mig fint. Jeg bor i Måløv med kort vej til Hedehusene og kan tiltræde "
     "efter aftale. Lad os tale om, hvordan jeg kan være med til at holde kundernes "
     "anlæg stabilt kørende med den driftssikkerhed, PM ENERGI står for. Jeg kan træffes "
     "på +45 93 99 95 14.")

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
para("Elautoriseret maskinmester med håndværksmæssig baggrund som elektromekaniker, "
     "praktisk erfaring med dieselmotorer og generatoranlæg og erfaring med "
     "el-diagrammer, styretavler og systematisk fejlsøgning. Arbejder med kontrol, "
     "prøvekørsel, fejlfinding og forebyggende service med kunden i centrum og "
     "dokumentation, der følger anlægget.")

para("Erfaring", style="CVH1")

job("Data Power Consultant ApS · København · CTO for AI-afdelingen og elautoriseret maskinmester med ansvar for el-teknik og ventilation · 2024 – nu", [
    "El-teknik og ventilation: ansvarlig for el-tekniske opgaver, tavler, styring samt "
    "ventilations- og klimaanlæg; installation, service og idriftsættelse, forebyggende og "
    "afhjælpende vedligehold med kundedokumentation, fra akutte udkald til afleveret anlæg "
    "(fortsat fra ELOHVAC, som lukkede i november 2026).",
    "Entreprise og personale: entreprise- og projektstyring med fuldt P&L-ansvar, "
    "underentreprenører, KS og afleveringsdokumentation; personaleledelse af 5 elektrikere og "
    "3 lærlinge; akkordbreve, opmåling og regulering af mer- og mindrearbejde.",
    "Ansvarlig for AI- og AI coding-afdelingen med 4-10 personer; implementering af "
    "tekniske og industrielle applikationer fra kravafdækning til idriftsættelse og overdragelse.",
    "AI som værktøj i ledelsesarbejdet: ledelsesrapportering, beslutningsoplæg og "
    "KPI-analyse med fast struktur.",
    "AI-assisteret softwareudvikling med fælles standarder for AI-output; kundeløsninger "
    "med LLM-API'er og AI-agenter.",
    "Matrixledelse af to sideløbende organisationer med én samlet plan (2024 – nov. 2026, "
    "mens ELOHVAC kørte sideløbende).",
])

job("ELOHVAC ApS · København · Ejer og elautoriseret maskinmester · maj 2023 – nov. 2026", [
    "Installation, service og idriftsættelse af el-tekniske anlæg, tavler, styring "
    "samt ventilations- og klimaanlæg; forebyggende og afhjælpende vedligehold med "
    "kundedokumentation, fra akutte udkald til afleveret anlæg.",
    "Entreprise- og projektstyring: planlægning og koordinering af tekniske "
    "arbejder, underentreprenører, KS og afleveringsdokumentation med fuldt "
    "P&L-ansvar.",
    "AI-værktøjer i Python og Claude API til tilbudsberegning, tidsplaner, "
    "KS-tjeklister og KPI-dashboards har givet over 40 % produktivitetsløft.",
])

job("Novo Nordisk A/S · Kalundborg og Bagsværd · Senior idriftsættelsesingeniør og projektleder, elsystem · nov. 2022 – jul. 2024", [
    "El-tekniske anlæg: tavler og styring, UPS, nød- og panikbelysning, ABA/ABV og PDS; "
    "fejlfinding med A3, 5xHvorfor og Ishikawa; SAP ERP og månedsrapportering.",
    "Tests og idriftsættelse: FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA med accepttest og "
    "nul kritiske afvigelser ved aflevering; tværfaglig ledelse af 25 specialister.",
    "Porteføljeansvar for 37 samtidige anlægs- og CAPEX-projekter (DKK 2–10 mio. pr. stk.) "
    "med fremdrift, økonomi og risici på tværs af engineering, indkøb og anlæg.",
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
bullet("Anlæg: dieselmotorer, generatoranlæg og elektriske styringer; styretavler og "
       "tavleinstallationer, UPS, ABA/ABV, PDS og SCADA.")
bullet("Fejlsøgning: systematisk fejlsøgning på el-diagrammer; rodårsagsanalyse "
       "(A3, 5xHvorfor, Ishikawa); akut reparation og fejlfinding på el og mekanik.")
bullet("Service og vedligehold: forebyggende service og vedligehold, kontrol, drift og "
       "prøvekørsel; FAT/SAT og accepttest før aflevering.")
bullet("Kunder: kundedialog og servicevirksomhed med aftaler og opfølgning på responstid, "
       "kvalitet og leveringsevne; kunden i centrum.")
bullet("Kvalitet og sikkerhed: KS, dokumentation, LOTO, APV og risikovurdering.")
bullet("Teknik: el-tekniske anlæg, ventilations- og klimaanlæg, pumper og mekaniske systemer.")
bullet("Digitalt: Power BI, Excel/Power Query, Python og Claude Code; automatiseret rapportering.")
bullet("Sprog: dansk og engelsk, skrift og tale.")
bullet("Betingelser: kørekort B; bosiddende i Måløv med kort vej til Hedehusene; Sjælland "
       "og Fyn; tiltrædelse efter aftale.")

# ----------------------------- KVALITETSKONTROL -----------------------------
full = "\n".join(p.text for p in doc.paragraphs)
banned = ["spearheaded", "leveraged", "passionate", "dynamic", "results-driven",
          "proven track record", "synergy", "cutting-edge", "innovative solutions",
          "seamlessly", "robust", "demonstrated ability", "fast-paced",
          "drevet", "lidenskabelig", "dynamisk", "synergi", "banebrydende",
          "sømløst", "ikke kun", "men også", "\u2014", "passion"]
hits = [w for w in banned if w.lower() in full.lower()]
jd_words = ["servicetekniker", "maskinmester", "håndværksmæssig", "dieselmotorer",
  "generatorer", "generatoranlæg", "elektriske styringer", "el-diagrammer",
  "systematisk", "fejlsøgning", "styretavler", "tavleinstallationer", "forebyggende",
  "service", "prøvekørsel", "kontrol", "drift", "kunden", "kommunikation",
  "holdspiller", "kvalitets", "stabil", "fleksibel", "dansk", "engelsk", "kørekort",
  "servicebil", "sjælland", "fyn", "hedehusene", "introduktion", "sidemandsoplæring",
  "selvstændigt", "overblik", "struktur", "komplekse", "driftssikkerhed",
  "kundetilfredshed", "UPS", "nødstrøm", "dokumentation", "arbejdsmiljø",
  "forbedring", "viden", "fejlfinding", "vedligehold", "måløv", "30 dage",
  "tre måneder", "el-tekniske", "tavler", "elektromekaniker", "data power"]
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

doc.save(OUT)
print("Gemte", OUT)
