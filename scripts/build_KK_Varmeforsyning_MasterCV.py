"""Varmemyndighed — ansøgning og fyldigt CV i uploadet masterdesign."""
from pathlib import Path
from master_design import MasterDoc
R=Path(__file__).resolve().parent.parent
m=MasterDoc(str(R/'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='da-DK')
n='SHAHRAM AJLOO';title='Sagsbehandler — varmeforsyning, klima og miljø | Københavns Kommune'
c='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
m.header_banner(n,title,c)
m.meta('Klima-, Miljø- og Teknikforvaltningen · Virksomheder og VVM',after=25)
m.para('**Ansøgning: Sagsbehandler til kommunens varmeteam**',after=100,justify=False)
m.para('Kære varmeteam',after=70,justify=False)
m.para('Omstillingen af Københavns varmeforsyning skal forene klima, forsyningssikkerhed og økonomi. Når et projektforslag kommer ind, er opgaven derfor både at forstå den tekniske løsning og at sikre en gennemskuelig sagsbehandling og et solidt grundlag for myndighedens beslutning. Det kræver et tæt samspil mellem varmeteamet, ansøgerne og kollegerne på klima- og planområdet.',after=80,line=260,justify=False)
m.para('**Fra ansøgning til beslutning: sådan vil jeg gribe opgaven an**',after=40,justify=False)
for a,b in [
('Sagsoplysning og vejledning','Afgræns projekt og område, gennemgå ansøgningsmaterialet, og saml mangler i en klar tilbagemelding. Kontroller varmebehov, kapacitet, driftsforudsætninger og sammenhængen mellem effekt og energi, så sammenligningen hviler på et oplyst grundlag.'),
('Samfundsøkonomiske beregninger','Gennemgå projekt og relevante alternativer med ensartet tidshorisont og dokumenterede forudsætninger for investering, drift, el- og varmeforbrug samt CO2. Brug gældende vejledning og beregningsforudsætninger; følsomheder for eksempelvis energipris, varmebehov og varmepumpens virkningsgrad skal gøre usikkerheden synlig. Adskil samfundsøkonomi fra bruger- og selskabsøkonomi.'),
('Myndighed og politisk behandling','Afklar varmeforsyningsloven, projektbekendtgørelsen, forvaltningsret, delegation og eventuelle høringer med teamet og jurister. En indstilling skal klart vise faktum, relevante alternativer, vurdering, konsekvenser og høringssvar. Projektgodkendelser og fritagelse fra tilslutningspligt håndteres efter de regler og den praksis, der gælder i den konkrete sag.'),
('Et samarbejde, der bringer sagen videre','Vejled HOFOR, energirådgivere og entreprenører om proces og manglende oplysninger uden at foregribe afgørelsen. Brug stjernemøder og arbejdsgrupper med klima-, miljø- og planfaglige kolleger til at afklare afhængigheder, dele ny viden og løse tværgående spørgsmål.'),
('Tydelige svar til borgerne','Besvar henvendelser i et sprog, der forklarer næste skridt og grundlaget for afgørelsen. Høringer og aktindsigt håndteres efter gældende regler og kommunens procedurer, med fokus på sporbarhed og rettidig opfølgning.')]:m.bullet(a,b,after=45,line=255)
m.para('Et godt beslutningsgrundlag gør det muligt at vurdere de tekniske muligheder, uden at klima, økonomi eller de berørte parter forsvinder i beregningerne. Jeg ser frem til at drøfte opgaven og har set stillingen hos TechJob.',after=60,line=255,justify=False)
m.meta('Med venlig hilsen',after=15);m.meta('Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com',after=0)
m.page_break();m.resume_header(n,title,c,'FAGLIG PROFIL — VARME, BEREGNING OG DOKUMENTATION')
m.para('Elautoriseret maskinmester med teknisk erfaring fra el-, ventilations- og klimaanlæg samt drift af pumper, HVAC og kritiske installationer. Har arbejdet med tekniske beregninger, projektøkonomi, dokumentation og tværfaglig koordinering. Disse erfaringer understøtter gennemgang af datagrundlag og tekniske løsninger i varmeprojekter og samarbejde om en grundig myndighedsproces.',after=65,line=255,justify=False)
m.section('FAGLIGE KOMPETENCER — RETTET MOD VARMETEAMETS OPGAVER')
for a,b in [
('Varme og el','Maskinmesteruddannelse, køleteknik og praktisk arbejde med el, HVAC og tekniske anlæg. Driftsforståelse fra BIOFOS og el-/klimaservice i ELOHVAC.'),
('Økonomi og analyser','Tilbudsberegning, projektøkonomi og fuldt P&L-ansvar; investeringsmodeller med nutidsværdi og følsomhedsanalyse. Relevante værktøjer ved gennemgang af økonomiske antagelser; samfundsøkonomiske analyser kræver deres eget metodegrundlag.'),
('Datagrundlag og dokumentation','Teknisk projektmateriale, kvalitetssikring og afleveringsdokumentation. FAT/SAT og IQ/OQ/PQ ved Novo Nordisk med nul kritiske afvigelser ved aflevering.'),
('Samarbejde og kommunikation','Kundedialog og samarbejde med underentreprenører; koordinering af engineering, indkøb, anlæg og specialister samt afrapportering til ledelse og bygherre.'),
('Digitale værktøjer','Excel-regneark, SAP ERP, Python og AI-baserede værktøjer til beregning, planlægning og kvalitetstjek. Faglig kontrol af resultater og dokumentation.')]:m.bullet(a,b,after=25,line=245)
m.section('ERHVERVSERFARING')
m.job('Ejer / teknisk direktør / elautoriseret maskinmester','ELOHVAC ApS · København · maj 2023–nu')
for a,b in [
('Tekniske anlæg','El-tekniske serviceopgaver for erhvervskunder: installation, tavler, styring, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg.'),
('Beregning og økonomi','Tilbud og beregning, materialer, planlægning og fuldt resultatansvar for entrepriser og serviceleverancer.'),
('Kvalitet og koordinering','Kundedialog, underentreprenører, kvalitetssikring og afleveringsdokumentation; personaleansvar for fem elektrikere og tre lærlinge.'),
('Resultat','Egne værktøjer til tilbud, tidsplaner og kvalitetstjek har bidraget til et produktivitetsløft på over 40 %.')]:m.bullet(a,b,after=15,line=245)
m.job('Medejer og CTO / teknisk ansvarlig for AI-afdelingen','Data Power Consultant ApS · København · 2024–nov. 2026')
for a,b in [('Tekniske løsninger','Ansvarlig for afdeling med 4–10 personer; implementering af tekniske og industrielle applikationer fra kravafdækning til dokumentation og overdragelse.'),('Sideløbende arbejde','Stillingen var sideløbende med ELOHVAC. Virksomheden er ophørt.')]:m.bullet(a,b,after=15,line=245)
m.page_break();m.section('ERHVERVSERFARING — FORTSAT')
m.job('Senior idriftsættelsesingeniør / projektleder, elsystem','Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024')
for a,b in [('Projektgrundlag','Koordinerede 37 samtidige CAPEX-projekter og 25 specialister på tværs af engineering, indkøb og anlæg.'),('Styring og dokumentation','Opfølgning på økonomi, fremdrift, ressourcer og risici; FAT/SAT og IQ/OQ/PQ i reguleret miljø med nul kritiske afvigelser ved aflevering.'),('El og rapportering','Arbejdede med tavler, styring og UPS samt månedsrapportering til ledelse og bygherre; SAP ERP til økonomi og omkostninger.')]:m.bullet(a,b,after=18,line=245)
m.job('Projekt- og værkstedsleder','Ventek-Air · København · jan. 2022–nov. 2022')
for a,b in [('Projektstyring','Ledede et team på 14 og styrede 11 samtidige anlægsprojekter fra specifikation til aflevering.'),('Aftaler og kvalitet','Tilbud, aftalegrundlag, underentreprenører, sikkerhedsdokumentation og afleveringspakker; tavlemøder og flaskehalsanalyse.')]:m.bullet(a,b,after=18,line=245)
m.job('Vedligeholdelses- og driftsleder / værkstedstekniker','BIOFOS, Lynetten · København · aug. 2017–jan. 2022')
for a,b in [('Teknisk drift','Kritisk el- og mekanisk drift: pumper, HVAC, højspændingstavler og SCADA; forebyggende vedligehold og akut fejlfinding.'),('Sikkerhed og forbedring','LOTO, risikovurdering og APV i skifteholdsdrift; reservedelsflow, 5S og PDCA i værksted og lager.')]:m.bullet(a,b,after=18,line=245)
m.job('Elektromekaniker / produktionsteamleder','ARJ Engineering · Teheran · dec. 2003–mar. 2010')
m.bullet('Anlæg og team','Ledede 12 mekanikere og teknikere med vagtplanlægning og materialestyring; fejldiagnose og reparation af industrielle el- og mekaniske anlæg.',after=20,line=245)
m.section('UDDANNELSE OG CERTIFICERING')
for a,b in [('B.Tech, Technology Management and Mechanical Engineering','Copenhagen School of Marine Engineering & Technology Management · 2017–2022'),('Elautoriseret maskinmester, LV/MV/HV','Sikkerhedsstyrelsen · 2023'),('PRINCE2 certificeret projektleder','AXELOS / PeopleCert'),('Køleteknik og klimaanlæg','Mercantec AMU · 2021'),('El- og maskinteknisk design, elteknik','Tehran Technical University · 2000–2003'),('HF matematik/fysik','VUC · 2012–2017')]:m.edu(a,b)
m.section('METODER, VÆRKTØJER OG SPROG')
m.para('**Beregning og dokumentation:** Excel, SAP ERP, Python, AI-værktøjer, digitale tjeklister og investeringsmodeller. **Metoder:** PRINCE2, Lean og Six Sigma anvendt i praksis; kun PRINCE2 er certificeret. **Sprog:** dansk, engelsk og persisk. **Kørekort:** B.',after=15,line=250,justify=False)
m.save(str(R/'Shahram_Ajloo_KK_Varmeforsyning_MasterCV.docx'))
