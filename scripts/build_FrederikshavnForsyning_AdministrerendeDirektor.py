#!/usr/bin/env python3
"""Build Shahram_Ajloo_FrederikshavnForsyning_AdministrerendeDirektor.docx (brev + CV).
Administrerende direktør, Frederikshavn Forsyning A/S (Knivholtvej 15, 9900 Frederikshavn;
9 selskaber, 242 medarbejdere, 678,8 mio. kr. i omsaetning 2025; 100 % ejet af Frederikshavn
Kommune; frist 10. december, samtaler i start januar 2027). Dansk dokument.

Stilvalg (jf. master/STILREGISTER.md): register = Kommerciel-forretningsmaessig;
aabningsgreb = G (spoergsmaalet om ejerkommunens indsigt vs. bestyrelsens beslutning);
struktur side 1 = Ordlisten (deres egne begreber: forsyningssikkerhed, fremtidssikring,
dialog, aabenhed og tillid, effektiviseringer, koncernstrategi og handleplaner).

23.11.2026 brugerbekaeftelser: bestyrelseserfaring; forsyningsdrift i flere driftsgrene
(el, vand, varme, spildevand, affald); reguleret og offentligt ejet kontekst; flytning
til Frederikshavn-omraadet mulig.

FORBUDT i teksten: drevet/dreven, robust/robusthed, synergi, dynamisk, visionaer,
selvbeskrivende rosord, em-dash (—), "ikke kun ... men ogsaa".
Career: Data Power foerst (kanonisk, ingen medejer)."""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_FrederikshavnForsyning_AdministrerendeDirektor.docx"

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
para("Ansøgning som administrerende direktør for Frederikshavn Forsyning A/S",
     style="LetterTitle")
para("Kære Anker Laden Andersen", after=4)

para("Hvor går grænsen mellem det, Frederikshavn Kommune skal have indsigt i, og det, "
     "der skal bestemmes i bestyrelsen? Det spørgsmål står i jeres ejerstrategi fra "
     "22. maj 2026, og det er i praksis den opgave, stillingen skal løse: at lede en "
     "virksomhed, hvor høj forsyningssikkerhed, økonomi, langsigtede investeringer, "
     "regulering og samfundsansvar skal gå hånd i hånd. Ni selskaber og 242 "
     "medarbejdere skal hver dag sikre en stabil forsyning af el, vand og "
     "varme, sørge for behandling og afledning af spildevand samt indsamling og "
     "håndtering af affald, samtidig med at årets investeringer på 252,6 mio. kr. "
     "skal holdes, konkurrencedygtige priser skal bevares, og varmeproduktionen skal "
     "bevæge sig fra naturgas over på el og videre mod biomasse.")

para("Forsyningssikkerhed og fremtidssikring af anlæg er den forudsætning, alt andet "
     "hviler på: stabil drift, der holder, når forholdene er onde, og beslutninger, der "
     "tages i tide. Min driftserfaring er fra et kritisk forsyningsanlæg med pumper, "
     "HVAC, højspændingstavler og SCADA-overvågning, akut fejlfinding døgnet rundt, "
     "LOTO og risikovurdering. I GMP-regulerede overdragelser endte arbejdet i nul "
     "kritiske afvigelser, og i serviceaftalerne blev responstid og leveringsevne gjort "
     "til målbare KPI'er. Samme gælder beredskab: en plan, der er testet, før den "
     "skal bruges.")

para("Den anden side af opgaven er økonomi og investeringer, fordi ejerskabet kræver "
     "transparens og gennemsigtighed, ikke bare et tal. Jeg har haft fuldt P&L-ansvar "
     "for el- og servicevirksomhed med dækningsgrad, akkordbreve, opmåling og "
     "regulering af mer- og mindrearbejde, og jeg har ledet 37 samtidige anlægs- og "
     "CAPEX-projekter fra 2 til 10 mio. kr. med styring af fremdrift, økonomi og risici. "
     "Til de større beslutninger har jeg bygget business cases og investeringsmodeller "
     "med NPV, IRR, følsomhed og scenarier, og det er den metode, jeg bruger i dag til "
     "at beregne udvikling og nye forretningsidéer.")

para("Bestyrelsen og ejerkommunen er den del af opgaven, der beslutter sammen med "
     "direktøren. Jeg har bestyrelseserfaring og arbejder med dagsordener, "
     "beslutningsoplæg og den dialog, jeres ejerstrategi beskriver: at ejerkommunen "
     "involveres og inddrages før større nye tiltag/investeringer gennem dialogmøder, "
     "at forholdet mellem Forsyningen og kommunen skal være baseret på dialog, åbenhed "
     "og tillid, at kommunen holdes orienteret om økonomi, investeringer og "
     "væsentlige strategiske beslutninger, og at der er respekt for bestyrelsens "
     "kompetencer. "
     "Ejerstrategien understreger desuden fokus på kommunens borgere, både som "
     "forbrugere og kunder, med stabile leverancer, effektive priser og god "
     "kundeservice. Ejerstrategiens "
     "principier er troværdighed og legitimitet, aktivt ejerskab, åbenhed og "
     "gennemsigtighed samt fuld indsigt og åbenhed om økonomi. Dem udmønter koncernen i "
     "koncernstrategi og handleplaner for de enkelte forsyningsarter, herunder kravet "
     "om at understøtte kommunes generelle strategier og politikker.")

para("En koncern med ni selskaber kræver, at retningen er tydelig, og en ledelse, der "
     "giver mandat frem for at trække "
     "beslutninger ind. I jeres egen beskrivelse er "
     "Forsyningen en udviklende og attraktiv arbejdsplads med en decentral struktur, "
     "hvor medarbejdernes indsats og samspillet i organisationen skaber resultatet. Det "
     "forudsætter ledere, der kender deres fag, og attraktive arbejdspladser, hvor "
     "medarbejderne trives, med sikkerhed, arbejdsmiljø og efteruddannelse som faste "
     "punkter. Min ledelseserfaring er delegering, 1:1, MUS, situationsbestemt ledelse "
     "og psykologisk tryghed i praksis, fra 25 specialister på tværs af faggrupper, fra "
     "et 14-mands entrepriseteam og fra to sideløbende organisationer i matrix. Styrken "
     "i koncernen ligger i fælles drift og stordriftsfordele, faglig "
     "kompetenceudvikling og det, at den enkelte forsyningschef kender sit område.")

para("Digitalisering i en forsyning er ikke et softwareprojekt. Det er datakvalitet, "
     "overvågning og beslutningsstøtte til de mennesker, der holder driften i gang. Det "
     "er den del af min praksis, der kan bruges i en forsyning: en AI-afdeling med 4 til 10 "
     "personer, der leverer tekniske og industrielle applikationer, kundeløsninger med "
     "AI-agenter, Python og Power BI til analyse og datakvalitet samt "
     "AI-assisterede arbejdsgange til ledelsesrapportering og beslutningsoplæg.")

para("De første 30 dage går med møder i bestyrelsen, med de fire forsyningschefer og med "
     "økonomichefen. Derefter gennemgår jeg drift, risici og investeringsplan i hvert "
     "selskab, og sammen med kommunens administration fastlægger jeg et årshjul for den "
     "økonomiske opfølgning. Efter 60 dage foreligger koncernstrategi og "
     "handleplaner for de enkelte forsyningsarter, et effektiviseringsprogram med "
     "navngivne initiativer og årlige effektiviseringer samt et risikoregister med "
     "drifts- og finansieringsrisici. Efter 90 dage er de første effektiviseringer "
     "realiseret, dialogmødet med kommunen om næste års investeringer gennemført, og "
     "beredskabs- og datakvalitetsforløb iværksat for de områder, hvor oppetiden "
     "betyder mest.")

para("Jeg flytter til Frederikshavn-området, så jeg kan mødes fysisk med bestyrelse, "
     "forsyningschefer, medarbejdere, kommunen, samarbejdspartnere og de øvrige "
     "interessenter. Dansk og engelsk "
     "er arbejdssprog. Jeg ser frem til en "
     "samtale om den næste fase for Frederikshavn Forsyning og kan træffes på "
     "+45 93 99 95 14.")

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
para("Elautoriseret maskinmester og CTO for en AI-afdeling med dokumenteret ansvar for "
     "drift, økonomi og investeringer i flere forsyningsdriftsgrene, herunder el, "
     "vand, varme, spildevand og affald. Erfaring fra kritisk forsyningsdrift, fra "
     "komplekse anlægs- og CAPEX-programmer og fra ledelse i en koncern med decentral "
     "driftsorganisation og et krav om fuld indsigt og åbenhed om økonomi.")

para("Erfaring", style="CVH1")

job("Data Power Consultant ApS · København · CTO for AI-afdelingen og elautoriseret maskinmester med ansvar for el-teknik og ventilation · 2024 – nu", [
    "El-teknik og ventilation: ansvarlig for installation, tavler, styring, service og "
    "idriftsættelse af el-, ventilations- og klimaanlæg, fra akutte udkald til "
    "afleveret anlæg (fortsat fra ELOHVAC, som lukkede i november 2026).",
    "Økonomi og entreprise: entreprise- og projektstyring med fuldt P&L-ansvar, "
    "underentreprenører, KS og afleveringsdokumentation; akkordbreve, opmåling af "
    "udført arbejde og regulering af mer- og mindrearbejde.",
    "Ledelse: personaleledelse af 5 elektrikere og 3 lærlinge med daglig planlægning, "
    "1:1 og MUS; ansvarlig for AI- og AI coding-afdelingen med 4-10 personer.",
    "AI i ledelsesarbejdet: ledelsesrapportering, beslutningsoplæg, mødeopsummering og "
    "KPI-analyse i AI-assisterede arbejdsgange med samme struktur hver gang.",
    "Investeringsmodeller: NPV og IRR med følsomhedsanalyser og scenarier for udvikling "
    "og nye forretningsidéer.",
    "Matrixledelse af to sideløbende organisationer med én samlet plan og skriftlige "
    "aftaler om, hvad der går forud.",
])

job("ELOHVAC ApS · København · Ejer og elautoriseret maskinmester · maj 2023 – nov. 2026", [
    "Installation, service og idriftsættelse af el-tekniske anlæg, tavler og styring "
    "samt ventilations- og klimaanlæg; forebyggende vedligehold og akut fejlfinding.",
    "Entreprise- og projektstyring med fuldt P&L-ansvar, planlægning og materialestyring, "
    "underentreprenører, KS og afleveringsdokumentation.",
    "AI-værktøjer i Python og Claude API til tilbudsberegning, tidsplaner, "
    "KS-tjeklister og KPI-dashboards har givet over 40 % produktivitetsløft.",
])

job("Novo Nordisk A/S · Kalundborg og Bagsværd · Senior idriftsættelsesingeniør og projektleder, elsystem · nov. 2022 – jul. 2024", [
    "Porteføljeansvar for 37 samtidige anlægs- og CAPEX-projekter (DKK 2–10 mio. pr. "
    "stk.) med fremdrift, økonomi og risici på tværs af engineering, indkøb og anlæg.",
    "Tværfaglig ledelse af 25 højt specialiserede medarbejdere; FAT/SAT og IQ/OQ/PQ "
    "under GMP/FDA/EMA med nul kritiske afvigelser ved aflevering.",
    "40 % reduktion af energiomkostninger via PDCA-program; SAP ERP til økonomi, aktiv og "
    "omkostning; månedsrapportering til ledelse og bygherre.",
    "El-tekniske anlæg: tavler og styring, UPS, nød- og panikbelysning, ABA/ABV og PDS; "
    "fejlfinding med A3, 5xHvorfor og Ishikawa.",
])

job("Ventek-Air · København · Projekt- og værkstedsleder · jan. 2022 – nov. 2022", [
    "11 samtidige anlægsprojekter (DKK 2–10 mio.) fra specifikation til formel "
    "aflevering, med daglig ledelse af 14-mands team, kapacitets- og fremdriftsstyring.",
    "Udbud og tilbud, underentreprenører, aftalegrundlag, sikkerhedsdokumentation og "
    "afleveringspakker.",
    "Daglige tavlemøder og flaskehalsanalyser; standardiserede arbejdsgange med markant "
    "løft i leveringsevnen.",
])

job("Biofos (Lynetten) · København · Vedligeholdelses- og driftsleder · aug. 2017 – jan. 2022", [
    "Drift og vedligehold af et kritisk forsyningsanlæg med pumper, HVAC, "
    "højspændingstavler og SCADA-overvågning: oppetid, forebyggende vedligehold og akut "
    "fejlfinding 24/7.",
    "5S, Standard Work og PDCA på værksted og lager; reservedelsflow og lagerstyring.",
    "Skifteholdsdrift med sikkerhedsdisciplin: LOTO, risikovurdering, APV og "
    "nærved-hændelser.",
])

job("ARJ Engineering · Teheran · Elektromekaniker og produktionsteamleder · dec. 2003 – mar. 2010", [
    "Ledelse af 12 mekanikere og teknikere i maskinværksted med vagtplanlægning, "
    "materialestyring og målstyring.",
    "Produkt- og porteføljeansvar for en produktionslinje med elektromotorer, pumper og "
    "dykpumper: roadmap, forretningscases, pris- og marginvurdering og "
    "investeringsbeslutninger.",
    "Fejldiagnose og reparation af industrielle el- og mekaniske anlæg; "
    "rodårsagsanalyse og korrigerende handlinger.",
])

para("Uddannelse", style="CVH1")
bullet("Dansk elautorisation LV/MV/HV som elautoriseret maskinmester, Sikkerhedsstyrelsen, maj 2023.")
bullet("B.Tech (EQF6), teknologiledelse og maskinteknik, Copenhagen School of Marine Engineering & Technology Management, 2017–2022.")
bullet("El- og maskinteknisk design, elteknik (EQF6), Tehran Technical University, 2000–2003; HF, matematik/fysik, VUC, 2012–2017.")
bullet("Køleteknik og klimaanlæg (AMU), Mercantec, 2021. STCW-certifikater, Søfartsstyrelsen, 2021–2023.")
bullet("PRINCE2, certificeret projektleder (AXELOS/PeopleCert).")
bullet("Lean og Six Sigma: DMAIC, 5S, PDCA, VSM, A3, Kaizen, Standard Work, SMED, TPM, 5xHvorfor, Ishikawa og FMEA, arbejdet med i praksis, ikke certificeret.")

para("Kompetencer", style="CVH1")
bullet("Forsyningssikkerhed og drift: kritisk drift døgnet rundt, SCADA og overvågning, "
       "oppetid, forebyggende vedligehold, beredskab, LOTO, risikovurdering og APV; "
       "nul kritiske afvigelser ved aflevering.")
bullet("Forsyningsdrift i flere driftsgrene: elnet, drikkevand, fjernvarme, spildevand "
       "og affald.")
bullet("Økonomi og investeringer: fuldt P&L-ansvar, dækningsgrad, akkord og opmåling, "
       "budget og forventet regnskab, business cases og investeringsmodeller (NPV, IRR, "
       "følsomhed og scenarier), 37 CAPEX-projekter fra 2 til 10 mio. kr.")
bullet("Strategi og ledelse: koncernstrategi og handleplaner, effektiviseringer, "
       "30-60-90-dages plan, situationsbestemt ledelse, 1:1, MUS, delegering og mandat, "
       "psykologisk tryghed, faglig kompetenceudvikling og efteruddannelse.")
bullet("Bestyrelse og ejerskab: bestyrelseserfaring, dagsordener og beslutningsoplæg, "
       "dialogmøder med ejerkommune, åben økonomi, gennemsigtighed og god selskabsledelse.")
bullet("Digitalisering, teknologi og nye arbejdsformer: AI-afdeling med 4-10 personer, "
       "LLM-API'er og AI-agenter, tekniske og industrielle applikationer, Python, "
       "Power BI, datakvalitet og datadreven drift, AI i ledelsesarbejdet.")
bullet("Reguleret og offentlig kontekst: kommunal og offentligt ejet virksomhed, "
       "myndighedsarbejde og dokumentation, dansk elautorisation LV/MV/HV, AB 18 og "
       "DS/HD 60364.")
bullet("Kommunikation og forhandling: kundekommunikation, forhandling i tilbud og "
       "akkord, samarbejde med underentreprenører, rådgivere, myndigheder, "
       "samarbejdspartnere, brancheorganisationer og øvrige interessenter.")
bullet("Sprog og vilkår: dansk (modersmål) og engelsk (professionelt); bosat i Måløv med "
       "flytning til Frederikshavn-området.")

para("Første 90 dage", style="CVH1")
bullet("Dag 1–30: møder med bestyrelsen, de fire forsyningschefer og økonomichefen; "
       "gennemgang af drift, risici og investeringsplan i hvert selskab; årshjul for "
       "økonomi- og investeringsopfølgning sammen med kommunens administration.")
bullet("Dag 31–60: koncernstrategi og handleplaner for de enkelte forsyningsarter lagt "
       "sammen med bestyrelsen; effektiviseringsprogram med navngivne initiativer; "
       "risikoregister med drifts- og finansieringsrisici.")
bullet("Dag 61–90: første effektiviseringer realiseret, dialogmøde med ejerkommunen om "
       "næste års investeringer, beredskabs- og datakvalitetsforløb for de områder, hvor "
       "oppetiden betyder mest.")


# ----------------------------- KRAVMATRIX (side 4) -----------------------------
from docx.shared import RGBColor
from docx.oxml import OxmlElement

KRAV = [ln.strip() for ln in open(
    "jd/FrederikshavnForsyning_AdministrerendeDirektor_krav.txt",
    encoding="utf-8").read().splitlines() if ln.strip()]

EVIDENS = [
    "Koncernstrategi og handleplaner sammen med bestyrelsen. Egen erfaring: produktansvar med roadmap, forretningscases og investeringsbeslutninger i ARJ (12 teknikere).",
    "Drift af kritisk forsyningsanlæg med pumper, HVAC, højspændingstavler og SCADA: oppetid, forebyggende vedligehold og akut fejlfinding 24/7 (Biofos 2017-2022).",
    "Fuldt P&L-ansvar med dækningsgrad, akkordbreve og opmåling. Budget og månedsrapportering i SAP ERP hos Novo Nordisk, hvor 37 CAPEX-projekter á DKK 2-10 mio. blev styret i økonomi.",
    "PDCA-program med 40 % reduktion af energiomkostninger (Novo Nordisk), A3 og 5xHvorfor i fejlfinding, daglige tavlemøder og flaskehalsanalyser i Ventek-Air.",
    "Matrixledelse af 2 sideløbende organisationer med én samlet plan (Data Power 2024 - nu) og tværfaglig ledelse af 25 specialister hos Novo Nordisk.",
    "Bestyrelseserfaring og erfaring fra offentligt ejet virksomhed. Dialogmøder og årshjul for økonomi- og investeringsopfølgning gør ejerkommunens inddragelse til procedure for de 9 selskaber.",
    "Situationsbestemt ledelse, 1:1, MUS og delegering. Ledelse af 5 elektrikere og 3 lærlinge, af AI-afdelingen på 4-10 personer og af 12 mekanikere og teknikere.",
    "Delegering med eget ansvar til fagfolk og sjak i 2 organisationer og i et 14-mands entrepriseteam, kombineret med daglig planlægning, så mandat og høj faglighed følger den enkelte opgave.",
    "Kundekommunikation og forhandling i tilbud, udbud og akkord. Samarbejde med underentreprenører, rådgivere og myndigheder om LOTO, risikovurdering og APV i 2 selskaber (ELOHVAC og Data Power).",
    "CTO for AI-afdelingen med 4-10 personer (2024 - nu), teknisk direktør og ejer i ELOHVAC (2023-2026), senior projektleder med 37 projekter i porteføljen.",
    "P&L-ansvar, dækningsgrad, akkord, materialestyring, budget og omkostning i SAP ERP samt månedsrapportering til ledelse og bygherre ved 37 projekter á DKK 2-10 mio.",
    "Erfaring fra reguleret og offentligt ejet virksomhed: dansk elautorisation LV/MV/HV (2023), AB 18, DS/HD 60364, LOTO og GMP-dokumentation med nul kritiske afvigelser.",
    "Bestyrelseserfaring med dagsordener, beslutningsoplæg og referater, samtidig med ansvaret for 2 sideløbende organisationer, så bestyrelsen får ét grundlag og direktionen mandat.",
    "Business cases og investeringsmodeller med NPV, IRR, følsomhed og scenarier; 37 samtidige CAPEX-projekter á DKK 2-10 mio. med styring af fremdrift, økonomi og risici.",
    "AI-afdeling med 4-10 personer, der leverer tekniske applikationer og kundeløsninger med LLM-API'er og AI-agenter; Python, Power BI og AI-assisterede arbejdsgange i ledelsesarbejdet.",
    "30-60-90-dages plan, tavlemøder og flaskehalsanalyser. PDCA-program med 40 % lavere energiomkostninger og AI-værktøjer med over 40 % produktivitetsløft.",
    "Kritisk drift med pumper, HVAC, højspændingstavler og SCADA, oppetid og forebyggende vedligehold 24/7, LOTO og APV. Nul kritiske afvigelser og serviceaftaler med responstid som KPI.",
    "Forhandling i tilbud, udbud og akkord med opmåling og regulering af mer- og mindrearbejde. Ledelsesrapportering og beslutningsoplæg i fast struktur i CTO-rollen siden 2024.",
    "Matrixledelse af 2 organisationer, ledelse af 25 specialister og 12 mekanikere. Samarbejde med underentreprenører, rådgivere, myndigheder og kunder gennem daglig drift og 1:1.",
    "Forsyningsdrift i flere driftsgrene: elnet, drikkevand, fjernvarme, spildevand og affald. Konkret driftsansvar i elteknik, i klima og ventilation på Biofos (2017-2022) og i el-service fra 2023.",
    "Teknisk og forretningsmæssig vurdering i samme beslutning: 37 CAPEX-projekter, 11 parallelle anlægsprojekter, 14-mands team og fuldt P&L-ansvar.",
    "Situationsbestemt ledelse, 1:1, MUS, delegering og psykologisk tryghed. Matrixledelse af 2 organisationer, hvor den samlede plan styrer prioriteringen, og ELOHVAC fortsatte uafbrudt.",
    "Ledelsesrapportering, beslutningsoplæg og mødeopsummering i fast struktur, så grundlaget foreligger, når mødet begynder. 1:1 og MUS som løbende praksis.",
    "Daglig planlægning og akkordtildeling, delegering til sjak med eget ansvar og beslutninger om prioritering, pris og bemanding. 12 teknikere i ARJ, 14-mands team i Ventek-Air.",
    "Tydeligt ansvar til 5 elektrikere og 3 lærlinge, til 12 mekanikere og til AI-udviklere, i rammer med LOTO, risikovurdering, APV, KS-dokumentation og Standard Work.",
    "Relationer til bestyrelse, forsyningschefer og medarbejdere via 1:1 og tavlemøder; til ejerkommune via dialogmøder; til kunder via tilbud og serviceaftaler. Ramme: 9 selskaber, 242 medarbejdere.",
    "B.Tech (EQF6) i teknologiledelse og maskinteknik (2017-2022), elteknisk design i Teheran (2000-2003), dansk elautorisation LV/MV/HV (2023), PRINCE2 og STCW (2021-2023).",
]
assert len(EVIDENS) == len(KRAV), f"matrix {len(EVIDENS)} vs krav {len(KRAV)}"

para("Kravdækning", style="CVH1")
para("Opslagets 27 krav er her besvaret med det dokumenterede grundlag.", after=4)

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
    "jd/FrederikshavnForsyning_AdministrerendeDirektor_words.txt",
    encoding="utf-8").read().splitlines() if w.strip()]
missing = [w for w in jd_words if w.lower() not in full.lower()]
kultur = [w.strip() for w in open(
    "jd/FrederikshavnForsyning_AdministrerendeDirektor_kultur.txt",
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
