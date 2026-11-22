"""Fyldig, jobrettet ansøgning og CV til Silvan Greve."""
from pathlib import Path
from master_design import MasterDoc
R=Path(__file__).resolve().parent.parent
N='SHAHRAM AJLOO';T='Varehuschef | Ledelse, kunder og drift'
C='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
def build(letter,filename):
 m=MasterDoc(str(R/'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='da-DK')
 if letter:
  m.header_banner(N,T,C);m.meta('Silvan · Varehuschef · Greve',after=30)
  m.para('**Ansøgning: Varehuschef i Silvan Greve**',after=70,justify=False)
  m.para('Kære Nicholas Dalgaard og ansættelsesteam',after=60,justify=False)
  m.para('Når en kunde kommer ind i Silvan med et projekt, er den gode oplevelse ikke bare at finde en vare. Det er at blive mødt af en medarbejder, der lytter, stiller spørgsmål og hjælper kunden videre. I Greve skal den oplevelse bygges på et team, der kender sine mål, trives i hverdagen og har tid og rammer til at hjælpe.',after=55,line=245,justify=False)
  m.para('Som varehuschef vil jeg samle medarbejderne om fire praktiske opgaver:',after=45,line=240,justify=False)
  for a,b in [
   ('Gør mål til handling','Omsæt Silvans strategi og varehusets KPI’er til få tydelige prioriteter for ugen. Følg op med medarbejderne på resultater, bemanding, varetilgængelighed og kundeoplevelser. Når et mål halter, skal teamet kende årsagen og aftale, hvem der gør hvad.'),
   ('Udvikl mennesker, ikke kun planer','Vær til stede på gulvet, giv løbende feedback og hold individuelle samtaler om trivsel, styrker og udviklingsønsker. Fordel ansvar efter kompetencer, giv nye kolleger en god oplæring, og skab plads til, at medarbejdere med potentiale kan tage næste skridt.'),
   ('Hjælp kunden helt videre','Skab en salgsklar butik, hvor medarbejderne kan finde varerne og give relevant vejledning. Lyt til både gør-det-selv-kundens projekt og håndværkerens behov. Følg op på spørgsmål og reklamationer, og brug kundernes tilbagemeldinger til at forbedre servicen.'),
   ('Skab en hverdag, der hænger sammen','Planlæg bemanding og opgaver efter varehusets behov, følg op på sikkerhed og sørg for klar kommunikation mellem medarbejdere og ledelse. Arbejd med lager og vareflow sammen med holdet, og brug Silvans koncepter som fælles ramme for prioriteringerne.')]:m.bullet(a,b,after=25,line=240)
  m.para('Min baggrund er teknisk service, drifts- og personaleledelse frem for en traditionel detailkarriere. I ELOHVAC har jeg ansvar for økonomi, kunder og leverancer samt ledelse af fem elektrikere og tre lærlinge. Hos Ventek-Air ledede jeg 14 medarbejdere og 11 samtidige projekter. Jeg har også arbejdet med at opbygge eller skalere kundeservice og teknisk support på tværs af kanaler.',after=55,line=245,justify=False)
  m.para('Silvans mål om at sikre kundernes succes med boligens projekter taler direkte til min erfaring med at omsætte praktiske behov til løsninger. Jeg vil gerne drøfte, hvordan jeg sammen med medarbejderne kan udvikle resultaterne og kundeoplevelsen i Greve.',after=40,line=245,justify=False)
  m.meta('Med venlig hilsen · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com',after=0)
  m.page_break()
 m.resume_header(N,T,C,'LEDERPROFIL OG MOTIVATION')
 m.meta('Silvan · Varehuschef · Greve',after=30)
 m.para('**Motivation:** Et velfungerende varehus skabes af medarbejdere, der ved, hvad de skal lykkes med, og som har lyst og mulighed for at hjælpe kunderne. Jeg søger rollen i Silvan Greve for at bruge min erfaring med personaleledelse, kundeservice, økonomi og praktisk drift til at skabe en hverdag med god rådgivning, tydelige mål og et stærkt samarbejde. I detail hænger kundetilfredshed og fastholdelse sammen med, at Silvans strategi bliver omsat til klare prioriteringer og en god hverdag for medarbejderne.',after=60,line=245,justify=False)
 m.para('Drifts- og personaleleder med fuldt resultatansvar i egen teknisk servicevirksomhed, erfaring med udvikling af medarbejdere og ledere, kunde- og leverandørkontakt samt planlægning af ressourcer og leverancer. Baggrunden er teknisk service og drift snarere end traditionel detailledelse; produkt- og kundekendskab fra bygge- og installationsområdet kan bruges sammen med Silvans oplæring i varehusets koncepter.',after=55,line=245,justify=False)
 m.section('LEDERKOMPETENCER TIL VAREHUSET I GREVE')
 for a,b in [
  ('Personaleledelse og trivsel','Daglig ledelse af fem elektrikere og tre lærlinge i ELOHVAC, tidligere 14 medarbejdere i Ventek-Air og 12 mekanikere og teknikere hos ARJ. Erfaring med 1:1, MUS, oplæring, feedback og udvikling af medarbejdere.'),
  ('Ledelse gennem andre','Har haft direkte personaleansvar for teamledere eller mellemledere, som selv ledede medarbejdere. Arbejder med tydelige forventninger, delegering, løbende sparring og opfølgning.'),
  ('Kundeoplevelse og service','Kundedialog, tilbud og leverancer i teknisk service. Erfaring med opbygning eller skalering af kundeservice og teknisk support på tværs af kanaler samt håndtering af reklamationer og garantisager.'),
  ('Økonomi og resultater','Fuldt P&L-ansvar i ELOHVAC, herunder tilbud, omkostninger, materialer og underentreprenører. Erfaring med forecast og kontraktopfølgning i drifts- eller serviceleverancer.'),
  ('Daglig drift og vareflow','Planlægning af kapacitet, mennesker, materialer og leverancer; lager- og reservedelsflow fra BIOFOS. I Ventek-Air blev tavlemøder, flaskehalsanalyse og standardiserede arbejdsgange brugt til at styrke leveringen.'),
  ('Forandring og forbedring','Praktisk anvendelse af Lean, Six Sigma og PDCA; AI-assisterede planlægnings- og kvalitetstjekværktøjer bidrog til over 40 % produktivitetsforbedring i ELOHVAC.')]:m.bullet(a,b,after=20,line=240)
 m.section('LEDELSESVÆRKTØJER OG PRAKTISKE METODER')
 m.para('**Mennesker:** situationsbestemt ledelse, 1:1/MUS, coaching, GROW, SBI, kompetencekortlægning og delegering. **Drift:** tavlemøder, visuel ledelse, KPI-opfølgning, RACI, interessentstyring, kapacitetsplanlægning og 30-60-90-dages plan. **Forbedring:** 5S, Kaizen, PDCA, A3, VSM, 5 x hvorfor og standardarbejde. PRINCE2-certificeret; Lean og Six Sigma anvendt i praksis.',after=20,line=240,justify=False)
 m.page_break();m.section('ERHVERVSERFARING — LEDELSE, KUNDER OG FORRETNING')
 m.job('Indehaver / teknisk direktør / elautoriseret maskinmester','ELOHVAC ApS · København · maj 2023–nu')
 for a,b in [
  ('Ledelse og oplæring','Personaleansvar for fem elektrikere og tre lærlinge. Daglig planlægning, 1:1 og MUS, oplæring, arbejdsmiljø og opfølgning på opgaver og trivsel.'),
  ('Kunder og økonomi','Fuldt P&L-ansvar; kundedialog, tilbud, beregning, materialer, underentreprenører, kvalitet og aflevering. Finder løsninger på tekniske opgaver og følger leverancer til dørs.'),
  ('Ressourcer og forbedringer','Udvikler AI-assisterede værktøjer til tilbud, tidsplaner, kvalitetstjek og KPI-overblik. Værktøjerne har bidraget til en produktivitetsforbedring på over 40 %.'),
  ('Sikkerhed','Risikovurdering, LOTO og arbejdsmiljøopfølgning på skiftende arbejdssteder.')]:m.bullet(a,b,after=20,line=240)
 m.job('Medejer og CTO / ansvarlig for AI- og AI coding-afdelingen','Data Power Consultant ApS · København · 2024–nov. 2026')
 for a,b in [
  ('Ledelse og prioritering','Ansvarlig for AI-afdeling med 4–10 personer. Sideløbende med ELOHVAC blev tid, opgaver og leverancer prioriteret i en fælles plan.'),
  ('Kundeløsninger og kvalitet','Tekniske og industrielle applikationer fra kravafdækning og integration til dokumentation og overdragelse. Arbejdede med AI-kodning, LLM-API’er og AI-agenter samt faglig kontrol af output.'),
  ('AI i ledelsesarbejdet','AI-assisteret rapportering, beslutningsoplæg, KPI-analyse og design af tekniske anlæg og komponenter. Virksomheden er ophørt.')]:m.bullet(a,b,after=20,line=240)
 m.job('Senior idriftsættelsesingeniør / projektleder, elsystemer','Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024')
 for a,b in [('Tværfaglig styring','Koordinerede 25 specialister på 37 samtidige CAPEX-projekter med opfølgning på økonomi, fremdrift, ressourcer og risiko.'),('Kvalitet og forbedring','FAT/SAT og IQ/OQ/PQ i reguleret miljø; nul kritiske afvigelser ved aflevering. Et PDCA-program reducerede energiomkostningerne med 40 %.')]:m.bullet(a,b,after=20,line=240)
 m.job('Projekt- og værkstedsleder','Ventek-Air · København · jan. 2022–nov. 2022')
 m.bullet('Mennesker og leverancer','Ledte 14 medarbejdere og 11 samtidige projekter; kapacitetsplanlægning, underentreprenører, daglige tavlemøder, sikkerhedsdokumentation og formel aflevering.',after=20,line=240)
 m.page_break();m.section('ERHVERVSERFARING — DRIFT OG PRODUKTER')
 m.job('Vedligeholdelses- og driftsleder / værkstedstekniker','BIOFOS, Lynetten · København · aug. 2017–jan. 2022')
 for a,b in [('Drift og service','El- og mekanisk drift med pumper, ventilation, højspændingstavler og SCADA; forebyggende vedligehold og akut fejlfinding i 24/7-drift.'),('Flow og forbedring','Reservedelsflow og lagerstyring samt 5S, standardarbejde og PDCA på værksted og lager. Sikkerhedsarbejde med LOTO og risikovurdering.')]:m.bullet(a,b,after=20,line=240)
 m.job('Elektromekaniker / produktionsteamleder','ARJ Engineering · Teheran · dec. 2003–mar. 2010')
 for a,b in [('Personale og drift','Ledte 12 mekanikere og teknikere med ansvar for planlægning, materialer, målstyring og teknisk problemløsning.'),('Produkt og forretning','Produktporteføljeansvar for en linje med elektromotorer og pumper, herunder roadmap, business cases, udvikling og lancering samt pris-, margin- og investeringsbeslutninger.')]:m.bullet(a,b,after=20,line=240)
 m.section('UDDANNELSE, KVALIFIKATIONER OG SPROG')
 for a,b in [('B.Tech, teknologiledelse og maskinteknik','Københavns Maskinmesterskole · 2017–2022'),('El- og maskinteknisk design, elteknik','Tehran Technical University · 2000–2003'),('Elautoriseret maskinmester, LV/MV/HV','Sikkerhedsstyrelsen · 2023'),('PRINCE2-certificeret projektleder','AXELOS / PeopleCert'),('Køleteknik og klimaanlæg','Mercantec · AMU · 2021'),('HF, matematik og fysik','VUC · 2012–2017'),('STCW-sikkerheds- og maskinrelaterede kurser','Søfartsstyrelsen · 2021–2023')]:m.edu(a,b)
 m.para('**Metoder:** Lean og Six Sigma i praksis; PRINCE2-certificeret. **Digitale værktøjer:** Excel, SAP ERP, Power BI, AI-assisteret planlægning og rapportering. **Sprog:** Dansk og persisk (modersmål), engelsk på professionelt niveau. **Kørekort:** B. **Bopæl:** Måløv.',after=35,line=240,justify=False)
 m.models_table('SILVAN GREVE — FORSLAG TIL DE FØRSTE 90 DAGE',('Periode','Fokus sammen med medarbejdere og ledelse'),[
  ('Dag 1–30','Lær medarbejderne, varehuset og Silvans koncepter at kende. Gennemgå mål, KPI’er, kundetilbagemeldinger, bemanding og vareflow; aftal de vigtigste prioriteringer med teamet og regionsledelsen.'),
  ('Dag 30–60','Hold udviklings- og trivselssamtaler, følg op på oplæring og afprøv konkrete forbedringer i kundeoplevelse eller daglige rutiner. Fordel ansvar og aftal, hvordan effekten følges.'),
  ('Dag 60–90','Gennemgå resultater og medarbejdernes erfaringer med ledelsen. Justér bemanding og indsatsområder efter varehusets behov, og forankr de arbejdsgange, der fungerer.')])
 m.save(str(R/filename))
build(True,'Shahram_Ajloo_Silvan_Varehuschef_Greve.docx')
build(False,'Shahram_Ajloo_Silvan_Varehuschef_Greve_CV.docx')
