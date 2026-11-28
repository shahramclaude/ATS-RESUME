# -*- coding: utf-8 -*-
"""Nexel A/S · Teknisk projektleder, Mellem-reinvesteringer og Linjer (Virum, hjemmearbejde nævnt).

Dansk opslag -> dansk dokument. Masterdesign (scripts/master_design.py): brev side 1, CV side 2-3,
kravmatrix side 4. Kun fakta fra master-CV'et og brugerbekræftelser.
Ikke dokumenteret og derfor ikke skrevet som erfaring: kabellægning af 30 kV kabler, arbejde i netstationer,
kontakt med naboer til et projekt, opstartsmøder som fast rutine, projektering af netanlæg,
tilladelser til reinvestering i net. Titlen er elautoriseret maskinmester, ikke elinstallatør.
Pendling til Virum og hjemmearbejde er ikke bekræftet for denne stilling (double-check).
Ansøgning sendes kun via annoncen (GDPR, jf. opslaget).
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
OUT_DIR = os.path.join(ROOT, 'output')
OUT = os.path.join(OUT_DIR, 'Shahram_Ajloo_Nexel_TekniskProjektleder_Reinvestering.docx')
KRAV = os.path.join(ROOT, 'jd', 'Nexel_TekniskProjektleder_Reinvestering_krav.txt')
KULTUR = os.path.join(ROOT, 'jd', 'Nexel_TekniskProjektleder_Reinvestering_kultur.txt')

NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Teknisk projektleder, Mellem-reinvesteringer og Linjer · Nexel A/S, Virum'
BANNER_RESUME = 'Projektledelse af el-anlæg og entrepriser fra idé til aflevering'

# (krav fra opslaget ordret, dokumentation og status)
ROWS = [
    ('En baggrund som ingeniør, elinstallatør eller maskinmester (evt. kombineret med en elektrikerbaggrund)',
     'Dokumenteret som maskinmester: elautoriseret maskinmester (LV/MV/HV), Sikkerhedsstyrelsen, maj 2023, og B.Tech (EQF6) '
     'i teknologiledelse og maskinteknik, 2017 til 2022. Jeg er ikke uddannet elinstallatør og har ikke svendebrev som elektriker.'),
    ('Minimum 2 års erfaring som projektleder',
     'Dokumenteret. Projektledelse i Novo Nordisk fra november 2022 til juli 2024, i Ventek-Air fra januar 2022, '
     'og i ELOHVAC fra maj 2023 og i Data Power fra 2024 til i dag.'),
    ('Motivation og erfaring med at skabe god og imødekommende kommunikation, om det er naboerne til dit projekt, eksterne rådgivere, entreprenørvirksomheder eller interne samarbejdspartnere, du kommunikerer med',
     'Delvist dokumenteret. Kommunikation med entreprenører og underentreprenører hos Ventek-Air og ELOHVAC, og tværfaglig koordinering '
     'af 25 specialister hos Novo Nordisk. Kommunikation med naboer til et projekt er ikke dokumenteret i min erfaring.'),
    ('Du formår at skabe følgeskab og tætte relationer omkring dine projekter, så deltagerne trækker i samme retning og bidrager til både fremdrift og en god stemning',
     'Dokumenteret. Daglige tavlemøder og flaskehalsanalyser med et 14-mands team hos Ventek-Air, enkeltsamtaler og MUS for '
     '5 elektrikere og 3 lærlinge i ELOHVAC, og tværfaglig ledelse af 25 specialister hos Novo Nordisk.'),
    ('Dansk på højt niveau og godt kendskab til engelsk',
     'Dokumenteret. Skrift og tale på højt niveau på dansk. Engelsk har været arbejdssprog i internationale projekter siden 2017, '
     'og det bruges i dag i professionelle sammenhænge, både skriftligt og mundtligt.'),
    ('Erfaring med Microsoft Office og SAP',
     'Dokumenteret. Excel og Office i daglig brug, Microsoft Project som fast planlægningsværktøj, og SAP ERP til økonomi, '
     'anlægsaktiver og omkostninger hos Novo Nordisk, 2022 til 2024.'),
    ('Kørekort B.',
     'Dokumenteret. Kørekort B med manuelt gear er bekræftet i min dokumentation. Kørsel mellem kontoret i Virum og anlæg i marken '
     'er en separat afklaring, og den står i rækken om placering.'),
    ('Planlægger og projekterer projekter fra idé til udførelse ved at vælge de rette tekniske løsninger og sikre de nødvendige myndighedstilladelser',
     'Delvist dokumenteret. Planlægning fra specifikation til aflevering hos Ventek-Air og Novo Nordisk, og tilbud og beregning i ELOHVAC. '
     'Direkte kontakt til myndigheder og indberetning i reguleret sammenhæng, uden navngivne myndigheder. '
     'Projektering af netanlæg og tilladelser til reinvestering i nettet er ikke dokumenteret.'),
    ('Udarbejder og kvalitetssikrer entreprisedokumenter, budgetter og projektplaner i tæt samarbejde med kolleger og interessenter',
     'Dokumenteret. Udbud, tilbud, aftalegrundlag og afleveringspakker hos Ventek-Air, tidsplaner og KS-tjeklister i ELOHVAC, '
     'og fremdrift, økonomi og risici i Novo Nordisk-projekterne. Dokumenterne gennemgås med faglig kontrol, før de sendes ud.'),
    ('Afholdelse af opstartsmøder med vores entreprenører og løbende opfølgning på, at fremdrift, kvalitet og leverancer gennem hele udførelsesfasen forløber som planlagt',
     'Delvist dokumenteret. Løbende opfølgning på fremdrift, kvalitet og leverancer i udførelsesfasen hos Novo Nordisk og Ventek-Air. '
     'Pladsopstart med LOTO og APV er dokumenteret i ELOHVAC. Opstartsmøder med entreprenører som fast rutine er ikke dokumenteret.'),
    ('Tager ansvar for, at arbejdet udføres sikkert, effektivt og i overensstemmelse med gældende krav og standarder',
     'Dokumenteret. LOTO, risikovurdering og APV ved pladsopstart i ELOHVAC, nul kritiske afvigelser ved aflevering hos Novo Nordisk, '
     'og ISO 9001-baseret kvalitetsstyring med audits.'),
    ('Fører projekterne i mål gennem tæt styring af økonomi, ressourcer og tidsplaner',
     'Dokumenteret. Fremdrift, økonomi, risici og ressourcer i 37 samtidige CAPEX-projekter hos Novo Nordisk, og fuldt P&L-ansvar '
     'i ELOHVAC og Data Power.'),
    ('Koordinerer samarbejdet på tværs af organisationen og sørger for, at dine kolleger i projektet er motiverede og klædt godt på til deres opgaver',
     'Dokumenteret. Koordinering af 25 specialister på tværs af engineering, indkøb og anlæg hos Novo Nordisk. '
     'Klare roller og daglig planlægning af et 14-mands team hos Ventek-Air.'),
    ('Du sikrer rettidig dokumentation og håndterer risici og udfordringer, så projekterne leveres som aftalt',
     'Dokumenteret. Afleveringsdokumentation og afleveringspakker hos Ventek-Air og ELOHVAC, risikostyring i Novo Nordisk-projekterne, '
     'og flaskehalsanalyser som fast værktøj i udførelsen.'),
    ('Som person har du en løsningsorienteret tilgang til opgaverne og trives med at tage ansvar for forskellige typer af projekter',
     'Dokumenteret i metoden. Rodårsagsanalyse med A3, 5 Hvorfor og Ishikawa hos Novo Nordisk, og fejldiagnose med korrigerende '
     'handlinger hos ARJ. Projekterne har spændt over el, ventilation, procesanlæg og service.'),
    ('Trives med at indgå i et fællesskab og med at være sammen med kolleger på kontoret og ude i marken',
     'Dokumenteret i arbejdsformen. Montage, test og fejlfinding på anlæg hos Novo Nordisk, Biofos og ELOHVAC, og tilbud, planlægning '
     'og dokumentation på kontoret. Fast placering i Virum og hjemmearbejde er ikke bekræftet for denne stilling.'),
    ('reinvesteringsprojekter i 10/04 kV nettet og kabellægning af 30 kV kabler',
     'Delvist dokumenteret. Direkte arbejde med 10/0,4 kV distributionsnet, uden konkrete anlæg, komponenter eller perioder. '
     'Kabellægning af 30 kV kabler er ikke dokumenteret.'),
    ('Typisk en projektportefølje på 3-5 projekter i gang hele tiden',
     'Dokumenteret. Langt flere samtidige projekter end 3 til 5: 11 parallelle anlægsprojekter hos Ventek-Air '
     'og 37 samtidige CAPEX-projekter hos Novo Nordisk, styret med én samlet plan.'),
]

KULTUR_PHRASES = [
    'økonomisk gatekeeper og teknisk sparringspartner',
    'driver dem selv fra end-to-end',
    'tæt styring af økonomi, ressourcer og tidsplaner',
    'i overensstemmelse med gældende krav og standarder',
    'god og imødekommende kommunikation',
    'skabe følgeskab og tætte relationer',
    'løsningsorienteret tilgang',
    'relationer, der bunder i tillid',
]


def write_inputs():
    with open(KRAV, 'w', encoding='utf-8') as f:
        f.write('# Krav fra Nexel A/S · Teknisk projektleder, Mellem-reinvesteringer og Linjer (Virum), dansk, ordret fra opslaget\n')
        for krav, _ in ROWS:
            f.write(krav + '\n')
    with open(KULTUR, 'w', encoding='utf-8') as f:
        f.write('# Arbejdsgiverens egne udtryk fra opslaget (dansk, ordret). Skal genfindes ordret i dokumentet.\n')
        for phrase in KULTUR_PHRASES:
            f.write(phrase + '\n')


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo')
    m.meta('28. november 2026')
    m.meta('Nexel A/S · Virum · ansøgning sendt via annoncen')
    m.para('Kære Signe Skovgaard Nielsen,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    def sub(text):
        p = m._p(spacing_after=20, spacing_before=60, line=260, justify=False, keep_next=True)
        m._run(p, text, bold=True, color='002B5C')
        return p

    # ------------------------------------------------------------ brev, side 1
    lp('Nexel bygger og varetager driften af forsyningsanlæg, der sikrer strøm til alle. I afdelingen for '
       'Mellem-reinvesteringer og Linjer skal 10/0,4 kV nettet fornyes, og 30 kV kabler skal lægges i jorden, '
       'mens strømmen fortsat skal være der. Stillingen som teknisk projektleder er den, der binder det sammen. '
       'Opslaget beskriver rollen som økonomisk gatekeeper og teknisk sparringspartner, og det er den rolle, jeg '
       'ser som kernen i opgaven.')

    sub('Fra idé til udførelse')
    lp('Et reinvesteringsprojekt starter med et teknisk valg, der skal kunne bygges i et net under drift. '
       'Tilladelserne skal være afklaret, før entreprisen udbydes, ellers flytter en enkelt ændring hele tidsplanen. '
       'Jeg vil afklare, hvilke myndigheder der skal inddrages, og hvad det kræver, før budget og projektplan skrives. '
       'Entreprisedokumenterne kvalitetssikres sammen med kolleger og interessenter, så de ikke skal rettes ude i marken.')

    sub('Naboer, rådgivere og entreprenører')
    lp('Et kabelarbejde i en vej rammer de boliger og virksomheder, der ligger langs den. Derfor skal der være en plan '
       'for, hvem der informerer hvem, og hvornår, før første gravning. God og imødekommende kommunikation er ikke en '
       'sidegerning her, og relationer, der bunder i tillid, bygges i de første møder. Rådgiverne skal have de samme '
       'oplysninger som entreprenøren, så spørgsmål fra pladsen kan besvares samme dag.')

    sub('Opstart og opfølgning')
    lp('Opstartsmødet med entreprenøren er stedet, hvor ansvar, sikkerhed og fremdrift aftales. Herfra følges fremdrift, '
       'kvalitet og leverancer, til arbejdet er udført, og arbejdslederen på lokationen er med i de beslutninger, der '
       'rammer pladsen. Det er her, jeg vil skabe følgeskab og tætte relationer, så alle trækker i samme retning. '
       'Sikkerheden står først, og arbejdet skal udføres i overensstemmelse med gældende krav og standarder.')

    sub('Tre til fem projekter ad gangen')
    lp('Opslaget beskriver en projektportefølje på tre til fem projekter i gang hele tiden. Projektlederen driver dem selv '
       'fra end-to-end, og det kræver, at økonomi, ressourcer og tidsplaner ses samlet. Et forsinket projekt må ikke '
       'stille og roligt trække folk fra et andet. Jeg vil starte med en fast ugentlig gennemgang af porteføljen med én '
       'fælles risikoliste og en tæt styring af økonomi, ressourcer og tidsplaner.')

    sub('Det, der er nyt for mig')
    lp('30 kV kabellægning og arbejde i netstationer er ikke dokumenteret i min erfaring. Jeg har arbejdet med '
       '10/0,4 kV distributionsnet, og jeg kender el- og ventilationsanlæg, tavler og styring, projektledelse i entreprise '
       'og drift i døgnbemanding. Netkomponenterne og 30 kV-arbejdet skal jeg lære i onboarding og sammen med '
       'mentoren og kollegerne i afdelingen.')

    lp('Jeg vil gerne tale om, hvilke projekter der har mest presserende behov i porteføljen, og hvilke tilladelser der '
       'er afklaret, før det første udbud.', after=44)
    lp('Med venlig hilsen', after=8)
    lp('Shahram Ajloo', after=8)

    # ------------------------------------------------------------ CV, side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Elautoriseret maskinmester (LV/MV/HV) med mindst tre års projektledelse og entreprisestyring i el- og beslægtede '
           'brancher. Hos Novo Nordisk fremdrift, økonomi og risici i 37 samtidige CAPEX-projekter, og hos Ventek-Air '
           '11 parallelle anlægsprojekter fra specifikation til aflevering. Direkte arbejde med 10/0,4 kV distributionsnet. '
           'PRINCE2-certificeret. Taler og skriver begge sprog flydende, og har kørekort B.', after=32)

    m.section('PROJEKTLEDELSE OG ENTREPRISE')
    tasks = [
        ('Planlægning og udbud',
         'Udbud, tilbud, aftalegrundlag og afleveringspakker hos Ventek-Air. Tidsplaner og KS-tjeklister i ELOHVAC.'),
        ('Økonomi og portefølje',
         'Fremdrift, økonomi, risici og ressourcer i 37 samtidige CAPEX-projekter hos Novo Nordisk, med månedsrapportering '
         'til ledelse og bygherre. Budgetter og anlægsaktiver i SAP ERP.'),
        ('Koordinering',
         'Tværfaglig koordinering af 25 specialister på tværs af engineering, indkøb og anlæg. Daglige tavlemøder og '
         'flaskehalsanalyser hos Ventek-Air.'),
        ('Sikkerhed og kvalitet',
         'LOTO, risikovurdering og APV ved pladsopstart. Nul kritiske afvigelser ved aflevering hos Novo Nordisk. '
         'ISO 9001-baseret kvalitetsstyring med audits.'),
    ]
    for head, body in tasks:
        m.bullet(head, body, after=24)

    m.section('DRIFT, VEDLIGEHOLD OG ANLÆG')
    tasks = [
        ('Elnet og anlæg',
         'Direkte arbejde med 10/0,4 kV distributionsnet. Drift og vedligehold af pumper, HVAC, højspændingstavler og SCADA '
         'i døgndrift hos Biofos, 2017 til 2022.'),
        ('Montage, test og idriftsættelse',
         'FAT, SAT og IQ/OQ/PQ under GMP, FDA og EMA hos Novo Nordisk. Idriftsættelse af el- og procesanlæg, tavler og styring.'),
        ('Fejlfinding og forbedring',
         'Rodårsagsanalyse med A3, 5 Hvorfor og Ishikawa. PDCA-program med 40 % lavere energiomkostninger hos Novo Nordisk.'),
    ]
    for head, body in tasks:
        m.bullet(head, body, after=24)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester, ansvarlig for el-teknik og ventilation',
         'Data Power Consultant ApS · København · 2024 til i dag',
         [('', 'Ansvarlig for AI- og AI coding-afdelingen med 4 til 10 personer. Tekniske og industrielle applikationer '
               'fra kravafdækning til overdragelse.'),
          ('', 'El-teknik og ventilation med fuldt P&L-ansvar, herunder akkord og opmåling. Fra november 2026 også de '
               'el-tekniske aktiviteter fra ELOHVAC.'),
          ('', 'Personaleledelse af 5 elektrikere og 3 lærlinge: daglig planlægning, enkeltsamtaler, MUS og oplæring.')]),
        ('Ejer og teknisk direktør, elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 til november 2026 (virksomheden lukket)',
         [('', 'Installation, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg, fra akutte udkald '
               'til afleverede anlæg.'),
          ('', 'Tilbud og beregning, tidsplaner, materialestyring og underentreprenører. Pladsopstart med LOTO, risikovurdering og APV.'),
          ('', 'Akkord og opmåling: akkordbreve, opmåling af udført arbejde og regulering af mer- og mindrearbejde.')]),
        ('Senior idriftsættelsesingeniør og projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg og Bagsværd · november 2022 til juli 2024',
         [('', 'FAT, SAT og IQ/OQ/PQ under GMP, FDA og EMA, med nul kritiske afvigelser ved aflevering.'),
          ('', 'Tværfaglig koordinering af 25 specialister og 37 samtidige anlægsprojekter.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · januar 2022 til november 2022',
         [('', '11 samtidige anlægsprojekter fra specifikation til formel aflevering, med et 14-mands team.'),
          ('', 'Udbud, underentreprenører, sikkerhedsdokumentation og afleveringspakker.')]),
        ('Vedligeholdelses- og driftsleder, værkstedstekniker',
         'Biofos (Lynetten) · København · august 2017 til januar 2022',
         [('', 'Drift og vedligehold af pumper, HVAC, højspændingstavler og SCADA i døgndrift på spildevandsrensningen.'),
          ('', 'Ledelse af driftsteam i skiftehold på ledelsesniveau og teamledelse på øvrige niveauer i døgnbemanding.')]),
        ('Elektromekaniker og produktionsteamleder',
         'ARJ Engineering · Teheran · december 2003 til marts 2010',
         [('', 'Ledelse af 12 mekanikere og teknikere i værkstedet: vagtplanlægning, materialer og mål.'),
          ('', 'Fejldiagnose og reparation af industrielle el- og mekaniske anlæg med rodårsagsanalyse.')]),
    ]
    for title, meta, bullets in jobs:
        m.job(title, meta)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('UDDANNELSE OG CERTIFICERINGER')
    m.edu('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('B.Tech (EQF6), teknologiledelse og maskinteknik',
          'Copenhagen School of Marine Engineering & Technology Management · 2017 til 2022')
    m.edu('Køleteknik og klimaanlæg (AMU)', 'Mercantec · 2021')
    m.edu('PRINCE2, certificeret', 'AXELOS / PeopleCert')
    m.para('Lean og Six Sigma anvendt i praksis, ikke certificeret: DMAIC, 5S, PDCA, VSM, A3, Kaizen, SMED, TPM, '
           '5 Hvorfor, Ishikawa og FMEA.', after=48)

    m.section('KOMPETENCER')
    m.models_table('Værktøjer og systemer', ('Område', 'Værktøjer'), [
        ('Projekt og styring', 'PRINCE2, Microsoft Project, RACI, udbud, tilbud, KS, afleveringspakker'),
        ('Net og anlæg', '10/0,4 kV distributionsnet, højspændingstavler, SCADA, styretavler, CTS/BMS'),
        ('Økonomi og data', 'SAP ERP, Microsoft Office, Excel, Python, Claude API'),
        ('Sikkerhed og kvalitet', 'LOTO, APV, risikovurdering, ISO 9001, audits, afvigelser'),
        ('Forbedring', 'PDCA, 5S, Standard Work, A3, FMEA, 5 Hvorfor, Ishikawa'),
    ], widths=(3400, 6946), compact=True)
    m.para('Persisk modersmål. Engelsk har været arbejdssprog siden 2017, og skrift og tale på dansk er fuldt ud på højt niveau. Kørekort B.', after=40)

    # ------------------------------------------------------------ kravmatrix, side 4
    m.page_break()
    m.section('KRAVMATRIX')
    m.models_table('Opslagets krav og min dokumentation', ('Krav', 'Dokumentation og status'),
                   ROWS, widths=(3600, 6746), compact=True)

    m.save(path, title='Teknisk projektleder, Mellem-reinvesteringer og Linjer - Nexel A/S',
           subject='Ansøgning Teknisk projektleder, Mellem-reinvesteringer og Linjer')
    print(path)


if __name__ == '__main__':
    os.makedirs(OUT_DIR, exist_ok=True)
    write_inputs()
    build(OUT)
