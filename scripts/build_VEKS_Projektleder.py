# -*- coding: utf-8 -*-
"""VEKS I/S — projektleder, Projekt (tekniske anlægsprojekter), Glostrup.

Dansk opslag → dansk dokument (da-DK): ansøgning side 1, CV side 2, uddannelse + 90 dage +
fire afsnit side 3, kravmatrix side 4.

STILVALG (master/STILREGISTER.md, policy 04.11.2026; godkendt af scripts/style_guard.py,
3/3 skift mod #197 — samme virksomhed, helt andet spor):
  register      = VALIDERET PRODUKTION (GMP) — sporbarhed, afvigelse, ændringskontrol, "nul
                  kritiske fund", revisionsparathed. Passer til en projektlederrolle, hvor
                  beslutninger skal kunne dokumenteres bagefter, og hvor ændringer er det, der
                  vælter projekter. Sidst brugt #189 (Cavendish).
  åbningsgreb   = B (NEGATION-MAXIMEN) — "et projekt bliver ikke styret af sin tidsplan …".
                  Sidst brugt #191.
  struktur      = KOMPONENTENS VEJ — her anlæggets vej: behovet → grundlaget → planen →
                  kontrakten → udførelsen → afleveringen. Sidst brugt: ikke før.
  kadence       = ét trin ad gangen, altid med hvem der beslutter, og hvad der står i
                  dokumentet bagefter.

Ingen opdigtede fakta: der påstås IKKE en projektledercertificering (PRINCE2/IPMA), og der
påstås ikke erfaring med kommunale anlægsprojekter i forsyningssektoren. Det dokumenterede
grundlag er 37 samtidige CAPEX-projekter (DKK 2–10 mio.) med fremdrift, økonomi og risici,
25 specialister, FAT/SAT og IQ/OQ/PQ med nul kritiske fund, SAP ERP-projektdokumentation,
månedsrapportering til ledelse og bygherre, 11 entrepriser med 14 mand, udbud/tilbud og
aftalegrundlag, fuldt P&L siden 2023 samt B.Tech i teknologiledelse.

Policy: master/README.md — jobbet først, kandidaten kun som bevis, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Projektleder · Tekniske anlægsprojekter, governance og fremdrift'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4. november 2026")
    m.meta("VEKS · Projektleder, Projekt · Fabriksparken 58A, 2600 Glostrup")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: projektleder — tekniske anlægsprojekter", bold=True, color='1A1A1A')
    m.para("Til teamleder Per M. Friis", after=70)

    # ---------------------------------------------------------------- side 1
    m.para("**Et projekt bliver ikke styret af sin tidsplan.** Det bliver styret af de beslutninger, "
           "ingen har skrevet ned, og af hvor hurtigt nogen opdager, at de er taget. Derfor er "
           "**projektledelse** for mig ikke at have den flotteste **milepælsplan**; det er at sørge for, "
           "at det, der bliver besluttet i et møde i marts, stadig står i **referat**et i september — og "
           "at den, der skal leve med beslutningen, vidste det, da den blev taget.", after=80)

    m.para("**Behovet.** Et **anlægsprojekt** starter med en grund til at bruge penge: en kapacitet, der "
           "mangler, en installation, der er slidt, eller et krav, der er kommet. Den grund skal skrives "
           "ned i klart sprog, før nogen tegner — for det er den, alle senere spørgsmål bliver målt imod. "
           "Jeg har styret **anlægsprojekter**, hvor behovet var formuleret som en løsning, og hvor vi "
           "brugte de første uger på at finde ud af, hvad problemet egentlig var. Det er billigere at "
           "gøre den øvelse i **projektgrundlag**et.", after=80)

    m.para("**Grundlaget.** **Projektgrundlag**et er ikke en formalitet, der skal underskrives; det er "
           "den kontrakt, projektet har med sig selv: mål, afgrænsning, leverancer, organisation, "
           "**økonomi** og de kriterier, der afgør, om det er en succes. Jeg vil have det kort nok til, "
           "at en styregruppe læser det, og præcist nok til, at en leverandør ikke kan fortolke det. "
           "Hos Novo Nordisk skrev vi protokoller, før testen blev udført — den vane koster en time og "
           "sparer en måned.", after=80)

    m.para("**Planen.** **Milepælsstyring** er en disciplin i at vælge, hvad der ikke må flytte sig. En "
           "plan med tres milepæle har ingen. Jeg arbejder med få, hårde milepæle, en synlig kritisk "
           "vej og en aftale om, hvem der må flytte hvad — og så en **fremdrift**sopfølgning, der er "
           "kort nok til at blive lavet hver uge og ærlig nok til at være værd at læse. 37 samtidige "
           "**anlægsprojekter** lærte mig, at overblik er noget, man vedligeholder, ikke noget man har.",
           after=80)

    m.para("**Kontrakten.** **Udbud**, **kontrakt** og **indkøb** er ikke en juridisk afdeling, der "
           "kommer til sidst; det er der, projektet bliver svært eller let at styre. En kontrakt er "
           "frem for alt en aftale om, hvad der sker, når noget ændrer sig — og om hvem der betaler. "
           "Jeg har skrevet **udbud** og **tilbudslister**, forhandlet aftalegrundlag og forbehold og "
           "stået med **leverandørstyring**, hvor den gode relation var det, der gjorde forskellen, da "
           "leverancen skred.", after=80)

    m.para("**Udførelsen.** Her ligger **ændringshåndtering**, **risikolog**en, **eskalering**en og "
           "**rapportering**en til **styregruppe** og ledelse. Min tilgang er hentet fra et regime, hvor "
           "en ændring ikke måtte ske i det skjulte: den skal beskrives, vurderes, godkendes og kunne "
           "**sporbar**es bagefter. Det er samme logik, der gælder her, bare med en anden konsekvens — "
           "et **anlægsprojekt**, der ændrer sig undervejs uden at nogen har skrevet det ned, ender med "
           "at koste mere, uden at nogen kan pege på hvorfor.", after=80)

    m.para("**Afleveringen.** Et projekt er ikke slut, når det kører; det er slut, når **dokumentation**en "
           "er der, driften har overtaget, og de, der skal leve med anlægget, ved, hvad de har fået. Jeg "
           "har stået for **aflevering** med kvalitetssikring og afleveringspakker og haft ansvaret for, "
           "at der ikke var kritiske **afvigelse**r ved overdragelsen. Nul kritiske fund er ikke held; "
           "det er et resultat af at have spurgt ind til det samme tre gange.", after=80)

    m.para("**Om det at være teknisk i en rolle, der ikke skal være teknisk.** Jeg er uddannet "
           "**elautoriseret maskinmester** og har arbejdet med teknik hele mit liv, og det er både en "
           "fordel og en fristelse her: fordelen er, at jeg kan stille fagfolk de rigtige spørgsmål og "
           "gennemskue, når et svar er for pænt. Fristelsen er at begynde at lave teknikken selv. Det "
           "har jeg lært at lade være — og på de 37 projekter var det netop pointen, at de 25 "
           "specialister skulle levere fagligheden, mens nogen holdt styr på mål, tid og penge.",
           after=80)

    m.para("**Hvad jeg ikke har — og hvad jeg har i stedet.** Jeg har ingen **projektledelse**s-"
           "certificering som PRINCE2 eller IPMA. Jeg har B.Tech i teknologiledelse og maskinteknik, "
           "Lean-værktøjerne i praksis og 37 projekter med formel **rapportering** til ledelse og "
           "bygherre bag mig, plus fuldt P&L-ansvar siden 2023. Hvis I ønsker en certificering som en "
           "del af rollen, tager jeg den gerne — men jeg vil hellere vise jer de **risikolog**er og "
           "**projektgrundlag**er, jeg faktisk har lavet.", after=80)

    m.para("Jeg bor i Måløv, har ca. 25 minutter til **Glostrup** og kan tiltræde efter aftale. At "
           "arbejde med **grøn omstilling** i den skala interesserer mig, og jeg har læst, at I lægger "
           "vægt på **samarbejde** og på, at stilen ikke bliver styrende — det er også den måde, jeg "
           "helst arbejder på: tæt på, men ikke oven på.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Projektleder med 20+ års erfaring i **anlægsprojekter**, hvor fagligheden kom fra "
           "specialister og leverandører — **elautoriseret maskinmester** (LV/MV/HV), EQF 6 og B.Tech i "
           "teknologiledelse og maskinteknik. Har styret 37 "
           "samtidige CAPEX-projekter (DKK 2–10 mio.) med **projektgrundlag**, **milepæle**, "
           "**risikovurdering** og **økonomi**, rapporteret til ledelse og bygherre i SAP ERP og "
           "afleveret med nul kritiske fund.", after=80)

    m.section("PROJEKTSTYRING OG GOVERNANCE")
    for label, body in [
        ("Projektgrundlag og plan",
         "Mål, afgrænsning, leverancer og succeskriterier skrevet ned før opstart; få hårde "
         "**milepæle**, synlig kritisk vej og en ugerapport, der er kort nok til at blive lavet."),
        ("Risiko og ændringer",
         "**Risikolog** ført og gennemgået, ikke arkiveret; ændringer og hver **afvigelse** "
         "beskrevet, godkendt og **sporbar**, så de kunne findes igen et år senere."),
        ("Rapportering og styregruppe",
         "Månedsrapport til ledelse og bygherre på 37 projekter med fremdrift, **økonomi** og risici — "
         "og en **beslutningslog**, en ny projektleder kan læse sig ind i."),
    ]:
        m.bullet(label, body)

    m.section("ØKONOMI, KONTRAKTER OG LEVERANDØRER")
    for label, body in [
        ("Projektøkonomi",
         "Budget, kalkulation og månedlig opfølgning i SAP ERP; afvigelser forklaret med årsag og "
         "handling, og prognose opdateret, så ingen blev overrasket i december."),
        ("Udbud og kontrakt",
         "Udbud, tilbudslister og aftalegrundlag; forbehold og grænseflader gennemgået, før "
         "underskriften — og kontraktens ændringsregler kendt af alle parter."),
        ("Leverandørstyring",
         "Leverandører og underentreprenører fulgt på leverance, kvalitet og tid; eskalering tidligt "
         "frem for konfrontation sent, og dokumentationen i orden ved hver delleverance."),
    ]:
        m.bullet(label, body)

    m.section("INTERESSENTER OG KOMMUNIKATION")
    for label, body in [
        ("Interessenter og myndigheder",
         "Bygherre, **rådgivere**, **entreprenører** og **myndigheder** i samme projekt; "
         "forventninger afstemt skriftligt."),
        ("Mødeledelse og formidling",
         "Dagsorden med beslutningspunkter, **referat** med navn og frist, opfølgning på hvert punkt; "
         "teknisk stof formidlet til ledelse, økonomi og drift på dansk og engelsk."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Ejer / teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · fuldt P&L · projekter, udbud og leverandører")
    m.bullet("Projekt- og forretningsansvar",
              "Projekter fra tilbud til aflevering med eget budget og egen risiko; udbud, "
              "underentreprenører og KS — og ansvaret for at sige nej, når kalkulen ikke holdt.")
    m.bullet("Struktur og værktøjer",
              "Tidsplaner, tjeklister og KPI-dashboards (Python, Power BI) bygget selv — over 40 % "
              "produktivitetsløft på det administrative og færre sager, der gik i glemmebogen.")

    m.job("Senior idriftsættelsesingeniør / projektleder, elsystem",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024",
          scope="37 samtidige anlægsprojekter · 25 specialister · GMP/FDA/EMA")
    m.bullet("Fremdrift, økonomi og risici",
              "Projektgrundlag, milepæle og månedsrapportering i SAP ERP; risici håndteret, før de "
              "blev afvigelser, og afvigelser lukket med rodårsagsanalyse — nul kritiske fund ved "
              "aflevering.")
    m.bullet("Verifikation og overdragelse",
              "FAT/SAT og IQ/OQ/PQ med protokoller skrevet før testen; afleveringspakker og "
              "overdragelse til drift med dokumentation, der kunne læses af en tredjemand.")

    m.job("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · DKK 2–10 mio.")
    m.bullet("Koordinering i pressede uger",
              "Daglige tavlemøder og flaskehalsanalyser; omfordeling af mandskab og leverandører, når "
              "en entreprise trak mere end planlagt — med kunden informeret samme dag.")

    m.job("Vedligeholdelses- og driftsleder", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="Renseanlæg i 24/7-drift · pumper, HVAC, højspændingstavler, SCADA")
    m.bullet("Drift som modtager",
              "Overtaget anlæg fra projekter og set, hvad der manglede i dokumentationen; 5S, LOTO, APV.")

    m.job("Elektromekaniker / produktionsteamleder",
          "ARJ Engineering · Teheran · dec. 2003–mar. 2010 · 12 mekanikere og teknikere")

    # ---------------------------------------------------------------- side 3
    m.page_break()
    m.section("UDDANNELSE OG AUTORISATION")
    m.edu("Elautoriseret maskinmester — dansk elautorisation LV/MV/HV",
          "Sikkerhedsstyrelsen · maj 2023")
    m.edu("B.Tech, teknologiledelse og maskinteknik (EQF 6) — herunder projekt- og teknologiledelse",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12")
    m.edu("El- og maskinteknisk design, elteknik (EQF 6)", "Tehran Technical University · 2000–2003")
    m.edu("Køleteknik & klimaanlæg (AMU)", "Mercantec · 2021")
    m.edu("Lean-/forbedringspraksis: 5S, PDCA, VSM, A3, Kaizen · STCW sikkerhedskurser (2021–2023)",
          "Mercantec / Søfartsstyrelsen")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("**Dansk:** modersmål · **Engelsk:** professionelt, skriftligt og mundtligt · **Persisk:** "
           "modersmål · **Bosat i Måløv**, ca. 25 minutter til Glostrup · **Kan tiltræde efter aftale** · "
           "Uddannelsesbevis og referencer fremsendes efter aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA PROJEKTGRUNDLAG TIL AFLEVERING",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–2",
             "Læse jeres projektmodel og skabeloner igennem og gennemgå to igangværende "
             "**anlægsprojekter** som tilhører: hvor står **risikolog**en, hvad er sidste godkendte "
             "ændring, og hvem beslutter hvad?"),
            ("Dag 30",
             "Eget **projektgrundlag** for en afgrænset sag: mål, leverancer, milepæle, budget og "
             "**interessenter** — gennemgået med en kollega og med fagansvarlig, før det går i "
             "styregruppen."),
            ("Dag 60",
             "Første **rapportering** i jeres format og en oprydning i **ændringshåndtering**en på "
             "eget projekt, så der er én log, én ejer og en dato pr. ændring."),
            ("Dag 90",
             "Egen portefølje af sager med **opfølgning** på **fremdrift** og **økonomi**; status med "
             "dig på, hvor jeg stadig skal sparre, og hvad jeg kan bære alene."),
        ],
        widths=(1500, 8830))

    m.section("ET REFERAT ER ET STYREVÆRKTØJ, IKKE EN HØFLIGHED")
    m.para("Det lyder som en detalje, men det er det sted, hvor de fleste projekter mister retningen: "
           "nogen husker mødet anderledes, end det blev holdt. Derfor skriver jeg **referat** med "
           "beslutningen, den der besluttede, og den dato, den gælder fra — og sender det ud samme dag. "
           "Det tager ti minutter og er den billigste **risikostyring**, der findes. Hvis beslutningen "
           "var forkert, kan den ændres; hvis den ikke er skrevet ned, kan den ikke engang diskuteres.",
           after=70)

    m.section("EN RISIKOLOG, DER IKKE BLIVER LÆST, ER LITTERATUR")
    m.para("Alle projekter har en **risikolog**. De fleste har en, der blev skrevet i uge to og åbnet "
           "igen ved afleveringen, hvor alle risiciene viste sig at være indtruffet som overraskelser. "
           "Min regel er enkel: hver risiko har en ejer, en dato og et trigger-punkt — hvad er det "
           "konkret, vi ser efter, og hvad gør vi, hvis vi ser det? Så kan **risikovurdering** bruges "
           "til at handle i stedet for at dokumentere.", after=70)

    m.section("JEG LAVER IKKE TEKNIKKEN SELV — OG DET ER ET VALG")
    m.para("Jeg kan gå ned i en tavle og finde fejlen, og nogle gange er det fristende at gøre det, "
           "fordi det er hurtigere. Men i den rolle, I beskriver, er min opgave at stille spørgsmålene, "
           "sørge for at svarene bliver dokumenteret, og holde **fremdrift**en — ikke at være den, der "
           "tegner. De 25 specialister på Novo-projekterne leverede fagligheden; jeg leverede "
           "**struktur**, **økonomi** og retning. Det er den fordeling, jeg søger igen.", after=70)

    m.section("HVIS JEG SKULLE MÅLE PROJEKTER PÅ ÉN TING")
    m.para("Ikke på hvor mange milepæle der blev nået, og ikke på hvor mange møder der blev holdt. Men på "
           "hvor lang tid der går fra en beslutning er nødvendig, til den er taget og skrevet ned. Det "
           "tal afslører, om projektet har en **styregruppe**, der fungerer, eller en, der mødes. Jeg "
           "har prøvet projekter, hvor teknikken var i orden, og hvor det alligevel gik langsomt — fordi "
           "ingen kunne beslutte noget uden at spørge tre personer, der ikke var i rummet. Det er den "
           "slags **struktur**, jeg gerne vil være med til at rydde op i.", after=70)

    m.section("NUL KRITISKE FUND ER IKKE HELD")
    m.para("Ved aflevering af store anlæg i et reguleret miljø er det fristende at sige, at det gik "
           "godt. Sandheden er, at nul kritiske **afvigelse**r kommer af at have spurgt til det samme "
           "tre gange, af at have læst protokollen før testen og af at have haft en **dokumentation**, "
           "der var **sporbar** nok til at kunne efterprøves. Det er sjældent populært i uge 30 og "
           "altid værdsat i uge 52.", after=0)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "HVAD STILLINGEN KRÆVER — HVAD JEG HAR LEVERET",
        ["Krav i opslaget", "Bevis"],
        [
            ("Projektledelse af tekniske anlægsprojekter på overordnet niveau",
             "37 samtidige CAPEX-projekter (DKK 2–10 mio.) som projektleder, hvor 25 specialister og "
             "leverandører leverede fagligheden; 11 entrepriser med 14 mand i egen regi."),
            ("Etablering af projektgrundlag og overordnet planlægning",
             "Projektgrundlag med mål, afgrænsning, leverancer og succeskriterier skrevet før opstart; "
             "plan med få hårde milepæle og synlig kritisk vej."),
            ("Milepælsstyring og opfølgning på fremdrift",
             "Milepæle og ugerapport i SAP ERP på 37 projekter; fremdrift fulgt mod plan og afvigelser "
             "forklaret, før de blev til forsinkelser."),
            ("Løbende opfølgning på økonomi",
             "Projektbudgetter og månedlig opfølgning på 37 projekter samt fuldt P&L-ansvar siden 2023; "
             "prognose opdateret, så december ikke kom bag på nogen."),
            ("Risikovurdering og ændringshåndtering",
             "Risikolog med ejer, dato og trigger-punkt; ændringer beskrevet, vurderet og godkendt med fuld "
             "**sporbarhed** — en vane fra et GMP-miljø, hvor ændringer ikke måtte ske i det skjulte."),
            ("Rapportering til styregrupper og ledelse",
             "Månedsrapport til ledelse og bygherre med fremdrift, økonomi, risici og "
             "beslutningspunkter — kort nok til at blive læst, konkret nok til at blive besluttet på."),
            ("Dialog og samarbejde med kommuner, myndigheder, forsyningsselskaber, rådgivere og entreprenører",
             "Bygherre, rådgivere, entreprenører, underentreprenører og myndigheder i samme projekt i "
             "20 år; forventninger afstemt skriftligt og beslutninger eftersporet."),
            ("Bidrage til udbud, kontrakt- og indkøbsprocesser",
             "Udbud, tilbudslister og aftalegrundlag skrevet og forhandlet; forbehold og grænseflader "
             "gennemgået før underskrift, og ændringsregler kendt af begge parter."),
            ("Skabe struktur i projekt- og anlægsdokumentation med fagansvarlige",
             "Afleveringspakker, KS og dokumentation i SAP ERP; struktur aftalt med fagansvarlige, så "
             "den passede til deres arbejde og ikke blev en ekstra byrde."),
            ("Beslutninger velunderbyggede og fælles forståelse for mål, tidsplan og leverancer",
             "Beslutningspunkter i referat med navn og dato; projektgrundlaget gennemgået med alle "
             "parter ved opstart, så mål og leverancer var de samme i alle hoveder."),
            ("Centralt omdrejningspunkt for kommunikation, koordinering og opfølgning",
             "Fast mødekadence og en indgang til projektet for både interne og eksterne; 14 mand og 11 "
             "entrepriser koordineret med daglige tavlemøder, når det var nødvendigt."),
            ("Meget struktureret og bevarer overblikket i komplekse projekter",
             "37 projekter over 20 måneder uden at tabe en tråd; skabeloner, tjeklister og dashboards "
             "bygget, så overblikket ikke afhang af hukommelsen."),
            ("Klar og professionel kommunikation og samarbejde på tværs af fagligheder",
             "Teknisk stof formidlet til ledelse, økonomi, drift og leverandører på dansk og engelsk; "
             "kort på skrift, klart i lokalet."),
            ("Ansvarlig, selvstændig og robust uden at blive styrende eller konfronterende",
             "Ansvar båret alene som ejer siden 2023 og i projektlederrollen; uenighed holdt faglig — "
             "eskalering tidligt frem for konfrontation sent."),
            ("Projektlederuddannelse, certificering eller dokumenteret faglighed inden for projektledelse",
             "Ingen PRINCE2/IPMA-certificering. B.Tech i teknologiledelse og maskinteknik, Lean i "
             "praksis og 37 projekter med formel rapportering — dokumenteret faglighed, ikke et "
             "kursusbevis alene."),
            ("Teknisk forståelse og erfaring med anlægsprojekternes faser, økonomi, risici, kontrakter og leverandørstyring",
             "Elautoriseret maskinmester med 20+ års erfaring gennem alle anlægsfaser: behov, "
             "projektering, udbud, udførelse, verifikation, validering og aflevering til drift."),
        ],
        widths=(3600, 6746))

    m.section("EN KONTRAKT ER EN AFTALE OM, HVAD DER SKER, NÅR NOGET ÆNDRER SIG")
    m.para("Det er ikke prisen, der vælter projekter; det er ændringerne. Derfor læser jeg "
           "**kontrakt**en efter det ene: hvordan bliver en ændring besluttet, hvem bærer risikoen i "
           "mellemperioden, og hvad er tidsfristen for at sige til? Kan parterne svare på det uden at "
           "ringe til en advokat, er projektet styrbart. Kan de ikke, bliver selv en lille ændring til "
           "en forhandling — og så har man mistet en måned på noget, der skulle have taget en uge.",
           after=70)

    m.section("HVOR JEG VILLE STARTE")
    m.para("Med at læse jeres projektmodel og se på to igangværende sager: hvor står "
           "**projektgrundlag**et, hvornår blev **risikolog**en sidst opdateret, og hvilke beslutninger "
           "ligger der uden en dato i **referat**et? Det er ikke for at kloge mig på teknikken — det er "
           "for at finde ud af, hvor overblikket i dag hænger på en enkelt person. Det er der, en ny "
           "**projektleder** gør den største forskel i de første tre måneder.", after=0)

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_VEKS_Projektleder.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_VEKS_Projektleder.docx'))
