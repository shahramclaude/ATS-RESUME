"""Jobrettet CV med kort motivation til Bavarian Nordic, JR101496."""
from pathlib import Path
from master_design import MasterDoc
R=Path(__file__).resolve().parent.parent
m=MasterDoc(str(R/'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='da-DK')
n='SHAHRAM AJLOO'; t='Automatiktekniker | teknisk drift og vedligehold'
c='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
m.resume_header(n,t,c,'MOTIVATION OG TEKNISK PROFIL')
m.meta('Bavarian Nordic · Kvistgaard · Automatiktekniker · JR101496',after=30)
m.para('**Motivation:** Stabil vaccineproduktion kræver, at tekniske problemer bliver løst sikkert, og at udstyret kan overdrages til produktionen med den nødvendige dokumentation. Jeg søger stillingen for at bruge min erfaring med elteknisk fejlfinding, vedligehold og arbejde i reguleret produktion tæt på kollegerne i Drug Product – Teknisk Support. Samarbejdet med teknikere og udstyrsejere om forebyggelse, genopretning og forbedring af driften tiltaler mig.',after=65,line=245,justify=False)
m.para('Elautoriseret maskinmester med baggrund i el- og mekanisk drift, SCADA, anlægsprojekter og idriftsættelse. Erfaringen omfatter forebyggende vedligehold og akut fejlfinding fra BIOFOS samt FAT/SAT og kvalificering i et GMP-reguleret produktionsmiljø hos Novo Nordisk. Har desuden ledet arbejde med industrielle PLC- og styresystemer.',after=60,line=245,justify=False)
m.section('FAGLIGE STYRKER TIL DRUG PRODUCT – TEKNISK SUPPORT')
for a,b in [
('Fejlfinding og vedligehold','Forebyggende vedligehold og akut fejlfinding på el- og mekaniske anlæg fra BIOFOS; elinstallationer, tavler og styringer i ELOHVAC.'),
('Overvågning og automatisering','SCADA indgik i den tekniske drift på Lynetten. Erfaring med ledelse af arbejde med PLC-styrede anlæg og industrielle styresystemer.'),
('GMP og dokumentation','FAT/SAT og IQ/OQ/PQ ved idriftsættelse af elsystemer hos Novo Nordisk under GMP/FDA/EMA; nul kritiske afvigelser ved aflevering.'),
('Sikker drift og samarbejde','Samarbejder om planlægning, sikkerhed og teknisk aflevering på tværs af faggrupper. Arbejder med risikovurdering og LOTO samt praktisk problemløsning og forbedring.'),
('Produktionens udstyr','Med afsæt i teknisk drift vil jeg sammen med udstyrsejerne sætte mig ind i pakkemaskiner, inspektionsudstyr, HMI og lokale instruktioner.')]:m.bullet(a,b,after=25,line=240)
m.models_table('PRAKTISK TILGANG TIL TEKNISK SUPPORT',('Opgave','Tilgang i rollen'),[
('Driftsforstyrrelse','Afklar symptomer med produktionen, sikr anlægget og undersøg fejlen sammen med ansvarlig tekniker. Bekræft funktion før tilbagelevering.'),
('Vedligehold','Følg godkendte instruktioner og sikkerhedsforanstaltninger; opret, udfør og afrapportér arbejdsordrer efter lokale procedurer.'),
('Overvågning','Brug SCADA og HMI efter oplæring til at undersøge alarmer og driftsstatus; ændringer håndteres efter gældende godkendelser.'),
('GMP og forbedring','Dokumentér arbejdet efter lokale GMP-krav, og inddrag udstyrsejer og relevante kvalitetspartnere ved afvigelser eller ændringer.')])
m.page_break();m.section('ERHVERVSERFARING')
m.job('Indehaver / teknisk direktør / elautoriseret maskinmester','ELOHVAC ApS · København · maj 2023–nu')
for a,b in [('Elteknik og service','Installation, tavler og styring, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg for erhvervskunder.'),('Kvalitet og sikkerhed','Planlægning, risikovurdering, LOTO, kvalitetssikring og afleveringsdokumentation; personaleansvar for fem elektrikere og tre lærlinge.'),('Forbedring','AI-assisterede værktøjer til tilbud, tidsplaner og kvalitetstjek bidrog til et produktivitetsløft på over 40 %.')]:m.bullet(a,b,after=15,line=240)
m.job('Medejer og CTO / ansvarlig for AI-afdelingen','Data Power Consultant ApS · København · 2024–nov. 2026')
m.bullet('Teknisk ledelse','Ledelse af AI-afdeling med 4–10 personer og kundeløsninger med AI-kodning, LLM-API’er og AI-agenter. AI anvendt til teknisk design og ledelsesarbejde med faglig kontrol. Sideløbende med ELOHVAC; virksomheden er ophørt.',after=15,line=240)
m.job('Senior idriftsættelsesingeniør / projektleder, elsystemer','Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024')
for a,b in [('Idriftsættelse og kvalitet','FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA på elsystemer; nul kritiske afvigelser ved aflevering.'),('Tværfaglig koordinering','Koordinerede 25 specialister på tværs af 37 samtidige anlægs- og CAPEX-projekter med opfølgning på fremdrift, ressourcer og risici.')]:m.bullet(a,b,after=15,line=240)
m.job('Projekt- og værkstedsleder','Ventek-Air · København · jan. 2022–nov. 2022')
m.bullet('Teknisk levering','Ledte 14 medarbejdere og 11 samtidige anlægsprojekter med planlægning, sikkerhedsdokumentation og aflevering.',after=15,line=240)
m.job('Vedligeholdelses- og driftsleder / værkstedstekniker','BIOFOS, Lynetten · København · aug. 2017–jan. 2022')
m.bullet('Drift og fejlfinding','El- og mekanisk drift med pumper, HVAC, højspændingstavler og SCADA; forebyggende vedligehold og akut fejlfinding i 24/7-drift.',after=15,line=240)
m.job('Elektromekaniker / produktionsteamleder','ARJ Engineering · Teheran · dec. 2003–mar. 2010')
m.bullet('Teknisk værksted','Fejldiagnose og reparation af el- og mekaniske anlæg samt ledelse af 12 mekanikere og teknikere.',after=15,line=240)
m.section('UDDANNELSE, METODER OG SPROG')
for a,b in [('Elautoriseret maskinmester, LV/MV/HV','Sikkerhedsstyrelsen · maj 2023'),('B.Tech, teknologiledelse og maskinteknik','Københavns Maskinmesterskole · 2017–2022'),('El- og maskinteknisk design, elteknik','Tehran Technical University · 2000–2003'),('PRINCE2-certificeret projektleder','AXELOS / PeopleCert')]:m.edu(a,b)
m.para('**Metoder:** Lean og Six Sigma anvendt i praksis; PRINCE2-certificeret. **Sprog:** Dansk, engelsk på professionelt niveau og persisk. **Bopæl:** Måløv.',after=20,line=235,justify=False)
m.save(str(R/'Shahram_Ajloo_BavarianNordic_Automatiktekniker_CV.docx'))
