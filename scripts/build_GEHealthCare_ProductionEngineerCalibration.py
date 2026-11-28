# -*- coding: utf-8 -*-
"""GE HealthCare · Production Engineer, Calibration & Maintenance (R4048177), Herlev.

Engelsk opslag -> engelsk dokument. Masterdesign (scripts/master_design.py):
brev side 1, CV side 2-3, kravmatrix side 4.

Kun fakta fra master-CV'et og brugerbekræftelser. Kalibrering, metrologi, HxGN EAM og AGORA er IKKE
dokumenteret i master og beskrives aldrig som erfaring. Krav-filen skrives fra samme liste som matrixen.
Intet foto. Opslaget beder ikke om motivation i CV'et, derfor er der ingen motivationssektion.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
OUT_DIR = os.path.join(ROOT, 'output')
OUT = os.path.join(OUT_DIR, 'Shahram_Ajloo_GEHealthCare_ProductionEngineerCalibration.docx')
KRAV = os.path.join(ROOT, 'jd', 'GEHealthCare_ProductionEngineerCalibration_krav.txt')
KULTUR = os.path.join(ROOT, 'jd', 'GEHealthCare_ProductionEngineerCalibration_kultur.txt')

NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Production Engineer, Calibration & Maintenance · GE HealthCare, Herlev'
BANNER_RESUME = 'Equipment maintenance and compliance in regulated manufacturing'

# (krav, dokumentation og status) - krav-teksten er identisk med krav-filen.
ROWS = [
    ('Coordinate the site calibration program: schedules, call-in activities, equipment status, due dates and timely completion',
     'Not in my record. Programmes with call-ins and due-date control are not documented. The closest documented work is the preventive maintenance schedule and work order control at Biofos, 2017 to 2022.'),
    ('Internal and external calibration flow: preparation, shipment, return, documentation review and release',
     'Not in my record. External suppliers, documentation control and release steps are documented through service and project handover at Novo Nordisk, Ventek-Air and ELOHVAC.'),
    ('New, returned, overdue, failed or out-of-tolerance equipment assessed and controlled before use',
     'Not in my record as calibration work. Assessment of faults and out-of-tolerance findings is documented in fault-finding and commissioning under GMP at Biofos and Novo Nordisk.'),
    ('SME role in HxGN EAM: asset records, calibration setups, PM schedules, work orders and task plans',
     'Partly documented. CMMS work on asset records, PM schedules and work orders, and asset management with maintenance strategy and systems. HxGN EAM itself is not in my record.'),
    ('Assessments of requirements, criticality, acceptance criteria, methods, frequencies and maintenance needs for calibration',
     'Partly documented. Criticality-based PM planning and failure analysis with FMEA at Biofos. Acceptance criteria and frequencies for calibration are not in my record.'),
    ('Procedures, SOPs and work instructions, developed with equipment owners, SMEs and Quality',
     'Documented. Standard Work, PDCA and 5S at Biofos workshop and store. Procedures written with Quality under GMP and FDA requirements at Novo Nordisk, and ISO 9001-based QMS documentation.'),
    ('Preventive and corrective maintenance for production and test equipment, with minimal disruption',
     'Confirmed in practice. Fault-finding and planned PM on pumps, HVAC and high-voltage switchgear in 24/7 operation at Biofos, with shift work under LOTO, risk assessment and APV.'),
    ('Investigations, risk and product-impact assessments, and input to NC, INV and CAPA where applicable',
     'Documented as method: 5 Whys, Ishikawa, FMEA and A3 in failure analysis. Related quality work in documentation and deviations is confirmed, while the employer and cases are not specified. CAPA-specific cases are not in my record.'),
    ('Supplier coordination: quotations, service activities, documentation and purchase orders',
     'Subcontractor coordination, quotations and tendering at ELOHVAC, Ventek-Air and Novo Nordisk. Purchasing, stock control and order flow confirmed. AGORA purchase orders are not in my record.'),
    ('Audit support: records complete, traceable, compliant and audit-ready',
     'Documented. Well-documented project and process audits, and ISO 9001-based quality management system work with continuous improvement.'),
    ('Performance monitoring and improvement in compliance, availability, data quality and execution',
     'Documented. MTBF, MTTR, OEE and spare parts availability in maintenance work, and a 40 % energy-cost reduction through a PDCA programme at Novo Nordisk.'),
    ("Bachelor's degree in Engineering, Manufacturing, Industrial Engineering, Metrology, Maintenance or a related technical discipline",
     'Confirmed. B.Tech (EQF6) in technology management and mechanical engineering, Copenhagen School of Marine Engineering and Technology Management, 2017 to 2022.'),
    ('Background in preventive maintenance, equipment management or Production Engineering in a regulated environment',
     'Partly documented. Equipment management and planned maintenance at Biofos, GMP qualification at Novo Nordisk. Calibration itself is not in my record.'),
    ('Grasp of calibration principles, equipment control, traceability and manufacturing process requirements',
     'Partly documented. Equipment control, documentation and traceability under GMP at Novo Nordisk. Formal study or practice in calibration principles is not documented.'),
    ('Computerised maintenance or enterprise asset management systems, preferably HxGN EAM or comparable systems',
     'Documented as comparable: CMMS work and asset management with maintenance systems. HxGN EAM is not in my record.'),
    ('Controlled procedures, work instructions and change management processes',
     'Change control and work instructions under GMP and FDA at Novo Nordisk, and handover documentation at Ventek-Air.'),
    ('Coordinating suppliers, service activities, quotations and purchase orders',
     'Tendering, quotations, subcontractors and handover packs at Ventek-Air and ELOHVAC. Purchase orders in a named system are not in my record.'),
    ('GMP and Quality Management System requirements within regulated manufacturing',
     'Confirmed. GMP, FDA and EMA requirements at Novo Nordisk, 2022 to 2024, where qualification work was held to GMP documentation standards. ISO 9001-based quality management system work with audits and continuous improvement.'),
    ('Medical device manufacturing, or another highly regulated manufacturing environment',
     'Partly documented. Highly regulated pharmaceutical manufacturing at Novo Nordisk, 2022 to 2024. Medical device manufacturing is not in my record.'),
    ('Strong analytical and problem-solving skills with high attention to detail',
     'Confirmed in practice. Root-cause analysis, A3 and FMEA, and FAT, SAT and IQ/OQ/PQ documentation with zero critical deviations at handover.'),
    ('Hands-on and practical approach to supporting manufacturing equipment and production operations',
     'Confirmed. Fault-finding at pumps, HVAC and switchgear at Biofos, and commissioning of tanks, process piping and instrumentation at Novo Nordisk.'),
    ('Structured working style with strong ownership and ability to manage recurring deadlines',
     'Shift planning in 24/7 operation at Biofos, and budget, progress and risk control on 37 CAPEX projects at Novo Nordisk.'),
    ('Strong collaboration skills across Manufacturing, Engineering, Quality, Supply Chain and external suppliers',
     'Cross-functional coordination at Novo Nordisk across engineering, procurement and site, and with subcontractors at Ventek-Air.'),
    ('Clear written and verbal communication skills',
     'Documented through reporting and handover documentation: monthly reporting to management and client at Novo Nordisk.'),
    ('Comfortable balancing equipment compliance, production continuity, quality requirements and operational priorities',
     'Shift operation with production continuity, and FAT, SAT and IQ/OQ/PQ work under GMP with a shared plan across parallel organisations.'),
    ('Proactive and improvement-focused approach to equipment reliability and calibration or maintenance processes',
     'Documented for reliability: PDCA, 5S, Standard Work, and failure analysis. Calibration processes specifically are not in my record.'),
]

# Kultur-udtryk fra opslaget, ordret. Skal genfindes ordret i dokumentet.
KULTUR_PHRASES = [
    'hands-on and practical approach',
    'structured working style',
    'strong ownership',
    'high attention to detail',
    'improvement-focused approach',
    'balancing equipment compliance, production continuity, quality requirements',
    'clear written and verbal communication',
    'analytical and problem-solving skills',
    'manage recurring deadlines',
    'collaboration skills across Manufacturing, Engineering, Quality',
]


def write_inputs():
    with open(KRAV, 'w', encoding='utf-8') as f:
        f.write('# Krav fra GE HealthCare · Production Engineer, Calibration & Maintenance (R4048177, Herlev), engelsk, ordret fra opslaget\n')
        for krav, _ in ROWS:
            f.write(krav + '\n')
    with open(KULTUR, 'w', encoding='utf-8') as f:
        f.write('# Arbejdsgiverens egne udtryk fra opslaget R4048177 (engelsk, ordret). Skal genfindes ordret i dokumentet.\n')
        for phrase in KULTUR_PHRASES:
            f.write(phrase + '\n')


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('28 November 2026')
    m.meta('GE HealthCare · Advanced Imaging Solutions, Herlev · R4048177')
    m.para('Dear Hiring Team,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    def sub(text):
        p = m._p(spacing_after=20, spacing_before=60, line=260, justify=False, keep_next=True)
        m._run(p, text, bold=True, color='002B5C')
        return p

    # ------------------------------------------------------------ letter, page 1
    lp('An overdue torque tester or a pressure gauge outside its tolerance can hold a production line as '
       'effectively as a failed motor, and nobody in the schedule sees it coming. The Production Engineer '
       'for calibration and maintenance keeps that risk visible: which equipment is due, which is out of '
       'tolerance, and what each finding means for the product that has already been made with it.')

    sub('Due dates controlled before they become holds')
    lp('The first step is a single status view for every measuring and production asset: due date, last '
       'result, open call-ins and the owner of each item. Calibration call-ins and maintenance windows are '
       'then planned together, so that equipment returns to production on the day it is released. Overdue '
       'items are flagged early enough for the production team to plan around them.')

    sub('Assessment before equipment goes back into use')
    lp('New, returned, failed or out-of-tolerance equipment should be assessed and held until the assessment '
       'is complete. The assessment states the requirement, the criticality, the acceptance criteria and the '
       'effect on product already made. Quality takes the product-impact decision, and the NC, investigation '
       'or CAPA route follows from it. Investigations run on root cause, not on the first explanation.')

    sub('Maintenance that keeps production running')
    lp('Preventive and corrective work on production and test equipment is planned against the production '
       'calendar. Intervals follow criticality and failure history, so that the plans that exist are the ones '
       'the site actually uses. Every intervention ends with a complete work order, because the asset record '
       'is what an auditor will read first.')

    sub('Procedures people can follow at the bench')
    lp('Calibration and maintenance procedures, SOPs and work instructions are written with the equipment owners '
       'and Quality, and tested at the bench before release. Change control keeps them current. Where a procedure '
       'does not match the way the work is done, the gap is reported and closed, not worked around.')

    sub('Suppliers as part of the control system')
    lp('External calibration and service suppliers are part of the same system. Quotations, shipment, '
       'documentation review and release back to production each need a named owner, and purchase orders follow '
       'the same route as the work. The aim is that an external service ends with the same record as an internal one.')

    lp('In the first 90 days I would start with the equipment list and the open calibration items, agree the '
       'critical assets with Manufacturing and Quality, and then bring the procedures and supplier routes into the '
       'same status view. Working hands-on with the production team and the equipment owners is the fastest way to '
       'find where the record and the equipment disagree. I would welcome a conversation about where to start.', after=44)
    lp('Yours sincerely', after=8)
    lp('Shahram Ajloo', after=8)

    # ------------------------------------------------------------ CV, pages 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFILE')
    m.para('Maintenance and asset engineer in 24/7 and GMP-regulated plants. Preventive maintenance and fault-finding '
           'on pumps, HVAC and high-voltage switchgear at Biofos, GMP qualification (FAT, SAT, IQ/OQ/PQ) at Novo '
           'Nordisk, and ISO 9001-based audit and documentation work. Works with CMMS and asset records, and with '
           'maintenance KPIs (MTBF, MTTR, OEE, spare parts availability). Bachelor-level engineering (B.Tech) and '
           'electrically authorised marine engineer (LV/MV/HV). PRINCE2 certified. Hands-on, structured, and able to '
           'keep several tasks and stakeholders moving. Danish native, English professional.', after=32)

    m.section('EQUIPMENT CONTROL AND MAINTENANCE WORK')
    tasks = [
        ('Preventive and corrective maintenance',
         'Pumps, HVAC, high-voltage switchgear and SCADA in 24/7 operation at Biofos, with planned PM and acute fault-finding. '
         'Spare parts flow and stock control.'),
        ('Asset records and CMMS',
         'Asset management with maintenance strategy and systems. PM schedules and work orders in CMMS, with MTBF, MTTR, OEE '
         'and spare parts availability as maintenance KPIs.'),
        ('Valves, pressure-bearing and safety equipment',
         'Maintenance work on valves, pressure-bearing equipment and safety equipment, confirmed in practice.'),
        ('GMP qualification and documentation',
         'FAT, SAT and IQ/OQ/PQ under GMP, FDA and EMA on CIP/SIP systems, tanks, process piping, instrumentation and UPS, '
         'with zero critical deviations at handover.'),
        ('Audits and quality management',
         'Well-documented project and process audits, and ISO 9001-based quality management with PDCA, 5S and Standard Work.'),
        ('Failure analysis and improvement',
         '5 Whys, Ishikawa, FMEA and A3 in failure analysis. A 40 % energy-cost reduction through a PDCA programme at Novo Nordisk.'),
        ('Suppliers and purchasing',
         'Quotations, tendering and subcontractor coordination at ELOHVAC and Ventek-Air. Supply chain, purchasing, stock control '
         'and order flow, confirmed. Supplier dialogue with international suppliers.'),
        ('Leading and developing people',
         'Development of 5 electricians and 3 apprentices through one-to-ones and MUS. Coordination of 25 specialists at Novo Nordisk.'),
    ]
    for head, body in tasks:
        m.bullet(head, body, after=24)

    m.section('EXPERIENCE')
    jobs = [
        ('CTO for the AI department and electrically authorised marine engineer, electrical and ventilation',
         'Data Power Consultant ApS · Copenhagen · 2024 to present',
         [('', 'Responsible for electrical and ventilation work with full P&L responsibility. From November 2026 this includes '
               'the electrical activities previously run through ELOHVAC.'),
          ('', 'Management of 5 electricians and 3 apprentices: daily planning, one-to-ones, MUS and structured training.'),
          ('', 'Responsible for the AI department with 4 to 10 people.')]),
        ('Owner and technical director, electrically authorised marine engineer',
         'ELOHVAC ApS · Copenhagen · May 2023 to November 2026 (company closed)',
         [('', 'Preventive maintenance and fault-finding on electrical, ventilation and climate systems, from emergency '
               'call-outs to handed-over installations.'),
          ('', 'Quotations, schedules, material planning and subcontractors. Productivity gain above 40 % from AI tools '
               'on quotations, schedules and KPI reporting.'),
          ('', 'LOTO, risk assessment and APV at each site start. Zero critical deviations in service agreements.')]),
        ('Senior commissioning engineer and project manager, electrical system',
         'Novo Nordisk A/S · Kalundborg and Bagsværd · November 2022 to July 2024',
         [('', 'FAT, SAT and IQ/OQ/PQ under GMP, FDA and EMA, with zero critical deviations at handover.'),
          ('', 'Cross-functional coordination of 25 specialists across engineering, procurement and site, with 37 concurrent '
               'CAPEX projects.'),
          ('', 'Monthly reporting to management and client. SAP ERP for finance, assets and cost.')]),
        ('Project and workshop manager',
         'Ventek-Air · Copenhagen · January 2022 to November 2022',
         [('', '11 concurrent installation projects from specification to formal handover, with a 14-person team.'),
          ('', 'Tendering, subcontractors, safety documentation and handover packs. Daily board meetings and bottleneck analysis.')]),
        ('Maintenance and operations manager, workshop technician',
         'Biofos (Lynetten) · Copenhagen · August 2017 to January 2022',
         [('', 'Operation and maintenance of pumps, HVAC, high-voltage switchgear and SCADA in 24/7 operation.'),
          ('', 'Shift operation under LOTO, risk assessment, APV and near-miss reporting.'),
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
    m.edu('PRINCE2, certified', 'AXELOS / PeopleCert')
    m.para('Lean and Six Sigma methods applied in practice, not certified: DMAIC, 5S, PDCA, VSM, A3, Kaizen, SMED, '
           'TPM, 5 Whys, Ishikawa and FMEA.', after=48)

    m.section('SKILLS')
    m.models_table('Tools and systems', ('Area', 'Tools'), [
        ('Maintenance and assets', 'CMMS, asset records, PM planning, work orders, MTBF, MTTR, OEE, spare parts'),
        ('GMP and quality', 'GMP, FDA, EMA, FAT, SAT, IQ/OQ/PQ, ISO 9001, audits, change control, deviations'),
        ('Control and automation', 'SCADA, control panels, CTS/BMS, KNX'),
        ('Improvement', 'PDCA, 5S, Standard Work, A3, FMEA, 5 Whys, Ishikawa'),
        ('Projects and economics', 'PRINCE2, budget and schedule control, economic follow-up, SAP ERP'),
        ('Data and AI', 'Python, Power BI, Excel, Claude API, Claude Code'),
    ], widths=(3400, 6946), compact=True)
    m.para('Danish native, spoken and written. English professional, working language in international projects since '
           '2017. Persian native. Driving licence B, manual gearbox.', after=40)

    # ------------------------------------------------------------ requirements matrix, page 4
    m.page_break()
    m.section('REQUIREMENTS MATRIX')
    m.models_table('Opslagets krav og min dokumentation', ('Krav', 'Dokumentation og status'),
                   ROWS, widths=(3600, 6746), compact=True)

    m.save(path, title='Production Engineer, Calibration & Maintenance - GE HealthCare Herlev',
           subject='Application Production Engineer, Calibration & Maintenance, R4048177')
    print(path)


if __name__ == '__main__':
    os.makedirs(OUT_DIR, exist_ok=True)
    write_inputs()
    build(OUT)
