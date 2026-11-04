# -*- coding: utf-8 -*-
"""SYSTRA: samlet ansøgning, CV og opstartsplan til Spor og Anlæg."""
import os
from master_design import MasterDoc
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Teknisk ledelse | Projekter, mennesker og kvalitet'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'

def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('4. november 2026')
    m.meta('SYSTRA Danmark · Spor og Anlæg · Julie Josefine Feddersen')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Teamleder til Spor og Anlæg, København', bold=True, color='1A1A1A')
    m.para('Når fem specialister skal levere på flere projekter, skal der være plads til faglig fordybelse og samtidig klarhed om kapacitet, kvalitet og de beslutninger, kunderne venter på. En god teamleder skaber ro om prioriteringerne og sørger for, at de rette fagpersoner bliver inddraget i tide.', after=80)
    m.para('I SYSTRA vil jeg begynde med at forstå teamets leverancer, samarbejdet med projektlederne og snitfladerne til Aarhus. Jeg vil bruge min erfaring med tekniske projekter og personaleledelse til at skabe et fælles overblik — og lade kvalificerede sporspecialister stå for de sporfaglige vurderinger og godkendelser.', after=80)
    for label, body in [
        ('Prioritering og fremdrift', 'Samle kommende leverancer, belastning og afhængigheder i en enkel kapacitetsoversigt. På et kort ugentligt tavlemøde afklarer teamet, hvad der haster, hvor der er pres, og hvilke beslutninger projektlederne skal træffe.'),
        ('Kvalitet og kunde', 'Aftale leverancens indhold, frist og kvalitetskontrol med projektleder og den ansvarlige specialist. Ved ændringer gør jeg konsekvenser for tid, økonomi og bemanding synlige og følger op på aftaler med kunden.'),
        ('Mennesker og videndeling', 'Bruge 1:1, situationsbestemt ledelse og en kompetenceoversigt til at forstå den enkelte medarbejders ambitioner og behov. Faglig sparring mellem København og Aarhus kan mindske sårbarhed og gøre viden lettere at dele.'),
        ('Sikker faglig afklaring', 'Spor, baneafvanding, projektering og CAD kræver dokumenteret faglighed. Jeg vil ikke træffe eller godkende sporfaglige beslutninger uden de rette kompetencer; mandat og faglig kvalitetssikring skal aftales med afdelingslederen.')]: m.bullet(label, body, after=35)
    m.para('Jeg er elautoriseret maskinmester og har ledet specialister og tekniske projekter, men mit CV dokumenterer ikke erfaring med sporprojektering, baneafvanding, jernbanestandarder eller CAD/3D på sporområdet. Det er et væsentligt gab i en stilling, hvor sporfaglighed er tyngdepunktet. Jeg vil gerne drøfte med jer, om min ledelses- og projektprofil kan være relevant, eller om en anden rolle er et bedre match.', after=80)
    m.para('Hos ELOHVAC leder jeg fem elektrikere og tre lærlinge; hos Novo Nordisk koordinerede jeg 25 specialister og fulgte økonomi, kvalitet og fremdrift i 37 tekniske CAPEX-projekter. Jeg søger en dialog om, hvordan den erfaring bedst kan bringes i spil hos SYSTRA.', after=80)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Elautoriseret maskinmester og erfaren personaleleder med baggrund i tekniske entrepriser, driftskritiske anlæg og tværfaglig projektstyring. Jeg skaber overblik over kapacitet, leverancer og risici og udvikler medarbejdere gennem tydelige aftaler og løbende dialog. Min dokumenterede tekniske erfaring er el, mekanik og idriftsættelse — ikke jernbane og spordisciplinen.', after=80)
    m.section('LEDELSE OG PROJEKTER I PRAKSIS')
    for label, body in [
        ('Personaleledelse', 'ELOHVAC: daglig ledelse af fem elektrikere og tre lærlinge med opgavefordeling, 1:1, MUS og oplæring. Ventek-Air: ledede et team på 14 og 11 samtidige tekniske projekter.'),
        ('Specialister og koordinering', 'Novo Nordisk: koordinerede 25 specialister på tværs af engineering, indkøb og anlæg på 37 samtidige tekniske CAPEX-projekter.'),
        ('Kvalitet, økonomi og kunder', 'Fulgte fremdrift, økonomi, risici og ressourcer og rapporterede til ledelse og bygherre hos Novo. ELOHVAC: tilbud, materialer, underentreprenører og fuldt P&L.'),
        ('Forbedringer og leverancer', 'Ventek-Air: daglige tavlemøder og flaskehalsanalyse. Novo: FAT/SAT og IQ/OQ/PQ samt PDCA-program, der reducerede energiomkostninger med 40 %.'),
        ('Digital udvikling', 'Aktiv professionel AI-/Claude-koder: Python/Claude API til planlægning, KS og KPI hos ELOHVAC; dokumenteret produktivitetsløft over 40 %. Bygger også investeringsmodeller til udvikling og nye forretningsidéer.')]: m.bullet(label, body, after=30)
    m.models_table('LEDELSESVÆRKTØJER I PRAKSIS', ('Område', 'Metode og anvendelse'), [
        ('Dialog og udvikling', 'Situationsbestemt ledelse, 1:1, MUS og struktureret oplæring hos ELOHVAC.'),
        ('Plan og prioritering', 'Tavlemøder og flaskehalsanalyse til kapacitetsstyring hos Ventek-Air.'),
        ('Kvalitet og læring', 'PDCA, A3, 5 x hvorfor og Ishikawa hos Novo; 5S og Standard Work hos Biofos.'),
        ('Sikkerhed', 'APV, LOTO og risikovurdering i teknisk drift og ved pladsopstart.')])
    m.section('FAGLIG AFGRÆNSNING')
    m.para('Erfaring med sporprojektering, baneafvanding, jernbanestandarder, 3D-modellering og CAD-værktøjer på sporområdet er ikke dokumenteret. B.Tech-maskinmesteruddannelsen er ikke angivet som diplom- eller civilingeniøruddannelse.', after=70)
    m.page_break()
    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør / elautoriseret maskinmester', 'ELOHVAC ApS · København · maj 2023–nu', '5 elektrikere og 3 lærlinge · fuldt P&L-ansvar', [
            ('Planlægning og leverancer', 'Daglig opgaveplanlægning, tilbud, materialer, underentreprenører, kvalitetskontrol og aflevering på el-, ventilations- og klimaanlæg.'),
            ('Digitale værktøjer', 'Python/Claude API-værktøjer til tilbud, tidsplaner, KS og KPI; over 40 % produktivitetsløft i virksomheden.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem', 'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024', '37 samtidige CAPEX-projekter · 25 specialister · 2–10 mio. kr. pr. projekt', [
            ('Fremdrift og ressourcer', 'Fulgte fremdrift, økonomi, risici og ressourcer mellem engineering, indkøb og anlæg. SAP ERP til økonomi og aktiver; rapportering til ledelse og bygherre.'),
            ('Kvalitet og forbedring', 'FAT/SAT og IQ/OQ/PQ i GMP-regulerede projekter uden kritiske fund ved aflevering. PDCA-program reducerede energiomkostninger med 40 %.')]),
        ('Projekt- og værkstedsleder', 'Ventek-Air · København · jan. 2022–nov. 2022', '14 medarbejdere · 11 samtidige anlægsprojekter', [
            ('Kapacitet og flow', 'Planlægning fra specifikation til aflevering, underentreprenører og dokumentation. Tavlemøder og flaskehalsanalyse gav bedre grundlag for levering.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker', 'Biofos, Lynetten · København · aug. 2017–jan. 2022', '24/7-drift · pumper, HVAC, højspændingstavler og SCADA', [
            ('Tilgængelighed og lager', 'Forebyggende vedligehold, akut fejlfinding og reservedelsflow. 5S, Standard Work, PDCA, LOTO og risikovurdering.')]),
        ('Elektromekaniker / produktionsteamleder', 'ARJ Engineering · Teheran · dec. 2003–mar. 2010', '12 mekanikere og teknikere', [
            ('Plan og materialer', 'Vagtplanlægning, materialestyring og målopfølgning; fejldiagnose og reparation af industrielt el- og mekanisk udstyr.')])]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        m.doc.paragraphs[-1].runs[0].text = 'Omfang: '
        for label, body in bullets: m.bullet(label, body, after=25)
    m.section('UDDANNELSE OG AUTORISATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering — maskinmesterretningen', 'Maskinmesterskolen København · 2017–2022 · EQF 6')
    m.edu('El- og maskinteknisk design, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('Køleteknik og klimaanlæg · STCW-sikkerhed og maskinrumsvagt', 'Mercantec 2021 · Søfartsstyrelsen 2021–2023')
    m.section('SPROG OG PRAKTISK')
    m.para('Dansk og persisk/farsi: modersmål · Engelsk: professionelt i skrift og tale · Kørekort B · Bopæl i Måløv. Opstart og overgang fra ELOHVAC aftales.', after=70)
    m.section('REFERENCER')
    m.para('Tidligere ledere hos Novo Nordisk og Biofos oplyses efter aftale.', after=70)

    m.page_break()
    m.models_table('FØRSTE 90 DAGE — FORSLAG TIL OPSTART', ('Tid', 'Handlinger og leverancer'), [
        ('Uge 1', 'Møde afdelingslederen, teamet og samarbejdspartnerne i Aarhus. Afklare mandat, faglig godkendelse og igangværende leverancer; lytte til medarbejdernes prioriteringer og bekymringer.'),
        ('Inden dag 30', 'Gennemføre 1:1 og danne overblik over kompetencer, kapacitet og projektforpligtelser. Aftale en enkel rytme for koordinering med projektledere og fagligt ansvarlige.'),
        ('Inden dag 60', 'Følge op på ressourcepres, tid, økonomi og kvalitet med de relevante projektledere. Aftale videndeling og faglig review med de kompetente sporspecialister; identificere egne læringsbehov.'),
        ('Inden dag 90', 'Evaluere samarbejde, trivsel og leveranceoverblik med teamet og afdelingslederen. Beslutte næste udviklingstiltag og sikre, at fagligt ansvar fortsat ligger hos kvalificerede personer.')])
    m.section('EN HVERDAG MED PLADS TIL FAGLIGHED')
    for label, body in [
        ('Medarbejderne', 'Afklare roller og forventninger gennem 1:1 og MUS. Bruge situationsbestemt ledelse til at støtte den enkelte uden at overtage specialistens arbejde.'),
        ('Projektledere og kunder', 'Få en fælles aftale om opgave, deadline, bemanding og review. Ved travlhed tydeliggøres konsekvenser og alternativer, så prioriteringen træffes på et oplyst grundlag.'),
        ('Faglig kvalitet', 'Sikre, at tekniske løsninger, projektering og kundens spørgsmål vurderes og godkendes af medarbejdere med den nødvendige kompetence og efter SYSTRAs procedurer.'),
        ('København og Aarhus', 'Aftale faste lejligheder til videndeling på tværs af kontorerne og involvere de rette kolleger, når en opgave kræver særlig sporfaglighed.')]: m.bullet(label, body, after=35)
    m.section('DATA OG FORBEDRING MED MENNESKET I CENTRUM')
    m.para('Tavlemøder kan skabe overblik over deadlines og afhængigheder; PDCA og årsagsanalyse kan hjælpe teamet med at lære af gentagne afvigelser. Ændringer bør afprøves i lille skala og må ikke erstatte virksomhedens kvalitetssystem eller faglige godkendelser.', after=80)
    m.para('Jeg udvikler værktøjer i Python og Claude til planlægning, kvalitet og analyse samt investeringsmodeller med NPV, IRR og scenarier. Eventuel brug i SYSTRA forudsætter godkendte systemer og data samt menneskelig kontrol. AI erstatter ikke sporfaglig rådgivning eller teknisk review.', after=80)
    m.section('FRA OPSTART TIL LEVERANCE')
    m.para('For hver opgave vil jeg sammen med projektleder og den fagligt ansvarlige afklare leverancens formål, kompetencebehov, tidsfrist og kvalitetskontrol. Herefter kan teamet synliggøre afhængigheder og åbne beslutninger. En klar aftale om ansvar og næste skridt gør det lettere at reagere, når projekterne ændrer sig.', after=80)
    return m.save(path, title='Ansøgning og CV — Teamleder Spor og Anlæg, SYSTRA', subject='Teknisk ledelse og projektkoordinering', keywords='teamleder, projektledelse, kvalitet, SYSTRA')

if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_SYSTRA_TeamlederSporOgAnlaeg.docx')))
