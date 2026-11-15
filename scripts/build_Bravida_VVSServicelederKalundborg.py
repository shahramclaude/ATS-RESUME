# -*- coding: utf-8 -*-
"""Bravida — Erfaren serviceleder til VVS i Kalundborg (reachmee rmjob=11867).

Dansk opslag → dansk dokument (da-DK): ansøgning side 1, CV side 2, uddannelse +
90 dage + fire afsnit side 3, kravmatrix side 4.
Vinkel: en serviceafdeling bygges af de første opgaver, hvor kunden ringer igen —
og af de montører, der har lyst til at blive.
Policy: master/README.md — jobbet først, kandidaten kun som bevis, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Serviceleder · VVS-service, forretningsudvikling og kalkulation'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4. november 2026")
    m.meta("Bravida Danmark A/S · VVS-service · Kalundborg")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Erfaren serviceleder til VVS i Kalundborg", bold=True, color='1A1A1A')
    m.para("Til Martin Nielsen, tlf. +45 2525 1936", after=70)

    # ---------------------------------------------------------------- side 1
    m.para("En serviceafdeling bliver ikke bygget af et organisationsdiagram. Den bliver bygget af de "
           "første halvtreds opgaver, hvor kunden ringer igen — fordi den, der tog telefonen, vidste hvad "
           "han talte om, fordi tilbuddet kunne betales, og fordi montøren stod på adressen på det aftalte "
           "tidspunkt. Og den bliver bygget af de montører, der har lyst til at blive. Det er den opgave, "
           "jeg søger i Kalundborg.", after=80)

    m.para("**Rækkefølgen er kunder, aftaler, teknikere — ikke omvendt.** En ny afdeling skal først vide, "
           "hvilke kunder i oplandet der har et vedvarende behov, og hvilke opgavetyper det giver; derefter "
           "sætte en **serviceaftale** op med en responstid, der kan holdes, og en pris, der kan betales; og "
           "til sidst sikre, at der er **montører nok med den rigtige autorisation** til at løse opgaven den "
           "dag, kunden ringer. Jeg har prøvet rækkefølgen før: I **ELOHVAC ApS** har jeg siden 2023 bygget "
           "en teknisk serviceforretning op fra første kunde til **5 elektrikere og 3 lærlinge**, med fuldt "
           "P&L, egne serviceaftaler og en kundekreds, der blev skabt ved at løse de små opgaver ordentligt "
           "og komme igen.", after=80)

    m.para("**Et tilbud er en beslutning, ikke en pris.** Det er her, serviceforretningen enten kan betale "
           "sig eller ikke: hvor mange timer der reelt er til rådighed, hvor besværlig adgangen er, hvad "
           "materialet koster, og hvem der betaler, når noget viser sig at være anderledes. Jeg har "
           "**kalkuleret og udarbejdet tilbud** på service, reparation og entreprise, fulgt dem op med "
           "**efterkalkulation** pr. opgave og fulgt **dækningsgraden** pr. kunde og pr. opgavetype — så "
           "næste tilbud blev bedre end det forrige, og så en kunde med akut arbejde ikke spiste "
           "overskuddet af de gode sager.", after=80)

    m.para("**Kommercielt blik er at se bygningen, ikke kataloget.** Mulighederne ligger i det, der allerede "
           "står i Kalundborg-oplandet: produktionsvirksomheder, forsyningsanlæg, ejendomsdrift og "
           "boligadministration med anlæg, der er ved at være slidte, og en driftschef der mangler en, "
           "han kan ringe til. Jeg har arbejdet med den slags kunder hele min karriere: finde behovet, "
           "beskrive aftalen, prissætte den og levere det, der står i den.", after=80)

    m.para("**Fagligt står jeg på el — og i teknikrummet er fagene fælles.** Jeg er **elautoriseret "
           "maskinmester (LV/MV/HV)**, har drevet **11 ventilationsentrepriser** med 14 mand i Ventek-Air, "
           "har **køleteknik og klimaanlæg** fra AMU og har i fem år holdt **HVAC**, pumper og tavler kørende "
           "på et 24/7-anlæg. Derfor ved jeg, hvad der sker, når en VVS-opgave bliver en el-opgave midt i "
           "den: styringen, føleren eller tavlen sidder i samme teknikrum, og kunden ringer "
           "én gang, ikke tre. Jeg skal ikke lære Kalundborg at kende på et kort; jeg bruger byen og "
           "fagene til at bygge en afdeling, der kan svare på kundernes spørgsmål.", after=80)

    m.para("**Kalundborg kender jeg indefra.** Fra 2022 til 2024 arbejdede jeg i **Novo Nordisk** med base "
           "i Kalundborg: store produktionsanlæg, hvor adgang, tilladelser og sikkerhedsinstrukser er en del "
           "af opgaven, og hvor arbejdet foregår på anlæg, der kører imens. Jeg har styret **37 "
           "kapitalprojekter** på 2–10 mio. kr. med kravspecifikation, kontrakt, fremdrift og økonomi — og "
           "**nul kritiske fund**. Jeg har pendlet Måløv–Kalundborg i to år, så rejsetiden er "
           "ikke et åbent spørgsmål, og jeg kender de vilkår, håndværkere og leverandører arbejder under.",
           after=80)

    m.para("**Montørerne er afdelingens produkt.** En ny afdeling bliver ikke god af, at lederen regner "
           "godt; den bliver god af, at den enkelte montør ved, hvad der forventes, har udstyr og autorisation "
           "i orden og bliver spurgt, før beslutningen er taget. Jeg har "
           "ledet **5, 12, 14 og 25 mand** med daglig planlægning, **MUS** og 1:1-samtaler, "
           "**kompetencematrix**, oplæring af **lærlinge** og faglig sparring på pladsen — og med en enkel "
           "holding til fejl: vi gennemgår dem uden navn, fordi vi skal bruge læringen.", after=70)

    m.para("**Økonomi, kvalitet og fremdrift følges op i måneden, ikke i december.** Afvigelser skal opdages, "
           "mens der stadig er tid til at gøre noget ved dem: dækningsgrad pr. opgave, budget mod faktisk "
           "forbrug, udestående fakturaer og timer pr. type arbejde — på et fast månedshjul og et tal, "
           "der kan forklares på et tavlemøde. Jeg har gjort det i SAP ERP og i egne **Power BI**- og "
           "**Python**-værktøjer, og det gav **over 40 % produktivitetsløft** i min egen drift.",
           after=80)

    m.para("**Fra første kundedialog til sidste faktura er det én sag.** Tilbud, ordrebekræftelse, "
           "planlægning af montøren, udførelse, afleveringsdokumentation, faktura og opfølgning — med et "
           "navn på hvert skridt. Det er ikke bureaukrati; det er det, der gør, at en ny afdeling kan "
           "vokse uden at tabe kvaliteten.", after=70)

    m.para("**Bravida er det rigtige sted at bygge den.** En koncern med 13.000 medarbejdere, heraf 3.000 i "
           "Danmark, 180+ byer, noteret på **Nasdaq Stockholm** og med en målsætning om at være "
           "**klimaneutral** i værdikæden i 2045 giver en ny afdeling noget, en mindre virksomhed ikke kan: "
           "**ét Bravida** at trække på, når opgaven kræver et andet fag. Jeg bor i Måløv, har "
           "kørekort og kan tiltræde hurtigt. Jeg vil gerne høre, hvor mange montører afdelingen har i dag, "
           "hvilke kunder den lever af, hvilken responstid I lover, og hvordan I måler dækningsgraden — så "
           "de første 90 dage starter fra tallene, ikke fra antagelser.", after=56)
    m.meta("Med venlig hilsen", after=8)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Teknisk serviceleder med 20+ års erfaring i el, ventilation og drift — **elautoriseret "
           "maskinmester (LV/MV/HV)** med fuldt P&L-ansvar siden 2023 og egen serviceforretning bygget op "
           "fra første kunde til **5 elektrikere + 3 lærlinge**. Har kalkuleret og prissat service, "
           "reparation og entreprise, fulgt **dækningsgrad** og efterkalkulation, og ledet teams på "
           "**5, 12, 14 og 25 mand** med **MUS**, **kompetencematrix** og oplæring af lærlinge. Kender "
           "**Kalundborg** fra to år i Novo Nordisk med 37 CAPEX-projekter og **nul kritiske fund**. Dansk "
           "og professionelt engelsk; bosat i Måløv; hurtig tiltrædelse.", after=80)

    m.section("SERVICE, KALKULATION OG KUNDER")
    for label, body in [
        ("Opbygning af serviceforretning",
         "Egen virksomhed grundlagt og drevet siden 2023: kundekreds skabt fra nul, serviceaftaler med "
         "responstid, prissætning og opfølgning — med fuldt ansvar for indtjening og likviditet."),
        ("Tilbud, kalkulation og efterkalkulation",
         "Tilbud på service, reparation og entreprise; timer, materiale, adgang og risiko prissat, og hver "
         "opgave fulgt op bagefter, så dækningsgraden pr. kunde og opgavetype var kendt."),
        ("Kunderelationer og salg",
         "Al kundekontakt selv: behov afdækket på adressen, aftalens indhold skrevet ned, opfølgning efter "
         "hver opgave; kunder, der kommer igen, er den eneste salgsmotor, der ikke skal betales for."),
        ("Teknisk bredde i teknikrummet",
         "El, tavler og styring (LV/MV/HV), ventilation fra 11 entrepriser med 14 mand, køleteknik og "
         "klimaanlæg (AMU), HVAC og pumper i 24/7-drift med SRO/SCADA."),
        ("Ledelse og vidensdeling",
         "Daglig planlægning, tavlemøder, MUS og 1:1, kompetencematrix og lærlingeoplæring; fejl gennemgået "
         "uden navn, så læringen bliver i afdelingen."),
        ("Økonomi, kvalitet og fremdrift",
         "Månedshjul med dækningsgrad, budgetmod faktisk, udestående og timer pr. opgavetype; KS og "
         "afleveringsdokumentation med nul kritiske afvigelser i serviceaftalerne."),
    ]:
        m.bullet(label, body, after=25)

    m.section("ERHVERVSERFARING")
    jobs = [
        ("Ejer / teknisk direktør",
         "ELOHVAC ApS · København · maj 2023–nu",
         "5 elektrikere + 3 lærlinge · fuldt P&L · service, kalkulation og kunder",
         [("Forretning, kunder og tilbud",
           "Serviceforretning bygget op fra første kunde: behov afdækket, tilbud kalkuleret og sendt, "
           "serviceaftaler indgået, kunder fulgt op; SAP ERP og egne Power BI-værktøjer til timer, "
           "dækningsgrad og udestående."),
          ("Montører, kvalitet og sikkerhed",
           "Daglig ledelse af fem elektrikere og tre lærlinge, oplæring efter kompetencematrix, APV, LOTO "
           "og risikovurdering ved opstart; nul kritiske afvigelser i serviceaftalerne.")]),
        ("Senior idriftsættelsesingeniør / projektleder, elsystem",
         "Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024",
         "37 kapitalprojekter · 25 specialister · GMP/FDA/EMA · arbejde på kørende anlæg",
         [("Projekter, økonomi og fremdrift",
           "37 samtidige CAPEX-projekter på 2–10 mio. kr. med kravspecifikation, kontrakt, fremdrift, "
           "økonomi og månedlig rapportering til ledelse og bygherre."),
          ("Adgang, tilladelser og aflevering",
           "Arbejde på anlæg i drift med adgangsprocedurer, arbejdstilladelser og dokumentationskrav; "
           "FAT/SAT og IQ/OQ/PQ med nul kritiske fund ved aflevering.")]),
        ("Projekt- og værkstedsleder",
         "Ventek-Air · København · jan. 2022–nov. 2022",
         "14 medarbejdere · 11 ventilationsentrepriser · DKK 2–10 mio.",
         [("Ventilation, kapacitet og levering",
           "11 samtidige ventilationsentrepriser fra specifikation til aflevering med 14 mand; "
           "kapacitetsstyring, materialer, underentreprenører og daglige tavlemøder.")]),
        ("Vedligeholdelses- og driftsleder",
         "Lynetten under Biofos · København · aug. 2017–jan. 2022",
         "Kritisk 24/7-anlæg · HVAC, pumper, højspændingstavler, SRO/SCADA",
         [("Drift, service og reservedele",
           "Forebyggende vedligehold og akut fejlfinding på HVAC, pumper og tavler; reservedelsflow og "
           "lagerstyring, 5S og standard work på værksted og lager."),
          ("Sikkerhed og arbejdsmiljø",
           "LOTO, APV, sikkerhedsrunderinger, nærved-hændelser og toolbox-møder i et anlæg, der ikke "
           "kunne stoppes.")]),
        ("Elektromekaniker / produktionsteamleder",
         "ARJ Engineering · Teheran · dec. 2003–mar. 2010",
         "12 mekanikere og teknikere · maskinværksted · industrianlæg",
         [("Team, materialer og målopfyldelse",
           "Daglig fordeling af arbejde til 12 teknikere med materialer og værktøj styret mod ugens plan og "
           "målopfølgning pr. medarbejder.")]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.page_break()
    m.section("UDDANNELSE OG AUTORISATION")
    m.edu("B.Tech, teknologiledelse og maskinteknik",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12")
    m.edu("El- og maskinteknisk design, elteknik (EQF6)", "Tehran Technical University · 2000–2003")
    m.edu("Dansk elautorisation LV/MV/HV — elautoriseret maskinmester",
          "Sikkerhedsstyrelsen · maj 2023")
    m.edu("Køleteknik og klimaanlæg (AMU) · Lean: 5S, PDCA, A3, standard work",
          "Mercantec · 2021 · anvendt i drift og værksted")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("Dansk: modersmål, flydende i skrift og tale · Engelsk: professionelt · Persisk: modersmål · "
           "**Bosat i Måløv** med to års pendling til Kalundborg fra Novo-tiden · Kørekort B og egen bil · "
           "Kan tiltræde hurtigt · Referencer efter aftale.", after=70)

    m.models_table("DE FØRSTE 90 DAGE — KUNDER, MONTØRER OG MARGIN",
                   ("Periode", "Hvad der sker, og hvordan det måles"), [
        ("Uge 1–2",
         "Gennemgå den nuværende ordrebog, serviceaftaler og kundeliste med afdelingen; ud på de fem "
         "største kunder med en montør; lær jeres kalkulationsgrundlag, systemer og responstider at kende — "
         "og find ud af, hvilke opgaver I siger nej til i dag, og hvorfor."),
        ("Dag 30",
         "Én side pr. igangværende serviceaftale med økonomi, responstid og næste handling; kundebesøg "
         "planlagt for de næste 60 dage; kapacitet, autorisationer og ressourcer lagt op på én tavle, så alle kan se, "
         "hvem der kan løse hvad."),
        ("Dag 60",
         "Tilbudsprocessen strammet: fælles skabelon, kalkulationsark og efterkalkulation på de sidste ti "
         "opgaver; de første nye kunder tilbudt en aftale; montørerne inddraget i, hvordan arbejdsgangene "
         "skal se ud, før de bliver besluttet."),
        ("Dag 90",
         "Dækningsgrad pr. kunde og opgavetype kendt og rapporteret månedligt; responstid målt mod det "
         "lovede; kompetencematrix opdateret med autorisationer og udløbsdatoer; og en skriftlig plan for, "
         "hvilke kunder og opgavetyper afdelingen skal vokse på det næste år.")])

    m.section("EN NY AFDELING SKAL IKKE SIGE JA TIL ALT")
    m.para("Det sværeste ved at bygge en serviceafdeling op er ikke at få opgaver ind; det er at sige nej til "
           "de opgaver, der ødelægger kapaciteten for de kunder, der betaler for aftalen. En akut opgave, som "
           "man ikke kan løse ordentligt, koster mere end den giver — i genkøb, i omdømme og i montørernes "
           "lyst til at tage telefonen næste gang. Derfor vil jeg tidligt have styr på, hvilke opgavetyper "
           "afdelingen er god til, hvilke der skal løses med en partner, og hvad responstiden reelt er.",
           after=80)

    m.section("TILBUDDET SKAL KUNNE FORSVARES OM ET ÅR")
    m.para("Et tilbud, der er vundet på en pris, der ikke kan bære arbejdet, bliver ikke et kundeforhold; det "
           "bliver en diskussion om tillæg, kvalitet og hvem der havde ret. Jeg regner med timer, materiale "
           "og adgang på den måde, montøren faktisk møder opgaven, lægger risikoen ind hvor den hører, og "
           "skriver det ned i tilbuddet — ikke som forbehold, men som en del af den pris, kunden sammenligner "
           "med. Bagefter holder jeg opgaven op mod kalkulationen, fordi det er den eneste måde, næste "
           "tilbud bliver skarpere.", after=80)

    m.section("KUNDEN KØBER IKKE EN MONTØR — KUNDEN KØBER EN, DER KOMMER IGEN")
    m.para("I service er produktet ikke røret, der blev skiftet. Det er, at nogen tog telefonen, at der blev "
           "sagt hvornår, at det holdt, hvad der blev lovet, og at der blev ryddet op bagefter. Kunder i Kalundborg-oplandet har "
           "typisk prøvet tre leverandører, før de ringer til os; det, der gør forskellen, er ikke at være "
           "billigst, men at være den, der kan planlægge, dokumentere og svare, når anlægget står stille. "
           "Derfor er den første samtale med en ny kunde en kortlægning af anlægget, ikke et salg af en "
           "aftale.", after=80)

    m.section("MONTØRERNE SKAL KUNNE SE, HVOR DE ER PÅ VEJ HEN")
    m.para("En ny afdeling er et dårligt sted at være, hvis ingen ved, hvad der bliver af den. Derfor skal "
           "kompetencematrix, oplæring og samtalerne hænge sammen med de opgaver, afdelingen tager ind: "
           "hvem kan få en autorisation, hvem skal oplæres i køleanlæg, hvem kan blive den, der tager de "
           "svære fejlsøgninger. I min egen virksomhed har den sammenhæng været det, der gjorde, at "
           "lærlinge blev svende, og at folk blev, selv når ugen var svær.", after=80)

    m.page_break()

    m.models_table("HVAD STILLINGEN KRÆVER — HVAD JEG HAR LEVERET", ("Krav i opslaget", "Bevis"), [
        ('Bygge og udvikle VVS-serviceafdelingen i Kalundborg',
         'Bygget teknisk serviceforretning op fra nul siden 2023: 5 elektrikere + 3 lærlinge, egne serviceaftaler og egen kundekreds.'),
        ('Opsøge muligheder hos eksisterende og nye kunder og udvikle forretningen',
         'Al kundekontakt og alt salg selv: behov afdækket på adressen, aftaler indgået og kunder fulgt op — ingen leadmotor bag sig.'),
        ('Lede og koordinere serviceopgaver og mindre projekter',
         'Daglig ledelse af service og anlæg: 11 ventilationsentrepriser med 14 mand, 37 CAPEX-projekter med 25 specialister.'),
        ('Beregne, udarbejde og følge op på tilbud',
         'Kalkulation og tilbudsberegning i egen virksomhed med efterkalkulation pr. opgave og dækningsgrad pr. kunde og opgavetype.'),
        ('Planlægge og prioritere opgaver og sikre effektiv anvendelse af ressourcerne',
         'Kapacitetsstyring mellem akutte udkald og planlagt arbejde; daglige tavlemøder, flaskehalsanalyse og prioritering på pladsen.'),
        ('Opbygge stærke og langvarige relationer til kunder og samarbejdspartnere',
         'Kunderelationer bygget over år med serviceaftaler, faste kontaktpersoner og opfølgning efter hver eneste opgave.'),
        ('Samarbejde tæt med montører og kolleger og dele viden',
         'Faglig sparring på pladsen, fejl gennemgået uden navn, lærlinge oplært efter kompetencematrix; MUS og 1:1 med alle.'),
        ('Følge op på økonomi, kvalitet og fremdrift',
         'Månedlig opfølgning på dækningsgrad, budget mod faktisk og udestående; KS med nul kritiske afvigelser i serviceaftalerne.'),
        ('VVS-teknisk uddannelse og solid erfaring fra branchen',
         'Elautoriseret maskinmester (LV/MV/HV), køleteknik og klimaanlæg (AMU), 11 ventilationsentrepriser og 20+ år i teknisk service.'),
        ('Erfaring med VVS-service og gerne koordinering eller ledelse',
         'Teknisk service i 20+ år: HVAC, pumper og tavler i 24/7-drift; ledelse af 5, 12, 14 og 25 mand — montører og teknikere.'),
        ('Motiveres af at udvikle og bygge en afdeling og forretning op',
         'Har bygget en forretning op fra første kunde til fem svende og tre lærlinge, og rejst den igen efter tilbagegang.'),
        ('Erfaring med beregning og udarbejdelse af tilbud',
         'Tilbud på service, reparation og entreprise med AB 18 og totalentreprise; prissat med underentreprenører og materialer.'),
        ('Kommercielt blik og kan se muligheder hos både eksisterende og nye kunder',
         'Ser behovet ud fra bygningen og anlægget, ikke kataloget: hvad der er slidt, hvad aftalen skal dække, hvad den kan koste.'),
        ('Stærk i kommunikationen med kunder, samarbejdspartnere og kolleger',
         'Dansk og engelsk i møder, tilbud og dokumentation; taler med både teknikere, indkøbere og driftschefer.'),
        ('Kan lide mennesker og er god til at skabe relationer og få andre med dig',
         'Relationsarbejde i praksis med kunder, leverandører og egne folk — og en leder, der er på pladsen frem for på kontoret.'),
        ('Arbejder struktureret og tager ansvar fra første kundedialog til opgaven er afsluttet',
         'Én sag fra telefon til faktura: tilbud, ordre, plan, udførelse, aflevering og opfølgning — med et navn på hvert skridt.'),
    ], widths=(3600, 7046))

    m.section("SERVICEAFTALEN SKAL SÆLGE VEDLIGEHOLD, IKKE KUN REPARATIONER")
    m.para("En afdeling, der kun lever af det, der er gået i stykker, er altid bagud: arbejdet kommer, når "
           "det er dyrest for kunden, og kapaciteten svinger med tilfældighederne. Den anden halvdel af "
           "forretningen er den planlagte: en anlægsliste pr. kunde, faste intervaller for eftersyn, filtre, "
           "pumper og styringer, og en rapport efter hvert besøg, som kunden kan lægge i sin "
           "driftsdokumentation. Jeg har arbejdet med forebyggende vedligehold på et 24/7-anlæg og med "
           "**PDCA** og **5S** på værksted og lager, og jeg har set, hvad det giver: **over 40 % lavere "
           "energiforbrug** på de anlæg, hvor nogen fulgte op på tallene i stedet for at vente på nedbruddet.",
           after=80)

    m.section("KALUNDBORG ER IKKE ET OPLAND — DET ER EN BY MED STORE ANLÆG")
    m.para("I Kalundborg er afstanden mellem kunde og håndværker kort, og den, der har sagt ja til opgaven, "
           "møder den også, når den skal afleveres. Det stiller to krav til en ny serviceafdeling: at den kan "
           "sige nej i tide, og at den kender de anlæg, den tilbyder at servicere. Jeg har arbejdet to år på "
           "den største bygherre i byen og boet i pendlerafstand siden — det er ikke et lokalnetværk, jeg kan "
           "påstå, men det er et sted, jeg ved, hvordan man arbejder, og hvad der bliver lagt mærke til.",
           after=80)

    return m.save(path, title="Serviceleder VVS — Bravida Kalundborg",
                  subject="VVS-service, kalkulation og opbygning af afdeling",
                  keywords="serviceleder, vvs-service, serviceaftale, tilbud, kalkulation, daekningsgrad, "
                           "ventilation, koleteknik, ledelse, kalundborg, bravida")


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Bravida_VVSServicelederKalundborg.docx')))
