"""DTE maskinmester i Ribe: opgavefokuseret ansøgning og CV."""
import os
from master_design import MasterDoc
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME='SHAHRAM AJLOO'
TITLE='Elautoriseret maskinmester | El-teknik, drift og energi'
CONTACT='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'

def build(path):
 m=MasterDoc(os.path.join(ROOT,'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='da-DK')
 m.header_banner(NAME,TITLE,CONTACT)
 m.meta('Actief Hartmanns · DTE, Dansk Træemballage A/S · Ribe')
 p=m._p(spacing_after=90,line=260,justify=False);m._run(p,'Ansøgning: Maskinmester til drift, el-teknik og energi',bold=True,color='1A1A1A')
 for text in [
 'På savværket i Ribe hænger driftssikkerhed, energiforbrug og sikkerhed tæt sammen. Råtræ skal blive til trækomponenter, mens restmaterialer indgår i træpilleproduktionen. Et stop eller en ændring ét sted kan påvirke flere led. Opgaven er derfor at skabe et teknisk beslutningsgrundlag, som gør det muligt at forbedre anlæggene uden at kompromittere sikkerhed eller produktion.',
 'Første prioritet er et fælles billede af tilstanden på virksomhedens produktionsanlæg sammen med produktion og tekniske kolleger: gentagne stop, kritiske komponenter, kendte fejl og afhængigheder registreres, og forebyggende vedligehold planlægges efter risiko og tilgængelige produktionsvinduer. Fejlfinding afsluttes med rodårsag, handling og kontrol af, om fejlen faktisk er fjernet. Reservedele prioriteres efter leveringsrisiko og konsekvens ved nedbrud.',
 'Energiledelse skal omsætte data til beslutninger. Kortlæg væsentlige energianvendelser, målepunkter og datakvalitet; fastlæg en relevant baseline og nøgletal, der tager højde for produktion og andre væsentlige forhold. Muligheder vurderes på besparelse, investering, driftskonsekvens og tilbagebetaling. Resultatet måles efter gennemførelse og indgår i ISO 50001-arbejdets PDCA-cyklus samt i et dokumenterbart grundlag for klimaregnskab og myndighedsrapportering.',
 'For el-tekniske projekter skal krav, risikovurdering, ansvarsfordeling, test og dokumentation være aftalt før implementering. KLS holdes aktuelt med kontroller, afvigelser og opfølgning; audits planlægges, så fund får en ansvarlig og en frist. Ved CE-mærkning og inkorporeringserklæringer afklares maskinens grænser og aktørernes ansvar med kompetente specialister, før dokumentationen færdiggøres.',
 'Ændringer i sikkerheds-PLC’er kræver særskilt kontrol: verificér eksisterende sikkerhedsfunktioner og dokumentation, vurder ændringens risiko og lad kvalificerede specialister gennemføre og validere ændringen, før anlægget frigives. Tilsvarende skal krav til kedelanlæg og tekniske installationer løbende identificeres og følges op. Lærlingenes opgaver planlægges med tydelig instruktion og faglig feedback. En kort, fast opfølgning med fabrikschef og produktion samler risici, energitiltag og beslutninger, så korte beslutningsveje bliver til holdbare forbedringer.'
 ]:m.para(text,after=65)
 m.meta('Med venlig hilsen',after=10);m.meta('Shahram Ajloo',after=0)
 m.page_break();m.resume_header(NAME,TITLE,CONTACT,'PROFIL')
 m.para('Elautoriseret maskinmester med erfaring fra teknisk drift, el-anlæg og projektledelse. Arbejder med fejlfinding, forebyggende vedligehold, anlægsprojekter og dokumentation i samarbejde med drift, specialister og kunder. Har gennemført et PDCA-program, der reducerede energiomkostninger med 40 % hos Novo Nordisk.',after=70)
 m.section('KOMPETENCER TIL DTE’S ANLÆG OG ENERGIARBEJDE')
 for a,b in [
 ('El-teknik og anlæg','ELOHVAC: installation, tavler, styring, fejlfinding og vedligehold. Novo Nordisk: el-tekniske anlæg, FAT/SAT og kvalificeret aflevering.'),
 ('Drift og reservedele','Biofos: kritisk el- og mekanisk drift, pumper, HVAC, højspændingstavler og SCADA; forebyggende vedligehold og reservedelsflow i døgnbemandet drift.'),
 ('Energi og forbedring','Novo Nordisk: 40 % reduktion af energiomkostninger via PDCA. Analyse og opfølgning i tekniske projekter; erfaring med ISO 50001 er ikke dokumenteret.'),
 ('Projekter og samarbejde','Novo: koordination af 25 specialister og 37 samtidige CAPEX-projekter; risici, ressourcer, økonomi og rapportering. PRINCE2-certificeret projektleder.'),
 ('Lærlinge og kvalitet','ELOHVAC: daglig ledelse af 5 elektrikere og 3 lærlinge, struktureret oplæring, KS og afleveringsdokumentation.'),
 ('Data og digitale værktøjer','SAP ERP; Python og Claude til tidsplaner, KS og KPI. Investeringsmodeller med NPV, IRR og scenarier til udvikling og nye idéer.')]:m.bullet(a,b,after=20)
 m.section('FAGLIGE AFKLARINGER')
 m.para('Praktisk erfaring med programmering og vedligeholdelse af PLC og sikkerheds-PLC, KLS, ISO 50001, CE-mærkning, inkorporeringserklæringer, energimyndighedsrapportering og kedellovgivning er ikke dokumenteret i det foreliggende CV. Teknisk styring, SCADA, dokumentation og energioptimering er nærliggende erfaring, men ikke det samme; ansvar og nødvendig oplæring afklares med DTE.',after=60)
 m.page_break();m.section('ERHVERVSERFARING')
 jobs=[
 ('Indehaver / teknisk direktør / elautoriseret maskinmester','ELOHVAC ApS · København · maj 2023–nu','5 elektrikere og 3 lærlinge · fuldt P&L-ansvar',[
 ('El og vedligehold','Installation, tavler, styring, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg.'),
 ('Projekter og mennesker','Tilbud, materialestyring, underentreprenører, KS, dokumentation og aflevering; daglig planlægning og oplæring af lærlinge. LOTO og risikovurdering.'),
 ('Digital forbedring','Python/Claude-værktøjer til tilbud, tidsplaner, KS og KPI; dokumenteret produktivitetsløft over 40 %.')]),
 ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen','Data Power Consultant ApS · København · 2024–2026 · sideløbende med ELOHVAC','4–10 personer',[
 ('Industrielle applikationer','Kravafdækning, integration, idriftsættelse og dokumenteret overdragelse af tekniske løsninger. Aktiv AI- og Claude-koder med faglig kontrol af output.')]),
 ('Senior idriftsættelsesingeniør / projektleder, elsystem','Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024','37 samtidige CAPEX-projekter · 25 specialister · 2–10 mio. kr. pr. projekt',[
 ('El-projekter','Fremdrift, økonomi og risiko på tværs af engineering, indkøb og anlæg; tavler, styring, UPS og sikkerhedsbelysning.'),
 ('Energi og test','40 % lavere energiomkostninger via PDCA; FAT/SAT og IQ/OQ/PQ uden kritiske afvigelser ved aflevering. SAP til økonomi og aktiver.')]),
 ('Projekt- og værkstedsleder','Ventek-Air · København · jan. 2022–nov. 2022','14 medarbejdere · 11 samtidige projekter',[
 ('Fra specifikation til aflevering','Kapacitetsplanlægning, underentreprenører, sikkerhedsdokumentation og leverancer; daglige tavlemøder og flaskehalsanalyse.')]),
 ('Vedligeholdelses- og driftsleder / værkstedstekniker','Biofos, Lynetten · København · aug. 2017–jan. 2022','Kritisk drift · el- og mekaniske anlæg',[
 ('Vedligehold','Fejlfinding på pumper, HVAC, højspændingstavler og SCADA; 5S, Standard Work, PDCA og reservedelsflow. LOTO, APV og risikovurdering.')]),
 ('Elektromekaniker / produktionsteamleder','ARJ Engineering · Teheran · dec. 2003–mar. 2010','12 mekanikere og teknikere',[
 ('Industriel teknik','Fejldiagnose og reparation af el- og mekaniske anlæg; rodårsagsanalyse, materialestyring og teamledelse.')])]
 for title,meta,scope,bullets in jobs:
  m.job(title,meta,scope=scope)
  for a,b in bullets:m.bullet(a,b,after=15)
 m.section('UDDANNELSE OG CERTIFICERING')
 for a,b in [('B.Tech, Technology Management & Mechanical Engineering — maskinmesterretningen','Maskinmesterskolen København · 2017–2022 · EQF 6'),('El- og maskinteknisk design, elteknik','Tehran Technical University · 2000–2003 · EQF 6'),('Elautoriseret maskinmester','Sikkerhedsstyrelsen · LV/MV/HV · 2023'),('PRINCE2-certificeret projektleder','AXELOS / PeopleCert')]:m.edu(a,b)
 m.para('Dansk og persisk/farsi: modersmål · Engelsk: professionelt · Kørekort B · Bopæl i Måløv. Praktisk tilstedeværelse i Ribe og tiltrædelse aftales.',after=40)
 m.page_break();m.models_table('PRAKTISK OPSTART — FORSLAG TIL DE FØRSTE 90 DAGE',('Tid','Prioritet og konkret leverance'),[
 ('Dag 1–30','Gå anlæg og el-dokumentation igennem med drift, sikkerhedsansvarlige og fabrikschef. Registrér kritiske stop, vedligeholdsbehov, reservedele, åbne KLS-afvigelser, auditplan og status for energimåling. Afklar kompetencer og ansvar for PLC og sikkerheds-PLC.'),
 ('Dag 31–60','Prioritér 1–2 mulige energitiltag med baseline, produktionsforudsætninger, økonomi og målemetode. Opdatér sammen med ansvarlige handlingslisten for lovkrav, kedelanlæg, el-installationer, rapportering og KLS. Udvælg vedligeholdsopgaver efter risiko.'),
 ('Dag 61–90','Fremlæg investerings- og beslutningsgrundlag for fabrikschefen, gennemfør godkendte tiltag og fastlæg måling af effekt. Test og frigivelse sker efter anlæggets procedurer og med de nødvendige kompetencer. Gennemgå lærlingeforløb, auditfund og næste udviklingsbehov.')])
 m.section('FRA TEKNISK IDÉ TIL SIKKER DRIFT')
 for a,b in [('Afgrænsning','Beskriv behov, driftsvindue, sikkerheds- og lovkrav samt forventet effekt med produktionen og relevante specialister.'),('Beslutning','Brug risikoanalyse og enkel businesscase: investering, forventet besparelse, usikkerhed og påvirkning af oppetid.'),('Gennemførelse','Aftal ansvar og test, sikr afbrydelse og LOTO, og involvér kompetente personer ved ændringer i maskinsikkerhed og sikkerheds-PLC.'),('Overdragelse','Kontrollér funktion, opdatér dokumentation og instruktioner, følg op på energidata og fejl samt luk afvigelser med ansvarlig og frist.')]:m.bullet(a,b,after=30)
 m.section('SIKKERHED OG KOMPETENCER')
 m.para('Opgaver inden for sikkerheds-PLC, CE-mærkning, KLS, ISO 50001 og rapportering forudsætter afklaring af eksisterende systemer, ansvar og kompetencer. Oplæring og kvalificeret specialiststøtte planlægges før selvstændige ændringer eller godkendelser.',after=50)
 return m.save(path,title='Ansøgning og CV — maskinmester, DTE Ribe',subject='El-teknik, drift og energi',keywords='maskinmester, energioptimering, drift, Ribe')
if __name__=='__main__':print(build(os.path.join(ROOT,'Shahram_Ajloo_DTE_Maskinmester_Ribe.docx')))
