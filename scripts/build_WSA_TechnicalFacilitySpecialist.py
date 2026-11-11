# -*- coding: utf-8 -*-
"""WSA (WS Audiology) — Technical Facility Specialist med BMS-viden, Lynge.

Form (master/FORMKATALOG.md): åbning **G** (spørgsmålet faget stiller), struktur
**Dokumentrækken** (ét dokument pr. afsnit), register **Laboratoriet** (hypotese, prøve,
reference, reproduktion). Kulturfil: jd/WSA_TechnicalFacilitySpecialist_kultur.txt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Technical Facility Specialist · CTS/BMS, HVAC og energioptimering'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('8. november 2026')
    m.meta('WSA · Facility Management · Hovedkontoret, Nymøllevej 6, Lynge')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Teknisk Specialist med BMS-viden', bold=True, color='1A1A1A')
    m.para('Til Facility Management i Lynge', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('**Hvornår er en alarm en fejl — og hvornår er den en føler, der driver?** Et **CTS**-anlæg '
           'kan sende hundredvis af **alarmer** i døgnet, og kun få af dem betyder, at noget skal '
           'repareres i dag. Forskellen står ikke på skærmen. Den findes ved at gå ned i '
           'maskinrummet, måle efter og skrive ned, hvad der blev fundet — så næste mand ikke starter '
           'forfra. Det er den slags arbejde, jeg søger hos WSA: at gøre anlægget forståeligt, så de '
           'otte i Facility Management kan styre det, uden at det kræver en ekstern leverandør hver '
           'gang. Det er den samme opgave, uanset om anlægget står i et **laboratorium**, på en '
           'produktionslinje — eller i det hus, hvor der bliver lavet **høreapparater** under brands '
           'som **Widex** og Signia.', after=80)

    m.para('**Fem dokumenter — det er, hvad jeg ville tage fat på først, og de hænger sammen i den '
           'rækkefølge.**', after=60)

    m.para('**1. Alarmloggen.** De fleste anlæg har for mange alarmer og for lidt information. Jeg '
           'har prioriteret **SRO**-alarmer efter kritikalitet i fem år på et 24/7-anlæg, hvor et '
           'manglende signal standsede forsyningen — og jeg ved, at en alarm, der ikke bliver handlet '
           'på, lærer folk at ignorere panelet.', after=60)

    m.para('**2. Trendkurven.** En **føler**, der driver to grader over et år, koster mere end den '
           'fejl, den skjuler. Jeg har arbejdet med **trend**data og **regulering** i døgndrift og '
           'med **energioptimering**, der gav **over 40 % lavere forbrug** — netop fordi målingerne '
           'blev læst som et spørgsmål, ikke som en sandhed.', after=60)

    m.para('**3. Ændringsloggen.** Hvem ændrede sætpunktet, hvornår, og hvorfor? Jeg har selv ændret '
           'sætpunkter, tidsprogrammer, alarmer og reguleringsparametre i **SRO/SCADA** og ved, hvor '
           'hurtigt et anlæg bliver uforståeligt, hvis ændringen ikke bliver skrevet ned. Det er den '
           'log, der gør **dokumenteret viden** og **stærk backup på tværs** mulig.', after=60)

    m.para('**4. Tjeklisten og vedligeholdsplanen.** Forebyggende **vedligehold** er kun forebyggende, '
           'hvis nogen har besluttet, hvad der skal tjekkes, og hvornår. Jeg har indført 5S og '
           'standard work på værksted og lager og styret **vedligehold** efter kritikalitet i 24/7 — '
           'og det er samme disciplin, der skal bære **ATES**, **varme**, **køl** og **ventilation** '
           'her.', after=60)

    m.para('**5. Fejlrapporten, der bliver til en model.** **AI** i **Facility Management** giver kun '
           'værdi, hvis dataene er ryddet op først: en **prædiktiv** model bygget på en alarmliste '
           'uden årsagskoder lærer støj. Jeg bygger selv værktøjer i **Python** til tjeklister, '
           'databehandling og rapportering — med **over 40 % færre manuelle timer** til følge — og '
           'jeg vil hellere starte med ti komponenter, der faktisk kan forudsiges, end med en '
           'platform, der kan alt.', after=80)

    m.para('**Det, jeg kan, og det, jeg skal lære.** Jeg har ændret og optimeret i **CTS**-lignende '
           'styring i drift, men jeg har ikke programmeret styringsblokke fra bunden. Til gengæld har '
           'jeg otte års arbejde med **HVAC**, **ventilation**, **varme** og **køl** — som '
           'elautoriseret maskinmester med køle- og ventilationsteknisk AMU — og jeg har stået på den '
           'side af bordet, hvor en dårlig **regulering** bliver til et indeklima, brugerne klager '
           'over.', after=70)

    m.para('**Hvorfor jeres team.** I skriver, at **praktisk teknisk arbejde og analytisk '
           'systemforståelse vægtes lige højt**, og at I vil **reducere unødvendig afhængighed af '
           'eksterne leverandører**. Det er præcis den kombination, jeg har dyrket: jeg har selv stået '
           'med instrumentet og selv skrevet værktøjet, der gjorde arbejdet hurtigere. At anlægget '
           'ligger på et **energineutralt** hovedkontor siden 2010 gør opgaven mere interessant, ikke '
           'mindre — der er ikke noget at hente på at slukke for noget, der aldrig var tændt.', after=70)

    m.para('**I vil, at vi opbygger og fastholder mere teknisk kompetence internt. Det er også mit '
           'argument for at søge her.** Jeg har prøvet at være '
           'den eneste, der vidste, hvordan anlægget reagerede — og det er en dårlig forretning for '
           'alle. **Fælles ejerskab** og **dokumenteret viden** er ikke en HR-sætning; det er den '
           'eneste måde, **stærk backup på tværs** bliver sand, når en kollega er syg i uge 42.', after=70)

    m.para('Og så det, der gør WSA til et sted, jeg gerne vil arbejde. I skriver, at **vi tager hånd om '
           'hinanden**, at I **værdsætter mangfoldighed**, og at **vi kan godt lide at grine sammen** — at '
           '**et godt arbejdsmiljø og hinandens gode selskab** vejer tungt. Det er ikke blødt i '
           'forhold til det faglige; det er forudsætningen for, at nogen tager telefonen, når alarmen '
           'går kl. 02. Og når formålet er at **frigøre menneskeligt potentiale** og sikre **god lyd '
           'til alle**, betyder et indeklima, der virker, faktisk noget for dem, der arbejder her.', after=70)

    m.para('**Praktisk:** jeg bor i Måløv, 20 minutter fra **Lynge**, har **kørekort** og bil, '
           '**dansk** som modersmål og **engelsk** på professionelt niveau, og jeg bor og arbejder i '
           'Danmark. Jeg kan starte efter aftale og vil gerne se anlæggene, før vi taler løn — '
           '**ATES**-anlægget og det, der styrer det, er det første, jeg ville spørge om.', after=70)

    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Teknisk specialist med 20+ års erfaring fra anlæg i døgndrift — **elautoriseret '
           'maskinmester (LV/MV/HV)** med køle- og ventilationsteknisk uddannelse og B.Tech i '
           'teknologiledelse og maskinteknik. Fem år som drifts- og vedligeholdelsesleder på et '
           'kritisk anlæg med **SRO/SCADA**, pumper, blæsere, **ventilation**, **varme** og '
           '**køl** — med **over 40 % lavere energiforbrug** gennem måling, indregulering og '
           '**energioptimering**. Ændrer selv sætpunkter, tidsprogrammer og alarmer i styringen, '
           'bygger **Python**-værktøjer til data og dokumentation og har leveret **37 '
           'kapitalprojekter** med idriftsættelse, FAT/SAT og nul kritiske fund.', after=80)

    m.section('LABORATORIET — FRA ALARM TIL MÅLING')
    for label, body in [
        ('CTS/BMS, SRO og optimering',
         'Driftsansvar i **SRO/SCADA** med alarmer, målinger og regulering af pumper, blæsere og '
         'ventilation; sætpunkter, tidsprogrammer og alarmer ændret og optimeret i drift — og '
         'ændringen skrevet ned bagefter.'),
        ('Fejlfinding fra skærm til anlæg',
         'Hypotese stillet på trenddata, verificeret med inspektion og måling ved anlægget: '
         'følerefterlevelse, **kalibrering**, tryk og temperatur; fejlen lukket med årsag, ikke kun '
         'med en kvittering.'),
        ('Ventilation, varme og køl',
         'Ventilation og indeklima projekteret og leveret i Ventek-Air og egen virksomhed; køle- og '
         'ventilationsteknik fra AMU; varme- og kølesystemer driftet med **komfort** og forbrug som '
         'samme opgave.'),
        ('Energi og driftsikkerhed',
         'Energiledelse med over 40 % lavere forbrug dokumenteret over fem år; **frekvensomformere**, '
         '**pumper** og blæsere indreguleret; driftsikkerhed og energiforbrug vejet sammen, ikke '
         'hver for sig.'),
        ('Dokumentation og vidensdeling',
         'Driftsinstruktioner, afvigelser og tilbagevendende fejl skrevet ned, så næste vagt kunne '
         'overtage; 5S og standard work på værksted og lager; tjeklister bygget som skabeloner og '
         'genbrugt.'),
        ('Digitale værktøjer og AI',
         'Egne værktøjer i **Python** og Claude til tjeklister, databehandling og rapportering med '
         'over 40 % færre manuelle timer; data ryddet op, før modeller blev bygget — og kun der, hvor '
         'der var nok historik.')]:
        m.bullet(label, body, after=25)

    m.models_table('SYSTEMER OG METODER', ('Område', 'Dokumenteret brug'), [
        ('Styring og overvågning',
         'SRO/SCADA: alarmer, trends, tidsprogrammer og reguleringsparametre; prioritering efter '
         'kritikalitet og opfølgning på tilbagevendende fejl.'),
        ('El og autorisation',
         'LV/MV/HV, transformere, koblingsanlæg, tavler, motorer og frekvensomformere; elautorisation og '
         'ansvar for, at arbejdet udføres af kompetente folk efter gældende krav.'),
        ('Data og dokumentation',
         'Python, Excel og Power Query til logdata, tjeklister og rapporter; ændringslog og '
         'driftsviden skrevet, så den kan læses af en anden.'),
        ('Projekt og idriftsættelse',
         'Kravspecifikation, FAT/SAT og afleveringspakker; 37 kapitalprojekter med månedlig '
         'opfølgning på fremdrift, økonomi og risiko.'),
        ('Leverandører og specialister',
         'Serviceaftaler og specialleverandører styret på tid, pris og kvalitet — og grænsen mellem '
         'hvad der løses internt, og hvornår der skal autorisation på.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · elautorisation · service- og entrepriseydelser',
         [('Drift, service og fejlfinding',
           'Fejlfinding og optimering på el- og installationstekniske anlæg hos kunder; serviceaftaler, '
           'responstider og dokumentation; faglig sparring med elektrikere og lærlinge i hverdagen.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('Idriftsættelse og verifikation',
           'Kravspecifikation, FAT/SAT og IQ/OQ af elektriske anlæg og styringer; test dokumenteret '
           'og afvigelser lukket med navn og dato; nul kritiske fund ved aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere og formænd · 11 samtidige anlægsprojekter · ventilation',
         [('Ventilation og leverance',
           'Kapacitets- og flaskehalsanalyse og omprioritering samme dag; leverancer af ventilation '
           'styret til deadline med afleveringspakker og test.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Lynetten under Biofos · København · aug. 2017–jan. 2022',
         'Kritisk anlæg i 24/7-drift · SRO/SCADA · ventilation, pumper, transformere, koblingsanlæg',
         [('Drift, alarmer og energi',
           'Alarmer og trends prioriteret efter kritikalitet; vedligeholdsplaner og reservedele; '
           'energiledelse og indregulering med over 40 % lavere forbrug; 5S og standard work.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 teknikere og værkstedsledere · maskinværksted · industrielt udstyr',
         [('Teknisk service og fejlfinding',
           'Reparation, kalibrering og fejlfinding på industrielt udstyr; vagtplanlægning, oplæring og '
           'opfølgning på mål for 12 teknikere.')]),
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
           '**Bosat i Danmark** med arbejds- og opholdstilladelse · **Kørekort B og egen bil** · '
           'Måløv, 20 minutter fra Lynge · Kan starte efter aftale · Referencer på forespørgsel.',
           after=70)

    m.models_table('OPSLAGETS KRAV — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Relevant teknisk baggrund som maskinmester, automatiktekniker, HVAC-/energiingeniør eller elektriker',
         'Elautoriseret maskinmester (LV/MV/HV) 2023; B.Tech i teknologiledelse og maskinteknik '
         '2017-2022 med 7,6/12; køle- og ventilationsteknisk AMU 2021; el- og maskinteknisk '
         'konstruktion 2000-2003, EQF 6.'),
        ('Erfaring med drift og vedligehold af komplekse bygningsinstallationer',
         '5 år som drifts- og vedligeholdelsesleder på et kritisk anlæg i 24/7-drift med ventilation, '
         'pumper, varme, SRO og koblingsanlæg; 11 samtidige anlægsprojekter med ventilation i 2022.'),
        ('Praktiske kompetencer inden for programmering eller konfigurering af CTS/BMS',
         'Sætpunkter, tidsprogrammer, alarmer og reguleringsparametre ændret og optimeret i '
         'SRO/SCADA; egne Python-værktøjer til databehandling og rapportering med over 40 % færre '
         'manuelle timer.'),
        ('Grundlæggende programmering, regulering og optimering i CTS/BMS',
         'Regulering af pumper, blæsere og ventilation i døgndrift med måling og efterfølgende '
         'indregulering; over 40 % lavere energiforbrug dokumenteret over 5 år. Blokprogrammering fra '
         'bunden er ikke det, jeg har gjort mest.'),
        ('Drift, vedligehold og fejlfinding på HVAC, ventilation, CTS/BMS, varme- og kølesystemer samt ATES',
         'Ventilation og indeklima i 11 projekter og i egen virksomhed; køle- og ventilationsteknik '
         'fra AMU 2021; varme og køl driftet i 5 år. ATES har jeg ikke arbejdet med — det er '
         'akkumulering i grundvand, og jeg vil lære anlægget, før jeg rører ved det.'),
        ('Analysere alarmer, trends og fejl og verificere gennem praktisk inspektion, test og fejlfinding',
         'Hypotese stillet på trends og prøvet ved anlægget: følerefterlevelse, kalibrering, tryk og '
         'temperatur; i 37 kapitalprojekter verificeret med FAT/SAT og nul kritiske fund.'),
        ('Overtage selvstændigt ejerskab for udvalgte anlæg',
         'Driftsansvar for hele anlægget i 5 år, herunder vagtordning og prioritering uden at spørge '
         'først; ejer af egen virksomhed siden 2023 med ansvar for autorisation, økonomi og kunder.'),
        ('Planlægge og koordinere forebyggende og korrigerende vedligehold og samarbejde med specialleverandører',
         'Vedligeholdsplaner, reservedele og eksterne montører i 24/7-drift; serviceaftaler og '
         'specialleverandører styret på tid, pris og kvalitet i egen virksomhed med 8 medarbejdere.'),
        ('Dokumentere ændringer, driftsviden, tilbagevendende fejl og tekniske løsninger',
         'Ændringslog, driftsinstruktioner og afvigelser skrevet, så næste vagt kunne overtage; '
         'tjeklister og skabeloner genbrugt på tværs af 37 projekter og i egen virksomhed.'),
        ('Bidrage til tekniske opgraderinger, idriftsættelser og energioptimering',
         'FAT/SAT og idriftsættelse af elektriske anlæg og styringer i 37 projekter; energioptimering '
         'med over 40 % lavere forbrug over 5 år; opgraderinger gennemført uden at stoppe driften.'),
        ('Undersøge hvordan AI kan skabe værdi i Facility Management',
         'Egne værktøjer i Python og Claude i daglig brug til tjeklister, dataanalyse og rapporter — '
         'over 40 % færre manuelle timer; arbejder ud fra, at modellen kun er så god som den rensede '
         'alarm- og trendhistorik, den bygger på.'),
        ('Struktureret tilgang til fejlfinding og gå fra analyse på skærmen til praktisk undersøgelse',
         'Fast rækkefølge: alarm, trend, hypotese, måling ved anlægget, konklusion — brugt i 5 års '
         'døgndrift og i 37 afleveringer; fejlen lukket med årsag, ikke kun med en kvittering.'),
        ('God teknisk dømmekraft for hvad der kan løses internt, og hvornår en ekstern specialist skal ind',
         'Elautorisation og grænsen for, hvad der må udføres af hvem; specialleverandører tilkaldt, '
         'når autorisation eller garanti krævede det, i 11 projekter og i egen virksomhed.'),
        ('Nysgerrighed, læringsparathed og lyst til at samarbejde i et team',
         'Nye systemer taget i brug som superbruger; 5S og standard work indført sammen med dem, der '
         'skulle arbejde i det; oplært 3 lærlinge og 12-14 medarbejdere gennem 20+ år.'),
        ('Evne til at kommunikere og dokumentere tekniske forhold klart på dansk og engelsk',
         'Dansk modersmål og engelsk professionelt, også i tekniske forhandlinger; beslutningsoplæg, '
         'driftsinstruktioner og afvigelsesrapporter skrevet for både teknikere og ledelse i 20+ år.'),
        ('Flydende dansk og gode engelskkundskaber',
         'Dansk som modersmål med 20+ års teknisk og kommerciel kommunikation; engelsk på '
         'professionelt niveau i møder, dokumentation og forhandlinger med leverandører.'),
        ('Bosat i Danmark med gyldig arbejds- og opholdstilladelse',
         'Bosat i Måløv med dansk arbejds- og opholdstilladelse; 20 minutter til Lynge med bil, og '
         'kan være på anlægget samme dag, hvis en alarm kræver det.'),
        ('Interesse for eller erfaring med anvendelse af AI i Facility Management',
         'Bygger og bruger egne AI- og Python-værktøjer i daglig drift: tjeklister, logdata, rapporter '
         'og fejlmønstre — med over 40 % færre manuelle timer som dokumenteret effekt.')])


    m.models_table('DE FØRSTE MÅLINGER — HVAD JEG VILLE SE PÅ, FØR JEG ÆNDRER NOGET',
                   ('Måling', 'Hvad den svarer på, og hvad der sker bagefter'), [
        ('Alarmvolumen pr. døgn og pr. anlæg',
         'Hvor mange alarmer kommer der, og hvor mange bliver der handlet på? De ti hyppigste '
         'alarmer gennemgået med den nuværende specialist — og de, der ikke betyder noget, flyttet '
         'til information i stedet for alarm.'),
        ('Følerefterlevelse på ti udvalgte følere',
         'Stemmer føleren med det, der faktisk sker i rummet? Målt mod en reference, ført ind i '
         'loggen — for en driver på to grader er både et indeklimaproblem og en skjult '
         'energiudgift.'),
        ('Sætpunkt mod faktisk tilstand i tre zoner',
         'Kører reguleringen mod det, nogen har sat, eller mod det, bygningen har brug for? '
         'Afvigelsen dokumenteret pr. zone, så ændringen kan begrundes og ikke bare mærkes.'),
        ('Energiforbrug pr. anlægstype',
         'Hvor ligger forbruget henne, når det normaliseres mod graddage og driftstid? Det er den '
         'rækkefølge, jeg ville arbejde i: måle, forklare, ændre — og så måle igen.')])

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_WSA_TechnicalFacilitySpecialist.docx')
    build(out)
    print(out)
