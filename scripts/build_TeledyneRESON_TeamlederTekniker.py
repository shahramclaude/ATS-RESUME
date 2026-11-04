# -*- coding: utf-8 -*-
"""Teledyne RESON A/S (via ScanPeople) — Teamleder til teknikerteam.

Opgave-først ansøgning + CV i ét dokument (masterdesign).
Kultur og fagligt indhold: se master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md,
afsnittet om Teledyne RESON (research 04.11.2026).
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Produktions- og personaleledelse · Teknik, kvalitet og flow'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('4. november 2026')
    m.meta('Teledyne RESON A/S · Produktionen, Slangerup · via ScanPeople, Rasmus De Roepstorff Christiansen')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Teamleder til teknikerteam', bold=True, color='1A1A1A')
    m.para('Til Teledyne RESON A/S og ScanPeople', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('Et teknisk produkt forlader først huset, når montagen er dokumenteret, testen er bestået og '
           'reparationen er lukket. Det sker kun, hvis de 13 erfarne teknikere i teamet ved, hvad der er vigtigst i '
           'dag — og hvis planlægning, indkøb, Service, R&D og PTA arbejder efter samme billede. Derfor ser jeg '
           'teamlederrollen som overblik før kontrol: hvad skal i montage, hvad venter på test, hvad mangler en '
           'reservedel, og hvad skal tilbage til R&D. Erfarne teknikere skal ikke styres. De skal have rammer, der '
           'gør det muligt at levere høj kvalitet til tiden.', after=80)

    m.para('**Systemet er allerede bygget, og det kan være i drift i løbet af de første uger.** Et kort tavlemøde '
           'hver morgen med opgavekø pr. tekniker og en skreven prioriteringsnøgle: sikkerhed og stop først, derefter '
           'kundelovede datoer, test og reparation med kunde ventende, og til sidst alt det, der kan flyttes uden at '
           'skade nogen. Et grænsefladekort for planlægning, indkøb, Service og R&D, så det er tydeligt, hvem der '
           'ejer hvad, når en ordre står stille. En KPI-tavle med levering til tiden (OTD), gennemløbstid, rework og '
           'åbne ordrer — og en ugentlig kapacitetsmodel, der viser, om ordrebogen kræver flere timer, end teamet har. '
           'Beslutningsretten skrives ned, så teknikerne kan træffe de faglige valg selv, og jeg kun løfter det, der '
           'kræver R&D, økonomi eller ledelsen.', after=80)

    m.para('Menneskene er den anden halvdel, og her har jeg en fast praksis. Performance Reviews tager jeg som en '
           'aftale med konkrete punkter, ikke som en hyggesamtale, og følger op kvartalsvis. Situationsbestemt ledelse '
           'og delegeringstrappen bruger jeg til at afstemme, hvor meget retning og støtte den enkelte skal have — '
           'erfarne specialister skal have ansvar, ikke instrukser. GROW bruger jeg, når en medarbejder skal finde sin '
           'egen vej til en svær opgave, og SBI når noget skal siges ligeud og ordentligt. Kompetencerne står på en '
           'kompetencematrix med to personer på hver kritisk testfærdighed, så bemanding og ferieplaner ikke gør teamet '
           'sårbart. Synlig ledelse betyder for mig at være på gulvet, når der er travlt — autoritet kommer af at være '
           'til stede og holde, hvad man lover. Psykologisk tryghed er i min praksis et spørgsmål, der kan stilles '
           'højt: »Er vi sikre på den her test?«', after=80)

    m.para('Arbejdsformen er afprøvet. Hos Novo Nordisk koordinerede jeg 25 specialister i 37 samtidige CAPEX-projekter '
           'og stod i FAT/SAT og IQ/OQ/PQ under GMP-krav uden kritiske afvigelser. Hos Ventek-Air styrede jeg 14 '
           'medarbejdere og 11 parallelle projekter; hos Biofos drev jeg 24/7-anlæg med pumper, højspændingstavler og '
           'SCADA; og hos ELOHVAC leder jeg i dag fem elektrikere og tre lærlinge med fuldt P&L-ansvar og SAP-baseret '
           'økonomiopfølgning. Jeg er vant til at være tæt på både maskinen og mennesket bag den.', after=80)

    m.para('Ét punkt skal siges klart: jeg er ikke uddannet elektronikfagtekniker, og jeg har ikke ledet '
           'serieproduktion af elektronisk udstyr før. Min baggrund er elektriker og elektromekaniker, B.Tech i Technology '
           'Management & Mechanical Engineering (maskinmesterretningen, EQF 6) og elautorisation LV/MV/HV, med tavler, '
           'styring, PLC/SCADA, test og fejlfinding i praksis. Derfor har jeg lagt en indkøringsplan frem: IPC-A-610 '
           'og ESD-sikring som standard for montage og håndtering, jeres testudstyr og akustiske testfaciliteter '
           'sammen med teamets nøglepersoner, ISO 9001:2015-systemet, som virksomheden har været certificeret efter '
           'siden 2004, ERP og PTA-samarbejdet — og den sikkerhedsgodkendelse, som leverancer til forsvarskunder '
           'kræver, er jeg naturligvis indstillet på at gennemgå.', after=80)

    m.para('Jeg søger stillingen, fordi rammerne passer til den måde, jeg arbejder på. Teledyne Way bygger på '
           'Integrity, Respect, Responsibility og Citizenship, og hos RESON er ledelseslinjen formuleret ligeud af '
           'jeres adm. direktør: »It’s all about people« — den unikke kultur og de medarbejdere, der allerede er der, '
           'er fundamentet. Det er også mit udgangspunkt: udvikle dem, vi har, før vi leder efter nye. Jeg udfordrer '
           'gerne status quo, når det skaber værdi, men med respekt for det håndværk og den faglighed, der har gjort '
           'produkterne verdensklasse.', after=80)

    m.para('Jeg er professionel og aktiv Claude-koder og bygger selv værktøjer i Python til KPI, kvalitetsopfølgning, '
           'kapacitetsmodeller og investeringsmodeller med NPV, IRR og følsomhed. I produktionen betyder det konkret '
           'mindre tid på at trække tal ud af systemerne og mere tid på gulvet: en model der viser, hvor mange '
           'teknikertimer næste måneds ordrebog kræver, og en tavle der opdaterer sig selv. Det sker inden for jeres '
           'systemer og godkendelser.', after=80)

    m.para('Jeg vil gerne komme forbi Fabriksvangen og gennemgå, hvordan jeg vil drive den daglige drift, '
           'kompetenceudviklingen og forbedringsarbejdet de første 90 dage.', after=80)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Teknisk produktions- og personaleleder med 20+ års erfaring i el, mekanik, drift og kvalitet. Har ledet '
           'teknikere og specialister i produktion, entreprise og 24/7-drift, stået i spidsen for test, idriftsættelse '
           'og afvigelseshåndtering og er vant til at eje både kvalitet, kapacitet og økonomi. Arbejder datadrevet med '
           'SAP, KPI-tavler og egne AI-værktøjer (Python, Claude) til planlægning, kvalitet og investeringsmodeller.',
           after=80)

    m.section('LEDELSE — ANSVAR OG RESULTATER')
    for label, body in [
        ('Mennesker, bemanding og udvikling',
         'Leder fem elektrikere og tre lærlinge hos ELOHVAC med Performance Reviews, MUS og strukturerede '
         'oplæringsforløb. Har tidligere ledet 14 medarbejdere hos Ventek-Air og 12 teknikere i ARJ.'),
        ('Kvalitet og test',
         'FAT/SAT og IQ/OQ/PQ i GMP-regulerede projekter hos Novo Nordisk uden kritiske afvigelser ved aflevering. '
         'Kvalitetskontrol, dokumentation og afvigelser med ejer og frist i alle tekniske leverancer.'),
        ('Kapacitet og flow',
         'Planlagde 11 parallelle projekter hos Ventek-Air fra specifikation til aflevering. Tavlemøder og '
         'flaskehalsanalyse gjorde prioriteringer og kapacitet synlige for projektlederne.'),
        ('Drift, oppetid og økonomi',
         'Drev kritiske anlæg 24/7 hos Biofos med pumper, HVAC, højspændingstavler og SCADA. Har i dag fuldt '
         'P&L-ansvar hos ELOHVAC med SAP til økonomi og ressourcer.'),
        ('Digital praksis',
         'Professionel og aktiv Claude-koder. Python/Claude API-værktøjer til tilbud, tidsplaner, KS og KPI har '
         'givet et dokumenteret produktivitetsløft på over 40 %. Bygger investeringsmodeller med NPV, IRR og '
         'scenarier til udvikling og nye forretningsidéer.')]:
        m.bullet(label, body, after=30)

    m.models_table('LEDELSESVÆRKTØJER OG METODER', ('Opgave', 'Værktøj og dokumenteret anvendelse'), [
        ('Styre den daglige drift',
         'Tavlemøder, Gemba og visuel KPI-tavle med opgavekø og prioriteringsnøgle. Brugt hos Ventek-Air (14 '
         'medarbejdere, 11 projekter) og ELOHVAC.'),
        ('Udvikle og bedømme medarbejdere',
         'Performance Reviews/MUS, situationsbestemt ledelse (SLII), delegeringstrappen, GROW og SBI. Fast praksis '
         'i den daglige personaleledelse hos ELOHVAC.'),
        ('Sikre kvaliteten',
         'A3, PDCA, 5 x hvorfor, Ishikawa og FMEA; kvalitetskontrol, dokumentation og afvikling af afvigelser. '
         'Brugt hos Novo under GMP og hos Biofos i 24/7-drift.'),
        ('Forbedre processer',
         'Lean: Standard Work, 5S, VSM, Kaizen og SMED; flaskehalsanalyse og gennemløbstid som måltal. Brugt hos '
         'Biofos og ARJ i værksted og produktion.'),
        ('Planlægge kapacitet og økonomi',
         'SAP ERP, KPI/OTD, kapacitetsmodel pr. måned, investeringsmodeller med NPV/IRR. Brugt hos Novo og i egen '
         'virksomhed med fuldt P&L-ansvar.'),
        ('Sikkerhed og risiko',
         'Risikoregister med ejer og frist, APV, LOTO og risikovurdering ved opstart af arbejde og nye opgaver.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L-ansvar · serviceaftaler med responstid som KPI',
         [('Personaleledelse', 'Daglig planlægning, Performance Reviews og MUS, oplæring af lærlinge samt opfølgning '
                               'på arbejdsmiljø og trivsel på skiftende opgaver.'),
          ('Leverance og kvalitet', 'Tilbud, beregning, materialer, underentreprenører, kvalitetskontrol og '
                                    'afleveringsdokumentation på el-, ventilations- og klimaanlæg.'),
          ('Digitale værktøjer', 'Python/Claude API til tilbud, tidsplaner, KS-tjeklister og KPI-dashboard; over '
                                 '40 % produktivitetsløft i virksomheden.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024',
         '37 samtidige CAPEX-projekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Test og idriftsættelse', 'FAT/SAT og IQ/OQ/PQ uden kritiske afvigelser ved aflevering; A3 og 5 x hvorfor '
                                     'i fejlfinding; dokumenteret testgrundlag og sporbarhed.'),
          ('Fremdrift, risiko og grænseflader', 'Fulgte fremdrift, økonomi, risici og ressourcer mellem engineering, '
                                                'indkøb og anlæg; SAP ERP til økonomi og aktiver og månedlig '
                                                'rapportering til ledelse og bygherre.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter · DKK 2–10 mio. pr. projekt',
         [('Kapacitet og prioritering', 'Planlægning fra specifikation til formel aflevering, udbud og tilbud, '
                                        'underentreprenører og afleveringspakker. Daglige tavlemøder og '
                                        'flaskehalsanalyser gav et markant løft i leveringsevnen.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos, Lynetten · København · aug. 2017–jan. 2022',
         '24/7-drift · pumper, HVAC, højspændingstavler og SCADA · skiftehold',
         [('Tilgængelighed og standarder', 'Forebyggende vedligehold, akut fejlfinding, reservedelsflow og lager. '
                                           '5S, Standard Work og PDCA på værksted og lager; LOTO, APV og '
                                           'risikovurdering i skifteholdsdrift.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted',
         [('Plan og mål', 'Vagtplanlægning, materialestyring og målopfølgning; fejldiagnose, rodårsagsanalyse og '
                          'korrigerende handlinger på industrielt el- og mekanisk udstyr.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        m.doc.paragraphs[-1].runs[0].text = 'Omfang: '
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('UDDANNELSE OG AUTORISATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering — maskinmesterretningen',
          'Maskinmesterskolen København · 2017–2022 · EQF 6 · GPA 7,6/12')
    m.edu('El- og maskinteknisk design, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('Køleteknik og klimaanlæg · STCW-sikkerhed og maskinrumsvagt',
          'Mercantec 2021 · Søfartsstyrelsen 2021–2023')

    m.section('SPROG, PRAKTISK OG REFERENCER')
    m.para('Dansk og persisk/farsi: modersmål · Engelsk: professionelt i skrift og tale · Kørekort B · Bopæl i Måløv, '
           'ca. 20 minutter fra Fabriksvangen i Slangerup · Indstillet på den sikkerhedsgodkendelse, leverancer til '
           'forsvarskunder kræver. Tidligere ledere hos Novo Nordisk og Biofos oplyses efter aftale.', after=70)

    m.models_table('KRAV I OPSLAGET — MIN DOKUMENTATION', ('Krav', 'Dokumentation'), [
        ('Personaleledelse i produktion eller teknisk miljø',
         'Fem elektrikere og tre lærlinge i dag, 14 medarbejdere hos Ventek-Air og 12 teknikere i ARJ.'),
        ('Teknisk forståelse for elektronik, montage og test',
         'Elektriker og elektromekaniker i bund, elautoriseret maskinmester, tavler, styring, PLC/SCADA, '
         'fejlfinding samt FAT/SAT og IQ/OQ/PQ. Ikke uddannet elektronikfagtekniker — indkøringsplan nedenfor.'),
        ('Performance Reviews',
         'Fast praksis med Performance Reviews/MUS, udviklingsaftaler og kvartalsvis opfølgning.'),
        ('Kompetenceudvikling og rette bemanding',
         'Kompetencematrix med to personer pr. kritisk færdighed, oplæringsforløb og rekruttering ved behov.'),
        ('Optimere arbejdsgange og processer',
         'Standard Work, 5S, VSM, Kaizen, SMED og A3/PDCA med gennemløbstid og OTD som måltal.'),
        ('Synlig ledelse på tværs af produktionsområder',
         'Tavlemøder, Gemba og grænsefladekort mellem planlægning, indkøb, Service, R&D og PTA.'),
        ('ERP og administrative systemer',
         'SAP ERP til økonomi, aktiver og ressourcer; CMMS og digitale tjeklister.'),
        ('Tydelig kommunikation og beslutningsdygtighed',
         'Skreven beslutningsret og prioriteringsnøgle, SBI-feedback i 1:1 og Performance Reviews, og daglig '
         'kommunikation fra tavlen frem for fra kontoret.'),
        ('Samarbejde med R&D om produktlancering',
         'NPI-forløb og idriftsættelse hos Novo med engineering, indkøb og anlæg; prøvning og accept før overlevering.')])
    m.page_break()

    m.models_table('FØRSTE 90 DAGE — DRIFT, MENNESKER OG FORBEDRING', ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1',
         'Møde alle 13 teknikere, teamlederen i Montage, planlægning og indkøb samt R&D og Service. Gennemgå åbne '
         'ordrer, testkø og kendte kvalitetsproblemer. Aftale mandat og beslutningsret, og hvem der kvalitetssikrer '
         'fagligt, indtil jeg selv kan.'),
        ('Dag 30',
         'Tavlemøde og opgavekø i drift med skreven prioriteringsnøgle. Grænsefladekort på plads. Performance Reviews '
         'planlagt, kompetencematrix dækket, og KPI-baseline for OTD, gennemløbstid og rework lagt frem.'),
        ('Dag 60',
         'Ugentlig kapacitetsmodel mod ordrebogen, så bemanding, overarbejde og rekrutteringsbehov ses i tid. Første '
         'A3 på den flaskehals, teamet selv peger på. Test- og reparationsflow gennemgået med R&D og Service.'),
        ('Dag 90',
         'Status på leveringsevne, kvalitet, gennemløbstid og trivsel fremlagt for ledelsen. Opfølgning på '
         'kompetenceplanen, på de første forbedringer og på de grænseflader, hvor der stadig opstår ventetid.')])

    m.section('TEKNISK INDKØRING — ELEKTRONIK, MONTAGE OG TEST')
    m.para('Jeg kommer med el-teknisk håndværk og produktionserfaring, ikke med elektronikfagteknikerens uddannelse. '
           'Indkøringen følger fire spor: IPC-A-610 som fælles acceptgrundlag for montage og loddearbejde, ESD-sikring '
           'i håndtering og opbevaring, jeres testudstyr og akustiske testfaciliteter sammen med teamets nøglepersoner, '
           'og ISO 9001:2015-systemet med tilhørende procedurer, afvigelser og audit. Målet er ikke at blive den '
           'bedste tester i huset, men at kunne stille de rigtige faglige spørgsmål, genkende en afvigelse og sikre, '
           'at svaret kommer fra den rette person.', after=80)

    m.section('KVALITET OG FORBEDRING I HVERDAGEN')
    m.para('Kvalitet er ikke en kampagne, men et flow. Jeg vil arbejde med tre tal, som teamet selv kan påvirke: '
           'levering til tiden, gennemløbstid pr. ordre og rework. De hænger sammen — pres på leveringstid uden '
           'kapacitet giver genarbejde, og genarbejde spiser den kapacitet, der skulle have løst næste opgave. '
           'Derfor tages afvigelser op med det samme med 5 x hvorfor og A3, når den samme fejl dukker op to gange, '
           'og forbedringer besluttes med dem, der skal leve med dem.', after=80)

    m.section('KOMPETENCEUDVIKLING DER KAN SES')
    m.para('Udvikling skal kunne ses i planen, ikke kun høres i samtalen. Hver medarbejder får en kort udviklingsaftale '
           'med et fagligt mål og et ansvar, der rækker ud over egen opgave — at være nøgleperson på en testtype, at '
           'oplære en kollega eller at eje en forbedring. Engagement kommer af at vide, hvorfor opgaven betyder noget, og '
           'af at blive spurgt til råds — det er den mest effektive måde at motivere erfarne teknikere på. Jeg bruger '
           'sidemandsoplæring og korte interne gennemgange frem for lange kursusplaner, og følger op i Performance '
           'Reviews, så det står klart, hvad der er lært, og hvad næste skridt er.', after=80)

    m.section('SAMARBEJDE, NÅR PLANEN ÆNDRER SIG')
    m.para('Kommer en hasteordre ind, eller mangler der en komponent, skal konsekvensen frem med det samme: hvilken '
           'leverance berøres, hvilke timer flytter, og hvad skal R&D, Service eller kunden vide? Et kort møde med de '
           'involverede og en skriftlig aftale om ansvar, frist og tilbagemelding giver ro — og en kunde, der hører om '
           'ændringen fra os, før den rammer leverancen.', after=80)

    m.section('DIGITALT ARBEJDE MED ET KLART FORMÅL')
    m.para('Jeg bygger værktøjer i Python og Claude til KPI, kvalitetsopfølgning og kapacitetsplanlægning samt '
           'investeringsmodeller med NPV, IRR, følsomhed og scenarier. I en produktionsvirksomhed kan det flytte tid '
           'fra rapporttræk til gulv og dialog: en tavle der opdaterer sig selv, en model der viser behovet for '
           'teknikertimer pr. måned, og et beslutningsoplæg der viser, hvad en ekstra testkapacitet koster over fem år. '
           'Det forudsætter godkendte systemer, menneskelig kontrol og respekt for kvalitetssystemet.', after=80)

    return m.save(path, title='Ansøgning og CV — Teamleder til teknikerteam, Teledyne RESON',
                  subject='Personaleledelse, kvalitet og produktionsflow',
                  keywords='teamleder, produktion, elektronik, montage, test, kvalitet, ERP')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_TeledyneRESON_TeamlederTekniker.docx')))
