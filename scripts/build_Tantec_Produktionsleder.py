# -*- coding: utf-8 -*-
"""
Tantec — produktionsleder, værksteder og personaleledelse.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Produktionsleder | Tantec | Planlægning, værksteder og mennesker'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = '2. november 2026'
RECIPIENT = 'Tantec A/S · via Anne Thomsen, MatchMaker'
SUBJECT = 'Ansøgning: Produktionsleder'

# ------------------------------------------------------------------ side 1
INTRO = ['Når mekanisk og elektrisk værksted, reparationer og vareflow deler ressourcer, skal prioriteringen '
 'være tydelig. De 15 medarbejdere hos Tantec skal kunne se, hvad der haster, hvad der er klar til at '
 'blive bygget, og hvem der tager fat, når en opgave går i stå. Produktionslederen skal samle den '
 'daglige styring og tage opfølgning fra COO uden at gøre en uformel organisation tungere.',
 'Jeg vil begynde på værkstederne og følge de aktuelle opgaver fra produktionsgrundlaget hos PTA til '
 'vareudlevering. Det skal vise, hvor planen holder, og hvor materialer, afklaringer eller kapacitet '
 'mangler. Derefter vil jeg samle medarbejderne om en enkel ugeplan med plads til både planlagte '
 'projekter og reparationer.']

BULLETS = [('Gøre dagens prioritering klar',
  'Et kort tavlemøde skal give overblik over dagens opgaver, flaskehalse og hjælp på tværs. Hos '
  'Ventek-Air ledede jeg et team på 14 på 11 samtidige projekter med kapacitetsstyring og tavlemøder. '
  'Hos ARJ Engineering havde jeg ansvar for 12 mekanikere og teknikere i et maskinværksted med '
  'reparation af industrielt el- og mekanisk udstyr.'),
 ('Få PTA-grundlaget sikkert ud i værkstedet',
  'Inden en opgave sættes i gang, skal tegninger, materialer, krav og eventuelle uklarheder være '
  'gennemgået med de rette fagpersoner. Ændringer skal tilbage til PTA, så værkstedet ikke arbejder '
  'efter hver sin version. Fra tekniske entrepriser har jeg erfaring med at føre opgaver fra '
  'specifikation til aflevering og følge økonomi, kvalitet og fremdrift undervejs.'),
 ('Være til stede, også når noget er svært',
  'Jeg vil lære medarbejdernes opgaver og erfaring at kende og være tydelig om ansvar og forventninger. '
  'I ELOHVAC leder jeg 5 elektrikere og 3 lærlinge med daglig planlægning, 1:1/MUS og oplæring. Det er '
  'konkrete samtaler og opfølgning i hverdagen, der skal støtte trivsel, motivation og et godt '
  'samarbejde – ikke kun en ny mødestruktur.'),
 ('Forbedre der, hvor tiden forsvinder',
  'Start med én tilbagevendende årsag til ventetid eller omarbejde. Brug medarbejdernes viden, prøv en '
  'løsning og se, om den virker. Jeg har brugt Lean, 5S og PDCA i drift og projekter og arbejder med '
  'Excel/Power Query fra MS Office. Min SAP-erfaring er økonomi og aktiver; Monitor og Tantecs konkrete '
  'produktionsplanlægning skal jeg lære.')]

SYSTEM = ('På sidste side har jeg lagt en 90-dagesplan. Den begynder med en fælles prioritering med COO og en '
 'gennemgang af de åbne opgaver. Planen skal derefter holdes op mod den faktiske kapacitet og følges '
 'med få tal for leveringsevne, omarbejde og belastning. Hvert åbent problem skal have en ansvarlig og '
 'en aftalt næste handling.')

MIRROR = ('Det tekniske fundament er B.Tech i Technology Management & Mechanical Engineering og elautorisation '
 'som elautoriseret maskinmester (LV/MV/HV). Min erfaring spænder fra mekanisk værksted og kritisk '
 'vedligehold til el- og HVAC-entrepriser. Hos Novo Nordisk koordinerede jeg 25 specialister på 37 '
 'CAPEX-projekter og arbejdede med FAT/SAT og dokumenteret aflevering uden kritiske fund.')

HONEST = ('Jeg har ikke arbejdet med plasma- og coronasystemer eller haft den samme samlede rolle med både PTA, '
 'værksteder og vareflow. Derfor skal overgangen bygge på produktkendskab, systemoplæring og en tydelig '
 'arbejdsdeling med COO og de erfarne medarbejdere.')

CULTURE = ('Tantecs kombination af mekanik, elektronik og kundetilpassede løsninger gør samarbejdet mellem fagene '
 'vigtigt. Jeg vil bevare de korte beslutningsveje og bruge ledergruppen til at få løst de problemer, '
 'produktionen ikke kan løse alene. Jeg er også professionel Claude-bruger og koder. Mine Python/Claude '
 'API-værktøjer til tilbud, planlægning, KS og KPI har givet over 40 % produktivitetsløft i '
 'entreprisedrift; eventuel brug hos Tantec skal følge jeres regler for systemer og data.')

PRACTICAL = ('Jeg bor i Måløv. En holdbar løsning for daglig tilstedeværelse i Lunderskov, startdato og overgangen '
 'fra ELOHVAC skal derfor aftales. Jeg deltager gerne i en indledende samtale i Kolding.')

CLOSING = ('Jeg vil gerne drøfte, hvilke opgaver der først skal flyttes fra COO, og hvor de 15 medarbejdere har '
 'mest brug for støtte fra deres nye produktionsleder.')

# ------------------------------------------------------------------ CV
PROFILE = ('Produktionen skal have en plan, der hænger sammen med kapacitet, materialer og det grundlag, PTA '
 'afleverer. Min erfaring er ledelse af tekniske medarbejdere, værkstedsdrift og koordinering af '
 'samtidige projekter. B.Tech og elautoriseret maskinmester (LV/MV/HV). Hos ARJ Engineering ledede jeg '
 '12 mekanikere og teknikere; hos Ventek-Air et team på 14 på 11 projekter. I ELOHVAC leder jeg 5 '
 'elektrikere og 3 lærlinge med fuldt P&L-ansvar. Monitor og Tantecs overfladebehandlingsudstyr vil '
 'være nyt. Professionel Claude-koder med egne værktøjer til planlægning og kvalitetsopfølgning.')

PRACTICE = [('Ledelse tæt på arbejdet',
  'ELOHVAC: 5 elektrikere og 3 lærlinge, daglig planlægning, 1:1/MUS og struktureret oplæring. '
  'Situationsbestemt ledelse med støtte efter opgave og erfaring.'),
 ('Mekanisk og elektrisk værkstedsforståelse',
  'ARJ Engineering: ledelse af 12 mekanikere og teknikere, vagtplaner, materialestyring og målstyring. '
  'Fejldiagnose, årsagsanalyse og reparation af industrielt el- og mekanisk udstyr.'),
 ('Planlægning og kapacitetsstyring',
  'Ventek-Air: 11 samtidige projekter og et team på 14. Tavlemøder, flaskehalsanalyse og '
  'ressourceallokering fra specifikation til aflevering.'),
 ('Kvalitet og dokumenteret aflevering',
  'Novo: 37 CAPEX-projekter à DKK 2–10 mio. Koordinering af 25 specialister på tværs af engineering, '
  'indkøb og anlæg. FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA uden kritiske fund ved aflevering.'),
 ('Økonomi og styringsværktøjer',
  'Fuldt P&L i ELOHVAC. SAP brugt til økonomi og aktiver hos Novo; Excel/Power Query og Power BI i det '
  'digitale værktøjssæt. Monitor er ikke dokumenteret erfaring.'),
 ('Forbedringer med medarbejderne',
  '5S, PDCA, A3 og 5xHvorfor til drift og projekter. Egne Python/Claude API-værktøjer har givet over 40 '
  '% produktivitetsløft i entreprisedrift – ikke et målt resultat i fabriksproduktion.')]

MODELS = [('Daglig opfølgning',
  'Tavlemøde om dagens plan, bemanding, materialer og blokeringer. Aftal ansvar og næste handling, før '
  'mødet slutter.'),
 ('Kapacitet og ugeplan',
  'Hold opgavernes behov op mod de tilgængelige kompetencer og timer. Synliggør også reparationer og '
  'hasteopgaver, så belastningen ikke skjules.'),
 ('Trivsel og udvikling',
  '1:1/MUS og oplæring fra ELOHVAC. GROW/SBI kan støtte konkrete udviklingsmål og feedback, hvor det '
  'passer til medarbejderen.'),
 ('Overdragelse fra PTA',
  'Aftal, hvad der skal være klart ved opstart: produktionsgrundlag, materialer, kvalitetskrav og '
  'tekniske afklaringer. Ændringer tilbage til den ansvarlige.'),
 ('Forbedring og orden',
  '5S og PDCA ved et afgrænset problem. Brug A3/5xHvorfor ved gentagelser og følg effekten med dem, der '
  'udfører arbejdet.'),
 ('Aflastning af COO',
  'Aftal beslutningsrum og en enkel ansvarsmatrix (RACI). Fast kort opfølgning på levering, kvalitet og '
  'kapacitet; kun undtagelser løftes videre.')]

ACHIEVEMENTS = [('12 mekanikere og teknikere hos ARJ Engineering',
  'Værkstedsledelse, materialestyring og reparation af industrielt el- og mekanisk udstyr.'),
 ('11 projekter og 14 medarbejdere hos Ventek-Air',
  'Kapacitetsstyring, tavlemøder og ansvar fra specifikation til aflevering.'),
 ('5 elektrikere og 3 lærlinge i ELOHVAC', 'Direkte personaleledelse, oplæring og fuldt P&L-ansvar.'),
 ('37 CAPEX-projekter hos Novo Nordisk',
  'DKK 2–10 mio. pr. projekt, koordinering af 25 specialister og aflevering uden kritiske fund.')]

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

PRACTICAL_CV = ('Bopæl i Måløv (Ballerup Kommune). Tantecs produktion ligger i Lunderskov; en holdbar løsning for '
 'daglig tilstedeværelse samt startdato og overgang fra ELOHVAC skal aftales. Ingen flytning eller '
 'hjemmearbejdsordning er forudsat. Samtaler i Kolding. Dansk og persisk/farsi på modersmålsniveau, '
 'engelsk professionelt i skrift og tale. Kørekort B. B.Tech og elautoriseret maskinmester (LV/MV/HV).')

REFERENCES = 'Tidligere ledere hos Novo Nordisk og Biofos (Lynetten) — oplyses efter aftale.'

PARTNER = [('COO og ledergruppen',
  'Kort, fast opfølgning på plan, kapacitet og undtagelser. Jeg tager den aftalte daglige koordinering '
  'og kommer med løsningsforslag, når en prioritering kræver en beslutning på tværs af virksomheden.'),
 ('De 15 medarbejdere',
  'Være synlig i værkstederne og følge op på de aftaler, vi laver. Spørge ind til opgaver, belastning '
  'og behov for oplæring. Prioriteringen skal være forståelig, og problemer skal kunne siges højt, mens '
  'de stadig kan løses.'),
 ('PTA og de tekniske fagpersoner',
  'Sikre en tydelig overdragelse til produktionen og hurtig afklaring af mangler. Tekniske ændringer '
  'skal vurderes og godkendes af den ansvarlige; en produktionsplan må ikke bygge på uafklarede '
  'antagelser.'),
 ('Reparation og varemodtagelse/-udlevering',
  'Gøre serviceopgaver og vareflow synlige i den samlede plan. Manglende dele, modtageafvigelser eller '
  'en hasteopgave skal hurtigt frem, så den aftalte prioritering kan justeres sammen med de berørte '
  'kolleger.')]

FIRST90 = [('Første uge',
  'Tale med de 15 medarbejdere og følge en opgave gennem mekanisk/elektrisk værksted, reparation og '
  'vareflow. Aftale med COO, hvilke beslutninger og opfølgninger jeg overtager. Samle de åbne opgaver '
  'og kendte blokeringer med PTA. Ved ugens slutning skal dagens prioritering og ansvar være tydelige.'),
 ('Inden dag 30',
  'Få en fælles ugeplan med bemanding, kompetencer, materialer og plads til reparationer. Aftale med '
  'PTA, hvad et klart produktionsgrundlag indeholder. Lære ERP-arbejdsgangen og få oplæring i Monitor, '
  'hvis det er systemet i brug. Etablere udgangspunkt for leveringsevne, omarbejde og '
  'kapacitetsbelastning samt holde de første individuelle samtaler.'),
 ('Inden dag 60',
  'Afprøve én forbedring med medarbejderne, fx færre stop på grund af manglende afklaring eller bedre '
  'materialeflow. Følge effekten på de valgte opgaver og justere. Bruge ugeplan og tavlemøder til at '
  'løse den daglige koordinering. Drøfte tværgående hindringer i ledergruppen med konkrete forslag til '
  'beslutning.'),
 ('Inden dag 90',
  'Gennemgå levering, kvalitet, kapacitet og medarbejdernes erfaringer med COO. Se, hvilke opfølgninger '
  'der faktisk er flyttet fra COO, og om de nye rutiner hjælper værkstederne. Aftale næste '
  'forbedringer, oplæring og eventuelle kompetencebehov på grundlag af de første måneders data og '
  'samtaler.')]

KEYWORDS = ('Produktionsplanlægning · Kapacitetsstyring · Ressourceoptimering · Værkstedsledelse · Reparation · '
 'Materialestyring · Kvalitet · Leveringsevne · Lean, 5S og PDCA · SAP ERP · Excel/Power Query fra MS '
 'Office · Power BI · Python og Claude API · Dansk og engelsk.')


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

    m.models_table("LEDELSE OG STYRING I HVERDAGEN",
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
    m.models_table("FØRSTE 90 DAGE — VÆRKSTEDER, PLAN OG SAMARBEJDE",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SAMARBEJDET I HVERDAGEN")
    for label, body in PARTNER:
        m.bullet(label, body, after=30)

    m.section("FRA PTA TIL FÆRDIG LEVERANCE")
    m.para('En planlagt opgave skal kunne gå fra PTA til værksted uden, at medarbejderen først skal lede efter den gældende tegning eller en manglende afklaring. Jeg vil derfor gennemgå et konkret forløb med PTA, værkstederne og varemodtagelsen: Hvad skal være klart ved opstart, hvordan registrerer vi ændringer, og hvem tager stilling, når noget afviger? Reparationer skal kunne komme ind i planen uden at gøre alle andre leveringsdatoer uforudsigelige. En enkel registrering af årsagen til stop og omarbejde kan vise, hvor vi bør begynde. Vi skal måle få ting konsekvent og bruge dem til at handle – ikke bygge et nyt rapporteringslag. Sikkerhed og aftalt kvalitet går forud for at få en opgave markeret færdig.', after=80)

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
    build(os.path.join(ROOT, "Shahram_Ajloo_Tantec_Produktionsleder.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_Tantec_Produktionsleder.docx"))
