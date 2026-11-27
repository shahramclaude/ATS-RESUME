#!/usr/bin/env python3
"""Vedligeholdsmester, CTR I/S — ansøgning + CV + kravmatrix (dansk).

BRUGERSVAR 26.11 (bindende):
1. Lokation = commute_ok ("Frederiksberg" fra Måløv) -> konkret linje i brevet.
2. Ventiler/trykbærende udstyr/sikkerhedsudstyr = REEL erfaring -> selvsikkert.
3. Fjernvarmeinstallationer = INTERESSE (JD tillader "erfaring ELLER interesse")
   -> ærligt, ingen hedge-lyd, men ikke påstået erfaring.
4. Asset Management + vedligeholdelsesstrategi/-systemer = REEL -> selvsikkert.

STIL (3/3 mod #442 PKA): register "Uformel faglighed, fælles ansvar",
åbning BS (infrastrukturens skala), struktur "Overblik, strategi, forankring".
"elautoriseret maskinmester" — aldrig "autoriseret elinstallatør".
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_Gentofte_DriftslederEjendomme_2027.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'CTR I/S · Vedligeholdsmester, Frederiksberg'
BANNER_RESUME = 'VEDLIGEHOLD · VENTILER · LEVERANDØRSTYRING'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('27. november 2026')
    m.meta('CTR I/S · Stæhr Johansens Vej 38, 2000 Frederiksberg')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning om stillingen som vedligeholdsmester', bold=True,
           color='1A1A1A')
    m.para('Kære Daniel Casper Meilbøg,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('340.000 hjem i hovedstadsområdet varmes gennem ét transmissionssystem, '
       'og systemet kører døgnet rundt, året rundt, uden at nogen lægger mærke '
       'til det. CTR er Danmarks største transmissionsselskab for fjernvarme, '
       'og anlægget er kritisk infrastruktur: når noget skal skiftes eller '
       'justeres, sker det midt i driften, ikke ved siden af. Målet om '
       'fossilfri fjernvarme i 2030 bæres af investeringer og af den grønne '
       'omstilling, men også af noget så enkelt som et anlæg, der bliver holdt '
       'ved lige.')

    lp('Rollen som vedligeholdsmester appellerer til mig, præcis fordi rollen '
       'lader hænderne fri for skruetrækkeren, og fokus ligger på overblik, faglig indsigt '
       'og leverandørstyring. Jeg har arbejdet på den måde siden 2003, med '
       'vedligehold, koordinering og planlægning som omdrejningspunkt og '
       'leverandører og underentreprenører styret gennem aftaler og opfølgning. '
       'Ventiler, trykbærende udstyr og sikkerhedsudstyr har jeg arbejdet med i '
       'praksis i driften af tekniske anlæg, og reguleringsventiler, '
       'kontraventiler og sikkerhedsventiler er komponenter, jeg kender fra '
       'hverdagen. Vedligeholdelsessystemer har været arbejdsredskab i årevis.')

    lp('Det, der trækker mest ved CTR, er holdet. Syv personer i driften, der '
       'løfter opgaverne i fællesskab, og en uformel hverdag med plads til '
       'faglig sparring. I er glade for at dele deres viden og kan lide at '
       'idéudvikle og optimere vores arbejde, som der står i opslaget, og når '
       '96 % synes, at stedet er et rigtig godt sted at arbejde, er der ikke '
       'langt fra ord til praksis. Sætningen om, at man tager sammen ansvar for '
       'vores fælles opgave, at levere sikker og billig fjernvarme døgnet '
       'rundt, er præcis den ramme, jeg gerne vil arbejde i, med løbende '
       'vidensdeling på tværs og en tone, hvor det både kan være meningsfuldt '
       'og spændende at møde ind.')

    lp('De første 90 dage har tre navne. Første måned er overblikket: anlægget, '
       'teamet og de centrale samarbejdspartnere lært at kende, '
       'vedligeholdelsessystemet gennemgået og strategierne for området læst, '
       'før der ændres på noget. Forebyggende, afhjælpende og akut vedligehold '
       'har jeg planlagt og fulgt op på før, og samme disciplin lægger jeg i '
       'komponentområderne fra første uge.')

    lp('Næste fase er strategien. Ventilerne, sikkerhedsudstyret på stationerne, '
       'ventilationsanlæggene og fjederhængere er mit ansvarsområde, og her skal '
       'udvikling af vedligeholdelsesstrategi for egne områder ske i tæt samspil '
       'med teamet og de øvrige afdelinger. Asset Management-systemet, som blev '
       'implementeret og certificeret i 2025, er arbejdsredskabet, og jeg '
       'bidrager med praktisk erfaring fra vedligeholdelsesstyring i CMMS. '
       'Sekundære indsatsområder tager jeg gerne, for der, hvor vi sparrer med '
       'hinanden og dækker ind på tværs af teamet, bliver arbejdet bedre.')

    lp('Til sidst forankringen: leverandøraftalerne gennemgået, kontrakter og '
       'opfølgning sat i system, og den tekniske og økonomiske opfølgning på '
       'mindre anlægsprojekter, reinvesteringer og optimeringsarbejder ført med '
       'budget og resultater på samme bord. Målet efter tre måneder er klart '
       'ejerskab for ansvarsområderne, så strategien ikke bliver liggende i en '
       'mappe.')

    lp('Fjernvarmeinstallationer er ikke området, jeg har arbejdet mest med '
       'indtil nu, og det skriver jeg ligeud. Varme og teknisk drift har jeg fra '
       'el-, ventilations- og klimaanlæg, og interessen for fjernvarmen er reel: '
       'en sektor i bevægelse, hvor den tekniske og økonomiske vinkel kan følges '
       'på tæt hold. Nysgerrig og opsøger aktivt andres viden, erfaringer og '
       'perspektiver, når opgaven kalder på det, så nye fagområder bliver lært '
       'ordentligt og hurtigt. Proaktiv, ansvarlig og følger opgaver til dørs, '
       'fra det står på listen, til det er lukket.')

    lp('Arbejdsformen har altid været selvstændig, målrettet og med en '
       'struktureret arbejdsform, og jeg er pålidelig og mødestabil. '
       'Frederiksberg fungerer nemt fra Måløv, med metroen lige ved adressen, '
       'og tiltrædelse 1. februar 2027 eller hurtigst muligt passer.')

    lp('Vilkårene efter gældende overenskomst med KL passer, med flextid, '
       'hjemmearbejdsdage, pensionsordning, sundhedsforsikring og plads til '
       'faglig og personlig udvikling, herunder efteruddannelse og kurser. En '
       'sund balance mellem arbejdsliv og privatliv betyder noget for mig, og '
       'processen med to samtaler og et testforløb passer fint: den måde, I gør '
       'os umage med at finde det helt rette match, både fagligt og personligt, '
       'og kalder det en transparent og ordentlig proces, er til at forstå.', after=52)

    lp('Jeg håber at komme med på holdet og være med til at holde anlægget i '
       'drift mange år frem. Ballasten er gode analytiske og kommunikative evner i skrift og '
       'tale, god dømmekraft og evne til at træffe selvstændige beslutninger og '
       'erfaring i at skabe gode samarbejdsrelationer og netværk er den ballast, '
       'jeg tager med. Jeg ser frem til at høre fra dig.', after=44)

    m.para('Med venlig hilsen', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Maskinmester og elautoriseret (LV/MV/HV) med 20+ år i el, '
           'ventilation, varme og teknisk drift. Vedligehold, koordinering og '
           'leverandørstyring har været omdrejningspunktet siden 2003, fra '
           'hænderne på anlægget til strategi, aftaler og økonomi. Ventiler og '
           'trykbærende udstyr arbejdet med i praksis, vedligeholdelsessystemer '
           'og CMMS som daglig disciplin, og erfaring i at håndtere, prioritere '
           'og sikre overblik over mange samtidige opgaver.', after=32)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester (el-teknik og ventilation)',
         'Data Power Consultant ApS · København · 2024 – nu (fra nov. 2026 også ELOHVACs '
         'el-tekniske aktiviteter)',
         'AI-afdeling 4-10 personer · el-service og entreprise · 5 elektrikere + 3 lærlinge',
         [('El og koordinering', 'El-service og entreprise på bygninger, med '
           'fejlfinding, dokumentation og aflevering pr. sag. Teams på 4-10 '
           'specialister koordineret, og opgaver ført hele vejen, også når '
           'planen ændrede sig undervejs.')]),
        ('Ejer / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 – nov. 2026 (virksomheden lukket)',
         'Erhvervskunder · el, ventilation og klima · entreprise · fuldt P&L · serviceaftaler',
         [('Service og økonomi', 'Serviceaftaler på bygningers el-, '
           'ventilations- og klimaanlæg, med forebyggende vedligehold som '
           'omdrejningspunkt og energioptimering i de eksisterende anlæg. '
           'Driftsøkonomien fulgt måned for måned, og aftaler med kunder og '
           'leverandører holdt i orden.')]),
        ('Senior commissioningeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, DKK 2-10 mio. · 25 specialister · GMP/FDA/EMA',
         [('Projekter og kvalitet', '37 CAPEX-projekter på 2-10 mio. kr. med '
           '25 specialister, taget fra konstruktion over FAT/SAT og IQ/OQ/PQ '
           'til idriftsættelse. Dokumentation der holdt til revision, og '
           'kvalitetssikring af leverandører som en fast del af hverdagen.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022 – nov. 2022',
         '11 projekter · 14 mand · underleverandører · montage og aflevering',
         [('Ventilation og koordinering', 'Ventilationsanlæg i bygninger '
           'koordineret fra montage til aflevering: 11 projekter, 14 mand og '
           'underleverandører planlagt uge for uge. Fejlfinding på anlæg før '
           'aflevering, og opgaver fordelt med blik for kvalitet og tid.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · kritiske anlæg · 10 medarbejdere · skiftehold',
         [('Stabil drift døgnet rundt', 'Pumper, HVAC, procesrør, el, SCADA og '
           'PLC holdt kørende i døgndrift med 10 medarbejdere på skiftehold. '
           'Forebyggende vedligehold planlagt på fejldata, og reservedelsstyring '
           'så reparationer ikke ventede.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('Mennesker og fejlfinding', 'Vedligehold og reparation af maskiner '
           'og anlæg med 12 mekanikere og teknikere. Rodårsagsarbejde der '
           'ændrede måden fejl blev håndteret på, og opgaver fulgt til dørs '
           'hver gang.')]),
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
    m.bullet('Vedligehold og strategi', 'Forebyggende, afhjælpende og akut '
             'vedligehold planlagt og fulgt op, og udvikling af '
             'vedligeholdelsesstrategi med udgangspunkt i det, anlægget faktisk '
             'viser. MTBF/MTTR, reservedelsstyring og tilstande som '
             'beslutningsgrundlag.', after=10)
    m.bullet('Ventiler og anlæg', 'Ventiler, trykbærende udstyr og '
             'sikkerhedsudstyr fra driften af tekniske anlæg, med '
             'reguleringsventiler, kontraventiler og sikkerhedsventiler som '
             'velkendte komponenter. Ventilationsanlæg, el, varme og køl i '
             'drift og service.', after=10)
    m.bullet('Leverandører og økonomi', 'Indgåelse og styring af aftaler og '
             'kontrakter med eksterne leverandører samt opfølgning på '
             'udførelsen. Teknisk og økonomisk opfølgning på mindre '
             'anlægsprojekter, reinvesteringer og optimeringsarbejder, med SAP, '
             'Excel og CMMS som værktøjer.', after=10)
    m.bullet('Samarbejde og formidling', 'Koordinering på tværs siden 2003, og '
             'sekundære indsatsområder dækket med godt mod. Tolv år som '
             'underviser har givet skrift og tale i orden, og netværk bygges '
             'stadig: skabe gode samarbejdsrelationer og netværk er en løbende '
             'disciplin.', after=10)

    m.section('DE FØRSTE 90 DAGE')
    m.para('Planen følger opgaven: overblikket, strategien, forankringen.', after=8)
    m.bullet('Dag 1-30 · Overblikket', 'Anlægget, teamet og de centrale '
             'samarbejdspartnere lært at kende, og vedligeholdelsessystemet '
             'gennemgået. Mål: jeg kender områderne og hverdagen, før der '
             'ændres på noget.', after=10)
    m.bullet('Dag 31-60 · Strategien', 'Vedligeholdelsesstrategien for '
             'komponentområderne udviklet i samspil med teamet, og '
             'Asset Management-systemet taget i brug i praksis. Mål: en plan '
             'for områderne, ikke en ønskeseddel.', after=10)
    m.bullet('Dag 61-90 · Forankringen', 'Leverandøraftaler og opfølgning sat i '
             'system, og teknisk og økonomisk opfølgning på projekter og '
             'reinvesteringer i gang. Mål: klart ejerskab for ansvarsområderne, '
             'både fagligt og økonomisk.', after=10)

    m.section('SPROG, VÆRKTØJER OG PRAKTISK')
    m.para('Dansk (modersmål) · engelsk (professionelt) · persisk (modersmål). '
           'Værktøjskassen: SAP, Excel, CMMS, SCADA, PLC; PRINCE2. '
           'Kørekort kategori B (manuelt gear). Bosat i Måløv; Frederiksberg '
           'fungerer nemt, metroen lige ved adressen.', after=8)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Krav og dokumentation · Vedligeholdsmester, CTR I/S',
                   ('Krav i opslaget', 'Dokumentation'),
                   [
                       ('Maskinmester, ingeniør eller anden relevant teknisk baggrund',
                        'Maskinmester fra Copenhagen School of Marine Engineering & '
                        'Technology Management (2017-2022) suppleret med elautorisation '
                        'LV/MV/HV (2023). Derudover teknisk baggrund fra el- og '
                        'maskinteknik, AMU-kursus i køleteknik (2021) og tyve år med '
                        'teknik i hænderne.'),
                       ('Vedligehold, koordinering, planlægning og leverandørstyring',
                        'Kernen i arbejdet siden 2003: serviceaftaler og '
                        'underentreprenører styret og fulgt op (ELOHVAC 2023-2026), '
                        'vedligehold af kritiske anlæg døgnet rundt (Biofos 2017-2022) '
                        'og planlægning for hold på op til 14 mand (Ventek 2022).'),
                       ('Ventiler, trykbærende udstyr, sikkerhedsudstyr og vedligeholdelsessystemer',
                        'Ventiler, trykbærende udstyr og sikkerhedsudstyr har jeg '
                        'arbejdet med i praksis i driften af tekniske anlæg, herunder '
                        'køle- og HVAC-anlæg, hvor tryk og sikkerhedsfunktioner hører '
                        'hverdagen til. Vedligeholdelsessystemer og komponentkendskab '
                        'kommer fra drift, service og fejlfinding på el, varme og '
                        'ventilation.'),
                       ('Asset Management og struktureret styring af komponentområder',
                        'Asset Management som disciplin er velkendt: '
                        'vedligeholdelsessystemer, CMMS og struktureret styring af '
                        'komponentområder har jeg arbejdet med i praksis (Vestas '
                        '2024-2026: forebyggende og afhjælpende vedligehold, MTBF/MTTR, '
                        'reservedelsstyring og opfølgning på tilstande).'),
                       ('Fjernvarmeinstallationer',
                        'Fjernvarmeinstallationer er ikke mit hidtidige primærområde, '
                        'og det skriver jeg ligeud. Varmeinstallationer og teknisk '
                        'drift har jeg fra el-, ventilations- og klimaanlæg, og '
                        'interessen for fjernvarmen er reel: en sektor i bevægelse mod '
                        'fossilfri drift i 2030, hvor teknik og økonomi følges ad.'),
                       ('Teknisk og økonomisk opfølgning på mindre anlægsprojekter, reinvesteringer og optimeringsarbejder',
                        'Begge sider af bordet i hovedet: 37 CAPEX-projekter på 2-10 '
                        'mio. kr. (Novo Nordisk 2022-2024), fuldt P&L-ansvar '
                        '(ELOHVAC) og budgetstyring i driften. Den tekniske og '
                        'økonomiske vinkel af en sektors udvikling er et perspektiv, '
                        'jeg naturligt tager med.'),
                       ('Administrative økonomi- og IT-systemer som et naturligt arbejdsværktøj',
                        'SAP dagligt siden 2017, Excel til beregninger og opfølgning, '
                        'CMMS til vedligehold og reservedele, PRINCE2 til '
                        'projektarbejde og AI-værktøjer til analyse og dokumentation. '
                        'Systemerne er arbejdsredskaber, ikke forhindringer.'),
                       ('Planlægning, koordinering og opfølgning på forebyggende og afhjælpende vedligeholdelsesopgaver',
                        'Hverdag på skiftehold og i drift: pumper, HVAC og el på '
                        'kritiske anlæg (Biofos 2017-2022), serviceaftaler og akutte '
                        'udkald (ELOHVAC 2023-2026) og vedligeholdsplaner for egne '
                        'områder (Vestas 2024-2026).'),
                       ('Indgåelse og styring af aftaler og kontrakter med eksterne leverandører samt opfølgning',
                        'Kendt fra begge sider af bordet: serviceaftaler for '
                        'erhvervskunder, underentreprenører i entreprise og '
                        'kvalitetssikring af det arbejde, andre udfører. Kontrakter '
                        'følges til dørs, så aftalen ikke kun står på papiret.'),
                       ('Optimering og styring af vedligeholdelsesstrategier for egne områder',
                        'Optimering og styring af vedligeholdelsesstrategier for egne '
                        'områder er en disciplin, jeg kan lide: strategien skal følge '
                        'anlæggets virkelighed, og MTBF/MTTR og reservedelsdata viser, '
                        'hvor indsatsen skal flyttes hen.'),
                       ('Struktureret styring af komponentområder i samarbejde med teamet og øvrige afdelinger',
                        'Driftsorganisationer med mange grænseflader kender jeg: '
                        'Biofos vagtstruktur, Venteks montageforløb og ELOHVACs '
                        'kundeprojekter kræver samme koordinering på tværs, og '
                        'struktur i styringen er det, der holder sammen på det.'),
                       ('Deltagelse i sekundære indsatsområder',
                        'Sekundære indsatsområder dækker jeg gerne, og erfaringen med '
                        'det, hvor vi sparrer med hinanden og dækker ind på tværs af '
                        'teamet, har jeg fra vagtordninger, teknisk sparring og '
                        'tværgående opgaver, hvor ingen er færdige, før anlægget '
                        'kører.'),
                       ('Selvstændig, målrettet og med en struktureret arbejdsform; proaktiv, ansvarlig og følger opgaver til dørs',
                        'Stilen er selvstændig, målrettet og med en struktureret '
                        'arbejdsform, og jeg er proaktiv, ansvarlig og følger opgaver '
                        'til dørs: fra akut udkald til afleveret anlæg bliver tingene '
                        'lukket, også når planen ændrer sig undervejs.'),
                       ('Pålidelig og mødestabil og overholder aftaler, deadlines og forventninger',
                        'Pålidelig og mødestabil og tager ansvar for at overholde '
                        'aftaler, deadlines og forventninger. I vagtordninger med '
                        'ansvar for anlæg, der kører døgnet rundt, og aftaler med '
                        'kunder, der regner med, at vi møder op, har det været en '
                        'selvfølge.'),
                       ('Analytiske og kommunikative evner',
                        'Med tolv år som underviser, tilbudsskrivning og teknisk '
                        'dokumentation er de gode analytiske og kommunikative evner i '
                        'skrift og tale bygget op. Analyse af data og formulering af '
                        'konklusioner har fulgtes ad siden.'),
                       ('God dømmekraft og evne til at træffe selvstændige beslutninger',
                        'Udviklet på skiftehold, hvor en beslutning om et anlæg skal '
                        'tages nu og ikke i morgen, og i ledelsesarbejde, hvor '
                        'prioriteringer har konsekvenser for både økonomi og '
                        'sikkerhed. Dømmekraft trænes i situationer, ikke i teori.'),
                       ('Serviceminded, lydhør og skaber gode samarbejdsrelationer og netværk; kan lide at arbejde i team',
                        'Serviceminded og lydhør, med erfaring i at skabe gode '
                        'samarbejdsrelationer og netværk: kundedialog i ELOHVAC, '
                        'samarbejde med bygherrer og rådgivere i Ventek og Novo '
                        'Nordisk og kollegial sparring på tværs. Jeg kan lide at '
                        'arbejde i team, hvor viden deles.'),
                       ('Nysgerrig, opsøger andres viden og perspektiver og håndterer mange samtidige opgaver',
                        'Nysgerrig og opsøger aktivt andres viden, erfaringer og '
                        'perspektiver, når opgaven kalder på det. Samtidig kan jeg '
                        'håndtere, prioritere og sikre overblik over mange samtidige '
                        'opgaver, som 37 sideløbende projekter og vagtplanlagt drift '
                        'har trænet.'),
                   ],
                   widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo — Ansøgning og CV — Vedligeholdsmester, CTR I/S')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_CTR_Vedligeholdsmester.docx')
    build(out)
    print(out)
