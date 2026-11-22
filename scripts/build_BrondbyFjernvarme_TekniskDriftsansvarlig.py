"""Motiveret og fyldigt CV for Brøndby Fjernvarme."""
from pathlib import Path
from master_design import MasterDoc
R=Path(__file__).resolve().parent.parent
m=MasterDoc(str(R/'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='da-DK')
n='SHAHRAM AJLOO';t='Maskinmester | Teknisk drift, forsyning og vedligehold'
c='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
m.resume_header(n,t,c,'PROFIL OG MOTIVATION')
m.meta('Brøndby Fjernvarme · Maskinmester / teknisk driftsansvarlig',after=30)
m.para('**Motivation:** Stabil varme kræver, at overvågning, forebyggende vedligehold og hurtig, sikker håndtering af alarmer hænger sammen. Jeg søger rollen for at bruge min erfaring fra kritisk forsyningsdrift og eltekniske anlæg til at holde hverdagen overskuelig for driftsmedarbejderen og forsyningen stabil for kunderne. Det nære samarbejde med kolleger, VEKS og eksterne fagfolk er en vigtig del af opgaven.',after=60,line=245,justify=False)
m.para('Elautoriseret maskinmester med praktisk erfaring i fejlfinding, vedligehold, pumper, el- og mekaniske anlæg, SCADA og teknisk koordinering. Fra BIOFOS bringes erfaring med kritisk 24/7-drift; fra ELOHVAC og Novo Nordisk erfaring med sikkerhed, dokumentation og opfølgning. Erfaringen er fra tekniske anlæg og anden forsyning frem for dokumenteret selvstændig fjernvarme- og kedeldrift.',after=55,line=245,justify=False)
m.section('KOMPETENCER TIL BRØNDBY FJERNVARMES DRIFT')
for a,b in [
 ('Stabil drift og fejl','Forebyggende vedligehold og akut fejlfinding på el- og mekaniske installationer i 24/7-drift hos BIOFOS. Arbejder systematisk med at afgrænse fejl, vurdere sikkerheden og inddrage den relevante fagperson.'),
 ('Pumper, el og overvågning','BIOFOS: pumper, HVAC, højspændingstavler og SCADA. ELOHVAC: installation, tavler, styring, elteknisk fejlfinding og service. Har ledet arbejde med industrielle PLC- og styresystemer.'),
 ('Opgaver og samarbejde','Planlægning og prioritering af medarbejdere, materialer, entreprenører og opgaver. Leder fem elektrikere og tre lærlinge i ELOHVAC; har tidligere ledet 14 medarbejdere i Ventek-Air.'),
 ('Vedligehold og dokumentation','Erfaring med planlagt vedligehold, kvalitetssikring, risikovurdering, LOTO og teknisk afleveringsdokumentation. Novo Nordisk: FAT/SAT og IQ/OQ/PQ under GMP med nul kritiske afvigelser ved aflevering.'),
 ('Tal og forbedringer','Hos Novo Nordisk reducerede et PDCA-program energiomkostninger med 40 %. Bruger SAP ERP, Excel og digitale værktøjer til opfølgning, planlægning og beslutningsstøtte.'),
 ('Leverandører og økonomi','Fuldt P&L-ansvar i ELOHVAC med tilbud, beregninger, materialer og underentreprenører. Erfaring med forecast og kontraktopfølgning i drifts- eller serviceleverancer.')]:m.bullet(a,b,after=20,line=240)
m.models_table('ARBEJDSFORM — FORSLAG TIL DEN DAGLIGE VARMEFORSYNING',('Situation','Praktisk tilgang sammen med drift og relevante fagfolk'),[
 ('Alarm og forsyning','Vurder alarmen og dens betydning for varmeforsyningen. Kontrollér oplysninger i SRO og på anlægget efter oplæring; afgræns fejlen, sikr anlægget og tilkald hjælp, når opgaven eller kompetencen kræver det.'),
 ('Forebyggende drift','Gennemgå temperatur, tryk, flow og driftstimer med kollegaen; planlæg service, eftersyn og opfølgning på pumper, varmevekslere og øvrigt udstyr efter lokale instruktioner.'),
 ('Samarbejde og dokumentation','Afklar driftsforhold med VEKS; aftal opgaver og opfølgning med leverandører. Registrér arbejdet og følg op på miljøindberetninger og myndighedskrav med ansvarlige kolleger.'),
 ('Beredskab og kedler','Gennemgå vagtinstrukser og afprøv beredskabsplaner sammen med teamet. Arbejde med olie- og gasfyrede kedler forudsætter de krævede certifikater og lokale tilladelser.')])
m.page_break();m.section('ERHVERVSERFARING — KRITISK DRIFT OG TEKNISKE ANLÆG')
m.job('Vedligeholdelses- og driftsleder / værkstedstekniker','BIOFOS, Lynetten · København · aug. 2017–jan. 2022')
for a,b in [('Forsyningsdrift','Kritisk el- og mekanisk drift med pumper, HVAC, højspændingstavler og SCADA; forebyggende vedligehold og akut fejlfinding i 24/7-miljø.'),('Systematik og sikkerhed','Arbejdede med reservedelsflow, lagerstyring, 5S, standardarbejde og PDCA samt LOTO og risikovurdering i skifteholdsdrift.')]:m.bullet(a,b,after=20,line=240)
m.job('Indehaver / teknisk direktør / elautoriseret maskinmester','ELOHVAC ApS · København · maj 2023–nu')
for a,b in [('El, styring og vedligehold','Installation, tavler, styring, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg for erhvervskunder.'),('Planlægning og koordinering','Ledelse af fem elektrikere og tre lærlinge; opgavefordeling, oplæring, materialer, underentreprenører, kvalitet og aflevering. Fuldt P&L-ansvar og kundeopfølgning.'),('Sikkerhed og digital opfølgning','Risikovurdering ved pladsopstart, LOTO og arbejdsmiljøopfølgning. AI-assisterede værktøjer til tilbud, tidsplaner, kvalitetstjek og KPI’er bidrog til over 40 % produktivitetsforbedring.')]:m.bullet(a,b,after=20,line=240)
m.job('Senior idriftsættelsesingeniør / projektleder, elsystemer','Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024')
for a,b in [('Kvalitet og aflevering','FAT/SAT og IQ/OQ/PQ på elsystemer i reguleret miljø, med nul kritiske afvigelser ved aflevering. Koordinerede 25 specialister på 37 samtidige CAPEX-projekter.'),('Fremdrift og forbedring','Opfølgning på økonomi, ressourcer, risiko og fremdrift; A3, 5 x hvorfor og Ishikawa til fejlfinding. Et PDCA-program reducerede energiomkostningerne med 40 %.')]:m.bullet(a,b,after=20,line=240)
m.job('Projekt- og værkstedsleder','Ventek-Air · København · jan. 2022–nov. 2022')
m.bullet('Mennesker og leverance','Ledte 14 medarbejdere og 11 samtidige tekniske projekter; kapacitetsplanlægning, underentreprenører, daglige tavlemøder, sikkerhedsdokumentation og aflevering.',after=20,line=240)
m.page_break();m.section('ERHVERVSERFARING — DIGITALT ARBEJDE OG TEKNISK LEDELSE')
m.job('Medejer og CTO / ansvarlig for AI- og AI coding-afdelingen','Data Power Consultant ApS · København · 2024–nov. 2026')
for a,b in [('Tekniske løsninger','Ledte en AI-afdeling med 4–10 personer og arbejdede med tekniske og industrielle applikationer fra kravafdækning og integration til dokumentation og overdragelse.'),('AI og styring','AI-kodning, LLM-API’er og AI-agenter samt fagligt kontrolleret teknisk design og ledelsesrapportering. Stillingen var sideløbende med ELOHVAC; virksomheden er ophørt.')]:m.bullet(a,b,after=20,line=240)
m.job('Elektromekaniker / produktionsteamleder','ARJ Engineering · Teheran · dec. 2003–mar. 2010')
for a,b in [('Teknisk ledelse','Ledte 12 mekanikere og teknikere; vagtplanlægning, materialer, fejldiagnose og reparation af industrielt el- og mekanisk udstyr.'),('Produkt og økonomi','Produktporteføljeansvar for elektromotorer og pumper, herunder forretningscases, pris- og investeringsbeslutninger.')]:m.bullet(a,b,after=20,line=240)
m.section('UDDANNELSE, KVALIFIKATIONER OG VÆRKTØJER')
for a,b in [('Elautoriseret maskinmester, LV/MV/HV','Sikkerhedsstyrelsen · 2023'),('B.Tech, teknologiledelse og maskinteknik','Københavns Maskinmesterskole · 2017–2022'),('El- og maskinteknisk design, elteknik','Tehran Technical University · 2000–2003'),('PRINCE2-certificeret projektleder','AXELOS / PeopleCert'),('Køleteknik og klimaanlæg','Mercantec · AMU · 2021'),('STCW-sikkerheds- og maskinrelaterede kurser','Søfartsstyrelsen · 2021–2023')]:m.edu(a,b)
m.para('**Drifts- og ledelsesmetoder:** Lean og Six Sigma i praksis, PDCA, A3, 5S, standardarbejde, risikovurdering og visuel opfølgning. PRINCE2-certificeret. **IT:** SAP ERP, Excel, Power BI og AI-assisteret planlægning. **Sprog:** Dansk og persisk (modersmål), engelsk på professionelt niveau. **Kørekort:** B. **Bopæl:** Måløv.',after=35,line=240,justify=False)
m.models_table('FORSLAG TIL OPSTART — FØRSTE 90 DAGE',('Periode','Fokus sammen med direktør, driftsmedarbejder og samarbejdspartnere'),[
 ('Dag 1–30','Gennemgå anlæg, SRO, alarmer, sikkerhedsprocedurer, vagtinstrukser og samarbejdsflader til VEKS. Afklar ansvarsfordeling, nødvendige certifikater og den påkrævede sikkerhedsgodkendelse før selvstændigt arbejde.'),
 ('Dag 30–60','Planlæg vedligehold og opfølgning sammen med driftsmedarbejderen. Gennemgå serviceaftaler, kritiske reservedele, driftstal og dokumentations- og indberetningsfrister med de ansvarlige.'),
 ('Dag 60–90','Følg op på alarmer og tilbagevendende fejl, gennemgå og afprøv beredskabsplaner med teamet og foreslå konkrete forbedringer til direktøren. Arbejd kun inden for de tilladelser og kompetencer, der er på plads.')])
m.save(str(R/'Shahram_Ajloo_BrondbyFjernvarme_TekniskDriftsansvarlig_CV.docx'))
