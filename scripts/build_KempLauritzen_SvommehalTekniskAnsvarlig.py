# -*- coding: utf-8 -*-
"""Kemp & Lauritzen — Teknisk ansvarlig, drift og vedligehold, Gribskov Svømmehal.

Dansk opslag -> dansk dokument. Form (master/FORMKATALOG.md): åbning **R**
(gæsten kl. 06.15, der ikke ved at nogen målte vandet kl. 06.00 — og ikke skal
vide det), struktur **Hvem opdager det først** (vandet · luften · varmen ·
anlægget · sikkerheden · naboen), register **Badevandet** (klor, pH, bundfald,
cirkulation, filter, prøve, journal, tilsyn).
Kulturfil: jd/KempLauritzen_SvommehalTekniskAnsvarlig_kultur.txt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Teknisk ansvarlig, svømmehal · drift, vand og anlæg'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('14. november 2026')
    m.meta('Kemp & Lauritzen A/S · Gribskov Svømmehal · OPP og FM · teknisk ansvarlig')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Teknisk ansvarlig, Gribskov Svømmehal', bold=True, color='1A1A1A')

    def lp(text, after=44):
        return m.para(text, after=after, line=236)

    # ---------------------------------------------------------------- side 1
    lp('**Klokken 06.15 kommer dagens første gæst. Hun ved ikke, at nogen har målt vandet kl. 06.00, '
       'og hun skal ikke vide det.** Det er målet for den tekniske drift af en svømmehal: at klor, pH, '
       'temperatur, cirkulation og luft er under kontrol, før nogen kan mærke dem. Et anlæg, der '
       'fungerer, bliver ikke rost. Det bliver brugt — og det er den eneste anbefaling, der tæller her.',
       after=40)

    lp('I skriver, at en bestemt uddannelsesmæssig baggrund ikke er afgørende, og at I giver **"Grundig '
       'oplæring i svømmebadsteknik"**. Det er den rigtige rækkefølge: vandbehandling, dosering og '
       'cirkulation har jeg fra fem år på et renseanlæg i døgndrift, ventilation og affugtning fra 11 '
       'ventilationsanlæg, og el, pumper og styring fra en elautoriseret maskinmesteruddannelse. '
       'Svømmebadsteknikkens regler, journaler og tilsyn skal jeg lære — og det er netop dem, I oplærer i.',
       after=40)

    lp('**Seks ting kan gå galt i en svømmehal. Den rækkefølge, de bliver opdaget i, er forskellen på en '
       'rolig hverdag og en dårlig uge.**', after=32)

    lp('**Vandet — gæsten opdager det først.** Uklart vand, klorlugt, svie i øjnene. Prøven kl. 06 er ikke '
       'en formalitet; den er den eneste måling, der kommer før gæsten. Fire bassiner betyder fire '
       'forskellige belastninger og fire sæt grænseværdier, og derfor en fast rute: prøve, aflæsning, '
       'justering, notat — samme rækkefølge hver dag, også tirsdag kl. 05.30. På Lynetten tog jeg prøver '
       'og doserede i døgndrift i fem år; der var ingen gæster, men der var grænseværdier, og de blev '
       'overholdt, fordi de blev målt.', after=28)

    lp('**Luften — betjeningen opdager det først.** Dug på ruderne og klor i indåndingsluften er ikke et '
       'komfortproblem; det er affugtning og ventilation, der ikke følger med belastningen. Det er den '
       'slags, jeg har projekteret og serviceret: 11 samtidige ventilationsanlæg, køl og varme i samme '
       'bygning, og en styring, der skal reagere, når 40 mennesker kommer i vandet på én gang.', after=28)

    lp('**Varmen — elregningen opdager det sidst.** En svømmehal er en af de største energiforbrugere, en '
       'kommune har, og vandet skal være varmt, mens luften skal være tør. Der er penge i at måle frem for '
       'at gætte: på Lynetten sænkede vi energiforbruget med **over 40 %** ved at måle, justere setpunkter '
       'og re-kommissionere anlægget — ikke ved at skrue ned for komforten.', after=28)

    lp('**Anlægget — tilsynet opdager det først.** Et tilsyn er ikke en eksamen; det er en gennemgang af, '
       'om hverdagen er dokumenteret. Journal, prøveresultater, egenkontrol, kemikaliehåndtering og '
       'instrukser skal stå der, når nogen spørger — også den dag den faste person har ferie. Jeg har '
       'skrevet den slags dokumentation på 37 kapitalprojekter, så den kunne læses af en, der ikke var med.',
       after=28)

    lp('**Sikkerheden — ingen opdager det, før det er galt.** Redningsudstyr, kemikalierum, nødbruser, '
       'afspærring ved elarbejde og en APV, der bliver brugt og ikke bare gemt. Sikkerhed er en række '
       'små beslutninger, der bliver taget ens hver dag, og det er der, en holdspiller bliver synlig.',
       after=28)

    lp('**Naboen — læreren opdager det.** Nordstjerneskolen ligger i direkte forbindelse med svømmehallen, '
       'og I beskriver selv arbejdet som et tæt samarbejde med en kollega. Fælles teknik betyder fælles '
       'aftaler: hvem tager telefonen, hvad gør vi ved et alarmopkald fra skolen i skoletiden, og hvordan '
       'deler vi dagens opgaver, så ingen af os står alene med en akut opgave. Jeg har prøvet det modsatte '
       'og ved, hvad det koster: to organisationer, én kalender, og en skriftlig aftale om, hvad der går '
       'forud.', after=40)

    lp('**Det, der sjældent står i et opslag — og som afgør hverdagen.** En svømmehal stopper ikke på '
       'grund af det store anlæg. Den stopper på en føler, en pakning eller en ventil, der koster mindre '
       'end en arbejdsdag. Derfor et lille lager af netop det, der stopper driften først, to telefonnumre '
       'til hver leverandør, og en liste over, hvad der må vente til mandag. Det er den slags, ingen '
       'lægger mærke til, når det virker — og alle spørger til, når det ikke gør.', after=40)

    lp('**Hvorfor Kemp & Lauritzen, i jeres egne ord.** **"Danmarks førende digitale og grønne '
       'teknikpartner"** med 3.000 medarbejdere, ejet af en fond, der **"investerer i vores medarbejdere og '
       'samfundet som helhed"** — og en virksomhed, der kalder sine folk **"Kemperne"** og vandt **"Årets '
       'virksomhed med mere end 500 medarbejdere"**, og som vil være **"én af Danmarks bedste '
       'arbejdspladser"** med **"gode udviklingsmuligheder"**. Det, der afgør det for mig, er noget andet: '
       'I skriver, at det hele handler om **"ordentlighed"**, at I vil **"skabe plads til forskellighed"**, '
       'at **"Vi tager ansvar i alt vi gør"**, at I leder efter **"sans for drift, fejlfinding og '
       'ansvar"** og byder på **"Et stærkt fællesskab og ordentlig arbejdskultur"**. En stilling med **"eget '
       'anlæg"** og **"Tæt sparring med kompetente kolleger i Facility Management"** i et **"OPP og FM '
       'Team"** på 18 er præcis den kombination, jeg søger: selvstændigt ansvar uden at være alene.',
       after=40)

    lp('**Praktisk.** Jeg bor i Måløv, har kørekort B og egen bil og kører til Gribskov på godt trekvarter. '
       'Dansk er førstesprog, engelsk arbejdssprog. Jeg kan tiltræde hurtigst muligt og er klar til at '
       'starte med oplæring i svømmebadsteknik — jeg ringer gerne til Erik Rasmussen på 61 91 78 00 eller '
       'Morten Østergaard på 25 26 44 08, hvis et par spørgsmål er hurtigere end en ansøgning.', after=16)

    m.meta('Med venlig hilsen', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('**Teknisk ansvarlig med vandbehandling, ventilation og el i bagagen** — elautoriseret '
           'maskinmester (LV/MV/HV), AMU i køle- og ventilationsteknik. Fem år som drifts- og '
           'vedligeholdelsesleder på et renseanlæg i **24/7-drift** med prøvetagning, dosering, SCADA og '
           'pumper; 11 samtidige ventilationsanlæg i Ventek-Air; **37 kapitalprojekter** hos Novo '
           'Nordisk; eget selskab med fuldt **P&L** siden 2023. Måler, justerer, dokumenterer — hver dag.',
           after=64)

    m.section('BADEVANDET — SÅDAN HOLDER JEG ET ANLÆG STABILT')
    for label, body in [
        ('Prøven',
         'Fast rute, fast tid, fast rækkefølge: prøve, aflæsning, justering, notat. En prøve, der bliver '
         'taget, når der er tid, er ikke en prøve — den er en undskyldning.'),
        ('Cirkulationen',
         'Vandet skal rundt, før det bliver behandlet. Pumpetryk, flow og vandstand fortæller, om '
         'anlægget arbejder, eller om det bare kører.'),
        ('Doseringen',
         'Klor og pH styres efter måling, ikke efter fornemmelse. Kemikalier håndteres med '
         'sikkerhedsdatablade, aflåst rum og en instruks, der også gælder om søndagen.'),
        ('Luften',
         '**Affugtning** og **ventilation** i en svømmehal er en del af vandbehandlingen: fugt og klor i '
         'luften slides på bygningen og på menneskene.'),
        ('Journalen',
         'Det, der ikke står skrevet, findes ikke ved et **tilsyn**. Dokumentation skrives samme dag, i et '
         '**vedligeholdelsessystem** — ikke i hukommelsen.'),
        ('Leverandøren',
         'Faste **leverandører** på filtre, kemi og pumper, med to numre til hver, og en **reservedel** på '
         'lager til det, der stopper driften først.'),
    ]:
        m.bullet(label, body, after=16)

    m.section('ERFARING')
    jobs = [
        ('Ejer / teknisk direktør', 'ELOHVAC ApS · København · maj 2023–nu',
         '8 ansatte · 5 elektrikere og 3 lærlinge · fuldt P&L',
         [('Teknik, økonomi og ansvar i egen virksomhed',
           'Ventilations-, køle- og elopgaver for erhverv og bolig: fejlfinding, udbedring, indkøb og '
           '**budget**; **P&L** og ansvar for otte medarbejdere.'),
          ('AI i den daglige drift',
           'AI-værktøjer i kalkulation og dokumentation: **over 40 % produktivitetsløft**, målt.')]),
        ('Medejer og CTO / teknisk ansvarlig, AI-afdelingen',
         'Data Power Consultant ApS · København · 2024–nov. 2026 (sideløbende)',
         '4–10 medarbejdere · tekniske og industrielle applikationer',
         [('Systemer, data og idriftsættelse',
           'Tekniske løsninger fra krav til arkitektur, datamodel og idriftsættelse, afsluttet med '
           'dokumentation og overdragelse.')]),
        ('Senior commissioning-ingeniør / projektleder, elsystemer',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('Aflevering, dokumentation og kvalitet',
           '**FAT/SAT**, **IQ/OQ/PQ** og aflevering på 37 projekter; nul kritiske afvigelser, og '
           'dokumentationen skrevet mens arbejdet blev udført.')]),
        ('Projekt- og værkstedsleder', 'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 montører · 11 samtidige anlæg · værksted og lager',
         [('Ventilation, køl og varme i drift',
           '11 samtidige **ventilationsanlæg** med **affugtning**, køl og varme; fejlfinding, '
           'indregulering og aflevering sammen med montørerne.')]),
        ('Drifts- og vedligeholdelsesleder', 'Biofos (Lynetten) · København · aug. 2017–jan. 2022',
         'Renseanlæg i 24/7-drift · SCADA, PLC, HV-tavler',
         [('Vandbehandling, prøver og døgndrift',
           '**Prøvetagning**, dosering, filtre og pumper i døgndrift; **SCADA** og alarmer; vagtordning og '
           '**arbejdsmiljø**; **over 40 % lavere energiforbrug** gennem måling og re-kommissionering.')]),
        ('Elektromekanisk tekniker / produktionsformand', 'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 teknikere · maskinværksted · maskiner og udstyr',
         [('Maskiner, reservedele og oplæring',
           'Fejlfinding, kalibrering og reparation; indkøb og vedligeholdelse af udstyr; oplæring og '
           'opfølgning på 12 teknikere.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=16)

    m.section('UDDANNELSE OG AUTORISATION')
    m.edu('B.Tech, teknologiledelse og maskinteknik',
          'Maskinmesterskolen København · 2017–2022 · karakter 7,6/12')
    m.edu('Autoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('Køle- og ventilationsteknik · AMU', 'Mercantec 2021 · STCW, Søfartsstyrelsen 2021')
    m.edu('El- og maskinteknisk konstruktion, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6')

    m.section('SPROG, IT OG PRAKTIK')
    m.para('Dansk (førstesprog) · engelsk (arbejdssprog) · persisk (modersmål) · **IT**: **SCADA** og '
           '**PLC**-loganalyse, styring og alarmer, **vedligeholdelsessystem** og sagsstyring, '
           '**Excel** til målinger og energiopfølgning, AI-værktøjer til dokumentation · **Kørekort B og '
           'egen bil** — Gribskov på godt trekvarter fra Måløv · Tiltrædelse hurtigst muligt.', after=44)

    m.models_table('STILLINGEN SOM UDBUDT — HVAD JEG BRINGER', ('Krav', 'Dokumentation'), [
        ('Dagligt ansvar for den tekniske drift af Gribskov Svømmehal',
         'Daglig teknisk ansvarlig i eget selskab siden 2023 og driftsleder på et anlæg i døgndrift i fem '
         'år: ansvaret for at anlægget kører, er ikke nyt for mig.'),
        ('Vandprøve inden dagens første gæst, hverdage kl. 06.00 og tirsdag kl. 05.30',
         'Faste prøveruter i døgndrift i fem år, hvor prøven blev taget, før anlægget blev belastet — en '
         'rutine, der holder, fordi den har et klokkeslæt og en fast rækkefølge.'),
        ('Daglig kontrol og prøvetagning af vandkvalitet i 4 bassiner',
         '**Prøvetagning** og **vandbehandling** med **klor**, pH, filtre og **cirkulation** fra '
         'renseanlægget; fire bassiner er fire sæt grænseværdier, ikke fire gange den samme prøve.'),
        ('Overvågning og opfølgning på tekniske installationer',
         '**SCADA**, alarmer og loganalyse i døgndrift: jeg læser historikken for at finde ud af, hvornår '
         'et anlæg begyndte at ændre sig — ikke kun at det er stoppet.'),
        ('Identificere og håndtere driftsudfordringer',
         'Fejlfinding på pumper, ventiler og **tekniske installationer** med fem spørgsmål: hvad er '
         'symptomet, hvornår startede det, hvad ændrede sig, hvad er risikoen, og hvad gør vi nu.'),
        ('Kontakt og koordinering med eksterne leverandører',
         '**Leverandør**- og underentreprenørkontakt i eget selskab og i 37 kapitalprojekter: aftale, '
         'fremmøde, pris og en skriftlig bekræftelse bagefter.'),
        ('Løbende bidrage til forbedringer',
         '**Forbedringer** med tal på: **over 40 % lavere energiforbrug** på Lynetten gennem måling, '
         'justering af setpunkter og re-kommissionering af anlægget.'),
        ('Samarbejde med ejendomsteknikeren om opgaver på Nordstjerneskolen',
         'Fælles teknik kræver fælles aftaler: hvem tager telefonen, hvad gør vi ved et alarmopkald i '
         'skoletiden, og hvordan fordeles dagens opgaver, når begge har travlt.'),
        ('Sikre at anlægget kører stabilt, energieffektivt og sikkert',
         '**Stabil drift** som rutine: faste runder, målinger og en grænseværdi, der udløser handling, før '
         'gæsten mærker noget. **Energi** måles hver måned, og **energieffektiv** drift er et krav, der '
         'trækker samme vej som sikkerheden.'),
        ('Indgå i OPP og FM Teamet på 18 engagerede kolleger',
         'Vant til at være en del af et team uden at sidde i samme lokale: 25 specialister på 37 '
         'projekter, 14 montører på 11 anlæg, og et team på otte i egen virksomhed.'),
        ('Vedligeholdelsessystemer og lovgivning om svømmebadsteknik og ejendomsdrift',
         '**Vedligeholdelsessystem** og dokumentation fra drift og fra 37 projekter; svømmebadsteknikkens '
         '**lovgivning** og journaler er det, jeg skal oplæres i — og det, jeg lærer hurtigst.'),
        ('Har teknisk forståelse og lysten til at lære',
         'Elautoriseret **maskinmester** med LV/MV/HV, AMU i køle- og ventilationsteknik og tyve års '
         'praktisk fejlfinding; nyt fagstof har aldrig været problemet, nyt udstyr har været det sjove.',
         ),
        ('Har erfaring med drift, vedligehold eller tekniske installationer',
         '**Drift** og **vedligehold** af renseanlæg i døgndrift, 11 ventilationsanlæg, el- og '
         'varmeanlæg og eget selskabs kundeanlæg — med **fejlfinding** som den daglige disciplin.'),
        ('Har fokus på kvalitet, sikkerhed og stabil drift',
         '**Kvalitet** målt og dokumenteret: nul kritiske afvigelser ved aflevering på 37 projekter; '
         '**sikkerhed** med APV, sikkerhedsgennemgang og **LOTO** i døgndrift.'),
        ('Kritisk nysgerrig og stiller spørgsmål for at finde de bedste løsninger',
         '**Kritisk nysgerrig** i praksis: jeg spørger, hvorfor setpunktet er, som det er, og har flere '
         'gange fundet besparelsen ved at måle efter i stedet for at tro på tavlen.'),
        ('Arbejder selvstændigt og tager ansvar for egne opgaver',
         '**Selvstændig** i praksis: egen virksomhed siden 2023 og nattevagter uden leder til stede i fem '
         'år — beslutningen taget, meldt ud og skrevet i logbogen.'),
        ('En holdspiller, som bidrager til den gode stemning',
         '**En holdspiller** i ordets praktiske forstand: tager de kedelige opgaver, deler viden i stedet '
         'for at holde den, og sørger for at nye folk ikke står alene med en akut opgave.'),
        ('Har kørekort kategori B',
         '**Kørekort B** og egen bil; Måløv til Gribskov på godt trekvarter, og klar til udkald og '
         'leverandørbesøg uden at skulle planlægges dagen før.'),
        ('Kan formulere sig godt på dansk',
         'Dansk er førstesprog: journaler, instrukser, tilsynsdokumentation og korrespondance med '
         'leverandører og kommune — skrevet og talt, uden oversættelse undervejs.'),
        ('Det er en fordel at være bosiddende i Nordsjælland',
         'Bosat i Måløv med fast pendling nordpå og bil til rådighed; mødetiden kl. 05.30 er ikke et '
         'problem, når der er under trekvarter til døren.'),
    ], widths=(2500, 7846))

    m.section('NÅR NOGET STOPPER')
    for label, body in [
        ('Sikr og afspær',
         'Først menneskene og vandet: bassinet lukkes eller afspærres, og gæsterne får en besked, der '
         'kan forstås, før rygterne kommer. En lukket bassin er en dårlig dag; en åben bassin med '
         'forkert vand er en sag.'),
        ('Find årsagen i historikken',
         'Alarmer, flow, tryk og dosering fortæller, hvornår det begyndte — ikke kun at det stoppede. Jeg '
         'læser loggen, før jeg ringer til nogen, så leverandøren får et symptom og ikke en formodning.'),
        ('Midlertidig løsning, aftalt og skrevet ned',
         'En midlertidig drift er acceptabel, hvis den er besluttet, tidsbegrænset og skrevet ned med '
         'navn. Det var reglen i døgndrift, og den gælder også her.'),
        ('Del og bestil',
         'Delen bestilles samme dag, og notatet i **vedligeholdelsessystem**et bliver lavet, mens sagen er '
         'varm — så den næste, der får den samme fejl, kan slå den op i stedet for at starte forfra.'),
    ]:
        m.bullet(label, body, after=16)

    m.section('UGEN DELT MELLEM TO ADRESSER')
    for label, body in [
        ('Om morgenen hører svømmehallen til først',
         'Prøve, runde og justering er faste punkter mellem 05.30 og 08.00, før hallen fyldes. Den tid '
         'bliver ikke flyttet for et møde på skolen; den er forudsætningen for, at der er et anlæg at '
         'møde ind til.'),
        ('Resten af dagen er fælles',
         'Opgaverne på Nordstjerneskolen aftales med kollegaen om morgenen og justeres, når noget ændrer '
         'sig. To mand, to adresser og én liste, som begge kan se — så ingen opdager en opgave først, når '
         'den er blevet akut.'),
        ('Når telefonen ringer fra skolen',
         'Skoletid er hverdag mellem 8 og 15, og der er mennesker i lokalerne. Et alarmopkald fra skolen '
         'går foran en planlagt opgave i svømmehallen — men ikke foran en prøve, der ikke er taget endnu.',
         ),
    ]:
        m.bullet(label, body, after=16)

    m.section('DE FØRSTE 90 DAGE')
    for b in (
        'Uge 1–2: gå ruten med den, der har passet anlægget — prøver, dosering, runder og journal — og '
        'læs tilsynsrapporterne. Ret ingenting, før jeg kender udgangspunktet.',
        'Uge 2: kemikaliehåndtering og sikkerhedsinstrukser gennemgået med den, der bestiller kemi — '
        'hvad står der, hvad gør vi, og hvem må røre hvad. Det er den slags, et tilsyn spørger om først.',
        'Uge 3–6: egen daglig rutine med klokkeslæt og kontrolpunkter, og et ugentligt notat til '
        'driftschefen: målinger, afvigelser, hvad der er bestilt, hvad der venter.',
        'Måned 2–3: reservedelsliste og leverandørliste for det, der kan stoppe driften, med to kontakter '
        'på hver; journal og instrukser gennemgået, så de kan læses af en vikar.',
        'Måned 2: aftalen med kollegaen på Nordstjerneskolen prøvet i praksis — en uge, hvor vi bytter '
        'opgaver, så begge ved, hvad den anden laver, når der er travlt eller ferie.',
        'Måned 3: energiforbruget gennemgået time for time mod belastning, med de tre første justeringer '
        'foreslået — og en fast aftale med kollegaen på Nordstjerneskolen om, hvem der tager hvad.'):
        m.bullet('', b, after=16)

    m.section('DET VILLE JEG SPØRGE OM')
    for b in (
        'Hvordan er ansvaret delt mellem kommunen som bygherre, OPP-selskabet og Kemp & Lauritzen på det '
        'her anlæg?',
        'Hvilke driftsudfordringer har anlægget haft det seneste år — vandkvalitet, fugt eller '
        'energiforbrug?',
        'Hvordan ser weekend- og helligdagsdækningen ud, og hvem tager telefonen, når noget stopper kl. '
        '22?',
        'Hvad vejer tungest i jeres vurdering efter det første år — vandkvaliteten, energien eller '
        'samarbejdet med skolen?'):
        m.bullet('', b, after=16)

    m.para('**Jeg kommer gerne forbi Gribskov Svømmehal og går en runde med den, der har anlægget i dag.** '
           'Kontakt: +45 93 99 95 14 · ajlooshahram@gmail.com. Referencer gives på forespørgsel — nærmeste '
           'leder på Lynetten og projektledelsen hos Novo Nordisk.', after=20)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_KempLauritzen_SvommehalTekniskAnsvarlig.docx')
    build(out)
    print(out)
