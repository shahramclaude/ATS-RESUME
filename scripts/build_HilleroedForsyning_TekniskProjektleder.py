# -*- coding: utf-8 -*-
"""Hillerød Forsyning · Teknisk projektleder, Energi, Plan & Projekt, Produktion (Hillerød).

Dansk opslag -> dansk dokument. Masterdesign (scripts/master_design.py): brev side 1, CV side 2-3,
kravmatrix side 4. Kun fakta fra master-CV'et og brugerbekræftelser.
Ikke dokumenteret og derfor ikke skrevet som erfaring: overskudsvarme, slamforbrænding, elkedler,
varmeakkumulering, varmepumper og ATES som projekter; feasibility studies; fjernvarmeselskab;
varmeerfaring med kedler og damp uden arbejdsgiver (ikke tilskrevet).
Research: research/HilleroedForsyning_TekniskProjektleder_2026-11.md
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
OUT_DIR = os.path.join(ROOT, 'output')
OUT = os.path.join(OUT_DIR, 'Shahram_Ajloo_HilleroedForsyning_TekniskProjektleder.docx')
KRAV = os.path.join(ROOT, 'jd', 'HilleroedForsyning_TekniskProjektleder_krav.txt')
KULTUR = os.path.join(ROOT, 'jd', 'HilleroedForsyning_TekniskProjektleder_kultur.txt')

NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Teknisk projektleder, energi- og produktionsprojekter · Hillerød Forsyning'
BANNER_RESUME = 'Tekniske anlægsprojekter fra beregning til drift'

# (krav fra opslaget, dokumentation og status)
ROWS = [
    ('Drive og lede tekniske energi- og produktionsprojekter fra idé til realisering',
     'Dokumenteret fra specifikation til aflevering. Hos Ventek-Air ledte jeg 11 parallelle anlægsprojekter fra specifikation til formel aflevering, '
     'og hos Novo Nordisk 37 samtidige anlægs- og CAPEX-projekter. Idé- og feasibility-fasen er ikke dokumenteret.'),
    ('Sikre fremdrift og styre økonomi, tidsplan, kvalitet og risici',
     'Dokumenteret. Hos Novo Nordisk fremdrift, økonomi, risici og ressourcer i anlægsprojekterne, med månedsrapportering til ledelse og bygherre. '
     'Hos ELOHVAC tidsplaner, tilbud og fuldt P&L-ansvar. FAT, SAT og IQ/OQ/PQ med nul kritiske afvigelser ved aflevering.'),
    ('Koordinere interne og eksterne projektdeltagere',
     'Dokumenteret. Tværfaglig koordinering af 25 specialister hos Novo Nordisk på tværs af engineering, indkøb og anlæg. '
     'Daglig koordinering af et 14-mands team og underentreprenører hos Ventek-Air.'),
    ('Gennemføre feasibility studies, udbud og kontraktstyring',
     'Delvist dokumenteret. Udbud og tilbud, underentreprenører, aftalegrundlag og afleveringspakker hos Ventek-Air. '
     'Feasibility studies er ikke dokumenteret i min erfaring.'),
    ('Kvalitetssikre tekniske løsninger og udfordre rådgivere på design og dimensionering',
     'Proposed for rådgiverdialogen. Beregning, dimensionering og designvarianter af tekniske anlæg valideres med faglig kontrol før noget går videre, '
     'som i Data Power. Rådgiverstyring som rolle er ikke dokumenteret.'),
    ('Sikre tæt involvering af driften og fokus på drift, vedligehold og funktionalitet',
     'Dokumenteret. Drift og vedligehold af pumper, HVAC, højspændingstavler og SCADA i døgndrift hos Biofos fra 2017 til 2022, og ledelse af et driftsteam i skiftehold. '
     'Den erfaring gør driftens krav til en del af projektets grundlag fra start.'),
    ('Har en relevant teknisk uddannelse, fx ingeniør, maskinmester eller tilsvarende',
     'Dokumenteret. B.Tech (EQF6) i teknologiledelse og maskinteknik, 2017 til 2022, og elautorisation som maskinmester (LV/MV/HV) fra Sikkerhedsstyrelsen, maj 2023. '
     'B.Tech er uddannelsen i teknologiledelse og maskinteknik, og maskinmester-autorisationen er erhvervet oven på den.'),
    ('Har erfaring med projektledelse af tekniske anlægsprojekter',
     'Dokumenteret. Projektledelse af tekniske anlægsprojekter hos Novo Nordisk, Ventek-Air og ELOHVAC. PRINCE2-certificeret projektleder. '
     'Microsoft Project bruges som fast planlægningsværktøj.'),
    ('Har arbejdet med udbud, rådgiverstyring og leverandørstyring',
     'Dokumenteret for udbud, tilbud og leverandørstyring hos Ventek-Air og Novo Nordisk (indkøb). Rådgiverstyring er ikke dokumenteret som selvstændig rolle, '
     'men engineering-koordinering hos Novo Nordisk ligger tæt på den opgave.'),
    ('Kan skabe struktur, fremdrift og motivation i dit projektteams samarbejde',
     'Dokumenteret. Daglige tavlemøder og flaskehalsanalyser hos Ventek-Air, faste mødestrukturer og én samlet plan i Data Power og ELOHVAC. '
     'Lærlinge og elektrikere har fået struktureret oplæring og MUS.'),
    ('Kan holde overblik over udbud, kontrakter og budgetter',
     'Dokumenteret. Budgetter og økonomi i anlægsprojekter hos Novo Nordisk, hvor økonomien styres i SAP ERP. Udbud og kontrakter hos Ventek-Air. '
     'Tilbud og P&L i ELOHVAC og Data Power.'),
    ('Bruger din tekniske indsigt til at udfordre løsninger, når det er nødvendigt',
     'Dokumenteret i metoden. Rodårsagsanalyse med A3, 5 Hvorfor og Ishikawa hos Novo Nordisk og fejldiagnose med korrigerende handlinger hos ARJ. '
     'Løsningerne udfordres med data før beslutning.'),
    ('Tager proaktivt ansvar for projektets samlede fremdrift',
     'Dokumenteret. Fuldt P&L-ansvar for el- og ventilationsopgaver i ELOHVAC og Data Power, og ansvar for fremdriften i 11 parallelle projekter hos Ventek-Air. '
     'Ansvar for hele projektforløbet, fra tilbud til aflevering.'),
    ('Trives i spændingsfeltet mellem teknik og projektledelse',
     'Dokumenteret i karrieren. Teknisk arbejde fra montage, test og fejlfinding til projektledelse, P&L og udbud, i både entreprise og anlægsdrift. '
     'Det er mit faglige udgangspunkt.'),
    ('Er loyal og møder dine kolleger med åbenhed og nysgerrighed',
     'Ikke dokumenteret som erfaring i CV\'et. Samarbejdsformen kan vurderes i en samtale, og den er beskrevet konkret med tavlemøder, sparring og oplæring.'),
    ('Har lyst til tværfagligt samarbejde, til at hjælpe andre og til at være med til at skabe en arbejdsplads, hvor man trives sammen',
     'Dokumenteret i samarbejdet. Tværfaglig koordinering af 25 specialister hos Novo Nordisk, personaleledelse af 5 elektrikere og 3 lærlinge, '
     'og daglig sparring med driftsteams i skiftehold hos Biofos.'),
    ('Arbejder med energiprojekter som overskudsvarme, slamforbrænding, elkedler, varmeakkumulering og varmepumper',
     'Ikke dokumenteret. Ingen projekter med overskudsvarme, slamforbrænding, elkedler, varmeakkumulering eller varmepumper i min erfaring. '
     'Det nærmeste er el- og ventilationsanlæg i ELOHVAC og drift af pumper og HVAC hos Biofos.'),
]

KULTUR_PHRASES = [
    'fra de første beregninger til de står færdige',
    'fra idé og feasibility study til udførelse og overdragelse til drift',
    'tæt involvering af driften',
    'udfordre rådgivere på design og dimensionering',
    'bæredygtig og effektiv varmeforsyning',
    'Vidensdeling, sparring og samarbejde',
    'tværfagligt samarbejde',
    'Forsyningsbranchen er i en rivende udvikling',
]


def write_inputs():
    with open(KRAV, 'w', encoding='utf-8') as f:
        f.write('# Krav fra Hillerød Forsyning · Teknisk projektleder, Energi, Plan & Projekt, Produktion (Hillerød), dansk, ordret fra opslaget\n')
        for krav, _ in ROWS:
            f.write(krav + '\n')
    with open(KULTUR, 'w', encoding='utf-8') as f:
        f.write('# Arbejdsgiverens egne udtryk fra opslaget (dansk, ordret). Skal genfindes ordret i dokumentet.\n')
        for phrase in KULTUR_PHRASES:
            f.write(phrase + '\n')


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo')
    m.meta('28. november 2026')
    m.meta('Hillerød Forsyning · afdelingen Energi, Plan & Projekt, Produktion')
    m.para('Kære Alexander Nielsen,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    def sub(text):
        p = m._p(spacing_after=20, spacing_before=60, line=260, justify=False, keep_next=True)
        m._run(p, text, bold=True, color='002B5C')
        return p

    # ------------------------------------------------------------ brev, side 1
    lp('Hillerød Forsyning skal levere grøn varme til hele Hillerød, og det sker i et system, hvor elnettet '
       'endnu ikke kan levere strøm til hele elkedlen i HKV. Forsyningen har beskrevet, at ombygningen af HKV '
       'til energicentral skal give fjernvarme fra elkedel, varmepumper og et ATES-anlæg. Det er en opgave, hvor '
       'projektlederen skal holde den grønne omstilling og elnettets tidsplan sammen. Projekterne går '
       'fra de første beregninger til de står færdige, og det er den rækkefølge, jeg vil tage udgangspunkt i, så borgere og virksomheder får en '
       'bæredygtig og effektiv varmeforsyning.')

    sub('Feasibility med elnettet med i beregningen')
    lp('Et projekt, der går fra idé og feasibility study til udførelse og overdragelse til drift, skal have et svar på elnettet tidligt. '
       'En feasibility study for overskudsvarme, slamforbrænding eller varmeakkumulering står og falder med, '
       'hvornår der er strøm nok, og hvad varmen koster i den periode. Jeg vil bygge studiet op med scenarier '
       'for elnettets kapacitet og varmeprisen, og den besvarelse skal ligge klar, før udbudsgrundlaget skrives. '
       'Budget og tidsplan følger de samme scenarier, og rådgivere og leverandører får én samlet tidsplan. '
       'Så ved beslutningen, hvilken del af projektet der kan køre først.')

    sub('Driften i designfasen')
    lp('Stillingen lægger vægt på tæt involvering af driften og fokus på drift, vedligehold og funktionalitet. Det bliver '
       'konkret, når driftens krav står i designgrundlaget fra start: adgang, tilsyn, reservedele og alarmer. '
       'Samme krav skal følge med ind i udbud og overdragelse, så anlægget kan drives, når det står færdigt.')

    sub('Rådgivere og design')
    lp('Stillingen indebærer at udfordre rådgivere på design og dimensionering. Det kræver tværfagligt samarbejde, og at beregninger '
       'kontrolleres af en, der ikke har lavet dem, med faste kontrolpunkter og dokumentation. Det er den '
       'metode, jeg vil bruge sammen med rådgiverne, så projektet har en kvalitetssikring, der kan følges.')

    sub('Første 90 dage')
    lp('De første 30 dage bruges på porteføljen af projekter sammen med Alexander Nielsen og teamet, og slutter '
       'med en samlet liste over projekter, økonomi og elnetsforudsætninger. Vidensdeling, sparring og samarbejde med driften starter allerede i den første måned. Dag 31 til 60 går til det første projekt '
       'med feasibility og et beslutningsoplæg til ledelsen. Dag 61 til 90 går til udbudsgrundlag og en fast '
       'kontraktstyring med tidsplan og risikoliste, der kan opdateres hver måned.')

    sub('Det, der er nyt for mig')
    lp('Overskudsvarme, slamforbrænding, elkedler, varmeakkumulering og varmepumper er nye projekttyper for mig. '
       'Jeg har arbejdet med el- og ventilationsanlæg og med drift af pumper og HVAC i døgndrift, og det er det '
       'grundlag, jeg tager med. Fjernvarmens økonomi og elmarkedet skal jeg lære i praksis sammen med jer.')

    lp('Opslaget nævner hjemmearbejde og fleksible arbejdstider, og den rammeaftale tager jeg gerne op i samtalen. '
       'Forsyningsbranchen er i en rivende udvikling, og Hillerød Forsyning har flere projekter i gang. Jeg vil '
       'gerne høre, hvilket projekt der skal have første prioritet i den nye periode, og hvilke data der mangler, før '
       'beslutningen kan træffes.', after=44)
    lp('Med venlig hilsen', after=8)
    lp('Shahram Ajloo', after=8)

    # ------------------------------------------------------------ CV, side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Teknisk projektleder med elautorisation som maskinmester (LV/MV/HV). Tekniske anlægsprojekter styret '
           'fra specifikation til aflevering: 37 samtidige CAPEX-projekter hos Novo Nordisk og 11 parallelle projekter hos Ventek-Air. '
           'Drift og vedligehold af pumper, HVAC og højspændingstavler i døgndrift hos Biofos. Udbud, tilbud og kontraktstyring, '
           'budgetter og P&L. PRINCE2-certificeret. Dansk og engelsk.', after=32)

    m.section('PROJEKTLEDELSE OG STYRING')
    tasks = [
        ('Fremdrift, økonomi og risici',
         'Tidsplaner, økonomi, risici og ressourcer i 37 samtidige CAPEX-projekter hos Novo Nordisk, med månedsrapportering til ledelse og bygherre.'),
        ('Udbud og kontraktstyring',
         'Udbud og tilbud, underentreprenører, aftalegrundlag, sikkerhedsdokumentation og afleveringspakker hos Ventek-Air og ELOHVAC.'),
        ('Koordinering',
         'Tværfaglig koordinering af 25 specialister på tværs af engineering, indkøb og anlæg. Daglige tavlemøder og flaskehalsanalyser hos Ventek-Air.'),
        ('Beregning og kvalitetssikring',
         'AI coding til beregning, dimensionering og designvarianter af tekniske anlæg, valideret med faglig kontrol før kundens godkendelse, hos Data Power.'),
        ('Økonomi',
         'Budgetter i SAP ERP hos Novo Nordisk, tilbud og tidsplaner med KS-tjeklister hos ELOHVAC, og KPI-dashboards i Python og Excel.'),
    ]
    for head, body in tasks:
        m.bullet(head, body, after=24)

    m.section('DRIFT, VEDLIGEHOLD OG ANLÆG')
    tasks = [
        ('Døgndrift',
         'Drift og vedligehold af pumper, HVAC, højspændingstavler og SCADA i døgndrift hos Biofos, 2017 til 2022. Forebyggende vedligehold og akut fejlfinding.'),
        ('Ledelse i skiftehold',
         'Ledelse af driftsteam i skiftehold på ledelsesniveau og teamledelse på øvrige niveauer i døgnbemanding.'),
        ('Montage, test og idriftsættelse',
         'FAT, SAT og IQ/OQ/PQ under GMP, FDA og EMA hos Novo Nordisk, med nul kritiske afvigelser ved aflevering. Idriftsættelse af tanke, procesrør og instrumentering.'),
        ('Forbedring',
         'PDCA-program med 40 % lavere energiomkostninger hos Novo Nordisk. 5S, Standard Work og PDCA på værksted og lager hos Biofos.'),
    ]
    for head, body in tasks:
        m.bullet(head, body, after=24)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester, ansvarlig for el-teknik og ventilation',
         'Data Power Consultant ApS · København · 2024 til i dag · kandidatens eneste ansættelse',
         [('', 'Ansvarlig for AI- og AI coding-afdelingen med 4 til 10 personer. Kundeløsninger med LLM-API\'er og AI-agenter samt '
               'tekniske og industrielle applikationer, fra kravafdækning og arkitektur til idriftsættelse og overdragelse.'),
          ('', 'AI coding til beregning, dimensionering og designvarianter af tekniske anlæg, valideret med faglig kontrol.'),
          ('', 'El-teknik og ventilation med fuldt P&L-ansvar, herunder akkord og opmåling. Fra november 2026 også de el-tekniske '
               'aktiviteter fra ELOHVAC.'),
          ('', 'Personaleledelse af 5 elektrikere og 3 lærlinge. Matrixledelse af to sideløbende organisationer, med én samlet plan og skriftlige aftaler.')]),
        ('Ejer og teknisk direktør, elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 til november 2026 (virksomheden lukket)',
         [('', 'Installation, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg, fra akutte udkald til afleverede anlæg.'),
          ('', 'Tilbud og beregning, tidsplaner, materialestyring og underentreprenører. KS og afleveringsdokumentation.'),
          ('', 'Akkord og opmåling: akkordbreve, opmåling af udført arbejde og regulering af mer- og mindrearbejde.')]),
        ('Senior idriftsættelsesingeniør og projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg og Bagsværd · november 2022 til juli 2024',
         [('', 'FAT, SAT og IQ/OQ/PQ under GMP, FDA og EMA, med nul kritiske afvigelser ved aflevering.'),
          ('', 'Tværfaglig koordinering af 25 specialister og 37 samtidige anlægsprojekter, med månedsrapportering til ledelse og bygherre.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · januar 2022 til november 2022',
         [('', '11 samtidige anlægsprojekter fra specifikation til formel aflevering, med et 14-mands team.'),
          ('', 'Udbud, underentreprenører, sikkerhedsdokumentation og afleveringspakker.')]),
        ('Vedligeholdelses- og driftsleder, værkstedstekniker',
         'Biofos (Lynetten) · København · august 2017 til januar 2022',
         [('', 'Drift og vedligehold af pumper, HVAC, højspændingstavler og SCADA i døgndrift på spildevandsrensningen.'),
          ('', 'Ledelse af driftsteam i skiftehold på ledelsesniveau og teamledelse på øvrige niveauer i døgnbemanding.'),
          ('', 'Skifteholdsdrift under LOTO, risikovurdering, APV og registrering af nærved-hændelser.')]),
        ('Elektromekaniker og produktionsteamleder',
         'ARJ Engineering · Teheran · december 2003 til marts 2010',
         [('', 'Ledelse af 12 mekanikere og teknikere i værkstedet: vagtplanlægning, materialer og mål.'),
          ('', 'Fejldiagnose og reparation af industrielle el- og mekaniske anlæg med rodårsagsanalyse.'),
          ('', 'Produkt- og porteføljeansvar for en produktionslinje med elektromotorer, pumper og dykpumper, på tværs af produktets '
               'livscyklus: roadmap, udvikling og lancering samt pris- og investeringsbeslutninger.')]),
    ]
    for title, meta, bullets in jobs:
        m.job(title, meta)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('UDDANNELSE OG CERTIFICERINGER')
    m.edu('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('B.Tech (EQF6), teknologiledelse og maskinteknik',
          'Copenhagen School of Marine Engineering & Technology Management · 2017 til 2022')
    m.edu('El- og maskinteknisk design, elteknik (EQF6)', 'Tehran Technical University · 2000 til 2003')
    m.edu('Køleteknik og klimaanlæg (AMU)', 'Mercantec · 2021')
    m.edu('PRINCE2, certificeret', 'AXELOS / PeopleCert')
    m.para('Lean og Six Sigma anvendt i praksis, ikke certificeret: DMAIC, 5S, PDCA, VSM, A3, Kaizen, SMED, TPM, '
           '5 Hvorfor, Ishikawa og FMEA.', after=48)

    m.section('KOMPETENCER')
    m.models_table('Værktøjer og systemer', ('Område', 'Værktøjer'), [
        ('Projekt og styring', 'PRINCE2, Microsoft Project, RACI, udbud, tilbud, KS, afleveringspakker'),
        ('Drift og vedligehold', 'Forebyggende vedligehold, CMMS, reservedele, MTBF, MTTR, OEE, fejlfinding'),
        ('Styring og automation', 'SCADA, styretavler, CTS/BMS, KNX'),
        ('Økonomi og data', 'SAP ERP, Excel, Python, Claude API'),
        ('Kvalitet', 'GMP, FDA, EMA, ISO 9001, audits, procedurer, afvigelser'),
        ('Forbedring', 'PDCA, 5S, Standard Work, A3, FMEA, 5 Hvorfor, Ishikawa'),
    ], widths=(3400, 6946), compact=True)
    m.para('Dansk og engelsk i skrift og tale, engelsk som arbejdssprog siden 2017. Persisk modersmål. Kørekort B med manuelt gear.', after=40)

    # ------------------------------------------------------------ kravmatrix, side 4
    m.page_break()
    m.section('KRAVMATRIX')
    m.models_table('Opslagets krav og min dokumentation', ('Krav', 'Dokumentation og status'),
                   ROWS, widths=(3600, 6746), compact=True)

    m.save(path, title='Teknisk projektleder, energi- og produktionsprojekter - Hillerød Forsyning',
           subject='Ansøgning Teknisk projektleder, Energi, Plan & Projekt, Produktion')
    print(path)


if __name__ == '__main__':
    os.makedirs(OUT_DIR, exist_ok=True)
    write_inputs()
    build(OUT)
