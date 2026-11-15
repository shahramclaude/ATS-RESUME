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
    m.meta('5. november 2026')
    m.meta('Energy Machines · København · Teknisk Projektleder')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Motiveret CV: Teknisk Projektleder hos Energy Machines', bold=True, color='1A1A1A')
    m.para('Til Morten Rasmussen, Head of Operations', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('En bygning er ikke et anlæg, man sætter op. Den er en maskine, der skal passe ind i noget, der '
           'allerede lever: et varmebehov, en eltarif, en kælder med plads til ingenting og en drift, der ikke '
           'har tid til at vente. Derfor er det jeres egen sætning, der rammer bedst — **energi skal flyttes, '
           'ikke genereres** — og derfor er et projekt som jeres ikke færdigt, når varmepumpen er løftet på '
           'plads. Det er færdigt, når anlægget kører, som det blev lovet, og nogen kan dokumentere det. Med over '
           '120 gennemførte projekter og både køb og Energy-as-a-Service på menuen er det den slags '
           'projektledelse, jeg gerne vil stå i spidsen for — fra kontraktforhandling til aflevering.', after=80)

    m.para('**Jeg vil lede projekterne på fire faste ting.** Først **økonomien, der bliver lavet i tilblivelsen**: '
           'jeg vil sidde med i salgs- og designfasen, hvor scope, risiko og reserver bliver besluttet, så '
           'kalkulationen holder, når byggepladsen begynder — og så en ændring bliver dokumenteret, før den bliver '
           'en ekstraregning. Dernæst **én ejer pr. grænseflade**: mellem design og montage, mellem el, VVS og '
           'mekanik, mellem os og entreprenøren, og mellem underleverandørens levering og den dag, kranen står '
           'på pladsen. Så **tilsyn i marken, ikke i mødelokalet**: jeg vil se montagen, prøvningerne og '
           'indreguleringen selv, for kvalitet og sikkerhed bliver afgjort der, hvor arbejdet bliver udført. Og '
           'endelig **kontrakten som styreværktøj**: AB, ABT og ABR er ikke formalia, men det sprog, '
           'ansvar, frister og ændringer bliver afgjort i, og det skal bruges, mens samarbejdet er godt.', after=80)

    m.para('Projektøkonomi har jeg prøvet fra begge sider af bordet. Hos **Novo Nordisk** løftede jeg **37 '
           'parallelle kapitalprojekter** med 25 specialister og **2–10 mio. kr. pr. projekt**: kalkulation og '
           'acceptkriterier, indkøb og kontrakter, ændringsstyring, månedlig opfølgning på tid, økonomi og risiko '
           '— og aflevering med **nul kritiske fund** ved audit. I **ELOHVAC**, som jeg har drevet siden 2023, '
           'har jeg **fuldt P&L** med fem håndværkere og tre lærlinge: der er en kalkulation, der skal holde, når '
           'tilbuddet er afgivet, og en dækningsgrad, der skal kunne ses på bundlinjen, når måneden er gået.', after=80)

    m.para('Udførelsen på pladsen er min hverdag. I fem år var jeg **drifts- og vedligeholdelsesleder på Lynetten '
           'under Biofos**, et af landets største anlæg i **24/7-drift** med varme, ventilation, pumper, '
           'højspænding og SCADA — og med entreprenører, underleverandører og myndighedskrav på pladsen hver '
           'uge. Som **projekt- og værkstedsleder i Ventek-Air** styrede jeg **14 medarbejdere og 11 samtidige '
           'opgaver**, hvor indkøb, logistik og fremdrift blev holdt sammen på daglige tavlemøder. Jeg ved, hvad '
           'der sker, når en underleverandør melder forsinket, og hvordan man flytter planen, før den flytter sig '
           'selv.', after=80)

    m.para('Teknisk er jeg hjemme i alle tre fag, projektet består af. Jeg er **elautoriseret maskinmester** med '
           '**LV/MV/HV**, uddannet i **køle- og ventilationsteknik** og med B.Tech i Technology Management & '
           'Mechanical Engineering — så varmepumper, varmegenvinding, styringer og tavler er ikke fremmede '
           'størrelser, men maskiner med tryk, temperatur og virkningsgrad, der skal prøves og indreguleres. '
           'Idriftsættelse har jeg gjort systematisk: **FAT og SAT, IQ/OQ/PQ, trykprøvning, funktionsafprøvning og '
           'indregulering**, med dokumentation der bliver skrevet, mens arbejdet foregår. Og jeg har selv hentet '
           'resultaterne hjem: energiledelse på målere og SCADA gav **over 40 % lavere energiforbrug** på '
           'Lynetten, dokumenteret og fastholdt.', after=80)

    m.para('Byggeretten kender jeg fra entreprenørens side. Siden 2023 har jeg drevet dansk entreprisevirksomhed '
           'og arbejdet under **AB og ABT** i praksis: hvad der er en ændring og hvad der er inden for ydelsen, '
           'hvad en frist er værd, hvornår en mangel er en mangel, og hvordan man dokumenterer det i tide — også '
           'når kunden er en god kunde og samarbejdet er godt. Den erfaring gør mig til en bedre projektleder for '
           'jer, fordi jeg kan læse både kontrakten og byggepladsen og ved, hvor de to steder beskriver noget '
           'forskelligt.', after=80)

    m.para('Kulturen lyder som noget, jeg kender: **højt tempo, korte beslutningsveje, uformelt**, og en '
           'virksomhed, der vokser, fordi nogen tør tage beslutningen og stå ved den. Hos mig betyder det, at '
           'projektets næste skridt altid er skrevet ned, at de rigtige mennesker sidder i rummet, når det bliver '
           'besluttet, og at jeg tager de svære samtaler selv — med kunden, med entreprenøren og med vores egen '
           'organisation. **Løsninger frem for problemer** er ikke en positiv indstilling, det er en metode: et '
           'problem, der bliver løftet uden et forslag, er bare blevet flyttet. Og når et projekt går godt, siger jeg '
           'det højt til dem, der gjorde arbejdet — det er den billigste form for fremdrift, der findes.', after=80)

    m.para('Praktisk: jeg bor i Måløv og har omkring en halv time til København, kørekort B og bil, så jeg kan '
           'være på byggepladsen, når der er brug for det, også med kort varsel. Jeg taler og skriver dansk og '
           'engelsk flydende. Kan starte efter aftale. Jeg vil gerne høre, hvilke anlægstyper I har i pipen lige '
           'nu — varmepumpe til fjernvarme, geotermisk lagring eller ren bygningsinstallation — for det er der, '
           'jeg vil lægge mine første uger.', after=70)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Teknisk projektleder med 20+ års erfaring fra tekniske projekter, entreprise og 24/7-drift — '
           'elautoriseret maskinmester med LV/MV/HV, uddannet i køle- og ventilationsteknik og med B.Tech i '
           'Technology Management & Mechanical Engineering. Har løftet 37 parallelle kapitalprojekter på 2–10 '
           'mio. kr. med fuld økonomi, indkøb, entreprenørstyring og idriftsættelse og afleveret med nul kritiske '
           'fund; driver egen entreprisevirksomhed med fuldt P&L siden 2023 under AB/ABT. Arbejder i marken med '
           'mekanik, el og VVS og har dokumenteret energiledelse med over 40 % lavere forbrug.', after=80)

    m.section('PROJEKTER, ØKONOMI OG INSTALLATIONER')
    for label, body in [
        ('Projektledelse og fremdrift',
         'Projektplan og projektplanlægning: milepæle, afhængigheder og én ejer pr. grænseflade; daglige tavlemøder og ugentlig '
         'opfølgning, hvor næste skridt er skrevet ned, aftalt med dem der udfører det, og meldt ud til '
         'projektets interessenter.'),
        ('Projektøkonomi og kontrakt',
         'Kalkulation og budget, ændringsstyring og månedlig opfølgning på tid, økonomi og risiko; fuldt P&L i '
         'egen virksomhed; AB/ABT/ABR anvendt i praksis som entreprenør.'),
        ('Entreprenører og underleverandører',
         'Koordinering af indkøb, logistik og leveranceplaner med entreprenører og underleverandører; krav til '
         'kvalitet, sikkerhed og dokumentation aftalt før opstart og fulgt op på pladsen.'),
        ('Mekanik, el og VVS',
         'Mekaniske installationer, elektriske installationer og VVS: varme, ventilation, køl, pumper og tavler i '
         '24/7-drift; '
         'LV/MV/HV under autorisation; tilsyn med '
         'montage, trykprøvning og funktionsafprøvning i alle tre fag.'),
        ('Idriftsættelse og performance',
         'FAT/SAT, IQ/OQ/PQ, indregulering og aflevering med dokumentation; energiledelse på målere og SCADA med '
         'over 40 % lavere energiforbrug som dokumenteret resultat.')]:
        m.bullet(label, body, after=25)

    m.models_table('VÆRKTØJER OG METODER', ('Opgave', 'Værktøj og dokumenteret brug'), [
        ('Plan og økonomi',
         'MS Project og Excel til plan, ressource- og timeforbrug; budget, dækningsgrad og prognose fulgt pr. '
         'pakke og pr. måned; SAP i daglig brug.'),
        ('Kontrakt og jura',
         'AB, ABT og ABR i praksis som entreprenør og som bygherres repræsentant; udbudsmateriale, '
         'tilbudsevaluering, ændringssager og dokumentation af frister og mangler.'),
        ('Teknisk tilsyn',
         'Montagekontrol, trykprøvning, funktionsafprøvning og indregulering; el-sikkerhed, LOTO og '
         'arbejdstilladelser på byggepladsen.'),
        ('Idriftsættelse',
         'FAT/SAT, IQ/OQ/PQ, acceptkriterier og punch lists; overlevering med as-built, driftsinstruks og '
         'oplæring af driftsfolkene.'),
        ('Data og performance',
         'SCADA og målerdata renset og sammenlignet i Excel og Python; KPI-tavler for energi, temperatur, '
         'tryk og driftstid.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 håndværkere og 3 lærlinge · fuldt P&L · dansk entreprise under AB/ABT',
         [('Økonomi, kunder og kontrakter', 'Kalkulation, tilbud og kontrakt i egen virksomhed; ændringer '
                                            'dokumenteret før udførelse, og kunden informeret samme dag noget '
                                            'ændrer sig.'),
          ('Teknisk levering', 'Tavler, drev, styringer og VVS-tekniske anlæg specificeret, installeret, testet og '
                               'afleveret med dokumentation.')]),
        ('Senior commissioning engineer / projektleder, elsystemer',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Projekt og økonomi', 'Tid, økonomi og risiko rapporteret månedligt til ledelse og kunde; kontrakter, '
                                 'acceptkriterier og ændringer styret i 37 projekter med nul kritiske fund.'),
          ('Idriftsættelse og grænseflader', 'FAT/SAT, IQ/OQ/PQ og aflevering til drift; grænseflader mellem el, '
                                             'mekanik og byg entreprenører styret til aftalt kvalitet og rækkefølge.')]),
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
    m.edu('Autoriseret maskin- og elinstallatør (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('Køle- og ventilationsteknik · STCW sikkerhed', 'Mercantec 2021 · Søfartsstyrelsen 2021')
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
        ('Erfaring med vedvarende energisystemer, varmepumper er en fordel',
         'Køle- og varmeteknik som fag: varmepumper, varmegenvinding og styring er termodynamik, tryk og '
         'virkningsgrad, der skal prøves og indreguleres; køle- og ventilationsteknisk uddannelse og fem år med '
         'varme- og ventilationsanlæg i 24/7-drift; energiledelse med over 40 % lavere forbrug, dokumenteret.'),
        ('Kendskab til dansk byggeret, AB, ABT og ABR',
         'Dansk entreprisevirksomhed siden 2023 med arbejde under AB og ABT i praksis: ændringer, frister, mangler '
         'og dokumentation — fra entreprenørens side af bordet.'),
        ('Indkøb, logistik, tilsyn og idriftsættelse',
         'Indkøb og leverancer styret mod montageplan, med underleverandører fulgt til levering; tilsyn med '
         'montage, trykprøvning, funktionsafprøvning og indregulering, FAT/SAT, IQ/OQ/PQ og aflevering med '
         'as-built og driftsinstruks i 37 projekter.'),
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
         'Projekterne leverer inden for egen økonomi, og afvigelser bliver meldt, før de bliver til tab. Mindst ét '
         'anlæg afleveret eller indkørt med dokumentation, der holder — og en projektmodel, den næste '
         'projektleder kan overtage uden at ringe til mig.')])

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
    m.para('Kvalitet bliver ikke skabt af en kontrolplan, men af en leder, der står ved montagen og spørger, om '
           'det er den løsning, der blev aftalt. Jeg vil se trykprøvningen, funktionsafprøvningen og '
           'indreguleringen, fordi det er der, fejlen stadig kan rettes uden at koste en uge. Og når noget ikke '
           'holder, skal det meldes samme dag — både til kunden og internt — for en forsinkelse, der bliver '
           'fortiet i to uger, er dyrere end den, der bliver meldt med det samme. Jeg vil hellere have en ubehagelig '
           'samtale med en underleverandør i uge tre end en mangelliste i uge tredive — og de fleste '
           'underleverandører foretrækker det samme.', after=80)

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
