# -*- coding: utf-8 -*-
"""
Newsec Danmark — Teamleder til Technical Management Services, Investeringsejendomme.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Teamleder | Technical Management Services | Teknisk drift og leverance"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = ("Newsec Danmark · Lyngby Hovedgade 4, 2800 Kongens Lyngby · "
             "att. Client Director Sofie Balslev-Olesen")
SUBJECT = "Ansøgning: Teamleder til Technical Management Services — Investeringsejendomme"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Newsecs internationale afdeling leverer teknisk drift til udenlandske investorer, hvor den "
    "enkelte kunde har sin egen portefølje, sine egne kontrakter og sin egen investeringsstrategi — "
    "domicilejendomme, hoteller, bolig og logistik. Opgaven som teamleder er derfor dobbelt: fælles "
    "processer og ensartet kvalitet på tværs, og en leverance pr. kunde, der kan læses ind i den "
    "strategi, kunden har købt ejendommene for.",

    "Nedenfor er min motivation og ledelsesmæssige tilgang samt det system, der står klar fra første "
    "dag: leverancemodel pr. kunde med KPI og kontraktkrav, fast lederkadence, økonomi- og "
    "driftsrapport på få tal og en leverandørplan med langsigtede aftaler.",
]

BULLETS = [
    ("Kravet: sætte den strategiske retning og lede og udvikle de ledere, der omsætter den",
     "Løsningen er at gøre retningen til få, målbare ting og give lederne ejerskab på hver deres: en "
     "skreven prioritering pr. kvartal, ledelsesaftaler med to-tre punkter og et ledermøde med "
     "beslutningslog. Jeg har selv bygget en virksomhed op og ledet teknikere, montører og "
     "leverandører mod samme standarder."),

    ("Kravet: økonomisk ansvar for afdelingen, KPI-opfølgning og levering i henhold til kontrakterne",
     "Løsningen er at styre på kontrakten: hvert KPI har en ejer, en måling og en fast gennemgang, og "
     "økonomien følges månedligt med prognose — så en afvigelse bliver set, før den bliver en "
     "kundesag. Jeg har haft fuldt P&L, budget i SAP og prognoseansvar."),

    ("Kravet: tydelige roller, fælles arbejdsgange og ensartet høj kvalitet på tværs af kunder og "
     "ejendomstyper",
     "Løsningen er én arbejdsgang pr. proces — ikke én pr. kunde: en standard for vedligehold, akut "
     "sag, leverandørvalg og dokumentation, med kundens særkrav som et lag ovenpå. Det er sådan, en "
     "lille organisation kan levere ensartet til mange uden at dobbeltarbejde."),

    ("Kravet: sparring med internationale kunder om resultater, der understøtter deres "
     "investeringsstrategi",
     "Løsningen er at tale kundens sprog: driftstab, energi, vedligeholdelsesbehov og "
     "investeringsforslag pr. ejendom, fremlagt i et fast kvartalsmøde — kort, på engelsk og med et "
     "klart forslag til næste beslutning."),

    ("Kravet: strategisk leverandørstyring og de rette aftaler på lang sigt",
     "Løsningen er en leverandørplan pr. fag: hvad der skal udbydes, hvad der skal være "
     "rammeaftale, og hvad der skal leveres på KPI med fast performance-review. Jeg har arbejdet med "
     "udbud, kontrakter og garantisager og ved, hvad der sker, når aftalen ikke er skrevet ordentligt."),

    ("Kravet: en kultur præget af tillid, tryghed og arbejdsglæde",
     "Løsningen er forudsigelighed: klare forventninger, plads til at sige til i tid, og en leder der "
     "er synlig. Fem år med 24/7-drift og nul uplanlagte stop har lært mig, at tryghed opstår, når "
     "ingen bliver overrasket."),

    ("Kravet: teknisk tyngde i ejendomsdrift — VVS, el, ventilation, klimaskærm, teknik i "
     "investeringsejendomme",
     "Løsningen er elautoriseret maskinmester (LV/MV/HV) med 20 år i tekniske anlæg: pumper, HVAC, "
     "køl, højspænding og styringer, tilstandsvurdering og prioritering af vedligehold — og fem år i "
     "et 24/7-anlæg, hvor nedbrud havde en pris."),

    ("Kravet: forretningsforståelse og et langsigtet blik",
     "Løsningen er at knytte drift til værdi: hvad koster en udskydelse, hvad er levetiden, og hvad "
     "betyder det for ejendommens afkast og udlejelighed — så vedligehold bliver et "
     "investeringsforslag frem for en regning. Jeg har bygget prognoser og kalkuler selv."),

    ("Kravet: international leverance på højt dansk og engelsk i skrift og tale",
     "Løsningen er dokumenter og oplæg på det sprog, kunden læser, og møder hvor jeg selv taler "
     "engelsk professionelt. Jeg rapporterer i dag til både danske og engelsktalende "
     "samarbejdspartnere."),

    ("Kravet: data og digitalisering som aktivt værktøj i leverancen",
     "Løsningen er dashboards på de tal, der styrer leverancen, og automatiseret rapportering, så "
     "tiden går til drift frem for til at samle tal. Jeg koder selv i Python og bruger Claude dagligt "
     "— det er den slags, Newsec i 2026 kalder vejen fra klassisk administrator til full-service "
     "partner."),
]

SYSTEM = (
    "Systemet står klar fra dag ét: leverancemodel pr. kunde med KPI og kontraktkrav, fast "
    "lederkadence med beslutningslog, månedlig økonomi- og driftsrapport, leverandørplan pr. fag og "
    "et kvartalsmødeformat til kunderne — ført i Power BI og Excel sammen med Newsecs "
    "administrationssystemer, med rapporter og oplæg genereret i Python og Claude."
)

MIRROR = (
    "Om kravene: elautoriseret maskinmester (LV/MV/HV) og B.Tech, 20 år i tekniske anlæg og otte år "
    "med personaleansvar — 5 elektrikere og 3 lærlinge med fuldt P&L, 14-mands team med 11 samtidige "
    "opgaver, 25 specialister koordineret på tværs af fag og fem år som drifts- og "
    "vedligeholdelseschef i Biofos med budget i SAP, leverandører og 24/7-drift."
)

HONEST = (
    "Det skal siges ligeud: jeg har ikke arbejdet i et kommercielt ejendomsforvaltningsselskab med "
    "investorkunder før, og min ledelse af ledere er foreløbig sket i mindre enheder — 5 elektrikere "
    "og 3 lærlinge og et 14-mands team — ikke i en afdeling med flere ledelsesniveauer. Det, jeg "
    "bringer, er teknisk drift på højt niveau, økonomi med fuldt ansvar og en dokumenteret evne til "
    "at lave systemer, der holder, når der er mange kunder og få hænder."
)

CULTURE = (
    "Newsec beskriver sig som en partner-ejet virksomhed, hvor kunden er i centrum, og hvor vejen frem "
    "mod 2026 er at gå fra klassisk administrator til full-service partner med data og digitale "
    "ydelser som aktive værktøjer. Det er præcis den rolle, jeg gerne vil have: drift, der bliver "
    "talt om som værdi for kunden — ikke som en omkostning, der skal holdes nede."
)

PRACTICAL = (
    "Bosat i Måløv — cirka 20 minutter i bil til Lyngby Hovedgade 4. Kørekort B og bil, dansk på "
    "modersmålsniveau og engelsk professionelt i skrift og tale. Kan tiltræde hurtigst muligt eller "
    "efter aftale."
)

CLOSING = (
    "I første samtale vil jeg gerne tale om, hvilke tre ting der skal være ens på tværs af kunderne i "
    "dag — og hvad der med vilje skal være forskelligt."
)

# ------------------------------------------------------------------ CV
PROFILE = (
    "Teknisk leder med 20 år i anlæg og drift og otte år med personaleansvar: fem år som drifts- og "
    "vedligeholdelseschef i Biofos med budget i SAP, leverandørstyring og 24/7-drift, to år som "
    "indehaver og teknisk direktør med fuldt P&L og to år som projektleder på 37 samtidige "
    "anlægsprojekter. Elautoriseret maskinmester (LV/MV/HV) og B.Tech — arbejder med KPI-styring, "
    "standardiserede arbejdsgange og dashboards, og koder selv de rapporter, ledelsen læser."
)

PRACTICE = [
    ("Multi-kunde leverance",
     "Leverancemodel pr. kunde med KPI, kontraktkrav og fast kvartalsmøde — og én fælles arbejdsgang "
     "pr. proces med kundens særkrav som lag ovenpå."),
    ("Økonomi og kontrakt",
     "Budget, prognose og økonomiopfølgning med fuldt ansvar i SAP; udbud, kontrakter og "
     "leverandøropfølgning på aftalte mål."),
    ("Ledelse af ledere",
     "Ledelsesaftaler, fast ledermøde med beslutningslog, tydelige roller og oplæring med to personer "
     "pr. kritisk kompetence; rekruttering og udvikling af en virksomhed fra bunden."),
    ("Teknisk drift og vedligehold",
     "Tilstands- og kritikalitetsbaseret vedligehold, HVAC, el, køl og styringer; nul uplanlagte stop "
     "i fem år på et 24/7-anlæg med KPI'er i SAP."),
    ("Leverandørstyring",
     "Leverandørplan pr. fag, rammeaftaler, performance-review og garantisager — fra udbud til "
     "lukket sag."),
    ("Data og rapportering",
     "Dashboards og automatiseret månedsrapportering i Power BI; Python og Claude i daglig brug til "
     "analyser, oplæg og instrukser."),
]

MODELS = [
    ("Leverancemodel pr. kunde",
     "Kontraktkrav, KPI, svartider og rapporteringskadence på én side pr. kunde; revideret ved "
     "kontraktændring, ikke kun ved klage"),
    ("Processtandard",
     "Én arbejdsgang pr. proces (akut sag, vedligehold, leverandørvalg, dokumentation) gældende for "
     "alle kunder; kundens særkrav som skrevet lag ovenpå"),
    ("Ledermøde",
     "Fast kadence med beslutningslog og en agenda, der starter med KPI og økonomi — ikke med "
     "sagerne"),
    ("Leverandørplan",
     "Pr. fag: hvad der er rammeaftale, hvad der skal udbydes, og hvornår performance-review "
     "gennemføres med KPI og pris"),
    ("Kundedialog",
     "Fast kvartalsmøde med driftstal, vedligeholdelsesbehov, energi og et investeringsforslag pr. "
     "ejendom — kort og på engelsk"),
    ("Opfølgning",
     "Månedlig rapport på få tal: KPI, økonomi, akutte sager og leverandørperformance; genereret i "
     "Python og Claude"),
]

ACHIEVEMENTS = [
    ("Nul uplanlagte stop i fem år",
     "24/7-anlæg med SCADA, højspænding og koblingsanlæg — planlagt vedligehold, tilstandskontrol "
     "og KPI'er i SAP, og en driftsorganisation der holdt, også under sygdom."),
    ("5 elektrikere og 3 lærlinge med fuldt P&L",
     "egen virksomhed: rekruttering, oplæring, arbejdsmiljø, kunder, leverandøraftaler og ansvar "
     "for bundlinjen."),
    ("14-mands team med 11 samtidige opgaver",
     "kapacitetsplanlægning, daglige tavlemøder og tydelig prioritering i eksisterende byggeri med "
     "drift og brugere omkring os."),
    ("37 anlægsprojekter uden kritiske fund",
     "2-10 mio. kr. hos Novo Nordisk med 25 specialister koordineret på tværs af mekanik, el, proces "
     "og indkøb — FAT/SAT og dokumentation der bestod revision."),
]

EXPERIENCE = [
    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7-anlæg · pumper, HVAC, køl, koblingsanlæg og højspænding · budget i SAP",
     [("Drift, vedligehold og driftssikkerhed",
       "planlagt vedligehold, tilstandskontrol og KPI'er i SAP; nul uplanlagte stop i fem år på et "
       "anlæg, hvor driften ikke kunne vente."),
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
     [("Personale, kapacitet og leverance",
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

PRACTICAL_CV = ("Bosat i Måløv — cirka 20 minutter i bil til Lyngby Hovedgade 4; kørekort kategori B "
                "og bil. Dansk på modersmålsniveau og engelsk professionelt i skrift og tale. Kan "
                "tiltræde hurtigst muligt eller efter aftale.")

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Biofos (Lynetten), Novo Nordisk A/S, "
              "Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Teamet og lederne",
     "Tydelige roller, ledelsesaftaler og et ledermøde, der starter med KPI og økonomi — og en chef, "
     "der tager de svære kunder selv."),
    ("De internationale kunder",
     "Fast kvartalsmøde med driftstal, vedligeholdelsesbehov og et investeringsforslag pr. ejendom — "
     "så driften bliver læst ind i kundens investeringsstrategi."),
    ("Kolleger på tværs af administration, økonomi, projekt og ESG",
     "Aftalte snitflader og én fælles arbejdsgang, så kunden møder ét svar og ikke fem."),
    ("Leverandørerne",
     "Rammeaftaler, performance-review og en plan for, hvad der skal udbydes hvornår — langsigtet "
     "frem for akut."),
]

FIRST90 = [
    ("Dage 1–30",
     "Mødt team og ledere, været på de væsentligste ejendomme og læst alle kundekontrakter igennem: "
     "hvad er lovet, hvad måles, og hvor er der afvigelser i dag."),
    ("Dage 30–60",
     "Leverancemodel pr. kunde på plads; lederkadence og beslutningslog etableret; økonomi- og "
     "KPI-rapport på få tal kørende."),
    ("Dage 60–90",
     "Én processtandard pr. arbejdsgang indført og prøvekørt på en ejendom; leverandørplan pr. fag "
     "lagt; første kvartalsmødeformat afprøvet med en kunde."),
    ("Måned 3–6",
     "Ensartet kvalitet på tværs af kunder kan dokumenteres på KPI; de første rammeaftaler "
     "forhandlet og de første dashboards i drift."),
    ("Måned 6–12",
     "Afdelingen leverer stabilt på kontrakterne, har en ledergruppe, der selv driver udviklingen — "
     "og en kundeportefølje, hvor ingen bliver overrasket.",
    ),
]

KEYWORDS = (
    "Teamleder · Technical Management Services · TMS · Investeringsejendomme · Newsec · "
    "Property Asset Management · Internationale kunder · Udenlandske ejendomsinvestorer · "
    "Porteføljer · Domicilejendomme · Hoteller · Bolig · Logistik · Teknisk drift · Leder · "
    "Driftsfolk · Fælles processer · Rammer · Kunder · Strategisk retning · "
    "Lede og udvikle dine ledere · Økonomisk ansvar · KPI-opfølgning · "
    "Leverancer i henhold til kontrakterne · Tydelige roller · Fælles arbejdsgange · "
    "Ensartet høj kvalitet · Ejendomstyper · Sparring · Investeringsstrategi · "
    "Strategisk leverandørstyring · Aftaler på lang sigt · Kultur · Tillid · Tryghed · Arbejdsglæde · "
    "Erfaring med ejendomsdrift · Struktur · Klar kommunikation · Teknisk uddannelse · Ingeniør · "
    "Maskinmester · Bygningstekniker · Forretningsfaglig uddannelse · Ledelseserfaring · "
    "Ledelse af ledere · Udvikling af en afdeling · Flere kunder · Forretningsforståelse · "
    "Langsigtet blik · Engelsk · Dansk · Lyngbyhus · Kongens Lyngby · Ejendomsadministration · "
    "Asset management · Udlejning · Bygherrerådgivning · ESG · Bæredygtige løsninger · "
    "Inkluderende kultur · Lean · SAP"
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

    m.models_table("AFDELINGENS STYRING — ANVENDT I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER AFDELINGEN I DRIFT",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN LEDES AFDELINGEN — DE FIRE PARTER")
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
    build(os.path.join(ROOT, "Shahram_Ajloo_Newsec_TeamlederTMS.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_Newsec_TeamlederTMS.docx"))
