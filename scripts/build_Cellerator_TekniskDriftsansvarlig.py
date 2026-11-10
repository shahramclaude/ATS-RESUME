# -*- coding: utf-8 -*-
"""Cellerator (Novo Nordisk Fonden) — Teknisk driftsansvarlig, Facility, Lyngby.

Dansk opslag -> dansk dokument, 4 sider: brev s.1, CV s.2, uddannelse + 90-dages-tabel +
metodeafsnit s.3, 18-rækkers kravmatrix s.4.

STILVALG (master/STILREGISTER.md; godkendt af scripts/style_guard.py, 3/3 skift mod #204):
  register      = VALIDERET PRODUKTION (GMP) — dokumentation, sporbarhed, kvalificering,
                  nul kritiske fund. Sidst #189, #198. Her er det ikke pynt: Cellerator bygger
                  GMP-fremstilling af celle- og genterapier fra bunden.
  åbningsgreb   = D (TALLET) — "Syv dage." Vagttelefonen har man en uge ad gangen, og det tal
                  åbner dokumentet, fordi det er deres eget krav. Sidst #197.
  struktur      = BESLUTNINGSKÆDEN — én hændelse fra alarm kl. 02.40 til strategi ugen efter:
                  alarm -> eftersyn -> service -> dokumentation -> forebyggelse. Sidst #197.
  kadence       = korte konstaterende sætninger, klokkeslæt og tidsfrister, intet tillægsord om
                  personen; hvert trin slutter i et bevis.

KULTURSYNKRONISERING (policy 04.11.2026): Cellerators egne ord bærer teksten — *sikker drift*,
*uplanlagt nedetid*, *forebyggende vedligeholdelse*, *black utilities*, *kvalificering*,
*"en kvalitetskultur begynder med veldefinerede systemer"*, *"pragmatiske løsninger frem for
perfekt teori"*, *flad organisation*, *partnerskab frem for hierarki*, *bygget sammen med dig*,
*Novo Nordisk Fonden*, *celle- og genterapier*.

Brugerens oplysninger (04.11.2026): DALUX-FM er prøvet; tilkaldevagt/tilkald er prøvet.
Ingen opdigtede systemer eller fakta.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Teknisk driftsansvarlig · drift, vedligehold og vagtordning'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Storkøbenhavn'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4. november 2026")
    m.meta("Cellerator · Teknisk driftsansvarlig · Facility · Lyngby")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Teknisk driftsansvarlig", bold=True, color='1A1A1A')

    # ---------------------------------------------------------------- side 1
    m.para("Kære leder af Facility,", after=60)

    m.para("**Syv dage.** Så længe har man **vagttelefonen**, når man har vagten — og i de syv dage "
           "er det telefonen, der afgør, om et **anlæg** står stille om morgenen, eller om nogen har "
           "været der klokken 03. En ny facilitet bliver ikke sikret af en plan alene. Den bliver "
           "sikret af den kæde, der starter med en **alarm** og slutter med en dokumenteret handling, "
           "der gør den samme alarm mindre sandsynlig næste gang. Denne ansøgning følger den kæde, "
           "trin for trin.", after=80)

    m.para("**1 · Alarmen, 02.40.** **BMS** og **FMS** melder, at noget er uden for interval. Det "
           "første arbejde er ikke at køre derud, men at afgøre hvad alarmen er: en enkelt føler, der "
           "har flyttet sig, eller et **anlæg**, der er ved at gå ned. Jeg læser historikken, "
           "sammenligner med de foregående døgn og vurderer, om der skal handling nu, eller om der "
           "kan ventes til 07.00 med en plan. På et renseanlæg i 24/7-drift og i min egen virksomhed "
           "har jeg haft den telefon — også de nætter, hvor svaret var \"kør derud\".", after=80)

    m.para("**2 · Eftersynet, inden for den aftalte tid.** På stedet er rækkefølgen fast: **pumper** "
           "og **rørsystemer** først, så **tryk** og temperatur, så **luftmængde** og "
           "**luftfugtighed** i de rum, hvor det betyder noget for processen. Fejlen findes ofte et "
           "andet sted, end alarmen kommer fra — en ventil, der står halvt åben, koster mere "
           "køretid end den føler, der meldte det.", after=80)

    m.para("**3 · Servicen, samme dag.** En **serviceleverandør**, der får beskeden \"kom og kig\", "
           "koster tre dage. Jeg giver den præcise opgave, den aftalte adgang, sikkerhedsforholdene "
           "og et tidsstempel — og jeg ved, hvad **serviceaftalen** dækker, før jeg ringer, så "
           "regningen ikke bliver en overraskelse for nogen. Akut og planlagt er to forskellige "
           "processer, og de skal ikke blandes sammen klokken tre om natten.", after=80)

    m.para("**4 · Dokumentationen, i SAP og DALUX-FM.** Samme dag: hvad der blev målt, hvad der blev "
           "skiftet, og hvad der stadig mangler. Det er ikke bureaukrati — i et **reguleret miljø** "
           "er det den dokumentation, der gør, at QA kan svare for anlægget, når nogen spørger, og "
           "at den næste tekniker ikke starter forfra. **SAP** og **DALUX-FM** er de to steder, hvor "
           "den historik skal stå, og den skal stå rigtigt første gang.", after=80)

    m.para("**5 · Strategien, ugen efter.** Hændelsen bliver input til den **forebyggende "
           "vedligeholdelse**: hvilket anlæg der skal have ekstra fokus, hvilken **serviceaftale** "
           "der mangler, hvilke reservedele der skal ligge på hylden, og hvordan anlægget kommer til "
           "at køre uden løbende indgriben. Det er her, en **uplanlagt nedetid** bliver til en "
           "planlagt en af slagsen.", after=80)

    m.para("I skriver, at en **kvalitetskultur** begynder med veldefinerede systemer. Enig — og det "
           "system, der betyder mest i en drift, er det, der gør en hændelse til en læring i stedet "
           "for en gentagelse. Det er også derfor, jeg vælger **pragmatiske løsninger frem for teori, "
           "der ikke holder i drift**: en procedure, der bliver brugt klokken 03, er bedre end en, "
           "der er pænere på papiret.", after=80)

    m.para("**Hvad jeg har prøvet det på.** Fire år som driftsansvarlig på et anlæg i 24/7-drift med "
           "pumper, VVS, HVAC og højspændingstavler; 37 samtidige CAPEX-projekter i **GMP** med "
           "kvalificering, FAT/SAT og IQ/OQ/PQ og **nul kritiske fund**; **SAP** i daglig brug til "
           "budget, prognose og projektdokumentation, og **DALUX-FM** i driften. Siden 2023 har jeg "
           "desuden drevet egen virksomhed med fem elektrikere og tre lærlinge og fuldt "
           "resultatansvar — det er der, man lærer, hvad en time og en reservedel koster.", after=80)

    m.para("**At bygge fra bunden betyder, at strategien kan skrives rigtigt første gang.** Cellerator "
           "rejser en facilitet til **celle- og genterapier** med **Novo Nordisk Fonden** i ryggen, "
           "og det er netop den situation, hvor et **anlæg** ikke skal arve en gammel plan. "
           "Forsyningerne kommer samtidig nedefra: DTU's underjordiske forsyningsbygning leverer el, "
           "vand, køling, varme og fiber ind i campus' tunnelnet — **black utilities**, som nogen skal "
           "have ansvaret for, når de møder en GMP-facilitet med renrum. "
           "Anlægsliste med kritiske komponenter, vedligeholdelsesintervaller pr. forsyning, "
           "reservedelslager og serviceaftaler, der matcher det, I faktisk har — ikke det, en "
           "leverandør plejer at sælge. Jeg har prøvet begge sider: som tekniker, der bliver kaldt "
           "ud, og som den, der sender regningen.", after=80)

    m.para("**Praktisk:** bosat i Måløv, tyve minutter fra Lyngby · kørekort B · **engelsk** på "
           "professionelt niveau i skrift og tale · dansk modersmål · **tilkaldevagt** og nattevagt "
           "er noget, jeg har stået i før, og jeg tager vagttelefonen en uge ad gangen · kan "
           "tiltræde snarest.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Teknisk driftsansvarlig med tyve års erfaring fra **tekniske installationer** i "
           "regulerede miljøer: elautoriseret **maskinmester** (LV/MV/HV), el- og maskinteknisk "
           "design (EQF 6) og B.Tech i teknologiledelse. Fire år med 24/7-drift, 37 "
           "CAPEX-projekter i **GMP** med **kvalificering** og **nul kritiske fund**, og **SAP** og "
           "**DALUX-FM** i daglig brug.", after=80)

    m.section("DRIFT OG VEDLIGEHOLDELSE")
    for label, body in [
        ("Alarmer og overvågning",
         "**BMS**/**SCADA** læst og vurderet i drift: hvad der kræver handling nu, og hvad der kan "
         "vente til 07.00 med en plan. Nattevagt og **tilkaldevagt** på anlæg, der ikke må stoppe."),
        ("Forebyggende vedligeholdelse",
         "Vedligeholdelsesplan pr. anlæg med kritiske komponenter, intervaller, reservedele og "
         "**serviceaftaler**; anlæg, der skal køre uden løbende indgriben."),
        ("Black utilities",
         "**Varme**, **vand**, el, **pumper**, **rørsystemer** og **HVAC** — fejlfinding på tværs "
         "af forsyninger, hvor årsagen sjældent sidder, hvor alarmen kommer fra."),
    ]:
        m.bullet(label, body)

    m.section("LEVERANDØRER, KVALIFICERING OG DOKUMENTATION")
    for label, body in [
        ("Serviceleverandører",
         "Præcis opgave, adgang, sikkerhed og tidsstempel; akut og planlagt som to processer — og "
         "kendskab til aftalen, før telefonen tages."),
        ("Kvalificering ved opstart",
         "FAT/SAT og IQ/OQ/PQ med protokoller skrevet før testen; **nul kritiske fund** ved "
         "aflevering, og fund lukket på årsag."),
        ("SAP og DALUX-FM",
         "Data og **dokumentation** vedligeholdt i **SAP** og **DALUX-FM**; historik, der kan "
         "fremvises for QA, og som den næste tekniker kan arbejde videre fra."),
    ]:
        m.bullet(label, body)

    m.section("SAMARBEJDE OG BESLUTNINGER")
    for label, body in [
        ("På tværs af fag",
         "Indkøb, QA, GMP og procesudvikling: krav afklaret, før opgaven bestilles — kort vej "
         "mellem dem, der ved noget, og dem, der beslutter."),
        ("Selvstændigt",
         "**Selvstændige beslutninger** inden for mandatet, også når klokken er mange: stoppe et "
         "anlæg, tilkalde service, eller vente med et argument, der kan dokumenteres."),
        ("Sprog",
         "**Engelsk** i den daglige dialog med internationale kolleger og leverandører — skriftligt "
         "såvel som mundtligt."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Indehaver / Teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · fuldt resultatansvar · drift, service og aflevering")
    m.bullet("Drift med eget ansvar",
              "Serviceopgaver, tilkald og afleveringer med egen økonomi og egen risiko; "
              "underleverandører, reservedele og dokumentation — og beslutningen om at sige nej til "
              "opgaver, der ikke kan løses ordentligt.")

    m.job("Senior Commissioning Engineer / Project Manager, elsystemer",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024",
          scope="37 samtidige CAPEX-projekter · 25 specialister · GMP/FDA/EMA")
    m.bullet("Kvalificering i reguleret miljø",
              "Projektgrundlag, milepæle og månedlig rapportering i SAP ERP; **kvalificering** med "
              "FAT/SAT og IQ/OQ/PQ — **nul kritiske fund** ved aflevering.")

    m.job("Projekt- og værkstedschef", "Ventek-Air · København · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · 2–10 mio. kr. pr. sag · ventilation")
    m.bullet("Ventilation og HVAC",
              "Leverancer med **luftmængde**, tryk og balance som acceptkriterier; daglige "
              "tavlemøder og flaskehalsanalyse, når en sag gik bagud.")

    m.job("Drifts- og vedligeholdelseschef", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="Renseanlæg i 24/7-drift · pumper, VVS, HVAC, højspændingstavler, SCADA")
    m.bullet("Anlæg, der ikke må stoppe",
              "Forebyggende **vedligeholdelse** og fejlfinding døgnet rundt; indgreb planlagt i "
              "snævre vinduer med midlertidig løsning klar, før den blev brugt. LOTO og APV.")

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
           "**Persisk:** modersmål · **Bosat i Måløv**, tyve minutter fra Lyngby · **Kørekort B** · "
           "**Tilkaldevagt** og nattevagt efter aftale · **Kan tiltræde snarest** · Referencer efter "
           "aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA OVERDRAGELSE AF DRIFTEN TIL EN PLAN, DER KAN BRUGES",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–2",
             "Gennemgå alle anlæg med den, der har dem i dag: hvad der er koblet på **BMS** og "
             "**FMS**, hvilke alarmer der har været de sidste tre måneder, og hvad der endnu ikke "
             "står i **SAP** eller **DALUX-FM**."),
            ("Dag 30",
             "Egen liste over kritiske anlæg og komponenter, med interval, ansvarlig og "
             "reservedelsstatus. Vagtlisten gennemgået, så jeg ved, hvem der ringer, og hvad jeg må "
             "beslutte, når jeg har telefonen."),
            ("Dag 60",
             "Første udkast til strategi for **forebyggende vedligeholdelse** for **black utilities**, "
             "med serviceaftaler, der dækker det, de skal — og de huller, hvor ingen aftale findes i "
             "dag."),
            ("Dag 90",
             "Strategien taget i brug i den daglige drift: alarmer reageret på inden for aftalt tid, "
             "alle hændelser dokumenteret samme dag, og de første to anlæg flyttet fra akutte "
             "indgreb til planlagt vedligeholdelse."),
        ],
        widths=(1500, 8830))

    m.section("VAGTTELEFONEN ER EN AFTALE, IKKE EN PLIGT")
    m.para("En vagtordning fungerer, når det er aftalt på forhånd, hvad der må gøres uden at spørge: "
           "hvem der kan tilkaldes, hvad der må lukkes ned, og hvad der under ingen omstændigheder må "
           "røres, før nogen med ansvar er vågen. Jeg vil hellere bruge en time på den aftale i "
           "uge ét end en nat på at ringe rundt uden mandat.", after=70)

    m.section("SERVICEAftalen SKAL LÆSES, FØR DEN BRUGES")
    m.para("Serviceaftaler bliver sjældent læst, før der er en regning. Derfor gennemgår jeg dem, når "
           "der er ro: hvad er dækket, hvad er undtaget, hvilke responstider er lovet, og hvad "
           "koster det, når vi ringer uden for aftalen. Det er den slags arbejde, der ikke ses i en "
           "driftsrapport, men som ses på bundlinjen og i antallet af akutte indgreb.", after=70)

    m.section("ANLÆGSLISTEN ER DEN FØRSTE DOKUMENTATION, DER BETYDER NOGET")
    m.para("En ny facilitet har ikke et vedligeholdelsesproblem endnu, men den har en anlægsliste, og "
           "den afgør alt det andet: hvilke komponenter der er kritiske, hvor ofte de skal ses, "
           "hvilke reservedele der skal ligge på hylden, og hvilke af dem der skal have en "
           "**serviceaftale** og hvilke der ikke skal. Skrives listen forkert i opstarten, bliver den "
           "dyr i årevis — derfor vil jeg hellere bruge tid på mærkning, kritikalitet og intervaller, "
           "mens anlæggene er nye og kvalificeringen stadig er i gang.", after=70)

    m.section("HVAC HANDLER OM FIRE TAL")
    m.para("**Luftmængde**, temperatur, tryk og **luftfugtighed**. Alt andet i et ventilationsanlæg "
           "er mekanik, der skal serviceres, men de fire tal er det, processen og myndighederne "
           "spørger til. Jeg har leveret ventilation som entreprise med balance og acceptkriterier, "
           "og jeg har stået i drift med anlæg, hvor de fire tal var det, der afgjorde, om et rum måtte "
           "bruges.", after=70)

    m.section("DET, DER IKKE STÅR I SYSTEMET, SKER IKKE")
    m.para("I et **reguleret miljø** er historikken lige så vigtig som reparationen. En hændelse, der "
           "ikke er registreret med tid, årsag og handling, findes ikke, når nogen spørger — og den "
           "lærer ikke organisationen noget. Derfor er dokumentation ikke noget, man gør bagefter: den "
           "gøres færdig, mens hænderne stadig er snavsede, i **SAP** eller **DALUX-FM**.", after=0)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "DET ROLLEN KRÆVER — DET HAR JEG LØST",
        ["Krav i opslaget", "Bevis"],
        [
            ("Overvåge og reagere på alarmer fra BMS og FMS, vurdere problemer, foretage eftersyn og inddrage rette service",
             "Alarmvurdering og **eftersyn** i 24/7-drift med **BMS**/**SCADA**; nattevagt og "
             "**tilkaldevagt** med eget mandat til at stoppe og tilkalde."),
            ("Koordinere eksterne serviceleverandører, så planlagt og akut vedligeholdelse bliver planlagt, udført og dokumenteret",
             "11 entrepriser med 14 mand og leverandører på flere sager samtidigt; præcis opgave, "
             "adgang, sikkerhed og tidsstempel på hver."),
            ("Tekniske forsyningsanlæg — black utilities: varme, vand, el, pumper, rørsystemer og HVAC",
             "Fire år med pumper, VVS, HVAC og højspændingstavler på et anlæg, der kørte døgnet "
             "rundt; elautoriseret LV/MV/HV."),
            ("Planlægge, føre tilsyn med og dokumentere vedligeholdelse af udstyr uden serviceaftale",
             "Vedligeholdelsesplaner pr. anlæg med intervaller, ansvarlig og reservedelsstatus — og "
             "tilsyn ført på skrift, også når opgaven blev løst af egne folk."),
            ("Udføre mindre vedligeholdelsesopgaver selv, hvor det er relevant",
             "Elektriker og **maskinmester** i praksis: fejlfinding og reparation udført selv, før "
             "der bliver ringet efter nogen."),
            ("Bidrage til strategi for forebyggende vedligeholdelse og identificere problemområder og anlæg med behov for ekstra fokus",
             "Forebyggende **vedligeholdelse** opbygget på eget anlæg og i egen virksomhed; "
             "problemanlæg identificeret på historik, ikke på mavefornemmelse."),
            ("Sikre sikker drift uden uplanlagt nedetid og anlæg, der fungerer uden løbende indgriben",
             "Ingreb planlagt i snævre vinduer med midlertidig løsning klar på forhånd; LOTO og APV "
             "som fast praksis."),
            ("Vedligeholde data og dokumentation i SAP og DALUX-FM",
             "**SAP** brugt dagligt til budget, prognose og projektdokumentation; **DALUX-FM** brugt "
             "i driften til sager og historik."),
            ("Deltage i kvalificering af udstyr ved opstart",
             "FAT/SAT og IQ/OQ/PQ på 37 projekter med protokoller skrevet før testen — **nul "
             "kritiske fund** ved aflevering."),
            ("Samarbejde med indkøb, QA, GMP og Proces udvikling samt resten af **Facility-teamet**",
             "25 specialister ledet på tværs af teknik, indkøb og drift; krav afklaret med QA, før "
             "opgaven blev bestilt."),
            ("Deltage i tilkaldevagtordning og have vagttelefonen en uge ad gangen",
             "Nattevagt og **tilkaldevagt** på anlæg i 24/7-drift, og telefonen båret i egne "
             "serviceaftaler siden 2023."),
            ("Uddannelse som diplomingeniør, maskinmester eller anden relevant teknisk baggrund",
             "Elautoriseret **maskinmester** (LV/MV/HV), el- og maskinteknisk design (EQF 6) og "
             "B.Tech i teknologiledelse."),
            ("Minimum 3 års relevant teknisk erfaring og bred forståelse for bygningsvedligeholdelse og tekniske installationer",
             "Tyve år med **tekniske installationer** og **bygningsvedligeholdelse** — de sidste otte år i "
             "drift, kvalificering og vedligeholdelse af komplekse anlæg."),
            ("Erfaring fra et reguleret miljø med tilsvarende kompleksitet, fx GMP eller medicinalindustrien, med grundig dokumentationstilgang",
             "Fire år i **medicinalindustrien** hos Novo Nordisk med **GMP**/FDA/EMA, KS og "
             "kvalificering; dokumentation skrevet så den kunne stå i en inspektion."),
            ("Praktisk erfaring med BMS/FMS og facility management-værktøjer som SAP og DALUX-FM",
             "**BMS**/**FMS** i drift, **SAP** dagligt og **DALUX-FM** i sagsbehandling; "
             "**facility management**-systemer lært ved at bruge dem, ikke ved at læse om dem."),
            ("Kendskab til HVAC-principper: luftmængde, temperatur, tryk og luftfugtighed",
             "Ventilation leveret som entreprise med balance og acceptkriterier; køle- og "
             "VVS-teknisk uddannelse (AMU) i baggrunden."),
            ("Venlig og samarbejdsorienteret tilgang, stærk kommunikation, løsningsorienteret og pragmatisk, bevare overblikket og træffe selvstændige beslutninger",
             "**Løsningsorienteret** og **samarbejdsorienteret** i praksis: beslutninger taget inden "
             "for mandatet, også klokken 03, og krav afklaret direkte med dem, der har dem."),
            ("Tale og skrive flydende engelsk i den daglige dialog",
             "**Engelsk** på professionelt niveau, skriftligt og mundtligt; projektdokumentation "
             "ført på engelsk for internationale parter."),
        ],
        widths=(3600, 6746))

    m.section("HVOR JEG VILLE STARTE")
    m.para("Med anlægslisten og de sidste tre måneders alarmer. De to ting tilsammen viser, hvor "
           "faciliteten faktisk bliver holdt kørende, og hvor den bliver holdt kørende af held. "
           "Derefter en runde på alle rum med **BMS**- og **FMS**-punkter og en snak med den, der "
           "har haft telefonen indtil nu — for den viden står sjældent i systemet, og den er dyr at "
           "skulle lære af en alarm klokken 03.", after=0)

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_Cellerator_TekniskDriftsansvarlig.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_Cellerator_TekniskDriftsansvarlig.docx'))
