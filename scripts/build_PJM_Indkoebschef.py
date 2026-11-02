# -*- coding: utf-8 -*-
"""
PJM — indkøbschef, ledelse og operationelt indkøb.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Indkøbschef | PJM | Tæt på teamet, teknikken og produktionen'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = '2. november 2026'
RECIPIENT = 'PJM A/S · via Didde Bernhammer, MatchMaker'
SUBJECT = 'Ansøgning: Indkøbschef'

# ------------------------------------------------------------------ side 1
INTRO = ['I en maskinvirksomhed er et indkøb først lykkedes, når produktionen har den rigtige del på det '
 'aftalte tidspunkt og med den nødvendige dokumentation. Den nye indkøbschef hos PJM skal hjælpe de tre '
 'indkøbere med netop det og samtidig tage den daglige opfølgning fra Supply Chain Manager, så der '
 'bliver mere plads til udvikling.',
 'Jeg vil starte med teamet og de igangværende ordrer. Hvilke leverancer kan forsinke produktionen, '
 'hvor mangler vi en teknisk afklaring, og hvilke spørgsmål ender igen og igen hos Supply Chain '
 'Manager? Svarene skal bruges til en enkel fælles prioritering, ikke til endnu et regneark ved siden '
 'af ERP-systemet.']

BULLETS = [('Give de tre indkøbere tydelig støtte',
  'Teamet skal kende prioriteterne og have nogen at gå til, når leverandør, krav og tidsplan ikke '
  'passer sammen. I ELOHVAC leder jeg 5 elektrikere og 3 lærlinge med daglig planlægning, 1:1/MUS og '
  'oplæring. Den erfaring vil jeg bruge til at skabe klare aftaler og hjælpe den enkelte videre uden at '
  'overtage alle opgaver.'),
 ('Få teknik og leverancer til at hænge sammen',
  'Produktion, kvalitet og udvikling skal med tidligt, når en del eller leverance kræver afklaring. Fra '
  'tekniske entrepriser har jeg erfaring med tilbud, materialer og underentreprenører og med at få en '
  'samlet leverance til at fungere. Ved tegninger, revisioner eller alternative komponenter skal den '
  'rette tekniske fagperson sikre grundlaget, før vi bestiller eller accepterer en ændring.'),
 ('Holde styr på det, der kan stoppe produktionen',
  'Jeg vil følge kritiske ordrer, bekræftede datoer og åbne spørgsmål sammen med teamet. En '
  'leveringsdato skal holdes op mod den faktiske produktionsplan. Når noget skrider, skal vi kende '
  'konsekvensen og tage stilling til mulighederne med de berørte kolleger. På Ventek-Air arbejdede jeg '
  'med kapacitet og flaskehalse på 11 samtidige projekter med 14 medarbejdere.'),
 ('Forbedre arbejdsgangene på et konkret grundlag',
  'Følg en ordre fra behov til modtagelse og se, hvor afklaringer eller fejl tager tid. Vælg derefter '
  'få forbedringer med teamet og mål, om de hjælper. Jeg har brugt SAP til økonomi, aktiver og '
  'omkostninger hos Novo Nordisk. Business Central og PJM’s indkøbsrutiner skal jeg lære; erfaring med '
  'ét ERP-system er ikke det samme som rutine i et andet.')]

SYSTEM = ('På sidste side har jeg beskrevet, hvordan jeg vil bruge de første 90 dage. Først skal Supply Chain '
 'Manager og jeg aftale beslutningsrum og opgavefordeling. Derefter skal teamet have et fælles billede '
 'af hasteopgaverne og en fast, kort opfølgning på de leverancer og afklaringer, der kræver handling.')

MIRROR = ('Mit fundament er B.Tech i Technology Management & Mechanical Engineering og elautorisation som '
 'elautoriseret maskinmester (LV/MV/HV). ELOHVAC har givet fuldt P&L-ansvar og arbejde med kunder, '
 'materialer og underentreprenører. Hos Novo Nordisk koordinerede jeg 25 specialister på 37 '
 'CAPEX-projekter på tværs af engineering, indkøb og anlæg.')

HONEST = ('Jeg har ikke dokumenteret erfaring fra en tilsvarende indkøbschefrolle i en maskinvirksomhed eller et '
 'etableret netværk blandt branchens leverandører. CAD- og tegningsrutinen skal også afklares konkret. '
 'Derfor er det vigtigt at få vurderet, om min tekniske drifts- og ledelsesbaggrund er det rette '
 'supplement til de tre indkøberes faglighed.')

CULTURE = ('PJM’s fokus på samarbejde og løbende læring tiltaler mig, især fordi produktion og know-how er i '
 'huset. Det giver mulighed for at få spørgsmål afklaret med dem, der kender løsningen. Jeg er selv '
 'professionel Claude-bruger og koder og har bygget Python/Claude API-værktøjer til tilbud, '
 'planlægning, KS og KPI. De har givet over 40 % produktivitetsløft i entreprisedrift; hos PJM skal '
 'eventuel brug passe til jeres systemer og godkendte data.')

PRACTICAL = ('Jeg bor i Måløv. Opslaget hos MatchMaker angiver Fårevejle Stationsby; tilstedeværelse, startdato og '
 'overgangen fra ELOHVAC skal aftales. Jeg deltager gerne i en første samtale i København eller via '
 'Teams.')

CLOSING = ('Jeg vil gerne tale med jer om, hvad indkøbsteamet først har brug for fra en ny leder, og om min '
 'erfaring kan bruges i rollen med den nødvendige oplæring og støtte.')

# ------------------------------------------------------------------ CV
PROFILE = ('Indkøbsafdelingen skal støtte produktionen med klare aftaler, sikre leverancer og hurtige tekniske '
 'afklaringer. Min baggrund er teknisk ledelse, materialestyring og økonomisk ansvar i entrepriser og '
 'projekter. Elautoriseret maskinmester (LV/MV/HV) og B.Tech. I ELOHVAC leder jeg 5 elektrikere og 3 '
 'lærlinge og har fuldt P&L-ansvar. Hos Novo Nordisk koordinerede jeg 25 specialister og arbejdede med '
 'SAP til økonomi og aktiver. Overgangen til en indkøbschefrolle kræver indføring i PJM’s systemer og '
 'branche. Professionel Claude-koder med egne værktøjer til planlægning og kvalitetsopfølgning.')

PRACTICE = [('Personaleledelse i hverdagen',
  'ELOHVAC: 5 elektrikere og 3 lærlinge med daglig planlægning, 1:1/MUS og struktureret oplæring. '
  'Situationsbestemt ledelse med støtte efter erfaring og opgave. Ledelse af indkøbere vil være en ny '
  'faglig sammenhæng.'),
 ('Materialer og økonomisk ansvar',
  'ELOHVAC: tilbud og beregning, materialestyring, underentreprenører og kundeleverancer med fuldt P&L. '
  'Erfaring med at få tekniske behov, omkostninger og levering til at hænge sammen.'),
 ('Prioritering på tværs af projekter',
  'Ventek-Air: 11 samtidige projekter og et team på 14. Kapacitetsstyring, tavlemøder og '
  'flaskehalsanalyse fra specifikation til aflevering.'),
 ('Teknisk samarbejde og kvalitet',
  'Novo: 37 CAPEX-projekter med koordinering på tværs af engineering, indkøb og anlæg. FAT/SAT og '
  'IQ/OQ/PQ under GMP/FDA/EMA uden kritiske fund ved aflevering.'),
 ('ERP og forbedringer',
  'SAP brugt til økonomi, aktiver og omkostninger hos Novo. Excel/Power Query fra MS Office og Power BI '
  'indgår i mit digitale værktøjssæt. Business Central er nyt; systemoplæring aftales med den '
  'ansvarlige.'),
 ('Digital støtte, der sparer tid',
  'Egne Python/Claude API-værktøjer til tilbud, tidsplaner, KS og KPI har givet over 40 % '
  'produktivitetsløft i entreprisedrift. Nye indkøbsværktøjer skal bruge godkendte data og understøtte '
  'ERP, ikke skabe en parallel ordrebog.')]

MODELS = [('Fælles prioritering',
  'Kort opfølgning på kritiske leverancer, bekræftede datoer og tekniske afklaringer. Hver åben sag får '
  'en ansvarlig og næste handling.'),
 ('Ledelse og udvikling',
  'Byg videre på 1:1/MUS og oplæring. GROW/SBI kan bruges til konkrete udviklingsmål og feedback, hvis '
  'det hjælper teamet.'),
 ('Ansvar og beslutninger',
  'Aftal med Supply Chain Manager, hvilke beslutninger lederen overtager. En enkel ansvarsmatrix (RACI) '
  'kan afklare tvivl.'),
 ('Teknisk indkøbsgrundlag',
  'Afklar specifikation, tegningsrevision og dokumentationskrav med udvikling/kvalitet. Alternative '
  'dele kræver godkendelse fra de rette fagpersoner.'),
 ('Fra behov til modtagelse',
  'Følg en konkret ordre i ERP sammen med indkøberne. Se på afklaringer, ordrebekræftelse, ændringer og '
  'håndtering af afvigelser ved modtagelse.'),
 ('Læring fra fejl og ventetid',
  'Brug PDCA/A3/5xHvorfor på gentagne problemer. Følg op med produktion og teamet på, om løsningen gør '
  'en forskel.')]

ACHIEVEMENTS = [('5 elektrikere og 3 lærlinge i ELOHVAC',
  'Direkte personaleledelse, daglig planlægning og oplæring samt fuldt P&L-ansvar.'),
 ('11 projekter og 14 medarbejdere hos Ventek-Air',
  'Kapacitetsstyring, tavlemøder og ansvar fra specifikation til aflevering.'),
 ('37 CAPEX-projekter hos Novo Nordisk',
  'DKK 2–10 mio. pr. projekt; koordinering af 25 specialister og reguleret aflevering uden kritiske '
  'fund.'),
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

PRACTICAL_CV = ('Bopæl i Måløv (Ballerup Kommune). MatchMaker-opslaget angiver Fårevejle Stationsby; den konkrete '
 'arbejdsordning og startdato skal aftales sammen med overgangen fra ELOHVAC. Samtaler i København '
 'eller via Teams. Dansk og persisk/farsi på modersmålsniveau; engelsk professionelt i skrift og tale. '
 'Kørekort B. B.Tech og elautoriseret maskinmester (LV/MV/HV).')

REFERENCES = 'Tidligere ledere hos Novo Nordisk og Biofos (Lynetten) — oplyses efter aftale.'

PARTNER = [('Supply Chain Manager',
  'En kort, fast samtale om prioriteringer, kapacitet og undtagelser skal holde os enige om retningen. '
  'Jeg vil komme med mulige løsninger, når noget kræver en beslutning, og tage ansvar for den '
  'opfølgning, vi har aftalt at flytte fra Supply Chain Managers bord.'),
 ('De tre indkøbere',
  'Der skal være plads til at sige til, når en leverance, et krav eller en tidsplan ikke hænger sammen. '
  'Jeg vil bruge medarbejdernes erfaring og være tydelig om prioriteringen, samtidig med at den enkelte '
  'får ansvar og støtte til at løse opgaven.'),
 ('Produktion, kvalitet og udvikling',
  'Spørgsmål om specifikationer, tegninger eller acceptable alternativer skal til de rigtige '
  'fagpersoner tidligt. Indkøb skal kunne forklare leverandøren det aftalte behov; teknisk accept og '
  'godkendelse af ændringer forbliver hos de ansvarlige.'),
 ('Leverandører',
  'Følg op på de aftalte krav, dokumentation og leveringsdatoer. Ved afvigelser skal både konsekvens og '
  'mulige løsninger frem, så produktionen kan planlægge på et troværdigt grundlag. Jeg kommer ikke med '
  'et påstået eksisterende netværk i PJM’s leverandørkreds.')]

FIRST90 = [('Første uge',
  'Aftale opgaver og beslutningsrum med Supply Chain Manager. Tale med alle tre indkøbere og følge de '
  'mest kritiske åbne ordrer sammen med produktionen. Finde de afklaringer, der haster mest. Ved ugens '
  'slutning skal teamet vide, hvem der følger op på hvad, og hvornår en sag skal videre.'),
 ('Inden dag 30',
  'Gennemgå et konkret indkøbsforløb fra behov til modtagelse med teamet, kvalitet og udvikling. Lære '
  'ERP-arbejdsgangen og aftale oplæring i Business Central, hvis det er det anvendte system. Afklare '
  'tegnings-/CAD-krav med en fagansvarlig. Få et fælles billede af leveringsafvigelser, manglende input '
  'og teamets behov for støtte.'),
 ('Inden dag 60',
  'Afprøve én aftalt forbedring på et afgrænset ordre- eller leverandørforløb. Det kan være tydeligere '
  'teknisk grundlag eller bedre opfølgning på bekræftede datoer. Følge med produktionen, om det '
  'mindsker ventetid og omarbejde. Tage den aftalte daglige opfølgning fra Supply Chain Manager og '
  'bruge teamets erfaring aktivt.'),
 ('Inden dag 90',
  'Gennemgå leveringsafvigelser, åbne afklaringer og teamets udviklingsaftaler med Supply Chain '
  'Manager. Se på, hvilke beslutninger der faktisk er flyttet fra Supply Chain Managers bord, og hvor der stadig mangler '
  'støtte. Beslutte næste forbedringer ud fra erfaringerne og aftale mit videre ansvar, når system- og '
  'branchekendskabet er vurderet.')]

KEYWORDS = ('Personaleledelse · Materialestyring · Projektøkonomi · Teknisk dokumentation · SAP ERP · Excel/Power '
 'Query fra MS Office · Power BI · Python og Claude API · PDCA og A3 · Kapacitetsstyring · Dansk og '
 'engelsk.')


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

    m.models_table("LEDELSE OG INDKØB I HVERDAGEN",
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
    m.models_table("FØRSTE 90 DAGE — TEAM, ORDRER OG SAMARBEJDE",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SAMARBEJDET I HVERDAGEN")
    for label, body in PARTNER:
        m.bullet(label, body, after=30)

    m.section("FRA TEKNISK BEHOV TIL DEN RIGTIGE LEVERANCE")
    m.para("Jeg vil gennemgå en konkret ordre sammen med en indkøber og dem, der skal bruge leverancen. Er det tydeligt, hvilken del der skal købes, hvilken revision der gælder, og hvornår den skal bruges? Stemmer ordrebekræftelsen med behovet, og er dokumentationskravene aftalt? Hvis leverandøren foreslår en anden del eller dato, skal ændringen vurderes med de rette kolleger og opdateres i det aftalte system. Ved modtagelse skal eventuelle afvigelser kunne følges tilbage til ordren. Den gennemgang skal vise, hvor teamet har brug for bedre afklaringer eller rutiner. Det er ikke nok at få ordren sendt; produktionen skal også kunne bruge det, der kommer ind ad døren.", after=80)

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
    build(os.path.join(ROOT, "Shahram_Ajloo_PJM_Indkoebschef.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_PJM_Indkoebschef.docx"))
