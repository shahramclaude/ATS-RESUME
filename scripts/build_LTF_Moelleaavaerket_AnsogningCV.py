"""Mølleåværket: jobfokuseret ansøgning og CV i uploadet masterstil."""
from pathlib import Path
from master_design import MasterDoc
R=Path(__file__).resolve().parent.parent
m=MasterDoc(str(R/'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='da-DK')
n='SHAHRAM AJLOO';t='Driftsleder — Mølleåværket | Lyngby-Taarbæk Forsyning'
c='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
m.header_banner(n,t,c);m.meta('Lyngby-Taarbæk Forsyning · Att.: Jannik Lund Olsen',after=25)
m.para('**Ansøgning: Driftsleder til Mølleåværket**',after=80,justify=False)
m.para('Kære Jannik Lund Olsen',after=75,justify=False)
m.para('Mølleåværket skal rense spildevandet stabilt og overholde miljøkravene, samtidig med at anlæg og medarbejdere udvikles. Det kræver en driftsleder, der er tæt på den daglige drift, prioriterer vedligeholdet og træffer beslutninger i samarbejde med dem, der kender anlægget. Den opgave vil jeg gerne løse sammen med jeres seks driftsmedarbejdere.',after=80,line=255,justify=False)
m.para('**En sikker drift med plads til forbedring**',after=45,justify=False)
for a,b in [
('Drift og medarbejdere','Jeg vil etablere en fast gennemgang af anlæggets tilstand, bemanding og opgaver sammen med teamet. Tydelige prioriteringer og overleveringer skal sikre, at både akutte fejl og planlagt vedligehold bliver fulgt til dørs. Gennem individuelle samtaler og faglig sparring vil jeg arbejde med kompetenceudvikling, trivsel og motivation og give medarbejderne plads til at bruge deres viden.'),
('Miljø og dokumentation','Miljøgodkendelser og udledningskrav skal være omsat til klare opgaver, ansvar og frister. Sammen med de relevante fagpersoner vil jeg sikre korrekt dokumentation af driftsforhold, prøvetagning og analyser samt rettidig rapportering til myndigheder. Afvigelser skal undersøges og følges op efter anlæggets procedurer.'),
('Vedligehold og sikkerhed','Vedligeholdelsesaktiviteter skal planlægges efter anlæggenes tilstand og betydning for sikkerhed, rensekvalitet og oppetid. Ved større reparationer og ombygninger vil jeg aftale arbejdsplan, risikovurdering, sikker afstilling og overdragelse med specialister, leverandører, projektledere og arbejdsmiljøorganisationen.'),
('Driftsdata og optimering','Jeg vil bruge driftsdata, SRO/SCADA, prøveresultater og medarbejdernes observationer til at identificere afvigelser og forbedringsmuligheder. Ændringer i proces og automation skal vurderes med anlæggets specialister og følges op, så de fungerer i den daglige drift og ikke kompromitterer udledningskravene.'),
('Budget og anlæggenes levetid','Jeg vil følge driftsbudgettet og bidrage til budgetlægningen med et overblik over forbrug, vedligeholdsbehov og større arbejder. Prioriteringerne skal afstemmes med driftschefen og bygge på konsekvenser for driftssikkerhed, levetid og økonomi. Forsyningens arbejde med energiforbrug og ressourceudnyttelse er en naturlig del af den vurdering.')]:m.bullet(a,b,after=40,line=245)
m.para('På BIOFOS’ renseanlæg Lynetten arbejdede jeg med pumper, el- og mekaniske anlæg, SCADA og forebyggende vedligehold i døgnbemandet drift. I ELOHVAC har jeg personale- og resultatansvar, og hos Novo Nordisk har jeg koordineret tekniske projekter og dokumentation i et reguleret miljø. Den erfaring vil jeg bruge til at skabe sammenhæng mellem sikkerhed, mennesker og teknisk drift på Mølleåværket.',after=55,line=250,justify=False)
m.para('Jeg vil gerne aftale et forløb for den relevante driftslederuddannelse på spildevandsområdet. Jeg ser frem til en samtale om, hvordan vi sammen kan sikre den daglige drift og udvikle anlægget med respekt for medarbejdernes faglighed.',after=45,line=250,justify=False)
m.meta('Med venlig hilsen',after=15);m.meta('Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com',after=0)
m.page_break();m.resume_header(n,t,c,'DRIFTSPROFIL — RENSEANLÆG, MENNESKER OG TEKNIK')
m.para('Erfaring med teknisk drift og vedligehold på BIOFOS’ renseanlæg Lynetten samt ledelse af tekniske medarbejdere og projekter. Arbejdet omfatter blandt andet pumper, el-anlæg og SCADA, planlægning af vedligehold og håndtering af akutte fejl. Som elautoriseret maskinmester har jeg desuden arbejdet med økonomi, sikkerhed og teknisk dokumentation i både servicevirksomhed og reguleret industri.',after=65,line=255,justify=False)
m.section('FAGLIGE OG LEDELSESMÆSSIGE KOMPETENCER')
for a,b in [
('Teknisk drift og vedligehold','Erfaring fra Lynetten med drift af pumper, ventilationsanlæg og højspændingstavler samt overvågning via SCADA. Arbejdet omfattede forebyggende vedligehold og fejlfinding i døgnbemandet drift.'),
('Personaleledelse','Daglig planlægning, medarbejdersamtaler og oplæring af fem elektrikere og tre lærlinge i ELOHVAC. Tidligere ansvar for et team på 14 medarbejdere hos Ventek-Air.'),
('Arbejdsmiljø og kvalitet','Arbejder med risikovurdering, APV og sikker afstilling af anlæg. Hos Novo Nordisk indgik test og dokumentation i aflevering af anlæg uden kritiske afvigelser.'),
('Driftsdata og forbedringer','Erfaring med SCADA fra Lynetten og med systematisk forbedringsarbejde, herunder 5S og PDCA. Digitale planlægningsværktøjer bidrog til et produktivitetsløft på over 40 % i ELOHVAC.'),
('Økonomi og samarbejde','Fuldt resultatansvar i ELOHVAC og erfaring med økonomi- og risikostyring i tekniske projekter. Koordinerer opgaver med medarbejdere, specialister, leverandører og underentreprenører.')]:m.bullet(a,b,after=20,line=245)
m.models_table('PRIORITERINGER I DRIFTSLEDELSEN — FORSLAG', ('Område', 'Praktisk tilgang'), [
('Daglig ledelse','Gennemgå opgaver, bemanding og åbne fejl med teamet; følg op på trivsel og kompetenceudvikling.'),
('Miljø og dokumentation','Overblik over udledningskrav, prøver, analyser, frister og ansvar sammen med relevante fagpersoner.'),
('Vedligehold','Prioritering efter risiko for arbejdsmiljø, rensekvalitet og oppetid; plan for kritiske anlægsdele.'),
('Driftsdata','Brug SRO/SCADA-data, prøveresultater og observationer til at finde afvigelser og følge forbedringer.'),
('Økonomi og projekter','Budgetlægning og budgetopfølgning samt koordinering af sikkerhed, ressourcer og overdragelse ved projekter.')])
m.section('UDVALGT ERFARING OG RESULTATER')
for a,b in [('Renseanlæg','Drift og vedligehold af tekniske anlæg på BIOFOS/Lynetten, herunder pumper og højspændingstavler samt overvågning via SCADA.'),('Projektledelse','Koordinerede 25 specialister på 37 samtidige anlægsprojekter hos Novo Nordisk. Anlæggene blev afleveret uden kritiske afvigelser.'),('Daglig ledelse','Ledede 14 medarbejdere og planlagde kapaciteten på 11 samtidige projekter hos Ventek-Air.'),('Virksomhedsdrift','Ansvar for fem elektrikere og tre lærlinge samt virksomhedens resultat i ELOHVAC. Digitale værktøjer bidrog til et produktivitetsløft på over 40 %.')]:m.bullet(a,b,after=15,line=235)
m.page_break()
m.section('ERHVERVSERFARING')
m.job('Ejer / teknisk direktør / elautoriseret maskinmester','ELOHVAC ApS · København · maj 2023–nu')
for a,b in [('Mennesker og planlægning','Leder fem elektrikere og tre lærlinge og står for daglig planlægning, medarbejdersamtaler, oplæring og arbejdsmiljø.'),('Drift og teknik','Udfører installation, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg for erhvervskunder.'),('Økonomi og kvalitet','Har fuldt resultatansvar og varetager tilbud, beregning, materialestyring, underentreprenører og kvalitetssikring.'),('Forbedring','Egne AI-værktøjer til tilbud, tidsplaner og kvalitetstjek har bidraget til over 40 % produktivitetsløft.')]:m.bullet(a,b,after=15,line=245)
m.job('Medejer og CTO / teknisk ansvarlig for AI-afdelingen','Data Power Consultant ApS · København · 2024–nov. 2026')
m.bullet('Tekniske løsninger','Ledede en afdeling med 4–10 personer og arbejdede med tekniske applikationer fra behovsafklaring til dokumentation og overdragelse. Stillingen var sideløbende med ELOHVAC; virksomheden er ophørt.',after=15,line=245)
m.job('Senior idriftsættelsesingeniør / projektleder, elsystem','Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024')
for a,b in [('Projekter og ressourcer','Koordinerede 25 specialister på 37 samtidige anlægsprojekter og fulgte fremdrift, økonomi, risici og ressourcer på tværs af fagområder.'),('Kvalitet og aflevering','Planlagde og gennemførte test og dokumentation, herunder FAT/SAT og IQ/OQ/PQ, i et reguleret miljø. Anlæggene blev afleveret uden kritiske afvigelser.')]:m.bullet(a,b,after=18,line=245)
m.job('Projekt- og værkstedsleder','Ventek-Air · København · jan. 2022–nov. 2022')
for a,b in [('Planlægning og mennesker','Ledede 14 medarbejdere og styrede 11 samtidige projekter med kapacitets- og fremdriftsstyring.'),('Sikkerhed og samarbejde','Arbejdede med tilbud, aftaler, underentreprenører, sikkerhedsdokumentation og aflevering. Brugte tavlemøder og flaskehalsanalyser til at følge fremdriften.')]:m.bullet(a,b,after=18,line=245)
m.job('Vedligeholdelses- og driftsleder / værkstedstekniker','BIOFOS, Lynetten · København · aug. 2017–jan. 2022')
for a,b in [('Kritisk drift','Arbejdede med el- og mekanisk drift på renseanlægget, herunder pumper, ventilationsanlæg, højspændingstavler og SCADA. Udførte forebyggende vedligehold og akut fejlfinding.'),('Sikkerhed og systematik','Indgik i skifteholdsdrift med fokus på sikker afstilling, risikovurdering og APV. Arbejdede med reservedelsflow og forbedringer på værksted og lager.')]:m.bullet(a,b,after=18,line=245)
m.job('Elektromekaniker / produktionsteamleder','ARJ Engineering · Teheran · dec. 2003–mar. 2010')
m.bullet('Drift og medarbejdere','Ledede 12 mekanikere og teknikere og havde ansvar for vagtplanlægning og materialestyring. Arbejdede med fejldiagnose og reparation af industrielle el- og mekaniske anlæg.',after=18,line=245)
m.section('UDDANNELSE, METODER OG SPROG')
for a,b in [('B.Tech, Technology Management and Mechanical Engineering','Copenhagen School of Marine Engineering & Technology Management · 2017–2022'),('Elautoriseret maskinmester, LV/MV/HV','Sikkerhedsstyrelsen · 2023'),('PRINCE2 certificeret projektleder','AXELOS / PeopleCert'),('Køleteknik og klimaanlæg','Mercantec AMU · 2021'),('El- og maskinteknisk design, elteknik','Tehran Technical University · 2000–2003')]:m.edu(a,b)
m.para('**Metoder:** Lean, Six Sigma og PRINCE2 anvendt i praksis; certificeret i PRINCE2. **Systemer:** SCADA, Excel, SAP ERP og digitale planlægningsværktøjer. **Sprog:** dansk, engelsk og persisk. **Kørekort:** B.',after=20,line=245,justify=False)
m.page_break()
m.models_table('FØRSTE 90 DAGE — FORSLAG TIL PRIORITERINGER', ('Hvornår', 'Fokus og handling'), [
('Dag 1–30','Møde medarbejderne og gennemgå anlæggets sikkerhed, miljøkrav, prøveplaner, bemanding og aktuelle driftsudfordringer med relevante fagpersoner.'),
('Dag 30–60','Aftale et fælles overblik over opgaver, åbne fejl, frister og ansvar. Gennemgå vedligeholdsplanen og kritiske grænseflader til projekter.'),
('Dag 60–90','Følge op på erfaringer og driftsdata, prioritere en afgrænset forbedring med teamet og aftale kompetenceudvikling og relevant driftslederuddannelse.'),
('Herefter','Følge rensekvalitet, sikkerhed, økonomi og vedligehold løbende og justere indsatser sammen med drift og specialister.')])
m.section('SAMARBEJDE OG ANSVARSFORDELING — FORSLAG')
for a,b in [('Driftsmedarbejderne','Tydelig fordeling af opgaver, faglig sparring og plads til at rejse problemer tidligt.'),('Driftschefen','Løbende overblik over budget, større risici, ressourcer og de beslutninger, der skal træffes.'),('Specialister og myndighedsfunktioner','Fælles opfølgning på prøver, analyser, udledningskrav og rapportering efter gældende procedurer.'),('Projektledere og leverandører','Aftale sikkerhed, arbejdsdeling og overdragelse, så anlæggets drift tænkes med i arbejdet.')]:m.bullet(a,b,after=30,line=245)
m.section('PRAKTISK')
m.para('Bosat i Måløv. Dansk, engelsk og persisk. Kørekort B.',after=80,justify=False)
m.save(str(R/'Shahram_Ajloo_LTF_Moelleaavaerket_AnsogningCV.docx'))
