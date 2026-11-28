# -*- coding: utf-8 -*-
"""Amgros · Teamleder til et forhandlingsområde i udvikling (Rådgivning og Forhandling), dansk opslag.

Dansk opslag -> dansk dokument. Masterdesign (scripts/master_design.py): brev side 1, CV side 2-3,
kravmatrix side 4. Kun fakta fra master-CV'et og brugerbekræftelser.
Ikke dokumenteret og derfor ikke skrevet som erfaring: forhandling af lægemiddelpriser, kendskab til
lægemiddelmarkedet og MFN-/alternative aftalemodeller, samarbejde med Medicinrådet, primærområdet,
individuel ibrugtagning. Startdato i opslaget står som 1. februar 2026, men datoen i dag er 28.11.2026;
det er flagget som double-check. Ansøgning senest 11.12.2026. Kontakt: chef Marie Gerstrøm, 61 75 50 81.
Salgsledelse, CRM, pipeline og forecast er brugerbekræftet generelt (23.11.2026) og er ikke bundet til en arbejdsgiver.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
OUT_DIR = os.path.join(ROOT, 'output')
OUT = os.path.join(OUT_DIR, 'Shahram_Ajloo_Amgros_TeamlederForhandlingsomraade.docx')
KRAV = os.path.join(ROOT, 'jd', 'Amgros_TeamlederForhandlingsomraade_krav.txt')
KULTUR = os.path.join(ROOT, 'jd', 'Amgros_TeamlederForhandlingsomraade_kultur.txt')

NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Teamleder til et forhandlingsområde i udvikling · Amgros, Rådgivning og Forhandling'
BANNER_RESUME = 'Personaleledelse, strategi til handling og aftalestyring i reguleret industri'

# (krav fra opslaget ordret, dokumentation og status)
ROWS = [
    ('Solid erfaring med forhandling og stærk kommerciel og strategisk forståelse for lægemiddelmarkedet',
     'Delvist dokumenteret. Udbud, tilbud og aftalegrundlag hos Ventek-Air og ELOHVAC, og prisopfølgning i SAP ERP hos Novo Nordisk. '
     'Forhandling af lægemiddelpriser og markedskendskab til lægemiddelområdet er ikke dokumenteret. GMP-produktion hos Novo Nordisk er ikke det samme som markedet.'),
    ('God til at omsætte strategi til handling og følge op på resultater',
     'Dokumenteret. 37 samtidige CAPEX-projekter hos Novo Nordisk med månedsrapportering til ledelse og bygherre. '
     'PDCA-program med 40 % lavere energiomkostninger, og daglige tavlemøder med flaskehalsanalyser hos Ventek-Air.'),
    ('Erfaring med eller lyst til personaleledelse',
     'Dokumenteret. Personaleledelse af 5 elektrikere og 3 lærlinge med enkeltsamtaler og MUS i ELOHVAC og Data Power. '
     'Ledelse af et 14-mands entrepriseteam hos Ventek-Air og et 12-mands værkstedsteam hos ARJ.'),
    ('Motiveres af at udvikle både mennesker og faglighed',
     'Dokumenteret i arbejdet. Oplæring af lærlinge og elektrikere, og struktureret MUS. Motivation i sig selv beskrives ikke her.'),
    ('Samarbejder stærkt på tværs og tør give kvalificeret modspil',
     'Dokumenteret. Tværfaglig koordinering af 25 specialister på tværs af engineering, indkøb og anlæg hos Novo Nordisk. '
     'Modspil i form af faglig kontrol før udsendelse af tilbud og dokumenter i ELOHVAC og Data Power.'),
    ('Kommunikerer klart og troværdigt',
     'Dokumenteret. Månedsrapportering til ledelse og bygherre, beslutningsoplæg og ledelsesrapportering i Data Power, og dansk og engelsk i skrift og tale.'),
    ('Trives med komplekse problemstillinger og kan omsætte overordnede mål til konkrete prioriteringer og handlinger',
     'Dokumenteret. Porteføljestyring af 37 CAPEX-projekter og 11 parallelle anlægsprojekter med én samlet plan, og strategi omsat til tavlemøder og flaskehalsanalyser.'),
    ('Sikre prioritering, kvalitet og fremdrift i de daglige forhandlinger',
     'Delvist dokumenteret. Prioritering, kvalitet og fremdrift i de daglige leverancer og tilbud hos Ventek-Air og ELOHVAC. '
     'Forhandlingsforløb med lægemiddelvirksomheder er ikke dokumenteret.'),
    ('Lede og udvikle medarbejderne med fokus på faglighed, motivation, trivsel og sparring',
     'Dokumenteret. Daglig planlægning, enkeltsamtaler, MUS og arbejdsmiljøopfølgning for 5 elektrikere og 3 lærlinge i ELOHVAC. '
     'Teamledelse i skiftehold hos Biofos og tværfaglig ledelse af 25 specialister hos Novo Nordisk.'),
    ('Omsætte Amgros strategi og mål til konkrete handlinger og resultater i teamet',
     'Delvist dokumenteret. Strategi omsat til handling i CAPEX-porteføljer og PDCA-programmer. Amgros-strategi og -mål er ikke kendt for mig ud over opslaget.'),
    ('Drive udviklingen af processer og governance for alternative aftaler fra vurdering og forhandling til implementering og opfølgning',
     'Delvist dokumenteret. Proces- og governancearbejde i ISO 9001-baseret kvalitetsstyring, afleveringsdokumentation og KS. '
     'Alternative aftaler, herunder managed entry, er ikke dokumenteret.'),
    ('Styrke det konkrete samarbejde med Medicinrådet om forhandling og alternative aftaler',
     'Ikke dokumenteret. Samarbejde med Medicinrådet er ikke i min erfaring. Myndighedskontakt og indberetning i reguleret sammenhæng er brugerbekræftet, men uden navngivne myndigheder.'),
    ('Bidrage til nye forhandlingsområder, herunder primærområdet og individuel ibrugtagning',
     'Ikke dokumenteret. Primærområdet og individuel ibrugtagning er ikke i min erfaring. Opbygning af nye arbejdsområder er dokumenteret i anlæg og projekter.'),
    ('Udvikle teamets forhandlingskompetencer og arbejdsformer',
     'Delvist dokumenteret. Udvikling af teamets arbejdsformer med tavlemøder, standardiserede arbejdsgange og Standard Work hos Ventek-Air og Biofos.'),
    ('Personaleansvar for fem medarbejdere på forhandlingsområdet',
     'Dokumenteret. Personaleansvar for 5 medarbejdere i ELOHVAC og Data Power, og ledelse af teams fra 12 til 25 personer.'),
]

KULTUR_PHRASES = [
    'Høj faglighed og professionalisme hånd i hånd med tillid',
    'tillid, nysgerrighed, mod, drive, sammenhold og humor',
    'tæt på medarbejderne og skabe de rammer',
    'give samtidig plads til, at medarbejderne tager ansvar, udfordrer hinanden og går forrest',
    'grundig, nysgerrig og modig',
    'bidrage til arbejdsglæde',
    'få strategien til at leve i hverdagen',
    'tør give kvalificeret modspil',
]


def write_inputs():
    with open(KRAV, 'w', encoding='utf-8') as f:
        f.write('# Krav fra Amgros · Teamleder til et forhandlingsområde i udvikling, dansk, ordret fra opslaget\n')
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
    m.meta('Amgros · Rådgivning og Forhandling · ansøgning senest 11. december 2026')
    m.para('Kære Marie Gerstrøm,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    def sub(text):
        p = m._p(spacing_after=20, spacing_before=60, line=260, justify=False, keep_next=True)
        m._run(p, text, bold=True, color='002B5C')
        return p

    # ------------------------------------------------------------ brev, side 1
    lp('Amgros står midt i en periode, hvor forhandlingen får større strategisk betydning. Nye rammevilkår, MFN, '
       'flere alternative aftaler og usikkerheden om nye lægemidlers effekt stiller krav til, hvordan teamet arbejder. '
       'Opgaven i stillingen er at få strategien til at leve i hverdagen i de daglige forhandlinger, uden at miste fremdriften i de sager, der allerede ligger på bordet. '
       'Det er den balance, jeg ser som kernen i rollen.')

    sub('Fra strategi til den enkelte sag')
    lp('Når et nyt lægemiddel nærmer sig Medicinrådet, skal teamet have en forhandlingsstrategi, der kan bæres af hele '
       'gruppen og ikke kun af den, der sidder med sagen. Det kræver faste prioriteringer, en klar fordeling af ansvar og en '
       'opfølgning, der kan se, om strategien holder, når den møder virkeligheden i forhandlingen. Jeg vil starte med at '
       'gøre den vurdering synlig for teamet, så prioriteringen også er den, der bliver fulgt.')

    sub('Alternative aftaler, som kan følges helt igennem')
    lp('Alternative aftalemodeller er kun så gode, som den proces, der fører til dem. Vurdering, forhandling, implementering '
       'og opfølgning skal være sammenhængende, ellers mister aftalen sin værdi i driften. Governance er derfor en del af '
       'arbejdet fra første dag, ikke et efterspil. Amgros-værdierne om at være grundig, nysgerrig og modig passer til den måde, '
       'aftalerne skal vurderes på. Samarbejdet med Medicinrådet skal ligeledes have faste rammer, så '
       'forventninger og beslutninger er afklaret, før de skal bruges.')

    sub('Mennesker og faglighed i samme team')
    lp('Fem medarbejdere med egen faglig tyngde har brug for en leder, der følger op, sparrer og prioriterer. '
       'Opslaget beskriver Høj faglighed og professionalisme hånd i hånd med tillid, og en kultur med tillid, nysgerrighed, mod, drive, sammenhold og humor. '
       'Som leder skal jeg være tæt på medarbejderne og skabe de rammer, der gør det muligt at lykkes, og give samtidig plads til, at medarbejderne tager ansvar, '
       'udfordrer hinanden og går forrest. Det er samtidig den ramme, der gør det muligt at bidrage til arbejdsglæde i teamet.')

    sub('Det, der er nyt for mig')
    lp('Forhandling af lægemiddelpriser, markedskendskab til lægemiddelområdet, MFN og alternative aftaler, samarbejdet med '
       'Medicinrådet og primærområdet er ikke en del af min dokumenterede erfaring. Min erfaring med udbud, tilbud, aftalegrundlag '
       'og styring af fremdrift og økonomi er reel, men den er fra andre markeder. Jeg vil bruge den første tid på at lære '
       'lægemiddelmarkedet og forhandlingerne sammen med teamet.')

    lp('Jeg vil gerne tale om, hvilke sager der har størst presserende behov i den kommende periode, og hvordan teamets '
       'prioriteringer skal se ud, når der kommer nye rammevilkår.', after=44)
    lp('Med venlig hilsen', after=8)
    lp('Shahram Ajloo', after=8)

    # ------------------------------------------------------------ CV, side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Elautoriseret maskinmester (LV/MV/HV) med mindst tre års projekt- og personaleledelse. Ledelse af teams fra fem til 25 '
           'personer, 37 samtidige CAPEX-projekter hos Novo Nordisk og 11 parallelle anlægsprojekter hos Ventek-Air. '
           'Erfaring med udbud, tilbud og aftalegrundlag, og styring af prioritering, fremdrift og økonomi. Forhandling af '
           'lægemiddelpriser og markedskendskab er ikke dokumenteret. PRINCE2-certificeret. Dansk og engelsk.', after=32)

    m.section('LEDELSE OG UDVIKLING AF MEDARBEJDERE')
    tasks = [
        ('Personaleledelse',
         'Personaleledelse af 5 elektrikere og 3 lærlinge i ELOHVAC og Data Power med daglig planlægning, enkeltsamtaler, MUS og oplæring.'),
        ('Teamledelse',
         'Ledelse af et 14-mands entrepriseteam hos Ventek-Air og et 12-mands værkstedsteam hos ARJ. Teamledelse i skiftehold hos Biofos.'),
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
         'PDCA-program med 40 % lavere energiomkostninger hos Novo Nordisk. Daglige tavlemøder og flaskehalsanalyser hos Ventek-Air.'),
        ('Governance',
         'ISO 9001-baseret kvalitetsstyring med audits, afleveringsdokumentation og KS-opfølgning i ELOHVAC.'),
        ('Udbud og aftaler',
         'Udbud, tilbud og aftalegrundlag hos Ventek-Air og ELOHVAC. Prisopfølgning og kalkulation i SAP ERP hos Novo Nordisk.'),
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
         [('', 'Drift og vedligehold af pumper, HVAC, højspændingstavler og SCADA i døgndrift.'),
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
        ('Ledelse', 'Personaleledelse, MUS, enkeltsamtaler, situationsbestemt ledelse (SLII), RACI, interessentanalyse'),
        ('Salg og kommerciel styring', 'Salgsledelse (brugerbekræftet generelt), udbud og tilbud, kalkulation'),
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

    m.save(path, title='Teamleder til et forhandlingsområde i udvikling - Amgros',
           subject='Ansøgning Teamleder til et forhandlingsområde i udvikling')
    print(path)


if __name__ == '__main__':
    os.makedirs(OUT_DIR, exist_ok=True)
    write_inputs()
    build(OUT)
