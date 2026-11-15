# -*- coding: utf-8 -*-
"""Novafos A/S — Projektleder til overløbsbygværker, Birkerød.

Form (master/FORMKATALOG.md): åbning **E** (tidsforskydningen: overløbet sker i regnvejr,
beslutningen tages i tørvejr), struktur **To veje** (den billige og den dyre løsning, og
hvornår man vælger hvilken), register **Afløbets** (vandstand, udløb, bassin, tørvejr) —
nyt register. Kulturfil: jd/Novafos_ProjektlederOverloeb_kultur.txt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Projektleder · overløbsbygværker, måleteknik og afløbssystemer'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('8. november 2026')
    m.meta('Novafos A/S · Spildevand · Blokken 9, Birkerød')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Projektleder til overløbsbygværker', bold=True, color='1A1A1A')
    m.para('Til ansættelsesudvalget i Novafos', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('**Overløbet sker i et skybrud i august. Beslutningen om det bliver taget i tørvejr i '
           'februar — når nogen vælger, om bygværket skal måles, optimeres eller rives ned og '
           'bygges om.** Det er den beslutning, stillingen handler om, og den er svær, fordi '
           '**overløbsbygværket er en sikkerhedsventil**: det skal helst aldrig bruges, og når det '
           'gør, er der sjældent nogen, der ser det. Derfor er **måling** ikke en detalje i denne '
           'stilling. Det er det, der gør de næste fire års renoveringer til en prioritering frem for '
           'en mavefornemmelse.', after=80)

    m.para('**Novafos har 3.400–4.000 km ledninger til regnvand og spildevand, 74.000 kunder og en '
           'indberetning til PULS, der hvert år gør overløbene op. Det, der mangler, er ikke tal.** '
           'Det er ensartet måling på tværs af ni kommuner — og en projektleder, der kan føre den fra '
           'beslutning til bygværk i hver enkelt **kommune**.', after=70)

    m.para('**I skriver, at målet er et mere datadrevet og robust afløbssystem, og at I arbejder på '
           'ensartede, fagligt funderede retningslinjer for, hvornår der etableres måling på et '
           'overløb.** Det er præcis den beslutning, der gør forskellen: ikke om der bliver målt, men '
           'om der bliver målt efter samme regel i alle ni kommuner — og om den regel kan forklares '
           'for en driftsmedarbejder, der skal vedligeholde måleren bagefter.', after=60)

    m.para('**To veje — og der findes kun to, når et overløb skal måles.**', after=60)

    m.para('**Vej 1: vandstandsmåleren.** Billig, hurtig at etablere, og god når spørgsmålet er, hvorvidt der '
           'der løber over. Den fortæller vandstanden i bygværket, ikke mængden i udløbet — og den '
           'skal kontrolleres, før nogen bygger en investeringsplan på den. Det er her, jeg ville '
           'starte i de kommuner, hvor målingen i dag er tyndest.', after=60)

    m.para('**Vej 2: flowmåleren.** Præcis, fordi den sidder i ledningen og måler det, der faktisk '
           'løber ud. Prisen er ikke kun indkøbet: måleren skal kunne komme til, den skal '
           'kalibreres, og nogen skal ned i nærheden af spildevandet for at tjekke den. Den vælges, '
           'hvor tallet skal bruges til at prioritere mellem bygværker — eller til at dokumentere '
           'effekten af en renovering over for myndigheden.', after=60)

    m.para('**Den tredje vej findes også, og den er dyrest: at bygge om uden at måle først.** Det er '
           'den rigtige løsning, når bygværket er problemet — for lille bassin, forkert tærskel, '
           'utæt konstruktion. Det er den forkerte, når problemet er drift: et sætpunkt, en '
           'pumpekurve eller en indstilling, der kan rettes for en brøkdel. Jeg har brugt fem år på '
           'at rette præcis den slags, før nogen byggede nyt — på et **renseanlæg** med **SRO**, '
           'pumper og vandstandsmålinger, hvor **over 40 % lavere energiforbrug** kom ud af måling og '
           'indregulering frem for af en ny installation.', after=70)

    m.para('**Projektledelse er ikke den del, jeg skal lære.** Jeg har ført **37 kapitalprojekter** '
           'fra krav til aflevering med **FAT/SAT**, **nul kritiske fund** og månedlig rapportering af '
           'fremdrift, økonomi og risiko; 11 samtidige anlægsprojekter i 2022 og egen virksomhed med '
           '**fuldt P&L** siden 2023. **AB 18** og entreprisekontrakter har jeg arbejdet under som '
           'entreprenør — udbud, **kontraktstyring**, ændringer og aflevering — og jeg ved, hvad et '
           'udbudsdokument skal indeholde, for at det ikke bliver en tvist.', after=70)

    m.para('**Måleteknik og instrumentering er min hjemmebane.** SRO/SCADA, **vandstandsmåler**e, '
           '**flowmåler**e, tryk og temperatur i døgndrift; **kalibrering** og følerefterlevelse; '
           '**dataopsamling** til **PULS**-indberetning og til de beslutninger, der kommer efter. Jeg '
           'bygger selv værktøjer i Python til at rense og sammenstille måledata — og jeg ved, at en '
           'måler, ingen har tid til at vedligeholde, bliver en dato i et regneark i stedet for en '
           'måling.', after=70)

    m.para('**Det, jeg ikke har, skal stå klart:** jeg har ikke projekteret **overløbsbygværker** fra '
           'net-siden, og **GIS** og **hydraulik** er ikke mine værktøjer. Jeg har arbejdet på den '
           'anden side af renseanlægget i fem år, hvor overløb og belastning var noget, vi mærkede — '
           'og jeg vil hellere lære jeres bygværker at kende med en måler i hånden end på et kursus.',
           after=70)

    m.para('Novafos er et **klimavenligt forsyningsselskab**, og **klimasikring** og **bæredygtighed** '
           'er den ramme, overløbene skal løses i. **Værdi for både samfund og miljø** er ikke en '
           'bisætning, når et bassin skal dimensioneres: det er argumentet for at måle først og bygge '
           'bagefter. Og når I samtidig vægter **balancen mellem arbejde og fritid**, et **trygt og '
           'stabilt arbejdsmiljø** og **overskud til familie og privatliv**, er det for mig et tegn på, '
           'at der er tænkt over, hvad der holder erfarne folk i forsyningen i tyve år.', after=70)

    m.para('**Praktisk:** jeg bor i Måløv, 25 minutter fra Blokken 9, har kørekort og bil og kan være '
           'på anlæggene i hele forsyningsområdet. Jeg taler dansk som modersmål og engelsk '
           'professionelt, og jeg kan starte efter aftale. Jeg vil gerne høre, hvor I er med **Plan '
           'for måling af overløb**, og hvilke bygværker der står først — det er der, jeg ville '
           'begynde.', after=70)

    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Projektleder med 20+ års erfaring fra tekniske anlæg i døgndrift — **elautoriseret '
           'maskinmester (LV/MV/HV)** med B.Tech i teknologiledelse og maskinteknik. Har ført **37 '
           'kapitalprojekter** fra krav til aflevering med FAT/SAT og **nul kritiske fund**, **11 '
           'samtidige anlægsprojekter** med 14 medarbejdere og drevet et **renseanlæg** i 24/7-drift '
           'i fem år med **SRO**, **vandstandsmålinger**, pumper og **over 40 % lavere '
           'energiforbrug**. Arbejder under **AB 18** og entreprisekontrakter, med **udbud**, '
           '**budget** og **økonomiopfølgning** som fast del af rollen.', after=80)

    m.section('AFLØBET — MÅLING, DRIFT OG OVERLØB')
    for label, body in [
        ('Måling og instrumentering',
         'SRO/SCADA i døgndrift med **vandstandsmåler**e, tryk- og temperaturfølere og '
         '**flowmåling**; **kalibrering** og følerefterlevelse kontrolleret, fordi et tal uden '
         'reference er en antagelse.'),
        ('Drift af et renseanlæg',
         'Fem år som drifts- og vedligeholdelsesleder på Lynetten under Biofos: belastning, overløb, '
         'pumper, bassiner og 24/7-drift — hvor et stop blev bemærket i hele byen; drift af '
         '**renseanlæg**; dertil drift af **pumpestation** og tilhørende anlæg.'),
        ('Projekt fra behov til overdragelse',
         '37 kapitalprojekter: behovsafdækning, løsningsvalg, kravspecifikation, udførelse, FAT/SAT '
         'og **overdragelse** til drift med dokumentation, der kunne bruges bagefter.'),
        ('Udbud, kontrakter og leverandører',
         'Udbud og **kontraktstyring** under **AB 18** i egen **entreprise**; rådgivere og entreprenører styret på tid, '
         'pris og kvalitet — og leverancer afvist, når de ikke holdt kontrakten.'),
        ('Økonomi og prioritering',
         'Projektbudgetter på 2–10 mio. kr. og fuldt P&L siden 2023; **budgetlægning** og '
         '**økonomiopfølgning** med månedlig afvigelsesforklaring til ledelse og bygherre.'),
        ('Data, dokumentation og AI',
         'Egne Python-værktøjer til at rense og sammenstille måledata og til tjeklister og rapporter '
         '— over 40 % færre manuelle timer; dokumentation skrevet, så den næste kunne overtage.')]:
        m.bullet(label, body, after=25)

    m.models_table('SYSTEMER OG METODER', ('Område', 'Dokumenteret brug'), [
        ('Styring og måling',
         'SRO/SCADA, alarmer og trends; vandstands- og flowmålinger vurderet mod reference og fulgt '
         'op med inspektion ved anlægget.'),
        ('Projekt og leverance',
         'Kravspecifikation, udbudsmateriale, FAT/SAT og afleveringspakker; fremdrift, økonomi og '
         'risiko rapporteret månedligt.'),
        ('Kontrakt og økonomi',
         'AB 18, entreprisekontrakter og ændringshåndtering; budget, dækningsgrad og '
         'betalingsopfølgning i egen virksomhed.'),
        ('Myndigheder og parter',
         'Dokumentation til tilsyn og godkendelse i 37 projekter; møder og korrespondance med '
         'myndigheder, rådgivere, entreprenører og bygherre.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · elautorisation · service- og entrepriseydelser',
         [('Projekt, kontrakt og økonomi',
           'Tilbud, udbud og ændringshåndtering; budget og **økonomiopfølgning**; kunder, rådgivere '
           'og entreprenører i daglig koordinering.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('Krav, udførelse og aflevering',
           'Kravspecifikation, FAT/SAT og idriftsættelse; afvigelser lukket med navn og dato; nul '
           'kritiske fund ved aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter',
         [('Fremdrift og koordinering',
           'Dagligt tavlemøde, kapacitetsanalyse og omprioritering samme dag; leverancer styret til '
           'deadline med afleveringspakker.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Lynetten under Biofos · København · aug. 2017–jan. 2022',
         'Renseanlæg i 24/7-drift · SRO · belastning, overløb, pumper, bassiner',
         [('Drift, måling og energi',
           'Belastning og overløb fulgt i døgndrift; vandstands- og flowmålinger brugt til '
           'prioritering; energiledelse med over 40 % lavere forbrug; 5S og standard work.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 teknikere · maskinværksted · industrielt udstyr',
         [('Teknisk service og fejlfinding',
           'Fejlfinding, kalibrering og reparation på industrielt udstyr; oplæring og opfølgning på '
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
    m.edu('Køle- og ventilationsteknik · AMU', 'Mercantec 2021 · STCW, Søfartsstyrelsen 2021')
    m.edu('El- og maskinteknisk konstruktion, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6')

    m.section('SPROG, PRAKTIK OG REFERENCER')
    m.para('Dansk: modersmål · Engelsk: professionelt, også teknisk · Persisk: modersmål · '
           '**Kørekort B og egen bil** · Måløv, 25 minutter fra Birkerød · Kan starte efter aftale · '
           'Referencer på forespørgsel.', after=70)

    m.models_table('OPSLAGETS KRAV — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Projektledelse af renovering og optimering af overløbsbygværker',
         'Projektledelse af 37 kapitalprojekter og 11 samtidige anlægsprojekter fra behov til '
         'aflevering; overløbsbygværker arbejder jeg med for første gang — metoden er den samme, '
         'anlæggene er nye.'),
        ('Etablering, udskiftning og idriftsættelse af målere på overløb',
         'Måling og instrumentering i 5 år: SRO, vandstandsmålere, tryk og temperatur i døgndrift; '
         'kalibrering og følerefterlevelse kontrolleret; idriftsættelse med FAT/SAT i 37 projekter.'),
        ('Planlægning, styring og koordinering af projekter fra start til slut',
         'Fremdrift, økonomi og risiko rapporteret månedligt i 37 projekter og 11 samtidige '
         'anlægsprojekter; leverancer styret til deadline med afleveringspakker.'),
        ('Budgetlægning og økonomiopfølgning',
         'Projektbudgetter på 2–10 mio. kr. pr. projekt i 37 projekter med månedlig opfølgning; '
         'fuldt P&L og lønbudget for 8 medarbejdere siden 2023.'),
        ('Udbud, kontraktstyring og samarbejde med rådgivere og entreprenører',
         'Udbud og kontraktstyring under AB 18; rådgivere og entreprenører styret på tid, pris og '
         'kvalitet i 37 projekter og egne entrepriser; leverancer afvist, når kontrakten ikke holdt.'),
        ('Dialog med kommuner og myndigheder',
         'Dokumentation til tilsyn og godkendelse i 37 projekter under GMP/FDA/EMA; møder og '
         'korrespondance med myndigheder, bygherre og rådgivere gennem 20+ år.'),
        ('Kvalitetssikring, dokumentation og overdragelse til drift',
         'FAT/SAT, IQ/OQ og afleveringspakker i 37 projekter med nul kritiske fund; dokumentation '
         'skrevet, så næste vagt kunne overtage, og afvigelser lukket med navn og dato.'),
        ('Faglig sparring om måleteknik og overløbsløsninger på tværs af organisationen',
         'Sparring om måling, regulering og fejlfinding i 20+ år; undervist og oplært 12-14 '
         'medarbejdere og 3 lærlinge; skrevet tjeklister og standarder, andre kunne arbejde efter.'),
        ('Arbejder struktureret og selvstændigt',
         'Egen virksomhed med fuldt ansvar siden 2023; 37 projekter drevet selvstændigt fra krav til '
         'aflevering; faste ugentlige opfølgninger og skriftlige afvigelser.'),
        ('Blik for både helhed, økonomi og tekniske detaljer',
         '37 projekter med både budgetansvar og teknisk aflevering; investeringer valgt, hvor de '
         'kunne tjenes ind — over 40 % lavere energiforbrug som dokumenteret resultat.'),
        ('Analytisk og løsningsorienteret',
         'Fast rækkefølge: data, hypotese, måling ved anlægget, konklusion — brugt i 5 års døgndrift '
         'og i 37 afleveringer; fejl lukket med årsag, ikke kun med en kvittering.'),
        ('Kan skabe gode samarbejdsrelationer på tværs af fagligheder',
         '25 specialister koordineret på 37 projekter; grænseflader mellem el, ventilation, VVS, '
         'styring og bygherre aftalt skriftligt med ejer og dato.'),
        ('Kommunikerer klart og professionelt',
         'Dansk modersmål og engelsk professionelt, også i forhandlinger; beslutningsoplæg på en til '
         'to sider, referater med navn og dato og fremlæggelse for ikke-tekniske modtagere i 20+ år.'),
        ('Trives med at kombinere projektledelse og teknik',
         'Projektleder, der selv har stået med instrumentet: 37 projekter med teknisk aflevering og '
         '5 år med fejlfinding, måling og regulering ved anlægget.'),
        ('Erfaring med afløbssystemer, spildevand eller forsyningsområdet',
         'Fem år på et renseanlæg i 24/7-drift med belastning, overløb, bassiner og pumper; '
         'spildevandsprocessen kendt fra driftsiden, ledningsnettet er det nye.'),
        ('Erfaring med måleteknik, dataopsamling eller instrumentering',
         'Vandstands-, tryk-, temperatur- og flowmålinger i SRO/SCADA i 5 års døgndrift; data renset og '
         'sammenstillet til rapportering og beslutninger med egne Python-værktøjer.'),
        ('Erfaring med bygge- og anlægsprojekter',
         '11 samtidige anlægsprojekter i 2022 med 14 medarbejdere og underentreprenører; 37 '
         'kapitalprojekter med byggeplads, FAT/SAT og aflevering.'),
        ('Erfaring med projektledelse og projektstyring',
         'Projektledelse i 20+ år: 37 kapitalprojekter, 11 anlægsprojekter, egen virksomhed med 8 '
         'medarbejdere — fremdrift, økonomi, risiko og interessenter i samme model.'),
        ('Erfaring med AB18 og entreprisekontrakter',
         'Arbejdet under AB 18 og beslægtede kontraktgrundlag som entreprenør: udbud, mængder, '
         'ændringshåndtering, fristforlængelser og aflevering i egne entrepriser og serviceaftaler.'),
        ('Erfaring med GIS eller hydrauliske forhold',
         'Ikke dokumenteret: GIS og hydrauliske beregninger er ikke mine værktøjer efter 20+ år i drift og '
         '37 projekter. Til gengæld har '
         'jeg arbejdet med måledata og anlægsdrift, hvor forståelsen for vandets vej er det, der gør '
         'tallene brugbare.'),
        ('Relevant teknisk uddannelse som ingeniør, bygningskonstruktør eller lignende',
         'Elautoriseret maskinmester (LV/MV/HV), Sikkerhedsstyrelsen 2023; B.Tech i teknologiledelse '
         'og maskinteknik 2017-2022 med 7,6/12; el- og maskinteknisk konstruktion 2000-2003, EQF 6.')])


    m.models_table('HVORNÅR MÅLER VI — OG HVORNÅR BYGGER VI OM',
                   ('Det, der ses i bygværket', 'Den vej jeg ville vælge, og hvorfor'), [
        ('Overløb ved næsten hver regnbyge',
         'Mål først: en vandstandsmåler i bygværket og en gennemgang af tærskel og indløb. Er bassinet '
         'for lille, er det en renovering — er tærsklen forkert, er det en justering. Forskellen '
         'koster millioner, og den kan afgøres på en uge.'),
        ('Overløb kun ved skybrud',
         'Mål flowmåleren, hvis mængden skal indgå i en prioritering mellem bygværker eller '
         'dokumenteres over for myndigheden. Byg ikke om endnu: et sjældent overløb i et skybrud er '
         'sikkerhedsventilen, der gør sit arbejde.'),
        ('Overløb i tørvejr',
         'Det er ikke et kapacitetsproblem, og det er ikke et måleproblem. Det er en fejl — utæthed, '
         'fejlkobling eller en styring, der står forkert — og den skal findes, før nogen tegner et '
         'bassin.'),
        ('Ingen overløb i måleperioden',
         'Mål ikke alt. I en målekampagne på 27 bygværker havde 12 ingen overløb; ressourcen hører '
         'til der, hvor der faktisk løber over, og dokumentationen hører til hos myndigheden.')])


    m.section('DE FØRSTE 90 DAGE')
    for b in (
        'En status pr. bygværk: findes der måling, hvilken type, sidste kalibrering, og hvilke '
        'bygværker har overløb i PULS-indberetningen — lagt ind i samme skema for alle ni kommuner.',
        'En prioritering efter hyppighed og mængde, ikke efter alder: de bygværker, der løber over '
        'ofte, får måling og renovering først, og de øvrige får dokumentation for hvorfor de venter.',
        'Ét bygværk kørt hele vejen — undersøgelse, løsningsvalg, projektering, udbud, udførelse og '
        'overdragelse til drift — så metoden er prøvet, før den skrives ned som retningslinje.'):
        m.bullet('', b, after=25)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Novafos_ProjektlederOverloeb.docx')
    build(out)
    print(out)
