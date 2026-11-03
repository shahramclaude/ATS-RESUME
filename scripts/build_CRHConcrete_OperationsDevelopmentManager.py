# -*- coding: utf-8 -*-
"""
CRH Concrete — Operations Development Manager (10 fabrikker, Viby Sjælland).
Dansk (JD-sprog). Ansøgning + CV i ét dokument, masterdesign.

Mission-første ansøgning (side 1): handler om opgaven — performance, CAPEX,
KPI-opfølgning og tværgående forbedringer på tværs af 10 fabrikker — ikke om mig.
CV (sider 2–4) dokumenterer bevis med egne ord.

Stemme: erfaren, analytisk projektleder og driftsleder. Konkret, dokumenteret,
ingen fyldord. Ledelsesværktøjer væves ind i fortællingen.

Ærlighed: JD'en søger relevant uddannelse (produktion, engineering, supply chain,
økonomi, business development) og erfaring med projektledelse, controlling eller
ledelsessupport. Jeg har B.Tech i teknologiledelse og maskinteknik, er
el-ingeniør + elautoriseret maskinmester, har ledet 37 CAPEX-projekter under
GMP/FDA/EMA, fuldt P&L-ansvar i egen virksomhed, og har fungeret som drifts- og
ledelsesstøtte i kompleks produktion. Jeg har ikke specifik betonelements- eller
byggevareerfaring — det siges én gang, uden at foregive andet.

Professionel og aktiv Claude-koder: investeringsmodeller (NPV/IRR, følsomhed,
scenarier), KPI-dashboards, digitale tjeklister, beslutningsgrundlag.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

TEMPLATE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = ("Operations Development Manager | CRH Concrete, produktion på tværs af 10 fabrikker")
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv, Danmark")

DATE = "4. november 2026"
RECIPIENT = ("CRH Concrete A/S · Vestergade 25, 4130 Viby Sjælland · Att: Sebastian, "
             "Operations Director")
SUBJECT = "Ansøgning: Operations Development Manager — produktion på tværs af 10 fabrikker"

# ------------------------------------------------------------------ side 1: ansøgning
OPENING = [
    "CRH Concrete leverer betonelementer og bygge løsninger til over 1.000 byggerier om året, på tværs af 10 "
    "fabrikker fra Varde i vest til Randers i øst. Hver dag skal produktion, kvalitet, sikkerhed og levering "
    "balanceres — og hver beslutning skal kunne omsættes til handling ude på fabrikkerne. Opgaven i denne stilling "
    "er at stå som Operations Directors højre hånd: skabe overblik over performance, drive tværgående "
    "forbedringer og styre CAPEX-processen, så de 10 fabrikker præsterer som én organisation, ikke som ti "
    "enheder der hver især løser det samme problem.",
]

BULLETS = [
    ("Performanceopfølgning, ikke kun rapportering",
     "Jeg bygger ikke KPI-værktøjer, der ender i en skuffe. Jeg udvikler den månedlige Production Performance "
     "Review som et fast beslutningsforum: klare nøgletal, ejerskab på hvert tal, og opfølgning der fører til "
     "handling — ikke bare præsentation. Data skal gøre det nemt for produktionscheferne at se, hvor de skal "
     "gribe ind, og svært at ignorere det de ser."),

    ("CAPEX og investeringsportefølje med styr på gevinsten",
     "Investeringer skal dokumenteres før de godkendes, og gevinsten skal måles bagefter. Jeg driver business "
     "cases, governance, prioritering, budgetopfølgning, risiko og gevinstrealisering — så CAPEX-puljen går til "
     "de projekter der skaber mest værdi, og vi ved om investeringen hjemtog det lovede."),

    ("Tværgående forbedringer på tværs af 10 fabrikker",
     "Standardisering og best practice virker kun, når de er tilpasset den enkelte fabrik. Jeg identificerer "
     "forbedringsinitiativer inden for planlægning, effektivitet, footprint, kvalitet, sikkerhed og "
     "omkostningsreduktion, og leder dem fra analyse til implementering — med produktionscheferne som medejere, "
     "ikke som modtagere af en ordre fra kontoret."),

    ("Uden formelt personaleansvar, men med følgeskab",
     "Rollen har ikke direkte personaleansvar, og det er en styrke: følgeskab skal opbygges på troværdighed, "
     "ikke på titel. Jeg arbejder analytisk og forretningsorienteret, men har samtidig blik for de mennesker og "
     "samarbejdsrelationer der er afgørende for at lykkes med forandringer. Tydelig retning, tillid og frihed "
     "under ansvar — som min nye leder Sebastian beskriver det — er præcis den ledelsesstil jeg trives bedst i."),
]

MIRROR = ("Stillingen søger en analytisk og forretningsorienteret profil med projektledelses-, controlling- eller "
          "ledelsessupporterfaring, stærke data- og KPI-kompetencer og evnen til at skabe følgeskab uden formelt "
          "ledelsesansvar. Jeg matcher: B.Tech (EQF 6) i teknologiledelse og maskinteknik, el-ingeniør og "
          "elautoriseret maskinmester (LV/MV/HV), 20+ år i teknisk drift, projektledelse og personaleledelse, "
          "ledelse af 37 samtidige CAPEX-projekter (DKK 2–10 mio.) under GMP/FDA/EMA, fuldt P&L-ansvar i egen "
          "virksomhed, samt erfaring som drifts- og ledelsesstøtte i kompleks produktion. Én ting er anderledes: "
          "jeg har ikke specifik erfaring fra betonelement- eller byggevarebranchen. Det, jeg har, er dokumenteret "
          "erfaring med at styrke performance og eksekvering i reguleret, industriel produktion — og evnen til "
          "hurtigt at sætte mig ind i et nyt fagligt område.")

HONEST = ("Det ærlige er et udgangspunkt, ikke et kompromis. Jeg er el-ingeniør og elautoriseret maskinmester med "
          "en teknisk ledelsesbaggrund — ikke betonelementspecialist. Jeg kender ikke CRH Concretes fabrikker "
          "fra før, men jeg kender industriel produktion, CAPEX-styring, KPI-opfølgning og tværgående "
          "forbedringsarbejde. For CRH Concrete betyder det en analytisk projektleder, der hurtigt kan opbygge "
          "overblik over de 10 fabrikker, skabe beslutningsgrundlag til ledelsen og drive forbedringer fra analyse "
          "til implementering.")

CULTURE = ("CRH Concrete er en del af CRH i Danmark, en af landets førende leverandører af betonelementer og "
           "bygningsløsninger med ca. 1.500 medarbejdere på 22 lokationer. Virksomheden har en klar bæredygtigheds-"
           "strategi — 50% CO2-reduktion i 2030, genanvendt beton (23% CO2-reduktion, 25% genanvendelsesprocent) og "
           "Low Carbon Concrete-elementer. Den jordnære kultur med tillid, frihed under ansvar og åben dialog passer "
           "til den måde jeg arbejder på: målrettet, følge-op stærkt, og med respekt for den faglighed der allerede "
           "findees ude på fabrikkerne.")

PRACTICAL = ("Bosat i Måløv med kørekort B, klar til at starte snarest. Viby Sjælland og de 10 fabrikker er inden "
             "for rimelig kørselsafstand, og jeg er indstillet på den transport og rejseaktivitet rollen kræver. "
             "Jeg afvikler min egen virksomhed (ELOHVAC ApS), så der er ingen konkurrerende forpligtelser. "
             "Struktureret, mødestabil, pligtopfyldende og fleksibel — som stillingen foreskriver.")

CLOSING = ("Jeg vil gerne komme til en samtale og se produktionen på nærmeste fabrik. Medbring en en-sides baseline "
           "for performanceopfølgning og et forslag til, hvordan jeg starter i uge 1 — så vi hurtigt kan se om vi "
           "er et godt match.")

# ------------------------------------------------------------------ CV
PROFILE = ("Analytisk drifts- og projektleder med 20+ år inden for reguleret produktion, teknisk drift og "
           "vedligehold, samt ledelsesansvar siden 2003 for teams på 5 til 25 med fuldt P&L-ansvar. Jeg leder "
           "tværfaglige opgaver fra analyse til eksekvering med klare strukturer, milepæle, RACI og opfølgning. "
           "Dokumenterede resultater: +40% produktivitet, −40% energiomkostninger, nul kritiske afvigelser ved "
           "aflevering på 37 samtidige CAPEX-projekter (DKK 2–10 mio. hver) under GMP/FDA/EMA hos Novo Nordisk. "
           "Professionel og aktiv Claude-koder: bygger investeringsmodeller (NPV, IRR, følsomhed, scenarier), "
           "KPI-dashboards og digitale tjeklister som driften kører på. B.Tech (EQF 6) teknologiledelse og "
           "maskinteknik; elautoriseret maskinmester LV/MV/HV; dansk modersmål, engelsk flydende.")

PRACTICE = [
    ("Projektledelse og CAPEX-styring",
     "Ledelse af 37 samtidige CAPEX-projekter (DKK 2–10 mio. hver) under GMP/FDA/EMA hos Novo Nordisk: business "
     "cases, tidsplan, økonomi, risici, ressourcer og månedlig rapportering til ledelse og bygherre. Nul kritiske "
     "afvigelser ved aflevering. Fuldt P&L-ansvar i egen virksomhed (ELOHVAC ApS) med tilbud, indkøb og "
     "leverandøraftaler."),

    ("KPI, data og ledelsesrapportering",
     "Udvikling af KPI-tavler, månedlige performance reviews og driftsrapportering i SAP ERP, Power BI og Excel/"
     "Power Query. Omsætning af data til klare beslutningsgrundlag for ledelsen. Automatiseret rapportering via "
     "Python og Claude API."),

    ("Tværgående forbedringer og standardisering",
     "Implementering af 5S, Standard Work, PDCA og A3 på tværs af produktion, vedligehold og engineering. "
     "Fælles processer, kompetencematricer og onboarding på tværs af teams. Styrkelse af best practice uden at "
     "gå på kompromis med den enkelte fabriks lokale forhold."),

    ("Teknisk drift og vedligehold",
     "5 år som drifts- og vedligeholdelsesleder på Biofos (Lynetten) med 24/7-anlæg: pumper, HVAC, "
     "højspændingstavler og SCADA. Forebyggende vedligehold, nul uplanlagte stop i fem år. El-autoriseret "
     "maskinmester (LV/MV/HV) med erfaring i tavler, styring, UPS og køleanlæg."),

    ("Sikkerhed, kvalitet og overholdelse",
     "LOTO, APV, risikovurdering, sikkerhedsrunderinger, toolbox-møder og nærved-hændelser. Kvalitets- og "
     "sikkerhedskrav under GMP/FDA/EMA med nul kritiske fund ved aflevering."),

    ("Digital drift og AI-understøttelse",
     "SAP ERP, CMMS, Power BI, Excel/Power Query, Microsoft 365, Python, Claude API / Claude Code. Automatiseret "
     "KPI-rapportering, digitale tjeklister, dokumentationsflow og investeringsmodeller med NPV, IRR og "
     "følsomhedsanalyse."),
]

MODELS = [
    ("Projekt- og investeringsstyring",
     "Business cases, CAPEX-governance, prioriteringsramme, budgetopfølgning, risikostyring, gevinstrealisering, "
     "projektplaner med milepæle, kritisk vej, 4-ugers rulleplan, KS-plan, egenkontrol, afleveringsforretning, "
     "leverandørstyring, snitflader mellem fag"),

    ("Performance og KPI",
     "Production Performance Reviews, KPI-værktøjer, ledelsesrapportering, OEE, OTD, MTBF/MTTR, kapacitetsplanlægning, "
     "visuel ledelse, KPI-tavler, månedshjul, eskaleringstrappe, Gemba-gange"),

    ("Lean, TPS og problemløsning",
     "5S, Kaizen, PDCA, A3, VSM, Standard Work, SMED, TPM, Kanban/WIP-styring, Poka-Yoke, Jidoka, 5xHvorfor, "
     "Ishikawa/fiskeben, FMEA, Toyota Kata, flaskehalsanalyse"),

    ("Ledelse uden formelt ansvar",
     "SLII (situationsbestemt ledelse), GROW coaching, SBI-feedback, 1:1-samtaler, kompetencematricer, "
     "udviklingsplaner, 30-60-90-dages plan, psykologisk tryghed, anerkendelse, følgeskab uden titel"),

    ("Kvalitet, sikkerhed og arbejdsmiljø",
     "APV, LOTO, sikkerhedsrunderinger, nærved-hændelser, toolbox-møder, GMP/FDA/EMA, audit readiness, "
     "brandsikring, nødudgange, hygiejnekrav, DS/HD 60364, el-autorisationsområdet"),

    ("Digital, ERP og AI",
     "SAP ERP, CMMS, Power BI, Excel/Power Query, Microsoft 365, Python, Claude API / Claude Code, prompt- og "
     "agentdesign, automatiseret rapportering, digitale tjeklister, investeringsmodeller (NPV, IRR, følsomhed, "
     "scenarier)"),

    ("Forretning og økonomi",
     "Fuldt P&L-ansvar, budget- og omkostningsstyring, tilbudsberegning, indkøb, leverandør- og kundeforhandling, "
     "serviceaftaler/SLA"),
]

ACHIEVEMENTS = [
    ("Nul uplanlagte stop i fem år",
     "på Biofos (Lynetten) 24/7-anlæg gennem forebyggende vedligehold, 5S, Standard Work og PDCA."),
    ("Nul kritiske afvigelser ved aflevering",
     "på 37 samtidige CAPEX-projekter (DKK 2–10 mio. hver) under GMP/FDA/EMA hos Novo Nordisk."),
    ("+40% produktivitet",
     "i en teknisk serviceoperation gennem datadrevet planlægning og standardiseret arbejde."),
    ("−40% energiomkostninger",
     "i reguleret produktion — opretholdt efter projektorganisationen blev opløst."),
    ("Teams på tværs af to lande",
     "25 specialister, et 14-mands produktionsteam, et 12-mands værksted, 5 elektrikere og 3 lærlinge — alle "
     "med kompetencematricer og udviklingsplaner."),
]

EXPERIENCE = [
    ("Ejer / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ servicepladser i Storkøbenhavn · fuldt P&L, tilbud og leverandøraftaler",
     [("Fuldt driftsansvar",
       "daglig produktionplanlægning, kapacitet mod ordrebeholdning, materiale- og reservedele-flow, "
       "kvalitetskontrol, levering til tiden og omkostninger — gennemgås hver morgen mod standard arbejde, 5S, "
       "visuelle tavler og KPI'er."),
      ("Personaleledelse",
       "daglig planlægning, 1:1 og MUS, kompetencematrix, sikkerhedsopfølgning og struktureret oplæring på tværs "
       "af skiftende byggepladser og prioriteter."),
      ("AI-understøttet ledelse",
       "bygget den digitale ryggrad selv — ERP-baseret ordre- og reservedelsstyring, Power BI dashboards og "
       "Python/Claude API-værktøjer til planlægning, tilbud, tjeklister og rapportering; produktivitet over "
       "+40%."),
      ("EHS og overholdelse",
       "risikovurdering ved hver ny plads, LOTO, håndtering af nærved-hændelser og dokumenteret service; nul "
       "kritiske afvigelser i serviceporteføljen.")]),

    ("Senior idriftsættelsesingeniør / Projektleder, el-anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige CAPEX-projekter, DKK 2–10 mio. hver · 25 specialister på tværs af engineering, indkøb og "
     "anlægsdrift · GMP/FDA/EMA",
     [("Porteføljelevering",
       "tidsplan, økonomi, risici, ressourcer og månedlig rapportering til ledelse og bygherre på tværs af "
       "engineering, indkøb og anlægsdrift."),
      ("Tværfaglig ledelse af 25 specialister",
       "idriftsættelse og kvalificering (FAT/SAT, IQ/OQ/PQ, valideringsdokumentation) med afvigelseshåndtering, "
       "CAPA og ændringskontrol i en aktiv revisionsspor — nul kritiske fund ved aflevering under GMP/FDA/EMA."),
      ("Energiprogram",
       "−40% energiomkostninger gennem struktureret PDCA, A3-problemløsning og standardiseret arbejde; SAP ERP "
       "til økonomi, aktiver og ordrekontrol."),
      ("Driftsnær virkelighed",
       "dagligt arbejde i rene rum, lagre og produktion: arbejdstilladelser, LOTO, renrumsdisciplin og grænseflader "
       "til Kvalitet, Vedligehold og Produktion.")]),

    ("Projekt- og værkstedsleder, ventilation og klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktion- og montageteam · 11 samtidige projekter (DKK 2–10 mio.) · specifikation til formel aflevering",
     [("Daglig ledelse og flow",
       "kapacitetsplanlægning og flowkontrol på 11 samtidige projekter, fra specifikation til formel aflevering."),
      ("Daglige huddles og flaskehalsanalyse",
       "standardiseret arbejde på hver station, med et markant løft i leveringsevne og førstegangs-kvalitet."),
      ("Leverandører og underentreprenører",
       "kontraktgrundlag, sikkerhedsdokumentation og afleveringspakker.")]),

    ("Vedligeholdelses- og driftsleder / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7-anlægsdrift · pumper, HVAC, højspændingstavler og SCADA · drifts- og vedligeholdelses-budgetter i SAP",
     [("Kritisk 24/7-drift",
       "driftsstabilitet, forebyggende vedligehold og hurtig fejlfinding med nul tolerance for uplanlagte stop."),
      ("Struktureret vedligehold",
       "standard arbejde, 5S, PDCA forebyggende vedligeholdelsesplan, A3 årsagsanalyse, reservedels-flow og kritiske "
       "reservedele."),
      ("Skifteholdsdrift og sikkerhedsdisciplin",
       "LOTO, risikovurdering, nærved-hændelsesrapportering og toolbox-møder; KPI'er og drifts-budgetter i SAP ERP.")]),

    ("Elektromekaniker / produktionsteamleder",
     "ARJ Engineering · Tehran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · vagtplanlægning, materiale- og lagerstyring",
     [("Produktionsteamsledelse",
       "vagtplanlægning, materiale- og lagerstyring, linjeforsyning, målopfølgning og situationsbestemt coaching."),
      ("Teknisk problemløsning",
       "reparation og diagnose af elektriske og mekaniske anlæg gennem struktureret årsagsanalyse.")]),
]

EDUCATION = [
    ("B.Tech (EQF-niveau 6) — teknologiledelse og maskinteknik",
     "Copenhagen School of Marine Engineering & Technology Management · 2017 – 2022 · karakter 7,6/12"),
    ("El- og mekanisk design, el-teknik (EQF-niveau 6)",
     "Tehran Technical University · 2000 – 2003"),
    ("HF (matematik og fysik)", "VUC · 2012 – 2017"),
]

CERTS = [
    ("El-autorisation (LV/MV/HV) — elautoriseret maskinmester", "Sikkerhedsstyrelsen · maj 2023"),
    ("Lean-praksis — 5S, PDCA, værdistrømsanalyse, A3 og Kaizen", "Anvendt i drift · 2017 – nu"),
    ("Køl- og klimaanlæg (AMU)", "Mercantec · mar. 2021"),
    ("STCW-søfartsbeviser — maskinvagtsbevis (A-III/1), skibssikkerhedsofficer (VI/5), tankskibsgrundlæggende (V/1-1, V/1-2)",
     "Søfartsstyrelsen · 2021 – 2023"),
    ("Arbejdsmiljø §16 og sikkerhedsbevidsthed (VI/6-1)", "Søfartsstyrelsen · maj 2021"),
]

LANGUAGES = ("Dansk (modersmål) · Engelsk (flydende i skrift og tale) · Persisk/farsi (modersmål) · Kørekort B")

REFERENCES = ("Tidligere ledere hos Novo Nordisk A/S (Kalundborg) og Biofos (Lynetten) — kan oplyses på forespørgsel.")

KEYWORDS = (
    "Operations Development Manager · CRH Concrete · produktion · 10 fabrikker · performance · eksekvering · "
    "Operations Director · produktionschefer · CAPEX · investeringsportefølje · business cases · governance · "
    "prioritering · budgetopfølgning · risici · gevinstrealisering · standardisering · best practice · fælles "
    "processer · forbedringsinitiativer · planlægning · effektivitet · footprint · kvalitet · sikkerhed · "
    "omkostningsreduktion · taktiske · strategiske · beslutningsoplæg · analyser · opfølgning · tværgående · "
    "datadrevet · KPI · nøgletal · beslutningsgrundlag · interessenter · følgeskab · ledelsessupport · "
    "projektledelse · controlling · industriel virksomhed · konsulentbranchen · kommunikation · dansk · engelsk · "
    "overblik · ansvar · relationer · uddannelse · engineering · supply chain · økonomi · business development · "
    "bæredygtighed · CO2-reduktion · genanvendt beton · Low Carbon Concrete · Varde · Linå · Tilst · Hobro · "
    "Viby Sjælland · Ringsted · Søndersø · Borup · Brørup · Randers · Måløv · elautoriseret maskinmester LV/MV/HV · "
    "B.Tech · teknologiledelse og maskinteknik · SLII · GROW · SBI · 1:1 · kompetencematrice · 30-60-90 · tavlemøder · "
    "visuel ledelse · KPI · RACI · eskaleringstrappe · PDCA · A3 · 5xHvorfor · Ishikawa · 5S · standard arbejde · "
    "Gemba · LOTO · APV · sikkerhedsrundering · nærved-hændelser · toolbox-møder · SAP ERP · CMMS · Power BI · Excel/"
    "Power Query · Python · Claude API · NPV · IRR · scenarier"
)

FIRST90 = [
    ("Uge 1",
     "På de nærmeste fabrikker, ikke på kontoret: mød Operations Director, produktionschefer og nøglemedarbejdere; "
     "lær produktion, KPI'er og aktuelle udfordringer at kende; gennemgå CAPEX-pipeline og igangværende "
     "forbedringsinitiativer; identificer de mest presserende flaskehalse."),
    ("Dag 1–30",
     "Én side baseline over performance på tværs af de 10 fabrikker: kapacitet, kvalitet, sikkerhed, levering og "
     "omkostninger. Bekræft opgavefordeling og ansvar (RACI) med Operations Director. Fastlæg den månedlige "
     "Production Performance Review-rytme og KPI-værktøjerne. Gennemfør første sikkerhedsrunde på to fabrikker."),
    ("Dag 31–60",
     "Kør de første forbedringsinitiativer efter planen med målelige resultater. Gennemfør en fuld gennemgang af "
     "CAPEX-processen: business cases, governance, prioritering og budgetopfølgning. Evaluer to eksisterende "
     "KPI'er og foreslå justeringer, hvor data ikke fører til handling. Opdater risikoregister for investerings-"
     "porteføljen."),
    ("Dag 61–90",
     "Driftsstabil performanceopfølgning med kørende månedlige reviews, dokumenterede KPI'er og et CAPEX-flow der "
     "fungerer. Overdrag værktøjerne — KPI-tavler, investeringsmatrix, forbedringspipeline og risikoregister — så "
     "systemet kører videre uanset hvem der er på plads. Evaluer de første 90 dages resultater med Operations "
     "Director og læg plan for de næste 90 dage, inklusive mål for standardisering på tværs af fabrikkerne."),
]


def build(path):
    m = MasterDoc(TEMPLATE, lang="da-DK")

    # ---------------------------------------------------------------- side 1: ansøgning
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta(RECIPIENT)

    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, SUBJECT, bold=True, color="1A1A1A")

    for t in OPENING:
        m.para(t, after=80)

    for label, body in BULLETS:
        m.bullet(label, body, after=40)

    m.para(MIRROR, after=80)
    m.para(HONEST, after=80)
    m.para(CULTURE, after=80)
    m.para(PRACTICAL, after=80)
    m.para(CLOSING, after=80)

    m.meta("Med venlig hilsen,", after=20)
    m.meta("Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+: CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "LEDERPROFIL")
    m.para(PROFILE, after=80)

    m.section("LEDERKOMPETENCER — BEVIS, IKKE PÅSTANDE")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("LEDERMODELLER OG METODER — ANVENDT I PRAKSIS",
                   ("Område", "Værktøjer"), MODELS)

    m.section("UDVALGTE RESULTATER")
    for label, body in ACHIEVEMENTS:
        m.bullet(label, body, after=30)

    m.section("PROFESSIONEL ERFARING")
    for title, meta, scope, bullets in EXPERIENCE:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=30)

    m.section("UDDANNELSE")
    for t, meta in EDUCATION:
        m.edu(t, meta)

    m.section("CERTIFIKATER OG AUTORISATIONER")
    for t, meta in CERTS:
        m.edu(t, meta)

    m.section("SPROG")
    m.para(LANGUAGES, after=80, justify=False)

    m.section("REFERENCER")
    m.para(REFERENCES, after=80, justify=False)

    m.section("KORE KOMPETENCER OG NØGLEORD")
    m.para(KEYWORDS, after=80)

    m.models_table("FØRSTE 90 DAGE — SYSTEMET JEG MEDBRINGER",
                   ("Hvornår", "Hvad der er på plads"), FIRST90)

    return m.save(path,
                  title="Ansøgning og CV — Operations Development Manager, CRH Concrete",
                  subject="Operations Development Manager · CRH Concrete · produktion · CAPEX · KPI",
                  keywords=("Operations Development Manager, CRH Concrete, produktion, CAPEX, KPI, performance, "
                            "forbedring, standardisering, business cases, governance, NPV, IRR, Python, SAP ERP, "
                            "Power BI, elautoriseret maskinmester"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. Ansøgning side 1, "
                           "CV sider 2-4.")


if __name__ == "__main__":
    out = "/home/user/ATS-RESUME/Shahram_Ajloo_CRHConcrete_OperationsDevelopmentManager.docx"
    print("OK", build(out))
