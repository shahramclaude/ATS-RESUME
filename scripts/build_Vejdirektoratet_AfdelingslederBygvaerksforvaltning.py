# -*- coding: utf-8 -*-
"""Vejdirektoratet — Afdelingsleder til bygværksforvaltning (Hedehusene / Skanderborg).

Dansk leverance: ansøgning side 1 (opgave-først), CV side 2–3, 90 dage + kravmatrix side 4.
Policy: master/README.md — jobbet først, kandidaten kun som bevis; ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Afdelingsleder · Bygværksforvaltning · Drift, vedligehold og asset management'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('7. november 2026')
    m.meta('Vejdirektoratet · Området Befæstelser, Bygværker og Geoteknik · Afdelingen Bygværksforvaltning')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Afdelingsleder til bygværksforvaltning', bold=True, color='1A1A1A')
    m.para('Til områdechef Jakob Schwartz, Befæstelser, Bygværker og Geoteknik', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('4.800 bygværker på statsvejene er ikke en opgaveliste — det er en portefølje, hvor hver bro, tunnel '
           'og pumpebygværk har en tilstand, en levetid og en konsekvens, hvis den ikke bliver håndteret i tide. '
           'Afdelingslederens arbejde er at gøre den portefølje styrbar: at vide hvad der haster, hvad der kan '
           'vente, og hvem der ejer beslutningen — og at gøre det i en balance mellem broteknik, anlægskonstruktion, '
           'trafikafvikling og arbejdsmiljø, hvor der sjældent er ét rigtigt svar, men altid et bedre og et dårligere '
           'grundlag at vælge på. Det er den opgave, jeg søger.', after=80)

    m.para('**Forvaltning er et system, ikke en række enkeltbeslutninger.** Det, afdelingen skal kunne levere, er et '
           'forvaltningsgrundlag, hvor hvert bygværk har en **tilstand**, en **plan** og en **ejer**: eftersyn og '
           'tilstandsvurdering omsat til prioritering, prioritering omsat til et vedligeholdelses- og '
           'investeringsbehov, og behovet omsat til noget, der kan besluttes og finansieres. Uden det system bliver '
           'forvaltning brandslukning, og brandslukning er dyrere end vedligehold — også når den ser billig ud på '
           'det års budget, hvor den bliver udskudt.', after=80)

    m.para('**Asset management er den disciplin, jeg har udøvet i praksis.** Som drifts- og vedligeholdelsesleder på '
           '**Lynetten under Biofos** havde jeg ansvaret for kritiske tekniske anlæg i 24/7-drift: pumper, '
           'blæsere, ventilation, transformere, koblingsanlæg og **SRO/SCADA**. Vi arbejdede med '
           'kritikalitetsvurdering pr. anlægsdel, vedligeholdsplaner, reservedelsbehov og levetid — og med at '
           'prioritere mellem det, der skulle ske nu, og det, der kunne vente til næste budgetår. Energiledelse og '
           'driftsoptimering gav **over 40 % lavere forbrug** dokumenteret, fordi vi målte, flyttede indsatsen og '
           'fulgte op i stedet for at gætte. Den samme systematik er det, der skal bære 4.800 bygværker.', after=80)

    m.para('**OT-driften og de tekniske anlæg er en del af forvaltningen, ikke et tillæg til den.** Pumpebygværker, '
           'vejbelysning, mekaniske og elektriske installationer på store broer og i tunneler styres i dag af '
           'systemer, der skal virke, når nogen har brug for dem — og som ikke kan erstattes uden at tænke på drift, '
           'sikkerhed og overgang. Jeg er **elautoriseret maskinmester (LV/MV/HV)**, har drevet SRO/SCADA i '
           'døgnrift, og har stået i udskiftning og idriftsættelse af styringer med **FAT/SAT og IQ/OQ/PQ** i et '
           'GMP-miljø, hvor et manglende signal betød en stoppet linje. Det er den erfaring, der gør, at en '
           'afdelingsleder kan gå i detaljen med specialisterne uden at overtage deres arbejde.', after=80)

    m.para('**Politisk styret organisation har jeg arbejdet i hele mit lederskab.** Biofos er ejet af kommunerne i '
           'hovedstadsområdet med HOFOR som hovedaktionær: beslutninger bliver til i et samspil mellem faglighed, '
           'politisk valgte bestyrelser, myndighedskrav og borgernes forventning om, at anlægget kører. Jeg har '
           'været på den anden side af bordet i myndighedsdialog og tilsyn, arbejdet efter krav, hvor '
           'dokumentationen skulle kunne fremvises, og samarbejdet med kommuner, rådgivere og leverandører om '
           'løsninger, der skulle holde i årevis. Derfor ved jeg, at et godt fagligt svar også skal kunne forklares '
           'i en politisk sammenhæng — og at det nogle gange er halvdelen af arbejdet.', after=80)

    m.para('**Resultater gennem andre er den eneste form for ledelse, der tæller i en faglig afdeling.** Jeg har '
           'ledet 14 medarbejdere i Ventek-Air, 12 teknikere i ARJ og 8 i min egen virksomhed, og arbejdet sammen '
           'med **25 specialister** på tværs af **37 kapitalprojekter** i Novo Nordisk, hvor ingen af dem havde brug '
           'for en leder, der kunne deres fag — de havde brug for rammer, mandat og en, der holdt kursen, når '
           'dagsordenen blev kompleks. Min opgave er at gøre det tydeligt, hvad den enkelte ejer, at fjerne det, '
           'der står i vejen, og at tage de samtaler, hvor en prioritet skal forsvares over for en, der har ret i '
           'sit fag.', after=80)

    m.para('**Strategiske mål bliver først til resultater, når de har en ejer og en dato.** Jeg har arbejdet med '
           'servicemål, KPI\'er og månedlig rapportering af fremdrift, økonomi og risiko til ledelse og bygherre, '
           'og jeg har bygget de værktøjer, der skulle til for at følge op — i Python og Excel, fordi det var '
           'hurtigere end at vente på et system. I en matrixorganisation som Vejdirektoratets er den tværgående '
           'del af arbejdet mindst lige så vigtigt: at få aftaler på plads med andre afdelinger, rådgivere, leverandører '
           'og forskning, så ansvaret ikke falder mellem to kontorer i Hedehusene og Skanderborg.', after=80)


    m.para('Jeg har base i Måløv, har **kørekort B og egen bil** og kan arbejde fra **Hedehusene** med fast '
           'tilstedeværelse i **Skanderborg**, når opgaven kræver det. Jeg kan gennemgå en **sikkerhedsgodkendelse** og '
           'opretholde den gennem ansættelsen, og jeg kan starte **1. februar 2027**. Jeg har set stillingen hos '
           '**TechJob** og vil gerne høre, hvor I er med den fortsatte udvikling af forvaltningen — og hvilke '
           'prioriteringer der er sværest at få til at hænge sammen i den kommende periode.', after=70)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Drifts-, vedligeholds- og projektleder med 20+ års erfaring fra **kritiske tekniske anlæg**: '
           '**elautoriseret maskinmester (LV/MV/HV)** med B.Tech i teknologiledelse og maskinteknik. Fem år som '
           'drifts- og vedligeholdelsesleder på **Lynetten under Biofos** med **kritikalitetsvurdering, '
           'vedligeholdsplaner, reservedelsstyring og SRO/SCADA** i 24/7-drift, og **over 40 % lavere '
           'energiforbrug** dokumenteret. To år som projektleder på **37 kapitalprojekter** med **25 specialister**, '
           'risikostyring og månedlig rapportering til ledelse og bygherre — **nul kritiske fund** ved aflevering. '
           'Arbejder i en **kommunalt ejet, politisk styret organisation** med myndighedskrav og tilsyn.', after=80)

    m.section('FORVALTNING, DRIFT OG ASSET MANAGEMENT')
    for label, body in [
        ('Kritikalitet og vedligeholdsplaner',
         'Anlægsdele vurderet efter kritikalitet og konsekvens, vedligehold planlagt pr. anlæg, reservedelsbehov og '
         'levetid fastlagt — og prioriteret mod det, der kunne vente, når budgettet ikke rakte til begge dele.'),
        ('Tilstand, data og opfølgning',
         'Driftsdata, alarmer og historik brugt til at flytte indsatsen fra brandslukning til forebyggelse — og '
         'opfølgning på, om handlingen virkede.'),
        ('OT og styringssystemer',
         'SRO/SCADA i døgndrift med ansvar for alarmer, regulering og fejlfinding; udskiftning og idriftsættelse af '
         'styringer med FAT/SAT og IQ/OQ/PQ og dokumenteret aflevering.'),
        ('El- og maskintekniske anlæg',
         'Elautoriseret maskinmester (LV/MV/HV) med erfaring fra transformere, tavler, koblingsanlæg, motorer, '
         'pumper og ventilation — og med ansvaret for, at arbejdet bliver udført af kompetente folk.'),
        ('Kontrakter og leverandører',
         'Serviceaftaler, driftskontrakter og eksterne leverancer fulgt på tid, økonomi og kvalitet — og afvist, når '
         'de ikke holdt det, der stod i kontrakten.'),
        ('Myndigheder og politisk kontekst',
         'Kommunalt ejet selskab med politisk valgte bestyrelser; myndighedskrav og tilsyn efterlevet med '
         'dokumentation, der kunne fremvises, og dialog med kommuner om løsninger og tid.')]:
        m.bullet(label, body, after=25)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · el-autorisation · el-tekniske service- og entrepriseydelser',
         [('Autorisation, kontrakter og drift',
           'Bærer el-autorisationen og ansvaret for, at arbejdet udføres efter gældende krav; serviceaftaler, '
           'prissætning, responstider og betalingsopfølgning; egne digitale værktøjer til kalkulation, tjeklister '
           'og KPI med over 40 % produktivitetsløft.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Portefølje, specialister og interessenter',
           'Kravsspecifikation, risikovurdering, FAT/SAT og IQ/OQ/PQ; fremdrift, økonomi og risiko rapporteret '
           'månedligt til ledelse og bygherre; samspil med rådgivere, leverandører og myndighedskrav — nul kritiske '
           'fund ved aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter · 2–10 mio. kr. pr. opgave',
         [('Kapacitet, prioritering og leverance',
           'Dagligt tavlemøde, kapacitets- og flaskehalsanalyse og omprioritering samme dag, når en maskine eller '
           'et menneske faldt væk; standardiserede arbejdsgange og afleveringspakker styret til deadline.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Lynetten under Biofos · København · aug. 2017–jan. 2022',
         'Kritisk spildevandsanlæg i 24/7-drift · SRO/SCADA · pumper, blæsere, ventilation, transformere, '
         'koblingsanlæg',
         [('Asset management i døgndrift',
           'Kritikalitet, vedligeholdsplaner, reservedele og eksterne montører; vagtordning og beredskab planlagt og '
           'prøvet; 5S og standard work på værksted og lager; energiledelse med over 40 % lavere forbrug.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · industrielt udstyr',
         [('Teknisk drift og fejlfinding',
           'Reparation, klargøring og fejlfinding på industrielt udstyr; vagtplanlægning, oplæring og opfølgning på '
           'mål for 12 teknikere.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('UDDANNELSE OG AUTORISATION')
    m.edu('B.Tech, teknologiledelse og maskinteknik', 'Maskinmesterskolen København · 2017–2022 · gennemsnit 7,6/12')
    m.edu('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('El- og maskinteknisk konstruktion, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Køle- og ventilationsteknik · STCW', 'Mercantec 2021 · Søfartsstyrelsen 2021')

    m.section('SPROG, PRAKTIK OG REFERENCER')
    m.para('Dansk: modersmål, sikkert både mundtligt og skriftligt · Engelsk: professionelt, også teknisk · '
           'Persisk: modersmål · **Kørekort B og egen bil** · Måløv, med fast base i **Hedehusene** og tilstedeværelse '
           'i **Skanderborg** efter behov · Hybrid og hjemmearbejde efter aftale · Kan sikkerhedsgodkendes · '
           'Opstart 1. februar 2027 · Referencer på forespørgsel.', after=70)

    m.models_table('DET AFDELINGEN EFTERSPØRGER — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Lede ca. 20 ingeniører, projektledere og specialister',
         '14 medarbejdere i Ventek-Air med 11 samtidige projekter, 12 teknikere i ARJ og 8 i egen virksomhed; 25 '
         'specialister på tværs af 37 kapitalprojekter i Novo Nordisk.'),
        ('Faglige problemstillinger og dialog med myndigheder, fx kommuner',
         'Myndighedsdialog og tilsyn i kommunalt ejet selskab (Biofos, ejet af kommunerne med HOFOR som '
         'hovedaktionær); krav efterlevet med dokumentation, der kunne fremvises.'),
        ('Understøtte den enkelte medarbejder og løsningen af teamets opgaver',
         'Dagligt tavlemøde og synlig ledelse i døgndrift; MUS, kompetenceplaner og oplæring for 12–14 medarbejdere; '
         'opgaver fordelt efter kompetence og kapacitet med omprioritering samme dag, når noget faldt væk.'),
        ('Understøtte udvikling af forvaltning og bygværker samt forventningsafstemning',
         'Forandringer gennemført sammen med dem, der skulle arbejde i dem — 5S og standard work i døgndrift, '
         'automatiserede arbejdsgange og mål med ejer og dato, aftalt og fulgt op med ledelsen månedligt.'),
        ('Indgå i ledelsesgruppe i området og referere til områdechefen',
         'Medlem af ledergruppen i egen virksomhed og i driftsorganisationen på Lynetten; månedlig rapportering af '
         'fremdrift, økonomi og risiko til ledelse og bygherre.'),
        ('Relevant teknisk eller akademisk baggrund',
         'B.Tech i teknologiledelse og maskinteknik, gennemsnit 7,6/12; elautoriseret maskinmester (LV/MV/HV), '
         'Sikkerhedsstyrelsen 2023; el- og maskinteknisk konstruktion.'),
        ('Erfaren leder med strategisk ledelse og organisationsudvikling',
         '20+ år i tekniske organisationer med ledelsesansvar; strategi omsat til planer med ejer og dato; 37 '
         'projekter leveret gennem andre med nul kritiske fund.'),
        ('Ledelse af specialister med stor faglig ekspertise',
         '25 specialister og projektledere i Novo Nordisk, 14 fagfolk i Ventek-Air og 8 i egen virksomhed; ledelse på '
         'rammer, mandat og opfølgning frem for detailstyring.'),
        ('Forvaltning, drift og vedligehold samt asset management',
         'Fem år med asset management på kritiske anlæg: kritikalitet, vedligeholdsplaner, reservedelsbehov og '
         'levetid, driftsdata og opfølgning — over 40 % lavere energiforbrug dokumenteret.'),
        ('Procesforståelse og navigation i politisk styret organisation',
         'Kommunalt ejet selskab med politisk valgte bestyrelser og GMP-organisation med myndighedskrav og tilsyn; '
         'processer for krav, afvigelser, godkendelser og dokumentation gennemført og vedligeholdt.'),
        ('Strategiske mål til resultater og tværgående samarbejde',
         'Servicemål og KPI\'er omsat til målbare forbedringer (over 40 % på produktivitet og forbrug); '
         'tværgående '
         'samarbejde med andre afdelinger, rådgivere, leverandører og myndigheder i 37 kapitalprojekter.'),
        ('Initiativrig, proaktiv og med overblik i en kompleks dagsorden',
         'Egne værktøjer bygget i Python og Claude, før der var et system; flaskehalse og kapacitet håndteret på 11 '
         'samtidige projekter med daglig prioritering og opfølgning.'),
        ('Relationelle kompetencer, engagement og trivsel',
         'Arbejdsmiljøledelse med sikkerhedsrunder, APV og opfølgning på nærvedhændelser; oplæring og '
         'kompetenceudvikling; teams ført gennem forandringer med åben dialog og klare aftaler.'),
        ('Kendskab til mekaniske og elektriske anlæg samt OT-drift (Operational Technology)',
         'Elautoriseret maskinmester (LV/MV/HV); SRO/SCADA i 24/7-drift med ansvar for alarmer, regulering og '
         'fejlfinding på driftskritiske anlæg; udskiftning og idriftsættelse af styringssystemer med FAT/SAT og '
         'IQ/OQ/PQ.')])
    m.page_break()

    m.models_table('DE FØRSTE 90 DAGE — PORTEFØLJEN, PRIORITERINGEN OG AFDELINGEN',
                   ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'Mød alle ca. 20 medarbejdere på begge tjenestesteder, de øvrige ledere i området og de vigtigste '
         'samarbejdspartnere i andre afdelinger; gennemgå forvaltningsgrundlaget: bygværksfortegnelse, eftersyn, '
         'tilstandsvurderinger og de drifts- og vedligeholdskontrakter, der styrer arbejdet.'),
        ('Dag 30',
         'Billede af porteføljens tilstand og de ti bygværker og anlæg, hvor indsatsen haster mest — med '
         'konsekvens, ejer og næste handling; de åbne sager hos andre myndigheder gennemgået; aftalt kadence for '
         'opfølgning med områdechefen.'),
        ('Dag 60',
         'Afdelingens mål og ansvar lagt fast, så den enkelte specialist kan se, hvad han ejer; prioriteringsmodel '
         'for vedligehold og udskiftning aftalt med specialisterne; plan for den fortsatte udvikling af '
         'forvaltningen med de første to forbedringer udpeget.'),
        ('Dag 90',
         'Første prioritering besluttet på et fælles grundlag og dokumenteret; tværgående aftale på plads med '
         'mindst én anden afdeling om grænseflader og ansvar; og en kompetence- og bemandingsplan, der viser, '
         'hvordan afdelingen kan bære både drift og udvikling.')])

    m.section('FORVALTNING HANDLER OM AT VÆLGE, IKKE OM AT HAVE RET')
    m.para('Når broteknik, trafikafvikling, arbejdsmiljø og økonomi peger i hver sin retning, er der ikke et fagligt '
           'svar, der vinder — der er et grundlag, nogen skal vælge på. Afdelingslederens opgave er at gøre '
           'konsekvensen af hvert valg tydelig: hvad det koster nu, hvad det koster senere, hvem der bliver berørt, '
           'og hvad der sker, hvis vi ikke gør noget. Det er den slags grundlag, specialisterne kan levere, og som '
           'lederen skal sørge for bliver bestilt, kvalificeret og besluttet.', after=80)

    m.section('SPECIALISTER SKAL LEDES PÅ RAMMER, IKKE PÅ DETALJER')
    m.para('En afdeling med 20 ingeniører og specialister har mere faglig viden end deres leder — og skal have det. '
           'Ledelse består i at sætte rammer, prioritere mellem opgaver, sikre at den enkelte har mandat og '
           'rygdækning, og at gå i detaljen, når beslutningen kræver det. Jeg har prøvet begge fejl: at gå for '
           'tæt på og at slippe for tidligt. Det, der virker, er en tydelig aftale om, hvem der beslutter hvad, og '
           'en fast rytme for opfølgning.', after=80)

    m.section('MATRIXORGANISATION KRÆVER, AT GRÆNSEFLADER HAR EN EJER')
    m.para('Når opgaven løses i en matrix med to tjenestesteder, andre afdelinger, rådgivere og leverandører, '
           'opstår de dyre fejl i overgangene: en sag, der ligger hos den forkerte, en kontrakt der ikke dækker, et '
           'behov der bliver opdaget for sent. Jeg har arbejdet med grænseflader hele mit lederskab — mod bygherre, '
           'rådgivere, leverandører og driftsorganisation — og ved, at de skal navngives og aftales, før de bliver '
           'et problem.', after=80)

    m.section('POLITISK STYRET BETYDER, AT FAGLIGHEDEN SKAL KUNNE FORKLARES')
    m.para('Beslutninger om statens bygværker bliver taget i et samspil mellem faglighed, økonomi og politik. Det '
           'stiller krav til, hvordan et grundlag bliver skrevet: kort, præcist, uden skjulte antagelser og med '
           'alternativerne tydeligt beskrevet. Jeg har skrevet ledelses- og bygherrerapportering i årevis og ved, at '
           'det grundlag, der ikke kan læses på to sider, ikke bliver besluttet.', after=80)

    m.section('JEG VIL BLIVE MÅLT PÅ, OM PORTEFØLJEN BLIVER STYRBAR')
    m.para('Om et år skal det kunne ses på tre ting: at der ligger en opdateret tilstandsvurdering for porteføljen '
           'med en prioritering, nogen har besluttet; at de bygværker, hvor indsatsen haster, har en plan og en ejer; '
           'og at specialisterne bruger mere af deres tid på faglige vurderinger end på at lede efter beslutninger. '
           'Lykkes det, er afdelingen ikke bare en, der ved noget om bygværker — den er en, hvis viden bliver brugt, '
           'når der skal vælges.', after=80)

    m.section('SIKKERHED OG ARBEJDSMILJØ ER EN DEL AF FORVALTNINGEN')
    m.para('Vedligehold og eftersyn af bygværker foregår tæt på trafik, i højder og i anlæg, hvor der ikke er plads '
           'til at springe over. Jeg har haft arbejdsmiljøansvaret i døgndrift: sikkerhedsinstruktioner, runder, APV '
           'og opfølgning på nærvedhændelser sammen med arbejdsmiljøgruppen. Det er den samme disciplin, der skal '
           'sikre, at en arbejdsinstruktion ved en bro bliver fulgt — ikke fordi den står i et system, men fordi '
           'nogen har gjort den til en vane.', after=80)


    m.section('SYSTEMER SKAL UNDERSTØTTE FORVALTNINGEN, IKKE ERSTATTE DEN')
    m.para('Data om bygværker er kun værdifulde, hvis de bliver brugt til at flytte en beslutning. Derfor er rækkefølgen '
           'vigtig: først aftale hvad der skal besluttes på hvilket grundlag, derefter hvilke data og hvilket system '
           'der skal levere dem. Jeg har bygget egne værktøjer, fordi det var hurtigere end at vente — og har lært, '
           'hvornår et system giver værdi, og hvornår det bare bliver endnu et sted, nogen skal opdatere.', after=80)

    return m.save(path, title='Afdelingsleder bygværksforvaltning — Vejdirektoratet',
                  subject='Bygværksforvaltning, drift og vedligehold, asset management og OT-drift',
                  keywords='afdelingsleder, bygværksforvaltning, asset management, drift, vedligehold, ot-drift, '
                           'sro, scada, el-tekniske anlæg, myndigheder, politisk styret, matrixorganisation, '
                           'specialister, strategi, kpi, sikkerhedsgodkendelse, dansk')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Vejdirektoratet_AfdelingslederBygvaerksforvaltning.docx')))
