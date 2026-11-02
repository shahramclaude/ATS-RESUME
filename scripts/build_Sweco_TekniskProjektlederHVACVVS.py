# -*- coding: utf-8 -*-
"""
Sweco — teknisk projektleder til HVAC og VVS.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Teknisk projektleder | Sweco | HVAC og VVS i bygninger i drift'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = '3. november 2026'
RECIPIENT = 'Sweco · Renovering & Installationer · Jan Urhammer'
SUBJECT = 'Ansøgning: Teknisk projektleder til HVAC og VVS'

# ------------------------------------------------------------------ side 1
INTRO = ['Når installationer skal renoveres i en bygning i drift, er den tekniske løsning kun en del af '
 'opgaven. Udførelsen skal også passe til brugerne, adgangen til installationerne og den drift, der '
 'skal fortsætte undervejs. Projektlederen skal samle kunden og fagene om en løsning, en økonomi og en '
 'plan, som kan gennemføres – og følge aftalerne helt til aflevering.',
 'Jeg vil begynde med en gennemgang af de eksisterende forhold sammen med kunden og de relevante '
 'kolleger. Hvad fungerer, hvad skal ændres, og hvilke begrænsninger giver bygningens brug? Det skal '
 'omsættes til en tydelig opgave med aftalte leverancer, tekniske afklaringer og beslutningspunkter, '
 'før vi lægger os fast på løsning og udførelsesplan.']

BULLETS = [('Forbinde løsningsvalg med drift og vedligehold',
  'Min erfaring omfatter el-, ventilations- og klimaanlæg i ELOHVAC og pumper, HVAC, el og SCADA i '
  'kritisk drift hos Biofos. Jeg vil bruge det praktiske blik i vurderingen af eksisterende '
  'installationer: Kan løsningen tilses og vedligeholdes, og hvad kræver ændringen af adgang og '
  'driftsstop? HVAC- og VVS-valg skal gennemgås med de rette fagpersoner, så forudsætninger og '
  'konsekvenser er klare.'),
 ('Samle projektteamet om fremdriften',
  'Hos Novo Nordisk koordinerede jeg 25 specialister på 37 CAPEX-projekter à DKK 2–10 mio. på tværs af '
  'engineering, indkøb og anlæg. På Ventek-Air ledede jeg et team på 14 på 11 samtidige projekter fra '
  'specifikation til formel aflevering. Tavlemøder og flaskehalsanalyse hjalp med at få afklaringer og '
  'kapacitet på plads. Hos Sweco skal samme opfølgning samle leverancerne på tværs af fagdiscipliner.'),
 ('Holde økonomi, omfang og ændringer sammen',
  'I ELOHVAC har jeg fuldt P&L-ansvar og arbejder med tilbud, beregning, materialer, underentreprenører '
  'og kundeleverancer. Ventek-erfaringen omfatter udbud, tilbud og aftalegrundlag. Jeg vil sikre, at '
  'kunden ved, hvad opgaven omfatter, og hvad en ændring betyder for pris, tid og leverance, før vi '
  'arbejder videre på nye forudsætninger.'),
 ('Gøre aflevering til en del af planen fra start',
  'Hos Novo arbejdede jeg med FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA uden kritiske fund ved aflevering. '
  'Den disciplin vil jeg bruge til at få test, dokumentation og åbne punkter fulgt til dørs. I en '
  'bygningsrenovering skal acceptkravene aftales med kunden og fagene, så driftspersonalet får et '
  'brugbart grundlag for at overtage installationerne.')]

SYSTEM = ('På sidste side har jeg lagt en konkret 90-dagesplan for et aftalt projekt. Først skal kundens behov, '
 'eksisterende forhold og min faglige opgavefordeling være afklaret. Derefter følger fælles plan, '
 'økonomi og en kort liste over åbne beslutninger. Kunden skal løbende kunne se, hvor projektet står, '
 'hvad der kræver en beslutning, og hvad næste skridt er.')

MIRROR = ('Det tekniske fundament er B.Tech i Technology Management & Mechanical Engineering, elautorisation som '
 'elautoriseret maskinmester (LV/MV/HV) og AMU i køleteknik og klimaanlæg. Erfaringen forbinder '
 'praktisk installation og drift med projektøkonomi, kundedialog og tværfaglig koordinering.')

HONEST = ('Jeg kommer fra entrepriser, idriftsættelse og drift – ikke en identisk rådgiverrolle. Selvstændig '
 'VVS-projektering og dimensionering er ikke dokumenteret i mit CV. Derfor skal vi konkret gennemgå, '
 'hvilke HVAC- og VVS-løsningsopgaver jeg kan tage fra start, og hvor der skal være specialiststøtte og '
 'fagkontrol. Det er en vigtig del af at vurdere matchet til rollen.')

CULTURE = ('Swecos kombination af ansvar og faglig sparring tiltaler mig. Jeg vil tage ansvar for aftalerne og '
 'samtidig bruge kollegernes viden, når en teknisk løsning skal udfordres. Jeg er professionel '
 'Claude-bruger og koder; mine Python/Claude API-værktøjer til tilbud, tidsplaner, KS og KPI har givet '
 'over 40 % produktivitetsløft i entreprisedrift. Eventuel brug hos Sweco skal passe til godkendte '
 'systemer, fagkontrol og regler for kundedata.')

PRACTICAL = ('Jeg bor i Måløv og søger rollen i København. Startdato, projektbesøg og overgangen fra ELOHVAC skal '
 'aftales.')

CLOSING = ('Jeg vil gerne drøfte, hvilke renoveringsopgaver der først skal løses, og hvordan min projekt- og '
 'driftserfaring kan bruges sammen med afdelingens installationsspecialister.')

# ------------------------------------------------------------------ CV
PROFILE = ('Tekniske renoveringer skal fungere for både bygningen, brugerne og den efterfølgende drift. Min '
 'erfaring omfatter el-, ventilations- og klimaleverancer, projektøkonomi og tværfaglig koordinering. '
 'B.Tech og elautoriseret maskinmester (LV/MV/HV), suppleret med AMU i køleteknik og klimaanlæg. I '
 'ELOHVAC har jeg fuldt P&L og leder 5 elektrikere og 3 lærlinge. Hos Novo koordinerede jeg 25 '
 'specialister på 37 CAPEX-projekter. Selvstændig VVS-projektering og dimensionering skal afklares; det '
 'er ikke dokumenteret erfaring. Professionel Claude-koder med egne planlægnings- og '
 'kvalitetsværktøjer.')

PRACTICE = [('Installationer og driftsforståelse',
  'ELOHVAC: installation, tavler, styring, fejlfinding og vedligehold på el-, ventilations- og '
  'klimaanlæg. Biofos: pumper, HVAC, højspændingstavler og SCADA i kritisk 24/7-drift. Praktisk '
  'forståelse for adgang, sikkerhed og vedligehold.'),
 ('Økonomi og kundeaftaler',
  'Fuldt P&L i ELOHVAC: tilbud, beregning, planlægning, materialer og underentreprenører samt KS og '
  'afleveringsdokumentation. Kundeleverancen skal hænge sammen med både aftaler og udførelse.'),
 ('Tværfaglig projektstyring',
  'Novo: 37 samtidige CAPEX-projekter à DKK 2–10 mio. med koordinering af 25 specialister på tværs af '
  'engineering, indkøb og anlæg. Opfølgning på fremdrift, økonomi, risici og ressourcer; rapportering '
  'til bygherre og ledelse.'),
 ('Fra specifikation til aflevering',
  'Ventek-Air: 11 projekter og et team på 14. Udbud, tilbud, underentreprenører, aftalegrundlag og '
  'sikkerheds-/afleveringsdokumentation. Tavlemøder, kapacitetsstyring og flaskehalsanalyse.'),
 ('Kvalitet og test',
  'Novo: FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA uden kritiske fund ved aflevering. LOTO, APV og '
  'risikovurdering indgår i installations- og driftsarbejdet.'),
 ('Digital støtte og forbedringer',
  'Egne Python/Claude API-værktøjer til tilbud, planlægning, KS og KPI med over 40 % produktivitetsløft '
  'i entreprisedrift. Excel/Power Query, Power BI og SAP økonomi/aktiver. PDCA, A3 og 5xHvorfor til '
  'forbedringer.')]

MODELS = [('Eksisterende forhold',
  'Gennemgå installationer og driftsbehov med kunde og fagpersoner. Notér datamangler, adgangsforhold '
  'og nødvendige afklaringer før løsningsvalg.'),
 ('Leverancer og ansvar',
  'Aftal omfang, fagkontrol og tekniske grænseflader. En enkel ansvarsmatrix (RACI) kan afklare tvivl '
  'mellem fag og projektledelse.'),
 ('Plan og kapacitet',
  'Brug erfaring med tavlemøder og flaskehalsanalyse til at følge leverancer og blokeringer. Afstem '
  'udførelse og eventuelle stop med bygningens drift.'),
 ('Økonomi og ændringer',
  'Følg aftalt budget, fremdrift og omfang. Vis konsekvenser af ændringer og få kundens beslutning '
  'dokumenteret før videre arbejde.'),
 ('Faglig kontrol og læring',
  'Lad de relevante fagpersoner kontrollere løsningen. Brug PDCA/A3/5xHvorfor ved gentagne problemer og '
  'del erfaringerne med teamet.'),
 ('Test og overdragelse',
  'Aftal acceptkrav og dokumentation tidligt. Følg åbne punkter til lukning og gennemgå '
  'driftsgrundlaget med dem, der skal overtage anlægget.')]

ACHIEVEMENTS = [('37 CAPEX-projekter hos Novo Nordisk',
  'DKK 2–10 mio. pr. projekt; koordinering af 25 specialister på tværs af engineering, indkøb og '
  'anlæg.'),
 ('11 projekter og 14 medarbejdere hos Ventek-Air',
  'Kapacitetsstyring, tavlemøder og ansvar fra specifikation til formel aflevering.'),
 ('Aflevering uden kritiske fund', 'FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA hos Novo Nordisk.'),
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

PRACTICAL_CV = ('Bopæl i Måløv (Ballerup Kommune), søger arbejdssted i København. Konkret kontor, projektbesøg, '
 'startdato og overgang fra ELOHVAC aftales. Dansk og persisk/farsi på modersmålsniveau, engelsk '
 'professionelt i skrift og tale. Kørekort B. B.Tech og elautoriseret maskinmester (LV/MV/HV), '
 'suppleret med AMU i køleteknik og klimaanlæg. Ingen omgående tilgængelighed forudsat.')

REFERENCES = 'Tidligere ledere hos Novo Nordisk og Biofos (Lynetten) — oplyses efter aftale.'

PARTNER = [('Kunden',
  'Være tydelig om leverance, økonomi og beslutninger og forklare tekniske valg i forhold til '
  'bygningens brug. Følg aftaler til dørs; yderligere opgaver skal udspringe af et reelt behov og en '
  'tydelig aftale.'),
 ('Projektteamet og specialisterne',
  'Samle HVAC, VVS, el og øvrige fag om de tekniske grænseflader. Jeg tager ansvar for koordineringen '
  'og det aftalte tekniske bidrag. Selvstændig VVS-dimensionering og projektering kræver en særskilt '
  'kompetenceafklaring.'),
 ('Entreprenører og øvrige interessenter',
  'Afklare udførelse, adgang og leverancer, så forskellige planer ikke spænder ben for hinanden. '
  'Ændringer skal tilbage til det gældende projektgrundlag og godkendes efter projektets aftalte '
  'proces.'),
 ('Drift og brugere',
  'Inddrage dem tidligt om adgang, afbrydelser og vedligehold. Følge de aftalte hensyn gennem '
  'projektering og udførelse og sikre, at overdragelsen omfatter det grundlag, driften faktisk skal '
  'bruge.')]

FIRST90 = [('Første uge',
  'Aftale et konkret projekt og min tekniske opgavefordeling med Jan Urhammer. Møde kunden og '
  'projektteamet, gennemgå leverance og økonomi samt besigtige de eksisterende installationer med '
  'fagpersoner. Afklare behov for specialiststøtte i HVAC/VVS. Samle de vigtigste åbne spørgsmål med '
  'ansvar og næste handling.'),
 ('Inden dag 30',
  'Afklare kundens behov, eksisterende grundlag og driftsbegrænsninger. Aftale omfang, leverancer, '
  'fagkontrol, budget og tidsplan. Gennemgå løsningsmuligheder med specialisterne og kunden. Få '
  'beslutningspunkter, tekniske grænseflader og eventuelle driftsstop ind i projektets fælles plan.'),
 ('Inden dag 60',
  'Føre den aftalte projektfase videre med teamet. Følge tekniske afklaringer og fagkontrol til dørs '
  'samt holde kunden orienteret om økonomi, ændringer og næste beslutning. Afstemme planlagt udførelse '
  'med drift og brugere. Afprøve en konkret forbedring af opfølgningen, hvis teamet oplever gentagne '
  'blokeringer.'),
 ('Inden dag 90',
  'Gennemgå fremdrift, økonomi og leverancer med kunde og leder. Bekræfte, at næste fase har de '
  'nødvendige tekniske afklaringer og kundebeslutninger. Følge op på test-/afleveringsplanen og '
  'dokumentationskrav. Samle erfaringer med teamet og aftale videre ansvar og faglig udvikling ud fra '
  'de konkrete opgaver.')]

KEYWORDS = ('Teknisk projektledelse · HVAC · Ventilation og klima · Projektøkonomi · Kundedialog · Tilbud og '
 'aftalegrundlag · Tværfaglig koordinering · Fremdrift og ændringer · Vedligehold · Kvalitetssikring og '
 'aflevering · FAT/SAT · PDCA og A3 · Python og Claude API.')


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
    m.models_table("FØRSTE 90 DAGE — BYGNING, KUNDE OG PROJEKT",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SAMARBEJDET I HVERDAGEN")
    for label, body in PARTNER:
        m.bullet(label, body, after=30)

    m.section("FRA EKSISTERENDE INSTALLATION TIL AFLEVERING")
    m.para('En renoveringsløsning skal prøves mod de eksisterende forhold, før den bliver til en udførelsesplan. Jeg vil med kunden og fagpersonerne afklare, hvilket grundlag vi kan stole på, og hvad der kræver besigtigelse eller yderligere undersøgelse. Derefter skal løsningsmulighederne holdes op mod adgang, plads, drift og vedligehold samt kundens økonomi. Fagspecialisterne skal sikre beregninger og tekniske valg inden for det aftalte ansvar. Hvis arbejdet kræver afbrydelser, skal rækkefølge, ansvar og kommunikation med brugerne være på plads. Ved ændringer skal både projektgrundlag, pris og tid følge med. Før aflevering skal de aftalte test, åbne punkter og driftsdokumenter gennemgås med kunden, så overdragelsen er mere end en færdigmelding.', after=80)

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
    build(os.path.join(ROOT, "Shahram_Ajloo_Sweco_TekniskProjektlederHVACVVS.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_Sweco_TekniskProjektlederHVACVVS.docx"))
