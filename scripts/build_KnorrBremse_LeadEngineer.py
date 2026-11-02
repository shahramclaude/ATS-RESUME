# -*- coding: utf-8 -*-
"""
Knorr-Bremse Lead Engineer — kundens depot i Struer.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Lead Engineer | Knorr-Bremse | Driftsnær analyse, vedligehold og teknisk kundedialog'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = '2. november 2026'
RECIPIENT = 'Knorr-Bremse Rail Systems Denmark · Teamleader Martin Alhmann'
SUBJECT = 'Ansøgning: Lead Engineer — kundens depot i Struer'

# ------------------------------------------------------------------ side 1
INTRO = ['En teknisk fejl er først løst, når årsagen er underbygget, handlingen er gennemført, og driften '
 'viser, at problemet ikke vender tilbage. Rollen i Struer skal forbinde depotets konkrete '
 'observationer med Engineering-teamets specialistviden, så kunden får én tydelig teknisk kontakt og '
 'løsninger, der både kan dokumenteres og bruges i hverdagen.',
 'Den foreslåede arbejdsstruktur er klar til tilpasning fra første dag: et prioriteret problemregister, '
 'en RCA-skabelon og en revisionslog for manualer, scope og serviceintervaller. Hver sag får '
 'driftskonsekvens, datagrundlag, ejer, næste handling og aftalt beslutningsvej. Arbejdet sker i '
 'kundens og Knorr-Bremses godkendte systemer, ikke i et parallelt skyggeregister.']

BULLETS = [('Drive root cause analysis (RCA) tæt på udstyret',
  'Gå fejlen igennem med teknikeren, afgræns symptomer og registrér komponent, konfiguration, tidspunkt '
  'og driftsforhold. Brug A3, 5xHvorfor og Ishikawa til at afprøve forklaringer mod observationer og '
  'historik. Skeln mellem en hypotese, en sandsynlig årsag og en verificeret årsag; følg op på '
  'gentagelser efter afhjælpning.'),
 ('Holde vedligeholdelsesgrundlaget anvendeligt',
  'Sammenhold vedligeholdelsesmanualer, scope og serviceintervaller med fejlmønstre, godkendt '
  'dokumentation og praktisk udførelse. Beskriv ændringsbehov og konsekvenser sammen med '
  'dokumentspecialisterne. Intervaller eller instrukser ændres ikke alene for at reducere tidsforbrug; '
  'teknisk begrundelse og godkendelse skal følge med.'),
 ('Skabe fremdrift i ingeniøropgaver',
  'Prioritér med kunden efter sikkerhed, driftskonsekvens, gentagelse og dokumentationsbehov. Aftal '
  'ansvar, frist og nødvendige input med specialister i Aarhus og København. Korte beslutningsreferater '
  'og tydelig eskalering forbinder fjernsamarbejdet med konkrete handlinger på depotet.'),
 ('Håndtere tekniske vurderinger og ændringer disciplineret',
  'Afklar dokumentationskrav, kompetencer og beslutningsansvar for CSM-RA og 1:1-udskiftninger med '
  'erfarne jernbanespecialister. En betegnelse som 1:1 er ikke i sig selv dokumentation for uændret '
  'risiko eller automatisk godkendelse. Jernbanespecifik risikovurdering er et oplæringsbehov, ikke en '
  'allerede dokumenteret specialistkompetence.'),
 ('Omsætte driftsdata til fælles beslutninger',
  'Følg togpræstationer, gentagne fejl og tekniske tendenser på et aftalt datagrundlag. Kontrollér '
  'registreringskvalitet og relevant eksponering, før perioder eller enheder sammenlignes. På møder om '
  'drift, performance og forbedringer skal kunden kunne se problemet, næste skridt og hvad der kræver '
  'en beslutning.')]

SYSTEM = ('Første uge bruges på depotets udstyr, sikkerhedsregler, problemportefølje og kontaktveje. Dag 30 '
 'foreligger et fælles prioriteringsgrundlag og én gennemgået fejlsag; dag 60 er en aftalt RCA og '
 'dokumentationsændring afprøvet gennem de rette godkendelser. Dag 90 vurderes effekt, tilbagevendende '
 'fejl og behovet for yderligere jernbanefaglig oplæring.')

MIRROR = ('Den relevante erfaring er driftsnær fejlfinding og teknisk koordinering: Biofos med pumper, HVAC, '
 'højspændingstavler og SCADA i kritisk 24/7-drift; Novo Nordisk med 37 CAPEX-projekter, koordinering '
 'af 25 specialister og nul kritiske fund ved reguleret aflevering. ELOHVAC bidrager med kundedialog, '
 'kvalitetssikring og oplæring af teknikere og lærlinge.')

HONEST = ('B.Tech i Technology Management & Mechanical Engineering og elautoriseret maskinmester (LV/MV/HV) er '
 'det tekniske fundament. CV’et dokumenterer ikke jernbaneerfaring, CSM-RA eller ansvar for togmanualer '
 'og 1:1-udskiftninger. Overgangen skal derfor aftales med en konkret oplærings- og kompetenceplan; '
 'GMP-erfaring er ikke jernbanegodkendelse.')

CULTURE = ('Engineering-teamets grundige faglige diskussion, sparring og plads til skæve idéer passer til en '
 'arbejdsform, hvor driftens viden bliver hørt, hypoteser udfordres respektfuldt, og aftaler følges til '
 'dørs. Professionel Claude-bruger og koder: egne Python/Claude API-værktøjer til planlægning, KS og '
 'KPI har givet over 40 % produktivitetsløft i teknisk entreprisedrift; kundedata anvendes kun i '
 'godkendte miljøer.')

PRACTICAL = ('Bopæl er Måløv. Daglig onsite-tilstedeværelse i Struer kræver en konkret aftale om base/ophold, før '
 'ansættelse er realistisk; fjernsamarbejdet med Engineering erstatter ikke depotrollen. De 37 timer, '
 'cirka 20 årlige rejsedage, startdato og ELOHVAC-ordning skal afklares. Dansk og engelsk beherskes '
 'professionelt.')

CLOSING = ('Stillingen er set hos Techjob. En første samtale kan afklare de vigtigste driftsproblemer, '
 'kompetencekravene til ændringsvurderinger og en holdbar løsning for den daglige base i Struer.')

# ------------------------------------------------------------------ CV
PROFILE = ('Opgaven er at skabe sammenhæng mellem depotets fejl, teknisk analyse og holdbare tekniske løsninger hos kunden '
 'i Struer. Grundlaget er B.Tech i Technology Management & Mechanical Engineering, elautoriseret '
 'maskinmester (LV/MV/HV), praktisk el-/mekanisk fejlfinding og reguleret projektaflevering. Biofos '
 'giver erfaring med kritisk vedligehold og SCADA; Novo Nordisk med 37 projekter og koordinering af 25 '
 'specialister. Kundedialog, KS og oplæring kommer fra ELOHVAC. Professionel Claude-koder med '
 'Python/Claude API-værktøjer og over 40 % produktivitetsløft. Jernbanespecifik CSM-RA, togmanualer og '
 '1:1-udskiftninger kræver oplæring og klare godkendelsesgrænser.')

PRACTICE = [('Fejlfinding og årsagsanalyse — dokumenteret praksis',
  'Biofos: forebyggende vedligehold, akut fejlfinding, reservedelsflow og drift af pumper, HVAC, '
  'højspændingstavler og SCADA. Novo: A3, 5xHvorfor og Ishikawa i teknisk problemløsning.'),
 ('Teknisk koordinering — dokumenteret praksis',
  'Novo Nordisk: 37 samtidige CAPEX-projekter og 25 specialister på tværs af engineering, indkøb og '
  'anlæg; opfølgning på fremdrift, økonomi, risici og ressourcer samt rapportering til ledelse og '
  'bygherre.'),
 ('Kunde og dokumentation — dokumenteret praksis',
  'ELOHVAC: tilbud, tekniske installationer, KS, underentreprenører og aflevering med fuldt P&L. '
  'Ventek-Air: specifikation til formel aflevering på 11 projekter; aftalegrundlag og '
  'afleveringspakker.'),
 ('Reguleret kvalitet — dokumenteret praksis',
  'FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA med nul kritiske fund ved aflevering. Kontrolleret accept og '
  'dokumentation er overførbart; ikke dokumentation for CSM-RA eller jernbanesikkerhedsgodkendelse.'),
 ('Faglig sparring og oplæring — dokumenteret praksis',
  'Daglig planlægning, 1:1/MUS og struktureret oplæring af 5 elektrikere og 3 lærlinge. Daglige '
  'tavlemøder og flaskehalsanalyse; foreslået teach-back/GROW/SBI understøtter tydelig faglig dialog.'),
 ('Data og forbedring — bevis og anvendelse',
  'PDCA gav 40 % lavere energiomkostninger hos Novo; SAP til økonomi, aktiver og omkostninger. '
  'Python/Claude-værktøjer gav >40 % produktivitetsløft i entreprisedrift; foreslået driftsanalyse '
  'kræver sporbare kilder og faglig kontrol.')]

MODELS = [('Problemregister',
  'Udstyr/konfiguration, symptom, driftskonsekvens, datakilde, prioritet, ejer, næste handling og '
  'beslutningsbehov.'),
 ('RCA og effektkontrol',
  'A3, 5xHvorfor og Ishikawa; adskil hypotese og evidens. Verificér årsag og følg gentagelser efter '
  'handling.'),
 ('Manual- og ændringslog',
  'Godkendt revision, scope, serviceinterval, ændringsbegrundelse, berørte komponenter og '
  'review/godkendelse med dokumentspecialist.'),
 ('Fjernsamarbejde',
  'Kort prioriteringsmøde, ansvarsmatrix og beslutningslog mellem kunde og Engineering i '
  'Aarhus/København.'),
 ('Data til driftsmøde',
  'Aftal definitioner og relevant eksponering; følg togpræstationer og tekniske tendenser uden at gøre '
  'korrelation til årsag.'),
 ('Sikkerhed og læring',
  'Dokumenteret LOTO/risikovurdering og PDCA; lokal depotadgang samt CSM-RA-rolle og kompetencer '
  'afklares før selvstændige vurderinger.')]

ACHIEVEMENTS = [('37 samtidige CAPEX-projekter',
  'DKK 2–10 mio. pr. projekt; koordinering af 25 specialister og reguleret aflevering uden kritiske '
  'fund hos Novo Nordisk.'),
 ('Kritisk 24/7-vedligehold',
  'Biofos: forebyggende vedligehold og akut fejlfinding på el-/mekaniske anlæg, pumper, HVAC, HV og '
  'SCADA.'),
 ('Over 40 % produktivitetsløft',
  'Egne Python/Claude API-værktøjer til beregning, planlægning, KS og KPI i ELOHVAC.'),
 ('40 % lavere energiomkostninger',
  'PDCA-baseret forbedringsprogram hos Novo Nordisk; ikke en påstået forbedring af togpræstationer.')]

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

PRACTICAL_CV = ('Bopæl: Måløv (Ballerup Kommune). Daglig arbejdsplads hos kunden i Struer, 37 timer og cirka 20 '
 'rejsedage årligt. En holdbar aftale om base/ophold i Struer samt startdato og ordningen for ELOHVAC '
 'er nødvendig; ingen flytning eller daglig pendling er forudsat. Dansk og persisk/farsi på '
 'modersmålsniveau, engelsk professionelt i skrift og tale; kørekort B. Uddannet B.Tech og '
 'elautoriseret maskinmester (LV/MV/HV). Ingen dokumenteret jernbane-/CSM-RA-erfaring; lokal sikkerhed, '
 'togudstyr, dokumentstandarder og ændringsmandat kræver oplæring. Jobbet er set hos Techjob.')

REFERENCES = 'Tidligere ledere hos Novo Nordisk og Biofos (Lynetten) — oplyses efter aftale.'

PARTNER = [('Kundens teknikere og beslutningstagere',
  'Vær synlig på depotet, lyt til fejlhistorien og kontrollér observationer ved udstyret. Oversæt '
  'analysen til driftskonsekvens, løsning og næste beslutning; lov ikke en årsag eller effekt, før '
  'evidensen bærer det.'),
 ('Teamleader og Engineering i Aarhus/København',
  'Afstem prioritering, faglige ressourcer og eskalering. Send en afgrænset problemstilling med '
  'historik, data og konkrete spørgsmål, så fjernsparring giver handlinger frem for nye uklare '
  'undersøgelser.'),
 ('Dokument- og jernbanesikkerhedsspecialister',
  'Afklar revisionsstyring, ændringsvurdering, CSM-RA og dokumentation for 1:1-udskiftninger med de '
  'kompetente ansvarlige. Lead Engineer koordinerer; godkendelses- og sikkerhedsansvar følger '
  'organisationens mandat.'),
 ('Drift og vedligehold',
  'Aftal praktisk afprøvning og acceptkriterier under depotets sikkerhedsregler. Kontrollér, at '
  'løsningen kan udføres og forstås af dem, der skal bruge den; følg effekt og uafklarede fejl efter '
  'implementering.')]

FIRST90 = [('Første uge',
  'Martin Alhmann og kunden afklarer mandat, sikkerheds-/adgangsregler, udstyr og aktuelle fejl. Mød '
  'teknikere og Engineering-/dokumentspecialister; aftal kontaktveje og prioritering. Leverance: fælles '
  'problemregister, kompetenceplan og afklaret rolle ved tekniske ændringer.'),
 ('Dag 30',
  'Gennemgå én tilbagevendende fejl fra observation til historik og mulige årsager. Afstem '
  'manualrevision, scope og serviceintervaller med godkendt grundlag. Aftal definitioner for driftsdata '
  'og relevant eksponering. Leverance: prioriteret backlog og en evidensbaseret RCA-plan med navngivne '
  'faglige reviewere.'),
 ('Dag 60',
  'Færdiggør en aftalt RCA og efterprøv afhjælpning gennem godkendt metode. Gennemfør review af et '
  'konkret dokumentations-/ændringsbehov med jernbanespecialister, herunder CSM-RA-afklaring hvor '
  'relevant. Leverance: godkendte handlinger, opdateret dokumentationsstatus og sporbar opfølgning hos '
  'kunden.'),
 ('Dag 90',
  'Vurdér gentagelsesfejl, åbne handlinger, dokumentationskvalitet og kundens oplevelse af teknisk '
  'fremdrift. Del læring med Aarhus/København; justér møder, prioritering og instrukser gennem godkendt '
  'proces. Aftal næste opgaver og resterende kompetenceløft før udvidet selvstændigt ansvar.')]

KEYWORDS = ('Opgavens fokus: Lead Engineer · root cause analysis (RCA) · vedligeholdelsesmanualer · scope · '
 'serviceintervaller · ingeniøropgaver · tekniske vurderinger · CSM-RA · 1:1-udskiftninger · '
 'togpræstationer · driftsdata · tekniske tendenser · kundens depot · produktion · fjernsamarbejde. '
 'Jernbanetermer beskriver stillingens opgaver og oplæringsbehov, ikke allerede dokumenteret '
 'branchekompetence.')


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

    m.models_table("FORESLÅET ARBEJDSMODEL — FEJL TIL HOLDBAR LØSNING",
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
    m.models_table("FØRSTE 90 DAGE — DEPOT, ANALYSE OG DOKUMENTERET EFFEKT",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SAMARBEJDE OG BESLUTNINGSANSVAR")
    for label, body in PARTNER:
        m.bullet(label, body, after=30)

    m.section("TEKNISK ÆNDRING — DOKUMENTATION FØR IMPLEMENTERING")
    m.para("Før en teknisk ændring eller 1:1-udskiftning gennemføres, skal den berørte komponent, konfiguration og funktion være entydigt beskrevet. Afklar ændringens betydning og den nødvendige risikovurdering med de kompetente jernbanespecialister; betegnelsen 1:1 må ikke blive en genvej uden om dokumentationskrav. Kontrollér godkendt reservedelsgrundlag, instrukser, test/accept og ansvar for frigivelse. Opdatér relevante manualer og registrér implementeringen i de godkendte systemer. Følg efterfølgende driftsdata for gentagelser og utilsigtede virkninger. En lukket sag er ikke automatisk en varig løsning; effektkontrollen skal kobles tilbage til RCA’en og til den tekniker, der møder udstyret i praksis.", after=80)

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
    build(os.path.join(ROOT, "Shahram_Ajloo_KnorrBremse_LeadEngineer.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_KnorrBremse_LeadEngineer.docx"))
