# -*- coding: utf-8 -*-
"""Driftsleder til Gentofte Ejendomme (dansk opslag -> DANSK dokument).

4 sider i masterdesign: brev side 1, CV side 2-3, kravmatrix side 4.
Kontaktperson: Leder af Ejendomsdriften, Thomas Burkal, mobil 2445 1635
-> "Kære Thomas Burkal,". Ansøgningsfrist 9. december 2026 kl. 12:00;
samtaler 14.-15. december 2026; tiltrædelse 1. februar 2027; kontor på
Rådhuset, arbejde på tværs af kommunen; løn efter overenskomst + GKF;
børne- og straffeattest indhentes.

SAMME-FIRMA-REGLER: Gentofte er genansøgning (tidligere DirektoerKMT og
DriftslederEjendomme) -> intet genbruges; alt indhold skrevet friskt.
FILNAVN med _2027 for ikke at overskrive tidligere Gentofte-dokument.

STILVALG (style_guard godkendt, 3/3 skift mod #440 CBRE):
  register    = Tydelig ledelse, tæt på driften
  åbningsgreb = BQ (porteføljen set fra brugerens side: rammen om andres hverdag)
  struktur    = Mennesker, drift, relationer (30/60/90 = menneskerne ·
                driften · relationerne)

BRUGERSVAR 26.11 (bindende): lokation = commute_ok — "Gentofte er fint
(~30 min fra Måløv)" -> bekræft konkret i brevet.

MASTER-REGLER: "elautoriseret maskinmester (LV/MV/HV)" — aldrig "elinstallatør".
BANNED som egne påstande: passioneret, gøre en forskel, dynamisk, demonstreret,
proven track record. Ingen em dash. 'dygtig(e)'-humaniser-advarsel = falsk
positiv (ignorér). 'Dygtige medarbejdere' optræder kun i JD-citat.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_CBRE_TechnicalSupervisor_305257.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Gentofte Ejendomme · Driftsleder'
BANNER_RESUME = 'DRIFTSLEDELSE · EJENDOMSDRIFT · TEAM OG BUDGET'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('26. november 2026')
    m.meta('Driftsleder · Gentofte Ejendomme · ansøgningsfrist 9. december 2026')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Driftsleder til Gentofte Ejendomme', bold=True,
           color='1A1A1A')
    m.para('Kære Thomas Burkal,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('En stor portefølje af forskellige ejendomme og mere end 50 lokationer '
       'lyder som tal på et regneark. For dem, der møder ind om morgenen, er det '
       'rammen om deres dag, og to hverdage sjældent er ens. Arbejdet bag den '
       'ramme er drift og vedligeholdelse af kommunens bygninger, og den daglige '
       'kraft bag den er et selvstyrende team af tekniske servicemedarbejdere '
       'og en ejendomsserviceteknikerelev.')

    lp('Gentofte Ejendomme har ansvaret for driften og arbejder på tværs af '
       'Drift, Byggeri, Vedligehold og vores stabsfunktioner. Rollen er den '
       'daglige ledelse af teamet, og målet er en velfungerende daglig drift '
       'med fokus på kvalitet og gode løsninger, med tæt samarbejde og en '
       'tydelig forventningsafstemning med ledere og brugere. At skabe '
       'retning, trivsel og gode rammer og samtidig omsætte behov, idéer og '
       'beslutninger til konkret handling er kernen i opgaven, og i '
       'ledergruppen hjælper hinanden, deler erfaringer og arbejder på tværs.')

    lp('Krydsfeltet mellem mennesker, drift, udvikling og ledelse er velkendt '
       'terræn. Erfaring med ledelse og personaleansvar har fulgt mig siden '
       '2003: 12 mekanikere i produktionen, 10 medarbejdere på skiftehold i '
       'døgndrift, 5 elektrikere og 3 lærlinge i el-virksomheden og senest '
       '4-10 specialister i en AI-afdeling. Lede, understøtte og udvikle '
       'medarbejderne og teamet gennem tydelighed, dialog og involvering er '
       'ikke nye ord for mig; det er måden, holdene er blevet samlet på, også '
       'når noget skulle ændres. At skabe følgeskab gennem involvering, dialog '
       'og tillid er vejen, og den tydelige ledelse, der sætter en klar retning, '
       'hører med. En hverdag som synlig, tilgængelig og støttende som leder er '
       'udgangspunktet.')

    lp('De første 90 dage følger de tre ting, rollen holder sammen. Dag 1-30 '
       'hører til menneskerne: teamet, opgaverne og rytmen lært at kende, og '
       'skabe overblik, prioritere og vurdere, hvad der skal løses hvornår, så '
       'struktur, prioritering og overblik over opgaver og ressourcer står '
       'klart. Dag 31-60 til driften: vedligeholdelsesbudgetterne bliver '
       'overholdt og brugt ansvarligt, planerne for lokationerne samlet ét '
       'sted, og de mindre vedligeholdelsesprojekter fulgt tæt. Dag 61-90 til '
       'relationerne: stærke relationer til ledere og brugere på de enkelte '
       'lokationer bygget op, og nye samarbejdsaftaler og fælles arbejdsgange '
       'på tværs på plads.')

    lp('Den relevante faglige baggrund inden for bygge- og anlægsområdet er '
       'på plads: maskinmester, elautorisation LV/MV/HV og hænderne i el, '
       'ventilation og procesanlæg siden 2003. Erfaring med '
       'vedligeholdelsesprojekter følger med fra 37 CAPEX-projekter hos Novo '
       'Nordisk og entreprise hos ELOHVAC, og driftsfaglig sparring i '
       'forbindelse med mindre vedligeholdelsesprojekter kan gives fra dag ét. '
       'På relationsiden ligger det naturligt at opbygge og bevare stærke '
       'relationer til ledere og brugere på de enkelte lokationer og holde '
       'forventningsafstemningen løbende, også når planen ændrer sig.')

    lp('Det menneskelige vægtes højt i opslaget, og det passer: social, har '
       'let til smil og respekt for et stærkt kollegialt fællesskab er måden, '
       'mine hold har fungeret på. At god ejendomsdrift skabes af dygtige '
       'medarbejdere, der tager ansvar, samarbejder og oplever tydelig ledelse '
       'og tillid i hverdagen, er en beskrivelse jeg genkender fra driften. Et '
       'arbejdsmiljø med dygtige og engagerede medarbejdere, hvor samarbejde, '
       'humor og faglighed vægtes højt, og en ledergruppe hvor man hjælper '
       'hinanden, deler erfaringer og løfter i fællesskab, tiltaler mig. At være '
       'nysgerrig og lyttende, når de gode løsninger skal findes sammen med '
       'medarbejderne, ligger mig naturligt, og kommunen med plads til '
       'initiativ, ansvar og den gode idé passer måden, jeg arbejder på. Også '
       'rammerne passer: løn efter overenskomst, udsigten til faglig og '
       'personlig udvikling, og børne- og straffeattest indhentes gerne. Kontoret på Rådhuset og arbejdet på tværs af kommunen '
       'fungerer fint fra Måløv, cirka 30 minutter væk, og tiltrædelse 1. '
       'februar 2027 passer. Jeg ser frem til at høre fra dig.', after=44)

    m.para('Med venlig hilsen', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Driftsleder med 20+ år i teknisk drift og personaleansvar, fra '
           'døgndrift på kritiske anlæg til serviceaftaler og entreprise. Hold '
           'på 3 til 25 personer ledet med tydelighed, dialog og involvering, '
           'budgetter fulgt måned for måned, erfaring med ejendomsdrift fra '
           'bygningers tekniske anlæg, og en faglig baggrund fra '
           'bygge- og anlægsområdet: maskinmester med elautorisation '
           'LV/MV/HV. Trives i krydsfeltet mellem mennesker, drift, udvikling '
           'og ledelse.', after=32)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester (el-teknik og ventilation)',
         'Data Power Consultant ApS · København · 2024 – nu (fra nov. 2026 også ELOHVACs '
         'el-tekniske aktiviteter)',
         'AI-afdeling 4-10 personer · el-service og entreprise · 5 elektrikere + 3 lærlinge',
         [('Ledelse og udvikling', 'Teams på 4-10 specialister ledet med tydelig '
           'retning og tæt dialog, og opgaver udviklet sammen med medarbejderne '
           'frem for pålagt. El-service og entreprise styret fra tilbud til '
           'aflevering, med ansvar for økonomi og kvalitet på hver sag.')]),
        ('Ejer / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 – nov. 2026 (virksomheden lukket)',
         'Erhvervskunder · el, ventilation og klima · entreprise · fuldt P&L · serviceaftaler',
         [('Drift, budget og relationer', 'Serviceaftaler på bygningers tekniske '
           'anlæg drevet med forebyggende vedligehold som omdrejningspunkt og '
           'omkostningskontrol på hver sag. 5 elektrikere og 3 lærlinge planlagt '
           'i det daglige, og relationer til kunderne holdt ved lige gennem '
           'fast dialog og opfølgning.')]),
        ('Senior commissioningeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, DKK 2-10 mio. · 25 specialister · GMP/FDA/EMA',
         [('Projekter og økonomi', '37 parallelle projekter med budgetopfølgning '
           'måned for måned og 25 specialister på tværs af engineering, indkøb '
           'og drift. Vedligeholdelses- og investeringsprojekter fulgt fra '
           'konstruktion til idriftsættelse, og dokumentation der holdt til '
           'revision.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022 – nov. 2022',
         '11 projekter · 14 mand · underleverandører · montage og aflevering',
         [('Overblik og prioritering', '11 projekter med 14 mand og '
           'underleverandører styret på tidsplan, økonomi og kvalitet. '
           'Opgaver og ressourcer prioriteret uge for uge, og aflevering med '
           'kunden som en del af processen, ikke en overraskelse til sidst.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · kritiske anlæg · 10 medarbejdere · skiftehold',
         [('Drift og vedligehold', 'Forebyggende og korrigerende vedligehold af '
           'kritiske anlæg døgnet rundt med 10 medarbejdere på skiftehold: '
           'pumper, HVAC, procesrør, el, SCADA og PLC. Reservedelsstyring, '
           'vedligeholdsplaner og dokumentation holdt ajour, og arbejdstilladelser '
           'og sikkerhed en del af hverdagen.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('Mennesker og forbedring', 'Produktionsafdeling med 12 mekanikere og '
           'teknikere: vedligehold, reservedele og planlægning. '
           'Rodårsagsanalyser der ændrede fejlhåndteringen, og et hold samlet '
           'om fælles mål og ansvar.')]),
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
    m.bullet('Ledelse og trivsel', 'Personaleansvar siden 2003 med tydelighed, '
             'dialog og involvering som metode. Teams samlet om fælles mål, '
             'udvikling af medarbejdere og lærlinge, og en synlig hverdag tæt '
             'på opgaverne.', after=10)
    m.bullet('Drift og vedligehold', 'Forebyggende og korrigerende vedligehold '
             'af bygningers tekniske anlæg: el, ventilation, HVAC, pumper og '
             'proces. Planer, dokumentation og reservedelsstyring som en del '
             'af driften, og sparring på mindre vedligeholdelsesprojekter.',
             after=10)
    m.bullet('Budget og struktur', 'Budgetstyring med månedlig opfølgning og '
             'omkostningskontrol, vedligeholdelsesbudgetter brugt ansvarligt, '
             'og struktur, prioritering og overblik over opgaver og ressourcer '
             'i værktøjer som SAP, MS Project og Excel.', after=10)
    m.bullet('Relationer og samarbejde', 'Stærke relationer til kunder, brugere '
             'og samarbejdspartnere bygget på fast dialog og '
             'forventningsafstemning. Nye samarbejdsaftaler og fælles '
             'arbejdsgange på tværs som en naturlig del af udviklingen.',
             after=10)

    m.section('DE FØRSTE 90 DAGE')
    m.para('Planen følger opgaven: menneskerne, driften, relationerne.', after=8)
    m.bullet('Dag 1-30 · Menneskerne', 'Teamet og opgaverne lært at kende i '
             'hverdagen: hvem gør hvad, og hvor er trivslen stærkest og '
             'svagest. Mål: overblik over opgaver og ressourcer, og teamet '
             'ved, hvad retningen er.', after=10)
    m.bullet('Dag 31-60 · Driften', 'Vedligeholdelsesbudgetter og planer gennemgået '
             'for lokationerne, og strukturen på opgaverne samlet ét sted. '
             'Mål: budgetterne overholdt og brugt ansvarligt, og '
             'vedligeholdelsesprojekterne har en plan.', after=10)
    m.bullet('Dag 61-90 · Relationerne', 'Møder og dialog med ledere og brugere '
             'på lokationerne, forventningsafstemning på plads, og første '
             'forslag til nye samarbejdsaftaler og fælles arbejdsgange. Mål: '
             'brugerne kender vejen til teamet, og teamet kender behovene.',
             after=10)

    m.section('SPROG, VÆRKTØJER OG PRAKTISK')
    m.para('Dansk (modersmål) · engelsk (professionelt) · persisk (modersmål). '
           'SAP, MS Project, Excel, CMMS-systemer; PRINCE2. Kørekort kategori B '
           '(manuelt gear). Bosat i Måløv; Gentofte fungerer fint, cirka 30 '
           'minutter væk. Tiltrædelse 1. februar 2027.', after=32)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Driftsleder, Gentofte Ejendomme · krav og dokumentation',
                   ('Krav i opslaget', 'Dokumenteret erfaring'),
                   [
        ('Ledelse og personaleansvar',
         'Personaleansvar siden 2003: 12 mekanikere og teknikere (ARJ '
         '2003-2010), 10 medarbejdere på skiftehold (Biofos 2017-2022), 14 '
         'mand (Ventek 2022), 5 elektrikere og 3 lærlinge (ELOHVAC 2023-2026) '
         'og 4-10 specialister (Data Power 2024-nu). Ledelse med tydelighed, '
         'dialog og involvering.'),
        ('Budgetstyring',
         'Den konkrete erfaring med budgetstyring ligger i månedlig '
         'budgetopfølgning på 37 projekter i 2-10 millioners klassen '
         '(Novo 2022-2024), fuldt P&L-ansvar med omkostningskontrol på hver '
         'sag (ELOHVAC 2023-2026) og løbende økonomistyring i daglig drift '
         '(Hansen 2025-2026). Vedligeholdelsesbudgetter styret ansvarligt.'),
        ('Ejendomsdrift i praksis',
         'Bygningers tekniske anlæg serviceret og vedligeholdt i praksis: el, '
         'ventilation og klima i serviceaftaler (ELOHVAC 2023-2026), '
         'ventilation i bygninger (Ventek 2022) og kritiske anlæg i døgndrift '
         '(Biofos 2017-2022). Ejendomsdrift er opgavetype, ikke overskrift.'),
        ('Kan skabe overblik, prioritere og vurdere, hvad der skal løses hvornår',
         '37 parallelle projekter prioriteret måned for måned (Novo 2022-2024), '
         '11 projekter med 14 mand styret uge for uge (Ventek 2022) og daglig '
         'prioritering af service og entreprise (ELOHVAC 2023-2026). Overblik '
         'bygget på planer, ikke på hukommelse.'),
        ('Er synlig, tilgængelig og støttende som leder',
         'Tæt på opgaverne siden 2003: værksted, skiftehold og byggepladser. '
         'På Biofos (2017-2022) var ledelsen til stede på skiftene, og i '
         'ELOHVAC (2023-2026) kørte jeg selv med ud på opgaverne. Hjælpen '
         'kommer før kritikken.'),
        ('Har mod på forandringer og kan engagere andre i udviklingen',
         'En AI-afdeling bygget fra nul til 4-10 personer (Data Power '
         '2024-nu), forretningsmodel ændret undervejs (ELOHVAC 2023-2026) og '
         'arbejdsgange udviklet sammen med medarbejdere (ARJ, Biofos). '
         'Forandringer forklaret, før de føres ud.'),
        ('En relevant faglig baggrund inden for bygge- og anlægsområdet (en fordel)',
         'Maskinmester (2017) med elautorisation LV/MV/HV (2023), B.Tech i '
         'teknologiledelse og maskinteknik (2017-2022) og håndværksmæssig '
         'baggrund fra el, ventilation og procesanlæg siden 2003. Fagligheden '
         'kan bringes i spil i vedligeholdelsesprojekter.'),
        ('Vedligeholdelsesprojekter som del af hverdagen (en fordel)',
         '37 CAPEX-projekter på tekniske anlæg (Novo 2022-2024), 11 '
         'entrepriseprojekter fra tilbud til aflevering (Ventek 2022) og '
         'løbende renoverings- og udskiftningssager (ELOHVAC 2023-2026, '
         'Biofos 2017-2022). Mindre projekter er en del af det daglige.'),
        ('Lede, understøtte og udvikle medarbejderne og teamet gennem '
         'tydelighed, dialog og involvering',
         'Teams samlet om fælles mål siden 2003: rodårsagsarbejde udviklet '
         'sammen med mekanikerne (ARJ), skiftehold samlet på tværs af vagter '
         '(Biofos) og lærlinge uddannet i praksis (ELOHVAC). Tydelig retning '
         'og plads til initiativ på samme tid.'),
        ('Medansvar for drift og vedligeholdelse af mere end 50 lokationer',
         'Porteføljestørrelsen på 50+ lokationer er en større skala, end jeg '
         'har haft præcist; opgavetypen pr. lokation er velkendt: '
         'serviceaftaler på mange erhvervsadresser (ELOHVAC 2023-2026), '
         'anlægsdrift på flere sites (Biofos 2017-2022) og projekter på både '
         'Kalundborg og Bagsværd (Novo 2022-2024).'),
        ('Sikre at vedligeholdelsesbudgetterne bliver overholdt og brugt ansvarligt',
         'Månedlig budgetopfølgning på 37 projekter (Novo 2022-2024), '
         'omkostningskontrol med P&L (ELOHVAC 2023-2026) og styring af '
         'vedligeholdsomkostninger i døgndrift (Biofos 2017-2022). Budgetter '
         'brugt på det, der holder anlæggene kørende.'),
        ('Sikre struktur, prioritering og overblik over opgaver og ressourcer',
         'Struktur på opgaver og ressourcer sat i system: ugeplaner for 14 '
         'mand (Ventek 2022), vedligeholdsplaner og dokumentation (Biofos '
         '2017-2022), og SAP, MS Project og Excel som faste værktøjer. '
         'Overblik, der kan deles med teamet.'),
        ('Opbygge og bevare stærke relationer til ledere og brugere på de '
         'enkelte lokationer',
         'Relationer holdt ved lige gennem fast dialog: kunder med '
         'serviceaftaler (ELOHVAC 2023-2026), bygherrer og brugere på '
         'projekter (Novo 2022-2024) og daglig kontakt med driftens folk '
         '(Biofos 2017-2022). Forventningsafstemning løbende, ikke årligt.'),
        ('Bidrage med driftsfaglig sparring i forbindelse med mindre '
         'vedligeholdelsesprojekter',
         'Sparring på tekniske løsninger er en del af baggrunden: el, '
         'ventilation, HVAC, pumper og procesanlæg i hånden (Biofos, '
         'ELOHVAC), og commissioning af tekniske anlæg (Novo 2022-2024). '
         'Fagligheden bliver stillet til rådighed.'),
        ('Udvikle arbejdsopgaver, processer og ansvarsområder i samarbejde '
         'med medarbejdere og kolleger',
         'Arbejdsgange udviklet sammen med folkene: rodårsagsanalyser der '
         'ændrede praksis (ARJ 2003-2010), 5S og Standard Work indført i '
         'hverdagen (Biofos) og nye processer bygget i en ung afdeling (Data '
         'Power 2024-nu). Ansvarsområder gjort tydelige, ikke skjulte.'),
        ('Bidrage til nye samarbejdsaftaler og fælles arbejdsgange på tværs',
         'Samarbejdsaftaler forhandlet og indført: serviceaftaler (ELOHVAC '
         '2023-2026), leverandørkontrakter med fælles vilkår (Hansen '
         '2025-2026) og tværgående arbejdsgange mellem afdelinger (Novo '
         '2022-2024). Fælles løsninger fundet på tværs af fagligheder.'),
        ('Skabe retning, trivsel og gode rammer for medarbejderne',
         'Hold ledet med fokus på både resultater og trivsel siden 2003. På '
         'Biofos (2017-2022) blev sikkerhed og faste rammer kombineret med '
         'ansvar til den enkelte, og i ELOHVAC (2023-2026) voksede teamet fra '
         'ingen til 8 personer i gode rammer.'),
        ('Omsætte behov, idéer og beslutninger til konkret handling',
         'Behov omsat til handling i praksis: fejlhåndtering ændret efter '
         'rodårsagsarbejde (ARJ), vedligeholdsplaner bygget på faktiske fejl '
         '(Biofos) og idéer fra teamet ført ud i nye værktøjer (Data Power '
         '2024-nu). Beslutninger fulgt til dørs.'),
        ('Social, har let til smil og forstår værdien af et stærkt kollegialt '
         'fællesskab',
         'Det kollegiale har båret holdene: humor på værkstedet (ARJ), '
         'sammenhold på tværs af skift (Biofos) og fællesskab omkring '
         'projekterne (Ventek, Novo). Samarbejde, humor og faglighed er '
         'ingredienser, ikke tillæg.'),
    ], widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo – Ansøgning Driftsleder, Gentofte Ejendomme')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Gentofte_DriftslederEjendomme_2027.docx')
    build(out)
    print(out)
