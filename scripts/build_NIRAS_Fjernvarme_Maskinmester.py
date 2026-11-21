"""NIRAS fjernvarme: jobrettet dansk ansøgning og CV i master-/RegionH-stil."""
from pathlib import Path
from master_design import MasterDoc
R=Path(__file__).resolve().parent.parent
m=MasterDoc(str(R/'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='da-DK')
n='SHAHRAM AJLOO';t='Maskinmester | Fjernvarmeprojekter · NIRAS'
c='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
m.header_banner(n,t,c);m.meta('NIRAS · Att.: afdelingschef Jesper Graa Andreasen',after=30)
m.para('**Ansøgning: Erfaren maskinmester til fjernvarmeprojekter**',after=70,justify=False)
m.para('Kære Jesper Graa Andreasen',after=65,justify=False)
m.para('Når en kritisk komponent i en energicentral til fjernvarme skal udskiftes, skal kunden kunne træffe en beslutning med kendskab til både anlæggets tilstand, konsekvensen for varmeforsyningen og mulighederne for et sikkert indgreb. Det er i krydsfeltet mellem teknisk analyse og den praktiske drift, jeg ønsker at bidrage til NIRAS’ fjernvarmeprojekter.',after=65,line=245,justify=False)
m.para('Jeg vil arbejde tæt sammen med kundens driftsfolk og NIRAS’ maskin-, el- og SRO-specialister, så anbefalingerne kan gennemføres på det konkrete anlæg. Opgaven vil jeg gribe an i fire trin:',after=55,line=240,justify=False)
for a,b in [
('Fra anlægsbesøg til beslutningsgrundlag','Gennemgå tilgængelig dokumentation, fejl- og vedligeholdshistorik med driftspersonalet og besigtige komponenterne på stedet. Sammenhold observationer og relevante driftsdata med leverandørens krav. Maskintekniske analyser og beslutningsgrundlag skal vise tilstand, usikkerheder, risiko ved fortsat drift og mulige næste skridt.'),
('Komponentvalg med blik for hele anlægget','I et deep dive vil jeg sammenligne relevante løsninger på kapacitet, driftsforhold, tilslutninger, tilgængelighed, vedligehold og levetidsomkostninger. Pumper, ventiler, varmevekslere, trykholdesystemer, kedler, elmotorer, frekvensomformere, målere, transmittere, varmepumper og røranlæg vurderes efter den konkrete opgave og med de relevante fagspecialister.'),
('Udskiftning uden at miste overblikket','Afstem løsning og leverance med kunde, leverandør og servicepartner. Planlæg udførelsen med blik for forsyningssikkerhed, adgang, reservedele, afprøvning og tilbagelevering. Ved sikkerhedsnedlukninger vil jeg støtte kundens ansvarlige med dokumentation og koordinering; afstilling og indgreb sker efter kundens procedurer og hos bemyndiget personale.'),
('Vedligehold, der kan bruges i hverdagen','Opbyg sammen med driften en vedligeholdelsesplan med komponentansvar, prioritet, intervaller, dokumentationskrav og opfølgning. Planen bør tage udgangspunkt i anlæggets kritikalitet, kendte fejl og leverandøranbefalinger og justeres, når nye erfaringer eller driftsdata giver grundlag for det.')]:m.bullet(a,b,after=35,line=240)
m.para('På BIOFOS’ renseanlæg Lynetten arbejdede jeg med pumper, el- og mekaniske anlæg, SCADA, forebyggende vedligehold og akut fejlfinding i døgnbemandet drift. I ELOHVAC arbejder jeg med installation og vedligehold på el-, ventilations- og klimaanlæg; hos Novo Nordisk koordinerede jeg 25 specialister på 37 samtidige projekter med dokumenteret aflevering. Det er erfaring, jeg vil bruge til at forene den maskintekniske vurdering med driftens behov og de øvrige fag.',after=55,line=245,justify=False)
m.para('NIRAS’ rådgivning om varmepumpeanlægget i Kalundborg viser, hvordan energi- og forsyningssystemer kan tænkes sammen. Jeg ser frem til at drøfte, hvordan jeg kan bidrage til beslutningsgrundlag og vedligeholdelsesløsninger for jeres kunder.',after=45,line=245,justify=False)
m.meta('Med venlig hilsen · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com',after=0)
m.page_break();m.resume_header(n,t,c,'MASKINTEKNIK, DRIFT OG FORSYNINGSSIKKERHED')
m.para('Elautoriseret maskinmester med erfaring fra kritisk el- og mekanisk drift, forebyggende vedligehold og tekniske projekter. Kombinationen af arbejde på BIOFOS/Lynetten, teknisk service i ELOHVAC og tværfaglig koordinering hos Novo Nordisk giver et praktisk grundlag for rådgivning om komponenter, drift og vedligehold.',after=60,line=245,justify=False)
m.section('ERFARING RELEVANT FOR FJERNVARMEPROJEKTER')
for a,b in [
('Pumper og kritisk drift','BIOFOS/Lynetten: drift og vedligehold af pumper, HVAC, højspændingstavler og SCADA, herunder forebyggende vedligehold og akut fejlfinding i døgnbemandet drift.'),
('Maskin- og elteknik','Maskinmesteruddannelse, køleteknik og erfaring med el-, ventilations- og klimaanlæg. ARJ Engineering: fejldiagnose og reparation af industrielle el- og mekaniske anlæg.'),
('Vedligehold og sikkerhed','Erfaring med planlagt vedligehold, reservedelsflow, LOTO, APV og risikovurdering. Arbejder med sikker udførelse og dokumentation i samarbejde med de ansvarlige fagpersoner.'),
('Projekt- og leverandørsamarbejde','Novo Nordisk: koordinering af 25 specialister på 37 samtidige projekter. ELOHVAC og Ventek-Air: planlægning, underentreprenører, kvalitetssikring og aflevering.'),
('Beslutningsstøtte og forbedring','Anvender systematisk problemløsning og digitale værktøjer til planlægning og kvalitet. AI-værktøjer i ELOHVAC bidrog til et produktivitetsløft på over 40 %.')]:m.bullet(a,b,after=20,line=240)
m.models_table('RÅDGIVNINGSOPGAVEN — FORSLAG TIL FREMGANGSMÅDE',('Opgave','Praktisk leverance til kunden'),[
('Tilstandsvurdering','Gennemgå dokumentation og historik; besigtig med driftspersonale og sammenfat observationer, usikkerhed og anbefalede næste skridt.'),
('Analyse og komponentvalg','Sammenlign teknisk egnethed, driftsforhold, tilgængelighed og levetidsomkostninger med kunde og leverandører.'),
('Udskiftning og nedlukning','Afstem plan, risici, sikker afstilling, test og overdragelse med kunden og relevante el-, SRO- og maskinfag.'),
('Vedligeholdelsesplan','Prioritér komponenter efter kritikalitet; aftal opgaver, intervaller, ansvar og dokumentation med drift og servicepartnere.'),
('Faglig sparring','Omsæt kundens driftsobservationer og faglige input til et beslutningsgrundlag med klare forudsætninger og anbefalinger.')])
m.section('UDVALGTE RESULTATER')
for a,b in [('Projekter og kvalitet','Novo Nordisk: 37 samtidige projekter og 25 specialister; nul kritiske afvigelser ved aflevering.'),('Energiforbedring','Novo Nordisk: 40 % reduktion af energiomkostninger via et PDCA-program.'),('Planlægning og leverance','Ventek-Air: 11 samtidige projekter og 14 medarbejdere; ELOHVAC: fuldt resultatansvar.')]:m.bullet(a,b,after=15,line=235)
m.page_break();m.section('ERHVERVSERFARING')
m.job('Ejer / teknisk direktør / elautoriseret maskinmester','ELOHVAC ApS · København · maj 2023–nu')
for a,b in [('Teknisk drift','Installation, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg for erhvervskunder.'),('Projekt og samarbejde','Tilbud, beregning, planlægning, materialer, underentreprenører, kvalitetssikring og afleveringsdokumentation; fuldt resultatansvar.'),('Forbedringer','AI-værktøjer til tilbud, tidsplaner og kvalitetstjek bidrog til et produktivitetsløft på over 40 %.')]:m.bullet(a,b,after=15,line=240)
m.job('Medejer og CTO / teknisk ansvarlig for AI-afdelingen','Data Power Consultant ApS · København · 2024–nov. 2026')
m.bullet('Tekniske løsninger','Ledede 4–10 personer og arbejdede med tekniske applikationer fra behovsafklaring til dokumentation og overdragelse. Sideløbende med ELOHVAC; virksomheden er ophørt.',after=15,line=240)
m.job('Senior idriftsættelsesingeniør / projektleder, elsystem','Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024')
for a,b in [('Koordinering','25 specialister og 37 samtidige CAPEX-projekter; fremdrift, økonomi, risici og ressourcer på tværs af engineering, indkøb og anlæg.'),('Kvalitet og energi','FAT/SAT og IQ/OQ/PQ med nul kritiske afvigelser ved aflevering. Et PDCA-program reducerede energiomkostningerne med 40 %.')]:m.bullet(a,b,after=15,line=240)
m.job('Projekt- og værkstedsleder','Ventek-Air · København · jan. 2022–nov. 2022')
m.bullet('Projekter','Ledede 14 medarbejdere og 11 samtidige anlægsprojekter med planlægning, underentreprenører, sikkerhedsdokumentation og aflevering.',after=15,line=240)
m.job('Vedligeholdelses- og driftsleder / værkstedstekniker','BIOFOS, Lynetten · København · aug. 2017–jan. 2022')
for a,b in [('Tekniske anlæg','El- og mekanisk drift af blandt andet pumper, HVAC, højspændingstavler og SCADA; forebyggende vedligehold og akut fejlfinding.'),('Sikkerhed og systematik','Skifteholdsdrift med LOTO, risikovurdering og APV; reservedelsflow, 5S og PDCA på værksted og lager.')]:m.bullet(a,b,after=15,line=240)
m.job('Elektromekaniker / produktionsteamleder','ARJ Engineering · Teheran · dec. 2003–mar. 2010')
m.bullet('Drift og reparation','Ledede 12 mekanikere og teknikere; vagtplanlægning, materialestyring, fejldiagnose og reparation af industrielle el- og mekaniske anlæg.',after=15,line=240)
m.section('UDDANNELSE, METODER OG SPROG')
for a,b in [('B.Tech, Technology Management and Mechanical Engineering','Copenhagen School of Marine Engineering & Technology Management · 2017–2022'),('Elautoriseret maskinmester, LV/MV/HV','Sikkerhedsstyrelsen · 2023'),('PRINCE2 certificeret projektleder','AXELOS / PeopleCert'),('Køleteknik og klimaanlæg','Mercantec AMU · 2021'),('El- og maskinteknisk design, elteknik','Tehran Technical University · 2000–2003')]:m.edu(a,b)
m.para('**Metoder:** PRINCE2, Lean og Six Sigma anvendt i praksis; certificeret i PRINCE2. **Systemer:** SCADA, Excel, SAP ERP og digitale planlægningsværktøjer. **Sprog:** dansk, engelsk og persisk. **Kørekort:** B.',after=20,line=235,justify=False)
m.page_break();m.models_table('FØRSTE OPGAVER — FORSLAG TIL ARBEJDSFORM',('Fase','Samarbejde og leverance'),[
('Opstart','Aftal kundens beslutningsbehov, anlæggets driftsbetingelser og rammerne for adgang og sikkerhed. Indhent tilgængelige tegninger og historik.'),
('På anlægget','Besigtig sammen med driftspersonalet og afklar observationer, kritiske komponenter og nødvendige input fra leverandører og øvrige fag.'),
('Vurdering','Sammenlign relevante løsninger, forudsætninger og risici. Aftal behov for yderligere analyse med maskin-, el- og SRO-specialister.'),
('Leverance og opfølgning','Præsenter anbefaling, vedligeholdelsesbehov og næste beslutninger; afstem tidsplan, sikkerhed og overdragelse med kunden.')])
m.section('FAGLIGT SAMARBEJDE')
for a,b in [('Kundens drift og vedligehold','Tag udgangspunkt i erfaringerne på anlægget, og afstem forslag mod de faktiske driftsvilkår.'),('NIRAS’ maskin-, el- og SRO-fag','Saml de relevante fag om grænseflader, sikkerhed og funktion før ændringer anbefales.'),('Leverandører og servicepartnere','Afklar tekniske data, vedligeholdelseskrav, levering og dokumentation for de valgte løsninger.')]:m.bullet(a,b,after=25,line=240)
m.save(str(R/'Shahram_Ajloo_NIRAS_Fjernvarme_Maskinmester.docx'))
