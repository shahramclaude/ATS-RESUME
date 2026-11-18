# -*- coding: utf-8 -*-
"""Samtank A/S — Operations Excellence Manager/Process Manager, job 9762.
Dansk kombineret ansøgning + CV, bygget i projektets masterdesign.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")
OUTPUT = os.path.join(ROOT, "Shahram_Ajloo_Samtank_OperationsExcellenceManager_9762.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Operations Excellence Manager · Vedligehold, drift og tværgående forbedringer"
CONTACT = "+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv"
DATE = "3. november 2026"
RECIPIENT = "Samtank A/S · Operations Manager · v/Management Consultant Majbrit Kock Andersen"
SUBJECT = "Operations Excellence Manager/Process Manager · job 9762 · Aarhus"

# Side 1: åbningsgreb AC — beslutningen før driftsstoppet.
OPENING = (
    "En forebyggende vedligeholdelsesstrategi bliver først til forsyningssikkerhed, når fire terminaler kan "
    "træffe den samme velbegrundede beslutning: Hvad er kritisk, hvad kan vente, og hvem ejer næste skridt?"
)

LETTER = [
    (
        "Hos Samtank skal svaret holde på tværs af otte tankanlæg, under døgnkontinuerlig drift og med "
        "brand- og eksplosionsrisiko i selve arbejdsmiljøet. Jeg læser virksomhedens formål som en "
        "«kontinuerligt stabil forsyning»; når anlæggene arbejder «24 timer i døgnet», er forebyggelse, "
        "arbejdsvinduer og reservedele en samlet driftsbeslutning — ikke hver sin lokale liste."
    ),
    (
        "Jeg ville begynde med Operations Manager, driftslederne og vedligeholdelseskoordinatoren om "
        "at fastlægge ét fælles grundlag: anlægs- og komponentregister, kritikalitet og konsekvens, "
        "lovpligtige og producentbestemte aktiviteter, fejl- og tilstandshistorik, kritikalitetsbaseret "
        "vedligehold, reservedelsrisiko samt realistiske stop- og adgangsvinduer. Derfra kan "
        "prioriteringsreglerne skelne mellem sikkerhed/compliance, tilgængelighed og økonomi. Fælles "
        "standarder og fælles indkøb bør fastlægges, hvor "
        "teknik og risiko er ens; lokale forhold og driftslederens ansvar skal fortsat være tydelige."
    ),
    (
        "Derefter skal projekt-, vedligeholds- og forbedringsinitiativer kunne styres i ét overblik: "
        "ejer, næste milepæl, kritisk leverance, afhængighed, vedligeholdelsesomkostninger, budget/forecast, risiko, management of "
        "change-status og gevinst. En fast tværgående gennemgang omsætter beslutninger til ansvarlig, "
        "frist og dokumenteret lukning. Business cases sammenligner sikkerheds- og driftskonsekvens, "
        "livscyklusomkostning, reservedele og forventet gevinst; efter implementering måles resultatet "
        "mod den registrerede baseline. Ændringer frigives først gennem Samtanks godkendte proces, "
        "med opdateret dokumentation og klar overdragelse til drift."
    ),
    (
        "Det passer til jeres udsagn om, at «sikkerhed er en grundlæggende forudsætning», at "
        "«sikkerhedshensyn gennemsyrer alt», og at I «samarbejder tæt med eksterne myndigheder». ISO 9001, "
        "lovkrav og arbejdstilladelser skal derfor indgå i "
        "arbejdets plan og afslutning — ikke tilføjes bagefter. Standardisering får først værdi, når "
        "den følges af «grundig oplæring i procedurerne». Samtanks fokus på «løbende på at finde nye "
        "muligheder for forbedring og optimering af vores processer» kræver en rytme, hvor idéer prøves, "
        "måles og deles på tværs."
    ),
    (
        "I uge 1–2 ville jeg lytte på alle fire terminaler, gennemgå gældende risikostyring, "
        "vedligeholdsdata, projekter og økonomi og aftale målepunkter med Operations Manager. Ved dag "
        "30 foreligger fælles baseline, kritikalitetsprincipper og prioriteret portefølje. Ved dag 60 "
        "afprøves modellen på en aftalt pilotlokation, inklusive MOC og beslutnings-/gevinstlog. Ved dag "
        "90 gennemgås effekt, åbne risici og læring med driftslederne, og en realistisk udrulningsplan "
        "aftales. Målepunkter fastsættes efter baselinen: rettidigt forebyggende vedligehold, forfaldne "
        "kritiske opgaver, gentagne fejl, uplanlagte afbrydelser, MOC-lukning og omkostning mod forecast."
    ),
    (
        "Samtank beskriver en «kort vej fra idé til handling». Den foreslåede "
        "styring skal derfor være let nok til at blive brugt i hverdagen: fælles retning og synlig "
        "opfølgning, men beslutninger tæt på anlægget og respekt for den tekniske faglighed."
    ),
]

PROFILE = (
    "Samtanks behov er en fælles, risikobaseret styring af vedligehold, projekter og forbedringer på tværs "
    "af anlæg med 24/7 drift. Relevant dokumenteret erfaring: drifts- og vedligeholdelsesledelse på Biofos/Lynetten "
    "(2017–2022) i kritisk procesindustri med forebyggende vedligehold, kritikalitet, reservedele og el-/procesudstyr; "
    "ELOHVAC fra maj 2023 med forebyggende service, 5 elektrikere + 3 lærlinge og fuldt P&L; Novo Nordisk "
    "med 37 samtidige CAPEX-projekter, 25 specialister, SAP-rapportering og PDCA-resultat på 40 % lavere "
    "energiomkostninger. B.Tech i Technology Management & Mechanical Engineering, elautoriseret "
    "maskinmester LV/MV/HV og PRINCE2-certificeret projektleder. Indstillet på at flytte til Aarhus-området."
)

RESULTS = [
    ("37 samtidige CAPEX-projekter", "Novo Nordisk · 25 tværfaglige specialister · DKK 2–10 mio. pr. projekt · nul kritiske fund ved aflevering."),
    ("40 % lavere energiomkostninger", "PDCA-program hos Novo Nordisk; investeringer, energi og omkostninger fulgt via SAP ERP."),
    ("11 parallelle installationsprojekter", "Ventek-Air · 14-personers team · kapacitets- og flaskehalsopfølgning fra specifikation til aflevering."),
    ("Over 40 % produktivitetsløft", "ELOHVAC · Python/Claude-værktøjer til tilbud, planlægning, KS-tjeklister og KPI-opfølgning."),
]

REQUIREMENTS = [
    ('Drive udviklingen af en forebyggende vedligeholdsstrategi',
     'Biofos: criticality-/condition-led preventive work on 24/7 assets; ELOHVAC: preventive el/HVAC service. Samtank plan links risk, windows, spares and owners.'),
    ('Fælles prioriteringsprincipper på tværs af terminaler',
     'Biofos: criticality-based maintenance; Novo: 37 CAPEX jobs across 25 experts. Rank terminal work by safety, availability, risk and capacity.'),
    ('Standardisere løsninger, reservedele, indkøb og arbejdsmetoder',
     'Biofos: spares, 5S, Standard Work; ELOHVAC: materials/QA. Standardize parts, procurement and methods with coordinator and project leaders.'),
    ('Koordinere forbedringer, vidensdeling og best practice',
     'Biofos PDCA/Standard Work; Novo 37 projects; Ventek 11 jobs. Record owner/effect and share proven practices across sites.'),
    ('Skabe værdi i drifts-, vedligeholds- og projektomkostninger',
     'ELOHVAC full P&L; Novo 37 CAPEX at DKK 2–10m; PDCA cut energy cost 40%. Compare lifecycle cost, risk and measured benefits.'),
    ('Samlet overblik over prioriterede Operations-aktiviteter',
     'Novo tracked budget/risk/resources for 37 projects; Ventek 11 daily. One view: owner, date, dependency, budget, risk, status, decision.'),
    ('Følge åbne projekter, kritiske leverancer og management of change',
     'Novo change/deviation records, FAT/SAT, qualification on 37 jobs; zero critical findings. ELOHVAC tracks material/QA to handover; assign MOC closure.'),
    ('Fast sparringspartner for Operations Manager',
     'Novo monthly reports/SAP cost and assets; ELOHVAC full P&L. Brief Ops Manager on availability, risk, overdue work, investment and benefits.'),
    ('Facilitere grupper og omsætte beslutninger til ejer og deadline',
     'Ventek huddles for 14; ELOHVAC allocation for 8; Novo coordination of 25. Close meetings with action, owner, due date and status.'),
    ('Business cases, investeringsprioritering og gevinstopfølgning',
     'Novo 37 CAPEX, DKK 2–10m, SAP and 40% energy saving; ELOHVAC full P&L. Compare scenarios, risk, lifecycle cost and measured benefit.'),
    ('Indirekte ledelse, porteføljestyring og forandringsledelse',
     'Coordinated 25 Novo specialists without line authority; led 14 at Ventek and 8 at ELOHVAC. Shared priorities and follow-up embed change.'),
    ('Mulig senere personaleledelse for et mindre team',
     'Led 8 ELOHVAC staff, 14 Ventek, 12 ARJ; 1:1, MUS, safety follow-up and apprentice training prepare for small-team leadership.'),
    ('Forebyggende vedligehold og stærk vedligeholdsfaglighed',
     'Biofos 2017–22: preventive upkeep on 24/7 pumps, HVAC, HV switchgear, drives, SCADA; spares. ELOHVAC preventive electrical/HVAC service.'),
    ('Stakeholder management, koordinering og projektopfølgning i drift',
     'Novo: 25 engineering/procurement/site specialists on 37 jobs; Ventek 14/11; ELOHVAC clients, suppliers and subcontractors; regular reports.'),
    ('Relevant teknisk uddannelse',
     'B.Tech in Technology Management & Mechanical Engineering; elautoriseret maskinmester LV/MV/HV; electrical/mechanical design and HVAC. Technical base for assets.'),
    ('Driftskritisk proces-/energi-/forsyningsmiljø med sikkerhed og dokumentation',
     'Biofos 24/7 process operations; Novo GMP/FDA/EMA records, zero critical findings; ELOHVAC LOTO/APV/risk. Follow terminal authority and ISO 9001 controls.'),
    ('Vedligehold, Process Excellence og forandringsledelse',
     'Biofos 5S/Standard Work/PDCA; Novo energy cost −40%; ELOHVAC productivity >40%. Lean/Six Sigma applied; PRINCE2 certified project manager.'),
    ('Faglig tillid og møde folk i øjenhøjde',
     'Led 8 ELOHVAC staff with 1:1, MUS and apprentice training; Biofos shifts; Ventek 14. Explain choices through safety, facts and site constraints.'),
    ('Analytisk og praktisk tilgang',
     'Troubleshot pumps, HV, HVAC, SCADA; PDCA, A3, 5 Why, Ishikawa; risk/cost across 37 Novo projects. Convert findings to work orders.'),
    ('Kommunikation og struktureret arbejdsform',
     'Novo monthly/validation reports; Ventek daily huddles; ELOHVAC estimates, plans, QA, handover, toolbox talks. Danish native; professional English.'),
    ('Prioritere og bevare overblik over mange samtidige aktiviteter',
     'Novo 37 CAPEX; Ventek 11 projects; ELOHVAC allocation for 5 electricians + 3 apprentices. Link capacity, milestones, risks, spares and MOC.'),
    ('Aarhus-base og besøg på øvrige lokationer',
     'Relocation to Aarhus on appointment confirmed; driving licence B. Previous roles coordinated operational and project work across several sites.'),
]

METHODS = [
    ("Vedligehold og aktiver", "CMMS · forebyggende og tilstandsbaseret vedligehold · kritikalitet · reservedelsflow · SAP ERP · SCADA"),
    ("Process Excellence", "PDCA · 5S · Standard Work · A3 · 5xHvorfor · Ishikawa · Lean/Six Sigma anvendt i praksis"),
    ("Projekt og ændring", "PRINCE2 · porteføljestyring · budget/risiko · FAT/SAT · IQ/OQ/PQ · afvigelses- og ændringsopfølgning"),
    ("Sikkerhed og kvalitet", "LOTO · APV · risikovurdering · toolbox talks · ISO 9001 som Samtank-systemramme · GMP/FDA/EMA dokumentationspraksis"),
    ("Økonomi og forbedring", "Fuldt P&L · CAPEX DKK 2–10 mio. · SAP ERP · KPI-rapportering · business cases · energi- og produktivitetsforbedring"),
]

FIRST90 = [
    ("Uge 1–2", "Lyt til Operations Manager, fire driftsledere, projektledere og vedligeholdskoordinator; besøg terminalerne, gennemgå procedurer, risici, CMMS-data, projekter og økonomi. Aftal baseline, mandat og faste møder."),
    ("Dag 30–60", "Fremlæg fælles aktiv-/kritikalitetsoversigt, prioriteringsprincipper og porteføljeformat. Vælg sammen en pilotterminal; afprøv vedligeholds- og MOC-flow, ejere, frister, risici og gevinstmåling."),
    ("Dag 61–90", "Gennemgå pilotens resultater og åbne risici; justér standarder og træning med terminalteams. Aftal site-for-site udrulning, business-case-kadence og ledelsesoverblik for næste kvartal."),
]


def build(path=OUTPUT):
    m = MasterDoc(TEMPLATE, lang="da-DK")

    # Side 1 — opgaven og arbejdsmodellen; ikke kandidatens biografi.
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta(RECIPIENT)
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, SUBJECT, bold=True, color="1A1A1A")
    m.para("Kære Majbrit Kock Andersen", after=60, justify=False)
    m.para(OPENING, after=75, line=240)
    for paragraph in LETTER:
        m.para(paragraph, after=60, line=225)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # Side 2 — relevant profil og de to stærkeste driftsbeviser.
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "DRIFT, VEDLIGEHOLD OG PROCESS EXCELLENCE")
    m.section("PROFIL")
    m.para(PROFILE, after=45, line=225)
    m.section("DOKUMENTEREDE RESULTATER")
    for label, detail in RESULTS:
        m.bullet(label, detail, after=15, line=220)

    m.section("ERHVERVSERFARING")
    m.job("Ejer / teknisk direktør / elautoriseret maskinmester", "ELOHVAC ApS · København · maj 2023–nu",
          "5 elektrikere + 3 lærlinge · 40+ serviceinstallationer · fuldt P&L")
    m.bullet("Drift og vedligehold", "Forebyggende vedligehold, fejlfinding, planlægning, materialer og underentreprenører på el-, ventilations- og klimaanlæg; kvalitetssikring og afleveringsdokumentation.", after=15, line=220)
    m.bullet("Mennesker, økonomi og sikkerhed", "Daglig arbejdsfordeling, 1:1, MUS og lærlingeoplæring; fuldt P&L, APV, risikovurdering og LOTO. Python/Claude-værktøjer til planlægning og KS gav over 40 % produktivitetsløft.", after=15, line=220)

    m.job("Drifts- og vedligeholdelsesleder / værkstedstekniker", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          "24/7 kritisk procesdrift · pumper, HVAC, HV-tavler, drev og SCADA")
    m.bullet("Forebyggende vedligehold og driftsikkerhed", "Vedligehold, akut fejlfinding, kritikalitetsbaseret prioritering, reservedelsflow og lagerstyring i døgnbemandet anlæg.", after=15, line=220)
    m.bullet("Forbedring og sikkerhed", "5S, Standard Work, PDCA, LOTO, risikovurdering, APV og nærved-hændelsesopfølgning; koordinering af værksted og skiftehold.", after=15, line=220)

    # Side 3 — projects, education, methods and staged entry plan.
    m.page_break()
    m.resume_header(NAME, "Driftskompasset · Asset, portefølje og forbedring", CONTACT, "PROJEKTER, FAGLIGHED OG OPSTART")
    m.section("ERHVERVSERFARING · FORTSAT")
    m.job("Medejer og CTO / teknisk ansvarlig for AI-afdelingen", "Data Power Consultant ApS · København · 2024–nov. 2026 (sideløbende med ELOHVAC)", "4–10 personer · tekniske/industrielle applikationer · AI coding")
    m.bullet("Krav til idriftsættelse", "Ledte kundeleverancer fra behov og arkitektur til integration, commissioning, dokumentation og overdragelse; indførte fælles review- og teststandarder for AI-assisteret udvikling.", after=15, line=220)
    m.bullet("Matrixledelse og rapportering", "Samlede to sideløbende organisationers planer, prioriteringer og leverancer; brugte AI-assisterede arbejdsgange til ledelsesrapportering og beslutningsoplæg.", after=15, line=220)

    m.job("Senior commissioning engineer / projektleder, elsystemer", "Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024", "37 samtidige CAPEX-projekter · DKK 2–10 mio. pr. projekt · 25 specialister")
    m.bullet("Portefølje og økonomi", "Koordinerede fremdrift, budget, risiko og ressourcer på tværs af engineering, indkøb og site; månedsrapportering til ledelse og kunde via SAP ERP.", after=15, line=220)
    m.bullet("Kvalitet og energiforbedring", "FAT/SAT, IQ/OQ/PQ, ændrings-/afvigelsesdokumentation; nul kritiske fund ved aflevering. PDCA-program reducerede energiomkostninger 40 %.", after=15, line=220)

    m.job("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022", "11 samtidige installationsprojekter · 14-personers team")
    m.bullet("Fremdrift", "Kapacitetsplanlægning, daglige tavlemøder og flaskehalsanalyse; standardiserede arbejdsgange fra specifikation gennem produktion og montage til aflevering.", after=15, line=220)
    m.job("Elektromekaniker / produktionsteamleder", "ARJ Engineering · Teheran · dec. 2003–mar. 2010", "12 teknikere")
    m.bullet("Teknisk drift og team", "Fejlfinding og reparation af industrielle el-/mekaniske anlæg; skift, materialer og daglig koordinering af 12 teknikere.", after=15, line=220)

    m.section("UDDANNELSE, AUTORISATION OG CERTIFICERING")
    m.edu("B.Tech (EQF 6), Technology Management & Mechanical Engineering", "Copenhagen School of Marine Engineering & Technology Management · 2017–2022")
    m.edu("Elautoriseret maskinmester, LV/MV/HV", "Sikkerhedsstyrelsen · maj 2023")
    m.edu("PRINCE2 — certificeret projektleder", "AXELOS / PeopleCert")
    m.edu("Lean og Six Sigma", "Anvendt i praksis; ikke certificeret")

    m.section("VÆRKTØJER OG METODER")
    m.models_table("VEDLIGEHOLD, FORBEDRING OG STYRING", ("Område", "Anvendte metoder/systemer"), METHODS, widths=(2600, 7746), compact=True)

    m.section("FØRSTE 90 DAGE · FRA BASELINE TIL TVÆRGÅENDE RYTME")
    m.models_table("LEVERANCER OG KONTROLPUNKTER", ("Periode", "Arbejde og resultat"), FIRST90, widths=(1700, 8646), compact=True)
    m.para("Mål og tærskler fastlægges sammen med Operations Manager efter gennemgang af eksisterende data; ingen baseline eller gevinst forudsættes.", after=35, line=210)
    m.para("Bopæl: Måløv · indstillet på at flytte til Aarhus-området ved ansættelse · kørekort B", after=25, line=210, justify=False)

    # Side 4 — one evidence row per requirement.
    m.page_break()
    m.resume_header(NAME, "Operations Excellence Manager · Job 9762", CONTACT, "DOKUMENTERET MATCH MOD OPGAVEN")
    m.section("EVIDENS FRA DRIFTEN")
    table = m.models_table("OPERATIONS EVIDENCE", ("Krav", "Dokumenteret erfaring og anvendelse"), REQUIREMENTS,
                           widths=(3900, 6446), compact=True)
    header_props = table.rows[1]._tr.get_or_add_trPr()
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    repeat = OxmlElement("w:tblHeader")
    repeat.set(qn("w:val"), "true")
    header_props.append(repeat)

    return m.save(path, title="Ansøgning og CV — Samtank A/S, Operations Excellence Manager, job 9762",
                  subject=SUBJECT,
                  keywords="Operations Excellence; Process Manager; vedligehold; porteføljestyring; forbedring; Samtank; Aarhus")


if __name__ == "__main__":
    print(build())
