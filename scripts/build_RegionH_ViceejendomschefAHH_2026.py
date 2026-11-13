# -*- coding: utf-8 -*-
"""Region Hovedstaden, Center for Ejendomme — Drift og Byg AHH:
Viceejendomschef, Amager og Hvidovre Hospital (rekruttering: Dansk HR Service).

Form (master/FORMKATALOG.md): åbning **D** (tallet: to millioner kvadratmeter,
som ingen leder — man leder faglederne), struktur **Ordlisten** (retning ·
prioritering · snitflade · opfølgning · tillid · stedfortræder), register
**Driftsdøgnet** (nyt: vagt, udkald, alarm, responstid, eskalering, logbog,
overlevering). Kulturfil: jd/RegionH_ViceejendomschefAHH_2026_kultur.txt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Viceejendomschef · teknisk drift, fagledere og projekter'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('13. november 2026')
    m.meta('Region Hovedstaden · Center for Ejendomme, Drift og Byg AHH · '
           'Amager og Hvidovre Hospital · via Dansk HR Service')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Viceejendomschef, Drift og Byg AHH', bold=True, color='1A1A1A')

    def lp(text, after=60):
        return m.para(text, after=after, line=236)

    # ---------------------------------------------------------------- side 1
    lp('**Center for Ejendomme varetager omkring to millioner kvadratmeter.** Ingen leder to '
       'millioner kvadratmeter. Man leder de fagledere, der hver dag holder bygninger, '
       'installationer og projekter sammen på Amager og Hvidovre Hospital — og den del af arbejdet '
       'består i at gøre det muligt for dem, ikke i at gøre deres arbejde. Det er hele grunden til, '
       'at jeg søger denne rolle og ikke en projektstilling.', after=56)

    lp('**Drift og Byg AHH har ansvar for bygninger, tekniske anlæg, vedligeholdelse og projekter '
       'på Amager og Hvidovre Hospital** og de tilknyttede matrikler, og **»hospitalets tekniske '
       'drift står aldrig stille«**. Som viceejendomschef bliver jeg **»ejendomschefens nærmeste '
       'ledelsesmæssige sparringspartner og stedfortræder«** med den daglige ledelse af faglederne '
       'og supportområdet — **»en rolle med mange snitflader og et stort ledelsesmæssigt ansvar«**. '
       'Center for Ejendomme hedder fra 1. januar 2027 **Ejendomme og Byggerier**, når Region '
       'Hovedstaden og Region Sjælland lægges sammen, og så skal arbejdsgange og styring kunne bære '
       'en større organisation. Og I spørger selv, om man vil være med til at sikre, at '
       '**»mennesker, fagligheder og opgaver arbejder i samme retning«** — det er den sætning, jeg '
       'har læst flest gange.', after=56)

    lp('**Seks ord, stillingen består af.**', after=46)

    lp('**Retning.** **»Din opgave er ikke at kende alle tekniske løsninger i detaljen«** — men en '
       'leder skal stadig kunne sige, hvad der vejer tungest: patientsikkerhed og driftsstabilitet først, derefter myndighedskrav, '
       'derefter tidskritiske projekter. Den nøgle skal stå skrevet, så faglederne kan bruge den uden '
       'at spørge — det var den, jeg brugte i fem år i 24/7-drift.', after=40)

    lp('**Prioritering.** **»Skabe klare prioriteringer«** og sikre, at **»beslutninger og aftaler '
       'bliver omsat til handling«**, er ikke en mødedisciplin, men en log: hver beslutning har en '
       'ejer, en dato og en linje, og de fem, der haster, står på én side ved ledelsesmødet. 37 '
       'kapitalprojekter blev ikke afsluttet, fordi nogen huskede dem.', after=40)

    lp('**Snitflade.** Mellem drift, projekter og hospitalets behov ligger de aftaler, ingen ejer. '
       'Hvert væsentligt forhold får en ejer og en varslingsvej, så en afbrydelse bliver aftalt i '
       'uger i stedet for opdaget om morgenen. Det er den del af **»at holde sammen på de '
       'væsentligste snitflader mellem drift, projekter og hospitalets behov«**, der afgør, om en '
       'uge bliver dyr.', after=40)

    lp('**Opfølgning.** Økonomi, ressourcer og risici skal på bordet, før de bliver et problem: én '
       'side om måneden med fremdrift, forbrug, de tre største risici og de beslutninger, jeg mangler '
       '— med en skreven grænse for, hvornår jeg handler selv, og hvornår ejendomschefen skal med. '
       '**»Følge udviklingen i økonomi, ressourcer og risici«** er en kadence, ikke en egenskab.',
       after=40)

    lp('**Tillid.** Fagledere med 20 års erfaring skal have plads, ikke instrukser. Det, jeg kan '
       'bidrage med, er rammen: en skreven **forventningsaftale** om resultat, mandat og '
       'eskaleringsgrænse, sparring på den svære sag og opfølgning på resultat — ikke på metode. Jeg '
       'har ledet specialister, der vidste mere end mig om deres område, og **»skabe følgeskab blandt '
       'erfarne fagpersoner«** er en arbejdsform, ikke en undskyldning.', after=40)

    lp('**Stedfortræder.** Det er en skreven aftale, ikke en titel: hvilke beslutninger jeg træffer, '
       'når ejendomschefen ikke er der, hvem der orienteres bagefter, og hvordan vi overlapper uden at '
       'efterprøve hinanden. Det aftaler man i den første uge — ikke den dag, det bliver nødvendigt.',
       after=56)

    lp('**Det, jeg ikke har, står her.** Jeg har ikke været viceejendomschef, ikke ledet fagledere på '
       'dette niveau, og ikke arbejdet på et hospital. Det tætteste er fem år som driftsleder i '
       '24/7-drift, 37 kapitalprojekter i en GMP-fabrik, 14 medarbejdere i 11 samtidige projekter, '
       '25 specialister — og en egen virksomhed med 8 ansatte og fuldt **P&L** siden 2023. Jeg er '
       '**elautoriseret maskinmester (LV/MV/HV)** og kan læse en tavle, en ventilationskurve og en '
       'alarmliste, men jeg skal ikke være den, der ved mest om den tekniske løsning. Det er ikke et '
       'forbehold; det er beskrivelsen af rollen, som I selv har skrevet den.', after=56)

    lp('**Jeres eget sprog er grunden til, at jeg søger.** I vil have en, der kan **»skabe retning, '
       'når forskellige hensyn, fagligheder og behov mødes«**, og som kan **»give faglederne plads '
       'til at drive deres områder og samtidig fastholde en fælles retning«** — **»sætte retning og '
       'være tydelig«**, men også **»opbygge tillid og få mennesker med dig«** og **»stille de '
       'rigtige spørgsmål, skabe klarhed«**, når man ikke selv er den, der ved mest. I efterspørger '
       '**»ro og dømmekraft«**, fordi **»stabil drift har stor betydning«** for dem, bygningerne '
       'tjener, og I lover **»reel ledelsesmæssig bredde«** og et **»solidt ledelsesmæssigt '
       'fundament«**. Det er den slags ledelse, jeg har arbejdet med i femten år — og den, jeg gerne '
       'vil prøve kræfter med her.', after=56)

    lp('**Praktisk:** Måløv, cirka 25 minutter til Amager og 20 minutter til Hvidovre, kørekort B og '
       'bil, kan starte efter aftale. Dansk og engelsk, skriftligt og mundtligt.', after=24)

    m.meta('Med venlig hilsen', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('**Teknisk leder med 24/7-drift og kapitalprojekter i bagagen** — **elautoriseret '
           'maskinmester (LV/MV/HV)**, B.Tech i teknologiledelse og maskinteknik. 20+ år i tekniske '
           'installationer, fem år som **driftsleder** i 24/7-drift, **37 kapitalprojekter** i en '
           'GMP-fabrik og **14 medarbejdere i 11 samtidige projekter**. Arbejder med '
           '**prioriteringsnøgle**, **beslutningslog**, **snitfladekort** og **ledelsesrapport på én '
           'side** — og med det, der får erfarne fagpersoner til at trække samme vej.', after=70)

    m.section('DRIFTSDØGNET — VAGT, TAVLE OG MENNESKER')
    for label, body in [
        ('Vagten og udkaldet',
         '**Vagt**, **udkald** og **responstid** som **KPI** i fem år: akut fejlfinding døgnet rundt '
         'på et renseanlæg med pumper, højspændingstavler og SCADA — og en eskaleringsvej, der stod '
         'på papir, før alarmen lød.'),
        ('Tavlen og logbogen',
         'Dagligt tavlemøde, **logbog** og **overlevering** mellem skift; i 2022 en **kapacitetsmodel** '
         'for 11 samtidige projekter og 14 medarbejdere, så omprioriteringen skete samme dag og ikke '
         'ugen efter.'),
        ('Eskaleringen',
         'Skreven grænse for, hvad der besluttes i driften, hvad der kræver en leder, og hvad der skal '
         'til ejendomschefen — samme model som beslutningsoplæggene på to sider i Novo Nordisk, hvor '
         '37 CAPEX-sager blev afgjort i tide.'),
        ('Økonomien',
         'Fuldt **P&L** i egen virksomhed siden 2023, budget- og ressourcestyring i 11 anlægsprojekter '
         'og 37 kapitalprojekter med rådighedsbeløb; **risici** gennemgået månedligt med navn og '
         'modtræk.'),
        ('Menneskene',
         '**Forventningsaftale** pr. medarbejder, **MUS** hvert år, opfølgning på **sygefravær**, '
         '**kompetenceudvikling** i en plan og **APV**/**arbejdsmiljø** som faste punkter — 12 '
         'teknikere, 14 medarbejdere, 25 specialister, 8 ansatte.')]:
        m.bullet(label, body, after=16)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · service og entreprise',
         [('Drift, økonomi og arbejdsmiljø',
           'Tilbud, **udbud**, materialer og **dokumentation**; **APV**, LOTO og sikkerhedsrundering; '
           'leverancer med egenkontrol og afleveringsprotokol.')]),
        ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen',
         'Data Power Consultant ApS · København · 2024–nov. 2026 (sideløbende med ELOHVAC)',
         '4–10 personer · tekniske og industrielle applikationer',
         [('Data i beslutninger',
           'Tekniske applikationer samt **AI** i ledelsesarbejdet — rapportering, beslutningsoplæg '
           'og **KPI**-analyse; selskabet er ophørt.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('Krav, afvigelser og aflevering',
           'Kravspecifikation, **FAT/SAT** og **IQ/OQ/PQ**; dokumentation bygget undervejs og nul '
           'kritiske afvigelser ved aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter',
         [('Fremdrift, kapacitet og snitflader',
           'Dagligt tavlemøde, **kapacitetsmodel** og omprioritering samme dag; underentreprenører og '
           'materialer styret mod aftalt dato.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Biofos (Lynetten) · København · aug. 2017–jan. 2022',
         'Renseanlæg i 24/7-drift · pumper, højspændingstavler, SCADA',
         [('Drift, udkald og energi',
           'Planlagte **driftsvinduer** og akut fejlfinding døgnet rundt; **over 40 % lavere '
           'energiforbrug** gennem måling og indregulering.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 teknikere · maskinværksted · maskiner og materiel',
         [('Værksted, materiel og oplæring',
           'Fejlfinding, kalibrering og reparation; indkøb og vedligehold af materiel; oplæring og '
           'opfølgning for 12 teknikere.')]),
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
    m.para('Dansk og engelsk, skriftligt og mundtligt · Persisk: modersmål · **IT**: økonomi- og '
           'sagsystemer, CMMS, Excel-modeller og egne **Python**-værktøjer til **KPI** og '
           'ressourcestyring; **5S** og standard work som arbejdsform · **Kørekort B og egen bil** · '
           'Måløv, cirka 25 minutter til Amager og 20 minutter til Hvidovre · Kan starte efter aftale '
           '· Referencer på forespørgsel.', after=50)

    m.models_table('OPSLAGETS KRAV — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Stå for den daglige ledelse af faglederne og supportområdet',
         'Daglig personaleledelse siden 2003: 12 teknikere, 14 medarbejdere i 11 projekter, 25 '
         'specialister i en GMP-organisation og 8 ansatte i egen virksomhed — med fast kadence for '
         'sparring og opfølgning.'),
        ('Være ejendomschefens nærmeste sparringspartner og træde til som stedfortræder',
         'Har været stedfortræder og højre hånd for projektchef og bygherre i Novo Nordisk og drevet '
         'egen virksomhed uden mellemled — beslutningsoplæg på to sider med tre alternativer og en '
         'anbefaling.'),
        ('Skabe klare prioriteringer og sikre, at beslutninger og aftaler bliver omsat til handling',
         'Prioriteringsnøgle og beslutningslog med ejer og dato; i 2022 blev 11 samtidige projekter '
         'omprioriteret samme dag, og de fem vigtigste stod på én side ved ledelsesmødet.'),
        ('Holde sammen på de væsentligste snitflader mellem drift, projekter og hospitalets behov',
         '**Snitfladekort** med ejer og varslingsvej mellem projekt, drift og den klinik, der skal '
         'bruge lokalet; fem år i 24/7-drift har gjort driftshensynet til et krav, ikke en høflighed.'),
        ('Følge udviklingen i økonomi, ressourcer og risici og sikre, at der bliver handlet',
         'Månedlig ledelsesrapport på én side: fremdrift, forbrug, de tre største risici og de '
         'beslutninger, der mangler — fuldt **P&L** siden 2023 og 37 CAPEX-sager med rådighedsbeløb.'),
        ('Solidt ledelsesmæssigt fundament og erfaring med personaleledelse',
         '20+ år med personaleledelse, **MUS** hvert år, **forventningsaftale** pr. medarbejder, '
         'opfølgning på **sygefravær** og **APV**; **B.Tech** i teknologiledelse og maskinteknik.'),
        ('Sætte retning og være tydelig, når noget skal prioriteres eller ændres',
         'Skrevet prioritetsrækkefølge — patientsikkerhed og driftsstabilitet, derefter '
         'myndighedskrav, derefter tidskritiske projekter — brugt i fem år i 24/7-drift og i en '
         'fabrik, der ikke måtte standse.'),
        ('Opbygge tillid og få mennesker med dig',
         'Mandat og metodefrihed inden for en skreven ramme; resultatet er leverancerne, ikke min '
         'egen tid i sagen — 25 specialister, 14 medarbejdere og 8 ansatte har arbejdet selvstændigt '
         'under den ramme.'),
        ('Stille de rigtige spørgsmål og skabe klarhed, når du ikke er den, der ved mest',
         'Som **elautoriseret maskinmester** blandt specialister i el, CTS og ventilation har jeg '
         'ledet fagligt stærkere medarbejdere ved at spørge, ikke ved at svare — og skrevet svaret '
         'ned som en beslutning.'),
        ('Ro og dømmekraft i en hverdag uden én enkel løsning',
         'Akut fejlfinding om natten i fem år og projekter, hvor to hensyn ikke kunne opfyldes '
         'samtidigt: valget blev taget, skrevet ned og forklaret til dem, det gik ud over.'),
        ('Erfaring fra ejendomsdrift, forsyning, industri eller hospital',
         'Fem år i **ejendomsdrift**-nær 24/7-drift på et renseanlæg, industri i en GMP-fabrik og '
         '20+ år i tekniske installationer i bygninger — **hospitalsdrift** er det eneste nye i '
         'rækken, og driftsdøgnet er det samme.'),
        ('Forstå hvad det kræver at drive teknisk komplekse bygninger og installationer',
         '**Elautoriseret maskinmester (LV/MV/HV)**: stærkstrøm, **VVS**, **ventilation**, '
         '**CTS**/**BMS**, alarm og SCADA; kan læse en tavle, en ventilationskurve og en alarmliste '
         'og se, om driften holder.'),
        ('Give faglederne plads til at drive deres områder og fastholde en fælles retning',
         'Rammer, ikke instrukser: mandat til at vælge metode, fast kadence for sparring, og en fælles '
         'retning der bliver skrevet ned — i 2022 kunne både sjak, kunde og underentreprenør læse, '
         'hvad der var aftalt.'),
        ('Sikre at de rigtige mennesker bliver involveret, og at der bliver fulgt op',
         '**At skabe overblik og sikre, at de rigtige mennesker bliver involveret**: snitfladekort '
         'og varslingsvej med navn, opfølgning på dato og en log, hvor den, der ejer opgaven, også '
         'ejer næste skridt.'),
        ('Skabe overblik uden at kende alle tekniske løsninger i detaljen',
         'En **portefølje** på én side pr. projekt og én side pr. måned med fremdrift, **økonomi**, '
         '**ressourcer** og **risici** — overblikket ligger i oversigten, ikke i detaljen, og det er '
         'den, jeg tager ansvar for.'),
        ('Bidrage til udvikling af arbejdsgange, styring og det samlede overblik',
         '**Metodebog** med én arbejdsgang pr. proces, prøvekørt og målt før den blev standard; '
         '**5S** og standard work indført i værksted og på anlæg; opbygget ledelsesrapportering fra '
         'bunden i egen virksomhed.'),
        ('Komme tæt på hverdagen og den tekniske drift',
         'Jeg har stået i **teknikrummet** og på anlægget, ikke kun i mødelokalet: fem år i '
         '24/7-drift, daglig tavle og akutte udkald — og jeg kan tage en vagt, hvis det er det, '
         'situationen kræver.'),
        ('Ledelsesmæssig bredde og potentiale til at vokse med opgaven',
         'Har prøvet ledelse i små enheder og i en stor GMP-organisation, fra værksted til egen '
         'virksomhed med fuldt **P&L** — bredden er der; niveauet i en hospitalsorganisation skal '
         'læres, og det er jeg indstillet på.'),
        ('Arbejdssted på Amager og Hvidovre Hospital',
         'Bor i Måløv: cirka 25 minutter til Amager og 20 minutter til Hvidovre, kørekort B og egen '
         'bil — to matrikler i samme uge er praktisk muligt, ikke et kompromis.'),
        ('Ansættelse i Center for Ejendomme, Region Hovedstaden',
         '**B.Tech** i teknologiledelse og maskinteknik og **elautoriseret maskinmester** — '
         'professionsbachelor på det tekniske område, og indstillet på regionens løn- og '
         'ansættelsesvilkår.'),
    ])

    m.section('DE FØRSTE 90 DAGE')
    for b in (
        'Gået matriklerne igennem med faglederne og set, hvad der faktisk driller — teknikrum, '
        'tagrender og de anlæg, der står øverst på alarmlisten.',
        'Skrevet stedfortræderaftalen med ejendomschefen: hvilke beslutninger jeg tager, hvem der '
        'orienteres, og hvornår vi overlapper.',
        'Sat kadencen: ugentligt ledelsesmøde med faglederne, månedlig ledelsesrapport på én side og '
        'en fast runde på de væsentligste snitflader til projekterne.',
        'Aftalt med faglederne, hvad der skal være fælles først — så sammenlægningen til Ejendomme og '
        'Byggerier 1. januar 2027 møder noget, der allerede er ens.',
        'Læst APV, alarmhistorik og det seneste halve års hændelser igennem, så billedet ikke kun '
        'kommer fra dem, der har tid til at fortælle det.'):
        m.bullet('', b, after=16)

    m.section('DET VILLE JEG SPØRGE OM')
    for b in (
        'Hvor mange fagledere og hvor stort et supportområde består den daglige ledelse af i dag?',
        'Hvordan måles driftsstabilitet i dag — og hvad ville ejendomschefen gerne kunne se, som ikke '
        'kan ses nu?',
        'Hvor ligger beslutningsretten i dag mellem ejendomschef, viceejendomschef og fagledere, og '
        'hvad skal flyttes for at få et tydeligt stedfortræderskab?',
        'Hvilke faglige og økonomiske rammer er lagt for 2027, og hvad betyder sammenlægningen til '
        'Ejendomme og Byggerier for AHH’s organisation?'):
        m.bullet('', b, after=16)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_RegionH_ViceejendomschefAHH_2026.docx')
    build(out)
    print(out)
