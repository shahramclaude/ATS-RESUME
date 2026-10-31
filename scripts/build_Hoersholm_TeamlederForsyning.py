# -*- coding: utf-8 -*-
"""
Hørsholm Kommune — Teamleder til Team Forsyning (Center for By og Miljø).
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Teamleder | Forsyning — spildevand & affald | Kommunal drift og udvikling"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "31. oktober 2026"
RECIPIENT = ("Hørsholm Kommune · Center for By og Miljø · Team Forsyning · att. centerchef Jeppe "
             "Fisker Jørgensen · 21657518")
SUBJECT = "Ansøgning: Teamleder til Team Forsyning"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Opgaven er at lede et nyetableret forsyningsteam, hvor den daglige drift af spildevand og affald "
    "ikke må tabe fart, mens separatkloakering, klimatilpasning, ny lovgivning om terrænnært grundvand, "
    "et fælles vandressourcecenter med Novafos og et kommende udbud af affaldsindsamling skal følges "
    "helt til dørs. Det er to spor på én gang: driften skal køre i dag, og udviklingen skal være længere "
    "frem om et år, end den er nu.",

    "Nedenfor er min læsning af rollen og det system, der står klar fra første dag: én fælles "
    "opgaveportefølje med ejer, frist og status, en kapacitetsplan der skiller drift fra udvikling, "
    "1:1 og faglig sparring på fast kadence, et standardformat til politiske oplæg og en mødekadence med "
    "de to andre teams og staben.",
]

BULLETS = [
    ("Kravet: lede et nyetableret team med to grupper — Spildevand og Affald",
     "Løsningen er at bygge rammerne sammen med teamet først: hvem beslutter hvad, hvem svarer på hvilke "
     "sager, og hvordan vi mødes. Kultur bliver ikke skrevet ned og vedtaget — den bliver skabt i de "
     "første hundrede dage, og den skal være fagligt stolt og uformel på samme tid."),

    ("Kravet: holde styr på den daglige drift og samtidig drive de større udviklingsopgaver",
     "Løsningen er at skille de to spor ad i planen: en driftsdel med faste frister og en udviklingsdel "
     "med navngivne ejere og milepæle, så udviklingen ikke kun ligger hos lederen, men bliver drevet af "
     "dem, der ejer opgaven — og bliver fulgt op hver uge."),

    ("Kravet: indgående kendskab til forsyningsområdet, fra kommune eller forsyningsselskab",
     "Løsningen er fem år på 24/7-forsyningsanlægget Lynetten: spildevandsrensning, pumpestationer, "
     "HVAC og koblingsanlæg med SCADA, budgetter i SAP og nul uplanlagte stop i fem år — i en "
     "virksomhed ejet af kommuner, hvor myndighedskrav og politiske beslutninger var rammen om arbejdet."),

    ("Kravet: personaleledelse og tydelige rammer med løbende sparring",
     "Løsningen er tæt ledelse i praksis: 1:1 hver fjerde uge, MUS med opfølgning, kompetencematrix og "
     "en klar forventningsafstemning pr. medarbejder — 14- og 12-mands teams, 5 elektrikere og 3 "
     "lærlinge og 25 specialister koordineret. Tillidsbaseret ledelse kræver rammer, ikke fravær."),

    ("Kravet: oversætte strategiske mål til konkret handling og levere politiske beslutningsoplæg",
     "Løsningen er et årshjul for teamet med de politiske deadlines lagt ind først, og et fast format "
     "for oplæg: faglig indstilling, økonomi, risici, alternativer og en anbefaling — skrevet så en "
     "politiker uden for faget kan træffe beslutningen."),

    ("Kravet: politisk forståelse og blik for borgernes og forsyningsselskabernes behov",
     "Løsningen er at kende forskellen på faglighed og beslutning: jeg leverer det faglige grundlag, "
     "tydeligt og uden skjulte dagsordener, og gennemfører bagefter den beslutning, der bliver truffet — "
     "også når den er en anden, end jeg anbefalede."),

    ("Kravet: samarbejde i centret, på tværs af kommunen og med omverdenen",
     "Løsningen er én indgang til Forsyning med aftalte svartider, fast mødekadence med Plan & Byg, Vej, "
     "Park & Miljø og staben om GIS og fælles sager, og en dialog med Novafos, nabokommunerne og "
     "affaldsindsamlerne, hvor aftaler og tal er dokumenteret."),
]

SYSTEM = ("Systemet er allerede bygget: fælles opgaveportefølje med ejer, frist og status, "
          "kapacitetsplan seks uger frem der skiller drift fra udvikling, 1:1- og sparringskalender, "
          "beslutningslog, standardformat til politiske oplæg og KPI'er for sager til tiden, "
          "kloakoplande og affaldsservice — i Excel og Power BI, med Python og Claude til overblik og "
          "rapportering.")

MIRROR = ("Om kravene: 20 år i forsyning, drift og projekter — fem år som drifts- og "
          "vedligeholdelseschef på 24/7-spildevandsanlægget Lynetten, 14- og 12-mands teams, 5 "
          "elektrikere og 3 lærlinge med fuldt P&L, 37 anlægsprojekter med 25 specialister under "
          "myndighedskrav; elautoriseret maskinmester (LV/MV/HV) og B.Tech.")

HONEST = ("Tre ting skal siges ligeud: jeg har ikke været ansat i en kommune før — min forsyning er "
          "kommet fra et kommunalt ejet selskab, hvor beslutningerne blev truffet et andet sted; "
          "affaldsområdet, herunder udbud af affaldsindsamling, har jeg ikke arbejdet i; og "
          "separatkloakering og klimatilpasning har jeg mødt fra drifts- og anlægssiden, ikke fra "
          "myndighedssiden. Det er præcis derfor, jeg vil bruge de første uger på at lære af teamet og "
          "af jer, før jeg foreslår ændringer.")

CULTURE = ("Hvorfor Hørsholm: I skriver uformel omgangstone og humoristisk sans — og i et nyetableret "
           "team er det ikke en detalje, det er infrastruktur. Relationel kapacitet bliver ikke skabt af "
           "et værdikort, men af hvordan vi taler sammen, når en sag er svær, og af at man kan sige "
           "højt, at man har brug for hjælp uden at tabe ansigt. Servicekulturen over for borgerne "
           "starter indad i teamet.")

PRACTICAL = ("Praktisk: bosat i Måløv — cirka 30 minutter til Hørsholm; kørekort B og bil; dansk på "
             "modersmålsniveau i skrift og tale; kan tiltræde 1. februar 2027 som ønsket, og egen "
             "virksomhed afvikles ved ansættelse.")

CLOSING = ("Jeg vil gerne høre, hvordan I i dag fordeler opgaverne mellem de to grupper, og hvad der "
           "skal være anderledes i teamet om et år. Og så vil jeg gerne vide, hvordan I arbejder med de "
           "politiske oplæg i centret — hvem skriver, og hvornår bliver fagligheden kvalificeret.")

# ------------------------------------------------------------------ CV
PROFILE = ("Rollen kræver tre ting på én gang: drift der ikke falder fra hinanden, udvikling der bliver "
           "ført ud i livet, og en leder der kan gøre faglighed til politisk beslutningsgrundlag. Alle "
           "tre har været hverdag i 20 år: fem år som drifts- og vedligeholdelseschef på "
           "24/7-spildevandsanlægget Lynetten med nul uplanlagte stop, 14- og 12-mands teams og egen "
           "virksomhed med 5 elektrikere og 3 lærlinge på fuldt P&L, samt 37 anlægsprojekter hos Novo "
           "Nordisk med 25 specialister under myndighedskrav. Elautoriseret maskinmester (LV/MV/HV), "
           "B.Tech i Technology Management & Mechanical Engineering.")

PRACTICE = [
    ("Ledelse af tekniske teams",
     "1:1-hjul, MUS med opfølgning, kompetencematrix, tydelige rammer og forventningsafstemning, "
     "situationsbestemt ledelse (SLII) og delegering med opfølgning — ikke med kontrol."),
    ("Drift og anlæg",
     "Forebyggende vedligeholdsplan, tilstandskontrol, kritiske reservedele, PDCA-årshjul og KPI'er i "
     "SAP; 24/7-drift med beredskab og nul uplanlagte stop i fem år."),
    ("Spildevand",
     "Driftserfaring fra rensning af spildevand: pumper, pumpestationer, HVAC, koblingsanlæg, "
     "højspænding og SCADA — plus anlægs- og dokumentationsarbejde i forbindelse med projekter."),
    ("Portefølje og prioritering",
     "Fælles opgaveportefølje med ejer, frist og status, kapacitetsplan seks uger frem, prioritering "
     "mellem drift og udvikling og en fast ugentlig opfølgning på, hvad der er kommet videre."),
    ("Strategi til handling",
     "Årshjul med politiske deadlines, målbillede oversat til indsatser med ejer og effektmål, og "
     "opfølgning på, om indsatsen faktisk flyttede noget — ikke kun om den blev iværksat."),
    ("Politiske oplæg og myndighed",
     "Beslutningsoplæg med faglig indstilling, økonomi, risici og alternativer; arbejde under "
     "myndighedskrav, tilsyn og revision i GMP/FDA/EMA- og forsyningsmiljøer."),
    ("Samarbejde og kommunikation",
     "Én indgang med aftalte svartider, mødekadence og referater på tværs af teams, stabe og eksterne "
     "parter; svære samtaler med borgere, leverandører og samarbejdspartnere."),
]

MODELS = [
    ("Ledelse",
     "1:1-hjul, MUS/GRUS, kompetencematrix, situationsbestemt ledelse (SLII), tillidsbaseret ledelse "
     "med klare rammer"),
    ("Portefølje",
     "Opgaveportefølje med ejer/frist/status, kapacitetsplan seks uger frem, drift- og udviklingsspor "
     "adskilt, ugentlig opfølgning"),
    ("Drift",
     "Forebyggende vedligeholdsplan, PDCA-årshjul, KPI'er i SAP, kritikalitet og beredskab på 24/7-anlæg"),
    ("Strategi og politik",
     "Målbillede → indsatser med ejer og effektmål; beslutningsoplæg med indstilling, økonomi, "
     "risici og alternativer"),
    ("Økonomi",
     "Budget og prognose, kalkule mod timeforbrug, afvigelser med ejer og frist, "
     "leverandør- og udbudsdokumentation"),
    ("Kvalitet og dokumentation",
     "Egenkontrol, afvigelser med root cause, dokumentstyring med version og ejer, "
     "afleverings- og driftsdokumentation"),
    ("Værktøjer",
     "Excel og Power BI til overblik, SAP/CMMS, GIS-baserede sagsdata og Python/Claude til "
     "rapportering og kvalitetssikring"),
]

ACHIEVEMENTS = [
    ("Nul uplanlagte stop i fem år",
     "på 24/7-forsyningsanlægget Lynetten — planlagt vedligehold, PDCA og A3-root-cause frem for "
     "brandslukning."),
    ("14- og 12-mands teams ledet",
     "kapacitetsplanlægning, prioritering og daglige tavlemøder i drift og montage."),
    ("5 elektrikere og 3 lærlinge med fuldt P&L",
     "daglig ledelse, kompetenceudvikling og udviklingssamtaler i egen virksomhed."),
    ("37 anlægsprojekter gennemført",
     "25 specialister koordineret på tværs af mekanik, el, proces og indkøb — nul kritiske fund ved "
     "aflevering."),
    ("−40 % energikost og +40 % produktivitet",
     "dokumenterede forbedringer via måling, standardarbejde, dataunderstøttet planlægning og egen "
     "AI-tooling."),
]

EXPERIENCE = [
    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 spildevandsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · budgetter i SAP",
     [("Drift og KPI",
       "PDCA-baseret vedligeholdsplan med fast årshjul, A3-root-cause på større nedetid og KPI'er i "
       "SAP; nul uplanlagte stop i fem år."),
      ("Prioritering og beredskab",
       "fejlfinding og reparation på pumper, HVAC, koblingsanlæg og højspænding; prioritering mellem "
       "anlæg, når flere ting stod på én gang."),
      ("Leverandører og sikkerhed",
       "koordinering af egne teknikere, entreprenører og leverandører — LOTO, arbejdstilladelser, "
       "garantisager og nærved-hændelser.")]),

    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og leverandøraftaler",
     [("Personale og rammer",
       "daglig ledelse af 5 elektrikere og 3 lærlinge, opgavefordeling, kompetencematrix og "
       "udviklingssamtaler."),
      ("Kunder og økonomi",
       "serviceaftaler og akutte sager med erhvervskunder, plan og prognose, indkøb og "
       "leverandøraftaler med fuldt ansvar for bundlinjen.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister · GMP/FDA/EMA",
     [("Kvalitet og dokumentation",
       "FAT/SAT, IQ/OQ/PQ og valideringsdokumentation med afvigelseshåndtering — nul kritiske fund; "
       "arbejde under myndighedskrav og revision."),
      ("Projekt og koordinering",
       "plan, økonomi og rapportering; 25 specialister koordineret på tværs af mekanik, el, proces og "
       "indkøb.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Team og fremdrift",
       "14-personers team med kapacitetsplanlægning, flowstyring og daglige tavlemøder over 11 "
       "samtidige entrepriser.")]),

    ("Elektromekaniker / Produktionsteamleder",
     "ARJ Engineering · Teheran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · skiftplanlægning, materialestyring og lager",
     [("Produktionsteam og teknisk problemløsning",
       "skiftplanlægning, materialestyring og målopfølgning; reparation og diagnosticering gennem "
       "struktureret root cause-analyse.")]),
]

EDUCATION = [
    ("B.Tech (EQF niveau 6) — Technology Management & Mechanical Engineering",
     "Maskinmesterskolen / Copenhagen School of Marine Engineering & Technology Management · 2017 – "
     "2022 · karakter 7,6/12"),
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
     "Anvendt i drift og projekter · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og projekter · 2017 – nu"),
]

LANGUAGES = ("Dansk (modersmål, skrift og tale) · Engelsk (professionelt) · Persisk/farsi · "
             "Kørekort B (kategori B)")

PRACTICAL_CV = ("Bosat i Måløv — cirka 30 minutter til Hørsholm; kørekort kategori B og bil; dansk på "
                "modersmålsniveau i skrift og tale; kan tiltræde 1. februar 2027; egen virksomhed "
                "afvikles ved ansættelse.")

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Biofos (Lynetten), Novo Nordisk A/S "
              "(Kalundborg) og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("De to grupper i teamet",
     "Klare rammer for, hvem der beslutter og svarer på hvad, 1:1 og faglig sparring på fast kadence, "
     "og en leder der tager de svære samtaler tidligt i stedet for at lade dem vokse."),
    ("Centerledelsen og de andre teams",
     "Én indgang til Forsyning med aftalte svartider, fast mødekadence med Plan & Byg, Vej, Park & "
     "Miljø og staben, og sager der kommer op, før de bliver akutte."),
    ("Politikere, Novafos og affaldsindsamlerne",
     "Beslutningsoplæg med indstilling, økonomi, risici og alternativer; samarbejdsaftaler og tal, der "
     "er dokumenteret, så prioriteringer kan forklares for borgerne."),
]

FIRST90 = [
    ("Uge 1–2",
     "Mødt alle i teamet — begge grupper — og gennemgået porteføljen, de åbne sager, aftalerne med "
     "Novafos og nabokommunerne samt de politiske sager, der er på vej. Mødt centerchefen, de to andre "
     "teams og staben."),
    ("Uge 3–6",
     "Fælles opgaveportefølje med ejer, frist og status lagt; rammer for hvem der beslutter og svarer "
     "på hvad aftalt med teamet; 1:1-kalender og ugentligt teammøde i gang."),
    ("Uge 7–12",
     "Kapacitetsplan seks uger frem, hvor drift og udvikling er skilt ad; status på udbudsforberedelsen "
     "og vandressourcecenter-sagen lagt frem for centerledelsen; KPI-baseline for sager til tiden."),
    ("Måned 3–6",
     "Udviklingsopgaver har navngivne ejere og milepæle og bliver fulgt op hver uge; første "
     "beslutningsoplæg skrevet i centerets format; arbejdsmiljø og sikkerhed gennemgået med teamet."),
    ("Måned 6–12",
     "Teamet leverer drift uden akutte sager, der skubber planlagt arbejde, og har flyttet mindst to "
     "udviklingsopgaver mærkbart; samarbejdet med Novafos, nabokommunerne og affaldsindsamlerne kører "
     "på faste aftaler. Løbende: månedlig ledelsesgennemgang og en fast post for, hvad der skal "
     "forenkles næste måned."),
]

KEYWORDS = (
    "Teamleder · Team Forsyning · Forsyning · Spildevand · Affald · Center for By og Miljø · Daglig "
    "drift · Udviklingsopgaver · Opgaveportefølje · Prioritering · Struktur · Rammer · Personaleledelse · "
    "Sparring · Tillidsbaseret ledelse · Strategiske mål · Konkret handling · Politiske beslutningsoplæg · "
    "Politisk forståelse · Politisk ledet organisation · Kommune · Forsyningsselskab · Novafos · "
    "Vandressourcecenter · Separatkloakering · Klimatilpasning · Terrænnært grundvand · Byudvikling · "
    "Affaldsindsamling · Udbud · Genanvendelse · Genbrug · Servicekultur · Relationel kapacitet · "
    "Samarbejde · Kommunikation · Svære samtaler · Borgerne · Driftsorganisation · KPI · SAP · SCADA · "
    "Power BI · Arbejdsmiljø · Dansk · Hørsholm · Måløv"
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
        m.para(t, after=80)

    for label, body in BULLETS:
        m.bullet(label, body, after=20)

    m.para(SYSTEM, after=80)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=35)

    m.meta("Med venlig hilsen · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "LEDELSESPROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("LEDELSES- OG DRIFTSMETODER — ANVENDT I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER TEAMET I RYTMEN",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN LEDES TEAMET — DE TRE PARTER")
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

    from docx.oxml.ns import qn as _qn
    from docx.oxml import OxmlElement as _OE
    for _tbl in m.doc.tables:
        for _tr in _tbl._tbl.findall(_qn("w:tr")):
            _trPr = _tr.find(_qn("w:trPr"))
            if _trPr is None:
                _trPr = _OE("w:trPr")
                _tr.insert(0, _trPr)
            if _trPr.find(_qn("w:cantSplit")) is None:
                _trPr.insert(0, _OE("w:cantSplit"))

    return m.save(path,
                  title="Ansøgning og CV — Teamleder til Team Forsyning, Hørsholm Kommune",
                  subject="Spildevand og affald · drift og udvikling · politisk ledet organisation",
                  keywords=("teamleder, forsyning, spildevand, affald, kommune, hørsholm, "
                            "beslutningsoplæg, personaleledelse, drift, udvikling, dansk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1 (krav → løsning), CV side 2-3, 90 dage side 4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_Hoersholm_TeamlederForsyning.docx")
    print("OK", build(out))
