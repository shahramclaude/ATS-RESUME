# -*- coding: utf-8 -*-
"""Mølleåværket — one-page job-focused application followed by evidence-led CV."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from master_design import MasterDoc

NAME = 'SHAHRAM AJLOO'
TITLE = 'Driftsleder — Mølleåværket | Lyngby-Taarbæk Forsyning'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
TEMPLATE = ROOT / 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'


def build(out):
    m = MasterDoc(str(TEMPLATE), lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('3. november 2026 · Att.: Jannik Lund Olsen, driftschef')
    m.para('**Ansøgning: Driftsleder til Mølleåværket**', after=35, justify=False)
    m.para('Mølleåværkets ansvar er at rense spildevand sikkert og miljømæssigt korrekt, mens anlæg, mennesker og ressourcer skal fungere som én driftsopgave. Værket behandler omkring 10 mio. m³ årligt fra fire kommuner og kombinerer mekanisk, biologisk og kemisk rensning før udledning til Øresund. Det stiller krav til sikker drift og en driftsleder, der kan forbinde hverdagsdisciplin med faglige forbedringer.', after=45, line=245, justify=False)
    m.para('**En tydelig rytme for mennesker, sikkerhed og drift**', after=20, justify=False)
    m.para('Start med teamet: gennemgå opgaver, bemanding, alarmer, åbne fejl og overleveringer, så hver kritisk handling har en ejer og en frist. Brug korte faste opfølgningsmøder og individuelle samtaler til at afstemme forventninger, høre medarbejdernes observationer og få øje på kompetencebehov. Sikkerhedshændelser og nærved-hændelser skal føre til konkrete handlinger sammen med arbejdsmiljøorganisationen.', after=38, line=240)
    m.para('**Vedligehold, proces og miljøkrav i samme plan**', after=20, justify=False)
    m.para('Saml anlægstilstand, forebyggende vedligehold, kritiske reservedele og planlagte stop i én prioritering efter konsekvens for sikkerhed, rensekvalitet, miljø og oppetid. Gør miljøgodkendelser og udledningskrav operationelle med navngivne ansvarlige for målinger, prøvetagning, analyser, frister, afvigelser og myndighedsrapportering. Følg SRO/SCADA-data sammen med prøveresultater for blandt andet kvælstof, fosfor og organisk materiale samt medarbejdernes observationer; vurder ændringer med de procesfaglige kolleger, der har den relevante kompetence.', after=38, line=240)
    m.para('**Reparationer, økonomi og samarbejde på tværs**', after=20, justify=False)
    m.para('Før større reparationer og ombygninger afstemmes arbejdsomfang, sikker afstilling, driftsvindue, ansvar, leverancer og overdragelse med projektleder, specialister, leverandører og arbejdsmiljøorganisation. Månedlig budgetopfølgning bør forbinde forbrug og vedligeholdsbehov med energi, aktivernes levetid og rensekrav. Mølleåværkets arbejde med at udnytte slam til biogas gør ressourceforbrug og driftsøkonomi til en naturlig del af den tekniske opfølgning.', after=38, line=240)
    m.para('De første uger bør skabe et fælles billede af anlæg, krav, teamets faglighed og aktuelle risici. Inden dag 30 fastlægges ansvar og opfølgningsrytme; inden dag 60 er vedligehold, miljøfrister og projektgrænseflader gennemgået med de relevante fagpersoner; inden dag 90 følges en afgrænset forbedring op mod aftalte drifts- og miljømål. Tilgangen bygger på LTF’s vægt på respekt for alles kompetencer og bidrag, trivsel, udvikling og samarbejde — uden at indføre en parallel proces til den, der allerede virker.', after=30, line=240)
    m.meta('Med venlig hilsen', after=8)
    m.meta('Shahram Ajloo', after=0)

    # CV page 1
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'DRIFTSPROFIL')
    m.para('Elautoriseret maskinmester med erfaring fra teknisk drift og vedligehold på BIOFOS’ renseanlæg Lynetten, personaleledelse og tekniske projekter. På Lynetten omfattede arbejdet pumper, HVAC, højspændingstavler og SCADA i døgnbemandet drift. Dertil kommer fuldt resultatansvar i ELOHVAC og koordinering af 37 samtidige CAPEX-projekter hos Novo Nordisk. Erfaringen giver en relevant drifts- og ledelsesbase; miljøgodkendelser, spildevandsprøver og procesrapportering skal udføres i samspil med de ansvarlige fagpersoner.', after=38, line=235, justify=False)

    matrix = [
        ('Relevant teknisk uddannelse', 'B.Tech i Technology Management & Mechanical Engineering samt dansk autorisation som elautoriseret maskinmester (LV/MV/HV). Uddannelsesbaggrunden kombinerer teknisk drift, mekanik og ledelse.'),
        ('Mere end fem års relevant forsynings-, rense- eller proceserfaring', 'BIOFOS/Lynetten er dokumenteret fra august 2017 til januar 2022 (ca. 4 år og 5 måneder). ARJ Engineering (2003–2010) er industriel el-/mekanisk produktion; det er ikke fastslået, om denne periode opfylder opslagets definition af relevant procesindustri.'),
        ('Driftslederuddannelse for spildevandsanlæg', 'Denne specifikke uddannelse fremgår ikke af det foreliggende CV-grundlag. Den må verificeres; hvis den mangler, kan et relevant uddannelsesforløb aftales med forsyningen.'),
        ('Daglig sikker og miljømæssigt korrekt drift', 'På BIOFOS indgik skifteholdsdrift, forebyggende vedligehold og akut fejlfinding på kritiske el- og mekaniske anlæg. Sikkerhedsarbejde omfatter LOTO, APV og risikovurdering; specifikt miljøgodkendelsesansvar er ikke dokumenteret.'),
        ('Personaleledelse, kompetencer og trivsel', 'ELOHVAC: daglig planlægning, 1:1, medarbejdersamtaler og oplæring af fem elektrikere og tre lærlinge. Ventek-Air: daglig ledelse af et team på 14. Det er overførbar personaleledelse, ikke tidligere ledelse af netop seks renseanlægsoperatører.'),
        ('Vedligehold og aktivernes levetid', 'BIOFOS: forebyggende vedligehold og fejlfinding på pumper, HVAC, højspændingstavler og SCADA samt reservedelsflow og værkstedsforbedringer. Aktivstrategi og specifikke levetidsberegninger er ikke dokumenteret.'),
        ('Dataanalyse og procesoptimering', 'PDCA og dataanalyse i forbedringsarbejde er anvendt; Novo Nordisk reducerede energiomkostninger med 40 %. Det er ikke dokumenteret som procesoptimering af spildevandsrensning eller som ejerskab af Mølleåværkets procesdata.'),
        ('SRO-, SCADA- og automationssystemer', 'Erfaring med SCADA-overvågning i BIOFOS’ driftsmiljø samt el- og styringsanlæg. Ingen konkret SRO-platform, PLC-programmering eller ændringsansvar for renseprocessens automatik er oplyst.'),
        ('Miljøkrav, prøver, analyser og myndighedsrapportering', 'Tidligere ansvar for miljøgodkendelser, udledningskrav, prøvetagning, laboratorieanalyser og myndighedsindberetning er ikke dokumenteret. Arbejdsfordeling, frister og rapportering bør afklares med LTF’s miljø- og procesfaglige ansvarlige.'),
        ('Reparationer, ombygninger, projektledelse og samarbejde', 'Novo Nordisk: projektledelse af 37 samtidige CAPEX-projekter, 25 specialister, fremdrift, risiko og ressourcer. Ventek-Air: 11 samtidige anlægsprojekter; ELOHVAC: kunder, underentreprenører og aflevering. Ikke tilskrevet tidligere Mølleåværket-projekter.'),
        ('Driftsbudget og økonomisk optimering', 'ELOHVAC: fuldt P&L-ansvar, tilbudsberegning og løbende økonomi. Novo Nordisk: SAP ERP til økonomi, aktiver og omkostninger samt projektøkonomi på 37 CAPEX-projekter; direkte LTF-budgetansvar er ikke påstået.'),
        ('Arbejdsmiljøorganisation, leverandører og kolleger', 'Risikovurdering, LOTO og APV i teknisk drift; koordinering med underentreprenører, leverandører, engineering, indkøb og anlæg. Samarbejde med Mølleåværkets arbejdsmiljøorganisation og eksterne myndighedsfunktioner vil følge LTF’s roller og procedurer.')]
    m.models_table('ERFARING OG AFGRÆNSNING', ('Krav i opslaget', 'Dokumenteret erfaring og afgrænsning'), matrix,
                   widths=(2600, 7746), compact=True)
    m.models_table('UDVALGTE DOKUMENTEREDE RESULTATER', ('Leverance', 'Resultat og kontekst'), [
        ('Projektportefølje', '37 samtidige CAPEX-projekter og 25 specialister hos Novo Nordisk; DKK 2–10 mio. pr. projekt.'),
        ('Energi', '40 % lavere energiomkostninger gennem et PDCA-program hos Novo Nordisk.'),
        ('Projektteam', '11 samtidige anlægsprojekter og daglig ledelse af 14 medarbejdere hos Ventek-Air.'),
        ('Arbejdsgang', 'Over 40 % produktivitetsløft i ELOHVAC med digitale værktøjer til tilbud, tidsplaner, KS og KPI-opfølgning.')], compact=True)

    # CV page 2: experience
    m.page_break()
    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør / elautoriseret maskinmester', 'ELOHVAC ApS · København · maj 2023–nu', '5 elektrikere + 3 lærlinge · fuldt P&L-ansvar', [
            ('Personale og planlægning', 'Daglig planlægning, 1:1, medarbejdersamtaler, oplæring og arbejdsmiljøopfølgning.'),
            ('Drift og tekniske leverancer', 'Installation, tavler, styring, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg for erhvervskunder.'),
            ('Økonomi og kvalitet', 'Tilbud og beregninger, materialestyring, underentreprenører, kvalitetssikring, dokumentation og aflevering; fuldt resultatansvar.'),
            ('Digital forbedring', 'Python/Claude API-værktøjer til tilbud, tidsplaner, KS-tjeklister og KPI-dashboards; over 40 % dokumenteret produktivitetsløft.')]),
        ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen', 'Data Power Consultant ApS · København · 2024–2026 (sideløbende med ELOHVAC)', '4–10 personer', [
            ('Tekniske applikationer', 'Ledte tekniske og industrielle applikationer fra behovsafklaring og integration til idriftsættelse, dokumentation og overdragelse. Professionel AI-coding, LLM-API’er og AI-agenter indgik i arbejdsområdet.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem', 'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024', '37 samtidige CAPEX-projekter · 25 specialister · DKK 2–10 mio. pr. projekt', [
            ('Projektstyring', 'Koordinerede engineering, indkøb og anlæg; fulgte fremdrift, økonomi, risici og ressourcer og rapporterede til ledelse og bygherre.'),
            ('Kvalitet og energi', 'FAT/SAT og IQ/OQ/PQ i reguleret miljø uden kritiske afvigelser ved aflevering. PDCA-program reducerede energiomkostninger med 40 %.'),
            ('Systemer', 'SAP ERP til økonomi, aktiver og omkostninger; arbejde med el-tavler, styring og UPS.')]),
        ('Projekt- og værkstedsleder', 'Ventek-Air · København · jan. 2022–nov. 2022', '14-personers team · 11 samtidige anlægsprojekter', [
            ('Fremdrift og samarbejde', 'Styring fra specifikation til aflevering, tilbud/udbud, kapacitetsplanlægning, underentreprenører, sikkerhedsdokumentation og afleveringspakker; daglige tavlemøder og flaskehalsanalyser.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker', 'BIOFOS, Lynetten · København · aug. 2017–jan. 2022', 'Spildevandsanlæg · døgnbemandet drift', [
            ('Drift og vedligehold', 'Forebyggende vedligehold og akut fejlfinding på pumper, HVAC, højspændingstavler og SCADA; sikkerhedsdisciplin i skifteholdsdrift.'),
            ('Systematik', 'LOTO, risikovurdering og APV; 5S, Standard Work, PDCA samt forbedring af reservedelsflow på værksted og lager.')]),
        ('Elektromekaniker / produktionsteamleder', 'ARJ Engineering · Teheran · dec. 2003–mar. 2010', '12 mekanikere og teknikere', [
            ('Industriel produktion og vedligehold', 'Vagtplanlægning, materialestyring, målopfølgning, fejldiagnose og reparation af industrielt el- og mekanisk udstyr; ledelse af tekniske medarbejdere.')])]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=11, line=235)

    # CV page 3: education, methods, and first-90-days plan
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'UDDANNELSE, VÆRKTØJER OG OPSTART')
    m.section('UDDANNELSE OG CERTIFICERING')
    for title, meta in [
        ('B.Tech, Technology Management & Mechanical Engineering', 'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · EQF 6'),
        ('El- og maskinteknisk design, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6'),
        ('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023'),
        ('PRINCE2-certificeret projektleder', 'AXELOS / PeopleCert'),
        ('Køleteknik og klimaanlæg', 'AMU · Mercantec · 2021'),
        ('STCW-sikkerhed og maskinrumsvagt', 'Søfartsstyrelsen · 2021–2023')]:
        m.edu(title, meta)

    m.models_table('METODER OG SYSTEMER I PRAKSIS', ('Område', 'Dokumenteret anvendelse'), [
        ('Sikkerhed og drift', 'LOTO, APV og risikovurdering i tekniske anlæg hos ELOHVAC og BIOFOS; forebyggende vedligehold og akut fejlfinding i døgnbemandet drift.'),
        ('Forbedringsarbejde', 'PDCA, 5S, Standard Work, A3, 5xHvorfor og Ishikawa anvendt i praksis; ikke Lean-/Six Sigma-certificeret.'),
        ('Projekt og kvalitet', 'PRINCE2-certificering; FAT/SAT og IQ/OQ/PQ hos Novo Nordisk; tavlemøder og flaskehalsanalyse hos Ventek-Air.'),
        ('Personaleledelse', '1:1, medarbejdersamtaler og oplæring i ELOHVAC; daglig opgavefordeling og sikkerhedsopfølgning.'),
        ('Data og værktøjer', 'SAP ERP, Excel/Power Query, Power BI, Python, Claude API og professionel AI-coding; konkret SCADA-erfaring fra BIOFOS.')], compact=True)

    m.section('FØRSTE 90 DAGE — FORSLAG TIL DRIFT OG TEAM')
    m.models_table('TID OG FOKUS', ('Periode', 'Handling og ønsket grundlag'), [
        ('Uge 1–2', 'Mød teamet og følg vagtskifte og driftsrutiner. Saml sikkerhedsrisici, åbne fejl, kritiske aktiver og gældende miljø-/udledningskrav med de ansvarlige. Kortlæg beslutnings- og eskalationsveje.'),
        ('Dag 15–30', 'Afstem ansvar, kompetencer og daglig opfølgning med medarbejderne. Gennemgå vedligeholdsplan, reservedele, prøvetagningsplan, analysefrister og myndighedsrapportering med miljø- og procesfagpersoner.'),
        ('Dag 31–60', 'Sammenhold SCADA-/driftsdata, prøveresultater, fejl og vedligehold. Prioritér større arbejder og budgetrisici med driftschefen; aftal sikre grænseflader mellem drift og projekter.'),
        ('Dag 61–90', 'Vælg én afgrænset forbedring med team og relevante specialister. Aftal før/efter-målepunkter for drift, miljø og økonomi; gennemgå læring og næste kompetencebehov.'),
        ('Løbende', 'Hold fast i den daglige dialog og månedlige budget-/risikogennemgang; justér planen, hvis drift, miljøkrav eller anlæggets tilstand ændrer sig.')], compact=True)
    m.para('Sprog: dansk og persisk/farsi — modersmål · engelsk — professionelt. Kørekort B. Bopæl: Måløv.', after=25, line=235, justify=False)

    return m.save(str(out), title='Ansøgning og CV — Driftsleder, Mølleåværket',
                  subject='Sikker drift, vedligehold og personaleledelse',
                  keywords='Driftsleder, Mølleåværket, spildevand, renseanlæg, SCADA, vedligehold, miljøkrav, personaleledelse')


if __name__ == '__main__':
    print(build(ROOT / 'Shahram_Ajloo_LTF_Moelleaavaerket_AnsogningCV.docx'))
