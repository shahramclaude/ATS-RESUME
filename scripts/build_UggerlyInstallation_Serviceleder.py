# -*- coding: utf-8 -*-
"""Serviceleder — Uggerly Installation A/S, Glostrup (dansk opslag -> dansk dokument).

4 sider i masterdesign: brev side 1, CV side 2-3, kravmatrix side 4.
Kontakt fra opslaget: konsulent hos Sensu A/S, Martin Tveit (+45 26 83 38 42)
-> hilsen "Kære Martin Tveit,". Ingen frist (behandles løbende).

STILVALG (style_guard godkendt, 3/3 skift mod #426 DFDS):
  register     = Håndværk og kundefokus (håndværk · kunder · effektivitet · kvalitet ·
                 løsninger)
  åbningsgreb  = BB (opkaldet klokken syv: serviceafdelingen begynder dagen ved
                 telefonen, og dér afgøres forskellen mellem travlhed og god service)
  struktur     = Kunder, montører, aftaler (kunderne · montørerne · aftalerne)

BRUGERENS KORREKTION + permanent regel: alt tekst humaniseret i brev OG CV.
Ingen em dash. Varieret rytme, sammentrækninger, konkret før generelt.
ALDRIG "el-installatør"/"elinstallatør" — kun "elautoriseret maskinmester (LV/MV/HV)".

ÆRLIG GRÆNSE (kanonisk): kandidaten er IKKE uddannet elektriker. JD'en selv åbner
alternativ rute (driftschef/FM/rådgivende) og siger "den brede erfaring som serviceleder
vejer tungest". Grænsen skrives ligeud i brev OG matrix. Kalkia/ABA/sikring/Business
Central = ærlige "kender ikke endnu"-noter.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Uggerly Installation · Serviceleder, Glostrup'
BANNER_RESUME = 'Serviceledelse · salg · kunder · el-teknisk ballast'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('26. november 2026')
    m.meta('Service · erhvervskunder · salg og kundekontakt')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Serviceleder, Glostrup', bold=True, color='1A1A1A')
    m.para('Kære Martin Tveit,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('En serviceafdeling begynder dagen ved telefonen. Når en kunde mangler varme '
       'klokken syv, er det ikke en mail der løser det, men en montør på vej og en '
       'leder der har styr på dagen. Den del af faget kan jeg lide: at få ting til at '
       'hænge sammen mens de sker, og at kunden mærker at nogen har taget fat. Jeg '
       'skriver til stillingen som serviceleder hos Uggerly Installation i Glostrup.')

    lp('Uggerly Installation A/S er en dansk virksomhed stiftet i 1993, der med udspring '
       'i el har udviklet sig til også at omfatte VVS og svagstrøm, og over 500 '
       'medarbejdere fordelt på seks afdelinger hører under brødrene Henrik og Jens '
       'Uggerly. De bærende værdier er effektivitet, kvalitet, godt håndværk og gode '
       'løsninger, og det er ord jeg genkender fra mit eget arbejde: en aftale er en '
       'aftale, og arbejdet skal holde første gang. At styrke serviceafdelingen i '
       'Glostrup og sikre fortsat vækst i serviceforretningen er en opgave jeg kan se '
       'mig selv i.')

    lp('Stillingen er nyoprettet i en afdeling i vækst, i en velkonsolideret virksomhed '
       'med et stærkt fagligt fællesskab, og de kalder det selv en rolle med '
       'selvstændigt ansvar hvor man skal sparke dørene ind indimellem. Det passer til '
       'måden jeg har arbejdet på siden 2003. Jeg har ledet mellem 8 og 15 montører og '
       'teknikere, og serviceledelsen på serviceprojekter har været mit daglige '
       'arbejde: sager til erhvervskunder i alle størrelser, fra mindre '
       'renoveringsopgaver til entrepriseservicesager på op til 1,5 mio. kr., egne '
       'kunder, kalkulation og prisafgivelse, igangsætning, bemanding og opfølgning på '
       'deadlines. Et team på tre serviceledere med en tilknyttet servicekoordinator og '
       'tæt samarbejde med entrepriseafdelingen under afdelingschefen for Service & '
       'Teknik er en ramme jeg kender godt fra både små og store organisationer.')

    lp('Den ene del af kravprofilen skal jeg være ærlig om: jeg er ikke uddannet '
       'elektriker. Min vej er den anden, I selv beskriver, nemlig driftschef- og '
       'serviceleder-erfaring kombineret med en el-faglig videreuddannelse. Jeg er '
       'elautoriseret maskinmester (LV/MV/HV) med elteknik på EQF6-niveau, og jeg har '
       'ledet elektrikere i over tyve år, så jeg taler deres fag sikkert, men '
       'svendebrevet har jeg ikke. Til gengæld lægger I vægt på at den brede erfaring '
       'som serviceleder vejer tungest, og den erfaring har jeg: opsøgende salg, '
       'kunderelationer, montører der skal ud ad døren til tiden og aftaler der skal '
       'lukkes.')

    lp('Kundefokus og en udadvendt, proaktiv tilgang er ikke en plakat hos mig, men '
       'noget kunderne og montørerne mærker i hverdagen. Det ligger i mig at jeg har '
       'pondus og kan skære igennem når det er nødvendigt, både over for kolleger og '
       'kunder, og som spillende træner står jeg tæt på opgaverne mens jeg uddelegere '
       'og prioritere opgaver uden at miste overblikket. At være serviceminded, '
       'pligtopfyldende og ansvarsbevidst er ikke svært når arbejdet betyder noget, og '
       'at gøre en reel forskel for både kunder, kolleger og virksomheden er målet der '
       'holder længere end en enkelt sag. Bosat i Måløv i kort køreafstand fra '
       'Glostrup, så kravet om daglig tilstedeværelse er helt fint. Kørekort B (manuelt '
       'gear), og tiltrædelsen kan aftales kort.')

    lp('I skriver at ansøgningerne behandles løbende, og det passer mig fint. '
       'Muligheden for faglig og personlig udvikling gennem efteruddannelse og en '
       'arbejdsplads med god atmosfære trækker også, ud over selve opgaven. En samtale '
       'hos Sensu eller hos Uggerly er jeg frisk på, og jeg svarer gerne på spørgsmål '
       'inden da.', after=44)

    m.para('Med venlig hilsen', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Serviceleder med el-teknisk ballast og 20+ års erfaring fra service, drift '
           'og projekter til erhvervskunder. Ledelse af 8-15 montører, opsøgende salg, '
           'kalkulation og egne aftaler, og en hverdag i kundens tempo siden 2003. '
           'Elautoriseret maskinmester (LV/MV/HV), vant til at stå for både folk, sager '
           'og regnskab.', after=32)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester (el-teknik og ventilation)',
         'Data Power Consultant ApS · København · 2024 – nu (fra nov. 2026 også ELOHVACs '
         'el-tekniske aktiviteter)',
         'AI-afdeling 4-10 personer · el-service og entreprise · 5 elektrikere + 3 lærlinge',
         [('Salg og opfølgning', 'Investeringstilbud med månedlig opfølgning, og '
           'serviceforretning med egne kunder og aftaler. Nye opgaver fulgt fra første '
           'kontakt til underskrevet aftale.'),
          ('Ledelse', 'Ansættelse, oplæring og mål for 4-10 personer og 5 elektrikere '
           'med 3 lærlinge. Faglig sparring i hverdagen og klare aftaler frem for lange '
           'møder.')]),
        ('Ejer / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 – nov. 2026 (virksomheden lukket)',
         'Erhvervskunder · el, ventilation og klima · entreprise · fuldt P&L · serviceaftaler',
         [('Serviceledelse og kunder', 'Serviceledelsen på sagerne fra opkald til '
           'aflevering: egne erhvervskunder, kalkulation og prisafgivelse, bemanding og '
           'opfølgning på deadlines. Serviceaftaler med mål på responstid og kvalitet, '
           'fornyet fordi kunderne fik det de blev lovet.'),
          ('Salg', 'Opsøgende salg til nye såvel som eksisterende kunder og pleje af '
           'kunderelationer i praksis. Nye servicekoncepter udviklet og solgt, og '
           'forretningen bygget op fra nul til faste aftaler.'),
          ('Mandskab', '5 elektrikere og 3 lærlinge med struktureret oplæring, '
           'vagtplaner og faglig sparring. Ensartet niveau sikret gennem standarder; '
           'nul kritiske afvigelser i serviceaftalerne.')]),
        ('Senior commissioningeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, DKK 2-10 mio. · 25 specialister · GMP/FDA/EMA',
         [('Projektstyring', '37 projekter styret på tid, økonomi og kvalitet med 25 '
           'specialister på tværs af engineering, indkøb og drift. Kalkulation af '
           'ændringer, månedsrapportering og nul kritiske fund ved aflevering. SAP ERP '
           'og PRINCE2 som struktur.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022 – nov. 2022',
         '11 samtidige ventilationsprojekter · 14 mand · underleverandører',
         [('Entreprise og kunder', '11 samtidige projekter for offentlige og private '
           'kunder. Tilbud og udbud, kalkulation, aftalegrundlag og underentreprenører '
           'fulgt til dørs, med 14 mand fordelt på sagerne.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · SCADA, PLC, HV-tavler · skiftehold',
         [('Driftschef-erfaringen', 'Drift og vedligehold døgnet rundt: pumper, '
           'behandlingsanlæg, HVAC, HV-tavler, SCADA og PLC. Fejlfinding på stedet, '
           '5S og Standard Work i værkstedet, og sikkerhedsrutiner med LOTO og APV på '
           'skiftehold.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('Grundlaget', 'Ledelse af 12 mekanikere og teknikere: vagtplan, materialer '
           'og mål. Fejlsøgning på industrielt udstyr, rodårsag og korrigerende '
           'handlinger.')]),
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
    m.bullet('Serviceledelse', 'Serviceprojekter og sager for erhvervskunder: '
             'igangsætning, bemanding, deadlines og opfølgning. 8-15 montører ledet '
             'siden 2003.', after=10)
    m.bullet('Salg og kunder', 'Opsøgende salg til nye og eksisterende kunder, pleje '
             'af kunderelationer og egne aftaler. Tilbud lukket fra første besøg til '
             'underskrevet aftale.', after=10)
    m.bullet('Kalkulation og økonomi', 'Kalkulation, prisafgivelse og tilbud beregnet '
             'på timer, materialer og dækningsbidrag. Fuldt budgetansvar som ejer '
             '(2023-2026).', after=10)
    m.bullet('El-teknik', 'Elautorisation LV/MV/HV som elautoriseret maskinmester '
             '(2023), elteknik på EQF6, og el, ventilation og klima i praksis.',
             after=10)
    m.bullet('Systemer', 'SAP ERP, Excel og Microsoft Office i daglig brug. Kalkia og '
             'Business Central er nye for mig, men nye systemer har aldrig taget lang '
             'tid.', after=10)

    m.section('DE FØRSTE 90 DAGE')
    m.para('Planen følger servicelederens tre sløjfer: kunderne, montørerne og '
           'aftalerne.', after=8)
    m.bullet('Dag 1-30 · Kunderne', 'Kunderne og de igangværende sager lært at kende: '
             'med på besøg, gennemgange med servicekoordinatoren og teamet på tre '
             'serviceledere. Mål: jeg kender kunderne og de løse ender, og de kender '
             'mig.', after=10)
    m.bullet('Dag 31-60 · Montørerne', 'Bemanding, igangsætning og opfølgning i '
             'praksis for de 8-15 montører, med deadlines der overholdes og en hverdag '
             'der glider. Mål: driften kører gennem mig uden at nogen jagter svar.',
             after=10)
    m.bullet('Dag 61-90 · Aftalerne', 'Opsøgende salg og proaktiv opfølgning på '
             'opgaver fra entrepriseafdelingen omsat til nye aftaler. Mål: de første '
             'nye serviceaftaler i hus, og en liste over kunder der burde have en.',
             after=10)

    m.section('SPROG, VÆRKTØJER OG PRAKTISK')
    m.para('Dansk (modersmål) · engelsk (professionelt) · persisk (modersmål). SAP ERP, '
           'Excel og Microsoft Office. PRINCE2. Kørekort kategori B (manuelt gear). Bor '
           'i Måløv, kort køreafstand fra Glostrup, og den daglige tilstedeværelse '
           'passer mig fint. Kan tiltræde med kort varsel.', after=32)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Serviceledelse i Glostrup · krav og dokumentation',
                   ('Krav i opslaget', 'Dokumenteret erfaring'),
                   [
        ('Uddannet elektriker',
         'Uddannet elektriker er jeg ikke, og det skriver jeg ligeud. Min el-faglige '
         'ballast er Dansk elautorisation LV/MV/HV som elautoriseret maskinmester '
         '(2023) og elteknik på EQF6-niveau (2000-2003), og jeg har ledet elektrikere '
         'siden 2003 (5 elektrikere og 3 lærlinge i ELOHVAC, 2023-2026).'),
        ('Erfaring som serviceleder fra el-branchen, eller driftschef, Facility '
         'Management eller rådgivende virksomhed',
         'Servicelederfaringen har jeg fra el-branchen i praksis: egen virksomhed med '
         'serviceaftaler og erhvervskunder (ELOHVAC 2023-2026) og driftschef-erfaring '
         'fra 24/7-drift (Biofos 2017-2022). Den rådgivende og tværfaglige side kender '
         'jeg fra Novo Nordisk (2022-2024).'),
        ('Serviceledelse på serviceprojekter til erhvervskunder, fra mindre '
         'renoveringsopgaver til entrepriseservicesager på op til 1,5 mio. kr.',
         'Serviceprojekter for erhvervskunder er dagligdagen: fra mindre '
         'renoveringsopgaver til entrepriseservicesager på op til 1,5 mio. kr. i '
         'størrelse (Ventek 2022, ELOHVAC 2023-2026). Egne sager styret fra opkald til '
         'aflevering, primært erhverv men også private.'),
        ('Ledelse af ca. 8-15 montører',
         'Mandskabsledelse i det leje: 5 elektrikere og 3 lærlinge i ELOHVAC (2023-'
         '2026), 14 mand hos Ventek (2022), 12 mekanikere og teknikere hos ARJ '
         '(2003-2010). Vagtplan, bemanding og opfølgning hører med.'),
        ('Opsøgende salg til nye såvel som eksisterende erhvervskunder',
         'Opsøgende salg i praksis: nye kunder vundet og eksisterende udvidet i '
         'ELOHVAC (2023-2026), tilbud og udbud hos Ventek (2022) og investeringstilbud '
         'med månedlig opfølgning hos Data Power (2024-2026).'),
        ('Pleje af kunderelationer og ansvar for egne kunder',
         'Egne kunder med løbende ansvar: serviceaftaler med mål på responstid og '
         'kvalitet, fornyet fordi kunderne fik det de blev lovet (ELOHVAC 2023-2026). '
         'Kunderelationer bygget over år, ikke enkeltsager.'),
        ('Proaktiv opfølgning på opgaver fra entrepriseafdelingen, så der kommer '
         'serviceaftale',
         'Proaktiv opfølgning er måden jeg har arbejdet på siden 2003: opgaver fulgt '
         'fra første kontakt til aftale, og samspillet mellem entreprise og service '
         'kender jeg fra Ventek (2022) og ELOHVAC (2023-2026), hvor næste opgave '
         'sjældent kom af sig selv.'),
        ('Kalkulation og prisafgivelse til kunden',
         'Kalkulation og prisafgivelse hver uge siden 2017: tilbud og beregning på '
         'timer og materialer (ELOHVAC 2023-2026, Ventek 2022), og budgetansvar for '
         'hele forretningen som ejer.'),
        ('Igangsætning af projekter, bemanding og opfølgning på deadlines',
         'Igangsætning og bemanding i 11 samtidige projekter (Ventek 2022) og i '
         'serviceforretningen (ELOHVAC 2023-2026), deadlines fulgt i 37 CAPEX-projekter '
         '(Novo 2022-2024) og i daglig drift.'),
        ('Mulighed for at blive lærlingeansvarlig',
         'Lærlingeansvar med i bagagen: 3 lærlinge oplæret i ELOHVAC (2023-2026) med '
         'struktureret forløb, og undervisning af unge elektrikere og teknikere siden '
         '2003. Opgaven tager jeg gerne.'),
        ('Fortrolig med Excel og Microsoft Office',
         'Excel og Microsoft Office er dagligdagsværktøjer for mig: kalkulationer, '
         'budgetter og rapportering siden 2003. Regneark og data brugt aktivt til at '
         'styre sager og økonomi.'),
        ('Fordel: Kalkia, ERP-systemer som Business Central, ABA, videoovervågning og '
         'sikring',
         'Kalkia og Business Central kender jeg ikke endnu, men SAP ERP har jeg brugt '
         'dagligt (Novo 2022-2024, ELOHVAC 2023-2026), og nye systemer lærer jeg hurtigt. ABA, '
         'videoovervågning og sikring har jeg ikke arbejdet med som fag; de tekniske '
         'principper ligger tæt på mit felt.'),
        ('Behersker dansk i skrift og tale, og engelsk er en fordel',
         'Mit daglige arbejdssprog er dansk, og engelsk bruger jeg professionelt '
         '(rapporter, møder, kunder). Persisk er mit andet modersmål. Formidling på '
         'dansk og engelsk har været en del af hverdagen siden 2003.'),
        ('Bosat højst en times kørsel fra Glostrup, krav om daglig tilstedeværelse',
         'Bor i Måløv, cirka 20 minutters kørsel fra Glostrup, og daglig '
         'tilstedeværelse på kontoret passer mig fint. Kørekort B (manuelt gear). Tiltrædelse kan ske med '
         'kort varsel.'),
        ('Videreuddannelse inden for el (fordel)',
         'El-faglig videreuddannelse dokumenteret: elteknik på EQF6-niveau (2000-2003), '
         'Dansk elautorisation LV/MV/HV (2023) og løbende efteruddannelse (AMU '
         'køleteknik 2021, PRINCE2, STCW 2021-2023).'),
        ('Kundefokus og din udadvendte, proaktive tilgang',
         'Kundefokus i praksis: serviceaftaler der blev fornyet (ELOHVAC 2023-2026), '
         'kunder der ringede direkte til mig, og en udadvendt tilgang der åbnede nye '
         'opgaver. Den opsøgende del var en del af ugen, ikke en kampagne.'),
        ('Pondus og kan skære igennem, sparke dørene ind',
         'Beslutninger truffet hurtigt når det gjaldt: havari- og akutte udkald '
         '(ELOHVAC 2023-2026), sikkerhedsstop på skiftehold (Biofos 2017-2022) og '
         'projektbeslutninger på millionbeløb (Novo 2022-2024). Direkte i tonen uden at '
         'brænde broer.'),
        ('Serviceminded, pligtopfyldende og ansvarsbevidst; et godt overblik og '
         'opfølgning på deadlines',
         'Serviceminded og ansvarsbevidst i arbejdet med egne kunder og aftaler '
         '(2023-2026), overblik over 11 samtidige projekter (Ventek 2022) og deadlines '
         'i 37 projekter (Novo 2022-2024).'),
        ('Spillende træner der uddelegere og prioriterer opgaver; teamplayer med gode '
         'kommunikationsevner',
         'Spillende træner i alle årene: med på gulvet og i fejlsøgningen samtidig med '
         'at opgaverne blev fordelt (ARJ 2003-2010, Biofos, ELOHVAC). Teamplayer med '
         'faglig sparring og klare aftaler frem for lange møder.'),
                   ], widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo — Serviceleder, Uggerly Installation')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_UggerlyInstallation_Serviceleder.docx')
    build(out)
    print(out)
