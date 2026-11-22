# -*- coding: utf-8 -*-
"""Silkeborg Forsyning — Maskinmester med el-teknisk profil.
Opgavefokuseret ansøgning først, efterfulgt af evidensbaseret CV.
Skelner mellem dokumenteret el-/procesdrift, PLC-relateret arbejde og konkret
PLC-programmering/SRO-erfaring, som ikke er specificeret i master-CV'et.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")
OUTPUT = os.path.join(ROOT, "Shahram_Ajloo_SilkeborgForsyning_MaskinmesterEl.docx")
NAME = "SHAHRAM AJLOO"
TITLE = "Maskinmester · el-teknik · drift og vedligehold"
CONTACT = "+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv"
DATE = "3. november 2026"

LETTER = [
    "Moderne varmeproduktionsanlæg med kraftvarme, solvarme, elkedler, varmepumper og biobrændsel stiller forskellige krav til drift, vedligehold og styring. Den fælles opgave er at sikre en stabil og klimavenlig energiforsyning og fjernvarmeproduktion, holde anlæggene sikre og tilgængelige, finde fejl hurtigt og gennemføre ændringer uden at miste overblikket over forsyningen.",
    "En praktisk driftsrutine kan samle vagtoverlevering, alarmer, åbne fejl, planlagte eftersyn og dagens arbejde på tværs af anlæggene. Ved en fejl bør første skridt være at bekræfte alarmen og procesforløbet, vurdere konsekvensen for anlæg og forsyning og derefter vælge mellem sikker fejlafhjælpning, eskalering eller planlagt stop. Gentagne fejl følges til årsag og korrigerende handling — ikke blot til alarmkvittering.",
    "Vedligeholdsplanen bør koble kritikalitet, fabrikantkrav, driftsdata, serviceeftersyn og reservedele. En fælles oversigt over opgaver, ansvar, frister og dokumentation gør det muligt at prioritere mellem produktionsanlæggene og at koordinere revisioner og eksterne leverandører. Efter udført arbejde registreres ændringer, test og driftsmæssig frigivelse, så næste vagt har et pålideligt grundlag.",
    "Automation og SRO kræver en kontrolleret ændringsvej: beskriv problem og ønsket funktion, afklar anlægsgrænse og sikker tilstand, gennemgå ændringen med driftskolleger og leverandør, test den aftalte funktion og opdatér dokumentationen. PLC-programmering udføres af den med den nødvendige platformserfaring og bemyndigelse; fejlfindingsdata og driftsbehov skal stadig samles, så ændringen løser den faktiske årsag.",
    "I de første uger bør introduktionen følge anlæggene, vagtinstrukserne, SRO-visningerne, el-dokumentationen og de vigtigste fejl- og vedligeholdshistorikker. Inden dag 30 kan åbne opgaver og kritiske reservedele samles i en prioriteret plan. Inden dag 60 kan én gentagen driftsforstyrrelse analyseres sammen med drift og leverandør; inden dag 90 gennemgås effekten, dokumentationen og de næste forbedringer. Det understøtter stabil og klimavenlig produktion, sikker drift, samarbejde og løbende forbedringer.",
    "En rådighedsvagt hver syvende uge bør efter oplæringen bygge på klare eskalationsveje, adgang til opdateret anlægsinformation og en dokumenteret overlevering mellem vagterne. Hændelser og ændringer registreres ensartet på tværs af Silkeborg Kraftvarmeværk og de øvrige produktionsanlæg, så erfaringer kan bruges i den daglige drift og ved kommende revisioner."
]

PROFILE = (
    "Elautoriseret maskinmester (LV/MV/HV) med el-teknisk uddannelse og praktisk erfaring fra "
    "kritisk 24/7-procesdrift, teknisk vedligehold og fejlfinding. BIOFOS/Lynetten: pumper, HVAC, "
    "højspændingstavler og SCADA i døgnbemandet spildevandsdrift. ELOHVAC: praktisk el-arbejde, "
    "tavler, styring, fejlfinding og forebyggende service. Har arbejdet med PLC-styrede anlæg i en "
    "teknisk ledelses-/projektkontekst; konkrete platforme og programmeringsansvar er ikke specificeret. "
    "Erfaring med projektkoordinering, dokumentation, sikkerhed og leverandørsamarbejde supplerer den "
    "praktiske driftsbaggrund."
)

MATRIX = [
    ("Uddannet maskinmester med interesse for el-teknik, automation og styring", "B.Tech i Technology Management & Mechanical Engineering samt dansk elautorisation som elautoriseret maskinmester (LV/MV/HV). Hertil el- og maskinteknisk design, elteknik, fra Tehran Technical University. Praktisk el- og styringserfaring er beskrevet i ELOHVAC-afsnittet; PLC-programmering er ikke påstået."),
    ("Daglig drift, overvågning og teknisk opfølgning på flere produktionsanlæg", "BIOFOS/Lynetten: næsten 4½ år i kritisk, døgnbemandet procesdrift med SCADA-overvågning, pumper, HVAC og højspændingstavler. Erfaringen er fra spildevandsanlæg og overføres til energiproduktion efter introduktion til de konkrete anlæg og driftsgrænser."),
    ("Fejlfinding, service og mindre reparationer på elektriske installationer og hjælpeudstyr", "ELOHVAC omfatter praktisk el-fejlfinding, installation, tavler, styring og forebyggende vedligehold på el-, ventilations- og klimaanlæg. BIOFOS omfatter akut fejlfinding og forebyggende vedligehold på elektriske og mekaniske anlæg."),
    ("Automation, PLC-programmering og SRO-styring", "SCADA-overvågning på BIOFOS samt erfaring med arbejde omkring PLC-styrede anlæg er dokumenteret. Konkrete PLC-platforme, programmeringsansvar og Silkeborg Forsynings SRO-system er ikke specificeret i kilde-CV'et; de læres gennem oplæring og udføres efter lokale ændrings- og adgangsregler."),
    ("Optimering af anlæg, styringer og driftsprocesser", "ELOHVAC følger tekniske serviceopgaver fra fejlfinding til aflevering. Hos Novo Nordisk koordinerede kandidaten 37 CAPEX-projekter og bidrog til PDCA, der reducerede energiomkostninger med 40 % i den pågældende organisation; resultatet tilskrives ikke Silkeborg Forsyning."),
    ("Planlagt vedligehold, revisioner og tekniske projekter", "BIOFOS: forebyggende vedligehold, reservedelsflow og 24/7-opfølgning. ELOHVAC: planlægning, materialer, underentreprenører og aflevering. Novo Nordisk: scope, fremdrift, risiko og ressourcer på tværs af 37 samtidige CAPEX-projekter."),
    ("Dokumentation af udførte opgaver, ændringer og tekniske løsninger", "ELOHVAC: KS-tjeklister og afleveringsdokumentation. Novo Nordisk: FAT/SAT, IQ/OQ/PQ og sporbare test-/valideringsregistre med nul kritiske fund ved aflevering. BIOFOS: standardiseret vedligehold og sikkerhedsregistreringer i skifteholdsdrift."),
    ("Samarbejde med driftskolleger og eksterne leverandører", "ELOHVAC: daglig planlægning af fem elektrikere og tre lærlinge samt koordinering med kunder og underentreprenører. Ventek-Air: 14-personers team og 11 samtidige anlægsprojekter. Novo Nordisk: tværfaglig koordinering af 25 specialister."),
    ("Rådighedsvagt på alle anlæg hver 7. uge efter oplæring", "BIOFOS-erfaring fra døgnbemandet skifteholdsdrift og akut teknisk fejlfinding er relevant baggrund. Kandidatens konkrete mulighed for at indgå i den beskrevne vagtrotation er ikke bekræftet i master-CV'et; vagtrutiner og oplæring er derfor ikke fremstillet som aftalt."),
    ("Kørekort til personbil og fortrolig med it som arbejdsredskab", "Kørekort B er dokumenteret. Digitale værktøjer omfatter Excel/Power Query, Power BI, SAP ERP, Python og Claude API. Bopæl er Måløv; opslagets krav om maksimalt 30 minutters kørsel til Silkeborg er ikke dokumenteret eller påstået, så det praktiske fremmødekrav skal afklares før ansøgning."),
    ("Kunne være på arbejdsstedet inden for maksimalt 30 minutters kørsel", "Bopæl er Måløv. Silkeborg Forsynings opslag angiver maksimalt 30 minutters kørsel; kandidaten har ikke bekræftet en flytning eller anden løsning, der opfylder dette krav. Afstandskravet er derfor ikke fremstillet som opfyldt."),
]

EXPERIENCE = [
    ("Ejer / teknisk direktør / elautoriseret maskinmester", "ELOHVAC ApS · København · maj 2023–nu", "5 elektrikere + 3 lærlinge · fuldt P&L-ansvar", [
        "Udfører og planlægger el-tekniske service- og entrepriseopgaver: installation, tavler, styring, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg.",
        "Koordinerer medarbejdere, materialer, kunder og underentreprenører fra tilbud til KS og aflevering; anvender LOTO, APV og risikovurdering.",
        "Python/Claude-værktøjer til tilbudsberegning, tidsplaner, KS-tjeklister og KPI-rapportering gav dokumenteret produktivitetsløft over 40 % i egne arbejdsgange."
    ]),
    ("Medejer og CTO / teknisk ansvarlig for AI-afdelingen", "Data Power Consultant ApS · København · 2024–2026 (sideløbende med ELOHVAC)", "AI-afdeling · tekniske og industrielle applikationer", [
        "Ledte kundeløsninger fra behovsafklaring og integration til idriftsættelse, dokumentation og overdragelse; arbejdede med LLM-API'er og AI-agenter.",
        "Indførte fælles standarder for AI-assisteret udvikling, review og test; anvendte AI i ledelsesrapportering og matrixledelse."
    ]),
    ("Senior idriftsættelsesingeniør / projektleder, elsystem", "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024", "37 CAPEX-projekter · 25 specialister · DKK 2–10 mio. pr. projekt", [
        "Koordinerede scope, fremdrift, omkostninger, risici og ressourcer på tværs af engineering, indkøb og anlæg; fulgte data i SAP ERP.",
        "Arbejdede med el-tavler, styring, UPS samt FAT/SAT og IQ/OQ/PQ. PDCA-program reducerede energiomkostninger med 40 % i den pågældende organisation."
    ]),
    ("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022", "11 samtidige anlægsprojekter · 14-personers team", [
        "Koordinerede projekter fra specifikation til aflevering med daglige tavlemøder, kapacitetsplanlægning, materialer, underentreprenører og dokumentation."
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
    ("El og anlæg", "LV/MV/HV-autorisation · el-fejlfinding · tavler · styring · pumper · HVAC · højspændingstavler"),
    ("Drift og sikkerhed", "24/7-procesdrift · SCADA-overvågning · forebyggende vedligehold · LOTO · APV · risikovurdering · nærved-hændelser"),
    ("Styring og automation", "Arbejde omkring PLC-styrede anlæg; konkrete platforme og programmeringsomfang ikke specificeret. SRO-/PLC-konfiguration læres efter lokale procedurer."),
    ("Data og forbedring", "Excel/Power Query · Power BI · SAP ERP · Python · Claude API · PDCA · 5S · Standard Work · A3"),
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
    m.meta("Silkeborg Forsyning · att. Anders Dyhr · Maskinmester med el-teknisk profil")
    p = m._p(spacing_after=50, line=240, justify=False)
    m._run(p, "Ansøgning · drift, vedligehold og el-teknisk udvikling", bold=True)
    m.para("Kære Anders Dyhr og Silkeborg Forsyning,", after=25, justify=False)
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
    m.resume_header(NAME, "Maskinmester · el-teknisk drift · vedligehold", CONTACT, "ERHVERVSERFARING")
    add_jobs(m, EXPERIENCE)
    m.section("UDDANNELSE OG CERTIFICERING")
    for title, detail in EDUCATION:
        m.edu(title, detail)
    m.section("ARBEJDSFORMER OG DIGITALE VÆRKTØJER")
    m.models_table("RELEVANTE VÆRKTØJER", ("Område", "Dokumenteret anvendelse"), TOOLS,
                   widths=(2700, 7646), compact=True)
    return m.save(path, title="Ansøgning og CV — Silkeborg Forsyning, maskinmester med el-teknisk profil",
                  subject="Maskinmester · el-teknik · energiproduktion · drift og vedligehold",
                  keywords="Maskinmester; Silkeborg Forsyning; fjernvarme; el-teknik; automation; PLC; SRO; drift; vedligehold; fejlfinding")


if __name__ == "__main__":
    print(build())
