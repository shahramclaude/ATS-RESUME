# -*- coding: utf-8 -*-
"""
ELCON — projektleder, større el-entrepriseprojekter, Fredericia.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Projektleder | ELCON Entreprise | Teknisk fremdrift, projektøkonomi og sikker aflevering'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = '2. november 2026'
RECIPIENT = 'ELCON · Entreprisedivisionen · Entreprisechef Brian Frost · Fredericia'
SUBJECT = 'Ansøgning: Projektleder til større el-entrepriseprojekter — Fredericia'

# ------------------------------------------------------------------ side 1
INTRO = ['Et el-entrepriseprojekt kommer sikkert i mål, når teknik, udførelse og økonomi styres som ét forløb. '
 'I Syddanmark og på Fyn skal projektlederen gøre aftaler og grænseflader tydelige, sikre et realistisk '
 'produktionsgrundlag og reagere på afvigelser, før de bliver til ventetid, omarbejde eller tab. '
 'Kontoret i Fredericia og byggepladsen skal dele samme billede af fremdrift, kvalitet og næste '
 'beslutning.',
 'Den foreslåede projektstruktur står klar til at blive tilpasset ELCONs arbejdsgange: en opstarts- og '
 'grænsefladeliste, en rullende udførelsesplan, et økonomi-/ændringsregister og en milepælsstyret KS- '
 'og afleveringsplan. Hver kritisk aktivitet får ejer, forudsætninger og beslutningsfrist. Styringen '
 'skal være let at bruge for de udførende og præcis nok til, at kunden og byggeledelsen kan handle på '
 'den.']

BULLETS = [('Etablere et klart teknisk og kommercielt grundlag',
  'Gennemgå aftalegrundlag, tegninger, leverancegrænser og åbne afklaringer med kunden, rådgivere og '
  'samarbejdspartnere. Aftal ansvar for projektering, koordinering og godkendelse. Registrér uafklarede '
  'forudsætninger med ejer og dato, før de sendes videre til udførelsen.'),
 ('Lede udførelsen tæt på byggepladsen',
  'Omsæt hovedtidsplanen til en rullende aktivitets- og bemandingsplan med materialer, adgang og '
  'forudgående arbejder som synlige forudsætninger. Korte tavlemøder og pladsrunder følger fremdrift, '
  'sikkerhed og blokeringer. Prioritér sammen med byggeledelsen og de udførende medarbejdere frem for '
  'kun at flytte datoer i planen.'),
 ('Holde projektøkonomien ajour',
  'Følg budget, disponerede omkostninger, faktisk forbrug og restbudget til færdiggørelse. Synliggør '
  'ændringer og ekstraarbejder med omfang, konsekvens, dokumentation og aftalt godkendelsesvej. Et '
  'forventet resultat skal afspejle de kendte risici og resterende opgaver, ikke blot de fakturaer der '
  'allerede er bogført.'),
 ('Sikre kvalitet og kontrolleret aflevering',
  'Læg KS, test og dokumentation ind i tidsplanen, så fejl opdages inden lukning af arbejder eller '
  'aflevering. Aftal acceptkriterier og ansvar for kontrol med de relevante fagpersoner. Følg mangler '
  'og åbne punkter til dokumenteret afslutning; en teknisk løsning er først færdig, når kunden har det '
  'aftalte afleveringsgrundlag.'),
 ('Skabe samarbejde og vedholdende problemløsning',
  'Vær en tilgængelig faglig sparringspartner for kunder, rådgivere, projektlederkolleger og '
  'specialister. Brug A3/5xHvorfor ved tilbagevendende fejl og korte beslutningsreferater ved '
  'ændringer. Ordentlighed er at melde konsekvenser tidligt og følge aftalen til dørs, også når svaret '
  'kræver en ny prioritering.')]

SYSTEM = ('Første uge afklares projektportefølje, mandat og vigtigste risici med entreprisechefen. Dag 30 '
 'foreligger et valideret projektgrundlag og en fælles økonomi-/fremdriftsbaseline for udvalgte '
 'projekter. Dag 60 er plan-, ændrings- og KS-rytmen afprøvet. Dag 90 vurderes prognosekvalitet, '
 'leveranceberedskab og åbne risici, før næste forbedringer prioriteres.')

MIRROR = ('Det dokumenterede grundlag er el-teknisk entreprise og projektledelse: ELOHVAC med tilbud/beregning, '
 'planlægning, materialer, underentreprenører, KS og aflevering samt fuldt P&L og ledelse af 5 '
 'elektrikere og 3 lærlinge. Ventek-Air: 11 samtidige projekter og 14 medarbejdere fra specifikation '
 'til formel aflevering. Novo Nordisk: 37 CAPEX-projekter på DKK 2–10 mio. pr. projekt og koordinering '
 'af 25 specialister.')

HONEST = ('Elautoriseret maskinmester (LV/MV/HV), B.Tech i Technology Management & Mechanical Engineering og '
 'praktisk erfaring med el-, ventilations- og klimaanlæg. Hos Novo blev FAT/SAT og IQ/OQ/PQ gennemført '
 'under GMP/FDA/EMA uden kritiske fund ved aflevering. Den erfaring understøtter disciplineret '
 'dokumentation; den er ikke en påstand om identiske projekt- eller kontraktkrav hos ELCON.')

CULTURE = ('ELCONs beskrevne ordentlighed, tillid, samarbejde og frihed under ansvar omsættes til klare aftaler, '
 'tidlig eskalering og aktiv brug af kollegers specialistviden. Oplæring og videndeling er dokumenteret '
 'gennem lærlingeledelse og 1:1/MUS. Professionel Claude-koder: Python/Claude API-værktøjer til tilbud, '
 'planlægning, KS og KPI gav over 40 % produktivitetsløft i entreprisedrift; brug hos ELCON forudsætter '
 'godkendte data og faglig kontrol.')

PRACTICAL = ('Bopæl er Måløv. Rollen kombinerer kontor i Fredericia og byggepladser i Syddanmark og på Fyn; en '
 'realistisk aftale om tilstedeværelse, base/ophold og rejser skal afklares. Flytning eller '
 'hjemmearbejde er ikke forudsat. Startdato og ordningen for ELOHVAC skal aftales; dansk og engelsk '
 'beherskes professionelt.')

CLOSING = ('En første samtale kan afklare de aktuelle projekter, projektlederens økonomi- og aftalemandat samt en '
 'holdbar løsning for daglig tilstedeværelse i projektområdet.')

# ------------------------------------------------------------------ CV
PROFILE = ('Opgaven er at gennemføre større el-entrepriseprojekter med teknisk kvalitet, sikker udførelse og sund '
 'økonomi. Fundamentet er elautoriseret maskinmester (LV/MV/HV), B.Tech og praktisk '
 'entreprise-/projektledelse fra tilbud og materialer til KS og aflevering. ELOHVAC: fuldt P&L, '
 'underentreprenører og 5 elektrikere/3 lærlinge. Ventek-Air: 11 samtidige projekter og 14 '
 'medarbejdere. Novo: 37 CAPEX-projekter, DKK 2–10 mio. hver, koordinering af 25 specialister og '
 'reguleret aflevering uden kritiske fund. Professionel Claude-koder med Python/Claude API-værktøjer og '
 '>40 % produktivitetsløft. ELCONs konkrete systemer, projektmandat og kontraktgrundlag afklares ved '
 'opstart.')

PRACTICE = [('El-entreprise fra tilbud til aflevering — dokumenteret praksis',
  'ELOHVAC: tilbud/beregning, planlægning, materialer og underentreprenører samt KS og '
  'afleveringsdokumentation på el-, ventilations- og klimaanlæg. Fuldt P&L og ansvar for kundens '
  'tekniske leverance.'),
 ('Projektøkonomi og risici — dokumenteret praksis',
  'Novo: fremdrift, økonomi, risici og ressourcer på 37 CAPEX-projekter med månedsrapportering til '
  'ledelse og bygherre; SAP til økonomi, aktiver og omkostninger. Foreslået ELCON-anvendelse: '
  'disponering, restbudget og ændringsopfølgning.'),
 ('Byggeplads og kapacitet — dokumenteret praksis',
  'Ventek-Air: specifikation til formel aflevering på 11 samtidige projekter, 14-personers team, '
  'kapacitetsstyring, tavlemøder og flaskehalsanalyse. Aftalegrundlag, underentreprenører og '
  'afleveringspakker.'),
 ('Tydelig ledelse og oplæring — dokumenteret praksis',
  '5 elektrikere og 3 lærlinge: daglig planlægning, 1:1/MUS, struktureret oplæring og situationsbestemt '
  'ledelse. Arbejdsmiljø, LOTO, APV og risikovurdering integreret i udførelsen.'),
 ('Kvalitet og tekniske grænseflader — dokumenteret praksis',
  'Novo: FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA; nul kritiske fund ved aflevering. Elsystemer, UPS og '
  'nødbelysning samt koordinering på tværs af engineering, indkøb og anlæg.'),
 ('Forbedring og digital støtte — dokumenteret praksis',
  'PDCA/A3/5xHvorfor, 5S og flaskehalsanalyse; Python/Claude API til beregning, tidsplaner, KS og KPI '
  'med >40 % produktivitetsløft. Nye projektværktøjer tilpasses ELCONs processer og godkendte '
  'datamiljø.')]

MODELS = [('Projektopstart',
  'Aftale-/tegningsgrundlag, grænseflader, risici og ansvar. RACI foreslås til uklare snitflader; '
  'konkret mandat aftales med entreprisechef.'),
 ('Udførelsesplan',
  'Rullende plan med bemanding, materialer, adgang og afhængigheder. Dokumenteret tavlemødepraksis gør '
  'blokeringer synlige.'),
 ('Økonomi og ændringer',
  'Budget, disponeret/faktisk forbrug, restbudget og prognose; ændringslog med omfang, konsekvens og '
  'godkendelsesstatus.'),
 ('KS og aflevering',
  'Kontrol-/testpunkter, dokumentejere, milepæle, mangelliste og acceptgrundlag; fagansvarlige '
  'godkender efter aftalt proces.'),
 ('Sikkerhed og læring',
  'Dokumenteret LOTO/APV/risikovurdering og PDCA/A3/5xHvorfor; effektkontrol på gentagne fejl.'),
 ('Faglig ledelse',
  'Dokumenterede 1:1/MUS og lærlingeoplæring; foreslået GROW/SBI-feedback, tydelig delegering og '
  'sparring med specialister.')]

ACHIEVEMENTS = [('37 samtidige CAPEX-projekter',
  'DKK 2–10 mio. pr. projekt; koordinering af 25 specialister og reguleret aflevering uden kritiske '
  'fund hos Novo Nordisk.'),
 ('11 projekter og 14 medarbejdere',
  'Ventek-Air: specifikation til aflevering, kapacitet og daglige tavlemøder.'),
 ('Fuldt P&L og direkte ledelse',
  'ELOHVAC: entrepriseansvar samt 5 elektrikere og 3 lærlinge med planlægning og oplæring.'),
 ('Over 40 % produktivitetsløft',
  'Egne Python/Claude API-værktøjer til beregning, planlægning, KS og KPI i entreprisedrift.')]

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

PRACTICAL_CV = ('Bopæl Måløv (Ballerup Kommune). Arbejdssted Fredericia med byggepladser i Syddanmark og på Fyn. En '
 'realistisk ordning for tilstedeværelse, base/ophold og rejser skal aftales; flytning, daglig pendling '
 'eller hjemmearbejde er ikke lovet. Startdato og ELOHVAC-overgang afklares før ansættelse. Dansk og '
 'persisk/farsi på modersmålsniveau, engelsk professionelt; kørekort B. Elautoriseret maskinmester '
 '(LV/MV/HV), ikke autoriseret elinstallatør. Firmabil er en mulighed i opslaget, ikke et aftalt '
 'vilkår. ELCONs systemer, projektportefølje og mandat skal afklares ved opstart.')

REFERENCES = 'Tidligere ledere hos Novo Nordisk og Biofos (Lynetten) — oplyses efter aftale.'

PARTNER = [('Entreprisechef og projektlederkolleger',
  'Afstem økonomi-, bemandings- og aftalemandat. Brug kollegial sparring ved risici og '
  'kapacitetskonflikter; eskalér med konsekvens og løsningsmuligheder, ikke kun en statusfarve.'),
 ('Kunder, rådgivere og byggeledelse',
  'Afklar teknik, grænseflader og ændringer tidligt. Saml beslutninger i korte referater med ansvar og '
  'dato; gør betydningen for pris, kvalitet og levering tydelig før udførelsen påvirkes.'),
 ('Udførende og samarbejdspartnere',
  'Omsæt planen til klare opgaver med materialer, adgang og korrekt grundlag. Lyt til praktiske '
  'hindringer på pladsen og følg op på sikkerhed, kvalitet og kapacitet; en ny dato løser ikke en '
  'manglende forudsætning.'),
 ('Specialister og dokumentansvarlige',
  'Inddrag relevante fagpersoner til teknisk vurdering, test og accept. Sammenhold udført løsning med '
  'dokumentation og godkendt revision; afleveringsberedskab opbygges gennem projektet, ikke i sidste '
  'uge.')]

FIRST90 = [('Første uge',
  'Entreprisechef og projektteam afklarer portefølje, mandat, kontaktveje og kritiske milepæle. Besøg '
  'relevante byggepladser; gennemgå aftalegrundlag, tegninger, risici og bemanding. Leverance: '
  'prioriteret opstartsliste med ejere og næste beslutninger.'),
 ('Dag 30',
  'Validér budget/disponering/restbudget, tidsplan og leverancegrænser for et aftalt projektudsnit. '
  'Afstem åbne afklaringer med kunder, rådgivere og byggeledelse. Leverance: '
  'økonomi-/fremdriftsbaseline, rullende udførelsesplan og KS-/afleveringsmilepæle.'),
 ('Dag 60',
  'Afprøv den samlede rytme for pladsopfølgning, økonomiprognose, ændringer og dokumentation. Følg ét '
  'teknisk problem fra afklaring til udført og kontrolleret løsning. Leverance: sporbar beslutning, '
  'opdateret plan/økonomi og synlige resterende risici.'),
 ('Dag 90',
  'Review prognoseafvigelser, åbne ændringer, forsinkede forudsætninger og KS-/afleveringsberedskab med '
  'entreprisechefen. Del læring med projektlederkolleger og specialister. Leverance: prioriteret '
  'forbedringsplan og aftalte ejere; mål fastlægges ud fra de faktiske projekter.')]

KEYWORDS = ('Projektleder · el-entreprise · el-teknisk baggrund · teknisk løsning · projektøkonomi · byggepladser '
 '· kunder · rådgivere · samarbejdspartnere · byggeledelse · udførende medarbejdere · fremdrift · '
 'kvalitet · koordinering · faglig sparring · videndeling · Fredericia · Syddanmark · Fyn. Konkrete '
 'systemer, projektstørrelser og aftale-/beslutningsmandat hos ELCON skal afklares; tidligere '
 'projektbudgetter angiver dokumenteret erfaring, ikke en antaget ELCON-portefølje.')


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

    m.models_table("PROJEKTSTYRING — OPSTART, UDFØRELSE OG AFLEVERING",
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
    m.models_table("FØRSTE 90 DAGE — PROJEKTGRUNDLAG, ØKONOMI OG FREMDRIFT",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SAMARBEJDE OG BESLUTNINGSANSVAR")
    for label, body in PARTNER:
        m.bullet(label, body, after=30)

    m.section("ÆNDRINGSKONTROL — TEKNIK, TID OG ØKONOMI")
    m.para("Følg en konkret projektændring fra den første afklaring til udførelse og dokumenteret afslutning. Beskriv ændret scope og grænseflader, aftal beslutningsvej og registrér godkendelsesstatus. Vurdér konsekvenser for materialer, bemanding, tidsplan, økonomi og KS; opdatér restbudget og forventet resultat, når ny viden foreligger. Skeln mellem en varslet konsekvens, et tilbud og en godkendt aftale efter det konkrete kontraktgrundlag. Kontrollér, at udførelsen bruger den rigtige revision, og at afleveringens dokumentation følger den faktiske løsning. En ændringslog skaber overblik, men giver ikke i sig selv ret til betaling eller udvidet mandat.", after=80)

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
    build(os.path.join(ROOT, "Shahram_Ajloo_ELCON_ProjektlederFredericia.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_ELCON_ProjektlederFredericia.docx"))
