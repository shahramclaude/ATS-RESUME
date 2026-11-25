# -*- coding: utf-8 -*-
"""Radiometer Medical ApS, Brønshøj: Produktionsleder (Value Stream Manager),
Solution Pack-afdelingen (dansk opslag, brugertekst 25.11.2026).

Dansk opslag -> dansk dokument. Form (master/FORMKATALOG.md): åbning **C**
(Stedet: beslutningen tages ved tavlen på gulvet kl. 06.00), struktur **Ugen**
(ugerytmen som ledelsessystem, seks faste punkter), register **Værdistrømmen**
(flow, takt, standard work, changeover, spild, gennemløb).

Kulturfil: jd/Radiometer_ProduktionslederSolutionPack_kultur.txt.
Første ansøgning til Radiometer. Kontakt: Senior Manager Anne Wichmann,
anne.wichmann@radiometer.dk; 1. samtaler i uge 48.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Produktionsleder (Value Stream Manager) · LEAN, standard work og daglig driftsstyring'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, 'Produktionsleder (Value Stream Manager) · Solution Pack, Brønshøj',
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo')
    m.meta('25. november 2026')
    m.meta('Radiometer Medical ApS · Brønshøj · Produktionsleder (Value Stream Manager), '
           'Solution Pack-afdelingen')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Produktionsleder (Value Stream Manager), Solution Pack-afdelingen',
           bold=True, color='1A1A1A')
    m.para('Kære Anne Wichmann,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ---------------------------------------------------------------- side 1
    lp('**Kl. 06.00 står skiftet ved tavlen i Solution Pack.** Det er dér, ugens produktion '
       'bliver afgjort: hvad der skal flyde i dag, hvor der er risiko for, at noget stopper, og '
       'hvad aftenholdet skal have med. Resten af ugen følger af det kvarter. I opslaget kalder I '
       'det "Dagligt engagement ved at interagere med alle operatører på gulvet og afholde daglige '
       'produktionsmøder for at sikre produktkvalitet og optimere produktionsoutputtet løbende", '
       'og rollen er præcis beskrevet: et produktionsområde (en value stream) '
       'med ca. 25 operatører og teknikere på dag- og aftenhold og 2 PTA-ingeniører, der skal '
       'levere effektiv produktion, høj kvalitet og rettidig levering, også når efterspørgslen '
       'stiger.', after=44)

    lp('**Ugen som ledelsessystem.** Seks faste punkter, hvert med sin ejer. Mandag planen: '
       'kapaciteten fordelt på to hold, så planlægningsteamet kender ugen, før den starter. '
       'Tirsdag flowet: jeg går værdistrømmen igennem på gulvet og ser, hvor arbejdet venter i '
       'stedet for at flyde. Onsdag standard work: gennemgået med de operatører, der kører den, '
       'for en standard, ingen kan udføre, er ikke en standard. Torsdag changeover: SMED på den '
       'omstilling, der tager længst tid, så produktionseffektiviteten ikke tabes mellem '
       'ordrerne. Fredag '
       'tallene: produktionsoutput, kvalitet og levering gennemgået med ledergruppen, så '
       'beslutninger træffes på tal og ikke på mavefornemmelse. Hver dag sikkerheden: et sundt '
       'og sikkert arbejdsmiljø er ikke en kampagne, men den måde holdet møder ind på.',
       after=44)

    lp('Tværs gennem ugen ligger samarbejdet med det tekniske supportteam, planlægningsteamet og '
       'ledergruppen, og med kollegerne i Polen, som I selv skriver, at samarbejdet skal bære. '
       'Grænseflader på tværs af to organisationer har jeg styret før: ELOHVAC og Data Power '
       'kørte sideløbende med én samlet plan og skriftlige aftaler om, hvad der går forud. '
       'Samme faste punkter gælder, når aftenholdet i Brønshøj skal have samme standard som '
       'dagholdet.', after=44)

    lp('**De første 90 dage, som plan og ikke som løfte.** De første 30 dage bruger jeg på gulvet '
       'på begge hold: standard work og changeover-tider kortlagt, som de er i dag, og intet '
       'ændret før grundlaget ligger der. Dag 31 til 60: standard work revideret sammen med '
       'operatørerne, SMED på den største omstilling, og tavlen udvidet, så aftenholdet arbejder '
       'efter samme tal som dagholdet. Dag 61 til 90: de første Kaizen-forløb sat ind på de '
       'største tab fra kortlægningen, og en 90-dages gennemgang med ledergruppen af '
       'vækstmålene og den kapacitet, værdistrømmen skal levere.', after=44)

    lp('**Hvorfor Radiometer.** En medicoteknisk virksomhed, der siden 1954 har fremstillet det '
       'medicinske udstyr, som hjælper læger med at stille hurtige og præcise diagnoser for '
       'kritisk syge patienter, og missionen står i opslaget: "Bring more to life". '
       'Danaher slutter opslaget med "Join our winning team today. Together, we\'ll accelerate '
       'the real-life impact of tomorrow\'s science and technology" og "bring the power of science '
       'to life", og hverdagen følger "life comes first".', after=44)

    lp('Det tekniske sprog er Danaher Business System og LEAN, og de fire prioriteter er quality, '
       'delivery, cost and innovation. Kulturen står der også på: "Best team wins", "better '
       'together", videndeling og faglig respekt, frihed under ansvar og plads til at gøre en '
       'forskel. Det er en kultur, jeg kender fra GMP-produktion hos Novo Nordisk og fra '
       '24/7-drift hos Biofos, hvor LEAN-værktøjerne var det, der holdt et skiftehold på sporet.',
       after=44)

    lp('Opslaget beder om en videregående teknisk uddannelse og erfaring med produktionsledelse, '
       'og om den balance mellem at stille krav og sætte forventninger, der hører med en imødekommende '
       'adfærd og lyttende væsen. Den balance har været mit arbejde siden 2003: fra 12 mekanikere '
       'og teknikere i et maskinværksted til 25 højt specialiserede medarbejdere i GMP-drift. '
       'Når en investering i udstyr eller en ændret omstilling skal begrundes, lægger jeg '
       'investeringsmodeller med NPV, følsomhed og scenarier bag forslaget, og bruger Python og '
       'Claude Code til at samle tallene, før beslutningen tages.', after=44)

    lp('Jeg bor i Måløv med kort vej til Brønshøj og kan tiltræde efter aftale. CV og '
       'uddannelsespapirer er vedlagt, og jeg er klar til en samtale med det samme, også i uge 48, '
       'som I lægger op til. Jeg ser frem til at gennemgå de første 90 dage og værdistrømmens mål '
       'med Anne Wichmann. Ring på +45 93 99 95 14, eller skriv til ajlooshahram@gmail.com.',
       after=16)

    m.meta('Med venlig hilsen', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Produktionsleder med driftsansvar og forbedringsfokus i ét: værdistrømme med operatører '
           'og teknikere på skift og PTA-ingeniører i samme flow, styret gennem daglige tavlemøder, '
           'standard work og mål, der kan aflæses. Elautoriseret maskinmester og B.Tech i '
           'teknologiledelse og maskinteknik, siden 2003 med produktion, skiftehold og tværfaglig '
           'ledelse, og LEAN som hverdagens værktøjskasse frem for som et skema.', after=64)

    m.section('VÆRDISTRØMMEN: SÅDAN LÆSER JEG ET PRODUKTIONSOMRÅDE')
    for label, body in [
        ('Flowet',
         'En værdistrøm måles på, hvad der når frem. Mit første spørgsmål på gulvet er, hvor '
         'arbejdet venter, og hvorfor.'),
        ('Takten',
         'Når efterspørgslen stiger, er svaret sjældent flere timer. Svaret er kortere '
         'gennemløbstid og en takt, begge hold kan holde.'),
        ('Standard work',
         'Standarden skrives sammen med dem, der udfører den, og vedligeholdes, når arbejdet '
         'ændrer sig. Ellers findes den kun i mappen.'),
        ('Changeover',
         'Omstillingstiden er spild, ingen fakturerer. SMED på de store omstillinger er den '
         'hurtigste kapacitet, en value stream kan få.'),
        ('Kvaliteten',
         'En fejl fanget ved tavlen koster en beslutning. En fejl fanget ved levering koster et '
         'batch, en forklaring og måske en kunde.'),
        ('Sikkerheden',
         'Et sundt og sikkert arbejdsmiljø er den første linje på tavlen hver dag, ikke den '
         'sidste note i rapporten.'),
    ]:
        m.bullet(label, body, after=16)

    m.section('ERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester (ansvarlig for el-teknik og ventilation)',
         'Data Power Consultant ApS · København · 2024 – nu',
         'AI-afdeling 4-10 personer · el-teknik og ventilation · fuldt P&L · 5 elektrikere + 3 lærlinge',
         [('Drift og personale i to organisationer',
           'Matrixledelse med ELOHVAC og Data Power sideløbende: én samlet plan og skriftlige '
           'aftaler om prioriteter. Daglig planlægning, 1:1 og MUS, struktureret oplæring og '
           'arbejdsmiljøopfølgning for 5 elektrikere og 3 lærlinge.'),
          ('AI og investeringsmodeller i ledelsesarbejdet',
           'Python og Claude API til KPI-dashboards, rapportering og beregninger; investeringsmodeller '
           'med NPV, følsomhed og scenarier bag nye tiltag, udarbejdet som beslutningsoplæg og '
           'valideret med faglig kontrol, før noget gik videre.')]),
        ('Ejer / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 – nov. 2026 (virksomheden lukket)',
         'Erhvervskunder · el, ventilation og klima · entreprise · fuldt P&L',
         [('Kvalitet og sikkerhed i driften',
           'Installation, tavler, styring, fejlfinding og forebyggende vedligehold; LOTO, APV og '
           'risikovurdering ved opstart. Nul kritiske afvigelser i serviceaftalerne.'),
          ('Akkord og opmåling',
           'Akkordbreve, opmåling af udført arbejde, tildeling til sjak og regulering af mer- og '
           'mindrearbejde, altid opgjort sammen med den, der udførte arbejdet.'),
          ('Værktøjer der gav tid',
           'Python og Claude API i tilbudsberegning, tidsplaner, KS-tjeklister og KPI-dashboards; '
           'dokumenteret produktivitetsløft over 40 %.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, DKK 2–10 mio. · 25 specialister · GMP/FDA/EMA',
         [('Kvalitet og aflevering i GMP-drift',
           'FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA på 37 anlægs- og CAPEX-projekter, DKK 2–10 mio. '
           'pr. stk. Nul kritiske afvigelser ved aflevering, dokumentation skrevet mens arbejdet '
           'blev udført.'),
          ('Planlægning på tværs af linjer',
           'Tværfaglig ledelse af 25 højt specialiserede medarbejdere; fremdrift, økonomi og '
           'ressourcer på tværs af engineering, indkøb og anlæg, månedsrapportering til ledelse '
           'og bygherre.'),
          ('Forbedring med PDCA',
           '40 % reduktion af energiomkostninger via PDCA-program; A3, 5xHvorfor og Ishikawa ved '
           'fejlfinding på el-tekniske anlæg, SAP ERP til økonomi og omkostninger.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022 – nov. 2022',
         '11 samtidige anlæg · 14-mands team · DKK 2–10 mio.',
         [('Daglig drift på tavlen',
           'Kapacitets- og fremdriftsstyring for 11 samtidige anlægsprojekter og et 14-mands team. '
           'Daglige tavlemøder og flaskehalsanalyser; standardiserede arbejdsgange med markant '
           'løft i leveringsevnen.'),
          ('Planlægning og levering',
           'Udbud og tilbud, underentreprenører, aftalegrundlag og afleveringspakker; '
           'materialestyring i værkstedet, så holdene ikke skulle stå og vente på en komponent.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · SCADA, PLC, højspændingstavler · skiftehold',
         [('Oppetid, sikkerhed og skiftehold',
           'Kritisk el- og mekanisk drift: pumper, HVAC, højspændingstavler og SCADA med oppetid, '
           'forebyggende vedligehold og akut fejlfinding døgnet rundt. Skifteholdsdrift med '
           'sikkerhedsdisciplin: LOTO, risikovurdering, APV og nærved-hændelser.'),
          ('Standard work på værksted og lager',
           '5S, Standard Work og PDCA indført på værksted og lager; reservedelsflow og lagerstyring '
           'som del af den forebyggende indsats, så en defekt komponent ikke skulle blive til et '
           'døgn med nedsat kapacitet.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('Produktionsteam og målstyring',
           'Ledelse af 12 mekanikere og teknikere i maskinværkstedet: vagtplanlægning, '
           'materialestyring og målstyring. Fejldiagnose og reparation af industrielle el- og '
           'mekaniske anlæg, rodårsagsanalyse og korrigerende handlinger.'),
          ('Produkt og portefølje',
           'Produktlinje med elektromotorer, pumper og dykpumper: roadmap, forretningscases, '
           'udvikling og lancering samt pris-, margin- og investeringsbeslutninger på tværs af '
           'produktets livscyklus.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=16)

    m.section('UDDANNELSE OG CERTIFICERINGER')
    m.edu('B.Tech (EQF6), teknologiledelse og maskinteknik',
          'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12')
    m.edu('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('El- og maskinteknisk design, elteknik (EQF6)', 'Tehran Technical University · 2000–2003')
    m.edu('PRINCE2, certificeret projektleder', 'AXELOS / PeopleCert')
    m.edu('Køleteknik og klimaanlæg (AMU)', 'Mercantec · 2021 · STCW 2021–2023, Søfartsstyrelsen')
    m.para('Lean og Six Sigma som praksis, ikke certificering: DMAIC, 5S, PDCA, VSM (Value Stream '
           'Mapping), A3, Kaizen, Standard Work, SMED, TPM, 5xHvorfor, Ishikawa og FMEA, alle '
           'brugt i dokumenterede opgaver med vedligehold, kvalitet og planlægning.', after=48)

    m.section('SPROG, IT OG PRAKTIK')
    m.para('Dansk (førstesprog) · engelsk (arbejdssprog) · persisk (modersmål). IT og daglige '
           'værktøjer: SAP ERP, CMMS, Power BI, Excel/Power Query, Python og Claude API/Claude '
           'Code; tavlemøder, Gemba og visuel ledelse som faste punkter i ugen, og KPI, OEE, OTD '
           'og MTBF/MTTR som tallene bag tavlen. Tiltrædelse efter aftale · Måløv, kort vej til '
           'Brønshøj.', after=48)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('STILLINGEN SOM UDBUDT: HVAD JEG BRINGER', ('Krav', 'Dokumentation'), [
        ('Dagligt engagement ved at interagere med alle operatører på gulvet og afholde daglige '
         'produktionsmøder',
         'Daglige tavlemøder med 14-mands team og 11 anlæg i Ventek-Air, og rundgang på gulvet som '
         'fast punkt i 24/7-driften hos Biofos, hvor tavlen bandt dag- og aftenhold sammen om '
         'dagens mål for output.'),
        ('Fremme sikkerheden ved at skabe og opretholde et sundt og sikkert arbejdsmiljø for alle '
         'teammedlemmer',
         'LOTO, APV, risikovurdering ved opstart og nærved-hændelser som fast disciplin i Biofos og '
         'ELOHVAC; sikkerhedsgennemgang før hvert arbejde, nul kritiske afvigelser i '
         'serviceaftalerne og i 37 GMP-afleveringer.'),
        ('Forbedre produktionsstandarder ved kontinuerligt at forbedre og vedligeholde standard '
         'work, SMED etc. for at understøtte vækstmålene',
         '5S, Standard Work og PDCA indført på værksted og lager i Biofos; SMED anvendt på '
         'omstillingen mellem opgaver, og standardiserede arbejdsgange i Ventek-Air gav markant '
         'løft i leveringsevnen, fordi rækkefølgen var aftalt på forhånd.'),
        ('Samarbejde med det tekniske supportteam, planlægningsteamet og ledergruppen om '
         'arbejdsglæde, output og produktivitet',
         'Matrixledelse af to sideløbende organisationer med én samlet plan; i Novo Nordisk blev '
         'fremdrift og ressourcer styret for 37 projekter på tværs af engineering, indkøb og anlæg '
         'med månedsrapportering til ledelse og bygherre, så beslutninger blev taget i fællesskab.'),
        ('Ansvar for et produktionsområde (en value stream) med ca. 25 operatører og teknikere på '
         'dag- og aftenhold samt 2 PTA-ingeniører',
         'Tværfaglig ledelse af 25 højt specialiserede medarbejdere hos Novo Nordisk, daglig ledelse '
         'af 14-mands team i Ventek-Air og skifteholdsdrift hos Biofos på dag- og aftenhold. '
         'PTA-samarbejdet svarer til samarbejdet med engineering og anlæg, jeg kørte på 37 projekter.'),
        ('Sikre effektiv produktion, høj kvalitet og rettidig levering med udgangspunkt i LEAN',
         '11 samtidige anlæg leveret til aftalt tid i Ventek-Air; 37 projekter afleveret uden '
         'kritiske afvigelser hos Novo Nordisk; 40 % lavere energiomkostninger via PDCA. LEAN er '
         'arbejdsformen, ikke en plakat.'),
        ('Stærkt samarbejde med kolleger både i Danmark og Polen',
         'Grænseflader mellem to organisationer er styret før: ELOHVAC og Data Power har kørt '
         'sideløbende siden 2024 med skriftlige aftaler om prioriteter. Samarbejdet med Polen '
         'kræver de samme faste punkter på tavlen, som jeg kører i dag, bare med en tidsforskel '
         'indbygget.'),
        ('Videregående teknisk uddannelse, fx som ingeniør, og erfaring med produktionsledelse',
         'B.Tech (EQF6) i teknologiledelse og maskinteknik, 2017–2022, og elautoriseret '
         'maskinmester LV/MV/HV, 2023; produktionsledelse siden 2003 som produktionsteamleder, '
         'driftsleder og projektleder med driftsansvar.'),
        ('Bachelor- eller kandidatgrad inden for ingeniørvidenskab, produktion eller lignende',
         'B.Tech svarer til bachelor-niveau (EQF6) med ingeniørfagligt indhold i maskinteknik, '
         'produktion og teknologiledelse; suppleret med elteknisk design fra Tehran Technical '
         'University (EQF 6), 2000–2003.'),
        ('Mindst 3 års erfaring med ledelse af produktion og kendskab til planlægning på tværs af '
         'linjer',
         'Over 20 år med ledelse af produktion og drift: 12 mekanikere og teknikere i ARJ '
         '(2003–2010), skiftehold i Biofos (2017–2022), 11 anlæg på tværs af linjer i Ventek-Air, '
         '37 projekter på tværs af engineering, indkøb og anlæg hos Novo Nordisk.'),
        ('Stærke lederevner og motivere teams til fælles retning og resultater',
         'Situationsbestemt ledelse (SLII), 1:1 og MUS som faste rammer; målstyring og '
         'vagtplanlægning i ARJ, kompetencematricer og struktureret oplæring af lærlinge i '
         'Data Power, og fælles retning sat via tavlemøder, hvor tallene blev gennemgået med '
         'holdet først.'),
        ('Løbende forbedringer og trives i en LEAN-kultur',
         'Lean og Six Sigma brugt i praksis siden 2017: DMAIC, 5S, PDCA, VSM, A3, Kaizen, SMED og '
         'TPM; PDCA-programmet gav 40 % lavere energiomkostninger hos Novo Nordisk, og Kaizen er '
         'planlagt som de første forløb i 90-dages planen.'),
        ('Imødekommende adfærd og lyttende væsen, balance mellem at stille krav og sætte '
         'forventninger',
         'Akkordopgørelse altid sammen med den, der udførte arbejdet; 1:1-samtaler og struktureret '
         'oplæring af lærlinge og teknikere siden 2003; krav og forventninger sat på tavlen med '
         'en begrundelse, så holdet kendte baggrunden.'),
        ('Trives i en rolle med både driftsansvar og forbedringsfokus',
         'Biofos: oppetid og akut fejlfinding i 24/7-drift samtidig med 5S og PDCA på værksted og '
         'lager. Novo Nordisk: daglig drift på anlæg samtidig med et PDCA-program, der skar '
         '40 % af energiomkostningerne.'),
        ('Opnåelse af givne produktionsmål og forandringer for at imødekomme vækst og stigende '
         'efterspørgsel',
         'Kapacitets- og fremdriftsstyring for 11 samtidige projekter under stigende belastning; '
         'ansvar for AI-afdelingen med 4-10 personer; overflytning af hele den el-tekniske '
         'aktivitet fra ELOHVAC til Data Power uden stop i driften.'),
        ('Benyttelse af LEAN-værktøjer som stor del af at opnå succes med målene',
         'Værktøjerne i brug på konkrete opgaver: 5S og Standard Work på lager og værksted, VSM og '
         'flaskehalsanalyser på tavlemøder, A3 og 5xHvorfor ved fejl, SMED ved omstilling, TPM og '
         'FMEA i det forebyggende vedligehold.'),
        ('Motiveres af ledelse af operatører',
         'Personaleledelse af 5 elektrikere og 3 lærlinge, 12 mekanikere og teknikere, et 14-mands '
         'team og 25 specialister: daglig planlægning, oplæring, målstyring og samtaler, tættest '
         'på dem, der udfører arbejdet.'),
        ('Ingeniør- eller tilsvarende faglig baggrund',
         'Elautoriseret maskinmester (LV/MV/HV, 2023) med B.Tech i maskinteknik og teknologiledelse '
         '(2017–2022): den faglige baggrund for at tale både PTA-ingeniørernes beregninger og '
         'operatørernes hverdag ved maskinen.'),
    ], widths=(2900, 7446), compact=True)

    m.section('DE FØRSTE 90 DAGE')
    for b in (
        'Dag 1–30: gulvet på begge hold. Alle operatører og teknikere talt med, standard work og '
        'changeover-tider kortlagt som de er i dag, sikkerhedsgennemgang på hvert skift. Intet '
        'ændret, før grundlaget ligger der.',
        'Dag 31–60: standard work revideret sammen med operatørerne, SMED-forløb på den '
        'omstilling, der tager længst tid, og daglige produktionsmøder kørt med samme struktur på '
        'dag- og aftenhold. Grænsefladerne til teknisk support, planlægning og kollegerne i Polen '
        'aftalt skriftligt.',
        'Dag 61–90: de første Kaizen-forløb sat ind på de største tab fra kortlægningen, mål for '
        'kvalitet, output og rettidig levering synlige på tavlen, og en 90-dages gennemgang med '
        'ledergruppen af værdistrømmens mål mod væksten.'):
        m.bullet('', b, after=16)

    m.para('**Jeg kan træffes på +45 93 99 95 14 og ajlooshahram@gmail.com** og er klar til '
           'samtale i uge 48.', after=20)

    m.save(path, title='Produktionsleder (Value Stream Manager), Solution Pack - Radiometer Medical ApS')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Radiometer_Produktionsleder.docx')
    build(out)
    print(out)
