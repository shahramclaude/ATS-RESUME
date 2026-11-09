# -*- coding: utf-8 -*-
"""Cembrane A/S (Ovivo) — Maintenance Technician, Lynge.

Dansk opslag → dansk dokument (da-DK): ansøgning side 1, CV side 2, uddannelse + 90 dage +
fire afsnit side 3, kravmatrix side 4.

STILVALG (master/STILREGISTER.md, policy 04.11.2026; godkendt af scripts/style_guard.py,
3/3 skift mod #191):
  register      = INGENIØR-PRÆCIS — definitioner, intervaller, tolerancer, sporbarhed. Passer til
                  en vedligeholdelsesrolle på procesudstyr, hvor forskellen mellem drift og stop
                  er et interval og en dokumenteret kontrol. Sidst brugt #182.
  åbningsgreb   = F (KONSEKVENSEN) — hvad der sker, når ovnen går ned: ikke ét stop, men en kæde
                  gennem ekstruder, blander og en kundes ibrugtagning. Sidst brugt #185.
  struktur      = ORDLISTEN — virksomhedens og opslagets egne begreber oversat til praksis:
                  oppetid · forebyggende vedligehold · sporbarhed · serviceaftaler · reservedele ·
                  tungt udstyr. Sidst brugt #182, i en anden version.
  kadence       = kort definition, derefter hvad der gøres, og hvordan det måles.

Ingen opdigtede fakta: ingen erfaring med SiC-membraner, ekstrudere eller sintringsovne påstås.
Det dokumenterede grundlag er 24/7-drift af et af landets største renseanlæg (pumper, køl, HVAC,
kompressorer, højspænding, SCADA), service og køleteknik i egen virksomhed samt fuld
elautorisation LV/MV/HV.

Policy: master/README.md — jobbet først, kandidaten kun som bevis, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Vedligeholdelsestekniker · Produktionsudstyr, oppetid og sporbarhed'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("9. november 2026")
    m.meta("Cembrane A/S (Ovivo) · Maintenance Technician · Nøglegaardsvej 10, 3540 Lynge")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Maintenance Technician — Cembrane", bold=True, color='1A1A1A')
    m.para("Til Head of Operations Lasse Boehm", after=70)

    # ---------------------------------------------------------------- side 1
    m.para("**Når højtemperaturovnen går ned, stopper den ikke ved ovnen.** Den stopper ved "
           "ekstruderen, der ikke kan tømme sig, ved blanderen, der blev fyldt forgæves, og til sidst "
           "hos en kunde, der har planlagt ibrugtagning af et vandbehandlingsanlæg et helt andet sted. "
           "Vedligeholdelse er derfor ikke en opgave, der følger produktionen — den er forudsætningen "
           "for, at produktionen kan planlægges. Jeg har stået med den slags anlæg i mere end fire år, "
           "hvor et stop blev målt i timer og ikke i kroner, og jeg vil gerne gøre det samme her.",
           after=80)

    m.para("**Oppetid** er ikke et procenttal på en tavle, men de timer du har købt tilbage, inden "
           "nogen spørger. På Lynetten under Biofos drev jeg et af landets største renseanlæg i "
           "**24/7-drift**: pumper, kompressorer, køle- og ventilationsanlæg, højspændingstavler og "
           "SCADA. Oppetid blev skabt om natten og i weekenderne — ved at vide, hvilke komponenter der "
           "kunne tages ud i hvilket vindue, og hvilke der ikke måtte.", after=80)

    m.para("**Forebyggende vedligehold** er et interval, ikke en hensigt. Jeg planlægger efter "
           "driftstimer, temperatur, vibration og smøring — ikke efter hvornår det passer — og lægger "
           "arbejdet i de vinduer, hvor produktionen alligevel står stille. **Reparationer og "
           "renoveringer** kommer oveni, og de skal kunne dokumenteres bagefter: hvad blev skiftet, "
           "hvorfor, og hvad koster det næste gang.", after=80)

    m.para("**Sporbarhed** betyder, at den næste person kan se, hvad der blev gjort — ikke kun jeg. "
           "Jeg registrerer arbejdet i det system, virksomheden bruger, med udstyr, årsag, indsats og "
           "tid, og jeg har prøvet at stå i en GMP-revision, hvor netop den registrering var forskellen "
           "mellem et fund og nul kritiske fund. **Serviceaftaler** behandles på samme måde: "
           "kompressoren og gaffeltrucken har aftalte responstider, og en aftale, der ikke bliver fulgt "
           "op, er dyrere end den service, den skulle dække.", after=80)

    m.para("**Reservedele** er en beslutning om kritikalitet, ikke en lagerbeholdning. Jeg vil "
           "sammen med engineering og indkøb klassificere komponenterne: hvad skal ligge på hylden, "
           "hvad kan skaffes på et døgn, og hvad koster en uge i leveringstid på ovnen. Jeg har styret "
           "reservedelsflow og **5S** på et kritisk anlæg og ved, at den del, der mangler klokken "
           "02:00, altid er den, ingen syntes var vigtig.", after=80)

    m.para("**Tungt udstyr** kræver en anden disciplin end en pumpe: **blander, ekstruder og "
           "højtemperaturovn** skal justeres, smøres og kontrolleres efter tolerancer — lejer, "
           "tætninger, remme, følere og varmeelementer — og et eftersyn skal planlægges, før det bliver "
           "en reparation. Jeg har ikke arbejdet med SiC-membraner eller sintringsovne før; det lærer "
           "jeg af jeres engineering og af driftstimerne, og indtil da spørger jeg frem for at gætte.",
           after=80)

    m.para("**Fejlfinding** er en rækkefølge, ikke en fornemmelse: spørg dem, der kørte maskinen, isolér "
           "energien, mål før du skruer, skift det mindste først, og skriv bagefter ned, hvad der var "
           "årsagen. Akutte stop har det med at komme igen, hvis man kun reparerer symbolet — derfor "
           "slutter hver fejlretning med en linje om, hvad der skal ændres, så den ikke kommer tilbage.",
           after=80)

    m.para("**Installation af nyt udstyr** er den billigste vedligeholdelse, man kan lave. Når "
           "maskinen bliver samlet, kan man se, hvordan den er justeret, hvad der er svagheden, hvilke "
           "reservedele der følger med, og hvad leverandøren mener med normal drift. Jeg har stået på "
           "den side af FAT/SAT og idriftsættelsen i årevis — 37 samtidige anlægsprojekter — og ved, at "
           "den viden er billigst at fange, inden garantien løber ud.", after=80)

    m.para("**Struktur** er ikke et projekt, man bliver færdig med. En fabrik i vækst får nyt udstyr "
           "hurtigere, end der bliver skrevet rutiner for det, og derfor skal vedligeholdelsen bygges "
           "som et system — register, intervaller, reservedele, registrering — mens produktionschefen "
           "stadig kan støtte, og ikke som en samling brandslukninger, der bliver sværere at arve for "
           "hver måned.", after=80)

    m.para("Jeg bor i Måløv, har 25 minutter til Lynge og bil, og jeg er **elautoriseret (LV/MV/HV)** "
           "— så **elektrisk fejlfinding** er ikke et bonusområde, jeg skal henvise, men en del af den "
           "samme fejlretning som det mekaniske. Jeg kan tiltræde snarest.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Vedligeholdelses- og driftstekniker med 20+ års erfaring fra kritiske anlæg og produktion — "
           "**elautoriseret maskinmester (LV/MV/HV)**, el- og maskinteknisk design (EQF 6), B.Tech og "
           "køleteknik (AMU). Har drevet et af landets største renseanlæg i **24/7-drift** med pumper, "
           "kompressorer, køle- og ventilationsanlæg og højspændingstavler, bygget **forebyggende "
           "vedligehold** op i produktionsvinduer og ført **reservedelsflow, 5S, LOTO og "
           "dokumentation** — i dag med fuldt P&L-ansvar i egen servicevirksomhed.", after=80)

    m.section("VEDLIGEHOLD OG DRIFT")
    for label, body in [
        ("Pumper, kompressorer og køl",
         "Daglig drift og reparation på pumper, kompressorer, køle- og ventilationsanlæg i 24/7-drift; "
         "fejlfinding døgnet rundt og reparation uden at flytte det, der ikke kunne flyttes."),
        ("Forebyggende vedligehold",
         "Eftersynsplaner efter driftstimer og tilstand, lagt i produktionsvinduer; reparationer og "
         "renoveringer dokumenteret med udstyr, årsag og indsats."),
        ("Oppetid og nedbrud",
         "Prioritering ved stop: hvad der skal køre først, hvem der rykker, og hvad det koster — "
         "besluttet før situationen opstår, ikke under den."),
    ]:
        m.bullet(label, body, after=20)

    m.section("EL, FEJLFINDING OG SIKKERHED")
    for label, body in [
        ("Elektrisk fejlfinding",
         "Elautorisation LV/MV/HV: fejlfinding på motorer, styringer, frekvensomformere og tavler som "
         "en del af den samme opgave som det mekaniske — ikke en separat leverandør."),
        ("Sikkerhed og procedurer",
         "LOTO, arbejdsprocedurer og risikovurdering under BEK 1608 og DS/HD 60364; APV og 5S som "
         "daglig praksis på et anlæg, hvor en fejl ikke måtte blive en ulykke."),
        ("Måling og kontrol",
         "Temperatur, vibration, tryk og smøring fulgt som en del af eftersynet; afvigelser noteret og "
         "lukket, ikke udskudt til næste stop."),
    ]:
        m.bullet(label, body, after=20)

    m.section("RESERVEDELE, SERVICEAFTALER OG STRUKTUR")
    for label, body in [
        ("Reservedele og indkøb",
         "Reservedelsflow og lagerstyring i SAP ERP; kritikalitet, leveringstider og koordinering med "
         "indkøb og underleverandører på 11 samtidige entrepriser."),
        ("Serviceaftaler og leverandører",
         "Aftaler med eksterne værksteder og leverandører fulgt på responstid og leverance; arbejde "
         "booket, dokumenteret og afregnet mod det, der var aftalt."),
        ("Struktur fra bunden",
         "Arbejdsgange, skabeloner og registrering bygget op i egen virksomhed siden 2023 — "
         "kompetencematrix, eftersynsplaner og opfølgning, der kan bruges af andre end mig."),
    ]:
        m.bullet(label, body, after=20)

    m.section("ERHVERVSERFARING")
    jobs = [
        ("Ejer / teknisk direktør",
         "ELOHVAC ApS · København · maj 2023–nu",
         "5 elektrikere + 3 lærlinge · fuldt P&L · service, produktion og mindre projekter",
         [("Service, køl og økonomi",
           "Service og reparation på køle-, ventilations- og elanlæg under eget P&L; planlægning, "
           "reservedele og dokumentation bygget op fra bunden.")]),
        ("Senior idriftsættelsesingeniør / projektleder, elsystem",
         "Novo Nordisk A/S · Kalundborg · nov. 2022–jul. 2024",
         "37 samtidige anlægsprojekter · 25 specialister · GMP/FDA/EMA",
         [("Idriftsættelse og dokumentation",
           "Anlæg sat i drift med FAT/SAT og IQ/OQ/PQ; afvigelser lukket med A3 og rodårsagsanalyse — "
           "nul kritiske fund.")]),
        ("Projekt- og værkstedsleder",
         "Ventek-Air · København · jan. 2022–nov. 2022",
         "14 medarbejdere · 11 samtidige entrepriser · DKK 2–10 mio.",
         [("Værksted og kapacitet",
           "14-mands værksted og 11 samtidige opgaver; daglige tavlemøder og ugentlig "
           "kapacitetstilpasning mod leveringsdatoen.")]),
        ("Vedligeholdelses- og driftsleder",
         "Lynetten under Biofos · København · aug. 2017–jan. 2022",
         "Kritisk renseanlæg i 24/7-drift · pumper, kompressorer, køl, HVAC, højspænding, SCADA",
         [("Forebyggende vedligehold og akut fejlfinding",
           "Eftersyn planlagt i produktionsvinduer; akut fejlfinding døgnet rundt, 5S og "
           "reservedelsflow, LOTO og APV.")]),
        ("Elektromekaniker / produktionsteamleder",
         "ARJ Engineering · Teheran · dec. 2003–mar. 2010",
         "12 mekanikere og teknikere · maskinværksted · industriel anlæg",
         [("Plan og output",
           "12 mand planlagt mod ugens plan med materialer og værktøj; output målt pr. medarbejder og "
           "pr. maskine.")]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=16)

    # ---------------------------------------------------------------- side 3
    m.page_break()
    m.section("UDDANNELSE OG AUTORISATION")
    m.edu("Elautoriseret maskinmester — dansk elautorisation LV/MV/HV",
          "Sikkerhedsstyrelsen · maj 2023")
    m.edu("B.Tech, teknologiledelse og maskinteknik (EQF 6)",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12")
    m.edu("El- og maskinteknisk design, elteknik (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("Køleteknik og klimaanlæg (AMU) · Lean: 5S, PDCA, VSM, A3, standard work",
          "Mercantec · 2021 · anvendt i vedligehold, kapacitet og opfølgning")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("**Dansk: modersmål** · **Engelsk: professionelt**, skriftligt og mundtligt, også i teknisk "
           "dokumentation og med leverandører · Persisk: modersmål · **Bosat i Måløv**, ca. 25 minutter "
           "til Lynge · Kørekort B og bil · Kan tiltræde snarest eller efter aftale · Referencer efter "
           "aftale.", after=70)

    m.models_table("DE FØRSTE 90 DAGE — UDSTYR, INTERVALLER OG STRUKTUR",
                   ("Periode", "Hvad der sker, og hvordan det måles"), [
        ("Uge 1–2",
         "Gå ruten med produktionen: blander, ekstruder, ovn, pumper, kompressorer og køl. Læs "
         "serviceaftaler og reservedelslister; notér hvert stop de sidste tre måneder med årsag."),
        ("Dag 30",
         "Ét udstyrsregister med kritikalitet, intervaller og ejer; de ti komponenter, der koster mest "
         "oppetid, markeret med leveringstid og lagerstatus. Serviceaftalerne lagt i kalender med "
         "responstid og kontaktperson."),
        ("Dag 60",
         "Eftersynsplanen kører i produktionens vinduer, og registreringen er ens for alle; "
         "reservedelsniveau aftalt med indkøb og engineering. Første måned med oppetid og "
         "gennemførte eftersyn dokumenteret."),
        ("Dag 90",
         "Måltal for oppetid, eftersyn til tiden og akutte stop pr. måned; oversigt over "
         "vedligeholdelsesomkostninger pr. udstyr, og en plan for det nye produktionsudstyr, der er på "
         "vej."),
    ], widths=(1500, 8830))

    m.section("EN OVN ER EN MASKINE MED TRE KILDER TIL STOP")
    m.para("Varmeelementer, følere og tætninger. Når ovnen står stille, er det næsten altid en af de "
           "tre, og spørgsmålet er, om man opdager det ved eftersyn eller ved et batch, der er tabt. "
           "Derfor vil jeg have temperatur, isolation og følere ind i den faste rute — og en aftale med "
           "leverandøren om, hvad der sker, når en føler skal skiftes på en søndag.", after=70)

    m.section("NYT UDSTYR SKAL IND, MENS DET GAMLE SKAL KØRE")
    m.para("Når kapaciteten udvides, bliver installationen en vedligeholdelsesopgave: hvornår kan "
           "linjen stå stille, hvilke forsyninger skal føres frem — el, vand, trykluft, afløb — og hvem "
           "skal have dokumentationen, før den første prøveproduktion. Jeg har koordineret installation "
           "og idriftsættelse af nyt udstyr i produktionsmiljøer, hvor driften ikke måtte stoppe, og "
           "ved at det arbejde tabes eller vindes i planlægningen — ikke i selve montagen.", after=70)

    m.section("ET STOP HER ER EN UDLEDNING ET ANDET STED")
    m.para("Cembranes membraner sidder i anlæg, hvor der bliver lavet drikkevand og renset spildevand. "
           "Når en ekstruder står stille i Lynge, er det ikke bare en ordre, der bliver sen — det er et "
           "anlæg til **vandrensning** et sted i verden, der venter på reservedele til en ibrugtagning. Jeg "
           "har arbejdet på den anden side af den kæde i mere end fire år, hvor vi rensede spildevand "
           "for en hel by, og **driftsikkerhed** var ikke et nøgletal, men en forudsætning. Den respekt "
           "for udstyret tager jeg med.", after=70)

    m.section("SIKKERHED ER EN RUTINE, IKKE EN PLAKAT")
    m.para("En ekstruder og en højtemperaturovn har energi i sig, også når den er slukket. Derfor skal "
           "isolering, aflåsning og frigivelse være en procedure, man kan følge i mørke: **LOTO**, "
           "arbejdsprocedure og risikovurdering under **BEK 1608**, og en kollega, der ved, at maskinen "
           "ikke kan starte. Jeg har stoppet arbejde på et 24/7-anlæg, da proceduren ikke var på plads, "
           "og det er billigere end den time, det kostede.", after=70)

    m.section("MÅLING SLÅR MENINGER")
    m.para("Vibration, temperatur, tryk og smøring kan måles, og når de kan måles, kan de følges — "
           "også før det bliver et stop. Det kræver en fast **kalibrering** af følere, at grænseværdier "
           "er skrevet ned, og at afvigelser bliver lukket i stedet for udskudt. Det er den samme "
           "disciplin, jeg har brugt på højspændingsanlæg og i GMP-miljøer, hvor en måling uden "
           "dokumentation ikke tæller.", after=70)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table("HVAD STILLINGEN KRÆVER — HVAD JEG HAR LEVERET",
                   ("Krav i opslaget", "Bevis"), [
        ("Daglig vedligeholdelse af pumper, motorer, kølesystemer og kompressorer",
         "24/7-drift af et af landets største renseanlæg: pumper, kompressorer, køle- og "
         "ventilationsanlæg, højspændingstavler og SCADA i mere end fire år."),
        ("Vedligehold af tungt udstyr som blander, ekstruder og højtemperaturovn",
         "Tungt procesudstyr og maskinværksted i 20+ år; eftersyn efter intervaller og tolerancer. "
         "SiC-ekstrudering og sintringsovn læres af jeres engineering og af driftstimerne."),
        ("Administration og opfølgning på serviceaftaler, fx kompressor og gaffeltruck",
         "Serviceaftaler og eksterne værksteder fulgt på responstid og leverance; arbejde booket, "
         "dokumenteret og afregnet mod det aftalte."),
        ("Korrekt registrering af vedligeholdelsesopgaver, så de er sporbare",
         "Registrering med udstyr, årsag, indsats og tid — samme disciplin, der gav nul kritiske fund "
         "i GMP-revisioner og dokumenteret afvigelseshåndtering med A3."),
        ("Support ved installation af nyt udstyr",
         "FAT/SAT og idriftsættelse af nye anlæg i 37 projekter: dokumentation, justering, "
         "reservedelslister og oplæring fanget før garantien løber ud."),
        ("Forebyggende vedligeholdelse, reparationer og renoveringer",
         "Eftersynsplaner lagt i produktionsvinduer og akut fejlfinding døgnet rundt; reparationer "
         "dokumenteret med årsag og efterfølgende tiltag."),
        ("Koordinering med engineering og indkøb om tilgængelige reservedele",
         "Reservedelsflow og lagerstyring i SAP ERP; materialer og underleverandører koordineret på 11 "
         "samtidige entrepriser."),
        ("Selvstændigt ansvar for at styre og føre tilsyn med alle vedligeholdelsesopgaver",
         "Vedligeholdelses- og driftsleder for et kritisk anlæg; i dag fuldt P&L-ansvar i egen "
         "virksomhed med 5 medarbejdere og 3 lærlinge."),
        ("Rettidig udførelse af vedligeholdelsesopgaver",
         "Eftersyn planlagt mod vinduer og driftstimer og fulgt på gennemførelse; arbejde, der "
         "overskred sin frist, blev eskaleret samme dag."),
        ("Høj oppetid på maskinerne",
         "Prioriteringsrækkefølge og contingens skrevet på forhånd; oppetid målt og fulgt, og nedbrud "
         "analyseret med rodårsag i stedet for gentagen reparation."),
        ("Styring af reservedele",
         "Kritikalitet, leveringstider og lagerbeholdning styret i SAP ERP; 5S på lager og værksted, "
         "så delen kan findes, når den skal bruges."),
        ("Korrekt administration af serviceaftaler",
         "Aftaler med leverandører og underentreprenører administreret i egen virksomhed: responstid, "
         "dokumentation og faktura mod aftalt indhold."),
        ("Praktisk orienteret og selvkørende, trives i produktionsmiljø med høj vækst og bidrager proaktivt til at opbygge struktur og rutiner",
         "Byggede vedligeholds-, ressource- og dokumentationssystem op fra bunden i egen virksomhed og "
         "drev et anlæg gennem vækst uden at lade rutinerne vente."),
        ("Solid forståelse for mekanik",
         "Elautoriseret maskinmester med maskinteknisk design (EQF 6) og 20+ år med pumper, "
         "kompressorer, køl, ventilation og tungt værkstedsudstyr."),
        ("Elektrisk fejlfinding er en bonus",
         "Fuld elautorisation LV/MV/HV og fejlfinding på motorer, styringer, frekvensomformere og "
         "tavler — samme opgave som det mekaniske, samme ansvar."),
        ("Uddannelsesmæssig baggrund er mindre vigtig end evnen til at tage ansvar og skabe orden",
         "20+ år med ansvar for drift, vedligehold og økonomi; orden er ikke en personlighed, men et "
         "register, en intervalplan og en registrering, andre kan læse."),
    ], widths=(3600, 6746))

    m.section("HVAD JEG VILLE SE PÅ FØRST")
    m.para("Hvilke ti komponenter der står bag flest timer i de sidste tre måneders stopsedler, hvordan "
           "reservedele bliver bestilt i dag, og hvem der rykker ud, når kompressoren stopper en "
           "søndag. De tre svar fortæller, om problemet er udstyr, lager eller aftaler — og de er også "
           "svaret på, hvor den første forbedring skal ligge.", after=80)

    m.section("OM AT VÆRE DEN, DER BLIVER RINGET OP")
    m.para("Beredskab er en aftale, ikke en holdning. Jeg har haft telefonen i mere end fire år på et "
           "anlæg, der ikke måtte stoppe, og jeg ved, at det, der afgør et akut stop, er om "
           "reservedelen ligger på hylden, om nummeret til leverandøren er det rigtige, og om den "
           "næste på holdet ved, hvad der er prøvet. Den slags skrives ned i fredstid.", after=80)

    m.section("EN FABRIK I VÆKST SKAL KUNNE ARVE SIN EGEN VIDEN")
    m.para("Når der bliver ansat flere og udstyret bliver mere avanceret, er den største risiko ikke, at "
           "nogen glemmer at smøre en leje — det er, at viden kun findes hos den, der tilfældigvis var "
           "på arbejde den dag. Derfor skal alt, hvad jeg laver, kunne læses af den næste: en "
           "vedligeholdelsesplan nogen kan følge, en registrering nogen kan søge i, og en reservedel "
           "nogen kan finde. Det var sådan, jeg byggede det i egen virksomhed, og det er den slags "
           "struktur, opslaget beder om.", after=80)

    return m.save(path, title="Maintenance Technician — Cembrane")


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Cembrane_MaintenanceTechnician.docx')
    build(out)
    print(out)
