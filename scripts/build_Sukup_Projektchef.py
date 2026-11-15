# -*- coding: utf-8 -*-
"""Sukup Europe A/S (Hedensted) — Projektchef, rekruttering via HumanTrust.

Form (master/FORMKATALOG.md): åbning **B** (negationen: det er ikke montagen,
der vælter et kundeprojekt — det er tilbuddet og kalenderen), struktur
**Kontrakten, kalenderen, kassen og folkene**, register **Anlægget** (nyt:
silo, tørrer, transportør, kapacitet, høst, montage, idriftsættelse).
Kulturfil: jd/Sukup_Projektchef_kultur.txt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Projektchef · kundeprojekter, projektøkonomi og ledelse'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('13. november 2026')
    m.meta('Sukup Europe A/S · Hedensted · via HumanTrust')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Projektchef', bold=True, color='1A1A1A')

    def lp(text, after=60):
        return m.para(text, after=after, line=236)

    # ---------------------------------------------------------------- side 1
    lp('**Et kundeprojekt hos Sukup går sjældent galt på montagen.** Montagen er synlig, og '
       'montørerne er faglærte. Projektet går galt seks måneder før: i tilbuddet, hvor kapaciteten '
       'blev regnet på en tørretid og ikke på en høst, og i kalenderen, hvor montagen blev lagt før '
       'byggetilladelsen var givet og før kunden havde besluttet, om der skulle være et siloanlæg '
       'mere. Derfor handler projektchefrollen her om tre ting, der ligger før og omkring '
       'montagen — og om de mennesker, der sidder med dem.', after=56)

    lp('**Sukup Europe udvikler, sælger, projekterer, leverer og monterer løsninger til håndtering, '
       'tørring og opbevaring af korn og andre landbrugsafgrøder** — **»specialister i tørring, '
       'opbevaring og håndtering«**, med **»rødder helt tilbage til 1955«**, DanCorn indtil 2015 og i '
       'dag en del af Sukup-koncernen med produktion i USA og Ukraine. I er **»en af Europas førende '
       'aktører«** med kunder og projekter over hele kontinentet, 60 medarbejdere og hovedkvarteret i '
       'Hedensted. Rollen har **»samlet ledelses-, ressource- og resultatansvar for seks '
       'projektledere«**, en plads i ledergruppen og reference til Jens Erik Iversen, der **»altid '
       'sætter mennesket først og samtidig har klare forventninger«** — det er præcis den '
       'kombination, jeg selv leder efter.', after=56)

    lp('**Kontrakten, kalenderen, kassen og folkene.**', after=46)

    lp('**Kontrakten.** En kontrakt er ikke et dokument, man underskriver; det er en fordeling af '
       'risiko, og den bliver dyr, når sælgeren har lovet noget, projektlederen skal indfri. Jeg har '
       'siddet på begge sider — som leverandør med fast pris og garantiansvar og som bygherresidens i '
       'en GMP-fabrik — og ved, hvilke klausuler der koster penge, når **»stærk kommerciel '
       'forståelse«** skal bruges i praksis i **»tilbuds- og kontraktfasen«**. Derfor sidder jeg med '
       'i tilbuddet, før det bliver sendt.', after=40)

    lp('**Kalenderen.** Seks projektledere, montagekapacitet og et Europa, hvor høsten ikke flytter '
       'sig. **Kapacitets- og ressourceplanlægning på tværs af projektporteføljen** er en model og et '
       'ugentligt møde: hvad der er booket, hvad der er bundet af montører og lastbiler, og hvad der '
       'skal rykkes, når en kunde ringer. I 2022 styrede jeg 11 samtidige anlægsprojekter og 14 '
       'medarbejdere på **kapacitetsmodel** — det er samme regnestykke, blot med korn i stedet for '
       'kanaler.', after=40)

    lp('**Kassen.** **»Rettidig og lønsom gennemførelse af kundeprojekter«** afgøres af '
       'efterkalkulationen, ikke af mavefornemmelsen: avance pr. projekt hver måned, ændringer og '
       '**ændringsordrer** dokumenteret, før de bliver udført, og en risikoliste med navn og '
       'modtræk. Jeg har drevet fuldt **P&L** i egen virksomhed siden 2023 og 37 kapitalprojekter '
       'med rådighedsbeløb — jeg kan læse et projekt på samme måde som et regnskab.', after=40)

    lp('**Folkene.** Seks projektledere skal have en ramme, ikke en instruks: en skreven '
       '**forventningsaftale** med resultat, mandat og eskaleringsgrænse, sparring på den svære sag og '
       'opfølgning på resultat. Jeg har ledet 25 specialister, 14 medarbejdere i 11 samtidige '
       'projekter og 8 ansatte i egen virksomhed, og det, der skaber **»skabe følgeskab og gode relationer '
       'på tværs af fagligheder«**, er, at folk ved, hvad de må beslutte — og at lederen tager den '
       'ubehagelige samtale selv.', after=56)

    lp('**Processer og værktøjer** er ikke et projekt ved siden af driften, men den måde, afdelingen '
       'bliver bedre på: én arbejdsgang pr. proces, prøvekørt på et projekt og målt, før den bliver '
       'standard. Det er **Project Governance** i praksis og **»løbende forbedringer«** med en ejer — '
       'ikke en mappe. I ledergruppen vil jeg bidrage med det, jeg er sikker på: hvordan en '
       'projektorganisation skalerer fra seks projektledere og op, uden at kvaliteten falder, mens '
       '**»en sund og profitabel virksomhed«** bliver ved med at vokse.', after=56)

    lp('**Det, jeg ikke har, står her.** Jeg har ikke solgt korntørringsanlæg og ikke ledet en '
       'projektafdeling i landbrugsindustrien. Jeg har leveret og monteret tekniske anlæg i 20+ år, '
       'ledet 37 kapitalprojekter i en reguleret fabrik og stået med **projektøkonomi**, '
       '**kontrakter** og **risikostyring** som dagligt ansvar — og jeg er **elautoriseret maskinmester (LV/MV/HV)** med '
       'B.Tech i teknologiledelse, altså den tekniske uddannelse, opslaget efterspørger. '
       'Landbrugsdelen lærer jeg af jeres projektledere og af kunderne; metoden tager jeg med.', after=56)

    lp('**Jeres eget sprog er grunden til, at jeg søger.** I beskriver en virksomhed, hvor '
       '**»familieejerskabet gør, at vi kan træffe hurtige beslutninger«**, hvor **»den uformelle tone '
       'og de stærke rødder i landbruget«** stadig præger hverdagen, og hvor **»frihed og fleksibilitet '
       'går hånd i hånd med en forventning om, at alle tager ansvar og bidrager«**. I efterspørger en '
       'leder med **»en naturlig evne til at skabe struktur og overblik«**, som **»møder du dem med ro og '
       'handlekraft«** og kan **»følge tingene til dørs«**, og som vil være med til at **»sætte '
       'retningen for fremtidens projektorganisation«**. Det er den slags ledelse, jeg selv er blevet '
       'ledet af — og den, jeg prøver at udøve.', after=56)

    lp('**Praktisk:** jeg bor i Måløv i dag, og hovedkontoret ligger i Hedensted. Jeg er indstillet på '
       'at flytte for rollen, så jeg er på plads på hovedsædet hver dag — og de 10-30 rejsedage om '
       'året passer mig fint. Dansk og engelsk, skriftligt og mundtligt, og jeg kan starte efter '
       'aftale.', after=24)

    m.meta('Med venlig hilsen', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('**Teknisk projektleder og leder med fuldt resultatansvar** — **elautoriseret '
           'maskinmester (LV/MV/HV)**, B.Tech i teknologiledelse og maskinteknisk teknik. 20+ år med '
           'tekniske anlæg, **37 kapitalprojekter** i en GMP-fabrik, **11 samtidige anlægsprojekter** '
           'med 14 medarbejdere og 25 specialister. Arbejder med **projektøkonomi**, '
           '**kapacitetsplanlægning**, **kontrakter** og **risikostyring** — og med at få seks '
           'projektledere til at trække samme vej.', after=70)

    m.section('ANLÆGGET — FRA TILBUD TIL AFLEVERING')
    for label, body in [
        ('Tilbuddet og kontrakten',
         '**Kontrakt** og tilbud gennemgået med sælger og projektleder, før det blev sendt: '
         '**risici**, **ændringsordrer** og grænseflader skrevet ind — 37 CAPEX-sager med '
         'rådighedsbeløb og fast pris i egen virksomhed.'),
        ('Kapaciteten og kalenderen',
         '**Kapacitetsplanlægning** på tavle og i model hver uge: montører, underentreprenører og '
         'materialer mod aftalt dato — 11 samtidige projekter og 14 medarbejdere i 2022.'),
        ('Økonomien og marginen',
         '**Efterkalkulation** pr. projekt hver måned, **projektmarginer** fulgt fra tilbud til '
         'aflevering, og en risikoliste med navn og modtræk; fuldt **P&L** i egen virksomhed siden '
         '2023.'),
        ('Montagen og idriftsættelsen',
         '**Silo**, **tørrer**, **transportør**, **montage**, **idriftsættelse** og **aflevering** med protokol, oplæring af driften og '
         'garantiperiode — samme model som **FAT/SAT** og **IQ/OQ/PQ** i pharma, blot med korn, '
         'transportører og tørrere.'),
        ('Projektlederne',
         'Seks eller flere ledere i samme ramme: **forventningsaftale** med mandat og '
         'eskaleringsgrænse, **faglig sparring** hver anden uge og opfølgning på resultat — 25 '
         'specialister, 14 medarbejdere og 8 ansatte gennem årene.')]:
        m.bullet(label, body, after=16)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · service og entreprise',
         [('Projekter, økonomi og kontrakter',
           'Tilbud, **kontrakter** og materialer; projekter leveret med egenkontrol og '
           'afleveringsprotokol; **arbejdsmiljø** med APV, LOTO og sikkerhedsrundering.')]),
        ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen',
         'Data Power Consultant ApS · København · 2024–nov. 2026 (sideløbende med ELOHVAC)',
         '4–10 personer · tekniske og industrielle applikationer',
         [('Data i beslutninger',
           'Tekniske applikationer samt **AI** i ledelsesarbejdet — rapportering, beslutningsoplæg '
           'og **KPI**-analyse; selskabet er ophørt.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('Krav, afvigelser og aflevering',
           'Kravspecifikation, **FAT/SAT** og **IQ/OQ/PQ**; dokumentation bygget undervejs og nul '
           'kritiske afvigelser ved aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter',
         [('Fremdrift, kapacitet og leverandører',
           'Dagligt tavlemøde, **kapacitetsplanlægning** og omprioritering samme dag; leverancer '
           'styret mod aftalt dato med underentreprenører og materialer.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Biofos (Lynetten) · København · aug. 2017–jan. 2022',
         'Renseanlæg i 24/7-drift · pumper, højspændingstavler, SCADA',
         [('Drift, anlæg og energi',
           'Planlagt vedligehold og akut fejlfinding døgnet rundt; **over 40 % lavere energiforbrug** '
           'gennem måling og indregulering.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 teknikere · maskinværksted · maskiner og materiel',
         [('Maskiner, materiel og oplæring',
           'Fejlfinding, kalibrering og reparation af maskiner; indkøb og vedligehold af materiel; '
           'oplæring og opfølgning for 12 teknikere.')]),
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
    m.para('Dansk og engelsk, skriftligt og mundtligt · Persisk: modersmål · **IT**: **MS Office** og '
           'Excel-modeller, **ERP**-arbejde (bl.a. sags- og økonomisystemer i egen virksomhed), '
           '**NAV**-lignende ERP-platforme, **SketchUp** og Plantegning i forbindelse med '
           'projektering, samt egne **Python**-værktøjer til **KPI** og **projektøkonomi** · '
           '**Kørekort B og egen bil** · Indstillet på at flytte til Hedensted-området · Kan starte '
           'efter aftale · Referencer på forespørgsel.', after=50)

    m.models_table('OPSLAGETS KRAV — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Lede, motivere og udvikle projekthåndteringsprocessen og projektteamet',
         'Projektmodel indført og drevet i tre organisationer: **forventningsaftale** pr. leder, '
         '**faglig sparring** hver anden uge og en proces pr. år der blev prøvekørt og målt — 25 '
         'specialister, 14 medarbejdere og 8 ansatte med **fantastiske medarbejdere** i alle tre '
         'miljøer.'),
        ('Sikre rettidig og lønsom gennemførelse af kundeprojekter',
         '37 kapitalprojekter leveret til tid og med **nul kritiske afvigelser**; 11 anlægsprojekter '
         'med aftalt dato holdt i 2022 og projekter i egen virksomhed med fast pris og garanti.'),
        ('Drive kapacitets- og ressourceplanlægning på tværs af projektporteføljen',
         '**Kapacitetsmodel** og ugentligt tavlemøde med omprioritering samme dag; 14 medarbejdere og '
         'underentreprenører fordelt på 11 samtidige projekter uden at flytte aftalte datoer.'),
        ('Sikre optimal projektøkonomi, forbedre projektmarginer og håndtere projektrelaterede risici',
         '**Efterkalkulation** hver måned, **projektmarginer** fulgt fra tilbud til aflevering og en '
         'risikoliste med ejer; fuldt **P&L** siden 2023 og 37 CAPEX-sager med rådighedsbeløb.'),
        ('Styrke samarbejdet mellem salg, projektledelse, montage og service',
         'Siddet i grænsefladen mellem salg, projektering og montage i 20+ år — som leverandør og som '
         'bygherre; uenighed blev skrevet ned som en beslutning med ejer og dato.'),
        ('Understøtte salgsprocessen i tilbuds- og kontraktfasen',
         'Gennemgået tilbud og **kontrakter** med sælger i **tilbudsfasen**, før de blev sendt: '
         'risiko, **ændringsordrer** og grænseflader skrevet ind — med blik for **den mest optimale '
         'løsning for den enkelte kunde** og fast pris samt garantiansvar i egen virksomhed.'),
        ('Videreudvikle afdelingens processer og værktøjer med fokus på løbende forbedringer',
         '**Metodebog** med én arbejdsgang pr. proces, prøvekørt og målt, før den blev standard; '
         '**5S** og standard work indført i værksted og på anlæg; ledelsesrapportering bygget fra '
         'bunden.'),
        ('Bidrage til virksomhedens strategiske udvikling i ledergruppen',
         'Ledelsesarbejde med fuldt **P&L** og strategiske vejvalg som ejer og teknisk direktør siden '
         '2023, og som medlem af en **ledergruppe** som teknisk ansvarlig i en vækstvirksomhed med '
         '4-10 personer.'),
        ('Samlet ledelses-, ressource- og resultatansvar for seks projektledere',
         'Ledererfaring siden 2003: 12 teknikere, 14 medarbejdere i 11 projekter, 25 specialister og '
         '8 ansatte — med ressource- og resultatansvar, ikke kun fagligt ansvar.'),
        ('Solid erfaring inden for projektledelse',
         '20+ år med tekniske projekter: 37 kapitalprojekter i GMP, 11 samtidige anlægsprojekter, '
         'projekter med fast pris og garanti i egen virksomhed og **projektportefølje** styret på én '
         'side pr. projekt.'),
        ('Erfaring fra bygge- og entreprisebranchen eller procesanlæg',
         '**Byggeprojekter** og entrepriseopgaver i egen virksomhed siden 2023 og procesanlæg i fem '
         'år: renseanlæg i 24/7-drift med pumper, transportører, højspændingstavler og **SCADA**.'),
        ('Erfaring med projekter indeholdende byggeri og teknik',
         'Byggeri og teknik i samme projekt: el, **VVS**, **ventilation**, **CTS**/**BMS** og '
         'bærende konstruktioner koordineret med montage — 37 projekter i en fabrik, der kørte '
         'videre.'),
        ('Teknisk uddannelse som konstruktør, ingeniør eller maskinmester',
         '**Elautoriseret maskinmester (LV/MV/HV)** og **B.Tech** i teknologiledelse og '
         'maskinteknik (7,6/12) — maskinmesterretningen, som opslaget efterspørger.'),
        ('Mindst tre års erfaring med personaleledelse',
         '20+ år med personaleledelse: 12 teknikere fra 2003, 14 medarbejdere i 2022, 25 specialister '
         'i 2023-2024 og 8 ansatte i egen virksomhed.'),
        ('Skabe struktur og overblik, når projekterne trækker i forskellige retninger',
         'Én side pr. projekt med økonomi, næste beslutning og tre risici, og et ugentligt møde hvor '
         'det røde blev besluttet samme dag — prøvet på 11 samtidige projekter.'),
        ('Analytisk tilgang og stærk kommerciel forståelse i kontrakter, projektøkonomi og risikostyring',
         '**Kontrakter**, **projektøkonomi** og **risikostyring** som dagligt ansvar i egen '
         'virksomhed og i 37 CAPEX-sager; beslutningsoplæg på to sider med tre alternativer og en '
         'anbefaling.'),
        ('Erfaring med LEAN, Project Governance eller lignende metoder',
         '**LEAN**, **5S** og standard work indført i værksted og på anlæg; stage-gate og '
         'beslutningspunkter brugt i pharma-projekter, hvor ingen fase måtte starte uden godkendelse.'),
        ('Synlig, tillidsvækkende og tydelig leder, der skaber følgeskab',
         'Daglig tilstedeværelse på gulvet, tavlemøde klokken 7 og en skreven ramme for mandat — '
         'medarbejdere har arbejdet selvstændigt under den ramme i 20+ år.'),
        ('Møde udfordringer med ro og handlekraft og følge tingene til dørs',
         'Akut fejlfinding om natten i fem år og afvigelser lukket før overlevering på 37 projekter; '
         'det, der blev besluttet, blev fulgt op til dato — også når svaret var nej.'),
        ('Beherske dansk og engelsk',
         'Dansk og engelsk, skriftligt og mundtligt, i 20+ år med danske og internationale '
         'leverandører, kunder og myndigheder; persisk som modersmål.'),
        ('Fortrolig med MS Office og ERP-systemer, gerne NAV, samt tegneprogrammer som Google SketchUp',
         '**MS Office**, **ERP** (sags-, økonomi- og lagerdel i egen virksomhed), **NAV**-lignende '
         'platforme i 5 år, **SketchUp** og plantegninger i projekteringen samt egne 12 '
         'Python-værktøjer til KPI.'),
        ('Daglig arbejdsplads i Hedensted med 10-30 rejsedage om året',
         'Bor i Måløv i dag og flytter gerne for rollen, så hverdagen er i Hedensted — med '
         '**forståelse for, at familie og arbejdsliv skal hænge sammen**; de 10-30 rejsedage til '
         'kunder og montage i Europa ser jeg som en del af jobbet.'),
    ])

    m.section('DE FØRSTE 90 DAGE')
    for b in (
        'Siddet med på tilbuds- og kontraktgennemgang med salg og set, hvor margenen forsvinder i dag '
        '— og hvad der kan skrives ind i tilbuddet i stedet.',
        'Gået porteføljen igennem projekt for projekt med de seks projektledere: økonomi, næste '
        'milepæl, de tre risici og den beslutning, der mangler.',
        'Sat kapacitetsmodellen op for montage og rejseaktivitet og aftalt en fast ugentlig kadence '
        'med salg, montage og service.',
        'Aftalt med ledergruppen, hvilke to processer der skal forbedres først — og hvad der skal '
        'måles på dem, før de bliver standard.'):
        m.bullet('', b, after=16)

    m.section('DET VILLE JEG SPØRGE OM')
    for b in (
        'Hvor mange projekter har den enkelte projektleder i porteføljen i dag, og hvor mange af dem '
        'er i montage samtidigt?',
        'Hvordan måles projektmargin i dag — ved aflevering eller løbende — og hvem ejer '
        'efterkalkulationen?',
        'Hvilke dele af projektmodellen er skrevet ned, og hvor er de største spring i overleveringen '
        'mellem salg, projektering og montage?'):
        m.bullet('', b, after=16)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Sukup_Projektchef.docx')
    build(out)
    print(out)
