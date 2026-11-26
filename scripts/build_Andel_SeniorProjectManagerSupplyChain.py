# -*- coding: utf-8 -*-
"""Senior Project Manager, Supply Chain — Andel (dansk opslag, dansk dokument).

4 sider i masterdesign: brev side 1, CV side 2-3, kravmatrix side 4.
Kontaktperson fra opslaget: Supply Chain Director Jesper Storm Nielsen (+45 23 47 68 13).

STILVALG (style_guard godkendt, 3/3 skift mod #417):
  register     = Andelstanken (formål · fællesskab · tillid · sammenhold · den grønne omstilling)
  åbningsgreb  = AS (hverdagen hos dem, der skal bruge materialerne: kollegerne på elnettet som
                 programmets målestok)
  struktur     = Flowet fra plan til retur (planlægning · indkøb · lager · levering · retur)

BRUGERENS KORREKTION + permanent regel: alt tekst humaniseret, menneskeskrevet i brev OG CV.
BANNED: "den rette kandidat" (opslagets slutning) citeres aldrig. Ingen em dash.

EVIDENSGRÆNSER: SAP S/4HANA og SAP EWM ikke brugt (fordel i opslaget, skrives ærligt). Supply
chain-erfaringen kommer fra entreprise/service-siden (indkøb, lager, logistik, materialestyring,
P&L), ikke fra en koncernfunktion; det skrives som det er.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Andel · Senior Project Manager, Supply Chain'
BANNER_RESUME = 'Programledelse fra plan til drift · Supply Chain'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('25. november 2026')
    m.meta('Andel · Supply Chain-programmet fra plan til drift')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Senior Project Manager, Supply Chain', bold=True, color='1A1A1A')
    m.para('Kære Jesper Storm Nielsen,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('Det, programmet i bund og grund handler om, står i opslaget: Når vi kender '
       'materialebehovet tidligere og arbejder efter fælles processer, kan vi levere de rigtige '
       'materialer til tiden og styre lagerbeholdningen bedre. Mit billede af det begynder hos '
       'dem, der skal bruge materialerne: kollegerne, der udbygger og vedligeholder elnettet og '
       'leverer energi og fiber. Hvis ikke deres uge fungerer, har programplanen ikke gjort sin '
       'del. Og det er derigennem, programmet i sidste ende kan understøtte den grønne '
       'omstilling.')

    lp('Programmet dækker hele flowet fra planlægning af materialebehov og operationelt indkøb '
       'til lager, levering og retur på tværs af koncernen, og rollen er den daglige programledelse: at omsætte '
       "programmets mål og rammer til en plan, drive arbejdet fra design til implementering og "
       'følge op på, om de nye arbejdsgange virker i driften. Andels selskaber har forskellige '
       'forretningsmodeller og behov, og min tilgang til den del er enkel: hvor fælles '
       'processer skaber værdi, skal de være fælles, og hvor arbejdsgangene skal tilpasses den '
       'lokale drift, skal de det.')

    lp('Min erfaring med den type arbejde kommer fra projekter, der skulle ende som drift. 37 '
       'anlægsprojekter fra design til idriftsættelse og aflevering på Novo Nordisk, 11 '
       'samtidige entrepriser med daglig opfølgning, og et el-servicefirma, hvor nye '
       'arbejdsgange blev omsat til krav til data og systemer, før de blev til praksis. Og I '
       'har fat i den rigtige side af bordet med 32 medarbejdere, der dækker operationelt '
       'indkøb, lager, logistik og masterdata. Jeg har samlet ledere og medarbejdere om '
       'beslutninger på tværs af engineering, indkøb, drift og '
       'økonomi, og jeg ved, hvordan beslutninger bliver til nye arbejdsgange i driften: ved at '
       'tage dem, der skal bruge dem, med i arbejdet, og skabe fremdrift, når interessenter '
       'har forskellige behov. At afklare, hvem der ejer processerne og '
       'har mandat til at træffe beslutninger, er ikke en detalje for mig; det er den del af '
       'planen, der afgør resten. Vi deler vores viden, taler åbent om det, der spænder ben i '
       'hverdagen, og finder løsninger sammen, og sådan har jeg kørt tavlemøder og 1:1 i ti år.')

    lp('Data til at prioritere indsatser og følge op på effekten er sådan, jeg arbejder: '
       'KPI-opfølgning hver måned, Power BI og egne værktøjer i Python til fremdrift og '
       'økonomi. Programplaner, milepæle, risici og afhængigheder mellem spor kender jeg fra '
       'PRINCE2 og fra 37 projekter i træk. Og så en ærlig note: SAP S/4HANA, SAP EWM har jeg '
       'ikke siddet i. Jeg kender SAP ERP og har flyttet arbejdsgange over i nye systemer før, '
       'så jeg lærer jeres systemer hurtigt, men jeg vil ikke love et system, jeg ikke har '
       'brugt.')

    lp('Din sætning om, at når vi får planlægning, indkøb, lager og logistik til at spille '
       'bedre sammen, gør vi hverdagen lettere for kollegerne i driften, er sådan jeg ser '
       'programarbejdet. Og din beskrivelse af andelstanken i praksis, når vi tager ansvar for '
       'helheden og udvikler løsninger sammen med dem, der skal bruge dem, følger med. '
       'Formål, faglighed og fællesskab i et demokratisk-ejet andelsselskab, der tænker '
       'langsigtet og formålsdrevet, tiltaler mig. Vores andelskultur er kendetegnet ved '
       'sammenhold og relationer der bunder i tillid, og at forandringer er velkomne som en '
       'vigtig del af dagligdagen passer med det tempo, jeg selv trives i. Og du kommer tæt '
       'på driften og kan se, hvordan dit arbejde har betydning for deres hverdag. Det er en '
       'af grundene til, jeg søger netop her.')

    lp('De første 90 dage står som en plan side 3 i CV\'et, skrevet så I kan holde mig op på '
       'den: de første 30 dage lytte og kortlægge flowet sammen med selskaberne, derefter '
       'programplan og fælles processer med klare ejere, og til sidst udrulning og mål med '
       'driften. Lokationerne Ballerup, Haslev, Virum, Svinninge og Sydhavn passer mig fint; '
       'jeg bor i Måløv i Ballerup Kommune. Jeg kan tiltræde efter aftale, og jeg kan træffes '
       'på +45 93 99 95 14 eller ajlooshahram@gmail.com, også hvis du vil have noget uddybet '
       'inden samtalen.', after=44)

    lp('Med venlig hilsen', after=8)
    lp('Shahram Ajloo', after=8)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Program- og projektleder med supply chain-kæden fra den udførende side: indkøb, '
           'lager, logistik og aflevering i entreprise og service, og større projekter fra '
           'design til implementering. 37 CAPEX-projekter på Novo Nordisk under GMP/FDA/EMA, 11 '
           'samtidige entrepriser med fuldt P&L, og nye arbejdsgange omsat til krav til data og '
           'systemer. PRINCE2, data til at prioritere (KPI, Power BI, Python), og SAP ERP fra '
           'økonomisiden.', after=32)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester (el-teknik og ventilation)',
         'Data Power Consultant ApS · København · 2024 – nu',
         'AI-afdeling 4-10 personer · el-service og entreprise · 5 elektrikere + 3 lærlinge',
         [('', 'Leder AI-afdelingen med 4 til 10 personer: tilbud, kunder, og hvordan løsninger '
               'bliver bygget og dokumenteret. Investeringstilbud og månedlig KPI-opfølgning.'),
          ('', 'Nye arbejdsgange omsat til krav til data og systemer: digitale tjeklister og '
               'rapportflow i Python og Claude, med dokumentation over 40% hurtigere siden '
               '2024.')]),
        ('Ejer / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 – nov. 2026 (virksomheden lukket)',
         'Erhvervskunder · el, ventilation og klima · entreprise · fuldt P&L',
         [('', 'Tilbud, planlægning, materialestyring, indkøb og underentreprenører i entreprise '
               'med fuldt P&L-ansvar. Lager og leverancer fulgt fra ordre til aflevering, og '
               'KS, dokumentation og aflevering i hver kontrakt.'),
          ('', 'Personaleledelse af 5 elektrikere og 3 lærlinge: daglig planlægning, 1:1 og MUS. '
               'Fælles plan og nye arbejdsgange indført på tværs af ELOHVAC og Data Power.')]),
        ('Senior commissioningeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, DKK 2-10 mio. · 25 specialister · GMP/FDA/EMA',
         [('', 'Commissioning og projektledelse på 37 CAPEX-projekter, DKK 2-10 mio. pr. stk., '
               'fra design til implementering og aflevering. FAT/SAT og IQ/OQ/PQ under '
               'GMP/FDA/EMA, nul kritiske fund.'),
          ('', 'Månedsrapport til ledelse og kunde om fremdrift, økonomi, risici og ressourcer. '
               '25 specialister på tværs af engineering, indkøb og drift. SAP ERP til '
               'økonomidata.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022 – nov. 2022',
         '11 samtidige projekter · 14 mand · lager og logistik',
         [('', '11 samtidige projekter og et team på 14 mand. Daglige tavler for kapacitet og '
               'fremdrift, lager og logistik, sikkerhedsdokumentation og afleveringspakker i '
               'hvert projekt.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · SCADA, PLC, HV-tavler · skiftehold',
         [('', 'Vedligehold og drift af pumper, HVAC, HV-tavler, SCADA og PLC døgnet rundt. '
               'Planlagt og korrigerende vedligehold, fejlfinding, og 5S og Standard Work i '
               'værkstedet. Skiftehold med LOTO, APV og nærved-hændelser.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('', 'Ledelse af 12 mekanikere og teknikere i maskinværksted: vagtplan, materialer og '
               'mål. Fejlfinding på industrielt udstyr, analyse af rodårsag og korrigerende '
               'handlinger.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('UDDANNELSE OG CERTIFIKATER')
    m.edu('B.Tech (EQF6), teknologiledelse og maskinteknik',
          'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12')
    m.edu('Dansk elautorisation LV/MV/HV som elautoriseret maskinmester',
          'Sikkerhedsstyrelsen · maj 2023')
    m.edu('El- og maskinteknisk design, elteknik (EQF6)',
          'Tehran Technical University · 2000–2003')
    m.edu('PRINCE2, certificeret projektleder', 'AXELOS / PeopleCert')
    m.edu('Køleteknik og klimaanlæg (AMU)',
          'Mercantec · 2021 · STCW 2021–2023, Søfartsstyrelsen')
    m.para('Lean- og Six Sigma-praksis uden certifikat: DMAIC, 5S, PDCA, VSM, A3, Kaizen, '
           'Standard Work, SMED, TPM, 5xHvorfor, Ishikawa og FMEA, brugt i dokumenteret arbejde '
           'med vedligehold, kvalitet og planlægning.', after=48)

    m.section('SPROG, VÆRKTØJER OG PRAKTISK')
    m.para('Dansk (modersmål) · engelsk (professionelt) · persisk (modersmål). SAP ERP, Power '
           'BI, Excel og Python til opfølgning og beslutningsgrundlag, PRINCE2 til '
           'programstruktur, tavlemøder og 1:1 som faste rutiner. Kørekort B. Bor i Måløv i '
           'Ballerup Kommune. Kan tiltræde efter aftale.', after=48)

    m.section('KOMPETENCER')
    for label, body in [
        ('Program og plan',
         'Programplaner, milepæle, ressourcer, risici og afhængigheder styret med PRINCE2 og '
         'daglige tavler. Beslutningsoplæg og opfølgning på beslutninger.'),
        ('Supply chain',
         'Planlægning, indkøb, lager, logistik og retur fra entreprise og service: '
         'materialestyring, leverancer og aflevering fulgt i praksis.'),
        ('Data',
         'KPI-opfølgning, Power BI, Excel og Python. Data til at prioritere indsatser og følge '
         'op på effekten, ikke kun til rapportering.'),
        ('Forandringer',
         'Forankring i drift via tavlemøder, 1:1 og oplæring. Beslutninger testet i drift, før '
         'de bliver standard.'),
        ('Systemer',
         'SAP ERP siden 2022, og arbejdsgange omsat til systemkrav i egne værktøjer. SAP S/4HANA '
         'og EWM ikke brugt endnu.'),
    ]:
        m.bullet(label, body, after=10)

    m.section('DE FØRSTE 90 DAGE')
    m.para('En plan for de første 90 dage, som I kan holde mig op på:', after=12)
    for b in [
        'Dag 1-30: Lære flowet og selskaberne at kende. Samtaler med kolleger i Supply Chain, '
        'Indkøb, Lager, Drift, Økonomi og IT, og et kortlægningsforløb af, hvor kæden i dag '
        'taber tid og materialer. Mål: et fælles billede af flowet fra plan til retur.',
        'Dag 31-60: Programplanen lægges, og de første fælles processer udvikles med klare '
        'ejere og mandat til at træffe beslutninger. Milepæle, ressourcer og fremdrift sat i '
        'system. Mål: planen godkendt hos dig, Jesper, og de første beslutningsoplæg klar til '
        'styregruppe-mødet.',
        'Dag 61-90: Udrulning i første spor sammen med de ledere og medarbejdere, der skal '
        'bruge de nye arbejdsgange, og aftalte mål med driften. Mål: første effekt målt på '
        'forsyningssikkerheden eller kapitalbinding.',
    ]:
        m.bullet('', b, after=10)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Andel · End-to-End Supply Chain-programmet',
                   ('Krav i opslaget', 'Dokumenteret erfaring'), [
        ('Lede større projekter eller programmer fra design til implementering',
         '37 CAPEX-projekter ledet fra design til implementering og aflevering (Novo Nordisk, '
         '2022-2024), 11 samtidige entrepriser med daglig programlignende opfølgning (2022), og '
         'PRINCE2 som metode. Projekter på DKK 2-10 mio. styret på tid, økonomi og kvalitet.'),
        ('Solid forståelse for End-to-End Supply Chain-processer',
         'Kæden fra den udførende side i 20+ år: planlægning af materialebehov, indkøb, lager, '
         'logistik, levering og aflevering i entreprise og service med fuldt P&L-ansvar '
         '(2023-2026). Forstår, hvad en arbejdsgang betyder ude på lageret og på pladsen.'),
        ('Udvikle fælles arbejdsgange og omsætte dem til krav til data og systemer',
         'Fælles plan og arbejdsgange indført på tværs af to selskaber (ELOHVAC og Data Power). '
         'Nye arbejdsgange omsat til digitale tjeklister og rapportflow i Python og Claude siden '
         '2024, med dokumentation over 40% hurtigere.'),
        ('Bruge data til at prioritere indsatser og følge op på effekten',
         'Månedlig KPI-opfølgning siden 2022, Power BI og Python til fremdrift og økonomi, og '
         'effektfulgt: PDCA-forløb med 40% lavere energiomkostninger og dokumentationshastighed '
         'over 40% bedre. Data brugt til prioritering, ikke kun til rapport.'),
        ('Samle ledere og medarbejdere om beslutninger og forankre nye arbejdsgange i '
         'driften',
         'Tværfaglig samling af 25 specialister (engineering, indkøb, drift) på Novo Nordisk, '
         'daglige tavlemøder med 14 mand, og forankring via 1:1, MUS og oplæring af 3 lærlinge. '
         'Nye arbejdsgange holdt i drift, fordi dem der brugte dem, var med til at lave dem.'),
        ('Lægge programplanen og følge op på milepæle, ressourcer og fremdrift',
         'PRINCE2-rammer brugt på 37 projekter i træk: plan, milepæle, ressourcer og fremdrift '
         'fulgt månedligt mod ledelse og kunde, og daglige tavler for kapacitet på 11 samtidige '
         'projekter. Ingen milepæl uden ejer og dato.'),
        ('Udvikle fælles processer og afklare, hvem der ejer processerne og har mandat til at '
         'træffe beslutninger',
         'Akkord og opmåling indført med klare ejere og mandater (ELOHVAC, bekræftet praksis), '
         'og fælles processer på tværs af to selskaber med skrevne aftaler om, hvem der beslutter '
         'hvad. Det er en vane fra entreprise: hvert grænseflade har en navngivet ansvarlig.'),
        ('Håndtere risici og afhængigheder mellem programmets spor',
         'Risici og afhængigheder styret på 37 projekter med 25 specialister og '
         'underentreprenører, og 11 spor kørt parallelt med daglig afhængighedskontrol (2022). '
         'Risikodelen i månedsrapporten blev brugt aktivt i styringen.'),
        ('Udarbejde beslutningsoplæg til styregruppen og følge op på beslutninger',
         'Beslutningsgrundlag og månedsrapporter til ledelse, kunde og bestyrelse siden 2022, og '
         'opfølgning på beslutninger som fast punkt. Som direktør selv siddet på den anden side '
         'af bordet og modtaget oplæggene.'),
        ('Samle selskaberne og kolleger fra bl.a. Supply Chain, Indkøb, Lager, Drift, Økonomi og '
         'IT om løsningerne',
         'Samarbejde på tværs af engineering, indkøb, drift og økonomi dagligt (2022-2024), og '
         'IT-siden fra egne systembyggerier siden 2024. To selskaber samlet om én plan '
         '(ELOHVAC/Data Power). Rollefordeling: jeg samler, de faglige ejer.'),
        ('Planlægge udrulningen sammen med de ledere og medarbejdere, der skal bruge de nye '
         'arbejdsgange',
         'Udrulning af nye arbejdsgange med de berørte som deltagere: digitale tjeklister indført '
         'med elektrikerne (2024), 5S og Standard Work i værkstedet med folkene selv (2017-2022), '
         'og oplæring af 3 lærlinge i nye rutiner.'),
        ('Aftale mål med driften og følge op på programmets effekt på forsyningssikkerhed, '
         'kapitalbinding og omkostninger',
         'Mål aftalt i 1:1 og på tavler og fulgt op månedligt (2023-2026). Effekt dokumenteret: '
         '40% lavere energiomkostninger via PDCA, 40% hurtigere dokumentation, og responstid og '
         'leveringsevne som KPI i serviceaftaler. Kapitalbinding fra lager- og materialestyring.'),
        ('SAP S/4HANA, SAP EWM eller tilsvarende ERP- og lagersystemer',
         'Ærligt: SAP S/4HANA og SAP EWM har jeg ikke brugt. SAP ERP kender jeg fra økonomi- og '
         'omkostningsopfølgning siden 2022, og jeg har flyttet arbejdsgange over i nye systemer '
         '(egne værktøjer i Python og Claude siden 2024). Systemerne lærer jeg; det er en fordel '
         'i opslaget, ikke et krav.'),
        ('Du trives med at skifte mellem programplanen og konkrete spørgsmål fra driften',
         'Hverdagen som projektleder og direktør har været netop det skift: programplanen om '
         'formiddagen og et spørgsmål om en ventil eller en levering om eftermiddagen. 11 '
         'samtidige projekter og akutte udkald imellem de planlagte opgaver i 3+ år.'),
        ('Du har ledet større forandringer på tværs af en organisation og ved, hvordan '
         'beslutninger bliver til nye arbejdsgange i driften',
         'Forandringer ledet i praksis: digitalisering af dokumentation og rapportering (2024), '
         'fælles plan på tværs af to selskaber, og nye vedligeholdsrutiner på Biofos fra 2017. '
         'Beslutninger blev til arbejdsgange, fordi de blev testet i drift inden de blev standard.'),
    ], widths=(3400, 6946), compact=True)
    m.para('**Spørgsmål til stillingen kan stilles til Supply Chain Director Jesper Storm '
           'Nielsen på +45 23 47 68 13. Jeg kan træffes på +45 93 99 95 14 eller '
           'ajlooshahram@gmail.com.**', after=8)

    m.save(path, title='Senior Project Manager, Supply Chain - Andel')
    print(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_Andel_SeniorProjectManagerSupplyChain.docx'))
