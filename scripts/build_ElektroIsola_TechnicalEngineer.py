#!/usr/bin/env python3
"""Byg Shahram_Ajloo_ElektroIsola_TechnicalEngineer.docx (brev + CV i ét dokument)."""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_ElektroIsola_TechnicalEngineer.docx"

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
para("Ansøgning som Technical Engineer, Elektro-Isola", style="LetterTitle")
para("Kære Finn Klein Sørensen", after=4)

para("Ambitionerne i Vejle er til at få øje på: CO2-udledningen skal skæres med "
     "50 procent inden 2030, automatiseringen øges, og vækstrejsen kræver nye "
     "produktionsanlæg og maskiner, der skal fungere sammen med den eksisterende "
     "maskinpark fra første dag. Kernen i rollen som Technical Engineer er derfor at "
     "føre projekterne hele vejen: fra behovsafdækning og beslutningsgrundlag over "
     "kravspecifikation og implementering til installation, indkøring og overdragelse "
     "til driften.")

para("Opgaverne spænder fra kundeprojekter og interne udviklingsprojekter til "
     "tekniske investeringsprojekter: planlægning og koordinering af opførelse, "
     "opstilling og installation af produktionsanlæg og maskineri, ledet på tværs af "
     "fagområder med tidsplan, økonomi, risici og leverancer. Der skal udarbejdes "
     "kravspecifikationer og afklares layout, kapacitet, flow og grænseflader til "
     "bygninger og forsyninger, og byggetekniske og miljømæssige regler, "
     "myndighedskrav og tilladelser skal være på plads. Leverandøropfølgning og "
     "accepttest hører med, både hos leverandøren og på fabrikken, og overdragelsen "
     "til produktion sker struktureret med dokumentation, oplæring og opfølgning. "
     "Som teknisk sparringspartner for Salgsafdelingen hører teknisk kundedialog om "
     "materialevalg og produkt- og procesforbedringer med, og rollen samler "
     "det fulde projektforløb med risici og anbefalinger til ledelsen uden opsøgende "
     "salg. Status, beslutninger og udfordringer bliver kommunikeret klart og troværdigt.")

para("Jeg er maskinmester med elautorisation og har arbejdet hands-on med anlæg, "
     "maskiner og supplerende udstyr hele vejen fra specifikation til igangsætning. "
     "Hos Novo Nordisk førte jeg 37 samtidige anlægs- og CAPEX-projekter, tekniske "
     "investeringsprojekter med FAT/SAT og accepttest, og overdragelse til drift uden "
     "kritiske afvigelser ved aflevering. I Ventek-Air stod jeg for 11 anlægsprojekter "
     "fra specifikation og layout til aflevering med leverandører, underentreprenører "
     "og tekniske grænseflader, og i Biofos lærte jeg proces- og "
     "produktionsteknikken i et anlæg, der aldrig måtte stå stille. Jeg har "
     "erfaring med materialevalg og produktudvikling, og jeg kommer fra "
     "produktionsvirksomheder med internationale samarbejdspartnere. Som professionel "
     "og aktiv Claude-koder med Python kan jeg holde kravspecifikationer, tidsplaner "
     "og projektdokumentation struktureret, og med beregningsmodeller for investeringer "
     "og scenarier kan jeg give ledelsen et klart beslutningsgrundlag for udvikling "
     "af produktionskapaciteten.")

para("Min plan for de første måneder er konkret. Efter 30 dage kender jeg værdikæden "
     "og maskinparken: materialer, processer, igangværende projekter og de tekniske "
     "grænseflader, og jeg har været i produktionen sammen med kollegerne og dig. "
     "Efter 60 dage driver jeg egne projekter i fast struktur med krav, tidsplan, "
     "budget og risici, og leverandøropfølgningen kører fra kravspecifikation til "
     "accepttest. Efter 90 dage er første projekt overdraget til drift med "
     "dokumentation og oplæring, og jeg har lagt et oplæg for, hvordan AI kan gøre "
     "kravspecifikationer og projektdokumentation hurtigere og mere ensartet.")

para("Jeg er indstillet på at flytte til Vejle-området, når det rigtige match er der, "
     "og jeg kan starte efter aftale. Jeg ser frem til at tale om, hvordan jeg kan "
     "bidrage til vækstrejsen og den stærke holdånd i teamet. Jeg kan træffes på "
     "+45 93 99 95 14.", after=6)

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
para("Jeg fører tekniske projekter fra idé og kravspecifikation til installation, "
     "indkøring og overdragelse til drift, så nye maskiner og anlæg leverer fra "
     "første dag. Maskinmester med elautorisation, praktisk baggrund fra produktion "
     "og anlæg og erfaring med investeringsprojekter, leverandørkoordinering og accepttest.")

para("Erfaring", style="CVH1")

job("ELOHVAC ApS · København · Ejer og elautoriseret maskinmester · maj 2023 – nu", [
    "Installation og igangsætning af el-tekniske anlæg, tavler, styring, fiber og "
    "PDS til afleveret anlæg med kundedokumentation og oplæring.",
    "Enterprise- og projektstyring: tilbud og beregning, planlægning, materialestyring, "
    "underentreprenører, KS og afleveringsdokumentation med fuldt P&L-ansvar.",
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
    "Porteføljeansvar for 37 samtidige anlægs- og CAPEX-projekter, tekniske "
    "investeringsprojekter (DKK 2–10 mio. pr. stk.) med fremdrift, økonomi og risici "
    "på tværs af engineering, indkøb og anlæg.",
    "FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA: accepttest og overdragelse til drift med "
    "nul kritiske afvigelser ved aflevering; tværfaglig ledelse af 25 højt specialiserede medarbejdere.",
    "El-tekniske anlæg: tavler og styring, UPS, nød- og panikbelysning, ABA/ABV og PDS; "
    "fejlfinding med A3, 5xHvorfor og Ishikawa; SAP ERP og månedsrapportering.",
    "40 % reduktion af energiomkostninger gennem PDCA-program.",
])

job("Ventek-Air · København · Projekt- og værkstedsleder · jan. 2022 – nov. 2022", [
    "11 samtidige anlægsprojekter (DKK 2–10 mio.) fra specifikation og layout til formel "
    "aflevering, med daglig ledelse af 14-mands team, kapacitets- og fremdriftsstyring.",
    "Udbud og tilbud, underentreprenører og leverandører, aftalegrundlag, tekniske "
    "grænseflader, sikkerhedsdokumentation og afleveringspakker.",
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
bullet("Projektledelse og investeringsprojekter: fra idé og kravspecifikation til "
       "implementering og overdragelse; tidsplan, økonomi, risici og leverancer; "
       "PRINCE2, RACI og interessentanalyse.")
bullet("Installation og indkøring: etablering, opstilling og igangsætning af maskiner "
       "og anlæg, leverandøropfølgning, accepttest og tekniske grænseflader; "
       "kendskab til myndighedskrav og tilladelser i regulerede miljøer.")
bullet("Proces og produktion: proces- og produktionsteknisk forståelse, layout, "
       "kapacitet og flow; materialevalg, produktudvikling, teknisk kundedialog og "
       "produkt- og procesforbedringer.")
bullet("El og teknik: el-tekniske anlæg, tavler og styring, automation; elautoriseret "
       "maskinmester med praktisk erfaring fra industrielle anlæg.")
bullet("Økonomi og beslutninger: budgetter, business cases og beregningsmodeller for "
       "investeringsprojekter (DCF og scenarier); SAP ERP.")
bullet("Digitalt: Microsoft Office (Excel og Power Query), Python, Claude API og Claude "
       "Code, professionel og aktiv AI- og Claude-koder, Power BI.")
bullet("Sprog: dansk som modersmål, engelsk i skrift og tale.")
bullet("Betingelser: kørekort B og egen bil; indstillet på at flytte til Vejle-området.")

# ----------------------------- KVALITETSKONTROL -----------------------------
full = "\n".join(p.text for p in doc.paragraphs)
banned = ["spearheaded", "leveraged", "passionate", "dynamic", "results-driven",
          "proven track record", "synergy", "cutting-edge", "innovative solutions",
          "seamlessly", "robust", "demonstrated ability", "fast-paced",
          "drevet", "lidenskabelig", "dynamisk", "synergi", "banebrydende",
          "sømløst", "ikke kun", "men også", "\u2014"]
hits = [w for w in banned if w.lower() in full.lower()]
jd_words = ["technical engineer", "produktudvikling", "teknisk kundedialog", "projektledelse",
  "behovsafdækning", "beslutningsgrundlag", "implementering", "overdragelse", "kravspecifikation",
  "layout", "kapacitet", "flow", "grænseflader", "byggetekniske", "miljømæssige", "myndighedskrav",
  "tilladelser", "leverandør", "accepttest", "fabrikken", "dokumentation", "oplæring",
  "opfølgning", "sparringspartner", "materialevalg", "procesforbedringer", "fagområder",
  "tidsplan", "økonomi", "risici", "leverancer", "invester", "produktionskapacitet",
  "produktion", "installation", "indkøring", "maskinpark", "produktionsteknik", "struktureret",
  "troværdigt", "dansk", "engelsk", "maskinmester", "produktionsvirksomhed", "internationale",
  "vækstrejse", "specifikation", "idé", "igangsætning", "drift", "vejle", "holdånd",
  "opførelse", "opstilling", "produktionsanlæg", "maskineri", "supplerende udstyr", "svært" ]
jd_words = [w for w in jd_words if w != "svært"]
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
