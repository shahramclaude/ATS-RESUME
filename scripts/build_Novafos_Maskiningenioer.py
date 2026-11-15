# -*- coding: utf-8 -*-
"""Novafos — Maskiningeniør til driftsoptimering og udvikling af vandforsyningen (Hørsholm).

Dansk opslag -> dansk dokument, 4 sider: brev s.1, CV s.2, uddannelse + 90-dages-tabel +
metodeafsnit s.3, 18-rækkers kravmatrix s.4.

STILVALG (master/STILREGISTER.md; godkendt af scripts/style_guard.py, 3/3 skift mod #205):
  register      = RÅDGIVENDE (beslutningsgrundlag, interessent, leverance, opfølgning). Sidst
                  #195. Rollen ER et beslutningsgrundlag: analyser, data, kriterier og
                  afrapportering, der skal kunne bruges af driften.
  åbningsgreb   = I (TESERNE) — tre påstande om, hvornår en optimering bliver til noget i
                  driften. Sidst #196.
  struktur      = FØR/EFTER — vandforsyningen i dag -> om tolv måneder, punkt for punkt, hvor
                  hvert par er beviset for en af teserne. Sidst #194.
  kadence       = korte, konstaterende sætninger; tal og enheder (m³, kWh, tryk, flow) frem for
                  tillægsord; ingen personbeskrivelse.

KULTURSYNKRONISERING (policy 04.11.2026): Novafos' egne ord bærer teksten — *hverdagsmestre i
at håndtere vand*, *stabil forsyning*, *drifts- og energioptimering*, *beslutningsgrundlag*,
*tilstandsbaseret vedligehold*, *forankring*, *bæredygtighed*, *klimasikring*, *de ni kommuner*,
*Sjælsø Vandværk*, *SRO*. Research: ~350–400 medarbejdere, 430.000+ forbrugere, ni kommuner,
ca. 1.000 målere der sender data døgnet rundt, Power BI-platform til driftsoptimering og
energiforbrug pr. pumpestation (Initiate-case), samtaler fra uge 48, opstart 1. februar 2027.

Brugerens oplysninger (04.11.2026, spurgt før byg): PowerBI er IKKE brugt — rapporter bygges i
Excel og egne AI-værktøjer; tilstandsbaseret vedligehold ER opbygget; energibesparelser kan
dokumenteres med tal (over 40 % lavere energiforbrug, jf. PDCA-programmet). Ingen opdigtede tal.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Maskiningeniør · driftsoptimering, energi og tilstandsbaseret vedligehold'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4. november 2026")
    m.meta("Novafos · Maskiningeniør til driftsoptimering og udvikling af vandforsyningen · Hørsholm")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Maskiningeniør til driftsoptimering", bold=True, color='1A1A1A')

    # ---------------------------------------------------------------- side 1
    m.para("Kære drifts- og udviklingsteam i Novafos,", after=60)

    m.para("**Tre ting afgør, om en optimering bliver til noget i driften.** Om den tager "
           "udgangspunkt i en **måling**, nogen stoler på. Om den, der skal leve med ændringen, var "
           "med til at finde den. Og om nogen skriver ned, hvad den gav — så den ikke skal opfindes "
           "igen om to år. Resten af dette brev er **vandforsyningen i dag og om tolv måneder**, "
           "punkt for punkt, med de tre ting som prøvesten.", after=80)

    m.para("**Energi.** I dag betales elregningen, og pumperne kører, når de skal. Om tolv måneder er "
           "energiforbruget pr. pumpet m³ kendt pr. station, og de stationer, der kører uden for "
           "deres bedste arbejdspunkt, er fundet på en **analyse** af tallene — ikke på mavefornemmelse. Jeg har kørt et "
           "PDCA-program, der gav **over 40 % lavere energiforbrug**, fordi nogen begyndte at måle "
           "det, alle troede, de vidste.", after=80)

    m.para("**Beslutningsgrundlag.** I dag ligger data i flere systemer, og rapporten bliver lavet, "
           "når nogen spørger. Om tolv måneder er der ét sted at se drift, energi og udvikling i "
           "samme billede, opdateret af dem, der ejer data — ikke af den, der har mest tid. Jeg "
           "bygger rapporter og dashboards i **Excel** og i **egne AI-værktøjer**; **PowerBI** er "
           "samme arbejdsgang i et andet værktøj, og det er den hurtigste del at sætte sig ind i.", after=80)

    m.para("**Vedligehold.** I dag sker service efter interval og erfaring. Om tolv måneder findes "
           "der **kriterier for tilstandsbaseret vedligehold** pr. anlægsklasse: hvilke målinger der "
           "afgør, om en pumpe skal åbnes, hvornår et filter er slidt, og hvad der er billigere at "
           "skifte før tid end at vente på stop. Jeg har opbygget den slags kriterier før, med "
           "intervaller og historik, der kunne forsvares over for dem, der betaler.", after=80)

    m.para("**Målinger.** I dag kvalitetssikres **tryk**- og **flow**målinger, når nogen opdager, at "
           "tallene ikke passer. Om tolv måneder er der en fast kontrol, der fanger den føler, der "
           "driver, før den bliver til et lækagetab eller en unødig **fejlretning**. På et anlæg i "
           "24/7-drift lærte jeg, at den dyreste måling er den, ingen kontrollerede.", after=80)

    m.para("**Projekter.** I dag bliver gode idéer til gode idéer. Om tolv måneder er de mindre "
           "**optimeringsprojekter** og fornyelser leveret med gevinst, dokumenteret i drift og "
           "afrapporteret som **energiforbedring** — og de større **anlægsprojekter** har fået et "
           "driftsperspektiv ind, mens de stadig var tegninger. Jeg har prøvet begge sider: som "
           "driftsansvarlig, der overtog anlæg, og som projektleder, der afleverede dem.", after=80)

    m.para("**Forankring.** I dag ender forbedringen ofte hos den, der fandt den. Om tolv måneder "
           "står den i arbejdsprocessen, i **dokumentationen** og i den ugentlige opfølgning, så den "
           "lever videre, når jeg har ferie. Det er også derfor, jeg vil sidde tæt på driften og "
           "**plan-afdelingen** — en optimering, der kun findes på et kontor, holder ikke i tre "
           "måneder.", after=80)

    m.para("**Hvad jeg har prøvet det på.** Fire år som driftsansvarlig på et forsyningsanlæg i "
           "24/7-drift: **pumper**, HVAC, højspændingstavler og **SRO**/**SCADA**, med planlagt og "
           "tilstandsbaseret vedligehold og energiledelse. 37 samtidige CAPEX-projekter i reguleret "
           "miljø med kvalificering og dokumentation, der skulle kunne stå i en revision. Og siden "
           "2023 egen virksomhed med fem elektrikere, tre lærlinge og fuldt resultatansvar — hvor "
           "jeg selv har mærket, hvad en time og en kWh koster.", after=80)

    m.para("I forsyner ni kommuner med **drikkevand**, tager jer af **spildevand** og regnvand og "
           "arbejder med **klimasikring** og **bæredygtighed** i det daglige — og I kalder jer "
           "**hverdagsmestre i at håndtere vand**. Det er et godt ord, for det, der skal forbedres i en forsyning, bliver ikke forbedret af store visioner, men af nogen, der "
           "kender hverdagen godt nok til at se, hvor den kan gøres billigere uden at blive dårligere.",
           after=80)

    m.para("**Praktisk:** bosat i Måløv, ca. 35 minutter fra Sjælsø Vandværk i Hørsholm · "
           "**kørekort B** · dansk modersmål, engelsk på professionelt niveau · 37 timers uge med "
           "mødetid fra 07.00 passer fint · **kan tiltræde 1. februar 2027**, som I planlægger, og "
           "er klar til samtale fra uge 48.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Maskiningeniørprofil med tyve års erfaring fra **tekniske anlæg** i drift: elautoriseret "
           "**maskinmester** (LV/MV/HV), el- og maskinteknisk design (EQF 6) og B.Tech i "
           "teknologiledelse. Fire år i 24/7-drift med **pumper**, **SRO**/**SCADA** og "
           "tilstandsbaseret vedligehold, **over 40 % lavere energiforbrug** gennem et PDCA-program, "
           "og 37 CAPEX-projekter med dokumentation og aflevering.", after=80)

    m.section("DRIFT OG OPTIMERING")
    for label, body in [
        ("Driftsanalyse",
         "Forbrug, driftstimer og fejlhistorik læst sammen, så forbedringen bliver fundet i tallene "
         "og ikke i en fornemmelse; **energioptimering** med dokumenteret effekt."),
        ("Tilstandsbaseret vedligehold",
         "Kriterier og intervaller pr. anlægsklasse, opbygget med historik og målinger; planlagt "
         "vedligehold, der flytter arbejde fra akut til forudsigeligt."),
        ("Målinger og fejlretning",
         "**Tryk**- og **flow**målinger kvalitetssikret mod fysisk kontrol; følere, der driver, "
         "fundet før de bliver til tab eller stop."),
    ]:
        m.bullet(label, body)

    m.section("DATA OG BESLUTNINGSGRUNDLAG")
    for label, body in [
        ("Rapporter og dashboards",
         "Datarapporter bygget i **Excel** og i **egne AI-værktøjer** til ledelse, drift og "
         "projekter; samme arbejdsgang som i **PowerBI**, uden at gøre værktøjet til et mål i sig selv."),
        ("Afrapportering",
         "**Energiforbedringer** dokumenteret før og efter, med enhed, periode og forudsætninger — "
         "så tallet kan forsvares, når nogen spørger om det igen."),
        ("Forankring",
         "Forbedringer skrevet ind i arbejdsprocesser og **dokumentation**, med en ejer og en "
         "opfølgningsdato, så de ikke forsvinder med den, der fandt dem."),
    ]:
        m.bullet(label, body)

    m.section("ANLÆG, KOORDINERING OG PROJEKTER")
    for label, body in [
        ("Anlæg og forsyning",
         "**Pumper**, rørsystemer, HVAC og højspændingstavler i 24/7-drift; **SRO**/**SCADA** som "
         "dagligt arbejdsredskab, ikke som fremmedord."),
        ("Koordinering",
         "Optimeringer drevet på tværs af drift, teknik og plan; 25 specialister koordineret på 37 "
         "projekter, 14 mand og 11 samtidige entrepriser."),
        ("Projekter",
         "Mindre **optimerings- og fornyelsesprojekter** fra idé til aflevering, og større "
         "**anlægsprojekter** med driftskrav ind tidligt i projekteringen."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Indehaver / Teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · fuldt resultatansvar · drift, service og aflevering")
    m.bullet("Forbedringer med egen økonomi",
              "Projekter og service med eget budget og egen risiko; **40 % mindre administration** og **over "
              "40 % produktivitetsløft** via egne værktøjer og faste arbejdsgange.")

    m.job("Senior Commissioning Engineer / Project Manager, elsystemer",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024",
          scope="37 samtidige CAPEX-projekter · 25 specialister · GMP/FDA/EMA")
    m.bullet("Projekter og dokumentation",
              "Projektgrundlag, milepæle og rapportering i SAP ERP; kvalificering med FAT/SAT og "
              "IQ/OQ/PQ — **nul kritiske fund** ved aflevering.")
    m.bullet("Energi og PDCA",
              "**PDCA-program** med **over 40 % lavere energiforbrug** som dokumenteret resultat, "
              "målt før og efter og fastholdt i driften.")

    m.job("Projekt- og værkstedschef", "Ventek-Air · København · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · 2–10 mio. kr. pr. sag")
    m.bullet("Ventilation under pres",
              "Leverancer med luftmængde, tryk og balance som acceptkriterier; daglig flaskehalsanalyse, når "
              "en sag gik bagud.")

    m.job("Drifts- og vedligeholdelseschef", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="Forsyningsanlæg i 24/7-drift · pumper, VVS, HVAC, højspændingstavler, SCADA")
    m.bullet("Drift, der ikke må stoppe",
              "Forebyggende og **tilstandsbaseret vedligehold** og fejlfinding døgnet rundt; indgreb planlagt "
              "i snævre vinduer med midlertidig løsning klar.")

    m.job("Elektromekanisk tekniker / produktionsleder",
          "ARJ Engineering · Teheran · dec. 2003–mar. 2010 · 12 mekanikere og teknikere")

    # ---------------------------------------------------------------- side 3
    m.page_break()
    m.section("UDDANNELSE OG AUTORISATION")
    m.edu("Elautoriseret maskinmester — dansk elautorisation LV/MV/HV",
          "Sikkerhedsstyrelsen · maj 2023")
    m.edu("B.Tech, teknologiledelse og maskinteknik (EQF 6)",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · karakter 7,6/12")
    m.edu("El- og maskinteknisk design, elektroteknik (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("Køle- og VVS-teknik (AMU) · Lean: 5S, PDCA, VSM, A3",
          "Mercantec · 2021 · STCW-sikkerhedskurser (2021–2023)")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("**Dansk:** modersmål · **Engelsk:** professionelt, skriftligt og mundtligt · "
           "**Persisk:** modersmål · **Bosat i Måløv**, ca. 35 minutter fra Hørsholm · "
           "**Kørekort B** · **Kan tiltræde 1. februar 2027** · Referencer efter aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA OVERBLIK TIL FØRSTE FORBEDRING, DER KAN MÅLES",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–4",
             "På vandværkerne med driftskollegerne: hvad der styrer, hvad der måles, og hvilke tal "
             "ingen kigger på. Energiforbrug, driftstimer og fejlhistorik samlet for de stationer, "
             "der betyder mest."),
            ("Dag 45",
             "En kort liste over de tre til fem steder, hvor der er mest at hente — med tal, årsag "
             "og hvad der skal til. Gennemgået med driften, før noget bliver besluttet."),
            ("Dag 60",
             "Første **optimeringsindsats** i gang med en ejer i driften, en måling før og en dato "
             "for, hvornår den evalueres. Udkast til kriterier for **tilstandsbaseret vedligehold** "
             "på én anlægsklasse."),
            ("Dag 90",
             "Første **energiforbedring** afrapporteret med tal og forudsætninger, kontrol af "
             "**tryk**- og **flow**målinger indført som fast rutine, og næste fornyelsesprojekt "
             "beskrevet."),
        ],
        widths=(1500, 8830))

    m.section("EN OPTIMERING, DER IKKE KAN MÅLES, BLIVER IKKE TIL NOGET")
    m.para("Før jeg ændrer noget, skal der stå et tal på bordet: forbrug pr. m³, driftstimer pr. dag, "
           "antal fejl pr. måned. Det tal er ikke bureaukrati — det er det, der gør det muligt at "
           "svare, når nogen spørger, om det virkede. Og det er det, der gør en forbedring værd at "
           "fastholde, fordi ingen kan bestride den bagefter.", after=70)

    m.section("PUMPER ER DEN STØRSTE ELREGNING PÅ ET VANDVÆRK")
    m.para("En pumpe, der kører lidt ved siden af sit bedste arbejdspunkt, mærkes ikke i hverdagen. "
           "Den mærkes på elregningen, året rundt, på alle de timer ingen kigger. Derfor er "
           "energioptimering i en forsyning først og fremmest at finde de stationer, hvor styring, "
           "tryksætning og kørselsmønster ikke passer sammen — og derefter at ændre så lidt som "
           "muligt, men det rigtige sted.", after=70)

    m.section("TRYKSÆTNING ER ET LØFTE TIL BORGEREN")
    m.para("Tryk og flow er ikke bare tekniske tal; de er det, forbrugeren mærker som vand i hanen, "
           "og det, forsyningen betaler som tab i rørene. Derfor skal en måling kvalitetssikres "
           "fysisk og ikke kun i systemet: en føler, der driver fem procent, kan se ud som en "
           "forbedring i rapporten og være et **lækagetab** i virkeligheden.", after=70)

    m.section("DATA ER KUN ET BESLUTNINGSGRUNDLAG, HVIS NOGEN EJER DEM")
    m.para("Når tusind målere sender data døgnet rundt, er problemet ikke at skaffe tal — det er at "
           "vide, hvilke tal der er rigtige, og hvem der svarer på dem. Derfor har hver rapport en "
           "ejer, hver måling en kontrol, og hver konklusion en dato, hvor den bliver prøvet af. Uden "
           "det bliver et dashboard et flot sted at have ret — og en dyr måde at opdage om tre "
           "måneder, at ingen brugte det.", after=70)

    m.section("SRO ER DET SPROG, ANLÆGGET TALER")
    m.para("Grænseværdier, sætpunkter og tendenser er den mest ærlige kilde til, hvordan et anlæg "
           "faktisk kører — og den mest oversete. Jeg læser **trends** før alarmer: en alarm "
           "fortæller, at noget allerede er sket; en tendens fortæller, at det er på vej. Den forskel "
           "er hele pointen med **tilstandsbaseret vedligehold**, og den kan ses i et hvilket som "
           "helst SRO-anlæg, hvis nogen har sat grænserne rigtigt.", after=70)

    m.section("DET SVÆRESTE ER IKKE ANALYSEN, MEN AT FÅ DRIFTEN MED")
    m.para("En optimering holder kun, hvis den, der har hænderne i anlægget, synes den er rimelig. "
           "Derfor tager jeg analysen med ud på vandværket, før den bliver en beslutning, og lytter "
           "til det, driften ved, som ingen rapport kan vise. Det er også der, man hører, hvilken "
           "forbedring der bliver gennemført, og hvilken der bliver modarbejdet i det stille.",
           after=0)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "DET ROLLEN KRÆVER — DET HAR JEG LØST",
        ["Krav i opslaget", "Bevis"],
        [
            ("Analysere driften og identificere muligheder for drifts- og energioptimering",
             "Forbrug, driftstimer og fejlhistorik læst sammen i 24/7-drift; PDCA-program med "
             "**over 40 % lavere energiforbrug** som dokumenteret resultat."),
            ("Bidrage til datarapporter og beslutningsgrundlag i PowerBI",
             "Rapporter og dashboards bygget i **Excel** og egne **AI-værktøjer** til ledelse og "
             "drift; **PowerBI** er samme arbejdsgang i et andet værktøj, og det er den hurtigste "
             "del at sætte sig ind i."),
            ("Koordinere og følge op på optimeringsindsatser med driften og plan-afdelingen",
             "Optimeringer drevet på tværs af drift, teknik og **plan-afdeling** — 25 specialister og "
             "11 samtidige entrepriser koordineret med faste opfølgningspunkter."),
            ("Sikre dokumentation og forankring af forbedringer, herunder afrapportering af energiforbedringer",
             "**Energiforbedringer** afrapporteret før/efter med enhed, periode og forudsætninger; "
             "forbedringer skrevet ind i arbejdsprocesser med ejer og dato."),
            ("Udvikle planer og kriterier for tilstandsbaseret vedligehold",
             "**Tilstandsbaseret vedligehold** opbygget med kriterier og intervaller pr. "
             "anlægsklasse, historik og målinger som grundlag."),
            ("Kvalitetssikre tryk- og flowmålinger samt sikre rettidige fejlretninger",
             "**Tryk**- og **flow**målinger kontrolleret mod fysisk tilstand i drift; fejl rettet, "
             "før de blev til stop eller tab, med LOTO og sikker procedure."),
            ("Drive mindre optimerings- og fornyelsesprojekter",
             "Små projekter leveret med gevinst i egen virksomhed siden 2023: **40 % mindre "
             "administration** og **over 40 % produktivitetsløft**, målt før og efter."),
            ("Bidrage til større anlægs- og udviklingsprojekter på tværs af organisationen",
             "37 CAPEX-projekter med projektgrundlag, økonomi og aflevering; driftskrav ført ind i "
             "projekteringen, mens anlægget stadig var på tegning."),
            ("Uddannet maskiningeniør eller tilsvarende teknisk uddannelse",
             "Elautoriseret **maskinmester** (LV/MV/HV), el- og maskinteknisk design (EQF 6) og "
             "B.Tech i teknologiledelse — den maskintekniske linje i dansk praksis."),
            ("Erfaring med procesanlæg, forsyning eller tekniske projekter — eller nyuddannet med lyst til at omsætte analyser til forbedringer",
             "Fire år i **forsyningsdrift** på et anlæg i 24/7-drift, og tyve år med tekniske anlæg "
             "og projekter i regulerede miljøer."),
            ("Stærke analytiske kompetencer og kan se sammenhænge i komplekse problemstillinger",
             "Sammenhænge fundet på tværs af systemer: forbrug mod driftstimer mod fejlhistorik — og "
             "beslutninger taget på det, tallene viste, ikke på det, alle troede."),
            ("God til at formidle tekniske budskaber mundtligt og skriftligt",
             "Analyser formidlet til driftsfolk, ledelse og leverandører i samme sprog; "
             "projektdokumentation ført på både dansk og engelsk."),
            ("Trives med dokumentation, afrapportering og opfølgning",
             "Dokumentation er en del af arbejdet, ikke en eftertanke: kvalificering, KS, "
             "afrapportering og opfølgning til dato i 37 projekter."),
            ("Kan planlægge og koordinere opgaver på tværs af fagområder",
             "Opgaver planlagt på tværs af el, VVS, ventilation, drift og eksterne leverandører — "
             "14 mand og 11 entrepriser samtidigt."),
            ("Arbejder struktureret og følger opgaverne helt til dørs",
             "Faste arbejdsgange, tjeklister og opfølgning til sagen er lukket; **40 % mindre "
             "administration** er resultatet af struktur, ikke af mindre arbejde."),
            ("Motiveres af forbedringer, der kan mærkes i den daglige drift",
             "Forbedringer valgt, hvor de kan mærkes af dem, der arbejder i anlægget: kortere "
             "fejlfinding, færre akutte indgreb, lavere forbrug."),
            ("Holdspiller, der skaber gode relationer og samarbejder med drift, specialister og projektledere",
             "**Holdspiller** i praksis: analysen taget med ud på anlægget, før den blev en "
             "beslutning, og driften lyttet til om det, ingen rapport viser."),
            ("Fordel: kendskab til tekniske anlæg, forsyningsområdet eller SRO-systemer",
             "**SRO**/**SCADA** som dagligt redskab i 24/7-drift, og fire år i **forsyningsområdet** "
             "med pumper, rørsystemer og rensning."),
        ],
        widths=(3600, 6746))

    m.section("HVOR JEG VILLE STARTE")
    m.para("Med elregningen og fejlhistorikken for de ti stationer, der betyder mest — og en tur ud på "
           "to af dem med dem, der kører dem. Tallene viser, hvor der er noget at hente; turen viser, "
           "hvorfor det ikke er hentet endnu. Forskellen mellem de to ting er som regel det arbejde, "
           "der skal gøres.", after=0)

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_Novafos_Maskiningenioer.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_Novafos_Maskiningenioer.docx'))
