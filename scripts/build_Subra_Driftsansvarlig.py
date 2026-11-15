# -*- coding: utf-8 -*-
"""Subra A/S, Måløv — driftsansvarlig for utility/facility (deep-tech scale-up).

Form (master/FORMKATALOG.md): åbning **K** (modstriden: deres egen sætning
»Du bliver den tekniske tunge … og er samtidig med ude ved anlæggene« vendes —
et anlæg skifter ikke ejer den dag, det idriftsættes), struktur **Fem
overtagelser** (prøvekørslen · nøglebundtet · den første alarm · det første år ·
bygningen), register **Anlægskortet** (anlægsnummer, kritikalitet, interval,
målepunkt, alarmgrænse, reservedel, leverandør). Kulturfil:
jd/Subra_Driftsansvarlig_kultur.txt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Driftsansvarlig · utility, facility og vedligehold'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('13. november 2026')
    m.meta('Subra A/S · Måløv · via ansøgningsknappen i opslaget')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: driftsansvarlig for utility og facility, Subra', bold=True, color='1A1A1A')

    def lp(text, after=60):
        return m.para(text, after=after, line=236)

    # ---------------------------------------------------------------- side 1
    lp('**Et anlæg skifter ikke ejer den dag, det idriftsættes.** Det skifter ejer den dag, hvor nogen '
       'kan køre det, fejlfinde på det og forsvare det over for produktionen uden at ringe til dem, der '
       'byggede det. I skriver, at jeg skal overtage nye anlæg, **»efterhånden som de bliver '
       'færdigbygget og idriftsat«**, og at jeg skal **»kende anlæggene til bunds«** — det er ikke to '
       'opgaver, det er den samme, og den afgøres i overtagelsen. I skriver også, at jeg skal være '
       '**»den tekniske tunge i organisationen«** og samtidig være ude ved anlæggene — så det her brev '
       'handler om de dage, hvor et anlæg skifter hænder, og om hvem der kan svare klokken tre.', after=56)

    lp('**»Subra vokser!«** står der — og I skriver selv, at **»vi bygger nyt produktionsanlæg og '
       'udvider vores faciliteter i Måløv«**. Det er den sjældne situation, hvor drift ikke skal rydde '
       'op efter fortiden, men sætte standarden for det, der kommer: køl, trykluft, vandbehandling, '
       'procesventilation, procesgasser, elforsyning og OT/automatik — otte systemer, der alle skal '
       'kunne køre, den dag produktionen gør. Efter jeres Series A på 40 mio. euro og overtagelsen af '
       'THEVA i april 2026 bliver der bygget mere, ikke mindre, og en deep-tech-virksomhed som Subra — '
       '**»en dansk deep-tech scale-up«** med **»banebrydende superlederløsninger til tabsfri '
       'strømtransmission og fusionsenergi«** — kan ikke have en utility-funktion, der først bliver '
       'rigtig, når nogen har tid.', after=56)

    lp('**Fem overtagelser.** Sådan ville jeg gribe rollen an, i den rækkefølge den kommer.', after=44)

    lp('**Prøvekørslen.** En prøve, der består, fordi den er skrevet, som leverandøren kører anlægget, '
       'beviser ingenting. Jeg vil se FAT/SAT, trykprøvning og funktionstest pr. komponent — og jeg vil '
       'simulere fejlen, mens leverandøren stadig er på stedet: luk ventilen, dyp føleren, fjern '
       'spændingen, se hvad styringen gør, og skriv det ned. På Novo Nordisk overtog jeg 37 '
       'kapitalprojekter på den måde, og der var nul kritiske afvigelser ved aflevering.', after=40)

    lp('**Nøglebundtet.** Et anlæg uden reservedelsliste er et anlæg med én leverandør og ingen '
       'forhandlingsposition. Ved overtagelsen skal as-built tegninger, P&ID, el-dokumentation, '
       'kalibreringscertifikater, reservedelsliste og serviceaftale ligge i samme mappe som '
       'driftsinstruksen — ellers er det leverandørens anlæg, ikke Subras. Her hører udbud og '
       'tilbudsindhentning også hjemme: jeg har købt håndværkere og indgået serviceaftaler med '
       'responstid og pris i egen virksomhed siden 2023.', after=40)

    lp('**Den første alarm.** Driften er ikke stabil, fordi anlægget kører; den er stabil, fordi nogen '
       'ved, hvad de gør, når det ikke gør. Alarmgrænse, målepunkt, eskalering og en runbook, der kan '
       'læses af den, der har vagten — det er den del af overtagelsen, der afgør, om det lykkes at '
       '**»sikre stabil, sikker og energieffektiv drift«**. Fem år i 24/7-drift på Lynetten med '
       'pumper, højspændingstavler og SCADA har lært mig, at den time koster mest, hvor ingen havde '
       'skrevet, hvem der ringer.', after=40)

    lp('**Det første år.** Første år er målingen: forbrug pr. anlæg, baseline, afvigelse og en '
       'månedsrapport, der kan læses af både teknikere og ledelse — og af forsyningsselskabet. '
       'På Lynetten gav måling, indregulering og udskiftning af de rigtige komponenter **over 40 % '
       'lavere energiforbrug**, fordi vi vidste, hvad vi sammenlignede med. Det er også her, '
       'beslutningsoplæggene hører til: sag, alternativer, pris, risiko og anbefaling på én side — '
       'ikke en rapport, en beslutning.', after=40)

    lp('**Bygningen.** Klimaskærm, vinduer, alarmer, adgangskontrol og de eksterne håndværkere er den '
       'del af rollen, der aldrig bliver akut, men altid bliver dyr, hvis den ikke har en plan. Jeg '
       'vil drive den som et rullende program: tilstand, udbedring, udbud og et tidspunkt — og med '
       'arbejdsmiljøet med: APV, LOTO og adgang til tag og teknikrum er ikke dokumenter, det er '
       'aftaler, nogen skal holde. Det giver **»en varieret hverdag«** — og en bygning, der bliver '
       'passet, mens den bliver brugt.', after=56)

    lp('**Det, jeg ikke har, står her.** Jeg har ikke kørt kryogene anlæg, et rentrums-utility '
       'eller et superlederanlæg, og jeg har ikke haft driftsansvar for procesgasser i høj renhed. '
       'Det er ny teknik for mig. Til gengæld er køleanlæg, ventilation, trykluft, pumper, '
       'vandbehandling, LV/MV/HV og SCADA ikke teori: det har jeg stået med i drift og i '
       'idriftsættelse, og en elautoriseret maskinmester læser et P&ID og en tavle, uanset om mediet '
       'hedder nitrogen eller fjernvarme.', after=56)

    lp('**Hvorfor Subra — i jeres egne ord.** I er en **»deep-tech scale-up«**, der vil **»skabe '
       'reel, grøn forandring gennem teknologi«**, så **»strøm flyder uden begrænsninger: Rent, '
       'forbundet og CO₂-frit«**, med **»anlæg, der understøtter teknologi til den grønne '
       'omstilling«**. I tilbyder en **»central og selvstændig rolle i en vækstvirksomhed«**, hvor '
       'man kan **»sætte dit personlige præg på, hvordan drift og vedligehold bygges op fra '
       'bunden«** — og det er præcis den slags opgave, jeg søger: ikke at arve et system, men at '
       'skrive det. Og I lægger vægt på et **»højt kvalificeret team med en stærk læringskultur«**, '
       'en **»stærk tværfaglig læringskultur«**, fordi **»samarbejde er en afgørende del af vores '
       'fundament«** og fordi **»vi værdsætter diversitet«**; den slags kultur holder kun, hvis '
       'drift og projekt taler samme sprog, og det er mit arbejde at gøre.', after=56)

    lp('**Praktisk:** jeg bor i Måløv, få minutter fra Værkstedsby, så jeg kan være på anlægget, når '
       'der er brug for det — også uden for arbejdstid. Jeg er **»ikke bange for at tage '
       'fat selv«**, og jeg kan tale med teknikere og ledelse på samme dag. Dansk og engelsk, '
       'skriftligt og mundtligt. Kan starte efter aftale; referencer indhentes gerne.', after=24)

    m.meta('Med venlig hilsen', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('**Maskinmester med drift, vedligehold og idriftsættelse som fag** — **elautoriseret '
           'maskinmester (LV/MV/HV)**, B.Tech i teknologiledelse og maskinteknik og køle- og '
           'ventilationsteknik fra AMU. Siden 2017 i drift og vedligehold: fem år i 24/7-drift, '
           '**37 kapitalprojekter** overtaget fra leverandør til drift, **11 samtidige anlægsprojekter** '
           'og egen virksomhed med fuldt **P&L** — arbejder med **forebyggende vedligehold**, '
           '**energiforbrug**, **udbud** og **leverandørstyring** i det daglige.', after=70)

    m.section('ANLÆGSKORTET — HVORDAN JEG DRIVER ET ANLÆG')
    for label, body in [
        ('Anlægsnummeret',
         'Hvert anlæg har en identitet: nummer, placering, medietype og en navngiven ejer i '
         'produktionen. Uden den ejer er der ingen, der ringer, da det går galt.'),
        ('Kritikaliteten',
         'A, B eller C: hvad stopper produktionen, hvad koster en time, og hvad kan vente til mandag. '
         'Prioriteringen blev skrevet ned, ikke aftalt mundtligt — 37 anlæg i GMP-regi.'),
        ('Intervallet',
         '**Forebyggende vedligehold** planlagt efter driftstimer og tilstand, ikke kun efter '
         'kalenderen; **afhjælpende** arbejde logget med årsag, så næste interval blev rigtigt.'),
        ('Målepunktet og alarmgrænsen',
         'Hvor målingen sidder, hvad normal er, og hvornår en alarm skal eskalere — prøvet af mod en '
         'simuleret fejl, før anlægget blev overtaget; **SCADA** og **PLC** læst, ikke kun set på.'),
        ('Reservedelen og udskiftningstiden',
         'Hvilke dele ligger på hylden, hvilke har tolv ugers levering, og hvad koster det at mangle '
         'dem — listen skrevet ved overtagelsen, mens leverandøren stadig svarede.'),
        ('Leverandøren',
         '**Serviceaftale** med responstid, pris pr. besøg og navn på den, der svarer; udbud og '
         'tilbudssammenligning på pris, levetid og responstid — forhandlet med fast pris og **AB 18** '
         'i baggrunden.')]:
        m.bullet(label, body, after=16)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · entreprise og service',
         [('Service, vedligehold og leverandører',
           '**Serviceaftaler**, **udbud**, indkøb og opfølgning; **APV**, **LOTO** og arbejdsmiljø i '
           'egen virksomhed; el-tavler, styringer og **adgangskontrol** projekteret og afleveret.')]),
        ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen',
         'Data Power Consultant ApS · København · 2024–nov. 2026 (sideløbende med ELOHVAC)',
         '4–10 personer · tekniske og industrielle applikationer',
         [('Data i beslutninger',
           '**KPI**-modeller og **beslutningsoplæg** til ledelsen; selskabet er ophørt.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('Idriftsættelse og overtagelse',
           '**FAT/SAT**, **IQ/OQ/PQ**, trykprøvning og funktionstest; nul kritiske afvigelser ved '
           'aflevering, og dokumentation bygget undervejs — ikke bagefter.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter',
         [('Ventilation, HVAC og montage',
           '**Procesventilation**, kanaler og **trykluft** monteret og indreguleret; 11 anlæg '
           'koordineret med **underentreprenører** og leverandører i samme tidsplan.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Biofos (Lynetten) · København · aug. 2017–jan. 2022',
         'Renseanlæg i 24/7-drift · pumper, højspændingstavler, SCADA',
         [('Drift, anlæg og energi',
           '**Forebyggende og afhjælpende vedligehold**, **vandbehandling**, **trykluft** og '
           '**elforsyning** døgnet rundt; **over 40 % lavere energiforbrug** gennem måling og '
           'indregulering.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 teknikere · maskinværksted · maskiner og materiel',
         [('Maskiner, materiel og oplæring',
           'Fejlfinding, **kalibrering** og reparation af **værktøjsmaskiner**; indkøb og vedligehold '
           'af materiel; oplæring og opfølgning for 12 teknikere.')]),
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
    m.para('Dansk og engelsk, skriftligt og mundtligt · Persisk: modersmål · **IT**: **MS Office**, '
           '**Excel** til vedligeholdelsesplan og energiregnskab, **ERP**- og **CMMS**-arbejde, '
           '**SCADA**- og **PLC**-læsning, egne **Python**-værktøjer til **KPI** og forbrugsdata · '
           '**Kørekort B og egen bil** · Måløv, få minutter fra **Værkstedsby** · Kan starte efter '
           'aftale · Referencer på forespørgsel.', after=50)

    m.models_table('OPSLAGETS KRAV — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Driftsansvar for utility og procesanlæg: køl, trykluft, vand, HVAC, gasser, el, OT',
         'Køleanlæg og ventilation fra Ventek-Air (14 mand, 11 anlæg); trykluft, pumper og '
         'vandbehandling i 24/7-drift på Lynetten — utility-anlæg, der ikke må stå stille; '
         '**LV/MV/HV** og **SCADA/PLC** samme sted. Procesgasser i høj renhed er det nye.'),
        ('Overtage nye anlæg, efterhånden som de færdigbygges og idriftsættes',
         '37 kapitalprojekter overtaget fra leverandør til drift med **FAT/SAT** og **IQ/OQ/PQ**; 11 '
         'anlægsprojekter afleveret med dokumentation, reservedelsliste og serviceaftale.'),
        ('Sikre stabil og sikker drift',
         'Fem år i 24/7-drift uden produktionstab; **LOTO** og **APV** ført i egen virksomhed; nul '
         'kritiske afvigelser ved aflevering på 37 projekter.'),
        ('Kende anlæggene til bunds',
         'P&ID, tavletegninger og reservedelslister gennemgået ved overtagelsen; én anlægsmappe pr. '
         'anlæg med **målepunkter**, alarmgrænser og historik — 37 anlæg i GMP.'),
        ('Facility-ansvar for bygning og site: klimaskærm, vinduer, alarmer, sikring',
         '**Klimaskærm** og vinduer som udbudte opgaver med fast kontakt og et rullende program over '
         'fem år; **alarmer** og **adgangskontrol** som svagstrømsaftaler med testinterval; tilsyn på '
         'faste datoer.'),
        ('Koordinere eksterne leverandører og håndværkere',
         'Indkøb og opfølgning på håndværkere og leverandører i egen virksomhed siden 2023; 11 '
         'entrepriser koordineret i samme tidsplan som egne folk.'),
        ('Deltage i idriftsættelse og overtagelse fra projekt til drift',
         '**FAT/SAT**, tomgangsprøve og funktionstest pr. komponent; fejltilstande simuleret før '
         'overtagelse; overtagelsesprotokol med åbne punkter, ejer og frist — 37 gange i GMP.'),
        ('Planlægge og følge op på forebyggende og afhjælpende vedligehold',
         '**Vedligeholdelsesplan** på driftstimer og tilstand, ikke kun kalender; akutte fejl logget '
         'med årsag, så næste interval blev rigtigt — fem år med planlagt vedligehold og 37 anlæg '
         'dokumenteret.'),
        ('Optimere anlæg og processer — finde forbedringer, før problemerne opstår',
         '**Over 40 % lavere energiforbrug** gennem måling, indregulering og udskiftning af de rigtige '
         'komponenter; tilstand brugt som beslutningsgrundlag, før havariet.'),
        ('Teknisk sparringspartner for teknikere og kolleger i produktionen',
         'Daglig sparring med 14 montører og 5 elektrikere; faglig beslutning forklaret, så den kunne '
         'udføres af andre — 25 specialister rådgivet på Novo.'),
        ('Indstillinger, beslutningsoplæg og tekniske vurderinger til ledelsen',
         '**Beslutningsoplæg** på én side: sag, alternativer, pris, risiko og anbefaling — brugt i 37 '
         'CAPEX-sager og i egne investeringer; beslutningen dokumenteret, ikke refereret.'),
        ('Udbud, tilbud og opfølgning på serviceaftaler og leverandører',
         '**Udbud** med teknisk kravspecifikation, tilbudssammenligning på pris og levetid og '
         '**serviceaftaler** med responstid skrevet ind; forhandlet med fast pris og **AB 18**.'),
        ('Bygningsvedligehold, alarmer, adgangskontrol og sikringssystemer',
         '**Alarm**- og **adgangskontrolsystemer** som leverandøraftaler med testinterval og navn på '
         'den, der svarer; **klimaskærm** og vinduer i et rullende program; afvigelser lukket med '
         'billede og dato, 37 gange i GMP.'),
        ('Opfølge på energiforbrug og rapportere til ledelse og forsyningsselskaber',
         'Månedsrapport med forbrug pr. anlæg, baseline og afvigelse; **over 40 %** reduktion '
         'dokumenteret over tid på Lynetten; indberetning som fast rutine, ikke et årshjul.'),
        ('Uddannet maskinmester eller lignende',
         '**Elautoriseret maskinmester (LV/MV/HV)**, Sikkerhedsstyrelsen maj 2023; B.Tech i '
         'teknologiledelse og maskinteknik, 7,6/12 — maskinmesterfaget med el som speciale.'),
        ('5-10 års erfaring med drift og vedligehold af tekniske anlæg',
         'Siden 2017 i drift og vedligehold i forsyning og procesindustri: Lynetten 2017–2022 (24/7), '
         'Ventek-Air 2022 (14 mand, 11 anlæg), ELOHVAC 2023–nu med service; før det syv år i '
         'maskinværksted.'),
        ('Solid forståelse for maskinteknik, processer og bygningsinstallationer',
         'Maskinteknik fra B.Tech og værkstedet, processer fra procesindustri, GMP og renseanlæg, '
         '**bygningsinstallationer** fra el-entreprisen: VVS, ventilation, **CTS** og '
         '**BMS**-grænseflader i 20+ år.'),
        ('Vant til ansvar og beslutninger — tage fat selv',
         'Fuldt **P&L** og 8 ansatte siden 2023; beslutninger om pris, bemanding og investering taget '
         'uden at vente på et møde — og konsekvensen båret, når den var forkert.'),
        ('Formidle tekniske problemstillinger klart til teknikere og ledelse',
         'Samme sag skrevet til to læsere: driftssprog til tavlen og beslutningssprog til ledelsen; '
         'referater og indstillinger på dansk i 20+ år, engelsk på tværs af lande.'),
        ('Skabe overblik og struktur',
         'Én side pr. anlæg, én tavle pr. uge, én liste pr. leverandør; 37 projekter og 11 anlæg i '
         'samme struktur, uden at nogen skulle spørge, hvad status var.'),
        ('Erfaring med idriftsættelse af nye anlæg',
         'Idriftsættelse af 37 kapitalprojekter og 11 anlægsprojekter; overtagelsesprøver skrevet, så '
         'de også testede fejltilstande — ikke kun den normale drift.'),
        ('Erfaring med udbud og leverandørstyring',
         'Udbud, tilbudsevaluering, kontrakt og opfølgning i egen virksomhed med 8 ansatte; '
         'serviceaftaler med responstid og sanktion; **leverandørvurdering** på pris, levetid og '
         'responstid.'),
        ('Bygge drift og vedligehold op fra bunden i en vækstvirksomhed',
         'Serviceforretning og vedligehold bygget fra nul i egen virksomhed 2023; systemer valgt, '
         'ikke arvet — og tilpasset, efterhånden som opgaverne kom.'),
        ('Tæt og parallelt samarbejde med Maintenance Team Lead og Technical Manager',
         'På Novo sad projekt og drift side om side i 37 sager, og på Ventek-Air blev 11 anlæg '
         'overdraget, mens det næste blev bygget — **»et tæt og parallelt samarbejde om at sikre '
         'stabil drift og produktion«** er den samme situation set fra driftsiden.'),
        ('4+ års erfaring med Technical Support',
         '**Teknisk support** i mere end tyve år: fejlfinding på anlæg i drift, rådgivning til '
         'montører og kunder og beslutningsstøtte til ledelsen — siden 2017 som en del af '
         'driftsansvaret.'),
        ('5+ års erfaring med Maintenance Management',
         'Vedligeholdelsesansvar siden 2017: plan, interval, reservedele, leverandører og opfølgning — '
         'fem år på Lynetten og siden 2023 i egen virksomhed.'),
        ('2+ års erfaring med Machine Tools',
         'Syv år i maskinværksted hos ARJ Engineering: 12 teknikere, fejlfinding, **kalibrering** og '
         'reparation af **værktøjsmaskiner**, indkøb og vedligehold af materiel.'),
        ('Autoriseret til at arbejde i Danmark',
         'Dansk statsborger bosat i Måløv; dansk og engelsk skriftligt og mundtligt; **elautoriseret** '
         'af Sikkerhedsstyrelsen — der skal ikke søges om arbejdstilladelse.'),
    ])

    m.section('DE FØRSTE 90 DAGE')
    for b in (
        'Uge 1–2: gennemgang af alle utility-systemer med tegninger og oprindelige idriftsættelses'
        'protokoller; liste over hvad der mangler i dokumentationen, før noget andet bliver gjort.',
        'Uge 3–6: anlægskort på hvert anlæg — kritikalitet, interval, målepunkt, reservedel og '
        'leverandør — og en første prioriteret liste over forbedringer, I kan beslutte på.',
        'Måned 2–3: vedligeholdelsesplan og serviceaftaler lagt om efter kritikalitet; udbud på de '
        'opgaver der ikke har en aftale; første månedsrapport om energi og drift.',
        'Måned 3: overtagelsesstandard skrevet ned, så næste anlæg fra Factory Scaling bliver '
        'overdraget én gang, med dokumentation, prøver og en navngiven ejer.'):
        m.bullet('', b, after=16)

    m.section('DET VILLE JEG SPØRGE OM')
    for b in (
        'Hvilke anlæg er på vej fra Factory Scaling det næste år, og hvornår skal de første være i '
        'drift?',
        'Hvem ejer anlæggene i dag — produktionen, teknikerne eller projektet — og hvem ringer man '
        'kl. 03?',
        'Er der et vedligeholdelsessystem i dag, eller er planen en kalender og en mailboks?'):
        m.bullet('', b, after=16)

    m.para('**Jeg kommer gerne forbi på Værkstedsby** og ser anlæggene, før vi taler om rollen — '
           'spørgsmålene bliver bedre af at stå ved dem. Kontakt: +45 93 99 95 14 · '
           'ajlooshahram@gmail.com.', after=24)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Subra_Driftsansvarlig.docx')
    build(out)
    print(out)
