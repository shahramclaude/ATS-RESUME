# -*- coding: utf-8 -*-
"""Novo Nordisk · HVAC Responsible, API Manufacturing (25K Facility Support, Hillerød).

Engelsk opslag -> engelsk dokument. Masterdesign (scripts/master_design.py):
brev side 1, CV side 2-3, kravmatrix side 4.

Kun fakta fra master-CV'et og brugerbekræftelser. Ikke dokumenteret: AHU-drift, UDF/LAF,
pressure cascades, ER-uddannelse, FMS. De beskrives som tilgang eller som gap, aldrig som erfaring.
Opslaget beder om en kort motivation i CV'et; den står under WHY THIS ROLE. Intet foto.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
OUT_DIR = os.path.join(ROOT, 'output')
OUT = os.path.join(OUT_DIR, 'Shahram_Ajloo_NovoNordisk_HVACResponsible_Hillerod.docx')

NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'HVAC Responsible, API Manufacturing · Novo Nordisk, Hillerød'
BANNER_RESUME = 'HVAC, ventilation and electrical maintenance in regulated production'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('28 November 2026')
    m.meta('Novo Nordisk · 25K Facility Support, API Manufacturing, Hillerød')
    m.para('Dear Gry Frost Eriksen and the 25K Facility Support team,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    def sub(text):
        p = m._p(spacing_after=20, spacing_before=60, line=260, justify=False, keep_next=True)
        m._run(p, text, bold=True, color='002B5C')
        return p

    # ------------------------------------------------------------ letter, page 1
    lp('Two API production facilities in one building are supplied with HVAC from the same plant. When one '
       'unit starts to drift, both production schedules can feel it before the diagnosis is finished. The HVAC '
       'Responsible in 25K decides what is repaired now, what waits for the next shutdown, and what has to '
       'be replaced altogether. That decision sits between the daily work and the long-term plan, and it is '
       'the part of the job I would take seriously.')

    sub('Daily stability starts with the rounds')
    lp('Routine rounds show where the next failure is forming. I would turn each round into a short '
       'condition note per unit: airflow and differential pressure, filter and coil condition, damper '
       'behaviour, alarms from the building management system, and what the operators have logged since '
       'the last visit. Those notes feed one list, ordered by effect on production. Servicecenter Hillerød '
       'receives the list before each shutdown window, so the repairs of the day and the shutdown work '
       'follow the same order.')

    sub('AHU exchange as a project, not as a series of repairs')
    lp('An ageing air handling unit is seldom replaced in one step. There is the repair that buys time, the '
       'upgrade that removes a recurring risk, and the exchange that needs a shutdown. Each exchange should '
       'be scoped with the project team and Environmental Support before work starts. That scope covers the '
       'effect on pressure cascades, the qualification steps that follow the change, and the sequence of work '
       'against the production plan. I would speak up when something stalls, and agree the next '
       'step with the people involved, so the work keeps moving. My aim is to turn complex challenges into '
       'practical solutions that the team can carry out on the next shutdown.')

    sub('UDF and LAF units with the same documentation route')
    lp('Unidirectional flow and laminar airflow units are where a small deviation becomes a production '
       'question. I would start with the installed base: the current documentation, the last verified '
       'performance and the open actions from the rounds. Installation support and problem solving follow '
       'the same route each time, so the next person can pick up the record without needing the one who did '
       'the work.')

    sub('From floor observations to the future state')
    lp('The future state of the HVAC systems in 25K should be built from what the floor already shows: where '
       'alarms repeat, which units take the most attention, and where the monitoring data is not yet good '
       'enough to plan from. I would bring those observations into a short set of priorities, each with an '
       'owner, a cost frame and a date. The site can keep a short plan. A long one tends to be shelved.')

    sub('The first 90 days')
    lp('In the first month I would walk both facilities with Servicecenter Hillerød and Environmental Support, '
       'and agree which systems are critical to production. By day 60, the condition notes and the failure '
       'history would form one priority list for the exchanges. By day 90, the first exchange should have a '
       'scope, a shutdown window and a documented qualification route, with the next decision points written '
       'down for the project team.')

    lp('Keeping daily operation stable while long-term work moves forward takes a pragmatic, resilient and '
       'collaborative mindset. The rounds are the easiest place for everyone on the floor to make your voice heard, '
       'and I would welcome a conversation about which unit needs the first decision.', after=44)
    lp('Yours sincerely', after=8)
    lp('Shahram Ajloo', after=8)

    # ------------------------------------------------------------ CV, pages 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFILE')
    m.para('Electrically authorised marine engineer (LV/MV/HV) with HVAC, ventilation and electrical maintenance '
           'experience. Fault-finding and preventive maintenance in 24/7 operation at Biofos, ventilation and '
           'climate service at ELOHVAC and Data Power, and commissioning under GMP at Novo Nordisk, with FAT, SAT '
           'and IQ/OQ/PQ. Works with maintenance KPIs, CMMS and building automation (CTS/BMS, KNX). PRINCE2 '
           'certified. Solution-oriented, and stays calm and structured when a system needs attention. Able to '
           'keep several tasks and stakeholders moving across operations, maintenance and projects. '
           'Danish native, English professional.', after=32)

    m.section('WHY THIS ROLE')
    m.para('Two production facilities that share one air system are a demanding place to work, and that is '
           'the reason I am applying. The job asks for calm, structured work when a unit needs attention, and '
           'for the discipline to plan the exchanges so that production does not pay for them. I want to work in '
           'a team that will value initiative, where people care for one another, and where people are empowered to '
           'drive projects forward. I want to make my voice heard on which unit gets replaced and when.', after=32)

    m.section('HVAC, MAINTENANCE AND GMP WORK')
    tasks = [
        ('Daily operation and fault-finding',
         'Preventive maintenance and fault-finding on pumps, HVAC and high-voltage switchgear in 24/7 operation at '
         'Biofos, 2017 to 2022, with shift work under LOTO, risk assessment and APV.'),
        ('Ventilation and climate installations',
         'Installation, maintenance and fault-finding on electrical, ventilation and climate systems at ELOHVAC and '
         'Data Power, from emergency call-outs to handed-over installations.'),
        ('Indoor climate',
         'Calculations and analyses of comfort and air quality through ventilation and climate work across my '
         'positions. Air quality and energy use are part of the same assessment.'),
        ('GMP qualification',
         'FAT, SAT and IQ/OQ/PQ under GMP, FDA and EMA at Novo Nordisk on CIP/SIP systems, tanks, process piping, '
         'instrumentation and UPS, with zero critical deviations at handover.'),
        ('Shutdown and project coordination',
         '37 concurrent CAPEX projects at Novo Nordisk and 11 concurrent projects at Ventek-Air, from specification '
         'to formal handover, with handover packs and subcontractor coordination.'),
        ('Building automation and monitoring',
         'CTS/BMS and KNX in building automation. SCADA and control panels in production support at Biofos.'),
        ('Leading and developing people',
         'Development of 5 electricians and 3 apprentices through one-to-ones and MUS. Coordination of 25 specialists '
         'at Novo Nordisk, and daily leadership of a 14-person team at Ventek-Air.'),
        ('Improvement and failure analysis',
         '40 % lower energy costs through a PDCA programme at Novo Nordisk. FMEA, 5 Whys, Ishikawa and A3 in failure '
         'analysis. MTBF, MTTR, OEE and spare parts availability in maintenance work.'),
    ]
    for head, body in tasks:
        m.bullet(head, body, after=24)

    m.section('EXPERIENCE')
    jobs = [
        ('CTO for the AI department and electrically authorised marine engineer, electrical and ventilation',
         'Data Power Consultant ApS · Copenhagen · 2024 to present',
         [('', 'Responsible for electrical and ventilation work with full P&L responsibility. From November 2026 this '
               'includes the electrical activities previously run through ELOHVAC.'),
          ('', 'Management of 5 electricians and 3 apprentices: daily planning, one-to-ones, MUS and structured training.'),
          ('', 'Two parallel organisations run under one shared plan with written priorities. Responsible for the AI '
               'department with 4 to 10 people.')]),
        ('Owner and technical director, electrically authorised marine engineer',
         'ELOHVAC ApS · Copenhagen · May 2023 to November 2026 (company closed)',
         [('', 'Preventive maintenance and fault-finding on electrical, ventilation and climate systems, from emergency '
               'call-outs to handed-over installations.'),
          ('', 'Quotations, schedules, material planning and subcontractors, with KPI dashboards built in Python. '
               'Productivity gain above 40 % from AI tools on quotations, schedules and KPI reporting.'),
          ('', 'LOTO, risk assessment and APV at each site start. Zero critical deviations in service agreements.')]),
        ('Senior commissioning engineer and project manager, electrical system',
         'Novo Nordisk A/S · Kalundborg and Bagsværd · November 2022 to July 2024',
         [('', 'Cross-functional coordination of 25 specialists across engineering, procurement and site, with 37 '
               'concurrent CAPEX projects.'),
          ('', 'FAT, SAT and IQ/OQ/PQ under GMP, FDA and EMA, with zero critical deviations at handover.'),
          ('', 'Monthly reporting to management and client. SAP ERP for finance, assets and cost.')]),
        ('Project and workshop manager',
         'Ventek-Air · Copenhagen · January 2022 to November 2022',
         [('', '11 concurrent installation projects from specification to formal handover, with a 14-person team.'),
          ('', 'Tendering, subcontractors, safety documentation and handover packs. Daily board meetings and '
               'bottleneck analysis.')]),
        ('Maintenance and operations manager, workshop technician',
         'Biofos (Lynetten) · Copenhagen · August 2017 to January 2022',
         [('', 'Operation and maintenance of pumps, HVAC, high-voltage switchgear and SCADA in 24/7 operation.'),
          ('', 'Shift operation with safety discipline: LOTO, risk assessment, APV and near-miss reporting.'),
          ('', 'Spare parts flow and stock control. 5S, Standard Work and PDCA in the workshop and store.')]),
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
    m.edu('B.Tech (EQF6), technology management and mechanical engineering',
          'Copenhagen School of Marine Engineering & Technology Management · 2017 to 2022')
    m.edu('Electrically authorised marine engineer (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('Refrigeration and air conditioning (AMU)', 'Mercantec · 2021')
    m.edu('Electrical and mechanical engineering design, electrical engineering (EQF6)',
          'Tehran Technical University · 2000 to 2003')
    m.edu('PRINCE2, certified', 'AXELOS / PeopleCert')
    m.para('Lean and Six Sigma methods applied in practice, not certified: DMAIC, 5S, PDCA, VSM, A3, Kaizen, SMED, '
           'TPM, 5 Whys, Ishikawa and FMEA.', after=48)

    m.section('SKILLS')
    m.models_table('Tools and systems', ('Area', 'Tools'), [
        ('Operation and maintenance', 'Preventive maintenance, fault-finding, CMMS, spare parts, MTBF, MTTR, OEE'),
        ('GMP and qualification', 'GMP, FDA, EMA, FAT, SAT, IQ/OQ/PQ, CIP/SIP, UPS, change and deviation handling'),
        ('Control and automation', 'SCADA, control panels, CTS/BMS, KNX, PLC-controlled plants'),
        ('Leadership and governance', 'Matrix leadership, one-to-ones, MUS, situational leadership (SLII), RACI'),
        ('Projects and economics', 'PRINCE2, budget and schedule control, economic follow-up, SAP ERP'),
        ('Data and AI', 'Python, Power BI, Excel, Claude API, Claude Code'),
    ], widths=(3400, 6946), compact=True)
    m.para('Danish native, spoken and written. English professional, working language in international projects since '
           '2017. Persian native. Driving licence B, manual gearbox.', after=40)

    # ------------------------------------------------------------ requirements matrix, page 4
    m.page_break()
    m.section('REQUIREMENTS MATRIX')
    rows = [
        ('Daily operation of the HVAC systems for two production facilities in one building, with fast problem solving',
         'Confirmed in practice. Fault-finding and preventive maintenance on HVAC in 24/7 operation at Biofos from 2017 to 2022. Ventilation and climate service with fast call-outs at ELOHVAC, 2023 to 2026, and at Data Power from 2024.'),
        ('Routine inspection rounds, condition assessments and upgrades of ageing equipment before it affects production',
         'Partly documented. Preventive maintenance and failure analysis at Biofos and ELOHVAC. Condition assessment of air handling units is not in my record, so the letter describes it as the approach I would take.'),
        ('Improvement projects for exchanging and maintaining the AHU systems',
         'Partly documented. Project leadership of 11 concurrent projects at Ventek-Air and 37 CAPEX projects at Novo Nordisk. Exchange work on AHUs specifically is not in my record.'),
        ('UDF and LAF units: installation support, systematic problem solving and documentation',
         'Not in my record. The closest method is GMP qualification at Novo Nordisk (FAT, SAT, IQ/OQ/PQ) together with FMEA and A3 problem solving. The letter sets out the approach.'),
        ('Future state of the HVAC systems in 25K, with clear priorities from floor observations',
         'Method documented through the 40 % energy programme at Novo Nordisk and condition notes and priority lists at Biofos. Future-state planning for a production site is not in my record.'),
        ('Collaboration with Servicecenter Hillerød on daily operations and shutdown maintenance',
         'Coordination of shutdown and project work with subcontractors at Novo Nordisk and Ventek-Air. Work with Servicecenter Hillerød specifically is not in my record.'),
        ('Collaboration with Environmental Support on troubleshooting, impact assessments and knowledge sharing',
         'Not in my record as a documented team. Impact assessment of changes is handled through risk assessment and change control under GMP at Novo Nordisk.'),
        ('Scope and implementation of improvements across the facilities, with the project team',
         'Documented. Scope, planning and handover of 11 concurrent projects at Ventek-Air and 37 CAPEX projects at Novo Nordisk, with handover packs.'),
        ('Solid HVAC experience, including operating, maintaining and troubleshooting air handling units (AHU)',
         'Partly documented. HVAC operation, maintenance and fault-finding at Biofos, and ventilation work at ELOHVAC. AHU-specific experience is not in my record.'),
        ('Education as Maskinmester, engineer or another relevant discipline',
         'Confirmed. Elautoriseret maskinmester (LV/MV/HV), May 2023. B.Tech (EQF6) in technology management and mechanical engineering, 2017 to 2022.'),
        ('Experience from the pharmaceutical industry or a similar regulated environment',
         'Confirmed. GMP, FDA and EMA qualification at Novo Nordisk, 2022 to 2024, with zero critical deviations at handover.'),
        ('Collaboration, coordination and planning across operations, maintenance and projects',
         'Coordination of 25 specialists at Novo Nordisk, a 14-person team at Ventek-Air, and two parallel organisations at Data Power and ELOHVAC.'),
        ('Stable daily operation while long-term improvements move forward, and raising problems early',
         'Shift operation with planning discipline at Biofos, with LOTO, risk assessment and near-miss reporting. The approach to stalled work, speaking up early and agreeing the next step, is set out in the letter.'),
        ('Training as Engineering Responsible (ER), useful but not essential',
         'Not in my record. No ER training is documented. I would clarify the site ER requirements in the first weeks of the role.'),
        ('Technical expertise in regulating pressure cascades, useful but not essential',
         'Not in my record as a documented topic. Ventilation and climate work at ELOHVAC and Data Power is the closest area. I would confirm the cascade requirements with the site before the first exchange.'),
        ('Experience with BMS and FMS, useful but not essential',
         'Partly documented. CTS/BMS and KNX building automation are confirmed, and SCADA and control panel work at Biofos. FMS is not in my record, so I would treat it as a learning item.'),
        ('A short motivation in the CV',
         'Included under WHY THIS ROLE. The motivation is written around the job priorities: stable daily HVAC for two production facilities, and planned exchanges.'),
        ('No photo in the CV',
         'No photo in this document, as the ad asks. The CV is a single text document with a banner, a profile and tables, and it contains no image of the applicant.'),
        ('Apply before 6 December 2026, on site in Hillerød',
         'Based in Måløv, within the Øresund region. The commute to Hillerød is a matter of distance and is not confirmed in my record.'),
    ]
    m.models_table('Opslagets krav og min dokumentation', ('Krav', 'Dokumentation og status'),
                   rows, widths=(3600, 6746), compact=True)

    m.save(path, title='HVAC Responsible, API Manufacturing - Novo Nordisk Hillerød',
           subject='Application HVAC Responsible, API Manufacturing, Hillerød')
    print(path)


if __name__ == '__main__':
    os.makedirs(OUT_DIR, exist_ok=True)
    build(OUT)
