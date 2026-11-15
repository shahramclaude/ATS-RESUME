# -*- coding: utf-8 -*-
"""Projektleder til grøn omstilling — solceller i boligforeninger — Københavns Kommune, MKB.

Dansk opslag -> dansk dokument, 4 sider: brev side 1, CV side 2, uddannelse + 90 dage +
metodeafsnit + "Hvor jeg ville starte" side 3, kravmatrix side 4. Format per master/README.md.

STILVALG (master/STILREGISTER.md; godkendt af scripts/style_guard.py, 3/3 skift mod #223):
  register      = FORVALTNING (nyt) — pulje, tilsagn, bevilling, høringssvar, afrapportering,
                  lokaludvalg, politisk behandling, interessenter. Ikke et teknisk register.
  åbningsgreb   = D (TALLET) — "Kommunen betaler halvdelen af rådgiveren. Ikke én krone af
                  anlægget." Sidst #215.
  struktur      = ORDLISTEN — seks ord, som opgaven faktisk består af: Solcellepuljen · den
                  opsøgende indsats · generalforsamlingen · bag-måler · evalueringen · samarbejdet.
                  Sidst #216.
  kadence       = korte sætninger med et beløb, en frist eller en person i hver anden linje.

KULTURSYNKRONISERING (policy 04.11.2026), kilder i master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md
§195:
  **Københavns Kommune, Klima-, Miljø- og Teknikforvaltningen (KMT)**, enheden
  **Bygningsfornyelse**, afdelingen **Mobilitet, Klimatilpasning og Byvedligehold (MKB)**,
  **Islands Brygge 37, 2300 København S**. Enheden er **ca. 40 ansatte** med forskellige
  uddannelser; forvaltningen har **ca. 2.700 medarbejdere** og et bruttobudget på **knap 4,8 mia.
  kr.** Stillingen er **midlertidig, et år, 37 timer/uge inkl. frokostpause**, ønsket besat
  **1. januar 2027 eller hurtigst muligt**; **frist 24. november 2026**, samtaler **uge 48-49**.
  Kontakt: **teamleder Anja Bollerup, 21 78 12 32** og **enhedschef Kristine Dose Bertelsen,
  51 84 30 93** — brevet er stilet til Anja. Ansøgning via **HR-manager** (cid 1518, ProjectId
  217374, DepartmentId 21063). Værdier: **"vi gør det ordentligt, vi gør det sammen, og vi gør det
  for København"**; **aktivitetsbaseret indretning** med hjemmezone og delte skriveborde.
  **Solcellepuljen** (byfornyelsespuljer.kk.dk): løber **2025-2027**, **først-til-mølle**,
  dækker **50 % af rådgiverudgiften** op til **20.000 kr.** pr. boligforening og op til
  **60.000 kr.** ved tre bygninger; kan søges af etageboligejendomme med **minimum fem boliger**
  (andels-, ejer-, privat udlejning og almen), af administratorer med fuldmagt og af private
  virksomheder; svar inden **3-4 uger**; udbetaling kræver **solcellerapport, faktura og
  bankkvittering** inden **6 måneder**; mail **solceller@kk.dk**. KK's egen guide "Solceller i
  boligforeninger" (Nordløv Rådgivning for Bygningsfornyelsen) beskriver **fællesmåler +
  lejlighedsmålere**, at netselskabet ejer målerne, og at **batteri og måleromlægning** flytter
  økonomien — mest for små anlæg uden batteri og uden måleromlægning. Energiteamet arbejder
  desuden med **fjernvarme og varmekældre**, **fleksibilitet og energideling** og
  **energirenovering**, ofte i **udsatte byområder**, og enheden har **puljer**, udviklingsprojekter
  og myndighedsopgaver via **Boligkommissionen**.

Ingen opdigtede fakta. Dokumenteret grundlag: **Biofos/Lynetten** 2017-2022 som drifts- og
vedligeholdelseschef med **energiledelse**, data fra **SRO/SCADA** og målere og **over 40 % lavere
energiforbrug** dokumenteret; **Novo Nordisk** 2022-2024 med **37 kapitalprojekter**, 25
specialister, FAT/SAT, nul kritiske fund, **SAP** og myndighedsdokumentation; **ELOHVAC** siden 2023
med fuldt **P&L**, **serviceaftaler**, **tilbud** og kunder i byggeriet; **Ventek Air** 2022 med 14
medarbejdere og 11 samtidige entrepriser; **ARJ** 2003-2010 med 12 teknikere; **elautoriseret
maskinmester** LV/MV/HV (maj 2023), **B.Tech** maskinteknik (EQF 6, 7,6/12), el- og maskinteknisk
design (EQF 6), **køle- og VVS-teknik** (AMU 2021), **Lean 5S/PDCA/VSM/A3** (2021); dansk
modersmål, engelsk professionelt; bor i **Måløv**, ca. 20 km fra Islands Brygge.
**Bevidst formulering:** ingen påstand om at have **projekteret eller etableret solcelleanlæg**, om
**bag-måler**-erfaring i praksis, om **EU-fondsansøgninger**, om ansættelse i en kommune eller om
**politisk-administrativt** arbejde — alle fire står som åbne mangler i brevet og i matrixrækkerne.
El- og målerkendskab er beskrevet som det, det er: elautorisation og drift, ikke solcelleprojektering.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Projektleder · grøn omstilling i byggeriet · solceller, puljer og evaluering · København'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4. november 2026")
    m.meta("Projektleder · Solceller i privatejede boligforeninger · Energiteamet, Bygningsfornyelse, MKB")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Projektleder til grøn omstilling — solceller i boligforeninger", bold=True, color='1A1A1A')
    m.para("Kære Anja,", after=60)

    # ---------------------------------------------------------------- side 1
    m.para("**Kommunen betaler halvdelen af rådgiveren. Ikke én krone af anlægget.** "
           "**Solcellepuljen** giver op til **20.000 kroner** — og op til **60.000**, hvis "
           "foreningen har tre bygninger — til at få undersøgt, om taget kan bære et anlæg. Resten "
           "skal besluttes på en **generalforsamling**, og der er det ikke taget, der vælter sagen. "
           "Det er økonomien, måleren og tidspunktet i forhold til tagrenoveringen, der aldrig blev "
           "forklaret godt nok.", after=80)

    m.para("Københavns Kommune har **ca. 2.700 medarbejdere** og et bruttobudget på **knap 4,8 mia. "
           "kroner** at gøre godt med; i MKB sidder **ca. 40** på Islands Brygge og arbejder med "
           "byfornyelse, og Energiteamet rører ikke kun **solceller**, men også **fjernvarme** og "
           "**varmekældre**, **fleksibilitet** og **energideling** og **energirenovering**. Puljen "
           "løber **2025-2027** og skal afsluttes og evalueres ved udgangen af 2027. Det er den "
           "opgave, jeg gerne vil have: ikke bare flere ansøgninger, men et tal på, hvad de førte til "
           "— også når svaret er, at de ikke førte til et anlæg.", after=80)

    m.para("**Solcellepuljen.** Puljen giver **tilskud** til halvdelen af rådgiverudgiften og kører "
           "**først-til-mølle**: svar inden **3-4 uger**, og udbetaling når der ligger "
           "**solcellerapport**, faktura og bankkvittering inden for **6 måneder**. Det er tre frister og en **afrapportering**, der skal kunne tåle at blive "
           "set efter i sømmene. Jeg har styret **37 kapitalprojekter** med ændringsstyring i **SAP** "
           "og nul kritiske fund ved aflevering; en **pulje**administration er ikke sværere, men den "
           "skal være kedelig på den rigtige måde.", after=70)

    m.para("**Den opsøgende indsats.** En **bestyrelse** i et udsat byområde beslutter ikke på et "
           "oplæg alene. Den beslutter på en nabo, der har gjort det, på en rådgiver, der har set "
           "taget, og på et regnestykke, der kan forklares på ti minutter. Derfor er **materiale** og "
           "**møder** ikke kommunikation til sidst i forløbet — de er selve indsatsen, og de skal "
           "kunne forstås af nogen, der aldrig har læst en teknisk rapport.", after=70)

    m.para("**Generalforsamlingen.** Her afgøres det. En **andelsboligforening** med 20 lejligheder "
           "skal se, hvad anlægget koster pr. lejlighed, hvad det giver, og hvornår det skal laves i "
           "forhold til facaden. Jeg har lavet den slags regnestykker i eget selskab og i 37 "
           "byggeprojekter — men jeg har ikke selv siddet i en **boligforening**sbestyrelse, og det "
           "skal jeg ikke påstå. Det, jeg kan, er at gøre en **business case** færdig nok til, at et "
           "lokale kan stemme om den.", after=70)

    m.para("**Bag-måler.** Det er her, mange sager bliver gode eller dårlige: en **fællesmåler** og "
           "en måler i hver lejlighed, målere ejet af netselskabet, og en **måleromlægning** eller et "
           "**batteri**, der flytter, hvem der får glæde af strømmen. Jeg er **elautoriseret "
           "maskinmester** og har arbejdet med tavler, målere og forbrugsdata i drift; jeg har ikke "
           "selv projekteret en bag-måler-løsning. Det siger jeg, fordi netop den detalje afgør, om "
           "anlægget bliver en god historie eller en dårlig **økonomi**.", after=70)

    m.para("**Evalueringen.** Ved udgangen af 2027 skal indsatsen kunne gøres op: hvor mange "
           "ansøgninger, hvor mange **tilsagn**, hvor mange anlæg, hvor mange kWh og hvor meget CO2 — "
           "og hvor mange foreninger der faldt fra, og hvorfor. Den sidste del er den, der gør "
           "**evaluering**en værd at læse for den næste **pulje**.", after=70)

    m.para("**Samarbejdet.** Opgaven løses ikke af én projektleder, men af en **projektgruppe**, et "
           "Energiteam og de rådgivere, der står på taget. Jeg har prøvet at være den, der kom ind "
           "med en plan, andre ikke havde været med til at lave — det holder i en måned. Derfor "
           "starter jeg med at spørge dem, der har gjort det før, hvad der ikke virkede sidst, og "
           "bygger planen på det svar.", after=80)

    m.para("**Hvad jeg ikke har.** Jeg har ikke skrevet en **EU-fond**sansøgning, jeg har ikke "
           "arbejdet i et **politisk administrativt** system, og jeg kender ikke "
           "**områdefornyelse**, **lokaludvalg** og **miljøpunkt**er indefra. Jeg har "
           "**projektledelse** og **økonomi** fra byggeriet, dokumentation fra myndighedsgodkendte "
           "anlæg og tolv år med at få andre til at flytte sig. Resten må jeg lære — og det er en "
           "del af grunden til, at jeg søger et projekt med en slutdato.", after=80)

    m.para("**Praktisk.** Jeg bor i Måløv, ca. 20 km fra Islands Brygge. Fuldtid, og **kan tiltræde "
           "1. januar 2027** eller efter aftale. **Dansk** modersmål, **engelsk** professionelt.",
           after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Projektleder med tolv års ledelse i teknik og byggeri: **37 kapitalprojekter** under "
           "myndighedskrav, **over 40 % lavere energiforbrug** dokumenteret i drift, fuldt **P&L** og "
           "**tilbud** i eget selskab siden 2023. Vant til at gøre tekniske valg til en **økonomi**, "
           "et **materiale** og en beslutning, andre kan træffe — og til at **afrapportere** det "
           "bagefter.", after=80)

    m.section("ENERGI, BYGNING OG ØKONOMI")
    for label, body in [
        ("Energi i drift",
         "**Energiledelse** på et 24/7-anlæg med data fra **SRO/SCADA** og målere; **over 40 % "
         "lavere energiforbrug** dokumenteret over få år."),
        ("Business case",
         "Investeringer vurderet på forbrug, pris og tilbagebetaling — i eget selskab og i **37** "
         "kapitalprojekter, hvor **økonomi**en skulle holde efter aflevering."),
        ("El og måling",
         "**Elautoriseret maskinmester** LV/MV/HV: tavler, målere og forbrugsdata kendt fra drift; "
         "**måleromlægning** og **bag-måler** som forhold, der skal regnes med i **business case**n."),
    ]:
        m.bullet(label, body)

    m.section("PROJEKTER, MYNDIGHED OG DOKUMENTATION")
    for label, body in [
        ("Projektledelse",
         "**Projektledelse** fra krav til aflevering: 37 anlægsprojekter, 25 specialister, FAT/SAT og "
         "nul kritiske fund — med en plan, der blev fulgt, ikke bare skrevet."),
        ("Myndighed og dokumentation",
         "**Dokumentation** godkendt under **GMP/FDA/EMA** og af myndigheder; ændringer styret i "
         "**SAP**, så historikken kunne læses af den næste."),
        ("Opfølgning og afrapportering",
         "**Monitorering** og **opfølgning** på tal hver måned; afvigelser lukket med navn og dato, "
         "og status skrevet, så den kunne læses af nogen uden for faget."),
    ]:
        m.bullet(label, body)

    m.section("BORGERE, INTERESSENTER OG FORMIDLING")
    for label, body in [
        ("Interessenter",
         "**Samarbejde** med teknik, indkøb, drift, rådgivere og myndighed; **interessenter** med "
         "forskellige interesser holdt sammen af en aftale og et referat."),
        ("Formidling",
         "**Kommunikation** til kunder, beboere og leverandører: det tekniske oversat til et valg, "
         "man kan tage stilling til — på skrift og i et **møde**."),
        ("Borgere og brugere",
         "Service og **tilbud** til bygningsejere og brugere i drift; klager og spørgsmål besvaret, "
         "inden de blev en sag."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Ejer / teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · fuldt P&L · tilbud, kunder og serviceaftaler")
    m.bullet("Forretning i byggeriet",
              "Tilbud, kalkulation og leverance for bygningsejere — **økonomi** og teknik i samme "
              "samtale, og ansvar for at det holdt.")

    m.job("Senior idriftsættelsesingeniør / projektleder",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024",
          scope="37 kapitalprojekter · 25 specialister · FAT/SAT · SAP · myndighedsdokumentation")
    m.bullet("Projekter med revisionsspor",
              "Ændringer dokumenteret i **SAP**, prøver kørt før overlevering og nul kritiske fund — "
              "et forløb, der kunne tåle et tilsyn bagefter.")

    m.job("Projekt- og værkstedsleder", "Ventek Air ApS · Vedbæk · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · ventilation, køl og CTS")
    m.bullet("Mange sager, én kalender",
              "Elleve samtidige opgaver prioriteret med leverandører og underentreprenører — "
              "kapacitet flyttet, før det blev en forsinkelse.")

    m.job("Drifts- og vedligeholdelseschef", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="24/7-drift · energiledelse · ventilation, køl, pumper · SRO/SCADA · beredskab")
    m.bullet("Energi, der kunne måles",
              "Forbrug fulgt på målere og i **SRO/SCADA**, tiltag valgt på data og **over 40 %** "
              "lavere energiforbrug dokumenteret i driften.")

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
           "**Persisk:** modersmål · **Bor i Måløv**, ca. 20 km fra Islands Brygge · Fuldtid, "
           "**kan tiltræde 1. januar 2027** eller efter aftale · Referencer efter aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA PULJE TIL BESLUTNING",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–2",
             "Læs puljens ansøgninger, **tilsagn** og afslag igennem for 2025 og 2026 — og find ud "
             "af, hvor i forløbet foreningerne stoppede: ved ansøgningen, ved rådgiveren eller ved "
             "**generalforsamlingen**. Gå med på to rådgivningsbesøg og et borgermøde."),
            ("Dag 30",
             "En kortlægning af, hvem der bliver nået i dag, og hvem der ikke gør — med et forslag "
             "til **materiale** og mødeform til de byområder, hvor der søges mindst. Gennemgået med "
             "**projektgruppen**, før den går videre."),
            ("Dag 60",
             "Et opfølgningsløb, hvor hvert **tilsagn** har en dato og en ejer, og hvor udbetalingen "
             "ikke kan falde mellem to stole. Første version af **monitorering**en på ét ark."),
            ("Dag 90",
             "En **evaluering**splan med de tal, der skal kunne fremlægges ved udgangen af 2027 — "
             "ansøgninger, **tilsagn**, anlæg, kWh, CO2 og frafald — og et oplæg til næste "
             "energiprojekt med en mulig fond bag."),
        ],
        widths=(1500, 8830))

    m.section("EN PULJE ER ET LØFTE, IKKE EN KASSE")
    m.para("Når kommunen lægger penge i en **pulje**, lover den borgerne, at der bliver fulgt op. En "
           "**ansøgning**, der får **tilsagn** og derefter aldrig bliver til noget, er dyrere for "
           "tilliden end et afslag. Derfor skal administrationen være så kedelig, at ingen skal "
           "ringe og spørge, hvor sagen står — og så hurtig, at de **3-4 uger** holder i praksis.",
           after=70)

    m.section("EN RÅDGIVERRAPPORT ER IKKE ET ANLÆG, DER BLIVER BYGGET")
    m.para("Et solcelleanlæg på et tag i København konkurrerer ikke med andre anlæg. Det konkurrerer "
           "med en ny facade, et nyt tag og en **måleromlægning**, der skal betales samme år. Den "
           "samtale vindes ikke med flere tekniske data; den vindes ved at lægge regnestykket frem, "
           "så det passer ind i den renovering, foreningen alligevel skal i gang med.", after=70)

    m.section("BORGERINDDRAGELSE ER ET HÅNDVÆRK, IKKE ET MØDE")
    m.para("**Borgere** møder ikke op for at høre om **bag-måler**. De møder op, fordi taget er "
           "utæt, eller fordi varmekælderen koster for meget. **Borgerinddragelse** består i at tage "
           "udgangspunkt i det, de allerede er optaget af, og først derefter tale om solceller — "
           "ellers bliver mødet et oplæg, og oplæg flytter ingen beslutning.", after=70)

    m.section("EVALUERING SKAL KUNNE TÅLES AF DEN, DER KOMMER EFTER")
    m.para("En **evaluering** er ikke en rapport om, hvor godt det gik. Det er en liste over, hvad "
           "der virkede, hvad der ikke gjorde, og hvad den næste **pulje** skal gøre anderledes — "
           "skrevet så kort, at en kollega kan læse den på en formiddag. Jeg har skrevet "
           "**afrapportering**er, der skulle godkendes af myndigheder; jeg ved, at det er den korte "
           "version, folk bruger.", after=70)

    m.section("ET AFSLAG ER OGSÅ ET RESULTAT")
    m.para("Den nemmeste **evaluering** tæller de anlæg, der blev bygget. Den nyttige tæller også "
           "dem, der fik et **tilsagn** og droppede ud, og dem, der aldrig søgte, fordi de hørte om "
           "**puljen** for sent eller ikke troede, at den var for dem. De tre tal er grundlaget for "
           "den næste **pulje** — og det er dem, jeg ville ringe efter, mens historien stadig er "
           "frisk, i stedet for at gætte i en **afrapportering** et år senere.", after=70)

    m.section("HVOR JEG VILLE STARTE")
    m.para("I ansøgningerne. Første uge: læse 2025 og 2026 igennem, gå med på to rådgivningsbesøg og "
           "sidde med til et borgermøde i et af de områder, hvor der søges mindst. Derefter finde ud "
           "af, om frafaldet ligger i ansøgningen, i rådgivningen eller i **generalforsamlingen** — "
           "for det er tre forskellige problemer, og de skal løses med tre forskellige greb.",
           after=0)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "KRAV I OPSLAGET — DET HAR JEG",
        ["Krav i opslaget", "Dokumentation"],
        [
            ("**Projektledelse**, udvikling og implementering af den borgernære **opsøgende indsats** "
             "om **solceller**",
             "37 kapitalprojekter fra krav til aflevering og 11 samtidige entrepriser; indsatser "
             "bygges som et forløb med **materiale**, **møder** og en opfølgning pr. deltager."),
            ("Administration af **Solcellepuljen**, herunder **monitorering**, **opfølgning** og "
             "**afrapportering**",
             "**Monitorering** og **opfølgning** på tal hver måned, ændringer i **SAP** og "
             "**afrapportering** til myndigheder; **pulje**ns tre frister styret som en kalender."),
            ("Planlægning og afvikling af **evaluering** af puljen og den opsøgende indsats",
             "Afleveringer med nul kritiske fund og afvigelser lukket med navn og dato; "
             "**evaluering** som kort rapport, den næste **pulje** kan bruge."),
            ("Sikre projektimplementeringen sammen med en **projektgruppe**",
             "Tværfagligt arbejde med teknik, indkøb, drift og myndighed i 37 projekter; **samarbejde** "
             "om en plan, ikke om en holdning."),
            ("Sikre afslutning og **evaluering** af Solcelleindsatsen ved udgangen af 2027",
             "Projekter afsluttet og dokumenteret til dato — FAT/SAT, afleveringsmappe og "
             "slutdokumentation; vant til at arbejde mod en fast slutdato."),
            ("Bistå med **projektudvikling** og **fundraising** af nye energirelaterede projekter",
             "Energiprojekter udviklet fra idé til investering i eget selskab og i drift; "
             "**fundraising** er ny for mig, **projektudvikling** er den del, jeg kender."),
            ("**Fundraising** af primært **EU-fonde**",
             "Ikke prøvet endnu. Jeg har skrevet **tilbud**, kravspecifikationer og "
             "**dokumentation**, der skulle godkendes eksternt — og jeg lærer et ansøgningsformat "
             "ved at skrive det første."),
            ("Fremme implementeringen af gode **energiløsninger** i den eksisterende by",
             "**Energiledelse** med **over 40 %** lavere forbrug dokumenteret, og "
             "**energirenovering** og **fjernvarme** kendt fra drift af ældre anlæg i byen."),
            ("Stærk interesse for **grøn omstilling** i byggeriet, **energi** og **bæredygtig** "
             "udvikling af **København**",
             "Fem år med drift og energi i København (Biofos/Lynetten), eget selskab i byggeriet og "
             "en uddannelse, der gør **bæredygtig** drift til et regnestykke, ikke et slogan."),
            ("Evne at skabe gode **samarbejder** med københavnerne",
             "Kunder og brugere i drift og service siden 2022; aftaler og forventninger afstemt med "
             "dem, der skulle leve med resultatet."),
            ("**Kommunikation** med både **borgere** og professionelle **samarbejdspartnere**",
             "Det tekniske oversat til et valg på skrift og i **møder** — over for teknikere, "
             "leverandører, kunder og myndighed i samme sag."),
            ("Erfaring fra arbejde med **energiprojekter**",
             "**Energiledelse** og forbrugsoptimering i 24/7-drift; energitiltag i eget selskab og "
             "energirelaterede investeringer i 37 kapitalprojekter."),
            ("Kendskab til **bag-måler**-system",
             "**Elautoriseret maskinmester** med tavler, målere og forbrugsdata i drift; "
             "**bag-måler** og **måleromlægning** kendt som forhold, ikke som egen projektering."),
            ("Kendskab til juridiske og organisatoriske forhold for etablering af **solcelleanlæg**",
             "Organisatorisk: **generalforsamling** og bestyrelse som beslutningssted forstået og "
             "respekteret. Juridisk og solcellefagligt: ikke min baggrund — det lærer jeg af "
             "rådgiverne og af jer."),
            ("Kunne tilrettelægge **borgerrettede processer**, herunder forberedelse af **materiale** "
             "og mediering af **møder**",
             "**Materiale** og **møder** til teknikere, kunder og samarbejdspartnere i tolv år; "
             "**borgerinddragelse** i udsatte områder er ny, og den skal læres af dem, der gør den."),
            ("Erfaring med at arbejde i et **politisk administrativt** system",
             "Ikke fra en kommune. Jeg har arbejdet i **forvaltning**ens grænseflade som "
             "leverandør og entreprenør, med myndighedsgodkendelser og **dokumentation** — og ved, "
             "at en **politisk** beslutning har en anden tidshorisont end en byggeplads."),
            ("Erfaring med udvikling og **projektledelse** af **EU**-finansierede projekter",
             "Ikke endnu. **Projektledelse**, budget og **afrapportering** er dokumenteret; "
             "**EU**-formatet er nyt, og jeg vil hellere sige det end love et halvfærdigt oplæg."),
            ("Facilitering af **samarbejder** med **rådgiver**e og brancheorganisationer",
             "**Rådgivere**, leverandører og underentreprenører styret i 37 projekter og 11 "
             "entrepriser; møder ledet med en dagsorden og et referat, der blev fulgt."),
            ("Kendskab til **områdefornyelse**, **lokaludvalg** og **miljøpunkt**er",
             "Ikke endnu. Jeg kender byfornyelsens faglige indhold fra byggeriet og "
             "**energirenovering**, og jeg vil bruge de første uger på at lære de tre strukturer at "
             "kende gennem dem, der sidder i dem."),
        ],
        widths=(3600, 6746))

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_KoebenhavnsKommune_SolcellerProjektleder.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_KoebenhavnsKommune_SolcellerProjektleder.docx'))
