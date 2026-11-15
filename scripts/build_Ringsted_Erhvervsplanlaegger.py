"""Ringsted Kommune: ansøgning og CV til erhvervsplanlægning."""
import os
from master_design import MasterDoc
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME='SHAHRAM AJLOO'
TITLE='Teknisk projektstyring | Tværfaglig koordinering og realisering'
CONTACT='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'

def build(path):
 m=MasterDoc(os.path.join(ROOT,'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='da-DK')
 m.header_banner(NAME,TITLE,CONTACT);m.meta('Ringsted Kommune · Plan, Byg og Land · Att.: Kristian Lønborg')
 p=m._p(spacing_after=80,line=260,justify=False);m._run(p,'Ansøgning: Udvikling og planlægning af erhvervsområder',bold=True,color='1A1A1A')
 m.para('En virksomhed kan have en god idé til en placering, men området bliver først brugbart, når adgang, forsyning og de planmæssige og miljømæssige hensyn kan hænge sammen. For Ringsted handler erhvervsudvikling derfor om både at skabe plads til vækst og at få afklaret de forhold, der afgør, om en plan kan gennemføres.',after=80)
 m.para('Jeg vil begynde med at skabe et fælles overblik over projektets ønsker, plangrundlag, berørte parter og nødvendige afklaringer. Sammen med kommunens planfaglige medarbejdere vil jeg samle spørgsmål om støj, natur, trafik, miljø, byggeri og forsyning i en tidsplan med ansvarlige og beslutningspunkter. Det skal være tydeligt, hvad der er afklaret, og hvad der stadig kræver en faglig eller politisk beslutning.',after=80)
 m.para('I dialogen med virksomheder, grundejere og rådgivere er det vigtigt at forklare både muligheder og begrænsninger uden at love et udfald på forhånd. Høringssvar og forskellige interesser skal samles og behandles efter kommunens procedurer. Et beslutningsoplæg bør gøre alternativer, konsekvenser og åbne spørgsmål forståelige for ledelse og politikere, mens de planfaglige og juridiske vurderinger udarbejdes og kvalitetssikres af de ansvarlige specialister.',after=80)
 m.para('Min erfaring kan bidrage med overblik over tekniske afhængigheder og gennemførelse: Hos Novo Nordisk koordinerede jeg 25 specialister på 37 tekniske CAPEX-projekter med opfølgning på økonomi, risici og fremdrift. Hos Ventek-Air styrede jeg kapacitet og aflevering på 11 projekter. Hos ELOHVAC arbejder jeg med erhvervskunder, tilbud, underentreprenører og tekniske løsninger; arbejdet på Biofos har givet mig indsigt i drift af spildevandsanlæg.',after=80)
 m.para('Jeg er elautoriseret maskinmester og teknisk projektleder, men mit CV dokumenterer ikke den solide erfaring med lokalplaner, kommuneplantillæg og planmyndighedsarbejde, som stillingen kræver. Det er et væsentligt fagligt spring. Jeg vil gerne drøfte med dig, om mine tekniske og koordinerende erfaringer kan være relevante i en anden eller supplerende rolle i kommunens udviklingsarbejde.',after=80)
 m.para('Jeg ser frem til at høre mere om de aktuelle erhvervsprojekter og samarbejdet mellem planteamet, virksomhederne og de øvrige fagområder.',after=70)
 m.meta('Med venlig hilsen',after=15);m.meta('Shahram Ajloo',after=0)
 m.page_break();m.resume_header(NAME,TITLE,CONTACT,'PROFIL')
 m.para('Elautoriseret maskinmester og projektleder med erfaring i tekniske anlæg, drift og tværfaglig koordinering. Skaber overblik over ressourcer, afhængigheder og leverancer og omsætter tekniske forhold til aftaler med kunder, specialister og projektledelse. Erfaringen er fra tekniske projekter, ikke kommunal lokalplanlægning.',after=70)
 m.section('ERFARING MED RELEVANS FOR OPGAVEN')
 for a,b in [
 ('Tværfaglig fremdrift','Novo Nordisk: koordinerede 25 specialister på tværs af engineering, indkøb og anlæg på 37 samtidige CAPEX-projekter. Fulgte risici, ressourcer og økonomi og rapporterede til ledelse og bygherre.'),
 ('Fra behov til levering','Ventek-Air: kapacitetsstyring af 11 tekniske projekter fra specifikation til aflevering med 14 medarbejdere; daglige tavlemøder og flaskehalsanalyse understøttede fremdrift.'),
 ('Erhverv og samarbejde','ELOHVAC: ansvar for tilbud, økonomi, kunder, materialer, underentreprenører, kvalitet og aflevering af tekniske installationer. Fuldt P&L-ansvar.'),
 ('Forsyning og teknisk drift','Biofos, Lynetten: vedligehold og fejlfinding på pumper, HVAC, højspændingstavler og SCADA i et spildevandsanlæg; kendskab til driftsmæssige hensyn, ikke kommunal spildevandsmyndighed.'),
 ('Digitale beslutningsgrundlag','Aktiv professionel AI-/Claude-koder: Python/Claude-værktøjer til tidsplaner, kvalitet og KPI med over 40 % dokumenteret produktivitetsløft hos ELOHVAC. Udvikler investeringsmodeller med NPV, IRR og scenarier.')]:m.bullet(a,b,after=25)
 m.models_table('METODER TIL AT SKABE OVERBLIK',('Opgave','Dokumenteret erfaring og anvendelse'),[
 ('Styring og ansvar','PRINCE2-certificeret projektleder; opfølgning på risici, ressourcer og fremdrift hos Novo.'),
 ('Koordinering','Daglige tavlemøder og flaskehalsanalyse hos Ventek-Air; skriftlige prioriteringer ved sideløbende virksomheder.'),
 ('Samarbejde','1:1, situationsbestemt ledelse og oplæring hos ELOHVAC; tværfaglig koordinering hos Novo.'),
 ('Forbedringer','PDCA og A3 hos Novo; 5S og Standard Work på Biofos.')])
 m.section('FAGLIGT UDGANGSPUNKT')
 m.para('Kommunal planlægning, lokalplaner, miljøvurderinger, høringer og politisk sagsfremstilling er ikke dokumenteret i min erfaring. Relevante planfaglige og juridiske vurderinger kræver kvalificerede myndighedsmedarbejdere.',after=60)
 m.page_break();m.section('ERHVERVSERFARING')
 jobs=[
 ('Indehaver / teknisk direktør / elautoriseret maskinmester','ELOHVAC ApS · København · maj 2023–nu','5 elektrikere og 3 lærlinge · fuldt P&L-ansvar',[
 ('Kunder og projekter','Tilbud, planlægning, materialer, underentreprenører, kvalitet og aflevering af el-, ventilations- og klimaanlæg for erhvervskunder.'),
 ('Digital udvikling','Python/Claude API til tilbud, tidsplaner, KS og KPI; dokumenteret produktivitetsløft over 40 %.')]),
 ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen','Data Power Consultant ApS · København · 2024–nov. 2026 · sideløbende med ELOHVAC','4–10 personer · virksomheden ophørt november 2026',[
 ('Tekniske løsninger','Ledte industrielle applikationer fra kundebehov og arkitektur til integration, idriftsættelse, dokumentation og overdragelse.'),
 ('Beslutningsstøtte','Anvendte AI til rapportering og beslutningsoplæg og styrede prioriteringer på tværs af to sideløbende virksomheder.')]),
 ('Senior idriftsættelsesingeniør / projektleder, elsystem','Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024','37 samtidige CAPEX-projekter · 25 specialister · 2–10 mio. kr. pr. projekt',[
 ('Koordinering og kvalitet','Fulgte økonomi, risiko, ressourcer og fremdrift på tværs af engineering, indkøb og anlæg. FAT/SAT og IQ/OQ/PQ uden kritiske afvigelser ved aflevering.'),
 ('Forbedring','PDCA-program reducerede energiomkostninger med 40 %; SAP ERP til økonomi og aktiver.')]),
 ('Projekt- og værkstedsleder','Ventek-Air · København · jan. 2022–nov. 2022','14 medarbejdere · 11 samtidige tekniske projekter',[
 ('Plan og aflevering','Kapacitetsstyring, tilbud, underentreprenører, aftalegrundlag og dokumentation fra specifikation til aflevering.')]),
 ('Vedligeholdelses- og driftsleder / værkstedstekniker','Biofos, Lynetten · København · aug. 2017–jan. 2022','24/7-drift · el- og mekaniske anlæg',[
 ('Spildevandsanlæg','Forebyggende vedligehold, fejlfinding og reservedelsflow; 5S, Standard Work, LOTO og risikovurdering.')]),
 ('Elektromekaniker / produktionsteamleder','ARJ Engineering · Teheran · dec. 2003–mar. 2010','12 mekanikere og teknikere',[
 ('Værksted','Vagtplanlægning, materialestyring og reparation af industrielt el- og mekanisk udstyr.')])]
 for title,meta,scope,bullets in jobs:
  m.job(title,meta,scope=scope)
  for a,b in bullets:m.bullet(a,b,after=15)
 m.section('UDDANNELSE OG CERTIFICERING')
 for a,b in [('B.Tech, Technology Management & Mechanical Engineering — maskinmesterretningen','Maskinmesterskolen København · 2017–2022 · EQF 6'),('El- og maskinteknisk design, elteknik','Tehran Technical University · 2000–2003 · EQF 6'),('Elautoriseret maskinmester','Sikkerhedsstyrelsen · LV/MV/HV · 2023'),('PRINCE2-certificeret projektleder','AXELOS / PeopleCert')]:m.edu(a,b)
 m.para('Dansk og persisk/farsi: modersmål · Engelsk: professionelt · Kørekort B · Bopæl i Måløv. Tiltrædelse og overgang fra ELOHVAC aftales.',after=40)
 m.page_break();m.models_table('FØRSTE 90 DAGE — FORSLAG TIL OPSTART',('Tid','Handling og forventet leverance'),[
 ('Uge 1','Møde planchef, planteam og samarbejdspartnere. Afklare rolle, planfagligt ansvar, aktuelle projekter, beslutningsgange og kommunens gældende procedurer.'),
 ('Inden dag 30','Sammen med en erfaren planlægger danne overblik over en udvalgt sag: plangrundlag, parter, tidsplan, eksisterende viden og spørgsmål til miljø, trafik, byggeri og forsyning.'),
 ('Inden dag 60','Under planfaglig ledelse følge op på aftalte afklaringer, dokumentere afhængigheder og hjælpe med dialog og mødeforberedelse. Faglige vurderinger og myndighedsbeslutninger varetages af de ansvarlige.'),
 ('Inden dag 90','Gennemgå fremdrift, åbne spørgsmål og læringsbehov med planchefen. Aftale næste opgaver og en plan for relevant oplæring inden eventuelt selvstændigt ansvar.')])
 m.section('FRA IDÉ TIL BESLUTNING — ET FORSLAG TIL SAMARBEJDE')
 for a,b in [
 ('Behov og rammer','Afdække virksomhedens ønsker og sammen med planfaglige kolleger gennemgå gældende kommuneplan, lokalplan og mulige alternativer. Afklaringer skal ikke foregribe politisk stillingtagen.'),
 ('Faglige spor','Aftale input fra de ansvarlige for natur, miljø, støj, trafik, byggeri og forsyning. Samle tidsfrister, afhængigheder og åbne spørgsmål i ét tilgængeligt overblik.'),
 ('Høring og interessenter','Aftale dialog og høringsproces med den ansvarlige planlægger. Registrere indkomne synspunkter og sikre, at de behandles efter kommunens procedurer og gældende regler.'),
 ('Beslutning og realisering','Bidrage med klar dokumentation af fakta, alternativer og konsekvenser. Planfaglige og juridiske vurderinger kvalitetssikres af myndighedens kompetente medarbejdere før politisk behandling.')]:m.bullet(a,b,after=30)
 m.section('DIGITAL STØTTE OG FAGLIG KONTROL')
 m.para('Jeg udvikler Python/Claude-værktøjer til planlægning, dokumentation og analyse samt investeringsmodeller til nye idéer. Eventuel brug i kommunen kræver godkendte systemer, korrekt behandling af oplysninger og menneskelig kontrol. AI erstatter aldrig en myndighedsvurdering, høringsbehandling eller politisk beslutning.',after=70)
 m.section('FORUDSÆTNING FOR ROLLEN')
 m.para('Solid selvstændig lokalplanlægning er ikke dokumenteret i mit CV. Før opgaver med planfagligt ansvar kan overtages, skal kompetencer, oplæring og kommunens krav til rollefordeling afklares.',after=60)
 return m.save(path,title='Ansøgning og CV — erhvervsplanlægning, Ringsted Kommune',subject='Tværfaglig koordinering og erhvervsudvikling',keywords='planlægning, erhverv, koordinering, Ringsted')

if __name__=='__main__':print(build(os.path.join(ROOT,'Shahram_Ajloo_Ringsted_Erhvervsplanlaegger.docx')))
