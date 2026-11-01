# -*- coding: utf-8 -*-
"""FLD Energi: driftschef. Dansk samlet ansøgning og CV i masterdesign."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Driftschef — FLD Energi | Montørteam, serviceleverancer og datadrevet drift'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = 'FLD Energi · Att. VVS-direktør Jonas Larsen'
SUBJECT = 'Ansøgning: Driftschef til FLD Energi'

# ------------------------------------------------------------------ side 1
INTRO = ['Vækst i rammeaftaler bliver først til en sund forretning, når den første serviceleverance er '
 'planlagt, montøren er klædt på, og kunden kan se, at aftalen virker. FLD Energis opgave er '
 'derfor at bygge kapacitet og leverancesikkerhed samtidigt: flere montører uden flere fejl, '
 'kortere tid fra aftale til første leverance og data, der hjælper med at prioritere arbejdet på '
 'varmecentralerne.',
 'Arbejdsmodellen er klar fra første dag: et overdragelseskort fra forretningsudvikling til drift, '
 'en fælles kapacitets- og serviceplan, en kompetencematrix med struktureret oplæring samt en '
 'enkel driftsrapport. Den nye dataplatform afprøves på konkrete kundesager, hvor alarmer skal '
 'blive til relevante handlinger og dokumentation — ikke blot flere beskeder.']

BULLETS = [('Kravet: gøre nye koncepter og rammeaftaler til leverancer',
  'Løsningen er et overdragelseskort pr. aftale: kundens anlæg, omfang, servicekrav, '
  'kontaktperson, dokumentation, bemanding og dato for første besøg. Forretningsudvikleren og '
  'driften gennemgår forudsætningerne sammen, før aftalen sættes i produktion. Manglende '
  'anlægsdata og kapacitet skal frem, mens de stadig kan håndteres.'),
 ('Kravet: lede funktionærer og montører i hverdagen',
  'Løsningen er korte tavlemøder med sikkerhed, dagens opgaver, materialer og blokeringer; klare '
  'beslutningsrum og opfølgning på aftaler. SLII bruges til at tilpasse støtte til erfaring, GROW '
  'i udviklingssamtaler og SBI til konkret feedback. Ledelse af 5 elektrikere og 3 lærlinge samt '
  'et 14-personers installationsteam er det praktiske fundament.'),
 ('Kravet: planlægge servicebesøg, vedligehold og projektopgaver',
  'Løsningen er én kapacitetsplan med aftalte besøg, planlagt vedligehold, projektarbejde og en '
  'synlig buffer til kritiske fejl. Opgaver klargøres med kompetencer, reservedele, adgang og '
  'varighed. En ugentlig planrunde og daglig omprioritering skaber færre forgæves ture og gør '
  'konsekvensen af hasteopgaver tydelig.'),
 ('Kravet: rekruttere, oplære og udvikle nye montører',
  'Løsningen er en kompetencematrix koblet til ordrebogen: hvilke opgaver skal dækkes, hvem kan '
  'oplære, og hvornår kan en ny kollega arbejde selvstændigt? En 30-60-90-dages oplæringsplan med '
  'makker, praksisprøver og kvalitetstjek gør vækst kontrolleret. FLD Skolen kobles til konkrete '
  'faglige og personlige udviklingsbehov.'),
 ('Kravet: koordinere tilbud på mindre opgaver',
  'Løsningen er en kort tilbudsskabelon med registreret behov, afgrænsning, timer, materialer, '
  'underleverancer og forudsætninger. Omfang og økonomi godkendes, før opgaven disponeres. Fuldt '
  'P&L-ansvar, tilbudsberegning og underentreprenørstyring i egen virksomhed giver forståelse for, '
  'hvad uklare aftaler koster i driften.'),
 ('Kravet: bruge energibesparelser og alarmer til prioritering',
  'Løsningen er et anlægskort med målepunkt, baseline, datakvalitet og driftskontekst. Alarmer '
  'sorteres efter konsekvens og verificeres, før de udløser arbejde. Energibesparelser '
  'dokumenteres med tydelige forudsætninger og relevante korrektioner; en ændring i vejr eller '
  'brug må ikke præsenteres som en teknisk besparelse.'),
 ('Kravet: teste den nye dataplatform',
  'Løsningen er en afgrænset pilot med aftalte testcases: dataindlæsning, alarmkvalitet, '
  'prioritering, oprettelse af opgave og rapport til kunden. Montørerne vurderer, om informationen '
  'kan bruges på anlægget. Fund får ejer og frist, og driftens accept gives først, når en '
  'sammenhængende arbejdsgang fungerer.'),
 ('Kravet: rapportere drift og kvalitet til Jonas Larsen',
  'Løsningen er en ugentlig driftsoversigt med kapacitet, tid fra aftale til første leverance, '
  'gennemførte besøg, genbesøg, åbne kvalitetsafvigelser og kundeaftaler i risiko. En månedlig '
  'gennemgang kobler tallene til bemanding, økonomi og forbedringer. Baseline og mål aftales '
  'først; der loves ikke effekter uden data.')]

SYSTEM = ('Systemet skal gøre det enkelt at levere korrekt: én aftaleoverdragelse, én plan og én '
 'forbedringstavle med PDCA/A3. Som professionel Claude-bruger og koder bygger jeg '
 'Python-værktøjer, tjeklister og KPI-dashboards til tilbud og planlægning. FLDs data- og '
 'IT-regler styrer brugen; kundedata deles ikke eksternt uden godkendelse, og tekniske vurderinger '
 'kvalitetssikres af den ansvarlige fagperson.')

MIRROR = ('Relevant fundament: elautoriseret maskinmester (LV/MV/HV), B.Tech i teknologiledelse og '
 'maskinteknik, køleteknik og klimaanlæg samt drift af pumper, HVAC, styring og kritiske '
 'installationer. Erfaring med 11 samtidige installationsprojekter, 14-personers team, egen '
 'virksomhed med fuldt P&L og 37 CAPEX-projekter forbinder teknik, mennesker og leveranceansvar.')

HONEST = ('Afgrænsning: baggrunden er maskinmester, el, ventilation og kritisk drift — ikke en '
 'VVS-uddannelse eller dokumenteret flerårigt specialansvar for varmecentraler og '
 'rørinstallationer. Selvstændig IoT/CTS-programmering og erfaring med FLDs dataplatform påstås '
 'heller ikke. Den varme- og VVS-specifikke kompetencedækning skal afklares med Jonas og sikres '
 'gennem fagkolleger og oplæring.')

CULTURE = ('Jonas beskriver frihed, tillid og læring frem for skyld. Det omsættes til klare rammer, plads '
 'til montørens faglige valg og en fast læringsrunde efter fejl: hvad skete, hvad manglede, og '
 'hvilken standard ændres? FLDs flade organisation og tværfaglighed mellem el, VVS, CTS og energi '
 'gør tidlig sparring mere værdifuld end flere godkendelsesled.')

PRACTICAL = ('Bosat i Måløv, kørekort B. Opgaver på Sjælland passer til det geografiske arbejdsområde; fast '
 'base og tiltrædelse aftales. Dansk på modersmålsniveau og professionelt engelsk. Rammerne for '
 'den eksisterende virksomhed afklares før ansættelse.')

CLOSING = ('En første samtale kan tage udgangspunkt i den næste rammeaftale: Hvad skal være på plads, før '
 'montøren kører ud, og hvordan gør vi den næste opstart hurtigere uden at miste kvalitet?')

# ------------------------------------------------------------------ CV
PROFILE = ('FLD Energi skal omsætte stigende salg til en stabil hverdag for kunder, funktionærer og '
 'montører. Relevant erfaring er opbygning og drift af egen teknisk virksomhed med 5 elektrikere '
 'og 3 lærlinge, fuldt P&L og tilbuds-/entrepriseansvar samt ledelse af et 14-personers team på 11 '
 'samtidige installationsprojekter. Elautoriseret maskinmester (LV/MV/HV), B.Tech i '
 'teknologiledelse og maskinteknik, med praktisk el-, ventilations- og driftserfaring. '
 'Ledelsesgreb er situationsbestemt støtte, klare aftaler, struktureret oplæring, tavlemøder og '
 'forbedringer med PDCA/A3. Professionel Claude-bruger og koder med Python/Claude API-værktøjer '
 'til tilbud, planlægning og kvalitet. VVS-/varmecentralspecialisering afgrænses åbent; styrken er '
 'sammenhæng mellem kapacitet, mennesker, teknik og leverance.')

PRACTICE = [('Daglig ledelse og kapacitet',
  'Evidens: 5 elektrikere og 3 lærlinge i ELOHVAC samt 14-personers team i Ventek-Air. Daglig '
  'planlægning, 1:1, MUS og struktureret oplæring. Anvendelse: tavlemøder, kompetencefordeling og '
  'opfølgning på aftaler.'),
 ('Service og planlagt vedligehold',
  'Evidens: forebyggende vedligehold og fejlfinding på el-, ventilations- og klimaanlæg samt '
  'kritisk drift hos Biofos. Anvendelse: klargjorte serviceordrer, reservedelsbehov og aftalt '
  'buffer til kritiske fejl.'),
 ('Vækst og montørudvikling',
  'Anvendelse: kompetencematrix mod ordrebog, kapacitetsprognose og 30-60-90-dages oplæring med '
  'makker og praksisprøver. Rekruttering styres af leverancebehov og tilgængelig '
  'oplæringskapacitet.'),
 ('Kunder, tilbud og økonomi',
  'Evidens: fuldt P&L, tilbud og beregning, underentreprenører, KS og aflevering. Anvendelse: '
  'aftaleoverdragelse, opgaveafgrænsning og opfølgning på tilbud versus faktisk tids- og '
  'materialeforbrug.'),
 ('Energi og dataplatform',
  'Evidens: 40 % lavere energiomkostninger via PDCA samt SAP-opfølgning. Anvendelse: kontrolleret '
  'baseline, alarmprioritering og testcases med montørfeedback. CTS/IoT-specialistkompetence '
  'afklares, ikke antages.'),
 ('Læring og kvalitet',
  'Evidens: GMP-afleveringer uden kritiske fund samt LOTO, APV og risikovurdering i egen '
  'virksomhed. Anvendelse: fejl uden skyldplacering, men med ansvar, korrigerende handling og '
  'verificeret effekt.')]

MODELS = [('Aftale til første besøg',
  'Overdragelseskort med anlæg, omfang, kundekontakt, servicekrav, kompetencer, data og første '
  'leverancedato. Tid måles fra aftalt startpunkt til gennemført første leverance.'),
 ('Kapacitet og bemanding',
  'Ordrebog, aftalte besøg og projektopgaver mod kompetencer og tilgængelige timer; synlig buffer '
  'og klar eskalering ved kapacitetskonflikt.'),
 ('Oplæring og ledelse',
  'Kompetencematrix, makkerordning, 30-60-90-dages plan, 1:1 og MUS; SLII, GROW og SBI som '
  'konkrete greb til støtte, udvikling og feedback.'),
 ('Data og energi',
  'Anlægskort med baseline og datakvalitet, alarmklassificering og dokumenterede handlinger. '
  'Besparelser vurderes mod sammenligneligt grundlag, ikke blot før/efter-tal.'),
 ('Platformpilot',
  'Testcases fra målepunkt til alarm, opgave og kunderapport; acceptkriterier, montørfeedback, '
  'fejllog og godkendelse før udbredelse.'),
 ('Drift og forbedring',
  'Ugentlig driftsoversigt, månedlig økonomi-/kvalitetsgennemgang, genbesøg og afvigelser med ejer '
  'og dato; PDCA/A3 til varige forbedringer.')]

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
  [('Entreprise og kundeansvar',
    'Tilbud og beregning, planlægning, materialestyring, underentreprenører, kvalitetssikring og '
    'afleveringsdokumentation.'),
   ('Installationer og team',
    'El-, ventilations- og klimaanlæg: installation, tavler, styring, fejlfinding og forebyggende '
    'vedligehold. Daglig planlægning, 1:1, MUS og struktureret oplæring.'),
   ('Sikkerhed og digitalisering',
    'LOTO, APV og risikovurdering ved pladsopstart; egne Python/Claude API-værktøjer til tilbud, '
    'planlægning og kvalitetssikring.')]),
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

CERTS = [
    ("Elautoriseret maskinmester (LV/MV/HV)",
     "Sikkerhedsstyrelsen · maj 2023"),
    ("Arbejdsmiljø §16 og sikkerhedsbevidsthed (VI/6-1)",
     "Søfartsstyrelsen · maj 2021"),
    ("Køleteknik & klimaanlæg (AMU)",
     "Mercantec · mar. 2021"),
    ("Lean — værdistrømsanalyse, standardarbejde, 5S, A3 og Kaizen",
     "Anvendt i drift, service og projekter · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og projekter · 2017 – nu"),
]

LANGUAGES = ("Dansk (modersmål, skrift og tale) · Engelsk (professionelt, skrift og tale) · "
             "Persisk/farsi · Kørekort B (kategori B)")

PRACTICAL_CV = ('Bopæl Måløv (Ballerup Kommune), kørekort B. Arbejdsområde Sjælland; fast base og rejsemønster '
 'aftales. Dansk på modersmålsniveau og professionelt engelsk. Tiltrædelse og rammerne for ELOHVAC '
 'aftales før ansættelse.')

REFERENCES = 'Tidligere ledere hos Novo Nordisk A/S og Biofos (Lynetten) — oplyses ved henvendelse.'

PARTNER = [('Jonas Larsen, VVS-direktør',
  'Drift, kvalitet, bemanding og risici på én side. Beslutningsbehov og muligheder for vækst gøres '
  'konkrete med kapacitet, konsekvens og næste handling.'),
 ('Forretningsudvikleren',
  'Koncepter og rammeaftaler gennemgås for leverbarhed før opstart. Nye kundebehov og erfaringer '
  'fra driften føres tilbage til konceptet, ikke blot til næste hasteopgave.'),
 ('Funktionærer og montører',
  'Klare rammer og tillid til faglige valg. Materialer, adgang og information skal være klar; fejl '
  'undersøges med dem, der udførte opgaven, og bruges til læring.'),
 ('Kunder og platformansvarlige',
  'Prioritering og dokumentation skal kunne forklares. Test af data og alarmer kobles til en '
  'konkret kundeværdi, og fejl i datagrundlaget synliggøres før konklusioner.')]

FIRST90 = [('Dage 1–30',
  'Lær kunder, anlæg, aftaler, medarbejdere og FLDs arbejdsgange at kende. Følg montørerne på '
  'opgaver og afklar varme/VVS-kompetencedækning. Etablér baseline for kapacitet, kvalitet og tid '
  'til første leverance. Gennemgå dataplatformens modenhed med de ansvarlige.'),
 ('Dage 31–60',
  'Afprøv overdragelseskort på en ny aftale og saml service-/kapacitetsplanen. Aftal '
  'rekrutteringsbehov og oplæringsforløb med Jonas; brug FLD Skolen målrettet. Vælg et afgrænset '
  'anlægsudsnit og aftal platformens testcases og acceptkriterier.'),
 ('Dage 61–90',
  'Gennemfør første pilot fra data og alarm til kundedokumenteret handling. Evaluer '
  'planopfyldelse, genbesøg og førsteleverancetid. Justér standarderne med montørerne, luk '
  'kritiske testfund og fremlæg næste væksttrin med bemandings- og økonomikonsekvens.'),
 ('Måned 3–6',
  'Udvid team og aftalevolumen i takt med dokumenteret kapacitet og kvalitet. Gentag '
  'oplæringsforløb, udbred afprøvede platformarbejdsgange efter godkendelse og følg kundernes '
  'oplevelse af leverancen.'),
 ('Første år',
  'Et større team med tydelige kompetencer, en mere forudsigelig aftaleopstart og brugbare '
  'driftsdata. Konkrete mål for vækst og gennemløbstid aftales med Jonas ud fra baseline; kvalitet '
  'og arbejdsmiljø er faste forudsætninger.')]

KEYWORDS = ('Driftschef · FLD Energi · Varmecentraler · Rørinstallationer · Service · Planlagt vedligehold · '
 'Funktionærer · Montører · Rekruttere · Oplære · Udvikle · Servicebesøg · Projektopgaver · Tilbud '
 '· Rammeaftaler · Forretningsudvikler · Dataplatform · Energibesparelser · Alarmer · Drift · '
 'Kvalitet · VVS · Energi · IoT · CTS · Struktureret · Kundevendt · FLD Skolen · Tillid · Frihed '
 'under ansvar')


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

    m.models_table("DRIFTENS STYRING — AFTALER, MENNESKER OG DATA",
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
    m.models_table("FØRSTE 90 DAGE — FRA AFTALE TIL STABIL LEVERANCE",
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
    out = os.path.join(ROOT, "Shahram_Ajloo_FLD_DriftschefEnergi.docx")
    build(out)
    print("OK " + out)
