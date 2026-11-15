# -*- coding: utf-8 -*-
"""Novafos A/S — Projektleder til klimatilpasning og separatkloakering, Birkerød.

Form (master/FORMKATALOG.md): åbning **B** (negationen: det er ikke gravemaskinen,
det er analysen), struktur **Analysens fire spørgsmål** (hvor løber vandet hen i dag ·
hvor kan regnvandet være · hvem skal sige ja · hvad skal driften kunne om tredive år),
register **Ledningsgraven** (grøft, brønd, boring, TV-inspektion, skel, indkørsel) — nyt
register. Kulturfil: jd/Novafos_Klimatilpasning_kultur.txt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Projektleder · klimatilpasning, separatkloakering og spildevand'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('11. november 2026')
    m.meta('Novafos A/S · Klimatilpasning og spildevand · Blokken 9, Birkerød')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Projektleder til klimatilpasning og separatkloakering',
           bold=True, color='1A1A1A')
    m.para('Til Christina Daél, sektionsleder', after=44)

    # ---------------------------------------------------------------- side 1
    m.para('**Det er ikke gravemaskinen, der vælter en separatkloakering. Det er en analyse, der '
           'ikke svarede på, hvordan grundejeren skulle tilslutte sin egen grund.** Novafos må '
           'ikke arbejde på privat grund: regnvand og spildevand skal skilles på den anden side af '
           'skel, af en autoriseret kloakmester, i en have nogen lige har lagt fliser i. '
           'Analysefasen afgør derfor ikke bare, hvor ledningen skal ligge — den afgør, om '
           'projektet kan afsluttes, eller ender som en liste af ejendomme uden tilslutning.',
           after=48)

    m.para('I skriver det selv i jeres tekst om at få **i hvert sit rør** og give **mere plads til '
           'regnvandet**: "Alle disse forhold skal analyseres og beregnes, før vi kan lægge os '
           'fast på, hvordan separatkloakeringen konkret skal udføres." Den sætning skal stillingen '
           'indfri — og analysen skal svare på fire ting på én gang; et svar, der kun dækker tre, '
           'bliver først dyrt i anlægsfasen.', after=44)

    m.para('**Omfanget er et program, ikke et projekt.** Rudersdal har politisk besluttet at '
           'separatkloakere hele kommunen over 30 år, med ti områder frem til 2036 og Rudegård '
           'først, hvor anlægsarbejdet begynder i 2026. Gladsaxe er delt i 18 områder og løber frem '
           'til 2055, med Mørkhøj i gang. Alene i Rudersdal er syv områder under planlægning '
           'samtidig, hver med boringer, naturregistreringer, opmåling af brønde og TV-inspektioner. Den portefølje styres ikke af den, der har flest møder, '
           'men af den, der har defineret, hvad undersøgelserne skal svare på. Stillingen '
           'ligger i **spændingsfeltet mellem teknik, myndighedssamarbejde og borgerdialog**, og '
           'det er dér, analysen bliver afgjort.', after=52)

    m.para('**Analysens fire spørgsmål.**', after=40)

    m.para('**1. Hvor løber vandet hen i dag?** TV-inspektion og opmåling af brønde er ikke en '
           'formalitet; de er specifikationen af, hvad vi ved. Jeg har siddet på den anden side af '
           'den slags rapporter i fem år: et resultat uden skelnen mellem utæthed, forkert fald og '
           'ulovlig tilslutning kan ikke bruges til at vælge løsning — kun til en ny inspektion.',
           after=40)

    m.para('**2. Hvor kan regnvandet være?** Under jorden som bassin, på terræn som regnvandssø, i '
           'render og grøfter eller nedsivning i bede. Valget flytter anlægsøkonomien og '
           'driftsøkonomien i tredive år: et **regnvandsbassin** skal tømmes og have adgang, en '
           'regnvandssø skal slås og tåle at ligge midt i et villakvarter.', after=40)

    m.para('**3. Hvem skal sige ja?** Kommunen gennem spildevandsplanen, myndigheden gennem '
           'tilladelsen, grundejeren gennem sin egen tilslutning. Kører tilladelsen parallelt med '
           'projekteringen, koster en ændring et møde; kører den bagefter, koster den en '
           'entreprise. Jeg har lagt dokumentation til tilsyn og godkendelse i 37 projekter og '
           'ved, hvornår en ansøgning skal af sted.', after=40)

    m.para('**4. Hvad skal driften kunne om tredive år?** Det spørgsmål står sjældent i et '
           'projekteringsgrundlag, og det er det, der bliver dyrt: adgang for en sugeblis, en '
           'måler nogen kan kalibrere, reservedele der stadig findes. Fem år som driftsleder på et '
           'renseanlæg gør det til en vane, ikke til et punkt på en tjekliste.', after=40)

    m.para('**Projektledelse er ikke det, jeg skal lære i denne stilling.** 37 kapitalprojekter '
           'fra behov til aflevering med FAT/SAT og nul kritiske fund; 11 samtidige anlægsprojekter '
           'i 2022 med 14 medarbejdere og underentreprenører, hvor gravning, asfalt og adgang for '
           'beboerne skulle koordineres i én tidsplan; budgetter på 2–10 mio. kr. med månedlig '
           'opfølgning. **AB 18** og entreprisekontrakter har jeg arbejdet under som entreprenør — '
           'jeg har prøvet at få en ændring afvist, og det er den erfaring, jeg bruger, når jeg '
           'sidder på den anden side og vurderer, om et krav er rimeligt.', after=44)

    m.para('Mange af jeres projektledere kommer fra rådgiverbranchen, og I skriver selv, at de '
           'vælger Novafos for at **arbejde tættere på beslutningerne**, **følge projekterne hele '
           'vejen** og **se dine projekter blive til virkelighed**. Jeg kommer fra den anden ende: '
           'fem år i driften af et renseanlæg og siden 2023 egen virksomhed med service- og '
           'entrepriseopgaver. Det gør mig ikke til en bedre projekteringsleder, men jeg har set, '
           'hvad en beslutning i analysefasen koster, når anlægget er overdraget — og derfor '
           'spørger jeg til driften, mens tegningen stadig kan ændres. Hydrauliske beregninger og '
           '**GIS** er rådgivernes værktøjer; jeg læser dem som den, der skal overtage '
           'resultatet.', after=44)

    m.para('Hos jer kan man **følge projekterne hele vejen** og arbejde med **langsigtede '
           'løsninger fremfor kortsigtede leverancer** — og opgaven handler om **hvordan vi klimatilpasser vores kommuner**, ikke om at levere en '
           'tegning. At I er et **klimavenligt forsyningsselskab** med **bæredygtighed, '
           'klimasikring** og **værdi for både samfund og miljø** gør ikke opgaven lettere, men '
           'lettere at forsvare, når en grundejer spørger, hvorfor haven skal åbnes. Og med **plads '
           'til et liv ved siden af arbejdet**, **trivsel og samarbejde** og **et stærkt fagligt '
           'miljø**, hvor man **arbejder sammen på tværs af fagligheder** og **hjælper hinanden med '
           'at lykkes**, vil jeg hellere sidde i Birkerød end i et konsulenthus.', after=44)

    m.para('**Praktisk:** jeg bor i Måløv, 25 minutter fra Blokken 9, har kørekort og bil og kan '
           'være i alle ni kommuner inden for en time. Jeg kan starte efter aftale. Det, jeg gerne '
           'vil høre om, er, hvor langt de syv områder i Rudersdal er i analysen — og hvordan I '
           'afgør, hvornår en undersøgelse er god nok til at vælge løsning.', after=44)

    m.meta('Med venlig hilsen', after=15)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Projektleder med 20+ års erfaring fra tekniske anlæg i døgndrift — '
           '**elautoriseret maskinmester (LV/MV/HV)** med B.Tech i teknologiledelse og '
           'maskinteknik. Har ført **37 kapitalprojekter** fra behov til aflevering med FAT/SAT og '
           '**nul kritiske fund**, **11 samtidige anlægsprojekter** i byrum med 14 medarbejdere og '
           'underentreprenører, og var fem år drifts- og vedligeholdelsesleder på et '
           '**renseanlæg** med bassiner, **pumpestationer** og overløb. Arbejder under **AB 18** '
           'som entreprenør med **udbud**, **budget** og **økonomiopfølgning** som fast del af '
           'rollen.', after=70)

    m.section('LEDNINGSGRAVEN — ANALYSE, ANLÆG OG DRIFT')
    for label, body in [
        ('Anlæg i byrum',
         '11 samtidige anlægsprojekter i 2022 med 14 medarbejdere og underentreprenører: '
         'gravearbejde, asfalt, adgang for beboere og drift koordineret i én tidsplan.'),
        ('Afløbssystemet fra driftssiden',
         'Fem år som drifts- og vedligeholdelsesleder på Lynetten under Biofos: **kloak**, '
         'belastning, overløb, **bassiner**, **pumpestationer** og 24/7-drift; vandstands- og flowmålinger '
         'brugt til at prioritere mellem anlæg, 5S indført som standard.'),
        ('Fra analyse til overdragelse',
         '37 kapitalprojekter: behovsafdækning, løsningsvalg, kravspecifikation, udførelse, FAT/SAT '
         'og **overdragelse** til **drift** med dokumentation, en efterfølger kunne bruge.'),
        ('Udbud, kontrakter og entreprenører',
         '**Udbud** og **kontraktstyring** under **AB 18** i egne entrepriser; **rådgivere** og '
         '**entreprenører** styret på tid, pris og kvalitet — mængder og ændringer afklaret, før '
         'de blev en tvist.'),
        ('Økonomi, risici og fremdrift',
         '**Budgetter** på 2–10 mio. kr. pr. projekt og fuldt P&L siden 2023; **risici** og '
         '**fremdrift** rapporteret månedligt med afvigelsesforklaring til ledelse og bygherre.'),
        ('Myndigheder og dokumentation',
         '**Dokumentation** til tilsyn og godkendelse i 37 projekter under GMP/FDA/EMA; '
         '**tilladelser** og inspektioner lagt ind som milepæle i **tidsplanen**.')]:
        m.bullet(label, body, after=16)

    m.models_table('SYSTEMER OG METODER', ('Område', 'Dokumenteret brug'), [
        ('Analyse og undersøgelser',
         'Behovsafdækning og kravspecifikation i 37 projekter; defineret hvad en undersøgelse '
         'skulle svare på, før den blev bestilt.'),
        ('Anlæg og drift',
         'SRO/SCADA, pumper, bassiner og pumpestationer i 5 års døgndrift; 5S og standard work; '
         'over 40 % lavere energiforbrug gennem måling og indregulering.'),
        ('Kontrakt og økonomi',
         'AB 18, entreprisekontrakter og ændringshåndtering; budget og betalingsopfølgning i egen '
         'virksomhed siden 2023.'),
        ('Parter og myndigheder',
         'Kommuner, myndigheder, rådgivere og entreprenører i 37 projekter; møder og '
         'korrespondance arkiveret med navn og dato.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · elautorisation · service- og entrepriseydelser',
         [('Projekt, kontrakt og økonomi',
           'Tilbud, udbud og ændringshåndtering; budget og **økonomiopfølgning**; kunder, '
           'rådgivere og entreprenører i daglig koordinering.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('Krav, udførelse og aflevering',
           'Kravspecifikation, FAT/SAT og idriftsættelse; afvigelser lukket med navn og dato; nul '
           'kritiske fund ved aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter',
         [('Fremdrift i et tæt program',
           'Dagligt tavlemøde, kapacitetsanalyse og omprioritering samme dag; 11 samtidige '
           'anlægsprojekter koordineret med underentreprenører og bygherre.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Lynetten under Biofos · København · aug. 2017–jan. 2022',
         'Renseanlæg i 24/7-drift · SRO · belastning, overløb, bassiner, pumpestationer',
         [('Drift, måling og energi',
           'Belastning og overløb fulgt i døgndrift; vandstands- og flowmålinger brugt til '
           'prioritering mellem anlæg; energiledelse med over 40 % lavere forbrug; 12 teknikere og '
           '3 lærlinge oplært i standarder, de kunne arbejde efter.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 teknikere · maskinværksted · industrielt udstyr',
         [('Teknisk service og fejlfinding',
           'Fejlfinding, kalibrering og reparation på industrielt udstyr; oplæring og opfølgning '
           'på mål for 12 teknikere.')]),
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

    m.section('SPROG, PRAKTIK OG REFERENCER')
    m.para('Dansk: modersmål · Engelsk: professionelt, også teknisk · Persisk: modersmål · '
           '**Kørekort B og egen bil** · Måløv, 25 minutter fra Birkerød · Kan starte efter aftale '
           '· Referencer på forespørgsel.', after=60)

    m.models_table('OPSLAGETS KRAV — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Projektledelse fra idé- og analysefase frem mod projektering',
         '**Analysefase** og **projektering** drevet i 37 kapitalprojekter fra behovsafdækning og '
         'løsningsvalg til kravspecifikation; i 11 samtidige anlægsprojekter blev undersøgelserne '
         'bestilt, før tidsplanen blev lagt.'),
        ('Planlægning og udvikling af løsninger for ledningssystemer, pumpestationer og bassiner',
         '**Ledningssystemer**, **pumpestationer** og **bassiner** kendt fra 5 års drift; løsningsvalg '
         'udviklet med driften i 37 projekter, hvor adgang blev afgjort før projekteringen.'),
        ('Tæt dialog og koordinering med kommuner, myndigheder og rådgivere',
         '**Kommuner**, **myndigheder** og **rådgivere** koordineret gennem 20+ år; tilsynet var '
         'part i tidsplanen i 37 projekter, og rådgiver og entreprenør sad i samme fremdriftsmøde.'),
        ('Styring af økonomi, risici og fremdrift',
         '**Økonomi**, **risici** og **fremdrift** rapporteret månedligt i 37 projekter med '
         '**budget** på 2–10 mio. kr.; risikoliste ført fra krav til aflevering.'),
        ('Myndighedsprocesser og sikring af nødvendige tilladelser',
         '**Tilladelser** og godkendelser planlagt som milepæle i 37 projekter under GMP/FDA/EMA — '
         '0 kritiske fund ved aflevering, fordi ansøgningen var sendt, før den blev kritisk.'),
        ('Borgerdialog og håndtering af interessenter',
         '**Borgerdialog** i den form, hvor arbejdet foregår i nogens hjem: 3 år med egen '
         'virksomhed og kundemøder, hvor en ekstra dag skulle forklares; **interessenter** kortlagt '
         'i 37 projekter med ejer og dato.'),
        ('Sparring med programleder og øvrige projektledere',
         '**Programledelse** tæt på i 11 samtidige anlægsprojekter med fælles tavlemøde; sparring '
         'om løsningsvalg med 25 specialister i 37 projekter og med 8 medarbejdere i egen '
         'virksomhed.'),
        ('Drive projekter sikkert fremad',
         '37 kapitalprojekter afleveret med nul kritiske fund og 11 samtidige anlægsprojekter uden '
         'standsning af drift; sikkerhed og adgang for beboere aftalt, før gravemaskinen kom.'),
        ('Bidrage med teknisk indsigt i løsninger inden for spildevand og klimatilpasning',
         '**Spildevand** kendt fra driftssiden i 5 år: belastning, overløb, bassiner, '
         'pumpestationer. **Klimatilpasning** som løsningsvalg — bassin, regnvandssø, render og '
         'grøfter — med driftsøkonomi for 30 år regnet ind.'),
        ('Ansvar for analysefasen af projekterne',
         '**Analysefasen** ejet i 37 projekter: hvad undersøgelsen skulle svare på blev skrevet '
         'først, og rapporter der ikke kunne bruges til at vælge løsning blev sendt tilbage.'),
        ('Arbejde i spændingsfeltet mellem teknik, myndighedssamarbejde og borgerdialog',
         '**Spændingsfeltet** prøvet i 37 projekter og egne entrepriser: teknik, '
         '**myndighedssamarbejde** og borgere i samme beslutning, med 3 parter hørt før mængderne '
         'blev låst.'),
        ('Direkte indflydelse på hvordan vi klimatilpasser vores kommuner',
         '**Klimatilpasning** og **klimasikring** som ramme i 11 anlægsprojekter og 5 års '
         'driftsansvar; over 40 % lavere energiforbrug er et resultat af netop de valg, der bliver '
         'siddende i anlægget.'),
        ('Forstå og udvikle de tekniske løsninger',
         'Løsninger udviklet med rådgiver og drift i 37 projekter: kravspecifikation, '
         'alternativvurdering og fravalg dokumenteret — 2–10 mio. kr. pr. projekt, hvor valget '
         'skulle forsvares økonomisk.'),
        ('Sikre fremdrift i en virkelighed med mange interessenter og krav',
         '**Fremdrift** holdt i 11 samtidige anlægsprojekter med 14 medarbejdere og '
         'underentreprenører; kapacitetsanalyse hver dag og omprioritering samme dag, når '
         'leverancen skred.'),
        ('Arbejde i tæt samspil med kommune, rådgivere og kolleger i Novafos',
         '**Kommune**, **rådgivere** og interne kolleger i samme model i 37 projekter; '
         'grænseflader aftalt skriftligt med navn og dato.'),
        ('Erfaring med projektledelse af anlægs- eller klimatilpasningsprojekter',
         '**Anlægsprojekter**: 11 samtidige i 2022 med 14 medarbejdere, gravning og asfalt; '
         '**projektledelse** i 20+ år og 37 kapitalprojekter fra krav til aflevering.'),
        ('Teknisk forståelse for afløbssystemer, hydraulik eller klimatilpasning',
         '**Afløbssystemer** fra driftssiden i 5 år og **klimatilpasning** som løsningsvalg i 11 '
         'anlægsprojekter; **hydraulik** er rådgiverens beregning — jeg læser den som den, der skal '
         'drive anlægget, og ved hvilke antagelser der bliver dyre.'),
        ('Erfaring med eller interesse for myndighedsarbejde og juridisk regulering',
         '**Myndighedsarbejde** i 37 projekter med tilsyn og godkendelse og **regulering** kendt fra '
         'GMP/FDA/EMA og AB 18; spildevandsplan og tilslutningspligt læses, før der tegnes.'),
        ('Evne til at navigere mellem teknik, økonomi, myndighedskrav og borgerhensyn',
         '**Teknik**, **økonomi**, **myndighedskrav** og **borgerhensyn** afvejet i 37 projekter og '
         'i egen virksomhed med 8 medarbejdere, hvor en forkert prioritering blev synlig i '
         'regnskabet samme kvartal.'),
        ('Stærke samarbejdsevner og lyst til at arbejde tværfagligt',
         '**Tværfagligt** samarbejde med 25 specialister i 37 projekter og driften på et renseanlæg '
         'med 12 teknikere; fælles tavlemøde hver dag i 11 samtidige anlægsprojekter.'),
        ('En struktureret tilgang og evne til at skabe fremdrift i komplekse projekter',
         'Fast rækkefølge i alle projekter: behov, undersøgelse, løsningsvalg, mængder, udbud, '
         'udførelse, aflevering — brugt i 37 projekter, hvor de 11 kørte parallelt i 2022 uden at '
         'standse hinanden.'),
        ('Kombinere projektledelse med teknisk forståelse',
         '**Projektledelse** på 20+ år og teknik prøvet med hænderne: SRO, pumper, bassiner og '
         'pumpestationer i 5 års døgndrift; 37 projekter med både budgetansvar og teknisk '
         'aflevering.'),
        ('Erfaring fra rådgiver- eller forsyningsbranchen',
         '**Forsyningsbranchen**: 5 år på et renseanlæg under Biofos med 24/7-drift, spildevand og '
         'overløb, og siden 2023 entreprenørvirksomhed med service og anlæg; rådgiverrollen er den, '
         'jeg sidder over for, ikke den, jeg kommer fra.')])

    m.models_table('HVIS ANALYSEN IKKE SVARER — HVAD DER SKER, OG HVAD DER FANGER DET',
                   ('Det, der går galt', 'Det, analysen skulle have svaret på'), [
        ('Grundejerne tilslutter ikke',
         'Analysen svarede på ledningen, ikke på grunden: hvem der graver, hvornår kloakmesteren '
         'kan komme, og hvad det koster for de **grundejere**, der skal tilslutte. Fanges af en '
         'tilslutningsplan pr. ejendom, ejet af projektlederen.'),
        ('Anlægget bliver dyrere end budgetteret',
         'Boringer, jordbund og trafik var ikke undersøgt, før mængderne blev sat. Fanges af, at '
         'undersøgelserne har egne milepæle og eget budget i analysefasen.'),
        ('Bassinet ligger rigtigt og kan ikke driftes',
         'Placeringen blev valgt på hydraulik og areal, ikke på adgang for en sugeblis. Fanges af, '
         'at driften skriver under på løsningsvalget, før projekteringen starter.'),
        ('Tilladelsen kommer efter udbuddet',
         'Myndighedsprocessen blev planlagt som en fase i stedet for som en parallel proces. Fanges '
         'af, at tilladelser og høring står i tidsplanen med datoer.')])

    m.section('DE FØRSTE 90 DAGE')
    for b in (
        'Læst alle syv områder i Rudersdal igennem og lagt én oversigt: hvor langt er '
        'undersøgelserne, hvad mangler analysen at svare på, og hvad ligger i kritisk vej.',
        'Gået de to områder, der er længst fremme, igennem med rådgiveren — og skrevet ned, hvad '
        'rapporterne ikke svarede på.',
        'Siddet med driften om et af de bassiner, der er projekteret: hvordan tømmes det, hvem '
        'slår skråningen, og hvor står måleren om ti år.'):
        m.bullet('', b, after=16)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Novafos_Klimatilpasning.docx')
    build(out)
    print(out)
