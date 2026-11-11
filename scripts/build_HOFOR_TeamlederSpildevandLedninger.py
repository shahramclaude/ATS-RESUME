# -*- coding: utf-8 -*-
"""Teamleder for Spildevand Ledninger — HOFOR, Smedeholmen, Herlev (dansk opslag).

Dansk opslag -> dansk dokument, 4 sider: brev side 1, CV side 2, uddannelse + 90 dage +
metodeafsnit + "Hvor jeg ville starte" side 3, kravmatrix side 4. Format per master/README.md.
Opslaget siger: "du skal derfor ikke skrive en ansøgning, men blot sende dit CV" — formen følges
ikke: brevet bliver side 1, som altid (brugerens bindende krav).

STILVALG (master/STILREGISTER.md; godkendt af scripts/style_guard.py, 3/3 skift mod #221):
  register      = TEKNISK-DRIFTSNÆR — kort, konkret, tæt på klokken, vejret, brønden og den, der
                  tager telefonen. Sidst #201.
  åbningsgreb   = E (TIDSFORSKYDNINGEN) — kontakten med spildevand bliver ikke afgjort i brønden,
                  men ugen før, når nogen planlægger spuling, robot eller TV-inspektion i stedet for
                  at sende et menneske ned. Sidst #214.
  struktur      = FØR/EFTER — seks linjer fra "i dag" til "om 12 måneder": sikker drift, arbejdsmiljø,
                  spulevogne og tilsyn, digitalisering, faglighed, retning. Sidst #187.
  kadence       = korte sætninger med en tid, et sted eller et antal liter i hver anden linje.

KULTURSYNKRONISERING (policy 04.11.2026), kilder i master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md
§193:
  **HOFOR** (Hovedstadsområdets Forsyningsselskab) — Danmarks største forsyningsselskab, ejet af
  Københavns Kommune sammen med Albertslund, Brøndby, Dragør, Herlev, Hvidovre, Rødovre og
  Vallensbæk. Spildevand: **ca. 4.000 km kloakledninger** og **mere end 250 tekniske anlæg** for
  omkring **899.000 kunder**; hovedparten af spildevandet føres til renseanlæggene Lynetten,
  Damhusåen og Avedøre (Biofos). **Smedeholmen i Herlev** er HOFORs spildevandscenter (indviet 2018,
  bygget af Raunstrup, husstand til godt 40 medarbejdere, der servicerer flere tusinde kilometer
  kloak). **Klima:** siden 2011 store **skybruds**ledninger under byen, **separatkloakering** i bl.a.
  Tingbjerg og Bystævneparken, og **Svanemøllen Skybrudstunnel** — ti km lang, op til 4,9 m i
  diameter, **100.000 m³** kapacitet, **16 skakte**, anlægsstart ultimo 2025, der reducerer overløb
  til Utterslev Mose og vandløb med **97 %** og til Øresund med **87 %**. Opslagets eget sprog:
  "stabil og **bæredygtig** forsyning", "sikker, daglig drift", "**arbejdsmiljø**", "reducere
  medarbejdernes **kontakt med spildevand**", "**digitalisere** nuværende arbejdsgange", "fremtidens
  regn- og spildevandssystemer", "**interne tilsynsopgaver** og aktiviteter knyttet til
  **spulevogne**", "**opkvalificering**", "**synlig og nærværende**", "**stærkt kollegaskab**",
  "**stor frihed under ansvar**". Teamet er **ca. 15 erfarne medarbejdere** i sektionen **Spildevand
  Egen Drift**; tæt samarbejde med **sektionsleder** (Johnny Pedersen, johpe@hofor.dk, 2795 3504),
  **fagkoordinatorer** og øvrige ledere. Frist **30. november 2026**, 1. samtaler uge 50, 2. samtaler
  uge 51 med personlighedsprofil.

  **Brugerens beslutninger før byg (10.11.2026):** sikkerhedsgodkendelsen til "Fortroligt" nævnes
  **ikke** i dokumentet, og der skrives **intet om BIM** — i stedet besvares digitale platforme med
  dokumenteret systembrug (SAP, SRO/SCADA, dokumentation) og digitalisering af arbejdsgange.

Ingen opdigtede fakta. Dokumenteret grundlag: fire år som drifts- og vedligeholdelseschef på
**Biofos/Lynetten** (2017-2022) — spildevand i 24/7-drift, tilløb fra ledningsnettet, overløb ved
regn, **H2S** og arbejdsmiljø, **LOTO** og **APV**, pumper, **SRO/SCADA**, beredskab og
myndighedsrapportering; **14 mand og 11 samtidige entrepriser** med underentreprenører og eget
værksted (Ventek-Air 2022); **5 elektrikere + 3 lærlinge** og fuldt P&L (ELOHVAC 2023-); **37
CAPEX-anlæg** med FAT/SAT, nul kritiske fund og ændringsstyring i **SAP** (Novo Nordisk 2022-2024);
**12 teknikere** (ARJ 2003-2010); **elautoriseret maskinmester** LV/MV/HV (maj 2023), **B.Tech**
maskinteknik (EQF 6, 7,6/12), el- og maskinteknisk design (EQF 6), **køle- og VVS-teknik** (AMU
2021); dansk modersmål, engelsk professionelt; **kørekort B**; bor i Måløv, ca. 12 km fra Smedeholmen.
**Bevidst formulering:** ingen påstand om at have drevet **kloakledningsnet**, kørt **spulevogn**
eller udført **TV-inspektion** — erfaringen er fra renseanlæggets side af ledningen, og det siges
ligeud. Ingen påstand om sikkerhedsgodkendelse. Ingen omtale af BIM.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Teamleder · spildevand og ledningsdrift · sikker drift, arbejdsmiljø og digitalisering'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("10. november 2026")
    m.meta("Teamleder, Spildevand Ledninger · Sektionen Spildevand Egen Drift · Smedeholmen, Herlev")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Teamleder for Spildevand Ledninger", bold=True, color='1A1A1A')
    m.para("Kære Johnny,", after=60)

    # ---------------------------------------------------------------- side 1
    m.para("**Kontakten med spildevand bliver ikke afgjort i brønden. Den bliver afgjort ugen før** "
           "— når nogen planlægger, om opgaven kan klares med en spuler, en robot eller et kamera, "
           "eller om der skal et menneske ned. Det er den beslutning, jeg gerne vil være med til at "
           "tage for HOFORs ledningsnet, og den er en ledelsesbeslutning, ikke en teknisk detalje.",
           after=80)

    m.para("**HOFOR driver omkring 4.000 km kloakledninger** og mere end **250 tekniske anlæg** for "
           "cirka **899.000 kunder** i otte kommuner — og arbejder samtidig på det største "
           "skybrudsprojekt i hovedstaden: **Svanemøllen Skybrudstunnel**, ti kilometer, 100.000 "
           "kubikmeter og seksten skakte, der skal fjerne op til **97 procent** af overløbene til "
           "Utterslev Mose og vandløbene. Teamet skal altså ikke bare passe det net, der ligger i "
           "dag. Det skal passes, mens byen bygges om ovenpå det — med **separatkloakering**, "
           "projekter mod **skybrud** og gravearbejde i samme gade.", after=80)

    m.para("En **bæredygtig** forsyning er ikke et tal i et regnskab. Det er et net, der holder, "
           "når vejret gør, hvad vejret gør, og når den næste graveentreprenør ringer.", after=80)

    m.para("**Sikker drift — i dag → om 12 måneder.** I dag er driften båret af erfarne folk og "
           "faste ruter. Om tolv måneder skal den stadig være båret af dem, men prioriteringen skal "
           "kunne læses af andre end dem: hvilke ledninger der spules hvornår, hvad der er akut, hvad der er planlagt **vedligehold**, og "
           "hvad der venter til næste sæson. Det er ikke et systemkrav. Det er, fordi en vagt klokken "
           "tre om natten skal kunne se, hvad der blev besluttet i går.", after=80)

    m.para("**Arbejdsmiljø og kontakt med spildevand — i dag → om 12 måneder.** Målet er mindre "
           "**spildevandskontakt**, og det nås med udstyr, planlægning og vaner: spuling og "
           "**TV-inspektion** før brøndarbejde, rene redskaber, håndvask og skiftetøj der, hvor "
           "arbejdet er, og **H2S**-måling før nogen åbner et dæksel. Jeg har stået i den anden ende "
           "af den beslutning — på renseanlægget, hvor det kom ind, når nettet ikke blev passet — og "
           "jeg har prøvet at have ansvaret for, at folk kom hjem uden at tage arbejdet med sig.",
           after=80)

    m.para("**Spulevogne og tilsyn — i dag → om 12 måneder.** Spulevognen er teamets vigtigste "
           "værktøj og den dyreste ressource i kalenderen. Om tolv måneder skal den køre efter et "
           "billede af nettet og ikke efter en huskeseddel: hvilke strækninger der er spulet, hvad "
           "**TV-inspektion**en viste, og hvilke tilsyn der skal lukkes inden for fristen. "
           "**Interne tilsynsopgaver** skal have en fast rytme og en ejer — ellers bliver de det, "
           "man laver, når der er tid.", after=80)

    m.para("**Digitalisering — i dag → om 12 måneder.** Jeg tror ikke på digitalisering som et "
           "projekt med en slutdato. Jeg tror på, at den opgave, en medarbejder udfører hver uge, "
           "bliver en klik kortere, og at data bliver skrevet ind, hvor de bliver lavet. I eget "
           "selskab og på 37 anlægsprojekter har jeg flyttet arbejdsgange ind i **SAP** og "
           "**dokumentation**, der kunne bruges af andre end mig — og det, der virkede, var altid "
           "det, medarbejderne selv havde været med til at forme.", after=80)

    m.para("**Faglighed og opkvalificering — i dag → om 12 måneder.** Et team på 15 erfarne "
           "medarbejdere med **stærkt kollegaskab** og stor frihed under ansvar skal ikke styres. Det "
           "skal have en retning og en plan for, hvad den enkelte skal kunne om to år: maskinfører, "
           "TV-inspektør, arbejdsmiljø eller fagkoordinator. Jeg har oplært lærlinge og teknikere "
           "før, og jeg ved, at kompetenceudvikling kun tæller, når den står i en kalender.",
           after=80)

    m.para("**Hvad jeg ikke har.** Jeg har ikke drevet et kloakledningsnet, og jeg har ikke selv "
           "kørt spulevogn eller lavet TV-inspektion. Det, jeg har, er fire år med spildevand i "
           "24/7-drift, hvor jeg har ejet anlægget, beredskabet og arbejdsmiljøet, og tolv år med "
           "**personaleledelse** i driftsorganisationer — 14 mand, 12 teknikere og 5 elektrikere med "
           "tre lærlinge. Det er ikke det samme som jeres net. Det er tæt nok på til, at jeg kan "
           "lære det sidste af dem, der kan det.", after=80)

    m.para("**Praktisk.** Jeg bor i Måløv, og **Smedeholmen** er en kort køretur — ingen flytning, "
           "ingen pendling. **Kørekort B** og vant til at være på flere lokationer i samme uge. "
           "**Dansk** som modersmål, **engelsk** på professionelt niveau. Kan tiltræde efter aftale.",
           after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Driftsleder med tolv års **personaleledelse** og fire år med **spildevand** i "
           "24/7-drift: tilløb fra ledningsnettet, overløb ved regn, **H2S** og arbejdsmiljø, "
           "**LOTO** og **APV**, pumper, **SRO/SCADA** og beredskab. Vant til at prioritere sikker "
           "drift, flytte **arbejdsgange** ind i **SAP** og **dokumentation** og til at udvikle "
           "medarbejdere, der har mere faglighed end mig.", after=80)

    m.section("SPILDEVAND, DRIFT OG BEREDSKAB")
    for label, body in [
        ("Anlæg i døgndrift",
         "Renseanlæg med tilløb fra ledningsnettet, overløb ved regn og akut fejlfinding — "
         "**pumpestationer**, riste, slam og **SRO/SCADA** i fast rytme."),
        ("Prioritering",
         "Dagens opgaver skilt fra ugens og sæsonens; akutte sager løst, planlagte sager ikke "
         "glemt, og næste vagt orienteret skriftligt."),
        ("Beredskab",
         "Vagtordning, eskalering og kontakt til entreprenører og myndighed, når noget skulle løses "
         "uden for normal arbejdstid."),
    ]:
        m.bullet(label, body)

    m.section("ARBEJDSMILJØ OG SIKKERHED")
    for label, body in [
        ("Kontakt med spildevand",
         "Arbejde i brønde og bassiner planlagt med **APV**, måling og udstyr; arbejde i "
         "spildevand undgået, hvor det kunne undgås."),
        ("LOTO og adgang",
         "Låsning, afspærring og tilladelser som fast praksis — ingen åbner et anlæg, før nogen har "
         "sagt, at det er sikkert."),
        ("Ulykker og nærved",
         "Hændelser skrevet ned og gennemgået, ikke fejet ind under gulvtæppet; opfølgning på "
         "udstyr, vaner og instrukser."),
    ]:
        m.bullet(label, body)

    m.section("DIGITALISERING OG ARBEJDSPROCESSER")
    for label, body in [
        ("Systemer i drift",
         "**SAP** til ændringer, budget og reservedele, **SRO/SCADA** til overvågning og "
         "**dokumentation**, der kunne læses af den næste."),
        ("Arbejdsgange",
         "Skabeloner og kontrolpunkter gjort ens på 11 entrepriser og 37 anlæg — indført sammen med "
         "dem, der skulle bruge dem."),
        ("Måling og opfølgning",
         "Driftstal, responstider og afvigelser fulgt fast; forbedringer valgt på data, ikke på "
         "mavefornemmelse."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Ejer / teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · fuldt P&L · kunder, leverandører og dokumentation")
    m.bullet("Drift med ansvar for bundlinjen",
              "Kundeaftaler med responstid, plan for oplæring og en ordrebog leveret som solgt.")

    m.job("Senior idriftsættelsesingeniør / projektleder",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024",
          scope="37 anlægsprojekter · 25 specialister · SAP · myndighedsdokumentation")
    m.bullet("Arbejdsgange og dokumentation",
              "Ændringer styret i SAP, prøver kørt før overlevering og nul kritiske fund ved "
              "aflevering.")

    m.job("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · eget værksted")
    m.bullet("Elleve opgaver, én prioritering",
              "Kapacitet og fremdrift flyttet, før flaskehalse blev til forsinkelser; "
              "underentreprenører og sikkerhed styret på pladsen.")

    m.job("Drifts- og vedligeholdelseschef", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="Renseanlæg i 24/7-drift · spildevand, pumper, HVAC, HV-tavler, SRO/SCADA")
    m.bullet("Spildevandets anden ende",
              "Fire år med tilløb, overløb og arbejdsmiljø omkring spildevand — den erfaring, der "
              "gør en prioritering på ledningsnettet genkendelig.")

    m.job("Produktionsformand / elektromekaniker",
          "ARJ Engineering · Teheran · 2003–2010 · 12 mekanikere og teknikere")
    m.bullet("Første lederrolle",
              "Vagtplan, fordeling og oplæring i et værksted med maskiner, værktøj og tegninger i "
              "daglig brug.")

    # ---------------------------------------------------------------- side 3
    m.page_break()
    m.section("UDDANNELSE OG AUTORISATION")
    m.edu("Elautoriseret maskinmester — dansk elautorisation LV/MV/HV",
          "Sikkerhedsstyrelsen · maj 2023")
    m.edu("B.Tech, Technology Management and Mechanical Engineering (EQF 6)",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12")
    m.edu("El- og maskinteknisk design, Electrical Engineering (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("Lean: 5S, PDCA, VSM, A3 · køle- og VVS-teknik (AMU) · STCW-sikkerhed",
          "Mercantec 2021 · Søfartsstyrelsen 2021–2023")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("**Dansk:** modersmål · **Engelsk:** professionelt, skriftligt og mundtligt · "
           "**Persisk:** modersmål · **Bor i Måløv**, ca. 12 km fra Smedeholmen · **Kørekort B** · "
           "**Kan tiltræde efter aftale** · Referencer efter aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA DRIFT I DAG TIL DRIFT MED EN RETNING",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–2",
             "Kør med på arbejdet: to spuledage, en TV-inspektion, et tilsyn og en nattevagt. Læs "
             "de sidste tolv måneders hændelser og nærved-hændelser igennem — ikke for at finde en "
             "skyldig, men for at se mønstret."),
            ("Dag 30",
             "En liste over de ti strækninger og ti arbejdsopgaver, hvor kontakten med spildevand er "
             "størst, med et forslag pr. punkt: udstyr, planlægning eller vane. Gennemgået med "
             "**fagkoordinatorer** og **sektionsleder**, før den går videre."),
            ("Dag 60",
             "Spulevognens rute og tilsynsfristerne lagt i samme kalender, så teamet kan se ugen "
             "samlet; én arbejdsgang digitaliseret fra papir eller hoved til system — den, der "
             "irriterer mest."),
            ("Dag 90",
             "**Fælles mål** for teamet for det næste år, en kompetenceplan pr. medarbejder og et "
             "tal på, hvor mange liter spildevand der kom i kontakt med hvem — før og efter."),
        ],
        widths=(1500, 8830))

    m.section("EN DRIFT ER SIKKER, NÅR DEN ER KEDELIG")
    m.para("Det bedste, man kan sige om en uge på et ledningsnet, er, at der ikke skete noget. Det "
           "resultat kommer ikke af held; det kommer af, at nogen prioriterede den samme runde for "
           "syvende gang, at en føler blev skiftet, før den blev defekt, og at der stod et navn på "
           "den opgave, ingen ellers tog. Jeg har prøvet at drive et anlæg, hvor en times stop "
           "kostede penge og lugt i nabolaget, og det lærte mig at elske de kedelige uger.", after=70)

    m.section("ARBEJDSMILJØ ER PLANLÆGNING, IKKE EN KAMPAGNE")
    m.para("Man kan ikke bede folk om at undgå spildevand, hvis udstyret og planen gør det svært. "
           "Derfor sidder arbejdsmiljøet i planlægningen: hvilke opgaver der kan klares uden at gå "
           "ned, hvor spuling og **TV-inspektion** skal ligge før et indgreb, og hvor der skal stå "
           "vand og sæbe inden for rækkevidde. Jeg har haft **APV** og **LOTO** som fast rytme, "
           "ikke som en mappe, og det er den slags, et team kan mærke forskel på.", after=70)

    m.section("DIGITALISERING SKAL SPARE ET KLIK, IKKE FLYTTE ET ANSVAR")
    m.para("Et system, der kun flytter papir til en skærm, gør arbejdet tungere. Det, der virker, er "
           "at tage den opgave, der bliver lavet hver uge, og gøre den en klik kortere — og at "
           "skrive data ind, hvor de bliver lavet, så der ikke sidder nogen bagefter og gætter. Jeg "
           "har indført ændringsstyring i **SAP** og skabeloner, der blev brugt, fordi folk selv "
           "havde været med til at lave dem, og jeg har set det modsatte: systemer, ingen brugte, "
           "fordi de var besluttet ovenfra.", after=70)

    m.section("ET ERFARENT TEAM SKAL HAVE EN RETNING, IKKE EN OPSKRIFT")
    m.para("Femten medarbejdere med høj faglighed og stor frihed under ansvar leverer mere end "
           "femten, der venter på ordrer. Opgaven er at gøre retningen tydelig nok til, at den "
           "enkelte kan træffe sin egen beslutning i det daglige — og derefter at holde sig til "
           "**fælles mål** i stedet for at flytte dem, hver gang ugen bliver travl.", after=70)

    m.section("SAMARBEJDE ER ET VILKÅR I ET NET, DER LIGGER UNDER ANDRES ARBEJDE")
    m.para("Ledningsnettet ligger under gader, der bliver gravet i af kommunen, entreprenører og "
           "**forsyning**ens egne anlægsprojekter, og en spulevogn, der ikke er koordineret med "
           "gravearbejdet, er en spildt dag. Jeg har arbejdet på tværs af teknik, indkøb, drift og "
           "myndighed i 37 projekter, og erfaringen er den samme: samarbejde holder, når nogen "
           "kommer med et tidspunkt og et navn, ikke med en intention.", after=70)

    m.section("HVOR JEG VILLE STARTE")
    m.para("I brønden og i kalenderen. Første uge: med på to spuledage, en TV-inspektion og en "
           "nattevagt — og læse årets hændelser igennem. Derefter tage de ti strækninger, hvor "
           "arbejdet med spildevand er mest udsat, og se, om forskellen ligger i udstyr, "
           "planlægning eller vane. Det er der, et arbejdsmiljø bliver bedre, og det er der, et "
           "team kan se, at retningen ikke bare var et møde.", after=0)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "KRAV I OPSLAGET — DET HAR JEG",
        ["Krav i opslaget", "Dokumentation"],
        [
            ("Lede og prioritere **sikker, daglig drift** af ledningsområdet",
             "Fire år som driftschef på et anlæg i **24/7-drift** med tilløb, overløb og akut "
             "fejlfinding; 14 og 12 mand i driftsteams og 11 samtidige entrepriser."),
            ("Sikkert **arbejdsmiljø** og reducere medarbejdernes **kontakt med spildevand**",
             "**APV**, **LOTO**, **H2S**-måling og adgangsplanlægning som fast praksis; hændelser og "
             "nærved-hændelser gennemgået med opfølgning."),
            ("Optimere og **digitalisere** nuværende **arbejdsgange**",
             "**SAP** til ændringer, budget og reservedele og **dokumentation** andre kunne bruge; "
             "skabeloner indført med dem, der skulle bruge dem."),
            ("Understøtte udviklingen af fremtidens **regnvandssystemer** og spildevandssystemer",
             "Fire år med regnvand, overløb og **separatkloakering** set fra anlægssiden; "
             "**skybrud**, gravearbejde og koordinering med kommuner og entreprenører."),
            ("**Interne tilsynsopgaver** og aktiviteter knyttet til **spulevogne**",
             "Tilsyns- og kontrolopgaver i 24/7-drift, eksterne entreprenører og eget værksted "
             "styret. Ingen egen spulevogns- eller TV-inspektionserfaring — det læres i jobbet."),
            ("Sikre fortsat **opkvalificering** og udvikling af medarbejderne",
             "Tre lærlinge oplært, tolv teknikere udviklet, kompetenceplan pr. medarbejder og MUS "
             "hvert år."),
            ("**Ledelseserfaring** fra en **driftsorganisation** — forsyning, entreprenør eller kloak",
             "Tolv år med **personaleledelse** i teknik og drift: Biofos/Lynetten (forsyning), "
             "Ventek-Air (entreprenør), ELOHVAC (service) og ARJ (værksted)."),
            ("Erfaring med **personaleledelse**",
             "5 elektrikere + 3 lærlinge, 14 mand i entrepriseteam, 12 teknikere og 25 specialister "
             "i tværfaglig ledelse."),
            ("Erfaring med **arbejdsmiljøledelse**",
             "**APV**, sikkerhedsrundering, LOTO og instrukser i fire år; arbejde omkring spildevand, "
             "kemikalier og **H2S** med tilhørende måling og værnemidler."),
            ("**Synlig og nærværende** leder, der skaber tillid og engagement",
             "Til stede på pladsen, ikke kun i mødelokalet: sikkerhedsrundering, morgenmøde og "
             "1:1 — og den svære samtale taget, da den var nødvendig, med **respekt** for den, den gik ud over."),
            ("Interesse for **digitalisering** og udvikling af **arbejdsprocesser**",
             "Arbejdsgange flyttet fra hoved og papir til system på 37 anlæg og i eget selskab; "
             "forbedringer valgt på data."),
            ("**Samarbejde** på tværs af fagligheder og organisatoriske grænser",
             "Tværfagligt arbejde med teknik, indkøb, drift og myndighed; koordinering med "
             "entreprenører, kommuner og naboanlæg."),
            ("Kommunikerer klart og tydeligt på **dansk**",
             "**Dansk** modersmål — kort, konkret og skriftligt, så næste vagt kan handle på det."),
            ("Kan begå sig på **engelsk**",
             "**Engelsk** professionelt: dokumentation, leverandørmøder og udenlandske "
             "samarbejdspartnere."),
            ("**Kørekort** er en forudsætning — flere lokationer",
             "**Kørekort B**; vant til flere lokationer i samme uge og til at være der, hvor "
             "opgaven er."),
            ("**Kendskab til digitale platforme** i drift og dokumentation",
             "**SAP**, **SRO/SCADA** og dokumentationssystemer i daglig brug; nye platforme læres "
             "ved at bruge dem på en rigtig opgave, ikke på et kursus."),
            ("Lede et **erfarent team** med **stærkt kollegaskab** og høj faglighed",
             "Leder af fagligt stærke medarbejdere i alle fire stillinger — ledelse gennem retning, "
             "rammer og fagligt ansvar, ikke gennem kontrol."),
            ("Skabe **fælles mål** og retning i en hverdag med drift, arbejdsmiljø og udvikling",
             "**Mål** sat sammen med teamet og fulgt på tavle hver uge; udvikling planlagt, ikke "
             "lovet."),
        ],
        widths=(3600, 6746))

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_HOFOR_TeamlederSpildevandLedninger.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_HOFOR_TeamlederSpildevandLedninger.docx'))
