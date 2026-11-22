# -*- coding: utf-8 -*-
"""Envases Europe A/S — Production Supervisor, Løsning.
Opgavefokuseret motivation, dokumenteret CV og krav/evidensmatrix.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")
OUTPUT = os.path.join(ROOT, "Shahram_Ajloo_Envases_Production_Supervisor.docx")
NAME = "SHAHRAM AJLOO"
TITLE = "Production Supervisor | produktion · medarbejdere · Lean · kvalitet"
CONTACT = "+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv"
DATE = "3. november 2026"

MOTIVATION = [
    "Stillingsopslaget beskriver Envases som en succesfuld virksomhed. Fabrikken har produktion i døgndrift på dag-, aften-, nat- og weekendhold. Når cirka 40 timelønnede medarbejdere arbejder på skift, skal kompetencer, hygiejne, orden, kvalitet og produktionsflow hænge sammen — også når supervisoren ikke er på gulvet på hvert hold.",
    "Jeg søger rollen, fordi Envases forener bæredygtig metalemballage med høj kvalitet og udvikling. Opslaget beskriver medarbejderne som vores absolut vigtigste aktiv; på karrieresiden står, at medarbejderne er kernen, og at virksomheden investerer i udvikling af medarbejdere og ledere. Det skal kunne mærkes i medarbejdertrivsel, kvalitet, stabilitet og fleksibilitet på tværs af skift.",
    "Min foreslåede driftsrytme tager udgangspunkt i nærværende ledelse på tværs af skift: daglige tavlemøder med involvering, engagement og samarbejde, fælles målepunkter og tydelig overlevering. Tilstedeværelse på øvrige skift planlægges med driften, så også aften-, natte- og weekendhold møder nærværende ledelse; afvigelser får ansvarlig og opfølgning, mens forbedringer prioriteres efter effekt på sikkerhed, kvalitet, stabilitet og produktivitet.",
    "Kompetencedækning kortlægges pr. proces og skift, så oplæring og fleksibilitet bliver planlagt. 5S, standardarbejde og årsagsanalyse skal understøtte hygiejne, orden og ryddelighed; ændringer afprøves kontrolleret og måles mod relevante forretningsmål. Sådan kobles medarbejdernes faglighed med teknik og processer, og best practice udvikles til et godt arbejdsmiljø i en sund, sikker og tryg arbejdsplads.",
    "Jeg motiveres af at lede mennesker tæt på produktionen, hvor god daglig ledelse både mærkes i arbejdsglæden og kan ses i stabil drift og kvalitet. Envases’ fokus på bæredygtighed og produktintegritet gør netop denne kombination meningsfuld.",
]

PROFILE = (
    "Maskinmester og B.Tech med direkte produktions- og teamledererfaring fra ARJ Engineering samt senere ledelse "
    "af tekniske teams, projektleverancer og 24/7-drift. Ledte 12 mekanikere og teknikere i maskinværksted/produktion; "
    "senere 14-personers team hos Ventek-Air og fem elektrikere plus tre lærlinge i ELOHVAC. Hos Novo Nordisk "
    "koordinerede jeg 25 specialister på tværs af 37 CAPEX-projekter — koordinering, ikke direkte personaleansvar. "
    "Praktisk erfaring med medarbejderoplæring, daglige tavlemøder, 5S, PDCA, Standard Work, A3, DMAIC, årsagsanalyse, "
    "KPI-opfølgning, LOTO, APV og kvalitetssikret overdragelse."
)

HIGHLIGHTS = [
    ("Produktions- og teamledelse", "ARJ: 12 mekanikere/teknikere med vagtplan, materialer og målopfølgning. Ventek-Air: daglig ledelse af et 14-personers team."),
    ("Medarbejderudvikling og arbejdsmiljø", "ELOHVAC: daglig planlægning, 1:1, MUS og oplæring af fem elektrikere og tre lærlinge; BIOFOS: LOTO, APV, risikovurdering og nærved-hændelser."),
    ("Kvalitet og forbedring", "Novo Nordisk: 37 CAPEX-projekter, 25 tværfagligt koordinerede specialister, FAT/SAT, IQ/OQ/PQ og nul kritiske fund ved aflevering; PDCA reducerede energiomkostninger med 40 % dér."),
]

EXPERIENCE = [
    ("Ejer / teknisk direktør / elautoriseret maskinmester", "ELOHVAC ApS · København · maj 2023–nu", "5 elektrikere + 3 lærlinge · fuldt P&L-ansvar", [
        ("Planlægning og leverancer", "Planlægger service- og entrepriseopgaver, tilbud, materialer og underentreprenører; følger kvalitet, levering, kundeopfølgning og økonomi."),
        ("Medarbejdere og kompetencer", "Daglig planlægning og opfølgning; 1:1, MUS, lærlingeoplæring, arbejdsmiljø og sikkerhed med LOTO og risikovurdering."),
        ("Målinger og standarder", "Python- og Claude-værktøjer til tilbud, tidsplaner, KS-tjeklister og KPI-dashboards; produktivitetsløft over 40 % i egne arbejdsprocesser."),
    ]),
    ("Medejer og CTO / teknisk ansvarlig for AI-afdelingen", "Data Power Consultant ApS · København · 2024–nov. 2026 (sideløbende med ELOHVAC)", "AI-afdeling på 4–10 personer", [
        ("Kundeleverancer og udvikling", "Ledte tekniske og industrielle applikationer fra behovsafklaring og datamodel til integration, idriftsættelse, dokumentation og overdragelse."),
        ("Kvalitet i arbejdsmetoder", "Indførte fælles AI coding-standarder for review og test; anvendte AI til ledelsesrapportering, beslutningsoplæg og KPI-analyse."),
        ("Digitalisering", "LLM-API'er og AI-agenter samt AI-assisterede beregninger og designvarianter med faglig validering før levering."),
    ]),
    ("Senior idriftsættelsesingeniør / projektleder, elsystem", "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024", "37 CAPEX-projekter · 25 specialister · DKK 2–10 mio. pr. projekt", [
        ("Ressourcer og opfølgning", "Koordinerede scope, fremdrift, økonomi, risici og ressourcer på tværs af engineering, indkøb og anlæg; månedlig rapportering til ledelse og bygherre."),
        ("Proceskvalitet og aflevering", "FAT/SAT, IQ/OQ/PQ og sporbar GMP-dokumentation; nul kritiske fund ved aflevering. PDCA-program reducerede energiomkostninger med 40 % i den pågældende organisation."),
    ]),
    ("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022", "11 samtidige anlægsprojekter · 14-personers team", [
        ("Daglig ledelse og flow", "Ledte montage- og produktionsteam; kapacitets- og fremdriftsplanlægning, daglige tavlemøder, flaskehalsanalyse, entreprenører, kvalitet og aflevering."),
    ]),
    ("Vedligeholdelses- og driftsleder / værkstedstekniker", "BIOFOS, Lynetten · København · aug. 2017–jan. 2022", "Kritisk 24/7-procesdrift", [
        ("Teknik og stabil drift", "Forebyggende vedligehold og akut fejlfinding på pumper, HVAC, højspændingstavler og el-/mekanisk udstyr; SCADA-overvågning."),
        ("Sikkerhed og orden", "Skifteholdsdrift, 5S, Standard Work, PDCA, reservedelsflow, LOTO, APV, risikovurdering og opfølgning på nærved-hændelser."),
    ]),
    ("Elektromekaniker / produktionsteamleder", "ARJ Engineering · Teheran · dec. 2003–mar. 2010", "12 mekanikere og teknikere", [
        ("Produktion og medarbejdere", "Ledte 12 mekanikere og teknikere i maskinværksted/produktion; vagtplanlægning, materialestyring og målopfølgning."),
        ("Produkter og forbedring", "Produktportefølje for en produktionslinje med elektromotorer, pumper og dykpumper: livscyklus, roadmap, business cases, udvikling/lancering samt pris-, margin- og investeringsbeslutninger."),
        ("Problemløsning", "Fejldiagnose, reparation og korrigerende handlinger på industrielle el- og mekaniske anlæg; ledelse under vækst og opskalering."),
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

METHODS = [
    ("Lean og drift", "5S · PDCA · Standard Work · VSM · A3 · DMAIC · Kaizen · SMED · TPM · flaskehalsanalyse"),
    ("Problemløsning og kvalitet", "FMEA i praksis · 5xHvorfor · Ishikawa · årsagsanalyse · afvigelser og korrigerende handlinger"),
    ("Sikkerhed og proces", "24/7-procesdrift · forebyggende vedligehold · FAT/SAT · IQ/OQ/PQ · GMP-dokumentation · LOTO · APV"),
    ("Data og værktøjer", "SAP ERP · generel CMMS-erfaring (platform ikke navngivet) · Excel/Power Query · Power BI · Python · Claude API"),
    ("Ledelse og sprog", "1:1 · MUS · tavlemøder · kompetenceudvikling · dansk og persisk/farsi modersmål · engelsk professionelt"),
]

REQUIREMENTS = [
    ("Lede ca. 40 medarbejdere i produktionsafdelingen", "ARJ: direkte ledelse af 12 mekanikere og teknikere i produktion; Ventek-Air: daglig ledelse af 14; ELOHVAC: fem elektrikere og tre lærlinge med arbejdsplan og udvikling."),
    ("Ansvar på dag-, aften-, nat- og weekendhold i døgndrift", "BIOFOS dokumenterer kritisk 24/7-drift og skifteholdsarbejde. Fælles standarder og tydelig overlevering mellem skift er den foreslåede vej til stabilitet."),
    ("Daglig arbejdstid med synlig tilstedeværelse på de øvrige skift", "Tilstedeværelsesplan med roterende besøg på aften-, nat- og weekendhold foreslås; BIOFOS giver erfaring fra skifteholdsdrift, men ikke påstand om samme Envases-skiftmodel."),
    ("Sikre nødvendigt kompetenceniveau nu og fremover", "ELOHVAC: oplæring af fem elektrikere og tre lærlinge; ARJ: ledelse af 12 teknikere. Kompetencematrix pr. proces og skift foreslås til at planlægge oplæring og dækning."),
    ("Højt kvalitetsniveau med hygiejne, orden og ryddelighed", "BIOFOS: 5S og Standard Work; Novo Nordisk: kontrolleret GMP-dokumentation, FAT/SAT og IQ/OQ/PQ. Hygiejne- og housekeepingstandarder omsættes til lokale rutiner."),
    ("Daglige tavlemøder med involvering, engagement og samarbejde", "Ventek-Air: daglige tavlemøder og flaskehalsanalyse i et 14-personers team; ARJ: daglig planlægning og målopfølgning med 12 medarbejdere."),
    ("Forbedringer, der understøtter forretningens målepunkter", "ELOHVAC: KPI-dashboards gav over 40 % produktivitetsløft i egne arbejdsgange; Novo Nordisk: PDCA reducerede energiomkostninger med 40 % i den pågældende organisation."),
    ("Udvikle medarbejdere, processer og arbejdsmetoder", "ARJ, Ventek-Air og ELOHVAC: teamledelse, vagt-/arbejdsplaner og oplæring; 5S, PDCA og Standard Work blev brugt i praksis til struktur og forbedring."),
    ("Sund, sikker og tryg arbejdsplads med trivsel og samarbejde", "LOTO, APV, risikovurdering og nærved-opfølgning i BIOFOS og ELOHVAC; MUS, 1:1 og oplæring i ELOHVAC. Sikkerhed og trivsel kobles til daglig opfølgning."),
    ("Indsigt i komplekse processer og teknisk udstyr", "BIOFOS: pumper, HVAC, højspændingstavler, SCADA og 24/7-procesdrift; ARJ: elektromotorer og pumper; Novo Nordisk: idriftsættelse og kvalificeret test."),
    ("Koble medarbejdernes kompetencer med virksomhedens teknik og processer", "Ledelse i ARJ og ELOHVAC kombinerede teknisk fejlfinding, vagt-/arbejdsplaner og oplæring; standardarbejde og kompetencedækning foreslås pr. maskine og skift."),
    ("Teknisk og ledelsesmæssig baggrund", "Opslaget nævner ingeniør, maskinmester eller maskintekniker; dokumenteret uddannelse er elautoriseret maskinmester (LV/MV/HV), B.Tech i Technology Management & Mechanical Engineering og el-/maskinteknisk design."),
    ("Ordreproducerende virksomhed og ledelse af timelønnede", "ARJ dokumenterer produktionsteamledelse for 12 mekanikere/teknikere; ELOHVAC planlægger og leverer kundeopgaver med fem elektrikere og tre lærlinge. Ingen procesomfang tilskrives."),
    ("Forbedringsprojekter", "Ventek-Air: daglige tavlemøder og flaskehalsanalyse; BIOFOS: 5S, PDCA og Standard Work; Novo Nordisk: PDCA-resultat på energiomkostninger i organisationen."),
    ("Bred kommerciel forståelse", "ELOHVAC: fuldt P&L-ansvar, tilbud, dækningsgrad og leverandører; ARJ: produktportefølje, business cases, pris/margin og investeringer."),
    ("Dansk i skrift og tale", "Dansk er modersmål med professionel skriftlig dokumentation, KS-tjeklister, afleveringsmateriale og daglig kommunikation med medarbejdere og kunder."),
    ("Solid erfaring med Lean-værktøjer til løbende forbedringer", "Praktisk anvendelse af 5S, PDCA, Standard Work, VSM, A3, DMAIC, Kaizen, SMED og TPM; metoderne er arbejdspraksis, ikke Lean-/Six Sigma-certificering."),
    ("Skabe resultater gennem involvering, empati og godt teamsamarbejde", "1:1, MUS, oplæring og daglige tavlemøder kobler forventninger til medarbejdernes input; teams ledet i ARJ, Ventek-Air og ELOHVAC."),
    ("Motivation for Envases' bæredygtige metalemballage og høje kvalitet", "Envases' karriereside fremhæver medarbejderne som kernen og udvikling; virksomhedens bæredygtighedsside fremhæver produktintegritet og sikkerhed på produktionslinjen."),
    ("CV og motivation for interessen i stillingen", "Første side er en målrettet motivation om tværskiftsledelse, kompetencer, kvalitet, sikkerhed og forbedring; CV'et dokumenterer leder- og teknikgrundlaget."),
]

CULTURE_TERMS = [
    "succesfuld virksomhed",
    "bæredygtighed",
    "høj kvalitet",
    "produktion i døgndrift",
    "nærværende ledelse",
    "på tværs af skift",
    "medarbejdertrivsel",
    "medarbejderne som vores absolut vigtigste aktiv",
    "trivsel, kvalitet, stabilitet og fleksibilitet",
    "hygiejne, orden og ryddelighed",
    "involvering, engagement og samarbejde",
    "sund, sikker og tryg arbejdsplads",
    "teknik og processer",
    "motiveres af at lede mennesker",
    "medarbejderne er kernen",
    "udvikling af medarbejdere og ledere",
    "produktintegritet",
    "best practice",
]


def add_jobs(m, jobs):
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope)
        for label, text in bullets:
            m.bullet(label, text, after=18, line=190)


def build(path=OUTPUT):
    m = MasterDoc(TEMPLATE, lang="da-DK")
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta("Envases Europe A/S · Production Supervisor · Løsning")
    p = m._p(spacing_after=45, line=235, justify=False)
    m._run(p, "Motivation · nærvær, kompetencer og stabil produktion", bold=True)
    for text in MOTIVATION:
        m.para(text, after=32, line=190)
    m.meta("Med venlig hilsen", after=6)
    m.meta("Shahram Ajloo", after=0)

    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PRODUKTION, MEDARBEJDERE OG KVALITET")
    m.para(PROFILE, after=30, line=190)
    for label, text in HIGHLIGHTS:
        m.bullet(label, text, after=22, line=190)
    m.section("ERHVERVSERFARING")
    for job in EXPERIENCE[:3]:
        add_jobs(m, [job])

    m.page_break()
    m.resume_header(NAME, "Produktion · medarbejdere · Lean · kvalitet", CONTACT, "ERHVERVSERFARING (FORTSAT)")
    for job in EXPERIENCE[3:]:
        add_jobs(m, [job])
    m.section("UDDANNELSE OG CERTIFICERING")
    for title, detail in EDUCATION:
        m.edu(title, detail)
    m.section("ARBEJDSFORMER OG DIGITALE VÆRKTØJER")
    m.models_table("RELEVANTE METODER", ("Område", "Dokumenteret praksis"), METHODS, widths=(2700, 7646), compact=True)

    m.page_break()
    m.resume_header(NAME, "Production Supervisor | team · kvalitet · Lean", CONTACT, "DOKUMENTERET ERFARING MOD STILLINGENS OPGAVER")
    matrix = m.models_table("DOKUMENTATION MOD STILLINGEN", ("Krav i stillingsopslaget", "Kandidatens dokumentation og anvendelse"), REQUIREMENTS, widths=(3900, 6446), compact=True)
    header_props = matrix.rows[1]._tr.get_or_add_trPr()
    repeat_header = OxmlElement("w:tblHeader")
    repeat_header.set(qn("w:val"), "true")
    header_props.append(repeat_header)
    m.section("ARBEJDSGIVERENS RETNING")
    m.para("Envases' officielle karrieremateriale beskriver medarbejderne som kernen og fremhæver udvikling; den officielle bæredygtighedsside fremhæver produktintegritet og sikkerhed for produktionslinjens medarbejdere. Motivationen og arbejdsmodellen er derfor forankret i mennesker, kvalitet og stabil drift.", after=18)

    return m.save(path, title="Motivation og CV — Envases Europe A/S, Production Supervisor",
                  subject="Production Supervisor · produktion · medarbejdere · Lean · kvalitet",
                  keywords="Envases; Production Supervisor; produktion; Lean; teamledelse; kvalitet; medarbejderudvikling; skift")


if __name__ == "__main__":
    print(build())
