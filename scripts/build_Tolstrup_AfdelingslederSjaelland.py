# -*- coding: utf-8 -*-
"""Tolstrup A/S — Afdelingsleder på Sjælland (anlægsgartnerbranchen), Hedehusene.

Form (master/FORMKATALOG.md): åbning **J** (citatet fra opslaget besvares direkte),
struktur **Spørgsmålene kunderne stiller** (fem spørgsmål i rækkefølge), register
**Sæsonen** (nyt: frost, tø, sætning, klipning, løvfald, beredskab, materiel, rute).
Kulturfil: jd/Tolstrup_AfdelingslederSjaelland_kultur.txt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Afdelingsleder · drift, medarbejdere og kunder på Sjælland'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('12. november 2026')
    m.meta('Tolstrup A/S · Baldersbuen 21B, 2640 Hedehusene · att. direktør Peter Lund')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Afdelingsleder, Sjælland', bold=True, color='1A1A1A')

    # ---------------------------------------------------------------- side 1
    m.para('**»Vil du lede vores afdeling på Sjælland?«** I har skrevet spørgsmålet selv — og I har '
           'skrevet svaret lige efter: **»Vær med til at opbygge, udvikle og sætte retningen.«** Det '
           'er to opgaver i én stilling. Den ene er at holde en drift, der allerede kører. Den anden '
           'er at gøre en afdeling, der blev åbnet i 2025, i stand til at bære det, salget lover. Det '
           'er den anden, jeg søger.', after=60)

    m.para('**Sjællandsafdelingen er ikke et forsøg.** I åbnede den, fordi kunderne havde efterspurgt '
           'jer her i årrække, og I blev landsdækkende med fire afdelinger og mere end 200 '
           'medarbejdere. Regnskabet for 2025 viser bruttofortjeneste på over 75 mio. kr. mod 56 året '
           'før og et resultat før skat på næsten 11 mio. kr. Det er den ramme, afdelingen bliver målt '
           'i: den skal bære sin andel af væksten uden at trække kvaliteten ned i Fredericia, Aarhus '
           'og Odense. Med Slots- og Kulturstyrelsen som kunde er der arealer, hvor en fejl ikke bliver '
           'en reklamation, men en avisoverskrift.', after=60)

    m.para('**Fem spørgsmål, jeres kunder stiller — og som afdelingen skal kunne svare på.**', after=50)

    m.para('**»Kan I være der på mandag?«** Det handler om kapacitet og om at kunne svare, før man '
           'regner. I 2022 havde vi 11 samtidige anlægsprojekter med 14 medarbejdere og '
           'underentreprenører: kapacitetsanalyse hver morgen, omprioritering samme dag og én samlet '
           'plan, som sjakkene kunne se. Det er den tavle, en ny afdeling skal starte med.', after=44)

    m.para('**»Hvem er det, der står på vores areal?«** Fagligheden er ikke noget, en afdelingsleder '
           'kan holde i hånden; den sidder i folkene. Jeg har oplært 12 teknikere og 3 lærlinge i '
           'standarder, de selv var med til at skrive, og jeg har drevet en virksomhed med 5 '
           'elektrikere og 3 lærlinge, hvor kunden mødte den, der ejede opgaven. Sådan vil jeg også '
           'lære anlægsgartnerfaget: ude på arealerne, af dem der har gjort det i tyve år.', after=44)

    m.para('**»Hvad sker der i januar?«** Vintertjeneste har jeg ikke kørt. Jeg har haft beredskab i '
           'fem år på Lynetten, hvor anlægget kørte 24/7: vagtplan, rådighed, responstid og en '
           'eskalering, der var skrevet ned, før telefonen ringede. Vinterberedskab er den samme '
           'disciplin med frost, tø og salt i stedet for pumper — og med maskiner og materiel, der '
           'skal stå klar, når sæsonen skifter, så jeres **udearealer** er farbare kl. 6 om morgenen. '
           'Maskiner, indkøb og reparation havde jeg som '
           'ansvarsområde i ARJ Engineering med eget værksted og 12 teknikere.', after=44)

    m.para('**»Hvad koster det, når vi ændrer noget?«** Jeg har haft budgetansvar på 2–10 mio. kr. pr. '
           'projekt, fuldt P&L i egen virksomhed og ændringshåndtering, hvor merarbejde skal '
           'godkendes, før det udføres. En afdeling i vækst dør ikke af for lidt ordrebog, men af '
           'opgaver, der blev taget for at være flink, og som ingen havde regnet på.', after=44)

    m.para('**»Hvordan ved vi, at kvaliteten holder?«** Grøn pleje måles ikke i en rapport, men på '
           'arealet, når kunden kigger. Derfor: egenkontrol før aflevering, runder med faste '
           'kontrolpunkter og dokumentation, der kan vise, hvad der blev gjort og hvornår. I 37 '
           'kapitalprojekter gav metoden nul kritiske afvigelser ved aflevering; kvalitetssikring er '
           'en kontrol, ikke en holdning.', after=60)

    m.para('**Jeg kommer ikke fra anlægsgartnerbranchen.** Det skal stå her og ikke opdages til '
           'samtalen. Det, jeg har, er 20+ år i drift og vedligehold af fysiske anlæg og udstyr, '
           'maskiner og materiel med indkøb og reparation, entreprise i byrum og på byggepladser samt '
           'personaleledelse af håndværkere, teknikere og specialister. Faget — træer, hæk, '
           'belægning, sætning, sæson — lærer jeg af sjakkene, og jeg lærer det hurtigere ved at '
           'spørge end ved at gætte.', after=60)

    m.para('**Jeres fire værdier er ikke pynt.** **»Ansvarlighed er ikke noget vi taler om, det er '
           'noget vi gør.«** **»God ledelse handler for os om at forløse menneskers potentiale.«** '
           '**»Vi ansætter mennesker efter potentiale og vilje«**, og **»Gensidighed og tillid er '
           'fundamentet.«** Det er den ledelse, jeg har praktiseret: standarder skrevet sammen med '
           'dem, der skal arbejde efter dem, og en grænse, der er tydelig nok til, at folk tør tage '
           'beslutningen selv. I skriver selv, at fastholdelse **reducerer sygefravær** og **udvikler '
           'os som ledere** — det er ikke et socialt projekt ved siden af driften, det er driften, '
           'der bliver stabil af det. Jeg har arbejdet i en virksomhed, hvor **faglighed, '
           'ordentlighed og ægte ansvar** var kravet i hverdagen, og hvor der var **frihed under '
           'ansvar** og **tanke til handling** uden fire mellemled — den slags kultur er ikke noget, '
           'man indfører; det er noget, man ikke ødelægger. Peter Lund har sagt det med jeres egne ord: '
           'det, der driver jer, er at mærke, at **kunderne føler sig godt behandlet** og har tiltro '
           'til jer — og at der er **synergi i de ting, vi gør vestpå såvel østpå**. Det kræver en '
           '**rummelig arbejdsplads** og **modet til at sige ja**, når der er et menneske, der kan '
           'løfte opgaven, og det er **det grønne håndværk**, der skal holdes højt, når hverdagen '
           'bliver travl. Jeres **ESG**-rapport og arbejdet med **bæredygtighed** i drift og materiel — '
           '41 % lavere energiintensitet siden 2022 — holder kun, hvis afdelingerne bliver målt på '
           'det hver måned.', after=60)

    m.para('**Praktisk:** jeg bor i Måløv, 35 minutter fra Hedehusene, har kørekort B og bil og kan '
           'dække Sjælland som en fast del af ugen. Dansk og engelsk, skriftligt og mundtligt. Jeg '
           'kan starte efter aftale. Det, jeg gerne vil høre om, er, hvor stor en del af '
           'Sjællandsomsætningen der i dag ligger på faste aftaler — og hvordan I måler kvaliteten i '
           'grøn pleje, når arealet er kundens og ikke jeres.', after=50)

    m.meta('Med venlig hilsen', after=15)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('**Drifts- og personaleleder** med 20+ års erfaring fra fysiske anlæg, entreprise og '
           'tekniske installationer — **elautoriseret maskinmester (LV/MV/HV)**, B.Tech i '
           'teknologiledelse og maskinteknik. Har ledet **14 medarbejdere** i **11 samtidige '
           'anlægsprojekter**, ført **37 kapitalprojekter** på 2–10 mio. kr. og drevet egen '
           'virksomhed med **fuldt P&L** siden 2023. Ansvar for **drift, økonomi, materiel, '
           'arbejdsmiljø og medarbejderudvikling** — og for at bygge de værktøjer, der gør tallene '
           'til beslutninger (**Python**, AI-assisteret rapportering og KPI).', after=70)

    m.section('SÆSONEN — DRIFT, MENNESKER OG ØKONOMI')
    for label, body in [
        ('Sæsonen og kapaciteten',
         'Året skifter i spidsbelastninger, og bemanding skal følge dem: **kapacitetsanalyse** hver '
         'morgen, **driftsplanlægning** på én tavle og omprioritering samme dag i 11 samtidige '
         'projekter med 14 medarbejdere og underentreprenører.'),
        ('Materiel og værksted',
         '**Maskiner** og **materiel** som ansvarsområde i ARJ Engineering: **indkøb**, '
         '**vedligehold**, reparation og eget værksted med 12 teknikere — materiel, der ikke kører, '
         'koster mere end det, der bliver repareret i tide.'),
        ('Folkene i marken',
         '12 teknikere og 3 lærlinge oplært i standarder, de selv var med til at skrive; 8 ansatte i '
         'egen virksomhed med **rekruttering**, **oplæring** og **medarbejderudvikling**; i dag '
         '**kundeudvikling** og **mødeledelse** som en fast del af ugen.'),
        ('Beredskabet',
         'Fem år i 24/7-drift på Lynetten: vagtplan, rådighed, **responstid** og skriftlig '
         '**beredskabs**instruks — den samme disciplin, vintertjenesten kræver, når frosten kommer '
         'før, der er bestilt salt.'),
        ('Økonomien',
         '**Budgetansvar** på 2–10 mio. kr. pr. projekt og fuldt P&L siden 2023; '
         '**økonomiopfølgning** månedligt med afvigelsesforklaring, dækningsgrad pr. opgave og '
         '**ressourcer** afsat til det, der faktisk skal leveres.'),
        ('Kunderne og kvaliteten',
         '**Tilbud**, **kontrakt** og **opfølgning** hos **kommuner**, **boligselskaber**, '
         'forsyningsselskaber og private **bygherrer**; **kvalitetssikring** som egenkontrol og '
         'runder med faste kontrolpunkter — ikke som en rapport, der skrives bagefter.')]:
        m.bullet(label, body, after=16)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · egen kundekreds',
         [('Drift, kunder og økonomi',
           '**Tilbud**, udbud og ændringshåndtering; **budget** og **økonomi**, kunder og '
           'entreprenører i daglig koordinering; **arbejdsmiljø** med APV, LOTO og '
           'sikkerhedsrundering.')]),
        ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen',
         'Data Power Consultant ApS · København · 2024–nov. 2026 (sideløbende med ELOHVAC)',
         '4–10 personer · tekniske og industrielle applikationer',
         [('AI i drift og ledelse',
           '**AI coding** til tekniske anlæg og industrielle komponenter, kundeløsninger med '
           'LLM-API\'er og **AI i ledelsesarbejdet** — ledelsesrapportering, beslutningsoplæg og '
           '**KPI**-analyse; selskabet er ophørt.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('Krav, udførelse og aflevering',
           'Kravspecifikation, FAT/SAT og idriftsættelse; **kvalitetssikring** med afvigelser lukket '
           'med navn og dato og nul kritiske fund ved aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter',
         [('Fremdrift og kapacitet',
           'Dagligt **tavlemøde**, kapacitetsanalyse og omprioritering samme dag; leverancer styret '
           'til deadline med afleveringspakker og **dokumentation**.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Biofos (Lynetten) · København · aug. 2017–jan. 2022',
         'Renseanlæg i 24/7-drift · pumper, bassiner, SCADA',
         [('Drift, måling og energi',
           'Belastning og drift fulgt i døgndrift; **over 40 % lavere energiforbrug** gennem måling '
           'og indregulering; 5S og **arbejdsmiljø** indført som standard.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 teknikere · maskinværksted · maskiner og materiel',
         [('Værksted, materiel og service',
           'Fejlfinding, kalibrering og reparation; **indkøb** og **vedligehold** af maskiner og '
           'bilpark; oplæring og målopfølgning for 12 teknikere.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=16)

    m.section('UDDANNELSE OG AUTORISATION')
    m.edu('B.Tech, teknologiledelse og maskinteknik',
          'Maskinmesterskolen København · 2017–2022 · gennemsnit 7,6/12')
    m.edu('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('Køle- og ventilationsteknik · AMU', 'Mercantec 2021 · STCW, Søfartsstyrelsen 2021')
    m.edu('El- og maskinteknisk konstruktion, elteknik',
          'Tehran Technical University · 2000–2003 · EQF 6')

    m.section('SPROG, IT OG PRAKTIK')
    m.para('Dansk og engelsk, skriftligt og mundtligt · Persisk: modersmål · **IT**: '
           'ERP-baserede drifts- og økonomisystemer, CMMS, Excel og egne **Python**-værktøjer til '
           '**KPI**, tjeklister og rapporter · **Kørekort B og egen bil** · Måløv, 35 minutter fra '
           'Hedehusene · Kan starte efter aftale · Referencer på forespørgsel.', after=50)

    m.models_table('OPSLAGETS KRAV — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Overordnet ansvar for afdelingen på Sjælland',
         'Overordnet ansvar i 20+ år: **drift** i 24/7 i fem år, 11 samtidige projekter med 14 '
         'medarbejdere og egen virksomhed med fuldt **P&L** siden 2023.'),
        ('Selv være aktiv i driften med egne kunder og projekter',
         'Egen virksomhed: den, der sælger, står også på opgaven. 5 elektrikere, 3 lærlinge og '
         'egne **kunder** — jeg har ikke bestilt arbejdet hos andre.'),
        ('Ledelse og udvikling af driftsledere og medarbejdere',
         'Ledere og specialister har refereret til mig: 14 medarbejdere i 11 projekter, 25 '
         'specialister i 37 projekter, 12 teknikere og 3 lærlinge — ugentlig opfølgning på mål og '
         '**ledelsesudvikling** af den enkelte leder.'),
        ('Planlægning, styring og kvalitetssikring af drift og projekter',
         'Fast rækkefølge fra behov til aflevering i 37 projekter: **plan**, dagligt tavlemøde, '
         '**kvalitetssikring** med tjekliste og afleveringspakke — nul kritiske fund.'),
        ('Kundekontakt og udvikling af eksisterende og nye kunder',
         '**Kundekontakt** i 20+ år og **kundeudvikling** i egen virksomhed: tilbud og udbud mod en '
         '**kommune** eller et **boligselskab**, mersalg på faste aftaler og 8 ansatte i dag.'),
        ('Budgetansvar og opfølgning på økonomi og ressourcer',
         '**Budgetansvar** 2–10 mio. kr. pr. projekt og fuldt **P&L** siden 2023: månedlig '
         '**økonomiopfølgning**, timeforbrug pr. opgave og korrektion samme kvartal.'),
        ('Sikring af struktur, fremdrift og overblik i hverdagen',
         'Én tavle, én plan, én opfølgning: 11 samtidige projekter holdt adskilt uden at standse '
         'hinanden; **5S** i værkstedet som fast standard, så **overblik** ikke afhænger af hukommelse.'),
        ('Forankring af Tolstrups værdier og måde at arbejde på',
         'Værdier bliver først forankret, når de kan ses i en beslutning: **ansvarlighed**, '
         '**rummelighed**, **loyalitet** og **stolthed** — 4 værdier omsat til faste spilleregler for '
         'kvalitet, oplæring og adfærd på arealet.'),
        ('Erfaring fra en lignende rolle som driftsleder, entrepriseleder eller projektleder',
         '**Driftsleder** i fem år i 24/7-drift, **projektleder** for 37 kapitalprojekter og '
         '**entrepriseleder** for 11 samtidige anlægsprojekter med 14 mand.'),
        ('Solid erfaring med personaleledelse',
         '**Personaleledelse** i 20+ år: 12 teknikere og 3 lærlinge, 14 medarbejdere og '
         'underentreprenører, 25 specialister og 8 ansatte — inkl. MUS, sygefraværssamtaler og '
         'rekruttering.'),
        ('Branchekendskab fra anlægsgartnerbranchen eller beslægtet område',
         '**Anlægsgartner** er ikke min baggrund; **beslægtet** er den: drift og **vedligehold** af '
         'fysiske **anlæg** i 20+ år, **maskiner** og '
         '**materiel** med indkøb og reparation, arbejde udendørs under myndighedskrav. '
         'Anlægsgartnerfaget lærer jeg af sjakkene — det står også i brevet.'),
        ('Økonomisk forståelse og erfaring med budgetstyring',
         '**Budgetstyring** i 37 projekter og eget regnskab siden 2023: dækningsgrad pr. opgave, '
         'timepris, materielomkostning og en klar grænse for, hvornår en opgave ikke skal tages.'),
        ('Arbejder struktureret og har overblik, også når tempoet er højt',
         'Omprioritering samme dag i 11 samtidige projekter og i 24/7-drift: rækkefølgen bliver '
         'besluttet på tavlen kl. 6.30, ikke i en mail kl. 14.'),
        ('Tydelig og tillidsbaseret leder, der skaber følgeskab',
         'Standarder skrevet sammen med dem, der skal arbejde efter dem — 12 teknikere, 3 lærlinge '
         'og 8 ansatte; tydelig grænse for, hvad der besluttes hvor.'),
        ('God til at opbygge relationer til både medarbejdere og kunder',
         'Relationer bygget på at have svaret, når der blev ringet: hos **kunderne** i egen '
         'virksomhed, hos teknikerne i værkstedet og hos **bygherren**, når afleveringen skred — det er '
         '20+ år med samme telefonnummer til den, der ejer opgaven.'),
        ('Tæt samarbejde med virksomhedens ledelse og stabsfunktioner',
         'Arbejdet i og med **ledergruppe** og stabsfunktioner: månedlig rapportering til direktion '
         'og bygherre i 37 projekter, HR- og indkøbsfunktioner i Novo Nordisk samt egen ledelse i '
         'ELOHVAC.'),
        ('Være med til at opbygge, udvikle og sætte retningen for afdelingen',
         'Opbygget en virksomhed til 8 ansatte siden 2023 og en værkstedsfunktion med 12 mand: '
         'retningen sat som tre mål for kvartalet — ikke tredive.'),
        ('Tage ansvar, træffe beslutninger og være tæt på den daglige drift',
         'Beslutninger taget samme dag, når leverancen skred — i 37 projekter og i 24/7-drift; jeg '
         'har selv stået i værkstedet og på anlægget, når det gjaldt.'),
        ('Sikre at opgaverne bliver løst i høj kvalitet',
         '**Kvalitet** som målbart krav: egenkontrol før aflevering, tjekliste pr. opgave og nul '
         'kritiske afvigelser i 37 projekter — kvalitet er en kontrol, ikke en holdning.'),
        ('Sikre at medarbejdere og kunder er i trygge hænder',
         '**Arbejdsmiljø** og **sikkerhed** som fast punkt: sikkerhedsrundering, APV, instruktion '
         'ved nyt **materiel** og opfølgning på nærved-hændelser — i fem år i 24/7-drift og i dag i egen '
         'virksomhed.'),
        ('Central rolle med ansvar for både drift, medarbejdere og kunder',
         'Alle tre i samme rolle i 20+ år: **drift** (24/7 og 11 samtidige projekter), '
         '**medarbejdere** (op til 25 specialister) og **kunder** (egne aftaler og udbud).')])

    m.section('DE FØRSTE 90 DAGE')
    for b in (
        'Kørt arealerne igennem med hver driftsleder og set den samme uge: hvad der er booket, '
        'hvad der bliver skubbet, og hvor materiellet står stille.',
        'Sat én tavle op for afdelingen — kapacitet, aftaler og materiel — og valgt de to ting, der '
        'skal være i orden før sæsonen, med en ejer og en dato.',
        'Lært faget af sjakkene: gået med på opgaver, spurgt til kvalitetskravene i grøn pleje og '
        'vintertjeneste og skrevet kontrolpunkterne ned sammen med dem, der udfører dem.'):
        m.bullet('', b, after=16)

    m.section('DET VILLE JEG SPØRGE OM I EN SAMTALE')
    for b in (
        'Hvor stor en del af Sjællandsomsætningen ligger i dag på faste aftaler — og hvor meget er '
        'enkeltopgaver, der skal planlægges fra uge til uge?',
        'Hvor mange sjak er der i Hedehusene i dag, hvem leder dem, og hvem tager beslutningen, når '
        'en opgave skal skubbes?',
        'Hvilken maskinpark står på Sjælland, og bliver den serviceret lokalt eller sendt vestpå — '
        'det afgør, hvor lang en nedbrudt maskine holder et sjak stille.',
        'Hvordan måler I kvaliteten i grøn pleje i dag: beskrivelseskontrol, runder med '
        'kontrolpunkter eller kundetilfredshed — og hvem fører den opfølgning videre?'):
        m.bullet('', b, after=16)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Tolstrup_AfdelingslederSjaelland.docx')
    build(out)
    print(out)
