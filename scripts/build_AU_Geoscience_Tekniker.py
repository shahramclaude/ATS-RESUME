# -*- coding: utf-8 -*-
"""Aarhus Universitet, Institut for Geoscience — tekniker til værksted og felt.
Bygger samlet jobfokuseret ansøgning og CV i masterdesign.
Krav/evidensgrænser og officiel AU-research: jd/AU_Geoscience_Tekniker_*.txt.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
OUTPUT = os.path.join(ROOT, 'Shahram_Ajloo_AU_Geoscience_Tekniker.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Maskinmester · elektromekanisk fejlfinding · værksted og felt'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'

LETTER = [
    'Et geofysisk målesystem er først klar til feltet, når hele kæden virker: sensor, strømforsyning, kabler, signalbehandling, optageenhed og datafil. En fejl, der ikke kan genskabes og afgrænses i værkstedet, bliver langt vanskeligere at løse om bord eller langt fra reservedele. Derfor bør service begynde med systemoverblik og ende med en dokumenteret funktionstest.',
    'Jeg vil bruge en fast fejlsøgningsrækkefølge: registrér symptom og driftsforhold, gennemgå forsyning og forbindelser, mål de relevante signaler, planlæg og dokumentér målinger, isolér fejlleddet, afprøv reparationen og gem resultatet sammen med instrumentets historik. Sikkerhed, fabrikantkrav og værkstedets instruktion styrer indgrebet; arbejde uden for egne kompetencer løftes til den erfarne tekniker. Fejlfinding på stærkstrøm og svagstrøm følger samme disciplin som arbejdet med mekaniske samlinger og bevægelige dele.',
    'Instituttets værksteder beskrives af AU som service- og udviklingsstøtte for geofysiske instrumenter, med både land- og marin seismik samt støtte i felten. Det stiller krav til mere end reparation: udstyr skal afprøves før afsendelse, kabler og reservedele pakkes efter en kontrolleret liste, og testresultater skal følge med udstyret, så forskere og teknikere kan forstå status og handle på stedet.',
    'En mobiliseringspakke bør samle instrument-ID, konfiguration, seneste test, kendte begrænsninger, diagrammer, kritiske reservedele og en kort fejlprocedure. Før afgang gennemgås funktion og sikker fastgørelse; efter brug registreres fejl og ændringer, så næste hold ikke starter uden historik. På skib skal løfte- og rigningsarbejde følge instruktioner, aftalte roller og stopkriterier for vejr og bevægelse. Det er en foreslået arbejdsform, der skal tilpasses AU’s procedurer og forskernes behov.',
    'Min dokumenterede baggrund er praktisk fejlfinding og reparation af industrielt el- og mekanisk udstyr, installation og vedligehold af el-anlæg samt erfaring fra flere områder af elektronikproduktion. Jeg har desuden arbejdet med FAT/SAT og kvalificeret aflevering af teknisk udstyr. Jeg har ikke lagt erfaring med AU’s navngivne land- og marinseismiske systemer, højtrykskompressorer, hydrauliske vibratorer, airguns, streamere, sparker, sedimentkerneoptagning, kernetagningsudstyr, mikroskoper eller hydrogeologiske laboratorieinstrumenter til grund. De systemer kræver oplæring ved en erfaren kollega. Det samme gælder konkret lodning, kabelreparationer, finmekanisk præcisionsarbejde og Windows-baserede optagesystemer.',
    'Jeg er indstillet på land- og søbaseret feltarbejde i det beskrevne omfang — cirka 6–8 uger årligt, herunder skibsture på 1–6 uger — og på at flytte til Aarhus. STCW-kurser er gennemført i 2021–2023; deres aktuelle gyldighed skal afklares. Jeg er indstillet på de nødvendige sikkerhedskurser og på at få undersøgt og søge om det krævede sundhedsbevis for søfarende. Målet er, at udstyr, data og sikker arbejdsform kan følge med forskerholdet fra værkstedet til feltet og tilbage.'
]

EXPERIENCE = [
    ('Indehaver / teknisk direktør / elautoriseret maskinmester', 'ELOHVAC ApS · København · maj 2023–nu', '5 elektrikere og 3 lærlinge · fuldt P&L-ansvar', [
        'Udfører og leder installation, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg; tavler og styring.',
        'Planlægger tilbud, materialer, underentreprenører, KS, dokumentation og aflevering; LOTO og risikovurdering ved pladsopstart.',
        'Udviklede Python/Claude-værktøjer til tidsplaner, KS og KPI med dokumenteret produktivitetsløft over 40 %.'
    ]),
    ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen', 'Data Power Consultant ApS · København · 2024–2026 · sideløbende med ELOHVAC', 'Tekniske og industrielle applikationer', [
        'Ledte tekniske applikationer fra krav og integration til idriftsættelse, dokumentation og overdragelse; Python, LLM-API’er og AI-agenter.',
        'Etablerede faglig kontrol, review og test af AI-assisteret udvikling samt koordinerede leverancer på tværs af teknik og kunde.'
    ]),
    ('Senior idriftsættelsesingeniør / projektleder, elsystem', 'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024', '37 CAPEX-projekter · 25 specialister · 2–10 mio. kr. pr. projekt', [
        'Koordinerede scope, fremdrift, økonomi, risici og ressourcer på tværs af engineering, indkøb og anlæg.',
        'FAT/SAT og IQ/OQ/PQ med nul kritiske afvigelser ved aflevering; tekniske tavler, styring, UPS og sikkerhedsbelysning.'
    ]),
    ('Projekt- og værkstedsleder', 'Ventek-Air · København · jan. 2022–nov. 2022', '14 medarbejdere · 11 samtidige projekter', [
        'Stod for kapacitets- og fremdriftsstyring, materialer, underentreprenører, sikkerhedsdokumentation og afleveringspakker.'
    ]),
    ('Vedligeholdelses- og driftsleder / værkstedstekniker', 'Biofos, Lynetten · København · aug. 2017–jan. 2022', 'Kritisk døgnbemandet procesdrift', [
        'Fejlfinding og forebyggende vedligehold på pumper, HVAC, højspændingstavler og øvrigt el-/mekanisk udstyr; SCADA-overvågning.',
        'Arbejdede med reservedelsflow, 5S, Standard Work, LOTO, APV og risikovurdering i skifteholdsdrift.'
    ]),
    ('Elektromekaniker / produktionsteamleder', 'ARJ Engineering · Teheran · dec. 2003–mar. 2010', '12 mekanikere og teknikere', [
        'Fejldiagnosticerede og reparerede industrielle el- og mekaniske anlæg; rodårsagsanalyse, materialestyring og teamledelse.'
    ]),
]


def add_jobs(m, jobs):
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for text in bullets:
            m.bullet('', text, after=12, line=195)


def build(path=OUTPUT):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('Aarhus Universitet · Institut for Geoscience · stillings-ID 173403')
    p = m._p(spacing_after=55, line=245, justify=False)
    m._run(p, 'Ansøgning · tekniker til forskningsudstyr, værksted og felt', bold=True)
    m.para('Til Institut for Geoscience, Aarhus Universitet', after=32, justify=False)
    for text in LETTER:
        m.para(text, after=42, line=215)
    m.meta('Med venlig hilsen', after=8)
    m.meta('Shahram Ajloo', after=0)

    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'FAGLIG PROFIL')
    m.para('Elautoriseret maskinmester med praktisk erfaring fra el- og mekanisk drift, fejlfinding og reparation samt tekniske projekter og udstyrsafprøvning. Har arbejdet med installationer, tavler og styring, industrielt udstyr, elektronikproduktion og dokumenteret aflevering. Arbejder systematisk fra symptom og måling til afhjælpning, funktionstest og overdragelse.', after=28, line=205)
    m.models_table('RELEVANT TEKNISK ERFARING', ('Dokumenteret grundlag', 'Afgrænsning / anvendelse'), [
        ('El og fejlfinding', 'ELOHVAC: stærkstrømsinstallationer, tavler, styring og vedligehold. Novo: svagstrømsrelaterede systemer som PDS, ABA/ABV og nød-/panikbelysning. Biofos: pumper, HVAC og højspændingstavler.'),
        ('Elektronikproduktion', 'Kandidaten har bekræftet erfaring fra flere områder i elektronikproduktion. Bestemte produktionsprocesser, loddeteknikker og stationer er ikke specificeret.'),
        ('Test og aflevering', 'Novo Nordisk: FAT/SAT og IQ/OQ/PQ på teknisk udstyr, tværfaglig koordinering og nul kritiske afvigelser ved aflevering.'),
        ('Værksted og vedligehold', 'Biofos: forebyggende vedligehold, akut fejlfinding og reservedelsflow i 24/7-drift. ARJ: elektromekanisk værkstedsarbejde og rodårsagsanalyse.'),
        ('Data og samarbejde', 'SAP ERP, Python/Claude, teknisk dokumentation og koordinering med teknikere, specialister, indkøb og drift.'),
        ('Felt og søsikkerhed', 'Indstillet på land- og søfeltarbejde i opslagets omfang. STCW-kurser gennemført 2021–2023; gyldighed skal afklares. Indstillet på at søge sundhedsbevis for søfarende.'),
    ], widths=(2450, 7896), compact=True)
    m.section('ERHVERVSERFARING · NYESTE FØRST')
    add_jobs(m, EXPERIENCE[:4])

    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'ERHVERVSERFARING · FORTSAT')
    add_jobs(m, EXPERIENCE[4:])
    m.section('UDDANNELSE, KURSER OG PRAKTISK')
    for title, detail in [
        ('B.Tech, Technology Management & Mechanical Engineering — maskinmesterretningen', 'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · EQF 6'),
        ('El- og maskinteknisk design, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6'),
        ('Elautoriseret maskinmester · LV/MV/HV', 'Sikkerhedsstyrelsen · 2023'),
        ('STCW-kurser', 'Søfartsstyrelsen · 2021–2023: vagt i maskinrummet (A-III/1), udpegede sikkerhedsopgaver (VI/6), skibssikkerhedsofficer (VI/5), sikkerhedsbevidsthed (VI/6-1), tankskibskurser (V/1-1, V/1-2). Aktuel gyldighed afklares.'),
        ('Køleteknik og klimaanlæg (AMU)', 'Mercantec · 2021'),
        ('PRINCE2-certificeret projektleder', 'AXELOS / PeopleCert'),
    ]:
        m.edu(title, detail)
    m.para('Dansk og persisk/farsi: modersmål · Engelsk: professionelt · Kørekort B (manuelt gear) · Windows-/måleplatforme: konkret drifts- og konfigurationskompetence afklares. Bopæl Måløv; indstillet på flytning til Aarhus.', after=28, line=195)
    m.section('OPLÆRING OG FAGLIG AFGRÆNSNING')
    m.para('Faglige områder til oplæring: AU’s land- og marinseismiske systemer, højtrykskompressorer, hydrauliske vibratorer, airguns, streamere, sparker, sedimentkerneoptagning og kernetagningsudstyr til søs, mikroskoper, hydrogeologisk laboratorieudstyr, Windows-baserede optagesystemer, konkrete lodde- og kabelreparationer, finmekanisk præcisionsarbejde samt forsendelse af udstyr/containere og feltmålinger/datahåndtering. Direkte erfaring med disse instrumenter og opgaver er ikke dokumenteret; oplæring med den erfarne kollega går forud for selvstændigt ansvar.', after=25, line=195)
    return m.save(path, title='Ansøgning og CV — tekniker, AU Institut for Geoscience',
                  subject='Elektromekanisk fejlfinding · forskningsudstyr · feltarbejde',
                  keywords='Aarhus Universitet; Geoscience; maskinmester; tekniker; fejlfinding; elektronik; mekanik; feltarbejde; STCW')


if __name__ == '__main__':
    print(build())
