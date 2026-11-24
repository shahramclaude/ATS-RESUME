#!/usr/bin/env python3
"""Byg Shahram_Ajloo_GiGroup_SeniorLabEngineer.docx (brev + CV i ét dokument).
Senior Lab Engineer, Gi Group (anonym kunde, Storkøbenhavn).
23.11.2026: SLA/SOW bekræftet ja (upinnet i Kompetencer + brev); kunde ukendt.
"""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_GiGroup_SeniorLabEngineer.docx"

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
para("Ansøgning som Senior Lab Engineer til kritisk laboratorieinfrastruktur", style="LetterTitle")
para("Kære Gi Group", after=4)

para("Kritiske laboratorieinstallationer er en forudsætning for arbejdet, ikke en "
     "støttefunktion: når VVS, el, styring, varme, ventilation og kører stabilt, "
     "kan forskere, specialister og eksterne samarbejdspartnere arbejde videre, og "
     "når noget stopper, tæller hurtig og præcis handling. Den rolle, I beskriver, "
     "er ikke en traditionel driftsrolle, men kombinationen af teknisk "
     "specialistviden, projektledelse og sparring med højt specialiserede brugere, "
     "der skal omsættes til praktiske, holdbare løsninger.")

para("Fra stabil drift og forebyggende vedligehold over fejlfinding, årsagsanalyse "
     "og akut reparation til optimering af kapacitet, energieffektivitet, "
     "driftssikkerhed og oppetid kender jeg hele kæden fra miljøer, hvor nedetid "
     "ikke var en mulighed. I Biofos stod jeg for driften af et kritisk "
     "forsyningsanlæg med pumper, HVAC, højspændingstavler og SCADA-overvågning "
     "døgnet rundt: forebyggende vedligehold, reservedelsflow og lagerstyring og "
     "akut fejlfinding på tværs af mekanik, el og proces. I Novo Nordisk arbejdede "
     "jeg med el-tekniske anlæg i et GMP-reguleret miljø, hvor inspektioner og "
     "idriftsættelser blev gennemgået og godkendt efter FAT/SAT og IQ/OQ under "
     "FDA- og EMA-krav, og hvor tavler og styring, UPS, ABA/ABV og PDS var en del "
     "af hverdagen. I ELOHVAC arbejder jeg med el, ventilations- og klimaanlæg for "
     "erhvervskunder, fra akutte udkald til afleveret anlæg.")

para("På styringssiden har jeg styret leverandører og underentreprenører med klare "
     "aftaler, opgavespecifikationer og opfølgning på SLA, KPI, kvalitet og "
     "leverancer, og jeg har arbejdet med økonomien omkring tekniske anlæg: i Novo "
     "Nordisk var 37 samtidige anlægs- og CAPEX-projekter en del af hverdagen, og "
     "jeg har udarbejdet budgetter, business cases og beslutningsoplæg ved "
     "investeringer og tekniske opgraderinger. Jeg omsætter komplekse tekniske "
     "forhold til korte, evidensbaserede anbefalinger og sparrer med interessenter "
     "om nye installationer og ændringer. Min tilgang er pragmatisk og analytisk: "
     "jeg går selv i detaljen, når det er nødvendigt, og bruger PDCA, "
     "rodårsagsanalyse og digitale værktøjer som Claude Code og Python til "
     "driftsdata, når det gør arbejdet bedre.")

para("De første 30 dage vil jeg sætte mig ind i de kritiske systemer, "
     "vedligeholdsplaner, arbejdsordrer og leverandøraftaler, så jeg hurtigt kan "
     "bidrage til driften. Derefter tager jeg selvstændigt ansvar for den løbende "
     "opfølgning på vedligehold, inspektioner og SLA/KPI, og i løbet af de første "
     "tre måneder vil konkrete forslag til bedre oppetid, energieffektivitet, "
     "metoder og standarder ligge klar, også til videndeling og coaching på tværs.")

para("Jeg er vant til at samarbejde med både teknikere, ledelse og højt "
     "specialiserede brugere, og jeg skaber tillid gennem faglig tyngde og en "
     "pragmatisk tilgang. Jeg tager naturligt ejerskab for mine ansvarsområder, og "
     "jeg er handlekraftig, når noget skal løses her og nu, og nysgerrig efter at "
     "forstå systemerne i dybden. Samtalen på engelsk er ikke en hindring. Jeg bor "
     "i Måløv med kort vej til Storkøbenhavn og kan tiltræde efter aftale. Lad os "
     "tale om, hvordan jeg kan tage ansvar for, at laboratoriets kritiske systemer "
     "fungerer stabilt og sikkert. Jeg kan træffes på +45 93 99 95 14.")

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
para("Elautoriseret maskinmester med erfaring fra kritiske driftsmiljøer inden for "
     "pharma og forsyning, hvor HVAC, el, pumper og automatiske anlæg skal køre "
     "stabilt med høj oppetid. Arbejder med forebyggende vedligehold, fejlfinding, "
     "leverandørstyring og optimering af driftssikkerhed, energieffektivitet og "
     "omkostninger og omsætter komplekse tekniske problemstillinger til praktiske "
     "løsninger.")

para("Erfaring", style="CVH1")

job("ELOHVAC ApS · København · Ejer og elautoriseret maskinmester · maj 2023 – nu", [
    "Installation, service og idriftsættelse af el-tekniske anlæg, tavler, styring "
    "samt ventilations- og klimaanlæg; forebyggende og afhjælpende vedligehold med "
    "kundedokumentation, fra akutte udkald til afleveret anlæg.",
    "Entreprise- og projektstyring: planlægning og koordinering af tekniske "
    "arbejder, underentreprenører, KS og afleveringsdokumentation med fuldt "
    "P&L-ansvar.",
    "AI-værktøjer i Python og Claude API til tilbudsberegning, tidsplaner, "
    "KS-tjeklister og KPI-dashboards har givet over 40 % produktivitetsløft.",
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
bullet("Kritiske driftsmiljøer: pharma under GMP/FDA/EMA og kritisk forsyning; driftssikkerhed, "
       "oppetid, compliance, arbejdsmiljø, LOTO, APV og risikovurdering.")
bullet("Installationer: HVAC (varme, ventilation og køling), el, styring og automatik, pumper, "
       "forsyningsanlæg, SCADA, ABA/ABV (brandalarm), UPS og PDS.")
bullet("Vedligehold og fejlfinding: forebyggende vedligehold, arbejdsordrer, reservedelsflow, "
       "lager- og materialestyring; akut reparation, nødvedligehold og årsagsanalyse "
       "(A3, 5xHvorfor, Ishikawa).")
bullet("Leverandørstyring: underentreprenører, SOW, SLA og KPI-opfølgning på responstid, "
       "kvalitet og leveringsevne.")
bullet("Økonomi: P&L og budgetansvar, omkostningsstyring, OPEX og CAPEX, business cases "
       "og beslutningsoplæg.")
bullet("Projektledelse: PRINCE2, portefølje, fremdrift, risici og ressourcer, "
       "interessenthåndtering og sparring om nye installationer og ændringer.")
bullet("Digitalt: SAP ERP, CMMS, Power BI, Excel/Power Query, Python og Claude Code; "
       "automatiseret rapportering.")
bullet("Sprog: dansk og engelsk, skrift og tale.")
bullet("Certificeringer: elautorisation LV/MV/HV, PRINCE2, Køleteknik og klimaanlæg (AMU) "
       "og STCW; Lean og Six Sigma er arbejdet med i praksis, ikke certificeret.")
bullet("Betingelser: bosiddende i Måløv; Storkøbenhavn; tiltrædelse efter aftale.")

# ----------------------------- KVALITETSKONTROL -----------------------------
full = "\n".join(p.text for p in doc.paragraphs)
banned = ["spearheaded", "leveraged", "passionate", "dynamic", "results-driven",
          "proven track record", "synergy", "cutting-edge", "innovative solutions",
          "seamlessly", "robust", "demonstrated ability", "fast-paced",
          "drevet", "lidenskabelig", "dynamisk", "synergi", "banebrydende",
          "sømløst", "ikke kun", "men også", "\u2014", "passion"]
hits = [w for w in banned if w.lower() in full.lower()]
jd_words = ["senior lab engineer", "kritisk", "laboratorie", "drift", "vedligehold",
  "optimering", "VVS", "el", "styring", "automatik", "varme", "ventilation", "køling",
  "compliance", "arbejdsmiljø", "sikkerhed", "standarder", "driftsdata",
  "energieffektivitet", "driftssikkerhed", "oppetid", "fejlfinding", "årsagsanalyse",
  "nødvedligehold", "arbejdsordrer", "reservedels", "lager", "leverandør", "entreprenør",
  "SLA", "KPI", "SOW", "inspektion", "brandalarm", "HVAC", "budgetansvar", "omkostningsstyring",
  "OPEX", "CAPEX", "business cases", "beslutningsoplæg", "evidensbaserede", "videndeling",
  "coaching", "maskinmester", "dansk", "engelsk", "certificering", "analytisk",
  "handlekraftig", "nysgerrig", "pragmatisk", "faglig tyngde", "selvstændigt", "tillid",
  "komplekse", "holdbare", "storkøbenhavn", "måløv", "30 dage", "tre måneder", "P&L",
  "investeringer", "ressource"]
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
