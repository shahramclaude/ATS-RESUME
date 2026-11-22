# -*- coding: utf-8 -*-
"""Georg Fischer A/S — Danish application and evidence-led CV."""
import os
import sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
from master_design import MasterDoc

NAME = 'SHAHRAM AJLOO'
TITLE = 'Elautoriseret maskinmester | Tekniske projekter, support og koordinering'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('3. november 2026 · Georg Fischer A/S · Technical Manager og Projects · Trekroner/Roskilde')
    p = m._p(spacing_after=70, line=260, justify=False)
    m._run(p, 'Ansøgning — teknisk projektstyring med tydelige snitflader', bold=True, color='1A1A1A')

    m.para('Når tekniske projekter spænder over salg, kunder og rådgivere, interne specialister og et internationalt hovedkontor, er fremdrift afhængig af mere end en tidsplan. Der skal være fælles forståelse af scope, tekniske forudsætninger, beslutninger, risici og næste ansvarlige — fra den første afklaring til overdragelsen, så projektfremdrift ikke bygger på skjulte antagelser.', after=60)
    m.para('Hos GF er denne koordinering tæt knyttet til et bredt flow-solutionssortiment: plast- og metalbaserede rørsystemer og fittings, ventiler, aktuatorer, måling og automation. Samtidig peger GF’s Strategy 2030 på nye applikationer, direkte-til-chip-køling og en “One GF”-arbejdskultur. Det gør præcis teknisk afklaring og samarbejde på tværs afgørende, når løsninger skal omsættes til brugbare projektbeslutninger.', after=60)

    m.section('EN PRAKTISK LEVERANCEMODEL FOR ROLLEN')
    for label, body in [
        ('Ét fælles projektbillede', 'Etablér ved opstart en kort projektoversigt med scope, kundens behov, tekniske antagelser, milepæle, beslutninger, risici, afhængigheder og navngivne ejere. Brug en fast opfølgningsrytme, så forsinkelser og afklaringer kommer frem, mens der stadig er handlemuligheder.'),
        ('Klar teknisk afklaring', 'Saml spørgsmål fra salg, kunde og rådgivere i en sporbar afklaringsliste. Indhent input fra de relevante produkt- og teknikspecialister; dokumentér beregningsforudsætninger, åbne punkter og godkendelser, før løsning og levering låses.'),
        ('Sammenhængende snitflader', 'Aftal hvem der beslutter, leverer og informeres i hver fase. Overdrag korte beslutningsnotater til Swiss HQ og tilbage til lokale projektparter på engelsk, så ændringer i krav, tidsplan eller produktvalg ikke forsvinder mellem funktionerne.'),
        ('Support, læring og forbedring', 'Registrér gentagne tekniske spørgsmål, afvigelser og løsningsvalg; brug dem til at forbedre svargrundlag, dokumentation og næste projekts opstart. Nye produkter og metoder indarbejdes med målrettet sparring og verificering hos de relevante specialister.')]:
        m.bullet(label, body, after=35, line=245)

    m.para('I de første 30 dage bør rolle, beslutningsveje, igangværende projekter og de vigtigste produkt-/kundesnitflader kortlægges sammen med teamet. Inden dag 60 kan en fælles status- og risikorytme være afprøvet på udvalgte sager; inden dag 90 kan erfaringerne omsættes til en enkel, fælles projektstandard med tydelige ejere og overdragelsespunkter. Tempo og indhold fastlægges efter GF’s eksisterende praksis — ikke som en parallel proces.', after=60)
    m.para('GF beskriver sin kultur gennem “Performance”, “Learning” og “Caring”, og sin retning som “One GF”. Den foreslåede arbejdsform kobler eksekvering og læring med samarbejde på tværs: synlig fremdrift, åbne tekniske afklaringer og fælles ansvar for den løsning, kunden modtager.', after=60)
    m.meta('Med venlig hilsen', after=10)
    m.meta('Shahram Ajloo', after=0)

    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Elautoriseret maskinmester med baggrund i teknisk projektlevering, idriftsættelse, industriel drift og kundevendte tekniske installationer. Har koordineret en portefølje på 37 samtidige CAPEX-projekter og fulgt økonomi, risiko, ressourcer og fremdrift på tværs af engineering, indkøb og anlæg. Erfaringen omfatter også teknisk tilbudsarbejde, beregninger, SAP ERP samt Excel/Power Query. Har bekræftet erfaring med plastbaserede rørsystemer og datacenterkøling; disse erfaringer beskrives på overordnet niveau, da konkrete systemer og personlige projektopgaver endnu ikke er specificeret.', after=55)

    m.section('FAGLIGT MATCH — DOKUMENTATION OG AFGRÆNSNING')
    matrix = [
        ('Teknisk projektkoordinering og fremdrift', 'Hos Novo Nordisk fulgte jeg 37 samtidige CAPEX-projekter på 2–10 mio. kr. pr. projekt med fokus på fremdrift, økonomi, risici og ressourcer. Koordineringen omfattede 25 specialister og snitflader til engineering, indkøb og anlæg.'),
        ('Salg, kunder, rådgivere, tekniske teams og Swiss HQ', 'ELOHVAC- og Ventek-Air-rollerne omfatter kunder, tilbud, underentreprenører og tekniske leverancer; Novo Nordisk omfattede tværfaglig koordinering. Direkte erfaring med GF’s Swiss HQ er ikke oplyst; flydende engelsk er bekræftet.'),
        ('Teknisk support', 'ELOHVAC omfatter tekniske kundeleverancer, fejlfinding, tilbud og aflevering på el-, ventilations- og klimaanlæg. Hos Biofos indgik akut fejlfinding og forebyggende vedligehold på pumper, HVAC, højspændingstavler og SCADA i døgnkritisk drift.'),
        ('Rørsystemer, ventiler, aktuatorer og reguleringskredse', 'Kandidaten har bekræftet direkte erfaring med plastrørsystemer, men har endnu ikke specificeret systemer, komponenter eller opgaver. Erfaring med datacenterkøling er ligeledes bekræftet på overordnet niveau; bestemte ventiler, aktuatorer eller reguleringskredse tilskrives ikke.'),
        ('Tekniske beregninger', 'Selvstændigt udførte tekniske beregninger er bekræftet. Master-CV’et dokumenterer tilbudsberegning samt beregning og dimensionering i teknisk arbejde; et konkret beregningseksempel, metode, input og output er ikke specificeret.'),
        ('SAP', 'SAP ERP blev anvendt hos Novo Nordisk til økonomi, aktiver og omkostninger; projektøkonomi blev fulgt på tværs af en portefølje på 37 samtidige CAPEX-projekter. SAP-moduler og konkrete transaktionskoder er ikke oplyst.'),
        ('Stærk Excel', 'Stærke Excel-kompetencer er bekræftet; master-CV’et anfører Excel og Power Query. Konkrete modeller, formler eller automatiseringsfunktioner er ikke specificeret, så der nævnes ingen bestemte Excel-funktioner.'),
        ('Flydende engelsk', 'Kandidaten har bekræftet flydende engelsk i tale og skrift. Det understøtter den internationale kommunikation, som rollen kræver; tidligere samarbejde med GF’s schweiziske hovedkontor er ikke påstået.'),
        ('Tysk som fordel', 'Tysk er ikke et arbejdssprog for kandidaten. Dansk og engelsk er flydende, og persisk/farsi er modersmål; der fremsættes derfor ikke et tyskkompetencekrav på kandidatens vegne.'),
        ('Plastrørsystemer', 'Direkte erfaring med plastrørsystemer er bekræftet. Systemtype, materiale, brand, anvendelse, arbejdsgiver og konkret ansvar skal afklares, før CV’et kan gå i detaljer; der opfindes derfor ingen produktspecifik erfaring.'),
        ('Køling til datacentre', 'Direkte erfaring med køling til datacentre er bekræftet. Projekt, køleteknisk løsning, komponenter, omfang og kandidatens konkrete opgaver er ikke specificeret og fremstilles derfor ikke mere detaljeret.'),
        ('Nye produkter og metoder', 'Erfaring på tværs af industrielle anlæg, tekniske installationer, projektlevering og teknisk support giver et relevant grundlag for produktlæring. GF-specifik produktviden og eventuel oplæring er et fremadrettet fokus, ikke en tidligere GF-erfaring.'),
        ('Trekroner/Roskilde', 'Kandidaten har bekræftet mulighed for at arbejde fra GF’s kontor i Roskilde/Trekroner. Bopæl i Måløv og kørekort B fremgår af master-CV’et; konkrete fremmødedage er ikke aftalt.')]
    m.models_table('RELEVANS OG DOKUMENTATION', ('Krav i stillingsopslaget', 'Dokumentation og relevans'), matrix,
                   widths=(2550, 7796), compact=True)
    m.models_table('UDVALGTE PROJEKT- OG SAMARBEJDSMETODER', ('Område', 'Dokumenteret anvendelse'), [
        ('Projektstyring', 'Fremdrift, ressourcer, risiko og økonomi på tværs af 37 CAPEX-projekter hos Novo Nordisk; 11 samtidige projekter fra specifikation til aflevering hos Ventek-Air.'),
        ('Teknisk kvalitet', 'FAT/SAT, IQ/OQ/PQ og afleveringsdokumentation hos Novo Nordisk; KS og dokumentationspakker i ELOHVAC- og Ventek-Air-leverancer.'),
        ('Forbedringsarbejde', 'PDCA hos Novo Nordisk og Biofos; 5S, Standard Work, A3, 5xHvorfor og Ishikawa anvendt i praksis. Lean-/Six Sigma-praksis, ikke certificeret.'),
        ('Digitale værktøjer', 'SAP ERP til økonomi/aktiver/omkostninger; Excel/Power Query, Power BI, Python og Claude API. Ingen SAP-moduler eller konkrete Excel-formler er angivet.')], compact=True)

    m.page_break()
    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør / elautoriseret maskinmester', 'ELOHVAC ApS · København · maj 2023–nu', '5 elektrikere + 3 lærlinge · fuldt P&L-ansvar', [
            ('Tekniske leverancer', 'El-tekniske opgaver for erhvervskunder på el-, ventilations- og klimaanlæg: installation, tavler, styring, fejlfinding og forebyggende vedligehold.'),
            ('Projekt og kundedialog', 'Tilbud og beregninger, planlægning, materialestyring, underentreprenører, kvalitetssikring og afleveringsdokumentation; fuldt ansvar for virksomhedens P&L.'),
            ('Værktøjer og forbedring', 'Python-/Claude API-værktøjer til tilbud, tidsplaner, KS-tjeklister og KPI-dashboards med dokumenteret produktivitetsløft over 40 %.')]),
        ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen', 'Data Power Consultant ApS · København · 2024–nov. 2026 (sideløbende)', '4–10 personer', [
            ('Kundeløsninger', 'Ledte tekniske og industrielle applikationer fra kravafdækning og integration til idriftsættelse, dokumentation og overdragelse.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem', 'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024', '37 samtidige CAPEX-projekter · 25 specialister · 2–10 mio. kr. pr. projekt', [
            ('Portefølje og opfølgning', 'Koordinerede engineering, indkøb og anlæg; fulgte fremdrift, økonomi, risici og ressourcer og rapporterede månedligt til ledelse og bygherre.'),
            ('Teknik og aflevering', 'Elektriske anlæg, tavler, styring og UPS; FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA uden kritiske afvigelser ved aflevering. SAP ERP til økonomi, aktiver og omkostninger.'),
            ('Energiresultat', 'Et PDCA-program reducerede energiomkostninger med 40 %.')]),
        ('Projekt- og værkstedsleder', 'Ventek-Air · København · jan. 2022–nov. 2022', '14-personers team · 11 samtidige anlægsprojekter', [
            ('Fra specifikation til aflevering', 'Stod for kapacitets- og fremdriftsstyring, tilbud/udbud, underentreprenører, aftalegrundlag, sikkerhedsdokumentation og afleveringspakker; anvendte daglige tavlemøder og flaskehalsanalyser.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker', 'Biofos (Lynetten) · København · aug. 2017–jan. 2022', 'Kritisk 24/7-drift', [
            ('Drift og fejlfinding', 'Forebyggende vedligehold og akut fejlfinding på pumper, HVAC, højspændingstavler og SCADA; arbejdede med 5S, Standard Work, PDCA og reservedelsflow.')]),
        ('Elektromekaniker / produktionsteamleder', 'ARJ Engineering · Teheran · dec. 2003–mar. 2010', '12 mekanikere og teknikere', [
            ('Industriel teknik og ledelse', 'Fejldiagnose og reparation af industrielt el- og mekanisk udstyr samt vagtplanlægning, materialestyring, målopfølgning og korrigerende handlinger.')])]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=18, line=240)

    m.section('UDDANNELSE, CERTIFICERING OG SPROG')
    for title, meta in [
        ('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023'),
        ('B.Tech, Technology Management & Mechanical Engineering', 'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · EQF 6'),
        ('El- og maskinteknisk design, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6'),
        ('PRINCE2-certificeret projektleder', 'AXELOS / PeopleCert'),
        ('Køleteknik og klimaanlæg', 'AMU · Mercantec · 2021')]:
        m.edu(title, meta)
    m.para('Sprog: dansk og persisk/farsi — modersmål · engelsk — flydende i tale og skrift · tysk — ingen arbejdskompetence. Kørekort B. Bopæl i Måløv; fremmøde i Trekroner/Roskilde er bekræftet.', after=50)
    return m.save(path, title='Ansøgning og CV — Georg Fischer A/S Technical Manager og Projects',
                  subject='Teknisk projektkoordinering, support og tekniske løsninger',
                  keywords='Technical Manager og Projects, plastbaserede rørsystemer, datacenterkøling, SAP ERP, Excel, tekniske beregninger, projektkoordinering')


if __name__ == '__main__':
    output = os.path.join(ROOT, 'Shahram_Ajloo_GeorgFischer_TechnicalManagerProjects.docx')
    print(build(output))
