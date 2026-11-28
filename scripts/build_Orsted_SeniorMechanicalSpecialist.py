# -*- coding: utf-8 -*-
"""Senior Mechanical Specialist — Ørsted Bioenergy & Thermal Power A/S (Skærbæk / Avedøre).

Dansk opslag -> dansk dokument. Masterdesign (scripts/master_design.py):
brev side 1, CV side 2-3, kravmatrix side 4.

Kun fakta fra master-CV'et, de tidligere resumeer og brugerens svar 28.11.2026.
Ikke erfaring: kraftværk, dampturbiner, forbrændingssystemer, CO2-fangst,
kedelpassercertifikat, tekniske specifikationer som dokumenteret opgave.
Uddannelse: B.Tech (EQF6) som i de tidligere resumeer. Ikke master.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
OUT_DIR = os.path.join(ROOT, 'output')
OUT = os.path.join(OUT_DIR, 'Shahram_Ajloo_Orsted_SeniorMechanicalSpecialist.docx')

NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Senior Mechanical Specialist · Skærbæk og Avedøre'
BANNER_RESUME = 'Mekaniske systemer, drift og dokumentation · kraftvarme'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('28. november 2026')
    m.meta('Ørsted Bioenergy & Thermal Power A/S · Skærbæk og Avedøre')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Senior Mechanical Specialist · Ørsted', bold=True, size=28, color='C00000')
    m.para('Kære rekrutteringsteam hos Ørsted,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    def sub(text):
        p = m._p(spacing_after=20, spacing_before=60, line=260, justify=False, keep_next=True)
        m._run(p, text, bold=True, color='002B5C')
        return p

    # ------------------------------------------------------------ brev, side 1
    lp('Avedøre og Skærbæk kører hovedsageligt på biomasse, og Ørsted bygger CO₂-fangst på '
       'Avedøres halmfyrede enhed med drift fra 2027. Opslaget handler om sikker og effektiv '
       'drift i dag og om fremtidens energianlæg. En mekanisk specialist skal holde systemerne '
       'kørende og få anlægsdokumentationen på plads, så ombygningerne kan bygges på en '
       'historik, man kan stole på. Det er den opgave, jeg vil starte med.')

    sub('Driften først')
    lp('Når en fejl kommer tilbage, er det ofte, fordi årsagen blev fjernet på det, der stod '
       'tydeligst, og ikke på det, der gik i stykker. Derfor ville jeg i de første fire uger '
       'lave en fejlliste pr. system sammen med driftsteamet, sorteret efter driftsstop og '
       'gentagelser, og gennemgå den med FMEA. Den anden vej er at gå direkte til de store '
       'komponenter og planlægge udskiftninger med det samme. Jeg vælger den første, fordi den '
       'viser, hvor tiden går tabt, før der bruges penge. En fejlliste holder kun, hvis folk, der '
       'har stået ved anlægget, er med, og det kræver en stærk holdånd og et team, der støtter '
       'hinandens faglige udvikling.')

    sub('Ombygninger og CAPEX')
    lp('På et værk, der skal køre hver dag, er den største risiko normalt stoptiden, ikke '
       'prisen på udstyret. Jeg ville lave en investeringscase pr. ombygning med NPV, IRR og '
       'følsomhed på driftsstop, og sammenligne to løsninger: trinvis udskiftning i planlagte '
       'stop, eller én samlet ombygning i et længere stop. Jeg anbefaler trinvis. Driftsdata '
       'fra første trin bruges til at rette andet trin, og produktionen står stille i kortere '
       'perioder.')
    lp('Jeg har bygget investeringsmodeller med NPV/IRR, følsomhed og scenarier, og jeg har '
       'styret 37 samtidige CAPEX-projekter i Novo Nordisk, dog i en anden branche. Det, der '
       'overføres, er styringen af snitfladerne mellem engineering, indkøb og montage.')

    sub('Dokumentation, der kan bruges')
    lp('Anlægsdokumentation er ofte det, der bliver forsinket, og den bliver nødvendig igen, '
       'når et anlæg skal ændres. Jeg ville starte med en status pr. anlæg: hvad findes, hvad '
       'er forældet, og hvem ejer det. Hver linje får én ansvarlig, og den følges ugentligt i en '
       'RACI-tabel. Første leverance er en opgørelse for det første værk inden for to uger. '
       'Resten følger den rækkefølge, lovkravene kræver. Afleveringspakker holder kun, hvis '
       'de bygges løbende og ikke samles til sidst, og det har jeg arbejdet med i både Novo '
       'Nordisk og Ventek-Air.')

    sub('CO₂-fangst og fjernvarme')
    lp('Jeg har ingen erfaring med fangstanlæg, og det skal I vide, før I læser resten. For '
       'mig er CO₂-fangst en del af bæredygtig drift, og det er en af de opgaver, der gør '
       'et biomassefyret værk til et af fremtidens energianlæg. Det, jeg kan bidrage med, er '
       'arbejdet med grænsefladerne: ventiler, trykbærende udstyr, driftsdata og styringen, der '
       'skal forbinde et nyt anlæg til et eksisterende. Med fjernvarme står det anderledes. Den '
       'del kender jeg fra varme- og VVS-anlæg, og jeg har aldrig stået for et fjernvarmeværk.')

    sub('De første 90 dage')
    lp('Dag 1 til 30: Jeg lærer værket at kende sammen med en erfaren kollega og gennemgår '
       'driftsdata, alarmer og fejlhistorik. Jeg arbejder ikke på kedel eller turbine uden '
       'oplæring og godkendelse, for jeg har ikke kedelpassercertifikat. Dag 31 til 60: '
       'Fejllisten er FMEA-vurderet, og dokumentationsstatus ligger i et fælles register med '
       'ansvarlige. Dag 61 til 90: Jeg fremlægger to forbedringsforslag med investeringscase '
       'og en plan for grænsefladen til fangstanlægget. Jeg sætter ikke tal på forventede '
       'resultater, før driftsdata er gennemgået.', after=44)
    lp('Jeg kan pendle til både Avedøre og Skærbæk. Løbende muligheder for læring og udvikling '
       'på tværs af de seks værker er det næste trin, jeg kigger efter. Jeg kan komme forbi, '
       'når det passer jer.', after=44)
    lp('Med venlig hilsen', after=8)
    lp('Shahram Ajloo', after=8)

    # ------------------------------------------------------------ CV, side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Drift, fejlfinding og dokumentation på mekaniske og el-tekniske anlæg i 24/7-drift, '
           'og styring af investeringsprojekter fra idriftsættelse til aflevering. Metoderne er '
           'FMEA, A3, PDCA og investeringsmodeller med NPV/IRR og scenarier. Ansættelse på et '
           'kraftværk findes ikke i mit CV, og det står tydeligt i opgaverne nedenfor.', after=32)

    m.section('OPGAVER OG LØSNINGER')
    tasks = [
        ('Sikker drift og vedligeholdelse af biofyrede kraftvarmeværker',
         'Fejllister pr. system, sorteret efter driftsstop og gentagelser, og FMEA sammen med '
         'driftsteamet. Vedligehold planlægges efter fejlhistorik, ikke efter kalender alene. '
         'Biofos gav næsten 4½ år i 24/7-drift med pumper, HVAC og højspændingstavler, og LOTO '
         'og APV fulgte hvert arbejde.'),
        ('Driftssupport og fejlfinding med driftsdata',
         'Rodårsagsanalyse med Ishikawa og 5 Whys, og en løsning, der kan gentages. SCADA-'
         'overvågning og akut fejlfinding gav mig driftsdata som udgangspunkt på Biofos, og hos '
         'ARJ Engineering lå ansvaret for rodårsagerne på industrielt udstyr.'),
        ('Anlægsdokumentation til lovkrav og deadline',
         'Ét register pr. anlæg med en ansvarlig pr. linje, følges ugentligt i RACI-tabel. '
         'FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA på Novo Nordisk, og afleveringspakker med KS-'
         'dokumentation i Ventek-Air og ELOHVAC.'),
        ('Forbedrings- og vedligeholdelsesopgaver med leverandører',
         'Investeringscase pr. ombygning med NPV, IRR og følsomhed på driftsstop, og trinvis '
         'udskiftning i planlagte stop som første anbefaling. 37 samtidige CAPEX-projekter på '
         'DKK 2-10 mio. på Novo Nordisk og 11 parallelle projekter med underentreprenører i '
         'Ventek-Air.'),
        ('Projektingeniør med specifikationer, risiko, compliance, budget og tidsplan',
         'Risikovurdering ved hvert opstartspunkt, PRINCE2-struktur og månedlig rapport til '
         'ledelse og kunde. Tekniske specifikationer er ikke dokumenteret som opgave i mit CV, '
         'og det skriver jeg ikke om. Budget og tidsplan har jeg styret på Novo Nordisk og i '
         'ELOHVAC med fuldt P&L-ansvar.'),
        ('CO₂-fangst på Avedøre og grænsefladen til kraftværket',
         'Mekaniske grænseflader som røggas, kondensat, damp og ventiler gennemgås, før '
         'fangstanlægget kobles til. Erfaring med fangstanlæg findes ikke. Ventiler, '
         'trykbærende udstyr og sikkerhedsudstyr kommer fra Biofos.'),
        ('Dampturbiner, forbrændingssystemer og fjernvarme',
         'Dampturbiner og forbrændingssystemer har jeg ikke arbejdet med. Fjernvarme kender jeg '
         'fra varme- og VVS-anlæg, ikke fra et værk. Det praktiske kedelarbejde på Biofos har '
         'ikke en angivet kedeltype. Kedelpasser er ikke taget endnu.'),
        ('Termodynamik i vand-damp-processen',
         'Teorien kommer fra B.Tech-uddannelsen i maskinteknik, herunder damp- og '
         'vandkredsløb, og fra køleteknik og klimaanlæg (AMU). Den praktiske side af damp og '
         'kedler er fra Biofos.'),
    ]
    for head, body in tasks:
        m.bullet(head, body, after=24)

    m.section('ERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester, ansvarlig for el-teknik og ventilation',
         'Data Power Consultant ApS · København · 2024 - nu',
         [('', 'Ansvar for AI-afdelingen med 4-10 personer og for el-teknik og ventilation, '
               'herunder entreprise med fuldt P&L-ansvar fra november 2026.'),
          ('', 'Personaleledelse af 5 elektrikere og 3 lærlinge med daglig planlægning, 1:1 og MUS.'),
          ('', 'AI-værktøjer i tilbudsberegning, tidsplaner og KS-tjeklister med et dokumenteret '
               'produktivitetsløft på over 40 %.')]),
        ('Ejer og teknisk direktør, elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 - nov. 2026 (virksomheden lukket)',
         [('', 'El-tekniske opgaver på erhvervskunders el-, ventilations- og klimaanlæg, fra '
               'akutte udkald til afleveret anlæg.'),
          ('', 'Tilbud, underentreprenører, KS og afleveringsdokumentation i alle kontrakter, '
               'med akkord og opmåling af udført arbejde.'),
          ('', 'LOTO, APV og risikovurdering ved pladsopstart. Ingen kritiske afvigelser i '
               'serviceaftalerne.')]),
        ('Senior idriftsættelsesingeniør og projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 - jul. 2024',
         [('', 'Styring af 37 samtidige anlægs- og CAPEX-projekter på DKK 2-10 mio. pr. stk. '
               'med fremdrift, økonomi og risici på tværs af engineering, indkøb og anlæg.'),
          ('', 'Tværfaglig ledelse af 25 specialister. FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA '
               'med nul kritiske afvigelser ved aflevering.'),
          ('', 'El-tekniske anlæg med tavler, UPS og ABA/ABV. Fejlfinding med A3, 5x Hvorfor og '
               'Ishikawa. 40 % reduktion i energiomkostninger via et PDCA-program.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022 - nov. 2022',
         [('', '11 samtidige anlægsprojekter fra specifikation til formel aflevering, med daglig '
               'ledelse af et 14-mands team.'),
          ('', 'Udbud og tilbud, underentreprenører, aftalegrundlag, sikkerhedsdokumentation og '
               'afleveringspakker. Daglige tavlemøder og flaskehalsanalyser.')]),
        ('Vedligeholdelses- og driftsleder, værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 - jan. 2022',
         [('', 'Drift og vedligehold af pumper, HVAC, højspændingstavler og SCADA i 24/7-drift, '
               'med forebyggende vedligehold og akut fejlfinding.'),
          ('', 'Praktisk kedelarbejde, ventiler, trykbærende udstyr og sikkerhedsudstyr.'),
          ('', 'Skifteholdsdrift med LOTO, risikovurdering, APV og nærved-hændelser. 5S, Standard '
               'Work og PDCA på værksted og lager.')]),
        ('Elektromekaniker og produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003 - mar. 2010',
         [('', 'Ledelse af 12 mekanikere og teknikere i værksted: vagtplan, materialer og mål.'),
          ('', 'Fejldiagnose og reparation af industrielle el- og mekaniske anlæg, med '
               'rodårsagsanalyse og korrigerende handlinger.')]),
    ]
    for title, meta, bullets in jobs:
        m.job(title, meta)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('UDDANNELSE OG AUTORISATIONER')
    m.edu('B.Tech (EQF6), Technology Management and Mechanical Engineering',
          'Copenhagen School of Marine Engineering & Technology Management · 2017-2022 · GPA 7,6/12')
    m.edu('Electrical and Mechanical Engineering Design, elteknik (EQF6)',
          'Tehran Technical University · 2000-2003')
    m.edu('Elautoriseret maskinmester (LV/MV/HV)',
          'Sikkerhedsstyrelsen · maj 2023')
    m.edu('PRINCE2, certificeret projektleder', 'AXELOS / PeopleCert')
    m.edu('Køleteknik og klimaanlæg (AMU)', 'Mercantec · 2021')
    m.edu('STCW: vagt i maskinrummet (A-III/1), skibssikkerhed og tankskib',
          'Søfartsstyrelsen · 2021-2023. Maritime kvalifikationer, ikke kedelpassercertifikat')
    m.para('Arbejdet med Lean og Six Sigma i praksis, ikke certificeret: DMAIC, 5S, PDCA, VSM, '
           'A3, Kaizen, Standard Work, SMED, TPM, 5 Whys, Ishikawa og FMEA.', after=48)

    m.section('KOMPETENCER')
    m.models_table('Værktøjer og systemer', ('Område', 'Værktøj'), [
        ('Drift og fejl', 'SCADA, FMEA, Ishikawa, 5 Whys, A3, PDCA, Standard Work'),
        ('Vedligehold og dokumentation', 'CMMS, SAP ERP, RACI, afleveringspakker, KS-dokumentation'),
        ('Projekt og økonomi', 'PRINCE2, NPV/IRR, følsomhed, scenarieanalyse, budget og tidsplan'),
        ('Data og AI', 'Python, Claude API og Claude Code, Power BI, Excel og Power Query'),
        ('Sikkerhed', 'LOTO, APV, risikovurdering, nærved-hændelser, GMP/FDA/EMA'),
    ], widths=(3400, 6946), compact=True)
    m.para('Dansk som modersmål. Engelsk på professionelt niveau, mundtligt og skriftligt. '
           'Persisk som modersmål. Kørekort B, manuel gear.', after=40)

    # ------------------------------------------------------------ kravmatrix, side 4
    m.page_break()
    m.section('KRAVMATRIX')
    rows = [
        ('har en maskinteknisk baggrund som maskiningeniør, maskinmester eller en tilsvarende '
         'uddannelse med omfattende teoretisk viden om kedler og trykbærende anlæg',
         'B.Tech (EQF6) i maskinteknik og teknologiledelse, 2017-2022. Elautoriseret maskinmester '
         '(LV/MV/HV) er en autorisation, ikke en maskinmesteruddannelse. Trykbærende udstyr er '
         'dokumenteret fra Biofos. Gap: der er ingen kedelpasser-uddannelse.'),
        ('har solid viden om termodynamik og mekaniske komponenter i vand-dampprocessen',
         'Teorien er fra B.Tech-uddannelsen, herunder damp- og vandkredsløb. Praktisk kedelarbejde '
         'er dokumenteret fra Biofos, med næsten 4½ år i 24/7-drift (2017-2022). Dampturbiner '
         'er der ingen praktisk erfaring med.'),
        ('har omfattende erfaring fra kraftværksbranchen, stor teoretisk og praktisk viden om '
         'forskellige mekaniske systemer inden for dit ekspertiseområde og har lyst til at lære mere',
         'Gap: ingen ansættelse på kraftværk. Den mekaniske erfaring er fra 24/7-drift på Biofos, '
         'pharma-anlæg på Novo Nordisk og værkstedsdrift. Vilje til at lære værkets anlæg '
         'med oplæring og godkendelse.'),
        ('behersker projektingeniørdiscipliner, herunder udarbejdelse af tekniske specifikationer, '
         'risikovurderinger, sikring af compliance samt overholdelse af budget og tidsplaner',
         'Risikovurdering, compliance og budget/tidsplan: 37 CAPEX-projekter på Novo Nordisk, '
         'PRINCE2 og månedlig rapportering. Tekniske specifikationer: ikke dokumenteret som '
         'opgave, og jeg skriver ikke om det.'),
        ('har analytiske og systematiske kompetencer til at løse komplekse problemstillinger inden '
         'for energianlæg og arbejder målrettet med opgaver både selvstændigt og i teams',
         'FMEA, A3, 5x Hvorfor og Ishikawa på fejl på Novo Nordisk og Biofos. Teamledelse af 25 '
         'specialister, 14-mands entrepriseteam og 12 mekanikere og teknikere.'),
        ('kan kommunikere teknisk komplekst stof klart og præcist på dansk og engelsk, både mundtligt '
         'og skriftligt',
         'Dansk som modersmål. Engelsk på professionelt niveau, og engelsk har været arbejdssprog '
         'i internationale projekter siden 2017.'),
        ('blive en af vores mekaniske specialister og understøtte sikker drift og vedligeholdelse af '
         'alle biofyrede kraftvarmeværker i Danmark',
         'Drift og vedligehold af pumper, HVAC, højspændingstavler og SCADA i næsten 4½ år i '
         '24/7-drift, LOTO og APV ved hvert arbejde. Fra første dag: fejlliste pr. system med FMEA.'),
        ('yde serviceorienteret, faglig rådgivning om dampturbiner, pumper, ventilatorer, trykbærende '
         'udstyr, forbrændingssystemer, fjernvarme og fjernkøling samt CO2-fangstanlæg',
         'Pumper, ventilatorer og trykbærende udstyr er dokumenteret. Dampturbiner, '
         'forbrændingssystemer og CO2-fangst er gap. Fjernvarme står som interesse, ikke som drift.'),
        ('udføre driftssupport samt analysere og finde tekniske fejl inden for specialistområdet, ved '
         'hjælp af driftsdata, tekniske dokumentation og beregninger',
         'SCADA-overvågning og akut fejlfinding i 24/7-drift på Biofos. Rodårsagsanalyse på '
         'industrielt udstyr med 12 mekanikere og teknikere hos ARJ Engineering. Beregninger i '
         'Python og Excel.'),
        ('udarbejde forbedrings- og vedligeholdelsesopgaver og som hands-on teknisk ansvarlig udføre '
         'projektingeniørarbejde med store og små ombygninger i samarbejde med leverandører',
         'Underentreprenører, leverandøraftaler og afleveringspakker i Ventek-Air med 11 '
         'samtidige projekter og et 14-mands team. Investeringscase med NPV og følsomhed for hver '
         'ombygning før beslutning.'),
        ('udarbejde og opdatere anlægsdokumentation iht. interne processer og lovkrav inden for den '
         'angivne deadline',
         'Afleveringsdokumentation og KS-dokumentation i 11 samtidige projekter i Ventek-Air. '
         'Register pr. anlæg med ansvarlig pr. linje og ugentlig opfølgning i RACI-tabel.'),
        ('bidrage i større CAPEX-projekter',
         'Projektstyring på Novo Nordisk: 37 samtidige projekter med fremdrift, økonomi og risici '
         'i porteføljen. Ingen erfaring fra CAPEX på kraftværk, kun fra pharma og el-systemer.'),
        ('rejse mellem kraftværkerne i Danmark',
         'Pendling er mulig til begge værker. Ørsted driver seks kraftvarmeværker, og hyppigheden '
         'af besøg på de øvrige er endnu ikke afklaret og skal aftales i ansættelsen.'),
    ]
    m.models_table('Opslagets krav og min dokumentation', ('Krav', 'Dokumentation og status'),
                   rows, widths=(3600, 6746), compact=True)

    m.save(path, title='Senior Mechanical Specialist - Ørsted',
           subject='Ansøgning Senior Mechanical Specialist, Skærbæk og Avedøre')
    print(path)


if __name__ == '__main__':
    os.makedirs(OUT_DIR, exist_ok=True)
    build(OUT)
