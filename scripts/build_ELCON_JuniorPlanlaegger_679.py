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
 m.section('RELEVANT ERFARING')
 for a,b in [
 ('Kundeservice og opfølgning','ELOHVAC: dialog med erhvervskunder om tilbud, installation og service; koordinering af opgaver frem til aflevering. Direkte callcentererfaring er ikke dokumenteret.'),
 ('Planlægning','ELOHVAC: daglig planlægning af elektrikere og lærlinge, materialer og underentreprenører. Ventek-Air: kapacitetsstyring og opfølgning på 11 sideløbende tekniske projekter.'),
 ('El-teknisk forståelse','Installation, tavler, styring og fejlfinding på el- og klimaanlæg. Specifik erfaring med installation eller booking af ladestandere er ikke dokumenteret.'),
 ('IT og struktur','MS Office, Excel/Power Query og SAP ERP; Python og Claude til tidsplaner, KS og KPI. Dokumenteret produktivitetsløft over 40 % hos ELOHVAC gennem AI-værktøjer.'),
 ('Samarbejde','Daglig koordinering med elektrikere, lærlinge, kunder og underentreprenører; tavlemøder og videndeling hos Ventek-Air.')]:m.bullet(a,b,after=30)
 m.section('SPROG OG PRAKTISK')
 m.para('Dansk og persisk/farsi: modersmål · Engelsk: professionelt · Bopæl: Måløv · Kørekort B. Arbejdstid og tiltrædelse aftales.',after=70)
 m.page_break();m.section('ERHVERVSERFARING')
 jobs=[
 ('Indehaver / teknisk direktør / elautoriseret maskinmester','ELOHVAC ApS · København · maj 2023–nu','5 elektrikere og 3 lærlinge',[
 ('Kunder og opgaver','Tilbud, planlægning, materialer, underentreprenører, kvalitet og aflevering af el-, ventilations- og klimaanlæg for erhvervskunder.'),
 ('Overblik','Daglig koordinering og tekniske serviceopgaver; Python/Claude-værktøjer til tidsplaner og kvalitetssikring.')]),
 ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen','Data Power Consultant ApS · København · 2024–2026 · sideløbende med ELOHVAC','4–10 personer',[
 ('Behov og overdragelse','Kravafdækning, tekniske løsninger og dokumenteret overdragelse til kunder. Professionel og aktiv AI- og Claude-koder.')]),
 ('Senior idriftsættelsesingeniør / projektleder, elsystem','Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024','37 samtidige CAPEX-projekter · 25 specialister',[
 ('Koordinering','Fremdrift, ressourcer og rapportering på tværs af engineering, indkøb og anlæg. SAP ERP til økonomi og aktiver.')]),
 ('Projekt- og værkstedsleder','Ventek-Air · København · jan. 2022–nov. 2022','14 medarbejdere · 11 samtidige projekter',[
 ('Planlægning','Kapacitetsstyring, aftaler med underentreprenører og dokumentation frem til aflevering. Daglige tavlemøder.')]),
 ('Vedligeholdelses- og driftsleder / værkstedstekniker','Biofos, Lynetten · København · aug. 2017–jan. 2022','El- og mekaniske anlæg · døgnbemandet drift',[
 ('Drift','Fejlfinding, forebyggende vedligehold og reservedelsflow på tekniske anlæg.')]),
 ('Elektromekaniker / produktionsteamleder','ARJ Engineering · Teheran · dec. 2003–mar. 2010','12 mekanikere og teknikere',[
 ('Værksted','Planlægning, materialestyring og reparation af industrielt el- og mekanisk udstyr.')])]
 for title,meta,scope,bullets in jobs:
  m.job(title,meta,scope=scope)
  for a,b in bullets:m.bullet(a,b,after=15)
 m.section('UDDANNELSE OG CERTIFICERING')
 for a,b in [('B.Tech, Technology Management & Mechanical Engineering — maskinmesterretningen','Maskinmesterskolen København · 2017–2022 · EQF 6'),('El- og maskinteknisk design, elteknik','Tehran Technical University · 2000–2003 · EQF 6'),('Elautoriseret maskinmester','Sikkerhedsstyrelsen · LV/MV/HV · 2023'),('PRINCE2-certificeret projektleder','AXELOS / PeopleCert')]:m.edu(a,b)
 return m.save(path,title='Ansøgning og CV — Junior Planlægger, ELCON',subject='Kundeservice og montørplanlægning',keywords='kundeservice, planlægning, ladestander, Glostrup')
if __name__=='__main__':print(build(os.path.join(ROOT,'Shahram_Ajloo_ELCON_JuniorPlanlaegger_679.docx')))
