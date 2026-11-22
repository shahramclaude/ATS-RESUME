"""Coor: ansøgning + CV i brugerens originale masterdesign."""
import os
from master_design import MasterDoc
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
m=MasterDoc(os.path.join(R,'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='da-DK')
n='SHAHRAM AJLOO'; title='Driftschef / Operations Manager — Coor Property, Ballerup'
c='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
m.header_banner(n,title,c)
m.meta('Coor Property · Att.: Søren Klemmensen',after=25)
m.para('**Ansøgning: Driftschef / Operations Manager**',after=90,justify=False)
m.para('Kære Søren Klemmensen',after=85,justify=False)
m.para('Coor Property skal give kunden en ejendom, der fungerer i hverdagen, og en service, der lever op til aftalen. Det kræver, at teamlederne har plads til at lede, at problemer bliver taget i opløbet, og at drift og økonomi følges som én samlet opgave. Sådan vil jeg gribe ansvaret an:',after=100,line=265,justify=False)
for a,b in [
('Ledelse tæt på opgaven','Jeg vil aftale tydelige mål og beslutningsrum med teamlederne og følge op på bemanding, trivsel og udvikling. Når en leder står med en vanskelig prioritering, skal sparringen være tilgængelig; løsningen skal ikke trækkes væk fra den, der har ansvaret.'),
('Kundens aftale som arbejdsgrundlag','Sammen med teamlederne vil jeg omsætte kontraktkrav til konkrete opgaver og ansvar. En fast kundedialog skal give overblik over leverancer, åbne afvigelser og kommende behov. Hvis en aftale er i risiko, skal kunden have besked og en realistisk plan.'),
('Drift, sikkerhed og vedligehold','Jeg vil gennemgå de tekniske opgaver, sikkerhedsforhold og vedligeholdsbehov med dem, der kender ejendommene. Akutte problemer skal håndteres hurtigt, men må ikke skubbe den forebyggende indsats til side. Risiko, konsekvens og næste handling skal være tydelig ved prioriteringen.'),
('Økonomi, der kan handles på','Budget, forecast og ressourceforbrug skal følges sammen med teamlederne og økonomi. Ved afvigelser vil jeg afklare årsagen og beslutte, om bemanding, indkøb eller prioritering skal justeres, før konsekvensen vokser.'),
('Forbedringer med værdi for kunden','Sammen med kunden og specialisterne vil jeg vælge forbedringer, der både styrker leverancen og giver mening økonomisk — eksempelvis en bedre plan for vedligehold eller en indsats på energiforbruget. Projekter, HR og indkøb inddrages, når opgaven kræver det.')]:m.bullet(a,b,after=85,line=265)
m.para('Jeg ser frem til at drøfte, hvordan Coor Property kan samle ledelse, kundesamarbejde og den tekniske drift om en stabil og udviklingsorienteret leverance.',after=80,line=265,justify=False)
m.meta('Med venlig hilsen',after=15);m.meta('Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com',after=0)
m.page_break();m.resume_header(n,title,c,'LEDERPROFIL')
m.para('Elautoriseret maskinmester med erfaring i ejendomsdrift, teknisk service og vedligehold. Personaleansvar for ledere, der selv leder medarbejdere, samt erfaring med et selvstyrende team og tekniske medarbejdere. Arbejder med kundekontakt, kontraktopfølgning og forecast; fuldt resultatansvar i ELOHVAC. Kombinationen af teknisk indsigt, ledelse og økonomi er relevant for Coor Property og Facility Management.',after=70,line=260,justify=False)
m.section('LEDERKOMPETENCER — DRIFT, MENNESKER OG KUNDE')
for a,b in [
('Ledelse gennem andre','Personaleansvar for ledere og medarbejdere; planlægning, 1:1, MUS og oplæring. Erfaring med at lede et selvstyrende team.'),
('Ejendomsdrift og service','Ejendomsdrift og vedligehold på flere lokationer; tekniske installationer, forebyggende vedligehold og fejlfinding.'),
('Kunde, aftale og kvalitet','Kundedialog, kundeoplevelse og kontraktopfølgning. Kvalitetssikring, sikkerhed og dokumentation indgår i tekniske leverancer.'),
('Økonomi og forbedring','Budget, forecast og opfølgning på resultater; fuldt P&L i ELOHVAC. Planlægning, ressourceprioritering og anvendelse af Lean og Six Sigma i praksis.'),
('Samarbejde og levering','Koordinering på tværs af engineering, indkøb, anlæg, underentreprenører og specialister. Fokus på fremdrift og aflevering.')]:m.bullet(a,b,after=30,line=250)
m.section('ERHVERVSERFARING')
m.job('Ejer / teknisk direktør / elautoriseret maskinmester','ELOHVAC ApS · København · maj 2023–nu')
for a,b in [
('Medarbejdere','Leder fem elektrikere og tre lærlinge; daglig planlægning, 1:1, MUS, oplæring og arbejdsmiljøopfølgning.'),
('Kunde og service','El-teknisk service for erhvervskunder: installation, tavler, styring, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg.'),
('Økonomi og kvalitet','Fuldt P&L-ansvar; tilbud, beregning, materialer, underentreprenører, kvalitetssikring og afleveringsdokumentation. LOTO, APV og risikovurdering.'),
('Forbedring','Egne digitale værktøjer til tilbud, tidsplaner og kvalitetstjek har bidraget til et produktivitetsløft på over 40 %.')]:m.bullet(a,b,after=20,line=250)
m.job('Medejer og CTO / teknisk ansvarlig for AI-afdelingen','Data Power Consultant ApS · København · 2024–nov. 2026')
m.bullet('Ledelse og kundeløsninger','Ledede en afdeling på 4–10 personer og implementering af tekniske og industrielle applikationer fra behov til dokumentation og overdragelse. Sideløbende med ELOHVAC; virksomheden er ophørt.',after=20,line=250)
m.page_break()
m.section('ERHVERVSERFARING — FORTSAT')
m.job('Senior idriftsættelsesingeniør / projektleder, elsystem','Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024')
for a,b in [('Projektledelse','Koordinerede 25 specialister og 37 samtidige CAPEX-projekter; fulgte økonomi, fremdrift, ressourcer og risiko på tværs af engineering, indkøb og anlæg.'),('Kvalitet og teknik','FAT/SAT og IQ/OQ/PQ i reguleret miljø med nul kritiske afvigelser ved aflevering; erfaring med tavler, styring, UPS og nød- og panikbelysning.')]:m.bullet(a,b,after=25,line=250)
m.job('Projekt- og værkstedsleder','Ventek-Air · København · jan. 2022–nov. 2022')
m.bullet('Drift og projekter','Ledede 14 medarbejdere og planlagde 11 samtidige projekter. Tilbud, aftalegrundlag, underentreprenører, sikkerhedsdokumentation og aflevering; tavlemøder og flaskehalsanalyse.',after=25,line=250)
m.job('Vedligeholdelses- og driftsleder / værkstedstekniker','BIOFOS, Lynetten · København · aug. 2017–jan. 2022')
m.bullet('Kritisk drift','Forebyggende vedligehold og akut fejlfinding på pumper, HVAC, højspændingstavler og SCADA. Arbejdede med LOTO, APV, reservedelsflow, 5S og PDCA i skifteholdsdrift.',after=25,line=250)
m.job('Elektromekaniker / produktionsteamleder','ARJ Engineering · Teheran · dec. 2003–mar. 2010')
m.bullet('Team og teknik','Ledede 12 mekanikere og teknikere; vagtplanlægning, materialestyring, fejldiagnose og reparation af industrielle el- og mekaniske anlæg.',after=25,line=250)
m.section('UDDANNELSE OG CERTIFICERING')
for a,b in [('B.Tech, Technology Management and Mechanical Engineering','Copenhagen School of Marine Engineering & Technology Management · 2017–2022'),('Elautoriseret maskinmester, LV/MV/HV','Sikkerhedsstyrelsen · 2023'),('PRINCE2 certificeret projektleder','AXELOS / PeopleCert'),('Køleteknik og klimaanlæg','Mercantec AMU · 2021'),('El- og maskinteknisk design, elteknik','Tehran Technical University · 2000–2003')]:m.edu(a,b)
m.section('VÆRKTØJER, METODER OG SPROG')
m.para('**Metoder:** PRINCE2, Lean og Six Sigma anvendt i praksis; PRINCE2 certificeret. 5S, PDCA, A3, 5 × hvorfor og standardarbejde. **Systemer:** Excel, SAP ERP og digitale værktøjer til planlægning og kvalitet. **Sprog:** dansk, engelsk og persisk. **Kørekort:** B.',after=20,line=250,justify=False)
m.section('UDGANGSPUNKT FOR DE FØRSTE 90 DAGE')
for a,b in [('Dag 1–30','Mød teamledere og kunde. Gennemgå aftaler, sikkerhed, åbne afvigelser, bemanding og økonomi; fastlæg de vigtigste beslutninger.'),('Dag 31–60','Aftal opfølgningsrytme og ansvar for leverancer, forecast og risici. Afstem snitflader med projekter, HR, indkøb og specialister.'),('Dag 61–90','Gennemfør prioriterede forbedringer med klare ansvarlige, og følg virkningen sammen med kunde og teamledere.')]:m.bullet(a,b,after=20,line=250)
m.save(os.path.join(R,'Shahram_Ajloo_Coor_Property_Masterstil.docx'))
