# -*- coding: utf-8 -*-
"""Novo Nordisk 346099: HRT Pak vedligehold. Dansk, samlet dokument i masterdesign."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Vedligeholdsansvarlig | HRT Pak, Måløv | Forebyggende vedligehold og stabil produktion'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = 'Novo Nordisk · Global Manufacturing & Supply · HRT Pak, Måløv'
SUBJECT = 'Motivation og bidrag: Vedligeholdsansvarlig — job-ID 346099'

# ------------------------------------------------------------------ side 1
INTRO = ['Vedligehold i HRT Pak skal flyttes fra at genoprette driften efter en fejl til at forebygge den '
 'næste — uden at den daglige produktion mister førsteprioriteten. På fem samlelinjer og tre '
 'pakkelinjer er det afgørende, at håndværkernes erfaringer bliver til bedre jobplaner, troværdige '
 'arbejdsordrer og de rigtige reservedele. Flere planer giver ikke i sig selv mere stabil '
 'produktion; planer, der bliver opdateret efter det faktiske arbejde, gør.',
 'Den korte motivation er at omsætte erfaring fra kritisk drift og GMP-projekter til et '
 'vedligehold, der kan lære af sig selv. Bidraget er en sammenhængende arbejdsmodel for '
 'planrevision, SAP-datakvalitet, reservedelsstruktur og verificerede forbedringer. Den '
 'koordinerende rolle skal gøre det lettere for håndværkere og produktion at lykkes — ikke indføre '
 'et parallelt administrationssystem.']

BULLETS = [('Kravet: opdatere vedligeholdelsesplaner med håndværkernes erfaringer',
  'Løsningen er et fast feedback-loop: arbejdsordre afsluttes med fejl, årsag, handling og '
  'forslag; væsentlige fund gennemgås med håndværkeren; jobplan, interval eller reservedelsbehov '
  'revideres efter godkendelse. Planændringen får ejer og dato, og effekten følges på gentagne '
  'fejl og driftsforstyrrelser.'),
 ('Kravet: forbedre tilbagemeldinger og teknisk struktur i SAP PM',
  'Løsningen er en fælles minimumsstandard for tilbagemeldinger: korrekt teknisk objekt, '
  'fejlbeskrivelse, årsag, udført arbejde, tid og dele. Et stikprøvetjek giver konkret feedback '
  'til teamet. Udstyrshierarki, navngivning og jobplaner gennemgås med dem, der bruger strukturen, '
  'så en fejl registreres på det anlæg, den tilhører.'),
 ('Kravet: drive implementeringen af SAP MM og reservedelsstrukturen',
  'Løsningen er en afgrænset implementeringsplan med procesejere, datakrav, oprydning, test og '
  'brugeroplæring. Reservedele kobles til udstyr med entydige materialedata og ansvar for '
  'vedligeholdelse. Genbestilling og lagerbehov aftales med indkøb og lager; en pilot afprøves før '
  'udrulning i godkendt system.'),
 ('Kravet: som procesejer bevare linjernes validerede stand',
  'Løsningen er at vurdere ændringer sammen med kvalitet, produktion og teknik, før de '
  'gennemføres. Dokumentation, ændringsstyring, relevante tests og godkendelser skal følge '
  'indgrebet. GMP-erfaring med FAT/SAT og IQ/OQ/PQ fra Novo Nordisk er fundamentet; HRT Paks '
  'konkrete procesansvar og procedurer skal læres lokalt.'),
 ('Kravet: systematisk problemløsning med varig effekt',
  'Løsningen er A3, 5xHvorfor og Ishikawa på gentagne fejl: afgræns problemet med data, undersøg '
  'årsagen med håndværkerne, aftal korrigerende handling og verificér effekten. En sag er ikke '
  'lukket, fordi opgaven er udført, men når kontrollen viser, at årsagen er håndteret og '
  'standarden opdateret.'),
 ('Kravet: analyser af nyt udstyr, RCM, FMEA og FMECA',
  'Løsningen er en risikogennemgang med funktion, fejlmåde, konsekvens, sandsynlighed og '
  'detektion. RCM bruges som beslutningsramme for valg mellem tidsbaseret, tilstandsbaseret eller '
  'anden vedligeholdsindsats. Nyt udstyr vurderes også på adgang, reservedele, dokumentation, '
  'kompetencer og vedligeholdsbehov før overdragelse.'),
 ('Kravet: ABC-analyser, reservedelsstrategier og skemalægning',
  'Løsningen er at kombinere ABC-analyser af forbrug og værdi med driftskritikalitet og '
  'leveringstid — en billig del kan stoppe en hel linje. Arbejder klargøres med dele, kompetencer '
  'og varighed og lægges i aftalte produktionsvinduer. Udførelse og evaluering kobles til næste '
  'planrevision.'),
 ('Kravet: bindeled og hurtige beslutninger uden kvalitetskompromis',
  'Løsningen er én prioriteringsrytme med håndværkere, supportfunktioner, projektledere og '
  'produktion: sikkerhed og kvalitet først, derefter driftskonsekvens og næste handling. '
  'Uafklarede forhold eskaleres med ejer og frist; fremdrift må ikke købes ved at springe '
  'godkendelser eller samarbejdet over.')]

SYSTEM = ('Værktøjerne er et planrevisionsregister, en SAP-datakvalitetstjekliste, en reservedels- og '
 'kritikalitetsmatrix samt en forbedringstavle med PDCA-opfølgning. Som professionel Claude-bruger '
 'og koder bygger jeg Python-værktøjer til analyse, tjeklister og rapportering. Hos Novo skal data '
 'og AI-brug følge godkendte IT- og kvalitetsregler; ingen fortrolige produktionsdata i eksterne '
 'AI-tjenester uden godkendelse, og ingen automatiske ændringer af validerede systemer.')

MIRROR = ('Relevant fundament: elautoriseret maskinmester (LV/MV/HV), B.Tech i teknologiledelse og '
 'maskinteknik, forebyggende vedligehold og reservedelsflow i 24/7-drift samt SAP-erfaring med '
 'økonomi, aktiver og omkostninger. Tidligere Novo-arbejde med 37 CAPEX-projekter, 25 specialister '
 'og aflevering uden kritiske afvigelser giver praktisk GMP-erfaring og tværgående koordinering.')

HONEST = ('Afgrænsning: SAP ERP-erfaring er dokumenteret, men selvstændig SAP PM-konfiguration, en '
 'gennemført SAP MM-implementering og formelt ejerskab af HRT-pakkelinjer er ikke. RCM/FMEA/FMECA '
 'beskrives som den foreslåede analyseramme, ikke som certificeringer eller gennemførte '
 'referenceprojekter. Onboarding skal derfor afklare modulkompetencer og etablere samarbejdet med '
 'SAP-specialister og lokale procesejere.')

CULTURE = ('Novo Nordisk Way forbinder kvalitet uden kompromis med et sundt og engagerende arbejdsmiljø. I '
 'HRT Pak betyder det, at håndværkernes viden bruges aktivt, at afvigelser gøres synlige, og at '
 'forebyggende arbejde bliver enkelt at udføre korrekt. Stabile leverancer af HRT-tabletter er '
 'forbindelsen mellem vedligeholdelsesplanen og patienterne.')

PRACTICAL = ('Bosat i Måløv — samme by som arbejdsstedet. Dansk på modersmålsniveau og professionelt engelsk; '
 'kørekort B. Tiltrædelse og rammerne for den eksisterende virksomhed afklares før ansættelse.')

CLOSING = ('En første drøftelse kan begynde med én tilbagevendende linjefejl: Hvad fortæller '
 'arbejdsordrerne, hvad ved håndværkerne, og hvilken planændring forebygger næste stop?')

# ------------------------------------------------------------------ CV
PROFILE = ('Stabil produktion i HRT Pak kræver, at vedligeholdsplaner, SAP-data og reservedelsstruktur '
 'afspejler arbejdet på linjerne. Erfaringen omfatter kritisk el- og mekanisk drift hos Biofos, '
 'forebyggende vedligehold og reservedelsflow, GMP-idriftsættelse hos Novo Nordisk samt '
 'planlægning og kvalitetssikring i egen virksomhed. Elautoriseret maskinmester (LV/MV/HV), B.Tech '
 'i teknologiledelse og maskinteknik, med tværfaglig koordinering og praktisk SAP ERP-erfaring. '
 'A3, 5xHvorfor, Ishikawa, PDCA, 5S og Standard Work er metoderne til struktur og varige '
 'forbedringer. Professionel Claude-bruger og koder med Python/Claude API-værktøjer til '
 'planlægning, kvalitetssikring og KPI. Rollen søges for at forbinde håndværkernes erfaringer med '
 'forebyggende vedligehold, ikke for personaleansvar.')

PRACTICE = [('Vedligeholdsplaner og feedback',
  'Erfaring: forebyggende vedligehold, Standard Work og PDCA i 24/7-drift. Foreslået anvendelse: '
  'feedback fra afsluttede arbejdsordrer gennemgås med håndværkeren og omsættes til kontrollerede '
  'planrevisioner.'),
 ('SAP PM og datakvalitet',
  'Dokumenteret SAP-erfaring vedrører ERP, økonomi, aktiver og omkostninger. Foreslået PM-praksis: '
  'teknisk objektstruktur, ensartede jobplaner, fejl/årsag/handling og stikprøver på '
  'tilbagemeldinger. Moduldybde afklares lokalt.'),
 ('SAP MM og reservedele',
  'Erfaring: reservedelsflow og lagerstyring. Foreslået implementeringsbidrag: datakvalitet, '
  'udstyrskobling, dubletoprydning, brugertest og oplæring sammen med SAP-, indkøbs- og '
  'lagerspecialister.'),
 ('Valideret stand og GMP',
  'Erfaring: FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA, teknisk dokumentation og nul kritiske '
  'afvigelser ved aflevering. Vedligeholdsændringer vurderes i sitets godkendte '
  'kvalitetsprocesser.'),
 ('Problemløsning og kritikalitet',
  'A3, 5xHvorfor, Ishikawa og PDCA anvendes til at forbinde årsag, handling og effekt. Foreslået '
  'RCM/FMEA/FMECA-gennemgang hjælper med prioritering; ABC suppleres med driftskonsekvens og '
  'leveringstid.'),
 ('Koordinering og digitale værktøjer',
  'Erfaring med 25 specialister og 14-personers installationsteam. Leveranceansvar, korte '
  'tavlemøder og synlige blokeringer; Python/Claude-værktøjer til planlægning og KPI under '
  'godkendt datahåndtering.')]

MODELS = [('Planrevision',
  'Arbejdsordre → håndværkerfeedback → årsagsvurdering → godkendt ændring af jobplan/interval → '
  'effektkontrol. Ingen planrevision uden ansvar og begrundelse.'),
 ('SAP PM-kvalitet',
  'Teknisk objekt, fejl, årsag, handling, tidsforbrug og materialer; stikprøver og feedback, '
  'fælles navngivning og kontrolleret ændring af den tekniske struktur.'),
 ('SAP MM og reservedelsdata',
  'Proces- og dataansvar, materialestamdata, udstyrskobling, dubletkontrol, test og oplæring; '
  'pilot før udrulning med SAP-specialister.'),
 ('Risiko og reservedele',
  'RCM/FMEA/FMECA som foreslået analyseramme; ABC-analyser koblet til driftskritikalitet, '
  'leveringstid og alternativer. Lagerbinding vurderes sammen med stoprisiko.'),
 ('Planlagt udførelse',
  'Klargjorte arbejdsordrer, dele, kompetencer og varighed før skemalægning; aftalt '
  'produktionsvindue, sikker udførelse og evaluering til næste planrunde.'),
 ('Kvalitet og forbedring',
  'Ændringsvurdering og relevante tests for valideret stand; A3/PDCA med korrigerende handling, '
  'ejer, frist og verificeret effekt. Gentagne fejl og planopfyldelse følges.')]

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
  [('Installation, kvalitet og sikkerhed',
    'El-tekniske opgaver for erhvervskunder: installation, tavler, styring, fejlfinding og '
    'forebyggende vedligehold på el-, ventilations- og klimaanlæg. LOTO, APV og risikovurdering; '
    'nul kritiske afvigelser i serviceaftalerne.'),
   ('Faglig ledelse og værktøjer',
    'Daglig planlægning og oplæring af 5 elektrikere og 3 lærlinge; KS og '
    'afleveringsdokumentation. Python/Claude API til tilbud, tidsplaner, tjeklister og KPI; over '
    '40 % produktivitetsløft.')]),
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

CERTS = [('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023'),
 ('Køleteknik & klimaanlæg (AMU)', 'Mercantec · 2021'),
 ('Lean og forbedringspraksis — 5S, PDCA, VSM, A3, Kaizen', 'Anvendt i drift og projekter'),
 ('STCW — maskinrumsvagt og maritime sikkerhedscertifikater', 'Søfartsstyrelsen · 2021–2023')]

LANGUAGES = ("Dansk (modersmål, skrift og tale) · Engelsk (professionelt, skrift og tale) · "
             "Persisk/farsi · Kørekort B (kategori B)")

PRACTICAL_CV = ('Bopæl og arbejdssted i Måløv. Dansk på modersmålsniveau og professionelt engelsk; kørekort B. '
 'Tiltrædelse og rammerne for den eksisterende virksomhed aftales før ansættelse. Fokus er '
 'administrativt og koordinerende vedligehold tæt på håndværkere og produktion.')

REFERENCES = 'Tidligere ledere hos Novo Nordisk A/S og Biofos (Lynetten) — oplyses ved henvendelse.'

PARTNER = [('Håndværkere og teknikere',
  'Fejlbeskrivelser og forbedringsforslag skal være nemme at aflevere. Feedback drøftes direkte og '
  'omsættes til planændringer med synlig tilbagemelding om, hvad der er besluttet.'),
 ('Produktion',
  'Den daglige drift er førsteprioritet. Vedligeholdsarbejde klargøres og aftales i realistiske '
  'produktionsvinduer; sikkerhed og kvalitet er faste betingelser, også når prioriteringer '
  'ændres.'),
 ('Supportfunktioner og SAP-specialister',
  'Materialedata, teknisk struktur og ændringsgodkendelser har tydelige ejere. '
  'PM/MM-implementering gennemføres med kompetent støtte og test, ikke som et uformelt '
  'regnearksprojekt.'),
 ('Projektledere og kvalitet',
  'Nyt udstyr vurderes på vedligehold, reservedele, dokumentation og kompetencer før overdragelse. '
  'Procesansvar og valideret stand afklares i godkendte procedurer.')]

FIRST90 = [('Dage 1–30',
  'Lær fem samlelinjer og tre pakkelinjer at kende sammen med håndværkere og produktion. Gennemgå '
  'vedligeholdsstrategi, valideringsgrænser og SAP PM/MM-arbejdsgange. Aftal baseline for '
  'datakvalitet, gentagne fejl og planopfyldelse.'),
 ('Dage 31–60',
  'Afprøv feedback-loop og minimumsstandard for arbejdsordrer på en afgrænset linje. Gennemgå '
  'teknisk struktur og kritiske reservedele; aftal MM-proces, dataansvar og pilot med '
  'SAP-specialister. Prioritér én tilbagevendende fejl til A3.'),
 ('Dage 61–90',
  'Gennemfør første godkendte planrevision og kontrollér effekten. Afprøv materialedata og '
  'arbejdsgange i aftalt testmiljø, oplær brugere og luk fund før udrulning. Rapportér '
  'dokumenterede resultater og åbne risici, ikke lovede besparelser.'),
 ('Måned 3–6',
  'Udbred de afprøvede standarder til flere linjer efter godkendelse. Følg gentagne fejl, '
  'ordretilbagemeldinger, reservedelsmangler og planopfyldelse; brug evalueringen til næste '
  'prioritering af forebyggende arbejde.')]

KEYWORDS = ('Vedligeholdsansvarlig · HRT Pak · HRT-tabletter · Forebyggende vedligehold · '
 'Vedligeholdelsesplaner · Arbejdsordrer · Tilbagemeldinger · Teknisk struktur · SAP PM · SAP MM · '
 'Reservedelsstruktur · Procesejer · Validerede stand · Kapacitetsudnyttelse · Systematisk '
 'problemløsning · Korrigerende handlinger · Nyt udstyr · Reservedelsstrategier · ABC-analyser · '
 'Skemalægning · Udførelse · Evaluering · RCM · FMECA · FMEA · Håndværkere · Supportfunktioner · '
 'Projektledere · Produktion · Kvalitet · Arbejdsmiljø · Samarbejde · GMP')


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

    m.models_table("VEDLIGEHOLDETS STYRING — PLANER, SAP OG FORBEDRINGER",
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
    m.models_table("FØRSTE 90 DAGE — OVERBLIK, KONTROL OG FORBEDRINGER",
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
    out = os.path.join(ROOT, "Shahram_Ajloo_NovoNordisk_Vedligeholdsansvarlig_HRTPak.docx")
    build(out)
    print("OK " + out)
