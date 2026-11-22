# -*- coding: utf-8 -*-
"""Energy Machines — Teknisk Projektleder (København).

Dansk leverance. Opslaget beder om CV; dokumentet leveres som motiveret CV med
motivationssiden først og CV'et i samme dokument.
Policy: master/README.md — ekstrem sikkerhed, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Teknisk projektleder · Energisystemer, projektøkonomi og idriftsættelse'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('3. november 2026')
    m.meta('Energy Machines · København · Teknisk Projektleder · QuickApply på Jobindex · søg snarest · samtaler løbende')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Motiveret CV: Teknisk Projektleder hos Energy Machines', bold=True, color='1A1A1A')
    m.para('Til Morten Rasmussen, Head of Operations', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('En integreret energimaskine skal passe ind i en bygning, der allerede er i drift: varme- og '
           'kølebehov, adgangsforhold, elkapacitet, eksisterende anlæg og brugernes hverdag sætter rammerne. '
           'Energy Machines’ princip — **energi skal flyttes, ikke genereres** — bliver derfor først til et '
           'resultat, når design, økonomi, udførelse og den efterfølgende drift hænger sammen. Energy Machines’ '
           'integrerede energisystemer samler varmepumper, geotermisk lagring, varmegenvinding og intelligent styring '
           'i én løsning for vedvarende energi og dekarbonisering. Et projekt er ikke færdigt, når udstyret står '
           'på plads; det er færdigt, når ydelsen er afprøvet, afleveret og kan følges op i drift, uanset om kunden '
           'ejer anlægget eller køber det som Energy-as-a-Service.', after=80)

    m.para('**Jeg vil lede projekterne på fire faste ting.** Først **økonomien, der bliver lavet i tilblivelsen**: '
           'jeg vil sidde med i salgs- og designfasen, hvor scope, risiko og reserver bliver besluttet, så '
           'kalkulationen holder, når byggepladsen begynder — og så en ændring bliver dokumenteret, før den bliver '
           'en ekstraregning. Dernæst **én ejer pr. grænseflade**: mellem design og montage, mellem mekaniske '
           'installationer, elektriske installationer, VVS og styring, mellem os og entreprenøren, og mellem '
           'underleverandørens levering og den dag, kranen står på pladsen. Så **tilsyn i marken, ikke i mødelokalet**: jeg vil se montagen, prøvningerne og '
           'indreguleringen selv, for kvalitet og sikkerhed bliver afgjort der, hvor arbejdet bliver udført. Og '
           'endelig **kontrakten som styreværktøj**: AB/ABT — og ABR, hvor aftaleformen gør det relevant — kræver, '
           'at scope, ansvar, frister og ændringer håndteres tidligt. Fortolkning og beslutninger forankres hos '
           'de rette kommercielle og juridiske ansvarlige, mens samarbejdet stadig er godt.', after=80)

    m.para('Projektøkonomien skal følge projektet fra første kalkule til afsluttende forecast. Sammen med salg og '
           'design afgrænses scope, mængder, ydelser, tidsforbrug, leverandørpriser, risikoposter og '
           'forudsætninger. Når planen er godkendt, følges den mod faktisk timeforbrug, bestillinger, ændringer '
           'og forventet slutomkostning. Afvigelser meldes tidligt med årsag, konsekvens og beslutningsmulighed; '
           'ændringer dokumenteres, før de bestilles eller udføres. Så bliver projektøkonomien både en del af '
           'tilblivelsen og et aktivt styringsredskab — ikke en kontrol først, når marginen allerede er væk.', after=80)

    m.para('På byggepladsen bliver planen omsat til daglige aftaler: hvem arbejder hvor, hvilke ydelser skal være '
           'færdige før næste fag kan begynde, og hvilke materialer eller beslutninger mangler. En kort '
           'fremdriftsrytme med ansvarlig og dato for hvert næste skridt gør det muligt at justere rækkefølgen, '
           'når leverancer eller adgangsforhold ændrer sig. Kunden skal samtidig have én tydelig kontaktperson, '
           'som melder status, risici og valg i tide — også når beskeden er, at en milepæl må flyttes. Det skaber '
           'forudsigelighed for entreprenører, underleverandører og den interne projektgruppe.', after=80)

    m.para('Installationsstyringen kræver klare faggrænser mellem mekanik, el, VVS, styring og bygningsdrift. '
           'Før montage fastlægges grænseflader, adgang og rækkefølge; under udførelsen følges kvalitet, '
           'arbejdsmiljø og aftalte kontrolpunkter op på pladsen. Idriftsættelsen planlægges med testforløb, '
           'acceptkriterier, ansvarlige og dokumentation, så afvigelser bliver lukket, før anlægget overdrages. '
           'Energy Machines beskriver selv en samarbejdsbaseret implementering fra boring og tagmontage til '
           'cloudbaseret overvågning. Når anlægget også skal levere en ydelse over tid, skal målinger og '
           'driftsdata med fra start — og afleveringspakken skal kunne bruges af dem, der overtager driften.', after=80)

    m.para('Byggeretten skal bruges tidligt i projektet: scope og forudsætninger tydeligt beskrevet, ændringer '
           'aftalt før udførelse, og frister, kvalitet og ansvar fulgt op med sporbar dokumentation. Min '
           'eksponering for AB/ABT er fra entreprenørens side gennem ELOHVAC; jeg har ikke været kontraktejer '
           'eller ført tvister, og konkret administration efter ABR er ikke dokumenteret. I projekterne vil jeg '
           'sikre, at de kontraktlige beslutninger træffes med den rette kommercielle/juridiske sparring og '
           'bliver omsat til klare næste skridt på pladsen.', after=80)

    m.para('En uformel kultur med højt tempo og korte beslutningsveje kræver tydelige aftaler uden unødige '
           'overleveringer. Salg, design, drift og udførende parter skal kunne se den samme plan og vide, hvem '
           'der beslutter næste skridt. Problemer løftes sammen med handlemuligheder, ikke blot som status; '
           'beslutninger skrives ned, og det gode samarbejde anerkendes, når milepæle nås. Sådan kan en '
           'scale-up bevare tempoet og samtidig holde kvalitet, sikkerhed og økonomi samlet.', after=80)

    m.para('EaaS gør et anlægs dokumenterede performance og driftsvenlige overdragelse til en del af den '
           'kommercielle leverance. Derfor bør projektets afslutning allerede fra opstart omfatte acceptkriterier, '
           'måledata, driftsinstruktioner, åbne punkter og ejerskab for opfølgning. Når disse elementer er '
           'planlagt sammen med salg, design, kunde og drift, kan installationen blive til den langsigtede '
           'energiløsning, Energy Machines lover.', after=70)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Teknisk projektleder og elautoriseret maskinmester (LV/MV/HV) med B.Tech i Technology Management & '
           'Mechanical Engineering og AMU i køle- og ventilationsteknik. Har koordineret 37 parallelle CAPEX-projekter '
           'på 2–10 mio. kr. med månedlig økonomi- og risikofølgeopfølgning samt aflevering uden kritiske fund. '
           'Driver ELOHVAC med fuldt P&L og fem elektrikere plus tre lærlinge. Praktisk grundlag i el, HVAC, '
           'mekanisk drift, projektøkonomi, idriftsættelse og dokumentation.', after=80)

    m.section('PROJEKTER, ØKONOMI OG INSTALLATIONER')
    for label, body in [
        ('Projektledelse og fremdrift',
         'Projektplan og projektplanlægning: milepæle, afhængigheder og én ejer pr. grænseflade; daglige tavlemøder og ugentlig '
         'opfølgning, hvor næste skridt er skrevet ned, aftalt med dem der udfører det, og meldt ud til '
         'projektets interessenter.'),
        ('Projektøkonomi og kontrakt',
         'Novo: månedlig økonomi- og risikoopfølgning på 37 CAPEX-projekter. ELOHVAC: fuldt P&L og tilbud/kalkulation. '
         'AB/ABT-eksponering fra entreprenørside; kontraktejerskab, tvister og konkret ABR-administration er ikke dokumenteret.'),
        ('Entreprenører og underleverandører',
         'Koordinering af indkøb, logistik og leveranceplaner med entreprenører og underleverandører; krav til '
         'kvalitet, sikkerhed og dokumentation aftalt før opstart og fulgt op på pladsen.'),
        ('Mekanik, el og VVS-grænseflader',
         'Biofos: pumper, HVAC og mekanisk/el-teknisk 24/7-drift. ELOHVAC: el-, ventilations- og klimaanlæg. '
         'Køle-/ventilationsteknisk AMU og LV/MV/HV-autorisation. Direkte VVS-rørarbejde eller selvstændigt tilsyn '
         'med alle VVS-installationer er ikke særskilt dokumenteret.'),
        ('Idriftsættelse og performance',
         'FAT/SAT, IQ/OQ/PQ og dokumenteret aflevering; energiledelse på målere og SCADA med over 40 % lavere '
         'energiforbrug som dokumenteret resultat.')]:
        m.bullet(label, body, after=25)

    m.models_table('VÆRKTØJER OG METODER', ('Opgave', 'Værktøj og dokumenteret brug'), [
        ('Plan og økonomi',
         'Excel, SAP ERP, tilbud/kalkulation, P&L, månedsopfølgning på tid, økonomi og risiko; tidsplaner og '
         'ressourcebehov koordineret i tekniske projekter.'),
        ('Kontrakt og jura',
         'AB/ABT-eksponering fra entreprenørside; scope, ændringer, frister og dokumentation. Ingen påstand om '
         'ABR-administration, kontraktejerskab eller tvistførelse.'),
        ('Teknisk tilsyn',
         'ELOHVAC-installationer, KS, sikkerhed og aflevering; LOTO/APV og risikovurdering. Tilsynsmetode for '
         'integrerede energi- og VVS-systemer aftales med ansvarlige fagpersoner.'),
        ('Idriftsættelse',
         'FAT/SAT, IQ/OQ/PQ, acceptkriterier og punch lists; overlevering med dokumentation og oplæring af drift.'),
        ('Data og performance',
         'SAP ERP, Excel/Power Query, Python og SCADA-overvågning; KPI-opfølgning og investeringsmodeller i NPV, '
         'IRR og scenarier.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 håndværkere og 3 lærlinge · fuldt P&L · dansk entreprise under AB/ABT',
         [('Økonomi, kunder og kontrakter', 'Kalkulation, tilbud og kontrakt i egen virksomhed; ændringer '
                                            'dokumenteret før udførelse, og kunden informeret samme dag noget '
                                            'ændrer sig.'),
          ('Teknisk levering', 'Tavler, styringer samt el-, ventilations- og klimaanlæg installeret, fejlsøgt og '
                               'vedligeholdt; KS og dokumenteret aflevering.')]),
        ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen',
         'Data Power Consultant ApS · København · 2024–2026 · sideløbende med ELOHVAC',
         '4–10 personer · tekniske og industrielle applikationer',
         [('Projektleverance og samarbejde', 'Ledte tekniske kundeprojekter fra behovsafklaring og integration til idriftsættelse, '
                                            'dokumentation og overdragelse; Python/Claude, LLM-API’er og AI-agenter med faglig review/test.')]),
        ('Senior commissioning engineer / projektleder, elsystemer',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Projekt og økonomi', 'Tid, økonomi og risiko rapporteret månedligt til ledelse og kunde; kontrakter, '
                                 'acceptkriterier og ændringer styret i 37 projekter med nul kritiske fund.'),
          ('Idriftsættelse og grænseflader', 'FAT/SAT, IQ/OQ/PQ og aflevering til drift; koordinerede grænseflader med engineering, indkøb og '
                                             'byggeorganisationen efter aftalte acceptkriterier.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige opgaver · 2–10 mio. kr. pr. opgave',
         [('Fremdrift og logistik', 'Daglige tavlemøder, flaskehalsanalyse og omprioritering på tværs af 11 '
                                     'samtidige opgaver; indkøb og leverancer fulgt til døren.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Lynetten under Biofos · København · aug. 2017–jan. 2022',
         'Procesanlæg i 24/7-drift · varme, ventilation, pumper, højspænding og SCADA',
         [('Anlæg, entreprenører og myndighed', 'Varme- og ventilationsanlæg drevet og vedligeholdt; entreprenører '
                                                'og underleverandører koordineret på pladsen, og myndighedskrav og '
                                                'arbejdstilladelser overholdt i et anlæg, der ikke måtte stoppe.'),
          ('Energi og dokumentation', 'Energiledelse på målere og SCADA: over 40 % lavere energiforbrug, '
                                      'dokumenteret og fastholdt.')]),
        ('Elektromekaniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · industrielt udstyr',
         [('Team og oppetid', 'Vagtplanlægning og opfølgning på mål; fejlretning, rodårsagsanalyse og korrigerende '
                              'handlinger på produktionsudstyr.'),
          ('El og mekanik i produktionen', 'Tavler, motorer og mekaniske komponenter fejlrettet under drift; '
                                           'ændringer udført sammen med produktionen, så stoppet blev så kort som '
                                           'muligt.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('UDDANNELSE OG AUTORISATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering',
          'Maskinmesterskolen København · 2017–2022 · gennemsnit 7,6/12')
    m.edu('Elautorisation som maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('Køle- og ventilationsteknik · STCW-kurser', 'Mercantec · 2021 · Søfartsstyrelsen · 2021–2023')
    m.edu('El- og maskinkonstruktion, elektroteknik',
          'Tehran Technical University · 2000–2003 · EQF 6')

    m.section('SPROG, PRAKTIK OG REFERENCER')
    m.para('Dansk: modersmål · Engelsk: professionelt · Persisk: modersmål · Kørekort B og bil · Bor i Måløv, '
           'ca. en halv time fra København · Kan starte efter aftale · SAP og Excel dagligt, Python til data · '
           'Referencer på forespørgsel.', after=70)

    m.models_table('DET EFTERSPØRGER DE — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Erfaring med ledelse af tekniske projekter og styring af projektøkonomi',
         '37 parallelle kapitalprojekter på 2–10 mio. kr. med budget, ændringsstyring og månedlig opfølgning; '
         'fuldt P&L i egen virksomhed siden 2023 og 11 samtidige opgaver i Ventek-Air.'),
        ('Stærke lederegenskaber, løsningsorienteret og eksekverende',
         'Daglig ledelse af håndværkere, teknikere og specialister; tavlemøder, fast skriftlig status og svære '
         'samtaler taget selv; flaskehalsanalyse og omprioritering under pres i 11 samtidige opgaver.'),
        ('Viden om mekaniske, elektriske og VVS-installationer',
         'Elautoriseret maskinmester (LV/MV/HV) med køle- og ventilationsteknisk uddannelse; varme, ventilation, '
         'pumper og tavler drevet i 24/7 og monteret og testet i egen virksomhed.'),
        ('Erfaring med vedvarende energisystemer; varmepumper er en fordel',
         'Relevant teknisk base fra AMU i køle- og ventilationsteknik, HVAC-service/drift og dokumenteret '
         'energioptimering (over 40 % lavere energiforbrug på Lynetten). Ledelse af Energy Machines-integrerede '
         'varmepumpe-/geotermiprojekter og BTES i praksis er ikke dokumenteret.'),
        ('Kendskab til dansk byggeret, AB, ABT og ABR',
         'ELOHVAC: entreprenørside-eksponering for AB/ABT, herunder scope, ændringer og dokumentation. '
         'Kontraktejerskab, tvister og konkret ABR-administration er ikke dokumenteret; relevant sparring indgår '
         'i håndteringen af juridiske spørgsmål.'),
        ('Indkøb, logistik, tilsyn og idriftsættelse',
         'Indkøb, leverancer og underleverandører koordineret mod plan; FAT/SAT og IQ/OQ/PQ samt dokumenteret aflevering '
         'i Novo Nordisk-projekter. ELOHVAC leverer installation, KS og afleveringsdokumentation.'),
        ('Kvalitets-, sikkerheds- og kontraktuelle forpligtelser',
         'Arbejdsmiljø og elsikkerhed på byggepladsen med arbejdstilladelser og LOTO; kvalitetskrav og '
         'acceptkriterier aftalt i kontrakten og kontrolleret ved aflevering. Sikkerhedsorganisation og entreprenørkrav '
         'fulgt op på pladsen, ikke kun i papirerne.'),
        ('Baggrund som ingeniør, maskinmester eller tilsvarende; dansk og engelsk',
         'Elautoriseret maskinmester med B.Tech i Technology Management & Mechanical Engineering og 20+ års '
         'erfaring; dansk modersmål og engelsk professionelt i internationale projektmiljøer.')])
    m.page_break()

    m.models_table('DE FØRSTE 90 DAGE — PLANEN, ØKONOMIEN OG PLADSEN', ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'Ind i de projekter, der kører: kontrakter, kalkulation, tidsplan og de åbne punkter på pladsen. Med ud '
         'på et anlæg under montage og et under indkøring, og en samtale med hver entreprenør om, hvad de ser som '
         'den største risiko.'),
        ('Dag 30',
         'Et projektkort pr. sag: økonomi mod kalkulation, milepæle, grænseflader, risici og næste beslutning med '
         'dato og ejer. Én fast rapporteringsrytme til salg, design og ledelse, som alle kan læse.'),
        ('Dag 60',
         'Ændringssager, indkøb og leveranceplaner ryddet op, så pladsen arbejder efter den plan, der gælder; '
         'kvalitets- og sikkerhedsgennemgang på de aktive pladser med handlinger, der har en ejer.'),
        ('Dag 90',
         'Hvert aktivt projekt har en ajourført forecast mod godkendt økonomi, navngivne risici og beslutninger '
         'med ejer og dato. Mindst ét projekt er ført frem til næste aftalte accept-/idriftsættelsesgate, når '
         'projektplanen tillader det, med sporbar dokumentation og klar overdragelse til drift.')])

    m.section('ØKONOMIEN LAVES FØR KONTRAKTEN')
    m.para('Et projekt bliver ikke dyrt på byggepladsen. Det bliver dyrt i den kalkulation, der blev lavet, før '
           'nogen havde været i kælderen: forkert scope, urealistisk tidsplan, en underleverandørpris uden '
           'reserve og en grænseflade, ingen havde talt om. Derfor vil jeg ind i tilblivelsen sammen med salg og '
           'design — ikke for at tage beslutningen fra dem, men for at sikre, at den bliver taget på et grundlag, '
           'der kan holde, når det møder virkeligheden. Det er også den billigste form for risikostyring: en reserveret '
           'post i kalkulationen koster mindre end en ombygning, der bliver opdaget i indkøringsfasen.', after=80)

    m.section('NÆSTE SKRIDT SKAL ALTID VÆRE SKREVET NED')
    m.para('Fremdrift er ikke tempo. Fremdrift er, at den, der skal levere i morgen, ved hvad han skal levere, og '
           'at den, der venter på ham, ved hvornår. Derfor arbejder jeg med en plan, der har én ejer pr. linje, et '
           'tavlemøde der er kort nok til at blive holdt hver dag, og en skriftlig status, hvor beslutninger og '
           'næste skridt står — ikke kun procenter og farver. På en byggeplads med mange fag samtidig er det den '
           'eneste måde at holde tiden. Jeg holder møderne korte, fordi et møde, der varer en time, koster elleve '
           'mandetimer — og fordi de fleste beslutninger bliver bedre, når de bliver taget af dem, der har '
           'hånden i maskinen.', after=80)

    m.section('TILSYN ER IKKE ET SKEMA')
    m.para('Kvalitet bliver ikke skabt af en kontrolplan alene. Ved installationen skal aftalte hold points, '
           'funktionsprøver og idriftsættelsesaktiviteter observeres af de ansvarlige fagpersoner, og afvigelser '
           'registreres med ejer og frist. Hvis prøvning eller indregulering indgår i scope, skal metode og '
           'acceptkriterier være aftalt på forhånd. Når noget ikke holder, meldes det tidligt til kunden og '
           'internt med konsekvens, løsningsmuligheder og næste beslutning — så en afvigelse ikke først dukker op '
           'på mangellisten ved aflevering.', after=80)

    m.section('KONTRAKTEN ER EN SAMTALE, DER ER SKREVET NED')
    m.para('AB og ABT findes for at gøre det forudsigeligt, hvad der sker, når parterne ikke er enige. Jeg bruger '
           'dem, mens samarbejdet er godt: ændringer bliver beskrevet, før de bliver udført, frister bliver '
           'dokumenteret, og mangelgennemgang bliver gennemført ordentligt, så den ikke bliver en diskussion '
           'bagefter. Det er ikke formalisme — det er det, der gør, at et godt kundeforhold også er godt om et år.', after=80)

    m.section('ET ANLÆG ER FÆRDIGT, NÅR DET KØRER')
    m.para('Aflevering er ikke den dag, nøglerne skifter hænder. Det er den dag, anlægget kører inden for de '
           'parametre, der blev lovet, driftsfolkene kan betjene det, og dokumentationen findes i den form, nogen '
           'kan bruge den i. Derfor lægger jeg indkøring, indregulering og oplæring ind i planen fra starten — og '
           'jeg bliver ved, til tallene viser det, kontrakten sagde.', after=80)

    m.section('SCALE-UP BETYDER BESLUTNINGER TÆT PÅ PLADSEN')
    m.para('I en virksomhed, der vokser, er den største risiko ikke, at nogen tager en forkert beslutning — det er, '
           'at ingen tager den, fordi den skal op i et system, der ikke findes endnu. Jeg er vant til at arbejde '
           'med korte beslutningsveje og til selv at tage beslutningen, når den ligger inden for mit mandat, og '
           'at skrive den ned bagefter, så den kan efterprøves. Det er sådan et scale-up holder tempo uden at '
           'miste overblikket.', after=80)

    m.section('ENERGI SKAL FLYTTES — OGSÅ I PROJEKTLEDELSEN')
    m.para('Energy Machines bygger systemer, hvor varme, køl og lagring flyttes mellem medier i stedet for at '
           'blive produceret fra bunden, og hvor kunden kan vælge at eje eller købe ydelsen. Det stiller krav til '
           'projektlederen, der rækker ud over tidsplan og budget: anlægget skal kunne drives økonomisk i ti år, '
           'servicevejen skal være mulig, og de data, der dokumenterer besparelsen, skal være der fra dag et. '
           'Det, der gør omstillingen bæredygtig i praksis, er netop, at de tre ting holder samtidigt — og det er '
           'den slags projekter, jeg gerne vil måles på.', after=80)

    return m.save(path, title='Motiveret CV — Teknisk Projektleder, Energy Machines',
                  subject='Energisystemer, projektøkonomi, installation og idriftsættelse',
                  keywords='teknisk projektleder, projektøkonomi, entreprenører, underleverandører, indkøb, '
                           'idriftsættelse, mekaniske installationer, elektriske installationer, VVS, varmepumper, '
                           'AB, ABT, ABR')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_EnergyMachines_TekniskProjektleder.docx')))
