# -*- coding: utf-8 -*-
"""Pharma Nord ApS — Teamleder til produktionen, Vojens.

Dansk opgave-først ansøgning + CV i ét dokument (masterdesign).
Kultur og fagligt indhold: master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md,
afsnittet om Pharma Nord (research 05.11.2026).
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Produktionsledelse · GMP, maskiner og nærværende ledelse på gulvet'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('5. november 2026')
    m.meta('Pharma Nord ApS · Produktionen, Tinglykke 4-6, 6500 Vojens · Driftslederen')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Teamleder til produktionen', bold=True, color='1A1A1A')
    m.para('Til driftslederen i Pharma Nord', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('En tabletproduktion bliver ikke styret fra et mødelokale. Den bliver styret af, hvad der står på tavlen '
           'klokken syv, hvem der står ved hvilken maskine, og om batchnummeret, kontroldokumenterne og rengøringen '
           'er i orden, når skiftet slutter. Hos jer er der op til 32 kontroldokumenter pr. fremstilling, og det er '
           'ikke bureaukrati — det er den eneste måde, kvaliteten kan dokumenteres bagefter. Teamlederens opgave er '
           'at gøre den standard gentagelig på hvert skift, også når to maskiner står stille og planen allerede er '
           'skredet.', after=80)

    m.para('**Den daglige rytme, jeg vil køre, er enkel nok til at holde i en travl uge.** Et tavlemøde på ti '
           'minutter ved skiftstart med fem tal: plan mod faktisk, kassation, nedetid pr. maskine, åbne afvigelser og '
           'dokumentfejl fundet ved batchgennemgang. En runde i produktionen hver morgen sammen med skiftets nøglefolk, '
           'fordi gulvet viser en blokeret maskine eller et manglende rengøringsskema, før rapporten gør. '
           'Batchdokumentation ført i nuet og ikke samlet sammen i sidste øjeblik. Afvigelser behandlet med A3 og '
           '5 x hvorfor, så det er årsagen der bliver rettet og ikke bare symbolet. Og en fast kadence med teknisk '
           'afdeling, hvor vi gennemgår de maskiner, der har drillet, med fejlkode, nedetid og hvad der blev gjort — '
           'så den samme fejl ikke kommer igen om tre uger.', after=80)

    m.para('Ressourceoptimering er for mig ikke et regneark, der bliver åbnet hver måned. Det er bemanding mod planen '
           'hver dag, omstillingstider der bliver målt og forkortet, flaskehalse der bliver flyttet frem for accepteret, '
           'og et fravær der bliver taget alvorligt, fordi det er kollegerne på holdet, der løber hurtigere. Planen kommer '
           'fra produktionsplanlægningen; min opgave er at gøre den gennemførlig og sige til i tide, når den ikke er. '
           'De tal, '
           'jeg vil måles på sammen med driftslederen, er planoverholdelse, nedetid og OEE på de kritiske maskiner, '
           'kassationsprocent, antal afvigelser og hvor længe de er åbne, samt dokumentfejl ved batchgennemgang. '
           'Det er de tal, der viser, om der er styr på produktionen — eller om der bare er travlt.', after=80)

    m.para('Jeg kommer med GMP fra medicinalindustrien, og det er ikke noget, jeg skal lære i rollen. Hos Novo Nordisk '
           'arbejdede jeg under GMP, FDA og EMA på 37 samtidige anlægsprojekter med 25 specialister: skrevne '
           'acceptkriterier, FAT/SAT og IQ/OQ/PQ, afvigelser med ejer og frist og nul kritiske fund ved aflevering. '
           'Jeg har også stået med drift og vedligehold på et 24/7-anlæg, hvor pumper, højspændingstavler og SCADA '
           'skulle køre hele døgnet, og hvor 5S, Standard Work og forebyggende vedligehold var det, der holdt '
           'nedetiden nede. Og jeg har haft personaleansvar i tre år: fem elektrikere og tre lærlinge med daglig '
           'planlægning, 1:1, MUS, kompetencematrix og oplæring — også når der var for mange opgaver til for få folk.',
           after=80)

    m.para('Jeg skal være tydelig om to ting. Den første: jeg har ikke stået i en teamlederrolle i '
           'produktion af kosttilskud og lægemidler før. Det, jeg har, er GMP-dokumentation, maskinkendskab, '
           'fejlfinding og personaleansvar fra sammenlignelige miljøer, og en arbejdsmåde der kan sættes i gang fra '
           'første uge. Den anden: jeg bor i Måløv, og Vojens er omkring tre timer væk. Det er en flytning og ikke '
           'en pendling, og det vil jeg hellere tage op i den første samtale end lade som om, afstanden ikke findes.',
           after=80)

    m.para('De første 90 dage har jeg lagt som en plan og ikke som en fortælling: uge 1–2 på gulvet på alle skift, '
           'hvor jeg følger en hel batch fra blanding til pakkeri og selv fører kontroldokumenterne; dag 30 med '
           'baseline på de fem tal og et overblik over, hvor planen bryder sammen; dag 60 med tavlemødet kørende, en '
           'fast kadence med teknisk afdeling og de første to forbedringer målt; dag 90 med kompetencematrix pr. '
           'medarbejder, en opdateret APV-gennemgang og en status til driftslederen på planoverholdelse, nedetid og '
           'kassation.', after=80)

    m.para('Det, der trækker mig mod Pharma Nord, er, at kvaliteten er noget, I kan dokumentere — over 300 '
           'videnskabelige studier, egen produktion fra bunden i Vojens og de skrappeste krav fra både GMP og HACCP. '
           'Det er en virksomhed, hvor produktionen ikke bare skal køre, men kunne tåle at blive gennemgået. Den slags '
           'miljøer har jeg arbejdet i hele mit voksne liv, og jeg trives med det: faste rammer, tydelige krav og '
           'plads til at gøre tingene bedre inden for rammerne.', after=80)

    m.para('Jeg er også professionel og aktiv Claude-koder og bruger Python og Claude til planlægning, KPI-opfølgning '
           'og små analyser — for eksempel at finde ud af, hvilken maskine der reelt koster mest nedetid, eller hvordan '
           'bemandingen passer til planen i næste uge. Det er ikke et system, jeg rører uden godkendelse; det er tid, '
           'der flytter fra regneark til gulv.', after=80)

    m.para('Jeg vil gerne komme til Vojens og gå gennem produktionen med jer — blanderummet, tabletpresse, '
           'kapselmaskine og pakkeri — og høre, hvor I mærker presset lige nu, og hvordan jeg kan aflaste driftslederen '
           'fra første uge.', after=80)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Produktions- og driftsleder med 20+ års erfaring fra GMP-reguleret produktion, teknisk drift og entreprise '
           '— personaleansvar, maskinansvar og ansvar for, at planen holder. Arbejder med GMP-dokumentation, afvigelser '
           'og CAPA som en del af den daglige rytme, ikke som et projekt ved siden af. Bruger SAP, KPI-tavler og egne '
           'AI-værktøjer (Python, Claude) til planlægning og opfølgning.', after=80)

    m.section('LEDELSE OG RESULTATER')
    for label, body in [
        ('Personaleansvar',
         'Fem elektrikere og tre lærlinge i tre år: daglig planlægning, 1:1 hver fjortende dag, MUS/GRUS, '
         'kompetencematrix, oplæring og arbejdsmiljøopfølgning — også når opgaverne var flere end folkene.'),
        ('GMP og kvalitet',
         '37 samtidige CAPEX-projekter under GMP/FDA/EMA med 25 specialister: skrevne acceptkriterier, FAT/SAT og '
         'IQ/OQ/PQ, afvigelseshåndtering med ejer og frist, nul kritiske fund ved aflevering.'),
        ('Maskiner og nedetid',
         'Drift og vedligehold på et 24/7-anlæg med pumper, HVAC, højspændingstavler og SCADA: forebyggende '
         'vedligehold, akut fejlfinding og reservedelsflow — 5S og Standard Work på værksted og lager.'),
        ('Plan og fremdrift',
         '11 parallelle anlægsprojekter og et 14-mands team hos Ventek-Air med daglige tavlemøder og '
         'flaskehalsanalyser, der gav et markant løft i leveringsevnen.'),
        ('Forbedring og data',
         'PDCA-program reducerede energiomkostningerne med 40 %. A3 og 5 x hvorfor som fast metode i fejlfinding. '
         'Egne Python/Claude-værktøjer har givet over 40 % produktivitetsløft i egen virksomhed. Bygger '
         'investeringsmodeller med NPV, IRR og scenarier, når et nyt udstyr eller en ny linje skal vurderes.')]:
        m.bullet(label, body, after=30)

    m.models_table('VÆRKTØJER OG METODER', ('Opgave', 'Værktøj og dokumenteret anvendelse'), [
        ('Daglig styring',
         'Tavlemøde ved skiftstart med fem tal (plan, kassation, nedetid, åbne afvigelser, dokumentfejl), Gemba-runde '
         'i produktionen og struktureret overdragelse mellem skift. Brugt på 24/7-anlæg og i entreprise.'),
        ('Personaleledelse',
         'Situationsbestemt ledelse (SLII), delegeringstrappen, 1:1 hver fjortende dag, MUS/GRUS, SBI-feedback og '
         'GROW; kompetencematrix og udviklingsplan pr. medarbejder. Lærlinge ført til svendeprøve.'),
        ('Kvalitet og GMP',
         'Batchdokumentation og kontroldokumenter, afvigelser med rodårsag (A3, 5 x hvorfor, Ishikawa), CAPA med '
         'effektkontrol, ændringskontrol og auditparathed. FAT/SAT og IQ/OQ/PQ ved idriftsættelse.'),
        ('Maskiner og fejlfinding',
         'Fejlkode, nedetidsregistrering og MTBF/MTTR som styringstal; forebyggende vedligehold planlagt fra '
         'driftsdata; samarbejde med teknisk afdeling og leverandører om udbedring og reservedele.'),
        ('Ressourceoptimering',
         'Bemanding mod produktionsplan, fraværsopfølgning, omstillingstider (SMED-principper), flaskehalsanalyse og '
         'kapacitetsberegning for næste uge.'),
        ('Sikkerhed og arbejdsmiljø',
         'APV, LOTO, risikovurdering ved opstart, nærved-hændelser og sikkerhedsrunder; afvigelser lukket med ejer og '
         'frist. Brugt i produktion, på anlæg og i entreprise.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L-ansvar · erhvervs- og industrikunder',
         [('Personale og planlægning', 'Daglig planlægning, 1:1 og MUS, kompetencematrix, oplæring og '
                                       'arbejdsmiljøopfølgning på skiftende opgaver.'),
          ('Teknisk ansvar', 'Fejlfinding, tavler og styring, dokumentation og aflevering; leverandør- og '
                             'kundedialog om løsningsvalg og tid.'),
          ('Digitale værktøjer', 'Python/Claude API til tidsplaner, tjeklister og KPI-dashboard; over 40 % '
                                 'produktivitetsløft i virksomheden.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024',
         '37 samtidige CAPEX-projekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('GMP og dokumentation', 'Acceptkriterier, test og kvalificering, afvigelser med ejer og frist samt '
                                   'dokumenteret overdragelse — nul kritiske fund ved aflevering.'),
          ('Fremdrift og tværfagligt samarbejde', 'Fremdrift, økonomi, risici og ressourcer mellem engineering, '
                                                 'indkøb og anlæg; A3 og 5 x hvorfor i fejlfinding; PDCA-program '
                                                 'reducerede energiomkostningerne med 40 %.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter · DKK 2–10 mio. pr. projekt',
         [('Leverance og arbejdsgange', 'Daglige tavlemøder, flaskehalsanalyser og standardiserede arbejdsgange gav '
                                        'et markant løft i leveringsevnen; udbud, tilbud og underentreprenører.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos, Lynetten · København · aug. 2017–jan. 2022',
         '24/7-drift · pumper, HVAC, højspændingstavler og SCADA · skiftehold',
         [('Drift og nedetid', 'Forebyggende vedligehold, akut fejlfinding og reservedelsflow på SCADA-data; 5S, '
                               'Standard Work og PDCA på værksted og lager.'),
          ('Sikkerhed', 'LOTO, APV, risikovurdering og nærved-hændelser i skifteholdsdrift.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted',
         [('Maskiner og mål', 'Vagtplanlægning, materialestyring og målopfølgning; fejldiagnose, rodårsagsanalyse og '
                              'korrigerende handlinger på industrielt el- og mekanisk udstyr.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        m.doc.paragraphs[-1].runs[0].text = 'Omfang: '
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('UDDANNELSE OG AUTORISATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering — maskinmesterretningen',
          'Maskinmesterskolen København · 2017–2022 · EQF 6 · GPA 7,6/12')
    m.edu('Elautoriseret maskinmester (LV/MV/HV), stærkstrøm', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('El- og maskinteknisk design, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Lean og forbedringspraksis: 5S, PDCA, VSM, A3, Kaizen', 'Løbende kurser og daglig anvendelse i drift og projekter')
    m.edu('Køleteknik og klimaanlæg · STCW-sikkerhed og maskinrumsvagt',
          'Mercantec 2021 · Søfartsstyrelsen 2021–2023')

    m.section('SPROG, PRAKTISK OG REFERENCER')
    m.para('Dansk og persisk/farsi: modersmål · Engelsk: professionelt i skrift og tale · Kørekort B · Bopæl i Måløv. '
           'Vojens er ca. tre timer herfra, så stillingen forudsætter en flytning, og det vil jeg gerne drøfte åbent i '
           'første samtale. Fleksibel omkring skift og weekender, som jeg kender fra 24/7-drift. Referencer fra Novo '
           'Nordisk og Biofos oplyses efter aftale.', after=70)

    m.models_table('KRAV I OPSLAGET — MIN DOKUMENTATION', ('Krav', 'Dokumentation'), [
        ('Solid teknisk forståelse af produktionsudstyr og processer',
         '15 år med maskiner og anlæg: fejlfinding på pumper, tavler, styring og SCADA; FAT/SAT og idriftsættelse; '
         'elautoriseret maskinmester (LV/MV/HV).'),
        ('Erfaring med ressourceoptimering',
         'Bemanding mod plan og fraværsopfølgning i egen virksomhed; flaskehalsanalyser og kapacitetsstyring i '
         'entreprise; 40 % lavere energiomkostning via PDCA.'),
        ('Overblik og planlægning i en travl og foranderlig hverdag',
         '37 samtidige projekter med skiftende prioriteringer og 11 parallelle anlægsprojekter; daglig tavle og '
         'eskalering ved undtagelse.'),
        ('Synlig i produktionen med nærværende ledelse',
         'Gemba hver morgen, tavlemøde ved skiftstart og 1:1 hver fjortende dag. Ledelse på gulvet, ikke fra '
         'kontoret — også i skifteholdsdrift.'),
        ('Motivation og trivsel gennem samarbejde',
         'Kompetencematrix, oplæring af lærlinge til svendeprøve, SBI-feedback og MUS/GRUS; medarbejdere der bliver '
         'og bliver dygtigere.'),
        ('Kendskab til GMP og kvalitetskrav',
         'To år under GMP/FDA/EMA hos Novo Nordisk med afvigelser, CAPA og kvalificering; nul kritiske fund ved '
         'aflevering. HACCP-krav fra fødevareindustrien kommer oveni som en del af samme dokumentationsdisciplin.'),
        ('Koordinering med andre afdelinger',
         'Daglig koordinering mellem produktion, teknisk afdeling, indkøb og kvalitet; RACI, beslutningslog og '
         'eskaleringstrappe.'),
        ('Sikkerhed og arbejdsmiljø',
         'APV, LOTO, risikovurdering og nærved-hændelser i daglig drift; sikkerhedsrunder og afvigelser lukket med '
         'ejer og frist.')])
    m.page_break()

    m.models_table('FØRSTE 90 DAGE — GULV, TAL OG TEAM', ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'På gulvet på alle skift: følg en hel batch fra blanding over tabletpresning eller kapselfyldning til '
         'pakkeri, og før selv kontroldokumenterne. Mød hver medarbejder til en kort 1:1 og teknisk afdeling til en '
         'gennemgang af de maskiner, der driller mest.'),
        ('Dag 30',
         'Baseline på de fem tal: plan mod faktisk, kassation, nedetid pr. maskine, åbne afvigelser og dokumentfejl. '
         'Overblik over, hvor planen typisk bryder sammen — maskine, materiale, bemanding eller dokumentation — '
         'fremlagt for driftslederen.'),
        ('Dag 60',
         'Tavlemødet kører hver dag uden mig som ordstyrer. Fast kadence med teknisk afdeling om nedetid og '
         'forebyggende vedligehold. De første to forbedringer gennemført og målt, fx omstillingstid eller '
         'rengøringsflow.'),
        ('Dag 90',
         'Kompetencematrix pr. medarbejder med plan for, hvem der kan hvad på hvilke maskiner. APV-gennemgang opdateret '
         'med afdelingen. Status til driftslederen på planoverholdelse, nedetid og kassation — og en liste over, hvad '
         'der stadig mangler.')])

    m.section('SÅDAN STYRES ET SKIFT')
    m.para('Et skift bliver ikke godt af, at teamlederen er den dygtigste på maskinen. Det bliver godt, hvis alle ved, '
           'hvad der skal køre, hvem der har ansvaret for hvilken maskine, og hvad man gør, når noget stopper. Derfor '
           'starter hvert produktionsskift med ti minutter ved tavlen: planen, de fem tal, én ting vi skal være særligt opmærksomme '
           'på, og én ting vi gør anderledes end i går. Undervejs går jeg rundt — ikke for at kontrollere, men for at '
           'fange problemet, mens det stadig er lille. Og når skiftet slutter, er der en overdragelse, hvor den næste '
           'holdleder ved, hvad der er i gang, hvad der er halvfærdigt, og hvad der venter på teknisk afdeling.',
           after=80)

    m.section('GMP OG DOKUMENTATION — FØRST GANG, HVER GANG')
    m.para('I en GMP-produktion er dokumentation ikke noget, der bliver skrevet bagefter. Det er en del af arbejdet, og '
           'hvis den kommer i anden række, ender man med afvigelser, der kunne have været undgået, og batches der '
           'skal vurderes igen. Jeg vil have kontroldokumenterne ført, mens processen kører, rengøringsskemaerne '
           'underskrevet af den, der gjorde arbejdet, og enhver afvigelse rejst med det samme — også de små, fordi det er '
           'dem, der bliver et mønster. Ved batchgennemgang kigger vi efter fejl som et læringspunkt i tavlemødet, '
           'ikke som en skyldssag.', after=80)

    m.section('FEJLFINDING SAMMEN MED TEKNISK AFDELING')
    m.para('Nedetid på en tabletpresse eller en kapselmaskine bliver dyr, når den først er blevet vanlig. Derfor vil jeg '
           'arbejde med nedetid som et tal pr. maskine og en kort beskrivelse af, hvad der gik i styk, hvad der blev '
           'gjort, og hvad der bør ændres — og gennemgå det med teknisk afdeling i en fast kadence, så vi flytter os '
           'fra at reparere til at forebygge. Jeg har selv stået med fejlfinding i mange år: A3 og 5 x hvorfor, når '
           'det er en gentagelse, og enkle forsøg, når det er nyt. Det, jeg ikke selv kan løse, skal videre til '
           'tekniske folk med en ordentlig beskrivelse — ikke med \"den driller igen\".', after=80)

    m.section('SIKKERHED OG ARBEJDSMILJØ I EN TRAVL HVERDAG')
    m.para('APV er ikke et dokument, der skal ligge i en mappe. Det er en samtale om, hvor det gør ondt at arbejde, og '
           'hvad vi gør ved det. Jeg tager sikkerhedsrunden med i den daglige runde, følger op på nærved-hændelser '
           'inden for en uge, og sørger for at LOTO og risikovurdering er på plads, når der skal arbejdes på en '
           'maskine — også når produktionen har travlt. Det er præcis der, det bliver farligt.', after=80)

    m.section('RESSOURCEOPTIMERING UDEN AT SLIDE FOLK OP')
    m.para('Optimering betyder ikke, at de samme mennesker skal løbe hurtigere. Det betyder, at vi fjerner det, der '
           'stjæler tid: unødige omstillinger, ventetid på materialer, maskiner der ikke er rengjort, når næste batch '
           'skal køre, og dokumenter der skal findes frem to gange. Jeg måler omstillingstider, ser på bemandingen mod '
           'planen og flytter folk derhen, hvor flaskehalsen er — inden for hvert produktionsafsnit og på tværs — og når vi '
           'har '
           'fået noget til at gå hurtigere, '
           'holder vi fast i det med en standard, så det ikke glider tilbage.', after=80)

    m.section('DIGITALT ARBEJDE MED ET KLART FORMÅL')
    m.para('Jeg bruger Python og Claude til de opgaver, der ellers spiser en formiddag: trække nedetid ud pr. maskine, '
           'sammenligne plan og faktisk forbrug, lave en enkel oversigt til tavlen. Det giver teamlederen tid i '
           'produktionen i stedet for ved skærmen — og det sker inden for jeres systemer og godkendelser, som det skal.',
           after=80)

    return m.save(path, title='Ansøgning og CV — Teamleder til produktionen, Pharma Nord',
                  subject='Produktionsledelse med GMP, maskinansvar og nærværende ledelse',
                  keywords='teamleder, produktion, GMP, ressourceoptimering, maskiner, sikkerhed')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_PharmaNord_TeamlederProduktion.docx')))
