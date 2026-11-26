# -*- coding: utf-8 -*-
"""Indeklima- og energiingeniør med fagansvar — Sweco (dansk opslag -> dansk dokument).

4 sider i masterdesign: brev side 1, CV side 2-3, kravmatrix side 4.
Kontakt fra opslaget: teamchef Maria Hansen (maria.hansen@sweco.dk) -> hilsen "Kære Maria Hansen,".

STILVALG (style_guard godkendt, 3/3 skift mod #423 Microsoft Quantum):
  register     = Sunde bygninger, åbent fag (indeklima · energi · komfort · bæredygtighed ·
                 videndeling)
  åbningsgreb  = AY (mennesket som måleapparat: indeklimaet læses i kroppen på dem, der
                 sidder i rummet; beregningerne er oversættelsen)
  struktur     = Fag, projekt, marked (fagudvikling · projekterne · kunderne)

BRUGERENS KORREKTION + permanent regel: alt tekst humaniseret i brev OG CV.
Ingen em dash. Varieret rytme, sammentrækninger, konkret før generelt.

BRUGERBEKRÆFTET 25.11.2026:
  - Indeklimaberegninger/-analyser/-rådgivning i ALLE stillinger siden 2003; emner = alle emner
    i energi (komfort, luftkvalitet, bygningers ydeevne dækket). Dagslys, akustik, fugt IKKE
    kerneberegninger -> ærlig grænse i brev OG matrix.
  - B.Tech + EQF6 elteknik + elautorisation dækker "tilsvarende teknisk uddannelse".
  - Byg ansøgningen (ikke spring over).
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Sweco · Indeklima- og energiingeniør med fagansvar'
BANNER_RESUME = 'Indeklima, energi og installationer · fagligt ansvar'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('25. november 2026')
    m.meta('Rådgivning · indeklima og energi med fagansvar i Sweco')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Indeklima- og energiingeniør med fagansvar', bold=True, color='1A1A1A')
    m.para('Kære Maria Hansen,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('Et indeklima findes ikke først i et regneark. Det findes i et klasselokale klokken '
       'elleve, hvor eleverne stadig kan koncentrere sig, og på en hospitalsstue, hvor luften '
       'og temperaturen bare er der. Bag hvert af de rum ligger beregninger, valg og et '
       'fagligt ansvar, der skal holde hele vejen fra den tidlige analyse til afleveringen. '
       'Et sundt og velfungerende indeklima er kort sagt noget, man mærker, længe før man '
       'lægger mærke til det, og jeg har brugt hele mit arbejdsliv på den slags usynlige '
       'resultater.')

    lp('Sweco planlægger og designer fremtidens bæredygtige samfund og byer under overskriften '
       'Transforming Society Together, og den grønne omstilling er ikke en bonus i jeres '
       'portefølje, men selve opgaven. Opgaverne spænder fra store, komplekse byggerier til '
       'mindre sager for både offentlige og private bygherrer, i nybyggeri og renovering af '
       'boliger, skoler og hospitaler, og jeg kender den virkelighed fra installations- og '
       'energisiden: ventilation, klima og el i bygninger, der skal fungere, mens folk er i '
       'dem. Rollen som indeklima- og energiingeniør og fagansvarlig er den kombination af '
       'projekter og fagudvikling, jeg har ledt efter.')

    lp('Spørgsmålet i toppen af opslaget, om jeg motiveres af at skabe sunde, komfortable, '
       'energieffektive og bæredygtige bygninger, kan jeg svare ja til uden at tøve. '
       'Indeklimaberegninger, analyser og vurderinger har fulgt mit arbejde på tværs af alle '
       'mine stillinger siden 2003, og emnerne har været dem, der fylder i en bygning: '
       'termisk komfort, luftkvalitet og energiforbrug. Bygningers ydeevne har jeg set fra '
       'både drift, projektering og rådgivning, og sammenhængen mellem bygningens arkitektur, '
       'materialer, installationer og brugeradfærd er noget, jeg har måttet forholde mig til '
       'hver gang, en løsning skulle virke i praksis. Energieffektivitet og bæredygtighed '
       'blev målbar for mig hos Novo Nordisk, hvor et PDCA-forløb skar 40 procent af '
       'energiomkostningerne.')

    lp('Der er også en ærlig grænse, og den skriver jeg selv. Dagslys, akustik og fugt er '
       'ikke mine kerneberegninger endnu; komfort, luftkvalitet og energi er. De øvrige emner '
       'tager jeg med i samarbejdet med kollegerne fra dag ét, og jeg lærer hurtigt, når '
       'faget er sat ordentligt i system. Uddannelseskravet ser jeg som opfyldt via den '
       'tilsvarende tekniske uddannelse, jeg har: en B.Tech (EQF6) i teknologiledelse og '
       'maskinteknik, EQF6 i elteknik og en elautoriseret maskinmesteruddannelse, alt sammen '
       'suppleret af 20+ års praktisk ingeniørarbejde. Bor i Måløv, har kørekort B, og jeg '
       'kan tiltræde hurtigst muligt.')

    lp('Det, der trækker mest ved stillingen, er de to ben på én gang: at være faglig '
       'sparringspartner og drive faglig udvikling på tværs af Sweco, og stadig have hænderne '
       'i projekterne som fagprojektleder med ansvar for tid, økonomi og kvalitet. Jeg har '
       'kørt begge dele før, som ejer og som projektleder: tilbud, kundedialog og udvikling '
       'af nye opgaver den ene dag, beregninger og tilsyn den næste. At identificere nye '
       'markedsmuligheder og omsætte kundernes behov til konkrete løsninger og ydelser er '
       'ikke fremmed for mig, og at skabe tillid hos både kunder, samarbejdspartnere og '
       'kolleger har været den eneste måde, mine aftaler er blevet fornyet på.')

    lp('Jeg trives i et miljø med mange forskellige opgaver, højt tempo og tværfagligt '
       'samarbejde, og jeg kan genkende mig selv i beskrivelsen af en konstruktiv og '
       'engageret samarbejdspartner med en positiv tilgang. Et fagligt stærkt og engageret '
       'miljø med høje ambitioner og balance mellem arbejdsliv og fritid er præcis den '
       'ramme, jeg arbejder bedst i, og synlige resultater både i projekterne og i '
       'organisationen er en målestok, jeg gerne står på mål for. Særligt fokus på kvaliteten '
       'af indeklimaet er en selvfølge for mig. Jeg kan tiltræde hurtigst muligt og svarer '
       'gerne på spørgsmål inden samtalen.', after=44)

    m.para('Med venlig hilsen', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Ingeniørprofil med indeklima, energi og installationer som omdrejningspunkt. '
           'Indeklimaberegninger, analyser og rådgivning på tværs af alle stillinger siden '
           '2003: komfort, luftkvalitet og bygningers ydeevne fra ventilation, klima, el og '
           'energiprojekter. Vant til fagprojektledelse med ansvar for tid, økonomi og '
           'kvalitet og til at få et fagligt emne til at leve på tværs af kolleger.', after=32)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester (el-teknik og ventilation)',
         'Data Power Consultant ApS · København · 2024 – nu (fra nov. 2026 også ELOHVACs '
         'el-tekniske aktiviteter)',
         'AI-afdeling 4-10 personer · el-service og entreprise · 5 elektrikere + 3 lærlinge',
         [('Faglig udvikling og værktøjer', 'Metoder og digitale værktøjer udviklet til '
           'afdelingen: AI-assisteret udvikling, tjeklister og rapportflow i Python. Faglig '
           'sparring med kolleger dagligt, og investeringstilbud med månedlig opfølgning.'),
          ('Service i bygninger', 'El-service og fejlfinding hos erhvervskunder: tavler, '
           'styring og forebyggende vedligehold på el, ventilation og klima i bygninger, der '
           'var i brug, mens vi arbejdede.')]),
        ('Ejer / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 – nov. 2026 (virksomheden lukket)',
         'Erhvervskunder · el, ventilation og klima · entreprise · fuldt P&L · serviceaftaler',
         [('Indeklima i praksis', 'Projektering og installation af el, ventilation og klima i '
           'erhvervsbygninger: komfort og luftkvalitet i løsningerne, indeklimaberegninger og '
           '-vurderinger som del af tilbud og udførelse. Fra akutte udkald til afleveret anlæg.'),
          ('Kunder og ydelser', 'Tilbud, prisfastsættelse, kundedialog og udvikling af nye '
           'opgaver. Serviceaftaler med mål på responstid, kvalitet og leveringsevne; aftalerne '
           'blev fornyet, fordi kunderne fik det, de blev lovet.'),
          ('Fagligt ansvar', '5 elektrikere og 3 lærlinge med struktureret oplæring og faglig '
           'sparring. Ensartet niveau sikret gennem standarder; nul kritiske afvigelser i '
           'serviceaftalerne.')]),
        ('Senior commissioningeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, DKK 2-10 mio. · 25 specialister · GMP/FDA/EMA',
         [('Energi og ydeevne', 'PDCA-forløb med 40% lavere energiomkostninger som målbart '
           'resultat. Bygningers ydeevne vurderet i drift og commissioning, med energiforbrug '
           'og anlæggenes funktion som fælles målestok.'),
          ('Fagprojektledelse', '37 projekter styret på tid, økonomi og kvalitet, med 25 '
           'specialister på tværs af engineering, indkøb og drift, og nul kritiske fund ved '
           'aflevering. SAP ERP og PRINCE2 som struktur.')]),
        ('Projekt- og værkstedsleder', 'Ventek-Air · København · jan. 2022 – nov. 2022',
         '11 samtidige ventilationsprojekter · 14 mand · underleverandører',
         [('Byggeri og ventilation', '11 samtidige projekter med ventilation i bygninger for '
           'offentlige og private bygherrer. Tilbud og udbud, aftalegrundlag, '
           'underentreprenører og sikkerhedsdokumentation fulgt til dørs.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · SCADA, PLC, HV-tavler · skiftehold',
         [('Drift og indeklima', 'Drift, overvågning og vedligehold af pumper, HVAC, HV-tavler, '
           'SCADA og PLC døgnet rundt. Komfort og luftkvalitet i anlæggene læst gennem målinger '
           'og erfaring; fejlfinding på stedet, 5S og Standard Work i værkstedet.'),
          ('Sikkerhed og standarder', 'Skiftehold og vagt med LOTO, APV og nærved-hændelser. '
           'Fagligt niveau holdt ved lige gennem oplæring og faste rutiner.')]),
        ('Elektromekanisk tekniker / produktionsleder', 'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('Grundlaget', 'Ledelse af 12 mekanikere og teknikere: vagtplan, materialer og mål. '
           'Fejlsøgning på industrielt udstyr, rodårsag og korrigerende handlinger.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('UDDANNELSE OG CERTIFIKATER')
    m.edu('B.Tech (EQF6), teknologiledelse og maskinteknik',
          'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12')
    m.edu('Dansk elautorisation LV/MV/HV som elautoriseret maskinmester', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('El- og maskinteknisk design, elteknik (EQF6)', 'Tehran Technical University · 2000–2003')
    m.edu('PRINCE2, certificeret projektleder', 'AXELOS / PeopleCert')
    m.edu('Køleteknik og klimaanlæg (AMU)', 'Mercantec · 2021 · STCW 2021–2023, Søfartsstyrelsen')

    m.section('KOMPETENCER')
    m.bullet('Indeklima og beregninger', 'Erfaringen med indeklimaberegninger, analyser og '
             'vurderinger spænder over alle stillinger siden 2003: termisk komfort, luftkvalitet, energiforbrug '
             'og bygningers ydeevne. Dagslys, akustik og fugt tages i samarbejde med fagkolleger.',
             after=10)
    m.bullet('Projektering og installationer', 'Tekniske installationer i bygninger: el, '
             'ventilation og klima projekteret og udført i nybyggeri og renovering. '
             'Sammenhængen mellem arkitektur, materialer, installationer og brugeradfærd '
             'vurderet konkret i opgaverne.', after=10)
    m.bullet('Fagprojektledelse', 'Ansvar for tid, økonomi og kvalitet på projekter fra 2 til '
             '37 ad gangen. PRINCE2, tavler og faste opfølgningsrutiner; kvalitet der holdt for '
             'GMP-krav og egne standarder.', after=10)
    m.bullet('Kunder og ydelser', 'Tilbud, kundedialog og salg af rådgiverydelser, '
             'markedsmuligheder omsat til konkrete ydelser. Lean- og Six Sigma-praksis uden '
             'certifikat: DMAIC, 5S, PDCA, VSM, A3, Kaizen, Standard Work, SMED, TPM, 5xHvorfor, '
             'Ishikawa og FMEA.', after=10)

    m.section('DE FØRSTE 90 DAGE')
    m.para('En plan i tre trin, svarende til stillingens tre ben:', after=8)
    m.bullet('Dag 1-30 · Faget', 'Fagmiljøet, metoderne og de igangværende projekter lært at '
             'kende: hvordan beregninger, analyser og vurderinger laves hos Sweco, og hvor jeg '
             'kan byde ind fra start. Mål: overblik over fagets praksis og mine første '
             'bidrag.', after=10)
    m.bullet('Dag 31-60 · Projektet', 'Fagprojektleder-ansvar taget på egne opgaver med ansvar '
             'for tid, økonomi og kvalitet, og faglig sparring for kolleger og projektledere i '
             'gang. Mål: egne projekter på sporet, og et fagligt spørgsmål løst for en kollega.',
             after=10)
    m.bullet('Dag 61-90 · Markedet', 'Tilbud, kundedialog og udvikling af nye opgaver: '
             'ydelserne inden for indeklima og energi synliggjort internt og eksternt, og '
             'første markedsmulighed omsat til et konkret tilbud. Mål: ét nyt tilbud og ét '
             'oplæg om faget.', after=10)

    m.section('SPROG, VÆRKTØJER OG PRAKTISK')
    m.para('Dansk (modersmål, flydende skrift og tale) · engelsk (professionelt) · persisk '
           '(modersmål). SAP ERP, SCADA, PLC, Power BI, Python og AI-værktøjer. PRINCE2. '
           'Kørekort kategori B (manuelt gear). Bor i Måløv og kører gerne til opgaver på '
           'Sjælland. Kan tiltræde hurtigst muligt.', after=32)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Indeklima og energi · krav og dokumentation',
                   ('Krav i opslaget', 'Dokumenteret erfaring'),
                   [
        ('Drive den faglige udvikling inden for indeklima og energi på tværs af Sweco',
         'Faglig udvikling drevet før: nye metoder indført som ejer (tjeklister, digitale '
         'arbejdsgange, 2023-2026), standarder udviklet hos Biofos (2017-2022) og AI-værktøjer '
         'gjort til fælles praksis i en hel afdeling (2024-2026).'),
        ('Være faglig sparringspartner for kolleger, projektledere og afdelinger',
         'Sparringspartner for kolleger og projektledere siden 2010: undervisning af elektrikere '
         'og lærlinge, faglig sparring på tværs af engineering, indkøb og drift hos Novo Nordisk '
         '(25 specialister, 2022-2024) og daglig teknisk dialog i ELOHVAC.'),
        ('Udvikle, kvalificere og udbrede metoder, værktøjer og koncepter',
         'Metoder og værktøjer udviklet og udbredt: 5S og Standard Work hos Biofos, KS-tjeklister '
         'og servicekoncepter i ELOHVAC, digitale værktøjer i Python (2024-2026). Kvalificeret '
         'før udbredt, testet i drift.'),
        ('Bidrage til projektering af tekniske installationer, så de understøtter et sundt, komfortabelt og energieffektivt indeklima',
         'Projektering og installationer, der understøtter et sundt og energieffektivt indeklima: '
         'ventilation, klima og el i bygninger (Ventek 2022, ELOHVAC 2023-2026) og tekniske anlæg '
         'i procesindustrien (Novo Nordisk, 2022-2024).'),
        ('Varetage indeklimaberegninger, analyser og vurderinger',
         'Mine indeklimaberegninger, analyser og vurderinger har fulgt arbejdet på tværs af alle mine '
         'stillinger siden 2003: komfort, luftkvalitet og bygningers ydeevne vurderet i projekter '
         'og serviceaftaler, altid med beregningerne som grundlag for anbefalingen.'),
        ('termisk komfort, luftkvalitet, dagslys, akustik, fugt og energiforbrug',
         'Termisk komfort, luftkvalitet og energiforbrug er mine kerneemner (ventilation, klima '
         'og energi siden 2003; energiforbrug målbart: 40% reduktion hos Novo Nordisk). Ærligt: '
         'dagslys, akustik og fugt er ikke mine kerneberegninger endnu.'),
        ('Agere fagprojektleder på større og mindre projekter med ansvar for tid, økonomi og kvalitet',
         'Fagprojektledelse i praksis: 37 CAPEX-projekter på tid, økonomi og kvalitet (Novo '
         'Nordisk, 2022-2024), 11 samtidige projekter (Ventek, 2022) og fuldt P&L-ansvar '
         '(ELOHVAC, 2023-2026). PRINCE2 som struktur.'),
        ('Sikre et højt og ensartet fagligt niveau i projekterne',
         'Ensartet fagligt niveau sikret gennem standarder og opfølgning: FAT/SAT og IQ/OQ/PQ med '
         'nul kritiske fund (2022-2024), nul kritiske afvigelser i serviceaftalerne (2023-2026), '
         'oplæring af 5 elektrikere og 3 lærlinge.'),
        ('Bidrage til tilbud, kundedialog og udvikling af nye opgaver',
         'Tilbud og kundedialog som dagligt sprog: tilbudsberegning, prisfastsættelse og udvikling '
         'af nye opgaver hos ELOHVAC (2023-2026), investeringstilbud i Data Power og udbud hos '
         'Ventek (2022).'),
        ('Synliggøre og sælge Swecos ydelser inden for indeklima og energi',
         'Synliggørelse og salg af rådgiverydelser: serviceaftaler solgt og fornyet på tillid '
         '(2023-2026), kunder præsenteret for løsninger, de ikke selv havde set, og målbare '
         'effekter brugt som argument.'),
        ('Identificere nye markedsmuligheder og omsætte kundernes behov til konkrete løsninger og ydelser',
         'Markedsmuligheder omsat til ydelser: energiløsninger med målt effekt (Novo Nordisk, 40% '
         'lavere energiomkostninger), nye servicekoncepter i ELOHVAC og AI-baserede ydelser i Data '
         'Power. Kundernes behov blev til konkrete tilbud.'),
        ('Formidle din faglighed klart og inspirerende gennem oplæg, sparring og videndeling',
         'Formidling i hverdagen: oplæg og undervisning for elektrikere og lærlinge, '
         'månedsrapporter til bygherre og ledelse (2022-2024) og videndeling gennem skrevne '
         'procedurer, andre faktisk bruger.'),
        ('uddannet diplomingeniør, civilingeniør eller har en tilsvarende teknisk uddannelse',
         'Tilsvarende teknisk uddannelse: B.Tech (EQF6) i teknologiledelse og maskinteknik, EQF6 i '
         'elteknik og elautoriseret maskinmester (LV/MV/HV), suppleret af 20+ års praktisk '
         'ingeniørarbejde siden 2003.'),
        ('mindst fem års erfaring med indeklima, herunder analyser, beregninger og rådgivning om komfort, luftkvalitet og bygningers ydeevne',
         'Femårs-kravet er indfriet mange gange: komfort, luftkvalitet og bygningers ydeevne har '
         'været en del af arbejdet i alle stillinger siden 2003, som rådgiver, entreprenør og '
         'driftsansvarlig. Mere end 20 år med indeklima i praksis.'),
        ('bygningens arkitektur, materialer, installationer og brugeradfærd påvirker indeklimaet og energiforbruget',
         'Sammenhængen set indefra: installationer i eksisterende bygninger (ELOHVAC, 2023-2026), '
         'ventilationsprojekter i byggeri (Ventek, 2022) og energioptimering, hvor bygning og '
         'adfærd skulle spille sammen (Novo Nordisk, PDCA).'),
        ('erfaring med eller interesse for faglig ledelse, udvikling og videndeling',
         'Faglig ledelse: 5 elektrikere og 3 lærlinge med struktureret oplæring (2023-2026), 25 '
         'specialister på tværs af fag (2022-2024) og en AI-afdeling på 4-10 personer (2024-2026). '
         'Udvikling og videndeling har været målet.'),
        ('kundedialog, tilbudsarbejde og salg af rådgiverydelser',
         'Kundedialog, tilbud og salg i 3+ år som selvstændig: forhandling om aftaler og priser, '
         'serviceaftaler med mål på responstid, og rådgivning kunderne kom tilbage efter.'),
        ('Arbejder struktureret og tager ansvar for kvalitet, økonomi og fremdrift',
         'Struktur og ansvar dokumenteret: PRINCE2 siden 2017, daglige tavler, månedlig '
         'budgetopfølgning (2023-2026) og kvalitet, der holdt for både GMP-krav og egne '
         'standarder.'),
        ('konstruktiv og engageret samarbejdspartner med en positiv tilgang',
         'Konstruktiv og engageret: jeg er den, der kommer med forslag i stedet for klager. '
         'Samarbejde på tværs af fag siden 2003; relationer der holder, aftaler der blev fornyet.'),
                   ], widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo — ansøgning som indeklima- og energiingeniør med '
                       'fagansvar, Sweco')
    print(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_Sweco_IndeklimaEnergiingenioerFagansvar.docx'))
