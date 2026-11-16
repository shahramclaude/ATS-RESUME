"""ELCON Junior Planlægger, Glostrup (rekvisition 679): dansk ansøgning og CV.

Design: scripts/master_design.py (masterdesignet — navy banner, sektionsbannere,
blå punkter),jf. de uploadede master-CV'er.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = 'SHAHRAM AJLOO'
TITLE = 'Elautoriseret maskinmester | Kundeservice, planlægning og el-teknik'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'), lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('ELCON · Kundecenter Glostrup · Att.: teamleder Therese Ring · Requisition 679')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Junior Planlægger — kundens vej fra bestilling til installation',
           bold=True, color='1A1A1A')
    m.para(
        'En ladestander bliver først en god kundeoplevelse, når bestillingen bliver til en aftale, '
        'kunden forstår næste skridt, og en servicemontør kan gennemføre arbejdet. ELCON beskriver '
        'sit landsdækkende kundecenter i Glostrup som den fælles indgang mellem kunden og de lokale '
        'afdelinger. For Junior Planlæggeren er opgaven at holde det sammen: besvare '
        'kundehenvendelser, booke installationer og sikre, at informationen følger med opgaven.',
        after=70)
    m.para('Et system for hverdagen — fra første samtale til aflevering:', after=40)
    for a, b in [
        ('Fra samtale til færdige oplysninger',
         'Kontrollér ordren, og kontakt kunden på en imødekommende måde. Sørg for, at '
         'kontaktoplysninger, adresse og de forhold, der påvirker installationen, er korrekte og '
         'registreret i kundecentrets IT-systemer. Er noget uklart, skal det frem i systemet, så den '
         'næste kollega kan handle på det — ikke ligge i en telefonsamtale.'),
        ('Fra booking til montør',
         'Sammenhold kundens ønske med ledig kapacitet og den rette afdeling efter teamets '
         'planlægningsregler. Bekræft tid og aftalte forudsætninger, og sørg for, at servicemontøren '
         'har de nødvendige oplysninger ved ankomst. Planlægning og booking skal kunne efterprøves '
         'af kunden og af kollegerne.'),
        ('Når aftalen ændrer sig',
         'Informér kunden og montøren, opdatér sagen, og aftal en ny ansvarlig opfølgning med en '
         'frist. En ændring, der kun findes i en besked, giver den næste kunde en uklar oplevelse og '
         'montøren en unødig kørsel.'),
        ('Når spørgsmålet gælder produktet frem for installationen',
         'Hvis henvendelsen gælder selve ladeproduktet, hjælpes kunden videre til den rette kontakt '
         'i ELCONs procedure, så den beløber sig hos den, der ikke kan svare — og kunden får ét '
         'svar, der gælder installationen.'),
        ('Når belastningen flytter sig',
         'Skeln mellem opgaver, der påvirker en nært forestående montøraftale, og spørgsmål, der '
         'kan få en aftalt tilbagemelding senere. En kort status med næste handling og ansvarlig '
         'gør det muligt for en kollega at tage over. Videndeling om tilbagevendende henvendelser '
         'gør svarene ensartede på dansk og engelsk.'),
        ('Når videns skal sidde i systemet',
         'Kend de tilbagevendende spørgsmål, og opdatér svarene, så alle i teamet giver den samme '
         'information. MS Office og de lokale it-systemer holdes aktuelle, og ændringer i '
         'arbejdsgange meldes til de, der skal bruge dem.'),
    ]:
        m.bullet(a, b, after=25)
    m.para(
        'Kvaliteten i registreringen er derfor målet: den næste kollega skal kunne handle på det, '
        'kunden allerede har fortalt, og montøren skal ikke starte med at ringe ind for at finde ud '
        'af, hvad der står i ordren. Målet er ikke flest mulige løfter, men aftaler, der kan '
        'holdes, og sager, der følges til dørs — med kunden informeret hele vejen.', after=70)
    m.para(
        'ELCONs arbejde med digitale ordreprocesser viser, hvorfor kvaliteten af registreringen '
        'betyder noget i et landsdækkende flow. Et kundecenter, der svarer ensartet, og en '
        'planlægning, der fungerer, er forudsætningen for, at den lokale afdeling kan gøre sit '
        'arbejde. Derfor må kundeservice hos ELCON ikke miste kunden i overgangen: hver '
        'henvendelse skal ende i en konkret aftale med en tid, en adresse og en forventning — også '
        'når svaret er, at der vender tilbage med en bekræftelse.', after=70)
    m.para(
        'Kvaliteten i svaret måles i, om kunden kan handle på det. Derfor skal hver henvendelse '
        'ende i en skriftlig status: hvad der er aftalt, hvad der mangler, og hvornår kunden hører '
        'næste gang. Det samme gælder sprog: det danske og det engelske svar skal beskrive samme '
        'forpligtelse, så en kunde ikke får en løs aftale på det ene sprog og en konkret på det '
        'andet. Og når svaret kræver faglig viden, skal kunden hjælpes videre — enten til den rette '
        'specialist i ELCON eller til den, der har ansvaret for det område.', after=70)
    m.para(
        'Montøren skal kunne gå ud ad døren med det, der skal bruges: adresse og adgang, type af '
        'installation, kundens forventning, det aftalte tidsrum og eventuelle forbehold. Mangler '
        'noget, skal det registreres som en forbehold — og genbesøges, inden montøren er på vej. '
        'Når en installation alligevel ikke kan gennemføres, er kundens information del af '
        'opgaven: hvad der sker nu, hvornår der følges op, og hvem der har ansvaret.', after=70)
    m.para(
        'Som Junior Planlægger i et kundecenter er det første arbejde at lære ELCONs arbejdsgange, '
        'systemer og produkter — og det sker bedst i det: kundecenteret er det sted, hvor '
        'spørgsmålene samles, og hvor svarene bliver ensartede. Teamet skal have plads til at '
        'spørge om hjælp og til at hjælpe andre, når belastningen skifter.', after=70)
    m.meta('Med venlig hilsen', after=10)
    m.meta('Shahram Ajloo', after=0)

    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para(
        'Elautoriseret maskinmester med 20+ års erfaring i el-teknisk drift, installation, service '
        'og personaleledelse — egen teknisk servicevirksomhed med fuldt P&L-ansvar (5 elektrikere og '
        '3 lærlinge), GMP-reguleret produktion (Novo Nordisk, 25 specialister, 37 projekter á DKK '
        '2–10 mio.), værkstedsdrift (Ventek-Air, 14 mand, 11 parallelle projekter) og kritisk '
        'døgnbemandet drift (Biofos). Kunde- og planlægningsarbejdet kommer fra service-, tilbuds- '
        'og projektarbejde, hvor aftaler, ressourcer, opfølgning og dokumentation er holdt i '
        'orden. Aktiv AI- og Claude-koder med egne værktøjer til planlægning, KS og KPI '
        '(dokumenteret produktivitetsforbedring over 40 %).', after=70)
    m.section('KOMPETENCER — KUNDE, PLAN OG TEKNIK')
    for a, b in [
        ('Kundeservice og kundekontakt',
         'ELOHVAC: erhvervskundedialog, tilbud, serviceaftaler og koordinering fra opgave til '
         'aflevering. Klare aftaler, opfølgning, kvalitetssikring og afleveringsdokumentation. '
         'Samarbejde med kunder, teknikere og underentreprenører i pressede situationer.'),
        ('Planlægning, booking og kapacitet',
         'Daglig planlægning af 5 elektrikere og 3 lærlinge hos ELOHVAC; kapacitetsstyring af 11 '
         'simultane projekter hos Ventek-Air. Materialer, underentreprenører og ressourcer på tværs, '
         'tavlemøder og flaskehalsanalyse.'),
        ('Servicemontørernes arbejdsgange',
         'Installation, tavler, styring og fejlfinding på el-, ventilations- og klimaanlæg. '
         'Biofos: pumper, HVAC, højspændingstavler og SCADA i døgnbemandet drift, reservedelsflow '
         'og LOTO. Kendskab til, hvad montøren skal have med, inden arbejdet starter.'),
        ('Økonomi, opmåling og ajour',
         'Fuldt P&L-ansvar, tilbud og beregning, akkordbreve, opmåling, tildeling til sjak samt '
         'regulering og opgørelse af mer- og mindrearbejde. Rapportering til ledelse og månedlig '
         'status på kapacitet, kvalitet og leveringsevne.'),
        ('Digitale værktøjer og it-systemer',
         'MS Office, Excel/Power Query, SAP ERP, Python og Claude API. Aktiv AI-/Claude-koder med '
         'egne værktøjer til planlægning, KS-tjeklister og KPI-dashboards; investeringsmodeller med '
         'NPV, IRR og scenarier. Systemer og arbejdsgange holdes aktuelle, og ændringer kommunikeres '
         'til brugerne.'),
        ('Ledelse og forbedringer',
         'PRINCE2-certificeret projektleder; tavlemøder, 1:1, MUS/GRUS, situationsbestemt ledelse '
         '(SLII), coaching efter GROW og feedback efter SBI. Gemba-walks, visuel ledelse, '
         'KPI-tavler, eskaleringstrappe og RACI i praksis. Lean- og Six Sigma-metoder — 5S, Kaizen, '
         'PDCA, A3, VSM, Standard Work, SMED, TPM, Kanban, 5xHvorfor, Ishikawa og FMEA — anvendt i '
         'praksis; ikke certificeret.'),
    ]:
        m.bullet(a, b, after=25)
    m.section('RESULTATER OG PRAKTISK INFORMATION')
    m.para(
        'Over 40 % produktivitetsløft med AI-værktøjer hos ELOHVAC · 40 % lavere energiomkostninger '
        'via PDCA hos Novo Nordisk · ingen kritiske afvigelser ved Novo-afleveringer. Dansk og '
        'persisk/farsi: modersmål · engelsk: professionelt · Kørekort B · Bopæl Måløv, '
        'Storkøbenhavn. Tiltrædelse og arbejdstid aftales.', after=50)
    m.para(
        'Kundedialog, planlægning og opfølgning er dokumenteret fra service-, tilbuds- og '
        'projektarbejde — herunder planlægning af montører, underentreprenører og materialer gennem '
        'hele projektet.', after=40)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L-ansvar',
         [('Kundeaftaler og levering',
           'Tilbud, beregning og kundedialog; planlægning af medarbejdere, materialer og '
           'underentreprenører, kvalitetssikring og dokumenteret aflevering af el-, ventilations- og '
           'klimaanlæg.'),
          ('Teknisk service',
           'Installation, tavler, styring, fejlfinding og forebyggende vedligehold fra akutte '
           'udkald til afsluttet anlæg. Serviceaftaler fulgt på responstid, kvalitet og '
           'leveringsevne.'),
          ('Økonomi og personale',
           'Fuld P&L, akkordbreve og opmåling; tildeling til sjak og opgørelse af mer- og '
           'mindrearbejde. 1:1, MUS, lærlingeoplæring, LOTO og risikovurdering.'),
          ('Digitale forbedringer',
           'Python/Claude API til tilbudsberegning, tidsplaner, KS-tjeklister og KPI-dashboards; '
           'dokumenteret produktivitetsløft over 40 %.')]),
        ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen',
         'Data Power Consultant ApS · København · 2024–2026 · sideløbende med ELOHVAC',
         '4–10 personer',
         [('Fra behov til overdragelse',
           'Kravafdækning, arkitektur og integration af tekniske og industrielle applikationer; '
           'idriftsættelse, dokumentation og overdragelse til kundens drift.'),
          ('AI og beslutningsstøtte',
           'Ledte AI-/AI coding-afdelingen; LLM-API’er, AI-agenter og kodegenerering med review og '
           'test. Anvendte AI til rapportering, KPI-analyse og beslutningsoplæg.'),
          ('AI i design og ledelse',
           'AI coding til design af tekniske anlæg og industrielle komponenter — beregning, '
           'dimensionering og designvarianter udarbejdet i AI-assisterede arbejdsgange og valideret '
           'fagligt. AI som værktøj i ledelsesarbejdet: mødeopsummeringer, ledelsesrapportering og '
           'beslutningsoplæg med samme struktur hver gang.'),
          ('Planlægning på tværs',
           'Prioriterede opgaver i to sideløbende virksomheder med fælles plan og skriftlige '
           'aftaler.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024',
         '37 samtidige CAPEX-projekter · 25 specialister · 2–10 mio. kr. pr. projekt',
         [('Styring og kommunikation',
           'Fremdrift, økonomi, risici og ressourcer på tværs af engineering, indkøb og anlæg; '
           'månedlig rapportering til ledelse og bygherre og SAP ERP til aktiver og omkostninger.'),
          ('Teknik og kvalitet',
           'Tavler og styring, UPS, nød- og panikbelysning samt ABA/ABV og PDS. FAT/SAT og IQ/OQ/PQ '
           'under GMP; ingen kritiske afvigelser ved aflevering.'),
          ('Energi og analyse',
           'PDCA-program reducerede energiomkostninger med 40 %. A3, 5xHvorfor og Ishikawa til '
           'fejlfinding og forbedring.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige projekter · 2–10 mio. kr. pr. projekt',
         [('Plan og aflevering',
           'Kapacitets- og fremdriftsstyring fra specifikation til aflevering; udbud, tilbud, '
           'aftalegrundlag, underentreprenører og sikkerhedsdokumentation.'),
          ('Daglig styring',
           'Tavlemøder, flaskehalsanalyse og standardiserede arbejdsgange med forbedret '
           'leveringsevne.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos, Lynetten · København · aug. 2017–jan. 2022',
         'El- og mekaniske anlæg · døgnbemandet drift',
         [('Drift og lager',
           'Fejlfinding og forebyggende vedligehold af pumper, HVAC, højspændingstavler og SCADA. '
           '5S, Standard Work og PDCA på værksted og reservedelslager.'),
          ('Sikkerhed',
           'LOTO, APV, risikovurdering og opfølgning på nærved-hændelser i skifteholdsdrift.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere',
         [('Værksted',
           'Vagtplanlægning, materialestyring, fejldiagnose og reparation af industrielle el- og '
           'mekaniske anlæg; rodårsagsanalyse og korrigerende handlinger.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for a, b in bullets:
            m.bullet(a, b, after=15)
    m.section('UDDANNELSE OG CERTIFICERING')
    for a, b in [
        ('B.Tech, Technology Management & Mechanical Engineering — maskinmesterretningen',
         'Maskinmesterskolen København · 2017–2022 · EQF 6'),
        ('El- og maskinteknisk design, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6'),
        ('HF, matematik og fysik', 'VUC · 2012–2017'),
        ('Elautoriseret maskinmester', 'Sikkerhedsstyrelsen · LV/MV/HV · 2023'),
        ('PRINCE2-certificeret projektleder', 'AXELOS / PeopleCert'),
        ('Køleteknik og klimaanlæg', 'AMU · Mercantec · 2021'),
        ('STCW-certifikater',
         'Maskinrumsvagt og udpegede sikkerhedsopgaver m.fl. · Søfartsstyrelsen · 2021–2023'),
    ]:
        m.edu(a, b)

    m.section('KERNEKOMPETENCER TIL KUNDECENTERET')
    for a, b in [
        ('Kundekontakt og kundeservice',
         'Rådgivning om installation og drift, håndtering af kundehenvendelser, klare aftaler og '
         'opfølgning, der holder kunden orienteret.'),
        ('Planlægning og booking',
         'Planlægning af servicemontører, kalenderstyring, kapacitet, ændringer og kommunikation '
         'til kunde og montør.'),
        ('Teknisk forståelse',
         'El-, installations- og klimaforhold, så henvendelserne kan besvares præcist og '
         'videregives korrekt til den rette specialist.'),
        ('Systemer og registrering',
         'MS Office, Excel/Power Query, SAP ERP og kundecentrets it-systemer; Python og Claude API '
         'til egne værktøjer, rapportering og automatisering.'),
        ('Sprog og samarbejde',
         'Dansk og engelsk i skrift og tale, tæt dialog med kunder, teknikere og kolleger, og '
         'eskalering til specialister, når opgaven kræver det.'),
        ('Egenskab og metode',
         'Ejerskab, struktur, prioritering under travlhed, opfølgning af aftaler og løbende '
         'forbedring af egen arbejdsgang.'),
    ]:
        m.bullet(a, b, after=25)
    m.page_break()
    m.models_table('PRAKTISK OPSTART — FORSLAG TIL DE FØRSTE 90 DAGE',
                   ('Tid', 'Prioritet og konkret leverance'),
                   [('Dag 1–30',
                     'Lær kundecentrets arbejdsgange, it-systemer og produkter fra kolleger og en '
                     'erfaren servicemontør: hvordan en henvendelse registreres, hvornår en booking '
                     'kræver godkendelse, og hvilke oplysninger montøren har brug for. Få overblik '
                     'over faste kunder, serviceaftaler og de hyppigste spørgsmål, og bed om at svare '
                     'på egne cases.'),
                    ('Dag 31–60',
                     'Overtag egne kundehenvendelser og bookings i et måleligt omfang, og følg dem '
                     'til aflevering. Hold en ugentlig gennemgang af åbne sager, afventende svar og '
                     'ændringer sammen med teamlederen, så prioritering og ejerskab er synlige. '
                     'Dokumentér de hyppigste spørgsmål, så svarene bliver ensartede på dansk og '
                     'engelsk.'),
                    ('Dag 61–90',
                     'Evaluer pålidelighed, svartid og fejl i registreringen sammen med holdet, og '
                     'rettér de hyppigste. Tag ansvar for én tilbagevendende henvendelsestype, så '
                     'specialviden samles hos én. Foreslå forbedringer af systemer og rutiner, og '
                     'vis i praksis, at kunden får samme svar, uanset hvem der tager imod.')])
    m.section('FØR EN BOOKING ER BEKRÆFTET')
    for a, b in [
        ('Kundens oplysninger',
         'Navn, adresse, adgang til installationen og et kontaktnummer, der virker — kontrolleret i '
         'systemet, så en montør ikke skal ringe for at finde ud af noget grundlæggende.'),
        ('Selve installationen',
         'Hvilken ladestander der skal sættes op, om der er en eksisterende installation, hvor den '
         'sidder i forhold til el-tavlen, og hvilke fysiske forhindringer kunden kender til.'),
        ('Tidsrummet',
         'Det aftalte tidsrum og adgangstidspunkt bekræftes mod montørens plan, så tiden er realistisk '
         'og ikke bygget på en antagelse om, hvor langt installationen tager.'),
        ('Forbehold',
         'Kundens og ELCONs forbehold registreres, så montøren ikke møder en uventet situation, og '
         'kunden ved, hvad der er aftalt og hvad der ikke er.'),
        ('Dokumentation og opfølgning',
         'Kunden får en skriftlig bekræftelse med tid, adresse og kontakt. Aftalen skal kunne '
         'efterprøves af kunden, af montøren og af kollegerne, og det skal fremgå, hvem der følger op '
         'og hvornår.'),
    ]:
        m.bullet(a, b, after=20)
    m.section('KONKRETE AFKLARINGER')
    m.para(
        'Direkte callcentererfaring og specifik booking af ladestanderinstallationer fremgår ikke af '
        'den dokumenterede erfaring; kunde- og planlægningsarbejdet er fra egen virksomhed, '
        'installationer og projekter. Motivationen for netop en juniorrolle i et kundecenter, '
        'praktisk tilgængelighed og overgang fra ELOHVAC afklares med ELCON. ELCONs konkrete '
        'it-systemer og de præcise bookingregler er ikke kendt på forhånd og læres i samarbejde med '
        'teamet.', after=60)
    m.section('NØGLEORD (ATS)')
    m.para(
        'Junior Planlægger · kundecenter · kundeservice · kunder · ladestander · installation · '
        'servicemontør · planlægning · booking · kundehenvendelser · dansk · engelsk · MS Office · '
        'it-systemer · team · opfølgning · Glostrup', after=40)
    return m.save(path,
                  title='Ansøgning og CV — Junior Planlægger, ELCON',
                  subject='Kundeservice, booking og montørplanlægning',
                  keywords='Junior Planlægger, kundecenter, kundeservice, ladestander, booking, Glostrup')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_ELCON_JuniorPlanlaegger_679.docx')))
