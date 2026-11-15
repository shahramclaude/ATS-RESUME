# -*- coding: utf-8 -*-
"""Bravida Danmark — Afdelingschef til tværfaglig enhed, Kalundborg.

Dansk opslag → dansk dokument: ansøgning p1, CV p2, uddannelse + 90 dage +
fire sektioner p3, kravmatrix p4.
Vinkel: en tværfaglig afdeling er ikke tværfaglig, fordi den har tre fag — den er
tværfaglig, når nogen ejer snitfladerne og økonomien i dem.
Policy: master/README.md — jobbet først, kandidaten kun som bevis, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Afdelingschef · Tværfaglig entreprise, økonomi og ledelse'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Danmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("8. november 2026")
    m.meta("Bravida Danmark · Tværfaglig afdeling · Kalundborg")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Afdelingschef, tværfaglig enhed i Kalundborg", bold=True, color='1A1A1A')
    m.para("Til regionsledelsen i Bravida og afdelingen i Kalundborg", after=70)

    # ---------------------------------------------------------------- side 1
    m.para("I Kalundborg er bygherren ikke en tilfældig kunde. Det er en produktionsvirksomhed, hvor et "
           "nedbrud koster mere end entreprisen, hvor adgang og tilladelser skal aftales uger i forvejen, og "
           "hvor dokumentationen skal kunne tåle, at nogen læser den to år senere. Det er den virkelighed, en "
           "**tværfaglig** afdeling i Kalundborg skal kunne levere i — og det er den, jeg har arbejdet i.", after=80)

    m.para("**En afdeling er ikke tværfaglig, fordi den har tre fag på lønningslisten.** Den er **tværfaglig**, "
           "når nogen ejer snitfladerne: hvem der leverer hvad til hvem, hvornår el-arbejdet skal være færdigt "
           "for at **ventilation** og **VVS** kan komme videre, og hvem der har sagt ja til en ændring, før "
           "den bliver til et tillæg. Det arbejde er der ingen, der ser i et regnskab, men det er der, "
           "**dækningsgrad**en bliver afgjort.", after=80)

    m.para("**Jeg har arbejdet på den største bygherre i Kalundborg — indefra.** Fra 2022 til 2024 var jeg "
           "projektleder og idriftsættelsesingeniør på **Novo Nordisk** i Kalundborg på **37 parallelle "
           "CAPEX-projekter** af 2–10 mio. kr. under **GMP/FDA/EMA**. Jeg kender adgangsprocedurerne, "
           "kravene til dokumentation, tempoet i et anlæg der kører, og hvordan entreprenører bliver vurderet, "
           "når de står i det. Det er en fordel, en lokal afdeling kun kan få på én måde.", after=80)

    m.para("**Entreprenøkonomi har jeg stået i ansvaret for — ikke kigget på.** Som ejer af ELOHVAC har jeg "
           "regnet **kalkulation**er, afgivet tilbud, forhandlet **AB 18** og **totalentreprise**, styret "
           "**underentreprenører** og fulgt **dækningsgrad**en måned for måned med **fuldt P&L-ansvar**. Før "
           "det havde jeg 11 samtidige anlægsprojekter med 14 mand og en **ordrebog**, der skulle leveres, "
           "mens kapaciteten blev flyttet rundt. **Budgetter** er ikke noget, man lægger oven på driften; de "
           "er den ramme, driften skal passe ind i.", after=80)

    m.para("**Fagene har jeg haft fingrene i — el i bund, ventilation og køl ovenpå.** Jeg er "
           "**elautoriseret maskinmester (LV/MV/HV)** og har bygget, testet og idriftsat tavler og styringer; "
           "på Ventek-Air ledede jeg **ventilation**sentrepriser med 14 medarbejdere, og jeg har "
           "køleteknik og klimaanlæg med fra AMU. Det gør det muligt at sparre fagligt med svendene og "
           "samtidig holde **VVS**-snitfladen, uden at afdelingen skal forklares af en projektleder, hvad der "
           "kan lade sig gøre.", after=80)

    m.para("**Kunder bliver ikke skabt af et tilbud; de bliver bevaret af den næste opgave.** Jeg har bygget "
           "en **kundeportefølje** fra nul i egen virksomhed, med **serviceaftaler** der holder kunden i drift "
           "efter afleveringen, og med den rækkefølge, der virker: kom først, mål før du foreslår, og skriv "
           "hvad du har aftalt. Bravidas styrke er, at **serviceaftaler** og entreprise kan trække i samme "
           "retning — den, der sidder med driften, skal ikke opdage, at entreprisen ikke kender anlægget.",
           after=80)

    m.para("**Strategi bliver kun til noget, når den kommer ud som en beslutning i en afdeling.** Jeg har "
           "omsat mål til månedstal og ugentlige handlinger: hvilke kunder der skal besøges, hvilke tilbud der "
           "skal af, hvilke medarbejdere der skal uddannes til det næste fag, og hvad der skal siges nej til. "
           "Det er den slags implementering, jeg vil lave sammen med **regionsledelsen** — og det kræver, at "
           "jeg kommer med tal, ikke med ønsker.", after=80)

    m.para("**Mennesker i pressede situationer er lederens egentlige prøve.** Jeg har ledet 5, 12, 14 og 25 "
           "mennesker — i skiftende byggepladser, i 24/7-drift og i en virksomhed, hvor jeg selv var den, der "
           "skulle sige, at ugen ikke gik som planlagt. **Trivsel** og **sikkerhed** kommer først, ikke fordi "
           "det er pænt, men fordi en afdeling, der har været presset for længe, begynder at lave fejl, som "
           "koster mere end den ekstra uge. **MUS**, **kompetencematrix**, oplæring af **lærlinge** og "
           "**arbejdsmiljø** er værktøjerne; opmærksomheden er det, der får dem til at virke.", after=80)

    m.para("**Bravidas styrke er, at ét Bravida kan levere det, en enkelt afdeling ikke kan.** En lokal "
           "afdeling på 20–30 mand kan ikke holde alle specialister selv, men den kan trække på en koncern med "
           "13.000 medarbejdere, heraf 3.000 i Danmark, 180+ byer, noteret på **Nasdaq Stockholm** og med en "
           "målsætning om at være **klimaneutral** i værdikæden i 2045. Det er en kvalitet i tilbuddet, kunden kan mærke — hvis afdelingen ved, hvem "
           "den skal ringe til, og hvis nogen tager ansvaret for, at det sker.", after=80)

    m.para("Jeg bor i Måløv, har kørekort og bil og har pendlet turen til Kalundborg i to år — jeg ved, hvad "
           "den koster, og hvordan ugen skal lægges. Jeg vil gerne høre, hvordan afdelingen er sammensat i dag "
           "— fag, mandskab og den nuværende **kundeportefølje** — hvordan I måler en afdelingschef på både "
           "**trivsel** og **dækningsgrad**, og hvilke dele af den samlede vækststrategi Kalundborg skal bære.",
           after=70)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Forretningsansvarlig leder med 20+ års erfaring i el-, ventilations- og anlægsentrepriser — "
           "**elautoriseret maskinmester (LV/MV/HV)** med **fuldt P&L-ansvar** siden 2023 og 37 CAPEX-projekter "
           "som projektleder hos **Novo Nordisk** i **Kalundborg** under **GMP/FDA/EMA**. Har regnet "
           "**kalkulation**er, forhandlet **AB 18** og **totalentreprise**, styret **underentreprenører** og "
           "fulgt **dækningsgrad** og **budgetter**; ledet teams på 5–25 medarbejdere med **MUS**, "
           "**kompetencematrix** og **arbejdsmiljø** som faste rammer. Dansk og professionelt engelsk.",
           after=80)

    m.section("FORRETNING, ENTREPRISE OG LEDELSE")
    for label, body in [
        ("Forretningsudvikling og kunder",
         "Kundeportefølje og serviceaftaler bygget fra nul i egen virksomhed; nye forretningsmuligheder "
         "fundet ved at komme først, måle først og skrive aftalen ned — og ved at sige nej til det, der ikke "
         "kan leveres."),
        ("Entreprenøkonomi og kalkulation",
         "Tilbud, kalkulation, AB 18 og totalentreprise med underentreprenører; månedlig opfølgning på "
         "dækningsgrad, budgetter og udestående, så afvigelser blev opdaget i den måned, de opstod."),
        ("Tværfaglig koordinering",
         "El, ventilation og køl i samme leverance: snitflader navngivet, rækkefølgen aftalt og ændringer "
         "besluttet, før de blev til tillæg — på 37 projekter og i egen virksomhed."),
        ("Ledelse i pressede perioder",
         "5–25 medarbejdere gennem 20 år: MUS og 1:1, kompetencematrix, oplæring af lærlinge, rekruttering og "
         "samtaler, når ugen ikke gik som planlagt."),
        ("Strategi omsat til handling",
         "Mål brudt ned til månedstal og ugentlige handlinger; prioritering af kunder, tilbud og uddannelse "
         "med regionsledelsen som medspiller, ikke som modtager."),
        ("Sikkerhed og arbejdsmiljø",
         "APV, risikovurdering ved opstart, LOTO og nærved-hændelser som linjelederansvar; nul kritiske "
         "afvigelser i serviceaftalerne, og sikkerhed drøftet hver uge — ikke kun når der er sket noget."),
    ]:
        m.bullet(label, body, after=25)

    m.section("ERHVERVSERFARING")
    jobs = [
        ("Ejer / teknisk direktør",
         "ELOHVAC ApS · København · maj 2023–nu",
         "Fuldt P&L · kalkulation og tilbud · 5 elektrikere + 3 lærlinge",
         [("Forretning, økonomi og kunder",
           "Kundeportefølje opbygget fra nul; tilbud og kalkulation, AB 18 og underentreprenører, "
           "dækningsgrad og budgetter fulgt månedligt, og serviceaftaler der holder kunden i drift."),
          ("Ledelse og faglig sparring",
           "Daglig ledelse, MUS, oplæring af lærlinge og faglig sparring på el-tekniske løsninger; "
           "kompetencematrix brugt til at beslutte, hvem der skulle uddannes til hvad.")]),
        ("Senior idriftsættelsesingeniør / projektleder, elsystem",
         "Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024",
         "37 parallelle CAPEX-projekter · 25 specialister · GMP/FDA/EMA",
         [("Entreprise og snitflader i Kalundborg",
           "37 projekter af 2–10 mio. kr. med teknik, indkøb og drift i samme plan; adgang, tilladelser og "
           "dokumentation håndteret i et anlæg, der ikke måtte stoppe."),
          ("Kvalitet, økonomi og aflevering",
           "FAT/SAT og IQ/OQ/PQ med nul kritiske afvigelser; budgetopfølgning og månedlig rapportering til "
           "ledelse og bygherre.")]),
        ("Projekt- og værkstedsleder",
         "Ventek-Air · København · jan. 2022–nov. 2022",
         "14 medarbejdere · 11 ventilationsentrepriser · DKK 2–10 mio.",
         [("Ventilationsentrepriser og kapacitet",
           "11 anlægsprojekter fra specifikation til formel aflevering med 14 mand; udbud og tilbud, "
           "underentreprenører, aftalegrundlag og daglig kapacitetsstyring.")]),
        ("Vedligeholdelses- og driftsleder",
         "Lynetten under Biofos · København · aug. 2017–jan. 2022",
         "Kritisk anlæg i 24/7-drift · tavler, pumper, HVAC · SRO/SCADA",
         [("Drift, sikkerhed og forbedring",
           "Forebyggende vedligehold og akut fejlfinding; 5S, standard work og PDCA på værksted og lager med "
           "over 40 % lavere energiforbrug; LOTO, APV og nærved-hændelser.")]),
        ("Elektromekaniker / produktionsteamleder",
         "ARJ Engineering · Teheran · dec. 2003–mar. 2010",
         "12 mekanikere og teknikere · maskinværksted",
         [("Team og målopfølgning",
           "Daglig ledelse af 12 teknikere: vagtplanlægning, materialestyring og målopfølgning på industrielle "
           "anlæg.")]),
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
    m.para("Dansk: modersmål, flydende i skrift og tale · **Engelsk: professionelt** · Persisk: modersmål · "
           "**Bosat i Måløv** med to års pendling til Kalundborg fra Novo Nordisk-tiden · Kørekort B og egen "
           "bil · Kan tiltræde snarest muligt eller efter aftale · Referencer efter aftale.", after=70)

    m.models_table("DE FØRSTE 90 DAGE — PORTEFØLJEN, FAGENE OG MÅLTALLENE",
                   ("Periode", "Hvad der sker, og hvordan det måles"), [
        ("Uge 1–2",
         "Gennemgå den overtagne portefølje: igangværende entrepriser, tilbudslisten, ordrebogen og de "
         "kunder, der sidder i den; mød medarbejderne på pladsen og i værkstedet og hør, hvor snitfladerne "
         "driller; aftal med regionsledelsen, hvilke tre tal afdelingen styres på."),
        ("Dag 30",
         "Én side pr. igangværende entreprise med økonomi, fremdrift, risiko og næste beslutning; "
         "dækningsgrad og udestående gennemgået med økonomi; MUS- og 1:1-samtaler planlagt med alle, og "
         "kompetencematrix opdateret så det er tydeligt, hvem der kan hvad."),
        ("Dag 60",
         "Salgsplan for lokalområdet aftalt: hvilke kunder der skal besøges, hvilke rammeaftaler og "
         "serviceaftaler der skal fornyes, og hvilke to faglige huller der skal lukkes med rekruttering eller "
         "uddannelse; første fælles tværfaglige tilbud afgivet med snitfladerne prissat."),
        ("Dag 90",
         "Afdelingen leverer på budget med kendt dækningsgrad og ordrebog dækkende de næste kvartaler; "
         "trivsel og sygefravær fulgt som et tal på linje med økonomien; to forbedringer gennemført i "
         "arbejdsgange eller sikkerhed, og en plan for det kommende år, som regionsledelsen kan nikke til.")])

    m.section("EN AFDELING ER IKKE TVÆRFAGLIG, FORDI DEN HAR TRE FAG")
    m.para("Det er snitfladerne, der afgør, om en **tværfaglig** afdeling leverer som én entreprenør eller som "
           "tre. Hvem sætter føringsveje, før ventilationen er projekteret? Hvem bestiller tavlen, når "
           "VVS-rørene skal igennem det samme teknikrum? Og hvem siger til kunden, at rækkefølgen ændrer sig, "
           "før det bliver et tillæg? På en byggeplads er svaret sjældent et system — det er en person, der har "
           "mandat til at beslutte det.", after=80)

    m.section("KALKULATIONEN ER DEN BESLUTNING, AFDELINGEN LEVER AF")
    m.para("Et tilbud er ikke et dokument; det er en beslutning om, hvor meget risiko afdelingen vil bære. "
           "Skrives der for lidt ind, bliver forskellen taget ud af dækningsgraden eller af den tid, "
           "svendene skulle have haft til at gøre det ordentligt. Skrives der for meget ind, får man ikke "
           "opgaven. Jeg har prøvet begge sider som ejer, og det, der flytter mest, er at have målt opgaven "
           "og aftalt grænsefladerne, inden prisen bliver sat.", after=80)

    m.section("ET OVERTAG ER ET LØFTE, IKKE EN OVERLEVERING")
    m.para("Når man overtager en eksisterende portefølje, arver man også kundernes forventning om, hvordan "
           "tingene bliver gjort — og medarbejdernes erfaring med, hvad der virker i praksis. Derfor starter "
           "jeg med at spørge, før jeg ændrer: hvad har fungeret, hvad har irriteret, og hvad ville I ønske, "
           "at en ny afdelingschef tog fat i først. Det giver både en bedre plan og den tillid, der skal til, "
           "når noget skal ændres alligevel.", after=80)

    m.section("SERVICE OG ENTREPRISE SKAL KENDE HINANDEN")
    m.para("Den entreprise, der afleveres i dag, er den serviceaftale, nogen skal drive om to år. Når de to "
           "dele af forretningen taler sammen tidligt, bliver tilbuddet stærkere: entreprisen kan bruge "
           "driften som reference, og driften ved, hvad der er bygget, hvordan det er mærket, og hvor "
           "svaghederne sidder. Det er den slags, der gør en **kundeportefølje** svær at flytte til en "
           "konkurrent.", after=80)

    m.section("EN ENTREPRISE PÅ 15–50 MIO. KR. AFGØRES I KONTRAKTEN")
    m.para("Jo større entreprisen er, jo mere af den afgøres i betingelserne og ikke på byggepladsen: "
           "tidsfrister, bod, samordningsansvar, grænseflader til de andre fag og hvem der bærer risikoen "
           "for forsinkede tegninger. Derfor læser jeg betingelserne, før jeg byder, og jeg skriver dem ind "
           "i tilbuddet — ikke som forbehold, men som en del af den pris, kunden sammenligner med. Det er "
           "den ene halvdel af **dækningsgraden**; den anden er, at den, der har skrevet tilbuddet, også "
           "står ved det, når sagen bliver svær.", after=0)

    m.page_break()

    m.models_table("HVAD STILLINGEN KRÆVER — HVAD JEG HAR LEVERET", ("Krav i opslaget", "Bevis"), [
        ('Ledelse og udvikling af en tværfaglig afdeling med fokus på trivsel, kvalitet og forretningsudvikling',
         'Ledet teams på 5, 12, 14 og 25 i el, ventilation og anlæg; trivsel, MUS og arbejdsmiljø som fast punkt og forretningsudvikling som årshjul.'),
        ('Ansvar for entrepriser i størrelsesordenen 15-50 mio. kr.',
         'Entreprenøkonomi med fuldt P&L-ansvar: kalkulation, tilbud, AB 18, totalentreprise og underentreprenører — og en portefølje på 37 samtidige projekter.'),
        ('Vedligeholdelse og udvikling af stærke relationer til både eksisterende og nye kunder',
         'Kunder fastholdt gennem elleve år i dansk el- og energidrift; kundeportefølje i egen virksomhed bygget fra nul og båret af serviceaftaler.'),
        ('Salg og udvikling af nye forretningsmuligheder i lokalområdet',
         'Egen virksomhed: alt salg og alle nye kunder skabt lokalt gennem dialog, referencer og opsøgning — ingen leadmotor bag sig.'),
        ('Udarbejdelse og opfølgning på afdelingens budgetter og økonomiske målsætninger',
         'Budget, forecast og dækningsgrad fulgt månedligt i SAP ERP og eget regneark; afvigelser forklaret og handlet i samme måned.'),
        ('Implementering af strategier og handlingsplaner i tæt samarbejde med regionsledelsen',
         'Mål brudt ned til månedstal og ugentlige handlinger; beslutninger taget med ledelsen på tal og prioriteringer, ikke på ønsker.'),
        ('Sikring af stærkt samarbejde på tværs af fagområder og Bravidas organisation',
         'El, ventilation, køl og anlæg i samme leverance med snitflader navngivet; på 37 projekter og i egen virksomhed med underentreprenører.'),
        ('Ledelse, motivation og faglig sparring af medarbejdere, også i pressede situationer',
         'Faglig sparring på LV/MV/HV-niveau og samtaler taget, når ugen ikke gik som planlagt; 20 år med skiftende byggepladser og 24/7-drift.'),
        ('Tværfaglig viden inden for en eller flere af fagområderne Ventilation, VVS eller El',
         'El i bund som elautoriseret maskinmester (LV/MV/HV); 11 ventilationsentrepriser med 14 mand hos Ventek-Air; køleteknik og klimaanlæg fra AMU.'),
        ('Betydelig erfaring med ledelse, drift og udvikling af en afdeling eller forretningsenhed',
         'Egen forretningsenhed med fuldt P&L siden 2023; før det værksteds- og driftsledelse med 14 og 12 medarbejdere og 24/7-drift.'),
        ('Dokumenteret erfaring med entrepriseprojekter og økonomisk styring',
         '37 CAPEX-projekter af 2–10 mio. kr. og 11 anlægsentrepriser gennemført fra udbud til aflevering, med budgetopfølgning og nul kritiske afvigelser.'),
        ('Stærk til at skabe og vedligeholde kunderelationer',
         'Kunderelationer båret af, at aftaler blev holdt og svar givet samme dag; også når svaret var, at opgaven ikke kunne løses som ønsket.'),
        ('Skarp strategisk forståelse og kan omsætte strategi til konkrete resultater',
         'Fra strategi til ugentlige handlinger: kundeplan, tilbudsplan og uddannelsesplan med navn og dato — og konsekvens, når det ikke blev fulgt.'),
        ('Trives i samarbejdet med både interne og eksterne interessenter',
         'Regionsledelse, økonomi, teknikere, underentreprenører, rådgivere og bygherre i samme sag; 25 specialister på tværs af fag i fælles plan.'),
        ('Kommunikerer tydeligt og professionelt på dansk og gerne engelsk',
         'Dansk som modersmål og professionelt engelsk i møder, tilbud og dokumentation — brugt i GMP-miljø med internationale standarder.'),
        ('Motiverende, engagerende og nærværende lederstil',
         'Gemba dagligt, tavlemøder og ledelse på pladsen; beslutninger taget med dem, der udfører arbejdet, og æren givet videre.'),
        ('Overtage og videreudvikle en eksisterende portefølje og forretning',
         'Overtaget og drevet egen forretning gennem vækst og tilbagegang; portefølje og ordrebog styret mod kapacitet hver uge.'),
        ('Medarbejdernes trivsel og sikkerhed kommer altid først',
         'Sikkerhed som linjelederansvar med APV, LOTO og nærved-hændelser; arbejdsmiljø drøftet hver uge, og arbejde stoppet, når det ikke var forsvarligt.'),
    ], widths=(3600, 7046))

    m.section("EN LOKAL AFDELING LEVER AF, AT NOGEN KENDER BYEN")
    m.para("I Kalundborg er afstanden mellem kunde og entreprenør kort, og der er ingen kæde at gemme sig "
           "bag: den, der har sagt ja til opgaven, møder den også, når den skal afleveres. Det gør to ting "
           "ved ledelsen af en afdeling — den skal kunne sige nej i tide, og den skal kende de håndværkere, "
           "den tilbyder med. Jeg har arbejdet to år på den største bygherre i byen og boet i pendlerafstand "
           "siden; det er ikke et lokalnetværk, jeg kan påstå, men det er et sted, jeg ved, hvordan man "
           "arbejder, og hvad der bliver lagt mærke til.", after=80)

    return m.save(path, title="Afdelingschef — Bravida Kalundborg",
                  subject="Tværfaglig entreprise, økonomi og ledelse",
                  keywords="afdelingschef, tværfaglig, entreprise, kalkulation, dækningsgrad, budget, "
                           "ventilation, vvs, el, kalundborg, bravida, ledelse")


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Bravida_AfdelingschefKalundborg.docx')))
