# -*- coding: utf-8 -*-
"""Stryhns Gruppen A/S — Teamleder, vedligeholdsafdelingen, Havnsø (Føllenslev).

Dansk opslag → dansk dokument (da-DK): ansøgning side 1, CV side 2, uddannelse + 90 dage +
fire afsnit side 3, kravmatrix side 4.

STILVALG (master/STILREGISTER.md, policy 04.11.2026; godkendt af scripts/style_guard.py,
3/3 skift mod #193):
  register      = ENTREPRENØR — praktisk, mandskab, fremdrift, håndværk. Rollen er
                  arbejdsledelse på en fabrik: nogen skal beslutte, hvem der går hvorhen, og
                  selv tage fat når det brænder. Sidst brugt #187.
  åbningsgreb   = H (DAGSFORLØBET) — "klokken 06.10 står en pakkelinje stille". Sidst brugt
                  #183 (Siemens Energy).
  struktur      = FØR/EFTER — fem par: hvordan en uge i afdelingen ser ud nu, og hvordan den
                  ser ud, når koordineringen er på plads. Sidst brugt #186.
  kadence       = kort før-sætning, derefter efter-sætning med værktøj, tal eller praksis.

Ingen opdigtede fakta: ingen erfaring fra fødevareproduktion påstås, og der påstås ikke
PLC-programmering. Det dokumenterede grundlag er drift og vedligehold i 24/7-anlæg (Biofos
Lynetten), verifikation og dokumentation i GMP-miljø (Novo Nordisk), koordinering af
14-mands entrepriseteams med daglige tavlemøder (Ventek-Air), personaleansvar for 5
elektrikere + 3 lærlinge og vagtplanlægning for 12 mekanikere (ELOHVAC, ARJ).

Policy: master/README.md — jobbet først, kandidaten kun som bevis, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Teamleder · Vedligehold, drift og koordinering'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4. november 2026")
    m.meta("Stryhns Gruppen A/S · Teamleder, vedligeholdsafdelingen · Havnevej 32, 4591 Føllenslev")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: teamleder — vedligeholdsafdelingen, Havnsø", bold=True, color='1A1A1A')
    m.para("Til teknisk chef Dennis Henrik Holmgaard Larsen", after=70)

    # ---------------------------------------------------------------- side 1
    m.para("**Klokken 06.10 står en pakkelinje stille, og den, der ved hvorfor, er ikke mødt ind "
           "endnu.** Sådan starter en del af dagene i en vedligeholdsafdeling — ikke med et møde, men "
           "med et spørgsmål om, hvem der rykker, hvad der kan vente, og hvad der ikke kan. Det er den "
           "morgen, rollen bliver målt på. Ikke de dage hvor planen holder, men de dage hvor den ikke "
           "gør.", after=80)

    m.para("**Før: alle løber mod den samme maskine. Efter: der er en eskaleringstrappe, og alle ved, "
           "hvor på den de står.** På Lynetten drev vi et kritisk renseanlæg 24/7 med pumper, "
           "højspændingstavler og SCADA, hvor et nedbrud ikke var en forsinkelse, men en begivenhed. "
           "Det, der holdt os kørende, var ikke flere hænder — det var at det var aftalt, hvem der "
           "tager den første vurdering, hvornår man kalder en kollega ind, og hvilke reservedele der "
           "skal ligge på hylden, fordi de ikke kan skaffes i morgen.", after=80)

    m.para("**Før: opgaver bliver fordelt til den, der står nærmest. Efter: de bliver fordelt til den, "
           "der skal have dem — og står på en tavle, hvor nogen kan se dem.** Hos Ventek-Air "
           "koordinerede jeg 14 mand og 11 samtidige entrepriser med daglige tavlemøder og "
           "flaskehalsanalyser. Forskellen var ikke mødet; den var, at opgaven havde en ejer og en "
           "næste handling, og at den ikke forsvandt, fordi telefonen ringede. Jeg vil have tre baner "
           "på den tavle — akut, planlagt og projekt — og en regel for, hvad der må flytte en opgave "
           "fra den ene til den anden.", after=80)

    m.para("**Før: viden sidder i hovedet på den, der har været der længst. Efter: den sidder i en A3 "
           "og i et **planlagt vedligehold**, som den næste kan udføre.** De fejl, der kommer igen, "
           "kommer igen af en grund. Jeg har lavet rodårsagsanalyse med A3, 5xHvorfor og Ishikawa, "
           "skrevet standard work for det faste arbejde og brugt 5S på lager og værksted, så "
           "reservedelsflowet ikke afhænger af, hvem der har vagten. Det er også den eneste måde, en "
           "turnus kan fungere uden at gå ud over oppetiden.", after=80)

    m.para("**Før: vagtplanen bliver lavet om fem gange om ugen. Efter: den er lavet én gang og "
           "justeret på faste tidspunkter — sammen med dig.** Jeg har lagt vagtplaner for 12 mekanikere "
           "og teknikere og drevet skifteholdsdrift med aften og nat, så jeg ved, at planen ikke kun "
           "skal gå op på papiret; den skal kunne forklares for den, der holder fri i weekenden. "
           "Turnus på aften hver 6. uge og planlagt lørdagsarbejde er til at planlægge omkring, hvis "
           "den bliver meldt ud i god tid og holdt.", after=80)

    m.para("**Før: tallene ligger i en rapport, nogen læser i ny og næ. Efter: de står på tavlen klokken "
           "07.00 med en ejer ved siden af.** Oppetid, **OEE**, **MTBF** og MTTR samt hvor stor en del "
           "af arbejdet der er planlagt i stedet for akut. Jeg har bygget KPI-dashboards i Power BI og "
           "brugt dem til at flytte arbejde fra brandslukning til forebyggelse — og til at vise, hvad "
           "det gav, når nogen spurgte om afdelingen fik noget for pengene.", after=80)

    m.para("**Jeg er ikke specialist i alle anlæg på Havnsø.** Jeg kommer ikke ind og har en "
           "mening om jeres **pakkemaskiner** på første dag. Den første måned handler om at lære "
           "linjerne, **procesanlæggene**, **køl**, **frost**, **ventilation**, **trykluft**, **varme** "
           "og det **bygningsvedligehold**, der også skal være styr på — og om at lytte til de "
           "**teknikere** og **reparatører**, der ved mere om den end jeg gør. Min rolle er at gøre "
           "deres viden omsættelig til prioritering.", after=80)

    m.para("**Og personaleansvaret ligger hos dig — det passer mig fint.** Jeg har prøvet begge sider: "
           "haft personaleansvar for 5 elektrikere og 3 lærlinge og koordineret teams uden at være "
           "chef. Modellen i opslaget er den, jeg selv foretrækker, fordi den lægger koordineringen "
           "tæt på driften og lader udviklingssamtalerne ligge der, hvor de hører til.", after=80)

    m.para("**Hvad jeg kommer med.** Elautoriseret maskinmester (LV/MV/HV) med el og automatik i "
           "bunden, el- og maskinteknisk design (EQF 6), B.Tech i teknologiledelse og maskinteknik og "
           "**køleteknik** fra AMU — 20+ år i drift, vedligehold og verifikation, heraf fire år med "
           "kritisk 24/7-drift. Jeg har ikke arbejdet i **fødevareproduktion** før; til gengæld har jeg "
           "arbejdet i GMP-miljø, hvor hygiejne, dokumentation og adgang er en del af arbejdsgangen, og "
           "hvor **K-Salats** slags produktionslinje ikke er det svære — det er kulturen omkring den, "
           "og den lærer man ved at gå på gulvet.", after=80)

    m.para("Jeg bor i Måløv, og Havnsø er godt en times kørsel — det er en pendling, jeg har forholdt "
           "mig til, og som jeg er indstillet på. Jeg har set, at I blev arbejdsmiljøcertificeret på "
           "Havnsø i 2024, og at I beskriver jer selv som et hus, hvor man løfter i fællesskab; det er "
           "den slags sted, jeg gerne vil være teamleder. Jeg kan tiltræde snarest.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Drifts- og vedligeholdsleder med 20+ års erfaring fra kritisk drift og tekniske anlæg — "
           "**elautoriseret maskinmester (LV/MV/HV)**, el- og maskinteknisk design (EQF 6), B.Tech i "
           "teknologiledelse og maskinteknik. Har koordineret 14-mands teams og 11 entrepriser, ligget "
           "i 24/7-drift med pumper, ventilation og højspændingstavler og arbejdet med **planlagt "
           "vedligehold**, **5S**, **A3** og **tavlemøder** — med **KPI** i **Power BI** og fuldt "
           "P&L-ansvar siden 2023.", after=80)

    m.section("DRIFT, NEDBRUD OG OPPETID")
    for label, body in [
        ("Kritisk drift i døgndrift",
         "Renseanlæg med pumper, HVAC, højspændingstavler og SCADA: forebyggende vedligehold, akut "
         "fejlfinding og prioritering af indsats, når flere anlæg krævede noget samtidigt."),
        ("Fejlfinding på anlæg og styring",
         "Fejlfinding på motorer, frekvensomformere, følere, **pneumatik**, **trykluft** og "
         "**procesanlæg**; læser og bruger **PLC** og **HMI** i fejlfindingen — programmerer dem ikke "
         "selv, men kan følge sekvensen og finde ud af, hvor den stopper."),
        ("Utility og bygningsdrift",
         "**Køl**, **frost**, **ventilation**, **varme** og **vand** samt tavler, nød- og "
         "panikbelysning og **bygningsvedligehold**; køleteknik er taget som AMU-kursus."),
    ]:
        m.bullet(label, body)

    m.section("PLANLÆGNING, KPI OG FORBEDRING")
    for label, body in [
        ("Koordinering af mandskab",
         "Daglige **tavlemøder** og flaskehalsanalyser for 14 mand og 11 entrepriser; opgavefordeling "
         "med ejer og næste handling, **prioritering** mellem akut, planlagt og projekt."),
        ("Vagtplan og turnus",
         "**Vagtplan** for 12 mekanikere og teknikere, skifteholdsdrift med aften og nat, "
         "weekendbemanding og ferieafvikling planlagt med ledelsen i fast kadence."),
        ("Måling og forbedring",
         "**Oppetid**, **OEE**, **MTBF**/MTTR og andelen af planlagt arbejde fulgt på **KPI**-tavler "
         "og i **Power BI**; **Lean**-værktøjer som 5S, PDCA, SMED og Kaizen med dokumenteret effekt."),
    ]:
        m.bullet(label, body)

    m.section("MENNESKER OG SIKKERHED")
    for label, body in [
        ("Personale og oplæring",
         "Personaleansvar for 5 elektrikere + 3 lærlinge: 1:1, MUS, oplæring og kompetencematrix, så "
         "den næste kan løfte opgaven."),
        ("Sikkerhed og arbejdsmiljø",
         "**LOTO**, **APV**, risikovurdering ved opstart og nærved-hændelser; nul kritiske afvigelser "
         "i serviceaftalerne og ved aflevering i GMP-miljø."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Ejer / teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · fuldt P&L · service, produktion og mindre projekter")
    m.bullet("Drift, akutudkald og økonomi",
              "Fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg, egen "
              "vagtordning, fuldt P&L og tilbudsberegning; AI-værktøjer til tidsplaner, tjeklister og "
              "KPI-dashboards — over 40 % produktivitetsløft på det administrative.")

    m.job("Senior idriftsættelsesingeniør / projektleder, elsystem",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024",
          scope="37 samtidige anlægsprojekter · 25 specialister · GMP/FDA/EMA")
    m.bullet("Verifikation og koordinering",
              "FAT/SAT og IQ/OQ/PQ: protokoller skrevet før testen, afvigelser lukket med "
              "rodårsagsanalyse — nul kritiske fund. Fremdrift og økonomi på tværs af engineering, "
              "indkøb og anlæg i SAP ERP.")

    m.job("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · DKK 2–10 mio.")
    m.bullet("Daglig koordinering",
              "Tavlemøder, kapacitetsstyring og flaskehalsanalyse; omfordeling af mandskab, når en "
              "entreprise trak mere end planlagt.")

    m.job("Vedligeholdelses- og driftsleder", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="Kritisk renseanlæg i 24/7-drift · pumper, køl, HVAC, højspændingstavler, SCADA")
    m.bullet("Oppetid og prioritering",
              "Akut fejlfinding og forebyggende vedligehold på el- og maskinanlæg døgnet rundt; "
              "prioritering af indsats efter konsekvens for driften, ikke efter hvem der ringede først.")
    m.bullet("Værksted, lager og sikkerhed",
              "5S og Standard Work på værksted og lager, reservedelsflow, LOTO, APV og nærved-"
              "hændelser.")

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
           "modersmål · **Bosat i Måløv**, bil og kan være på Havnsø om morgenen · **Kan tiltræde "
           "snarest** · Referencer efter aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA NEDBRUD TIL PLAN",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–2",
             "Gå på gulvet på alle skift. Lære linjerne, **pakkemaskinerne**, **procesanlæggene** og "
             "**utility** at kende; gennemgå de sidste tre måneders **nedbrud** og se, hvilke der kom "
             "igen. Ingen ændringer i de to første uger, ud over det sikkerhedsmæssige."),
            ("Dag 30",
             "Tavlen i brug med tre baner og en ejer pr. opgave. Eskaleringstrappe aftalt med dig: "
             "hvem rykker, hvornår, og hvad koster en times stop. Basismåling af **oppetid**, "
             "**MTBF** og andelen af planlagt arbejde."),
            ("Dag 60",
             "Vagtplan og **turnus** lagt i fast kadence. De tre hyppigste **nedbrud** har hver fået "
             "en A3 med en **planlagt vedligehold**-handling; **reservedele** på de kritiske emner "
             "gennemgået med lageret."),
            ("Dag 90",
             "Første **KPI**-gennemgang med dig på et helt kvartal: **OEE**, oppetid, akut/planlagt-"
             "fordeling og status på de mindre **projekter**. Forslag til, hvad vi tager først i næste "
             "kvartal — og hvad vi bevidst lader være."),
        ],
        widths=(1500, 8830))

    m.section("ET LAGER ER EN DEL AF VEDLIGEHOLDET")
    m.para("En manglende pakning på hylden kan koste en hel aften, og den beslutning bliver træffet "
           "længe før, nogen står med en stoppet **produktionslinje**. Derfor er **reservedele** og "
           "**prioritering** af lageret en del af vedligeholdet og ikke en indkøbsopgave ved siden af. "
           "Jeg har prøvet at mangle delen og at have den; den anden version er billigere, også når "
           "den ser dyrere ud på bundlinjen i november.", after=70)

    m.section("OPPETID ER IKKE ET TAL, MAN RAPPORTERER — DET ER ET VALG, MAN TAGER OM MORGENEN")
    m.para("**OEE** og **oppetid** bliver skabt i de første tyve minutter, hvor nogen beslutter, om "
           "den lille ulyd skal undersøges nu eller efter frokost. Jeg vil hellere have en aftale om, "
           "hvad der må vente, end en rapport om, hvad der ventede. Det er også derfor, jeg holder af "
           "**tavlemøder** klokken syv og ikke klokken ti.", after=70)

    m.section("TURNUS SKAL KUNNE FORKLARES, IKKE BARE PLANLÆGGES")
    m.para("En **vagtplan** går altid op i et regneark. Det er i hjemmet, den skal gå op. Aften hver "
           "6. uge og planlagt lørdagsarbejde er til at leve med, hvis den bliver meldt ud i god tid, "
           "hvis bytte handler om vilje og ikke om held, og hvis den tekniske chef og jeg har samme "
           "billede af, hvad der er muligt. Det har jeg prøvet med 12 mand og med 5 elektrikere — det "
           "er ikke et regnearksproblem.", after=70)

    m.section("ØKONOMI I VEDLIGEHOLD HANDLER OM TIMING")
    m.para("Der er to måder at bruge penge på en fabrik: betale for det, der holder, eller betale for det, "
           "der er stoppet. Den anden regning er altid dyrere, men den kommer senere, og derfor vinder "
           "den nogle gange i et budgetmøde. Jeg har arbejdet med fuldt P&L-ansvar siden 2023 og brugt "
           "investeringsmodeller (NPV/IRR) til at vælge mellem reparation og udskiftning — ikke for at "
           "gøre regnearket flot, men for at kunne sige til en teknisk chef: her er hvad det koster at "
           "vente, og her er hvad vi får for at gøre det nu.", after=70)

    m.section("JEG HAR IKKE STÅET PÅ DENNE FABRIK — DET ER HELLER IKKE DET, DER AFGØR DET")
    m.para("Jeg kender ikke jeres linjer endnu, og jeg vil ikke påstå, at **K-Salats** produktions-"
           "linje er som det renseanlæg, jeg drev. Det, der ligner, er logikken: nogen skal vide, "
           "hvad der er kritisk, hvem der rykker, hvad det koster at vente, og hvordan viden bliver "
           "hængende efter den, der går på pension. Den del har jeg prøvet i **fødevareproduktion**s "
           "nabolag — i GMP — og i fire år i døgndrift. Resten lærer jeg ved at gå på gulvet, og det "
           "er også der, jeg helst vil være teamleder.", after=0)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "HVAD STILLINGEN KRÆVER — HVAD JEG HAR LEVERET",
        ["Krav i opslaget", "Bevis"],
        [
            ("Sikre den daglige drift og koordinering i vedligeholdsafdelingen",
             "Daglig koordinering af 14 mand og 11 entrepriser med tavlemøder; 24/7-drift på Lynetten "
             "med forebyggende vedligehold og akut fejlfinding."),
            ("Planlægge og fordele opgaver mellem afdelingens teknikere",
             "Opgavefordeling med ejer og næste handling; vagtplan for 12 mekanikere og teknikere; "
             "kapacitetsstyring ved 37 samtidige projekter."),
            ("Håndtere akutte nedbrud og prioritere ressourcer, så produktionen påvirkes mindst muligt",
             "Eskaleringstrappe og prioritering efter konsekvens i døgndrift; fejlfinding på pumper, "
             "HVAC, højspændingstavler og SCADA med fokus på tid til genopretning."),
            ("Deltage aktivt i fejlfinding og tekniske problemstillinger",
             "Fejlfinding på motorer, frekvensomformere, følere, pneumatik og procesanlæg; læser PLC "
             "og HMI i fejlfindingen — programmerer dem ikke selv."),
            ("Bidrage til planlagt vedligehold og løbende forbedringer",
             "Forebyggende vedligehold som system, ikke som lyst; A3 og 5xHvorfor på tilbagevendende "
             "fejl; 5S og Standard Work på værksted og lager."),
            ("Samarbejde om afdelingens økonomi og budgetmål",
             "Fuldt P&L-ansvar siden 2023; tilbud og kalkulation, materialestyring, SAP ERP; "
             "investeringsmodeller (NPV/IRR) til reparér-eller-udskift."),
            ("Udarbejde og følge op på vagtplaner med teknisk chef",
             "Vagtplan for 12 mand og skifteholdsdrift med aften og nat; weekend og ferie planlagt i "
             "fast kadence med ledelsen."),
            ("Drive tavlemøder og følge op på mål og KPI'er",
             "Daglige tavlemøder og flaskehalsanalyser; KPI-tavler og Power BI-dashboards for oppetid, "
             "OEE, MTBF/MTTR og andelen af planlagt arbejde."),
            ("Gennemføre mindre maskin- og procesrelaterede projekter",
             "37 samtidige anlægsprojekter (DKK 2–10 mio.) med fremdrift, økonomi og aflevering; "
             "mindre udskiftninger og ombygninger i egen virksomhed."),
            ("Bidrage til et sikkert og velfungerende arbejdsmiljø",
             "LOTO, APV, risikovurdering, sikkerhedsrunder og nærved-hændelser; nul kritiske "
             "afvigelser i serviceaftaler og ved aflevering i GMP-miljø."),
            ("Teknisk baggrund og erfaring fra produktions- eller procesindustrien",
             "Elautoriseret maskinmester (LV/MV/HV), el- og maskinteknisk design (EQF 6), B.Tech; "
             "drift og vedligehold i procesanlæg i døgndrift — ikke i fødevareproduktion."),
            ("Bred teknisk forståelse: pakkemaskiner, procesanlæg, el og automatik, utility",
             "El, tavler og styring, motorer og frekvensomformere, pneumatik; køl, frost, ventilation, "
             "trykluft, varme og vand fra drift og fra AMU-kursus i køleteknik."),
            ("Forståelse for tekniske installationer og bygningsvedligehold",
             "El-tekniske installationer, nød- og panikbelysning, ABA/ABV, UPS og PDS; bygnings- og "
             "ejendomsdrift for erhvervskunder siden 2023."),
            ("Struktureret, vedholdende og handlingsorienteret — bevarer roen under pres",
             "Prioritering i døgndrift og ved akutudkald; A3, PDCA og standard work som arbejdsform; "
             "40 % produktivitetsløft på administration via faste tjeklister og dashboards."),
            ("Synlig og nærværende teamleder, der skaber samarbejde og engagement",
             "Personaleansvar for 5 elektrikere + 3 lærlinge med 1:1 og MUS; situationsbestemt ledelse "
             "(SLII) på skiftende arbejdspladser; kompetencematrix og struktureret oplæring."),
            ("Trives i en omskiftelig hverdag med skiftende prioriteter",
             "Skifteholdsdrift med aften og nat i fire år; 11 samtidige entrepriser og 37 samtidige "
             "projekter; daghold og turnus er en arbejdsform, jeg har prøvet før."),
        ],
        widths=(3600, 6746))

    m.section("ET TAVLEMØDE ER FÆRDIGT, NÅR NOGEN HAR TAGET EN OPGAVE")
    m.para("Der findes møder, hvor alle er enige, og hvor ingenting flytter sig. Forskellen er ikke "
           "dagsordenen; det er, om der står et navn og en dag ud for hver linje. Jeg har holdt "
           "tavlemøder på en byggeplads med 14 mand, hvor halvdelen af tiden gik med at flytte "
           "opgaver mellem folk, fordi materialet ikke var der. Det, der løste det, var ikke et bedre "
           "møde — det var at lageret og **prioritering**en kom ind i mødet. Det samme vil jeg gøre på "
           "Havnsø: **Lean** er kun et værktøj, hvis det ændrer, hvad der sker klokken otte.", after=70)

    m.section("HVOR JEG VILLE STARTE")
    m.para("Med at gå en uge på alle skift og lytte — og med at se på, hvad der står på tavlen i dag. "
           "Derefter tage de tre **nedbrud**, der har kostet mest tid i det seneste kvartal, og lave en "
           "A3 på hver: hvorfor skete det, hvad ville have fanget det, og hvad koster det at gøre "
           "noget ved det nu frem for i december. Det er den slags arbejde, der giver ro i hverdagen "
           "— og som gør, at **oppetid** bliver et resultat og ikke et håb.", after=0)

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_Stryhns_Teamleder.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_Stryhns_Teamleder.docx'))
