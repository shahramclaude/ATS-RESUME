# -*- coding: utf-8 -*-
"""GreyBird Pilot Academy — Planlægning og produktion, Aarhus Lufthavn (Kolind).

Dansk opslag → dansk dokument (da-DK): ansøgning side 1, CV side 2, uddannelse + 90 dage +
fire afsnit side 3, kravmatrix side 4.

STILVALG (master/STILREGISTER.md, policy 04.11.2026; godkendt af scripts/style_guard.py,
3/3 skift mod #187):
  register       = MARITIM/OFFSHORE — regime, værvindue, besætning, sikkerhed. Registeret er
                   valgt, fordi luftfart deler de tre ting, der styrer planen: vejr, regler og
                   mennesker, der ikke kan arbejde i det uendelige. Sidst brugt #177 og derfor
                   ikke i nærheden af de seneste dokumenter.
  åbningsgreb    = D (TALLET) — de tolv fly, de tretten nye, de 40 instruktører, de 200
                   studerende og de syv baser, taget fra opslaget. Sidst brugt #173.
  struktur       = TESERNE — fem påstande om planlægning, bevist én for én, derefter S&OP,
                   systemer, flåde, baser og arbejdsform. Ny struktur for dette dokument.
  kadence        = kort påstand, derefter et konkret eksempel med tal — mere brief end brev.

Ingen opdigtede fakta: ingen erfaring fra luftfart, flyveskole eller flyvedligehold påstås.
Planlægningserfaringen er dokumenteret i drift, entreprise og produktion (37 samtidige projekter,
11 samtidige entrepriser, 24/7-anlæg, flåde af vare- og servicebiler gennem egen virksomhed).

Policy: master/README.md — jobbet først, kandidaten kun som bevis, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Planlægning og produktion · Kapacitet, systemer og daglig drift'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("8. november 2026")
    m.meta("GreyBird Pilot Academy · Planlægning og produktion · Aarhus Lufthavn, Kolind")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Planlægning og produktion — GreyBird Pilot Academy", bold=True, color='1A1A1A')
    m.para("Til COO Thomas Brams", after=70)

    # ---------------------------------------------------------------- side 1
    m.para("**Tolv fly i drift, tretten på vej, 40 instruktører, 200 studerende og syv baser fra Dublin til "
           "Helsinki.** Det er ikke en kalender, der skal fyldes — det er en kapacitet, der skal besluttes, "
           "og den beslutning træffes måneder før, den bliver en flyvetime. Fem ting styrer den beslutning, "
           "og dem holder jeg mig til her.", after=80)

    m.para("**1. En plan er en kapacitetsbeslutning, ikke et skema.** Et skema viser, hvad der er aftalt; en "
           "plan viser, hvad der kan lade sig gøre, og hvad det koster at gøre noget andet. Jeg har planlagt "
           "**37 samtidige projekter** med 25 specialister og **11 samtidige entrepriser** med 14 mand — ikke "
           "ved at fylde kalenderen, men ved at beslutte, hvad der ikke skulle ske i denne måned.", after=80)

    m.para("**2. Det, der ikke kan flyttes, skal planlægges først.** Vejrminima, luftdygtighed og "
           "vedligeholdelsesvinduer er faste punkter, som alt andet lægger sig omkring. Jeg har planlagt "
           "produktion efter vinduer, der ikke kunne rykkes: nedbrud, tilsyn, reservedele og de perioder, "
           "hvor anlægget ikke måtte stå stille. Rækkefølgen er altid den samme — de faste punkter ind først, "
           "resten bagefter.", after=80)

    m.para("**3. Reglerne er ikke en hindring; de er planens rammer.** **Flyve- og hviletidsregler**, "
           "**vejrminima** og krav til **vedligehold og luftdygtighed** er det, planen skal holde sig inden "
           "for — ikke noget, der kommer i vejen bagefter. Jeg har arbejdet under **BEK 1608**, "
           "**DS/HD 60364** og GMP/FDA/EMA-regler, hvor en procedure er en del af planen og ikke en "
           "overraskelse.", after=80)

    m.para("**4. Planen skal kunne tåle, at den ændres.** En aflysning er ikke et nederlag; et akademi uden "
           "en plan for aflysninger er. Jeg har drevet **24/7-drift** og akutte udkald i mere end fire år, "
           "hvor næste beslutning skulle være taget, før telefonen blev lagt på — og jeg ved, at contingencen "
           "skal skrives, mens ugen er rolig.", after=80)

    m.para("**5. Mennesker følger en plan, de har været med til at lave.** Instruktører, mekanikere og "
           "studerende er ikke ressourcer på en linje; de er tre grupper med hver deres krav til dagen. Jeg "
           "har ledet teams på **5, 12, 14 og 25** med tavlemøder, MUS og kompetencematrix og lært, at den "
           "plan, der bliver fulgt, er den, folk selv har været med til at lægge.", after=80)

    m.para("**S&OP — det bliver en rullende kapacitetsplan.** Mellem- og langsigtet planlægning handler om "
           "at kende flaskehalsen et halvt år før, den bliver et problem: instruktørkapacitet i "
           "højsæsonen, fly der er inde til **vedligehold**, simulatorer der er booket, og studerende, der "
           "skal videre til næste fase. Jeg har kørt månedshjul med rullende 12-måneders kapacitet, "
           "efterkalkulation og en fast beslutningsdag — og det er den samme disciplin, bare med fly på "
           "linjen.", after=80)

    m.para("**Systemer og data — planen skal kunne ses af 40 instruktører.** Et regneark, som kun "
           "planlæggeren forstår, er en flaskehals. Jeg har bygget rapportering i **SAP ERP**, **Power BI** "
           "og **Python**, med **KPI'er** for kapacitet, udnyttelse og **nedetid**, og målt **over 40 % "
           "produktivitetsløft** ved at flytte rutinearbejdet ind i systemet. Det er også sådan, planen "
           "bliver til at tale om på et møde.", after=80)

    m.para("**Flåden og vedligehold — planlagt som en del af produktionen.** Tolv fly i dag og tretten på vej "
           "betyder, at **vedligehold** er en kapacitetsbeslutning og ikke et værkstedsanliggende: hvilke "
           "fly kan tages ud i hvilke uger, hvad koster det i flyvetimer, og hvornår skal de **eksterne** "
           "kræfter bookes. Jeg har koordineret underentreprenører og leverandører på 11 samtidige "
           "entrepriser og ved, at en aftale, der ikke er booket i tid, bliver den dyreste i regnskabet.",
           after=80)

    m.para("**De syv baser — samme plan i syv tidszoner.** Fra Dublin til Helsinki skal **fly**, "
           "**simulatorer** og instruktører kunne flyttes, og studerende skal kunne rejse mellem baserne med "
           "**transport** og **indkvartering** aftalt, før de pakker. Jeg har styret drift på flere adresser "
           "samtidig og ved, at det kun holder, hvis den samme plan og den samme melding gælder alle steder.",
           after=80)

    m.para("**Aarhus Lufthavn, Kolind og arbejdsformen.** Jeg bor i Måløv, og jeg læser jeres "
           "fleksibilitet som en arbejdsform, ikke en undskyldning: jeg vil være på basen, når planen, "
           "instruktørerne og mekanikerne kræver det, og bruge de virtuelle dage på det, der egner sig til "
           "det. **Dansk** og **engelsk** — engelsk er arbejdssprog, og det taler jeg i møder, i "
           "dokumentation og på gulvet.", after=80)

    m.para("Jeg vil gerne høre, hvor flaskehalsen sidder lige nu — instruktører, fly eller simulatorer — "
           "hvordan masterplanerne bliver lavet i dag, og hvor langt frem planen rækker. Og jeg vil gerne "
           "måles på, at udnyttelsen stiger, uden at planen bliver sværere at følge for dem, der flyver.",
           after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Planlægnings- og produktionsleder med 20+ års erfaring i drift, produktion og entreprise — "
           "**elautoriseret maskinmester (LV/MV/HV)**, el- og maskinteknisk design (EQF 6), B.Tech og fuldt "
           "**P&L-ansvar siden 2023**. Har planlagt **37 samtidige projekter** med 25 specialister og **11 "
           "samtidige entrepriser** med 14 mand, kørt **månedshjul med rullende kapacitetsplan og "
           "efterkalkulation**, ledet teams på **5, 12, 14 og 25** og bygget rapportering i **SAP ERP**, "
           "**Power BI** og **Python** med **over 40 % produktivitetsløft**. Dansk og engelsk.", after=80)

    m.section("PLANLÆGNING OG KAPACITET")
    for label, body in [
        ("Ressource- og kapacitetsplanlægning",
         "37 samtidige projekter og 11 samtidige entrepriser planlagt mod samme kapacitet: hvad der kan "
         "leveres i måneden, og hvad der ikke kan — besluttet før kunden spurgte."),
        ("S&OP, månedshjul og opfølgning",
         "Rullende 12-måneders kapacitetsplan med fast beslutningsdag, efterkalkulation og opfølgning på "
         "udnyttelse, timeforbrug og nedetid i SAP ERP og Power BI."),
        ("Vedligehold og eksterne ressourcer",
         "Vedligeholdelsesvinduer planlagt som en del af produktionen; underentreprenører og leverandører "
         "booket på kapacitet og levering, ikke på telefonsvar."),
    ]:
        m.bullet(label, body, after=20)

    m.section("DRIFT, AFVIGELSER OG SYSTEMER")
    for label, body in [
        ("Daglig drift og omprioritering",
         "24/7-drift med akutte udkald i mere end fire år; dagen omplanlagt inden for timer uden at flytte "
         "aftaler, der ikke kunne flyttes."),
        ("Aflysninger og nedetid",
         "Contingency skrevet på forhånd: hvem rykker, hvilke opgaver går forrest, og hvad koster det — målt "
         "som nedetid og gennemført volumen, ikke som undskyldninger."),
        ("Data og planlægningsværktøjer",
         "SAP ERP som fælles datagrundlag, Power BI til KPI'er og Python til beregning og automatisering; "
         "planen gjort læsbar for dem, der skal følge den."),
    ]:
        m.bullet(label, body, after=20)

    m.section("LEDELSE OG SAMARBEJDE")
    for label, body in [
        ("Team og ledelse",
         "5, 12, 14 og 25 medarbejdere ledet med MUS/GRUS, 1:1, kompetencematrix og udviklingsplaner; "
         "struktur bygget fra bunden i egen virksomhed."),
        ("Mange faggrupper om én plan",
         "Fag, kunder, rådgivere, tilsyn og underentreprenører samlet om samme plan og samme melding; "
         "beslutninger skrevet ned med ejer og dato."),
    ]:
        m.bullet(label, body, after=20)

    m.section("ERHVERVSERFARING")
    jobs = [
        ("Ejer / teknisk direktør",
         "ELOHVAC ApS · København · maj 2023–nu",
         "5 elektrikere + 3 lærlinge · fuldt P&L · service, produktion og mindre projekter",
         [("Kapacitet, struktur og økonomi",
           "Alle opgaver planlagt og afleveret under eget P&L; daglig bemanding på skiftende adresser, "
           "arbejdsgange og skabeloner bygget fra bunden, kompetencematrix, MUS og tre lærlinge.")]),
        ("Senior idriftsættelsesingeniør / projektleder, elsystem",
         "Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024",
         "37 samtidige anlægsprojekter · 25 specialister · GMP/FDA/EMA",
         [("Ressourceplanlægning i komplekst miljø",
           "37 samtidige projekter af DKK 2–10 mio. planlagt mod fælles kapacitet og faste vinduer; møder "
           "med beslutningslog og månedlig rapportering i SAP ERP."),
          ("Afvigelser og aflevering",
           "Afvigelser håndteret med A3 og rodårsagsanalyse; afleveringspakke og mangellukning — nul "
           "kritiske fund.")]),
        ("Projekt- og værkstedsleder",
         "Ventek-Air · København · jan. 2022–nov. 2022",
         "14 medarbejdere · 11 samtidige entrepriser · DKK 2–10 mio.",
         [("Produktion og flaskehalse",
           "14-mands værksted og 11 samtidige opgaver; daglige tavlemøder, flaskehalsanalyse og "
           "kapacitetstilpasning uge for uge.")]),
        ("Vedligeholdelses- og driftsleder",
         "Lynetten under Biofos · København · aug. 2017–jan. 2022",
         "Kritisk anlæg i 24/7-drift · pumper, HVAC, højspændingstavler, SCADA",
         [("Vedligehold, vinduer og sikkerhed",
           "Forebyggende vedligehold planlagt i produktionsvinduer; akut fejlfinding døgnet rundt, 5S og "
           "reservedelsflow, LOTO og APV.")]),
        ("Elektromekaniker / produktionsteamleder",
         "ARJ Engineering · Teheran · dec. 2003–mar. 2010",
         "12 mekanikere og teknikere · maskinværksted · industriel anlæg",
         [("Plan og målstyring",
           "12 mand planlagt mod ugens plan med materialer og værktøj; output målt pr. medarbejder og pr. "
           "maskine.")]),
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
    m.edu("Lean: 5S, PDCA, VSM, A3, standard work · Køleteknik og klimaanlæg (AMU)",
          "Mercantec · 2021 · anvendt i kapacitetsstyring og opfølgning")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("**Dansk: modersmål** · **Engelsk: professionelt**, skriftligt og mundtligt, som arbejdssprog i "
           "møder og dokumentation · Persisk: modersmål · **Bosat i Måløv**, indstillet på at være til stede "
           "på basen i Kolind, når planen og teamet kræver det · Kørekort B og bil · Kan tiltræde snarest "
           "eller efter aftale · Referencer efter aftale.", after=70)

    m.models_table("DE FØRSTE 90 DAGE — KAPACITET, SYSTEM OG BASER",
                   ("Periode", "Hvad der sker, og hvordan det måles"), [
        ("Uge 1–2",
         "Læs masterplanerne, instruktør- og flykalenderen og de sidste tre måneders aflysninger; mød "
         "instruktører, mekanikere og baseledere; se, hvordan en uge faktisk bliver planlagt i dag."),
        ("Dag 30",
         "Ét billede af kapaciteten: fly, simulatorer og instruktørtimer pr. base pr. uge — med flaskehalsen "
         "markeret og de tre ting, der koster mest nedetid, noteret med ejer og dato."),
        ("Dag 60",
         "Rullende 12-måneders kapacitetsplan lagt frem for COO; fast ugentlig planlægningsrytme og en "
         "aflysningsprocedure, der kan følges af alle baser; vedligeholdelsesvinduer booket med de eksterne "
         "værksteder."),
        ("Dag 90",
         "Planlægningssystemet samlet i én kilde, som baselederne selv kan læse; KPI'er for udnyttelse, "
         "progression og nedetid live; første S&OP-møde afholdt med beslutninger, ikke med status."),
    ], widths=(1500, 8830))

    m.section("ET AKADEMI ER EN KAPACITETSKÆDE, IKKE EN KALENDER")
    m.para("En flyvetime kræver fire ting på samme tid: et fly, der er luftdygtigt, en instruktør, der har "
           "timer nok tilbage på vagten, en plads i luftrummet og en studerende, der er klar til næste trin. "
           "Mangler én af dem, er de tre andre bundet uden at producere. Derfor er planlægningens vigtigste "
           "tal ikke antallet af bookinger, men hvor stor en del af kapaciteten der faktisk blev brugt.",
           after=80)

    m.section("VEJRET PLANLÆGGER MED, UANSET HVAD DER STÅR I SKEMAET")
    m.para("I en branche, hvor vejrminima kan lukke en flyvedag, skal planen have luft i sig: en buffer pr. "
           "uge, en prioriteringsrækkefølge for hvem der flyttes først, og en aftale om, hvad der sker med de "
           "studerendes progression, når en dag falder væk. Jeg har planlagt produktion i anlæg, hvor vejr og "
           "nedbrud gjorde det samme — og løsningen er den samme: beslut rækkefølgen, før dagen kommer.",
           after=80)

    m.section("VEDLIGEHOLD ER EN DEL AF PLANEN, IKKE ET AFBRUD I DEN")
    m.para("Når flåden vokser fra tolv til femogtyve fly, bliver vedligeholdelsen den største enkeltpost i "
           "planlægningen: hvert fly skal have timer nok til næste eftersyn, og hvert eftersyn skal ligge i en "
           "uge, hvor flyet ikke er hårdt booket. Sker det omvendt — at værkstedet bliver planlagt efter "
           "bookingen — bliver flyet det dyreste element i produktionen.", after=80)

    m.section("SYV BASER ER SYV KULTURER MED ÉN PLAN")
    m.para("Fra Dublin til Helsinki bliver den samme plan læst af mennesker med forskellige vaner, "
           "sprogfærdigheder og lokale forhold. Det holder kun, hvis planen er skrevet i et sprog, alle kan "
           "følge, og hvis der er én, der ejer hver linje. Jeg har styret drift og projekter på flere adresser "
           "og lært, at forskellen mellem syv baser og syv virksomheder er en fælles plan og en fast rytme.",
           after=80)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table("HVAD STILLINGEN KRÆVER — HVAD JEG HAR LEVERET",
                   ("Krav i opslaget", "Bevis"), [
        ("Bygge den mellem- og langsigtede planlægning op, herunder S&OP",
         "Rullende 12-måneders kapacitetsplan med fast beslutningsdag og efterkalkulation; 37 samtidige "
         "projekter og 11 samtidige entrepriser planlagt mod samme kapacitet."),
        ("Udvikle planlægningsprocesser og systemer, så de kan bære væksten",
         "Arbejdsgange og skabeloner bygget fra bunden i egen virksomhed; rapportering gjort fælles i SAP "
         "ERP, Power BI og Python — over 40 % produktivitetsløft."),
        ("Sikre mest muligt ud af instruktører, fly og simulatorer på tværs af alle baser",
         "Kapacitetsstyring på tværs af adresser og fag: udnyttelse målt pr. uge, flaskehals identificeret "
         "før den blev et problem, og omprioritering besluttet på tavlemødet."),
        ("Planlægge og koordinere vedligehold af flyene med interne og eksterne ressourcer",
         "Vedligeholdelsesvinduer planlagt som en del af produktionen; underentreprenører og leverandører "
         "booket på kapacitet og levering på 11 samtidige entrepriser."),
        ("Planlægge, koordinere og booke flyve- og teoriundervisning på alle baser",
         "Daglig planlægning på tværs af adresser og hold: bemanding, materialer og tid sat i system, booket "
         "med en ejer pr. linje og fulgt op samme uge."),
        ("Følge de studerendes progression i forhold til masterplanerne og tilpasse skemaerne undervejs",
         "Progression fulgt pr. sag og pr. hold mod en masterplan: 37 projekter og 11 entrepriser fulgt på "
         "milepæl, med omplanlægning når forudsætningerne flyttede sig."),
        ("Håndtere aflysninger og ombookninger hurtigt, så driften kører videre uden unødig nedetid",
         "24/7-drift med akutte udkald i mere end fire år; prioriteringsrækkefølge og contingency skrevet på "
         "forhånd, så næste beslutning var taget, før telefonen blev lagt på."),
        ("Koordinere transport og indkvartering af elever, når de rejser mellem baserne",
         "Logistik på tværs af adresser og lande: materialer, værktøj og folk flyttet efter plan, med "
         "leverandører og underentreprenører koordineret mod samme uge."),
        ("Uddannet ingeniør, cand.merc eller tilsvarende stærk faglig baggrund med solid forretningssans",
         "El- og maskinteknisk design (EQF 6), B.Tech i teknologiledelse og maskinteknik og elautoriseret "
         "maskinmester (LV/MV/HV); fuldt P&L-ansvar siden 2023."),
        ("Dokumenterede resultater med ressourceplanlægning og kapacitetsstyring i komplekse miljøer, fx supply chain, logistik eller planlægning",
         "37 samtidige projekter (DKK 2–10 mio.) med 25 specialister og 11 samtidige entrepriser med 14 "
         "mand; materiale- og reservedelsflow, lager og leverandørstyring i SAP ERP."),
        ("Har ledet mennesker, eller er klar til at tage skridtet ind i en lederrolle",
         "20+ år med personaleledelse: 5, 12, 14 og 25 medarbejdere, lærlinge og svende, med MUS, "
         "kompetencematrix og udviklingsplaner."),
        ("Er bedst, når der skal skabes struktur fra bunden, og bevarer roen, når planen skal ændres med kort varsel",
         "Byggede virksomhedens planlægning, økonomiopfølgning og arbejdsgange op fra 2023; drev 24/7-anlæg "
         "og akutte udkald, hvor dagen blev lagt om inden for timer."),
        ("Kan samle mange forskellige faggrupper om en fælles plan",
         "Fag, kunder, rådgivere, tilsyn og underentreprenører samlet om én plan; dagligt tavlemøde med "
         "beslutninger, ejer og dato."),
        ("Mestrer IT- og planlægningsværktøjer og bruger data til at træffe beslutninger",
         "SAP ERP, Power BI og Python i daglig brug; KPI'er for kapacitet, udnyttelse og nedetid bygget og "
         "brugt som beslutningsgrundlag."),
        ("Taler og skriver flydende dansk og engelsk — engelsk er arbejdssprog på tværs af baserne",
         "Dansk modersmål; engelsk professionelt i møder, dokumentation og på plads, også hvor "
         "leverandører og samarbejdspartnere ikke taler dansk."),
    ], widths=(3600, 6746))

    m.section("EN PLAN, DER IKKE KAN FORKLARES, BLIVER IKKE FULGT")
    m.para("Instruktører og mekanikere arbejder efter en plan, de forstår. Derfor skal prioriteringen kunne "
           "siges højt på to linjer: hvad der flyttes først, hvorfor, og hvem der betaler for det. Det er den "
           "samme disciplin, jeg har brugt i drift og entreprise — og den er grunden til, at planen bliver "
           "fulgt, også i den uge hvor vejret ikke samarbejder.", after=80)

    m.section("AT VÆRE TÆT PÅ, NÅR DET GÆLDER")
    m.para("Planlægning kan laves meget virtuelt, men ikke alt: en plan bliver bedre af at se flyet, "
           "værkstedet og det skema, der hænger på væggen. Jeg bor i Måløv og vil bruge dagene på basen, når "
           "kapaciteten, vedligeholdelsen eller et hold skal vendes — og de øvrige dage på at holde planen "
           "levende på tværs af syv baser.", after=80)

    return m.save(path, title="Planlægning og produktion — GreyBird Pilot Academy")


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_GreyBird_PlanlaegningProduktion.docx')
    build(out)
    print(out)
