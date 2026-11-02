# -*- coding: utf-8 -*-
"""
Newsec Danmark — Teamleder til Technical Management Services, Teknisk ejendomsdrift, job 8648966.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Teamleder | Teknisk ejendomsdrift | Technical Management Services'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = '2. november 2026'
RECIPIENT = 'Newsec Danmark · Att. HR Koordinator Marie Nissen · Kongens Lyngby'
SUBJECT = 'Ansøgning: Teamleder til teknisk ejendomsdrift — job 8648966'

# ------------------------------------------------------------------ side 1
INTRO = ['En stor kundes ejendomsportefølje skal fungere hver dag, samtidig med at vedligehold, service og '
 'udvikling bliver styret på tværs af ejendommene. Opgaven er at give driftschefer og driftsledere '
 'tydelige rammer og reel handlefrihed, så kunden oplever ensartet kvalitet, rettidig opfølgning og '
 'færre overraskelser — også når akutte sager presser planen.',
 'Den foreslåede driftsmodel står klar til at blive tilpasset Newsecs systemer: ét porteføljeoverblik, '
 'en fælles prioriteringsnøgle, en fast ledelsesrytme og et KPI-kort med ansvar og datakilde. '
 'Teamlederen skal både udvikle lederne og kunne tage egen mindre portefølje i en periode; kapaciteten '
 'til de to opgaver skal derfor aftales eksplicit.']

BULLETS = [('Ledelse og motivation — trivsel, performance og kvalitet',
  'Individuelle forventningsaftaler, faste 1:1 og MUS/GRUS kobles til kompetencematrix og konkrete '
  'udviklingsmål. Situationsbestemt ledelse tilpasses erfaring og opgave; GROW bruges til sparring og '
  'SBI til præcis feedback. Ugentlige møder slutter med beslutning, ejer og frist, ikke blot '
  'orientering.'),
 ('Proaktiv teknisk drift — effektiv drift på tværs',
  'Anlæg og vedligeholdsbehov vurderes efter sikkerhed, myndighedskrav, driftskritikalitet og '
  'konsekvens for kunden. En rullende plan samler lovbundne eftersyn, forebyggende vedligehold og åbne '
  'afvigelser. Akutte opgaver får en tydelig eskalationsvej, så planlagt vedligehold ikke forsvinder i '
  'indbakken.'),
 ('Nøgletal, resultater og KPI’er',
  'Med nærmeste leder aftales få mål med definition, datakilde og baseline: rettidige eftersyn, alder '
  'på åbne sager, gentagne fejl, budgetafvigelser og kundens tilbagemeldinger. PDCA og A3 omsætter '
  'afvigelser til forbedringer. Tal skal udløse en beslutning, ikke en ekstra rapport.'),
 ('Kunden, leverandører og samarbejdspartnere',
  'En fælles sags- og beslutningslog forbinder kundens prioriteringer med leverandørernes opgaver. '
  'Bestilling, acceptkriterium, servicerapport og økonomisk opfølgning kobles sammen. Et fast kundemøde '
  'afklarer behov, ændringer og næste beslutning; væsentlige risici meldes tidligt.'),
 ('Egen lille portefølje i en periode',
  'Den praktiske del løses med samme standard som teamets: ejendomskort, kontaktveje, planlagte '
  'eftersyn og opfølgningsliste. Der aftales tidsramme og stedfortræder, så teamets sparring og '
  'ledelsesopgaver ikke bliver resttid. Erfaringerne bruges til at forbedre arbejdsgange sammen med '
  'teamet.'),
 ('Tal, IT-systemer og bæredygtig udvikling',
  'SAP-erfaring og egne Python/Claude API-værktøjer giver en konkret digital værktøjskasse. Data '
  'kontrolleres før automatisering, og AI anvendes kun inden for godkendte fortrolighedsregler. Energi '
  'og vedligehold vurderes sammen med funktion, levetid og driftsrisiko; dokumenterede effekter skelnes '
  'fra estimater.')]

SYSTEM = ('Første uge giver et fælles billede af kundens aftale, teamets mandat og de mest kritiske ejendomme. '
 'Dag 30 har hver prioriteret sag en ejer og et næste skridt. Dag 60 er én forbedret arbejdsgang '
 'afprøvet; dag 90 vurderes effekten med kunden og nærmeste leder. Værktøjerne skal understøtte '
 'eksisterende systemer og faglighed — ikke skabe en parallel administration.')

MIRROR = ('Beviserne er praktiske: ELOHVAC med fuldt P&L og ledelse af 5 elektrikere og 3 lærlinge; Ventek-Air '
 'med 14 personer og 11 samtidige projekter; Novo Nordisk med koordinering af 25 specialister på 37 '
 'CAPEX-projekter. Biofos giver erfaring med kritisk teknisk drift og vedligehold. Professionel '
 'Claude-bruger og koder med Python/Claude API-værktøjer og dokumenteret produktivitetsløft over 40 %.')

HONEST = ('Der er ikke dokumenteret erfaring med UNIK4, kommerciel ejendomsforvaltning eller direkte '
 'personaleledelse af driftschefer og driftsledere. Broen er teknisk drifts- og personaleledelse, '
 'sidemandsoplæring i Newsecs systemer og klare mandater aftalt med nærmeste leder — ikke en påstand om '
 'allerede at have haft samme rolle.')

CULTURE = ('Newsecs fokus på fleksibilitet, balance og en inkluderende kultur skal kunne mærkes i planlægningen: '
 'realistisk kapacitet, tydelige forventninger og plads til faglig uenighed. Trivsel og kvalitet hænger '
 'sammen, når medarbejderne kan melde risiko og behov for hjælp i tide.')

PRACTICAL = ('Bosat i Måløv (Ballerup Kommune), med praktisk adgang til Kongens Lyngby og ejendomme i området. '
 'Kørekort B; dansk på modersmålsniveau og professionelt engelsk. Tiltrædelse og rammerne for den '
 'eksisterende virksomhed aftales før ansættelse.')

CLOSING = ('En første samtale må gerne tage udgangspunkt i en konkret ejendom: hvor tabes der tid eller kvalitet '
 'i dag, og hvad skal teamet kunne løse selvstændigt efter de første 90 dage?')

# ------------------------------------------------------------------ CV
PROFILE = ('Newsecs teamlederopgave er at skabe stabil teknisk ejendomsdrift for én stor kunde gennem et '
 'velfungerende team af driftschefer og driftsledere. Den relevante baggrund er elautoriseret '
 'maskinmester (LV/MV/HV), B.Tech og praktisk erfaring med teknisk drift, vedligehold, personaleledelse '
 'og fuldt P&L. Beviserne omfatter ledelse af 5 elektrikere og 3 lærlinge, et 14-personers projektteam '
 'og tværfaglig koordinering af 25 specialister. Der arbejdes med daglige tavlemøder, 1:1/MUS, '
 'prioritering, 5S og PDCA. Professionel Claude-bruger og koder med Python/Claude API-værktøjer til '
 'beregning, planlægning, kvalitet og KPI. Overgangen til ejendomsforvaltning og ledelse af '
 'driftsledere kræver introduktion til kundeaftale, systemer og mandat.')

PRACTICE = [('Personaleledelse — dokumenteret praksis',
  'ELOHVAC: 5 elektrikere og 3 lærlinge med daglig fordeling, 1:1, MUS, oplæring og '
  'arbejdsmiljøopfølgning. Ventek-Air: daglig ledelse af 14 personer, kapacitetsstyring og tavlemøder.'),
 ('Daglig drift og vedligehold — dokumenteret praksis',
  'Biofos: pumper, HVAC, højspændingstavler og SCADA i kritisk drift. Forebyggende vedligehold, akut '
  'fejlfinding, reservedelsflow, 5S, Standard Work og PDCA.'),
 ('Økonomi og leverance — dokumenteret praksis',
  'ELOHVAC: tilbud, materialer, underentreprenører, kvalitet og aflevering med fuldt P&L. Novo Nordisk: '
  'fremdrift, budget, risici og ressourcer i CAPEX-portefølje samt SAP ERP til økonomi og aktiver.'),
 ('Lede driftschefer og driftsledere — foreslået tilgang',
  'Aftal beslutningsrum, opfølgning og eskalation pr. leder. GROW/SBI og situationsbestemt ledelse '
  'støtter selvstændighed; direkte erfaring med personaleledelse af ledere er ikke dokumenteret.'),
 ('Kunde og leverandører — overførbar erfaring',
  'Kundevendte tekniske opgaver, tilbud, leverandørkoordinering og dokumentation. Anvend en fælles '
  'sagslog og målbare acceptkriterier på den nye ejendomsportefølje.'),
 ('IT og forbedringer — dokumenteret praksis',
  'Python/Claude API til tilbud, tidsplaner, KS og KPI med produktivitetsløft over 40 %. UNIK4 er et '
  'oplæringspunkt; eksisterende data og adgangsregler skal forstås før nye automatiseringer.')]

MODELS = [('Porteføljeoverblik',
  'Ejendomskort med kritiske anlæg, ansvar, aftalte ydelser, eftersyn, åbne risici og næste beslutning. '
  'Afstemmes med kunden og teamets eksisterende systemer.'),
 ('Prioritering og vedligehold',
  'Sikkerhed/myndighedskrav → driftskritikalitet → kundekonsekvens. Rullende vedligeholdsplan og synlig '
  'liste over udskudte opgaver med begrundelse og ejer.'),
 ('Ledelsesrytme',
  '1:1, MUS/GRUS og ugentligt driftsmøde; kompetencematrix, situationsbestemt ledelse, GROW og SBI. '
  'Mandat og eskalationsgrænse aftales pr. leder.'),
 ('KPI-kort og PDCA',
  'Definition, datakilde, måleejer og baseline. Månedlig gennemgang med nærmeste leder; A3/5xHvorfor på '
  'gentagne afvigelser og tydelig effektkontrol.'),
 ('Kunde og leverandører',
  'Kundemøde med beslutningslog; opgavebestilling med acceptkriterier, servicerapport og opfølgning. '
  'RACI tydeliggør grænseflader og ansvar.'),
 ('Egen portefølje og kapacitet',
  'Samme standarder som teamet; aftalt tidsandel, stedfortræder og grænse for egen sagsmængde. '
  'Ledelsestid beskyttes og kapaciteten vurderes løbende.')]

ACHIEVEMENTS = [('Over 40 % produktivitetsløft',
  'Egne Python/Claude API-værktøjer til tilbud, planlægning, KS og KPI-rapportering i ELOHVAC.'),
 ('37 samtidige CAPEX-projekter',
  'DKK 2–10 mio. pr. projekt; koordinering af 25 specialister og aflevering uden kritiske fund under '
  'GMP/FDA/EMA.'),
 ('11 samtidige projekter og 14 personer',
  'Ventek-Air: specifikation til formel aflevering, kapacitetsstyring, daglige tavlemøder og '
  'flaskehalsanalyse.'),
 ('40 % reduktion i energiomkostninger',
  'PDCA-baseret forbedringsprogram hos Novo Nordisk; SAP til økonomi-, aktiv- og '
  'omkostningsopfølgning.')]

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

PRACTICAL_CV = ('Bosat i Måløv (Ballerup Kommune); Kongens Lyngby er en praktisk arbejdsbase. Kørekort B. Dansk og '
 'persisk/farsi på modersmålsniveau, engelsk professionelt. Klar til at drøfte en egen mindre '
 'portefølje som del af rollen, med tydelig kapacitets- og ansvarsfordeling. Tiltrædelse og rammerne '
 'for ELOHVAC aftales før ansættelse. UNIK4 er ikke dokumenteret erfaring; oplæring planlægges sammen '
 'med superbruger og nærmeste leder.')

REFERENCES = 'Tidligere ledere hos Novo Nordisk og Biofos (Lynetten) — oplyses efter aftale.'

PARTNER = [('Driftschefer og driftsledere',
  'Tydelige mandater og forventninger, støtte ved vanskelige sager og faglig sparring uden '
  'detailstyring. Kapacitet og trivsel følges i 1:1; problemer kan løftes tidligt og uden at blive '
  'gjort personlige.'),
 ('Kunden',
  'Fast dialog om prioriteringer, kvalitet og bæredygtig udvikling. Oplæg skelner mellem kendte '
  'forhold, forudsætninger og forslag. Beslutninger og ændringer dokumenteres, så team og kunde har '
  'samme billede af leverancen.'),
 ('Nærmeste leder og interne kolleger',
  'KPI-opfølgning med definition og datakilde; afvigelser ledsages af årsag, handling og behov for '
  'beslutning. Snitflader til administration og økonomi afklares, før opgaver falder mellem to stole.'),
 ('Leverandører og samarbejdspartnere',
  'Klar bestilling, adgang, sikkerhed, acceptkriterier og servicerapport. Uafsluttede fejl får '
  'ansvarlig og frist. Gentagne mangler gennemgås systematisk med leverandøren frem for at udløse endnu '
  'et udkald.')]

FIRST90 = [('Uge 1',
  'Nærmeste leder og teamet afklarer kundeaftale, mandat, bemanding og egen portefølje. Besøg '
  'prioriterede ejendomme sammen med driftslederne. Leverance: fælles risikobillede og '
  'introduktionsplan til Newsecs IT-systemer, herunder eventuel UNIK4.'),
 ('Dag 30',
  'Ejendomskort og kritiske eftersyn samlet i eksisterende system. Individuelle forventningsaftaler og '
  '1:1-kadence på plads. Nærmeste leder godkender KPI-definitioner og baseline; kunden bekræfter '
  'vigtigste behov og kontaktveje.'),
 ('Dag 60',
  'Teamet afprøver én forbedret arbejdsgang, fx fra bestilling til lukket servicesag. Registrér '
  'ventetid, manglende dokumentation og gentagne fejl før/efter. Etabler leverandøropfølgning og afstem '
  'egen porteføljes tidsforbrug med ledelsesopgaven.'),
 ('Dag 90',
  'Fælles review med kunden og nærmeste leder: rettidige eftersyn, åbne sager, kvalitet, økonomiske '
  'afvigelser og kundens tilbagemeldinger. Teamet vurderer trivsel og kompetencebehov. Beslut hvilke '
  'forbedringer der skaleres, med ejer, mål og næste kontrol.')]

KEYWORDS = ('Rollens fokus: Teamleder · Technical Management Services · TMS · Driftschefer · Driftsledere · '
 'Teknisk ejendomsdrift · Vedligehold · Ejendomsporteføljer · Kundetilfredshed · Trivsel · Performance '
 '· Kvalitet · Nøgletal · KPI’er · Arbejdsgange og processer · Leverandører · Samarbejdspartnere · '
 'Driftsudvikling · Facility management · IT-systemer. UNIK4 er et oplæringspunkt, ikke en påstået '
 'kompetence.')


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
    m.resume_header(NAME, TITLE, CONTACT, "LEDELSESPROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("DRIFTSMODEL — FORESLÅET ANVENDELSE HOS NEWSEC",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER AFDELINGEN I DRIFT",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN LEDES AFDELINGEN — DE FIRE PARTER")
    for label, body in PARTNER:
        m.bullet(label, body, after=30)

    m.section("FÆLLES KONTROL AF DRIFTSMODELLEN")
    m.para("På en pilot-ejendom gennemgås en konkret servicesag fra kundens henvendelse til dokumenteret afslutning: hvem bestiller, hvem godkender, hvornår orienteres kunden, og hvor gemmes servicerapporten? Teamet peger på dobbeltregistrering og ventetid, før arbejdsgangen ændres. Effekten vurderes på genåbnede sager, gennemløbstid og kvaliteten af dokumentationen — ikke alene på antal lukkede opgaver. Samtidig kontrolleres, at lovbundne eftersyn fortsat gennemføres rettidigt. Først når ansvar, datakilder og afvigelser er afklaret, aftales udbredelse til flere ejendomme. Kundens oplevelse og teamets belastning indgår i vurderingen; en hurtigere proces er ikke en forbedring, hvis den flytter fejl eller overarbejde til andre.", after=80)

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
    build(os.path.join(ROOT, "Shahram_Ajloo_Newsec_TeamlederTekniskEjendomsdrift.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_Newsec_TeamlederTekniskEjendomsdrift.docx"))
