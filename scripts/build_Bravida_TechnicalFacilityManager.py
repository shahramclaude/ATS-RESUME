# -*- coding: utf-8 -*-
"""
Bravida Danmark — Technical Facility Manager (kunde-site, København), Brøndby.
Bygget i designet fra master-CV'erne. Sprog: dansk (JD-sprog).
Ansøgning + CV i ét dokument.

Opslaget beder om CV + "en kort beskrivelse af, hvorfor netop denne rolle
motiverer dig" — derfor er brevet bevidst kortere end standarden, og CV'et
bærer dokumentationen. Kontaktperson er navngivet: Jonas Barnkob Nielsen.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Technical Facility Manager · Drift af komplekse tekniske installationer"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Søborg")

DATE = "30. oktober 2026"
RECIPIENT = ("Bravida Danmark · Teknisk Facility Management, Brøndby · Att.: Jonas Barnkob Nielsen")
SUBJECT = "Ansøgning: Technical Facility Manager — drift og vedligehold hos kunden i København"

# ------------------------------------------------------------------ side 1
INTRO = ("I jeres opslag er der to ting, der skal lykkes på samme tid: at en bygning med komplekse "
         "installationer bare kører — og at kunden oplever, at den kører, fordi nogen følger op. Jeg har stået på "
         "begge sider af den ligning: som drifts- og vedligeholdelseschef på et 24/7-anlæg med pumper, "
         "ventilation, koblingsanlæg, højspænding og SCADA, og som indehaver af en autoriseret el-virksomhed, "
         "hvor kunden var den, der ringede. Derfor ved jeg, hvad der skal til for at være den, der bliver ringet "
         "til — og hvad der skal til for ikke at blive det.")

MOTIVATION = [
    ("Hvorfor netop denne rolle",
     "Fordi jeg er træt af at være mange steder i kort tid. Jeg vil have én bygning, kende dens installationer "
     "bedre end nogen anden, følge den gennem årstiderne og se, at de ting jeg satte i gang for et år siden, "
     "stadig virker. Og fordi en teknisk kompleks bygning er et system: når ventilationen driller, er årsagen "
     "ofte styringen eller strømmen — ikke ventilationsanlægget. Den sammenhæng er min faglige baggrund."),

    ("Drift og vedligehold, dokumenteret",
     "24/7 kritisk drift med nul tolerance for uplanlagte stop: forebyggende vedligeholdelsesplan, 5S, "
     "A3-root-cause og reservedelsflow. Ansvarlig for drift og vedligehold af tekniske installationer i egen "
     "virksomhed med 40+ serviceanlæg."),

    ("Kunden, kontrakten og økonomien",
     "Fuldt P&L-ansvar med budget, tilbud, serviceaftaler og leverandøraftaler; kundedialog og "
     "forventningsafstemning i hverdagen — både som leverandør og som den, der har købt ydelsen."),

    ("Teknisk sparring, med autorisation i ryggen",
     "Autoriseret el-installatør (LV/MV/HV) og B.Tech i Technology Management & Mechanical Engineering. Kan "
     "læse tavler, koblingsanlæg, ventilation, CTS og dokumentation — og tale med håndværkerne på deres sprog."),

    ("Vagtordning og sikkerhedsgodkendelse",
     "Jeg har haft 24/7-ansvar i fem år og været den, der blev ringet op om natten — det er en vane, ikke en "
     "byrde. Jeg kan sikkerhedsgodkendes og indgår gerne i vagtordningen med én uge hver femte."),

    ("Ét Bravida, ikke én mand alene",
     "Størstedelen af de opgaver, jeg løser, løses i samspil med andre fag. Derfor er et stærkt tværfagligt "
     "netværk i Brøndby ikke et plus men en forudsætning — og jeg bruger det hellere end at gætte."),

    ("Koordinering af mennesker",
     "Daglig ledelse af 5 elektrikere og 3 lærlinge og tværfaglig ledelse af 25 specialister på 37 samtidige "
     "projekter; arbejdsmiljø, LOTO, arbejdstilladelser og entreprenørkontrol i drift."),
]

MIRROR = ("Mod jeres ønsker: teknisk baggrund som autoriseret el-installatør med B.Tech i Technology Management "
          "& Mechanical Engineering · erfaring med drift og vedligehold af komplekse installationer og med "
          "kundedialog, budget- og kontraktmøder · arbejder selvstændigt og struktureret · dansk på "
          "modersmålsniveau og engelsk professionelt · kan sikkerhedsgodkendes · indgår gerne i vagtordningen "
          "(én uge hver femte).")

CLOSE = ("CV'et ligger ved. Jeg kommer gerne ud og ser bygningen, før vi taler om den — og kan tage fat med "
         "kort varsel, så snart sikkerhedsgodkendelsen er på plads.")

# ------------------------------------------------------------------ CV
PROFILE = ("Teknisk driftsleder med mere end 20 års erfaring fra komplekse tekniske installationer, 24/7-drift og "
           "reguleret produktion — og med ledelsesansvar siden 2003 med fuldt P&L-ansvar. Har haft ansvaret for "
           "drift og vedligehold af pumper, ventilation, koblingsanlæg, højspænding og SCADA på et 24/7-anlæg, og "
           "driver i dag egen autoriseret el-virksomhed med 40+ serviceanlæg, hvor kundedialog, kontrakt og "
           "økonomi er en daglig del af arbejdet. Autoriseret el-installatør (LV/MV/HV), B.Tech i Technology "
           "Management & Mechanical Engineering, og bygger selv de data- og AI-værktøjer, der gør drift, "
           "afvigelser og økonomi synlige. Dansk på modersmålsniveau, engelsk professionelt.")

PRACTICE = [
    ("Drift og vedligehold af komplekse installationer",
     "24/7-anlæg med pumper, HVAC, koblingsanlæg, højspænding, motorer og SCADA: forebyggende "
     "vedligeholdelsesplan, lovpligtige eftersyn, A3-root-cause-analyse, reservedelsflow og kritiske lagre. "
     "Fejl findes systematisk, mens driften kører."),

    ("Kundedialog og forventningsafstemning",
     "40+ serviceanlæg i Storkøbenhavn: aftaler, opfølgning, ændringer i brug og behov, og den svære samtale, "
     "når en opgave koster mere, end kunden havde forestillet sig. Jeg har også siddet på kundens side af "
     "bordet og ved, hvad der skaber tillid."),

    ("Kontrakt, økonomi og rapportering",
     "Fuldt P&L-ansvar: budgetopfølgning, prognose, serviceaftaler (SLA), tilbud, leverandør- og "
     "underleverandøraftaler. Afvigelser meldes ud, samme uge som de opstår — ikke ved årsafslutningen."),

    ("Teknisk sparring og dokumentation",
     "Tavler og koblingsanlæg, el-dokumentation og kredsskemaer, CTS/BMS-grænseflader, myndighedsgodkendelser "
     "og FDV. Dokumentationen skal kunne læses af den, der skal fejlfinde om fem år — også når det ikke er mig."),

    ("Sikkerhed, arbejdsmiljø og koordinering",
     "APV og risikovurdering, LOTO og sikringsprocedurer, arbejdstilladelser og entreprenørkontrol på aktive "
     "anlæg; koordinering af håndværkere, brugere og kolleger på tværs af fag — og stop-ret, når sikkerheden "
     "er i spil."),

    ("Data og AI i driften",
     "SAP ERP og CMMS som kilde til sandheden, Power BI til KPI'er på responstid, tilgængelighed og økonomi, "
     "og Python/Claude til automatiseret rapportering og tjeklister — dokumenteret produktivitetsløft over "
     "40 % i planlægning og rapportering."),
]

FIRST90 = [
    ("Dag 1–30",
     "Går bygningen igennem fra teknikrum til tag: tavler, koblingsanlæg, ventilation, varme, CTS, "
     "brand-anlæg og de installationer, der giver flest driftsforstyrrelser. Læser serviceaftalen og de sidste "
     "12 måneders driftsjournaler, møder brugerne og overtager vagtordningen."),
    ("Dag 31–60",
     "Vedligeholdsplan og årshjul på plads med lovpligtige eftersyn og serviceintervaller; KPI'er for "
     "responstid, tilgængelighed og kundetilfredshed aftalt med kunden. Håndværkere og leverandører "
     "koordineret på faste aftaler i stedet for på tilfældige telefonopkald."),
    ("Dag 61–90",
     "Kontraktgennemgang med kunden: hvad dækker aftalen, hvad koster ændringer, og hvor er der behov for "
     "investeringer. Dokumentationsmappe (FDV) ajourført, og de første 2–3 optimeringer gennemført med målt "
     "effekt på energi eller driftsomkostninger."),
    ("Måned 6–12",
     "Stabile KPI'er og en kunde, der sjældent har grund til at ringe. Forslag til kunden om "
     "energioptimeringer og investeringer med tilbagebetalingstid — og et driftsbudget, der holder, fordi "
     "vedligeholdelsen er planlagt og ikke akut."),
]

MODELS = [
    ("Tekniske installationer",
     "El-forsyning, tavler og koblingsanlæg, højspænding og nødstrøm, ventilation og klima, varme og køl, "
     "vand og afløb, brand-anlæg og ABA, CTS/BMS og SCADA, elevator- og adgangsgrænseflader"),
    ("Drift & vedligehold",
     "Forebyggende vedligeholdelsesplan og årshjul, lovpligtige eftersyn, tilstandsbaseret vedligehold, "
     "reservedelsstyring, A3-root-cause og 5S, driftsjournaler og afvigelsesopfølgning, FDV-dokumentation"),
    ("Kunde & kontrakt",
     "Serviceaftaler og SLA, ændringshåndtering og merarbejde, kundemøder og forventningsafstemning, "
     "KPI-rapportering, kundetilfredshedsopfølgning, kontraktforhandling"),
    ("Økonomi & styring",
     "Budget og budgetopfølgning, prognose og cost-to-complete, tilbudsberegning, indkøb og "
     "leverandøraftaler, P&L-ansvar, fakturering og afstemning"),
    ("Sikkerhed & arbejdsmiljø",
     "APV og risikovurdering, LOTO og sikringsprocedurer, arbejdstilladelser, entreprenørkontrol på aktive "
     "anlæg, near-miss-opfølgning, stop-ret, myndighedskrav og sikkerhedsgodkendelse"),
    ("El-fagligt ansvar",
     "Autorisation og egenkontrol, kredsskemaer og el-dokumentation, DS/HD 60364 og EN 61439, måling og "
     "test (isolation, kontinuitet, RCD), spændingssætning og afleveringsforretning"),
    ("Energi & bæredygtighed",
     "Energikortlægning og optimering, driftsoptimering af ventilation, varme og køl, måling og "
     "verifikation, investeringscases med tilbagebetalingstid (NPV, IRR), bæredygtighedskrav i drift"),
    ("Data & værktøjer",
     "SAP ERP og CMMS, Power BI til KPI og økonomi, Excel og Power Query, Python og Claude API til "
     "automatiseret rapportering, tjeklister og dokumentation"),
]

ACHIEVEMENTS = [
    ("24/7-drift uden uplanlagte stop",
     "pumper, HVAC, koblingsanlæg, højspænding og SCADA — oppetid gennem forebyggende vedligehold og hurtig "
     "fejlfinding."),
    ("Autoriseret virksomhed bygget fra bunden",
     "med egenkontrol, dokumentationssystem og 40+ serviceanlæg — fuldt P&L- og kundeansvar."),
    ("−40 % energikost",
     "i reguleret produktion via struktureret PDCA, A3 og standardiserede løsninger; målt og fastholdt "
     "efter projektets afslutning."),
    ("Nul kritiske afvigelser ved aflevering",
     "på 37 samtidige anlægsprojekter (2–10 mio. kr.) — dokumentation og aflevering uden fund."),
    ("+40 % produktivitet",
     "i egen virksomhed gennem dataunderstøttet planlægning, standardarbejde og egen AI-tooling."),
]

EXPERIENCE = [
    ("Indehaver / Teknisk direktør / Autoriseret el-installatør",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg i Storkøbenhavn · fuldt P&L, serviceaftaler og "
     "leverandøraftaler",
     [("Drift og levering til kunderne",
       "daglig planlægning, kapacitet mod ordrebogen, materiale- og reservedelsflow, kvalitetskontrol, "
       "responstider og omkostning — gennemgået hver morgen mod standardarbejde, 5S og KPI'er."),
      ("Kontrakt, kunde og økonomi",
       "serviceaftaler, tilbud, ændringshåndtering og leverandøraftaler; forventningsafstemning direkte med "
       "kunderne og fuldt ansvar for bundlinjen."),
      ("Teknisk bredde",
       "el-installationer, tavler og styring, ventilation og klima samt fejlfinding på tværs af fag; "
       "risikovurdering, LOTO og dokumenterede serviceregistreringer."),
      ("Digitalt fundament, bygget selv",
       "ERP-baseret ordre- og reservedelsstyring, Power BI-dashboards og Python/Claude-værktøjer til "
       "planlægning, tilbud, tjeklister og rapportering; produktivitetsløft over 40 %.")]) ,

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · drifts- og "
     "vedligeholdelsesbudgetter i SAP",
     [("24/7 kritisk drift",
       "oppetid, forebyggende vedligehold og hurtig fejlfinding med nul tolerance for uplanlagte stop; "
       "koordinering af egne teknikere, entreprenører og leverandører."),
      ("Struktureret vedligehold",
       "standardarbejde, 5S, PDCA-baseret vedligeholdsplan, A3-root-cause-analyse, reservedelsflow og "
       "kritiske lagre."),
      ("Sikkerhed og miljø",
       "LOTO, risikovurdering, arbejdstilladelser, near-miss-rapportering og værktøjsmøder; KPI'er og "
       "driftsbudgetter i SAP ERP.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister inden for teknik, indkøb og drift · "
     "GMP/FDA/EMA",
     [("Porteføljeleverance",
       "tidsplan, økonomi, risiko, ressourcer og månedlig rapportering til ledelse og kunde på tværs af "
       "teknik, indkøb og driftsorganisation."),
      ("Idriftsættelse og aflevering",
       "FAT/SAT, IQ/OQ/PQ og valideringsdokumentation med afvigelseshåndtering, CAPA og change control — nul "
       "kritiske fund ved aflevering."),
      ("Anlæg i drift",
       "arbejde i renrum, lager og produktion: arbejdstilladelser, LOTO, entreprenørkontrol og grænseflader "
       "til Kvalitet, Vedligehold og Produktion."),
      ("Energiprogram",
       "−40 % energikost gennem struktureret PDCA, A3 og standardiseret arbejde; SAP ERP til omkostning, "
       "anlæg og ordrestyring.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.) · specifikation til "
     "formel aflevering",
     [("Levering og flow",
       "kapacitetsplanlægning og flowstyring over 11 samtidige projekter, fra specifikation til formel "
       "aflevering."),
      ("Daglige tavlemøder og flaskehalsanalyse",
       "standardiseret arbejde ved hver station med mærkbar fremgang i leveringsperformance og "
       "førstegangskvalitet."),
      ("Leverandører og underleverandører",
       "kontraktgrundlag, sikkerhedsdokumentation og afleveringspakker.")]),

    ("Elektromekaniker / Produktionsteamleder",
     "ARJ Engineering · Teheran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · skiftplanlægning, materialestyring og lager",
     [("Produktionsteam",
       "skiftplanlægning, materialestyring, lager og linjesideforsyning, målopfølgning og situationel "
       "coaching."),
      ("Teknisk problemløsning",
       "reparation og diagnosticering af elektriske og mekaniske systemer gennem struktureret "
       "root cause-analyse.")]),
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
    ("Autoriseret el-installatør (LV/MV/HV)",
     "Sikkerhedsstyrelsen · maj 2023"),
    ("Køle- og HVAC-teknik (AMU)",
     "Mercantec · mar. 2021"),
    ("Lean — værdistrømsanalyse, standardarbejde, 5S, A3 og Kaizen",
     "Anvendt i drift · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og projekter · 2017 – nu"),
    ("Arbejdsmiljø §16 og sikkerhedsbevidsthed (VI/6-1)",
     "Søfartsstyrelsen · maj 2021"),
    ("STCW — maskinrumsvagt (A-III/1), skibssikkerhedsofficer (VI/5)",
     "Søfartsstyrelsen · 2021 – 2023"),
]

LANGUAGES = "Dansk (modersmål) · Engelsk (professionelt, skriftligt og mundtligt) · Persisk/farsi · Kørekort B"

REFERENCES = "Tidligere ledere hos Biofos (Lynetten) og Novo Nordisk A/S (Kalundborg) — oplyses ved henvendelse."

KEYWORDS = (
    "Technical Facility Manager · Technical Facility Management · TFM · Driftsansvarlig · Drift og vedligehold · "
    "Bygningsdrift · Tekniske installationer · Bygningstekniske installationer · Kompleks bygning · "
    "El-installationer · VVS · Ventilation · HVAC · Klima · Køl · Varme · CTS · BMS · SCADA · Tavler · "
    "Koblingsanlæg · Højspænding · Lavspænding · Nødstrøm · Brand · ABA · Sprinkler · Elevatorer · Tekniske "
    "eftersyn · Lovpligtige eftersyn · Vedligeholdsplan · Årshjul · Serviceaftale · SLA · Kontraktstyring · "
    "Økonomistyring · Budget · Budgetopfølgning · KPI · Responstid · Tilgængelighed · Kundetilfredshed · "
    "Kundedialog · Kunderådgivning · Forventningsafstemning · Interessenter · Håndværkere · Underleverandører · "
    "Leverandørstyring · Koordinering · Samarbejde · Selvstændig · Struktureret · Serviceorienteret · "
    "Vagtordning · Sikkerhedsgodkendelse · Maskinmester · Installatør · El-installatør · Autorisation · APV · "
    "Arbejdsmiljø · LOTO · Sikkerhed · Energioptimering · Bæredygtighed · Klimaneutral · Dokumentation · FDV · "
    "SAP · ERP · Power BI · Excel · AI · Claude · Python · Dansk · Engelsk"
)


def build(path):
    m = MasterDoc(TEMPLATE, lang="da-DK")

    # ---------------------------------------------------------------- side 1
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta(RECIPIENT)

    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, SUBJECT, bold=True, color="1A1A1A")

    m.para(INTRO, after=80)

    for label, body in MOTIVATION:
        m.bullet(label, body, after=40)

    m.para(MIRROR, after=80)
    m.para(CLOSE, after=80)

    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "FAGLIG PROFIL")
    m.para(PROFILE, after=80)

    m.section("DRIFT, KUNDE OG ØKONOMI — BEVIS, IKKE PÅSTANDE")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("TEKNISKE OMRÅDER & VÆRKTØJER — ANVENDT I PRAKSIS",
                   ("Område", "Installationer og værktøjer"), MODELS)

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
    for t, meta in CERTS:
        m.edu(t, meta)

    m.section("SPROG")
    m.para(LANGUAGES, after=80, justify=False)

    m.section("REFERENCER")
    m.para(REFERENCES, after=80, justify=False)

    m.section("KERNEKOMPETENCER & NØGLEORD")
    m.para(KEYWORDS, after=80)

    m.models_table("FØRSTE 90 DAGE — SÅDAN TAGER JEG OVER",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    return m.save(path,
                  title="Ansøgning og CV — Technical Facility Manager, Bravida Danmark",
                  subject="Technical Facility Management · drift og vedligehold · kunde og kontrakt · "
                          "autoriseret el-installatør LV/MV/HV",
                  keywords=("technical facility manager, technical facility management, drift og vedligehold, "
                            "bygningsdrift, tekniske installationer, kunde, kontrakt, sla, økonomi, kpi, "
                            "el-installatør, autorisation, cts, ventilation, dansk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1 (kort, som opslaget beder om), CV side 2-4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_Bravida_TechnicalFacilityManager.docx")
    print("OK", build(out))
