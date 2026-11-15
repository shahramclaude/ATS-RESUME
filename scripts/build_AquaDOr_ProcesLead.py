# -*- coding: utf-8 -*-
"""Aqua d'Or / Danone — Proces Lead, Brande.

Dansk leverance (opslaget er dansk). Ét samlet dokument: brev side 1, CV side 2-3,
krav-dokumentation og 90 dage + afsnit side 4.
Policy: master/README.md — ekstrem sikkerhed, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Proces Lead · Processer, SOP\'er og kvalitet på linjen'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('5. november 2026')
    m.meta('Aqua d\'Or Mineral Water A/S (Danone) · Brande · Proces Lead, DAN-IWS')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Proces Lead hos Aqua d\'Or / Danone', bold=True, color='1A1A1A')
    m.para('Til IWS & Operations Department Manager Martin Mayland Martinsen', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('En produktionslinje kører ikke på instrukser alene. Den kører på det øjeblik, hvor operatøren '
           'træffer den samme beslutning som i går — og på at nogen opdager det, når hun ikke gør. Det er den '
           'slags arbejde, jeg søger hos Aqua d\'Or: ikke at skrive endnu et dokument om, hvordan linjen burde '
           'køre, men at gøre den ens, målbar og bedre, hold efter hold. **DAN-IWS** er præcis den tilgang, jeg '
           'har arbejdet efter hele mit lederliv i teknisk drift: standarder først, tabene synlige, og '
           'forbedringerne ejet af dem, der står ved linjen.', after=80)

    m.para('**Jeg vil løfte rollen som Proces Lead på fire faste ting.** Først **SOP\'en som arbejdsinstruks**: '
           'skrevet sammen med dem, der udfører den, ét skridt og én beslutning ad gangen, med de billeder og '
           'grænseværdier der skal til — også når den læses klokken tre om natten af en vikar. Dernæst '
           '**træning og coaching, der måles på linjen og ikke i et skema**: jeg følger op ved maskinen, ser om '
           'skridtene faktisk bliver gjort, retter i nuet og lader de erfarne operatører undervise de nye. Så '
           '**afvigelser behandlet som data, ikke som skyld**: hver kvalitetsafvigelse skal have en rodårsag, en '
           'handling og en dato, og den skal kunne tåle at blive læst af den næste, der får samme problem. Og '
           'endelig **procesparametre ændret én ad gangen**: før og efter dokumenteret, med operatørteamet som '
           'dem, der ved, hvad der reelt sker ved linjen, og med et tal der viser, om det virkede.', after=80)

    m.para('Kvalitets- og dokumentationssiden er min hverdag. Hos **Novo Nordisk** har jeg arbejdet i et '
           'GMP-miljø, hvor en proces ikke er godkendt, fordi den kører, men fordi den kan dokumenteres: '
           '**SOP\'er, ændringsstyring, afvigelser, CAPA og rodårsagsanalyse**, kvalificering med IQ/OQ/PQ og '
           'FAT/SAT, og auditeret aflevering. Jeg har løftet **37 parallelle kapitalprojekter** med 25 '
           'specialister og 2–10 mio. kr. pr. projekt og leveret med **nul kritiske fund** — og lært, at den '
           'bedste dokumentation er den, der bliver skrevet, mens arbejdet foregår, ikke den, der bliver '
           'rekonstrueret bagefter.', after=80)

    m.para('Processiden har jeg fra et anlæg, der aldrig måtte stoppe. I fem år var jeg **drifts- og '
           'vedligeholdelsesleder på Lynetten under Biofos**, et af landets største spildevandsanlæg i '
           '**24/7-drift**: operatører i skift, processer med tryk, flow, temperatur og kemikaliedosering, '
           'målinger og **SCADA** i sanntid, og et anlæg hvor en ændret indstilling kunne mærkes på '
           'driftsresultatet samme dag. Jeg har ført tal og parametre tilbage til dem, der stod ved anlægget, '
           'og jeg har gennemført energiledelse med **over 40 % lavere energiforbrug** som dokumenteret '
           'resultat — ikke fordi nogen bad om en rapport, men fordi vi fandt ud af, hvor energien gik hen, og '
           'ændrede arbejdsmåden.', after=80)

    m.para('At arbejde i en **Trio** er en arbejdsform, jeg kender. En linje har brug for, at Line Lead, '
           'Maintenance Lead og Proces Lead trækker i samme retning og taler om de samme tal: hvad stopper os, '
           'hvad koster det, hvad gør vi ved det, og hvem gør det. Jeg har kørt tavlemøder, flaskehalsanalyser '
           'og daglige prioriteringer med både produktion og vedligehold — og jeg ved, at processtabilitet '
           'ikke ejes af et system, men af den aftale, de tre ledere har med hinanden om morgenen.', after=80)

    m.para('Danones **\"One Planet One Health\"** og B-Corp-certificeringen er ikke pynt for mig, og som '
           'fødevarevirksomhed har I et kvalitetskrav, der ikke kan forhandles. Vand er et '
           'produkt, hvor kvalitet og ressourceforbrug hænger sammen i samme proces: et tabt produkt er også '
           'et spildt vand- og energiregnskab, og en stabil linje er den billigste form for bæredygtighed, '
           'fordi den laver færre fejl, mindre omarbejde og mindre spild. Det er den slags forbedring, der '
           'holder, når den ikke kræver, at nogen husker den.', after=80)

    m.para('Mineralvand er et produkt, hvor råvaren er grundvand og processen er tapperiet: vandkvalitet og '
           'behandling, CIP og hygiejne, tryk og flow, fyldhøjde, lukning og mærkning — og en linje, hvor hvert '
           'af de led skal gøres ens hver gang, ellers er det ikke kvalitet men held. Det er den slags proces, '
           'jeg kender fra drift, hvor parametre, prøver og hygiejne er daglige krav og ikke kampagner.', after=80)

    m.para('Jeg har også selv stået med ansvaret for at lære folk op. I **ELOHVAC**, som jeg har drevet siden '
           '2023, har jeg tre lærlinge, og jeg har lavet den oplæring, de arbejder efter — det er samme '
           'disciplin som en SOP: vis det, lad dem gøre det, se efter, og ret før det bliver en vane. Som '
           '**projekt- og værkstedsleder i Ventek-Air** for 14 medarbejdere og 11 samtidige opgaver har jeg '
           'haft travlt med at holde kvaliteten, når tiden var knap — og det er netop der, standarden bliver '
           'afgørende.', after=80)

    m.para('Praktisk: jeg bor i Måløv, og Brande er omkring to en halv time væk. Jeg indretter mig med fast '
           'tilstedeværelse på fabrikken i arbejdsugens dage og hjem i weekenderne, kører selv og har '
           '**kørekort B**. Jeg taler og skriver dansk og engelsk uden problemer, og mine **IT-kompetencer** '
           'er ikke kun kontorprogrammer: jeg arbejder i **SAP** og **Excel** hver dag og bruger **Python** til '
           'at trække, rense og sammenligne produktions- og energidata, når der skal findes en rodårsag. Kan '
           'starte efter aftale. Jeg vil gerne høre, hvilke linjer I ruller DAN-IWS ud på først — så ved jeg, '
           'hvor jeg skal begynde, og hvad der skal måles på i uge et.', after=70)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Proces- og driftsleder med 20+ års erfaring fra teknisk drift, farmaceutisk '
           'produktion og entreprise — elautoriseret maskinmester med B.Tech i Technology Management & '
           'Mechanical Engineering. Har arbejdet i GMP-miljø med SOP\'er, ændringsstyring, afvigelser, CAPA og '
           'rodårsagsanalyse i 37 kapitalprojekter med nul kritiske fund, drevet 24/7-procesanlæg på '
           'SCADA-data med over 40 % lavere energiforbrug som dokumenteret resultat, og oplært operatører og '
           'teknikere i standardiserede arbejdsprocesser. Arbejder struktureret og systematisk, data-drevet og tæt på '
           'dem, '
           'der udfører arbejdet.', after=80)

    m.section('PROCES, KVALITET OG STANDARDER')
    for label, body in [
        ('SOP og standardiserede arbejdsprocesser',
         'Arbejdsinstrukser skrevet med dem, der udfører arbejdet: skridt, grænseværdier, billeder og '
         'acceptkriterier; versioneret, tilgængelig ved linjen og opdateret, når processen ændrer sig.'),
        ('Kvalitet og afvigelser',
         'Kvalitetsafvigelser analyseret til rodårsag med korrigerende og forebyggende handlinger, lukket med '
         'dato og ejer; afvigelser og hændelser brugt som læring frem for skyldfordeling.'),
        ('Træning og coaching af operatører',
         'Oplæring efter standarden — vis, gør sammen, se efter — og opfølgning ved maskinen, så træning bliver '
         'målt på adfærd og ikke på deltagelse. Lærlinge- og oplæringsansvar i egen virksomhed siden 2023.'),
        ('Procesparametre og optimering',
         'Tryk, flow, temperatur, dosering og hastighed fulgt på målere og SCADA; ændringer gennemført én ad '
         'gangen med før- og eftermåling, dokumenteret og gjort til ny standard.'),
        ('Forbedringskultur og data',
         'Tab og flaskehalse synliggjort på tavlen og i data; forbedringer ejet af operatørteamet og fulgt op, '
         'til de holder — energiledelse med over 40 % reduktion som dokumenteret resultat.')]:
        m.bullet(label, body, after=25)

    m.models_table('VÆRKTØJER OG METODER', ('Opgave', 'Værktøj og dokumenteret brug'), [
        ('Kvalitet og dokumentation',
         'SOP\'er, ændringsstyring, afvigelser og CAPA, IQ/OQ/PQ, FAT/SAT og auditeret aflevering; dokumentation '
         'skrevet mens arbejdet foregår.'),
        ('Proces og data',
         'SCADA, målere og trenddata; målinger renset og sammenlignet i Excel og Python; forsøg med én variabel '
         'ad gangen og før/efter dokumenteret.'),
        ('Træning og standard',
         'Oplæringsplan pr. medarbejder, kompetencematrix, sidemandsoplæring og opfølgning ved maskinen; '
         'lærlingeansvar i egen virksomhed.'),
        ('Arbejdsmiljø og sikkerhed',
         'APV, arbejdstilladelser, LOTO og kemikalier; hændelsesundersøgelse med rodårsag og lukkede handlinger '
         'i 24/7-drift.'),
        ('IT og systemer',
         'SAP og Excel i daglig brug, Python til dataanalyse og opfølgning; Microsoft Dynamics 365 med sager, '
         'kontrakter og økonomi — samme opbygning som de ERP-systemer, jeg har indført og brugt.'),
        ('Drift og koordinering',
         'Tavlemøder, flaskehalsanalyse og daglig prioritering mellem produktion og vedligehold; skiftplanlægning '
         'og beredskab i 24/7-drift.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 håndværkere og 3 lærlinge · fuldt P&L · private og erhvervsmæssige kunder',
         [('Kvalitet og oplæring', 'Arbejdsprocesser og oplæring skrevet og gennemført med lærlingene; kvalitet '
                                   'fulgt på den enkelte sag, og kunden informeret samme dag noget ændrer sig.'),
          ('Økonomi og drift', 'Budget, tilbud og indkøb; tavler, drev og styringer specificeret, installeret og '
                               'testet før aflevering.')]),
        ('Senior commissioning engineer / projektleder, elsystemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Kvalificering og dokumentation', 'IQ/OQ/PQ, FAT/SAT, acceptkriterier og ændringsstyring; SOP\'er og '
                                             'afvigelser håndteret i et GMP-system med nul kritiske fund.'),
          ('Afvigelser og rodårsag', 'Afvigelser og hændelser undersøgt til rodårsag med korrigerende handlinger; '
                                     'grænseflader mod andre fag og leverandører styret til aftalt kvalitet.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige opgaver · 2–10 mio. kr. pr. projekt',
         [('Standard og kvalitet under pres', 'Daglige tavlemøder, flaskehalsanalyse og omprioritering uden at '
                                              'tabe kvalitet; leverancer kontrolleret mod acceptkriterier før '
                                              'afsendelse.'),
          ('Oplæring i praksis', 'Nye medarbejdere lært op ved maskinen af de erfarne, med arbejdsinstrukser '
                                 'skrevet i værkstedet og kvalitet kontrolleret på den enkelte opgave.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Lynetten under Biofos · København · aug. 2017–jan. 2022',
         'Procesanlæg i 24/7-drift · vand, slam, pumper, ventilation, højspænding og SCADA',
         [('Procesdrift og operatører', 'Skiftplanlægning og daglig ledelse af driftsmedarbejdere; procesparametre '
                                        'fulgt på målere og SCADA, og ændringer gennemført med dem, der stod ved '
                                        'anlægget.'),
          ('Kvalitet og myndighed', 'Prøver, grænseværdier og miljødokumentation overholdt; arbejdsmiljø og sikker '
                                    'drift i hverdagen i et anlæg, der ikke måtte stoppe.'),
          ('Energi og data', 'Energiledelse på store anlægsmasser med data fra målere og SCADA: over 40 % lavere '
                             'energiforbrug, dokumenteret og fastholdt.')]),
        ('Elektromekaniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · industrielt udstyr',
         [('Fejlretning og rodårsag', 'Vagtplanlægning og opfølgning på mål; fejlretning, rodårsagsanalyse og '
                                      'korrigerende handlinger på produktionsudstyr.')]),
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
    m.para('Dansk: modersmål · Engelsk: professionelt · Persisk: modersmål · Kørekort B · Bor i Måløv, Brande '
           'ca. to en halv time væk, fast tilstedeværelse på fabrikken i arbejdsugens dage · Kan starte efter '
           'aftale · SAP og Excel dagligt, Python til data · Referencer på forespørgsel.', after=70)

    m.models_table('DET EFTERSPØRGER DE — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Teknisk baggrund og procesforståelse',
         'Elautoriseret maskinmester med B.Tech i Technology Management & Mechanical Engineering. Opslaget '
         'nævner ingeniør, procesteknolog, procesoperatør eller mejerist — min vej er maskinmester med samme '
         'tekniske og procesmæssige fundament, og 20+ år i drift og produktion, heraf fem år som drifts- og '
         'vedligeholdelsesleder på et procesanlæg i 24/7-drift.'),
        ('Sikring af produktkvalitet på produktionslinjen',
         'Kvalitet fulgt mod acceptkriterier i GMP-produktion og i 37 kapitalprojekter med nul kritiske fund; '
         'prøver, grænseværdier og miljødokumentation overholdt i 24/7-drift.'),
        ('Udarbejdelse og vedligeholdelse af SOP\'er',
         'SOP\'er og arbejdsinstrukser skrevet, godkendt og versioneret i GMP-system; oplærings- og '
         'instruktionsmateriale skrevet for lærlinge og teknikere i egen virksomhed.'),
        ('Træning og coaching af operatører',
         'Daglig oplæring og coaching af driftsmedarbejdere og teknikere; kompetencematrix pr. medarbejder, '
         'sidemandsoplæring og opfølgning ved maskinen; tre lærlinge i eget ansvar siden 2023.'),
        ('Deltagelse i test og implementering af nye produkter',
         'FAT/SAT, IQ/OQ/PQ og idriftsættelse af nye anlæg og ændringer i 37 projekter; ændringer testet mod '
         'acceptkriterier, før de blev frigivet til drift.'),
        ('Analyse af kvalitetsafvigelser og identificering af root causes',
         'Afvigelser og hændelser undersøgt til rodårsag med korrigerende og forebyggende handlinger, lukket med '
         'ejer og dato; samme metode brugt på produktionsudstyr og i 24/7-drift.'),
        ('Optimering af procesparametre og driftsindstillinger',
         'Tryk, flow, temperatur, dosering og hastighed optimeret på målinger og SCADA-data med operatørteamet; '
         'energiledelse med over 40 % lavere energiforbrug som dokumenteret resultat.'),
        ('Bidrag til forbedringskultur og implementering af DAN-IWS',
         'Standarder, tavlemøder, flaskehalsanalyse og opfølgning brugt som daglig arbejdsform; forbedringer '
         'ejet af dem, der udfører arbejdet, og fastholdt efterfølgende.'),
        ('Gode IT-kompetencer',
         'SAP og Excel i daglig brug, Python til dataanalyse og opfølgning, SCADA og trenddata; Microsoft '
         'Dynamics 365 med sager, kontrakter og økonomi.'),
        ('Dansk og engelsk, struktureret og samarbejdsorienteret',
         'Dansk modersmål og engelsk professionelt i internationalt projektmiljø; struktureret arbejde '
         'dokumenteret i 37 projekter og i tværfagligt samarbejde mellem produktion, vedligehold og '
         'kvalitet.')])
    m.page_break()

    m.models_table('DE FØRSTE 90 DAGE — STANDARDEN, TALLENE OG TRIOEN', ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'På linjen med alle tre skift og med Trioen: hvilke SOP\'er findes, hvor bruges de, og hvor bliver de '
         'omgået i praksis. Kvalitetsdata og de sidste måneders afvigelser gennemgået linje for linje.'),
        ('Dag 30',
         'En liste over de processer, hvor standarden og virkeligheden ikke er den samme, prioriteret efter '
         'kvalitetsrisiko og tab. Oplæringsbehovet pr. skift lagt fast, og tavlemødet med Line Lead og '
         'Maintenance Lead kørende i fast rytme.'),
        ('Dag 60',
         'De vigtigste SOP\'er skrevet om sammen med operatørerne og taget i brug med træning; '
         'parametervindue og grænseværdier dokumenteret, og de første to forbedringer målt før og efter.'),
        ('Dag 90',
         'Et kvalitetsbillede, der kan læses af alle: afvigelser pr. linje, rodårsager, tid til lukning og '
         'effekt af de gennemførte ændringer. Standarderne holder, når Trioen ikke er på vagt, og mindst én '
         'forbedring er blevet ny standard.')])

    m.section('SOP\'EN SKAL KUNNE BRUGES KL. 03')
    m.para('En arbejdsinstruks, der kun giver mening for den, der skrev den, er ikke en standard — den er en '
           'hensigtserklæring. Derfor skriver jeg SOP\'er på gulvet, med dem der udfører arbejdet, og med de '
           'grænseværdier, billeder og beslutningspunkter, der skal til, når linjen kører om natten og den '
           'erfarne operatør har fri. Standarden skal være den nemmeste måde at gøre det rigtige på, ellers '
           'bliver den omgået — og så er det ikke operatøren, der er problemet.', after=80)

    m.section('TRÆNING SES PÅ LINJEN, IKKE I ET SKEMA')
    m.para('Et gennemført træningskursus beviser, at nogen har siddet i lokalet. Det beviser ikke, at skridtene '
           'bliver gjort. Jeg følger op ved maskinen efter oplæringen, ser arbejdet blive udført, retter i '
           'nuet og lader de erfarne operatører undervise de nye — for den viden, der sidder i hænderne, '
           'flytter sig ikke af sig selv. Videndeling er en del af oplæringen: det, et skift finder ud af, skal det '
           'næste skift ikke opdage igen. Og når jeg ser den samme fejl hos tre forskellige, er det ikke tre '
           'medarbejdere, der er problemet, men SOP\'en.', after=80)

    m.section('EN AFVIGELSE ER DATA, IKKE EN SKYLD')
    m.para('Når et produkt bliver kasseret, er den dyreste reaktion at finde ud af, hvem der havde vagten. Den '
           'rigtige reaktion er at finde ud af, hvad der ændrede sig: råvare, indstilling, rengøring, '
           'temperatur, holdskifte eller slid. Det kræver, at data er der, når spørgsmålet stilles, og at '
           'operatørerne tør melde fejlen, fordi de ved, at meldingen bliver brugt til at rette processen og '
           'ikke til at hænge nogen op. Det er den kultur, jeg vil bygge, og den er samtidig den eneste, der '
           'giver rigtige rodårsager.', after=80)

    m.section('PARAMETRE SKAL ÆNDRES ÉN AD GANGEN')
    m.para('En linje, hvor der skrues på fem indstillinger på én gang, kan ikke fortælle, hvad der virkede. Jeg '
           'ændrer én parameter, måler før og efter, skriver det ned og gør resultatet til ny standard, hvis '
           'det holder. Operatørteamet er med i den beslutning, fordi de kender maskinens lyde og mærkelige '
           'vaner bedre end nogen rapport — og fordi en ændring, de har været med til at beslutte, bliver '
           'overholdt. Det er også den hurtigste vej til at flytte et tabstal: de fleste tab forsvinder ikke ved at '
           'køre hurtigere, men ved at fjerne de stop og omkørsler, ingen havde tal på.', after=80)

    m.section('RÅVAREN ER VAND')
    m.para('Når råvaren er grundvand, er kvalitetsarbejdet ikke kun et spørgsmål om at måle det færdige produkt. '
           'Det er behandlingen, filtrene, CIP-cyklusserne, hygiejnen i tappezonen og de grænseværdier, der '
           'afgør, om vandet er i orden, før flasken er fyldt. Derfor skal de parametre være en del af '
           'standarden og af tavlen — ikke kun af laboratoriets journal. En afvigelse på vandkvalitet er dyrere '
           'end en afvigelse på en emballage, fordi den rammer hele produktionen og omdømmet på én gang.',
           after=80)

    m.section('TRIOEN ER ÉN LINJE')
    m.para('Line Lead, Maintenance Lead og Proces Lead har tre ansvarsområder og ét resultat. Derfor skal '
           'trioen tale om de samme tal hver morgen: hvad stoppede os, hvad kostede det i kvalitet og output, '
           'hvad gør vi ved det, og hvem har opgaven i morgen. Jeg bidrager med processtabilitet og kvalitet, '
           'men jeg ser det som en del af mit ansvar at gøre vedligehold og drift i stand til at lykkes — en '
           'linje, der går ned hver anden dag, kan ikke have en stabil proces, uanset hvor gode SOP\'erne er. Og når '
           'output og kvalitet trækker i hver sin retning en travl fredag, skal trioens svar være det samme som '
           'mandag: kvaliteten bestemmer, hvad der må sendes ud, og tempoet tilpasser sig — ikke omvendt.', after=80)

    m.section('FORBEDRINGER SKAL HOLDE EFTER FERIEN')
    m.para('Forbedringer, der kun holder, så længe den, der fandt på dem, er på arbejde, er ikke forbedringer — '
           'de er personafhængighed. Derfor skal hver forbedring ende i en standard, en oplæring og et tal, der '
           'bliver fulgt, ellers falder linjen tilbage i løbet af få uger. Danones udgangspunkt — at vejen til '
           'målet er lige så vigtig som resultatet, og at alle tager lederskab uanset rolle — passer præcis '
           'her: det er operatøren, der holder standarden, og det er min opgave at gøre det muligt for hende.',
           after=80)

    return m.save(path, title='Proces Lead — Aqua d\'Or / Danone, Brande',
                  subject='Processer, SOP\'er, kvalitet og procesoptimering på produktionslinjen',
                  keywords='proces lead, sop, standardiserede arbejdsprocesser, kvalitet, afvigelser, rodårsag, '
                           'træning, coaching, procesparametre, dan-iws, iws, fødevarer')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_AquaDOr_ProcesLead.docx')))
