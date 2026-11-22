# -*- coding: utf-8 -*-
"""Envases Europe A/S — Production Manager, Løsning.
Short, job-centred motivation followed by evidence-led CV and requirements matrix.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")
OUTPUT = os.path.join(ROOT, "Shahram_Ajloo_Envases_Production_Manager.docx")
NAME = "SHAHRAM AJLOO"
TITLE = "Production Manager | produktion · Lean · kvalitet · medarbejderudvikling"
CONTACT = "+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv"
DATE = "3. november 2026"

MOTIVATION = [
    "Når ca. 150 timelønnede producerer fødevareemballage i døgndrift, skal sikkerhed, hygiejne, kvalitet og levering holde samme standard på dag-, aften-, nat- og weekendhold. Tre supervisors og produktionsassistenten skal have et fælles driftsbillede, klare beslutningsrum og en enkel vej fra afvigelse til handling.",
    "Jeg søger rollen, fordi bæredygtig metalemballage til fødevareindustrien skal forene produktsikkerhed og produktintegritet med arbejdsglæde. Envases beskriver det sådan: medarbejderne er kernen. Virksomheden fremhæver bæredygtighed samt udvikling af medarbejdere og ledere. Med involverende og anerkendende ledelse kan udvikling, trivsel og et stærkt samarbejde gå hånd i hånd med Lean-optimering og klare krav til drift.",
    "Først vil jeg etablere en fælles kadence tæt på den daglige drift: kort opfølgning på sikkerhed, kvalitet, leverance og bemanding; ugentlig gennemgang af tab, flaskehalse og Lean-tiltag; månedlig vurdering af KPI-tendenser, ressourcer og projekter. Hvert tal får definition, ejer og opfølgning. Samtidig kortlægges kompetencedækning på tværs af skift, og supervisors aftaler oplæring, lederudvikling og hvordan forbedringsarbejde bringes videre mellem holdene.",
    "Lean skal følge proces og risiko: standardarbejde og årsagsanalyse før ændringer, afprøvning under kontrollerede forhold og dokumenteret effekt på kvalitet, sikkerhed, levering og produktivitet. Envases’ fokus på ansvarlig emballage, produktintegritet og medarbejderudvikling gør netop kombinationen af stabil produktion og løbende forbedring interessant. CV’et viser de konkrete lederforløb og resultater.",
]

PROFILE = (
    "Maskinmester og B.Tech med produktionsteamledelse fra ARJ Engineering samt erfaring med teknisk drift, "
    "vedligehold, kvalitetsstyrede projekter og medarbejderudvikling. Ledte 12 mekanikere og teknikere i et "
    "produktionsværksted; senere 14-personers team hos Ventek-Air og fem elektrikere plus tre lærlinge i ELOHVAC. "
    "Hos Novo Nordisk koordinerede jeg 25 specialister på tværs af 37 CAPEX-projekter — tværfaglig koordinering, "
    "ikke direkte personaleansvar. Arbejder praktisk med 5S, PDCA, Standard Work, A3, DMAIC, årsagsanalyse, "
    "KPI-opfølgning og dokumenteret overdragelse."
)

HIGHLIGHTS = [
    ("Produktion og personale", "ARJ: produktionsleder for 12 mekanikere og teknikere; planlægning, materialer og mål. ELOHVAC: 5 elektrikere + 3 lærlinge; fuldt P&L."),
    ("Driftsrytme og forbedringer", "Ventek-Air: daglig ledelse af 14-personers team, tavlemøder og flaskehalsanalyse på 11 samtidige projekter. BIOFOS: kritisk 24/7-drift, vedligehold og 5S/PDCA."),
    ("Kvalitet, projekter og økonomi", "Novo Nordisk: 37 CAPEX-projekter, 25 specialister, SAP ERP, FAT/SAT og IQ/OQ/PQ; nul kritiske fund ved aflevering. PDCA-forløb reducerede energiomkostninger med 40 % dér."),
]

EXPERIENCE = [
    ("Ejer / teknisk direktør / elautoriseret maskinmester", "ELOHVAC ApS · København · maj 2023–nu", "5 elektrikere + 3 lærlinge · fuldt P&L-ansvar", [
        ("Planlægning og økonomi", "Planlægger service- og entrepriseopgaver, tilbud, materialer og underentreprenører; følger dækningsgrad, kvalitet, levering og kundeaftaler."),
        ("Ledelse og kompetencer", "Daglig planlægning og opfølgning med fem elektrikere og tre lærlinge; 1:1, MUS, oplæring, arbejdsmiljø, LOTO og risikovurdering."),
        ("KPI og digital forbedring", "Python- og Claude-værktøjer til tilbud, tidsplaner, KS-tjeklister og KPI-dashboards; produktivitetsløft over 40 % i egne arbejdsgange."),
    ]),
    ("Medejer og CTO / teknisk ansvarlig for AI-afdelingen", "Data Power Consultant ApS · København · 2024–nov. 2026 (sideløbende med ELOHVAC)", "AI-afdeling på 4–10 personer", [
        ("Tekniske leverancer", "Ledte kundeløsninger fra behovsafklaring og datamodel til integration, idriftsættelse, dokumentation og overdragelse."),
        ("Arbejdsstandarder og ledelsesdata", "Indførte fælles AI coding-standarder for review og test; anvendte AI til ledelsesrapportering, beslutningsoplæg og KPI-analyse."),
        ("Tekniske og industrielle applikationer", "AI-agenter og LLM-API'er samt AI-assisterede beregninger og designvarianter med faglig validering før levering."),
    ]),
    ("Senior idriftsættelsesingeniør / projektleder, elsystem", "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024", "37 CAPEX-projekter · 25 specialister · DKK 2–10 mio. pr. projekt", [
        ("Portefølje og ressourcer", "Koordinerede scope, fremdrift, økonomi, risici og ressourcer på tværs af engineering, indkøb og anlæg; månedlig rapportering til ledelse og bygherre."),
        ("Kvalitet og overdragelse", "FAT/SAT, IQ/OQ/PQ og sporbar GMP-dokumentation; nul kritiske fund ved aflevering. PDCA-program reducerede energiomkostninger med 40 % i den pågældende organisation."),
    ]),
    ("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022", "11 samtidige anlægsprojekter · 14-personers team", [
        ("Daglig produktion og flow", "Ledte montage- og produktionsteamet; kapacitets- og fremdriftsplanlægning, daglige tavlemøder, flaskehalsanalyse, entreprenører, kvalitet og aflevering."),
    ]),
    ("Vedligeholdelses- og driftsleder / værkstedstekniker", "BIOFOS, Lynetten · København · aug. 2017–jan. 2022", "Kritisk 24/7-procesdrift", [
        ("Drift og vedligehold", "Forebyggende vedligehold og akut fejlfinding på pumper, HVAC, højspændingstavler og øvrigt el-/mekanisk udstyr; SCADA-overvågning."),
        ("Forbedringer og sikkerhed", "Reservedelsflow, 5S, Standard Work og PDCA; skifteholdsdrift med LOTO, APV, risikovurdering og opfølgning på nærved-hændelser."),
    ]),
    ("Elektromekaniker / produktionsteamleder", "ARJ Engineering · Teheran · dec. 2003–mar. 2010", "12 mekanikere og teknikere", [
        ("Produktionsledelse", "Ledte et 12-personers mekaniker- og teknikerteam; vagtplanlægning, materialestyring og målopfølgning i maskinværksted/produktion."),
        ("Produkt- og procesansvar", "Produktportefølje for en produktionslinje med elektromotorer, pumper og dykpumper: livscyklus, roadmap, business cases, udvikling/lancering samt pris-, margin- og investeringsbeslutninger. Ingen konkrete resultatmål oplyst."),
        ("Teknisk problemløsning", "Fejldiagnose, reparation og korrigerende handlinger på industrielle el- og mekaniske anlæg; erfaring med ledelse under vækst og opskalering."),
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
    ("Produktion og Lean", "Produktionsledelse · 5S · PDCA · Standard Work · VSM · A3 · DMAIC · Kaizen · SMED · TPM"),
    ("Problemløsning", "FMEA i praksis · 5xHvorfor · Ishikawa · rodårsagsanalyse · afvigelser og korrigerende handlinger"),
    ("Drift, kvalitet og sikkerhed", "Kritisk 24/7-drift · forebyggende vedligehold · FAT/SAT · IQ/OQ/PQ · GMP-dokumentation · LOTO · APV"),
    ("KPI og digitale værktøjer", "SAP ERP · generel CMMS-erfaring (platform ikke navngivet) · Excel/Power Query · Power BI · Python · Claude API"),
    ("Ledelse og sprog", "MUS · 1:1 · tavlemøder · kompetenceudvikling · dansk og persisk/farsi modersmål · engelsk professionelt"),
]

REQUIREMENTS = [
    ("Overordnet ansvar for produktion og ca. 150 timelønnede", "ARJ: produktionsleder i maskinværksted med direkte ledelse af 12 mekanikere og teknikere; ELOHVAC: fem elektrikere og tre lærlinge. Ledelse tæt på drift og mål."),
    ("Direkte ledelse af tre supervisors og en produktionsassistent", "ARJ og ELOHVAC dokumenterer direkte teamledelse; Ventek-Air dokumenterer daglig ledelse af 14 personer. Novo Nordisk: 25 specialister koordineret tværfagligt, ikke direkte personaleansvar."),
    ("Produktion i døgndrift på dag-, aften-, nat- og weekendhold", "BIOFOS dokumenterer kritisk 24/7-procesdrift og skiftehold. Fælles skiftoverlevering, ens standarder og synlige afvigelser kan sikre kontinuitet mellem produktionshold."),
    ("Daglig opfølgning på produktion, ressourcer og projekter med nærmeste team", "Ventek-Air: daglig teamledelse, tavlemøder, kapacitets- og fremdriftsplanlægning på 11 samtidige projekter. ELOHVAC: arbejdsplaner, materialer og leverandører."),
    ("Drive Lean-produktionsoptimering og effektivitetsforbedringer", "Praktisk 5S, PDCA, Standard Work, DMAIC, A3, VSM og flaskehalsanalyse fra drift og teamledelse; ELOHVAC-værktøjer gav over 40 % løft i egne arbejdsgange."),
    ("Udvikle medarbejdere, trivsel og samarbejde på tværs af skift", "ELOHVAC: daglig planlægning, 1:1, MUS og oplæring af fem elektrikere og tre lærlinge; Ventek-Air: tavlemøder og daglig koordinering af et 14-personers team."),
    ("Samarbejde og udvikling blandt nærmeste ledere", "Dokumenteret teamledelse i ARJ, Ventek-Air og ELOHVAC; konkret ledelsesrytme foreslås med afstemte mål, ansvar, bemanding og løbende coaching af supervisors."),
    ("Processer og procedurer for kvalitet og rettidige leverancer", "Novo Nordisk: FAT/SAT, IQ/OQ/PQ, GMP-dokumentation og nul kritiske fund ved aflevering; Ventek-Air/ELOHVAC: KS, planlægning og afleveringsmateriale."),
    ("Efterleve strenge regler for fødevareemballagens kvalitet, hygiejne og sikkerhed", "Novo Nordisk-projekter krævede kontrolleret ændring, test og sporbar GMP-dokumentation; LOTO, APV og risikovurdering i drift. Arbejdsgiverens fødevarekrav styrer standarderne."),
    ("Daglig, ugentlig og månedlig KPI-rapportering af produktionen", "ELOHVAC: Python/Claude KPI-dashboards og opfølgning; Novo Nordisk: månedlig rapportering til ledelse/bygherre. Foreslået kadence: skiftdaglige signaler, ugentlig tabsgennemgang, månedlig trend."),
    ("Udvikle medarbejdere og ledere til fremtidens krav", "Oplæring, 1:1 og MUS i ELOHVAC; 12-personers ARJ-team og 14-personers Ventek-Air-team. Kompetencematrix og oplæringsplan pr. skift er foreslået som fælles driftsværktøj."),
    ("Teknisk og ledelsesmæssigt funderet; ingeniør, maskinmester eller lignende", "Elautoriseret maskinmester (LV/MV/HV), B.Tech i Technology Management & Mechanical Engineering og el-/maskinteknisk design; praktisk teknisk drifts- og produktionserfaring."),
    ("Erfaring med at lede ledere og større medarbejdergrupper", "Dokumenteret direkte ledelse: ARJ 12, Ventek-Air 14, ELOHVAC 5 elektrikere + 3 lærlinge; Data Power AI-afdeling 4–10. Novo: 25 specialister koordineret, ikke personaleledet."),
    ("Involverende og anerkendende ledelse", "ELOHVAC: daglig planlægning, 1:1, MUS og lærlingeoplæring; Ventek-Air: tavlemøder og flaskehalsanalyse med teamet. Løsningerne udvikles med dem, der udfører arbejdet."),
    ("Opstille mål og rammer for både økonomi og medarbejdernes indsats", "Fuldt P&L-ansvar i ELOHVAC; ressource-, risiko- og økonomiopfølgning på 37 Novo Nordisk CAPEX-projekter; ARJ-vagtplanlægning, materialestyring og målopfølgning."),
    ("Understøtte samarbejde på tværs af organisation og alle skift", "Novo Nordisk: 25 specialister koordineret på tværs af engineering, indkøb og anlæg; BIOFOS skifteholdsdrift; Ventek-Air daglige tavlemøder og tværfaglige grænseflader."),
    ("Sikre produktivitet, kvalitet og trivsel i hele produktionen", "Kobler sikkerhed, bemanding, standardarbejde, kvalitet og levering i en fælles opfølgningsrytme; erfaring fra 24/7-drift, reguleret projektaflevering og produktionsteamledelse."),
    ("Bæredygtig metalemballage af høj kvalitet til fødevareindustrien", "Motivationen retter sig mod Envases' opgave: ansvarlig emballage med produktintegritet. Envases' officielle materiale fremhæver bæredygtighed, produkt-/fødevaresikkerhed og medarbejderudvikling."),
    ("Sende CV med få linjer om interesse for stillingen", "Første side giver en kort opgave- og virksomhedsfokuseret motivation; CV'et efterfølgende dokumenterer produktion, medarbejderledelse, teknisk drift, Lean og KPI-arbejde."),
]

CULTURE_TERMS = [
    "bæredygtig metalemballage",
    "fødevareindustrien",
    "døgndrift",
    "involverende og anerkendende",
    "arbejdsglæde",
    "Lean-optimering",
    "udvikling, trivsel og et stærkt samarbejde",
    "kvalitet, hygiejne og sikkerhed",
    "medarbejderne er kernen",
    "bæredygtighed",
    "produktsikkerhed",
    "produktintegritet",
    "udvikling af medarbejdere og ledere",
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
    m.meta("Envases Europe A/S · Production Manager · Løsning")
    p = m._p(spacing_after=45, line=235, justify=False)
    m._run(p, "Kort motivation · produktion, kvalitet og mennesker", bold=True)
    for text in MOTIVATION:
        m.para(text, after=38, line=195)

    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PRODUKTIONSLEDELSE OG DRIFTSRESULTATER")
    m.para(PROFILE, after=35, line=190)
    for label, text in HIGHLIGHTS:
        m.bullet(label, text, after=25, line=190)
    m.section("ERHVERVSERFARING")
    for job in EXPERIENCE[:3]:
        add_jobs(m, [job])

    m.page_break()
    m.resume_header(NAME, "Produktion · Lean · drift · kvalitet", CONTACT, "ERHVERVSERFARING (FORTSAT)")
    for job in EXPERIENCE[3:]:
        add_jobs(m, [job])
    m.section("UDDANNELSE OG CERTIFICERING")
    for title, detail in EDUCATION:
        m.edu(title, detail)
    m.section("ARBEJDSFORMER OG DIGITALE VÆRKTØJER")
    m.models_table("RELEVANTE METODER", ("Område", "Dokumenteret praksis"), METHODS, widths=(2700, 7646), compact=True)

    m.page_break()
    m.resume_header(NAME, "Production Manager | produktion · Lean · kvalitet", CONTACT, "DOKUMENTERET ERFARING MOD STILLINGENS OPGAVER")
    matrix = m.models_table("DOKUMENTATION MOD STILLINGEN", ("Krav i stillingsopslaget", "Kandidatens dokumentation og anvendelse"), REQUIREMENTS, widths=(3900, 6446), compact=True)
    header_props = matrix.rows[1]._tr.get_or_add_trPr()
    repeat_header = OxmlElement("w:tblHeader")
    repeat_header.set(qn("w:val"), "true")
    header_props.append(repeat_header)
    m.section("ARBEJDSGIVERENS RETNING")
    m.para("Envases’ officielle materiale beskriver ansvarlig emballage, bæredygtighed, produktsikkerhed og medarbejderudvikling. Produktionsopgaven i dette CV følger stillingsopslaget: stabil døgndrift, høj kvalitet, sikkerhed, levering og Lean-forbedring.", after=20)

    return m.save(path, title="CV og kort motivation — Envases Europe A/S, Production Manager",
                  subject="Production Manager · produktion · Lean · kvalitet · medarbejderledelse",
                  keywords="Envases; Production Manager; produktion; Lean; metalemballage; fødevareindustrien; døgndrift; KPI; kvalitet; sikkerhed")


if __name__ == "__main__":
    print(build())
