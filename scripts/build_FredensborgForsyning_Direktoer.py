# -*- coding: utf-8 -*-
"""
Fredensborg Forsyning — Direktør.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Direktør | Forsyningssektor, kritisk infrastruktur og grøn omstilling | Hovedstaden"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = ("Fredensborg Forsyning A/S · Højvangen 23, 3480 Fredensborg · "
             "att. bestyrelsesformand Lars Jørgen Simonsen")
SUBJECT = "Ansøgning: Direktør for Fredensborg Forsyning"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Fredensborg Forsyning står med tre beslutninger, der rækker årtier frem: et nyt fælles "
    "vandressourcecenter med Novafos, der erstatter tre anlæg og står færdigt omkring 2036; en "
    "klimatilpasning, der kan tage 70-100 år, og som allerede er i gang i Nivå, Humlebæk, Kokkedal "
    "og dele af Fredensborg by; og et investeringsniveau, der mærkes på taksten — 65 kr. pr. m³ i "
    "2025. Direktørens opgave er ikke at vælge ét af dem, men at holde dem sammen i én plan, der kan "
    "forklares for borgerne og forsvares i bestyrelsen.",

    "Nedenfor er min motivation og ledelsesmæssige tilgang samt det system, der står klar fra første "
    "dag: bestyrelsesårshjul, beslutningsoplæg på én side, porteføljestyring af anlæg og "
    "klimaprojekter, krisestab og en månedlig ledelsesrapport på få tal.",
]

BULLETS = [
    ("Kravet: gennemføre den fælles vandressourcecenter Øresund-løsning med Novafos",
     "Løsningen er at styre det som et program: faseporte frem mod 2036, skrevne grænseflader til "
     "Novafos om økonomi, risiko og beslutningsret og en tilkoblingsplan pr. anlæg, så drift og "
     "myndighedskrav holdes hele vejen. Jeg har ledet leverancer med mange samtidige afhængigheder."),

    ("Kravet: klimatilpasning for hyppigere skybrud og stigende grundvand",
     "Løsningen er en prioriteret klimahandlingsplan pr. by med konsekvens og pris: hvor vandet gør "
     "skade først, hvad drift og ledningsfornyelse kan klare, og hvad der kræver anlæg — koordineret "
     "med kommunens planer, så gaden kun graves op én gang."),

    ("Kravet: beskytte drikkevandet efter hændelserne i 2025 og 2026",
     "Løsningen er at gøre beredskabet operationelt: kildesporing og prøveprogram som fast "
     "driftsdata, en krisestab med roller og mødekadence og en kommunikationsplan skrevet før "
     "hændelsen. Jeg har stået i 24/7-drift i fem år og arbejdet under GMP-krav, hvor afvigelser "
     "skulle lukkes."),

    ("Kravet: balancere et stort investeringsbehov med rimelige takster",
     "Løsningen er en investeringsplan med levetid, konsekvens og alternativ pr. sag, hvor "
     "finansiering og takstkonsekvens er regnet med — så bestyrelsen vælger mellem oplyste "
     "alternativer frem for at få én regning. Jeg har haft fuldt P&L og bygget prognoser selv."),

    ("Kravet: skærpede miljø- og klimakrav til rensning og egne anlæg",
     "Løsningen er at tage kvarternær rensning og energioptimering ind som designkrav fra start i "
     "vandressourcecenteret og samtidig måle eget forbrug og lattergas på de anlæg, der kører videre. "
     "Jeg har arbejdet med køl, varmegenvinding og energiledelse i drift."),

    ("Kravet: affald, sortering og cirkulær økonomi under nye producentansvarsregler",
     "Løsningen er at måle sorteringskvalitet og omkostning pr. ordning, gøre ordningerne enkle for "
     "borgeren og bruge data til at flytte genanvendelsen. Affaldsområdet vil jeg lære af "
     "medarbejderne og af tallene."),

    ("Kravet: kritisk infrastruktur, beredskab og cybersikkerhed",
     "Løsningen er en beredskabsplan med scenarier, roller og øvelser i kalenderen — strømsvigt, "
     "ekstremvejr, forurening og cyber — og et IT-samarbejde med tydelig ansvarsdeling. Jeg er "
     "uddannet i arbejdsmiljø og sikkerhed og har drevet et anlæg, der ikke kunne vente."),

    ("Kravet: mange samtidige anlægsprojekter med entreprenører, godkendelser og borgerdialog",
     "Løsningen er én projektportefølje med status, næste beslutning og risiko, fast møde med "
     "kommunen om gravetilladelser og trafik og borgerdialog planlagt pr. projekt — ikke først når "
     "graven er åben. Jeg har koordineret 37 anlægsprojekter uden kritiske fund."),

    ("Kravet: bestyrelsesbetjening, ejerkommune og en attraktiv arbejdsplads",
     "Løsningen er et bestyrelsesårshjul med faste temaer, beslutningsoplæg på én side med to "
     "alternativer og en anbefaling, kvartalsvis dialog med ejerkommunen inden for ejerstrategien og "
     "kodekset for god selskabsledelse — og en ledergruppe med udviklingsaftaler og arbejdsmiljø som "
     "fast punkt."),
]

SYSTEM = (
    "Systemet står klar fra dag ét: bestyrelsesårshjul, beslutningsoplæg på én side, "
    "projektportefølje med milepæle og risiko, krisestab med roller og øvelser samt månedlig "
    "ledelsesrapport på få tal — ført i Excel og Power BI sammen med økonomi- og driftssystemerne, "
    "med oplæg genereret i Python og Claude, så ledelse og bestyrelse ser samme tal."
)

MIRROR = (
    "Om kravene: 20 år i tekniske anlæg og otte år med personaleansvar, heraf fem år som drifts- og "
    "vedligeholdelseschef i et kommunalt ejet selskab med bestyrelse, 24/7-drift, budget i SAP og "
    "myndighedstilsyn — og to år som teknisk direktør med fuldt P&L. Elautoriseret maskinmester "
    "(LV/MV/HV), B.Tech."
)

HONEST = (
    "Det skal siges ligeud: jeg har ikke været direktør for et forsyningsselskab med "
    "bestyrelsesreference før, jeg har ikke arbejdet med vanddistribution og affald i drift, og jeg "
    "har ikke prøvet en fusion eller et fælles selskab som vandressourcecenteret. Spildevandssiden "
    "kender jeg fra fem år på Lynetten. Det, jeg bringer, er driftsforståelse, økonomi og "
    "ledelseshåndværk — og jeg vil bruge de første måneder på at lære af dem, der har stået i det."
)

CULTURE = (
    "Selskabet er kommunalt ejet, kundefinansieret og en arbejdsplads med medarbejderindflydelse — en "
    "bestyrelse med byråd, forbrugere og medarbejdere kræver, at man kan tale til alle tre "
    "perspektiver med samme tal. Jeg kommer med gummistøvlerne på først: fem år i drift har lært mig, "
    "at tillid skabes ved at være der, når det gør ondt."
)

PRACTICAL = (
    "Bosat i Måløv — cirka 30 minutter i bil til Højvangen 23. Kørekort B og bil, dansk på "
    "modersmålsniveau og engelsk professionelt. Kan tiltræde efter aftale og deltager gerne i "
    "testforløb (NEO-PI-3 og IST-2000R) og referencetagning."
)

CLOSING = (
    "I første samtale vil jeg gerne tale om, hvilke tre beslutninger der skal træffes i det første "
    "år — og hvordan vi undgår, at beslutningen om fremtidens spildevand bliver udskudt endnu en gang."
)

# ------------------------------------------------------------------ CV
PROFILE = (
    "Direktør- og driftschefprofil med 20 år i tekniske anlæg og otte år med personaleansvar: fem år "
    "som drifts- og vedligeholdelseschef i et kommunalt ejet selskab med bestyrelse, "
    "myndighedstilsyn og 24/7-drift, to år som teknisk direktør med fuldt P&L og to år som "
    "projektleder/commissioning på 37 samtidige anlægsprojekter. Arbejder med investeringsplaner, "
    "leverandørstyring, beredskab og dataunderstøttet ledelse. Elautoriseret maskinmester (LV/MV/HV), "
    "B.Tech og Lean."
)

PRACTICE = [
    ("Strategi og bestyrelse",
     "Bestyrelsesårshjul, beslutningsoplæg på én side med to alternativer og en anbefaling, "
     "kvartalsdialog med ejerkommunen og rapportering efter kodekset for god selskabsledelse."),
    ("Investeringer og takster",
     "Flerårig investeringsplan med levetid, konsekvens og alternativ pr. sag; finansiering og "
     "takstkonsekvens regnet med, og månedlig prognose med fuldt ansvar i SAP."),
    ("Drift og kritisk infrastruktur",
     "Planlagt vedligehold, tilstandskontrol og KPI'er; nul uplanlagte stop i fem år på et "
     "24/7-anlæg — beredskabsplaner med roller og øvelser i kalenderen."),
    ("Projekter og eksterne parter",
     "Projektportefølje med milepæle og risiko, entreprenører og myndighedsgodkendelser, "
     "borgerdialog planlagt pr. projekt og aflevering uden kritiske fund (37 anlægsprojekter)."),
    ("Organisation og rekruttering",
     "Bygget en virksomhed op fra bunden: rekruttering, oplæringsplaner, arbejdsmiljø (§16), "
     "ledelsesaftaler og kompetenceudvikling."),
    ("Data og digitalisering",
     "Måling før system: forbrug, nedbrud og svartider som månedstal, dashboards og AI-genererede "
     "ledelsesoplæg; selvkodet i Python og Claude i daglig brug."),
]

MODELS = [
    ("Bestyrelsesårshjul",
     "Fast kadence for strategi, investeringer, økonomi, risiko og bæredygtighed — med hvilke "
     "beslutninger der skal træffes hvornår"),
    ("Beslutningsoplæg",
     "Én side: situation, konsekvens, to alternativer og en anbefaling; beslutningslog med ejer og "
     "frist"),
    ("Portefølje",
     "Alle anlægs- og klimaprojekter i ét overblik med fase, næste beslutning, økonomi og risiko; "
     "gennemgang hver måned med ledergruppen"),
    ("Beredskab",
     "Scenarier (strømsvigt, ekstremvejr, forurening, cyber) med roller, mødekadence og øvelser — "
     "nærved-hændelser følgt til lukning"),
    ("Økonomi og takster",
     "Investeringsplan, prognose og takstberegning i samme model, så konsekvensen af en beslutning "
     "kan ses med det samme; rapporter genereret i Python og Claude"),
    ("Ejerkommune",
     "Kvartalsvis dialog og en skreven forventningsafstemning inden for ejerstrategien; væsentlige "
     "beslutninger drøftet med ejeren, før de er endelige"),
]

ACHIEVEMENTS = [
    ("Nul uplanlagte stop i fem år",
     "24/7-renseanlæg med SCADA, højspænding og koblingsanlæg — planlagt vedligehold, "
     "tilstandskontrol og KPI'er i SAP, og en driftsorganisation der holdt, også under sygdom."),
    ("Fuldt P&L i egen virksomhed",
     "5 elektrikere og 3 lærlinge, 40+ serviceanlæg: rekruttering, økonomi, leverandøraftaler og "
     "ansvar for bundlinjen — fra opstart til drift."),
    ("37 anlægsprojekter uden kritiske fund",
     "2-10 mio. kr. hos Novo Nordisk med 25 specialister koordineret på tværs af mekanik, el, proces "
     "og indkøb; FAT/SAT og dokumentation der bestod revision."),
    ("14-mands team med 11 samtidige opgaver",
     "kapacitetsplanlægning, daglige tavlemøder og tydelig prioritering i eksisterende byggeri med "
     "drift og brugere omkring os."),
]

EXPERIENCE = [
    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 spildevandsanlæg · pumper, HVAC, køl, koblingsanlæg og højspænding · budget i SAP",
     [("Drift, vedligehold og driftssikkerhed",
       "planlagt vedligehold, tilstandskontrol og KPI'er i SAP; nul uplanlagte stop i fem år på et "
       "anlæg, hvor spildevandet ikke kan vente — i en kommunalt ejet virksomhed med bestyrelse."),
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

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2-10 mio. kr.)",
     [("Personale, kapacitet og fremdrift",
       "14-personers team med kapacitetsplanlægning, daglige tavlemøder og opfølgning på den enkelte "
       "— og 11 samtidige entrepriser i eksisterende byggeri med brugere omkring os.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2-10 mio. kr. · 25 specialister · GMP/FDA/EMA",
     [("Koordinering, snitflader og aflevering",
       "25 specialister koordineret på tværs af mekanik, el, proces og indkøb; fremdrift og "
       "rapportering til styregruppe; FAT/SAT, IQ/OQ/PQ og aflevering uden kritiske fund.")]),

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

PRACTICAL_CV = ("Bosat i Måløv — cirka 30 minutter i bil til Højvangen 23, 3480 Fredensborg; "
                "kørekort kategori B og bil. Dansk på modersmålsniveau og engelsk professionelt. Kan "
                "tiltræde efter aftale.")

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Biofos (Lynetten), Novo Nordisk A/S, "
              "Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Bestyrelsen",
     "Et årshjul og beslutningsoplæg, der gør det muligt at træffe de langsigtede beslutninger med "
     "åbne øjne — og loyal gennemførelse bagefter."),
    ("Medarbejdere og ledere",
     "En ledergruppe med udviklingsaftaler, faste møder og en direktør, der kommer ud på anlæggene — "
     "og som tager de svære sager selv."),
    ("Fredensborg Kommune",
     "Kvartalsvis dialog og skreven forventningsafstemning inden for ejerstrategien; væsentlige "
     "beslutninger drøftet med ejeren, før de er endelige."),
    ("Borgere, forbrugere og myndigheder",
     "Åben kommunikation under hændelser, borgerdialog før gravearbejdet og tal, der kan forklares — "
     "også når svaret er, at noget tager længere tid."),
]

FIRST90 = [
    ("Dage 1–30",
     "Mødt alle medarbejdere og været på hver anlægstype; gennemgået bestyrelsens beslutninger, "
     "vandressourcecenterprogrammet, beredskabsplanerne og ejerstrategien."),
    ("Dage 30–60",
     "Én samlet portefølje af anlægs- og klimaprojekter med næste beslutning og risiko; "
     "investerings- og takstmodel opdateret; dialog med kommunen om gravetilladelser og trafik."),
    ("Dage 60–90",
     "Første udkast til strategi og investeringsplan fremlagt for bestyrelsen; kriseøvelse "
     "gennemført; prøveprogram og kildesporing gennemgået med henblik på robusthed."),
    ("Måned 3–6",
     "Program for vandressourcecenteret med faseporte og grænseflader til Novafos på plads; "
     "klimatilpasning prioriteret pr. by; affaldsordningerne gennemgået på kvalitet og omkostning."),
    ("Måned 6–12",
     "Selskabet styrer efter få tal: driftssikkerhed, vandtab, sorteringskvalitet, økonomi og "
     "takstudvikling — og bestyrelsen har et beslutningsgrundlag, den kan stå inde for over for "
     "byrådet."
    ),
]

KEYWORDS = (
    "Direktør · Fredensborg Forsyning · Multiforsyningsselskab · Drikkevand · Spildevand · Affald · "
    "Vandforsyning · Spildevandsrensning · Affaldsindsamling · Fredensborg Kommune · "
    "Samfundskritiske opgaver · Aktieselskab · 100% ejet · Bestyrelsen · Daglige drift · Økonomien · "
    "Borgernes tillid · Klimatilpasning · Fremtidige spildevandsstruktur · Ledelseserfaring · "
    "Strategisk niveau · Ledelse af ledere · Komplekse tekniske driftsorganisationer · "
    "Forsyningssektoren · Forretningsforståelse · Grøn omstilling · Strategisk og retningssættende "
    "leder · Autoritet · Relationelle kompetencer · Vandressourcecenter Øresund · Novafos · "
    "Renseanlæg · Vandressourcecenter · Kloak · Pumpestationer · Separatkloakering · "
    "Regnvandsbassiner · Nivå · Humlebæk · Kokkedal · Fredensborg by · Grundvand · Pesticider · "
    "Vandledninger · Vandtab · Ledningsbrud · Kogeanbefalinger · Investeringsbehov · Takster · "
    "Forsyningssikkerhed · Miljøkrav · Udledninger · Bæredygtighed · Affaldssortering · "
    "Cirkulær økonomi · Genanvendelse · Producentansvar · Kritisk infrastruktur · Beredskab · "
    "Cybersikkerhed · Strømsvigt · Ekstremvejr · Forurening · Cyberangreb · Anlægsarbejder · "
    "Entreprenører · Myndighedsgodkendelser · Borgerdialog · Bestyrelsesbetjening · "
    "Beslutningsgrundlag · Arbejdsplads · Arbejdsmiljø og sikkerhed · Kompetenceudvikling · "
    "Ejerkommunen · Ejerstrategi · Kodeks for god selskabsledelse i kommunale forsyningsselskaber · "
    "Kundeservice · Anlægsprojekter · Årsregnskabsloven · Koncern · Holdingselskab · Serviceselskab · "
    "Forbrugervalgte · Medarbejderrepræsentanter · Driftsmedarbejdere · Teknikere · Ingeniører · "
    "Projektledere · Administration · Interessenter · Konsolidering · Partnerskaber · Fusioner · "
    "Maskinmester · Lean · SAP"
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

    m.models_table("SELSKABETS STYRING — ANVENDT I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER SELSKABET I STYRING",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN LEDES SELSKABET — DE FIRE PARTER")
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
    build(os.path.join(ROOT, "Shahram_Ajloo_FredensborgForsyning_Direktoer.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_FredensborgForsyning_Direktoer.docx"))
