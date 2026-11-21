"""Mølleåværket — fornyet ansøgning og CV i brugerens RegionH-format."""
from pathlib import Path
from master_design import MasterDoc
R=Path(__file__).resolve().parent.parent
m=MasterDoc(str(R/'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='da-DK')
n='SHAHRAM AJLOO';t='Driftsleder | Mølleåværket · Lyngby-Taarbæk Forsyning'
c='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
m.header_banner(n,t,c);m.meta('Lyngby-Taarbæk Forsyning · Att.: driftschef Jannik Lund Olsen',after=35)
m.para('**Ansøgning: Driftsleder til Mølleåværket**',after=75,justify=False)
m.para('Kære Jannik Lund Olsen',after=70,justify=False)
m.para('På et renseanlæg skal driften fungere hver dag — også når udstyr svigter, vedligehold skal gennemføres, eller anlægget bygges om. På Mølleåværket er opgaven samtidig at rense spildevand og overholde udledningskravene og udvikle et anlæg, hvor blandt andet energi og slam er vigtige ressourcer. Det kræver både overblik over teknikken og en tæt dialog med de medarbejdere, der kender anlægget.',after=70,line=250,justify=False)
m.para('Jeg søger stillingen, fordi den samler de opgaver, jeg har arbejdet med på Lynetten og i teknisk ledelse: sikker drift, vedligehold, mennesker og samarbejde på tværs. Som driftsleder vil jeg især prioritere følgende:',after=65,line=245,justify=False)
for a,b in [
('Et team med klare aftaler','Sammen med de seks medarbejdere vil jeg gennemgå opgaver, bemanding, alarmer og udeståender, så det er tydeligt, hvad der haster, og hvem der følger op. Individuelle samtaler og løbende sparring skal give plads til faglig udvikling og trivsel. Jeg har personaleansvar for fem elektrikere og tre lærlinge og har tidligere ledet 14 medarbejdere hos Ventek-Air.'),
('Sikker drift og planlagt vedligehold','Sammen med teamet vil jeg vurdere kritiske anlægsdele, kendte fejl og de planlagte vedligeholdsaktiviteter. Opgaverne prioriteres efter konsekvens for arbejdsmiljø, rensekvalitet og oppetid. På Lynetten arbejdede jeg med pumper, højspændingstavler, SCADA og forebyggende vedligehold i døgnbemandet drift.'),
('Miljøkrav og opfølgning','Miljøgodkendelser og udledningskrav skal omsættes til en fælles oversigt over prøvetagning, analyser, dokumentation, ansvar og frister. Jeg vil sammen med anlæggets fagpersoner sikre opfølgning på afvigelser og rettidig rapportering til myndigheder efter gældende procedurer.'),
('Procesforbedring og projekter','Driftsdata fra SRO/SCADA, prøveresultater og medarbejdernes observationer skal danne grundlag for optimering. Før ændringer i proces eller automation gennemføres, vil jeg afstemme effekt og risici med specialisterne. Ved reparationer og ombygninger aftales arbejdsplan, sikker afstilling og overdragelse med projektledere, leverandører og arbejdsmiljøorganisationen.'),
('Økonomi og anlæggets levetid','Driftsbudgettet skal følges op mod forbrug og forventede vedligeholdsbehov. Sammen med driftschefen vil jeg prioritere større arbejder og bidrage til budgetlægningen, så økonomi, energiforbrug og risiko for driftsstop vurderes samlet. Fra ELOHVAC har jeg fuldt resultatansvar; hos Novo Nordisk fulgte jeg økonomi og ressourcer på tekniske projekter.')]:m.bullet(a,b,after=30,line=240)
m.para('Jeg vil aftale et forløb for den relevante driftslederuddannelse på spildevandsområdet med forsyningen. Jeg ser frem til at drøfte, hvordan teamets erfaring og en tydelig plan for drift og vedligehold kan understøtte Mølleåværkets opgave.',after=45,line=245,justify=False)
m.meta('Med venlig hilsen · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com',after=0)
m.page_break();m.resume_header(n,t,c,'DRIFTSLEDELSE — RENSEANLÆG OG TEKNISKE ANLÆG')
m.para('Elautoriseret maskinmester med erfaring fra el- og mekanisk drift på BIOFOS’ renseanlæg Lynetten. Har arbejdet med forebyggende vedligehold, akut fejlfinding og sikkerhed i døgnbemandet drift samt med personaleledelse, projektøkonomi og dokumentation i tekniske virksomheder og reguleret industri.',after=70,line=245,justify=False)
m.section('ERFARING RELEVANT FOR MØLLEÅVÆRKET')
for a,b in [
('Renseanlæg og vedligehold','BIOFOS/Lynetten: pumper, ventilation, højspændingstavler og SCADA. Forebyggende vedligehold, akut fejlfinding og reservedelsflow på et anlæg i døgnbemandet drift.'),
('Ledelse og kompetenceudvikling','ELOHVAC: daglig planlægning, 1:1, MUS og oplæring af fem elektrikere og tre lærlinge. Ventek-Air: daglig ledelse af et team på 14 medarbejdere.'),
('Arbejdsmiljø og kvalitet','Risikovurdering, APV og sikker afstilling i teknisk drift. Test og dokumentation i reguleret miljø hos Novo Nordisk; nul kritiske afvigelser ved aflevering.'),
('Driftsdata og forbedringer','SCADA-erfaring fra Lynetten samt anvendelse af 5S, standardarbejde og PDCA. Digitale værktøjer til planlægning og kvalitetstjek bidrog til over 40 % produktivitetsløft i ELOHVAC.'),
('Økonomi og samarbejde','Fuldt resultatansvar i ELOHVAC. Koordinerede 25 specialister på 37 samtidige anlægsprojekter hos Novo Nordisk med opfølgning på økonomi, ressourcer og risici.')]:m.bullet(a,b,after=25,line=240)
m.models_table('STYRING AF DRIFTEN — FORSLAG TIL PRAKSIS',('Område','Hvad der skal følges op på'),[
('Daglig drift','Opgaver, bemanding, alarmer, akutte fejl og overlevering mellem medarbejdere.'),
('Miljø og kvalitet','Gældende udledningskrav, prøvetagning, analyser, afvigelser og rapporteringsfrister med relevante fagpersoner.'),
('Vedligehold','Anlæggenes tilstand, sikkerhed, reservedelsbehov og prioritering af planlagte arbejder.'),
('Proces og økonomi','Driftsdata og prøveresultater; forbrug, budget og konsekvenser ved større forbedringer.'),
('Projekter','Arbejdsplan, risikovurdering, grænseflader og sikker overdragelse mellem drift, leverandører og projektledelse.')])
m.section('UDVALGTE RESULTATER')
for a,b in [('Projektleverancer','37 samtidige projekter og 25 specialister hos Novo Nordisk; nul kritiske afvigelser ved aflevering.'),('Forbedring','Over 40 % produktivitetsløft i ELOHVAC understøttet af digitale planlægnings- og kvalitetstjekværktøjer.'),('Kapacitet','11 samtidige anlægsprojekter og et team på 14 hos Ventek-Air.')]:m.bullet(a,b,after=20,line=235)
m.page_break();m.section('ERHVERVSERFARING')
m.job('Ejer / teknisk direktør / elautoriseret maskinmester','ELOHVAC ApS · København · maj 2023–nu')
for a,b in [('Personale og drift','Leder fem elektrikere og tre lærlinge med ansvar for planlægning, medarbejdersamtaler, oplæring og arbejdsmiljø.'),('Teknik og økonomi','Arbejder med el-, ventilations- og klimaanlæg, herunder vedligehold og fejlfinding. Har fuldt resultatansvar for tilbud, materialer, underentreprenører og kvalitet.'),('Digitalisering','Udvikler AI-værktøjer til tilbud, tidsplaner og kvalitetstjek; værktøjerne har bidraget til et produktivitetsløft på over 40 %.')]:m.bullet(a,b,after=16,line=240)
m.job('Medejer og CTO / teknisk ansvarlig for AI-afdelingen','Data Power Consultant ApS · København · 2024–nov. 2026')
m.bullet('Ledelse og løsninger','Ledede en afdeling med 4–10 personer og arbejdede med tekniske applikationer fra behov til dokumentation og overdragelse. Stillingen var sideløbende med ELOHVAC; virksomheden er ophørt.',after=16,line=240)
m.job('Senior idriftsættelsesingeniør / projektleder, elsystem','Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024')
for a,b in [('Projektstyring','Koordinerede 25 specialister på 37 samtidige anlægsprojekter med opfølgning på økonomi, fremdrift, ressourcer og risici.'),('Kvalitet og aflevering','FAT/SAT og IQ/OQ/PQ i reguleret miljø med nul kritiske afvigelser ved aflevering. Arbejdede med tavler, styring og UPS.')]:m.bullet(a,b,after=16,line=240)
m.job('Projekt- og værkstedsleder','Ventek-Air · København · jan. 2022–nov. 2022')
m.bullet('Ledelse og gennemførelse','Ledede 14 medarbejdere og styrede 11 samtidige projekter. Arbejdet omfattede planlægning, underentreprenører, sikkerhedsdokumentation og aflevering.',after=16,line=240)
m.job('Vedligeholdelses- og driftsleder / værkstedstekniker','BIOFOS, Lynetten · København · aug. 2017–jan. 2022')
for a,b in [('Teknisk drift','Arbejdede med pumper, HVAC, højspændingstavler og SCADA; forebyggende vedligehold og akut fejlfinding på renseanlæg.'),('Sikkerhed og forbedringer','Skifteholdsdrift med LOTO, risikovurdering og APV. Arbejdede med reservedelsflow, 5S og PDCA på værksted og lager.')]:m.bullet(a,b,after=16,line=240)
m.job('Elektromekaniker / produktionsteamleder','ARJ Engineering · Teheran · dec. 2003–mar. 2010')
m.bullet('Produktion og vedligehold','Ledede 12 mekanikere og teknikere; vagtplanlægning, materialestyring, fejldiagnose og reparation af industrielle el- og mekaniske anlæg.',after=16,line=240)
m.section('UDDANNELSE, METODER OG SPROG')
for a,b in [('B.Tech, Technology Management and Mechanical Engineering','Copenhagen School of Marine Engineering & Technology Management · 2017–2022'),('Elautoriseret maskinmester, LV/MV/HV','Sikkerhedsstyrelsen · 2023'),('PRINCE2 certificeret projektleder','AXELOS / PeopleCert'),('Køleteknik og klimaanlæg','Mercantec AMU · 2021'),('El- og maskinteknisk design, elteknik','Tehran Technical University · 2000–2003')]:m.edu(a,b)
m.para('**Metoder:** Lean, Six Sigma og PRINCE2 anvendt i praksis; certificeret i PRINCE2. **Systemer:** SCADA, Excel, SAP ERP og digitale planlægningsværktøjer. **Sprog:** dansk, engelsk og persisk. **Kørekort:** B.',after=20,line=235,justify=False)
m.page_break();m.models_table('FØRSTE 90 DAGE — FORSLAG TIL PRIORITERING',('Periode','Fokus i samarbejde med teamet og driftschefen'),[
('Dag 1–30','Lære medarbejderne og anlægget at kende. Gennemgå gældende miljøkrav, sikkerhedsforhold, prøveplaner, åbne fejl, bemanding og budget med de ansvarlige.'),
('Dag 30–60','Afstemme vedligeholdsplan, kritiske anlægsdele og kommende projekter. Aftale en praktisk opfølgning på fejl, prøvefrister og økonomi.'),
('Dag 60–90','Vælge en afgrænset forbedring med team og specialister. Aftale ansvar og målepunkt, følge effekten på drift og rensekvalitet og planlægge relevant kompetenceudvikling.'),
('Løbende','Følge trivsel, sikkerhed, rensekvalitet og økonomi; justere prioriteringerne, når anlæggets behov ændrer sig.')])
m.section('SAMARBEJDE OM DRIFTEN')
for a,b in [('Medarbejderne','Fælles prioritering, faglig sparring og individuelle samtaler om udvikling og trivsel.'),('Driftschefen','Opfølgning på budget, risici, bemanding og beslutninger om større arbejder.'),('Fagpersoner og myndighedsfunktioner','Sikre klar ansvarsfordeling for analyser, dokumentation, miljøkrav og indberetning.'),('Projekter og leverandører','Planlægge adgang, sikkerhed, vedligehold og overdragelse, så den daglige drift kan fortsætte forsvarligt.')]:m.bullet(a,b,after=25,line=240)
m.save(str(R/'Shahram_Ajloo_LTF_Moelleaavaerket_DriftLedelse.docx'))
