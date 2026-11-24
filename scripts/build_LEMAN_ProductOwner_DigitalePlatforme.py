#!/usr/bin/env python3
"""Build Shahram_Ajloo_LEMAN_ProductOwner_DigitalePlatforme.docx (brev + CV).
Product Owner, kundevendte digitale platforme, LEMAN (Group IT/Digital; Greve; deadline
4/12 kl. 12:00; 2 remote-udviklere; 5-10 rejsedage/aar; ingen navngiven kontakt).
Dansk dokument. 23.11.2026 brugerbekræftelser (upinnet): Product Ownership/Management =
konkret; Agile + backlog/roadmap-vaerktoejer = konkret (ingen specifikke tool-navne
paaastaaet); logistik = kun kompleks B2B (GMP-broen til LEMAN Pharma bruges).
ADVARSEL: ordet driven/drevet er FORBUDT selv som verbum - LEMAN-sloganet citeres aldrig.
Career: Data Power foerst (kanonisk, ingen medejer)."""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_LEMAN_ProductOwner_DigitalePlatforme.docx"

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
para("Ansøgning som Product Owner for kundevendte digitale platforme, LEMAN",
     style="LetterTitle")
para("Kære LEMAN", after=4)

para("En kunde, der booker en forsendelse sent om aftenen, mærker med det samme "
     "forskellen på en platform, der bare virker, og en der ikke gør. Her bliver digital "
     "kundeoplevelse til forretningsværdi, og netop det bindeled mellem kunder, "
     "forretning og teknik er kernen i stillingen som Product Owner hos jer. Jeg er "
     "maskinmester og CTO for en AI-afdeling, hvor jeg har produktansvar for digitale "
     "løsninger fra kravspecifikation til lancering, og hvor kundernes oplevede forskel "
     "er målet for hver eneste release.")

para("Product Ownership og Product Management er konkret erfaring for mig: "
     "produktvision og roadmap for "
     "kundevendte løsninger, backlog prioriteret efter kunde- og forretningsværdi og "
     "udvikling fulgt fra idé til lancering og videre til løbende forbedringer. Jeg "
     "arbejder Agile med udviklere både i samme rum og på distancen, med daglige "
     "tavlemøder, iterationer og strukturerede prioriteringer i backlog- og "
     "roadmap-værktøjer, og jeg kender vilkårene for et lille, dedikeret team. "
     "AI-muligheder, der forbedrer kundeoplevelsen, er mit daglige arbejde: LLM-API'er, "
     "AI-agenter og kundeløsninger, der gør det enklere at være kunde.")

para("At koble kundeoplevelse, forretningsværdi og tekniske muligheder har været mit "
     "ansvar i snart to årtier: fra komplekse B2B-leverancer og kundeprojekter til fuldt "
     "P&L-ansvar, hvor hver prioritering skulle hænge sammen kommercielt. Jeg skaber "
     "relationer og involverer stakeholders på tværs af Commercial, Operations og IT, og "
     "jeg træffer beslutninger, når forskellige prioriteter skal mødes. Min "
     "GMP-erfaring fra Novo Nordisk er relevant for jer: LEMAN er GDP/GMP-certificeret "
     "til farmaceutisk logistik, og jeg taler den dokumentationsdisciplin, jeres "
     "farmakunder kender.")

para("De første 30 dage vil jeg bruge på kunderne og platformen: kunderejsen, data og "
     "produktperformance og de vigtigste stakeholders i Commercial og Operations. Efter "
     "60 dage vil jeg eje roadmap og backlog for de kundevendte platforme med en tydelig "
     "prioriteret retning, og efter 90 dage vil de første AI-baserede forbedringer af "
     "kundeoplevelsen være sat i værk med målbare resultater.")

para("Jeg er bosat i Måløv, de 5-10 rejsedage om året passer mig, og arbejde på dansk "
     "og engelsk er en selvfølge. Jeg kan tiltræde efter opsigelse, og jeg ser frem til "
     "en samtale om at sætte retningen for kundernes digitale møde med LEMAN. Jeg kan "
     "træffes på +45 93 99 95 14.")

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
para("Maskinmester (B.Tech) og CTO for en AI-afdeling med konkret erfaring inden for "
     "Product Ownership og digital produktudvikling: produktvision, roadmap og backlog "
     "prioriteret fra idé til lancering, og AI-implementeringer (LLM-API'er, AI-agenter), "
     "der forbedrer kundeoplevelsen. Forener teknisk forståelse med forretningsansvar "
     "(fuldt P&L), kobler kundeoplevelse, forretningsværdi og tekniske muligheder og "
     "skaber fremdrift på tværs af stakeholders i komplekse B2B-miljøer.")

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
bullet("Produktansvar og ejerskab: produktvision og roadmap for kundevendte digitale "
       "platforme "
       "(konkret erfaring); kunde- og forretningsbehov omsat til features og "
       "produktkrav; backlog prioriteret fra idé til lancering og løbende forbedringer.")
bullet("Teknik og AI: stærk teknisk forståelse; AI-implementeringer i praksis "
       "(LLM-API'er, AI-agenter, Python og Claude); Agile-erfaring med backlog- og "
       "roadmap-værktøjer, daglige tavlemøder og iterationer.")
bullet("Kundeoplevelse og forretning: kundeoplevelse, forretningsværdi og tekniske "
       "muligheder koblet i konkrete løsninger; feedback, data og produktperformance "
       "brugt til at sætte retningen; kompleks B2B som kontekst.")
bullet("Samarbejde og beslutninger: relationer skabt på tværs af Commercial, Operations "
       "og IT; stakeholders involveret med respekt for forskellige prioriteter; "
       "beslutninger truffet med fremdrift for øje; erfaring med remote udviklingsteams.")
bullet("AI-muligheder: identificeret og realiseret til forbedret kundeoplevelse og "
       "stærkere digitale løsninger.")
bullet("Branchekendskab: kompleks B2B (enterprise-kunder, tekniske leverancer); "
       "GMP-dokumentationsdisciplin fra Novo Nordisk, relevant for GDP/GMP-certificeret "
       "farmalogistik.")
bullet("Ledelse og styring: team på 4-10 specialister; 25 specialister på tværs af "
       "faggrupper; projekt- og porteføljestyring (37 parallelle projekter).")
bullet("Sprog og vilkår: dansk og engelsk (arbejdssproget er delvist engelsk); 5-10 "
       "rejsedage om året; bosat i Måløv; start efter opsigelse.")

# ----------------------------- KVALITETSKONTROL -----------------------------
full = "\n".join(p.text for p in doc.paragraphs)
banned = ["spearheaded", "leveraged", "passionate", "dynamic", "results-driven",
          "proven track record", "synergy", "cutting-edge", "innovative solutions",
          "seamlessly", "robust", "demonstrated ability", "fast-paced",
          "drevet", "lidenskabelig", "dynamisk", "synergi", "banebrydende",
          "sømløst", "ikke kun", "men også", "\u2014", "passion"]
hits = [w for w in banned if w.lower() in full.lower()]
jd_words = ["product owner", "product ownership", "product management", "produktvision",
  "roadmap", "backlog", "features", "produktkrav", "idé", "lancering", "agile", "ai",
  "kundeoplevelse", "forretningsværdi", "tekniske muligheder", "stakeholders",
  "commercial", "operations", "it", "feedback", "data", "produktperformance",
  "produktudvikling", "digital", "platforme", "kunder", "relationer", "beslutninger",
  "remote", "rejsedage", "engelsk", "fremdrift", "prioriteret", "kompleks b2b", "b2b",
  "ejerskab", "løsninger", "teknisk forståelse"]
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
