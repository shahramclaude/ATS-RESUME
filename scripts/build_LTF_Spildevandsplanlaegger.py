# -*- coding: utf-8 -*-
"""Lyngby-Taarbæk Forsyning — Spildevandsplanlægger application and evidence-led CV."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from master_design import MasterDoc

NAME = 'SHAHRAM AJLOO'
TITLE = 'Spildevandsplanlægger | Strategi, teknisk drift og projekter'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
TEMPLATE = ROOT / 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'


def build(out):
    m = MasterDoc(str(TEMPLATE), lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('3. november 2026 · Lyngby-Taarbæk Forsyning · Att.: Andreas Rose')
    m.para('**Ansøgning: Spildevandsplanlægger til fremtidens spildevandsløsninger**', after=30, justify=False)
    m.para('Mølleåværket modtager spildevand fra fire kommuner, mens kommunens spildevandsplan beskriver kloakeringens nuværende og fremtidige udbredelse, hvordan spildevandet samles, renses og udledes, og hvad der skal ske fremover. Spildevandsplanlægning skal derfor forbinde udviklingen af afløbssystemet med kapacitet, miljøhensyn, konkrete projekter og myndighedsprocesser — med klare aftaler mellem forsyning, kommune og rådgivere.', after=34, line=240, justify=False)
    m.para('**Et fælles og efterprøveligt planlægningsgrundlag**', after=15, justify=False)
    m.para('Start med ét versionsstyret overblik over eksisterende spildevandsplan, lednings- og anlægsdata, kendte kapacitetsproblemer, aflastninger, planlagte byudviklingsområder, udledningstilladelser og allerede besluttede projekter. For hvert datasæt noteres ejer, aktualitet, usikkerhed og ansvar for opdatering. Det giver kommunen og rådgiverne et fælles billede af, hvad der er kendt, og hvad der skal undersøges, før en løsning vælges.', after=28, line=238)
    m.para('**Fra klima- og kapacitetsproblem til valgbare løsninger**', after=15, justify=False)
    m.para('Afgræns opland og serviceniveau sammen med kommunen, og aftal med de hydrauliske specialister, hvilke regn-, belastnings- og udviklingsscenarier der skal vurderes. Sammenlign relevante muligheder — eksempelvis lokal afledning af regnvand, forsinkelse, bassin, separering eller ledningsforstærkning — på kapacitet, overløbsrisiko, vandmiljø, areal, anlægsøkonomi, drift og levetid. Synliggør antagelser og følsomheder; beslutningen skal kunne forklares både teknisk og økonomisk.', after=28, line=238)
    m.para('**Plan, tilladelser og projektgennemførelse**', after=15, justify=False)
    m.para('Knyt hver planændring og hvert prioriteret projekt til beslutningsejer, myndighedsskridt, nødvendige udledningstilladelser, dokumentation, høring eller politisk behandling, tidsplan og afhængigheder. I byggemodninger og tværkommunale projekter om Mølleåsystemet bør grænseflader, databehov og milepæle aftales tidligt. Et fælles beslutnings- og handlingsregister gør det tydeligt, hvad der mangler, hvem der følger op, og hvornår sagen kan gå videre.', after=28, line=238)
    m.para('De første 30 dage bør etablere baseline, interessentkort og åbne beslutninger. Inden dag 60 kan de vigtigste kapacitets- og tilladelsesafhængigheder prioriteres sammen med kommunen og rådgiverne; inden dag 90 bør ét afgrænset område have et sammenlignet løsningsgrundlag, tydelige usikkerheder og en anbefalet næste beslutning. Det følger LTF’s beskrevne vægt på samarbejde, trivsel, udvikling og respekt for alles kompetencer og bidrag — og holder forslag adskilt fra vedtagne planer.', after=26, line=238)
    m.meta('Med venlig hilsen', after=8)
    m.meta('Shahram Ajloo', after=0)

    # CV page 1
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'FAGLIG PROFIL')
    m.para('Elautoriseret maskinmester med teknisk driftserfaring fra BIOFOS’ renseanlæg Lynetten og en projektbaggrund på tværs af industri, tekniske installationer og regulerede anlæg. Kombinerer praktisk forståelse for spildevandsanlæg og SCADA med koordinering af 37 samtidige CAPEX-projekter, budgetopfølgning, sikkerhed og tværfagligt samarbejde. Dataværktøjer omfatter Excel/Power Query, Power BI, SAP ERP og Python/Claude API. Den dokumenterede erfaring er stærkest i drift, projekter og data; spildevandsplaner, hydrauliske modeller og kommunal myndighedsbehandling beskrives ikke som tidligere ejerskab.', after=35, line=232, justify=False)

    matrix = [
        ('Relevant teknisk uddannelse', 'B.Tech i Technology Management & Mechanical Engineering samt dansk autorisation som elautoriseret maskinmester (LV/MV/HV). Hertil el- og maskinteknisk design fra Tehran Technical University.'),
        ('Erfaring fra spildevandsanlæg', 'Erfaring fra BIOFOS/Lynetten, august 2017–januar 2022: drift og vedligehold i døgnbemandet miljø, herunder pumper, HVAC, højspændingstavler, SCADA, forebyggende vedligehold og akut fejlfinding.'),
        ('Strategier og langsigtede planer', 'Planlægning af vedligehold, ressourcer og projektforløb samt omkostnings- og risikovurdering er dokumenteret. Ejerskab af en kommunal spildevandsstrategi eller langsigtet afløbsplan er ikke angivet i kilde-CV’et.'),
        ('Samarbejde med kommunen om planer og myndighedsbehandling', 'Novo Nordisk-projekter krævede tværfaglig koordinering og sporbar dokumentation; ELOHVAC/Ventek-Air omfattede kunder og leverandører. Direkte udarbejdelse af kommunale spildevandsplaner eller myndighedsbehandling er ikke beskrevet.'),
        ('Klimatilpasning og bæredygtig vandhåndtering', 'PDCA-program hos Novo Nordisk reducerede energiomkostninger med 40 %. Driftserfaringen giver forståelse for anlæg og konsekvenser; direkte LAR-design eller klimatilpasningsprojekter er ikke oplyst.'),
        ('Kapacitetsvurdering og hydraulisk modellering', 'Projektøkonomi, risici, ressourcer og tekniske forudsætninger er fulgt på 37 CAPEX-projekter. En specifik hydraulisk model, kapacitetsberegning eller modelplatform fremgår ikke af kilde-CV’et.'),
        ('GIS, databaser og digitale værktøjer', 'Dokumenteret værktøjserfaring: Excel/Power Query, Power BI, SAP ERP, Python og Claude API. Et konkret GIS-system, kloakdatabase eller hydraulisk modelværktøj er ikke navngivet.'),
        ('Projektarbejde og byggemodning', 'Dokumenteret projektledelse hos Novo Nordisk: 37 samtidige CAPEX-projekter, 25 specialister og DKK 2–10 mio. pr. projekt. Ventek-Air: 11 samtidige anlægsprojekter fra specifikation til aflevering; ELOHVAC: tilbud, planlægning og underentreprenører.'),
        ('Udledningstilladelser og sagsbehandling', 'Reguleret test- og afleveringsdokumentation er dokumenteret fra Novo Nordisk. Tidligere ansvar for spildevandstilladelser, miljøsagsbehandling eller myndighedsindberetninger er ikke beskrevet.'),
        ('Tværkommunale vandmiljøprojekter', 'Tværfaglig koordinering med engineering, indkøb, anlæg, kunder og leverandører er dokumenteret. Tidligere projektarbejde om Mølleåsystemet eller tværkommunale vandmiljøprojekter er ikke oplyst.'),
        ('Struktureret analyse og selvstændigt ansvar', 'ELOHVAC: fuldt P&L-ansvar, beregninger, planlægning og opfølgning. Novo Nordisk: fremdrift, økonomi, risici og ressourcer på en portefølje af 37 projekter.'),
        ('Samarbejde og kommunikation med myndigheder, kommune, rådgivere og faggrupper', 'Daglig koordinering med tekniske teams, kunder, underentreprenører og specialister i ELOHVAC og Ventek-Air samt tværfaglige grupper og ledelsesrapportering hos Novo Nordisk.')]
    m.models_table('RELEVANS OG DOKUMENTATION', ('Krav i opslaget', 'Erfaring og sammenhæng'), matrix,
                   widths=(2600, 7746), compact=True)

    # CV page 2: professional history
    m.page_break()
    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør / elautoriseret maskinmester', 'ELOHVAC ApS · København · maj 2023–nu', '5 elektrikere + 3 lærlinge · fuldt P&L-ansvar', [
            ('Planlægning og økonomi', 'Tilbud og beregninger, daglig planlægning, materialestyring, underentreprenører, kvalitet og afleveringsdokumentation.'),
            ('Teknisk leverance', 'Installation, tavler, styring, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg for erhvervskunder.'),
            ('Mennesker og digital udvikling', '1:1, medarbejdersamtaler, oplæring og arbejdsmiljø. Python/Claude API-værktøjer til tilbud, tidsplaner, KS og KPI’er gav over 40 % produktivitetsløft.')]),
        ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen', 'Data Power Consultant ApS · København · 2024–2026 (sideløbende)', '4–10 personer', [
            ('Tekniske applikationer', 'Ledte tekniske og industrielle løsninger fra behovsafklaring og integration til idriftsættelse, dokumentation og overdragelse. Professionel AI-coding, LLM-API’er og AI-agenter indgik i arbejdsområdet.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem', 'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024', '37 samtidige CAPEX-projekter · 25 specialister · DKK 2–10 mio. pr. projekt', [
            ('Portefølje og beslutningsgrundlag', 'Koordinerede engineering, indkøb og anlæg; fulgte fremdrift, økonomi, risici og ressourcer og rapporterede til ledelse og bygherre.'),
            ('Test, dokumentation og energi', 'FAT/SAT og IQ/OQ/PQ i reguleret miljø uden kritiske afvigelser ved aflevering. PDCA-program reducerede energiomkostninger med 40 %.'),
            ('Digitale systemer', 'SAP ERP til økonomi, aktiver og omkostninger; tekniske anlæg omfattede el-tavler, styring og UPS.')]),
        ('Projekt- og værkstedsleder', 'Ventek-Air · København · jan. 2022–nov. 2022', '14-personers team · 11 samtidige anlægsprojekter', [
            ('Fra specifikation til aflevering', 'Kapacitets- og fremdriftsstyring, tilbud/udbud, underentreprenører, aftalegrundlag, sikkerhedsdokumentation og afleveringspakker; daglige tavlemøder og flaskehalsanalyser.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker', 'BIOFOS, Lynetten · København · aug. 2017–jan. 2022', 'Spildevandsanlæg · døgnbemandet drift', [
            ('Renseanlægsdrift', 'Forebyggende vedligehold og akut fejlfinding på pumper, HVAC, højspændingstavler og SCADA; sikkerhedsdisciplin i skifteholdsdrift.'),
            ('Systematik og sikkerhed', 'LOTO, risikovurdering og APV; 5S, Standard Work, PDCA og forbedring af reservedelsflow på værksted og lager.')]),
        ('Elektromekaniker / produktionsteamleder', 'ARJ Engineering · Teheran · dec. 2003–mar. 2010', '12 mekanikere og teknikere', [
            ('Teknisk produktion', 'Vagtplanlægning, materialestyring, målopfølgning, fejldiagnose og reparation af industrielle el- og mekaniske anlæg; ledelse af tekniske medarbejdere.')])]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=11, line=235)

    # CV page 3: education, methods and a practical 90-day plan
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'UDDANNELSE, VÆRKTØJER OG PLAN')
    m.section('UDDANNELSE OG CERTIFICERING')
    for title, meta in [
        ('B.Tech, Technology Management & Mechanical Engineering', 'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · EQF 6'),
        ('El- og maskinteknisk design, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6'),
        ('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023'),
        ('PRINCE2-certificeret projektleder', 'AXELOS / PeopleCert'),
        ('Køleteknik og klimaanlæg', 'AMU · Mercantec · 2021'),
        ('STCW-sikkerhed og maskinrumsvagt', 'Maskinrumsvagt A-III/1, skibssikkerhed VI/5 og sikkerhedsopgaver VI/6 · Søfartsstyrelsen · 2021–2023'),
        ('HF, matematik og fysik', 'VUC · 2012–2017')]:
        m.edu(title, meta)

    m.models_table('ARBEJDSFORMER OG DIGITALE VÆRKTØJER', ('Område', 'Dokumenteret anvendelse'), [
        ('Projektstyring', 'PRINCE2-certificering; tids-, økonomi-, risiko- og ressourceopfølgning hos Novo Nordisk og Ventek-Air.'),
        ('Data og rapportering', 'Excel/Power Query, Power BI, SAP ERP, Python og Claude API; KPI-dashboards og automatiseret rapportering.'),
        ('Procesforbedring', 'PDCA, 5S, Standard Work, A3, 5xHvorfor og Ishikawa anvendt i praksis; Lean-/Six Sigma-praksis, ikke certificeret.'),
        ('Drift og sikkerhed', 'SCADA-overvågning, forebyggende vedligehold, akut fejlfinding, LOTO, APV og risikovurdering i BIOFOS/ELOHVAC.')], compact=True)

    m.section('FØRSTE 90 DAGE — FORSLAG TIL TILGANG')
    m.models_table('TID OG LEVERANCER', ('Periode', 'Fokus og konkret output'), [
        ('Uge 1–2', 'Aftal roller, dataejere og beslutningsveje med spildevandsteamet, kommunen og rådgiverne. Saml gældende spildevandsplan, projektliste, tilladelser, datahuller og åbne sager i ét overblik.'),
        ('Dag 15–30', 'Prioritér oplande og udviklingsområder efter kapacitetsbehov, miljø-/overløbsrisiko og planlagte ændringer. Aftal hvilke hydrauliske analyser, GIS-lag og faglige vurderinger der skal opdateres af ansvarlige specialister.'),
        ('Dag 31–60', 'Sammenlign løsninger for ét prioriteret område på kapacitet, klima, miljø, investering, drift og afhængigheder. Knyt myndighedsskridt og tilladelsesbehov til ejere og tidsplan.'),
        ('Dag 61–90', 'Fremlæg et beslutningsklart grundlag med alternativer, antagelser, usikkerheder, økonomi og anbefalet næste skridt. Indarbejd feedback fra kommune og rådgivere i plan- og projektforløbet.'),
        ('Løbende', 'Følg op på datakvalitet, myndighedsfrister og afhængigheder mellem plan, tilladelse og projekt; opdatér prioriteringen, når nye oplysninger eller klima-/udviklingsforudsætninger ændres.')], compact=True)
    m.para('Sprog: dansk og persisk/farsi — modersmål · engelsk — professionelt. Kørekort B. Bopæl: Måløv.', after=25, line=235, justify=False)

    return m.save(str(out), title='Ansøgning og CV — Spildevandsplanlægger, Lyngby-Taarbæk Forsyning',
                  subject='Spildevandsplanlægning, klima og tværfaglige projekter',
                  keywords='spildevandsplanlægger, spildevandsplanlægning, GIS, hydraulisk modellering, byggemodning, myndighedsbehandling, vandmiljø')


if __name__ == '__main__':
    print(build(ROOT / 'Shahram_Ajloo_LTF_Spildevandsplanlaegger.docx'))
