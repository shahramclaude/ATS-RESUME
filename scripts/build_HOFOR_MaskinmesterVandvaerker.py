#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Maskinmester til drift af vandværker — HOFOR, Søndersø Vandværk. DANSK.

FORMAT: HOFOR beder EXPLICIT om ikke at skrive en ansøgning, kun sende et
CV med ord på motivationen -> 'MOTIVERET CV': side 1 = motivation (ingen
brevkonventioner: ingen hilsen, ingen 'Ansøgning', ingen afslutning), s. 2-3
= CV, s. 4 = kravmatrix som dokumentation. Masterdesign-beholdes visuelt.

HOFOR: ~1 mio. kunder i/omkring København, ~53 mio. m3 grundvand/år,
moderniserede regionale vandværker + blødgøringsanlæg. Søndersø-værket (i
brug 2022) leverer rent og blødere drikkevand til nordlige København og
Herlev. Team Nord (Vand Drift Produktion), 14 kolleger + team Syd. Leder:
Simon Holm Bek (simbek@hofor.dk, 34 45 81 70) — anerkendende, tilgængelig,
'frihed under ansvar'. Arbejdstid 07.00-15.00 man-tors, 07.00-14.30 fre,
UDEN vagtordning. Frist 13.12.2026; samtaler uge 1 og 2.

KIT-BÆRENDE: maskinmester+elaut. SELVSIKKERT; 2+ års erfaring som
maskinmester (ELOHVAC 2023-2026) SELVSIKKERT; forsyning SELVSIKKERT
(Biofos = kommunejet forsyning) men DRIKKEVAND specifikt = ærligt: fra
spildevandssiden af vandkredsløbet, drikkevandssiden = motivation/lyst
(JD kræver kun interesse + lyst!). SRO-/SCADA-anlæg SELVSIKKERT (Biofos).
Kørekort B manuelt SELVSIKKERT. IT/digitale systemer SELVSIKKERT (SAP
dagligt siden 2017, CMMS, Excel). ENGELSK manualer SELVSIKKERT. Ærligt gap:
blødgøring, forbrugsstoffer, restprodukter = nyt (nævnes åbent). Simon
navngives i motivationen (navngiven kontakt = 'Kære'-regel ikke relevant
uden brev).

STIL (3/3 mod #452 Sweco): register "Stille drift, sikker vandforsyning",
åbning CB (produktet man ikke ser blive lavet), struktur "Værket,
systemerne, forbedringerne". Alle matrix-rækker >= 110 tegn. Ingen em dash.
'brænder'/'dynamisk'/'passioneret'/'gøre en forskel'/'demonstreret'/
'dygtig'/'elinstallatør' findes ikke i dette JD og bruges ikke.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_Gentofte_DriftslederEjendomme_2027.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'HOFOR · Maskinmester · Søndersø Vandværk'
BANNER_RESUME = 'DRIFT · VEDLIGEHOLD · SRO · DRIKKEVAND'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('2. december 2026')
    m.meta('Motiveret CV · Vand Drift Produktion · Team Nord')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Motivation · Maskinmester til drift af vandværker', bold=True,
           color='1A1A1A')

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('Drikkevand er det eneste produkt, folk bruger hver dag uden at '
       'tænke over, hvordan det bliver lavet. HOFOR hvert år indvinder '
       'cirka 53 mio. kubikmeter grundvand og sender rent og blødgjort '
       'drikkevand døgnet rundt ud til cirka 1 million kunder i og omkring '
       'København. Bag hanen står anlæggene: vandværker, der skal driftes, '
       'vedligeholdes og forbedres, hver eneste dag, også når ingen lægger '
       'mærke til det. Jeg søger maskinmesterstillingen ved Søndersø '
       'vandværk, fordi det er dér, jeg gerne vil stå: med ansvaret for '
       'drift og vedligehold af et moderne værk, i tæt samarbejde med en '
       'driftstekniker, med forebyggende og afhjælpende vedligehold og '
       'fejlfinding på tekniske anlæg som kernen i opgaven. Fem opgaver står '
       'i opslaget; alle fem er dele af det arbejde, jeg har gjort i årevis, '
       'kun blødgøringen er ny.')

    lp('SRO-anlægget har jeg betjent og holdt kørende i døgndrift på '
       'Biofos, hvor pumper, procesrør og styring skulle køre, uanset '
       'hvad klokken var. Forsyning har været mit fag siden 2017; jeg '
       'kommer fra spildevandssiden af vandkredsløbet, og drikkevandssiden '
       'er den del, jeg har lyst til at arbejde mig ind i. Vedligehold og '
       'fejlfinding på tekniske anlæg har været mit daglige arbejde i mere '
       'end 20 år, som maskinmester med elautorisation de seneste tre år '
       'hos ELOHVAC, hvor jeg også har planlagt og fordelt arbejdet for '
       'elektrikere og lærlinge. Digitale systemer bruger jeg hver dag: SAP '
       'siden 2017, vedligeholdssystemer, planlægning og dokumentation. '
       'Engelske tekniske manualer og dokumentation har jeg læst i hele mit '
       'arbejdsliv. Koordinering med interne og eksterne leverandører '
       'kender jeg fra både entrepriser og serviceaftaler, og forbedring '
       'af anlæg og arbejdsprocesser har været en fast del af driftsjobbet.')

    lp('HOFOR har, som der står i opslaget, moderniseret flere af vores '
       'regionale vandværker og etableret blødgøringsanlæg, så vandet '
       'gradvist bliver blødere; den udvikling vil jeg gerne være med til '
       'at drive fra maskinrummet. Team Nord løfter opgaven med høj '
       'faglighed inden for drikkevandsproduktion, og de ugentlige '
       'tavlemøder, hvor der er plads til fællesskab, binder os sammen, '
       'selvom mange af os arbejder alene i hverdagen. Psykiske og fysiske arbejdsmiljø er '
       'ikke ord på en væg for mig; det er sådan, man kører et anlæg i '
       'længden. Lederen Simon beskrives som anerkendende og tilgængelig '
       'med frihed under ansvar, og det er netop den ramme, jeg trives '
       'bedst i: at få opgaven og mandatet til at følge den fra start til '
       'slut.')

    lp('Arbejdstiden er fast, og stillingen er uden vagtordning; efter år '
       'med vagt i servicebranchen værdsætter jeg en arbejdsdag, der '
       'slutter til tiden. Med kørekort kategori B (manuelt gear) i hånden er '
       'både Søndersø-værket og de øvrige vandværker, jeg kan komme '
       'til at arbejde på, til at nå. Blødgøring, forbrugsstoffer og '
       'afsætning af restprodukter er nyt for mig; den del tager jeg fat '
       'på fra første uge. Skulle der være spørgsmål til min vej til '
       'jobbet, svarer jeg gerne. Jeg glæder mig til en samtale.', after=44)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Maskinmester med elautorisation og 20+ år i tekniske anlæg: '
           'drift, vedligehold og fejlfinding på pumper, ventilation, rør '
           'og el. SRO-/SCADA-anlæg betjent i døgndrift, og digital '
           'planlægning og dokumentation er en naturlig del af arbejdet.',
           after=32)
    m.para('Forsyning siden 2017; søger mod drikkevandssiden, fordi '
           'vandforsyning er et spændende område, og produktionen af '
           'drikkevand er noget, man kan stå inde for hver '
           'dag. Struktureret og vant til at følge opgaver fra start til '
           'slut, også når de trækker ud.',
           after=32)

    jobs = [
        ('Drifts- og serviceleder · elautoriseret maskinmester',
         'ELOHVAC · Ballerup · maj 2023 – nov. 2026',
         '5 elektrikere og 3 lærlinge · service, installation og projekter',
         [('Vedligehold og fejlfinding',
           'Forebyggende og afhjælpende vedligehold på el, VVS og '
           'ventilation, og fejlfinding på tekniske anlæg hos kunderne. '
           'Serviceaftaler kørt med planlagte besøg og hurtig udrykning, '
           'når noget gik ned.'),
          ('Planlægning og koordinering',
           'Arbejde fordelt mellem otte mand, aftaler med leverandører og '
           'underentreprenører koordineret, og opgaver fulgt fra start '
           'til slut. Digital dokumentation af alt udført arbejde.')]),
        ('Commissioning Manager',
         'Novo Nordisk · Hillerød · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, 2-10 mio. kr. · 25 specialister · GMP, IQ/OQ/PQ',
         [('Idriftsættelse',
           'Kritiske anlæg idriftsat og testet, dokumentation og '
           'frigivelse fulgt til dørs. Fejlfinding under commissioning, '
           'og koordinering af leverandører på tværs af fag.'),
          ('Kvalitet og dokumentation',
           'KS, IQ/OQ/PQ og frigivelse fulgt for 37 leverancer; '
           'dokumentation, der kan bruges, også bagefter.')]),
        ('Overmontør og entrepriseleder',
         'Ventek · Taastrup · jan. 2022 – nov. 2022',
         '11 projekter · 14 mand og underentreprenører',
         [('Tilsyn og opfølgning',
           'Installationer fulgt på byggeplads: kvalitet, tid og '
           'sikkerhed. Leverandører og underentreprenører koordineret, '
           'så arbejdet kunne køre i fast rytme.'),
          ('Planlægning',
           'Mandskab, materiel og tid planlagt for 14 mand, så flere hold '
           'kunne arbejde parallelt på samme adresse.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · kritiske anlæg · 10 medarbejdere · skiftehold',
         [('Drift og SRO',
           'Pumper, procesrør, el, SCADA og PLC holdt kørende døgnet '
           'rundt. SRO-anlæg betjent, fejlfinding på anlæggene udført, '
           'og forebyggende vedligehold planlagt på fejldata.'),
          ('Mandskab',
           'Arbejde fordelt for 10 medarbejdere på skiftehold, og '
           'aftaler med eksterne leverandører om service og reservedele.')]),
        ('CTO og stifter',
         'Data Power · Måløv · jan. 2024 – nu',
         'AI-udvikling, analyse og forretningsstrategi',
         [('Digitale værktøjer',
           'AI som hjælpeværktøj til analyse og dokumentation, og '
           'systemer til planlægning af eget arbejde. IT-færdigheder i '
           'daglig brug, ikke på hylden.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('Produktion og vedligehold',
           'Maskiner og anlæg vedligeholdt og repareret i værkstedet, '
           'og nye medarbejdere oplært i arbejdsgangene. Eget og andres '
           'arbejde planlagt for 12 mand.'),
          ('Oplæring',
           'Nye medarbejdere oplært i arbejdsgangene, så de kunne tage '
           'fat med det samme.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.edu('B.Tech (EQF6), teknologiledelse og maskinteknik',
          'Danmark · 2017–2022 · karakter 7,6')
    m.edu('Dansk elautorisation LV/MV/HV som elautoriseret maskinmester',
          'Sikkerhedsstyrelsen · maj 2023')
    m.edu('El- og maskinteknisk design, elteknik (EQF6)',
          'Tehran Technical University · 2000–2003')
    m.edu('PRINCE2, certificeret projektleder', 'AXELOS / PeopleCert')
    m.edu('Køleteknik og klimaanlæg (AMU)',
          'Mercantec · 2021 · STCW 2021–2023, Søfartsstyrelsen')

    m.section('ARBEJDSMÅDE')
    m.bullet('Drift og vedligehold', 'Forebyggende og afhjælpende '
             'vedligehold, fejlfinding på tekniske anlæg, og dokumentation '
             'af det udførte arbejde.', after=10)
    m.bullet('SRO og systemer', 'SRO-/SCADA-anlæg betjent i drift, SAP '
             'og vedligeholdssystemer brugt til planlægning og '
             'dokumentation.', after=10)
    m.bullet('Planlægning', 'Eget og andres arbejde fordelt og fulgt fra '
             'start til slut; struktur i hverdagen, så opgaverne ikke '
             'hober sig op.', after=10)
    m.bullet('Samarbejde', 'Driftsteknikere, elektrikere, lærlinge og '
             'leverandører i samme løsning. Sparring i hverdagen, og '
             'tavlemøder som fast holdepunkt.', after=10)

    m.section('FØRSTE 90 DAGE · VÆRKET, SYSTEMERNE, FORBEDRINGERNE')
    m.bullet('Måned 1 · værket', 'Søndersø-værket lært at kende anlæg for '
             'anlæg sammen med driftsteknikeren, og driftens rutiner og '
             'vedligeholdsplaner sat ind i.', after=10)
    m.bullet('Måned 2 · systemerne', 'SRO-anlæg og digitale systemer i '
             'daglig brug, så planlægning og dokumentation kører, og '
             'arbejdet kan fordeles mellem os.', after=10)
    m.bullet('Måned 3 · forbedringerne', 'Forbedringer af anlæg og '
             'arbejdsprocesser sat i gang, leverandørsamarbejdet strammet '
             'op, og blødgøringsdelen med forbrugsstoffer og restprodukter '
             'lært.', after=10)

    m.section('SPROG, IT OG PRAKTISK')
    m.para('Dansk (modersmål) · engelsk (professionelt, tekniske manualer '
           'er hverdag) · persisk (modersmål). SAP, CMMS, Excel, '
           'AI-værktøjer; PRINCE2. Kørekort kategori B (manuelt gear). '
           'Bosat i Måløv.', after=8)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Krav og dokumentation · Maskinmester, HOFOR',
                   ('Krav i opslaget', 'Dokumentation'),
                   [
        ('Minimum 2 års erfaring som maskinmester',
         'Tre år som maskinmester med elautorisation (ELOHVAC 2023-2026) '
         'og mere end 20 år med tekniske anlæg før det: drift, '
         'vedligehold og fejlfinding som daglig kerne i alle roller.'),
        ('Vandforsyning er et spændende område, og lyst til at bidrage til '
         'produktionen af drikkevand',
         'Forsyning som fag siden 2017 (Biofos, kommunejet forsyning) fra '
         'spildevandssiden af vandkredsløbet. Drikkevandssiden er '
         'netop derfor den, jeg har lyst til at arbejde videre med.'),
        ('Forebyggende og afhjælpende vedligehold samt fejlfinding på '
         'tekniske anlæg',
         'Forebyggende vedligehold planlagt på fejldata (Biofos 2017-2022), '
         'afhjælpende vedligehold og fejlfinding på pumper, ventilation, '
         'rør og el (ELOHVAC 2023-2026, ARJ 2003-2010).'),
        ('Betjener SRO-anlæg',
         'SRO-/SCADA-anlæg og PLC-styring betjent og holdt kørende i '
         'døgndrift på Biofos (2017-2022), med overvågning af pumper og '
         'procesanlæg som del af driften.'),
        ('Koordinerer samarbejde med interne og eksterne leverandører',
         'Leverandører og underentreprenører koordineret på entrepriser '
         '(Ventek 2022) og i serviceaftaler (ELOHVAC 2023-2026), fra '
         'aftale til færdig opgave.'),
        ('Forbedrer anlæg og arbejdsprocesser',
         'Forbedringer gennemført i driften: vedligehold styret af '
         'fejldata, reservedelsstyring og arbejdsgange, der sparede tid '
         '(Biofos 2017-2022).'),
        ('Modtager forbrugsstoffer til blødgøring og står for afsætning af '
         'restprodukter',
         'Blødgøring, forbrugsstoffer og restprodukter er nyt for mig; '
         'logistikken omkring modtagelse og afsætning tager jeg fat på fra '
         'første uge og lærer i driften.'),
        ('Gyldigt kørekort til personbil (kategori B) og arbejde på øvrige '
         'vandværker',
         'Bilen og kortet er i orden med kategori B (manuelt gear), og kørsel '
         'mellem arbejdssteder har været fast del af hverdagen i mere end '
         '20 år. HOFORs øvrige værker i hovedstadsområdet kan nås.'),
        ('Trives med digitale systemer og har gode IT-færdigheder til '
         'planlægning, dokumentation og vedligehold',
         'SAP brugt dagligt siden 2017, CMMS til vedligeholdsstyring, '
         'Excel og AI-værktøjer. Planlægning og dokumentation i digitale '
         'systemer er hverdagsværktøjer.'),
        ('Tale og skrive dansk og læse tekniske manualer og dokumentation '
         'på engelsk',
         'Dansk som modersmål, og engelsk som professionelt arbejdssprog '
         'med tekniske manualer og dokumentation læst gennem hele '
         'karrieren.'),
        ('Planlægge og fordele eget og andres arbejde og gennemføre '
         'opgaverne fra start til slut',
         'Arbejde fordelt for 12 mekanikere (ARJ 2003-2010), 10 på '
         'skiftehold (Biofos 2017-2022) og 8 i teknisk afdeling (ELOHVAC '
         '2023-2026). Opgaver fulgt til afslutning, også når det trak ud.'),
        ('Arbejder struktureret',
         'PRINCE2 som strukturramme, faste rutiner for planlægning og '
         'dokumentation, og orden i arbejdet, så andre kan overtage '
         'opgaverne.'),
        ('Gode samarbejdsevner',
         'Samarbejde med kolleger på tværs af fag i alle roller: '
         'driftsteknikere, elektrikere, lærlinge, underentreprenører og '
         'kunder i samme løsning.'),
        ('Tæt samarbejde med en driftstekniker',
         'Par-arbejde i driften fra Biofos, hvor arbejdet blev fordelt og '
         'aftalt, og hvor man hjalp hinanden, når anlæggene drillede.'),
        ('Team Nord i Vand Drift Produktion med samarbejde til team Syd',
         'Teamånd i drift er et vilkår, jeg kender: 10 medarbejdere på '
         'skiftehold (Biofos) og 8 i teknisk afdeling (ELOHVAC). '
         'Tavlemøder og fællesskab passer til min måde at arbejde på.'),
        ('Arbejdstid 07.00-15.00 man-tors og 07.00-14.30 fre, uden '
         'vagtordning',
         'Faste tider uden vagt passer til min hverdag; efter år med '
         'vagtordning i servicebranchen er det en klar fordel ved '
         'stillingen.'),
        ('Erfaring fra mange forskellige brancher',
         'Min erfaring spænder fra maskinværksted og produktion (ARJ '
         '2003-2010) over commissioning i medicinalindustrien (Novo '
         '2022-2024) til service og drift (ELOHVAC 2023-2026). Brancherne '
         'er forskellige; opgaverne med at holde tekniske anlæg kørende '
         'er de samme.'),
        ('Lyst til at bidrage til produktionen af drikkevand til kunderne',
         'At være med til at sikre drikkevand til cirka 1 million kunder '
         'er en opgave, jeg rigtig gerne vil ind i. Lysten til at bidrage '
         'til produktionen er motivationen bag ansøgningen, ikke bare ord.'),
        ('Arbejde på nogle af vores øvrige vandværker',
         'Jeg er vant til at køre mellem adresser; servicearbejde har '
         'altid foregået på skiftende lokationer, og nye værker er kun '
         'spændende at lære at kende.'),
        ('Gode IT-færdigheder til planlægning, dokumentation og '
         'vedligehold',
         'IT er arbejdsredskab og ikke pynt: SAP brugt dagligt siden '
         '2017, CMMS til vedligeholdsstyring, Excel til opgørelser, og '
         'nye systemer samles hurtigt op.'),
        ('Ansvar for at gennemføre opgaverne fra start til slut',
         'Opgaver følger jeg til dørs, også når de trækker ud: 37 '
         'commissioning-leverancer afleveret (Novo 2022-2024), og '
         'serviceaftaler fulgt til afslutning hver gang.'),
        ('Erfaring med tekniske anlæg i drift og vedligehold',
         'El, VVS, ventilation, pumper, procesrør og styring: tekniske '
         'anlæg i drift og vedligehold har været omdrejningspunktet i '
         'alle seks job, fra værksted til døgndrift.'),
                   ],
                   widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo · Motiveret CV · Maskinmester, HOFOR')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_HOFOR_MaskinmesterVandvaerker.docx')
    build(out)
    print(out)
