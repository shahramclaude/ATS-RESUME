# -*- coding: utf-8 -*-
"""Multi-Tech A/S (via Career | a JKS Company) — Serviceleder, Sorø.

Dansk leverance (opslaget er dansk): ansøgning side 1, CV side 2-3,
krav-dokumentation og 90 dage + afsnit side 4.
Policy: master/README.md — ekstrem sikkerhed, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Serviceleder · El-service, personale og forretning'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('5. november 2026')
    m.meta('Multi-Tech A/S · Sorø · Serviceleder · via Career | a JKS Company')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Serviceleder hos Multi-Tech A/S i Sorø', bold=True, color='1A1A1A')
    m.para('Til Recruitment Specialist Kristine Askjær, Career | a JKS Company', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('En serviceafdeling bliver ikke vurderet på organisationsdiagrammet. Den bliver vurderet på to '
           'ting: om vognen kommer, når kunden ringer, og om fakturaen passer med det, der blev lavet på '
           'adressen. Alt andet — planlægning, bemanding, tilbud, ISO-papir og trivsel — er det, der gør de to '
           'ting mulige hver dag. Det er den slags ledelse, jeg søger hos Multi-Tech: en afdeling i Sorø, hvor '
           'medarbejderne har rammerne til at lykkes, kunderne møder den samme ordentlighed hver gang, og hvor '
           'økonomien hænger sammen med det arbejde, der faktisk bliver udført.', after=80)

    m.para('**Jeg vil lede afdelingen på fire faste ting.** Først **dagen, der er planlagt, før den begynder**: '
           'service- og spjældopgaver fordelt efter kompetence og geografi, akutopkald med en aftalt '
           'vagtfordeling, og et morgenmøde der er kort nok til at blive holdt hver dag, hvor alle ved, hvad de '
           'skal, og hvem der tager det, der kommer ind undervejs. Dernæst **mesteren på skulderen**: faglig '
           'sparring i marken, kvalitet set efter i virkeligheden og ikke i et skema, og oplæring af lærlinge, '
           'der giver dem arbejde, de kan stå ved om fem år. Så **tilbud og faktura, der hænger sammen**: en '
           'kalkulation der holder, et faktureringsgrundlag der bliver lavet samme dag, og en dækningsgrad pr. '
           'opgave man kan se, mens måneden stadig kan nås. Og endelig **kunden, der ikke behøver at ringe to '
           'gange**: tydelig aftale, opfølgning efter opgaven og nye opgaver identificeret i driften frem for i '
           'et tilfældigt tilbud.', after=80)

    m.para('Det er ikke teori for mig. Siden 2023 har jeg drevet **ELOHVAC**, en dansk el-virksomhed med **fem '
           'håndværkere og tre lærlinge** og **fuldt P&L**: tilbud skrevet, kalkuleret og afgivet, materialer og '
           'underleverandører indkøbt, opgaver planlagt ud fra hvem der var hvor, fakturaer sendt og '
           'dækningsgraden fulgt hver måned. Jeg har selv stået med telefonen, når en kunde ringede klokken '
           'otte om morgenen, og jeg ved, at det, der redder den dag, er en plan og en kollega, der tager over — '
           'ikke en undskyldning.', after=80)

    m.para('Personaleledelse har jeg fra flere sider. Som **projekt- og værkstedsleder i Ventek-Air** havde jeg '
           '**14 medarbejdere og 11 samtidige opgaver** og holdt tavlemøde hver morgen: hvad skal ud i dag, hvem '
           'laver hvad, og hvad er i vejen. I fem år var jeg **drifts- og vedligeholdelsesleder på Lynetten under '
           'Biofos** med driftsmedarbejdere i skift og akutopkald uden for normal arbejdstid — dér lærer man, at '
           'en vagtplan ikke er et regneark, men en aftale med mennesker, der har et liv ved siden af. Og som '
           'leder for **12 teknikere i ARJ Engineering** havde jeg ansvaret for både oppetid, oplæring og den '
           'daglige kvalitet.', after=80)

    m.para('Fagligt er jeg el-mand i bund og grund: **elautoriseret maskin- og elinstallatør med LV/MV/HV** og '
           'el-teknisk håndværk i bagagen, ud over B.Tech i Technology Management & Mechanical Engineering. Det '
           'betyder, at jeg kan læse opgaven, vurdere om et tilbud er realistisk, gå ud på pladsen og se, om '
           'arbejdet er udført ordentligt — og tage den faglige samtale med en svend eller en lærling uden at '
           'skulle ringe til nogen. Jeg har også arbejdet i et miljø, hvor dokumentation ikke var valgfrit: hos '
           '**Novo Nordisk** leverede jeg **37 kapitalprojekter** med acceptkriterier, timeregistrering og '
           'afvigelser i et styret system og **nul kritiske fund** ved audit — det er samme disciplin som ISO- og '
           'kvalitetsprocedurer, bare med et andet ord.', after=80)

    m.para('Hvorfor så ikke bare blive ved med at være selvstændig? Fordi det, jeg er god til, bliver bedre i en '
           'større sammenhæng: flere kunder, faglige kolleger at sparre med, overmontører og ledelse at spille '
           'sammen med, og en organisation der kan løfte de opgaver, en lille virksomhed må sige nej til. Jeg har '
           'prøvet at stå med hele ansvaret selv — og det er præcis derfor, jeg ved, hvad en afdeling kræver af '
           'sin leder, og hvor let en travl hverdag spiser den opfølgning, der skulle have været der.', after=80)

    m.para('Arbejdsmiljø og el-sikkerhed tager jeg alvorligt af en enkel grund: i el-faget går det galt på den '
           'måde, ingen havde planlagt. Derfor skal sikkerheden være på tavlemødet og på pladsen — arbejdstilladelser, '
           'LOTO, eftersyn af værktøj og en kultur, hvor man siger til, når noget er farligt, uden at nogen '
           'bliver gjort til problemet. En serviceleder, der kun taler om sikkerhed, når der er sket noget, har '
           'allerede tabt den samtale.', after=80)

    m.para('Kulturen i Multi-Tech lyder som noget, jeg kender godt: **flad struktur, korte beslutningsveje, '
           'kvalitet, troværdighed og ordentlighed** — og et ledelsessamarbejde, hvor man spiller hinanden gode. '
           'Jeg er en leder, der er tæt på medarbejderne, som lytter før jeg beslutter, og som tager beslutningen '
           'og står ved den bagefter. Følgeskab får man ikke ved at fortælle, at man er chefen; man får det ved '
           'at være den, der rydder vejen, når dagen er svær, og som giver kreditten videre, når det går godt.', after=80)

    m.para('Praktisk: jeg bor i Måløv og har omkring **en time til Sorø**, kørekort B og bil, så jeg kan være '
           'der, når afdelingen åbner, og køre ud til kunderne, når der er brug for det. Dansk er mit '
           'modersmål, og jeg arbejder i engelsk til daglig. Kan starte efter aftale. Jeg vil gerne høre, hvordan '
           'serviceopgaverne fordeler sig i dag mellem planlagt arbejde og spjæld — for det er der, planlægningen '
           'og økonomien skal begynde.', after=70)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Serviceleder med el-teknisk baggrund og 20+ års erfaring fra el-installation, service og 24/7-drift — '
           'elautoriseret maskinmester og elinstallatør (LV/MV/HV) med B.Tech i Technology Management & Mechanical '
           'Engineering. Driver egen el-virksomhed med fuldt P&L siden 2023: tilbud, kalkulation, bemanding, '
           'fakturering og fem håndværkere plus tre lærlinge. Har ledet 14 medarbejdere og 11 samtidige opgaver '
           'med daglig styring ved tavlen, og 12 teknikere med ansvar for oppetid og oplæring. Arbejder tæt på '
           'medarbejderne, struktureret med økonomien og ordentlig i kundeforholdet.', after=80)

    m.section('SERVICE, PERSONALE OG ØKONOMI')
    for label, body in [
        ('Personaleledelse og udvikling',
         'Daglig ledelse af håndværkere, teknikere og lærlinge: MUS og udviklingssamtaler, kompetencematrix, '
         'faglig sparring og oplæring, der følges op i marken og ikke kun i skemaet.'),
        ('Planlægning, koordinering og bemanding',
         'Service- og spjældopgaver fordelt efter kompetence, geografi og kapacitet; akutopkald med aftalt '
         'vagtfordeling; dagligt tavlemøde og ugentlig opfølgning på tid, kvalitet og udnyttelse.'),
        ('Tilbud, fakturering og økonomi',
         'Kalkulation og tilbudsgivning, faktureringsgrundlag lavet samme dag som opgaven, dækningsgrad fulgt pr. '
         'opgave og pr. måned; fuldt P&L i egen virksomhed siden 2023.'),
        ('Kunder og service',
         'Eksisterende kunder fastholdt gennem tydelig aftale og opfølgning efter opgaven; nye opgaver '
         'identificeret i driften og tilbudt, mens man er på adressen; professionel håndtering af det akutte.'),
        ('Kvalitet, dokumentation og ISO',
         'Arbejds- og kvalitetsprocedurer fulgt i praksis; timeregistrering og dokumentation ført løbende; '
         'afvigelser lukket med rodårsag, og audit gennemført uden kritiske fund i 37 projekter.')]:
        m.bullet(label, body, after=25)

    m.models_table('VÆRKTØJER OG METODER', ('Opgave', 'Værktøj og dokumenteret brug'), [
        ('El-teknisk',
         'El-installationer i bolig, erhverv og industri; LV/MV/HV under autorisation; fejlretning, tavler, drev '
         'og styringer, og vurdering af arbejdets kvalitet på pladsen.'),
        ('Drift og service',
         'Akutopkald og vagtplaner i 24/7-drift; serviceaftaler, reservedele og leverandører; prioritering mellem '
         'planlagt arbejde og spjæld.'),
        ('Plan og økonomi',
         'Tilbud og kalkulation, timeregistrering, fakturering og dækningsgrad i Excel og forretningssystem; SAP '
         'i daglig brug i større organisationer.'),
        ('Kvalitet og dokumentation',
         'Acceptkriterier, egenkontrol og afvigelser dokumenteret undervejs; as-built, driftsinstruks og '
         'overlevering; ISO- og kvalitetsprocedurer som daglig praksis.'),
        ('Arbejdsmiljø og sikkerhed',
         'APV, arbejdstilladelser, LOTO og el-sikkerhed på pladsen; sikkerhed som fast punkt på tavlemødet og '
         'som lederens opgave, ikke som et dokument.'),
        ('Ledelse',
         'MUS og udviklingssamtaler, 1:1 i fast rytme, oplæringsplan pr. lærling og svend, rekruttering og '
         'delegering med klare rammer og tydelig opfølgning.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 håndværkere og 3 lærlinge · fuldt P&L · el-installation og service for private og erhverv',
         [('Kunder, tilbud og økonomi', 'Tilbud og kalkulation udarbejdet og afgivet; fakturering og dækningsgrad '
                                        'fulgt pr. sag, og kunden informeret samme dag noget ændrer sig.'),
          ('Personale og lærlinge', 'Daglig ledelse af fem håndværkere og oplæring af tre lærlinge efter fast '
                                    'plan; arbejdsmiljø og kvalitet på pladsen uden undtagelser.')]),
        ('Senior commissioning engineer / projektleder, elsystemer',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Dokumentation og kvalitet', 'Acceptkriterier, timeregistrering og afvigelser i et styret system; '
                                        'auditeret aflevering med nul kritiske fund.'),
          ('Koordination', 'Grænseflader mod andre fag og leverandører styret til aftalt kvalitet og rækkefølge; '
                           'månedlig opfølgning på tid og økonomi til ledelse og kunde.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige opgaver · 2–10 mio. kr. pr. opgave',
         [('Daglig styring', 'Tavlemøde hver morgen med bemanding, flaskehalsanalyse og omprioritering på tværs af '
                             '11 samtidige opgaver; indkøb og leverancer fulgt til døren.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Lynetten under Biofos · København · aug. 2017–jan. 2022',
         'Procesanlæg i 24/7-drift · varme, ventilation, pumper, højspænding og SCADA',
         [('Service, vagt og akutopkald', 'Skiftplanlægning og akutopkald uden for normal arbejdstid; '
                                          'prioritering mellem planlagt vedligehold og nedbrud, og entreprenører '
                                          'koordineret på pladsen.'),
          ('Energi og forbrug', 'Energiledelse på målere og SCADA-data: over 40 % lavere energiforbrug, '
                                'dokumenteret og fastholdt.')]),
        ('Elektromekaniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · industrielt udstyr',
         [('Team, oppetid og oplæring', 'Vagtplanlægning, oplæring og opfølgning på mål; fejlretning, '
                                        'rodårsagsanalyse og korrigerende handlinger på produktionsudstyr.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('UDDANNELSE OG AUTORISATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering',
          'Maskinmesterskolen København · 2017–2022 · gennemsnit 7,6/12')
    m.edu('Autoriseret maskin- og elinstallatør (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('El- og maskinkonstruktion, elektroteknik',
          'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Køle- og ventilationsteknik · STCW sikkerhed', 'Mercantec 2021 · Søfartsstyrelsen 2021')

    m.section('SPROG, PRAKTIK OG REFERENCER')
    m.para('Dansk: modersmål · Engelsk: professionelt · Persisk: modersmål · Kørekort B og bil · Bor i Måløv, '
           'ca. en time fra Sorø · Kan starte efter aftale · Excel og forretningssystem dagligt, SAP og Python '
           'til data · Referencer på forespørgsel.', after=70)

    m.models_table('DET EFTERSPØRGER DE — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Solid el-teknisk baggrund, gerne uddannet elektriker',
         'Elautoriseret maskin- og elinstallatør (LV/MV/HV) med el-teknisk håndværk i bagagen og B.Tech i '
         'Technology Management & Mechanical Engineering; el-installation og service i egen virksomhed siden '
         '2023.'),
        ('Bred erfaring fra installations- og servicebranchen',
         'El-installation, service og vedligehold i egen virksomhed, i 24/7-drift på Lynetten og i 37 '
         'kapitalprojekter; akutopkald, vagtplaner og serviceopgaver i mere end tyve år.'),
        ('Erfaring med personaleledelse, gerne serviceleder eller overmontør',
         'Daglig personaleledelse af fem håndværkere og tre lærlinge siden 2023; 14 medarbejdere i Ventek-Air; 12 '
         'teknikere i ARJ; driftsmedarbejdere i skift på Lynetten.'),
        ('Medarbejderudvikling, trivsel og faglig sparring',
         'MUS og udviklingssamtaler, kompetencematrix og oplæringsplan pr. medarbejder; faglig sparring i marken '
         'og opfølgning på arbejdet, ikke kun på timerne.'),
        ('Oplæring af lærlinge',
         'Tre lærlinge i eget ansvar siden 2023 med fast oplæringsplan og svendeprøveperspektiv; oplæring af nye '
         'medarbejdere ved maskinen og på pladsen i både Ventek-Air og ARJ.'),
        ('Planlægge og koordinere serviceopgaver, bemanding og ressourcer',
         'Dagligt tavlemøde og bemandingsplan i 11 samtidige opgaver; service og akutopkald koordineret i '
         '24/7-drift; udnyttelse og geografi indregnet i planen hver dag.'),
        ('Tilbudsgivning, økonomisk opfølgning og faktureringsgrundlag',
         'Tilbud og kalkulation skrevet og afgivet i egen virksomhed; fakturering samme dag som opgaven og '
         'dækningsgrad fulgt pr. sag og pr. måned; fuldt P&L siden 2023.'),
        ('Kunderelationer og løsningsorienteret kundeservice',
         'Eksisterende kunder fastholdt gennem tydelig aftale og opfølgning; nye opgaver identificeret på '
         'adressen; akutte situationer håndteret med en plan og en kollega, der tager over; kunden informeret, før '
         'han selv skal spørge.'),
        ('Dokumentation, timeregistrering og ISO-procedurer',
         'Timeregistrering og dokumentation ført løbende; afvigelser lukket med rodårsag; auditeret aflevering '
         'med nul kritiske fund i 37 projekter under GMP; egenkontrol og as-built dokumenteret, mens arbejdet blev '
         'udført.'),
        ('Struktureret, tydelig kommunikation og samarbejde på tværs',
         'Fast skriftlig status til ledelse og kunde; beslutninger taget tæt på medarbejderne og forklaret '
         'bagefter; lederkolleger og andre fag inddraget, før beslutningen blev taget.')])
    m.page_break()

    m.models_table('DE FØRSTE 90 DAGE — DAGEN, FOLKENE OG TALLENE', ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'Med ud på opgaverne med sjakket: hvordan fordeles service og spjæld i dag, hvem tager akutopkaldene, og '
         'hvor går tiden tabt. Gennemgang af kunder, serviceaftaler, timeregistrering og de sidste måneders '
         'økonomi.'),
        ('Dag 30',
         'En fast morgenrytme med tavlemøde og bemandingsplan; akutopkald og vagtfordeling aftalt. Overblik over '
         'dækningsgrad pr. opgavetype, og de tre steder hvor tid og penge forsvinder, navngivet.'),
        ('Dag 60',
         'Tilbuds- og faktureringsgangen ryddet op, så grundlaget bliver lavet samme dag; oplæringsplan pr. '
         'lærling og ny medarbejder lagt; kvalitets- og sikkerhedsgennemgang på pladserne med handlinger, der har '
         'en ejer.'),
        ('Dag 90',
         'Afdelingen kører med en plan, alle kender; kunderne får ét telefonnummer og én aftale; dækningsgraden er '
         'kendt og forbedret på mindst ét område — og medarbejderne kan mærke, at der er en leder, der følger op.')])

    m.section('SERVICE ER EN KÆDE AF SMÅ LØFTER')
    m.para('En serviceopgave består af ti små skridt, og kunden dømmer os på det svageste af dem: telefon, '
           'aftale, kørsel, adgang, fejlfinding, reservedel, udførelse, oprydning, dokumentation og faktura. Der '
           'skal ikke meget svigt til, før helheden føles dårlig — og der skal ikke meget styring til, før den '
           'føles god. Derfor er mit arbejde at gøre de ti skridt ens hver gang og fjerne det, der typisk går '
           'galt: reservedele der ikke er på bilen, en adgang der ikke er aftalt, og en seddel der bliver væk.', after=80)

    m.section('FOLKENE LEVERER, IKKE PLANEN')
    m.para('Man kan planlægge sig til meget, men ikke til engagement og motivation. En serviceleder, der sidder på '
           'kontoret og '
           'spørger til timeforbruget, får timeforbrug. En leder, der er med ude, ser hvordan opgaven bliver '
           'løst, roser det der er godt, og retter det der ikke er — får en medarbejder, der tager ansvar, når '
           'han er alene på adressen. Det er også den billigste kvalitetssikring, der findes: en svend, der ved, '
           'hvad ordentligt arbejde er, fordi nogen har vist ham det.', after=80)

    m.section('TILBUDDET ER ET LØFTE, FAKTURAEN ER BEVISET')
    m.para('Et tilbud er ikke et stykke papir, det er en aftale om, hvad kunden kan forvente. Derfor skal '
           'kalkulationen bygges på de timer, opgaven faktisk tager, og materialerne faktisk koster — med plads '
           'til det uforudsete, som et ældre anlæg altid byder på. Når arbejdet er udført, skal '
           'faktureringsgrundlaget laves samme dag, mens man husker hvad der blev gjort, og dækningsgraden skal '
           'kunne ses, mens måneden stadig kan nås. Det er den slags orden, der gør en afdeling sund, også i en '
           'travl uge: at man ved, hvad man har solgt, hvad det har kostet at levere, og hvad der er tilbage.', after=80)

    m.section('KUNDEN SKAL MØDE DEN SAMME ORDENTLIGHED HVER GANG')
    m.para('Troværdighed bliver ikke bygget på et slogan, men på gentagelse. Kunden skal møde den samme aftale, '
           'den samme påklædning, det samme ryddelige arbejde og den samme ærlige besked, når noget ikke kan '
           'lade sig gøre i dag. Det er også sådan nye opgaver bliver til: ikke ved at sælge, men ved at være den, '
           'kunden ringer til, fordi sidste gang gik, som den skulle. Og når vi finder noget på adressen, der '
           'trænger, siger vi det samme dag — med et tilbud, ikke med en bemærkning.', after=80)

    m.section('LÆRLINGER ER FREMTIDEN, MEN DE ER OGSÅ EN OPGAVE I DAG')
    m.para('En lærling, der bliver sat til at feje og hente materialer i to år, bliver ikke svend — han bliver en, '
           'der forlader faget. Derfor skal der være en plan pr. lærling: hvad skal han kunne om seks måneder, '
           'hvem lærer ham det, og hvornår står han selv med opgaven, mens en svend ser på. Det kræver, at '
           'svendene har tid til at lære fra sig, og at det bliver anerkendt som en del af deres arbejde. En '
           'afdeling, der uddanner godt, har også nemmere ved at holde på folk — og en lærling, der bliver set, bliver '
           'ofte den svend, der løfter weekendvagten om fem år, fordi han husker, hvem der lærte ham faget.', after=80)

    m.section('FLAD STRUKTUR KRÆVER TYDELIGE AFTALER')
    m.para('Korte beslutningsveje er et gode, men de virker kun, hvis alle ved, hvem der beslutter hvad. Derfor '
           'aftaler jeg tidligt med overmontørerne og ledelsen, hvor min beslutningsret går, hvornår jeg spørger, '
           'og hvordan vi deler kunder og kapacitet mellem os. Resten af tiden bruger jeg på at spille mine '
           'lederkolleger gode — for en serviceafdeling, der vinder en opgave, skal ikke tabe den i næste afdeling. '
           'Det kræver, at kunden har ét navn at ringe til, også når opgaven går på tværs af fag.', after=80)

    m.section('ØKONOMI ER IKKE ET TAL PÅ ET ARK')
    m.para('Når en afdeling mister penge, er det sjældent, fordi timeprisen er for lav. Det er som regel kørsel, '
           'der ikke er faktureret, materialer der ikke er registreret, opgaver der tog tre gange så lang tid som '
           'antaget, eller akutopkald der blev løst uden at blive skrevet ned. Jeg finder de steder ved at se på '
           'timerne og opgaverne sammen med dem, der udfører dem, og ved at gøre opfølgningen til en fast rytme '
           'frem for en månedlig overraskelse. Det er også den mest retfærdige måde at tale om tal på: alle kan '
           'se, hvad der bliver målt, og hvorfor.', after=80)

    return m.save(path, title='Ansøgning — Serviceleder, Multi-Tech A/S Sorø',
                  subject='El-service, personaleledelse, tilbud og økonomi',
                  keywords='serviceleder, el-installation, service, personaleledelse, lærlinge, planlægning, '
                           'tilbudsgivning, fakturering, dækningsgrad, kunderelationer, ISO, dokumentation')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_MultiTech_Serviceleder.docx')))
