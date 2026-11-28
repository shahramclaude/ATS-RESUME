# -*- coding: utf-8 -*-
"""Ferring · Head of Engineering, Maintenance & IT/OT (R0038817), Syntese, Hvidovre.

Engelsk opslag -> engelsk dokument. Masterdesign (scripts/master_design.py):
brev side 1, CV side 2-3, kravmatrix side 4.

Kun fakta fra master-CV'et og brugerbekræftelser. Ikke: kandidatgrad, medlemskab af et site
leadership team, ledelse af ledere i et site af denne størrelse, IT-systemansvar, globale stakeholdere.
Opslaget beder om motivation i CV'et; det er skrevet som en kort "Why this role" med fokus på jobbet.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
OUT_DIR = os.path.join(ROOT, 'output')
OUT = os.path.join(OUT_DIR, 'Shahram_Ajloo_Ferring_Syntese_HeadEngineeringMaintenanceITOT.docx')

NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Head of Engineering, Maintenance & IT/OT · Syntese, Hvidovre'
BANNER_RESUME = 'Engineering and maintenance leadership in GMP-regulated manufacturing'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('28 November 2026')
    m.meta('Ferring Pharmaceuticals · Syntese, Hvidovre · R0038817')
    m.para('Dear Site Leadership Team at Syntese,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    def sub(text):
        p = m._p(spacing_after=20, spacing_before=60, line=260, justify=False, keep_next=True)
        m._run(p, text, bold=True, color='002B5C')
        return p

    # ------------------------------------------------------------ letter, page 1
    lp('Syntese makes mesalazine around the clock, and every day of that production depends on '
       'three functions that rarely share the same plan: engineering projects, the maintenance '
       'backlog and IT/OT changes. The head of these functions has to set one order of priority that '
       'Production and Quality can accept, and keep it through the shutdown windows. The job is about '
       'that order, and about moving the site from reactive maintenance toward planned, data-driven work '
       'without loosening GMP control.')

    sub('One priority list before any new initiative')
    lp('The first step would be a single page per production-critical system: what it does, what it '
       'costs when it stops, the open engineering items, the maintenance backlog and the IT/OT changes '
       'that touch it. The three managers and Production agree the order on that page. Work that does not '
       'move a critical system waits. The page is reviewed at each Site Leadership Team meeting, so the '
       'trade-offs are visible to the people who carry them.')

    sub('Preventive work follows the failure history')
    lp('Proactive maintenance only works when the asset data is clean. I would check the asset hierarchy, '
       'the failure coding and the quality of work orders on two or three systems where unplanned stops '
       'repeat. Criticality and preventive intervals follow from that history, and MTBF, MTTR and OEE become '
       'site targets only after everyone agrees how they are calculated. A pragmatic approach here means '
       'fewer, better-kept plans, not a larger register.')

    sub('IT/OT under the same change discipline')
    lp('OT systems that control or monitor production need the same change control and validation route '
       'as process equipment. I would give each OT change one owner in IT and one in Maintenance, and make '
       'the GMP impact a required line in the change request. The technical decisions stay with the managers '
       'who know the systems. My role is to make sure those decisions are taken on time and written down.')

    sub('Managers who can explain their own priorities')
    lp('Each manager gets a written mandate: what they decide alone, what goes to the site team, and what '
       'needs Production or Quality sign-off. That mandate empowers managers to decide, and it keeps the '
       'decisions visible. Then come regular one-to-ones and a review of how decisions '
       'were made, not only of the results. The test is simple. A manager should be able to explain the '
       'priority to Production without me in the room. I would also make room for constructive challenge in '
       'the site team, because a plan that nobody questions is usually not tested. I would lead through others '
       'here: the managers take the decisions, and my job is to bring people together around one list.')

    sub('Global standards on a local site')
    lp('Ferring runs its sites inside a complex matrix organization. I would list which global requirements '
       'are binding at Syntese and which parts leave room for local design. That list lets the site argue '
       'for its own schedule with evidence. The aim is a future-ready manufacturing organisation that does not '
       'treat every global standard as a local problem.')

    lp('I live in Måløv, within the Øresund region. I would welcome a conversation about which of the three '
       'functions needs the first decision, and how the Site Leadership Team wants to set priorities across '
       'them.', after=44)
    lp('Yours sincerely', after=8)
    lp('Shahram Ajloo', after=8)

    # ------------------------------------------------------------ CV, pages 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFILE')
    m.para('Engineering, maintenance and project leadership in 24/7 industrial plants, with GMP, FDA and EMA '
           'qualification work at Novo Nordisk, preventive maintenance and fault-finding at Biofos, and '
           'leadership of two parallel organisations at Data Power and ELOHVAC. Works with maintenance KPIs '
           '(MTBF, MTTR, OEE, spare parts availability) and CMMS. Electrically authorised marine engineer '
           '(LV/MV/HV) and PRINCE2 certified. Danish native, English professional.', after=32)

    m.section('WHY THIS ROLE')
    m.para('The core of this role is to lead three functions toward one site plan, and to move maintenance '
           'from reactive work toward planned, data-driven work under GMP. Ferring +You describes that way of '
           'working together, and these are the parts of the job I have '
           'worked on directly: shutdown and project priorities across engineering and site, and preventive '
           'maintenance built on failure history. I would bring that practice to the Syntese plan.', after=32)

    m.section('LEADERSHIP AND MAINTENANCE WORK')
    tasks = [
        ('Priorities across functions',
         'Economic follow-up of shutdown stops and each rebuild decision, with budget and schedule control. Joint plans '
         'across engineering, procurement and site on 37 concurrent CAPEX projects at Novo Nordisk.'),
        ('Leading through others',
         'Direct line responsibility for team leaders who led their own staff, confirmed by the candidate. Daily '
         'leadership of a 14-person team at Ventek-Air. Development of 5 electricians and 3 apprentices through '
         'one-to-ones and MUS.'),
        ('Preventive and data-driven maintenance',
         'Preventive maintenance of pumps, HVAC and high-voltage switchgear in 24/7 operation at Biofos, with '
         'MTBF, MTTR, OEE and spare parts availability in maintenance work. CMMS work on asset data and work orders.'),
        ('GMP-regulated systems and utilities',
         'FAT, SAT and IQ/OQ/PQ under GMP, FDA and EMA at Novo Nordisk on tanks, CIP/SIP systems, process piping, '
         'instrumentation and UPS, with zero critical deviations at handover.'),
        ('Stakeholders and governance',
         'Monthly reporting to management and client at Novo Nordisk. Two parallel organisations at ELOHVAC and Data Power '
         'run under one shared plan with written priorities.'),
        ('Technical depth without being the specialist',
         'SCADA and control panels at Biofos. CTS/BMS and KNX in building automation. AI and software leadership '
         'as CTO for the AI department at Data Power, with validation of AI output before it reaches customers.'),
    ]
    for head, body in tasks:
        m.bullet(head, body, after=24)

    m.section('EXPERIENCE')
    jobs = [
        ('CTO for the AI department and electrically authorised marine engineer, electrical and ventilation',
         'Data Power Consultant ApS · Copenhagen · 2024 to present',
         [('', 'Responsible for the AI and AI coding department, 4 to 10 people, and for electrical and ventilation work '
               'with full P&L responsibility from November 2026.'),
          ('', 'Led two parallel organisations under one shared plan, with written priorities.'),
          ('', 'Management of 5 electricians and 3 apprentices.')]),
        ('Owner and technical director, electrically authorised marine engineer',
         'ELOHVAC ApS · Copenhagen · May 2023 to November 2026 (company closed)',
         [('', 'Preventive maintenance and fault-finding on electrical, ventilation and HVAC systems, from emergency '
               'call-outs to handed-over installations.'),
          ('', 'KPI dashboards for service work, with a productivity gain above 40 % on quotation, schedules, KS checklists '
               'and KPI reporting, using AI tools.'),
          ('', 'LOTO, risk assessment and APV at each site start. Zero critical deviations in service agreements.')]),
        ('Senior commissioning engineer and project manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg and Bagsværd · November 2022 to July 2024',
         [('', 'Cross-functional leadership of 25 specialists across engineering, procurement and site.'),
          ('', 'FAT/SAT and IQ/OQ/PQ under GMP, FDA and EMA, with zero critical deviations at handover.'),
          ('', '40 % lower energy costs through a PDCA programme. SAP ERP for finance and asset cost.')]),
        ('Project and workshop manager',
         'Ventek-Air · Copenhagen · January 2022 to November 2022',
         [('', '11 concurrent installation projects from specification to formal handover, with a 14-person team.'),
          ('', 'Tendering, subcontractors, safety documentation and handover packs. Board meetings and bottleneck analysis.')]),
        ('Maintenance and operations manager, workshop technician',
         'Biofos (Lynetten) · Copenhagen · August 2017 to January 2022',
         [('', 'Operation and maintenance of pumps, HVAC, high-voltage switchgear and SCADA in 24/7 operation.'),
          ('', 'Responsibility for process plant equipment at a water treatment plant, alongside shift operation.'),
          ('', 'Shift work under LOTO, risk assessment, APV and near-miss reporting. 5S, Standard Work and PDCA.')]),
        ('Electromechanic and production team leader',
         'ARJ Engineering · Tehran · December 2003 to March 2010',
         [('', 'Led 12 mechanics and technicians in the workshop: shift planning, materials and targets.'),
          ('', 'Fault diagnosis and repair of industrial electrical and mechanical equipment, with root-cause analysis.')]),
    ]
    for title, meta, bullets in jobs:
        m.job(title, meta)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('EDUCATION AND CERTIFICATIONS')
    m.edu('Maskinmester (marine engineering & technology management)',
          'Copenhagen School of Marine Engineering & Technology Management · 2017 to 2022')
    m.edu('Electrical and Mechanical Engineering Design, electrical engineering (EQF6)',
          'Tehran Technical University · 2000 to 2003')
    m.edu('Electrically authorised marine engineer (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('PRINCE2, certified', 'AXELOS / PeopleCert')
    m.para('Lean and Six Sigma methods applied in practice, not certified: DMAIC, 5S, PDCA, VSM, A3, Kaizen, SMED, '
           'TPM, 5 Whys, Ishikawa and FMEA.', after=48)

    m.section('SKILLS')
    m.models_table('Tools and systems', ('Area', 'Tools'), [
        ('Leadership and governance', 'Matrix leadership, one-to-ones, MUS, SLII, RACI, situational leadership'),
        ('Maintenance and reliability', 'CMMS, asset data, preventive plans, MTBF, MTTR, OEE, FMEA, A3, 5 Whys'),
        ('GMP and qualification', 'GMP, FDA, EMA, FAT, SAT, IQ/OQ/PQ, CIP/SIP, UPS'),
        ('Control and automation', 'SCADA, control panels, PLC-controlled plants, CTS/BMS, KNX'),
        ('Projects and economics', 'PRINCE2, budget and schedule control, economic follow-up, investment models'),
        ('Data and AI', 'Python, Power BI, Excel, Claude API, Claude Code'),
    ], widths=(3400, 6946), compact=True)
    m.para('Danish native, spoken and written. English professional, working language in international projects since '
           '2017. Persian native. Driving licence B, manual gearbox.', after=40)

    # ------------------------------------------------------------ requirements matrix, page 4
    m.page_break()
    m.section('REQUIREMENTS MATRIX')
    rows = [
        ('Solid leadership experience within Engineering and/or Maintenance in a manufacturing environment',
         'Engineering leadership in a GMP pharma site: cross-functional leadership of 25 specialists at Novo Nordisk, 2022 to 2024. Maintenance leadership in 24/7 operation at Biofos, 2017 to 2022. Team leadership in a 14-person team at Ventek-Air in 2022.'),
        ('Proven experience leading and developing managers',
         'Direct line responsibility for team leaders who led their own staff, confirmed by the candidate. Employer, period and number of leaders are not stated in my record. Development of 5 electricians and 3 apprentices through one-to-ones and MUS at ELOHVAC and Data Power.'),
        ('Experience from a GMP-regulated environment',
         'GMP, FDA and EMA requirements at Novo Nordisk, 2022 to 2024. FAT, SAT and IQ/OQ/PQ on tanks, CIP/SIP systems, process piping, instrumentation and UPS, with zero critical deviations at handover.'),
        ('Strong stakeholder management skills within complex organizations',
         'Coordination across engineering, procurement and site with 37 concurrent projects at Novo Nordisk. Monthly reporting to management and client. Two parallel organisations at Data Power and ELOHVAC run under one shared plan.'),
        ('A strategic mindset combined with a strong understanding of operational and production priorities',
         'Economic follow-up of shutdown stops. Shift operation and fault-finding in 24/7 production support at Biofos. AI and KPI analysis used to prepare management decisions at Data Power.'),
        ("A master's degree, ideally within Engineering or a related technical discipline",
         'Not held. My highest degree is the maskinmester (marine engineering & technology management) from 2017 to 2022, which is bachelor level (EQF6), and the electrical engineering degree from Tehran at EQF6 level.'),
        ('Knowledge of manufacturing utilities and equipment',
         'Utilities at Novo Nordisk: UPS, emergency and panic lighting, access control, CIP/SIP systems, tanks and process piping. Pumps, HVAC and high-voltage switchgear at Biofos. HVAC and ventilation systems at ELOHVAC.'),
        ('Experience with maintenance data and KPIs',
         'MTBF, MTTR, OEE and spare parts availability used in maintenance work, and CMMS work on asset data and work orders. KPI dashboards built in Python and Power BI for service work at ELOHVAC.'),
        ('Technical background that enables you to understand and challenge Engineering, Maintenance and IT/OT topics without needing to be the technical expert',
         'I hold the electrically authorised marine engineer authorisation, with SCADA and control panel work at Biofos, CTS/BMS and KNX in building automation, and AI and software leadership at Data Power. I do not present myself as the IT/OT system specialist.'),
        ('Leading, coaching and developing the three managers responsible for Engineering, Maintenance and IT/OT',
         'Not a documented role in my record: I have not led three functional managers at a site. Coaching is documented at team level, through one-to-ones and MUS with electricians and apprentices.'),
        ('Setting direction and priorities while empowering your managers to lead their organizations',
         'Led ELOHVAC and Data Power in parallel with one shared plan and written priorities, and an agreed order of work in the two organisations. Empowerment of managers at site level is not documented in my record.'),
        ('Contributing a strategic and cross-functional perspective to the Site Leadership Team',
         'Cross-functional coordination at Novo Nordisk and Ventek-Air, including board meetings and bottleneck analysis. Membership of a site leadership team is not in my record.'),
        ('Driving the transition from reactive maintenance towards a more proactive, preventive and data-driven approach',
         'Preventive maintenance alongside acute fault-finding at Biofos in 24/7 operation, 2017 to 2022. Failure analysis with FMEA, 5 Whys and A3. A full site-wide programme of this transition is not in my record.'),
        ('Aligning Engineering, Maintenance and IT/OT priorities with production needs and the overall site strategy',
         'Joint plans for engineering, procurement and site on 37 CAPEX projects at Novo Nordisk, and the 40 % energy saving programme. Alignment with production at site strategy level is not in my record.'),
        ('Building strong relationships across the organization and balancing local and global priorities',
         'Relationships across site teams, customers and subcontractors at ELOHVAC and Ventek-Air. Global stakeholder relations and global standards work are not in my record.'),
        ('Driving key projects and decisions forward through constructive challenges, influence and stakeholder buy-in',
         'Economic follow-up for each rebuild decision. Delivery of 11 concurrent projects at Ventek-Air and 37 concurrent CAPEX projects at Novo Nordisk, with handover packs.'),
        ('Navigating a complex matrix organization',
         'Data Power and ELOHVAC ran side by side under one shared plan and written agreements on which work comes first. Cross-functional work at Novo Nordisk with engineering, procurement and site.'),
        ('Working on-site in Hvidovre, located within the Øresund region, as no relocation assistance is offered',
         'Based in Måløv, Ballerup Municipality, within the Øresund region. No relocation is needed for on-site work in Hvidovre.'),
        ('Including a few lines regarding your motivation for applying in your CV',
         'Included in the CV under WHY THIS ROLE, written around the job priorities and the move from reactive to planned work.'),
    ]
    m.models_table('Opslagets krav og min dokumentation', ('Krav', 'Dokumentation og status'),
                   rows, widths=(3600, 6746), compact=True)

    m.save(path, title='Head of Engineering, Maintenance & IT/OT - Ferring Syntese',
           subject='Application Head of Engineering, Maintenance & IT/OT, R0038817')
    print(path)


if __name__ == '__main__':
    os.makedirs(OUT_DIR, exist_ok=True)
    build(OUT)
