# -*- coding: utf-8 -*-
"""KLAR Forsyning — Plan- og anlægschef, DK-11209. Dansk brev og CV."""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Teknisk leder | Anlægsprojekter, forsyning og medarbejderudvikling'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv (Ballerup Kommune)'

def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('3. november 2026')
    m.meta('KLAR Forsyning A/S · Vasebækvej 40 · 4600 Køge · att. teknisk direktør Jesper Koziara')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Plan- og anlægschef · DK-11209', bold=True, color='1A1A1A')
    m.para('Når investeringerne vokser, skal overblikket vokse med – uden at projektledernes ansvar bliver mindre. Opgaven i Plan og Anlæg er at omsætte et stort investeringsprogram til robuste anlæg, mens drift, økonomi og borgernes behov hænger sammen. Det kræver en chef, der er tæt nok på til at opdage en risiko i tide og samtidig giver specialisterne plads til at gøre deres arbejde.', after=80)
    m.para('Jeg vil begynde med at forstå den eksisterende projektmodel og samarbejdet med driftschefen. Sammen med projektlederne og teamlederen for GIS, Miljø & Hydraulik vil jeg skabe et samlet billede af fremdrift, økonomi, risici, ressourcer og de beslutninger, der mangler. Det skal være en hjælp til at prioritere og fjerne forhindringer – ikke en ekstra rapporteringsøvelse.', after=80)
    for label, body in [
        ('Ledelse tæt på, uden at overtage', 'Aftale beslutningsrum, 1:1-samtaler og faglig sparring med projektlederne og teamlederen. Situationsbestemt ledelse og GROW kan støtte udvikling og delegering; når en sag eskaleres, aftaler vi, hvem der gør hvad, og hvornår der følges op.'),
        ('Portefølje og økonomi', 'Bruge eksisterende projektdata til et kort overblik over milepæle, budget, prognose, væsentlige afvigelser og næste beslutning. Med projektledere, økonomi og drift vurderes afhængigheder og ressourcekonflikter, inden de bliver til forsinkelser.'),
        ('Risiko, drift og kvalitet', 'Videreudvikle projektstyring og risikostyring med projektlederne og driftschefen: klare grænseflader, rettidig overdragelse og opfølgning på risici. Afdelingens bidrag til ISO 9001, ISO 14001, ISO 22000 og overvågningsvagten afklares med de ansvarlige.'),
        ('Ejere og omverden', 'Sammen med direktionen sikre kort og ærlig kommunikation til ejerkommuner, myndigheder og rådgivere. Beslutningsgrundlaget skal vise alternativer, økonomi og konsekvenser – også når investeringer påvirker takster og borgere.')]:
        m.bullet(label, body, after=35)
    m.para('I den første uge vil jeg lytte og gennemgå porteføljen. Inden dag 30 aftaler vi et fælles udgangspunkt og beslutningsrum; inden dag 60 afprøver vi en enkel opfølgning på udvalgte projekter; inden dag 90 fremlægger jeg læring, prioriteringer og næste beslutninger for chefgruppen.', after=80)
    m.para('Erfaringen fra Biofos giver et praktisk kendskab til spildevandsdrift; hos Novo Nordisk har jeg koordineret specialister og fulgt økonomi og risici i anlægsprojekter. Jeg har ikke dokumenteret ansvar for et investeringsprogram på KLARs størrelse eller formel ledelse af en teamleder. Det vil jeg gå åbent til og bygge videre på den faglighed og de processer, der allerede findes.', after=80)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'LEDELSESPROFIL')
    m.para('Elautoriseret maskinmester og teknisk leder med erfaring fra spildevandsdrift, tværfaglige anlægsprojekter, personaleledelse og virksomhedsøkonomi. Samler medarbejdere om klare prioriteringer og følger økonomi og risici uden at tage ejerskabet fra dem, der udfører opgaven. Aktiv professionel AI-/Claude-koder med egne værktøjer til planlægning og investeringsmodeller.', after=80)
    m.section('LEDELSE OG LEVERANCER')
    for label, body in [
        ('Specialister og medarbejdere', 'Novo Nordisk: koordinerede 25 specialister på tværs af engineering, indkøb og anlæg. ELOHVAC: leder fem elektrikere og tre lærlinge med 1:1, MUS og oplæring.'),
        ('Anlægsprojekter og fremdrift', 'Novo: 37 samtidige CAPEX-projekter på 2–10 mio. kr. pr. projekt med opfølgning på fremdrift, økonomi, ressourcer og risici. Ventek-Air: ledede et team på 14 på 11 samtidige projekter.'),
        ('Forsyningsdrift', 'Biofos Lynetten: el- og mekanisk drift af spildevandsanlæg med pumper, HVAC, højspændingstavler og SCADA i 24/7-miljø. Forebyggende vedligehold, fejlfinding og reservedele.'),
        ('Økonomi og samarbejde', 'Fuldt P&L i ELOHVAC med tilbud, indkøb og underentreprenører. Ventek-Air: udbud, aftalegrundlag og afleveringsdokumentation; Novo: rapportering til ledelse og bygherre.'),
        ('Forbedringer og AI', 'PDCA-program hos Novo reducerede energiomkostninger med 40 %. Python/Claude API-værktøjer til tilbud, planlægning og KPI gav over 40 % produktivitetsløft i ELOHVAC.')]:
        m.bullet(label, body, after=30)
    m.models_table('LEDELSESVÆRKTØJER — ERFARING', ('Område', 'Metoder anvendt i praksis'), [
        ('Mennesker', 'Situationsbestemt ledelse, 1:1, MUS og struktureret oplæring i ELOHVAC.'),
        ('Fremdrift', 'Daglige tavlemøder og flaskehalsanalyse hos Ventek-Air til planlægning og kapacitet.'),
        ('Forbedring', 'PDCA, A3 og rodårsagsanalyse hos Novo; 5S, Standard Work og PDCA hos Biofos.'),
        ('Sikkerhed', 'LOTO, APV og risikovurdering i ELOHVAC og Biofos; opfølgning på nærved-hændelser hos Biofos.')])
    m.section('UDVALGTE RESULTATER')
    for label, body in [('25 specialister / 37 projekter', 'Koordinering hos Novo Nordisk; nul kritiske fund ved aflevering.'), ('14 medarbejdere / 11 projekter', 'Kapacitetsstyring og daglig ledelse hos Ventek-Air.'), ('40 % lavere energiomkostninger', 'Resultat af PDCA-program hos Novo Nordisk.')]: m.bullet(label, body, after=30)

    m.page_break()
    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør / elautoriseret maskinmester', 'ELOHVAC ApS · København · maj 2023–nu', '5 elektrikere og 3 lærlinge · fuldt P&L-ansvar', [
            ('Ledelse og leverancer', 'Daglig planlægning, 1:1, MUS og oplæring. Tilbud og beregning, materialer, underentreprenører, kvalitet og aflevering.'),
            ('Digitale værktøjer', 'Bygget Python/Claude API-værktøjer til tilbud, tidsplaner, KS og KPI; produktivitetsløft over 40 %.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem', 'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024', '37 samtidige CAPEX-projekter · 25 specialister · 2–10 mio. kr. pr. projekt', [
            ('Projektstyring', 'Fulgte fremdrift, økonomi, ressourcer og risici på tværs af engineering, indkøb og anlæg; rapporterede til ledelse og bygherre. SAP ERP til økonomi og aktiver.'),
            ('Kvalitet og forbedring', 'FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA uden kritiske fund ved aflevering. PDCA-program reducerede energiomkostninger med 40 %.')]),
        ('Projekt- og værkstedsleder', 'Ventek-Air · København · jan. 2022–nov. 2022', '14 medarbejdere · 11 samtidige anlægsprojekter', [
            ('Fremdrift og aftaler', 'Kapacitetsstyring fra specifikation til aflevering; udbud, tilbud, underentreprenører og sikkerhedsdokumentation. Daglige tavlemøder og flaskehalsanalyse.')]),
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
    m.models_table('FØRSTE 90 DAGE — FORSLAG TIL OPSTART', ('Tid', 'Handlinger og leverancer'), [
        ('Uge 1', 'Møde projektledere, teamleder og driftschef. Forstå den eksisterende projektmodel, roller, aktuelle risici og beslutninger. Aftale mandat og forventninger med teknisk direktør.'),
        ('Inden dag 30', 'Sammen med teamene og økonomi skabe et fælles billede af projektportefølje, budget, prognose, bemanding, risici og afhængigheder. Afholde 1:1 og aftale, hvornår en projektleder har brug for chefens hjælp.'),
        ('Inden dag 60', 'Afprøve en kort, fælles status på udvalgte projekter med projektledere og drift. Afklare næste beslutning, risikoejer og kapacitet; drøfte rapportering til direktion og chefgruppe.'),
        ('Inden dag 90', 'Evaluere med medarbejderne, om opfølgningen hjælper. Fremlægge prioriteringer, ressourcekonflikter, økonomiske afvigelser og forslag til videre udvikling af projektmodellen for chefgruppen.')])
    m.section('LEDELSE PÅ TVÆRS')
    for label, body in [
        ('Projektledere og teamleder', 'Giv tydelige rammer og vær tilgængelig, når beslutninger eller ressourcer spærrer. Brug 1:1, GROW og situationsbestemt ledelse til at udvikle mennesker uden at overtage projekterne.'),
        ('Drift og teknisk direktør', 'Inddrag driftskompetencer fra planlægning til aflevering. Aftal hvornår risici løftes, og giv teknisk direktør et klart beslutningsgrundlag ved afvigelser.'),
        ('Ejerkommuner og rådgivere', 'Afstem forventninger til projekternes forudsætninger, myndighedsprocesser og kommunikation. Hold ansvar og næste skridt tydelige for alle parter.'),
        ('Fælles ledelse', 'Bidrag i chefgruppen med åben prioritering på tværs af afdelinger; økonomi, kvalitet og forsyningssikkerhed skal ses i sammenhæng med trivsel og kapacitet.')]: m.bullet(label, body, after=35)
    m.section('DATA, INVESTERINGER OG KVALITET')
    m.para('Jeg bygger aktivt værktøjer i Python og Claude, herunder investeringsmodeller med NPV, IRR og følsomhedsanalyse. Et beslutningsoplæg til KLAR kan sammenligne livscyklusomkostninger, risici og alternativer, men forudsætninger og resultater skal valideres med økonomi og de tekniske fagfolk. AI anvendes kun efter virksomhedens regler for datasikkerhed og godkendte systemer.', after=80)
    m.para('Kravene i ISO 9001, ISO 14001 og ISO 22000 samt ordningen for overvågningsvagt skal gennemgås med de ansvarlige. Erfaring fra GMP og dokumenteret aflevering er relevant, men er ikke det samme som dokumenteret ansvar for disse ISO-systemer.', after=80)
    m.section('FRA PORTFØLJE TIL BESLUTNING')
    m.para('Projektlederen ejer sit projekt og beskriver den aktuelle situation. Chefens opgave er at sammenholde projekterne: Er de samme ressourcer lovet flere steder? Er der ændringer i økonomi, myndighedsforhold eller tidsplan, som kræver en beslutning? En kort beslutningslog med ejer, frist og opfølgning gør hjælpen konkret uden at fjerne det lokale ansvar.', after=80)
    m.section('FAGLIGE FOKUSOMRÅDER')
    m.para('Anlægsprojekter · spildevand · drikkevand · klimatilpasning · portefølje · governance · risikostyring · budget · regnskab · indkøb · udbud · projektledelse · tillidsbaseret ledelse · fremdrift · kommunikation · forsyningssikkerhed', after=70)
    return m.save(path, title='Ansøgning og CV — Plan- og anlægschef, KLAR Forsyning DK-11209', subject='Anlægsprojekter, forsyning og ledelse', keywords='plan og anlægschef, forsyning, projektstyring, ledelse')

if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_KLAR_PlanOgAnlaegschef.docx')))
