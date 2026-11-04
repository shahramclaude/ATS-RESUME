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
    m.para('Til Julie Josefine Feddersen', after=70)
    m.para('Når et specialistteam arbejder på flere projekter inden for jernbane samtidig, kræver gode leverancer mere end en plan. Medarbejderne skal vide, hvad der er vigtigst, projektlederne skal kende kapaciteten, og kunden skal have svar, der er både gennemarbejdede og rettidige. Det er i den sammenhæng, jeg ser værdien af en teamleder, der er tæt på opgaverne og tydelig om beslutningerne.', after=80)
    m.para('Mit udgangspunkt vil være et kort ugentligt overblik over leverancer, bemanding og åbne beslutninger. Sammen med medarbejdere og projektledere vil jeg afklare, hvor opgaverne presser hinanden, og hvad en ændring betyder for kvalitet, tid og økonomi. Når prioriteringerne er aftalt, skal teamet have arbejdsro — og kunden en klar tilbagemelding.', after=80)
    m.para('Samtidig skal den enkelte have plads til at udvikle sin faglighed. Jeg bruger 1:1 og MUS til at følge op på trivsel, forventninger og udvikling; situationsbestemt ledelse hjælper mig med at tilpasse støtte og ansvar til den enkelte. Mellem København og Aarhus vil jeg skabe en fast anledning til faglig sparring om løsninger og erfaringer på tværs af projekterne.', after=80)
    m.para('Den arbejdsform bygger på konkret erfaring. Hos ELOHVAC leder jeg fem elektrikere og tre lærlinge og har ansvar for økonomi og tekniske leverancer. Hos Ventek-Air styrede jeg kapaciteten for 14 medarbejdere og 11 projekter; hos Novo Nordisk koordinerede jeg 25 specialister og fulgte økonomi og fremdrift i 37 tekniske CAPEX-projekter.', after=80)
    m.para('Jeg er elautoriseret maskinmester med erfaring i el, mekanik og teknisk projektledelse. Min baggrund omfatter ikke dokumenteret sporprojektering, baneafvanding eller CAD og 3D-modellering på sporområdet. Da stillingen indebærer fagligt ansvar for spor, vil jeg gerne afklare med jer, om min profil er relevant for netop dette ansvar, eller om mine styrker passer bedre til en anden rolle hos SYSTRA.', after=80)
    m.para('Jeg vil gerne uddybe, hvordan jeg arbejder med mennesker, prioriteringer og kvalitet — og høre mere om det faglige mandat i Spor og Anlæg.', after=80)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Elautoriseret maskinmester og teknisk leder med ansvar for mennesker, projekter og økonomi. Jeg samler specialister om klare prioriteringer, følger leverancer tæt og skaber plads til faglig sparring. Min erfaring spænder fra daglig personaleledelse og entrepriser til koordinering af komplekse tekniske CAPEX-projekter.', after=80)
    m.section('LEDERPROFIL — ANSVAR OG RESULTATER')
    for label, body in [
        ('Mennesker og udvikling', 'Leder fem elektrikere og tre lærlinge hos ELOHVAC. Fordeler opgaver, gennemfører 1:1 og MUS og følger op på oplæring og arbejdsmiljø. Tidligere leder for 14 medarbejdere hos Ventek-Air.'),
        ('Projektportefølje', 'Koordinerede 25 specialister i engineering, indkøb og anlæg hos Novo Nordisk. Fulgte ressourcer, risiko, økonomi og fremdrift på 37 samtidige CAPEX-projekter til 2–10 mio. kr. pr. projekt.'),
        ('Kapacitet og leverance', 'Planlagde 11 samtidige tekniske projekter hos Ventek-Air fra specifikation til aflevering. Tavlemøder og flaskehalsanalyse gjorde prioriteringerne synlige og understøttede leveringsevnen.'),
        ('Kvalitet og økonomi', 'Har fuldt P&L-ansvar hos ELOHVAC. Hos Novo omfattede leverancerne FAT/SAT og IQ/OQ/PQ uden kritiske afvigelser ved aflevering; et PDCA-program reducerede energiomkostningerne med 40 %.'),
        ('Digital udvikling', 'Aktiv professionel AI- og Claude-koder. Har udviklet Python/Claude API-værktøjer til tilbud, tidsplaner, kvalitet og KPI hos ELOHVAC med et dokumenteret produktivitetsløft på over 40 %. Bygger også investeringsmodeller til udvikling og nye forretningsidéer.')]: m.bullet(label, body, after=30)
    m.models_table('LEDELSESVÆRKTØJER', ('Opgave', 'Praktisk anvendelse'), [
        ('Udvikle medarbejdere', 'Situationsbestemt ledelse, 1:1, MUS og struktureret oplæring hos ELOHVAC.'),
        ('Prioritere arbejdet', 'Daglige tavlemøder og flaskehalsanalyse til kapacitetsstyring hos Ventek-Air.'),
        ('Lære af afvigelser', 'PDCA, A3, 5 x hvorfor og Ishikawa hos Novo; 5S og Standard Work hos Biofos.'),
        ('Arbejde sikkert', 'APV, LOTO og risikovurdering ved teknisk drift og pladsopstart.')])
    m.section('FAGLIGT UDGANGSPUNKT')
    m.para('El, mekanik, driftskritiske anlæg og teknisk idriftsættelse. B.Tech i Technology Management & Mechanical Engineering, maskinmesterretningen.', after=70)
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
    m.models_table('FØRSTE 90 DAGE — FORSLAG TIL OPSTART', ('Periode', 'Leverance og opfølgning'), [
        ('Uge 1', 'Møde de fem medarbejdere, afdelingslederen og teamlederen i Aarhus. Gennemgå de aktuelle leverancer og aftale mandat, fagligt ansvar og kvalitetssikring med afdelingslederen.'),
        ('Dag 30', 'Afslutte individuelle 1:1 og samle et overblik over projekter, frister, kapacitet og kompetencer. Aftale en fast prioriteringsrytme med teamet og projektlederne.'),
        ('Dag 60', 'Følge op på belastning, leverancefrister og åbne kvalitets- og kundeafklaringer med projektlederne. Sammen med teamet vælge ét område, hvor koordinering eller videndeling kan forbedres.'),
        ('Dag 90', 'Evaluere prioriteringer, samarbejde og trivsel med medarbejderne og afdelingslederen. Fremlægge en kort status på leverancer, kapacitet og aftalte udviklingstiltag.')])
    m.section('ET KONKRET GREB OM OPGAVEN')
    for label, body in [
        ('Fælles prioritering', 'En oversigt viser opgave, projektleder, ansvarlig, frist, kapacitet og næste beslutning. Ændringer drøftes med de berørte, inden en ny prioritering meldes ud.'),
        ('Kvalitet og kunder', 'Leverancens omfang og review aftales fra start. Åbne faglige spørgsmål og deres konsekvenser for tid og økonomi løftes hurtigt til rette beslutningstager.'),
        ('Udvikling og samarbejde', '1:1 og MUS omsættes til konkrete udviklingsaftaler. Faglig sparring på tværs af København og Aarhus kan gøre viden mere tilgængelig og styrke samarbejdet.'),
        ('Løbende forbedring', 'Ved gentagne afvigelser kan teamet bruge PDCA og årsagsanalyse til at afprøve en forbedring og følge op på, om den virker.')]: m.bullet(label, body, after=35)
    m.section('DIGITALT ARBEJDE MED ET KLART FORMÅL')
    m.para('Jeg udvikler værktøjer i Python og Claude til planlægning, kvalitet og analyse samt investeringsmodeller med NPV, IRR og scenarier. I en rådgivningsorganisation kan automatisering frigøre tid fra rutineopfølgning til faglig dialog. Det forudsætter godkendte systemer og data, menneskelig kontrol og respekt for virksomhedens kvalitetssystem.', after=80)
    m.section('SAMARBEJDE, NÅR PLANEN ÆNDRER SIG')
    m.para('Hvis en ny hasteopgave påvirker et igangværende projekt, skal konsekvenserne frem i lyset: Hvilken leverance berøres, hvilke kompetencer er til rådighed, og hvilken beslutning har projektlederen brug for? Et kort møde med de involverede og en tydelig aftale om ansvar, frist og tilbagemelding skaber ro og et fælles grundlag for kunden.', after=80)
    return m.save(path, title='Ansøgning og CV — Teamleder Spor og Anlæg, SYSTRA', subject='Teknisk ledelse og projektkoordinering', keywords='teamleder, projektledelse, kvalitet, SYSTRA')

if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_SYSTRA_TeamlederSporOgAnlaeg.docx')))
