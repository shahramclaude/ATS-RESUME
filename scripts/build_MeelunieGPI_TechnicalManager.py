"""MeelunieGPI Technical Manager: ansøgning og CV."""
import os
from master_design import MasterDoc
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME='SHAHRAM AJLOO'
TITLE='Elautoriseret maskinmester | Teknisk drift, vedligehold og projekter'
CONTACT='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'

def build(path):
 m=MasterDoc(os.path.join(ROOT,'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='da-DK')
 m.header_banner(NAME,TITLE,CONTACT);m.meta('Hansentoft · MeelunieGPI · Hedensted · Att.: Casper Olesen')
 p=m._p(spacing_after=80,line=260,justify=False);m._run(p,'Technical Manager — fra commissioning til stabil og skalerbar drift',bold=True,color='1A1A1A')
 for text in [
 'Når et nyt anlæg til hestebønnebaserede ingredienser skal skaleres, er den tekniske opgave mere end at holde maskinerne i gang. Viden fra commissioning og eksterne specialister skal omsættes til en vedligeholdelsesorganisation, der kan sikre oppetid, fødevaresikkerhed og ensartet kapacitet. Det kræver en nærværende teknisk leder, klare prioriteringer og et beslutningsgrundlag, som også kan bruges i ledergruppen.',
 'Start med en fælles gennemgang på anlægget med produktion, kvalitet og de leverandører, der kender udstyret. Registrér udstyr, sikkerheds- og kvalitetskritiske funktioner, åbne commissioning-punkter, gentagne stop og manglende dokumentation. En kritikalitetsvurdering skal afgøre, hvad der vedligeholdes først; et vedligeholdsårshjul bygger på leverandørernes intervaller og faktiske driftsdata og justeres, efterhånden som fejlmønstret bliver kendt.',
 'Eksterne ressourcers viden skal overdrages systematisk: navngiv en intern ejer for hvert anlægsområde, aftal instruktion, dokumentation og praktisk sidemandsoplæring, og følg kompetencerne i en enkel matrix. Det fremtidige team opbygges efter dokumenterede behov inden for el, mekanik og proces. En fast tavlegennemgang med produktionen afklarer prioritet, stopvinduer og opfølgning, mens teknisk ledelse er synlig i hverdagen — omtrent 60 % tæt på driften og 40 % til planlægning og udvikling som foreslået i opslaget.',
 'Reservedelslageret organiseres efter kritikalitet, leveringstid og forbrug med tydelige minimumsniveauer og ansvar. Tegninger, manualer, servicehistorik og arbejdsordrer kobles til aktiverne i det vedligeholdelsessystem, der anvendes lokalt (IPV). Et ryddeligt værksted og 5S gør det lettere at finde dele, udføre arbejdet sikkert og registrere det, der er gjort.',
 'Tekniske beslutninger kræver sammenhæng mellem oppetid, kapacitet og økonomi. Etabler et begrænset sæt KPI’er, herunder uplanlagte stop og gennemført forebyggende vedligehold; afklar definitioner og datakvalitet, før mål fastsættes. OPEX og CAPEX prioriteres efter sikkerhed, fødevarekvalitet, risiko og samlet effekt. For ombygninger og optimeringer aftales scope, businesscase, test og overdragelse; eksterne el-, mekanik- og procesleverancer følges op på kvalitet, fremdrift og dokumentation. Ændringer koordineres med produktion og kvalitet, så anlægget ikke frigives uden de nødvendige kontroller.'
 ]:m.para(text,after=70)
 m.meta('Med venlig hilsen',after=10);m.meta('Shahram Ajloo',after=0)
 m.page_break();m.resume_header(NAME,TITLE,CONTACT,'PROFIL')
 m.para('Elautoriseret maskinmester med erfaring i teknisk drift, vedligehold, idriftsættelse og ledelse af tekniske teams. Kombinerer praktisk fejlfinding og reservedelsflow med projektstyring, leverandørkoordinering og dokumenteret forbedringsarbejde. Erfaringen er fra industri, spildevandsdrift, tekniske installationer og reguleret lægemiddelproduktion; solid erfaring fra fødevareproduktion er ikke dokumenteret.',after=70)
 m.section('DOKUMENTERET BIDRAG TIL TEKNISK DRIFT')
 for a,b in [
 ('Drift og vedligehold','Biofos Lynetten: forebyggende vedligehold og akut fejlfinding på pumper, HVAC, højspændingstavler og SCADA i 24/7-drift. 5S, Standard Work og reservedelsflow på værksted og lager.'),
 ('Projekt til overdragelse','Novo Nordisk: 37 samtidige CAPEX-projekter, 25 specialister og opfølgning på risiko, ressourcer, økonomi og fremdrift. FAT/SAT og IQ/OQ/PQ uden kritiske afvigelser ved aflevering.'),
 ('Teknisk ledelse','ELOHVAC: 5 elektrikere og 3 lærlinge, fuldt P&L-ansvar, kvalitet, underentreprenører og dokumentation. Ventek-Air: ledelse af 14 medarbejdere og 11 projekter med daglige tavlemøder.'),
 ('Forbedring og energi','PDCA-program hos Novo reducerede energiomkostninger med 40 %. A3, 5xHvorfor og Ishikawa til fejlanalyse. Lean- og Six Sigma-metoder anvendt i praksis, ikke certificeret.'),
 ('Data og investering','SAP ERP til økonomi og aktiver; aktiv Python-/Claude-koder med egne løsninger til KPI og planlægning. Bygger investeringsmodeller med NPV, IRR og scenarier.')]:m.bullet(a,b,after=25)
 m.section('FAGLIGE AFKLARINGER')
 m.para('Solid erfaring med fødevareproduktion, fødevareteknisk udstyr og fødevaresikkerhed er ikke dokumenteret. Lægemiddelproduktion hos Novo er en anden reguleret branche og må ikke sidestilles med fødevareproduktion. Erfaring med vedligeholdelsessystemet IPV og ledelse af en samlet teknisk fødevareafdeling er heller ikke dokumenteret; oplæring og samarbejde med relevante fødevare- og processpecialister vil være nødvendigt.',after=60)
 m.page_break();m.section('ERHVERVSERFARING')
 jobs=[
 ('Indehaver / teknisk direktør / elautoriseret maskinmester','ELOHVAC ApS · København · maj 2023–nu','5 elektrikere og 3 lærlinge · fuldt P&L-ansvar',[
 ('Teknisk drift','Installation, tavler, styring, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg.'),
 ('Ledelse og leverancer','Planlægning, materialer, underentreprenører, KS, aflevering, 1:1 og oplæring. LOTO, APV og risikovurdering.'),
 ('Digitale værktøjer','Python/Claude API til tilbud, tidsplaner, KS og KPI; dokumenteret produktivitetsløft over 40 %.')]),
 ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen','Data Power Consultant ApS · København · 2024–2026 · sideløbende med ELOHVAC','4–10 personer',[
 ('Tekniske applikationer','Ledte tekniske og industrielle løsninger fra kravafdækning og integration til idriftsættelse, dokumentation og overdragelse.')]),
 ('Senior idriftsættelsesingeniør / projektleder, elsystem','Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024','37 samtidige CAPEX-projekter · 25 specialister · 2–10 mio. kr. pr. projekt',[
 ('Anlægsprojekter','Tværfaglig koordinering, økonomi, risici og ressourcer på tværs af engineering, indkøb og anlæg; el-tavler og styring.'),
 ('Energi og aflevering','PDCA-program med 40 % reduktion af energiomkostninger. FAT/SAT, IQ/OQ/PQ og GMP-dokumentation; SAP ERP til økonomi og aktiver.')]),
 ('Projekt- og værkstedsleder','Ventek-Air · København · jan. 2022–nov. 2022','14 medarbejdere · 11 samtidige projekter',[
 ('Kapacitet og fremdrift','Styring fra specifikation til aflevering, underentreprenører og dokumentation; tavlemøder og flaskehalsanalyser.')]),
 ('Vedligeholdelses- og driftsleder / værkstedstekniker','Biofos, Lynetten · København · aug. 2017–jan. 2022','24/7-drift · el- og mekaniske anlæg',[
 ('Oppetid','Fejlfinding og forebyggende vedligehold på pumper, HVAC, højspændingstavler og SCADA; værkstedsstandarder og reservedelsflow.')]),
 ('Elektromekaniker / produktionsteamleder','ARJ Engineering · Teheran · dec. 2003–mar. 2010','12 mekanikere og teknikere',[
 ('Industriel teknik','Fejldiagnose og reparation på el- og mekaniske anlæg, rodårsagsanalyse, materialestyring og teamledelse.')])]
 for title,meta,scope,bullets in jobs:
  m.job(title,meta,scope=scope)
  for a,b in bullets:m.bullet(a,b,after=15)
 m.section('UDDANNELSE OG CERTIFICERING')
 for a,b in [('B.Tech, Technology Management & Mechanical Engineering — maskinmesterretningen','Maskinmesterskolen København · 2017–2022 · EQF 6'),('El- og maskinteknisk design, elteknik','Tehran Technical University · 2000–2003 · EQF 6'),('Elautoriseret maskinmester','Sikkerhedsstyrelsen · LV/MV/HV · 2023'),('PRINCE2-certificeret projektleder','AXELOS / PeopleCert')]:m.edu(a,b)
 m.para('Dansk og persisk/farsi: modersmål · Engelsk: professionelt · Kørekort B · Bopæl i Måløv. Fremmøde i Hedensted og tiltrædelse aftales.',after=40)
 m.page_break();m.models_table('OPSTARTSPLAN — FORSLAG TIL DE FØRSTE 90 DAGE',('Tid','Handling og beslutningsgrundlag'),[
 ('Dag 1–30','Gennemgå anlægget med drift, kvalitet og leverandører. Registrér aktiver, åbne commissioning-punkter, kendte stop, risici, dokumentation og eksisterende vedligeholdsdata. Afklar hygiejnekrav og kompetencebehov med fødevarespecialister.'),
 ('Dag 31–60','Klassificér kritiske aktiver og reservedele; opret første vedligeholdsårshjul ud fra leverandørkrav og driftsdata. Afklar, hvordan udstyr, arbejdsordrer og historik registreres i IPV. Etablér ugentlig prioritering med produktion og kvalitet.'),
 ('Dag 61–90','Fremlæg forslag til team, ekstern støtte, OPEX og CAPEX for Site Director. Følg op på stop, vedligehold og forbedringer; revidér intervaller ud fra erfaring. Aftal ejerskab for dokumentation og målrettet videnoverdragelse fra leverandører.')])
 m.section('STYRING AF ET TEKNISK SETUP I OPBYGNING')
 for a,b in [
 ('Mennesker og viden','Gemba i produktionen, tavlemøder og 1:1 skaber dialog om problemer, oplæring og ejerskab. En kompetencematrix synliggør, hvor ekstern ekspertise fortsat er nødvendig.'),
 ('Vedligehold og reservedele','Prioritér efter sikkerhed, fødevarekvalitet, konsekvens for oppetid og leveringstid. Brug 5S og Standard Work i værksted og lager; justér planer, når driftsdata giver bedre grundlag.'),
 ('Økonomi og projekter','Saml projekter og forbedringer i én prioriteret portefølje. PRINCE2-inspirerede beslutningspunkter, risiko og businesscase giver Site Director og ledergruppen et klart valg mellem investering, kapacitet og driftsrisiko.'),
 ('Læring og sikker overdragelse','Brug PDCA og rodårsagsanalyse på gentagne stop. Dokumentér ændringer, aftal test med relevante specialister og koordinér frigivelse med produktion og kvalitet efter lokale fødevaresikkerhedsprocedurer.')]:m.bullet(a,b,after=30)
 m.section('FORUDSÆTNINGER')
 m.para('Planen er et forslag, ikke en beskrivelse af MeelunieGPI’s nuværende systemer. Fødevaretekniske forhold, IPV, virksomhedens procedurer og den enkelte persons kompetencer skal afklares, før ansvar og ændringer fordeles.',after=50)
 return m.save(path,title='Ansøgning og CV — Technical Manager, MeelunieGPI',subject='Teknisk drift og vedligehold',keywords='Technical Manager, vedligehold, CAPEX, Hedensted')
if __name__=='__main__':print(build(os.path.join(ROOT,'Shahram_Ajloo_MeelunieGPI_TechnicalManager.docx')))
