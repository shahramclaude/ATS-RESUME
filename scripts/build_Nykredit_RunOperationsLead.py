# -*- coding: utf-8 -*-
"""
Nykredit — Run Operations Lead, Process Automation / Intelligent Automation.
Nordhavn, København. Dansk JD. Bygget i designet fra master-CV'erne og efter
den bindende regel: dokumentet handler om opgaven, missionen og stillingen —
ikke om ansøgeren. Side 1 = "Kravet → Løsningen er" + "Systemet er allerede bygget".
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Run Operations Lead | Intelligent Automation | Nykredit"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv")

DATE = "31. oktober 2026"
RECIPIENT = ("Nykredit · Intelligent Automation / Process Automation · Sundkrogsgade 25, 2150 "
             "Nordhavn · Att.: Andreas Larsen")
SUBJECT = "Ansøgning: Run Operations Lead — Nykredits automatiserings-CoE"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Opgaven er at gøre en automatiseringsplatform driftssikker: tydeligt ejerskab, ensartet struktur og en "
    "daglig drift, der ikke afhænger af, hvem der tilfældigvis husker det. Det betyder miljøer og adgange "
    "med navn på, kontroller der faktisk bliver kørt, monitorering der fanger fejl før forretningen gør, og "
    "dokumentation og overdragelse, så en løsning kan overtages af en, der ikke har bygget den. Med et "
    "driftsteam i Polen er det rammerne — ikke nærheden — der binder driften sammen.",

    "Nedenfor er min læsning af stillingen og det system, der ligger klar: runbook pr. løsning, miljø- og "
    "adgangsmatrix, kontrol- og monitoreringsplan, dokumentations- og overdragelsesskabelon, PLC-forløb med "
    "gates og en driftstavle med de rigtige KPI'er.",
]

BULLETS = [
    ("Kravet: primært ansvar for drift og projektopgaver — og koordinering på tværs",
     "Løsningen er en runbook pr. løsning og en fast driftsrytme: hvem har vagten, hvad kontrolleres "
     "dagligt og ugentligt, hvad eskaleres hvorhen, og et fælles backlog-møde hvor drifts- og "
     "projektopgaver prioriteres i samme billede. Er driften fordelt på flere lande, skal rytmen stå "
     "skriftligt."),

    ("Kravet: videreudvikle PLC-processen for automatiseringsløsninger",
     "Løsningen er et livscyklusforløb med gates: behov → vurdering → byg → test → go-live → drift → "
     "ændring → afvikling. Hver gate har en ejer, en dokumentation og en godkendelse, og en ændringslog "
     "sikrer, at ingen løsning ændrer sig, uden at nogen ved det — det er den proces, der gør en "
     "portefølje forvaltbar i stedet for bare stor."),

    ("Kravet: administrere Power Platformen — miljøer, adgange, kontroller og monitorering",
     "Løsningen er en miljø- og adgangsmatrix: hvilke miljøer der findes og hvad de bruges til, hvem der må "
     "hvad, hvordan adgang tildeles og fjernes ved onboarding og exit, hvilke kontroller der køres og hvor "
     "ofte, og hvem der ejer hver applikation. Monitorering sættes på kørsler og fejl med alarm til ejeren "
     "— ikke til en fællespostkasse."),

    ("Kravet: organisere Citizen Development med rammer for dokumentation, overdragelse og support",
     "Løsningen er en trappemodel med tre niveauer — ide, godkendt og produktionssat — med en fast "
     "dokumentationsskabelon, en overdragelsescheckliste (adgang, datakilder, logik, kontakt, backup) og en "
     "supportmodel med responstider. Så bliver citizen-løsninger en del af porteføljen, ikke private "
     "værktøjer."),

    ("Kravet: omsætte behov til processer, standarder og ansvarsfordelinger",
     "Løsningen er RACI pr. proces, en beslutningslog og et fast forum med forretning, platform, sikkerhed "
     "og drift: hvem beslutter, hvem rådgiver, hvem informeres. Samarbejdspartnere får en rolle, der er "
     "skrevet ned, så governance bliver rammen, forretningen kan bygge videre i."),
]

SYSTEM = ("Systemet er allerede bygget i min egen praksis: runbook- og overdragelsesskabelon, kontrol- og "
          "monitoreringsplan, ændringslog, dokumentationsstandard og en driftstavle med hændelser, "
          "responstid og gentagne fejl. Det er bygget med de værktøjer, CoE'en selv arbejder med: Power BI "
          "til monitorering, Excel og SharePoint som datagrundlag, Python og Claude til automatiseret "
          "rapportering. Jeg har ikke administreret Power Platform i en koncern; jeg har bygget de rammer, "
          "der gør, at en platform kan driftes af flere end den, der byggede den.")

MIRROR = ("Om kravene: solid erfaring med drift, forvaltning og koordinering fra tekniske miljøer med "
          "myndighedskrav og dokumentationspligt; forståelse for governance og for at omsætte behov til "
          "processer, standarder og ansvarsfordelinger; struktureret, ansvarstagende og vant til at samle "
          "løse ender og følge opgaver til dørs; kan koordinere på tværs af tekniske og forretningsmæssige "
          "miljøer, også når de sidder i forskellige lande; dansk på modersmålsniveau og engelsk "
          "professionelt.")

HONEST = ("To ting påvirker opgaven og skal siges ligeud: jeg har ikke arbejdet med UiPath eller "
          "administreret Power Platform i en koncern. Min automationserfaring er selvbygget — Python, Claude "
          "API, Power BI og Excel — og min driftserfaring kommer fra tekniske miljøer, hvor egenkontrol, "
          "adgangsstyring og dokumentation var myndighedskrav, ikke god praksis. Disciplinen er den samme: "
          "navn på ejerskab, kontrol før fejl, dokumentation ved overdragelse. Værktøjerne læres ved at sidde "
          "med miljøerne.")

CULTURE = ("Hvorfor Nykredit og Intelligent Automation: ambitionen om at skabe synlig og hurtig værdi for "
           "kunder og kolleger kræver den modsatte bevægelse af det, man skulle tro — nemlig stabilitet i "
           "bunden. En platform, der fejler i det stille, skaber ikke hurtig værdi, og løbende forbedringer "
           "forudsætter, at nogen holder standarden. Når I skriver, at faglig kvalitet, sammenhold og humor "
           "er vigtige, er det præcis den kombination, governance-arbejde har brug for.")

PRACTICAL = ("Praktisk: bosat i Måløv, et kvarters kørsel fra Nordhavn; dansk på modersmålsniveau og engelsk "
             "professionelt, hvilket er nødvendigt med et driftsteam i Polen; kort opsigelse og klar til "
             "hurtigt start; egen virksomhed afvikles ved ansættelse.")

CLOSING = ("Jeg vil gerne høre, hvordan driften er organiseret i dag, og bruge den første samtale på tre "
           "spørgsmål: hvordan PLC-processen ser ud nu, hvem der ejer applikationerne, og hvordan miljøer og "
           "adgange bliver kontrolleret i praksis.")

# ------------------------------------------------------------------ CV
PROFILE = ("Rollen kræver fire ting på én gang: ejerskab over en daglig drift, der er fordelt på flere "
           "personer og lande, evnen til at gøre en livscyklus og en platform forvaltbar, rammer for "
           "citizen development og dokumentation, og en koordinering, der holder både forretning og "
           "teknik sammen. Alle fire har været en del af arbejdet i tyve år: 40+ serviceanlæg og 5 "
           "elektrikere i egen autoriseret virksomhed med fuldt P&L-ansvar, 24/7-drift med SAP og "
           "KPI'er på Biofos Lynetten, og 37 samtidige anlægsprojekter i et GMP-miljø hos Novo Nordisk, "
           "hvor ændringer krævede change control og dokumentation. Elautoriseret maskinmester "
           "(LV/MV/HV), B.Tech i Technology Management & Mechanical Engineering, dansk på modersmålsniveau "
           "og engelsk professionelt.")

PRACTICE = [
    ("Drift og forvaltning",
     "Driftsrytme med daglige og ugentlige kontroller, runbook pr. løsning, vagt- og "
     "eskaleringsmodel, fælles backlog for drift og projekt, og en fast gennemgang af gentagne fejl."),

    ("PLC og livscyklus",
     "Gates fra behov til afvikling med ejer, dokumentation og godkendelse ved hver overgang; "
     "ændringslog, versionsstyring og beslutningslog, så en løsning kan revideres bagud."),

    ("Power Platform-rammer",
     "Miljø- og adgangsmatrix, on/offboarding af adgange, kontrolplan med kadence og ansvarlig, "
     "monitorering af kørsler og fejl med alarm til applikationsejer, ejerskab dokumenteret pr. app."),

    ("Citizen Development",
     "Trappemodel med tre niveauer (ide, godkendt, produktionssat), dokumentationsskabelon, "
     "overdragelsescheckliste og supportmodel med responstider — så løsninger ikke bliver "
     "personafhængige."),

    ("Governance og standarder",
     "RACI pr. proces, faste fora med forretning, platform, sikkerhed og drift, beslutningslog og "
     "ensartede standarder for, hvad der må bygges, og hvordan det forvaltes."),

    ("Dokumentation og overdragelse",
     "Én dokumentationsstandard pr. løsning: formål, datakilder, logik, adgange, kontrolpunkter, "
     "kontaktperson og kendte begrænsninger — skrevet så en ny kollega kan overtage uden møde."),

    ("Monitorering og KPI",
     "Hændelser og responstid, kørsler og fejlrate, andel af løsninger med dokumenteret ejer og seneste "
     "kontrol i Power BI — få tal, men de rigtige, rapporteret månedligt til ledelsen."),

    ("Automatisering i praksis",
     "Python og Claude API til rapportering og databehandling, Power BI-dashboards, Excel-modeller og "
     "SharePoint som datagrundlag; dokumenterede løft på +40 % produktivitet og −40 % energikost."),
]

FIRST90 = [
    ("Uge 1–2",
     "Driftsteamet i Polen og nøglepersonerne i København og Aalborg mødt; løsningsporteføljen, "
     "miljøerne, adgangene, de åbne hændelser og den nuværende PLC-dokumentation gennemgået — hvad "
     "findes, og hvad mangler."),
    ("Uge 3–6",
     "Runbook og driftsrytme aftalt med driftsteamet; miljø- og adgangsmatrix i første version; "
     "monitorering sat på de mest kritiske løsninger, så fejl bliver set af os og ikke af forretningen; "
     "PLC-gates dokumenteret som de ser ud i dag, før de ændres."),
    ("Uge 7–12",
     "Kontrolplanen kørt en hel cyklus med registrering, så vi ved hvad der faktisk bliver kontrolleret og "
     "hvad der kun står i planen; dokumentations- og overdragelsesskabelon i brug på nye løsninger; "
     "citizen development-rammen med tre niveauer og supportmodel aftalt med driftsteamet; driftstavle med "
     "baseline for hændelser og responstid."),
    ("Måned 3–6",
     "Adgangsreview gennemført, og ejerskab dokumenteret for hele porteføljen; gentagne hændelser "
     "analyseret med årsag og rettet ved kilden; beslutningslog og RACI på plads i de faste fora."),
    ("Måned 6–12",
     "Driften har målbare forbedringer: færre hændelser, hurtigere responstid og kontrol uden "
     "overskridelser; nye citizen-løsninger kommer i produktion gennem rammen i stedet for ved siden af "
     "den, og driftsbyrden pr. løsning er dokumenteret, så kapacitet kan planlægges."),
    ("Måned 12+",
     "Platformen er forvaltbar på tværs af lande: én standard, ét ejerskab, ét sæt KPI'er — og kapaciteten "
     "bruges på professionalisering og nye teknologier i stedet for brandslukning."),
    ("Løbende",
     "Månedlig driftsrapport med hændelser, responstid, kontrolstatus og dokumenteret ejerskab; "
     "kvartalsvis adgangsreview med sikkerhed; og en fast post på dagsordenen i de faste fora, hvor nye "
     "løsninger godkendes mod de rammer, der er aftalt."),
]

MODELS = [
    ("Driftsstyring",
     "Runbook pr. løsning, driftsrytme og vagtmodel, eskalationsveje, backlog for drift og projekt, "
     "root cause på gentagne hændelser, månedlig driftsrapport"),
    ("Livscyklus (PLC)",
     "Gate-model fra behov til afvikling, ejer og godkendelse pr. gate, ændringslog, versionsstyring, "
     "beslutningslog, dokumentation ved hver overgang"),
    ("Platformsadministration",
     "Miljøstrategi og -matrix, roller og adgangsstyring, on/offboarding, kontrolplan med kadence, "
     "monitorering af kørsler og fejl, alarm til applikationsejer"),
    ("Citizen Development",
     "Trappemodel (ide, godkendt, produktionssat), dokumentationsskabelon, overdragelsescheckliste, "
     "supportmodel og responstider, kompetencekrav til citizen developers"),
    ("Governance",
     "RACI pr. proces, beslutningsfora med forretning, platform, sikkerhed og drift, standarder for "
     "hvad der må bygges, risiko- og kontrolvurdering, revisionsspor"),
    ("KPI & rapportering",
     "Hændelser og responstid, fejlrate og kørsler, kontrolstatus og dokumenteret ejerskab, "
     "Power BI-dashboards, Excel-modeller, ledelsesrapportering"),
    ("Automatisering & værktøj",
     "Python og Claude API til rapportering og databehandling, Excel og SharePoint som datagrundlag, "
     "Power BI til monitorering, strukturerede tjeklister og logfiler"),
    ("Procesoptimering",
     "PDCA og 5S, standardarbejde, A3 og fem-hvorfor, proceskortlægning og RACI ved ændringer, "
     "før/efter-målinger på tid, kvalitet og fejl"),
]

ACHIEVEMENTS = [
    ("Drift med nul uplanlagte stop",
     "24/7-anlæg i fem år — oppetid gennem forebyggende kontrol, faste eftersyn og hurtig eskalation."),
    ("Ejerskab og dokumentation som krav",
     "myndigheds- og GMP-miljø, hvor adgang, ændringer og afvigelser skulle kunne dokumenteres bagud — "
     "nul kritiske fund ved aflevering på 37 projekter."),
    ("Standardarbejde indført",
     "5S, standardiserede tjeklister og proceskortlægning i drift og produktion; samme arbejde udført "
     "ens uanset hvem der var på vagt."),
    ("+40 % produktivitet",
     "gennem dataunderstøttet planlægning og egen AI-tooling — målt over tid og fastholdt."),
    ("Automatiseret rapportering",
     "Python- og Claude-baserede værktøjer, der samler status og afvigelser fra SAP, CMMS og Excel — "
     "rapportering på minutter i stedet for en arbejdsdag."),
]

EXPERIENCE = [
    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "40+ serviceanlæg · 5 elektrikere og 3 lærlinge · fuldt P&L, leverandør- og serviceaftaler",
     [("Drift og forvaltning",
       "daglig drift af 40+ anlæg med runbook, tjeklister og prioritering; egenkontrol og "
       "dokumentationspligt efter myndighedskrav."),
      ("Standarder og dokumentation",
       "ensartede arbejdsgange, adgang til anlæg og registrering af udført arbejde; dokumentation der kan "
       "vises ved tilsyn."),
      ("Automatisering og rapportering",
       "ERP-baseret ordre- og reservedelsstyring, Power BI-dashboards og Python/Claude-værktøjer til "
       "status, tjeklister og rapportering; produktivitetsløft over 40 %."),
      ("Koordinering",
       "kunder, leverandører og servicepartnere koordineret mod samme tidsplan; fuldt ansvar for "
       "bundlinjen.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · drifts- og "
     "vedligeholdelsesbudgetter i SAP",
     [("Kontrol og monitorering",
       "PDCA-baseret vedligeholdsplan med fast årshjul og KPI'er i SAP ERP; A3-root-cause på større "
       "nedetid, så fejlen blev rettet ved kilden."),
      ("Adgang og sikkerhed",
       "arbejdstilladelser, LOTO og adgangsstyring på et aktivt anlæg; near-miss-rapportering og "
       "opfølgning."),
      ("Koordinering på tværs",
       "egne teknikere, entreprenører og leverandører styret mod samme plan og samme dokumentation.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister inden for teknik, indkøb og drift · "
     "GMP/FDA/EMA",
     [("Change control og dokumentation",
       "ændringer, afvigelser og CAPA håndteret i et reguleret miljø, hvor alt skulle kunne spores — "
       "nul kritiske fund ved aflevering."),
      ("Koordinering af specialister",
       "25 specialister på tværs af mekanik, el, proces og indkøb; beslutninger dokumenteret, så alle "
       "arbejdede efter samme aftale."),
      ("Standarder og overlevering",
       "FAT/SAT, IQ/OQ/PQ og valideringsdokumentation — overlevering, der kunne overtages af driften "
       "uden mundtlig overlevering.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Standardarbejde",
       "standardiseret arbejde ved hver station og daglige tavlemøder over 11 samtidige projekter."),
      ("Sikkerhed og dokumentation",
       "arbejdstilladelser og sikkerhedsdokumentation ved montage i bygninger, hvor driften kørte "
       "videre.")]),

    ("Elektromekaniker / Produktionsteamleder",
     "ARJ Engineering · Teheran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · skiftplanlægning, materialestyring og lager",
     [("Planlægning og opfølgning",
       "skiftplanlægning, materialestyring og målopfølgning med situationel coaching."),
      ("Struktureret problemløsning",
       "reparation og diagnosticering gennem struktureret root cause-analyse.")]),
]

EDUCATION = [
    ("B.Tech (EQF niveau 6) — Technology Management & Mechanical Engineering",
     "Maskinmesterskolen / Copenhagen School of Marine Engineering & Technology Management · 2017 – 2022 · "
     "karakter 7,6/12"),
    ("Elektrisk & mekanisk design, el-ingeniør (EQF niveau 6)",
     "Tehran Technical University · 2000 – 2003"),
    ("HF — matematik og fysik",
     "VUC · 2012 – 2017"),
]

CERTS = [
    ("Elautoriseret maskinmester (LV/MV/HV)",
     "Sikkerhedsstyrelsen · maj 2023"),
    ("Køle- og HVAC-teknik (AMU)",
     "Mercantec · mar. 2021"),
    ("Arbejdsmiljø §16 og sikkerhedsbevidsthed (VI/6-1)",
     "Søfartsstyrelsen · maj 2021"),
    ("Lean — værdistrømsanalyse, standardarbejde, 5S, A3 og Kaizen",
     "Anvendt i drift · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og projekter · 2017 – nu"),
    ("STCW — maskinrumsvagt (A-III/1), skibssikkerhedsofficer (VI/5)",
     "Søfartsstyrelsen · 2021 – 2023"),
]

LANGUAGES = "Dansk (modersmål) · Engelsk (professionelt, skriftligt og mundtligt) · Persisk/farsi · Kørekort B"

REFERENCES = "Tidligere ledere hos Biofos (Lynetten), Novo Nordisk A/S (Kalundborg) og egne kunder i ELOHVAC — oplyses ved henvendelse."

KEYWORDS = (
    "Run Operations Lead · Run Operations · Drift · Forvaltning · Koordinering · Automatisering · "
    "Automatiseringsteknologier · Intelligent Automation · Process Automation · CoE · "
    "Automatiserings-CoE · PLC-processen · PLC · Livscyklus · Power Platform · UiPath · Miljøer · "
    "Miljøstrategi · Adgange · Adgangsstyring · Kontroller · Monitorering · Ejerskab · Løsningsejerskab · "
    "Citizen Development · Dokumentation · Overdragelse · Support · Governance · Standarder · "
    "Ansvarsfordeling · RACI · Interessenter · Driftsteam · Projektopgaver · Procesoptimering · "
    "Effektive Løsninger · Robust Drift · Stabil Drift · Struktureret · Ansvarstagende · Selvstændig · "
    "Løsningsorienteret · Overblik · Samarbejdspartner · Kommunikator · KPI · Rapportering · Power BI · "
    "Excel · SharePoint · Python · Claude · SAP · IT · Dansk · Engelsk · København · Nordhavn · "
    "Aalborg · Polen · Nykredit · Finansiel Sektor"
)


def build(path):
    m = MasterDoc(TEMPLATE, lang="da-DK")

    # ---------------------------------------------------------------- side 1
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta(RECIPIENT)

    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, SUBJECT, bold=True, color="1A1A1A")

    for t in INTRO:
        m.para(t, after=80)

    for label, body in BULLETS:
        m.bullet(label, body, after=40)

    m.para(SYSTEM, after=80)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=60)

    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("DRIFTS- OG GOVERNANCE-METODER — ANVENDT I PRAKSIS",
                   ("Område", "Metoder og værktøjer"), MODELS)

    m.section("UDVALGTE RESULTATER")
    for label, body in ACHIEVEMENTS:
        m.bullet(label, body, after=30)

    m.section("ERHVERVSERFARING")
    for title, meta, scope, bullets in EXPERIENCE:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=30)

    m.section("UDDANNELSE")
    for t, meta in EDUCATION:
        m.edu(t, meta)

    m.section("AUTORISATIONER & CERTIFICERINGER")
    for _i, (t, meta) in enumerate(CERTS):
        _p_ = m.edu(t, meta)
        if _i < len(CERTS) - 1:
            _p_.paragraph_format.keep_with_next = True

    m.section("SPROG")
    m.para(LANGUAGES, after=80, justify=False)

    m.section("REFERENCER")
    m.para(REFERENCES, after=80, justify=False)

    m.section("KERNEKOMPETENCER & NØGLEORD")
    m.para(KEYWORDS, after=80)

    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER DRIFTEN I RYTMEN",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    # ingen afsnit eller tabelrække må knække over en sideskift
    for _p in m.doc.paragraphs:
        _p.paragraph_format.keep_together = True
    for _tbl in m.doc.tables:
        for _row in _tbl.rows:
            for _c in _row.cells:
                for _p in _c.paragraphs:
                    _p.paragraph_format.keep_together = True

    from docx.oxml.ns import qn as _qn
    from docx.oxml import OxmlElement as _OE
    for _tbl in m.doc.tables:
        for _tr in _tbl._tbl.findall(_qn("w:tr")):
            _trPr = _tr.find(_qn("w:trPr"))
            if _trPr is None:
                _trPr = _OE("w:trPr")
                _tr.insert(0, _trPr)
            if _trPr.find(_qn("w:cantSplit")) is None:
                _trPr.insert(0, _OE("w:cantSplit"))

    return m.save(path,
                  title="Ansøgning og CV — Run Operations Lead, Nykredit",
                  subject="Run operations · PLC-processen · Power Platform · Citizen Development · "
                          "governance og standarder",
                  keywords=("run operations lead, drift, forvaltning, koordinering, plc-processen, power "
                            "platform, miljøer, adgange, kontroller, monitorering, citizen development, "
                            "governance, dokumentation, overdragelse, dansk, engelsk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1 (krav → løsning), CV side 2-4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_Nykredit_RunOperationsLead.docx")
    print("OK", build(out))
