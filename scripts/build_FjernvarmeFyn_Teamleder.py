# -*- coding: utf-8 -*-
"""Fjernvarme Fyn — Teamleder for el-teamet (automatikteknikere og elektrikere), Odense.

Form (master/FORMKATALOG.md): åbning **J** (deres egen overskrift besvares direkte),
struktur **Ugen** (mandag → fredag, et bevis pr. dag), register **Maskinrummet**
(last, kapacitet, margin, reservedele). Kulturfil: jd/FjernvarmeFyn_Teamleder_kultur.txt.
Opslaget beder om *fyldestgørende CV + kort profiltekst* — side 1 er derfor et kort
brev med korte afsnit, ikke en lang ansøgning.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Teamleder · El-teamet · Vedligehold · elautoriseret maskinmester (LV/MV/HV)'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('4. november 2026')
    m.meta('Fjernvarme Fyn · Vedligeholdelsesafdelingen · Teamleder for el-teamet · Odense')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Teamleder til automatikteknikere og elektrikere', bold=True,
           color='1A1A1A')
    m.para('Til vedligeholdelseschef Søren Moltrup Rasmussen', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('**»Vil du være den faglige og menneskelige leder af et dygtigt el-team, der sikrer en '
           'stabil energiforsyning på Fyn?«** Ja. Ikke fordi jeg mangler en lederstilling, men fordi '
           'el-arbejdet hos Fjernvarme Fyn har skiftet karakter: da kullet forsvandt, og varmen i '
           'stigende grad bliver lavet på **elkedler** og **varmepumper**, er det el-teamets '
           '**rådighed**, der sætter grænsen for, hvor meget **last** anlæggene kan tage i '
           'spidsbelastningen. **19 fagfolk** — 6 **automatikteknikere**, 13 **elektrikere** og '
           'lærlingene — er den **kapacitet**, der afgør, om målet om at være **klimaneutral i 2030** '
           'bliver en plan eller en hverdag.', after=80)

    m.para('**Et el-team på et kraftvarmeværk leverer ikke timer. Det leverer margin.** Maskinrummet '
           'skal kunne tage den last, der bliver lagt på det kl. 06 en februardag, og marginen '
           'bestemmes af tre ting: om **koblingsanlægget** er prøvet, om **frekvensomformeren** blev '
           'skiftet i tide, og om **reservedelen** lå på lageret, da den skulle bruges. Den slags '
           '**vedligehold** har jeg stået i — fem år som drifts- og vedligeholdelsesleder på Lynetten '
           'under Biofos med 24/7-drift, **SRO/SCADA**, **transformere** og koblingsanlæg, og i dag '
           'som ejer af en el-virksomhed med fem **elektrikere**, tre lærlinge og '
           '**elautorisationen** i hånden.', after=80)

    m.para('**En uge i stillingen ser jeg sådan her — og det er de fem steder, jeg vil måles.**',
           after=60)

    m.para('**Mandag — planlægning og opgavefordeling.** 19 mand, seks produktionsanlæg og én plan. '
           'Mandagens **tavlemøde** skal vise, hvad der er kritisk, hvad der kan vente, og hvad der '
           'ikke kan udskydes uden at koste rådighed. Jeg har gjort det med 14 medarbejdere og 11 '
           'samtidige anlægsprojekter i Ventek-Air og med 12 teknikere i ARJ: kapacitets- og '
           'flaskehalsanalyse og omprioritering samme dag, når en maskine eller et menneske faldt '
           'væk.', after=70)

    m.para('**Tirsdag — sikker udførelse.** Arbejde med spænding på og varme i rørene er ikke '
           'sikkert, fordi nogen siger det; det er sikkert, fordi instruksen er skrevet, så den '
           'bliver brugt, og fordi der er en, der stopper arbejdet, når den ikke bliver det. Jeg '
           'bærer **elautorisationen** i dag og havde ansvaret for **arbejdsmiljø og sikkerhed** i '
           'døgndrift på '
           'Lynetten: sikkerhedsrunder, handlingsplaner fra **APV** og opfølgning på '
           'nærvedhændelser sammen med arbejdsmiljøgruppen.', after=70)

    m.para('**Onsdag — rådighed.** **Høj rådighed** er et spørgsmål om at have tænkt over, hvad der '
           'går i stykke først. Når varmen laves af el, er det effektafbrydere, frekvensomformere, '
           '**motorer** på pumperne og styringen, der afgør, hvor længe en fejl koster produktion. '
           'Jeg har prioriteret SRO-alarmer efter kritikalitet i fire år og fem måneder på et '
           '24/7-anlæg, hvor et manglende signal standsede forsyningen — og jeg har selv stået i '
           '**vagtordningen**.', after=70)

    m.para('**Torsdag — menneskerne.** **MUS**, lønsamtaler, **timegodkendelse** og **trivsel i '
           'teamet** er ikke administration ved siden af driften; det er der, man opdager, at en '
           'erfaren elektriker er på vej væk, eller at en lærling har stået for længe med den samme '
           'opgave. Jeg har holdt MUS og lavet **kompetenceplan** for 12–14 medarbejdere, oplært '
           'tre lærlinge i egen virksomhed og set, hvad det gør ved en arbejdsplads, når nogen '
           'bliver spurgt, hvad de vil lære næste gang.', after=70)

    m.para('**Fredag — opfølgning og sammenhæng.** El-teamet er ét af flere i vedligeholdelses-'
           'afdelingen; smedeteamet, lageret og planlægningen venter på de samme svar. Fredag er '
           'den dag, hvor det udskudte bliver navngivet, og hvor næste uges aftaler med de øvrige '
           'teamledere ligger fast. **Sammenhængskraft** bliver skabt af en, der kommer til mødet '
           'med en dato og ikke en undskyldning.', after=70)

    m.para('I skriver om **formål, faglighed og fleksibilitet**, om en **uformel omgangstone** og om, at '
           'omstillingen kalder på både **fællesskab og handlekraft**. '
           'Det kan en ansøgning ikke bevise; det viser sig i, hvem der bliver spurgt til råds, når '
           'planen skal lægges. Min erfaring er, at trivsel og rådighed følger samme kurve: et team, '
           'der bliver lyttet til, tager telefonen, når den ringer kl. 03.', after=70)

    m.para('**Sikker og konkurrencedygtig fjernvarme** er det, I lover fynboerne. **Grøn omstilling** '
           'er vejen derhen — og **fremtidens klimaneutrale, robuste og konkurrencedygtige '
           'forsyning** bliver kun robust, hvis vedligeholdet kan bære den last, omstillingen lægger '
           'på det. Det er den opgave, jeg søger. Jeg **flytter gerne til Odense** for stillingen og '
           'kan være på anlæggene fra første arbejdsdag, og jeg er indforstået med, at den kræver '
           '**sikkerhedsgodkendelse**.', after=70)

    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Vedligeholdelses- og driftsleder med 20+ års erfaring fra tekniske anlæg i døgndrift — '
           '**elautoriseret maskinmester (LV/MV/HV)** med B.Tech i teknologiledelse og '
           'maskinteknik. Fem år som drifts- og vedligeholdelsesleder på **Lynetten under Biofos**: '
           '24/7-drift, **SRO/SCADA**, transformere, koblingsanlæg, pumper og ventilation, og **over '
           '40 % lavere energiforbrug** dokumenteret gennem driftsoptimering. Har ledet **12–14 '
           'teknikere** i to virksomheder og driver siden maj 2023 egen el-virksomhed med **5 '
           'elektrikere, 3 lærlinge, fuldt P&L og elautorisationen** — med **over 40 % '
           'produktivitetsløft** fra egne digitale værktøjer.', after=80)

    m.section('MASKINRUMMET — LAST, MARGIN OG DRIFT')
    for label, body in [
        ('Drift og rådighed i døgndrift',
         'Driftsansvar på et kritisk anlæg i 24/7-drift: vagtordning, alarmer og prioritering af '
         'indsats efter kritikalitet, reservedelsdisciplin og opfølgning på tilbagevendende fejl i '
         'stedet for brandslukning.'),
        ('El-tekniske anlæg og autorisation',
         'Elautoriseret maskinmester LV/MV/HV (2023); arbejde med transformere, koblingsanlæg, '
         'tavler, motorer, frekvensomformere og beskyttelse — og ansvaret for, at arbejdet bliver '
         'udført af kompetente folk efter gældende krav.'),
        ('Styring, regulering og overvågning',
         'SRO/SCADA som den måde driften bliver udført på: målinger, regulering, trenddata og '
         'fejlfinding på tværs af pumper, blæsere, ventilation og koblingsanlæg.'),
        ('Arbejdsmiljø og sikker udførelse',
         'Arbejdsmiljøledelse i døgndrift: sikkerhedsinstruktioner, sikkerhedsrunder, APV-handlinger '
         'og opfølgning på nærvedhændelser; 5S og standard work som grundlag for ensartet og sikker '
         'udførelse.'),
        ('Mennesker, lærlinge og kompetence',
         'MUS og lønsamtaler for 12–14 medarbejdere; oplæring af tre lærlinge i egen virksomhed; '
         'kompetenceplaner med et konkret næste skridt og opfølgning hvert halve år.'),
        ('Økonomi, tid og leverandører',
         'Fuldt P&L i egen virksomhed: timeregistrering, timegodkendelse, fakturering og '
         'betalingsopfølgning; serviceaftaler og leverandører fulgt på tid, pris og kvalitet.')]:
        m.bullet(label, body, after=25)

    m.models_table('SYSTEMER, MÅLINGER OG METODER', ('Område', 'Dokumenteret brug'), [
        ('Drift og overvågning',
         'SRO/SCADA, alarmer og trenddata; driftslog og afvigelser; vedligeholdsplaner og '
         'reservedele styret efter kritikalitet.'),
        ('El og autorisation',
         'LV/MV/HV-anlæg, beskyttelse, dokumentation og sikkerhedsinstruktioner; elautorisation og '
         'ansvar for kompetence ved arbejde på og nær spændingssatte anlæg.'),
        ('Ledelse i hverdagen',
         'Dagligt tavlemøde, MUS, lønsamtaler, timegodkendelse og kompetenceplaner; synlig ledelse '
         'på gulvet frem for rapportering bag en skærm.'),
        ('Projekt og leverance',
         'Kravspecifikation, FAT/SAT og afleveringspakker; fremdrift, økonomi og risiko rapporteret '
         'månedligt til ledelse og bygherre i 37 kapitalprojekter.'),
        ('Digitale værktøjer',
         'Egne tjekliste- og planlægningsværktøjer i Python og Claude; SAP, Excel og Power Query '
         'dagligt; vant til at stille krav til et system, før det bliver købt.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · elautorisation · el-tekniske service- og '
         'entrepriseydelser',
         [('Faglig ledelse og autorisation',
           'Bærer elautorisationen og ansvaret for, at arbejdet udføres efter gældende krav; '
           'daglig faglig sparring med elektrikere og lærlinge, prissætning, serviceaftaler, '
           'responstider og betalingsopfølgning.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('El-systemer, leverandører og aflevering',
           'Kravspecifikation, FAT/SAT og idriftsættelse af elektriske anlæg og styringer; '
           'fremdrift, økonomi og risiko rapporteret månedligt; nul kritiske fund ved aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter',
         [('Kapacitet og leverance til dato',
           'Dagligt tavlemøde, kapacitets- og flaskehalsanalyse og omprioritering samme dag, når '
           'en maskine eller et menneske faldt væk; standardiserede arbejdsgange og '
           'afleveringspakker styret til deadline.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Lynetten under Biofos · København · aug. 2017–jan. 2022',
         'Kritisk anlæg i 24/7-drift · SRO/SCADA · transformere, koblingsanlæg, pumper, ventilation',
         [('Drift af et kritisk forsyningsanlæg',
           'Kritikalitet, vedligeholdsplaner, reservedele og eksterne montører i døgndrift; '
           'vagtordning planlagt og arbejdet; SRO-alarmer prioriteret efter betydning for '
           'forsyningen; 5S og standard work på værksted og lager; energiledelse med over 40 % '
           'lavere forbrug.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · industrielt udstyr',
         [('Teknisk service og fejlfinding',
           'Reparation, klargøring og fejlfinding på industrielt udstyr; vagtplanlægning, oplæring '
           'og opfølgning på mål for 12 teknikere.')]),
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
    m.para('Dansk: modersmål · Engelsk: professionelt, også teknisk · Persisk: modersmål · '
           '**Kørekort B og egen bil** · **Flytter gerne til Odense** for stillingen · Kan '
           'sikkerhedsgodkendes · Kan starte efter aftale · Referencer på forespørgsel.', after=70)

    m.models_table('DET OPSLAGET SPØRGER OM — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Relevant teknisk baggrund — installatør eller maskinmester',
         'Elautoriseret maskinmester (LV/MV/HV), Sikkerhedsstyrelsen maj 2023; B.Tech i '
         'teknologiledelse og maskinteknik 2017–2022 med 7,6/12; el- og maskinteknisk konstruktion '
         '2000–2003, EQF 6.'),
        ('Ledelse og udvikling af teamet',
         '19-personers team er den størrelse, jeg kender: 14 medarbejdere i Ventek-Air, 12 teknikere '
         'i ARJ og 8 i egen virksomhed — med tavlemøde, MUS og kompetenceplan som faste elementer.'),
        ('Ansvarlig leder, der skaber resultater gennem tillid og godt samarbejde',
         'Fem år som drifts- og vedligeholdelsesleder på Lynetten i 24/7-drift med vagtplan og '
         'daglig ledelse på gulvet; nul kritiske fund ved aflevering af 37 kapitalprojekter, fordi '
         'kravene blev aftalt med dem, der skulle bygge.'),
        ('Nysgerrig, opsøgende og skaber sammenhængskraft i teamet og på tværs i virksomheden',
         'I egen virksomhed har jeg siden maj 2023 bygget faste samarbejder op med leverandører og '
         'underentreprenører; i Novo Nordisk koordinerede jeg 25 specialister på tværs af fag i 37 '
         'kapitalprojekter.'),
        ('Trives med mange opgaver og holder hovedet koldt, når det går stærkt',
         '11 samtidige anlægsprojekter i Ventek-Air og 37 parallelle kapitalprojekter i Novo '
         'Nordisk; omprioritering samme dag, når en maskine eller en mand faldt væk, uden at datoen '
         'flyttede sig.'),
        ('Ansvarsfuld, struktureret og motiveret af at skabe positive forandringer',
         '5S og standard work indført på værksted og lager på Lynetten; energiledelse med over 40 % '
         'lavere forbrug over fem år; egne tjekliste- og planlægningsværktøjer med over 40 % færre '
         'manuelle timer.'),
        ('Sikker udførelse af arbejdsopgaverne',
         'Elautorisationen bæres i dag i egen virksomhed med 5 elektrikere og 3 lærlinge; '
         'arbejdsmiljøansvar i døgndrift med sikkerhedsrunder, APV-handlinger og opfølgning på '
         'nærvedhændelser dokumenteret og lukket.'),
        ('Høj rådighed på vores anlæg',
         'Fire år og fem måneder i 24/7-drift på Lynetten med vagtordning, SRO-alarmer prioriteret '
         'efter kritikalitet og en reservedelsdisciplin, der gjorde, at en fejl blev afhjulpet '
         'inden for samme vagt.'),
        ('Planlægning, opgavefordeling og opfølgning',
         'Dagligt tavlemøde med kapacitet mod last i både Ventek-Air og ARJ; vedligeholdsplaner og '
         'opgavefordeling for 12–14 teknikere med ugentlig opfølgning på udførte og udskudte '
         'opgaver.'),
        ('Timegodkendelse og anden administration',
         'Fuldt P&L i ELOHVAC siden 2023: timeregistrering, fakturering, løngrundlag og '
         'betalingsopfølgning for 8 medarbejdere; timegodkendelse og tillæg håndteret som en del af '
         'driftslederrollen.'),
        ('Trivsel i teamet samt MUS og lønsamtaler',
         'MUS og lønsamtaler gennemført for 12–14 medarbejdere i to virksomheder; kompetenceplaner '
         'på skrift med et konkret næste skridt pr. medarbejder og opfølgning hvert halve år.'),
        ('Personaleledelse og koordinering — sparringspartner for medarbejderne',
         'Daglig sparring med 12–14 elektrikere og teknikere om fejlfinding og prioritering: jeg har selv '
         'stået med instrumentet i hånden og kan vurdere, om en opgave er løst, før den bliver '
         'meldt færdig.'),
        ('Udvikle teamet til en moderne arbejdsplads, fagligt og menneskeligt',
         'Tre lærlinge oplært i egen virksomhed siden 2023; digitale tjeklister og '
         'planlægningsværktøjer indført, så opgaver og timer kan ses af hele teamet i stedet for i '
         'en mappe på et kontor.'),
        ('Kan opnå og opretholdelse af sikkerhedsgodkendelse og baggrundstjek',
         'Indforstået med baggrundsundersøgelsen; har arbejdet på kritisk infrastruktur og i '
         'GMP-miljø, hvor adgang er betinget af godkendelse, uden anmærkninger i fem år og i 37 '
         'kapitalprojekter.'),
        ('Samarbejde på tværs af virksomheden og med de øvrige teamledere',
         'I Novo Nordisk arbejdede jeg på tværs af produktion, kvalitet, vedligehold og eksterne '
         'entreprenører i 37 projekter; i egen virksomhed er samarbejde med bygherre, rådgiver og '
         'andre fag den daglige form.'),
        ('Fagligt lederskab af elektrikere, automatikteknikere og lærlinge',
         'El-teknisk baggrund med LV/MV/HV, transformere, koblingsanlæg, motorer, frekvensomformere '
         'og SRO/SCADA; leder i dag 5 elektrikere og 3 lærlinge fagligt og har oplært dem på '
         'anlæg, ikke i et klasselokale.'),
        ('Teamet er en del af vedligeholdelsesafdelingen med smedeteam, lager og planlægning',
         '19 elektrikere og automatikteknikere skal spille sammen med smedeteam, lager og '
         'planlægningsfunktion; jeg har selv siddet i den konstellation som projekt- og '
         'værkstedsleder med 14 medarbejdere og eget lager — og som driftsleder med eksterne '
         'montører og reservedelslager.'),
        ('Sammenhæng mellem strategi og indsats i vedligehold',
         'Vedligeholdet skal bære lasten af, at varmen i stigende grad laves af el. Jeg har styret '
         'vedligehold efter kritikalitet i 5 år på et 24/7-anlæg: prioriteringsmodel, ugentlig '
         'opfølgning og en liste over, hvad der blev udskudt og hvorfor.'),
        ('Stabil energiforsyning på Fyn',
         '5 år med driftsansvar på et kritisk forsyningsanlæg, hvor et stop blev bemærket i hele '
         'byen — samme type konsekvens som en fjernvarmeforsyning, der falder ud midt i '
         'spidsbelastningen i Odense.')])


    m.models_table('DE FØRSTE 90 DAGE — FRA OVERLEVERING TIL MARGIN',
                   ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'Møde med alle 19 elektrikere og automatikteknikere plus lærlingene og de øvrige teamledere '
         'i vedligehold; gennemgang af de sidste 12 måneders driftsstop, hvad de kostede i '
         'produktion, og hvad der blev gjort bagefter; runder på anlæggene med smedeteam, lager og '
         'planlægning.'),
        ('Dag 30',
         'Kritikalitetsliste pr. anlæg: hvilke el-tekniske komponenter der stopper varmeproduktionen, '
         'og hvad reservedelsstatus er på hver af dem. Tavlemødet kører fast hver morgen med '
         'kapacitet mod last, og udskudte opgaver har et navn og en ny dato.'),
        ('Dag 60',
         'Vedligeholdsplanen for el gennemgået mod produktionens lastprofil — elkedler, varmepumper '
         'og overskudsvarme prioriteret efter, hvad der koster mest rådighed pr. vedligeholdskrone; '
         'aftaler med produktion og planlægning skrevet ned, ikke aftalt mundtligt.'),
        ('Dag 90',
         'Kompetenceplan for alle 19 og lærlingene med et mål og en dato pr. person; MUS-forløbet i '
         'gang; timegodkendelse, tillæg og fakturering kørt tre måneder uden fejl; '
         'sikkerhedsrunder gennemført og APV-handlinger lukket med dokumentation.')])

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_FjernvarmeFyn_Teamleder.docx')
    build(out)
    print(out)
