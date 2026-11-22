# -*- coding: utf-8 -*-
"""Energnist Kolding — jobfokuseret ansøgning og dokumenteret CV i masterdesign.
Ingen direkte affaldsforbrændings-, SRO-, kedel- eller turbineerfaring påstås.
"""
from pathlib import Path
from master_design import MasterDoc
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

R = Path(__file__).resolve().parent.parent
TEMPLATE = R / 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'
OUT = R / 'Shahram_Ajloo_Energnist_Kolding_Maskinmester.docx'
NAME = 'SHAHRAM AJLOO'
TITLE = 'Elautoriseret maskinmester | kritisk drift, vedligehold og fejlfinding'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv (Ballerup Kommune)'
DATE = '22. november 2026'

LETTER = [
 ('Et affaldsenergianlæg skal holdes stabilt gennem skiftende belastninger, alarmer og vagtskifter; beslutningen ved kontrolrummet skal kunne følges af en sikker handling og en præcis overlevering.', 'opening'),
 ('På Kolding-anlægget betyder det, at SRO-overvågning, anlæggets fysiske tilstand, sikkerhed og driftsdata skal hænge sammen. Kedel, turbine og røggasrensning er nye anlægstyper for mig. Min relevante erfaring er fra kritisk 24/7-procesdrift hos BIOFOS, hvor jeg arbejdede med SCADA-overvågning, forebyggende vedligehold og akut fejlfinding på elektriske og mekaniske installationer. Det er en overførbar driftsdisciplin – ikke erfaring med Energnists SRO eller affaldsenergiproces.', 'para'),
 ('En fast skifteholdsplan kræver, at en observation ikke stopper ved den enkelte vagt. Fejlens omfang, risici, midlertidige foranstaltninger, udført arbejde og næste kontrol skal registreres, så næste kollega kan fortsætte på et fælles faktagrundlag. Ved afvigelser må anlæggets instrukser, kompetencegrænser og eskalationsveje styre handlingen; ukendte procestrin skal læres med erfarne kolleger, før jeg tager selvstændigt ansvar for dem.', 'para'),
 ('I den daglige drift vil tilgangen være at følge anlæggets signaler og lokale driftsinstrukser, bekræfte afvigelser, vurdere konsekvenser og sikkerhed, handle inden for oplæring og mandat og dokumentere resultatet. Vedligeholdsopgaver og projektarbejde skal kobles til produktionsplanen, så adgang, risici, reservedele, test og overlevering er aftalt med de relevante fagpersoner.', 'para'),
]
SOLUTION = [
 ('Vagt og overlevering', 'Følg fast skifteholdsplan og brug en fælles logik for hændelse, anlægstilstand, beslutning, udført handling, åbne risici og næste kontrol. Lær Energnists SRO, vagtinstruks og eskalationsveje sammen med erfarne kolleger.'),
 ('Vedligehold og indgreb', 'Planlæg tekniske indgreb med driftsvinduet, arbejdssikkerheden og produktionsbehovet for øje. Afgræns opgaven, afklar isolering og ansvar, udfør kun arbejde inden for kvalifikationerne og dokumentér test, fejl og genindkobling.'),
 ('Data, orden og forbedring', 'Registrér drift og udført arbejde rettidigt i de relevante systemer, og følg op på gentagne fejl og aftalte handlinger. Hold arbejdsområdet ryddeligt og rent som del af sikker og stabil drift; bidrag til projektopgaver med praktisk teknisk koordinering.'),
]
CULTURE = ('Energnist beskriver opgaven som en del af den grønne omstilling i en fælleskommunal virksomhed med mangeartede problemstillinger og opgaver i dagligdagen. Muligheden for at præge dit arbejde og træffe beslutninger sammen med ca. 20 erfarne kolleger passer til en driftsform, hvor selvstændige observationer skal bringes ind i fællesskabets beslutninger. På vagtholdet vægter alle kompetencer for optimal drift af anlægget; alle kompetencer vægter i et hold, hvor gode kollegaer bidrager til en sikker overlevering. Indflydelse på egen arbejdstid og opgaver på disp-dage, mulighed for afspadsering og deltagelse i kurser/efteruddannelse er konkrete rammer, som Energnist selv fremhæver. Her er efteruddannelse særligt relevant for at opnå de certifikater og den anlægsspecifikke oplæring, der kræves.')
CLOSING = ('Opslaget angiver fuldtid, hurtigst mulig tiltrædelse og løbende samtaler; den konkrete startdato afklares i dialog. Jeg har ikke oplyst, om jeg har gyldigt kørekort B, kedelpassercertifikat eller truckcertifikat, og ansøgningen gør ikke krav på disse kvalifikationer. Energnist oplyser, at virksomheden kan tilrettelægge kurser til kedelpasser- og truckcertifikat, når det passer ind i den daglige arbejdsgang. En samtale kan afklare kørekortkravet, vagtplanen og den nødvendige oplæring.')
PROFILE = ('Elautoriseret maskinmester (LV/MV/HV) og B.Tech i Technology Management & Mechanical Engineering med dokumenteret erfaring fra kritisk teknisk drift, elektriske og mekaniske installationer, SCADA-overvågning, vedligehold, fejlfinding, idriftsættelse og projektkoordinering. Hos BIOFOS arbejdede jeg i et 24/7-procesanlæg med pumper, HVAC og højspændingstavler; ansvaret omfattede forebyggende vedligehold og akut fejlretning. Hos Novo Nordisk koordinerede jeg 37 samtidige CAPEX-projekter med 25 specialister og arbejdede med test og aflevering. Jeg har ikke dokumenteret SRO-, affaldsenergianlægs-, kedel-, turbine- eller røggasrensningserfaring. Energnists anlæg og systemer kræver oplæring og kvalificering.')
RESULTS = [
 ('Kritisk 24/7-drift', 'BIOFOS/Lynetten: forebyggende vedligehold og akut fejlfinding i procesmiljø.'),
 ('37 CAPEX-projekter', 'Novo Nordisk: DKK 2–10 mio. pr. projekt; koordinering på tværs af 25 specialister.'),
 ('40 % lavere energiomkostninger', 'Novo Nordisk: resultat af et PDCA-program i den pågældende organisation.'),
 ('12 medarbejdere', 'ARJ Engineering: ledelse af mekanikere og teknikere i produktionsmiljø.'),
]
EXPERIENCE = [
 ('Vedligeholdelses- og driftsleder / værkstedstekniker', 'BIOFOS (Lynetten) · København · aug. 2017 – jan. 2022', 'Kritisk 24/7-procesanlæg', [
  ('Drift og fejlfinding', 'Arbejdede med pumper, HVAC, højspændingstavler og SCADA-overvågning; udførte forebyggende vedligehold og akut fejlfinding på tekniske installationer.'),
  ('Sikkerhed og systematik', 'Anvendte LOTO, risikovurdering, APV og nærved-rapportering. Arbejdede med reservedelsflow, 5S, Standard Work og PDCA i et skifteholds- og driftsmiljø.')]),
 ('Ejer / teknisk direktør / elautoriseret maskinmester', 'ELOHVAC ApS · København · maj 2023 – nu', '5 elektrikere + 3 lærlinge · fuldt P&L', [
  ('Tekniske installationer', 'Udfører elteknisk service, fejlfinding og vedligehold på el-, ventilations- og klimaanlæg; følger op fra opgaveafgrænsning til kvalitetssikring og aflevering.'),
  ('Planlægning og koordinering', 'Planlægger opgaver, materialer og underentreprenører, leder fem elektrikere og tre lærlinge og følger arbejdsmiljø, KS og kundeleverancer.'),
  ('Digital forbedring', 'AI-understøttede værktøjer til tilbudsberegning, tidsplaner, KS-tjeklister og KPI-dashboards bidrog til et dokumenteret produktivitetsløft på over 40 %.')]),
 ('Senior idriftsættelsesingeniør / projektleder, elsystemer', 'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024', '37 CAPEX-projekter · 25 specialister', [
  ('Projektkoordinering', 'Koordinerede fremdrift, økonomi, risici og ressourcer på tværs af engineering, indkøb og anlæg; projekterne havde budgetter på DKK 2–10 mio. pr. projekt.'),
  ('Test og forbedring', 'Arbejdede med FAT/SAT og IQ/OQ/PQ; nul kritiske fund ved aflevering. Et PDCA-program reducerede energiomkostninger med 40 % i organisationen.')]),
 ('Projekt- og værkstedsleder, ventilation og klima', 'Ventek-Air · København · jan. 2022 – nov. 2022', '11 samtidige projekter · 14-personers team', [
  ('Leverance og opfølgning', 'Koordinerede team, kapacitet, fremdrift, entreprenører, sikkerhed, kvalitet og dokumentation fra planlægning til aflevering af tekniske anlægsprojekter.')]),
 ('Medejer og CTO / ansvarlig for AI-afdelingen', 'Data Power Consultant ApS · København · 2024–2026 (sideløbende)', '4–10 personer i AI- og AI coding-afdelingen', [
  ('Tekniske løsninger', 'Ledte teknisk udvikling fra kravafdækning og arkitektur til integration, test, dokumentation og overdragelse; indførte fælles standarder for review og kvalitet.')]),
 ('Elektromekaniker / produktionsteamleder', 'ARJ Engineering · Teheran · dec. 2003 – mar. 2010', '12 mekanikere og teknikere', [
  ('Produktion og vedligehold', 'Vagtplanlægning, materialestyring, målopfølgning, fejldiagnose og reparation på industrielle elektriske og mekaniske anlæg.')]),
]
EDUCATION = [
 ('B.Tech — Technology Management & Mechanical Engineering', 'Copenhagen School of Marine Engineering & Technology Management · 2017–2022'),
 ('El- og maskinteknisk design, elteknik', 'Tehran Technical University · 2000–2003'),
 ('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023'),
 ('PRINCE2 — certificeret projektleder', 'AXELOS / PeopleCert'),
 ('Køleteknik og klimaanlæg (AMU)', 'Mercantec · 2021'),
 ('STCW A-III/1 — maskinrums-/vagtkvalifikation', 'Dokumenteret maritim kvalifikation; ikke kedelpassercertifikat eller landbaseret SRO-kvalifikation.'),
]
REQUIREMENTS = [
 ('Maskinmester eller tilsvarende teknisk uddannelse', 'Elautoriseret maskinmester (LV/MV/HV) og B.Tech i Technology Management & Mechanical Engineering. Uddannelsen giver el- og maskinteknisk grundlag; den erstatter ikke anlægsspecifik oplæring eller myndighedscertifikater.'),
 ('Håndværksmæssig baggrund inden for el eller metal', 'Elautoriseret maskinmester med praktisk elteknisk service og fejlfinding hos ELOHVAC samt tidligere elektromekanisk arbejde hos ARJ. ELOHVAC omfatter installationer, tavler og styringer; ingen specifik industrielektrikeruddannelse hævdes.'),
 ('Erfaring fra procesanlæg', 'BIOFOS/Lynetten dokumenterer kritisk 24/7-procesdrift med pumper, HVAC, højspændingstavler og SCADA. Dette er relevant proceserfaring, men ikke drift af affaldsforbrænding, dampkedel, turbine eller røggasrensning.'),
 ('Fast skifteholdsplan', 'BIOFOS var et kritisk 24/7-anlæg med skifteholdsdrift og overlevering. Den konkrete Energnist-rotationsplan er ikke oplyst; vagter, tilgængelighed og praktisk tilrettelæggelse skal afklares ved samtale.'),
 ('SRO: styre kedelanlægget', 'Jeg har ikke dokumenteret SRO-styring eller kedeldrift. BIOFOS-erfaring med elektriske og mekaniske installationer er overførbar, men Energnists kedelstyring kræver oplæring, instrukser og godkendelse før betjening.'),
 ('SRO: overvåge kedelanlægget', 'BIOFOS dokumenterer SCADA-overvågning af kritiske procesinstallationer, ikke Energnists SRO eller kedelanlæg. Kedelparametre, alarmer og normale driftsbilleder skal læres med erfarne kolleger og efter anlæggets instrukser.'),
 ('SRO: fejlrette på kedelanlægget', 'Jeg har ikke dokumenteret kedelfejlfinding. Erfaring fra akut fejlfinding på andre BIOFOS-installationer giver en metode til sikker afgrænsning; konkrete kedelindgreb kræver oplæring, mandat og relevante certifikater.'),
 ('SRO: styre turbineanlægget', 'Jeg har ikke dokumenteret turbinebetjening eller SRO-styring. Overførbar erfaring med teknisk koordinering og styringsmiljøer er ikke turbinekompetence; Energnists driftssekvens og grænser skal læres og godkendes.'),
 ('SRO: overvåge turbineanlægget', 'BIOFOS-erfaring omfatter SCADA-overvågning af andre procesanlæg, men ikke dampturbiner. Turbinens parametre, alarmer og normalområde skal læres gennem Energnists oplæring og lokale driftsprocedurer.'),
 ('SRO: fejlrette på turbineanlægget', 'Jeg har ikke dokumenteret fejlfinding eller vedligehold på turbineanlæg. Generel elektrisk/mekanisk fejlretning fra BIOFOS kan overføres som metode, men turbineindgreb kræver anlægsspecifik oplæring og ansvarlig godkendelse.'),
 ('SRO: styre røggasrensningsanlægget', 'Jeg har ikke dokumenteret styring af røggasrensning eller SRO-erfaring. Min relevante erfaring er teknisk procesdrift på BIOFOS; røggasrensningens procestrin og styrelogik kræver oplæring og kvalifikation hos Energnist.'),
 ('SRO: overvåge røggasrensningsanlægget', 'BIOFOS dokumenterer SCADA-overvågning, men ikke røggasrensning. Jeg vil lære Energnists målepunkter, alarmer og driftsgrænser i samarbejde med holdet og følge gældende instrukser før selvstændig overvågning.'),
 ('SRO: fejlrette på røggasrensningsanlægget', 'Direkte fejlretning på røggasrensningsanlæg er ikke dokumenteret. Praktisk fejlfinding på andre tekniske installationer er overførbar, men anlæggets procesrisici, sikkerhed og tilladte handlinger skal læres lokalt.'),
 ('Sikre optimal drift af hele produktionsanlægget', 'BIOFOS: understøttede kontinuerlig kritisk drift med forebyggende vedligehold, akut fejlfinding og sikkerhedsrutiner. På Energnist vil driftsprioriteringer følge instrukser, holdets samlede kompetencer og oplæring i anlæggets proces.'),
 ('Indberette data til overlevering i vedligeholdelsessystem', 'BIOFOS og Novo Nordisk dokumenterer drifts-, vedligeholds- og projektopfølgning; SAP ERP, Excel og digitale værktøjer er anvendt i andre sammenhænge. Energnists specifikke vedligeholdelsessystem er ikke oplyst eller påstået kendt.'),
 ('Indberette elproduktion', 'Ingen direkte erfaring med indberetning af elproduktion er dokumenteret. Erfaring med teknisk projekt- og driftsdata samt økonomiopfølgning kan overføres til indlæring af Energnists registreringsregler, frister og datakvalitetskontrol.'),
 ('Indberette data om modtagelse af affald', 'Ingen erfaring med affaldsmodtagelse eller tilhørende registrering er dokumenteret. Jeg vil lære lokale datafelter, kontrolpunkter og overlevering sammen med ansvarlige kolleger og følge fastlagte procedurer for sporbarhed.'),
 ('Vedligeholde tekniske installationer', 'BIOFOS: forebyggende vedligehold og akut fejlretning på pumper, HVAC og elinstallationer. ELOHVAC: service og vedligehold på el-, ventilations- og klimaanlæg; sikker afgrænsning og dokumentation indgår i arbejdet.'),
 ('Deltage i projektopgaver', 'Novo Nordisk: koordinering af 37 samtidige CAPEX-projekter og 25 specialister med test og aflevering. Ventek-Air: 11 samtidige anlægsprojekter. Erfaringen er projektleverance på andre anlæg, ikke Energnist-projekter.'),
 ('Holde rent og orden i produktionsbygningen', 'BIOFOS-erfaring omfatter 5S, Standard Work og orden i værksted/lager; sikker adgang og ryddelige arbejdsområder indgik i driftsdisciplinen. Energnists rengørings- og housekeepingstandarder skal følges lokalt.'),
 ('Struktureret og analytisk tilgang til tekniske systemer', 'Fejlfinding i BIOFOS 24/7-drift krævede signal- og symptomafgrænsning, risikovurdering og opfølgning; PDCA og rodårsagsmetoder er anvendt i praksis. Metoden bruges inden for den konkrete oplæring og kompetencegrænse.'),
 ('Arbejde selvstændigt og stå ved beslutninger', 'ELOHVAC indebærer selvstændigt ansvar for tekniske opgaver, planlægning, sikkerhed og kundeleverance. I et nyt procesanlæg skal beslutningsmandat følge vagtinstruks, oplæring og eskalationsregler; selvstændighed erstatter ikke godkendelse.'),
 ('Reagere på skiftende situationer og finde praktiske løsninger', 'Akut fejlretning i BIOFOS’ 24/7-miljø og servicearbejde hos ELOHVAC dokumenterer praktisk reaktion på tekniske afvigelser. På Energnist vil løsningen afstemmes med procesrisiko, sikkerhed og ansvarlig kollega.'),
 ('Følge op på handlinger og målsætninger', 'Novo Nordisk omfattede fremdrifts-, økonomi- og risikorapportering for 37 projekter; BIOFOS omfattede vedligehold og forbedringsopfølgning. Aftalte handlinger kan følges gennem registrering, ejer, frist og kontrol af resultat.'),
 ('Samarbejde i hold med forskellige kompetencer', 'Ventek-Air: ledelse af et 14-personers team; Novo Nordisk: koordinering af 25 specialister; BIOFOS: arbejde i kritisk drift. På Energnist skal operatørernes og vedligeholdets kompetencer samles om sikker anlægsdrift.'),
 ('Gyldigt kørekort til personbil, kategori B', 'Master-CV dokumenterer ikke status for gyldigt kategori-B-kørekort, og jeg oplyser derfor ikke at have det. Opslaget gør det til en betingelse; status skal bekræftes, før en eventuel ansøgning kan vurderes som fuldt opfyldende.'),
 ('Kedelpassercertifikat eller opnå det via Energnist', 'Kedelpassercertifikat er ikke dokumenteret. STCW A-III/1 er en maritim maskinrumsvagtkvalifikation og må ikke sidestilles med kedelpassercertifikat. Energnist oplyser, at virksomheden kan arrangere kursus, når driften tillader det.'),
 ('Truckcertifikat eller opnå det via Energnist', 'Truckcertifikat er ikke dokumenteret og hævdes ikke. Energnist oplyser, at virksomheden kan arrangere kurset, hvis certifikatet mangler; eventuel truckkørsel forudsætter gennemført uddannelse og lokal godkendelse.'),
 ('Fuldtidsstilling', 'Stillingen er slået op som fuldtid. Den konkrete arbejdstids- og vagtplan bør afklares med Energnist; ingen uoplyst pendler- eller tilstedeværelsesaftale fra Måløv er lagt til grund.'),
 ('Hurtigst mulig tiltrædelse', 'Opslaget ønsker stillingen besat hurtigst muligt. Den konkrete startdato bør aftales med Energnist og er ikke fastsat i ansøgningen; der antages ikke en uoplyst rejse- eller fremmødeordning.'),
 ('Ansøgning via QuickApply', 'Energnists opslag henviser til QuickApply på Jobindex. Dette dokument er forberedte ansøgningsmaterialer og ikke en indsendelse; ingen ansøgning eller kontakt til arbejdsgiveren foretages uden udtrykkelig tilladelse.'),
 ('Frist 9. december 2026 i brugerens opslag', 'Brugerens annonce angiver 9. december 2026. Den aktuelle officielle Energnist-side, som blev undersøgt, viser ikke denne dato og siger i stedet løbende samtaler; QuickApply-portalens aktuelle status er ikke bekræftet.'),
]

def build():
    m = MasterDoc(str(TEMPLATE), lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta('Energnist · Affaldsenergianlægget i Kolding')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Maskinmester eller tilsvarende', bold=True, color='1A1A1A')
    for text, kind in LETTER:
        m.para(text, after=60 if kind == 'opening' else 50)
    for a,b in SOLUTION: m.bullet(a,b,after=32)
    m.para(CULTURE, after=45)
    m.para(CLOSING, after=45)
    m.meta('Med venlig hilsen', after=15)
    m.meta('Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com', after=0)

    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'TEKNISK PROFIL')
    m.para(PROFILE, after=45)
    m.section('DOKUMENTEREDE RESULTATER')
    for a,b in RESULTS: m.bullet(a,b,after=20)
    m.section('ERHVERVSERFARING')
    for title, meta, scope, bullets in EXPERIENCE[:4]:
        m.job(title,meta,scope=scope)
        for a,b in bullets: m.bullet(a,b,after=16)

    m.page_break()
    m.resume_header(NAME, 'Teknisk drift | vedligehold | projektleverance', CONTACT, 'ERHVERVSERFARING, UDDANNELSE OG KRAVMATCH')
    for title, meta, scope, bullets in EXPERIENCE[4:]:
        m.job(title,meta,scope=scope)
        for a,b in bullets: m.bullet(a,b,after=14)
    m.section('UDDANNELSE OG KVALIFIKATIONER')
    for a,b in EDUCATION: m.edu(a,b)
    m.para('Metoder: forebyggende vedligehold · SCADA-overvågning · fejlfinding · LOTO · risikovurdering · 5S · Standard Work · PDCA · FAT/SAT · IQ/OQ/PQ. IT: SAP ERP · Excel · Power BI · Python. Dataindberetning og vedligeholdelsessystemer: erfaring fra andre drifts- og projektmiljøer; Energnists systemer skal læres. Produktionsanlæg: erfaring fra BIOFOS’ kritiske procesanlæg; ikke affaldsenergianlæg. Kedelpasser- og gaffeltruckcertifikat er ikke dokumenteret; gaffeltruck må kun betjenes efter uddannelse og godkendelse. Energnist oplyser, at kurser kan arrangeres. Sprog: dansk og persisk (modersmål), engelsk (professionelt). Bopæl: Måløv. Kørekort B-status: ikke oplyst.', after=30, line=230, justify=False)
    m.page_break()
    m.resume_header(NAME, 'Dokumenteret erfaring og tydelige kvalifikationsgrænser', CONTACT, 'KRAV- OG EVIDENSMATRIX')
    table = m.models_table('KRAVMATRIX', ('Krav i stillingsopslaget','Dokumentation / erfaring og afgrænsning'), REQUIREMENTS, widths=(3900,6446))
    trpr = table.rows[1]._tr.get_or_add_trPr(); repeat = OxmlElement('w:tblHeader'); repeat.set(qn('w:val'),'true'); trpr.append(repeat)
    return m.save(str(OUT), title='Ansøgning og CV — Energnist Kolding, Maskinmester eller tilsvarende', subject='Maskinmester eller tilsvarende til affaldsenergianlægget i Kolding', keywords='Energnist; Kolding; maskinmester; procesdrift; vedligehold; SCADA; skiftehold; SRO')

if __name__ == '__main__': print(build())
