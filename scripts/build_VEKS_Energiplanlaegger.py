# -*- coding: utf-8 -*-
"""VEKS I/S — energiplanlægger, Team Plan & Kontrakt, Glostrup.

Dansk opslag → dansk dokument (da-DK): ansøgning side 1, CV side 2, uddannelse + 90 dage +
fire afsnit side 3, kravmatrix side 4.

STILVALG (master/STILREGISTER.md, policy 04.11.2026; kørt gennem scripts/style_guard.py,
3/3 skift mod #196):
  register      = KOMMERCIEL-FORRETNINGSMÆSSIG — tal, beslutning, kunde, hvad det koster.
                  Rollen er forretningsudvikling i et non-profit forsyningsselskab: beslutningen
                  skal kunne tåle at blive læst af en bestyrelse. Sidst brugt #190.
  åbningsgreb   = D (TALLET) — "tolv kommuner hæfter solidarisk". Sidst brugt #183-området.
  struktur      = BESLUTNINGSKÆDEN — samme greb som #193, men med en klar ny vinkel: kæden løber
                  på penge og tilslutningsvillighed (potentiale → pris → projektforslag →
                  beslutningsgrundlag → udrulning), ikke på standarder og målinger.
                  Sidst brugt #193.
  kadence       = ét led ad gangen, altid med hvem der beslutter, og hvad der står på spil.

Ingen opdigtede fakta: der påstås IKKE erfaring med varmeplaner, varmeforsyningslovens
projektforslag, kommunale godkendelsesprocesser eller fjernvarmedrift. Det dokumenterede grundlag
er elautoriseret maskinmester (LV/MV/HV), el- og maskinteknisk design (EQF 6), B.Tech i
teknologiledelse og maskinteknik, 37 samtidige CAPEX-projekter med økonomi og risici, fuldt
P&L-ansvar siden 2023, investeringsmodeller (NPV/IRR, følsomhed, scenarier), datamodeller i
Power BI/Python, månedsrapportering til ledelse og bygherre samt køleteknik og varmeanlæg i drift.

Policy: master/README.md — jobbet først, kandidaten kun som bevis, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Energiplanlægger · Udrulning, beslutningsgrundlag og økonomi'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4. november 2026")
    m.meta("VEKS · Energiplanlægger, Team Plan & Kontrakt · Fabriksparken 58A, 2600 Glostrup")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: energiplanlægger — Plan & Kontrakt", bold=True, color='1A1A1A')
    m.para("Til teamleder Sanne Rendal", after=70)

    # ---------------------------------------------------------------- side 1
    m.para("**Tolv kommuner hæfter solidarisk for VEKS' økonomi.** Det gør en beslutning om at føre "
           "**fjernvarme** ind i et nyt kvarter i **Køge** til noget andet end en teknisk beslutning: "
           "den er økonomisk, den er politisk, og den skal kunne læses af en **bestyrelse**, der ikke "
           "er ingeniører. Det er den slags beslutningsgrundlag, jeg gerne vil være med til at bygge "
           "— og det er der, min erfaring faktisk ligger.", after=80)

    m.para("**Potentialet.** En **udrulning** starter ikke med et rør, men med et spørgsmål: hvor "
           "mange kunder kan vi få, hvad koster deres nuværende varme, og hvad skal der til, for at de "
           "skifter? **Tilslutningsvillighed** er ikke en følelse, den er et regnestykke — og det "
           "regnestykke skal bygges på data om bygninger, varmekilder og alternativer, ikke på det "
           "område, nogen helst vil have med. Jeg har bygget en **datamodel** i **Power BI** og "
           "**Python** og ved, at det sjældne problem er at få tal; det svære er at blive enige om, "
           "hvad der skal tælles med.", after=80)

    m.para("**Prisen.** En **kampagnepris** er et tilbud, ikke en rabat. Den skal kunne forklares som "
           "en samlet økonomi for kunden — **tilslutningsaftale**, bidrag, **tarif** og forbrug over "
           "femten år — og den skal hænge sammen med **prisstruktur**en i resten af selskabet. Ellers "
           "sælger vi en indgang, kunden fortryder om tre år, og så koster det mere at håndtere end at "
           "vinde. Jeg har lavet tilbud og kalkulation med fuldt P&L-ansvar siden 2023 og lært, at en "
           "rabat, der ikke kan forklares, altid bliver dyr.", after=80)

    m.para("**Projektforslaget.** Her har jeg et ærligt hul: jeg har ikke skrevet **projektforslag** "
           "efter **varmeregulering**ens regler og ikke siddet i en kommunal "
           "**godkendelsesproces** ved siden af en **varmeplan**. Det er håndværk, der skal læres, og "
           "jeg vil hellere lære det af jer end gætte mig til det. Til gengæld har jeg skrevet de "
           "beskrivelser, der ligger bag, i 20 år: afgrænsning, forudsætninger, økonomi, "
           "konsekvenser — og ved, hvor et forslag bliver læst hen, når en myndighed eller en "
           "**bestyrelse** skal sige ja.", after=80)

    m.para("**Beslutningsgrundlaget.** Det er her, jeg kan bidrage fra dag et. Et "
           "**beslutningsgrundlag** er ikke en rapport, der viser, at vi har regnet; det er tre "
           "scenarier, der viser, hvad der sker med **business case**n, hvis **tilslutningsgrad**en "
           "bliver ti point lavere end antaget, og hvilken udrulningstakt der stadig er forsvarlig. Jeg "
           "har lavet **investeringskalkule**r med **NPV**, **følsomhed** og **scenarier** på 37 "
           "samtidige anlægsprojekter og rapporteret månedligt til ledelse og bygherre — og jeg ved, "
           "at en beslutningstager ikke har brug for flere tal, men for at vide, hvad der er det "
           "afgørende tal.", after=80)

    m.para("**Udrulningen.** Når beslutningen er taget, bliver den et projekt med en tidsplan, en "
           "entreprenør, en kunde, der skal have svar, og en kollega i en anden afdeling, der skal "
           "levere noget. Jeg har koordineret 14 mand og 11 samtidige entrepriser og 37 projekter på "
           "tværs af engineering, indkøb og anlæg — inklusive de uger, hvor planen ikke holdt, og hvor "
           "nogen skulle sige det højt før kunden opdagede det.", after=80)

    m.para("**Strategien.** En **energiplanlægger** i et selskab som VEKS arbejder ikke i et vakuum: "
           "hver udrulning skal hænge sammen med **forsyningssikkerhed**, økonomi og et tæt "
           "**samarbejde** med de lokale **fjernvarmeselskaber** og de tolv **kommuner**. Det gælder "
           "ikke mindst i **distributionsselskab**et, hvor forretningsudviklingen skal kunne ses i "
           "samme plan som transmissionen. Min rolle er at tænke den enkelte sag ind i det større "
           "billede — og at gøre det, så den, der står med **drift**en eller kunden, kan se, hvorfor.",
           after=80)

    m.para("**Hvad jeg ikke er, og hvad jeg er.** Jeg er ikke uddannet **energiplanlægger**, og jeg "
           "har ikke VEKS' historik i hovedet. Jeg er **elautoriseret maskinmester** med el- og "
           "maskinteknisk design (EQF 6) og B.Tech i teknologiledelse og maskinteknik, og jeg har "
           "brugt 20+ år på den side af bordet, hvor et teknisk valg skal forsvares i kroner og øre. "
           "Det, jeg kan levere fra første uge, er økonomien, dataene og formidlingen; det, jeg skal "
           "lære, er **regulering**en og planfaget. Det bytte vil jeg gerne lave, og jeg vil gerne sige "
           "det højt i stedet for at lade som om, jeg kan det hele.", after=80)

    m.para("Jeg bor i Måløv, har 25 minutter til **Glostrup** med bil og kan sagtens arbejde 1–2 dage "
           "om ugen i **Køge** — det er en del af rollen, ikke en undtagelse. Jeg har læst, at I gerne "
           "ser en start 1. januar 2027; det kan jeg indfri. Jeg har også bemærket, at I beder om, at "
           "man undlader foto og alder — det er der hverken billede eller fødselsdato i denne "
           "ansøgning.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Teknisk projekt- og økonomileder med 20+ års erfaring i anlægsprojekter, "
           "**investeringskalkule** og beslutningsmateriale — **elautoriseret maskinmester** "
           "(LV/MV/HV), el- og maskinteknisk design (EQF 6), B.Tech i teknologiledelse og "
           "maskinteknik. Har styret 37 samtidige CAPEX-projekter med fremdrift, økonomi og risici, "
           "haft fuldt P&L-ansvar siden 2023 og bygget **datamodel**ler og **KPI**-rapportering i "
           "**Power BI**, **Python** og SAP ERP.", after=80)

    m.section("ØKONOMI OG BESLUTNINGSGRUNDLAG")
    for label, body in [
        ("Investeringskalkule og scenarier",
         "NPV/IRR-modeller med følsomhed og scenarier til at vælge mellem reparation, udskiftning og "
         "nyinvestering; én **investeringskalkule** pr. beslutning, ikke ét regneark til alle."),
        ("Budget og opfølgning",
         "Budgettet, kalkulation og månedlig opfølgning på 37 projekter (DKK 2–10 mio.) og på egen "
         "virksomhed med fuldt P&L-ansvar — afvigelser forklaret, ikke bortforklaret."),
        ("Beslutningsmateriale",
         "Månedsrapportering til ledelse og bygherre samt materiale til godkendelse af investeringer: "
         "tre scenarier, det afgørende tal og en klar anbefaling."),
    ]:
        m.bullet(label, body)

    m.section("DATA, MODELLER OG FORMIDLING")
    for label, body in [
        ("Datamodel og dashboards",
         "Power BI, Python, Excel/Power Query og SAP ERP; datamodeller bygget selv, når værktøjet "
         "manglede — inklusive KPI-dashboards og automatiserede tjeklister."),
        ("Analyse og kvalitet i tal",
         "Kilderne dokumenteret, forudsætningerne skrevet ned og følsomheden vist, så en anden kan "
         "efterprøve regnestykket — det var kravet i GMP-miljø og er vanen i dag."),
        ("Formidling til ikke-teknikere",
         "Tekniske sammenhænge formidlet til ledelse, bygherre, entreprenør og myndighed; kort på "
         "skrift, klart i mødelokalet, på dansk og engelsk."),
    ]:
        m.bullet(label, body)

    m.section("PROJEKTER, INTERESSENTER OG DRIFT")
    for label, body in [
        ("Koordinering på tværs",
         "37 projekter og 25 specialister koordineret på tværs af engineering, indkøb og anlæg; 14 "
         "mand og 11 entrepriser styret med tavlemøder og flaskehalsanalyser."),
        ("Interessenter og aftaler",
         "Bygherre, entreprenør, underentreprenør og myndighed; aftalegrundlag, forbehold og "
         "forventningsafstemning — også når svaret var nej."),
        ("Teknisk forståelse i bund",
         "Køl, varme, ventilation, el og CTS samt fjernvarmenære anlæg som pumper, vekslere og "
         "styring fra drift og projektering; køleteknik som AMU-kursus."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Ejer / teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · fuldt P&L · projekter, tilbud og kalkulation")
    m.bullet("Forretning og økonomi",
              "Tilbud, kalkulation og investeringsvurdering; AI-værktøjer til tidsplaner, tjeklister "
              "og KPI — over 40 % produktivitetsløft på det administrative.")
    m.bullet("Kunde og beslutning",
              "Løsningsvalg præsenteret med pris, konsekvens og alternativ, så kunden kunne beslutte "
              "— og opfølgning, når beslutningen var taget.")

    m.job("Senior idriftsættelsesingeniør / projektleder, elsystem",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024",
          scope="37 samtidige anlægsprojekter · 25 specialister · DKK 2–10 mio. pr. projekt")
    m.bullet("Fremdrift, økonomi og risici",
              "Projektøkonomi og månedsrapportering i SAP ERP; risici håndteret før de blev "
              "afvigelser, og afvigelser lukket med rodårsagsanalyse — nul kritiske fund.")

    m.job("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · DKK 2–10 mio.")
    m.bullet("Koordinering og leverance",
              "Daglige tavlemøder og flaskehalsanalyser; udbud, tilbudslister og aflevering til "
              "kunden — og de svære samtaler, når kapaciteten ikke rakte.")

    m.job("Vedligeholdelses- og driftsleder", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="Renseanlæg i 24/7-drift · pumper, HVAC, højspændingstavler, SCADA")
    m.bullet("Drift, økonomi og forsyning",
              "Forebyggende vedligehold og investeringsprioritering i døgndrift; 5S og standard work "
              "på værksted og lager, LOTO og APV.")

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
    m.para("**Dansk:** modersmål · **Engelsk:** professionelt, skriftligt og mundtligt · **Persisk:** "
           "modersmål · **Bosat i Måløv**, ca. 25 minutter til Glostrup, villig til 1–2 dage om ugen i "
           "Køge · **Kan starte 1. januar 2027** · Referencer efter aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA POTENTIALE TIL BESLUTNING",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–2",
             "Læse det grundlag, der allerede findes: **varmeplan**er, tidligere "
             "**projektforslag**, **tilslutningsaftale**r og de **business case**s, der er sagt nej "
             "til. Spørge til, hvad der manglede i dem."),
            ("Dag 30",
             "Egen opgave leveret på et afgrænset område i **Køge**: et **beslutningsgrundlag** med "
             "tre scenarier for **tilslutningsgrad** og **prisstruktur**, gennemgået med en kollega før "
             "det går videre."),
            ("Dag 60",
             "Forslag til ensartet skabelon for **projektforslag** — hvilke forudsætninger der altid "
             "skal stå, og hvordan **økonomi**en præsenteres, så to forslag kan sammenlignes."),
            ("Dag 90",
             "Egen portefølje af udrulningssager med **opfølgning** mod **bestyrelse**-materialet; "
             "status med dig på, hvor jeg stadig skal sparre, og hvad jeg kan løfte alene."),
        ],
        widths=(1500, 8830))

    m.section("EN KAMPAGNEPRIS ER ET TILBUD, IKKE EN RABAT")
    m.para("Når en **kampagnepris** virker, er det ikke fordi, den er lav — det er fordi, kunden kan se, "
           "hvad den samlede økonomi bliver over femten år, og hvad alternativet koster. Når den ikke "
           "virker, er det ofte, fordi vi sammenlignede en engangspris med en månedlig regning og lod "
           "kunden regne resten selv. **Tilslutningsvillighed** er et spørgsmål om tillid til "
           "regnestykket, og den tillid bygges med **formidling**, ikke med rabat.", after=70)

    m.section("FØLSOMHED ER IKKE ET BILAG, DET ER SVARET")
    m.para("En **business case** uden **følsomhed** er en påstand. Det interessante er ikke, om "
           "**NPV** er positiv ved de forudsætninger, vi selv valgte; det er, hvor meget "
           "**tilslutningsgrad**en må falde, før beslutningen skifter fortegn. Det tal skal stå i "
           "materialet til **bestyrelsen**, for det er det, der gør en beslutning forsvarlig — også "
           "hvis udrulningen senere går langsommere, end vi håbede.", after=70)

    m.section("DET SVÆRE ER IKKE AT FÅ TAL — DET ER AT BLIVE ENIGE OM, HVAD DER TÆLLES")
    m.para("En **datamodel** bliver aldrig bedre end de aftaler, den bygger på: tæller vi kunder eller "
           "ejendomme, regner vi med eller uden varmt brugsvand, og hvad gør vi med dem, der har en "
           "varmepumpe i forvejen? De spørgsmål bliver ikke løst i regnearket; de bliver løst i et møde, "
           "og de skal skrives ned, før nogen regner videre. Jeg har prøvet at bygge modeller, hvor "
           "forudsætningerne var uenige i to afdelinger — og det var ikke modellen, der var problemet.",
           after=70)

    m.section("TOLV KOMMUNER BETYDER TOLV SLAGS SPØRGSMÅL")
    m.para("I et **interessentskab** som VEKS er der ikke én interessent, men tolv **kommune**r med "
           "hver deres politik, økonomi og borgere — og 19 **fjernvarmeselskaber** oveni, der hver "
           "især skal kunne se sig selv i planen. Det betyder ikke, at svaret skal være tolv "
           "forskellige; det betyder, at det samme svar skal kunne forklares på tolv måder. Den "
           "disciplin har jeg fra entrepriser, hvor bygherre, entreprenør og myndighed sjældent "
           "spurgte om det samme.", after=70)

    m.section("JEG HAR IKKE SKREVET EN VARMEPLAN — ENDNU")
    m.para("Jeg har ikke lavet **varmeplan**er og ikke arbejdet med **varmeregulering** i praksis, og "
           "jeg kender ikke hver eneste **godkendelsesproces** i de tolv kommuner. Det, jeg har, er "
           "tyve år med at bygge beslutningsgrundlag på tekniske forhold, som andre skulle sige ja "
           "til: økonomi, **potentiale**, **scenarier** og en klar anbefaling. Resten er fagligt "
           "håndværk, og det lærer man ikke ved at læse om det — man lærer det ved at lave det sammen "
           "med nogen, der har gjort det før.", after=0)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "HVAD STILLINGEN KRÆVER — HVAD JEG HAR LEVERET",
        ["Krav i opslaget", "Bevis"],
        [
            ("Erfaren energiplanlægger eller lignende uddannelsesmæssig baggrund",
             "Ikke uddannet energiplanlægger. Elautoriseret maskinmester (LV/MV/HV), el- og "
             "maskinteknisk design (EQF 6) og B.Tech i teknologiledelse og maskinteknik — med 20+ år "
             "i anlægsøkonomi og beslutningsgrundlag."),
            ("Indsigt i energisystemer, varmeplaner og varmereguleringen",
             "Energisystemer fra drift og projektering: køl, varme, ventilation, el og CTS samt "
             "pumper, vekslere og styring. Varmeplaner og varmeregulering er ikke arbejdet med — det "
             "er den vigtigste ting, jeg skal lære."),
            ("Erfaring med udarbejdelse af projektforslag",
             "Ikke projektforslag efter varmeforsyningsloven. Beskrivelser, afgrænsning, "
             "forudsætninger og konsekvenser skrevet i 20 år — som udbudsmateriale, "
             "projektgrundlag og afvigelsesrapporter."),
            ("Kendskab til politiske godkendelsesprocesser",
             "Ikke kommunale godkendelsesprocesser for fjernvarme. Politiske og myndighedsmæssige "
             "processer kendt fra byggeri og anlæg, hvor et ja skulle hentes hos bygherre, kommune "
             "eller myndighed."),
            ("Koordinering af udrulningsprojekterne i Køge Fjernvarme",
             "11 samtidige entrepriser og 14 mand koordineret; 37 samtidige anlægsprojekter med "
             "fremdrift, økonomi og risici. Udrulning i Køge læres i de første uger på gulvet."),
            ("Sikre at projektforslag udarbejdes på ensartet grundlag",
             "Ensartet grundlag er noget, jeg har bygget: skabeloner, tjeklister og fælles "
             "forudsætninger på 37 projekter, så to sager kunne sammenlignes uden at starte forfra."),
            ("Sparring om prisstruktur, kampagnepriser og tilslutningsaftaler",
             "Pris, kalkulation og aftalegrundlag med fuldt P&L-ansvar siden 2023; "
             "investeringsmodeller brugt til at vise, hvad en pris gør ved økonomien over tid."),
            ("Materiale der danner beslutningsgrundlag for ledelse og bestyrelse",
             "Månedsrapportering til ledelse og bygherre på 37 projekter; investeringsmateriale med "
             "scenarier, følsomhed og en klar anbefaling — kort nok til at blive læst."),
            ("Delopgaver der understøtter VEKS' strategi",
             "Delopgaver løftet på tværs af organisationen i alle roller: fra KPI-dashboards til "
             "arbejdsmiljø og kompetencematrix — med fokus på det, der flyttede noget."),
            ("Langsigtet planlægning for udrulning af fjernvarme i Køge",
             "Langsigtet planlægning som disciplin: 37 projekter over 20 måneder med rullende "
             "fremdriftsplan og prioritering mellem konkurrerende hensyn. Køge specifikt skal læres."),
            ("Struktureret tilgang, strategisk tæft og fremsynethed ift. regulatoriske tiltag",
             "Struktureret: A3, PDCA og standard work. Regulatorisk fremsyn: arbejdet under BEK 1608, "
             "DS/HD 60364 og GMP/FDA/EMA-krav, hvor ændrede krav flyttede hele planen."),
            ("Tilslutningsvillighed, kampagnepriser og potentialer for overskudsvarme",
             "Potentiale og villighed regnet som kundens samlede økonomi i egen virksomhed; "
             "overskudsvarme har jeg ikke regnet på, men jeg har arbejdet med spildvarme og "
             "varmegenvinding i ventilation og køl."),
            ("Arbejde på tværs af teamet og VEKS' øvrige afdelinger",
             "Tværfagligt arbejde som standard: engineering, indkøb, produktion, salg og myndighed i "
             "37 projekter og 11 entrepriser; ingen af dem blev løst inden for én afdeling."),
            ("Tænke enkelte løsninger ind i et større perspektiv",
             "Enkeltløsninger vurderet mod helheden: en investering i ét anlæg forklaret mod "
             "driftsøkonomi, forsyningssikkerhed og de næste ti års behov."),
            ("Skabe og vedligeholde samarbejdsrelationer til kolleger, ledelse og samarbejdspartnere",
             "Relationer vedligeholdt over år med bygherre, entreprenør, underentreprenør og "
             "myndighed; også når uenigheden var faglig og ikke personlig."),
            ("Struktureret, metodisk, vedholdende og skarp faglig formidling",
             "Metodisk arbejde dokumenteret i A3 og projektmodeller; formidling på dansk og engelsk "
             "til ledelse, teknikere og kunder — og til bestyrelsesniveau, når det krævedes."),
        ],
        widths=(3600, 6746))

    m.section("ET PROJEKTFORSLAG SKAL KUNNE LÆSES AF EN, DER IKKE ER INGENIØR")
    m.para("Et **projektforslag**, der kun giver mening for den, der har skrevet det, bliver godkendt "
           "eller afvist på et forkert grundlag. Derfor skal forudsætningerne stå først — hvad er "
           "antaget om **tilslutningsgrad**, hvad koster alternativet, og hvad sker der, hvis "
           "antagelsen ikke holder. Det er ikke en indrømmelse af usikkerhed; det er den eneste måde, "
           "en **bestyrelse** kan træffe en beslutning, den stadig kan stå inde for om to år.", after=70)

    m.section("HVOR JEG VILLE STARTE")
    m.para("Med at læse de **projektforslag** og beslutningsoplæg, der allerede findes, og spørge til "
           "det ene: hvilket tal var det, beslutningen vendte på? Derefter tage en enkelt sag i "
           "**Køge** og bygge grundlaget om, så det kan læses af en, der ikke var med i mødet — og se, "
           "om konklusionen holder. Hvis den gør, er der en skabelon; hvis den ikke gør, er der noget, "
           "vi skal vide, før vi lover en udrulning.", after=0)

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_VEKS_Energiplanlaegger.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_VEKS_Energiplanlaegger.docx'))
