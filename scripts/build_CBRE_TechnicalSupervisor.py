# -*- coding: utf-8 -*-
"""
CBRE Global Workplace Solutions — Technical Supervisor, København.
Job ID 303099 · base København · sites på Sjælland. Dansk JD.
Bygget i designet fra master-CV'erne. Sprog: dansk.

Vinkel: han kommer fra den tunge tekniske drift (24/7-anlæg, 40+ serviceanlæg,
egne underleverandører) og søger bevidst en rolle tæt på driften og kunden —
ikke en ledelsesrolle på afstand. Bosat i Måløv = opfylder kravet om København.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Technical Supervisor | CBRE Global Workplace Solutions | København"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv")

DATE = "30. oktober 2026"
RECIPIENT = ("CBRE Global Workplace Solutions · København · Att.: Contract Manager · "
             "Job ID 303099")
SUBJECT = "Ansøgning: Technical Supervisor — København (Job ID 303099)"

# ------------------------------------------------------------------ side 1
INTRO = [
    "En teknisk supervisor bliver målt på noget andet end en driftschef: på om bygningen kører, når kunden kommer "
    "om morgenen, på om underleverandøren var der som aftalt, og på om de ting, der blev observeret på "
    "runderingen, rent faktisk blev registreret og fulgt op. Jeg har stået i begge ender af den kæde — som "
    "driftsansvarlig på et 24/7-anlæg og som den håndværker, kunden ringede til.",

    "Jeg søger denne rolle bevidst. Jeg har prøvet at sidde et skridt tilbage fra driften, og det er ikke der, jeg "
    "er bedst. Det er ude på stedet, i teknikrummet og i samtalen med kunden, hvor jeg kan gøre en forskel — og "
    "jeg vil hellere være tæt på den daglige tekniske drift på flere sites end langt fra den på et kontor.",
]

BULLETS = [
    ("Teknisk drift, hvor der ikke er plads til uplanlagte stop",
     "24/7-anlæg med pumper, HVAC, koblingsanlæg, højspænding, nødstrøm og SCADA: fejlfinding under pres, "
     "forebyggende vedligehold efter plan og hurtig eskalering, når noget ikke kan løses på stedet."),

    ("Fiere sites og mange bolde — min hverdag i dag",
     "40+ serviceanlæg i Storkøbenhavn med 5 elektrikere og 3 lærlinge: planlægning, kørsel mellem adresser, "
     "koordinering af underleverandører og daglig kundekontakt på hvert sted. Det er præcis den arbejdsform, "
     "stillingen beskriver."),

    ("El, VVS og ventilation — ikke kun ét fag",
     "Elautoriseret maskinmester (LV/MV/HV) med egen autoriseret virksomhed og egenkontrol, suppleret med "
     "køle- og HVAC-teknik (AMU) og tyve års arbejde med tekniske installationer i bygninger, produktion og "
     "forsyningsanlæg. Jeg kan vurdere opgaven selv, før jeg sender den videre."),

    ("Underleverandører og dokumentation",
     "Underleverandører og servicepartnere styret på kontrakt, sikkerhedsdokumentation og fremdrift; tekniske "
     "runderinger, registrering i systemerne og sporbar dokumentation, så næste eftersyn ikke starter forfra."),

    ("Sikkerhed, lovkrav og KPI",
     "APV, risikovurdering, LOTO og arbejdstilladelser; lovpligtige eftersyn og myndighedskrav uden "
     "anmærkninger; KPI'er på responstid, oppetid og økonomi fulgt op månedligt og brugt til at pege på, hvor "
     "driften kan forbedres."),
]

MIRROR = ("Mod jeres ønsker: erfaring med teknisk drift, ejendomsdrift og facility management · indgående kendskab "
          "til tekniske installationer inden for el, VVS og ventilation · bosat i Måløv, altså i Københavns "
          "omegn og ikke en pendlerafstand · indstillet på kørsel mellem lokationer på Sjælland, kørekort B · "
          "dansk på modersmålsniveau og engelsk professionelt, skriftligt og mundtligt · struktureret og vant til "
          "at bevare overblikket med mange bolde i luften.")

HONEST = ("Én ting, lige ud: jeg søger ikke denne rolle, fordi jeg vil et skridt op. Jeg har haft ledelsesansvar i "
          "tyve år, med fuldt P&L-ansvar i dag, og jeg søger bevidst en teknisk rolle tættere på driften og "
          "kunden. Det betyder også, at jeg ikke kommer for at bygge et nyt system eller organisere om — jeg "
          "kommer for at få den daglige drift til at fungere og for at gøre det nemt for Contract Manager at se, "
          "hvordan det går.")

CULTURE = ("Hvorfor CBRE GWS. I leverer hard services med egen udførelse og høj downstream accountability — altså "
           "ikke et konsulentlag oven på driften, men et team, der selv står inde for, at arbejdet er gjort. Det er "
           "den form for ansvar, jeg er vant til. Og jeres RISE-værdier — Respect, Integrity, Service, Excellence "
           "— er ikke svære at underskrive, når man kommer fra en branche, hvor tillid hos kunder, kollegaer og "
           "samarbejdspartnere er det, der afgør, om man bliver ringet op igen: respekt for folks arbejde, integritet i det man lover, service på det tidspunkt "
           "man har sagt, og excellence i detaljen, fordi detaljen er det, der holder bygningen kørende.")

PRACTICAL = ("Praktisk: bosat i Måløv, kort til alle kundens lokationer i hovedstadsområdet og kørende på Sjælland "
             "uden problemer; kørekort B og egen bil; dansk som modersmål og engelsk på professionelt niveau. "
             "Kort opsigelse, og ved ansættelse afvikler jeg min egen virksomhed, så der er ingen konkurrerende "
             "forpligtelser i hverdagen.")

CLOSING = ("Jeg kommer gerne med ud på et af sites og ser den tekniske drift, før vi taler om KPI'er — det er "
           "lettere at tale om forbedringer, når man har set, hvordan udstyret faktisk har det.")

# ------------------------------------------------------------------ CV
PROFILE = ("Teknisk driftsansvarlig med mere end 20 års erfaring fra tekniske installationer, 24/7-drift og "
           "reguleret produktion — og med ledelsesansvar siden 2003 og fuldt P&L-ansvar. Har ansvaret for drift og "
           "vedligehold af el, tavler, koblingsanlæg, højspænding, ventilation, køl og SCADA på et 24/7-anlæg, og "
           "driver i dag egen autoriseret el-virksomhed med 40+ serviceanlæg fordelt over hele Storkøbenhavn, "
           "hvor kørsel mellem adresser, underleverandører, kundekontakt og dokumentation er en del af hver "
           "arbejdsdag. Elautoriseret maskinmester (LV/MV/HV) og B.Tech i Technology Management & Mechanical "
           "Engineering. Registrerer, dokumenterer og følger op i systemerne — og bruger Power BI, Python og "
           "Claude til at gøre oppetid, responstider og økonomi synlige. Dansk på modersmålsniveau, engelsk "
           "professionelt.")

PRACTICE = [
    ("Daglig teknisk drift og fejlfinding",
     "24/7-anlæg og 40+ serviceanlæg: fejl findes systematisk, mens driften kører, og løses i samarbejde med "
     "teknikere og underleverandører. El, tavler, koblingsanlæg, motorer, ventilation, køl, varme, vand og "
     "CTS — og den vurdering, der afgør, om en opgave skal løses nu, planlægges eller eskaleres."),

    ("Forebyggende og afhjælpende vedligehold",
     "Vedligeholdsplan med fast årshjul, lovpligtige eftersyn og serviceintervaller; prioritet efter "
     "kritikalitet, og afhjælpende arbejde der bliver til forebyggelse, fordi årsagen bliver fundet og "
     "registreret — ikke bare udbedret."),

    ("Sites, runderinger og systemer",
     "Tekniske runderinger med registrering af opgaver og observationer i CMMS/ERP, SAP og egne tjeklister; "
     "Power BI-dashboards og Python/Claude-værktøjer til automatiseret rapportering. Dokumentationen er "
     "sporbar, så næste eftersyn eller næste kollega ikke starter forfra."),

    ("Underleverandører og tilsyn",
     "Underleverandører og servicepartnere på kontrakt: sikkerhedsdokumentation, arbejdstilladelser og LOTO, "
     "tilsyn med at arbejdet udføres korrekt, til tiden og efter aftale — og tydelig melding til kunden, når "
     "noget ikke kan holde."),

    ("Kunde, kommunikation og KPI",
     "Kundens faste tekniske kontaktperson med daglig dialog og forventningsafstemning; KPI'er på responstid, "
     "oppetid og økonomi med input til rapportering og konkrete forslag til optimering — ikke kun status."),

    ("Energi og driftsoptimering",
     "−40 % energikost i reguleret produktion gennem struktureret PDCA, A3 og standardiserede løsninger — målt, "
     "dokumenteret og fastholdt efter projektets afslutning. Driftsoptimering er for mig en rundering, der "
     "bliver til en beslutning, ikke en rapport."),

    ("Sikkerhed, lovkrav og økonomi",
     "APV, risikovurdering og arbejdsmiljø; myndighedskrav og lovpligtige eftersyn; budgetopfølgning, "
     "leverandøraftaler og indkøb med fuldt P&L-ansvar i egen virksomhed."),
]

FIRST90 = [
    ("Uge 1–4",
     "Med på rundering på alle sites og lærer udstyret og kundens hverdag at kende; gennemgår "
     "vedligeholdsplanen, de åbne opgaver og de sidste 12 måneders driftsforstyrrelser. Møder teknikere og de "
     "vigtigste underleverandører på pladsen, ikke på mail."),
    ("Uge 5–8",
     "Overtager den daglige koordinering og kundekontakten på de aftalte sites: runderinger, registrering, "
     "opgaver i systemet og opfølgning med underleverandører. KPI-baseline lagt fast sammen med Contract "
     "Manager, så forbedringer kan måles."),
    ("Uge 9–12",
     "Driften kører uden overraskelser, og de ting der bliver observeret, bliver lukket. To-tre konkrete "
     "forbedringer gennemført med målbar effekt på responstid, gentagne fejl eller energiforbrug — og meldt "
     "ind som input til KPI-rapporteringen."),
    ("Måned 6–12",
     "En stabil teknisk drift på tværs af sites, hvor kunden ringer til mig først og får svar; underleverandører "
     "leverer som aftalt, dokumentationen er ajour, og forbedringsforslagene kommer fra observationer på "
     "runderingen frem for fra en rapport."),
]

MODELS = [
    ("Teknisk drift & installationer",
     "El-forsyning, tavler og koblingsanlæg, LV/MV/HV, nødstrøm, ventilation og klima, varme og køl, vand og "
     "afløb, trykluft, brand-anlæg, CTS/BMS og SCADA, elevator- og adgangsgrænseflader"),
    ("Vedligehold",
     "Forebyggende vedligeholdsplan og årshjul, lovpligtige eftersyn, afhjælpende vedligehold, "
     "kritikalitetsvurdering, reservedelsstyring, A3-root-cause og fem-hvorfor, 5S og standardarbejde"),
    ("Sites & koordinering",
     "Runderinger og observationer, opgave- og arbejdsordrestyring i CMMS/ERP, koordinering af teknikere og "
     "underleverandører, tilsyn og dokumentation, arbejdstilladelser og adgangsstyring"),
    ("Kunde & KPI",
     "Daglig kundedialog og forventningsafstemning, KPI-rapportering (responstid, oppetid, økonomi), "
     "serviceaftaler og SLA, forbedringsforslag med beregnet effekt"),
    ("Sikkerhed & compliance",
     "APV og risikovurdering, LOTO og sikringsprocedurer, arbejdstilladelser, entreprenørkontrol på aktive "
     "anlæg, near-miss-opfølgning, myndighedskrav og lovpligtige eftersyn"),
    ("El-fagligt ansvar",
     "Autorisation og egenkontrol, kredsskemaer og el-dokumentation, DS/HD 60364 og EN 61439, måling og test "
     "(isolation, kontinuitet, RCD), fejlfinding og spændingssætning"),
    ("Økonomi & indkøb",
     "Budgetopfølgning og prognose, tilbud og prissammenligning, leverandør- og underleverandøraftaler, "
     "indkøb af komponenter og serviceydelser, fakturering og afstemning"),
    ("Data & værktøjer",
     "SAP ERP og CMMS, Power BI til KPI og økonomi, Excel og Power Query, Python og Claude API til "
     "automatiseret rapportering og tjeklister"),
]

ACHIEVEMENTS = [
    ("24/7-drift uden uplanlagte stop",
     "pumper, HVAC, koblingsanlæg, højspænding og SCADA — oppetid gennem forebyggende vedligehold og hurtig "
     "fejlfinding."),
    ("40+ serviceanlæg i daglig drift",
     "med 5 elektrikere og 3 lærlinge — planlægning, kørsel mellem adresser, underleverandører og kundekontakt "
     "på hvert sted."),
    ("−40 % energikost",
     "i reguleret produktion via struktureret PDCA, A3 og standardiserede løsninger; målt og fastholdt efter "
     "projektets afslutning."),
    ("Nul kritiske afvigelser ved aflevering",
     "på 37 samtidige anlægsprojekter (2–10 mio. kr.) — dokumentation og aflevering uden fund."),
    ("+40 % produktivitet",
     "i egen virksomhed gennem dataunderstøttet planlægning, standardarbejde og egen AI-tooling."),
]

EXPERIENCE = [
    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg i Storkøbenhavn · fuldt P&L, serviceaftaler og "
     "leverandøraftaler",
     [("Daglig teknisk drift på mange adresser",
       "planlagt og afhjælpende vedligehold, fejlfinding på el, tavler, styring, ventilation og klima — med "
       "kørsel mellem sites og prioritering efter kritikalitet."),
      ("Kunde og kommunikation",
       "kundens kontaktperson på stedet: aftaler, opfølgning, ændringer i behov og den klare melding, "
       "når en opgave kræver mere, end der var regnet med."),
      ("Underleverandører og dokumentation",
       "koordinering og tilsyn, sikkerhedsdokumentation og arbejdstilladelser; egenkontrol, kredsskemaer og "
       "sporbar serviceregistrering."),
      ("Data, KPI og rapportering",
       "ERP-baseret ordre- og reservedelsstyring, Power BI-dashboards og Python/Claude-værktøjer til "
       "planlægning, tjeklister og rapportering; produktivitetsløft over 40 %.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · drifts- og "
     "vedligeholdelsesbudgetter i SAP",
     [("24/7 teknisk drift",
       "oppetid, forebyggende vedligehold og hurtig fejlfinding med nul tolerance for uplanlagte stop; "
       "koordinering af egne teknikere, entreprenører og leverandører."),
      ("Vedligeholdsplan og dokumentation",
       "standardarbejde, 5S, PDCA-baseret vedligeholdsplan, A3-root-cause, reservedelsflow og kritiske lagre; "
       "registrering og opfølgning i SAP."),
      ("Sikkerhed og myndighed",
       "LOTO, risikovurdering, arbejdstilladelser, near-miss-rapportering og værktøjsmøder; KPI'er og "
       "driftsbudgetter.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister inden for teknik, indkøb og drift · "
     "GMP/FDA/EMA",
     [("Idriftsættelse og aflevering",
       "FAT/SAT, IQ/OQ/PQ og valideringsdokumentation med afvigelseshåndtering, CAPA og change control — nul "
       "kritiske fund ved aflevering."),
      ("Anlæg i drift",
       "arbejde i renrum, lager og produktion: arbejdstilladelser, LOTO, entreprenørkontrol og grænseflader "
       "til Kvalitet, Vedligehold og Produktion."),
      ("Projekt og økonomi",
       "tidsplan, økonomi, risiko og månedlig rapportering til ledelse og kunde på tværs af teknik, indkøb og "
       "drift; −40 % energikost gennem PDCA og standardiseret arbejde.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Ventilation og montage",
       "kapacitetsplanlægning og flowstyring over 11 samtidige projekter, fra specifikation til formel "
       "aflevering."),
      ("Kvalitet og levering",
       "standardiseret arbejde ved hver station med mærkbar fremgang i leveringsperformance og "
       "førstegangskvalitet."),
      ("Sikkerhed på aktive anlæg",
       "arbejdstilladelser, sikkerhedsdokumentation og entreprenørkontrol ved montage i bygninger, hvor driften "
       "kørte videre.")]),

    ("Elektromekaniker / Produktionsteamleder",
     "ARJ Engineering · Teheran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · skiftplanlægning, materialestyring og lager",
     [("Produktionsteam",
       "skiftplanlægning, materialestyring og målopfølgning."),
      ("Teknisk problemløsning",
       "reparation og diagnosticering af elektriske og mekaniske systemer gennem struktureret "
       "root cause-analyse.")]),
]

EDUCATION = [
    ("B.Tech (EQF niveau 6) — Technology Management & Mechanical Engineering",
     "Maskinmesterskolen / Copenhagen School of Marine Engineering & Technology Management · 2017 – 2022 · "
     "karakter 7,6/12"),
    ("Elektrisk & mekanisk design, el-ingeniør (EQF niveau 6)",
     "Tehran Technical University · 2000 – 2003"),
    ("HF — matematik og fysik",
     "VUC · 2012 – 2017"),
]

CERTS = [
    ("Elautoriseret maskinmester (LV/MV/HV)",
     "Sikkerhedsstyrelsen · maj 2023"),
    ("Køle- og HVAC-teknik (AMU)",
     "Mercantec · mar. 2021"),
    ("Arbejdsmiljø §16 og sikkerhedsbevidsthed (VI/6-1)",
     "Søfartsstyrelsen · maj 2021"),
    ("Lean — værdistrømsanalyse, standardarbejde, 5S, A3 og Kaizen",
     "Anvendt i drift · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og projekter · 2017 – nu"),
    ("STCW — maskinrumsvagt (A-III/1), skibssikkerhedsofficer (VI/5)",
     "Søfartsstyrelsen · 2021 – 2023"),
]

LANGUAGES = "Dansk (modersmål) · Engelsk (professionelt, skriftligt og mundtligt) · Persisk/farsi · Kørekort B"

REFERENCES = "Tidligere ledere hos Biofos (Lynetten) og Novo Nordisk A/S (Kalundborg) — oplyses ved henvendelse."

KEYWORDS = (
    "Technical Supervisor · Teknisk Supervisor · Teknisk Drift · Ejendomsdrift · Facility Management · "
    "GWS Segment · Bygninger · Installationer · Tekniske Installationer · El · VVS · Ventilation · Fejlfinding · "
    "Forebyggende Vedligehold · Afhjælpende Vedligehold · Vedligeholdsplan · Vedligehold · Underleverandører · "
    "Leverandører · Teknikere · Tilsyn · Koordinering · Tekniske Runderinger · Runderinger · Registrere Opgaver · "
    "Systemer · Kundekontakt · Kommunikation · Sikkerhed · Lovkrav · Myndighedskrav · KPI · KPI-Rapportering · "
    "Forbedringer · Optimeringer · Selvstændig · Løsningsorienteret · Struktureret · Overblik · Ansvar · Tillid · "
    "Samarbejde · Contract Manager · Kørekort B · Dansk · Engelsk · København · Sjælland · Sites · Lokationer · "
    "Stabil Drift · Oppetid · Arbejdsmiljø · Dokumentation · CMMS · SAP · ERP · Power BI · Excel · Python · AI"
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
        m.bullet(label, body, after=40)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=80)

    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "FAGLIG PROFIL")
    m.para(PROFILE, after=80)

    m.section("TEKNISK DRIFT, SITES OG KUNDE — BEVIS, IKKE PÅSTANDE")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("FAGLIGE OMRÅDER & VÆRKTØJER — ANVENDT I PRAKSIS",
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
    for t, meta in CERTS:
        m.edu(t, meta)

    m.section("SPROG")
    m.para(LANGUAGES, after=80, justify=False)

    m.section("REFERENCER")
    m.para(REFERENCES, after=80, justify=False)

    m.section("KERNEKOMPETENCER & NØGLEORD")
    m.para(KEYWORDS, after=80)

    m.models_table("FØRSTE 90 DAGE — SÅDAN TAGER JEG OVER",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    return m.save(path,
                  title="Ansøgning og CV — Technical Supervisor, CBRE Global Workplace Solutions",
                  subject="Teknisk drift · multi-site · underleverandører · KPI · el, VVS og ventilation · "
                          "København",
                  keywords=("technical supervisor, teknisk drift, ejendomsdrift, facility management, "
                            "installationer, el, vvs, ventilation, fejlfinding, forebyggende vedligehold, "
                            "underleverandører, kpi, dokumentation, dansk, engelsk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1, CV side 2-4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_CBRE_TechnicalSupervisor.docx")
    print("OK", build(out))
