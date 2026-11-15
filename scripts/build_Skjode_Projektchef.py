# -*- coding: utf-8 -*-
"""H. Skjøde Knudsen A/S — projektchef, totalentrepriser på Sjælland.

Dansk opslag → dansk dokument (da-DK): ansøgning side 1, CV side 2, uddannelse + 90 dage +
fire afsnit side 3, kravmatrix side 4.

STILVALG (master/STILREGISTER.md; godkendt af scripts/style_guard.py, 3/3 skift mod #199):
  register      = ENTREPRENØR — byggeplads, fremdrift, kalkulation, håndværk. Rollen er
                  projektchef i en udførende totalentreprenør, hvor økonomien afgøres i
                  kalkulation og projektering. Sidst brugt #194.
  åbningsgreb   = A (PLACEN/MISPLACERINGEN) — beslutningen tages et andet sted, end man tror:
                  en totalentreprise bliver afgjort i kalkulationen og projekteringen, ikke på
                  byggepladsen. Sidst brugt #189.
  struktur      = ORDLISTEN — virksomhedens egne begreber oversat til praksis: ordholdenhed,
                  ordentlighed, åben og sund dialog, frihed under ansvar, købmandskab,
                  troværdighed. Sidst brugt #192.

Ingen opdigtede fakta: der påstås IKKE uddannelse som bygningsingeniør/bygningskonstruktør,
ikke projektchefansvar på 200–500 mio. kr., ikke DGNB-certificering som ansvar og ikke ledelse
af byggeledere/projekteringsledere i en totalentreprise. Det dokumenterede grundlag er fuldt
P&L i egen virksomhed, 37 samtidige CAPEX-projekter, 11 entrepriser med 14 mand, AB 18/ABT 18
som underentreprenør, arbejdsmiljø (LOTO/APV) og nul kritiske fund ved aflevering.

Policy: master/README.md — jobbet først, kandidaten kun som bevis, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Projektchef · Totalentrepriser, Sjælland'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4. november 2026")
    m.meta("H. Skjøde Knudsen A/S · Projektchef, totalentrepriser · Blækhatten 27, 5220 Odense SØ")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: projektchef — totalentrepriser på Sjælland", bold=True, color='1A1A1A')
    m.para("Til Gert Breinholt, UnikRecruitment — videre til H. Skjøde Knudsen A/S", after=70)

    # ---------------------------------------------------------------- side 1
    m.para("**En totalentreprise bliver ikke afgjort på byggepladsen.** Den bliver afgjort i "
           "**kalkulation**en og i **projektering**en, længe før den første mur står — og den "
           "bliver afgjort igen den dag, nogen opdager, at en forudsætning ikke holder. Det er "
           "derfor, en **projektchef**s vigtigste værktøj ikke er byggepladsen, men de aftaler, "
           "der blev lavet, før den blev indrettet. Jeg søger rollen, fordi det er den slags "
           "ansvar, jeg har arbejdet mig mod i ni år: entreprise, økonomi og **aflevering** i "
           "samme hånd.", after=80)

    m.para("**Ordholdenhed.** Det er jeres første ord i opslaget, og det er det rigtige sted at "
           "begynde. En **totalentreprise** er et løfte med en dato på: det, der stod i tilbuddet, "
           "er det, bygherren skal have — og hvis det ikke kan holde, skal beskeden komme fra os, "
           "før bygherren opdager det. Siden 2023 har jeg drevet egen virksomhed med fuldt "
           "P&L-ansvar, og der er ingen at gemme sig bag: enten holder **kalkulation**en, eller "
           "også siger man det i tide. Det er den vane, jeg tager med ind i en **byggesag** på "
           "300 mio. kr.", after=80)

    m.para("**Ordentlighed.** I byggeri er ordentlighed noget meget konkret: en kalkulation, som "
           "en anden kan læse; et **aftalegrundlag**, hvor forbehold og grænseflader er gennemgået "
           "før underskrift; og en **afleveringsforretning**, hvor **mangelliste**n bliver lukket, "
           "og hvor **1-års gennemgang** ikke bliver en overraskelse for nogen. Jeg har arbejdet "
           "med **AB 18** og **ABT 18** som underentreprenør, med **IKT** og **KS** i projekter, "
           "hvor dokumentationen skulle kunne bruges af en tredjemand, og med **byggelovgivning** "
           "så langt den rammer en **byggeplads** i drift — ikke som paragraf, men som krav.", after=80)

    m.para("**Åben, sund dialog.** Der er altid en periode i en **byggesag**, hvor det ser skævt "
           "ud: en kalkulation, der strammer, en **projektering**, der halter, en "
           "**underentreprenør**, der ikke leverer. Pointen med åben dialog er ikke at være enig "
           "med alle — den er, at den, der bliver ramt, hører det fra os og ikke fra en videresendt "
           "mail fra bygherren. Jeg har ført den samtale med 25 specialister på 37 projekter og "
           "med kunder i egen virksomhed, og den er lettere i uge 4 end i uge 40.", after=80)

    m.para("**Frihed under ansvar.** Det ord betyder kun noget, hvis mandatet er reelt, og hvis "
           "rapporteringen er ærlig. Jeg er vant til at træffe **beslutning**er tæt på udførelsen "
           "— i egen virksomhed er der ingen mellem mig og konsekvensen — og jeg er lige så vant "
           "til at melde status opad, når den ikke er pæn. Frihed uden den slags rapportering er "
           "ikke frihed; det er bare uopdaget **risiko**.", after=80)

    m.para("**Købmandskab.** **Købmandskab** i en **entreprenørvirksomhed** er ikke at presse "
           "priser. Det er at vide, hvor i en **totalentreprise** pengene bliver tjent eller "
           "tabt. Efter min erfaring ligger risikoen sjældent i betonen — den ligger i de fag, "
           "ingen i kalkulationen havde tid til at regne på: el, styring, ventilation og køl, og "
           "i grænsefladerne mellem dem. Der er jeg hjemme: **elautoriseret maskinmester** "
           "(LV/MV/HV), el- og maskinteknisk design (EQF 6) og ni år med at få de fag til at gå "
           "op i **tidsplan** og budget.", after=80)

    m.para("**Hovedentreprise eller totalentreprise.** Forskellen er, hvem der ejer "
           "**projektering**en. I en **hovedentreprise** kan man henvise til en rådgiver, når en "
           "detalje ikke holder; i en **totalentreprise** er det os, og derfor skal "
           "**projekteringsleder**en og **byggeleder**en sidde i samme rum fra dag ét. Det er den "
           "forskel, jeg gerne vil være **projektchef** på.", after=80)

    m.para("**Det, jeg ikke har.** I skriver, at ambitionen er at være Danmarks mest "
           "troværdige entreprenørvirksomhed, og det er ikke et ord, man skriver om sig selv i en "
           "ansøgning — det er antallet af løfter, der holdt. Derfor skal det også stå klart, "
           "hvad jeg ikke har: jeg er ikke **bygningsingeniør** eller **bygningskonstruktør**, "
           "jeg har ikke ført en **totalentreprise** på 300 mio. kr., og jeg har ikke været "
           "certificeringsansvarlig for **DGNB**. Det, jeg har, er ni år i entreprise, anlæg og "
           "reguleret produktion, fuldt P&L i egen virksomhed og 37 CAPEX-projekter, hvor "
           "**økonomistyring**, **kontrakt**er og aflevering var mit ansvar.", after=80)

    m.para("**En sjællandsk afdeling, der skal kunne det samme to gange.** I skriver, at I har "
           "projekter på vej på **Sjælland**, og at I er midt i en udvikling. Det, en "
           "**projektchef** kan bidrage med der, er ikke en helt ny metode, men at den samme "
           "**byggesag** bliver grebet ens hver gang: samme kalkulationsgrundlag, samme "
           "**opfølgning** på **fremdrift**, samme måde at lukke en **mangelliste** på. Jeg bor i "
           "Måløv, Sjælland er en halv time væk, og jeg kan tiltræde snarest.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Projektleder og entreprenør med ni års ansvar for **entreprise**, økonomi og "
           "**aflevering** i byggeri, anlæg og reguleret produktion — **elautoriseret "
           "maskinmester** (LV/MV/HV), el- og maskinteknisk design (EQF 6), B.Tech i "
           "teknologiledelse og maskinteknik. Fuldt P&L i egen virksomhed siden 2023, 37 "
           "samtidige CAPEX-projekter med **tidsplan**, budget og **risiko**opfølgning, 11 "
           "samtidige entrepriser på DKK 2–10 mio. med 14 mand — og nul kritiske fund ved "
           "aflevering.", after=80)

    m.section("ENTREPRISE, KALKULATION OG KONTRAKT")
    for label, body in [
        ("Kalkulation og tilbud",
         "Tilbudsberegning og kalkulation med egen risiko; forbehold, mængder og grænseflader "
         "skrevet ind, før prisen blev givet — og en pris, der blev sagt nej til, når den ikke "
         "kunne bære."),
        ("Aftalegrundlag og forhandling",
         "AB 18 og ABT 18 i praksis som underentreprenør og som leverandør til større "
         "entreprenører; IKT-aftaler, forsikring og ansvarsgrænser gennemgået før underskrift."),
        ("Ændringer og krav",
         "Ændringer beskrevet, prissat og godkendt skriftligt, mens de var små; krav mod "
         "bygherre og krav fra underentreprenører holdt ude af hinanden, så en sag ikke blev "
         "til en forhandling om alt."),
    ]:
        m.bullet(label, body)

    m.section("ØKONOMI, FREMDRIFT OG AFLEVERING")
    for label, body in [
        ("Økonomistyring",
         "Budget og prognose opdateret månedligt i SAP ERP på 37 projekter; afvigelser forklaret "
         "med årsag og handling, før de blev en overraskelse i regnskabet."),
        ("Fremdrift og milepæle",
         "Få hårde **milepæle**, synlig kritisk vej og ugentlig opfølgning, der er kort nok til "
         "faktisk at blive lavet; daglige tavlemøder og flaskehalsanalyser på 11 samtidige "
         "entrepriser."),
        ("Aflevering og mangellukning",
         "Afleveringspakker, prøvekørsel og dokumentation aftalt undervejs; **mangelliste** "
         "lukket med rodårsag, og **1-års gennemgang** forberedt, før garantien blev aktuel."),
        ("Kvalitetssikring",
         "KS-plan, tjeklister og egenkontrol pr. fag; afvigelser registreret og lukket, ikke "
         "forklaret væk. Nul kritiske fund ved aflevering i GMP-reguleret byggeri."),
    ]:
        m.bullet(label, body)

    m.section("LEDELSE AF PROJEKTTEAM OG FAG")
    for label, body in [
        ("Projektteam og faglig sparring",
         "25 specialister på tværs af engineering, indkøb og anlæg ledet gennem "
         "faste møder og tydelige beslutningspunkter; **personaleledelse** med MUS, 1:1 "
         "og kompetencematrix."),
        ("Byggeledere og formænd",
         "14-mands entrepriseteam og fem elektrikere plus tre lærlinge ledet på skiftende "
         "**byggeplads**er; situationsbestemt ledelse (SLII) og delegering med klart mandat."),
        ("Arbejdsmiljø i byggefasen",
         "LOTO, APV, risikovurdering ved pladsopstart og sikkerhedsrunder; arbejdsmiljø koordineret, "
         "når flere fag arbejder i samme rum — det er et krav, ikke et banner."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Ejer / teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · fuldt P&L · udbud, kalkulation og leverandører")
    m.bullet("Forretning og entreprise i egen hånd",
              "Projekter fra tilbud til aflevering med eget budget og egen risiko; udbud, "
              "underentreprenører og KS — og ansvaret for at sige nej, når kalkulen ikke holdt.")

    m.job("Senior idriftsættelsesingeniør / projektleder, elsystem",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024",
          scope="37 samtidige CAPEX-projekter · 25 specialister · GMP/FDA/EMA")
    m.bullet("Fremdrift, økonomi og overdragelse",
              "Projektgrundlag, milepæle og månedsrapportering i SAP ERP; FAT/SAT og IQ/OQ/PQ med "
              "protokoller skrevet før testen, og aflevering med nul kritiske fund.")

    m.job("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · DKK 2–10 mio.")
    m.bullet("Koordinering i pressede uger",
              "Daglige tavlemøder og flaskehalsanalyser; omfordeling af mandskab og leverandører, "
              "når en entreprise trak mere end planlagt — med bygherre informeret samme dag.")

    m.job("Vedligeholdelses- og driftsleder", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="Renseanlæg i 24/7-drift · pumper, HVAC, højspændingstavler, SCADA")
    m.bullet("Anlæg, der ikke må stoppe",
              "Forebyggende vedligehold og akut fejlfinding i døgndrift; udfald planlagt i smalle "
              "vinduer, 5S og standard work, LOTO og APV.")

    m.job("Elektromekaniker / produktionsteamleder",
          "ARJ Engineering · Teheran · dec. 2003–mar. 2010 · 12 mekanikere og teknikere")

    # ---------------------------------------------------------------- side 3
    m.page_break()
    m.section("UDDANNELSE OG AUTORISATION")
    m.edu("Elautoriseret maskinmester — dansk elautorisation LV/MV/HV",
          "Sikkerhedsstyrelsen · maj 2023")
    m.edu("B.Tech, teknologiledelse og maskinteknik (EQF 6)",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12")
    m.edu("El- og maskinteknisk design, elteknik (EQF 6)", "Tehran Technical University · 2000–2003")
    m.edu("Køleteknik & klimaanlæg (AMU) · Lean: 5S, PDCA, VSM, A3",
          "Mercantec · 2021 · STCW sikkerhedskurser (2021–2023)")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("**Dansk:** modersmål · **Engelsk:** professionelt, skriftligt og mundtligt · **Persisk:** "
           "modersmål · **Bosat i Måløv** — halv time til Sjælland · **Kan tiltræde snarest** · "
           "Referencer efter aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA OVERTAGET SAG TIL FØRSTE AFLEVERING",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–2",
             "Læse jeres **projektmodel** og de igangværende **byggesager** igennem som tilhører: "
             "hvor står **risiko**en, hvad er sidste godkendte ændring, og hvornår blev "
             "**byggeleder**en sidst spurgt om noget, der ikke stod i planen?"),
            ("Dag 30",
             "Overtage en afgrænset sag med **tidsplan**, kalkulation og **interessent**er; første "
             "**økonomistyring** i jeres format og en aftale med **projektering**en om, hvornår et "
             "projekt er færdigt nok til at blive bygget."),
            ("Dag 60",
             "Egen portefølje og et forslag til én ting, vi gør ens i alle sager — fx hvordan "
             "ændringer godkendes, eller hvordan **KS** og **aflevering** bliver samme dokument "
             "hver gang."),
            ("Dag 90",
             "Første **afleveringsforretning** gennemført efter jeres standard, og status med dig "
             "på, hvad jeg bærer selv, og hvor jeg stadig skal have et fagligt blik fra en kollega."),
        ],
        widths=(1500, 8830))

    m.section("EN KALKULATION ER ET LØFTE, IKKE ET GÆT")
    m.para("Når en **totalentreprise** taber penge, er det sjældent, fordi nogen var uærlig. Det er, "
           "fordi nogen regnede på det, de kunne, og gættede på resten. Jeg har siddet med den "
           "anden side af bordet i ni år: som underentreprenør, der skulle levere et tilbud, og som "
           "den, der skulle stå med kalkulen bagefter. Det giver en vane med at spørge, hvor de "
           "sidste ti procent af prisen ligger — og med at skrive forbeholdet ind, mens det stadig "
           "er et forbehold og ikke en tvist.", after=70)

    m.section("PROJEKTERINGEN AFGØR, HVAD BYGGERIET KOSTER")
    m.para("En **projekteringsleder** kan spare en byggesag for mere, end en byggeleder kan "
           "indhente. Det er i **projektering**en, at en løsning bliver dyr at udføre, og det er "
           "der, grænsefladerne mellem fag bliver aftalt eller glemt. Jeg har ikke været "
           "projekteringsleder i en totalentreprise, men jeg har projekteret og prissat "
           "el-entreprise selv, siddet i **IKT**-processer og set, hvad en uafklaret grænseflade "
           "koster i uge 50. Den samtale vil jeg ind i tidligt — med **projekteringsleder**en, "
           "ikke om den.", after=70)

    m.section("ET MANDAT, EN BYGGELEDER KAN BRUGE")
    m.para("En **byggeleder** skal kunne træffe en beslutning på pladsen uden at ringe tre gange. "
           "Det kræver, at rammen er skrevet ned på forhånd: hvad må koste hvad, hvem bestemmer "
           "over hvad, og hvornår skal jeg have en **beslutning** fra dig. Jeg har ledet "
           "14-mands entrepriseteam og en gruppe på fem elektrikere og tre lærlinge, og jeg har "
           "lært, at mandat gives med et tal og en grænse — ikke med tillid alene. Tillid er det, "
           "der gør, at mandatet bliver brugt.", after=70)

    m.section("TONEN PÅ PLADSEN ER EN DEL AF STYRINGEN")
    m.para("På en **byggeplads** får man først sandheden om **fremdrift**en, når tonen er god nok "
           "til, at en formand tør sige, at han er bagefter. Jeg har prøvet det med 14 mand og "
           "daglige tavlemøder, hvor tallene stod på tavlen, og hvor det var tilladt at sige, at "
           "ugen var gået skævt. Uformel omgangstone er ikke et pusterum fra økonomien — det er "
           "det, der gør, at økonomien bliver meldt ærligt ind. Den slags arbejdsplads holder man "
           "ved at stille op, sige tak og tage sin del, når noget ikke holdt.", after=70)

    m.section("DET JEG IKKE HAR GJORT ENDNU")
    m.para("Min uddannelse er ikke **bygningsingeniør** eller **bygningskonstruktør**, og det skal "
           "man vide, når man ansætter en **projektchef** til en sag på 300 mio. kr. Det, jeg har i "
           "stedet, er el- og maskinteknisk design (EQF 6) og en B.Tech i teknologiledelse — og ni "
           "år, hvor jeg har læst tegninger, mængder og tilbud for at kunne prissætte og bygge det, "
           "andre havde **projekteret**. Skalaen ændrer tallet, ikke rækkefølgen: kalkule, "
           "**kontrakt**, udførelse, **mangelliste**, **aflevering**. Det er en påstand, der skal "
           "bevises i praksis, og det er den slags, en prøvetid er til.", after=0)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "HVAD STILLINGEN KRÆVER — HVAD JEG HAR LEVERET",
        ["Krav i opslaget", "Bevis"],
        [
            ("Teknisk uddannelse som bygningsingeniør eller bygningskonstruktør",
             "Ikke opfyldt i den form: **elautoriseret maskinmester** (LV/MV/HV), el- og "
             "maskinteknisk design (EQF 6) samt B.Tech i teknologiledelse og maskinteknik. "
             "**Byggelovgivning** og **aftalegrundlag** arbejdet med i praksis, ikke på skolebænken."),
            ("Erfaring med ledelse og styring af projektteams som projektleder eller projektchef",
             "37 samtidige CAPEX-projekter som projektleder, 11 entrepriser som projektleder med "
             "14 mand og fuldt P&L-ansvar i egen virksomhed siden 2023."),
            ("Erfaring med totalentrepriser",
             "**Totalentreprise** og **hovedentreprise** prøvet fra den side, der bærer "
             "risikoen: faste priser, "
             "egen kalkulation, underentreprenører og **ABT 18**-vilkår — i egen virksomhed og som "
             "underentreprenør på større sager."),
            ("Økonomistyring",
             "Budget, prognose og månedlig opfølgning i SAP ERP på 37 projekter; eget regnskab, "
             "egen likviditet og egen **kalkulation** i virksomheden."),
            ("Kontrakter og forhandlinger",
             "**Kontrakt**er, **forhandling** med underentreprenører og leverandører, forsikring og "
             "ansvarsgrænser; forbehold og grænseflader afklaret før underskrift."),
            ("Købmandskab",
             "Fuldt P&L i egen virksomhed: pris, dækning, kapacitet og risiko hænger sammen i "
             "hverdagen — og et nej til en ordre, der ikke kunne bære sig."),
            ("Kendskab til byggelovgivning",
             "**Byggelovgivning**, arbejdsmiljøregler og myndighedskrav i byggesager og "
             "el-installationer; dokumentation og tilladelser håndteret i praksis."),
            ("Byggeriets aftalegrundlag",
             "**AB 18**, **ABT 18** og **IKT** anvendt i egne sager; krav og ændringer håndteret "
             "efter aftalen og ikke efter forhandlingsstyrke."),
            ("Klar kommunikation og stærke relationer",
             "Bygherrer, entreprenører, underentreprenører og egne folk i ni år; status meldt ud, "
             "før den anden opdagede problemet — også når den var dårlig."),
            ("Interesse for bæredygtigt byggeri og certificeringer som DGNB",
             "**Grøn omstilling** arbejdet med konkret: 40 % lavere energiomkostninger via "
             "PDCA-program, solcelle- og styringsprojekter. **DGNB** har jeg ikke været "
             "certificeringsansvarlig for; det vil jeg lære af jeres ESG-funktion."),
            ("Overordnet ansvar for byggesager fra opstart til aflevering",
             "Sager båret hele vejen: tilbud, kontrakt, udførelse, **afleveringsforretning** og "
             "**1-års gennemgang** — i egen virksomhed uden nogen at skyde ansvaret på."),
            ("Kvalitet, styring og fremdrift",
             "**Kvalitetssikring** med KS-plan og egenkontrol, **fremdrift** med få hårde "
             "**milepæle** og ugentlig opfølgning, nul kritiske fund ved aflevering."),
            ("Ledelse af projektledere, projekteringsledere og byggeledere",
             "25 specialister og 14-mands entrepriseteam ledet; direkte ledelse af "
             "**byggeleder**e og **projektleder**e i den form har jeg ikke haft — jeg har været "
             "den, der blev ledet på den måde, og ved, hvad der virker."),
            ("Beslutninger i en uforudset og dynamisk hverdag",
             "11 entrepriser og 37 projekter med daglige tavlemøder og flaskehalsanalyser; "
             "omprioritering efter konsekvens, når to ting væltede samme uge."),
            ("Projekter i størrelsesordenen 200-500 mio. kr.",
             "Ikke i den størrelse: største enkeltprojekter DKK 2–10 mio., portefølje på 37 sager "
             "og egen virksomheds samlede ordrebehold. Skalaen læres i jeres organisation — "
             "metoden er den samme, tallene er større."),
            ("Ordholdenhed, ordentlighed og åben, sund dialog",
             "Det er de tre ord, dokumentet er bygget op om: aftaler holdt, sager afleveret "
             "ordentligt, og dårligt nyt meldt ud med en plan — ikke med en undskyldning."),
        ],
        widths=(3600, 6746))

    m.section("SJÆLLAND KRÆVER EN MODEL, DER KAN GENTAGES")
    m.para("At bygge på **Sjælland** fra en base i Odense er ikke bare et spørgsmål om at køre "
           "længere. Det er et spørgsmål om, at den **projektchef**, der sidder på sagen, kan "
           "træffe beslutningerne uden at skulle have dem hjem hver gang — og at det, der bliver "
           "besluttet, bliver skrevet ned, så den næste sag ikke starter forfra. Jeg har drevet "
           "virksomhed med korte beslutningsveje og ved, hvad det kræver at holde dem korte uden "
           "at miste overblikket: tal, der er opdaterede, og en **økonomistyring**, der bliver "
           "lavet hver måned, også når måneden var dårlig.", after=70)

    m.section("HVOR JEG VILLE STARTE")
    m.para("Med at læse de igangværende **byggesager** igennem og tale med **byggeleder**ne: hvor "
           "står **risiko**en, hvad er den seneste ændring, nogen har godkendt, og hvad ville de "
           "gerne have haft anderledes, da sagen startede? Derefter overtage én sag og køre den "
           "efter jeres bog, så **projektteam**et kan se, hvordan jeg arbejder, før vi skal være "
           "enige om noget fælles. Tillid i en projektorganisation kommer ikke fra et oplæg; den "
           "kommer fra den første sag, man ikke tabte.", after=0)

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_Skjode_Projektchef.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_Skjode_Projektchef.docx'))
