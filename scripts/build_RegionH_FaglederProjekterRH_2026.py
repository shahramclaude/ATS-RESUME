# -*- coding: utf-8 -*-
"""Region Hovedstaden, Center for Ejendomme — Drift og Byg, Rigshospitalet:
Fagleder for projekter (rekruttering: Dansk HR Service, frist 20.11.2026).

Form (master/FORMKATALOG.md): åbning **G** (spørgsmålet: hvornår er et
byggeprojekt på et hospital færdigt?), struktur **Fordelingen af ansvar**
(beslutningen · grænsefladen · afbrydelsen · pengene · afleveringen), register
**Driftsvinduet** (nyt: afbrydelse, varsling, sluse, støjzone, midlertidig
forsyning, tilbagekobling, driftsejer). Kulturfil:
jd/RegionH_FaglederProjekterRH_2026_kultur.txt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Fagleder for projekter · Drift og Byg · Rigshospitalet'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('13. november 2026')
    m.meta('Region Hovedstaden · Center for Ejendomme, Drift og Byg · Rigshospitalet · '
           'via Dansk HR Service')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Fagleder for projekter, Drift og Byg', bold=True, color='1A1A1A')

    def lp(text, after=60):
        return m.para(text, after=after, line=236)

    # ---------------------------------------------------------------- side 1
    lp('**Hvornår er et byggeprojekt eller en renovering på et hospital egentlig færdigt?** '
           'Ikke når nøglen overgives. Det er færdigt den morgen, hvor afdelingen, der flyttede ind, '
           'har haft en uge uden at ringe for at spørge, hvorfor der stadig er støj over hovedet, og '
           'hvor den tekniske drift ikke længere holder et system kørende på en midlertidig løsning, '
           'ingen har skrevet ned. Mellem de to ligger det arbejde, rollen skal gøre muligt.', after=56)

    lp('**Drift og Byg gennemfører bygge- og renoveringsprojekter på Rigshospitalets '
           'matrikler**, og I skriver selv, at det sker **»i en hospitalsvirkelighed, hvor den '
           'daglige drift fortsætter, mens der bygges, ændres og udvikles omkring den«**. Rollen '
           'er en del af den lokale ledelse sammen med viceejendomschefen og de øvrige fagledere, og '
           'en **fagkoordinator arbejder tæt sammen med dig om prioritering og koordinering**. Fra 1. januar 2027 hedder '
           'centeret **Ejendomme og Byggerier**, når Region Hovedstaden og Region Sjælland lægges '
           'sammen — og så er **»fælles metoder, arbejdsgange og kvalitet i den måde, projekterne '
           'bliver gennemført på«** ikke en sætning i et opslag, men en opgave fra dag ét.', after=56)

    lp('**Fem ting, der skal fordeles, før et projekt kan lykkes.**', after=46)

    lp('**Beslutningen.** Et projekt sidder sjældent fast i teknikken; det sidder fast i et '
           'spørgsmål, ingen har stillet den, der må svare. Derfor har hvert projekt en '
           '**beslutningslog** med næste beslutning, hvem der ejer den, og hvad den koster at udskyde '
           '— og projektlederen ved, hvad han eller hun må beslutte selv. I Novo Nordisk var det 37 '
           'parallelle kapitalprojekter og 25 specialister.', after=40)

    lp('**Grænsefladen.** Det er **»en rolle med mange snitflader«**: den tekniske drift, '
           'supportfunktionerne, klinikken, hygiejnen og sikkerheden mærker projektet hver dag uden '
           'at være med i det. Hvert projekt får et **snitfladekort** — hvilken '
           'grænseflade, hvem der ejer den, hvem der varsler, og hvad der sker, hvis den ikke holdes. '
           'Sådan bliver det muligt at **»styrke samarbejdet mellem projektområdet, den tekniske '
           'drift, supportfunktionerne og hospitalets øvrige interessenter«** at følge op på.',
           after=40)

    lp('**Afbrydelsen.** Et projekt på en hospitalmatrikel er en plan for, hvornår noget ikke '
           'virker. **Driftsvinduet** aftales i uger: hvad der må slukkes, hvor længe, hvad der kører '
           'på **midlertidig forsyning**, hvilken **sluse** håndværkerne går igennem, hvilken '
           '**støjzone** der gælder hvornår, og hvem der kobler tilbage og kvitterer. Fem år i '
           '24/7-drift på Lynetten har lært mig, hvad **patientsikkerhed** og **driftsstabilitet** '
           'koster, når en afbrydelse bliver længere end aftalt.', after=40)

    lp('**Pengene.** **»Kvalitet og fremdrift i projektporteføljen med blik for økonomi, '
           'tidsplaner og risici«** kræver én oversigt, som er sand: pr. projekt økonomi mod budget, '
           'næste milepæl, de tre største risici og det, der skal besluttes i denne måned. **Udbud, '
           'kontrakter og projektopfølgning** har jeg arbejdet med fra begge sider — som leverandør '
           'med fast pris og garantiansvar og som bygherresidens med **FAT/SAT** og **IQ/OQ/PQ**.', after=40)

    lp('**Afleveringen.** Den er ikke en dato, men en liste: dokumentation, as-built, '
           'driftsinstruks, oplæring af dem, der skal overtage, og en prøveperiode, hvor fejlene '
           'bliver rettet, mens **rådgiveren** og **entreprenøren** stadig er på kontrakten. At **»få '
           'komplekse projekter sikkert fra beslutning til aflevering«** kom ikke af held: **37 '
           'projekter med nul kritiske afvigelser**, fordi dokumentationen blev skrevet undervejs og '
           'afleveringen var et møde med en dagsorden.', after=52)

    lp('**Det er mennesker, der leverer — ikke porteføljen.** Jeg har ledet **14 medarbejdere i '
           '11 samtidige projekter**, 25 specialister i en GMP-organisation og i dag **5 elektrikere '
           'og 3 lærlinge**: skreven **forventningsaftale** pr. medarbejder, **faglig sparring** på '
           'sagen frem for timerkontrol og **kompetenceudvikling** i en plan, der tages op hvert kvartal. '
           'Jeg har '
           'ikke ledet en gruppe projektledere før, men fagligt stærke medarbejdere, der vidste mere '
           'end mig — og det er disciplinen: **»stille de rigtige spørgsmål, udfordre '
           'konstruktivt«** og lade svaret være deres, fordi man **»skaber resultater gennem '
           'andre«**.', after=56)

    lp('**Det, jeg ikke har, står her.** Jeg har ikke været ansat i en offentlig '
           'bygherrefunktion med regionsråd og politisk budgetproces, og jeg har ikke bygget på et '
           'hospital. Det tætteste er en GMP-fabrik i drift '
           '(37 kapitalprojekter), et renseanlæg i 24/7-drift i fem år og 20+ år i tekniske '
           'installationer, hvor **elautoriseret maskinmester (LV/MV/HV)** betyder, at jeg kan se på '
           'en tavle eller et CTS-anlæg og vide, om det, der bliver lovet, kan lade sig gøre.',
           after=56)

    lp('**Jeres eget sprog er grunden til, at jeg søger.** I vil have en, der kan **»skabe de '
           'rammer, der gør projektlederne i stand til at lykkes«** og er **»tæt nok på projekterne '
           'til at kunne udfordre, sparre og hjælpe med prioriteringer«**. I kalder det at **»lede mennesker og sikre kvalitet og fremdrift '
           'på tværs af den samlede projektportefølje«**, med **»klare rammer, følger op på de '
           'væsentlige projekter«** og sørger for, at **»teamets tid og kompetencer bliver brugt '
           'rigtigt«**. I efterspørger **»faglig sparring, tydelige forventninger og løbende '
           'opfølgning«** og **»gode rammer for prioritering og ressourcefordeling på tværs af '
           'projekterne«** — og en leder, der er **»tydelig om retning og forventninger«**, kan '
           '**»samle forskellige perspektiver og skabe fremdrift«**, fordi **»En leder, der skaber '
           'følgeskab«** gør det ved at give plads.', after=56)

    lp('**Praktisk:** Måløv, 25 minutter fra Rigshospitalet og 20 fra Glostrup, kørekort B og bil, '
           'kan starte efter aftale, og arbejdsdagene kan lægges, så begge matrikler får en fast dag.',
           after=24)

    m.meta('Med venlig hilsen', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('**Teknisk leder med bygge- og anlægsprojekter i drift** — **elautoriseret maskinmester '
           '(LV/MV/HV)**, B.Tech i teknologiledelse og maskinteknik. 20+ år i tekniske '
           'installationer, **37 kapitalprojekter** i en GMP-fabrik i drift, **11 samtidige '
           'anlægsprojekter** med 14 medarbejdere og fem år som driftsleder i **24/7-drift**. '
           'Arbejder med **porteføljestyring**, **beslutningslog**, **snitfladekort** og '
           '**driftsvinduer** — og med den del, der sjældent står i en projektmodel: at gøre '
           'projektlederen i stand til at træffe beslutningen selv.', after=70)

    m.section('DRIFTSVINDUET — PROJEKTER, DRIFT OG MENNESKER')
    for label, body in [
        ('Driftsvinduet',
         '**Afbrydelse**, **varsling**, **sluse**, **støjzone**, **midlertidig forsyning** og '
         '**tilbagekobling** med kvittering — fem år i 24/7-drift og 37 projekter i en fabrik, der '
         'kørte videre, mens vi byggede.'),
        ('Porteføljen',
         'Én oversigt pr. projekt: økonomi mod budget, næste milepæl, de tre største **risici** og '
         'den beslutning, der skal tages i denne måned — 37 parallelle kapitalprojekter med 25 '
         'specialister i 2023-2024.'),
        ('Grænsefladen',
         '**Snitfladekort** med driftsejer, varslingsvej og konsekvens; grænsefladen skrevet ned, '
         'før arbejdet starter — mellem projekt, teknisk drift, support og den klinik, der skal '
         'bruge lokalet bagefter.'),
        ('Pengene og kontrakterne',
         '**Udbud**, tilbud, fast pris, **AB 18/ABT 18**, garantier og **afvigelser**, der skal '
         'lukkes før overtagelse; både **totalentreprise** og **fagentreprise** med **entreprenører** '
         'og **rådgivere**; fuldt **P&L** siden 2023 og 37 CAPEX-sager med rådighedsbeløb.'),
        ('Menneskerne',
         '**Forventningsaftale** pr. medarbejder, **faglig sparring** på sagen, **kompetenceplan** '
         'hvert kvartal og **trivsel** som fast punkt — 14 medarbejdere, 25 specialister, 12 '
         'teknikere og 5 elektrikere plus 3 lærlinge gennem årene.')]:
        m.bullet(label, body, after=16)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · service og entreprise',
         [('Projekter, økonomi og aflevering',
           'Tilbud, **udbud**, materialer og **dokumentation**; projekter leveret med '
           '**egenkontrol** og afleveringsprotokol; **arbejdsmiljø** med APV, LOTO og '
           'sikkerhedsrundering.')]),
        ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen',
         'Data Power Consultant ApS · København · 2024–nov. 2026 (sideløbende med ELOHVAC)',
         '4–10 personer · tekniske og industrielle applikationer',
         [('Data i beslutninger',
           'Tekniske applikationer samt **AI** i ledelsesarbejdet — rapportering, beslutningsoplæg '
           'og **KPI**-analyse; selskabet er ophørt.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('Krav, afvigelser og aflevering',
           'Kravspecifikation, **FAT/SAT** og **IQ/OQ/PQ**; **dokumentation** bygget undervejs og '
           'nul kritiske afvigelser ved aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter',
         [('Fremdrift og kapacitet',
           'Dagligt tavlemøde, **kapacitetsmodel** og omprioritering samme dag; leverancer styret '
           'mod aftalt dato med underentreprenører og materialer.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Biofos (Lynetten) · København · aug. 2017–jan. 2022',
         'Renseanlæg i 24/7-drift · pumper, højspændingstavler, SCADA',
         [('Drift, afbrydelser og energi',
           'Planlagte **driftsvinduer** og akut fejlfinding døgnet rundt; **over 40 % lavere '
           'energiforbrug** gennem måling og indregulering.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 teknikere · maskinværksted · maskiner og materiel',
         [('Værksted, materiel og oplæring',
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
    m.para('Dansk og engelsk, skriftligt og mundtligt · Persisk: modersmål · **IT**: projekt- og '
           'økonomisystemer, **CMMS**, Excel-modeller og egne **Python**-værktøjer til '
           'porteføljeopfølgning; **5S** og standard work som arbejdsform · **Kørekort B og egen '
           'bil** · Måløv, cirka 25 minutter til Rigshospitalet og 20 minutter til Glostrup · Kan '
           'starte efter aftale · Referencer på forespørgsel.', after=50)

    m.models_table('OPSLAGETS KRAV — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Lede og udvikle projektteamet gennem faglig sparring, tydelige forventninger og løbende opfølgning',
         '**Sparring** på sagen, skreven **forventningsaftale** og opfølgning hver måned: 14 '
         'medarbejdere i 11 projekter, 25 specialister og 5 elektrikere plus 3 lærlinge.'),
        ('Sikre kvalitet og fremdrift i projektporteføljen med blik for økonomi, tidsplaner og risici',
         'Porteføljeoversigt pr. projekt med økonomi mod budget, næste milepæl og tre risici; 37 '
         'CAPEX-projekter med **nul kritiske afvigelser** og tidsplanen holdt.'),
        ('Skabe gode rammer for prioritering og ressourcefordeling på tværs af projekterne',
         '**Kapacitetsmodel** og dagligt tavlemøde med omprioritering samme dag: 11 anlægsprojekter '
         'og 14 medarbejdere fordelt efter det tidskritiske.'),
        ('Styrke samarbejdet mellem projektområdet, den tekniske drift, supportfunktionerne og hospitalets øvrige interessenter',
         '**Snitfladekort** pr. projekt med driftsejer og varslingsvej — mellem projekt, teknisk '
         'drift, hygiejne og den klinik, der skal bruge lokalet bagefter.'),
        ('Bidrage til fælles metoder, arbejdsgange og kvalitet i den måde, projekterne bliver gennemført på',
         '**Metodebog** med én arbejdsgang pr. proces, prøvekørt og målt før den blev standard; '
         '**5S** og standard work i værksted og på anlæg.'),
        ('Solid erfaring fra byggeprojekter og projektledelse',
         '20+ år i tekniske installationer og byggeri: 37 kapitalprojekter i en GMP-fabrik, 11 '
         'anlægsprojekter med 14 mand og projekter med fast pris og garanti.'),
        ('Få komplekse projekter sikkert fra beslutning til aflevering',
         'Fra kravspecifikation til **FAT/SAT**, **IQ/OQ/PQ** og driftsmodtagelse; afvigelser lukket '
         'før overtagelse — nul kritiske ved aflevering på 37 projekter.'),
        ('Erfaring med at lede projektledere eller andre fagligt stærke medarbejdere',
         'Ledet **specialister**, der vidste mere end mig: 25 i en GMP-organisation og 12 teknikere i '
         'et værksted — med skrevet mandat og fast sparringskadence.'),
        ('Ledelseserfaring og motiveres af at skabe resultater gennem andre',
         'Ledererfaring fra værksted til egen virksomhed: 12 teknikere, 14 medarbejdere, 25 specialister og 8 ansatte i '
         'egen virksomhed — resultatet er leverancerne, ikke min egen tid i sagen.'),
        ('Stille de rigtige spørgsmål, udfordre konstruktivt og hjælpe projektlederne med at finde vej',
         'Beslutningsoplæg på to sider med tre alternativer og en anbefaling, gennemgået med '
         'projektlederen inden mødet — spørgsmålet stilles, før beslutningen tages.'),
        ('Erfaring med offentlig bygherrefunktion',
         'Ikke ansat i en offentlig bygherreorganisation før; bygherresiden har jeg fra Novo Nordisk '
         '(CAPEX, rådgivere og entreprenører under GMP), leverandørsiden fra 20+ år.'),
        ('Erfaring med udbud, kontrakter og projektopfølgning',
         '**Udbud** og tilbud med fast pris, **AB 18/ABT 18**, garantiansvar og '
         'afvigelsesbehandling; fuldt **P&L** siden 2023 og 37 CAPEX-sager med budgetopfølgning.'),
        ('Tydelig om retning og forventninger og give medarbejderne plads til at bruge deres faglighed',
         'Skreven **forventningsaftale** med resultat, mandat og eskaleringsgrænse og frihed til at '
         'vælge metode; opfølgning på resultat — 8 ansatte og 25 specialister.'),
        ('Samle forskellige perspektiver og skabe fremdrift, når interesserne ikke peger samme vej',
         'Tværfaglige møder med drift, projekt, kvalitet og leverandør, hvor uenigheden blev skrevet '
         'ned som en beslutning med ejer og dato.'),
        ('Blik for teamets kompetencer, trivsel og faglige udvikling',
         '**Kompetenceplan** pr. medarbejder hvert kvartal, MUS hvert år, opfølgning på sygefravær og '
         'aftalen om, at den stille mand bliver spurgt først.'),
        ('Være sparringspartner for ejendomschefen og viceejendomschefen med et klart billede af porteføljen',
         'Månedlig ledelsesrapport på én side: fremdrift, økonomi, risiko og de beslutninger, der '
         'skal tages — samme format som oplæggene til bygherre i Novo Nordisk.'),
        ('Projekter i en hospitalsvirkelighed, hvor den daglige drift fortsætter',
         'Fem år i **24/7-drift** med planlagte **driftsvinduer** og akut fejlfinding, og 37 '
         'projekter i en GMP-fabrik, der kørte videre, mens vi byggede.'),
        ('Kendskab til bygninger og tekniske installationer',
         '**Elautoriseret maskinmester (LV/MV/HV)** og 20+ år med stærkstrøm, **VVS**, '
         '**ventilation**, **CTS**/**BMS**, alarm og netværk — kan læse en tavle og en CTS-oversigt.'),
        ('Arbejde tæt sammen med en fagkoordinator om prioritering og koordinering',
         'Vant til arbejdsdelingen: i 2022 koordinerede jeg 11 projekter med fast '
         'planlægningskadence og en tavle, som både sjak, kunde og underentreprenør kunne læse.'),
        ('Arbejdssted på Rigshospitalet i København og arbejdsdage på matriklen i Glostrup',
         'Bor i Måløv: 25 minutter til Rigshospitalet og 20 minutter til Glostrup, kørekort B og '
         'egen bil — to matrikler i samme uge er praktisk muligt.'),
        ('Uddannelse og ansættelse inden for en af overenskomsterne på det tekniske eller akademiske område',
         '**B.Tech** i teknologiledelse og maskinteknik (7,6/12) og **elautoriseret '
         'maskinmester** — professionsbachelor på det tekniske område.'),
    ])

    m.section('DE FØRSTE 90 DAGE')
    for b in (
        'Gået porteføljen igennem projekt for projekt med projektlederen selv — økonomi, næste '
        'beslutning og de tre risici, han eller hun holder øje med.',
        'Siddet med til de møder, hvor grænsefladen til teknisk drift og klinik bliver afgjort, og '
        'skrevet ned, hvem der ejer hvad, før det bliver en sag.',
        'Sat en fast kadence: månedlig porteføljegennemgang med fagkoordinatoren, sparring med den '
        'enkelte projektleder hver anden uge og én side til ejendomschefen.',
        'Aftalt med viceejendomschefen og de øvrige fagledere, hvilke metoder der skal være fælles '
        'først — før sammenlægningen til Ejendomme og Byggerier 1. januar 2027.'):
        m.bullet('', b, after=16)

    m.section('DET VILLE JEG SPØRGE OM')
    for b in (
        'Hvor mange projektledere er der i teamet i dag, og hvor mange projekter har den enkelte i '
        'porteføljen på samme tid?',
        'Hvordan måler I fremdrift og kvalitet i dag — og hvad ville I gerne kunne se, som I ikke kan '
        'se nu?',
        'Hvor ligger beslutningsretten i dag på ændringer og tillægsarbejde, og hvem skal '
        'faglederen have med, når den skal flyttes?'):
        m.bullet('', b, after=16)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_RegionH_FaglederProjekterRH_2026.docx')
    build(out)
    print(out)
