"""MME Nordic Product Management & R&D: employer-focused Danish letter and CV."""
import os
from master_design import MasterDoc
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAVN='SHAHRAM AJLOO'
TITEL='Product Manager · teknologi, procesudvikling og teknisk forretning'
KONTAKT='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
def build(path):
    m=MasterDoc(os.path.join(ROOT,'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='da-DK')
    m.header_banner(NAVN,TITEL,KONTAKT)
    m.meta('4. november 2026')
    m.meta('MME Nordic · Product Management & R&D · Thisted')
    p=m._p(spacing_after=80,line=260,justify=False); m._run(p,'Fra brugerbehov til produktionsplatform',bold=True,color='1A1A1A')
    def lp(t):m.para(t,after=40,line=235)
    lp('**En produktionsplatform er først en god investering, når den løser et behov, som både brugeren og fabrikken kan mærke.** For Continence og Ostomy er kvalitet og ensartethed ikke blot tekniske specifikationer: produkterne bliver en del af menneskers hverdag. Samtidig skal jeres kunder kunne producere stabilt, dokumentere løsningen og få ny teknologi i drift.')
    lp('MME Nordics ambition om at forbedre livskvaliteten for mennesker med stomi, inkontinens og andre kroniske lidelser giver et tydeligt formål til rollen. Jeg søger Product Management & R&D, fordi opgaven forbinder kundeindsigt og produktstrategi med automation, materialer og processer. Jeres arbejde med specialmaskiner, validering og kortere time-to-market kræver, at udviklingsvalg kan forklares både teknisk og forretningsmæssigt.')
    lp('**Fra brugerbehov til platform.** Jeg vil først undersøge behov og adfærd hos relevante kundesegmenter sammen med salg, kunder og tekniske specialister: Hvilke produkt- og proceskrav går igen, og hvor er der forskel? Derefter vil jeg sammenholde produktanalyse og teknologiscouting med eksisterende løsninger og udviklingsmuligheder. Et roadmap bør vise de væsentligste usikkerheder, afhængigheder og beslutningspunkter — ikke blot en liste over ideer.')
    lp('For hvert forretningsscenarie vil jeg synliggøre antagelser om kundebehov, omkostninger, teknisk risiko og tid til markedet og lade ledelsen prioritere på et gennemsigtigt grundlag. Før en løsning opskaleres, bør relevante krav og dokumentationsbehov afklares med specialisterne. På den måde kan strategisk prioritering føre til et konkret forsøg, en beslutning om at fortsætte — eller et velbegrundet nej.')
    lp('Jeg kan bidrage med en ingeniørfaglig B.Tech i teknologiledelse og maskinteknik, praktisk erfaring med el, styring og tekniske anlæg samt projektstyring af 37 samtidige CAPEX-projekter hos Novo Nordisk. Her arbejdede 25 specialister på tværs af engineering, indkøb og anlæg med FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA; ved aflevering var der nul kritiske afvigelser. I Data Power omsatte jeg kundekrav til tekniske applikationer og brugte AI-assisteret design med faglig kontrol. I ELOHVAC bygger jeg på samme kombination af teknisk arbejde, kalkulation og kundebehov.')
    lp('Min baggrund er ikke et bevis på flere års selvstændigt ejerskab af en MedTech-produktportefølje eller på direkte udvikling af stomi- og kontinensprodukter. Jeg bringer derimod erfaring fra reguleret produktion, tekniske styringer og digital udvikling; de konkrete produkter, materialer og medico-standarder vil jeg lære sammen med jeres specialister. Treårskravet skal derfor vurderes på min erfaring med automation og teknisk udvikling, ikke på en opdigtet produktmanager-titel.')
    lp('Jeres fokus på ansvar, kvalitet, innovation og en åben og ærlig omgangstone passer til en udviklingsproces, hvor antagelser må kunne udfordres, og både kunden og fagfolkene bliver hørt. Jeg bor i Måløv og **flytter gerne til Thisted**. Jeg vil gerne drøfte, hvilke beslutninger der er vigtigst for jeres Continence- og Ostomy-platforme i den kommende tid.')
    m.meta('Med venlig hilsen',after=6);m.meta('Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com',after=0)
    m.page_break();m.resume_header(NAVN,TITEL,KONTAKT,'PROFIL — PRODUKT, PROCES OG FORRETNING')
    m.para('Elautoriseret maskinmester (LV/MV/HV), B.Tech i teknologiledelse og maskinteknik samt PRINCE2-certificeret projektleder. Kombinerer tekniske styringer, reguleret projektlevering og kundevendte digitale løsninger med kalkulation og fuldt P&L. Medico-produktledelse og direkte udvikling af stomi-/kontinensprodukter er ikke dokumenteret erfaring; reguleret produktion og teknisk udvikling er den overførbare basis.',after=35)
    m.section('PRODUKTBESLUTNINGEN — MIN TILGANG')
    for a,b in [('Kunde og marked','Indsaml markedsindsigt og segmentér efter behov og adfærd; undersøg forskelle mellem kundens proceskrav og slutbrugerens behov.'),('Produkt og teknologi','Kombinér produktanalyse med teknologiovervågning og dialog med R&D om materialer, automation, dokumentation og mulige teknologiplatforme.'),('Scenarie og roadmap','Beskriv alternativer, antagelser, risiko og omkostninger; prioritér med ledelsen og omsæt beslutningerne til et roadmap med klare næste skridt.'),('Projekt og læring','Afprøv antagelser i passende skala og følg op på kvalitet og dokumentation med tekniske specialister, inden en løsning udvikles videre.')]:m.bullet(a,b,after=10)
    m.section('ERHVERVSERFARING')
    jobs=[
      ('Ejer / teknisk direktør / elautoriseret maskinmester','ELOHVAC ApS · København · maj 2023–nu','8 medarbejdere inkl. 3 lærlinge · fuldt P&L',[('Teknik og forretning','Ansvar for kundebehov, tilbud, kalkulation, projektplanlægning og kvalitet ved el-, ventilations- og klimaanlæg. Arbejder med installation, tavler, styring og fejlfinding.'),('Digital procesudvikling','Udviklede AI-understøttede værktøjer til tilbud, tidsplaner, kvalitetstjek og KPI; dokumenteret produktivitetsløft over 40 %.')]),
      ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen','Data Power Consultant ApS · København · 2024–nov. 2026 · sideløbende med ELOHVAC','4–10 medarbejdere · selskabet er ophørt',[('Fra krav til teknisk løsning','Implementerede tekniske og industrielle applikationer: krav, arkitektur, integration, idriftsættelse og dokumenteret overdragelse.'),('AI-assisteret design','Anvendte AI coding til beregning, dimensionering og designvarianter af tekniske anlæg og industrielle komponenter; faglig validering før levering.')]),
      ('Senior idriftsættelsesingeniør / projektleder, elsystem','Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024','37 samtidige CAPEX-projekter · 25 specialister',[('Reguleret teknisk leverance','Fremdrift, budget og risici på projekter på 2–10 mio. kr.; FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA, nul kritiske afvigelser ved aflevering.'),('Tekniske systemer','El-tavler, styring og UPS; tværfaglig koordinering mellem engineering, indkøb og anlæg og månedlig rapportering.')]),
      ('Projekt- og værkstedsleder','Ventek-Air · København · jan. 2022–nov. 2022','14 medarbejdere · 11 samtidige anlægsprojekter',[('Fra specifikation til aflevering','Planlægning, aftalegrundlag, underentreprenører og dokumentation; daglige tavlemøder og opfølgning på fremdrift.')]),
      ('Vedligeholdelses- og driftsleder / værkstedstekniker','BIOFOS Lynetten · København · aug. 2017–jan. 2022','Drift 24/7 · pumper · HVAC · SCADA',[('Styring og proces','Forebyggende vedligehold og fejlfinding på el- og mekaniske anlæg; 5S, standard work og PDCA i værksted og lager.')]),
      ('Elektromekaniker / produktionsteamleder','ARJ Engineering · Teheran · dec. 2003–mar. 2010','12 mekanikere og teknikere · maskinværksted',[('Industriel teknik','Ledelse, materialestyring, fejldiagnose og reparation af industrielle el- og mekaniske anlæg med rodårsagsanalyse.')])]
    for title,meta,scope,bullets in jobs:
      m.job(title,meta,scope=scope)
      for a,b in bullets:m.bullet(a,b,after=9)
    m.page_break()
    m.section('UDDANNELSE OG PRAKTISK')
    for a,b in [('B.Tech, teknologiledelse og maskinteknik','Copenhagen School of Marine and Technical Engineering · 2017–2022 · 7,6/12'),('Elautoriseret maskinmester, LV/MV/HV','Sikkerhedsstyrelsen · maj 2023'),('PRINCE2 certificeret projektleder','AXELOS / PeopleCert'),('El- og maskinteknisk design, elteknik','Tehran Technical University · 2000–2003 · EQF 6'),('Køle- og ventilationsteknik','Mercantec AMU · 2021; STCW-kurser 2021–2023')]:m.edu(a,b)
    m.para('**Metoder:** Lean og Six Sigma anvendt i praksis, ikke certificeret; PDCA, VSM og FMEA. **IT:** Excel, SAP ERP, Python og Claude API. **Sprog:** dansk og persisk modersmål; professionelt engelsk. Måløv; flytter gerne til Thisted · kørekort B.',after=15)
    rows=[
      ('Markedsindsigt','Kundeforståelse og kravarbejde fra ELOHVAC og Data Power; vil samle markedsindsigt fra kunder, salg og R&D før strategiske beslutninger.'),
      ('Produktanalyse og materialer','Teknisk analyse af anlæg og komponenter, herunder AI-assisterede designvarianter med faglig kontrol. Stomi- og kontinensmaterialer skal læres med specialister.'),
      ('Teknologiscouting og teknologiovervågning','Anvendt AI coding og tekniske applikationer i praksis. Vil kortlægge relevante automationsteknologier og sammenligne modenhed, integration og dokumentationsbehov.'),
      ('Produktstrategi, roadmaps og teknologiplatforme','Forretnings- og teknisk ledelse med eget P&L; vil sammen med ledelsen omsætte behov og tekniske valg til prioriterede roadmaps. Direkte porteføljeejerskab er ikke dokumenteret.'),
      ('Forretningsscenarier og strategisk prioritering','Tilbud, kalkulation og økonomistyring i ELOHVAC; 37 projekter med økonomi og risici hos Novo. Vil opstille alternativer med tydelige antagelser og beslutningspunkter.'),
      ('Kundesegmentering efter behov og adfærd','Erfaring med kravafdækning hos kunder. Metoden vil være at undersøge behov og anvendelse med kunder og salg; formel segmenteringsledelse er ikke dokumenteret.'),
      ('Ingeniøruddannelse eller tilsvarende','Opslaget søger ingeniør eller tilsvarende: B.Tech i teknologiledelse og maskinteknik, elautoriseret maskinmester og el- og maskinteknisk design.'),
      ('3+ års produktudvikling, automation eller MedTech','Tekniske styringer og processer fra BIOFOS og ELOHVAC samt applikationsudvikling hos Data Power. Selvstændig produktudviklings- eller MedTech-portefølje er ikke dokumenteret.'),
      ('Projektstyring','PRINCE2 certificeret; 37 samtidige Novo-projekter og 11 Ventek-Air-projekter med ansvar for fremdrift, ressourcer og teknisk koordinering.'),
      ('Praktisk og analytisk arbejde','El- og mekanisk fejlfinding, installation og styring kombineret med beregninger, kvalitetstjek, KPI og AI-assisteret design med faglig validering.'),
      ('MedTech, automation og medico-teknisk forståelse','Reguleret pharma-erfaring med GMP/FDA/EMA, FAT/SAT og IQ/OQ/PQ; styring og SCADA fra teknisk drift. Direkte udvikling af medico-produkter er ikke dokumenteret.'),
      ('Samarbejde med globale kunder, kvalitet og innovation','Kundekrav og leverancer i Data Power og ELOHVAC; 25 specialister koordineret hos Novo. Vil afklare krav, dokumentation og tekniske valg med MME og kunden.'),
      ('Bopæl og tiltrædelse','Baseret i Måløv; flytter gerne til Thisted. Tiltrædelse aftales nærmere. Kontaktperson ifølge opslaget: Kenneth Ørbæk Rasmussen.')]
    m.models_table('STILLINGEN — ERFARING OG TILGANG',('Krav','Dokumentation og tilgang'),rows,widths=(2500,7846))
    m.section('FØRSTE TID — FRA INDSIGT TIL ET BESLUTNINGSGRUNDLAG')
    for t in ['Lær Continence- og Ostomy-produkter, maskiner, kunder og dokumentationskrav med R&D, salg og ledelse; afdæk igangværende prioriteringer.', 'Vælg et afgrænset behov, kortlæg segmenter og relevante teknologier, og saml antagelser om materialer, proces, omkostninger og risiko.', 'Præsentér et sammenligneligt beslutningsgrundlag og foreslå næste undersøgelse eller afprøvning samt placering på et roadmap.']:m.bullet('',t,after=10)
    m.save(path)
if __name__=='__main__':
    p=os.path.join(ROOT,'Shahram_Ajloo_MMENordic_ProductManager.docx');build(p);print(p)
