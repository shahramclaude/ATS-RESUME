# -*- coding: utf-8 -*-
"""Elos Medtech Pinol A/S (Gørløse) — Process Development Manager.

Form (master/FORMKATALOG.md): åbning **E** (tidsforskydningen: linjen bliver
bestemt atten måneder før maskinen ankommer), struktur **De fem tal** (tid fra
beslutning til produktion · udbytte og scrap · cyklustid · changeover og
oppetid · antal gange nogen ringer), register **Valideringen** (nyt: URS,
FAT/SAT, IQ/OQ/PQ, afvigelse, change control, sporbarhed). Kulturfil:
jd/ElosMedtech_ProcessDevelopment_kultur.txt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Process Development Manager · produktionsudstyr, automatisering og validering'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('13. november 2026')
    m.meta('Elos Medtech Pinol A/S · Gørløse · Engineering · via Jobindex QuickApply')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Process Development Manager', bold=True, color='1A1A1A')

    def lp(text, after=60):
        return m.para(text, after=after, line=236)

    # ---------------------------------------------------------------- side 1
    lp('**En produktionslinje bliver ikke bestemt, den dag maskinen ankommer.** Den bliver bestemt '
       'atten måneder før — i den specifikation, ingen gad læse, og i den business case, hvor nogen '
       'skrev »forventet højere kapacitet« uden at skrive, hvem der skulle dokumentere det, og hvad '
       'der skulle ske, hvis udbyttet faldt. Det er de beslutninger, Elos Medtech nu ansætter en '
       'leder til at tage, og det er der, jeg har arbejdet i 20 år.', after=56)

    lp('**Elos Medtech Pinol A/S søger en Process Development Manager til en nyoprettet stilling i '
       'Gørløse**, hvor I leder efter en, der kan **»stå i spidsen for udviklingen af fremtidens '
       'produktionsløsninger«**. Afdelingen består af **projektledere, automationsspecialister og '
       'finmekanikere** og arbejder med **»investering i produktionsudstyr, udvikling af '
       'specialmaskiner, automatisering, digitalisering«** og teknisk support til produktionen. I '
       'producerer **medicoteknisk** udstyr til **dental** og **medico**, og det sker i en '
       'international medicoorganisation med høje kvalitetskrav. Stillingen handler om at '
       '**»lede og udvikle den afdeling, som er ansvarlig for vores produktionsprocesser og '
       'produktionsudstyr«** — og om at **»omsætte det strategiske automation roadmap til konkrete '
       'projekter og resultater på fabrikken«** med **»en central rolle i at sikre, at virksomhedens '
       'investeringer og teknologiske udvikling omsættes«** til noget, der kan køre i tre skift. At '
       'stillingen er ny, er en del af grunden til, at jeg søger: rammerne skal bygges, ikke '
       'overtages.', after=56)

    lp('**Fem tal, der afgør, om et udviklingsprojekt bliver en succes.**', after=46)

    lp('**Tid fra beslutning til produktion.** Det er det tal, ingen har lyst til at måle, fordi det '
       'peger på os selv og ikke på leverandøren. I Novo Nordisk var det 37 kapitalprojekter, hvor '
       'kravspecifikation, **FAT/SAT** og **IQ/OQ/PQ** skulle holdes i én plan — og hvor projektet '
       'først var færdigt, da produktionen kunne køre uden at spørge os.', after=40)

    lp('**Udbytte og scrap.** En ny proces er ikke implementeret, når den kører; den er implementeret, '
       'når udbyttet holder i tre skift. Derfor skrives baseline ned, før vi rører maskinen — og '
       '**»drive løbende forbedringer inden for kvalitet, leveringssikkerhed og produktivitet«** '
       'bliver et regnestykke med en før- og efter-måling i stedet for en fornemmelse.', after=40)

    lp('**Cyklustid.** Kapacitet er ikke en maskine, det er en cyklus gange oppetid. I 2022 lavede jeg '
       'kapacitetsmodel hver morgen for 11 samtidige anlægsprojekter og 14 medarbejdere — det er den '
       'samme disciplin, der skal ligge bag **»robuste, skalerbare og konkurrencedygtige '
       'produktionsløsninger«**.', after=40)

    lp('**Changeover og oppetid.** Hvad koster det at skifte produkt, og hvem kan gøre det om natten? '
       'Fem år i 24/7-drift har lært mig at regne på det, før udstyret bestilles — og at skrive '
       'vedligehold og reservedele ind i business casen, ikke i en fodnote.', after=40)

    lp('**Antal gange nogen ringer til engineering.** Det er det ærligste mål for, om udstyret er '
       'robust: hvor ofte produktionen må ringe, fordi noget driller. Jeg vil hellere måle det hver '
       'uge og rette årsagen end høre om det i en kvartalsrapport.', after=56)

    lp('**Det er et tværfagligt team, og det er ikke en tilfældighed.** Projektledere, '
       'automationsspecialister og finmekanikere har tre forskellige slags dømme — én plan, én '
       'styring, én tolerance. Jeg har ledet **25 specialister** i en GMP-organisation, **14 '
       'medarbejdere** i 11 samtidige projekter og **8 ansatte** i egen virksomhed, og det, der virker, '
       'er det samme: en skreven **forventningsaftale** med resultat, mandat og eskaleringsgrænse, '
       '**faglig sparring** på den svære sag og opfølgning på resultat frem for metode. Som leder skal '
       'man være **»en synlig leder, som skaber engagement og samarbejde«** — og synlig betyder på '
       'fabrikken, ikke i mødelokalet — og **projektledelse** er håndværket, mens ledelse er at få '
       'tre fagligheder til at bruge det samme håndværk.', after=56)

    lp('**Det, jeg ikke har, står her.** Jeg har ikke arbejdet i dentalindustrien og ikke drevet en '
       'afdeling for procesudvikling før. Jeg har arbejdet i **reguleret produktion** — GMP, '
       'FDA/EMA-krav, **validering** og dokumentation i Novo Nordisk — og med specialmaskiner, '
       'automation og el-teknik i 20+ år, som **elautoriseret maskinmester (LV/MV/HV)** og B.Tech i '
       'teknologiledelse. Det faglige fundament er der; branchen og den nye rolle skal læres, og det '
       'siger jeg hellere nu end i tredje samtale.', after=56)

    lp('**Jeres eget sprog er grunden til, at jeg søger.** I skriver, at **»engineering spiller en '
       'afgørende rolle i udviklingen af fremtidens produktion«**, og at man får **»frihed til at '
       'præge en ny rolle«** og kan **»sætte et markant aftryk på udviklingen af både afdelingen og '
       'fabrikken«**. I efterspørger en, der kan **»skabe struktur, overblik og fremdrift i en travl '
       'projektportefølje«**, som **»trives tæt på produktionen og motiveres af at omsætte idéer til '
       'konkrete løsninger«**, og som deltager i **»teknisk problemløsning og procesoptimering«** — '
       'ikke en, der kun leder møder. Og i en virksomhed med høje kvalitetskrav er det også en '
       'leder, der selv kan **»sikre validering og dokumentation af produktionsudstyr«** uden at skulle '
       'have det forklaret.', after=56)

    lp('**Praktisk:** Måløv, cirka 30 minutter til Gørløse, kørekort B og bil. Jeg er fysisk til '
       'stede og trives i et miljø, hvor Engineering og produktion arbejder tæt sammen — det er ikke '
       'en remote-rolle for mig. Dansk og engelsk, skriftligt og mundtligt, og kan starte efter '
       'aftale.', after=24)

    m.meta('Med venlig hilsen', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('**Teknisk leder med procesudvikling, specialmaskiner og validering** — **elautoriseret '
           'maskinmester (LV/MV/HV)** og B.Tech i teknologiledelse og maskinteknik. 20+ år i '
           'produktions- og anlægsteknik, **37 kapitalprojekter** i en GMP-fabrik, **14 medarbejdere i '
           '11 samtidige projekter** og 25 specialister. Arbejder med **roadmap**, '
           '**projektportefølje**, **business case** og **validering** — og med det, der får '
           'projektledere, automationsfolk og finmekanikere til at trække samme vej.', after=70)

    m.section('VALIDERINGEN — FRA SPECIFIKATION TIL IDRIFTSÆTTELSE')
    for label, body in [
        ('URS og kravspecifikationen',
         '**Kravspecifikation** skrevet sammen med dem, der skal bruge udstyret, med acceptkriterier og '
         'grænseflader — 37 CAPEX-projekter i en GMP-fabrik, hvor en uklar URS blev dyr tre måneder '
         'senere.'),
        ('FAT og SAT',
         '**FAT/SAT** med prøveprotokol og afvigelsesliste; udstyr, der ikke bestod, blev ikke '
         'modtaget — og leverandøren vidste det, før den tog hjem.'),
        ('IQ, OQ og PQ',
         '**IQ/OQ/PQ** med sporbarhed til kravet, dokumenteret undervejs i stedet for samlet til '
         'slut; **nul kritiske afvigelser** ved aflevering på 37 projekter.'),
        ('Afvigelser og change control',
         '**Afvigelse**, **change control** og risikovurdering med ejer og dato, og **layout** og '
         '**robot**-celler vurderet før udstyret blev bestilt — også når det betød at udskyde en '
         'idriftsættelse.'),
        ('Sporbarhed og dokumentation',
         '**Dokumentation** og **sporbarhed** som en del af arbejdet, ikke en oprydning: i pharma var '
         'det et myndighedskrav, i egen virksomhed er det, der gør en faktura og en garanti til en '
         'formalitet.')]:
        m.bullet(label, body, after=16)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · service og entreprise',
         [('Drift, økonomi og arbejdsmiljø',
           'Tilbud, materialer og dokumentation; projekter med egenkontrol og afleveringsprotokol; '
           '**APV**, LOTO og sikkerhedsrundering.')]),
        ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen',
         'Data Power Consultant ApS · København · 2024–nov. 2026 (sideløbende med ELOHVAC)',
         '4–10 personer · tekniske og industrielle applikationer',
         [('Data i beslutninger',
           'Tekniske applikationer samt **AI** i ledelsesarbejdet — rapportering, beslutningsoplæg '
           'og **KPI**-analyse; selskabet er ophørt.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('Udstyr, krav og aflevering',
           'Kravspecifikation, **FAT/SAT**, **IQ/OQ/PQ** og idriftsættelse; dokumentation bygget '
           'undervejs og nul kritiske afvigelser ved aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter',
         [('Fremdrift, kapacitet og leverandører',
           'Dagligt tavlemøde, **kapacitetsmodel** og omprioritering samme dag; leverancer styret mod '
           'aftalt dato med underentreprenører og materialer.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Biofos (Lynetten) · København · aug. 2017–jan. 2022',
         'Renseanlæg i 24/7-drift · pumper, højspændingstavler, SCADA',
         [('Drift, oppetid og energi',
           'Planlagt vedligehold og akut fejlfinding døgnet rundt; **over 40 % lavere energiforbrug** '
           'gennem måling og indregulering.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 teknikere · maskinværksted · maskiner og materiel',
         [('Maskiner, materiel og oplæring',
           'Fejlfinding, kalibrering og reparation af maskiner; indkøb og vedligehold af materiel; '
           'oplæring og opfølgning for 12 teknikere.')]),
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
    m.para('Dansk og engelsk, skriftligt og mundtligt · Persisk: modersmål · **IT**: ERP og **MES**-nære '
           'systemer, **SCADA** og **PLC**-overvågning, Excel-modeller og egne **Python**-værktøjer til '
           '**KPI** og **OEE**; **LEAN**, **5S**, **Six Sigma**-værktøjskasse · **Kørekort B og egen '
           'bil** · Måløv, cirka 30 minutter til Gørløse · Kan starte efter aftale · Referencer på '
           'forespørgsel.', after=50)

    m.models_table('OPSLAGETS KRAV — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Ledelse og udvikling af afdelingens medarbejdere',
         'Personaleledelse siden 2003: 12 teknikere, 14 medarbejdere, 25 specialister og 8 ansatte i '
         'egen virksomhed — **forventningsaftale**, **kompetenceudvikling** i en plan og MUS hvert år.'),
        ('Ejerskab for virksomhedens automationsstrategi i samarbejde med produktionsledelsen',
         '20+ år med **PLC**, **SCADA**, **CTS**/**BMS** og procesinstrumentering; har ejet tekniske '
         'vejvalg som teknisk ansvarlig og CTO og skrevet dem ned som en plan med ejer og årstal.'),
        ('Prioritering og koordinering samt sikre fremdrift af afdelingens roadmap',
         '**Roadmap** omsat til projekter med ejer og dato; prioriteringsnøgle og '
         '**kapacitetsmodel** i 11 samtidige projekter, hvor omprioriteringen skete samme dag.'),
        ('Sikring af fremdrift på investerings- og udviklingsprojekter',
         '**37 kapitalprojekter** med **business case**, rådighedsbeløb og milepæle; fuldt **P&L** i '
         'egen virksomhed siden 2023 og budgetopfølgning på alle CAPEX-sager.'),
        ('Ansvar for implementering af nyt produktionsudstyr og nye produktionsprocesser',
         'Implementering fra **URS** og **FAT/SAT** til **IQ/OQ/PQ** og driftsmodtagelse; udstyr '
         'godkendt før overtagelse og dokumenteret undervejs — nul kritiske afvigelser på 37 '
         'projekter.'),
        ('Deltagelse i teknisk problemløsning og procesoptimering',
         'Fejlfinding på maskiner, tavler og anlæg i 20+ år, og indregulering der gav **over 40 % '
         'lavere energiforbrug** — målt, ikke vurderet.'),
        ('Sikre validering og dokumentation af produktionsudstyr',
         '**Validering** under GMP/FDA/EMA på 37 projekter: krav, prøvning, afvigelser og **change '
         'control** med sporbarhed; dokumentation skrevet mens arbejdet foregik.'),
        ('Drive løbende forbedringer inden for kvalitet, leveringssikkerhed og produktivitet',
         'Baseline ned før ændringen og måling efter; **5S** og standard work indført i værksted og på '
         'anlæg, så forbedringen blev siddende og ikke blev en kampagne.'),
        ('Samarbejde med produktion, kvalitet, supply chain og øvrige engineering funktioner',
         'Tværfaglige projekter med produktion, kvalitet, indkøb og leverandører gennem 20+ år; '
         '**stakeholders** på tværs og uenighed skrevet ned som en beslutning med ejer og dato.'),
        ('Lede et tværfagligt team af projektledere, automationsspecialister og finmekanikere',
         'Er vant til faggrupper med forskellige dømme: 25 specialister i GMP, 12 teknikere i værksted, '
         '5 elektrikere og 3 lærlinge — med én ramme og tre forskellige slags faglighed.'),
        ('Ingeniør eller tilsvarende teknisk baggrund',
         '**Elautoriseret maskinmester (LV/MV/HV)** og **B.Tech** i teknologiledelse og maskinteknik '
         '(7,6/12) — teknisk baggrund på professionsbachelor-niveau med ledelse ovenpå.'),
        ('Erfaring fra medicoindustrien eller anden reguleret produktion',
         '**Reguleret produktion** i Novo Nordisk (GMP, FDA/EMA) i 2022-2024 med validering, afvigelser '
         'og dokumentationskrav; dentalindustrien er ny, den regulerede hverdag er den ikke.'),
        ('Erfaring med ledelse af ingeniører, teknikere eller procesudviklingsteams',
         'Ledet ingeniører og specialister, der vidste mere end mig om deres område: 25 specialister i '
         'en GMP-organisation og 12 teknikere i et værksted — mandat, sparring og opfølgning.'),
        ('Stærke projektledelseskompetencer og erfaring med tekniske projekter',
         '37 CAPEX-projekter, 11 samtidige anlægsprojekter og projekter i egen virksomhed med fast pris '
         'og garanti; **projektportefølje** styret på én side pr. projekt.'),
        ('Skabe struktur, overblik og fremdrift i en travl projektportefølje',
         'Én side pr. projekt med økonomi, næste milepæl og tre risici, og et ugentligt tavlemøde hvor '
         'det, der var rødt, blev besluttet samme dag — prøvet på 11 samtidige projekter i 2022.'),
        ('Trives tæt på produktionen og omsætte idéer til konkrete løsninger',
         'Har stået i værkstedet og ved maskinen, ikke kun ved tavlen: fem år i 24/7-drift og en egen '
         'virksomhed, hvor løsningen skulle virke, før den blev faktureret.'),
        ('Synlig leder, som skaber engagement og samarbejde',
         'Daglig tilstedeværelse, tavlemøde klokken 7 og en rundtur på gulvet — ikke et månedligt '
         'statusmøde; resultatet er leverancerne, ikke min egen tid i sagen.'),
        ('Fysisk til stede på fabrikken i Gørløse',
         'Bor i Måløv, cirka 30 minutter fra Gørløse, kørekort B og egen bil — på fabrikken hver dag, '
         'og det er et valg, ikke en pligt.'),
    ])

    m.section('DE FØRSTE 90 DAGE')
    for b in (
        'Gået fabrikken igennem med produktion og kvalitet og set de fem steder, hvor der oftest bliver '
        'ringet efter hjælp.',
        'Læst roadmap, investeringsliste og de seneste afvigelser igennem og lavet én porteføljeoversigt '
        'med ejer, næste beslutning og risiko pr. projekt.',
        'Sat kadencen: ugentligt tavlemøde med afdelingen, sparring med den enkelte hver anden uge og én '
        'side til produktionsledelsen om måneden.',
        'Aftalt med produktionsledelsen, hvad der skal være det første fælles mål for automatisering — '
        'og hvad der ikke skal.'):
        m.bullet('', b, after=16)

    m.section('HVAD JEG VILLE AUTOMATISERE FØRST — OG IKKE')
    for b in (
        'Først den gentagne håndtering, hvor to operatører gør det samme med to forskellige resultater, '
        'og hvor sporbarheden i dag er et stykke papir.',
        'Dernæst den maskine, der findes som den eneste af sin slags, fordi det er der, reservedele og '
        'knowhow bliver dyrest at undvære.',
        'Ikke en proces, der ikke er stabil endnu: automatisering af en ustabil proces gør bare fejlen '
        'hurtigere.',
        'Ikke et projekt uden en ejer i produktionen — hvis driften ikke vil have udstyret, bliver det '
        'en hylde.'):
        m.bullet('', b, after=16)

    m.section('DET VILLE JEG SPØRGE OM')
    for b in (
        'Hvor mange projektledere, automationsspecialister og finmekanikere består afdelingen af i dag, '
        'og hvor mange projekter kører der samtidigt?',
        'Hvordan måles udbytte, oppetid og scrap i dag — og hvem ejer de tal?',
        'Hvilke investeringer ligger allerede i 2027-budgettet, og hvor langt er de i validering?',
        'Er automationsstrategien skrevet ned i dag, og hvem har ejerskabet, indtil rollen er besat?'):
        m.bullet('', b, after=16)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_ElosMedtech_ProcessDevelopmentManager_2026.docx')
    build(out)
    print(out)
