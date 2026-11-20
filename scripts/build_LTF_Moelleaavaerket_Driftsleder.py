"""Lyngby-Taarbæk Forsyning — driftsleder, Mølleåværket."""
from pathlib import Path
from master_design import MasterDoc
R=Path(__file__).resolve().parent.parent
m=MasterDoc(str(R/'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='da-DK')
n='SHAHRAM AJLOO';t='Driftsleder — Mølleåværket | Lyngby-Taarbæk Forsyning'
c='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
m.header_banner(n,t,c);m.meta('Lyngby-Taarbæk Forsyning · Att.: Jannik Lund Olsen',after=25)
m.para('**Ansøgning: Driftsleder til Mølleåværket**',after=80,justify=False)
m.para('Kære Jannik Lund Olsen',after=80,justify=False)
m.para('Mølleåværket skal rense spildevandet sikkert hver dag, samtidig med at anlægget vedligeholdes og udvikles. Forsyningen beskriver blandt andet renovering af sandfang og membrananlæg og udnyttelse af slam til biogas. Det understreger behovet for at holde styr på både renseprocessen, arbejdsmiljøet og samspillet mellem drift og projekter.',after=85,line=260,justify=False)
m.para('**Et driftsfællesskab med overblik over anlægget**',after=45,justify=False)
for a,b in [
('Sikker drift og tydelige prioriteringer','Sammen med de seks driftsmedarbejdere vil jeg skabe en fast rytme for opgaver, bemanding og overlevering. Åbne fejl, planlagt vedligehold og risiko for påvirkning af renseprocessen skal være synlige, så akutte opgaver ikke fortrænger de nødvendige forebyggende indsatser.'),
('Mennesker og arbejdsmiljø','Tydelige forventninger skal følges af nærværende sparring og plads til medarbejdernes faglige vurderinger. Ved større reparationer og ombygninger vil jeg afstemme adgang, sikkerhed og arbejdsfordeling med arbejdsmiljøorganisationen, specialister, projektledere og leverandører før arbejdet igangsættes.'),
('Udledningskrav og dokumentation','Miljøgodkendelser og udledningskrav skal omsættes til et praktisk overblik over målinger, prøvetagning, ansvar og frister. Sammen med de relevante fagpersoner vil jeg sikre, at analyser og afvigelser bliver dokumenteret, fulgt op med rapportering til myndigheder efter anlæggets gældende procedurer.'),
('Proces og vedligehold','Optimering skal tage udgangspunkt i driftsdata, alarmer, prøveresultater og medarbejdernes observationer for at opdage ændringer tidligt. Jeg vil prioritere vedligehold efter konsekvens for sikkerhed, rensekvalitet og oppetid og lade ændringer i proces eller styring blive vurderet og afprøvet med anlæggets specialister.'),
('Økonomi og udvikling','Budget og forbrug skal følges sammen med driftschefen, så større reparationer og forbedringer prioriteres på et oplyst grundlag. Indsatser for lavere energiforbrug eller længere levetid skal vurderes mod anlæggets udledningskrav og den daglige drift, før de gennemføres.')]:m.bullet(a,b,after=55,line=255)
m.para('Jeg vil sammen med forsyningen aftale et forløb for den relevante driftslederuddannelse på spildevandsområdet. Jeg ser frem til at drøfte, hvordan teamets erfaring og en systematisk opfølgning kan sikre Mølleåværkets rensekvalitet og udvikling — også når drift og projekter skal fungere samtidig.',after=65,line=260,justify=False)
m.meta('Med venlig hilsen',after=15);m.meta('Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com',after=0)
m.page_break();m.resume_header(n,t,c,'DRIFTSLEDELSE — RENSEANLÆG, TEKNIK OG MENNESKER')
m.para('Elautoriseret maskinmester med erfaring fra BIOFOS, Lynetten, hvor kritisk el- og mekanisk drift, vedligehold og sikkerhed i skifteholdsdrift var centrale opgaver. Baggrunden kombinerer teknisk drift på renseanlæg med personaleledelse, projektøkonomi og tværfaglig koordinering. Den er relevant for Mølleåværkets daglige drift og udvikling.',after=65,line=255,justify=False)
m.section('KOMPETENCER TIL MØLLEÅVÆRKET')
for a,b in [
('Renseanlæg og kritisk drift','BIOFOS/Lynetten: pumper, HVAC, højspændingstavler og SCADA; forebyggende vedligehold og akut fejlfinding i 24/7-drift.'),
('Personaleledelse','Daglig ledelse, planlægning, 1:1, MUS og oplæring af fem elektrikere og tre lærlinge i ELOHVAC; 14 medarbejdere hos Ventek-Air.'),
('Sikkerhed og kvalitet','LOTO, APV og risikovurdering; dokumentation og aflevering. Novo Nordisk: FAT/SAT og IQ/OQ/PQ med nul kritiske afvigelser ved aflevering.'),
('Data og forbedring','SCADA-erfaring fra Lynetten; PDCA, 5S og standardarbejde i drift. ELOHVACs digitale værktøjer til tilbud, tidsplaner og kvalitetstjek bidrog til over 40 % produktivitetsløft.'),
('Økonomi og samarbejde','Fuldt P&L i ELOHVAC; koordinering af underentreprenører og tværfaglige projekter med engineering, indkøb og anlæg.')]:m.bullet(a,b,after=25,line=245)
m.section('ERHVERVSERFARING')
m.job('Ejer / teknisk direktør / elautoriseret maskinmester','ELOHVAC ApS · København · maj 2023–nu')
for a,b in [('Ledelse og planlægning','Ansvar for fem elektrikere og tre lærlinge; 1:1, MUS, oplæring, arbejdsmiljø og prioritering af opgaver.'),('Teknisk drift','El-, ventilations- og klimaanlæg: installation, tavler, styring, forebyggende vedligehold og fejlfinding.'),('Økonomi og kvalitet','Fuldt resultatansvar, tilbud, materialer, underentreprenører, kvalitetssikring og dokumentation.')]:m.bullet(a,b,after=18,line=245)
m.job('Medejer og CTO / teknisk ansvarlig for AI-afdelingen','Data Power Consultant ApS · København · 2024–nov. 2026')
m.bullet('Tekniske løsninger','Ansvarlig for 4–10 personer og implementering af tekniske applikationer fra behov til dokumentation og overdragelse. Sideløbende med ELOHVAC; virksomheden er ophørt.',after=20,line=245)
m.page_break();m.section('ERHVERVSERFARING — FORTSAT')
m.job('Senior idriftsættelsesingeniør / projektleder, elsystem','Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024')
for a,b in [('Samarbejde og styring','Koordinerede 25 specialister på 37 samtidige CAPEX-projekter; fremdrift, økonomi, ressourcer og risici på tværs af engineering, indkøb og anlæg.'),('Aflevering','FAT/SAT og IQ/OQ/PQ i reguleret miljø; nul kritiske afvigelser ved aflevering. Arbejde med tavler, styring og UPS.')]:m.bullet(a,b,after=20,line=245)
m.job('Projekt- og værkstedsleder','Ventek-Air · København · jan. 2022–nov. 2022')
m.bullet('Ledelse og projekter','Ledede et team på 14 og styrede 11 samtidige anlægsprojekter; aftalegrundlag, underentreprenører, sikkerhedsdokumentation og aflevering. Tavlemøder og flaskehalsanalyse.',after=20,line=245)
m.job('Vedligeholdelses- og driftsleder / værkstedstekniker','BIOFOS, Lynetten · København · aug. 2017–jan. 2022')
for a,b in [('Renseanlæg og vedligehold','Kritisk el- og mekanisk drift på renseanlæg: pumper, HVAC, højspændingstavler og SCADA; forebyggende vedligehold og akut fejlfinding.'),('Sikkerhed og forbedringer','LOTO, APV og risikovurdering i skifteholdsdrift; reservedelsflow, 5S og PDCA på værksted og lager.')]:m.bullet(a,b,after=20,line=245)
m.job('Elektromekaniker / produktionsteamleder','ARJ Engineering · Teheran · dec. 2003–mar. 2010')
m.bullet('Drift og medarbejdere','Ledede 12 mekanikere og teknikere; vagtplanlægning, materialestyring, fejldiagnose og reparation af industrielle el- og mekaniske anlæg.',after=20,line=245)
m.section('UDDANNELSE OG CERTIFICERING')
for a,b in [('B.Tech, Technology Management and Mechanical Engineering','Copenhagen School of Marine Engineering & Technology Management · 2017–2022'),('Elautoriseret maskinmester, LV/MV/HV','Sikkerhedsstyrelsen · 2023'),('PRINCE2 certificeret projektleder','AXELOS / PeopleCert'),('Køleteknik og klimaanlæg','Mercantec AMU · 2021'),('El- og maskinteknisk design, elteknik','Tehran Technical University · 2000–2003')]:m.edu(a,b)
m.section('METODER, VÆRKTØJER OG SPROG')
m.para('**Metoder:** PRINCE2, Lean og Six Sigma anvendt i praksis; PRINCE2 certificeret. **Teknik og systemer:** SCADA, Excel, SAP ERP og digitale værktøjer til planlægning og kvalitet. **Sprog:** dansk, engelsk og persisk. **Kørekort:** B.',after=20,line=250,justify=False)
m.save(str(R/'Shahram_Ajloo_LTF_Moelleaavaerket_Driftsleder.docx'))
