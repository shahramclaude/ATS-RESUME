# -*- coding: utf-8 -*-
"""airteam a/s, Hillerød — Projektleder til større ventilationsprojekter (dansk opslag).

Dansk opslag -> dansk dokument. Form (master/FORMKATALOG.md): åbning **Q** (den
anden dato: den i kontrakten og den i hovedet på dem, der skal bruge bygningen),
struktur **Kanalvejen** (syv stationer fra indtag til drift, hver med sin egen
måde at gå galt på), register **Indreguleringen** (tryk, luftmængde, spjæld,
måling, tolerance, afvigelse).
Kulturfil: jd/airteam_ProjektlederVentilation_kultur.txt.
Tidligere ansøgning til samme virksomhed: #223 (Service-projektleder) — intet
genbrugt, hverken åbning (B), struktur (Problemkataloget) eller register
(Kundeservice).
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Projektleder, ventilationsentrepriser · projektering til aflevering'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('14. november 2026')
    m.meta('airteam a/s · Hillerød · Projektleder til større ventilationsprojekter')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Projektleder, ventilationsentrepriser', bold=True, color='1A1A1A')

    def lp(text, after=56):
        return m.para(text, after=after, line=236)

    # ---------------------------------------------------------------- side 1
    lp('**Der står to datoer i et ventilationsprojekt. Den ene i kontrakten. Den anden i hovedet på dem, '
       'der skal bruge bygningen.** Kontrakten kan holdes til timen og bygningen være en skuffelse — den '
       'morgen personalet møder ind i et lokale, hvor luften er tung, eller hvor det suser i en kanal, så '
       'ingen kan holde møde. Det er den anden dato, jeg styrer efter. **"Bygbarhed"** er ikke en '
       'egenskab ved tegningen; det er en egenskab ved den bygning, nogen skal leve i bagefter. '
       '**"Effektiv eksekvering, høj kvalitet og godt samarbejde"** er de tre ting, der afgør, om den '
       'dato holder.', after=44)

    lp('Og som I selv skriver: **"Når den fungerer, mærkes den næsten ikke. Når den svigter, påvirkes '
       'indeklima, energi og drift."** Derfor står der ikke "montage" i min plan, men måling, '
       'indregulering og drift — det er dér, anlægget bliver bedømt, og der en projektleder enten har '
       'styr på sit projekt eller ikke har.', after=44)

    lp('**Kanalvejen fra indtag til drift — syv stationer, hver med sin egen måde at gå galt på.**',
       after=40)

    lp('**Indtaget — kravet, ikke tegningen.** Her afgøres projektet: hvilket indeklima skal rummene '
       'have, og hvad står der egentlig i kravet? Et **"sundt indeklima"** er ikke et aggregat i '
       'kælderen; det er m³/s i det enkelte rum. I jeres arbejdsmetode står der: **"Vi udfordrer '
       'specifikationer og forenkler løsninger"**, når samme funktion kan fås med bedre totaløkonomi — '
       'det er også min praksis, og den kræver, at nogen har regnet på alternativet, før bygherren '
       'beslutter.', after=24)

    lp('**Aggregatet — pladsen og leveringstiden.** Aggregatet bliver det første problem: det er stort, '
       'skal løftes ind ad en åbning, der måske ikke findes endnu, og har leveringstid. Indkøb er derfor planlægning, ikke administration: behovsafdækning '
       'tidligt, tilbudsindhentning med tekniske forbehold, ordrebekræftelse med dato — ellers venter '
       'montørerne på noget, der ikke kommer. I Ventek-Air styrede jeg 14 montører og 11 samtidige '
       'anlæg, og værkstedet var lageret: rækkefølgen var planen.', after=24)

    lp('**Kanalerne — bygbarheden og de andre fag.** En kanal bliver ikke dyr i projekteringen. Den '
       'bliver dyr den morgen, den skal forbi en bjælke, der ikke var tegnet, eller gennem et hul, som '
       'håndværkeren har lavet et andet sted. Derfor koordinerer jeg uge for uge og ikke måned for '
       'måned: hvem er i lokalet, hvad skal der være plads til, og hvornår kan det hele lade sig gøre. '
       'Jeg har siddet på begge sider af den grænseflade — som entreprenør og som driftens projektleder.', after=24)

    lp('**Spjældene — økonomien og ændringerne.** Et spjæld, ingen har reguleret, er ikke et teknisk '
       'problem; det er et økonomisk. Sådan er ændringer også: hver skal have et nummer, en pris og en '
       'dato, og siger nogen ja på pladsen, skal den i budgettet samme uge. Jeg fører budgetopfølgning '
       'måned for måned med restliste, reserver og usikkerheder — og har stået med fuldt **P&L** i eget '
       'selskab, hvor en forkert kalkulation ramte mig.', after=24)

    lp('**Rummene — menneskene, der skal bruge det.** **"Kundens virkelighed først"** betyder i praksis, '
       'at brugerne får besked, før larmen kommer, og at bygherren hører om forsinkelser fra mig, ikke '
       'fra pladsen. Det er også der, man skal **"skabe struktur, fremdrift og gode relationer"** — i den '
       'rækkefølge. Fem år på Lynetten, hvor driften ikke kunne stoppe, lærte mig, at en uges varsling og '
       'en fast kontaktperson gør en indgriben til en aftale.', after=24)

    lp('**Målingen — kvaliteten, dokumentationen og arbejdsmiljøet.** Afleveringen er en måling, ikke en '
       'underskrift: luftmængder, tryk, lyd, regulering og en dokumentation, der viser hvad der blev '
       'bygget. Hos Novo Nordisk blev dokumentationen skrevet, mens arbejdet blev udført — **FAT/SAT** og '
       '**IQ/OQ/PQ** — og 37 projekter gik til aflevering uden kritiske afvigelser. Arbejdsmiljøet er '
       'samme disciplin: sikkerhedsgennemgang før opstart, **LOTO** og APV i drift.', after=24)

    lp('**Driften — det første år.** **"Vi forlader ikke pladsen før arbejdet er færdigt"** — for et '
       'ventilationsanlæg betyder "færdigt" også det første år: eftersyn, garanti og den telefon, der kommer i februar.'
       ' Den ringer til projektlederen, hvis '
       'driften ikke har fået andet at ringe til. Derfor afleverer jeg med driftsinstruktion, '
       'indreguleringsrapport og en navngiven kontakt — og jeg tager selv telefonen det første år.',
       after=48)

    lp('**Hvor erfaringen kommer fra.** Ventilationen har jeg fra Ventek-Air, hvor jeg som projekt- og '
       'værkstedsleder styrede 11 samtidige anlæg og 14 montører, og fra AMU i køle- og '
       'ventilationsteknik. Resten kommer fra 37 kapitalprojekter, fra fem år i 24/7-drift og fra en '
       'elautoriseret maskinmesteruddannelse, så jeg ved, hvad en ændring gør ved tavlen.', after=44)

    lp('**Hvorfor airteam, i jeres egne ord.** **"Danmarks største ventilationsentreprenør"** siden 1998 '
       'med **400+ medarbejdere**, **15 byer** og **6.000+ projekter**. Det, der imponerer mig, er **"Et projekt. '
       'Mange kompetencer."** og jeres egen sætning om, at **"Vi regner på alternativerne, når det '
       'skaber værdi"** i stedet for at sælge det samme anlæg to gange. I kalder det en **"kundeorienteret '
       'virksomhedskultur"** med et **"engageret team af dygtige medarbejdere"**, **"frihed under '
       'ansvar"**, **"nærværende ledelse"**, **"tydelige forventninger"** og en **"sund, attraktiv og '
       'udviklende arbejdsplads"** med **"airteam Academy"** — og **"faglig stolthed"** som krav.',
       after=44)

    lp('**Praktisk.** Jeg bor i Måløv, kører til Hillerød på godt en halv time i egen bil og kan '
       'tiltræde hurtigst muligt. Dansk er førstesprog, engelsk arbejdssprog — og jeg ringer gerne til '
       'Michael B. Demant på 22 77 53 44.', after=16)

    m.meta('Med venlig hilsen', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('**Projektleder med ventilations-, el- og driftsteknisk baggrund og fuldt økonomiansvar** — '
           'elautoriseret maskinmester (LV/MV/HV), AMU i køle- og ventilationsteknik, B.Tech i teknologi'
           'ledelse og maskinteknik. 11 samtidige ventilationsanlæg og 14 montører i Ventek-Air; **37 '
           'kapitalprojekter** med rådgivere og bygherrer hos Novo Nordisk; fem år som drifts- og '
           'vedligeholdelsesleder i 24/7-drift; eget selskab med fuldt **P&L** og otte ansatte siden '
           '2023. Projektering, fremdrift, økonomi og aflevering — på samme tavle.', after=64)

    m.section('INDREGULERINGEN — SÅDAN LÆSER JEG ET PROJEKT')
    for label, body in [
        ('Trykket',
         'Et anlæg, der ikke kan holde trykket, er et anlæg, der ikke kan levere luftmængden. Det viser '
         'sig først ved målingen — hvis nogen har planlagt en.'),
        ('Mængden',
         'Kravet er m³/s i det enkelte rum, ikke et aggregat i kælderen. Projekteringen starter i '
         'rummene og regner baglæns gennem kanalerne.'),
        ('Spjældet',
         'Det, der kan reguleres, kan også stå forkert. Indregulering er en aftale om, hvem der må røre '
         'det, og en rapport der viser udgangspunktet.'),
        ('Målingen',
         'Afleveringen er dokumentation, ikke et håndtryk: luftmængder, lyd, tryk og en driftsinstruktion, '
         'der kan bruges af en, der ikke var med i byggeriet.'),
        ('Afvigelsen',
         'En afvigelse, der bliver skrevet ned samme dag, koster en beslutning. En, der bliver opdaget '
         'ved afleveringen, koster en ombygning — og som regel en tillægssag.'),
        ('Det første år',
         'Garantiåret er den rigtige test. Eftersyn, justering og en telefon, der bliver taget — af mig, '
         'indtil driften har sin egen kontakt.'),
    ]:
        m.bullet(label, body, after=16)

    m.section('ERFARING')
    jobs = [
        ('Ejer / teknisk direktør', 'ELOHVAC ApS · København · maj 2023–nu',
         '8 ansatte · 5 elektrikere og 3 lærlinge · fuldt P&L',
         [('Ventilation, el og økonomi i samme virksomhed',
           'Ventilations- og elopgaver for erhverv og bolig: kalkulation, tilbud, indkøb, fremdrift og '
           'aflevering; **budget** og **P&L** med ansvar for otte medarbejdere og kundernes tidsfrister.'),
          ('AI i den daglige drift',
           'AI-værktøjer i kalkulation, dokumentation og projektering: **over 40 % produktivitetsløft**, '
           'målt og ikke påstået.')]),
        ('Medejer og CTO / teknisk ansvarlig, AI-afdelingen',
         'Data Power Consultant ApS · København · 2024–nov. 2026 (sideløbende)',
         '4–10 medarbejdere · tekniske og industrielle applikationer',
         [('Arkitektur, datamodel og idriftsættelse',
           'Kundeløsninger fra kravafdækning til arkitektur, datamodel, integration og idriftsættelse, '
           'afsluttet med dokumentation og overdragelse.')]),
        ('Projekt- og værkstedsleder', 'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 montører · 11 samtidige anlæg · værksted og lager',
         [('11 anlæg, 14 montører, én plan',
           'Daglig kapacitetsplan for 11 samtidige ventilationsanlæg; underentreprenører og leverandører '
           'koordineret, så grænseflader ikke blev til forsinkelser; værkstedet styrede materiel og '
           'rækkefølge.')]),
        ('Senior commissioning-ingeniør / projektleder, elsystemer',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('Aflevering, dokumentation og kvalitet',
           '**FAT/SAT**, **IQ/OQ/PQ** og aflevering på 37 projekter; nul kritiske afvigelser, og '
           'dokumentationen skrevet mens arbejdet blev udført.')]),
        ('Drifts- og vedligeholdelsesleder', 'Biofos (Lynetten) · København · aug. 2017–jan. 2022',
         'Renseanlæg i 24/7-drift · SCADA, PLC, HV-tavler',
         [('24/7-drift, arbejdsmiljø og energi',
           'Vagtordning og **arbejdsmiljø** i døgndrift; planlagt vedligehold og rodårsagsopfølgning; '
           '**over 40 % lavere energiforbrug** gennem måling og re-kommissionering.')]),
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
    m.para('Dansk (førstesprog) · engelsk (arbejdssprog) · persisk (modersmål) · **IT**: kalkulation og '
           '**budget** i Excel, projekt- og sagsstyring, **ERP**, **SCADA** og **PLC**-loganalyse, '
           'AI-værktøjer til kalkulation og dokumentation · **Kørekort B og egen bil** — Hillerød på godt '
           'en halv time fra Måløv · Tiltrædelse hurtigst muligt.', after=48)

    m.models_table('STILLINGEN SOM UDBUDT — HVAD JEG BRINGER', ('Krav', 'Dokumentation'), [
        ('Lede og styre ventilationsentrepriser fra projektering til aflevering',
         'Projekt- og værkstedsleder i Ventek-Air med 11 samtidige ventilationsanlæg: projektering, '
         'montage, koordinering og aflevering — fra tegning til indreguleret anlæg.'),
        ('Have det overordnede ansvar for økonomi, budgetopfølgning og byggestyring',
         'Fuldt **P&L** og **budget** i eget selskab siden 2023, kalkulation og tilbud på hver sag, '
         'månedlig budgetopfølgning med restliste, reserver og usikkerheder.'),
        ('Projektere og optimere ventilationsløsninger med interne og eksterne parter',
         '**Projektering** af **energieffektive** ventilations- og elinstallationer i ELOHVAC, AMU i køle- og '
         'ventilationsteknik, og alternativberegninger forelagt bygherre før beslutning.'),
        ('Planlægge, følge op på og styre tid, fremdrift og kvalitet gennem hele projektet',
         'Daglig kapacitetsplan for 14 montører og 11 anlæg; ugeseddel med færdiggrad, restliste og '
         'kritiske leverancer — **projektorganisation** og fremdrift gennemgået med pladsen hver uge.'),
        ('Koordinere udførelsen med øvrige fag og sikre godt samarbejde på byggepladsen',
         '**Koordinering** med el, VVS, tømrer og rådgivere på 11 samtidige **entrepriser** og i '
         '37 kapitalprojekter, hvor grænsefladen blev aftalt på byggemødet og skrevet ned samme dag.'),
        ('Sikre god kommunikation og effektiv koordinering med kollegaer, montører og underentreprenører',
         'Én ugentlig tavlegennemgang med **montører** og **underentreprenører**: hvad skal ske, hvad '
         'mangler, hvem venter på hvem — og et navn på hver opgave.'),
        ('Sikre en professionel og løsningsorienteret dialog med bygherrer, rådgivere og samarbejdspartnere',
         'Atten år med **bygherre**- og **rådgiver**dialog: alternativer regnet igennem, ændringen '
         'prissat før den blev accepteret, og svaret givet skriftligt med en dato på.'),
        ('Håndtere indkøb af materialer, behovsafdækning, tilbudsindhentning og rettidig levering',
         '**Indkøb** med behovsafdækning før tilbud, to leverandører på kritiske komponenter og '
         'leveringstid ind i planen — værkstedet i Ventek-Air fungerede som lager og forkant.'),
        ('Sikre korrekt dokumentation, kvalitetssikring og efterlevelse af arbejdsmiljøkrav',
         '**Dokumentation** skrevet mens arbejdet blev udført, **kvalitetssikring** med nul kritiske '
         'afvigelser på 37 projekter, **arbejdsmiljø** med sikkerhedsgennemgang, APV og LOTO.'),
        ('Identificere risici, træffe beslutninger og implementere tiltag, der holder projektet på sporet',
         'Risikoliste med ejer og dato, gennemgået på hvert byggemøde: de tre største risici har altid '
         'et tiltag og en frist, før de bliver forsinkelser.'),
        ('Bidrage til løbende optimering af processer, projektmetoder og interne arbejdsgange',
         'Standarder indført og brugt: én kalkulationsskabelon, én afleveringsmappe, én ugeseddel — og '
         'AI i kalkulation og dokumentation med over 40 % målt produktivitetsløft.'),
        ('Have fokus på projekternes bygbarhed og gennemførelse til den aftalte kvalitet, tid og pris',
         '**Bygbarhed** afprøvet før montage: montagerækkefølge, løfteveje og kanalføring gennemgået med '
         'montørerne, inden materialerne blev bestilt — også når bygherren kører **totalentreprise**.'),
        ('Kvalitetsbevidst, beslutningsdygtig og stærk teknisk profil med flair for projektstyring',
         'Elautoriseret **maskinmester** med LV/MV/HV, AMU i ventilation og 37 projekter bag sig: '
         'beslutninger taget på pladsen med teknisk begrundelse, ikke på fornemmelse.'),
        ('Uddannelse som ingeniør, maskinmester, bygningskonstruktør eller tilsvarende teknisk baggrund',
         '**Maskinmester** (B.Tech, 7,6/12) med elautorisation LV/MV/HV — en teknisk uddannelse med '
         'både projektering, økonomi og drift i pensum.'),
        ('Flere års erfaring med ventilationsentrepriser og økonomi- og budgetansvar',
         'Ventilation fra Ventek-Air (11 samtidige anlæg, 14 montører) og AMU i køle- og '
         'ventilationsteknik; **økonomi** fra eget selskabs **P&L** siden 2023 og fra 37 kalkulerede '
         'kapitalprojekter.'),
        ('Solid erfaring med projektering, projektledelse og styring af større byggeprojekter',
         '**Projektering** og **projektledelse** i 37 parallelle kapitalprojekter hos Novo Nordisk med '
         'rådgivere, bygherre og myndigheder; 11 samtidige anlæg i Ventek-Air med egen økonomi.'),
        ('Stærke forhandlingsevner og kompetencer inden for projektøkonomi, planlægning og koordinering',
         '**Forhandling** af underentreprenør- og leverandøraftaler i eget selskab; **projektøkonomi** '
         'med dækningsgrad pr. sag, **planlægning** i uger og **koordinering** på tværs af fag.'),
        ('Kan skabe overblik, struktur og sikre fremdrift i samarbejde med projektets aktører',
         'Ét projektkort pr. sag: tid, penge, kvalitet, risici og næste handling — samme struktur på 11 '
         'anlæg og 37 projekter, så overblikket ikke afhang af hukommelse.'),
        ('Kommunikerer klart og formår at opbygge tillidsfulde relationer på tværs af fag',
         'Skriftligt og mundtligt på dansk og engelsk, med montører, rådgivere og direktionsniveau; '
         'relationer bygget på, at det jeg lovede på mødet, stod i referatet bagefter.'),
        ('Arbejder selvstændigt, er initiativrig og trives i en hverdag, hvor tingene kan ændre sig',
         'Egen virksomhed drevet selvstændigt siden 2023, og 24/7-drift i fem år hvor planen blev '
         'skiftet tre gange før frokost — beslutningen taget, meldt ud og skrevet ned.'),
        ('Har et løsningsorienteret mindset',
         '**Løsningsorienteret** i praksis: når en kanal ikke kan være der, findes der en anden vej, et '
         'andet tryk eller en anden fordeling — og alternativet bliver prissat, før det bliver valgt.'),
        ('Gode danskkundskaber i skrift og tale',
         'Dansk er førstesprog: tilbud, referater, byggemødenoter og korrespondance med bygherre, '
         'rådgiver og myndighed — skrevet og talt, uden oversættelse undervejs.'),
    ], widths=(2500, 7846))

    m.section('DE FØRSTE 90 DAGE')
    for b in (
        'Uge 1–2: læs de igangværende sagers kontrakter, kalkuler og afleveringsmapper; en tur på hver '
        'plads med den montør, der har været længst på sagen. Ret ingenting endnu.',
        'Uge 3–6: ét projektkort pr. sag — tid, penge, kvalitet, risici og næste handling — og en '
        'ugentlig tavlegennemgang med pladsen, så fremdriften kan ses og ikke bare fortælles.',
        'Måned 2–3: indkøbsplan for de næste seks måneder med leveringstider og to leverandører på '
        'kritiske komponenter; risikoliste med ejer og dato på hver sag.',
        'Måned 3: afleveringsstandarden skrevet ned — måling, indreguleringsrapport, driftsinstruktion og '
        'navngiven kontakt det første år — og prøvet på én sag.'):
        m.bullet('', b, after=16)

    m.section('DET VILLE JEG SPØRGE OM')
    for b in (
        'Hvilke entrepriseformer og projektstørrelser kører Hillerød-afdelingen nu, og hvem er '
        'bygherrerne?',
        'Hvor i projektet bliver økonomien typisk svær — i kalkulationen, i ændringerne eller i '
        'afleveringen?',
        'Hvordan måler I selv, om en aflevering var god — og hvem spørger brugerne bagefter?',
        'Hvilke leverandører og underentreprenører er faste, og hvor er der plads til at prøve noget '
        'nyt?'):
        m.bullet('', b, after=16)

    m.para('**Jeg kommer gerne forbi Hillerød og ser en af de sager, der kører nu** — og tager gerne '
           'en snak med den montør, der har været længst på pladsen. Kontakt: +45 93 99 95 14 · '
           'ajlooshahram@gmail.com.', after=20)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_airteam_ProjektlederVentilation.docx')
    build(out)
    print(out)
