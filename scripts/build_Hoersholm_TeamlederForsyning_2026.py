# -*- coding: utf-8 -*-
"""Revideret dansk ansøgning og CV: Hørsholm Kommune, Team Forsyning."""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Teamleder | Spildevand, teknisk drift og udvikling'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv (Ballerup Kommune)'

def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('3. november 2026')
    m.meta('Hørsholm Kommune · Center for By og Miljø · att. centerchef Jeppe Fisker Jørgensen')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Teamleder til Team Forsyning', bold=True, color='1A1A1A')
    m.para('Et nyt forsyningsteam skal kunne holde fast i den daglige service, samtidig med at større beslutninger om spildevand og affald bevæger sig fremad. Det kræver ikke én plan oven på alle de andre, men et fælles overblik over, hvad der haster, hvem der ejer opgaven, og hvornår der skal træffes en beslutning.', after=80)
    m.para('Jeg vil begynde med at møde medarbejderne i de to grupper og forstå deres opgaver, samarbejder og faglige vurderinger. Sammen kan vi samle drift og udvikling i en overskuelig portefølje med ansvar, frister, kapacitet og afhængigheder. Den skal bruges til prioritering med centerchefen – og til at give medarbejderne arbejdsro og råderum.', after=80)
    for label, body in [
        ('Spildevand og klima', 'Sammen med teamets fagfolk og Novafos vil jeg kortlægge næste beslutninger og snitflader for separatkloakering, klimatilpasning, terrænnært grundvand og samarbejdet om vandressourcecenteret. Status og forudsætninger skal undersøges, før der lægges nye milepæle.'),
        ('Affald og borgerservice', 'Forberede udbud af affaldsindsamling med de ansvarlige specialister: behov, service, gennemsigtige priser, tidsplan og beslutningspunkter. Borgerhenvendelser og vanskelige samtaler kræver klare svar, respekt og opfølgning.'),
        ('Ledelse og samarbejde', 'Bruge 1:1, situationsbestemt ledelse og GROW til sparring og udvikling. Med tydelig delegering og fælles prioriteringer kan beslutninger træffes tæt på medarbejderne. Relationel kapacitet bliver konkret, når vi afklarer fælles sager med Plan & Byg, Vej, Park & Miljø, GIS og øvrige centre.'),
        ('Politisk beslutningsgrundlag', 'Aftale med centerchefen, hvordan faglige oplæg skal udformes. Et godt oplæg viser handlemuligheder, økonomi, konsekvenser, risici og det, der skal besluttes – og gør det muligt at omsætte beslutningen til en opgave med ejer og frist.')]:
        m.bullet(label, body, after=35)
    m.para('I den første uge vil jeg lytte og skabe overblik. Inden dag 30 skal vi have aftalt prioriteringer og mødeform; inden dag 60 skal de vigtigste samarbejdsflader og beslutningspunkter være beskrevet; inden dag 90 vil jeg følge op med teamet og justere planen sammen med centerchefen.', after=80)
    m.para('Min erfaring med spildevand kommer fra drift og vedligehold på Biofos Lynetten, kombineret med personale- og projektledelse. Jeg har ikke dokumenteret kommunal myndighedserfaring eller erfaring med affaldsudbud; her vil jeg trække på teamets og kommunens faglighed. Jeg vil gerne bidrage til et team med både faglig stolthed, en uformel tone og plads til humor.', after=80)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'LEDELSESPROFIL')
    m.para('Elautoriseret maskinmester og teknisk leder med erfaring fra spildevandsdrift, personaleledelse, entrepriser og tværfaglige projekter. Arbejder med tydelige prioriteringer og tæt sparring, så medarbejdere kan løse opgaver selvstændigt og problemer kommer frem i tide. Erfaring fra et kommunalt ejet forsyningsselskab giver indsigt i driftsopgaven; den kommunale myndighedsrolle og affaldsområdet skal læres i samarbejde med fagfolk.', after=80)
    m.section('LEDELSE OG FORSYNING I PRAKSIS')
    for label, body in [
        ('Spildevand og drift', 'Biofos Lynetten, 2017–2022: drift og vedligehold af pumper, HVAC, højspændingstavler og SCADA i et anlæg med 24/7-drift. Forebyggende vedligehold, fejlfinding og reservedelsflow.'),
        ('Personale og udvikling', 'ELOHVAC: leder fem elektrikere og tre lærlinge med opgavefordeling, 1:1, MUS og oplæring. Ventek-Air: ledede et team på 14 på 11 samtidige projekter.'),
        ('Opgaver på tværs', 'Novo Nordisk: koordinerede 25 specialister på tværs af engineering, indkøb og anlæg på 37 samtidige CAPEX-projekter; fulgte fremdrift, økonomi, ressourcer og risici.'),
        ('Aftaler og økonomi', 'ELOHVAC: fuldt P&L-ansvar, tilbud, leverandører og kundeaftaler. Ventek-Air: udbud og tilbud, underentreprenører og aftalegrundlag i tekniske projekter.'),
        ('Forbedring og digitalisering', 'PDCA-program hos Novo reducerede energiomkostninger 40 %. Som aktiv AI-/Claude-koder bygger jeg Python/Claude API-værktøjer til planlægning, kvalitet og KPI; produktivitetsløft over 40 % i ELOHVAC.')]:
        m.bullet(label, body, after=30)
    m.models_table('LEDELSESVÆRKTØJER — ERFARING', ('Område', 'Værktøjer anvendt i praksis'), [
        ('Mennesker', 'Situationsbestemt ledelse, 1:1, MUS og struktureret lærlingeoplæring i ELOHVAC.'),
        ('Fremdrift', 'Daglige tavlemøder og flaskehalsanalyse hos Ventek-Air til kapacitet og prioritering.'),
        ('Forbedring', '5S, Standard Work og PDCA hos Biofos; PDCA, A3 og rodårsagsanalyse hos Novo.'),
        ('Sikkerhed', 'LOTO, APV og risikovurdering på tekniske opgaver hos Biofos og ELOHVAC.')])
    m.section('UDVALGTE RESULTATER')
    for label, body in [
        ('14 medarbejdere og 11 projekter', 'Daglig ledelse og kapacitetsstyring hos Ventek-Air.'),
        ('25 specialister og 37 projekter', 'Tværfaglig koordinering hos Novo Nordisk; nul kritiske afvigelser ved aflevering.'),
        ('40 % lavere energiomkostninger', 'Dokumenteret forbedring via PDCA-program hos Novo Nordisk.')]: m.bullet(label, body, after=30)

    m.page_break()
    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør / elautoriseret maskinmester', 'ELOHVAC ApS · København · maj 2023–nu', '5 elektrikere og 3 lærlinge · fuldt P&L', [
            ('Medarbejdere og kunder', 'Daglig planlægning, 1:1, MUS og oplæring. Tilbud, serviceaftaler, materialer og underentreprenører samt kvalitets- og afleveringsdokumentation.'),
            ('Digital udvikling', 'Python/Claude API-værktøjer til tilbud, tidsplaner, kvalitet og KPI-opfølgning; over 40 % produktivitetsløft i virksomheden.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem', 'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024', '37 samtidige CAPEX-projekter · 25 specialister · 2–10 mio. kr. pr. projekt', [
            ('Plan og koordinering', 'Fulgte økonomi, fremdrift, ressourcer og risici mellem engineering, indkøb og anlæg; rapporterede til ledelse og bygherre.'),
            ('Kvalitet og forbedring', 'FAT/SAT og IQ/OQ/PQ i GMP-regulerede projekter uden kritiske fund ved aflevering. PDCA-program reducerede energiomkostninger med 40 %.')]),
        ('Projekt- og værkstedsleder', 'Ventek-Air · København · jan. 2022–nov. 2022', '14 medarbejdere · 11 samtidige anlægsprojekter', [
            ('Ledelse og leverancer', 'Kapacitetsstyring, udbud og tilbud, underentreprenører, sikkerhedsdokumentation og aflevering. Tavlemøder og flaskehalsanalyse understøttede bedre levering.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker', 'Biofos, Lynetten · København · aug. 2017–jan. 2022', 'Spildevandsanlæg · kritisk el- og mekanisk drift · 24/7', [
            ('Drift og sikkerhed', 'Forebyggende vedligehold og akut fejlfinding på pumper, HVAC, højspændingstavler og SCADA. 5S, Standard Work, PDCA, LOTO og risikovurdering.')]),
        ('Elektromekaniker / produktionsteamleder', 'ARJ Engineering · Teheran · dec. 2003–mar. 2010', '12 mekanikere og teknikere', [
            ('Team og værksted', 'Vagtplanlægning, materialestyring og målopfølgning samt fejldiagnose og reparation af industrielle el- og mekaniske anlæg.')])]
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
    m.para('Dansk og persisk/farsi: modersmål · Engelsk: professionelt · Kørekort B · Bopæl i Måløv. Tiltrædelse og overgang fra ELOHVAC aftales.', after=70)
    m.section('REFERENCER')
    m.para('Tidligere ledere hos Biofos og Novo Nordisk oplyses efter aftale.', after=70)

    m.page_break()
    m.models_table('FØRSTE 90 DAGE — ET FORSLAG', ('Tid', 'Handlinger og leverancer'), [
        ('Uge 1', 'Møde medarbejderne i Spildevand og Affald, centerchefen og nøglepersoner i centret. Lytte til aktuelle sager, frister, borgerhenvendelser og samarbejdet med Novafos; aftale beslutningsrum.'),
        ('Inden dag 30', 'Sammen med teamet skabe et samlet overblik over drift, udviklingsopgaver, ejere, frister og belastning. Aftale 1:1-samtaler, faglig sparring og en fast, kort prioritering med centerchefen.'),
        ('Inden dag 60', 'Gennemgå næste beslutninger om spildevand, terrænnært grundvand og affaldsudbud med fagfolk og samarbejdspartnere. Afklare snitflader til andre teams, GIS, Novafos og nabokommuner.'),
        ('Inden dag 90', 'Følge op på fremdrift og samarbejde med de to grupper. Forelægge centerchefen en justeret prioritering med ansvar, tidsplan, risici og eventuelle behov for politiske beslutninger.')])
    m.section('SÅDAN SKABES SAMMENHÆNG')
    for label, body in [
        ('Tillidsbaseret ledelse', 'Aftal tydelige rammer og giv fagpersoner ansvar for løsningerne. Brug 1:1, GROW og situationsbestemt ledelse til at støtte, udfordre og følge op uden at overtage arbejdet.'),
        ('Relationel kapacitet', 'Mød de andre teams om de sager, der krydser faggrænser. Afklar fælles mål, hvem der gør hvad, og hvordan uenighed håndteres; følg aftaler op i stedet for at sende dem videre.'),
        ('Borgere og samarbejdspartnere', 'Lyt til behov og bekymringer, giv et klart svar eller en realistisk tilbagemeldingstid, og sørg for, at sagerne når den rette fagperson. Samarbejd respektfuldt med indsamlere, forsyninger og nabokommuner.'),
        ('Politisk proces', 'Lad fagfolk kvalificere alternativer og konsekvenser, inden et oplæg sendes videre efter kommunens procedurer. Hold faglig anbefaling, politisk beslutning og den efterfølgende gennemførelse adskilt.')]: m.bullet(label, body, after=35)
    m.section('DIGITALT OVERBLIK OG LÆRING')
    m.para('Som professionel og aktiv AI-/Claude-koder bruger jeg Python og Claude til egne planlægnings- og analyseværktøjer samt investeringsmodeller med NPV, IRR og scenarier. I kommunen vil enhver brug af AI kræve godkendte løsninger, sikker behandling af borgerdata og menneskelig kontrol; ingen oplysninger lægges i eksterne værktøjer uden tilladelse.', after=80)
    m.para('Mine erfaringer fra Biofos er driftsnære og tekniske. For lovgivning, myndighedsopgaver og affaldsudbud vil jeg lære kommunens praksis af de ansvarlige specialister og sikre, at forslag bliver fagligt og juridisk kvalificeret.', after=80)
    m.section('FRA BESLUTNING TIL BORGER')
    m.para('Når en politisk beslutning er truffet, skal teamet kunne se, hvem der gør hvad, hvilken tidsfrist der gælder, og hvem der orienterer berørte borgere og samarbejdspartnere. Jeg vil bruge en enkel beslutningslog og følge op på eventuelle nye afklaringer med centerchefen. Det giver medarbejderne et fælles grundlag og gør det lettere at vende tilbage til borgerne med et præcist svar.', after=80)
    m.para('For det kommende udbud vil jeg bede affaldsgruppen og kommunens udbudsfaglige kolleger gennemgå den nuværende aftale, brugerbehov og tidsplan, før vi fastlægger nye løsninger. Service, sortering, genbrug, genanvendelse, pris og risici skal belyses i sammenhæng, og de relevante beslutninger skal forankres i den gældende proces.', after=80)
    m.section('FAGLIGE FOKUSOMRÅDER')
    m.para('Spildevand · affald · separatkloakering · klimatilpasning · terrænnært grundvand · vandressourcecenter · personaleledelse · portefølje · prioritering · politiske beslutningsoplæg · borgerdialog · Novafos · samarbejde på tværs', after=70)
    return m.save(path, title='Ansøgning og CV — Teamleder Team Forsyning, Hørsholm Kommune', subject='Ledelse, spildevand og affald', keywords='teamleder, forsyning, spildevand, affald, ledelse')

if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Hoersholm_TeamlederForsyning_2026.docx')))
