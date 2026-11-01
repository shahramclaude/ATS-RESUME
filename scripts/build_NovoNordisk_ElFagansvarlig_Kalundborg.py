# -*- coding: utf-8 -*-
"""Novo Nordisk job 346295: el-fagligt ansvar i Manufacturing II. Masterdesign, dansk."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'El-faglig ansvarlig | Elautoriseret maskinmester (LV/MV/HV) | Manufacturing II, Kalundborg'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = 'Novo Nordisk · Manufacturing II, Kalundborg · Att. Lars Lund Hansen'
SUBJECT = 'Ansøgning: El-Installatør og Fagansvarlig — job-ID 346295'

# ------------------------------------------------------------------ side 1
INTRO = ['Elektrisk pålidelighed i API-produktion begynder før en fejl stopper anlægget. Den kræver '
 'overblik over installationernes tilstand, en vedligeholdsplan styret af risiko og et '
 'kvalitetsledelsessystem, der virker i den daglige praksis. Nye installationer skal kunne '
 'overtages sikkert af vedligeholdelsen, mens eksisterende installationer holdes lovlige, '
 'dokumenterede og tilgængelige for produktionen.',
 'Opgaven i Manufacturing II løses derfor med ét sammenhængende system: anlægsregister med '
 'kritikalitet, lovkravs- og kontrolmatrix, risikobaseret vedligehold, sikker ibrugtagning og '
 'afvigelser, der følges til verificeret lukning. Arbejdsmodellen nedenfor forbinder det '
 'el-faglige ansvar med produktionens behov — med sikkerhed og kvalitet som forudsætninger for '
 'højere produktionsoutput.']

BULLETS = [('Kravet: stærk el-faglig baggrund og praktisk installationserfaring',
  'Svaret på opslagets uddannelseskrav er elautoriseret maskinmester (LV/MV/HV), med '
  'elektriker-/elektromekanikerbaggrund og praktisk arbejde med installationer, tavler, styring og '
  'fejlfinding. Rollen skal bruge fagligheden på anlægget og i dokumentationen, ikke blot i en '
  'godkendelsesfunktion. Den konkrete formelle ansvarsplacering afklares ved ansættelsen.'),
 ('Kravet: understøtte nye installationer og ibrugtagning',
  'Løsningen er en overdragelsesgate med kravgrundlag, kontrolplan, testresultater, ajourført '
  'dokumentation og driftsaccept før frigivelse. Vedligeholdelsen inddrages før designet låses. '
  'Erfaring med FAT/SAT og IQ/OQ/PQ i 37 CAPEX-projekter hos Novo Nordisk giver et konkret '
  'fundament for en aflevering uden kritiske fund.'),
 ('Kravet: understøtte vedligeholdelse af eksisterende installationer',
  'Løsningen er et anlægskort med kritikalitet, tilstand, fejlforløb og næste kontrol. SAP-data og '
  'driftsobservationer bruges til at prioritere indsatsen efter konsekvens og sandsynlighed. '
  'Gentagne fejl behandles med A3, 5xHvorfor og korrigerende handlinger frem for endnu en '
  'midlertidig reparation.'),
 ('Kravet: tilsyn og et sundt og sikkert arbejdsmiljø',
  'Løsningen er planlagt tilsyn med risikovurdering, arbejdstilladelse og sikker isolering/LOTO '
  'før indgreb. Arbejdets omfang, kompetencer og grænseflader afklares ved opstart; afvigelser og '
  'nærved-hændelser omsættes til handlinger med ejer og frist. Produktionens tidspres ændrer ikke '
  'betingelserne for sikkert arbejde.'),
 ('Kravet: et effektivt kvalitetsledelsessystem for lovkrav',
  'Løsningen er en lovkravsmatrix, som forbinder gældende krav med anlæg, procedure, ansvarlig, '
  'kontrolinterval og dokumentationsbevis. Egenkontrol, kompetenceopfølgning, ændringsstyring og '
  'auditfund samles i et fast årshjul. Det el-faglige kvalitetsledelsessystem kobles til sitets '
  'QMS uden at forveksle elsikkerhed med GMP-kvalificering.'),
 ('Kravet: udføre termografering af eltavler',
  'Løsningen er et planlagt termografiforløb med entydigt tavle-ID, sikker adgang, dokumenteret '
  'belastning, målebetingelser, termobillede og visuel reference. Fund prioriteres fagligt, får en '
  'ansvarlig og efterkontrolleres efter udbedring. Selvstændig udførelse forudsætter dokumenteret '
  'metodekompetence og oplæring i sitets udstyr og procedurer.'),
 ('Kravet: forbedre, optimere og standardisere vedligeholdelsen',
  'Løsningen er PDCA med fælles jobplaner, kontrolpunkter og fejlkoder på tværs af '
  'produktionsområderne. En forbedring afprøves i afgrænset skala og vurderes på nedetid, gentagne '
  'fejl og planopfyldelse, før den udbredes. Standarder skal være brugbare for teknikeren og '
  'understøtte lovkrav, ikke skabe ekstra papirarbejde.'),
 ('Kravet: selvstændigt ansvar og samarbejde på tværs',
  'Løsningen er tydelige beslutningsgrænser og en daglig prioritering med produktion og '
  'vedligehold: sikkerhed, kvalitetsrisiko, driftskritikalitet og næste handling. Kolleger og '
  'interessenter inddrages tidligt, når prioriteringer ændres. Tekniske spørgsmål forklares på '
  'dansk og engelsk med konsekvens, anbefaling og beslutningsbehov.')]

SYSTEM = ('Det digitale fundament er anlægs- og kontroldata i godkendte systemer, suppleret med Excel, '
 'Power BI og Python til analyse og opfølgning. Som professionel Claude-bruger og koder bygger jeg '
 'tjeklister, beregningsmodeller og rapporteringsflow; brug i Novo Nordisk skal ske efter gældende '
 'data-, IT- og kvalitetsregler. Ingen fortrolige produktionsdata lægges i eksterne AI-tjenester '
 'uden godkendelse, og faglige konklusioner verificeres.')

MIRROR = ('Relevant evidens: elautoriseret maskinmester, B.Tech i teknologiledelse og maskinteknik, '
 'el-teknisk entrepriseansvar, 24/7-drift med højspænding, pumper og SCADA samt tidligere '
 'ansættelse hos Novo Nordisk i Kalundborg/Bagsværd. 37 samtidige anlægsprojekter, koordinering af '
 '25 specialister og nul kritiske afvigelser ved aflevering forbinder installation, kvalitet og '
 'samarbejde.')

HONEST = ('Afgrænsning: dokumenteret erfaring med selvstændig termografering eller termografcertificering '
 'foreligger ikke i mit CV. Den kompetence skal derfor afklares og om nødvendigt opbygges før '
 'selvstændige målinger. Tidligere Novo-erfaring erstatter heller ikke oplæring i Manufacturing '
 'II, de aktuelle lovkravsprocedurer eller en formel vurdering af fagansvaret.')

CULTURE = ('Novo Nordisk Way forbinder et sundt og engagerende arbejdsmiljø med kvalitet uden kompromis. I '
 'denne rolle betyder det at reagere på el-faglige afvigelser, gøre risiko synlig og skabe en '
 'enkel kontrolpraksis, som kollegerne kan følge. Et sikkert og pålideligt produktionsanlæg er '
 'ikke et mål adskilt fra patienterne; det er en del af forudsætningen for stabil levering.')

PRACTICAL = ('Bosat i Måløv, kørekort B; tidligere arbejde i Kalundborg er en relevant praktisk '
 'referenceramme. Dansk på modersmålsniveau og professionelt engelsk. Tiltrædelse og rammerne for '
 'den eksisterende virksomhed aftales før ansættelse.')

CLOSING = ('En første drøftelse kan tage udgangspunkt i ét kritisk tavleanlæg: Hvad ved vi om tilstanden, '
 'hvad kræver kontrollen, og hvilke handlinger beskytter både mennesker og produktion?')

# ------------------------------------------------------------------ CV
PROFILE = ('Manufacturing II har brug for el-fagligt ansvar, der forbinder sikre installationer med stabil '
 'API-produktion. Relevant erfaring dækker elektriske installationer, tavler og styring i egen '
 'virksomhed, idriftsættelse af elsystemer hos Novo Nordisk og kritisk el- og mekanisk drift hos '
 'Biofos. Elautoriseret maskinmester (LV/MV/HV), B.Tech i teknologiledelse og maskinteknik, med '
 'praktisk installationsbaggrund og tværfaglig koordinering. Erfaring med FAT/SAT, IQ/OQ/PQ, '
 'GMP-dokumentation, SAP, LOTO, APV og risikovurdering. Professionel Claude-bruger og koder med '
 'egne Python/Claude API-værktøjer til planlægning, kvalitetssikring og KPI-opfølgning. Fokus er '
 'faglig ledelse og anlæggenes livscyklus — ikke et krav om personaleansvar.')

PRACTICE = [('Elektriske installationer og life cycle management',
  'Anvendelse i rollen: anlægsregister, kritikalitet, tilstand og kontrolbehov for '
  'produktionsudstyr og faciliteter. Vedligehold, ændringer og overdragelse ses som én '
  'livscyklus.'),
 ('Ibrugtagning og kvalitet',
  'Evidens: 37 CAPEX-projekter med FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA; nul kritiske afvigelser '
  'ved aflevering. Anvendelse: dokumenteret kontrolgrundlag, driftsaccept og ajourført teknisk '
  'dokumentation.'),
 ('Forebyggende vedligehold og fejlfinding',
  'Evidens: pumper, HVAC, højspændingstavler og SCADA i 24/7-drift. PDCA, A3, 5xHvorfor og '
  'Ishikawa bruges til at skelne symptomer fra årsager og følge korrigerende handlinger.'),
 ('Tilsyn, arbejdsmiljø og lovkrav',
  'Evidens: LOTO, APV, risikovurdering og arbejdsmiljøopfølgning. Foreslået praksis: '
  'lovkravsmatrix og årshjul med kompetencer, kontrolbeviser, afvigelser og verificeret lukning.'),
 ('Termografering — plan og kompetenceafklaring',
  'Foreslået praksis: tavle-ID, belastning og målebetingelser, termisk/visuel dokumentation, '
  'faglig prioritering og efterkontrol. Ikke angivet som eksisterende certificering eller '
  'dokumenteret selvstændig erfaring.'),
 ('Standardisering og digital opfølgning',
  'Fælles jobplaner og fejlkoder, KPI for nedetid og gentagne fejl samt PDCA-opfølgning. SAP, '
  'Power BI og Python anvendes med godkendt datagrundlag; Claude-arbejde underlagt virksomhedens '
  'regler og menneskelig kontrol.')]

MODELS = [('Anlægs- og risikokort',
  'Anlægs-ID, forsyning, kritikalitet, tilstand, dokumentationsstatus, vedligeholdsbehov og '
  'ansvarlig. Understøtter prioritering af eksisterende og nye installationer.'),
 ('Lovkrav og kvalitetsledelse',
  'Krav/procedure/kontrol/bevis/ansvarlig i én matrix; ændringsstyring, kompetencematrix, '
  'egenkontrol og auditopfølgning. Aktuelle retningslinjer og lovgivning styrer kontrollen.'),
 ('Sikkert arbejde og tilsyn',
  'Risikovurdering, arbejdstilladelser, LOTO, kompetence- og entreprenørkontrol, tilsyn og '
  'nærved-opfølgning. Frigivelse og tilbagelevering aftales med produktionen.'),
 ('Vedligehold og forbedring',
  'Risikobaserede jobplaner, fejlregistrering og SAP-opfølgning; A3, 5xHvorfor, Ishikawa og PDCA. '
  'Gentagne fejl, nedetid og planopfyldelse bruges som effektmål.'),
 ('Termografi og fund',
  'Tavle-ID, belastning, målebetingelser, termobillede og visuel reference; fund med prioritet, '
  'ansvarlig og frist, efterfulgt af kontrol efter udbedring. Kompetenceafklaring før udførelse.'),
 ('Ibrugtagning og overdragelse',
  'Kravgrundlag, kontrol- og testplan, afvigelseslukning, FAT/SAT hvor relevant, teknisk '
  'dokumentation og driftsaccept; relevante GMP-krav håndteres i sitets kvalitetsprocesser.')]

ACHIEVEMENTS = [('37 samtidige CAPEX-projekter',
  '2–10 mio. kr. pr. projekt; koordinering af 25 specialister og aflevering uden kritiske '
  'afvigelser under GMP/FDA/EMA.'),
 ('11 parallelle installationsprojekter',
  'Ventilation og klima fra specifikation til formel aflevering; 14-personers team med kapacitets- '
  'og fremdriftsstyring.'),
 ('40 % lavere energiomkostninger',
  'PDCA-baseret forbedringsprogram i reguleret produktion; SAP anvendt til økonomi-, aktiv- og '
  'omkostningsopfølgning.'),
 ('Over 40 % produktivitetsløft',
  'Egne Python/Claude API-værktøjer til tilbud, tidsplaner, KS-tjeklister og KPI-dashboards i '
  'ELOHVAC.')]

EXPERIENCE = [('Indehaver / Teknisk direktør / Elautoriseret maskinmester',
  'ELOHVAC ApS · København · maj 2023 – nu',
  '5 elektrikere og 3 lærlinge · fuldt P&L',
  [('Installation, kvalitet og sikkerhed',
    'El-tekniske opgaver for erhvervskunder: installation, tavler, styring, fejlfinding og '
    'forebyggende vedligehold på el-, ventilations- og klimaanlæg. LOTO, APV og risikovurdering; '
    'nul kritiske afvigelser i serviceaftalerne.'),
   ('Faglig ledelse og værktøjer',
    'Daglig planlægning og oplæring af 5 elektrikere og 3 lærlinge; KS og '
    'afleveringsdokumentation. Python/Claude API til tilbud, tidsplaner, tjeklister og KPI; over '
    '40 % produktivitetsløft.')]),
 ('Senior idriftsættelsesingeniør / Projektleder, elsystem',
  'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
  '37 samtidige CAPEX-projekter · 2–10 mio. kr. pr. projekt · 25 specialister',
  [('Leverance og koordinering',
    'Fremdrift, økonomi, risici og ressourcer på tværs af engineering, indkøb og anlæg; '
    'månedsrapportering til ledelse og bygherre.'),
   ('Kvalitet og driftsoverdragelse',
    'FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA; nul kritiske afvigelser ved aflevering. Elsystemer, '
    'UPS, nød- og panikbelysning og brandtekniske grænseflader.'),
   ('Energi og økonomi',
    '40 % reduktion af energiomkostninger via PDCA; SAP til økonomi-, aktiv- og '
    'omkostningsopfølgning.')]),
 ('Projekt- og værkstedsleder',
  'Ventek-Air · København · jan. 2022 – nov. 2022',
  '11 samtidige ventilations- og klimaprojekter · 14-personers team',
  [('Projekter fra specifikation til aflevering',
    'Kapacitets- og fremdriftsstyring, udbud og tilbud, underentreprenører, aftalegrundlag, '
    'sikkerhedsdokumentation og afleveringspakker.'),
   ('Daglig ledelse',
    'Tavlemøder, flaskehalsanalyse og standardiserede arbejdsgange med løft i leveringsevnen.')]),
 ('Vedligeholdelses- og driftsleder / Værkstedstekniker',
  'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
  '24/7-anlæg · pumper, HVAC, højspænding og SCADA',
  [('Drift og vedligehold',
    'Forebyggende vedligehold, akut fejlfinding, reservedelsflow og lagerstyring; 5S, Standard '
    'Work og PDCA.'),
   ('Arbejdsmiljø', 'LOTO, risikovurdering, APV og nærved-hændelser i skifteholdsdrift.')]),
 ('Elektromekaniker / Produktionsteamleder',
  'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
  '12 mekanikere og teknikere',
  [('Ledelse og problemløsning',
    'Vagtplanlægning, materialestyring og målstyring; fejldiagnose, rodårsagsanalyse og reparation '
    'af el- og mekaniske anlæg.')])]

EDUCATION = [
    ("B.Tech (EQF niveau 6) — Technology Management & Mechanical Engineering",
     "Maskinmesterskolen / Copenhagen School of Marine Engineering & Technology Management · "
     "2017 – 2022 · karakter 7,6/12"),
    ("Elektrisk & mekanisk design, el-ingeniør (EQF niveau 6)",
     "Tehran Technical University · 2000 – 2003"),
    ("HF — matematik og fysik",
     "VUC · 2012 – 2017"),
]

CERTS = [('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023'),
 ('Køleteknik & klimaanlæg (AMU)', 'Mercantec · 2021'),
 ('Lean og forbedringspraksis — 5S, PDCA, VSM, A3, Kaizen', 'Anvendt i drift og projekter'),
 ('STCW — maskinrumsvagt og maritime sikkerhedscertifikater', 'Søfartsstyrelsen · 2021–2023')]

LANGUAGES = ("Dansk (modersmål, skrift og tale) · Engelsk (professionelt, skrift og tale) · "
             "Persisk/farsi · Kørekort B (kategori B)")

PRACTICAL_CV = ('Arbejdssted Kalundborg; bopæl Måløv (Ballerup Kommune), kørekort B. Dansk og engelsk i skrift og '
 'tale. Tiltrædelse og rammerne for den eksisterende virksomhed aftales før ansættelse. Der søges '
 'fagligt ansvar tæt på den daglige produktion.')

REFERENCES = 'Tidligere ledere hos Novo Nordisk A/S og Biofos (Lynetten) — oplyses ved henvendelse.'

PARTNER = [('Produktionerne i Manufacturing II',
  'Prioritering ud fra sikkerhed, kvalitet og driftskonsekvens. Indgreb, stopvinduer og genstart '
  'aftales, og ændrede behov bliver synlige, før der disponeres.'),
 ('Vedligeholdelse og teknikere',
  'Jobplaner og kontroller udvikles med dem, der udfører arbejdet. Fejlforløb og erfaringer bruges '
  'til at forbedre standarderne; kompetencebehov får en konkret oplæringsplan.'),
 ('Projekter, engineering og kvalitet',
  'Vedligeholds- og dokumentationskrav indgår før ibrugtagning. El-faglig kontrol og '
  'GMP-kvalificering koordineres, men deres ansvar og godkendelser holdes tydelige.'),
 ('Interessenter på tværs af sitet',
  'Afvigelser og forbedringer deles i et ensartet format: risiko, evidens, anbefaling, ansvar og '
  'frist. Faglig uenighed afklares på grundlaget, ikke gennem uformelle genveje.')]

FIRST90 = [('Dage 1–30',
  'Lær Manufacturing II, ansvar, godkendte procedurer og kvalitetsledelsessystem at kende. '
  'Gennemgå kritiske installationer med vedligeholdelse og produktion; kortlæg dokumentation, '
  'kontroller og åbne afvigelser. Afklar termografikompetence og udstyr.'),
 ('Dage 31–60',
  'Afprøv anlægs- og lovkravsmatrix på et afgrænset område. Prioritér vedligeholdsbehov efter '
  'risiko og aftal ejere og frister. Planlæg oplæring og superviseret termografi, hvis nødvendigt. '
  'Gennemgå en ny installations overdragelseskrav.'),
 ('Dage 61–90',
  'Gennemfør første opfølgningscyklus: kontroller udført, afvigelser verificeret, jobplaner '
  'forbedret og relevante risici eskaleret. Vis udviklingen i gentagne fejl og planopfyldelse uden '
  'at love en effekt, før data understøtter den.'),
 ('Måned 3–6',
  'Udbred afprøvede vedligeholdsstandarder med kollegerne på tværs af produktionsområdet. Evaluér '
  'kontroldækning, termografiforløb og driftens modtagelse af nye installationer; tilpas årshjulet '
  'efter resultaterne.')]

KEYWORDS = ('El-faglig ansvarlig · Elektriske installationer · Life cycle management · Produktionsudstyr · '
 'Faciliteter · Ibrugtagning · Vedligeholdelse · Kvalitetsledelsessystem · Lovkrav · '
 'Retningslinjer · Lovgivning · Termografering · Eltavler · Tilsyn · Arbejdsmiljø · Pålidelighed · '
 'Nedetid · Produktionsoutput · Forbedringer · Optimere · Standardisere · '
 'Vedligeholdelsesaktiviteter · Industri · Produktionsanlæg · Manufacturing II · Active '
 'Pharmaceutical Ingredient · API · Kolleger · Interessenter · Dansk · Engelsk')


def build(path):
    m = MasterDoc(TEMPLATE, lang="da-DK")

    # ---------------------------------------------------------------- side 1
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta(RECIPIENT)

    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, SUBJECT, bold=True, color="1A1A1A")

    for t in INTRO:
        m.para(t, after=24, line=218)

    for label, body in BULLETS:
        m.bullet(label, body, after=1, line=208)

    m.para(SYSTEM, after=20, line=212)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=0, line=204)

    m.meta("Med venlig hilsen · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "FAGLIG PROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("EL-FAGLIG STYRING — SIKKERHED, LEVETID OG DRIFT",
                   ("Område", "Metoder og værktøjer"), MODELS)

    m.section("UDVALGTE RESULTATER")
    for label, body in ACHIEVEMENTS:
        m.bullet(label, body, after=30)

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

    m.section("KERNEKOMPETENCER & NØGLEORD")
    m.para(KEYWORDS, after=80)

    # afsluttende side
    m.page_break()
    m.models_table("FØRSTE 90 DAGE — OVERBLIK, KONTROL OG FORBEDRINGER",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN ARBEJDES DER — DE FIRE PARTER")
    for label, body in PARTNER:
        m.bullet(label, body, after=30)

    m.section("PRAKTISK OM ANSÆTTELSEN")
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
    out = os.path.join(ROOT, "Shahram_Ajloo_NovoNordisk_ElFagansvarlig_Kalundborg.docx")
    build(out)
    print("OK " + out)
