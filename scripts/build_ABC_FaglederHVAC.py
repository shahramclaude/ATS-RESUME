# -*- coding: utf-8 -*-
"""ABC – Rådgivende Ingeniører A/S — Fagleder, HVAC (Glostrup).

Form (master/FORMKATALOG.md): åbning **K** (modstriden: deres egen sætning vendes),
struktur **Fejltilstandene** (fem fejl med det, der fanger dem), register **Lærerens**
(facitliste, pensum, oplæg, rettelse, kompetence). Kulturfil: jd/ABC_FaglederHVAC_kultur.txt.
Opslaget beder om CV og løbende samtaler — side 1 er breve, CV s.2-3, matrix s.3-4.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Fagleder HVAC · installationer, granskning og standarder · elautoriseret maskinmester'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('4. november 2026')
    m.meta('ABC – Rådgivende Ingeniører A/S · Installationsafdelingen · Glostrup')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Fagleder, HVAC', bold=True, color='1A1A1A')
    m.para('Til forretningschef for Installationer Kasper Lyngsfeldt', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('**I skriver, at I ikke har ret meget »sådan plejer vi at gøre«-mentalitet. Det er '
           'styrken — og det er præcis den risiko, stillingen skal håndtere.** En '
           'installationsafdeling, der er gået fra 1 til 30 på halvandet år, har ikke et '
           'rutineproblem. Den har et **facitliste**problem: kvaliteten hænger på de få, der har '
           'prøvet det før, indtil nogen skriver ned, hvordan den bliver lavet, så den næste kan '
           'lave den igen. Otte års **Børsens Gazellepris** og en afdeling, der er vokset fra 1 til 30, '
           'giver netop det råderum — og gør spørgsmålet om **faglig retning** til det mest '
           'presserende i huset. Det er den opgave, jeg søger som **go-to fagspecialist** for HVAC.', after=80)

    m.para('**En fagleder på 30 mand laver ikke kvaliteten selv. Han laver facitlisten.** Derfor er '
           'denne side bygget som fem fejltilstande, jeg har set koste penge på den anden side af '
           'bordet, og det, der fanger dem. Det er samme rækkefølge, jeg ville tage '
           '**konceptgranskning** og **kvalitetssikring** i. Det er også den måde, **Kompetencebaseret '
           'Rådgivning** bliver holdbar på: den enkelte specialists viden skal kunne ses af de andre.', after=70)

    m.para('**1. Rummet, der ikke havde plads.** Kanaler, rør og kabelbakker skal mødes i et snit, '
           'som ingen har tegnet færdigt, og bliver det opdaget på pladsen, koster det en ændring og '
           'en frist. Det fanges i granskningen, før modellen låses — af en, der har stået i rummet: '
           'jeg har leveret 11 samtidige anlægsprojekter i Ventek-Air og drevet anlæg i døgndrift, '
           'hvor plads til service og udskiftning blev afgjort efter, at der var støbt.', after=60)

    m.para('**2. Grænsefladen, der blev aftalt mundtligt.** El, VVS, ventilation og styring mødes '
           'altid samme sted, og der er altid to, der mener, at den anden har ansvaret. Jeg har '
           'koordineret 25 specialister på 37 kapitalprojekter, hvor hver grænseflade havde et navn '
           'og en dato, og hvor nul kritiske fund ved aflevering var resultatet af det — ikke af '
           'held.', after=60)

    m.para('**3. Modellen og virkeligheden.** En BIM-model kan være korrekt og stadig ubrugelig for '
           'dem, der skal drifte anlægget. Jeg har drevet det, der blev tegnet, i fem år på et '
           'kritisk anlæg med **SRO** og 24/7-drift, og ved, hvilke krav til måling, adgang og '
           'udskiftning der skal ind, før modellen låses. BIM som arbejdsform kender jeg fra '
           'grænseflader og granskning; jeg tegner ikke modellerne selv.', after=60)

    m.para('**4. Tilbuddet, der blev billigere end forudsætningerne.** Jeg har ejet en virksomhed '
           'med fuldt P&L siden 2023 og ved, hvad en mængde, der ikke står skrevet, koster, når '
           'regningen skal gøres op. **ABR89, AB92, ABR18, AB18 og A113** har jeg arbejdet under som '
           'entreprenør: tilbud, ændringshåndtering, frister og aflevering. En ændring, der ikke er '
           'beskrevet, er en gave til den anden part.', after=60)

    m.para('**5. Viden, der gik ud ad døren.** Den mest erfarne konstruktør tager sin viden med, når '
           'hun skifter job — medmindre den står i en **firmastandard**, et notat eller et regneark, '
           'nogen kan bruge. Det er hele ideen i **ABC Academy**, og det er den del af stillingen, '
           'jeg glæder mig mest til: oplæg for installationsgruppen og materiale, der kan '
           'genbruges. Jeg har lavet kompetenceplaner for 12–14 medarbejdere, oplært tre lærlinge og '
           'bygget egne tjekliste- og beregningsværktøjer med over 40 % færre manuelle timer til '
           'følge.', after=70)

    m.para('**Det, jeg ikke har, skal stå klart:** jeg har ikke syv års projektering på et '
           'rådgivningskontor. Jeg har over tyve år på den side af bordet, hvor tegningen bliver til '
           'et anlæg — som entreprenør, som driftsleder og som den, der skulle modtage og '
           'idriftsætte andres arbejde med FAT/SAT og nul kritiske fund. Det er den erfaring, en '
           '**konceptgranskning** har brug for at blive holdt op imod, og det er derfor, jeg søger '
           'en faglig retning frem for en tegnestue.', after=70)

    m.para('**Praktisk:** jeg bor i Måløv, 12 km fra jeres kontor i Glostrup, har kørekort og bil og '
           'kan være på projekterne i hverdagen. Jeg taler dansk som modersmål og engelsk '
           'professionelt, også i tekniske forhandlinger, og jeg kan starte efter aftale. Et **uformelt '
           'arbejdsmiljø** kræver, at nogen tager ansvar for, at **trivsel, udvikling og socialt '
           'sammenhold** hænger sammen med det faglige — det har jeg gjort i tre virksomheder. Jeg vil '
           'gerne høre, hvordan I i dag vælger, hvilke projekter der skal granskes, og hvem der '
           'skriver den første firmastandard — det er der, jeg ville begynde.', after=70)

    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Installations- og driftsleder med 20+ års erfaring fra tekniske anlæg — **elautoriseret '
           'maskinmester (LV/MV/HV)**, B.Tech i teknologiledelse og maskinteknik og køle- og '
           'ventilationsteknisk uddannelse fra AMU. Har leveret **11 samtidige anlægsprojekter** med '
           '14 medarbejdere i Ventek-Air, koordineret **25 specialister** på **37 kapitalprojekter** '
           'med nul kritiske fund i Novo Nordisk og drevet et kritisk anlæg i **24/7-drift** i fem år '
           'med **over 40 % lavere energiforbrug**. Driver siden 2023 egen el- og '
           'installationsteknisk virksomhed med **5 elektrikere, 3 lærlinge, fuldt P&L og '
           'elautorisationen** — og bygger de standarder, andre kan arbejde efter.', after=80)

    m.section('FACITLISTEN — GRANSKNING, STANDARDER OG OPLÆRING')
    for label, body in [
        ('Konceptgranskning og kvalitetssikring',
         'Granskning af andres arbejde mod forudsætningerne: krav, mængder, grænseflader og '
         'fremdrift gennemgået før udsendelse; i Novo Nordisk som modtager af 37 leverancer med '
         'FAT/SAT og nul kritiske fund ved aflevering.'),
        ('Faglig retning og standarder',
         'Standarder skrevet for at blive brugt: tjeklister, skabeloner og regneark, der gør den '
         'samme opgave ens for nummer to og tredje mand — indført i egen virksomhed med over 40 % '
         'færre manuelle timer som resultat.'),
        ('Grænseflader og tværfaglighed',
         'El, VVS, ventilation, styring, arkitekt og bygherre koordineret i 37 kapitalprojekter og 11 '
         'anlægsprojekter: hver grænseflade med ejer, dato og skriftligt svar frem for mundtlig '
         'aftale.'),
        ('Projekteringsmøder og leverance',
         'Deltagelse i projekterings- og byggemøder med projektledere, rådgivere og entreprenører; '
         'leverancer fulgt på tid og kvalitet, afvigelser rejst samme uge og lukket med navn.'),
        ('Forudsætninger og kontraktgrundlag',
         'ABR89, AB92, ABR18, AB18 og A113 arbejdet under som entreprenør: tilbud, mængder, '
         'ændringer, fristforlængelser og aflevering; forudsætninger skrevet ned, før de blev '
         'dyre.'),
        ('Oplæring og sparring',
         'MUS og kompetenceplaner for 12–14 medarbejdere, tre lærlinge oplært; faglige oplæg og '
         'sidemandsoplæring som fast del af lederrollen — tilgængelighed i hverdagen, ikke kun i '
         'mødelokalet.')]:
        m.bullet(label, body, after=25)

    m.models_table('FAG, SYSTEMER OG METODER', ('Område', 'Dokumenteret brug'), [
        ('HVAC og installationer',
         'Ventilation, køl og VVS projekteret og leveret i egen virksomhed og i Ventek-Air; '
         'kanaler, luftmængder, tryk og indeklima vurderet mod drift og energiforbrug.'),
        ('El og styring',
         'LV/MV/HV, transformere, koblingsanlæg, motorer og frekvensomformere; SRO/SCADA som den '
         'måde ventilation og pumper bliver styret på i døgndrift.'),
        ('Byggeri og kontrakt',
         'AB-vilkår, tilbud, mængdeberegning og ændringshåndtering; bekendtgørelser og '
         'retningslinjer omsat til arbejdsinstruktioner på pladsen.'),
        ('BIM og granskning',
         'Modelgranskning og grænsefladekontrol som bruger og bestiller; krav til modellen stillet '
         'skriftligt, før den blev låst — ikke authorering.'),
        ('Energi og indeklima',
         'Energiledelse med over 40 % lavere forbrug på et 24/7-anlæg; måling, indregulering og '
         'driftsoptimering af pumper, blæsere og ventilation.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · elautorisation · el- og installationstekniske '
         'ydelser',
         [('Faglig ledelse, tilbud og standarder',
           'Tilbud, mængder og ændringer på entreprise- og serviceopgaver; standarder og skabeloner '
           'for tjek, dokumentation og aflevering; faglig sparring med elektrikere og lærlinge i '
           'hverdagen.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('Granskning, grænseflader og aflevering',
           'Kravspecifikation, FAT/SAT og idriftsættelse af elektriske anlæg og styringer; '
           'grænseflader til ventilation, VVS og bygherre aftalt skriftligt; nul kritiske fund ved '
           'aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter · ventilation',
         [('Leverance og fremdrift',
           'Dagligt tavlemøde, kapacitets- og flaskehalsanalyse og omprioritering samme dag, når en '
           'maskine eller et menneske faldt væk; leverancer styret til deadline med '
           'afleveringspakker.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Lynetten under Biofos · København · aug. 2017–jan. 2022',
         'Kritisk anlæg i 24/7-drift · SRO · ventilation, pumper, transformere, koblingsanlæg',
         [('Drift, indeklima og energi',
           'Ventilation, pumper og blæsere optimeret med over 40 % lavere energiforbrug; 5S og '
           'standard work på værksted og lager; arbejdsmiljø, sikkerhedsrunder og APV-handlinger '
           'fulgt til dørs.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · industrielt udstyr',
         [('Teknisk service og oplæring',
           'Fejlfinding og reparation på industrielt udstyr; vagtplanlægning, oplæring og opfølgning '
           'på mål for 12 teknikere.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('UDDANNELSE OG AUTORISATION')
    m.edu('B.Tech, teknologiledelse og maskinteknik',
          'Maskinmesterskolen København · 2017–2022 · gennemsnit 7,6/12')
    m.edu('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('Køle- og ventilationsteknik · AMU', 'Mercantec 2021 · STCW, Søfartsstyrelsen 2021')
    m.edu('El- og maskinteknisk konstruktion, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6')

    m.section('SPROG, PRAKTIK OG REFERENCER')
    m.para('Dansk: modersmål · Engelsk: professionelt, også teknisk · Persisk: modersmål · '
           '**Kørekort B og egen bil** · Måløv, 12 km fra Glostrup · Kan starte efter aftale · '
           'Referencer på forespørgsel.', after=70)

    m.models_table('OPSLAGETS KRAV — MIT FACIT', ('Krav i opslaget', 'Dokumentation'), [
        ('Installationsfagligt relevant uddannelse',
         'Elautoriseret maskinmester (LV/MV/HV), Sikkerhedsstyrelsen 2023; B.Tech i '
         'teknologiledelse og maskinteknik 2017–2022 med 7,6/12; køle- og ventilationsteknisk AMU '
         '2021; el- og maskinteknisk konstruktion 2000–2003, EQF 6.'),
        ('Stærk faglig ekspertise inden for installationer med 7+ års relevant erhvervserfaring',
         '20+ år i installationer og drift: 11 anlægsprojekter i ventilation (Ventek-Air 2022), 37 '
         'kapitalprojekter med el og styring (Novo Nordisk 2022-2024), fem år i 24/7-drift med '
         'ventilation og SRO (2017-2022), 12 teknikere i ARJ 2003-2010.'),
        ('Forståelse for bekendtgørelser og retningslinjer',
         'Elautorisation og arbejde under Sikkerhedsstyrelsens krav, arbejdsmiljølovgivning og '
         'GMP/FDA/EMA i 37 projekter; regler omsat til arbejdsinstruktioner, der blev brugt på '
         'pladsen — og kontrolleret ved sikkerhedsrunder.'),
        ('Indgående kendskab til byggebranchen',
         'Entreprenør siden 2023 med fuldt P&L, tilbud og aflevering; 11 samtidige anlægsprojekter '
         'med underentreprenører i 2022; bygherre- og modtagerside i 37 kapitalprojekter med '
         'FAT/SAT og nul kritiske fund.'),
        ('Kendskab til kontraktgrundlag ABR89, AB92, ABR18, AB18 og A113',
         'Arbejdet under alle 5 kontraktgrundlag som entreprenør og leverandør i 11 anlægsprojekter og '
         'egne entrepriser: tilbud, mængder, '
         'ændringshåndtering, fristforlængelser og aflevering — og set, hvad et skriftligt svar '
         'gør ved en sag.'),
        ('Forståelse for kundernes behov og sans for det kommercielle',
         'Egen virksomhed med fuldt P&L siden 2023: prissætning, dækningsgrad, serviceaftaler og '
         'betalingsopfølgning for 8 medarbejdere; forretningen vokset fra opstart til fast '
         'opgaveportefølje.'),
        ('Sætte den faglige retning og sikre fremdriften for HVAC',
         'Standarder og arbejdsgange indført i egen virksomhed med over 40 % færre manuelle timer; '
         'dagligt tavlemøde og ugentlig opfølgning for 12-14 medarbejdere; leverancer styret til '
         'dato i 11 samtidige projekter.'),
        ('Afholde konceptgranskning og kvalitetssikring på egne og andres projekter',
         'Granskning af andres leverancer mod forudsætningerne i 37 kapitalprojekter; FAT/SAT og '
         'afleveringsgennemgang med nul kritiske fund; tjeklister og facitlister udarbejdet, så '
         'granskningen blev ens hver gang.'),
        ('Fagansvarlig eller delprojektleder for HVAC-ingeniører og BIM-tegnere',
         'Ledelse af 11-14 medarbejdere i to virksomheder og faglig ledelse af 5 elektrikere og 3 '
         'lærlinge i dag; koordinering af 25 specialister på 37 projekter — arbejdsfordeling, '
         'faglig sparring og opfølgning pr. person.'),
        ('Sikre proaktive grænseflader op imod andre fag',
         'Grænseflader mellem el, VVS, ventilation, styring og bygherre aftalt skriftligt med ejer '
         'og dato i 37 kapitalprojekter; i egen virksomhed er grænsefladen til andre fag den '
         'daglige form.'),
        ('Ansvar for leverancer, både kvalitets- og tidsmæssigt',
         '37 parallelle kapitalprojekter med månedlig rapportering af fremdrift, økonomi og risiko; '
         '11 samtidige anlægsprojekter i 2022 leveret til deadline; nul kritiske fund ved '
         'aflevering.'),
        ('Deltage på projekteringsmøder sammen med projektledere',
         'Projekterings- og byggemøder med projektledere, rådgivere, arkitekt og entreprenører i 37 '
         'kapitalprojekter og i egen virksomhed; beslutninger skrevet ned samme dag med navn og dato.'),
        ('Løbende fastlægge og opdatere projekternes forudsætninger',
         'Forudsætninger skrevet ned, før arbejdet blev sat i gang, i 37 kapitalprojekter og i egen '
         'virksomheds tilbud; ændringer dokumenteret med mængde, pris og konsekvens for tidsplanen.'),
        ('Bidrage til ABC Academy med faglige oplæg og firmastandarder',
         'Faglige oplæg og sidemandsoplæring som fast del af lederrollen; tjeklister, skabeloner og '
         'regneark bygget og genbrugt på tværs af opgaver med over 40 % færre manuelle timer; tre '
         'lærlinge oplært siden 2023.'),
        ('Være tilgængelig sparringspartner for kolleger i installationsafdelingen',
         'Daglig sparring med 12-14 teknikere og 5 elektrikere i to virksomheder; MUS og '
         'kompetenceplaner med et konkret næste skridt pr. person; tilgængelig på gulvet, ikke kun '
         'i mødelokalet.'),
        ('Struktureret, tager ansvar og møder deadlines uden at gå på kompromis med kvaliteten',
         '37 kapitalprojekter rapporteret månedligt til ledelse og bygherre; 11 samtidige '
         'anlægsprojekter uden at kvaliteten faldt; nul kritiske fund ved aflevering og tjeklister '
         'fulgt hver gang.'),
        ('Strategisk tilgang til komplekse problemer og tværfaglige løsninger',
         'Flaskehals- og kapacitetsanalyse i 11 samtidige projekter; energiledelse med over 40 % '
         'lavere forbrug på et 24/7-anlæg; beslutninger vejet mod både drift, økonomi og '
         'tidsplan.'),
        ('Kommunikerer konstruktivt og effektivt og trives i et åbent og uformelt miljø',
         'Dansk som modersmål og engelsk professionelt, også i tekniske forhandlinger; daglig '
         'kommunikation med håndværkere, specialister og ledelse i 20+ år — kort på skrift, klart i '
         'mødet.')])


    m.models_table('DET FØRSTE PENSUM — MATERIALE TIL ABC ACADEMY',
                   ('Materiale', 'Hvad det indeholder, og hvem der kan bruge det'), [
        ('Facitliste til konceptgranskning',
         'De 12 punkter enhver granskning skal svare på, før modellen låses: frihøjder, kanalføring, '
         'grænseflader, mængder, forudsætninger samt brand- og lydkrav — så granskningen bliver ens, '
         'uanset hvem der holder den.'),
        ('Grænsefladeliste',
         'Én linje pr. grænseflade med ejer, modpart, dato og status; gennemgået på '
         'projekteringsmødet og lukket skriftligt, så en aftalt grænseflade ikke forsvinder med den '
         'person, der aftalte den.'),
        ('Forudsætningsskema',
         'Det, projektet bygger på, skrevet ned ved opstart og opdateret ved hver ændring: arealer, '
         'luftmængder, temperaturer, tryk og kontraktgrundlag (ABR 18, AB 18, A 113) — det dokument, '
         'en ændring kan måles imod.'),
        ('Test- og afleveringsprotokol',
         'Hvad der skal måles, dokumenteres og godkendes ved aflevering, med ansvarlig og dato; '
         'bygget på de 37 leverancer jeg har modtaget med FAT/SAT og nul kritiske fund, så næste '
         'projekt ikke starter forfra.')])

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_ABC_FaglederHVAC.docx')
    build(out)
    print(out)
