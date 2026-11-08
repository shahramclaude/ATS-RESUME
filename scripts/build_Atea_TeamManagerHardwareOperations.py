# -*- coding: utf-8 -*-
"""Atea Danmark — Team Manager til Hardware Operations (Ballerup).

Dansk opslag → dansk dokument: ansøgning p1, CV p2, uddannelse + 90 dage +
fire sektioner p3, kravmatrix p4.
Vinkel: stabil drift er ikke det modsatte af udvikling — den er forudsætningen,
og den skabes af fjorten mennesker, der ved hvad der er vigtigst i dag.
Policy: master/README.md — jobbet først, kandidaten kun som bevis, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Team Manager, Hardware Operations · Drift, personaleledelse og forbedringer'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Danmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("7. november 2026")
    m.meta("Atea Danmark · Hardware Operations · Ballerup")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Team Manager, Hardware Operations", bold=True, color='1A1A1A')
    m.para("Til Director Sanne Meinertz og lederteamet i Atea", after=70)

    # ---------------------------------------------------------------- side 1
    m.para("Fjorten mennesker i drift har ikke brug for en plan, der holder hele året. De har brug for at "
           "vide, hvad der er vigtigst i dag — og for en leder, der tager beslutningen, når prioriteringerne "
           "ændrer sig klokken ti om formiddagen. Det er den slags ledelse, jeg har udøvet i tyve år, og det "
           "er den, jeg søger her: tæt på driften, med et tydeligt ansvar for mennesker og for den kvalitet, "
           "kunderne møder.", after=80)

    m.para("**Stabil drift er ikke det modsatte af udvikling. Det er forudsætningen for den.** I **Hardware "
           "Operations** betyder det, at hardware skal ind, klargøres, kontrolleres og ud igen med den "
           "kvalitet og den **responstid**, der er lovet — og at forbedringer skal bygges oven på en drift, "
           "der allerede står fast. Jeg har prøvet begge dele på samme tid: som driftsleder på et kritisk "
           "anlæg i 24/7-drift, hvor **stabil drift** var kravet, og hvor vi indførte 5S, standard work og "
           "PDCA uden at stoppe produktionen.", after=80)

    m.para("**Jeg har ledet præcis den størrelse team, stillingen handler om.** Som projekt- og værkstedsleder "
           "havde jeg **14 medarbejdere** og 11 samtidige leverancer, med daglige **tavlemøder**, "
           "flaskehalsanalyse og standardiserede arbejdsgange. I dag driver jeg egen virksomhed med **fuldt "
           "P&L-ansvar** og fem elektrikere plus tre **lærlinge** — med **rekruttering**, oplæring, "
           "**kompetencematrix**, **MUS** og 1:1, og med **SLA** og **responstid** som de tal, kunderne "
           "faktisk holder os op på. Før det stod jeg i spidsen for et værksted med 12 teknikere og for 25 "
           "specialister på 37 samtidige projekter.", after=80)

    m.para("**Prioritering er en beslutning, ikke en liste.** Når behov og prioriteringer flytter sig, skal "
           "nogen vælge, hvad der går først, og fortælle hvorfor. Min erfaring er, at det kun virker, når "
           "teamet kan se de samme tal: hvor mange sager er i kø, hvad er gennemløbstiden, hvad haster "
           "egentlig, og hvad er konsekvensen for kunden. **Struktur og transparens** er ikke et "
           "styringsdokument — det er en halv side på tavlen, der er opdateret, og et møde om morgenen, hvor "
           "nogen siger højt, hvad der er vigtigst i dag og hvorfor.", after=80)

    m.para("**Forbedringer skal kunne mærkes af kunden, ellers er de administration.** Jeg har drevet "
           "forbedringer med **Lean**-værktøjer — 5S, standard work, **A3** og PDCA — og med "
           "**automatisering** af det, der ellers bliver gjort i hånden: rapportering, tjeklister, tilbud og "
           "opfølgning. I egen virksomhed gav det **over 40 % produktivitetsløft**; på Lynetten gav "
           "energiarbejdet **over 40 % lavere forbrug**. Effekten skal måles før og efter, og helst af dem, "
           "der udfører arbejdet.", after=80)

    m.para("**AI og digitale værktøjer er noget, jeg bruger — ikke noget, jeg har læst om.** Jeg bygger selv "
           "løsninger med **Claude**, **Python** og **Power BI**: en tjekliste, der bliver genereret, en "
           "rapport, der skriver sig selv, et dashboard, der henter tallene i stedet for at nogen taster dem "
           "ind. Den slags bliver kun værdi, hvis teamet tager det i brug, så jeg starter altid med at "
           "automatisere det, der irriterer flest — og med at lære det videre i stedet for at beholde det "
           "selv.", after=80)

    m.para("**Kundeoplevelsen ligger i det, der sker, når noget ikke virker.** En vare, der er forsinket, en "
           "sag der går i stå, eller en enhed der kommer retur — det er der, **kundetilfredshed** bliver afgjort. Jeg har "
           "arbejdet med serviceaftaler, hvor **responstid** og kvalitet var de målte KPI'er, og med nul "
           "kritiske afvigelser i de aftaler, jeg selv stod for. Det kræver, at nogen tager ansvar for "
           "opfølgningen og ikke kun for den gode historie.", after=80)

    m.para("**Relationer er arbejdsredskabet, ikke en sidegevinst.** Interne **interessenter** som salg, "
           "teknik, lager og support, og eksterne som kunder, leverandører og partnere — de skal alle sammen "
           "have et svar, der passer med det, de andre har fået. Jeg har stået i den position som enejer: "
           "tekniske chefer, indkøbere, leverandører og rådgivere på samme sag, hvor nogen skulle have det "
           "første og ærlige svar.", after=80)

    m.para("**Atea er en arbejdsplads, hvor ledelse ikke er noget, man gør alene.** Et team på 14, et "
           "lederteam omkring sig og en organisation på over 1.400 mennesker, der bygger Danmark med "
           "**it-infrastruktur** — det er en ramme, hvor jeg kan bidrage med **driftsledelse**, "
           "**personaleledelse** og konkrete forbedringer, og samtidig blive udfordret af kolleger, der har "
           "prøvet ting, jeg ikke har. ISO 37001 og en notering på **Oslo Børs** fortæller også, at "
           "professionelle processer er en forudsætning, ikke en begrænsning.", after=80)

    m.para("Jeg bor i Måløv, ti minutter fra **Ballerup**, og kan tiltræde inden 1. februar 2027. Jeg vil "
           "gerne høre, hvordan Hardware Operations er sammensat i dag — hvor mange opgavetyper teamet "
           "dækker, hvordan kvalitet og gennemløbstid måles, og hvor I ser det største potentiale for "
           "forbedringer i det kommende år.", after=70)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Drifts- og personaleleder med 20+ års erfaring i tekniske driftsmiljøer — team fra 5 til 25 "
           "medarbejdere, **fuldt P&L-ansvar** siden 2023. Ledte **14 medarbejdere** og 11 samtidige "
           "leverancer med daglige **tavlemøder** og standardiserede arbejdsgange; driver i dag egen "
           "virksomhed med **rekruttering**, oplæring, **kompetencematrix**, **SLA**-opfølgning og **synlig "
           "ledelse** på gulvet. Arbejder "
           "med **Lean**, 5S, **A3** og PDCA og med **AI**-værktøjer (**Claude**, **Python**, "
           "**Power BI**), der har givet **over 40 % produktivitetsløft**. Elautoriseret maskinmester "
           "(LV/MV/HV), bosat i Måløv — ti minutter fra **Ballerup**.", after=80)

    m.section("PERSONALEDELESE, DRIFT OG FORBEDRING")
    for label, body in [
        ("Personaleledelse tæt på driften",
         "5 til 25 medarbejdere: daglig planlægning, MUS og 1:1, oplæring af lærlinge, sygefraværs- og "
         "trivselssamtaler, og beslutninger taget på gulvet frem for i et mødelokale."),
        ("Stabil drift og kvalitet",
         "24/7-drift med oppetid som krav; serviceaftaler med responstid og kvalitet som KPI'er, nul kritiske "
         "afvigelser og leveringssikkerhed som fast punkt. Kvalitet måles på, hvad kunden oplever."),
        ("Prioritering og kapacitet",
         "Én kapacitetspulje mod 11 og 37 samtidige leverancer: ugentlig prioritering, daglig opfølgning på "
         "tavlen og tydelig besked om, hvad der går først, og hvad der må vente."),
        ("Forbedringer med målbar effekt",
         "5S, standard work, A3 og PDCA i drift og værksted; forbedringerne ejet af teamet, effekten målt før "
         "og efter — over 40 % lavere energiforbrug og over 40 % produktivitetsløft."),
        ("AI og digitale værktøjer i praksis",
         "Python, Claude og Power BI i daglig brug til rapportering, tjeklister, tilbud og dashboards; "
         "løsninger bygget, dokumenteret og lært videre til kolleger og lærlinge."),
        ("Relationer og samarbejde",
         "Interne og eksterne interessenter i samme sag: kunder, leverandører, underentreprenører, "
         "myndigheder og rådgivere; svaret er det samme, uanset hvem der spørger."),
    ]:
        m.bullet(label, body, after=25)

    m.section("ERHVERVSERFARING")
    jobs = [
        ("Ejer / teknisk direktør",
         "ELOHVAC ApS · København · maj 2023–nu",
         "5 elektrikere + 3 lærlinge · fuldt P&L · SLA og responstid",
         [("Ledelse, drift og kundeoplevelse",
           "Rekruttering, oplæring og daglig ledelse af 5 elektrikere og 3 lærlinge; serviceaftaler med "
           "responstid og kvalitet som KPI'er, nul kritiske afvigelser, og ordrebog styret mod faste datoer."),
          ("Forbedringer og AI-værktøjer",
           "Standard work og Python/Claude-værktøjer til tilbud, tjeklister og rapportering med over 40 % "
           "produktivitetsløft; dokumentation og dashboards, som teamet selv kan bruge og vedligeholde.")]),
        ("Senior idriftsættelsesingeniør / projektleder, elsystem",
         "Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024",
         "37 parallelle CAPEX-projekter · 25 specialister · GMP/FDA/EMA",
         [("Koordination, kvalitet og leverance",
           "25 specialister og 37 samtidige projekter med fremdrift, økonomi og snitflader mod teknik, indkøb "
           "og drift; nul kritiske afvigelser ved aflevering og månedlig rapportering til ledelsen."),
          ("Forbedring og målbar effekt",
           "PDCA-program med 40 % lavere energiomkostninger; forbedringer identificeret i driften og drevet "
           "sammen med dem, der skulle leve med dem.")]),
        ("Projekt- og værkstedsleder",
         "Ventek-Air · København · jan. 2022–nov. 2022",
         "14 medarbejdere · 11 samtidige leverancer · DKK 2–10 mio.",
         [("14 medarbejdere og daglig drift",
           "Daglig ledelse af 14-mands team og værksted: kapacitet, prioritering og fremdrift, flaskehalse "
           "fundet på morgenmødet og standardiserede arbejdsgange med markant løft i leveringsevne.")]),
        ("Vedligeholdelses- og driftsleder",
         "Lynetten under Biofos · København · aug. 2017–jan. 2022",
         "Kritisk anlæg i 24/7-drift · tavler, pumper, HVAC · SRO/SCADA",
         [("Stabil drift og løbende forbedring",
           "Forebyggende vedligehold og akut fejlfinding med oppetid som krav; 5S, standard work og PDCA på "
           "værksted og lager med over 40 % lavere energiforbrug; arbejdsmiljø med LOTO, APV og nærved-hændelser.")]),
        ("Elektromekaniker / produktionsteamleder",
         "ARJ Engineering · Teheran · dec. 2003–mar. 2010",
         "12 mekanikere og teknikere · maskinværksted",
         [("Team, mål og opfølgning",
           "Daglig ledelse af 12 teknikere: vagtplanlægning, materialestyring, målopfølgning og korrigerende "
           "handlinger ved afvigelser.")]),
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
           "modersmål · **Bosat i Måløv**, ti minutter fra Ballerup · Kørekort B · Kan tiltræde inden "
           "1. februar 2027 · Referencer efter aftale.", after=70)

    m.models_table("DE FØRSTE 90 DAGE — RETNING, DRIFT OG FORBEDRINGER",
                   ("Periode", "Hvad der sker, og hvordan det måles"), [
        ("Uge 1–2",
         "Sid med ved opgaverne og lær flowet: hvad kommer ind, hvad går ud, hvor venter sagerne, og hvor "
         "opstår fejlene; mød de vigtigste interessenter i salg, teknik og lager og få deres billede af, hvor "
         "Hardware Operations gør en forskel, og hvor den ikke gør."),
        ("Dag 30",
         "Én side på tavlen med de vigtigste tal — sager i kø, gennemløbstid, kvalitet og responstid — og et "
         "fast morgenmøde, hvor dagens prioritet bliver sagt højt; MUS- og 1:1-samtaler planlagt med alle "
         "14, og de to eller tre største tidstyve identificeret med en ejer."),
        ("Dag 60",
         "To forbedringer gennemført med baseline og effekt — typisk indgang, klargøring eller overlevering "
         "mellem stationer; transparens på plads, så teamet selv kan se, hvad der er vigtigst, og så "
         "lederteamet kan se det samme."),
        ("Dag 90",
         "Stabil drift målt over fire uger med kendt kvalitet og gennemløbstid; første AI- eller "
         "automatiseringsløsning i brug i den daglige rutine; og en plan for det næste halve år med "
         "kompetenceudvikling, der matcher de opgaver, der faktisk kommer.")])

    m.section("STABIL DRIFT ER IKKE DET MODSATTE AF UDVIKLING")
    m.para("En drift, der kører, er ikke en drift, der står stille — den er den platform, forbedringerne skal "
           "stå på. Derfor bliver rækkefølgen vigtig: først vished om, hvad der er vigtigst i dag, så tal "
           "der kan ses af alle, og først derefter et forbedringsprojekt. Forbedringer, der bliver startet "
           "oven på en uklar drift, ender som endnu et initiativ, teamet skal forholde sig til.", after=80)

    m.section("PRIORITERING ER EN BESLUTNING, IKKE EN LISTE")
    m.para("Når der er mere arbejde, end der er timer, er der kun to ærlige muligheder: flytte en leverance "
           "eller skaffe hænder. Alt andet er ønsketænkning, som teamet betaler for i weekenden. Jeg har "
           "prøvet det med 37 projekter og én pulje af specialister, og det, der gjorde forskellen, var ikke "
           "et bedre regneark — det var en fast rytme, hvor nogen med mandat sagde, hvad der gik først, og "
           "hvorfor, så alle kunne indrette sig efter det samme svar.", after=80)

    m.section("AI BLIVER FØRST EN FORDEL, NÅR TEAMET BRUGER DEN")
    m.para("Jeg bruger **Claude**, **Python** og **Power BI** hver dag, og det, der giver mest, er ikke de "
           "store løsninger: det er de små, gentagne opgaver, hvor nogen taster det samme ind hver uge. "
           "Fremgangsmåden er enkel — find den opgave, der irriterer flest, løs den sammen med den person, "
           "der har den, mål tiden før og efter, og lær den videre. AI, der bliver en personlig "
           "produktivitetshemmelighed, forsvinder, når personen gør.", after=80)

    m.section("KUNDEOPLEVELSEN LIGGER I DET, DER SKER, NÅR NOGET IKKE VIRKER")
    m.para("En ordre, der går som den skal, mærker kunden ikke. Det gør den forsinkede leverance, den "
           "manglende besked og den enhed, der kommer retur. Derfor er opfølgning og ærlig kommunikation "
           "undervejs en del af driften og ikke en serviceafdeling, der kommer bagefter — og derfor skal "
           "teamet have et mandat til at sige »det her når vi ikke i dag, og her er hvad vi gør i stedet«, "
           "før kunden selv finder ud af det.", after=80)

    m.page_break()

    m.models_table("HVAD STILLINGEN KRÆVER — HVAD JEG HAR LEVERET", ("Krav i opslaget", "Bevis"), [
        ('Lede, udvikle og sparre med 14 medarbejdere og skabe tydelig retning for teamet',
         'Ledte 14 medarbejdere og 11 samtidige leverancer i Ventek-Air; i dag 5 elektrikere og 3 lærlinge med fuldt P&L — samme størrelse, samme ansvar.'),
        ('Sikre høj kvalitet og stabil drift med fokus på gode kundeoplevelser',
         '24/7-drift med oppetid som krav; serviceaftaler med responstid og kvalitet som KPI\'er og nul kritiske afvigelser i de aftaler, jeg selv stod for.'),
        ('Prioritere opgaver og ressourcer, når behov og prioriteringer ændrer sig',
         'Én kapacitetspulje mod 11 og 37 samtidige leverancer; ugentlig re-prioritering og beslutningen om, hvad der venter, taget eksplicit.'),
        ('Identificere og drive forbedringer, der skaber værdi på tværs af organisationen',
         '5S, standard work, A3 og PDCA i fire organisationer; 40 % lavere energiomkostninger og over 40 % produktivitetsløft, målt før og efter.'),
        ('Skabe struktur og transparens, så teamet ved, hvad der er vigtigst, og hvorfor',
         'En halv side på tavlen med de få tal, der styrer dagens arbejde, og et morgenmøde, hvor prioriteten bliver sagt højt.'),
        ('Bygge stærke relationer og sikre et godt samarbejde med interne og eksterne interessenter',
         'Kunder, leverandører, underentreprenører, rådgivere og myndigheder på samme sag; svaret er det samme, uanset hvem der spørger.'),
        ('Erfaring med personaleledelse eller et stærkt fundament for at tage næste skridt ind i en lederrolle',
         'Personaleledelse gennem 20 år på fire niveauer — 5, 12, 14 og 25 medarbejdere — med MUS, 1:1, oplæring og lærlingeansvar.'),
        ('Kan skabe struktur, overblik og retning, også når der er mange bolde i luften',
         '37 parallelle projekter og 11 samtidige leverancer på én gang; struktur i skriftlig plan, navngiven ejer og dato på hver opgave.'),
        ('Er synlig og nærværende og formår at skabe tillid og følgeskab',
         'Gemba dagligt og ledelse på skiftende byggepladser og værksteder; nærved-hændelser rapporteres, når svaret er en rettelse og ikke en navngivning.'),
        ('Tager initiativ og ser muligheder for forbedringer frem for blot at holde driften kørende',
         'Forbedringer startet uden påbud, mens driften kørte — standarder, værktøjer og arbejdsgange taget i brug, før nogen bad om dem.'),
        ('Kommunikerer tydeligt og kan samarbejde med forskellige interessenter',
         'Dansk som modersmål og professionelt engelsk; daglig dialog med medarbejdere, kunder, leverandører og rådgivere — svære samtaler taget tidligt.'),
        ('Er nysgerrig på teknologi, nye perspektiver og smartere måder at arbejde på',
         'Bygger egne løsninger i Python, Claude og Power BI; nye værktøjer prøvet af på egen hånd først, derefter lært videre til teamet.'),
        ('Er nysgerrig på, hvordan AI, Copilot og andre digitale værktøjer kan gøre arbejdet enklere og skabe mere værdi',
         'Automatiseret rapportering, tjeklister og tilbud med over 40 % produktivitetsløft; metoden er at løse den irriterende opgave sammen med den, der har den.'),
        ('Trives tæt på den daglige drift, hvor personaleledelse, prioritering og udvikling kombineres',
         'Lederen på gulvet i 20 år — værksted, byggeplads og 24/7-anlæg; jeg søger ikke en strategisk rolle langt fra den daglige drift.'),
        ('Har lyst til det reelle ledelsesansvar og motiveres af at skabe resultater gennem andre',
         'Resultater leveret gennem teamet: nul kritiske afvigelser, 40 % lavere energiforbrug og lærlinge, der i dag arbejder selvstændigt.'),
        ('Indgår i et velfungerende lederteam og løfter et fælles ansvar',
         'Lederteams og tværfaglige fora med 25 specialister og 14 medarbejdere; ansvar delt eksplicit, og beslutninger taget i fællesskab frem for alene.'),
    ], widths=(3600, 7046))

    m.section("TÆT PÅ DRIFTEN ER IKKE DET MODSATTE AF AT LØFTE BLIKKET")
    m.para("Det er i den daglige drift, forbedringerne bliver mulige: man ser, hvor varen venter, hvor "
           "systemet kræver det samme indtastet to gange, og hvor en kollega løber for at rette op på noget, "
           "der kunne have været undgået. En leder, der er der, får de observationer gratis — men kun hvis "
           "teamet oplever, at det fører til noget. Derfor er min ambition for de første måneder dobbelt: "
           "driften skal stå stille og roligt, mens vi flytter to eller tre ting, som alle kan mærke. Det er "
           "sådan, et mandat bliver til følgeskab.", after=80)

    return m.save(path, title="Team Manager, Hardware Operations — Atea",
                  subject="Drift, personaleledelse og forbedringer",
                  keywords="team manager, hardware operations, personaleledelse, stabil drift, lean, 5s, "
                           "ai, copilot, python, power bi, kompetencematrix, ballerup, atea")


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Atea_TeamManagerHardwareOperations.docx')))
