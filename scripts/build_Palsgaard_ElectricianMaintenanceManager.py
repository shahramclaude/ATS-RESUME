# -*- coding: utf-8 -*-
"""Palsgaard A/S — Electrician Maintenance Manager, Juelsminde.

Danish combined application + CV in the repository master design.
Style: opening AD (the operating-day test), structure Signal → prioritisation → execution → learning,
register Elvedligeholdets kontrolsløjfe. Evidence and proposals are kept distinct.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")
OUTPUT = os.path.join(ROOT, "Shahram_Ajloo_Palsgaard_ElectricianMaintenanceManager.docx")
NAME = "SHAHRAM AJLOO"
TITLE = "Electrician Maintenance Manager · elautoriseret maskinmester (LV/MV/HV)"
CONTACT = "+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv"
DATE = "3. november 2026"
RECIPIENT = "Palsgaard A/S · Technical Service · att. Technical Service Manager Jesper Kristensen"
SUBJECT = "Electrician Maintenance Manager · Juelsminde"

LETTER = [
    "På Palsgaards Juelsminde-site skal el-vedligehold kunne mærkes mindst muligt i produktionen: sikkert arbejde, høj oppetid og færre gentagne fejl, mens kundetilpassede løsninger fortsat leveres med den fødevarekvalitet og sikkerhed, som fødevare- og non-food-kunderne forventer. Det kræver, at akutte behov håndteres hurtigt uden at den planlagte vedligeholdelse og læringen fra fejl forsvinder i dagens kø.",
    "**Først skal teamet have ét fælles billede af arbejdet.** På tavlen mødes planlagte opgaver, akutte fejl, risici, kompetencer og adgang til anlægget. Hver opgave får en ansvarlig, en prioritet, en sikker arbejdsplan og en tydelig afslutning. Produktionsbehov og teknisk risiko afgør rækkefølgen sammen; faglig vurdering bliver synlig, og medarbejderne bringes ind, før løsningen fastlægges.",
    "**Dernæst skal fejl blive til forebyggelse.** Gennemgang af arbejdsordrer, alarmer, gentagne fejl og erfaringer giver et datagrundlag, der kan omsættes til ændret interval, inspektion, reservedel eller teknisk forbedring. KPI-definitioner fastlægges med teamet og produktionen; vedligeholdsperformance og vedligeholds-KPI’er følger oppetid, planopfyldelse, gentagne fejl, nedetid og energi i en fast kadence. Årsag og effekt dokumenteres, så tiltag ikke lukkes, før driften har vist, om de virker.",
    "**Dokumentation og eftersyn skal være en del af arbejdsordren.** Lovkrav, standarder, teknisk dokumentation og DKV-opgaver føres i en fælles oversigt med anlæg, interval, ansvarlig, planlagt dato, dokumentationskrav og lukning af afvigelser. Koordinering med relevante fag og eksterne serviceparter gør det muligt at planlægge kontroller uden at miste overblik over produktionens vinduer. El- og automatikprojekter føres fra scope og sikkerhedsafklaring til test, dokumentation og overdragelse til vedligehold.",
    "Palsgaards mission er “With a good workplace and advanced technology as our foundation” og “customer-tailored emulsifier and stabiliser solutions”; her skal el-vedligehold understøtte sikker, stabil og effektiv drift gennem en forebyggende og databaserede vedligeholdstilgang. Jeres værdier — **Loyalty, Responsibility, Commitment** — får derfor en konkret form i ansvar for aftaler, rettidig opfølgning, faglig udvikling og sikker drift. Energiindsatsen bør koble energiforbrug og teknisk ændring: først baseline og driftsforhold, dernæst afprøvning og dokumenteret effekt.",
    "**De første 90 dage** begynder med fælles gennemgang med de otte elektrikere og automatikteknikere, produktion, automation og Technical Service Manager. Uge 1–2: kortlæg opgavekø, anlægskritikalitet, eftersyn, åbne afvigelser og eksisterende KPI-definitioner. Dag 30: aftal prioriteringsregler, tavlerytme og baseline. Dag 60: afprøv én forbedringscyklus på et aftalt anlæg eller fejlmønster. Dag 90: gennemgå effekt og læring med teamet og aftal næste forbedringsportefølje. Måltal og tærskler fastsættes efter den faktiske baseline — ikke på forhånd."
]

PROFILE = (
    "Elautoriseret maskinmester (LV/MV/HV) med personlig godkendelse som fagligt ansvarlig på elområdet "
    "(kandidatoplysning) og erfaring fra industriel vedligeholdelse, teknisk projektleverance og daglig personaleledelse. "
    "Biofos/Lynetten: 24/7 kritisk procesdrift, forebyggende el- og mekanisk vedligehold, højspændingstavler, SCADA, "
    "reservedelsflow og sikkerhed. ELOHVAC: fem elektrikere og tre lærlinge, el-/HVAC-service, planlægning og fuldt P&L. "
    "Novo Nordisk: 37 samtidige CAPEX-projekter, 25 specialister, FAT/SAT og IQ/OQ/PQ; nul kritiske fund ved aflevering. "
    "40 % lavere energiomkostninger gennem PDCA hos Novo Nordisk. Indstillet på at flytte til Juelsminde-området ved ansættelse."
)

RESULTS = [
    ("24/7 vedligeholdsdrift", "Biofos/Lynetten · el- og mekanisk procesudstyr, forebyggende vedligehold, akut fejlfinding, reservedelsflow og sikkerhed."),
    ("40 % lavere energiomkostninger", "Novo Nordisk · dokumenteret PDCA-program med opfølgning på energi og driftsøkonomi."),
    ("37 CAPEX-projekter · 25 specialister", "Novo Nordisk · parallel fremdrift, økonomi, risiko, FAT/SAT og IQ/OQ/PQ; nul kritiske fund ved aflevering."),
    ("5 elektrikere + 3 lærlinge", "ELOHVAC · daglig arbejdsplanlægning, personaleudvikling, kvalitet, sikkerhed og fuldt P&L."),
]

EXPERIENCE = [
    ("Ejer / teknisk direktør / elautoriseret maskinmester", "ELOHVAC ApS · København · maj 2023–nu", "5 elektrikere + 3 lærlinge · fuldt P&L · elautorisation", [
        "Planlægger og leder el-teknisk service og forebyggende vedligehold på el-, tavle-, styrings-, ventilations- og klimaanlæg; prioriterer akutte og planlagte opgaver og følger op på kvalitet og aflevering.",
        "Daglig personaleledelse, 1:1, MUS, oplæring af lærlinge, APV og LOTO. Ansvar for tilbud, materialer, underentreprenører, serviceaftaler og økonomi.",
        "Byggede Python-/Claude-værktøjer til tilbudsberegning, planlægning, KS-tjeklister og KPI-rapportering; dokumenteret produktivitetsløft over 40 %."
    ]),
    ("Drifts- og vedligeholdelsesleder / værkstedstekniker", "Biofos (Lynetten) · København · aug. 2017–jan. 2022", "Kritisk 24/7 procesdrift · pumper, HVAC, højspændingstavler, SCADA", [
        "Forebyggende vedligehold og akut fejlfinding på el- og mekaniske anlæg; prioritering efter kritikalitet, driftsbehov og sikkerhed.",
        "Arbejdede med tilstands-/kritikalitetsbaseret vedligehold, reservedelsflow, lagerstyring, 5S, Standard Work og PDCA; LOTO, APV og risikovurdering i skifteholdsdrift."
    ]),
]

EXPERIENCE_MORE = [
    ("Medejer og CTO · teknisk ansvarlig for AI-afdelingen", "Data Power Consultant ApS · 2024–nov. 2026 · sideløbende med ELOHVAC", "4–10 personer", [
        "Ledte AI coding med LLM-API'er og AI-agenter til tekniske og industrielle applikationer, bl.a. design af anlæg/komponenter; brugte AI i ledelsesarbejdet og matrixledelse."
    ]),
    ("Senior idriftsættelsesingeniør / projektleder, elsystem", "Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024", "37 samtidige CAPEX-projekter · DKK 2–10 mio. pr. projekt · 25 specialister", [
        "Koordinerede el-projekter, fremdrift, budget, risici og tværfaglige ressourcer; SAP ERP og månedsrapportering. Tavler/styring, UPS, ABA/ABV og PDS; FAT/SAT, IQ/OQ/PQ, nul kritiske fund. PDCA: 40 % lavere energiomkostninger."
    ]),
    ("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022", "11 samtidige anlægsprojekter · 14-personers team", [
        "Daglige tavlemøder og kapacitetsprioritering fra specifikation til aflevering; fulgte økonomi, tidsplan og kvalitet."
    ]),
    ("Elektromekaniker / produktionsteamleder", "ARJ Engineering · Teheran · dec. 2003–mar. 2010", "12 mekanikere og teknikere", [
        "Fejlfinding på industrielle el-/mekaniske anlæg; vagtplanlægning, materialer og daglig teamopfølgning."
    ]),
]

METHODS = [
    ("El-fag og sikkerhed", "Elautoriseret maskinmester LV/MV/HV · personligt godkendt fagligt ansvarlig · tavler · styring · SCADA · LOTO · APV"),
    ("Vedligehold og kontrol", "Forebyggende vedligeholdelse · Drift, Kontrol og Vedligehold (DKV) · arbejdsordre/CMMS · eftersyn og afvigelsesopfølgning"),
    ("Forbedring og problemløsning", "PDCA · Lean · Six Sigma · 5S · Standard Work · A3 · 5xHvorfor · Ishikawa · rodårsagsanalyse · anvendt i praksis"),
    ("Ledelse og opfølgning", "Daglig planlægning · tavlemøder · vedligeholdsperformance · KPI-styring · medarbejderudvikling · medarbejderudvikling i praksis · MUS/1:1 · PRINCE2-certificeret projektleder"),
    ("Systemer og data", "SAP ERP · SCADA · CMMS/arbejdsordrer · Excel/Power Query · Python · Claude Code · KPI-rapportering"),
]

PLAN = [
    ("Uge 1–2", "Ejer: teamleder. Gennemgå skiftene, kritiske anlæg, åbne ordre, sikkerhed, eftersyn og kompetencer med teamet; afstem produktionsvinduer med Technical Service Manager."),
    ("Dag 30", "Ejer: teamleder + teamet. Aftal prioriteringsregler, ansvar, tavlerytme og baseline for oppetid, PM-planopfyldelse, gentagne fejl, nedetid og energi."),
    ("Dag 60", "Ejer: navngiven fagperson. Afprøv én fejlårsags-/forebyggelsescyklus og én DKV-opfølgning; gennemgå afvigelser, sikkerhed, reservedele og produktionsvindue."),
    ("Dag 90", "Ejer: teamleder. Vis effekt mod baseline, opdater standarder og kompetencebehov, luk eller eskalér handlinger, og aftal næste kvartals forbedrings- og projektportefølje."),
]

REQUIREMENTS = [
    ("Daglig ledelse og udvikling af otte elektrikere og automatikteknikere", "ELOHVAC: daglig ledelse af fem elektrikere og tre lærlinge, arbejdsfordeling, 1:1/MUS og oplæring; Biofos supplerer med ledelse i kritisk 24/7-skifteholdsdrift."),
    ("Prioritere planlagte og akutte vedligeholdsopgaver og skabe fremdrift her og nu", "Biofos: forebyggende og akut vedligehold på kritisk procesudstyr; ELOHVAC: prioritering af service og planlagte opgaver med ansvarlig, materialer og afslutning samme dag."),
    ("Sikre sikker, stabil og effektiv drift af elinstallationer og produktionsudstyr", "Elautoriseret maskinmester LV/MV/HV; tavler, styring, pumper, HVAC og SCADA i drift. LOTO, APV og risikovurdering indgår i planlægning og sikker udførelse."),
    ("Arbejde systematisk for bedre drift på længere sigt", "Biofos: kritikalitetsbaseret vedligehold, reservedelsflow, 5S, Standard Work og PDCA. Forbedringer følger fejlmønster og driftsrisiko frem for alene næste akutte opgave."),
    ("Omsætte data, fejl og erfaringer til læring og styrke forebyggende, databaseret vedligehold", "SCADA-/driftsinformation, fejlretning, PDCA, A3, 5xHvorfor og Ishikawa er anvendt. Arbejdsordrer og gentagne fejl omsættes til ejer, handling, frist og kontrol af gentagelse."),
    ("Synlig og tilgængelig ledelse, retning, prioriteter og beslutninger", "Ledelse på gulvet i ELOHVAC og Biofos' skifteholdsdrift; tavlemøder og direkte opfølgning gør prioriteringer og hjælp synlige i hverdagen."),
    ("Udvikle medarbejdernes faglighed og bruge teamets kompetencer", "ELOHVAC: medarbejderudvikling gennem MUS/1:1 og oplæring af tre lærlinge under daglig ledelse af fem elektrikere. Opgavefordeling kobles til faglige kompetencer og næste udviklingsbehov."),
    ("Sikre høj oppetid og reducere driftsforstyrrelser, fejl, nedetid og vedligeholdsomkostninger", "Fem år i kritisk 24/7-procesdrift hos Biofos med forebyggende vedligeholdelse og akut fejlfinding; kritikalitet og reservedelsflow indgik i prioriteringen af driftssikkerhed og driftsindsats."),
    ("KPI’er, data og konkrete forbedringer af effektivitet, energioptimering og drift", "ELOHVAC følger serviceaftaler på tid, kvalitet og leveringsevne; Novo månedsrapporterede fremdrift og økonomi. PDCA hos Novo gav 40 % lavere energiomkostninger."),
    ("Teknisk dokumentation, lovkrav, standarder og sikkerhedskrav", "ELOHVAC: KS og afleveringsdokumentation; Novo: FAT/SAT, IQ/OQ/PQ og nul kritiske fund ved 37 CAPEX-projekter. Krav følges gennem udførelse og overdragelse."),
    ("Planlægge og dokumentere lovpligtige eftersyn, koordinere DKV og følge op på kontroller", "Kandidaten bekræfter erfaring med tilsvarende kontrol-/eftersynsprocesser: planlægning, dokumentation og opfølgning. DKV, Drift, Kontrol og Vedligehold, organiseres med anlæg, interval, ejer, bevis og afvigelseslukning."),
    ("Lede og bidrage til tekniske projekter på el- og automatikområdet", "Novo: 37 samtidige el-/CAPEX-projekter fra specifikation til FAT/SAT og kvalificeret aflevering; ELOHVAC leverer el-tekniske service- og projektopgaver med fuldt P&L og KS."),
    ("Stærk el-faglig profil og industriel vedligeholdelse i produktionsmiljø", "Elautoriseret maskinmester med personlig elautorisation og autorisation på LV/MV/HV; electrical maintenance på Biofos' kritiske procesanlæg dokumenterer erfaring fra et industrielt produktionsmiljø."),
    ("Forstå teknikken og den produktionsvirkelighed, udstyret skal fungere i", "Biofos 24/7 og Novo Nordisks driftsnære CAPEX gav erfaring med at planlægge arbejde, test og overdragelse, så tekniske ændringer fungerer under produktionens krav."),
    ("Omsætte problemer og data til konkrete handlinger", "Fejlfinding og rodårsagsanalyse med PDCA kobler observation til årsag, handling og effektkontrol; Novo-programmet gav 40 % lavere energiomkostninger, og ELOHVAC-værktøjer over 40 % produktivitetsløft."),
    ("Kvalifikationer til fagligt ansvar på elområdet", "Brugeren bekræfter personlig godkendelse som fagligt ansvarlig på elområdet; master-CV dokumenterer desuden elautoriseret maskinmester LV/MV/HV og maskinmesteruddannelse."),
    ("Ledelseserfaring fra lignende rolle", "ELOHVAC: direkte personaleledelse af fem elektrikere og tre lærlinge; Biofos: vedligeholds-/driftsledelse i 24/7-anlæg; Ventek-Air: 14-personers team og 11 samtidige projekter."),
    ("Erfaring med automation og CMMS", "Dokumenteret arbejde med tavler, styring og SCADA hos Biofos og ELOHVAC samt arbejdsordre-/CMMS-data til opgaveprioritet, plan, fejl- og reservedelsinformation og status."),
    ("Erfaring med KPI-styring", "KPI-opfølgning på serviceaftaler i ELOHVAC samt projekt-, budget- og risikorapportering hos Novo. Definitioner og Palsgaards baseline fastlægges med teamet."),
    ("Erfaring med tavlemøder", "Daglige tavlemøder og kapacitets-/flaskehalsopfølgning i Ventek-Air; tavlen samlede opgaver, ansvar og næste handling på tværs af 11 samtidige anlægsprojekter."),
    ("Erfaring med Lean og systematisk problemløsning", "Lean/Six Sigma anvendt i praksis, ikke certificeret; Biofos 5S/Standard Work/PDCA samt A3, 5xHvorfor og Ishikawa understøtter systematisk problemløsning."),
    ("Rollemodel for Ansvarlighed, Engagement og Loyalitet", "Palsgaards Loyalty, Responsibility, Commitment kobles til at holde aftaler, følge op rettidigt og udvikle faglighed; sikker udførelse og tydeligt ejerskab ses i hverdagen."),
    ("Samarbejde med produktion, automation og øvrige tekniske funktioner", "Novo: 25 specialister på tværs af engineering, indkøb og site; Ventek-Air: 14-personers team på 11 anlæg. Samarbejdet styres gennem fælles plan og beslutningsejer."),
    ("Arbejdsstedet Palsgaard i Juelsminde", "Kandidaten er indstillet på at flytte til Juelsminde-området ved ansættelse; konkret tilstedeværelses- og flytteplan aftales i forbindelse med processen.")
]


def _add_jobs(m, jobs):
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope)
        for text in bullets:
            m.bullet("", text, after=12, line=210)


def build(path=OUTPUT):
    m = MasterDoc(TEMPLATE, lang="da-DK")
    # Page 1: task-led proposal, with no candidate biography or claimed past results.
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta(RECIPIENT)
    p = m._p(spacing_after=60, line=250, justify=False)
    m._run(p, SUBJECT, bold=True)
    m.para("Kære Jesper Kristensen", after=45, justify=False)
    for text in LETTER:
        m.para(text, after=45, line=215)
    m.meta("Med venlig hilsen", after=10)
    m.meta("Shahram Ajloo", after=0)

    # Page 2: core evidence and daily operations.
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "ELVEDLIGEHOLDETS KONTROLSLØJFE")
    m.section("PROFIL")
    m.para(PROFILE, after=30, line=215)
    m.section("DOKUMENTEREDE RESULTATER")
    for label, detail in RESULTS:
        m.bullet(label, detail, after=10, line=205)
    m.section("ERHVERVSERFARING")
    _add_jobs(m, EXPERIENCE)

    # Page 3: broader relevant experience, methods and 90-day operating plan.
    m.page_break()
    m.resume_header(NAME, "Elvedligeholdets kontrolsløjfe · faglig ledelse · forbedring", CONTACT, "ERFARING, FAGLIGHED OG OPSTART")
    m.section("ERHVERVSERFARING · FORTSAT")
    _add_jobs(m, EXPERIENCE_MORE)
    m.section("UDDANNELSE OG GODKENDELSER")
    m.edu("B.Tech (EQF 6), Technology Management & Mechanical Engineering", "Copenhagen School of Marine Engineering & Technology Management · 2017–2022")
    m.edu("Elautoriseret maskinmester (LV/MV/HV)", "Sikkerhedsstyrelsen · maj 2023 · elautorisation")
    m.edu("Fagligt ansvarlig på elområdet", "Personlig godkendelse bekræftet af kandidaten")
    m.edu("PRINCE2 · certificeret projektleder", "AXELOS / PeopleCert")
    m.edu("Lean og Six Sigma", "Anvendt i praksis; ikke certificeret")
    m.section("VÆRKTØJER, SIKKERHED OG KULTUR")
    METHODS = [
        ("Vedligehold", "Forebyggende · kritikalitetsbaseret · arbejdsordre/CMMS · planlagte eftersyn · afvigelsesopfølgning"),
        ("Problemløsning", "PDCA · Lean · Six Sigma · 5S · Standard Work · A3 · 5xHvorfor · Ishikawa; anvendt i praksis"),
        ("Drift og sikkerhed", "Tavler · styring · SCADA · LOTO · APV · risikovurdering · teknisk dokumentation · FAT/SAT · IQ/OQ/PQ"),
        ("Ledelse og data", "Daglig prioritering · tavlemøder · KPI-opfølgning · MUS/1:1 · kompetenceudvikling · SAP ERP · Excel · Python · Claude Code"),
        ("Palsgaards sprog", "Loyalty - Responsibility - Commitment · Heart working people · professional and efficient business partner · customer at the centre of our activities · proactively and in a timely manner · good workplace · With a good workplace and advanced technology as our foundation · customer-tailored emulsifier and stabiliser solutions · forebyggende og databaserede vedligeholdstilgang · ISO 50001 · FSSC 22000 · fødevaresikkerhed")
    ]
    m.models_table("ANVENDTE METODER OG ARBEJDSFORM", ("Område", "Værktøjer / praksis"), METHODS, widths=(2350, 7996), compact=True)
    m.section("FØRSTE 90 DAGE · FRA ARBEJDSKØ TIL LÆRING")
    m.models_table("EJER OG LEVERANCE", ("Periode", "Arbejde og kontrolpunkt"), PLAN, widths=(1500, 8846), compact=True)
    m.para("Baseline, KPI-definitioner og måltærskler fastlægges med teamet og Technical Service Manager efter gennemgang af eksisterende data.", after=20, line=200)
    m.para("Bopæl: Måløv · indstillet på at flytte til Juelsminde-området ved ansættelse · kørekort B", after=10, line=200, justify=False)

    # Page 4: complete evidence matrix, one row per requirement item.
    m.page_break()
    m.resume_header(NAME, "Electrician Maintenance Manager · dokumenteret evidens", CONTACT, "KRAV, METODE OG DOKUMENTATION")
    m.para("De foreslåede Palsgaard-arbejdsgange er adskilt fra nedenstående dokumenterede erfaring.", after=20, line=200)
    table = m.models_table("STILLINGENS KRAV OG KANDIDATENS EVIDENS", ("Krav i opslaget", "Dokumenteret erfaring og anvendelse"), REQUIREMENTS,
                           widths=(3650, 6696), compact=True)
    header_props = table.rows[1]._tr.get_or_add_trPr()
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    repeat = OxmlElement("w:tblHeader")
    repeat.set(qn("w:val"), "true")
    header_props.append(repeat)
    return m.save(path, title="Ansøgning og CV — Palsgaard Electrician Maintenance Manager",
                  subject=SUBJECT,
                  keywords="Electrician Maintenance Manager; elvedligehold; fagligt ansvarlig; forebyggende vedligehold; DKV; Palsgaard; Juelsminde")


if __name__ == "__main__":
    print(build())
