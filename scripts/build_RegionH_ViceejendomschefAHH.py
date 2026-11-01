# -*- coding: utf-8 -*-
"""
Region Hovedstaden — Viceejendomschef, Drift og Byg AHH (Amager og Hvidovre Hospital).
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Viceejendomschef | Teknisk drift og ledelse af fagledere | Hovedstaden"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = ("Region Hovedstaden · Center for Ejendomme, Drift og Byg AHH · "
             "att. ejendomschef Lars Nyman · via Dansk HR Service, Christopher Sunddahl")
SUBJECT = "Ansøgning: Viceejendomschef til Drift og Byg på Amager og Hvidovre Hospital"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Drift og Byg AHH skal holde to hospitaler i fuld drift, vedligeholde bygningerne og gennemføre "
    "projekter — samtidig. Viceejendomschefens opgave er ikke at kende den tekniske løsning, men at "
    "sørge for, at de rigtige mennesker er involveret, at prioriteringen er skrevet ned, og at der "
    "bliver fulgt op — det er den rolle, jeg har stået i.",

    "Nedenfor er min motivation og ledelsesmæssige tilgang samt det system, der står klar fra første "
    "dag: fast faglederkadence med beslutningslog, en prioriteringsnøgle for hvad der går foran, en "
    "snitflademodel mellem drift og projekter og en månedlig status på økonomi, ressourcer og risiko.",
]

BULLETS = [
    ("Kravet: daglig ledelse af faglederne og supportområdet",
     "Løsningen er kadence og klarhed: faste en-til-en-samtaler med hver fagleder, et fagledermøde "
     "med beslutningslog og en skreven forventningsaftale om, hvad der er deres område, og hvad der "
     "løftes fælles. Jeg har ledet 14-mands team og 5 elektrikere med 3 lærlinge — erfarne fagfolk "
     "skal ikke styres, de skal have rammer."),

    ("Kravet: være ejendomschefens nærmeste sparringspartner og stedfortræder",
     "Løsningen er at dele ledelsesopgaven op på forhånd: hvad jeg tager, når jeg er i spidsen, "
     "hvilke sager der altid går til ejendomschefen, og hvordan vi holder hinanden orienteret. Jeg "
     "har været teknisk direktør med fuldt ansvar."),

    ("Kravet: skabe klare prioriteringer og sikre, at beslutninger og aftaler bliver omsat til handling",
     "Løsningen er en prioriteringsnøgle, der er skrevet ned og kendt: patientsikkerhed og "
     "driftsstabilitet først, derefter myndighedskrav og tidskritiske projekter — og en beslutningslog "
     "med ejer og frist, gennemgået hver uge. Jeg har ført beslutningslog i både 24/7- og "
     "GMP-regulerede miljøer."),

    ("Kravet: holde sammen på snitfladerne mellem drift, projekter og hospitalets behov",
     "Løsningen er en snitflademodel pr. projekt: hvem ejer hvad i grænsefladen, hvad kræver et "
     "afbrud, og hvordan aftales det med den kliniske afdeling — i god tid og skriftligt. Jeg har "
     "koordineret 37 anlægsprojekter i byggeri, der var i drift imens."),

    ("Kravet: følge udviklingen i økonomi, ressourcer og risici og handle, når noget kræver det",
     "Løsningen er en fast månedlig status på få tal med prognose og risikoliste — og en aftale om, "
     "hvornår en afvigelse skal eskaleres. Jeg har haft budget i SAP med fuldt ansvar og bygget "
     "prognoser selv."),

    ("Kravet: skabe følgeskab blandt erfarne fagpersoner uden selv at være den, der ved mest",
     "Løsningen er at spørge fagligt ind i stedet for at svare: hvad er konsekvensen, hvad er "
     "alternativet, hvad ville du gøre — og så beslutte. Fem år som driftschef på et 24/7-anlæg har "
     "lært mig, at dygtige teknikere følger en leder, der står ved beslutningen."),

    ("Kravet: teknisk forståelse for komplekse bygninger og installationer, hvor stabil drift er "
     "afgørende",
     "Løsningen er 20 år i tekniske anlæg: el og højspænding, VVS og HVAC, køl, CTS/SCADA, pumper og "
     "koblingsanlæg — elautoriseret maskinmester (LV/MV/HV) og B.Tech. Jeg ved, hvad et nedbrud "
     "betyder, og hvad der skal til for at forebygge det."),

    ("Kravet: navigere i en hverdag uden én enkel løsning — ro og dømmekraft",
     "Løsningen er at skelne mellem det, der skal besluttes nu, og det der skal undersøges først, og "
     "at sige det højt, når noget ikke kan løses i dag. Jeg har stået i akutte situationer, hvor "
     "beslutningen skulle tages med det samme."),

    ("Kravet: bidrage til udvikling af arbejdsgange, styring og overblik på længere sigt",
     "Løsningen er at gøre det i små, prøvede skridt: én arbejdsgang ad gangen, med en navngiven ejer "
     "og en gevinstmåling — og kun meldt ud som standard, når den er prøvet på en rigtig bygning. Jeg "
     "har indført standardarbejde og Lean i drift og produktion."),
]

SYSTEM = (
    "Systemet står klar fra dag ét: faglederkadence med beslutningslog, prioriteringsnøgle, "
    "snitflademodel mellem drift og projekter, månedlig status på økonomi, ressourcer og risiko samt "
    "et årshjul for vedligehold og projekter — ført i Excel og Power BI sammen med Center for "
    "Ejendommes systemer, med oplæg genereret i Python og Claude."
)

MIRROR = (
    "Om kravene: elautoriseret maskinmester (LV/MV/HV) og B.Tech, 20 år i tekniske anlæg og otte år "
    "med personaleansvar — fem år som drifts- og vedligeholdelseschef i Biofos med budget i SAP og "
    "24/7-drift, to år som teknisk direktør med fuldt P&L, 14-mands team med 11 samtidige opgaver og "
    "25 specialister koordineret på tværs af fag."
)

HONEST = (
    "Det skal siges ligeud: jeg har ikke ledet fagledere i en hospitalsorganisation og ikke prøvet en "
    "regionspolitisk styret organisation med så mange snitflader mod kliniske afdelinger. Til gengæld "
    "har jeg fem år i et kommunalt ejet selskab med bestyrelse og myndighedstilsyn — og prøvet at "
    "drive teknik videre, mens byggeriet kørte omkring mig."
)

CULTURE = (
    "Center for Ejendomme hedder fra 1. januar 2027 Ejendomme og Byggerier, når Region Hovedstaden og "
    "Region Sjælland lægges sammen — og AHH overtager samtidig driften af 138 sundheds- og "
    "omsorgspladser. Ny organisation og nye kvadratmeter oven i den daglige drift. Det er præcis der, "
    "en viceejendomschef gør en forskel ved at holde fast i kadence, prioritering og overblik."
)

PRACTICAL = (
    "Bosat i Måløv — cirka 25 minutter i bil til Hvidovre Hospital og 30 minutter til Amager "
    "Hospital. Kørekort B og bil, dansk på modersmålsniveau og engelsk professionelt. Kan tiltræde "
    "hurtigst muligt eller efter aftale."
)

CLOSING = (
    "I første samtale vil jeg gerne tale om, hvordan prioriteringen mellem drift og projekter bliver "
    "skrevet ned i dag — og hvad der skal være anderledes den 1. januar, når organisationen skifter navn."
)

# ------------------------------------------------------------------ CV
PROFILE = (
    "Teknisk leder med 20 år i anlæg og drift og otte år med personaleansvar: fem år som drifts- og "
    "vedligeholdelseschef i Biofos med budget i SAP, myndighedstilsyn og 24/7-drift, to år som teknisk "
    "direktør med fuldt P&L og to år som projektleder på 37 samtidige anlægsprojekter i eksisterende "
    "byggeri. Arbejder med prioriteringsmodeller, beslutningslog og månedlig status på økonomi og "
    "risiko. Elautoriseret maskinmester (LV/MV/HV), B.Tech."
)

PRACTICE = [
    ("Ledelse af fagledere og specialister",
     "En-til-en med forventningsaftale, fagledermøde med beslutningslog, tydelige roller og "
     "beslutningsret; rekruttering, oplæring og kompetenceudvikling."),
    ("Prioritering og opfølgning",
     "Skreven prioriteringsnøgle, beslutningslog med ejer og frist og ugentlig gennemgang — så "
     "aftaler bliver til handling i stedet for til referat."),
    ("Snitflader mellem drift og projekter",
     "Snitflademodel pr. projekt: hvem ejer grænsefladen, hvad kræver et afbrud, og hvordan aftales "
     "det med brugerne i tide; 37 anlægsprojekter uden kritiske fund."),
    ("Økonomi, ressourcer og risiko",
     "Budget, prognose og økonomiopfølgning i SAP med fuldt ansvar; månedlig status på få tal med "
     "risikoliste og aftalte eskaleringsgrænser."),
    ("Teknisk drift og vedligehold",
     "Tilstands- og kritikalitetsbaseret vedligehold; el, HVAC, køl, CTS/SCADA, højspænding og "
     "koblingsanlæg — nul uplanlagte stop i fem år."),
    ("Udvikling af arbejdsgange",
     "Én arbejdsgang ad gangen med navngiven ejer, prøvekørsel på en rigtig bygning og "
     "gevinstmåling; standardarbejde og Lean fra drift og produktion."),
]

MODELS = [
    ("Faglederkadence",
     "Fast en-til-en med forventningsaftale og et fagledermøde med beslutningslog — dagsorden "
     "starter med sikkerhed, drift og projekter i den rækkefølge"),
    ("Prioriteringsnøgle",
     "Skrevet ned og kendt: patientsikkerhed og driftsstabilitet, derefter myndighedskrav og "
     "tidskritiske projekter — bruges når hensyn trækker i hver sin retning"),
    ("Snitflademodel",
     "Pr. projekt: grænsefladeejer, afbrudsplan, varsling til klinikken og aftalt dokumentation ved "
     "overlevering"),
    ("Økonomi og risiko",
     "Månedlig status på få tal med prognose og risikoliste; aftalte eskaleringsgrænser, så "
     "afvigelser bliver set tidligt"),
    ("Stedfortrædelse",
     "Aftalt på forhånd: hvilke sager der altid går til ejendomschefen, og hvordan orienteringen "
     "fungerer, når jeg træder ind"),
    ("Opfølgning",
     "Ugentlig gennemgang af beslutningslog og projekter; rapporter og oplæg genereret i Python og "
     "Claude"),
]

ACHIEVEMENTS = [
    ("Nul uplanlagte stop i fem år",
     "24/7-renseanlæg med SCADA, højspænding og koblingsanlæg — planlagt vedligehold, "
     "tilstandskontrol og KPI'er i SAP, og en driftsorganisation der holdt, også under sygdom."),
    ("37 anlægsprojekter uden kritiske fund",
     "2-10 mio. kr. hos Novo Nordisk med 25 specialister koordineret på tværs af mekanik, el, proces "
     "og indkøb — i byggeri der var i drift imens; FAT/SAT og dokumentation der bestod revision."),
    ("14-mands team med 11 samtidige opgaver",
     "kapacitetsplanlægning, daglige tavlemøder og tydelig prioritering i eksisterende byggeri med "
     "drift og brugere omkring os."),
    ("Fuldt P&L i egen virksomhed",
     "5 elektrikere og 3 lærlinge, 40+ serviceanlæg: rekruttering, økonomi, leverandøraftaler og "
     "ansvar for bundlinjen."),
]

EXPERIENCE = [
    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7-anlæg · pumper, HVAC, køl, CTS/SCADA, koblingsanlæg og højspænding · budget i SAP",
     [("Drift, vedligehold og driftssikkerhed",
       "planlagt vedligehold, tilstandskontrol og KPI'er i SAP; nul uplanlagte stop i fem år på et "
       "anlæg, hvor driften ikke kunne vente — i et kommunalt ejet selskab med bestyrelse."),
      ("Sikkerhed, leverandører og beredskab",
       "koordinering af egne teknikere, entreprenører og rådgivere — LOTO, arbejdstilladelser, "
       "garantisager og nærved-hændelser fulgt til lukning.")]),

    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og leverandøraftaler",
     [("Organisation, rekruttering og arbejdsmiljø",
       "byggede virksomheden op fra bunden: rekruttering, oplæringsplaner og arbejdsplaner, "
       "sikkerhed og arbejdsmiljø som fast punkt."),
      ("Økonomi og kunder",
       "tilbudsberegning, indkøb og leverandøraftaler, plan og prognose med fuldt ansvar for "
       "bundlinjen.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2-10 mio. kr. · 25 specialister · GMP/FDA/EMA",
     [("Koordinering, snitflader og aflevering",
       "25 specialister koordineret på tværs af mekanik, el, proces og indkøb; fremdrift og "
       "rapportering til styregruppe; FAT/SAT, IQ/OQ/PQ og aflevering uden kritiske fund.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2-10 mio. kr.)",
     [("Personale, kapacitet og fremdrift",
       "14-personers team med kapacitetsplanlægning, daglige tavlemøder og opfølgning på den enkelte "
       "— og 11 samtidige entrepriser i eksisterende byggeri med brugere omkring os.")]),

    ("Elektromekaniker / Produktionsteamleder",
     "ARJ Engineering · Teheran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · skiftplanlægning, materialestyring og lager",
     [("Fremstilling og teknisk problemløsning",
       "skiftplanlægning, materialestyring og målopfølgning; reparation og diagnosticering gennem "
       "struktureret root cause-analyse.")]),
]

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
     "Anvendt i drift, produktion og projekter · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og projekter · 2017 – nu"),
]

LANGUAGES = ("Dansk (modersmål, skrift og tale) · Engelsk (professionelt, skrift og tale) · "
             "Persisk/farsi · Kørekort B (kategori B)")

PRACTICAL_CV = ("Bosat i Måløv — cirka 25 minutter i bil til Hvidovre Hospital og 30 minutter til "
                "Amager Hospital; kørekort kategori B og bil. Dansk på modersmålsniveau og engelsk "
                "professionelt. Kan tiltræde hurtigst muligt eller efter aftale.")

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Biofos (Lynetten), Novo Nordisk A/S, "
              "Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Faglederne og supportområdet",
     "Fast kadence, forventningsaftale og en leder, der giver plads til fagligheden — og som tager "
     "beslutningen, når den skal tages."),
    ("Ejendomschefen",
     "Aftalt stedfortrædelse, fælles prioritering og en sparringspartner, der siger sin mening "
     "tydeligt og gennemfører beslutningen loyalt."),
    ("Hospitalets kliniske afdelinger",
     "Afbrud og arbejde i drift varslet i god tid og aftalt skriftligt, så behandlingen ikke bliver "
     "overrasket over et gravearbejde eller en lukket elevator."),
    ("Projekter, leverandører og Center for Ejendomme",
     "Snitflademodel pr. projekt, leverandøropfølgning på KPI og ét fælles overblik — også når "
     "organisationen skifter navn til Ejendomme og Byggerier den 1. januar."),
]

FIRST90 = [
    ("Dage 1–30",
     "Mødt alle fagledere og supportområdet, været på begge hospitaler og gennemgået de væsentligste "
     "projekter med ejendomschefen: hvad er lovet, hvad er i gang, og hvor er risikoen."),
    ("Dage 30–60",
     "Prioriteringsnøgle og beslutningslog indført; snitflademodel pr. projekt aftalt med "
     "projektlederne; månedlig status på økonomi, ressourcer og risiko på plads."),
    ("Dage 60–90",
     "Kadence og forventningsaftaler med alle fagledere gennemført; eskaleringsgrænser aftalt; "
     "stedfortrædelsesaftalen med ejendomschefen prøvet i praksis."),
    ("Måned 3–6",
     "Overgangen til Ejendomme og Byggerier og de nye sundheds- og omsorgspladser håndteret uden "
     "at driften mærker det; første arbejdsgangsforbedring prøvekørt og målt."),
    ("Måned 6–12",
     "Driften leverer stabilt, projekterne har styr på snitfladerne, og overblikket findes på ét "
     "sted — så ejendomschefen og hospitalet kan træffe beslutninger uden at vente på en indberetning.",
    ),
]

KEYWORDS = (
    "Viceejendomschef · Drift og Byg · Drift og Byg AHH · Amager og Hvidovre Hospital · Hvidovre · "
    "Center for Ejendomme · Region Hovedstaden · Teknisk kompleks hospitalsdrift · Ejendomschef · "
    "Ledelsesmæssig sparringspartner · Stedfortræder · Dagligt ledelsesansvar · Fagledere · "
    "Supportområdet · Teknisk drift · Projekter · Hospitalets behov · Snitflader · Skabe retning · "
    "Fagligheder · Skabe overblik · Følgeskab · Erfarne fagpersoner · Fælles retning · "
    "Klare prioriteringer · Beslutninger og aftaler · Omsat til handling · "
    "Drift, projekter og hospitalets behov · Økonomi, ressourcer og risici · Arbejdsgange · "
    "Styring · Samlende ledelse · Personaleledelse · Tillid · Dømmekraft · Ejendomsdrift · "
    "Forsyning · Industri · Hospital · Driftsintensiv organisation · Tekniske anlæg · Installationer · "
    "Stabil drift · Bygninger · Vedligeholdelse · Matrikler · To millioner kvadratmeter · "
    "Patientbehandling · Dansk HR Service · QuickApply · Jobindex · Maskinmester · Lean · SAP"
)


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

    m.models_table("DRIFT OG BYG — STYRING I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER DRIFT OG BYG I RYTMEN",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN LEDES OMRÅDET — DE FIRE PARTER")
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
    build(os.path.join(ROOT, "Shahram_Ajloo_RegionH_ViceejendomschefAHH.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_RegionH_ViceejendomschefAHH.docx"))
