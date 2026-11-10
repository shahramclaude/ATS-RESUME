# -*- coding: utf-8 -*-
"""Kalundborg Forsyning A/S — projektleder, Projekt & Tilsyn (vand, spildevand, varme).

Dansk opslag → dansk dokument (da-DK): ansøgning side 1, CV side 2, uddannelse + 90 dage +
fire afsnit side 3, kravmatrix side 4.

STILVALG (master/STILREGISTER.md, policy 04.11.2026; godkendt af scripts/style_guard.py,
3/3 skift mod #198):
  register      = TEKNISK-DRIFTSNÆR — kort, konkret, "klokken tre om natten"-nærhed. Rollen er
                  anlægsprojekter i kritisk infrastruktur, hvor anlægget kører, mens det bygges
                  om. Sidst brugt #191.
  åbningsgreb   = C (STEDET FØRST) — Kalundborg som præmis: vand, damp og restvarme er delt
                  mellem virksomheder, længe før nogen kaldte det symbioses. Sidst brugt #190.
  struktur      = MÅLESTOKKEN — hver sektion åbner med et tal og hvad det betyder. Tallene er
                  virksomhedens egne (fire forsyningsarter · tolv projektledere og to
                  tilsynsførende · tretten kilometer fra Tissø · tyve grader i spildevandet) og
                  kandidatens egne (fire år i døgndrift · elleve entrepriser · 37 projekter ·
                  nul kritiske fund). Sidst brugt #190.
  kadence       = tal, derefter hvad det betyder for projektet og for dem, der skal leve med det.

Ingen opdigtede fakta: der påstås IKKE erfaring med fjernvarmedistribution eller med
myndighedsbehandling efter forsyningslovgivningen, og der påstås ikke bygherreerfaring fra et
forsyningsselskab. Det dokumenterede grundlag er fire år i døgndrift på renseanlæg (Biofos
Lynetten), 37 samtidige CAPEX-projekter med økonomi, risici og overdragelse, 11 entrepriser med
14 mand, udbud og kontrakt, arbejdsmiljø (LOTO/APV) samt nul kritiske fund ved aflevering.

Policy: master/README.md — jobbet først, kandidaten kun som bevis, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Projektleder · Anlægsprojekter i vand, spildevand og varme'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4. november 2026")
    m.meta("Kalundborg Forsyning · Projektleder, Projekt & Tilsyn · Dokhavnsvej 15, 4400 Kalundborg")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: projektleder — anlægsprojekter", bold=True, color='1A1A1A')
    m.para("Til afdelingsleder Kenneth Aagaard, Projekt & Tilsyn", after=70)

    # ---------------------------------------------------------------- side 1
    m.para("**I Kalundborg har man delt vand, damp og restvarme mellem virksomheder, længe før nogen "
           "begyndte at kalde det en symbiose.** Det betyder noget for, hvordan et **anlægsprojekt** "
           "her skal drives: man bygger ikke bare noget nyt, man bygger det ind i **kritisk infrastruktur**, "
           "der allerede kører, og som nogen er afhængig af i morgen. Det er den slags projekter, jeg "
           "gerne vil føre til dørs — hvor **driften** ikke er modtageren til sidst, men en part, der "
           "skal med hele vejen.", after=80)

    m.para("**Fire forsyningsarter.** **Vand**, overfladevand til industrien, **spildevand** og "
           "**fjernvarme** — fire systemer, der deler plads, grave og mennesker. Et projekt, der ser "
           "isoleret ud på papiret, rører næsten altid en anden forsyning, og derfor er den første "
           "rigtige opgave at finde ud af, hvem der bliver påvirket i uge 14, når der skal graves i "
           "Dokhavnsvej.", after=80)

    m.para("**Tolv projektledere og to tilsynsførende.** Det er en afdeling, hvor man kan sparre, og "
           "hvor der er **arbejdsmetoder** at dele. Jeg kommer ikke med en færdig model, der skal "
           "indføres; jeg kommer med nogle vaner, der har virket — kort **beslutningsgrundlag**, tydelig "
           "**risikolog**, ugentlig **fremdrift**sopfølgning — og jeg tager gerne imod jeres. At bygge "
           "en fælles **projektmodel** er et arbejde, man gør sammen, ellers holder den ikke — og i en "
           "**matrixorganisation** betyder det, at man låner hinandens faglighed i stedet for at vente "
           "på den.",
           after=80)

    m.para("**Tretten kilometer fra Tissø.** Vandet i **Kalundborg** kommer ikke kun fra grundvandet; "
           "det kommer også gennem en lang ledning og skal videre til virksomheder, der regner med "
           "det. **Forsyningssikkerhed** er derfor et spørgsmål om rør, tryk og aftaler — og om at "
           "kunne tage et anlæg ud af drift i et vindue, hvor ingen mangler vand. Jeg har planlagt "
           "udfald i døgndrift, hvor den slags vinduer var smalle.", after=80)

    m.para("**Tyve grader i spildevandet.** Restvarmen i proces- og spildevand er et af de projekter, "
           "der kræver, at teknik, økonomi og aftaler med naboen går op samtidig. Jeg har ikke regnet "
           "på restvarme fra industrielt spildevand, men jeg har arbejdet med varmegenvinding i "
           "ventilation og **køl** og ved, at grænsefladen mellem to virksomheders anlæg er der, hvor "
           "sådan et projekt enten bliver en god idé eller en lang sag.", after=80)

    m.para("**Fire år i døgndrift.** På Lynetten drev vi et **rensningsanlæg** 24/7 med **pumper**, "
           "højspændingstavler og **SCADA**, og jeg lærte det, der er hele pointen i et "
           "**forsyningsprojekt**: man bygger om på noget, der ikke må stoppe. Det betyder "
           "midlertidige løsninger, der er tænkt færdige, før de bliver nødvendige — og en "
           "**ibrugtagning**, der er aftalt med dem, der står med driften klokken tre om natten.",
           after=80)

    m.para("**Elleve entrepriser på én gang.** **Koordinering** af **rådgivere**, **entreprenører**, "
           "**myndigheder** og egne folk er ikke et møde om ugen; det er en rytme. Jeg har styret 14 "
           "mand og 11 samtidige entrepriser med daglige tavlemøder og flaskehalsanalyser, og 37 "
           "**anlægsprojekter** på tværs af engineering, indkøb og anlæg — og der er altid en uge, "
           "hvor to ting vælter samtidig. Det er den uge, rollen findes for.", after=80)

    m.para("**Nul kritiske fund.** Ved **overdragelse** er det tallet, der betyder noget — ikke hvor "
           "pænt anlægget ser ud på dagen. Jeg har afleveret anlæg i et reguleret miljø, hvor "
           "**dokumentation**en skulle kunne læses af en tredjemand, og hvor **kvalitet** var noget, "
           "man kunne efterprøve. Det er også den mest effektive måde at undgå, at driften arver en "
           "overraskelse, der først viser sig i februar.", after=80)

    m.para("**Jeg har ikke arbejdet i et forsyningsselskab som bygherre**, og jeg har ikke ført "
           "**tilsyn** som ansat tilsynsførende. Det, jeg har, er 20+ år med **anlægsprojekter** i "
           "drift, entreprise og reguleret produktion, elautorisation (LV/MV/HV), el- og "
           "maskinteknisk design (EQF 6) og B.Tech i teknologiledelse og maskinteknik. Erfaring fra "
           "**forsyningsområdet**, som opslaget kalder en fordel, har jeg fra spildevandssiden — og "
           "den del er ikke teoretisk for mig.", after=80)

    m.para("**To stillinger, én opgave.** I søger to, og I skriver, at I ikke behøver have identiske "
           "erfaringer. Det passer mig godt: jeg kommer med projektstyringen og den tekniske forståelse "
           "for anlæg, og jeg vil gerne lære af en kollega, der kender **fjernvarme** og den kommunale "
           "**myndighedsbehandling** bedre, end jeg gør. Det **samarbejde** er en del af grunden til, at jeg "
           "søger her. Kalundborg er godt en times kørsel fra Måløv; "
           "det er en pendling, jeg har valgt til, og jeg kan tiltræde snarest.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Projektleder med 20+ års erfaring i **anlægsprojekter** i drift, entreprise og reguleret "
           "produktion — **elautoriseret maskinmester** (LV/MV/HV), el- og maskinteknisk design "
           "(EQF 6), B.Tech i teknologiledelse og maskinteknik. Fire år i **døgndrift** på renseanlæg, "
           "37 samtidige CAPEX-projekter med **tidsplan**, **økonomi**, **risici** og **overdragelse**, "
           "11 entrepriser med 14 mand — og nul kritiske fund ved aflevering.", after=80)

    m.section("PROJEKTSTYRING FRA PLAN TIL OVERDRAGELSE")
    for label, body in [
        ("Plan og fremdrift",
         "Mål, afgrænsning og leverancer nedskrevet før opstart; få hårde milepæle, synlig kritisk vej "
         "og ugentlig fremdriftsopfølgning, der er kort nok til at blive lavet hver uge."),
        ("Kvalitet og dokumentation",
         "KS, afleveringspakker og dokumentation aftalt med driften undervejs; prøvekørsel og "
         "ibrugtagning planlagt, før anlægget var færdigt — ikke bagefter."),
        ("Risiko og ændringer",
         "Risikolog med ejer og trigger-punkt; ændringer beskrevet, vurderet og godkendt, så "
         "forudsætninger kunne ændres uden at nogen tabte overblikket."),
    ]:
        m.bullet(label, body)

    m.section("ØKONOMI, KONTRAKTER OG INTERESSENTER")
    for label, body in [
        ("Økonomi og opfølgning",
         "Budget, kalkulation og månedlig opfølgning i SAP ERP; prognose opdateret og afvigelser "
         "forklaret med årsag og handling — også når svaret var ubehageligt."),
        ("Udbud og kontrakt",
         "Udbud, tilbudslister og aftalegrundlag; forbehold og grænseflader gennemgået før underskrift, "
         "og ændringsregler kendt af begge parter."),
        ("Interessenter i samme rum",
         "Rådgivere, entreprenører, underentreprenører og myndigheder koordineret i 11 entrepriser; "
         "forventninger afstemt skriftligt og beslutninger eftersporet i referat."),
    ]:
        m.bullet(label, body)

    m.section("DRIFT, ANLÆG OG ARBEJDSMILJØ")
    for label, body in [
        ("Kritisk drift i døgndrift",
         "Renseanlæg med pumper, HVAC, højspændingstavler og SCADA; prioritering efter konsekvens og "
         "midlertidige løsninger klar, når et anlæg skulle ud af drift."),
        ("Arbejdsmiljø i byggefasen",
         "LOTO, APV, risikovurdering ved opstart og sikkerhedsrunder; arbejdsmiljøkoordinering, når "
         "andre arbejder i samme rum — certificeret arbejdsmiljø er et krav, ikke et banner."),
        ("Teknisk forståelse i bund",
         "El, styring og CTS, køl og varme, pumper og vandbehandling; køleteknik som AMU-kursus — nok "
         "til at stille fagfolk de rigtige spørgsmål og gennemskue et svar, der er for pænt."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Ejer / teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · fuldt P&L · projekter, udbud og leverandører")
    m.bullet("Projekt- og forretningsansvar",
              "Projekter fra tilbud til aflevering med eget budget og egen risiko; udbud, "
              "underentreprenører og KS — og ansvaret for at sige nej, når kalkulen ikke holdt.")

    m.job("Senior idriftsættelsesingeniør / projektleder, elsystem",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024",
          scope="37 samtidige anlægsprojekter · 25 specialister · GMP/FDA/EMA")
    m.bullet("Fremdrift, økonomi og overdragelse",
              "Projektgrundlag, milepæle og månedsrapportering i SAP ERP; FAT/SAT og IQ/OQ/PQ med "
              "protokoller skrevet før testen, og overdragelse til drift med nul kritiske fund.")

    m.job("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · DKK 2–10 mio.")
    m.bullet("Koordinering i pressede uger",
              "Daglige tavlemøder og flaskehalsanalyser; omfordeling af mandskab og leverandører, når "
              "en entreprise trak mere end planlagt — med bygherre informeret samme dag.")

    m.job("Vedligeholdelses- og driftsleder", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="Renseanlæg i 24/7-drift · pumper, HVAC, højspændingstavler, SCADA")
    m.bullet("Anlæg, der ikke må stoppe",
              "Forebyggende vedligehold og akut fejlfinding i døgndrift; udfald planlagt i smalle "
              "vinduer, 5S og standard work på værksted og lager, LOTO og APV.")

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
           "modersmål · **Bosat i Måløv**, ca. en times kørsel til Kalundborg · **Kan tiltræde "
           "snarest** · Referencer efter aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA FØRSTE MØDE TIL FØRSTE OVERDRAGELSE",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–2",
             "Læse den nye **projektmodel** igennem og følge to igangværende sager som tilhører: hvor "
             "står **risici**, hvad er sidste godkendte ændring, og hvornår blev **driften** sidst "
             "spurgt?"),
            ("Dag 30",
             "Overtage en afgrænset sag med **tidsplan**, budget og **interessenter**; første "
             "**opfølgning** i jeres format og en fælles aftale med driften om, hvordan "
             "**overdragelse**n skal se ud."),
            ("Dag 60",
             "Egen portefølje og et forslag til én ting, vi gør ens i alle projekter — fx hvordan "
             "**ændringer** godkendes, eller hvordan **dokumentation** overdrages uden at blive en "
             "byrde for driften."),
            ("Dag 90",
             "Første **overdragelse** gennemført efter aftalen; status med dig på, hvad jeg bærer selv, "
             "og hvor jeg stadig skal have et fagligt blik fra en kollega."),
        ],
        widths=(1500, 8830))

    m.section("FIRE ÅRS DØGNDRIFT LÆRTE MIG AT SPØRGE DRIFTEN FØRST")
    m.para("Når man har stået med et **rensningsanlæg**, der ikke må stoppe, lærer man at spørge de "
           "mennesker, der skal overtage anlægget, mens det stadig er en tegning. Ikke fordi de ved "
           "bedst, men fordi de ved noget andet: hvad der er svært at komme til, hvad der bliver slidt "
           "først, og hvad der bliver et problem klokken tre om natten. Det er billigere at tage den "
           "samtale i projekteringen end i uge 60.", after=70)

    m.section("EN TIDSPLAN ER EN AFTALE MED NOGENS HVERDAG")
    m.para("Når vi flytter en **milepæl**, flytter vi også noget for nogen: en entreprenør, der har "
           "booket mandskab, en driftsmedarbejder, der har planlagt en afspærring, eller en borger, der "
           "skal have gravet sin indkørsel op. Derfor skal en tidsplan ikke bare være realistisk — den "
           "skal være meldt ud i god tid og ændret med en samtale, ikke med en mail. Det er den del af "
           "**koordinering**en, der ikke står i planen.", after=70)

    m.section("MYNDIGHEDER ER IKKE EN MODPART")
    m.para("Jeg har ikke siddet med **myndighedsbehandling** efter forsyningslovgivningen, og det skal "
           "jeg lære. Men jeg har samarbejdet med **myndigheder** i byggeri og anlæg i 20 år, og den "
           "erfaring er enkel: en myndighed, der bliver inddraget tidligt og får et klart "
           "**beslutningsgrundlag**, bliver en medspiller; en myndighed, der får sagen til sidst, "
           "bliver en forsinkelse. Det handler ikke om at kende paragrafferne på forhånd, men om at "
           "vide, hvornår man skal spørge.", after=70)

    m.section("TO MÅNEDER FØR OVERDRAGELSE")
    m.para("Der er et tidspunkt i et **anlægsprojekt**, hvor det stadig kan nås: to måneder før "
           "**overdragelse**. Der skal aftales en prøvekørsel med **driften**, dokumentationen skal "
           "være færdig nok til at blive brugt, og der skal være nogen, der ved, hvem man ringer til, "
           "når noget ikke virker en søndag. Jeg har prøvet at komme for sent til den aftale, og det "
           "koster mere end at holde den — ikke i penge, men i tillid til projektet, som er sværere at "
           "genopbygge.", after=70)

    m.section("DET JEG IKKE HAR GJORT ENDNU")
    m.para("Jeg har ikke været bygherreprojektleder i et **forsyningsselskab**, ikke ført **tilsyn** "
           "som ansat tilsynsførende og ikke distribueret **fjernvarme**. Det står i min ansøgning, "
           "fordi det er rigtigt. Det, jeg har, er fire år i døgndrift på et anlæg, der ikke måtte "
           "stoppe, 37 projekter med økonomi og overdragelse og en vane med at læse **kontrakt**er og "
           "**risikolog**er, før de bliver til problemer. Resten lærer jeg i et team på tolv, og det er "
           "en af grundene til at søge her.", after=0)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "HVAD STILLINGEN KRÆVER — HVAD JEG HAR LEVERET",
        ["Krav i opslaget", "Bevis"],
        [
            ("Erfaring med projektledelse af anlægsprojekter",
             "37 samtidige CAPEX-projekter (DKK 2–10 mio.) som projektleder og 11 entrepriser med 14 "
             "mand i egen regi — fra planlægning over **byggeledelse** til overdragelse."),
            ("Relevant teknisk baggrund",
             "Elautoriseret maskinmester (LV/MV/HV), el- og maskinteknisk design (EQF 6), B.Tech i "
             "teknologiledelse og maskinteknik samt køleteknik (AMU)."),
            ("Kendskab til sammenhængen mellem planlægning, projektering og udførelse",
             "Alle tre faser gennemført selv: projektering og udbud i egen virksomhed, udførelse som "
             "entreprenør og bygherreprojektleder — og set konsekvensen af dårlig projektering i "
             "drift."),
            ("Anlægs- og forsyningsprojekter inden for vand, spildevand og varme",
             "Spildevand og vand fra fire år i døgndrift på renseanlæg (pumper, vandbehandling, "
             "SCADA); varme og køl fra ventilation og klimaanlæg. Fjernvarmedistribution er ikke "
             "arbejdet med."),
            ("Klare mål, realistiske tidsplaner og løbende økonomisk opfølgning",
             "Mål og leverancer nedskrevet før opstart; ugentlig fremdrift og månedlig økonomi i SAP "
             "ERP på 37 projekter, med prognose opdateret undervejs."),
            ("Koordinering mellem rådgivere, entreprenører, myndigheder og kolleger",
             "11 entrepriser og 14 mand koordineret med daglige tavlemøder; rådgivere, entreprenører "
             "og myndigheder i samme projekt i 20 år."),
            ("Opfølgning på kvalitet, risikohåndtering og initiativ ved ændrede forudsætninger",
             "Risikolog med ejer og trigger-punkt; ændringer vurderet og godkendt; kvalitet fulgt med "
             "KS og afvigelser lukket med rodårsagsanalyse."),
            ("Dialog med driften gennem projektet og en overdragelse, der lever op til behov og forventninger",
             "Fire år på modtagersiden af projekter — ved, hvad der irriterer driften; afleveringer med "
             "afleveringspakker, prøvekørsel og nul kritiske fund."),
            ("Bidrage til fælles arbejdsmetoder og dele erfaringer",
             "Skabeloner, tjeklister og dashboards indført og delt i egne og andres projekter — 40 % "
             "produktivitetsløft på det administrative; videndeling som vane, ikke som projekt."),
            ("Struktureret og grundig, med fakta og analyser som beslutningsgrundlag",
             "A3, PDCA og standard work som metode; beslutningsoplæg med scenarier og følsomhed, så et "
             "valg kunne begrundes bagefter."),
            ("Bevare overblik, prioritere og få projektet videre ved uforudsete forhold",
             "Fire år i døgndrift, hvor planen blev afbrudt af nedbrud; prioritering efter konsekvens "
             "og midlertidige løsninger klar, før de blev nødvendige."),
            ("Lytte, kommunikere tydeligt og skabe tillidsfulde relationer",
             "Kunder, entreprenører, underentreprenører og egne folk i 20 år; tillid bygget ved at "
             "melde ud, før den anden opdagede problemet."),
            ("Samle mennesker med forskellige perspektiver og tage de nødvendige samtaler",
             "Faglige uenigheder holdt faglige på 37 projekter med 25 specialister og på 11 "
             "entrepriser; eskalering tidligt frem for konfrontation sent."),
            ("Styre projektets rammer, følge op og skabe fremdrift",
             "Projektrammer, milepæle og økonomi styret selvstændigt; fuldt P&L-ansvar siden 2023 og "
             "projektansvar for 37 sager."),
            ("Erfaring fra forsyningsområdet er en fordel",
             "Spildevandssiden af forsyningsområdet, fire år i døgndrift — ikke som bygherre i et "
             "forsyningsselskab, men med hænderne i anlægget."),
            ("Lyst til at tage ansvar og bidrage til et stærkt fagligt og socialt fællesskab",
             "Egen virksomhed drevet siden 2023 med ansvar for alt fra første opkald til sidste "
             "faktura; trives med sparring og med at dele, hvad der virkede."),
        ],
        widths=(3600, 6746))

    m.section("ET ANLÆG, DER KØRER, SKAL BYGGES OM AF NOGEN, DER IKKE ER BANGE FOR DET")
    m.para("Det er den forskel, jeg tror, jeg kan bidrage med i **Kalundborg**: jeg har prøvet at stå "
           "med et anlæg, der ikke måtte stoppe, mens det skulle ændres. Det gør én kedelig på den "
           "gode måde — man vil have midlertidige løsninger, afspærringer og telefonnumre på plads, før "
           "spaden går i jorden. Ikke fordi man er bange for at bygge, men fordi man ved, hvad der sker, "
           "når der ikke er vand i hanen.", after=70)

    m.section("HVOR JEG VILLE STARTE")
    m.para("Med at læse jeres **projektmodel** og se på to igangværende sager: hvor står **risici**, "
           "hvornår blev **driften** sidst inddraget, og hvad er den seneste **ændring**, nogen har "
           "godkendt? Derefter overtage én sag og køre den efter bogen, så kollegerne kan se, hvordan "
           "jeg arbejder, før vi skal være enige om noget fælles. Tillid i et team på tolv kommer ikke "
           "fra et oplæg; den kommer fra den første sag, man ikke tabte.", after=0)

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_KalundborgForsyning_Projektleder.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_KalundborgForsyning_Projektleder.docx'))
