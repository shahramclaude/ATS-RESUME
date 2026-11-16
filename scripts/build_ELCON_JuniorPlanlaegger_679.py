"""ELCON Junior Planlægger: dansk ansøgning og CV."""
import os
from master_design import MasterDoc
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME='SHAHRAM AJLOO'
TITLE='Kundeservice | Planlægning | El-teknisk forståelse'
CONTACT='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'

def build(path):
 m=MasterDoc(os.path.join(ROOT,'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='da-DK')
 m.header_banner(NAME,TITLE,CONTACT);m.meta('ELCON · Kundecenter Glostrup · Att.: teamleder Therese Ring · Rekvisition 679')
 p=m._p(spacing_after=90,line=260,justify=False);m._run(p,'Junior Planlægger — en tryg vej fra bestilling til installation',bold=True,color='1A1A1A')
 for text in [
 'Når en kunde har bestilt en ladestander, skal vejen til en fungerende løsning være enkel. Kundecenterets opgave er at omsætte ordren til en klar aftale, give kunden svar undervejs og sikre, at servicemontøren har de oplysninger, der skal til for at møde forberedt. Hver kontakt er en mulighed for at gøre installationen mere overskuelig for kunden.',
 'En god samtale starter med at lytte og afklare, hvad kunden har brug for. Oplysninger om adresse, kontakt og aftalt tidspunkt registreres i de IT-systemer, ELCON anvender, sammen med eventuelle forhold, der kræver nærmere afklaring. Spørgsmål besvares i et forståeligt sprog på dansk eller engelsk. Hvis et svar kræver teknisk vurdering eller ligger uden for kundecenterets ansvar, sendes spørgsmålet til den rette kollega frem for at give et usikkert løfte.',
 'Planlægningen skal binde kunde og montør sammen: find en ledig tid, tag højde for område og de oplysninger, der er til rådighed, og bekræft aftalen efter de gældende arbejdsgange. Hvis en opgave ændrer sig, skal berørte kunder og montører have besked, og en ny aftale skal registreres. Et tydeligt næste skridt og en ansvarlig på hver åben sag gør det muligt at følge op uden, at kunden skal starte forfra.',
 'Når telefonerne er travle, hjælper det at prioritere kundehenvendelser i fællesskab: hastende ændringer håndteres først, øvrige henvendelser får en realistisk tilbagemelding, og kollegerne i hvert team hjælper hinanden med at holde overblik. Videndeling om tilbagevendende spørgsmål og korte, præcise notater skaber sammenhæng i kundeoplevelsen. Sådan kan ELCONs kundecenter understøtte den grønne omstilling med en service, der fungerer helt nede i den enkelte aftale.'
 ]:m.para(text,after=100)
 m.meta('Med venlig hilsen',after=10);m.meta('Shahram Ajloo',after=0)
 m.page_break();m.resume_header(NAME,TITLE,CONTACT,'PROFIL')
 m.para('Elautoriseret maskinmester med erfaring i kundekontakt, planlægning af tekniske opgaver og koordinering af medarbejdere. Har fulgt installationer fra kundens behov til aflevering og er vant til at holde styr på aftaler, ressourcer og dokumentation.',after=70)
 m.section('KOMPETENCER — KUNDE, PLAN OG TEKNIK')
 for a,b in [
 ('Kunder og service','ELOHVAC: erhvervskundedialog, tilbud, serviceaftaler og koordinering fra opgave til aflevering. Klare aftaler, opfølgning, kvalitetssikring og afleveringsdokumentation.'),
 ('Planlægning og fremdrift','Daglig koordinering af 5 elektrikere og 3 lærlinge hos ELOHVAC; kapacitetsstyring af 11 samtidige projekter hos Ventek-Air. Materialer, underentreprenører og ressourcer på tværs.'),
 ('El-teknik og drift','Installation, tavler, styring og fejlfinding på el-, ventilations- og klimaanlæg. Biofos: pumper, HVAC, højspændingstavler og SCADA i døgnbemandet drift.'),
 ('Økonomi og opmåling','Fuldt P&L-ansvar, tilbud og beregning. Akkordbreve, opmåling, tildeling til sjak samt regulering og opgørelse af mer- og mindrearbejde.'),
 ('Digitale værktøjer','MS Office, Excel/Power Query, SAP ERP, Python og Claude API. Aktiv AI-/Claude-koder med værktøjer til planlægning, KS og KPI; investeringsmodeller med NPV, IRR og scenarier.'),
 ('Ledelse og forbedringer','PRINCE2-certificeret; tavlemøder, 1:1 og situationsbestemt ledelse. PDCA, A3, 5S, Standard Work, 5xHvorfor og flaskehalsanalyse anvendt i praksis; ikke Lean- eller Six Sigma-certificeret.')]:m.bullet(a,b,after=25)
 m.section('RESULTATER OG PRAKTISK INFORMATION')
 m.para('Over 40 % produktivitetsløft med AI-værktøjer hos ELOHVAC · 40 % lavere energiomkostninger via PDCA hos Novo Nordisk · Ingen kritiske afvigelser ved Novo-afleveringer. Dansk og persisk/farsi: modersmål; engelsk: professionelt. Måløv · Kørekort B · Tiltrædelse og arbejdstid aftales.',after=50)
 m.para('Direkte callcentererfaring samt specifik booking eller installation af ladestandere er ikke dokumenteret. El- og planlægningserfaringen er relevant, men ikke identisk med disse opgaver.',after=40)
 m.page_break();m.section('ERHVERVSERFARING')
 jobs=[
 ('Indehaver / teknisk direktør / elautoriseret maskinmester','ELOHVAC ApS · København · maj 2023–nu','5 elektrikere og 3 lærlinge · fuldt P&L-ansvar',[
 ('Kundeaftaler og levering','Tilbud, beregning og kundedialog; planlægning af medarbejdere, materialer og underentreprenører, kvalitetssikring og dokumenteret aflevering af el-, ventilations- og klimaanlæg.'),
 ('Teknisk service','Installation, tavler, styring, fejlfinding og forebyggende vedligehold fra akutte udkald til afsluttet anlæg. Serviceaftaler fulgt på responstid, kvalitet og leveringsevne.'),
 ('Økonomi og personale','Fuld P&L, akkordbreve og opmåling; tildeling til sjak og opgørelse af mer- og mindrearbejde. 1:1, MUS, lærlingeoplæring, LOTO og risikovurdering.'),
 ('Digitale forbedringer','Python/Claude API til tilbudsberegning, tidsplaner, KS-tjeklister og KPI-dashboards; dokumenteret produktivitetsløft over 40 %.')]),
 ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen','Data Power Consultant ApS · København · 2024–2026 · sideløbende med ELOHVAC','4–10 personer',[
 ('Fra behov til overdragelse','Kravafdækning, arkitektur og integration af tekniske og industrielle applikationer; idriftsættelse, dokumentation og overdragelse til kundens drift.'),
 ('AI og beslutningsstøtte','Ledte AI-/AI coding-afdelingen; LLM-API’er, AI-agenter og kodegenerering med review og test. Anvendte AI til rapportering, KPI-analyse og beslutningsoplæg.'),
 ('Planlægning på tværs','Prioriterede opgaver i to sideløbende virksomheder med fælles plan og skriftlige aftaler.')]),
 ('Senior idriftsættelsesingeniør / projektleder, elsystem','Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024','37 samtidige CAPEX-projekter · 25 specialister · 2–10 mio. kr. pr. projekt',[
 ('Styring og kommunikation','Fremdrift, økonomi, risici og ressourcer på tværs af engineering, indkøb og anlæg; månedlig rapportering til ledelse og bygherre og SAP ERP til aktiver og omkostninger.'),
 ('Teknik og kvalitet','Tavler og styring, UPS, nød- og panikbelysning samt ABA/ABV og PDS. FAT/SAT og IQ/OQ/PQ under GMP; ingen kritiske afvigelser ved aflevering.'),
 ('Energi og analyse','PDCA-program reducerede energiomkostninger med 40 %. A3, 5xHvorfor og Ishikawa til fejlfinding og forbedring.')]),
 ('Projekt- og værkstedsleder','Ventek-Air · København · jan. 2022–nov. 2022','14 medarbejdere · 11 samtidige projekter · 2–10 mio. kr. pr. projekt',[
 ('Plan og aflevering','Kapacitets- og fremdriftsstyring fra specifikation til aflevering; udbud, tilbud, aftalegrundlag, underentreprenører og sikkerhedsdokumentation.'),
 ('Daglig styring','Tavlemøder, flaskehalsanalyse og standardiserede arbejdsgange med forbedret leveringsevne.')]),
 ('Vedligeholdelses- og driftsleder / værkstedstekniker','Biofos, Lynetten · København · aug. 2017–jan. 2022','El- og mekaniske anlæg · døgnbemandet drift',[
 ('Drift og lager','Fejlfinding og forebyggende vedligehold af pumper, HVAC, højspændingstavler og SCADA. 5S, Standard Work og PDCA på værksted og reservedelslager.'),
 ('Sikkerhed','LOTO, APV, risikovurdering og opfølgning på nærved-hændelser i skifteholdsdrift.')]),
 ('Elektromekaniker / produktionsteamleder','ARJ Engineering · Teheran · dec. 2003–mar. 2010','12 mekanikere og teknikere',[
 ('Værksted','Vagtplanlægning, materialestyring, fejldiagnose og reparation af industrielle el- og mekaniske anlæg; rodårsagsanalyse og korrigerende handlinger.')])]
 for i,(title,meta,scope,bullets) in enumerate(jobs):
  if i == 3: m.page_break();m.section('ERHVERVSERFARING — FORTSAT')
  m.job(title,meta,scope=scope)
  for a,b in bullets:m.bullet(a,b,after=15)
 m.section('UDDANNELSE OG CERTIFICERING')
 for a,b in [('B.Tech, Technology Management & Mechanical Engineering — maskinmesterretningen','Maskinmesterskolen København · 2017–2022 · EQF 6'),('El- og maskinteknisk design, elteknik','Tehran Technical University · 2000–2003 · EQF 6'),('HF, matematik og fysik','VUC · 2012–2017'),('Elautoriseret maskinmester','Sikkerhedsstyrelsen · LV/MV/HV · 2023'),('PRINCE2-certificeret projektleder','AXELOS / PeopleCert'),('Køleteknik og klimaanlæg','AMU · Mercantec · 2021'),('STCW-certifikater','Maskinrumsvagt og udpegede sikkerhedsopgaver m.fl. · Søfartsstyrelsen · 2021–2023')]:m.edu(a,b)
 return m.save(path,title='Ansøgning og CV — Junior Planlægger, ELCON',subject='Kundeservice og montørplanlægning',keywords='kundeservice, planlægning, ladestander, Glostrup')
if __name__=='__main__':print(build(os.path.join(ROOT,'Shahram_Ajloo_ELCON_JuniorPlanlaegger_679.docx')))
