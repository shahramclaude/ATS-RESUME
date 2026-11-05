# -*- coding: utf-8 -*-
"""WSP Danmark — Afdelingschef for Havne og Geoteknik (Høje-Taastrup / Esbjerg).

Dansk leverance (opslaget er dansk): opgavefokuseret motiveringsside + CV i ét dokument.
Kultur- og rolleintel: master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md, afsnit om WSP.
Policy: master/README.md — ekstrem sikkerhed, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Afdelingschef · Havne og Geoteknik · Ledelse, marked og projektleverancer'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('5. november 2026')
    m.meta('WSP Danmark · Transport & Infrastructure · Høje-Taastrup og Esbjerg')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Afdelingschef for Havne og Geoteknik', bold=True, color='1A1A1A')
    m.para('Til divisionen Transport & Infrastructure', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('Havne, marine konstruktioner, kystteknik og geoteknik er den slags anlæg, der skal stå i hundrede år i '
           'et miljø, der arbejder imod dem: vand, vind, salt, sætninger og en myndighed, der stiller krav om '
           'dokumentation. En afdeling, der leverer det, bliver ikke ledet på gode intentioner. Den bliver ledet på '
           'tre tal — kostcentrets resultat, pipelinens dækning og kapacitetens udnyttelse — og på én kultur, der gør, '
           'at de dygtige mennesker bliver. Det er den kombination, jeg søger hos WSP.', after=80)

    m.para('**Jeg vil lede afdelingen på fire faste ting.** Først kostcentret: et budget, der er bygget ned på '
           'projektniveau, en månedlig rytme hvor forecast, igangværende arbejde og tilbudsprocent bliver gennemgået '
           'med de samme tal hver gang, og en kapacitetsplan der viser, hvor mange timer der er solgt, og hvor mange '
           'der er tilbage at sælge. Dernæst markedet: en prioriteret kundeliste, en pipeline hvor hver mulighed har '
           'et navn, en værdi og en dato, og en go/no-go-disciplin i tilbudsarbejdet, så vi bruger kræfterne på de '
           'opgaver, vi kan vinde med overskud — inklusive rammeaftalerne, hvor den lange relation slås fast.', after=80)

    m.para('Så menneskerne, fordi afdelingen er sine ingeniører og specialister i Høje-Taastrup og Esbjerg. Én '
           'afdeling på to adresser skal have fælles standarder, fælles kvalitetsniveau og en bevidst udveksling, så '
           'viden ikke bliver liggende på den ene side af landet. Jeg vil rekruttere bredt, udvikle målrettet og '
           'holde på de erfarne ved at give dem ansvar for noget, der er større end deres eget projekt. Og endelig '
           'leverancerne: projektgennemgang på de rigtige milepæle, et risikoregister der bliver læst, overholdelse '
           'af standarder og myndighedskrav som en fast del af kvaliteten — og erfaringer, der ender i næste tilbud i '
           'stedet for i en skuffe. Det er også de fire ting, jeg vil måle mig selv på fra første måned: resultatet, '
           'pipelinen, kapaciteten og leverancerne — og jeg vil hellere fremlægge dem på én side hver måned end '
           'forklare dem bagefter.', after=80)

    m.para('Jeg har prøvet alle fire dele med ansvar for resultatet. I **ELOHVAC**, som jeg har drevet siden 2023, har '
           'jeg fuldt P&L med fem elektrikere og tre lærlinge: budget, tilbud, kalkuler, dækningsgrad, indkøb og '
           'kunder — og jeg har bygget virksomheden op med digitale værktøjer, der tog over 40 % af det administrative '
           'arbejde ud af tilbud og opfølgning. I **Ventek-Air** var jeg projekt- og værkstedsleder for 14 '
           'medarbejdere og 11 samtidige anlægsprojekter med tilbud, underleverandører og afleveringspakker. Hos '
           '**Novo Nordisk** løftede jeg 37 samtidige anlægsprojekter med 25 specialister og 2–10 mio. kr. pr. '
           'projekt under GMP, FDA og EMA — hvor en manglende underskrift stopper en frigivelse, og hvor '
           'interessenthåndtering er en del af leverancen, ikke et tillæg til den.', after=80)

    m.para('Infrastrukturdelen har jeg fra **Biofos, Lynetten**, hvor jeg i fem år var drifts- og '
           'vedligeholdelsesleder på et af landets største anlæg i kystnær og maritim kontekst: tungt teknisk udstyr, '
           'pumper, konstruktioner og installationer, 24/7-drift, myndighedskrav og miljødokumentation, og et anlæg '
           'der ikke måtte stoppe. Jeg har arbejdet med entreprenører, rådgivere, leverandører og myndighed i samme '
           'projekt, og jeg ved, hvad der sker med tid og økonomi, når en undersøgelse kommer for sent, eller når et '
           'myndighedskrav dukker op i detailfasen. Den geotekniske rapport og konstruktionstegningen læser jeg som '
           'en del af beslutningsgrundlaget — og stiller de spørgsmål, der skal stilles, før støbejernet går i jorden.', after=80)

    m.para('Fagligt er jeg uddannet **elautoriseret maskinmester** med B.Tech i Technology Management & Mechanical '
           'Engineering — en maritim ingeniøruddannelse i konstruktion, maskin og drift, suppleret med elautorisation '
           'på LV, MV og HV — og jeg har været på den anden side af bordet som både rådgiver, entreprenør og kunde. '
           'Det er en fordel i en afdeling, der både skal projektere, rådgive og bistå under udførelsen: jeg ved, '
           'hvordan et tilbud bliver læst, hvordan en bygherre tænker, og hvor i et projekt den dyre fejl plejer at '
           'ligge.', after=80)

    m.para('WSPs eget sprog rammer opgaven: **Future Ready** handler om at designe til fremtiden med klima, samfund, '
           'teknologi og ressourcer i beslutningen — og for havne og kyster er det ikke et program, men en '
           'forudsætning, fordi havvandstanden, klimaet og myndighedernes krav flytter sig hurtigere end '
           'anlæggenes levetid — og bæredygtige løsninger er ikke et tillæg til leverancen, men selve leverancen. At '
           'være en af WSPs **Visioneers** er at tage det ansvar, og det globale netværk inden for havne, '
           'marine og geoteknik er netop det aktiv, en afdelingschef skal kunne sætte i spil for kunderne i Danmark. '
           'Jeg vil gerne være den, der binder det sammen: dansk leverance, global faglighed, og en afdeling der '
           'bliver den foretrukne partner — ikke den billigste.', after=80)

    m.para('Praktisk: jeg bor i Måløv, ca. 20 minutter fra Høje-Taastrup, og er indstillet på den rejseaktivitet, to '
           'kontorer og Esbjerg kræver. Jeg taler dansk og persisk som modersmål og engelsk professionelt, og jeg '
           'arbejder i SAP og Excel dagligt samt med egne Python- og Claude-værktøjer til økonomi-, pipeline- og '
           'kapacitetsopfølgning. Jeg kan starte efter aftale.', after=70)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Ledelses- og projektingeniør med 20+ års erfaring fra rådgivning, entreprise og tung infrastruktur — '
           'elautoriseret maskinmester (LV/MV/HV) og B.Tech i Technology Management & Mechanical Engineering. Fuldt '
           'P&L med fem elektrikere og tre lærlinge, 14 medarbejdere og 11 anlægsprojekter i tidligere lederrolle, '
           '37 kapitalprojekter med 25 specialister under GMP/FDA/EMA og fem år som driftsleder på et af landets '
           'største anlæg i kystnær kontekst. Leder på tal: kostcenter, pipeline og kapacitet.', after=80)

    m.section('LEDELSE, ØKONOMI OG VÆKST')
    for label, body in [
        ('Kostcenter og økonomistyring',
         'Fuldt P&L siden 2023: budget, forecast, dækningsgrad og igangværende arbejde, fulgt op hver måned med de '
         'samme tal, så afvigelser ses i samme måned, de opstår.'),
        ('Marked, kunder og tilbud',
         'Egen kundeportefølje, serviceaftaler og tilbudsarbejde i ELOHVAC og Ventek-Air; prioritering af kunder, '
         'go/no-go før tilbud og gevinst/tab-analyse efter.'),
        ('Personaleledelse og udvikling',
         '5 elektrikere og 3 lærlinge, 14 medarbejdere i Ventek-Air, 12 teknikere i ARJ og 25 specialister i '
         'Novo Nordisk-projekter: ansættelser, MUS, kompetencematrix, oplæring og fastholdelse.'),
        ('Forretningsudvikling og vækst',
         'Opbygget egen kundeportefølje og serviceaftaler fra første år, og digitale værktøjer til tilbud og '
         'opfølgning har taget over 40 % af det administrative arbejde ud — kapacitet frigivet til kunder og projekter.'),
        ('Projektleverancer og interessenter',
         '37 anlægsprojekter under GMP/FDA/EMA med FAT/SAT, IQ/OQ/PQ og nul kritiske fund; daglig koordinering med '
         'bygherre, rådgiver, entreprenør og myndighed, med beslutninger der har ejer og frist.')]:
        m.bullet(label, body, after=25)

    m.models_table('VÆRKTØJER OG METODER', ('Opgave', 'Værktøj og dokumenteret anvendelse'), [
        ('Økonomi og kostcenter',
         'Budget pr. projekt og afdeling, forecast, igangværende arbejde, dækningsgrad og timepriser; '
         'investeringsberegninger med NPV, IRR og scenarier.'),
        ('Marked og tilbudsledelse',
         'Markedsstrategi, salgsplan, pipeline med navn, værdi og dato, kundeprioritering og rammeaftaler; '
         'go/no-go før tilbud og gevinst/tab-analyse efter.'),
        ('Kapacitet og bemanding',
         'Kapacitetsplan med timer solgt mod timer til salg; kompetencematrix, belægningsprognose og prioritering '
         'mellem projekter, tilbud og udvikling.'),
        ('Projektledelse og kvalitet',
         'Milepælsplan, risikoregister, projektgennemgang og afvigelser; FAT/SAT, IQ/OQ/PQ og auditeret aflevering — '
         'med standarder og myndighedskrav som fast del af leverancen.'),
        ('Sikkerhed, standarder og myndighed',
         'LOTO, APV, risikovurdering og arbejdstilladelser i drift og på byggeplads; GMP/FDA/EMA og '
         'miljødokumentation som daglig praksis, med myndighedsdialog indarbejdet i plan og kontrakt.'),
        ('Digitalt og data',
         'SAP og Excel dagligt; egne Python/Claude-værktøjer til økonomi-, pipeline- og kapacitetsdata, '
         'ledelsesrapport på én side og scenarier ved store beslutninger.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · erhvervs- og industrikunder',
         [('Kostcenter og kunder', 'Budget, forecast, tilbud, kalkuler, dækningsgrad og indkøb; egen kundeportefølje '
                                   'med serviceaftaler og kunden orienteret samme dag, når noget ændrer sig.'),
          ('Mennesker og digitalt', 'Ansættelser, MUS, kompetencematrix og oplæring; Python og Claude API til tilbud, '
                                    'planlægning og KPI-dashboard — over 40 % produktivitetsløft.')]),
        ('Senior idriftsættelsesingeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024',
         '37 samtidige anlægsprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Projektledelse og interessenter', 'Fremdrift, økonomi, risiko og ressourcer på tværs af engineering, '
                                              'indkøb og drift; månedsrapportering til ledelse og bygherre.'),
          ('Kvalitet og dokumentation', 'FAT/SAT og IQ/OQ/PQ med sporbar dokumentation og afvigelseshåndtering; '
                                        'auditeret aflevering med nul kritiske fund.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter · 2–10 mio. kr. pr. projekt',
         [('Entreprise og leverance', 'Tilbud, kalkuler, underleverandører og afleveringspakker inden for ventilation '
                                       'og tekniske installationer; daglige tavlemøder og flaskehalsanalyser.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos, Lynetten · København · aug. 2017–jan. 2022',
         '24/7-drift · tungt teknisk anlæg i kystnær kontekst · myndighedskrav og miljødokumentation',
         [('Drift, anlæg og myndighed', 'Pumper, ventiler, ventilation og højspænding i døgndrift med rodårsag og '
                                        'korrigerende handling; myndighedsdialog og miljødokumentation som fast del af '
                                        'den daglige drift.'),
          ('Vedligehold, sikkerhed og miljø', 'Vedligeholdelsesplaner, reservedelslager og LOTO/APV i skiftdrift; '
                                              'standard work, 5S og PDCA i værksted og lager.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran, Iran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · industrielt udstyr',
         [('Personale og produktion', 'Vagtplanlægning, materialestyring og opfølgning på mål; fejlfinding, '
                                      'rodårsagsanalyse og korrigerende handlinger på produktionsudstyr.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        m.doc.paragraphs[-1].runs[0].text = 'Omfang: '
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('UDDANNELSE OG AUTORISATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering',
          'Maskinmesterskolen København · 2017–2022 · EQF 6 · GPA 7,6/12')
    m.edu('Elautoriseret maskinmester (LV/MV/HV), stærkstrøm', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('Maritim teknik: damp- og vandkredsløb, køleanlæg og maskinlære',
          'Maskinmesterskolen København · Mercantec 2021 · Søfartsstyrelsen 2021–2023')
    m.edu('El- og maskinteknisk design, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Lean og procesforbedring: 5S, PDCA, VSM, A3, Kaizen',
          'Løbende kurser og daglig anvendelse i drift og projekter')

    m.section('SPROG, PRAKTISK OG REFERENCER')
    m.para('Dansk og persisk: modersmål · Engelsk: professionelt, skriftligt og mundtligt · Kørekort B · Bopæl i '
           'Måløv, ca. 20 minutter fra Høje-Taastrup, og indstillet på rejser til Esbjerg · SAP og Excel i daglig '
           'brug · Referencer fra Novo Nordisk og Biofos samt fra kunder og bygherrer oplyses efter aftale.', after=70)

    m.models_table('KRAV I OPSLAGET — MIN DOKUMENTATION', ('Krav', 'Dokumentation'), [
        ('Civilingeniør eller tilsvarende',
         'Elautoriseret maskinmester med B.Tech i Technology Management & Mechanical Engineering (EQF 6) — maritim '
         'ingeniøruddannelse i konstruktion, maskin og drift, med elautorisation LV/MV/HV ovenpå.'),
        ('Omfattende erfaring med projektering og gennemførelse af anlægsprojekter',
         '20+ år i rådgivning, entreprise og drift: 37 kapitalprojekter med 25 specialister, 11 ventilations-'
         'entrepriser og egen virksomhed med projektering og udførelse for industri- og erhvervskunder.'),
        ('Dokumenteret ledelseserfaring: personale, økonomi og projektledelse',
         'Fuldt P&L siden 2023 med 5 elektrikere og 3 lærlinge — budget, forecast, dækningsgrad og indkøb; 14 '
         'medarbejdere og 12 teknikere i tidligere lederroller med ansættelser, MUS og kompetenceudvikling; 37 '
         'samtidige projektleverancer med fremdrift, økonomi og risiko.'),
        ('Resultater inden for forretningsudvikling, kundeudvikling og tilbudsledelse',
         'Opbygget egen kundeportefølje og serviceaftaler samt forretningsudvikling og kundedialog i egen '
         'virksomhed; tilbuds- og kalkulationsansvar i to virksomheder; digitale værktøjer har løftet '
         'produktiviteten med over 40 %.'),
        ('Faglig ledelse i havne-, marine- og geotekniske projekter',
         'Fem år som driftsleder på et af landets største anlæg i kystnær og maritim kontekst: tunge konstruktioner, '
         'myndighedskrav og miljødokumentation; ledelse af specialister på tværs af fag.'),
        ('Stærke projektleverancer: tid, økonomi, ressourcer og kvalitet',
         'Projektgennemgang på milepæle, risikoregister og afvigelseshåndtering; nul kritiske fund ved aflevering i '
         '37 GMP-projekter og dokumenteret aflevering i alle egne entrepriser.'),
        ('Standarder, myndighedskrav og kundekrav',
         'GMP/FDA/EMA, arbejdsmiljø og miljødokumentation i daglig praksis; myndighedsdialog og auditeret aflevering '
         'som fast del af leverancen.'),
        ('Kommunikation, interessenter og samarbejde på tværs af fag',
         'Daglig kontakt med kunder, bygherrer, rådgivere, entreprenører og myndigheder; dansk modersmål og '
         'professionelt engelsk i en international projektorganisation.')])
    m.page_break()

    m.models_table('FØRSTE 90 DAGE — KOSTCENTER, PIPELINE OG KAPACITET', ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'Møde med hver medarbejder i Høje-Taastrup og Esbjerg om opgaver, styrker og friktion i hverdagen. '
         'Gennemgang af kostcentret, de fem største projekter og de ti største muligheder i pipelinen.'),
        ('Dag 30',
         'Én side pr. kontor: omsætning, indtjening, igangværende arbejde, timer solgt mod timer til salg, pipeline '
         'og de tre største risici. Fælles standarder for tilbud, projektgennemgang og timeopfølgning aftalt med '
         'teamet, og en fast dag for den månedlige økonomigennemgang.'),
        ('Dag 60',
         'Månedlig ledelsesrytme indført — samme tal, samme dag, samme ejer. To tilbud afleveret med skærpet go/no-go '
         'og gevinst/tab-analyse; kompetencematrix samt plan for rekruttering, talent og kompetenceudvikling på begge '
         'kontorer færdig.'),
        ('Dag 90',
         'Markedsplan for Havne og Geoteknik med prioriterede kunder, rammeaftaler og positionering, og et budget '
         'genberegnet på det, vi nu ved. Mindst ét målbart løft — belægning, dækningsgrad eller tid fra tilbud til '
         'kontrakt — dokumenteret på én side til divisionsledelsen.')])

    m.section('EN AFDELING LEDES PÅ KAPACITET, IKKE PÅ TIMER')
    m.para('En rådgivende afdeling tjener penge på solgte timer og taber dem på ubrugt kapacitet og tilbud, der ikke '
           'vandt. Kapacitetsplanen er derfor det vigtigste styringsredskab: hvor mange timer er solgt, hvor mange er '
           'på vej, og hvad gør vi, hvis svaret er "ikke nok"? Ikke sælge billigere — flytte kompetence, rekruttere i '
           'tide og vælge tilbud med omhu. Det er samme logik, jeg har brugt i egen virksomhed, hvor en måned med for lidt '
           'arbejde ikke bliver dækket af næste måned.', after=80)

    m.section('KOSTCENTER: FORECAST DER HOLDER')
    m.para('Budget bygget ned på projekt og medarbejder, og en opfølgning hver måned med de samme tre spørgsmål: hvad '
           'tjener vi, hvad har vi bundet, og hvad kommer ind? Igangværende arbejde, udestående fakturering og '
           'tilbudsprocent afslører, om resultatet er virkeligt. Med fuldt P&L-ansvar har jeg lært, at det er de små '
           'ubetalte timer, der vælter et resultat — ikke den ene store post.', after=80)

    m.section('MARKED OG TILBUD: PIPELINE MED NAVNE OG DATOER')
    m.para('Havne, marine konstruktioner, kystteknik og geoteknik er få, store kunder og lange relationer: kommuner, '
           'havne, forsyningsselskaber og bygherrer, der vælger partner på erfaring og tillid. Det er en kommerciel '
           'disciplin: vi skal vælge, hvor vi kan vinde, og positionere os strategisk i konkurrence om de opgaver, hvor vi '
           'er stærkest, frem for at byde på alt. Derfor skal pipelinen '
           'være konkret — kunde, værdi, dato og ansvarlig — og tilbud bygges på en go/no-go, før nogen bruger 200 '
           'timer på at skrive. Gevinst/tab-analysen tages også, når vi vinder.', after=80)

    m.section('TO KONTORER, ÉN AFDELING')
    m.para('Høje-Taastrup og Esbjerg er to kulturer og to markeder, men én afdeling med ét kvalitetsniveau. Jeg vil '
           'have fælles skabeloner for tilbud, projektgennemgang og timeopfølgning, bevidst udveksling ved større '
           'leverancer og en fast faglig rytme, hvor erfaringer bliver til beslutninger. Jeg har ledet 14 medarbejdere '
           'i Ventek-Air og 5 elektrikere plus 3 lærlinge i ELOHVAC, og jeg ved, at det, der binder en afdeling '
           'sammen, er at se sine idéer blive brugt.', after=80)

    m.section('FAGLIGHED: HAVNE, MARINE OG GEOTEKNIK')
    m.para('Kvaliteten afgøres tidligt: er forundersøgelser og jordbundsforhold gode nok, er vandstande, belastninger, '
           'sætninger og levetid forstået, og er myndighedens krav i konceptet frem for i detailfasen? Derfor en fast '
           'faglig gennemgang ved tre milepæle — forundersøgelser, koncept og detailprojektering — med en kollega fra et '
           'andet fagområde i panelet. Som maskinmester med maritim uddannelse og 20+ år i tunge anlæg læser jeg den '
           'geotekniske rapport, konstruktionstegningen og entreprisekontrakten — og ved, hvad der sker med tid og '
           'økonomi, når de tre ikke taler sammen. Kunder, tilsyn og myndighed får tidlig besked: gennemsigtighed er '
           'billigere end overraskelser. Og når et projekt kræver en specialist, vi ikke har i Danmark, skal det '
           'globale netværk ind over bordet i tide — det er en af WSPs stærkeste sider, og den skal bruges, ikke '
           'beundres.', after=80)

    m.section('KUNDER, MYNDIGHEDER OG INTERESSENTER')
    m.para('En afdelingschef i rådgivning sælger ikke timer; han sælger en relation, der holder i ti år. Jeg er vant '
           'til at sidde over for bygherre, tilsyn og myndighed og forklare, hvad der er muligt, hvad det koster, og '
           'hvad der ikke kan lade sig gøre — tidligt nok til, at det er en oplysning og ikke en konflikt. Fem år med '
           '24/7-drift under myndighedstilsyn og to år med GMP/FDA/EMA-audits har lært mig, at gennemsigtighed er '
           'billigere end overraskelser.', after=80)

    m.section('DIGITALT: DATA I LEDELSEN')
    m.para('Python og Claude gør ledelsesdata hurtige: pipeline og hitrate på én side, kapacitet og belægning pr. '
           'medarbejder, projektøkonomi med afvigelser fremhævet og investeringsberegninger med NPV, IRR og '
           'scenarier. Det erstatter ikke WSPs systemer eller den faglige dømmekraft — men det gør opfølgningen '
           'hurtig nok til, at den bliver brugt.', after=80)

    return m.save(path, title='Ansøgning og CV — Afdelingschef for Havne og Geoteknik, WSP Danmark',
                  subject='Ledelse af rådgivningsafdeling: kostcenter, marked, kapacitet og projektleverancer',
                  keywords='afdelingschef, havne, geoteknik, marine konstruktioner, kostcenter, pipeline, ledelse')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_WSP_AfdelingschefHavneGeoteknik.docx')))
