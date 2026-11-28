# -*- coding: utf-8 -*-
"""Vejdirektoratet · ME/OT fagansvarlig til elektriske og mekaniske installationer på bygværker.

Dansk opslag -> dansk dokument. Masterdesign (scripts/master_design.py):
brev side 1, CV side 2-3, kravmatrix side 4.

Kun fakta fra master-CV'et og brugerens bekræftelser. Ingen erfaring med NIS2, CER,
trafikanlæg, bygherretilsyn i offentlig sammenhæng eller sikkerhedsgodkendelse.
Titel: maskinmester (marine engineering & technology management), som brugeren bekræftede.
Kilder til bygværkerne er sekundære (Dagens Byggeri, Licitationen) og angivet med årstal.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
OUT_DIR = os.path.join(ROOT, 'output')
OUT = os.path.join(OUT_DIR, 'Shahram_Ajloo_Vejdirektoratet_MEOTFagansvarligBygvaerk.docx')

NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'ME/OT fagansvarlig · elektriske og mekaniske installationer på bygværker'
BANNER_RESUME = 'Drift, test og dokumentation af el- og mekaniske anlæg'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('28. november 2026')
    m.meta('Vejdirektoratet · Bygværksforvaltning · Skanderborg eller Hedehusene')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: ME/OT fagansvarlig til elektriske og mekaniske installationer på bygværker',
           bold=True, size=26, color='002B5C')
    m.para('Kære Jakob Schwartz,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    def sub(text):
        p = m._p(spacing_after=20, spacing_before=60, line=260, justify=False, keep_next=True)
        m._run(p, text, bold=True, color='002B5C')
        return p

    # ------------------------------------------------------------ brev, side 1
    lp('Et bygværk skal kunne køre hver dag, og trafikanterne tænker ikke på det, der holder det i '
       'gang: ventilation i tunnelen, belysning, pumper, brandalarmer og styringen, der binder det '
       'hele sammen. Vejdirektoratet driver og vedligeholder ca. 2.500 broer og tunneler på '
       'statsvejnettet. Den daglige drift er det, der afgør, om de er trygge at køre på, og den '
       'er kernen i stillingen: at bygværkerne driftes sikkert og stabilt, med fokus på drift og '
       'mange forskellige fagligheder under samme tag.')

    sub('Én driftsplan pr. bygværk')
    lp('Et bygværk har mange anlæg, og hvert anlæg har sin egen testrytme. Jeg ville starte med en '
       'anlægsliste pr. bygværk: hvilke installationer der findes, hvem der ejer dem, hvornår de sidst '
       'blev testet, og hvad der står næste gang. Listen er grundlaget for planlægningen, og den '
       'holder kun, hvis den opdateres efter hvert eftersyn. Den skal derfor ligge hos driftspersonalet '
       'på bygværket og ikke kun på kontoret.')

    sub('NIS2 og CER starter med en kortlægning')
    lp('NIS2 og CER er nye for mig i praksis, og jeg vil ikke give et andet indtryk. Det, jeg kender, '
       'er risikovurdering, afvigelseshåndtering og dokumentationskrav i et reguleret miljø. Første '
       'skridt ville være at kortlægge, hvilke M&E- og OT-anlæg på bygværkerne der er netværksforbundne, '
       'hvem der har adgang, og hvor driften hænger på et enkelt system. Resultatet er en prioriteret '
       'liste, som I kan drøfte med beredskab og rådgivere, før noget købes eller ændres.')

    sub('Grænseflader med rådgivere, entreprenører og beredskab')
    lp('Bygherretilsyn er det sted, hvor en fejl bliver til en fakta, hvis ingen skriver den ned. Jeg '
       'ville bruge én fast tjekliste pr. besøg, med det aftalte, den ansvarlige og fristen. Så har '
       'rådgivere og entreprenører samme udgangspunkt, og beredskabet ved, hvad der er i drift, og hvad '
       'der er under arbejde. Det er også den form for matrixorganisation, hvor ansvaret ligger klart, '
       'selv når mange hænder er på samme anlæg.')

    sub('Hvornår specialisten skal kaldes')
    lp('Stillingen beder om, at man kan bedømme, hvornår der skal indhentes specialviden. Jeg ville '
       'gøre det skriftligt: hvilke opgaver der løses i huset, og hvilke der sendes til specialister. '
       'Det gælder især OT-sikkerhed og trafikanlæg, hvor jeg ikke har dokumenteret erfaring. Så er det '
       'klart for alle, hvad der er gjort, og hvad der venter.')

    sub('Test og dokumentation i samme rytme')
    lp('Test og vedligehold betyder kun noget, hvis dokumentationen følger med, mens arbejdet står på. '
       'Jeg ville lægge testintervallerne ind i anlægslisten og lukke hver test med måling, dato og '
       'underskrift i samme system. Så kan driftslederen se forfaldne test, før de bliver fundet ved '
       'næste eftersyn. Det er også den bedste måde at få videndeling mellem kontorerne til at virke, '
       'fordi alle arbejder i samme liste.')

    lp('Jeg har set stillingen via Techjob. Bygværksforvaltning er jeres kompetencecenter for alt '
       'bygværksrelateret arbejde, og jeg vil gerne tale om, hvilke bygværker I ser som de første, der '
       'skal have en driftsplan. Jeg vil også høre, hvordan den daglige drift, tilsynene og NIS2-arbejdet '
       'fordeles i ugen, de ugentlige hjemmearbejdsdage inklusive. I beskriver en positiv ånd og god dialog, '
       'og høj medarbejdertrivsel er det, der holder en driftsgruppe sammen over tid. Fleksibilitet, '
       'kompetenceudvikling og arbejdsliv i balance er også noget, jeg gerne vil drøfte, så det passer til '
       'driftens behov.', after=44)
    lp('Med venlig hilsen', after=8)
    lp('Shahram Ajloo', after=8)

    # ------------------------------------------------------------ CV, side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Drift, fejlfinding og vedligehold af el- og mekaniske anlæg i 24/7-drift, bygningsautomatik '
           'og styring, samt projektstyring fra idriftsættelse til aflevering. Jeg er elautoriseret '
           'maskinmester (LV/MV/HV). Stillingens krav om NIS2, CER og trafikanlæg er ikke '
           'dækket af min erfaring i dag, og det fremgår af kravmatrixen.', after=32)

    m.section('OPGAVER OG LØSNINGER')
    tasks = [
        ('Driftsplan pr. bygværk',
         'Anlægsliste med ejer, testintervaller og næste test, opdateret efter hvert eftersyn. '
         'Forebyggende vedligehold af pumper, HVAC og højspændingstavler i 24/7-drift på Biofos.'),
        ('Fejlfinding og driftssupport',
         'Rodårsagsanalyse med 5 hvorfor, Ishikawa og FMEA. SCADA-overvågning og akut fejlfinding '
         'på Biofos. Driftsdata brugt som udgangspunkt, før en fejl blev rettet.'),
        ('Test og dokumentation',
         'FAT, SAT og IQ/OQ/PQ på Novo Nordisk med nul kritiske afvigelser ved aflevering. KS-dokumentation '
         'og afleveringspakker i Ventek-Air og ELOHVAC.'),
        ('Sikkerhed under drift',
         'LOTO, risikovurdering og APV ved hvert arbejde. ABA, ABV, adgangskontrol og nød- og '
         'panikbelysning på Novo Nordisk.'),
        ('Grænseflader og koordinering',
         '11 samtidige projekter med underentreprenører i Ventek-Air og 37 samtidige CAPEX-projekter '
         'i Novo Nordisk, med engineering, indkøb og anlæg på samme plan.'),
        ('Bygningsautomatik og OT-nære anlæg',
         'CTS/BMS og KNX i bygningsautomatik. SCADA og styringstavler. Ledelse af arbejdet på PLC-styrede anlæg.'),
    ]
    for head, body in tasks:
        m.bullet(head, body, after=24)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester, el-teknik og ventilation',
         'Data Power Consultant ApS · København · 2024 til nu',
         [('', 'Ansvarlig for AI- og AI coding-afdelingen med 4 til 10 personer. Samtidig el-teknik og '
               'ventilation, herunder de el-tekniske aktiviteter fra ELOHVAC fra november 2026, med fuldt P&L-ansvar.'),
          ('', 'Personaleledelse af 5 elektrikere og 3 lærlinge med daglig planlægning, 1:1 og MUS.'),
          ('', 'Matrixledelse af to sideløbende organisationer med én samlet plan og skriftlige prioriteringer.')]),
        ('Ejer og teknisk direktør, elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 til nov. 2026 (virksomheden lukket)',
         [('', 'El-tekniske opgaver på erhvervskunders el-, ventilations- og klimaanlæg, fra akutte udkald til afleveret anlæg.'),
          ('', 'Tilbud, underentreprenører, KS og afleveringsdokumentation i alle kontrakter.'),
          ('', 'LOTO, APV og risikovurdering ved pladsopstart. Nul kritiske afvigelser i serviceaftalerne.')]),
        ('Senior idriftsættelsesingeniør og projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg og Bagsværd · nov. 2022 til jul. 2024',
         [('', 'Styring af 37 samtidige anlægs- og CAPEX-projekter på DKK 2 til 10 mio. pr. stk. med fremdrift, økonomi og risici.'),
          ('', 'Tværfaglig ledelse af 25 specialister. FAT/SAT og IQ/OQ/PQ under GMP, FDA og EMA med nul kritiske afvigelser ved aflevering.'),
          ('', 'El-tekniske anlæg med tavler og styring, UPS, nød- og panikbelysning, ABA/ABV og PDS. 40 % lavere energiomkostninger via et PDCA-program.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022 til nov. 2022',
         [('', '11 samtidige anlægsprojekter fra specifikation til formel aflevering, med daglig ledelse af et 14-mands team.'),
          ('', 'Udbud og tilbud, underentreprenører, aftalegrundlag, sikkerhedsdokumentation og afleveringspakker.')]),
        ('Vedligeholdelses- og driftsleder, værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 til jan. 2022',
         [('', 'Drift og vedligehold af pumper, HVAC, højspændingstavler og SCADA i 24/7-drift. Ansvar for procesudstyret på renseanlægget.'),
          ('', 'Skifteholdsdrift med LOTO, risikovurdering, APV og nærved-hændelser. 5S, Standard Work og PDCA på værksted og lager.')]),
        ('Elektromekaniker og produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003 til mar. 2010',
         [('', 'Ledelse af 12 mekanikere og teknikere i værksted: vagtplan, materialer og mål.'),
          ('', 'Fejldiagnose og reparation af industrielle el- og mekaniske anlæg, med rodårsagsanalyse.')]),
    ]
    for title, meta, bullets in jobs:
        m.job(title, meta)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('UDDANNELSE OG AUTORISATIONER')
    m.edu('Maskinmester (marine engineering & technology management)',
          'Copenhagen School of Marine Engineering & Technology Management · 2017 til 2022')
    m.edu('El- og maskinteknisk design, elteknik (EQF6)',
          'Tehran Technical University · 2000 til 2003')
    m.edu('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('PRINCE2, certificeret projektleder', 'AXELOS / PeopleCert')
    m.edu('Køleteknik og klimaanlæg (AMU)', 'Mercantec · 2021')
    m.edu('STCW: vagt i maskinrummet, skibssikkerhed og tankskib', 'Søfartsstyrelsen · 2021 til 2023')
    m.para('Lean og Six Sigma arbejdet med i praksis, ikke certificeret: DMAIC, 5S, PDCA, VSM, A3, Kaizen, '
           'SMED, TPM, 5 hvorfor, Ishikawa og FMEA. Sikkerhedsgodkendelse har jeg endnu ikke, men jeg er klar til at blive godkendt.',
           after=48)

    m.section('KOMPETENCER')
    m.models_table('Værktøjer og systemer', ('Område', 'Værktøj'), [
        ('Drift og fejl', 'SCADA, FMEA, Ishikawa, 5 hvorfor, A3, PDCA, Standard Work'),
        ('Installationer', 'Pumper, HVAC, ventilation, højspænding, tavler, UPS, ABA og ABV, adgangskontrol, nød- og panikbelysning'),
        ('Bygningsautomatik', 'CTS/BMS, KNX, styring og overvågning'),
        ('Dokumentation og vedligehold', 'CMMS, KS-dokumentation, afleveringspakker, RACI, SAP ERP'),
        ('Projekt og økonomi', 'PRINCE2, NPV/IRR, budget og tidsplan'),
        ('Sikkerhed', 'LOTO, APV, risikovurdering, nærved-hændelser, GMP/FDA/EMA'),
    ], widths=(3400, 6946), compact=True)
    m.para('Dansk som modersmål, skriftligt og mundtligt. Engelsk på professionelt niveau. Persisk som '
           'modersmål. Kørekort B, manuelt gear.', after=40)

    # ------------------------------------------------------------ kravmatrix, side 4
    m.page_break()
    m.section('KRAVMATRIX')
    rows = [
        ('Planlægning og gennemførelse af den daglige drift og vedligeholdelse af mekaniske og elektriske installationer på flere af vores eksisterende store og små bygværker',
         'Forebyggende vedligehold og driftsplanlægning på Biofos, 2017 til 2022, for pumper, HVAC og højspændingstavler i 24/7-drift. Vedligehold og akut fejlfinding af el- og ventilationsanlæg i ELOHVAC, 2023 til 2026, fra udkald til afleveret anlæg. Bygværker som sådan er ikke dokumenteret.'),
        ('Implementering af nye tiltag på bygværker i forhold til NIS2 og CER',
         'Erfaring med NIS2 eller CER i praksis er ikke til stede. Nærmeste: risikovurdering, LOTO og APV ved hvert arbejde, og dokumentationskrav under GMP, FDA og EMA på Novo Nordisk, 2022 til 2024. Første skridt er en kortlægning af netværksforbundne anlæg og adgangsrettigheder.'),
        ('Sikre at anlæg løbende bliver testet, vedligeholdt og dokumenteret',
         'FAT, SAT og IQ/OQ/PQ på Novo Nordisk, 2022 til 2024, med nul kritiske afvigelser ved aflevering. KS-dokumentation og afleveringspakker i Ventek-Air i 2022 og i ELOHVAC fra 2023 til 2026. Vedligehold registreret i CMMS.'),
        ('Bygherretilsyn og gennemgang på bygværkerne med rådgivere, entreprenører, beredskab m.fl.',
         'Bygherrerapportering og koordinering med rådgivere og underentreprenører i Novo Nordisk og Ventek-Air. Offentligt bygherretilsyn på bygværker er ikke dokumenteret i min erfaring, og det er et område, jeg vil afklare i de første uger.'),
        ('Installationer som pumper og rør, elforsyning, belysningsanlæg, brand og sikring, trafikanlæg og OT (Operational Technology)',
         'Pumper og rørsystemer fra Biofos og Ventek-Air. Elforsyning med højspændingstavler og UPS, belysning med nød- og panikbelysning, ABA og ABV samt adgangskontrol på Novo Nordisk. Trafikanlæg er ikke dokumenteret. OT er nært forbundet med SCADA og styring.'),
        ('Uddannelse som stærkstrømsingeniør, automationsingeniør eller tekniker, maskiningeniør, maskinmester, elinstallatør eller lignende',
         'Maskinmester (marine engineering & technology management), 2017 til 2022, og elteknik (EQF6) fra Tehran, 2000 til 2003. Autorisationen som maskinmester (LV/MV/HV) er fra maj 2023. Jeg er ikke stærkstrømsingeniør eller automationsingeniør.'),
        ('Lyst til at varetage driften af alle typer installationer og se på den samlede drift',
         'Drift af pumper, HVAC, højspænding, SCADA og bygningsautomatik i praksis, og fra udkald til afleveret anlæg i ELOHVAC. Den samlede drift af alle installationstyper i ét bygværk er ikke dokumenteret i en tidligere stilling.'),
        ('Minimum 5 års relevant erfaring indenfor elektriske og mekaniske installationer',
         'Biofos alene dækker 4 år og 5 måneder, fra august 2017 til januar 2022, med el- og mekanisk drift i 24/7. Novo Nordisk, Ventek-Air, ELOHVAC og Data Power med el-teknik og ventilation ligger oven i det fra 2022 til i dag.'),
        ('Teknisk velfunderet inden for M&E og OT, og kan bedømme hvornår der er brug for at indhente specialviden',
         'Teknisk fundament i elektrisk og mekanisk drift samt OT-nær erfaring: SCADA-overvågning på Biofos, styring og tavler på Novo Nordisk, CTS/BMS og KNX, og ledelse af PLC-styrede anlæg. Jeg bedømmer selv, hvornår specialister skal inddrages, og skriver det ned.'),
        ('Motiveres af og trives i projekter med mange grænseflader',
         'Projekter med mange parter har været den daglige ramme: 11 samtidige projekter med underentreprenører i Ventek-Air, 37 samtidige CAPEX-projekter i Novo Nordisk og to sideløbende organisationer i Data Power og ELOHVAC med én samlet plan.'),
        ('Kan arbejde selvstændigt, systematisk og er god til at holde overblik',
         'Systematisk arbejde med FMEA, A3 og 5 hvorfor. Daglig planlægning af et 14-mands team i Ventek-Air og af 5 elektrikere og 3 lærlinge. Skriftlige aftaler om, hvad der går forud, i ELOHVAC og Data Power.'),
        ('Kan kommunikere tydeligt både mundtligt og skriftligt på dansk',
         'Dansk som modersmål, mundtligt og skriftligt. Månedsrapportering til ledelse og bygherre i Novo Nordisk. Afleveringsdokumentation med KS-krav i entreprisen.'),
        ('Kørekort B',
         'Kørekort B med manuelt gear. Vejdirektoratet stiller biler til rådighed, så jeg har ikke brug for egen bil til arbejdet, og kørekortet dækker kravet fuldt ud.'),
        ('Sikkerhedsgodkendelse, som kan opretholdes i hele ansættelsesperioden',
         'Sikkerhedsgodkendelse har jeg ikke i dag. Jeg er klar til at blive sikkerhedsgodkendt og til at opretholde godkendelsen i hele ansættelsen.'),
    ]
    m.models_table('Opslagets krav og min dokumentation', ('Krav', 'Dokumentation og status'),
                   rows, widths=(3600, 6746), compact=True)

    m.save(path, title='ME/OT fagansvarlig - Vejdirektoratet',
           subject='Ansøgning ME/OT fagansvarlig, bygværker, Vejdirektoratet')
    print(path)


if __name__ == '__main__':
    os.makedirs(OUT_DIR, exist_ok=True)
    build(OUT)
