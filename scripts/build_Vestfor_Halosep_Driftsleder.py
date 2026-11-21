"""Vestforbrænding HaloSep: ansøgning og CV i brugerens master-/RegionH-stil."""
from pathlib import Path
from master_design import MasterDoc
R=Path(__file__).resolve().parent.parent
m=MasterDoc(str(R/'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='da-DK')
n='SHAHRAM AJLOO';t='Driftsleder | HaloSep · Vestforbrænding'
c='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
m.header_banner(n,t,c);m.meta('Vestforbrænding · Att.: produktionschef Ahmad Gabokji',after=30)
m.para('**Ansøgning: Driftsleder til HaloSep**',after=70,justify=False)
m.para('Kære Ahmad Gabokji',after=65,justify=False)
m.para('På HaloSep skal sikker drift og ressourceudnyttelse fungere sammen. Når flyveaske behandles, så metaller kan udskilles, stiller det krav til både anlæggets stabilitet, de daglige rutiner og medarbejdernes sikkerhed. Driftslederens opgave er at skabe overblik, støtte holdet og få problemer løst, før de udvikler sig til større driftsforstyrrelser.',after=70,line=245,justify=False)
m.para('Jeg vil tage ansvar for driften gennem en tæt dialog med de fem driftsassistenter og seks operatører. Erfaringen fra kritisk teknisk drift på BIOFOS/Lynetten, personaleledelse i ELOHVAC og projekt- og værkstedsledelse hos Ventek-Air giver et praktisk grundlag for følgende prioriteringer:',after=60,line=245,justify=False)
for a,b in [
('Et hold med klar retning','Sammen med medarbejderne vil jeg gennemgå bemanding, opgaver, aktuelle fejl og overlevering. Individuelle samtaler, feedback og faglig sparring skal gøre forventningerne tydelige og give plads til udvikling. Jeg har ansvar for fem elektrikere og tre lærlinge og har tidligere ledet et team på 14 medarbejdere.'),
('Sikkerhed og kvalitet i driften','Før arbejde udføres, skal risici, instruktioner, nødvendige værnemidler og sikker afstilling være afklaret. Flyveaske og procesmedier skal håndteres af oplærte medarbejdere efter anlæggets gældende procedurer. Afvigelser og nærved-hændelser skal følges op sammen med holdet og de relevante sikkerhedsfunktioner.'),
('Vedligehold og stabilitet','Operatørvedligehold skal planlægges sammen med operatørerne og koordineres med vedligeholdelsesfunktionen. Åbne fejl, gentagne stop og udestående opgaver skal have en ansvarlig og en aftalt opfølgning. På Lynetten arbejdede jeg med pumper, SCADA, forebyggende vedligehold og akut fejlfinding i døgnbemandet drift.'),
('Resultater og forbedringer','Jeg vil følge anlæggets aftalte KPI’er for sikkerhed, kvalitet og drift og undersøge afvigelser sammen med medarbejderne. Lean og 5S kan understøtte tydelige arbejdspladser og standarder; jeg vil bruge Vestforbrændings 4C-arbejdsform efter de lokale instruktioner til at behandle problemer og følge effekten af forbedringer.'),
('Samarbejde på tværs','Driftens behov skal være tydelige for kolleger i vedligehold, specialister og produktionsledelsen. Før indgreb aftales ansvar, adgang, sikkerhed og tilbagelevering, så løsningen fungerer for både medarbejderne og anlægget.')]:m.bullet(a,b,after=30,line=240)
m.para('Vestforbrænding lægger vægt på tillid, respekt og tydelige roller. Det er et godt grundlag for at lede tæt på anlægget og tage medarbejdernes viden med i beslutningerne. Jeg medvirker naturligvis til den krævede sikkerhedsgodkendelse og ser frem til at drøfte, hvordan jeg kan bidrage til sikker og stabil drift af HaloSep.',after=45,line=245,justify=False)
m.meta('Med venlig hilsen · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com',after=0)
m.page_break();m.resume_header(n,t,c,'DRIFTSLEDELSE — MENNESKER, SIKKERHED OG TEKNIK')
m.para('Elautoriseret maskinmester med erfaring fra teknisk drift og vedligehold på BIOFOS’ renseanlæg Lynetten samt ledelse af tekniske medarbejdere og projekter. Har arbejdet med sikkerhed, planlægning, fejlretning og løbende forbedringer i døgnbemandet drift og reguleret industri.',after=60,line=245,justify=False)
m.section('ERFARING RELEVANT FOR HALOSEP')
for a,b in [
('Personaleledelse','Daglig planlægning, 1:1, MUS og oplæring af fem elektrikere og tre lærlinge i ELOHVAC. Tidligere daglig ledelse af 14 medarbejdere hos Ventek-Air.'),
('Drift og vedligehold','På Lynetten arbejdede jeg med pumper, HVAC, højspændingstavler og SCADA, forebyggende vedligehold og akut fejlfinding. Erfaringen giver et teknisk grundlag for samarbejdet om et procesanlæg.'),
('Sikkerhed og kvalitet','LOTO, risikovurdering, APV og opfølgning på nærved-hændelser. Hos Novo Nordisk indgik test og dokumentation i aflevering uden kritiske afvigelser.'),
('Løbende forbedringer','Lean, 5S, standardarbejde og PDCA anvendt i praksis. Digitale værktøjer til planlægning og kvalitetstjek bidrog til over 40 % produktivitetsløft i ELOHVAC.'),
('Planlægning og samarbejde','Styring af 11 samtidige projekter hos Ventek-Air og koordinering af 25 specialister på 37 projekter hos Novo Nordisk, herunder ressourcer, risici og fremdrift.')]:m.bullet(a,b,after=20,line=240)
m.models_table('DAGLIG DRIFT — FORSLAG TIL OPFØLGNING',('Område','Praktisk tilgang'),[
('Hold og bemanding','Afstem opgaver, kompetencer, bemanding og overlevering; følg op med medarbejderne.'),
('Sikkerhed og kvalitet','Gennemgå risici, instruktioner og afvigelser; anvend anlæggets procedurer og relevante sikkerhedsfunktioner.'),
('Operatørvedligehold','Aftal ansvar og intervaller med operatører og vedligehold; følg op på fejl og udestående opgaver.'),
('KPI og forbedring','Gennemgå aftalte drifts- og kvalitetsmål, undersøg afvigelser og følg op på forbedringer med Lean, 4C og 5S efter lokale standarder.'),
('Samarbejde','Afklar arbejdsdeling og overdragelse med teknikere, specialister og produktionsledelse.')])
m.section('UDVALGTE RESULTATER')
for a,b in [('Kvalitet','37 samtidige projekter med 25 specialister hos Novo Nordisk; nul kritiske afvigelser ved aflevering.'),('Produktivitet','Over 40 % produktivitetsløft i ELOHVAC understøttet af digitale værktøjer.'),('Ledelse og planlægning','14 medarbejdere og 11 samtidige anlægsprojekter hos Ventek-Air.')]:m.bullet(a,b,after=15,line=235)
m.page_break();m.section('ERHVERVSERFARING')
m.job('Ejer / teknisk direktør / elautoriseret maskinmester','ELOHVAC ApS · København · maj 2023–nu')
for a,b in [('Medarbejdere og planlægning','Leder fem elektrikere og tre lærlinge med ansvar for daglig planlægning, medarbejdersamtaler, oplæring og arbejdsmiljø.'),('Teknik og kvalitet','Installation, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg. Tilbud, materialer, underentreprenører og kvalitetssikring med fuldt resultatansvar.'),('Forbedring','Egne AI-værktøjer til tilbud, tidsplaner og kvalitetstjek har bidraget til over 40 % produktivitetsløft.')]:m.bullet(a,b,after=15,line=240)
m.job('Medejer og CTO / teknisk ansvarlig for AI-afdelingen','Data Power Consultant ApS · København · 2024–nov. 2026')
m.bullet('Ledelse og løsninger','Ledede 4–10 personer og arbejdede med tekniske applikationer fra behovsafklaring til dokumentation og overdragelse. Sideløbende med ELOHVAC; virksomheden er ophørt.',after=15,line=240)
m.job('Senior idriftsættelsesingeniør / projektleder, elsystem','Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024')
for a,b in [('Projektstyring','Koordinerede 25 specialister på 37 samtidige anlægsprojekter med opfølgning på ressourcer, økonomi, risiko og fremdrift.'),('Kvalitet og aflevering','FAT/SAT og IQ/OQ/PQ i reguleret miljø med nul kritiske afvigelser ved aflevering. Arbejdede med tavler, styring og UPS.')]:m.bullet(a,b,after=15,line=240)
m.job('Projekt- og værkstedsleder','Ventek-Air · København · jan. 2022–nov. 2022')
m.bullet('Daglig ledelse','Ledede 14 medarbejdere og styrede 11 samtidige projekter; planlægning, underentreprenører, sikkerhedsdokumentation og aflevering.',after=15,line=240)
m.job('Vedligeholdelses- og driftsleder / værkstedstekniker','BIOFOS, Lynetten · København · aug. 2017–jan. 2022')
for a,b in [('Teknisk drift','Arbejdede med pumper, HVAC, højspændingstavler og SCADA; forebyggende vedligehold og akut fejlfinding på renseanlæg.'),('Sikkerhed og forbedringer','Skifteholdsdrift med LOTO, risikovurdering og APV; reservedelsflow, 5S og PDCA på værksted og lager.')]:m.bullet(a,b,after=15,line=240)
m.job('Elektromekaniker / produktionsteamleder','ARJ Engineering · Teheran · dec. 2003–mar. 2010')
m.bullet('Produktion og drift','Ledede 12 mekanikere og teknikere med ansvar for vagtplanlægning, materialestyring og fejldiagnose på industrielle anlæg.',after=15,line=240)
m.section('UDDANNELSE, METODER OG SPROG')
for a,b in [('B.Tech, Technology Management and Mechanical Engineering','Copenhagen School of Marine Engineering & Technology Management · 2017–2022'),('Elautoriseret maskinmester, LV/MV/HV','Sikkerhedsstyrelsen · 2023'),('PRINCE2 certificeret projektleder','AXELOS / PeopleCert'),('Køleteknik og klimaanlæg','Mercantec AMU · 2021'),('El- og maskinteknisk design, elteknik','Tehran Technical University · 2000–2003')]:m.edu(a,b)
m.para('**Metoder:** Lean, Six Sigma og PRINCE2 anvendt i praksis; certificeret i PRINCE2. **Systemer:** SCADA, Excel, SAP ERP og digitale planlægningsværktøjer. **Sprog:** dansk, engelsk og persisk. **Kørekort:** B.',after=20,line=235,justify=False)
m.page_break();m.models_table('FØRSTE 90 DAGE — FORSLAG',('Periode','Prioritet sammen med hold og produktionsledelse'),[
('Dag 1–30','Lære medarbejderne og anlæggets processer, sikkerhedsinstruktioner, bemanding, KPI’er og aktuelle driftsudfordringer at kende. Følge oplæring og gældende adgangs- og sikkerhedskrav.'),
('Dag 30–60','Gennemgå overlevering, vedligeholdsopgaver og tilbagevendende afvigelser sammen med operatører og vedligehold. Afklare ansvar og opfølgningsform.'),
('Dag 60–90','Vælge en afgrænset forbedring med holdet, anvende den lokale 4C-tilgang og følge op på effekt, sikkerhed og kvalitet. Aftale individuelle udviklingsbehov.'),
('Løbende','Holde fokus på sikkerhed, medarbejderdialog, kvalitet og stabil drift; justere planen med produktionsledelsen.')])
m.section('SAMARBEJDE OM HALOSEP')
for a,b in [('Driftsassistenter og operatører','Tydelige aftaler om opgaver, instruktioner, feedback og overlevering.'),('Vedligehold og specialister','Afklare fejl, arbejdsdeling, sikker afstilling og tilbagelevering før indgreb.'),('Produktionsledelsen','Følge op på bemanding, sikkerhed, resultater og prioritering af forbedringer.')]:m.bullet(a,b,after=25,line=240)
m.save(str(R/'Shahram_Ajloo_Vestfor_Halosep_Driftsleder.docx'))
