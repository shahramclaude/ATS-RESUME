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
m.para('Mølleåværkets opgave er at rense spildevandet sikkert og stabilt, også når anlægget vedligeholdes og udvikles. Forsyningen har beskrevet forbedringer af sandfang og membrananlæg og udnyttelse af slam til biogas. Driftsledelse handler om at skabe sammenhæng mellem mennesker, rensekvalitet, sikkerhed og økonomi, så udvikling kan ske uden at slippe den daglige drift.',after=85,line=260,justify=False)
m.para('**Sådan vil jeg samle driften om opgaven**',after=45,justify=False)
for a,b in [
('Daglig drift og fælles prioritering','Sammen med de seks driftsmedarbejdere vil jeg skabe overblik over anlæggets tilstand, opgaver, bemanding og overlevering. Kritiske fejl og ændringer i renseprocessen skal have en tydelig ansvarlig og opfølgning, mens forebyggende vedligehold planlægges, så det ikke forsvinder i dagens akutte opgaver.'),
('Ledelse og arbejdsmiljø','Klare forventninger, løbende dialog og plads til medarbejdernes faglighed skal gøre det muligt at handle tidligt. Opgaver og kompetencebehov gennemgås med teamet; sikkerhedsrisici og nærved-hændelser følges op sammen med arbejdsmiljøorganisationen. Ved indgreb skal relevant risikovurdering og sikker afstilling være på plads før arbejdet starter.'),
('Miljøkrav, prøver og rapportering','Miljøgodkendelser og udledningskrav omsættes til et overblik over målepunkter, prøvetagning, frister og ansvar. Sammen med de relevante fagpersoner skal analyser, afvigelser og korrigerende handlinger dokumenteres, med rettidig rapportering til myndigheder efter gældende krav og anlæggets procedurer.'),
('Driftsdata, proces og vedligehold','SRO/SCADA-oplysninger, driftsdata, prøveresultater og medarbejdernes observationer skal sammen vise, hvor udviklingen afviger. Vedligehold prioriteres efter konsekvens for sikkerhed, rensekvalitet og oppetid. Optimering af proces og styring vurderes med anlæggets specialister og følges op på faktisk effekt.'),
('Projekter og økonomi','Ved reparationer og ombygninger aftales grænseflader, tidsplan, sikkerhed og overdragelse med projektledere, specialister og leverandører. Budget, forbrug og forventede større arbejder følges med driftschefen; energioptimering og investeringer vurderes mod rensekrav, risiko og anlæggets levetid.')]:m.bullet(a,b,after=55,line=255)
m.para('På Lynetten har jeg arbejdet med drift og vedligehold af blandt andet pumper, højspændingstavler og SCADA i et døgnbemandet renseanlæg. Fra ELOHVAC bringer jeg personaleledelse og resultatansvar, og fra Novo Nordisk erfaring med koordinering og dokumenteret aflevering i et reguleret miljø. Den kombination vil jeg bruge til at understøtte medarbejdernes arbejde og samarbejdet om en stabil drift.',after=65,line=255,justify=False)
m.para('Jeg vil sammen med forsyningen aftale et forløb for den relevante driftslederuddannelse på spildevandsområdet. Jeg ser frem til at drøfte, hvordan teamets faglighed og en systematisk opfølgning kan understøtte en sikker og miljømæssigt korrekt drift.',after=60,line=255,justify=False)
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
('Dagligt overblik','Fælles gennemgang af opgaver, alarmer, bemanding, åbne fejl og næste beslutning.'),
('Miljø og dokumentation','Overblik over udledningskrav, prøver, analyser, frister og ansvar sammen med relevante fagpersoner.'),
('Vedligehold','Prioritering efter risiko for arbejdsmiljø, rensekvalitet og oppetid; plan for kritiske anlægsdele.'),
('Driftsdata','SCADA-data, prøveresultater og observationer bruges til at finde afvigelser og følge forbedringer.'),
('Økonomi og projekter','Budgetopfølgning og koordination af arbejdstid, sikkerhed og overdragelse med drift og projekter.')])
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
m.save(str(R/'Shahram_Ajloo_LTF_Moelleaavaerket_Professionel.docx'))
