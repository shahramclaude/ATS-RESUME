# -*- coding: utf-8 -*-
"""Dines Jørgensen & Co. A/S — VVS-/HVAC-ingeniør (rådgiverrolle), Hillerød.

Dansk opslag → dansk dokument (da-DK): ansøgning side 1, CV side 2, uddannelse + 90 dage +
fire afsnit side 3, kravmatrix side 4.

STILVALG (master/STILREGISTER.md, policy 04.11.2026; kørt gennem scripts/style_guard.py,
3/3 skift mod #194):
  register      = RÅDGIVENDE — udbud, beslutningsgrundlag, interessent, leverance. Rollen ER en
                  rådgiverrolle, så registret er valgt på fagligt fit, ikke på variation. Brugt
                  i #193; ordvalg, rytme og sektionsoverskrifter er derfor holdt i byggefagligt
                  sprog (snitflade, kollision, frihøjde, tålegrænse, entrepriseform) og ikke i
                  laboratorie- og standardiseringssprog.
  åbningsgreb   = E (TIDSFORSKYDNINGEN) — beslutningen ligger før det, man tror: i registreringen,
                  ikke i tegningen. Sidst brugt #187.
  struktur      = SNITFLADERNE — seks grænseflader i en renovering: det bestående mod det nye,
                  fagene imellem, bygherre/arkitekt, beskrivelse/entreprenør, budget/virkelighed,
                  projektering/plads.
  kadence       = kort, konkret byggefagligt; én grænseflade pr. afsnit, ingen jargon uden pointe.

Ingen opdigtede fakta: der påstås IKKE VVS-installatør- eller bygningsingeniøruddannelse, ikke
10 år som rådgivende ingeniør med tegningsansvar, og ikke tegningsproduktion i Revit. Det
dokumenterede grundlag er elautoriseret maskinmester (LV/MV/HV), el- og maskinteknisk design
(EQF 6), B.Tech, køleteknik (AMU), 20+ år med ventilation, køl, vand og CTS i drift og entreprise,
udbud/tilbud og afleveringspakker fra entreprenørsiden, FAT/SAT og dokumentation i GMP-miljø samt
personaleledelse af 5 elektrikere + 3 lærlinge og koordinering af 14 mand / 11 entrepriser.

Policy: master/README.md — jobbet først, kandidaten kun som bevis, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'VVS-/HVAC-ingeniør · Renovering, projektering og tilsyn'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4. november 2026")
    m.meta("Dines Jørgensen & Co. A/S · VVS-/HVAC-ingeniør · Kirsebæralle 9, 3400 Hillerød")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: VVS-/HVAC-ingeniør — rådgivning, projektering og tilsyn", bold=True, color='1A1A1A')
    m.para("Til Martin Møller, Møller & Partners", after=70)

    # ---------------------------------------------------------------- side 1
    m.para("**En renovering bliver afgjort, længe før den første tegning bliver tegnet.** Den bliver "
           "afgjort en tirsdag formiddag med en lommelygte i hånden, når nogen finder ud af, at der "
           "ikke er plads til både ventilationskanal og faldstamme over loftet i stueetagen — og at "
           "den beslutning koster mere end hele projekteringsfasen, hvis den bliver taget for sent. "
           "Det er den slags formiddage, jeg gerne vil bruge min faglighed på: at finde snitfladerne, før "
           "de bliver til kollisioner på pladsen.", after=80)

    m.para("**Snitfladen mellem det, der står, og det, der skal bygges.** En **transformation** af en "
           "ældre bygning starter ikke med en løsning; den starter med en **registrering**, der er "
           "ærlig. Hvor løber rørene, hvor er der frihøjde, hvad er der isoleret, og hvad er der "
           "sjusket med i 1987? Jeg har arbejdet i bygninger, hvor ingen vidste, hvor "
           "**ventilationen** endte, og hvor den eneste brugbare tegning var den, der blev tegnet "
           "bagefter. Den erkendelse skal ind i **tilstandsrapporten** — ikke forsødes, fordi den er "
           "ubelejlig.", after=80)

    m.para("**Snitfladen mellem fagene.** Vand, varme, ventilation, køl, CTS og kloak skal alle samme "
           "vej gennem det samme loft. Jeg har projekteret og dimensioneret **ventilations**- og "
           "**klimaanlæg**, arbejdet med **køl** og **varme** i drift og med **CTS** og styring fra "
           "tavlesiden, og jeg ved, at den dyreste kollision sjældent er den, der er sværest at løse — "
           "det er den, der bliver løst af to fag hver for sig. Derfor vil jeg hellere sidde med "
           "**koordineringen** tidligt, hvor det stadig kun er en flytning af en kanal.", after=80)

    m.para("**Snitfladen mellem bygherre og arkitekt.** En **boligforening** eller en **offentlig "
           "bygherre** køber ikke en teknisk løsning; den køber et **indeklima**, en **energi**regning "
           "og en bygning, der ikke giver klager. Min rolle er at gøre valget eksplicit: her er to "
           "løsningsprincipper, her er hvad de koster i anlæg og i drift, og her er hvad I giver afkald "
           "på, hvis I vælger den billige. Jeg har siddet på den anden side af bordet som entreprenør "
           "og som rådgiver for private bygherrer, og jeg ved, hvor forskelligt det samme forslag "
           "bliver læst, alt efter hvem der læser det.", after=80)

    m.para("**Snitfladen mellem beskrivelsen og entreprenøren.** Et **udbudsmateriale** er ikke et "
           "dokument, der skal imponere — det er en aftale, der skal kunne prissættes uden at nogen "
           "ringer. Jeg har skrevet **udbud** og **tilbudslister** og siddet med "
           "**tilbudsgivningen** fra entreprenørsiden, hvor en uklar beskrivelse bliver til et "
           "forbehold, og et forbehold bliver til en ekstraregning. Derfor skriver jeg anderledes end "
           "den, der aldrig har skullet bygge efter sine egne ord: korte sætninger, tal hvor der kan "
           "sættes tal, og en tydelig grænse for, hvad der er med.", after=80)

    m.para("**Snitfladen mellem budgettet og virkeligheden.** **Økonomiske overslag** er et løfte, og "
           "et **budget**, der holder i marts, skal også holde i november. Jeg har haft fuldt "
           "P&L-ansvar siden 2023 og lavet **overslag** på egne **entrepriser** siden 2017 — inklusive "
           "dem der blev dyrere, end jeg havde regnet, og som jeg lærte mest af. I en "
           "**renovering** skal usikkerheden stå i overslaget som en linje, ikke som en overraskelse "
           "senere.", after=80)

    m.para("**Snitfladen mellem projektering og pladsen.** **Tilsyn** og rollen som **byggeleder** er ikke "
           "kontrol for kontrollens skyld; det er den funktion, der sikrer, at det, der blev besluttet, "
           "også bliver det, der bliver bygget. Jeg har ført tilsyn med egne entrepriser, stået for "
           "**aflevering** med KS og afleveringspakker og arbejdet i **arbejdsmiljø**koordinering med "
           "LOTO, APV og sikkerhedsrunder. På en renovering, hvor der boes eller arbejdes imens, er den "
           "del ikke en formalitet.", after=80)

    m.para("**Hvor jeg ikke passer i skabelonen — og hvorfor det er til at arbejde med.** Jeg er ikke "
           "**VVS-installatør** og ikke **bygningsingeniør**; min vej er **elautoriseret "
           "maskinmester** (LV/MV/HV), el- og maskinteknisk design (EQF 6) og B.Tech i "
           "teknologiledelse og maskinteknik, med **køleteknik** oveni. Jeg har heller ikke ti år bag "
           "mig som **rådgivende ingeniør** med tegningsansvar. Til gengæld har jeg 20+ år i faget, "
           "heraf projektering og **entrepriser** siden 2017 og egen virksomhed med projektering, "
           "**udbud** og **tilsyn** siden 2023 — og det, opslaget kalder \"eller tilsvarende\", er "
           "netop den vej.", after=80)

    m.para("Til gengæld er der en ting, jeg kan, som opslaget ikke spørger om, men som I får med: "
           "**teamledelse**. Jeg har haft personaleansvar for 5 elektrikere og 3 lærlinge, "
           "koordineret 14 mand på 11 samtidige entrepriser og lagt vagtplan for 12 mekanikere. Hvis "
           "muligheden for at indtræde som teamleder på sigt bliver aktuel, er den ikke ny for mig — "
           "og jeg vil hellere vokse ind i den i et hus, hvor fagligheden kommer først.", after=80)

    m.para("Jeg bor i Måløv, og Hillerød er ca. 25 minutter. At komme tilbage til en rådgiverrolle i et "
           "hus med flad organisation, kort fredag og et kollegaskab, man faktisk deltager i, er ikke "
           "et kompromis for mig — det er den ramme, jeg gerne vil arbejde i efter tre år med egen "
           "virksomhed. Jeg kan tiltræde snarest.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Rådgivende og udførende tekniker med 20+ års erfaring i **ventilation**, **køl**, **varme**, "
           "**vand** og **CTS** — **elautoriseret maskinmester** (LV/MV/HV), el- og maskinteknisk "
           "design (EQF 6), B.Tech i teknologiledelse og maskinteknik og **køleteknik** (AMU). Har "
           "projekteret og dimensioneret ventilations- og klimaanlæg, skrevet **udbud** og "
           "**tilbudslister**, ført **tilsyn** med egne **entrepriser** og afleveret med KS — og "
           "koordineret 14 mand og 11 samtidige **entrepriser** med fuldt P&L-ansvar siden 2023.",
           after=80)

    m.section("VENTILATION, VARME, KØL OG VAND")
    for label, body in [
        ("Projektering og dimensionering",
         "Ventilations- og klimaanlæg projekteret fra specifikation til aflevering: luftmængder, "
         "kanaldimensioner, armaturer og styring; køleanlæg og varmeflader dimensioneret efter "
         "driftsforhold, ikke efter kataloget."),
        ("CTS, styring og el",
         "CTS og SCADA i drift og fejlfinding; el-tekniske installationer, tavler og styring fra "
         "elautorisationen — grænsefladen mellem VVS-anlægget og det, der styrer det, er ikke en "
         "fremmed størrelse for mig."),
        ("Vand, afløb og spildevand",
         "Pumper, pumpestationer og vandbehandling i døgndrift på renseanlæg; **afløb** og **kloak** "
         "som en del af den samlede installation, ikke som et selvstændigt fag."),
    ]:
        m.bullet(label, body)

    m.section("PROJEKTERING, UDBUD OG TILSYN")
    for label, body in [
        ("Udbud og beskrivelser",
         "Udbudsmateriale, tilbudslister og beskrivelser skrevet, så de kan prissættes uden "
         "telefonopkald; aftalegrundlag og forbehold gennemgået fra entreprenørsiden."),
        ("Økonomi og overslag",
         "Økonomiske overslag og budgetter på egne entrepriser (DKK 2–10 mio.), kalkulation og "
         "tilbudsberegning, fuldt P&L-ansvar; investeringsmodeller (NPV/IRR) ved valg mellem "
         "reparation og udskiftning."),
        ("Tilsyn, KS og aflevering",
         "Tilsyn med egne entrepriser, kvalitetssikring og afleveringspakker; prøvekørsel og "
         "dokumentation, 1- og 5-års gennemgang samt FAT/SAT og IQ/OQ/PQ i GMP-miljø."),
    ]:
        m.bullet(label, body)

    m.section("KOORDINERING, LEDELSE OG ARBEJDSMILJØ")
    for label, body in [
        ("Koordinering af fag og mandskab",
         "14 mand og 11 samtidige entrepriser styret med daglige tavlemøder og flaskehalsanalyser; "
         "faglig sparring med underentreprenører og bygherre."),
        ("Personaleledelse",
         "Personaleansvar for 5 elektrikere + 3 lærlinge: 1:1, MUS, oplæring og kompetencematrix; "
         "situationsbestemt ledelse på skiftende arbejdspladser."),
        ("Arbejdsmiljø på pladsen",
         "LOTO, APV, risikovurdering ved opstart, sikkerhedsrunder og nærved-hændelser; "
         "arbejdsmiljøkoordinering i byggeri, hvor andre arbejder imens."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Ejer / teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · fuldt P&L · projektering, udbud og tilsyn")
    m.bullet("Projektering og bygherredialog",
              "Ventilations- og klimaanlæg for erhvervskunder: registrering, løsningsvalg, "
              "økonomiske overslag og udbud — fra første besigtigelse til aflevering.")
    m.bullet("Udførelse og aflevering",
              "Egen vagtordning, KS og afleveringsdokumentation; AI-værktøjer (Python, Power BI) til "
              "tidsplaner, tjeklister og KPI — over 40 % produktivitetsløft på det administrative.")

    m.job("Senior idriftsættelsesingeniør / projektleder, elsystem",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024",
          scope="37 samtidige anlægsprojekter · 25 specialister · GMP/FDA/EMA")
    m.bullet("Grænseflader og afvigelser",
              "FAT/SAT og IQ/OQ/PQ: protokoller skrevet før testen, afvigelser lukket med "
              "rodårsagsanalyse — nul kritiske fund. Fremdrift og økonomi i SAP ERP.")

    m.job("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · DKK 2–10 mio.")
    m.bullet("Projektering til plads",
              "Ventilationsentrepriser fra specifikation til formel aflevering: udbud, tilbudslister, "
              "prøvekørsel og afleveringspakker; daglige tavlemøder med teknikere og ugentlig "
              "opfølgning mod bygherre.")

    m.job("Vedligeholdelses- og driftsleder", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="Renseanlæg i 24/7-drift · pumper, HVAC, højspændingstavler, SCADA")
    m.bullet("Anlæg, der ikke må stoppe",
              "Forebyggende vedligehold og akut fejlfinding på pumper, vand- og spildevandsanlæg og "
              "ventilation; 5S og standard work på værksted og lager, LOTO og APV.")

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
    m.edu("Køleteknik & klimaanlæg (AMU)", "Mercantec · 2021")
    m.edu("Lean-/forbedringspraksis: 5S, PDCA, VSM, A3, Kaizen · STCW sikkerhedskurser (2021–2023)",
          "Mercantec / Søfartsstyrelsen")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("**Dansk:** modersmål, skriftligt og mundtligt på professionelt niveau · **Engelsk:** "
           "professionelt · **Persisk:** modersmål · **Bosat i Måløv**, ca. 25 minutter til Hillerød · "
           "**Kan tiltræde snarest** · Referencer efter aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA REGISTRERING TIL AFLEVERING",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–2",
             "Læse jeres projektmetode og skabeloner igennem; gennemgå to igangværende "
             "**renoveringer** fra **registrering** til **udbud** og se, hvor beslutningerne faktisk "
             "bliver taget. Sidde med på et byggemøde som tilhører, ikke som den, der fører ordet."),
            ("Dag 30",
             "Egen opgave leveret: et **økonomisk overslag** og en **tilbudsliste** på et afgrænset "
             "projekt, gennemgået med en kollega før det går videre — første skridt mod at være "
             "**nøgleperson** på egne projekter."),
            ("Dag 60",
             "Ansvarlig for en mindre sag alene: **registrering**, løsningsprincip, **dimensionering** "
             "og **tilsyn**; grænsefladerne til de øvrige fag aftalt skriftligt, før tegningerne låses."),
            ("Dag 90",
             "To–tre sager i eget navn med bygherre- og **arkitekt**dialog. Status med dig: hvad jeg "
             "løser selv, hvad jeg sparrer om, og hvad der skal til, for at **teamledelse** bliver et "
             "naturligt næste skridt."),
        ],
        widths=(1500, 8830))

    m.section("EN TILSTANDSRAPPORT SKAL KUNNE LÆSES AF EN, DER IKKE VAR DER")
    m.para("Der er forskel på at beskrive en bygning og på at beskrive, hvad der er galt med den. Den "
           "gode **tilstandsrapport** giver bygherren mulighed for at beslutte noget: hvad der skal "
           "løses nu, hvad der kan vente, og hvad der bliver dyrere af at vente. Jeg har skrevet "
           "afvigelser i GMP-miljø, hvor et manglende bilag stoppede en aflevering — den disciplin "
           "tager jeg med ind i **renoveringen**, for der er ingen, der takker en for en pæn "
           "formulering, når vandet står i kælderen.", after=70)

    m.section("JEG REGNER, FØR JEG TEGNER")
    m.para("Et **ventilations**anlæg, der er tegnet rigtigt og regnet forkert, virker ikke i en "
           "renoveret ejendom — det larmer, det trækker, og det bruger for meget **energi**. Jeg "
           "regner på luftmængder, trykfald, **isolering** og kølebehov, før der bliver sat streger, "
           "og jeg vil hellere bruge en time på at efterprøve et tal end en uge på at rette en "
           "kanal, der ikke kan være der. Det er ikke den sjoveste del af arbejdet; det er den, der "
           "gør resten muligt.", after=70)

    m.section("KORT FREDAG ER IKKE DET SAMME SOM KORT ARBEJDSDAG")
    m.para("En 36-timers uge kræver, at nogen har tænkt over, hvad der ikke skal laves. Jeg har drevet "
           "virksomhed i tre år, hvor weekender og aftenmøder var en del af regnestykket, og jeg "
           "foretrækker et sted, hvor **energi**en bliver brugt på projekterne og ikke på at være "
           "tilgængelig hele tiden. Det er ikke et spørgsmål om indsats; det er et spørgsmål om, "
           "hvordan et **rådgivende ingeniør**hus får mest faglighed ud af de timer, det har.", after=70)

    m.section("JEG HAR VÆRET PÅ DEN SIDE, DER MODTAGER UDBUDDET")
    m.para("Det er den erfaring, jeg vil bruge mest. Som **entreprenør** har jeg læst beskrivelser, hvor "
           "det var umuligt at se, om **isolering** var med, og hvor svaret først kom som et forbehold "
           "tre uger senere. Det gør ikke mine beskrivelser gode i sig selv, men det gør mig opmærksom på, "
           "hvor prisen på en uklar sætning lander: hos **bygherren**, til sidst, som en ekstraregning "
           "og en dårlig sag.", after=70)

    m.section("DET JEG IKKE HAR GJORT ENDNU — OG DET JEG HAR")
    m.para("Jeg har ikke tegnet i Revit som rådgiver og ikke siddet med tegningsansvar i et "
           "rådgivende ingeniørhus; det skal læres her, og det regner jeg med at kunne på et par "
           "måneder med jeres skabeloner og en kollega, der gider rette. Det, jeg har med i stedet, er "
           "20+ år på den anden side af bordet: jeg ved, hvordan et anlæg opfører sig i drift, hvordan "
           "en **entreprenør** læser en beskrivelse, og hvad der sker, når **myndighed**en spørger til "
           "**afløb** og **indeklima** — og jeg er ikke bange for at sige, at noget skal regnes om.",
           after=0)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "HVAD STILLINGEN KRÆVER — HVAD JEG HAR LEVERET",
        ["Krav i opslaget", "Bevis"],
        [
        ("VVS-/HVAC-ingeniør med minimum 10 års erfaring som rådgivende ingeniør eller tilsvarende",
         "20+ år i faget: projektering og entrepriser siden 2017, egen virksomhed med projektering, "
         "udbud og tilsyn siden 2023. Ikke 10 år som rådgivende ingeniør med tegningsansvar."),
        ("Uddannet VVS-installatør eller bygningsingeniør",
         "Ikke VVS-installatør eller bygningsingeniør. Elautoriseret maskinmester (LV/MV/HV), el- og "
         "maskinteknisk design (EQF 6), B.Tech i teknologiledelse og maskinteknik samt køleteknik "
         "(AMU) — den tekniske og installationsfaglige vej ind i samme arbejde."),
        ("Erfaring med projektledelse inden for ventilation, varme, vand, CTS, afløb og kloak",
         "11 samtidige entrepriser og 14 mand som projekt- og værkstedsleder; 37 anlægsprojekter hos "
         "Novo Nordisk; ventilation og CTS i projektering og drift, vand, afløb og spildevand fra "
         "renseanlæg."),
        ("Erfaring med projektering inden for ventilation, varme, vand, CTS, afløb og kloak",
         "Ventilations- og klimaanlæg projekteret fra specifikation til aflevering; varme- og "
         "køleanlæg dimensioneret; CTS og styring fra tavlesiden. Tegningsansvar i et rådgiverhus er "
         "ikke prøvet endnu."),
        ("Registrering, projektering og dimensionering af installationer: vand, varme, ventilation, køl, CTS, kloak",
         "Besigtigelse og registrering af eksisterende anlæg i erhvervsejendomme; dimensionering af "
         "luftmængder, kanaler, køl og varme; kloak og afløb som del af den samlede installation."),
        ("Beskrivelser, udbudsmateriale, tilbudslister og tilstandsrapporter",
         "Udbud, tilbudslister og beskrivelser skrevet og prissat; afvigelser og tilstand beskrevet i "
         "rapporter, der kunne følges af en tredjemand — fra entreprenørsiden, hvor de skulle bygges "
         "efter."),
        ("Økonomiske overslag og budgetter",
         "Økonomiske overslag og kalkulation på egne entrepriser (DKK 2–10 mio.), fuldt P&L-ansvar "
         "siden 2023, investeringsmodeller (NPV/IRR) ved valg mellem reparation og udskiftning."),
        ("Dialog med bygherrer og arkitekter om projektomfang og løsningsprincipper",
         "Bygherredialog i egen virksomhed og hos Ventek-Air; løsningsprincip og omfang gennemgået med "
         "bygherre før udbud, med pris og konsekvens i drift som beslutningsgrundlag."),
        ("Faglig koordinering med øvrige ingeniører",
         "25 specialister og 37 projekter koordineret hos Novo Nordisk; grænseflader mellem el, "
         "ventilation og CTS aftalt skriftligt, før tegningerne blev låst."),
        ("Samarbejde med entreprenører",
         "Underentreprenører styret på 11 entrepriser, aftalegrundlag og forbehold forhandlet — og "
         "selv været entreprenøren, der modtog beskrivelsen."),
        ("Tilsyn og byggelederrolle på HVAC- og kloakprojekter",
         "Tilsyn med egne entrepriser, KS og afleveringspakker, prøvekørsel og 1-/5-års gennemgang; "
         "byggelederrolle på kloakprojekter ikke prøvet, tilsynsrollen er."),
        ("Arbejder struktureret og selvstændigt",
         "Egen virksomhed drevet selvstændigt siden 2023 med projektering, udbud, tilsyn og "
         "økonomi; A3, PDCA og standard work som arbejdsform."),
        ("Trives med fagligt ansvar og er stærk i dialogen med samarbejdspartnere",
         "Fagligt ansvar for afleveringer med nul kritiske fund; dialog med bygherre, arkitekt og "
         "entreprenør i 20+ år, på dansk og engelsk."),
        ("Behersker flydende dansk på et professionelt niveau i skrift og tale",
         "Dansk modersmål; teknisk dokumentation, udbud og korrespondance skrevet på dansk i årevis, "
         "engelsk ved siden af."),
        ("Nøgleperson på egne projekter og bidrag til valg af tekniske løsningsprincipper",
         "Nøgleperson på egne entrepriser i dag; løsningsprincipper valgt med begrundelse i anlæg, "
         "drift og pris — og efterprøvet ved aflevering."),
        ("På sigt mulighed for at indtræde som teamleder",
         "Personaleansvar for 5 elektrikere + 3 lærlinge, koordinering af 14 mand og vagtplan for 12 "
         "mekanikere; SLII og MUS i praksis, ikke på kursusbevis."),
        ],
        widths=(3600, 6746))

    m.section("EN KANAL ER SJÆLDENT DET SVÆRE — PLADSEN ER")
    m.para("De fleste **ventilation**sproblemer i en **ombygning** handler ikke om luft, men om "
           "centimeter. Frihøjde over loftet, fald på **afløb**et, plads til **isolering** og adgang "
           "til at komme til, når noget skal serviceres om fem år. Derfor tegner jeg gerne den svære "
           "del først: hvor skal det hele være, og hvem flytter sig. Det er billigere at flytte en "
           "kanal på papir end at flytte en hovedkanal i en beboet ejendom.", after=70)

    m.section("JEG SØGER EN RÅDGIVERROLLE, IKKE EN PENSION")
    m.para("Jeg har prøvet at være den, der tager beslutningen alene, og det er ikke det, jeg søger nu. "
           "Jeg søger **faglig sparring** med nogen, der har gjort det længere end mig, og projekter "
           "hvor der er tid til at gøre det ordentligt — **transformation**, **renovering** og "
           "installationer, hvor en fejl ikke kan males over. Hvis det også betyder, at jeg på sigt "
           "skal lede et lille team, tager jeg gerne den del med.", after=0)

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_Dines_Joergensen_HVAC.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_Dines_Joergensen_HVAC.docx'))
