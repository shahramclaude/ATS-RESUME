#!/usr/bin/env python3
"""Byg Shahram_Ajloo_Coor_DriftschefOperationsManager.docx (brev + CV i ét dokument)."""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_Coor_DriftschefOperationsManager.docx"

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
para("Ansøgning som Driftschef / Operations Manager, Coor Property", style="LetterTitle")
para("Kære Søren Klemmensen", after=4)

para("På en god arbejdsplads mærker ingen driften: varme, lys, adgang og teknik "
     "virker bare. Bag den ro ligger 30.000 servicebrugere i Danmark, kvadratmeter "
     "der skal passes, og en leverance, der skal holde hver eneste dag. Coor Property "
     "tager opgaven med at drive og optimere ejendommene, og driftschefens rolle er "
     "at få holdet, kunderne og økonomien til at spille sammen, så resultaterne "
     "skabes gennem mennesker.")

para("Rollens opgave er at skabe rammerne. Ledelsen går gennem teamledere med "
     "tydelige roller og forventninger, tillid, følgeskab og nærværende opfølgning, "
     "så medarbejderne har de bedste forudsætninger for at lykkes. Kunderelationerne "
     "skal holdes varme med forståelse for behov, opfølgning på aftaler, proaktive "
     "løsninger og en kundeoplevelse i stjerneklasse, og forretningen skal være sund "
     "og lønsom: budget, forecast, resultater og reaktion på afvigelser. Driften skal "
     "være velfungerende med overblik over kvalitet, leverancer, tekniske opgaver, "
     "sikkerhed og kontrakkrav, så vi holder det, vi lover, og samarbejdet med "
     "driftschefer, projektafdelingen, økonomi, HR og indkøb får brikkerne til at "
     "falde på plads. Udviklingen stopper ikke: gode idéer omsættes til konkrete "
     "forbedringer og mere værdi for kunden. Jeg skal ikke selv løse alle opgaverne i "
     "driften, men få andre til at lykkes.")

para("Jeg er maskinmester med håndværksmæssig baggrund som elektromekaniker og har "
     "i over 20 år bygget en bred ledelsesmæssig ballast for teknisk drift og service, "
     "både direkte og gennem teamledere "
     "med opfølgning på resultater. I ELOHVAC leder jeg et team af elektrikere og "
     "lærlinge og driver service og entrepriser med fuldt budget- og P&L-ansvar, "
     "aftaleopfølgning, kvalitet og sikkerhed i hverdagen. Tidligere har jeg ledet "
     "skifteholdsdrift døgnet rundt, 14-mands teams og 25 specialister på tværs af "
     "fagområder, og jeg ved, at drift, vedligehold, kvalitet og service først tæller, "
     "når det fungerer i praksis. Min erfaring med ejendomsdrift ligger i den tekniske "
     "del: bygningsinstallationer, energioptimering, vedligehold og serviceleverancer "
     "i en beslægtet verden til facility management. Jeg har blik for både detaljen og "
     "det større billede, fra fejlfinding i anlægget til økonomien i porteføljen, og "
     "prioriterer efter det, der flytter resultaterne. Med "
     "Python og Claude som professionel og aktiv koder kan jeg give hurtigt overblik "
     "over budget, forecast og afvigelser, og med Lean, PDCA og investeringsoverslag "
     "omsætter jeg idéer til konkrete forbedringer og et klart beslutningsgrundlag.")

para("Min plan for de første måneder er konkret. Efter 30 dage kender jeg "
     "driftsområdet: teamledere og medarbejdere, kunderne og kontrakterne, ejendommene "
     "udefra og indefra, og de aftaler for kvalitet, sikkerhed og opfølgning, der "
     "allerede virker. Efter 60 dage kører min faste rytme med teamledermøder, 1:1 og "
     "opfølgning på resultater mod fælles mål, kundemøder og budgetstatus med reaktion "
     "på afvigelser. Efter 90 dage ligger de første forbedringsforslag klar med "
     "tydelige gevinster for kunden, og jeg har lagt et oplæg for, hvordan AI kan give "
     "hurtigere overblik over økonomi og drift.")

para("Jeg bor i Måløv, få minutter fra Ballerup, og kender området. Lad os tale om, "
     "hvordan vi skaber en drift, som både medarbejdere og kunder er stolte af. Jeg "
     "kan træffes på +45 93 99 95 14.", after=6)

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
para("Jeg skaber stabil drift med tydelige roller og forventninger, tæt opfølgning "
     "og styr på økonomi, kvalitet og sikkerhed, så leverancen holder, og menneskerne "
     "udvikles. Maskinmester med håndværksmæssig baggrund og over 20 års erfaring med "
     "ledelse af teknisk drift og service, direkte og gennem teamledere.")

para("Erfaring", style="CVH1")

job("ELOHVAC ApS · København · Ejer og elautoriseret maskinmester · maj 2023 – nu", [
    "Personaleledelse af 5 elektrikere og 3 lærlinge med planlægning, 1:1, MUS og "
    "oplæring; ansvar for teamets resultater og udvikling.",
    "Service og entreprise med fuldt P&L-ansvar: tilbud og beregning, planlægning, "
    "materialestyring, underentreprenører, KS og afleveringsdokumentation.",
    "Installation, service og idriftsættelse af el-tekniske anlæg, tavler, styring, "
    "fiber og PDS med kundedokumentation.",
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
    "Drift og vedligehold af kritisk forsyningsanlæg med pumper, HVAC, højspændingstavler "
    "og SCADA: oppetid, forebyggende vedligehold og akut fejlfinding 24/7.",
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
bullet("Ledelse: personaleledelse direkte og gennem teamledere og mellemledere; tydelige "
       "roller og forventninger, prioritering og opfølgning på resultater, 1:1, MUS og "
       "udvikling af mennesker.")
bullet("Drift og service: teknisk drift, vedligehold, kvalitet og service; tekniske "
       "serviceleverancer, bygningsinstallationer og ejendomsteknik; kontrakkrav, "
       "leverancer og sikkerhed (APV, LOTO, risikovurdering).")
bullet("Økonomi og styring: budget, forecast, P&L og månedsrapportering; struktureret "
       "opfølgning på afvigelser, investeringsoverslag og business cases.")
bullet("Udvikling: Lean, PDCA og standardisering; forbedringsprojekter med målbare "
       "gevinster, herunder over 40 % produktivitetsløft og 40 % lavere energiomkostninger.")
bullet("Kunder: kunderelationer, aftaleopfølgning og kundeoplevelse; teknisk rådgivning "
       "og proaktive løsninger.")
bullet("Digitalt: Microsoft Office (Excel og Power Query), Python, Claude API og Claude "
       "Code, professionel og aktiv AI- og Claude-koder, Power BI.")
bullet("Sprog: dansk som modersmål, engelsk i skrift og tale.")
bullet("Betingelser: kørekort B og egen bil; bopæl i Måløv få minutter fra Ballerup.")

# ----------------------------- KVALITETSKONTROL -----------------------------
full = "\n".join(p.text for p in doc.paragraphs)
banned = ["spearheaded", "leveraged", "passionate", "dynamic", "results-driven",
          "proven track record", "synergy", "cutting-edge", "innovative solutions",
          "seamlessly", "robust", "demonstrated ability", "fast-paced",
          "drevet", "lidenskabelig", "dynamisk", "synergi", "banebrydende",
          "sømløst", "ikke kun", "men også", "\u2014"]
hits = [w for w in banned if w.lower() in full.lower()]
jd_words = ["driftschef", "operations manager", "driftsområde", "teamleder", "medarbejder",
  "kundeoplevelse", "økonomi", "udvikling", "resultater", "gennem mennesker", "relation",
  "tillid", "følgeskab", "nærværende", "tydelig", "struktureret", "overblik", "prioritere",
  "opfølg", "beslutning", "budget", "forecast", "sund", "lønsom", "kvalitet", "leverancer",
  "tekniske opgaver", "sikkerhed", "kontrakkrav", "forbedring", "idéer", "værdi",
  "samarbejde", "driftschefer", "projektafdeling", "indkøb", "teknisk drift", "ejendomsdrift",
  "facility management", "vedligehold", "service", "maskinmester", "håndværksmæssig",
  "ballast", "detaljen", "større billede", "ballerup", "fælles mål", "stjerneklasse",
  "stolte", "lykkes", "opgaverne i driften"]
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
