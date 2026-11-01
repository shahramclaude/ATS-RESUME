# -*- coding: utf-8 -*-
"""Sweco: teknisk projektleder HVAC/VVS. Dansk, opgave-først, genbrugt masterdesign."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Teknisk projektleder — HVAC og VVS | Sweco | Renovering & Installationer'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = 'Sweco · Eksisterende Byggeri og Specialer · Att. Jan Urhammer'
SUBJECT = 'Ansøgning: Teknisk projektleder til HVAC og VVS, København'

# ------------------------------------------------------------------ side 1
INTRO = ['En installation kan være korrekt dimensioneret og stadig være den forkerte løsning, hvis den '
 'ikke kan etableres, mens bygningen er i brug, eller vedligeholdes af dem, der overtager den. '
 'Opgaven hos Sweco er derfor ikke blot at udskifte HVAC og VVS. Det er at forbinde kundens behov, '
 'bygningens faktiske forhold, projektøkonomien og den fremtidige drift i én beslutning, kunden '
 'kan stå på mål for.',
 'Til den opgave er arbejdsmodellen klar: registrering før løsningsvalg, et kort beslutningsoplæg '
 'med alternativer, en faseopdelt leveranceplan, et økonomi- og ændringsspor og en driftsaftalt '
 'udførelsesplan. Nedenfor er sammenhængen fra første afklaring til dokumenteret aflevering — '
 'bygget på erfaring med installationer, projekter og drift, ikke kun på en tidsplan.']

BULLETS = [('Kravet: udvikle og vurdere HVAC- og VVS-løsninger',
  'Løsningen begynder med registrering af kapacitet, tilstand, føringsveje, indregulering og '
  'styring sammen med driftspersonalet. To eller tre løsningsmuligheder vurderes på indeklima, '
  'energi, investering, vedligehold og udførelsesrisiko. Ukendte forhold markeres som '
  'forudsætninger, der skal undersøges — ikke som skjulte reserver hos entreprenøren.'),
 ('Kravet: lede projektteamet på tværs af fagdiscipliner',
  'Løsningen er en leverancematrix med fagansvarlig, grænseflade, review og dato pr. leverance. Et '
  'ugentligt koordineringsmøde behandler beslutninger og blokeringer frem for statusoplæsning. '
  'Erfaringen omfatter koordinering af 25 specialister og 11 samtidige installationsprojekter med '
  'et 14-personers team.'),
 ('Kravet: styre projektøkonomi, fremdrift og ændringer',
  'Løsningen er en faseopdelt budgetbaseline med forbrug, restprognose og aftalt leverance. '
  'Ændringsloggen viser årsag, konsekvens for honorar og tid, beslutningstager og godkendelse, før '
  'ekstraarbejdet sættes i gang. P&L-ansvar fra egen virksomhed og økonomiopfølgning på '
  'CAPEX-projekter er det praktiske fundament.'),
 ('Kravet: være kundens kontaktperson og rådgive om prioriteringer',
  'Løsningen er ét beslutningsoplæg: behov, muligheder, konsekvens for drift og økonomi, '
  'anbefaling og næste skridt. Kunden skal kunne vælge uden at være installationsspecialist. '
  'Aftaler føres i en beslutningslog, og åbne spørgsmål får en ejer og en svarfrist.'),
 ('Kravet: udarbejde tilbud og afklare omfang, kontrakt og aftalegrundlag',
  'Løsningen er en tydelig ydelsesbeskrivelse med leverancer, afgrænsninger, kundens oplysninger, '
  'milepæle, honorar og ændringsprocedure. Swecos kontraktskabeloner og godkendelsesgange bruges '
  'som ramme. Tilbudsberegning og entrepriseaftaler fra egen virksomhed giver forståelse for, hvad '
  'en uklar formulering koster.'),
 ('Kravet: samarbejde med entreprenører og øvrige interessenter',
  'Løsningen er et interessent- og snitfladekort med kunde, brugere, drift, rådgivere og '
  'entreprenører. Grænseflader afklares før udførelse, og tekniske afvigelser behandles med '
  'dokumentation, ansvar og næste beslutning. Samarbejdet skal give plads til specialisternes '
  'viden uden at sprede projektansvaret.'),
 ('Kravet: planlægge med hensyn til drift, brugere og vedligehold',
  'Løsningen er en etapeplan med adgang, støj, støv, midlertidig forsyning, nedlukningsvinduer, '
  'sikker isolering og en tilbagerulningsmulighed. Driftsherren godkender forløbet, og '
  'afleveringen omfatter funktionsafprøvning, dokumentation og instruktion. Erfaring med '
  '24/7-anlæg og GMP-projekter gør driftskonsekvensen konkret.'),
 ('Kravet: fastholde kunderelationen og udvikle afdelingens ydelser',
  'Løsningen er opfølgning efter aflevering: virker anlægget som aftalt, er driften oplært, og '
  'hvilke behov går igen? Gentagne behov omsættes til et afgrænset ydelsesforslag, som afprøves '
  'med kollegerne. Nye opgaver skal udspringe af kundeværdi, ikke af mersalg uden et teknisk '
  'behov.')]

SYSTEM = ('Arbejdsmodellen samler registrering, løsningsvalg, økonomi, udførelse og aflevering i et fælles '
 'projektgrundlag. Python og Claude bruges professionelt til beregningsmodeller, tilbudsstruktur, '
 'tjeklister og beslutningsoplæg; input, tekniske antagelser og resultater efterprøves af den '
 'ansvarlige fagperson. Værktøjerne frigør tid til kunden og de tekniske valg — de overtager ikke '
 'rådgiveransvaret.')

MIRROR = ('Fagligt fundament: elautoriseret maskinmester (LV/MV/HV), B.Tech i teknologiledelse og '
 'maskinteknik, køleteknik og klimaanlæg samt erfaring med ventilation, installationer, '
 'commissioning og kritisk drift. 37 samtidige CAPEX-projekter på 2–10 mio. kr., 25 specialister '
 'og aflevering uden kritiske fund er dokumenteret erfaring med leverance, kvalitet og tværgående '
 'koordinering.')

HONEST = ('Afgrænsningen er vigtig: baggrunden er udførelse, idriftsættelse og drift, ikke mange år i en '
 'rådgivende projekteringsafdeling. Dyb VVS-specialprojektering, Swecos beregningsværktøjer og '
 'interne kontraktpraksis påstås ikke allerede behersket. Den praktiske systemforståelse bringes '
 'ind i løsningsarbejdet; specialberegninger og projektering kvalitetssikres med de rette '
 'fagkolleger.')

CULTURE = ('Swecos opgavebeskrivelse lægger vægt på frihed under ansvar, respekt, hjælpsomhed og sparring '
 'mellem specialister. Det omsættes her til tydeligt leveranceansvar og tidlige faglige reviews, '
 'ikke sololøsninger. At afdelingen arbejder for blandt andre Novo Nordisk giver en relevant '
 'fælles referenceramme: en installation er først god, når den virker for dem, der skal bruge og '
 'drive den.')

PRACTICAL = ('Bosat i Måløv, kørekort B, dansk på modersmålsniveau og professionelt engelsk. Arbejdssted '
 'København. Tiltrædelse og rammerne for den eksisterende virksomhed afklares før ansættelse.')

CLOSING = ('En første samtale kan tage udgangspunkt i en konkret renoveringsopgave: Hvilke forhold skal '
 'registreres, før løsningen vælges, og hvordan holdes drift, økonomi og kundens beslutninger '
 'samlet?')

# ------------------------------------------------------------------ CV
PROFILE = ('Teknisk renovering i bygninger i drift kræver, at løsningsvalg, projektøkonomi, kundedialog og '
 'udførelse hænger sammen. Relevant erfaring omfatter 11 samtidige ventilations- og klimaprojekter '
 'fra specifikation til aflevering, 37 CAPEX-projekter i reguleret produktion og kritisk el- og '
 'mekanisk drift på 24/7-anlæg. Elautoriseret maskinmester (LV/MV/HV) med B.Tech i '
 'teknologiledelse og maskinteknik; erfaring med fuldt P&L, tilbud, underentreprenører, '
 'dokumentation og tværfaglig teamledelse. Professionel Claude-bruger og koder: Python/Claude '
 'API-værktøjer til beregning, planlægning, kvalitetssikring og KPI-opfølgning. Styrken er at '
 'forbinde installationens tekniske funktion med driftens faktiske behov.')

PRACTICE = [('Tekniske valg med driften som kriterium',
  'Anvendelse i rollen: registrere eksisterende installationer, opstille alternativer og vurdere '
  'indeklima, energi, adgang, vedligehold og levetidsøkonomi. Forudsætninger og specialistbehov '
  'synliggøres før beslutning.'),
 ('Projektteam og faglige snitflader',
  'Erfaring: ledelse af 25 specialister på tværs af engineering, indkøb og anlæg samt 14-personers '
  'projektteam. Anvendelse: leverancematrix, faglige reviews og aftalte snitflader til el, '
  'automatik og bygning.'),
 ('Projektøkonomi og aftaler',
  'Erfaring: fuldt P&L, tilbudsberegning, planlægning og underentreprenører i egen virksomhed; '
  'CAPEX-opfølgning i SAP. Anvendelse: honorarbudget, restprognose, ændringslog og '
  'kundegodkendelse.'),
 ('Kundens beslutninger og kundesamarbejder',
  'Anvendelse: møder med et klart beslutningsbehov, korte oplæg med konsekvenser, opfølgning på '
  'aftaler og tydelig eskalering. Teknisk formidling på dansk og engelsk til kunde, håndværkere og '
  'drift.'),
 ('Udførelse og aflevering i drift',
  'Erfaring: pumper, HVAC, højspænding og SCADA i 24/7-drift; FAT/SAT og IQ/OQ/PQ i GMP-miljø. '
  'Anvendelse: etapeplan, arbejdstilladelser, funktionsafprøvning og driftsklar dokumentation.'),
 ('Digitale værktøjer og forbedringer',
  'Excel, SAP, Power BI, Python og Claude API til tilbud, planlægning og KPI. Dokumenteret '
  'produktivitetsløft over 40 % med egne AI-værktøjer; tekniske beregninger gennemgår faglig '
  'kontrol.')]

MODELS = [('Tekniske installationer og løsningsvalg',
  'Anlægskort med tilstand, kapacitet, målegrundlag og manglende oplysninger; alternativmatrix med '
  'anlægspris, energi, vedligehold og driftsrisiko.'),
 ('Leverance og team',
  'Faseplan og leverancematrix: ansvarlig, input, review og afleveringsdato; snitfladeregister og '
  'ugentlig blokeringstavle.'),
 ('Økonomi og ændringer',
  'Budgetbaseline, forbrug og restprognose pr. fase; ændringslog med konsekvens, godkendelse og '
  'opdateret aftalegrundlag.'),
 ('Kunde og interessenter',
  'Beslutningsoplæg på én side, beslutningslog, interessentkort og aftalt møderytme; opfølgning på '
  'beslutninger med ejer og dato.'),
 ('Drift og udførelse',
  'Etapeplan, nedlukningsvinduer, midlertidige forsyninger, arbejdsmiljø, brugerinformation og '
  'tilbagerulning; driftsherrens accept før indgreb.'),
 ('Kvalitet og aflevering',
  'Faglige reviews, kontrolplan, funktionsafprøvning, mangelliste med lukningsbevis, '
  'driftsdokumentation og instruktion af brugere og drift.')]

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

PRACTICAL_CV = ('Bosat i Måløv (Ballerup Kommune); kørekort B. København er det angivne arbejdssted. Dansk på '
 'modersmålsniveau og professionelt engelsk. Tiltrædelse og rammerne for den eksisterende '
 'virksomhed aftales før ansættelse.')

REFERENCES = 'Tidligere ledere hos Novo Nordisk A/S og Biofos (Lynetten) — oplyses ved henvendelse.'

PARTNER = [('Kunden og ejendommens brugere',
  'Behov, prioriteringer og beslutninger formuleres forståeligt. Brugerne får tidlig besked om '
  'indgreb, adgang og driftsforstyrrelser; beslutningsloggen fastholder aftalerne.'),
 ('Projektteam og specialister',
  'Faglige bidrag aftales med ansvar, tid og review. Specialister inddrages, før løsningen låses; '
  'uenigheder omsættes til dokumenterede alternativer.'),
 ('Entreprenører og leverandører',
  'Omfang, grænseflader, udførelsesrækkefølge og kontrol er tydelige før opstart. Afvigelser '
  'behandles i ændringssporet og ikke som mundtlige aftaler på pladsen.'),
 ('Driftsorganisationen',
  'Driftens viden bruges i registrering og løsningsvalg. Etaper, serviceadgang, indregulering, '
  'instruktion og dokumentation planlægges, så anlægget kan drives efter aflevering.')]

FIRST90 = [('Dage 1–30',
  'Lær Swecos projektmodel, kontraktskabeloner, økonomiopfølgning og faglige kontrol at kende. '
  'Følg en eksisterende opgave med teamchef og fagkolleger. Gennemfør registrering med kunden og '
  'driftspersonalet på en afgrænset opgave.'),
 ('Dage 31–60',
  'Overtag aftalt projektansvar. Få omfang, budget, leverancer, fagansvarlige og '
  'beslutningspunkter på plads. Udarbejd et løsningsoplæg med driftskonsekvenser og gennemfør '
  'fagligt review før kundens valg.'),
 ('Dage 61–90',
  'Gennemfør første fulde opfølgningscyklus med økonomiprognose, ændringslog og kundedialog. Aftal '
  'udførelsesetaper og kontrol med drift og entreprenør. Afleveringskrav er skrevet ind, før '
  'arbejdet udføres.'),
 ('Måned 3–6',
  'Følg løsningen gennem udførelse eller næste aftalte fase. Saml erfaringer fra kunde og drift, '
  'og foreslå én konkret forbedring af afdelingens rådgivningsydelser med kollegernes faglige '
  'input.')]

KEYWORDS = ('Teknisk projektleder · HVAC · VVS · Eksisterende byggeri · Renovering · Installationer · '
 'Projektteam · Fagdiscipliner · Samlet leverance · Projektøkonomi · Fremdrift · Ændringer · '
 'Kundedialog · Kundens behov · Kontaktperson · Rådgivning · Tilbud · Omfang · Kontrakt · '
 'Aftalegrundlag · Entreprenører · Interessenter · Drift · Brugere · Vedligehold · Tekniske valg · '
 'Installationstekniske projekter · Projektledelse · Faglighed · Samarbejde · Videndeling')


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

    m.models_table("PROJEKTETS STYRING — FRA REGISTRERING TIL AFLEVERING",
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
    m.models_table("FØRSTE 90 DAGE — FAGLIGHED, KUNDE OG LEVERANCE",
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
    out = os.path.join(ROOT, "Shahram_Ajloo_Sweco_TekniskProjektleder_HVACVVS.docx")
    build(out)
    print("OK " + out)
