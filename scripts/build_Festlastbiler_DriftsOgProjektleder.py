# -*- coding: utf-8 -*-
"""Festlastbiler.dk / Jørgensen-gruppen — Drifts- og projektleder.

Dansk leverance (opslaget er dansk): ansøgning side 1, CV side 2–3.
Policy: master/README.md — ekstrem sikkerhed, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Drifts- og projektleder · Ansvar, sæson og udvikling i en portefølje af virksomheder'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('6. november 2026')
    m.meta('Festlastbiler.dk · Jørgensen-gruppen · Drifts- og projektleder')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Drifts- og projektleder, Festlastbiler.dk', bold=True, color='1A1A1A')
    m.para('Til Mads og Bjørn Jørgensen', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('En studenterkørsel er ikke et år. Den er ti dage, hvor 22 lastbiler, omkring 30 chauffører og 3.000 '
           'studenter skal ramme det rigtige sted på det rigtige tidspunkt — og otte måneder, hvor man forbereder '
           'dem. Det er den slags virksomhed, jeg søger: hvor resultatet bliver afgjort i maj, længe før den første '
           'student kravler op på ladet, og hvor der ikke er nogen, der fanger fejlen for en. Jeg har drevet '
           'virksomhed med fuldt ansvar i tre år, og jeg har stået med 11 samtidige projekter og 37 '
           'anlægsprojekter, hvor planlægningen enten holdt eller ikke gjorde. Nu vil jeg gerne have ansvaret for en '
           'virksomhed, hvor jeg kan se virkningen på bundlinjen — og for en portefølje, der vokser.', after=80)

    m.para('**Jeg ville drive Festlastbiler på fire faste ting.** Først **planlægning baglæns fra første køredag**: '
           'en masterplan pr. bil og pr. dag — syn, reparationer, godkendelser, kontrakter, betalinger og '
           'bemanding — med milepæle i februar og marts, så juni er gennemførelse og ikke opdagelse. For det andet '
           '**chauffører er en rekrutterings- og oplæringsopgave, ikke en kalenderpost**: tidlig rekruttering, '
           'fast oplæring og tjekliste pr. bil, en tydelig ansvarlig pr. køredag og en plan for sygdom, for 30 '
           'mennesker på ti dage falder fra hinanden, hvis ikke nogen har tænkt over, hvem der kører i stedet. For '
           'det tredje **økonomien styres ugentligt i sæsonen**: omsætning pr. tur, kapacitetsudnyttelse, '
           'omkostning pr. bil og betalingsstatus — ikke et regnskab, der bliver læst til august. For det fjerde '
           '**systemer og automatisering skal fjerne manuelt arbejde, inden sæsonen starter**: CRM, booking, '
           'kontrakter, betalinger og dokumentation, og det, systemet ikke kan, bygger jeg selv i Python og Claude, '
           'som jeg har gjort i min egen virksomhed med over 40 % dokumenteret produktivitetsløft.', after=80)

    m.para('Jeg kender det med at have ansvaret for alt. Siden 2023 har jeg drevet **ELOHVAC** med fuldt P&L: '
           'salgsprocessen og tilbud, kontrakter, prissætning, fakturering og betalingsopfølgning, **fem elektrikere '
           'og tre lærlinge** og en hverdag, hvor kunden ringer, hvis noget ikke bliver leveret. Der er ingen '
           'arm at læne sig op ad, og der er ingen, der retter fejlen bagud. Det er den samme rolle, jeg søger hos '
           'jer: ansvar for omsætning, omkostninger og indtjening på én gang — og ansvar for at motivere det '
           'ledelsesteam, der skal levere den. Jeg har været projektleder, driftsleder og ejer, og det er '
           'ejerrollen, der ligner jeres mest.', after=80)

    m.para('Planlægning under pres og mange bevægelige dele har jeg prøvet i stor skala. I **Ventek-Air** ledede jeg '
           '**14 medarbejdere og 11 samtidige projekter** med dagligt tavlemøde, kapacitetsstyring og standardiserede '
           'arbejdsgange — leverancer, der skulle gå op i en hverdag, hvor en bil, en maskine eller et menneske '
           'kunne forsvinde. På **Novo Nordisk** styrede jeg **37 parallelle anlægsprojekter** med 25 specialister, '
           '2–10 mio. kr. pr. projekt, og rapporterede fremdrift, økonomi og risiko hver måned. Og fra **Lynetten '
           'under Biofos** kender jeg den del, der handler om materiel: koordinering af vedligehold, reparation og '
           'reservedele med mekanikere og eksterne leverandører i et døgnmiljø, hvor bilen — eller pumpen — ikke '
           'måtte stå stille, fordi nogen havde glemt at bestille delen.', after=80)

    m.para('Jeg er også den, der tager fat selv. Jeg har stået på byggepladser og i værksteder, jeg har koordineret '
           'håndværkere og underentreprenører, og jeg har bygget systemer, fordi det var hurtigere end at vente på '
           'et projekt: CRM-lignende opfølgning, tilbudsberegning, tjeklister og KPI-dashboards i Python og Claude. '
           'Det betyder ikke, at jeg laver reparationerne — det betyder, at jeg kan tale med mekanikeren om, hvad der '
           'skal ske først, og at jeg kan se på tallene, om det, vi gør, også virker.', after=80)

    m.para('Det, der især tiltrækker mig ved jer, er kombinationen: en drift, der skal køre perfekt i ti dage, og '
           'udviklingsprojekter resten af året — hytter, bookingsystem, adgangssystem, opkøb. Jeg har arbejdet med '
           'den slags projekter hele mit arbejdsliv: projektering, budget, godkendelser fra myndigheder, '
           'leverandører og koordinering på tværs. Og jeg har prøvet at drive forretningsudvikling og vurdere, '
           'hvad en virksomhed er værd at bygge videre på: den '
           'øvelse består i at forstå kundestrømmen, kapaciteten, omkostningsdriverne og det, der faktisk skaber '
           'overskuddet — det er præcis det, jeg gør hver måned i min egen virksomhed.', after=80)

    m.para('Praktisk: jeg bor i Måløv, har **kørekort B og egen bil**, og både kontoret i Vanløse og pladsen ved '
           'Sorø er inden for rækkevidde i hverdagen. Jeg kan arbejde de lange dage i juni og i weekenderne, når '
           'sæsonen kræver det, og jeg kan starte efter aftale. En resultatbaseret bonus passer mig fint: ansvar '
           'skal kunne ses på resultatet. Jeg vil gerne høre, hvordan I i dag styrer '
           'bemandingen til de ti køredage, og hvad der skal være på plads i marts for at sæsonen bliver en succes — '
           'det er der, jeg ville begynde.', after=70)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Drifts- og projektleder med 20+ års erfaring fra tekniske virksomheder, anlægsprojekter og 24/7-drift — '
           'elautoriseret maskinmester (LV/MV/HV) med B.Tech i teknologiledelse og maskinteknik. Har drevet egen '
           'virksomhed med fuldt P&L siden 2023: salg, kontrakter, prissætning, fakturering, betalingsopfølgning og '
           'indtjening. Har ledet 14 medarbejdere og 11 samtidige projekter samt 37 anlægsprojekter med 25 '
           'specialister. Bygger selv de systemer, der mangler — CRM-flow, kalkulation, tjeklister og dashboards i '
           'Python og Claude, med over 40 % dokumenteret produktivitetsløft. Struktureret, selvstændig og vant til '
           'at træffe beslutninger, når der er mange bevægelige dele.', after=80)

    m.section('DRIFT, PROJEKTER OG KOMMERCIELT ANSVAR')
    for label, body in [
        ('Drift og planlægning',
         'Masterplan baglæns fra deadline: milepæle, kapacitet, bemanding og afhængigheder lagt fast i en fast struktur, så '
         'gennemførelsen er planlagt og ikke opdaget; daglig tavle og ugentlig opfølgning i de perioder, hvor der '
         'ikke er plads til overraskelser.'),
        ('Ledelse og rekruttering',
         'Rekruttering og oplæring af 5 til 14 medarbejdere i fire forskellige virksomheder; vagt- og '
         'kapacitetsplanlægning, tjeklister, oplæring for nye og de svære samtaler taget direkte og tidligt.'),
        ('Salg, kunder og betaling',
         'Salgsproces, tilbud og kontrakter, prissætning, fakturering og betalingsopfølgning med fuldt P&L; kunder '
         'der forventer svar, og en økonomi der skal hænge sammen hver måned — ikke kun ved årets udgang.'),
        ('Økonomi og resultater',
         'Omsætning, omkostninger og dækning fulgt månedligt; kalkulation pr. opgave og pr. bil, budgetter der '
         'bliver brugt til at styre med, og forbedringer der bliver målt før og efter.'),
        ('Systemer og automatisering',
         'CRM- og opfølgningsflow, digitalisering, bookingsystemer og adgangssystem implementeret i samarbejde med brugerne; manuelle '
         'arbejdsgange automatiseret i Python og Claude med over 40 % dokumenteret produktivitetsløft.'),
        ('Teknisk koordinering',
         'Syn, service og reparationer koordineret med mekanikere og eksterne værksteder i 24/7-drift og på '
         'byggepladser: hvad skal ske først, hvem gør det, hvornår er delen hjemme, og hvad gør vi, hvis den ikke '
         'er.')]:
        m.bullet(label, body, after=25)

    m.models_table('VÆRKTØJER OG METODER', ('Opgave', 'Værktøj og dokumenteret brug'), [
        ('Projektstyring',
         'Milepæle, afhængigheder, risikolog og fremdriftsopfølgning på 37 anlægsprojekter og 11 samtidige '
         'entrepriser; dagligt tavlemøde i gennemførelsesfasen.'),
        ('Økonomi og kalkulation',
         'Tilbud og kalkulation, budgetter, månedsafslutning, dækningsopfølgning og fakturering på eget P&L; SAP '
         'til ordrer, økonomi og aktiver.'),
        ('Salg og kunder',
         'Salgsproces fra første henvendelse til kontrakt og betaling; opfølgning på tilbud, kundekommunikation og '
         'rykkerflow.'),
        ('Systemer og data',
         'CRM- og opfølgningsflow, Excel og Power Query, Python og Claude til dashboards, automatiserede rapporter '
         'og tjeklister.'),
        ('Teknisk koordinering',
         'Vedligeholds- og reparationsplaner pr. enhed, reservedelsbehov, leverandør- og værkstedskontakt samt '
         'myndighedskrav som syn og godkendelser.'),
        ('Ledelse',
         'MUS og 1:1, rekruttering, oplæring og kompetencematrix, sygefraværsopfølgning og prioritering af opgaver '
         '— ansvar givet videre med mandat.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · el-tekniske service- og entrepriseydelser',
         [('Fuldt operationelt ansvar og kommercielt ansvar',
           'Salg, tilbud og kontrakt, prissætning, indkøb, fakturering og betalingsopfølgning; daglig drift med '
           'kunder, medarbejdere og leverandører, og månedlig opfølgning på omsætning, omkostninger og dækning; '
           'egne Python/Claude-værktøjer til kalkulation, tjeklister og KPI med over 40 % produktivitetsløft.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Portefølje, økonomi og interessehavere',
           'Fremdrift, økonomi og risiko på 37 projekter rapporteret månedligt til ledelse og bygherre; tværfaglig '
           'ledelse af 25 specialister og samspil med rådgivere, leverandører og entreprenører; nul kritiske fund '
           'ved aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter · 2–10 mio. kr. pr. opgave',
         [('Mange bevægelige dele på én gang',
           'Daglige tavlemøder, kapacitets- og flaskehalsanalyse, omprioritering samme dag når en maskine eller et '
           'menneske faldt væk; udbud, underentreprenører og afleveringspakker styret til deadline.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Lynetten under Biofos · København · aug. 2017–jan. 2022',
         'Kritisk procesanlæg i 24/7-drift · pumper, blæsere, ventilation, transformere, koblingsanlæg og SCADA',
         [('Materiel, mekanikere og myndighedskrav',
           'Vedligehold, reparation og reservedele koordineret med mekanikere og eksterne leverandører i døgndrift; '
           '5S og standard work på værksted og lager; energiledelse med over 40 % lavere forbrug dokumenteret.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · industrielt udstyr',
         [('Værksted og klargøring',
           'Klargøring, reparation og fejlfinding på industrielt udstyr; vagtplanlægning, oplæring og opfølgning på '
           'mål for 12 teknikere.')]),
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
           'kontoret i Vanløse og pladsen ved Sorø inden for rækkevidde · Kan arbejde lange dage og weekender i '
           'sæsonen · Kan starte efter aftale · SAP og Excel dagligt, Python til data og systemer · Referencer på '
           'forespørgsel.', after=70)

    m.models_table('DET DE EFTERSPØRGER — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Drift og planlægning af en sæson eller en periode med faste deadlines',
         '11 samtidige entrepriser med dagligt tavlemøde og kapacitetsstyring; 37 anlægsprojekter med milepæle og '
         'månedlig fremdriftsrapportering; masterplaner lagt baglæns fra leveringsdato.'),
        ('Ledelse og rekruttering af et større antal medarbejdere',
         '14 medarbejdere i Ventek-Air, 12 teknikere i ARJ, 5 elektrikere og 3 lærlinge i egen virksomhed — '
         'rekruttering, oplæring, vagtplanlægning og opfølgning, også når nogen faldt væk.'),
        ('Salg, kundekommunikation, kontrakter og betalingsopfølgning',
         'Salgsproces, tilbud og kontrakt, prissætning, fakturering og rykkerflow drevet med fuldt P&L i egen '
         'virksomhed siden 2023; kunder der ringer, hvis noget ikke er leveret.'),
        ('Økonomi: omsætning, omkostninger og forbedret indtjening',
         'Månedsafslutning og dækningsopfølgning på eget P&L; kalkulation pr. opgave; forbedringer målt før og efter, '
         'fx over 40 % produktivitetsløft gennem automatisering.'),
        ('Systemer og automatisering — CRM og arbejdsgange',
         'Opfølgnings- og CRM-flow, kalkulations- og tjeklisteværktøjer samt dashboards bygget i Python og Claude; '
         'implementering sammen med brugerne, så det bliver brugt efter den første uge.'),
        ('Teknisk koordinering: syn, reparation og klargøring',
         'Vedligehold, reparation og reservedele koordineret med mekanikere og eksterne værksteder i 24/7-drift; '
         'plan for hvad der skal ske først, og hvad der sker, hvis en del ikke er hjemme.'),
        ('Opkøb og vækst',
         'Bygget og drevet egen virksomhed med fuldt P&L: kundestrøm, kapacitet, omkostningsdrivere og indtjening '
         'gennemgået hver måned — den samme analyse, et opkøb skal kunne tåle.'),
        ('Kommerciel forståelse og ønske om at udvikle virksomheder',
         'Egen virksomhed drevet fra nul til en drift med fem håndværkere og tre lærlinge; projekter på tværs af '
         'teknik, økonomi og kunder, hvor resultatet kunne aflæses på bundlinjen.'),
        ('Struktureret og løsningsorienteret under pres',
         'Beslutninger taget på tavlemøder i 24/7-drift og på byggepladser med 11 parallelle opgaver; opgaver '
         'delegeret med mandat og fulgt op på dato.')])
    m.page_break()

    m.models_table('DE FØRSTE 90 DAGE — SÆSONEN, SYSTEMERNE OG PORTEFØLJEN', ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'Gennemgå sidste sæsons tal, kontrakter, kalender og kundeliste sammen med jer; mød mekanikeren, de faste '
         'deltidsmedarbejdere og de centrale leverandører; se bilerne, dokumentationen og de nuværende arbejdsgange '
         'i praksis — og kortlæg, hvad der i dag kun findes i hovedet på nogen.'),
        ('Dag 30',
         'En sæsonplan baglæns fra første køredag med milepæle for syn, klargøring, rekruttering, oplæring, salg og '
         'betaling; en liste over de fem største risici og hvad der skal være besluttet i februar for at undgå dem; '
         'kravsspecifikation og tidsplan for det nye CRM.'),
        ('Dag 60',
         'Rekrutterings- og oplæringsplan for chauffører klar med tjekliste pr. bil og ansvarlig pr. køredag; '
         'pris- og kapacitetsmodel gennemgået, så udnyttelsen kan følges ugentligt; CRM i drift med de første '
         'arbejdsgange automatiseret.'),
        ('Dag 90',
         'Sæsonen kører efter plan med daglig status på biler, chauffører og kunder og ugentlig status på omsætning '
         'og betalinger; en evaluering klar til juli; og de første udviklingsprojekter på Sorø Sø Camping taget ind '
         'med ejer, budget og tidsplan.')])

    m.section('TI DAGE KAN IKKE REDDES I JUNI')
    m.para('Alt, hvad der går galt i en studentersæson, er besluttet tidligere: bilen, der ikke blev synet i tide, '
           'chaufføren, der blev rekrutteret for sent, kontrakten, hvor der stod noget andet end det, kunden troede, '
           'og betalingen, der aldrig blev fulgt op. Derfor lægger jeg planen baglæns: først den 20. juni, så det, der '
           'skal være færdigt i maj, april, marts og februar — med en ejer på hver enkelt. Når sæsonen starter, '
           'skal der ikke træffes nye beslutninger, kun gennemføres og justeres.', after=80)

    m.section('TREDIVE CHAUFFØRER ER ET REKRUTTERINGSANSVAR, IKKE EN LISTE')
    m.para('Tredive mennesker, der skal køre i ti dage, og som ikke har gjort det før, er en opgave i rekruttering, '
           'oplæring og tydelighed. Det betyder tidlig udvælgelse, en fast oplæringsdag med tjekliste, en klar '
           'ansvarlig pr. køredag, en aftalt måde at melde fra på, og en plan for, hvem der kører i stedet — for '
           'sygdom kommer altid i den uge, hvor der ikke er plads. Og de mennesker skal behandles sådan, at de kommer '
           'igen næste år — erfaring er den billigste kapacitet, en sæsonvirksomhed har.', after=80)

    m.section('ØKONOMIEN SKAL KUNNE SES UGENTLIGT, IKKE TIL AUGUST')
    m.para('I en virksomhed med ti intense uger og halvtreds rolige er det farligt at vente på regnskabet. Jeg vil '
           'have omsætning, kapacitetsudnyttelse, omkostning pr. bil og betalingsstatus op på en tavle hver uge i '
           'sæsonen, og en simpel model for, hvad en ekstra køredag eller en ekstra bil betyder for indtjeningen. Det '
           'er også det grundlag, et opkøb skal vurderes på: hvad er kapaciteten, hvad koster den, og hvad skaber '
           'overskuddet.', after=80)

    m.section('SYSTEMER SKAL FJERNE ARBEJDE, IKKE TILFØJE ET')
    m.para('Et nyt CRM lykkes ikke, fordi det bliver købt, men fordi nogen har besluttet, hvilke tre ting det skal '
           'gøre bedre: følge op på tilbud, holde styr på kontrakter og betalinger, og give overblik over kapacitet. '
           'Jeg starter med de tre, bygger de arbejdsgange, der mangler, selv i Python og Claude, og måler på, hvor '
           'lang tid opgaverne tog før og efter. Resten af systemet kan komme bagefter — hvis det stadig er '
           'nødvendigt.', after=80)

    m.section('UDVIKLINGSPROJEKTER KRÆVER EN EJER, ET BUDGET OG EN DATO')
    m.para('Hytter, bookingsystem, kodelåse, endnu et opkøb: det er forskellige opgaver, men de fejler på samme '
           'måde, hvis ingen ejer dem. Så et projekt får en ejer, et budget med en ramme, en dato for hvornår det '
           'skal være besluttet, og et kort dokument, der kan læses af dem, der ikke var med i mødet. Jeg har kørt '
           'den slags projekter med myndighedsgodkendelser, leverandører og håndværkere før — og jeg ved, at det er '
           'koordineringen, ikke tegningen, der afgør, om det bliver færdigt.', after=80)

    m.section('JEG HAR PRØVET AT HAVE ANSVARET FOR ALT SELV')
    m.para('Forskellen på at være ansat og at eje er ikke arbejdstiden; det er, at der ikke er nogen, der betaler '
           'regningen, hvis man ikke selv gør. Det har gjort mig hurtig til at beslutte og prioritere, tydelig om mål og '
           'meget lidt imponeret af processer, der ikke flytter noget. Jeg søger ikke en stilling, hvor jeg skal '
           'sidde og vente på en beslutning, men et sted, hvor jeg kan tage den og stå ved resultatet — præcis som '
           'I beskriver.', after=80)

    m.section('ET OPKØB ER EN DRIFTSANALYSE, IKKE EN RABAT')
    m.para('Når man køber en lille virksomhed, køber man sjældent en maskine eller en kundeliste — man køber den måde, '
           'tingene bliver gjort på. Derfor er den første opgave efter et opkøb at dokumentere driften, som den '
           'faktisk foregår: hvad der skaber omsætningen, hvad der koster, og hvor der er en flaskehals, som ejeren '
           'kaldte tradition. Det er samme metode, jeg bruger i min egen virksomhed hver måned.', after=80)

    return m.save(path, title='Drifts- og projektleder — Festlastbiler.dk',
                  subject='Drift, sæson, ledelse og udviklingsprojekter i en portefølje af virksomheder',
                  keywords='driftsleder, projektleder, operationelt og kommercielt ansvar, sæson, rekruttering, '
                           'salg, kontrakter, betalingsopfølgning, økonomi, CRM, automatisering, opkøb, '
                           'tekniske koordinering')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Festlastbiler_DriftsOgProjektleder.docx')))
