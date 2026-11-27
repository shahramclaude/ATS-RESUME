#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Operations Manager — NordicCell ApS, Symbion Science Park, København.

Dansk opslag -> DANSK dokument i masterdesign (4 sider). TEMPLATE
Gentofte-2027 (dansk kæde). Søges via Basico; kontakt Benedikte Rindom
Gerstenberg, Director, Executive Search & Recruitment, +45 31 56 03 66.

BRUGERSVAR (bindende):
1. Business Central = SAP-overført: SAP daglig bruger (kanon) som solid
   ERP-baggrund, Business Central som overført viden/opleerbar — ÆRLIGT,
   ingen påstand om BC-erfaring.
2. Power BI = interesse; rapportering/KPI-dashboards REEL (Excel, AI-værktøjer).
3. Supply chain/lager/indkøb/ordreflow/logistik = REEL -> selvsikkert.
4. Lokation Symbion, København = commute_ok -> konkret.

STIL (3/3 mod #444 NOVENCO): register "Nær ledelse, roligt overblik",
åbning BU (flowets kæde), struktur "Flow, team, udvikling" (30/60/90).
Intet genbrug fra NOVENCO. Ingen em dash. 'elautoriseret maskinmester'
i CV-titler som kanonisk.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_Gentofte_DriftslederEjendomme_2027.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'NordicCell · Operations Manager, København'
BANNER_RESUME = 'DRIFT · SUPPLY CHAIN · TEAMLEDELSE · SYSTEMER'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('29. november 2026')
    m.meta('NordicCell ApS · Symbion Science Park, København')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning om stillingen som Operations Manager', bold=True,
           color='1A1A1A')
    m.para('Kære Benedikte Rindom Gerstenberg,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('En ordre hos NordicCell begynder i webshoppen og slutter først, når '
       'udstyret er fremme hos klinikken i Norden eller EMEA, og fakturaen er '
       'sendt. Derimellem ligger indkøb, lager, logistik og Business Central, '
       'og hvert led skal hænge sammen med det næste. Når et slip i '
       'ordreflowet til sidst mærkes hos en fertilitetsklinik, der venter på '
       'udstyr, er det for sent at finde sammenhængen.')

    lp('Rollen som Operations Manager er den koordinerende drivkraft i den '
       'kæde, og som bindeled mellem direktøren, teamet, lageret og de '
       'eksterne samarbejdspartnere er det et vigtigt bindeled, og opgaven er at skabe sammenhæng mellem '
       'ordreflow, indkøb, lager, webshop, Business Central, logistik og '
       'fakturering. Teamledelse, daglig drift og udvikling i samme rolle '
       'passer mig: tydelig prioritering, opfølgning og ansvarsfordeling i '
       'teamet, og bidrager selv hands-on, når det er nødvendigt. Rollen kombinerer det at skabe overblik i hverdagen og drive forbedringer af processer, systemunderstøttelse og samarbejdsformer.')

    lp('Siden 2003 har jeg arbejdet med supply chain, logistik, indkøb og '
       'lagerstyring i praksis, i produktion, service og entreprise: indkøb og '
       'materialestyring, lager og reservedelsstyring, leverandører og '
       'leverancer fulgt til dørs, og økonomien i det hele set fra både '
       'bogholderiet og bundlinjen. Min ERP-baggrund er SAP i daglig brug '
       'siden 2017, og Microsoft Dynamics 365 Business Central er et system, '
       'jeg tager fat på med erfaringen fra SAP: strukturen er genkendelig, '
       'og datakvalitet og flow betyder det samme i begge. Rapportering og '
       'KPI-overblik har jeg bygget i praksis, og Power BI er det værktøj, '
       'jeg gerne vil dykke dybere i.')

    lp('De første 90 dage følger opgavens tre sider. Dag 1-30 er flowet: her '
       'ordreflowet fra webshop til fakturering gennemgået led for led, '
       'lagerbeholdning og leverancer afstemt, og samspillet mellem webshop, '
       'Business Central, lager, logistik og fakturering kortlagt før der '
       'ændres på noget. Dag 31-60 er teamet: daglig teamledelse og koordinering '
       'med tydelig retning, ressourcer fordelt, og tværgående opgaver fulgt '
       'systematisk. Dag 61-90 er udviklingen: procesforbedringer og '
       'systemunderstøttelse, og datakvalitet og drive løbende procesforbedringer sættes i en fast rytme.')

    lp('Som person er jeg en tydelig og rolig leder, som tager ansvar, tør '
       'prioritere og skaber fremdrift, og jeg arbejder struktureret og '
       'vedholdende med blik for både detaljerne og den større sammenhæng. En '
       'mindre organisation, hvor man arbejder tæt sammen, hjælper hinanden og '
       'har en naturlig dialog i hverdagen, er det miljø, jeg trives bedst i, '
       'og nærheden og fleksibiliteten i en mindre organisation med tæt på '
       'både kolleger, beslutninger og den daglige drift er præcis det, '
       'NordicCell tilbyder. Min arbejdsform er nysgerrig og ydmyg over for eksisterende '
       'arbejdsgange: jeg sætter mig ind i, hvad der '
       'allerede fungerer, før du foreslår ændringer, og en hands-on-rolle, '
       'hvor du både leder, koordinerer og selv bidrager praktisk, er den '
       'jeg kender fra værkstedsgulvet og kontoret.')

    lp('Med dansk flydende og stærke engelskkundskaber i både skrift og tale har '
       'jeg brugt dagligt i årevis, både med kunder i Norden og EMEA og med '
       'internationale leverandører. Uddannelsesmæssigt er min baggrund '
       'teknologiledelse og maskinmester, ikke logistiklinjen, og solid '
       'erfaring kan dog kompensere for en anden uddannelsesbaggrund, som der '
       'står i opslaget. Erfaring fra fertilitetsområdet har jeg ikke, men '
       'NordicCell er en specialiseret distributør af udstyr og løsninger til '
       'fertilitetsbehandling, og det vigtigste er noget andet: en stærk '
       'driftsforståelse, gode '
       'systemkompetencer og lyst til at skabe struktur og forbedringer, og '
       'det er præcis det, jeg bringer. Ambitionen om at fordoble omsætningen '
       'på det europæiske marked er en rejse, jeg gerne vil være med på, '
       'som en central del af NordicCells videre digitalisering og udvikling, '
       'med korte beslutningsveje og en bred kontaktflade. Symbion ligger nemt fra '
       'Måløv, og jeg kan starte hurtigt. Jeg ser frem til at høre fra dig.',
       after=44)

    m.para('Med venlig hilsen', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Drifts- og supply chain-profil med 20+ år i koordinering, indkøb '
           'og styring af flow fra ordre til levering. SAP som dagligt '
           'arbejdsredskab siden 2017, rapportering og KPI-overblik bygget i '
           'praksis, og teamledelse på tværs af funktioner siden 2003. '
           'Struktureret og vedholdende, med blik for både detaljerne og den '
           'større sammenhæng, og lige så hjemme på lageret som ved '
           'systemet.', after=32)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester (el-teknik og ventilation)',
         'Data Power Consultant ApS · København · 2024 – nu (fra nov. 2026 også ELOHVACs '
         'el-tekniske aktiviteter)',
         'AI-afdeling 4-10 personer · el-service og entreprise · 5 elektrikere + 3 lærlinge',
         [('Koordinering og flow', 'Opgaver og ressourcer koordineret på tværs '
           'af teams på 4-10 specialister, med indkøb, materialestyring og '
           'leverancer planlagt pr. sag. Tværgående opgaver fulgt til dørs, '
           'og dokumentation og aflevering holdt i orden undervejs.')]),
        ('Ejer / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 – nov. 2026 (virksomheden lukket)',
         'Erhvervskunder · el, ventilation og klima · entreprise · fuldt P&L · serviceaftaler',
         [('Indkøb, økonomi og kunder', 'Indkøb, materialestyring og '
           'prisberegning i tilbud og ordreflow, fakturering og bogholderi '
           'ført med månedlig opfølgning på driftsøkonomien. Serviceaftaler '
           'med erhvervskunder og leverandørkontrakter styret med tydelig '
           'prioritering og opfølgning.')]),
        ('Senior commissioningeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, DKK 2-10 mio. · 25 specialister · GMP/FDA/EMA',
         [('Struktur i stort flow', '37 sideløbende projekter planlagt og '
           'fulgt med materialestyring, leverancer og dokumentation i faste '
           'rammer. Datakvalitet i registreringerne var en forudsætning, og '
           '25 specialister og leverandører koordineret mod fælles '
           'deadline.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022 – nov. 2022',
         '11 projekter · 14 mand · underleverandører · montage og aflevering',
         [('Ressourcer og leverancer', 'Ressourcer fordelt og fulgt op på '
           'tværs af 11 projekter: 14 mand, underleverandører og leverancer '
           'planlagt uge for uge, og lager og materialestyring holdt ajour, '
           'så montage ikke stod stille.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · kritiske anlæg · 10 medarbejdere · skiftehold',
         [('Lager og drift døgnet rundt', 'Reservedelsstyring og lagerbeholdning '
           'holdt, så reparationer ikke ventede, og 10 medarbejdere på '
           'skiftehold koordineret med tydelig retning. Driften kørte døgnet '
           'rundt, og både datakvalitet i CMMS og opfølgning på leverancer '
           'var en del af hverdagen.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('Produktion og team', 'Produktion og lager i et maskinværksted med '
           '12 mekanikere og teknikere: ordreflow fra opgave til færdigt '
           'emne, indkøb af materialer og teamkoordinering i daglig drift, '
           'hvor alle hjalp hinanden, når det spidsede til.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('UDDANNELSE OG CERTIFIKATER')
    m.edu('B.Tech (EQF6), teknologiledelse og maskinteknik',
          'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12')
    m.edu('Dansk elautorisation LV/MV/HV som elautoriseret maskinmester', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('El- og maskinteknisk design, elteknik (EQF6)', 'Tehran Technical University · 2000–2003')
    m.edu('PRINCE2, certificeret projektleder', 'AXELOS / PeopleCert')
    m.edu('Køleteknik og klimaanlæg (AMU)', 'Mercantec · 2021 · STCW 2021–2023, Søfartsstyrelsen')

    m.section('KOMPETENCER')
    m.bullet('Flow og supply chain', 'Indkøb, lagerstyring, leverancer og '
             'logistik styret som ét flow, fra ordre til levering. '
             'Lagerbeholdning og reservedelsstyring holdt i orden, så '
             'fremdriften ikke afhang af gætterier.', after=10)
    m.bullet('Systemer og data', 'SAP i daglig brug siden 2017, ERP-forståelse '
             'der overføres direkte til Microsoft Dynamics 365 Business '
             'Central, og rapportering og KPI-overblik bygget i praksis. '
             'Power BI som næste værktøj, og digitalisering, '
             'systemintegrationer og procesoptimering som interesse, der '
             'løbende omsættes.', after=10)
    m.bullet('Team og koordinering', 'Daglig teamledelse med tydelig retning '
             'og ansvarsfordeling siden 2003: skiftehold, montagehold og '
             'fagteams. Ressourcer koordineret, tværgående opgaver fulgt op, '
             'og alle vidste, hvem der gjorde hvad.', after=10)
    m.bullet('Økonomi og opfølgning', 'God økonomisk forståelse fra fuldt '
             'P&L-ansvar, budget og fakturering til månedlig opfølgning. '
             'Som fast disciplin, ikke som kampagner, følger datakvalitet og drive '
             'løbende procesforbedringer med.', after=10)

    m.section('DE FØRSTE 90 DAGE')
    m.para('Planen følger opgaven: flowet, teamet, udviklingen.', after=8)
    m.bullet('Dag 1-30 · Flowet', 'Ordreflowet fra webshop til fakturering '
             'gennemgået led for led, og samspillet mellem webshop, Business '
             'Central, lager, logistik og fakturering kortlagt. Mål: jeg kender '
             'kæden, før der ændres på den.', after=10)
    m.bullet('Dag 31-60 · Teamet', 'Daglig teamledelse og koordinering med '
             'tydelig retning, ressourcer fordelt, og tværgående opgaver fulgt '
             'systematisk. Mål: tydelig prioritering, opfølgning og '
             'ansvarsfordeling, som alle kan se.', after=10)
    m.bullet('Dag 61-90 · Udviklingen', 'Procesforbedringer og '
             'systemunderstøttelse prioriteret, og datakvalitet sat i fast '
             'rytme. Mål: forbedringer der holder, bygget på hvad der '
             'allerede fungerer.', after=10)

    m.section('SPROG, VÆRKTØJER OG PRAKTISK')
    m.para('Modersmål dansk · engelsk (professionelt) · persisk (modersmål). '
           'SAP, Excel, CMMS; PRINCE2. Power BI som interesse. Kørekort '
           'kategori B (manuelt gear). Bosat i Måløv; Symbion ligger nemt '
           'derfra.', after=8)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Krav og dokumentation · Operations Manager, NordicCell',
                   ('Krav i opslaget', 'Dokumentation'),
                   [
        ('Supply chain, logistik, indkøb og lagerstyring fra handels-, '
         'produktions- eller distributionsvirksomhed',
         'Arbejdet med supply chain, logistik, indkøb og lagerstyring siden 2003 '
         'i praksis, på tværs af produktion (ARJ 2003-2010), service og '
         'entreprise (ELOHVAC 2023-2026) og projektdrift (Ventek 2022, Novo '
         'Nordisk 2022-2024). Indkøb, materialestyring, lagerbeholdning og '
         'leverancer er velkendte discipliner, ikke teori.'),
        ('Erfaring med teamkoordinering eller teamledelse',
         'Teamkoordinering og teamledelse siden 2003: 12 mekanikere og '
         'teknikere (ARJ), 10 medarbejdere på skiftehold (Biofos 2017-2022), '
         '14 mand på montage (Ventek 2022), 5 elektrikere og 3 lærlinge '
         '(ELOHVAC) og 25 specialister koordineret på tværs (Novo Nordisk). '
         'Daglig teamledelse med tydelig retning og ansvarsfordeling.'),
        ('Stærke brugerkompetencer i Microsoft Dynamics 365 Business Central',
         'Min ERP-baggrund er SAP i daglig brug siden 2017, og Microsoft '
         'Dynamics 365 Business Central tager jeg fat på med den erfaring: '
         'ERP-struktur, datakvalitet og flow er genkendeligt på tværs af '
         'systemer, og oplæringen er kort, når grundforståelsen er på plads. '
         'Ærligt sagt: SAP er mit sprog, Business Central er mit næste.'),
        ('God økonomisk forståelse, især med ERP, Power BI og rapportering',
         'God økonomisk forståelse fra fuldt P&L-ansvar (ELOHVAC 2023-2026): '
         'budget, fakturering og månedlig opfølgning på driftsøkonomi. ERP '
         '(SAP) dagligt siden 2017, rapportering og KPI-overblik bygget i '
         'praksis, og Power BI som værktøj jeg er i gang med at dykke dybere '
         'i.'),
        ('Interesse for digitalisering, systemintegrationer og procesoptimering',
         'Interessen er reel og omsat i praksis: AI-værktøjer taget i brug til '
         'beregning, tidsplaner og KPI-dashboards (ELOHVAC), '
         'systemunderstøttelse af processer i drift (Biofos CMMS), og '
         'digitalisering, systemintegrationer og procesoptimering som noget, '
         'jeg aktivt opsøger viden om.'),
        ('Dansk flydende og stærke engelskkundskaber i både skrift og tale',
         'Med dansk flydende som modersmål og stærke engelskkundskaber i både '
         'skrift og tale brugt professionelt i årevis: kunder og leverandører på tværs af Norden og '
         'internationale samarbejdspartnere, teknisk dokumentation og '
         'forhandlinger på engelsk. Persisk som tredje sprog.'),
        ('Relevant uddannelse inden for logistik, supply chain, handel, økonomi '
         'eller operations',
         'B.Tech (EQF6) i teknologiledelse og maskinteknik (2017-2022) dækker '
         'operations- og ledelsesdelen, og solid erfaring kan dog kompensere '
         'for en anden uddannelsesbaggrund: 20+ års praktisk drift, '
         'økonomistyring og supply chain-erfaring fra virksomheder i vækst og '
         'under pres.'),
        ('Daglig teamledelse, koordinering og tydelig retning',
         'Daglig teamledelse, koordinering og tydelig retning har været '
         'hverdagen siden 2003, senest med 5 elektrikere og 3 lærlinge i '
         'marken (ELOHVAC) og vagtstruktur med 10 medarbejdere (Biofos). '
         'Ansvarsfordeling og opfølgning er en fast rytme, ikke en '
         'undtagelse.'),
        ('Koordinere ressourcer og følge op på tværgående opgaver',
         'Ressourcer koordineret og tværgående opgaver fulgt op på tværs af '
         '11 projekter med 14 mand og underleverandører (Ventek 2022) og 37 '
         'CAPEX-projekter med 25 specialister (Novo Nordisk 2022-2024). '
         'Koordinering på tværs af funktioner er min faste arbejdsform.'),
        ('Optimale processer og effektivt samspil mellem webshop, Business '
         'Central, lager, logistik og fakturering',
         'Samspillet mellem systemer, lager og økonomi har jeg drevet i '
         'praksis: ordreflow fra tilbud til fakturering (ELOHVAC), '
         'materialestyring og leverancer i projektfølge (Novo Nordisk, '
         'Ventek) og lager og reservedelsstyring i døgndrift (Biofos). '
         'Webshop-specifik drift kender jeg som opgavekæde, ikke som tidligere '
         'stilling.'),
        ('Følge op på indkøb, ordreflow, lagerbeholdning og leverancer',
         'Indkøb, ordreflow, lagerbeholdning og leverancer fulgt op som en '
         'samlet disciplin: prisberegning og indkøb i tilbud (ELOHVAC), '
         'reservedelsstyring så reparationer ikke ventede (Biofos, Vestas '
         '2024-2026) og leverancer planlagt uge for uge mod faste deadlines '
         '(Ventek, Novo Nordisk).'),
        ('Datakvalitet og løbende procesforbedringer',
         'Som fast disciplin arbejdes der med datakvalitet og drive løbende procesforbedringer: '
         'CMMS-data der kunne bruges til at planlægge vedligehold på fejldata '
         '(Biofos), dokumentation der holdt til revision (Novo Nordisk), og '
         'procesforbedringer der byggede på hvad der allerede fungerer, før '
         'noget blev ændret.'),
        ('Skabe struktur, prioritere opgaver og sikre fremdrift på tværs af '
         'team, lager, leverandører og kunder',
         'Skabe struktur, prioritere opgaver og sikre fremdrift på tværs af '
         'team, lager, leverandører og kunder har været kernen i arbejdet '
         'siden 2003: fra værksted og produktion i Teheran til serviceaftaler '
         'og entreprise i København, altid med både detaljerne og den større '
         'sammenhæng i kikkerten.'),
        ('Tydelig og rolig leder, som tager ansvar, tør prioritere og skaber '
         'fremdrift',
         'Ledelsesstilen er tydelig og rolig: tager ansvar, tør prioritere og '
         'skaber fremdrift, også når to opgaver kæmper om samme ressource. '
         'Situationsbestemt ledelse fra skiftende byggepladser og vagtordninger '
         'har lært mig at holde hovedet koldt, når tempoet stiger.'),
        ('Struktureret og vedholdende med blik for både detaljerne og den '
         'større sammenhæng',
         'Struktureret og vedholdende arbejdsform: planer der bliver fulgt, '
         'opfølgning der bliver husket, og blik for både detaljerne og den '
         'større sammenhæng, når 37 projekter og 25 specialister skal hænge '
         'sammen i én portefølje.'),
        ('Trives i mindre team med tæt samarbejde og naturlig dialog',
         'Mindre teams er min hjemmebane: værksted med 12 mekanikere, hold på '
         '10 på skiftehold, entreprise med 5 elektrikere og 3 lærlinge. Arbejder '
         'tæt sammen, hjælper hinanden og har en naturlig dialog i hverdagen, '
         'er sådan holdene altid har fungeret omkring mig.'),
        ('Nysgerrig og ydmyg over for eksisterende arbejdsgange',
         'Nysgerrig og ydmyg over for eksisterende arbejdsgange: jeg sætter '
         'mig ind i, hvad der allerede fungerer, før du foreslår ændringer, '
         'og ændringer bygges på den virkelighed, jeg møder, ikke på en '
         'skabelon. Rodårsagsarbejde i ARJ og driftsoptimering i Biofos er '
         'bygget på samme metode.'),
        ('Hands-on-rolle, hvor man både leder, koordinerer og selv bidrager '
         'praktisk',
         'Hands-on-rolle, hvor du både leder, koordinerer og selv bidrager '
         'praktisk, er præcis den måde, jeg har arbejdet på hele vejen: fra '
         'hænderne på anlægget som tekniker til ledelse med skruetrækkeren '
         'inden for rækkevidde. Bidrager selv hands-on, når det er nødvendigt, '
         'og det er det ofte.'),
                   ],
                   widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo — Ansøgning og CV — Operations Manager, '
                       'NordicCell')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_NordicCell_OperationsManager.docx')
    build(out)
    print(out)
