# -*- coding: utf-8 -*-
"""Schneider Electric — Project Technician, CTS (Ballerup, req. 134668).

Dansk leverance (opslaget er dansk): opgavefokuseret motiveringsside + CV i ét dokument.
Kultur- og rolleintel: master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md, afsnit om Schneider Electric.
Policy: master/README.md — ekstrem sikkerhed, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'CTS og bygningsautomatik · Idriftsættelse, indregulering og energioptimering'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('5. november 2026')
    m.meta('Schneider Electric Danmark A/S · Lautrupvang 1, 2750 Ballerup · Project Technician, CTS (134668)')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Project Technician — CTS, bygningsautomatik og BMS', bold=True, color='1A1A1A')
    m.para('Til projektafdelingen, Customer Projects, Solutions and Services', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('Et CTS-anlæg er ikke et panel på væggen. Det er bygningens nervesystem: følere, ventiler, spjæld, '
           'pumper og frekvensomformere, der alle skal gøre præcis det, som funktionsbeskrivelsen lover — time efter '
           'time, i varme, ventilation og køl. Idriftsættelse er derfor ikke at få anlægget til at køre. Det er at få '
           'det til at køre rigtigt, og at kunne vise det med tal: temperaturer, differenstryk, luftmængder og '
           'energiforbrug, der holder, når jeg har forladt bygningen. Det er det håndværk, jeg søger hos jer.', after=80)

    m.para('**Jeg griber opgaven an på fire faste måder.** Først punkt for punkt: I/O-liste og punktlister holdes op '
           'mod tavlen, før noget testes, og hvert punkt får en adresse, en skala, en alarmgrænse og en ejer. Dernæst '
           'funktionsafprøvning pr. anlæg — varme, ventilation og køl hver for sig og derefter i sekvens — med '
           'trendlogs, der beviser, at reguleringen rammer setpunktet og bliver der. Så indregulering, hvor jeg måler '
           'før jeg justerer: luftmængder, differenstryk, frem- og returtemperaturer og ventilautoritet, så '
           'energiforbruget er facit og ikke en mavefornemmelse. Og endelig afleveringen: dokumentation, '
           'parameternoter, kurver, brugeroplæring og en gennemgang med kundens driftspersonale, så anlægget bliver '
           'drevet rigtigt af dem, der har det til hverdag.', after=80)

    m.para('Jeg har bygget det op fra tre sider. Som **elautoriseret maskinmester** med B.Tech i Technology Management '
           '& Mechanical Engineering er jeg uddannet i damp- og vandkredsløb, køleanlæg, regulering og maskinlære — '
           'og jeg har elautorisation på LV, MV og HV, så jeg kan stå med både styringen, stærkstrømmen og '
           'dokumentationen uden at vente på en anden. Som **drifts- og vedligeholdelsesleder på Biofos** havde jeg '
           'fem år med 24/7-drift, SCADA, alarmer, pumper, ventilation og højspænding, hvor jeg lærte, at et '
           'reguleringsanlæg kun er så godt som den føler, der sidder bag det. Og som **idriftsættelsesingeniør og '
           'projektleder hos Novo Nordisk** har jeg i to år stået med 37 samtidige anlægsprojekter, FAT/SAT, '
           'IQ/OQ/PQ, BMS- og FMS-ændringer og auditeret aflevering med nul kritiske fund — dokumentation, der '
           'skulle kunne læses og godkendes af nogen, der ikke var i rummet.', after=80)

    m.para('Siden 2023 har jeg drevet **ELOHVAC** med fem elektrikere og tre lærlinge: service, installation og '
           'ombygninger hos erhvervs- og industrikunder, med fuldt P&L og med kunden i telefonen, når noget ikke '
           'virker. Før det var jeg projekt- og værkstedsleder i **Ventek-Air** med 14 medarbejdere og 11 samtidige '
           'ventilationsprojekter — tilbud, kalkuler, underleverandører og afleveringspakker. Den kombination betyder, '
           'at jeg kan programmeringen, kan læse P&ID og el-tegning, kan tale med montøren på væggen og med kunden om '
           'økonomi og tid — og at jeg ved, hvad et anlæg koster at drive videre, når jeg har indreguleret det.', after=80)

    m.para('CTS og BMS er samme fag med to navne: dansk byggebranche siger CTS, og I bruger BMS om løsningerne. '
           'Jeg arbejder i den type systemer til daglig — punktlister, grafik, alarmklasser, trendlogs, tidsplaner og '
           'sekvenser — og jeg har programmeret, testet og idriftsat styringer på tekniske anlæg i både '
           'farmaceutisk produktion og almindelig drift. I jeres projekter betyder det, at jeg kan tage et anlæg fra '
           'tavlen og ind i EcoStruxure Building Operation, få det til at opføre sig som beskrevet, og efterlade '
           'kunden med en bygning, der bruger mindre energi end før.', after=80)

    m.para('Energioptimering er ikke et projekt oven på projektet; det er en egenskab ved den måde, anlægget er sat op '
           'på. Jeg har kørt et PDCA-forløb på et 24/7-anlæg, der tog 40 % af energiforbruget, og jeg ved, hvor '
           'gevinsterne ligger: sekvensstyring mellem varme og køl, natsænkning der holder, luftmængder der ikke står '
           '10 % for højt for en sikkerheds skyld, og alarmgrænser der ikke er sat, så de skjuler et forbrug, ingen '
           'opdager. Hver kWh er en beslutning, nogen har taget i et CTS-anlæg — og den beslutning kan gøres bedre.', after=80)

    m.para('Kunden er en del af arbejdet, ikke en modpart. Jeg er vant til at stå ude hos folk, forklare hvad der sker '
           'og hvornår, melde en forsinkelse samme dag den opstår, og undervise driftspersonalet så de kan bruge '
           'anlægget, når jeg er kørt. Dansk og engelsk på professionelt niveau skriftligt og mundtligt, og jeg '
           'arbejder lige så godt selvstændigt på en byggeplads i Jylland som i et team omkring en tavle i Ballerup.', after=80)

    m.para('Schneiders egne ord rammer mit arbejde præcist: IMPACT-værdierne — **Inclusion, Mastery, Purpose, Action, '
           'Curiosity, Teamwork** — er ikke plakater, men den måde et projekt bliver godt på: nysgerrighed nok til at '
           'forstå anlægget før man rører det, action nok til at tage ansvar for sin egen del, mastery i håndværket, '
           'og teamwork omkring tavlen, kunden og de andre fag. At være med til at gøre bygninger mindre '
           'energiforbrugende er konkret grøn omstilling — og at Schneider er kåret som verdens mest bæredygtige '
           'selskab i TIME (2025) gør ikke opgaven mindre interessant.', after=80)

    m.para('Praktisk: jeg bor i Måløv, fem minutter fra Lautrupvang 1, har kørekort B og er parat til projekter i hele '
           'Danmark — Sjælland, Fyn og Jylland — med de overnatninger, det kræver. Jeg arbejder i SAP og Excel '
           'dagligt og bygger mine egne Python- og Claude-værktøjer til punktlister, afvigelseslogs, alarmstatistik '
           'og energiberegninger, så opfølgningen er hurtig og kan vises frem. Jeg kan starte efter aftale.', after=70)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('CTS-, drift- og projektingeniør med 20+ års erfaring fra tekniske anlæg, bygningsautomatik og reguleret '
           'produktion — elautoriseret maskinmester (LV/MV/HV) og B.Tech i Technology Management & Mechanical '
           'Engineering. Fem år i 24/7-drift med SCADA, alarmer, pumper, ventilation og højspænding; to år med 37 '
           'anlægsprojekter, FAT/SAT, IQ/OQ/PQ og BMS-/FMS-ændringer hos Novo Nordisk, nul kritiske fund; tre år som '
           'indehaver med service, installation og ombygninger inden for elkraft, varme, ventilation og køl. '
           'Idriftsætter, indregulerer og dokumenterer — og måler effekten bagefter.', after=80)

    m.section('CTS, IDRIFTSÆTTELSE OG INDREGULERING')
    for label, body in [
        ('Idriftsættelse og funktionsafprøvning',
         'Punktlister og I/O mod tavlen, skalering, alarmgrænser, trendlogs og funktionsafprøvning pr. anlæg — varme, '
         'ventilation og køl hver for sig og i sekvens — dokumenteret i en afleveringsforretning, der kan læses af '
         'kunden og af den næste tekniker.'),
        ('Indregulering og optimering',
         'Måling før justering: luftmængder, differenstryk, frem- og returtemperaturer, ventilautoritet og '
         'sekvensstyring mellem varme og køl. PDCA-forløb på et 24/7-anlæg tog 40 % af energiforbruget.'),
        ('Programmering og styring',
         'Styringer og sekvenser på tekniske anlæg, PLC- og SCADA-baserede systemer samt BMS/FMS: grafik, '
         'alarmklasser, tidsplaner og grænseflader til anlæg via Modbus og BACnet; fejlfinding hele vejen fra føler '
         'til skærmbillede.'),
        ('Ombygninger i eksisterende anlæg',
         '11 samtidige ventilationsprojekter som projekt- og værkstedsleder og løbende service, installation og '
         'ombygninger i egen virksomhed — med eksisterende drift kørende imens, og med aflevering til en kunde, der '
         'skal kunne bruge anlægget samme dag.'),
        ('Kunde, dokumentation og aflevering',
         'FAT/SAT og IQ/OQ/PQ i 37 GMP-projekter, change control og afvigelser, samt brugeroplæring og gennemgang '
         'med kundens driftspersonale i egne servicekontrakter; nul kritiske fund ved aflevering.')]:
        m.bullet(label, body, after=25)

    m.models_table('VÆRKTØJER OG METODER', ('Opgave', 'Værktøj og dokumenteret anvendelse'), [
        ('CTS/BMS og bygningsautomatik',
         'Punktlister, grafik, alarmklasser, trendlogs, tidsplaner og sekvenser; grænseflader via Modbus og BACnet; '
         'EcoStruxure Building Operation som platform i jeres projekter.'),
        ('Idriftsættelse og test',
         'I/O-check, skalering og grænseværdier, funktionsafprøvning pr. anlæg, FAT/SAT og IQ/OQ/PQ med '
         'sporbarhedsmatrix og dokumenteret accept.'),
        ('Indregulering og energi',
         'Måling af luftmængde, differenstryk og temperaturer før justering; sekvensstyring varme/køl, '
         'natsænkning, behovsstyring og energiberegninger med NPV, IRR og scenarier.'),
        ('El, varme, ventilation og køl',
         'Elautorisation LV/MV/HV, tavler og motorstyringer, frekvensomformere, HVAC-anlæg og køleanlæg fra '
         'uddannelse, drift og service; P&ID og el-tegninger.'),
        ('Projekt og kunde',
         'Tilbud, kalkuler, tidsplan, underleverandører og afleveringspakker; daglig koordinering med kunde, '
         'bygherre og rådgiver og skriftlig opfølgning på aftaler.'),
        ('Sikkerhed og digitalt',
         'LOTO, APV, risikovurdering og arbejdstilladelser før arbejde i drift; SAP og Excel dagligt samt egne '
         'Python/Claude-værktøjer til punktlister, afvigelser og energidata.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · service, installation og ombygninger',
         [('Service og kunder', 'Drift, fejlfinding og ombygninger hos erhvervs- og industrikunder; serviceaftaler '
                                'med responstid og kvalitet som KPI, og kunden orienteret samme dag, når noget ændrer sig.'),
          ('Anlæg og styring', 'El, varme, ventilation og køl i samme leverance: tavler, motorstyringer, '
                               'frekvensomformere og styringer, testet og afleveret med dokumentation.'),
          ('Økonomi og digitalt', 'Tilbud, dækningsgrad og indkøb; Python og Claude API til tilbud, planlægning, '
                                  'checklister og KPI-dashboard — over 40 % produktivitetsløft i virksomheden.')]),
        ('Senior idriftsættelsesingeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024',
         '37 samtidige anlægsprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Idriftsættelse og dokumentation', 'Acceptkriterier, FAT/SAT og IQ/OQ/PQ med sporbar dokumentation og '
                                              'afvigelseshåndtering; nul kritiske fund ved aflevering.'),
          ('BMS- og FMS-ændringer', 'Arbejdet i BMS og FMS i daglig drift og i projekter: punkt- og alarmlister, '
                                    'ændringer af grænser og grafik, verifikation efter ændring og den '
                                    'valideringsdokumentation, der følger.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige ventilationsprojekter · 2–10 mio. kr. pr. projekt',
         [('Ventilation og aflevering', 'Tilbud, kalkuler, underleverandører og afleveringspakker inden for '
                                        'ventilation og tekniske installationer; daglige tavlemøder og flaskehalsanalyser.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos, Lynetten · København · aug. 2017–jan. 2022',
         '24/7-drift · SCADA, pumper, ventilation, højspænding · spildevandsanlæg med miljødokumentation',
         [('Drift, alarmer og regulering', 'Alarmer, driftsforstyrrelser og fejlfinding på pumper, ventiler, '
                                           'ventilation og højspænding; tilstandsdata fra SCADA brugt til prioritering.'),
          ('Forebyggende vedligehold og sikkerhed', 'Vedligeholdelsesplaner, reservedelslager og LOTO/APV i skiftdrift; '
                                                    'standard work, 5S og PDCA i værksted og lager.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran, Iran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · industrielt udstyr',
         [('Anlæg og fejlfinding', 'Vagtplanlægning, materialestyring og opfølgning på mål; fejlfinding, '
                                  'rodårsagsanalyse og korrigerende handlinger på produktionsudstyr.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        m.doc.paragraphs[-1].runs[0].text = 'Omfang: '
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('UDDANNELSE OG AUTORISATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering',
          'Maskinmesterskolen København · 2017–2022 · EQF 6 · GPA 7,6/12')
    m.edu('Elautoriseret maskinmester (LV/MV/HV), stærkstrøm', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('Damp- og vandkredsløb, køleanlæg og maskinlære',
          'Maskinmesterskolen København · Mercantec 2021 · Søfartsstyrelsen 2021–2023')
    m.edu('El- og maskinteknisk design, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Lean og procesforbedring: 5S, PDCA, VSM, A3, Kaizen',
          'Løbende kurser og daglig anvendelse i drift og projekter')

    m.section('SPROG, PRAKTISK OG REFERENCER')
    m.para('Dansk og persisk: modersmål · Engelsk: professionelt, skriftligt og mundtligt · Kørekort B · Bopæl i '
           'Måløv, fem minutter fra Lautrupvang 1 · Parat til rejser og projekter i hele Danmark med de overnatninger, '
           'det kræver · SAP og Excel i daglig brug · Referencer fra Novo Nordisk og Biofos samt fra kunder og '
           'samarbejdspartnere i egen virksomhed oplyses efter aftale.', after=70)
    m.para('Schneiders Trust Charter — tillid som grundlag for samarbejde og teamånd — passer på den måde, jeg arbejder '
           'på: klare aftaler, tidlig information og ærlig opfølgning, også når noget er gået galt.', after=70)

    m.models_table('KRAV I OPSLAGET — MIN DOKUMENTATION', ('Krav', 'Dokumentation'), [
        ('Erfaring med CTS-systemer',
         'Arbejder i CTS/BMS til daglig — bygningsautomation er mit fag: punktlister, grafik, alarmklasser, '
         'trendlogs, tidsplaner og sekvenser, de samme systemer som en CTS-tekniker og en automatiktekniker arbejder '
         'i, fra Novo Nordisks BMS/FMS, SCADA-drift på Biofos og styringer i egne el- og HVAC-projekter.'),
        ('Installere og konfigurere software og hardware',
         'Konfiguration af styringer og grænseflader, tavler, motorstyringer og frekvensomformere; elautorisation '
         'LV/MV/HV, ti år med installation, test og dokumentation af tekniske anlæg samt anlægsforståelse for '
         'komponenter.'),
        ('Idriftsætte og indregulere tekniske anlæg',
         'I/O-check, funktionsafprøvning og aflevering i 37 anlægsprojekter hos Novo Nordisk og i 11 '
         'ventilationsprojekter hos Ventek-Air; indregulering med måling før justering og energi som facit.'),
        ('Ombygninger og udvidelser af eksisterende systemer',
         'Løbende ombygninger hos erhvervs- og industrikunder i egen virksomhed og ændringer i eksisterende '
         'BMS/FMS-anlæg under GMP med change control og verifikation efter ændringen.'),
        ('Digital erfaring, programmering og bygningsfunktioner som varme, ventilation og køling',
         'Styringer og sekvenser på tekniske anlæg, PLC/SCADA og BMS; maskinmester med damp- og vandkredsløb, '
         'køleanlæg og regulering; HVAC-projekter og service på varme-, ventilations- og køleanlæg.'),
        ('Kendskab til segmenter inden for bygningsområdet',
         'Farmaceutisk produktion (Novo Nordisk), forsynings- og procesanlæg (Biofos), industri og erhverv samt '
         'ventilationsentrepriser (Ventek-Air) — hvert segment med egne krav til dokumentation og drift.'),
        ('Selvstændig, kan planlægge egen tid, kundeorienteret og teamorienteret',
         'Tre år som indehaver med fuldt P&L, egne kunder og ansvar for at planlægge min egen og virksomhedens tid; '
         'fem år i skiftdrift og to år som projektleder med 25 specialister i et team — og daglig kontakt med '
         'kunder, bygherrer og rådgivere.'),
        ('Dansk og engelsk i skrift og tale',
         'Dansk modersmål, engelsk professionelt skriftligt og mundtligt; to år i en international projektorganisation '
         'med engelsk som arbejdssprog.')])
    m.page_break()

    m.models_table('FØRSTE 90 DAGE — FRA TAVLE TIL AFLEVERING', ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'Ind i jeres projektafdeling og ud på et kørende projekt: læs funktionsbeskrivelse, punktlister og '
         'grænseflader, gå tavlen igennem med den tekniker, der har bygget den, og se, hvordan EBO-projektet er '
         'struktureret i jeres standarder.'),
        ('Dag 30',
         'Jeg har selvstændigt idriftsat og afprøvet et anlæg hos en kunde — dokumenteret i jeres skabeloner og '
         'gennemgået med projektlederen. En liste over de ting, der typisk driller i afleveringen, er skrevet ned og '
         'delt med teamet.'),
        ('Dag 60',
         'To kundeafleveringer gennemført med brugeroplæring, og mindst ét anlæg indreguleret med målinger før og '
         'efter, så energigevinsten kan vises i tal. Mine checklister for I/O, alarmer og funktionsafprøvning er '
         'tilpasset jeres standarder.'),
        ('Dag 90',
         'Jeg kører projekter selvstændigt i hele landet og er den kollega, projektlederen sætter på det anlæg, hvor '
         'der er mest på spil. En skreven arbejdsmetode — punkt for punkt, med målinger og aflevering — ligger i '
         'teamet, så den ikke afhænger af mig.')])

    m.section('CTS ER BYGNINGENS NERVESYSTEM')
    m.para('Et CTS-anlæg består af få hundrede små beslutninger, som ingen ser: en føler, der skal sidde rigtigt, en '
           'ventil, der skal have den rigtige karakteristik, et spjæld, der skal have den rigtige slaglængde, og en '
           'sekvens, der skal vide, hvad der har prioritet, når både varme og køl kalder. Fejlen ligger sjældent i '
           'softwaren alene; den ligger i overgangen mellem det fysiske anlæg og styringen. Derfor starter jeg altid '
           'med det fysiske, før jeg skriver en linje kode, og derfor kan jeg lide arbejdet: det er håndværk og '
           'logik i samme opgave.', after=80)

    m.section('IDRIFTSÆTTELSE PUNKT FOR PUNKT')
    m.para('Min rækkefølge er fast: I/O-liste mod tavle, skalering og enheder, grænseværdier og alarmklasser, '
           'trendlogs på de vigtigste målinger, og derefter funktionsafprøvning pr. anlæg — varme, ventilation og '
           'køl hver for sig, og til sidst sekvensen mellem dem. Hvert punkt får en ejer og en dokumenteret accept, '
           'så afleveringen er et bevis og ikke en samtale. Jeg har gjort det samme i 37 GMP-projekter, hvor '
           'dokumentationen var en del af leverancen — og hvor en manglende underskrift stoppede en frigivelse.', after=80)

    m.section('INDREGULERING: MÅL FØR DU JUSTERER')
    m.para('Indregulering er ikke at skrue, til det ser rigtigt ud. Det er at måle luftmængder, differenstryk, '
           'fremløbs- og returtemperaturer og ventilautoritet, og derefter justere det, der faktisk afviger. '
           'Rækkefølgen betyder mest: er sekvensen mellem varme og køl sat rigtigt, forsvinder det meste '
           'samtidige forbrug af sig selv; står en luftmængde 10 % for højt for en sikkerheds skyld, koster det '
           'energi hver dag, året rundt. Jeg dokumenterer målingerne, så kunden kan se forskellen — og så næste '
           'tekniker ved, hvad der er gjort.', after=80)

    m.section('ENERGIFORBRUGET ER FACIT')
    m.para('Jeg har kørt et PDCA-forløb på et 24/7-anlæg, der reducerede energiforbruget med 40 %, og det lærte mig, '
           'at gevinsterne sjældent kommer fra ét stort indgreb, men fra mange små, der bliver fulgt op. Derfor vil '
           'jeg altid kunne svare på, hvad et anlæg bruger, hvorfor det bruger det, og hvad det ville koste at gøre '
           'det bedre — i kWh og i kroner. Hos Schneider betyder det, at en aflevering ikke slutter med en '
           'funktionstest, men med et tal, kunden kan tage med videre i sin klimarapportering.', after=80)

    m.section('KUNDEN OG DRIFTEN EFTER AFLEVERING')
    m.para('Det er kundens driftspersonale, der afgør, om et anlæg bliver kørt godt et år efter, at jeg er kørt. '
           'Derfor gennemgår jeg altid grafik, alarmer, tidsplaner og de tre ting, der oftest går galt, sammen med '
           'dem — og efterlader en kort, skreven vejledning ud over den officielle dokumentation. Tre år med egne '
           'kunder har lært mig, at ærlig og tidlig information om en forsinkelse eller en merudgift koster mindre '
           'tillid end en overraskelse senere.', after=80)

    m.section('TEAMET OG REJSERNE')
    m.para('Jeg har ledet 14 medarbejdere i Ventek-Air, 12 mekanikere i ARJ og fem elektrikere i ELOHVAC, og jeg ved, '
           'at et godt projektteam er kendetegnet ved, at viden deles uden at nogen skal spørge om lov. Jeg giver '
           'gerne mine egne skabeloner, mine målemetoder og mine Python-værktøjer videre. Rejserne i hele Danmark er '
           'ikke et problem men en del af arbejdet: jeg bor fem minutter fra Ballerup og har bil og kørekort B.', after=80)

    m.section('DIGITALT: PROGRAMMERING OG DATA')
    m.para('Jeg programmerer styringer og sekvenser, og jeg bruger Python og Claude til det, der ellers tager tid: '
           'punktlister der kan sammenlignes mellem tavle og system, afvigelseslogs med ejer og frist, '
           'alarmstatistik der viser de gentagne fejl, og energiberegninger med NPV og scenarier. Det erstatter '
           'hverken EBO eller jeres projektmodel, og det sker inden for jeres procedurer — men det gør opfølgningen '
           'hurtig nok til, at den bliver gjort.', after=80)

    return m.save(path, title='Ansøgning og CV — Project Technician, CTS, Schneider Electric',
                  subject='Idriftsættelse og indregulering af CTS- og BMS-anlæg i hele Danmark',
                  keywords='CTS, BMS, bygningsautomatik, idriftsættelse, indregulering, varme, ventilation, køl')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Schneider_ProjectTechnicianCTS.docx')))
