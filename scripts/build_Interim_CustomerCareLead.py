# -*- coding: utf-8 -*-
"""
Interim Customer Care Lead — fortrolig dansk produktionsvirksomhed.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Interim Customer Care Lead | Stabil drift, ordreoverblik og kundeløfter'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = '2. november 2026'
RECIPIENT = 'Rekrutteringsteamet · Fortrolig dansk produktionsvirksomhed'
SUBJECT = 'Ansøgning: Interim Customer Care Lead — hasteopgave'

# ------------------------------------------------------------------ side 1
INTRO = ['Højsæson, tab af erfarne kolleger og et ERP-skifte gør det afgørende at stabilisere ordreflowet, før '
 'nye rutiner og systemer ændres. Kunden skal have et realistisk leveringsløfte, produktionen skal '
 'kende den rigtige ordre, og varer må ikke frigives på et uafklaret betalingsgrundlag. Første '
 'prioritet er derfor overblik over åbne ordrer, kritiske leverancer og de beslutninger, der blokerer '
 'flowet.',
 'Den foreslåede driftsmodel står klar til at blive tilpasset fra første dag: en prioriteret '
 'ordreliste, forecast-til-ordre-afstemning, kort daglig koordinering og en tjekliste fra '
 'ordrebekræftelse til betaling. Salg ejer strategien og distributørernes forretningsplaner; Customer '
 'Care omsætter de aftalte mål til et troværdigt forecast og konkrete ordrer sammen med salg.']

BULLETS = [('Stabil drift og rettidig ordrebehandling',
  'Gennemgå ordrebogen med teamet: lovet dato, lager/produktion, betalingsstatus og næste handling. '
  'Prioritér efter kundekonsekvens og seneste beslutningsdato, og afstem leveringsmuligheder før nye '
  'løfter. En kort daglig tavle samler forsinkelser og akutte sager med ejer og frist.'),
 ('Forecasts, mål og registrerede ordrer',
  'Afstem distributørernes forecasts med salgsmål og faktisk ordreindgang pr. periode og varegruppe. '
  'Hold forecast og bindende ordre adskilt, så forventet efterspørgsel ikke tælles to gange. Afvigelser '
  'bliver til konkrete spørgsmål til kundens indkøber og salg: ændret behov, manglende ordre eller '
  'urealistisk timing?'),
 ('Produktion, lager og lange lead times',
  'Lav én synlig leveranceplan med planlægning, produktion og relevante leverandører. Mangelvarer, '
  'sæsonudsving og transporttid skal frem før lovet leveringsdato. Alternativer som dellevering eller '
  'ændret dato aftales med kunden og salg inden for det kommercielle mandat.'),
 ('Fragt, eksport og betalingsbetingelser',
  'Foreslå en dokument- og frigivelsestjekliste med godkendte roller for container- og '
  'palleforsendelser, fragtbooking, eksportdokumenter, B/L og Incoterms. Økonomi og speditør afklarer '
  'betalings- og dokumentbetingelser pr. forsendelse; frigivelse følger aftalt procedure. Praktisk '
  'søfragts- og eksporterfaring er ikke dokumenteret i mit CV og må ikke erstattes af en generisk '
  'tjekliste.'),
 ('Prislister og kundedialog',
  'Kontrollér gyldig prisliste, valuta, kundetype, aftalt rabat og leveringsbetingelser før '
  'ordrebekræftelse. Vejledende udsalgspris, forhandler- og distributørpriser skal kunne skelnes '
  'tydeligt. Behov for marketingmateriale eller nye salgskanaler sendes videre til salg; strategien '
  'overtages ikke af Customer Care.'),
 ('Team, oplæring og ERP-overgang',
  'Skab faste rutiner, sidemandsoplæring og en tydelig vej til hjælp for yngre kolleger. Afstem åbne '
  'ordrer og stamdata før overgangen fra Navision til Business Central; test centrale '
  'ordre-/leverings-/faktureringsforløb med superbrugeren. SAP-erfaring og egne Python/Claude-værktøjer '
  'er et fundament, ikke dokumenteret erfaring som Navision/Business Central-bruger.')]

SYSTEM = ('De første 48 timer bruges på kritiske ordrer, kapacitet og beslutningsmandat med COO. Første uge '
 'giver en fælles baseline på leverancer, restordrer og systemrisici. Derefter afprøves forbedringer på '
 'afgrænsede flows, mens højsæsonens drift beskyttes. Automatisering kommer efter datakontrol og klare '
 'ejere, ikke midt i en uafklaret ERP-overgang.')

MIRROR = ('Den overførbare erfaring er kundevendt teknisk drift med fuldt P&L, tilbud, materialestyring, '
 'underentreprenører og aflevering i ELOHVAC. Ventek-Air gav ledelse af 14 personer og 11 samtidige '
 'projekter; Novo Nordisk koordinering af 25 specialister på 37 CAPEX-projekter. Professionel '
 'Claude-bruger og koder med Python/Claude API-værktøjer og dokumenteret produktivitetsløft over 40 %.')

HONEST = ('CV’et dokumenterer ikke solid Customer Care-/salgskoordinationserfaring med eksportdistributører, '
 'praktisk søfragt/B/L/Incoterms eller rutineret Navision/Business Central-brug. Det er væsentlige '
 'huller i en hasteopgave. SAP, ledelse og teknisk leverancekoordination er relevante styrker, men '
 'opgaven er kun realistisk, hvis COO kan acceptere den overgang og sikre nødvendig system- og '
 'eksportfaglig støtte.')

CULTURE = ('Briefet beskriver en mindre virksomhed, hvor den erfarne kollega skal tage fat og oplære teamet. '
 'Tilgangen er derfor synlig prioritering, direkte kundesvar og korte instrukser afprøvet sammen med '
 'kollegerne — ikke en ny rapporteringsorganisation. Virksomheden er fortrolig; særlige interne værdier '
 'eller arbejdssystemer antages ikke.')

PRACTICAL = ('Bosat i Måløv; dansk på modersmålsniveau og professionelt engelsk i skrift og tale. Lokation, '
 'opstart, tilgængelighed og ordningen for ELOHVAC skal afklares før aftale. Muligheden for '
 'fastansættelse kan drøftes, men må ikke forsinke løsningen af den akutte opgave.')

CLOSING = ('Første samtale bør afklare de kritiske kompetencekrav og driften her og nu: hvilke ordrer risikerer '
 'at fejle i denne uge, hvornår skifter ERP-systemet, og hvem kan understøtte eksport og systemoplæring '
 'fra dag ét?')

# ------------------------------------------------------------------ CV
PROFILE = ('Opgaven er at sikre stabile kundeløfter og et sammenhængende flow fra forecast og ordre til '
 'produktion, fragt, levering og betaling. Den relevante baggrund er teknisk drifts- og projektledelse, '
 'kundedialog, materialestyring, leverandørkoordinering og fuldt P&L i egen virksomhed. Elautoriseret '
 'maskinmester (LV/MV/HV), B.Tech og professionel Claude-bruger/koder med Python/Claude API-værktøjer '
 'til beregning, planlægning, KS og KPI. Ledelsesbeviser omfatter 5 elektrikere og 3 lærlinge, et '
 '14-personers projektteam og koordinering af 25 specialister. SAP ERP er dokumenteret; '
 'eksportdistributørservice, søfragt/B/L/Incoterms og Navision/Business Central er ikke etableret '
 'erfaring. Dette er derfor en overgangsprofil, ikke en påstand om allerede at være erfaren '
 'eksport-Customer Care Lead.')

PRACTICE = [('Kunder og økonomi — dokumenteret praksis',
  'ELOHVAC: tilbud, beregning, materialer, underentreprenører, kvalitet og aflevering med fuldt P&L. '
  'Praktisk ansvar for kundens tekniske leverance, ikke dokumenteret ordreflow til udenlandske '
  'distributører.'),
 ('Kapacitet og leveringskoordination — dokumenteret praksis',
  'Ventek-Air: 11 samtidige projekter og 14 personer, kapacitetsplanlægning, fremdrift og tavlemøder. '
  'Novo Nordisk: koordinering af engineering, indkøb og anlæg på 37 CAPEX-projekter.'),
 ('Team og oplæring — dokumenteret praksis',
  'Ledelse af 5 elektrikere og 3 lærlinge med daglig fordeling, 1:1/MUS og struktureret oplæring. '
  'Foreslået anvendelse: korte instrukser og sidemandsoplæring for yngre Customer Care-kolleger.'),
 ('Procesdisciplin — dokumenteret praksis',
  'FAT/SAT og IQ/OQ/PQ med nul kritiske fund ved aflevering. PDCA, 5S og Standard Work i drift og '
  'vedligehold; overføres til tydelige kontroller, afvigelser og opfølgning, ikke til en påstået '
  'eksportcertificering.'),
 ('Systemer og data — bevis og læringsbehov',
  'SAP ERP til økonomi, aktiver og omkostninger. Python/Claude API-værktøjer til tilbud, planlægning og '
  'KPI gav over 40 % produktivitetsløft. Navision/Business Central og Copilot kræver afklaring og '
  'oplæring; rutineret brugerstatus påstås ikke.'),
 ('Forecast og eksport — foreslået arbejdsgang',
  'Afstem mål, forecast og ordrebog sammen med salg; valider fragt- og dokumentbetingelser med speditør '
  'og økonomi. Praktisk Incoterms/B/L-ansvar og erfaring med detailkunders ordrekrav er væsentlige '
  'kompetencehuller.')]

MODELS = [('Daglig ordretavle',
  'Ordre, lovet dato, lager/produktion, betaling, blokering, ejer og næste handling. Korte møder '
  'prioriterer kritiske leverancer frem for rapportering for rapporteringens skyld.'),
 ('Forecast-til-ordre',
  'Salgsmål, distributørforecast og registreret ordre holdes adskilt pr. periode. Afvigelser afklares '
  'med indkøber og salg; dobbeltregning undgås.'),
 ('Leverance og lead time',
  'Planlægning, produktion, leverandør og transport kobles til realistisk leveringsdato. Mangelvarer, '
  'sæsonforhold og alternativer eskaleres tidligt.'),
 ('Dokument- og betalingskontrol',
  'Godkendt prisliste og leveringsbetingelser; fragtbooking, eksportdokumenter, B/L og Incoterms '
  'valideres af fagansvarlige. Frigivelse følger den aftalte betalingsprocedure.'),
 ('ERP-kontrol',
  'Afstem åbne ordrer, beholdninger, kunde-/vare-/prisstamdata efter aftalt scope. Test forløb med '
  'superbruger; dataejer, fejlrettelse og rollback besluttes af ERP-ansvarlig.'),
 ('Team og forbedring',
  'Sidemandsoplæring, opgavefordeling og daglig hjælp. GROW/SBI til foreslået coaching; '
  'PDCA/A3/5xHvorfor på gentagne fejl. Mål kvalitet og levering sammen med sagshastighed.')]

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

PRACTICAL_CV = ('Bosat i Måløv (Ballerup Kommune). Dansk og persisk/farsi på modersmålsniveau, engelsk professionelt i '
 'skrift og tale; kørekort B. Arbejdssted, opstart, varighed og tilgængelighed skal aftales sammen med '
 'ordningen for ELOHVAC. Virksomhed og formidler er ikke identificeret i briefet. Navision/Business '
 'Central, eksport/søfragt og distributør-Customer Care er ikke dokumenteret specialistbaggrund; støtte '
 'og mandat skal afklares, før hasteopgaven kan påtages realistisk.')

REFERENCES = 'Tidligere ledere hos Novo Nordisk og Biofos (Lynetten) — oplyses efter aftale.'

PARTNER = [('COO',
  'Kort status på kritiske leverancer, kapacitet og ERP-risiko. Eskalér med konsekvens, alternativer og '
  'anbefaling. Aftal eksplicit mandat for pris, levering og frigivelse samt den faglige støtte, som en '
  'overgangsprofil kræver.'),
 ('Salg og kundernes indkøbere',
  'Salg ejer strategien og forretningsplanerne. Customer Care følger op på forecasts, konkrete ordrer '
  'og leveringer og bringer afvigelser og kommercielle behov tilbage til salg uden at ændre aftaler '
  'uden mandat.'),
 ('Produktion, planlægning, leverandører og speditør',
  'Brug samme overblik over kapacitet, lager, lange lead times og transportfrister. Afklar '
  'dokumentansvar og leveringsmuligheder før kunden får et løfte. Eksportforhold valideres med erfarne '
  'fagpersoner.'),
 ('Customer Care-team, økonomi og ERP-ansvarlig',
  'Fordel opgaver og oplæring tydeligt; sørg for stedfortræder på kritiske rutiner. Økonomi bekræfter '
  'betalingsgrundlaget, ERP-ansvarlig ejer migreringsbeslutninger, og teamet tester de faktiske '
  'ordreflows og rapporterer fejl.')]

FIRST90 = [('Første 48 timer',
  'COO afklarer mandat, bemanding og støtte fra salg, økonomi, speditør og ERP-superbruger. Gennemgå '
  'kritiske ordrer og leverancer; identificér betalings-/dokumentblokeringer. Aftal hvad der kan '
  'besluttes selvstændigt, og hvem der overtager eksportfaglige spørgsmål.'),
 ('Første uge',
  'Daglig ordretavle og prioriteret restordreliste i drift. Afstem forecast og ordreindgang med salg på '
  'de vigtigste kunder. Skab overblik over prislister og kundeaftaler. Få en konkret '
  'systemoplæringsplan og kendt ERP-tidsplan; lov ikke en selvstændig migration.'),
 ('Dag 30',
  'Standard for ordreopfølgning, kundesvar og dokumentkontrol er afprøvet. Unge kolleger trænes på '
  'faktiske sager. COO får baseline på levering til lovet dato, alder på blokeringer og '
  'fejl/genarbejde. ERP-test udføres og fejl prioriteres med ansvarlige og beslutningspunkter.'),
 ('Dag 60–90 / ved opgavens afslutning',
  'Afstem ordreforløb og dokumentation efter ERP-overgangen, hvis den ligger i perioden. Kontrollér om '
  'faste rutiner giver færre forsinkede leverancer og rettelser. Overdrag åbne risici, kontaktveje og '
  'instrukser. Varighed og kalender fastlægges med COO; planen tilpasses en kortere interimperiode.')]

KEYWORDS = ('Opgavens fokus: Customer Care · Ordrebehandling · Forecasts · Registrerede ordrer · Distributører · '
 'Detailkunder · Online-forretning · Produktion · Planlægning · Lager · Leverandører · Lead times · '
 'Containerforsendelser · Palleforsendelser · Fragtbooking · Eksportdokumenter · B/L · Incoterms · '
 'Betalingsbetingelser · Prislister · Leveringsbetingelser · Navision · Business Central · Excel · '
 'Copilot. Eksport- og systemtermer angiver opgavens krav og læringsbehov, ikke dokumenteret '
 'specialistkompetence.')


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

    m.models_table("FORESLÅET DRIFTSMODEL — ORDRE TIL BETALING",
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
    m.models_table("OPSTART OG FØRSTE 90 DAGE — TILPASSES OPGAVENS VARIGHED",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SAMARBEJDE OG BESLUTNINGSANSVAR")
    for label, body in PARTNER:
        m.bullet(label, body, after=30)

    m.section("ERP-OVERGANG UDEN AT MISTE ORDREFLOWET")
    m.para("Før et ordreflow flyttes, afprøves repræsentative scenarier i det godkendte testmiljø: almindelig ordre, ændret pris, restordre, dellevering og kunde med betalingsblokering. Sammenhold de forventede resultater med de faktiske posteringer og dokumenter, og få fagansvarlige til at godkende kontrollen. Afstem den aftalte cutover-liste, så åbne ordrer ikke forsvinder eller dubleres mellem systemerne. Der skal være en navngiven ejer for hver fejl og en aftalt vej til at fortsætte driften, hvis testen eller datakvaliteten ikke er tilstrækkelig. Beslutninger om go-live og tilbagefald ligger hos COO og ERP-ansvarlig — ikke hos en uprøvet ny bruger. Ekstra Excel-kontrol må ikke blive en uafstemt parallel ordrebog.", after=80)

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
    build(os.path.join(ROOT, "Shahram_Ajloo_Interim_CustomerCareLead.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_Interim_CustomerCareLead.docx"))
