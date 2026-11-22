# -*- coding: utf-8 -*-
"""Multi Køl & Energi — Salgshjælp til DataCenterGruppen.
Opgavefokuseret ansøgning og evidensbaseret CV i masterdesign.
Skelner mellem dokumenteret HVAC/ventilation, tilbudsarbejde og UPS-/el-erfaring
på den ene side og ikke-dokumenteret datacenterkøling på den anden.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")
OUTPUT = os.path.join(ROOT, "Shahram_Ajloo_MultiKoel_DataCenter_Salgshjaelp.docx")
NAME = "SHAHRAM AJLOO"
TITLE = "Maskinmester · køling · teknisk salg og tilbud"
CONTACT = "+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv"
DATE = "3. november 2026"

LETTER = [
    "Salgshjælp til DataCenterGruppen handler om mere end en pris på køleudstyr til datacentre. Det skal vise, at kundens driftsbehov, tekniske forudsætninger, el- og nødstrømsgrænseflader, leveranceomfang og økonomi er forstået — og gøre det tydeligt, hvad løsningen løser, og hvilke antagelser den bygger på.",
    "En fast tilbudsproces kan begynde med en kort teknisk afklaring: Hvad er belastningen og driftsprofilen? Hvilke temperaturer og hvor meget varme skal kølingen håndtere? Hvad er kundens krav til redundans, vedligehold og fremtidig udvidelse? Hvilke eksisterende installationer, el-forsyning og nødstrøm skal den spille sammen med? Spørgsmål, der kræver specialviden om et produkt eller et anlæg, afklares med de rette kolleger og leverandører, før beregningen låses.",
    "Tilbuddet bør samle beregningsforudsætninger, løsningsvalg og tekniske data med pris, leverancegrænser, optioner, tidsplan, idriftsættelse og forbehold. Hvor der er flere realistiske valg, kan kunden få et sammenligneligt grundlag for investering, drift og service — ikke blot flere linjer i et katalog. En intern teknisk og kommerciel gennemgang inden afsendelse sikrer, at omfang, indkøb, leverandørpriser og dækningsbidrag hænger sammen.",
    "Teknisk rådgivning skal være tydelig og rettidig: Når kunden spørger ind til løsningen, skal svaret være præcist, og eventuelle åbne punkter have en ejer og en aftalt tilbagemelding. Det tætte kundesamarbejde fortsætter efter tilbuddet. Den samme disciplin gælder rådgivende ingeniørers forespørgsler og udbudsmateriale: registrér krav, afklar afvigelser, dokumentér beregninger og følg ændringer frem til den endelige pris. Efter aflevering kan erfaringer fra udførelse og drift føres tilbage til beregningsgrundlag, tilbudsskabeloner og næste kundedialog.",
    "I de første 30 dage bør tilbudshistorik, produktdata, beregningsværktøjer og salgs-/teknikgrænseflader gennemgås med DataCenterGruppen. Inden dag 60 kan en ensartet krav- og tilbudscheckliste bruges på nye forespørgsler; inden dag 90 kan teamet evaluere åbne tilbud, gentagne tekniske spørgsmål og feedback fra kunder og kolleger og vælge de næste forbedringer. Det placerer salgsstøtten som en central rolle, hvor teknik, salg og kundekontakt går hånd i hånd. I et stærkt fagligt miljø og tæt samarbejde mellem kolleger kan teamet kvalificere spændende tekniske løsninger indenfor køling og skabe mulighed for faglig udvikling gennem konkrete tilbud og leverancer. Kritisk infrastruktur vurderes fortsat på driftssikkerhed, oppetid og dokumenterede forudsætninger."
]

PROFILE = (
    "Elautoriseret maskinmester (LV/MV/HV) med køleteknisk efteruddannelse, praktisk HVAC- og "
    "ventilationserfaring samt kommercielt ansvar for tekniske tilbud og leverancer. ELOHVAC: "
    "tilbud, beregninger, prissætning, fuldt P&L og service/installation på el-, ventilations- og "
    "klimaanlæg. Ventek-Air: ventilationsprojektering/dimensionering og 11 samtidige anlægsprojekter. "
    "Novo Nordisk: 37 CAPEX-projekter, idriftsættelse, BMS/FMS og UPS-relaterede el-systemer. "
    "Datacenterkøling eller datacenterspecifikke køleanlægsberegninger er ikke dokumenteret; erfaringen "
    "med HVAC, kritisk drift, nødstrømsgrænseflader og kommerciel tilbudsgivning er den relevante bro."
)

MATRIX = [
    ("Teknisk baggrund som maskinmester eller tilsvarende", "B.Tech i Technology Management & Mechanical Engineering og dansk autorisation som elautoriseret maskinmester (LV/MV/HV). Hertil el- og maskinteknisk design samt AMU i køleteknik og klimaanlæg."),
    ("Teknisk forståelse og erfaring inden for køling", "AMU i køleteknik/klimaanlæg; ELOHVAC: installation, fejlfinding og forebyggende vedligehold på ventilations- og klimaanlæg. Ventek-Air: projektering/dimensionering af ventilation/klima. Erfaring med konkrete datacenterkølesystemer er ikke dokumenteret."),
    ("Beregning og udarbejdelse af tekniske løsninger til køling og datacentre", "ELOHVAC: tekniske tilbud, beregninger og løsningsvalg på el-, ventilations- og klimaleverancer. Ventek-Air: ventilationsprojektering/dimensionering på 11 samtidige anlægsprojekter. Datacenterspecifikke beregninger for køleanlæg, belastningsprofiler og kølesystemplatforme fremgår ikke af kildematerialet."),
    ("Forståelse for el og nødstrøm", "Elautoriseret maskinmester LV/MV/HV; ELOHVAC elinstallationer, tavler og styring. Novo Nordisk: el-systemer, tavler, UPS og CAPEX-idriftsættelse. Generatorer eller drift af komplette datacenter-nødstrømsanlæg påstås ikke."),
    ("Prissætning af tekniske løsninger og udbudsmateriale", "ELOHVAC: tilbud, beregninger, prissætning og fuldt P&L-ansvar. Ventek-Air: tilbud, udbud, specifikationer og aftalegrundlag på ventilationsprojekter. Novo Nordisk: økonomi- og risikostyring af 37 CAPEX-projekter à DKK 2–10 mio."),
    ("Udarbejde tilbud og besvare konkrete kundeforespørgsler", "ELOHVAC: kundevendte tekniske tilbud og servicehenvendelser fra afklaring til udførelse og aflevering. Kandidaten har generelt bekræftet teknisk support på tværs af kanaler, men konkrete kundetal og tilbudsresultater er ikke oplyst."),
    ("Sparring med kolleger om tekniske løsninger og tilbud", "ELOHVAC: teknisk sparring og daglig opgaveplanlægning med fem elektrikere og tre lærlinge; Ventek-Air: koordinering af 14-personers team og 11 samtidige projekter. Novo Nordisk: koordinering med 25 specialister på tværs af engineering, indkøb og site."),
    ("Kundekontakt, kundepleje og teknisk salg", "ELOHVAC: erhvervskundedialog, tilbud, service og fuldt P&L. Kandidaten har bekræftet generel erfaring med kundeudvikling, nysalg og leverandørdialog; specifikke salgsvolumener, datacenterkunder og markedsandele er ikke oplyst."),
    ("Deltagelse på datacentermesser og branchearrangementer", "Kundemøder, leverandørdialog og tværfaglig teknisk kommunikation er dokumenteret på tværs af ELOHVAC, Ventek-Air og Novo Nordisk. Konkret datacentermesse- eller branchearrangementserfaring er ikke angivet og påstås ikke."),
    ("Bidrage til udvikling af løsninger og tilbudsarbejde", "ELOHVAC: fuldt P&L, tilbudsberegning, KS-tjeklister, KPI-rapportering og digitale arbejdsgange med over 40 % dokumenteret produktivitetsløft i egne processer. Forbedringen er ikke et salgsresultat eller et DataCenterGruppen-resultat."),
    ("Forståelse for kritisk infrastruktur, oppetid og driftssikkerhed", "BIOFOS/Lynetten: kritisk døgnbemandet procesdrift, pumper, HVAC, højspændingstavler og SCADA. Novo Nordisk: regulerede produktionsmiljøer, UPS-relaterede el-systemer, commissioning og nul kritiske fund ved aflevering. Det er beslægtet drifts-/projektarbejde, ikke datacentererfaring."),
    ("Kommunikation på dansk og engelsk", "Dansk modersmål og engelsk professionelt i skrift og tale; teknisk kundedialog, projektkoordinering, leverandørkontakt og ledelsesrapportering er dokumenteret."),
]

EXPERIENCE = [
    ("Ejer / teknisk direktør / elautoriseret maskinmester", "ELOHVAC ApS · København · maj 2023–nu", "5 elektrikere + 3 lærlinge · fuldt P&L-ansvar", [
        "Udarbejder tilbud og beregninger; prissætter og planlægger tekniske leverancer fra materialer og underentreprenører til installation, KS og aflevering.",
        "Kundevendt arbejde med service, installation, tavler, styring, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg.",
        "Python/Claude-værktøjer til tilbud, tidsplaner, KS-tjeklister og KPI-rapportering gav dokumenteret produktivitetsløft over 40 % i egne arbejdsgange."
    ]),
    ("Medejer og CTO / teknisk ansvarlig for AI-afdelingen", "Data Power Consultant ApS · København · 2024–2026 (sideløbende med ELOHVAC)", "Tekniske og industrielle applikationer", [
        "Ledte kundeløsninger fra behovsafklaring og integration til idriftsættelse, dokumentation og overdragelse; arbejdede med LLM-API'er og AI-agenter.",
        "Indførte fælles standarder for AI-assisteret udvikling, review og test; anvendte AI i ledelsesrapportering og matrixledelse."
    ]),
    ("Senior idriftsættelsesingeniør / projektleder, elsystem", "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024", "37 CAPEX-projekter · 25 specialister · DKK 2–10 mio. pr. projekt", [
        "Koordinerede scope, fremdrift, økonomi, risici og ressourcer; SAP ERP, teknisk dokumentation, FAT/SAT og IQ/OQ/PQ.",
        "Arbejdede med el-tavler, styring, UPS og BMS/FMS i daglig drift og projekter; commissioning uden kritiske fund ved aflevering."
    ]),
    ("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022", "11 samtidige ventilationsprojekter · 14-personers team", [
        "Ventilationsprojektering/dimensionering og projekter fra specifikation til aflevering; tilbud, udbud, kapacitetsplanlægning og koordinering af teknikere og underentreprenører."
    ]),
    ("Vedligeholdelses- og driftsleder / værkstedstekniker", "BIOFOS, Lynetten · København · aug. 2017–jan. 2022", "Kritisk døgnbemandet procesdrift", [
        "Forebyggende vedligehold og akut fejlfinding på pumper, HVAC, højspændingstavler og øvrigt el-/mekanisk udstyr; SCADA-overvågning.",
        "Skifteholdsdrift med LOTO, APV, risikovurdering og nærved-hændelser; 5S, Standard Work, PDCA og reservedelsflow."
    ]),
    ("Elektromekaniker / produktionsteamleder", "ARJ Engineering · Teheran · dec. 2003–mar. 2010", "12 mekanikere og teknikere", [
        "Fejldiagnosticerede og reparerede industrielle el- og mekaniske anlæg; stod for vagtplanlægning, materialestyring og korrigerende handlinger."
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
    ("Køl, klima og HVAC", "AMU køleteknik/klimaanlæg · Ventek-Air ventilationsprojektering/dimensionering · ELOHVAC klima-/ventilationsservice"),
    ("El og nødstrøm", "Elautorisation LV/MV/HV · tavler og styring · UPS-relaterede el-systemer hos Novo Nordisk · ingen generatorerfaring påstås"),
    ("Tilbud og projektøkonomi", "ELOHVAC fuldt P&L · tilbud/beregninger/prissætning · Ventek-Air udbud · Novo 37 CAPEX-projekter/SAP ERP"),
    ("Commissioning og dokumentation", "FAT/SAT · IQ/OQ/PQ · BMS/FMS-verifikation · KS-tjeklister · afleveringsdokumentation"),
    ("Digitale værktøjer", "SAP ERP · Excel/Power Query · Power BI · Python · Claude API · KPI-rapportering"),
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
    m.meta("Multi Køl & Energi A/S · DataCenterGruppen · att. Per Ronald Jørgensen")
    p = m._p(spacing_after=50, line=240, justify=False)
    m._run(p, "Kort motiveret ansøgning · tekniske beregninger og kundeløsninger", bold=True)
    m.para("Kære Per Ronald Jørgensen,", after=25, justify=False)
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
    m.resume_header(NAME, "Maskinmester · køleteknik · teknisk tilbudsarbejde", CONTACT, "ERHVERVSERFARING")
    add_jobs(m, EXPERIENCE)
    m.section("UDDANNELSE OG CERTIFICERING")
    for title, detail in EDUCATION:
        m.edu(title, detail)
    m.section("ARBEJDSFORMER OG DIGITALE VÆRKTØJER")
    m.models_table("RELEVANTE VÆRKTØJER", ("Område", "Dokumenteret anvendelse"), TOOLS,
                   widths=(2700, 7646), compact=True)
    return m.save(path, title="Kort ansøgning og CV — Multi Køl, DataCenterGruppen, salgshjælp",
                  subject="Maskinmester · køling · datacentre · beregning · tilbud · teknisk salg",
                  keywords="Maskinmester; Multi Køl; DataCenterGruppen; køling; datacenter; UPS; nødstrøm; teknisk salg; beregning; tilbud; prissætning")


if __name__ == "__main__":
    print(build())
