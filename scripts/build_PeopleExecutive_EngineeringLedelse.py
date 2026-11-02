# -*- coding: utf-8 -*-
"""
People Executive — fortrolig Engineering-ledelse, Nordjylland.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Engineering-ledelse | Spillende træner | Standardisering, teamudvikling og ordreflow'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = '2. november 2026'
RECIPIENT = 'People Executive · Fortrolig international industrivirksomhed i Nordjylland'
SUBJECT = 'Ansøgning: Ledelse af Engineering — teknisk spillende træner'

# ------------------------------------------------------------------ side 1
INTRO = ['Engineering skal gøre kundeordren produktionsklar uden gentagne afklaringer, ventetid og tilbageløb. '
 'Med fem medarbejdere og reference til CTO bliver opgaven at beskytte den tekniske kvalitet, '
 'prioritere teamets kapacitet og skabe en fælles arbejdsform mellem konstruktion, produktion og salg. '
 'Den spillende træner skal bidrage fagligt uden selv at blive flaskehals for alle beslutninger.',
 'Den foreslåede arbejdsstruktur er klar til tilpasning fra første dag: en fælles opgave- og '
 'kapacitetstavle, en afklaringsliste før konstruktionsstart og en frigivelsestjekliste til '
 'PTA-funktionen. Et enkelt ændringsspor forbinder ordrekrav, teknisk dokumentation og '
 'produktionsgrundlag. Før systemer og organisation ændres, skal teamet og CTO have et fælles billede '
 'af, hvor flowet faktisk bryder sammen.']

BULLETS = [('Lede fem medarbejdere med retning og faglig nærhed',
  'Aftal prioriteringer, ansvar og beslutningsgrænser med CTO. Brug korte tavlemøder og regelmæssige '
  '1:1-samtaler til fremdrift, kvalitet og kompetenceudvikling. Afsæt tid til eget teknisk bidrag og '
  'specialistreview, men delegér tydelige opgaver, så teamets løsninger ikke afventer én person.'),
 ('Standardisere konstruktion med produktionen',
  'Udpeg sammen med erfarne konstruktører en tilbagevendende produkt-/opgavetype til pilot. Gennemgå '
  'modulgrænser, grænseflader, tolerancer, materialer, montage og serviceadgang med produktionen efter '
  'Design for Manufacturing-principper. Standarder skal bygge på valideret teknisk grundlag; modulære '
  'løsninger er en foreslået retning, ikke en påstået tidligere produktplatform.'),
 ('Reducere flaskehalse og tilbageløb i kundeordrer',
  'Afklar krav og undtagelser med salg før konstruktion; prioritér efter leveringsbehov, risiko og '
  'tilgængelig kapacitet. Gør årsagen til hver tilbagelevering synlig. PTA-grundlaget skal have aftalt '
  'scope, relevante tegninger, styklister, revisioner og åbne afklaringer, før det frigives efter '
  'virksomhedens proces.'),
 ('Digitalisere et sammenhængende produktionsgrundlag',
  'Kortlæg hvem der ejer data, revisioner og ændringer mellem ERP og PLM/PDM. Test én repræsentativ '
  'kundeordre fra salgsafklaring til produktionsgrundlag, før automatisering skaleres. SAP og '
  'Python/Claude er dokumenteret erfaring; PLM/PDM og den aktuelle konstruktionsplatform kræver konkret '
  'oplæring.'),
 ('Udvikle tekniske løsninger med de rette kompetencer',
  'Inddrag eksterne tekniske specialister og interne fagansvarlige ved beregninger, maskinsikkerhed og '
  'særlige krav. FEM og ATEX er ikke dokumenterede kompetencer i CV’et. Aftal review- og '
  'godkendelsesansvar, så en travl ordre ikke bliver anledning til at springe teknisk vurdering over.')]

SYSTEM = ('Første uge afklares CTO’s mandat, teamets styrker og de vigtigste ordreblokeringer. Dag 30 foreligger '
 'en baseline for ventetid, tilbageløb og rettidig frigivelse. Dag 60 afprøves én standardiserings- og '
 'dataflowpilot. Dag 90 vurderes effekt, kompetencebehov og næste udviklingstrin på dokumenteret '
 'grundlag, ikke på et på forhånd opfundet besparelsesmål.')

MIRROR = ('Ledelses- og flowgrundlaget er dokumenteret: ELOHVAC med 5 elektrikere og 3 lærlinge, daglig '
 'prioritering, oplæring og fuldt P&L; Ventek-Air med 11 samtidige projekter, 14 medarbejdere, '
 'tavlemøder og flaskehalsanalyse; Novo Nordisk med 37 CAPEX-projekter og koordinering af 25 '
 'specialister. Egne Python/Claude API-værktøjer til tilbud, planlægning, KS og KPI har givet over 40 % '
 'produktivitetsløft i entreprisedrift.')

HONEST = ('B.Tech i Technology Management & Mechanical Engineering og elautoriseret maskinmester (LV/MV/HV) er '
 'det tekniske fundament. CV’et dokumenterer ikke solid nyere mekanisk produktkonstruktion, Design for '
 'Manufacturing, PLM/PDM, FEM, ATEX eller maskinsikkerhedsansvar. Det er væsentlige faglige huller i en '
 'spillende træner-rolle og kræver en reel afklaring af eget konstruktionsbidrag og specialiststøtte.')

CULTURE = ('Briefet peger på ejerskab, teknisk nærhed og samarbejde på tværs. Det omsættes til synlige '
 'prioriteringer, respekt for konstruktørernes faglighed og korte feedbacksløjfer mellem salg og '
 'produktion. Virksomheden er fortrolig; der tillægges den ikke værdier eller interne ledelsesmodeller, '
 'som ikke er oplyst.')

PRACTICAL = ('Bopæl er Måløv. En daglig rolle i Nordjylland kræver en konkret aftale om arbejdssted og base/ophold; '
 'flytning eller hjemmearbejde er ikke forudsat. Startdato og ordningen for ELOHVAC skal aftales. Dansk '
 'og engelsk beherskes professionelt.')

CLOSING = ('En første vurdering bør afklare balancen mellem daglig mekanisk konstruktion og team-/procesledelse, '
 'samt om en teknisk drifts- og projektlederprofil kan løse opgaven med det nødvendige faglige '
 'supplement.')

# ------------------------------------------------------------------ CV
PROFILE = ('Opgaven er at gøre Engineering mere effektiv gennem prioritering, standardisering og sammenhæng '
 'mellem konstruktion, produktion og salg. Den dokumenterede styrke er teknisk ledelse: 5 elektrikere '
 'og 3 lærlinge med daglig planlægning og oplæring, 11 projekter/14 medarbejdere hos Ventek-Air og '
 'koordinering af 25 specialister hos Novo Nordisk. B.Tech og elautoriseret maskinmester (LV/MV/HV). '
 'Professionel Claude-koder med egne Python/Claude API-værktøjer og >40 % produktivitetsløft. Nyere '
 'mekanisk produktkonstruktion, DFM, PLM/PDM og beregnings-/maskinsikkerhedsansvar er ikke dokumenteret '
 'og skal afklares før et selvstændigt konstruktionsmandat.')

PRACTICE = [('Ledelse og udvikling — dokumenteret praksis',
  'ELOHVAC: 5 elektrikere og 3 lærlinge, daglig planlægning, 1:1/MUS, struktureret oplæring og '
  'situationsbestemt ledelse. Overføres til tydelige opgaver og feedback; ikke en påstand om tidligere '
  'personaleledelse af et mekanisk konstruktionsteam.'),
 ('Kapacitet og flaskehalse — dokumenteret praksis',
  'Ventek-Air: 11 samtidige projekter og 14-personers team; tavlemøder, kapacitetsstyring og '
  'flaskehalsanalyse. Relevant for prioritering og fremdrift, ikke dokumenteret produktionsmodning af '
  'en maskinplatform.'),
 ('Tværfaglig koordinering — dokumenteret praksis',
  'Novo: 37 CAPEX-projekter, DKK 2–10 mio. pr. projekt, og 25 specialister på tværs af engineering, '
  'indkøb og anlæg. Fremdrift, risici og ressourcer fulgt og rapporteret til ledelse og bygherre.'),
 ('Kvalitet og dokumentation — dokumenteret praksis',
  'FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA, nul kritiske fund ved aflevering. ELOHVAC: KS og '
  'afleveringsgrundlag. Ikke en erstatning for produktkonstruktion, maskinsikkerhed eller '
  'ATEX-vurdering.'),
 ('Digitalisering — dokumenteret praksis og grænse',
  'SAP til økonomi, aktiver og omkostninger; Python/Claude API-værktøjer til beregning, planlægning, KS '
  'og KPI. PLM/PDM, CAD-platform og dataejerskab kræver oplæring; automatisering må ikke frigive '
  'teknisk materiale uden faglig kontrol.'),
 ('Mekanisk fundament — dokumenteret praksis og læringsbehov',
  'ARJ: elektromekanisk fejldiagnose/reparation, materialestyring og ledelse af 12 teknikere. Biofos: '
  'pumper, HVAC og kritisk vedligehold. Det etablerer ikke solid nyere erfaring med mekanisk '
  'konstruktion, DFM eller modulære produktløsninger.')]

MODELS = [('Prioritering og kapacitet',
  'Fælles tavle: opgave, kundeordre, deadline, kapacitet, blokering, ejer og næste handling. CTO '
  'afklarer konflikter og mandat.'),
 ('Krav før konstruktion',
  'Afklaringsliste med salg/produktion: funktion, scope, grænseflader, undtagelser og tekniske '
  'beslutninger før konstruktionsstart.'),
 ('Standardisering og DFM',
  'Pilot med erfarne konstruktører/produktion: modulgrænser, tolerancer, materialer, montage og '
  'service. Fagansvarlige validerer løsningen.'),
 ('ERP–PLM/PDM-flow',
  'Aftalt dataejer og revisions-/ændringsspor fra ordre til produktionsgrundlag. Test en konkret ordre '
  'før skalering.'),
 ('Ledelse og feedback',
  'Dokumenteret 1:1/MUS, oplæring og tavlemøder; foreslået RACI, GROW/SBI og kompetencematrix for '
  'delegering og udvikling.'),
 ('Tilbageløb og læring',
  'PDCA/A3/5xHvorfor til gentagne fejl og ventetid. Kontrollér effekt efter ændring; ingen automatisk '
  'lighed mellem færre timer og bedre kvalitet.')]

ACHIEVEMENTS = [('5 elektrikere og 3 lærlinge',
  'Direkte ledelse, daglig prioritering, oplæring og fuldt P&L i ELOHVAC.'),
 ('11 projekter og 14 medarbejdere',
  'Ventek-Air: specifikation til aflevering, kapacitetsstyring og daglige tavlemøder.'),
 ('37 CAPEX-projekter og 25 specialister',
  'Novo Nordisk: tværfaglig koordinering og reguleret aflevering uden kritiske fund.'),
 ('Over 40 % produktivitetsløft',
  'Python/Claude API-værktøjer til beregning, planlægning, KS og KPI i entreprisedrift; ikke et løfte '
  'om samme gevinst i Engineering.')]

EXPERIENCE = [('Indehaver / teknisk direktør / elautoriseret maskinmester',
  'ELOHVAC ApS · København · maj 2023 – nu',
  '5 elektrikere + 3 lærlinge · fuldt P&L',
  [('Kunder og økonomi',
    'Tilbud, beregning, planlægning, materialer og underentreprenører; KS og afleveringsdokumentation '
    'på el-, ventilations- og klimaanlæg.'),
   ('Personale og sikkerhed',
    'Daglig planlægning, 1:1/MUS og lærlingeoplæring; LOTO, APV og risikovurdering. Nul kritiske '
    'afvigelser i serviceaftalerne.'),
   ('Digital forbedring',
    'Python/Claude API-værktøjer til tilbud, tidsplaner, KS og KPI; produktivitetsløft over 40 %.')]),
 ('Senior idriftsættelsesingeniør / projektleder, elsystem',
  'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
  '37 samtidige CAPEX-projekter á DKK 2–10 mio. · 25 specialister',
  [('Tværfaglig koordinering',
    'Fremdrift, økonomi, risici og ressourcer på tværs af engineering, indkøb og anlæg; rapportering '
    'til ledelse og bygherre.'),
   ('Kvalitet og energi',
    'FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA, nul kritiske fund ved aflevering. PDCA gav 40 % lavere '
    'energiomkostninger; SAP ERP til økonomi og aktiver.')]),
 ('Projekt- og værkstedsleder',
  'Ventek-Air · København · jan. 2022 – nov. 2022',
  '11 samtidige projekter · 14-personers team',
  [('Kapacitet og leverance',
    'Specifikation til formel aflevering; tilbud, underentreprenører, sikkerheds- og '
    'afleveringsdokumentation. Daglige tavlemøder og flaskehalsanalyse.')]),
 ('Vedligeholdelses- og driftsleder / værkstedstekniker',
  'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
  'Kritisk 24/7-drift · pumper, HVAC, højspændingstavler og SCADA',
  [('Drift og vedligehold',
    'Forebyggende vedligehold, akut fejlfinding og reservedelsflow. 5S, Standard Work og PDCA på '
    'værksted/lager; LOTO, APV og nærved-hændelser.')]),
 ('Elektromekaniker / produktionsteamleder',
  'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
  '12 mekanikere og teknikere',
  [('Ledelse og problemløsning',
    'Vagtplanlægning, materialestyring og målopfølgning; fejldiagnose, rodårsagsanalyse og reparation '
    'af industrielle el- og mekaniske anlæg.')])]

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

PRACTICAL_CV = ('Bopæl Måløv (Ballerup Kommune). Virksomheden ligger i Nordjylland; præcist arbejdssted og en '
 'realistisk aftale om base/ophold skal afklares. Ingen flytning, daglig langdistancependling eller '
 'hjemmearbejdsordning er lovet. Startdato og ELOHVAC-ordning skal aftales. Dansk/persisk på '
 'modersmålsniveau, engelsk professionelt; kørekort B. B.Tech og elautoriseret maskinmester (LV/MV/HV). '
 'Solid nyere mekanisk konstruktion, DFM, PLM/PDM, FEM, maskinsikkerhed og ATEX er ikke dokumenteret; '
 'eget teknisk mandat kræver eksplicit fit- og kompetenceafklaring.')

REFERENCES = 'Tidligere ledere hos Novo Nordisk og Biofos (Lynetten) — oplyses efter aftale.'

PARTNER = [('CTO og Engineeringteamet',
  'CTO fastlægger retning og delegeret mandat; teamet får klare prioriteter og faglig sparring. Beskyt '
  'tid til teknisk fordybelse, og gør flaskehalse og ressourcemangler synlige uden at overtage alle '
  'opgaver.'),
 ('Salg og kundeordreansvarlige',
  'Afklar krav, afvigelser og leveringsforudsætninger før konstruktion. Tekniske ændringer efter '
  'opstart får synlig konsekvens for scope, pris og tid; salgsønsker bliver ikke automatisk '
  'konstruktionskrav.'),
 ('Produktion og PTA',
  'Review produktionsvenlighed, montage, materialer og relevante instrukser tidligt. Frigiv kun efter '
  'aftalt modenhed og kompetent godkendelse; produktionens tilbagemeldinger føres tilbage til '
  'standarder og dokumentation.'),
 ('Eksterne specialister og systemansvarlige',
  'Brug fagkyndige til mekaniske beregninger, FEM, maskinsikkerhed og ATEX efter behov. '
  'Systemansvarlige validerer data-/revisionsflow og adgang; digitalisering ændrer ikke det tekniske '
  'godkendelsesansvar.')]

FIRST90 = [('Første uge',
  'CTO og teamet afklarer mandat, prioriteringsregler og balancen mellem eget teknisk arbejde og '
  'ledelse. Hold 1:1 med alle fem; følg en kundeordre sammen med salg, konstruktion og produktion. '
  'Leverance: fælles opgaveoversigt, vigtigste blokeringer og afklaret fagligt reviewansvar.'),
 ('Dag 30',
  'Mål ventetid, tilbageløb, åbne afklaringer og rettidig frigivelse på et afgrænset ordreudsnit. '
  'Kortlæg dataejerskab/revisioner i ERP og PLM/PDM. Vælg en tilbagevendende opgavetype til '
  'DFM-/standardiseringspilot med de kompetente konstruktører. Leverance: baseline og CTO-godkendt '
  'pilotmål.'),
 ('Dag 60',
  'Afprøv kravtjek, standardiseret review og PTA-frigivelse på én repræsentativ kundeordre. Gennemgå '
  'data-/revisionssporet og dokumentér fejl, ejere og korrektioner. Fagansvarlige vurderer konstruktion '
  'og sikkerhed. Leverance: valideret pilotgrundlag, instruktion og aftalt opfølgning i produktionen.'),
 ('Dag 90',
  'Sammenhold piloten med baseline for tilbageløb, ventetid, kvalitet og rettidig eksekvering. Review '
  'teamets kapacitet og kompetenceudvikling med CTO. Beslut hvad der skal standardiseres og skaleres, '
  'og hvilke faglige huller der fortsat kræver støtte. Leverance: prioriteret udviklingsplan og '
  'tydeligt ejerskab.')]

KEYWORDS = ('Opgavens fokus: Engineering · spillende træner · CTO · Technical Operations · konstruktion · '
 'standardisering · modulære, produktionsvenlige løsninger · produktion · salg · flaskehalse · tilbageløb · digitalisering '
 '· ERP · PLM/PDM · PTA-funktion · kundeordre · teknisk dokumentation · Design for Manufacturing · FEM '
 '· maskinsikkerhed · ATEX · automatisering. Konstruktions-, beregnings- og sikkerhedstermer angiver '
 'opgaven og læringsbehov; ikke dokumenteret specialistkompetence.')


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

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("FORESLÅET ARBEJDSMODEL — KRAV TIL PRODUKTIONSKLAR ORDRE",
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

    m.section("KERNEKOMPETENCER & NØGLEORD")
    m.para(KEYWORDS, after=80)

    # afsluttende side
    m.page_break()
    m.models_table("FØRSTE 90 DAGE — TEAM, ORDREFLOW OG STANDARDISERING",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SAMARBEJDE OG BESLUTNINGSANSVAR")
    for label, body in PARTNER:
        m.bullet(label, body, after=30)

    m.section("PILOTKONTROL — FRA ORDREKRAV TIL PTA-FRIGIVELSE")
    m.para("Følg en afgrænset kundeordre fra godkendte krav til produktion. Kontrollér sammenhæng mellem konstruktion, tegninger, styklister og revisioner i de aftalte systemer. Registrér hvem der må ændre og frigive data, og hvordan undtagelser fra standarden håndteres. Lad kompetente konstruktører og produktionen gennemgå tolerancer, montage og dokumentation; særlige beregnings- og sikkerhedskrav vurderes af fagansvarlige. Test ændringssporet på en konkret revision, så forældet materiale ikke følger med ud i produktionen. Mål bagefter tilbageløb og afklaringsbehov, ikke kun gennemløbstid. CTO godkender skalering efter evidens; automatisering må ikke gøre fejl hurtigere eller fjerne nødvendigt review.", after=80)

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
    build(os.path.join(ROOT, "Shahram_Ajloo_PeopleExecutive_EngineeringLedelse.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_PeopleExecutive_EngineeringLedelse.docx"))
