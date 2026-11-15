"""Aalborg Portland Mechanical Supervisor — dansk ansøgning og CV.
Kilder: master-CV, brugerens opslag og bekræftelser; INTEL §237.
"""
import os
from master_design import MasterDoc
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAVN='SHAHRAM AJLOO'
TITEL='Mechanical Supervisor · mekanisk vedligehold, planlægning og sikker ledelse'
KONTAKT='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
def build(path):
    m=MasterDoc(os.path.join(ROOT,'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='da-DK')
    m.header_banner(NAVN,TITEL,KONTAKT)
    m.meta('4. november 2026')
    m.meta('Aalborg Portland · Mechanical Supervisor · Aalborg')
    p=m._p(spacing_after=80,line=260,justify=False); m._run(p,'Mekanisk vedligehold, der er klar, når produktionen giver adgang',bold=True,color='1A1A1A')
    def lp(t): m.para(t,after=45,line=240)
    lp('**Et planlagt stop begynder længe før anlægget står stille.** Arbejdet skal være afgrænset, folkene vide, hvad de skal gøre, og reservedele og eksterne ydelser være klar. Når produktionen giver adgang, skal sikkerheden og koordineringen holde — og når anlægget er tilbage i drift, skal erfaringerne med videre til næste plan.')
    lp('Hos Aalborg Portland er den opgave en del af det daglige mekaniske vedligehold på en cementfabrik i drift. Jeg søger rollen som Mechanical Supervisor, fordi jeg kan bringe vedligeholdsplanlægning, teknisk fejlsøgning og nærværende ledelse ind i samarbejdet mellem mekanikere, produktion, pålidelighedsafdeling og de øvrige supervisors.')
    lp('På BIOFOS Lynetten arbejdede jeg med forebyggende vedligehold og akut fejlfinding på pumper, HVAC, højspændingstavler og SCADA i drift døgnet rundt. På ARJ ledede jeg 12 mekanikere og teknikere i et maskinværksted med fejldiagnose og reparation af industrielle el- og mekaniske anlæg. Hos Ventek-Air planlagde jeg arbejdet for 14 medarbejdere på 11 samtidige projekter; i ELOHVAC har jeg ansvar for tilbud, materialer, underentreprenører, sikkerhed og økonomi.')
    lp('**Fra behov til afsluttet arbejde.** Jeg vil planlægge opgaven med produktionen og mekanikerne, vurdere tid og omkostninger og sikre, at opgavens materialer og ressourcer er afklaret. Arbejdsordrer og rekvisitioner skal passe til jeres SAP- og indkøbsprocesser. Under udførelsen vil jeg være til stede, løse tekniske spørgsmål sammen med holdet og følge op på interne og eksterne ressourcers sikkerhed. Efter arbejdet vil jeg samle observationer med pålidelighedsafdelingen og bruge dem til at forbedre relevante inspektionsprocedurer og arbejdsbeskrivelser.')
    lp('Jeg vil være åben om et væsentligt forhold: **Jeg har ikke de krævede tre års erfaring fra en cementfabrik**, hverken som ansat eller entreprenør. Min erfaring kommer fra teknisk drift, vedligehold, værksted og anlægsprojekter; jeres cementproces og udstyr skal jeg lære af dem, der kender fabrikken. Jeg har brugt SAP ERP til økonomi og aktiver, men konkrete arbejdsordrer i jeres SAP-opsætning skal jeg oplæres i.')
    lp('Jeres arbejdsmiljøpolitik gør sikkerhed til en del af hverdagen, og ACCSION er en planlagt del af den grønne omstilling. Det gør et solidt dagligt vedligehold vigtigt, mens produktionen udvikles. Jeg arbejder med LOTO, risikovurdering og tydelige aftaler og lægger vægt på den frie dialog, vidensdeling og frihed under ansvar, I beskriver.')
    lp('Jeg bor i Måløv og **flytter gerne til Aalborg**. Dansk er mit modersmål, og jeg arbejder professionelt på engelsk. Jeg vil gerne uddybe, hvordan min driftserfaring kan bringes i spil hos jer, selv om jeg ikke opfylder branchekravet; tiltrædelse aftales nærmere.')
    m.meta('Med venlig hilsen',after=6); m.meta('Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com',after=0)
    m.page_break(); m.resume_header(NAVN,TITEL,KONTAKT,'PROFIL — DRIFTSSIKKERHED OG MENNESKER')
    m.para('Elautoriseret maskinmester (LV/MV/HV) og B.Tech med erfaring fra teknisk drift og forebyggende vedligehold, værkstedsledelse, el-/mekanisk fejlfinding og anlægsprojekter. BIOFOS Lynetten: kritisk drift 24/7. ARJ: 12 mekanikere og teknikere. Ventek-Air: 14 medarbejdere og 11 samtidige projekter. Ingen erfaring fra cementfabrik; fabrikkens proces og udstyr skal læres.',after=35)
    m.section('VEDLIGHOLDSORDREN — FRA PLAN TIL NÆSTE INSPEKTION')
    for a,b in [('Planlægning og estimat','Afklar omfang med produktion og mekanikere, beregn tid og omkostninger og koordinér materialer, bemanding og eventuelle eksterne ydelser.'),('Sikker udførelse','Afstem adgang og sikkerhed med driften, følg virksomhedens procedurer for afbrydelse og risikovurdering, og vær til stede ved tekniske afklaringer.'),('Opfølgning og læring','Følg fremdrift og afslutning af arbejdsordrer; saml observationer og afvigelser med holdet og pålidelighedsafdelingen som input til inspektion, procedurer og pålidelighed.')]: m.bullet(a,b,after=12)
    m.section('ERHVERVSERFARING')
    jobs=[
      ('Ejer / teknisk direktør / elautoriseret maskinmester','ELOHVAC ApS · København · maj 2023–nu','8 medarbejdere inkl. 3 lærlinge · fuldt P&L',[('Service, planlægning og sikkerhed','El-, ventilations- og klimaanlæg: installation, tavler, styring, fejlfinding og forebyggende vedligehold. Planlægger materialer, underentreprenører og kvalitet; LOTO og risikovurdering ved pladsopstart.'),('Estimat og medarbejdere','Udarbejder tilbud og beregninger, leder fem elektrikere og tre lærlinge og følger op på opgaver og arbejdsmiljø. AI-understøttede værktøjer til tidsplan og kvalitet gav over 40 % produktivitetsløft.')]),
      ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen','Data Power Consultant ApS · København · 2024–nov. 2026 · sideløbende med ELOHVAC','4–10 medarbejdere · selskabet er ophørt',[('Tekniske systemer og overdragelse','Ledede AI- og AI coding-arbejde og leverede tekniske applikationer fra krav og integration til dokumenteret idriftsættelse og overdragelse.')]),
      ('Senior idriftsættelsesingeniør / projektleder, elsystem','Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024','37 samtidige anlægsprojekter · 25 specialister',[('Fremdrift og kvalitet','Koordinerede teknik, indkøb og anlæg; projekter på 2–10 mio. kr. hver. FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA med nul kritiske afvigelser ved aflevering. Brugte SAP ERP til CAPEX-budget, aktiver og omkostninger.')]),
      ('Projekt- og værkstedsleder','Ventek-Air · København · jan. 2022–nov. 2022','14 medarbejdere · 11 samtidige projekter',[('Daglig koordinering','Kapacitets- og fremdriftsstyring, underentreprenører, aftaler, sikkerhedsdokumentation og afleveringspakker. Daglige tavlemøder og flaskehalsanalyser.')]),
      ('Vedligeholdelses- og driftsleder / værkstedstekniker','BIOFOS Lynetten · København · aug. 2017–jan. 2022','Kritisk el- og mekanisk drift 24/7',[('Drift og vedligehold','Forebyggende vedligehold og akut fejlfinding på pumper, HVAC, højspændingstavler og SCADA. LOTO, risikovurdering og sikkerhed i skifteholdsdrift.'),('Reservedele og forbedring','5S, standard work og PDCA på værksted og lager samt styring af reservedele og lagerflow.')]),
      ('Elektromekaniker / produktionsteamleder','ARJ Engineering · Teheran · dec. 2003–mar. 2010','12 mekanikere og teknikere · maskinværksted',[('Mekanisk værksted','Ledelse, vagtplaner og materialestyring; fejldiagnose og reparation af industrielle el- og mekaniske anlæg med rodårsagsanalyse og korrigerende handlinger.')])]
    for title,meta,scope,bullets in jobs:
      m.job(title,meta,scope=scope)
      for a,b in bullets:m.bullet(a,b,after=10)
    m.section('UDDANNELSE, METODER OG PRAKTISK')
    for a,b in [('Elautoriseret maskinmester, LV/MV/HV','Sikkerhedsstyrelsen · maj 2023'),('B.Tech, teknologiledelse og maskinteknik','Copenhagen School of Marine and Technical Engineering · 2017–2022 · 7,6/12'),('PRINCE2 certificeret projektleder','AXELOS / PeopleCert'),('El- og maskinteknisk design, elteknik','Tehran Technical University · 2000–2003 · EQF 6'),('Køle- og ventilationsteknik','Mercantec AMU · 2021; STCW-kurser 2021–2023')]:m.edu(a,b)
    m.para('**IT:** MS Office, SAP ERP (økonomi/aktiver); lokalt ordreflow læres. **Metoder:** Lean og Six Sigma i praksis, ikke certificeret. **Sprog:** dansk, persisk og professionelt engelsk. Måløv; flytter gerne til Aalborg · kørekort B.',after=10)
    m.page_break()
    rows=[
      ('Mekanisk vedligehold, planlægning og gennemførelse','BIOFOS: forebyggende vedligehold og akut fejlfinding i 24/7-drift. ELOHVAC: planlægning af opgaver, materialer, underentreprenører og kvalitet.'),
      ('Ledelse af mekanikere og kommunikation','ARJ: ledelse af 12 mekanikere og teknikere. Ventek-Air: daglig koordinering af 14 medarbejdere; klare opgaver og opfølgning på fremdrift.'),
      ('Omkostnings- og tidsestimater','ELOHVAC: tilbud, beregninger, tidsplaner og fuldt P&L. Novo Nordisk: 37 samtidige projekter med fremdrift og økonomi på tværs af fag.'),
      ('Arbejdsordrer og rekvisitioner til reservedele, udstyr og ydelser','Materiale- og underentreprenørstyring i ELOHVAC samt reservedelsflow hos BIOFOS. SAP ERP brugt til økonomi/aktiver; lokalt ordreflow skal læres.'),
      ('Tekniske problemer ved planlægning og udførelse','Fejldiagnose og reparation af industrielle el- og mekaniske anlæg hos ARJ og akut fejlfinding på pumper og tekniske anlæg hos BIOFOS.'),
      ('Inspektionsprocedurer og pålidelighedsafdeling','BIOFOS: forebyggende vedligehold og standard work. Vil bruge fund fra mekanikere og drift til at udvikle inspektioner sammen med jeres pålidelighedsafdeling.'),
      ('Interne og eksterne ressourcer, effektivitet og sikkerhed','ELOHVAC: planlægning af medarbejdere og underentreprenører med LOTO og risikovurdering. Ventek-Air: styring af 14 medarbejdere på 11 projekter.'),
      ('Procedurer for sikkerhed, kvalitet og ensartethed','Kvalitetstjeklister, sikkerhedsopfølgning og dokumentation hos ELOHVAC; 5S og standard work i BIOFOS-værksted og lager.'),
      ('Maskinmester eller tilsvarende teknisk baggrund','Elautoriseret maskinmester (LV/MV/HV) med B.Tech i teknologiledelse og maskinteknik; teknisk grundlag i elektriske og mekaniske anlæg.'),
      ('Solid erfaring fra produktionsvirksomhed','ARJ: industrielt maskinværksted og reparation; BIOFOS: procesanlæg i kontinuerlig drift. Erfaringen er relevant, men er ikke cementproduktion.'),
      ('Mindst tre års erfaring fra cementfabrik','Jeg har ikke erfaring fra en cementfabrik som ansat eller entreprenør og opfylder derfor ikke dette krav. Cementprocessen og fabrikkens udstyr skal jeg lære.'),
      ('Dansk, teknisk engelsk, MS Office og SAP','Dansk modersmål og professionelt engelsk. MS Office og SAP ERP til økonomi, aktiver og omkostninger; SAP-vedligeholdsflow på stedet kræver oplæring.'),
      ('Tværfagligt samarbejde og ledelse i produktion','Novo Nordisk: 25 specialister på tværs af teknik, indkøb og anlæg. Ventek-Air: samarbejde om 11 projekter med medarbejdere og underentreprenører.'),
      ('Bopæl og tiltrædelse','Jeg bor i Måløv og flytter gerne til Aalborg. Tiltrædelsestidspunkt aftales; ansøgningen og CV sendes via virksomhedens hjemmeside.')]
    m.models_table('STILLINGEN — ERFARING OG TILGANG',('Krav','Dokumentation og tilgang'),rows,widths=(2500,7846))
    m.section('FØRSTE TID — LÆR ANLÆGGET OG BYG PLANEN SAMMEN')
    for t in ['Gå anlæg og sikkerhedsprocedurer igennem med mekanikerne, produktionen og pålidelighedsafdelingen; få overblik over kritiske opgaver og igangværende planer.', 'Lær SAP-arbejdsordrer og rekvisitioner, reservedele, eksterne ydelser og planlægningskadencen; aftal ansvar og opfølgning med Mechanical Manager.', 'Følg en planlagt vedligeholdsopgave fra forberedelse til afslutning og brug holdets observationer til at drøfte en konkret forbedring af inspektion eller procedure.']:m.bullet('',t,after=12)
    m.save(path)
if __name__=='__main__':
    p=os.path.join(ROOT,'Shahram_Ajloo_AalborgPortland_MechanicalSupervisor.docx');build(p);print(p)
