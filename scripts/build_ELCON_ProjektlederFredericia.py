# -*- coding: utf-8 -*-
"""
ELCON — projektleder, større el-entrepriseprojekter, Fredericia.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Projektleder | El-entreprise, økonomi og ledelse tæt på byggepladsen'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = '2. november 2026'
RECIPIENT = 'ELCON · Entreprisedivisionen · Entreprisechef Brian Frost · Fredericia'
SUBJECT = 'Ansøgning: Projektleder til større el-entrepriseprojekter — Fredericia'

# ------------------------------------------------------------------ side 1
INTRO = ['På en byggeplads hænger teknik og økonomi uløseligt sammen. En manglende afklaring kan koste både '
 'timer, materialer og tillid hos kunden. Derfor skal ELCONs projekter i Syddanmark og på Fyn have en '
 'projektleder, der følger arbejdet tæt, får beslutningerne på plads og kender økonomien bag den '
 'tekniske løsning.',
 'Hos ELCON vil jeg samle styringen om fire ting: et klart aftalegrundlag, en plan de udførende kan '
 'arbejde efter, løbende økonomiopfølgning og KS, der følger arbejdet helt frem til aflevering. Det er '
 'samme sammenhæng mellem kunde, materialer, medarbejdere og leverance, som jeg arbejder med i ELOHVAC, '
 'hvor jeg har fuldt P&L-ansvar.']

BULLETS = [('Afklaringer før udførelse',
  'Ved opstart gennemgår jeg tegninger, leverancegrænser og åbne spørgsmål med kunden, rådgivere og '
  'byggeledelse. Hvem leverer hvad, og hvad skal være afklaret, før arbejdet kan begynde? De spørgsmål '
  'skal have et svar, en ansvarlig og en dato, så tvivlen ikke ender hos elektrikeren på pladsen.'),
 ('En plan, der holder på pladsen',
  'Bemanding, materialer, adgang og andre fags arbejde skal passe sammen. Korte tavlemøder og '
  'pladsrunder giver mulighed for at opdage det, der spænder ben, mens der stadig er tid til at gøre '
  'noget ved det. Fra Ventek-Air har jeg erfaring med kapacitetsstyring og flaskehalsanalyse på 11 '
  'samtidige projekter med et team på 14 medarbejdere.'),
 ('Økonomi uden overraskelser',
  'Jeg vil følge forbrug og disponeringer sammen med det, der mangler for at gøre projektet færdigt. '
  'Ændringer og ekstraarbejder skal beskrives, prissættes og følges op efter den aftalte '
  'godkendelsesvej. Erfaringen kommer fra eget entrepriseansvar og fra Novo Nordisk, hvor jeg fulgte '
  'økonomi, risici og fremdrift på 37 CAPEX-projekter.'),
 ('Kvalitet hele vejen til aflevering',
  'KS og test skal ind i planen fra begyndelsen. Mangler skal opdages, mens de kan rettes ordentligt, '
  'og dokumentationen skal passe til det udførte arbejde. Hos Novo indgik FAT/SAT og IQ/OQ/PQ i '
  'afleveringen under GMP/FDA/EMA, uden kritiske fund. Hos ELOHVAC omfatter ansvaret både KS og det '
  'grundlag, kunden får ved aflevering.')]

SYSTEM = ('Den første tid vil jeg bruge sammen med entreprisechefen og projektteamet på at lære de aktuelle '
 'projekter at kende. Derefter skal vi have et fælles overblik over økonomi, tidsplan og de '
 'afklaringer, der haster mest. På sidste side har jeg beskrevet, hvordan jeg vil gribe de første 90 '
 'dage an.')

MIRROR = ('Det el-tekniske fundament er min uddannelse som maskinmester og elautorisationen LV/MV/HV. I ELOHVAC '
 'leder jeg 5 elektrikere og 3 lærlinge og arbejder med tilbud, planlægning, materialer og '
 'underentreprenører. Tidligere har jeg koordineret 25 specialister hos Novo Nordisk. Det har lært mig '
 'at give tydelig retning og samtidig bruge de fagfolk, der ved mest om den enkelte opgave.')

HONEST = ('Teknikken skal kunne forklares, og aftaler skal kunne holdes. Det er sådan, jeg læser ELCONs vægt på '
 'ordentlighed, tillid og samarbejde. Jeres faglige miljø med projektlederkolleger og specialister er '
 'også vigtigt: gode løsninger bliver bedre af at blive vendt med andre.')

CULTURE = ('Jeg bruger selv digitalisering dér, hvor den gør hverdagen lettere. Som professionel Claude-bruger og '
 'koder har jeg bygget Python/Claude API-værktøjer til tilbud, planlægning, KS og KPI-opfølgning. Det '
 'har givet over 40 % produktivitetsløft i entreprisedriften. Hos ELCON skal den slags værktøjer passe '
 'til jeres systemer, med godkendt brug af data og faglig kontrol.')

PRACTICAL = ('Jeg bor i Måløv. Derfor skal vi finde en holdbar aftale om min tilstedeværelse i Fredericia og på '
 'byggepladserne i Syddanmark og på Fyn. Startdato og overgangen fra ELOHVAC skal også aftales; jeg har '
 'ikke forudsat flytning eller hjemmearbejde.')

CLOSING = ('Jeg vil gerne tale med jer om de projekter, der venter, og om hvordan jeg bedst kan bidrage med '
 'el-teknisk erfaring, økonomisk ansvar og ledelse tæt på de udførende.')

# ------------------------------------------------------------------ CV
PROFILE = ('Større el-entrepriser kræver en projektleder, der kan få teknik, folk og økonomi til at hænge sammen. '
 'Elautoriseret maskinmester (LV/MV/HV) med erfaring fra tilbud og beregning til udførelse, KS og '
 'aflevering. I ELOHVAC omfatter ansvaret fuldt P&L, kunder, underentreprenører og ledelse af 5 '
 'elektrikere og 3 lærlinge. Hos Ventek-Air gjaldt det 11 samtidige projekter og et team på 14. Hos '
 'Novo Nordisk koordinerede jeg 25 specialister på 37 CAPEX-projekter. Jeg bygger desuden Python/Claude '
 'API-værktøjer, der har gjort tilbud, planlægning og kvalitetsopfølgning mere effektive.')

PRACTICE = [('Ansvar fra tilbud til aflevering',
  'ELOHVAC: beregning, planlægning, materialer og underentreprenører på el-, ventilations- og '
  'klimaanlæg. Ansvar for kundedialog, projektøkonomi, kvalitet og afleveringsdokumentation.'),
 ('Overblik over økonomi og risici',
  'Novo Nordisk: opfølgning på økonomi, fremdrift, risici og ressourcer med månedsrapportering til '
  'ledelse og bygherre. SAP blev brugt til økonomi, aktiver og omkostninger.'),
 ('Koordinering på byggepladsen',
  'Ventek-Air: 11 projekter fra specifikation til formel aflevering. Daglige tavlemøder, '
  'kapacitetsstyring og flaskehalsanalyse hjalp med at holde opgaver og bemanding samlet.'),
 ('Ledelse af elektrikere og lærlinge',
  'ELOHVAC: daglig opgavefordeling, 1:1/MUS og struktureret oplæring. Situationsbestemt ledelse med '
  'forskellig støtte til den erfarne elektriker og lærlingen. LOTO, APV og risikovurdering er en del af '
  'arbejdet.'),
 ('Teknisk kvalitet og samarbejde',
  'Novo: elsystemer, UPS og nødbelysning samt samarbejde på tværs af engineering, indkøb og anlæg. '
  'FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA med nul kritiske fund ved aflevering.'),
 ('Forbedringer, der kan bruges i hverdagen',
  'Erfaring med PDCA, A3, 5xHvorfor og 5S. Egne Python/Claude API-værktøjer til beregning, tidsplaner, '
  'KS og KPI har givet over 40 % produktivitetsløft i entreprisedrift.')]

MODELS = [('Ved opstart',
  'Gennemgå aftaler, tegninger og grænseflader. En enkel ansvarsmatrix (RACI) kan bruges, hvis det er '
  'uklart, hvem der beslutter eller leverer.'),
 ('Under udførelsen',
  'Rullende plan for bemanding, materialer og adgang. Tavlemøder og pladsrunder bruges til at få '
  'hindringer fjernet, ikke blot noteret.'),
 ('Økonomi og ændringer',
  'Følg budget, disponeringer, forbrug og restbudget. Hold styr på ekstraarbejder og på, hvad der er '
  'tilbudt, aftalt og godkendt.'),
 ('KS og aflevering',
  'Planlæg test, kontroller og dokumentation sammen med arbejdet. Følg mangler til dørs og afstem '
  'accept med de ansvarlige fagpersoner.'),
 ('Når fejl gentager sig',
  'Brug PDCA, A3 og 5xHvorfor til at finde årsagen. Kontrollér bagefter, om løsningen faktisk har '
  'fjernet problemet.'),
 ('Ledelse og sparring',
  'Byg videre på 1:1/MUS og oplæring. GROW/SBI kan bruges til konkrete udviklingssamtaler og feedback; '
  'anvendelsen aftales efter behov.')]

ACHIEVEMENTS = [('37 samtidige CAPEX-projekter hos Novo Nordisk',
  'DKK 2–10 mio. pr. projekt og koordinering af 25 specialister. Reguleret aflevering uden kritiske '
  'fund.'),
 ('11 samtidige projekter hos Ventek-Air',
  'Et team på 14 medarbejdere med ansvar fra specifikation til aflevering.'),
 ('Fuldt P&L i ELOHVAC', 'Entrepriseansvar og direkte ledelse af 5 elektrikere og 3 lærlinge.'),
 ('Over 40 % produktivitetsløft',
  'Egne Python/Claude API-værktøjer til tilbud, planlægning, KS og KPI i entreprisedrift.')]

EXPERIENCE = [('Indehaver / teknisk direktør / elautoriseret maskinmester',
  'ELOHVAC ApS · København · maj 2023 – nu',
  '5 elektrikere og 3 lærlinge · fuldt P&L',
  [('Entreprise og kunder',
    'Tilbud og beregning, planlægning, materialer og underentreprenører. KS og aflevering af el-, '
    'ventilations- og klimaanlæg.'),
   ('Medarbejdere og sikkerhed',
    'Daglig planlægning, 1:1/MUS og oplæring af lærlinge. LOTO, APV og risikovurdering; ingen kritiske '
    'afvigelser i serviceaftalerne.'),
   ('Egne digitale værktøjer',
    'Python/Claude API til tilbud, tidsplaner, KS og KPI-opfølgning. Produktivitetsløft på over 40 '
    '%.')]),
 ('Senior idriftsættelsesingeniør / projektleder, elsystem',
  'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
  '37 samtidige CAPEX-projekter, DKK 2–10 mio. pr. projekt · koordinering af 25 specialister',
  [('Projektledelse',
    'Opfølgning på fremdrift, økonomi, risici og ressourcer på tværs af engineering, indkøb og anlæg. '
    'Rapportering til ledelse og bygherre.'),
   ('Aflevering og forbedringer',
    'FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA uden kritiske fund ved aflevering. PDCA-program gav 40 % '
    'lavere energiomkostninger. SAP til økonomi og aktiver.')]),
 ('Projekt- og værkstedsleder',
  'Ventek-Air · København · jan. 2022 – nov. 2022',
  '11 samtidige projekter · team på 14 medarbejdere',
  [('Fra specifikation til aflevering',
    'Tilbud, underentreprenører samt sikkerheds- og afleveringsdokumentation. Daglige tavlemøder, '
    'kapacitetsstyring og flaskehalsanalyse.')]),
 ('Vedligeholdelses- og driftsleder / værkstedstekniker',
  'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
  'Kritisk 24/7-drift · pumper, HVAC, højspændingstavler og SCADA',
  [('Drift og vedligehold',
    'Forebyggende vedligehold, akut fejlfinding og reservedelsflow. 5S, Standard Work og PDCA på '
    'værksted og lager; LOTO, APV og opfølgning på nærved-hændelser.')]),
 ('Elektromekaniker / produktionsteamleder',
  'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
  '12 mekanikere og teknikere',
  [('Ledelse og fejlfinding',
    'Vagtplanlægning, materialer og opfølgning på mål. Fejldiagnose, rodårsagsanalyse og reparation af '
    'industrielle el- og mekaniske anlæg.')])]

EDUCATION = [
    ("B.Tech (EQF niveau 6) — Technology Management & Mechanical Engineering",
     "Maskinmesterskolen / Copenhagen School of Marine Engineering & Technology Management · "
     "2017 – 2022 · karakter 7,6/12"),
    ("El- og maskinteknisk design, elteknik (EQF niveau 6)",
     "Tehran Technical University · 2000 – 2003"),
    ("HF — matematik og fysik",
     "VUC · 2012 – 2017"),
]

CERTS = [('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023'),
 ('Køleteknik & klimaanlæg (AMU)', 'Mercantec · 2021'),
 ('Lean-praksis: 5S, PDCA, VSM, A3 og Kaizen', 'Anvendt i drift og projekter'),
 ('STCW: sikkerhed og maskinrumsvagt', 'Søfartsstyrelsen · 2021–2023')]

LANGUAGES = ("Dansk (modersmål, skrift og tale) · Engelsk (professionelt, skrift og tale) · "
             "Persisk/farsi · Kørekort B (kategori B)")

PRACTICAL_CV = ('Bopæl i Måløv (Ballerup Kommune). Rollen har base i Fredericia og omfatter byggepladser i Syddanmark '
 'og på Fyn. En ordning for tilstedeværelse, eventuelt ophold og rejser skal aftales sammen med '
 'startdato og overgangen fra ELOHVAC. Dansk og persisk/farsi på modersmålsniveau; engelsk '
 'professionelt i skrift og tale. Kørekort B. Elautoriseret maskinmester (LV/MV/HV).')

REFERENCES = 'Tidligere ledere hos Novo Nordisk og Biofos (Lynetten) — oplyses efter aftale.'

PARTNER = [('Entreprisechef og projektlederkolleger',
  'Jeg vil afklare, hvilke økonomiske og bemandingsmæssige beslutninger jeg selv kan træffe, og hvornår '
  'jeg skal tage en sag videre. Ved problemer skal entreprisechefen have både konsekvensen og '
  'realistiske muligheder at vælge mellem.'),
 ('Kunder, rådgivere og byggeledelse',
  'Tekniske spørgsmål og ændringer skal drøftes, mens der er tid til at handle. Korte referater med '
  'ansvar og dato gør det lettere at holde aftalerne. Betydningen for pris, tid og kvalitet skal være '
  'tydelig for alle parter.'),
 ('Udførende medarbejdere og samarbejdspartnere',
  'Opgaverne skal kunne udføres på det aftalte grundlag. Jeg vil lytte til de hindringer, medarbejderne '
  'møder, og følge op på materialer, adgang, sikkerhed og kvalitet. Det er her, planens svagheder ofte '
  'bliver opdaget først.'),
 ('Specialister og dokumentansvarlige',
  'Faglig sparring skal bruges, når den gør løsningen bedre eller reducerer en risiko. Test og '
  'dokumentation skal følge det udførte arbejde. Afleveringen bliver lettere, når materialet er samlet '
  'undervejs i stedet for i de sidste dage.')]

FIRST90 = [('Første uge',
  'Møde med Brian Frost og projektteamet om de opgaver, jeg overtager, og det ansvar der følger med. '
  'Besøge byggepladserne og tale med de udførende. Gennemgå aftaler, tegninger, bemanding og de '
  'nærmeste milepæle. Ved ugens slutning skal de vigtigste åbne spørgsmål have en ansvarlig og en '
  'aftalt frist.'),
 ('Inden dag 30',
  'Gennemgå budget, disponeringer og restbudget for de aftalte projekter. Sammenholde økonomien med '
  'tidsplanen og arbejdet på pladsen. Afklare grænseflader med kunder, rådgivere og byggeledelse. Vi '
  'skal kunne se, hvilke leverancer der er i fare, hvad der mangler, og hvornår KS og test skal '
  'udføres.'),
 ('Inden dag 60',
  'Have en fast rytme for pladsbesøg, økonomiopfølgning og gennemgang af ændringer. Følge en konkret '
  'teknisk afklaring helt frem til udført og kontrolleret arbejde. Bruge forløbet til at se, om '
  'beslutninger, tegninger og materialer når frem til de rigtige personer i tide, og rette det der ikke '
  'fungerer.'),
 ('Inden dag 90',
  'Gennemgå projekternes økonomi og fremdrift med entreprisechefen. Se på åbne ekstraarbejder, '
  'forsinkelser og mangler i dokumentationen. Aftale de næste forbedringer og dele erfaringerne med '
  'projektlederkolleger. Målene skal tage udgangspunkt i projekternes faktiske tilstand, ikke et '
  'generelt løfte om en bestemt besparelse.')]

KEYWORDS = ('El-entreprise og el-teknisk projektledelse · Projektøkonomi og planlægning · Koordinering på '
 'byggepladser · Kunder, rådgivere og samarbejdspartnere · Samarbejde med byggeledelse og udførende '
 'medarbejdere · Teknisk løsning, KS og aflevering · Faglig sparring, oplæring og videndeling.')


def build(path):
    m = MasterDoc(TEMPLATE, lang="da-DK")

    # ---------------------------------------------------------------- side 1
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta(RECIPIENT)

    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, SUBJECT, bold=True, color="1A1A1A")

    for t in INTRO:
        m.para(t, after=64, line=232)

    for label, body in BULLETS:
        m.bullet(label, body, after=10, line=228)

    m.para(SYSTEM, after=50, line=226)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=10, line=222)

    m.meta("Med venlig hilsen · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "TEKNISK PROFIL")
    m.para(PROFILE, after=80)

    m.section("ERFARING, DER PASSER TIL OPGAVEN")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("PROJEKTSTYRING — OPSTART, UDFØRELSE OG AFLEVERING",
                   ("Område", "Metoder og værktøjer"), MODELS)

    m.section("UDVALGTE RESULTATER")
    for label, body in ACHIEVEMENTS:
        m.bullet(label, body, after=30)

    m.page_break()
    m.section("ERHVERVSERFARING")
    for title, meta, scope, bullets in EXPERIENCE:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=30)

    m.section("UDDANNELSE")
    for t, meta in EDUCATION:
        m.edu(t, meta)

    m.section("AUTORISATIONER & CERTIFICERINGER")
    for _i, (t, meta) in enumerate(CERTS):
        _p_ = m.edu(t, meta)
        if _i < len(CERTS) - 1:
            _p_.paragraph_format.keep_with_next = True

    m.section("SPROG")
    m.para(LANGUAGES, after=80, justify=False)

    m.section("FAGLIGT FOKUS")
    m.para(KEYWORDS, after=80)

    # afsluttende side
    m.page_break()
    m.models_table("FØRSTE 90 DAGE — PROJEKTGRUNDLAG, ØKONOMI OG FREMDRIFT",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SAMARBEJDET OM PROJEKTERNE")
    for label, body in PARTNER:
        m.bullet(label, body, after=30)

    m.section("ÆNDRINGSKONTROL — TEKNIK, TID OG ØKONOMI")
    m.para("Et ekstraarbejde skal kunne følges fra den første besked til den færdige løsning. Først skal det være klart, hvad der er ændret, hvem der tager stilling, og hvad det betyder for materialer, timer og tidsplan. Derefter skal aftalen og godkendelsesstatus fremgå, så de udførende ved, hvilket grundlag de arbejder efter. Jeg vil følge ændringen ind i restbudgettet og kontrollere, at tegninger og afleveringsmateriale følger den udførte løsning. Der er forskel på at have varslet en konsekvens, afgivet et tilbud og fået en aftale på plads. Den forskel skal holdes tydelig efter projektets kontraktgrundlag, også når tempoet er højt.", after=80)

    m.section("PRAKTISKE FORHOLD")
    m.para(PRACTICAL_CV, after=80)

    m.section("REFERENCER")
    m.para(REFERENCES, after=80, justify=False)

    # ingen afsnit eller tabelrække må knække over en sideskift
    for _p in m.doc.paragraphs:
        _p.paragraph_format.keep_together = True
    for _tbl in m.doc.tables:
        for _row in _tbl.rows:
            for _c in _row.cells:
                for _p in _c.paragraphs:
                    _p.paragraph_format.keep_together = True

    from docx.oxml import OxmlElement as _OE
    for _tbl in m.doc.tables:
        for _tr in _tbl._tbl.tr_lst:
            _pr = _tr.get_or_add_trPr()
            _el = _OE("w:cantSplit")
            _pr.append(_el)

    m.save(path)


if __name__ == "__main__":
    build(os.path.join(ROOT, "Shahram_Ajloo_ELCON_ProjektlederFredericia.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_ELCON_ProjektlederFredericia.docx"))
