#!/usr/bin/env python3
"""Byg Shahram_Ajloo_Norlys_TeamLeaderSalgOgService.docx (brev + CV i ét dokument)."""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_Norlys_TeamLeaderSalgOgService.docx"

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
para("Ansøgning som Team Leader, Norlys Salg og Service", style="LetterTitle")
para("Kære Lasse Birch", after=4)

para("Når 805.000 andelshavere ejer forsyningen, er hvert kundemøde et lille stykke "
     "af fællesskabets ansvar. I Norlys Salg og Service skal de møder være værdifulde "
     "hver gang, og Service Excellence-programmet samler præcis den opgave: salg, "
     "kvalitet, effektivitet og en ensartet kundeoplevelse på tværs af energi og "
     "telco. For et team på 10-12 medarbejdere i Sønderborg bliver vejen dertil "
     "nærværende ledelse på gulvet, hvor resultaterne skabes gennem mennesker.")

para("Rollens opgave er at være tæt på. Lytte live, coache i realtid og støtte, når "
     "opkaldene er svære, så kvaliteten er høj i hvert eneste møde. 1:1-feedback og "
     "tavlemøder med fokus på udvikling og motivation, opfølgning på KPI'er og "
     "performance med blik for både resultater og trivsel, og struktur og fremdrift i "
     "en hverdag med højt tempo og tydelige mål. Teamet er ét af fire i et ledelsesteam, "
     "der sammen løfter salget, kundetilfredsheden og arbejdsglæden, og forandringen "
     "mod Service Excellence kræver viljen til at gøre tingene bedre uden at glemme "
     "menneskerne i dem.")

para("Jeg har ledet mennesker i mere end 20 år, både direkte og gennem teamledere, "
     "og jeg har bygget min ledelse omkring 1:1, tydelige forventninger og tæt "
     "opfølgning. I mit eget firma driver jeg salg og kundedrift selv: nysalg, "
     "tilbud og dialog fra første kontakt til aftale, og jeg har flyttet både "
     "kvalitet og resultater med tavlemøder, KPI-opfølgning og faste rytmer. Min "
     "erfaring med kundeservice kommer fra salg og teknisk servicevirksomhed med egen "
     "kundedrift, ikke fra et callcenter, men opgaven er den samme: at få et team til "
     "at lykkes med høj kvalitet under pres og følge op på resultaterne uden at miste "
     "trivslen af syne. Jeg søger bevidst en rolle, hvor ledelse på gulvet er selve "
     "opgaven. Som professionel og aktiv Claude-koder med Python kan jeg give hurtigt "
     "overblik over KPI'er og opfølgning, og forretningsforståelsen er skærpet af "
     "budget- og P&L-ansvar, så trivsel og performance kan følges ad i tallene.")

para("Min plan for de første måneder er konkret. Efter 30 dage kender jeg teamet og "
     "kunderejserne: jeg har lyttet med på opkald, holdt 1:1 med alle, lært "
     "KPI'erne og Service Excellence-processerne at kende og mærket, hvor teamet har "
     "brug for støtte. Efter 60 dage kører min faste rytme med coaching, tavlemøder "
     "og KPI-opfølgning, og de første forbedringsforslag er på vej sammen med "
     "kollegerne i ledelsesteamet. Efter 90 dage følges performance og trivsel i et "
     "stabilt loop, og jeg har lagt et oplæg for, hvordan AI kan lette opfølgningen, "
     "så tiden går til kunderne og coachingen.")

para("Jeg er indstillet på at flytte til Sønderborg-området og kan tiltræde efter "
     "aftale, også 1. januar eller 1. februar. Lad os tale om, hvordan teamet skal "
     "løftes mod Service Excellence. Jeg kan træffes på +45 93 99 95 14.", after=6)

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
para("Jeg skaber resultater gennem mennesker med nærværende ledelse, tydelige "
     "forventninger og fast opfølgning på KPI'er, kvalitet og trivsel. Bred "
     "ledelseserfaring fra over 20 år med at lede, coache og udvikle teams i salg, "
     "service og teknisk drift, direkte og gennem teamledere.")

para("Erfaring", style="CVH1")

job("ELOHVAC ApS · København · Ejer og elautoriseret maskinmester · maj 2023 – nu", [
    "Personaleledelse af 5 elektrikere og 3 lærlinge med coaching i hverdagen, 1:1, "
    "MUS og oplæring; ansvar for teamets resultater, trivsel og udvikling.",
    "Salg og kundedrift: nysalg, tilbud og beregning, kundedialog fra første kontakt "
    "til aftale og opfølgning hele vejen til aflevering.",
    "Service og entreprise med fuldt P&L-ansvar: planlægning, materialestyring, "
    "underentreprenører, KS og afleveringsdokumentation.",
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
bullet("Ledelse: nærværende ledelse på gulvet, coaching i realtid, 1:1-feedback, "
       "tavlemøder og udvikling af mennesker; direkte ledelse og ledelse gennem "
       "teamledere med opfølgning på resultater.")
bullet("Salg og kundeservice: nysalg og kundedrift, tilbud og dialog, kundeservice i "
       "praksis; KPI'er og performance med blik for både resultater og trivsel.")
bullet("Struktur og fremdrift: tydelige mål, faste rytmer og opfølgning i højt tempo; "
       "PRINCE2, RACI og interessentanalyse.")
bullet("Økonomi og forretningsforståelse: budget, P&L, forecast og månedsrapportering; "
       "business cases og investeringsoverslag.")
bullet("Udvikling og forbedringer: Lean, PDCA og standardisering; målbare gevinster, "
       "herunder over 40 % produktivitetsløft.")
bullet("Digitalt: Microsoft Office (Excel og Power Query), Python, Claude API og Claude "
       "Code, professionel og aktiv AI- og Claude-koder, Power BI.")
bullet("Sprog: dansk som modersmål, engelsk i skrift og tale.")
bullet("Betingelser: kørekort B og egen bil; indstillet på at flytte til Sønderborg-området.")

# ----------------------------- KVALITETSKONTROL -----------------------------
full = "\n".join(p.text for p in doc.paragraphs)
banned = ["spearheaded", "leveraged", "passionate", "dynamic", "results-driven",
          "proven track record", "synergy", "cutting-edge", "innovative solutions",
          "seamlessly", "robust", "demonstrated ability", "fast-paced",
          "drevet", "lidenskabelig", "dynamisk", "synergi", "banebrydende",
          "sømløst", "ikke kun", "men også", "\u2014", "passion"]
hits = [w for w in banned if w.lower() in full.lower()]
jd_words = ["team leader", "salg", "service", "kundeoplevelse", "medarbejder", "coaching",
  "realtid", "1:1", "tavlemøder", "kpi", "performance", "resultater", "trivsel", "struktur",
  "fremdrift", "tempo", "mål", "motivation", "udvikling", "mennesker", "forretningsforståelse",
  "kundeservice", "ledelseserfaring", "service excellence", "ensartet", "kvalitet",
  "effektivitet", "værdi", "møde", "fællesskab", "andelshavere", "sønderborg",
  "arbejdsglæde", "kundetilfredshed", "opkald", "feedback", "energi", "telco",
  "nærværende", "tydelig", "kunderejser", "lykkes", "lytte"]
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
