# -*- coding: utf-8 -*-
"""Assens Forsyning — Maskinmester til drift, teknik og automation.
Opgavefokuseret ansøgning først og evidensbaseret CV bagefter.
Dokumenterer BIOFOS-/SCADA- og eldrift; afgrænser konkrete PLC-programmerings-
og SRO-platformpåstande til det, der faktisk står i master-CV'et.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")
OUTPUT = os.path.join(ROOT, "Shahram_Ajloo_AssensForsyning_MaskinmesterAutomation.docx")
NAME = "SHAHRAM AJLOO"
TITLE = "Maskinmester · drift · el og automation"
CONTACT = "+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv"
DATE = "3. november 2026"

LETTER = [
    "Ved rensning af spildevand og håndtering af afløb skal fejlsøgningen begynde både i processen og i styringen. Når pumper, ventiler eller målere giver et forkert signal, skal den fysiske observation sammenholdes med anlægsdata. Assens Forsynings opgave er at få den fysiske observation, PLC/SCADA-data og anlæggets faktiske tilstand til at pege på samme årsag — og derefter få en sikker, dokumenteret løsning tilbage i drift.",
    "Et samlet teknisk overblik kan gøre det lettere at følge anlæggene på tværs af vagter: opdaterede proces- og eltegninger, PLC-/SCADA-funktioner, sekvensbeskrivelser, alarmgrænser, backup, kritiske målere og kendte fejl. Ved en hændelse registreres tidspunkt, alarm, trend, lokal kontrol, udført handling og driftsresultat. Det giver næste vagt et brugbart spor og hjælper med at skelne en enkeltstående hændelse fra et tilbagevendende problem.",
    "For hver gentagen fejl bør drift, el, mekanik og automation sammen afklare årsagen, før der ændres i styringen. En ændring får en tydelig beskrivelse, risikovurdering, testplan og aftalt mulighed for tilbagerulning. Efter test under de aftalte driftsforhold opdateres tegninger, sekvensbeskrivelser og vedligeholdelsessystem, så løsningens virkning kan ses i alarmhistorik, trends og procesdata — ikke kun i en lukket arbejdsordre.",
    "Energi- og forbrugsdata kan kobles til driftstid, belastning og procesbehov for at finde afvigelser, der er værd at undersøge, og pege på konkrete bidrag til grøn omstilling. Tekniske projekter bør følges fra behovsbeskrivelse og projektering til commissioning, overdragelse og efterfølgende optimering. En fælles aflevering med driftskollegerne sikrer, at ændringerne kan betjenes og vedligeholdes i hverdagen.",
    "De første uger bør bruges på at følge vagtskifte, procesforløb, SRO/SCADA-billeder, vedligeholdssystem og sikker arbejdspraksis sammen med erfarne kolleger. Inden dag 30 kan kendte fejl og dokumentationshuller samles; inden dag 60 kan én tilbagevendende fejl eller et energiforbrug undersøges med drift og automation; inden dag 90 kan en afgrænset forbedring testes og evalueres med data. En fast læringsgennemgang kan bygge på åbenhed om afvigelser, anerkendelse af driftskollegernes viden og loyalitet mod aftalte driftsbeslutninger; resultatorienteret opfølgning og fokus på personlig udvikling gør forbedringerne holdbare.",
    "Vagtordningen bør bygge på en tydelig eskalationsvej, kendte sikre tilstande og en kort, konsekvent overlevering mellem vagterne. Dermed kan den tekniske udvikling styrke forsyningens drift uden at skille automation fra processen eller fra de kolleger, der skal bruge løsningen."
]

PROFILE = (
    "Elautoriseret maskinmester (LV/MV/HV) med praktisk baggrund i el, vedligehold og "
    "døgnbemandet procesdrift. På BIOFOS/Lynetten omfattede arbejdet pumper, HVAC, "
    "højspændingstavler, SCADA, forebyggende vedligehold og akut fejlfinding. I ELOHVAC udføres "
    "el-teknisk service på installationer, tavler og styring. Har erfaring med PLC-styrede anlæg "
    "i en teknisk ledelses-/projektkontekst, men konkrete platforme og personligt programmeringsansvar "
    "er ikke specificeret. Supplerer driftsgrundlaget med commissioning, projektkoordinering, "
    "teknisk dokumentation og energi-/forbrugsopfølgning."
)

MATRIX = [
    ("Uddannet maskinmester eller tæt på at være det", "B.Tech i Technology Management & Mechanical Engineering samt dansk elautorisation som elautoriseret maskinmester (LV/MV/HV). Hertil el- og maskinteknisk design, elteknik, fra Tehran Technical University."),
    ("Aktiv del af driftsorganisationen og praktisk fejlfinding", "BIOFOS/Lynetten: næsten 4½ år i kritisk, døgnbemandet procesdrift med pumper, HVAC, højspændingstavler, SCADA, forebyggende vedligehold og akut fejlfinding. ELOHVAC omfatter fortsat praktisk el-service og fejlfinding hos erhvervskunder."),
    ("Udvikling og optimering af SCADA, PLC, styringer og sekvenser", "SCADA-overvågning på BIOFOS er dokumenteret, og kandidaten oplyser erfaring med arbejde omkring PLC-styrede anlæg. Specifik PLC-platform, kodeændringer og selvstændigt programmeringsansvar er ikke fastlagt i CV-grundlaget; de fremstilles ikke som todokumenteret programmering."),
    ("Fejlfinding på tværs af proces, el og automation", "BIOFOS dokumenterer akut fejlfinding på elektriske og mekaniske anlæg, pumper og HVAC i 24/7 drift. ELOHVAC dokumenterer praktisk fejlfinding på elinstallationer, tavler og styring. Kandidaten arbejder inden for elautorisation, sikkerhedsregler og lokale bemyndigelser."),
    ("Alarmer, trends og analyse af driftsdata", "BIOFOS: SCADA-overvågning og akut opfølgning på kritisk procesudstyr. Novo Nordisk: SAP ERP, rapportering af projekt-/energidata og tværfaglig opfølgning. En navngiven SCADA-platform eller specifikt trendanalyseprojekt er ikke identificeret."),
    ("Energi- og forbrugsovervågning samt dokumentation", "Novo Nordisk: PDCA-program reducerede energiomkostninger med 40 % i den pågældende organisation. ELOHVAC: KPI-rapportering, KS-tjeklister og afleveringsdokumentation. Resultatet tilskrives ikke Assens Forsyning."),
    ("Drift og videreudvikling af vedligeholdelsessystem", "BIOFOS: forebyggende vedligehold, reservedelsflow og standardiseret arbejdspraksis. Erfaring med vedligeholdsdata/CMMS indgår i kompetencegrundlaget, men et bestemt systemnavn eller systemejerskab er ikke oplyst."),
    ("Teknisk dokumentation og løbende optimeringer", "ELOHVAC: KS, ændrings- og afleveringsdokumentation. Novo Nordisk: FAT/SAT, IQ/OQ/PQ og sporbare testregistre uden kritiske fund ved aflevering. BIOFOS: LOTO, APV, risikovurdering, 5S og Standard Work i driftsmiljø."),
    ("Projekter fra idé og projektering gennem commissioning til drift", "Novo Nordisk: koordinering af 37 CAPEX-projekter, 25 specialister, fremdrift, risiko, økonomi og idriftsættelse/test. Ventek-Air: 11 samtidige anlægsprojekter fra specifikation til aflevering. Det dokumenterer projekt- og commissioningled, ikke ejerskab af hele Assens' projektlivscyklus."),
    ("Samarbejde med drift, proces, mekanik, el, automation og leverandører", "ELOHVAC: daglig koordinering af fem elektrikere og tre lærlinge samt kunder og underentreprenører. Novo Nordisk: tværfaglig koordinering af 25 specialister på tværs af engineering, indkøb og anlæg; Ventek-Air: daglig koordinering af et 14-personers team."),
    ("Vagtordning efter oplæring", "BIOFOS' døgnbemandede skifteholdsdrift og akutte fejlfinding er dokumenteret. Kandidatens konkrete mulighed for at indgå i Assens Forsynings vagtordning er ikke bekræftet i master-CV'et; accept eller tilgængelighed er derfor ikke påstået."),
    ("Almindeligt kørekort", "Kørekort B (manuelt gear) er dokumenteret. Bopæl er Måløv; daglig transport til Forsyningsparken uden for Assens og vagtfremmøde er ikke særskilt afklaret."),
]

EXPERIENCE = [
    ("Ejer / teknisk direktør / elautoriseret maskinmester", "ELOHVAC ApS · København · maj 2023–nu", "5 elektrikere + 3 lærlinge · fuldt P&L-ansvar", [
        "Udfører og planlægger el-tekniske service- og entrepriseopgaver: installationer, tavler, styring, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg.",
        "Koordinerer medarbejdere, materialer, kunder og underentreprenører fra tilbud til KS og aflevering; anvender LOTO, APV og risikovurdering.",
        "Python/Claude-værktøjer til tilbudsberegning, tidsplaner, KS-tjeklister og KPI-rapportering gav dokumenteret produktivitetsløft over 40 % i egne arbejdsgange."
    ]),
    ("Medejer og CTO / teknisk ansvarlig for AI-afdelingen", "Data Power Consultant ApS · København · 2024–2026 (sideløbende med ELOHVAC)", "Tekniske og industrielle applikationer", [
        "Ledte kundeløsninger fra behovsafklaring og integration til idriftsættelse, dokumentation og overdragelse; arbejdede med LLM-API'er og AI-agenter.",
        "Indførte fælles standarder for AI-assisteret udvikling, review og test; anvendte AI i ledelsesrapportering og matrixledelse."
    ]),
    ("Senior idriftsættelsesingeniør / projektleder, elsystem", "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024", "37 CAPEX-projekter · 25 specialister · DKK 2–10 mio. pr. projekt", [
        "Koordinerede scope, fremdrift, økonomi, risici og ressourcer på tværs af engineering, indkøb og anlæg; fulgte data i SAP ERP.",
        "Arbejdede med el-tavler, styring og UPS samt FAT/SAT og IQ/OQ/PQ. PDCA-program reducerede energiomkostninger med 40 % i den pågældende organisation."
    ]),
    ("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022", "11 samtidige anlægsprojekter · 14-personers team", [
        "Koordinerede projekter fra specifikation til aflevering med daglige tavlemøder, kapacitetsplanlægning, materialer, underentreprenører, kvalitet og dokumentation."
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
    ("El og procesanlæg", "LV/MV/HV-autorisation · el-fejlfinding · tavler · styring · pumper · HVAC · højspændingstavler"),
    ("Drift og vedligehold", "24/7-procesdrift · SCADA-overvågning · forebyggende vedligehold · akut fejlfinding · CMMS/vedligeholdsdata"),
    ("Sikkerhed og kvalitet", "LOTO · APV · risikovurdering · nærved-hændelser · 5S · Standard Work · PDCA · FAT/SAT · IQ/OQ/PQ"),
    ("Data og digitale værktøjer", "SAP ERP · Excel/Power Query · Power BI · Python · Claude API · KPI-rapportering"),
    ("Automation", "Erfaring omkring PLC-styrede anlæg; PLC-platforme/programmering og specifik SCADA-/SRO-platform ikke dokumenteret"),
    ("Praktisk", "Dansk og persisk/farsi — modersmål · engelsk — professionelt · kørekort B · bopæl Måløv"),
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
    m.meta("Assens Forsyning A/S · att. Niels Sørensen · Maskinmester til drift, teknik og automation")
    p = m._p(spacing_after=50, line=240, justify=False)
    m._run(p, "Ansøgning · drift, teknik og automation", bold=True)
    m.para("Kære Niels Sørensen og Assens Forsyning,", after=25, justify=False)
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
    m.resume_header(NAME, "Maskinmester · procesdrift · teknik og automation", CONTACT, "ERHVERVSERFARING")
    add_jobs(m, EXPERIENCE)
    m.section("UDDANNELSE OG CERTIFICERING")
    for title, detail in EDUCATION:
        m.edu(title, detail)
    m.section("ARBEJDSFORMER OG DIGITALE VÆRKTØJER")
    m.models_table("RELEVANTE VÆRKTØJER", ("Område", "Dokumenteret anvendelse"), TOOLS,
                   widths=(2700, 7646), compact=True)
    return m.save(path, title="Ansøgning og CV — Assens Forsyning, maskinmester til drift, teknik og automation",
                  subject="Maskinmester · spildevand · drift · SCADA · PLC · automation",
                  keywords="Maskinmester; Assens Forsyning; spildevand; drift; automation; PLC; SCADA; fejlfinding; vedligehold; el; procesdata")


if __name__ == "__main__":
    print(build())
