# -*- coding: utf-8 -*-
"""
Hørkram Foodservice — Teamleder med erfaring som ejendomsfunktionær, Sorø.
Dansk (JD-sprog). Ansøgning + CV i ét dokument, masterdesign.

Mission-første ansøgning (side 1): handler om opgaven, ejendommen og teamet —
ikke om mig. Projekterer at systemet til at holde ejendommen kørende er bygget
fra dag 1. CV (sider 2–4) dokumenterer bevis.

Ærlighed: JD'en efterspørger en faglært håndværker (gerne elektriker/VVS).
Jeg er el-ingeniør og elautoriseret maskinmester (LV/MV/HV) med praktisk
elektromekanisk baggrund — ikke uddannet elektriker. Det siges én gang, præcist,
uden at påtage mig titlen elektriker/elinstallatør.

Professionel og aktiv Claude-koder: investeringsmodeller (NPV/IRR), dashboards,
digitale tjeklister, dokumentationsflow, automatiseret rapportering.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

TEMPLATE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = ("Teamleder med erfaring som ejendomsfunktionær | Hørkram Foodservice, Sorø")
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv, Danmark")

DATE = "3. november 2026"
RECIPIENT = ("Hørkram Foodservice A/S · Centervej 1, 4180 Sorø · Att: Julie Ditte Bruun "
             "Jacobsen, rekrutteringskoordinator, Anzet A/S")
SUBJECT = "Ansøgning: Teamleder med erfaring som ejendomsfunktionær, Sorø"

# ------------------------------------------------------------------ side 1: ansøgning
OPENING = [
    "Hørkram leverer mad og varer til professionelle køkkener over hele landet. Bag det står et stort "
    "lager med køl og frost, egen kødproduktion og en transportflåde, der ikke kan vente. Hvis en port "
    "sidder fast, et kølerum svigter eller rampen er glat, mærker hele forretningen det straks. "
    "Opgaven i denne stilling er at holde ejendommen i Sorø kørende — bygninger, porte, ramper, døre, "
    "gulve og belysning i topform; køl, frost, ventilation, varme og trykluft under opsyn; tekniske "
    "runder der fanger fejl før de bliver til problemer; og personaleansvar for 12 medarbejdere på "
    "værkstedet og i servicegruppen, så driften aldrig står stille.",
]

BULLETS = [
    ("Klare strukturer, opgavefordeling og opfølgning",
     "Jeg fordeler opgaverne mellem de 2 medarbejdere på værkstedet og de 10 i servicegruppen, "
     "sætter klare ansvar (RACI) og følger op i en fast ugentlig rytme. Ingen opgave ligger og "
     "venter på, at nogen opdager den — den har en ejer og en deadline."),

    ("Tekniske runder og forebyggende vedligehold",
     "Gå faste runder og fange fejl før de bliver til problemer. Holde øje med køl, frost, "
     "ventilation, varme og trykluft og kalde de rette folk ind, når det brænder på. Forebyggende "
     "vedligehold er billigere end akutte stop i en 24/7-virksomhed."),

    ("Reparationer på tværs af fag og eksterne leverandører",
     "Lidt tømrer, lidt maler, lidt el og VVS — og evnen til at vurdere, hvornår en opgave skal "
     "løses internt, og hvornår en ekstern håndværker skal ind. Indhente tilbud, koordinere og "
     "følge op, så arbejdet bliver udført til tiden og til den rigtige pris."),

    ("Personaleansvar og souschef-rollen",
     "Teamleder for 12 medarbejdere og souschef samt sparringspartner for den nærmeste leder. "
     "Tavlemøder, 1:1-samtaler, kompetencematricer og situationsbestemt ledelse, så teamet ved, "
     "hvad der forventes, og kan arbejde selvstændigt og ansvarligt."),
]

MIRROR = ("Mod dine krav: relevant teknisk uddannelse (B.Tech, EQF 6, teknologiledelse og "
          "maskinteknik); elautoriseret maskinmester (LV/MV/HV); erfaring med bygningsdrift, "
          "teknisk vedligehold og ejendomsservice; ledelseserfaring og lyst til at gå forrest; "
          "klart kommunikerende med købmandskab til at vurdere tilbud; kørekort B; Office-pakken; "
          "dansk og engelsk. Jeg er struktureret, mødestabil, pligtopfyldende og fleksibel — klar "
          "til at træde til uden for normale arbejdstider i en virksomhed, der kører 24/7.")

HONEST = ("Én ting siges helt ærligt: stillingen efterspørger en faglært håndværker, gerne "
          "elektriker eller VVS'er. Jeg er el-ingeniør og elautoriseret maskinmester (LV/MV/HV) "
          "med en praktisk elektromekanisk baggrund — ikke uddannet elektriker, og jeg påtager mig "
          "ikke den titel. Min el-autorisation og 20+ år med tekniske anlæg gør, at jeg kan vurdere "
          "el- og VVS-opgaver, fejlfinde og koordinere de rette fagfolk. Det, jeg ikke har, er et "
          "svendebrev; det, jeg har, er dokumenteret driftserfaring, ledelsesansvar og evnen til at "
          "holde tekniske installationer kørende.")

CULTURE = ("Hvorfor Hørkram, og hvorfor nu. Hørkram er en virksomhed i stærk vækst — 5 mia. kr. i "
           "omsætning i 2025 — med rødder tilbage til 1960'erne og hovedsæde i Sorø. Kulturen med "
           "flad struktur, frihed under ansvar, ordentlighed og høj anciennitet passer til den måde, "
           "jeg leder på: tillidsbaseret, dialogorienteret og med tydelige forventninger. Jeg vil "
           "gerne bidrage til at holde ejendommen kørende, så lager, produktion og transport kan "
           "levere til kunderne hver dag.")

PRACTICAL = ("Praktisk: bosat i Måløv, kørekort B, klar til at starte snarest. Jeg er selvstændig, "
             "struktureret, mødestabil og pligtopfyldende — og fleksibel nok til at træde til uden "
             "for den normale arbejdstid, når en 24/7-drift har brug for det. Rollen er i Sorø, og "
             "jeg er indstillet på den transport det kræver. Jeg afvikler min egen virksomhed "
             "(ELOHVAC ApS), så der er ingen konkurrerende forpligtelser.")

CLOSING = ("Jeg vil gerne komme til en samtale på stedet i Sorø. Tretten minutter på ejendommen med "
           "teamet er mere værd end endnu en side tekst — og jeg vil medbringe en en-sides baseline "
           "for ejendomsdriften og et forslag til, hvordan jeg starter i uge 1.")

# ------------------------------------------------------------------ CV
PROFILE = ("Erfaren drifts- og projektleder med 20+ år inden for reguleret produktion, "
           "teknisk drift og vedligehold, samt ledelsesansvar siden 2003 for teams på 5 til 25 med "
           "fuldt P&L-ansvar. Jeg leder tværfaglige opgaver fra planlægning til eksekvering med "
           "klare strukturer, milepæle, RACI og opfølgning. Dokumenterede resultater: +40% "
           "produktivitet, −40% energiomkostninger, nul kritiske afvigelser ved aflevering på 37 "
           "samtidige CAPEX-projekter (DKK 2–10 mio. hver) under GMP/FDA/EMA hos Novo Nordisk. "
           "Professionel og aktiv Claude-koder: bygger investeringsmodeller (NPV, IRR, "
           "følsomhed, scenarier), dashboards og digitale tjeklister som driften kører på. B.Tech "
           "(EQF 6) teknologiledelse og maskinteknik; elautoriseret maskinmester LV/MV/HV; dansk "
           "modersmål, engelsk flydende.")

PRACTICE = [
    ("Personaleledelse og teamledelse",
     "Daglig ledelse af 5 elektrikere og 3 lærlinge i egen autoriseret virksomhed (ELOHVAC ApS) samt "
     "koordinering af 25 specialister på tværs af engineering, indkøb og anlæg hos Novo Nordisk. "
     "Tavlemøder, 1:1-samtaler, MUS, kompetencematricer, 30-60-90-dages onboarding og "
     "situationsbestemt ledelse (SLII)."),

    ("Bygningsdrift og teknisk vedligehold",
     "5 år som drifts- og vedligeholdelsesleder på Biofos (Lynetten) med 24/7-anlæg: pumper, HVAC, "
     "højspændingstavler og SCADA. Forebyggende vedligehold, 5S, Standard Work, PDCA og A3 "
     "årsagsanalyse. Nul uplanlagte stop i fem år."),

    ("El- og teknisk fejlfinding",
     "El-autoriseret maskinmester (LV/MV/HV) med erfaring i tavler, styring, UPS, nød- og "
     "panikbelysning, adgangskontrol og køleanlæg. Fejlfinding på tværs af el, mekanik og VVS i "
     "drift og projekter."),

    ("Leverandør- og indkøbsstyring",
     "Indhentning af tilbud, koordinering af eksterne håndværkere og leverandører, kontrakt- og "
     "økonomiopfølgning. Købmandskab til at vurdere, om et tilbud hænger sammen. Fuldt P&L-ansvar i "
     "egen virksomhed."),

    ("Sikkerhed, brandsikring og hygiejne",
     "LOTO, APV, risikovurdering, sikkerhedsrunderinger, toolbox-møder og nærmest-hændelser. "
     "Brand-, nødudgangs- og hygiejnekrav under GMP/FDA/EMA med nul kritiske fund ved aflevering."),

    ("Digital drift og AI-understøttelse",
     "SAP ERP, CMMS, Power BI, Excel/Power Query, Microsoft 365, Python, Claude API / Claude Code. "
     "Automatiseret KPI-rapportering, digitale tjeklister, dokumentationsflow og investeringsmodeller "
     "med NPV, IRR og følsomhedsanalyse."),
]

MODELS = [
    ("Personaleledelse",
     "SLII (situationsbestemt ledelse: instruerende, coachende, støttende, delegerende), GROW "
     "coaching, SBI-feedback, 1:1-samtaler, MUS/GRUS, delegeringstrappen, kompetencematricer, "
     "individuelle udviklingsplaner, 30-60-90-dages plan, psykologisk tryghed, anerkendelse"),

    ("Drifts- og performanceledelse",
     "Tavlemøder/huddles, visuel ledelse, KPI-tavler, Gemba-gange, ledelseskadence, "
     "eskaleringstrappe, RACI, månedshjul, OEE, OTD, MTBF/MTTR, kapacitetsplanlægning"),

    ("Lean, TPS og problemløsning",
     "5S, Kaizen, PDCA, A3, VSM, Standard Work, SMED, TPM, Kanban/WIP-styring, Poka-Yoke, Jidoka, "
     "5xHvorfor, Ishikawa/fiskeben, FMEA, Toyota Kata, flaskehalsanalyse"),

    ("Projekt- og vedligeholdsstyring",
     "Projektplaner med milepæle, kritisk vej, 4-ugers rulleplan, vedligeholdsplaner, KS-plan, "
     "egenkontrol, afleveringsforretning, leverandørstyring, snitflader mellem fag"),

    ("Kvalitet, sikkerhed og arbejdsmiljø",
     "APV, LOTO, sikkerhedsrunderinger, nærved-hændelser, toolbox-møder, GMP/FDA/EMA, audit "
     "readiness, brandsikring, nødudgange, hygiejnekrav, DS/HD 60364, el-autorisationsområdet"),

    ("Digital, ERP og AI",
     "SAP ERP, CMMS, Power BI, Excel/Power Query, Microsoft 365, Python, Claude API / Claude Code, "
     "prompt- og agentdesign, automatiseret rapportering, digitale tjeklister, investeringsmodeller "
     "(NPV, IRR, følsomhed, scenarier)"),

    ("Forretning og økonomi",
     "Fuldt P&L-ansvar, budget- og omkostningsstyring, tilbudsberegning, indkøb, leverandør- og "
     "kundeforhandling, serviceaftaler/SLA"),
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
     "25 specialister, et 14-monds produktionsteam, et 12-mands værksted, 5 elektrikere og 3 "
     "lærlinge — alle med kompetencematricer og udviklingsplaner."),
]

EXPERIENCE = [
    ("Ejer / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ servicepladser i Storkøbenhavn · fuldt P&L, tilbud og "
     "leverandøraftaler",
     [("Fuldt driftsansvar",
       "daglig produktionplanlægning, kapacitet mod ordrebeholdning, materiale- og reservedele-flow, "
       "kvalitetskontrol, levering til tiden og omkostninger — gennemgås hver morgen mod standard "
       "arbejde, 5S, visuelle tavler og KPI'er."),
      ("Personaleledelse",
       "daglig planlægning, 1:1 og MUS, kompetencematrix, sikkerhedsopfølgning og struktureret "
       "oplæring på tværs af skiftende byggepladser og prioriteter."),
      ("AI-understøttet ledelse",
       "bygget den digitale ryggrad selv — ERP-baseret ordre- og reservedelsstyring, Power BI "
       "dashboards og Python/Claude API-værktøjer til planlægning, tilbud, tjeklister og "
       "rapportering; produktivitet over +40%."),
      ("EHS og overholdelse",
       "risikovurdering ved hver ny plads, LOTO, håndtering af nærved-hændelser og dokumenteret "
       "service; nul kritiske afvigelser i serviceporteføljen.")]),

    ("Senior idriftsættelsesingeniør / Projektleder, el-anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige CAPEX-projekter, DKK 2–10 mio. hver · 25 specialister på tværs af engineering, "
     "indkøb og anlægsdrift · GMP/FDA/EMA",
     [("Porteføljelevering",
       "tidsplan, økonomi, risici, ressourcer og månedlig rapportering til ledelse og bygherre på "
       "tværs af engineering, indkøb og anlægsdrift."),
      ("Tværfaglig ledelse af 25 specialister",
       "idriftsættelse og kvalificering (FAT/SAT, IQ/OQ/PQ, valideringsdokumentation) med "
       "afvigelseshåndtering, CAPA og ændringskontrol i en aktiv revisionsspor — nul kritiske "
       "fund ved aflevering under GMP/FDA/EMA."),
      ("Energiprogram",
       "−40% energiomkostninger gennem struktureret PDCA, A3-problemløsning og standardiseret "
       "arbejde; SAP ERP til økonomi, aktiver og ordrekontrol."),
      ("Driftsnær virkelighed",
       "dagligt arbejde i rene rum, lagre og produktion: arbejdstilladelser, LOTO, renrumsdisciplin "
       "og grænseflader til Kvalitet, Vedligehold og Produktion.")]),

    ("Projekt- og værkstedsleder, ventilation og klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktion- og montageteam · 11 samtidige projekter (DKK 2–10 mio.) · specifikation "
     "til formel aflevering",
     [("Daglig ledelse og flow",
       "kapacitetsplanlægning og flowkontrol på 11 samtidige projekter, fra specifikation til "
       "formel aflevering."),
      ("Daglige huddles og flaskehalsanalyse",
       "standardiseret arbejde på hver station, med et markant løft i leveringsevne og "
       "førstegangs-kvalitet."),
      ("Leverandører og underentreprenører",
       "kontraktgrundlag, sikkerhedsdokumentation og afleveringspakker.")]),

    ("Vedligeholdelses- og driftsleder / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7-anlægsdrift · pumper, HVAC, højspændingstavler og SCADA · drifts- og vedligeholdelses-"
     "budgetter i SAP",
     [("Kritisk 24/7-drift",
       "driftsstabilitet, forebyggende vedligehold og hurtig fejlfinding med nul tolerance for "
       "uplanlagte stop."),
      ("Struktureret vedligehold",
       "standard arbejde, 5S, PDCA forebyggende vedligeholdelsesplan, A3 årsagsanalyse, reservedels-"
       "flow og kritiske reservedele."),
      ("Skifteholdsdrift og sikkerhedsdisciplin",
       "LOTO, risikovurdering, nærved-hændelsesrapportering og toolbox-møder; KPI'er og drifts-"
       "budgetter i SAP ERP.")]),

    ("Elektromekaniker / produktionsteamleder",
     "ARJ Engineering · Tehran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · vagtplanlægning, materiale- og lagerstyring",
     [("Produktionsteamsledelse",
       "vagtplanlægning, materiale- og lagerstyring, linjeforsyning, målopfølgning og "
       "situationsbestemt coaching."),
      ("Teknisk problemløsning",
       "reparation og diagnose af elektriske og mekaniske anlæg gennem struktureret årsagsanalyse.")]),
]

EDUCATION = [
    ("B.Tech (EQF-niveau 6) — teknologiledelse og maskinteknik",
     "Copenhagen School of Marine Engineering & Technology Management · 2017 – 2022 · karakter 7,6/12"),
    ("El- og mekanisk design, el-teknik (EQF-niveau 6)",
     "Tehran Technical University · 2000 – 2003"),
    ("HF (matematik og fysik)",
     "VUC · 2012 – 2017"),
]

CERTS = [
    ("El-autorisation (LV/MV/HV) — elautoriseret maskinmester",
     "Sikkerhedsstyrelsen · maj 2023"),
    ("Lean-praksis — 5S, PDCA, værdistrømsanalyse, A3 og Kaizen",
     "Anvendt i drift · 2017 – nu"),
    ("Køl- og klimaanlæg (AMU)",
     "Mercantec · mar. 2021"),
    ("STCW-søfartsbeviser — maskinvagtsbevis (A-III/1), skibssikkerhedsofficer (VI/5), "
     "tankskibsgrundlæggende (V/1-1, V/1-2)",
     "Søfartsstyrelsen · 2021 – 2023"),
    ("Arbejdsmiljø §16 og sikkerhedsbevidsthed (VI/6-1)",
     "Søfartsstyrelsen · maj 2021"),
]

LANGUAGES = ("Dansk (modersmål) · Engelsk (flydende i skrift og tale) · Persisk/farsi (modersmål) · "
             "Kørekort B")

REFERENCES = ("Tidligere ledere hos Novo Nordisk A/S (Kalundborg) og Biofos (Lynetten) — kan "
              "oplyses på forespørgsel.")

KEYWORDS = (
    "Teamleder · Ejendomsfunktionær · Bygningsdrift · Teknisk vedligehold · Personaleansvar · "
    "Ejendomsservice · Servicegruppe · Værksted · Bygninger · Porte · Ramper · Døre · Gulve · "
    "Belysning · Reparationer · Tømrer · Maler · El · VVS · Tekniske runder · Køl · Frost · "
    "Ventilation · Varme · Trykluft · Udearealer · Parkering · Vintertjeneste · Tilbud · "
    "Eksterne håndværkere · Leverandører · Brandsikring · Nødudgange · Hygiejnekrav · "
    "Kørekort B · Office-pakken · Dansk · Engelsk · Lager · Logistik · Fødevarer · Truck · Lift · "
    "SLII · GROW · SBI · MUS · 1:1 · Kompetencematrice · 30-60-90 · Tavlemøder · Visuel ledelse · "
    "KPI · RACI · Eskaleringstrappe · PDCA · A3 · 5xHvorfor · Ishikawa · 5S · Standard Work · "
    "Gemba · LOTO · APV · Sikkerhedsrundering · Nærved-hændelser · Toolbox-møder · SAP ERP · CMMS · "
    "Power BI · Excel/Power Query · Python · Claude API · Investeringer · NPV · IRR · Scenarier · "
    "Hørkram · Sorø · Måløv · Elautoriseret maskinmester LV/MV/HV · B.Tech · Teknologiledelse og "
    "Maskinteknik"
)

FIRST90 = [
    ("Uge 1",
     "På ejendommen i Sorø, ikke på kontoret: gå tekniske runder med medarbejderne på værkstedet "
     "og i servicegruppen; gennemgå åbne opgaver, køl/frost, porte, ramper, døre, gulve, belysning "
     "og sikkerhedsudstyr; mød den nærmeste leder og lær ejendommens kritiske anlæg at kende; "
     "aflæg rapport over de mest presserende vedligeholdelsesopgaver."),
    ("Dag 1–30",
     "Én side baseline over ejendommen: kritiske anlæg, vedligeholdsplan, åbne opgaver, leverandører "
     "og eksterne håndværkere med kontakt og aftaler. Bekræft opgavefordeling, ansvar (RACI) og "
     "opfølgningstavle med teamet. Fastlæg den ugentlige tavlemøderytme. Gennemfør første "
     "sikkerhedsrunde med fokus på brandsikring og nødudgange."),
    ("Dag 31–60",
     "Kør de første forebyggende vedligehold-opgaver efter planen med målelige resultater. "
     "Gennemfør en fuld sikkerhedsrunde (LOTO, APV, brandsikring, nødudgange, hygiejnekrav) med "
     "ejer og frist på eventuelle afvigelser. Evaluer to eksterne leverandører og indhent nye "
     "tilbud, hvor det giver økonomisk mening. Opdater kompetencematricen for alle 12 medarbejdere."),
    ("Dag 61–90",
     "Driftsstabil ejendom med kørende vedligeholdsplan, dokumenterede tekniske runder og et team, "
     "der kender sine opgaver og ansvar. Overdrag værktøjerne — opgavetavle, vedligeholdsplan, "
     "leverandørmatrix og risikoregister — så systemet kører videre uanset hvem der er på vagt. "
     "Evaluer de første 90 dages resultater med den nærmeste leder og læg plan for de næste 90 dage."),
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

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=80)

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
                  title="Ansøgning og CV — Teamleder med erfaring som ejendomsfunktionær, Hørkram Foodservice, Sorø",
                  subject="Teamleder · Ejendomsfunktionær · Bygningsdrift · Personaleledelse · Sorø",
                  keywords=("teamleder, ejendomsfunktionær, bygningsdrift, teknisk vedligehold, "
                            "personaleansvar, køl, frost, ventilation, SLII, GROW, SBI, RACI, PDCA, "
                            "A3, 5S, LOTO, APV, SAP ERP, Power BI, Python, Claude API, NPV, IRR"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1, CV sider 2-4.")


if __name__ == "__main__":
    out = "/home/user/ATS-RESUME/Shahram_Ajloo_Hoerkram_TeamlederEjendomsfunktionær.docx"
    print("OK", build(out))
