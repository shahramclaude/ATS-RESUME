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
m.para('Jeg vil sammen med forsyningen aftale et forløb for den relevante driftslederuddannelse på spildevandsområdet. Jeg ser frem til at drøfte, hvordan teamets faglighed og en systematisk opfølgning kan understøtte en sikker og miljømæssigt korrekt drift.',after=60,line=255,justify=False)
m.meta('Med venlig hilsen',after=15);m.meta('Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com',after=0)
m.page_break();m.resume_header(n,t,c,'DRIFTSPROFIL — RENSEANLÆG, MENNESKER OG TEKNIK')
m.para('Elautoriseret maskinmester med erfaring fra kritisk el- og mekanisk drift på BIOFOS’ renseanlæg Lynetten, forebyggende vedligehold og skifteholdsdrift. Hertil kommer personaleledelse af tekniske medarbejdere, projekt- og resultatansvar samt erfaring med dokumentation i reguleret miljø. Det giver et praktisk grundlag for at arbejde med driftssikkerhed, vedligehold og samarbejde på Mølleåværket.',after=65,line=255,justify=False)
m.section('DRIFTSKOMPETENCER — RETTET MOD MØLLEÅVÆRKET')
for a,b in [
('Renseanlæg og vedligehold','Lynetten: pumper, HVAC, højspændingstavler og SCADA, forebyggende vedligehold, akut fejlfinding og reservedelsflow i kritisk drift.'),
('Personaleledelse','ELOHVAC: fem elektrikere og tre lærlinge med planlægning, 1:1, MUS og oplæring. Ventek-Air: daglig ledelse af 14 medarbejdere.'),
('Sikkerhed og kvalitet','LOTO, APV, risikovurdering og nærved-hændelser fra teknisk drift. FAT/SAT og IQ/OQ/PQ med nul kritiske afvigelser ved Novo Nordisk-aflevering.'),
('Data og procesforbedring','SCADA-erfaring fra Lynetten og anvendelse af 5S, PDCA og standardarbejde. Digitale værktøjer i ELOHVAC bidrog til et produktivitetsløft på over 40 %.'),
('Forretning og samarbejde','Fuldt P&L i ELOHVAC; økonomi- og risikostyring på tekniske projekter samt koordinering af specialister, indkøb og underentreprenører.')]:m.bullet(a,b,after=20,line=245)
m.section('ERHVERVSERFARING')
m.job('Ejer / teknisk direktør / elautoriseret maskinmester','ELOHVAC ApS · København · maj 2023–nu')
for a,b in [('Mennesker og planlægning','Personaleansvar for fem elektrikere og tre lærlinge; 1:1, MUS, oplæring, sikkerhed og daglig prioritering.'),('Drift og teknik','El-, ventilations- og klimaanlæg: tavler, styring, installation, fejlfinding og forebyggende vedligehold for erhvervskunder.'),('Økonomi og kvalitet','Fuldt resultatansvar; tilbud, beregning, materialestyring, underentreprenører, kvalitetssikring og dokumentation.'),('Forbedring','Egne AI-værktøjer til tilbud, tidsplaner og kvalitetstjek har bidraget til over 40 % produktivitetsløft.')]:m.bullet(a,b,after=15,line=245)
m.job('Medejer og CTO / teknisk ansvarlig for AI-afdelingen','Data Power Consultant ApS · København · 2024–nov. 2026')
m.bullet('Tekniske løsninger','Ledede 4–10 personer og implementering af tekniske applikationer fra behov til dokumentation og overdragelse. Sideløbende med ELOHVAC; virksomheden er ophørt.',after=15,line=245)
m.page_break();m.section('ERHVERVSERFARING — FORTSAT')
m.job('Senior idriftsættelsesingeniør / projektleder, elsystem','Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024')
for a,b in [('Projekter og ressourcer','Koordinerede 25 specialister på 37 samtidige CAPEX-projekter; fremdrift, økonomi, risiko og ressourcer på tværs af engineering, indkøb og anlæg.'),('Kvalitet og aflevering','FAT/SAT og IQ/OQ/PQ i reguleret miljø med nul kritiske afvigelser ved aflevering; tavler, styring og UPS.')]:m.bullet(a,b,after=18,line=245)
m.job('Projekt- og værkstedsleder','Ventek-Air · København · jan. 2022–nov. 2022')
for a,b in [('Planlægning og mennesker','Ledede 14 medarbejdere og styrede 11 samtidige projekter med kapacitets- og fremdriftsstyring.'),('Sikkerhed og samarbejde','Tilbud, aftalegrundlag, underentreprenører, sikkerhedsdokumentation og aflevering; tavlemøder og flaskehalsanalyser.')]:m.bullet(a,b,after=18,line=245)
m.job('Vedligeholdelses- og driftsleder / værkstedstekniker','BIOFOS, Lynetten · København · aug. 2017–jan. 2022')
for a,b in [('Kritisk drift','El- og mekanisk drift på renseanlæg: pumper, HVAC, højspændingstavler og SCADA; forebyggende vedligehold og akut fejlfinding.'),('Sikkerhed og systematik','Skifteholdsdrift med LOTO, APV, risikovurdering og nærved-hændelser; reservedelsflow, 5S, standardarbejde og PDCA.')]:m.bullet(a,b,after=18,line=245)
m.job('Elektromekaniker / produktionsteamleder','ARJ Engineering · Teheran · dec. 2003–mar. 2010')
m.bullet('Drift og medarbejdere','Ledelse af 12 mekanikere og teknikere; vagtplanlægning, materialestyring, fejldiagnose og reparation af industrielle el- og mekaniske anlæg.',after=18,line=245)
m.section('UDDANNELSE, METODER OG SPROG')
for a,b in [('B.Tech, Technology Management and Mechanical Engineering','Copenhagen School of Marine Engineering & Technology Management · 2017–2022'),('Elautoriseret maskinmester, LV/MV/HV','Sikkerhedsstyrelsen · 2023'),('PRINCE2 certificeret projektleder','AXELOS / PeopleCert'),('Køleteknik og klimaanlæg','Mercantec AMU · 2021'),('El- og maskinteknisk design, elteknik','Tehran Technical University · 2000–2003')]:m.edu(a,b)
m.para('**Metoder:** Lean, Six Sigma og PRINCE2 anvendt i praksis; kun PRINCE2 er certificeret. **Systemer:** SCADA, Excel, SAP ERP og digitale planlægningsværktøjer. **Sprog:** dansk, engelsk og persisk. **Kørekort:** B.',after=20,line=245,justify=False)
m.section('FØRSTE PRIORITERINGER — FORSLAG')
for a,b in [('Drift og krav','Gennemgå sikkerhed, miljøgodkendelser, driftsdata, prøveplaner og åbne opgaver med teamet.'),('Ressourcer og vedligehold','Afstem bemanding, kritiske anlægsdele og planlagte arbejder med driftschef, medarbejdere og specialister.'),('Forbedring','Vælg en afgrænset indsats sammen med teamet, aftal ansvar og følg effekt på drift og rensekvalitet.')]:m.bullet(a,b,after=15,line=245)
m.save(str(R/'Shahram_Ajloo_LTF_Moelleaavaerket_Masterstil.docx'))
