# -*- coding: utf-8 -*-
"""
Uggerly Installation — entrepriseleder EL, Odense.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Entrepriseleder EL | Uggerly Installation | Fra tilbud til aflevering'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = '3. november 2026'
RECIPIENT = 'Uggerly Installation, Odense · via Martin Tveit, Sensu A/S'
SUBJECT = 'Ansøgning: Entrepriseleder EL'

# ------------------------------------------------------------------ side 1
INTRO = ['En el-entreprise skal hænge sammen fra det første tilbud til den sidste mangel er lukket. Mandskab, '
 'materialer og arbejdstegninger skal være klar, når pladsen er det, og ændringer skal afklares, før de '
 'koster tid og penge. Hos Uggerly i Odense skal entrepriselederen både få den enkelte sag sikkert '
 'gennemført og være med til at udvikle relationerne på det fynske marked.',
 'Jeg vil begynde med at gennemgå den overdragne sag med afdelingslederen og derefter følge arbejdet på '
 'pladsen. Hvad er aftalt, hvad er regnet med, og hvor mangler vi afklaring? Det skal blive til en '
 'brugbar plan for bemanding, indkøb, udførelse og KS med tydelige aftaler om næste skridt.']

BULLETS = [('Få tilbud og udførelse til at hænge sammen',
  'I ELOHVAC har jeg fuldt P&L-ansvar og arbejder med tilbud, beregning, planlægning, materialer, '
  'underentreprenører og aflevering af el-, ventilations- og klimaanlæg. Jeg vil bruge den erfaring til '
  'at gennemgå mængder, forudsætninger og leverancer ved sagens opstart og holde økonomien op mod det '
  'arbejde, der faktisk er udført og mangler.'),
 ('Give mandskabet klare rammer',
  'Jeg leder i dag 5 elektrikere og 3 lærlinge med daglig planlægning, oplæring og opfølgning på '
  'sikkerhed og kvalitet. På Ventek-Air ledede jeg et team på 14 på 11 samtidige projekter og brugte '
  'tavlemøder og flaskehalsanalyse til at styre kapaciteten. På byggepladsen skal folk kende dagens '
  'prioritering og vide, hvem der tager fat, hvis tegninger, adgang eller materialer mangler.'),
 ('Følge ændringer og faggrænser til dørs',
  'Jeg vil koordinere rækkefølge og adgang med entreprenører og øvrige faggrupper og få konsekvenserne '
  'af ændringer frem i tide. Hos Novo Nordisk koordinerede jeg 25 specialister på 37 CAPEX-projekter à '
  'DKK 2–10 mio. med opfølgning på fremdrift, økonomi, risici og ressourcer. Den erfaring er relevant, '
  'når tekniske afhængigheder skal afklares uden at miste grebet om den enkelte el-leverance.'),
 ('Gøre kvalitet og kundekontakt til en del af hverdagen',
  'KS skal følge arbejdet, ikke samles i sidste øjeblik. Jeg vil bruge Uggerlys fælles digitale '
  'KS-system og følge åbne punkter frem til aflevering. Fra ELOHVAC har jeg erfaring med '
  'kundeleverancer og serviceaftaler; hos Novo med FAT/SAT og dokumenteret aflevering uden kritiske '
  'fund. Nye opgaver skal udvikles med afdelingslederen ud fra kundens faktiske behov og de aftaler, vi '
  'holder.')]

SYSTEM = ('På sidste side har jeg lagt en plan for de første 90 dage på en konkret entreprise. Først skal '
 'aftalegrundlag og ansvar være klart. Derefter følger en rullende plan for mandskab, materialer og '
 'pladsens afklaringer samt kort opfølgning på timer, økonomi og KS. Hvert åbent punkt skal have en '
 'ansvarlig og en dato, så afdelingslederen og kunden kan se, hvad der kræver en beslutning.')

MIRROR = ('Mit fundament er B.Tech i Technology Management & Mechanical Engineering og elautorisation som '
 'elautoriseret maskinmester (LV/MV/HV), med praktisk elektromekanisk og el-teknisk baggrund. Jeg '
 'kender installationsvirksomhedens hverdag fra tilbud og akutte opgaver til planlagt udførelse, '
 'medarbejderledelse og afleveringsdokumentation.')

HONEST = ('Min praktiske el-erfaring og autorisation er dokumenteret; et særskilt dansk elektrikersvendebrev og '
 'konkret erfaring med akkordstyring er ikke dokumenteret i CV’et. Det skal afklares med jer. Jeg har '
 'arbejdet med timer, kapacitet og økonomi, men vil ikke sidestille det med rutine i jeres '
 'akkordpraksis.')

CULTURE = ('Uggerlys vægt på godt håndværk, tydeligt ansvar og fejlfri aflevering passer til en arbejdsform med '
 'faste aftaler og tæt opfølgning på pladsen. Jeg er også professionel Claude-bruger og koder. Mine '
 'Python/Claude API-værktøjer til tilbud, tidsplaner, KS og KPI har givet over 40 % produktivitetsløft '
 'i entreprisedrift. Hos Uggerly skal eventuel anvendelse understøtte jeres eksisterende systemer og '
 'følge reglerne for kunde- og projektdata.')

PRACTICAL = ('Jeg bor i Måløv og opfylder derfor ikke kravet om bopæl cirka 45 minutters kørsel fra Odense. En '
 'eventuel lokal bopæls-/flytteløsning skal afklares, før et videre forløb giver mening; jeg har ikke '
 'truffet en flyttebeslutning. Start og overgangen fra ELOHVAC skal også aftales.')

CLOSING = ('Hvis bopælsspørgsmålet kan løses, vil jeg gerne tale om de entrepriser, I først har brug for hjælp '
 'til, og hvordan min erfaring kan bruges til både fremdrift og kundesamarbejde på Fyn.')

# ------------------------------------------------------------------ CV
PROFILE = ('En el-entreprise skal styres fra tilbudsberegning til aflevering med mandskab, materialer og økonomi '
 'i samme plan. Min erfaring er el-tekniske leverancer, entreprisestyring og medarbejderledelse med '
 'fuldt P&L i ELOHVAC. Elautoriseret maskinmester (LV/MV/HV) og B.Tech. Leder 5 elektrikere og 3 '
 'lærlinge; tidligere team på 14 på 11 projekter hos Ventek-Air. Professionel Claude-koder med egne '
 'værktøjer til tilbud, planlægning og KS. Konkret akkordpraksis og formelt uddannelsesgrundlag skal '
 'afklares. Bopæl Måløv opfylder ikke Odense-kravet; lokal løsning er ikke aftalt.')

PRACTICE = [('El-teknik og entreprisestyring',
  'ELOHVAC: installation, tavler, styring, fejlfinding og forebyggende vedligehold på el-, '
  'ventilations- og klimaanlæg. Tilbud/beregning, planlægning, materialer, underentreprenører, KS og '
  'aflevering med fuldt P&L.'),
 ('Ledelse på skiftende pladser',
  '5 elektrikere og 3 lærlinge med daglig planlægning, 1:1/MUS, struktureret oplæring og '
  'situationsbestemt ledelse. LOTO, APV og risikovurdering ved pladsopstart; ingen kritiske afvigelser '
  'i serviceaftalerne.'),
 ('Kapacitet og fremdrift',
  'Ventek-Air: 11 samtidige projekter og et team på 14 fra specifikation til formel aflevering. Udbud, '
  'tilbud, underentreprenører og aftalegrundlag. Daglige tavlemøder og flaskehalsanalyse.'),
 ('Tekniske grænseflader',
  'Novo: 37 CAPEX-projekter à DKK 2–10 mio. med koordinering af 25 specialister på tværs af '
  'engineering, indkøb og anlæg. Opfølgning på økonomi, ressourcer og risici samt rapportering til '
  'bygherre og ledelse.'),
 ('Kvalitet og aflevering',
  'ELOHVAC KS og afleveringsdokumentation. Novo FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA uden kritiske '
  'fund ved aflevering. Erfaring med test, åbne punkter og dokumenteret accept.'),
 ('Digitale værktøjer i dagligdagen',
  'Python/Claude API til tilbud, tidsplaner, KS og KPI med over 40 % produktivitetsløft i '
  'entreprisedrift. Excel/Power Query, Power BI og SAP økonomi/aktiver. Nye værktøjer skal passe til '
  'virksomhedens aftalte systemer.')]

MODELS = [('Sagsoverdragelse',
  'Gennemgå aftalegrundlag, tilbudsforudsætninger, leverancer og åbne afklaringer med afdelingslederen. '
  'Aftal beslutningsrum og opfølgning.'),
 ('Plads- og ressourceplan',
  'Brug tavlemøder og flaskehalsanalyse fra Ventek. Hold mandskab, materialer, værktøj og '
  'arbejdstegninger op mod den faktiske udførelsesplan.'),
 ('Økonomi og ændringer',
  'Følg timer, forbrug og restarbejde. Gør konsekvenser for tid, pris og bemanding synlige og få '
  'ændringer afklaret efter sagens aftalegrundlag.'),
 ('Sikkerhed og oplæring',
  'LOTO/APV/risikovurdering og tydelig instruktion fra ELOHVAC/Biofos. Tilpas støtte til erfaring; '
  'lærlinge skal have klare opgaver og faglig hjælp.'),
 ('KS og aflevering',
  'Brug Uggerlys digitale KS-system. Aftal kontroller og dokumentation tidligt, følg mangler til '
  'lukning og gør overdragelsen brugbar for kunden.'),
 ('Problemer og ansvar',
  'PDCA/A3/5xHvorfor ved gentagne fejl. En enkel ansvarsmatrix (RACI) kan afklare tvivl mellem fag; '
  'brug den eksisterende projektorganisation.')]

ACHIEVEMENTS = [('5 elektrikere og 3 lærlinge i ELOHVAC',
  'Direkte personaleledelse, oplæring og fuldt P&L med tilbud, materialer og entreprisestyring.'),
 ('11 projekter og 14 medarbejdere hos Ventek-Air',
  'Kapacitetsstyring, tavlemøder og ansvar fra specifikation til formel aflevering.'),
 ('37 CAPEX-projekter hos Novo Nordisk',
  'DKK 2–10 mio. pr. projekt; koordinering af 25 specialister og aflevering uden kritiske fund.'),
 ('Over 40 % produktivitetsløft i entreprisedrift',
  'Egne Python/Claude API-værktøjer til tilbud, tidsplaner, KS og KPI-opfølgning.')]

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

PRACTICAL_CV = ('Bopæl i Måløv (Ballerup Kommune). Kravet om at bo inden for cirka 45 minutters kørsel fra Odense er '
 'ikke opfyldt. Lokal bopæls-/flytteløsning kræver særskilt afklaring; ingen beslutning eller aftale '
 'foreligger. Start og overgang fra ELOHVAC aftales. Dansk og persisk/farsi på modersmålsniveau, '
 'engelsk professionelt i skrift og tale. Kørekort B. Elautoriseret maskinmester LV/MV/HV; særskilt '
 'dansk elektrikersvendebrev og konkret akkorderfaring er ikke dokumenteret i CV’et.')

REFERENCES = 'Tidligere ledere hos Novo Nordisk og Biofos (Lynetten) — oplyses efter aftale.'

PARTNER = [('Afdelingslederen',
  'Holde overblik over egen sag og løfte undtagelser med et forslag til løsning. Aftale bidrag til '
  'salg, kundekontakt og andre opgaver ud fra afdelingens behov og den faktiske kapacitet. Ingen '
  'påstået eksisterende kundebase på Fyn.'),
 ('Elektrikere og lærlinge',
  'Gøre opgaver, prioritering og sikkerhed tydelige. Følge op på manglende afklaringer og sørge for '
  'faglig støtte til lærlinge. Aftaler skal kunne bruges på pladsen, ikke kun stå i en plan.'),
 ('Entreprenører og øvrige faggrupper',
  'Koordinere adgang, rækkefølge og tekniske grænseflader. Arbejde efter de gældende arbejdstegninger '
  'og få ændringer tilbage i projektgrundlaget, så fagene ikke udfører efter hver sin version.'),
 ('Kunder og samarbejdspartnere',
  'Være tydelig om aftalt leverance og konsekvenser af ændringer. Følge beslutninger og åbne punkter '
  'til dørs og bruge kundens behov som grundlag for videre samarbejde sammen med afdelingslederen.')]

FIRST90 = [('Første uge',
  'Forudsætter afklaret lokal bopæl/tilstedeværelse. Gennemgå en konkret el-entreprise med '
  'afdelingslederen: aftaler, tilbud, økonomi, tidsplan og risici. Møde mandskab og pladsens '
  'samarbejdspartnere. Lære KS-systemet og få åbne spørgsmål om materialer, arbejdstegninger og adgang '
  'fordelt med ansvar og dato.'),
 ('Inden dag 30',
  'Få en rullende udførelsesplan med mandskab, materialer, værktøj og faggrænser. Aftale kort '
  'opfølgning på timer, økonomi, ændringer og KS. Gennemgå akkordpraksis med den ansvarlige og afklare '
  'nødvendig oplæring. Sikre, at kunden og pladsen kender de næste beslutninger og leverancer.'),
 ('Inden dag 60',
  'Drive den aftalte entreprise og følge fremdrift, kvalitet og restarbejde sammen med mandskabet. '
  'Afklare ændringer, før de låser udførelsen. Tage et konkret tilbagevendende problem op med de '
  'berørte fag og kontrollere, om løsningen hjælper. Drøfte reelle kundehenvendelser og mulige nye '
  'opgaver med afdelingslederen.'),
 ('Inden dag 90',
  'Gennemgå økonomi, leverancer og næste milepæl med afdelingslederen og kunden efter aftale. '
  'Kontrollere plan for test, dokumentation, mangler og aflevering. Samle erfaringer fra pladsen og '
  'aftale videre opgaver og støtte. Vurdere kapacitet, før der tilføjes serviceprojekter, typehuse '
  'eller grøn energi.')]

KEYWORDS = ('El-entrepriser · Tilbud og beregning · Planlægning og materialestyring · Mandskabsledelse · '
 'Projektøkonomi · Kundekontakt · Underentreprenører · Tekniske grænseflader · KS og aflevering · LOTO '
 'og APV · Tavlemøder og flaskehalsanalyse · Python og Claude API.')


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

    m.models_table("ENTREPRISESTYRING OG PLADSLEDELSE",
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
    m.models_table("FØRSTE 90 DAGE — SAG, PLADS OG KUNDE",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SAMARBEJDET I HVERDAGEN")
    for label, body in PARTNER:
        m.bullet(label, body, after=30)

    m.section("FRA TILBUDSGRUNDLAG TIL AFLEVERET ENTREPRISE")
    m.para('Jeg vil begynde med at sammenholde det aftalte arbejde med pladsens faktiske forudsætninger. Er de gældende tegninger til rådighed, er materialer og værktøj klar, og kan arbejdet udføres i den planlagte rækkefølge? Hvis et andet fag eller en teknisk afklaring spærrer, skal næste handling og ansvar være tydeligt. Timer og materialer skal følges sammen med restarbejdet, så en fremdriftsmelding også siger noget om økonomien. Ved ændringer skal pris, tid og aftalegrundlag afklares, og dokumentationen følge den udførte løsning. KS og nødvendige test skal ind i planen undervejs. Det giver et bedre grundlag for en aflevering, hvor de sidste punkter bliver lukket, og kunden ved, hvad der er leveret.', after=80)

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
    build(os.path.join(ROOT, "Shahram_Ajloo_Uggerly_EntrepriselederEL.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_Uggerly_EntrepriselederEL.docx"))
