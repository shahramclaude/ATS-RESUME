# -*- coding: utf-8 -*-
"""CUBIC-Modulsystem A/S (Rockwell Automation) — Produktionschef.

Dansk opslag → dansk dokument: ansøgning p1, CV p2, uddannelse + 90 dage +
fire sektioner p3, kravmatrix p4.
Vinkel: en ny produktionslokation bliver ikke god, fordi den er ny — den bliver god,
fordi standarden og kulturen sættes de første uger, og fordi lederen står på gulvet.
Policy: master/README.md — jobbet først, kandidaten kun som bevis, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Produktionschef · Opbygning, LEAN og kapacitetsstyring'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Danmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("7. november 2026")
    m.meta("CUBIC-Modulsystem A/S · en del af Rockwell Automation")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Produktionschef", bold=True, color='1A1A1A')
    m.para("Til Plant Manageren og CUBICs ledelse", after=70)

    # ---------------------------------------------------------------- side 1
    m.para("En ny produktionslokation bliver ikke god, fordi den er ny. Den bliver god, fordi de første "
           "tyve medarbejdere lærer den samme standard at kende, før den første ordre går i produktion — og "
           "fordi nogen står på gulvet og ser det ske. Det er den opgave, jeg søger: at være med til at "
           "etablere CUBICs nye site og gøre det til et sted, hvor **lavspændingstavler** og "
           "**kapslingsløsninger** til **energidistribution** forlader porten med samme **driftssikkerhed** "
           "som dem, kunderne kender i dag.", after=80)

    m.para("**Jeg kender produktet fra den anden side af tavlen.** Som **elautoriseret maskinmester "
           "(LV/MV/HV)** har jeg bygget, testet, idriftsat og fejlrettet **lavspændingstavler** og "
           "styringer efter **DS/HD 60364** — jeg ved, hvor monteringen bliver svær, hvor dokumentationen "
           "skal følge med tavlen, og hvad det koster kunden og os, hvis en samling ikke er, som den skal "
           "være. Det er den viden, der gør det muligt at sætte en kvalitetsstandard fra dag ét i stedet for "
           "at rette den bagefter.", after=80)

    m.para("**Jeg har prøvet at bygge fra nul før.** Siden maj 2023 har jeg opbygget og drevet ELOHVAC med "
           "**fuldt P&L-ansvar**, fem elektrikere og tre **lærlinge** — med alt, hvad det indebærer af "
           "**rekruttering**, oplæring, arbejdsgange, **kvalitetssikring** og **leverance**sdisciplin. Før det "
           "stod jeg i spidsen for et maskinværksted og en produktion med 12 teknikere og senere for "
           "projekt- og værkstedsdriften med 14 medarbejdere. En **produktionslokation** er et projekt med "
           "en driftsdag, der ikke kan flyttes: lokalet skal være klar, teamet skal være der, og standarden "
           "skal være skrevet ned, inden den første vare skal ud.", after=80)

    m.para("**Kulturen bliver sat af de første tyve medarbejdere — og af det, lederen går forbi.** Jeg "
           "rekrutterer på faglighed og på vilje til at følge en standard, og jeg bruger de første uger på at "
           "være til stede: **Gemba** hver dag, **tavlemøder** hver morgen, oplæring ved maskinen og en "
           "**kompetencematrix**, der viser, hvem der kan hvad, og hvem der er ved at lære det. Mennesker "
           "gør, som de ser lederen gøre — ikke det, der står i kvalitetshåndbogen.", after=80)

    m.para("**Kapacitet er en beslutning, ikke en beregning, der ligger fast.** Jeg har planlagt "
           "**kapacitet** og **produktionsplanlægning** mod én pulje af medarbejdere på 37 samtidige "
           "CAPEX-projekter og 11 parallelle anlægsprojekter med 14 mand: hvad der kan leveres i denne uge, "
           "hvad der skal skubbes, og hvad der kræver ekstra hænder. **KPI**er som **OEE**, "
           "**leveringssikkerhed** og kvalitet giver kun mening, hvis de følges op dagligt og fører til en "
           "beslutning — ikke hvis de lander i en månedsrapport.", after=80)

    m.para("**LEAN skal kunne ses på gulvet inden for en måned.** Jeg arbejder med **5S**, **standard "
           "work**, **A3**, værdistrømsanalyse, **Kaizen** og PDCA, og jeg har gjort det i miljøer, hvor "
           "produktionen ikke måtte stoppe: standard work og 5S på værksted og lager, PDCA på en 24/7-drift "
           "og et program, der gav **40 % lavere energiomkostninger**, samt værktøjer, der gav **over 40 % "
           "produktivitetsløft** i eget arbejde. **Kontinuerlige forbedringer** holder kun, når de mennesker, "
           "der udfører arbejdet, har været med til at designe dem.", after=80)

    m.para("**Sikkerhed er en del af produktionen, ikke et dokument ved siden af.** Jeg har haft "
           "**arbejdsmiljø** som linjelederansvar med **APV**, risikovurdering ved opstart, **LOTO** ved "
           "arbejde på spændingssatte anlæg og systematisk opfølgning på nærved-hændelser. I en produktion af "
           "**tavler** er de farligste situationer de planlagte: test, spændingsprøvning og fejlsøgning. Dem "
           "skal der være en skriftlig procedure og en navngiven ansvarlig for, før lokalet tages i brug.",
           after=80)

    m.para("**Structuren skal være der, før volumen kommer.** Det betyder produktionsflow med definerede "
           "stationer og mellemlagre, en ordrestyring, der matcher **ERP**ens virkelighed, og en "
           "**produktionsorganisation**, hvor det er tydeligt, hvem der ejer kvalitet, plan og sikkerhed. "
           "Jeg arbejder dagligt i **SAP ERP**, CMMS, **Power BI**, **Excel** og **Office 365**, og den "
           "datamodel, en produktionsplan bygges på — vare, ordre, kapacitet, spild — er den samme logik som "
           "i **Microsoft Dynamics AX**.", after=80)

    m.para("**CUBIC og Rockwell Automation giver et fundament, som en ny lokation sjældent får.** Modulære "
           "**lavspændingstavlesystemer** og kundetilpassede **kapslingsløsninger**, kunder og partnere over "
           "hele verden og et kvalitetssystem, der allerede er defineret — opgaven er at få det omsat til "
           "**produktionsflow**, standarder og daglig adfærd på et nyt site. Det gør jeg med **synlig "
           "ledelse** og med respekt for, at en ny fabrik skal levere, mens den stadig bliver bygget.",
           after=80)

    m.para("Jeg bor i Måløv, har kørekort og kan være på lokationen hver dag. Jeg vil gerne høre, hvor langt "
           "etableringen er, hvilke produktlinjer og volumener det nye site skal bære i år ét, hvordan I måler "
           "leveringssikkerhed og kvalitet i dag, og hvordan **Rockwell**s kvalitets- og "
           "produktionssystem skal anvendes på den nye lokation.", after=70)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Produktions- og driftsleder med 20+ års erfaring i el-teknisk produktion, tavler og teknisk "
           "drift — **elautoriseret maskinmester (LV/MV/HV)** med hænderne i faget og **fuldt P&L-ansvar** "
           "siden 2023. Opbyggede og drev egen virksomhed fra nul med fem elektrikere og tre **lærlinge**; "
           "tidligere ledelse af 12-mands maskinværksted og 14-mands projekt- og værkstedsdrift. Arbejder med "
           "**LEAN**, **5S**, **standard work**, **A3**, **Kaizen** og PDCA i produktion og drift, med "
           "**kapacitetsstyring** og **produktionsplanlægning** mod én ressourcepulje, og med målbare "
           "resultater: **40 % lavere energiomkostninger** og **over 40 % produktivitetsløft**. Dagligt i "
           "**SAP ERP**, **Power BI**, **Excel** og **Office 365**.", after=80)

    m.section("PRODUKTION, LEAN OG KAPACITET")
    for label, body in [
        ("Opbygning af produktion fra bunden",
         "Egen virksomhed etableret fra nul: lokaler, arbejdsgange, rekruttering, oplæring, kvalitetskontrol "
         "og leveringsdisciplin — med en ordrebog, der skulle leveres, mens strukturen blev bygget."),
        ("Produktionsplanlægning og kapacitetsstyring",
         "Kapacitet planlagt mod én pulje af medarbejdere på 11 og 37 samtidige projekter; prioritering "
         "ugentligt, flaskehalse identificeret på daglige tavlemøder og leverancer aftalt med dato."),
        ("LEAN og kontinuerlige forbedringer",
         "5S, standard work, A3, værdistrømsanalyse, Kaizen og PDCA indført i drift og værksted; forbedringer "
         "ejet af dem, der udfører arbejdet, og effekten målt før og efter."),
        ("El-teknisk produktkendskab",
         "Lavspændingstavler, styring og kapslinger bygget, testet og idriftsat efter DS/HD 60364; kvalitet "
         "vurderet på den færdige tavle, ikke på tegningen."),
        ("Arbejdsmiljø og sikkerhed",
         "APV, risikovurdering ved opstart, LOTO på spændingssatte anlæg, sikkerhedsrunder og "
         "nærved-hændelser fulgt til lukning; nul kritiske afvigelser i serviceaftalerne."),
        ("Data, ERP og opfølgning",
         "SAP ERP, CMMS, Power BI og Office 365 i daglig brug; KPI'er som OEE, leveringssikkerhed og kvalitet "
         "omsat til daglig opfølgning og værktøjer, der fjernede manuelle trin."),
    ]:
        m.bullet(label, body, after=25)

    m.section("ERHVERVSERFARING")
    jobs = [
        ("Ejer / teknisk direktør",
         "ELOHVAC ApS · København · maj 2023–nu",
         "5 elektrikere + 3 lærlinge · fuldt P&L · ordrebog, kapacitet og levering",
         [("Opbygning, rekruttering og drift",
           "Virksomheden etableret fra nul: ansættelse og oplæring af elektrikere og lærlinge, arbejdsgange "
           "og kvalitetskontrol, tilbud og beregning, leverancer styret mod en ordrebog med faste datoer."),
          ("Standarder, sikkerhed og forbedring",
           "El-tekniske opgaver på tavler, styring, ventilation og klimaanlæg efter DS/HD 60364; LOTO, APV "
           "og nærved-hændelser; standard work og Python/Power BI-værktøjer med over 40 % produktivitetsløft.")]),
        ("Senior idriftsættelsesingeniør / projektleder, elsystem",
         "Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024",
         "37 parallelle CAPEX-projekter · 25 specialister · GMP/FDA/EMA",
         [("Kapacitet og leverance på tværs",
           "37 samtidige projekter planlagt mod én kapacitetspulje med 25 specialister; fremdrift, økonomi "
           "og snitflader mod indkøb, teknik og drift, og månedlig rapportering til ledelse og bygherre."),
          ("Kvalitet og dokumentation",
           "FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA med nul kritiske afvigelser ved aflevering; "
           "energiprogram med PDCA gav 40 % lavere energiomkostninger.")]),
        ("Projekt- og værkstedsleder",
         "Ventek-Air · København · jan. 2022–nov. 2022",
         "14 medarbejdere · 11 samtidige anlægsprojekter · DKK 2–10 mio.",
         [("Værksted, planlægning og flow",
           "Daglig ledelse af 14-mands team og værkstedsdrift: kapacitets- og fremdriftsstyring, "
           "flaskehalsanalyser på daglige tavlemøder og standardiserede arbejdsgange.")]),
        ("Vedligeholdelses- og driftsleder",
         "Lynetten under Biofos · København · aug. 2017–jan. 2022",
         "Kritisk anlæg i 24/7-drift · tavler, pumper, HVAC · SRO/SCADA",
         [("Drift, sikkerhed og forbedring",
           "Forebyggende vedligehold og reservedelsflow; 5S, standard work og PDCA på værksted og lager med "
           "over 40 % lavere energiforbrug; LOTO og risikovurdering ved arbejde på anlægget.")]),
        ("Elektromekaniker / produktionsteamleder",
         "ARJ Engineering · Teheran · dec. 2003–mar. 2010",
         "12 mekanikere og teknikere · maskinværksted · industrianlæg",
         [("Produktionsledelse i værksted",
           "Daglig ledelse af 12 teknikere i maskinproduktion og reparation: vagtplanlægning, materialestyring, "
           "målopfølgning og korrigerende handlinger ved afvigelser.")]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.page_break()
    m.section("UDDANNELSE OG AUTORISATION")
    m.edu("B.Tech, teknologiledelse og maskinteknik",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12")
    m.edu("El- og maskinteknisk design, elteknik (EQF6)",
          "Tehran Technical University · 2000–2003")
    m.edu("Dansk elautorisation LV/MV/HV — elautoriseret maskinmester",
          "Sikkerhedsstyrelsen · maj 2023")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("Dansk: modersmål · Engelsk: professionelt i møder, dokumentation og rapportering · Persisk: "
           "modersmål · **Bosat i Måløv**, kan være på lokationen hver dag · Kørekort B · Kan tiltræde "
           "snarest muligt · Referencer efter aftale.", after=70)

    m.models_table("DE FØRSTE 90 DAGE — FRA TOMT LOKALE TIL STABIL PRODUKTION",
                   ("Periode", "Hvad der sker, og hvordan det måles"), [
        ("Uge 1–2",
         "Gennemgå produktporteføljen, tegninger og kvalitetskrav med Plant Manageren og Rockwells "
         "kvalitetsfunktion; kortlæg layout, stationer og det udstyr, der skal være klar; aftal bemanding, "
         "vagtmodel og hvem der ejer kvalitet, plan og sikkerhed i den nye organisation."),
        ("Dag 30",
         "Første medarbejdere ansat og i oplæring, med en kompetencematrix der viser, hvad de kan selv, og "
         "hvad de kan med støtte; skriftlige procedurer for test og spændingsprøvning samt APV og "
         "risikovurdering for lokalet; produktionsflow og stationer defineret."),
        ("Dag 60",
         "Første serie kørt gennem det definerede flow med 5S og standard work på plads, tavlemøde hver "
         "morgen og KPI'er for OEE, leveringssikkerhed og kvalitet synlige på gulvet; ERP-opsætning afstemt "
         "med den faktiske produktionsplan."),
        ("Dag 90",
         "Stabil produktion med kendt kapacitet: leveringsevne målt over fire uger, kvalitetsafvigelser "
         "fulgt til lukning, to Kaizen-forbedringer gennemført med målbar effekt, og en bemandingsplan for "
         "det næste halvår, der følger volumenerne og ikke omvendt.")])

    m.section("EN TAVLE ER ET STYKKE HÅNDVÆRK, DER SKAL KUNNE MÅLES")
    m.para("En **lavspændingstavle** er færdig, når den er testet, dokumenteret og kan sættes i drift af en "
           "anden end den, der byggede den. Derfor skal kvalitetskontrollen ligge på stationer undervejs — "
           "moment, afisolering, mærkning, føringsveje, test — og ikke som en slutkontrol, hvor fejlen er "
           "blevet dyr at rette. Det er den samme logik som FAT/SAT i en pharma-aflevering: man tester, fordi "
           "man vil finde fejlen, ikke fordi man vil dokumentere, at man har kigget.", after=80)

    m.section("KULTUREN SÆTTES AF DE FØRSTE TYVE MEDARBEJDERE")
    m.para("I en ny produktion er der ingen historie at læne sig på, og derfor bliver de første måneders "
           "adfærd normen i årevis. Det betyder, at rekruttering er den vigtigste proces i projektet: faglig "
           "bredde nok til at starte produktionen, lærevillighed nok til at følge en standard, der stadig "
           "bliver finpudset, og en blanding af erfarne og **lærlinge**, så kompetencen ikke hænger på to "
           "personer. Jeg har ansat og oplært folk i egen virksomhed og i værkstedet, og jeg ved, at de "
           "første måneder kræver tilstedeværelse, ikke møder.", after=80)

    m.section("KAPACITET ER EN BESLUTNING, IKKE EN BEREGNING")
    m.para("En kapacitetsplan er kun noget værd, hvis nogen har besluttet, hvad der skal prioriteres, når to "
           "ordrer kræver de samme timer. Jeg har prøvet det med 37 projekter og én pulje af specialister, og "
           "løsningen er ikke et bedre regneark: det er et fast forum, hvor salg, plan og produktion ser de "
           "samme tal, og hvor nogen har mandat til at vælge. Ellers bliver planen en ønskeliste, og "
           "leveringssikkerheden falder, uden at nogen har besluttet det.", after=80)

    m.section("LEAN PÅ GULVET, IKKE PÅ ET PAPIR")
    m.para("5S og standard work er ikke en kampagne, men en daglig rutine, der skal være enklere at følge end "
           "at springe over. Jeg starter med det område, der generer flest mennesker mest — typisk "
           "materialeflow, værktøj eller overlevering mellem stationer — måler før og efter og lader teamet "
           "være dem, der præsenterer resultatet. Forbedringer, som medarbejderne har designet, holder; "
           "forbedringer, der er pålagt ovenfra, holder til den næste travle uge.", after=80)

    m.page_break()

    m.models_table("HVAD STILLINGEN KRÆVER — HVAD JEG HAR LEVERET", ("Krav i opslaget", "Bevis"), [
        ('Opbygning og etablering af CUBICs nye produktionslokation i samarbejde med Plant Manager',
         'Egen virksomhed etableret fra nul i 2023: lokaler, arbejdsgange, team, rekruttering og levering — bygget, mens der blev leveret.'),
        ('Rekruttering, ledelse og udvikling af produktionsorganisationen',
         'Ansat og oplært 5 elektrikere og 3 lærlinge; før det ledelse af 12-mands værksted og 14-mands projekt- og værkstedsdrift med kompetencematrix og 1:1.'),
        ('Sikring af et sikkert arbejdsmiljø og overholdelse af gældende standarder',
         'APV, risikovurdering ved opstart, LOTO på spændingssatte anlæg og nærved-hændelser fulgt til lukning; nul kritiske afvigelser i serviceaftalerne.'),
        ('Planlægning af kapacitet, ressourcer, prioriteringer og leverancer',
         'Kapacitet planlagt mod én pulje på 11 og 37 samtidige projekter; ugentlig prioritering, daglige tavlemøder og leverancer aftalt med dato.'),
        ('Sikring af stabile og effektive produktionsflows',
         'Definerede stationer, standard work og 5S på værksted og lager; flaskehalse fundet dagligt og flyttet, før de blev til forsinkelser.'),
        ('Optimering af processer og arbejdsgange med afsæt i LEAN-principper',
         'LEAN i praksis: 5S, standard work, A3, værdistrømsanalyse, Kaizen og PDCA — med 40 % lavere energiomkostninger og over 40 % produktivitetsløft som målte resultater.'),
        ('Skabe struktur, fremdrift og resultater gennem synlig ledelse',
         'Gemba dagligt, tavlemøde hver morgen og ledelse på gulvet i skiftende byggepladser og værksteder; beslutninger taget med dem, der udfører arbejdet.'),
        ('Samarbejde på tværs af organisationen for at sikre høj kvalitet og leveringssikkerhed',
         '37 CAPEX-projekter med indkøb, teknik og drift i samme plan; snitflader navngivet og dateret i stedet for opdaget ved aflevering.'),
        ('Erfaring med ledelse i en produktionsvirksomhed',
         'Produktions- og værkstedsledelse med 12 teknikere, 14 medarbejdere og egen virksomhed siden 2023 — daglig drift, bemanding, kvalitet og levering.'),
        ('Solid teknisk og mekanisk forståelse',
         'Elautoriseret maskinmester (LV/MV/HV) og B.Tech i maskinteknik; tavler, styring, pumper, HVAC, værksted og fejlfinding med hænderne i faget.'),
        ('Arbejder struktureret og målrettet',
         'Skriftlig plan, navngiven ansvarlig og dato på hver opgave; opfølgning på samme møde hver uge, og åbne punkter lukkes, før nye åbnes.'),
        ('Erfaring med LEAN og kontinuerlige forbedringer',
         '5S, standard work, A3, Kaizen og PDCA indført i fire organisationer; forbedringerne ejet af teamet og effekten målt før og efter.'),
        ('Fortrolig med produktionsplanlægning og kapacitetsstyring',
         'Produktions- og projektplanlægning i 20 år, med 11 og 37 samtidige leverancer mod én kapacitetspulje og ugentlig re-prioritering.'),
        ('Erfaring med ERP-systemer, eksempelvis Microsoft Dynamics AX',
         'SAP ERP og CMMS dagligt med stamdata, ordrer, kapacitet og spild; samme datamodel og logik som i Microsoft Dynamics AX.'),
        ('Stærke kommunikations- og samarbejdsevner',
         'Daglig dialog med medarbejdere, kunder, leverandører og rådgivere; svære samtaler taget tidligt og ansigt til ansigt.'),
        ('Erfaren bruger af Microsoft Office 365',
         'Office 365, Excel og Power BI i daglig brug til planer, KPI-dashboards og rapportering; værktøjer bygget, hvor der ikke fandtes et.'),
        ('Visibel og hands-on tilgang til produktionen',
         'Lederen står på gulvet: Gemba hver dag, oplæring ved stationen og fejlfinding sammen med teamet — ikke instrukser fra et kontor.'),
        ('Kendskab til modulære lavspændingstavlesystemer og kapslingsløsninger til energidistribution',
         'Lavspændingstavler, styring og kapslinger bygget, testet og idriftsat efter DS/HD 60364 gennem 20 år; autorisation LV/MV/HV.'),
        ('Erfaring med at opbygge en produktionskultur og et team fra bunden',
         'Team og arbejdsgange bygget fra nul i egen virksomhed og i værkstedet; standarden skrevet ned og lært videre til lærlinge og nye medarbejdere.'),
    ], widths=(3600, 7046))

    m.section("EN NY LOKATION SKAL LEVERE, MENS DEN BLIVER BYGGET")
    m.para("Det er den egentlige sværhedsgrad i denne stilling: produktionen skal i gang, før alt er færdigt — "
           "mens layoutet justeres, mens de sidste medarbejdere ansættes, og mens kunderne allerede har fået "
           "datoer. Så rækkefølgen skal besluttes bevidst: hvilke produkter der kan køres stabilt først, "
           "hvilke stationer der må være midlertidige, og hvad der absolut ikke må være midlertidigt — test, "
           "isolering, mærkning og dokumentation. Jeg har prøvet den slags overgange i drift og på "
           "byggepladser, og erfaringen er enkel: det, der bliver midlertidigt på sikkerhedsområdet, bliver "
           "permanent, indtil nogen kommer til skade.", after=80)

    return m.save(path, title="Produktionschef — CUBIC / Rockwell Automation",
                  subject="Opbygning af produktionssite, LEAN og kapacitetsstyring",
                  keywords="produktionschef, lean, 5s, kapacitetsstyring, produktionsplanlægning, "
                           "lavspændingstavler, arbejdsmiljø, erp, sap erp, office 365, cubic, "
                           "rockwell automation")


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_CUBIC_Produktionschef.docx')))
