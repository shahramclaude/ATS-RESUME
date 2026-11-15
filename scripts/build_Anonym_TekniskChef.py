# -*- coding: utf-8 -*-
"""Anonym produktionsvirksomhed i Trekantområdet/Sønderjylland (via erwin andersen
a/s, stilling 02.11.88) — teknisk chef for teknisk afdeling, 8-10 medarbejdere.

Form (master/FORMKATALOG.md): åbning **L** (dokumentet/nummeret: stillingsnummer
02.11.88 er det eneste, der findes om virksomheden — og det flytter brevet over på
opgaven), struktur **Køen** (ordren · tegningen · indkøbet · værkstedet ·
ændringen), register **Tegnestuen** (revision, snit, tolerance, stykkliste,
frigivelse, ændringsseddel). Kulturfil: jd/Anonym_TekniskChef_kultur.txt.
Brugerbeslutning 13.11.2026: »Jeg flytter gerne« — afstanden skrives ind.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Teknisk chef · teknisk afdeling, produktion og ledelse'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('13. november 2026')
    m.meta('erwin andersen a/s · stilling 02.11.88 · Trekantområdet/Sønderjylland')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: teknisk chef, stilling 02.11.88', bold=True, color='1A1A1A')

    def lp(text, after=60):
        return m.para(text, after=after, line=236)

    # ---------------------------------------------------------------- side 1
    lp('**02.11.88.** Det er det eneste nummer, jeg har på virksomheden bag opslaget — og det er nok, '
       'fordi opgaven står i klartekst: en teknisk afdeling med **»8-10 dygtige og dedikerede '
       'medarbejdere«**, en produktion, der skal kunne bygge det, der tegnes, og en leder, der sørger '
       'for, at de to ting sker i samme uge. Når navnet er anonymt, må brevet handle om jobbet. Så det '
       'gør det.', after=56)

    lp('**Det, I ikke beder om, er en tegner.** I skriver selv, at det ikke bliver min opgave at side '
       'og nørde tegninger, fordi **»at det, der tegnes, også fungerer i produktionen«** allerede er '
       'et fag, I har folk til. Det, I beder om, er gennemtræk: at **»fjerne flaskehalse og optimere '
       'workflow«**, at **»skabe struktur, retning og overblik«** og at sikre, at I **»kommer sikkert '
       'og effektivt i mål med gennemarbejdede løsninger, der fungerer i praksis og holder i '
       'produktionen«**. Det er en produktionsopgave med en tegning som mellemled — og det er den '
       'slags opgaver, jeg har løst i tyve år, i entreprise, i drift og i egen virksomhed.', after=56)

    lp('**Fem køer.** En teknisk afdeling er en række køer, og hver kø har en ejer, en tid og en pris. '
       'Først når **»unødvendige arbejdsgange er skåret fra«**, bliver der plads til at levere — og '
       'derfor er det køerne, jeg ville starte med. Sådan ville jeg styre dem.', after=44)

    lp('**Ordren i kø.** Sælgeren har lovet en dato, før nogen har regnet på den. Derfor starter '
       'styringen dér: hvad er lovet, til hvornår, og af hvem — og hvilke tre ting i ordren der kan '
       'vælte datoen. Jeg har selv solgt med fast pris og **AB 18** og prøvet, hvad en optimistisk '
       'leveringsdato koster, når den ikke kan holdes.', after=40)

    lp('**Tegningen i kø.** Her ligger rollens kerne, og I formulerer den præcist: **»at udfordre '
       'løsningerne – ikke bare godkende dem«**. Jeg læser en tegning som den, der skal bygge efter '
       'den: kan den fremstilles, kan delene købes, kan den samles, og hvad sker der, når den skal '
       'ændres i næste uge? Det er de spørgsmål, der flytter en tegning fra godkendt til '
       'byggeklar.', after=40)

    lp('**Indkøbet i kø.** Den kø, ingen ser, og som oftest bestemmer datoen: tolv ugers leveringstid '
       'på den forkerte komponent er et halvt års forskydning. Jeg har stået med udbud, tilbud og '
       'leverandører i egen virksomhed og ved, at en leverandøraftale er et løfte med en dato — eller '
       'ikke noget.', after=40)

    lp('**Værkstedet i kø.** Den **»mest lønsomme produktionsrækkefølge«** bliver ikke besluttet i '
       'salg eller i teknik alene; den bliver besluttet i samarbejdet mellem dem, der lover, dem der '
       'tegner, og dem der står ved maskinen. Jeg har stået på alle tre sider: tolv teknikere i et '
       'maskinværksted, 14 montører i 11 samtidige anlæg og en virksomhed med fuldt **P&L**.', after=40)

    lp('**Ændringen i kø.** En ændring er ikke et problem — en ændring, der kommer for sent, er. '
       'Ændringsseddel, revision og en frigivelse, der betyder noget, er det, der holder en '
       'produktion fra at bygge efter en tegning, som ikke findes længere. I GMP-regi var det '
       'change control; i entreprise var det tillægsarbejdet; begge steder var det samme disciplin: '
       'skriv det ned, før nogen bygger.', after=56)

    lp('**Teamet, der skal performe.** I skriver, at **»trivsel og performance hænger tæt sammen«**, '
       'og at der skal ansættes flere. Jeg har ledet 25 specialister, 14 montører, 12 teknikere og '
       'siden 2023 otte egne medarbejdere — og lært, at det er forskellen på **»når teknisk afdeling '
       'performer – ikke bare producerer«**: at hver enkelt ved, hvad der er vigtigst i dag, og at det '
       'er tilladt at sige, at en opgave ikke kan nås. Ansættelser, **rekruttering**, oplæring og de '
       'første 30 dage har jeg planlagt, før stillingen blev slået op. Og det er min opgave at '
       '**»skabe retning, sikre fremdrift«** — ikke at levere flest mulige tegninger.', after=56)

    lp('**Det, jeg ikke har, står her.** Jeg er ikke konstruktør og har ikke ledet en tegnestue i en '
       'produktionsvirksomhed. Det er jeres 8-10 medarbejderes fag, og det skal blive ved med at '
       'være det. Til gengæld er jeg **elautoriseret maskinmester (LV/MV/HV)** med B.Tech i '
       'teknologiledelse og maskinteknik, har læst og udfordret tekniske løsninger i 20+ år, og ved, '
       'hvad der sker på gulvet, når en tegning er forkert — fordi jeg har stået der.', after=56)

    lp('**Jeres eget sprog er grunden.** I lover **»en markedsledende virksomhed«**, hvor jeg bliver '
       '**»en nøgleressource«**, en **»solid, jysk virksomhedskultur«** og en **»uformel omgangstone '
       'på alle niveauer«** med **»højt engagement, professionalisme«** — og et arbejdsmiljø, hvor '
       '**»samarbejde, kvalitet og ansvar går hånd i hånd«**. Det er en beskrivelse af en virksomhed, '
       'hvor man bliver målt på, om tingene bliver færdige, og hvor man siger det til hinanden, når de '
       'ikke bliver. Der vil jeg gerne lede.', after=56)

    lp('**Praktisk:** jeg bor i Måløv i dag og **flytter gerne**, så hverdagen er i Trekantområdet eller '
       'Sønderjylland. Jeg **»tager beslutninger, skærer igennem og skaber fremdrift«** — og jeg '
       '**»ser du mulighederne i samspillet mellem de forskellige grænseflader«**, fordi det er der, '
       'sagerne typisk går i stå. Dansk og engelsk, skriftligt og mundtligt. Kan starte efter aftale; '
       'referencer indhentes gerne.', after=24)

    m.meta('Med venlig hilsen', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('**Teknisk leder med produktion, projektering og økonomi under ét** — **elautoriseret '
           'maskinmester (LV/MV/HV)**, B.Tech i teknologiledelse og maskinteknik og køle- og '
           'ventilationsteknik fra AMU. 20+ år i tekniske projekter: **37 kapitalprojekter** i GMP, '
           '**11 samtidige anlægsprojekter** med 14 medarbejdere, 12 teknikere i maskinværksted og egen '
           'virksomhed med fuldt **P&L** siden 2023. Arbejder med **workflow**, **kapacitet**, '
           '**kvalitet** og **leverancer** — og med at gøre andre i stand til at levere.', after=70)

    m.section('TEGNESTUEN — SÅDAN LÆSER JEG EN TEGNING')
    for label, body in [
        ('Revisionen',
         'Hvilken revision der er gældende, og om montagen har fået den samme som indkøbet. To '
         'forskellige revisioner i omløb er den dyreste fejl, der findes — den koster to gange.'),
        ('Snittet',
         'Detaljen, der afgør om det kan samles: hvad ligger inden for hvad, hvilke rør og kanaler '
         'skal krydse, og hvad der skal demonteres igen for at komme til. Et **snit** gennem '
         'tegningen, prøvet på 11 anlæg.'),
        ('Tolerancen',
         'Hvilke mål der er kritiske, og hvilke der kan justeres på pladsen; en tolerance, der er '
         'strengere end nødvendigt, er en dyr beslutning, der aldrig bliver taget op til revision.'),
        ('Styklisten',
         'Om **en stykkliste** kan købes ind som den står: antal, leveringstid og alternativer — arbejdet '
         'med '
         '**indkøb** og **leverandører** i egen virksomhed har lært mig, at styklisten er en '
         'leveringsdato forklædt som teknik.'),
        ('Frigivelsen',
         'Hvem der må sige »den er klar«, og hvad der skal være på plads, før produktionen begynder — '
         'én frigivelse pr. ordre, med navn og dato, ikke en mail til alle.'),
        ('Ændringssedlen',
         'Hvad ændringen gør ved pris, tid og allerede indkøbte dele; i GMP var det change control '
         'med nummer og godkendelse, og samme disciplin gjaldt tillægsarbejdet i entreprisen.')]:
        m.bullet(label, body, after=16)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · entreprise og service',
         [('Leverancer, arbejdsmiljø og vækst',
           '**Udbud**, **indkøb** og **leverandører**; **APV** og **LOTO**; ansættelse, oplæring og '
           '**medarbejderudvikling** i egen virksomhed — otte ansatte og fuldt **P&L**.')]),
        ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen',
         'Data Power Consultant ApS · København · 2024–nov. 2026 (sideløbende med ELOHVAC)',
         '4–10 personer · tekniske og industrielle applikationer',
         [('Data i beslutninger',
           '**KPI**-modeller, **prioritering** og **opfølgning** til ledelsen; selskabet er ophørt.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('Konstruktion, ændring og aflevering',
           '**Kravspecifikation**, **kvalitetssikring**, **FAT/SAT**, **IQ/OQ/PQ** og change control; '
           '37 projekter med dokumentation og nul kritiske afvigelser ved aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter',
         [('Kapacitet, snitflader og montage',
           '**Kapacitetsmodel** opdateret hver morgen; **montage** koordineret med '
           '**underentreprenører** og leverandører, så 11 anlæg kunne bygges i samme tidsplan.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Biofos (Lynetten) · København · aug. 2017–jan. 2022',
         'Renseanlæg i 24/7-drift · pumper, højspændingstavler, SCADA',
         [('Drift, anlæg og energi',
           'Planlagt vedligehold og akut fejlfinding døgnet rundt; **over 40 % lavere energiforbrug** '
           'gennem måling og indregulering.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 teknikere · maskinværksted · maskiner og materiel',
         [('Værksted, maskiner og oplæring',
           'Fejlfinding, kalibrering og reparation af maskiner; indkøb og vedligehold af materiel; '
           '**oplæring** og opfølgning for 12 teknikere.')]),
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
    m.para('Dansk og engelsk, skriftligt og mundtligt · Persisk: modersmål · **IT**: **MS Office**, '
           '**Excel** til kalkule, kapacitet og **KPI**, **ERP**-arbejde med sags- og økonomidel, '
           'tegningslæsning og **stykkliste** i PDF/CAD-viewer, egne **Python**-værktøjer til '
           'planlægning · **Kørekort B og egen bil** · Flytter gerne for rollen · Kan starte efter '
           'aftale · Referencer på forespørgsel.', after=50)

    m.models_table('OPSLAGETS KRAV — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Lede og tage styring hver dag',
         'Daglig tavlestyring med fast **dagsorden**, beslutninger samme dag og en navngiven ejer på '
         'hver opgave; som ejer har jeg ledet 8 ansatte og taget pris-, bemandings- og '
         'leverancebeslutninger uden at vente på et møde.'),
        ('Sikre levering til tiden',
         'Datoen styret bagfra: hvilke tegninger og hvilke komponenter der skal være klar hvornår — 37 '
         'kapitalprojekter og 11 anlægsprojekter afleveret til aftalt dato.'),
        ('Udfordre løsningerne i stedet for bare at godkende dem',
         'Review med tre spørgsmål: kan den bygges, kan den købes, kan den serviceres; 11 anlæg '
         'gennemgået før montage og fejltilstande testet ved **FAT/SAT** i stedet for godkendt på '
         'papir.'),
        ('Fokus på at det der tegnes, også fungerer i produktionen',
         'Montagevenlighed prøvet på gulvet: 14 montører og 5 elektrikere har bygget efter det, jeg '
         'selv har specificeret, og akkord betyder, at en dårlig detalje koster penge samme dag.'),
        ('Fjerne flaskehalse og optimere workflow',
         '**Kapacitetsmodel** for 11 samtidige projekter og 14 medarbejdere, opdateret hver morgen; '
         'flaskehalsen flyttet fra montage til indkøb, fordi det var der, datoen blev bestemt.'),
        ('Skabe struktur, retning og overblik',
         'Én tavle, én liste og én status pr. uge; 37 projekter i samme struktur i GMP og 11 anlæg i '
         'samme struktur i entreprise — uden at nogen skulle spørge, hvor sagen stod.'),
        ('Opbygge et stærkt arbejdsmiljø, hvor teamet trives og performer',
         '**APV** og **LOTO** ført i egen virksomhed, sikker adfærd taget op på tavlemødet, og 3 '
         'lærlinge og 5 elektrikere fastholdt — arbejdsmiljø er noget, man gør, ikke noget, man '
         'skriver.'),
        ('Ansætte flere på sigt og sætte fremtidens hold',
         'Ansat og oplært medarbejdere i egen virksomhed siden 2023: jobprofil, samtaler, '
         '**oplæring** og de første 30 dage planlagt, før stillingen blev slået op.'),
        ('Samarbejde med salg og produktion om den mest lønsomme produktionsrækkefølge',
         'Rækkefølgen aftalt ugentligt med salg og værksted: hvad der giver færdigvare først, hvad der '
         'kan samles i samme opstilling, og hvad der skal vente — på tal, ikke på hvem der råbte '
         'højest.'),
        ('Reference direkte til COO',
         'Rapporteret til direktion og bestyrelse i egen virksomhed; **beslutningsoplæg** på én side '
         'med pris, risiko og anbefaling — beslutningen taget til mødet, ikke udskudt til næste.'),
        ('Teknisk baggrund som konstruktør, ingeniør eller projekteringsleder',
         '**Elautoriseret maskinmester (LV/MV/HV)** og B.Tech i teknologiledelse og maskinteknik, '
         '7,6/12; el- og maskinteknisk konstruktion i grunduddannelsen og 20+ år med at læse og '
         'udfordre tekniske løsninger.'),
        ('5-10 års erfaring fra tegnestue, teknisk afdeling eller projektering',
         '20+ år i tekniske projekter og projekteringens konsekvenser: kravspecifikation, **FAT/SAT**, '
         '**IQ/OQ/PQ**, 37 kapitalprojekter og 11 anlægsprojekter — i produktionsvirksomheder som Novo '
         'Nordisk og Biofos.'),
        ('Forstå produktionen og vide, hvad der virker i praksis',
         'Syv år i maskinværksted med 12 teknikere og fem år i 24/7-drift; **montage**, akkord og '
         'vedligehold har lært mig, hvad der holder på et gulv — og hvad der kun ser godt ud i en '
         'præsentation.'),
        ('Bidrage til et godt arbejdsmiljø med fokus på trivsel og performance',
         '**Trivsel** og sygefravær ført som en del af driften, ikke som en HR-sag; arbejdsmiljøet '
         'taget op samme dag, hvis en opgave var farlig eller urimelig at udføre.'),
        ('Tage beslutninger, skære igennem og skabe fremdrift',
         'Beslutning samme dag, når to løsninger stod lige: vælg den, der kan bygges først, og skriv '
         'ned hvorfor; omkostningen ved at vente er altid højere end omkostningen ved at vælge.'),
        ('Ikke være bange for at stille krav og motiveres af ansvar',
         'Krav stillet til leverandører, underentreprenører og egne folk — med dato og konsekvens; '
         'fuldt **P&L** og ansvar for otte medarbejdere siden 2023, inklusive de beslutninger der viste '
         'sig at være forkerte.'),
        ('Være grundig og have en god analytisk sans',
         'Talvejen før mavefornemmelsen: kalkule, timeforbrug og afvigelse regnet igennem, før en '
         'løsning blev valgt — 37 CAPEX-sager med begrundelse og efterkalkulation.'),
        ('Have positiv indstilling og godt humør',
         'Dagen starter med, at nogen griner på tavlemødet; i 24/7-drift var humøret det, der bar en '
         'nattevagt efter et havari igennem — og det smitter mere end en mail om, at det haster.'),
        ('Være handlingsorienteret, stærk og fremsynet med godt overblik',
         'Handlet, før beslutningen var formel, når anlægget stod stille; planlagt med tolv ugers '
         'leveringstid på kritiske komponenter indregnet fra første dag.'),
        ('Selvstændigt kunne prioritere og løse mange opgaver uden detaljeret beskrivelse',
         '11 samtidige projekter, 14 medarbejdere og tre interessenter pr. projekt — prioriteret hver '
         'morgen uden en plan, der fortalte, hvad der var vigtigst.'),
        ('Være engageret med god faglig forståelse',
         'Fagligt nysgerrig i praksis: **SCADA**, **PLC** og el-tavler læst selv, så en diskussion med '
         'en tekniker blev faglig i stedet for en bestilling — og en fejl blev fundet, før den blev en '
         'sag.'),
        ('Se mulighederne i samspillet mellem de forskellige grænseflader',
         'Grænseflader mellem el, ventilation og VVS koordineret i 20+ år; på Ventek-Air på tværs af 11 '
         'anlæg og på Novo Nordisk med rådgivere, bygherre og entreprenører omkring sig.'),
        ('Være aktiv og engageret i at udvikle kolleger og selv søge ny viden',
         '12 teknikere oplært, 3 lærlinge i egen virksomhed og 25 specialister rådgivet; selv taget '
         'B.Tech som voksen, elautorisation i 2023 og køle- og ventilationsteknik på AMU i 2021.'),
        ('Være fagligt stolt og pligtopfyldende',
         'Dokumentation afleveret komplet, også når ingen spurgte: nul kritiske afvigelser ved '
         'aflevering på 37 projekter er ikke held, men en vane — og et valg om at gøre det færdigt.'),
    ])

    m.section('DE FØRSTE 90 DAGE')
    for b in (
        'Uge 1–2: siddet med i salgsmøder og på værkstedet og set, hvor ordren bliver til en dato, og '
        'hvor datoen bliver til en tegning — uden at ændre noget endnu.',
        'Uge 3–6: kortlagt de fem køer med tid og ejer pr. ordre; fundet de to flaskehalse, der koster '
        'mest, og skrevet dem ned med tal.',
        'Måned 2–3: tavle og ugestatus indført, så teknik, salg og værksted ser samme dato; review '
        'indført ved frigivelse, ikke ved klage.',
        'Måned 3: plan for de næste ansættelser og en oplæringsvej for de 8-10 medarbejdere, der '
        'allerede er der — så væksten ikke bliver et tempo, nogen falder af.',
        'Løbende: månedlig gennemgang med salg og produktion af, hvad der blev lovet, hvad der blev '
        'leveret, og hvad der kostede — tre tal, samme side, hver måned.'):
        m.bullet('', b, after=16)

    m.models_table('SÅDAN VILLE JEG MÅLE ROLLEN', ('Mål', 'Sådan aflæses det'), [
        ('Levering til tiden',
         'Andel ordrer afleveret på den dato, salget gav kunden — ikke den dato, teknikken fik ordren; '
         'forskellen mellem de to datoer er rollens egentlige problem.'),
        ('Gennemløbstid pr. ordre',
         'Dage fra ordre til frigivet tegning og fra frigivelse til produktion; køerne bliver kortere, '
         'når de bliver målt hver uge.'),
        ('Ændringer efter frigivelse',
         'Antal og kostpris pr. ordre, hver med en årsag fra listen — ikke forklaret med, at kunden '
         'ændrede sig.'),
        ('Belastning i afdelingen',
         'Ordrer i gang pr. medarbejder og overarbejdstimer pr. måned; den tidlige indikator på, at '
         'der skal ansættes, før nogen siger det.'),
        ('Trivsel og performance',
         'Sygefravær og trivselsmåling læst sammen med leveringen, så de ikke bliver to forskellige '
         'historier om den samme afdeling.')])

    m.section('DET VILLE JEG SPØRGE OM')
    for b in (
        'Hvor mange ordrer er i gang samtidig, og hvor mange af dem er lovet en dato, der allerede er '
        'presset?',
        'Hvor stopper en ordre i dag — i salget, i tegningen, i indkøbet eller på værkstedet?',
        'Er der en frigivelsesproces i dag, eller afhænger det af, hvem der spørger?'):
        m.bullet('', b, after=16)

    m.para('**Jeg kommer gerne til Trekantområdet** og ser afdelingen og produktionen, før vi taler om '
           'rollen — og jeg flytter gerne for at være der i hverdagen. Ansøgningen er sendt gennem '
           'erwin andersen a/s under stillingsnummer **02.11.88**. Kontakt: +45 93 99 95 14 · '
           'ajlooshahram@gmail.com.', after=24)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Anonym_TekniskChef.docx')
    build(out)
    print(out)
