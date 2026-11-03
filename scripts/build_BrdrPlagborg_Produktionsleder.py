# -*- coding: utf-8 -*-
"""
Brdr. Plagborg A/S — Leder til produktion af kundetilpassede varebiler, Lindved.
Dansk (JD-sprog). Ansøgning + CV i ét dokument, masterdesign.

Mission-første ansøgning (side 1): handler om opgaven, produktionen og teamet —
ikke om mig. Projekterer at systemet til at holde produktionen kørende er bygget
fra dag 1. CV (sider 2–4) dokumenterer bevis med egne ord, ikke JD-gentagelser.

Stemme: erfaren, konfidensfuld leder. Konkret, dokumenteret, ingen fyldord.
Ledelsesværktøjer væves ind i fortællingen.

Ærlighed: JD'en søger en leder med produktion/teknisk baggrund og gerne erfaring
som teamleder/værkfører/produktionsleder. Jeg har 20+ års teknisk drift og
personaleledelse, men ikke direkte erfaring med opbygning af varebiler. Det siges
én gang, uden at foregive andet.

Professionel og aktiv Claude-koder: investeringsmodeller (NPV/IRR, følsomhed,
scenarier), dashboards, digitale tjeklister, dokumentationsflow.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

TEMPLATE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = ("Leder til produktion af kundetilpassede varebiler | Brdr. Plagborg, Lindved")
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv, Danmark")

DATE = "4. november 2026"
RECIPIENT = ("Brdr. Plagborg A/S · Lindevej 12, 7100 Lindved · Att: Tim Lykke Jensen, "
             "Headhunter, ERHR Rekruttering")
SUBJECT = "Ansøgning: Leder til produktion af kundetilpassede varebiler — Lindved"

# ------------------------------------------------------------------ side 1: ansøgning
OPENING = [
    "Hver dag leverer Brdr. Plagborg kundetilpassede varebiler, lastbiler og påhængsvogne, der skal "
    "stå klare til tiden og efter kundens præcise specifikationer. Bag det står en produktion, der "
    "skal balancere kvalitet, fremdrift og leveringsevne i en travl hverdag. Opgaven i denne stilling "
    "er at stå i spidsen for produktionen: samle medarbejderne om opgaverne, prioritere ressourcer, "
    "følge op på kvalitet og levere resultater — så de 1.500–1.700 årlige opbygninger fortsætter med "
    "den høje standard, kunderne forventer.",
]

BULLETS = [
    ("Et system til produktion, ikke en tilfældighed",
     "Jeg bygger ikke løsninger, der afhænger af at én person opdager fejlen. Jeg bygger et system med "
     "faste tekniske runder, klare ansvar og en ugentlig opfølgning, så et problem fanges før det bliver "
     "til en driftsforstyrrelse. Hver opgave har en ejer og en deadline — intet ligger og venter på at "
     "nogen ser det."),

    ("Synlig ledelse i produktionen",
     "Jeg leder bedst, når jeg er til stede i produktionen. Gå iblandt medarbejderne, se hvordan opgaverne "
     "løses, spørg ind til blokeringer og træf beslutninger på stedet. Synlighed skaber troværdighed, og "
     "troværdighed skaber følgeskab."),

    ("Kvalitet og effektivitet hænger sammen",
     "Kundetilpassede opbygninger kræver præcision — hver bil er unik, men processen skal være stabil. "
     "Jeg sikrer, at kvalitetskravene overholdes uden at gå på kompromis med fremdriften, og at vi leverer "
     "til tiden, hver gang."),

    ("Ledelse af et blandet team",
     "Produktionen rummer medarbejdere med forskellig erfaring og faglighed — kleinsmede, mekanikere, "
     "montører. Min opgave er at fordele opgaver, give klare instruktioner, motivere og stille tydelige "
     "krav. Tavlemøder, 1:1-samtaler og kompetencematricer er værktøjer; tillid og tydelige forventninger "
     "er målet."),
]

MIRROR = ("Stillingen søger en tydelig, handlekraftig leder med teknisk indsigt, produkterfaring og "
          "evnen til at lede mennesker situationsbestemt. Jeg matcher det meste: B.Tech i teknologiledelse "
          "og maskinteknik, elautoriseret maskinmester (LV/MV/HV), 20+ år i teknisk drift og vedligehold, "
          "personaleledelse siden 2003 for teams på 5 til 25 med fuldt P&L-ansvar, kørekort B, flydende "
          "dansk og engelsk. Én ting er anderledes: jeg har ikke direkte erfaring med opbygning af varebiler "
          "eller lastbiler. Det, jeg har, er dokumenteret erfaring med at lede teknisk produktion, vedligehold "
          "og projektleverancer under pres — og evnen til hurtigt at sætte mig ind i et nyt fagligt område.")

HONEST = ("Det ærlige er ikke et kompromis, men et udgangspunkt. Jeg er el-ingeniør og elautoriseret maskinmester "
          "med en praktisk elektromekanisk baggrund — ikke opbygger af varebiler. Jeg kender ikke Plagborgs "
          "specifikke produkter fra før, men jeg kender produktionsledelse, teknisk drift og kvalitetsstyring. "
          "For Brdr. Plagborg betyder det en leder, der forstår de tekniske installationer, kan lede håndværkere "
          "og hurtigt kan lære de specifikke opbygningsprocesser.")

CULTURE = ("Brdr. Plagborg er en ejerledet virksomhed i Lindved, grundlagt i 2002 af de tre brødre Plagborg, med "
           "kerneværdierne solid kvalitet, ærligt købmandskab og gode relationer. Virksomheden er i vækst med en "
           "stor ordrepipeline og har netop leveret sin 20.000. opbygning. Den ambitiøse arbejdskultur med fokus på "
           "trivsel og arbejdslyst passer til den måde, jeg leder på: tillidsbaseret, dialogorienteret og med "
           "tydelige forventninger. Jeg vil gerne bidrage til at holde produktionen kørende, så kunderne får deres "
           "kundetilpassede køretøjer til tiden.")

PRACTICAL = ("Bosat i Måløv med kørekort B, klar til at starte snarest. Lindved tæt ved Vejle og motorvejen er "
             "inden for rimelig kørselsafstand, og jeg er indstillet på den transport det kræver. Jeg afvikler min "
             "egen virksomhed (ELOHVAC ApS), så der er ingen konkurrerende forpligtelser. Struktureret, mødestabil, "
             "pligtopfyldende og fleksibel — som stillingen foreskriver.")

CLOSING = ("Jeg vil gerne komme til en samtale på stedet i Lindved. Tretten minutter i produktionen med teamet er "
           "mere værd end endnu en side tekst — og jeg vil medbringe en en-sides baseline for produktionen og et "
           "forslag til, hvordan jeg starter i uge 1.")

# ------------------------------------------------------------------ CV
PROFILE = ("Erfaren drifts- og projektleder med 20+ år inden for reguleret produktion, teknisk drift og "
           "vedligehold, samt ledelsesansvar siden 2003 for teams på 5 til 25 med fuldt P&L-ansvar. Jeg leder "
           "tværfaglige opgaver fra planlægning til eksekvering med klare strukturer, milepæle, RACI og "
           "opfølgning. Dokumenterede resultater: +40% produktivitet, −40% energiomkostninger, nul kritiske "
           "afvigelser ved aflevering på 37 samtidige CAPEX-projekter (DKK 2–10 mio. hver) under GMP/FDA/EMA "
           "hos Novo Nordisk. Professionel og aktiv Claude-koder: bygger investeringsmodeller (NPV, IRR, "
           "følsomhed, scenarier), dashboards og digitale tjeklister som driften kører på. B.Tech (EQF 6) "
           "teknologiledelse og maskinteknik; elautoriseret maskinmester LV/MV/HV; dansk modersmål, engelsk "
           "flydende.")

PRACTICE = [
    ("Personaleledelse og teamledelse",
     "Daglig ledelse af 5 elektrikere og 3 lærlinge i egen autoriseret virksomhed (ELOHVAC ApS) samt "
     "koordinering af 25 specialister på tværs af engineering, indkøb og anlæg hos Novo Nordisk. Tavlemøder, "
     "1:1-samtaler, MUS, kompetencematricer, 30-60-90-dages onboarding og situationsbestemt ledelse (SLII)."),

    ("Produktionsledelse og teknisk drift",
     "5 år som drifts- og vedligeholdelsesleder på Biofos (Lynetten) med 24/7-anlæg: pumper, HVAC, "
     "højspændingstavler og SCADA. Forebyggende vedligehold, 5S, Standard Work, PDCA og A3 årsagsanalyse. "
     "Nul uplanlagte stop i fem år."),

    ("El- og teknisk fejlfinding",
     "El-autoriseret maskinmester (LV/MV/HV) med erfaring i tavler, styring, UPS, nød- og panikbelysning, "
     "adgangskontrol og køleanlæg. Fejlfinding på tværs af el, mekanik og VVS i drift og projekter."),

    ("Leverandør- og indkøbsstyring",
     "Indhentning af tilbud, koordinering af eksterne håndværkere og leverandører, kontrakt- og økonomiopfølgning. "
     "Købmandskab til at vurdere, om et tilbud hænger sammen. Fuldt P&L-ansvar i egen virksomhed."),

    ("Sikkerhed, kvalitet og overholdelse",
     "LOTO, APV, risikovurdering, sikkerhedsrunderinger, toolbox-møder og nærved-hændelser. Kvalitets- og "
     "sikkerhedskrav under GMP/FDA/EMA med nul kritiske fund ved aflevering."),

    ("Digital drift og AI-understøttelse",
     "SAP ERP, CMMS, Power BI, Excel/Power Query, Microsoft 365, Python, Claude API / Claude Code. Automatiseret "
     "KPI-rapportering, digitale tjeklister, dokumentationsflow og investeringsmodeller med NPV, IRR og "
     "følsomhedsanalyse."),
]

MODELS = [
    ("Personaleledelse",
     "SLII (situationsbestemt ledelse: instruerende, coachende, støttende, delegerende), GROW coaching, "
     "SBI-feedback, 1:1-samtaler, MUS/GRUS, delegeringstrappen, kompetencematricer, individuelle udviklingsplaner, "
     "30-60-90-dages plan, psykologisk tryghed, anerkendelse"),

    ("Drifts- og performanceledelse",
     "Tavlemøder/huddles, visuel ledelse, KPI-tavler, Gemba-gange, ledelseskadence, eskaleringstrappe, RACI, "
     "månedshjul, OEE, OTD, MTBF/MTTR, kapacitetsplanlægning"),

    ("Lean, TPS og problemløsning",
     "5S, Kaizen, PDCA, A3, VSM, Standard Work, SMED, TPM, Kanban/WIP-styring, Poka-Yoke, Jidoka, 5xHvorfor, "
     "Ishikawa/fiskeben, FMEA, Toyota Kata, flaskehalsanalyse"),

    ("Projekt- og produktionsstyring",
     "Projektplaner med milepæle, kritisk vej, 4-ugers rulleplan, vedligeholdsplaner, KS-plan, egenkontrol, "
     "afleveringsforretning, leverandørstyring, snitflader mellem fag"),

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
    "Leder · Produktionsleder · Teamleder · Værkfører · Produktion · Kundetilpassede varebiler · Opbygning · "
    "Varebiler · Lastbiler · Påhængsvogne · Kvalitet · Fremdrift · Leveringsevne · Personaleansvar · Teknisk indsigt · "
    "Håndværkere · Kleinsmede · Mekanikere · Montører · Instruktion · Motivering · Klare krav · Hverdag · "
    "Synlig ledelse · Produktion · Vedligehold · Fejlfinding · El · VVS · Mekanik · Leverandører · Indkøb · "
    "Tilbud · Kontrakter · Brandsikring · Nødudgange · Hygiejnekrav · Kørekort B · Office-pakken · Dansk · Engelsk · "
    "Lager · Logistik · Truck · Lift · SLII · GROW · SBI · MUS · 1:1 · Kompetencematrice · 30-60-90 · Tavlemøder · "
    "Visuel ledelse · KPI · RACI · Eskaleringstrappe · PDCA · A3 · 5xHvorfor · Ishikawa · 5S · Standard Work · Gemba · "
    "LOTO · APV · Sikkerhedsrundering · Nærved-hændelser · Toolbox-møder · SAP ERP · CMMS · Power BI · Excel/Power "
    "Query · Python · Claude API · Investeringer · NPV · IRR · Scenarier · Brdr. Plagborg · Lindved · Vejle · Måløv · "
    "Elautoriseret maskinmester LV/MV/HV · B.Tech · Teknologiledelse og Maskinteknik"
)

FIRST90 = [
    ("Uge 1",
     "På produktionen i Lindved, ikke på kontoret: gå iblandt medarbejderne, lær opbygningsprocessen at kende, "
     "gennemgå åbne opgaver, kvalitets krav og leveringsplaner; mød teamet og den nærmeste leder; identificer de "
     "mest presserende flaskehalse i produktionen."),
    ("Dag 1–30",
     "Én side baseline over produktionen: kapacitet, aktuelle ordrer, kvalitetsafvigelser, leverandører og "
     "eksterne samarbejdspartnere med kontakt og aftaler. Bekræft opgavefordeling, ansvar (RACI) og opfølgningstavle "
     "med teamet. Fastlæg den ugentlige tavlemøderytme. Gennemfør første sikkerhedsrunde."),
    ("Dag 31–60",
     "Kør de første forebyggende vedligehold- og kvalitetsopgaver efter planen med målelige resultater. Gennemfør en "
     "fuld sikkerhedsrunde (LOTO, APV, brandsikring, nødudgange) med ejer og frist på eventuelle afvigelser. Evaluer "
     "to eksterne leverandører og indhent nye tilbud, hvor det giver økonomisk mening. Opdater kompetencematricen for "
     "produktionsteamet."),
    ("Dag 61–90",
     "Driftsstabil produktion med kørende vedligeholdsplan, dokumenterede kvalitetsrunder og et team, der kender sine "
     "opgaver og ansvar. Overdrag værktøjerne — opgavetavle, produktionsplan, leverandørmatrix og risikoregister — "
     "så systemet kører videre uanset hvem der er på vagt. Evaluer de første 90 dages resultater med den nærmeste "
     "leder og læg plan for de næste 90 dage. Fastlæg mål for kvalitet, leveringsevne og medarbejdertrivsel, som "
     "teamet kan arbejde efter fremadrettet."),
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
                  title="Ansøgning og CV — Leder til produktion af kundetilpassede varebiler, Brdr. Plagborg, Lindved",
                  subject="Leder · Produktion · Kundetilpassede varebiler · Lindved",
                  keywords=("leder, produktion, kundetilpassede varebiler, kvalitet, fremdrift, leveringsevne, "
                            "personaleansvar, SLII, GROW, SBI, RACI, PDCA, A3, 5S, LOTO, APV, SAP ERP, Power BI, "
                            "Python, Claude API, NPV, IRR"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. Ansøgning side 1, "
                           "CV sider 2-4.")


if __name__ == "__main__":
    out = "/home/user/ATS-RESUME/Shahram_Ajloo_BrdrPlagborg_Produktionsleder.docx"
    print("OK", build(out))
