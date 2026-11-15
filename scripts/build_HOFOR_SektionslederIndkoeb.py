# -*- coding: utf-8 -*-
"""HOFOR — Sektionsleder til Operationelt Indkøb.

Dansk leverance (opslaget er dansk) og formen er "motiveret CV": HOFOR beder ikke om en
ansøgning, men om et CV med et par ord om motivationen. Derfor side 1 = motiveret del,
side 2–3 = CV i samme dokument.
Policy: master/README.md — ekstrem sikkerhed, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Sektionsleder · Operationelt indkøb, leveringssikkerhed og stabil drift'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('6. november 2026')
    m.meta('HOFOR A/S · Operationelt Indkøb · Sektionsleder')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Motiveret CV: Sektionsleder til Operationelt Indkøb', bold=True, color='1A1A1A')
    m.para('Til områdechef Ole Egebøl', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('Leveringssikkerhed bliver ikke skabt på et indkøbskontor. Den bliver bevist i driften, når nogen står '
           'og mangler den reservedel, der holder vandet, varmen eller spildevandet i gang. Jeg har stået på den '
           'side i fem år på et kritisk anlæg i 24/7-drift, hvor et manglende lagerført emne ikke var en '
           'irritation, men en driftsforstyrrelse med en pris. Den erfaring er grunden til, at jeg søger den her '
           'sektion: indkøb er ikke en supportfunktion, der bestiller varer — det er den funktion, der gør, at '
           'driften kan holde sit løfte.', after=80)

    m.para('**Jeg ville lede sektionen på fire faste ting.** Først **kritikalitet styrer varebeholdningen**: ikke '
           'alt på lager, men det rigtige — pr. varegruppe besluttes levetid, leveringstid, alternativ og '
           'konsekvens for driften sammen med drift og lager, så beslutningen kan begrundes og ikke bare arves. For '
           'det andet **én proces fra behov til faktura**: standardiserede arbejdsgange, rammeaftaler og kataloger, '
           'der gør det nemt at gøre det rigtige, så hasteindkøb bliver den undtagelse, vi tæller og forklarer, i '
           'stedet for den normale tilstand. For det tredje **data i stedet for fornemmelser**: leveringsevne, '
           'ordrecyklustid, andel af indkøb på aftale, antal hasteindkøb og lageromsætning — fem-seks nøgletal, der '
           'bliver fulgt hver måned og faktisk brugt til at flytte noget. For det fjerde **digitalisering og '
           'standardisering sammen med medarbejderne**: automatisér det gentagne — genbestilling, ordrebekræftelser, '
           'fakturakontrol, rapportering — og tag de tolv medarbejdere og teamlederen med, for det er dem, der ved, '
           'hvor processen knækker.', after=80)

    m.para('Jeg har arbejdet med indkøb og lager, hvor det gjorde ondt, og hvor det blev målt. På **Lynetten under '
           'Biofos** var jeg drifts- og vedligeholdelsesleder på et kritisk anlæg i 24/7-drift: **reservedelsflow og '
           'lagerstyring** for pumper, blæsere, ventilation, transformere og koblingsanlæg, **5S på lageret**, '
           'leverandører der skulle levere i tide til et anlæg, der ikke kunne stoppe, og myndighedskrav der '
           'indsnævrede, hvad vi måtte købe. Leveringsevne var ikke et KPI på et møde — det var forskellen mellem en '
           'planlagt reparation og et akut stop.', after=80)

    m.para('Siden 2023 har jeg drevet **ELOHVAC** med fuldt P&L, hvor indkøb er en del af forretningen og ikke en '
           'funktion ved siden af: tilbud og kalkulation, indkøb af materialer og komponenter, leverandørvalg, '
           'priser, leveringstider, fakturering og den månedlige opfølgning på, om dækningen holdt. Jeg har prøvet '
           'at stå med en kunde, der venter, fordi en leverance ikke kom som lovet — og det er den oplevelse, der '
           'gør, at jeg hellere vil have en aftale med en leverandør, der kan måles, end en rabat, der lyder godt. '
           'Før det ledede jeg **14 medarbejdere og 11 samtidige projekter** i **Ventek-Air**, med materialestyring, '
           'udbud, underentreprenører og standardiserede arbejdsgange, og **12 teknikere** i **ARJ Engineering**, '
           'hvor lager og indkøb var det, der afgjorde, om værkstedet kunne levere.', after=80)

    m.para('Indkøb i en offentligt ejet virksomhed er en anden disciplin end indkøb i en privat, og jeg har prøvet '
           'begge. I Biofos skulle indkøb kunne tåle at blive læst af en revisor og en politiker: udbudsregler, '
           'rammeaftaler, dokumentation og sporbarhed. I min egen virksomhed handler det om margin, tempo og at '
           'vælge den leverandør, der stadig svarer om et år. Kombinationen er det, sektionen skal bruge: '
           'forretningsforståelse nok til at udfordre en indkøbskurv, og systematik nok til at gøre det dokumenterbart.',
           after=80)

    m.para('Digitalisering er det, jeg har bygget selv, når systemet ikke kunne. I dag laver jeg værktøjer i Python '
           'og Claude til kalkulation, tid, KS-tjeklister, KPI-dashboards og automatiseret rapportering med **over '
           '40 % dokumenteret produktivitetsløft** — og på Lynetten blev energiledelse på måler- og SCADA-data til '
           '**over 40 % lavere forbrug**, fordi tallene blev defineret én gang og fulgt hver måned. Det er samme '
           'metode, jeg vil bruge på indkøb: find den gentagne manuelle handling, mål hvor lang tid den tager, '
           'automatisér den, og skriv det ned, så det holder, når hverdagen presser.', after=80)

    m.para('Jeg arbejder struktureret og databaseret og trives med tværgående samarbejde og et komplekst landskab '
           'af interessenter, hvor planlægning og involvering af de rigtige mennesker er det, der gør en beslutning '
           'holdbar. Det er også derfor, jeg søger en sektionslederrolle og ikke en specialistrolle: jeg vil gerne '
           'være den, der gør en indkøbsfunktion til noget, driften regner med — og som medarbejderne oplever som en, '
           'der tager beslutningerne i tide.', after=80)

    m.para('HOFOR er et selskab, hvor indkøb har direkte betydning for en million kunders vand og varme, og hvor '
           'rammeaftaler, udbud og leverandørstyring er en del af den daglige professionalisme. Det er den slags '
           'ansvar, jeg gerne vil have — og det er en sektion med **tolv medarbejdere og en teamleder**, hvor '
           'ledelse er at sætte retning, holde en fast rytme og få fagligheden til at vokse. Jeg bor i Måløv, '
           'HOFORs hovedkontor i Ørestad er ca. en halv time væk i bil, og jeg kan starte efter aftale. Jeg vil '
           'gerne høre, hvor I i dag oplever de største forsyningsrisici, og hvordan opfølgningen på leveringsevne ser '
           'ud — det er der, jeg ville begynde.', after=80)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Drifts- og indkøbsleder med 20+ års erfaring fra kritisk infrastruktur, kapitalprojekter og teknisk '
           'service — elautoriseret maskinmester (LV/MV/HV) med B.Tech i teknologiledelse og maskinteknik. Fem år '
           'med reservedelsflow, lagerstyring og leverandører i 24/7-drift; fuldt P&L siden 2023 med indkøb, '
           'kalkulation, fakturering og dækningsopfølgning; 37 kapitalprojekter med leverandørkrav og SAP. Leder af '
           '12 til 14 medarbejdere gennem fire stillinger, med standardisering og digitalisering af arbejdsgange som '
           'fast metode — over 40 % dokumenteret produktivitetsløft.', after=80)

    m.section('INDKØB, LAGER OG LEVERINGSSIKKERHED')
    for label, body in [
        ('Leveringssikkerhed og forsyningsrisici',
         'Kritiske varegrupper identificeret efter konsekvens for driften, ikke efter pris alene: leveringstid, '
         'levetid, alternativ og genanskaffelsesmulighed dokumenteret pr. gruppe, med lagerbeholdning og beredskab '
         'aftalt med drift og lager.'),
        ('Indkøb og ordreafvikling',
         'Behov til ordre til modtagelse og faktura i én standardiseret proces; rammeaftaler og kataloger, så det '
         'rigtige køb er det nemmeste; hasteindkøb talt op og forklaret i stedet for accepteret.'),
        ('Lager og reservedele',
         'Reservedelsflow og lagerstyring på et kritisk 24/7-anlæg med 5S på lageret, kritikalitetsvurdering af '
         'beholdninger og løbende afstemning mellem lager, drift og indkøb.'),
        ('Leverandører og aftaler',
         'Leverandørvalg på pris, leveringsevne og kvalitet; aftaler med tydelige krav, opfølgning på afvigelser og '
         'eskalering, når en leverance skrider — i offentligt ejet virksomhed inden for udbudsregler og rammeaftaler.'),
        ('Data, KPI og optimering',
         'Leveringsevne, ordrecyklustid, andel af indkøb på aftale, hasteindkøb og lageromsætning fulgt månedligt; '
         'analyse i Excel og Python på ordre- og lagerdata, med forbedringer der kan måles før og efter.'),
        ('Digitalisering og standardisering',
         'Genbestilling, ordrebekræftelser, fakturakontrol og rapportering automatiseret med egne værktøjer; '
         'standardiserede arbejdsgange og procesforbedringer indført med medarbejderne, så ændringen holder efter '
         'den første måned.')]:
        m.bullet(label, body, after=25)

    m.models_table('VÆRKTØJER OG METODER', ('Opgave', 'Værktøj og dokumenteret brug'), [
        ('Indkøbsproces',
         'Behovsafdækning, ordre, modtagelse og fakturakontrol i én arbejdsgang; rammeaftaler og kataloger brugt '
         'aktivt, med undtagelser synlige og forklarede.'),
        ('Lager og kritikalitet',
         'Kritikalitetsvurdering pr. varegruppe, min./maks. beholdninger, reservedelsstrategi og 5S på lageret; '
         'afstemning med drift og vedligehold hver måned.'),
        ('Leverandørstyring',
         'Kravspecifikation, tilbudsevaluering, aftaleforløb og opfølgning på leveringsevne og kvalitet; afvigelser '
         'håndteret med ejer, dato og konsekvens.'),
        ('Data og rapportering',
         'SAP ERP til ordrer, økonomi og aktiver; Excel og Python til indkøbs- og lageranalyser samt automatiserede '
         'KPI-dashboards til ledelsen.'),
        ('Ledelse og udvikling',
         'MUS og 1:1, kompetenceplaner, rekruttering og oplæring, sygefraværsopfølgning og prioritering af '
         'opgaver — med en fast ugentlig rytme på tavlen.'),
        ('Forbedringsarbejde',
         '5S, standard work, PDCA og A3 brugt som daglig metode; hver forbedring har ejer, dato og et tal, der skal '
         'flytte sig.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · el-tekniske service- og entrepriseydelser',
         [('Indkøb, leverandører og økonomi',
           'Indkøb af materialer og komponenter, leverandørvalg og priser, kalkulation og tilbud, fakturering og '
           'månedlig opfølgning på dækning; dokumentationsflow og KPI-dashboards automatiseret med egne værktøjer.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Leverandørkrav og ordre til aflevering',
           'Krav til leverancer og dokumentation i 37 projekter, leverandørgrænseflader styret, ordrer og økonomi i '
           'SAP; aflevering med nul kritiske fund.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter · 2–10 mio. kr. pr. opgave',
         [('Materialer, udbud og leveringsevne',
           'Materialestyring og indkøb til 11 samtidige projekter, udbud og underentreprenører; daglige tavlemøder og '
           'standardiserede arbejdsgange med markant løft i leveringsevnen.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Lynetten under Biofos · København · aug. 2017–jan. 2022',
         'Kritisk procesanlæg i 24/7-drift · pumper, blæsere, ventilation, transformere, koblingsanlæg og SCADA',
         [('Reservedele, lager og forsyningssikkerhed',
           'Reservedelsflow og lagerstyring med 5S, kritikalitet og leverandører i et anlæg, der ikke måtte stoppe; '
           'myndighedskrav og dokumentation i offentligt ejet virksomhed; energiledelse med over 40 % lavere forbrug.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · industrielt udstyr',
         [('Værkstedets indkøb og drift',
           'Materialer og komponenter skaffet hjem til produktion og reparation; vagtplanlægning, oplæring og '
           'opfølgning på mål for 12 teknikere.')]),
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
    m.para('Dansk: modersmål · Engelsk: professionelt · Persisk: modersmål · Kørekort B og bil · Bor i Måløv, HOFORs '
           'hovedkontor i Ørestad ca. en halv time væk · Kan starte efter aftale · Arbejder gerne fleksibelt og bruger '
           'hjemmearbejde, når opgaven tillader det · SAP og Excel dagligt, Python til '
           'analyse og dashboards · Referencer på forespørgsel.', after=70)

    m.models_table('DET EFTERSPØRGER DE — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Personaleledelse og udvikling af medarbejdere',
         '12 teknikere, 14 medarbejdere og 11 samtidige projekter, 5 elektrikere og 3 lærlinge samt 25 specialister '
         'på tværs af 37 projekter — ledelse, MUS, oplæring og medarbejderudvikling i fire forskellige miljøer.'),
        ('Sætte retning og skabe følgeskab om fælles mål',
         'Fast ugentlig rytme på tavlen, skriftlige forventninger pr. rolle og prioriteringer, der kan gentages; '
         'forandring gennemført med medarbejderne i 24/7-drift og i et projektmiljø med 11 parallelle opgaver.'),
        ('Effektiv og professionel håndtering af indkøb og ordreafvikling',
         'Indkøb og ordreafvikling i egen virksomhed med fuldt P&L; materialestyring til 11 samtidige projekter; '
         'leverandørkrav og ordrer i SAP på 37 kapitalprojekter.'),
        ('Høj leveringssikkerhed og minimering af forsyningsrisici',
         'Reservedelsflow og lagerstyring på et kritisk anlæg i 24/7-drift med kritikalitetsvurdering, alternativer '
         'og leverandører, der skulle levere i tide — risiko håndteret før den blev et driftsstop, og forsyningskæden '
         'gennemgået hver måned mod driftsplan og anlægsprojekter, så forsyningskæde og risiko følges samlet.'),
        ('Omsætte forretningens behov til effektive indkøbsløsninger',
         'Behov afdækket sammen med driften og omsat til krav, aftaler og lagerstrategi; i egen virksomhed er '
         'indkøbsløsningen det, der afgør, om tilbuddet kan holdes.'),
        ('Koordinere på tværs af indkøb, økonomi, lager, logistik og drift',
         'Daglig berøring med drift, lager, økonomi og leverandører i 24/7-drift og på byggepladser; månedlig '
         'afstemning mellem forbrug, beholdning og økonomi.'),
        ('Procesoptimering, digitalisering og standardisering',
         '5S, standard work og PDCA indført på værksted og lager, og organisatorisk udvikling gennemført med '
         'medarbejderne; dokumentations- og rapporteringsflow automatiseret med Python og Claude, med over 40 % '
         'dokumenteret produktivitetsløft.'),
        ('Understøtte implementering af nye systemer, processer og værktøjer',
         'SAP ERP i daglig brug til ordrer, økonomi og aktiver; nye arbejdsgange indført med oplæring og en '
         'skriftlig standard, så de holder ud over den første måned.'),
        ('Datadrevet opfølgning, performance og løbende optimering',
         'KPI på tilgængelighed, nedbrud, responstider og energi i 24/7-drift; indkøbs- og lagerdata analyseret i '
         'Excel og Python med forbedringer målt før og efter.')])
    m.page_break()

    m.models_table('DE FØRSTE 90 DAGE — RISIKO, RYTME OG RAPPORTERING', ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'Individuelle samtaler med teamlederen og alle tolv: hvad de ejer, hvor processen driller, og hvad de '
         'bruger mest tid på. Gennemgå de 10 største rammeaftaler, lagerbeholdningen på de kritiske varegrupper og '
         'listen over hasteindkøb det seneste halve år.'),
        ('Dag 30',
         'Et billede af sektionen som den faktisk kører: ordrevolumen, cyklustid fra behov til levering, andel af '
         'indkøb på aftale, de tre største forsyningsrisici og de tre steder, hvor medarbejderne bruger tid på at '
         'rette fejl i stedet for at købe ind.'),
        ('Dag 60',
         'Kritikalitetsliste over varegrupper aftalt med drift og lager, med beholdning, leveringstid og alternativ; '
         'én standardiseret indkøbsproces beskrevet og taget i brug; første digitaliseringstiltag valgt ud fra, hvor '
         'der er mest manuelt arbejde.'),
        ('Dag 90',
         'Fem-seks nøgletal på en fast månedlig rapport, som sektionen selv bruger; hasteindkøb reduceret og '
         'begrundet; første automatisering i drift og målt; og en sektion, hvor alle kan svare på, hvad der er '
         'kritisk, og hvad der ikke er.')])

    m.section('LEVERINGSSIKKERHED ER EN BESLUTNING, IKKE EN BEHOLDNING')
    m.para('Det er fristende at løse forsyningsrisici ved at lægge mere på lager. Det gør bare kapitalbindingen '
           'dyr og flytter problemet. Den rigtige beslutning er pr. varegruppe: hvad koster det at mangle den, hvor '
           'lang tid tager det at skaffe den, findes der et alternativ, og hvem aftaler vi det med. Når den '
           'samtale er taget med drift og lager én gang, kan beholdningen begrundes — og så kan den også forsvares, '
           'når nogen spørger, hvorfor vi har ti af den ene og nul af den anden.', after=80)

    m.section('EN PROCESS, DER ER NEM AT FØLGE, BLIVER OGSÅ FULGT')
    m.para('Efterlevelse kommer ikke fra en politik på intranettet. Den kommer fra en proces, hvor det rigtige køb '
           'også er det hurtigste: en rammeaftale, der er nem at finde, et katalog, der virker, en godkendelse, der '
           'tager minutter, og en faktura, der går igennem første gang. Så bliver de udenomgange, der koster både '
           'pris og dokumentation, pludselig et dårligt tilbud — og så forsvinder de af sig selv.', after=80)

    m.section('TALLENE SKAL KUNNE FORKLARES AF DEM, DER BRUGER DEM')
    m.para('Et KPI, der kun findes i en rapport til ledelsen, flytter ingenting. Jeg vil have fem-seks tal, som '
           'sektionen selv kigger på hver uge: hvor mange ordrer venter, hvor lang tid tager en ordre, hvor mange '
           'hasteindkøb har vi lavet og hvorfor, hvordan ligger leveringsevnen hos de ti største leverandører, og '
           'hvordan udvikler lagerbeholdningen sig. Det er ikke rapportering for rapporteringens skyld — det er den '
           'samtale, der gør en sektion i stand til at prioritere selv.', after=80)

    m.section('DIGITALISERING SKAL FJERNE ET ARBEJDE, IKKE TILFØJE ET SYSTEM')
    m.para('Digitalisering i indkøb ender ofte som endnu et system, ingen har tid til at lære. Jeg starter det '
           'modsatte sted: hvilken opgave bliver gentaget flest gange, hvor lang tid tager den, og hvad ville der '
           'ske, hvis den kørte af sig selv i stedet. Genbestilling på faste varegrupper, ordrebekræftelser, der '
           'læses ind automatisk, fakturakontrol mod ordre og en rapport, der genererer sig selv. Jeg har bygget den '
           'slags værktøjer selv, fordi det var hurtigere end at vente på et projekt — og det er også den respekt '
           'for medarbejdernes tid, der gør, at de tager imod det.', after=80)

    m.section('EN SEKTION MED ET GODT GRIN KOMMER LÆNGERE')
    m.para('Tolv medarbejdere og en teamleder med videndeling, sparring og humor i hverdagen er ikke et blødt '
           'parameter — det er en forudsætning for at kunne sige, at en leverance skrider, og for at turde foreslå '
           'en ny måde at gøre tingene på. Jeg har ledet værksteder, hvor tonen er hård og humoren er en del af '
           'arbejdsmiljøet, og jeg har siddet i møder, hvor hvert ord blev skrevet ned. Begge steder gælder det '
           'samme: man kan sige næsten hvad som helst, hvis man mener det og kommer med en løsning. Det er den '
           'slags sektion, jeg vil lede.', after=80)

    m.section('EN FORSYNINGSVIRKSOMHED KØBER IKKE IND SOM EN FABRIK')
    m.para('HOFOR køber ind til drift, anlæg og projekter på én gang, inden for udbudsreglerne, med rammeaftaler der '
           'løber i årevis og leverandører, der skal kunne stå på mål for både pris og dokumentation. Det gør '
           'indkøbsarbejdet mere langsigtet end i en produktion: en aftale, der bliver indgået i dag, er stadig '
           'rammen om hverdagen om tre år. Derfor skal kravene skrives, så de kan efterprøves — leveringsevne, '
           'kvalitet, dokumentation og hvad der sker, hvis det skrider — og derfor skal opfølgningen være en fast '
           'rytme og ikke et møde, der bliver indkaldt, når det er gået galt.', after=80)

    return m.save(path, title='Sektionsleder, Operationelt Indkøb — HOFOR A/S',
                  subject='Operationelt indkøb, leveringssikkerhed, lagerstyring og ledelse af sektionen',
                  keywords='sektionsleder, operationelt indkøb, leveringssikkerhed, forsyningsrisici, lager, '
                           'reservedele, rammeaftaler, udbud, leverandører, standardisering, digitalisering, KPI')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_HOFOR_SektionslederIndkoeb.docx')))
