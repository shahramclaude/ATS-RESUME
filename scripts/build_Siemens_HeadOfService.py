# -*- coding: utf-8 -*-
"""Siemens A/S — Head of Service, Smart Infrastructure (Ballerup).

Dansk leverance (opslaget er dansk): ansøgning side 1, CV side 2–3.
Policy: master/README.md — ekstrem sikkerhed, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Head of Service · Serviceforretning, kontrakter og digitalisering'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('6. november 2026')
    m.meta('Siemens A/S · Smart Infrastructure · Head of Service · Ballerup · Job ID 527752')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Head of Service, Smart Infrastructure, Siemens A/S', bold=True, color='1A1A1A')
    m.para('Til Head of Area Danmark og ledergruppen i Smart Infrastructure', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('En serviceaftale er et løfte, der bliver indfriet hver dag — ikke på kontraktdagen, men den tirsdag i '
           'februar, hvor en teknisk installation står stille og kunden venter. Derfor er serviceforretningen en af '
           'de sværeste at modernisere: kontrakten skal prises på noget, der kan måles, leverancen skal kunne '
           'holdes af mennesker, der har mandat, og digitaliseringen skal fjerne et besøg i stedet for at tilføje '
           'et dashboard. Det er præcis den opgave, jeg søger.', after=80)

    m.para('**Jeg ville udvikle serviceforretningen på fire faste ting.** Først **serviceaftalen er produktet**: '
           'den skal beskrive responstider, oppetid, data og hvad der sker, når noget ikke kan løses — og prisen '
           'skal afspejle den risiko, vi reelt tager, så avancen ikke forsvinder i år to. For det andet '
           '**digitalisering skal fjerne et besøg, ikke tilføje et system**: data fra den installerede base skal '
           'give fjernovervågning, bedre fejlfinding og færre køreture, og de digitale services skal indgå i '
           'kontrakten og i prisen, ikke ligge ved siden af som et projekt. For det tredje **KPI\'er skal kunne '
           'forklares af dem, der leverer dem**: responstid, first-time-fix, oppetid, kundetilfredshed og '
           'lønsomhed målt så tæt på opgaven, at den enkelte tekniker kan handle på dem. For det fjerde '
           '**forandring sker gennem mellemledere**: jeg leder gennem andre ved at give ledere mandat, klare mål '
           'og rygdækning, når det bliver ubehageligt — ikke ved at gå uden om dem.', after=80)

    m.para('Jeg kommer fra serviceforretningen, ikke fra en stab. Siden 2023 har jeg drevet **ELOHVAC** med fuldt '
           'P&L — en el-teknisk service- og entreprisevirksomhed med **fem elektrikere og tre lærlinge** — hvor jeg '
           'selv har sat priser, skrevet kontrakter, planlagt responstider, faktureret og fulgt op på, om '
           'aftalerne også var lønsomme efter år ét. Jeg har bygget kundeflow, tjeklister og opfølgning i Python '
           'og Claude, fordi det var hurtigere end at vente på et system, og det har givet **over 40 % '
           'produktivitetsløft** — ikke som et projekt, men som en ændring i den måde arbejdet bliver udført på.',
           after=80)

    m.para('Før det var jeg i **fem år drifts- og vedligeholdelsesleder på Lynetten under Biofos**, et kritisk '
           'anlæg i 24/7-drift: pumper, blæsere, ventilation, transformere, koblingsanlæg og SCADA. Det var '
           'vedligeholdelse som kontrakt med sig selv — kritikalitet, reservedele, eksterne montører, '
           'vagtordning og målinger, der viste, om planen holdt. Energiledelsen gav **over 40 % lavere forbrug '
           'dokumenteret**, og 5S og standard work på værksted og lager var det, der gjorde, at en ny tekniker '
           'kunne levere noget, der lignede det samme, som den erfarne gjorde.', after=80)

    m.para('Skaleringen og det kommercielle har jeg fra **Ventek-Air**, hvor jeg ledede **14 medarbejdere og 11 '
           'samtidige projekter** med dagligt tavlemøde og kapacitetsstyring, og fra **Novo Nordisk**, hvor jeg '
           'stod med **37 parallelle kapitalprojekter** med 25 specialister, 2–10 mio. kr. pr. projekt, '
           'kravsspecifikation, **FAT/SAT og IQ/OQ/PQ** og månedlig rapportering af fremdrift, økonomi og risiko '
           'til ledelsen. Det er den samme disciplin, en serviceorganisation skal have: en aftale, der bliver '
           'oversat til en plan, en plan der bliver målt, og et tal nogen tør tage ansvar for.', after=80)

    m.para('Service er den eneste del af forretningen, hvor kunden betaler for at undgå noget, der ikke er sket '
           'endnu. Det gør økonomien anderledes end i projektsalg: indtægten er tilbagevendende, men avancen bliver '
           'spist år for år, hvis antallet af besøg stiger, mens prisen står stille. Derfor følger jeg tre tal '
           'tættere end alle andre — aftalens dækning, antallet af udrykninger pr. anlæg og andelen af sager, der '
           'bliver løst i første forsøg — fordi det er dem, der afgør, om forretningen vokser, eller bare bliver '
           'større.', after=80)

    m.para('Og for at sige det direkte: jeg leder gennem andre. Jeg har selv stået med værktøjet i hånden og ved, '
           'hvad det koster at få en beslutning, der ikke kan forklares på gulvet. Derfor giver jeg lederne mål og '
           'mandat og holder mig til at spørge til resultatet og til at tage de samtaler, der er svære — også når '
           'det er mig, der skal sige, at vi ikke leverede som lovet.', after=80)

    m.para('Det, der især tiltrækker mig ved Siemens Smart Infrastructure, er, at I har det, de fleste '
           'serviceforretninger mangler: en installeret base i danske bygninger — bygningsautomatik, sikkerhed og '
           'elfordeling — data fra den og teknologien til at bruge dem. '
           'Digitalisering i service bliver først forretning, når den ændrer kontrakten — når fjernovervågning '
           'bliver et lavere responstidsløfte til en anden pris, når data bliver et mersalg, og når kunden kan se, '
           'hvad de får for abonnementet. Det er den samtale, jeg gerne vil føre med jeres nøglekunder, og det er '
           'den, jeg har ført med mine egne.', after=80)

    m.para('Praktisk: jeg bor i Måløv, har **kørekort B og egen bil**, og Ballerup er inden for rækkevidde i '
           'hverdagen. Jeg arbejder gerne hybridt og på stedet efter behov, kommunikerer på dansk og engelsk, og '
           'kan starte efter aftale. Jeg vil gerne høre, hvordan I i dag måler serviceleverancen, og hvor '
           'kontrakterne holder jer tilbage fra at sælge de digitale services — det er der, jeg ville begynde.',
           after=70)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Service- og driftsleder med 20+ års erfaring fra teknisk service, drift og projekter — elautoriseret '
           'maskinmester (LV/MV/HV) med B.Tech i teknologiledelse og maskinteknik. Har drevet egen el-teknisk '
           'servicevirksomhed med fuldt P&L siden 2023: prissætning, serviceaftaler, responstider, fakturering og '
           'lønsomhed, med **over 40 % produktivitetsløft** fra egne digitale værktøjer. Fem år som drifts- og '
           'vedligeholdelsesleder på et kritisk anlæg i 24/7-drift med kritikalitet, reservedele, eksterne '
           'montører, vagtordning og **over 40 % lavere energiforbrug** dokumenteret. Har ledet 14 medarbejdere og '
           '11 samtidige projekter samt 37 kapitalprojekter med 25 specialister. Leder gennem mål, mandat og '
           'opfølgning — ikke gennem møder.', after=80)

    m.section('SERVICE, KUNDER OG RESULTATER')
    for label, body in [
        ('Serviceaftaler og kontrakter',
         'Priser, responstider, leveranceomfang og betalingsvilkår sat og holdt i egen virksomhed; aftaler '
         'revurderet, når omkostningerne flyttede sig, så avancen ikke forsvandt i år to.'),
        ('Kommerciel serviceforretning',
         'Salg, mersalg og kundedialog med fuldt P&L: nye kunder, tilbagevendende aftaler, kalkulation pr. '
         'opgave og et dækningsbidrag, der blev fulgt månedligt.'),
        ('Kundetilfredshed og kvalitet',
         'Leverance målt på det, kunden oplever: responstid, first-time-fix og dokumentation — og de svære '
         'samtaler taget direkte, når noget ikke blev leveret som lovet.'),
        ('Digitalisering og data',
         'Egne værktøjer i Python og Claude til tjeklister, kalkulation, opfølgning og dashboards; manuelle '
         'arbejdsgange automatiseret med over 40 % produktivitetsløft.'),
        ('Performance og budget',
         'Budget, ressourceallokering og KPI\'er med fuldt P&L; 37 kapitalprojekter med månedlig rapportering af '
         'fremdrift, økonomi og risiko til ledelsen og nul kritiske fund ved aflevering.'),
        ('Ledelse gennem andre',
         '14 medarbejdere i Ventek-Air, 12 teknikere i ARJ og 8 i egen virksomhed — mål og mandat givet videre, '
         'kompetenceudvikling, opfølgning på dato og rygdækning, når beslutningen blev upopulær.')]:
        m.bullet(label, body, after=25)

    m.models_table('VÆRKTØJER OG METODER', ('Område', 'Dokumenteret brug'), [
        ('Service og kontrakt',
         'Aftaleomfang, responstider, eskalering og prissætning pr. kunde; kontraktgennemgang med fokus på, hvad '
         'der kan måles, og hvem der bærer risikoen.'),
        ('Performance og KPI',
         'KPI-tavler, responstid, first-time-fix, oppetid og dækning; månedlig opfølgning og forbedringer målt før '
         'og efter.'),
        ('Digitalisering',
         'Data fra drift og SCADA, dashboards og automatiserede rapporter i Python og Claude; arbejdsgange '
         'designet, så systemet bliver brugt frem for omgået.'),
        ('Drift og vedligehold',
         'Kritikalitet, vedligeholdsplaner pr. anlæg, reservedelsbehov og eksterne montører; 5S og standard work '
         'som grundlag for ensartet leverance.'),
        ('Projekter og leverance',
         'Kravspecifikation, FAT/SAT, IQ/OQ/PQ og afleveringspakker; fremdrift, økonomi og risiko rapporteret '
         'månedligt.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · el-tekniske service- og entrepriseydelser',
         [('Service som forretning',
           'Prissætning, serviceaftaler, responstider, fakturering og betalingsopfølgning; daglig drift med kunder '
           'og medarbejdere og selv med i opgaverne; egne digitale værktøjer til kalkulation, tjeklister og KPI '
           'med over 40 % produktivitetsløft.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Portefølje, leverance og interessenter',
           'Kravsspecifikation, FAT/SAT og IQ/OQ/PQ ved modtagelse og idriftsættelse; fremdrift, økonomi og risiko '
           'rapporteret månedligt til ledelse og bygherre; nul kritiske fund ved aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter · 2–10 mio. kr. pr. opgave',
         [('Kapacitet og leverance til dato',
           'Dagligt tavlemøde, kapacitets- og flaskehalsanalyse og omprioritering samme dag, når en maskine eller '
           'et menneske faldt væk; standardiserede arbejdsgange og afleveringspakker styret til deadline.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Lynetten under Biofos · København · aug. 2017–jan. 2022',
         'Kritisk procesanlæg i 24/7-drift · pumper, blæsere, ventilation, transformere, koblingsanlæg og SCADA',
         [('Vedligehold som kontrakt med sig selv',
           'Kritikalitet, vedligeholdsplaner, reservedele og eksterne montører i døgndrift; vagtordning planlagt og '
           'arbejdet; 5S og standard work på værksted og lager; energiledelse med over 40 % lavere forbrug.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · industrielt udstyr',
         [('Teknisk service og fejlfinding',
           'Reparation, klargøring og fejlfinding på industrielt udstyr; vagtplanlægning, oplæring og opfølgning '
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
    m.edu('El- og maskinteknisk konstruktion, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Køle- og ventilationsteknik · STCW', 'Mercantec 2021 · Søfartsstyrelsen 2021')

    m.section('SPROG, PRAKTIK OG REFERENCER')
    m.para('Dansk: modersmål · Engelsk: professionelt · Persisk: modersmål · Kørekort B og egen bil · Bor i Måløv, '
           'Ballerup inden for rækkevidde · Hybrid og på stedet efter behov · Kan starte efter aftale · SAP og '
           'Excel dagligt, Python til data og systemer · Referencer på forespørgsel.', after=70)

    m.models_table('DET DE EFTERSPØRGER — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Erfaring med at udvikle og professionalisere en serviceforretning',
         'Bygget og drevet egen el-teknisk servicevirksomhed siden 2023 med aftaler, responstider, prissætning og '
         'lønsomhed; fem år med vedligehold som leverance på et kritisk anlæg i døgnrift.'),
        ('Stærk kommerciel forståelse og erfaring med serviceaftaler og kontraktmodeller',
         'Fuldt P&L med kalkulation, kontrakter, fakturering og betalingsopfølgning; aftaler revurderet, når '
         'omkostningerne flyttede sig, så dækningen holdt.'),
        ('Digitale services, data og nye teknologier omsat til værdi',
         'Egne værktøjer i Python og Claude til tjeklister, kalkulation, opfølgning og dashboards med over 40 % '
         'produktivitetsløft; data fra SCADA og drift brugt til beslutninger, ikke til rapporter.'),
        ('Analytisk og datadrevet med aktiv brug af KPI\'er',
         'KPI-tavler og månedlig opfølgning på omsætning, dækning, responstid og kvalitet; analyse af hvorfor tallet '
         'flyttede sig, procesoptimering og forbedringer målt før og efter i stedet for beskrevet.'),
        ('Strategisk udsyn kombineret med operationel forståelse',
         'En strategi for serviceforretningen oversat til planer med ejer og dato i egen virksomhed og i 37 '
         'kapitalprojekter; arbejder '
         'selv med i opgaverne, når det er det, der får leverancen i mål.'),
        ('Budget, ressourceallokering og performance',
         'Fuldt P&L med budget og ressourcestyring; balancen mellem kundetilfredshed, kvalitet, effektivitet og '
         'lønsomhed fulgt månedligt på tværs af 14 medarbejdere og 37 projekter med 25 specialister.'),
        ('Lede, motivere og udvikle ledere og medarbejdere',
         '14 medarbejdere i Ventek-Air, 12 teknikere i ARJ og 8 i egen virksomhed; mål og mandat givet videre med '
         'opfølgning på dato og rygdækning, når beslutningen blev upopulær.'),
        ('Forandring og forankring i organisationen',
         'Forandringsledelse i praksis: standard work, 5S og PDCA indført i døgndrift; arbejdsgange automatiseret, så '
         'ændringen blev en del af '
         'den daglige rutine frem for et projekt, der døde efter første kvartal.'),
        ('Kundeoplevelse og relationer til nøglekunder',
         'Hele kunderejse-forløbet fra aftale til aflevering med fuldt ansvar i egen virksomhed; kundedialog og '
         'eskalering; samspil '
         'med bygherre, rådgivere og '
         'leverandører i 37 projekter med nul kritiske fund.'),
        ('Kommunikation fra drift til direktion',
         'Månedlig skriftlig rapportering til ledelse og bygherre med fremdrift, økonomi og risiko; daglige '
         'tavlemøder med teknikerne og bestyrelsesmateriale i egen virksomhed.')])
    m.page_break()

    m.models_table('DE FØRSTE 90 DAGE — KUNDERNE, KONTRAKTERNE OG ORGANISATIONEN',
                   ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'Mød lederne i serviceorganisationen og de fem største kunder; læs de ti vigtigste serviceaftaler igennem '
         'for leveranceomfang, responstider, pris og hvad der ikke er dækket — og se, hvordan leverancen måles i '
         'dag.'),
        ('Dag 30',
         'Én fælles KPI-struktur for serviceleverance (responstid, first-time-fix, oppetid, kundetilfredshed og '
         'dækning) synlig for ledergruppen; en liste over de aftaler, hvor kontrakten ikke følger teknologien; '
         'aftalt kadence for ledelsesopfølgning.'),
        ('Dag 60',
         'To konkrete servicekoncepter skitseret — fx et digitalt baseret responstidsløfte og et '
         'vedligeholdelsesabonnement med data — med pris, risiko og krav til leverance; lederne har fået egne mål '
         'og mandat.'),
        ('Dag 90',
         'Servicestrategien lagt frem for Head of Area med mål, ejere og datoer; første moderniserede aftale ude '
         'hos en kunde; og en plan for, hvordan de digitale services kommer ind i kontraktgrundlaget i stedet for '
         'at ligge ved siden af.')])

    m.section('EN SERVICEAFTALE ER ET LØFTE, DER BLIVER INDFRIET HVER DAG')
    m.para('Kontrakten bliver underskrevet én gang, men leveret hver dag — af en tekniker, der har travlt, og af en '
           'planlægger, der har tre andre opgaver. Derfor er det ikke dokumentet, der afgør kundetilfredsheden; det '
           'er, om løftet kan holdes af den bemanding og de systemer, der reelt er til rådighed. En servicechefs '
           'vigtigste arbejde er at gøre forskellen mellem de to så lille som muligt.', after=80)

    m.section('DIGITALISERING SKAL FJERNE ET BESØG, IKKE TILFØJE ET DASHBOARD')
    m.para('Den installerede base fortæller os noget, kunden endnu ikke ved: at et filter er ved at være tæt, at en '
           'pumpe kører med en anden vibration, at en styring har skiftet adfærd. Hvis de data bliver til endnu et '
           'dashboard, har vi brugt penge på at vide noget, vi ikke handler på. De skal blive til færre køreture, '
           'hurtigere fejlfinding og et løfte til kunden, der er bedre end det, konkurrenten kan give — og de skal '
           'ind i kontrakten og prisen, ikke ligge ved siden af.', after=80)

    m.section('KPI\'ER DER IKKE KAN FORKLARES AF DEM, DER LEVERER DEM, BLIVER IKKE BRUGT')
    m.para('Responstid, first-time-fix og oppetid er kun nyttige, hvis den enkelte tekniker kan se, hvad hans '
           'beslutning betød for tallet. Det betyder målinger tæt på opgaven, få tal og en fast rytme, hvor de '
           'bliver gennemgået med dem, der ejer dem. Jeg har set dashboards, der var smukke og døde efter to '
           'måneder; de døde, fordi de blev bygget til ledelsen og ikke til dem, der skulle handle.', after=80)

    m.section('KONTRAKTEN SKAL FØLGE MED TEKNOLOGIEN')
    m.para('De fleste serviceaftaler er skrevet i en verden, hvor et besøg var den eneste leverance, og hvor '
           'responstid var det eneste løfte. Når overvågning, data og fjernsupport kommer ind, ændrer risikoen sig '
           '— og dermed prisen og ansvaret. Derfor skal kontrakterne moderniseres aktivt: hvad er leverancen nu, '
           'hvad koster den at levere, hvad gør vi, når kunden selv kan se fejlen, og hvem hæfter, hvis '
           'fjernovervågningen ikke fangede den — og en leverancemodel, der kan beskrives i kontrakten, før den bliver '
           'solgt. Det er ikke en juridisk øvelse; det er en kommerciel.', after=80)

    m.section('ET ABONNEMENT ER ET LØFTE OM DRIFT, IKKE EN RABATORDNING')
    m.para('Abonnements- og kontraktmodeller virker, når kunden køber et resultat — at anlægget kører, at '
           'temperaturen holder, at energiforbruget falder — og ikke når de blot fordeler den samme regning over '
           'tolv måneder. Det kræver, at vi kan måle resultatet, at vi tør sætte et tal på det, og at vi har en '
           'leverance, der kan bære løftet. Det er den slags mersalg, der holder i årevis, fordi kunden ikke kan '
           'komme tilbage til udgangspunktet.', after=80)

    m.section('FORANDRING SKER GENNEM MELLEMLEDERE')
    m.para('En serviceorganisation ændrer sig ikke, fordi direktionen beslutter det, men fordi mellemlederne gør '
           'noget andet på mandag. Derfor bruger jeg min tid på dem: klare mål, mandat til at træffe beslutningen '
           'og rygdækning, når den er upopulær — og en åben samtale om, hvad der ikke virker, uden at nogen skal '
           'holde masken. Det er også dem, der ved, hvorfor kunden er utilfreds, længe før tallet viser det — og '
           'det er på ledergruppe-niveau, beslutningen om at ændre kadence og mandat skal tages.', after=80)

    m.section('JEG HAR SOLGT SERVICE OG LEVERET DEN SELV')
    m.para('I egen virksomhed har jeg stået med begge sider: prisen, jeg satte, og den fredag eftermiddag, hvor '
           'opgaven tog tre timer mere, end den skulle. Det har givet en vane, som jeg tager med i en større '
           'organisation: en aftale, jeg ikke kan levere med den bemanding, jeg har, skal jeg ikke sælge — og en '
           'aftale, jeg kan levere, skal prises, så den også er værd at levere om to år.', after=80)

    return m.save(path, title='Head of Service — Siemens A/S, Smart Infrastructure',
                  subject='Serviceforretning, serviceaftaler, digitalisering og performance',
                  keywords='head of service, serviceforretning, serviceaftaler, kontraktmodeller, digitale '
                           'services, digitalisering, abonnement, kundetilfredshed, KPI, performance, budget, '
                           'servicestrategi, forandringsledelse, datadrevet, dansk, engelsk')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Siemens_HeadOfService.docx')))
