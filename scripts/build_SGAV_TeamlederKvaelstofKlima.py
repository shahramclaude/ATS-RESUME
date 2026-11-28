# -*- coding: utf-8 -*-
"""SGAV · Teamleder til Kvælstof & Klima (Styrelsen for Grøn Arealomlægning og Vandmiljø), dansk opslag.

Dansk opslag -> dansk dokument. Masterdesign (scripts/master_design.py): brev side 1, CV side 2-3,
kravmatrix side 4. Kun fakta fra master-CV'et og brugerbekræftelser.
Ikke dokumenteret og derfor ikke skrevet som erfaring: kvælstofregulering, miljø- og landbrugsfaglig viden,
politisk styret organisation, handelsgødningsområdet. Brevet skriver, at stillingen er fundet på Jobindex
(opslagets anmodning). Ansøgning senest 11.12.2026. Kontakt: kontorchef Jesper Loldrup, jeslol@sgav.dk, 31 99 69 32.
1. samtaler onsdag 16.12.2026. Test forventes; ikke bekræftet af brugeren, derfor ikke nævnt som tilsagn.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
OUT_DIR = os.path.join(ROOT, 'output')
OUT = os.path.join(OUT_DIR, 'Shahram_Ajloo_SGAV_TeamlederKvaelstofKlima.docx')
KRAV = os.path.join(ROOT, 'jd', 'SGAV_TeamlederKvaelstofKlima_krav.txt')
KULTUR = os.path.join(ROOT, 'jd', 'SGAV_TeamlederKvaelstofKlima_kultur.txt')

NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Teamleder til Kvælstof & Klima · Styrelsen for Grøn Arealomlægning og Vandmiljø'
BANNER_RESUME = 'Personaleledelse, planlægning og implementering i reguleret og offentligt ejet miljø'

# (krav fra opslaget ordret, dokumentation og status) — 17 krav
ROWS = [
    ('Erfaring med ledelse eller en naturlig ledelseslyst og en motiverende tilgang til mennesker',
     'Dokumenteret. Ledelseserfaring fra produktionsteamleder hos ARJ (12 mekanikere og teknikere) til CTO for AI-afdelingen i Data Power. '
     'Personaleledelse af 5 elektrikere og 3 lærlinge i ELOHVAC og Data Power med 1:1, MUS og oplæring.'),
    ('Tydelig og præcis kommunikationsform. Du kan formidle komplekse budskaber enkelt og sikre, at alle involverede parter er informeret og inddraget',
     'Dokumenteret. Månedsrapportering til ledelse og bygherre hos Novo Nordisk, beslutningsoplæg og ledelsesrapportering i Data Power, '
     'og dansk og engelsk i skrift og tale.'),
    ('Trives i et miljø, hvor samarbejde på tværs af fagligheder er afgørende. Du har blik for de fælles mål og ser værdien i at koordinere bredt, herunder med dine kolleger i ledelsesgruppen',
     'Delvist dokumenteret. Tværfaglig koordinering af 25 specialister på tværs af engineering, indkøb og anlæg hos Novo Nordisk. '
     'Ledelsesgruppe i en enhed med flere teamledere er ikke dokumenteret.'),
    ('Du er god til at understøtte processer, så samarbejdet glider',
     'Dokumenteret. Standard Work, tavlemøder og standardiserede arbejdsgange hos Ventek-Air og Biofos, og ISO 9001-baseret kvalitetsstyring med audits og procedurer i ELOHVAC.'),
    ('Din ledelsesstil er baseret på tillid og feedback. Du får energi af at se dine medarbejdere vokse og af at skabe resultater gennem fælles indsats',
     'Dokumenteret i arbejdet. Enkeltsamtaler, MUS, situationsbestemt ledelse (SLII) og GROW i ELOHVAC og Data Power. '
     'Tillid som ledelsesholdning kan ikke dokumenteres ud over det konkrete samarbejde.'),
    ('Du evner at stå fast på dine principper og tydeligt kommunikere udfordringer',
     'Dokumenteret. Faglig kontrol før udsendelse af tilbud og dokumenter i ELOHVAC og Data Power, og beslutningsoplæg til ledelse med klare udfordringer og risici.'),
    ('Miljø- eller landbrugsfaglig viden (gerne)',
     'Ikke dokumenteret. Miljø- eller landbrugsfaglig viden er ikke en del af min erfaring. Spildevandsdrift hos Biofos (2017 til 2022) er teknisk drift af anlæg, ikke miljøregulering.'),
    ('Erfaring fra en politisk styret organisation (gerne)',
     'Delvist dokumenteret. Biofos (2017 til 2022) er et kommunalt ejet selskab med bestyrelse og myndighedstilsyn. Erfaring fra en politisk styret organisation i forvaltningen er ikke dokumenteret.'),
    ('Direkte personaleansvar og ansvaret for at drive dit teams opgaver i mål',
     'Dokumenteret. Personaleansvar for 5 medarbejdere i ELOHVAC og Data Power, og ledelse af teams fra 12 til 25 personer. '
     'Ansvar for at levere opgaverne i mål med tidsplan, økonomi og kvalitet i CAPEX-porteføljen hos Novo Nordisk.'),
    ('Sikre at dit team har de rette rammer, kvalifikationer og prioriteringer for at løse deres kerneopgaver effektivt og med høj kvalitet',
     'Dokumenteret. Daglig planlægning, kompetenceopfølgning og egen oplæringsplan for lærlinge i ELOHVAC, og prioritering af 37 CAPEX-projekter hos Novo Nordisk.'),
    ('Gennem sparring, feedback og tillid skabe trivsel, motivation og engagement hos medarbejderne',
     'Dokumenteret. Enkeltsamtaler, MUS og arbejdsmiljøopfølgning for 5 elektrikere og 3 lærlinge i ELOHVAC. '
     'Effekten på trivsel og engagement er ikke målt.'),
    ('Tænke den samlede enhed ind i dine beslutninger og aktivt bidrage til løsningen af enhedens fælles opgaver sammen med de øvrige teamledere og kontorchefen',
     'Delvist dokumenteret. Porteføljestyring af 37 CAPEX-projekter hos Novo Nordisk med fælles prioriteringer på tværs af engineering, indkøb og anlæg. '
     'Samarbejde med teamledere og kontorchef i en enhed er ikke dokumenteret.'),
    ('Omsætte enhedens prioriteter til konkrete arbejdsplaner, så opgaverne løses rettidigt og med den rette kvalitet',
     'Dokumenteret. 37 samtidige CAPEX-projekter og 11 parallelle anlægsprojekter med én samlet plan, tavlemøder og flaskehalsanalyser i Ventek-Air.'),
    ('Sikre en klar informationsstrøm til teamet og gnidningsfri information på tværs af andre teams og enheder',
     'Delvist dokumenteret. Månedsrapportering til ledelse og bygherre hos Novo Nordisk, og informationsstrøm via tavlemøder i Ventek-Air og Data Power. '
     'Gnidningsfri information på tværs af enheder er ikke dokumenteret.'),
    ('Være en aktiv sparringspartner for medarbejderne i komplekse sagsforløb',
     'Dokumenteret. Fejlfinding i døgndrift hos Biofos, rådgivning om drift, service og projekter, og rodårsagsanalyse med A3, 5 Hvorfor og Ishikawa.'),
    ('Omsætte politiske og faglige målsætninger til konkret handling i teamet, herunder implementeringen af den nye kvælstofregulering i 2027 og koordination med styrelsens processer, bl.a. IT-opsætningen',
     'Delvist dokumenteret. Implementering af applikationer i Data Power: kravafdækning, integration mod kundens systemer, idriftsættelse og overdragelse. '
     'Ny GMP-procedure og ændringsstyring hos Novo Nordisk. Kvælstofregulering og styrelsens IT-opsætning er ikke dokumenteret.'),
    ('Ansvar for handelsgødningsområdet, herunder et område i udvikling med produkter med flere anvendelser',
     'Ikke dokumenteret. Handelsgødning og produkter med flere anvendelser er ikke i min erfaring. Produktudvikling er ikke dokumenteret i dette område.'),
]

KULTUR_PHRASES = [
    'Vi har et engageret arbejdsmiljø med høj faglighed',
    'det skal være sjovt at gå på arbejde',
    'lægger vægt på lederudvikling og god ledelse på alle niveauer',
    'et kollegialt netværk',
    'en udfordrende opgave med gode muligheder for personlig og faglig udvikling',
    'Ledelsesgruppen er central ift. at formidle styrelsens retning og værdier til medarbejderne',
    'Dine teamleder-kollegaer fungerer også som dine nærmeste sparringspartnere i dagligdagen',
    'Vi har mange dygtige ledere i styrelsen',
]


def write_inputs():
    with open(KRAV, 'w', encoding='utf-8') as f:
        f.write('# Krav fra SGAV · Teamleder til Kvælstof & Klima, dansk, ordret fra opslaget (Ministeriet for Natur og Dyrevelfærd, Nyropsgade 30)\n')
        for krav, _ in ROWS:
            f.write(krav + '\n')
    with open(KULTUR, 'w', encoding='utf-8') as f:
        f.write('# Arbejdsgiverens egne udtryk fra opslaget (dansk, ordret). Skal genfindes ordret i dokumentet.\n')
        for phrase in KULTUR_PHRASES:
            f.write(phrase + '\n')


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER, 'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo')
    m.meta('28. november 2026')
    m.meta('SGAV · Ministeriet for Natur og Dyrevelfærd · ansøgning senest 11. december 2026')
    m.para('Kære Jesper Loldrup,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    def sub(text):
        p = m._p(spacing_after=20, spacing_before=60, line=260, justify=False, keep_next=True)
        m._run(p, text, bold=True, color='002B5C')
        return p

    # ------------------------------------------------------------ brev, side 1
    lp('Jeg fandt stillingen på Jobindex. Styrelsen for Grøn Arealomlægning og Vandmiljø står midt i implementeringen af kvælstofreguleringen, som træder i kraft i 2027, og opgaven er at omsætte de politiske og faglige '
       'målsætninger til konkrete arbejdsplaner for et team på ca. 45 i enheden. Det kræver, at teamet kender prioriteterne, og at '
       'informationen flyder til de andre teams og til IT-opsætningen uden friktion. Den balance ser jeg som kernen i rollen. Dine teamleder-kollegaer fungerer også som dine nærmeste sparringspartnere i dagligdagen, og det er dem, jeg vil bygge samarbejdet med fra start.')

    sub('Fra målsætning til arbejdsplan')
    lp('Jeg har ledet teams, hvor fremdrift og kvalitet skulle holdes sammen på tværs af fag. Som projektleder hos Novo Nordisk '
       'fulgte jeg 37 samtidige CAPEX-projekter med månedsrapportering til ledelse og bygherre. Hos Ventek-Air ledte jeg 11 parallelle '
       'anlægsprojekter med én samlet plan, tavlemøder og flaskehalsanalyser. Metoden er den samme, uanset om opgaven er et anlæg eller en regulering: '
       'prioriteringen skal være synlig, og opfølgningen skal vise, om planen holder.')

    sub('Koordination på tværs og med IT')
    lp('Opslaget beskriver, at ledelsesgruppen er central ift. at formidle styrelsens retning og værdier til medarbejderne. '
       'Vi har mange dygtige ledere i styrelsen, og jeg har koordineret 25 specialister på tværs af engineering, indkøb og anlæg hos Novo Nordisk. I Data Power har jeg '
       'ansvaret for implementering af applikationer, herunder integration mod kundens eksisterende systemer. Den erfaring vil jeg '
       'bringe ind i koordinationen med styrelsens IT-opsætning.')

    sub('Medarbejdere og faglighed')
    lp('Opslaget siger, at det skal være sjovt at gå på arbejde, og at vi har et engageret arbejdsmiljø med høj faglighed. Styrelsen lægger vægt på lederudvikling og god ledelse på alle niveauer. '
       'Jeg leder med enkeltsamtaler, MUS og en fast oplæringsplan for lærlinge, og jeg vil gerne sparre med medarbejderne i de komplekse sager, '
       'så faglig kvalitet bliver en fælles sag. Den ramme ønsker jeg at skabe i teamet.')

    sub('Det, der er nyt for mig')
    lp('Kvælstofregulering, miljø- og landbrugsfaglig viden og erfaring fra en politisk styret organisation er ikke en del af min dokumenterede erfaring. '
       'Handelsgødningsområdet er også nyt for mig. Jeg vil bruge den første tid på at lære regelgrundlaget og teamets sager at kende, '
       'og jeg vil bruge mit kendskab til at styre processer og regulerede miljøer til at understøtte det arbejde. '
       'Opslaget beskriver et kollegialt netværk fordelt i hele landet og en udfordrende opgave med gode muligheder for personlig og faglig udvikling, og det er en ramme, jeg gerne vil arbejde i.')

    lp('Jeg vil gerne tale om, hvilke sager der har størst presserende behov i starten, og hvordan IT-opsætningen skal '
       'koordineres med teamets arbejde.', after=44)
    lp('Med venlig hilsen', after=8)
    lp('Shahram Ajloo', after=8)

    # ------------------------------------------------------------ CV, side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Elautoriseret maskinmester (LV/MV/HV) med ledelseserfaring fra produktion og projekter. Personaleledelse af 5 elektrikere '
           'og 3 lærlinge, ledelse af teams fra 5 til 25 personer, 37 samtidige CAPEX-projekter hos Novo Nordisk og 11 parallelle '
           'anlægsprojekter hos Ventek-Air. Erfaring fra kommunalt ejet forsyning (Biofos) med bestyrelse og myndighedstilsyn. '
           'Kvælstofregulering, miljø- og landbrugsfaglig viden og politisk styret forvaltning er ikke dokumenteret. PRINCE2-certificeret. Dansk og engelsk.', after=32)

    m.section('LEDELSE OG UDVIKLING AF MEDARBEJDERE')
    tasks = [
        ('Personaleledelse',
         'Personaleledelse af 5 elektrikere og 3 lærlinge i ELOHVAC og Data Power med daglig planlægning, enkeltsamtaler, MUS og oplæring.'),
        ('Teamledelse',
         'Ledelse af et 14-mands entrepriseteam hos Ventek-Air og et 12-mands værkstedsteam hos ARJ. Ledelse af driftsteam i skiftehold hos Biofos.'),
        ('Tværfaglig koordinering',
         'Koordinering af 25 specialister på tværs af engineering, indkøb og anlæg hos Novo Nordisk.'),
        ('Faglig udvikling',
         'Standard Work, 5S og PDCA-arbejde på værksted og lager, og struktureret oplæring af lærlinge.'),
    ]
    for head, body in tasks:
        m.bullet(head, body, after=24)

    m.section('STRATEGI, PRIORITERING OG OPFØLGNING')
    tasks = [
        ('Porteføljestyring',
         '37 samtidige CAPEX-projekter (DKK 2 til 10 mio. pr. stk.) hos Novo Nordisk med fremdrift, økonomi, risici og ressourcer, og månedsrapportering til ledelse og bygherre.'),
        ('Strategi til handling',
         'PDCA-program med 40 % lavere energiomkostninger hos Biofos. Daglige tavlemøder og flaskehalsanalyser hos Ventek-Air.'),
        ('Governance',
         'ISO 9001-baseret kvalitetsstyring med audits, afleveringsdokumentation og KS-opfølgning i ELOHVAC.'),
        ('Implementering af applikationer',
         'Kravafdækning, integration mod kundens systemer, idriftsættelse og overdragelse i Data Power.'),
    ]
    for head, body in tasks:
        m.bullet(head, body, after=24)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester, ansvarlig for el-teknik og ventilation',
         'Data Power Consultant ApS · København · 2024 til i dag',
         [('', 'Ansvarlig for AI- og AI coding-afdelingen med 4 til 10 personer. Tekniske og industrielle applikationer fra kravafdækning til overdragelse.'),
          ('', 'El-teknik og ventilation med fuldt P&L-ansvar. Fra november 2026 også de el-tekniske aktiviteter fra ELOHVAC.'),
          ('', 'Personaleledelse af 5 elektrikere og 3 lærlinge.')]),
        ('Ejer og teknisk direktør, elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 til november 2026 (virksomheden lukket)',
         [('', 'Tilbud og beregning, tidsplaner, materialestyring og underentreprenører. Fuldt P&L-ansvar.'),
          ('', 'Akkord og opmåling, med akkordbreve og regulering af mer- og mindrearbejde.')]),
        ('Senior idriftsættelsesingeniør og projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg og Bagsværd · november 2022 til juli 2024',
         [('', '37 samtidige anlægs- og CAPEX-projekter, med fremdrift, økonomi og risici på tværs af engineering, indkøb og anlæg.'),
          ('', 'Tværfaglig ledelse af 25 specialister. SAP ERP til økonomi, anlægsaktiver og omkostninger.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · januar 2022 til november 2022',
         [('', '11 samtidige anlægsprojekter fra specifikation til formel aflevering, med et 14-mands team.'),
          ('', 'Udbud, tilbud, underentreprenører og aftalegrundlag.')]),
        ('Vedligeholdelses- og driftsleder, værkstedstekniker',
         'Biofos (Lynetten) · København · august 2017 til januar 2022',
         [('', 'Drift og vedligehold af pumper, HVAC, højspændingstavler og SCADA i døgndrift. Erfaring fra spildevandssiden.'),
          ('', 'Ledelse af driftsteam i skiftehold på ledelsesniveau.')]),
        ('Elektromekaniker og produktionsteamleder',
         'ARJ Engineering · Teheran · december 2003 til marts 2010',
         [('', 'Ledelse af 12 mekanikere og teknikere: vagtplanlægning, materialer og mål.'),
          ('', 'Fejldiagnose og reparation af industrielle el- og mekaniske anlæg.')]),
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
        ('Ledelse', 'Personaleledelse, MUS, enkeltsamtaler, situationsbestemt ledelse (SLII), GROW, RACI, interessentanalyse'),
        ('Kommunikation', 'Beslutningsoplæg, ledelsesrapportering, månedsrapportering til bygherre'),
        ('Økonomi og data', 'SAP ERP, Excel, Python, Claude API'),
        ('Kvalitet og governance', 'ISO 9001, audits, afvigelser, procedurer, KS, afleveringsdokumentation'),
        ('Forbedring', 'PDCA, 5S, Standard Work, A3, Kaizen, 5 Hvorfor, Ishikawa'),
    ], widths=(3400, 6946), compact=True)
    m.para('Dansk og engelsk i skrift og tale, engelsk som arbejdssprog siden 2017. Persisk modersmål. Kørekort B med manuelt gear.', after=40)

    # ------------------------------------------------------------ kravmatrix, side 4
    m.page_break()
    m.section('KRAVMATRIX')
    m.models_table('Opslagets krav og min dokumentation', ('Krav', 'Dokumentation og status'),
                   ROWS, widths=(3600, 6746), compact=True)

    m.save(path, title='Teamleder til Kvælstof & Klima - SGAV',
           subject='Ansøgning Teamleder til Kvælstof & Klima')
    print(path)


if __name__ == '__main__':
    os.makedirs(OUT_DIR, exist_ok=True)
    write_inputs()
    build(OUT)
