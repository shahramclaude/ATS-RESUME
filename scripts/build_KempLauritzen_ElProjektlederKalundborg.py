# -*- coding: utf-8 -*-
"""Kemp & Lauritzen A/S — El-Projektleder til komplekst byggeprojekt, Kalundborg (pharma).

Form (master/FORMKATALOG.md): åbning **F** (konsekvensen — fejlen viser sig et andet sted, på et
andet tidspunkt), struktur **Regnestykket** (timerne · materialerne · underentreprenøren ·
risikoen · dækningsgraden), register **Akkorden** (nyt: akkord, styk, opmåling, tildeling,
akkordbrev, regulering, merarbejde, sjak, formand, dækningsgrad).
Kulturfil: jd/KempLauritzen_ElProjektlederKalundborg_kultur.txt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'El-Projektleder · el-entreprise og akkord i pharma-projekt'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('12. november 2026')
    m.meta('Kemp & Lauritzen A/S · Projekt i Kalundborg · att. projektchef Thomas Bech')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: El-Projektleder, Kalundborg', bold=True, color='1A1A1A')

    # ---------------------------------------------------------------- side 1
    m.para('**En el-entreprise i et pharma-byggeri går ikke galt i tavlen. Den går galt seks uger '
           'senere** — den dag kvalitetsafdelingen skal bruge den tegning, der blev rettet i hånden, '
           'den dag akkorden skal gøres op og der mangler opmåling, eller den dag et sjak står uden '
           'materiale, fordi indkøbet blev lovet i en mail. Fejlen findes altid et andet sted, end hvor '
           'den blev lavet. Derfor har jeg brugt 20+ år på at gøre de ting færdige samme uge, som '
           'ingen ser: opmålingen, dokumentationen, aftalen med akkordholderen.', after=60)

    m.para('**Kemp & Lauritzen er 3.000 medarbejdere og en fond, der investerer i medarbejderne** — '
           'el, VVS, ventilation og køl, fra service til store entrepriser. Projektet i Kalundborg er '
           'et pharma-byggeri med høje krav til kvalitet, sikkerhed og fremdrift, og rollen refererer '
           'til den tværfaglige projektchef. Jeg kender miljøet: jeg har i to år arbejdet i en '
           'pharma-fabrik i drift i Kalundborg med 37 parallelle projekter og de dokumentationskrav, '
           'der gælder, også for entreprenøren. Nu vil jeg gerne stå på entreprenørens side af den '
           'samme byggeplads.', after=60)

    m.para('**Fem linjer i regnestykket, jeg styrer en el-entreprise efter.**', after=50)

    m.para('**Timerne.** Akkorden er ikke en pris, den er et antal timer, nogen har regnet rigtigt '
           'eller forkert. Jeg har selv stået med **akkordbreve, opmåling og tildeling til sjak** og '
           'med **regulering**, når virkeligheden ikke lignede tilbuddet — og jeg ved, at forskellen '
           'mellem en god og en dårlig akkord oftest ligger i forudsætningerne, ikke i tempoet. Derfor '
           'bliver forudsætningerne skrevet ned og godkendt, før sjakket går i gang.', after=44)

    m.para('**Materialerne.** Spild, retur og forkert leveringsrækkefølge er den lydløse tabspost. I '
           '37 projekter med tavler, UPS, nød- og panikbelysning, PDS og ABA/ABV var materialestyring '
           'og leveranceopfølgning en fast del af mødet — ikke noget, der blev opdaget på '
           'byggepladsen. Et sjak, der venter, er dyrere end en ekstra leverance.', after=44)

    m.para('**Underentreprenøren.** Grænsefladen skal være aftalt, før den bliver et tillæg: hvem '
           'laver føringsvejene, hvem tilslutter, hvem dokumenterer, og hvem har ansvaret, når to '
           'parter har ret. I 11 samtidige anlægsprojekter med 14 medarbejdere og underentreprenører '
           'var den øvelse daglig — og i egen virksomhed har jeg prøvet at være den, der måtte ringe og '
           'sige, at grænsen lå et andet sted.', after=44)

    m.para('**Risikoen.** Adgang i et byggeri, hvor der arbejdes i etaper, merarbejde, ændringer og '
           'krav fra en bygherre, der skal bruge anlægget. Risiko er ikke et forbehold i tilbuddet; '
           'det er de tre ting, vi bliver enige om at gøre, hvis de sker. Jeg har siddet med budget '
           '2–10 mio. kr. pr. projekt og med fuldt P&L siden 2023, så jeg ved, hvad et forbehold '
           'koster, når det ikke blev skrevet.', after=44)

    m.para('**Dækningsgraden.** Den er resultatet af de fire andre linjer — og den skal være synlig '
           'hver måned, ikke ved aflevering. Jeg har fulgt **økonomi** og **kvalitet** månedligt med '
           'afvigelsesforklaring, ført **KS** og afleveringsdokumentation og afleveret projekter med '
           '**nul kritiske afvigelser**. En el-entreprise, der vinder på kvalitet, taber ikke på '
           'økonomi; den taber, når ingen har set på tallene i tide.', after=60)

    m.para('**Jeg er ikke uddannet el-installatør — jeg er elautoriseret maskinmester (LV/MV/HV).** '
           'Det er den »tilsvarende tekniske baggrund«, opslaget selv åbner for: autorisationen, '
           'håndværket i bund og 20+ år i el-entreprise, drift og projektering. Akkord har jeg stået '
           'med selv, ikke kun hørt om; pharma har jeg arbejdet i; og entrepriserne har jeg ført både '
           'som underentreprenør og som den, der ejede dem.', after=60)

    m.para('**Jeres eget sprog rammer det, jeg søger:** **»sikkerhed, ordentlighed og samarbejde er '
           'fundamentet«**, og **»hos os handler det om ordentlighed«**. I er **Danmarks førende '
           'digitale og grønne teknikpartner** med **3.000 medarbejdere**, hvor **grøn** omstilling og '
           'digitalisering er selve forretningen og ikke et tillæg, og I leverer **fra daglig '
           'service til store entrepriser og unikke specialer** — og rollen er **en central rolle i et '
           'komplekst og fagligt udfordrende pharma-projekt** med **stort ansvar og stor indflydelse**. '
           'I skriver, at **»Vi tager ansvar i alt vi gør«**, at I vil **skabe plads til forskellighed** '
           'og være **én af Danmarks bedste arbejdspladser** — I blev **Årets virksomhed med mere end '
           '500 medarbejdere** i 2023 — og at fonden **investerer i vores medarbejdere og samfundet som '
           'helhed**. Det sidste er ikke en detalje for mig: det er forskellen på en arbejdsplads, man '
           'bliver i, og en man skifter fra. Og det kræver **kompetente kolleger, der vil fremad** '
           'samt **evnen til at skabe tillid og samarbejde på tværs af interessenter** — det er den '
           '**løsningsorienteret tilgang**, jeg har praktiseret i 20+ år.', after=60)

    m.para('**Praktisk:** jeg bor i Måløv og har pendlet til Kalundborg i to år, så det ved jeg, hvad '
           'betyder i hverdagen — jeg kører den tur igen. Dansk og engelsk, skriftligt og mundtligt. '
           'Jeg kan starte efter aftale. Det, jeg gerne vil høre om, er, hvordan entreprisen er '
           'opdelt i akkord i dag, og hvornår i forløbet I forventer, at el-entreprisen går i gang.',
           after=50)

    m.meta('Med venlig hilsen', after=15)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('**El-teknisk projektleder** — **elautoriseret maskinmester (LV/MV/HV)**, B.Tech i '
           'teknologiledelse og maskinteknik. Har ført **37 parallelle kapitalprojekter** på 2–10 mio. '
           'kr. i en pharma-fabrik i drift, ledet **11 samtidige anlægsprojekter** med **14 '
           'medarbejdere** og drevet egen el-virksomhed med **fuldt P&L** siden 2023. Har arbejdet med '
           '**akkord, opmåling og regulering**, med **KS** og afleveringsdokumentation og med '
           '**nul kritiske afvigelser** som krav — og har pendlet til Kalundborg i to år.', after=70)

    m.section('AKKORDEN — EL-ENTREPRISE, ØKONOMI OG FOLK')
    for label, body in [
        ('Akkord og opmåling',
         '**Akkordbreve**, **opmåling** af udført arbejde, **tildeling** af **akkord** til sjak og '
         '**regulering** af mer- og mindrearbejde — opgjort sammen med den formand eller akkordholder, '
         'der udførte arbejdet, så uenigheden blev afklaret i marken og ikke i regnskabet.'),
        ('Sjakket og formanden',
         'Daglig ledelse af **sjak** og formænd: hvad der er dagens opgave, hvad der blokerer, og '
         'hvem der har materialet. 5 elektrikere og 3 lærlinge i egen virksomhed og 14 medarbejdere '
         'plus underentreprenører i 11 samtidige anlægsprojekter.'),
        ('El-entreprisen',
         'El-tekniske entrepriser fra tavle til aflevering: **installationer**, tavler, styring, '
         'føringsveje, **idriftsættelse** og **dokumentation** — samt 37 projekter med tavler, UPS, '
         'ABA/ABV, PDS og nød- og panikbelysning i pharma-miljø.'),
        ('Økonomien',
         '**Dækningsgrad** pr. opgave, **kalkulation** og **tilbud**, ændringshåndtering og '
         '**økonomistyring** månedligt med afvigelsesforklaring; fuldt **P&L** i egen virksomhed '
         'siden 2023.'),
        ('Kvalitet og sikkerhed',
         '**KS** og **kvalitetssikring** med tjekliste pr. opgave, egenkontrol før aflevering og '
         '**arbejdsmiljø** med **APV**, '
         'LOTO og **sikkerhedsrundering**; nul kritiske afvigelser i 37 projekter under GMP/FDA/EMA.'),
        ('Interessenterne',
         '**Bygherre**, **rådgivere**, **faggrupper** og **underentreprenører** i samme møderække med '
         'beslutningslog — **koordinering** og **opfølgning** med navn på ejer og dato for næste svar.')]:
        m.bullet(label, body, after=16)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · el-entreprise og service',
         [('El-entreprise, akkord og kunder',
           '**Tilbud** og **kalkulation**, **akkord** og **opmåling**, ændringshåndtering og '
           '**aflevering**; **økonomi**, **ressourcer** og **kvalitet** fulgt månedligt; **arbejdsmiljø** med APV, '
           'LOTO og sikkerhedsrundering.')]),
        ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen',
         'Data Power Consultant ApS · København · 2024–nov. 2026 (sideløbende med ELOHVAC)',
         '4–10 personer · tekniske og industrielle applikationer',
         [('AI i projekt- og ledelsesarbejde',
           '**AI coding** til tekniske anlæg og industrielle komponenter og AI i ledelsesarbejdet — '
           'ledelsesrapportering, beslutningsoplæg og KPI-analyse; selskabet er ophørt.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('Pharma, dokumentation og aflevering',
           'Kravspecifikation, FAT/SAT, IQ/OQ/PQ og **aflevering** i en fabrik i drift — '
           '**dokumentation** bygget undervejs og nul kritiske afvigelser.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter',
         [('Fremdrift og kapacitet',
           'Dagligt **tavlemøde**, kapacitetsanalyse og omprioritering samme dag; **underentreprenører** '
           'og afleveringspakker med dokumentation.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Biofos (Lynetten) · København · aug. 2017–jan. 2022',
         'Renseanlæg i 24/7-drift · pumper, højspændingstavler, SCADA',
         [('Drift, der ikke må stoppe',
           'Vedligehold og ombygning udført i **drift**: LOTO, isolering, varsling og genopretning; '
           '**over 40 % lavere energiforbrug** gennem måling og indregulering.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 teknikere · maskinværksted · maskiner og materiel',
         [('Værksted og materiel',
           'Fejlfinding, kalibrering og reparation; indkøb og vedligehold af maskiner og bilpark; '
           'oplæring og målopfølgning for 12 teknikere.')]),
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
    m.para('Dansk (modersmål) og engelsk, skriftligt og mundtligt · Persisk: modersmål · **IT**: '
           'ERP-baserede projekt- og økonomisystemer, kalkulations- og tilbudsværktøjer, Excel og egne '
           '**Python**-værktøjer til tid, **KS** og **KPI** · **Kørekort B og egen bil** · Måløv, '
           'pendling til Kalundborg prøvet i to år · Kan starte efter aftale.', after=50)

    m.models_table('OPSLAGETS KRAV — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Ledelse og styring af el-entreprisen på projektet',
         '**El-entreprise** som ejer siden 2023 med fuldt **P&L**, og el-teknisk projektledelse i 37 '
         'kapitalprojekter med tavler, UPS, ABA/ABV og PDS.'),
        ('Koordinering og opfølgning på akkordarbejde i tæt samarbejde med akkordholdere',
         '**Akkordbreve**, **opmåling**, tildeling til sjak og **regulering** — opgjort sammen med '
         'formanden eller akkordholderen, der udførte arbejdet.'),
        ('Sikre overholdelse af tidsplan, økonomi og kvalitet',
         '**Tidsplan** med milepæle, **økonomi** månedligt med afvigelsesforklaring og **kvalitet** '
         'via **KS** og afleveringspakke — i 37 projekter og i 11 samtidige anlægsprojekter.'),
        ('Løbende dialog med bygherre, rådgivere og øvrige faggrupper',
         '**Bygherre** og **rådgivere** i fast møderække i 20+ år: i Novo Nordisk som bygherres '
         'projektleder og i egen virksomhed over for både bygherre og **faggrupper**.'),
        ('Håndtering af udfordringer med en løsningsorienteret tilgang',
         'Da forudsætningerne skred i 11 samtidige projekter, blev rækkefølgen besluttet på tavlen '
         'samme dag — med tre alternativer og en anbefaling, ikke med en mail om, hvem der havde ret.'),
        ('Sikre at vi følger gældende interne administrative og økonomiske processer',
         'Arbejdet i en GMP-organisation, hvor proces, dokumentation og godkendelse var vilkåret — og '
         'i egen virksomhed, hvor **aftaler** og fakturaer skal kunne dokumenteres ved en '
         'gennemgang.'),
        ('Sikre tæt samarbejde med eksterne samarbejdspartnere',
         '**Underentreprenører** og eksterne partnere i 11 samtidige projekter med 14 medarbejdere; '
         'grænsefladen aftalt skriftligt, før den blev et tillæg.'),
        ('Uddannet el-installatør eller tilsvarende teknisk baggrund',
         '**Elautoriseret maskinmester (LV/MV/HV)**, Sikkerhedsstyrelsen 2023, plus B.Tech i '
         'teknologiledelse og maskinteknik — ikke uddannet el-installatør, men **elautorisation** (LV/MV/HV) '
         'og håndværket er der.'),
        ('Dokumenteret erfaring med entrepriseprojekter',
         '**Entreprise** siden 2023 i egen virksomhed med tilbud, kontrakt, underentreprenører og '
         'aflevering — og 37 kapitalprojekter på 2–10 mio. kr. som entrepriseprojektleder.'),
        ('Har arbejdet med akkord og har indgående forståelse for akkordarbejde',
         '**Akkord** stået med selv: forudsætningerne skrevet ned før start, **opmåling** undervejs, '
         '**regulering** af mer- og mindrearbejde og **dækningsgrad** fulgt pr. opgave.'),
        ('Er struktureret, ansvarsbevidst og løsningsorienteret',
         'Fast rækkefølge fra behov til aflevering: plan, tavlemøde, **KS** og afleveringspakke — og '
         'mangellister lukket med navn og dato i 37 projekter.'),
        ('Evnen til at skabe tillid og samarbejde på tværs af interessenter',
         '**Interessenter** med modstridende krav håndteret ved at gøre konflikten eksplicit og '
         'beslutte den ét sted — produktion mod byggeri, fremdrift mod sikkerhed.'),
        ('Taler og skriver dansk',
         'Dansk som modersmål, også teknisk og i forhandlinger; engelsk professionelt og persisk som '
         'tredje sprog.'),
        ('Referere direkte til den tværfaglige projektchef som nøgleperson i projektet',
         'Rapporteret direkte til projektchef og bygherre i 37 projekter og til egen ledelse i '
         'ELOHVAC — beslutningsoplæg på 1-2 sider, når der skulle besluttes noget.'),
        ('Arbejde tæt sammen med akkordholdere, rådgivere og bygherre samt øvrige fagdiscipliner',
         'Akkordholdere og formænd i den daglige plan, **rådgivere** i projekteringsmøder og '
         '**faggrupper** i koordinationsmøder på pladsen.'),
        ('Høje krav til kvalitet, sikkerhed og fremdrift',
         '**Sikkerhed** som fast punkt: APV, LOTO, sikkerhedsrundering og opfølgning på '
         'nærved-hændelser; **fremdrift** styret på tavlen hver morgen.'),
        ('Komplekst og fagligt udfordrende pharma-projekt',
         'To år i en **pharma**-fabrik i drift i Kalundborg: 37 parallelle projekter, GMP/FDA/EMA, '
         'adgangsprocedurer og dokumentationskrav — jeg kender vilkårene, ikke kun ordene.'),
        ('Præge løsninger og processer i et projekt med høje standarder',
         'Standarder skrevet sammen med dem, der skulle arbejde efter dem — 12 teknikere, 3 lærlinge '
         'og 8 ansatte; proces er noget, man bygger, ikke noget man pålægger.'),
        ('Sikkerhed, ordentlighed og samarbejde som fundament',
         '**Ordentlighed** som praksis: aftaler overholdt, dokumentation i orden og ingen genveje i '
         '**sikkerheden** — i 20+ år og i egen virksomhed hver eneste uge.'),
        ('Stort ansvar og stor indflydelse',
         'Fuldt **P&L** siden 2023, 37 projekter på 2–10 mio. kr. og 14 medarbejdere i 11 samtidige '
         'projekter — ansvar for både tal, tid og mennesker.')])

    m.section('DE FØRSTE 90 DAGE')
    for b in (
        'Gennemgået el-entreprisens akkordbreve og forudsætninger med projektchefen og akkordholderne '
        'og skrevet ned, hvad der er uafklaret — før det bliver til merarbejde.',
        'Sat én tavle op for el-entreprisen: tidsplan, materialer, sjak og åbne grænseflader mod de '
        'andre fag, med navn og dato på hver post.',
        'Gået pladsen igennem med sikkerhedsorganisationen og bygherrens kvalitetsfunktion og rettet '
        'dokumentationsflowet, så det passer med den måde, der faktisk arbejdes på.'):
        m.bullet('', b, after=16)

    m.section('DET VILLE JEG SPØRGE OM I EN SAMTALE')
    for b in (
        'Hvordan er el-entreprisen opdelt i akkord i dag — én samlet akkord eller flere, og hvem '
        'opmåler?',
        'Hvor langt er byggeriet, når jeg starter, og hvilke etaper er allerede låst af hensyn til '
        'bygherrens produktion?',
        'Hvor mange sjak og akkordholdere skal jeg lede, og er der underentreprenører på el-siden?',
        'Hvad har været den største udfordring i Kemp & Lauritzens pharma-projekter indtil nu — '
        'dokumentation, adgang eller fremdrift?'):
        m.bullet('', b, after=16)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_KempLauritzen_ElProjektlederKalundborg.docx')
    build(out)
    print(out)
