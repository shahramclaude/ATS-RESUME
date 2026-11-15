# -*- coding: utf-8 -*-
"""City Container A/S — Operations Director, Farum.

Form (master/FORMKATALOG.md): åbning **C** (stedet: kl. 06.15 på pladsen),
struktur **De fem tal** (udnyttelse · tomkørsel · skader og nedetid · svartid ·
menneskerne), register **Pladsen** (plads, vogn, last, hjul, værksted, skift) — nyt
register. Kulturfil: jd/CityContainer_OperationsDirector_kultur.txt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Operations Director · drift, flåde og materiel'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('11. november 2026')
    m.meta('City Container A/S · Farum Gydevej 62, Farum')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Operations Director', bold=True, color='1A1A1A')
    m.para('Til adm. direktør Kathrine Konnerup', after=60)

    # ---------------------------------------------------------------- side 1
    m.para('**Klokken 06.15 på pladsen i Farum er dagens resultat allerede ved at være afgjort.** '
           'Er vognene lastet, er ruterne kørt igennem, står værkstedet med en bil og en smed, der '
           'mangler en reservedel? Det er her, driften bliver til, og det er her, jeg har brugt min '
           'karriere. Stillingen handler ikke om at stå der hver morgen. Den handler om at gøre '
           'klokken 06.15 forudsigelig i Farum, i Kolding og i Odense — også den morgen, hvor du '
           'ikke selv er der. Det er den slags beslutning, der bliver taget i **ledergruppen**.',
           after=60)

    m.para('**City Container er en landsdækkende organisation med ca. 400 medarbejdere, afdelinger '
           'fra Hørsholm og Greve til Kalundborg, Odense og Kolding og en vognpark på omkring 175 '
           'biler** — komprimatorbiler til kommunalt affald, lastbiler til industrien og container- '
           'og kranbiler til byggeriet, plus containere, materiel og et værksted, der skal holde det '
           'kørende. Det er en organisation, hvor et stop ét sted bliver et problem et helt andet '
           'sted, og hvor forskellen på en god og en dyr måned ligger i processer, ikke i '
           'anstrengelse.', after=60)

    m.para('**De fem tal, jeg ville styre efter.**', after=50)

    m.para('**Udnyttelsen.** Hvor stor en del af døgnet er hver vogn på vej, og hvor meget står den '
           'stille ved læssestedet, i kø eller på værksted? Det tal har jeg arbejdet med i praksis: '
           'dagligt tavlemøde, kapacitetsanalyse hver morgen og omprioritering samme dag i 11 '
           'samtidige anlægsprojekter med 14 medarbejdere.', after=44)

    m.para('**Tomkørslen.** Den koster brændstof, hjul og tid, og den er usynlig i regnskabet. Jeg '
           'har ikke kørt ruteplanlægning i et transport-IT-system; jeg har arbejdet med den samme '
           'slags tal i drift — forbrug pr. anlæg, målt, sammenlignet og fulgt op, indtil forbruget '
           'var **over 40 % lavere**.', after=44)

    m.para('**Skaderne og nedetiden.** En skade er tre udgifter: bilen, forsikringen og de timer, '
           'værkstedet holder en anden vogn fra. Jeg har haft bilpark og materiel som '
           'ansvarsområde i ARJ Engineering med indkøb, service og skader, og jeg har selv stået i '
           'værkstedet, når en reservedel skulle findes.', after=44)

    m.para('**Svartiden.** Hvor lang tid går der, fra salg lover en kunde en container, til '
           'chaufføren står der? Den tid har jeg siddet med fra begge sider: som entreprenør med '
           'egne kunder, og som den, der måtte ringe til kunden og forklare, at det blev i '
           'morgen.', after=44)

    m.para('**Menneskerne.** **Sygefravær**, gennemtræk og hvor mange der bliver længe nok til at kunne '
           'noget. Det er det tal, de fire andre hænger på. Jeg har oplært 12 teknikere og 3 '
           'lærlinge i standarder, de kunne arbejde efter, og jeg har haft ledere, der refererede '
           'til mig.', after=60)

    m.para('**Jeg har ikke ledet 400 mand, og jeg kommer ikke fra transport eller logistik.** Det '
           'skal stå klart. Det, jeg har, er 20+ år i drift af tekniske anlæg, 37 kapitalprojekter '
           'fra krav til aflevering, ansvar for drift på flere adresser samtidig og en virksomhed '
           'med eget regnskab siden 2023. Ledelse gennem ledere er ikke noget, jeg skal lære: har '
           'du ledere, der refererer til dig, er din vigtigste opgave at gøre dem i stand til at '
           'tage beslutningen uden dig.', after=60)

    m.para('**Professionalisering og forandringsledelse er ikke et projekt, der bliver færdigt — og '
           'det laves med dem, der skal leve med det.** I 2022 havde vi 11 anlægsprojekter i luften '
           'samtidig; det gik '
           'kun med et fast tavlemøde, en skriftlig opfølgning pr. projekt og 5S i værkstedet. '
           'Chauffører med 20 år på samme ruter og smede, der kender materiellet bedre end nogen '
           'manual, har ret i mere, end en ny plan antager. Jeg har selv bygget værktøjer i '
           '**Python** til data, tjeklister og rapporter — **IT-systemer** er det sted, hvor tallene '
           'bliver til en beslutning.', after=60)

    m.para('Jeres eget sprog er grunden til, at jeg søger: **vores vigtigste ressource er vores '
           'medarbejdere**, **branchens bedste service**, og en kultur, hvor man **passer på '
           'hinanden og løfter i fællesskab** og **passer på vores medarbejdere** — med **et godt '
           'arbejdsklima**, **løbende efteruddannelse** og et **forebyggende '
           'vedligeholdelsesprogram**, der giver **høj driftsikkerhed**. I vil **arbejde systematisk '
           'med løbende forbedringer** og har **målbare mål for kvalitet, miljø og arbejdsmiljø**; '
           '**den enkelte gør den store forskel**, **vi samarbejder og udvikler hinanden**, og '
           '**løbende opfølgning er en naturlig del af vores arbejdsdag**. Når I samtidig driver et '
           '**rummeligt arbejdsmarked** med **meningsfulde jobs** og **bæredygtige affalds- og '
           'logistikløsninger** og **cirkulære logistikløsninger** med **genanvendelse** og '
           '**bæredygtighed** som mål, er det en drift, der bliver målt på mere end kroner.',
           after=60)

    m.para('**Praktisk:** jeg bor i Måløv, 20 minutter fra Farum, har kørekort og bil og kan være i '
           'Kolding og Odense som en fast del af ugen. Jeg taler og skriver dansk og engelsk og kan '
           'starte efter aftale. Det, jeg gerne vil høre om, er, hvordan I i dag måler udnyttelsen '
           'på tværs af afdelingerne — og om værkstedet er en omkostning eller en kapacitet i jeres '
           'planlægning.', after=50)

    m.meta('Med venlig hilsen', after=15)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('**Driftsledelse** og projektledelse med 20+ års erfaring fra tekniske anlæg i døgndrift — '
           '**elautoriseret maskinmester (LV/MV/HV)**, B.Tech i teknologiledelse og maskinteknik. Har '
           'ledet **14 medarbejdere** og **11 samtidige anlægsprojekter** på flere adresser, ført '
           '**37 kapitalprojekter** og drevet en virksomhed med **fuldt P&L** siden 2023. '
           'Ansvarsområder: **flåde og materiale**, **værksted**, **arbejdsmiljø** og **budgetter** '
           'på 2–10 mio. kr.', after=70)

    m.section('PLADSEN — DRIFT, FLÅDE OG MENNESKER')
    for label, body in [
        ('Drift på flere adresser',
         '11 samtidige anlægsprojekter i 2022 med 14 medarbejdere og underentreprenører: '
         'kapacitetsanalyse hver morgen, omprioritering samme dag og én samlet **tidsplan**.'),
        ('Flåde, materiel og værksted',
         'Bilpark og materiel som ansvarsområde i ARJ Engineering: **indkøb**, service og '
         '**skader**, **vedligehold** og maskinværksted med 12 teknikere.'),
        ('Mennesker og ledere',
         'Ledere har refereret til mig; 12 teknikere og 3 lærlinge oplært i standarder, de kunne '
         'arbejde efter, og 8 medarbejdere i egen virksomhed med **rekruttering** og oplæring.'),
        ('Økonomi og performance',
         '**Budget** på 2–10 mio. kr. pr. projekt og fuldt **P&L** siden 2023; **KPI**-opfølgning '
         'månedligt med afvigelsesforklaring til ledelse og bygherre.'),
        ('Processer og forbedringer',
         '**5S**, standard work og **tavlemøder** hver dag; **over 40 % lavere energiforbrug** '
         'gennem måling og indregulering.'),
        ('Kunder og salg',
         'Egen virksomhed: **kunder** i det private og erhverv, tilbud og kontrakt.')]:
        m.bullet(label, body, after=16)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · elautorisation',
         [('Drift, kunder og økonomi',
           'Tilbud, udbud og ændringshåndtering; **budget** og **økonomi**, kunder, rådgivere og '
           'entreprenører i daglig koordinering.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('Krav, udførelse og aflevering',
           'Kravspecifikation, FAT/SAT og idriftsættelse; afvigelser lukket med navn og dato og nul '
           'kritiske fund ved aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter',
         [('Fremdrift og kapacitet',
           'Dagligt **tavlemøde**, kapacitetsanalyse og omprioritering samme dag; leverancer styret '
           'til deadline med afleveringspakker.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Lynetten under Biofos · København · aug. 2017–jan. 2022',
         'Renseanlæg i 24/7-drift · SRO · pumper, bassiner, pumpestationer',
         [('Drift, måling og energi',
           'Belastning og drift fulgt i døgndrift; **over 40 % lavere energiforbrug**; 12 teknikere '
           'og 3 lærlinge oplært; **arbejdsmiljø** og 5S indført som standard.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 teknikere · maskinværksted · bilpark og materiel',
         [('Værksted, materiel og service',
           'Fejlfinding, kalibrering og reparation; **indkøb** og **vedligehold** af materiel og '
           'bilpark; oplæring og opfølgning på mål for 12 teknikere.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=16)

    m.section('UDDANNELSE OG AUTORISATION')
    m.edu('B.Tech, teknologiledelse og maskinteknik',
          'Maskinmesterskolen København · 2017–2022 · gennemsnit 7,6/12')
    m.edu('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('Køle- og ventilationsteknik · AMU', 'Mercantec 2021 · STCW, Søfartsstyrelsen 2021')
    m.edu('El- og maskinteknisk konstruktion, elteknik',
          'Tehran Technical University · 2000–2003 · EQF 6')

    m.section('SPROG, IT OG PRAKTIK')
    m.para('Dansk og engelsk, skriftligt og mundtligt · Persisk: modersmål · **IT**: SRO/SCADA, '
           'ERP-baserede drifts- og økonomisystemer, Excel og egne **Python**-værktøjer til data, '
           'tjeklister og rapporter · **Kørekort B og egen bil** · Måløv, 20 minutter fra Farum · '
           'Kan starte efter aftale · Referencer på forespørgsel.', after=50)

    m.models_table('OPSLAGETS KRAV — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Stærk leder og people manager med gennemslagskraft og overblik',
         '14 medarbejdere i 11 samtidige anlægsprojekter, 12 teknikere i værkstedet og 8 ansatte i '
         'egen virksomhed; ledere har refereret til mig.'),
        ('Sætte en tydelig retning og skabe følgeskab',
         'Fast tavlemøde hver morgen i 11 samtidige projekter, hvor alle kunne se, hvad der var '
         'booket, og hvad der blev omprioriteret — i 37 projekter uden at standse hinanden.'),
        ('Jordnær og tilgængelig',
         'Jeg har stået i værkstedet og på anlægget, ikke kun i mødelokalet: 5 år i 24/7-drift og '
         'en egen virksomhed, hvor kunden ringer til den, der ejer den.'),
        ('Overordnet ansvar for drift, flåde, materiel og værkstedsfunktion',
         '**Drift** i 24/7 i 5 år, **flåde** og **materiel** med indkøb, service og skader i ARJ '
         'Engineering, og **værksted** med 12 teknikere og fast 5S.'),
        ('Lede en større operationel organisation med funktionærer, chauffører, mekanikere og smede',
         'Blandede faggrupper i 20+ år: 14 medarbejdere plus underentreprenører, 12 teknikere og 3 '
         'lærlinge; 25 specialister i 37 projekter.'),
        ('Lede en geografisk spredt driftsorganisation på flere lokationer',
         '11 samtidige anlægsprojekter på flere adresser i 2022; i dag kunder og opgaver spredt over '
         'Storkøbenhavn fra egen virksomhed.'),
        ('Daglig ledelse gennem ledere og udvikling af dine ledere',
         'Ledere har refereret til mig; min opgave var at gøre dem i stand til at tage beslutningen '
         'selv — ugentlig opfølgning i 37 projekter, ikke møder.'),
        ('Skabe en effektiv og velfungerende organisation',
         '11 samtidige anlægsprojekter gennemført med 14 medarbejdere i 2022 uden at standse '
         'driften; 37 kapitalprojekter afleveret med nul kritiske fund.'),
        ('Være hands-on og gå ned i detaljen i operationelle problemstillinger',
         'Fejlfinding og reparation på industrielt udstyr i 7 år, SRO og pumper i 24/7-drift i 5 '
         'år; jeg går ned i sagen, når tallet ikke stemmer.'),
        ('Professionalisere og optimere driften',
         '**Effektivisering** dokumenteret: **over 40 % lavere energiforbrug** gennem måling og '
         'indregulering; 5S og standard work indført i værksted og på anlæg.'),
        ('Skabe struktur og udvikle processer',
         'Fast rækkefølge fra behov til aflevering i 37 projekter; **processer** skrevet ned som '
         'tjeklister og standarder, så en efterfølger kunne overtage uden mig.'),
        ('Sikre effektiv anvendelse af ressourcer og materiel',
         'Kapacitetsanalyse hver dag i 11 samtidige projekter og **vedligehold** planlagt '
         'forebyggende; materiel og **bilpark** styret på service, skader og levetid.'),
        ("Arbejde med tal og KPI'er og bruge data til forbedring og opfølgning",
         '**KPI**-opfølgning månedligt i 37 projekter og dagligt på tavlen; data renset og '
         'sammenstillet i egne **Python**-værktøjer, fordi et tal uden reference er en antagelse.'),
        ('Flåde og materiel: bilpakke, indkøb og vedligeholdelse',
         '**Bilpark** og materiel som ansvarsområde i ARJ i 7 år med **indkøb**, service og syn samt '
         '**vedligehold**; i dag egen virksomhed med servicevogne i drift.'),
        ('Håndtering af skader',
         'Jeg har håndteret **skader** i bilparken i 7 år: vurdering, forsikring og reparation, plus '
         'den driftsmæssige side — hvad koster 3 dages stilstand?'),
        ('Overholdelse af lovgivning som arbejdsdirektivet og køre- og hviletidsregler',
         'Jeg har arbejdet med **arbejdsdirektivet** og **hviletidsregler** i praksis ved planlægning '
         'af kørsel og arbejdstid i 20+ år; jeg har siddet med vagtplanen, ikke læst om den.'),
        ('Bred kontaktflade og tæt samarbejde med salgsorganisationen',
         '**Salgsorganisationen** som modpart i 20+ år: i egen virksomhed er den, der sælger, og den, '
         'der kører, de samme to — loveriet bliver opdaget med det samme.'),
        ('Se forretningen som en helhed: kunder, salg, drift, økonomi og medarbejdere',
         '**Kunder**, **salg**, **drift**, **økonomi** og **medarbejdere** i samme model i egen '
         'virksomhed med fuldt **P&L** siden 2023; en forkert prioritering blev synlig i '
         'regnskabet samme kvartal.'),
        ('Analytisk og struktureret, men ikke teoretisk, og handlingsorienteret',
         'Data, hypotese, måling på anlægget, konklusion — brugt i 5 års døgndrift og i 37 '
         'afleveringer; beslutningen blev taget på stedet, ikke i en rapport ugen efter.'),
        ('Nysgerrig på forbedringer og udfordre arbejdsgange konstruktivt',
         'Forbruget faldt over 40 %, fordi vi turde spørge til, hvorfor en pumpe kørte, som den '
         'gjorde; 5S blev indført, fordi værktøjet ikke var der, hvor det blev brugt.'),
        ('Respekt for den erfaring og faglige viden der findes i organisationen',
         'Standarder skrevet sammen med dem, der skulle arbejde efter dem — 12 teknikere, 3 '
         'lærlinge og 8 medarbejdere i egen virksomhed; ellers holder forbedringen kun til næste '
         'travle uge.'),
        ('Robust, handlekraftig og beslutningsdygtig',
         '37 projekter med 0 kritiske fund og 11 samtidige anlægsprojekter uden standsning af '
         'drift; beslutninger taget samme dag, når leverancen skred.'),
        ('Kommunikere naturligt med mennesker på alle niveauer',
         'Dansk og engelsk på alle niveauer: værkstedet, chaufføren, bygherren og direktionen — '
         'beslutningsoplæg på 1-2 sider og referater med navn og dato i 20+ år.'),
        ('Erfaring fra en operationel lederstilling med en større driftsorganisation',
         'Operationel ledelse i 20+ år: 14 medarbejdere og 11 samtidige projekter, 12 teknikere, 8 '
         'ansatte og fuldt **P&L**. En organisation på 400 er større, end jeg har ledet — det står '
         'også i brevet.'),
        ('Baggrund inden for transport, logistik, distribution, supply chain, service eller industri',
         '**Industri** og **service**: 7 år med industrielt udstyr og værksted, 5 år i 24/7-drift og '
         'siden 2023 egen virksomhed med egne vogne. **Transport** og **logistik** er nyt for mig.'),
        ('Erfaring med kompleks operationel drift, effektivisering og organisationsudvikling',
         '**Kompleks drift**: 24/7-anlæg, 11 samtidige projekter, 25 specialister; '
         '**effektivisering** med over 40 % lavere forbrug; **organisationsudvikling** fra 5 til 8 '
         'ansatte.'),
        ('Solid ledelseserfaring med at lede gennem andre og selv være tæt på driften',
         'Ledere, der refererer til mig, samtidig med at jeg selv har stået i værkstedet og på '
         'anlægget — 20+ år hvor begge dele var en del af arbejdsdagen.'),
        ("Analytisk arbejde med økonomi, performance og KPI'er og omsætte data til handling",
         '**Økonomi** og **performance** månedligt i 37 projekter og dagligt på tavlen; data '
         'omsat til en anden rute, en anden indstilling eller en anden bemanding samme uge.'),
        ('Relevant videregående uddannelse',
         '**Elautoriseret maskinmester (LV/MV/HV)**, Sikkerhedsstyrelsen 2023; B.Tech i '
         'teknologiledelse og maskinteknik 2017-2022 med 7,6/12; EQF 6 fra 2003.'),
        ('Flydende dansk og engelsk, skriftligt og mundtligt',
         'Dansk som modersmål og engelsk professionelt, også teknisk og i forhandlinger; '
         'persisk som tredje sprog og 20+ år med engelsksproget dokumentation.'),
        ('Erfaren IT-bruger der arbejder sikkert og effektivt i forskellige systemer',
         'SRO/SCADA i 5 år, ERP-baserede drifts- og økonomisystemer, Excel og egne **Python**-'
         'værktøjer; **IT-systemer** er der, hvor tallene bliver til en beslutning.')])

    m.section('DE FØRSTE 90 DAGE')
    for b in (
        'Kørt pladserne igennem — Farum, Kolding, Odense — og set den samme uge: hvordan lastes '
        'der, og hvad venter værkstedet på.',
        'Lavet én oversigt over de fem tal pr. afdeling og sat de to, der kan flyttes inden for '
        '90 dage, i gang med en ejer og en dato.',
        'Siddet med hver leder og aftalt, hvad de selv skal beslutte, og hvad der skal op til '
        'mig — ledelse gennem ledere begynder med en tydelig grænse.'):
        m.bullet('', b, after=16)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_CityContainer_OperationsDirector.docx')
    build(out)
    print(out)
