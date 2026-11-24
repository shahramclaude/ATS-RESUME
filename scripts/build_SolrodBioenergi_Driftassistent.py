#!/usr/bin/env python3
"""Byg Shahram_Ajloo_SolrodBioenergi_Driftassistent.docx (brev + CV i ét dokument).
Driftassistent – Biogasanlæg, Solrød Bioenergi (Bigadan-gruppen).
23.11.2026: kabeldimensionering = ja (upinnet); vagtordning inkl. weekender = ja;
ansøgning pr. e-mail (adressen har brugeren). Karriereforløb som i PM ENERGI v3."""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_SolrodBioenergi_Driftassistent.docx"

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
para("Ansøgning som Driftassistent til biogasanlægget i Solrød", style="LetterTitle")
para("Kære Solrød Bioenergi", after=4)

para("7.000 tons organisk biomasse om ugen bliver til biogas på naturgasnettet, og "
     "planerne om udvidelse stiller krav til et anlæg, der kører stabilt døgnet rundt. "
     "Bigadans mission er at omdanne organiske restprodukter til værdifulde ressourcer, "
     "og i hverdagen hviler den mission på driften: et hold, der tager ansvar for anlægget, "
     "og elektriske systemer, der er dokumenteret, dimensioneret og vedligeholdt. Jeg er "
     "maskinmester med håndværksmæssig baggrund som elektromekaniker og med elautorisation, "
     "og det elektriske ansvarsområde i stillingen er det, jeg har arbejdet med gennem hele min "
     "karriere.")

para("Det overordnede ansvar for de elektriske systemer svarer til mine opgaver i praksis: "
     "el-tekniske anlæg med tavler og styring, UPS, ABA/ABV og PDS hos Novo Nordisk, "
     "installation, fejlfinding og vedligeholdelse af el-tekniske anlæg i ELOHVAC og nu hos "
     "Data Power Consultant ApS, og dokumentation, der følger anlægget, med opdaterede "
     "ledningsdiagrammer, kabeltræk og føringsveje, KS og afleveringsdokumentation. "
     "Dimensionering af kabler og komponenter har jeg konkret erfaring med fra el-projektering "
     "og beregning, og i AI-assisteret design af tekniske anlæg bliver beregninger og "
     "designvarianter valideret med faglig kontrol, før de bruges.")

para("Den daglige drift og vedligeholdelse af et industrianlæg kender jeg fra Biofos, hvor jeg "
     "kørte skifteholdsdrift på et kritisk forsyningsanlæg med pumper, SCADA og procesudstyr, "
     "og procesforståelsen fra anlæg, hvor mekanik, el og styring hænger sammen. Jeg arbejder "
     "struktureret og selvstændigt og bevarer overblikket, når situationer er pressede, jeg kan "
     "indgå i vagtordning på hverdage og weekender, og pc og mobil er faste arbejdsredskaber "
     "hos mig med SAP, Power BI og digitale tjeklister. Som operatør i et 5-mands hold tager "
     "jeg min del af ansvaret og bidrager til, at holdet fungerer.")

para("De første 30 dage vil jeg sætte mig ind i anlægget, de elektriske systemer og "
     "ledningsdiagrammerne og komme med i holdets rytme og vagtplan. Derefter tager jeg "
     "selvstændigt min del af den daglige drift og vedligeholdelsen af de elektriske anlæg, og "
     "i løbet af de første tre måneder vil dokumentationen være gennemgået og opdateret, og "
     "konkrete forslag til bedre drift og vedligeholdelse vil ligge klar. Jeg vil gerne bidrage "
     "til den grønne omstilling og bedre udnyttelse af ressourcerne, og planerne om udvidelse "
     "passer til mig, der gerne vil være med til at bygge videre.")

para("Jeg bor i Måløv med kort vej til Solrød og kan tiltræde efter aftale. Lad os tale om, "
     "hvordan jeg kan tage ansvar for de elektriske systemer og min del af driften på anlægget. "
     "Jeg kan træffes på +45 93 99 95 14.")

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
para("Elautoriseret maskinmester med håndværksmæssig baggrund som elektromekaniker og "
     "erfaring med drift og vedligeholdelse af industrianlæg, el-tekniske systemer, "
     "procesanlæg og dokumentation. Arbejder struktureret og selvstændigt med "
     "dimensionering af kabler og komponenter, ledningsdiagrammer, fejlfinding og "
     "forebyggende vedligeholdelse tæt på anlægget.")

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
bullet("Elektriske systemer: overordnet ansvar for el, tavler og styring, UPS, ABA/ABV, PDS "
       "og SCADA; elautorisation LV/MV/HV; baggrund som elektromekaniker og entrepriseelektriker.")
bullet("Dimensionering og diagrammer: dimensionering af kabler og komponenter (DS/HD 60364); "
       "ledningsdiagrammer, kabeltræk og føringsveje.")
bullet("Drift og vedligeholdelse: daglig drift, forebyggende og afhjælpende vedligeholdelse, "
       "fejlfinding på el og mekanik; akutte udkald.")
bullet("Proces og industrianlæg: procesforståelse fra forsynings- og produktionsanlæg; "
       "pumper, styring og SCADA.")
bullet("Hold og vagt: skifteholdsdrift og vagtordning på hverdage og weekender; teamsamarbejde "
       "i faste hold.")
bullet("Digitalt: pc og mobil som arbejdsredskaber; SAP ERP, CMMS, Power BI, Excel/Power Query, "
       "Python og Claude Code.")
bullet("Sprog: dansk og engelsk, skrift og tale.")
bullet("Betingelser: kørekort B; bosiddende i Måløv med kort vej til Solrød; tiltrædelse efter aftale.")

# ----------------------------- KVALITETSKONTROL -----------------------------
full = "\n".join(p.text for p in doc.paragraphs)
banned = ["spearheaded", "leveraged", "passionate", "dynamic", "results-driven",
          "proven track record", "synergy", "cutting-edge", "innovative solutions",
          "seamlessly", "robust", "demonstrated ability", "fast-paced",
          "drevet", "lidenskabelig", "dynamisk", "synergi", "banebrydende",
          "sømløst", "ikke kun", "men også", "\u2014", "passion"]
hits = [w for w in banned if w.lower() in full.lower()]
jd_words = ["driftassistent", "maskinmester", "elektriker", "struktureret", "selvstændigt",
  "pressede", "dimensionering", "kabler", "komponenter", "procesforståelse", "industrianlæg",
  "pc", "mobil", "daglig drift", "vedligeholdelse", "vagtordning", "hverdage", "weekender",
  "elektriske systemer", "ledningsdiagrammer", "grønne omstilling", "ressourcer", "operatør",
  "5-mands", "ansvar", "dokumentation", "fejlfinding", "tavler", "styring", "solrød",
  "bigadan", "biogas", "el-tekniske", "elautorisation", "skifteholdsdrift", "holdet",
  "udvidelse", "biomasse", "naturgasnet"]
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
