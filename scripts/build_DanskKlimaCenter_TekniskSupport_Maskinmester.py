# -*- coding: utf-8 -*-
"""Dansk Klima Center — Maskinmester til teknisk support på Haier varmepumper.
Jobfokuseret ansøgning først og evidensbaseret CV bagefter.
Kandidatens generelle support-/servicebaggrund er medtaget, men Haier-produktkendskab,
specifikke varmepumpeserier og kølemiddelcertifikater opfindes ikke.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")
OUTPUT = os.path.join(ROOT, "Shahram_Ajloo_DanskKlimaCenter_TekniskSupport.docx")
NAME = "SHAHRAM AJLOO"
TITLE = "Maskinmester · teknisk support · køl og klima"
CONTACT = "+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv"
DATE = "3. november 2026"

LETTER = [
    "En teknisk supportsag er først løst, når modtageren ved, hvad der skal gøres, løsningen virker i drift, og erfaringen kan bruges næste gang. Opslaget beskriver teknisk support som “en central del af vores service”. Samme supportfunktion skal give hurtig respons til en forhandler, der har brug for et præcist svar, og faglig sparring til en af jeres teknikere, der står ved anlægget. Kunderne skal mødes som samarbejdspartnere, ikke som sagsnumre.",
    "Jeg vil bygge sagen op omkring en enkel, fælles sagsstyring: registrér produkt og serienummer, installationsforhold, symptom og fejlkode; afklar hvad der allerede er kontrolleret; vurder sikkerhed og driftskritikalitet; og aftal ejer, næste handling og tidspunkt for tilbagemelding. Distributører og andre forhandlere skal have hurtig respons og løsningsorienteret rådgivning: Er sagen afklaret, eller skal en tekniker eller Haier-support kobles på? Teknikeren skal have en sparring, der kan omsættes til sikre målinger, tekniske løsninger og handlinger på stedet.",
    "Når en sag skal videre til Haier, for eksempel som en reklamation eller garantisag, bør den sendes med et brugbart teknisk grundlag: model, serienummer, driftsforhold, fejlkode, relevante målinger, udførte kontroller og dokumentation. Et tydeligt eskalationsspor reducerer gentagne spørgsmål og gør dialogen med leverandøren mere effektiv. Svar og afhjælpninger føres tilbage til den enkelte sag og til en versionsstyret guide, så vigtig viden ikke bliver hos én person.",
    "Supportfunktionen bør følge både svartid og kvalitet: hvor længe en sag venter på første svar, hvor ofte den genåbnes, hvad der gentager sig, og hvor mange sager der kræver eskalering. De tal skal bruges til at prioritere manualer, intern vidensdeling og tekniske møder — ikke som mål uden kontekst. Ved gentagne fejl skal support, teknikere og Haier sammen afklare årsag, løsning og forebyggelse.",
    "Flytningen fra Næstved til Fløng er også en anledning til at systematisere kontaktveje, sagsansvar, dokumenter og vidensbase, så distributørforretningen og kølevirksomheden bruger samme grundlag uden at miste deres forskellige behov. De første 30 dage kan bruges på at kortlægge sagstyper og følge forhandlere og teknikere; inden dag 60 kan en fælles sagsstruktur og de første fejlguides afprøves; inden dag 90 kan gentagne sager, svartider og feedback bruges til at prioritere næste forbedring. Den opbygning giver reel indflydelse på supportens arbejdsmåde og gør relationer, ordentlighed og et højt serviceniveau til en konkret standard, hvor vi løfter i flok — også når ansvaret for sagen er tydeligt placeret."
]

PROFILE = (
    "Elautoriseret maskinmester (LV/MV/HV) med praktisk el- og klimaerfaring, køleteknisk "
    "efteruddannelse og teknisk fejlfinding fra både installations- og døgnbemandet driftsmiljø. "
    "ELOHVAC: kundevendt service, installation, tavler, styring, fejlfinding og vedligehold på el-, "
    "ventilations- og klimaanlæg; daglig ledelse af fem elektrikere og tre lærlinge. Kandidaten har "
    "bekræftet erfaring med at opbygge/skalere kundeservice og teknisk support på tværs af kanaler, "
    "samt generel erfaring med reklamationer, garantisager og international leverandørdialog; konkrete omfang og tilskrivning "
    "til arbejdsgivere er ikke oplyst. Haier-specifik erfaring er ikke dokumenteret."
)

MATRIX = [
    ("Uddannet maskinmester med solid teknisk forståelse", "B.Tech i Technology Management & Mechanical Engineering samt dansk autorisation som elautoriseret maskinmester (LV/MV/HV). Hertil el- og maskinteknisk design, elteknik, og AMU i køleteknik og klimaanlæg."),
    ("Praktisk fejlsøgning på varme-, køle- og klimaanlæg", "ELOHVAC: praktisk installation, tavler, styring, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg. BIOFOS/Lynetten: pumper, HVAC, højspændingstavler, SCADA og akut fejlfinding i kritisk 24/7-drift."),
    ("Teknisk support til forhandlere og egne teknikere", "Kandidaten har bekræftet erfaring med opbygning/skalering af kundeservice og teknisk support på tværs af flere supportkanaler. ELOHVAC giver dokumenteret kundevendt teknisk service og sparring med elektrikere/lærlinge; konkrete supportkanaler, teamstørrelser og arbejdsgiverfordeling er ikke specificeret."),
    ("Dialog med Haier og deltagelse i tekniske møder", "Kandidaten har bekræftet international leverandørdialog og reklamations-/garantisager på tværs af roller, uden angivne leverandørnavne eller omfang. Direkte dialog med Haier eller kendskab til Haier-produkter er ikke dokumenteret."),
    ("Manualer, guides og intern vidensdeling", "ELOHVAC: KS-tjeklister, service- og afleveringsdokumentation samt AI-understøttede arbejdsgange. Novo Nordisk: sporbar test- og valideringsdokumentation. Specifik Haier-manual eller produktguide er ikke tidligere angivet; udvikling af den foreslås som en del af rollen."),
    ("Opbygge og udvikle en ny supportfunktion med selvstændigt ansvar; skabe struktur og retning",   "Brugerbekræftet erfaring med at opbygge eller skalere kundeservice og teknisk support på tværs af kanaler. ELOHVAC: fuldt P&L-ansvar, opgaveplanlægning, kvalitetsopfølgning og digitale værktøjer; konkrete teamstørrelser/KPI-resultater for support er ikke oplyst."),
    ("Skelne mellem forhandlernes behov og egne teknikeres behov",  "ELOHVAC dokumenterer erhvervskundedialog og teknisk service; Ventek-Air dokumenterer koordinering af 11 samtidige anlægsprojekter med 14-personers team. Opdelingen mellem DKC's forhandler- og teknikerkunder er hentet fra opslaget; tidligere DKC- eller distributørerfaring påstås ikke."),
    ("Dokumentere sager og følge op til løsning", "ELOHVAC: KS, kundeopfølgning og afleveringsdokumentation. Novo Nordisk: projekt- og testdokumentation i GMP-miljø, FAT/SAT og IQ/OQ/PQ med nul kritiske fund ved aflevering. Et bestemt ticketsystem eller CRM er ikke navngivet."),
    ("Køleteknisk forståelse og service på varme-/klimaanlæg", "AMU i køleteknik og klimaanlæg samt ELOHVAC-erfaring med ventilations- og klimaanlæg er dokumenteret. Specifik erfaring med Haier varmepumper, produktserier, kølemidler eller kølemiddelcertifikater fremgår ikke; produktoplæring hos DKC/Haier må derfor indgå i opstarten."),
    ("Service, kvalitet og relationer på tværs af organisationen", "ELOHVAC: kundedialog, tilbud, service, udførelse og opfølgning; Ventek-Air: daglig koordinering af team og underentreprenører; Novo: koordinering af 25 specialister. Samarbejde med kolleger og tekniske leverandører er dokumenteret på tværs af disse opgaver."),
    ("Kørekort og praktisk arbejdssted", "Kørekort B (manuelt gear) er dokumenteret. Bopæl er Måløv; Dansk Klima Centers kommende lokation i Fløng er gengivet fra opslaget. Ingen ændring af bopæl eller konkrete arbejdsdage er aftalt."),
]

EXPERIENCE = [
    ("Ejer / teknisk direktør / elautoriseret maskinmester", "ELOHVAC ApS · København · maj 2023–nu", "5 elektrikere + 3 lærlinge · fuldt P&L-ansvar", [
        "Kundevendt teknisk service og installation: tavler, styring, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg.",
        "Planlægger opgaver, materialer og underentreprenører; følger kvalitet, kundedialog og aflevering. Anvender LOTO, APV og risikovurdering.",
        "Python/Claude-værktøjer til tilbud, tidsplaner, KS-tjeklister og KPI-rapportering gav dokumenteret produktivitetsløft over 40 % i egne arbejdsgange."
    ]),
    ("Medejer og CTO / teknisk ansvarlig for AI-afdelingen", "Data Power Consultant ApS · København · 2024–2026 (sideløbende med ELOHVAC)", "Tekniske og industrielle applikationer", [
        "Ledte kundeløsninger fra behovsafklaring og integration til idriftsættelse, dokumentation og overdragelse; arbejdede med LLM-API'er og AI-agenter.",
        "Indførte fælles standarder for AI-assisteret udvikling, review og test; anvendte AI i ledelsesrapportering og matrixledelse."
    ]),
    ("Senior idriftsættelsesingeniør / projektleder, elsystem", "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024", "37 CAPEX-projekter · 25 specialister · DKK 2–10 mio. pr. projekt", [
        "Koordinerede scope, fremdrift, økonomi, risici og ressourcer; SAP ERP, teknisk dokumentation, FAT/SAT og IQ/OQ/PQ.",
        "Arbejdede med BMS/FMS i daglig drift og projekter, herunder alarmer/punktlister, ændringer og verifikation; nul kritiske fund ved aflevering."
    ]),
    ("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022", "11 samtidige ventilationsprojekter · 14-personers team", [
        "Ledte projekter fra specifikation til aflevering; daglige tavlemøder, kapacitetsplanlægning, koordinering af teknikere og underentreprenører samt kvalitet og dokumentation."
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
    ("Køl, klima og el", "Køleteknik/klimaanlæg og køleanlæg (AMU) · ventilation og klima · tavler · styring · el-fejlfinding · LV/MV/HV-autorisation"),
    ("Support og service", "Kundevendt teknisk service · fejlfinding · leverandør-/kundedialog · reklamations- og garantisager (brugerbekræftet generelt; uden omfangstal)"),
    ("Sagsdokumentation", "KS-tjeklister · afleverings- og testdokumentation · SAP ERP · Excel/Power Query · Power BI · Python/Claude API"),
    ("Proces og kvalitet", "FAT/SAT · IQ/OQ/PQ · LOTO · APV · risikovurdering · 5S · Standard Work · PDCA"),
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
    m.meta("Dansk Klima Center ApS · Teknisk support på Haier varmepumper")
    p = m._p(spacing_after=50, line=240, justify=False)
    m._run(p, "Ansøgning · teknisk support og opbygning af en fælles servicefunktion", bold=True)
    m.para("Til Dansk Klima Center,", after=25, justify=False)
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
    m.resume_header(NAME, "Maskinmester · teknisk service · køl og klima", CONTACT, "ERHVERVSERFARING")
    add_jobs(m, EXPERIENCE)
    m.section("UDDANNELSE OG CERTIFICERING")
    for title, detail in EDUCATION:
        m.edu(title, detail)
    m.section("ARBEJDSFORMER OG DIGITALE VÆRKTØJER")
    m.models_table("RELEVANTE VÆRKTØJER", ("Område", "Dokumenteret anvendelse"), TOOLS,
                   widths=(2700, 7646), compact=True)
    return m.save(path, title="Ansøgning og CV — Dansk Klima Center, teknisk support Haier varmepumper",
                  subject="Maskinmester · teknisk support · køl og klima · serviceudvikling",
                  keywords="Maskinmester; Dansk Klima Center; Haier; varmepumper; teknisk support; køleteknik; fejlfinding; service; distributør; teknikere; dokumentation")


if __name__ == "__main__":
    print(build())
