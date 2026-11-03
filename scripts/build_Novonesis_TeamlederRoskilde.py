# -*- coding: utf-8 -*-
"""Novonesis Roskilde JR113971: dansk ansøgning og CV i masterdesign."""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Teamleder | Mennesker, sikker drift og løbende forbedringer'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv (Ballerup Kommune)'

def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('3. november 2026')
    m.meta('Novonesis · Manufacturing site Roskilde · att. Pernille Bech Daugaard')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Teamleder til manufacturing site Roskilde · JR113971', bold=True, color='1A1A1A')
    m.para('Stabil produktion af bakteriekulturer kræver, at mennesker, instruktioner og udstyr spiller sammen på både dag- og aftenhold. Når en teamleder er tæt på hverdagen, er det lettere at opdage en udfordring tidligt, få den rette hjælp ind og holde fast i kvalitet og sikkerhed, også når planen ændrer sig.', after=80)
    m.para('Jeg vil begynde med at lære operatørerne og deres arbejdsgange at kende sammen med de øvrige teamledere og supportteamet. På den baggrund kan vi samle et enkelt overblik over bemanding, kompetencer, træning og åbne driftsproblemer. Det skal være et redskab for holdet – ikke et ekstra lag papir.', after=80)
    for label, body in [
        ('Mennesker og retning', 'Aftale korte 1:1-samtaler, tydelige forventninger og løbende feedback. Med situationsbestemt ledelse og GROW kan støtte og ansvar tilpasses den enkelte, mens medarbejderne inddrages i løsningerne.'),
        ('Stabil drift og oplæring', 'Gennemgå vagtplanlægning og overlevering mellem dag og aften med holdet. Aftale en kompetencematrice og træningsplan med relevante oplærere, så bemandingen passer til de opgaver, medarbejderne er kvalificeret til.'),
        ('Kvalitet og forbedring', 'Følge gældende arbejdsinstruktioner, GMP, hygiejne og sikkerhed. Bruge tavlemøder, PDCA og A3 til at undersøge årsager til spild eller udsving i udbytte sammen med operatører og support – og afprøve ændringer inden for de godkendte rammer.'),
        ('Fælles kultur', 'Omsætte Novonesis’ Culture Commitments – Explore, Impact, Ownership og Care til nysgerrige spørgsmål, klare aftaler, ansvar for opfølgning og respekt for hinandens faglighed. En god idé skal både kunne siges højt og følges til dørs.')]:
        m.bullet(label, body, after=35)
    m.para('I den første uge vil jeg lytte og gennemgå de vigtigste instruktioner. Inden dag 30 skal bemanding, træning og de største driftsrisici være synlige; inden dag 60 vil jeg sammen med teamet følge op på et afgrænset forbedringsforslag, og inden dag 90 evaluere effekten med lederteamet.', after=80)
    m.para('Min erfaring kommer fra teknisk drift, personaleledelse og GMP-regulerede projekter – ikke fra selv at lede fermentering eller frysetørring. Jeg vil derfor lære processerne af operatørerne og de fagligt ansvarlige, før jeg ændrer noget. Jeg vil gerne være med til at skabe en hverdag i Roskilde, hvor holdet lykkes sammen og kvaliteten kan mærkes i det daglige arbejde.', after=80)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL OG MOTIVATION')
    m.para('Jeg søger rollen, fordi kombinationen af nærværende personaleledelse, stabil produktion og udvikling af arbejdsgange giver mening for mig. Jeg vil være en synlig leder for holdet og samarbejde med operatører og support om sikkerhed, kvalitet og forbedringer. Jeg er elautoriseret maskinmester med erfaring fra teknisk drift, personalelederansvar og projekter i GMP-regulerede omgivelser.', after=80)
    m.section('LEDELSE OG DRIFT I PRAKSIS')
    for label, body in [
        ('Personaleledelse og oplæring', 'ELOHVAC: leder fem elektrikere og tre lærlinge med daglig planlægning, 1:1, MUS og struktureret oplæring. Tilpasser støtte og ansvar til medarbejderens erfaring.'),
        ('Bemanding og fremdrift', 'Ventek-Air: ledede et team på 14 på tværs af 11 samtidige projekter. Daglige tavlemøder og flaskehalsanalyser gav grundlag for kapacitetsstyring og bedre levering.'),
        ('GMP og dokumentation', 'Novo Nordisk: FAT/SAT og IQ/OQ/PQ for eltekniske anlæg i GMP-regulerede projekter; ingen kritiske afvigelser ved aflevering. Erfaringen er fra idriftsættelse, ikke operatøransvar for bakteriekulturer.'),
        ('Sikkerhed og standarder', 'Biofos: forebyggende vedligehold og fejlfinding i 24/7-drift; 5S, Standard Work og PDCA i værksted og lager samt LOTO, APV og opfølgning på nærved-hændelser.'),
        ('Løbende forbedring', 'Novo Nordisk: PDCA-program med 40 % lavere energiomkostninger. ELOHVAC: egne Python/Claude API-værktøjer til planlægning og KPI-opfølgning med dokumenteret produktivitetsløft over 40 %.')]:
        m.bullet(label, body, after=30)
    m.models_table('LEDELSESVÆRKTØJER — ANVENDT I PRAKSIS', ('Område', 'Værktøjer og erfaring'), [
        ('Personer og udvikling', 'Situationsbestemt ledelse, 1:1 og MUS hos ELOHVAC; daglig sparring og struktureret oplæring af lærlinge.'),
        ('Fælles overblik', 'Daglige tavlemøder og flaskehalsanalyse hos Ventek-Air; prioritering af mandskab og opgaver.'),
        ('Forbedringer', 'PDCA, A3 og rodårsagsanalyse hos Novo Nordisk; 5S og Standard Work hos Biofos.'),
        ('Sikkerhed', 'LOTO, APV og risikovurdering hos ELOHVAC og Biofos; åben opfølgning på forhold, der kræver handling.')])
    m.section('UDVALGTE RESULTATER')
    for label, body in [('14 medarbejdere og 11 projekter', 'Ledelse og kapacitetsstyring hos Ventek-Air fra specifikation til aflevering.'), ('25 specialister på tværs af fag', 'Koordinering mellem engineering, indkøb og anlæg hos Novo Nordisk.'), ('40 % lavere energiomkostninger', 'Resultat af et PDCA-forbedringsprogram hos Novo Nordisk.')]:
        m.bullet(label, body, after=30)

    m.page_break()
    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør / elautoriseret maskinmester', 'ELOHVAC ApS · København · maj 2023–nu', '5 elektrikere og 3 lærlinge · fuldt P&L-ansvar', [
            ('Mennesker og opgaver', 'Daglig planlægning, 1:1, MUS og oplæring. Risikovurdering og LOTO; ingen kritiske afvigelser i serviceaftalerne.'),
            ('Drift og forbedring', 'El-, ventilations- og klimaanlæg, materialer og underentreprenører. Udviklede Python/Claude API-værktøjer til tilbud, tidsplaner, KS og KPI med over 40 % produktivitetsløft.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem', 'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024', '37 samtidige CAPEX-projekter · 25 tværfaglige specialister · 2–10 mio. kr. pr. projekt', [
            ('Koordinering', 'Fulgte fremdrift, økonomi, ressourcer og risici på tværs af engineering, indkøb og anlæg; rapporterede til ledelse og bygherre.'),
            ('GMP og forbedring', 'FAT/SAT og IQ/OQ/PQ i regulerede projekter uden kritiske fund ved aflevering. PDCA-program reducerede energiomkostninger med 40 %.')]),
        ('Projekt- og værkstedsleder', 'Ventek-Air · København · jan. 2022–nov. 2022', '14 medarbejdere · 11 samtidige projekter', [
            ('Daglig ledelse', 'Kapacitet, fremdrift og underentreprenører fra specifikation til aflevering. Tavlemøder og flaskehalsanalyse understøttede forbedringer i leveringsevnen.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker', 'Biofos, Lynetten · København · aug. 2017–jan. 2022', 'Kritisk drift døgnet rundt · pumper, HVAC, højspændingstavler og SCADA', [
            ('Stabil drift', 'Forebyggende vedligehold, akut fejlfinding og reservedelsflow. 5S, Standard Work og PDCA samt LOTO og risikovurdering i skifteholdsdrift.')]),
        ('Elektromekaniker / produktionsteamleder', 'ARJ Engineering · Teheran · dec. 2003–mar. 2010', '12 mekanikere og teknikere i maskinværksted', [
            ('Team og produktion', 'Vagtplanlægning, materialestyring og målopfølgning; fejldiagnose og reparation af industrielle el- og mekaniske anlæg.')])]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        m.doc.paragraphs[-1].runs[0].text = 'Omfang: '
        for label, body in bullets: m.bullet(label, body, after=25)
    m.section('UDDANNELSE OG AUTORISATION')
    m.edu('B.Tech i Technology Management & Mechanical Engineering — maskinmesterretningen', 'Maskinmesterskolen København · 2017–2022 · EQF 6')
    m.edu('El- og maskinteknisk design, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('Køleteknik og klimaanlæg · STCW-sikkerhed og maskinrumsvagt', 'Mercantec 2021 · Søfartsstyrelsen 2021–2023')
    m.section('SPROG OG PRAKTISK')
    m.para('Dansk og persisk/farsi: modersmål · Engelsk: professionelt i skrift og tale · Kørekort B. Bopæl i Måløv; arbejdstid og overgang fra ELOHVAC aftales.', after=70)
    m.section('REFERENCER')
    m.para('Tidligere ledere hos Novo Nordisk og Biofos oplyses efter aftale.', after=70)

    m.page_break()
    m.models_table('DE FØRSTE 90 DAGE — FORSLAG TIL OPSTART', ('Tidspunkt', 'Samarbejde og konkrete leverancer'), [
        ('Uge 1', 'Møde operatører på både dag og aften, de to øvrige teamledere og support. Gennemgå instruktioner, sikkerhed, GMP og hygiejne samt aftale ansvar og forventninger med afdelingslederen.'),
        ('Inden dag 30', 'Sammen med holdet skabe overblik over vagtplan, overlevering, bemanding og gældende kompetence- og træningskrav. Aftale 1:1-samtaler og vælge få driftsmål sammen med support.'),
        ('Inden dag 60', 'Gennemgå træningsbehov og dækning med oplærere og medarbejdere. Vælge én årsag til spild eller ustabilitet, undersøge den med PDCA/A3 og aftale en afprøvning inden for godkendte procedurer.'),
        ('Inden dag 90', 'Følge op på læring, trivsel og den valgte forbedring med holdet. Fremlægge effekt, åbne spørgsmål og næste skridt for lederteamet; opdatere planen sammen med support.')])
    m.section('SAMARBEJDE OM PRODUKTIONEN')
    for label, body in [
        ('Operatørholdet', 'Være tilgængelig i hverdagen og møde både dag- og aftenhold. Spørge, hvad der hindrer et godt skift, og følge aftaler og bekymringer til dørs.'),
        ('Teamledere og support', 'Afstemme bemanding, overlevering og behov for hjælp på tværs. Få faglige vurderinger fra de ansvarlige, før processer eller instruktioner ændres.'),
        ('Afdelingslederen', 'Aftale beslutningsrum og backup-ansvar. Give et kort, ærligt billede af sikkerhed, drift, træning og de beslutninger, der kræver støtte.'),
        ('Udvikling og trivsel', 'Bruge 1:1, GROW og situationsbestemt ledelse til at afklare styrker og mål. Skabe rum for feedback og sikre, at oplæring følges op i praksis.')]:
        m.bullet(label, body, after=35)
    m.section('FAGLIGT UDGANGSPUNKT OG DIGITALE VÆRKTØJER')
    m.para('Jeg kender reguleret projektarbejde fra Novo Nordisk og teknisk drift fra Biofos, men har ikke dokumenteret praktisk ansvar for fermentering, frysetørring eller fremstilling af bakteriekulturer. Den specifikke proces, hygiejnepraksis og lokale instruktioner skal læres sammen med sitets fagfolk. Min B.Tech er teknisk og ikke en natur- eller fødevarevidenskabelig uddannelse.', after=80)
    m.para('Som aktiv professionel AI-/Claude-koder udvikler jeg værktøjer i Python og Claude til planlægning, opfølgning og investeringsmodeller, herunder NPV, IRR og scenarier. Hos Novonesis vil brug af AI kræve godkendelse, korrekt datahåndtering og faglig kontrol; digitale forslag erstatter aldrig GMP-godkendte systemer eller instruktioner.', after=80)
    m.section('FRA TRÆNING TIL STABILT SKIFT')
    m.para('En træningsplan skal vise, hvilke opgaver holdet skal kunne løse, hvem der kan oplære, og hvornår kompetencen skal følges op. Jeg vil sammenholde planen med vagtplanen og den faktiske bemanding, så sygdom, oplæring og opgaver på tværs ikke overlades til tilfældigheder. Faglig godkendelse af en operatørs kompetence ligger hos de ansvarlige efter sitets regler.', after=80)
    m.para('Ved skiftoverlevering vil jeg sørge for, at åbne opgaver, udstyr, sikkerhed og eventuelle afvigelser bliver givet videre med en klar ansvarlig. Målet er, at næste hold ved, hvad der er aftalt, og hvor hjælp kan hentes.', after=80)
    m.section('FOKUSOMRÅDER')
    m.para('Personaleledelse · produktion · træning og onboarding · vagtplanlægning · kompetenceudvikling · trivsel · feedback · GMP · hygiejne · sikkerhed · LEAN · PDCA · standardisering · udbytte · mindre spild · samarbejde', after=70)
    return m.save(path, title='Ansøgning og CV — Teamleder, Novonesis Roskilde, JR113971', subject='Teamledelse, GMP og produktion', keywords='teamleder, produktion, GMP, kompetenceudvikling, Novonesis')

if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Novonesis_TeamlederRoskilde.docx')))
