# -*- coding: utf-8 -*-
"""Sales Engineer - HVAC — Johnson Controls, Hornslet (fra foråret 2027: Holme, Aarhus). Dansk opslag.

Dansk opslag -> dansk dokument, 4 sider: brev side 1, CV side 2, uddannelse + 90 dage +
metodeafsnit + "Hvor jeg ville starte" side 3, kravmatrix side 4. Format per master/README.md.
Opslaget beder om ansøgning "allerede i dag", løbende behandling — det ændrer ikke formen.

STILVALG (master/STILREGISTER.md; godkendt af scripts/style_guard.py, 3/3 skift mod #219):
  register      = KOMMERCIEL-FORRETNINGSMÆSSIG — tal, margin, ordrebog, kunde, beslutning; teknik
                  kun hvor den flytter en krone. Sidst #197.
  åbningsgreb   = I (TESERNE) — tre påstande om, hvordan en HVAC-ordre bliver vundet og tabt,
                  som dokumentet beviser én for én. Sidst #215.
  struktur      = SNITFLADERNE — de fem grænseflader rollen ejer: kunden · teknikken · tilbuddet ·
                  kontrakten (Engineering, Procurement, Operations) · driften og service. Sidst #213.
  kadence       = korte sætninger med en krone, en dato eller en person i hver anden linje; ingen
                  tillægsord uden et beløb bag.

KULTURSYNKRONISERING (policy 04.11.2026), kilder i master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md
§191:
  **Johnson Controls Danmark** (Sabroe-arven): salg af **HVAC- og køleløsninger** og
  **serviceforretning** til erhverv og industri, med **Systems**-forretning og et **EPO**-set-up
  (**Engineering, Procurement, Operations**), som sælgeren arbejder igennem. Opslagets eget sprog:
  "omsætte kundernes behov til **værdiskabende HVAC-løsninger**", "**bindeleddet** mellem kunder,
  teknikere og interne specialister", "**energioptimeringer, opgraderinger og mindre projekter** samt
  **udbud og systemprojekter**", "**karriereskridt fra teknik til salg**", "stor frihed og indflydelse
  på egen hverdag", "erfaring fra branchen er vigtigere end erfaring med salg". Beliggenhed:
  **Hornslet** i dag, **Holme/Aarhus** fra foråret 2027, hvor JCI samler engineering-, projekt- og
  automationskompetencer (jf. JCI's egen jobtekst for projektleder i Hornslet). Samme koncern som
  #219 (Sabroe/Holme) — derfor er **intet tal og ingen formulering genbrugt** fra det dokument.

  Markedspræmis brugt i brevet (F-gasforordningen 2024/573, Tekniq/Køleteknik-vejledninger): fra
  **1. januar 2025** må fluorholdige drivhusgasser med **GWP på 2 500 eller derover** ikke bruges til
  **servicering eller vedligeholdelse**; fra **2027** er der forbud mod nye fabriksfremstillede
  **køleanlæg med GWP over 150**; **lækagekontrol** kræves på anlæg over **5 ton CO2-ækvivalenter**
  (eller 1 kg HFO) med interval **3, 6 eller 12 måneder** efter fyldning. Det gør den installerede
  base til et opgraderings- og service marked, ikke bare et nybygningsmarked.

Ingen opdigtede fakta. Dokumenteret grundlag: **eget selskab siden 2023** med fuldt **P&L**, tilbud,
kalkulation, **kundeaftaler med responstid** og service på 5 elektrikere + 3 lærlinge (ELOHVAC);
**kundeaftaler og 11 samtidige entrepriser** med 14 mand, underentreprenører og leverandører
(Ventek-Air 2022); **37 CAPEX-anlæg** med FAT/SAT, nul kritiske fund, ændringsstyring i **SAP** og
samarbejde med indkøb, teknik, drift og myndighed (Novo Nordisk 2022-2024); fire år som **ejer af
anlæggene** i 24/7-drift med HVAC, køl, pumper og SRO/SCADA (Biofos 2017-2022) — dvs. kundens side
af serviceaftalen; **12 teknikere** (ARJ 2003-2010); **elautoriseret maskinmester** LV/MV/HV
(maj 2023), **B.Tech** maskinteknik (EQF 6, 7,6/12), el- og maskinteknisk design (EQF 6) og
**køle- og VVS-teknik** (AMU 2021); dansk modersmål, engelsk professionelt; kørekort B; Måløv.
**Bevidst formulering:** ingen påstand om at være uddannet **kølemontør**, om at have **F-gas-
certifikat**, om at have solgt for en anden virksomhed end sin egen, eller om CRM-/salgsværktøjer
(opslaget tilbyder selv at lære dem). Flytning til Aarhus-området står som forudsætning, fordi
stillingen er baseret i Hornslet og flytter til Holme.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Sales Engineer · HVAC og køl · teknik, kunder og forretning'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("10. november 2026")
    m.meta("Sales Engineer, HVAC · Johnson Controls · Hornslet (Holme, Aarhus fra foråret 2027)")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Sales Engineer til HVAC og køl", bold=True, color='1A1A1A')
    m.para("Kære Iben,", after=60)

    # ---------------------------------------------------------------- side 1
    m.para("**Tre påstande, som rollen kan gøres op på.** En **HVAC**-ordre bliver ikke vundet på, "
           "hvad anlægget koster, men på hvad det koster at drive i ti år. Den sælger, der kan sige "
           "nej til det forkerte anlæg, får det næste opkald. Og **service** er ikke en omkostning "
           "ved siden af salget — det er den del af tilbuddet, kunden køber igen. Jeg har prøvet "
           "alle tre, og jeg har prøvet dem fra begge sider af bordet.", after=80)

    m.para("Hos **Johnson Controls** er rollen beskrevet som **bindeleddet** mellem kunder, teknikere "
           "og specialister — med **Engineering**, **Procurement** og **Operations** i ryggen. Det "
           "er præcis den rolle, jeg har stået i, før jeg fik titlen: Jeg har ejet et selskab med "
           "**P&L**, **ordrebog** og serviceaftaler siden 2023, og jeg har siddet på den anden side "
           "og købt de samme ydelser ind. Nu vil jeg gerne gøre det for en forretning, hvor "
           "**Systems**-projekter og den installerede base er lidt større end min egen. Og jeg kommer "
           "med det, I selv kalder det vigtigste: erfaring fra den **tekniske** del af branchen — "
           "med **Sabroe** som det navn, dansk køleteknik stadig måles op imod.", after=80)

    m.para("**Kunden.** Her bliver et ønske til et **behov** — ikke en bestilling på et bestemt mærke. Det "
           "kræver, at man tør spørge, hvad lokalet bruges til, hvor mange timer det kører, og hvem "
           "der står med det om fem år. I eget selskab har jeg haft **kundeaftaler** med fast "
           "**responstid** og skrevet ned, hvad der var lovet — også da svaret var, at det blev "
           "dyrere end håbet. En kunde, der har prøvet det én gang, køber hellere af den, der "
           "sagde det, end af den, der lovede for meget.", after=80)

    m.para("**Teknikken.** En **løsning**, der ikke kan serviceres, bliver en rabat, man giver i tre "
           "år. Jeg har **dimensioneret** køl og varme, valgt komponenter og prøvet anlæggene af "
           "med FAT/SAT på 37 anlæg. Det betyder ikke, at jeg kan alt om kølemaskiner; det betyder, "
           "at når **Engineering** siger, at det ikke kan lade sig gøre, kan jeg spørge hvorfor — og "
           "når de har ret, siger jeg det til kunden.", after=80)

    m.para("**Tilbuddet.** Et **tilbud** er en kontrakt i kladde: hver linje, der står i det, bliver "
           "lovet. Jeg har lavet **tilbud** og kalkulation på egen regning i tre år og set, hvad der "
           "sker, når en post var sat for lavt — det betaler man selv. Derfor prissætter jeg "
           "**energioptimering** og **opgraderinger** på driftstal og ikke på mavefornemmelse, og "
           "jeg skriver forudsætningerne ind, hvor kunden kan læse dem.", after=80)

    m.para("**Kontrakten.** **Udbud** og **kontrakter** bliver først gode, når indkøb, teknik og "
           "drift har læst dem med samme briller. Jeg har kørt 37 anlægsprojekter med "
           "ændringsstyring i **SAP**, leverandører og myndighed om bordet og lært, at den "
           "kommercielle koordinering er det, der afgør, om en sag ender som en reference eller som "
           "en tvist. I **Systems**-forretningen er det samme øvelse i større skala: flere "
           "parter, længere løbetid og en kunde, der kun ser én leverandør — os.", after=80)

    m.para("**Driften.** Her bliver ordren til næste ordre. Jeg har været **anlægsejer** i fire år "
           "og ved, hvad en **serviceleder** bliver målt på: at anlægget kører, at **eftersyn** er "
           "overholdt, og at der er en, der tager telefonen. Og jeg ved, at reglerne flytter "
           "markedet: siden 2025 må **F-gas** over 2 500 GWP ikke bruges til **service**, "
           "**lækagekontrol** skal ske hvert 3., 6. eller 12. måned efter fyldning, og fra 2027 må "
           "nye anlæg ikke fyldes med over 150 GWP. Den **installerede base** skal altså opgraderes "
           "— og den, der kender anlæggene, får ordren.", after=80)

    m.para("**Hvad jeg ikke er.** Jeg er ikke uddannet **kølemontør** og har ikke "
           "**F-gas**-certifikatet; min vej ind er el-teknisk og maskinteknisk med **køle- og "
           "VVS-teknik** som fag. Til gengæld har jeg solgt, prissat og leveret i eget navn, og "
           "jeg ved, hvad en ordre koster, når den bliver dyr. **Dansk** som modersmål, "
           "**engelsk** professionelt.", after=80)

    m.para("**Praktisk.** Jeg bor i Måløv, og **Hornslet** er omkring tre timer væk — det er en "
           "**flytning**, ikke en pendling, og med udsigten til **Holme** i 2027 er der ingen grund "
           "til at vente med at tage den. **Elautoriseret maskinmester** (LV/MV/HV), B.Tech i "
           "maskinteknik. **Kørekort B.** Kan tiltræde efter aftale.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Teknisk sælger med eget selskab og fuldt **P&L** siden 2023: tilbud, kalkulation, "
           "**ordrebog** og serviceaftaler med fast responstid — oven på tyve år i køl, varme og "
           "eltekniske anlæg. Har dimensioneret og afleveret 37 anlæg og har selv været kunde og "
           "anlægsejer i fire år, så jeg ved, hvad der bliver købt igen.", after=80)

    m.section("SALG, TILBUD OG KUNDER")
    for label, body in [
        ("Salgsproces",
         "Fra første kontakt til afsluttet ordre i eget selskab: behovsafdækning, beregning, tilbud, "
         "forhandling og opfølgning — med egen margin på spil."),
        ("Tilbud og kalkulation",
         "Tilbud bygget på timer, materialer, risiko og driftsomkostning; forudsætninger skrevet "
         "ind, så de kan læses af kunden og af den, der skal udføre."),
        ("Kunderelationer",
         "Serviceaftaler med fast responstid og skriftlige vilkår; kunder, der ringer igen, fordi de "
         "ved, hvad de får — ikke fordi de fik en rabat."),
    ]:
        m.bullet(label, body)

    m.section("HVAC, KØL OG TEKNISK GRUNDLAG")
    for label, body in [
        ("Løsninger",
         "Køleanlæg, varmeflader, ventilation og styring dimensioneret efter driftstimer og "
         "belastning — en løsning, der kan serviceres, ikke kun sælges."),
        ("Energioptimering",
         "Opgraderinger solgt og udført på målinger: energiforbrug, delftast og driftstid før og "
         "efter, ikke på et skøn."),
        ("Test og overlevering",
         "FAT/SAT og sekvenser på 37 anlæg med nul kritiske fund — det, der gør en reference til en "
         "reference."),
    ]:
        m.bullet(label, body)

    m.section("KONTRAKT, UDBUD OG SAMARBEJDE")
    for label, body in [
        ("Udbud og kontrakter",
         "Ændringsstyring i SAP, leverandørkrav og kontraktlige grænseflader mod indkøb, teknik og "
         "drift på 37 CAPEX-projekter."),
        ("Tværfagligt salg",
         "Tilbud lagt sammen med teknik, indkøb og drift, før det gik til kunden — så prisen holdt, "
         "da ordren blev udført."),
        ("Kundens side",
         "Fire år som anlægsejer i 24/7-drift: bestilt, modtaget og betalt for de samme ydelser, jeg "
         "nu sælger."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Ejer / teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · fuldt P&L · tilbud, ordrebog og serviceaftaler")
    m.bullet("Salg og leverance i samme person",
              "Kundeaftaler med responstid, pris og vilkår; nul kritiske afvigelser i "
              "serviceaftalerne og en ordrebog, der blev leveret, som den var solgt.")

    m.job("Senior idriftsættelsesingeniør / projektleder",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024",
          scope="37 anlægsprojekter · 25 specialister · indkøb, teknik og drift · SAP")
    m.bullet("Kommerciel koordinering",
              "Ændringer prissat og godkendt før arbejdet, kontraktlige grænseflader holdt adskilt, "
              "og dokumentation der bestod myndighedens gennemlæsning.")

    m.job("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · kundeaftaler og leverandører")
    m.bullet("Elleve kunder, elleve aftaler",
              "Fremdrift, pris og ændringer holdt adskilt pr. sag, så ingen kunde betalte for en "
              "andens forsinkelse.")

    m.job("Drifts- og vedligeholdelseschef", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="Renseanlæg i 24/7-drift · HVAC, køl, pumper, HV-tavler, SRO/SCADA")
    m.bullet("Anlægsejerens blik",
              "Serviceaftaler, eftersyn og leverandører styret i fire år — den erfaring, der gør et "
              "tilbud troværdigt.")

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
    m.edu("Køle- og VVS-teknik (AMU) · Lean: 5S, PDCA, VSM, A3 · STCW-sikkerhed",
          "Mercantec 2021 · Søfartsstyrelsen 2021–2023")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("**Dansk:** modersmål · **Engelsk:** professionelt, skriftligt og mundtligt · "
           "**Persisk:** modersmål · **Bor i Måløv** og søger stillingen med **flytning til "
           "Aarhus-området** for øje · **Kørekort B** · **Kan tiltræde efter aftale** · Referencer "
           "efter aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA ORDREBOG TIL INSTALLERET BASE",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–2",
             "Læs de sidste tolv måneders tilbud og ordrer: hvad blev vundet, hvad blev tabt, og "
             "til hvem. Kør med to **serviceledere** og se de tyve største anlæg i den installerede "
             "base."),
            ("Dag 30",
             "En liste over de kunder, hvor der er et konkret **opgraderings**- eller "
             "**energioptimerings**behov — med anlæg, fyldning, **eftersyn** og en anslået værdi i "
             "kroner. Gennemgået med **Engineering** og **Procurement**, før den går til kunden."),
            ("Dag 60",
             "To **systemprojekter** i tilbud, hvor teknik, indkøb og drift har læst kalkulationen, "
             "før den blev sendt; og en fast møderække med **tilbudsberegning** om, hvad der bliver "
             "spurgt om."),
            ("Dag 90",
             "En ordrebog med kendt **margin** og kendt leveranceevne, en plan for hvilke kunder der "
             "skal have et **service**eftersyn som indgang til næste salg — og et tal på, hvor lang "
             "tid et tilbud tager fra behov til underskrift."),
        ],
        widths=(1500, 8830))

    m.section("ET TILBUD ER EN KONTRAKT I KLADDE")
    m.para("Det, der står i tilbuddet, bliver lovet. Står der ikke, hvad der er inkluderet, bliver "
           "det forhandlet senere — og der er kunden allerede i gang. Derfor skriver jeg "
           "forudsætninger, fravalg og hvad der sker ved ændringer ind i tilbuddet, mens det stadig "
           "er et tilbud. Det koster en halv time og sparer en samtale om tre måneder.", after=70)

    m.section("DEN DYRESTE RABAT ER DEN, DER BETALER EN FEJL")
    m.para("En rabat er let at give og svær at tjene ind igen, hvis anlægget samtidig skal køre i "
           "tyve år. Jeg har prissat ud fra driftstimer og levetid, ikke kun "
           "indkøbspris, og jeg har hellere tabt en ordre end solgt en **løsning**, der ville koste "
           "kunden penge hver måned. Det er den slags, der giver genkøb i stedet for genforhandling.", after=70)

    m.section("SERVICEFORRETNINGEN ER SALGSARGUMENTET — IKKE BILAGET")
    m.para("Reglerne har gjort den installerede base til et marked: **F-gas**-grænserne flytter "
           "anlæggene, **lækagekontrol** og **eftersyn** skaber faste besøg, og et anlæg, der er "
           "opgraderet, er et anlæg, kunden kender. Sælgeren, der kan fortælle kunden, hvornår "
           "anlægget skal skiftes, og hvad det koster at vente, får opgaven. Sælgeren, der kun "
           "kommer med et tilbud, får den næste runde som prisforhandling.", after=70)

    m.section("SÆLGEREN SKAL KUNNE SIGE NEJ — OG SIGE DET TIDLIGT")
    m.para("Det er dyrere at trække et tilbud tilbage end at lade være med at sende det. Når "
           "**Engineering** siger, at et anlæg ikke kan levere det, kunden beder om, er det min "
           "opgave at sige det samme på dansk — med et alternativ i hånden. Jeg har prøvet at være "
           "den, der måtte sige det til en kunde, og jeg har prøvet at være den, der ikke gjorde "
           "det. Den første samtale er kortere.", after=70)

    m.section("KUNDEN KØBER EN DATO, IKKE EN RABAT")
    m.para("Leveringstid og opstart er en del af produktet. Et anlæg, der kommer tre uger for sent, "
           "koster kunden mere end rabatten. Derfor lover jeg datoer, som "
           "**Operations** kan holde, og jeg skriver dem ind med det samme forbehold, som teknikken "
           "giver mig — ikke med et håb.", after=70)

    m.section("HVOR JEG VILLE STARTE")
    m.para("I ordrebogen og i den installerede base. Første uge: læs de sidste tolv måneders tilbud "
           "og find ud af, hvorfor de tabte sager blev tabt — pris, teknik eller tid. Derefter tage "
           "de tyve største anlæg, finde ud af, hvad de kører på, og hvornår **F-gas**-reglerne "
           "tvinger en beslutning. Det er der, den næste ordre ligger, og det er der, jeg kan vise "
           "en **margin** frem for en aktivitet.", after=0)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "DET EFTERSPØRGER DE — DET HAR JEG",
        ["Krav i opslaget", "Dokumentation"],
        [
            ("Omsætte kundernes behov til **værdiskabende HVAC-løsninger**",
             "Behovsafdækning, **beregning** og **løsninger** solgt i eget selskab siden 2023 — og "
             "37 anlæg leveret, hvor kravet blev oversat til teknik, før prisen blev sat."),
            ("**Rådgive** kunder om **HVAC**- og **køl**eløsninger",
             "Tyve år i køl, varme og eltekniske anlæg; **køle- og VVS-teknik** (AMU) oveni "
             "maskinmester- og B.Tech-niveauet, og fire år som anlægsejer."),
            ("Udarbejde **tilbud** og drive **salgsprocessen** fra første kontakt til afsluttet "
             "**ordre**",
             "Fuldt **P&L** i tre år: behov, tilbud, forhandling, ordre og opfølgning — med egen "
             "**margin** på spil ved hver underskrift."),
            ("Identificere muligheder for **energioptimering**, **opgraderinger** og "
             "**systemprojekter**",
             "Opgraderinger solgt på målinger og **F-gas**-grænser: hvornår anlægget skal skiftes, "
             "hvad det koster at vente, og hvad kunden sparer."),
            ("Håndtere **udbud** og **kontrakter** i samarbejde med **Engineering**, **Procurement** "
             "og **Operations**",
             "37 CAPEX-projekter med ændringsstyring i SAP, leverandørkrav og grænseflader mod "
             "indkøb, teknik og drift; kontrakt læst af alle tre, før den blev underskrevet."),
            ("Bidrage til **Systems**-forretningen og sikre **kommerciel** koordinering på tværs af "
             "kontrakt, indkøb og drift",
             "Tilbud lagt sammen med teknik, indkøb og drift, før det gik til kunden — så prisen "
             "holdt, da ordren blev udført."),
            ("Udvikle stærke **kunderelationer** og skabe ny **forretning**",
             "Serviceaftaler med fast responstid og kunder, der ringer igen; nyt salg kommet fra "
             "eksisterende anlæg, ikke fra annoncer."),
            ("Erfaring fra den **tekniske** del af branchen",
             "Tyve år: **elautoriseret maskinmester** (LV/MV/HV), **B.Tech** maskinteknik, "
             "**køle-/VVS-teknik** — fra værksted og tavle til anlæg i 24/7-drift."),
            ("Erfaring med **HVAC**-, **køle**- eller **serviceforretningen**",
             "Egen **serviceforretning** siden 2023 med aftaler og responstid; fire år som "
             "**anlægsejer** med HVAC, køl og pumper i døgndrift."),
            ("Trives med **kundekontakt** og relationsopbygning",
             "Kundeaftaler forhandlet i eget navn i tre år, og elleve samtidige kunder i "
             "Ventek-Air-perioden — uden at nogen betalte for en andens forsinkelse."),
            ("Nysgerrig på **forretning** og kan omsætte muligheder til konkrete **løsninger**",
             "Ordrebog, **margin** og indtjening fulgt måned for måned i eget selskab — "
             "forretningssans med regnskab bag, ikke med slides."),
            ("Kommunikerer professionelt på **dansk** og **engelsk**",
             "**Dansk** modersmål, **engelsk** professionelt skriftligt og mundtligt; **global** "
             "organisation er ikke et fremmedsprog for mig."),
            ("Baggrund som **køletekniker**, **HVAC-tekniker**, **serviceleder** eller lignende",
             "**Drifts- og vedligeholdelseschef** med HVAC, køl og pumper i fire år, elektromekaniker "
             "i bunden og **køle-/VVS-teknik** som fag — ikke uddannet kølemontør."),
            ("Bygge bro mellem den **tekniske** og **kommercielle** del af forretningen",
             "Samme person har regnet, solgt og afleveret: teknik, pris og leverance besluttet ved "
             "samme bord, på 37 anlæg og i eget selskab."),
            ("Tæt samarbejde med **serviceledere**, **teknikere** og specialister inden for "
             "**Engineering**, **tilbudsberegning**, **Procurement** og **Operations**",
             "Tværfaglige fora med indkøb, teknik, drift og myndighed; tilbudsberegning læst "
             "igennem, før tilbuddet blev sendt."),
            ("Arbejde med både **forretning** og større projekter",
             "37 CAPEX-anlæg og 11 samtidige entrepriser ved siden af den daglige drift — store "
             "sager uden at miste de små."),
            ("Stor frihed og indflydelse på egen hverdag",
             "Eget selskab drevet selvstændigt i tre år: prioritering, kunder og kalender styret "
             "uden en bagkant — og leveret alligevel."),
            ("Baseret i **Hornslet** — fra foråret 2027 **Holme**, **Aarhus**",
             "Bor i Måløv i dag og søger med **flytning** til **Aarhus**-området for øje; "
             "**kørekort** B og klar til fremmøde fra første dag."),
        ],
        widths=(3600, 6746))

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_JohnsonControls_SalesEngineerHVAC.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_JohnsonControls_SalesEngineerHVAC.docx'))
