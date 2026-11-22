# -*- coding: utf-8 -*-
"""Terotech A/S — Engageret og innovativ vedligeholdelsesingeniør.
Jobfokuseret ansøgning først og evidensbaseret CV i masterdesign.
Afgrænser CMMS/masterdata- og asset-arbejde, dokumenteret vedligehold og
FMEA-praksis fra formel RCM/FMECA-facilitering og Terotech-kundeleverancer.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")
OUTPUT = os.path.join(ROOT, "Shahram_Ajloo_Terotech_Vedligeholdelsesingenioer.docx")
NAME = "SHAHRAM AJLOO"
TITLE = "Maskinmester · vedligehold · data og asset management"
CONTACT = "+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv"
DATE = "3. november 2026"

LETTER = [
    "En vedligeholdelsesplan bliver først værdifuld, når data, arbejdsopgaver og reservedele hænger sammen i driften. Hvis anlægsregisteret ikke svarer til det, teknikeren møder på stedet, eller hvis fejl og arbejdsordrer ikke kan kobles til den rigtige komponent, bliver selv en veldesignet plan svær at gennemføre og forbedre.",
    "En praktisk start på et Maintenance & Data Excellence-projekt er at afgrænse anlægsstruktur og datakilder sammen med kunden: funktionel placering, udstyr, kritikalitet, fejl- og arbejdshistorik, vedligeholdsopgaver, styklister, reservedelsforbrug og leverandørdata. Masterdata: hvert felt får en definition, en kilde og en ansvarlig; tekniske input fra drift og leverandører afklares, før data ændres. Datakvalitet afprøves mod udstyret og vedligeholdspersonalet — manglende eller modstridende oplysninger markeres som usikkerhed, ikke udfyldes med gæt.",
    "Vedligeholdsanalyser bør derefter forbinde fejlmåder og konsekvenser med den opgave, der faktisk reducerer risikoen. RCM/FMECA-arbejde kræver en fælles systemafgrænsning, realistiske driftsdata og deltagelse fra dem, der kender anlægget. Resultatet skal kunne føres ind i kundens CMMS/ERP som ansvar, opgave, interval, materialer og dokumentation — og følges op på gentagne fejl, planopfyldelse og reservedelstilgængelighed. Workshopbeslutninger, antagelser og åbne spørgsmål skal kunne genfindes bagefter.",
    "Ved ad-hoc support kan den samme grundstruktur hjælpe kunden hurtigt: afklar anlæg og symptom, se på historik og stamdata, find næste sikre handling, og registrér hvad der blev ændret. Når mønstret går igen, bliver enkeltsagen til en forbedring af data, plan eller reservedelsopsætning. Det gør systemviden, maskinviden og vedligeholdsteori anvendelige sammen i stedet for at behandle dem som adskilte fag.",
    "De første 30 dage bør bruges på at lære Terotechs metode, kundernes ERP/CMMS-miljøer og den måde drift og vedligehold arbejder på. Inden dag 60 kan en afgrænset datagennemgang og analyse af fejl- eller reservedelsdata være valideret med kunden; inden dag 90 kan ét prioriteret forbedringsforslag være implementeret, dokumenteret og overdraget med opfølgning aftalt. Nysgerrighed, åbenhed, empati, tillid og integritet bliver synlige i måden datausikkerhed, risici og anbefalinger deles på. Det understøtter Terotechs ambition om at gøre kunderne world class inden for operationel asset management."
]

PROFILE = (
    "Elautoriseret maskinmester (LV/MV/HV) med næsten 4½ års kritisk 24/7-drift og vedligehold hos "
    "BIOFOS/Lynetten, suppleret af teknisk service, projekter og dataarbejde. Har arbejdet med "
    "forebyggende vedligehold, akut fejlfinding, kritikalitet, SCADA, pumper, HVAC, reservedelsflow, "
    "SAP ERP og CMMS-principper. ELOHVAC giver kunde- og leverandørvendt teknisk service samt fuldt "
    "P&L; Novo Nordisk giver 37 CAPEX-projekter, dokumentation og tværfaglig koordinering. Praktisk "
    "FMEA, 5xHvorfor, Ishikawa, A3, PDCA og 5S er anvendt; formel RCM/FMECA-facilitering og "
    "kundespecifik master data-optimering er ikke dokumenteret."
)

MATRIX = [
    ("Teknisk relevant uddannelse som maskinmester eller ingeniør", "B.Tech i Technology Management & Mechanical Engineering samt dansk autorisation som elautoriseret maskinmester (LV/MV/HV). Hertil el- og maskinteknisk design, elteknik."),
    ("Vedligeholdsoptimering i forskellige industrier",  "BIOFOS/Lynetten: næsten 4½ år i kritisk døgnbemandet procesdrift med forebyggende vedligehold, akut fejlfinding, kritikalitet, SCADA, pumper, HVAC og højspændingstavler. Samlet asset management-ejerskab på tværs af flere kundeanlæg er ikke påstået."),
    ("Master Data-optimering direkte i kundens ERP-system", "SAP ERP er anvendt hos Novo Nordisk til økonomi, aktiver og omkostningsopfølgning; Excel/Power Query, Power BI og Python bruges til dataanalyse. Et konkret kundemasterdata-oprydningsprojekt eller kundens ERP-platform er ikke dokumenteret."),
    ("Maintenance & Data Excellence-projekter", "Novo Nordisk: koordinering af 37 CAPEX-projekter, 25 specialister, risici, økonomi og data i SAP ERP. BIOFOS: forebyggende vedligehold og reservedelsflow. Vedligeholdsdata-optimering hos en ekstern kunde er ikke særskilt dokumenteret."),
    ("Ad-hoc CMMS-support og opdatering af vedligeholdsdata", "Generel CMMS-erfaring står i kandidatens kompetencegrundlag, men intet bestemt CMMS-system er navngivet. BIOFOS dokumenterer vedligehold, arbejdspraksis og reservedelsflow; ELOHVAC dokumenterer kundevendt teknisk fejlfinding og opfølgning."),
    ("Vedligeholdelsesanalyser og implementering af vedligeholdelsesplaner", "BIOFOS: forebyggende vedligehold, kritikalitetsforståelse, 5S, Standard Work, PDCA og reservedelsflow. ELOHVAC: planlagt service og opfølgning. Selvstændig udarbejdelse og implementering af en fuld kundes vedligeholdsplan er ikke specificeret."),
    ("Reservedelsstrategier og reservedelsdata", "BIOFOS: reservedelsflow og lagerstyring i kritisk procesdrift; ARJ: materialestyring; ELOHVAC: materialer og indkøb som del af egne service-/entrepriseleverancer. Formelt reservedelsstrategiprojekt hos kunde er ikke dokumenteret."),
    ("Eksekvering og facilitering af RCM/FMECA-pålidelighedsstudier", "Praktisk FMEA, kritikalitetsvurdering, 5xHvorfor, Ishikawa og A3 er angivet i kompetencegrundlaget. Formelt RCM- eller FMECA-studie, certificering eller facilitering af kundeworkshops er ikke dokumenteret; dette skal læres efter Terotechs metode."),
    ("Facilitering af møder og workshops", "Ventek-Air: daglige tavlemøder, flaskehalsanalyse og koordinering af et 14-personers team. Novo Nordisk: tværfaglig koordinering af 25 specialister. Facilitering af kundeworkshops eller RCM/FMECA-workshops er ikke dokumenteret."),
    ("Teknisk support til kunder og afklaring med leverandører", "ELOHVAC: kundevendt service, fejlfinding, tilbud, underentreprenør- og leverandørdialog. Kandidaten har generelt bekræftet teknisk support, kundeservice og leverandørdialog, men konkrete CMMS-supportsager eller Terotech-kunder er ikke tilskrevet."),
    ("Projektledelse, rådgivning og implementering", "ELOHVAC: fuldt P&L, tilbud, planlægning, koordinering, kvalitet og aflevering. Novo Nordisk: 37 CAPEX-projekter med 25 specialister. Rådgivning om asset management i konsulenthus er ikke tidligere ansættelse."),
    ("Struktureret dataanalyse til beslutninger og rådgivning på dansk og engelsk",  "SCADA-/målerdata, SAP ERP, Excel/Power Query, Power BI og Python er dokumenteret. Novo Nordisk PDCA-program reducerede energiomkostninger med 40 % i den pågældende organisation; resultatet tilskrives ikke Terotech-kunder."),
    ("Skriftlig formidling, undervisning og træning på dansk og engelsk", "Dansk modersmål og engelsk professionelt. ELOHVAC: oplæring og daglig ledelse af fem elektrikere og tre lærlinge; dokumentation, KS-tjeklister og afleveringsmateriale. Ekstern kundetræning i CMMS/RCM er ikke dokumenteret."),
]

EXPERIENCE = [
    ("Ejer / teknisk direktør / elautoriseret maskinmester", "ELOHVAC ApS · København · maj 2023–nu", "5 elektrikere + 3 lærlinge · fuldt P&L-ansvar", [
        "Planlægger el-tekniske service- og entrepriseopgaver: tilbud, materialer, underentreprenører, udførelse, kvalitet og aflevering.",
        "Fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg; LOTO, APV og risikovurdering ved pladsopstart.",
        "Python/Claude-værktøjer til tilbud, tidsplaner, KS-tjeklister og KPI-rapportering gav dokumenteret produktivitetsløft over 40 % i egne arbejdsgange."
    ]),
    ("Medejer og CTO / teknisk ansvarlig for AI-afdelingen", "Data Power Consultant ApS · København · 2024–2026 (sideløbende med ELOHVAC)", "Tekniske og industrielle applikationer", [
        "Ledte kundeløsninger fra behovsafklaring og integration til idriftsættelse, dokumentation og overdragelse; LLM-API'er og AI-agenter.",
        "Indførte fælles standarder for AI-assisteret udvikling, review og test; anvendte AI i ledelsesrapportering og matrixledelse."
    ]),
    ("Senior idriftsættelsesingeniør / projektleder, elsystem", "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024", "37 CAPEX-projekter · 25 specialister · DKK 2–10 mio. pr. projekt", [
        "Koordinerede scope, fremdrift, økonomi, risici og ressourcer på tværs af engineering, indkøb og anlæg; SAP ERP.",
        "FAT/SAT, IQ/OQ/PQ og sporbar teknisk dokumentation med nul kritiske fund ved aflevering; PDCA-program reducerede energiomkostninger med 40 % i den pågældende organisation."
    ]),
    ("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022", "11 samtidige anlægsprojekter · 14-personers team", [
        "Kapacitets- og fremdriftsstyring, tilbud/udbud, materialer, underentreprenører, kvalitet og afleveringspakker; daglige tavlemøder og flaskehalsanalyse."
    ]),
    ("Vedligeholdelses- og driftsleder / værkstedstekniker", "BIOFOS, Lynetten · København · aug. 2017–jan. 2022", "Kritisk døgnbemandet procesdrift", [
        "Forebyggende vedligehold og akut fejlfinding på pumper, HVAC, højspændingstavler og øvrigt el-/mekanisk udstyr; SCADA-overvågning.",
        "Reservedelsflow, 5S, Standard Work og PDCA; skifteholdsdrift med LOTO, APV, risikovurdering og nærved-hændelser."
    ]),
    ("Elektromekaniker / produktionsteamleder", "ARJ Engineering · Teheran · dec. 2003–mar. 2010", "12 mekanikere og teknikere", [
        "Fejldiagnosticerede og reparerede industrielle el- og mekaniske anlæg; materialestyring, vagtplanlægning og korrigerende handlinger."
    ]),
]

EDUCATION = [
    ("B.Tech, Technology Management & Mechanical Engineering", "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · EQF 6"),
    ("El- og maskinteknisk design, elteknik", "Tehran Technical University · 2000–2003 · EQF 6"),
    ("Elautoriseret maskinmester (LV/MV/HV)", "Sikkerhedsstyrelsen · maj 2023"),
    ("Køleteknik og klimaanlæg (AMU)", "Mercantec · 2021"),
    ("PRINCE2-certificeret projektleder", "AXELOS / PeopleCert"),
    ("HF, matematik og fysik", "VUC · 2012–2017"),
]

TOOLS = [
    ("Vedligehold og asset", "Kritikalitet · forebyggende vedligehold · reservedelsflow · Standard Work · 5S · PDCA"),
    ("Reliability og problemløsning", "FMEA i praksis · A3 · 5xHvorfor · Ishikawa · risikovurdering; ingen formel RCM/FMECA-certificering påstås"),
    ("Data og systemer", "SAP ERP · generel CMMS-erfaring (platform ikke navngivet) · Excel/Power Query · Power BI · Python · Claude API"),
    ("Projekt og dokumentation", "PRINCE2 · CAPEX · FAT/SAT · IQ/OQ/PQ · KS-tjeklister · teknisk afleveringsdokumentation"),
    ("Sprog og praktisk", "Dansk og persisk/farsi — modersmål · engelsk — professionelt · kørekort B · bopæl Måløv"),
]


def add_jobs(m, jobs):
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope)
        for text in bullets:
            m.bullet("", text, after=12, line=195)


def build(path=OUTPUT):
    m = MasterDoc(TEMPLATE, lang="da-DK")
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta("Terotech A/S · Vedligeholdelsesingeniør · Esbjerg")
    p = m._p(spacing_after=50, line=240, justify=False)
    m._run(p, "Ansøgning · vedligehold, data og pålidelighed", bold=True)
    m.para("Til Terotech A/S,", after=25, justify=False)
    for text in LETTER:
        m.para(text, after=30, line=200)
    m.meta("Med venlig hilsen", after=6)
    m.meta("Shahram Ajloo", after=0)

    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "FAGLIG PROFIL")
    m.para(PROFILE, after=20, line=195)
    m.models_table("KRAV OG DOKUMENTERET ERFARING", ("Krav i opslaget", "Dokumentation / præcisering"), MATRIX,
                   widths=(3400, 6946), compact=True)

    m.page_break()
    m.resume_header(NAME, "Maskinmester · vedligehold · data og pålidelighed", CONTACT, "ERHVERVSERFARING")
    add_jobs(m, EXPERIENCE)
    m.section("UDDANNELSE OG CERTIFICERING")
    for title, detail in EDUCATION:
        m.edu(title, detail)
    m.section("ARBEJDSFORMER OG DIGITALE VÆRKTØJER")
    m.models_table("RELEVANTE VÆRKTØJER", ("Område", "Dokumenteret anvendelse"), TOOLS,
                   widths=(2700, 7646), compact=True)
    return m.save(path, title="Ansøgning og CV — Terotech, vedligeholdelsesingeniør",
                  subject="Vedligehold · asset management · ERP/CMMS · FMEA · data",
                  keywords="Terotech; vedligeholdelsesingeniør; maskinmester; asset management; CMMS; master data; ERP; maintenance; data excellence; RCM; FMECA; FMEA; vedligeholdelsesplaner; reservedele")


if __name__ == "__main__":
    print(build())
