# -*- coding: utf-8 -*-
"""Operation Specialist — Aeven, Datacenter Ejby (Ejby Industrivej 11, Glostrup) (dansk opslag).

Dansk opslag -> dansk dokument, 4 sider: brev side 1, CV side 2, uddannelse + 90 dage +
metodeafsnit + "Hvor jeg ville starte" side 3, kravmatrix side 4. Format per master/README.md.

STILVALG (master/STILREGISTER.md; godkendt af scripts/style_guard.py, 3/3 skift mod #215):
  register      = VALIDERET PRODUKTION (GMP) — dokumentation, sporbarhed, afvigelse, ændrings-
                  styring, revision, "nul kritiske fund". Sidst #205.
  åbningsgreb   = B (NEGATIONEN) — "Et datacenter går sjældent ned, fordi strømmen forsvinder",
                  understøttet af Uptime Institutes egen fejlstatistik. Sidst #191.
  struktur      = ORDLISTEN — virksomhedens og certificeringens egne begreber oversat til praksis:
                  Tier III · PM · MOP/SOP/EOP · change management · on call · revision · energi.
                  Sidst #208.
  kadence       = forklarende sætninger med en konkret praksis i hver; ingen tillægsord om personen.

KULTURSYNKRONISERING (policy 04.11.2026), kilder i master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md
§187:
  Aeven: udskilt af NNIT's infrastrukturforretning (april 2023, Agilitas Private Equity), ca. 1.400
  medarbejdere, CEO Henrik Bodskov, positionering "**Adaptive Digital Infrastructure**" — "
  pålideligheden fra lokal infrastruktur i Danmark med fleksibiliteten fra cloud". Kunder i **life
  science, sundhed, finans, energi og den offentlige sektor**; "systemer, der ikke må fejle"; 30+
  års arv fra NNIT. Datacentre: **EIA1, Ejby Industrivej 11, 2600 Glostrup** (Tier III, 4.200 m²,
  45.000+ servere, 1,9 MW kritisk effekt, 1,9 MW redundant batteri- og generatorbackup) og **BA1P,
  Brudelysvej 28, Bagsværd** (Tier III Gold for Operational Sustainability, recertificeret 2022).
  **ISO 14001**-certificeret, fysisk sikkerhedspersonale 24/7, biometrisk adgangskontrol og
  **mantraps**. Deres egen tone: "**dansk ledet**", "kort vej fra idé til handling", "du er med til
  at forme og videreudvikle vores datacenterprodukt", kultur af "expertise, inclusion and growth".
  Opslaget: facility-team, 24/7/365, roller bygget op om **Uptime Institutes** principper for
  Tier-certificeret drift.

Uptime Institute (kilder: uptimeinstitute.com Tier Certification Operational Sustainability,
Uptime Journal 2015 og Uptime-analyse 2025): **human error mere end 70 %** af alle datacenter-
nedbrud; knap **40 %** af organisationerne har haft et større nedbrud forårsaget af menneskelig fejl
inden for tre år, og **85 %** af dem skyldtes, at procedurer ikke blev fulgt, eller at procedurerne
var mangelfulde. **MOP** = skriftlige trin for at ændre tilstanden af en kritisk komponent, ligger
inde i change management, risikovurderes og godkendes før arbejdet starter og gennemgås mindst en
gang om året; **SOP** = rutinedrift; **EOP** = ordnet respons på en unormal hændelse. **AOS**
(Accredited Operations Specialist) er den relevante certificering for drifts- og facilitysikkerhed.

Ingen opdigtede fakta. Dokumenteret grundlag: 4 år i 24/7-drift med SRO/SCADA, HV-tavler, pumper,
HVAC, vagtordning og akut fejlfinding (Biofos/Lynetten 2017-2022); 37 CAPEX-anlæg med FAT/SAT,
IQ/OQ/PQ, nul kritiske fund og dokumentation i SAP under GMP/FDA/EMA (Novo Nordisk 2022-2024),
herunder UPS samt nød- og sikkerhedsbelysning; 14 mand, 11 samtidige entrepriser og eget værksted
(Ventek-Air 2022); 5 elektrikere + 3 lærlinge med fuldt P&L og serviceaftaler med responstid
(ELOHVAC 2023-); 12 mekanikere og teknikere (ARJ 2003-2010); PDCA med 40 % lavere energiforbrug;
elautoriseret maskinmester LV/MV/HV; B.Tech EQF 6 (7,6/12); dansk modersmål, engelsk professionelt;
kørekort B. **Ingen påstand om datacenter-, AOS- eller generatoroperatørerfaring.**
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Operation Specialist · kritisk datacenterinfrastruktur'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("10. november 2026")
    m.meta("Operation Specialist · Datacenter Ejby, Glostrup · Aeven")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Operation Specialist", bold=True, color='1A1A1A')
    m.para("Kære ledelsen i Aeven,", after=60)

    # ---------------------------------------------------------------- side 1
    m.para("**Et datacenter går sjældent ned, fordi strømmen forsvinder.** Uptime Institute regner "
           "mere end **70 procent** af alle nedbrud i datacentre for menneskelig fejl, og deres egen "
           "analyse peger på, at langt de fleste af dem handler om procedurer, der ikke blev fulgt — "
           "eller som var skrevet forkert. Det er den slags fejl, en ekstra UPS ikke løser. De bliver "
           "løst i hverdagen: i PM-planen, i MOP'en, i loggen og hos den, der tager telefonen kl. "
           "02.30.", after=80)

    m.para("**Aeven ejer og driver selv sine datacentre med egne folk** — Tier III i Glostrup og i "
           "Bagsværd, ISO 14001, døgndrift og kunder i life science, sundhed, finans, energi og den "
           "offentlige sektor: **samfundskritiske** virksomheder, hvor et stop ikke bare er en sag, "
           "men en avisoverskrift. Det er den slags drift, jeg har stået i i fire år: anlæg, der ikke må "
           "stoppe, med dokumentation som nogen læser bagefter, og med en vagtordning, hvor "
           "responstiden ikke er en hensigt men et vilkår.", after=80)

    m.para("**Tier III — samtidig vedligeholdelig, ikke ufejlbarlig.** At en komponent kan skiftes, "
           "mens lasten kører, er en egenskab ved anlægget. At det sker uden afbrydelse, er en "
           "egenskab ved dem, der gør det: MOP'en er skrevet, rækkefølgen er prøvet af, og "
           "tilbagerulningen er besluttet, før den første kontakt bliver åbnet.", after=80)

    m.para("**PM er en kalender, ikke en hensigt.** Planlagt vedligehold bliver kun forebyggende, "
           "hvis datoen holder, hvis proceduren følger med, og hvis udførelsen bliver kvitteret. Jeg "
           "har kørt **planlagt vedligehold** på 24/7-anlæg med SRO/SCADA, HV-tavler, pumper og "
           "HVAC — og med et reservedelslager bygget efter, hvad der faktisk stod stille, ikke efter "
           "hvad der var nemt at bestille.", after=80)

    m.para("**MOP, SOP og EOP er tre dokumenter med tre forskellige formål.** Ændringen, rutinen og "
           "nødretten må ikke blandes sammen, for så bliver nødproceduren læst som en vejledning "
           "midt i en **hændelse**. Jeg har skrevet arbejdsinstrukser og ændringsprocedurer under "
           "**GMP**/FDA/EMA, hvor et dokument uden version og underskrift ikke var et dokument.",
           after=80)

    m.para("**En ændring uden tilbagerulning er en plan uden bagkant.** **Change management** ved "
           "live last betyder, at ændringen er risikovurderet, godkendt og tidsbestemt, før den "
           "bliver sat i gang — og at der er en vej tilbage, som nogen har prøvet. Det er samme "
           "disciplin som change control i SAP og som en **afvigelse**, der skal lukkes på rodårsag "
           "og ikke på høflighed.", after=80)

    m.para("**On call er en responstid, ikke en telefonsvarer.** En **vagtordning** er kun noget "
           "værd, hvis **eskaleringen** er kendt på forhånd, hvis den, der bliver ringet op, ved "
           "hvad han må gøre uden at spørge, og hvis hændelsen bliver skrevet ned, mens den sker. "
           "Jeg har haft vagttelefonen i fire år på Lynetten og tilkaldevagt i eget selskab, og "
           "det første kvarter bliver afgjort af det, der blev skrevet ned i sidste uge.", after=80)

    m.para("**Dokumentationen skal kunne læses af en revisor, ikke kun af os.** **Logføring** er "
           "ikke en byrde oven på driften; det er den måde, en hændelse bliver til noget, andre kan "
           "lære af. På 37 anlæg under GMP/FDA/EMA blev dokumentationen læst af myndigheden, og nul "
           "kritiske fund ved aflevering var ikke held — det var et krav, der blev holdt.", after=80)

    m.para("**Energi er en driftsmåling, ikke en kampagne.** Køl og el er de to poster, der kan "
           "flyttes uden at røre **oppetiden**. Jeg har hentet **40 procent lavere energiforbrug** "
           "gennem PDCA på et 24/7-anlæg, og det skete ved at måle, justere og skrive det ned — ikke "
           "ved at slukke noget.", after=80)

    m.para("**Dansk ledet betyder kort vej fra beslutning til handling.** Når et anlæg skal "
           "ændres, eller en procedure skal skrives om, venter man ikke på et møde i næste måned. "
           "Det er den arbejdsform, jeg selv har haft som ejer i tre år, hvor idé, beslutning og "
           "udførelse lå i samme uge — fordi der ikke var nogen anden til at tage den.", after=80)

    m.para("**Praktisk.** Jeg bor i Måløv, og Ejby Industrivej er en kort køretur derfra, også når "
           "det er nat. Jeg er uddannet **elautoriseret maskinmester** (LV/MV/HV), taler og skriver "
           "**dansk** og **engelsk**, og går ind i **on call**-ordningen fra første dag. "
           "Certificeringen hos **Uptime Institute** er en fordel, og den ligger lige for: jeg arbejder "
           "allerede efter logikken hver dag og tager gerne **AOS** som en del af opstarten. "
           "**Kørekort B.** Kan tiltræde efter aftale.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Operation Specialist med tolv års drifts- og vedligeholdelsesansvar i døgnkritisk miljø. "
           "Fire år i **24/7**-drift med SRO/SCADA, HV-tavler, køl og **vagtordning**; 37 anlæg "
           "under GMP/FDA/EMA med **nul kritiske fund**; 40 procent lavere **energiforbrug** gennem "
           "PDCA. **Elautoriseret maskinmester** (LV/MV/HV) med hænderne i fejlfindingen.", after=80)

    m.section("DRIFT AF KRITISK INFRASTRUKTUR")
    for label, body in [
        ("El, køl og styring",
         "HV-tavler, **UPS**, nød- og sikkerhedsbelysning, pumper, HVAC og **BMS** i form af "
         "SRO/SCADA; alarmer, målinger og **fejlfinding** efter dokumenteret metode."),
        ("Planlagt vedligehold",
         "**PM**-kalender med procedure, kvittering og log pr. opgave; reservedele og "
         "kritiske komponenter styret efter, hvad der faktisk stopper driften."),
        ("Hændelser og beredskab",
         "Fast **eskalering**, responstid og aftalt beslutningsret i **beredskabet**; hændelsen "
         "logget fra alarm til lukning og gennemgået dagen efter."),
    ]:
        m.bullet(label, body)

    m.section("PROCEDURER, ÆNDRING OG DOKUMENTATION")
    for label, body in [
        ("Instrukser og procedurer",
         "Arbejdsinstrukser, **SOP** og nødprocedurer skrevet sammen med dem, der skal bruge dem "
         "— med version, ejer og gennemgang en gang om året."),
        ("Change control",
         "**Change management** med risikovurdering, godkendelse og tilbagerulning før arbejdet "
         "starter; ændringer i **konfigurationen** dokumenteret i SAP."),
        ("Log, afvigelse og audit",
         "**Logføring**, **afvigelse** og **validering** under GMP/FDA/EMA; **audit** og "
         "**revision** med nul kritiske fund på 37 anlæg — dokumentation, der kunne læses udefra."),
    ]:
        m.bullet(label, body)

    m.section("LEVERANDØRER, ENERGI OG ØKONOMI")
    for label, body in [
        ("Serviceaftaler og leverandører",
         "**Serviceaftaler** med fast responstid og **leverandører** styret på møde, dokumentation "
         "og opfølgning — ikke på tillid alene."),
        ("Energi og bæredygtighed",
         "**Energiforbrug** målt pr. anlæg og **bæredygtighed** som driftsmål: 40 procent lavere "
         "forbrug gennem PDCA; ISO 14001-logikken er kendt fra reguleret produktion."),
        ("Økonomi og indkøb",
         "Fuldt P&L, indkøb, tilbud og efterkalkulation; anlæg og reservedele prioriteret efter "
         "**oppetid** og risiko, ikke efter hvad der er nemmest at købe."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Ejer / teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · fuldt P&L · serviceaftaler med responstid")
    m.bullet("Drift med kunde på den anden side",
              "Akutte udkald, fast responstid og serviceaftaler, hvor en time ekstra er en kunde, "
              "der står stille; nul kritiske afvigelser i aftalerne.")

    m.job("Senior idriftsættelsesingeniør / projektleder",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024",
          scope="37 CAPEX-anlæg · 25 specialister · GMP/FDA/EMA · SAP · UPS og sikkerhedsbelysning")
    m.bullet("Idriftsættelse og dokumentation",
              "FAT/SAT og IQ/OQ/PQ med sekvenser prøvet af, før anlægget gik i drift; nul "
              "kritiske fund og dokumentation, der kunne læses af en myndighed.")

    m.job("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · eget værksted")
    m.bullet("Én rytme på elleve sager",
              "Dagligt møde, kapacitet og fremdrift på samme tavle; flaskehalse flyttet, inden de "
              "blev til forsinkelser.")

    m.job("Drifts- og vedligeholdelseschef", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="Renseanlæg i 24/7-drift · pumper, HVAC, HV-tavler, SRO/SCADA · vagtordning")
    m.bullet("Døgnkritisk drift",
              "Alarmer, akut fejlfinding og **planlagt vedligehold** i fast rytme; 5S, "
              "standardarbejde og PDCA med 40 procent lavere energiforbrug som effekt.")

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
           "**Persisk:** modersmål · **Bor i Måløv**, Ejby Industrivej er en kort køretur derfra · "
           "**On call** og skiftearbejde: ja · **Kørekort B** · **Kan tiltræde efter aftale** · "
           "Referencer efter aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA PM-PLAN TIL EN LOG, DER HOLDER",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–2",
             "Gå med i alle vagtlag og læs de sidste tre måneders hændelser, afvigelser og "
             "ændringer igennem: hvad skete der, hvem godkendte, og hvad står der i loggen bagefter. "
             "Lær anlægget at kende fra tavlen, ikke fra mappen."),
            ("Dag 30",
             "PM-planen gennemgået med det tekniske team og **leverandørerne**: hvad er udført, hvad "
             "er udskudt, og hvilke komponenter står uden prøvet tilbagerulning. En ejer og en dato "
             "på hver."),
            ("Dag 60",
             "**MOP** og **EOP** prøvet af i praksis — ikke læst op. De procedurer, der ikke kan "
             "følges kl. 02.30, bliver skrevet om; de ændringer, der mangler en vej tilbage, får "
             "en."),
            ("Dag 90",
             "En fast rytme: PM-status, hændelsesgennemgang og ændringskalender på samme møde, med "
             "**logføring** der kan læses af en **revisor**. **Oppetid**, responstid og "
             "energiforbrug målt, så næste kvartal kan planlægges på tal."),
        ],
        widths=(1500, 8830))

    m.section("EN LOG, DER BLIVER SKREVET EFTER HÆNDELSEN, ER EN MENING")
    m.para("Loggen er det eneste sted, hvor en hændelse bliver til viden. Derfor bliver den skrevet, "
           "mens den sker — tid, komponent, hvad der blev set, hvad der blev gjort, og hvem der "
           "godkendte — og ikke renskrevet om mandagen. Det er den forskel, der gør, at den samme "
           "fejl ikke kommer igen med et nyt nummer, og at en **audit** kan følges tilbage til den "
           "aften, beslutningen blev taget.", after=70)

    m.section("COMPLIANCE ER DET, DER STÅR TILBAGE, NÅR REVISOREN GÅR")
    m.para("**Regulatoriske** krav og kundernes **compliance**-standarder bliver ikke opfyldt i "
           "måneden op til revisionen. De bliver opfyldt, fordi dokumentationen bliver skrevet i "
           "samme rytme som driften: ændringen, afvigelsen, kvitteringen og gennemgangen. Jeg har "
           "haft myndigheden som medlæser på 37 anlæg, og erfaringen er enkel: det, der ikke står "
           "skrevet, har ikke fundet sted.", after=70)

    m.section("FYSISK SIKKERHED ER EN DRIFTSOPGAVE, IKKE EN PORT")
    m.para("Biometrisk **adgangskontrol**, **mantraps** og sikkerhedspersonale er kun noget værd, "
           "når de bliver brugt rigtigt i hverdagen: adgang følger opgaven, ikke stillingen, "
           "besøgende har en ledsager, og et åbent dørparti bliver meldt, ikke diskuteret. Jeg er "
           "vant til at arbejde i **sikkerhedsklassificerede** miljøer, hvor adgang, log og ansvar "
           "hænger sammen, og hvor en afvigelse er en sag — også når den er lille.", after=70)

    m.section("BÆREDYGTIGHED ER ET TAL PÅ TAVLEN, IKKE ET AFSNIT I ÅRSRAPPORTEN")
    m.para("**ISO 14001** kræver, at man kan vise, hvad man har gjort — ikke kun hvad man vil. Køl "
           "og el er de to poster, der kan flyttes uden at røre **oppetiden**, og de flytter sig kun, "
           "hvis nogen måler, justerer og skriver ned. Jeg har gjort det på et 24/7-anlæg med 40 "
           "procent lavere **energiforbrug** som resultat, og metoden er den samme her: sæt et "
           "måltal, følg det ugentligt, og luk de tiltag, der ikke flytter noget.", after=70)

    m.section("ET ANLÆG, DER IKKE ER PRØVET, ER EN ANTAGELSE")
    m.para("**Redundans** er kun redundans, når den er prøvet. En **generator**, der aldrig er "
           "kørt i prøve, og en **UPS**, der aldrig har båret last, er to antagelser — og de bliver "
           "først til viden, når nogen har prøvet dem af med en plan, en måling og et dokument "
           "bagefter. Jeg har lagt prøvesekvenser og FAT/SAT på 37 anlæg, hvor \"det plejer at "
           "virke\" ikke var et svar, og hvor prøven blev gentaget, hver gang noget var ændret.",
           after=70)

    m.section("HVOR JEG VILLE STARTE")
    m.para("I tavlerummet og i loggen. Første uge: gå med i alle vagtlag, læs de sidste tre måneders "
           "hændelser og ændringer, og find ud af, hvor mange af dem der var den samme fejl med et "
           "nyt nummer. Derefter tage den første hele vejen — afgræns, find årsagen, luk, skriv det "
           "ned og prøv proceduren af igen om en måned. Det er ikke et projekt. Det er den rytme, "
           "**Tier III** holder af.", after=0)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "DET EFTERSPØRGER DE — DET HAR JEG",
        ["Krav i opslaget", "Dokumentation"],
        [
            ("Overvågning og daglig drift af el-, køle- og bygningsinstallationer (**BMS**), "
             "generatorer, **UPS** og **redundante** systemer",
             "**BMS** som SRO/SCADA, HV-tavler, **køleanlæg** og **el-tavler** i 24/7-drift; "
             "**UPS**, nød- og sikkerhedsbelysning projekteret, idriftsat og prøvet ved FAT/SAT "
             "— og **redundans** holdt prøvet i drift, ikke antaget."),
            ("**Planlagt vedligehold** (PM) og **fejlfinding** efter dokumenterede metoder, med "
             "teknikere og **leverandører**",
             "**PM**-kalender med procedure, kvittering og log; fejlfinding på A3 og 5xHvorfor; "
             "**leverandører** styret på møde, dokumentation og opfølgning."),
            ("Arbejde efter og videreudvikle standard- og nødprocedurer, så **afvigelser** og "
             "**hændelser** kan håndteres sikkert",
             "**Procedurer** skrevet med dem, der bruger dem: **SOP** og nødprocedure med version, "
             "ejer og årlig gennemgang; hændelsen logget fra alarm til lukning."),
            ("**Change management** — vurdere og gennemføre ændringer i sitets **konfiguration** "
             "med minimal risiko",
             "Ændringen risikovurderet, godkendt og tidsbestemt før arbejdet starter, med "
             "tilbagerulning prøvet; change control dokumenteret i **SAP**."),
            ("Præcis **logføring** og **dokumentation**, der lever op til kundernes "
             "**compliance**-krav og **Uptime Institute**-certificeringen",
             "**Logføring** og **dokumentation** under GMP/FDA/EMA, hvor et dokument uden version "
             "og underskrift ikke var et dokument; nul kritiske fund på 37 anlæg."),
            ("Driften lever op til **regulatoriske** krav og kundespecifikke "
             "**compliance**-standarder, herunder **revision** og **audit**",
             "**Audit** og **revision** med myndigheden som medlæser; **validering** og "
             "**afvigelse** lukket på rodårsag og efterprøvet efter 60 dage."),
            ("**Energieffektiv** drift og reduktion af det miljømæssige aftryk",
             "**Energiforbrug** målt pr. anlæg og fulgt ugentligt; 40 procent lavere forbrug "
             "gennem PDCA — og tiltag lukket, når de ikke flyttede tallet."),
            ("Uddannet maskinmester, installatør eller elektriker — eller anden teknisk uddannelse "
             "med solid driftserfaring",
             "**Elautoriseret maskinmester** (LV/MV/HV), B.Tech EQF 6 og el- og maskinteknisk design; "
             "autorisationen er erhvervet oven på maskinmesteruddannelsen, og tolv år er gået "
             "med hænderne i drift, tavler og fejlfinding."),
            ("Erfaring fra **datacenterdrift**, ejendomsdrift eller pharma-industrien",
             "Fire år i døgnkritisk drift med SRO/SCADA og vagtordning (Biofos) og 37 anlæg under "
             "**GMP**/FDA/EMA (Novo Nordisk), hvor **validering** og **compliance** var en fast del "
             "af hverdagen og ikke et projekt ved siden af."),
            ("Grundighed, **dokumentation** og at følge **procedurer**, hvor fejl kan få store "
             "konsekvenser",
             "24/7-drift, hvor et stop koster produktion med det samme; nul kritiske fund ved "
             "aflevering, og hændelser gennemgået dagen efter med dem, der sad med dem."),
            ("Indstillet på at indgå i en **on call**-**vagtordning**",
             "Vagttelefon og tilkaldevagt i fire år på Lynetten samt **on call** i eget selskab; "
             "**eskalering** og responstid aftalt på forhånd, ikke improviseret."),
            ("Taler og skriver **dansk** og **engelsk**",
             "**Dansk** modersmål; **engelsk** professionelt i møder, rapporter og med udenlandske "
             "**leverandører** — også som mødeleder."),
            ("Certificeringer eller kendskab til **Uptime Institute**s standarder, fx Accredited "
             "Operations Specialist, er en fordel",
             "**AOS** tages som en del af opstarten. Principperne er allerede arbejdsmetode: "
             "**MOP** i change management, **SOP** for rutinen og en prøvet **EOP** for nøden."),
            ("Drift af kritisk infrastruktur 24/7/365 i et **Tier**-certificeret **datacenter** med "
             "fokus på **oppetid**",
             "**Oppetid** som vilkår: 24/7-drift med SRO/SCADA, alarmer og akut fejlfinding; "
             "**beredskabet** prøvet af og hændelser gennemgået dagen efter, så den samme fejl "
             "ikke kommer igen med et nyt nummer."),
            ("Være med til at forme og videreudvikle datacenterproduktet i et dansk ledet "
             "miljø med kort vej fra idé til handling",
             "Arbejdsgange og instrukser bygget om i eget selskab og i eget værksted: idé, "
             "beslutning og udførelse i samme uge, med en ejer og en dato."),
            ("Samarbejde med tekniske kolleger og **leverandører** i et **sikkerhedsklassificeret** "
             "miljø med **fysisk sikkerhed** og **adgangskontrol**",
             "**Adgangskontrol** og **fysisk sikkerhed** som driftsopgave: adgang følger opgaven, "
             "log og ansvar hænger sammen, og afvigelser meldes samme dag."),
        ],
        widths=(3600, 6746))

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_Aeven_OperationSpecialist.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_Aeven_OperationSpecialist.docx'))
