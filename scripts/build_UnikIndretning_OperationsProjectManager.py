# -*- coding: utf-8 -*-
"""UnikRecruitment (fortrolig klient) — Operations & Project Manager, København.

Dansk opslag → dansk dokument (da-DK): ansøgning side 1, CV side 2, uddannelse + 90 dage +
tre afsnit side 3, kravmatrix side 4.

STILVALG (master/STILREGISTER.md; godkendt af scripts/style_guard.py, 3/3 skift mod #201):
  register      = INGENIØR-PRÆCIS — definitioner, tolerancer, grænseflader, godkendelser.
                  Produktet er kundetilpasset indretning, hvor finish og detalje er det, kunden
                  betaler for; derfor er præcision ikke en tone, men indholdet. Sidst brugt #192.
  åbningsgreb   = G (SPØRGSMÅLET) — ét skarpt spørgsmål, som rollen skal svare på: hvem ejer
                  snitfladen, når en detalje ikke kan bygges som tegnet. Sidst brugt #193.
  struktur      = SNITFLADERNE — fem grænseflader i projektets vej: salg → projektering ·
                  tegnestue → værksted · værksted → transport og montage · montører → kunde ·
                  systemet → alle. Sidst brugt #195.
  kadence       = korte definitioner, ét krav pr. afsnit, ingen tillægsord om personen.

KULTURSYNKRONISERING (policy 04.11.2026): virksomhedens navn er fortroligt — derfor er dokumentet
skrevet til OPGAVEN og ikke til et logo, og det siges eksplicit. Segmentets egne ord bærer teksten:
  *kundetilpassede indretningsløsninger*, *tegnestue*, *eksterne produktionsværksteder*, *montører*,
  *materialer, finish og udførelse*, *work management- og CRM-system*, *montage i Danmark og udlandet*,
  *intern entrepriseafdeling*. Konkret greb: fem snitflader med fem definitioner af "færdig".
  Bemærk: samme rekrutterer (Michael Kjærgaard) som #202 — dokumentet er bevidst bygget i et helt
  andet register, åbning og struktur, så de to ikke ligner hinanden i samme indbakke.

BRUGERENS OPLYSNINGER (04.11.2026): work management/CRM-erfaring = **Monday** og **MS Project**,
suppleret med egenudviklede AI-værktøjer. Nævnes ved navn — opslaget kalder det en forudsætning.

Ingen opdigtede fakta. Dokumenteret grundlag: fuldt P&L i egen virksomhed siden 2023 (5 elektrikere
+ 3 lærlinge), 11 samtidige entrepriser med 14 mand, 37 CAPEX-projekter med projektgrundlag,
budget/prognose i SAP ERP og KS, FAT/SAT og IQ/OQ/PQ med nul kritiske fund, IKT og
afleveringspakker, APV/LOTO på skiftende pladser, kompetencematrix og oplæring af lærlinge.

Policy: master/README.md — jobbet først, kandidaten kun som bevis, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Operations & Project Manager · Indretning, montage og finish'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4. november 2026")
    m.meta("Operations & Project Manager · København · rekruttering via UnikRecruitment (fortrolig klient)")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: operations & project manager", bold=True, color='1A1A1A')
    m.para("Til Michael Kjærgaard, UnikRecruitment", after=70)

    # ---------------------------------------------------------------- side 1
    m.para("**Hvem ejer snitfladen, når en detalje ikke kan bygges, som den er tegnet?** I en "
           "standardløsning koster spørgsmålet ingenting. I en **kundetilpasset** gør det: "
           "materialet er valgt, **finishen** er aftalt, og målet skal passe i et rum, nogen har "
           "opmålt. Svaret afgør, om projektet holder tid, pris og **kvalitet** — og det er den "
           "rolle, jeg søger: ikke at tegne og ikke at montere, men at sørge for, at svaret er "
           "givet, før nogen tager stilling til det på pladsen.", after=80)

    m.para("Opslaget oplyser ikke, hvad virksomheden hedder, og det respekterer jeg. Derfor skriver "
           "jeg til opgaven og ikke til et navn: **projekter** fra afsluttet salg gennem "
           "**projektering** og produktion til færdig **montage** — **kundetilpassede "
           "indretningsløsninger**, hvor **detaljer** og udførelse er det, kunden betaler for, "
           "i Danmark og udlandet. Nedenfor er de fem **snitflader**, "
           "jeg ville tage fat på først, og hvad jeg lægger i ordet færdig på hver af dem.",
           after=80)

    m.para("**1 · Salg → projektering.** Den dyreste ændring er den, der bliver opdaget, efter "
           "materialet er bestilt. Derfor skal mål, materialer, **finish** og **tolerancer** stå i et "
           "projekteringsgrundlag, som kunden har set og godkendt, før et **værksted** får en "
           "tegning. På 37 projekter skrev jeg projektgrundlag og afgrænsning ned, før opgaven gik i "
           "gang; samme disciplin, dyrere materialer.", after=80)

    m.para("**2 · Tegnestue → værksted.** En tegning, der er halvfems procent færdig, bliver hundrede "
           "procent dyr i produktionen. Hver tegning skal have en revision, en dato og et navn: hvem "
           "har godkendt den, hvad er ændret, og hvad må værkstedet ikke bygge videre på. Jeg har "
           "arbejdet med **tegningsmateriale** i IKT-processer og med **kvalitetskontrol**, hvor "
           "protokollen blev skrevet, før testen blev lavet.", after=80)

    m.para("**3 · Værksted → transport og montage.** En forkert leverance på en adresse i udlandet "
           "koster ikke en fragt — den koster en **montage**uge og en kunde, der har ventet. Derfor "
           "en kontrolport før afsendelse: mål, finish, pakkeliste og montagerækkefølge godkendt, og "
           "**transport** og folk booket efter pladsens faktiske fremdrift, ikke efter den planlagte — "
           "og en **leverandørstyring**, hvor **værksted** og fragtmand har en aftalt dato, ikke "
           "en forventning.",
           after=80)

    m.para("**4 · Montører → kunde.** Erfarne **montører** lader sig ikke styre af nogen, der ikke ved, "
           "hvad arbejdet kræver. Mandatet kommer fra fagligheden: hvem der har sidste hånd på en "
           "detalje, hvad der er aftalt med kunden, og hvornår en opgave er færdig. Jeg har ledet fem "
           "elektrikere og tre lærlinge og et **team** på 14 i entreprise — med daglige tavlemøder, "
           "MUS og tydelige aftaler, ikke med mails.", after=80)

    m.para("**5 · Systemet → alle.** Står status to steder, står den ingen steder. **Monday** og **MS "
           "Project** er de systemer, jeg har brugt til at holde **deadlines**, **afhængigheder** og "
           "ansvar synlige, og jeg bygger selv **AI-værktøjer**, når standardsystemet ikke kan svare "
           "på det, en byggesag faktisk kræver. Det er ikke et tillæg til rollen; det er den måde, "
           "**projektledelse** bliver rigtigt på.", after=80)

    m.para("**Den interne entrepriseafdeling.** I beskriver den som en mulighed på sigt. For mig er den "
           "ikke teoretisk: jeg driver i dag en virksomhed, der tager **projektering**, **montage** og "
           "aflevering på sig med eget budget og egen risiko. Det er præcis den rolle, I peger på som "
           "næste skridt — og derfor er den første opgave også den vigtigste for mig: at få den "
           "daglige planlægning til at holde.", after=80)

    m.para("Jeg bor i Måløv, har omkring 20 minutter til København og rejser gerne med projekterne. Jeg "
           "kan tiltræde snarest, og CV og ansøgning er sendt via UnikRecruitments hjemmeside, som I "
           "beder om.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Projekt- og produktionsleder med håndværket i bund: elektriker, **elautoriseret "
           "maskinmester** (LV/MV/HV), el- og maskinteknisk design (EQF 6) og B.Tech i "
           "teknologiledelse og maskinteknik. 20+ år med projekter fra grundlag og projektering til "
           "montage og aflevering — 11 samtidige entrepriser med 14 mand, 37 CAPEX-projekter med "
           "budget og prognose, **Monday** og **MS Project** som styringsværktøj og egne "
           "**AI-værktøjer** til planlægning og opfølgning.", after=80)

    m.section("PROJEKTERING, TOLERANCER OG GODKENDELSE")
    for label, body in [
        ("Tegnings- og målgrundlag",
         "Mål, materialer og specifikationer afklaret og skrevet ned, før arbejdet blev sat i gang; "
         "revision, dato og godkendelse på alt, der gik videre til udførelse."),
        ("Tolerancer og finish",
         "**Kvalitetskontrol** med egenkontrol pr. fag og målbare kriterier, ikke skøn; afvigelser "
         "registreret med rodårsag, så den samme fejl ikke kom igen på næste sag."),
        ("Godkendelse før afsendelse",
         "Kontrol og godkendelse som port før leverance: protokol skrevet før testen, dokumentation "
         "og pakkeliste kontrolleret — nul kritiske fund ved aflevering i GMP-reguleret byggeri."),
    ]:
        m.bullet(label, body)

    m.section("MONTAGE, TRANSPORT OG FREMDRIFT")
    for label, body in [
        ("Montageplan og rækkefølge",
         "Montagen planlagt i rækkefølge efter, hvad der skal være færdigt først; mandskab og "
         "leverancer tilpasset pladsens faktiske **fremdrift** ugentligt."),
        ("Leverancekontrol",
         "**Leverancer** kontrolleret mod mål og specifikation ved modtagelse og før afsendelse; "
         "mangler lukket, før de blev til ventetid på pladsen."),
        ("Flere sager på én gang",
         "11 samtidige **projekter** med daglige tavlemøder og flaskehalsanalyser; resurser flyttet, "
         "før en sag gik i stå — og kunden orienteret samme dag."),
    ]:
        m.bullet(label, body)

    m.section("LEDELSE, SYSTEM OG ØKONOMI")
    for label, body in [
        ("Håndværkere og montører",
         "5 elektrikere og 3 lærlinge samt 14-mands entrepriseteam: ansættelser, oplæring, MUS og "
         "situationsbestemt ledelse (SLII) på skiftende **byggepladser**."),
        ("Systemer som styring",
         "**Monday** og **MS Project** til **tidsplan**, **deadlines**, **afhængigheder** og ansvar; "
         "SAP ERP til budget og prognose, Power BI til opfølgning."),
        ("Egne AI-værktøjer",
         "**AI-værktøjer** bygget med Python og Claude til tilbudsberegning, tidsplaner, "
         "**kvalitetskontrol**-tjeklister og KPI-dashboards — 40 % mindre administration."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Ejer / teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · fuldt P&L · projektering, montage og aflevering")
    m.bullet("Projekt og forretning i egen hånd",
              "Sager fra tilbud til aflevering med eget budget og egen risiko; underentreprenører, "
              "materialestyring og KS — og ansvaret for at sige nej, når kalkulen ikke holdt.")

    m.job("Senior idriftsættelsesingeniør / projektleder, elsystem",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024",
          scope="37 samtidige CAPEX-projekter · 25 specialister · GMP/FDA/EMA")
    m.bullet("Godkendelse, dokumentation og aflevering",
              "FAT/SAT og IQ/OQ/PQ med protokol skrevet før testen; afleveringspakker og "
              "dokumentation kontrolleret — nul kritiske fund.")

    m.job("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · DKK 2–10 mio.")
    m.bullet("Montage og fremdrift",
              "Daglige tavlemøder og flaskehalsanalyser; mandskab og leverandører flyttet mellem "
              "sager, når en entreprise trak mere end planlagt.")

    m.job("Vedligeholdelses- og driftsleder", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="Anlæg i 24/7-drift · pumper, HVAC, højspændingstavler, SCADA")
    m.bullet("Drift og sikkerhed på pladsen",
              "Forebyggende vedligehold og akut fejlfinding; LOTO, APV og sikkerhedsrunderinger, "
              "5S og standard work på værksted og lager.")

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
    m.edu("Køleteknik & klimaanlæg (AMU) · Lean: 5S, PDCA, VSM, A3",
          "Mercantec · 2021 · STCW sikkerhedskurser (2021–2023)")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("**Dansk:** modersmål · **Engelsk:** professionelt, skriftligt og mundtligt · **Persisk:** "
           "modersmål · **Bosat i Måløv**, ca. 20 minutter til København · **Rejser gerne** · "
           "**Kan tiltræde snarest** · Referencer efter aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA GENNEMGANG TIL FØRSTE PROJEKT UDEN OVERRASKELSER",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–2",
             "Gennemgå de sager, der er i gang, i **Monday** og **MS Project**: hvor står "
             "**deadlines**, hvilke **afhængigheder** holder ikke, og hvad venter **montørerne** på "
             "lige nu?"),
            ("Dag 30",
             "Én status pr. **projekt** med navn, dato og næste handling; kontrolport før afsendelse "
             "aftalt med **tegnestue** og **værksteder**, og **leverancer** prioriteret efter "
             "pladsernes fremdrift."),
            ("Dag 60",
             "Fælles tegngrundlag: revision, godkendelse og ændringslog på alt, der går i produktion; "
             "**kvalitetskontrol** med målbare kriterier for **finish** og **tolerancer**."),
            ("Dag 90",
             "Første **projekt** afleveret uden overraskelser — målt på tid, omkostninger og "
             "reklamationer — og en kort evaluering, der går videre til næste sag."),
        ],
        widths=(1500, 8830))

    m.section("EN TEGNING ER ET LØFTE TIL VÆRKSTEDET")
    m.para("Når en tegning går i produktion, er den ikke et forslag. Værkstedet bygger det, der står — "
           "også når målet er forkert, eller når en detalje ikke kan samles med det materiale, der er "
           "valgt. Derfor skal godkendelsen ligge før produktion og ikke efter: en revision, en dato, "
           "et navn, og en linje om, hvad der er ændret. Det koster en halv time at skrive; det koster "
           "et møbel og en montagedag at lade være.", after=70)

    m.section("KVALITET ER ET MÅL, IKKE EN HOLDNING")
    m.para("Finish bliver først et krav, når nogen har defineret, hvad der er godt nok: en **tolerance** "
           "i millimeter, en samling der skal være synlig eller skjult, og en overflade der ikke må "
           "repareres på pladsen. Jeg har arbejdet med egenkontrol og protokoller, hvor kriteriet stod "
           "skrevet, før arbejdet begyndte — og hvor en afvigelse blev registreret, ikke forklaret. "
           "Det er den samme øvelse her, bare med dyrere materialer.", after=70)

    m.section("DET, DER IKKE STÅR I SYSTEMET, SKER IKKE")
    m.para("Et **work management**-system er kun et overblik, hvis det er stedet, hvor sandheden står "
           "— ikke et sted, man opdaterer før mødet. Jeg har brugt **Monday** og **MS Project** til at "
           "holde **kapacitet**, **bemanding** og **afhængigheder** synlige, og bygget egne "
           "**AI-værktøjer**, når svaret skulle hentes på tværs af systemer. Reglen er enkel: én "
           "opgave, én ejer, én dato — og opdateret samme dag, den ændrede sig.", after=0)

    m.section("MONTØRERNE SER FEJLENE FØRST")
    m.para("Den, der står med en samling på pladsen, opdager, hvad tegningen ikke kunne vise. Hvis den "
           "viden bliver på pladsen, betaler næste projekt for den samme fejl. Derfor skal hver sag "
           "slutte med en kort evaluering — hvad gik galt, hvad blev løst godt, og hvad ændrer vi i "
           "grundlaget næste gang — og en løsning, der er værd at genbruge, skal skrives ned, så andre "
           "kan finde den. Jeg har gjort det med skabeloner og videndeling i **teamet**; det er ikke et "
           "møde mere, det er den billigste kvalitetsforbedring, der findes.", after=60)

    m.section("HVOR JEG VILLE STARTE")
    m.para("I systemet, ikke i mødelokalet. Første uge vil jeg åbne **Monday** og **MS Project** og se, "
           "hvor mange sager der har en status, der er ældre end syv dage — det er der, overblikket "
           "faktisk knækker. Derefter tage de tre sager med næste **montage** og gennemgå dem fra "
           "tegning til pakkeliste, så jeg ved, hvor **tolerancerne** og **leverancerne** typisk "
           "glipper. Så kan jeg tale med **montørerne** om det, jeg har set — og ikke om det, jeg "
           "tror.", after=0)


    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "HVAD STILLINGEN KRÆVER — HVAD JEG HAR LEVERET",
        ["Krav i opslaget", "Bevis"],
        [
            ("Håndværksmæssig baggrund og erfaring med at styre projekter og lede håndværkere",
             "Elektriker og **elautoriseret maskinmester**; 20+ år med projekter, 11 entrepriser "
             "med 14 mand og fuldt P&L."),
            ("Planlægge og koordinere flere samtidige projekter, kapacitet på tegnestue, værksteder og montage",
             "11 samtidige entrepriser og 37 CAPEX-projekter med fælles ressource- og "
             "**kapacitet**splan."),
            ("Lede montørerne i hverdagen, planlægge opgaver og inddrage eksterne håndværkere",
             "5 elektrikere og 3 lærlinge samt 14-mands **team**: daglige tavlemøder, MUS og "
             "opgaver med navn og dato."),
            ("Sikre at tegninger, mål og specifikationer er afklaret og afleveret til værkstederne i rette tid",
             "**Tegningsmateriale**, mål og **specifikationer** afklaret før udførelse, med revision "
             "og godkendelse på alt."),
            ("Styre projekter og underleverandører i work management- og CRM-system",
             "**Monday** og **MS Project** med status, **deadlines** og **afhængigheder**; SAP ERP, "
             "Power BI og egne **AI-værktøjer**."),
            ("Følge op på kvalitet og leverancer og reagere tidligt på fejl, flaskehalse og forsinkelser",
             "Daglige flaskehalsanalyser og ugentlig opfølgning; **leverancer** kontrolleret mod mål, "
             "før de gik videre."),
            ("Tilpasse bemanding og leverancer til byggepladsernes faktiske fremdrift",
             "**Bemanding** flyttet efter pladsens fremdrift ugentligt; ventetid fjernet, før den "
             "blev til en ekstra montagedag."),
            ("Holde kunder og samarbejdspartnere orienteret og følge op på ressourceforbrug og omkostninger",
             "Fast status til bygherre og kunde; **ressourceforbrug** og **omkostninger** fulgt pr. "
             "sag med afvigelser forklaret."),
            ("Sikre at tegninger, mål og leverancer er kontrolleret og godkendt, inden produkterne sendes til kunden",
             "Kontrolport før afsendelse: protokol skrevet før test, pakkeliste og dokumentation "
             "kontrolleret — nul kritiske fund."),
            ("Koordinere transport og montage i Danmark og udlandet",
             "**Transport** og **montage** koordineret på skiftende pladser i Danmark; internationale "
             "projektforløb i GMP-regi og syv år i udlandet — rejser gerne."),
            ("Følge op med montørerne og sikre at erfaringer og gode løsninger bliver delt i teamet",
             "Kort evaluering efter hver sag og fælles skabeloner; erfaringer delt i **teamet**, så "
             "næste sag startede bedre."),
            ("Forstå arbejdet på byggepladsen og bruge fagligheden til at finde løsninger og træffe beslutninger",
             "Håndværket i bund fra ti år på værksted og plads; beslutninger taget på pladsen med "
             "fagligheden som grundlag."),
            ("Ledet erfarne håndværkere og skabt respekt gennem faglighed, ordentlighed og tydelige aftaler",
             "Erfarne håndværkere og formænd ledet i 20 år; aftaler skrevet ned og holdt — også når "
             "det kostede."),
            ("Bevarer roen når noget går galt og tager fat i problemet sammen med dem der skal løse det",
             "Nedbrud og omprioritering i døgndrift; problemet taget på pladsen med dem, der skulle "
             "løse det, samme dag."),
            ("Kan læse og vurdere tegningsmateriale og har blik for detaljer, finish og kvalitet",
             "El- og maskintegninger, IKT og **kvalitetskontrol**; **finish** og **tolerancer** "
             "vurderet mod skrevet kriterium, ikke mod smag."),
            ("Erfaring med og interesse for work management- og CRM-systemer, brugt aktivt",
             "**Monday** og **MS Project** brugt dagligt til planlægning og opfølgning; kunder, tilbud "
             "og status ført i egne systemer i virksomheden."),
            ("Interesse for og erfaring med AI-værktøjer og AI-agenter",
             "Egne **AI-agenter** og **AI-værktøjer** bygget med Python og Claude til tilbud, "
             "tidsplaner, tjeklister og dashboards — 40 % mindre administration."),
            ("Forstår sammenhængen mellem god forberedelse, effektiv montage og projekternes økonomi",
             "Fuldt P&L og egne kalkuler: hver time i forberedelse er hentet igen i **montage** og i "
             "færre fejl på pladsen."),
            ("Kommunikerer klart med håndværkere, kunder og kolleger og har mod på internationale projekter",
             "Kunder, håndværkere og kolleger i 20 år i tre sprog; internationale forløb og "
             "**montage i udlandet** som en opgave, jeg tager."),
        ],
        widths=(3600, 6746))

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_UnikIndretning_OperationsProjectManager.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_UnikIndretning_OperationsProjectManager.docx'))
