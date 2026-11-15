# -*- coding: utf-8 -*-
"""Lead Engineer, køleanlæg og varmepumper — Johnson Controls (Sabroe), Holme/Aarhus (dansk opslag).

Dansk opslag -> dansk dokument, 4 sider: brev side 1, CV side 2, uddannelse + 90 dage +
metodeafsnit + "Hvor jeg ville starte" side 3, kravmatrix side 4. Format per master/README.md.
Opslaget skriver: "Hvis du ønsker at inkludere en motiveret ansøgning, så tilføj denne i dit CV,
så det hele ligger i samme PDF" — formen følges ikke: brevet bliver side 1, og hele pakken er én
PDF, som de beder om.

STILVALG (master/STILREGISTER.md; godkendt af scripts/style_guard.py, 3/3 skift mod #218):
  register      = KONSTRUKTIONSBORD — komponentniveau, enheder (kW, kPa, °C, COP), tryk, temperatur,
                  test, dokumentation, tør humor, ingen corporate-engelsk. Nyt register; nærmest
                  beslægtet med *ingeniør-præcis* (#214), men uden standard- og compliance-tale.
  åbningsgreb   = G (SPØRGSMÅLET) — "Hvor mange steder i en varmepumpe kan en komponent skiftes,
                  uden at nogen skal regne efter?" Sidst #211/#181.
  struktur      = MÅLESTOKKEN — hver sektion på side 1 åbner med et tal fra fabrikken og hvad det
                  betyder (1897 · 122 °C · 95 °C · 27 MW · 2 300 m²). Sidst #181.
  kadence       = korte sætninger, ét tal eller én enhed pr. linje, ingen tillægsord uden en måling.

KULTURSYNKRONISERING (policy 04.11.2026), kilder i master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md
§190:
  **Johnson Controls Danmark ApS** — i Danmark kendt som **Sabroe** med isbjørnen; grundlagt 1897 af
  ingeniør **Thomas Th. Sabroe** ved Aarhus havn, købt af **York** 1999 (407 mio. dollar) og en del
  af **Johnson Controls** siden **2005**. Fabrikken ligger i **Holme** ved Aarhus og laver
  kundetilpassede **Sabroe-varmepumper og -chillere** samt **remanufactured, aftermarket og marine
  reservedele**; ca. **700** medarbejdere i Danmark (2022, 125 år). Sabroes egen tone: "teknisk,
  engageret og fokuseret på at levere produkter i verdensklasse til tiden", "den daglige
  kommunikation er uformel, humoristisk og direkte", "rig mulighed for at forme sin egen hverdag",
  "se teorien realiseret i fysiske produkter", og fabrikkens eget løfte: "al data er dokumenteret og
  produkterne er gennemtestede før de forlader fabrikken i Holme".

  Fakta brugt i dokumentet (Johnson Controls pressemeddelelser 2024-2026, Sabroe-brochure, Cooling
  Post, NaturalRefrigerants.com, Sustainability/Manufacturing Digital):
  * Fabrikken i Holme dækker ca. **14 hektar**; **R&D-testcentret** har testet Sabroe-produkter i
    mere end **20 år**.
  * Udvidelsen (meldt sept. **2024**, stod færdig i **2026**): **+2 300 m²** produktion og
    **+1 800 m²** test- og kundecenter, **100+** nye job og **fordoblet** kapacitet af store
    varmepumper. Anlægget kører på **100 % grøn energi**.
  * **HicaHP** (ammoniak, R717): **2-25 MW**, op til **95 °C** fremløb, **SAB407** skruekompressor
    med højt tryk, system-COP op til **4,2**.
  * **HitemHP** (butan/isobutan, ultra-lav GWP): op til **122 °C**, ca. **100 kW-1 MW**, bygget på
    **SMC**-stempelkompressoren, testet i Holme, 10 konfigurationer.
  * **DualPAC** (to-trins ammoniak): f.eks. Seinäjoki, Finland — tre enheder à ca. **1,6 MW**,
    **4,9 MW** i alt, ca. 2 000 husstande; Utrecht, Holland — fire HicaHP, **27 MW**, ca. **15 %** af
    byens fjernvarme, ca. **30 000 t CO2/år** mindre; Berlin-Buch — **700 kW**; Marstal — to
    **716 HPX**; Zurich — **42 MW**.
  * Kølemidler i porteføljen: **ammoniak (R717)**, **CO2 (R744)**, **propan (R290)**, butan/isobutan —
    naturlige kølemidler, positioneret mod **EU's F-gasregler** med stramninger i **2027** og **2030**.
  * Markedet: over **60 %** af den energi, europæisk industri bruger, går til **varme** (European Heat
    Pump Association, citeret af JCI).

Ingen opdigtede fakta. Dokumenteret grundlag: **B.Tech, Technology Management and Mechanical
Engineering** (EQF 6, 2017-2022, 7,6/12), **el- og maskinteknisk design** (EQF 6), **elautoriseret
maskinmester** LV/MV/HV (maj 2023) og **køle- og VVS-teknik** (AMU 2021); dimensionering af
køleanlæg og varmeflader, kanaler, armatur og styring samt tegninger og tavler (ELOHVAC 2023-);
**37 CAPEX-anlæg** med FAT/SAT, nul kritiske fund, SAP-ændringsstyring og dokumentation læst af
myndigheden (Novo Nordisk 2022-2024); **14 mand og 11 samtidige entrepriser** med eget værksted og
leverandørstyring (Ventek-Air 2022); fire år med **HV-tavler, pumper, HVAC, SRO/SCADA** og akut
fejlfinding i 24/7-drift (Biofos 2017-2022); **12 teknikere** (ARJ 2003-2010); dansk modersmål,
engelsk professionelt; kørekort B; Måløv.
**Bevidst formulering:** ingen påstand om at have udviklet kompressorer eller serieprodukter, om at
have været ansvarlig for en PED-kategorivurdering, eller om at have arbejdet med ammoniak- og
CO2-anlæg i drift. Flytning til Aarhus-området står som forudsætning, fordi opslaget kræver dagligt
fremmøde i Holme.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Lead Engineer · køleanlæg og varmepumper · beregning, konstruktion og test'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("10. november 2026")
    m.meta("Lead Engineer, køleanlæg og varmepumper · Johnson Controls (Sabroe) · Holme, Aarhus")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Lead Engineer til køleanlæg og varmepumper", bold=True, color='1A1A1A')
    m.para("Kære Marco,", after=60)

    # ---------------------------------------------------------------- side 1
    m.para("**Hvor mange steder i en varmepumpe kan en komponent skiftes, uden at nogen skal regne "
           "efter?** Ingen steder. En anden kompressor flytter tryktrinnet. En anden varmeveksler "
           "flytter temperaturdifferencen. Et andet kølemiddel flytter hele kurven. Oveni ligger "
           "**PED**-dokumentationen, testen og de tyve års service, som komponenten også skal holde "
           "i. Det er den slags regnestykke, jeg gerne vil sidde med hver dag — og det er derfor, "
           "jeg søger rollen som **Lead Engineer** i Holme.", after=80)

    m.para("**1897.** Fabrikken i Holme har lavet kølemaskiner, siden ingeniør Thomas Th. Sabroe "
           "grundlagde virksomheden ved Aarhus havn — og Sabroe har været en del af **Johnson "
           "Controls** siden 2005. Deres eget løfte om produkterne er, at «al data er dokumenteret og "
           "produkterne er gennemtestede, før de forlader fabrikken». Det er ikke en "
           "marketingformulering; det er beskrivelsen af et **konstruktionsbord**, hvor beregning, "
           "test og dokumentation er samme arbejdsgang. **Testcentret** har kørt i mere end tyve år, "
           "og udvidelsen, der blev meldt i 2024 og stod færdig i 2026, lagde **2 300 m²** produktion "
           "og **1 800 m²** test- og kundecenter til på de cirka **14 hektar**. Det er den slags "
           "investering, man kun laver, hvis nogen kan regne efter bagefter.", after=80)

    m.para("**122 °C.** Det er, hvad **HitemHP** kan levere med butan og isobutan — bygget på "
           "SMC-stempelkompressoren, testet i Holme, ti konfigurationer fra cirka **100 kW** til "
           "**1 MW**. Og **95 °C** er HicaHP-familiens fremløb med **ammoniak**: **2-25 MW**, "
           "skruekompressoren **SAB407** og system-**COP** op til **4,2**. Ved de temperaturer er "
           "komponentvalget ikke et katalogopslag. Det er **termodynamik** og tryk — og når "
           "kølemidlet samtidig er naturligt, er sikkerhed, **EN 378**, **PED** og **F-gas**-reglerne en "
           "del af samme beregning.", after=80)

    m.para("**27 MW.** Så stor er den samlede varmepumpeinstallation, Sabroe leverede til Utrechts "
           "fjernvarme — fire HicaHP-enheder, der dækker omkring **15 %** af byens behov og sparer "
           "cirka **30 000 ton CO2** om året. I Seinäjoki giver tre DualPAC-enheder **4,9 MW** til omkring "
           "2 000 husstande, og i Berlin-Buch står en enhed på **700 kW** og erstatter fossil "
           "spidslast. Det er **grøn omstilling** målt i ton CO2 og ikke i billedsprog — og den slags "
           "projekt i **industrien** skal køre **energieffektiv** drift og være **bæredygtig** "
           "i tyve år, fordi nogen regnede rigtigt i starten. Når én enhed er "
           "6-7 MW, er der ikke «lidt» plads til en fejl i "
           "dimensioneringen — og **dokumentationen** skal følge produktet i samme tempo som "
           "beregningen.", after=80)

    m.para("**Det, jeg kan lægge på bordet.** Termodynamik, **konstruktion** og komponentvalg fra "
           "maskinmester- og B.Tech-niveauet i maskinteknik, plus **køle- og VVS-teknik** fra AMU. "
           "Jeg har **dimensioneret** køleanlæg, varmeflader, kanaler, armatur og styring og tegnet "
           "det, der blev bygget efter. Jeg har kørt **FAT/SAT** og sekvenser på 37 anlæg med **nul "
           "kritiske fund** ved aflevering, og jeg har skrevet den **dokumentation**, en myndighed "
           "skulle kunne læse fem år senere. Det er tre ting, der ligner produktudvikling mere, end "
           "titlen antyder: regn det, prøv det, skriv det ned.", after=80)

    m.para("**Hvor jeg står med PED.** Jeg kender **PED** som ramme — kategorierne efter tryk og "
           "volumen, CE-mærkning, de grundlæggende sikkerhedskrav og den dokumentation, der følger "
           "med — og jeg har arbejdet med trykbærende systemer: pumper, HVAC, trykluft og "
           "varmevekslere. Jeg har ikke været den, der skrev kategorivurderingen på en trykbeholder, "
           "og det siger jeg, fordi I skal kunne bruge mit svar i et møde. Til gengæld læser jeg "
           "direktivet, når det er det, opgaven kræver.", after=80)

    m.para("**Viden, der bliver i hovedet på én konstruktør, forsvinder ved første "
           "organisationsændring.** Derfor er **vidensdeling** ikke et personalegode; det er en "
           "del af produktet. Jeg har bygget komponent- og leverandørdokumentation, der blev "
           "brugt af andre end mig, oplært tre lærlinge og skrevet afvigelser op, så de kunne læses "
           "af den næste. **Support** på tværs af afdelinger er ikke noget, jeg skal tage stilling "
           "til; det er sådan, et teknisk hus fungerer.", after=80)

    m.para("**Praktisk.** Jeg bor i Måløv, og Holme er omkring tre og en halv time væk — det er en "
           "**flytning**, ikke en pendling — og da rollen er med dagligt fremmøde, er det en "
           "forudsætning, jeg er indstillet på. **Elautoriseret maskinmester** (LV/MV/HV), B.Tech "
           "i Technology Management and Mechanical Engineering (EQF 6, 7,6/12). **Dansk** som "
           "modersmål, **engelsk** professionelt. **Kørekort B.** Kan tiltræde efter aftale.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Konstruktions- og idriftsættelsesingeniør med tyve år i køle-, varme- og eltekniske "
           "anlæg. Har dimensioneret køleanlæg og varmeflader, valgt komponenter og skrevet "
           "dokumentationen, der blev bygget og godkendt efter; 37 anlæg med FAT/SAT og nul "
           "kritiske fund. **Elautoriseret maskinmester** (LV/MV/HV) og **B.Tech** i maskinteknik — "
           "vant til at regne, prøve og dokumentere i samme arbejdsgang.", after=80)

    m.section("BEREGNING, KONSTRUKTION OG KOMPONENTER")
    for label, body in [
        ("Dimensionering",
         "Køleanlæg, varmeflader, kanaler, armatur og styring dimensioneret efter belastning, "
         "trykfald og temperaturløft; tegninger og komponentlister, der kunne bygges efter."),
        ("Komponent- og leverandørviden",
         "Komponenter valgt og fravalgt på data, tolerancer og driftstimer — og dokumenteret, så "
         "valget kunne forsvares to år senere."),
        ("Termodynamik og tryk",
         "Køle- og VVS-teknik (AMU 2021) oveni maskinmester- og B.Tech-niveauet; tryktrin, "
         "kølemiddel og varmeveksler regnet som en kreds, ikke som enkeltdele."),
    ]:
        m.bullet(label, body)

    m.section("TEST, DOKUMENTATION OG MYNDIGHED")
    for label, body in [
        ("FAT/SAT og sekvenser",
         "Prøver ved grænsen, ikke ved nominel last; 37 anlæg godkendt med nul kritiske fund ved "
         "aflevering."),
        ("Dokumentation",
         "Beregnings- og afleveringspakker, ændringsstyring i SAP og sporbarhed, der bestod "
         "myndighedens gennemlæsning under GMP/FDA/EMA."),
        ("Standarder og rammer",
         "PED som trykbærende ramme, EN 378 som kølemiddelramme og F-gasreglerne som den "
         "tidsplan, hele branchen arbejder efter."),
    ]:
        m.bullet(label, body)

    m.section("DRIFT, SUPPORT OG VIDENSKAB")
    for label, body in [
        ("Anlæg i drift",
         "Fire år med HV-tavler, pumper, HVAC og SRO/SCADA i 24/7 — fejlfinding, reservedele og "
         "opgraderinger på det, andre havde bygget."),
        ("Support på tværs",
         "Vidensdeling med produktion, indkøb, teknik og myndighed; oplæring af tre lærlinge og "
         "skriftlige procedurer, andre kunne bruge."),
        ("Selvstændigt arbejde",
         "Eget selskab siden 2023 med fuldt P&L: tilbud, beregning, udførelse og aflevering uden "
         "en bagkant at læne sig på."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Ejer / teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · fuldt P&L · projektering og komponentvalg")
    m.bullet("Regne, vælge, bygge",
              "Køleanlæg og varmeflader dimensioneret, komponenter valgt på data og "
              "afleveringsdokumentation skrevet til kunden.")

    m.job("Senior idriftsættelsesingeniør / projektleder",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024",
          scope="37 anlægsprojekter · 25 specialister · FAT/SAT · GMP/FDA/EMA · SAP")
    m.bullet("Testen som fag",
              "Sekvenser, grænseværdier og afvigelser prøvet af før overlevering; nul kritiske fund "
              "og dokumentation, myndigheden kunne læse uden at ringe.")

    m.job("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · eget værksted")
    m.bullet("Elleve sager, én rytme",
              "Komponenter, leverancer og kapacitet koordineret, så flaskehalse blev flyttet, før "
              "de blev forsinkelser.")

    m.job("Drifts- og vedligeholdelseschef", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="Renseanlæg i 24/7-drift · HV-tavler, pumper, HVAC, SRO/SCADA")
    m.bullet("Anlægget efter afleveringen",
              "Fire år med tryk, temperatur og måling i praksis — den erfaring, der gør en "
              "konstruktion nem eller svær at servicere.")

    m.job("Produktionsformand / elektromekaniker",
          "ARJ Engineering · Teheran · 2003–2010 · 12 mekanikere og teknikere")
    m.bullet("Første tekniske lederrolle",
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
    m.edu("Køle- og VVS-teknik (AMU) · Lean: 5S, PDCA, VSM, A3 · STCW-sikkerhed",
          "Mercantec 2021 · Søfartsstyrelsen 2021–2023")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("**Dansk:** modersmål · **Engelsk:** professionelt, skriftligt og mundtligt · "
           "**Persisk:** modersmål · **Bor i Måløv** og søger stillingen med **flytning til "
           "Aarhus-området** for øje · **Kørekort B** · **Kan tiltræde efter aftale** · Referencer "
           "efter aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA KOMPONENT TIL PRODUKTPROGRAM",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–2",
             "Læs produktprogrammet bagfra: de tre familier (stempel, skrue, HicaHP/HitemHP), fem "
             "igangværende udviklingssager og testcentret. Mød konstruktion, produktion, service og "
             "eftermarked."),
            ("Dag 30",
             "Regn en eksisterende enhed efter — samme tal som den frigivne beregning — og find ud "
             "af, hvor usikkerheden sidder: kølemiddel, tryktrin, veksler eller rør. Afvigelser "
             "skrevet ned med rodårsag."),
            ("Dag 60",
             "Én komponentvejledning med acceptkriterier, ført ind i det system, hvor "
             "konstruktion og service allerede søger, og prøvet af på to sager."),
            ("Dag 90",
             "En fast vej tilbage fra service og eftermarked til konstruktion — én rytme, én ejer, "
             "ét sted — plus en liste over, hvor PED- og EN 378-dokumentationen halter i dag."),
        ],
        widths=(1500, 8830))

    m.section("EN BEREGNING, DER IKKE KAN GENSKABES, ER EN MENING")
    m.para("En beregning er kun et svar, hvis den næste kan komme til samme tal med de samme "
           "antagelser. Derfor skal kølemiddel, tryktrin, temperaturer, enheder og version stå "
           "skrevet ned sammen med resultatet — ikke i en mail fra i fredags. Jeg har set, hvad det "
           "koster, når en ændring blev gennemført uden at grundlaget fulgte med: så skal nogen "
           "regne det hele om, og det er altid dyrere end at skrive det ned første gang.", after=70)

    m.section("PED ER IKKE PAPIR — DET ER ET TRYK, NOGEN SKAL KUNNE FORSVARE")
    m.para("Kategorierne efter tryk og volumen, CE-mærkningen og de grundlæggende sikkerhedskrav "
           "findes, fordi udstyret kan slå mennesker ihjel, når det svigter. I praksis betyder det, "
           "at en komponentændring også er en dokumentationsændring, og at den, der godkender, skal "
           "kunne pege på beregningen. Jeg har ikke været ansvarlig for en kategorivurdering — men "
           "jeg har prøvet at stå med et anlæg, hvor papirerne ikke passede til det, der var bygget, "
           "og det er en fejl, man kun laver én gang.", after=70)

    m.section("TESTCENTRET ER DEN BILLIGSTE MÅDE AT TAGE FEJL PÅ")
    m.para("En fejl, der findes på prøvestand, koster en arbejdsdag. Den samme fejl hos kunden koster "
           "en vogn, to teknikere og et forhold. Derfor prøver jeg ved grænsen og ikke ved nominel "
           "last: opstart, nedlukning, delftast, den kolde nat og den varme eftermiddag. På 37 anlæg "
           "gav det nul kritiske fund ved aflevering — fordi fejlene blev fundet, mens de stadig var "
           "billige.", after=70)

    m.section("KOMPONENTVIDEN BLIVER FØRST VÆRDI, NÅR ANDRE KAN FINDE DEN")
    m.para("Et produktprogram er ikke en mappe med tegninger. Det er viden om, hvorfor netop denne "
           "veksler, denne kompressor og dette kølemiddel blev valgt, og hvad der skete i drift. Den "
           "viden skal ligge et sted, hvor en sælger, en servicetekniker og en ny konstruktør kan "
           "finde den — ellers bliver den genopfundet hvert tredje år. Jeg har bygget den slags "
           "dokumentation før, og jeg ved, at det kun holder, hvis dem, der skal bruge den, har "
           "været med til at lave den.", after=70)

    m.section("SELVSTÆNDIG BETYDER IKKE ALENE")
    m.para("Jeg kan arbejde selvstændigt i ugevis med en beregning, der ikke vil gå op — og jeg "
           "kan lide det. Men **support** og **vidensdeling** er ikke det modsatte; det er den "
           "måde, et teknisk miljø bliver klogere på. Når en kollega i en anden afdeling spørger, "
           "svarer jeg samme dag, og hvis svaret er «det ved jeg ikke», står der et navn i mit svar "
           "om, hvem der gør.", after=70)

    m.section("HVOR JEG VILLE STARTE")
    m.para("Ved beregningen, ikke ved mødet. Første uge: regn en eksisterende HicaHP-enhed efter fra "
           "grundlaget og se, om jeg kommer til det samme tal som den frigivne beregning — hvor jeg "
           "ikke gør, er der en antagelse, der ikke står skrevet ned. Derefter tage den komponent, "
           "der bliver spurgt mest til, og gøre den til en vejledning, som konstruktion, service og "
           "eftermarked kan bruge samme sted.", after=0)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "DET EFTERSPØRGER DE — DET HAR JEG",
        ["Krav i opslaget", "Dokumentation"],
        [
            ("**Ingeniøruddannelse** inden for **mekanik** eller lignende",
             "**B.Tech** i Technology Management and **Mechanical Engineering** (EQF 6, 7,6/12), "
             "el- og maskinteknisk **design** (EQF 6) og **elautoriseret maskinmester** LV/MV/HV "
             "(maj 2023)."),
            ("Viden om **termodynamik**",
             "**Køle- og VVS-teknik** (AMU 2021) og termodynamik på maskinmester-/B.Tech-niveau; "
             "**køleanlæg** og varmeflader **dimensioneret** med tryktrin, **temperatur**løft og "
             "**COP** regnet igennem."),
            ("Viden om **konstruktion**",
             "**Design** og **dimensionering** af forsyning, **varmevekslere**, armatur og "
             "**komponenter**; tegninger og komponentlister, der blev bygget efter — på 37 anlæg "
             "og i eget selskab."),
            ("Viden om **PED**",
             "PED (2014/68/EU) som ramme: kategorier efter **tryk** og volumen, CE, grundlæggende "
             "sikkerhedskrav og **dokumentation**; arbejdet med trykbærende systemer (pumper, HVAC, "
             "trykluft). Ikke ansvarlig for kategorivurdering."),
            ("Relevant erfaring inden for lignende område",
             "Tyve år i **køle**-, varme- og eltekniske anlæg: **beregning**, **konstruktion**, "
             "**test** og **support** — fra **komponent**valg til aflevering."),
            ("**Proaktiv** i dit arbejde",
             "Taget initiativ før det blev efterspurgt: ændringer rejst, mens de var billige, og "
             "**dokumentation** lavet, før nogen spurgte efter den."),
            ("Bidrage til **vidensdeling** med kolleger og resten af virksomheden",
             "**Komponent**- og leverandørdokumentation bygget til andre end mig; tre lærlinge "
             "oplært; procedurer skrevet, så næste kunne bruge dem."),
            ("**Ansvarsfuld** og **resultatorienteret** person",
             "Fuldt P&L siden 2023 og **projekt**ansvar for 37 CAPEX-anlæg: **resultat** målt på "
             "godkendt aflevering og **nul kritiske fund**."),
            ("Evne til at skabe **overblik**",
             "37 **anlæg**, 25 specialister og 11 **entrepriser** på samme tavle; én **plan**, én "
             "status, samme tal til alle."),
            ("Struktureret og **analytisk** tilgang",
             "Samme skabelon og kontrolpunkter hver gang, ændringsstyring i SAP og afvigelser "
             "analyseret til rodårsag — ikke til undskyldning."),
            ("Nyder at arbejde **selvstændigt**",
             "Eget selskab siden 2023: **beregning**, tilbud, udførelse og aflevering drevet uden "
             "en bagkant at læne sig på."),
            ("**Teamplayer** — **support** og **vidensdeling** på tværs af afdelinger",
             "Support til produktion, indkøb, teknik og myndighed; tværfaglige fora hvor svaret kom "
             "samme dag, også når svaret var et navn."),
            ("**Udvikling af nye produkter**",
             "Produktnært udviklingsarbejde: nye **komponenter** valgt, **test**et og dokumenteret, "
             "og koncepter ændret, når målingen viste noget andet end antagelsen."),
            ("**Vedligeholdelse** og **support** af eksisterende produkter",
             "Fire år i 24/7-drift og siden egen serviceforretning: fejlfinding, reservedele og "
             "opgraderinger på anlæg, andre havde konstrueret."),
            ("**Beregninger** af **køleanlæg**, **varmepumper** og diverse **komponenter**",
             "Belastning, **tryk**fald, **varmeveksler**e og **kompressor**valg regnet igennem og "
             "skrevet ned; **kølemiddel** og **temperatur** behandlet som ét system."),
            ("**Opsamle viden** om **komponenter** og produkter og deres anvendelse til udvikling "
             "af **produktprogrammet**",
             "**Komponent**viden dokumenteret med acceptkriterier og driftserfaring, så den kunne "
             "bruges af konstruktion, service og **eftermarked** — ikke kun af mig."),
            ("Dagligt fremmøde på **udviklingskontoret i Holme**",
             "Bor i Måløv i dag og søger med **flytning** til **Aarhus**-området for øje; "
             "**kørekort** B og klar til fremmøde fra første dag."),
            ("**Uformel**, **humoristisk** og **direkte** kommunikation i et teknisk team",
             "Tyve år på gulvet i **dansk** teknisk miljø: kort, konkret og uden omveje — også når "
             "budskabet er, at beregningen ikke holder."),
        ],
        widths=(3600, 6746))

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_JohnsonControls_LeadEngineer.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_JohnsonControls_LeadEngineer.docx'))
