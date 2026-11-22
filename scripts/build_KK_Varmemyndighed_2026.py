"""Københavns Kommune: varmesagsbehandler, ansøgning + CV i masterdesign."""
from pathlib import Path
from master_design import MasterDoc
R=Path(__file__).resolve().parent.parent
m=MasterDoc(str(R/'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='da-DK')
n='SHAHRAM AJLOO'; t='Sagsbehandler · varmeforsyning, klima og miljø | Københavns Kommune'
c='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
m.header_banner(n,t,c)
m.meta('Klima-, Miljø- og Teknikforvaltningen · Virksomheder og VVM',after=30)
m.para('**Ansøgning: Sagsbehandler inden for varmeforsyning, klima og miljø**',after=95,justify=False)
m.para('Kære varmeteam',after=75,justify=False)
m.para('Københavns varmeforsyning skal omstilles, samtidig med at forsyningssikkerhed, økonomi og klima tænkes sammen. Det stiller krav til sagsbehandlingen: Ansøgernes tekniske løsninger og beregninger skal kunne gennemskues, relevante hensyn skal belyses, og beslutninger skal hvile på et klart og lovligt grundlag.',after=95,line=265,justify=False)
for a,b in [
('Et grundlag, der kan efterprøves','Jeg vil begynde med at afgrænse projektet og kontrollere, om ansøgning, varmebehov, tekniske data og beregningsforudsætninger er tilstrækkelige. Mangler samles i en konkret tilbagemelding til ansøgeren. El- og varmeenheder, driftstimer og anlæggenes virkningsgrad skal hænge sammen, før resultaterne bruges videre.'),
('Samfundsøkonomi og alternativer','Projekt og relevante alternativer bør sammenlignes på et fælles og dokumenteret grundlag. Jeg vil gennemgå investeringer, drift, energipriser, CO2-emissioner og levetider efter de gældende beregningsforudsætninger og undersøge, hvordan centrale usikkerheder påvirker resultatet. Samfundsøkonomi skal holdes adskilt fra bruger- og selskabsøkonomi.'),
('En ordentlig myndighedsproces','For hvert projekt vil jeg afklare varmeforsyningsloven, projektbekendtgørelsen, forvaltningsret, delegation og høringsbehov med teamet og relevante jurister. Høringer, høringssvar og væsentlige vurderinger skal fremgå af sagen, så en politisk indstilling klart viser alternativer, konsekvenser og usikkerheder. Projektgodkendelser og ansøgninger om fritagelse fra tilslutningspligt behandles efter de regler og den praksis, der gælder for den konkrete sag.'),
('Fælles retning på tværs','Dialog med HOFOR, energirådgivere og entreprenører skal være tydelig om proces og behov for oplysninger uden at foregribe afgørelsen. I stjernemøder og arbejdsgrupper vil jeg dele det tekniske overblik med klima-, plan- og miljøkolleger. Borgerhenvendelser og aktindsigt kræver klar kommunikation og behandling efter kommunens gældende procedurer.')]:m.bullet(a,b,after=70,line=260)
m.para('Jeg ser frem til at drøfte, hvordan et grundigt beslutningsgrundlag kan understøtte kommunens klimaarbejde og samtidig give ansøgere en forståelig proces. Jeg har set stillingen hos TechJob.',after=75,line=260,justify=False)
m.meta('Med venlig hilsen',after=15);m.meta('Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com',after=0)
m.page_break();m.resume_header(n,t,c,'TEKNISK OG ANALYTISK GRUNDLAG FOR VARMESAGER')
m.para('Elautoriseret maskinmester med teknisk baggrund inden for el, HVAC, anlægsdrift og projektøkonomi. Har arbejdet med beregninger, teknisk dokumentation og tværfaglig koordinering i energi- og anlægsopgaver. Erfaringen giver et praktisk grundlag for at gennemgå varmeprojekters data og samarbejde med specialister om sagsbehandling og myndighedsgrundlag.',after=70,line=260,justify=False)
m.section('KOMPETENCER RELEVANTE FOR VARMETEAMET')
for a,b in [
('El, varme og anlæg','Maskinmesteruddannelse og praktisk arbejde med el-, ventilations- og klimaanlæg; kritisk teknisk drift, pumper og HVAC hos BIOFOS.'),
('Tal og beregninger','Tilbudsberegning, projektøkonomi, regneark og digitale modeller. Investeringsmodeller med nutidsværdi og følsomhedsanalyser er relevante analytiske værktøjer; samfundsøkonomisk metode skal følge de gældende myndighedsforudsætninger.'),
('Dokumentation og kvalitet','Kvalitetssikring og afleveringsdokumentation i tekniske projekter; FAT/SAT og IQ/OQ/PQ ved Novo Nordisk med nul kritiske afvigelser ved aflevering.'),
('Tværfagligt samarbejde','Koordinering af engineering, indkøb, anlæg og specialister; kundedialog og samarbejde med underentreprenører i tekniske leverancer.'),
('Digital understøttelse','Excel, SAP ERP, Python og egne AI-værktøjer til beregning, planlægning og kvalitetstjek; faglig kontrol af output.')]:m.bullet(a,b,after=40,line=250)
m.section('ERHVERVSERFARING')
m.job('Ejer / teknisk direktør / elautoriseret maskinmester','ELOHVAC ApS · København · maj 2023–nu')
for a,b in [('Teknik og beregning','Installation, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg; tilbud, beregning, planlægning og fuldt resultatansvar.'),('Dokumentation og samarbejde','Kundedialog, underentreprenører, kvalitetssikring og afleveringsdokumentation. Leder fem elektrikere og tre lærlinge.'),('Digital forbedring','Egne værktøjer til tilbud, tidsplaner og kvalitetstjek har bidraget til et produktivitetsløft på over 40 %.')]:m.bullet(a,b,after=25,line=250)
m.job('Medejer og CTO / teknisk ansvarlig for AI-afdelingen','Data Power Consultant ApS · København · 2024–nov. 2026')
m.bullet('Tekniske kundeløsninger','Ansvarlig for afdeling med 4–10 personer og tekniske applikationer fra kravafdækning til dokumentation og overdragelse. Sideløbende med ELOHVAC; virksomheden er ophørt.',after=25,line=250)
m.page_break();m.section('ERHVERVSERFARING — FORTSAT')
m.job('Senior idriftsættelsesingeniør / projektleder, elsystem','Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024')
for a,b in [('Projektgrundlag','Koordinerede 37 samtidige CAPEX-projekter og 25 specialister; opfølgning på økonomi, fremdrift, ressourcer og risici på tværs af engineering, indkøb og anlæg.'),('Teknisk kvalitet','Arbejdede med el-tekniske anlæg og FAT/SAT samt IQ/OQ/PQ i reguleret miljø; nul kritiske afvigelser ved aflevering.')]:m.bullet(a,b,after=25,line=250)
m.job('Projekt- og værkstedsleder','Ventek-Air · København · jan. 2022–nov. 2022')
m.bullet('Planlægning og aflevering','Ledede et team på 14 og styrede 11 samtidige anlægsprojekter; arbejdede med tilbud, aftalegrundlag, underentreprenører og afleveringspakker.',after=25,line=250)
m.job('Vedligeholdelses- og driftsleder / værkstedstekniker','BIOFOS, Lynetten · København · aug. 2017–jan. 2022')
m.bullet('Energi og driftsforståelse','Kritisk el- og mekanisk drift med pumper, HVAC, højspændingstavler og SCADA; forebyggende vedligehold, fejlfinding og sikkerhed i skifteholdsdrift.',after=25,line=250)
m.job('Elektromekaniker / produktionsteamleder','ARJ Engineering · Teheran · dec. 2003–mar. 2010')
m.bullet('Tekniske anlæg','Ledede 12 mekanikere og teknikere med planlægning og materialestyring; fejldiagnose og reparation af industrielle el- og mekaniske anlæg.',after=25,line=250)
m.section('UDDANNELSE OG CERTIFICERING')
for a,b in [('B.Tech, Technology Management and Mechanical Engineering','Copenhagen School of Marine Engineering & Technology Management · 2017–2022'),('Elautoriseret maskinmester, LV/MV/HV','Sikkerhedsstyrelsen · 2023'),('PRINCE2 certificeret projektleder','AXELOS / PeopleCert'),('Køleteknik og klimaanlæg','Mercantec AMU · 2021'),('El- og maskinteknisk design, elteknik','Tehran Technical University · 2000–2003')]:m.edu(a,b)
m.section('METODER, VÆRKTØJER OG SPROG')
m.para('**Beregning og dokumentation:** Excel, SAP ERP, Python, digitale tjeklister og investeringsmodeller. **Metoder:** PRINCE2, Lean og Six Sigma anvendt i praksis; PRINCE2 certificeret. **Sprog:** dansk, engelsk og persisk. **Kørekort:** B.',after=30,line=250,justify=False)
m.section('TILGANG TIL VARMESAGER — FORSLAG')
for a,b in [('Oplysning','Afgræns ansøgning og relevante alternativer; indhent manglende data og dokumentér forudsætninger.'),('Vurdering','Gennemgå energi, økonomi og følsomheder; afklar lovgrundlag og proces med fagkolleger og jurister.'),('Beslutning','Saml høringssvar, vurderinger og usikkerheder i en klar indstilling; følg delegation og kommunens procedurer for afgørelse og aktindsigt.')]:m.bullet(a,b,after=25,line=250)
m.save(str(R/'Shahram_Ajloo_Koebenhavn_Varmeforsyning_2026.docx'))
