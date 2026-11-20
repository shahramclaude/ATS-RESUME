"""CV målrettet Coor Property; dokumenterede fakta fra master-CV."""
import os
from master_design import MasterDoc
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(R,'Shahram_Ajloo_Coor_Property_CV.docx')
m=MasterDoc(os.path.join(R,'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='da-DK')
m.header_banner('SHAHRAM AJLOO','DRIFTSCHEF  |  TEKNISK DRIFT OG SERVICE', '+45 93 99 95 14  ·  ajlooshahram@gmail.com  ·  linkedin.com/in/shahramajloo  ·  Måløv')
m.meta('CV målrettet Driftschef / Operations Manager · Coor Property · Ballerup',after=100)
m.section('PROFIL')
m.para('Elautoriseret maskinmester og driftsleder med erfaring i ejendomsdrift, teknisk vedligehold og service. Erfaring med personaleansvar for teamledere og tekniske medarbejdere samt med kontraktopfølgning og forecast. Baggrunden er relevant for Facility Management og kundeoplevelse. Forener teknisk indsigt med kundeansvar og økonomistyring. I Coor-rollen vil jeg samarbejde på tværs med projekter, økonomi, HR, indkøb og specialister.',after=80,line=275,justify=False)
m.section('LEDELSE OG DRIFTSANSVAR')
for a,b in [
('Mennesker','Personaleledelse af ledere og medarbejdere; daglig prioritering, 1:1, oplæring og opfølgning. Erfaring med at lede et selvstyrende team.'),
('Kunde og leverance','Kundekontakt, tekniske serviceleverancer og kontraktopfølgning. Fokus på kvalitet, sikkerhed og kontraktkrav samt klare aftaler mellem kunde, medarbejdere og samarbejdspartnere.'),
('Forretning','Fuldt resultatansvar i ELOHVAC samt erfaring med budget og forecast. Tilbud, ressourceplanlægning og opfølgning på økonomi og resultater.'),
('Drift og forbedring','Ejendomsdrift og vedligehold på flere lokationer; forebyggende vedligehold, teknisk fejlfinding og forbedring af arbejdsgange.')]:m.bullet(a,b,after=65,line=275)
m.section('ERHVERVSERFARING')
m.job('Ejer / teknisk direktør / elautoriseret maskinmester','ELOHVAC ApS · København · maj 2023–nu')
for a,b in [
('Ledelse','Personaleansvar for fem elektrikere og tre lærlinge; planlægning, 1:1, MUS og struktureret oplæring.'),
('Kunde og drift','Ansvar for el-tekniske serviceopgaver, vedligehold og fejlfinding på el-, ventilations- og klimaanlæg for erhvervskunder.'),
('Økonomi og kvalitet','Fuldt P&L-ansvar; tilbud, beregning, materialer, underentreprenører, kvalitetssikring og dokumentation.'),
('Resultat','Egne digitale værktøjer til blandt andet tilbud, tidsplaner og kvalitetstjek har bidraget til et produktivitetsløft på over 40 %.')]:m.bullet(a,b,after=45,line=270)
m.job('Medejer og CTO / teknisk ansvarlig for AI-afdelingen','Data Power Consultant ApS · København · 2024–nov. 2026')
m.para('Sideløbende med ELOHVAC. Virksomheden er ophørt.',after=30,line=250,justify=False)
for a,b in [('Ledelse','Ansvarlig for en afdeling med 4–10 personer og for prioritering af tekniske leverancer.'),('Kundeløsninger','Ledede implementering af tekniske og industrielle applikationer fra kravafdækning til dokumentation og overdragelse.')]:m.bullet(a,b,after=40,line=270)
m.page_break()
m.header_banner('SHAHRAM AJLOO','CV  |  ERHVERVSERFARING OG UDDANNELSE', '+45 93 99 95 14  ·  ajlooshahram@gmail.com  ·  linkedin.com/in/shahramajloo')
m.section('ERHVERVSERFARING — FORTSAT')
m.job('Senior idriftsættelsesingeniør / projektleder, elsystem','Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024')
for a,b in [('Ledelse og koordinering','Koordinerede 25 specialister på tværs af engineering, indkøb og anlæg i 37 samtidige CAPEX-projekter.'),('Leverance','Fulgte fremdrift, økonomi og risiko; ansvar for FAT/SAT og IQ/OQ/PQ med nul kritiske afvigelser ved aflevering.')]:m.bullet(a,b,after=40,line=270)
m.job('Projekt- og værkstedsleder','Ventek-Air · København · jan. 2022–nov. 2022')
for a,b in [('Drift og medarbejdere','Daglig ledelse af et team på 14 og styring af kapacitet og fremdrift på 11 samtidige projekter.'),('Leverancer','Tilbud, aftalegrundlag, underentreprenører, sikkerhedsdokumentation og aflevering. Tavlemøder og flaskehalsanalyse understøttede prioriteringen.')]:m.bullet(a,b,after=40,line=270)
m.job('Vedligeholdelses- og driftsleder / værkstedstekniker','BIOFOS, Lynetten · København · aug. 2017–jan. 2022')
for a,b in [('Teknisk drift','Kritisk el- og mekanisk drift med forebyggende vedligehold og akut fejlfinding på blandt andet pumper, HVAC og højspændingstavler.'),('Sikkerhed og forbedring','Arbejdede med LOTO, risikovurdering, APV, standardarbejde og PDCA i skifteholdsdrift.')]:m.bullet(a,b,after=40,line=270)
m.job('Elektromekaniker / produktionsteamleder','ARJ Engineering · Teheran · dec. 2003–mar. 2010')
m.bullet('Team og teknik','Ledelse af 12 mekanikere og teknikere; vagtplanlægning, materialestyring samt diagnose og reparation af industrielt udstyr.',after=40,line=270)
m.section('UDDANNELSE OG CERTIFICERING')
for a,b in [('Elautoriseret maskinmester, LV/MV/HV','Sikkerhedsstyrelsen · 2023'),('B.Tech, Technology Management and Mechanical Engineering','Copenhagen School of Marine Engineering & Technology Management · 2017–2022'),('PRINCE2 certificeret projektleder','AXELOS / PeopleCert'),('Køleteknik og klimaanlæg','Mercantec AMU · 2021'),('El- og maskinteknisk design, elteknik','Tehran Technical University · 2000–2003')]:m.edu(a,b)
m.section('METODER, SYSTEMER OG SPROG')
m.para('**Metoder:** PRINCE2, Lean og Six Sigma anvendt i praksis; kun PRINCE2 certificeret. **Systemer:** Excel, SAP ERP og digitale planlægningsværktøjer. **Sprog:** dansk, engelsk og persisk. **Kørekort:** B.',after=30,line=270,justify=False)
m.save(OUT)
