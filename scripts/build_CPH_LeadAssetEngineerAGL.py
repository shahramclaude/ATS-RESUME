# -*- coding: utf-8 -*-
"""Københavns Lufthavne (CPH) — Lead Asset Engineer, Airfield Ground Lighting.

Dansk leverance. Opslaget siger "vi modtager som udgangspunkt kun CV": dokumentet er et
motiveret CV med motivationsdelen først og CV'et i samme dokument.
Policy: master/README.md — ekstrem sikkerhed, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Lead Asset Engineer · Kritisk elektrisk infrastruktur, asset management og totaløkonomi'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('5. november 2026')
    m.meta('Københavns Lufthavne (CPH) · Aeronautical Asset Engineering · Lead Asset Engineer, AGL')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Motiveret CV: Lead Asset Engineer, Airfield Ground Lighting', bold=True, color='1A1A1A')
    m.para('Til Søren Wieseltier, Senior Manager, Aeronautical Asset Engineering', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('Lys på en bane er ikke belysning. Det er en instruktion. En indflyvning, en rullevej der drejer af, en '
           'stopbar der skal stå rød — AGL er lufthavnens eget sprog til piloten, og et mørkt felt er ikke en '
           'gene, men en begrænsning i driften. Det er derfor, denne rolle er interessant: den handler ikke om at '
           'holde lamper tændt, men om at sætte de standarder, den vedligeholdelsesstrategi og den '
           'reinvesteringsplan, der gør, at anlægget kan siges at være sikkert og tilgængeligt — ikke kun se ud '
           'som om det er det.', after=80)

    m.para('**Jeg vil sætte den faglige retning på fire faste ting.** Først **standarder, der kan efterprøves**: '
           'tekniske krav, principper og vedligeholdelsesstrategier udledt af myndighedskrav, kritikalitet og '
           'fejlmåder — ikke af, hvad en leverandør plejer at levere. Dernæst **reinvestering på levetid og '
           'risiko**: en asset-plan pr. anlæg med tilstand, restlevetid, konsekvens og totaløkonomi, så '
           'levetidsforlængelse og udskiftning bliver en beslutning med et regnestykke under og ikke en '
           'mavefornemmelse i en budgetrunde. Så **kravstiller i projekterne**: krav skrevet, så de kan '
           'verificeres, designgranskning der finder fejlen før støbningen, test og dokumentation der følger '
           'anlægget, og en idriftsættelse der slutter med, at driften kan overtage uden forbehold. Og endelig '
           '**data som grundlag for forbedring**: nedbrud, alarmer, responstider og gentagne fejl talt op, så '
           'næste års strategi bygger på, hvad anlægget faktisk gjorde — ikke på hvad vi troede.', after=80)

    m.para('Et AGL-anlæg er et system af systemer: seriekredse med konstante strømkilder, lysarmaturer i og over '
           'banen, et kontrol- og overvågningssystem, og en dokumenteret tilstand for hver sektion. Derfor er den '
           'farligste tilstand ikke en lampe, der er gået — det er en kreds, hvor fejlen er fundet og midlertidigt '
           'udbedret, og hvor ingen længere ved, hvad der er originalt, og hvad der er lappet. Standarder, '
           'reservedele og dokumentation er det, der gør forskellen mellem et anlæg, der er sikkert, og et anlæg, '
           'der ser sikkert ud.', after=80)

    m.para('Kritisk elektrisk infrastruktur er mit fag. Jeg er **elautoriseret maskinmester med LV/MV/HV** og har i '
           'fem år været **drifts- og vedligeholdelsesleder på Lynetten under Biofos**, et af landets største '
           'anlæg i **24/7-drift**: transformere, koblingsanlæg, beskyttelse, drev, pumper og **SCADA** på alt, '
           'der bevægede sig, og et anlæg hvor en udkobling ikke var en ulejlighed, men en miljøhændelse. Der har '
           'jeg arbejdet med det, denne rolle skal stå i spidsen for: tilstandsbaseret vedligehold, '
           'kritikalitetsvurdering, reservedele mod leveringstider, myndighedskrav og dokumentation, der kunne '
           'fremlægges.', after=80)

    m.para('Asset management har jeg gjort med tal og med hænder. Jeg har opbygget vedligeholdet efter '
           'kritikalitet og tilstand frem for efter kalender, ført fejlhistorik mens fejlen var ny, og brugt '
           'målinger og **SCADA-data** til at finde ud af, hvor energien og driftstiden forsvandt — resultatet var '
           '**over 40 % lavere energiforbrug**, dokumenteret og fastholdt. Det er den samme slags arbejde som '
           'performanceopfølgning på AGL: definér, hvad der måles, mål det samme sted hver gang, og brug '
           'afvigelsen til at beslutte noget.', after=80)

    m.para('Kravstillerrollen har jeg fra projektsiden. Hos **Novo Nordisk** løftede jeg **37 parallelle '
           'kapitalprojekter** med 25 specialister og 2–10 mio. kr. pr. projekt: krav og acceptkriterier, '
           'designgranskning, **FAT og SAT, IQ/OQ/PQ**, ændringsstyring og aflevering — med **nul kritiske fund** '
           'ved audit. Jeg har siddet på begge sider af bordet, også som **indehaver af ELOHVAC** siden 2023 med '
           'fuldt P&L, hvor en dårlig kravspecifikation bliver til ekstraarbejde, der skal betales af nogen. Det '
           'gør mig til en kravstiller, der skriver krav, som leverandøren kan svare på, og som driften kan '
           'overtage.', after=80)

    m.para('At skabe sammenhæng mellem drift, asset management, projekter, rådgivere, leverandører og de øvrige '
           'interessenter er ikke et '
           'mødeforum for mig, men en arbejdsform. Som **projekt- og værkstedsleder i Ventek-Air** styrede jeg '
           '**14 medarbejdere og 11 samtidige opgaver** med dagligt tavlemøde, og som leder for **12 teknikere i '
           'ARJ** havde jeg både oppetid, oplæring og den faglige kvalitet. Jeg er vant til at være den, der '
           'samler faglighederne og træffer den beslutning, ingen af dem kan træffe alene — og til at forklare '
           'den bagefter, så den holder.', after=80)

    m.para('CPH som arbejdsplads tiltrækker mig, fordi infrastrukturen er både gammel og ny på samme tid: noget '
           'skal holde i tyve år endnu, noget skal udskiftes, og begge dele skal kunne forsvares over for '
           'myndighed, økonomi og drift. Jeg kan lide den slags beslutninger — dem hvor man ikke kan få alle '
           'svarene, men godt kan gøre grundlaget så godt, at beslutningen er forsvarlig. Og jeg kan lide, at '
           'fagligheden bliver videreført: jeg har oplært lærlinge, teknikere og kolleger i hele mit arbejdsliv, '
           'og det er den del af et lead-ansvar, jeg tager mest alvorligt.', after=80)

    m.para('Praktisk: jeg bor i Måløv med omkring en halv time til CPH, kørekort B og bil. Jeg taler og skriver '
           'dansk og engelsk professionelt, og jeg kan blive **politigodkendt** og opretholde godkendelsen gennem '
           'ansættelsen. Kan starte efter aftale. Jeg vil gerne høre, hvor AGL-området står med '
           'reinvesteringsbehov og standarder i dag — det er der, jeg vil lægge de første uger.', after=70)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Asset- og driftsleder med 20+ års erfaring fra kritisk elektrisk infrastruktur og 24/7-drift — '
           'elautoriseret maskinmester med LV/MV/HV og B.Tech i Technology Management & Mechanical Engineering. '
           'Fem år som drifts- og vedligeholdelsesleder på et af landets største anlæg med transformere, '
           'koblingsanlæg, beskyttelse, drev og SCADA: tilstandsbaseret vedligehold, kritikalitet, '
           'reservedelsstrategi og myndighedskrav. Teknisk kravstiller i 37 kapitalprojekter med FAT/SAT, '
           'IQ/OQ/PQ og nul kritiske fund. Arbejder datadrevet — over 40 % lavere energiforbrug dokumenteret — og '
           'skriver standarder, som andre kan efterprøve.', after=80)

    m.section('ASSET MANAGEMENT, STANDARDER OG KRITISK INFRASTRUKTUR')
    for label, body in [
        ('Asset management og vedligeholdelsesstrategi',
         'Asset-register fra infrastruktur til komponent, kritikalitetsvurdering, tilstandsbaseret vedligehold, '
         'reservedelskritikalitet mod leveringstider og en strategi, der kan forsvares over for drift og økonomi.'),
        ('Reinvestering, levetid og totaløkonomi',
         'Restlevetid, fejlmåder og konsekvens som grundlag for levetidsforlængelse eller udskiftning; '
         'investerings- og aktiveringssager dokumenteret i 37 kapitalprojekter og i egen virksomhed med fuldt P&L.'),
        ('Teknisk kravstiller',
         'Krav og acceptkriterier skrevet, så de kan verificeres; designgranskning, ændringsstyring, FAT/SAT, '
         'IQ/OQ/PQ og aflevering med as-built og driftsinstruks.'),
        ('Kritisk el-infrastruktur',
         'Transformere, koblingsanlæg, beskyttelse, drev og motorer i 24/7-drift under LV/MV/HV-autorisation; '
         'isolation, LOTO og sikker kobling som daglig praksis.'),
        ('Data, performance og forbedring',
         'SCADA- og målerdata renset og sammenlignet i Excel og Python; nedbrud, alarmer og gentagne fejl fulgt op '
         'med rodårsag og handling — energiledelse med over 40 % lavere forbrug dokumenteret.'),
        ('Faglighed og videndeling',
         'Oplæring og coaching af teknikere og lærlinge, kompetencematrix pr. medarbejder og faglig sparring i '
         'marken; faglige standarder formidlet, så de bliver brugt og ikke blot udgivet.')]:
        m.bullet(label, body, after=25)

    m.models_table('VÆRKTØJER OG METODER', ('Opgave', 'Værktøj og dokumenteret brug'), [
        ('Asset og vedligehold',
         'Kritikalitetsanalyse, risikoanalyse, FMECA-tankegang, tilstandsbaseret vedligehold, reservedelsstrategi og '
         'levetidsbetragtninger på kritiske komponenter.'),
        ('Standarder og krav',
         'Tekniske standarder og kravspecifikationer skrevet og vedligeholdt; myndighedskrav og '
         'leverandørkrav omsat til verifikation og dokumentation.'),
        ('Projekt og kvalitet',
         'Designgranskning, FAT/SAT, IQ/OQ/PQ, acceptkriterier og aflevering; ændringsstyring før ændringen, '
         'as-built og driftsinstruks ved overlevering.'),
        ('Drift og sikkerhed',
         '24/7-drift, skifteplanlægning, beredskab og akutopkald; APV, arbejdstilladelser, LOTO og el-sikkerhed '
         'under LV/MV/HV.'),
        ('Data og økonomi',
         'SCADA og målerdata i Excel og Python; KPI\'er for tilgængelighed, nedbrud og energi; SAP, budget og '
         'totaløkonomi i egen virksomhed.'),
        ('Samarbejde og ledelse',
         'Tavlemøder, fast skriftlig status og beslutningsoplæg, der kan læses af både teknikere og ledelse; '
         'MUS, oplæring og coaching af kolleger.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 håndværkere og 3 lærlinge · fuldt P&L · el-installation og service',
         [('Økonomi, krav og kunder',
           'Tilbud, kalkulation og kontrakt med fuldt P&L; krav og dokumentation aftalt med kunden, før arbejdet '
           'gik i gang, og ændringer dokumenteret undervejs.')]),
        ('Senior commissioning engineer / projektleder, elsystemer',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Kravstiller og kvalitet',
           'Acceptkriterier, designgranskning, FAT/SAT og IQ/OQ/PQ i 37 projekter; auditeret aflevering med nul '
           'kritiske fund.'),
          ('Aktivering og økonomi',
           'Investeringer og aktivering dokumenteret og afstemt med økonomifunktionen; tid, økonomi og risiko '
           'rapporteret månedligt til ledelse og kunde.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige opgaver · 2–10 mio. kr. pr. opgave',
         [('Fremdrift og leverancer',
           'Dagligt tavlemøde, flaskehalsanalyse og omprioritering på tværs af 11 samtidige opgaver; leverancer '
           'kontrolleret mod acceptkriterier før afsendelse.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Lynetten under Biofos · København · aug. 2017–jan. 2022',
         'Kritisk procesanlæg i 24/7-drift · transformere, koblingsanlæg, beskyttelse, drev, pumper og SCADA',
         [('Anlæg, myndighed og sikkerhed',
           'Tilstandsbaseret vedligehold og kritikalitetsbaseret prioritering; myndighedskrav, arbejdstilladelser '
           'og LOTO overholdt i et anlæg, der ikke måtte stoppe.'),
          ('Energi, data og resultat',
           'Energiledelse på målere og SCADA-data: over 40 % lavere energiforbrug, dokumenteret og fastholdt.')]),
        ('Elektromekaniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · industrielt udstyr',
         [('Oppetid og faglighed',
           'Vagtplanlægning, oplæring og opfølgning på mål; fejlretning, rodårsagsanalyse og korrigerende '
           'handlinger på produktionsudstyr.')]),
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
    m.para('Dansk: modersmål · Engelsk: professionelt · Persisk: modersmål · Kørekort B og bil · Bor i Måløv, ca. '
           'en halv time fra CPH · Kan politigodkendes og opretholde godkendelsen · Kan starte efter aftale · SAP '
           'og Excel dagligt, Python til data · Referencer på forespørgsel.', after=70)

    m.models_table('DET EFTERSPØRGER DE — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Relevant videregående teknisk uddannelse, fx elektroingeniør, stærkstrømsingeniør eller maskinmester',
         'Elautoriseret maskinmester (LV/MV/HV) med B.Tech i Technology Management & Mechanical Engineering og '
         '20+ års erfaring i kritisk elektrisk infrastruktur og drift.'),
        ('Flere års erfaring med AGL, elektrisk infrastruktur eller andre kritiske tekniske anlæg',
         'Fem år som drifts- og vedligeholdelsesleder på et kritisk anlæg i 24/7-drift med transformere, '
         'koblingsanlæg, beskyttelse, drev og SCADA; før det 12 teknikere på produktionsudstyr og siden 2023 egen '
         'el-virksomhed.'),
        ('Myndighedskrav, driftsbehov og strategi omsat til tekniske løsninger og standarder',
         'Myndighedskrav og miljødokumentation omsat til procedurer og vedligehold i 24/7-drift; tekniske krav og '
         'acceptkriterier skrevet og efterprøvet i 37 projekter.'),
        ('Asset management, vedligeholdelsesstrategier og risikoanalyser',
         'Tilstandsbaseret vedligehold, kritikalitetsvurdering, reservedelsstrategi og fejlmåder i drift; risiko '
         'vurderet og håndteret pr. opgave i projekter, ved produktionsstop og i egen virksomhed med fuldt ansvar.'),
        ('Performanceopfølgning og reinvesteringsplan',
         'KPI\'er for tilgængelighed, nedbrud og energi fulgt på SCADA- og målerdata; investerings- og '
         'aktiveringssager dokumenteret og afstemt i 37 kapitalprojekter, og levetidsbetragtninger brugt i eget '
         'budget.'),
        ('Teknisk kravstiller i komplekse projekter',
         'Krav, acceptkriterier og designgranskning i 37 parallelle projekter med 25 specialister; '
         'leverandørgrænseflader styret til aftalt kvalitet og rækkefølge.'),
        ('Kvalitet gennem designgranskning, test, dokumentation og idriftsættelse',
         'FAT/SAT, IQ/OQ/PQ, punch lists og aflevering med as-built og driftsinstruks; nul kritiske fund ved '
         'audit og dokumentation, der kunne fremlægges år senere.'),
        ('Safety, compliance, driftssikkerhed og totaløkonomi som beslutningsgrundlag',
         'Beslutninger taget på et dokumenteret grundlag i 24/7-drift og i 37 projekter: krav, risiko, konsekvens '
         'og økonomi lagt frem sammen, så ledelsen kunne vælge — og efterprøvet bagefter.'),
        ('Dansk og engelsk, følgeskab og udvikling af fagligheden',
         'Dansk modersmål og engelsk professionelt; faglig sparring, oplæring og coaching af teknikere og lærlinge '
         'i alle lederroller — og beslutningsoplæg, der kan læses af både fag og ledelse.')])
    m.page_break()

    m.models_table('DE FØRSTE 90 DAGE — STANDARDERNE, ANLÆGGET OG TALLENE', ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'Ud på arealerne og ind i dokumentationen: hvilke AGL-anlæg findes, i hvilken tilstand, hvilke standarder '
         'og vedligeholdelsesplaner gælder i dag, og hvilke myndighedskrav og projekter er på vej. Samtaler med '
         'drift, Asset Management, rådgivere og de leverandører, der kender anlægget.'),
        ('Dag 30',
         'Et billede af AGL-området pr. anlægstype: tilstand, alder, fejlhistorik, kritikalitet og næste '
         'reinvestering. De standarder og vedligeholdelsesstrategier, der ikke længere passer til virkeligheden, '
         'navngivet — og de tre vigtigste risici lagt frem for ledelsen.'),
        ('Dag 60',
         'En opdateret asset-plan og reinvesteringsrækkefølge med levetid, konsekvens og totaløkonomi som '
         'grundlag; kravprofil og kvalitetssikring i de kørende AGL-projekter gennemgået, så krav, test og '
         'dokumentation hænger sammen.'),
        ('Dag 90',
         'Performanceopfølgning på plads: tilgængelighed, nedbrud og responstider målt ens hver måned og læsbare '
         'for både drift og ledelse; mindst én standard og én vedligeholdelsesstrategi opdateret — og et fagligt '
         'miljø, hvor rådgivere og leverandører ved, hvad der bliver målt på.')])

    m.section('STANDARDEN ER DEN BESLUTNING, DER BLIVER TAGET HVER DAG')
    m.para('En standard er ikke et dokument, der bliver udgivet. Det er den beslutning, der bliver taget hver dag, '
           'når en tekniker står ved et anlæg og skal vælge mellem to løsninger. Derfor skal standarden være '
           'skrevet, så den kan bruges klokken tre om natten: hvad er kravet, hvad er grænsen, hvad gør man, når '
           'grænsen er nået, og hvem beslutter. Hvis standarden ikke kan bruges på den måde, er det ikke en '
           'standard — det er en hensigtserklæring, som ingen kan efterprøve. Og en standard, der ikke bliver brugt, '
           'skal ændres eller afskaffes: et regelsæt, folk går uden om, lærer dem kun, at regler er noget, man '
           'omgår.', after=80)

    m.section('LEVETID ER ET REGNESTYKKE, IKKE EN MENING')
    m.para('Om et anlæg skal holde fem år mere eller skiftes i år, er en af de beslutninger, hvor alle har en '
           'holdning. Jeg vil hellere stille de tre spørgsmål, der kan besvares: hvad koster det at holde det '
           'kørende, hvad koster det, når det svigter, og hvad er sandsynligheden for, at det svigter inden for '
           'den periode? Med tilstand, fejlhistorik og konsekvens på plads bliver totaløkonomi et regnestykke, '
           'man kan fremlægge — også når svaret er, at det gamle anlæg skal have lov at leve et år mere.', after=80)

    m.section('SERIEDRIFT OG SIKKERHED HAR IKKE RÅD TIL GÆT')
    m.para('Elektrisk infrastruktur på en lufthavn er bygget til at fejle kontrolleret: redundans, selektivitet, '
           'overvågning og en klar procedure, når noget falder ud. Det er den samme tankegang som i en kritisk '
           'procesdrift — en fejl må ikke sprede sig, og den må ikke opdages af den, der har brug for anlægget. '
           'Derfor lægger jeg vægt på beskyttelsesindstillinger, dokumenteret koblingsdrift, LOTO og på, at '
           'ændringer bliver modelleret og godkendt, før de bliver udført, ikke bagefter. På et anlæg, der skal kunne '
           'bruges hver nat, er den dyreste fejl den, der først bliver opdaget, da nogen havde brug for '
           'anlægget.', after=80)

    m.section('KRAVSTILLER ER EN ROLLE, MAN KAN MÅLES PÅ')
    m.para('Et godt krav er skrevet, så leverandøren kan svare på det, entreprenøren kan bygge efter det, og '
           'driften kan overtage det. Et dårligt krav bliver opdaget i idriftsættelsen, hvor det er dyrest at '
           'ændre. Derfor skriver jeg krav med en verifikation ved siden af hver sætning — hvordan vi ser, at det '
           'er opfyldt — og følger op i designgranskning, FAT, SAT og afleveringsforretning. Det er også den rolle, '
           'jeg bedst kan lide i et projekt: den, der sørger for, at man ikke bygger noget forkert, mens alle er '
           'enige om, at det går godt. Det er også den rolle, der giver mest ro i maven hos driften: nogen har læst '
           'papirerne efter i sømmene, før anlægget blev deres.', after=80)

    m.section('DATA SKAL KUNNE TÅLE AT BLIVE SPURGT')
    m.para('Performanceopfølgning bliver først værdifuld, når tallene er defineret én gang og målt samme sted '
           'hver gang. Hvad er en tilgængelighed, hvad tæller som et nedbrud, og hvornår starter responstiden? Når '
           'de tre ting er aftalt med drift og leverandør, kan man følge udviklingen og bruge den i '
           'reinvesteringsplanen. Jeg har bygget den slags op i Excel og Python på SCADA-data, og jeg ved, at det '
           'ikke handler om værktøjet, men om at blive enige om definitionen, før den første måned bliver rapport. '
           'Ellers ender man med to sandheder om det samme anlæg, og så bliver ingen af dem brugt til noget.', after=80)

    m.section('FAGLIGHED BLIVER IKKE VIDEREFØRT AF SIG SELV')
    m.para('Et lead-ansvar er også et ansvar for, at fagligheden findes om fem år. Det betyder, at viden om '
           'anlægget skal være skrevet ned, at rådgivere og leverandører ikke må være de eneste, der kender '
           'systemet, og at de yngre teknikere bliver sat til opgaver, der er svære nok. Jeg har oplært lærlinge, '
           'teknikere og kolleger i hele mit arbejdsliv, og jeg ved, at det kræver tid, der skal planlægges — ikke '
           'tid, der bliver tilbage. Derfor skal den stå i planen som en opgave med en ejer — ikke som noget, man '
           'gør, når der er plads.', after=80)

    return m.save(path, title='Motiveret CV — Lead Asset Engineer, Airfield Ground Lighting, CPH',
                  subject='Kritisk elektrisk infrastruktur, asset management og totaløkonomi',
                  keywords='asset management, airfield ground lighting, AGL, kritisk infrastruktur, '
                           'vedligeholdelsesstrategi, reinvestering, totaløkonomi, kravstiller, LV/MV/HV, SCADA')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_CPH_LeadAssetEngineerAGL.docx')))
