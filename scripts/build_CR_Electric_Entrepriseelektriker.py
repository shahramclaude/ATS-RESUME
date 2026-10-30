# -*- coding: utf-8 -*-
"""CR Electric A/S — Entrepriseelektriker (Roskilde). Ansøgning + CV i ét dokument."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ats_builder import Application

a = Application()

DATE = "30. oktober 2026"
RECIPIENT = ("CR Electric A/S · Industrivej 28 · 4000 Roskilde · att. afdelingschef Christen Jensen · "
             "tlf. 22 60 99 74 · crelectric.dk")
SUBJECT = "Ansøgning: Entrepriseelektriker — el-tekniske projekter og entrepriser, Roskilde"

OPENING = [
    "**Entreprisen afgøres på byggepladsen — mellem kl. 7 og 15.** Der trækkes kabler rigtigt første gang, "
    "tavlen dokumenteres, de øvrige fag venter ikke på os, og kunden finder ikke fejlen ved afleveringen. Den "
    "opgave søger jeg: el-tekniske projekter og entrepriser — nybyg, ombygning og renovering — hvor faglig "
    "stolthed, overblik under pres og et godt kollegaskab gør forskellen.",

    "Hos CR Electric er det ikke et ønske, men forretningen: 37 års entrepriseerfaring, mere end 8.000 typehuse "
    "og en organisation, der er vokset fra ca. 50 til ca. 300 medarbejdere, heraf ca. 35 lærlinge. Den vækst "
    "holder kun, hvis hver entreprise leveres med samme system — og det system er allerede lagt:",
]

POINTS = [
    ("El-tekniske entrepriser — nybyg, ombygning og renovering",
     "Rækkefølge frem for improvisation — 4-ugers rulleplan, kritisk vej og tydelige snitflader til de øvrige fag, "
     "så føringsveje, kabler og tavler kommer i rigtig takt. Dokumenteret: 37 CAPEX-entrepriser og 11 "
     "anlægsprojekter. Effekt: færre standsninger og aftaler, der holder."),

    ("Planlægning og koordinering på pladsen",
     "Morgenbriefing, byggemøder og én fælles tavle — hvem laver hvad i dag, hvad venter vi på, hvem eskalerer "
     "hvad — med AB 18/ABT 18, IKT og tidsplanen som arbejdsredskab. Dokumenteret: 14-mands team og 25 "
     "specialister. Effekt: alle ved, hvad der sker i morgen."),

    ("Tæt dialog, kollegaskab og oplæring",
     "Korte aftaler, skriftlig opsummering og samme information til byggeleder, kunde og kollega. Oplæring er en "
     "del af driften: følgesvend, tjekliste, egen opgave med ansvar og feedback efter SBI-modellen. "
     "Dokumenteret: 3 lærlinge i egen virksomhed. Effekt: tillid og en aflastet svend."),

    ("Kvalitet i top — og leveret til tiden",
     "KS-plan, egenkontrol og tjeklister ved hver arbejdsgang, løbende målinger og en komplet afleveringspakke "
     "ved afleveringsforretningen; FAT/SAT og IQ/OQ/PQ som disciplin. Dokumenteret: nul kritiske afvigelser. "
     "Effekt: mindre rework og dokumentation, der holder til 1- og 5-års gennemgang."),

    ("El-sikkerhed og arbejdsmiljø som vane",
     "Autorisation LV/MV/HV — og vanen med at arbejde efter den: LOTO, APV, risikovurdering ved pladsopstart, "
     "sikkerhedsrunderinger og toolbox-møder, hvor nærved-hændelser følges til dørs. Effekt: alle går hjem, som "
     "de kom."),

    ("Faglig tyngde i el-teknikken",
     "El-teknisk design og tavler, styring og fejlfinding, ABA/ABV, UPS, nød- og panikbelysning, PDS samt "
     "energi- og solcelleanlæg — kendt fra idriftsættelse og drift af kritiske anlæg. Effekt: jeg står alene med "
     "opgaven fra dag ét."),

    ("Bæredygtighed der kan måles",
     "Materialevalg med levetid for øje, energiopgørelse, affaldssortering på pladsen og dokumenteret "
     "energiforbedring — 40 % lavere energiforbrug via et struktureret PDCA-program. Effekt: ambitionerne bliver "
     "til tal i afleveringsmappen."),

    ("Digitale værktøjer og AI i det daglige",
     "Tilbudsberegning, mængdeudtræk, tidsplaner, KS-tjeklister og afleveringsdokumentation som egne værktøjer — "
     "Python, Claude API og Power BI; over 40 % effektivitetsløft. Effekt: tid på pladsen frem for på papir."),
]

MIRROR = ("**Profilen spejlet:** elektriker/elektromekaniker med dansk elautorisation LV/MV/HV "
          "(Sikkerhedsstyrelsen) og B.Tech i teknologiledelse & maskinteknik (EQF6) — faglig stolthed, "
          "selvstændig og initiativrig, overblik når det presser, ansvar for tid og kvalitet, stabil med godt humør "
          "og et stærkt kollegaskab. Dansk og engelsk, kørekort B.")

HONEST = ("**To ting, åbent sagt:** Jeg har de seneste år løftet mere planlægning, KS og ledelse end kabeltangen, "
          "fordi det var opgaven — nu søger jeg entreprisen, hvor jeg selv udfører og samtidig bærer planlægning "
          "og dokumentation. Og typehusenes tempo er ny rytme for mig; men 8.000 installationer er standarder, og "
          "standarder er min hjemmebane.")

CULTURE = ("**Hvorfor CR Electric:** Fordi kulturen matcher den måde, entrepriser lykkes på. Flad struktur og korte "
           "beslutningsveje betyder, at en elektriker på pladsen får en beslutning samme dag. Frihed under ansvar "
           "betyder, at man ikke skal spørge om lov til at gøre det rigtige. Efteruddannelse og ca. 35 lærlinge "
           "betyder, at faget føres videre. Og værdierne — \"vi holder altid, hvad vi aftaler\", kvalitet hver "
           "gang og bæredygtighed — er den kontrakt, en entrepriseelektriker underskriver hver morgen, han kører "
           "ud. Derfor låner jeg ikke kun ud af mine hænder: planlægning, tavlemøder, KS og oplæring tager jeg med, "
           "så afdelingschefen kan sende mig ud på den svære entreprise og vide, at den lander.")

PRACTICAL = ("**Praktisk:** Ansøgningen er sendt via jeres profil på Jobindex, mærket \"Entrepriseelektriker\", "
             "som I beder om — ikke på mail, og da I behandler løbende, er den sendt med det samme. Tiltrædelse "
             "hurtigst muligt; ved ansættelse afvikler jeg min egen virksomhed. Spørgsmål: afdelingschef Christen "
             "Jensen, tlf. 22 60 99 74.")

PROFILE = ("Erfaren, udførende el-tekniker og leder med 20+ års erfaring i el-tekniske entrepriser, tavler og "
           "styring, fejlfinding, idriftsættelse og teknisk drift — med dokumenteret ansvar for tid, kvalitet, "
           "sikkerhed og økonomi på byggepladsen. Autoriseret elinstallatør (LV/MV/HV, Sikkerhedsstyrelsen 2023) "
           "og B.Tech i teknologiledelse & maskinteknik (EQF6). Har ledet 37 samtidige CAPEX-entrepriser "
           "(DKK 2–10 mio.) på Novo Nordisk, 11 parallelle anlægsprojekter hos Ventek-Air, et 14-mands "
           "entrepriseteam, 25 specialister og 5 elektrikere + 3 lærlinge i egen virksomhed med fuldt P&L-ansvar. "
           "Professionel og aktiv Claude-koder: bygger egne AI-værktøjer til tilbudsberegning, mængder, "
           "tidsplaner, KS, dashboards og investeringsmodeller (Python, Claude API) med dokumenteret "
           "effektivitetsløft over 40 %. Dansk flydende, engelsk professionelt, kørekort B.")

TOOLBOX = [
    ("Personaleledelse og relationel ledelse",
     "Situationsbestemt ledelse (SLII — Hersey & Blanchard), coaching efter GROW-modellen, feedback efter "
     "SBI-modellen, MUS/GRUS og 1:1-samtaler, delegeringstrappen, psykologisk tryghed (Edmondson), "
     "kompetencematricer og individuelle udviklingsplaner, struktureret lærlinge- og svendeoplæring, "
     "onboarding med 30-60-90-dages plan, sygefraværs- og trivselssamtaler."),
    ("Drifts- og performance-ledelse",
     "Tavlemøder (huddles), visuel ledelse og KPI-tavler, Gemba-walks, fast ledelseskadence dagligt/ugentligt/"
     "månedligt, eskaleringstrappe, RACI, OEE, leveringsevne (OTD), fejlrate og rework, MTBF/MTTR, månedshjul "
     "og ledelsesrapportering."),
    ("Lean/TPS og systematisk problemløsning",
     "5S, Kaizen, PDCA, A3-problemløsning, VSM, Standard Work, SMED, TPM, Kanban og WIP-styring, Poka-Yoke, "
     "Jidoka, 5xHvorfor, Ishikawa, FMEA, Toyota Kata, Hansei og Yokoten (spredning af forbedringer)."),
    ("Projekt- og entreprisestyring",
     "4-ugers rulleplan (last planner), kritisk vej og milepæle, udbud og tilbud, mængdeberegning, AB 18/ABT 18, "
     "IKT-aftale, byggemøder og fagtavler, KS-plan, afleveringsforretning med 1- og 5-års gennemgang, "
     "underentreprenørstyring og sikkerhedsdokumentation."),
    ("Kvalitet, sikkerhed og arbejdsmiljø",
     "APV, sikkerhedsrunderinger og safety walks, registrering af nærved-hændelser, LOTO, risikovurdering, "
     "toolbox-møder, brand (ABA/ABV, nød- og panikbelysning), FAT/SAT, IQ/OQ/PQ, afvigelser/CAPA, "
     "audit readiness, GMP/FDA/EMA og IMS."),
    ("Digitalt og AI",
     "SAP ERP, CMMS, Power BI, Excel/Power Query, Python, Claude API/Claude Code, prompt- og agentdesign, "
     "automatiseret rapportering, investerings- og scenariemodeller (NPV/IRR, følsomhedsanalyse), digitale "
     "tjeklister og dokumentationsflow."),
    ("Forretning og kunder",
     "P&L- og budgetansvar, omkostningsstyring, serviceaftaler og SLA, tilbudsberegning, kundeopfølgning samt "
     "leverandør- og underentreprenørforhandling."),
]

EXPERIENCE = [
    {"job": "Ejer / teknisk direktør / autoriseret elinstallatør",
     "meta": "ELOHVAC ApS · København · maj 2023 – nu",
     "bullets": [
         "El-tekniske opgaver for erhvervskunder: installation, tavler, styring, fejlfinding og forebyggende "
         "vedligehold på el-, ventilations- og klimaanlæg — fra akutte udkald til afleveret anlæg.",
         "Entreprise- og projektstyring: tilbud og beregning, planlægning, materialestyring, underentreprenører, "
         "KS og afleveringsdokumentation med fuldt P&L-ansvar.",
         "Personaleledelse af 5 elektrikere og 3 lærlinge: daglig planlægning, 1:1 og MUS, arbejdsmiljøopfølgning "
         "og struktureret oplæring; situationsbestemt ledelse på skiftende byggepladser.",
         "AI-værktøjer (Python, Claude API): tilbudsberegning, tidsplaner, KS-tjeklister og KPI-dashboards — "
         "dokumenteret produktivitetsløft over 40 %.",
         "Sikkerhed og kvalitet: LOTO, APV og risikovurdering ved opstart på nye pladser; nul kritiske afvigelser "
         "i serviceaftalerne.",
     ]},
    {"job": "Senior idriftsættelsesingeniør / projektleder, elsystem",
     "meta": "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024",
     "bullets": [
         "37 samtidige anlægs- og CAPEX-projekter (DKK 2–10 mio. pr. stk.): fremdrift, økonomi, risici og "
         "ressourcer på tværs af engineering, indkøb og anlæg.",
         "Tværfaglig teamledelse af 25 højt specialiserede medarbejdere; idriftsættelse og kvalitetssikring "
         "(FAT/SAT, IQ/OQ/PQ) under GMP/FDA/EMA — nul kritiske afvigelser ved aflevering.",
         "El-tekniske anlæg: tavler og styring, UPS, nød- og panikbelysning, ABA/ABV og PDS; fejlfinding og "
         "systematisk rodårsagsanalyse (A3, 5xHvorfor, Ishikawa).",
         "40 % reduktion af energiomkostninger via struktureret PDCA-program; SAP ERP til økonomi-, aktiv- og "
         "omkostningsstyring samt månedsrapportering til ledelse og bygherre.",
     ]},
    {"job": "Projekt- og værkstedsleder, ventilation & klima",
     "meta": "Ventek-Air · København · jan. 2022 – nov. 2022",
     "bullets": [
         "11 samtidige anlægsprojekter (DKK 2–10 mio.) fra specifikation gennem udførelse til formel aflevering; "
         "daglig ledelse af 14-mands team med kapacitets- og fremdriftsstyring.",
         "Udbud og tilbud, underentreprenører, aftalegrundlag, sikkerhedsdokumentation og afleveringspakker.",
         "Daglige tavlemøder og flaskehalsanalyser; standardiserede arbejdsgange med markant løft i "
         "leveringsevne.",
     ]},
    {"job": "Vedligeholdelses- og driftsleder / værkstedstekniker",
     "meta": "Biofos (renseanlægget Lynetten) · København · aug. 2017 – jan. 2022",
     "bullets": [
         "Kritisk el- og mekanisk drift: pumper, HVAC, højspændingstavler og SCADA — oppetid, forebyggende "
         "vedligehold og akut fejlfinding 24/7.",
         "5S, Standard Work og PDCA på værksted og lager; reservedelsflow og lagerstyring til kritisk drift.",
         "Skifteholdsdrift med sikkerhedsdisciplin: LOTO, risikovurdering, APV og systematisk håndtering af "
         "nærved-hændelser.",
     ]},
    {"job": "Elektromekaniker / produktionsteamleder",
     "meta": "ARJ Engineering · Teheran · dec. 2003 – mar. 2010",
     "bullets": [
         "Ledelse af 12 mekanikere og teknikere i maskinværksted: vagtplanlægning, materialestyring og "
         "målstyring.",
         "Fejldiagnose og reparation af industrielle el- og mekaniske anlæg; struktureret rodårsagsanalyse og "
         "korrigerende handlinger.",
     ]},
]

EDUCATION = [
    "Dansk elinstallatørs-/elektrikerautorisation LV/MV/HV — Sikkerhedsstyrelsen, maj 2023.",
    "B.Tech (EQF6), teknologiledelse & maskinteknik — Copenhagen School of Marine Engineering & Technology "
    "Management, 2017–2022 · GPA 7,6/12.",
    "El- og maskinteknisk design, elteknik (EQF6) — Tehran Technical University, 2000–2003.",
    "HF (matematik/fysik) — VUC, 2012–2017.",
    "Køleteknik & klimaanlæg (AMU) — Mercantec, 2021.",
    "STCW: vagt i maskinrummet (A-III/1), udpegede sikkerhedsopgaver (VI/6), skibssikkerhedsofficer (VI/5), "
    "sikkerhedsbevidsthed (VI/6-1), tankskib (V/1-1, V/1-2) — Søfartsstyrelsen, 2021–2023.",
    "Lean-/forbedringspraksis: 5S, PDCA, VSM, A3 og Kaizen.",
    "Sprog: dansk (modersmål), engelsk (professionelt), persisk/farsi (modersmål) · Kørekort B.",
]

CORE = [
    "El-tekniske entrepriser: nybyg, ombygning og renovering — installation, tavler, styring, kabeltræk og "
    "føringsveje.",
    "Fejlfinding og idriftsættelse: FAT/SAT, målinger, dokumentation, aflevering og 1-/5-års gennemgang.",
    "Planlægning og koordinering på byggepladsen: 4-ugers rulleplan, byggemøder, tavlemøder og snitflader til "
    "øvrige fag.",
    "Kvalitet og sikkerhed: KS-plan, egenkontrol, APV, LOTO, nærved-hændelser, AB 18/ABT 18 og IKT.",
    "El-teknisk bredde: ABA/ABV, UPS, nød- og panikbelysning, PDS/adgangskontrol, solcelle- og energianlæg "
    "samt ventilation og klima.",
    "Samarbejde og kommunikation: god kommunikation og stærke relationer til byggeleder, øvrige fag og "
    "kunde — fælles tavle, skriftlig opsummering og teamånd i hverdagen.",
    "AI og digitalisering: Python/Claude API til tilbud, planlægning, KS og rapportering; SAP, CMMS og "
    "Power BI.",
]

KEYWORDS = (
    "entrepriseelektriker · el-tekniske projekter · entrepriser · ombygning · renovering · nybyg · byggeplads · "
    "planlægning og koordinering · el-installation · el-teknik · tavler · styring · fejlfinding · idriftsættelse · "
    "aflevering · kvalitetssikring · KS · dokumentation · el-sikkerhed · LOTO · APV · arbejdsmiljø · ABA · ABV · "
    "UPS · nød- og panikbelysning · PDS · adgangskontrol · solcelleanlæg · fiber · kabeltræk · føringsveje · "
    "service · typehuse · underentreprenører · AB 18 · ABT 18 · IKT · Lean · 5S · Kaizen · PDCA · A3 · VSM · "
    "Gemba · tavlemøder · situationsbestemt ledelse · SLII · GROW · SBI · MUS · 1:1 · kompetenceudvikling · "
    "lærlinge · psykologisk tryghed · KPI · OEE · OTD · Power BI · SAP · CMMS · Python · Claude API · AI · "
    "selvstændig · initiativrig · overblik · faglig stolthed · godt humør · stabil · team · teamånd · "
    "samarbejde · kommunikation · relationer · medarbejdertrivsel · trivsel · bæredygtighed · "
    "kørekort B · dansk · engelsk"
)

a.cover_letter(
    date=DATE, recipient=RECIPIENT, subject=SUBJECT, opening=OPENING, points=POINTS,
    mirror=MIRROR, honest=HONEST, culture=CULTURE, practical=PRACTICAL,
    signature="Shahram Ajloo",
    contact="+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Søborg, Danmark",
)

a.resume(
    name="Shahram Ajloo",
    title="Entrepriseelektriker · autoriseret elinstallatør (LV/MV/HV) · el-teknisk projekt- og driftsleder",
    contact="+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Søborg, Danmark — Roskilde",
    profile=PROFILE, toolbox=TOOLBOX,
    toolbox_title="Ledelses- og faglige værktøjer — alle i praktisk brug",
    experience=EXPERIENCE, education=EDUCATION, core=CORE,
    core_title="Kernekompetencer til entrepriseafdelingen",
    keywords=KEYWORDS,
)

out = "/home/user/Claude/Shahram_Ajloo_CR_Electric_Entrepriseelektriker.docx"
a.save(out,
       title="Ansøgning og CV — Entrepriseelektriker, CR Electric A/S",
       subject="Entrepriseelektriker · el-tekniske projekter og entrepriser · Roskilde",
       keywords=("entrepriseelektriker, el-teknik, entrepriser, byggeplads, kvalitetssikring, "
                 "el-sikkerhed, tavler, idriftsættelse, Lean, 5S, PDCA, situationsbestemt ledelse, "
                 "Python, Claude API"),
       comments="Ansøgning + CV i ét dokument. ATS-optimeret, dansk.")
print("OK", out)
