# -*- coding: utf-8 -*-
"""Artelia — Projektleder, Energi & Industri (rådgiver), Aarhus C.

Dansk opslag → dansk dokument: ansøgning p1, CV p2, uddannelse + 90 dage +
fire sektioner p3, kravmatrix p4.
Vinkel: rådgiveren skal kunne begge sider af bordet — skrive det udbud, en
entreprenør kan prissætte, og følge udførelsen, så intentionen bliver realiseret.
Policy: master/README.md — jobbet først, kandidaten kun som bevis, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Projektleder, Energi & Industri · Rådgivning, udbud og udførelse'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Danmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("8. november 2026")
    m.meta("Artelia Danmark · Energi & Industri · Aarhus C")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Projektleder — Energi & Industri (rådgiver)", bold=True, color='1A1A1A')
    m.para("Til John Brinkmann, Claus Christian Skov Nielsen og fagmiljøet i Energi & Industri", after=70)

    # ---------------------------------------------------------------- side 1
    m.para("Et udbud bliver afgjort, længe før tilbuddene kommer ind. Det bliver afgjort i, hvor præcist "
           "kravet er beskrevet, i om grænsefladerne er navngivet, og i om den, der skriver det, selv har "
           "stået med opgaven på en byggeplads. Det er derfor, jeg søger rådgiversporet hos Artelia: Jeg har "
           "været på begge sider af bordet — som entreprenør, der skulle prissætte andres udbud, og som "
           "bygherres projektleder, der skulle stå med resultatet.", after=80)

    m.para("**Rollens kerne er at give kunden et beslutningsgrundlag, der holder.** Ikke en præsentation med "
           "tre muligheder og ingen anbefaling, men et valg med konsekvenser skrevet ud: hvad det koster, "
           "hvad det betyder for driften, hvilke **risici** der følger med, og hvad der sker, hvis man vælger "
           "det andet. Jeg har siddet med den beslutning på **37 parallelle CAPEX-projekter** af 2–10 mio. kr. "
           "hos Novo Nordisk, hvor teknik, **økonomi** og fremdrift skulle gå op samtidig — og i egen "
           "virksomhed, hvor kunden er en, man ringer tilbage til i morgen.", after=80)

    m.para("**Energi- og industrisegmentet — forsyningsselskaber og industrivirksomheder — kender jeg fra "
           "indersiden af driften.** Jeg har været driftsleder "
           "på Lynetten under Biofos, et **forsyningsselskab** i 24/7-drift med pumper, HVAC, "
           "højspændingstavler og SCADA, hvor der ikke var noget at forhandle om, hvis anlægget stod stille. "
           "Jeg har leveret til pharma-produktion under **GMP/FDA/EMA**, og jeg har drevet "
           "**energieffektivisering** med dokumenteret effekt: **40 % lavere energiomkostninger** på et "
           "PDCA-program og **over 40 % lavere forbrug** på Lynetten. Det er de anlæg og den drift, "
           "kundernes projekter ender i.", after=80)

    m.para("**Projektering og fagdiscipliner har jeg styret, ikke blot deltaget i.** Som elautoriseret "
           "maskinmester (LV/MV/HV) har jeg projekteret el-tekniske anlæg, dimensioneret, koordineret med "
           "ventilation, HVAC og styring og kvalitetssikret arbejdet, inden det blev bygget. På Novo Nordisk "
           "var det **25 specialister** på tværs af teknik, indkøb og drift, hvor snitfladerne mellem "
           "fagdisciplinerne var min opgave — og hvor **FAT/SAT** og **IQ/OQ/PQ** var de kontroller, der "
           "afgjorde, om intentionen var realiseret.", after=80)

    m.para("**Udbud, forhandling og kontrahering er noget, jeg har gjort med penge på bordet.** Jeg har "
           "siddet med tilbudslisten, prissat arbejde, forhandlet vilkår og skrevet under på "
           "aftalegrundlaget — med **AB 18**, **totalentreprise** og **underentreprenører** som de rammer, "
           "opgaven skulle leve i. Det betyder, at jeg kan læse et tilbud og se, hvor entreprenøren har lagt "
           "risikoen hen, og at jeg kan skrive et udbud, der bliver prissat rigtigt i stedet for at give "
           "tillæg senere.", after=80)

    m.para("**Udførelsesfasen er der, hvor rådgivning bliver til virkelighed — eller til tillæg.** Jeg har "
           "stået med **afleveringsforretning**, mangellister, 1- og 5-års gennemgang og den samtale, hvor "
           "leverandøren mener, at alt er leveret, og driften mener noget andet. Min holdning er enkel: "
           "rådgiveren skal blive på banen, til anlægget kører, og de aftalte prøver er dokumenteret.",
           after=80)

    m.para("**Økonomi, tid, kvalitet og risici er én samtale, ikke fire.** I et projekt af 2–10 mio. kr. "
           "hænger de sammen: en forkortet **tidsplan** flytter risiko over i idriftsættelsen, en stram "
           "**økonomi** flytter den over i kvaliteten, og en uafklaret grænseflade flytter den over til "
           "kunden. Jeg arbejder med **tidsstyring**, risikoregister og økonomiopfølgning i samme månedlige "
           "rytme, så ledelsen ser de samme tal som projektet.", after=80)

    m.para("**Struktur i komplekse forløb handler om at gøre det næste skridt tydeligt.** På 37 samtidige "
           "projekter var forskellen mellem en god og en dårlig uge ikke flere møder, men en skriftlig plan "
           "med en navngiven ejer og en dato pr. opgave, og et forum hvor nogen kunne beslutte. Det er også "
           "kernen i min **kommunikation**: kort på skrift til dem, der skal beslutte, detaljeret til dem, "
           "der skal bygge, og tydeligt til de **interessenter**, der skal godkende — på **dansk** og "
           "**engelsk**.", after=80)

    m.para("**Artelia er en rådgivervirksomhed, hvor fagligheden er forudsætningen for tillid.** Over 1.400 "
           "medarbejdere i Danmark, et multidisciplinært miljø og en koncern med mere end 10.000 ansatte i over "
           "40 lande giver netop den bredde, rollen kræver: en **rådgiver**, der kan trække på specialister "
           "og stadig stå med ansvaret over for kunden. Akademi, **frihed under ansvar** og et miljø, hvor "
           "man løfter i flok, er den ramme, jeg gerne vil arbejde i.", after=80)

    m.para("Jeg bor i Måløv og er indstillet på at have min arbejdsplads i **Aarhus**; hvordan "
           "tilstedeværelsen praktisk gribes an, vil jeg gerne aftale i en første samtale. Jeg vil også gerne "
           "høre, hvilke projekter der er på vej i segmentet — hvor mange der er **varmepumper**, "
           "**elkedler** og **lagertanke** mod teknisk byggeri — og hvor tidligt i forløbet rådgiveren "
           "kommer ind.", after=70)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Projektleder og rådgiver med 20+ års erfaring i **energi**, **industri** og teknisk anlæg — "
           "**elautoriseret maskinmester (LV/MV/HV)** med praktisk sans og fuldt P&L-ansvar siden 2023. "
           "Styrede **37 parallelle CAPEX-projekter** af 2–10 mio. kr. og **25 specialister** hos Novo "
           "Nordisk; har skrevet **udbud** og tilbud, forhandlet kontrakter og stået med "
           "**afleveringsforretning** og 1- og 5-års gennemgang. Driftsleder på Lynetten under Biofos, et "
           "forsyningsselskab i 24/7-drift. **Energieffektivisering** med dokumenteret effekt: 40 % lavere "
           "energiomkostninger og over 40 % lavere forbrug. Dansk og engelsk på professionelt niveau.",
           after=80)

    m.section("PROJEKTLEDELSE, UDBUD OG RÅDGIVNING")
    for label, body in [
        ("Projektledelse gennem alle faser",
         "Fra behov og beslutningsgrundlag over projektering og udbud til udførelse, prøvning og "
         "aflevering — 37 CAPEX-projekter, 11 anlægsprojekter og egen virksomheds leverancer."),
        ("Udbud, forhandling og kontrahering",
         "Udbud og tilbud udarbejdet og vurderet, vilkår forhandlet og aftalegrundlag indgået med AB 18, "
         "totalentreprise og underentreprenører som ramme; tillæg undgået ved at beskrive kravet præcist."),
        ("Økonomi, tid, kvalitet og risici",
         "Budget og forecast i SAP ERP, tidsstyring med milepæle og kritisk vej, risikoregister og "
         "månedlig rapportering; nul kritiske afvigelser ved aflevering."),
        ("Projektering og fagdiscipliner",
         "El-teknisk projektering og dimensionering efter DS/HD 60364, koordineret med ventilation, HVAC og "
         "styring; kvalitetssikring før udførelse og dokumentation, der holder ved 1- og 5-års gennemgang."),
        ("Energi og forsyning",
         "24/7-drift på Lynetten med pumper, HVAC, højspænding og SCADA; energieffektivisering med 40 % "
         "lavere energiomkostninger og over 40 % lavere forbrug, målt og dokumenteret."),
        ("Kundekontakt og beslutningsgrundlag",
         "Kundenes betroede modpart i egen virksomhed: behov analyseret, løsninger sammenlignet på pris, "
         "drift og risiko, og anbefalingen givet skriftligt med konsekvenserne for øje."),
    ]:
        m.bullet(label, body, after=25)

    m.section("ERHVERVSERFARING")
    jobs = [
        ("Ejer / teknisk direktør",
         "ELOHVAC ApS · København · maj 2023–nu",
         "Fuldt P&L · tilbud og kontrakter · 5 elektrikere + 3 lærlinge",
         [("Kunderådgivning og kontrakt",
           "Behovsafdækning, løsningsvalg, tilbud og forhandling på el-tekniske opgaver — fra akut fejlfinding "
           "til afleveret anlæg, med dokumentation og opfølgning efter aflevering."),
          ("Økonomi, kvalitet og forbedring",
           "Budget, forecast og dækningsgrad fulgt månedligt; standard work, kvalitetssikring og "
           "Python/Power BI-værktøjer med over 40 % produktivitetsløft.")]),
        ("Senior idriftsættelsesingeniør / projektleder, elsystem",
         "Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024",
         "37 parallelle CAPEX-projekter · 25 specialister · 2–10 mio. kr. · GMP/FDA/EMA",
         [("Projektledelse og beslutningsgrundlag",
           "Fremdrift, økonomi, risiko og snitflader mod teknik, indkøb og drift; beslutningsoplæg til "
           "ledelse og bygherre med konsekvenser, alternativer og anbefaling."),
          ("Prøvning, aflevering og energi",
           "FAT/SAT og IQ/OQ/PQ med nul kritiske afvigelser; PDCA-energiprogram med 40 % lavere "
           "energiomkostninger og dokumenteret effekt.")]),
        ("Projekt- og værkstedsleder",
         "Ventek-Air · København · jan. 2022–nov. 2022",
         "14 medarbejdere · 11 anlægsprojekter · DKK 2–10 mio.",
         [("Udbud, aftalegrundlag og udførelse",
           "Udbud og tilbud på 11 anlægsprojekter, underentreprenører og aftalegrundlag; kapacitetsstyring og "
           "levering fra specifikation til formel aflevering.")]),
        ("Vedligeholdelses- og driftsleder",
         "Lynetten under Biofos · København · aug. 2017–jan. 2022",
         "Forsyningsselskab i 24/7-drift · pumper, HVAC, højspænding, SCADA",
         [("Drift, anlæg og forbedring",
           "Forebyggende vedligehold og akut fejlfinding på kritisk anlæg; 5S, standard work og PDCA på "
           "værksted og lager; energiprogram med over 40 % lavere forbrug.")]),
        ("Elektromekaniker / produktionsteamleder",
         "ARJ Engineering · Teheran · dec. 2003–mar. 2010",
         "12 teknikere · maskinværksted · industrianlæg",
         [("Teknisk gennemførelse",
           "Fejldiagnose, reparation og korrigerende handlinger på industrielle anlæg; planlægning, "
           "materialestyring og målopfølgning for 12 mand.")]),
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
    m.edu("Køleteknik og klimaanlæg (AMU)",
          "Mercantec · 2021")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("Dansk: modersmål, flydende i skrift og tale · **Engelsk: professionelt** i møder, udbud og "
           "dokumentation · Persisk: modersmål · **Bosat i Måløv**, indstillet på arbejdsplads i **Aarhus** · "
           "Kørekort B · Kan tiltræde snarest muligt · Referencer efter aftale.", after=70)

    m.models_table("DE FØRSTE 90 DAGE — FRA KUNDEBEHOV TIL AFLEVERING",
                   ("Periode", "Hvad der sker, og hvordan det måles"), [
        ("Uge 1–2",
         "Lær Artelias projektmodel, skabeloner og kvalitetssystem at kende; mød fagdisciplinerne og de "
         "specialister, der skal leveres sammen med; gennemgå to–tre igangværende projekter fra "
         "beslutningsgrundlag til aflevering for at se, hvor de er stærke, og hvor de taber tid."),
        ("Dag 30",
         "Overtag et selvstændigt projekt med kendt økonomi, tidsplan og risikoregister; aftal med kunden, "
         "hvad der skal besluttes hvornår, og hvordan rapporteringen ser ud — månedlig skriftlig status, "
         "der kan læses af både teknik og ledelse."),
        ("Dag 60",
         "Første udbud eller større beslutningsoplæg gennemført i Artelias format: krav beskrevet, så de kan "
         "prissættes, grænseflader navngivet, og tilbuddene vurderet på pris, risiko og drift; "
         "evalueringsnotat til kunden med en klar anbefaling."),
        ("Dag 90",
         "To til tre projekter drevet i den aftalte rytme med økonomi, tid og risiko under kontrol; "
         "udførelsesfasen fulgt på stedet med prøvnings- og afleveringskrav dokumenteret; og en kort liste "
         "over, hvad der kan standardiseres i min del af rådgivningen.")])

    m.section("ET UDBUD ER EN KONKURRENCE I TYDELIGHED")
    m.para("Når et udbud er uklart, vinder den entreprenør, der har gættet mest optimistisk — og forskellen "
           "kommer tilbage som tillæg, forsinkelse eller en løsning, kunden ikke bad om. Derfor bruger jeg "
           "arbejdet på kravet: hvad skal leveres, hvad er ikke omfattet, hvem ejer grænsefladen, og "
           "hvordan dokumenteres det ved aflevering. Det er den halve projektledelse, og det er den, der "
           "sparer pengene.", after=80)

    m.section("RÅDGIVEREN SKAL KUNNE SIGES IMOD")
    m.para("En rådgiver, der kun siger ja, er en administrator med en titel. Kunden betaler for den vurdering, "
           "der ikke er populær: at den valgte løsning bliver dyr i drift, at tidsplanen er urealistisk, "
           "eller at der mangler en beslutning fra ledelsen, før projektet kan gå videre. Jeg har siddet på "
           "begge sider af den samtale — som den, der skulle levere, og som den, der skulle betale — og det "
           "gør det lettere at sige det klart og tidligt.", after=80)

    m.section("ØKONOMI, TID, KVALITET OG RISIKO ER ÉN SAMTALE")
    m.para("Et projekt styrer ikke fire ting; det styrer én ting, som viser sig som fire tal. Flyttes tid, "
           "flytter risikoen. Skæres der i økonomien, lander forskellen i kvaliteten eller hos en "
           "underentreprenør. Derfor rapporterer jeg dem sammen og med konsekvensen skrevet ud: hvad betyder "
           "denne afvigelse for afleveringen, for driften og for kunden — og hvad foreslår jeg, at vi gør.",
           after=80)

    m.section("I EKSISTERENDE ANLÆG ER UDFØRELSE HALVDELEN AF PROJEKTERINGEN")
    m.para("På et anlæg, der kører, er spørgsmålet ikke kun, hvordan det skal bygges, men hvordan det kan "
           "bygges uden at stoppe driften: hvilke udfald, hvilke midlertidige løsninger, hvornår på døgnet, "
           "og hvem der har fingeren på knappen, hvis noget går galt. Jeg har prøvet det i 24/7-drift og på "
           "en byggeplads i drift, og erfaringen er, at de svar skal være skrevet ned i projekteringen — ikke "
           "aftales på dagen.", after=80)

    m.page_break()

    m.models_table("HVAD STILLINGEN KRÆVER — HVAD JEG HAR LEVERET", ("Krav i opslaget", "Bevis"), [
        ('Lede og styre projekter inden for energi- og industrisegmentet gennem alle projektets faser',
         '37 CAPEX-projekter i industriel produktion og 11 anlægsprojekter fra specifikation til aflevering — beslutningsgrundlag, projektering, udbud, udførelse og aflevering.'),
        ('Være kundens betroede rådgiver og holde fokus på værdi, risiko og kvalitet',
         'Egen virksomhed: kunden er en, man ringer tilbage til — løsning sammenlignet på pris, drift og risiko, og anbefalingen givet skriftligt.'),
        ('Sikre stærke beslutningsgrundlag og rådgive om valg af løsninger',
         'Beslutningsoplæg til ledelse og bygherre med alternativer, konsekvenser og anbefaling; 37 projekter med teknik, økonomi og fremdrift i samme beslutning.'),
        ('Styre projektering i samarbejde med fagdiscipliner og specialister',
         'El-teknisk projektering og dimensionering efter DS/HD 60364 koordineret med ventilation, HVAC og styring; 25 specialister på tværs af fag.'),
        ('Planlægge og gennemføre udbud samt bistå i forhandlinger og kontrahering',
         'Udbud og tilbud udarbejdet og vurderet, vilkår forhandlet, aftalegrundlag indgået med AB 18, totalentreprise og underentreprenører.'),
        ('Følge projekterne i udførelsesfasen og sikre, at intentionerne realiseres',
         'Byggeplads i drift med KS, mangellister, afleveringsforretning og 1- og 5-års gennemgang; FAT/SAT og IQ/OQ/PQ med nul kritiske afvigelser.'),
        ('Have ansvar for økonomi, tid, kvalitet og risici',
         'Budget og forecast i SAP ERP, tidsstyring med milepæle, risikoregister og månedlig rapportering på projekter af 2–10 mio. kr.'),
        ('Opbygge og vedligeholde relationer til kunder og samarbejdspartnere',
         'Kunder, underentreprenører, leverandører, rådgivere og myndigheder i samme sag; relationen holdt ved at svare, også når svaret er nej.'),
        ('Arbejde både strategisk og operationelt og være med, hvor beslutningerne træffes',
         'Beslutningsfora med ledelse og bygherre på 37 projekter og daglig tilstedeværelse på byggeplads og værksted — begge steder, ikke ét af dem.'),
        ('Teknisk baggrund som ingeniør, konstruktør eller lignende',
         'Elautoriseret maskinmester (LV/MV/HV) og B.Tech i teknologiledelse og maskinteknik (7,6/12); elteknik EQF6 og køleteknik/klimaanlæg.'),
        ('Ca. 5–8 års erfaring, gerne fra rådgivningsbranchen, teknisk entreprenørvirksomhed, forsyningsselskab eller projekttung industrivirksomhed',
         '20+ år i teknisk entreprenørvirksomhed (Ventek-Air), forsyningsselskab (Biofos/Lynetten), projekttung industri (Novo Nordisk) og egen virksomhed.'),
        ('Erfaring med projektering, udbud og/eller gennemførelse af anlægs- eller industriprojekter',
         'Anlægsprojekter af 2–10 mio. kr. gennemført fra projektering og udbud til aflevering — i drift, i produktion og på byggeplads.'),
        ('Styr på klassisk projektledelse: økonomi, tid, kvalitet og risici',
         'Økonomiopfølgning, tidsstyring, kvalitetssikring og risikoregister som fast månedlig rytme; nul kritiske afvigelser ved aflevering.'),
        ('God til at skabe struktur og overblik i komplekse forløb',
         '37 samtidige projekter og 11 parallelle anlægsprojekter; skriftlig plan med navngiven ejer og dato pr. opgave og et forum, hvor nogen kan beslutte.'),
        ('Kan kommunikere klart med teknikere, ledelse og samarbejdspartnere',
         'Kort på skrift til dem, der beslutter, detaljeret til dem, der bygger; samme svar til alle parter og svære budskaber givet tidligt.'),
        ('Arbejder på et højt fagligt niveau og har samtidig god praktisk sans',
         'Teoretisk grundlag fra maskinmesteruddannelsen og 20 år med hænderne i anlægget — løsninger vurderet på, om de kan bygges og driftes.'),
        ('Værdsætter variation mellem store og små opgaver',
         'Daglig variation: 37 CAPEX-projekter ved siden af akutte udkald, små serviceopgaver og enkelte store anlægsforløb i egen virksomhed.'),
        ('Evner at analysere kundernes behov og komme med konstruktive løsninger',
         'Behovsafdækning på stedet og løsning beskrevet i kundens drift og økonomi; alternativer sammenlignet, så valget er kundens, men begrundet.'),
        ('Kan arbejde selvstændigt, tager ansvar og trives i samarbejdet med kollegaer i projektteams',
         'Eneansvar for egen virksomhed og projektledelse i teams af 14–25; ansvar taget for egne fejl, og hjælp hentet, før det blev dyrt.'),
        ('Stærke skriftlige og mundtlige kommunikationsevner på dansk og engelsk',
         'Dansk som modersmål og professionelt engelsk i møder, udbud og dokumentation; skriftligt materiale, der kan læses af både teknik og ledelse.'),
        ('Er udadvendt, troværdig, har et godt humør og en positiv indstilling',
         'Kundeforhold bygget på at holde, hvad der blev lovet; godt humør også når tidsplanen skred, og samme tone over for kunde, kollega og leverandør.'),
        ('Erfaring med energianlæg som varmepumper, elkedler og lagertanke samt energieffektivisering',
         'Anlægsteknisk erfaring med HVAC, køleteknik (AMU), pumper og højspænding, og energieffektivisering med 40 % lavere energiomkostninger dokumenteret.'),
    ], widths=(3600, 7046))

    return m.save(path, title="Projektleder, Energi & Industri — Artelia",
                  subject="Rådgivning, udbud og udførelse af energi- og industrianlæg",
                  keywords="projektleder, rådgiver, energi, industri, udbud, forhandling, kontrahering, "
                           "projektering, økonomi, risici, energieffektivisering, aarhus, artelia")


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Artelia_ProjektlederEnergiOgIndustri.docx')))
