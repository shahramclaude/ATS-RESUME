# -*- coding: utf-8 -*-
"""Driftsmester til Helsingør Kraftvarmeværk — Forsyning Helsingør (dansk opslag, frist 30.11.2026).

Dansk opslag -> dansk dokument, 4 sider i masterdesign: brev side 1, CV side 2-3, kravmatrix side 4.
Kontaktpersoner fra opslaget (må bruges): Driftsmester Frederik Thygaard (24790719),
afdelingsleder René August Bruun (21121633), HR-ansvarlig Mia Hartzbech (48405109).

STILVALG (style_guard godkendt, 3/3 skift mod #418):
  register     = Forsyningskritisk hverdag (stabil drift · forsyningssikkerhed · driftsstabilitet
                 · faglighed, ansvar og samarbejde · rådighedsvagt)
  åbningsgreb  = AT (vejrudsigt og varmebehov som ugens første arbejdsredskab: produktions-
                 planlægningen begynder med, hvad byerne skal bruge)
  struktur     = De tre anlæg (biomasse · gas · el) — værkets tre produktionssystemer som rygrad

BRUGERENS KORREKTION + permanent regel: alt tekst humaniseret, menneskeskrevet i brev OG CV.
Ingen em dash.

EVIDENSGRÆNSER (brugerbekræftelse 25.11.2026): kedelpassercertifikat A og gasautorisation B-4
har kandidaten IKKE — vil erhverve efter ansættelse (opslaget tillader det). Skrives ærligt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Helsingør Kraftvarmeværk · Driftsmester'
BANNER_RESUME = 'Drift og optimering af kraftvarmeværk · maskinmester'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('25. november 2026')
    m.meta('Forsyning Helsingør · Driftsmester til Helsingør Kraftvarmeværk')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Driftsmester til Helsingør Kraftvarmeværk', bold=True, color='1A1A1A')
    m.para('Kære Frederik Thygaard og René August Bruun,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('En uge på et kraftvarmeværk begynder med en vejrudsigt. Hvor meget varme skal der til '
       'Hornbæk og Hørsholm, hvornår er der mest brug for systemydelser til elnettet, og hvilket '
       'af de tre anlæg, biomasse, gas og el, skal bære hvornår. Produktionsplanlægning af '
       'varme- og elproduktion på tværs af biomasse-, gas- og elanlæg ser måske ud som et '
       'regneark udefra, men det er et dagligt valg mellem driftsstabilitet, økonomi og '
       'forsyningssikkerhed. Det valg vil jeg gerne stå for.')

    lp('I skriver, at stabil drift og grøn udvikling går hånd i hånd, og det er netop '
       'sammenhængen på jeres biomasse- og gasturbinebaserede kraftvarmeværk, der leverer '
       'fjernvarme fra Hornbæk til Hørsholm samt el og systemydelser til elnettet. '
       'Produktionen med bæredygtig biomasse og elbaserede varmeløsninger gør værket til en '
       'del af den grønne omstilling og en sikker energiforsyning. Drift, '
       'overvågning og optimering med fokus på høj forsyningssikkerhed og driftsstabilitet er '
       'en disciplin, jeg kender, bare ikke fra kraftvarme endnu: jeg kommer fra et renseanlæg, '
       'der kørte døgnet rundt med SCADA, PLC, HV-tavler og pumper, og fra commissioning af '
       'procesanlæg hos Novo Nordisk. Anlæg, der ikke måtte stå stille, har jeg arbejdet med '
       'siden 2017.')

    lp('Profilen, I beskriver, er næsten min: maskinmester med faglig grunduddannelse som '
       'elektriker. Elautorisation LV/MV/HV fra Sikkerhedsstyrelsen, elektriker og '
       'elektromekaniker fra bunden, '
       'og erfaring fra procesindustri, energianlæg eller lignende tekniske produktionsmiljøer '
       'i form af Novo Nordisk og Biofos. El, automatik, styringer og teknisk fejlsøgning, som '
       'I kalder en fordel, bruger jeg hver dag: tavler, styring, SCADA, PLC og '
       'fejlsøgning på tværs af mekanik og el. Selvstændigt ansvar for udvalgte anlægsområder '
       'har jeg båret før, som driftsleder med vedligeholdsplanlægning og budgetansvar og som '
       'teknisk direktør med leverandørsamarbejde og aftaler med eksterne servicepartnere.')

    lp('De formelle krav skal jeg også være ærlig om. Kedelpassercertifikat A og '
       'gasautorisation B-4 har jeg ikke endnu, men viljen til at erhverve certificeringerne '
       'efter ansættelse er der, og jeg tager dem som en del af jobbet. Kørekort kategori B '
       'har jeg. Rådighedsvagtordningen kender jeg fra skiftehold og tilkald på Biofos, også '
       'efter oplæring, når telefonen går. Sikkerhedsgodkendelse har jeg arbejdet på kritisk '
       'forsyningsinfrastruktur og GMP-kontrollerede projekter i årevis og forventer ingen '
       'problemer i en godkendelse. Og da jeres kommunikation foregår på dansk, er det mit '
       'modersmål, og jeg taler og skriver flydende dansk.')

    lp('Det, der trækker mest ved stillingen, er to ting i opslaget: kort vej fra idé til '
       'beslutning, og at faglighed, ansvar og samarbejde er afgørende for en stabil og '
       'bæredygtig energiforsyning. Sådan har jeg arbejdet på et renseanlæg, hvor '
       'beslutningerne skulle tages midt i driften, og i en virksomhed, jeg selv drev. Et '
       'erfarent driftsteam bestående af maskinmestre og faglærte specialister er også et godt '
       'sted at lande; jeg lærer gerne af folk, der har været på værket længere end mig. Og et '
       'multiforsyningsselskab der leverer el, vand og varme og nyttiggør ressourcer i affald '
       'og spildevand i en cirkulær økonomi. At I er aktive i den grønne omstilling, er en '
       'sammenhæng, jeg kan se mig selv i. Nordsjælland kører jeg gerne til, det har jeg gjort '
       'i årevis.')

    lp('De første 90 dage står som en plan side 3 i CV\'et: de første 30 dage går med at komme '
       'med i driften '
       'og lære anlæggene og vagtmandskabet at kende, derefter tager jeg '
       'vedligeholdsplanlægningen og anlægsområderne, og til sidst kommer optimeringsforslag og '
       'tekniske standarder. Jeg kan tiltræde hurtigst muligt, og to samtalerunder med '
       'personlighedstests passer mig fint; en grundig proces har jeg intet imod. Mine '
       'kontaktoplysninger står øverst, og jeg svarer gerne på spørgsmål inden da. Løn efter '
       'kvalifikationer og overenskomst mellem KL og relevant fagforening er fint med mig.',
       after=44)

    lp('Med venlig hilsen', after=8)
    lp('Shahram Ajloo', after=8)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Driftsprofil med maskinmesterbaggrund og elektrikergrunduddannelsen i bunden. '
           '24/7-drift og vedligehold på renseanlæg med SCADA, PLC, HV-tavler og pumper, '
           'commissioning af procesanlæg hos Novo Nordisk under GMP/FDA/EMA, og el-teknisk '
           'drift og fejlsøgning som elautoriseret maskinmester. Produktionsplanlægning, '
           'vedligeholdsplanlægning og budgetansvar har jeg ført før, og el, automatik, '
           'styringer og fejlsøgning i daglig brug.', after=32)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester (el-teknik og ventilation)',
         'Data Power Consultant ApS · København · 2024 – nu',
         'AI-afdeling 4-10 personer · el-service og entreprise · 5 elektrikere + 3 lærlinge',
         [('', 'Leder AI-afdelingen med 4 til 10 personer: tilbud, kunder, og hvordan løsninger '
               'bliver bygget og dokumenteret. Investeringstilbud og månedlig KPI-opfølgning.'),
          ('', 'El-service og fejlsøgning hos erhvervskunder: tavler, styring, automatik og '
               'forebyggende vedligehold på el, ventilation og klima.')]),
        ('Ejer / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 – nov. 2026 (virksomheden lukket)',
         'Erhvervskunder · el, ventilation og klima · entreprise · fuldt P&L',
         [('', 'Drift og vedligehold fra akutte udkald til afleveret anlæg: installation, '
               'tavler, styring og fejlsøgning på el, ventilation og klima. Budgetansvar og '
               'vedligeholdsplanlægning i serviceaftaler.'),
          ('', 'Personaleledelse af 5 elektrikere og 3 lærlinge: daglig planlægning, 1:1 og MUS. '
               'Samarbejde med leverandører og eksterne servicepartnere hver uge.')]),
        ('Senior commissioningeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, DKK 2-10 mio. · 25 specialister · GMP/FDA/EMA',
         [('', 'Commissioning og projektledelse på 37 CAPEX-projekter, DKK 2-10 mio. pr. stk. '
               'Procesanlæg idriftsat og testet efter FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA, '
               'nul kritiske fund ved afleveringen.'),
          ('', 'Planlægning og gennemførelse af idriftsættelsesforløb med test og aflevering, '
               'månedsrapport om fremdrift, økonomi, risici og ressourcer, og 25 specialister '
               'på tværs af engineering, indkøb og drift. SAP ERP.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022 – nov. 2022',
         '11 samtidige projekter · 14 mand · lager og logistik',
         [('', '11 samtidige projekter og et team på 14 mand. Daglige tavler for kapacitet og '
               'fremdrift, sikkerhedsdokumentation og afleveringspakker i hvert projekt.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · SCADA, PLC, HV-tavler · skiftehold',
         [('', 'Drift, overvågning og vedligehold af pumper, HVAC, HV-tavler, SCADA og PLC '
               'døgnet rundt. Planlagt og korrigerende vedligehold, fejlsøgning, og 5S og '
               'Standard Work i værkstedet.'),
          ('', 'Skiftehold og rådighedsvagt med tilkald, LOTO, APV og nærved-hændelser. '
               'Produktionen kørte videre, når noget blev skiftet om natten.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('', 'Ledelse af 12 mekanikere og teknikere i maskinværksted: vagtplan, materialer og '
               'mål. Fejlsøgning på industrielt udstyr, analyse af rodårsag og korrigerende '
               'handlinger.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('UDDANNELSE OG CERTIFIKATER')
    m.edu('B.Tech (EQF6), teknologiledelse og maskinteknik',
          'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12')
    m.edu('Dansk elautorisation LV/MV/HV som elautoriseret maskinmester',
          'Sikkerhedsstyrelsen · maj 2023')
    m.edu('El- og maskinteknisk design, elteknik (EQF6)',
          'Tehran Technical University · 2000–2003')
    m.edu('PRINCE2, certificeret projektleder', 'AXELOS / PeopleCert')
    m.edu('Køleteknik og klimaanlæg (AMU)',
          'Mercantec · 2021 · STCW 2021–2023, Søfartsstyrelsen')
    m.para('Lean- og Six Sigma-praksis uden certifikat: DMAIC, 5S, PDCA, VSM, A3, Kaizen, '
           'Standard Work, SMED, TPM, 5xHvorfor, Ishikawa og FMEA, brugt i dokumenteret arbejde '
           'med vedligehold, kvalitet og planlægning.', after=48)

    m.section('SPROG, VÆRKTØJER OG PRAKTISK')
    m.para('Dansk (modersmål, flydende skrift og tale) · engelsk (professionelt) · persisk '
           '(modersmål). SAP ERP, SCADA, PLC, Power BI og Python til driftsdata og opfølgning, '
           'PRINCE2 til projektstruktur. Kørekort kategori B. Bor i Måløv og kører gerne til '
           'opgaver i Nordsjælland. Kan tiltræde hurtigst muligt.', after=48)

    m.section('KOMPETENCER')
    for label, body in [
        ('Drift og anlæg',
         'Drift, overvågning og optimering af procesanlæg med fokus på forsyningssikkerhed og '
         'driftsstabilitet. El, automatik, styringer og teknisk fejlsøgning på tværs.'),
        ('Vedligehold',
         'Planlagt og korrigerende vedligehold, fejlsøgning og vedligeholdsplanlægning med '
         'budgetansvar. LOTO, APV og risikovurdering som fast rutine.'),
        ('Ledelse og samarbejde',
         'Selvstændigt ansvar for anlægsområder og tæt tværfagligt samarbejde. Teams fra 3 til '
         '25 personer, leverandører og eksterne servicepartnere.'),
        ('Systemer og data',
         'SCADA, PLC, SAP ERP, Power BI og Python. Data brugt til at prioritere og følge op på '
         'driftens effektivitet.'),
    ]:
        m.bullet(label, body, after=10)

    m.section('DE FØRSTE 90 DAGE')
    m.para('En plan for de første 90 dage, som I kan holde mig op på:', after=12)
    for b in [
        'Dag 1-30: Ind i driften. Gå med i driftsteamet på alle tre anlæg, biomasse, gas og el, '
        'lære rådighedsvagten at kende og gennemgå de udvalgte anlægsområder. Mål: jeg kan '
        'tage en vagtrunde selv.',
        'Dag 31-60: Ansvar og planlægning. Vedligeholdsplanlægning og budgetopfølgning for '
        'mine anlægsområder, samarbejde med leverandører og servicepartnere sat i system, og '
        'revisioner planlagt. Mål: ingen akut opgave overrasker to gange.',
        'Dag 61-90: Optimering og standarder. Forslag til driftsrutiner, arbejdsgange og '
        'tekniske standarder, og deltagelse i udviklings- og investeringsprojekter. Mål: ét '
        'konkret optimeringsforslag med målbar effekt.',
    ]:
        m.bullet('', b, after=10)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Forsyning Helsingør · Driftsmester · krav og dokumentation',
                   ('Krav i opslaget', 'Dokumenteret erfaring'), [
        ('Produktionsplanlægning af varme- og elproduktion på tværs af biomasse-, gas- og '
         'elanlæg',
         'Produktions- og driftsplanlægning på tværs af anlægstyper i 24/7-drift (Biofos, '
         '2017-2022): pumper, HVAC, HV-tavler, SCADA og PLC i én plan. Planlægning af el, '
         'ventilation og klima på tværs af kunder siden 2023. Biomasse og gasturbine er nye '
         'anlæg for mig; planlægningsdisciplinen er den samme.'),
        ('Drift, overvågning og optimering af kraftvarmeværkets produktionsanlæg med fokus på '
         'høj forsyningssikkerhed og driftsstabilitet',
         '4,5 års drift og overvågning af et forsyningskritisk anlæg døgnet rundt (2017-2022) '
         'med SCADA og PLC som øjne. Optimering dokumenteret: PDCA-forløb med 40% lavere '
         'energiomkostninger. Stabilitet målt som oppetid i skiftehold og tilkald.'),
        ('Vedligehold, fejlsøgning og optimering',
         'Planlagt og korrigerende vedligehold siden 2003. Fejlsøgning på el, automatik og '
         'mekanik med A3, 5xHvorfor og Ishikawa som systematik. Optimering gennem 5S og '
         'Standard Work i værkstedet og digitale værktøjer siden 2024.'),
        ('Planlægning og gennemførelse af revisioner',
         'Større tekniske forløb planlagt og gennemført: idriftsættelse og aflevering af 37 '
         'anlægsprojekter (2022-2024) med protokoller, test og godkendelse, og planlagte '
         'vedligeholdsstop på Biofos, hvor anlægget skulle tilbage i drift til tiden.'),
        ('Budgetansvar og vedligeholdsplanlægning',
         'Fuldt P&L-ansvar 2023-2026 med månedlig budgetopfølgning, og vedligeholdsplanlægning '
         'i serviceaftaler med faste intervaller. 37 projekter på DKK 2-10 mio. styret på '
         'økonomi i SAP ERP.'),
        ('Samarbejde med leverandører og eksterne servicepartnere',
         'Leverandøraftaler og underentreprenørstyring siden 2023, servicepartnere i daglig '
         'kontakt på Biofos (kompressorer, køl, el) i 4,5 år, og forhandlinger om aftaler og '
         'priser som direktør.'),
        ('Deltagelse i tekniske udviklings- og investeringsprojekter samt implementering af '
         'nye energi- og procesløsninger',
         'Investeringsprojekter vurderet og gennemført: 37 CAPEX-projekter (2022-2024), '
         'solcelleanlæg i installationsregi, og energiløsninger med målt 40% lavere '
         'energiomkostninger. Nye løsninger implementeret i drift, ikke kun testet.'),
        ('Bidrag til udvikling af driftsrutiner, arbejdsgange og tekniske standarder',
         '5S, Standard Work og driftsrutiner udviklet i værkstedet (2017-2022), fælles '
         'arbejdsgange indført på tværs af to selskaber (2023-2026), og digitale standarder '
         '(tjeklister og rapportflow) bygget i Python og Claude siden 2024.'),
        ('Deltagelse i værkets rådighedsvagt sammen med det øvrige driftsteam',
         'Skiftehold og tilkaldsvagt på Biofos i 4,5 år (2017-2022): vagttelefonen gik også om '
         'natten, og arbejdet blev delt med holdet. Rådighedsvagt ca. hver 6. uge kender jeg '
         'rytmen i.'),
        ('arbejder struktureret og løsningsorienteret',
         'Struktureret: PRINCE2, daglige tavler og faste rutiner for dokumentation. '
         'Løsningsorienteret: akutte udkald løst på stedet i 3+ år og fejlsøgning, der ender '
         'i en løsning og ikke i en rapport.'),
        ('tager ansvar og handler, når driften udfordres',
         'Driftsleder for et anlæg, der kørte døgnet rundt, med beslutninger taget midt i '
         'situationen (2017-2022). Overblik i komplekse driftsmiljøer har været en del af '
         'jobbet siden 2017, og som ejer med fuldt P&L-ansvar var der heller ingen at skubbe '
         'beslutningen over på.'),
        ('kan arbejde selvstændigt og samtidig indgå i et tæt tværfagligt samarbejde',
         'Selvstændigt: driftsmand med eget ansvarsområde på skift. Tværfagligt: 25 specialister '
         'på tværs af engineering, indkøb og drift (2022-2024), og el, VVS/ventilation og '
         'automatik i samme sjak siden 2023.'),
        ('kommunikerer klart og professionelt med kolleger, leverandører og samarbejdspartnere',
         'Klar kommunikation på tværs af faggrupper siden 2003: elektrikere, ingeniører, '
         'produktion og kunder. Som projektleder broen mellem specialister og ledelse; som '
         'direktør forhandlinger med leverandører og samarbejdspartnere på dansk og engelsk.'),
        ('erfaring med el, automatik, styringer og teknisk fejlsøgning',
         'Elautoriseret maskinmester (LV/MV/HV) med 20+ års erfaring: el, automatik (PLC, '
         'styringer) og teknisk fejlsøgning siden 2003. SCADA, HV-tavler og instrumentering '
         'fra drift og commissioning. Redskaberne er i brug hver dag.'),
        ('Kedelpassercertifikat A og gasautorisation B-4 eller vilje til at erhverve '
         'certificeringerne efter ansættelse',
         'Ærligt: certifikaterne har jeg ikke endnu, og jeg er indstillet på at erhverve '
         'kedelpassercertifikat A og gasautorisation B-4 efter ansættelse. Jeg har lært nye '
         'certificeringer før (elautorisation 2023, STCW 2021-2023) og tager dem alvorligt.'),
        ('Kørekort kategori B',
         'Kørekort kategori B (manuelt gear) og brugt dagligt i job siden 2003 mellem '
         'arbejdspladser og anlæg, også til længere ture i Nordsjælland og på Sjælland.'),
        ('Mulighed for at opnå og opretholde sikkerhedsgodkendelse',
         'Jeg har arbejdet på kritisk forsyningsinfrastruktur (Biofos, 2017-2022) og '
         'GMP-kontrollerede projekter med baggrundskontrol (Novo Nordisk, 2022-2024) og '
         'forventer ingen problemer i en sikkerhedsgodkendelse.'),
        ('Deltagelse i værkets rådighedsvagtordning (ca. hver 6. uge efter oplæring)',
         'Vagtordning og tilkald kendt fra 4,5 års skiftehold (2017-2022) og ansvar for '
         'beredskab som direktør. Ca. hver 6. uge efter oplæring passer mig; det er færre '
         'vagter end i skifteholdet.'),
        ('Da vores interne og eksterne kommunikation foregår på dansk, er det et krav, at du '
         'taler og skriver flydende dansk',
         'Dansk er mit modersmål, og jeg har skrevet ansøgninger, rapporter og dokumentation '
         'på dansk i alle danske job siden 2017. Flydende dansk i skrift og tale, også med '
         'fagteknisk ordforråd.'),
    ], widths=(3400, 6946), compact=True)
    m.para('**Spørgsmål kan rettes til Driftsmester Frederik Thygaard på 24 79 07 19 eller '
           'afdelingsleder René August Bruun på 21 12 16 33. Jeg kan træffes på +45 93 99 95 '
           '14 eller ajlooshahram@gmail.com.**', after=8)

    m.save(path, title='Driftsmester Helsingør Kraftvarmeværk - Forsyning Helsingør')
    print(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_HelsingorForsyning_DriftsmesterKraftvarmevaerk.docx'))
