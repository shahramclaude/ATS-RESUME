# -*- coding: utf-8 -*-
"""
FlexCon — driftschef, personaleledelse og bygningsautomatik, Odense.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Driftschef | FlexCon | Nærværende ledelse og bedre sammenhæng i projekterne'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = '2. november 2026'
RECIPIENT = 'FlexCon ApS · via Didde Bernhammer, MatchMaker'
SUBJECT = 'Ansøgning: Driftschef — Odense'

# ------------------------------------------------------------------ side 1
INTRO = ['Når projektlederne og teknikerne har klare prioriteter og hurtigt kan få hjælp, behøver direktøren '
 'ikke være inde over alle daglige spørgsmål. Det er den forskel, den nye driftschef skal gøre hos '
 'FlexCon: samle otte medarbejdere om opgaverne, få afklaringer på plads og give direktøren mere tid '
 'til virksomhedens udvikling.',
 'Jeg vil begynde med at lære medarbejderne og de igangværende projekter at kende. Hvad fungerer '
 'allerede, hvor venter opgaverne, og hvilke beslutninger bliver ved med at ende hos direktøren? Derfra '
 'vil jeg sammen med teamet indføre et enkelt overblik over projekter, bemanding og åbne spørgsmål. En '
 'virksomhed med 12 medarbejdere har brug for brugbare aftaler, ikke et tungt lag af rapportering.']

BULLETS = [('Ledelse tæt på medarbejderne',
  'De otte medarbejdere skal vide, hvad der er vigtigst, og hvem de kan gå til. Korte fælles '
  'prioriteringsmøder og regelmæssige 1:1-samtaler skal give plads til både fremdrift og trivsel. I '
  'ELOHVAC leder jeg 5 elektrikere og 3 lærlinge med daglig planlægning, MUS og oplæring. Støtten skal '
  'passe til den enkelte, så ansvar ikke bliver til at stå alene.'),
 ('Teknisk sparring, der hjælper opgaven videre',
  'Et teknisk spørgsmål skal afgrænses, så den rette fagperson kan svare på det. Min erfaring med el, '
  'HVAC, styringer og SCADA giver et grundlag for dialogen med projektledere og teknikere. Jeg har ikke '
  'dokumenteret erfaring med Schneider Electric EBO eller Tridium Niagara, og heller ikke en '
  'tilsvarende rolle i et CTS-hus. Derfor skal platformoplæring og grænserne for egne mindre projekter '
  'aftales fra start.'),
 ('Arbejdsgange med færre stop og tilbageløb',
  'Krav, grænseflader, tidsplan og afleveringsgrundlag skal være kendt, før næste person overtager '
  'arbejdet. Fra Ventek-Air har jeg erfaring med 11 samtidige projekter, et team på 14 og daglige '
  'tavlemøder. Hos FlexCon vil jeg følge et konkret projekt fra aftale til idriftsættelse og service, '
  'før vi beslutter, hvad der skal standardiseres.'),
 ('Kvalitet, som kan følges i dokumentationen',
  'Compliance skal hænge sammen med arbejdet: de relevante krav, test, ændringer og godkendelser skal '
  'kunne findes og forstås. Hos Novo Nordisk koordinerede jeg 25 specialister på 37 CAPEX-projekter med '
  'reguleret aflevering uden kritiske fund. Det er erfaring med dokumentationsdisciplin, ikke en '
  'påstand om kendskab til alle FlexCons CTS-krav.')]

SYSTEM = ('På sidste side har jeg beskrevet de første 90 dage. Første skridt er at aftale med direktøren, hvilke '
 'beslutninger jeg overtager, og hvad der fortsat skal vendes med ham. Derefter skal vi have en fast '
 'rytme for prioritering, medarbejdersamtaler og opfølgning på projekterne.')

MIRROR = ('Mit tekniske fundament er B.Tech i Technology Management & Mechanical Engineering og elautorisation '
 'som elautoriseret maskinmester (LV/MV/HV). ELOHVAC har givet ansvar for kunder, tilbud, materialer, '
 'underentreprenører og fuldt P&L. Biofos har givet praktisk erfaring med pumper, HVAC, '
 'højspændingstavler og SCADA i kritisk drift. Det er den baggrund, jeg vil bringe ind i samarbejdet '
 'med FlexCons specialister.')

HONEST = ('For mig er en nærværende leder til at få fat på, tydelig om forventningerne og villig til at lytte, '
 'når planen ikke passer til virkeligheden. Det stemmer godt med jeres flade struktur og korte '
 'beslutningsveje. FlexCons motto, “Work smarter not harder”, giver også mening, når bedre planlægning '
 'kan spare både ventetid og unødige afbrydelser.')

CULTURE = ('Jeg er professionel Claude-bruger og koder og har bygget Python/Claude API-værktøjer til tilbud, '
 'planlægning, KS og KPI-opfølgning. De har givet over 40 % produktivitetsløft i entreprisedriften. Hos '
 'FlexCon vil jeg først se, hvor sådan en hjælp er nyttig, og kun bruge godkendte data og fagligt '
 'kontrollerede løsninger.')

PRACTICAL = ('Jeg bor i Måløv, mens arbejdsstedet er i Odense. Derfor skal vi aftale en holdbar ordning for '
 'tilstedeværelse og eventuelt ophold. Startdato og overgangen fra ELOHVAC skal også afklares. Jeg er '
 'indforstået med, at samtalerne foregår i Kolding.')

CLOSING = ('Jeg vil gerne tale med jer om, hvor teamet først har brug for støtte, og om min ledelses- og '
 'driftsbaggrund kan være det rette supplement til jeres bygningsautomatikfaglighed.')

# ------------------------------------------------------------------ CV
PROFILE = ('FlexCons nye driftschef skal gøre hverdagen lettere for både direktøren og teamet: tydelig '
 'prioritering, tilgængelig faglig sparring og opfølgning på aftaler. Elautoriseret maskinmester '
 '(LV/MV/HV) med erfaring fra teknisk drift, projekter og direkte personaleledelse. I ELOHVAC leder jeg '
 '5 elektrikere og 3 lærlinge og har fuldt P&L-ansvar. Ventek-Air gav ledelse af 14 medarbejdere; Novo '
 'Nordisk gav koordinering af 25 specialister. Praktisk erfaring med HVAC, styringer og SCADA, men ikke '
 'dokumenteret EBO-/Niagara-erfaring eller en tilsvarende lederrolle inden for bygningsautomatik. '
 'Professionel Claude-koder med egne værktøjer til planlægning og kvalitetsopfølgning.')

PRACTICE = [('Personaleledelse og udvikling',
  'ELOHVAC: daglig planlægning for 5 elektrikere og 3 lærlinge, 1:1/MUS, struktureret oplæring og '
  'opfølgning på arbejdsmiljø. Situationsbestemt ledelse med forskellig støtte efter erfaring og '
  'opgave.'),
 ('Overblik over projekter og kapacitet',
  'Ventek-Air: 11 samtidige projekter og et team på 14. Arbejdet omfattede kapacitetsstyring, '
  'tavlemøder og flaskehalsanalyse fra specifikation til aflevering.'),
 ('Teknisk drift og problemløsning',
  'Biofos: forebyggende vedligehold og akut fejlfinding på pumper, HVAC, HV og SCADA. ELOHVAC: '
  'elinstallationer, tavler, styring samt ventilations- og klimaanlæg. CTS-platformene hos FlexCon '
  'kræver oplæring.'),
 ('Samarbejde og dokumentation',
  'Novo Nordisk: 37 CAPEX-projekter med koordinering på tværs af engineering, indkøb og anlæg. FAT/SAT '
  'og IQ/OQ/PQ under GMP/FDA/EMA uden kritiske fund ved aflevering.'),
 ('Økonomi og forbedringer',
  'Fuldt P&L i ELOHVAC. SAP til økonomi, aktiver og omkostninger hos Novo, hvor et PDCA-program gav 40 '
  '% lavere energiomkostninger. Det er ikke et løfte om samme besparelse på CTS-anlæg.'),
 ('Digital støtte til hverdagen',
  'Egne Python/Claude API-værktøjer til tilbud, tidsplaner, KS og KPI har givet over 40 % '
  'produktivitetsløft i entreprisedrift. Nye værktøjer skal gøre arbejdet enklere, ikke skabe endnu et '
  'system, der skal passes.')]

MODELS = [('Fælles prioritering',
  'Et kort ugemøde om bemanding, deadlines og opgaver, der venter på svar. Hver blokering får en '
  'ansvarlig og en aftalt dato.'),
 ('Medarbejdersamtaler',
  'Byg videre på 1:1/MUS og oplæring. GROW/SBI kan bruges til konkrete udviklingsmål og feedback, hvis '
  'det passer til teamet.'),
 ('Ansvar og beslutninger',
  'Aftal med direktøren, hvilke spørgsmål driftschefen afgør. En enkel ansvarsmatrix (RACI) kan '
  'tydeliggøre tvivl om roller.'),
 ('Fra projekt til service',
  'Gennemgå krav, ændringer, test og afleveringsmateriale på ét projekt. Brug det til at finde de få '
  'fælles rutiner, der gør størst forskel.'),
 ('Når problemer vender tilbage',
  'Brug PDCA, A3 og 5xHvorfor til at undersøge årsagen. Følg op med medarbejderne på, om løsningen '
  'virker i praksis.'),
 ('Faglig oplæring',
  'Aftal EBO-/Niagara-oplæring og specialistreview af egne CTS-opgaver. Erfaring med el og SCADA '
  'erstatter ikke platformkendskab.')]

ACHIEVEMENTS = [('5 elektrikere og 3 lærlinge i ELOHVAC',
  'Direkte personaleledelse med daglig planlægning, MUS og oplæring samt fuldt P&L-ansvar.'),
 ('11 projekter og 14 medarbejdere hos Ventek-Air',
  'Kapacitetsstyring, daglige tavlemøder og ansvar fra specifikation til aflevering.'),
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

PRACTICAL_CV = ('Bopæl i Måløv (Ballerup Kommune). Arbejdsstedet er Odense; samtaler foregår i Kolding. '
 'Tilstedeværelse, eventuelt ophold, startdato og overgangen fra ELOHVAC skal aftales. Der er ikke '
 'forudsat flytning eller hjemmearbejde. Dansk og persisk/farsi på modersmålsniveau; engelsk '
 'professionelt i skrift og tale. Kørekort B. B.Tech og elautoriseret maskinmester (LV/MV/HV). Ingen '
 'påstået EBO-/Niagara-certificering eller tidligere selvstændigt ansvar for et CTS-projekthus.')

REFERENCES = 'Tidligere ledere hos Novo Nordisk og Biofos (Lynetten) — oplyses efter aftale.'

PARTNER = [('Direktøren',
  'En kort, fast samtale skal holde os enige om prioriteter, kapacitet og de sager, der kræver hans '
  'beslutning. Jeg vil tage den daglige opfølgning og komme med mulige løsninger, når en sag skal '
  'videre, så den nye rolle faktisk frigør tid.'),
 ('Projektledere og teknikere',
  'Der skal være plads til at sige til, når tid, krav eller kompetencer ikke hænger sammen. Jeg vil '
  'være tæt nok på arbejdet til at forstå problemet og samtidig holde fast i en fælles prioritering. '
  'Trivsel og performance skal drøftes konkret, ikke kun gennem tal.'),
 ('CTS-specialister og fagansvarlige',
  'EBO, Niagara og de konkrete CTS-løsninger skal læres af dem, der kender dem. De rette specialister '
  'skal gennemgå funktion, ændringer og test, indtil mit eget platformkendskab er på plads. Egne '
  'projekter må ikke blive på bekostning af teamets støtte.'),
 ('Kunder og dem, der overtager anlægget',
  'Afleveringen skal gøre det muligt at bruge og servicere løsningen. Krav og aftaler skal følges '
  'gennem projektet, så brugervenlighed, stabilitet og energiforbrug ikke forsvinder mellem '
  'projektering, idriftsættelse og service.')]

FIRST90 = [('Første uge',
  'Aftale opgavefordeling og beslutninger med direktøren. Tale med alle otte medarbejdere om deres '
  'opgaver, trivsel og behov for støtte. Gennemgå igangværende projekter sammen med projektlederne. Ved '
  'ugens slutning skal de vigtigste hasteopgaver og afklaringer have en ansvarlig og en dato.'),
 ('Inden dag 30',
  'Få et fælles overblik over bemanding, deadlines og projekter, der mangler input. Følge et konkret '
  'CTS-projekt og lære kravene til dokumentation, test og aflevering. Aftale individuelle '
  'udviklingsbehov og en plan for min egen platformoplæring. Vælge én arbejdsgang, som teamet mener '
  'giver unødigt besvær.'),
 ('Inden dag 60',
  'Afprøve den forbedrede arbejdsgang på et aftalt projekt og følge den sammen med de berørte '
  'medarbejdere. Tage et mindre projekt med det specialistreview, platformkendskabet kræver. '
  'Kontrollere, at ændringer og åbne punkter bliver fulgt til dørs. Justere møder og opfølgning, hvis '
  'de tager mere tid, end de hjælper.'),
 ('Inden dag 90',
  'Gennemgå med direktøren, hvilke daglige beslutninger der nu er flyttet fra hans bord, og hvad der '
  'stadig kræver afklaring. Følge op på medarbejdernes udviklingsaftaler og på projektforsinkelser, '
  'omarbejde og åbne spørgsmål. Beslutte de næste forbedringer og mit videre ansvar for egne '
  'CTS-projekter ud fra den opnåede kompetence.')]

KEYWORDS = ('Personaleledelse og udvikling · Trivsel og samarbejde · Teknisk sparring · Projektprocesser og '
 'projektplanlægning · Kvalitet og dokumentation · El, HVAC og SCADA · Løbende forbedringer og digital '
 'støtte. Schneider Electric EBO, Tridium Niagara og FlexCons CTS-arbejdsgange er områder, hvor der '
 'skal aftales oplæring og faglig støtte.')


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

    m.models_table("ENKLE RUTINER FOR LEDELSE OG PROJEKTER",
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
    m.models_table("FØRSTE 90 DAGE — TEAMET, PROJEKTERNE OG DIREKTØRENS TID",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SAMARBEJDET I HVERDAGEN")
    for label, body in PARTNER:
        m.bullet(label, body, after=30)

    m.section("KRAV OG KVALITET I DET DAGLIGE ARBEJDE")
    m.para("Jeg vil begynde med at gennemgå et projekt sammen med den ansvarlige projektleder og en tekniker. Kan vi finde de aftalte funktioner, den gældende dokumentation og de ændringer, der er lavet undervejs? Er test og åbne punkter registreret, og ved kunden, hvad der er afleveret? De spørgsmål viser ofte, hvor en enkel fælles rutine kan hjælpe. Kravene skal afklares ud fra den konkrete opgave og de gældende standarder og interne procedurer. Ved tvivl skal den rette fagansvarlige inddrages. Nye skabeloner eller digitale værktøjer giver først værdi, når medarbejderne bruger dem, og når de gør det lettere at levere et stabilt anlæg, som andre kan overtage og servicere.", after=80)

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
    build(os.path.join(ROOT, "Shahram_Ajloo_FlexCon_Driftschef.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_FlexCon_Driftschef.docx"))
