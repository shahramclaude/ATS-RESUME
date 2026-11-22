# -*- coding: utf-8 -*-
"""Det Kgl. Bibliotek — teknisk projektleder: ansøgning, CV og kravmatrix.
Dokumenterne skelner mellem dokumenteret erfaring, overførbare kompetencer og krav, der
beror på myndighedsgodkendelse. CTS/BMS-erfaring fremstilles præcist som BMS/FMS i Novo.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from master_design import MasterDoc
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

R = Path(__file__).resolve().parent.parent
TEMPLATE = R / 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'
NAME = 'SHAHRAM AJLOO'
TITLE = 'Elautoriseret maskinmester | tekniske projekter, bygningsdrift og vedligehold'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv (Ballerup Kommune)'
DATE = '3. november 2026'
OUT = R / 'Shahram_Ajloo_DetKglBibliotek_TekniskProjektleder.docx'

LETTER = [
 ('Et teknisk projekt er først reelt afleveret, når driftskollegerne kan finde den opdaterede dokumentation, forstå installationen og vedligeholde den uden at være afhængige af projektlederen.', 'opening'),
 ('Det er forbindelsen mellem projektleverance og daglig drift, der gør stillingen i Bygningsdrift særlig. På Det Kgl. Bibliotek skal tekniske projekter og vedligehold fungere på tværs af en varieret bygningsmasse — fra arbejdsstedet bag Den Sorte Diamant til magasinet i Frederikssund — mens brugere, medarbejdere og kulturarv fortsat har brug for bygningerne.', 'para'),
 ('En praktisk projekt- og driftsrytme begynder med en fælles afklaring af behov, anlæg, adgang, risici og hvad bygningens drift ikke må miste under arbejdet. Herefter fastlægges omfang, budget, tidsplan, snitflader og acceptkriterier med interne kolleger, rådgiver og udførende leverandør. Under udførelsen følges kvalitet, sikkerhed og ændringer op på stedet; ved aflevering kontrolleres funktion, restpunkter og dokumentation. Tegninger, anlægsdata og vedligeholdsgrundlag opdateres, inden ansvaret går tilbage til den daglige drift.', 'para'),
 ('Den samme disciplin gælder de mindre opgaver og servicebesøg: bestillingen skal være tydelig, adgang og forventninger aftalt, og leverandørens arbejde vurderes mod den konkrete opgave. Tilbagevendende fejl eller uklare dokumenter bliver synlige på en prioriteret liste, så forebyggende vedligehold og ændringsprojekter ikke konkurrerer uplanlagt om tid og adgang.', 'para'),
]
SOLUTION = [
 ('Projekt fra behov til drift', 'Afgræns funktion, økonomi, tidsvindue og risici; koordinér interne fag, rådgivere og leverandører; følg udførelse og ændringer; afprøv og aflever med opdateret dokumentationspakke.'),
 ('Daglig drift og service', 'Prioritér akut fejl, planlagt vedligehold og projektarbejde efter konsekvens for brugere, bygning og installation. Aftal adgang og leverance med håndværkere, serviceleverandører og rådgivere, og luk opgaven med kontrol og registrering.'),
 ('Teknisk dokumentation', 'Hold tegninger, anlægsoplysninger, test/commissioning og vedligeholdsdata sammen med den faktiske installation. Afvigelser fra projektmaterialet indarbejdes, så driftsteamet kan finde gældende version og bruge den i næste indgreb.'),
]
CULTURE = ('Det Kgl. Bibliotek beskriver sig som hele Danmarks bibliotek. Strategiens formulering “Vi indsamler, bevarer og formidler vores fælles viden og kulturarv” gør bygninger og magasiner til en del af kerneopgaven, ikke blot en teknisk ramme; de skal understøtte “rum til fordybelse og fællesskab” og ambitionen “Vi viser vej til viden”. Det kræver, at en energieffektiv eller moderniseret installation også respekterer bygningens brug og samlingernes bevaringsbehov. I klimastrategien er bygnings- og magasindrift et indsatsområde i arbejdet for et grønnere bibliotek og et klimavenligt samfund. Strategien fremhæver en helhedsorienteret anvendelse af vores lokaliteter og den samlede bygningsmasse. Det passer til en rolle i Bygningsdrift med 16 kolleger fordelt mellem Aarhus og København og et samlet bygningsareal på ca. 120.000 m². Jeg hæfter mig også ved ambitionen om en attraktiv, inspirerende og inkluderende arbejdsplads med sundt arbejdsmiljø, balanceret arbejdsliv og leder- og medarbejderudvikling; fysisk fremmøde og fleksibel arbejdstid er konkrete vilkår i opslaget.')
CLOSING = ('Jeg har gyldigt kørekort kategori B og er indstillet på at blive sikkerhedsgodkendt til hemmeligt gennem den proces, som stillingen forudsætter; jeg påstår ikke, at en eksisterende godkendelse allerede dækker dette niveau. Tiltrædelse i februar 2027 eller efter aftale kan drøftes. Ansøgningen er målrettet opslagets elektroniske ansøgningsvej.')
PROFILE = ('Elautoriseret maskinmester (LV/MV/HV), B.Tech i Technology Management & Mechanical Engineering og teknisk projektleder med erfaring fra el-, HVAC- og mekaniske installationer, vedligehold, idriftsættelse og projektleverance. ELOHVAC omfatter service, fejlfinding og vedligehold af el-, ventilations- og klimaanlæg, planlægning, underentreprenører, kvalitet og afleveringsdokumentation. Hos Novo Nordisk koordinerede jeg 37 CAPEX-projekter og 25 specialister med FAT/SAT og IQ/OQ/PQ; Ventek-Air omfattede 11 samtidige tekniske projekter og et 14-personers team. Jeg har desuden bekræftet direkte ansvar for ejendomsdrift og vedligeholdelse på tværs af en portefølje. BMS/FMS-erfaring er bekræftet i Novo Nordisk-sammenhæng; specifik CTS-platformserfaring på Det Kgl. Bibliotek er ikke dokumenteret.')
RESULTS = [
 ('37 samtidige CAPEX-projekter', 'Novo Nordisk: DKK 2–10 mio. pr. projekt; koordinering af fremdrift, risici, økonomi og 25 specialister.'),
 ('Nul kritiske fund ved aflevering', 'Novo Nordisk: FAT/SAT og IQ/OQ/PQ i GMP-miljø; dokumenteret test- og overdragelsesdisciplin.'),
 ('11 samtidige tekniske projekter', 'Ventek-Air: planlægning og fremdrift fra specifikation til formel aflevering; 14-personers team.'),
 ('40 % lavere energiomkostninger', 'Novo Nordisk: resultat af et PDCA-program i den pågældende organisation.'),
 ('5 elektrikere + 3 lærlinge', 'ELOHVAC: daglig planlægning, kundeleverance, sikkerhed, leverandører og fuldt P&L-ansvar.'),
]
EXPERIENCE = [
 ('Ejer / teknisk direktør / elautoriseret maskinmester', 'ELOHVAC ApS · København · maj 2023 – nu', '5 elektrikere + 3 lærlinge · fuldt P&L', [
  ('Service og vedligehold', 'Udfører elteknisk service, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg; følger op fra akut henvendelse til kvalitetssikret aflevering.'),
  ('Projekt- og leverandørstyring', 'Afklarer opgaven, udarbejder tilbud og beregning, planlægger ressourcer og materialer og koordinerer underentreprenører og leverandører gennem udførelse og aflevering.'),
  ('Dokumentation og ledelse', 'Følger KS, arbejdsmiljø og afleveringsdokumentation; leder fem elektrikere og tre lærlinge med daglig opgavefordeling, oplæring og opfølgning.')]),
 ('Medejer og CTO / ansvarlig for AI-afdelingen', 'Data Power Consultant ApS · København · 2024 – nov. 2026 (sideløbende med ELOHVAC)', '4–10 personer i AI- og AI coding-afdelingen', [
  ('Tekniske løsninger', 'Ledte udvikling fra krav og arkitektur til integration, test, dokumentation og overdragelse; standardiserede review og kvalitet. Selskabet ophørte i november 2026.')]),
 ('Senior idriftsættelsesingeniør / projektleder, elsystemer', 'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024', '37 CAPEX-projekter · DKK 2–10 mio. pr. projekt · 25 specialister', [
  ('Portefølje og tværfaglig koordinering', 'Koordinerede fremdrift, økonomi, risici og ressourcer på tværs af engineering, indkøb og anlæg; månedlig rapportering til ledelse og bygherre.'),
  ('Commissioning og dokumentation', 'Arbejdede med FAT/SAT og IQ/OQ/PQ under GMP; nul kritiske fund ved aflevering. BMS/FMS-arbejde i drift/projekter er kandidatbekræftet, men ikke knyttet til en navngiven CTS-platform.')]),
 ('Projekt- og værkstedsleder, ventilation og klima', 'Ventek-Air · København · jan. 2022 – nov. 2022', '11 samtidige projekter · 14-personers team', [
  ('Leverance og dokumenter', 'Koordinerede projekter fra specifikation til formel aflevering; udbud/tilbud, aftalegrundlag, entreprenører, sikkerhedsdokumentation og afleveringspakker indgik i leverancen.')]),
 ('Vedligeholdelses- og driftsleder / værkstedstekniker', 'BIOFOS (Lynetten) · København · aug. 2017 – jan. 2022', 'Kritisk 24/7-procesanlæg', [
  ('Teknisk drift', 'Forebyggende vedligehold og akut fejlfinding på pumper, HVAC og højspændingstavler; SCADA-overvågning i kritisk 24/7-drift.'),
  ('Sikkerhed og orden', 'Arbejdede med LOTO, risikovurdering, APV, nærved-rapportering, 5S, Standard Work og reservedelsflow i vedligehold og værkstedsdrift.')]),
 ('Elektromekaniker / produktionsteamleder', 'ARJ Engineering · Teheran · dec. 2003 – mar. 2010', '12 mekanikere og teknikere', [
  ('Teknik og personaleledelse', 'Vagtplanlægning, materialer og målopfølgning samt fejldiagnose og reparation på industrielle elektriske og mekaniske anlæg.')]),
]
EDUCATION = [
 ('B.Tech — Technology Management & Mechanical Engineering', 'Copenhagen School of Marine Engineering & Technology Management · 2017–2022'),
 ('Køleteknik og klimaanlæg (AMU)', 'Mercantec · 2021'),
 ('HF — matematik og fysik', 'VUC · 2012–2017'),
 ('El- og maskinteknisk design, elteknik', 'Tehran Technical University · 2000–2003'),
]
QUALIFICATIONS = [
 ('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023'),
 ('STCW A-III/1 — maskinrums-/vagtkvalifikation', 'Søfartsstyrelsen · 2021–2023'),
 ('PRINCE2 — certificeret projektleder', 'AXELOS / PeopleCert'),
]
REQUIREMENTS = [
 ('Teknisk projektleder: tekniske projekter og daglig vedligeholdelse', 'ELOHVAC kombinerer projektstyring, teknisk service og forebyggende vedligehold af el-, ventilations- og klimaanlæg. Novo Nordisk leverede CAPEX-projekter fra planlægning til test og aflevering; BIOFOS dækkede den daglige vedligeholdelse af kritiske installationer.'),
 ('Solid teknisk baggrund: maskinmester eller tilsvarende', 'Elautoriseret maskinmester (LV/MV/HV) og B.Tech i Technology Management & Mechanical Engineering. Praktisk elteknisk og elektromekanisk erfaring supplerer uddannelsen; ingen anden autorisation end den dokumenterede elautorisation påstås.'),
 ('Erfaring med bygningsdrift', 'Kandidaten har bekræftet direkte ansvar for ejendomsdrift og vedligeholdelse på tværs af en portefølje. ELOHVAC dokumenterer HVAC- og elservice, mens BIOFOS dokumenterer kritisk teknisk drift; arbejdsgiver og omfang for porteføljeansvaret er ikke specificeret.'),
 ('CTS/BMS-anlæg er en fordel', 'BMS/FMS-arbejde i Novo Nordisk-drift og projekter er kandidatbekræftet, sammen med commissioning og FAT/SAT. Det dokumenterer ikke erfaring med en bestemt CTS-platform eller Det Kgl. Biblioteks automatik; systemoplæring vil være nødvendig.'),
 ('Gennemføre større tekniske projekter', 'Novo Nordisk: 37 samtidige CAPEX-projekter á DKK 2–10 mio.; fremdrift, økonomi, risiko og 25 tværfaglige specialister koordineret. FAT/SAT og IQ/OQ/PQ indgik, og afleveringerne havde nul kritiske fund.'),
 ('Gennemføre mindre tekniske projekter', 'ELOHVAC omfatter afgrænsning, tilbud, beregning, materialer, udførelse, underentreprenører, KS og aflevering af tekniske arbejder. Ventek-Air omfattede parallelle anlægsprojekter fra specifikation til formel aflevering.'),
 ('Ombygningsprojekter på tekniske anlæg', 'Tekniske anlægs- og CAPEX-leverancer hos Novo Nordisk og Ventek-Air omfattede koordinering fra specifikation til aflevering. Den konkrete type ombygning pr. projekt er ikke specificeret i master-CV’et; metoden til scope, sikker udførelse og overdragelse er dokumenteret.'),
 ('Ændringsprojekter på tekniske anlæg', 'ELOHVAC planlægger ændringer i el-, ventilations- og klimainstallationer med materialer, entreprenører, KS og aflevering. Novo Nordisk dokumenterer test- og change-control-orienteret commissioning; konkrete KB-installationer eller ændringsvolumener tilskrives ikke.'),
 ('Varetage daglig drift af anlæg', 'BIOFOS dokumenterer forebyggende vedligehold, akut fejlfinding og SCADA-overvågning i 24/7-procesdrift. ELOHVAC leverer daglig service på tekniske installationer, og kandidaten har bekræftet direkte ansvar for ejendomsdrift og porteføljevedligehold.'),
 ('Struktureret anvendelse af teknisk dokumentation', 'Novo Nordisk: FAT/SAT, IQ/OQ/PQ, test- og afleveringsdokumentation i GMP. Ventek-Air: sikkerhedsdokumentation og afleveringspakker. ELOHVAC: KS og afleveringsdokumentation; brug af dokumenter kobles til udført arbejde og kvalitet.'),
 ('Vedligeholde teknisk dokumentation', 'I projekt- og serviceleverancer er dokumentation fulgt sammen med KS, test og aflevering. ELOHVAC omfatter afleveringsdokumentation; Novo Nordisk omfattede commissioning-records. Ingen specifik KB-dokumentplatform påstås kendt.'),
 ('Opdatere teknisk dokumentation', 'Aflevering hos Ventek-Air og Novo Nordisk omfattede dokumentationspakker og overdragelse. Den praktiske tilgang er at indarbejde as-built-afvigelser og testresultater, kontrollere version og ansvarlig ejer og aflevere gældende materiale til drift.'),
 ('Arbejde både på kontor og ude i bygninger', 'Projektarbejde spænder fra tilbud, planlægning og rapportering til koordinering på anlæg og byggeplads. Novo Nordisk krævede tværfaglig opfølgning; ELOHVAC og Ventek-Air omfattede udførelse, leverandører og fysisk aflevering.'),
 ('Håndtere eksterne serviceleverandører', 'ELOHVAC dokumenterer leverandør- og underentreprenørkoordinering, materialestyring og fuldt P&L-ansvar. Opgaver afgrænses, forventninger aftales og kvalitet/aflevering følges op; ingen KB-specifik leverandøraftale hævdes.'),
 ('Håndtere håndværkere', 'ELOHVAC leder fem elektrikere og tre lærlinge og koordinerer underentreprenører i tekniske service- og projektleverancer. Ventek-Air koordinerede entreprenører på 11 samtidige projekter; Novo Nordisk koordinerede udførende og faglige grænseflader.'),
 ('Håndtere rådgivere', 'Novo Nordisk-projekter krævede koordinering på tværs af engineering, indkøb og anlæg samt rapportering til bygherre; Ventek-Air havde udbud, aftalegrundlag og tekniske afleveringer. Rådgiverrollen på KB vil følge projektets mandat og grænseflader.'),
 ('Servicere samarbejdspartnere og sikre bedst mulig ydelse', 'ELOHVAC arbejder med kundedialog, tilbud, planlægning, underentreprenører, KS og aflevering; fuldt P&L giver ansvar for at få leverancen til at fungere. Ventek-Air fulgte partnernes fremdrift og dokumentation til formel aflevering.'),
 ('Serviceminded og ansvarsfuld i arbejdet', 'Adfærden vises gennem kundeansvar i ELOHVAC, kvalitetssikring og aflevering samt sikkerhedsdisciplin i BIOFOS. Eksemplerne knytter ansvarlighed til konkrete tekniske leverancer frem for at bruge personlige superlativer.'),
 ('Arbejde selvstændigt og tage ejerskab', 'Som ejer/teknisk direktør i ELOHVAC varetager kandidaten opgaveafgrænsning, ressourcer, sikkerhed, leverandører og økonomi. I KB-rollen vil beslutninger fortsat følge myndighedskrav, sikkerhedsprocedurer og aftalte beslutningsmandater.'),
 ('Prioritere arbejdsopgaver', 'ELOHVAC kombinerer serviceopgaver, medarbejdere, materialer, entreprenører og fuldt P&L; hos Novo Nordisk blev 37 samtidige projekter prioriteret på risiko, ressourcer og fremdrift. Den konkrete KB-portefølje og hasteklassifikation læres lokalt.'),
 ('Rutineprægede og komplekse opgaver', 'BIOFOS vedligehold og driftsrutiner stod side om side med akut fejlfinding; ELOHVAC kombinerer gentagen service og komplekse installationsopgaver. Det viser erfaring med både faste driftsopgaver og projektmæssige problemstillinger.'),
 ('Samarbejde med forskellige faglige baggrunde', 'Novo Nordisk: 25 specialister koordineret på tværs af engineering, indkøb og anlæg; Ventek-Air: 14-personers team og entreprenører. ELOHVAC forbinder teknikere, kunder, leverandører og underentreprenører omkring én leverance.'),
 ('Bygningsportefølje i København, Vinge og Aarhus', 'Stillingsopslaget beskriver ca. 120.000 m² og opgaver flere steder. Kandidatens porteføljeansvar for ejendomsdrift er bekræftet uden oplyst antal eller geografi; relevante konkrete erfaringer er HVAC-service, vedligehold og teknisk projektleverance.'),
 ('37 timer, fysisk fremmøde og fleksibel arbejdstid', 'Opslaget fastlægger 37 timer med fysisk fremmøde og mulighed for fleksibel arbejdstid. Kandidaten bor i Måløv og har gyldigt kategori-B-kørekort; ingen fjernarbejds- eller fast fremmødeaftale er antaget.'),
 ('Gyldigt kørekort kategori B', 'Master-CV dokumenterer gyldigt kørekort kategori B med manuelt gear. Det matcher transportkravet mellem bibliotekets adresser; kørekortet præsenteres som bekræftet kvalifikation.'),
 ('Kunne sikkerhedsgodkendes til hemmeligt', 'Master-CV registrerer en tidligere brugerbekræftet sikkerhedsgodkendelse, der blev vurderet egnet til en anden rolle, men niveau, gyldighed og identifikator fremgår ikke. Den må derfor ikke sidestilles med KB’s krav; kandidaten er indstillet på at blive sikkerhedsgodkendt til hemmeligt gennem den formelle vurdering.'),
 ('Tiltrædelse forventeligt februar 2027', 'Opslaget angiver forventet tiltrædelse februar 2027 og mulighed for at vente på rette kandidat. Ansøgningen fastsætter ikke en individuel startdato; den kan aftales i forbindelse med rekrutteringsforløbet.'),
 ('Elektronisk ansøgning med ansøgning og CV', 'Materialet er udarbejdet som særskilt ansøgning og CV, så de kan vedlægges via bibliotekets elektroniske ansøgningslink. Eventuelle anbefalinger vedlægges kun, hvis de foreligger; ingen anbefalinger er opfundet.'),
 ('Ansøgningsfrist 27. november 2026', 'Ansøgningen skal være modtaget senest 27. november 2026 ifølge brugerens opslag. Materialet er gjort klar til det elektroniske link, men ansøgningen sendes ikke uden brugerens udtrykkelige tilladelse.'),
 ('Samtaler 2.–3. og 9. december 2026; test før anden samtale', 'Opslaget planlægger første samtale 2. og 3. december, anden samtale 9. december og personlighedstest før anden samtale. Dette registreres som arbejdsgiverens tidsplan; kandidatens deltagelse skal aftales, ikke antages.'),
]

def add_letter(m):
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta('Det Kgl. Bibliotek · Bygningsdrift · Søren Kirkegaards Plads 1, 1221 København K')
    p = m._p(spacing_after=70, line=250, justify=False)
    m._run(p, 'Ansøgning: Teknisk projektleder', bold=True, color='1A1A1A')
    for text, kind in LETTER: m.para(text, after=45 if kind == 'opening' else 35, line=238)
    for a,b in SOLUTION: m.bullet(a,b,after=22,line=235)
    m.para(CULTURE, after=32, line=232)
    m.para(CLOSING, after=30, line=232)
    m.meta('Med venlig hilsen', after=12)
    m.meta('Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com', after=0)

def add_cv(m):
    m.resume_header(NAME, TITLE, CONTACT, 'TEKNISK PROFIL')
    m.para(PROFILE, after=35, line=232)
    m.section('RESULTATER RELEVANTE FOR BYGNINGSDRIFT')
    for a,b in RESULTS: m.bullet(a,b,after=15,line=230)
    m.section('ERHVERVSERFARING — NYESTE FØRST')
    for title, meta, scope, bullets in EXPERIENCE[:4]:
        m.job(title,meta,scope=scope)
        for a,b in bullets: m.bullet(a,b,after=14,line=230)
    m.page_break()
    m.resume_header(NAME, 'Teknisk projektledelse | bygningsdrift | vedligehold', CONTACT, 'ERHVERVSERFARING FORTSAT | UDDANNELSE')
    for title, meta, scope, bullets in EXPERIENCE[4:]:
        m.job(title,meta,scope=scope)
        for a,b in bullets: m.bullet(a,b,after=14,line=230)
    m.section('UDDANNELSE — SENESTE FØRST')
    for a,b in EDUCATION: m.edu(a,b)
    m.section('AUTORISATIONER OG CERTIFICERINGER')
    for a,b in QUALIFICATIONS: m.edu(a,b)
    m.section('FAGLIGE METODER OG IT')
    m.para('Projektleverance · vedligehold · anvendelse, vedligeholdelse og opdatering af teknisk dokumentation · FAT/SAT · IQ/OQ/PQ · BMS/FMS (Novo Nordisk, kandidatbekræftet) · LOTO · risikovurdering · 5S · PDCA · SAP ERP · Excel · Power BI · Python.', after=22, line=230, justify=False)
    m.section('SPROG OG PRAKTISK')
    m.para('Dansk og persisk (modersmål) · engelsk (professionelt) · kørekort B (manuelt gear) · bopæl Måløv. Kandidaten er indstillet på at medvirke i sikkerhedsgodkendelsesprocessen til hemmeligt; endelig godkendelse beror på myndighedens vurdering.', after=22, line=230, justify=False)

def build_all():
    combined = MasterDoc(str(TEMPLATE), lang='da-DK')
    add_letter(combined)
    combined.page_break()
    add_cv(combined)
    combined.page_break()
    combined.resume_header(NAME, 'Dokumenteret match til teknisk projektledelse og bygningsdrift', CONTACT, 'KRAV- OG EVIDENSMATRIX')
    table = combined.models_table('KRAVMATRIX', ('Krav i stillingsopslaget','Dokumentation / erfaring og afgrænsning'), REQUIREMENTS, widths=(3950,6396))
    trpr = table.rows[1]._tr.get_or_add_trPr()
    repeat = OxmlElement('w:tblHeader'); repeat.set(qn('w:val'),'true'); trpr.append(repeat)
    combined_path = combined.save(str(OUT), title='Ansøgning og CV — Det Kgl. Bibliotek, teknisk projektleder', subject='Teknisk projektleder, Bygningsdrift', keywords='Det Kgl. Bibliotek; teknisk projektleder; bygningsdrift; maskinmester; BMS; CTS; vedligehold; dokumentation')

    letter = MasterDoc(str(TEMPLATE), lang='da-DK')
    add_letter(letter)
    letter_path = letter.save(str(R / 'Shahram_Ajloo_DetKglBibliotek_Ansogning.docx',), title='Ansøgning — Det Kgl. Bibliotek, teknisk projektleder', subject='Teknisk projektleder, Bygningsdrift', keywords='tekniske projekter; bygningsdrift; dokumentation; serviceleverandører')

    cv = MasterDoc(str(TEMPLATE), lang='da-DK')
    add_cv(cv)
    cv_path = cv.save(str(R / 'Shahram_Ajloo_DetKglBibliotek_CV.docx'), title='CV — Shahram Ajloo — Det Kgl. Bibliotek', subject='Teknisk projektleder, Bygningsdrift', keywords='maskinmester; projektledelse; teknisk dokumentation; BMS/FMS; vedligehold')
    return combined_path, letter_path, cv_path

if __name__ == '__main__':
    for path in build_all(): print(path)
