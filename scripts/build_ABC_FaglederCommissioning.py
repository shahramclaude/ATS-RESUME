# -*- coding: utf-8 -*-
"""Fagleder, Commissioning — ABC Rådgivende Ingeniører A/S, Glostrup (dansk opslag).

Dansk opslag -> dansk dokument, 4 sider: brev side 1, CV side 2, uddannelse + 90 dage +
metodeafsnit + "Hvor jeg ville starte" side 3, kravmatrix side 4. Format per master/README.md:
brev -> CV -> uddannelse/90 dage -> matrix. Rekrutterens anvisninger om ansøgningsform følges ikke
(opslaget beder om CV hurtigst muligt — brevet bliver alligevel side 1).

STILVALG (master/STILREGISTER.md; godkendt af scripts/style_guard.py, 3/3 skift mod #210):
  register      = RÅDGIVENDE — faglighed, metode, standarder, sparring, leveranceansvar. ABC *er*
                  et rådgivende ingeniørfirma, og rollen er at bygge et fagområde. Sidst #206.
  åbningsgreb   = G (SPØRGSMÅLET) — \"Hvornår er en bygning færdig?\" Sidst #193.
  struktur      = DOKUMENTERNE — fire dokumenter commissioning står og falder med: Cx-planen ·
                  grænsefladelisten · testprotokollen · afvigelseslisten og afleveringsmappen.
                  Sidst #189.
  kadence       = kort, næsten mundtlig åbning (to sætninger, et spørgsmål), derefter lange,
                  forklarende sætninger i brevet og rolige, kronologiske sætninger i CV'et.

KULTURSYNKRONISERING (policy 04.11.2026), kilder i master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md §182:
  ABC – Rådgivende Ingeniører A/S, stiftet 2006, Østbrovej 4C, Glostrup (og Silkeborg), ca. 180
  medarbejdere. Egen beskrivelse: \"rådgivere på alle ingeniørfagene med fuldt ansvar for
  leverancen\", \"agilitet og faglig dybde\", \"tætte relationer med kunder og samarbejdspartnere\".
  Installationsafdelingen etableret 2023, 1 → 50 medarbejdere på tre år; ny afdeling
  **Bygningsperformance** (commissioning, bygningsautomatik og drift) fra august 2026, ledet af
  **Henrik Toelstang Jørgensen** (fra COWI). Forretningschef for installationsforretningen:
  Kasper Lyngsfeldt. Opslagets projekter: Sankt Lukas Hospice, Fælledby Skole, Maskincentralen på
  Carlsberg. Kulturord fra opslaget og pressen: \"kort vej fra idé til handling\", åbent
  storrumskontor, uformelt miljø, ABC Academy.

Ingen opdigtede fakta. Dokumenteret grundlag: 37 CAPEX-projekter med FAT/SAT, IQ/OQ/PQ og nul
kritiske fund under GMP/FDA/EMA; idriftsættelse, afleveringsforretning og 1-/5-års gennemgang;
24/7-drift med SRO/SCADA, HVAC, HV-tavler; CTS/bygningsautomatik; ventilation og køl (Ventek-Air,
AMU); 11 entrepriser/14 mand og fuldt P&L siden 2023; 12 teknikere i værksted (ARJ); PDCA med
40 % lavere energiforbrug og 40 % højere produktivitet; SAP. Ingen påstand om Cx-leder-titel —
postingen tillader \"eller haft en tilsvarende rolle\", og dokumentet beskriver rollen ved indhold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Fagleder, Commissioning · Cx fra projektering til aflevering'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4. november 2026")
    m.meta("Fagleder, Commissioning · ABC – Rådgivende Ingeniører · Glostrup")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Fagleder, Commissioning", bold=True, color='1A1A1A')
    m.para("Kære Henrik Troelstang Jørgensen,", after=60)

    # ---------------------------------------------------------------- side 1
    m.para("**Hvornår er en bygning færdig?** Det spørgsmål bliver besvaret på hvert eneste "
           "byggemøde, og det bliver som regel besvaret af den, der taler sidst. Er bygningen "
           "færdig, når entreprenøren har afleveret sine sidste timer, når rådgiveren har lukket "
           "sin sidste afvigelse, eller når driftsorganisationen kan overtage anlægget uden at "
           "ringe til nogen? De tre svar er ikke det samme, og afstanden mellem dem er præcis dét, "
           "commissioning findes for at fjerne. En Cx-leder kommer ikke til sidst for at teste "
           "lidt. Cx-lederen skriver ned i projekteringen, hvad der skal måles, hvem der måler "
           "det, og hvad svaret mindst skal være — og holder derefter alle op på det, når "
           "bygningen står færdig.", after=80)

    m.para("**Cx-planen er det dokument, ingen læser, før det er for sent.** Den skal ligge, "
           "inden de første kanaler er trykprøvet: hvilke systemer der skal prøves, hvem der "
           "prøver, hvad acceptkriteriet er, og i hvilken uge det sker. Jeg har skrevet "
           "prøveprotokoller, før testen blev kørt — FAT og SAT, IQ/OQ/PQ og funktionsprøvning af "
           "**CTS**-anlæg, **eltavler** og **ventilations**systemer — på 37 CAPEX-projekter med "
           "nul kritiske fund ved **afleveringen**. Forskellen på en plan, der bliver brugt, og en "
           "plan, der bliver arkiveret, er, om der står et navn og en dato ud for hver linje.", after=80)

    m.para("**Grænsefladelisten er der, hvor byggeriet falder fra hinanden.** **CTS** skal have "
           "signal fra ventilationen, ventilationen skal have spænding fra el, og brandspjældet "
           "skal lukke, når ABA'en siger det — men ingen af de tre fag ejer den test, der beviser "
           "det. Derfor skal nogen eje den: én linje pr. **grænseflade**, med hvem der leverer, "
           "hvem der modtager, hvordan det prøves, og hvad \"færdig\" betyder. Jeg har stået på "
           "alle sider af den liste — som elinstallatør, som projektleder for 11 entrepriser og "
           "som den, der skulle overtage anlægget i 24/7-**drift**.", after=80)

    m.para("**Testprotokollen skal vise funktion, ikke bare spænding.** Det er nemt at "
           "dokumentere, at pumpen kører. Det svære er at dokumentere, at anlægget gør det rigtige, "
           "når udetemperaturen falder, når en føler fejler, og når to styringer vil det samme. "
           "Derfor prøves sekvenser og fejlsimuleringer, ikke kun komponenter, og resultatet "
           "skrives ned, mens anlægget kører — med kalibreringsdato på instrumentet og navn på den, "
           "der målte.", after=80)

    m.para("**Afvigelseslisten og afleveringsmappen er det, kunden husker.** En afvigelse er ikke "
           "lukket, fordi entreprenøren har lovet det; den er lukket, når nogen har set den virke, "
           "og der står en dato og et navn ved. **Afleveringsmappen** indeholder as-built, "
           "testresultater, **driftsinstruks**, **brugeruddannelse**, afvigelser og en plan for 1- "
           "og **5-års gennemgang**. Det er ikke bureaukrati; det er den fil, driftsfolkene åbner "
           "klokken 03.10, første gang anlægget ikke opfører sig som planlagt.", after=80)

    m.para("**Mødet er Cx-lederens vigtigste værktøj.** Ikke fordi møder løser noget i sig selv, "
           "men fordi en beslutning, der ikke er skrevet ned, holder til næste møde og ikke "
           "længere. Jeg leder byggemøder, tavlemøder og afleveringsmøder med en dagsorden, der "
           "slutter i beslutninger med navn og dato — **mødeledelse** er håndværket, ikke "
           "formaliteten. **Afleveringsforretningen** kører jeg efter **AB 18**, og den "
           "**kompetence**, der skal bære faget videre, bygger jeg med planer og skabeloner i "
           "stedet for med held.", after=80)

    m.para("**Hos ABC skal det ikke bare gøres — det skal kunne gentages.** Det er den del af "
           "rollen, jeg søger: at gøre de fire dokumenter til ABC's **standard**, med skabeloner, "
           "**tjeklister** og en testvejledning, som en ny **fagleder** kan tage i brug i uge to, "
           "og med en **kompetence**plan, så commissioning-fagligheden breder sig ud over "
           "Bygningsperformance. Jeg har prøvet det før — i egen virksomhed med fem elektrikere og "
           "tre lærlinge, hvor oplæring, skabeloner og **værktøjer** flyttede produktiviteten 40 "
           "procent, og på 37 projekter, hvor den samme dokumentationspakke blev genbrugt hver "
           "gang i stedet for at blive opfundet.", after=80)

    m.para("**Praktisk.** Jeg bor i Måløv, har godt 20 minutter til Glostrup og sidder gerne i "
           "åbent landskab. Uddannet **elautoriseret maskinmester**, kører ud på pladsen, taler "
           "dansk med håndværkerne og engelsk med de udenlandske leverandører. Kan starte efter "
           "aftale.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Maskinmester med mere end tyve år i tekniske installationer og commissioning: "
           "elautoriseret på LV/MV/HV-niveau, el- og maskinteknisk design (EQF 6) og B.Tech i "
           "teknologiledelse. 37 CAPEX-projekter med FAT/SAT, IQ/OQ/PQ og nul kritiske fund ved "
           "afleveringen, 11 entrepriser med 14 mand og fire år med 24/7-drift af et anlæg med SRO "
           "og højspænding.", after=80)

    m.section("COMMISSIONING OG AFLEVERING")
    for label, body in [
        ("Cx fra projektering til aflevering",
         "Aktiviteter, tests og dokumentation planlagt fra projekteringsfasen, så afleveringen er "
         "en gennemført sekvens og ikke en uges panik til sidst."),
        ("Grænseflader mellem fagene",
         "Én linje pr. grænseflade mellem CTS, ventilation, el, VVS og ABA med leverandør, "
         "modtager, prøvemetode og acceptkriterium — og en ejer, der kan svare for den."),
        ("Aflevering og gennemgang",
         "Afleveringsforretning med as-built, testresultater, driftsinstruks og brugeruddannelse; "
         "1- og 5-års gennemgang med afvigelser lukket på dato, navn og virkning."),
    ]:
        m.bullet(label, body)

    m.section("TEKNISK BREAKDE")
    for label, body in [
        ("El og tavler",
         "**El-installationer** fra tavle til terminal, UPS, nød- og panikbelysning og "
         "føringsveje; DS/HD 60364 og SB-vejledning i praksis, LV/MV/HV på tegning og på pladsen."),
        ("Ventilation og køl",
         "Ventilations- og køleanlæg projekteret, monteret og idriftsat som entreprise — 11 "
         "samtidige opgaver med tilhørende indregulering og måling."),
        ("CTS og bygningsautomatik",
         "**Bygningsautomatik**, **SRO** og **SCADA** i daglig brug gennem fire år, med alarmer, "
         "sekvenser, fejlsimulering og de grænseflader, der skal prøves, før de virker."),
        ("Energi, indeklima og bæredygtighed",
         "**Energi** og **indeklima** som målbare størrelser: PDCA-program med over 40 procent "
         "lavere energiforbrug, dokumenteret over en årrække og ikke som en intention."),
    ]:
        m.bullet(label, body)

    m.section("METODE, SPARRING OG ØKONOMI")
    for label, body in [
        ("Metoder og standarder",
         "Skabeloner, **tjeklister** og prøveprotokoller, der bliver brugt på pladsen; egne "
         "AI-værktøjer til KS-tjek og KPI-dashboards med 40 procent højere produktivitet."),
        ("Sparring og oplæring",
         "Faglig sparring med kolleger og systematisk oplæring: tre lærlinge med egen plan, "
         "AMU-kurser, MUS og tavlemøder på de samme tal hver uge."),
        ("Tid og økonomi",
         "**Fremdrift** og **økonomi** i egne projekter med fuldt P&L-ansvar siden 2023, og 11 "
         "parallelle entrepriser á 2–10 mio. kr. fra specifikation til formel aflevering."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Ejer / teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · fuldt P&L · projektering, udførelse og aflevering")
    m.bullet("Commissioning og aflevering i egen virksomhed",
              "Idriftsættelse, funktionsprøvning, afleveringsforretning og 1-års gennemgang på "
              "egne sager — med testprotokol, dokumentation og kundens underskrift som afslutning.")

    m.job("Senior Commissioning Engineer / Project Manager",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul 2024",
          scope="37 samtidige CAPEX-projekter · 25 specialister · GMP/FDA/EMA")
    m.bullet("Test, dokumentation og myndighed",
              "FAT/SAT og IQ/OQ/PQ med protokol skrevet før testen; **dokumentation** i **SAP** og "
              "nul kritiske fund ved afleveringen — med myndigheden siddende i rummet.")

    m.job("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · ventilation og køl")
    m.bullet("Tværfaglig koordinering under pres",
              "Ventilation, køl og styring koordineret med de øvrige fag på 11 parallelle sager; "
              "kunden orienteret samme dag, når planen flyttede sig.")

    m.job("Drifts- og vedligeholdelseschef", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="Renseanlæg i 24/7-drift · pumper, HVAC, HV-tavler, SRO/SCADA")
    m.bullet("Anlæg i drift og planlagte udfald",
              "Drift, fejlfinding og planlagte udfald med reservevej designet på forhånd; "
              "tilbagevendende fejl taget til rodårsag, og PDCA-program med 40 procent lavere "
              "energiforbrug.")

    m.job("Elektromekaniker / produktionsformand",
          "ARJ Engineering · Teheran · 2003–2010 · 12 teknikere")

    # ---------------------------------------------------------------- side 3
    m.page_break()
    m.section("UDDANNELSE OG AUTORISATION")
    m.edu("Elautoriseret maskinmester — dansk elautorisation LV/MV/HV",
          "Sikkerhedsstyrelsen · maj 2023")
    m.edu("B.Tech, Technology Management and Mechanical Engineering (EQF 6)",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12")
    m.edu("El- og maskinteknisk design, Electrical Engineering (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("Køle- og VVS-teknik (AMU) · Lean: 5S, PDCA, VSM, A3",
          "Mercantec · 2021 · STCW-sikkerhedscertifikater (2021–2023)")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("**Dansk:** modersmål · **Engelsk:** professionelt, skriftligt og mundtligt · "
           "**Persisk:** modersmål · **Bor i Måløv**, godt 20 minutter til Glostrup og gerne på "
           "pladsen i hele landet · **Kørekort B** · **Kan starte efter aftale** · Referencer efter "
           "aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA Cx-PLANEN TIL EN AFLEVERING DER HOLDER",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–2",
             "Læs de kørende projekters Cx-planer, grænsefladelister og afvigelseslister; gå "
             "Sankt Lukas Hospice, Fælledby Skole og Maskincentralen igennem med den projektleder, "
             "der ejer dem, og find ud af, hvor testene i dag falder mellem to fag."),
            ("Dag 30",
             "Én Cx-plan, én grænsefladeliste og én testprotokol som ABC-standard, afprøvet på et "
             "løbende projekt; hver linje har en ejer, en dato og et acceptkriterium."),
            ("Dag 60",
             "Første aflevering kørt efter den nye standard, med afvigelser lukket på virkning og "
             "en afleveringsmappe, som driften kan overtage uden at ringe til os."),
            ("Dag 90",
             "Testvejledning og kompetenceplan for commissioning lagt frem for afdelingslederen, "
             "med to kolleger uddannet til at køre en prøvning selv — og et tal på, hvad "
             "standarderne har sparet i tid pr. projekt."),
        ],
        widths=(1500, 8830))

    m.section("EN TEST, DER IKKE KAN FEJLE, BEVISER INGENTING")
    m.para("Hvis acceptkriteriet er formuleret, så det altid opfyldes, er testen en formalitet med "
           "en underskrift på. Derfor skrives kriteriet som et interval, en responstid eller en "
           "sekvens, der kan fejle — og derfor prøves der med vilje på kanten: den højeste "
           "fremløbstemperatur, den laveste udetemperatur, den fejl der er sværest at simulere. "
           "Det er også derfor, jeg vil se instrumentets kalibrering, før jeg ser målingen. En "
           "test, der består, fordi den ikke blev svær, koster mere på 5-års gennemgangen, end den "
           "sparede i byggefasen.", after=70)

    m.section("AFLEVERINGEN ER EN OVERDRAGELSE, IKKE EN DATO")
    m.para("Afleveringsdagen er et punkt i en kontrakt; overdragelsen er det øjeblik, hvor driften "
           "kan stå alene. De to falder sjældent sammen af sig selv, så jeg planlægger baglæns fra "
           "overdragelsen: brugeruddannelsen skal ligge, før anlægget kører for alvor, "
           "driftsinstruksen skal være skrevet af dem, der har bygget det, og de sidste afvigelser "
           "skal lukkes, mens entreprenøren stadig har folk på pladsen. Ellers betaler kunden for "
           "vores aflevering i fem år.", after=70)

    m.section("STANDARDEN SKAL KUNNE BRUGES AF EN NY KOLLEGA I UGE TO")
    m.para("Et fagområde bliver først et fagområde, når det kan udføres af en anden end "
           "specialisten. Derfor bygger jeg standarder som noget, der kan læses og bruges: en "
           "Cx-plan med faste felter, en grænsefladeliste der starter som skabelon, en "
           "testprotokol med prætrykte kriterier for de typer anlæg, vi møder oftest, og en "
           "kompetenceplan med to niveauer — den, der kan prøve et anlæg efter en vejledning, og "
           "den, der kan skrive vejledningen. Det er også den eneste måde, en afdeling på halvtreds "
           "kan vokse uden at kvaliteten bliver personafhængig.", after=70)

    m.section("RÅDGIVERENS ARBEJDE ER AT SIGE DET, FØR DET KOSTER")
    m.para("Jeg har siddet på modtagersiden af rådgivning i tyve år — som elinstallatør, som "
           "entreprenør og som den, der skulle drive anlægget bagefter. Det giver en bestemt vane: "
           "at sige \"det her kan ikke prøves som beskrevet\" i projekteringen, når det koster en "
           "mail, i stedet for i uge 60, når det koster en flyttedato. Hos ABC er kunden både "
           "bygherre, investor og den driftsorganisation, der skal leve med svaret i ti år — og "
           "rådgivningen er kun noget værd, hvis den er skrevet, så alle tre kan bruge den.",
           after=70)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "DET EFTERSPØRGER DE — DET HAR JEG",
        ["Krav i opslaget", "Dokumentation"],
        [
            ("Drive commissioningprocessen som Cx-leder fra projektering til aflevering med aktiviteter, tests og dokumentation",
             "Commissioningledelse på 37 CAPEX-projekter og i egen virksomhed: aktiviteter planlagt "
             "fra projektering, tests kørt med protokol, dokumentation afleveret som én pakke."),
            ("Gennemførelse af aktiviteter, tests og dokumentation i samme sekvens",
             "Test bliver ikke en selvstændig fase: protokollen skrives i projekteringen, prøves i "
             "udførelsen og afleveres med as-built og driftsinstruks."),
            ("Planlægge og styre tid inden for egne projekter og fagområde",
             "**Fremdrift** styret baglæns fra afleveringen på 37 projekter og 11 entrepriser; "
             "testvinduer aftalt med de øvrige fag, før de blev booket."),
            ("Styre økonomi inden for egne projekter og fagområde",
             "Fuldt P&L-ansvar siden 2023: tilbud, kalkulation, timeforbrug, underentreprenører og "
             "efterkalkulation — Cx-timer prissat som en post, ikke som et tillæg."),
            ("Udvikle og forankre ABC's metoder, værktøjer og standarder inden for commissioning",
             "Skabeloner, **tjeklister** og prøveprotokoller bygget og genbrugt i egen virksomhed "
             "og på 37 projekter; egne AI-**værktøjer** til KS-tjek og dashboards."),
            ("Agere faglig sparringspartner for kolleger",
             "Sparring som en fast del af rollen: tavlemøder, faglige gennemgange før test og "
             "skriftlige notater, der kan læses af den, der ikke var med."),
            ("Opbygge commissioning-kompetencer på tværs af organisationen",
             "Oplæringsplan for tre lærlinge, AMU-kurser og **kompetence**matrix; to niveauer i "
             "Cx-uddannelsen — den, der prøver efter en vejledning, og den, der skriver den."),
            ("Relevant teknisk uddannelse som ingeniør, installationstekniker eller maskinmester",
             "**Elautoriseret maskinmester** (LV/MV/HV), B.Tech i teknologiledelse og "
             "maskinteknik (EQF 6) og el- og maskinteknisk design (EQF 6)."),
            ("Flere års erfaring med commissioning i komplekse byggeprojekter og Cx-leder eller tilsvarende rolle",
             "Tyve år med tekniske installationer og to år som commissioning- og projektleder på 37 "
             "CAPEX-projekter i reguleret byggeri — rollen udført i indhold, ikke kun i titel."),
            ("Facilitere møder, lede processer og tage styringen mellem projektets aktører",
             "Byggemøder, tavlemøder og afleveringsmøder ledet med en dagsorden, der slutter i "
             "beslutninger med navn og dato; 14 mand og 11 entrepriser koordineret samtidigt."),
            ("Rådgivererfaring",
             "El- og maskinteknisk design, specifikationer og løsningsvalg fra projekteringssiden, "
             "og tyve år på modtagersiden af rådgivning — som entreprenør, elinstallatør og "
             "driftsansvarlig."),
            ("Solid forståelse for samspillet mellem bygningens tekniske installationer",
             "**Grænseflader** mellem CTS, ventilation, el, VVS, køl og ABA prøvet fra alle sider: "
             "som udførende, som projektleder og som den, der overtog anlægget i drift."),
            ("Tage ansvaret på et projekt og gå proaktivt til værks med faglig stolthed og kvalitetsarbejde",
             "**KS** og dokumentspor som fast arbejdsform; nul kritiske fund ved aflevering på 37 "
             "projekter, og afvigelser lukket på virkning frem for på løfte."),
            ("Tværfagligt samarbejde med andre specialister og konstruktiv og effektiv kommunikation",
             "25 specialister og 11 entrepriser koordineret på samme tid; dansk med håndværkerne, "
             "engelsk med leverandørerne, og skriftligt med dem, der kom til senere."),
            ("Trives i et uformelt miljø med kort vej til beslutningstagerne",
             "Egen virksomhed med fem mand og direkte linje til kunden; beslutninger taget på "
             "pladsen og skrevet ned samme dag — korte linjer er en arbejdsform, ikke et ønske."),
            ("Fagområderne VVS, ventilation, CTS, energi og indeklima, el, kloak og bæredygtighed",
             "**VVS**, **ventilation** og køl som entreprise, **CTS** og **bygningsautomatik** i "
             "drift, **el-installationer** med **tavler** og UPS, **kloak** og procesvand fra fire "
             "år på renseanlæg, og **energi**/**indeklima**/**bæredygtighed** målt i 40 procent "
             "lavere forbrug."),
        ],
        widths=(3600, 6746))

    m.section("ET FAGLIGT FYRTÅRN ER IKKE DEN, DER VED MEST")
    m.para("Det er den, der gør viden anvendelig for andre. I praksis betyder det en Cx-standard, "
           "der er skrevet ned; en prøvevejledning, som en kollega kan bruge, første gang hun står "
           "med opgaven; en fast faglig gennemgang, hvor projektet bliver udfordret, før kunden gør "
           "det; og et kompetenceniveau, der kan måles på, hvem der selv kan køre en aflevering. Det "
           "er også den rolle, jeg helst vil have: den, folk går til, når noget skal prøves — og "
           "den, der sørger for, at svaret ikke kun findes i mit hoved.", after=80)

    m.section("HVOR JEG VILLE STARTE")
    m.para("Med de kørende projekter og den ældste linje i afvigelseslisten. Første uge: to "
           "afleveringer, der venter, og en gennemgang af, hvordan Cx-plan, grænsefladeliste og "
           "testprotokol ser ud i dag — ikke for at kritisere den, men for at se, hvor den allerede "
           "virker, og hvor den falder mellem to fag. Derefter den næste aftale, der skal vindes: "
           "en Cx-leverance, hvor kunden kan se på papiret, hvad de får for pengene.", after=0)

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_ABC_FaglederCommissioning.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_ABC_FaglederCommissioning.docx'))
