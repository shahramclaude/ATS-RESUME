# -*- coding: utf-8 -*-
"""Vedligeholdelsestekniker til Drug Substance — FUJIFILM Biotechnologies, Hillerød (R0012721, dansk opslag).

Dansk opslag -> dansk dokument, 4 sider i masterdesign: brev side 1, CV side 2-3, kravmatrix side 4.
Intet kontaktnavn i opslaget; brevet er adresseret til rekrutteringsteamet.

STILVALG (style_guard godkendt, 3/3 skift mod #415):
  register     = Sammenhold og humor (sammenhold · humor · hjælpsomhed · spiller hinanden gode ·
                 ét team · plads til humor) — holdets eget sprog fra opslaget
  åbningsgreb  = AQ (de tre hensyn i samme time: stabil drift, høj kvalitet og sikkerhed i det
                 højteknologiske GMP-setup — opslagens egen trekant som det operative spørgsmål)
  struktur     = Upstream og Downstream (fabrikkens egen retning: følge processen gennem de to
                 halvdele)

BRUGERENS KORREKTION + permanent regel: alt tekst humaniseret, menneskeskrevet tone i brev OG CV.
BANNED: "dynamisk" (JD: "Et dynamisk og professionelt arbejdsmiljø") og "den rette kandidat" og
"passion" (EN-tekst) citeres ALDRIG.

EVIDENSGRÆNSER (brugerbekræftelse 25.11.2026, master §1): bio-udstyr er fra Novo-commissioning:
CIP/SIP-anlæg, tanke, procesrør og instrumentering (idriftsat/testet under GMP). Bioreaktorer,
filtrering og kromatografi er IKKE serviceret — skrives ærligt (opslaget: "en fordel, men ikke et
krav"). Elautoriseret maskinmester, ikke flymekaniker/smed — "anden relevant teknisk uddannelse".
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Drug Substance · Vedligeholdelsestekniker'
BANNER_RESUME = 'Vedligehold, GMP og procesanlæg · Drug Substance'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('25. november 2026')
    m.meta('FUJIFILM Biotechnologies, Hillerød · Vedligeholdelsestekniker til Drug Substance')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Vedligeholdelsestekniker til Drug Substance', bold=True, color='1A1A1A')
    m.para('Kære rekrutteringsteam hos FUJIFILM Biotechnologies,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('Stabil drift, høj kvalitet og sikkerhed i et højteknologisk GMP-setup. De tre ting på '
       'én gang, og de kan ikke altid fås samtidig: det udstyr, produktionen venter på, den '
       'dokumentation, kvaliteten kræver, og den sikkerhed, EHS holder øje med. '
       'Vedligeholdelsesteknikerens dag i Drug Substance ligger i det krydsfelt. Næsten fem '
       'års 24/7-drift på et renseanlæg og to års GMP-projekter på Novo Nordisk i medicinal- '
       'og procesindustrien har lært mig '
       'at stå i det uden at droppe nogen af de tre.')

    lp("Opgaven står der lige ud: 'drift, vedligehold og overvågning af vores produktionsudstyr "
       "i Drug Substance', på tværs af Upstream og Downstream. Det passer mig at følge "
       'anlægget hele vejen. Planlægning og udførelse af forebyggende og korrigerende '
       'vedligehold på procesanlæg og udstyr. Fejlfinding der løber over fagene: mekanik, '
       'instrumentering i samme sag. Og så det, der adskiller en GMP-fabrik fra de fleste '
       'andre steder: Nøjagtig dokumentation af alt udført arbejde og efterlevelse af '
       'procedurer, også når produktionen står og tripper.')

    lp('Min vej ind i faget går forbi procesmiljøerne. Under commissioning på Novo Nordisk '
       'arbejdede jeg med biofarmaceutisk udstyr: CIP/SIP-anlæg, tanke, procesrør og '
       'instrumentering, der blev idriftsat og testet efter protokol under GMP. Før det '
       'pumper, ventiler, HVAC, HV-tavler, SCADA og PLC i drift og vedligehold på Biofos, og '
       'fejlfinding på el, styring og automatik som el-tekniker. EHS-delen kender jeg fra '
       'byggeplads og drift: LOTO, APV, risikovurdering og opfølgning på nærved-hændelser.')

    lp("To ting skal jeg sige ligeud, før I læser videre. Som I skriver: "
       "'flymekaniker, automatiktekniker, industritekniker, smed eller tilsvarende' er jeg "
       'ikke. Jeg er elautoriseret maskinmester med B.Tech i maskinteknik, og det er en anden '
       'relevant teknisk uddannelse med vedligeholdserfaring. Og udstyrslisten '
       "'CIP/SIP, bioreaktorer, pumper, ventiler, sensorer, filtrering eller kromatografi' har "
       'jeg en blandet pose af: CIP/SIP, tanke, procesrør og instrumentering fra commissioning, '
       'pumper, ventiler og sensorer fra driftssiden, men bioreaktorer og kromatografi har jeg '
       'ikke serviceret endnu. Dem skal jeg lære hos jer.')

    lp("Kulturen i opslaget gør også en forskel. 'Sammenhold, humor og hjælpsomhed vægtes "
       "højt', står der, og det er ikke en selvfølge i et vedligeholdsteam med skarpe "
       'deadlines. Jeg trives både selvstændigt og i teams og kan træffe velbegrundede '
       'beslutninger alene på en runde, og jeg kommunikerer klart og konstruktivt på tværs af '
       'faggrupper og niveauer, når sagen skal løses på tværs. En proaktiv tilgang til '
       'vedligehold og høj kvalitetsbevidsthed har været mit arbejdsgrundlag i fire år i '
       'GMP-regi og på et renseanlæg, hvor en glemt ventil bliver til et udkald. Jeg er '
       'omstillingsparat og motiveres af forandringer og vækstprojekter, og en sund og røgfri '
       'arbejdsplads med gode kollegaer og plads til humor passer også mig.')

    lp('En global CDMO med anlæg i Danmark, UK og USA. Det, jeg søger, er moderne '
       'produktionsudstyr i et stærkt sikkerheds- og kvalitetsmiljø '
       'og at kunne påvirke din hverdag og udvikling, som I skriver. Primært daghold '
       'passer mig, og en Aftenvagt/tilkald ca. hver 6.–8. uge har jeg rytme i efter år med '
       'skiftehold og vagtordning på Biofos.')

    lp('De første 90 dage står som en plan side 3 i CV\'et, ikke som løfter. Kort sagt: de '
       'første 30 dage lærer jeg anlægget at kende i begge retninger, opstrøm og nedstrøm, '
       'og målet er at kunne tage en runde selv. Dag 31-60 tager jeg opgaverne og får '
       'dokumentationen i et system, jeg kan stå inde for. Dag 61-90 står på optimering og '
       'tæt sparring og support til Produktion, Engineering og EHS. Gode dansk- og '
       'engelskkundskaber i skrift og tale har jeg, og jeg kan tiltræde hurtigst muligt efter '
       'aftale. Ring eller skriv endelig, hvis der er noget, I vil have uddybet.', after=44)

    lp('Med venlig hilsen', after=8)
    lp('Shahram Ajloo', after=8)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Vedligeholdelsestekniker med procesanlæg og GMP i hænderne. Commissioning af '
           'biofarmaceutisk udstyr på Novo Nordisk (CIP/SIP-anlæg, tanke, procesrør og '
           'instrumentering) under GMP/FDA/EMA, næsten fem års 24/7-drift og vedligehold på '
           'renseanlæg med pumper, ventiler, HVAC, HV-tavler, SCADA og PLC, og el-teknisk '
           'fejlfinding hen over mekanik, automatik og instrumentering som elautoriseret '
           'maskinmester. Rutineret IT-bruger: SAP, CMMS, Power BI, Python og Claude til '
           'dokumentation og opfølgning.', after=32)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester (el-teknik og ventilation)',
         'Data Power Consultant ApS · København · 2024 – nu',
         'AI-afdeling 4-10 personer · el-service og entreprise · 5 elektrikere + 3 lærlinge',
         [('', 'Leder AI-afdelingen med 4 til 10 personer: tilbud, kunder, og hvordan løsninger '
               'bliver bygget og dokumenteret. Investeringstilbud og månedlig KPI-opfølgning.'),
          ('', 'El-service og entreprise for erhvervskunder: installation, tavler, styring, '
               'fejlfinding og forebyggende vedligehold på el, ventilation og klima. UPS, '
               'fiber, PDS og adgangskontrol hører med.')]),
        ('Ejer / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 – nov. 2026 (virksomheden lukket)',
         'Erhvervskunder · el, ventilation og klima · entreprise · fuldt P&L',
         [('', 'Forebyggende og korrigerende vedligehold fra akutte udkald til afleveret anlæg: '
               'installation, tavler, styring og fejlfinding på el, ventilation og klima.'),
          ('', 'Tilbud, planlægning, underentreprenører, KS, dokumentation og aflevering med '
               'fuldt P&L-ansvar. Personaleledelse af 5 elektrikere og 3 lærlinge med 1:1, '
               'MUS og struktureret oplæring.')]),
        ('Senior commissioningeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, DKK 2-10 mio. · 25 specialister · GMP/FDA/EMA',
         [('', 'Commissioning og projektledelse på 37 CAPEX-projekter, DKK 2-10 mio. pr. stk. '
               'Biofarmaceutisk procesudstyr: CIP/SIP-anlæg, tanke, procesrør og instrumentering, '
               'idriftsat og testet efter FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA. Nul kritiske '
               'fund ved afleveringen.'),
          ('', 'Månedsrapport til ledelse og kunde om fremdrift, økonomi, risici og ressourcer. '
               '25 specialister på tværs af engineering, indkøb og drift. SAP ERP.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022 – nov. 2022',
         '11 samtidige projekter · 14 mand · DKK 2-10 mio.',
         [('', '11 samtidige projekter og et team på 14 mand. Daglige tavler for kapacitet og '
               'fremdrift. Sikkerhedsdokumentation og afleveringspakker i hvert projekt.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · SCADA, PLC, HV-tavler · skiftehold',
         [('', 'Vedligehold og drift af pumper, ventiler, HVAC, HV-tavler, SCADA og PLC døgnet '
               'rundt. Planlagt og korrigerende vedligehold, fejlfinding, og 5S og Standard '
               'Work i værkstedet.'),
          ('', 'Skiftehold med LOTO, APV, risikovurdering og nærved-hændelser, og vagtordning '
               'med tilkald. Opgaverne blev løst på tværs af holdene, også klokken tre om '
               'natten.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('', 'Ledelse af 12 mekanikere og teknikere i maskinværksted: vagtplan, materialer og '
               'mål. Fejlfinding på industrielt udstyr, analyse af rodårsag og korrigerende '
               'handlinger.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('UDDANNELSE OG CERTIFIKATER')
    m.edu('B.Tech (EQF6), teknologiledelse og maskinteknik',
          'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12')
    m.edu('Dansk elautorisation LV/MV/HV som elautoriseret maskinmester',
          'Sikkerhedsstyrelsen · maj 2023')
    m.edu('El- og maskinteknisk design, elteknik (EQF6)',
          'Tehran Technical University · 2000–2003')
    m.edu('PRINCE2, certificeret projektleder', 'AXELOS / PeopleCert')
    m.edu('Køleteknik og klimaanlæg (AMU)',
          'Mercantec · 2021 · STCW 2021–2023, Søfartsstyrelsen')
    m.para('Lean- og Six Sigma-praksis uden certifikat: DMAIC, 5S, PDCA, VSM, A3, Kaizen, '
           'Standard Work, SMED, TPM, 5xHvorfor, Ishikawa og FMEA, brugt i dokumenteret arbejde '
           'med vedligehold, kvalitet og planlægning.', after=48)

    m.section('SPROG, VÆRKTØJER OG PRAKTISK')
    m.para('Dansk (modersmål) · engelsk (professionelt, skrift og tale) · persisk (modersmål). '
           'Rutineret IT-bruger: SAP ERP, CMMS-systemer (fx SAP/Maximo), Power BI, Excel, '
           'Python og Claude til dokumentation og opfølgning. Kørekort B. Bor i Måløv; '
           'Hillerød er en overkommelig tur. Kan tiltræde hurtigst muligt efter aftale, også '
           'med vagtordning og aftenvagt.', after=48)

    m.section('KOMPETENCER')
    for label, body in [
        ('Vedligehold og fejlfinding',
         'Forebyggende og korrigerende vedligehold på procesanlæg og udstyr, og fejlfinding '
         'når en sag rører mekanik, automatik og instrumentering på én gang.'),
        ('GMP og dokumentation',
         'Nøjagtig dokumentation af alt udført arbejde og efterlevelse af procedurer. '
         'Protokoller skrevet før arbejdet, aflevering med nul kritiske fund på 37 projekter.'),
        ('Bio- og procesudstyr',
         'CIP/SIP-anlæg, tanke, procesrør og instrumentering fra commissioning. Pumper, ventiler '
         'og sensorer fra driftssiden. Bioreaktorer og kromatografi: set i projekter, ikke '
         'serviceret endnu.'),
        ('Sprog og dokumentation',
         'GMP-dokumentation på engelsk, rapporter på dansk og engelsk. Ingen opgave er lukket, '
         'før journalen er skrevet færdig.'),
        ('EHS og sikkerhed',
         'LOTO, APV, risikovurdering og nærved-hændelser. Identificere, implementere og følge '
         'op på sikre løsninger og forbedringer.'),
    ]:
        m.bullet(label, body, after=10)

    m.section('DE FØRSTE 90 DAGE')
    m.para('En plan for de første 90 dage, som I kan holde mig op på:', after=12)
    for b in [
        'Dag 1-30: Lære anlægget at kende i begge retninger, Upstream og Downstream. Gå med på '
        'runderinger, læse procedurerne for kritisk udstyr og lære CMMS hos jer. Målet er at '
        'kunne tage en runde selv efter de 30 dage.',
        'Dag 31-60: Selvstændige opgaver i planlagt og korrigerende vedligehold. '
        'Dokumentationen på plads efter hver opgave, og et forslag til standardisering af det '
        'tilbagevendende vedligehold, målt på antal planlagte opgaver pr. uge.',
        'Dag 61-90: Løbende forbedringer og optimering. Tæt sparring og support til Produktion, '
        'Engineering og EHS, og en første vurdering af, hvor anlægget taber mest tid i '
        'vedligeholdsprocesserne.',
    ]:
        m.bullet('', b, after=10)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('FUJIFILM Biotechnologies · Vedligeholdelsestekniker · Drug Substance (R0012721)',
                   ('Krav i opslaget', 'Dokumenteret erfaring'), [
        ('Planlægning og udførelse af forebyggende og korrigerende vedligehold på procesanlæg og '
         'udstyr',
         'Planlagt og korrigerende vedligehold på pumper, ventiler, HVAC, HV-tavler, SCADA og '
         'PLC i næsten 5 år (Biofos, 2017-2022) og på el, ventilation og klima for erhvervskunder '
         '(2023-2026). Forebyggende vedligehold i serviceaftaler med faste intervaller.'),
        ('Systematisk fejlfinding og problemløsning på tværs af mekanik, automatik og '
         'instrumentering',
         'Fejlfinding på el, styring og automatik siden 2003. A3, 5xHvorfor og Ishikawa som '
         'systematik. På tværs af fag: mekanik (pumper, ventiler), automatik (PLC, SCADA) og '
         'instrumentering fra commissioning af procesudstyr 2022-2024.'),
        ('GMP: Nøjagtig dokumentation af alt udført arbejde og efterlevelse af procedurer',
         'To år med GMP-projekter på Novo Nordisk (2022-2024): 37 CAPEX-projekter, protokoller '
         'skrevet før arbejdet, FAT/SAT og IQ/OQ/PQ, og nul kritiske fund ved afleveringen. '
         'Dokumentation i SAP og egne digitale tjeklister.'),
        ('EHS: Identificere, implementere og følge op på sikre løsninger og forbedringer',
         'LOTO, APV, risikovurdering ved opstart og nærved-hændelsesrapportering i 24/7-drift og '
         'på byggeplads (2017-2026). Opfølgning på sikre løsninger som fast punkt i 1:1 og på '
         'tavlemøder, og sikkerhedsdokumentation i alle entrepriser.'),
        ('Tæt sparring og support til Produktion, Engineering og EHS',
         'Tæt dialog med ledelse, kunder og produktion: månedsrapporter som projektleder, daglig '
         'sparring med produktion på Biofos i 4,5 år, og leverandørkontakt fra '
         'underentreprenørstyring i entreprise siden 2023, med kontakt til leverandør og '
         'underentreprenør undervejs. Vi løser opgaverne som ét team og '
         'spiller hinanden gode, og det passer med måden, holdene løste det på i skift.'),
        ('Bidrag til løbende forbedringer, standardisering og optimering af vedligeholdsprocesser',
         '5S og Standard Work indført i værkstedet (Biofos), PDCA-forløb med 40% lavere '
         'energiomkostninger, og digitalisering af tjeklister og rapporter siden 2024 med over '
         '40% hurtigere dokumentation.'),
        ('Vagtordning: Aftenvagt/tilkald ca. hver 6.–8. uge',
         'Skiftehold og vagtordning med tilkald på Biofos i 4,5 år (2017-2022): døgnbemanding, '
         'aftenvagter og tilkald, når anlægget stoppede. Rytmen kender jeg, og aftenvagt hver '
         '6.-8. uge er mildere end det.'),
        ('en teknisk baggrund som fx flymekaniker, automatiktekniker, industritekniker, smed '
         'eller tilsvarende',
         'Ikke flymekaniker eller smed. Elautoriseret maskinmester (LV/MV/HV, Sikkerhedsstyrelsen '
         'maj 2023) og elektromekanisk tekniker fra 2003, med hænderne i tekniske anlæg i over '
         '20 år. Tilsvarende teknisk baggrund, ikke bogstavet i opslaget.'),
        ('en anden relevant teknisk uddannelse med vedligeholdserfaring',
         'B.Tech (EQF6) i teknologiledelse og maskinteknik (2017-2022) og elteknik (EQF6). '
         'Vedligeholdserfaring: 4,5 år som vedligeholdelses- og driftsleder (Biofos) plus el- og '
         'servicevedligehold 2023-2026. Uddannelsen er relevant, erfaringen er dokumenteret.'),
        ('Du trives både selvstændigt og i teams og kan træffe velbegrundede beslutninger',
         'Selvstændigt: ejer og teknisk direktør med fuldt P&L-ansvar i 3+ år. I teams: '
         'skiftehold i 4,5 år og sjak på op til 14 mand. Beslutninger alene på pladsen: '
         'fejlfindingssager på renseanlægget, hvor ledelsen lå i Kalundborg og ikke kunne '
         'spørges.'),
        ('Du er omstillingsparat og motiveres af forandringer og vækstprojekter',
         'Virksomheden lukket november 2026 og næste kapitel valgt med det samme. Før det: '
         'skift fra værksted til renseanlæg (2017), fra drift til commissioning (2022) og til '
         'ejer af el-virksomhed (2023). Fire skift på 9 år er omstilling i praksis.'),
        ('Du har en proaktiv tilgang til vedligehold og høj kvalitetsbevidsthed',
         'Forebyggende vedligehold med faste intervaller frem for udkald, og kvalitet målt som '
         'nul kritiske fund ved aflevering (37 projekter) og nul kritiske afvigelser i '
         'serviceaftaler (2023-2026). Kvalitetsbevidsthed i GMP-ord er netop at følge '
         'procedurerne, også når det tager længere tid.'),
        ('Du har gode dansk- og engelskkundskaber i skrift og tale',
         'Dansk er mit modersmål, engelsk arbejdssprog i fire år på Novo Nordisk og i '
         'internationale samarbejder. Rapporter og protokoller skrevet på begge sprog '
         '(GMP-dokumentation på engelsk 2022-2024).'),
        ('Du er rutineret IT-bruger og arbejder struktureret med dokumentation',
         'SAP ERP, CMMS, Power BI, Excel, Python og Claude i daglig brug. Digitale tjeklister og '
         'rapportflow bygget i Python/Claude siden 2024. Struktureret dokumentation er en vane '
         'fra GMP: ingen opgave lukket uden sin journal.'),
        ('Du kommunikerer klart og konstruktivt på tværs af faggrupper og niveauer',
         'Faglig dialog med elektrikere, ingeniører, produktion og kunder siden 2003. Som '
         'projektleder broen mellem 25 specialister og ledelsen; som direktør forhandlinger med '
         'underentreprenører og kunder. Klar tale uden at tale ned.'),
        ('GMP-miljøer',
         'To års erfaring med GMP-miljøer fra Novo Nordisk (2022-2024): protokoller, '
         'afvigelseshåndtering, dokumentation og audit-klar aflevering på 37 projekter under '
         'GMP/FDA/EMA.'),
        ('CMMS-systemer (fx SAP/Maximo)',
         'SAP ERP i daglig drift siden 2022 og CMMS-vaner fra serviceaftaler med faste '
         'serviceintervaller, reservedelshåndtering og lukning af ordrer. Digitale tjeklister '
         'bygget i Python og Claude supplerer systemet.'),
        ('LEAN/5S/TPM',
         '5S og Standard Work indført i værkstedet på Biofos, PDCA-forløb med 40% lavere '
         'energiomkostninger, og TPM-elementer i det forebyggende vedligehold. LOTO-sikkerhed '
         'brugt dagligt i 24/7-drift og på byggeplads i 9 år.'),
        ('Udstyrstyper fra biofarmaceutisk produktion (fx CIP/SIP, bioreaktorer, pumper, ventiler, '
         'sensorer, filtrering eller kromatografi)',
         'CIP/SIP-anlæg, tanke, procesrør og instrumentering idriftsat og testet under GMP på '
         'Novo Nordisk (2022-2024). Pumper, ventiler og sensorer fra 4,5 års drift på Biofos. '
         'Bioreaktorer, filtrering og kromatografi: ikke serviceret endnu, og det er netop det, '
         'jeg vil lære hos jer.'),
    ], widths=(3400, 6946), compact=True)
    m.para('**Opslaget beder om ansøgning hurtigst muligt, og jeg kan tiltræde efter aftale. '
           'Jeg kan træffes på +45 93 99 95 14 eller ajlooshahram@gmail.com.**', after=8)

    m.save(path, title='Vedligeholdelsestekniker Drug Substance - FUJIFILM Biotechnologies')
    print(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_FUJIFILM_VedligeholdelsesteknikerDrugSubstance.docx'))
