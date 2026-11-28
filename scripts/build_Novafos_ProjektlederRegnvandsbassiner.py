# -*- coding: utf-8 -*-
"""Novafos · Projektleder / Fagkoordinator til regnvandsbassiner (Birkerød).

Dansk opslag -> dansk dokument. Masterdesign (scripts/master_design.py): brev side 1, CV side 2-3,
kravmatrix side 4. Kun fakta fra master-CV'et og brugerbekræftelser.
Ikke dokumenteret og derfor ikke skrevet som erfaring: regnvandsbassiner (drift, oprensning,
renovering, design), tilladelsesforløb for bassiner, vandforsyning, landskab og planlægning som uddannelse.
Research: research/Novafos_ProjektlederRegnvandsbassiner_2026-11.md
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
OUT_DIR = os.path.join(ROOT, 'output')
OUT = os.path.join(OUT_DIR, 'Shahram_Ajloo_Novafos_ProjektlederRegnvandsbassiner.docx')
KRAV = os.path.join(ROOT, 'jd', 'Novafos_ProjektlederRegnvandsbassiner_krav.txt')
KULTUR = os.path.join(ROOT, 'jd', 'Novafos_ProjektlederRegnvandsbassiner_kultur.txt')

NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Projektleder / fagkoordinator til regnvandsbassiner · Novafos, Birkerød'
BANNER_RESUME = 'Planlægning, koordinering og drift af tekniske anlæg'

# (krav fra opslaget, dokumentation og status)
ROWS = [
    ('Erfaring med projektledelse, projektering eller koordinering af tekniske anlægsprojekter',
     'Dokumenteret. Hos Novo Nordisk styrede jeg fremdrift, økonomi, risici og ressourcer i 37 samtidige anlægs- og CAPEX-projekter '
     '(DKK 2 til 10 mio. pr. stk.) på tværs af engineering, indkøb og anlæg. Hos Ventek-Air ledte jeg 11 parallelle anlægsprojekter fra specifikation til formel aflevering.'),
    ('Trives med at skabe fremdrift og koordinere opgaver på tværs af mange interessenter',
     'Dokumenteret. Månedsrapportering til ledelse og bygherre hos Novo Nordisk, daglige tavlemøder og flaskehalsanalyser med et 14-mands team hos Ventek-Air, '
     'med underentreprenører i ELOHVAC og med kunder i Data Power.'),
    ('Arbejder struktureret og formår at holde overblikket, også når flere projekter kører samtidig',
     'Dokumenteret. Samtidige projekter hos Novo Nordisk og Ventek-Air styres med én samlet plan, faste mødestrukturer og et samlet overblik over flaskehalse. '
     'ELOHVAC og Data Power kørte side om side med fælles tid, prioritering og skriftlige aftaler om, hvad der går forud.'),
    ('Har interesse for tekniske løsninger, anlæg og forsyningsinfrastruktur',
     'Dokumenteret i drift. Pumper, HVAC, højspændingstavler og SCADA i døgndrift på spildevandsrensningen hos Biofos fra 2017 til 2022. '
     'Regnvandsbassiner er nyt for mig, og den viden skal jeg opbygge sammen med teamet.'),
    ('Kan omsætte tekniske problemstillinger til praktiske og holdbare løsninger',
     'Dokumenteret. Rodårsagsanalyse med A3, 5 Hvorfor og Ishikawa hos Novo Nordisk og fejldiagnose med korrigerende handlinger hos ARJ. '
     'Beregning, dimensionering og designvarianter af tekniske anlæg i AI-assisterede arbejdsgange hos Data Power, valideret før noget gik til kunden.'),
    ('Trives i en hverdag, der veksler mellem skrivebordet, mødelokalet og anlæggene ude i marken',
     'Dokumenteret. Mit arbejde har vekslet mellem kontor, møde og anlæg: tilbud, tidsplaner og materialestyring i ELOHVAC, '
     'og driftsmøder kombineret med døgndrift på renseanlægget hos Biofos.'),
    ('Har kørekort til personbil',
     'Dokumenteret. Kørekort B med manuelt gear, og bopæl i Måløv. Jeg kører gerne til Storkøbenhavn, Sjælland og trekantsområdet.'),
    ('Relevant teknisk baggrund som ingeniør, maskinmester, landskabsarkitekt, planlægger eller lignende',
     'Dokumenteret. B.Tech (EQF6) i teknologiledelse og maskinteknik, 2017 til 2022, og elautorisation som maskinmester (LV/MV/HV) fra Sikkerhedsstyrelsen, maj 2023. '
     'Ingen uddannelse som landskabsarkitekt eller planlægger.'),
    ('Erfaring fra forsyningsbranchen eller anden teknisk infrastruktur (fordel)',
     'Dokumenteret. Biofos (Lynetten), kommunalt ejet forsyning, 2017 til 2022, med døgndrift af pumper, HVAC, højspændingstavler og SCADA. '
     'Vandforsyning er ikke dokumenteret i min erfaring.'),
    ('Erfaring med renovering, vedligeholdelse eller optimering af tekniske anlæg (fordel)',
     'Dokumenteret. Forebyggende vedligehold og akut fejlfinding hos Biofos, service og fejlfinding på el-, ventilations- og klimaanlæg i ELOHVAC, '
     'og 40 % lavere energiomkostninger gennem et PDCA-program hos Novo Nordisk.'),
    ('Erfaring med regnvands-, spildevands- eller andre forsyningsanlæg (fordel)',
     'Delvist dokumenteret. Spildevand i døgndrift hos Biofos fra 2017 til 2022. Regnvandsbassiner, oprensning af bassiner og overløbsbygværker er ikke dokumenteret i min erfaring.'),
    ('Prioritere indsatser på Novafos\' mere end 350 regnvandsbassiner og bidrage til den langsigtede planlægning af området',
     'Proposed. Prioritering efter tilstand og konsekvens, opdateret i samme tabel som drift og planlægning. Den nærmeste prioritering er 37 CAPEX-projekter hos Novo Nordisk, '
     'ikke fra regnvandsbassiner.'),
    ('Planlægge og koordinere oprensnings- og renoveringsprojekter, herunder valg af løsninger og afklaring af nødvendige tilladelser',
     'Dokumenteret for planlægning og koordinering af projekter, ikke for bassinoprensning. Tilladelser til regnvandsbassiner er ikke dokumenteret. '
     'Første fase afklarer tilladelsesspor og myndighedskrav, før løsningen vælges.'),
    ('Skabe en konstruktiv og respektfuld dialog med myndighederne, så de bedste løsninger kan realiseres på det enkelte projekt',
     'Dokumenteret generelt. Direkte kontakt til myndigheder og indberetning i reguleret sammenhæng, uden navngivne myndigheder. '
     'Dialogen med en kommune om et konkret regnvandsbassin er ny for mig.'),
    ('Sparre med projektledere og specialister om design af nye regnvandsbassiner med fokus på funktion, drift og langsigtet værdi',
     'Proposed. Design af regnvandsbassiner er ikke dokumenteret. Design af tekniske anlæg hos Data Power og drift i døgndrift hos Biofos '
     'giver grundlag for at sparre om funktion og drift.'),
    ('Videreudvikle Novafos\' tekniske krav og standarder for regnvandsbassiner baseret på ny viden og praktiske erfaringer',
     'Proposed. Procedurer og dokumentation under GMP hos Novo Nordisk og standard work fra værkstedet hos Biofos kan bruges til at strukturere et kravgrundlag. '
     'Regnvandsbassiner har jeg ikke arbejdet med endnu.'),
    ('Deltage i udviklingsprojekter, der forbedrer fremtidens metoder til bassinrenovering og design af nye anlæg',
     'Proposed. PDCA-arbejdet hos Novo Nordisk og AI-værktøjer til beregning og KPI-analyse i ELOHVAC og Data Power viser, hvordan jeg arbejder med metodeudvikling. '
     'Bassinrenovering har jeg ikke udført.'),
    ('Samarbejde tæt med drift, planlægning, rådgivere, entreprenører og myndigheder om både eksisterende og kommende anlæg',
     'Dokumenteret. Samarbejde med driftsteams i skiftehold hos Biofos, underentreprenører og aftalegrundlag hos Ventek-Air og ELOHVAC, '
     'og månedlig rapportering til bygherre hos Novo Nordisk.'),
]

KULTUR_PHRASES = [
    'stærke kompetencer, data og metoder inden for regnvandsbassiner',
    'et solidt fagligt fundament',
    'tæt sparring',
    'konstruktiv og respektfuld dialog',
    'klimavenligt forsyningsselskab',
    'værdi for både samfund og miljø',
    'fleksible arbejdstider',
    'kurser, intern undervisning og uddannelse',
]


def write_inputs():
    with open(KRAV, 'w', encoding='utf-8') as f:
        f.write('# Krav fra Novafos · Projektleder / Fagkoordinator til regnvandsbassiner (Birkerød), dansk, ordret fra opslaget\n')
        for krav, _ in ROWS:
            f.write(krav.replace(' (fordel)', '') + '\n')
    with open(KULTUR, 'w', encoding='utf-8') as f:
        f.write('# Arbejdsgiverens egne udtryk fra opslaget (dansk, ordret). Skal genfindes ordret i dokumentet.\n')
        for phrase in KULTUR_PHRASES:
            f.write(phrase + '\n')


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo')
    m.meta('28. november 2026')
    m.meta('Novafos A/S · Birkerød · Team Anlæg Øst & Bassiner')
    m.para('Kære Novafos,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    def sub(text):
        p = m._p(spacing_after=20, spacing_before=60, line=260, justify=False, keep_next=True)
        m._run(p, text, bold=True, color='002B5C')
        return p

    # ------------------------------------------------------------ brev, side 1
    lp('Novafos har over 350 regnvandsbassiner, og de skal holde, når regnen kommer hårdere og oftere. '
       'Opgaven er derfor ikke at løse ét bassin ad gangen, men at vælge, hvilke bassiner der får hjælp først, '
       'og hvordan arbejdet gøres uden at stoppe det, der allerede virker. Novafos har gennem flere år opbygget '
       'stærke kompetencer, data og metoder inden for regnvandsbassiner, og projektlederen skal føre dem videre '
       'til konkrete projekter på hele porteføljen. Som klimavenligt forsyningsselskab skal Novafos kunne vise, at bassinerne skaber '
       'værdi for både samfund og miljø, og det kræver et solidt fagligt fundament i hvert projekt.')

    sub('Prioritering først')
    lp('En prioriteringsliste må ikke kun se på tilstanden. Den skal også vise, hvad der sker med oplandet, '
       'hvis et bassin svigter i en kraftig regnhændelse, og hvad en oprensning koster i forhold til en renovering. '
       'Jeg vil bygge listen som en fast tabel, som planlægning, drift og projektledere kan opdatere, '
       'så den følger med, når nye målinger kommer ind.')

    sub('Tilladelser før løsning')
    lp('Tilladelser bestemmer ofte tidsplanen mere end selve arbejdet. Jeg vil afklare tilladelsesspor og '
       'myndighedskrav i den første fase, før valget mellem oprensning, renovering og nyt bassin træffes. '
       'Dialogen med kommuner og myndigheder tager udgangspunkt i det faglige grundlag: hvad vi ved, hvad vi endnu ikke ved, '
       'og hvilke løsninger der kan realiseres på stedet. Opslaget beder om en konstruktiv og respektfuld dialog med myndighederne, '
       'og det er den dialog, jeg vil føre.')

    sub('Design, der kan drives')
    lp('Når et nyt bassin designes, skal funktion, drift og langsigtet værdi vurderes samlet. '
       'Det betyder, at driftsfolkene sidder med ved bordet fra start, og at der er tæt sparring med projektlederne '
       'og specialisterne om adgang, tømning og overløb. Samme spørgsmål skal stilles til de tekniske krav og standarder. '
       'Hvert afleveret projekt bør give et bidrag tilbage til kravene: hvad fungerede, hvad skal ændres, og hvilke data mangler.')

    sub('Første 90 dage')
    lp('De første 30 dage bruges på porteføljen sammen med drift og planlægning, og slutter med en første prioriteringsliste. '
       'Dag 31 til 60 går til de højest prioriterede bassiner, med tilladelser, data og valg af løsning. '
       'Dag 61 til 90 går til en fast projektpakke og et forslag til ændringer i de tekniske krav, som ledelsen kan godkende. '
       'Opslaget nævner fleksible arbejdstider og støtte til kurser, intern undervisning og uddannelse. '
       'Det er rammer, jeg vil have med i planen for teamets faglige udvikling.')

    sub('Det, der er nyt for mig')
    lp('Regnvandsbassiner er nyt for mig. Jeg har arbejdet med pumper, ventiler, rørsystemer og el- og styreanlæg '
       'i døgndrift, og fra spildevandsrensningen kender jeg kravene til drift og vedligehold. '
       'Bassinernes funktion, sedimenter og tilladelsesforhold skal jeg lære at kende sammen med teamet. '
       'Det er en del af den opgave, opslaget beskriver.')

    lp('Jeg vil gerne tale om, hvilke bassiner der skal først på listen, og hvilke data der mangler, '
       'før vi kan træffe beslutningen.', after=44)
    lp('Med venlig hilsen', after=8)
    lp('Shahram Ajloo', after=8)

    # ------------------------------------------------------------ CV, side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Projektleder med teknisk baggrund som elautoriseret maskinmester (LV/MV/HV), og erfaring fra planlægning og koordinering af tekniske anlægsprojekter. '
           'Hos Novo Nordisk styrede jeg fremdrift, økonomi og risici i 37 samtidige CAPEX-projekter, og hos Biofos stod jeg for '
           'drift og vedligehold af pumper, HVAC og højspændingstavler i døgndrift på spildevandsrensningen. '
           'Leder af et 14-mands entrepriseteam hos Ventek-Air. Ansvarlig for AI- og AI coding-afdelingen hos Data Power Consultant ApS. '
           'PRINCE2-certificeret. Dansk og engelsk.', after=32)

    m.section('PLANLÆGNING OG KOORDINERING')
    tasks = [
        ('Projektstyring',
         'Fremdrift, økonomi, risici og ressourcer i 37 samtidige CAPEX-projekter hos Novo Nordisk (DKK 2 til 10 mio. pr. stk.). '
         '11 parallelle anlægsprojekter hos Ventek-Air fra specifikation til formel aflevering.'),
        ('Udbud og aftalegrundlag',
         'Udbud og tilbud, underentreprenører, aftalegrundlag, sikkerhedsdokumentation og afleveringspakker hos Ventek-Air og ELOHVAC.'),
        ('Prioritering og flaskehalse',
         'Daglige tavlemøder og flaskehalsanalyser hos Ventek-Air. Prioritering af samtidige projekter med én samlet plan hos Novo Nordisk og Data Power.'),
        ('Rapportering',
         'Månedsrapportering til ledelse og bygherre hos Novo Nordisk. KPI-dashboards og tilbudsberegning i ELOHVAC, udarbejdet med Python og Claude API.'),
    ]
    for head, body in tasks:
        m.bullet(head, body, after=24)

    m.section('DRIFT, VEDLIGEHOLD OG ANLÆG')
    tasks = [
        ('Døgndrift på spildevand',
         'Drift og vedligehold af pumper, HVAC, højspændingstavler og SCADA i døgndrift hos Biofos (Lynetten), 2017 til 2022. '
         'Forebyggende vedligehold, akut fejlfinding og reservedelsflow.'),
        ('Ledelse i skiftehold',
         'Ledelse af driftsteam i skiftehold på ledelsesniveau og teamledelse på øvrige niveauer i døgnbemanding.'),
        ('Montage, test og idriftsættelse',
         'FAT, SAT og IQ/OQ/PQ under GMP, FDA og EMA hos Novo Nordisk, med nul kritiske afvigelser ved aflevering. '
         'Idriftsættelse af tanke, procesrør, CIP/SIP-systemer og instrumentering.'),
        ('Ventiler og trykudstyr',
         'Vedligehold af ventiler, trykbærende udstyr og sikkerhedsudstyr. LOTO, risikovurdering og APV ved hvert arbejde.'),
        ('Forbedring',
         'PDCA-program med 40 % lavere energiomkostninger hos Novo Nordisk. 5S, Standard Work og PDCA på værksted og lager hos Biofos.'),
    ]
    for head, body in tasks:
        m.bullet(head, body, after=24)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester, ansvarlig for el-teknik og ventilation',
         'Data Power Consultant ApS · København · 2024 til i dag · kandidatens eneste ansættelse',
         [('', 'Ansvarlig for AI- og AI coding-afdelingen med 4 til 10 personer. Kundeløsninger med LLM-API\'er og AI-agenter '
               'samt tekniske og industrielle applikationer, fra kravafdækning og arkitektur til idriftsættelse og overdragelse.'),
          ('', 'AI coding til beregning, dimensionering og designvarianter af tekniske anlæg og industrielle komponenter, '
               'valideret med faglig kontrol, før noget gik videre til kunden.'),
          ('', 'El-teknik og ventilation med fuldt P&L-ansvar, herunder akkord og opmåling. Fra november 2026 også de el-tekniske '
               'aktiviteter fra ELOHVAC.'),
          ('', 'Personaleledelse af 5 elektrikere og 3 lærlinge: daglig planlægning, enkeltsamtaler, MUS og oplæring.'),
          ('', 'Matrixledelse af to sideløbende organisationer, ELOHVAC og Data Power, med én samlet plan og skriftlige aftaler '
               'om, hvad der går forud.')]),
        ('Ejer og teknisk direktør, elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 til november 2026 (virksomheden lukket)',
         [('', 'Installation, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg, fra akutte udkald til afleverede anlæg.'),
          ('', 'Tilbud og beregning, tidsplaner, materialestyring og underentreprenører. LOTO, risikovurdering og APV ved hver pladsopstart.'),
          ('', 'Akkord og opmåling: akkordbreve, opmåling af udført arbejde, tildeling af akkord til sjak og regulering af mer- og mindrearbejde.')]),
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
        ('Projekt og planlægning', 'PRINCE2, Microsoft Project, RACI, udbud, tilbud, afleveringspakker, MUS'),
        ('Drift og vedligehold', 'Forebyggende vedligehold, CMMS, reservedele, MTBF, MTTR, OEE, fejlfinding'),
        ('Styring og automation', 'SCADA, styretavler, CTS/BMS, KNX'),
        ('Kvalitet og dokumentation', 'GMP, FDA, EMA, ISO 9001, audits, procedurer, afvigelser'),
        ('Forbedring', 'PDCA, 5S, Standard Work, A3, FMEA, 5 Hvorfor, Ishikawa'),
        ('Digitale værktøjer', 'Python, Power BI, Excel, Claude API'),
    ], widths=(3400, 6946), compact=True)
    m.para('Dansk og engelsk i skrift og tale, engelsk som arbejdssprog siden 2017. Persisk modersmål. Kørekort B med manuelt gear.', after=40)

    # ------------------------------------------------------------ kravmatrix, side 4
    m.page_break()
    m.section('KRAVMATRIX')
    m.models_table('Opslagets krav og min dokumentation', ('Krav', 'Dokumentation og status'),
                   ROWS, widths=(3600, 6746), compact=True)

    m.save(path, title='Projektleder / fagkoordinator til regnvandsbassiner - Novafos',
           subject='Ansøgning Projektleder / fagkoordinator til regnvandsbassiner')
    print(path)


if __name__ == '__main__':
    os.makedirs(OUT_DIR, exist_ok=True)
    write_inputs()
    build(OUT)
