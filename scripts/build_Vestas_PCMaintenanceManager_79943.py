# -*- coding: utf-8 -*-
"""Preventive & Corrective Maintenance Manager — Vestas, Nakskov, req 79943
(blandet opslag: engelsk kerne + dansk boilerplate -> DANSK dokument, brugerens valg).

4 sider i masterdesign: brev side 1, CV side 2-3, kravmatrix side 4.
Intet kontaktnavn i opslaget -> "Kære ansættende leder,". Rekvisitions-id 79943.
Full onsite i Nakskov; lejlighedsvis støtte uden for normal arbejdstid.

SAMME-FIRMA-REGLER: Vestas er genansogning (adskillige tidligere: HeadOfAnalytics,
HeadVPMS, InstallationSupervisor, OffshoreTeamLeader, ProcessLead m.fl.) ->
intet genbruges; alt indhold skrevet friskt til 79943.

STILVALG (style_guard godkendt, 3/3 skift mod #435 NNE):
  register    = Vedligehold der bærer produktionen (sikkerhed · stabilitet ·
                løbende forbedring)
  åbningsgreb = BL (uret der aldrig står stille: en fabrik der kører 24/7 har
                ingen stille timer)
  struktur    = Stabilitet, kapabilitet, kultur (30/60/90 = stabiliteten ·
                kapabiliteten · kulturen)

BRUGERSVAR 26.11 (bindende): Dansk dokument (trods engelsk jobkerne). Nakskov ->
"kan flytte til omraadet hvis jobbet er rigtigt" (Lystrup/Kalundborg-moenstret).
MTBF, MTTR, OEE, spare parts availability + CMMS = REEL erfaring -> skriv
selvsikkert (brugerens eget svar).

MASTER-REGLER: "elautoriseret maskinmester (LV/MV/HV)" — aldrig "elinstallatør".
BANNED: "demonstrated ability"/"demonstreret" citeres aldrig (JD'ens
"Demonstrated leadership experience" parafraseres i rk9-label). Marine Engineering
(B.Tech fra Copenhagen School of Marine Engineering & Technology Management) er
JD'ens foretrukne baggrund — reel og stærk.

BRUGERENS KORREKTION: humaniseret brev OG CV. Ingen em dash. Ingen forbudte ord.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Vestas · Preventive & Corrective Maintenance Manager, Nakskov'
BANNER_RESUME = 'Vedligehold · ledelse · døgndrift · sikkerhed · forbedring'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('26. november 2026')
    m.meta('Rekvisitions-id 79943 · Produktion · Nakskov')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Preventive & Corrective Maintenance Manager, Nakskov',
           bold=True, color='1A1A1A')
    m.para('Kære ansættende leder,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('En fabrik der kører 24/7 har ingen stille timer. Hver gang et anlæg står '
       'stille, bliver det målt i tabt produktion, og der bliver vedligeholdet enten '
       'bærer linjen eller bremser den. Et 24/7 manufacturing environment stiller '
       'krav til hver time, og safe, stable, and efficient operations er ikke et '
       'mål men et vilkår. At lede vedligeholdsorganisationen i Nakskov med det '
       'for øje er opgaven jeg søger.')

    lp('Vestas er energibranchens globale partner inden for bæredygtige '
       'energiløsninger, og I er specialister i at designe, producere, installere og '
       'servicere vindmøller over hele verden, både onshore og offshore. Mere end 200 '
       'GW vindkapacitet installeret over hele verden og 40+ års erfaring indenfor '
       'vindenergi har gjort jer til pionerer inden for vind, og 39.000 ansatte '
       'løfter opgaven sammen: at #PowerTheSolution. Rollen ligger i Production '
       'Engineering under Head of Production Engineering, med 2 Maintenance '
       'Supervisors og cirka 40 Maintenance Technicians i organisationen, og tæt '
       'samarbejde med Production, Quality, HSE, Logistics og Operational Excellence.')

    lp('Min indgang er driftsiden. Equipment availability skabes gennem forebyggende '
       'og korrigerende vedligehold med rytme, og de sidste seks år som '
       'vedligeholdelsesleder i døgndrift gav mig disciplinen: pumper, HVAC, '
       'procesrør, SCADA og PLC holdt kørende på skiftehold. MTBF, MTTR, OEE og '
       'reservedelstilgængelighed har jeg fulgt som faste måltal, og maintenance '
       'planning, documentation, and CMMS data der er korrekte og strukturerede er '
       'for mig en selvfølge, ikke et projekt. Fabrikkens Safety, Quality, Delivery, '
       'Cost, and People-mål kender jeg fra samme type styring.')

    lp('Eksterne entreprenører og facility service providers har jeg styret på '
       'aftaler og standarder, og KPI-styring med omkostningskontrol og klare '
       'prioriteringer er måden en vedligeholdsafdeling kører på i praksis. '
       'Løbende forbedring af udstyrets ydeevne, effektivitet og procesoptimering '
       'er ikke et sideprojekt hos mig; det er forskellen på at slukke brande og at '
       'drive fabrik. Lean Manufacturing og Root Cause Analysis har jeg i hænderne, '
       'fra rodårsagsanalyser der ændrede fejlhåndteringen til PDCA, 5S og Standard '
       'Work i hverdagen.')

    lp('Sikkerhedskulturen er fundamentet under det hele: HSE standards, '
       'permit-to-work systems og LOTO procedures kender jeg fra anlæg der aldrig '
       'sover, hvor arbejdstilladelser og risikovurderinger hørte til hvert skift. '
       'Som leder skaber jeg engagement og ansvarlighed, balancerer den direkte '
       'tekniske involvering med det strategiske blik, og træffer beslutninger på '
       'data og driftsprioriteringer. Jeg kommunikerer lige så klart med folkene '
       'på gulvet som med ledelsen, og fokus på sikkerhed, kvalitet og løbende '
       'forbedring slipper jeg ikke.')

    lp('Baggrunden er maskinmester og maritim teknik: B.Tech fra Copenhagen School '
       'of Marine Engineering & Technology Management, og Marine Engineering var '
       'endda det foretrukne på kravlisten. Sproget er på plads: dansk og engelsk '
       'i skrift og tale. Stillingen er full onsite i Nakskov, og jeg kan flytte til området '
       'hvis jobbet er rigtigt, også når der er brug for støtte uden for normal '
       'arbejdstid. Vestas værdier om mangfoldighed, lighed og inklusion og målet '
       'om en bæredygtig, grøn energifremtid trækker, og fabrikken på Lolland '
       'gør det ikke mindre. Jeg ser frem til samtalen.', after=44)

    m.para('Med venlig hilsen', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Vedligeholdsleder med 20+ års erfaring fra tekniske anlæg i produktion '
           'og døgndrift. Forebyggende og korrigerende vedligehold styret på KPI-mål '
           'som MTBF, MTTR, OEE og reservedelstilgængelighed, CMMS-data der holder, '
           'og teams ledet tæt på gulvet. Maskinmester med maritim ingeniør-'
           'baggrund (B.Tech, Marine Engineering), LOTO og permit-to-work som '
           'daglig disciplin, og Root Cause Analysis frem for gentagne fejl.',
           after=32)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester (el-teknik og ventilation)',
         'Data Power Consultant ApS · København · 2024 – nu (fra nov. 2026 også ELOHVACs '
         'el-tekniske aktiviteter)',
         'AI-afdeling 4-10 personer · el-service og entreprise · 5 elektrikere + 3 lærlinge',
         [('Teknik og teams', 'El-service og entreprise med anlægsdrift på kundesiden, '
           'planlægning og aflevering styret fra tilbud til idriftsættelse. Teams på '
           '4-10 specialister ledet tæt på opgaverne, og beslutninger truffet på data '
           'frem for mavefornemmelser.')]),
        ('Ejer / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 – nov. 2026 (virksomheden lukket)',
         'Erhvervskunder · el, ventilation og klima · entreprise · fuldt P&L · serviceaftaler',
         [('Drift og økonomi', 'Serviceaftaler på tekniske anlæg drevet med '
           'forebyggende vedligehold som omdrejningspunkt, KPI-mål i aftalerne og '
           'omkostningskontrol på hver sag. 5 elektrikere og 3 lærlinge, og eksterne '
           'leverandører styret på kontrakt.'),
          ('Planlægning', 'Vedligeholdsplaner og dokumentation holdt ajour, så '
           'fejl blev fundet før de blev til stop. Engagerede medarbejdere og klare '
           'ansvarsfordelinger var vejen til stabil drift.')]),
        ('Senior commissioningeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, DKK 2-10 mio. · 25 specialister · GMP/FDA/EMA',
         [('Anlæg og dokumentation', '37 projekter med commissioning, test og '
           'idriftsættelse (FAT/SAT, IQ/OQ/PQ), og dokumentation der holdt til '
           'revision. Performance management på fremdrift og kvalitet, og 25 '
           'specialister på tværs af engineering, indkøb og drift.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022 – nov. 2022',
         '11 samtidige ventilationsprojekter · 14 mand · underleverandører',
         [('Entreprenørstyring', '11 samtidige projekter med 14 mand, og eksterne '
           'entreprenører holdt på aftaler, sikkerhed og kvalitet. Planlægning, '
           'fremdrift og omkostninger fulgt pr. projekt, og prioriteringer sat '
           'efter driftsbehov.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · kritiske anlæg · 10 medarbejdere · skiftehold',
         [('Vedligehold i døgndrift', 'Forebyggende og korrigerende vedligehold af '
           'kritiske anlæg døgnet rundt: pumper, HVAC, procesrør, SCADA og PLC. '
           'MTBF, MTTR og oppetid fulgt som måltal, reservedelsstyring i orden, og '
           'CMMS-data vedligeholdt løbende. LOTO, arbejdstilladelser og '
           'risikovurderinger på tværs af skiftehold, og fejl fundet før de blev '
           'til stop.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('Produktion og rodårsager', 'Produktionsafdeling med 12 mekanikere og '
           'teknikere: vedligehold af maskiner, reservedele og planlægning. '
           'Rodårsagsanalyser der ændrede fejlhåndteringen, og engagement og '
           'ansvarlighed bygget op i teamet.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('UDDANNELSE OG CERTIFIKATER')
    m.edu('B.Tech (EQF6), teknologiledelse og maskinteknik',
          'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12')
    m.edu('Dansk elautorisation LV/MV/HV som elautoriseret maskinmester', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('El- og maskinteknisk design, elteknik (EQF6)', 'Tehran Technical University · 2000–2003')
    m.edu('PRINCE2, certificeret projektleder', 'AXELOS / PeopleCert')
    m.edu('Køleteknik og klimaanlæg (AMU)', 'Mercantec · 2021 · STCW 2021–2023, Søfartsstyrelsen')

    m.section('KOMPETENCER')
    m.bullet('Vedligehold og anlæg', 'Forebyggende og korrigerende vedligehold af '
             'pumper, HVAC, procesrør, tavler, SCADA og PLC. Reservedelsstyring, '
             'planlægning og dokumentation som en del af driften, og anlæg der '
             'holdes kørende i døgndrift.', after=10)
    m.bullet('KPI-styring og CMMS', 'MTBF, MTTR, OEE og reservedelstilgængelighed '
             'som faste måltal. CMMS-data vedligeholdt, så planlægning og '
             'performance management bygger på tal der passer. Omkostningskontrol '
             'og klare prioriteringer i en travl hverdag.', after=10)
    m.bullet('Sikkerhed og HSE', 'LOTO, permit-to-work (arbejdstilladelser), APV og '
             'risikovurderinger fra anlæg der aldrig sover. Robust sikkerhedskultur '
             'bygget på rutiner der følges, ikke på skilte.', after=10)
    m.bullet('Ledelse', 'Teams fra 10 til 25 personer ledet med engagement og '
             'ansvarlighed, beslutninger på data og driftsprioriteringer, og klar '
             'kommunikation både til gulvet og til ledelsen. Skiftehold og '
             'supervisor-strukturer er velkendt terræn.', after=10)
    m.bullet('Lean og forbedring', 'Root Cause Analysis som metode, rodårsagsanalyser i praksis, PDCA, 5S '
             'og Standard Work. Procesoptimering og '
             'løbende forbedring som arbejdsform, ikke som kampagne.', after=10)

    m.section('DE FØRSTE 90 DAGE')
    m.para('Planen følger ansvaret: stabiliteten, kapabiliteten, kulturen.', after=8)
    m.bullet('Dag 1-30 · Stabiliteten', 'Organisationen lært at kende: de 2 '
             'Maintenance Supervisors, teknikerne, de kritiske anlæg og '
             'CMMS-datagrundlaget. Mål: jeg kender holdet og anlæggene, og de '
             'straks-farlige forhold er håndteret.', after=10)
    m.bullet('Dag 31-60 · Kapabiliteten', 'Vedligeholdsplaner og KPI-baseline på '
             'plads (MTBF, MTTR, OEE, reservedelstilgængelighed), og '
             'entreprenørstyringen strammet. Mål: planlægningen kører, og '
             'måltallene er synlige for teamet.', after=10)
    m.bullet('Dag 61-90 · Kulturen', 'Løbende forbedring forankret med de første '
             'forbedringsprojekter, Root Cause Analysis som fast rutine, og '
             'sikkerhedsarbejdet sat i system på tværs af skift. Mål: færre '
             'gentagne fejl, og et team der løfter i flok.', after=10)

    m.section('SPROG, VÆRKTØJER OG PRAKTISK')
    m.para('Dansk (modersmål) · engelsk (professionelt) · persisk (modersmål). '
           'CMMS-systemer, SAP ERP, Excel, Microsoft Project; PRINCE2. Kørekort '
           'kategori B (manuelt gear). Bosat i Måløv; kan flytte til Nakskov-'
           'området hvis jobbet er rigtigt. Tiltrædelse aftales.', after=32)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Preventive & Corrective Maintenance Manager, Vestas · krav og dokumentation',
                   ('Krav i opslaget', 'Dokumenteret erfaring'),
                   [
        ("Manage and develop the factory's maintenance organization, including 2 "
         'Maintenance Supervisors and approximately 40 Maintenance Technicians',
         'Ledelse og udvikling af tekniske organisationer siden 2003: 10 medarbejdere '
         'på skiftehold (Biofos 2017-2022), 12 mekanikere og teknikere (ARJ '
         '2003-2010), 14 mand (Ventek 2022) og 25 specialister (Novo 2022-2024). '
         '42 mand med 2 supervisors er næste skridt i samme disciplin, og '
         'supervisor-laget har jeg selv været tæt på som skifteholdsleder.'),
        ('Improve equipment availability and operational stability through effective '
         'preventive and corrective maintenance practices',
         'Udstyrstilgængelighed har været mit mål i seks år i døgndrift (Biofos '
         '2017-2022): forebyggende planer, korrigerende indsatser og fejl fundet '
         'før de blev til stop. Pumper, HVAC, procesrør, SCADA og PLC holdt '
         'kørende på skiftehold, og oppetiden fulgt uge for uge.'),
        ('Ensure maintenance planning, documentation, and CMMS data are accurate, '
         'structured, and aligned with operational needs',
         'Planlægning, dokumentation og CMMS-data i orden som en del af driften: '
         'vedligeholdsplaner, reservedelslister og registreringer vedligeholdt '
         'løbende (Biofos 2017-2022), og dokumentation der holdt til revision '
         '(Novo 2022-2024). Data skal passe før de bruges.'),
        ('Manage external contractors and facility service providers while ensuring '
         'compliance with safety, quality, and performance standards',
         'Eksterne entreprenører styret siden 2003: underentreprenører på aftaler '
         'og deadlines (Ventek 2022, ELOHVAC 2023-2026) og leverandører i drift '
         '(Biofos 2017-2022). Compliance med sikkerhed, kvalitet og performance '
         'aftalt på forhånd og fulgt op på stedet.'),
        ('Improve performance by managing KPIs, controlling costs, and setting clear '
         'priorities for resources and activities',
         'KPI-styring som fast rutine: MTBF, MTTR, OEE og reservedels-'
         'tilgængelighed fulgt i vedligeholdsarbejdet (Biofos 2017-2022), '
         'omkostningskontrol fra fuldt P&L (ELOHVAC 2023-2026) og prioriteringer '
         'sat efter driftsbehov i 37 projekter (Novo 2022-2024).'),
        ('Oversee continuous improvement activities focused on improving equipment '
         'performance, efficiency, and process optimization',
         'Løbende forbedring som arbejdsform: rodårsagsanalyser der ændrede '
         'fejlhåndteringen (ARJ 2003-2010), arbejdsgange forbedret på tværs af '
         'skiftehold (Biofos 2017-2022) og PDCA, 5S og Standard Work som '
         'daglige værktøjer (kvalitetsarbejdet siden 2022).'),
        ('Promote a robust safety culture and ensure compliance with HSE standards, '
         'permit-to-work systems, LOTO procedures, and site requirements',
         'Sikkerhedskultur i praksis: LOTO, APV og arbejdstilladelser på tværs af '
         'skiftehold i døgndrift (Biofos 2017-2022), risikovurderinger på '
         'byggepladser (Ventek 2022) og sikkerhedsarbejde i GMP-regi (Novo '
         '2022-2024). Rutiner der følges, også på natholdet.'),
        ('A degree within mechanical, electrical, automation, maintenance, Marine '
         'Engineering (Preferred), or a related discipline',
         'Uddannelsen rammer både det maskintekniske, elektriske og maritime: '
         'B.Tech (EQF6) fra Copenhagen School of Marine Engineering & Technology '
         'Management (2017-2022), elteknik på EQF6 (2000-2003) og STCW-'
         'certifikater fra Søfartsstyrelsen. Marine Engineering er bogstaveligt '
         'skolens navn.'),
        ('Leadership experience from an industrial or manufacturing environment, '
         'including responsibility for larger technical teams',
         'Ledelseserfaring fra industri og produktion siden 2003: produktions-'
         'afdeling med 12 mand (ARJ), drift og vedligehold med 10 medarbejdere på '
         'skiftehold (Biofos 2017-2022), 14 mand i entrepriser (Ventek 2022) og '
         '25 specialister (Novo 2022-2024). Ansvar for større tekniske teams er '
         'trappet op gennem hele karrieren.'),
        ('Experience within maintenance operations, including preventive and '
         'corrective maintenance methodologies and KPIs (MTBF, MTTR, OEE and spare '
         'parts availability)',
         'Vedligeholdsdrift i seks år som vedligeholdelsesleder i døgndrift '
         '(Biofos 2017-2022): forebyggende og korrigerende metoder, MTBF, MTTR, '
         'OEE og reservedelstilgængelighed som faste måltal, og reservedels-'
         'styring der sikrede at delene var der når de skulle bruges.'),
        ('Experience working with CMMS systems, maintenance planning, and '
         'performance management',
         'CMMS-systemer brugt i det daglige vedligeholdsarbejde (Biofos 2017-2022) '
         'med planlægning, registrering og opfølgning. Performance management '
         'suppleret af PRINCE2-struktur og faste opfølgningsmøder på fremdrift '
         '(Novo 2022-2024).'),
        ('Experience managing contractors and external service providers',
         'Kontraktstyring siden 2003: underentreprenører og leverandører holdt på '
         'aftaler (Ventek 2022, ELOHVAC 2023-2026) og eksterne serviceleverandører '
         'i drift (Biofos 2017-2022). Klare aftaler, målt kvalitet og opfølgning '
         'på stedet.'),
        ('Knowledge of Lean Manufacturing, Root Cause Analysis, and continuous '
         'improvement principles',
         'Lean og forbedring som metode: Root Cause Analysis i form af '
         'en rodårsagsanalyse der ændrede praksis (ARJ 2003-2010), PDCA, 5S og '
         'Standard Work fra kvalitetsarbejdet, og forbedringsprojekter på '
         'arbejdsgange gennemført på skiftehold (Biofos 2017-2022).'),
        ('Professional proficiency in both Danish and English',
         'På dansk og engelsk brugt professionelt i skrift og tale: dokumentation og '
         'møder på begge sprog (Novo 2022-2024), kundedialog og aftaler (Ventek, '
         'ELOHVAC 2023-2026) og teknisk formidling siden 2010. Persisk som '
         'modersmål oveni.'),
        ('Creates engagement, accountability, and team performance',
         'Engagement og ansvarlighed bygget op i team gennem 20 år: skiftehold der '
         'holdt sammen (Biofos 2017-2022), en produktionsafdeling der leverede på '
         'mål (ARJ 2003-2010) og specialister der fulgte med på tværs af '
         'arbejdsgivere (ELOHVAC 2023-2026).'),
        ('Balances direct technical involvement with a strategic perspective',
         'Balancen er min arbejdsform: hænderne i anlægget som vedligeholdelsesleder '
         '(Biofos 2017-2022) og det strategiske blik som teknisk direktør med fuldt '
         'P&L (ELOHVAC 2023-2026) og som projektleder for 37 CAPEX-projekter '
         '(Novo 2022-2024).'),
        ('Makes sound decisions based on data and operational priorities',
         'Beslutninger på data: KPI-mål som grundlag i vedligeholdet (Biofos '
         '2017-2022), økonomiske tal i styringen (ELOHVAC 2023-2026) og '
         'prioriteringer i 37 projekter sat efter driftsbehov og risici (Novo '
         '2022-2024).'),
        ('Develops collaborative relationships and communicates clearly with both '
         'shop floor and management stakeholders',
         'Relationer og kommunikation hele vejen rundt: folkene på gulvet på '
         'skiftehold (Biofos 2017-2022), ledelsesrapportering i fast kadence (Novo '
         '2022-2024) og kunder og samarbejdspartnere i øjenhøjde (Ventek, ELOHVAC '
         '2023-2026).'),
        ('Maintains a clear focus on safety, quality, and continuous improvement; '
         'full onsite in Nakskov with occasional support outside normal working '
         'hours',
         'Fokus på sikkerhed, kvalitet og løbende forbedring går igen i '
         'alle jobs, senest dokumentationsdisciplinen i GMP-regi (Novo 2022-2024). '
         'Full onsite i Nakskov er gangbar: jeg kan flytte til området hvis jobbet '
         'er rigtigt, og kender døgndrift fra seks år på skiftehold.'),
                   ], widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo · Preventive & Corrective Maintenance Manager, Vestas')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Vestas_PreventiveCorrectiveMaintenanceManager_79943.docx')
    build(out)
    print(out)
