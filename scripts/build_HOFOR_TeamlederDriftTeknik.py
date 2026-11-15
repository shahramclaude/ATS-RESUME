# -*- coding: utf-8 -*-
"""HOFOR — Teamleder til Drift Teknik, Spildevand Egen Drift (Kløvermarken).

HOFOR beder om et *motiveret CV* — derfor motiveret forside i stedet for formelt brev,
CV på side 2–3 og 90 dage + afsnit på side 4.
Policy: master/README.md — ekstrem sikkerhed, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Teamleder · Drift Teknik · SRO, SCADA og el-autorisation'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('6. november 2026')
    m.meta('HOFOR · Sektionen Spildevand Egen Drift · Teamleder til Drift Teknik · Kløvermarken, Herjedalsgade')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Motiveret CV: Teamleder til Drift Teknik', bold=True, color='1A1A1A')
    m.para('Til sektionsleder Johnny Pedersen og ledergruppen i Spildevand Egen Drift', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('Et spildevandsanlæg har ikke en dårlig dag — det har en dag, hvor en pumpe kører tør, en niveaumåler '
           'viser forkert, eller et signal i SRO-anlægget forsvinder, og hvor nogen skal beslutte sig inden for '
           'minutter. Det er den slags drift, jeg har stået i i fem år på Lynetten, og det er baggrunden for min '
           'motivation og for, at jeg søger teamlederstillingen i Drift Teknik: et fagligt stærkt team på 16 '
           'mennesker, en SCADA-udskiftning, der '
           'skal lykkes, og en digitalisering, der skal gøre hverdagen lettere for dem, der arbejder i den.',
           after=80)

    m.para('**Det, jeg kan bidrage med, er kombinationen af el-teknik, drift og ledelse.** Jeg er **elautoriseret '
           'maskinmester (LV/MV/HV)** og bærer i dag el-autorisationen i min egen virksomhed — jeg ved, hvad det '
           'betyder at have ansvaret på papiret og skulle stå ved det i virkeligheden. Jeg har arbejdet med '
           '**SRO og SCADA** som driftsleder på et kritisk 24/7-anlæg med pumper, blæsere, ventilation, '
           'transformere, koblingsanlæg og målinger, hvor styringen ikke var et IT-system ved siden af driften, men '
           'den måde driften blev udført på. Og jeg har ledet teknikere — 12 i ARJ, 14 i Ventek-Air og 8 i egen '
           'virksomhed — med den indstilling, at en leder er tættest på sin værdi, når han er tilgængelig i '
           'hverdagen og ikke kun i mødelokalet.', after=80)

    m.para('**SCADA-udskiftningen ser jeg som en driftsopgave, ikke et IT-projekt.** En ny løsning bliver kun god, '
           'hvis dem, der sidder med den om natten, har været med til at definere, hvad der skal vises, hvad der '
           'skal alarmere, og hvad der må vente. Derfor ville jeg tidligt i forløbet sikre tre ting: at drifternes '
           'egne scenarier ligger i kravspecifikationen, at der findes en plan for, hvordan vi kører videre, mens '
           'det gamle og det nye anlæg lever side om side, og at der er navngivne superbrugere i teamet — ikke kun '
           'i IT. Jeg har prøvet begge sider af den slags leverance: som driftsleder, der skulle modtage et system, '
           'og som projektleder, der skulle levere 37 kapitalprojekter med FAT/SAT og IQ/OQ/PQ til en '
           'produktionsorganisation, hvor et manglende signal betød en stoppet linje.', after=80)

    m.para('**Arbejdsmiljø og sikkerhed hænger for mig sammen med drift.** Et anlæg, hvor der bliver sprunget over, '
           'fordi der er travlt, er også et anlæg, hvor der bliver sprunget over i instruktionerne. Jeg har haft '
           'arbejdsmiljøansvaret i døgndrift: sikkerhedsinstruktioner, sikkerhedsrunder, opfølgning på '
           'nærvedhændelser og handlinger fra APV, gennemført sammen med arbejdsmiljøgruppen og ikke ovenfra. På '
           'Lynetten kom den disciplin til at hænge sammen med 5S og standard work, fordi det samme arbejde skal '
           'kunne udføres sikkert af en ny kollega som af en erfaren.', after=80)

    m.para('**Det, der gør HOFOR interessant for mig, er, at opgaven er samfundsmæssig og samtidig konkret.** '
           'Spildevandsforsyningen i hovedstaden er ikke et sted, hvor man kan vælge en løsning, der ser godt ud i '
           'et projekt, men er svær at drifte. Det passer til den måde, jeg arbejder på: beslutningen skal kunne '
           'forsvares både over for dem, der står med anlægget, og over for dem, der kigger på økonomien. Jeg har '
           'været i begge situationer — som driftsleder, der skulle leve med beslutningen i årevis, og som '
           'virksomhedsejer, der skulle betale for den.', after=80)

    m.para('**Hvad jeg vil måles på efter det første år:** at teamet ved, hvad de ejer, og at alarmer og driftsdata '
           'bliver brugt til at flytte indsatsen — ikke kun til at dokumentere, at noget gik galt. At '
           'SCADA-udskiftningen har driftens krav med fra begyndelsen og en plan for overgangen, der ikke koster '
           'forsyningssikkerhed. At arbejdsmiljøet bliver fulgt på runder og handlinger, ikke på intentioner. Og at '
           'de 16 medarbejdere stadig synes, det er et godt sted at være, når året er gået.', after=80)

    m.para('**Kontraktstyring og leverandører kender jeg fra begge sider af bordet.** Jeg har selv siddet med '
           'serviceaftaler, priser og betalingsvilkår i egen virksomhed, og jeg har som bygherre og projektleder '
           'fulgt eksterne leverancer på tid, økonomi og kvalitet. Det giver en praktisk tilgang til kontrakter: '
           'de skal beskrive, hvad der bliver leveret, hvornår det er i orden, og hvad der sker, når det ikke er — '
           'og de skal kunne læses af den tekniker, der står med opgaven.', after=80)

    m.para('**Krav skal kunne findes igen, når nogen spørger.** Efterlevelse af gældende krav — KLS, '
           'el-autorisation, arbejdsmiljø og myndighedskrav — holder kun, hvis instrukserne er skrevet, så de bliver '
           'brugt, og dokumentationen ligger der, hvor den bliver ledt efter. Jeg har arbejdet i et GMP-miljø, hvor '
           'et manglende dokument betød, at arbejdet ikke var udført, og i døgndrift, hvor svaret skulle komme med '
           'det samme; begge steder var dokumentationen det, der gjorde, at den næste kunne overtage.', after=80)

    m.para('Praktisk: jeg bor i Måløv, har **kørekort B og egen bil** og kan være på Kløvermarken og på de øvrige '
           'lokationer i hverdagen. Jeg kommunikerer sikkert på dansk og begår mig på engelsk, også i tekniske '
           'forhandlinger, og jeg kan gennemgå en **sikkerhedsgodkendelse til Fortroligt**. Jeg vil gerne høre, hvor I er i '
           'forberedelsen af SCADA-udskiftningen, og hvordan teamet i dag arbejder med alarmer og '
           'driftsoptimering — det er der, jeg ville begynde.', after=70)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Drifts- og vedligeholdelsesleder med 20+ års erfaring fra tekniske anlæg i døgndrift — **elautoriseret '
           'maskinmester (LV/MV/HV)** med B.Tech i teknologiledelse og maskinteknik. Fem år som drifts- og '
           'vedligeholdelsesleder på **Lynetten under Biofos**, et kritisk spildevandsanlæg i 24/7-drift med '
           '**SRO/SCADA**, pumper, blæsere, ventilation, transformere og koblingsanlæg; **over 40 % lavere '
           'energiforbrug** dokumenteret gennem driftsoptimering og energiledelse. Har ledet **12–14 teknikere** i '
           'to virksomheder og driver siden 2023 egen el-teknisk virksomhed med **fuldt P&L og el-autorisationen** '
           '— med **over 40 % produktivitetsløft** fra egne digitale værktøjer. Arbejdsmiljøledelse, kontraktstyring '
           'og leverandøropfølgning som en fast del af driftsansvaret.', after=80)

    m.section('DRIFT, SRO OG EL-TEKNIK')
    for label, body in [
        ('SRO og SCADA i døgndrift',
         'Driftsansvar på anlæg styret via SRO/SCADA: alarmer, målinger, regulering og fejlfinding på tværs af '
         'pumper, blæsere, ventilation og koblingsanlæg; prioritering af indsats ud fra kritikalitet og '
         'driftsforstyrrelsens betydning for forsyningen.'),
        ('El-tekniske anlæg og el-autorisation',
         'Elautoriseret maskinmester LV/MV/HV (2023); bærer el-autorisationen i egen virksomhed og har arbejdet med '
         'transformere, tavler, koblingsanlæg, motorer og beskyttelse — herunder sikkerhedsafbrydelse og '
         'arbejdsinstruktioner efter gældende krav.'),
        ('Driftsoptimering og energi',
         'Energiledelse og måling på pumpestationer og procesanlæg med over 40 % lavere forbrug; '
         'kapacitetsanalyse, flaskehalsanalyse og indregulering af pumper og blæsere som en fast del af driften.'),
        ('Digitalisering af driften',
         'Egne værktøjer i Python og Claude til tjeklister, kalkulation, databehandling og dashboards — manuelle '
         'arbejdsgange automatiseret med over 40 % produktivitetsløft; vant til at stille krav til systemer og '
         'til at være den, der tager dem i brug.'),
        ('Arbejdsmiljø og sikkerhed',
         'Arbejdsmiljøledelse i døgndrift: sikkerhedsinstruktioner, sikkerhedsrunder, APV-handlinger og opfølgning '
         'på nærvedhændelser sammen med arbejdsmiljøgruppen; 5S og standard work som grundlag for ensartet og '
         'sikker udførelse.'),
        ('Kontraktstyring og leverandører',
         'Serviceaftaler, priser og betalingsvilkår i egen virksomhed; eksterne montører og leverandører fulgt på '
         'tid, økonomi og kvalitet — og leverancer afvist, når de ikke holdt det, der stod i kontrakten.')]:
        m.bullet(label, body, after=25)

    m.models_table('SYSTEMER OG METODER', ('Område', 'Dokumenteret brug'), [
        ('Drift og overvågning',
         'SRO/SCADA, alarmer og trenddata; driftslog, afvigelser og opfølgning på tilbagevendende fejl frem for '
         'brandslukning.'),
        ('El og autorisation',
         'LV/MV/HV-anlæg, beskyttelse, dokumentation og sikkerhedsinstruktioner; el-autorisation og ansvar for, at '
         'arbejdet bliver udført af kompetente folk.'),
        ('Digitale værktøjer',
         'Python og Claude til tjeklister, data og rapporter; SAP, Excel og Power Query dagligt; superbruger på nye '
         'systemer og vant til at oversætte et behov til krav, før leverandøren bygger.'),
        ('Projekt og leverance',
         'Kravspecifikation, FAT/SAT, IQ/OQ/PQ og afleveringspakker; fremdrift, økonomi og risiko rapporteret '
         'månedligt til ledelse og bygherre.'),
        ('Ledelse og arbejdsmiljø',
         'Daglige tavlemøder, MUS og kompetenceplaner; sikkerhedsrunder, APV-handlinger og opfølgning på '
         'nærvedhændelser dokumenteret og lukket.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · el-autorisation · el-tekniske service- og entrepriseydelser',
         [('Autorisation, drift og forretning',
           'Bærer el-autorisationen og ansvaret for, at arbejdet udføres efter gældende krav; prissætning, '
           'serviceaftaler, responstider, fakturering og betalingsopfølgning; daglig drift med kunder og '
           'medarbejdere og selv med i opgaverne.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('El-systemer, leverandører og aflevering',
           'Kravsspecifikation, FAT/SAT og IQ/OQ/PQ ved modtagelse og idriftsættelse af elektriske anlæg og '
           'styringer; fremdrift, økonomi og risiko rapporteret månedligt; nul kritiske fund ved aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter · 2–10 mio. kr. pr. opgave',
         [('Kapacitet og leverance til dato',
           'Dagligt tavlemøde, kapacitets- og flaskehalsanalyse og omprioritering samme dag, når en maskine eller '
           'et menneske faldt væk; standardiserede arbejdsgange og afleveringspakker styret til deadline.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Lynetten under Biofos · København · aug. 2017–jan. 2022',
         'Kritisk spildevandsanlæg i 24/7-drift · SRO/SCADA · pumper, blæsere, ventilation, transformere, '
         'koblingsanlæg',
         [('Drift af et kritisk anlæg',
           'Kritikalitet, vedligeholdsplaner, reservedele og eksterne montører i døgndrift; vagtordning planlagt og '
           'arbejdet; SRO/SCADA-alarmer prioriteret efter betydning for forsyningen; 5S og standard work på '
           'værksted og lager; energiledelse med over 40 % lavere forbrug.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · industrielt udstyr',
         [('Teknisk service og fejlfinding',
           'Reparation, klargøring og fejlfinding på industrielt udstyr; vagtplanlægning, oplæring og opfølgning '
           'på mål for 12 teknikere.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('UDDANNELSE OG AUTORISATION')
    m.edu('B.Tech, teknologiledelse og maskinteknik',
          'Maskinmesterskolen København · 2017–2022 · gennemsnit 7,6/12')
    m.edu('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('El- og maskinteknisk konstruktion, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Køle- og ventilationsteknik · STCW', 'Mercantec 2021 · Søfartsstyrelsen 2021')

    m.section('SPROG, PRAKTIK OG REFERENCER')
    m.para('Dansk: modersmål · Engelsk: professionelt, også teknisk · Persisk: modersmål · **Kørekort B og egen '
           'bil** · Måløv, kort afstand til Kløvermarken og de øvrige lokationer · Kan sikkerhedsgodkendes til '
           'Fortroligt · Kan starte efter aftale · Referencer på forespørgsel.', after=70)

    m.models_table('DET DE EFTERSPØRGER — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Erfaring med ledelse i en teknisk driftsorganisation',
         'Fem år som drifts- og vedligeholdelsesleder på et kritisk anlæg i døgndrift; 14 medarbejdere i '
         'Ventek-Air, 12 teknikere i ARJ og 8 i egen virksomhed — daglig ledelse på gulvet.'),
        ('Teknisk uddannelse som maskinmester, elinstallatør eller ingeniør',
         'Elautoriseret maskinmester (LV/MV/HV), Sikkerhedsstyrelsen 2023; B.Tech i teknologiledelse og '
         'maskinteknik, gennemsnit 7,6/12.'),
        ('Erfaring med el-tekniske anlæg og el-autorisation',
         'Elautoriseret maskinmester med erfaring fra transformere, tavler, koblingsanlæg og motorer; bærer i dag '
         'el-autorisationen i egen virksomhed og ansvaret for, at arbejdet udføres efter gældende krav.'),
        ('Erfaring med SRO (Styring, Regulering og Overvågning)',
         'Driftsansvar via SRO/SCADA på Lynetten: alarmer, målinger og regulering af pumper, blæsere, ventilation '
         'og koblingsanlæg — og prioritering af indsats ud fra kritikalitet.'),
        ('Erfaring med arbejdsmiljøledelse',
         'Arbejdsmiljøansvar i døgndrift: sikkerhedsinstruktioner, sikkerhedsrunder, APV-handlinger og opfølgning '
         'på nærvedhændelser sammen med arbejdsmiljøgruppen; 5S og standard work indført i praksis.'),
        ('Kontraktstyring inden for teamets område',
         'Serviceaftaler, priser og betalingsvilkår i egen virksomhed; eksterne leverancer fulgt på tid, økonomi og '
         'kvalitet i 37 kapitalprojekter og 11 anlægsprojekter.'),
        ('Kommunikerer sikkert på dansk og kan begå sig på engelsk',
         'Dansk som modersmål med 20+ års teknisk og kommerciel kommunikation; engelsk professionelt, også i '
         'tekniske forhandlinger og rapportering.'),
        ('Erfaring med eller interesse for digitale værktøjer, fx Dynamics 365',
         'Egne værktøjer i Python og Claude med over 40 % produktivitetsløft; SAP, Excel og Power Query dagligt; '
         'superbruger på nye systemer og vant til at stille krav, før leverandøren bygger.'),
        ('Nærværende leder, der skaber tillid og følger op på resultater',
         'Daglige tavlemøder og synlig ledelse i døgndrift; MUS og kompetenceplaner for 12–14 medarbejdere; '
         'forandringer gennemført ved at tage dem sammen med dem, der skulle arbejde i dem.'),
        ('Kørekort og flere lokationer',
         'Kørekort B og egen bil; Måløv som bopæl med kort afstand til Kløvermarken og de øvrige lokationer i '
         'hovedstadsområdet.')])
    m.page_break()

    m.models_table('DE FØRSTE 90 DAGE — TEAMET, SCADA OG HVERDAGEN', ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'Mød alle 16 medarbejdere og de to andre teamledere; gå runder på Kløvermarken og de øvrige lokationer; læs '
         'driftsinstrukser, alarmer og de aftaler, teamet i dag leverer på; tal med IT og digitalisering om '
         'status på SCADA-udskiftningen.'),
        ('Dag 30',
         'Overblik over alarmer, tilbagevendende fejl og de opgaver der bliver udskudt — med en liste over de fem '
         'ting, der koster mest driftstid; aftalt kadence for ledelsesopfølgning med driftschefen; arbejdsmiljøets '
         'åbne handlinger gennemgået med arbejdsmiljøgruppen.'),
        ('Dag 60',
         'Teamets mål og ansvar lagt fast, så den enkelte tekniker kan se, hvad han ejer; superbrugere og '
         'driftsscenarier meldt ind til SCADA-projektet; plan for, hvordan det gamle og det nye anlæg kører side om '
         'side; kontraktoversigt med hvad der leveres, af hvem og til hvilken pris.'),
        ('Dag 90',
         'Første forbedring i drift dokumenteret med tal — fx færre gentagne alarmer eller kortere nedetid på en '
         'pumpestation; plan for langsigtet udvikling af teamets kompetence og bemanding; digitaliseringsplan med '
         'to konkrete værktøjer i brug.')])

    m.section('KVALITETEN AF EN BESLUTNING MÅLES I MINUTTER')
    m.para('I døgndrift bliver kvaliteten af en beslutning målt i minutter og i konsekvenser. Derfor er den '
           'vigtigste ledelsesopgave i Drift Teknik ikke at tage alle beslutningerne selv, men at gøre det tydeligt '
           'for den, der har vagten, hvornår han skal handle, hvornår han skal spørge, og hvad der er godt nok. Det '
           'kræver instrukser, der er skrevet af dem, der bruger dem, og en leder, der er til at få fat i.', after=80)

    m.section('SCADA-UDBSKIFTNING ER EN DRIFTSOPGAVE, IKKE ET IT-PROJEKT')
    m.para('Et nyt SCADA-system bliver kun en forbedring, hvis det bliver bedre for dem, der sidder med det klokken '
           'tre om natten. Det betyder, at drifternes scenarier skal ind i kravspecifikationen, at alarmer skal '
           'være prioriteret efter konsekvens i stedet for efter, hvad der er let at vise, og at overgangen skal '
           'planlægges, så drift og udskiftning kan løbe samtidig uden at gå på kompromis med forsyningen. Jeg har '
           'prøvet begge sider: at modtage et system som driftsleder og at levere et som projektleder med FAT/SAT '
           'og IQ/OQ/PQ.', after=80)

    m.section('EL-AUTORISATION ER ET ANSVAR, IKKE EN TITEL')
    m.para('At have el-autorisationen betyder, at man hæfter for, at arbejdet bliver udført af kompetente '
           'mennesker, efter gældende krav og med den dokumentation, der skal til. Jeg har den selv — og jeg har '
           'prøvet at stå i en situation, hvor en opgave skulle løses hurtigt, og hvor svaret var, at den skulle '
           'løses ordentligt. Det er den slags samtaler, en teamleder skal kunne tage uden at gøre det til et '
           'spørgsmål om tillid.', after=80)

    m.section('ARBEJDSMILJØ ER EN DEL AF DRIFTEN, IKKE VED SIDEN AF')
    m.para('Når der bliver travlt, er det arbejdsmiljøet, der bliver sprunget over først — og det er også der, de '
           'dyre fejl ligger. Derfor har jeg arbejdet med sikkerhed som en fast rytme: runder, instrukser, APV og '
           'nærvedhændelser, der bliver fulgt op og lukket. Det er en vane, der skal holdes ved lige, og en leder, '
           'der selv går runden.', after=80)

    m.section('DIGITALISERING SKAL GØRE ARBEJDET LETTERE, IKKE STØRRE')
    m.para('Jeg har bygget mine egne værktøjer, fordi det var hurtigere end at vente på et system — tjeklister, '
           'kalkulation, databehandling og rapporter i Python og Claude. Det har givet mig en vane, som jeg tager '
           'med i en større organisation: at spørge, hvad det er for en arbejdsgang, vi gerne vil af med, før vi '
           'spørger, hvilket system der skal løse den. Microsoft Dynamics 365 og SCADA-udskiftningen bliver kun en '
           'gevinst, hvis nogen har stillet det spørgsmål først.', after=80)

    m.section('HYDRAULIK, PUMPER OG DRIFTSOPTIMERING HAR JEG ARBEJDET MED I PRAKSIS')
    m.para('På Lynetten var driftsoptimering ikke et projekt, men en daglig disciplin: indregulering af pumper og '
           'blæsere, målinger der viste, om indstillingen holdt, og et forbrug der faldt med over 40 %, fordi vi '
           'målte og flyttede os i stedet for at gætte. Jeg kan læse hydrauliske modellers resultater og omsætte dem '
           'til '
           'indstillinger, der kan mærkes på et anlæg.', after=80)

    m.section('16 MENNESKER MED STOR FAGLIGHED KRÆVER EN LEDER, DER GIVER PLADS')
    m.para('Et team med 16 erfarne medarbejdere og stor tillid i kulturen skal ikke styres, men ledes: klare mål, '
           'mandat til at træffe beslutningen, og en leder, der tager de svære samtaler — også når beslutningen '
           'kommer oppefra, og ingen i teamet syntes om den. Engagement og samarbejde kommer ikke af, at alle er '
           'enige, men af at alle ved, hvorfor. Det er også det, jeg tager med ind i ledergruppe-arbejdet med de to '
           'andre teamledere og driftschefen.', after=80)

    m.para('Praktisk: bor i Måløv, har bil, kan gennemgå sikkerhedsgodkendelse til Fortroligt og starte efter '
           'aftale.', after=60)

    return m.save(path, title='Teamleder Drift Teknik — HOFOR, Spildevand Egen Drift',
                  subject='Drift, SRO/SCADA, el-autorisation, arbejdsmiljø og digitalisering',
                  keywords='teamleder, drift teknik, spildevand, SRO, SCADA, el-autorisation, el-tekniske anlæg, '
                           'arbejdsmiljø, kontraktstyring, digitalisering, Dynamics 365, driftsoptimering, pumper, '
                           'hydraulik, ledelse, dansk, engelsk')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_HOFOR_TeamlederDriftTeknik.docx')))
