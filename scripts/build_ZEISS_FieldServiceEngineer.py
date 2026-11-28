# -*- coding: utf-8 -*-
"""ZEISS · Field Service Engineer, JR_1055358, Birkerød (Nordic Service), English posting.

English posting -> English document. Masterdesign (scripts/master_design.py): letter page 1, CV pages 2-3,
requirement matrix page 4. Only facts from the master CV and user confirmations.
Not documented, therefore not claimed: a Master's degree (master: "Master's claimes aldrig"), medical-equipment
service, ZEISS instruments, ISO 13485, OEM or customer technical training delivery, travel for this role
(travel 50-75 % was confirmed for another role only), Swedish language (never written).
The posting has no deadline; it says "Posted 9 Days Ago" (about 19 Nov 2026). Recruiter named in posting:
Hayley Lem; letter opens with "Dear Hayley Lem,".
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
OUT_DIR = os.path.join(ROOT, 'output')
OUT = os.path.join(OUT_DIR, 'Shahram_Ajloo_ZEISS_FieldServiceEngineer.docx')
KRAV = os.path.join(ROOT, 'jd', 'ZEISS_FieldServiceEngineer_krav.txt')
KULTUR = os.path.join(ROOT, 'jd', 'ZEISS_FieldServiceEngineer_kultur.txt')

NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'
BANNER_LETTER = 'Field Service Engineer (JR_1055358) · ZEISS, Birkerød'
BANNER_RESUME = 'Installation, maintenance and fault diagnosis of critical electrical, mechanical and HVAC systems'

# (krav verbatim from posting, documentation and status) — 17 requirements
ROWS = [
    ('Master\'s degree in a relevant technical or engineering discipline.',
     'Gap. No Master\'s degree is held. Relevant technical education: elautoriseret maskinmester (LV/MV/HV), Danish Safety Technology Authority, May 2023; '
     'B.Tech (EQF6) in technology management and mechanical engineering, 2017 to 2022; and EQF6 electrical and mechanical design, Tehran, 2000 to 2003.'),
    ('Typically 3–5 years of relevant professional experience, supported by a strong technical background.',
     'Documented. Over 3 years as maintenance and operations manager at Biofos (2017 to 2022), and as owner and technical director at ELOHVAC (May 2023 to November 2026). '
     'Earlier technical work as electromechanical technician and production team leader at ARJ Engineering, 2003 to 2010.'),
    ('Extensive experience in technical customer service, ideally within a complex product or instrument environment.',
     'Partly documented. Service and maintenance of pumps, HVAC, high-voltage switchboards and SCADA at Biofos, with 24/7 fault response. '
     'Commissioning of CIP/SIP systems, tanks, process piping and instrumentation at Novo Nordisk. Medical equipment and ZEISS instruments are not documented.'),
    ('Demonstrated advanced knowledge of mechanical, hardware, software and system diagnostics, installation, maintenance and repair.',
     'Partly documented. Installation, preventive maintenance and repair of electrical, mechanical and HVAC systems, with diagnosis at system level. '
     'Software diagnostics of instruments and medical systems is not documented. Software work is in Data Power, applications for customers.'),
    ('Ability to independently diagnose and resolve complex technical issues, applying sound judgement and practical problem-solving skills.',
     'Documented. Fault diagnosis and repair of industrial electrical and mechanical systems at ARJ. Acute fault diagnosis 24/7 at Biofos, '
     'with root-cause analysis using A3, 5 Why and Ishikawa, and corrective actions.'),
    ('Strong understanding of service processes, performance KPIs and the commercial factors that influence service delivery and customer success.',
     'Documented. Service agreements with response time, quality and delivery KPIs tracked in the P&L. MTBF, MTTR, OEE, spare parts availability and CMMS in operations. '
     'Commercial follow-up on budgets, economy and tenders on projects of DKK 2 to 10 million each at Novo Nordisk and Ventek-Air.'),
    ('Proven ability to build and maintain strong customer relationships, demonstrating a professional and customer-focused approach.',
     'Documented. Commercial customer work at ELOHVAC, from acute call-outs to a handed-over installation for business customers. '
     'Monthly reporting to management and client at Novo Nordisk. Relationship management with subcontractors and suppliers.'),
    ('Excellent planning, organisational and communication skills, with the ability to manage competing priorities independently.',
     'Documented. 37 concurrent CAPEX projects at Novo Nordisk and 11 parallel construction projects at Ventek-Air, with one plan, daily planning boards and bottleneck analysis. '
     'Written decision papers and reporting in Danish and English.'),
    ('Experience supporting and mentoring colleagues, sharing technical knowledge and contributing to team development.',
     'Documented. Structured training of 3 apprentices at ELOHVAC, 1:1 meetings and MUS, and Standard Work for workshop and warehouse teams at Biofos.'),
    ('Willingness to undertake relevant technical training and development to maintain expertise as products and technologies evolve.',
     'Partly documented. AMU refrigeration and air-conditioning (2021), PRINCE2 certification, and STCW courses (2021 to 2023). '
     'The candidate has not confirmed willingness to attend manufacturer training for this role.'),
    ('Carrying out installations, preventive maintenance, upgrades, engineering changes and repairs of ZEISS medical equipment, products and instruments in accordance with company guidelines and quality standards.',
     'Partly documented. Installation, preventive maintenance and repair of industrial systems, with engineering changes under ISO 9001-based quality management. '
     'Medical equipment and ZEISS products are not documented.'),
    ('Completing all required service, quality and expense reports accurately and within agreed timescales.',
     'Documented for service, quality and handover documentation, and monthly reporting to management. Expense reporting is not specifically documented.'),
    ('Desirable: Experience delivering technical training, including on-the-job training and coaching for other service engineers.',
     'Partly documented. Structured training of apprentices and electricians at ELOHVAC, with an apprentice training plan. Technical training for customers or service engineers is not documented.'),
    ('Desirable: Experience acting as a recognised technical expert or subject matter specialist within a service organisation.',
     'Not documented as a recognised expert in a service organisation. Technical responsibility for electrical systems and ventilation in Data Power is documented.'),
    ('Desirable: Experience supporting regional or international service activities and working across multiple product markets.',
     'Partly documented. Projects at Novo Nordisk in Kalundborg and Bagsværd, and AI applications for customers in Data Power. Regional or international service activities are not documented.'),
    ('Desirable: An understanding of commercial service operations and identifying opportunities to improve service performance and generate additional business.',
     'Documented. Service agreements with KPIs in the P&L at ELOHVAC, tender and offer work, and PDCA programme with 40 % lower energy costs at Biofos.'),
    ('Desirable: Experience working within a quality-managed environment, with knowledge of ISO standards and corporate compliance requirements.',
     'Documented. ISO 9001-based quality management with audits and procedures at ELOHVAC, and GMP/FDA/EMA compliance at Novo Nordisk. ISO 13485 is not documented.'),
]

KULTUR_PHRASES = [
    'ZEISS is technology and innovation',
    'committed to responsibility in all its activities',
    'push the boundaries of what is possible',
    'With a strong focus on quality and innovation',
    'Working closely with customers, sales colleagues and the wider service organisation',
    'ensuring equipment reliability, patient safety and excellent customer satisfaction while minimising customer downtime',
    'acting as a trusted technical expert and ambassador for the ZEISS brand',
    'sharing knowledge and best practices, supporting colleagues and contributing to the development of less experienced engineers',
]


def write_inputs():
    with open(KRAV, 'w', encoding='utf-8') as f:
        f.write('# Requirements from ZEISS · Field Service Engineer, JR_1055358, Birkerød, English, verbatim from the posting (required and desirable, plus role responsibilities)\n')
        for krav, _ in ROWS:
            f.write(krav + '\n')
    with open(KULTUR, 'w', encoding='utf-8') as f:
        f.write('# Employer\'s own phrases from the posting (English, verbatim). Must appear verbatim in the document.\n')
        for phrase in KULTUR_PHRASES:
            f.write(phrase + '\n')


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, BANNER_LETTER, 'Måløv, Denmark · +45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo')
    m.meta('28 November 2026')
    m.meta('ZEISS · Birkerød · Nordic Service · JR_1055358 · application via the ZEISS Workday posting')
    m.para('Dear Hayley Lem,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    def sub(text):
        p = m._p(spacing_after=20, spacing_before=60, line=260, justify=False, keep_next=True)
        m._run(p, text, bold=True, color='002B5C')
        return p

    # ------------------------------------------------------------ letter, page 1
    lp('I am applying for the Field Service Engineer role in Birkerød. ZEISS is technology and innovation, and the posting places the service role '
       'in a company that is committed to responsibility in all its activities. The job is about ensuring equipment reliability, patient safety and excellent customer satisfaction '
       'while minimising customer downtime. That is the part of my work I have carried out the longest: diagnosing, repairing and handing back critical systems to the people who depend on them. '
       'The ZEISS teams I read about want engineers who push the boundaries of what is possible. With a strong focus on quality and innovation, that is the standard I have worked to in every service role.')

    sub('Diagnosis and repair when downtime matters')
    lp('At Biofos I was responsible for maintenance and operations of pumps, HVAC, high-voltage switchboards and SCADA in 24/7 operation, '
       'with acute fault diagnosis around the clock. At ARJ Engineering I diagnosed and repaired industrial electrical and mechanical systems, '
       'and I used root-cause analysis with A3, 5 Why and Ishikawa to make the corrective action stick. The method transfers directly to a '
       'technical service visit: establish the failure, isolate the cause, and restore the system with the least downtime.')

    sub('Installation and commissioning under quality control')
    lp('At Novo Nordisk I commissioned CIP/SIP systems, tanks, process piping and instrumentation under GMP, with FAT, SAT and IQ/OQ/PQ, '
       'and handed over with zero critical deviations. At ELOHVAC I ran installations and service from tender to handover, with ISO 9001-based quality management. '
       'Medical equipment is not part of my experience, and I would expect to learn the ZEISS products and their quality requirements in the first months.')

    sub('Service performance and customers')
    lp('Service agreements at ELOHVAC were measured on response time, quality and delivery in the P&L, and in operations I worked with MTBF, MTTR, OEE, '
       'spare parts availability and CMMS. The posting asks for a technical expert who is a trusted partner to customers, '
       'working closely with customers, sales colleagues and the wider service organisation. I have done that in daily work with customers, '
       'in reporting that management and clients could act on, and in handovers that the customer could run without us. '
       'The role also calls for acting as a trusted technical expert and ambassador for the ZEISS brand, which I would take on from the first visit.')

    sub('Sharing knowledge')
    lp('I have trained three apprentices and electricians with a written plan, run 1:1 meetings and MUS, and used Standard Work with the teams. '
       'That is the basis for sharing knowledge and best practices, supporting colleagues and contributing to the development of less experienced engineers, '
       'which is part of this role.')

    lp('I do not hold a Master\'s degree. My technical base is the elautoriseret maskinmester authorisation (LV/MV/HV) and a B.Tech in mechanical engineering. '
       'I would welcome a conversation about which installation and repair tasks you expect the engineer to carry out in the first months, and how the spare parts and planning work fits into that.', after=44)
    lp('Kind regards', after=8)
    lp('Shahram Ajloo', after=8)

    # ------------------------------------------------------------ CV, pages 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFILE')
    m.para('Elautoriseret maskinmester (LV/MV/HV), with more than three years of maintenance, service and fault diagnosis on pumps, HVAC, '
           'high-voltage switchboards and SCADA in 24/7 operation, and installation and handover of electrical systems. '
           'Team leadership from 5 to 25 people, 37 concurrent CAPEX projects at Novo Nordisk, and ISO 9001-based quality management. '
           'No Master\'s degree. Medical equipment is not documented. PRINCE2 certified. Danish and English.', after=32)

    m.section('SERVICE AND TECHNICAL WORK')
    tasks = [
        ('Installation and maintenance',
         'Installation, preventive maintenance and repair of pumps, HVAC, switchboards, UPS and automation systems at Biofos and ELOHVAC.'),
        ('Fault diagnosis',
         'Acute fault diagnosis 24/7 at Biofos. Diagnosis and repair of industrial electrical and mechanical systems at ARJ. Root-cause analysis with A3, 5 Why and Ishikawa.'),
        ('Commissioning',
         'CIP/SIP systems, tanks, process piping and instrumentation under GMP at Novo Nordisk, with FAT, SAT and IQ/OQ/PQ.'),
        ('Service performance',
         'Service agreements with response time, quality and delivery KPIs in the P&L. MTBF, MTTR, OEE, spare parts availability and CMMS.'),
    ]
    for head, body in tasks:
        m.bullet(head, body, after=24)

    m.section('LEADERSHIP, CUSTOMERS AND KNOWLEDGE SHARING')
    tasks = [
        ('Team leadership',
         'A 14-person installation team at Ventek-Air and a 12-person workshop team at ARJ, plus shift operations teams at Biofos.'),
        ('Customer work',
         'Acute call-outs to completed installations for business customers at ELOHVAC. Reporting on the CAPEX portfolio to management and the client at Novo Nordisk.'),
        ('Training',
         'Structured training of 3 apprentices and electricians at ELOHVAC, with a written plan, 1:1 meetings and MUS.'),
        ('Quality',
         'ISO 9001-based quality management, audits and handover documentation at ELOHVAC. GMP/FDA/EMA compliance at Novo Nordisk.'),
    ]
    for head, body in tasks:
        m.bullet(head, body, after=24)

    m.section('EXPERIENCE')
    jobs = [
        ('CTO for the AI department and licensed electrical master craftsman, responsible for electrical and ventilation work',
         'Data Power Consultant ApS · Copenhagen · 2024 to present',
         [('', 'Responsible for the AI and AI coding department with 4 to 10 people. Technical and industrial applications from requirements to handover.'),
          ('', 'Electrical and ventilation work with full P&L responsibility. From November 2026 also the electrical activities from ELOHVAC.'),
          ('', 'Five electricians and three apprentices managed directly.')]),
        ('Owner and technical director, licensed electrical master craftsman',
         'ELOHVAC ApS · Copenhagen · May 2023 to November 2026 (company closed)',
         [('', 'Tenders and calculations, schedules, material management and subcontractors. Full P&L responsibility.'),
          ('', 'Piecework and measurement, with piecework letters and handling of additional and reduced work.')]),
        ('Senior commissioning engineer and project lead, electrical systems',
         'Novo Nordisk A/S · Kalundborg and Bagsværd · November 2022 to July 2024',
         [('', '37 concurrent construction and CAPEX projects, with schedule, economy and risk across engineering, procurement and construction.'),
          ('', 'Cross-functional leadership of 25 specialists. SAP ERP for economy, fixed assets and costs.')]),
        ('Project and workshop leader',
         'Ventek-Air · Copenhagen · January 2022 to November 2022',
         [('', '11 concurrent construction projects from specification to formal handover, with a 14-person team.'),
          ('', 'Tenders, offers, subcontractors and contract basis.')]),
        ('Maintenance and operations manager, workshop technician',
         'Biofos (Lynetten) · Copenhagen · August 2017 to January 2022',
         [('', 'Operation and maintenance of pumps, HVAC, high-voltage switchboards and SCADA in 24/7 operation.'),
          ('', 'Shift operations teams run at management level.')]),
        ('Electromechanical technician and production team leader',
         'ARJ Engineering · Tehran · December 2003 to March 2010',
         [('', 'Twelve mechanics and technicians in a workshop, with shift planning, materials and targets.'),
          ('', 'Fault diagnosis and repair of industrial electrical and mechanical systems, with root-cause analysis and corrective actions.')]),
    ]
    for title, meta, bullets in jobs:
        m.job(title, meta)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('EDUCATION AND CERTIFICATIONS')
    m.edu('Licensed electrical master craftsman (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('B.Tech (EQF6), technology management and mechanical engineering',
          'Copenhagen School of Marine Engineering & Technology Management · 2017 to 2022')
    m.edu('Refrigeration and air-conditioning (AMU)', 'Mercantec · 2021')
    m.edu('PRINCE2, certified', 'AXELOS / PeopleCert')
    m.para('Lean and Six Sigma applied in practice, not certified: DMAIC, 5S, PDCA, VSM, A3, Kaizen, SMED, TPM, '
           '5 Why, Ishikawa and FMEA.', after=48)

    m.section('SKILLS')
    m.models_table('Tools and systems', ('Area', 'Tools'), [
        ('Service and maintenance', 'Installation, preventive maintenance, repair, CMMS, spare parts, MTBF, MTTR, OEE'),
        ('Diagnosis', 'Electrical and mechanical diagnosis, SCADA, root-cause analysis (A3, 5 Why, Ishikawa, FMEA)'),
        ('Quality and compliance', 'ISO 9001, GMP/FDA/EMA, audits, handover documentation, KS'),
        ('Data and tools', 'SAP ERP, Excel, Python, Claude API'),
        ('Leadership', 'MUS, 1:1 meetings, situational leadership (SLII), GROW, Standard Work'),
    ], widths=(3400, 6946), compact=True)
    m.para('Danish and English in writing and speech; English as working language since 2017. Persian native. Driving licence B with manual gearbox.', after=40)

    # ------------------------------------------------------------ requirement matrix, page 4
    m.page_break()
    m.section('REQUIREMENT MATRIX')
    m.models_table('Posting requirements and my documentation', ('Requirement', 'Documentation and status'),
                   ROWS, widths=(3600, 6746), compact=True)

    m.save(path, title='Field Service Engineer - ZEISS',
           subject='Application Field Service Engineer (JR_1055358)')
    print(path)


if __name__ == '__main__':
    os.makedirs(OUT_DIR, exist_ok=True)
    write_inputs()
    build(OUT)
