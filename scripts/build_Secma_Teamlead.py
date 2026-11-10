# -*- coding: utf-8 -*-
"""Secma — Teamlead, medicoteknisk service, Skævinge (Hillerød).

Dansk opslag → dansk dokument (da-DK): ansøgning side 1, CV side 2, uddannelse + 90 dage +
fire afsnit side 3, kravmatrix side 4.

STILVALG (master/STILREGISTER.md, policy 04.11.2026; godkendt af scripts/style_guard.py,
3/3 skift mod #195):
  register      = KUNDESERVICE — menneske først, relation, responstid, tillid. Rollen er en
                  servicefunktion, hvor kunden ringer med et problem, og svaret skal kunne
                  handles på. Sidst brugt #186.
  åbningsgreb   = I (TESERNE) — tre påstande om hvad der afgør, om en sag bliver løst samme dag;
                  resten af brevet beviser dem. Sidst brugt #188.
  struktur      = KUNDEREJSEN — henvendelsen → afklaringen → udførelsen → afslutningen → næste
                  gang. Sidst brugt #186.
  kadence       = kort, mundtlig, kundevendt; ét trin ad gangen, med hvad kunden ser.

Ingen opdigtede fakta: der påstås IKKE erfaring med ultralyds-, shockwave- eller laserudstyr og
ikke erfaring fra et medicoteknisk serviceværksted. Det dokumenterede grundlag er elautoriseret
maskinmester (LV/MV/HV), el- og maskinteknisk design (EQF 6), B.Tech, fejlfinding på elektronik,
styringer og CTS/SCADA, FAT/SAT og IQ/OQ/PQ i GMP/FDA/EMA-miljø, service og akutudkald med
kundedialog i egen virksomhed, SAP ERP og Power BI samt koordinering af 37 samtidige sager og
14 mand / 11 entrepriser. Norsk og svensk påstås IKKE som flydende.

Policy: master/README.md — jobbet først, kandidaten kun som bevis, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Teamlead · Medicoteknisk service, support og fejlfinding'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4. november 2026")
    m.meta("Secma · Teamlead, medicoteknisk service · Møllerisvej 4, 3320 Skævinge")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: teamlead — medicoteknisk service", bold=True, color='1A1A1A')
    m.para("Til Annette Brændstrup Møller, Møller & Partners", after=70)

    # ---------------------------------------------------------------- side 1
    m.para("**Tre ting afgør, om en servicesag bliver løst samme dag.** Hvad der bliver spurgt om i "
           "det første minut · om den rigtige reservedel er på lager, eller om nogen tør sige, at den "
           "ikke er · og om kunden hører fra os, før kunden ringer igen. Det er de tre ting, jeg "
           "gerne vil være med til at holde styr på i en **serviceafdeling**, hvor teknik, "
           "**kundesupport** og koordinering ikke er tre opgaver, men én.", after=80)

    m.para("**Henvendelsen.** En **kundeoplevelse** bliver afgjort i de første to minutter, og det er "
           "sjældent teknikeren på **værkstedet**, der afgør den — det er den, der tager telefonen. Jeg "
           "har taget den slags opkald i egen virksomhed siden 2023: akutudkald til el-, ventilations- "
           "og klimaanlæg, hvor den, der ringer, er frustreret og har brug for at vide, hvad der sker "
           "nu. Min første sortering er altid den samme: kan det løses over telefonen, skal der en "
           "tekniker ud, eller skal sagen videre til en, der ved mere end jeg. At sige det højt med "
           "det samme er også en del af svaret.", after=80)

    m.para("**Afklaringen.** Når en sag ikke kan klares på stedet, begynder den systematiske "
           "**fejlfinding**: hvad virker, hvad virker ikke, hvornår blev det sidst set, og hvad er "
           "blevet ændret siden. På **medicinsk udstyr** er der typisk flere fejlkilder end én — "
           "føleren, kablet, softwareindstillingen eller den, der har brugt udstyret. Jeg har "
           "fejlfundet på motorer, frekvensomformere, følere, **CTS** og SCADA og ved, at den "
           "hurtigste vej sjældent er at skifte dele i rækkefølge efter pris. Først når jeg kan sige, "
           "hvorfor det skete, kan jeg sige, hvad det koster.", after=80)

    m.para("**Udførelsen.** Mindre **reparation** og **test** på værkstedet er noget af det, jeg har "
           "gjort længst. Jeg har verificeret og idriftsat anlæg med FAT/SAT, IQ/OQ/PQ og **validering** "
           "i GMP/FDA/EMA-miljø, hvor hver test skulle kunne læses af en tredjemand bagefter, og hvor "
           "**dokumentation** var en del af arbejdet og ikke noget, man skrev bagefter. Den samme "
           "disciplin vil jeg bruge på **kalibrering** og på funktionskontrol: en **test**, der ikke "
           "er skrevet ned, er en mening. Og når udstyret står hos en kunde, der skal bruge det i "
           "morgen, betyder det, at testen skal kunne forklares i telefonen.", after=80)

    m.para("**Afslutningen.** En sag er ikke lukket, når den er repareret; den er lukket, når kunden "
           "ved, hvad der skete, og hvad der er aftalt. **Garantisager** er særligt følsomme, fordi "
           "de handler om, hvem der betaler — og fordi kunden sjældent har læst betingelserne, da "
           "udstyret blev købt. Jeg har stået med afvigelser, hvor et manglende bilag stoppede en "
           "aflevering, og med **servicekontrakt**er, hvor det, der ikke stod i aftalen, blev det, "
           "der blev diskuteret. Derfor skriver jeg hellere for kort end for pænt, og ringer hellere "
           "én gang for meget.", after=80)

    m.para("**Næste gang.** Det er her, en **service**afdeling bliver bedre end sin egen travlhed. "
           "Hvis de samme tre fejl kommer igen, er det ikke kundens brug af udstyret, der er "
           "problemet, men vores **proces**. Jeg har bygget **KPI**-dashboards i **Power BI** og "
           "arbejdet i **SAP ERP** med sagsdata, og jeg ved, hvad der kan hentes ud af en "
           "**responstid**, en gentagelsesprocent og en lukketid, hvis nogen gider kigge på det hver "
           "uge. En **SLA**, der ikke bliver holdt, er værre end ingen aftale. Det er også den slags, "
           "jeg gerne vil **optimere** i en nyoprettet rolle, hvor arbejdsgangene ikke er låst endnu.", after=80)

    m.para("**Hvad jeg ikke har, og hvad jeg har i stedet.** Jeg har ikke serviceret **ultralyd**- eller "
           "**shockwave**udstyr og ikke arbejdet med terapeutisk **laser**. Jeg har heller ikke siddet "
           "i et medicoteknisk **ticketsystem**. Det, jeg har, er 20+ år med fejlfinding på "
           "elektronik og styringer, test og dokumentation i et reguleret miljø, og en "
           "servicehverdag med akutudkald, hvor kunden er et menneske, der har ondt — eller en klinik, "
           "der ikke kan behandle, fordi udstyret står stille. Den del er ikke ny for mig, og "
           "resten lærer jeg hurtigere, end de fleste tror, fordi jeg har lært nye anlæg at kende "
           "hele mit arbejdsliv.", after=80)

    m.para("**Rollen som bindeled** — uden **personaleansvar** — passer mig godt. Jeg har prøvet begge "
           "sider: personaleansvar for 5 elektrikere og 3 lærlinge og koordinering af 14 mand på 11 "
           "samtidige entrepriser. Det, der flytter noget i en serviceorganisation, er ikke, at nogen "
           "bestemmer; det er, at nogen sørger for, at **salg**, **backoffice** og **logistik** ved, "
           "hvad der er lovet kunden, og hvornår. Det er den rolle, jeg søger.", after=80)

    m.para("Secma ligger 20 minutter fra Måløv, og jeg kender omgivelserne omkring Skævinge. Jeg har "
           "læst, at stillingen er nyoprettet — det er en af grundene til, at jeg søger den: der er "
           "noget at forme, og jeg vil hellere være med til at bygge **arbejdsgange**ne end til at "
           "overtage nogen andens. Jeg kan tiltræde snarest.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Teknisk servicetekniker og leder med 20+ års erfaring i **fejlfinding**, reparation, test og "
           "kundedialog — **elautoriseret maskinmester** (LV/MV/HV), el- og maskinteknisk design "
           "(EQF 6), B.Tech i teknologiledelse og maskinteknik. Har verificeret og idriftsat anlæg med "
           "FAT/SAT og IQ/OQ/PQ i GMP/FDA/EMA-miljø med nul kritiske fund, drevet service og "
           "akutudkald med fuldt P&L siden 2023, styret 37 samtidige sager i SAP ERP og bygget "
           "**KPI**-dashboards i Power BI.", after=80)

    m.section("TEKNISK SUPPORT OG FEJLFINDING")
    for label, body in [
        ("Systematisk fejlfinding",
         "Fejlfinding på motorer, frekvensomformere, følere, elektronik, CTS og SCADA: hvad virker, "
         "hvad er ændret, og hvad koster det at teste i den forkerte rækkefølge. A3, 5xHvorfor og "
         "Ishikawa som metode, ikke som pligt."),
        ("Test og dokumentation",
         "FAT/SAT og IQ/OQ/PQ med protokoller skrevet før testen og nul kritiske fund; "
         "funktionskontrol, kalibrering og afvigelser dokumenteret, så en tredjemand kan følge "
         "sporet bagefter."),
        ("Reparation og værksted",
         "Reparation og prøvekørsel i værksted og på stedet; el-tekniske installationer, tavler og "
         "styring fra elautorisationen — grænsen mellem mekanik, elektronik og software er ikke en "
         "grænse, jeg stopper ved."),
    ]:
        m.bullet(label, body)

    m.section("SERVICE, KUNDER OG AFTALER")
    for label, body in [
        ("Kundesupport og akutudkald",
         "Telefonisk support og udkald for erhvervskunder siden 2023: første afklaring, forventning "
         "om tid og pris meldt ud med det samme, og opfølgning efter besøget."),
        ("Prioritering af sager",
         "Daglig prioritering mellem akut, planlagt og garanti ud fra konsekvens for kunden — i "
         "døgndrift på Lynetten, hvor et stop ikke kunne vente til mandag."),
        ("Aftaler og økonomi",
         "Servicekontrakter, tilbud og kalkulation, garantiforhold og fakturagrundlag; fuldt "
         "P&L-ansvar siden 2023 og investeringsvurdering (NPV/IRR) ved reparér-eller-udskift."),
    ]:
        m.bullet(label, body)

    m.section("SYSTEMER, DATA OG FORBEDRING")
    for label, body in [
        ("Systemstærk i hverdagen",
         "SAP ERP, Power BI, Excel/Power Query og Python; egne tjeklister og dashboards bygget, fordi "
         "det var hurtigere end at vente på en rapport."),
        ("Data om sager og tid",
         "Sagsdata brugt til at se gentagne fejl, responstid og lukketid; forbedringer valgt på "
         "grundlag af det, ikke på mavefornemmelse."),
        ("Koordineret på tværs",
         "Salg, indkøb, lager og teknik koordineret i 11 entrepriser og 37 projekter — med tavlemøder "
         "og en fast rytme for opfølgning."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Ejer / teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · service, akutudkald og projekter · fuldt P&L")
    m.bullet("Service og kundekontakt",
              "Telefonisk afklaring, udkald og opfølgning hos erhvervskunder; egen vagtordning og "
              "aftaler om responstid — kunden skal vide, hvornår der er en på vej.")
    m.bullet("Drift af forretningen",
              "Tilbud, kalkulation og fakturering; AI-værktøjer til tidsplaner, tjeklister og KPI — "
              "over 40 % produktivitetsløft på de administrative opgaver.")

    m.job("Senior idriftsættelsesingeniør / projektleder, elsystem",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024",
          scope="37 samtidige anlægsprojekter · 25 specialister · GMP/FDA/EMA")
    m.bullet("Verifikation og afvigelser",
              "FAT/SAT og IQ/OQ/PQ: protokoller skrevet før testen, afvigelser lukket med "
              "rodårsagsanalyse — nul kritiske fund ved aflevering. Fremdrift og økonomi i SAP ERP.")

    m.job("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · DKK 2–10 mio.")
    m.bullet("Koordinering og aflevering",
              "Daglige tavlemøder og flaskehalsanalyser; prøvekørsel, dokumentation og aflevering til "
              "kunden — og opfølgning, når der kom en mangel efter overdragelsen.")

    m.job("Vedligeholdelses- og driftsleder", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="Renseanlæg i 24/7-drift · pumper, HVAC, højspændingstavler, SCADA")
    m.bullet("Akut fejlfinding i døgndrift",
              "Prioritering af indsats efter konsekvens, ikke efter hvem der ringede først; 5S og "
              "standard work på værksted og lager, LOTO og APV.")

    m.job("Elektromekaniker / produktionsteamleder",
          "ARJ Engineering · Teheran · dec. 2003–mar. 2010 · 12 mekanikere og teknikere")

    # ---------------------------------------------------------------- side 3
    m.page_break()
    m.section("UDDANNELSE OG AUTORISATION")
    m.edu("Elautoriseret maskinmester — dansk elautorisation LV/MV/HV",
          "Sikkerhedsstyrelsen · maj 2023")
    m.edu("B.Tech, teknologiledelse og maskinteknik (EQF 6)",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12")
    m.edu("El- og maskinteknisk design, elteknik (EQF 6)", "Tehran Technical University · 2000–2003")
    m.edu("Køleteknik & klimaanlæg (AMU)", "Mercantec · 2021")
    m.edu("Lean-/forbedringspraksis: 5S, PDCA, VSM, A3, Kaizen · STCW sikkerhedskurser (2021–2023)",
          "Mercantec / Søfartsstyrelsen")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("**Dansk:** modersmål · **Engelsk:** professionelt, skriftligt og mundtligt · **Persisk:** "
           "modersmål · Norsk og svensk læses uden besvær; jeg påstår ikke at tale dem flydende · "
           "**Bosat i Måløv**, ca. 20 minutter til Skævinge · **Kan tiltræde snarest** · Referencer "
           "efter aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA FØRSTE HENVENDELSE TIL LUKKET SAG",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–2",
             "Lytte med på **kundesupport** og læse de sidste tre måneders sager igennem: hvilke "
             "henvendelser kommer igen, og hvor mange bliver lukket i første opkald? Sidde med på "
             "**værkstedet** og se, hvordan udstyret faktisk opfører sig."),
            ("Dag 30",
             "Egen sagsportefølje med **prioritering** og **opfølgning**; **responstid** og lukketid "
             "målt på et helt månedligt datasæt, så vi ved, hvor vi står — ikke hvor vi tror."),
            ("Dag 60",
             "Forslag til én konkret forbedring af en **proces** (f.eks. hvordan en garantisag bliver "
             "oprettet, så **salg** og **backoffice** ser det samme) med tal fra vores egne sager "
             "bag det."),
            ("Dag 90",
             "Etableret rytme for **sparring** med teknikerne og for opfølgning med **logistik** om "
             "**reservedele**; status med Service Manager på, hvad jeg løser selv, og hvad der stadig "
             "skal læres om udstyret."),
        ],
        widths=(1500, 8830))

    m.section("EN SAG ER IKKE LUKKET, FORDI DEN ER REPARERET")
    m.para("Det er fristelsen i en travl **serviceafdeling**: at sætte fluebenet, når udstyret kører "
           "igen, og gå videre til den næste. Men kunden ringer ikke tilbage for at høre, om det "
           "virkede — kunden ringer tilbage, hvis det ikke gjorde, og så er det dyrere for alle. En "
           "**kundeoplevelse** bliver skabt i det sidste opkald, ikke i det første: her er hvad der "
           "var galt, her er hvad vi gjorde, og her er, hvad du skal være opmærksom på. Det er også "
           "den eneste måde, **kvalitet** bliver målbar i en serviceafdeling: ikke på hvor mange sager "
           "vi lukker, men på hvor mange der ikke kommer igen.", after=70)

    m.section("JEG SPØRGER HELLERE EN GANG FOR MEGET")
    m.para("Telefonsupport er et håndværk, og det består mest i at stille spørgsmål, der lyder "
           "dumme. Hvilken fejlkode stod der? Hvornår begyndte det? Har I flyttet på noget? Det er "
           "sjældent den avancerede diagnose, der løser sagen; det er det spørgsmål, ingen gad stille, "
           "fordi det virkede for indlysende. Jeg har prøvet at stå på den anden side som tekniker og "
           "fået en sag, hvor alle detaljer manglede — og jeg har prøvet at være den, der spurgte.",
           after=70)

    m.section("DET ER IKKE MIG, DER SKAL HAVE ÆREN — DET ER KUNDEN, DER SKAL HAVE SVARET")
    m.para("Når en sag går godt, er der altid nogen i **salg** eller på **værkstedet**, der har gjort "
           "en forskel. Min rolle er at sørge for, at det, der blev lovet i telefonen, også er det, "
           "der sker — og at sige det højt, når noget ikke kan lade sig gøre i dag. Tillid i en "
           "serviceorganisation bliver ikke bygget på, at man aldrig fejler, men på at man melder ud, "
           "før kunden opdager det.", after=70)

    m.section("DET JEG IKKE HAR PRØVET — OG DET JEG HAR")
    m.para("Jeg har ikke arbejdet med **medicoteknisk** udstyr som **ultralyd**, **shockwave** eller "
           "**laser**, og jeg kender ikke **sundhedssektor**ens arbejdsgange fra inde i en klinik. "
           "Det, jeg har, er tyve år med at lære nye anlæg at kende på den måde, der virker: læse "
           "dokumentationen, spørge den, der har prøvet det, og selv stå med det. **Fejlfinding** er "
           "ikke branchespecifik; det er en metode, og metoden har jeg brugt på alt fra "
           "højspændingstavler til følere, der gav forkert signal.", after=0)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "HVAD STILLINGEN KRÆVER — HVAD JEG HAR LEVERET",
        ["Krav i opslaget", "Bevis"],
        [
            ("Erfaring inden for medicoteknisk udstyr",
             "Ikke medicoteknisk udstyr. Erfaring fra beslægtet teknisk branche: fejlfinding, test og "
             "dokumentation i GMP/FDA/EMA-miljø (Novo Nordisk) og service på el-, ventilations- og "
             "klimaanlæg."),
            ("Teknisk baggrund: elektriker, automatiktekniker, elektronik-/svagstrømstekniker, industritekniker, maskinmester eller ingeniør",
             "Elautoriseret maskinmester (LV/MV/HV), el- og maskinteknisk design (EQF 6) og B.Tech i "
             "teknologiledelse og maskinteknik — to af de nævnte uddannelser, plus elektronik og "
             "styring i praksis."),
            ("Erfaring med teknisk kundesupport og sparring med kolleger",
             "Telefonisk support og udkald siden 2023; sparring med 25 specialister i 37 projekter og "
             "med teknikere på 11 entrepriser — teknisk sparring uden at være den, der bestemmer."),
            ("Håndtering af henvendelser via telefon, mail og ticketsystemer",
             "Telefon og mail i egen virksomhed som primær kanal; sagsstyring i SAP ERP på 37 "
             "samtidige sager. Ikke et medicoteknisk ticketsystem — det lærer jeg i uge et."),
            ("Vurdering, prioritering og koordinering af serviceopgaver",
             "Daglig prioritering mellem akut, planlagt og garanti; koordinering af 14 mand og 11 "
             "entrepriser på tavlemøder, og af 37 projekter på tværs af engineering og indkøb."),
            ("Første afklaring og fejlfinding på tekniske problemer",
             "Første afklaring over telefonen som fast del af servicen; fejlfinding på motorer, "
             "frekvensomformere, følere, elektronik, CTS og SCADA med A3 og 5xHvorfor."),
            ("Planlægning og opfølgning på igangværende sager",
             "Fremdrift og økonomi fulgt ugentligt i SAP ERP og Power BI; egne dashboards for "
             "responstid, lukketid og gentagne fejl."),
            ("Mindre reparationer, test og fejlfinding på værkstedet",
             "Reparation og prøvekørsel i værksted og på stedet; FAT/SAT og IQ/OQ/PQ med protokoller "
             "skrevet før testen og nul kritiske fund ved aflevering."),
            ("Håndtering af service- og garantisager",
             "Servicekontrakter, aftalegrundlag og garantiforhold håndteret i egen virksomhed; "
             "afvigelser lukket med rodårsagsanalyse og dokumenteret, så sagen kunne forklares "
             "bagefter."),
            ("Optimering af arbejdsgange, systemer og processer",
             "Tjeklister, dashboards og AI-værktøjer indført med over 40 % produktivitetsløft på det "
             "administrative; 5S og standard work på værksted og lager."),
            ("Tæt samarbejde med salg, backoffice og logistik",
             "Salg, indkøb, lager og teknik koordineret i egen virksomhed og i 11 entrepriser; "
             "leverancepakker og fakturagrundlag afstemt med backoffice."),
            ("Systemstærk og komfortabel i en digital hverdag",
             "SAP ERP, Power BI, Excel/Power Query og Python — værktøjer bygget selv, når de manglede, "
             "inklusive investeringsmodeller og automatiserede tjeklister."),
            ("Arbejder struktureret og tager ansvar for at få opgaver afsluttet",
             "Egen virksomhed drevet siden 2023 med ansvar for alt fra første opkald til sidste "
             "faktura; A3, PDCA og standard work som arbejdsform."),
            ("Kan bevare overblikket i en hverdag med både planlagte og akutte opgaver",
             "Fire år i 24/7-drift, hvor planen blev afbrudt af nedbrud; akutudkald ved siden af "
             "planlagte opgaver i egen virksomhed."),
            ("Kommunikerer sikkert på dansk og engelsk og er fortrolig med skandinaviske sprog",
             "Dansk modersmål, engelsk professionelt skriftligt og mundtligt; norsk og svensk læses "
             "uden besvær — flydende tale på dem påstås ikke."),
            ("Koordinerende bindeled mellem kunder og interne funktioner, uden personaleansvar",
             "Bindeled i praksis: kunde, tekniker, salg og lager i egen virksomhed; har også prøvet "
             "den anden model med personaleansvar for 5 + 3 og ved forskellen."),
        ],
        widths=(3600, 6746))

    m.section("EN TICKET ER ET LØFTE, IKKE EN HUSKESEDDEL")
    m.para("Når en sag bliver skrevet ind, er der givet et eller andet håb videre til kunden — om tid, "
           "om pris eller bare om at nogen kigger på det. Derfor skal **ticket**en indeholde det, den "
           "næste har brug for, og ikke det, den første syntes var sjovt at skrive. Jeg har set sager "
           "gå i stå, fordi der stod \"defekt\" i stedet for, hvad der var defekt. Det koster en "
           "time ekstra hver gang, og det er den time, kunden venter i.", after=70)

    m.section("HVOR JEG VILLE STARTE")
    m.para("Med at lytte og med at se på de sidste tre måneders sager. Ikke for at finde ud af, hvem "
           "der har gjort noget forkert, men for at finde de tre ting, der går igen: en type "
           "henvendelse, der altid tager for lang tid, en **reservedel**, der aldrig er på hylden, og "
           "en aftale mellem **salg** og service, der bliver fortolket forskelligt. Det er der, en "
           "nyoprettet rolle kan gøre en forskel fra den første måned.", after=0)

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_Secma_Teamlead.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_Secma_Teamlead.docx'))
