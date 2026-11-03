# -*- coding: utf-8 -*-
"""HARIBO Faxe: ansøgning og CV til produktionsplanlægger, job 1478."""
import os
from master_design import MasterDoc
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Produktionsplanlægning | Kapacitet, koordinering og forbedringer'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv (Ballerup Kommune)'

def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('4. november 2026')
    m.meta('HARIBO · Produktion og Supply Chain · Faxe')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Produktionsplanlægger · job 1478', bold=True, color='1A1A1A')
    m.para('En produktionsplan virker først, når den kan gennemføres på fabrikken og samtidig understøtter det, kunderne forventer. Det kræver et fælles billede af efterspørgsel, kapacitet, råvarer og lager – og hurtig afklaring, når én af forudsætningerne ændrer sig.', after=80)
    m.para('I Faxe vil jeg begynde med at forstå HARIBOs eksisterende planlægningsrytme og data sammen med Supply Chain, Produktion, Lager og Customer Service. Jeg vil følge en plan fra prognose til levering for at se, hvor beslutninger træffes, hvor der opstår ventetid, og hvem der skal kontaktes, når planen må ændres.', after=80)
    for label, body in [
        ('En realistisk plan', 'Sammenholde salgsprognoser og efterspørgsel med tilgængelig produktionskapacitet, råvarer og lagerbeholdning. Aftale en kortsigtet plan med Produktionen og et længere sigte med Supply Chain, hvor usikkerheder og manglende data er synlige.'),
        ('Når noget ændrer sig', 'Gøre konsekvensen for ordren, kapaciteten og leveringstidspunktet tydelig. Afklare alternativer med Produktion og Lager og give Customer Service et aftalt grundlag at kommunikere ud fra.'),
        ('Opfølgning og forbedring', 'Følge planernes effektivitet og leveringssikkerhed med de mål, HARIBO allerede bruger. Undersøge gentagne afvigelser med PDCA og flaskehalsanalyse, før vi ændrer planlægningsprocesser eller værktøjer.'),
        ('Samarbejde og ejerskab', 'Holde aftaler, næste beslutning og ansvar synlige på tværs af funktionerne. Jeg vil bruge min erfaring med tavlemøder og tydelig opfølgning til at gøre det lettere for kollegerne at handle – ikke til at skabe ekstra rapportering.')]:
        m.bullet(label, body, after=35)
    m.para('I den første uge vil jeg lære flowet og planlægningens samarbejdspartnere at kende. Inden dag 30 vil jeg sammen med dem kortlægge de vigtigste begrænsninger; inden dag 60 afprøve en afgrænset forbedring; inden dag 90 følge op på virkningen og aftale de næste skridt.', after=80)
    m.para('Min erfaring med kapacitetsplanlægning og materialestyring kommer fra værksted, teknisk drift og projekter, ikke fra en stilling som fødevareproduktionsplanlægger. Jeg har brugt SAP til økonomi og aktiver hos Novo Nordisk og vil lære HARIBOs planlægningsfunktioner i ERP-systemet sammen med teamet. Start og de praktiske forhold mellem Måløv og Faxe aftales.', after=80)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL OG MOTIVATION')
    m.para('Teknisk planlægger og leder med erfaring i kapacitetsstyring, materialer og koordinering af mennesker og leverancer. Jeg søger en specialistrolle, hvor et godt planlægningsgrundlag og tæt samarbejde hjælper produktionen med at levere stabilt. Jeg arbejder analytisk og trives med at afklare prioriteringer sammen med dem, der skal udføre planen.', after=80)
    m.section('RELEVANT ERFARING')
    for label, body in [
        ('Kapacitet og fremdrift', 'Ventek-Air: planlagde kapacitet for et team på 14 og 11 samtidige anlægsprojekter. Daglige tavlemøder og flaskehalsanalyse understøttede bedre levering.'),
        ('Materialer og plan', 'ARJ Engineering: vagtplanlægning, materialestyring og målopfølgning i et maskinværksted med 12 mekanikere og teknikere. ELOHVAC: materialer, tilbud og underentreprenører til tekniske leverancer.'),
        ('Tværfaglig koordinering', 'Novo Nordisk: koordinerede 25 specialister på tværs af engineering, indkøb og anlæg og fulgte fremdrift, ressourcer og risici på 37 samtidige CAPEX-projekter.'),
        ('ERP og data', 'SAP ERP til økonomi, aktiver og omkostninger hos Novo Nordisk; Excel/Power Query og Power BI. Erfaring med SAPs produktionsplanlægningsmoduler er ikke dokumenteret.'),
        ('Forbedring og AI', 'Egne Python/Claude API-værktøjer til tilbud, tidsplaner, kvalitet og KPI hos ELOHVAC med dokumenteret produktivitetsløft over 40 %. Aktiv professionel AI-/Claude-koder, også med investeringsmodeller til nye idéer.')]: m.bullet(label, body, after=30)
    m.models_table('PLANLÆGNING OG FORBEDRING — ANVENDT I PRAKSIS', ('Område', 'Metoder og erfaring'), [
        ('Flow og prioritering', 'Tavlemøder og flaskehalsanalyse hos Ventek-Air til kapacitetsstyring og fremdrift.'),
        ('Materialer', 'Materialestyring og skiftplanlægning hos ARJ Engineering; reservedele og lagerflow hos Biofos.'),
        ('Forbedringer', 'PDCA og A3 hos Novo Nordisk; 5S og Standard Work i Biofos værksted og lager.'),
        ('Koordinering', 'Daglig planlægning og 1:1 i ELOHVAC; tværfaglig opfølgning på ressourcer og fremdrift hos Novo.')])
    m.section('UDVALGTE RESULTATER')
    for label, body in [('11 samtidige projekter', 'Kapacitetsstyring for et team på 14 hos Ventek-Air.'), ('25 specialister', 'Koordineret på tværs af engineering, indkøb og anlæg hos Novo Nordisk.'), ('40 % lavere energiomkostninger', 'Resultat af PDCA-program hos Novo Nordisk.')]: m.bullet(label, body, after=30)

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
    m.para('Dansk og persisk/farsi: modersmål · Engelsk: professionelt i skrift og tale · Kørekort B · Bopæl i Måløv. Tilstedeværelse i Faxe, opstart og overgang fra ELOHVAC aftales.', after=70)
    m.section('REFERENCER')
    m.para('Tidligere ledere hos Novo Nordisk og Biofos oplyses efter aftale.', after=70)

    m.page_break()
    m.models_table('FØRSTE 90 DAGE — FORSLAG TIL OPSTART', ('Tid', 'Handlinger og leverancer'), [
        ('Uge 1', 'Møde Supply Chain, Produktion, Lager og Customer Service. Følge en plan fra salgsprognose til levering, lære planlægningsværktøjerne og aftale prioriteringer med nærmeste leder.'),
        ('Inden dag 30', 'Kortlægge planlægningshorisonter, produktionskapacitet, råvarer og lagerdata med de ansvarlige. Sammenligne plan og faktisk udfald og identificere de mest tilbagevendende årsager til ændringer.'),
        ('Inden dag 60', 'Aftale én afgrænset forbedring med de berørte funktioner; bruge PDCA til at afprøve den i gældende processer. Afklare, hvem der beslutter ændringer og kommunikerer konsekvenser for kunderne.'),
        ('Inden dag 90', 'Følge op på forbedringen mod de aftalte mål for planernes effektivitet og leveringssikkerhed. Dokumentere læring og aftale næste skridt med teamet uden at indføre et parallelt system.')])
    m.section('SAMARBEJDE OM EN PLAN, DER KAN HOLDE')
    for label, body in [
        ('Supply Chain', 'Afstemme efterspørgsel, salgsprognoser og prioriteringer på kort og langt sigt; få usikkerheder frem, før de påvirker produktionen.'),
        ('Produktion og lager', 'Kontrollere realistisk produktionskapacitet, råvarer og lagerbeholdning med de ansvarlige. Aftale en praktisk plan og hurtigt melde ændringer tilbage.'),
        ('Customer Service', 'Afklare konsekvenser for levering og sikre, at kunderne får en sammenhængende tilbagemelding gennem de aftalte kanaler.'),
        ('Læring og koordinering', 'Bruge tydelig forventningsafstemning, tavlemøder og løbende feedback. Som specialist skaber jeg fremdrift gennem samarbejde og ansvar for egne aftaler.')]: m.bullet(label, body, after=35)
    m.section('DATA, VÆRKTØJER OG FAGLIG UDVIKLING')
    m.para('Min SAP-erfaring er fra økonomi og aktiver, ikke dokumenteret SAP-produktionsplanlægning. Jeg vil lære HARIBOs ERP-opsætning og datagrundlag sammen med de erfarne kolleger, før jeg foreslår ændringer. Erfaringen fra tekniske projekter og værksted er overførbar, men er ikke det samme som planlægningsansvar på en fødevarefabrik.', after=80)
    m.para('Som aktiv AI-/Claude-koder bygger jeg Python-værktøjer til planlægning og analyse samt investeringsmodeller med NPV, IRR og scenarier. Hos HARIBO anvendes AI og virksomhedsdata kun efter gældende regler, og analyser kontrolleres af de ansvarlige; eksisterende ERP og planlægningsprocesser er udgangspunktet.', after=80)
    m.section('FRA ÆNDRING TIL AFTALE')
    m.para('Hvis en prognose ændrer sig, vil jeg først undersøge, hvilke ordrer, råvarer og produktionsperioder der berøres. Derefter afklarer jeg med Produktion og Lager, hvilke muligheder der faktisk kan gennemføres. En aftalt beslutning, en ansvarlig og en tydelig besked til Customer Service giver alle et fælles grundlag for næste skridt.', after=80)
    m.section('FAGLIGE FOKUSOMRÅDER')
    m.para('Produktionsplanlægning · efterspørgsel · salgsprognoser · produktionsplaner · produktionskapacitet · lageroptimering · råvarer · leveringssikkerhed · Supply Chain · ERP · SAP · datadrevet analyse · løbende forbedringer', after=70)
    return m.save(path, title='Ansøgning og CV — Produktionsplanlægger, HARIBO Faxe', subject='Produktionsplanlægning, kapacitet og koordinering', keywords='produktionsplanlægning, kapacitet, supply chain, SAP, HARIBO')

if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_HARIBO_Produktionsplanlaegger.docx')))
