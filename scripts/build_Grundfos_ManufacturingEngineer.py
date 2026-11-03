# -*- coding: utf-8 -*-
"""
Grundfos — Manufacturing Engineer, CR-pumpefabrikken.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Manufacturing Engineer | Grundfos | Oppetid, udstyr og forbedringer'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = '3. november 2026'
RECIPIENT = 'Grundfos · Manufacturing Engineering · CR-pumpefabrikken, Bjerringbro'
SUBJECT = 'Ansøgning: Manufacturing Engineer · job 77575'

# ------------------------------------------------------------------ side 1
INTRO = ['En produktionslinje bliver ikke mere stabil af en god analyse alene. Fejlen skal forstås sammen med '
 'dem, der står ved udstyret, løsningen skal afprøves sikkert, og effekten skal kunne ses i den daglige '
 'drift. På CR-pumpefabrikken skal Manufacturing Engineering både hjælpe, når noget stopper, og få de '
 'forbedringer gennemført, som giver bedre oppetid og produktionsflow.',
 'Jeg vil begynde ude ved linjen sammen med operatører, vedligehold og ME-kollegerne. Hvilke stop '
 'gentager sig, hvor venter emnerne, og hvilke forklaringer har vi faktisk belæg for? Derfra vil jeg '
 'vælge en afgrænset opgave med teamet, få et pålideligt udgangspunkt og følge forbedringen helt frem '
 'til, at den fungerer i produktionen.']

BULLETS = [('Gå til udstyret, når driften har brug for hjælp',
  'Hos Biofos arbejdede jeg med kritisk 24/7-drift: pumper, HVAC, højspændingstavler og SCADA, '
  'forebyggende vedligehold og akut fejlfinding. Min håndværksmæssige baggrund er elektromekanisk, og '
  'hos ARJ Engineering arbejdede jeg med fejldiagnose og reparation af industrielle el- og mekaniske '
  'anlæg. Det er den praktiske indgang, jeg vil tage med ind i den tekniske support – med respekt for '
  'operatørernes viden og fabrikkens sikkerhedsprocedurer.'),
 ('Finde årsagen og følge forbedringen til dørs',
  'Jeg bruger PDCA, A3 og 5xHvorfor til at komme fra symptom til en løsning, der kan efterprøves. '
  'Biofos gav erfaring med 5S og Standard Work i værksted og lager. Hos Ventek-Air brugte vi tavlemøder '
  'og flaskehalsanalyse til at styre kapacitet på 11 projekter. På fabrikken skal vi måle, om ændringen '
  'faktisk mindsker stop eller ventetid, før den bliver en ny standard.'),
 ('Få nyt udstyr sikkert over i driften',
  'Hos Novo Nordisk koordinerede jeg 25 specialister på 37 CAPEX-projekter à DKK 2–10 mio. og arbejdede '
  'med FAT/SAT samt IQ/OQ/PQ under GMP/FDA/EMA uden kritiske fund ved aflevering. Det giver erfaring '
  'med at samle tekniske krav, test, åbne punkter og dokumentation. Ved hjemtagning af udstyr hos '
  'Grundfos skal acceptkrav og overdragelse aftales med produktion, vedligehold og de ansvarlige '
  'specialister.'),
 ('Bruge data til en konkret beslutning',
  'Jeg arbejder med Excel/Power Query, Power BI og egne Python-værktøjer. SAP har jeg brugt til '
  'økonomi, aktiver og omkostninger hos Novo – ikke som dokumenteret superbruger i produktionsmoduler. '
  'I et forbedringsprojekt vil jeg først sikre, at data beskriver det, vi ser ved linjen, og derefter '
  'bruge dem til at prioritere og følge effekten. Ny teknologi skal løse et kendt problem, ikke kun '
  'give flere målinger.')]

SYSTEM = ('På sidste side har jeg lagt en 90-dagesplan omkring én konkret linje og én aftalt forbedring. Den '
 'begynder med sikkerhed, procesforståelse og et fælles billede af problemerne. Derefter følger '
 'årsagsanalyse, et afgrænset forsøg og opfølgning med operatører og vedligehold. Først når resultatet '
 'holder i driften, skal løsningen udbredes.')

MIRROR = ('Mit fundament er B.Tech i Technology Management & Mechanical Engineering og elautorisation som '
 'elautoriseret maskinmester (LV/MV/HV), suppleret med praktisk el- og mekanisk arbejde. Jeg søger den '
 'udførende og forbedrende ingeniørrolle tæt på udstyret; tidligere personale- og P&L-ansvar er '
 'erfaring at trække på, ikke et krav om en lederstilling.')

HONEST = ('Jeg har ikke dokumenteret erfaring fra CR-pumpeproduktion, NPI eller gennemførte Industri '
 '4.0-pilotprojekter på en fabrik. Det skal læres med kollegerne. Min erfaring med drift, tekniske '
 'investeringer, test og egne digitale værktøjer er et konkret udgangspunkt, men ikke det samme som at '
 'kende Grundfos’ processer og produktionssystemer.')

CULTURE = ('Grundfos’ vægt på åbenhed og mennesker passer til en arbejdsform, hvor vi lægger fakta frem og bruger '
 'hinandens erfaring. Jeg er professionel Claude-bruger og koder. Mine Python/Claude API-værktøjer til '
 'tilbud, planlægning, KS og KPI har givet over 40 % produktivitetsløft i entreprisedrift. Hos Grundfos '
 'skal eventuel anvendelse følge godkendte systemer og dataregler og kunne forsvares både teknisk og '
 'praktisk.')

PRACTICAL = ('Jeg bor i Måløv. Rollen er placeret på fabrikken i Bjerringbro, så en holdbar løsning for '
 'tilstedeværelse, eventuelt ophold eller flytning, samt start og overgangen fra ELOHVAC skal aftales. '
 'Jeg forudsætter ikke, at hjemmearbejde kan erstatte arbejdet ved linjerne.')

CLOSING = ('Jeg vil gerne høre, hvilke driftsproblemer og udstyrsinvesteringer ME-teamet først har brug for hjælp '
 'til, og drøfte hvordan min praktiske og projektmæssige erfaring kan bruges.')

# ------------------------------------------------------------------ CV
PROFILE = ('Produktionsudstyr skal fungere sikkert i hverdagen, og forbedringer skal kunne ses i oppetid og flow. '
 'Min baggrund er elektromekanisk fejlfinding, kritisk anlægsdrift, tekniske projekter og dokumenteret '
 'aflevering. B.Tech og elautoriseret maskinmester (LV/MV/HV). Hos Biofos arbejdede jeg med pumper, '
 'HVAC, HV og SCADA; hos Novo koordinerede jeg 25 specialister på 37 CAPEX-projekter og arbejdede med '
 'FAT/SAT. Jeg søger en hands-on Manufacturing Engineer-rolle, ikke personaleansvar. CR-processer, NPI '
 'og fabrikkens Industri 4.0-arbejde vil være nyt. Professionel Claude-koder med egne værktøjer til '
 'planlægning og kvalitet.')

PRACTICE = [('Teknisk support og fejlfinding',
  'Biofos: forebyggende vedligehold, akut fejlfinding og reservedelsflow i kritisk 24/7-drift med '
  'pumper, HVAC, højspændingstavler og SCADA. ARJ Engineering: fejldiagnose og reparation af '
  'industrielle el- og mekaniske anlæg.'),
 ('Problemløsningsværktøjer og LEAN',
  '5S, Standard Work og PDCA i Biofos-værksted/lager. A3, 5xHvorfor og Ishikawa i teknisk arbejde hos '
  'Novo. Ventek: tavlemøder og flaskehalsanalyse. Metoderne skal bruges på det observerede problem og '
  'følges op med dem, der udfører arbejdet.'),
 ('Investeringer og tekniske leverancer',
  'Novo: 37 CAPEX-projekter à DKK 2–10 mio. med koordinering af 25 specialister på tværs af '
  'engineering, indkøb og anlæg. Fremdrift, økonomi, risici og ressourcer samt rapportering til '
  'bygherre og ledelse.'),
 ('Test og overdragelse',
  'FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA hos Novo uden kritiske fund ved aflevering. Erfaring med at '
  'følge test, afklaringer og dokumentation til accept; fabrikkens egne kriterier og udstyrsstandarder '
  'skal læres.'),
 ('Data og digitale værktøjer',
  'Excel/Power Query, Power BI, Python og Claude API. SAP til økonomi, aktiver og omkostninger. Egne '
  'værktøjer har givet over 40 % produktivitetsløft i entreprisedrift, ikke et dokumenteret '
  'pumpeproduktionsresultat.'),
 ('Sikkerhed og samarbejde',
  'LOTO, APV og risikovurdering fra installations- og driftsarbejde. ELOHVAC: daglig planlægning og '
  'oplæring af 5 elektrikere/3 lærlinge. Ventek: team på 14 på 11 projekter. Erfaringen bruges til '
  'samarbejde og tydelige aftaler i en specialistrolle.')]

MODELS = [('Se problemet ved linjen',
  'Gennemgå forløbet med operatører og vedligehold. Skeln mellem observeret fejl, antagelse og det, der '
  'mangler at blive undersøgt.'),
 ('PDCA og årsagsanalyse',
  'Brug A3/5xHvorfor/Ishikawa efter opgavens behov. Afprøv en afgrænset ændring og sammenlign med et '
  'aftalt udgangspunkt.'),
 ('5S og Standard Work',
  'Træk på Biofos-erfaringen. Gør løsningen enkel at bruge, og afstem ændringer med dem, der skal '
  'arbejde efter standarden.'),
 ('Data og effekt',
  'Aftal definitioner og datakilder for stop og ventetid. Kontrollér registreringerne mod det faktiske '
  'forløb, før der konkluderes.'),
 ('Udstyr og accept',
  'Afklar krav med produktion og vedligehold. Følg tekniske leverancer, FAT/SAT, dokumentation og åbne '
  'punkter til aftalt overdragelse.'),
 ('Plan og ansvar',
  'Brug kort opfølgning og flaskehalsanalyse. Afklar næste handling og beslutningsejer; en enkel '
  'ansvarsmatrix (RACI) kan bruges, hvor det hjælper.')]

ACHIEVEMENTS = [('37 CAPEX-projekter hos Novo Nordisk',
  'DKK 2–10 mio. pr. projekt; koordinering af 25 specialister på tværs af engineering, indkøb og '
  'anlæg.'),
 ('Aflevering uden kritiske fund', 'FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA hos Novo Nordisk.'),
 ('40 % lavere energiomkostninger hos Novo',
  'PDCA-program; ikke en påstået forbedring af oppetid eller produktionsflow i pumpefremstilling.'),
 ('Over 40 % produktivitetsløft i entreprisedrift',
  'Egne Python/Claude API-værktøjer til tilbud, planlægning, KS og KPI-opfølgning.')]

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

PRACTICAL_CV = ('Bopæl i Måløv (Ballerup Kommune). Stillingen er en onsite-rolle på CR-pumpefabrikken i Bjerringbro. '
 'Tilstedeværelse, eventuelt ophold/flytning, startdato og overgang fra ELOHVAC skal aftales; ingen '
 'flytning eller fast hjemmearbejdsordning lovet. Dansk og persisk/farsi på modersmålsniveau, engelsk '
 'professionelt i skrift og tale. Kørekort B. B.Tech og elautoriseret maskinmester (LV/MV/HV).')

REFERENCES = 'Tidligere ledere hos Novo Nordisk og Biofos (Lynetten) — oplyses efter aftale.'

PARTNER = [('Operatørerne',
  'Spørge til forløbet, se udstyret i arbejde og gøre næste handling tydelig. Deres erfaring skal med i '
  'både årsagsanalyse og afprøvning. En løsning er først brugbar, når den også fungerer for dem i '
  'hverdagen.'),
 ('Vedligehold og tekniske fagpersoner',
  'Aftale sikker adgang og afprøvning, følge fejl og reservedele og få konsekvenserne for vedligehold '
  'vurderet. Ændringer skal følge fabrikkens godkendelser og opgavefordeling; min elautorisation er '
  'ikke en lokal udpegnings- eller koblingstilladelse.'),
 ('ME-teamet og projektkolleger',
  'Følge aftalte opgaver i investeringer, nyt udstyr og New Product Introduction. Koble afklaringer og '
  'test til planen og gøre behov for specialiststøtte synligt. CR-processer og NPI-arbejdsgange læres '
  'med de erfarne kolleger.'),
 ('Data- og digitaliseringskolleger',
  'Starte med driftsproblemet, få adgang og databrug godkendt og undersøge kvaliteten af '
  'registreringerne. Jeg kan bidrage med Python og analyse, men påstår ikke erfaring med fabrikkens '
  'MES, PLC-platforme eller gennemførte Industri 4.0-piloter.')]

FIRST90 = [('Første uge',
  'Lære fabrikkens sikkerhedsregler og den valgte linje sammen med operatører, vedligehold og '
  'ME-teamet. Følge en konkret fejl eller flaskehals og gennemgå eksisterende registreringer. Aftale '
  'ansvar, støtte og hvilke opgaver jeg kan tage i den daglige support. Samle åbne spørgsmål og næste '
  'handling.'),
 ('Inden dag 30',
  'Vælge én forbedringsopgave med teamet ud fra stop, ventetid og driftsbehov. Kontrollere '
  'datagrundlaget og aftale et målbart udgangspunkt, fx stopminutter for den valgte fejl. Lære de '
  'relevante SAP-arbejdsgange. Gennemgå en aktuel udstyrs- eller NPI-opgave med den ansvarlige for at '
  'forstå krav, plan og accept.'),
 ('Inden dag 60',
  'Gennemføre årsagsanalyse og et sikkert, afgrænset forsøg med de relevante fagpersoner. Sammenligne '
  'resultatet med udgangspunktet og justere. Følge en aftalt teknisk leverance eller testaktivitet på '
  'nyt udstyr. Afklare, om et digitalt pilotforsøg giver mening, før der vælges teknologi og bruges '
  'produktionsdata.'),
 ('Inden dag 90',
  'Vurdere med operatører og vedligehold, om forbedringen holder i normal drift. Dokumentere ændringen '
  'og aftale standard, ejer og opfølgning. Gennemgå bidrag til udstyr/NPI og næste forbedringsbehov med '
  'ME-lederen. Aftale videre opgaver og læring ud fra erfaringerne; en digital pilot skaleres kun, hvis '
  'effekten og driftsstøtten er på plads.')]

KEYWORDS = ('Elektromekanisk fejlfinding · Pumper og SCADA · Forebyggende vedligehold · PDCA, A3, 5xHvorfor og '
 'Ishikawa · 5S og Standard Work · Tekniske projekter og CAPEX · FAT/SAT · LOTO og risikovurdering · '
 'SAP økonomi/aktiver · Excel/Power Query · Python og Claude API.')


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

    m.models_table("PROBLEMLØSNING OG TEKNISK SAMARBEJDE",
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
    m.models_table("FØRSTE 90 DAGE — LINJE, DATA OG FORBEDRING",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SAMARBEJDET I HVERDAGEN")
    for label, body in PARTNER:
        m.bullet(label, body, after=30)

    m.section("FRA FEJL TIL EN FORBEDRING, DER HOLDER")
    m.para('Jeg vil følge én tilbagevendende fejl fra første symptom til genstart sammen med operatør og vedligehold. Hvad skete der faktisk, hvor blev det registreret, og hvad er endnu kun en forklaring? Analysen skal føre til en ændring, der kan testes uden at tilsidesætte sikkerhed eller kvalitet. Før forsøget aftaler vi, hvad vi vil måle, og hvem der kan godkende det. Bagefter ser vi på resultatet i normal drift, ikke kun i et enkelt vellykket forsøg. Hvis ændringen virker, skal dokumentation, standard og ansvar følge med. Ved nye digitale løsninger gælder samme princip: et kendt behov, troværdige data og en ejer, der kan støtte løsningen, når pilotprojektet er slut.', after=80)

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
    build(os.path.join(ROOT, "Shahram_Ajloo_Grundfos_ManufacturingEngineer.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_Grundfos_ManufacturingEngineer.docx"))
