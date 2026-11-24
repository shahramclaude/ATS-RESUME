#!/usr/bin/env python3
"""Byg Shahram_Ajloo_Vestforbraending_Udbudskonsulent.docx (brev + CV i ét dokument)."""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_Vestforbraending_Udbudskonsulent.docx"

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
para("Ansøgning som Udbudskonsulent, Vestforbrænding", style="LetterTitle")
para("Kære Stefan Hauger-Rosendahl", after=4)

para("Når 19 kommuner og en million borgere ejer forsyningen, bliver hvert udbud et "
     "strategisk valg for både økonomi og miljø. Vestforbrænding står midt i "
     "varmeplan 2030 og fjernvarme til flere, CO2-fangst og målet om at gøre mere af "
     "affaldet til genanvendelse, og de aftaler, der udbydes nu, afgør hvem der "
     "bygger næste stykke af det. Udbudskonsulentens opgave er at gøre de valg "
     "skarpe: konkurrenceudsættelser efter gældende udbudsregler, klare kriterier "
     "for udvælgelse og tildeling og kontrakter, der holder.")

para("Rollens opgave er at skabe struktur og fremdrift i komplekse processer. Som "
     "projektleder for egne udbud og tilbudsindhentninger koordinerer jeg med de "
     "forretningsansvarlige, gennemfører markedsdialog, udarbejder udbudsmateriale "
     "og kontrakter og overdrager aftalerne efterfølgende. Dertil rådgivning af "
     "forretningsområder og ledere om udbud og udbudsregler, og flere projekter i "
     "gang samtidig i tæt dialog og samarbejde med kollegerne i udbudsteamet, hvor "
     "faglig sparring er en del af hverdagen. Processer, analyse, "
     "leverandørvalg og aftaler skal hænge sammen, og gode relationer og den "
     "personlige kontakt vægtes højt hele vejen.")

para("Jeg har arbejdet med udbud og udbudsregler konkret og kender begge sider af "
     "bordet. Som leverandør har jeg svaret på udbud, skrevet tilbud og kæmpet for "
     "klare kravspecifikationer; som køber har jeg indgået aftaler med leverandører "
     "og underentreprenører på aftalegrundlag som AB 18 og AB forenklet, vurderet "
     "tilbud og ført kontrakterne til aflevering. Jeg driver op til 37 projekter "
     "samtidig med fast struktur for økonomi, tidsplan og opfølgning, og jeg "
     "rådgiver ledere og kolleger i beslutningsoplæg, der er til at handle på. Min "
     "motivation er klar: efter år med at vinde udbud vil jeg være "
     "med til at skrive dem, så konkurrencen bliver skarp, og aftalerne holder. Jeg "
     "har meget at lære om jeres processer og politikker, og det glæder jeg mig til. "
     "Som "
     "professionel og aktiv Claude-koder med Python kan jeg gøre udbudsmateriale og "
     "analyse hurtigere og mere ensartet, så tiden går til dialogen med de "
     "forretningsansvarlige og markedet.")

para("Min plan for de første måneder er konkret. Efter 30 dage kender jeg "
     "indkøbs- og udbudspolitikken, de igangværende udbud og forretningsområderne: "
     "jeg har læst aftalerne, lyttet med i teamet og taget de første samtaler med "
     "forretningsansvarlige. Efter 60 dage driver jeg egne udbud og "
     "tilbudsindhentninger i fast proces fra markedsdialog og kriterier til "
     "udvælgelse og tildeling. Efter 90 dage har jeg overdraget den første aftale "
     "med et ordentligt grundlag, og jeg har lagt et oplæg for, hvordan AI kan "
     "gøre udbudsmateriale og analyse hurtigere og mere ensartet.")

para("Jeg bor i Måløv, få minutter fra Glostrup, og kan tiltræde den 1. februar "
     "2027. Vestforbrænding giver god energi videre; lad os tale om, hvordan den "
     "også ligger i de aftaler, vi indgår. Jeg kan træffes på +45 93 99 95 14.", after=6)

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
para("Jeg driver udbud og indkøb med struktur, klare kriterier og kontrakter, der "
     "holder fra udvælgelse til overdragelse. Maskinmester med erfaring fra begge "
     "sider af bordet, EU-udbud og udbudsregler i praksis og projektledelse af "
     "mange parallelle processer.")

para("Erfaring", style="CVH1")

job("ELOHVAC ApS · København · Ejer og elautoriseret maskinmester · maj 2023 – nu", [
    "Udbud, tilbud og kontrakter: tilbudsindhentning og beregning, aftalegrundlag og "
    "kontraktforberedelse, forhandling og opfølgning med leverandører og underentreprenører.",
    "Indkøb og leverandørstyring: materialestyring, leverandørvurdering og indkøb til "
    "entrepriser med fuldt budget- og P&L-ansvar.",
    "Enterprise- og projektstyring: planlægning, KS og afleveringsdokumentation; "
    "installation og idriftsættelse af el-tekniske anlæg.",
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
bullet("Udbud og kontrakter: EU-udbud og konkurrenceudsættelser, udbudsmateriale og "
       "tilbudsindhentning, kriterier for udvælgelse og tildeling, kontrakter og "
       "aftalegrundlag (AB 18 og AB forenklet); erfaring fra begge sider af bordet.")
bullet("Indkøb og leverandører: strategiske indkøb, leverandørvurdering, markedsdialog, "
       "forhandling og opfølgning på aftaler.")
bullet("Projektledelse: flere parallelle udbud og projekter med struktur og fremdrift; "
       "PRINCE2, RACI og interessentanalyse.")
bullet("Analyse og økonomi: proces og analyse, budget, business cases og "
       "investeringsoverslag; P&L- og SAP-erfaring.")
bullet("Rådgivning: teknisk og kommerciel rådgivning af forretningsområder og ledere; "
       "beslutningsoplæg og klare anbefalinger.")
bullet("Digitalt: Microsoft Office (Excel og Power Query), Python, Claude API og Claude "
       "Code, professionel og aktiv AI- og Claude-koder, Power BI.")
bullet("Sprog: dansk som modersmål, engelsk i skrift og tale.")
bullet("Betingelser: kørekort B og egen bil; bopæl i Måløv få minutter fra Glostrup.")

# ----------------------------- KVALITETSKONTROL -----------------------------
full = "\n".join(p.text for p in doc.paragraphs)
banned = ["spearheaded", "leveraged", "passionate", "dynamic", "results-driven",
          "proven track record", "synergy", "cutting-edge", "innovative solutions",
          "seamlessly", "robust", "demonstrated ability", "fast-paced",
          "drevet", "lidenskabelig", "dynamisk", "synergi", "banebrydende",
          "sømløst", "ikke kun", "men også", "\u2014", "passion"]
hits = [w for w in banned if w.lower() in full.lower()]
jd_words = ["udbud", "udbudskonsulent", "indkøb", "kontrakt", "eu-udbud",
  "konkurrenceudsættelse", "tilbudsindhentning", "udbudsregler", "strategiske indkøb",
  "markedsdialog", "udvælgelse", "tildeling", "kriterier", "forretningsansvarlige",
  "forretningsområder", "overdrag", "rådgiv", "struktur", "fremdrift", "proces",
  "analyse", "leverandør", "aftaler", "relationer", "dialog", "samarbejde",
  "projekter", "team", "sparring", "glostrup", "fjernvarme", "affald", "miljø",
  "genanvendelse", "motivation", "lære", "vestforbrænding", "god energi videre",
  "maskinmester", "1. februar", "stefan"]
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
