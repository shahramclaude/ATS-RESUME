# -*- coding: utf-8 -*-
"""make:net a/s (Gentofte) — Serviceleder, rekruttering via Moment Professionals.

Form (master/FORMKATALOG.md): åbning **H** (dagsforløbet: fire klokkeslæt som bevis),
struktur **Fejltilstandene** (fem navngivne fejl i en serviceforretning, hver med det,
der fanger den), register **Servicebilen** (nyt: vogn, kasse, materiale, rute, udkald,
seddel, timer). Kulturfil: jd/Makenet_Serviceleder_kultur.txt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Serviceleder · serviceelektrikere, kunder og planlægning'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('13. november 2026')
    m.meta('make:net a/s · Gentofte · via Moment Professionals, job nr. 204772')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Serviceleder', bold=True, color='1A1A1A')

    # ---------------------------------------------------------------- side 1
    m.para('**Klokken 7 skal montørerne ud af døren.** Klokken 9.30 ringer en kunde, fordi en opgave '
           'driller, og der skal være en, der tager den. Klokken 13 står man i en fredet bygning og ser '
           'på en tavle, der ikke er fra i går. Klokken 16.15 skal dagens sedler, timer og morgendagens '
           'ruter hænge sammen — ellers møder montøren i morgen op til et hul, han ikke kan se. De fire '
           'tidspunkter kender jeg fra egen virksomhed.', after=60)

    m.para('**make:net er et autoriseret el-installatørfirma i Gentofte, stiftet i 2000**, med '
           'el-installationer, alarm og sikring, overvågning, netværk og **el-entreprise** — og i '
           '**fredede og bevaringsværdige bygninger har make:net en stærk position**, som I selv '
           'skriver. Kunderne er **boligforeninger** og **erhvervskunder** i hovedstadsområdet og '
           '**Nordsjælland**. **Serviceteamet arbejder side om side med entrepriseafdelingen**, og I skriver '
           'selv, at **»Du refererer til direktøren i en flad organisation«** med **»råderum til at gøre '
           'tingene smartere«**. Det er en struktur, hvor service ikke er et vedhæng til entreprisen, '
           'men den daglige kontakt med kunden.', after=60)

    m.para('**Fem fejltilstande i en serviceforretning — og det, der fanger dem.**', after=50)

    m.para('**Montøren kører uden materiale.** Det er den dyreste time i en serviceforretning, og den '
           'opstår altid klokken 7.10. Derfor er fordelingen om morgenen ikke en liste, men et tjek: '
           'ordre, materiale og adgang på plads, før nøglen drejes — og en **fælles planlægning**, hvor '
           'materialet står på den samme sag, som montøren åbner på telefonen.', after=44)

    m.para('**Kunden ringer, og der er ingen hjemme.** En servicekunde måler ikke på kvalitet; han '
           'måler på, hvor hurtigt nogen svarer, og om han får det samme navn to gange. Min regel er '
           'enkel: den, der tager telefonen, ejer opgaven, indtil den er lukket — og en **responstid**, '
           'der står i systemet, ikke i hovedet på den enkelte. Jeg har siddet med serviceaftaler, hvor '
           'responstid var **KPI** og ikke en intention.', after=44)

    m.para('**Opgaven vokser, uden at nogen opdager det.** En **tavleudskiftning** bliver til en '
           '**renovering** over flere uger, og pludselig er der en grænseflade til '
           '**entrepriseafdelingen**, som ingen har aftalt. Den grænse skal skrives ned, før arbejdet '
           'udføres: hvem ejer sagen, hvem har kunden, og hvad er ændringen værd.', after=44)

    m.para('**Dokumentationen kommer uger efter opgaven.** Så kan kunden ikke få sin dokumentation, '
           'fakturaen bliver en diskussion, og næste elektriker starter forfra. **Dokumentation** og '
           'timer skal ind samme dag, mens montøren husker, hvad han så — det var kravet i en GMP-fabrik, '
           'og det er den samme vane, der gør en serviceforretning til at handle med.', after=44)

    m.para('**Montøren holder op med at sige noget.** Det er den fejl, ingen opdager i tide: manden '
           'kører stadig ud, men han siger ikke, at materialet er væk, at kunden er urimelig, eller at '
           'han er ved at brænde sammen. Derfor foregår ledelse ude ved **montørerne**, ikke i et '
           'mødelokale — daglig kontakt, **sparring** på opgaven og en samtale, der ikke handler om '
           'timer, mindst én gang i kvartalet. Den ene, der er stille, er den, man skal tale med først.',
           after=60)

    m.para('**Jeg er ikke el-installatør — og I skriver selv, at det ikke er nødvendigt.** Jeg er '
           'elektriker i bund og **elautoriseret maskinmester (LV/MV/HV)**, så autorisationen er ikke '
           'kun dækket i huset, den er på plads hos mig. Det, jeg har, er 20+ år i el-faget: 5 '
           'elektrikere og 3 lærlinge i egen virksomhed siden 2023 med service, tilbud og kunder, 37 '
           'kapitalprojekter i drift og fem år i 24/7-drift. Boligforeninger er en ny kundetype for '
           'mig — service i beboede bygninger er det ikke.', after=60)

    m.para('**Jeres eget sprog er grunden til, at jeg søger.** **»Er du elektrikeren, kunderne kan '
           'regne med, og montørerne gerne følger?«** er hele stillingen i én sætning. I vil have en, '
           'der **»leder serviceelektrikerne tæt på opgaverne«**, **»Du bliver den, der samler '
           'make:nets serviceopgaver ét sted«**, med **»en udpræget servicesans«** og evnen til at '
           '**»se mennesket bag montøren og samtidig sætte en tydelig ramme«** — og en, hvor **»Du '
           'leder tæt på montører og kunder«** og **»tager gerne værktøjet med ud, når der er brug for '
           'en ekstra hånd«**. I sætter en ære i at **»holde de aftaler, du laver med kunderne, også når '
           'dagen skrider«**, **»svare hurtigt og ringe til kunden, når en opgave driller«**, **»bruge '
           'den fælles planlægning, så alle kan se, hvad der sker«** og **»give en montør en hånd, både '
           'med værktøjet og med det, der fylder«** — de fire ting, jeg selv har holdt fast i, når ugen '
           'blev for kort. Og at **»montørerne har mulighed for selv at disponere over en del af deres '
           'opgaver«** betyder, at ansvar bliver givet, ikke bare beskrevet.', after=60)

    m.para('**Praktisk:** jeg bor i Måløv, 20 minutter fra Gentofte, har kørekort B og bil og kan være '
           'ude hos kunder og montører hver dag. Dansk og engelsk og kan starte efter aftale. Det, jeg '
           'gerne vil høre om, er, hvor mange serviceelektrikere der er i teamet i dag, og hvordan '
           'opgaverne fordeles mellem service og entreprise — så jeg ved, hvor grænsefladen skal ligge '
           'fra første uge.', after=50)

    m.meta('Med venlig hilsen', after=15)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('**El-teknisk leder og elektriker i bund** — **elautoriseret maskinmester (LV/MV/HV)**, '
           'B.Tech i teknologiledelse og maskinteknik. Har drevet egen el-virksomhed siden 2023 med '
           '**service**, tilbud og kunder som dagligdag, ledet **14 medarbejdere** i 11 samtidige '
           'projekter og **5 elektrikere og 3 lærlinge** i egen virksomhed. Ansvarsområder: '
           '**planlægning**, **materialer**, **kundekontakt**, **dokumentation** og **opfølgning** — '
           'med **arbejdsmiljø** og **sikkerhed** som faste punkter på ugen.', after=70)

    m.section('SERVICEBILEN — MONTØRER, KUNDER OG PLANLÆGNING')
    for label, body in [
        ('Vognen og materialet',
         'Service fra egen virksomhed: **ordination** til vognen, materiale på sagen før afgang og fast '
         'leverandøraftale, så en manglende reservedel er en undtagelse — ikke en morgenrutine.'),
        ('Ruten og udkaldet',
         'Dagens **rute** og **udkald** planlagt fra morgenen: hvad der er booket, hvad der er akut, og '
         'hvem der har plads til det, der dukker op kl. 10 — kapacitetsanalyse hver morgen med 11 '
         'samtidige opgaver og 14 medarbejdere i 2022.'),
        ('Sedlen og timerne',
         '**Seddel**, timer og **dokumentation** ind samme dag; i pharma var det et krav (GMP), i egen '
         'virksomhed er det, der gør fakturaen til en formalitet i stedet for en diskussion.'),
        ('Kunden',
         '**Kundekontakt** i 20+ år med private og erhverv: den, der tager opgaven, ejer den til den er '
         'lukket, og kunden har et navn — ikke et telefonnummer til en hovedtelefon.'),
        ('Montørerne',
         '5 elektrikere og 3 lærlinge med daglig **sparring**, **oplæring** og **KPI**-opfølgning; '
         '**trivsel** som fast punkt og MUS hvert år, fordi den stille mand er den, man mister først.')]:
        m.bullet(label, body, after=16)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · service og entreprise',
         [('Service, kunder og økonomi',
           '**Service** og akutte udkald for private og erhverv; tilbud, **materialer** og '
           '**dokumentation**; **arbejdsmiljø** med APV, LOTO og sikkerhedsrundering.')]),
        ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen',
         'Data Power Consultant ApS · København · 2024–nov. 2026 (sideløbende med ELOHVAC)',
         '4–10 personer · tekniske og industrielle applikationer',
         [('AI i drift og ledelse',
           'AI-coding og tekniske applikationer samt AI i ledelsesarbejdet — rapportering, '
           'beslutningsoplæg og **KPI**-analyse; selskabet er ophørt.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('Krav, dokumentation og aflevering',
           'Kravspecifikation, FAT/SAT og idriftsættelse; **dokumentation** bygget undervejs og nul '
           'kritiske afvigelser ved aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter',
         [('Fremdrift og kapacitet',
           'Dagligt tavlemøde, kapacitetsanalyse og omprioritering samme dag; **materialer** og '
           'underentreprenører styret mod aftalt dato.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Biofos (Lynetten) · København · aug. 2017–jan. 2022',
         'Renseanlæg i 24/7-drift · pumper, højspændingstavler, SCADA',
         [('Drift, fejlfinding og responstid',
           'Akut fejlfinding døgnet rundt med **responstid** som krav; **over 40 % lavere '
           'energiforbrug** gennem måling og indregulering.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 teknikere · maskinværksted · maskiner og materiel',
         [('Værksted, materiel og fejlfinding',
           'Fejlfinding, kalibrering og reparation; indkøb og vedligehold af materiel; oplæring og '
           'opfølgning for 12 teknikere.')]),
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
    m.para('Dansk og engelsk, skriftligt og mundtligt · Persisk: modersmål · **IT**: **E-Komplet** har '
           'jeg ikke arbejdet i, men det er samme type system som dem, jeg har brugt: sag, materiale, '
           'timer og faktura i én kæde (ERP-baserede drifts- og økonomisystemer, CMMS, Excel og egne '
           '**Python**-værktøjer til **KPI**) · **Kørekort B og egen bil** · Måløv, 20 minutter fra '
           'Gentofte · Kan starte efter aftale · Referencer på forespørgsel.', after=50)

    m.models_table('OPSLAGETS KRAV — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Samlet ansvar for make:nets serviceområde',
         'Service og entreprise i egen virksomhed siden 2023 med fuldt **P&L**: tilbud, **materialer**, '
         '**dokumentation** og kunder i samme rolle — 5 elektrikere og 3 lærlinge.'),
        ('Lede de serviceelektrikere, der dagligt kører ud til kunderne',
         'Daglig ledelse af **montører** og elektrikere i 20+ år: 5 elektrikere og 3 lærlinge i egen '
         'virksomhed, 14 medarbejdere og underentreprenører i 11 samtidige projekter.'),
        ('Fordele opgaverne og sikre at ordre og materialer er på plads, før montøren kører',
         'Morgenfordeling med **ordre** og **materialer** tjekket før afgang; kapacitetsanalyse hver '
         'morgen og omprioritering samme dag, når noget akut kom ind.'),
        ('Holde kontakten med kunderne, så de ved hvem der tager sig af dem',
         '**Kundekontakt** i 20+ år: den, der tager opgaven, ejer den til den er lukket, og kunden har '
         'et navn — ikke en omstilling.'),
        ('Være ude at se på opgaver og følge op hos kunder og montører',
         'Jeg har stået i værkstedet og på anlægget, ikke kun i mødelokalet: 5 år i 24/7-drift og en '
         'virksomhed, hvor kunden ringer til den, der ejer den.'),
        ('Arbejde i E-Komplet som fælles sagsstyrings- og økonomisystem',
         'Ikke E-Komplet specifikt, men samme type system: ERP-baserede drifts- og økonomisystemer, '
         'CMMS og egne værktøjer, hvor sag, materiale, timer og faktura hænger sammen.'),
        ('Overtage kunderne gradvist og bygge relationerne videre',
         'Kundekredsen i egen virksomhed er opbygget fra nul til 8 ansatte på to år — relationer bygget '
         'på at have svaret, når der blev ringet.'),
        ('Sikre høj kvalitet gennem løbende sparring og opfølgning, og udvikle montørerne fagligt',
         'Fast **sparring** på opgaven og KS-tjekliste før aflevering: 37 projekter med nul kritiske '
         'afvigelser; **oplæring** af 12 teknikere og 3 lærlinge i standarder, de selv var med til at '
         'skrive.'),
        ('Have blik for teamets trivsel og reagere, når en kollega har brug for støtte',
         '**Trivsel** som fast punkt: 1:1 og MUS, opfølgning på sygefravær og en aftale om, at den '
         'stille mand bliver spurgt først — 8 ansatte og 12 teknikere gennem årene.'),
        ('Bruge ressourcerne på tværs af stærkstrøm og netværk',
         '**Stærkstrøm** i bund som elektriker og **elautoriseret maskinmester**; **netværk**, **alarm** '
         'og **sikring** samt **overvågning** fra ELOHVAC og PDS/ABA-arbejde i pharma.'),
        ('Referere til direktøren i en flad organisation',
         'Vant til korte beslutningsveje: egen virksomhed har ingen mellemled, og i pharma gik '
         'beslutningsoplæg på 1-2 sider direkte til projektchef og bygherre.'),
        ('Holde aftalerne med kunderne og svare hurtigt, når en opgave driller',
         'Aftaler holdt med en ringe-besked, før kunden opdagede det; **responstid** som **KPI** i '
         'serviceaftaler og fem år med akut fejlfinding om natten.'),
        ('Bruge den fælles planlægning, så alle kan se, hvad der sker',
         'Én tavle og ét system for alle: i 11 samtidige projekter kunne både sjak og kunde se, hvad '
         'der var booket, og hvad der blev rykket.'),
        ('Give en montør en hånd, både med værktøjet og med det, der fylder',
         'Jeg har selv stået med værktøjet, når dagen var kort, og jeg har taget samtalen bagefter — '
         'begge dele hører til jobbet.'),
        ('Uddannet elektriker, gerne el-installatør',
         '**Elektriker** i bund og **elautoriseret maskinmester (LV/MV/HV)**, Sikkerhedsstyrelsen 2023 '
         '— ikke el-installatør, hvilket opslaget selv siger ikke er nødvendigt.'),
        ('Erfaring som serviceleder, servicekoordinator eller overmontør',
         'Service og daglig koordinering i egen virksomhed siden 2023, projekt- og værkstedsleder med '
         '14 mand i 2022 og driftsleder i 24/7-drift i fem år.'),
        ('Erfaring med kundekontakt i service og kendskab til forløbet fra aftale til dokumentation',
         '**Kundekontakt** i service i 20+ år, fra akutte udkald til planlagte opgaver; hele kæden — '
         'aftale, **materialer**, udførelse, **dokumentation** og **opfølgning** — hver uge.'),
        ('Være struktureret og trives med et fælles sags- og planlægningssystem',
         '5S og standard work indført i værksted og på anlæg; **planlægning** på tavle og i system, '
         'ikke i hovedet på den enkelte.'),
        ('Kunne se mennesket bag montøren og samtidig sætte en tydelig ramme',
         'Tydelig ramme og personlig opfølgning: standarder skrevet sammen med dem, der skal arbejde '
         'efter dem, og en samtale, når nogen er gået i stå.'),
        ('Udpræget servicesans over for kunderne',
         '**Service** som fag, ikke som tilbehør: kunden skal vide, hvem der kommer, hvornår, og hvad '
         'det koster — også når dagen skrider.')])

    m.section('DE FØRSTE 90 DAGE')
    for b in (
        'Kørt med på opgaver i de første uger og set, hvordan dagen faktisk former sig — ikke kun '
        'hvordan den er planlagt.',
        'Overtaget kunderne gradvist med en fast introduktion: hvem de er, hvad de plejer at få, og '
        'hvem der har deres sag i dag.',
        'Sat morgenfordelingen op som et tjek — ordre, materiale, adgang — og aftalt med '
        'entrepriseafdelingen, hvor grænsen mellem service og entreprise går.',
        'Siddet med i E-Komplet og den fælles planlægning, til jeg kunne slå en sag op uden at '
        'spørge om vejen, og sat navn på, hvem der har hvilke kunder.'):
        m.bullet('', b, after=16)

    m.section('SÅDAN VILLE JEG MÅLE DET')
    for b in (
        '**Materialet på vognen ved afgang** — andelen af opgaver, der kan køres uden et stop undervejs.',
        '**Genopkald pr. opgave** — hvor ofte vi kommer igen for det samme, og hvorfor.',
        '**Kunden kendte navn og tid** — andelen af besøg, hvor kunden vidste, hvem der kom, og '
        'hvornår, inden bilen holdt.'):
        m.bullet('', b, after=16)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Makenet_Serviceleder.docx')
    build(out)
    print(out)
