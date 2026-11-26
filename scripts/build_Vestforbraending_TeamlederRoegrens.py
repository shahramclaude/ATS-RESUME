# -*- coding: utf-8 -*-
"""Teamleder for Team Røgrens — Vestforbrænding (dansk opslag -> dansk dokument).

4 sider i masterdesign: brev side 1, CV side 2-3, kravmatrix side 4.
Kontakt fra opslaget: Teknisk chef Torben Graae (togr@vestfor.dk, 21 33 20 75) ->
hilsen "Kære Torben Graae,". Frist 7. januar 2027.

STILVALG (style_guard godkendt, 3/3 skift mod #424 Sweco):
  register     = Forsyning og driftsansvar (forsyning · driftsstabilitet · sikkerhed ·
                 teknisk kvalitet · teamudvikling)
  åbningsgreb  = AZ (løftet til byen: rørensen som det løfte, anlægget giver byen om
                 varme og ren røggas)
  struktur     = Team, anlæg, udvikling (teamet · anlægget · udviklingen)

BRUGERENS KORREKTION + permanent regel: alt tekst humaniseret i brev OG CV.
Ingen em dash. Varieret rytme, sammentrækninger, konkret før generelt.

BRUGERBEKRÆFTET 26.11.2026:
  - DCS: direkte erfaring fra procesanlæg (brugerbekræftet) — intet systemnavn, ingen
    arbejdsgiver tilskrevet; skriv generelt.
  - PET-sikkerhedsgodkendelse (Fortrolig): gælder Saildrone-svaret — ingen tidligere
    godkendelse, ingen forventede problemer (ærligt).
  - Termisk produktion: direkte erfaring med kedler, damp og fjernvarme fra tidligere
    arbejde (brugerbekræftet) — generel beskrivelse, ingen arbejdsgiver tilskrevet.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Vestforbrænding · Teamleder for Team Røgrens'
BANNER_RESUME = 'Teamledelse, drift og vedligehold · røgrens og behandlingsanlæg'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('26. november 2026')
    m.meta('Forsyning og fjernvarme · teamleder for Team Røgrens')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Teamleder for Team Røgrens', bold=True, color='1A1A1A')
    m.para('Kære Torben Graae,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('Rørensen på et affaldsenergianlæg er det løfte, anlægget giver byen: at varmen '
       'bliver leveret, og at røggassen er ren, før den forlader skorstenen. Når det '
       'kører, mærker ingen i hovedstadsområdet andet end varmen i radiatoren, og sådan '
       'skal det være. Løftet holdes ikke af udstyret alene. Det holdes af folk der '
       'kender anlægget, og af en teamleder der skaffer dem rammerne, også på en torsdag '
       'morgen hvor noget driller. Stillingen som teamleder for Team Røgrens er den rolle, '
       'jeg skriver om.')

    lp('Vestforbrænding giver god energi videre, og forsyningsopgaven er konkret: et af '
       'Danmarks største affaldsselskaber, hvor opgaven er at indsamle, genanvende og '
       'behandle affald miljømæssigt og økonomisk forsvarligt, og hvor en del af det '
       'bliver til produktion af fjernvarme til hovedstadsområdet. Affaldsenergianlægget '
       'er blandt Danmarks største og en vigtig del af varmeforsyningen i '
       'hovedstadsområdet, og her spiller røgrens og behandlingsanlæg en central rolle. '
       'Målet er høj driftsstabilitet, sikkerhed og teknisk kvalitet, og stabil og sikker '
       'drift af det område er praktisk arbejde hver eneste dag, '
       'og en stabil og effektiv drift kommer ikke af sig selv. Den form for ansvar '
       'kender jeg fra Lynetten, hvor anlægget kørte døgnet rundt, og hvor aftalen med '
       'byen i bund og grund var, at der ikke skulle ske noget.')

    lp('Det, der trækker mest ved stillingen, er kombinationen af folk og anlæg. Jeg har '
       'ledet teams på otte til femogtyve mennesker: tolv mekanikere og teknikere i et '
       'maskinværksted, fem elektrikere og tre lærlinge i min egen virksomhed og '
       'femogtyve specialister på tværs af engineering, indkøb og drift hos Novo '
       'Nordisk. Opgaven med at lede og udvikle folkene i teamet har jeg taget mest '
       'alvorligt alle tre steder, og jeg gør det i praksis: med på gulvet, med i '
       'fejlsøgningen og med til den svære samtale, når den er nødvendig. '
       'At have fokus på arbejdsmiljø og sikkerhed og omsætte det til praksis i både mit '
       'eget og andres arbejde er en selvfølge for mig. LOTO, '
       'APV og nærved-hændelser var faste rutiner på skiftehold hos Biofos, og de '
       'vaner tager jeg med.')

    lp('Opgaverne kender jeg fra driftens side. Koordinering af større anlægsarbejder og '
       'havari- og serviceudkald, sagsbehandling af tekniske afvigelser hvor årsagen '
       'skal frem, ikke kun symptomet, og rollen som bindeled mellem et projekt og en '
       'drift der skal køre videre bagefter. DCS-systemer har jeg arbejdet med i '
       'procesanlæg, og vedligeholdelsesstyring har jeg brugt i SAP siden tiden hos Novo. '
       'Kedler, damp og fjernvarme har jeg erfaring med fra tidligere stillinger, '
       'suppleret med køleteknik og procesudstyr. RCM som navn er nyt for mig, men '
       'indholdet er velkendt: rodårsager, korrigerende handlinger og planlagt '
       'vedligehold har været måden at arbejde på siden 2003. Formidling på dansk og '
       'engelsk til både kolleger, kunder og ledelse hører med, og '
       'databehandling, dokumentations- og rapporteringssystemer bruger jeg hver dag. '
       'Kravet om, at jeg kan sikkerhedsgodkendes til Fortrolig, har jeg ingen '
       'forventede problemer med: jeg '
       'har ikke været sikkerhedsgodkendt før, men der er intet i min baggrund, jeg '
       'forventer bremser det.')

    lp('Planen for de første 90 dage står side 3 i CV\'et, og den begynder med teamet, '
       'ikke med anlægget: seks medarbejdere skal kunne mærke, at deres leder kender '
       'deres hverdag. Rammen tiltaler mig også: Drift & Produktion med cirka 100 '
       'medarbejdere, der arbejder tæt sammen om driften. At være medarbejder hos jer er '
       'samtidig at gøre en forskel for miljø, borgere og virksomheder, og det er en af '
       'grundene til, jeg søger. Jeg bor i Måløv, har kørekort B, og tiltrædelsen kan '
       'aftales '
       'kort.', after=52)

    lp('Et alsidigt og inkluderende miljø er vigtigt for at skabe en inspirerende og '
       'effektiv arbejdsplads, og den slags bidrager jeg gerne til. Samtalen håber jeg '
       'bliver næste skridt. Der er sikkert spørgsmål til både '
       'drift og ledelse, som jeg hellere svarer på i rummet end på skrift.', after=44)

    m.para('Med venlig hilsen', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Teamleder og driftstekniker med mere end 20 års erfaring fra drift, '
           'vedligehold og projekter på forsyningskritiske anlæg. Ledelse af teams på '
           '8-25 personer, 24/7-drift på behandlingsanlæg og commissioning på '
           'procesanlæg, og styringssystemer fra DCS til SCADA, PLC og SRO. Vant til at '
           'stå med både medarbejdere, økonomi og teknik på samme tid.', after=32)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester (el-teknik og ventilation)',
         'Data Power Consultant ApS · København · 2024 – nu (fra nov. 2026 også ELOHVACs '
         'el-tekniske aktiviteter)',
         'AI-afdeling 4-10 personer · el-service og entreprise · 5 elektrikere + 3 lærlinge',
         [('Ledelse og udvikling', 'Ansættelse, oplæring og mål for afdelingens 4-10 '
           'personer, og 5 elektrikere med 3 lærlinge i serviceforretningen. Faglig '
           'sparring i hverdagen og investeringstilbud med månedlig opfølgning.'),
          ('Værktøjer og rapportering', 'Arbejdsgange og rapportflow udviklet i Python '
           'med AI-understøttelse, så dokumentation og opfølgning tog kortere tid. '
           'Systemer og data brugt aktivt til at styre forretningen.')]),
        ('Ejer / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 – nov. 2026 (virksomheden lukket)',
         'Erhvervskunder · el, ventilation og klima · entreprise · fuldt P&L · serviceaftaler',
         [('Drift og kunder', 'El-service og fejlfinding hos erhvervskunder: tavler, '
           'styring og forebyggende vedligehold på el, ventilation og klima i bygninger '
           'i brug, og akutte udkald når noget stoppede.'),
          ('Økonomi og aftaler', 'Fuldt budget- og driftsansvar for forretningen. '
           'Tilbud, prisfastsættelse og indkøb, og serviceaftaler med mål på '
           'responstid, kvalitet og leveringsevne; aftalerne blev fornyet, fordi '
           'kunderne fik det, de blev lovet.'),
          ('Personale', '5 elektrikere og 3 lærlinge med struktureret oplæring og faglig '
           'sparring. Ensartet niveau sikret gennem standarder; nul kritiske afvigelser '
           'i serviceaftalerne.')]),
        ('Senior commissioningeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, DKK 2-10 mio. · 25 specialister · GMP/FDA/EMA',
         [('Projekter og koordinering', '37 projekter styret på tid, økonomi og kvalitet, '
           'med 25 specialister på tværs af engineering, indkøb og drift, og nul '
           'kritiske fund ved aflevering. SAP ERP og PRINCE2 som struktur, og '
           'månedsrapportering til ledelse og bygherre.'),
          ('Kvalitet og dokumentation', 'FAT/SAT og kvalificeringsprotokoller (IQ/OQ/PQ) '
           'i GMP-miljø, hvor dokumentationen skal holde til revision. PDCA-forløb med '
           '40% lavere energiomkostninger som målbart resultat.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022 – nov. 2022',
         '11 samtidige ventilationsprojekter · 14 mand · underleverandører',
         [('Koordinering', '11 samtidige projekter med ventilation i bygninger for '
           'offentlige og private bygherrer. Tilbud og udbud, aftalegrundlag, '
           'underentreprenører og sikkerhedsdokumentation fulgt til dørs.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · SCADA, PLC, HV-tavler · skiftehold',
         [('Drift af behandlingsanlæg', 'Drift, overvågning og vedligehold af pumper, '
           'behandlingsanlæg, HVAC, HV-tavler, SCADA og PLC døgnet rundt på '
           'spildevandsbehandlingsanlægget. Fejlfinding på stedet, 5S og Standard Work '
           'i værkstedet.'),
          ('Sikkerhed og standarder', 'Skiftehold og vagt med LOTO, APV og '
           'nærved-hændelser som faste rutiner. Fagligt niveau holdt ved lige gennem '
           'oplæring og fælles procedurer.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('Grundlaget', 'Ledelse af 12 mekanikere og teknikere: vagtplan, materialer og '
           'mål. Fejlsøgning på industrielt udstyr, rodårsag og korrigerende '
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
    m.bullet('Ledelse', 'Teams på 8-25 personer siden 2003: ansættelse, oplæring, mål, '
             'daglig sparring og de svære samtaler. Erfaring fra værksted, entreprise og '
             'funktion med mange fagligheder.', after=10)
    m.bullet('Drift og vedligehold', '24/7-drift, planlagt og forebyggende vedligehold, '
             'tilstandsbaseret tankegang, rodårsag og korrigerende handlinger. CMMS og '
             'SAP som styring.', after=10)
    m.bullet('Styring og systemer', 'DCS-systemer i procesanlæg, SCADA, PLC og SRO fra '
             'drift og commissioning. El, HVAC, pumper og procesudstyr på tværs.', after=10)
    m.bullet('Termisk produktion', 'Kedler, damp og fjernvarme fra tidligere stillinger, '
             'køleteknik og klimaanlæg (AMU 2021) og procesudstyr hos Novo Nordisk.',
             after=10)
    m.bullet('Dokumentation og økonomi', 'GMP-dokumentation og protokoller, procedurer '
             'og arbejdsinstrukser, budget og P&L, SAP ERP, Power BI, Python og '
             'AI-værktøjer.', after=10)

    m.section('DE FØRSTE 90 DAGE')
    m.para('Planen følger opgaverne i stillingen: teamet først, så anlægget, så '
           'udviklingen.', after=8)
    m.bullet('Dag 1-30 · Teamet', 'De seks medarbejdere og deres hverdag lært at kende '
             'indefra: med på skiftene, med i gennemgangen af anlæg og procedurer. '
             'Mål: teamet og jeg kender hinandens styrker, og sikkerhed og arbejdsmiljø '
             'er omsat til praksis i stedet for på papiret.', after=10)
    m.bullet('Dag 31-60 · Anlægget', 'Den daglige koordinering, sagsbehandlingen af '
             'tekniske afvigelser og de større anlægs- og havariarbejder kørt i et '
             'flow, hvor projektafdelingen og drift har samme billede. Mål: koordineringen '
             'er min, og de større arbejder er planlagt uden overraskelser.', after=10)
    m.bullet('Dag 61-90 · Udviklingen', 'RCM og asset management for de vitale komponenter '
             'grebet konkret an: hvilke komponenter, hvilke data, hvilke beslutninger. '
             'Mål: første forslag til optimering og struktureret vedligehold præsenteret, '
             'og budget- og dokumentationsarbejdet sat i gang.', after=10)

    m.section('SPROG, VÆRKTØJER OG PRAKTISK')
    m.para('Dansk (modersmål) · engelsk (professionelt, skrift og tale) · persisk '
           '(modersmål). DCS, SCADA, PLC, SRO, SAP ERP, CMMS, Power BI, Python og '
           'AI-værktøjer. PRINCE2. Kørekort kategori B (manuelt gear). Bor i Måløv. '
           'Kan tiltræde med kort varsel.', after=32)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Teamledelse og drift · krav og dokumentation',
                   ('Krav i opslaget', 'Dokumenteret erfaring'),
                   [
        ('Maskinmester, ingeniør eller tilsvarende',
         'B.Tech (EQF6) i teknologiledelse og maskinteknik (2017-2022) og Dansk '
         'elautorisation LV/MV/HV som elautoriseret maskinmester (2023). Elteknik på '
         'EQF6-niveau fra 2000-2003 og mere end 20 års praksis fra drift og projekter.'),
        ('Erfaring med DCS-systemer',
         'DCS-systemer har jeg arbejdet med i procesanlæg, og klassen kender jeg fra '
         'SCADA-, PLC- og SRO-anlæg i døgndrift på Lynetten (2017-2022) og fra '
         'commissioning hos Novo Nordisk (2022-2024): overvågning, fejlfinding og '
         'dialog med systemejere.'),
        ('Erfaring med vedligeholdelsesstyring',
         'Vedligeholdelsesstyring brugt dagligt siden 2003: planlagt og forebyggende '
         'vedligehold, arbejdsordrer og reservedelsstyring i SAP og CMMS hos Novo '
         'Nordisk og i egne virksomheder, med mål på oppetid, responstid og kvalitet.'),
        ('Gerne erfaring inden for termisk produktion',
         'Kedler, damp og fjernvarme har jeg erfaring med fra tidligere stillinger, suppleret '
         'med køleteknik og klimaanlæg (AMU 2021) og procesudstyr, tanke og rør hos '
         'Novo Nordisk. Termisk produktion kombineret med proces og el er præcis den '
         'blanding, jeg kender.'),
        ('Fagligt og personalemæssigt ansvar for et team',
         'Personaleansvar siden 2003: 12 mekanikere og teknikere hos ARJ Engineering, '
         '5 elektrikere og 3 lærlinge i ELOHVAC, 25 specialister på tværs af funktioner '
         'hos Novo Nordisk og 4-10 medarbejdere i AI-afdelingen hos Data Power.'),
        ('Lede og udvikle medarbejdere i teamet',
         'Medarbejderudvikling i praksis: struktureret oplæring af 5 elektrikere og 3 '
         'lærlinge (ELOHVAC 2023-2026), undervisning og faglig sparring blandt 12 '
         'mekanikere (ARJ 2003-2010) og mål med opfølgning for 4-10 personer (Data '
         'Power 2024-2026). Ensartet niveau sikret gennem standarder og daglig sparring.'),
        ('Koordinere større anlægs- revisions- og havariarbejder',
         'Koordineringen af anlægsarbejder og akutte udkald kender jeg fra 11 samtidige '
         'projekter med underentreprenører (Ventek 2022), 37 CAPEX-projekter på et '
         'driftende procesanlæg (Novo 2022-2024) og havari- og serviceudkald med '
         'responstmål (ELOHVAC 2023-2026).'),
        ('Sagsbehandle tekniske afvigelser, som hastighed- og rådighedstab',
         'Tekniske afvigelser sagsbehandlet i praksis: fejlfinding og rodårsag på '
         'industrielt udstyr (ARJ), driftsfejl under 24/7-drift (Biofos), garanti- og '
         'servicesager med mål på responstid og oppetid (ELOHVAC) og afvigelser i '
         'commissioning (Novo). Årsagen skal frem, ikke kun symptomet.'),
        ('Deltage i arbejdet med RCM og en struktureret asset management-tilgang til '
         'vores vitale komponenter',
         'Struktureret vedligehold og asset-tankegang har været måden at arbejde på '
         'siden 2003: vitale komponenter, planlagt vedligehold, rodårsag og korrigerende '
         'handlinger fra maskinværksted til procesanlæg. RCM som formelt forløb er jeg '
         'ny i, men metoden bag er velkendt, og jeg bidrager gerne fra første møde.'),
        ('Deltage i projekter og fungere som bindeled mellem projektafdelingen og drift- '
         'og produktionsafdelingen',
         'Bindeled mellem projekt og drift: commissioning af el-systemer på et driftende '
         'anlæg hos Novo Nordisk (37 projekter, 2022-2024), hvor drift og engineering '
         'skulle mødes om løsningerne, og fast koordinering mellem værksted, kunder og '
         'underentreprenører hos Ventek og ELOHVAC.'),
        ('Indkøbsspecifikationer, budgetter, dokumentation, procedurebeskrivelser',
         'Indkøbsspecifikationer og kontrakter skrevet og forhandlet i ELOHVAC og '
         'Ventek; budget og økonomi med direkte ansvar som ejer (fuldt P&L, 2023-2026) '
         'og som projektleder (CAPEX 2-10 mio., Novo). Procedurer og arbejdsinstrukser '
         'sat i system hos Biofos og ELOHVAC.'),
        ('Implementering af nye tekniske løsninger',
         'Nye tekniske løsninger implementeret i drift: energiforbrug sænket 40% i et '
         'PDCA-forløb hos Novo Nordisk, digitale værktøjer og AI-assisterede '
         'arbejdsgange indført i egen afdeling (2024-2026) og nye servicekoncepter '
         'udviklet i ELOHVAC.'),
        ('Fokus på arbejdsmiljø og sikkerhed og omslætte det til praksis i både dit eget '
         'og andres arbejde',
         'Sikkerhed omsat til praksis på skiftehold og i entreprise: LOTO, APV og '
         'nærved-hændelser som faste rutiner hos Biofos (2017-2022), '
         'sikkerhedsdokumentation for underentreprenører hos Ventek og dagligt '
         'sikkerhedsarbejde i egen virksomhed siden 2023.'),
        ('Koordinere opgaver og samarbejde på tværs af organisationen',
         'Samarbejdet på tværs har været en del af alle rollerne: 25 specialister på '
         'tværs af engineering, indkøb og drift hos Novo, leverandører og kunder i '
         'ELOHVAC og tværfaglige skiftehold i Biofos. Dialogen tages tidligt og '
         'direkte.'),
        ('Formidle komplekse tekniske problemstillinger på dansk og engelsk til '
         'forskellige målgrupper, både internt og eksternt',
         'Teknisk formidling på dansk og engelsk til forskellige målgrupper: rapporter '
         'og månedlig ledelsesrapportering for ledelse og bygherre (Novo, 25 specialister), '
         'kundedialog, undervisning af 8 elektrikere og lærlinge (ELOHVAC) og oplæg på '
         'begge sprog. Dansk og engelsk bruges dagligt.'),
        ('Vurdere alternative løsninger og se sammenhænge på tværs af anlæg og systemer',
         'Tværfagligt overblik fra el, ventilation, klima og proces: løsninger vurderet '
         'på tværs af anlæg i ELOHVAC og Ventek (11 samtidige projekter, 2022), og '
         'commissioning hvor el, maskin og proces skulle hænge sammen (Novo, 37 '
         'projekter, 2022-2024). Løsningen skal holde i drift, ikke kun '
         'på tegningen.'),
        ('Erfaring med databehandling, dokumentations- og rapporteringssystemer',
         'Databehandling og rapportering i daglig drift: SAP ERP og CMMS som '
         'styringssystemer, Power BI og månedsrapportering, GMP-dokumentation hos Novo '
         'og egne rapportflows udviklet i Python med AI-understøttelse (2024-2026).'),
        ('Drift, vedligehold, optimering og udvikling af røgrensningsanlæg, '
         'spildevandsbehandlingsanlæg og behandlingsanlæg til produktion af procesvand med '
         'tilhørende kemikaliedoseringsanlæg',
         'Drift og vedligehold af behandlingsanlæg i samme skala: pumper, HVAC, '
         'HV-tavler, SCADA og PLC på spildevandsbehandlingsanlægget Lynetten døgnet '
         'rundt (2017-2022) og procesudstyr, tanke og rør hos Novo Nordisk (2022-2024). '
         'Røgrens som specifikt anlæg vil være nyt for mig.'),
        ('Vandbalancen over anlægget med tilhørende buffer- og opsamlingstanke',
         'Vand- og proceshåndtering fra behandlingsanlæg og procesanlæg: '
         'pumpestationer, tanke og bufferkapacitet på Lynetten (2017-2022) og procesvand, '
         'tanke og rør hos Novo Nordisk (2022-2024). Vandbalance og tankstyring som '
         'værktøj læres konkret på jeres anlæg.'),
        ('Forudsætning: sikkerhedsgodkendelse til Fortrolig',
         'Sikkerhedsgodkendelse til Fortrolig har jeg ingen forventede problemer med: '
         'ingen tidligere godkendelse, men heller intet i min baggrund siden 2003, jeg '
         'forventer bremser processen. Min historik er dokumenteret og gennemsigtig.'),
                   ], widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo — Teamleder for Team Røgrens, Vestforbrænding')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Vestforbraending_TeamlederRoegrens.docx')
    build(out)
    print(out)
