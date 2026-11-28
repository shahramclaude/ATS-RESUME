# -*- coding: utf-8 -*-
"""Aquarden Technologies · Teknisk medarbejder, produktion og field service (Skævinge, TechJob).

Dansk opslag -> dansk dokument. Masterdesign (scripts/master_design.py): brev side 1, CV side 2-3,
kravmatrix side 4. Kun fakta fra master-CV'et og brugerbekræftelser.
Ikke dokumenteret og derfor ikke skrevet som erfaring: SCWO-anlæg, PFAS-behandling, rejsevilje
for denne stilling (ikke bekræftet for denne stilling i master), procesteknik som fagområde.
Opslaget beder om at skrive, at jobbet er set hos TechJob; det står i brevet.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
OUT_DIR = os.path.join(ROOT, 'output')
OUT = os.path.join(OUT_DIR, 'Shahram_Ajloo_Aquarden_TekniskMedarbejder.docx')
KRAV = os.path.join(ROOT, 'jd', 'Aquarden_TekniskMedarbejder_krav.txt')
KULTUR = os.path.join(ROOT, 'jd', 'Aquarden_TekniskMedarbejder_kultur.txt')

NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Teknisk medarbejder, produktion og field service · Aquarden Technologies, Skævinge'
BANNER_RESUME = 'Montage, test og service af tekniske anlæg i industrien'

# (krav fra opslaget, dokumentation og status)
ROWS = [
    ('Produktion og montage af anlæg og tilhørende tekniske systemer i tæt samarbejde med kolleger',
     'Dokumenteret. Montage og idriftsættelse af tanke, procesrør og instrumentering i et GMP-miljø hos Novo Nordisk, 2022 til 2024, og installation af el- og ventilationsanlæg hos ELOHVAC.'),
    ('Test, fejlfinding og klargøring af anlæg inden levering til kunder',
     'Dokumenteret. FAT, SAT og IQ/OQ/PQ hos Novo Nordisk med nul kritiske afvigelser ved aflevering. Fejlfinding på pumper, HVAC og højspændingstavler i døgndrift hos Biofos.'),
    ('Installation og idriftsættelse af anlæg hos kunder',
     'Dokumenteret. Idriftsættelse af el- og procesanlæg hos Novo Nordisk, og overdragelse af færdige installationer hos ELOHVAC og Ventek-Air.'),
    ('Service, vedligeholdelse og løsning af tekniske problemstillinger på installerede anlæg',
     'Dokumenteret. Forebyggende vedligehold og akut fejlfinding hos Biofos, 2017 til 2022. Service og fejlfinding på el-, ventilations- og klimaanlæg hos ELOHVAC og Data Power.'),
    ('Bidrage til løbende forbedringer af produkter, produktionsmetoder og serviceløsninger',
     'Dokumenteret som metode. PDCA-program med 40 % lavere energiomkostninger hos Novo Nordisk, og 5S og Standard Work på værksted og lager hos Biofos.'),
    ('Udarbejdelse og vedligeholdelse af teknisk dokumentation og arbejdsprocedurer',
     'Dokumenteret. Afleveringsdokumentation og procedurer under GMP, FDA og EMA hos Novo Nordisk, samt ISO 9001-baseret kvalitetsstyring med audits.'),
    ('Bred teknisk forståelse og flair for praktiske og tekniske løsninger',
     'Dokumenteret. Fejldiagnose og reparation af industrielle el- og mekaniske anlæg hos ARJ, og rodårsagsanalyse med FMEA, 5 Hvorfor og A3.'),
    ('Erfaring med montage, vedligeholdelse eller fejlfinding på maskiner eller tekniske anlæg',
     'Dokumenteret. Vedligehold og fejlfinding på pumper, HVAC og SCADA-styrede anlæg i døgndrift hos Biofos, samt montage af el- og ventilationsanlæg hos ELOHVAC.'),
    ('Planlægge og gennemføre tekniske opgaver selvstændigt',
     'Dokumenteret. Daglig planlægning af skifteholdsdrift hos Biofos, og fuldt P&L-ansvar for el- og ventilationsopgaver hos ELOHVAC og Data Power.'),
    ('Indstillet på rejseaktivitet i perioder',
     'Ikke afklaret for denne stilling. Min dokumentation om rejseaktivitet gælder bestemte roller, og rejsevilje til denne stilling er ikke bekræftet i min dokumentation.'),
    ('Kommunikere og formidle på dansk og engelsk',
     'Dokumenteret. Dansk i skrift og tale. Engelsk er arbejdssprog i internationale projekter siden 2017, og engelsk er mit professionelle arbejdssprog i dag.'),
    ('Interesse for på sigt at påtage sig et større fagligt og koordinerende ansvar',
     'Dokumenteret. Ledelse af et 14-mands entrepriseteam hos Ventek-Air, koordinering af 25 specialister hos Novo Nordisk og personaleledelse af 5 elektrikere og 3 lærlinge.'),
    ('Uddannelse som maskinmester eller anden relevant teknisk eller håndværksmæssig baggrund',
     'Dokumenteret. LV/MV/HV-autorisation som elautoriseret maskinmester, maj 2023, og B.Tech (EQF6) i teknologiledelse og maskinteknik, 2017 til 2022.'),
    ('Erfaring med procesanlæg, mekanik, rørsystemer, procesinstrumentering, el eller automation',
     'Dokumenteret. Procesrør, tanke og instrumentering hos Novo Nordisk, mekanisk drift af pumper hos Biofos, og el og automation med SCADA og CTS/BMS.'),
    ('Selvstændigt arbejde og samarbejde med kolleger',
     'Dokumenteret. Skifteholdsdrift med sikkerhedsdisciplin, LOTO og APV, og daglige tavlemøder og flaskehalsanalyser hos Ventek-Air.'),
    ('Ansvarsbevidst, kvalitetsbevidst og struktureret arbejdsform',
     'Dokumenteret. ISO 9001-baseret kvalitetsstyring og audits, GMP-dokumentation og registrering af nærved-hændelser ved skifteholdsdrift hos Biofos.'),
    ('Initiativrig og i stand til at bevare overblikket, også når opgaverne ikke er kendte på forhånd',
     'Dokumenteret. 11 samtidige anlægsprojekter hos Ventek-Air og 37 samtidige CAPEX-projekter hos Novo Nordisk, med daglige tavlemøder og flaskehalsanalyser hos Ventek-Air.'),
    ('Omhyggelig i både rutineprægede og nye opgaver',
     'Dokumenteret. Forebyggende vedligeholdelsesplaner hos Biofos og validering af nye systemer under GMP hos Novo Nordisk.'),
    ('Fleksibel og villig til at påtage sig forskellige typer opgaver',
     'Dokumenteret. Montage, test, idriftsættelse og service i forskellige faser af det samme anlæg hos Novo Nordisk og ELOHVAC.'),
    ('Nysgerrig og interesseret i at tilegne sig ny viden',
     'Dokumenteret. Python og Claude API anvendes i daglig drift til tilbud, planlægning og KPI-analyse, og AI-værktøjerne gav over 40 % produktivitetsløft i ELOHVAC-posten.'),
]

KULTUR_PHRASES = [
    'Et spændende og alsidigt job i en teknologivirksomhed i udvikling',
    'Højt specialiserede kolleger inden for kemi, konstruktion, produktion og procesteknik',
    'en flad ledelsesstruktur, hvor der lyttes til medarbejderne',
    'alle kan bidrage med idéer',
    'Stor variation i arbejdsopgaverne',
    'Mulighed for at præge udviklingen af virksomhedens fremtidige serviceorganisation',
    'Mulighed for både faglig og personlig udvikling',
    'reducerer omkostningerne ved behandling af industrielt spildevand',
]


def write_inputs():
    with open(KRAV, 'w', encoding='utf-8') as f:
        f.write('# Krav fra Aquarden Technologies · Teknisk medarbejder, produktion og field service (Skævinge, TechJob), dansk, ordret fra opslaget\n')
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
    m.meta('Aquarden Technologies ApS · Skævinge · stillingen set på TechJob')
    m.para('Kære Aquarden Technologies,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    def sub(text):
        p = m._p(spacing_after=20, spacing_before=60, line=260, justify=False, keep_next=True)
        m._run(p, text, bold=True, color='002B5C')
        return p

    # ------------------------------------------------------------ brev, side 1
    lp('Aquarden bygger anlæg, der nedbryder PFAS, medicinrester og opløsningsmidler i komplekst industrielt '
       'spildevand med superkritisk vandoxidation. Virksomhedens mission er at levere løsninger, der reducerer omkostningerne ved behandling af industrielt spildevand. Stillingen som teknisk medarbejder i Production & Development, '
       'som jeg har set hos TechJob, binder værkstedet sammen med felten: montage, test og klargøring i Skævinge, '
       'og installation, idriftsættelse og fejlfinding hos kunderne. Det er den samlede opgave, jeg gerne vil løse.')

    sub('Klargøring før levering')
    lp('En SCWO-anlæg er først klar, når testen har vist, at reaktor, trykudstyr, pumper og styring opfører sig, '
       'som de skal under belastning. Jeg vil bruge samme rækkefølge, som vi kender fra GMP-systemer: testplan, '
       'afvigelseshåndtering og dokumentation, der følger anlægget ud af værkstedet. Det sparer tid hos kunden, '
       'og det gør fejlfindingen lettere, hvis der opstår noget.')

    sub('Montage med de samme tegninger og krav')
    lp('Når produktion og montage deler de samme rammer, forsvinder mange af de fejl, der først opdages på '
       'byggepladsen. Jeg vil arbejde med stykliste, rørføring, instrumentering og el-tegninger, så der er én '
       'version af sandheden, både i værkstedet og i det, der sendes til kunden.')

    sub('Field service, der kan vokse')
    lp('Når antallet af installerede anlæg stiger, skal serviceopgaverne have faste rutiner: hvem der kører '
       'opgaven, hvilke reservedele der skal være med, hvordan fejlen dokumenteres, og hvad kunden får at vide. '
       'Opslaget beskriver en flad ledelsesstruktur, hvor der lyttes til medarbejderne, og hvor alle kan bidrage med idéer. '
       'Det er den rette ramme for at få erfaringer fra felten tilbage til værkstedet. Opslaget nævner også mulighed '
       'for at præge udviklingen af virksomhedens fremtidige serviceorganisation, og det er den opgave, der vokser frem, '
       'når flere anlæg står ude hos kunderne.')

    sub('Det, der er nyt for mig')
    lp('SCWO og behandling af PFAS er nyt for mig. Jeg kender pumper, ventiler, trykudstyr og rørsystemer fra '
       'drift og vedligehold, men processen og de kemiske forhold skal læres sammen med kollegerne. Opslaget nævner mulighed for både faglig og personlig udvikling, og det er den retning, jeg ser i stillingen. '
       'Et spændende og alsidigt job i en teknologivirksomhed i udvikling. Stor variation i arbejdsopgaverne og '
       'højt specialiserede kolleger inden for kemi, konstruktion, produktion og procesteknik gør det til en stilling, '
       'hvor man lærer hele tiden. Den læring er en del af jobbet.')

    lp('Jeg vil gerne tale om, hvor den første field service-opgave skal begynde, og hvordan den kan dokumenteres, '
       'så den bliver brugbar for værkstedet, næste gang vi står med det samme problem.', after=44)
    lp('Med venlig hilsen', after=8)
    lp('Shahram Ajloo', after=8)

    # ------------------------------------------------------------ CV, side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Elautoriseret maskinmester (LV/MV/HV) med erfaring i montage, idriftsættelse, test og service af tekniske '
           'anlæg. Fejlfinding og forebyggende vedligehold i døgndrift på pumper, HVAC og højspændingstavler hos Biofos, '
           'idriftsættelse og FAT, SAT og IQ/OQ/PQ under GMP hos Novo Nordisk, og el- og ventilationsanlæg hos ELOHVAC og '
           'Data Power. Arbejder med CMMS, teknisk dokumentation og ISO 9001-baseret kvalitetsstyring. PRINCE2-certificeret. '
           'Dansk og engelsk.', after=32)

    m.section('MONTAGE, TEST OG SERVICE')
    tasks = [
        ('Montage og idriftsættelse',
         'Idriftsættelse af tanke, procesrør, CIP/SIP-systemer og instrumentering hos Novo Nordisk, og overdragelse af færdige '
         'el- og ventilationsanlæg hos ELOHVAC.'),
        ('Test og klargøring',
         'FAT, SAT og IQ/OQ/PQ med nul kritiske afvigelser ved aflevering. Klargøring af anlæg inden levering til kunden.'),
        ('Fejlfinding og service',
         'Akut fejlfinding og forebyggende vedligehold på pumper, HVAC, højspændingstavler og SCADA i døgndrift hos Biofos, '
         '2017 til 2022.'),
        ('Ventiler, trykudstyr og sikkerhedsudstyr',
         'Vedligeholdelsesarbejde på ventiler, trykbærende udstyr og sikkerhedsudstyr. LOTO, risikovurdering og APV før '
         'arbejdet startede.'),
        ('Dokumentation og procedurer',
         'Afleveringsdokumentation, procedurer og arbejdsinstruktioner under GMP, FDA og EMA. ISO 9001-baserede audits.'),
        ('Forbedring',
         'PDCA-program med 40 % lavere energiomkostninger hos Novo Nordisk. 5S, Standard Work og A3 i værksted og lager.'),
        ('Koordinering og ledelse',
         'Ledelse af et 14-mands entrepriseteam hos Ventek-Air. Personaleledelse af 5 elektrikere og 3 lærlinge gennem enkeltsamtaler og MUS.'),
    ]
    for head, body in tasks:
        m.bullet(head, body, after=24)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester, ansvarlig for el-teknik og ventilation',
         'Data Power Consultant ApS · København · 2024 til i dag · kandidatens eneste ansættelse',
         [('', 'Ansvarlig for AI- og AI coding-afdelingen med 4 til 10 personer. Kundeløsninger med LLM-API\'er og AI-agenter samt '
               'tekniske og industrielle applikationer, fra kravafdækning og arkitektur til idriftsættelse og overdragelse.'),
          ('', 'AI coding til design af tekniske anlæg og industrielle komponenter: beregning, dimensionering og designvarianter, '
               'valideret med faglig kontrol, før noget gik videre til kunden.'),
          ('', 'El-teknik og ventilation med fuldt P&L-ansvar, herunder akkord og opmåling. Fra november 2026 også de el-tekniske '
               'aktiviteter fra ELOHVAC.'),
          ('', 'Personaleledelse af 5 elektrikere og 3 lærlinge: daglig planlægning, enkeltsamtaler, MUS og oplæring.'),
          ('', 'Matrixledelse af to sideløbende organisationer, ELOHVAC og Data Power, med én samlet plan og skriftlige aftaler '
               'om, hvad der går forud.')]),
        ('Ejer og teknisk direktør, elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 til november 2026 (virksomheden lukket)',
         [('', 'Installation, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg, fra akutte udkald til '
               'afleverede anlæg.'),
          ('', 'Tilbud, tidsplaner, materialestyring og underentreprenører. LOTO, risikovurdering og APV ved hver pladsopstart.'),
          ('', 'Akkord og opmåling: akkordbreve, opmåling af udført arbejde, tildeling af akkord til sjak og regulering af mer- og mindrearbejde.')]),
        ('Senior idriftsættelsesingeniør og projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg og Bagsværd · november 2022 til juli 2024',
         [('', 'FAT, SAT og IQ/OQ/PQ under GMP, FDA og EMA, med nul kritiske afvigelser ved aflevering.'),
          ('', 'Tværfaglig koordinering af 25 specialister og 37 samtidige anlægsprojekter.')]),
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
    m.edu('Køleteknik og klimaanlæg (AMU)', 'Mercantec · 2021')
    m.edu('PRINCE2, certificeret', 'AXELOS / PeopleCert')
    m.para('Lean og Six Sigma anvendt i praksis, ikke certificeret: DMAIC, 5S, PDCA, VSM, A3, Kaizen, SMED, TPM, '
           '5 Hvorfor, Ishikawa og FMEA.', after=48)

    m.section('KOMPETENCER')
    m.models_table('Værktøjer og systemer', ('Område', 'Værktøjer'), [
        ('Montage og test', 'Idriftsættelse, FAT, SAT, IQ/OQ/PQ, CIP/SIP, procesrør, instrumentering, tanke'),
        ('Vedligehold', 'Forebyggende vedligehold, CMMS, reservedele, MTBF, MTTR, OEE, fejlfinding'),
        ('Styring og automation', 'SCADA, styretavler, CTS/BMS, KNX'),
        ('Kvalitet', 'GMP, FDA, EMA, ISO 9001, audits, procedurer, afvigelser og dokumentation'),
        ('Forbedring', 'PDCA, 5S, Standard Work, A3, FMEA, 5 Hvorfor, Ishikawa'),
        ('Digitale værktøjer', 'Python, Power BI, Excel, Claude API'),
    ], widths=(3400, 6946), compact=True)
    m.para('Dansk og engelsk i skrift og tale, engelsk som arbejdssprog siden 2017. Persisk modersmål. Kørekort B med manuelt gear.', after=40)

    # ------------------------------------------------------------ kravmatrix, side 4
    m.page_break()
    m.section('KRAVMATRIX')
    m.models_table('Opslagets krav og min dokumentation', ('Krav', 'Dokumentation og status'),
                   ROWS, widths=(3600, 6746), compact=True)

    m.save(path, title='Teknisk medarbejder, produktion og field service - Aquarden Technologies',
           subject='Ansøgning Teknisk medarbejder, produktion og field service')
    print(path)


if __name__ == '__main__':
    os.makedirs(OUT_DIR, exist_ok=True)
    write_inputs()
    build(OUT)
