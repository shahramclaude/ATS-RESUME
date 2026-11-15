# -*- coding: utf-8 -*-
"""Service-projektleder til serviceafdelingen — airteam a/s, Roskilde / Københavns Lufthavn.

Dansk opslag -> dansk dokument, 4 sider: brev side 1, CV side 2, uddannelse + 90 dage +
metodeafsnit + "Hvor jeg ville starte" side 3, kravmatrix side 4. Format per master/README.md.

STILVALG (master/STILREGISTER.md; godkendt af scripts/style_guard.py, 3/3 skift mod #222):
  register      = KUNDESERVICE — telefonen, kunden, teknikeren i bilen, koordinatoren ved tavlen,
                  aftalen der skal holde. Sidst #196.
  åbningsgreb   = B (NEGATIONEN) — det er ikke anlægget, der vælter en serviceafdeling, men de fem
                  minutter ingen havde planlagt. Sidst #216.
  struktur      = PROBLEMKATALOGET — fire navngivne problemer: teknikeren med et halvt svar ·
                  koordinatoren der lover en tid · det lille projekt der aldrig bliver et projekt ·
                  kunden der hører om det som en regning. Sidst #217.
  kadence       = korte sætninger med et klokkeslæt, et anlæg eller en person i hver anden linje.

KULTURSYNKRONISERING (policy 04.11.2026), kilder i master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md
§194:
  **airteam a/s** — dansk ventilationsentreprenør, grundlagt **1998**, **15 lokationer i Danmark og
  Sverige**, **400+ medarbejdere**, **6.000+ gennemførte projekter**, "Danmarks største
  ventilationsentreprenør" (opslagets eget udsagn), mission: **"Nordens foretrukne
  ventilationspartner"** og "godt indeklima til gavn for danskernes sundhed". Kunder nævnt i
  opslaget: **lejlighedskomplekser, hospitaler, kontorhuse, fabrikker, hoteller og
  medicinalfirmaer**. Kulturord fra opslaget: **frihed under ansvar**, **godt humør**,
  **vidensdeling**, personlig og faglig udvikling, **sundhed og trivsel**, **airteam Academy**,
  pension, tandforsikring og sundhedsforsikring. **Roskilde-afdelingen** ligger på **Langebjerg 4,
  4000 Roskilde**; serviceafdelingen består ifølge opslaget af **5 serviceteknikere** og **3
  servicekoordinatorer**, og stillingen **assisterer servicechefen**. **Servicechef i Roskilde:
  Henrik Albertsen** (heal@airteam.dk, 51 17 53 71) — navnet er hentet fra airteam.dk/kontakt
  (okt. 2026) og nyheden af 1. juni 2026 om hans skifte fra servicechef i Københavns Lufthavn til
  Roskilde; **opslaget selv navngiver ingen kontaktperson**, så brevet er stilet til ham med
  forbehold. **Københavns Lufthavn:** airteam har ventilationsentreprisen på **T3AE (Terminal 3
  Airside Expansion)** — bygherre **Københavns Lufthavn A/S**, totalentreprenør **Per Aarsleff**,
  **100.000 m²**, ventilationsentreprisen **830.000 m³/h**, **12 brandventilationsanlæg på 840.000
  m³/h**, **32 udsugningsanlæg**, **3 indblæsningsanlæg** og arbejde på **25 eksisterende anlæg**,
  periode **2021-2028**; tidligere **Finger E etape 2** (afsluttet sommeren 2020) og **Terminal 3
  airside** med **23 nye anlæg** på ca. **450.000 m³/h** og brand/røg på ca. **750.000 m³/h**.

Ingen opdigtede fakta. Dokumenteret grundlag: **Ventek Air ApS** (Vedbæk) 2022 — ventilations-,
køle- og CTS-virksomhed med hospitaler, laboratorier og forskningsinstitutioner som kunder — hvor
han var **projekt- og værkstedsleder for 14 medarbejdere** med **11 samtidige entrepriser**,
leverandører og underentreprenører; **ELOHVAC** siden 2023 med fuldt **P&L**, **serviceaftaler med
responstid**, reservedele og **5 elektrikere + 3 lærlinge**; **Biofos/Lynetten** 2017-2022 som
drifts- og vedligeholdelseschef med **ventilation, køl, pumper, HV-tavler og SRO/SCADA** i
**24/7-drift**, **APV**, **LOTO**, beredskab og myndighedsdokumentation; **Novo Nordisk** 2022-2024
med **37 anlægsprojekter**, 25 specialister, FAT/SAT, nul kritiske fund og ændringsstyring i
**SAP**; **ARJ** 2003-2010 med **12 teknikere**; **elautoriseret maskinmester** LV/MV/HV (maj 2023),
**B.Tech** maskinteknik (EQF 6, 7,6/12), el- og maskinteknisk design (EQF 6), **køle- og VVS-teknik**
(AMU 2021), **Lean 5S/PDCA/VSM/A3** (2021); dansk modersmål, engelsk professionelt; **kørekort B**;
bor i **Måløv** (ca. 40 km til Roskilde, ca. 35 km til Kastrup).
**Bevidst formulering:** ingen påstand om at være **VVS-installatør**, om at have udført
**indregulering** eller **SFP-målinger** som fagperson, om **airside-adgang** i lufthavnen eller om
at have arbejdet i **luftfartsmiljø**. Ventilation erfaring er beskrevet, som den er: entreprise,
service og drift — ikke som montagefag.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Service-projektleder · ventilation, service og indeklima · Roskilde og CPH'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4. november 2026")
    m.meta("Serviceprojektleder · Serviceafdelingen i Roskilde · fast dag om ugen i Københavns Lufthavn")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Service-projektleder til serviceafdelingen", bold=True, color='1A1A1A')
    m.para("Kære Henrik,", after=60)

    # ---------------------------------------------------------------- side 1
    m.para("**Det er ikke anlægget, der vælter en serviceafdeling. Det er de fem minutter, ingen havde "
           "planlagt.** 07:40 ringer en kunde, fordi der er stuff i et klasseværelse. 07:45 lover "
           "koordinatoren en tekniker inden frokost. 08:20 kører han uden at vide, hvilket anlæg det "
           "er, om der er adgang, og hvad der blev gjort sidst. 10:10 er han der. Ingen af de fire "
           "minutter var et teknikerproblem — de var planlægning, information og en aftale, der ikke "
           "holdt.", after=80)

    m.para("**airteam er Danmarks største ventilationsentreprenør** — grundlagt i 1998, **15 "
           "lokationer** i Danmark og Sverige, mere end **400 medarbejdere** og over **6.000 "
           "gennemførte projekter**. I Københavns Lufthavn er I midt i **T3AE**: **100.000 m²**, en "
           "ventilationsentreprise på **830.000 m³/h**, **12 brandventilationsanlæg** på 840.000 "
           "m³/h, **32 udsugningsanlæg** og arbejde på **25 eksisterende anlæg** frem mod 2028. Det "
           "er den slags anlæg, hvor en serviceaftale ikke er en telefonlinje, men en driftskontrakt "
           "med navn på.", after=80)

    m.para("**1. Teknikeren står i marken med et halvt svar.** Det sker, fordi historikken sidder i "
           "hovedet på den, der havde opgaven sidst. Jeg vil have, at hver sag møder teknikeren med "
           "anlæg, adresse, adgang, ansvarlig og sidste udførte arbejde — og at det står skrevet, "
           "inden han sætter sig i bilen. Jeg har gjort det samme med skabeloner og kontrolpunkter på "
           "37 anlægsprojekter, og det virkede, fordi teknikerne selv havde været med til at lave "
           "dem.", after=70)

    m.para("**2. Koordinatoren lover en tid, teknikeren ikke kan holde.** Det er ikke ond vilje; det er "
           "to kalendere, der ikke kender hinanden. Fem teknikere og tre **servicekoordinatorer** skal "
           "dele én virkelighed: hvem der er hvor, hvad der haster, og hvad der må vente til i morgen. "
           "**Bemanding** og **ressource** skal besluttes på et tal, ikke på en fornemmelse — og når "
           "dagen vælter, skal det være aftalt på forhånd, hvad der ryger først.", after=70)

    m.para("**3. Det lille projekt bliver aldrig et projekt.** En **energioptimering** eller en "
           "**ombygning** af et indblæsningsanlæg bliver født som en god idé i en telefonsamtale og "
           "dør som en uafsluttet seddel. Den skal have det samme som de store: en aftale, en pris, en "
           "mand og en dato — ellers bliver den hverken tjent eller afleveret. Jeg har stået med 11 "
           "samtidige entrepriser og med 37 projekter under GMP; forskellen på dem og på en seddel er "
           "systematik, ikke størrelse.", after=70)

    m.para("**4. Kunden hører om problemet som en regning.** Når den første besked er en faktura, har "
           "**kommunikation**en fejlet en måned tidligere. En kunde, der bliver ringet op inden "
           "problemet vokser, betaler hellere for den rigtige løsning — og ringer igen næste gang. "
           "Det er den del af rollen, jeg holder mest af: **teknisk support** til teknikeren og "
           "sparring med kunden i samme telefon.", after=80)

    m.para("**Lufthavnsdagen.** Én fast dag om ugen i CPH er ikke en pendlerdag, det er den dag, hvor "
           "de små sager bliver til noget: gennemgang af de **25 eksisterende anlæg** sammen med jeres "
           "teknikere, aftalt med lufthavnen og totalentreprenøren, og skrevet ned, inden jeg kører "
           "hjem. Jeg vil bruge den dag på at være der, hvor kunden er — ikke på at sidde i Roskilde og "
           "gætte.", after=80)

    m.para("**Om kulturen.** **Frihed under ansvar** og **vidensdeling** er let at skrive og svært at "
           "praktisere i en afdeling, hvor telefonen ringer. Det bliver kun til noget, hvis der er "
           "**kurser** og en rytme, hvor den, der lige har løst en svær sag, fortæller hvordan. "
           "airteam Academy — jeres eget **akademi** — er den ramme, jeg helst vil arbejde i, fordi "
           "den gør faglig udvikling til en kalender og ikke til et løfte.", after=80)

    m.para("**Hvad jeg ikke har.** Jeg er ikke **VVS-installatør**, og jeg har ikke selv stået for "
           "**indregulering** eller målt **SFP** som fagperson — det ville jeg lære af jeres teknikere. Jeg er "
           "elautoriseret **maskinmester** med fire år i teknisk drift af ventilation, køl og pumper, "
           "et år som leder i **ventilationsbranchen** og **serviceaftaler** med **responstid** i min "
           "egen virksomhed. Lufthavnens adgangs- og sikkerhedsregler kender jeg ikke; dem regner jeg "
           "med at blive indkørt i, som alle andre.", after=80)

    m.para("**Praktisk.** Jeg bor i Måløv — ca. 40 km til Roskilde og ca. 35 km til Kastrup, og **én "
           "fast dag om ugen i lufthavnen** passer fint i min uge. **Kørekort B**. **Dansk** "
           "modersmål, **engelsk** professionelt. Kan tiltræde efter aftale.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Leder af teknikere og service i tolv år — fire år som drifts- og vedligeholdelseschef på "
           "et 24/7-anlæg med **ventilation**, køl og pumper, et år som projekt- og værkstedsleder i "
           "en **ventilationsvirksomhed** med 14 medarbejdere, og siden 2023 eget selskab med "
           "**serviceaftaler**, **responstid**, **projektledelse** og fuldt P&L. Vant til at være bindeled mellem kunde, "
           "kontor og tekniker — og til at tage telefonen, når det gælder.", after=80)

    m.section("VENTILATION OG INDEKLIMA")
    for label, body in [
        ("Anlæg i drift",
         "Ventilations-, køle- og pumpesystemer i 24/7-drift med **SRO/SCADA**, alarmer og akut "
         "fejlfinding — **indeklima** som en driftsopgave, ikke et projekt."),
        ("Ventilationsentreprise",
         "Projekt- og værkstedsleder i **Ventek Air** (ventilation, køl og **CTS**) med hospitaler og "
         "laboratorier som kunder — 14 medarbejdere og 11 samtidige opgaver."),
        ("Komponenter og system",
         "Kanaler, **filter**, spjæld, **VAV** og **brandventilation** kendt fra tavler, tegninger og "
         "driftsinstrukser; **luftmængde** og tryk læst i drift, ikke gættet."),
    ]:
        m.bullet(label, body)

    m.section("SERVICE, KUNDER OG KOORDINERING")
    for label, body in [
        ("Serviceaftaler",
         "Aftaler med **responstid**, faste tilsyn og reservedele på lager — solgt som en aftale og "
         "leveret som en kalender, kunden kan regne med."),
        ("Kunden i telefonen",
         "Besigtigelse, **tilbud** og opfølgning på samme sag; kunden hørt før problemet blev en "
         "faktura, og teknikeren briefet, før han kørte."),
        ("Bindeled",
         "Opgaven gået fra kunde til koordinator til tekniker uden at tabe information — skrevet ned, "
         "ikke husket."),
    ]:
        m.bullet(label, body)

    m.section("DRIFT, BEMANDING OG PROJEKTER")
    for label, body in [
        ("Bemanding",
         "Vagtplan og **ressource**styring for 5-14 medarbejdere og 12 teknikere; prioritering af "
         "dagens, ugens og sæsonens opgaver skrevet ned og fulgt op."),
        ("Mindre projekter",
         "Energi- og ombygningsopgaver styret med aftale, pris, ansvarlig og aflevering — samme "
         "skabelon som de store, blot mindre."),
        ("Økonomi og dokumentation",
         "Fuldt P&L i eget selskab, ændringsstyring i **SAP** og **dokumentation**, der kan læses af "
         "den næste."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Ejer / teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · fuldt P&L · serviceaftaler med responstid · tilbud")
    m.bullet("Service som forretning",
              "Aftaler med **responstid**, udrykning, reservedele og **tilbud** — og en kalender, der "
              "skal hænge sammen med det, der blev lovet.")

    m.job("Senior idriftsættelsesingeniør / projektleder",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024",
          scope="37 anlægsprojekter · 25 specialister · FAT/SAT · SAP · myndighedsdokumentation")
    m.bullet("Små og store projekter med samme rytme",
              "Prøver før overlevering, afvigelser lukket med navn og dato og nul kritiske fund ved "
              "aflevering.")

    m.job("Projekt- og værkstedsleder", "Ventek Air ApS · Vedbæk · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · ventilation, køl og CTS · eget værksted")
    m.bullet("Teknikere i marken, kunder i røret",
              "Dagens opgaver fordelt på 14 mand og 11 sager — ventilation til hospitaler, "
              "laboratorier og undervisningsbyggerier, hvor indeklimaet ikke må svigte.")

    m.job("Drifts- og vedligeholdelseschef", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="24/7-drift · ventilation, køl, pumper, HV-tavler, SRO/SCADA · beredskab")
    m.bullet("Anlæg der ikke må stoppe",
              "Fem år med alarmer, tilsyn og akutopkald om natten; **arbejdsmiljø** med **APV** og "
              "**LOTO** som fast praksis og en beredskabsplan, der blev brugt, ikke bare skrevet.")

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
           "**Persisk:** modersmål · **Bor i Måløv** — ca. 40 km til Roskilde og ca. 35 km til "
           "Kastrup · **Kørekort B** · **IT** og **Office** i daglig brug · Kan tiltræde efter aftale "
           "· Referencer efter aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA TELEFONEN TIL KALENDEREN",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–2",
             "Kør med på arbejdet: to dage i Roskilde, én dag i lufthavnen, en tur med hver af de fem "
             "teknikere og en formiddag ved koordinatorens telefon. Læs de sidste tre måneders "
             "serviceordrer igennem — ikke for at finde en skyldig, men for at se, hvor de stoppede. Det er "
             "**driftsoptimering** med jord under neglene."),
            ("Dag 30",
             "En liste over de ti opgavetyper, der oftest går galt, med et forslag pr. punkt: "
             "information, bemanding eller aftale. Gennemgået med **servicechefen** og teknikerne, før "
             "den går videre."),
            ("Dag 60",
             "Én arbejdsgang flyttet fra hoved og seddel til system — den, der irriterer mest — og et "
             "fast overblik over ugen, som både **servicekoordinatorer** og teknikere kigger på om "
             "morgenen."),
            ("Dag 90",
             "De første mindre projekter kørt med aftale, pris og aflevering, en **responstid** der "
             "kan måles, og et tal på, hvor mange sager der blev løst i første besøg — før og efter."),
        ],
        widths=(1500, 8830))

    m.section("EN SERVICEAFDELING SÆLGER IKKE VENTILATION. DEN SÆLGER NÆSTE ÅR")
    m.para("Anlægget er solgt én gang. Serviceaftalen sælges hvert år, og den sælges på det, kunden "
           "oplevede sidst: kom der en, da der blev ringet, og virkede det bagefter? Derfor er "
           "**responstid** og **dokumentation** ikke administration — de er produktet.", after=70)

    m.section("PRIORITERING ER ET TAL, IKKE EN FORNEMMELSE")
    m.para("Fem teknikere og tre koordinatorer kan ikke prioritere sig til enighed hver morgen. "
           "Akut, aftalt og planlagt skal være tre kategorier med hver sin regel for, hvad der "
           "afbryder hvad — og når dagen vælter, skal alle vide, hvad der rykker først. Jeg har prøvet "
           "at drive et anlæg, hvor en times stop kunne mærkes, og det giver en respekt for "
           "**bemanding**, der er svær at læse sig til.", after=70)

    m.section("DET LILLE PROJEKT SKAL HAVE SAMME PAPIR SOM DET STORE")
    m.para("En **energioptimering** eller en **ombygning** af et anlæg skal have en aftale med "
           "omfang, pris, ansvarlig og afleveringsdato, før nogen tager værktøj med. Ellers bliver "
           "den en gave, og gaver tjener man ikke penge på — og kunden får ikke den dokumentation, "
           "vedkommende har betalt for. På 37 anlægsprojekter lærte jeg, at det er skabelonen og "
           "rytmen, der gør arbejdet ensartet, ikke størrelsen.", after=70)

    m.section("KUNDEN SKAL HØRE DET FRA OS, FØR DET STÅR I EN FAKTURA")
    m.para("Dårlig service er sjældent en tekniker, der ikke kunne sit fag. Det er en kunde, der "
           "måtte ringe to gange. Derfor ringer jeg tilbage, når jeg har besluttet noget — også når "
           "beslutningen er, at det bliver dyrere, end vi sagde. **Kommunikation** er ikke et "
           "høflighedstillæg; det er det, der gør, at næste sæson ikke skal vindes forfra.", after=70)

    m.section("INDEKLIMA ER ET TAL, KUNDEN KAN MÆRKE — OG ET TAL, VI SKAL KUNNE VISE")
    m.para("Træk, støj, temperatur og **luftmængde** bliver diskuteret som smagssager, indtil nogen "
           "måler. Derfor skal en serviceordre slutte med en måling eller en tydelig grund til, at der "
           "ikke blev målt: det er kundens **dokumentation**, og det er vores eget grundlag, når "
           "anlægget skal **driftsoptimeres** næste gang. Jeg har prøvet at drive ventilation uden at "
           "kunne vise, hvad der var galt — og at kunne vise det bagefter er hele forskellen, når "
           "kunden spørger, hvorfor regningen ser ud, som den gør.", after=70)

    m.section("HVOR JEG VILLE STARTE")
    m.para("Ved telefonen. Første uge: en formiddag ved koordinatoren, en dag i lufthavnen og en tur "
           "med hver af de fem teknikere — og de sidste tre måneders sager læst igennem. Derefter tage "
           "de ti opgavetyper, der oftest stopper, og se, om forskellen ligger i information, "
           "bemanding eller aftalen. Det er der, en serviceafdeling bliver bedre, og det er der, "
           "kunderne kan mærke det.", after=0)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "KRAV I OPSLAGET — DET HAR JEG",
        ["Krav i opslaget", "Dokumentation"],
        [
            ("Sikre fortsat drift af **serviceafdelingen**",
             "Fire år som drifts- og vedligeholdelseschef på et **24/7**-anlæg og siden 2023 eget "
             "selskab med **serviceaftaler** og udrykning — daglig drift er den vare, jeg har leveret "
             "længst."),
            ("Styring af mindre projekter som fx **energioptimering** eller mindre **ombygning**er",
             "37 anlægsprojekter med FAT/SAT og aflevering (Novo Nordisk) og 11 samtidige entrepriser "
             "(Ventek Air); små opgaver kørt med aftale, pris og ansvarlig."),
            ("Sikre **værdiskabende løsninger** for vores kunder",
             "Serviceaftaler med **responstid** og faste tilsyn; tilbud og besigtigelse på samme sag, "
             "så kunden får en løsning og ikke en regning."),
            ("Arbejde minimum én fast dag om ugen fra **Københavns Lufthavn**",
             "Bor i Måløv, ca. 35 km fra Kastrup; **kørekort B** og vant til at være på flere "
             "lokationer i samme uge."),
            ("Assistere **servicechefen** i en afdeling med 5 **serviceteknikere** og 3 "
             "**servicekoordinatorer**",
             "Ledererfaring med 5 elektrikere + 3 lærlinge, 14 medarbejdere og 12 teknikere; vant til "
             "at være nummer to i en struktur og tage ansvar for dagens beslutninger."),
            ("Opsøge nye muligheder og være med til at udvikle **forretning**en",
             "Eget selskab med fuldt P&L og egen kundebase; serviceaftaler, reservedele og "
             "opgraderinger solgt som en pakke, ikke som en timepris."),
            ("Tage **initiativ**, åbne nye døre og omsætte muligheder til konkrete projekter",
             "Arbejdsgange indført på 37 anlæg og i eget selskab; nye kunder og nye aftaler skabt fra "
             "nul siden 2023."),
            ("**Planlægning og prioritering** af serviceopgaver i afdelingen",
             "Vagtplan og ruter for 5-14 medarbejdere; akut, aftalt og planlagt som tre kategorier "
             "med hver sin regel."),
            ("Sikre effektiv drift, herunder **bemanding** og **ressource** styring",
             "Bemanding og materiel styret på 11 entrepriser og i 24/7-drift med beredskab; "
             "kapacitet flyttet, før flaskehalse blev til forsinkelser."),
            ("**Teknisk support** og sparring til teknikerne i marken og med kunderne",
             "Fagligt ansvar for ventilation, køl, pumper, HV-tavler og SRO/SCADA; elautoriseret "
             "maskinmester LV/MV/HV og den, teknikerne ringede til."),
            ("Sikre god **kommunikation** mellem serviceteknikere, koordinatorer og kunder",
             "Kunde, kontor og tekniker holdt sammen af skriftlige aftaler; tilbagemelding til kunden, "
             "også når svaret var dyrere end ventet."),
            ("Baggrund som **maskinmester**, ingeniør, VVS-installatør eller lignende",
             "**Elautoriseret maskinmester** (maj 2023), **B.Tech** maskinteknik (EQF 6, 7,6/12) og "
             "el- og maskinteknisk design (EQF 6)."),
            ("Erfaring fra **ventilationsbranchen** i en lignende lederrolle",
             "**Ventek Air** 2022: projekt- og værkstedsleder for 14 medarbejdere med ventilation, "
             "køl og **CTS** til hospitaler og laboratorier — 11 samtidige opgaver."),
            ("Rutineret i **IT** og erfaren bruger af **Office**-pakken",
             "**SAP** til ændringer og økonomi, **SRO/SCADA** til drift, Office til tilbud, "
             "tidsplaner og opfølgning hver uge."),
            ("Gyldigt **kørekort**",
             "**Kørekort B**; vant til at være på flere lokationer i samme uge — Roskilde, Kastrup og kunderne imellem."),
            ("**Pålidelig**, **udadvendt**, **relationsskabende** og **serviceminded**",
             "Tolv år med kunder og teknikere: aftaler holdt, kunden ringet op først og relationer "
             "bygget på, at det passede, næste gang der blev ringet."),
            ("Være bindeleddet mellem kontoret, teknikerne og kunderne",
             "Opgaven gået fra kunde til koordinator til tekniker uden at tabe information — i eget "
             "selskab, på 11 entrepriser og i 24/7-drift."),
            ("Kombination af stærk **teknisk indsigt**, ledelse og **kundefokus**",
             "Elautoriseret maskinmester med fire år i teknisk drift og et år som leder i "
             "ventilationsbranchen; kundekontakt og tilbud i eget selskab siden 2023."),
            ("Bidrage til væksten i og omkring **CPH Lufthavn**",
             "Nye kunder og nye aftaler skabt fra nul i eget selskab; ingen erfaring fra lufthavnen i "
             "dag, men en fast dag om ugen sat af til at være til stede, hvor kunden er."),
            ("Fokus på **sundhed og trivsel** blandt medarbejderne",
             "**Arbejdsmiljø** med **APV**, sikkerhedsrundering og opfølgning i fire år; MUS og "
             "oplæring af lærlinge og teknikere i alle lederroller."),
            ("Motiveres af at skabe resultater og levere på et højt teknisk serviceniveau",
             "Serviceaftaler med målt **responstid**, nul kritiske fund ved aflevering og et selskab, "
             "der leverer det, der blev solgt."),
        ],
        widths=(3600, 6746))

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_airteam_ServiceProjektleder.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_airteam_ServiceProjektleder.docx'))
