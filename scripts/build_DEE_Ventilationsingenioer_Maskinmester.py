# -*- coding: utf-8 -*-
"""DEE Teknisk rådgivning — ventilation, projektering og commissioning.
Jobfokuseret ansøgning først; kandidatens evidens og grænser i CV'et.
Skelner mellem dokumenteret ventilationsprojektering/dimensionering, Revit-erfaring
(ikke dokumenteret i CV-kilden) og overførbar commissioning-/kvalitetserfaring.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")
OUTPUT = os.path.join(ROOT, "Shahram_Ajloo_DEE_Ventilationsingenioer_Maskinmester.docx")
NAME = "SHAHRAM AJLOO"
TITLE = "Maskinmester · ventilation · projektering og commissioning"
CONTACT = "+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv"
DATE = "3. november 2026"

LETTER = [
    "Et ventilationsprojekt er først færdigt, når den projekterede løsning kan bygges, indreguleres og fungere i drift. Det kræver, at luftmængder, trykforhold og energiforbrug hænger sammen med ventilation, VVS, varme, køling, CTS/BMS og de øvrige installationer — og at grænsefladerne bliver afklaret, før de bliver til ændringer på byggepladsen.",
    "En robust projektstart samler bygherrens behov, eksisterende forhold, driftskrav og de tekniske forudsætninger i et fælles grundlag. Beregninger og projektmateriale bør vise forudsætninger og valg, så rådgivere og entreprenører kan granske, prissætte og koordinere løsningen. I Revit/BIM-modellen skal plads, føringsveje, serviceadgang og installationernes indbyrdes afhængigheder gennemgås sammen — ikke først ved montage.",
    "Under udførelsen giver korte, regelmæssige tilsyn størst værdi, når de følger projektets risici: udførelse mod tegninger og specifikationer, adgang til filtre og komponenter, isolering, målepunkter, indreguleringsforudsætninger og ændringer. Afvigelser får en ansvarlig, beslutning og frist; projektmaterialet rettes, når løsningen ændres. Det gør kvalitetssikringen brugbar for både bygherre og udførende.",
    "Commissioning bør planlægges ind fra projekteringen. Aftal testforløb, indregulering og acceptkriterier for luftmængder, tryk, temperaturer, regulering og samspillet mellem ventilation, varme, køling og BMS. Registrér måleresultater, fejl og retest, og afslut med as-built-materiale og en overdragelse, som driftspersonalet kan bruge. Opfølgningen efter idriftsættelse viser, om anlægget faktisk leverer den funktion og energieffektivitet, projektet var dimensioneret til.",
    "I de første uger bør den nye projektansvarlige gennemgå DEE's projektskabeloner, beregningsgrundlag, granskningspraksis og igangværende sager sammen med kollegerne. Inden dag 30 kan ansvar, tekniske beslutninger og grænseflader være tydelige på egne projekter; inden dag 60 kan et projekt have en gennemarbejdet koordinations- og tilsynsplan; inden dag 90 kan commissioning- og afleveringsforløbet være fulgt op med dokumenterede åbne punkter og læring. Det giver plads til frihed under ansvar og indflydelse, samtidig med at et stærkt fagligt miljø og tæt samarbejde fastholdes, og der skabes faglig udvikling på løsninger, der virker i praksis."
]

PROFILE = (
    "Maskinmester med dansk elautorisation (LV/MV/HV), B.Tech i Technology Management & Mechanical "
    "Engineering og praktisk erfaring med ventilations- og klimaprojekter. Hos Ventek-Air havde "
    "ansvar for 11 samtidige anlægsprojekter; mastergrundlaget dokumenterer ventilationsprojektering "
    "og dimensionering i denne rolle. ELOHVAC supplerer med installation, fejlfinding, styring og "
    "vedligehold på el-, ventilations- og klimaanlæg. Hos Novo Nordisk omfattede commissioning- og "
    "projektarbejdet FAT/SAT, IQ/OQ/PQ og BMS/FMS-ændringer. Specifik Revit-erfaring eller "
    "dimensioneringssoftware er ikke navngivet i kildematerialet. Dansk er modersmål, engelsk professionelt; kørekort B."
)

MATRIX = [
    ("Maskinmester, ingeniør eller tilsvarende teknisk baggrund", "B.Tech i Technology Management & Mechanical Engineering samt dansk autorisation som elautoriseret maskinmester (LV/MV/HV). Hertil el- og maskinteknisk design, elteknik, fra Tehran Technical University."),
    ("Solid erfaring med projektering og dimensionering af ventilationsanlæg", "Ventek-Air: masterens bekræftede grundlag angiver projektering og dimensionering af ventilation/klima i rollen som projekt- og værkstedsleder med 11 samtidige anlægsprojekter og 14 medarbejdere. Konkrete beregningssoftware, anlægsstørrelser og dimensioneringsresultater er ikke specificeret."),
    ("Erfaring med eller kendskab til Revit", "Revit er ikke navngivet som anvendt værktøj i master-CV eller de bekræftede kompetencenoter; der fremsættes derfor ingen påstand om Revit-authoring. Dokumenteret projekt-, installations- og koordineringserfaring kan overføres til DEE's modellerings- og reviewproces efter introduktion."),
    ("Samspil mellem ventilation, varme, køling, CTS/BMS og øvrige installationer", "ELOHVAC: el-, ventilations- og klimaanlæg, tavler, styring og service. Maskinmesteruddannelse og AMU i køleteknik/klimaanlæg understøtter varme-/køleforståelse. Novo Nordisk: bekræftet arbejde med BMS/FMS i drift og projekter, herunder ændringer og verifikation; ingen bestemt CTS-platform påstås."),
    ("Selvstændigt ansvar for egne projekter og leverancer", "ELOHVAC: fuldt P&L-ansvar, tilbud og beregninger, planlægning, materialer, underentreprenører, KS og aflevering. Novo Nordisk: scope, fremdrift, økonomi, risiko og ressourcer på 37 CAPEX-projekter."),
    ("Tilsyn, kvalitetssikring eller teknisk granskning", "ELOHVAC: KS-tjeklister, kvalitetsopfølgning og afleveringsdokumentation på tekniske entrepriser. Ventek-Air: projekter fra specifikation til aflevering. Novo Nordisk: FAT/SAT og IQ/OQ/PQ med nul kritiske fund ved aflevering. Omfanget af formelt rådgivertilsyn er ikke særskilt specificeret."),
    ("Dialog med bygherre, entreprenører og samarbejdspartnere", "ELOHVAC: kundedialog, tilbud, leverandører og underentreprenører. Ventek-Air: daglig koordinering af 14-personers team og 11 samtidige projekter. Novo Nordisk: tværfaglig koordinering med 25 specialister på tværs af engineering, indkøb og site."),
    ("Følge projekter fra projektering til udførelse og idriftsættelse", "Ventek-Air dokumenterer ventilationsprojekter fra specifikation til aflevering. Novo Nordisk dokumenterer commissioning og test via FAT/SAT og IQ/OQ/PQ. ELOHVAC følger tekniske installationer fra tilbud/plan til udførelse, KS og overdragelse."),
    ("Beregning af luftmængder, tryktab og energiforhold", "Ventilationsprojektering og dimensionering er bekræftet for Ventek-Air, men CV-kilden specificerer ikke beregningsmetoder, tryktabsberegninger, måledata eller værktøjer. Energiopfølgning er dokumenteret i andre sammenhænge, herunder et PDCA-program hos Novo Nordisk med 40 % lavere energiomkostninger dér; det præsenteres ikke som DEE-resultat."),
    ("Udarbejdelse og granskning af projektmateriale", "ELOHVAC: beregninger, tilbud, KS-tjeklister og afleveringsmateriale. Ventek-Air: tilbud, specifikationer, underentreprenører og afleveringspakker. Novo Nordisk: sporbar test- og valideringsdokumentation. Revit-tegninger eller rådgiverprojektmateriale er ikke hævdet."),
    ("Commissioning, test og idriftsættelse", "Novo Nordisk: idriftsættelsesingeniør og projektleder på el-systemer, FAT/SAT, IQ/OQ/PQ og nul kritiske fund ved aflevering. ELOHVAC: test og aflevering af tekniske installationer. Commissioning-erfaringen er tværfaglig/elektrisk og ikke præsenteret som aleneansvar for ventilationscommissioning."),
    ("Kørekort og praktisk samarbejde på byggepladser", "Kørekort B (manuelt gear) er dokumenteret. ELOHVAC og Ventek-Air omfatter praktisk koordinering med udførende og underentreprenører. Bopæl er Måløv; fremmøde og eventuel flytning i forbindelse med Støvring er ikke aftalt."),
]

EXPERIENCE = [
    ("Ejer / teknisk direktør / elautoriseret maskinmester", "ELOHVAC ApS · København · maj 2023–nu", "5 elektrikere + 3 lærlinge · fuldt P&L-ansvar", [
        "Tilbud, beregninger, planlægning, materialer og underentreprenører; installation, tavler, styring, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg.",
        "Kvalitetssikring, LOTO, APV og risikovurdering; opfølgning på kunde, udførelse og afleveringsdokumentation.",
        "Python/Claude-værktøjer til tilbud, tidsplaner, KS-tjeklister og KPI-rapportering gav dokumenteret produktivitetsløft over 40 % i egne arbejdsgange."
    ]),
    ("Medejer og CTO / teknisk ansvarlig for AI-afdelingen", "Data Power Consultant ApS · København · 2024–2026 (sideløbende med ELOHVAC)", "Tekniske og industrielle applikationer", [
        "Ledte kundeløsninger fra behovsafklaring og integration til idriftsættelse, dokumentation og overdragelse; arbejdede med LLM-API'er og AI-agenter.",
        "Indførte fælles standarder for AI-assisteret udvikling, review og test; anvendte AI i ledelsesrapportering og matrixledelse."
    ]),
    ("Senior idriftsættelsesingeniør / projektleder, elsystem", "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024", "37 CAPEX-projekter · 25 specialister · DKK 2–10 mio. pr. projekt", [
        "Koordinerede scope, fremdrift, økonomi, risici og ressourcer på tværs af engineering, indkøb og anlæg; fulgte data i SAP ERP.",
        "Commissioning af el-systemer, FAT/SAT, IQ/OQ/PQ og BMS/FMS-ændringer i drift og projekter; nul kritiske fund ved aflevering. PDCA-program reducerede energiomkostninger med 40 % i den pågældende organisation."
    ]),
    ("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022", "11 samtidige ventilationsprojekter · 14-personers team", [
        "Projektering og dimensionering af ventilations-/klimaanlæg i projektleverancen; ledte projekter fra specifikation til aflevering med daglige tavlemøder, kapacitetsplanlægning og underentreprenørkoordinering.",
        "Tilbud, specifikationer, materialer, udførelse, kvalitet og afleveringspakker på tværs af samtidige opgaver."
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
    ("Ventilation og HVAC", "Ventilationsprojektering/-dimensionering (Ventek-Air) · ventilation/klima-installation og fejlfinding (ELOHVAC) · køleteknik/klimaanlæg (AMU)"),
    ("Commissioning og kvalitet", "FAT/SAT · IQ/OQ/PQ · BMS/FMS-ændringer og verifikation · KS-tjeklister · afleveringsdokumentation"),
    ("Projektøkonomi og koordinering", "PRINCE2 · 37 CAPEX-projekter · 11 samtidige ventilationsprojekter · tilbud, P&L, ressourcer, leverandører og underentreprenører"),
    ("Data og værktøjer", "SAP ERP · Excel/Power Query · Power BI · Python · Claude API · KPI-rapportering"),
    ("BIM og beregningssoftware", "Revit/MagiCAD eller HVAC-beregningsplatform er ikke navngivet i det dokumenterede erfaringsgrundlag; ingen platformskompetence påstås."),
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
    m.meta("DEE Teknisk rådgivning · att. Palle Gudum · Ventilationsingeniør/maskinmester")
    p = m._p(spacing_after=50, line=240, justify=False)
    m._run(p, "Ansøgning · projektering, udførelse og commissioning", bold=True)
    m.para("Kære Palle Gudum og DEE,", after=25, justify=False)
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
    m.resume_header(NAME, "Maskinmester · ventilation · teknisk projektleverance", CONTACT, "ERHVERVSERFARING")
    add_jobs(m, EXPERIENCE)
    m.section("UDDANNELSE OG CERTIFICERING")
    for title, detail in EDUCATION:
        m.edu(title, detail)
    m.section("ARBEJDSFORMER OG DIGITALE VÆRKTØJER")
    m.models_table("RELEVANTE VÆRKTØJER", ("Område", "Dokumenteret anvendelse"), TOOLS,
                   widths=(2700, 7646), compact=True)
    return m.save(path, title="Ansøgning og CV — DEE Teknisk rådgivning, ventilationsingeniør/maskinmester",
                  subject="Ventilation · projektering · commissioning · tekniske installationer",
                  keywords="Ventilationsingeniør; maskinmester; DEE; ventilation; projektering; dimensionering; commissioning; Revit; HVAC; BMS; VVS")


if __name__ == "__main__":
    print(build())
