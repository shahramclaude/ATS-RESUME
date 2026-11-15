# -*- coding: utf-8 -*-
"""Jeudan A/S — Produktionsleder til VVS-afdelingen (København / Frederiksberg).

Dansk leverance (opslaget er dansk): motiveringsside + CV i ét dokument.
Kultur- og rolleintel: master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md (Jeudan-afsnit).
Policy: master/README.md — ekstrem sikkerhed, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Produktionsleder · VVS · Ledelse tæt på udførelsen'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('5. november 2026')
    m.meta('Jeudan A/S · VVS-afdelingen · København og Frederiksberg')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Produktionsleder til VVS-afdelingen', bold=True, color='1A1A1A')
    m.para('Til teknisk direktør Dennis Patrick Lund', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('I VVS-arbejde er det sjældent røret, der er svært. Det er rækkefølgen. Ti montører, flere samtidige '
           'projekter, en ejendom fra 1890 der ikke fortæller dig, hvor røret ligger, en lejer der skal have vand '
           'klokken syv, og en projekteringsleder der har brug for en dato, han kan regne med. Det er den slags '
           'produktionsledelse, jeg gerne vil stå i spidsen for hos Jeudan — tæt på håndværket, tæt på '
           'byggepladsen og tæt på de mennesker, der udfører arbejdet.', after=80)

    m.para('**Jeg vil lede VVS-teamet på fire faste ting.** Først planen på tavlen: hver montør og hvert projekt '
           'med navn, timer og næste milepæl, en fast ugentlig gennemgang af fremdrift, ressourcer og tidsplaner, '
           'og time- og materialeforbrug fulgt på den enkelte sag — ikke på måneden, men mens der stadig er noget '
           'at styre. Dernæst sikkerhed og kvalitet som håndværk: arbejdsmiljø og sikkerhedsansøgning i orden før '
           'opstart, løfteanordninger og arbejde i højden tænkt ind, vand og el adskilt, og egenkontrol, trykprøvning '
           'og afleveringssyn dokumenteret som en del af arbejdet. Så koordineringen: jeg vil have en fælles tidsplan '
           'med de tolv øvrige produktionsledere og med projekt- og projekteringslederne, hvor konflikter bliver '
           'løst i planen og ikke på byggepladsen, og hvor en forsinkelse bliver varslet samme uge, den opstår. Og '
           'endelig menneskerne: MUS med løn- og udviklingssamtaler, lærlinge der får ansvar, og en klar '
           'forventning til den enkelte om, hvad der skal være færdigt i morgen.', after=80)

    m.para('Jeg har prøvet alle fire dele med ansvar for resultatet. I **Ventek-Air** var jeg projekt- og '
           'værkstedsleder for **14 medarbejdere og 11 samtidige anlægsprojekter** i ventilation og tekniske '
           'installationer — tilbud, kalkuler, underleverandører, fremdrift, timeforbrug og afleveringspakker, med '
           'daglige tavlemøder og flaskehalsanalyse. I **ELOHVAC**, som jeg har drevet siden 2023, har jeg fuldt '
           'P&L med **fem håndværkere og tre lærlinge**: bemanding, indkøb, kunder, kvalitet og økonomi i samme '
           'hverdag — og ansvar for at de unge bliver dygtige. Hos **Novo Nordisk** løftede jeg 37 samtidige '
           'kapitalprojekter med 25 specialister, hvor en manglende underskrift stopper en frigivelse. Og på '
           '**Biofos, Lynetten** var jeg i fem år drifts- og vedligeholdelsesleder på et 24/7-anlæg med vand, varme, '
           'ventilation, trykluft og tekniske installationer, hvor en nedetid koster penge med det samme.', after=80)

    m.para('De historiske ejendomme er ikke et argument imod mig — de er grunden til, at jeg søger. En gammel '
           'ejendom i indre København har skjulte føringer, skæve dæk, materialer der ikke findes mere, og lejere '
           'der bor og arbejder, mens vi er der. Det kræver, at man opdager før man ødelægger, at man har en plan B '
           'med i bilen, og at man taler med dem, der bruger bygningen, før man lukker for vandet. Jeg har stået i '
           'den situation mange gange: i drift på et anlæg, hvor alt var i brug, og i egen virksomhed, hvor kunden '
           'skulle have varme igen samme dag. Ordentlighed, ansvarlighed og tilgængelighed er Jeudans kerneværdier '
           '— og de er i praksis tre krav til en produktionsleder: ryddeligt arbejde, ansvar for egne fejl og et '
           'telefonnummer, der bliver taget.', after=80)

    m.para('En VVS-afdeling på 32 medarbejdere i en organisation med 270 håndværkere og 200 ejendomme er en '
           'afdeling, hvor man ikke kan arbejde som ø i systemet. Jeg vil bruge de tolv kolleger og '
           'projektkoordinatorerne aktivt: en fast ugentlig koordinering, hvor kommende opgaver bliver fordelt '
           'efter kompetence og kapacitet i stedet for efter hvem der råbte højest, og en aftale om, at ingen '
           'opgave starter på byggepladsen, før materiale, adgang og forudgående fag er på plads. Det er den slags '
           'forberedelse, der ikke ses i et regnskab, men som afgør, om ugen holder.', after=80)

    m.para('Fagligt er jeg **elautoriseret maskinmester** med B.Tech i Technology Management & Mechanical '
           'Engineering: varme, ventilation, sanitet, køl og tekniske installationer er den faglighed, uddannelsen '
           'er bygget på, suppleret med elautorisation på LV, MV og HV — hvilket er en fordel i et VVS-team, hvor '
           'styringer, tavler og samspillet med el-faggruppen er en del af hverdagen. Jeg læser tegninger og '
           'tekniske forskrifter, og jeg ved, hvad bygningsreglementet og de gældende standarder kræver, fordi jeg '
           'har skullet stå på mål for det over for kunder og myndigheder.', after=80)

    m.para('Praktisk: jeg bor i Måløv, har omkring en halv time til Bredgade og til ejendommene i indre by og på '
           'Frederiksberg, og det er på byggepladsen, jeg regner med at være — det administrative arbejde lægger '
           'jeg, når det giver mening. Ansættelse som funktionær passer mig fint: rammerne er fleksible, og ansvaret '
           'er fast. Nye IT-systemer lærer jeg hurtigt: jeg bygger selv værktøjer i Python til '
           'tilbud, tidsplaner og opfølgning, og jeg har arbejdet i SAP og Excel dagligt. Jeg kan starte efter '
           'aftale. Jeg vil gerne høre, hvordan I fordeler projekterne mellem de tolv produktionsledere, og hvordan '
           'VVS-teamet er sammensat i dag — og jeg kommer gerne forbi en af ejendommene, hvor der kører en sag, så '
           'vi kan tale om den konkrete plan i stedet for om planen i almindelighed.', after=70)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Produktions- og driftsleder med 20+ års erfaring fra tekniske installationer, håndværk og 24/7-drift — '
           'elautoriseret maskinmester med B.Tech i Technology Management & Mechanical Engineering. Har ledet 14 '
           'medarbejdere og 11 samtidige anlægsprojekter i ventilation og tekniske installationer, 25 specialister '
           'på 37 parallelle GMP-projekter og en egen virksomhed med fem håndværkere og tre lærlinge med fuldt '
           'P&L. Fem år som drifts- og vedligeholdelsesleder på et af landets største anlæg med vand, varme, '
           'ventilation og tekniske installationer. Stærk på bemanding, time- og materialeforbrug, sikkerhed, '
           'kvalitet og koordinering mellem fag.', after=80)

    m.section('VVS, TEKNISKE INSTALLATIONER OG PRODUKTION')
    for label, body in [
        ('Bemanding og fremdrift',
         'Daglig og ugentlig planlægning af montører på flere samtidige projekter: tavlemøder, flaskehalsanalyse, '
         'omprioritering uden at tabe kvalitet — og en tidsplan, der bliver opdateret, før den holder op med at '
         'passe.'),
        ('VVS-fagligheden',
         'Varme, ventilation, sanitet, køl og tekniske installationer fra uddannelsen og fra driften: systemer, '
         'komponenter, trykprøvning, indregulering og aflevering — plus elautorisation LV/MV/HV, så styringer og '
         'samspillet med el-faget er en del af helheden.'),
        ('Sikkerhed og kvalitet',
         'Arbejdsmiljø og sikkerhedsansøgning før opstart, arbejde i højden og løft planlagt, LOTO og '
         'arbejdstilladelser i en 24/7-drift; egenkontrol, dokumentation og afleveringssyn som fast praksis.'),
        ('Koordinering på tværs',
         'Fælles tidsplan og tydelige grænseflader med projekt- og projekteringsledere, andre faggrupper og '
         'leverandører; konflikter løst i planen og ikke på byggepladsen — med samme information til alle.'),
        ('Mennesker og økonomi',
         'MUS, løn- og udviklingssamtaler, oplæring af lærlinge og rekruttering; budget, indkøb, '
         'materialeforbrug og dækningsgrad fulgt på den enkelte sag i egen virksomhed siden 2023.')]:
        m.bullet(label, body, after=25)

    m.models_table('VÆRKTØJER OG METODER', ('Opgave', 'Værktøj og dokumenteret brug'), [
        ('Produktionsstyring',
         'Ugentlig tavle med bemanding pr. projekt, fremdrift mod milepæle, time- og materialeforbrug pr. sag; '
         'flaskehalsanalyse og omprioritering med kort varsel.'),
        ('VVS og teknik',
         'Tegninger og tekniske forskrifter, trykprøvning, indregulering og aflevering; varme, ventilation, '
         'sanitet, køl og styringer — elautorisation LV/MV/HV.'),
        ('Sikkerhed og arbejdsmiljø',
         'Sikkerhedsansøgning og arbejdspladsvurdering, LOTO og arbejdstilladelser, arbejde i højden og løft, '
         'kemikalier og støj — planlagt ind i tidsplanen, ikke oven på den.'),
        ('Kvalitet og dokumentation',
         'Egenkontrol, afvigelseshåndtering med årsag og lukning, as-built og afleveringspakke; myndighedskrav og '
         'standarder som en del af leverancen.'),
        ('Økonomi og indkøb',
         'Kalkulation, tilbud, budget og dækningsgrad; indkøb og leverandøraftaler med pris, leveringstid og '
         'alternativ i orden, før materialet mangler.'),
        ('IT og data',
         'Python, Claude API, SAP og Excel: tidsplaner, timelister, KPI-tavler og opfølgning — over 40 % af det '
         'administrative arbejde fjernet i egen virksomhed.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 håndværkere og 3 lærlinge · fuldt P&L · private og erhvervsmæssige kunder',
         [('Produktion og bemanding', 'Planlægning af montører og lærlinge på skiftende opgaver, indkøb og '
                                      'levering, kvalitet og aflevering — med kunden informeret samme dag, noget '
                                      'ændrer sig.'),
          ('Økonomi og ledelse', 'Budget, tilbud, kalkulation og dækningsgrad; rekruttering, MUS og oplæring af '
                                 'lærlinge.'),
          ('Digitale værktøjer', 'Python og Claude API til tilbud, tidsplaner, checklister og KPI-tavler; over '
                                 '40 % produktivitetsforbedring.')]),
        ('Senior commissioning engineer / projektleder, elsystemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Koordinering og fremdrift', 'Acceptkriterier, milepæle og grænseflader mod andre fag og leverandører; '
                                        'status, tid, økonomi og risiko rapporteret månedligt til ledelse og '
                                        'kunde.'),
          ('Kvalitet og dokumentation', 'Dokumentation, afvigelser og auditeret aflevering med nul kritiske fund.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter · 2–10 mio. kr. pr. projekt',
         [('Produktionsledelse', 'Tilbud, kalkuler, underleverandører og afleveringspakker i ventilation og '
                                 'tekniske installationer; daglige tavlemøder og flaskehalsanalyse.')]),
        ('Drifts- og vedligeholdelsesleder / værkstedsassistent',
         'Biofos, Lynetten · København · aug. 2017–jan. 2022',
         '24/7-anlæg · vand, varme, ventilation, trykluft, pumper, højspænding og SCADA',
         [('Drift og vedligehold', 'Planer for forebyggende vedligehold, reservedelskritikalitet, kalibrering og '
                                   'fejlretning i skiftende teams; alarmopkald og akutudrykning.'),
          ('Sikkerhed i praksis', 'LOTO, arbejdstilladelser og arbejdspladsvurdering før hver opgave i et anlæg, '
                                  'der ikke måtte stoppe.')]),
        ('Elektromekaniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · industrielt udstyr',
         [('Team og oppetid', 'Vagtplanlægning og opfølgning på mål; fejlfinding, rodårsagsanalyse og korrigerende '
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
    m.edu('Køle- og ventilationsteknik · STCW sikkerhed og maskinvagt',
          'Mercantec 2021 · Søfartsstyrelsen 2021–2023')

    m.section('SPROG, PRAKTIK OG REFERENCER')
    m.para('Dansk: modersmål · Engelsk: professionelt · Persisk: modersmål · Kørekort B · Bor i Måløv, ca. en halv '
           'time fra Bredgade, og på byggepladsen hver dag · Kan starte efter aftale · SAP og Excel i daglig brug · '
           'Referencer fra Novo Nordisk, Biofos, Ventek-Air samt kunder og leverandører i egen virksomhed på '
           'forespørgsel.', after=70)

    m.models_table('DET EFTERSPØRGER DE — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Erfaring som overmontør, teamleder eller formand',
         'Produktions- og værkstedsleder for 14 medarbejdere og 11 samtidige anlægsprojekter i ventilation og '
         'tekniske installationer (Ventek-Air); drifts- og vedligeholdelsesleder i fem år (Biofos); indehaver med '
         'fem håndværkere og tre lærlinge og fuldt P&L (ELOHVAC, 2023–).'),
        ('Lede et VVS-team og planlægge bemanding på flere samtidige projekter',
         'Daglig og ugentlig bemandingsplanlægning af VVS-montører og teknikere på 11 parallelle projekter og på 37 '
         'GMP-kapitalprojekter med 25 specialister; tavlemøder og flaskehalsanalyse som fast rytme.'),
        ('Følge op på fremdrift, ressourcer, tidsplaner og time- og materialeforbrug',
         'Time- og materialeforbrug fulgt pr. sag i egen virksomhed; fremdrift, økonomi og risiko rapporteret '
         'månedligt til ledelse og kunde på Novo Nordisk-projekterne; budget og dækningsgrad med fuldt P&L.'),
        ('Sikre sikkert arbejde efter love, standarder og kvalitetskrav',
         'Arbejdsmiljø, sikkerhedsansøgning, LOTO og arbejdstilladelser i 24/7-drift; egenkontrol og aflevering '
         'efter gældende love, standarder og kvalitetskrav — med elautorisation LV/MV/HV og ansvar for egen '
         'virksomheds lovpligtige arbejde.'),
        ('Koordinere med projekt- og projekteringsledere, øvrige produktionsledere og fagspecialister',
         'Fælles tidsplan og grænseflader mod andre fag, leverandører og bygherre — i pharma-projekter, i '
         'ventilationsprojekter og i service og ejendomsdrift for private og erhverv.'),
        ('Løse udfordringer og sikre klar kommunikation på tværs af afdelinger',
         'Daglig tavlestatus med samme information til alle; eskalering samme uge; kunde og underleverandør '
         'informeret, før de selv opdager ændringen.'),
        ('Medarbejdersamtaler, herunder løn- og udviklingssamtaler',
         'Rekruttering, MUS, løn- og udviklingssamtaler og oplæring af lærlinge i egen virksomhed; teamudvikling '
         'og 1:1-samtaler i Biofos- og Ventek-Air-organisationen.'),
        ('Kendskab til regler og standarder i VVS-arbejde samt flair for IT-systemer',
         'Bygningsreglement, standarder og myndighedskrav fra uddannelse og praksis; SAP og Excel dagligt, og '
         'Python/Claude API til tidsplaner, timelister og KPI-tavler.')])
    m.page_break()

    m.models_table('DE FØRSTE 90 DAGE — MENNESKER, PLAN OG KVALITET', ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'Ud på byggepladserne med teamet, gennemgang af de kørende sager, tidsplaner, timeforbrug og åbne punkter. '
         'Møde med de tolv øvrige produktionsledere og med projekt- og projekteringslederne, og en runde forbi '
         'byggepladskontorer. Lær Jeudans systemer og sagsgange, før jeg ændrer noget.'),
        ('Dag 30',
         'Én samlet tavle for mit team: navn, projekt, timer og næste milepæl — og en fast ugentlig gennemgang, som '
         'projektlederne kan regne med. De første medarbejdersamtaler gennemført, og sikkerheden på de kørende '
         'sager verificeret.'),
        ('Dag 60',
         'Time- og materialeforbrug bliver fulgt pr. sag, før måneden er slut; afvigelser har en ejer og en dato. '
         'Én koordineringsrytme med de øvrige produktionsledere, hvor konflikter bliver løst i planen.'),
        ('Dag 90',
         'Mit team leverer til tidsplan og kvalitet uden at jeg skal stå i hver sag, og mine tal kan læses af '
         'andre. Mindst én arbejdsgang er forbedret og delt — så næste projekt starter bedre end mit gjorde.')])

    m.section('RÆKKEFØLGEN ER FAGET')
    m.para('Det svære i VVS-produktion er ikke den enkelte opgave, men rækkefølgen: hvem er hvor, hvornår er '
           'forudgående fag færdige, hvornår kan der lukkes for vandet, og hvornår er materialet på pladsen. Jeg '
           'planlægger baglæns fra afleveringen og lægger bufferen dér, hvor den gør mindst skade — og jeg hader '
           'overraskelser, der kunne være set i tirsdags. Derfor er tavlen ikke et møde, men et værktøj: den skal '
           'kunne læses af en montør på to minutter og af en projektleder på ét.', after=80)

    m.section('SIKKERHED OG KVALITET ER SAMME SAG')
    m.para('Et godt håndværk er et sikkert håndværk. Arbejdsmiljø, arbejde i højden, løft og vand- og el-adskillelse '
           'skal være planlagt, før dagen begynder — ikke opdaget, når opgaven er i gang. Kvalitet er den anden '
           'halvdel: trykprøvning, indregulering, egenkontrol og aflevering udført og dokumenteret, så det holder '
           'om ti år, og så den næste, der skal ind i systemet, kan se, hvad der er lavet. Jeg står på mål for '
           'begge dele — også når det koster en dag.', after=80)

    m.section('HISTORISKE EJENDOMME KRÆVER RESPEKT OG EN PLAN B')
    m.para('I en ejendom fra 1890 er tegningen et udgangspunkt, ikke en sandhed. Skjulte føringer, skæve dæk og '
           'materialer, der ikke findes mere, betyder, at man undersøger før man skærer, at man har alternativet '
           'med i bilen, og at man fortæller lejeren, hvornår vandet er tilbage. Det er også det, der gør arbejdet '
           'værd at være stolt af: man kan se resultatet, og bygningen står stadig om hundrede år.', after=80)

    m.section('TOLV KOLLEGER ER EN STYRKE, IKKE EN FORHINDRING')
    m.para('Med tolv andre produktionsledere i fem faggrupper er den vigtigste kompetence koordinering: én fælles '
           'tidsplan, tydelige grænseflader og en aftale om, hvem der taler med kunden hvornår. Jeg vil hellere '
           'bruge et kvarter på at aftale rækkefølgen med tømrerne end en dag på at forklare kunden, hvorfor der stod '
           'to hold i samme gang. Samarbejde er i praksis aftaler, der bliver holdt, og beslutninger, der bliver taget '
           'én gang og gælder for alle. Og når planen ikke holder, siger jeg det samme dag — til kunden og til '
           'mit team.', after=80)

    m.section('MENNESKERNE PÅ PLADSEN')
    m.para('Montører mærker forskel på ledelse i hverdagen: om materialet er der, om opgaven er beskrevet, om '
           'aftaler holder, og om nogen tager ansvar, når det brænder. Jeg vil være på pladsen, kende navnene og '
           'være den, der rydder forhindringerne af vejen. Udvikling sker i samtalen — MUS, løn og næste skridt — '
           'og i at give ansvar, der er lidt større end i går. Det er også sådan, man holder på de dygtige '
           'håndværkere.', after=80)

    m.section('AFLEVERINGEN ER KUNDENS FØRSTE INDTRYK')
    m.para('For en lejer i en Jeudan-ejendom er VVS-arbejdet ikke et projekt — det er den dag, hvor der blev lukket '
           'for vandet, eller den uge hvor radiatoren ikke virkede. Derfor vil jeg have afleveringen med i planen '
           'fra dag ét: hvad er færdigt, hvad bliver prøvet, hvornår er der adgang, og hvornår er der ryddet op. En '
           'god aflevering er den billigste service — den fjerner de genopkald, der ellers kommer ugen efter.', after=80)

    m.section('TAL DER KAN LÆSES AF ANDRE — OG IT DER GIVER TID')
    m.para('Jeg vil kunne svare på tre spørgsmål uden at slå op: Hvor mange timer har vi brugt på sagen, hvor mange '
           'er der tilbage, og hvad koster materialet i forhold til kalkulen. Det kræver, at timerne registreres '
           'samme dag og fordeles rigtigt — derfor er tidsregistrering en ledelsesopgave og ikke en formalitet. Nye '
           'IT-systemer lærer jeg hurtigt, og jeg bygger selv de værktøjer, der mangler: tidsplaner, timelister, '
           'checklister og KPI-tavler i Python og Excel. Målet er altid det samme — en halv time mindre '
           'administration om dagen pr. mand bliver til timer på byggepladsen. Jeg deler værktøjerne frem for at '
           'gemme dem.', after=80)

    return m.save(path, title='Ansøgning og CV — Produktionsleder, VVS, Jeudan',
                  subject='Produktionsledelse i VVS: bemanding, fremdrift, kvalitet og mennesker',
                  keywords='produktionsleder, VVS, bemanding, fremdrift, tidsplaner, kvalitet, sikkerhed, '
                           'koordinering, håndværk, ejendomme')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Jeudan_ProduktionslederVVS.docx')))
