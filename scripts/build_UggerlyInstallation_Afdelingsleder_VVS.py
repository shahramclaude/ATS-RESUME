# -*- coding: utf-8 -*-
"""Afdelingsleder VVS — Uggerly Installation A/S, Ringsted (dansk opslag -> dansk dokument).

4 sider i masterdesign: brev side 1, CV side 2-3, kravmatrix side 4.
Kontakt fra opslaget: Martin Tveit, Sensu A/S, tlf. 26 83 38 42
-> hilsen "Kære Martin Tveit,". Ingen frist (behandles løbende).

STILVALG (style_guard godkendt, 3/3 skift mod #427 Uggerly Serviceleder — SAMME FIRMA,
intet genbruges fra Glostrup-ansøgningen):
  register     = Ledelse, drift og udvikling (retning · struktur · helhed · resultater)
  åbningsgreb  = BD (byggepladsen mandag morgen: en beslutning om bemanding er først god
                 når den holder ude hos montørerne)
  struktur     = Retning, struktur, udvikling (retningen · strukturen · udviklingen)

BRUGERENS KORREKTION + permanent regel: alt tekst humaniseret i brev OG CV.
Ingen em dash. "dynamisk" citeres aldrig (JD'ens boilerplate).

BRUGERSVAR 26.11: (1) Ringsted: kandidaten er indstillet på at flytte tættere på Ringsted
ved ansættelse (stillingsspecifik bekræftelse). (2) Serviceleder-ansøgningen i Glostrup
nævnes IKKE — de to ansøgninger holdes adskilt.

ÆRLIG GRÆNSE: VVS-installatøruddannelsen har kandidaten IKKE (JD'en kalder den "relevant",
ikke et hårdt krav). Erstatning: tyve års VVS-nær erfaring (varme, ventilation, køl,
procesrør, bioanlæg) + elautoriseret maskinmester (LV/MV/HV). Formen "el-installatør"/
"elinstallatør" bruges ALDRIG.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Uggerly Installation · Afdelingsleder VVS, Ringsted'
BANNER_RESUME = 'Afdelingsledelse · drift · udvikling · VVS-nære anlæg'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('26. november 2026')
    m.meta('Ledelse · drift · udvikling · Ringsted')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Afdelingsleder VVS, Ringsted', bold=True, color='1A1A1A')
    m.para('Kære Martin Tveit,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('En beslutning om bemanding er først god, når den holder på byggepladsen mandag '
       'morgen. Det er der ledelsen kan ses: om montørerne ved hvad de skal, om kunden '
       'har fået det aftalte, og om dagen hænger sammen. Jeg skriver til stillingen som '
       'afdelingsleder for VVS-afdelingen i Ringsted.')

    lp('Uggerly Installation A/S er en dansk virksomhed stiftet i 1993, der med udspring '
       'i el har udviklet sig til også at omfatte VVS og svagstrøm. Virksomheden ledes af '
       'brødrene Henrik og Jens Uggerly, som også er ejere af virksomheden, og der er '
       'over 475 medarbejdere fordelt på seks afdelinger med tre i Jylland, en på Fyn og '
       'to på Sjælland. De bærende værdier er effektivitet, kvalitet, godt håndværk og '
       'gode løsninger, og de ord kan jeg genkende fra mine egne år i branchen: det '
       'udførte arbejde er det eneste argument der holder i længden.')

    lp('At styrke VVS-afdelingen i Ringsted med en erfaren og struktureret leder er en '
       'opgave med tyngde, og stillingen rummer det overordnede ansvar for den daglige '
       'ledelse og drift af hele VVS-afdelingen, funktionærer såvel som montører. Jeg har '
       'haft den slags ansvar før, nemlig den daglige drift af en afdeling, et '
       'forretningsområde eller en tilsvarende enhed, med effektiv drift, høj faglig '
       'kvalitet, tilfredse kunder og gode resultater som mål. Det er ikke nye ord for '
       'mig at skabe struktur, prioritere ressourcer og sikre et godt samarbejde på tværs '
       'af afdelingens funktioner; kravene har jeg arbejdet under siden 2003, i Biofos\u2019 '
       'døgndrift, i Venteks entrepriser og i min egen virksomhed.')

    lp('På ét punkt skal jeg være ligefrem: VVS-installatøruddannelsen har jeg ikke. Min '
       'baggrund er el-teknisk som elautoriseret maskinmester (LV/MV/HV) og elteknik på '
       'EQF6-niveau, og solid ledelseserfaring har jeg samlet op siden 2003 sammen med '
       'solidt kendskab til branchen og til en installationsvirksomhed indefra: varme og '
       'ventilation hos Ventek, bioanlæg, procesrør og HVAC i Biofos\u2019 døgndrift og el, '
       'ventilation og klima i egen virksomhed. Jeg har ledet håndværkere og funktionærer '
       'side om side, og jeg har fulgt montørerne på byggepladserne tæt nok til at vide '
       'hvad der skal til.')

    lp('At skabe retning og sikre, at medarbejdere og drift fungerer som en samlet '
       'helhed, er kernen i det her job. Naturlig autoritet og gennemslagskraft får man '
       'tildelt af folkene omkring en, ikke af titlen, og at sætte retning for og følge '
       'op på montørerne på byggepladserne har været en del af mit arbejde siden 2003. '
       'Det går hånd i hånd med at stille krav og skabe gode relationer; kommunikationen '
       'er ligefrem og åben, og jeg lytter før jeg beslutter. Struktureret, vedholdende, '
       'udadvendt og kunde-minded er ord jeg gerne står på mål for. På afstandsspørgsmålet: '
       'jeg bor i Måløv i dag, men er indstillet på at flytte tættere på Ringsted hvis '
       'jobbet er det rigtige.')

    lp('Dansk i skrift og tale er mit daglige arbejdssprog, og engelsk bruger jeg '
       'professionelt. At I behandler ansøgningerne løbende passer mig fint, og jeg '
       'svarer gerne på spørgsmål fra Martin Tveit hos Sensu inden da. En samtale hvor I '
       'mærker om kemien er der, er jeg frisk på.', after=44)

    m.para('Med venlig hilsen', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Afdelingsleder med drifts- og udviklingsansvar fra installationer og forsyning '
           'siden 2003. Funktionærer og faglærte ledet i skiftehold, entrepriser og egen '
           'virksomhed, med økonomiopfølgning, bemanding og resultater i fokus. '
           'Elautoriseret maskinmester (LV/MV/HV), vant til at stå for både mennesker, '
           'drift og tal.', after=32)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester (el-teknik og ventilation)',
         'Data Power Consultant ApS · København · 2024 – nu (fra nov. 2026 også ELOHVACs '
         'el-tekniske aktiviteter)',
         'AI-afdeling 4-10 personer · el-service og entreprise · 5 elektrikere + 3 lærlinge',
         [('Ledelse og opfølgning', 'Ansættelse, oplæring og mål for 4-10 personer, og '
           'den tekniske ledelse af 5 elektrikere med 3 lærlinge. Investeringstilbud med '
           'månedlig opfølgning og serviceforretning med egne kunder og aftaler.')]),
        ('Ejer / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 – nov. 2026 (virksomheden lukket)',
         'Erhvervskunder · el, ventilation og klima · entreprise · fuldt P&L · serviceaftaler',
         [('Afdelingen', 'Forretningen drevet som en afdeling med fuldt ansvar: '
           'økonomiopfølgning, bemanding af 5 elektrikere og 3 lærlinge, kalkulation og '
           'aftaler. Serviceaftaler med mål på responstid og kvalitet, fornyet fordi '
           'kunderne fik det aftalte.'),
          ('Anlæg', 'Varmepumper, gasfyr, ventilation og klima serviceret og leveret til '
           'erhvervskunder. Fejlsøgning og igangsætning fulgt til dørs, med kvalitet som '
           'aftalen og ikke som undtagelsen.')]),
        ('Senior commissioningeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, DKK 2-10 mio. · 25 specialister · GMP/FDA/EMA',
         [('Resultater og økonomi', '37 projekter styret på tid, økonomi og kvalitet med '
           '25 specialister på tværs af engineering, indkøb og drift. Budget, '
           'ressourceforbrug og ændringer fulgt månedligt, nul kritiske fund ved '
           'aflevering. SAP ERP og PRINCE2 som struktur.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022 – nov. 2022',
         '11 samtidige ventilationsprojekter · 14 mand · underleverandører',
         [('Entreprise', '11 samtidige projekter for offentlige og private kunder, med 14 '
           'mand fordelt på sagerne. Planlægning, administration og udførelse bundet '
           'sammen, aftaler forhandlet med underentreprenører og økonomien fulgt pr. '
           'projekt.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · bioanlæg, HVAC, procesrør · 10 medarbejdere · skiftehold',
         [('Driften', 'Daglig drift og vedligehold med 10 medarbejdere på skiftehold: '
           'bioanlæg, pumper, ventilations- og varmeanlæg, køl, procesrør og HVAC. '
           'Vagtplaner, bemanding og økonomiopfølgning for funktionen, og 5S og Standard '
           'Work indført i værkstedet.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('Grundlaget', 'Produktionsafdeling med 12 mekanikere og teknikere: vagtplan, '
           'materialer og mål. Rodårsagsanalyser der ændrede måden fejl blev håndteret '
           'på, og opbygget ledelseserfaring med både faglært og ufaglært mandskab.')]),
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
    m.bullet('Drift og økonomi', 'Daglig drift med ansvar for økonomi, ressourceforbrug '
             'og effektivitet. Fuldt P&L som ejer (2023-2026), budgetopfølgning i 37 '
             'projekter (Novo 2022-2024) og driftsbudget i døgndrift (Biofos 2017-2022).',
             after=10)
    m.bullet('Ledelse på tværs', 'Funktionærer og faglærte i samme hverdag: 25 '
             'specialister hos Novo, 14 mand i entreprise, 10 i drift, 8 i egen '
             'virksomhed. Klare aftaler, udviklingssamtaler og tid ude hos folkene.',
             after=10)
    m.bullet('Kunder og aftaler', 'Kunder, samarbejdspartnere og underentreprenører '
             'håndteret professionelt: serviceaftaler, tilbud og entrepriseaftaler, og '
             'kunder der blev hos os.', after=10)
    m.bullet('Planlægning og struktur', 'Bemanding, koordinering og opfølgning bundet '
             'sammen i et overblik der holder, fra planlægning og administration til '
             'udførelse på stedet.', after=10)
    m.bullet('Varme, ventilation og køl', 'Tyve års arbejde med varme, ventilation, køl '
             'og procesanlæg: ventilationsentrepriser (Ventek 2022), bioanlæg, HVAC og '
             'procesrør (Biofos 2017-2022), varmepumper og gasfyr (ELOHVAC 2023-2026).',
             after=10)

    m.section('DE FØRSTE 90 DAGE')
    m.para('Planen følger overskriften: retning, struktur, udvikling.', after=8)
    m.bullet('Dag 1-30 · Retning', 'Afdelingen lært at kende indefra: funktionærer, '
             'montører, igangværende opgaver og de aftaler der ligger. Mål: alle ved '
             'hvem jeg er, og jeg ved hvor skoen trykker.', after=10)
    m.bullet('Dag 31-60 · Struktur', 'Bemanding, koordinering og økonomiopfølgning '
             'samlet i et overblik der holder, og samarbejdet med de øvrige afdelinger '
             'sat i system. Mål: driften kører struktureret, uden at nogen gætter.',
             after=10)
    m.bullet('Dag 61-90 · Udvikling', 'Forbedringsmuligheder i arbejdsgange og '
             'samarbejde omsat til konkrete tiltag, og medarbejdernes udvikling sat i '
             'gang. Mål: mindst ét synligt løft i måden vi arbejder på.', after=10)

    m.section('SPROG, VÆRKTØJER OG PRAKTISK')
    m.para('Dansk (modersmål) · engelsk (professionelt) · persisk (modersmål). SAP ERP, '
           'Excel og Microsoft Office. PRINCE2. Kørekort kategori B (manuelt gear). Bor '
           'i Måløv og er indstillet på at flytte tættere på Ringsted ved ansættelse. '
           'Tiltrædelse kan aftales kort.', after=32)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Afdelingsleder VVS i Ringsted · krav og dokumentation',
                   ('Krav i opslaget', 'Dokumenteret erfaring'),
                   [
        ('Solid ledelseserfaring med ansvar for den daglige drift af en afdeling, et '
         'forretningsområde eller en tilsvarende enhed',
         'Driftsansvaret står i CV\u2019et: Biofos\u2019 værksted og vedligehold '
         '(2017-2022, 10 medarbejdere, 24/7-drift), egen virksomhed med fuldt P&L '
         '(2023-2026) og produktionsafdeling hos ARJ (2003-2010).'),
        ('VVS-installatøruddannelse og erfaring fra en tilsvarende stilling',
         'Uddannelsen har jeg ikke, og det skriver jeg ligeud. Min erfaring med '
         'tilsvarende opgaver er til gengæld tyve år med VVS-nære anlæg: varme og '
         'ventilation (Ventek 2022), procesrør, bioanlæg og HVAC (Biofos 2017-2022), '
         'varmepumper, gasfyr og klima (ELOHVAC 2023-2026).'),
        ('Solidt kendskab til branchen og forståelse for forholdene i en '
         'installationsvirksomhed',
         'Branchen har jeg kendt indefra siden 2003: el og installationer, egen '
         'installationsvirksomhed med serviceaftaler og entreprise (2023-2026) og 37 '
         'projekter i stor skala (Novo 2022-2024).'),
        ('Sikre tydelig retning, struktur og opfølgning for både funktionærer og '
         'VVS-montører',
         'Funktionærer og montører ledet side om side: 25 specialister (Novo 2022-2024), '
         '14 mand i entreprise (Ventek 2022) og skifteholdsteknikere (Biofos). Retningen '
         'er givet via tavlemøder, klare aftaler og opfølgning ude på stederne.'),
        ('Motivere, udvikle og fastholde medarbejderne samt sikre klare forventninger, '
         'ansvar og samarbejde',
         'Udvikling og fastholdelse i praksis: 3 lærlinge oplæret til svende (ELOHVAC '
         '2023-2026), AMU-forløb og interne kurser (Biofos, ARJ) og samtaler hvor '
         'forventninger og ansvar blev aftalt, ikke antaget.'),
        ('Sikre hensigtsmæssig bemanding, prioritering og koordinering af afdelingens '
         'samlede opgaver',
         'Bemanding uge for uge: 14 mand fordelt på 11 projekter (Ventek 2022), '
         'vagtplaner i døgndrift (Biofos 2017-2022) og 5 elektrikere med 3 lærlinge '
         'fordelt på sagerne (ELOHVAC 2023-2026).'),
        ('Følge op på afdelingens økonomi, ressourceforbrug og effektivitet inden for '
         'det aftalte ansvarsområde',
         'Tallene er fulgt tæt: fuldt P&L og likviditet som ejer (2023-2026), budget og '
         'opfølgning i 37 projekter (Novo 2022-2024) og ressourceforbrug styret i '
         'entreprise (Ventek 2022).'),
        ('Sikre høj faglig kvalitet, overholdelse af aftaler og en professionel '
         'håndtering af kunder og samarbejdspartnere',
         'Kvalitet og aftaler som målestok: nul kritiske fund ved aflevering (Novo '
         '2022-2024), serviceaftaler fornyet fordi kunderne fik det aftalte (ELOHVAC '
         '2023-2026) og professionel håndtering af underentreprenører (Ventek 2022).'),
        ('Skabe sammenhæng mellem planlægning, administration og udførelse og et godt '
         'samarbejde med de øvrige afdelinger i Uggerly Installation',
         'Sammenhængen er kernen i måden jeg arbejder på: planlægning og administration '
         'bundet til udførelsen i 11 projekter (Ventek 2022) og i driften (Biofos), og '
         'tværgående samarbejde med øvrige funktioner som fast disciplin.'),
        ('Identificere forbedringsmuligheder og sikre løbende udvikling af arbejdsgange, '
         'samarbejde og drift',
         'Forbedringer sat i værk: 5S og Standard Work i værkstedet (Biofos), '
         'rodårsagsanalyser der ændrede fejlhåndteringen (ARJ) og nye servicekoncepter '
         'udviklet og driftet (ELOHVAC 2023-2026).'),
        ('Ledelse af både funktionærer og faglærte medarbejdere',
         'Begge grupper i årevis: funktionærer og specialister (Novo, 25 personer) og '
         'faglærte (ARJ 12, Ventek 14, Biofos 10, ELOHVAC 8). Fællesnævneren er klare '
         'aftaler og tid ude hos folk.'),
        ('God forretningsmæssig forståelse med prioritering af ressourcer og opfølgning '
         'på resultater',
         'Forretningen er øvet i praksis: pris og dækningsbidrag på egne tilbud '
         '(2023-2026), investeringstilbud med månedlig opfølgning (Data Power 2024-2026) '
         'og ressourcer prioriteret når 11 projekter kæmpede om de samme 14 mand (Ventek '
         '2022).'),
        ('Håndtering af driftsmæssige udfordringer',
         'Driftsudfordringer løst undervejs: havari- og akutte udkald (ELOHVAC), '
         'procesnedbrud på skiftehold med LOTO og sikkerhedsprocedurer (Biofos 2017-2022) '
         'og projektændringer på millionbeløb uden at stoppe byggepladsen (Novo 2022-2024).'),
        ('Erfaring med økonomiopfølgning, planlægning og kundehåndtering',
         'De tre ting hænger sammen i mit arbejde: økonomiopfølgning, planlægning og '
         'kundehåndtering i egen virksomhed (2023-2026), i entreprise (Ventek 2022) og i '
         'drift (Biofos). Kundekontakt har været en del af ugen, ikke en undtagelse.'),
        ('Naturlig autoritet og gennemslagskraft, og sætte retning for og følge op på '
         'montørerne på byggepladserne',
         'Autoriteten er bygget i praksis: 35-40 installatører fulgt på byggepladsen og '
         'i tavleværkstedet (NNE 2010-2017), sikkerhedsstop og beslutninger gennemført på '
         'skiftehold (Biofos) og montører fulgt tæt i egen virksomhed (2023-2026).'),
        ('Stille krav og skabe gode relationer til medarbejderne',
         'Krav og relationer i samme arbejde: udviklingssamtaler, faglig sparring og '
         'klare forventninger (ARJ 2003-2010, Biofos, ELOHVAC 2023-2026), og folk der '
         'aftalerne blev holdt.'),
        ('Robust, ligefrem i din kommunikation og gode kommunikative evner internt og '
         'eksternt',
         'Kommunikation på begge led internt og eksternt: rapportering til direktion på '
         'dansk og engelsk (Novo 2022-2024), kundemøder og forhandlinger (ELOHVAC, '
         'Ventek) og daglig ledelseskommunikation på skiftehold (Biofos).'),
        ('Struktureret, vedholdende, udadvendt og kunde-minded',
         'Struktur og vedholdenhed bar 37 projekter i mål uden kritiske fund (Novo '
         '2022-2024), og det udadvendte og kundeorienterede ligger i salgs- og '
         'servicedelen af arbejdet (ELOHVAC 2023-2026).'),
        ('Behersker dansk i skrift og tale og hensigtsmæssig køreafstand til afdelingen i '
         'Ringsted',
         'Sproget i hverdagen er dansk, og engelsk bruger jeg professionelt. Bopælen '
         'er Måløv i dag, cirka 50 minutters kørsel fra Ringsted, og jeg er '
         'indstillet på at flytte tættere på byen ved '
         'ansættelse, så køreafstanden ikke bliver et tema. Kørekort B (manuelt gear), '
         'tiltrædelse kan aftales kort.'),
                   ], widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo — Afdelingsleder VVS, Uggerly Installation')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_UggerlyInstallation_Afdelingsleder_VVS.docx')
    build(out)
    print(out)
