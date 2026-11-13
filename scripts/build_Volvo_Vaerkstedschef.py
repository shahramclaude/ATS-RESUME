# -*- coding: utf-8 -*-
"""Volvo Truck Center Danmark — Værkstedschef, Taastrup & Karlslunde (req. 37243).

Form (master/FORMKATALOG.md): åbning **N** (historien: »80 år« fra deres eget
opslag vendes til det operative spørgsmål — en lastbil på liften er den eneste,
der ikke kører), struktur **Det samme og det forskellige** (fem ting der skal
være ens på to værksteder, tre der skal være forskellige), register
**Værkstedshallen** (løftebord, fejlkode, reservedel, servicetime, oppetid,
kapacitet, tavle). Kulturfil: jd/Volvo_Vaerkstedschef_kultur.txt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Værkstedschef · to værksteder, ledere, økonomi og drift'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('13. november 2026')
    m.meta('Volvo Truck Center Danmark · Taastrup og Karlslunde · req. 37243')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: værkstedschef, Taastrup & Karlslunde', bold=True, color='1A1A1A')

    def lp(text, after=60):
        return m.para(text, after=after, line=236)

    # ---------------------------------------------------------------- side 1
    lp('**80 år.** Så længe har Volvo ifølge jeres eget opslag stået i spidsen for udvikling af '
       'transportløsninger — og den eneste lastbil, der ikke udvikler noget, er den, der står på '
       'liften. Et værksted er derfor ikke en støttefunktion til forretningen. Det er der, kundens '
       'lastbil bliver til kundens indtjening igen, og det er den logik, to værksteder i Taastrup og '
       'Karlslunde skal styres efter: kapacitet, reservedele og ledere, der kan træffe en beslutning '
       'klokken 7.', after=56)

    lp('**I skriver, at opgaven er at få de to værksteder til at »lykkes både hver for sig og '
       'sammen«** — og at jeg skal **»skabe resultater gennem ledere«**. Det er præcis den slags '
       'lederjob, hvor man ikke bliver målt på, hvor god man selv er til at skrue, men på om de lokale '
       'værksteds- og reservedelsledere kan holde deres tal uden at ringe. Jeg har ledet værksted, '
       'service og projektorganisation siden 2003, og jeg har prøvet begge fejl: at være for langt '
       'væk, og at være for tæt på.', after=56)

    lp('**Det, der skal være ens på begge matrikler.**', after=44)

    lp('**Retningen.** To værksteder kan ikke have hver sin fortolkning af, hvad der er en god uge. '
       'Én fælles plan med tre tal — oppetid på kundens lastbil, **servicetime** pr. ordre og '
       'indtjening pr. lift-time — og en månedlig gennemgang, hvor begge ledere læser den samme side. '
       'Det er også den side, jeg selv tager med i den danske **ledergruppe**.', after=40)

    lp('**Tallene.** **Budgetter** og **nøgletal** er ikke rapportering; de er redskaber til at flytte '
       'kapacitet, før kunden mærker det. Jeg har ført fuldt **P&L** i egen virksomhed siden 2023 og '
       'arbejdet med dækningsgrad og timeforbrug hver måned — og lært, at et budget, der ikke bliver '
       'brugt til at beslutte noget, er en PDF.', after=40)

    lp('**Lederne.** En lokal værkstedsleder skal have rammer, ikke instrukser: hvad de selv beslutter '
       'om bemanding, pris og kundekredit — og hvad der kommer til mig. Jeg har oplært 12 teknikere, '
       '14 montører og 8 egne medarbejdere og ved, at udvikling af ledere sker i deres egne sager, '
       'ikke i et kursuslokale.', after=40)

    lp('**Kunden.** **Kundetilfredshed** måles bedst på det, kunden siger i telefonen, når lastbilen '
       'står stille — og på om vi ringede tilbage, før han gjorde. Jeg har drevet service med '
       'responstid og **serviceaftaler** og ved, at den samtale er hele forretningen.', after=40)

    lp('**Væksten.** **»Opsøgende servicemarkedssalg«** bliver ikke en kampagne; det bliver en vane, '
       'hvor den enkelte montør ved, hvad der kan sælges videre på den lastbil, han står med, og hvor '
       'lederen følger op på det sammen med salgsorganisationen. Jeg har bygget en serviceforretning fra '
       'nul i egen virksomhed og ved, at vækst i service kommer fra de kunder, der allerede kender os.',
       after=40)

    lp('**Sikkerheden.** Standarder, processer og **sikkerheds- og miljøkrav** bliver ikke overholdt, '
       'fordi de står i en mappe; de bliver overholdt, fordi lederen på stedet går gennem hallen og '
       'siger det højt. Jeg har ført **APV**, **LOTO** og arbejdsmiljø i egen virksomhed — det er '
       'håndværk, ikke politik.', after=56)

    lp('**Det, der ikke skal være ens.** Karlslunde og Taastrup har forskellige kunder, forskellig '
       'kapacitet og sandsynligvis forskellige ledelsesstile, der virker. Jeg vil ikke gøre dem '
       'identiske; jeg vil gøre dem sammenlignelige — samme tal, samme standarder, hver sin plan for, '
       'hvordan de når dem. Det er også, hvad I skriver: **»blik for helheden uden at miste '
       'forståelsen for lokale forskelle og behov«**.', after=56)

    lp('**Det, jeg ikke har, står her.** Jeg har ikke arbejdet i en lastbilforretning og ikke ledet '
       'ledere med budgetansvar i en koncern som Volvo. Til gengæld har jeg stået i spidsen for et '
       'værksted med 12 teknikere, en serviceforretning med 8 ansatte og fuldt **P&L**, 14 montører på '
       '11 samtidige anlæg og 25 specialister i en koncern — og jeg er **elautoriseret maskinmester '
       '(LV/MV/HV)**, så den tekniske samtale i hallen koster mig ikke tid.', after=56)

    lp('**Hvorfor Volvo — i jeres egne ord.** I lover **»reel indflydelse«** i et miljø med **»høj '
       'faglighed, stærkt samarbejde og stor stolthed«** omkring kunder og produkter, en **»veldrevet '
       'og profitabel forretning med høje markedsandele«** og **»tilfredse kunder og medarbejdere«** — '
       'med **»Kvalitet, Sikkerhed og Miljø«** som værdier og en ambition om at forme **»bæredygtige '
       'transportløsninger til fremtiden«**. Det er fire ting, der ikke kan købes for penge, men kun '
       'bygges af ledere, og det er den slags arbejde, jeg søger.', after=56)

    lp('**Praktisk:** jeg bor i Måløv og har cirka en halv time til Taastrup, så jeg kan være i begge '
       'haller på samme dag og deltage i morgenmøderne uden at bo i bilen. **Engelsk** på '
       'forretningsniveau og **kørekort B**. Kan starte efter aftale; referencer indhentes gerne.', after=24)

    m.meta('Med venlig hilsen', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('**Driftsleder med værksted, service og økonomi under ét** — **elautoriseret maskinmester '
           '(LV/MV/HV)**, B.Tech i teknologiledelse og maskinteknik. Ledet værksted med 12 teknikere, '
           'serviceforretning med 8 ansatte og fuldt **P&L** siden 2023, 14 montører på 11 samtidige '
           'anlæg og 25 specialister i en koncern. Arbejder med **budget**, **nøgletal**, '
           '**resultatopfølgning** og **forbedringsarbejde** — og med at få ledere til at lykkes i '
           'deres egen hverdag.', after=70)

    m.section('VÆRKSTEDSHALLEN — SÅDAN LÆSER JEG EN DRIFT')
    for label, body in [
        ('Løftebordet',
         'Hvor mange lifter der er optaget, og hvor længe; en optaget lift uden en ordre på er den '
         'dyreste kvadratmeter i hallen, og den kan ses på tavlen klokken 7.'),
        ('Fejlkoden',
         'Hvilken **fejlkode** der fylder mest, og om årsagen er teknik, kunde eller reservedel — det '
         'afgør, om svaret er en instruks, et opkald eller et lager.'),
        ('Ugen i tal',
         'Seks tal på én side: fakturerede timer, oppetid på kundens lastbil, ordrer pr. lift, '
         'dækningsgrad, reklamationer og sygefravær — samme side på begge værksteder.'),
        ('Reservedelen',
         'Hvad der ligger på hylden, hvad der har tre dages levering, og hvad der stopper en lift midt '
         'i ugen; **indkøb** og **logistik** er en del af kapaciteten, ikke en side af den.'),
        ('Servicetimen',
         'Én time i hallen skal give mere end den koster; timeforbrug, **dækningsgrad** og '
         'fakturerede timer pr. montør er de tre tal, jeg ville se hver uge.'),
        ('Oppetiden',
         'Kundens lastbil skal ud igen — målt fra kunden ringer, ikke fra vi åbner ordren. Det tal er '
         'den ærlige version af **kundetilfredshed**.'),
        ('Tavlen',
         'Én tavle pr. værksted med de samme felter, så de to steder kan sammenlignes; det er også '
         'derfra, en god løsning bliver delt, fordi den er synlig.')]:
        m.bullet(label, body, after=16)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · entreprise og service',
         [('Service, økonomi og ledelse',
           '**Budget**, **P&L** og **resultatopfølgning** hver måned; **serviceaftaler**, udbud og '
           'indkøb; ansættelse, oplæring og **personaleledelse** af otte medarbejdere.')]),
        ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen',
         'Data Power Consultant ApS · København · 2024–nov. 2026 (sideløbende med ELOHVAC)',
         '4–10 personer · tekniske og industrielle applikationer',
         [('Tal i driften',
           '**KPI**-modeller for kapacitet, timeforbrug og indtjening; selskabet er ophørt.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('Ledere og specialister uden at være i linjen',
           '25 specialister koordineret på tværs af 37 projekter; standarder og dokumentation fulgt '
           'til dørs — nul kritiske afvigelser ved aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter',
         [('Værksted, kapacitet og kunder',
           'Daglig **kapacitetsmodel** for 11 anlæg og 14 montører; omprioritering samme dag, når en '
           'kunde eller en leverance flyttede sig.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Biofos (Lynetten) · København · aug. 2017–jan. 2022',
         'Renseanlæg i 24/7-drift · pumper, højspændingstavler, SCADA',
         [('Oppetid, sikkerhed og miljø',
           'Planlagt vedligehold og akut fejlfinding døgnet rundt; **over 40 % lavere energiforbrug** '
           'gennem måling og indregulering.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 teknikere · maskinværksted · maskiner og materiel',
         [('Værksted og oplæring',
           'Fejlfinding, kalibrering og reparation af maskiner; indkøb og vedligehold af materiel; '
           '**oplæring** og opfølgning for 12 teknikere.')]),
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
    m.para('Dansk og **engelsk** på forretningsniveau · Persisk: modersmål · **IT**: **MS Office** med '
           '**Excel**-modeller til budget, kapacitet og **KPI**, **ERP** med sags- og økonomidel, '
           '**CRM** og tavlesystemer, egne **Python**-værktøjer til timeforbrug og indtjening · '
           '**Kørekort B** og egen bil · Måløv, cirka en halv time til **Taastrup** · Kan starte efter '
           'aftale · Referencer på forespørgsel.', after=50)

    m.models_table('OPSLAGETS KRAV — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Samlet ansvar for værksteds- og reservedelsforretningen på to værksteder',
         'Fuldt **P&L** og otte ansatte i egen virksomhed siden 2023, værksted med 12 teknikere og '
         'serviceforretning med aftaler, indkøb og lager — ansvaret for både ordren, delen og '
         'indtjeningen.'),
        ('Sætte fælles retning og sikre koordinering og samarbejde på tværs',
         'Én tavle og én månedlig status pr. enhed i 11 samtidige anlægsprojekter og 37 '
         'kapitalprojekter; samme felter på alle, så de kunne sammenlignes og løsninger kunne deles.'),
        ('Ansvar for budgetter og samlede resultater',
         'Budget og **P&L** i egen virksomhed med otte ansatte og månedlig opfølgning på dækningsgrad, '
         'timeforbrug og indtjening — og konsekvenserne, når et tal gik den forkerte vej.'),
        ('Følge op med de lokale ledere på nøgletal, kapacitet og forbedringsbehov',
         'Ugentlig opfølgning med fagansvarlige og formænd i 20+ år: kapacitet, fremdrift og de to '
         'forbedringer, der betyder mest — ikke en ti-punkts liste, der ikke bliver lukket.'),
        ('Lede, sparre med og udvikle de lokale værksteds- og reservedelsledere',
         '**Sparring** som arbejdsform: 12 teknikere, 14 montører, 25 specialister og 8 egne '
         'medarbejdere udviklet gennem deres egne sager, med faste en-til-en-samtaler.'),
        ('Sikre at lederne lykkes med personaleledelse og udvikling af deres teams',
         'Onboarding og oplæringsvej skrevet ned, før stillingen blev slået op; 3 lærlinge og 5 '
         'elektrikere fastholdt i egen virksomhed gennem tydelige rammer og tæt opfølgning.'),
        ('Drive vækst og fokus på opsøgende servicemarkedssalg',
         '**Servicemarked** og serviceforretning bygget op fra nul i egen virksomhed 2023: '
         '**opsøgende salg** på eksisterende kunder, aftaler med responstid og en pris, der kunne '
         'forsvares i hallen.'),
        ('Følge op på kvalitet og kundetilfredshed',
         '**Kvalitet** målt på reklamationer og genarbejde, og **kundetilfredshed** målt på '
         'tilbagelevering og genkøb — to tal, samme månedsside som økonomien.'),
        ('Sikre at standarder, processer og sikkerheds- og miljøkrav bliver handling',
         '**APV**, **LOTO** og arbejdsmiljø ført i egen virksomhed; standarder gjort til en '
         'dagsorden på tavlemødet, ikke til en mappe i skabet.'),
        ('Drive fælles forbedringsinitiativer',
         '**Forbedringsarbejde** med tal: fra kapacitetsmodel til udskiftning af de komponenter, der '
         'gav over 40 % lavere energiforbrug — forbedring valgt på måling, ikke på mavefornemmelse.'),
        ('Støtte de lokale ledere i at omsætte strategier til handlingsplaner',
         'Strategi oversat til en **handlingsplan** med tre punkter, en ejer og en dato; prøvet på 37 '
         'projekter og i egen virksomheds vækst, hvor planen skulle kunne læses af andre.'),
        ('Bidrage med resultater, aktiviteter og status til den danske ledergruppe',
         'Rapporteret til direktion og bestyrelse i egen virksomhed: status på én side med tal, '
         'afvigelser og det, der kræver en beslutning — ikke en fortælling om, hvor travlt der er.'),
        ('Ledelseserfaring fra en driftsorienteret organisation — automotive, transport, værksted, service',
         'Driftsorienteret ledelse siden 2003: værksted med 12 teknikere, 24/7-drift i fem år, 14 '
         'montører på 11 anlæg og serviceforretning med fuldt **P&L** — ikke lastbiler, men samme '
         'logik: en kunde, der ikke kan vente.'),
        ('Stærk forretningsforståelse',
         'Egen virksomhed med pris, indkøb, løn og indtjening; tilbud med fast pris under **AB 18** og '
         'efterkalkulation på hver sag — forretningen lært fra kasseapparatet og ikke fra et '
         'lederudviklingsforløb.'),
        ('Erfaring med budgetter, nøgletal og resultatopfølgning',
         '**Budget** og **nøgletal** i drift siden 2023, **KPI**-modeller også i CTO-rollen, og '
         'månedlig **resultatopfølgning** med de lokale ledere — samme rytme, hver måned.'),
        ('Analysere en forretning, identificere forbedringer og omsætte dem til handling',
         'Analyse med en beslutning som mål: tal, tre muligheder, én anbefaling og en dato. 37 '
         'CAPEX-sager og egne investeringer er dokumenteret på den måde.'),
        ('Erfaring med at lede og udvikle ledere',
         'Formænd og fagansvarlige udviklet gennem deres egne sager; 25 specialister i en koncern og 14 '
         'montører i en entreprise — ledelse gennem andre, hvor jeg ikke selv kunne være i alle sager.'),
        ('Skabe tydelige rammer for ansvar, samarbejde og opfølgning',
         'Beslutningsret skrevet ned: hvad den lokale leder afgør alene, hvad der aftales, og hvad der '
         'kommer til mig — med navn og dato, og med **medarbejderudvikling** som fast punkt.'),
        ('Arbejde struktureret og følge vedholdende op',
         'Opfølgning som fast rytme: ugentlig tavle, månedlig status, kvartalsvis gennemgang — og en '
         'liste, der bliver lukket, før der åbnes en ny.'),
        ('Være empatisk, motiverende og tæt på mennesker og drift',
         'Til stede i hallen og på anlægget, ikke kun i mødelokalet; medarbejdere fastholdt gennem '
         'svære perioder, fordi rammerne var tydelige og samtalen tog den sværeste ting først.'),
        ('Engelsk på forretningsniveau',
         '**Engelsk** som arbejdssprog med leverandører, kunder og kolleger i koncernregi; '
         'dokumentation, tilbud og møder på engelsk i 20+ år.'),
        ('Kørekort kategori B',
         '**Kørekort B** og egen bil; bor i Måløv med cirka en halv time til Taastrup og kortere til '
         'Karlslunde — hverdagen kan deles mellem to matrikler uden at gå tabt i transport.'),
        ('Være handlekraftig og skabe følgeskab gennem dialog og involvering',
         'Beslutning samme dag, når den ikke kan vente; ellers beslutningen taget sammen med dem, der '
         'skal leve med den — 11 anlæg og 37 projekter blev ikke styret med ordrer alene.'),
        ('Blik for helheden uden at miste forståelsen for lokale forskelle og behov',
         'Fælles standarder og fælles tal, men lokal plan: to værksteder har forskellige kunder og '
         'forskellig kapacitet, og det skal planen afspejle — ligesom 11 anlæg på Ventek-Air fik hver '
         'deres plan i samme system.'),
    ])

    m.section('DERES EGNE ORD OM LEDELSE')
    m.para('I søger en, der er **»tydelig og empatisk«**, som **»skaber tillid, sætter klare '
           'forventninger«** og som **»giver de lokale ledere plads til at tage ansvar«** — og opgaven '
           'er **»forretningsudvikling med indsigt i den daglige drift«** med **»fokus på medarbejdere, '
           'kunder, kvalitet og indtjening«**, fordi **»kunder, medarbejdere, kvalitet og økonomi skal '
           'gå hånd i hånd«**. Det er ikke fem krav, det er én ledelsesstil, og den kræver, at man kan '
           '**»omsætte strategier til konkrete handlingsplaner«** og **»omsætte vores standarder, '
           'processer samt sikkerheds- og miljøkrav til handling i hverdagen«** — og at man kan '
           '**»sikre, at gode løsninger bliver delt på tværs«**, så det ene værksted ikke opfinder det, '
           'det andet har prøvet. **»Transport er kernen i det moderne samfund«**, skriver I, og '
           '**»næste generations teknologier og de skarpeste kollegaer«** bliver kun til noget, hvis '
           'nogen sørger for, at hverdagen i hallen hænger sammen.', after=50)

    m.section('DE FØRSTE 90 DAGE')
    for b in (
        'Uge 1–2: en dag i hver hal, med hver leder, og med den tavle de bruger i dag — uden at ændre '
        'noget; derefter en liste over de tre ting, kunderne klager over, og de tre ting, der koster '
        'mest.',
        'Uge 3–6: fælles tal og én månedsside for begge værksteder; gennemgang af kapacitet pr. lift og '
        'reservedelslagerets tre vigtigste huller.',
        'Måned 2–3: en-til-en med hver lokal leder om ansvar, mål og udvikling; handlingsplan med '
        'ejer og dato for de forbedringer, der giver mest pr. krone.',
        'Måned 3: første fælles gennemgang med begge værksteder og en status til ledergruppen, der '
        'kan læses på én side.'):
        m.bullet('', b, after=16)

    m.section('DET VILLE JEG SPØRGE OM')
    for b in (
        'Hvilke to tal bliver jeg målt på om et år — og hvem har dem i dag?',
        'Har de to værksteder forskellige kunder, eller konkurrerer de om de samme?',
        'Hvor mange lifter står tomme i snit, og hvad er den største flaskehals: folk, dele eller '
        'planlægning?'):
        m.bullet('', b, after=16)

    m.para('**Jeg kommer gerne forbi begge haller**, før vi taler om rollen — en værkstedschef, der ikke '
           'har set hallen, taler om noget andet end den. Kontakt: +45 93 99 95 14 · '
           'ajlooshahram@gmail.com.', after=24)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Volvo_Vaerkstedschef.docx')
    build(out)
    print(out)
