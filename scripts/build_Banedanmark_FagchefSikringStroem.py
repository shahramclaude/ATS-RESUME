# -*- coding: utf-8 -*-
"""Fagchef — Sikring & Strøm, Banedanmark (dansk opslag).

Dansk opslag -> dansk dokument, 4 sider: brev side 1, CV side 2, uddannelse + 90 dage +
metodeafsnit + "Hvor jeg ville starte" side 3, kravmatrix side 4. Format per master/README.md.
Opslaget beder om "ansøgning og CV hurtigst muligt" — formen følges ikke, brevet bliver side 1.

STILVALG (master/STILREGISTER.md; godkendt af scripts/style_guard.py, 3/3 skift mod #216):
  register      = RÅDGIVENDE — projekteringsgrundlag, udbud, leverancer, grænseflader, standarder,
                  beslutningsgrundlag. Sidst #211.
  åbningsgreb   = A (PLACEN/MISPLACERINGEN) — kvaliteten af et kørestrømsanlæg bliver ikke afgjort
                  i anlægget, men i projekteringsgrundlaget. Sidst #210.
  struktur      = PROBLEMKATALOGET — tre ting der går galt i faglig udvikling og egenprojektering,
                  hver med metode og bevis. Sidst #210.
  kadence       = korte, konstaterende sætninger med et tal eller en konsekvens i hver anden linje.

KULTURSYNKRONISERING (policy 04.11.2026), kilder i master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md
§188:
  Banedanmark, Afdelingen **Sikring & Strøm** (Trafikdivisionen/Anlægsprogrammer og Strøm): arbejder
  med "landets mest komplekse og samfundskritiske infrastrukturprojekter". Fagområdet består af
  **sikring/fjernstyring** og **strøm**; sikringsanlæggene skifter karakter og får mindre omfang i
  takt med signalsystemets udrulning, mens **strømområdet** (elektrificering, modernisering, nye
  tekniske løsninger) vokser. Rollen: faglig retning, ensartethed, fagmiljø gennem sparring,
  læring fra projekterne til standarder/metoder/arbejdsprocesser, understøttelse af
  egenprojekterings- og projekteringslederteams og udvikling af Banedanmarks **model for
  egenprojektering**; tæt samarbejde med afdelingsleder, sektionschef og teamledere. Arbejdssted
  København eller Fredericia efter bopæl, noget rejseaktivitet, fleksible arbejdstider og
  hjemmearbejde. Kontakt: **ledende sektionschef for Sikring og Strøm, Osama Hussein, 2518 3291**.
  Ansættelse som specialkonsulent eller chefkonsulent (akademikeroverenskomst), pension 18,07 %.
  Banedanmarks mission, værdier (ambition, respekt, ansvar) og ledelsesgrundlag er de samme som i
  §186 og bruges ikke igen som citat her — dokumentet taler i stedet fagets sprog.

Faglige fakta (bane.dk, Anlægsplan 2030, bæredygtighedsstrategi, FT.dk-statusrapporter):
  S-banen er **100 % elektrificeret**; ca. **41 %** af fjernbanesporene er elektrificerede i dag, og
  frem mod **2027** skal fjernbanen dække ca. **80 %**. Folketinget har afsat op til **12 mia. kr.**
  til elektrificering af ca. **1.350 km** jernbane. Elektrificeringen Fredericia-Aarhus-Aalborg
  ibrugtages ultimo **2026** (køreplan 27); kørestrømsanlægget kan opsættes før det nye
  signalsystem, men kan først **ibrugtages** efter — medmindre strækningen **immuniseres** mod
  elektrisk støj. Egenprojektering: Banedanmark køber primært projektering i markedet og
  egenprojekterer kun i begrænset omfang (sikring/fjernstyring, scopefasen i udvalgte sporprojekter);
  på kørestrøm har over halvdelen af projekteringslederne været eksterne ressourcepersoner, og
  markedet for signal- og sikringsteknisk projektering er smalt.

Ingen opdigtede fakta. Dokumenteret grundlag: el- og maskinteknisk design (EQF 6) og elautorisation
LV/MV/HV; 37 CAPEX-projekter som senior idriftsættelsesingeniør/projektleder med 25 specialister,
FAT/SAT, IQ/OQ/PQ, nul kritiske fund, ændringsstyring i SAP og dokumentation læst af myndigheden
(Novo Nordisk 2022-2024); 14 mand og 11 samtidige entrepriser med eget værksted (Ventek-Air 2022);
5 elektrikere + 3 lærlinge med fuldt P&L, tilbud, beregning og afleveringsdokumentation (ELOHVAC
2023-); 24/7-drift med HV-tavler, SRO/SCADA og vagtordning (Biofos 2017-2022); 12 teknikere (ARJ
2003-2010); B.Tech EQF 6 (7,6/12); dansk modersmål, engelsk professionelt, kørekort B.
**Ingen påstand om kørestrøms-, signal- eller jernbaneprojektering.**
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Fagchef · Sikring & Strøm · projektering, standarder og faglig udvikling'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("10. november 2026")
    m.meta("Fagchef · Afdelingen Sikring & Strøm · Banedanmark")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Fagchef til Sikring & Strøm", bold=True, color='1A1A1A')
    m.para("Kære Osama,", after=60)

    # ---------------------------------------------------------------- side 1
    m.para("**Kvaliteten af et kørestrømsanlæg bliver ikke afgjort i anlægget.** Den bliver afgjort "
           "i **projekteringsgrundlaget** — i den ene antagelse om, hvordan anlægget skal "
           "**immuniseres** mod det nye **signalsystem**, som ingen fik udfordret, før entreprisen "
           "var i **udbud**. Når først udbuddet er sendt, er der to veje tilbage: en ændringssag "
           "eller en løsning, der bliver dyrere i drift. Det er den slags beslutninger, en **fagchef** "
           "skal ind og tage stilling til, mens de stadig er billige.", after=80)

    m.para("**Banedanmark er midt i den bevægelse: en bæredygtig jernbane, der skal køre på el.** "
           "S-banen er fuldt **elektrificeret**, omkring "
           "**41 procent** af fjernbanesporene er det, og frem mod **2027** skal det være cirka "
           "**80 procent** — på en portefølje, hvor der er afsat op til **12 mia. kr.** til omkring "
           "**1.350 km bane**. Samtidig skifter sikringsanlæggene karakter, når signalsystemet ruller "
           "ud, og på **kørestrøm** har over halvdelen af projekteringslederne været eksterne. Derfor "
           "er **egenprojektering** ikke et princip. Det er en kapacitet, der skal bygges — og det er "
           "den opgave, jeg søger.", after=80)

    m.para("**Problem 1: Budgettet bliver først prøvet i byggefasen.** Et **budget** er ikke et tal, "
           "der skal holde; det er en række antagelser, der skal holde. Derfor skal krav, "
           "**grænseflader** og **forudsætninger** være afklaret, før udbuddet går ud, og den "
           "**bygbare løsning** skal være tegnet sammen med dem, der skal bygge den. Jeg har ført 37 "
           "CAPEX-**anlægsprojekter** og 11 samtidige entrepriser, hvor ændringen blev vurderet på "
           "**risici** og tid, før arbejdet startede — ikke efter.", after=80)

    m.para("**Problem 2: Læringen bliver i projektet.** Erfaring bliver først til **metode**, når "
           "nogen skriver den ned og prøver den af igen. Derfor hører **erfaringsudveksling** og "
           "**læring** hjemme i en fast rytme: hvad gik galt, hvorfor, og hvad ændrer vi i "
           "**standarder** og **arbejdsprocesser** i morgen. Jeg har kørt samme kontrol og samme "
           "acceptkriterier på elleve parallelle sager, og jeg har lukket **afvigelser** på rodårsag "
           "under GMP/FDA/EMA med **nul kritiske fund** som resultat.", after=80)

    m.para("**Problem 3: Standarden findes, men bliver ikke brugt.** En **standard**, der er skrevet "
           "uden dem, der skal arbejde efter den, bliver et dokument i en mappe. Derfor bliver "
           "**metoder** og arbejdsinstruktioner skrevet med teknikerne, prøvet af på et anlæg og "
           "gennemgået en gang om året. Det er også sådan, **kompetenceudvikling** bliver noget "
           "andet end et kursuskatalog: superbruger i hver vagtgruppe, sidemandsoplæring og en "
           "kompetencematrix, der viser, hvem der kan hvad.", after=80)

    m.para("**Et fag, der bliver mindre, skal ikke bare lukkes ned.** Når sikringsanlæggene "
           "gradvist får mindre omfang, er den største risiko ikke, at opgaverne forsvinder, men at "
           "viden gør det — den viden, der sidder hos dem, der har projekteret anlæggene, og som "
           "ikke står i nogen **standard**. Den skal samles, mens den stadig er der, og skrives ned, "
           "før folkene går videre til **strøm**opgaverne. Ellers betaler vi for den samme erfaring "
           "to gange.", after=80)

    m.para("**Faglig ledelse er ikke personaleansvar.** Det er at sætte en retning, som de fagligt "
           "stærke kan arbejde inden for, og at være den, der spørger, hvorfor vi gør det på den måde. Jeg "
           "har ledet gennem fagligt ansvarlige på 37 projekter med 25 specialister og arbejdet i "
           "**tværfaglige** snitflader mod indkøb, myndighed og drift; **sparring** har været en fast "
           "del af ugen, ikke et årligt seminar.", after=80)

    m.para("**Strømområdet vokser ikke af sig selv.** Det vokser af **lavspænding**, "
           "**mellemspænding** og **højspænding**, der bliver projekteret rigtigt første gang, af "
           "**tavler** og beskyttelse, der passer til den last, der kommer, og af nogen, der kan "
           "**idriftsætte** og **overlevere** uden at efterlade åbne punkter i **dokumentationen**. "
           "Jeg er uddannet el- og maskinteknisk designer og **elautoriseret maskinmester** "
           "(LV/MV/HV), og jeg har stået på begge sider af bordet: som den, der projekterer og "
           "beregner, og som den, der skal drive og vedligeholde det bagefter.", after=80)

    m.para("**En løsning bliver først god, når den, der skal drive den, kan bruge den.** Fire år "
           "med **højspænding**stavler, SRO/SCADA og akut fejlfinding har givet mig den vane at "
           "spørge driftsteknikeren, før tegningen låses: kan den fejlfindes, kan reservedelen skaffes, "
           "og står der en klemme, hvor nogen skal bruge den kl. 03? Det spørgsmål bliver sjældent "
           "stillet i et **udbud**, og det er derfor, det skal stilles i **projekteringsgrundlaget**.", after=80)

    m.para("**Praktisk.** Jeg bor i Måløv, har kort til København, og rejserne til Fredericia og ud "
           "på anlæggene er en del af arbejdet. **Dansk** som modersmål, **engelsk** på "
           "professionelt niveau. **Kørekort B.** Kan tiltræde efter aftale.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("El-teknisk specialist og projektleder med tyve år i **projektering**, **idriftsættelse** "
           "og drift af el-anlæg — **lavspænding**, **mellemspænding** og **højspænding**, "
           "**tavler**, UPS og styring. 37 CAPEX-**anlægsprojekter** med 25 specialister og nul "
           "kritiske fund; 11 samtidige entrepriser; eget værksted med 14 mand. "
           "**Elautoriseret maskinmester** (LV/MV/HV) og uddannet i el- og maskinteknisk design.", after=80)

    m.section("PROJEKTERING OG TEKNISK GRUNDLAG")
    for label, body in [
        ("El-teknisk design",
         "**Projektering** af **tavler**, forsyning og styring — belastningsberegning, selektivitet, "
         "komponentvalg og **dokumentation**, der kan bygges og drives efter."),
        ("Grænseflader og krav",
         "**Grænseflader** mod ventilation, køl, ABA/ABV og bygningsautomatik afklaret i "
         "**projekteringsgrundlaget**; krav specificeret, så de kan bestilles og afprøves."),
        ("Myndighed og standarder",
         "**Standarder** og **myndighedskrav** som ramme for løsningen — DS/HD 60364, "
         "**lavspænding**sinstallationer og **højspænding**sanlæg dokumenteret til aflevering."),
    ]:
        m.bullet(label, body)

    m.section("GENNEMFØRELSE, ØKONOMI OG LEVERANCER")
    for label, body in [
        ("Budget og kalkulation",
         "**Budget**, tilbud og efterkalkulation med fuldt P&L; **bygbare løsninger** valgt på pris, "
         "drift og risiko — ikke på hvad der var nemmest at tegne."),
        ("Udbud og leverandører",
         "**Udbud** og aftalegrundlag, underentreprenører og **leverancer** styret på møde, "
         "**dokumentation** og opfølgning; **overlevering** med åbne punkter lukket."),
        ("Idriftsættelse",
         "**Idriftsættelse** med FAT/SAT, sekvenser prøvet af og **risici** gennemgået, før "
         "anlægget blev spændingssat; nul kritiske fund ved aflevering."),
    ]:
        m.bullet(label, body)

    m.section("FAGLIG UDVIKLING OG SAMARBEJDE")
    for label, body in [
        ("Metode og læring",
         "**Læring** fra projekterne samlet i faste gennemgange og skrevet ind i "
         "**arbejdsprocesser** og instrukser — samme standard på elleve sager."),
        ("Sparring og kompetence",
         "**Sparring** ved opgaven, sidemandsoplæring og **kompetenceudvikling** som plan pr. "
         "medarbejder; tre lærlinge uddannet med egen plan."),
        ("Tværfagligt arbejde",
         "**Tværfagligt** samarbejde med indkøb, teknik, **myndighed** og drift i 37 projekter; "
         "**interessenter** hørt, før løsningen blev låst."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Ejer / teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · fuldt P&L · projektering, beregning og aflevering")
    m.bullet("Egenprojektering i lille skala",
              "Tilbud, beregning, tegning og **dokumentation** lavet in-house, med samme "
              "acceptkriterier på alle sager; nul kritiske afvigelser i serviceaftalerne.")

    m.job("Senior idriftsættelsesingeniør / projektleder",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024",
          scope="37 CAPEX-anlæg · 25 specialister · GMP/FDA/EMA · SAP")
    m.bullet("Teknisk grundlag og ændring",
              "Ændringer risikovurderet og godkendt før arbejdet startede; **dokumentation** i SAP, "
              "der kunne læses af **myndigheden**, og nul kritiske fund ved aflevering.")

    m.job("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · eget værksted")
    m.bullet("Elleve sager, én standard",
              "**Udbud**, aftalegrundlag og **leverancer** styret ens på 11 parallelle opgaver; "
              "flaskehalse flyttet, inden de blev til forsinkelser.")

    m.job("Drifts- og vedligeholdelseschef", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="Renseanlæg i 24/7-drift · pumper, HVAC, HV-tavler, SRO/SCADA")
    m.bullet("Driftssiden af projektet",
              "Fire år med **højspænding**stavler, SRO/SCADA og akut fejlfinding — den erfaring, "
              "der gør en projekteret løsning nem eller svær at drive.")

    m.job("Produktionsformand / elektromekaniker",
          "ARJ Engineering · Teheran · 2003–2010 · 12 mekanikere og teknikere")
    m.bullet("Første lederrolle",
              "Vagtplan, fordeling og oplæring i et værksted med maskiner, værktøj og tegninger i "
              "daglig brug.")

    # ---------------------------------------------------------------- side 3
    m.page_break()
    m.section("UDDANNELSE OG AUTORISATION")
    m.edu("Elautoriseret maskinmester — dansk elautorisation LV/MV/HV",
          "Sikkerhedsstyrelsen · maj 2023")
    m.edu("B.Tech, Technology Management and Mechanical Engineering (EQF 6)",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12")
    m.edu("El- og maskinteknisk design, Electrical Engineering (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("Lean: 5S, PDCA, VSM, A3 · køle- og VVS-teknik (AMU) · STCW-sikkerhed",
          "Mercantec 2021 · Søfartsstyrelsen 2021–2023")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("**Dansk:** modersmål · **Engelsk:** professionelt, skriftligt og mundtligt · "
           "**Persisk:** modersmål · **Bor i Måløv** — København er hverdagen, Fredericia og "
           "anlæggene er rejsedage · **Kørekort B** · **Kan tiltræde efter aftale** · Referencer "
           "efter aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA PROJEKTBANK TIL EN FÆLLES STANDARD",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–2",
             "Læs de seneste projekter igennem — projekteringsgrundlag, udbud, ændringssager og "
             "afleveringer — og find ud af, hvor mange af ændringerne der startede som en "
             "**forudsætning**, ingen havde skrevet ned. Mød projekteringslederne på begge "
             "lokationer."),
            ("Dag 30",
             "Et fælles billede af, hvor **budgettet** bliver til teknik: de fem hyppigste "
             "**grænseflader**, der bliver afklaret for sent, og hvilke **standarder** der findes på "
             "papir men ikke i praksis. En ejer og en dato på hver."),
            ("Dag 60",
             "Den første **metode** omskrevet sammen med dem, der skal bruge den, og prøvet af i et "
             "løbende projekt; **sparring** i fast rytme med teamlederne og en "
             "**kompetenceudvikling**splan for **strøm**området, der peger på næste års opgaver."),
            ("Dag 90",
             "En fælles **standard** for projekteringsgrundlag på **strøm** med krav, grænseflader og "
             "**bygbare løsninger** beskrevet; **læring** fra kvartalets projekter lukket ind i "
             "**arbejdsprocesserne**, og modellen for **egenprojektering** beskrevet med bemanding "
             "og mandat."),
        ],
        widths=(1500, 8830))

    m.section("ET UDBUD ER ET BESLUTNINGSGRUNDLAG, IKKE EN TEKNISK BESKRIVELSE")
    m.para("Når udbuddet går ud, er de valg, der koster penge, allerede taget. Derfor skal "
           "**projekteringsgrundlaget** kunne læses af en entreprenør uden at gætte, og de "
           "**grænseflader**, der ikke er løst, skal stå som risici med en ejer — ikke som en "
           "fodnote. Det er den forskel, der afgør, om ændringerne kommer som få og dyre eller "
           "mange og billige.", after=70)

    m.section("ERFARING BLIVER FØRST TIL METODE, NÅR DEN ER SKREVET NED OG PRØVET IGEN")
    m.para("**Erfaringsudveksling** er ikke et møde, hvor nogen fortæller, hvad der gik galt. Det er "
           "en **arbejdsproces**: hændelsen bliver beskrevet, årsagen fundet, ændringen skrevet ind i "
           "**standarden**, og effekten efterprøvet i det næste projekt. Jeg har gjort det med "
           "**afvigelser** under GMP/FDA/EMA, hvor en lukket sag blev læst igen efter 60 dage — og "
           "hvor en gentagelse betød, at lukningen havde været for hurtig.", after=70)

    m.section("STRØMOMRÅDET VOKSER IKKE AF SIG SELV — DET VOKSER AF KOMPETENCER")
    m.para("**Elektrificering** er ikke et program, der bliver færdigt; det er et fag, der skal "
           "kunne mere om **kørestrøm**, **stærkstrøm** og **immunisering**, end markedet kan levere "
           "i dag. Derfor er **kompetenceudvikling** en del af **egenprojektering**en: hvem kan "
           "projektere hvad, hvem skal lære det af hvem, og hvad skal vi købe ude, indtil vi kan "
           "selv. En **kompetencematrix** gør den samtale konkret — og gør det muligt at sige nej til "
           "en opgave, før den bliver dyr.", after=70)

    m.section("EN STANDARD SKAL KUNNE BRUGES KL. 07.00 EN MANDAG")
    m.para("**Standarder** bliver ikke bedre af at være lange. De bliver bedre af at blive brugt, og "
           "de bliver brugt, når de svarer på det spørgsmål, der står i projektet: hvad skal jeg gøre "
           "her, hvad må jeg ikke, og hvem godkender. Derfor skal hver **metode** have en ejer, en "
           "version og en gennemgangsdato — og skal prøves af i et rigtigt projekt, før den bliver "
           "obligatorisk.", after=70)

    m.section("HVOR JEG VILLE STARTE")
    m.para("I projekteringsgrundlaget for det næste **strøm**projekt, der er tæt på udbud. Første "
           "uge: læs de sidste tolv måneders ændringssager igennem og find ud af, hvor mange af dem "
           "der startede som en **forudsætning**, ingen havde skrevet ned. Derefter tage den største "
           "fællesnævner og gøre den til en **standard** — sammen med dem, der skal arbejde efter "
           "den.", after=0)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "DET EFTERSPØRGER DE — DET HAR JEG",
        ["Krav i opslaget", "Dokumentation"],
        [
            ("Erfaren specialist med solid faglig baggrund inden for **sikring** eller **strøm** og "
             "omkring 8 års erfaring som projekterende ingeniør",
             "Tyve år i el-teknisk **projektering**, idriftsættelse og drift; **elautoriseret** "
             "maskinmester (LV/MV/HV) og uddannet i el- og maskinteknisk design (EQF 6) — "
             "beregning, tegning og aflevering lavet selv, også under tidspres."),
            ("Erfaring med **projektering**, planlægning og gennemførelse af sikrings- eller "
             "**strøm**projekter",
             "37 CAPEX-**anlægsprojekter** og 11 entrepriser: teknisk grundlag, **udbud**, "
             "gennemførelse og **overlevering** med nul kritiske fund."),
            ("Omsætte store **budgetter** til teknisk **bygbare løsninger** i samarbejde med fagets "
             "specialister",
             "**Budget**, kalkulation og efterkalkulation med fuldt P&L; løsninger valgt med "
             "25 specialister og entreprenøren i samme beslutning."),
            ("Sætte retning for **fagligheden** og sikre høj **kvalitet** og **ensartethed** i "
             "løsningerne",
             "Samme kontrol og acceptkriterier på 11 parallelle sager og på 37 anlæg; én "
             "**standard**, der blev fulgt, fordi den var skrevet med dem, der brugte den."),
            ("Udvikle **fagmiljøet** gennem **sparring** og tæt **tværfagligt** samarbejde",
             "**Sparring** ved opgaven og i fast ugentlig rytme; **tværfagligt** arbejde med indkøb, "
             "teknik, **myndighed** og drift i 37 projekter."),
            ("Indsamle **læring** fra projekterne og bruge den til at udvikle **standarder**, "
             "**metoder** og **arbejdsprocesser**",
             "**Læring** samlet i faste gennemgange og skrevet ind i arbejdsinstrukser; "
             "**afvigelser** lukket på rodårsag og efterprøvet efter 60 dage."),
            ("Udfordre og understøtte **egenprojekterings**- og **projekteringsledelse**teams i "
             "planlægning og gennemførelse",
             "Ledelse gennem fagligt ansvarlige på 37 projekter med 25 specialister; "
             "**projekteringsledelse** prøvet i praksis i eget selskab og på 11 entrepriser."),
            ("Bidrage til udviklingen af Banedanmarks model for **egenprojektering**",
             "**Egenprojektering** i lille skala med fuldt P&L siden 2023: beregning, tegning, "
             "**dokumentation** og aflevering lavet in-house, med samme standard hver gang — og "
             "med erfaring i at vide, hvornår opgaven skal købes ude i stedet."),
            ("Understøtte udviklingen af **strøm**området, hvor **elektrificering**, modernisering og "
             "nye tekniske løsninger får større betydning",
             "**Lavspænding**, **mellemspænding** og **højspænding** projekteret og idriftsat; "
             "**tavler**, UPS og forsyning på 37 anlæg — og fire år med drift og vedligehold af "
             "HV-anlæg, hvor belastning, selektivitet og reservedele er hverdag."),
            ("Sikre og videreudvikle de eksisterende faglige kompetencer og samtidig styrke kapacitet "
             "og **faglighed** inden for **strøm**",
             "**Kompetenceudvikling** som plan pr. medarbejder og kompetencematrix; tre lærlinge "
             "uddannet, superbruger i hver vagtgruppe ved nye systemer."),
            ("Være med til at sætte retningen for, hvordan kompetencer, **metoder** og organisering "
             "tilpasses fremtidens opgaver",
             "Arbejdsgange og organisation bygget om i eget selskab og i eget værksted: beslutning "
             "og udførelse i samme uge, med en ejer og en dato."),
            ("Arbejde tæt sammen med afdelingsleder, sektionschef og **teamledere** om højt fagligt "
             "niveau og medarbejdernes udvikling",
             "Tolv år med personaleansvar og tæt ledelsessamarbejde; MUS og 1:1 hvert år, og "
             "faglighed løftet gennem oplæring frem for kontrol."),
            ("Fremme den teknologiske udvikling og kendskab til branchens teknologier, trends og "
             "udvikling",
             "Nye systemer indført i drift med superbrugere og fejltræning; **signalsystem** og "
             "**immunisering** læst som tekniske forudsætninger, der skal koordineres."),
            ("Kombinere teknisk faglighed med faglig ledelse, strategisk udvikling og tæt samarbejde "
             "med projekterne",
             "**Fagchef**-rollen udøvet som fagligt ansvar uden personaleansvar: retning, metoder og "
             "**sparring** — sideløbende med egen projektering."),
            ("Analysere komplekse problemstillinger struktureret og løsningsorienteret, forstå "
             "**risici** og **forudsætninger** på tværs af projekter",
             "Risici og forudsætninger løftet ud af projekterne og ind i fælles lister med ejer; "
             "A3, 5xHvorfor og Ishikawa som fast problemløsningsmetode."),
            ("Bevæge sig mellem konkrete tekniske problemstillinger og langsigtet udvikling og skabe "
             "resultater gennem andre",
             "Fra tavlen i værkstedet til **standarder** og **strategi** i eget selskab; resultater "
             "skabt gennem 25 specialister, 14 mand og 12 teknikere — ikke alene."),
        ],
        widths=(3600, 6746))

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_Banedanmark_FagchefSikringStroem.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_Banedanmark_FagchefSikringStroem.docx'))
