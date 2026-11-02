# -*- coding: utf-8 -*-
"""
Sweco — senior energiplanlægger.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Senior energiplanlægger | Sweco Energi | Analyse, økonomi og kundedialog'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = '3. november 2026'
RECIPIENT = 'Sweco Energi · Senior energiplanlægger'
SUBJECT = 'Ansøgning: Senior energiplanlægger'

# ------------------------------------------------------------------ side 1
INTRO = ['En varmeplan skal kunne bruges til at træffe en beslutning – ikke kun vise, hvad der teknisk kan lade '
 'sig gøre. Forbruget, varmekilderne og kapaciteten skal hænge sammen med økonomi, myndighedskrav og '
 'kundens mulighed for at gennemføre projektet. Swecos opgave er at samle de hensyn og gøre både '
 'muligheder og usikkerheder forståelige for forsyninger, kommuner og andre kunder.',
 'Jeg vil begynde med det valg, kunden står overfor, og få grundlaget for det på plads: Hvilke behov '
 'skal dækkes, hvilke data har vi, og hvad kan ændre anbefalingen? Derfra skal analysen føre til et '
 'overskueligt beslutningsgrundlag med tydelige forudsætninger, alternativer og næste skridt. '
 'Kundedialogen skal forme opgaven fra starten, ikke først komme, når beregningen er færdig.']

BULLETS = [('Forbinde energidata med praktiske forbedringer',
  'Hos Novo Nordisk gav et PDCA-program 40 % lavere energiomkostninger. Min baggrund omfatter også '
  'kritisk drift med pumper, HVAC og SCADA hos Biofos samt el-, ventilations- og klimaleverancer i '
  'ELOHVAC. Det giver en praktisk indgang til energiforbrug og drift. Resultatet hos Novo er ikke et '
  'fjernvarmeplanlægningsprojekt, men det er erfaring med at følge en forbedring helt frem til en '
  'økonomisk effekt.'),
 ('Gøre økonomi og forudsætninger synlige',
  'Jeg arbejder med Excel/Power Query, Power BI og egne Python-værktøjer, herunder investeringsmodeller '
  'med NPV/IRR, scenarier og følsomhed. I en energiopgave vil jeg bruge det til at gøre datakilder, '
  'antagelser og usikkerheder efterprøvelige. En virksomhedsøkonomisk beregning kan ikke uden videre '
  'bruges som et projektforslag efter Varmeforsyningsloven; den del skal følge det relevante grundlag '
  'og kontrolleres af erfarne fagpersoner.'),
 ('Omsætte kundens behov til en afgrænset opgave',
  'I ELOHVAC har jeg fuldt P&L-ansvar og arbejder med tilbud, beregning, materialer, underentreprenører '
  'og kundeleverancer. På Ventek-Air indgik udbud og tilbud i 11 samtidige tekniske projekter. Den '
  'erfaring vil jeg bruge i behovsafklaring og tilbudsarbejde: Hvad skal kunden kunne beslutte, hvad '
  'leverer vi, og hvilke afklaringer er nødvendige? Jeg kommer ikke med et påstået etableret marked '
  'blandt kommuner og fjernvarmeforsyninger.'),
 ('Samle specialister om anbefalingen',
  'Hos Novo koordinerede jeg 25 specialister på 37 CAPEX-projekter à DKK 2–10 mio. på tværs af '
  'engineering, indkøb og anlæg. Jeg fulgte fremdrift, økonomi og risici og rapporterede til bygherre '
  'og ledelse. Hos Sweco skal teknologivalg, netforhold og myndighedsspørgsmål kvalificeres sammen med '
  'specialisterne, så kunden får én sammenhængende anbefaling med klare forbehold.')]

SYSTEM = ('På sidste side har jeg beskrevet de første 90 dage omkring en konkret kundeopgave. Først skal ansvar '
 'og faglig støtte aftales. Derefter følger gennemgang af datagrundlag, forudsætninger og alternativer '
 'med kunden og teamet. En enkel beslutnings- og afklaringsliste skal holde analysen på sporet og vise, '
 'hvad der skal være afgjort, før projektet kan videre.')

MIRROR = ('Det tekniske fundament er B.Tech i Technology Management & Mechanical Engineering og elautorisation '
 'som elautoriseret maskinmester (LV/MV/HV). Drift, tekniske projekter og økonomisk ansvar er min '
 'baggrund. Jeg er vant til at forbinde tekniske detaljer med det arbejde og de omkostninger, der '
 'følger i praksis.')

HONEST = ('Min erfaring dokumenterer ikke seniorrådgivning i fjernvarme, projektforslag efter '
 'Varmeforsyningsloven eller eget ansvar for myndighedsprocesser. EnergyPRO har jeg heller ikke '
 'dokumenteret erfaring med. Et match kræver derfor en konkret vurdering af, om min energi-, analyse- '
 'og kundebaggrund kan bruges med den rette faglige arbejdsdeling; oplæring alene erstatter ikke den '
 'specialisterfaring, rollen efterspørger.')

CULTURE = ('Swecos ansvar tæt på kunderne og faglige sparring på tværs tiltaler mig. Jeg vil bidrage med praktisk '
 'driftsforståelse, åbne beregninger og tydelig opfølgning og bruge kollegernes specialistviden aktivt. '
 'Jeg er professionel Claude-bruger og koder; egne Python/Claude API-værktøjer har givet over 40 % '
 'produktivitetsløft i entreprisedrift. Eventuel anvendelse hos Sweco skal følge godkendte systemer, '
 'fagkontrol og regler for kundedata.')

PRACTICAL = ('Jeg bor i Måløv og foretrækker et kontor i Storkøbenhavn, hvis det passer til teamet. Stillingen er '
 'opslået til hele landet; konkret kontor, projektbesøg, startdato og overgangen fra ELOHVAC skal '
 'aftales.')

CLOSING = ('Jeg vil gerne drøfte, hvor I har størst behov for at forbinde energianalyse, teknisk '
 'projektforståelse og kundedialog, og om der er et realistisk match med min baggrund.')

# ------------------------------------------------------------------ CV
PROFILE = ('Energiplanlægning skal føre til valg, kunden kan forstå og gennemføre. Min baggrund er '
 'energioptimering, teknisk drift, projektkoordinering og kommercielt ansvar. Hos Novo gav et '
 'PDCA-program 40 % lavere energiomkostninger, og jeg koordinerede 25 specialister på 37 '
 'CAPEX-projekter. B.Tech og elautoriseret maskinmester (LV/MV/HV). Arbejder med Excel/Power Query, '
 'investeringsmodeller og Python/Claude API. Seniorrådgivning om fjernvarme, projektforslag efter '
 'Varmeforsyningsloven og EnergyPRO er ikke dokumenteret erfaring; den faglige arbejdsdeling skal '
 'afklares.')

PRACTICE = [('Energi og økonomisk effekt',
  'Novo Nordisk: PDCA-program med 40 % reduktion af energiomkostninger. Teknisk projektarbejde med '
  'opfølgning på økonomi, risici og ressourcer. SAP brugt til økonomi, aktiver og omkostninger.'),
 ('Analyseværktøjer og investeringsmodeller',
  'Excel/Power Query, Power BI og Python. Egne værktøjer med NPV/IRR, følsomhed og scenarier. '
  'Datakilder og antagelser skal kunne gennemgås; modellerne er ikke en påstået erstatning for '
  'EnergyPRO eller lovpligtige projektforslag.'),
 ('Kundedialog og tilbud',
  'ELOHVAC: fuldt P&L, tilbud, beregning, materialer og underentreprenører samt KS og aflevering af '
  'el-, ventilations- og klimaanlæg. Ventek: udbud og tilbud som del af teknisk projektleverance.'),
 ('Tværfaglig koordinering',
  'Novo: 37 samtidige CAPEX-projekter à DKK 2–10 mio., koordinering af 25 specialister på tværs af '
  'engineering, indkøb og anlæg. Fremdrift og rapportering til bygherre/ledelse.'),
 ('Forståelse for drift og vedligehold',
  'Biofos Lynetten: kritisk 24/7-drift med pumper, HVAC, højspændingstavler og SCADA. Forebyggende '
  'vedligehold, fejlfinding og reservedelsflow. Relevant anlægsindsigt, ikke erfaring med '
  'fjernvarmeinfrastruktur eller netdimensionering.'),
 ('Faglig opfølgning og videndeling',
  'Ventek: team på 14 på 11 projekter, tavlemøder og flaskehalsanalyse. ELOHVAC: 5 elektrikere og 3 '
  'lærlinge med 1:1/MUS og oplæring. Python/Claude API-værktøjer har givet over 40 % produktivitetsløft '
  'i entreprisedrift.')]

MODELS = [('Kundens beslutning',
  'Afklar formål, leverance, beslutningstidspunkt og nødvendige input. Aftal, hvilke spørgsmål analysen '
  'skal besvare, før modellen bygges.'),
 ('Forudsætninger og scenarier',
  'Gør datakilder, reference og alternativer tydelige. Brug følsomhed til at vise, hvilke antagelser '
  'der kan ændre anbefalingen.'),
 ('Teknik og økonomi',
  'Hold investering, drift og usikkerheder sammen. Afklar beregningsgrundlag med fagansvarlig; adskil '
  'kundeøkonomi fra lovpligtige vurderinger.'),
 ('Fagkontrol og myndigheder',
  'Aftal, hvem der kvalitetssikrer teknologi-, net- og regulatoriske forhold. Få godkendelsesprocesser '
  'og åbne spørgsmål ind i planen.'),
 ('Projekt og samarbejde',
  'Træk på Novo-koordinering og Venteks tavlemøder. En enkel ansvarsmatrix (RACI) og beslutningsliste '
  'kan afklare næste handling på tværs af fag.'),
 ('Forbedring og læring',
  'Brug PDCA/A3/5xHvorfor til gentagne fejl og mangler. Del forudsætninger og erfaringer med '
  'kollegerne, så arbejdet kan efterprøves og bruges igen.')]

ACHIEVEMENTS = [('40 % lavere energiomkostninger hos Novo',
  'PDCA-program i teknisk drift/projektmiljø; ikke et fjernvarmestrategi- eller varmeplanresultat.'),
 ('37 CAPEX-projekter hos Novo Nordisk',
  'DKK 2–10 mio. pr. projekt; koordinering af 25 specialister på tværs af engineering, indkøb og '
  'anlæg.'),
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

PRACTICAL_CV = ('Bopæl i Måløv (Ballerup Kommune). Storkøbenhavn foretrækkes som kontor, men det konkrete team og '
 'kontor skal aftales; opslaget angiver hele landet. Projektbesøg/rejser, startdato og overgang fra '
 'ELOHVAC aftales. Ingen bestemt hjemmearbejdsordning eller omgående start forudsat. Dansk og '
 'persisk/farsi på modersmålsniveau, engelsk professionelt i skrift og tale. Kørekort B.')

REFERENCES = 'Tidligere ledere hos Novo Nordisk og Biofos (Lynetten) — oplyses efter aftale.'

PARTNER = [('Kunder og interessenter',
  'Lytte til behov, forretning og beslutningsproces. Forklare konsekvenser uden at skjule usikkerheder. '
  'Tilbud og nye opgaver skal bygge på et behov, en tydelig leverance og realistiske forudsætninger.'),
 ('Energiplanlæggere og tekniske specialister',
  'Samle input om varmekilder, net, teknologivalg og drift. Ved sektorkobling, overskudsvarme, '
  'varmepumper og lavtemperatursystemer skal vurderingen ske med de relevante fagpersoner; det er ikke '
  'dokumenterede egne specialistområder.'),
 ('Myndigheds- og økonomispecialister',
  'Afklare grundlag for projektforslag og myndighedsdialog tidligt. Lad erfarne kolleger kvalitetssikre '
  'lovgrundlag og de nødvendige økonomiske vurderinger. Hold ansøgninger, afgørelser og eventuelle '
  'vilkår adskilt i opfølgningen.'),
 ('Kollegaer og projektledelse',
  'Dele beregningsforudsætninger og driftsindsigt, gøre tvivl synlig og følge aftaler til dørs. Brug '
  'Swecos faglige netværk og sparring frem for at opbygge en parallel metode uden fagkontrol.')]

FIRST90 = [('Første uge',
  'Aftale rolle, faglig støtte og et afgrænset bidrag til en kundeopgave med lederen. Møde erfarne '
  'energiplanlæggere og kunden. Gennemgå formålet med analysen, kendte data og næste beslutning. '
  'Afklare behov for oplæring i værktøjer, fjernvarme og regulatorisk grundlag, før selvstændigt ansvar '
  'aftales.'),
 ('Inden dag 30',
  'Gennemgå forbrug, produktion, kapacitet og forudsætninger sammen med fagansvarlig. Aftale reference, '
  'alternativer og kvalitetssikring. Afklare med myndighedsspecialisten, hvilke processer og '
  'vurderinger opgaven kræver. Samle datamangler, ansvar og beslutningspunkter i projektets aftalte '
  'system.'),
 ('Inden dag 60',
  'Levere det aftalte analysebidrag til fagkontrol. Gennemgå økonomiske følsomheder og usikkerheder med '
  'specialisterne og bruge resultaterne i kundedialogen. Bidrage til et afgrænset tilbud eller en '
  'opgavebeskrivelse, hvis et reelt kundebehov er afdækket. Følge oplæringen og justere ansvar efter '
  'den konkrete kompetencevurdering.'),
 ('Inden dag 90',
  'Fremlægge det fagkontrollerede bidrag til beslutningsgrundlaget med teamet. Sikre, at kunden kan se '
  'alternativer, væsentlige forudsætninger og næste skridt. Evaluere leverance, kundedialog og faglige '
  'udviklingsbehov med lederen. Aftale videre opgaver ud fra faktisk kompetence og teamets behov, ikke '
  'anciennitet i de første måneder.')]

KEYWORDS = ('Energioptimering · Teknisk projektledelse · Kundedialog og tilbud · Projektøkonomi · '
 'Investeringsmodeller · NPV/IRR og følsomhed · Tværfaglig koordinering · Datagrundlag og dokumentation '
 '· PDCA og A3 · SAP økonomi/aktiver · Excel/Power Query · Power BI · Python og Claude API.')


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
    m.models_table("FØRSTE 90 DAGE — KUNDE, DATA OG FAGLIGT GRUNDLAG",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SAMARBEJDET I HVERDAGEN")
    for label, body in PARTNER:
        m.bullet(label, body, after=30)

    m.section("FRA ANALYSE TIL EN BEGRUNDET ANBEFALING")
    m.para('Jeg vil gennemgå et analysegrundlag med kunden og en erfaren energiplanlægger, før en anbefaling formuleres. Er forbrug og produktion sammenlignet på et relevant grundlag, og er kapacitet og driftsbegrænsninger synlige? Hvilke data er målte, hvilke er skøn, og hvor meget betyder det for valget? En vurdering af overskudsvarme eller varmepumper skal også hænge sammen med den modtagende løsning og kundens muligheder for at realisere projektet. Investerings- og driftsforudsætninger skal være tydelige, og de nødvendige regulatoriske og miljømæssige vurderinger skal udføres af kompetente fagpersoner. Til sidst skal kunden kunne se, hvad der taler for løsningen, hvad der kan ændre anbefalingen, og hvad der stadig mangler før en beslutning.', after=80)

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
    build(os.path.join(ROOT, "Shahram_Ajloo_Sweco_SeniorEnergiplanlaegger.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_Sweco_SeniorEnergiplanlaegger.docx"))
