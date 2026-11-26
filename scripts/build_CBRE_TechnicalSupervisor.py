# -*- coding: utf-8 -*-
"""Technical Supervisor — CBRE Global Workplace Solutions (dansk opslag, Job ID 303099, 29-10-2026).

Dansk opslag -> dansk dokument, 4 sider i masterdesign: brev side 1, CV side 2-3, kravmatrix side 4.
Opslaget navngiver ingen kontaktperson (ansøgning via rekrutteringsportal) -> generisk hilsen
"Kære rekrutteringsteam hos CBRE Global Workplace Solutions,".

STILVALG (style_guard godkendt, 3/3 skift):
  register     = Løsninger der virker i praksis (tillid · tilstedeværelse · sikker drift ·
                 tydelig kommunikation · mange bolde i luften)
  åbningsgreb  = AU (brugerne ser ikke installationerne; de ser hverdagen. Bygningen før
                 systemet, det der ikke går i stykker, som målestokken)
  struktur     = På stedet, på planen, hos kunden (tilstedeværelse · vedligehold · kundedialog)

BRUGERENS KORREKTION + permanent regel: alt tekst humaniseret, menneskeskrevet i brev OG CV.
Ingen em dash. Navne kun fra leveret materiale (ingen navngiven kontakt i opslaget).

EVIDENSGRÆNSER: el, ventilation og klima er hovedspor; VVS-nære sider (pumper, rør, varme)
dokumenteres fra Biofos-drift og Novo-commissioning — ingen påstand om VVS-autorisation.
Engelsk skrives "professionelt" (masterord), ikke "flydende".
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'CBRE GWS · Technical Supervisor'
BANNER_RESUME = 'Teknisk drift på flere sites · el, ventilation og service'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('25. november 2026')
    m.meta('CBRE Global Workplace Solutions · Technical Supervisor til sites på Sjælland')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Technical Supervisor til flere sites på Sjælland', bold=True, color='1A1A1A')
    m.para('Kære rekrutteringsteam hos CBRE Global Workplace Solutions,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('Brugerne i en bygning ser sjældent en teknisk installation. De ser, om lyset virker, '
       'om der er varmt nok, og om døren åbner. Resten står på runderingslister og i '
       'serviceaftaler, og et sted derimellem ligger jobbet som Technical Supervisor: at '
       'hverdagen bare kører, på flere sites, uden at nogen rigtig lægger mærke til det. '
       'Sådan et mål kan jeg lide at arbejde efter.')

    lp('I søger en kollega til stabil og velfungerende teknisk drift hos en af jeres vigtigste '
       'kunder, og rollen er til at få øje på: være tæt på driften på flere af kundens sites '
       'på Sjælland, så bygninger og installationer fungerer optimalt i hverdagen, og være '
       'kundens faste tekniske kontaktperson på stedet. Som I selv skriver, er kunden en af '
       'vores vigtigste kunder, og den tillid tager jeg alvorligt. Globalt leverer CBRE Global '
       'Workplace Solutions (GWS) facilities management og drift til nogle af verdens største '
       'virksomheder; jeg kommer fra en verden, hvor anlægget ikke måtte stå stille, og hvor '
       'løsninger, der virker i praksis, var hele pointen. Den tekniske nøgleperson ude på '
       'stedet har jeg været før: på et renseanlæg, der kørte døgnet rundt, og på '
       'erhvervsbygninger, hvor el, ventilation og klima skulle virke, dagen efter håndværkeren '
       'var kørt.')

    lp('Min faglige bund er el: elektriker fra bunden, elautoriseret maskinmester i dag, og '
       'tekniske installationer, fx el, VVS og ventilation, har jeg rørt ved siden 2003. '
       'VVS-nære ting, pumper, rør og varme, kender jeg fra driften på renseanlægget og fra '
       'procesanlæg hos Novo Nordisk. Solid teknisk forståelse og lyst til at tage ansvar '
       'passer på den måde, jeg arbejder på: løsningsorienteret, selvstændig og vant til '
       'mange bolde i luften. En dag i ELOHVAC kunne være et akut udkald om morgenen, et '
       'tilbud over middag og en snak med en underentreprenør inden fyraften. At skabe tillid '
       'hos både kunder, kollegaer og samarbejdspartnere har ikke været en overskrift, men '
       'den eneste måde at få serviceaftaler til at holde på.')

    lp('Der er intet i opslaget, jeg behøver pynte på. Jeg arbejder struktureret og bevarer '
       'overblikket, når flere sites trækker på samme dag, og sikkerhedsdelen kender jeg: '
       'LOTO, APV og risikovurdering fra driften og GMP-afleveringer hos Novo Nordisk, altid '
       'i overensstemmelse med gældende lovkrav og myndighedskrav. Kørekort (B) har jeg, '
       'jeg bor i Måløv, og jeg er indstillet på kørsel mellem lokationer på Sjælland, også '
       'i de perioder, hvor det fylder en del. Dansk er mit modersmål, og engelsk har været '
       'arbejdssproget i internationale forløb siden 2017, skriftligt og mundtigt. Én ærlig '
       'ting mere: jeres kundes sites og systemer kender jeg ikke endnu. De første uger er '
       'netop til det.')

    lp('Det, der trækker, er kombinationen: en global organisation med fokus på din udvikling '
       'og alligevel en hverdag, der er lokal og konkret ude hos kunden. Et stærkt fagligt '
       'fællesskab med plads til sparring og erfaringsudveksling, og en selvstændig og '
       'varieret hverdag, hvor jeg selv lægger ruten mellem adresserne. Høje ambitioner, '
       'stærkt samarbejde og løsninger, der virker i praksis, er også en beskrivelse af det, '
       'jeg gerne vil levere: hurtig og tydelig kommunikation i hverdagen, KPI-rapportering, '
       'der kan bruges til noget, og konkrete forslag til forbedringer og optimeringer. '
       'Input til, hvordan driften kan forbedres, må meget gerne komme fra mig.')

    lp('De første 90 dage har jeg skrevet som en plan side 3 i CV\'et: stederne først, så '
       'planen og aftalerne, og til sidst forbedringerne hos kunden. Jeg kan tiltræde '
       'hurtigst muligt, og jeg er klar til at referere direkte til Contract Manager, som '
       'stillingen lægger op til. Ansøgningen går gennem jeres portal, som I beder om, og jeg '
       'svarer gerne på spørgsmål inden da.', after=44)

    m.para('Med venlig hilsen', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Driftsorienteret teknisk supervisor med elautoriseret maskinmester i hånden og elektrikerfaget i '
           'bunden. El, ventilation og klima på erhvervsbygninger, 24/7-drift på forsyningsanlæg '
           'og commissioning af procesanlæg hos Novo Nordisk. Vant til at være den faste '
           'tekniske kontakt på stedet, følge op på vedligehold og holde kunder informeret, '
           'også når svaret ikke er færdigt endnu. Kører gerne mellem sites.', after=32)

    m.section('ERHVERVSERFARING')
    m.job('CTO for AI-afdelingen og elautoriseret maskinmester (el-teknik og ventilation)',
          'Data Power Consultant ApS · København · 2024 – nu (fra nov. 2026 også ELOHVACs '
          'el-tekniske aktiviteter)',
          scope='AI-afdeling 4-10 personer · el-service og entreprise · 5 elektrikere + 3 lærlinge')
    m.bullet('El-service og fejlfinding', 'Erhvervskunder med aftaler: tavler, styring, automatik '
             'og forebyggende vedligehold på el, ventilation og klima. Akutte udkald løst på '
             'stedet, opfølgning skrevet ned bagefter.', after=10)
    m.bullet('Ledelse og opfølgning', 'AI-afdelingen med 4 til 10 personer, investeringstilbud og '
             'månedlig KPI-opfølgning. KPI-analyse og beslutningsoplæg klargjort med AI-værktøjer, '
             'før mødet begyndte.', after=10)

    m.job('Ejer / teknisk direktør / elautoriseret maskinmester',
          'ELOHVAC ApS · København · maj 2023 – nov. 2026 (virksomheden lukket)',
          scope='Erhvervskunder · el, ventilation og klima · entreprise · fuldt P&L · serviceaftaler')
    m.bullet('Service og vedligehold', 'Drift og vedligehold fra akutte udkald til afleveret anlæg: '
             'installation, tavler, styring og fejlfinding på el, ventilation og klima. '
             'Forebyggende og afhjælpende vedligehold i faste aftaler med responstid, kvalitet og '
             'leveringsevne som mål.', after=10)
    m.bullet('Kunder og aftaler', 'Faste erhvervskunder, tilbud og opmåling, underentreprenører og '
             'servicepartnere i ugentlig kontakt. Budgetansvar og vedligeholdsplanlægning hørte '
             'med; tillid var det, der fik aftalerne fornyet.', after=10)
    m.bullet('Personale', '5 elektrikere og 3 lærlinge: daglig planlægning, 1:1 og MUS, '
             'arbejdsmiljøopfølgning og struktureret oplæring på skiftende adresser.', after=10)

    m.job('Senior commissioningeniør / projektleder, el-systemer',
          'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
          scope='37 CAPEX-projekter, DKK 2-10 mio. · 25 specialister · GMP/FDA/EMA')
    m.bullet('Commissioning', 'Procesanlæg idriftsat og testet efter FAT/SAT og IQ/OQ/PQ under '
             'GMP/FDA/EMA, nul kritiske fund ved afleveringen. Fejlfinding på el og styring '
             'undervejs, A3 og 5xHvorfor, når noget skulle findes på plads.', after=10)
    m.bullet('Planlægning og rapportering', 'Idriftsættelsesforløb med test og aflevering, '
             'månedsrapport om fremdrift, økonomi, risici og ressourcer til ledelse og bygherre, '
             'og 25 specialister på tværs af engineering, indkøb og drift. SAP ERP.', after=10)

    m.job('Projekt- og værkstedsleder', 'Ventek-Air · København · jan. 2022 – nov. 2022',
          scope='11 samtidige projekter · 14 mand · underleverandører · lager og logistik')
    m.bullet('Koordinering', '11 samtidige projekter og et team på 14 mand. Udbud og tilbud, '
             'aftalegrundlag, underentreprenører og sikkerhedsdokumentation fulgt til dørs, '
             'daglige tavler for kapacitet og fremdrift.', after=10)

    m.job('Vedligeholdelses- og driftsleder / værkstedstekniker',
          'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
          scope='24/7-drift · SCADA, PLC, HV-tavler · skiftehold')
    m.bullet('Drift på stedet', 'Drift, overvågning og vedligehold af pumper, HVAC, HV-tavler, '
             'SCADA og PLC døgnet rundt. Planlagt og korrigerende vedligehold, fejlfinding på '
             'stedet, og 5S og Standard Work i værkstedet.', after=10)
    m.bullet('Sikkerhed og vagt', 'Skiftehold og rådighedsvagt med tilkald, LOTO, APV og '
             'nærved-hændelser. Produktionen kørte videre, når noget blev skiftet om natten.',
             after=10)

    m.job('Elektromekanisk tekniker / produktionsleder', 'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
          scope='12 mekanikere og teknikere · maskinværksted · produktlinje')
    m.bullet('Hold og fejlsøgning', 'Ledelse af 12 mekanikere og teknikere: vagtplan, materialer '
             'og mål. Fejlsøgning på industrielt udstyr, analyse af rodårsag og korrigerende '
             'handlinger, der blev fulgt op.', after=10)

    m.section('UDDANNELSE OG CERTIFIKATER')
    m.edu('B.Tech (EQF6), teknologiledelse og maskinteknik',
          'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12')
    m.edu('Dansk elautorisation LV/MV/HV som elautoriseret maskinmester', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('El- og maskinteknisk design, elteknik (EQF6)', 'Tehran Technical University · 2000–2003')
    m.edu('PRINCE2, certificeret projektleder', 'AXELOS / PeopleCert')
    m.edu('Køleteknik og klimaanlæg (AMU)', 'Mercantec · 2021 · STCW 2021–2023, Søfartsstyrelsen')

    m.section('KOMPETENCER')
    m.bullet('Drift på stedet', 'Bygninger og installationer i daglig drift: el, ventilation, klima, '
             'styring, pumper og rør. Opgaverne løses på tværs af fag, med tekniske runderinger og '
             'opfølgning i systemer.', after=10)
    m.bullet('Vedligehold og tilsyn', 'Forebyggende og afhjælpende vedligehold efter plan, '
             'tilsyn med underleverandører og sikkerhed, der holder for lovkrav og myndighedskrav.',
             after=10)
    m.bullet('Kunder og aftaler', 'Faste tekniske kontaktroller, hurtig og tydelig kommunikation, '
             'aftaler og serviceaftaler med mål på responstid og kvalitet.', after=10)
    m.bullet('Systemer og værktøjer', 'SAP ERP, SCADA, PLC, Power BI og Python. Digitale '
             'tjeklister og KPI-opfølgning bygget i huset. Lean- og Six Sigma-praksis uden '
             'certifikat: DMAIC, 5S, PDCA, VSM, A3, Kaizen, Standard Work, SMED, TPM, 5xHvorfor, '
             'Ishikawa og FMEA.', after=10)

    m.section('DE FØRSTE 90 DAGE')
    m.para('En plan for de første 90 dage, skrevet så I kan holde mig op på den:', after=8)
    m.bullet('Dag 1-30 · På stedet', 'Alle lokationer gået igennem, teknikere og underleverandører '
             'mødt, systemerne til registrering lært. Mål: jeg kan lave en fuld teknisk '
             'rundering på hvert site selv og kende status på vedligeholdsplanen.', after=10)
    m.bullet('Dag 31-60 · På planen', 'Forebyggende og afhjælpende vedligehold fulgt op, aftaler '
             'med underleverandører gennemgået (korrekt, til tiden, efter aftale), sikkerhed og '
             'lovkrav på plads. Mål: fælles overblik over vedligeholdet på tværs af sites.',
             after=10)
    m.bullet('Dag 61-90 · Hos kunden', 'KPI-rapportering sat i system, fast rytme for kontakt og '
             'forbedringsforslag sat i gang. Mål: ét konkret forslag til forbedringer og '
             'optimeringer med målbar effekt.', after=10)

    m.section('SPROG, VÆRKTØJER OG PRAKTISK')
    m.para('Sprog: dansk (modersmål, flydende skrift og tale) · engelsk (professionelt, dagligt '
           'arbejdssprog i internationale projekter siden 2017) · persisk (modersmål). SAP ERP, '
           'SCADA, PLC, Power BI og Python. PRINCE2. Kørekort kategori B (manuelt gear). Bor i '
           'Måløv og kører mellem sites på Sjælland. Kan tiltræde hurtigst muligt.', after=32)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('CBRE Global Workplace Solutions · krav og dokumentation',
                   ('Krav i opslaget', 'Dokumenteret erfaring'),
                   [
        ('stabil og velfungerende teknisk drift',
         'Driftsleder for et renseanlæg, der kørte døgnet rundt (2017-2022): pumper, HVAC, '
         'HV-tavler og SCADA holdt kørende gennem skiftehold og tilkald. Stabil drift har '
         'været målet i alle mine job siden, også som servicepartner for erhvervskunder.'),
        ('fejlfinding og løse tekniske problemer',
         'Fejlfinding på el, automatik og mekanik siden 2003, fra akutte udkald hos ELOHVACs '
         'kunder til fejldiagnose på industrielle anlæg hos ARJ. A3, 5xHvorfor og Ishikawa, '
         'når fejlen skal findes hurtigt og ikke komme igen.'),
        ('forebyggende og afhjælpende vedligehold efter den fastlagte plan',
         'Planlagt og korrigerende vedligehold i faste intervaller: serviceaftaler med faste '
         'runderinger som ejer (2023-2026), forebyggende vedligehold på renseanlægget og SAP '
         'ERP til opfølgning hos Novo Nordisk. Planen er et værktøj, ikke en hindring.'),
        ('Koordinere og føre tilsyn med underleverandører',
         'Underentreprenører og leverandører koordineret i entreprise siden 2023, og som '
         'projektleder hos Ventek-Air var aftalegrundlag og sikkerhedsdokumentation min del af '
         '11 parallelle projekter. Tilsyn betyder at være derude, ikke at ringe dagen efter.'),
        ('gennemføre tekniske runderinger',
         'Sikkerhedsrunderinger og daglige tavler gennem årene, og som driftsleder gik jeg '
         'anlægget igennem på hvert skift i 4,5 år. Tekniske runderinger registreret i tjeklister og '
         'systemer, i dag også digitale, bygget i Python.'),
        ('registrere opgaver og observationer i vores systemer',
         'Opgaver og observationer registreret i SAP ERP hos Novo Nordisk, i serviceaftalernes '
         'dokumentation som ejer og i egne digitale tjeklister og rapportflow siden 2024. '
         'Systemerne skal gøre opfølgningen lettere, ikke tungere.'),
        ('hurtig og tydelig kommunikation med kunden',
         'Hurtig og tydelig kommunikation praktiseret som kundens faste ansigt hos ELOHVACs '
         'erhvervskunder: hurtig og ærlig besked, når noget går galt, og en aftale om næste '
         'skriftlige del fra Novo Nordisk (2022-2024), hvor månedsrapportering gik til bygherre.'),
        ('i overensstemmelse med gældende lovkrav og myndighedskrav',
         'LOTO, APV, risikovurdering og nærved-hændelser som fast disciplin på Biofos og ved '
         'pladsopstart i ELOHVAC, og GMP-afleveringer under FDA/EMA-krav hos Novo Nordisk. Nul '
         'kritiske afvigelser i serviceaftalerne og ved aflevering i 4,5 års drift.'),
        ('KPI-rapportering',
         'KPI-dashboards bygget som ejer på responstid, kvalitet og leveringsevne i '
         'serviceaftalerne, og KPI-analyse i ledelsesarbejdet i Data Power. KPI-rapportering '
         'skal kunne bruges til at handle på; siden 2023 har jeg fulgt op på den slags hver måned.'),
        ('forslag til forbedringer og optimeringer',
         'PDCA-forløb med 40% lavere energiomkostninger hos Novo Nordisk, 5S og Standard Work '
         'på værkstedet hos Biofos, og digitale arbejdsgange med over 40% produktivitetsløft i '
         'ELOHVAC. Forslag ender i noget, der kører i hverdagen.'),
        ('solid teknisk forståelse og lyst til at tage ansvar',
         'Elautoriseret maskinmester (LV/MV/HV) med elektrikergrunduddannelsen i bunden: tavler, '
         'styring, automatik og fejlfinding siden 2003. Ansvar har fulgt med i hvert job, '
         'senest hele den el-tekniske aktivitet i Data Power.'),
        ('løsningsorienteret, selvstændig',
         'Akutte udkald løst på stedet hos erhvervskunder i 3+ år, og som ejer var der ikke en '
         'leder at spørge. Løsningsorienteret betyder at komme tilbage med en løsning, der '
         'virker, og ikke med en forklaring.'),
        ('mange bolde i luften',
         '11 samtidige projekter hos Ventek-Air, 37 CAPEX-projekter hos Novo Nordisk og drift, '
         'tilbud og personale samtidig i ELOHVAC. Mange bolde i luften er en arbejdsform, jeg '
         'kender godt, og taber jeg en, siger jeg det med det samme.'),
        ('skabe tillid hos både kunder, kollegaer og samarbejdspartnere',
         'Serviceaftaler med faste erhvervskunder byggede på tillid: det samme sjak kom igen, '
         'og aftalerne blev fornyet. Som projektleder var tillid til kolleger og '
         'underentreprenører det, der fik 14 mand til at trække samme vej.'),
        ('tekniske installationer, fx el, VVS og ventilation',
         'El og ventilation/klima er mine hovedspor fra ELOHVAC og Ventek-Air, og de VVS-nære '
         'ting, pumper, rør og varme, har jeg fra driften på renseanlægget (2017-2022) og fra '
         'procesanlæg '
         'hos Novo Nordisk. El er hele min faglige bund.'),
        ('bosat i København eller omegn',
         'Jeg bor i Måløv og har arbejdet i København og omegn siden 2017. Turen '
         'ind til byen eller ud til et site er en del af hverdagen, ikke et problem der skal '
         'løses.'),
        ('kørsel mellem lokationer på Sjælland',
         'Kortet har fulgt mig siden 2003, og daglig kørsel mellem kunder, byggepladser og '
         'leverandører i alle mine job. Jeg er indstillet på kørsel mellem lokationer på Sjælland, '
         'også når '
         'det fylder en del i perioder.'),
        ('kommunikerer flydende på dansk og engelsk',
         'Mit modersmål er dansk, og engelsk har været arbejdssproget i mine internationale '
         'projekter siden 2017: GMP-dokumentation, møder og skriftlig aflevering. Jeg '
         'kommunikerer klart og tydeligt på begge sprog, i tale og på skrift.'),
        ('arbejder struktureret og bevarer overblikket',
         'PRINCE2, daglige tavler og faste dokumentationsrutiner har været mine redskaber siden '
         '2017. Overblikket i en rodet situation kom jeg først rigtigt i skole med hos Biofos, '
         'når noget skulle skiftes om natten, og alle kiggede på mig.'),
        ('kørekort (B)',
         'Kørekort kategori B (manuelt gear) siden 2003 og brugt dagligt mellem arbejdspladser, '
         'dagligt mellem arbejdspladser, kunder og anlæg. Den er et af de værktøjer, jeg regner '
         'med at bruge mellem jeres adresser.'),
        ('teknisk drift, ejendomsdrift eller Facility Management',
         'Teknisk drift og service på erhvervsbygninger siden 2023: el, ventilation og klima, '
         'aftaler og opfølgning som ejer af ELOHVAC. Før det drift og vedligehold på et '
         'forsyningskritisk anlæg i 4,5 år, og commissioning på procesanlæg.'),
        ('den tekniske nøgleperson ude på flere af kundens sites',
         'På Biofos var jeg i 4,5 år den, vagtholdet kaldte på, når anlægget drillede, og hos Novo '
         'Nordisk den faste tekniske bro mellem entreprenører og drift. Rollen som den, der '
         'står med svaret ude på stedet, kender jeg godt.'),
        ('input til, hvordan driften kan forbedres',
         'Som ejer så jeg, at de bedste forslag kom fra folk tæt på opgaven, og jeg har selv '
         'lagt forslag frem med målbar effekt: 40% lavere energiomkostninger hos Novo Nordisk og '
         'arbejdsgangene i værkstedet hos Biofos.'),
                   ], widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo — ansøgning som Technical Supervisor, CBRE Global '
                       'Workplace Solutions')
    print(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_CBRE_TechnicalSupervisor.docx'))
