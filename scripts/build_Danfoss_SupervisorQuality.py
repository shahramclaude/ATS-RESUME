# -*- coding: utf-8 -*-
"""Supervisor, Quality — Danfoss, Orbital & Gear Solutions (OGS), Nordborg (dansk opslag).

Dansk opslag -> dansk dokument, 4 sider: brev side 1, CV side 2, uddannelse + 90 dage +
metodeafsnit + "Hvor jeg ville starte" side 3, kravmatrix side 4. Format per master/README.md:
brev -> CV -> uddannelse/90 dage -> matrix. Opslagets anvisninger om ansøgningsform følges ikke.

STILVALG (master/STILREGISTER.md; godkendt af scripts/style_guard.py, 3/3 skift mod #212):
  register      = TEKNISK-DRIFTSNÆR — drift, klokken, tavlen, opfølgning, daglig performance.
                  Sidst #207/#208.
  åbningsgreb   = J (BREVET: deres egen sætning besvares) — "Vil du skabe resultater gennem
                  mennesker?" Sidst #203.
  struktur      = SNITFLADERNE — rollens fire grænseflader: produktion · engineering ·
                  procurement og leverandører · økonomi og ledelse (Cost of Quality). Sidst #202.
  kadence       = korte, konstaterende sætninger hele vejen igennem; tavlen og tallet som
                  omdrejningspunkt, ingen tillægsord om personen.

KULTURSYNKRONISERING (policy 04.11.2026), kilder i master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md §184:
  Danfoss, OGS (Orbital & Gear Solutions), Nordborg: produktion af **styreenheder og
  hydraulikmotorer** til kunder over hele verden; team på ca. **22 kvalitetsoperatører**; mål
  følges på **SQDCI** via **daglige tavlemøder** og Factory Board; bred kontaktoverflade mod
  produktion, engineering, procurement og leverandører; Cost of Quality som fagligt fundament.
  Søsteropslag i samme forretningsområde beskriver kulturen som "et stærkt fællesskab og en
  ambition om hele tiden at blive bedre – sammen" (Senior Operations Manager Tina Munk Düwel),
  med SQDC på tavlen. Opslaget selv: intern udvikling, mentoring, work-life balance, inklusion.

Ingen opdigtede fakta. Dokumenteret grundlag: 12 mekanikere og teknikere (ARJ 2003–2010), 14
medarbejdere og 11 entrepriser (Ventek-Air 2022), 5 elektrikere + 3 lærlinge med fuldt P&L
(ELOHVAC 2023–), 37 CAPEX-projekter med 25 specialister og nul kritiske fund under GMP/FDA/EMA
(Novo Nordisk 2022–2024), 24/7-drift med SRO/SCADA, 5S, APV og LOTO (Biofos 2017–2022);
PDCA med 40 % lavere energiforbrug og 40 % højere produktivitet; SAP; dansk modersmål og
professionelt engelsk.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Supervisor, Quality · kvalitet, tavle og daglig performance'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4. november 2026")
    m.meta("Supervisor, Quality · Orbital & Gear Solutions · Danfoss, Nordborg")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Supervisor, Quality", bold=True, color='1A1A1A')
    m.para("Kære Quality-ledelsen i OGS,", after=60)

    # ---------------------------------------------------------------- side 1
    m.para("**\"Vil du skabe resultater gennem mennesker?\"** Ja. Men resultaterne kommer ikke gennem "
           "mennesker alene. De kommer gennem mennesker, der ved, hvad der er vigtigst i dag, som har "
           "lov til at stoppe linjen, når noget ikke er i orden, og som bliver spurgt, før "
           "beslutningen falder. Det er den slags ledelse, jeg har udøvet i tolv år i produktion og "
           "værksted — og i de sidste tre år med mit eget navn på regnskabet, hvor dårlig kvalitet "
           "ikke var en KPI, men en udgift, jeg selv betalte.", after=80)

    m.para("**En styreenhed eller en hydraulikmotor, der går i stykker ude hos kunden, bliver ikke "
           "en sag i Nordborg — den bliver en garanti, en stoppet maskine og et spørgsmål om, hvorfor "
           "vi ikke så det, før den blev sendt.** Derfor er kvalitetsarbejdet i produktionen ikke en "
           "kontrol til sidst. Det er en række beslutninger, der bliver taget ved emnet, ved "
           "opspændingen og ved tavlen, længe før varen bliver pakket. Det er den slags arbejde, jeg "
           "har lyst til at lede: tæt på **produktionen**, med tal der kan ses, og med et team der "
           "må sige til.", after=80)

    m.para("**Snitfladen mod produktionen: hvem ejer stoppet?** Kvalitetsoperatøren ser fejlen "
           "først, og hvis hun ikke må stoppe linjen, bliver hun en, der registrerer den bagefter. Så "
           "første regel er, at stopretten ligger hos den, der ser fejlen, og at beslutningen bliver "
           "taget inden for få minutter — ikke til næste møde. Anden regel er, at den, der stopper, "
           "ikke bliver målt på stilstand, men på hvor hurtigt fejlen bliver afgrænset: hvilke emner, "
           "hvilke serier, hvilke kunder. Jeg har kørt **produktion** med den model i et værksted med "
           "12 teknikere og i en virksomhed med 14 mand og 11 samtidige opgaver.", after=80)

    m.para("**Snitfladen mod engineering: hvad kan maskinen faktisk lave?** En tolerance, der er "
           "skrevet på en tegning, er en aftale — ikke en mulighed. Når **engineering** ændrer en "
           "specifikation, skal kvalitetsfunktionen have den, før den rammer gulvet, ellers bliver "
           "første batch til forsøgsproduktion med kundens penge. Derfor sidder kvalitet med i "
           "ændringsvurderingen, og derfor bliver en ændring prøvet af på et afgrænset antal emner "
           "med et måltal, før den ruller ud. Det er den samme disciplin som ændringsstyring under "
           "GMP, hvor en ændring uden vurdering er en afvigelse, der venter på at ske.", after=80)

    m.para("**Snitfladen mod procurement og leverandører: reklamationen skal hjem til kilden.** "
           "**Leverandørkvalitet** er ikke en modtagelseskontrol, der sorterer det dårlige fra. Det "
           "er en aftale om, hvad der bliver målt hos leverandøren, hvordan en **reklamation** bliver "
           "behandlet, og hvornår en **CAPA** er lukket på **rodårsag** og ikke på høflighed. I eget "
           "selskab har jeg købt, kontrolleret og afvist emner og siddet med regningen, når "
           "**procurement** valgte på pris alene — og jeg har lært at tage den samtale, før ordren "
           "bliver sendt, i stedet for efter.", after=80)

    m.para("**Snitfladen mod økonomien: Cost of Quality er fire tal, ikke en holdning.** Scrap, "
           "omarbejde, garanti og kontrol koster hver for sig, og de bliver næsten altid betalt af "
           "forskellige budgetter, så ingen ser summen. Jeg har set den sum på mit eget regnskab: en "
           "time omarbejde i produktionen er dyrere end den time, der ville have forebygget den. "
           "Derfor følger jeg **Cost of Quality** på samme **tavlemøde** som **SQDCI**, og derfor "
           "bliver hver **forebyggende** handling vurderet på, om den flytter et af de fire tal.",
           after=80)

    m.para("**Teamet og hverdagen.** 22 **kvalitetsoperatører** er ikke et team, fordi de står i "
           "samme afdeling. Det bliver et team, når de ved, hvad der bliver målt, når **coaching** "
           "sker ved emnet og ikke i et mødelokale, og når **udvikling** er en plan pr. person og "
           "ikke et kursuskatalog. Jeg har oplært tre lærlinge med egen plan, kørt **MUS** hvert år "
           "og bygget **kompetence**matrix, så det var tydeligt, hvem der kunne hvad — og hvem der "
           "skulle have noget nyt. **Sikkerhed** og **trivsel** kommer før performance; det er ikke "
           "bløde ord, det er forudsætningen for, at nogen gider sige, at der er et problem.",
           after=80)

    m.para("**Praktisk.** Jeg bor i Måløv. **Nordborg** er en flytning, ikke en pendling, og det er "
           "jeg indstillet på. **Dansk** som modersmål og **engelsk** på professionelt niveau — "
           "skriftligt og mundtligt, også i møder med leverandører og kolleger i udlandet. "
           "**Kørekort B.** Kan starte efter aftale.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Produktionsleder med tolv år i drift og kvalitet. 12 mekanikere og teknikere, 14 "
           "medarbejdere og 11 entrepriser, 5 elektrikere og 3 lærlinge med fuldt P&L, og 37 "
           "CAPEX-projekter med nul kritiske fund. Arbejder på tavlen med de samme tal hver dag — og "
           "har betalt prisen for dårlig kvalitet af egen lomme.", after=80)

    m.section("LEDELSE OG DAGLIG DRIFT")
    for label, body in [
        ("Tavlemøde og SQDCI",
         "Daglig tavle med **SQDCI**-rækkefølgen: sikkerhed først, så kvalitet, levering, "
         "omkostning og lager. Femten minutter, faste tal, en ejer pr. linje."),
        ("Planlægning og kapacitet",
         "**Kapacitet** og bemanding styret mod produktionsplanen uge for uge; flytninger begrundet, "
         "meldt ud og fulgt op dagen efter."),
        ("Coaching på gulvet",
         "**Coaching** ved emnet: hvad er fejlen, hvad koster den, og hvad gør vi i morgen. "
         "**Udvikling** som plan pr. medarbejder, **MUS** hvert år, ansvar givet tidligt."),
    ]:
        m.bullet(label, body)

    m.section("KVALITET OG FORBEDRING")
    for label, body in [
        ("Rodårsag og CAPA",
         "**Problemløsning** med **rodårsag** før Handling: afgræns, mål, find årsagen, luk med "
         "**korrigerende** og **forebyggende** tiltag og efterprøv effekten."),
        ("LEAN i produktionen",
         "**LEAN** som værktøjskasse — **5S**, **A3**, **Kaizen**, **PDCA**, **standardarbejde** og "
         "tavler; 40 procent højere produktivitet efter systematisk forbedringsarbejde."),
        ("Måling og dokumentation",
         "**Måling**, **kalibrering**, **sporing** og **afvigelse** i samme fil pr. ordre; nul "
         "kritiske fund ved aflevering på 37 projekter i reguleret produktion."),
    ]:
        m.bullet(label, body)

    m.section("TVÆRFUNKTIONELT OG LEVERANDØRER")
    for label, body in [
        ("Mod engineering og procurement",
         "**Tværfunktionelt** samarbejde i ændringsvurdering og indkøb: kvalitet med i beslutningen, "
         "før tegningen og ordren forlader huset."),
        ("Leverandørkvalitet",
         "Leverandørvurdering, modtagelseskontrol og **reklamation** behandlet til **rodårsag**; "
         "**leverandørkvalitet** målt på gentagelser, ikke på antal sager."),
        ("Kunder og myndigheder",
         "**Audit** og kundeinspektion som hverdag: dokumentationen findes, når den bliver spurgt om "
         "— også klokken 14 en fredag."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Ejer / teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · fuldt P&L · kvalitet, økonomi og levering")
    m.bullet("Kvalitet betalt af egen lomme",
              "Scrap, omarbejde og garanti på eget regnskab; **Cost of Quality** blev ikke et "
              "begreb, men en post — og en grund til at forebygge tidligere.")

    m.job("Senior Commissioning Engineer / Project Manager",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul 2024",
          scope="37 samtidige CAPEX-projekter · 25 specialister · GMP/FDA/EMA")
    m.bullet("Afvigelser og myndighed",
              "Afvigelser, ændringsstyring og **CAPA** med nul kritiske fund ved aflevering; "
              "**sporing** og dokumentation i **SAP**, med myndigheden som medlæser.")

    m.job("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · eget værksted")
    m.bullet("Én standard på elleve sager",
              "Samme kontrol og samme acceptkriterier på 11 parallelle opgaver; afvigelser fra "
              "værksted og leverandører i ét register med én ejer pr. linje.")

    m.job("Drifts- og vedligeholdelseschef", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="Renseanlæg i 24/7-drift · pumper, HVAC, HV-tavler, SRO/SCADA")
    m.bullet("Systematik i driften",
              "**5S**, **standardarbejde** og forebyggende vedligehold som fast rytme; **PDCA** med "
              "40 procent lavere energiforbrug som dokumenteret effekt.")

    m.job("Produktionsformand / elektromekaniker",
          "ARJ Engineering · Teheran · 2003–2010 · 12 mekanikere og teknikere")
    m.bullet("Første lederrolle",
              "Daglig fordeling, kvalitetskontrol og oplæring i et produktionsværksted med maskiner, "
              "værktøj og tegninger i daglig brug.")

    # ---------------------------------------------------------------- side 3
    m.page_break()
    m.section("UDDANNELSE OG AUTORISATION")
    m.edu("Elautoriseret maskinmester — dansk elautorisation LV/MV/HV",
          "Sikkerhedsstyrelsen · maj 2023")
    m.edu("B.Tech, Technology Management and Mechanical Engineering (EQF 6)",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12")
    m.edu("El- og maskinteknisk design, Electrical Engineering (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("Køle- og VVS-teknik (AMU) · Lean: 5S, PDCA, VSM, A3",
          "Mercantec · 2021 · STCW-sikkerhedscertifikater (2021–2023)")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("**Dansk:** modersmål · **Engelsk:** professionelt, skriftligt og mundtligt · "
           "**Persisk:** modersmål · **Bor i Måløv**, søger stillingen i Nordborg med flytning for "
           "øje · **Kørekort B** · **Kan starte efter aftale** · Referencer efter aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA TAVLEN TIL ET TAL DER FLYTTER SIG",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–2",
             "Stå på gulvet i alle skift: lær teamet og de 22 roller at kende, se hvor "
             "**afvigelser** opstår, og læs de sidste tre måneders **reklamationer** og "
             "**CAPA**-sager igennem."),
            ("Dag 30",
             "Tavlemødet kører med **SQDCI** i fast rækkefølge og en ejer pr. linje; "
             "**Cost of Quality** opgjort på fire poster, så summen kan ses."),
            ("Dag 60",
             "To **rodårsager** lukket med effektkontrol, og den første leverandør gennemgået med "
             "aftalte målinger i stedet for modtagelseskontrol alene."),
            ("Dag 90",
             "Et **standardarbejde** for den mest kritiske kontroloperation, kompetencematrix for "
             "teamet og et fald i gentagne afvigelser, der kan dokumenteres — ikke fortælles."),
        ],
        widths=(1500, 8830))

    m.section("EN KVALITETSOPERATØR SKAL HAVE RET TIL AT STOPPE — OG GRUND TIL AT GØRE DET")
    m.para("Stoppet er kun noget værd, hvis det bliver taget alvorligt. Det betyder, at den, der "
           "stopper linjen, får svar inden for få minutter, at afgrænsningen sker sammen med hende, "
           "og at der bliver sagt tak — også når stopet viste sig at være en falsk alarm. Et team, "
           "der stopper for sjældent, er dyrere end et team, der stopper for meget, fordi fejlen "
           "allerede er sendt videre i kæden. Det er den ene adfærd, jeg ville bruge mest tid på.",
           after=70)

    m.section("EN GENTAGELSE ER IKKE EN NY FEJL — DET ER EN MANGLENDE LUKNING")
    m.para("Når den samme afvigelse dukker op to gange, er det ikke produktionen, der er problemet. "
           "Det er lukningen, der var for hurtig. Derfor bliver hver **CAPA** vurderet på, om den "
           "ændrede noget, der kan måles — en fixtur, en instruks, en kontrol, et valg hos en "
           "leverandør — og derfor bliver den læst igennem igen efter 60 dage. En lukket sag er ikke "
           "en løst sag.", after=70)

    m.section("TALLET PÅ TAVLEN SKAL KUNNE FORKLARES AF DEN, DER STÅR VED MASKINEN")
    m.para("**Datadrevet** betyder ikke mange diagrammer. Det betyder, at den, der står med opgaven, "
           "kan se sit eget tal og forklare, hvorfor det er, som det er. Derfor er tavlen enkel: få "
           "tal, samme rækkefølge, en ejer og en dato. Det er også derfor, jeg hellere vil have fem "
           "**KPI**'er, der bliver brugt, end tyve der bliver præsenteret.", after=70)

    m.section("BUDGETTET BETALER SIG IKKE SELV — DET SKAL EJES AF NOGEN")
    m.para("En kvalitetsafdeling bliver ofte målt på, hvad den koster, og sjældent på, hvad den "
           "forhindrer. Derfor vil jeg have budgettet ind på samme måde som de andre tal: hvad "
           "koster kontrollen, hvad koster det, vi ikke fangede, og hvad ville det koste at fange "
           "det tidligere. Den sammenligning er også den, der giver mandat til at sige nej til en "
           "besparelse, som flytter udgiften til kunden. Jeg har ført den samtale med mit eget "
           "regnskab som indsats.", after=70)

    m.section("HVOR JEG VILLE STARTE")
    m.para("Ved tavlen klokken 06.30 og ved emnet, der blev afvist i går. Første uge: gå med i alle "
           "skift, læs månedens afvigelser og reklamationer, og find ud af, hvor mange af dem der er "
           "den samme fejl med et nyt nummer. Derefter tage den første af dem hele vejen: afgræns, "
           "mål, find årsagen, luk, og mål igen efter 60 dage.", after=0)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "DET EFTERSPØRGER DE — DET HAR JEG",
        ["Krav i opslaget", "Dokumentation"],
        [
            ("Erfaring med ledelse i en produktions- eller produktionsnær organisation",
             "Tolv år: 12 mekanikere og teknikere i produktionsværksted, 14 medarbejdere og 11 "
             "entrepriser, 5 elektrikere og 3 lærlinge med fuldt P&L."),
            ("Praktisk erfaring med kvalitetsarbejde og kontinuerlige forbedringer i et produktionsmiljø",
             "**Forbedringer** drevet på gulvet: 5S, A3 og PDCA med 40 procent lavere energiforbrug og "
             "40 procent højere produktivitet; nul kritiske fund ved aflevering på 37 projekter."),
            ("En struktureret, systematisk og datadrevet tilgang til problemløsning og beslutningstagning",
             "**Problemløsning** på A3 med afgrænsning, måling, **rodårsag** og effektkontrol; beslutninger "
             "dokumenteret med tal, ejer og dato."),
            ("Tværfunktionelt samarbejde på tværs af produktion, engineering, procurement og leverandører",
             "**Tværfunktionelt** arbejde i 37 CAPEX-projekter og 11 entrepriser: 25 specialister, "
             "indkøb, leverandører og udførelse omkring samme plan."),
            ("Flydende dansk samt gode engelskkundskaber skriftligt og mundtligt",
             "**Dansk** modersmål; **engelsk** professionelt i møder, rapporter og med udenlandske "
             "leverandører — også som mødeleder."),
            ("Erfaring med LEAN og strukturerede forbedringsværktøjer",
             "**LEAN** i praksis: **5S**, **A3**, **Kaizen**, **PDCA**, **standardarbejde** og tavler — "
             "indført i værksted og drift, ikke kun læst om."),
            ("Erfaring med leverandørkvalitet eller kvalitetsledelse i en produktionsvirksomhed",
             "**Leverandørkvalitet** som bestiller og modtager: krav i ordren, kontrol ved modtagelse, "
             "**reklamation** til **rodårsag** og opfølgning på gentagelser."),
            ("Lede, coache og udvikle et team på cirka 22 kvalitetsoperatører med samarbejde, ansvarlighed og respekt",
             "Team på op til 14 personer ledet dagligt, med **coaching** ved opgaven, **MUS**, "
             "oplæringsplaner og ansvar givet tidligt; tre lærlinge uddannet."),
            ("Sikre sikker og effektiv daglig drift gennem planlægning, koordinering og opfølgning på SQDCI-mål via daglige tavlemøder",
             "Dagligt **tavlemøde** med fast rækkefølge og et tal pr. linje; bemanding og **kapacitet** "
             "koordineret mod produktionsplanen hver uge."),
            ("Drive løbende kvalitetsforbedringer gennem systematisk problemløsning, faktabaserede analyser og LEAN med korrigerende og forebyggende handlinger",
             "**Korrigerende** og **forebyggende** handlinger lukket med navn og dato og efterprøvet "
             "efter 60 dage; gentagne afvigelser behandlet som manglende lukning."),
            ("Samarbejde med produktion, engineering, procurement og leverandører for at forebygge gentagelser",
             "Ændringsvurdering med **engineering** og indkøb, før en specifikation rammer gulvet; "
             "**leverandører** målt på gentagelser, ikke på antal sager."),
            ("Fremme en kultur, hvor kvalitet, ejerskab og kontinuerlige forbedringer er en naturlig del af hverdagen, og understøtte budgetstyring og performance",
             "Kvalitet som ejerskab pr. emne og pr. skift; **budget** og **performance** fulgt med fuldt "
             "P&L-ansvar siden 2023."),
            ("Vedholdenhed i kvalitetsarbejdet baseret på en grundlæggende forståelse for Cost of Quality",
             "**Cost of Quality** opgjort på fire poster — scrap, omarbejde, garanti og kontrol — og "
             "betalt af eget regnskab: den dyreste time er den, der ikke blev brugt på at forebygge."),
            ("Sikkerhed som første prioritet i den daglige drift",
             "**Sikkerhed** før tal: LOTO, APV og sikkerhedsrundering i fire år i 24/7-drift, og "
             "nærved-hændelser behandlet samme uge."),
            ("Kendskab til sporing, kalibrering og revision i et kvalitetssystem",
             "**Sporing**, **kalibrering** og **audit** fra reguleret produktion under GMP/FDA/EMA, "
             "med dokumentation der kunne læses af en myndighed."),
        ],
        widths=(3600, 6746))

    m.section("ET TEAM PÅ 22 BLIVER IKKE ET TEAM AF ET ORGANISATIONSDIAGRAM")
    m.para("Det bliver et team, når de samme tal bliver gennemgået på samme måde hver morgen, når "
           "fejl bliver behandlet som systemer og ikke som personer, og når den, der siger noget "
           "ubehageligt klokken 06.30, stadig bliver lyttet til klokken 14. Det er ikke kultur som "
           "overskrift. Det er kultur som rækkefølge i dagsordenen.", after=0)

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_Danfoss_SupervisorQuality.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_Danfoss_SupervisorQuality.docx'))
