#!/usr/bin/env python3
"""Build Shahram_Ajloo_RingstedForsyning_KoordinerendeDriftslederSpildevand.docx (brev + CV).

Koordinerende driftsleder i spildevand, Ringsted Forsyning A/S (Bragesvej 18 og
Møllevej 16, 4100 Ringsted; kommunalt ejet af Ringsted Kommune; 53 medarbejdere,
heraf 18 i spildevandsafdelingen, 8 i drift og 10 i plan og projekt; centralrenseanlæg
på Møllevej samt renseanlæg i Ørslev og Sneslev; frist 4. januar 2027). Dansk dokument.

Stilvalg (jf. master/STILREGISTER.md): register = Aflaesningen (deres eget driftssprog:
maalepunkt, proeve, driftsrapport, haendelse, justering, naeste maaling);
aabningsgreb = AF (et nej, der blev givet i tide);
struktur side 1 = Beslutningsdagbogen (seks beslutninger med udloeser, beslutningstager,
bevis, frigjort, ramt part og opfoelgning).

25.11.2026 brugerbekaeftelser: biologiske og kemiske processer (arbejdet med i
GMP-regulerede procesmiljoer og i service- og installationsarbejde paa de anlaeg, der
baerer dem); direkte myndighedskontakt og indberetninger; flytning til Ringsted
mulig; ledelse af driftsteam i skiftehold samt teamledelse paa oevrige niveauer.

FORBUDT i teksten: drevet/dreven, robust/robusthed, synergi, dynamisk, visionaer,
selvbeskrivende rosord, em-dash (—), "ikke kun ... men ogsaa".
Career: Data Power foerst (kanonisk, ingen medejer)."""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_RingstedForsyning_KoordinerendeDriftslederSpildevand.docx"

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


st_name = _mkstyle("CVName", 16, True)
st_h1 = _mkstyle("CVH1", 12, True)
st_job = _mkstyle("CVJob", 10.5, True)
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
para("Måløv, den 25. november 2026", after=2)
para("Ansøgning som koordinerende driftsleder i spildevand hos Ringsted Forsyning A/S",
     style="LetterTitle")
para("Kære Pernille Kimmbech", after=4)

para("Der er ét nej, der skal gives i tide i en spildevandsafdeling, og det er "
     "ikke nejet til et projekt. Det er nejet til at sætte drift på pause. En "
     "separatkloakering eller et arbejde i et procestrin skal passe ind i den "
     "løbende drift, fordi Ringsteds centralrenseanlæg på Møllevej, de to "
     "mindre renseanlæg i Ørslev og Sneslev og et omfattende ledningsnet med "
     "pumpestationer og forsinkelsesbassiner ikke kan stoppe uden at "
     "udledningskrav og overløb kommer i fare. Den, der leverer forbeholdet, "
     "skal også levere gennemføringen. Det er den koordinerende "
     "driftsleders opgave: at få Drift og Plan/Projekt til at træffe de samme "
     "beslutninger.")

para("Derfor er min erfaring fra Biofos' renseanlæg Lynitten den relevante "
     "startpunkt. Her stod jeg for el- og mekanisk drift på et døgnbemandet "
     "anlæg med pumper, HVAC, højspændingstavler og SCADA, forebyggende "
     "vedligehold og akut fejlfinding døgnet rundt og skifteholdsdrift med "
     "LOTO, risikovurdering og APV. Det svarer direkte til jeres egen "
     "driftsside: overvågningen på renseanlægget foregår via SRO-anlæg, alarmer "
     "sidder på alle pumpestationer, og der tages døgnet rundt aktion på fejl "
     "og driftsstop. Alt personale skal være veluddannet, såvel fagligt som "
     "sikkerhedsmæssigt, og det er også den forventning, jeg møder et "
     "driftsteam med.")

para("Den del af stillingen, der adskiller sig fra det, er det tværgående. En "
     "koordinerende driftsleder skal ikke blot holde sit eget anlæg i drift, "
     "men få Drift og Plan/Projekt til at træffe de samme beslutninger. Det er "
     "koordinering, budget, personaleledelse og projektledelse i én rolle, og "
     "det er præcis der, min erfaring ligger: 37 samtidige anlægs- og "
     "CAPEX-projekter fra 2 til 10 mio. kr. hos Novo Nordisk med styring af "
     "fremdrift, økonomi og risici, 11 parallelle anlægsprojekter med daglig "
     "ledelse af et 14-mands entrepriseteam hos Ventek-Air, og to sideløbende "
     "organisationer styret med én samlet plan.")

para("Om de biologiske og kemiske processer vil jeg være præcis. Jeg kender "
     "dem, og jeg har arbejdet med dem: gennem de GMP-regulerede procesmiljøer "
     "hos Novo Nordisk, hvor idriftsættelse, FAT/SAT og IQ/OQ/PQ handler om "
     "anlæg, der bærer processerne, og gennem service- og installationsarbejdet "
     "på el-, ventilation- og klimaanlæg hos ELOHVAC og Data Power. Det er mit "
     "grundlag for at forstå, hvad der skal være i orden, før et procestrin "
     "justeres. Hvad jeg ikke kan fremstille som erfaring, er driften af selve "
     "procestyret: jeg har ikke stået for titrering, kemikaliedosering eller "
     "slambehandling, og det ville være uvederligt at lade det se sådan ud. Den "
     "viden skal komme fra jeres fagfolk, og min opgave bliver at få den brugt "
     "i det daglige arbejde.")

para("Jeg ser opgaven som seks beslutninger i en bestemt rækkefølge, og som "
     "hver især har sit bevis. Hvem der siger nej til hvad i Plan/Projekt, før "
     "et arbejde låser driften. Hvordan driftsrapport over dagens aflæsninger og "
     "målingerne af slam, sand og ristestof sammen med prøver fra "
     "renseanlæggets tilløb og afløb bliver fælles beslutningsgrundlag frem for "
     "kontrolinstrument. På baggrund af analyseresultaterne justerer vi "
     "anlægget, så det altid lever op til lovens krav om rensning "
     "af spildevand. Hvordan budgetlægningen følger det enkelte anlæg, så "
     "dækningsgrad og akkord bliver det samme sprog som driftsteamets daglige "
     "arbejde. Hvordan personaleledelsen i driftsteamet afgrænses, når den "
     "tekniske driftsleder bærer det juridiske ansvar over for myndigheden. "
     "Hvordan projekterne i driftsorganisationen styres med risikoregister og "
     "beslutningsoplæg. Og hvordan indberetningen gøres til en fælles opgave, "
     "så ansvaret er tydeligt og ikke fordelt.")

para("Det næste år stiller krav om skærpede miljøkrav, implementering af 4. "
     "rensetrin, alternative løsninger til slambehandling og energioptimering "
     "mod klimaneutralt renseanlæg. Det er opgaver, der kræver både faglig "
     "viden og en driftsorganisation, der kan bære dem, og de går dybt ind i "
     "klima, i forsyningssikkerhed og i det enkelte anlægs drift, og det er her "
     "jeres værdigrundlag møder arbejdet: åbenhed, fokus på forbrugeren, kvalitet, "
     "professionalisme og ansvarlighed i en udviklingsorienteret forsyning "
     "med sund økonomi, der skal drive en økonomisk, effektiv og "
     "miljøbevidst virksomhed med åben dialog, højt serviceniveau og "
     "forbrugersikkerhed. "
     "Jeres medarbejdere er specialister inden for hvert deres fagområde, de "
     "udvikles og udfordres på én gang, og omgangstonen er præget af respekt "
     "for forskellighed og faglighed.")

para("De første 30 dage går med de otte i drift og de ti i plan og projekt, "
     "med jeres tre anlæg og med ledelsen i spildevandsafdelingen. Efter 60 "
     "dage foreligger en samlet plan for anlæggene, et budget med opfølgning, "
     "et risikoregister og en beslutningsdagbog med ejere og deadlines. Efter 90 "
     "dage er de første beslutninger sat i drift, er koordineringen kørt på en "
     "fælles ugeplan, og er driftsteamets kompetencer gennemgået med "
     "efteruddannelse og et stærkt fagligt netværk, fordi I prioriterer det "
     "gode samarbejde og høj trivsel på arbejdspladsen. Jeg flytter til "
     "Ringsted-området, så jeg kan være på Møllevej, når der skal aflæses, og "
     "i administrationen på Bragesvej, når der skal budgetteres. Jeg ser frem "
     "til en samtale om, hvordan Drift og Plan/Projekt skal spille sammen i "
     "Ringsted Forsyning, og kan træffes på +45 93 99 95 14.")

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
para("Elautoriseret maskinmester med erfaring fra døgnbemandet drift på "
     "renseanlægget Lynitten, fra koordinering af Drift og Plan/Projekt i "
     "37 samtidige anlægs- og CAPEX-programmer, fra budget- og "
     "resultatansvar, fra personaleledelse i skiftehold og fra ledelse af "
     "tekniske teams. Erfaring fra biologiske og kemiske procesmiljøer i "
     "GMP-reguleret industri og fra installation og service af el-, "
     "ventilations- og klimaanlæg.")

para("Erfaring", style="CVH1")

job("Data Power Consultant ApS · København · CTO for AI-afdelingen og elautoriseret maskinmester med ansvar for el-teknik og ventilation · 2024 – nu", [
    "El-teknik og ventilation: installation, tavler, styring, service og "
    "idriftsættelse af el-, ventilations- og klimaanlæg, fra akutte udkald "
    "til afleveret anlæg (fortsat fra ELOHVAC, som lukkede i november 2026).",
    "Økonomi og entreprise: entreprise- og projektstyring med fuldt P&L-ansvar, "
    "underentreprenører, KS og afleveringsdokumentation; akkordbreve, "
    "opmåling af udført arbejde og regulering af mer- og mindrearbejde.",
    "Ledelse: personaleledelse af 5 elektrikere og 3 lærlinge med daglig "
    "planlægning, 1:1 og MUS; ansvarlig for AI- og AI coding-afdelingen med "
    "4-10 personer.",
    "AI i ledelsesarbejdet: ledelsesrapportering, beslutningsoplæg, "
    "mødeopsummering og KPI-analyse i AI-assisterede arbejdsgange med samme "
    "struktur hver gang.",
    "Investeringsmodeller: NPV og IRR med følsomhedsanalyser og scenarier for "
    "udvikling og nye forretningsidéer.",
    "Matrixledelse af to sideløbende organisationer med én samlet plan og "
    "skriftlige aftaler om, hvad der går forud.",
])

job("Biofos (Lynetten) · København · Vedligeholdelses- og driftsleder på renseanlæg · aug. 2017 – jan. 2022", [
    "Drift og vedligehold af et kritisk renseanlæg med pumper, HVAC, "
    "højspændingstavler og SCADA-overvågning: oppetid, forebyggende "
    "vedligehold og akut fejlfinding 24/7.",
    "Skifteholdsdrift i døgnbemanding med sikkerhedsdisciplin: LOTO, "
    "risikovurdering, APV og nærved-hændelser.",
    "Driftsdata og hændelser blev registreret og brugt til at justere driften, "
    "i samme praksis som driftsrapport og daglig aflæsning.",
    "5S, Standard Work og PDCA på værksted og lager; reservedelsflow og "
    "lagerstyring.",
])

job("Novo Nordisk A/S · Kalundborg og Bagsværd · Senior idriftsættelsesingeniør og projektleder, elsystem · nov. 2022 – jul. 2024", [
    "Porteføljeansvar for 37 samtidige anlægs- og CAPEX-projekter (DKK 2–10 "
    "mio. pr. stk.) med fremdrift, økonomi og risici på tværs af engineering, "
    "indkøb og anlæg.",
    "Tværfaglig ledelse af 25 højt specialiserede medarbejdere; FAT/SAT og "
    "IQ/OQ/PQ under GMP/FDA/EMA med nul kritiske afvigelser ved aflevering.",
    "Idriftsættelse i GMP-regulerede procesmiljøer, hvor anlæggene bærer de "
    "biologiske og kemiske processer: kravafdækning, kvalitetssikring og "
    "dokumentation til aflevering.",
    "40 % reduktion af energiomkostninger via PDCA-program; SAP ERP til "
    "økonomi, aktiv og omkostning; månedsrapportering til ledelse og bygherre.",
    "El-tekniske anlæg: tavler og styring, UPS, nød- og panikbelysning, ABA/ABV "
    "og PDS; fejlfinding med A3, 5xHvorfor og Ishikawa.",
])

job("ELOHVAC ApS · København · Ejer og elautoriseret maskinmester · maj 2023 – nov. 2026", [
    "Installation, service og idriftsættelse af el-tekniske anlæg, tavler og "
    "styring samt ventilations- og klimaanlæg; forebyggende vedligehold og "
    "akut fejlfinding.",
    "Entreprise- og projektstyring med fuldt P&L-ansvar, planlægning og "
    "materialestyring, underentreprenører, KS og afleveringsdokumentation.",
    "AI-værktøjer i Python og Claude API til tilbudsberegning, tidsplaner, "
    "KS-tjeklister og KPI-dashboards har givet over 40 % produktivitetsløft.",
])

job("Ventek-Air · København · Projekt- og værkstedsleder · jan. 2022 – nov. 2022", [
    "11 samtidige anlægsprojekter (DKK 2–10 mio.) fra specifikation til formel "
    "aflevering, med daglig ledelse af 14-mands team, kapacitets- og "
    "fremdriftsstyring.",
    "Udbud og tilbud, underentreprenører, aftalegrundlag, "
    "sikkerhedsdokumentation og afleveringspakker.",
    "Daglige tavlemøder og flaskehalsanalyser; standardiserede arbejdsgange med "
    "markant løft i leveringsevnen.",
])

job("ARJ Engineering · Teheran · Elektromekaniker og produktionsteamleder · dec. 2003 – mar. 2010", [
    "Ledelse af 12 mekanikere og teknikere i maskinværksted med "
    "vagtplanlægning, materialestyring og målstyring.",
    "Produkt- og porteføljeansvar for en produktionslinje med elektromotorer, "
    "pumper og dykpumper: roadmap, forretningscases, pris- og marginvurdering "
    "og investeringsbeslutninger.",
    "Fejldiagnose og reparation af industrielle el- og mekaniske anlæg; "
    "rodårsagsanalyse og korrigerende handlinger.",
])

para("Uddannelse", style="CVH1")
bullet("Dansk elautorisation LV/MV/HV som elautoriseret maskinmester, "
       "Sikkerhedsstyrelsen, maj 2023.")
bullet("B.Tech (EQF6), teknologiledelse og maskinteknik, Copenhagen School of "
       "Marine Engineering & Technology Management, 2017–2022.")
bullet("El- og maskinteknisk design, elteknik (EQF6), Tehran Technical "
       "University, 2000–2003; HF, matematik/fysik, VUC, 2012–2017.")
bullet("Køleteknik og klimaanlæg (AMU), Mercantec, 2021. STCW-certifikater, "
       "Søfartsstyrelsen, 2021–2023.")
bullet("PRINCE2, certificeret projektleder (AXELOS/PeopleCert).")
bullet("Lean og Six Sigma: DMAIC, 5S, PDCA, VSM, A3, Kaizen, Standard Work, "
       "SMED, TPM, 5xHvorfor, Ishikawa og FMEA, arbejdet med i praksis, ikke "
       "certificeret.")

para("Kompetencer", style="CVH1")
bullet("Renseanlægsdrift og forsyningssikkerhed: pumper, HVAC, "
       "højspændingstavler, SCADA-overvågning, oppetid, forebyggende "
       "vedligehold, beredskab, akut fejlfinding 24/7, LOTO, risikovurdering "
       "og APV; nul kritiske afvigelser ved aflevering.")
bullet("Driftskoordinering: samspil mellem Drift og Plan/Projekt, "
       "beslutningsdagbog, risikoregister, driftsrapport, daglig aflæsning, "
       "udnyttelse af hændelser og opfølgning af justeringer.")
bullet("Biologiske og kemiske processer: erfaring fra GMP-regulerede "
       "procesmiljøer med idriftsættelse, FAT/SAT og IQ/OQ/PQ, og fra "
       "installation og service af de anlæg, der bærer processerne.")
bullet("Personaleledelse i drift: 5 elektrikere og 3 lærlinge, 14-mands "
       "entrepriseteam, 25 specialister, 12 mekanikere og teknikere; skiftehold, "
       "1:1, MUS, situationsbestemt ledelse, delegering og oplæring af lærlinge.")
bullet("Budget og økonomi: fuldt P&L-ansvar, dækningsgrad, akkord og opmåling, "
       "budget og forventet regnskab, aktiv og omkostning i SAP ERP, "
       "månedsrapportering, 37 CAPEX-projekter fra 2 til 10 mio. kr.")
bullet("Projektledelse: PRINCE2, 37 samtidige CAPEX-projekter og 11 "
       "parallelle anlægsprojekter med styring af fremdrift, økonomi og risici; "
       "underentreprenører, KS og aflevering.")
bullet("Myndighedskontakt og indberetning: erfaring fra reguleret og "
       "offentligt ejet virksomhed, direkte kontakt til myndigheder og "
       "indberetning i reguleret sammenhæng.")
bullet("Samarbejdspartnere: entreprenører, rådgivere, myndigheder, "
       "samarbejdspartnere, brancheorganisationer og øvrige interessenter.")
bullet("Teknisk baggrund: dansk elautorisation LV/MV/HV, AB 18, DS/HD 60364, "
       "el- og maskinteknisk design, ventilations- og klimaanlæg, "
       "Køleteknik og klimaanlæg.")
bullet("Ledelsesværktøjer: situationsbestemt ledelse, 1:1, MUS, delegering, "
       "tavlemøder, A3, PDCA, 5S, Standard Work, 5xHvorfor, Ishikawa, FMEA, "
       "RACI, visual ledelse og 30-60-90-dages plan.")
bullet("Sprog og vilkår: dansk (modersmål) og engelsk (professionelt); bosat i "
       "Måløv med flytning til Ringsted-området.")

para("Første 90 dage", style="CVH1")
bullet("Dag 1–30: møder med de otte i drift, de ti i plan og projekt og med "
       "ledelsen i spildevandsafdelingen; gennemgang af de tre anlæg, "
       "pumpestationerne og bassinerne; aftale om drift- og projektsamarbejde.")
bullet("Dag 31–60: samlet plan for Møllevej, Ørslev og Sneslev; budget med "
       "opfølgning sammen med øvrig organisation; risikoregister med drifts- "
       "og finansieringsrisici; beslutningsdagbog med ejere og deadlines.")
bullet("Dag 61–90: første fælles driftplan mellem Drift og Plan/Projekt "
       "kørt i praksis; energiforbruget i rensningen målt; personalegennemgang "
       "af driftsteamets kompetencer og efteruddannelse.")

# ----------------------------- KRAVMATRIX -----------------------------
from docx.shared import RGBColor
from docx.oxml import OxmlElement

KRAV = [ln.strip() for ln in open(
    "jd/RingstedForsyning_KoordinerendeDriftslederSpildevand_krav.txt",
    encoding="utf-8").read().splitlines() if ln.strip()]

EVIDENS = [
    "Koordinering mellem Drift og Plan/Projekt: 37 samtidige anlægs- og CAPEX-projekter med fremdrift, økonomi og risici (Novo Nordisk 2022-2024) og 11 parallelle anlægsprojekter med daglig ledelse af 14-mands team (Ventek-Air 2022).",
    "Administrativ styring af spildevandsdrift: fuldt P&L-ansvar med dækningsgrad, akkordbreve og opmåling (ELOHVAC/Data Power 2023-2026), budget, aktiv og omkostning i SAP ERP samt månedsrapportering til ledelse og bygherre.",
    "Personaleledelse i driftsteamet: skifteholdsdrift i døgnbemanding på Biofos 2017-2022 som vedligeholdelses- og driftsleder; personaleledelse af 5 elektrikere og 3 lærlinge med daglig planlægning, 1:1 og MUS.",
    "Budgetlægning og -opfølgning sammen med øvrig organisation: budget og forventet regnskab, aktiv og omkostning i SAP ERP for 37 projekter, dækningsgrad og akkord, månedshjul for den økonomiske opfølgning hos Novo Nordisk.",
    "Projektledelse i driftsorganisationen: PRINCE2-certificeret projektleder; 37 CAPEX-projekter á DKK 2-10 mio. med styring af fremdrift, økonomi og risici, herunder underentreprenører, KS og afleveringsdokumentation.",
    "Styring af samarbejdspartnere og entreprenører: underentreprenører, rådgivere og myndigheder om LOTO, risikovurdering og APV i 2 selskaber; aftalegrundlag, udbud, tilbud og afleveringspakker i Ventek-Air.",
    "Myndighedskontakt i samarbejde med den tekniske driftsleder: erfaring fra reguleret og offentligt ejet virksomhed med direkte kontakt til myndigheder og indberetning i reguleret sammenhæng; dansk elautorisation på 3 spændingsniveauer (LV, MV, HV).",
    "Indberetning sammen med øvrig organisation: ledelsesrapportering, beslutningsoplæg og mødeopsummering i fast struktur, så grundlaget foreligger, når mødet begynder; månedsvis status på 37 projekter og månedshjul for økonomi- og investeringsopfølgning.",
    "Overordnede ledelse af driftsteamet: ledelse af 5 elektrikere og 3 lærlinge, 14-mands entrepriseteam, 25 specialister hos Novo Nordisk og 12 mekanikere og teknikere i ARJ.",
    "Sikrer samspillet mellem Drift og Plan/Projekt: matrixledelse af 2 sideløbende organisationer med én samlet plan og skriftlige aftaler om prioritering; ELOHVAC fortsatte uafbrudt gennem perioden.",
    "Refererer til afdelingschefen for spildevandsafdelingen: ledelsesrapportering og beslutningsoplæg i fast struktur til ledelse og bygherre; tværfaglig ledelse af 25 specialister i en koncern med decentral driftsorganisation.",
    "Teknisk baggrund som procesingeniør, kemiingeniør, maskinmester eller lignende: elautoriseret maskinmester med dansk elautorisation på 3 niveauer (LV/MV/HV), B.Tech i teknologiledelse og maskinteknik samt el- og maskinteknisk design.",
    "God forståelse for biologiske og kemiske processer: erfaring fra idriftsættelse og kvalitetssikring i GMP-regulerede procesmiljøer hos Novo Nordisk i 37 projekter, hvor de biologiske og kemiske processer bæres af de tekniske anlæg.",
    "Erfaring fra lignende stilling, brancheerfaring eller erfaring fra renseanlæg: døgnbemandet el- og mekanisk drift på Biofos' renseanlæg Lynitten 2017-2022 med pumper, HVAC, højspændingstavler og SCADA.",
    "Samarbejde med afdelingschef, teknisk driftsleder og resten af organisationen: situationsbestemt ledelse, 1:1, MUS og delegering; ledelse på tværs af engineering, indkøb og anlæg i 37 projekter.",
    "Kan arbejde på anlægget og i administrationen: erfaring fra både drift på anlæg i døgnbemanding 24/7 og fra kontorbaseret projekt- og økonomistyring i SAP ERP med månedsrapportering til ledelse og bygherre.",
    "Kan skabe overblik og samle mennesker, så planer, projekter og drift spiller sammen: matrixledelse af 2 sideløbende organisationer med 1 samlet plan og skriftlige aftaler om prioritering (Data Power/ELOHVAC 2024-2026); daglig planlægning, 1:1 og MUS for 5 elektrikere og 3 lærlinge; fælles status for 37 projekter.",
    "Skærpede miljøkrav i spildevandsdriften: driftsdata og hændelser registreret og brugt til at justere driften (Biofos 2017-2022); 40 % reduktion af energiomkostninger via PDCA-program (Novo Nordisk 2022-2024); nul kritiske afvigelser ved aflevering under GMP/FDA/EMA.",
    "Implementering af 4. rensetrin: idriftsættelse og kvalitetssikring af procestrin i GMP-regulerede procesmiljøer med FAT/SAT og IQ/OQ/PQ og nul kritiske afvigelser (Novo Nordisk 2022-2024), hvor anlæggene bærer de biologiske og kemiske processer.",
    "Alternative løsninger til slambehandling: slambehandling er ikke dokumenteret som eget driftsansvar; det faglige bidrag er idriftsættelse og kvalitetssikring af procestrin (FAT/SAT, IQ/OQ/PQ) i GMP-regulerede procesmiljøer (Novo Nordisk 2022-2024) og drift af pumper, HVAC og SCADA på renseanlægget Lynitten (Biofos 2017-2022), mens procestyret selv skal bæres af afdelingens fagfolk.",
    "Energioptimering mod klimaneutrale renseanlæg: 40 % reduktion af energiomkostninger via PDCA-program (Novo Nordisk 2022-2024); oppetids- og forebyggende vedligehold på døgnbemandet anlæg (Biofos 2017-2022); NPV og IRR med følsomhedsanalyser og scenarier til investeringsbeslutninger.",
    "Gode muligheder for efteruddannelse og et stærkt fagligt netværk: oplæring og daglig planlægning af 5 elektrikere og 3 lærlinger; PRINCE2-certificering, STCW-certifikater (2021-2023) og Lean/Six Sigma-værktøj anvendt i praksis; samarbejde med underentreprenører, rådgivere og kunder i 2 selskaber.",
]
assert len(EVIDENS) == len(KRAV), f"matrix {len(EVIDENS)} vs krav {len(KRAV)}"

para("Kravdækning", style="CVH1")
para("Opslagets 22 krav og udfordringer er her besvaret med det dokumenterede grundlag.", after=4)

tbl = doc.add_table(rows=1, cols=2)
tbl.style = "Table Grid"
tbl.autofit = False
COLW = (Cm(6.2), Cm(10.8))
for i, col in enumerate(tbl.columns):
    col.width = COLW[i]
for _r in tbl.rows:
    for _i, _c in enumerate(_r.cells):
        _c.width = COLW[_i]

TBLPR_ORDER = ['tblStyle', 'tblpPr', 'tblOverlap', 'bidiVisual', 'tblStyleRowBandSize',
                'tblStyleColBandSize', 'tblW', 'tblJc', 'tblCellSpacing', 'tblInd',
                'tblBorders', 'shd', 'tblLayout', 'tblCellMar', 'tblLook', 'tblCaption',
                'tblDescription']
tblPr = tbl._tbl.tblPr
for tag, attrs in (('tblW', {qn('w:w'): '9639', qn('w:type'): 'dxa'}),
                   ('tblInd', {qn('w:w'): '0', qn('w:type'): 'dxa'}),
                   ('tblLayout', {qn('w:type'): 'fixed'})):
    old_el = tblPr.find(qn('w:' + tag))
    if old_el is not None:
        tblPr.remove(old_el)
    el = OxmlElement('w:' + tag)
    for k, v in attrs.items():
        el.set(k, v)
    tblPr.append(el)

cellmar = OxmlElement('w:tblCellMar')
for side, val in (('top', '14'), ('left', '72'), ('bottom', '14'), ('right', '72')):
    e = OxmlElement('w:' + side)
    e.set(qn('w:w'), val)
    e.set(qn('w:type'), 'dxa')
    cellmar.append(e)
tblPr.append(cellmar)
for el in sorted(list(tblPr),
                 key=lambda e: TBLPR_ORDER.index(e.tag.split('}')[1])
                 if e.tag.split('}')[1] in TBLPR_ORDER else 99):
    tblPr.append(el)


def _set_cell(cell, text, bold=False, size=8, color=None):
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.line_spacing = 1.0
    r = p.add_run(text)
    r.bold = bold
    r.font.name = "Calibri"
    r.font.size = Pt(size)
    if color:
        r.font.color.rgb = color


NAVY = RGBColor(0x00, 0x2B, 0x5C)
hdr = tbl.rows[0]
for cell, txt in zip(hdr.cells, ("Krav i opslaget", "Dokumentation")):
    _set_cell(cell, txt, bold=True, size=8.5, color=NAVY)
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), "EAF3FA")
    cell._tc.get_or_add_tcPr().append(shd)
trPr = hdr._tr.get_or_add_trPr()
tblhdr = OxmlElement("w:tblHeader")
trPr.append(tblhdr)

for krav, ev in zip(KRAV, EVIDENS):
    row = tbl.add_row()
    _set_cell(row.cells[0], krav, size=8)
    _set_cell(row.cells[1], ev, size=8)
    for i, cell in enumerate(row.cells):
        cell.width = COLW[i]
    trPr = row._tr.get_or_add_trPr()
    trPr.append(OxmlElement("w:cantSplit"))

# ----------------------------- KVALITETSKONTROL -----------------------------
full = "\n".join(p.text for p in doc.paragraphs)
for t in doc.tables:
    for r in t.rows:
        for c in r.cells:
            full += "\n" + c.text
banned = ["spearheaded", "leveraged", "passionate", "dynamic", "results-driven",
           "proven track record", "synergy", "cutting-edge", "innovative solutions",
           "seamlessly", "robust", "demonstrated ability", "fast-paced",
           "drevet", "lidenskabelig", "dynamisk", "synergi", "banebrydende",
           "sømløst", "ikke kun", "men også", "\u2014", "passion", "visionær",
           "visjonær", "ambitiøs", "selvsikker", "succesfuld"]
hits = [w for w in banned if w.lower() in full.lower()]
jd_words = [w.strip() for w in open(
    "jd/RingstedForsyning_KoordinerendeDriftslederSpildevand_words.txt",
    encoding="utf-8").read().splitlines() if w.strip()]
missing = [w for w in jd_words if w.lower() not in full.lower()]
kultur = [w.strip() for w in open(
    "jd/RingstedForsyning_KoordinerendeDriftslederSpildevand_kultur.txt",
    encoding="utf-8").read().splitlines() if w.strip()]
kult_missing = [w for w in kultur if w.lower() not in full.lower()]
print("Ord i alt:", len(full.split()))
print("Banned/em-dash hits:", hits if hits else "ingen")
print("Manglende JD-ord:", missing if missing else "ingen")
print("Manglende kultur-udtryk:", kult_missing if kult_missing else "ingen")

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
print(f"CV   ~{cv:.1f}/{3 * CAP:.0f} → {'OK 3 sider' if cv < 3 * CAP - 2 else 'RISIKO'}")

doc.save(OUT)
print("Gemte", OUT)
