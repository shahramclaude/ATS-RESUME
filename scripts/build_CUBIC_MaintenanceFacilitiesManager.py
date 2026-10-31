# -*- coding: utf-8 -*-
"""
Rockwell Automation / CUBIC-Modulsystem A/S — Maintenance & Facilities Manager.
Aabybro (primært onsite) + Brønderslev. Dansk JD.
Bygget i designet fra master-CV'erne. Sprog: dansk.

Vinkel: kernen i opslaget er transformationen fra reaktiv til proaktiv,
planlagt og datadrevet vedligehold — og Fiix som løftestang. Det er præcis
det arbejde, han har gjort på 24/7-anlæg, og hans el-autorisation passer
direkte til en virksomhed, der bygger lavspændingstavler.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Maintenance & Facilities Manager | CUBIC · Rockwell Automation | Aabybro & Brønderslev"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv")

DATE = "30. oktober 2026"
RECIPIENT = ("CUBIC-Modulsystem A/S · en del af Rockwell Automation · Aabybro & Brønderslev · "
             "Att.: Plant Manager, CUBIC")
SUBJECT = "Ansøgning: Maintenance & Facilities Manager — CUBIC, Aabybro og Brønderslev"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Vedligehold bliver ikke proaktivt af sig selv. Det bliver det, når nogen beslutter, at en arbejdsordre kun "
    "er lukket, når årsagen er fundet — og når systemet er så nemt at bruge, at teknikeren hellere registrerer "
    "arbejdet end at gå videre til næste opgave. Det er den transformation, I beskriver som det centrale mål for "
    "stillingen, og det er den, jeg har gennemført på et 24/7-anlæg og i en egen virksomhed med 40+ "
    "serviceanlæg.",

    "Jeg er uddannet el-installatør med B.Tech i Technology Management & Mechanical Engineering, og jeg har i "
    "tyve år haft ansvaret for drift og vedligehold af tekniske installationer, hvor uplanlagte stop var det, der "
    "kostede. At det netop er CUBIC — der bygger modulopbyggede lavspændingstavler til datacentre, energi og "
    "infrastruktur — gør rollen fagligt nær: det er den type udstyr, jeg har fejlsøgt, målt på og dokumenteret "
    "hele mit arbejdsliv.",
]

BULLETS = [
    ("Fra reaktiv til proaktiv — gjort, ikke proklameret",
     "PDCA-baseret vedligeholdsplan med fast årshjul, kritiske reservedele på lager og A3-root-cause på hver "
     "større nedetid. På 24/7-anlæg med pumper, HVAC, koblingsanlæg, højspænding og SCADA var målet nul "
     "uplanlagte stop — og det holdt, fordi vedligeholdelsen var planlagt, ikke akut."),

    ("Systemet i hænderne på teknikerne",
     "Jeg har selv bygget det digitale fundament: ERP-baseret ordre- og reservedelsstyring, CMMS som kilde til "
     "sandheden, Power BI-dashboards og Python/Claude-værktøjer til automatiseret rapportering og tjeklister. "
     "Gevinsten var målbar — over 40 % produktivitetsløft — fordi data blev indsamlet i arbejdet, ikke bagefter."),

    ("El-faglig tyngde i en tavleproducent",
     "Elautoriseret maskinmester (LV/MV/HV) med egen autoriseret virksomhed og egenkontrol. Jeg kan vurdere "
     "tavler, koblingsanlæg, beskyttelse og selektivitet — og sikre, at anlæggene på begge sites lever op til "
     "myndigheds- og sikkerhedskravene, uden at det skal udliciteres."),

    ("To sites, entreprenører og økonomi",
     "Fuldt P&L-ansvar med budget, tilbud og leverandøraftaler; serviceaftaler og SLA'er, underleverandører styret "
     "på kontrakt, sikkerhedsdokumentation og fremdrift. KPI'er på responstid, oppetid og økonomi fulgt op "
     "månedligt — ikke opdaget ved årsafslutningen."),

    ("Tekniske projekter, faciliteter og energi",
     "37 samtidige anlægsprojekter (2–10 mio. kr.) med investeringsgrundlag, tidsplan og aflevering — og −40 % "
     "energikost i reguleret produktion via struktureret PDCA og standardiserede løsninger, målt og fastholdt "
     "efter projektets afslutning."),
]

MIRROR = ("Mod jeres krav: ingeniørfaglig baggrund (B.Tech, EQF 6) og elautoriseret maskinmester · mere end 8 års "
          "erfaring med vedligehold, teknisk drift og produktion · erfaring med ledelse af tekniske medarbejdere og "
          "lærlinge · indgående kendskab til produktionsudstyr og tekniske installationer · forebyggende "
          "vedligehold og vedligeholdelsesstyringssystemer (CMMS/ERP) · struktureret, datadrevet og "
          "forbedringsorienteret tilgang · hands-on og med stærk samarbejdsevne · gode engelskkundskaber, "
          "skriftligt og mundtligt.")

HONEST = ("To ting, lige ud. Jeg bor i Måløv, og stillingen er primært onsite i Aabybro — det er ikke en "
          "pendlerafstand, og jeg søger derfor med en klar forventning om at flytte til Nordjylland, ikke med en "
          "plan om at køre frem og tilbage. Og jeg har ikke arbejdet i Fiix specifikt; jeg har implementeret og "
          "drevet CMMS- og ERP-baserede vedligeholdelsesflows fra bunden, og Fiix er det system, jeg ville lære "
          "først og hurtigst — fordi hele transformationen afhænger af, at det bliver brugt.")

CULTURE = ("Hvorfor CUBIC og Rockwell. CUBIC har bygget modulopbyggede tavler siden 1973 og er i dag en del af "
           "Rockwells Power Control Business — et sted, hvor korte beslutningsveje og høj tillid til teknisk "
           "ekspertise er en del af stillingsbeskrivelsen, og hvor kvalitet og sikkerhed er langsigtede "
           "beslutninger snarere end kampagner. Rockwells værdier — integritet, kundefokus, innovation og \"One "
           "Rockwell\" — er ikke fremmede for en, der er vant til at skulle kunne stå ved sin beslutning, når "
           "anlægget kører klokken tre om natten.")

PRACTICAL = ("Praktisk: kort opsigelse og klar til at starte hurtigt; dansk på modersmålsniveau og engelsk "
             "professionelt; kørekort B og mobil mellem de to sites. Ved ansættelse afvikler jeg min egen "
             "virksomhed, så der er ingen konkurrerende forpligtelser.")

CLOSING = ("Jeg vil gerne se de to sites og den nuværende vedligeholdelsesorganisation, før vi taler om planer — "
           "og jeg kommer gerne med den første skitse til, hvordan Fiix kan tages i brug, så det bliver teknikerne "
           "og ikke systemet, der sætter dagsordenen.")

# ------------------------------------------------------------------ CV
PROFILE = ("Vedligeholds- og driftsleder med mere end 20 års erfaring fra tekniske installationer, 24/7-drift og "
           "reguleret produktion — med ledelsesansvar siden 2003 og fuldt P&L-ansvar. Har ansvaret for drift og "
           "vedligehold af pumper, HVAC, koblingsanlæg, højspænding og SCADA på et 24/7-anlæg og har bygget "
           "vedligeholdelsen om fra reaktiv til planlagt og forebyggende med fast årshjul, kritiske reservedele og "
           "A3-root-cause. Elautoriseret maskinmester (LV/MV/HV) med egen autoriseret virksomhed og egenkontrol; "
           "B.Tech i Technology Management & Mechanical Engineering. Bygger selv de data- og AI-værktøjer, der gør "
           "oppetid, nedetid og økonomi synlige — CMMS/ERP, Power BI, Python, Claude. Dansk på modersmålsniveau, "
           "engelsk professionelt.")

PRACTICE = [
    ("Vedligeholdelsesstrategi og transformation",
     "Fra reaktiv til forebyggende, planlagt og datadrevet: kritikalitetsvurdering af udstyr, fast årshjul for "
     "lovpligtige eftersyn og serviceintervaller, tilstandsbaseret vedligehold hvor det giver mening, og "
     "A3-root-cause på hver større nedetid. Målt på MTBF, responstid og uplanlagt nedetid."),

    ("Vedligeholdelsessystem og data",
     "CMMS og ERP som kilde til sandheden: arbejdsordrer, anlægsdata og historik, reservedelslager og "
     "kritiske komponenter, tjeklister og rapportering. Power BI og Python/Claude til dashboards og "
     "automatiseret rapportering — så data bliver indsamlet i arbejdet, ikke bagefter."),

    ("Ledelse af tekniske medarbejdere",
     "Daglig ledelse af 5 elektrikere og 3 lærlinge samt tværfaglig ledelse af 25 specialister; kompetencematrix, "
     "1:1-samtaler, 30-60-90-onboarding, sikker adfærd og en kultur, hvor man melder fejl, før de bliver til stop."),

    ("Bygninger, faciliteter og entreprenører",
     "Ansvar for tekniske installationer og faciliteter i drift: el, ventilation, varme og køl, vand, trykluft, "
     "brand-anlæg og CTS; entreprenører og servicepartnere koordineret på kontrakt, sikkerhedsdokumentation og "
     "fremdrift, med arbejdstilladelser og LOTO på aktive anlæg."),

    ("Budget, KPI og investeringer",
     "Vedligeholds- og facilitybudgetter med prognose og opfølgning; KPI'er på oppetid, responstid og økonomi; "
     "investeringscases med tilbagebetalingstid (NPV, IRR) og beslutningsgrundlag for udskiftning kontra "
     "reparation."),

    ("Sikkerhed, myndighed og energi",
     "APV, risikovurdering og sikkerhedsgodkendelse; myndighedskrav og lovpligtige eftersyn; ISO 9001-baseret "
     "kvalitetsstyring; energioptimering med målt effekt — −40 % energikost i reguleret produktion, fastholdt "
     "efter projektets afslutning."),
]

FIRST90 = [
    ("Dag 1–30",
     "Går begge sites igennem fra teknikrum til tag og lærer udstyret at kende, mens det kører: kritiske anlæg, "
     "kendte svagheder, reservedelslager og de sidste 12 måneders nedetid. Taler med teknikerne om, hvorfor "
     "arbejdsordrer i dag bliver lukket på papir og ikke i systemet."),
    ("Dag 31–60",
     "Fiix sat op omkring det, der faktisk skal styres: anlægsregister med kritikalitet, PM-planer pr. udstyr, "
     "arbejdsordrer der kan bruges på telefonen, og reservedele knyttet til anlæggene. KPI-baseline lagt fast, "
     "så forbedringen kan måles og ikke bare mærkes."),
    ("Dag 61–90",
     "Vedligeholdelsesorganisationen arbejder efter plan, ikke efter larm: ugentlig planlægning, fast "
     "tilbageblik på nedetid og to-tre forbedringer gennemført med målt effekt på oppetid eller "
     "vedligeholdsomkostning. Budget og leverandøraftaler gennemgået med Produktion og EHS."),
    ("Måned 6–12",
     "En vedligeholdelseskultur, hvor forebyggelse er normen, Fiix er det sted, hvor historikken bor, og "
     "teknikerne selv foreslår forbedringer. Målbare fremskridt på uplanlagt nedetid, MTBF og energiforbrug — "
     "og en organisation, der kan holde niveauet uden mig i hverdagen."),
]

MODELS = [
    ("Vedligehold & pålidelighed",
     "Forebyggende og planlagt vedligehold, tilstandsbaseret vedligehold, kritikalitetsanalyse, MTBF/MTTR, "
     "RCM-tankegang, TPM, A3-root-cause, fem-hvorfor, FMEA, reservedelskritikalitet"),
    ("Systemer & data",
     "CMMS (Fiix-principper: anlægsregister, PM-planer, arbejdsordrer, historik, reservedele), SAP ERP, Power "
     "BI, Excel/Power Query, Python og Claude API til automatiseret rapportering og tjeklister"),
    ("Tekniske installationer",
     "El-forsyning, tavler og koblingsanlæg, LV/MV/HV, nødstrøm, ventilation og klima, varme og køl, vand og "
     "afløb, trykluft, brand-anlæg, CTS/BMS og SCADA, elevator- og adgangsgrænseflader"),
    ("Facilities & bygninger",
     "Bygningsdrift og vedligehold, lovpligtige eftersyn, arbejdsmiljø og APV, entreprenørkontrol på aktive "
     "anlæg, arbejdstilladelser og LOTO, areal- og kapacitetstilpasning ved ændringer i produktionen"),
    ("Økonomi & styring",
     "Vedligeholds- og facilitybudget, prognose og cost-to-complete, indkøb og leverandøraftaler, "
     "serviceaftaler og SLA, investeringscases (NPV, IRR, tilbagebetalingstid), KPI-rapportering"),
    ("Energi & bæredygtighed",
     "Energikortlægning, optimering af ventilation, varme, køl og trykluft, måling og verifikation, "
     "energiledelse (ISO 50001-principper), dokumenterede besparelser"),
    ("Kvalitet & compliance",
     "ISO 9001-baseret kvalitetsstyring, myndighedskrav og dokumentation, sporbare service- og "
     "eftersynsregistreringer, leverandørdokumentation, sikkerhedsgodkendelse"),
    ("Ledelse & forbedring",
     "Situationsbestemt ledelse, coaching og 1:1, kompetencematrix og udviklingsplaner, tavlemøder og "
     "daglig styring, PDCA, Kaizen og standardarbejde, forandringsledelse ved nyt system"),
]

ACHIEVEMENTS = [
    ("24/7-drift uden uplanlagte stop",
     "pumper, HVAC, koblingsanlæg, højspænding og SCADA — oppetid gennem forebyggende vedligehold og hurtig "
     "fejlfinding."),
    ("−40 % energikost",
     "i reguleret produktion via struktureret PDCA, A3 og standardiserede løsninger; målt og fastholdt efter "
     "projektets afslutning."),
    ("+40 % produktivitet",
     "i egen virksomhed gennem datadrevet planlægning, standardarbejde og egen AI-tooling."),
    ("Nul kritiske afvigelser ved aflevering",
     "på 37 samtidige anlægsprojekter (2–10 mio. kr.) — dokumentation og aflevering uden fund."),
    ("Autoriseret virksomhed bygget fra bunden",
     "med egenkontrol, dokumentationssystem, 5 elektrikere og 3 lærlinge — fuldt P&L- og kundeansvar."),
]

EXPERIENCE = [
    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg i Storkøbenhavn · fuldt P&L, serviceaftaler og "
     "leverandøraftaler",
     [("Drift og vedligehold",
       "planlagt vedligehold og fejlfinding på el-installationer, tavler, styring, ventilation og klima; "
       "reservedelsflow og dokumenterede serviceregistreringer."),
      ("Kontrakt, kunde og økonomi",
       "serviceaftaler, tilbud, ændringshåndtering og leverandøraftaler; fuldt ansvar for bundlinjen og for "
       "responstiderne."),
      ("Teknisk dokumentation og compliance",
       "egenkontrol, kredsskemaer og el-dokumentation, risikovurdering og LOTO; nul kritiske afvigelser i "
       "porteføljen."),
      ("Digitalt fundament, bygget selv",
       "ERP-baseret ordre- og reservedelsstyring, Power BI-dashboards og Python/Claude-værktøjer til "
       "planlægning, tjeklister og rapportering; produktivitetsløft over 40 %.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · drifts- og "
     "vedligeholdelsesbudgetter i SAP",
     [("Vedligeholdelse fra reaktiv til planlagt",
       "PDCA-baseret vedligeholdsplan med fast årshjul, kritikalitetsvurdering, A3-root-cause på større "
       "nedetid og reservedelsflow med kritiske lagre."),
      ("24/7 kritisk drift",
       "oppetid, forebyggende vedligehold og hurtig fejlfinding med nul tolerance for uplanlagte stop; "
       "koordinering af egne teknikere, entreprenører og leverandører."),
      ("Sikkerhed og myndighed",
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
       "førstegangskvalitet.")]),

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
    ("Elautoriseret maskinmester (LV/MV/HV)",
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
    "Maintenance & Facilities Manager · Vedligehold · Vedligeholdelseschef · Vedligeholdelsesorganisation · "
    "Vedligeholdelsesstrategi · Reaktiv · Proaktiv · Forebyggende vedligehold · Planlagt vedligehold · "
    "Tilstandsbaseret vedligehold · Datadrevet vedligehold · CMMS · Fiix · Vedligeholdelsessystem · "
    "Arbejdsordrer · Asset Management · Anlægsdata · Reservedele · Reservedelslager · Oppetid · Tilgængelighed · "
    "MTBF · MTTR · OEE · KPI · Nedetid · Driftsstabilitet · Produktionsudstyr · Tekniske installationer · "
    "Bygninger · Faciliteter · Facility · Eltavler · Lavspændingstavler · Switchgear · Kapslinger · "
    "El-installationer · El-installatør · Autorisation · Højspænding · Lavspænding · VVS · Ventilation · Køl · "
    "Trykluft · Varme · Styring · PLC · SCADA · CTS · BMS · Entreprenører · Serviceleverandører · "
    "Leverandørstyring · Budget · Økonomi · Investeringer · Tekniske projekter · Forbedringsarbejde · Lean · "
    "Fem hvorfor · Root Cause Analysis · A3 · TPM · 5S · Energioptimering · Energieffektivitet · EHS · Sikkerhed · "
    "Arbejdsmiljø · APV · LOTO · Myndighedskrav · Compliance · ISO 9001 · Samarbejde · Interessenter · "
    "Produktion · Engineering · Ledelse · Kompetenceudvikling · Hands-on · Struktureret · Datadrevet · SAP · "
    "ERP · Power BI · Excel · Python · AI · Rockwell Automation · CUBIC · Brønderslev · Aabybro · Dansk · Engelsk"
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

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=80)

    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "FAGLIG PROFIL")
    m.para(PROFILE, after=80)

    m.section("VEDLIGEHOLD, DRIFT OG ØKONOMI — BEVIS, IKKE PÅSTANDE")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("FAGLIGE OMRÅDER & VÆRKTØJER — ANVENDT I PRAKSIS",
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
    for t, meta in CERTS:
        m.edu(t, meta)

    m.section("SPROG")
    m.para(LANGUAGES, after=80, justify=False)

    m.section("REFERENCER")
    m.para(REFERENCES, after=80, justify=False)

    m.section("KERNEKOMPETENCER & NØGLEORD")
    m.para(KEYWORDS, after=80)

    m.models_table("FØRSTE 90 DAGE — FRA REAKTIV TIL PROAKTIV",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    return m.save(path,
                  title="Ansøgning og CV — Maintenance & Facilities Manager, CUBIC (Rockwell Automation)",
                  subject="Vedligehold · proaktiv vedligeholdelseskultur · Fiix · facilities · "
                          "el-autorisation · Aabybro og Brønderslev",
                  keywords=("maintenance & facilities manager, vedligehold, forebyggende vedligehold, cmms, "
                            "fiix, oppetid, kpi, budget, entreprenører, facilities, eltavler, el-installatør, "
                            "energioptimering, dansk, engelsk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1, CV side 2-4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_CUBIC_MaintenanceFacilitiesManager.docx")
    print("OK", build(out))
