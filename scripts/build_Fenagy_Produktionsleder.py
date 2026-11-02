# -*- coding: utf-8 -*-
"""
Fenagy — produktionsleder, el-assembly, isolering og final preparation.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Produktionsleder | Fenagy | El-assembly, isolering og final preparation'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = '2. november 2026'
RECIPIENT = 'Fenagy A/S · Produktionsdirektør Torben Nissen · Lystrup'
SUBJECT = 'Ansøgning: Produktionsleder med elbaggrund'

# ------------------------------------------------------------------ side 1
INTRO = ['Kvaliteten skal være synlig, før anlægget forlader Fenagy: korrekt fortrådning og montage, færdig '
 'isolering og en udgangskontrol, hvor dokumentation, mærkning og pakning stemmer med det konkrete '
 'anlæg. Produktionslederens opgave er at samle cirka 30 medarbejdere om sikker eksekvering og et '
 'stabilt flow gennem el-assembly, isolering og final preparation – også når kundeordrerne er '
 'forskellige.',
 'Den foreslåede arbejdsstruktur er klar til tilpasning fra første dag: en fælles bemandings- og '
 'kapacitetstavle, klare overleveringskriterier mellem de tre områder og en slutkontrolliste knyttet '
 'til anlæggets identitet og revision. Afvigelser bliver i Fenagys NCR-system med ejer, årsag, handling '
 'og effektkontrol. Systemet skal understøtte den eksisterende ISO 9001-produktion, ikke indføre en '
 'parallel kvalitetsproces.']

BULLETS = [('Være synlig og tydelig på gulvet',
  'Start med korte tavlemøder og en daglig runde gennem alle tre områder. Afklar dagens mål, '
  'sikkerhedsforhold, mangler og hjælp til kollegerne. Regelmæssige 1:1- og MUS-samtaler kobler trivsel '
  'og udvikling til konkrete kompetencer; ansvar og frihed følges af klare forventninger og '
  'opfølgning.'),
 ('Planlægge bemanding og flow på tværs',
  'Afstem med planlægning og projekt, hvilke anlæg der reelt er klar til næste proces. Brug en '
  'kompetencematrix til elektrikere, eltestere, isolatører og final prep, så kapacitet ikke kun tælles '
  'som antal personer. Synliggør manglende materiale, afklaring eller testgrundlag, før arbejdet '
  'flyttes videre.'),
 ('Fastholde kvalitet fra eltavle til shipping',
  'Aftal med eldesign og kvalitet det godkendte grundlag for montage, eltest, isolering og '
  'udgangskontrol. Kontrollér relevante dokumenter, mærkning, pakning og klargøring til shipping efter '
  'den konkrete ordre. Afvigelser og åbne punkter skal have en godkendt håndtering før frigivelse; '
  'produktionspres ændrer ikke acceptkriterierne.'),
 ('Bruge NCR til at forhindre gentagelser',
  'Skeln mellem korrektion af det aktuelle anlæg og korrigerende handlinger mod årsagen. Brug A3, '
  '5xHvorfor og Ishikawa ved tilbagevendende fejl. Giv hver handling ejer og frist, og kontrollér '
  'effekt på efterfølgende arbejde; en lukket registrering er ikke automatisk et løst problem.'),
 ('Forbedre sikkerhed og procesdisciplin',
  'Anvend LEAN, 5S, Standard Work og PDCA til orden, korte overleveringer og færre tilbageløb. LOTO, '
  'APV og risikovurdering er dokumenteret praksis. CO₂-anlæg, test, tryk og isolering kræver Fenagys '
  'lokale instruktioner og kompetente fagansvarlige; forbedringer skal bevare sikkerhed og sporbarhed.')]

SYSTEM = ('Første uge fastlægges ledelsesmandat, daglig rytme og de største flow-/sikkerhedsproblemer med '
 'produktionsdirektøren. Dag 30 foreligger kompetence- og kapacitetsbillede samt baseline for NCR, '
 'omarbejde og rettidig overlevering. Dag 60 afprøves én forbedring på et afgrænset anlægsflow. Dag 90 '
 'vurderes effekt, medarbejderudvikling og næste prioriteringer uden opfundne procentløfter.')

MIRROR = ('Ledelsesgrundlaget er praktisk: ELOHVAC med 5 elektrikere og 3 lærlinge, daglig planlægning, 1:1/MUS, '
 'oplæring og fuldt P&L; Ventek-Air med 14 medarbejdere, 11 projekter og flaskehalsanalyse; ARJ med '
 'ledelse af 12 mekanikere og teknikere i produktion. Novo Nordisk bidrager med koordinering af 25 '
 'specialister og reguleret aflevering uden kritiske fund.')

HONEST = ('Elautoriseret maskinmester (LV/MV/HV), B.Tech og køleteknik/klimaanlæg fra Mercantec er det tekniske '
 'fundament. Direkte ledelse af 30 medarbejdere, CO₂-varmepumpeproduktion, isolerings-/final '
 'prep-ledelse, Fenagys NCR-system og praktisk læsning af PI-diagrammer er ikke dokumenteret. De '
 'områder skal afklares og indgå i en konkret oplæringsplan; kursusbaggrund er ikke en '
 'CO₂-specialistautorisation.')

CULTURE = ('Fenagys åbenhed, ærlighed, tillid og ansvar omsættes til tidlig eskalering af fejl, klare aftaler og '
 'støtte til medarbejderne. Virksomhedens fokus på effektive, kundetilpassede energiløsninger kræver, '
 'at forbedringer hjælper næste proces og i sidste ende kunden. Professionel Claude-koder: egne '
 'Python/Claude API-værktøjer til planlægning, KS og KPI har givet over 40 % produktivitetsløft i '
 'entreprisedrift; ikke et løfte om samme gevinst her.')

PRACTICAL = ('Bopæl er Måløv. En daglig produktionsrolle i Lystrup kræver en konkret aftale om base/ophold; '
 'flytning eller hjemmearbejde er ikke forudsat. Startdato og ordningen for ELOHVAC skal aftales. Dansk '
 'og engelsk beherskes professionelt.')

CLOSING = ('En første samtale kan afklare de vigtigste udfordringer mellem de tre områder, mandatet omkring '
 'bemanding og frigivelse samt en realistisk løsning for daglig tilstedeværelse i Lystrup.')

# ------------------------------------------------------------------ CV
PROFILE = ('Opgaven er at lede medarbejdere og sikre flow, sikkerhed og kvalitet fra el-assembly gennem isolering '
 'til final preparation. Fundamentet er elautoriseret maskinmester (LV/MV/HV), B.Tech og praktisk '
 'teknisk ledelse i produktion, projekter og entreprisedrift. ELOHVAC: 5 elektrikere/3 lærlinge, '
 'planlægning, MUS og oplæring. Ventek-Air: 14-personers team; ARJ: 12 mekanikere/teknikere. Novo: '
 'koordinering af 25 specialister og reguleret aflevering. Professionel Claude-koder med '
 'Python/Claude-værktøjer og >40 % produktivitetsløft. Ledelse af 30, CO₂-produktion, PI-diagrammer og '
 'de konkrete isolerings-/slutkontrolprocesser kræver afklaring og lokal oplæring.')

PRACTICE = [('Nærværende personaleansvar — dokumenteret praksis',
  'ELOHVAC: daglig planlægning af 5 elektrikere og 3 lærlinge, 1:1/MUS, struktureret oplæring og '
  'opfølgning på arbejdsmiljø. Situationsbestemt ledelse tilpasses erfaring og opgave; 30 direkte '
  'referencer er en ny skala.'),
 ('Produktion og kapacitet — dokumenteret praksis',
  'ARJ: produktions-/værkstedsteam på 12, vagtplaner, materialer og mål. Ventek-Air: 14 medarbejdere, '
  '11 samtidige projekter, tavlemøder og flaskehalsanalyse; relevant for daglig prioritering og '
  'eksekvering.'),
 ('El og tekniske snitflader — dokumenteret praksis',
  'ELOHVAC: installationer, tavler, styring og el-/ventilations-/klimaanlæg. Biofos: pumper, HVAC, HV '
  'og SCADA. Eltegninger gennemgås mod konkret anlæg; praktisk PI-diagramrutine skal verificeres, ikke '
  'udledes af elautorisation.'),
 ('Kvalitet og afvigelser — dokumenteret praksis',
  'Novo: FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA med nul kritiske fund ved aflevering. ELOHVAC: KS og '
  'afleveringsdokumentation. NCR-arbejdsgangen hos Fenagy er ny; reguleret aflevering er ikke '
  'dokumenteret ISO 9001-systemansvar.'),
 ('LEAN, sikkerhed og forbedring — dokumenteret praksis',
  '5S, Standard Work, PDCA, A3/5xHvorfor og Ishikawa; LOTO, APV og risikovurdering. Novo: 40 % lavere '
  'energiomkostninger via PDCA; ikke en påstået reduktion i Fenagys fejl eller produktionstid.'),
 ('Digital støtte og medarbejderudvikling',
  'Python/Claude API-værktøjer til tilbud, planlægning, KS og KPI gav >40 % produktivitetsløft. '
  'Foreslået kompetencematrix, GROW/SBI-feedback og RACI understøtter oplæring og ansvar; kun godkendte '
  'data og fagligt kontrollerede outputs.')]

MODELS = [('Daglig ledelse',
  'Tavle og gulvrunde: sikkerhed, bemanding, klar-til-næste-proces, blokering, ejer og næste handling. '
  'Dokumenteret tavlemødepraksis.'),
 ('Kompetence og kapacitet',
  'Kompetencematrix for el-assembly, eltest, isolering og final prep; bemanding afstemmes med faktisk '
  'procesklarhed og træningsbehov.'),
 ('Overlevering og slutkontrol',
  'Godkendte kriterier for montage/test/isolering; dokumentation, mærkning, pakning og '
  'frigivelsesansvar kobles til anlæg og revision.'),
 ('NCR og årsag',
  'Korrektion, årsag, korrigerende handling, ejer, frist og effektkontrol; A3/5xHvorfor/Ishikawa ved '
  'gentagelser.'),
 ('LEAN og sikkerhed',
  'Dokumenteret 5S/Standard Work/PDCA og LOTO/APV; lokale risici og instrukser valideres med '
  'fagansvarlige.'),
 ('MUS og udvikling',
  'Dokumenterede 1:1/MUS og lærlingeoplæring; foreslået GROW/SBI og tydelige kompetencemål med praktisk '
  'opfølgning.')]

ACHIEVEMENTS = [('5 elektrikere og 3 lærlinge',
  'Direkte ledelse, planlægning, MUS og struktureret oplæring i ELOHVAC.'),
 ('14-personers team og 11 projekter',
  'Ventek-Air: kapacitet, tavlemøder, flaskehalsanalyse og aflevering.'),
 ('25 specialister og nul kritiske fund',
  'Novo Nordisk: tværfaglig koordinering på 37 CAPEX-projekter under GMP/FDA/EMA.'),
 ('Over 40 % produktivitetsløft',
  'Egne Python/Claude API-værktøjer til beregning, planlægning, KS og KPI i teknisk entreprisedrift.')]

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

PRACTICAL_CV = ('Bopæl Måløv (Ballerup Kommune). Daglig tilstedeværelse i Lystrup kræver aftale om base/ophold; ingen '
 'flytning, pendlerordning eller hjemmearbejde er lovet. Startdato og ELOHVAC-overgang skal aftales. '
 'Dansk/persisk modersmål, engelsk professionelt; kørekort B. Elautoriseret maskinmester (LV/MV/HV), '
 'B.Tech og Mercantec køleteknik/klimaanlæg. Ingen påstået direkte ledelse af 30, '
 'CO₂-varmepumpeproduktionsspecialisme, PI-diagramrutine eller ISO 9001-/NCR-systemejerskab. Fenagys '
 'proces-, test-, sikkerheds- og systemkrav kræver lokal kompetenceafklaring.')

REFERENCES = 'Tidligere ledere hos Novo Nordisk og Biofos (Lynetten) — oplyses efter aftale.'

PARTNER = [('Produktionsdirektør og medarbejdere',
  'Afstem mål, bemandingsmandat og eskalering. Vær tæt på daglig drift, tag fejl alvorligt og støt '
  'medarbejdere med forskellige fagligheder. Tydelige aftaler og opfølgning gør frihed og ansvar '
  'praktisk anvendeligt.'),
 ('Planlægning og projekt',
  'Aftal rækkefølge og realistisk procesklarhed; synliggør materiale-/dokumentmangler og konsekvenser '
  'for leveringsevne tidligt. Undgå at flytte ufærdige anlæg videre blot for at vise lokal fremdrift.'),
 ('Eldesign og kvalitet',
  'Afklar elgrundlag, test-/acceptkriterier, NCR og ændringer med de kompetente ansvarlige. Produktion '
  'følger godkendt revision; eventuelle afvigelser håndteres gennem aftalt proces, ikke uformelle '
  'løsninger.'),
 ('Isolering, final prep og shipping',
  'Sikr overlevering mellem fagene og et entydigt slutgrundlag. Kontrollér, at isolering, '
  'dokumentation, mærkning og pakning opfylder ordrekravene. Frigivelse sker efter mandat og aftalte '
  'kriterier, ikke alene efter en planlagt afsendelsesdato.')]

FIRST90 = [('Første uge',
  'Produktionsdirektør og team afklarer mandat, bemanding og prioriteringer. Følg et anlæg gennem '
  'el-assembly, isolering og final preparation; gennemgå sikkerhed, instrukser og frigivelsesansvar. '
  'Leverance: daglig tavlerytme, vigtigste risici og plan for 1:1-/kompetenceafdækning.'),
 ('Dag 30',
  'Afstem kompetencer og kapacitet for de tre områder. Etablér baseline for omarbejde, NCR-gentagelser, '
  'åbne blokeringer og rettidig overlevering. Gennemgå eltegninger/PI-diagrammer med fagansvarlige; '
  'kortlæg test- og dokumentationskrav. Leverance: prioriteret forbedringsliste og oplæringsplan.'),
 ('Dag 60',
  'Afprøv klare overleveringskriterier og slutkontrolliste på et afgrænset anlægsflow. Gennemfør én '
  'årsagsanalyse og korrigerende handling i NCR med kvalitet. Afprøv bemandings-/kompetenceplan og '
  'lokale 5S-tiltag. Leverance: sporbare kontroller, ansvarlige og aftalt effektopfølgning.'),
 ('Dag 90',
  'Review flow, fejlmønstre, sikkerhedsopfølgning og medarbejderudvikling med produktionsdirektøren. '
  'Kontrollér, om piloten giver færre gentagelser uden skjult omarbejde i næste proces. Aftal '
  'standardisering, bemanding og næste udviklingstrin på evidens; MUS-/udviklingsaftaler følges op.')]

KEYWORDS = ('Opgavens fokus: produktionsleder · el-assembly · isolering · final preparation · fortrådning · '
 'montage · eltavler · eltestere · isolatører · final prep · udgangskontrol · dokumentation · mærkning '
 '· pakning · shipping · ISO 9001 · NCR-systemet · MUS-samtaler · bemanding · kapacitet · LEAN · '
 'eltegninger · PI-diagrammer · CO₂-varmepumper · køleanlæg. Fenagy-specifikke proces-/systemtermer '
 'beskriver opgaven og oplæringsbehov, ikke allerede dokumenteret produktionserfaring.')


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

    m.models_table("FORESLÅET DRIFTSMODEL — EL-ASSEMBLY TIL SHIPPING",
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
    m.models_table("FØRSTE 90 DAGE — MENNESKER, FLOW OG KVALITET",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SAMARBEJDE OG BESLUTNINGSANSVAR")
    for label, body in PARTNER:
        m.bullet(label, body, after=30)

    m.section("SLUTKONTROL OG NCR — LUKKET SAG ELLER VARIG LØSNING")
    m.para("Følg et konkret anlæg fra det godkendte montagegrundlag til afsluttende udgangskontrol. Kontrollér, at teststatus, dokumenter, mærkning og pakning vedrører den rigtige enhed og revision. Afklar åbne punkter med kvalitet og de relevante fagansvarlige før frigivelse efter aftalt mandat. Når en NCR lukkes, skelnes mellem korrektionen her og nu og den handling, der skal forhindre gentagelse. Efterprøv effekten på efterfølgende arbejde og kontrollér, at problemet ikke blot er flyttet til næste proces. Sikkerhed, dokumentation og acceptkriterier må ikke lempes for at nå shipping; en afvigelse kræver godkendt håndtering og sporbar beslutning.", after=80)

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
    build(os.path.join(ROOT, "Shahram_Ajloo_Fenagy_Produktionsleder.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_Fenagy_Produktionsleder.docx"))
