# -*- coding: utf-8 -*-
"""
Technical Project Manager + fagligt ansvarlig for el-installationer (dansk JD).
Bygget i designet fra master-CV'erne. Sprog: dansk (JD-sprog).
Ansøgning + CV i ét dokument.

Bemærk: opslaget navngiver ikke virksomheden, og ansøgningen er derfor adresseret
neutralt. Sæt VIRKSOMHED/MODTAGER ind, når navnet kendes.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Technical Project Manager · Fagligt ansvarlig for el-installationer"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Søborg")

DATE = "30. oktober 2026"
RECIPIENT = ("Til ansættelsesudvalget · Technical Project Manager / fagligt ansvarlig el · "
             "København")
SUBJECT = "Ansøgning: Technical Project Manager med fagligt ansvar for el-installationer"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Et projekt lander på bordet. Kravene er fastlagt, de første tekniske afklaringer er lavet, flere "
    "afdelinger skal ind over, leverandørerne skal koordineres, og dokumentationen skal i hus — og de "
    "el-tekniske løsninger skal være skarpe, lovlige og sikre. Det er den rolle, jeg har stået i de sidste "
    "tyve år: som indehaver af en autoriseret el-virksomhed, som projekt- og commissioningleder på 37 "
    "samtidige anlægsprojekter og som den, der har skrevet under på dokumentationen til myndighederne.",
    "Jeg er autoriseret el-installatør (LV/MV/HV) og kan godkendes som fagligt ansvarlig. Jeg har drevet "
    "egen virksomhed med autorisation og egenkontrol, og jeg har leveret FAT/SAT, spændingssætning og "
    "afleveringsforretning på anlæg, hvor en fejl ikke er en gene men en fare. Derfor er svaret her ikke "
    "en personlig historie — det er, hvad jeg vil gøre i rollen, og hvad jeg vil forandre.",
]

# De fire spørgsmål i opslaget besvares i samme rækkefølge
Q1 = ("Sådan vil jeg udfylde rollen som Technical Project Manager og fagligt ansvarlig",
      [("Projektet fra A til Z:",
        "krav, afklaringer, tidsplan, økonomi og risiko — 37 samtidige anlægsprojekter (2–10 mio. kr.) med "
        "rapportering til ledelse og kunde, fra første snit i tegningen til kvitteret aflevering."),
       ("Det faglige ansvar:",
        "love, standarder og SKS efterlevet på hver eneste installation — kredsskemaer, el-dokumentation og "
        "myndighedsgodkendelser afleveret, så de holder ved eftersyn. Nul kritiske afvigelser ved aflevering."),
       ("Sparring og rådgivning:",
        "koblingsanlæg, elforsyning, tavler og fejlsøgning — jeg taler med netselskab, leverandør og kunde i "
        "samme møde og sørger for, at beslutningen bliver skrevet ned, før mødet slutter."),
       ("Test og idriftsættelse:",
        "FAT, SAT, funktionstest, spændingssætning og afleveringsforretning med mangelgennemgang — planlagt "
        "før arbejdet starter, ikke opdaget til sidst."),
       ("Indkøb og økonomi:",
        "el-komponenter, leverancer og underleverandører styret mod budget og tidsplan; afvigelser meldt ud "
        "samme uge, som de opstår.")])

Q2 = ("Hvad der motiverer mig og giver mig energi",
      "Det øjeblik hvor dokumentationen er afleveret, anlægget er sat under spænding, kunden har kvitteret — og "
      "teamet gik hjem i samme stand, som de kom, uden skader og uden at nogen har \"løst\" noget på egen hånd. "
      "Jeg får energi af at være den, der skaber overblik, når ti mennesker trækker i hver sin retning, og af at "
      "se en ung installatør løse en opgave, han ikke turde røre ved for et år siden.")

Q3 = ("Hvad jeg har brug for fra kolleger, leder og organisation",
      "Et tydeligt mandat — især hvor det faglige ansvar begynder og slutter, og hvem der må sige stop og blive "
      "hørt. Adgang til tegnings- og dokumentationsgrundlaget fra dag ét. En leder, der bakker op, når sikkerhed "
      "koster tid, og kolleger der siger til, når de ser noget. Til gengæld lover jeg, at beslutninger bliver "
      "truffet og kommunikeret, ikke udskudt — og at jeg tager ansvar for dem bagefter.")

Q4 = ("De første 12–24 måneder: hvad jeg vil bringe i spil",
      [("Én dokumentationsstandard",
        "fælles kredsskema- og egenkontrolskabeloner og en fast afleveringsmappe, så hver installation "
        "dokumenteres ens — og autorisationen er let at vise ved tilsyn."),
       ("Én projektmodel",
        "gate-review ved afsluttet projektering, indkøb og FAT, med tjeklister for SAT, idriftsættelse og "
        "aflevering; samme model på alle projekter, så ingen starter forfra hver gang."),
       ("Leverandør- og komponentpanel",
        "færre og bedre aftaler på tavler, komponenter og underleverandører, så pris, leveringstid og teknisk "
        "dokumentation er kendt, før projektet begynder."),
       ("Data og AI i leverancen",
        "Power BI-portefølje på økonomi, fremdrift og afvigelser — og Claude/Python til dokumentations- og "
        "tilbudsarbejdet, så ingeniørtiden går til teknik i stedet for copy-paste.")])

CLOSING = ("I skriver, at I ikke er interesserede i mange sider om, hvem jeg er. Det her er derfor, hvad jeg vil "
           "gøre — resten står i CV'et. Jeg kommer gerne forbi og gennemgår et af jeres igangværende projekter, "
           "hvis I vil se, hvordan jeg tænker, når det er virkeligt.")

# ------------------------------------------------------------------ CV
PROFILE = ("El-installatør og projektleder med mere end 20 års erfaring fra reguleret produktion, tekniske anlæg "
           "og el-teknisk drift — og med det faglige ansvar, som rollen kræver: autoriseret el-installatør "
           "(LV/MV/HV) med egen autoriseret virksomhed, egenkontrol og dokumentation, der er godkendt af "
           "myndighederne. Har ledet 37 samtidige anlægsprojekter (2–10 mio. kr.) med økonomi, tid, risiko, "
           "indkøb, FAT/SAT og idriftsættelse, og har drevet 24/7-forsyningsanlæg med koblingsanlæg, "
           "højspænding og SCADA. Arbejder struktureret med standarder, tjeklister og sporbar dokumentation — og "
           "bygger selv de data- og AI-værktøjer, der gør fremdrift og afvigelser synlige. B.Tech i Technology "
           "Management & Mechanical Engineering (EQF 6); dansk og engelsk på professionelt niveau.")

PRACTICE = [
    ("Fagligt ansvar, dokumenteret",
     "Egen autoriseret el-virksomhed med egenkontrol, kredsskemaer og afleveringsdokumentation; "
     "risikovurdering ved hvert nyt anlæg, LOTO og sikringsprocedurer, og nul kritiske afvigelser i "
     "serviceporteføljen. På Novo Nordisk: nul kritiske afvigelser ved aflevering på 37 projekter."),

    ("Projektledelse fra afklaring til drift",
     "37 samtidige anlægsprojekter (2–10 mio. kr.): kravafklaring, tidsplan, økonomi, risiko, "
     "interessentstyring og månedlig rapportering til ledelse og kunde — på tværs af teknik, indkøb og "
     "driftsorganisation."),

    ("El-teknisk tyngde",
     "Koblingsanlæg, tavler, elforsyning, højspænding, motorer, pumper, HVAC og SCADA; fejlsøgning under "
     "driftspres og valg af komponenter med dokumenteret grundlag. Daglig kontakt til netselskab, leverandører "
     "og rådgivere."),

    ("Test, idriftsættelse og aflevering",
     "FAT og SAT, IQ/OQ/PQ, funktionstest, spændingssætning og afleveringsforretning med mangelgennemgang — "
     "planlagt og bemandet, så driftsstart er en begivenhed og ikke en overraskelse."),

    ("Økonomi, indkøb og underleverandører",
     "Budgetopfølgning, ressourcestyring og indkøb af el-komponenter og leverancer; underleverandører styret på "
     "kontrakt, sikkerhedsdokumentation og fremdrift — i egen virksomhed med fuldt P&L-ansvar."),

    ("Data, dashboards og AI-værktøjer",
     "SAP ERP og CMMS som kilde til sandheden, Power BI til portefølje- og økonomiopfølgning, og Python/Claude "
     "til automatiseret rapportering, tjeklister og dokumentationsflow — dokumenteret produktivitetsløft over "
     "40 % i planlægning og rapportering."),
]

FIRST90 = [
    ("Dag 1–14",
     "Læser autorisationen igennem: hvilke installationer dækker den, hvem har været fagligt ansvarlig hidtil, "
     "hvor er egenkontrollen og de sidste afleveringer. Går de igangværende projekter igennem ét for ét — "
     "status, åbne afvigelser, dokumentation, næste milepæl."),
    ("Dag 15–45",
     "Én projektmodel og ét afleveringsformat på plads, i brug på mindst to kørende projekter. Fast ugentlig "
     "porteføljeoversigt for økonomi, fremdrift og afvigelser. Tydelig rollebeskrivelse af det faglige ansvar, "
     "godkendelser og stop-ret, aftalt med ledelsen."),
    ("Dag 46–90",
     "Leverandørpanel og komponentaftaler forberedt; tjeklister for FAT, SAT og idriftsættelse i brug; "
     "kompetenceplan for el-medarbejdere, så autorisationen hviler på flere skuldre end mine."),
    ("Måned 6–24",
     "Dokumentation og myndighedsgodkendelser går gennem en fast proces, uanset hvem der er projektleder; "
     "leverancen måles på afvigelser, gennemløbstid og økonomi — og forbedringerne bliver i organisationen, "
     "fordi de er skrevet ned og brugt, ikke bare præsenteret."),
]

MODELS = [
    ("Fagligt ansvar & autorisation",
     "El-installatørautorisation LV/MV/HV, egenkontrol, kredsskemaer og el-dokumentation, "
     "myndighedsgodkendelser, SKS og gældende standarder (DS/HD 60364, EN 61439), tilsyn og "
     "dokumentationsspor"),
    ("Projektledelse",
     "Faseopdelt projektmodel med gate-review, tidsplan og kritisk vej, risikostyring, interessentanalyse, "
     "RACI, mødestruktur og beslutningslog, budget og ressourcestyring, månedlig rapportering"),
    ("El-teknisk projektering",
     "Kredsskemaer og tavletegninger, komponentvalg og beregninger, koblingsanlæg, elforsyning og "
     "transformerstationer, selektivitet og beskyttelse, dokumenteret grundlag for ændringer"),
    ("Test & idriftsættelse",
     "FAT (fabrikstest) og SAT (site test), IQ/OQ/PQ, funktionstest og spændingssætning, "
     "afleveringsforretning med mangelgennemgang, driftsinstruktion og oplæring af driftspersonale"),
    ("Indkøb & leverandører",
     "Indkøb af el-komponenter og leverancer, underleverandørstyring på kontrakt og sikkerhedsdokumentation, "
     "leveringsopfølgning, prissammenligning og aftaler"),
    ("Sikkerhed & arbejdsmiljø",
     "APV og risikovurdering, LOTO og sikringsprocedurer, arbejdstilladelser, near-miss-opfølgning, "
     "stop-ret, entreprenørsikkerhed på aktive anlæg"),
    ("Data, ERP & AI",
     "SAP ERP og CMMS, Power BI-porteføljer, Excel/Power Query, Python og Claude API til automatiseret "
     "rapportering, tjeklister og dokumentation; investeringsmodeller (NPV, IRR)" ),
    ("Økonomi & styring",
     "Budgetopfølgning og prognose, cost-to-complete, ressourceplanlægning, produktivitetsopgørelse, "
     "tilbud og serviceaftaler (SLA)"),
]

ACHIEVEMENTS = [
    ("Nul kritiske afvigelser ved aflevering",
     "på 37 samtidige anlægsprojekter (2–10 mio. kr.) under GMP/FDA/EMA-krav."),
    ("37 projekter leveret samtidig",
     "med økonomi, tid, risiko og månedlig rapportering — uden at driften standsede."),
    ("+40 % produktivitet",
     "i en teknisk serviceforretning gennem dataunderstøttet planlægning og standardarbejde."),
    ("−40 % energikost",
     "i reguleret produktion via struktureret PDCA, A3 og standardiserede løsninger."),
    ("Autoriseret virksomhed bygget fra bunden",
     "med egenkontrol, dokumentationssystem og 5 elektrikere + 3 lærlinge."),
]


EL_TEKNIK = [
    ("Forsyning og transformerstationer",
     "elforsyning, koblingsanlæg og transformerstationer: valg af komponenter og beskyttelse, selektivitet, "
     "kortslutningsberegning, dokumenteret grundlag for hver ændring — og dialog med netselskabet, når "
     "tilslutningen skal godkendes."),
    ("Tavler og installationer",
     "lavspænding, mellemspænding og højspænding (LV/MV/HV) i samme miljø; tavlebyggeri efter EN 61439 og "
     "installationer "
     "efter DS/HD 60364; "
     "kredsskemaer og el-dokumentation, der kan læses af den, der skal fejlfinde om fem år."),
    ("Myndighed og autorisation",
     "ansøgninger og godkendelser, tilsyn og eftersyn; dokumentation afleveret samlet, så den kan fremlægges "
     "uden at nogen skal lede efter den."),
    ("Test og måling",
     "isolationstest, kontinuitet, beskyttelsesleder- og RCD-test, spændingssætning og funktionstest — "
     "protokolleret, og med afvigelser lukket før overtagelse, ikke efter."),
    ("Drift og fejlsøgning under pres",
     "24/7-anlæg med pumper, motorer, HVAC, koblingsanlæg og SCADA: fejl findes systematisk, mens driften "
     "kører, og udbedres med mindst mulig nedetid."),
]

AUTORISATION = [
    ("Egenkontrol",
     "skriftlig egenkontrolprocedure, der følges på hvert anlæg, og som kan vise myndigheden, hvordan vi "
     "kontrollerer os selv — ikke bare at vi gør det."),
    ("Kompetencekort",
     "hvem der må hvad, og hvem der har været på hvilke kurser; autorisationen skal ikke hænge på én person, "
     "men på en organisation."),
    ("Stop-ret og eskalering",
     "alle kan stoppe arbejdet, når sikkerheden er i spil; beslutningen bliver dokumenteret, og der bliver "
     "fulgt op — også når det koster tid."),
    ("Dokumentationsspor",
     "én mappe pr. anlæg med kredsskemaer, målprotokoller, afleveringsforretning og myndighedsgodkendelse; "
     "ved tilsyn eller nyt projekt starter ingen forfra."),
]

EXPERIENCE = [
    ("Indehaver / Teknisk direktør / Autoriseret el-installatør",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg i Storkøbenhavn · fuldt P&L, tilbud og leverandøraftaler",
     [("Fagligt ansvar",
       "autorisation, egenkontrol, kredsskemaer og dokumentation for alle installationer; risikovurdering, "
       "LOTO og sikringsprocedurer ved hvert nyt anlæg."),
      ("Drift og levering",
       "daglig planlægning, kapacitet mod ordrebogen, materiale- og reservedelsflow, kvalitetskontrol, "
       "leveringssikkerhed og omkostning — gennemgået hver morgen mod standardarbejde, 5S og KPI'er."),
      ("Digitalt fundament, bygget selv",
       "ERP-baseret ordre- og reservedelsstyring, Power BI-dashboards og Python/Claude-værktøjer til "
       "planlægning, tilbud, tjeklister og rapportering; produktivitetsløft over 40 %."),
      ("Sikkerhed og compliance",
       "risikovurdering på hvert nyt anlæg, near-miss-håndtering og dokumenterede serviceregistreringer; nul "
       "kritiske afvigelser i porteføljen.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister inden for teknik, indkøb og drift · "
     "GMP/FDA/EMA",
     [("Porteføljeleverance",
       "tidsplan, økonomi, risiko, ressourcer og månedlig rapportering til ledelse og kunde på tværs af "
       "teknik, indkøb og driftsorganisation."),
      ("Tværfaglig ledelse af 25 specialister",
       "commissioning og kvalificering (FAT/SAT, IQ/OQ/PQ, valideringsdokumentation) med afvigelseshåndtering, "
       "CAPA og change control i et levende revisionsspor — nul kritiske fund ved aflevering."),
      ("Energiprogram",
       "−40 % energikost gennem struktureret PDCA, A3-problemløsning og standardiseret arbejde; SAP ERP til "
       "omkostning, anlæg og ordrestyring."),
      ("Anlæg i drift",
       "dagligt arbejde i renrum, lager og produktion: arbejdstilladelser, LOTO, entreprenørkontrol, "
       "afklædningsdisciplin og grænseflader til Kvalitet, Vedligehold og Produktion.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.) · specifikation til "
     "formel aflevering",
     [("Daglig ledelse og flow",
       "kapacitetsplanlægning og flowstyring over 11 samtidige projekter, fra specifikation til formel "
       "aflevering."),
      ("Daglige tavlemøder og flaskehalsanalyse",
       "standardiseret arbejde ved hver station med mærkbar fremgang i leveringsperformance og "
       "førstegangskvalitet."),
      ("Leverandører og underleverandører",
       "kontraktgrundlag, sikkerhedsdokumentation og afleveringspakker.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · drifts- og "
     "vedligeholdelsesbudgetter i SAP",
     [("24/7 kritisk drift",
       "oppetid, forebyggende vedligehold og hurtig fejlfinding med nul tolerance for uplanlagte stop."),
      ("Struktureret vedligehold",
       "standardarbejde, 5S, PDCA-baseret vedligeholdsplan, A3-root cause-analyse, reservedelsflow og kritiske "
       "lagre."),
      ("Skiftdrift og sikkerhedsdisciplin",
       "LOTO, risikovurdering, near-miss-rapportering og værktøjsmøder; KPI'er og driftsbudgetter i SAP ERP.")]),

    ("Elektromekaniker / Produktionsteamleder",
     "ARJ Engineering · Teheran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · skiftplanlægning, materialestyring og lager",
     [("Produktionsteam",
       "skiftplanlægning, materialestyring, lager og linjesideforsyning, målopfølgning og situationel coaching."),
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
    ("Lean — værdistrømsanalyse, standardarbejde, 5S, A3 og Kaizen",
     "Anvendt i drift · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og anlægsprojekter · 2017 – nu"),
    ("Køle- og HVAC-teknik (AMU)",
     "Mercantec · mar. 2021"),
    ("STCW — maskinrumsvagt (A-III/1), skibssikkerhedsofficer (VI/5), tankbasisk (V/1-1, V/1-2)",
     "Søfartsstyrelsen · 2021 – 2023"),
    ("Arbejdsmiljø §16 og sikkerhedsbevidsthed (VI/6-1)",
     "Søfartsstyrelsen · maj 2021"),
]

LANGUAGES = "Dansk (modersmål) · Engelsk (professionelt, skriftligt og mundtligt) · Persisk/farsi · Kørekort B"

REFERENCES = "Tidligere ledere hos Novo Nordisk A/S (Kalundborg) og Biofos (Lynetten) — oplyses ved henvendelse."

KEYWORDS = (
    "Technical Project Manager · Projektleder · Projektledelse · Fagligt ansvarlig · El-fagligt ansvarlig · "
    "El-installatør · El-teknisk · El-teknik · Autorisation · Autoriseret · SKS · Sikkerhedskrav · Kredsskema · "
    "El-dokumentation · Dokumentation · Myndighedsgodkendelser · Elforsyning · Transformerstation · "
    "Koblingsanlæg · Højspænding · Lavspænding · Tavler · FAT · SAT · Test · Idriftsættelse · Spændingssætning · "
    "Afleveringsforretning · Mangelgennemgang · Projektindkøb · Indkøb · Leverandører · Underleverandører · "
    "Koordinering · Budgetopfølgning · Økonomi · Ressourcestyring · Rapportering · Risikostyring · Tidsplan · "
    "APV · LOTO · Sikkerhed · Arbejdsmiljø · Kvalitet · Egenkontrol · DS/HD 60364 · EN 61439 · SAP · ERP · "
    "Power BI · Excel · Python · Claude · AI · Interessentledelse · Tværfagligt samarbejde · Rådgivning · "
    "Teknisk sparring · Produktion · Industri · Forsyningsanlæg · SCADA · Maskinmester · El-ingeniør · "
    "Dansk · Engelsk"
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

    def q_label(text):
        lp = m._p(spacing_after=20, spacing_before=60, line=260, justify=False, keep_next=True)
        m._run(lp, text, bold=True, color="002B5C")

    q_label(Q1[0])
    for label, body in Q1[1]:
        m.bullet(label, body, after=30)

    q_label(Q2[0])
    m.para(Q2[1], after=80)

    q_label(Q3[0])
    m.para(Q3[1], after=80)

    q_label(Q4[0])
    for label, body in Q4[1]:
        m.bullet(label, body, after=30)

    m.para(CLOSING, after=80)

    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "FAGLIG PROFIL")
    m.para(PROFILE, after=80)

    m.section("FAGLIGT ANSVAR & PROJEKTLEDELSE — BEVIS, IKKE PÅSTANDE")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("FAGLIGE METODER & VÆRKTØJER — ANVENDT I PRAKSIS",
                   ("Område", "Værktøjer og metoder"), MODELS)

    m.section("UDVALGTE RESULTATER")
    for label, body in ACHIEVEMENTS:
        m.bullet(label, body, after=30)

    m.section("EL-TEKNISK ERFARING I DETALJEN")
    for label, body in EL_TEKNIK:
        m.bullet(label, body, after=30)

    m.section("SÅDAN SIKRER JEG DEN FORTSATTE AUTORISATION")
    for label, body in AUTORISATION:
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

    m.models_table("FØRSTE 90 DAGE — SYSTEMET JEG STILLER OP",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    return m.save(path,
                  title="Ansøgning og CV — Technical Project Manager / fagligt ansvarlig for el-installationer",
                  subject="El-teknisk projektledelse · autoriseret el-installatør LV/MV/HV · FAT/SAT og idriftsættelse",
                  keywords=("technical project manager, projektleder, fagligt ansvarlig, el-installatør, "
                            "autorisation, SKS, kredsskema, el-dokumentation, FAT, SAT, idriftsættelse, "
                            "koblingsanlæg, elforsyning, budget, SAP, Power BI"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1, CV side 2-4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_TechnicalProjectManager_ElFagligtAnsvarlig.docx")
    print("OK", build(out))
