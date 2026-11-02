# -*- coding: utf-8 -*-
"""
Sweco — projektleder til procesanlæg i Vand og Klima.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Projektleder | Sweco Vand og Klima | Procesanlæg og sikker drift'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = '3. november 2026'
RECIPIENT = 'Sweco · Vand og Klima · Ørestad'
SUBJECT = 'Ansøgning: Projektleder til procesanlæg i Vand og Klima'

# ------------------------------------------------------------------ side 1
INTRO = ['Et renseanlæg skal kunne fungere, mens det bliver vedligeholdt, ændret og udviklet. Derfor skal '
 'projektets procesvalg, tekniske leverancer og tidsplan hænge sammen med både driften og de krav, '
 'anlægget skal leve op til. Projektlederen skal samle kunden og specialisterne om et grundlag, der er '
 'til at træffe beslutninger på – og følge beslutningerne helt frem til et anlæg, der kan overtages.',
 'Jeg vil begynde med at få kundens behov og projektets åbne spørgsmål frem: Hvad skal anlægget kunne, '
 'hvilke forhold begrænser løsningen, og hvad skal afklares før næste fase? Det skal blive til en '
 'fælles plan med ansvar, økonomi og beslutningspunkter. Driftsorganisationen skal med tidligt, så den '
 'løsning, der projekteres, også kan bruges og vedligeholdes i hverdagen.']

BULLETS = [('Tage driften med ind i projektet',
  'Fra Biofos på Lynetten har jeg erfaring med kritisk el- og mekanisk drift, pumper, HVAC, '
  'højspændingstavler og SCADA. Jeg kender betydningen af vedligehold, reservedele, sikker fejlfinding '
  'og klare aftaler, når et anlæg skal holdes i gang. Det perspektiv vil jeg bruge i dialogen med '
  'kunden og de projekterende; procesdimensionering og valg af renseteknologi skal ske med de '
  'ansvarlige processpecialister.'),
 ('Holde de tværfaglige leverancer sammen',
  'Hos Novo Nordisk koordinerede jeg 25 specialister på 37 CAPEX-projekter à DKK 2–10 mio. på tværs af '
  'engineering, indkøb og anlæg. Jeg fulgte fremdrift, økonomi, risici og ressourcer og rapporterede '
  'til ledelse og bygherre. Hos Sweco vil jeg bruge den erfaring til at få tekniske afhængigheder og '
  'manglende afklaringer frem, før de rammer tidsplanen.'),
 ('Gøre aftaler og udbudsgrundlag tydelige',
  'På Ventek-Air arbejdede jeg med 11 samtidige projekter fra specifikation til formel aflevering, '
  'herunder udbud, tilbud, underentreprenører og dokumentation. I ELOHVAC har jeg fuldt P&L-ansvar og '
  'løbende kundedialog om opgaver, materialer og levering. I et rådgiverprojekt skal tekniske '
  'beskrivelser og kravspecifikationer gennemgås med de rette fagpersoner, så ansvar, grænseflader og '
  'acceptkrav er klare.'),
 ('Følge kvaliteten helt til aflevering',
  'FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA hos Novo gav erfaring med test, åbne punkter og dokumenteret '
  'accept uden kritiske fund ved aflevering. Den arbejdsdisciplin kan bruges til at holde styr på '
  'kvalitetssikring og leverancer. Vandprojekternes konkrete krav og godkendelser skal aftales med '
  'kunden og de fagansvarlige; en myndighedsansøgning er ikke det samme som en tilladelse.')]

SYSTEM = ('På sidste side har jeg lagt en plan for de første 90 dage på et konkret projekt. Først skal opgaven '
 'og beslutningsrummet være klart. Derefter følger et fælles billede af tidsplan, økonomi, tekniske '
 'leverancer og myndighedsafklaringer. Opfølgningen skal være kort og brugbar: Hvad mangler, hvem tager '
 'næste skridt, og hvornår skal kunden eller projektledelsen beslutte noget?')

MIRROR = ('Mit fundament er B.Tech i Technology Management & Mechanical Engineering og elautorisation som '
 'elautoriseret maskinmester (LV/MV/HV). Erfaringen spænder fra drift på Lynetten til tekniske '
 'anlægsprojekter, tværfaglig koordinering og ledelse af elektrikere og lærlinge. Det giver et praktisk '
 'blik for sammenhængen mellem projekt, udførelse og drift.')

HONEST = ('Jeg kan ikke dokumentere 5–10 år som projektleder for vandbehandlingsanlæg, selvstændig '
 'procesprojektering eller ansvar for udlednings- og tilslutningstilladelser. Derfor skal et match '
 'bygge på min tekniske projekt- og driftserfaring med en tydelig faglig arbejdsdeling og oplæring i '
 'vandprojekternes proces- og myndighedsgrundlag.')

CULTURE = ('Swecos decentrale ansvar og faglige sparring passer til en arbejdsform, hvor beslutninger træffes tæt '
 'på opgaven, og tvivl bringes frem i tide. Jeg er også professionel Claude-bruger og koder. Mine '
 'Python/Claude API-værktøjer til tilbud, planlægning, KS og KPI har givet over 40 % produktivitetsløft '
 'i entreprisedrift. Hos Sweco skal eventuel brug tage udgangspunkt i et reelt behov og følge jeres '
 'regler for kundedata og systemer.')

PRACTICAL = ('Jeg bor i Måløv og ønsker arbejdssted i Ørestad. Startdato, rejser i forbindelse med projekterne og '
 'overgangen fra ELOHVAC skal aftales.')

CLOSING = ('Jeg vil gerne drøfte, hvilke projekter der har brug for min kombination af driftsforståelse og '
 'teknisk projektledelse, og hvordan samarbejdet med proces- og myndighedsspecialisterne kan '
 'tilrettelægges.')

# ------------------------------------------------------------------ CV
PROFILE = ('Procesanlæg skal projekteres og afleveres med blik for den drift, der følger efter. Min baggrund er '
 'teknisk projektledelse, tværfaglig koordinering og kritisk el- og mekanisk drift på Biofos, Lynetten. '
 'B.Tech og elautoriseret maskinmester (LV/MV/HV). Hos Novo koordinerede jeg 25 specialister på 37 '
 'CAPEX-projekter; hos Ventek-Air ledede jeg et team på 14 på 11 projekter. Erfaringen omfatter ikke '
 '5–10 års projektledelse af vandbehandlingsanlæg eller selvstændigt ansvar for procesdimensionering og '
 'miljøtilladelser. Professionel Claude-koder med egne planlægnings- og kvalitetsværktøjer.')

PRACTICE = [('Driftserfaring fra renseanlæg',
  'Biofos, Lynetten: kritisk 24/7-drift med pumper, HVAC, højspændingstavler og SCADA. Forebyggende '
  'vedligehold, akut fejlfinding, reservedelsflow, LOTO og risikovurdering. Relevant driftsindsigt, '
  'ikke et tidligere ansvar for renseprocessernes projektering.'),
 ('Tværfaglig projektstyring',
  'Novo: 37 samtidige CAPEX-projekter à DKK 2–10 mio. med koordinering af 25 specialister på tværs af '
  'engineering, indkøb og anlæg. Opfølgning på fremdrift, økonomi, risici og ressourcer samt '
  'rapportering til bygherre og ledelse.'),
 ('Fra specifikation til aflevering',
  'Ventek-Air: 11 projekter og et team på 14. Udbud, tilbud, underentreprenører, sikkerheds- og '
  'afleveringsdokumentation. Tavlemøder, kapacitetsstyring og flaskehalsanalyse.'),
 ('Kunder og projektøkonomi',
  'ELOHVAC: tilbud, beregning, materialer og underentreprenører med fuldt P&L. Kundedialog og '
  'kvalitetssikring af el-, ventilations- og klimaleverancer. Økonomiske konsekvenser og ændringer skal '
  'frem, før de bliver en overraskelse.'),
 ('Test og dokumenteret kvalitet',
  'Novo: FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA uden kritiske fund ved aflevering. Erfaring med at '
  'koordinere test, følge åbne punkter og samle dokumentation frem mod accept.'),
 ('Forbedringer og digitale værktøjer',
  'PDCA, A3 og 5xHvorfor i drift/projekter. SAP økonomi og aktiver, Excel/Power Query og Power BI. Egne '
  'Python/Claude API-værktøjer har givet over 40 % produktivitetsløft i entreprisedrift.')]

MODELS = [('Plan og tekniske grænseflader',
  'Aftal leverancer og ansvar på tværs af fag. Knyt åbne afklaringer til tidsplanen med en ansvarlig og '
  'en dato.'),
 ('Kundens beslutningsgrundlag',
  'Saml alternativer, forudsætninger, økonomi og risici med fagpersonerne. Kunden skal kunne se '
  'konsekvensen af at vælge – eller udskyde en beslutning.'),
 ('Myndighedsafklaringer',
  'Få fagansvarlig til at afklare udlednings- og tilslutningstilladelser, nødvendige input og vilkår. '
  'Følg afhængighederne i planen; antag ikke en godkendelse.'),
 ('Fremdrift og risikostyring',
  'Brug en kort risiko- og beslutningsliste i projektets aftalte system. Følg budget, ændringer og '
  'næste milepæl sammen med kunden.'),
 ('Kvalitet og problemløsning',
  'Aftal fagkontrol og acceptkrav tidligt. Brug PDCA/A3/5xHvorfor ved gentagne problemer og følg op på '
  'effekten.'),
 ('Samarbejde og ansvar',
  'En enkel ansvarsmatrix (RACI) kan afklare tvivl. Tavlemøder og flaskehalsanalyse fra Ventek bruges '
  'til at få opgaver videre, ikke til ekstra rapportering.')]

ACHIEVEMENTS = [('37 CAPEX-projekter hos Novo Nordisk',
  'DKK 2–10 mio. pr. projekt; koordinering af 25 specialister på tværs af engineering, indkøb og '
  'anlæg.'),
 ('Aflevering uden kritiske fund', 'FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA hos Novo Nordisk.'),
 ('11 projekter og 14 medarbejdere hos Ventek-Air',
  'Kapacitetsstyring, tavlemøder og ansvar fra specifikation til formel aflevering.'),
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

PRACTICAL_CV = ('Bopæl i Måløv (Ballerup Kommune), ønsket kontor i Ørestad. Stillingen tilbyder også Aarhus. '
 'Startdato, projektbesøg/rejser og overgangen fra ELOHVAC skal aftales; ingen omgående tilgængelighed '
 'forudsat. Dansk og persisk/farsi på modersmålsniveau, engelsk professionelt i skrift og tale. '
 'Kørekort B. B.Tech og elautoriseret maskinmester (LV/MV/HV).')

REFERENCES = 'Tidligere ledere hos Novo Nordisk og Biofos (Lynetten) — oplyses efter aftale.'

PARTNER = [('Kunden og driftsorganisationen',
  'Forstå både målet med investeringen og de daglige begrænsninger. Aftal forventninger og følg op. '
  'Tillidsfulde kunderelationer bygges ved at holde aftaler og sige til, når forudsætninger ændrer sig. '
  'Nye projektmuligheder skal udspringe af et reelt behov.'),
 ('Proces- og fagspecialister',
  'Saml deres input til procesvalg, optimering og fremtidige rensekrav. Gør afhængighederne mellem '
  'proces, mekanik, el og styring synlige. Selvstændig dimensionering og vurdering af renseteknologi er '
  'ikke min dokumenterede specialistkompetence.'),
 ('Myndigheder og myndighedsrådgivere',
  'Forbered dialogen sammen med den fagansvarlige, så spørgsmål, input og forventede afgørelser er '
  'tydelige. Følg tilladelser og vilkår i tidsplanen. Jeg har ikke dokumenteret eget ansvar for disse '
  'miljømyndighedsprocesser.'),
 ('Projektingeniører og udførende',
  'Aftal tekniske grænseflader, fagkontrol og dokumentationskrav. Ved ændringer skal den gældende '
  'løsning og dens konsekvenser være kendt af dem, der projekterer, udfører og senere overtager '
  'anlægget.')]

FIRST90 = [('Første uge',
  'Aftale et konkret projekt, ansvar og beslutningsrum med lederen. Møde kunden, projektingeniører og '
  'proces-/myndighedsspecialister. Gennemgå opgave, økonomi, tidsplan og åbne beslutninger. Afklare min '
  'oplæring og faglige støtte. Få de vigtigste afklaringer på en fælles liste med ansvar og næste '
  'handling.'),
 ('Inden dag 30',
  'Gennemgå projektgrundlag og driftsbehov med kunden og fagpersonerne. Samle tekniske leverancer, '
  'fagkontrol og myndighedsafklaringer i projektets aftalte plan. Afklare, hvilke tilladelser og '
  'beslutninger der styrer næste fase. Etablere kort, fast opfølgning på fremdrift, økonomi, risici og '
  'ændringer.'),
 ('Inden dag 60',
  'Føre et aftalt delprojekt eller en fase videre med teamet. Få tværfaglige afklaringer frem før '
  'fagkontrol og næste kundebeslutning. Gennemgå udbuds- eller projekteringsmateriale med de ansvarlige '
  'specialister og følge kommentarer til lukning. Drøfte eventuelle yderligere behov med kunden uden at '
  'love løsninger uden for det aftalte grundlag.'),
 ('Inden dag 90',
  'Gennemgå leverancer, økonomi, risici og næste milepæl med kunde og leder. Bekræfte, at næste fase '
  'bygger på de aftalte faglige kontroller og myndighedsafklaringer. Samle erfaringer fra teamet og '
  'driften. Aftale næste projektansvar og fortsat oplæring på baggrund af den konkrete erfaring.')]

KEYWORDS = ('Teknisk projektledelse · Tværfaglige teams · Anlægsdrift · Pumper og SCADA · Udbud og tilbud · '
 'Projektøkonomi · Risikostyring · Kundedialog · FAT/SAT · Kvalitetssikring · Afleveringsdokumentation '
 '· PDCA og A3 · SAP økonomi/aktiver · Python og Claude API.')


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

    m.models_table("PROJEKTSTYRING OG FAGLIGT SAMARBEJDE",
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
    m.models_table("FØRSTE 90 DAGE — KUNDE, GRUNDLAG OG FREMDRIFT",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SAMARBEJDET I HVERDAGEN")
    for label, body in PARTNER:
        m.bullet(label, body, after=30)

    m.section("FRA DRIFTSBEHOV TIL ET AFKLARET PROJEKT")
    m.para('Når et eksisterende anlæg ændres, vil jeg få driftens forudsætninger frem sammen med kunden: Hvilke dele skal holdes i gang, hvor er der adgangs- eller vedligeholdsproblemer, og hvad kræver ombygningen af planlagte stop? Processpecialisterne skal vurdere kapacitet, procesvalg og rensekrav, mens myndighedsrådgiveren afklarer tilladelser og vilkår. Projektlederens opgave er at få de svar koblet til de tekniske beskrivelser, økonomien og tidsplanen. Før næste fase skal vi kunne se, hvad der er kontrolleret, hvad kunden har besluttet, og hvilke forbehold der stadig gælder. Klimatilpasning og fremtidige miljøkrav skal vurderes af de relevante fagpersoner og afspejles i løsningen, ikke blot stå som en ambition i projektbeskrivelsen.', after=80)

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
    build(os.path.join(ROOT, "Shahram_Ajloo_Sweco_ProjektlederVandKlima.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_Sweco_ProjektlederVandKlima.docx"))
