# -*- coding: utf-8 -*-
"""Andel Energi · Teknisk Specialist, Teknik & Service (Svinninge), dansk opslag.

Dansk opslag -> dansk dokument. Masterdesign (scripts/master_design.py): brev side 1, CV side 2-3,
kravmatrix side 4. Kun fakta fra master-CV'et og brugerbekræftelser.
Ikke dokumenteret og derfor ikke skrevet som erfaring: varmepumper (beregning, installation, support,
reklamation), VVS-installatøruddannelse, VE-uddannelse, teknisk salgssupport og produktmanagement for varmepumper,
ankeklagesager. Varme generelt er erfaring fra ELOHVAC; fjernvarme er interesse, ikke erfaring.
Pendling til Svinninge og to kontordage om ugen er ikke bekræftet (double-check).
Opslaget har ingen frist: "hurtigst muligt" og løbende samtaler. Kontakt: afdelingsleder Niels Bigum, +45 71 96 07 55.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
OUT_DIR = os.path.join(ROOT, 'output')
OUT = os.path.join(OUT_DIR, 'Shahram_Ajloo_AndelEnergi_TeknikSpecialist.docx')
KRAV = os.path.join(ROOT, 'jd', 'Andel_TeknikSpecialist_krav.txt')
KULTUR = os.path.join(ROOT, 'jd', 'Andel_TeknikSpecialist_kultur.txt')

NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Teknisk Specialist, Teknik & Service · Andel Energi, Svinninge'
BANNER_RESUME = 'Teknisk support, installationsforståelse og reklamationsarbejde i reguleret industri'

# (krav fra opslaget ordret, dokumentation og status)
ROWS = [
    ('Yde teknisk support og installationshjælp i forbindelse med varmepumper',
     'Delvist dokumenteret. Teknisk support og fejlfinding på el-, ventilations- og klimaanlæg hos ELOHVAC og Data Power, og på pumper og HVAC hos Biofos. '
     'Varmepumper er ikke dokumenteret i min erfaring.'),
    ('Beregne og vurdere varmepumpeinstallationer',
     'Varmepumpeberegning mangler i min dokumentation. Tilbud og beregning, tidsplaner og materialeberegning hos ELOHVAC gælder el- og ventilationsanlæg. '
     'Varmepumpeberegning og -dimensionering er ikke i min erfaring.'),
    ('Understøtte salgsorganisationen med teknisk salgssupport',
     'Delvist dokumenteret. Tilbud, beregning og aftalegrundlag hos ELOHVAC og Ventek-Air. Teknisk salgssupport til en salgsorganisation er ikke dokumenteret.'),
    ('Yde teknisk support til produktmanagement',
     'Delvist dokumenteret. Produkt- og porteføljeansvar for en produktionslinje med elektromotorer, pumper og dykpumper hos ARJ, herunder roadmap, udvikling og lancering. '
     'Det er ikke varmepumper.'),
    ('Være ansvarlig for dialog og samarbejde med vores installationspartnere',
     'Delvist dokumenteret. Samarbejde med underentreprenører og leverandører hos Ventek-Air og ELOHVAC, og leverandørdialog hos Novo Nordisk. '
     'Installationspartnere i VVS- eller varmebranchen er ikke dokumenteret.'),
    ('Udarbejde teknisk dokumentation og installationsmateriale til installationspartnerne',
     'Delvist dokumenteret. Afleveringsdokumentation, afleveringspakker og procedurer under GMP, FDA og EMA hos Novo Nordisk og Ventek-Air. '
     'Installationsmateriale til eksterne partnere er ikke dokumenteret.'),
    ('Håndtere kundeklager og reklamationssager vedrørende varmepumpeinstallationer',
     'Reklamationer på varmepumper er ikke i min erfaring. Reklamations- og garantiansvar er bekræftet generelt på tværs af mine stillinger, '
     'og rodårsagsanalyse med A3, 5 Hvorfor og Ishikawa er dokumenteret. Varmepumpesager er ikke i min erfaring.'),
    ('Bidrage til håndtering af ankeklagesager',
     'Ankeklagesager er ikke i min erfaring. Kundeklager og reklamationer med rodårsagsanalyse er dokumenteret generelt, og den erfaring kan bruges, når en klage skal gennemgås. '
     'Jeg har ikke håndteret en ankesag.'),
    ('En teknisk baggrund, og trives med at bruge sin faglighed, rådgive andre og finde løsninger',
     'Dokumenteret. Teknisk uddannelse som B.Tech (EQF6) og elautoriseret maskinmester (LV/MV/HV), og rådgivning og fejlfinding i drift, service og projekter.'),
    ('Arbejder selvstændigt, tager ansvar for sine opgaver og kan bevare overblikket, når mange opgaver er i gang',
     'Dokumenteret. Porteføljer med 11 og 37 samtidige projekter, daglige tavlemøder og flaskehalsanalyser, og selvstændigt ansvar for ELOHVAC og Data Power.'),
    ('Erfaring med beregning og vurdering af varmepumpeinstallationer',
     'Tilbud og beregning, tidsplaner og materialeberegning hos ELOHVAC gælder el-, ventilations- og klimaanlæg. '
     'Beregning og vurdering af varmepumpeinstallationer er ikke dokumenteret.'),
    ('Teknisk forståelse for installationer og varmepumpeløsninger',
     'Delvist dokumenteret. Teknisk forståelse for installationer: tavler, styring, ventilation, klimaanlæg og pumper. Varmepumpeløsninger er ikke dokumenteret.'),
    ('Erfaring med eller kendskab til håndtering af reklamations- og klagesager inden for varmepumpeinstallationer',
     'Min erfaring med sager omfatter ikke varmepumper. Generel reklamationshåndtering og rodårsagsanalyse er dokumenteret.'),
    ('Erfaring med teknisk support og salgssupport',
     'Delvist dokumenteret. Fejlfinding i døgndrift hos Biofos og ELOHVAC, og rådgivning om drift, service og projekter. '
     'Teknisk support til en salgsorganisation er ikke dokumenteret.'),
    ('Evnen til at understøtte produktmanagement med teknisk sparring',
     'Delvist dokumenteret. Roadmap, udvikling og lancering i ARJ-produktporteføljen, og AI-værktøjer til produktanalyse og KPI i Data Power. '
     'Produktmanagement for varmepumper er ikke dokumenteret.'),
    ('Gode kommunikationsevner og evnen til at formidle teknisk viden på en forståelig måde',
     'Dokumenteret. Månedsrapportering til ledelse og bygherre hos Novo Nordisk, beslutningsoplæg og ledelsesrapportering i Data Power, og dansk og engelsk i skrift og tale.'),
    ('Fordel: branche relevant uddannelse, eksempelvis VVS\'er, VVS-installatør, VE-uddannet eller maskinmester',
     'Delvist dokumenteret. Maskinmester: elautoriseret maskinmester (LV/MV/HV), Sikkerhedsstyrelsen, maj 2023. VVS-installatøruddannelse og VE-uddannelse har jeg ikke.'),
]

KULTUR_PHRASES = [
    'Vi er forskellige som mennesker, men behandler hinanden med ligeværd og respekt',
    'dialog, hjælpsomhed og en flad struktur',
    'finder løsninger sammen',
    'en afdeling i udvikling',
    'sammenhold og relationer, der bunder i tillid',
    'engagerer sig i den grønne omstilling',
    'formålsdrevet',
    'hverdagen ikke er ens, og hvor der til tider er fart på',
]


def write_inputs():
    with open(KRAV, 'w', encoding='utf-8') as f:
        f.write('# Krav fra Andel Energi · Teknisk Specialist, Teknik & Service (Svinninge), dansk, ordret fra opslaget\n')
        for krav, _ in ROWS:
            f.write(krav + '\n')
    with open(KULTUR, 'w', encoding='utf-8') as f:
        f.write('# Arbejdsgiverens egne udtryk fra opslaget (dansk, ordret). Skal genfindes ordret i dokumentet.\n')
        for phrase in KULTUR_PHRASES:
            f.write(phrase + '\n')


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER, 'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo')
    m.meta('28. november 2026')
    m.meta('Andel Energi · Svinninge · ansøgning via annoncen')
    m.para('Kære Niels Bigum,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    def sub(text):
        p = m._p(spacing_after=20, spacing_before=60, line=260, justify=False, keep_next=True)
        m._run(p, text, bold=True, color='002B5C')
        return p

    # ------------------------------------------------------------ brev, side 1
    lp('Andel Energi vil udskifte endnu flere gas- og oliefyr til varmepumper frem mod 2027. Opslaget beskriver en afdeling i udvikling, '
       'hvor man engagerer sig i den grønne omstilling på en formålsdrevet måde. Det kræver, at installationerne '
       'holder, at installatørerne får svar, når de har brug for dem, og at reklamationer bliver forklaret rigtigt første gang. '
       'Stillingen som teknisk specialist i Teknik & Service er placeret, hvor de tre hænger sammen. Den opgave ser jeg i stillingen.')

    sub('Installationen er der, hvor kvaliteten afgøres')
    lp('Opslaget siger: "Vi er forskellige som mennesker, men behandler hinanden med ligeværd og respekt." En varmepumpe, der er dimensioneret forkert, giver en klage, længe før den giver en besparelse. Beregningen af '
       'installationen skal derfor være gennemsigtig for installatøren, så det er tydeligt, hvilke forudsætninger der ligger bag. '
       'Jeg har beregnet og vurderet el-, ventilations- og klimaanlæg, og den metode vil jeg bruge på varmepumper. '
       'Det er en ny teknologi for mig, og det første, jeg vil gøre, er at lære de beregningsforudsætninger, afdelingen allerede bruger.')

    sub('Support, der kan bruges ude hos installatøren')
    lp('Installationspartnerne har brug for korte og præcise svar, og dialog, hjælpsomhed og en flad struktur gør det hurtigere at få dem. Teknisk dokumentation skal kunne bruges uden at ringe '
       'tilbage. Teknisk dokumentation og installationsmateriale skal være skrevet, så den, der står på taget eller i kælderen, '
       'kan følge den. Det kræver en fast skabelon, og den vil jeg lave sammen med salgs- og produktmanagementkollegerne.')

    sub('Reklamation og klage med en rodårsag')
    lp('Når en kunde klager, skal sagen have en årsag, der kan slås fast, før der vælges en løsning. Sagen løses, når vi finder løsninger sammen med dem, der har den. Jeg bruger A3, 5 Hvorfor og '
       'Ishikawa til det. Reklamationer på varmepumper er en ny sagstype for mig, og jeg vil bygge sagsgangen op sammen med dem, der '
       'allerede behandler klager og ankesager i afdelingen.')

    sub('Bro mellem salg, produkt og installatør')
    lp('Produktmanagement og salg kender produktet, men installatøren ser det i det hus, det skal monteres i. Den tekniske specialist er '
       'bindeleddet, der oversætter fra det ene til det andet. Den rolle ser jeg som kernen i stillingen.')

    sub('Det, der er nyt for mig')
    lp('Varmepumper, beregning og dimensionering af varmepumpeinstallationer, reklamation og ankesager på varmepumper er ikke en '
       'del af min dokumenterede erfaring. Mit grundlag er el-, ventilations- og klimaanlæg, drift og service i døgnbemanding, og '
       'projekter med udbud og dokumentation. Jeg har ingen VVS-installatøruddannelse og ingen VE-uddannelse.')

    lp('Opslaget beskriver sammenhold og relationer, der bunder i tillid, og at hverdagen ikke er ens, og hvor der til tider er fart på. '
       'Jeg vil gerne tale om, hvilke reklamationssager der fylder mest i dag, og hvilke installationsspørgsmål '
       'installatørerne stiller oftest.', after=44)
    lp('Med venlig hilsen', after=8)
    lp('Shahram Ajloo', after=8)

    # ------------------------------------------------------------ CV, side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Elautoriseret maskinmester (LV/MV/HV) med teknisk support, beregning og fejlfinding på el-, ventilations- og klimaanlæg. '
           'Fejlfinding og forebyggende vedligehold i døgndrift på pumper, HVAC og højspændingstavler hos Biofos. Erfaring med '
           'dokumentation, afleveringspakker og udbud. Ingen varmepumpeerfaring er dokumenteret. Dansk og engelsk. Kørekort B.', after=32)

    m.section('TEKNISK SUPPORT OG INSTALLATION')
    tasks = [
        ('Support og fejlfinding',
         'Installation, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg hos ELOHVAC og Data Power.'),
        ('Beregning og tilbud',
         'Tilbud og beregning, tidsplaner og materialestyring for el- og ventilationsanlæg hos ELOHVAC. Akkord og opmåling.'),
        ('Drift i døgnbemanding',
         'Drift og vedligehold af pumper, HVAC, højspændingstavler og SCADA i 24/7 drift hos Biofos, 2017 til 2022.'),
        ('Rodårsag',
         'Rodårsagsanalyse med A3, 5 Hvorfor og Ishikawa. Fejldiagnose og reparation af industrielle anlæg hos ARJ.'),
    ]
    for head, body in tasks:
        m.bullet(head, body, after=24)

    m.section('DOKUMENTATION, PRODUKT OG SAMARBEJDE')
    tasks = [
        ('Dokumentation',
         'Afleveringsdokumentation og procedurer under GMP, FDA og EMA hos Novo Nordisk. Udbud, tilbud og afleveringspakker hos Ventek-Air.'),
        ('Produkt og portefølje',
         'Produkt- og porteføljeansvar hos ARJ, herunder roadmap, udvikling og lancering. AI-værktøjer til KPI-analyse i Data Power.'),
        ('Installationspartnere',
         'Samarbejde med underentreprenører og leverandører hos Ventek-Air og ELOHVAC. Leverandørdialog hos Novo Nordisk.'),
    ]
    for head, body in tasks:
        m.bullet(head, body, after=24)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester, ansvarlig for el-teknik og ventilation',
         'Data Power Consultant ApS · København · 2024 til i dag',
         [('', 'Ansvarlig for AI- og AI coding-afdelingen med 4 til 10 personer. Tekniske og industrielle applikationer fra kravafdækning til overdragelse.'),
          ('', 'El-teknik og ventilation med fuldt P&L-ansvar. Fra november 2026 også de el-tekniske aktiviteter fra ELOHVAC.')]),
        ('Ejer og teknisk direktør, elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 til november 2026 (virksomheden lukket)',
         [('', 'Installation, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg, fra akutte udkald til afleverede anlæg.'),
          ('', 'Tilbud og beregning, tidsplaner, materialestyring og underentreprenører. Akkord og opmåling.')]),
        ('Senior idriftsættelsesingeniør og projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg og Bagsværd · november 2022 til juli 2024',
         [('', 'FAT, SAT og IQ/OQ/PQ under GMP, FDA og EMA, med nul kritiske afvigelser ved aflevering.'),
          ('', '37 samtidige anlægs- og CAPEX-projekter, med SAP ERP til økonomi og omkostninger.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · januar 2022 til november 2022',
         [('', '11 samtidige anlægsprojekter fra specifikation til formel aflevering, med et 14-mands team.'),
          ('', 'Udbud, tilbud, underentreprenører og afleveringspakker.')]),
        ('Vedligeholdelses- og driftsleder, værkstedstekniker',
         'Biofos (Lynetten) · København · august 2017 til januar 2022',
         [('', 'Drift og vedligehold af pumper, HVAC, højspændingstavler og SCADA i døgndrift.'),
          ('', 'Ledelse af driftsteam i skiftehold på ledelsesniveau.')]),
        ('Elektromekaniker og produktionsteamleder',
         'ARJ Engineering · Teheran · december 2003 til marts 2010',
         [('', 'Fejldiagnose og reparation af industrielle el- og mekaniske anlæg med rodårsagsanalyse.'),
          ('', 'Produkt- og porteføljeansvar for en produktionslinje med elektromotorer, pumper og dykpumper.')]),
    ]
    for title, meta, bullets in jobs:
        m.job(title, meta)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('UDDANNELSE OG CERTIFICERINGER')
    m.edu('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('B.Tech (EQF6), teknologiledelse og maskinteknik',
          'Copenhagen School of Marine Engineering & Technology Management · 2017 til 2022')
    m.edu('Køleteknik og klimaanlæg (AMU)', 'Mercantec · 2021')
    m.edu('PRINCE2, certificeret', 'AXELOS / PeopleCert')
    m.para('Lean og Six Sigma anvendt i praksis, ikke certificeret: DMAIC, 5S, PDCA, VSM, A3, Kaizen, SMED, TPM, '
           '5 Hvorfor, Ishikawa og FMEA.', after=48)

    m.section('KOMPETENCER')
    m.models_table('Værktøjer og systemer', ('Område', 'Værktøjer'), [
        ('Teknik', 'Beregning og tilbud for el- og ventilationsanlæg, tavler, styring, CTS/BMS, KNX, pumper og HVAC'),
        ('Support og service', 'Fejlfinding, forebyggende vedligehold, CMMS, reservedele, MTBF, MTTR, OEE'),
        ('Dokumentation og kvalitet', 'Afleveringspakker, procedurer, ISO 9001, audits, afvigelser, rodårsagsanalyse'),
        ('Digitale værktøjer', 'SAP ERP, Microsoft Office, Excel, Python, Claude API'),
    ], widths=(3400, 6946), compact=True)
    m.para('Dansk og engelsk i skrift og tale, engelsk som arbejdssprog siden 2017. Persisk modersmål. Kørekort B.', after=40)

    # ------------------------------------------------------------ kravmatrix, side 4
    m.page_break()
    m.section('KRAVMATRIX')
    m.models_table('Opslagets krav og min dokumentation', ('Krav', 'Dokumentation og status'),
                   ROWS, widths=(3600, 6746), compact=True)

    m.save(path, title='Teknisk Specialist, Teknik & Service - Andel Energi',
           subject='Ansøgning Teknisk Specialist, Teknik & Service')
    print(path)


if __name__ == '__main__':
    os.makedirs(OUT_DIR, exist_ok=True)
    write_inputs()
    build(OUT)
