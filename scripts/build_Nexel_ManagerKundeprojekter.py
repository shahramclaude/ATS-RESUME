# -*- coding: utf-8 -*-
"""Manager, kundeprojekter 10-0,4 kV — Nexel (Andel), Sjælland (dansk opslag).

Dansk opslag -> dansk dokument, 4 sider: brev side 1, CV side 2, uddannelse + 90 dage +
metodeafsnit + "Hvor jeg ville starte" side 3, kravmatrix side 4. Format per master/README.md.
Opslaget beder om "ansøgning og CV hurtigst muligt" via annoncen — formen følges ikke, brevet
bliver side 1.

STILVALG (master/STILREGISTER.md; godkendt af scripts/style_guard.py, 3/3 skift mod #217):
  register      = ENTREPRENØR — byggeplads, fremdrift, kalkulation, udførelse, håndværk, aftaler
                  med entreprenører. Sidst #200.
  åbningsgreb   = F (KONSEKVENSEN) — når en tilslutning går galt, går den ikke galt i elnettet,
                  men i kalenderen. Sidst #209.
  struktur      = KUNDEREJSEN — kundens vej gennem projektet: aftalen · projekteringen ·
                  entreprisen · tilslutningen · afslutningen og næste gang. Sidst #196.
  kadence       = korte, konkrete sætninger med en person og en dato i hver anden linje.

KULTURSYNKRONISERING (policy 04.11.2026), kilder i master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md
§189:
  **Nexel** er driftselskabet for netselskaberne **Cerius** og **Radius Elnet** i **Andel**-koncernen:
  "vi bygger og varetager driften af forsyningsanlæg, der sikrer strøm til vores fælles hverdag",
  ca. **800 kollegaer**, døgnet rundt, biler med det karakteristiske X, arbejde i by og på land.
  Afdelingen for **10-0,4 kV kundeprojekter** har **4 teams** med hver sin manager og dækker hele
  Sjælland; opgaverne er **kundeaftaler, projektledelse, projektering, entreprisestyring,
  eksekvering og dokumentation**. Fokus i opslaget: effektive processer, **økonomisk styring**,
  **myndighedsrapportering** og kundens forventninger. Citater fra opslaget: **Bettina Wadsbach
  Petersen, Director** — "i din nærmeste ledergruppe får du 3 tætte kolleger … alt sammen for at løfte
  i fællesskab", og "dine ledelsesmæssige værdier bygger på synlighed og nærvær … resultatskabelse
  gennem mennesker, processer og et højt fagligt engagement". Kultur: **andelsselskab**, sammenhold,
  relationer der bunder i **tillid**, uformel tone i kantinen, ligeværdig tilgang på tværs af
  koncernen, **diversitet**, **grøn omstilling**. Andel er Danmarks ledende energi- og fibernetkoncern
  (Cerius, Radius, Clever, Energi Danmark, Fibia, Andel Energi).

  Markedskontekst (Andel-årsrapport 2025, Cerius/Radius, Installatør, Alt om Teknik): mere end
  **1,5 mio. elnetkunder** i Cerius-Radius' område; **Radius** ejer over **19.200 km kabler** og ca.
  1,1 mio. netkunder, **Cerius** ca. **25.000 km** og over 400.000 netkunder; elektrificeringen kræver
  **fire til fem nye hovedstationer om året frem mod 2030**; Nexel har indført **totalentreprise** på
  hovedstationer (15 stationer i milliardudbud med Skanstec, de første syv i drift slut 2026/løbet af
  2027) og får **700 distributionstransformere om året** fra Eaton (ca. 90 mio. kr. årligt,
  2025-2029). Funktionschef Tomas Christensen: "alle analyser viser, at efterspørgslen på strøm vil
  stige, og det betyder et øget pres på elnettet".

Ingen opdigtede fakta. Dokumenteret grundlag: elautoriseret maskinmester LV/MV/HV og el- og
maskinteknisk design (EQF 6); 37 CAPEX-anlæg som senior idriftsættelsesingeniør/projektleder med 25
specialister, FAT/SAT, nul kritiske fund, ændringsstyring i SAP og dokumentation læst af myndigheden
(Novo Nordisk 2022-2024); 14 mand, 11 samtidige entrepriser, udbud og eget værksted (Ventek-Air
2022); 5 elektrikere + 3 lærlinge med fuldt P&L, tilbud, beregning og afleveringsdokumentation
(ELOHVAC 2023-); fire år med HV-tavler, SRO/SCADA, LOTO/APV og vagtordning (Biofos 2017-2022);
12 teknikere (ARJ 2003-2010); B.Tech EQF 6 (7,6/12); dansk modersmål, engelsk professionelt;
kørekort B. **Ingen påstand om at have arbejdet med netselskabsprojekter eller 10 kV-netstationer.**
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Manager · kundeprojekter i elnettet · 10/0,4 kV'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("10. november 2026")
    m.meta("Manager · afdelingen for 10-0,4 kV kundeprojekter · Nexel")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Manager til projektafdelingen for kundeprojekter", bold=True, color='1A1A1A')
    m.para("Kære Bettina,", after=60)

    # ---------------------------------------------------------------- side 1
    m.para("**Når en tilslutning går galt, går den ikke galt i elnettet. Den går galt i "
           "kalenderen.** Kunden har sat byggeriet i gang og står med en station, der ikke er spændt "
           "op. **Entreprenøren** har folk på pladsen og venter på en besked. Og den "
           "**dokumentation**, myndigheden skal have, mangler netop det bilag, ingen spurgte efter i "
           "tide. Ingen af de fejl er elektriske. De er **arbejdsgange**, der ikke var ens — og det "
           "er den slags, en manager kan gøre noget ved.", after=80)

    m.para("**Nexel driver og udbygger elnettet for Cerius og Radius** — mere end **1,5 mio. "
           "elnetkunder**, og et **distributionsnet**, der skal bære en **grøn omstilling** og en "
           "elektrificering, som kræver "
           "fire til fem nye hovedstationer om året frem mod 2030 og omkring **700 "
           "distributionstransformere** årligt. I afdelingen for **10-0,4 kV kundeprojekter** er der "
           "fire teams, der laver den samme slags **kundeprojekter** på hele Sjælland. Det er hele "
           "pointen: når fire teams gør det samme, er den største gevinst ikke et genialt "
           "enkeltprojekt, men at **ensartede arbejdsgange** gør det kedelige mere sikkert.", after=80)

    m.para("**Aftalen.** Kundens projekt starter med et løfte: hvad bliver tilsluttet, hvad koster "
           "det, og hvem ejer datoen. Er de tre ting ikke skrevet ned, bliver de forhandlet senere — "
           "og der er kunden allerede i gang. I eget selskab har jeg lavet tilbud, beregning og "
           "**kundeaftaler** med **responstid** og fast pris, og jeg har prøvet, hvad det koster at "
           "love noget, der ikke var regnet færdigt.", after=80)

    m.para("**Projekteringen.** Her bliver økonomien afgjort, ikke i udførelsen: komponenter, "
           "**beskyttelse** og **selektivitet**, kabeldimensionering, tilladelser — og de "
           "**grænseflader** mod kundens eget anlæg, som ingen ejer, hvis ikke nogen gør det. Jeg har "
           "**projekteret** og idriftsat **tavler** og forsyning på 37 anlæg, og jeg ved, hvor ofte "
           "en ændring i **projekteringen** er billigere end en ændring i **entreprisen**. Og en "
           "**netstation** er ikke et anlæg for sig selv: den skal kobles ind i et **elnet**, der "
           "er i drift, med **koblingsanlæg**, **beskyttelse** og **måling** der passer til det, "
           "der står der i forvejen.", after=80)

    m.para("**Entreprisen.** Når **entreprenøren** står på pladsen, er **fremdrift**, **sikkerhed** "
           "og adgang de tre ting, der afgør dagen — og de skal være aftalt, før gravemaskinen "
           "kommer. Jeg har styret 11 samtidige entrepriser med 14 mand, eget værksted og "
           "underentreprenører, og jeg har kørt LOTO og APV som fast rytme, ikke som en mappe i "
           "skurvognen.", after=80)

    m.para("**Tilslutningen.** Det er her, alt det usynlige bliver synligt: **idriftsættelse**, "
           "**måling**, kontrol og den **dokumentation**, der skal kunne læses af en myndighed om "
           "fem år. Jeg har lagt FAT/SAT og sekvenser for 37 anlæg med **nul kritiske fund** ved "
           "aflevering, og jeg har set, hvad der sker, når det sidste bilag kommer efter "
           "spændingssætningen.", after=80)

    m.para("**Afslutningen og næste gang.** Et projekt er ikke slut, når det er spændt op. Det er "
           "slut, når **myndighedsrapporteringen** er afleveret, **økonomien** er gjort op, og "
           "**kundens forventninger** er indfriet eller forklaret. Og når læringen er skrevet ind i "
           "den fælles metode, så det næste projekt i samme bydel ikke starter forfra.", after=80)

    m.para("**Økonomien sidder i aftalen, ikke i regnskabet.** Bliver et kundeprojekt dyrere, er "
           "forskellen lavet tidligt: en forudsætning, ingen skrev ned, eller en ændring, der blev "
           "udført, før den blev godkendt. Jeg har fulgt aftalt pris, brugt pris og det uafklarede "
           "hver uge — ikke ved afslutningen.", after=60)

    m.para("**Teamet og ledergruppen.** 16-18 mennesker er ikke et team, fordi de sidder samme sted. "
           "Det bliver et team, når **målene** er fælles og forklaret, når **kompetenceudvikling** "
           "er en plan pr. person, og når **synlighed** og **nærvær** betyder, at man er med, hvor "
           "arbejdet sker. **Resultatskabelse** gennem mennesker og processer er ikke et slogan for "
           "mig; det er den eneste måde, en afdeling med fire teams kan blive ens uden at blive "
           "ensrettet. Jeg har siddet i ledergrupper i eget selskab og i store "
           "**anlægsprojekter** — og foretrækker den **tillid**, der gør, at uenigheden bliver sagt "
           "højt, før den bliver dyr.", after=80)

    m.para("**Praktisk.** Jeg bor i Måløv og har hele Sjælland inden for rækkevidde. "
           "**Elautoriseret maskinmester** (LV/MV/HV) med el- og maskinteknisk design i bagagen, "
           "tolv år med personaleansvar og tyve år i **projekter** og drift. **Dansk** som "
           "modersmål, **engelsk** på professionelt niveau. **Kørekort B.** Kan tiltræde efter "
           "aftale.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("El-teknisk projekt- og driftsleder med tolv års personaleansvar. 37 "
           "**anlægsprojekter** med 25 specialister og nul kritiske fund; 11 samtidige "
           "**entrepriser** med 14 mand og eget værksted; 5 elektrikere og 3 lærlinge med fuldt "
           "P&L. **Elautoriseret maskinmester** (LV/MV/HV) — **projektering**, **tavler**, "
           "**højspænding** og **lavspænding** — og vant til at stå med **budget**, **fremdrift** "
           "og **dokumentation** på samme tid.", after=80)

    m.section("KUNDEPROJEKTER OG ENTREPRISE")
    for label, body in [
        ("Fra aftale til aflevering",
         "**Kundeaftaler**, tilbud og **projektering** ført til **idriftsættelse** og aflevering; "
         "samme acceptkriterier på elleve parallelle sager."),
        ("Entreprisestyring",
         "**Entreprenører** og underentreprenører styret på **fremdrift**, **tidsplan**, "
         "**økonomi** og **sikkerhed**; ændringer afgjort før arbejdet, ikke efter."),
        ("Kundens forventninger",
         "Fast **responstid** og skriftlig aftale om, hvad der er lovet — også når svaret er, at "
         "det bliver dyrere eller senere end håbet."),
    ]:
        m.bullet(label, body)

    m.section("PROJEKTERING, DOKUMENTATION OG MYNDIGHED")
    for label, body in [
        ("El-teknisk projektering",
         "**Tavler**, forsyning og **beskyttelse** med **selektivitet** og belastning regnet "
         "igennem; **højspænding** og **lavspænding** dokumenteret til drift og vedligehold."),
        ("Dokumentation og kontrol",
         "FAT/SAT, sekvenser prøvet af, **måling** og afleveringspakke med **nul kritiske fund** "
         "— dokumentation, der kan læses af **myndigheden** om fem år."),
        ("Myndighed og rapportering",
         "**Myndighedsrapportering** i fast rytme under GMP/FDA/EMA og i entrepriser med "
         "tilsyn; ingen rapport uden den måling, den bygger på."),
    ]:
        m.bullet(label, body)

    m.section("LEDELSE, MÅL OG PROCESSER")
    for label, body in [
        ("Team og mål",
         "12 år med personaleansvar op til 25 specialister; **mål** sat sammen med teamet, MUS og "
         "1:1 hvert år, **kompetenceudvikling** som plan pr. person."),
        ("Proces og ensartethed",
         "**Procesfokus** i praksis: samme skabelon, samme kontrolpunkter og samme "
         "**arbejdsgange** på 11 entrepriser og 37 anlæg — **ensartede** uden at blive stive."),
        ("Tværgående arbejde",
         "**Tværorganisatoriske** fora med indkøb, teknik, drift og **myndighed**; beslutninger "
         "taget på det niveau, hvor de hører til — uden at gå ned i detaljen."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Ejer / teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · fuldt P&L · kundeaftaler med responstid")
    m.bullet("Kunde, pris og leverance i samme beslutning",
              "Tilbud, beregning og **projektering** med egen økonomi på spil; nul kritiske "
              "afvigelser i serviceaftalerne.")

    m.job("Senior idriftsættelsesingeniør / projektleder",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024",
          scope="37 anlægsprojekter · 25 specialister · GMP/FDA/EMA · SAP")
    m.bullet("Fremdrift, økonomi og dokumentation",
              "**Tidsplan** og **budget** fulgt pr. projekt, ændringer risikovurderet før arbejdet, "
              "og **dokumentation** der bestod en **myndigheds** gennemlæsning.")

    m.job("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · eget værksted")
    m.bullet("Elleve byggepladser, én rytme",
              "Dagligt møde, **fremdrift** og kapacitet på samme tavle; **entreprenører** og "
              "leverancer koordineret, så flaskehalse blev flyttet før de blev forsinkelser.")

    m.job("Drifts- og vedligeholdelseschef", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="Renseanlæg i 24/7-drift · HV-tavler, pumper, HVAC, SRO/SCADA")
    m.bullet("Anlægget efter afleveringen",
              "Fire år med **højspænding**stavler og akut fejlfinding — den erfaring, der gør en "
              "projekteret løsning nem eller svær at drive.")

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
           "**Persisk:** modersmål · **Bor i Måløv**, hele Sjælland inden for rækkevidde · "
           "**Kørekort B** · **Kan tiltræde efter aftale** · Referencer efter aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA FIRE TEAMS TIL ÉN ARBEJDSGANG",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–2",
             "Sid med på ti kundeprojekter i mit eget team — fra aftale til aflevering — og læs "
             "årets ændringssager igennem. Mød de tre andre managere og de **entreprenører**, der "
             "laver mest for os."),
            ("Dag 30",
             "Et fælles billede af, hvor **tidsplanen** og **økonomien** glider: de fem hyppigste "
             "årsager, målt i dage og kroner, med en ejer pr. årsag. **Målene** for teamet skrevet "
             "ned og gennemgået med hver enkelt."),
            ("Dag 60",
             "Én **arbejdsgang** gjort ens på tværs af de fire teams — aftale, ændring og "
             "aflevering — prøvet af i et løbende projekt og justeret efter det, der faktisk skete. "
             "**Myndighedsrapporteringen** lagt i en fast rytme."),
            ("Dag 90",
             "Et fælles sæt kontrolpunkter for **kundeprojekter** med **dokumentation**, der er "
             "den samme hver gang; en **kompetenceudviklings**plan pr. medarbejder og et "
             "ledergruppeforløb, hvor de fire teams deler tal i stedet for historier."),
        ],
        widths=(1500, 8830))

    m.section("FIRE TEAMS, DER LAVER DET SAMME, SKAL GØRE DET ENS")
    m.para("Det er ikke en standardiseringsøvelse for sin egen skyld. Det er, fordi kunden ikke "
           "kender vores organisation — kun sin egen dato. Når den samme slags projekt har fire "
           "forskellige måder at blive aftalt, projekteret og afleveret på, bliver forskellen "
           "synlig som forsinkelse og som en faktura, nogen skal forklare. Derfor skal der være én "
           "**arbejdsgang** med navn på ejeren, og den skal være kort nok til, at en "
           "**projektleder** kan bruge den i en travl uge.", after=70)

    m.section("EN TIDSPLAN UDEN EN EJER ER EN ØNSKESEDDEL")
    m.para("Hver dato i et **kundeprojekt** skal have et navn og en afhængighed: hvem leverer, hvornår, "
           "og hvad sker der, hvis det glider. Uden det bliver **fremdrift** noget, man taler om, "
           "når det er for sent. Jeg har kørt projekter, hvor ændringen blev vurderet på tid og "
           "**budget**, før den blev gennemført — og hvor opfølgningen lå fast hver uge, ikke når "
           "nogen spurgte.", after=70)

    m.section("ENTREPRENØREN SKAL HAVE SVARET, FØR HAN SPØRGER")
    m.para("Et godt samarbejde med **entreprenørerne** er ikke et møde hvert kvartal. Det er en "
           "aftale om, hvad der er ændret, hvad det koster, og hvornår det bliver afgjort — og en "
           "beslutningsvej, der er kort nok til, at han ikke sætter folk på andre opgaver imens. "
           "Jeg har siddet på begge sider af den snak, som bestiller og som leder, og begge steder "
           "var svaret det samme: en hurtig afklaring er billigere end den grundige analyse, der kommer for sent.", after=70)

    m.section("FÆLLESSKAB ER IKKE ET ORD PÅ EN PLAKAT — DET ER EN MÅDE AT DELE TAL PÅ")
    m.para("**Andelsselskabet** bygger på **tillid**, og tillid kræver, at de fire teams kan se "
           "hinandens tal uden at føle sig målt. Derfor skal ledergruppen dele **mål**, "
           "belastning og læring, før den deler succeshistorier. Det er også den eneste måde at få "
           "**ensretning** uden at gøre fire forskellige teams til ét stort, langsomt team.", after=70)

    m.section("HVOR JEG VILLE STARTE")
    m.para("I mit eget team, på et projekt der er midt i det. Første uge: sid med på ti "
           "**kundeprojekter** fra aftale til aflevering, læs årets ændringssager, og find ud af, "
           "hvor mange af dem der startede som en **forudsætning**, ingen havde skrevet ned. "
           "Derefter tage den hyppigste årsag og gøre den til en fælles **arbejdsgang** — sammen med "
           "de tre andre managere, ikke oven på dem.", after=0)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "DET EFTERSPØRGER DE — DET HAR JEG",
        ["Krav i opslaget", "Dokumentation"],
        [
            ("Manager til projektafdeling — **kundeprojekter** i **elnettet** på 10-0,4 kV niveau",
             "Tolv år med personaleansvar og tyve år i el-tekniske **projekter**; "
             "**elautoriseret** maskinmester (LV/MV/HV) med **højspænding**, **lavspænding**, "
             "**tavler** og forsyning."),
            ("Indgå konstruktivt i afdelingens **ledergruppe** og sikre **ensretning** og "
             "optimering på tværs",
             "**Ledergruppe**arbejde i eget selskab og i 37 **anlægsprojekter**; fire teams' "
             "arbejdsgange gjort ens ved at dele tal og metode, ikke ved at bestemme ovenfra."),
            ("Ledelse af teamet og sikre, at faglige kompetencer opretholdes og udvikles",
             "Team på op til 25 specialister og 14 mand; **kompetenceudvikling** som plan pr. "
             "medarbejder, MUS og 1:1 hvert år, tre lærlinge uddannet."),
            ("Optimering af **arbejdsgangene** og udvikling af **samarbejdet** på tværs og med "
             "**entreprenørerne**",
             "Samme skabelon og kontrolpunkter på 11 **entrepriser** og 37 anlæg; "
             "**entreprenører** styret på ændring, pris og svarfrist."),
            ("Leve op til **kundens forventninger** og håndtere **kundeaftaler**, projektledelse, "
             "**projektering**, **entreprisestyring**, eksekvering og **dokumentation**",
             "Hele kæden ført selv: aftale, tilbud, **projektering**, udførelse, "
             "**idriftsættelse** og afleveringspakke — med fuldt P&L i eget selskab siden 2023."),
            ("Fastsætte og kommunikere **mål** for teamet i tråd med afdelingens og "
             "funktionsområdets retning",
             "**Mål** sat sammen med teamet og fulgt på tavle hver uge; **resultatskabelse** målt "
             "på levering, ikke på aktivitet."),
            ("Deltage i **tværorganisatoriske** arbejdsfora og optimere samarbejde og processer "
             "uden at fordybe sig i detaljen",
             "**Tværorganisatoriske** fora med indkøb, teknik, drift og **myndighed** i 37 "
             "projekter — beslutninger løftet til det niveau, hvor de hører til."),
            ("Ledelsesmæssige værdier der bygger på **synlighed** og **nærvær**",
             "**Synlighed** som rytme: Gemba, sikkerhedsrundering og møde på pladsen — ikke møder "
             "om pladsen; **nærvær** i MUS, 1:1 og i den svære samtale."),
            ("Fokus på **resultatskabelse** gennem mennesker, processer og et højt **fagligt "
             "engagement**",
             "Mål nået gennem andre: nul kritiske fund på 37 anlæg og et produktivitetsløft på over "
             "40 procent — ingen af delene skabt alene."),
            ("Teknisk baggrund f.eks. elinstallatør, ingeniør, **maskinmester**",
             "**Elautoriseret maskinmester** (LV/MV/HV), B.Tech EQF 6 og el- og maskinteknisk "
             "design (EQF 6) — med hænderne i faget i tyve år."),
            ("1-2 års erfaring med **personaleledelse**",
             "Tolv år: 5 elektrikere + 3 lærlinge, 14-mands entrepriseteam, 12 teknikere og 25 "
             "specialister i tværfaglig ledelse."),
            ("Minimum 3 års erfaring med **projektledelse** og **entreprisestyring** i relaterede "
             "brancher",
             "37 CAPEX-projekter og 11 samtidige **entrepriser** med **udbud**, aftalegrundlag, "
             "**fremdrift** og aflevering — i alt tyve år i el-tekniske projekter."),
            ("Kendskab til **10/0,4 kV**-**distributionsnet**tet og de tekniske komponenter",
             "**Højspænding**stavler og forsyning i fire år samt **tavler**, **beskyttelse**, "
             "**selektivitet**, **måling** og kabelføring projekteret og idriftsat på 37 anlæg."),
            ("Optimere og implementere nye **metoder**, der understøtter afdelingen i at "
             "planlægge, **projektere**, dokumentere, lede og udføre",
             "**Metoder** ændret i praksis: én skabelon for tilbud og aflevering, ændringsstyring "
             "i SAP og et fælles sæt kontrolpunkter — hver gang indført med dem, der skulle bruge "
             "den."),
            ("Skabe enighed om **struktur** og **metoder**",
             "**Struktur** forhandlet på plads, før den blev skrevet ned: møderække, roller og "
             "kontrolpunkter gennemgået med dem, der skulle leve med dem — og ændret, når de "
             "havde ret."),
            ("**Procesfokus** og evnen til at bevare struktur samt skabe **ensartede** "
             "**arbejdsgange** på tværs af de 4 teams",
             "**Arbejdsgange** gjort ens på 11 entrepriser og i eget selskab: skabelon, "
             "kontrolpunkter og ejer på hvert trin — **ensartede**, ikke stive."),
            ("Effektive **processer**, **økonomisk styring** og **myndighedsrapportering**",
             "Fuldt P&L og **budget** pr. projekt, **økonomisk styring** i SAP og "
             "**myndighedsrapportering** under GMP/FDA/EMA — aftalt pris, brugt pris og det "
             "uafklarede fulgt hver uge."),
            ("**Trives i travle omgivelser** med en initiativrig og systematisk tilgang, også når "
             "det bliver svært",
             "11 samtidige **entrepriser**, 37 anlæg og 24/7-drift: prioriteret efter risiko, "
             "ikke efter larm — og taget den svære samtale, da det gjaldt."),
        ],
        widths=(3600, 6746))

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_Nexel_ManagerKundeprojekter.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_Nexel_ManagerKundeprojekter.docx'))
