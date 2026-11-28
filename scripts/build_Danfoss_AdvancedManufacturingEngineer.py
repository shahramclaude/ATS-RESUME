# -*- coding: utf-8 -*-
"""Danfoss Climate Solutions · Advanced Manufacturing Engineer (req 52222), Tallahassee FL, on-site.

English posting -> English document. Masterdesign (scripts/master_design.py): letter page 1, CV pages 2-3,
requirement matrix page 4. Only facts from the master CV and user confirmations.
Not documented, therefore not claimed: robotics, vision systems, AGV/AMR, CNC machining centres,
Siemens OpCenter, Ignition, MES deployment, PLC programming, US work authorisation, relocation to Tallahassee,
travel willingness for this role. Lean Six Sigma is applied in practice, not certified.
The posting gives no deadline and no named contact; the letter opens with "Dear Hiring Team,".
Double-checks are listed in the research note: research/Danfoss_AdvancedManufacturingEngineer_2026-11.md
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
OUT_DIR = os.path.join(ROOT, 'output')
OUT = os.path.join(OUT_DIR, 'Shahram_Ajloo_Danfoss_AdvancedManufacturingEngineer.docx')
KRAV = os.path.join(ROOT, 'jd', 'Danfoss_AdvancedManufacturingEngineer_krav.txt')
KULTUR = os.path.join(ROOT, 'jd', 'Danfoss_AdvancedManufacturingEngineer_kultur.txt')

NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'
BANNER_LETTER = 'Advanced Manufacturing Engineer · Danfoss Climate Solutions, Tallahassee, FL'
BANNER_RESUME = 'Automation, testing and process validation from equipment to scale-up'

# (requirement from the posting, documentation and status)
ROWS = [
    ("Bachelor's degree in Manufacturing Engineering, Mechanical Engineering, Industrial Engineering, Electrical Engineering, Mechatronics, or a related technical field, or equivalent experience",
     "Partly documented. B.Tech (EQF6) in technology management and mechanical engineering, Copenhagen School of Marine Engineering & Technology Management, 2017 to 2022, "
     "and the Danish electrical authorisation LV/MV/HV as elautoriseret maskinmester, May 2023. The B.Tech is not a Bachelor of Engineering under US terms, so equivalence is for Danfoss to assess."),
    ("Typically 5+ years of experience in manufacturing engineering, advanced manufacturing, industrial engineering, service engineering, or related operational environments",
     "Documented. Operations, service and engineering roles from 2003 to today: ARJ Engineering (2003 to 2010), Biofos (2017 to 2022), Ventek-Air (2022), "
     "Novo Nordisk (2022 to 2024), ELOHVAC (2023 to 2026) and Data Power (2024 to today). Manufacturing engineering in the strict sense is shorter, so the match is operational rather than titled."),
    ('Demonstrated experience implementing manufacturing technologies, process automation, testing systems, and continuous improvement initiatives in a production environment',
     "Documented. FAT, SAT and IQ/OQ/PQ for process equipment and testing under GMP, FDA and EMA at Novo Nordisk, with zero critical deviations at handover. "
     "PDCA programme with 40% lower energy costs at Novo Nordisk. Automation and SCADA-based operation of pumps, HVAC and HV switchgear at Biofos."),
    ('Proven ability to lead capital equipment, process development, or technology deployment projects while collaborating across multiple functions and stakeholders',
     "Documented. 37 concurrent CAPEX projects at Novo Nordisk (DKK 2 to 10 million each) with cross-functional coordination across engineering, procurement and installation, "
     "and 11 parallel installation projects at Ventek-Air from specification to handover."),
    ('Strong understanding of manufacturing processes, industrial controls, process validation, ERP/MES-driven operations, and structured problem-solving methodologies',
     "Partly documented. Process validation (IQ/OQ/PQ, FAT/SAT) and structured problem solving with A3, 5 Why and Ishikawa. SAP ERP for finance, fixed assets and cost. "
     "Industrial controls: SCADA and building automation (CTS/BMS, KNX). MES is not documented."),
    ('Lead automation, advanced manufacturing, and Industry 4.0 initiatives that improve safety, quality, throughput, and operational efficiency across manufacturing and aftermarket operations',
     "Partly documented. Automation and SCADA-supported operation of critical plant at Biofos, and continuous improvement in GMP environments at Novo Nordisk. "
     "Industry 4.0 programmes, robotics and aftermarket operations are not documented."),
    ('Develop and implement manufacturing processes, testing systems, and standardized workflows that enable consistent performance and support global operational excellence',
     "Documented. Standard Work, 5S and PDCA on workshop and warehouse floors at Biofos. Validated test and handover packages at Novo Nordisk. "
     "Global operational excellence across several sites is not documented."),
    ('Drive equipment deployment, facility expansion, and new product industrialization projects by creating scalable production solutions, optimizing material flow, and increasing manufacturing capacity',
     "Partly documented. Equipment deployment and commissioning at Novo Nordisk, and installation projects from specification to handover at Ventek-Air. "
     "Material flow and capacity work on a production line are not documented in my CV."),
    ('Partner with cross-functional teams and external suppliers to identify, evaluate, and integrate new technologies that strengthen manufacturing capabilities and support long-term business growth',
     "Documented. Tender, quotation and subcontractor management at Ventek-Air and ELOHVAC, and supplier coordination for procurement at Novo Nordisk. "
     "Evaluating robotics, vision systems or AGV/AMR vendors is not documented."),
    ('Lead continuous improvement efforts through Lean Manufacturing, Six Sigma, and data-driven problem solving to reduce waste, improve productivity, and share best practices across global sites',
     "Documented in practice, not certified. DMAIC, 5S, PDCA, VSM, A3, Kaizen, SMED, TPM, 5 Why, Ishikawa and FMEA. Data-driven work with KPI dashboards, tested in Python and Claude API. "
     "Sharing practice across global sites is not documented."),
    ('Lean Six Sigma certification (preferred)',
     "Not held. The methods are applied in practice. PRINCE2 is a certified project management qualification, but it is not a Lean Six Sigma certificate."),
    ('Controls engineering expertise: PLC, HMI, SCADA, industrial networking, motion control, and machine safety (preferred)',
     "Partly documented. SCADA-supported operation of pumps, HVAC and HV switchgear at Biofos, CTS/BMS and KNX in building automation, and LOTO, risk assessment and APV for machine work. "
     "PLC programming, HMI development, motion control and networking are not documented. I led work on PLC-controlled equipment; scope and period are not specified in my record."),
    ('Deployment of robotics, vision systems, AGVs/AMRs, CNC machining centers, digital work instructions, manufacturing analytics platforms, Siemens OpCenter, or Ignition (preferred)',
     "Not documented. Digital work instructions and analytics platforms are in my practice (Python, KPI dashboards). Robotics, vision, AGV/AMR, CNC, Siemens OpCenter and Ignition are not in my record."),
    ('Full-time, on-site role in Tallahassee, FL, US',
     "Not confirmed. Role location and US work authorisation are not documented in my record, and relocation to Tallahassee is not confirmed for this role. "
     "Flagged for double-check before any submission."),
    ('English at professional level',
     "Documented. English as working language in international projects since 2017, and professional use today in writing and speech."),
]

KULTUR_PHRASES = [
    'We promote from within',
    'flexibility, autonomy, and support',
    'healthy work-life balance',
    'inclusive work environment where people of all backgrounds are respected',
    'measurable business impact',
    'scalable manufacturing solutions',
    'global operational excellence',
    'where your career can go with us',
]


def write_inputs():
    with open(KRAV, 'w', encoding='utf-8') as f:
        f.write('# Requirements from Danfoss Climate Solutions, Advanced Manufacturing Engineer (req 52222, Tallahassee FL), English, from the posting\n')
        for krav, _ in ROWS:
            f.write(krav + '\n')
    with open(KULTUR, 'w', encoding='utf-8') as f:
        f.write('# Employer expressions from the posting (English, verbatim). Must appear verbatim in the document.\n')
        for phrase in KULTUR_PHRASES:
            f.write(phrase + '\n')


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, BANNER_LETTER, 'Måløv, Denmark · +45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo')
    m.meta('28 November 2026')
    m.meta('Danfoss Climate Solutions · Tallahassee, FL, US · req 52222 · posting submitted via the Danfoss careers site')
    m.para('Dear Hiring Team,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    def sub(text):
        p = m._p(spacing_after=20, spacing_before=60, line=260, justify=False, keep_next=True)
        m._run(p, text, bold=True, color='002B5C')
        return p

    # ------------------------------------------------------------ letter, page 1
    lp('The posting describes a role that moves automation, testing and standard work from a single site into '
       'production that can scale. Equipment deployment, facility expansion and new product industrialisation all depend '
       'on the same thing: a manufacturing process that holds when it is copied to the next line, the next plant or the '
       'next region. That is the problem I want to work on as Advanced Manufacturing Engineer at Danfoss Climate Solutions.')

    sub('Testing that holds up when it is copied')
    lp('Automated testing only pays off when the test plan, the acceptance criteria and the records follow the equipment '
       'from the first installation to the aftermarket. In validated environments we used IQ, OQ and PQ for this, and the same '
       'discipline suits a production line that has to be reproduced at several sites. The posting asks for scalable manufacturing solutions '
       'and measurable business impact, and a test that proves the same thing at every site is where both start. The first step is to agree what the test '
       'proves and what it does not.')

    sub('Controls, MES and the people who run the line')
    lp('A PLC, an HMI, a SCADA layer and an ERP order are only useful when they agree on what was built and when. The '
       'interfaces between controls, MES and ERP are where most scale-up problems show up. I would start with the data that '
       'operators and quality already trust, and make the automation match that data, not the other way round.')

    sub('Lean with data, applied at the line')
    lp('Continuous improvement is part of how I work: value stream maps, 5S, PDCA and structured root-cause analysis. I have applied '
       'Six Sigma tools in practice but I do not hold a certificate, and I would rather say so than imply otherwise. The posting asks for '
       'data-driven problem solving that reduces waste and is shared across sites. That is a question of which problems are '
       'worth fixing first and how the result is written down for the next team.')

    sub('Choosing technology with the suppliers')
    lp('Robotics, vision systems and AGVs or AMRs each change the material flow and the staffing of a cell. The useful question '
       'is which technology fits the product mix and the volume at this site, and what it takes to run it after go-live. '
       'I would bring a structured evaluation with suppliers, including the aftermarket and service consequences, before any '
       'capital decision.')

    sub('What is new to me')
    lp('Robotics, vision systems, AGVs and AMRs, CNC machining centres, Siemens OpCenter and Ignition are not part of my '
       'documented experience. Neither is manufacturing in a US plant or US regulation. I would learn these with the '
       'engineers who already run them, and I would document what I learn in the same way as the rest of the work.')

    lp('A standard supports global operational excellence only when someone who never saw the original work can follow it. '
       'The posting says We promote from within, and it describes flexibility, autonomy, and support, a healthy work-life balance and an inclusive work environment '
       'where people of all backgrounds are respected. Those conditions suit the work of scaling a process. I would welcome a '
       'conversation about which capital project comes first, and about where your career can go with us.', after=44)
    lp('Kind regards,', after=8)
    lp('Shahram Ajloo', after=8)

    # ------------------------------------------------------------ CV, pages 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFILE')
    m.para('Electrically authorised mechanical engineer (elautoriseret maskinmester, LV/MV/HV, Denmark) with operations, '
           'service and engineering experience from 2003. Commissioning and test of process equipment under GMP, FDA and EMA at '
           'Novo Nordisk, and SCADA-supported operation of pumps, HVAC and HV switchgear at Biofos. Managed progress, budget and risk across 37 '
           'concurrent CAPEX projects and 11 parallel installation projects. PRINCE2 certified. Lean and Six Sigma applied in practice. '
           'Danish and English.', after=32)

    m.section('MANUFACTURING, TEST AND AUTOMATION')
    tasks = [
        ('Equipment deployment and commissioning',
         'FAT, SAT and IQ/OQ/PQ for process equipment at Novo Nordisk, with zero critical deviations at handover. '
         'Commissioning of tanks, process piping, CIP/SIP systems and instrumentation.'),
        ('Automation and controls',
         'SCADA-supported operation of pumps, HVAC, HV switchgear and automation at Biofos, 2017 to 2022. CTS/BMS and KNX in building automation.'),
        ('Test and validation',
         'Validation documentation and handover packages under GMP, FDA and EMA. Acceptance testing before equipment left the site.'),
        ('Continuous improvement',
         'PDCA programme with 40% lower energy costs at Novo Nordisk. Standard Work, 5S and A3 on workshop and warehouse floors at Biofos.'),
        ('Problem solving',
         'Root-cause analysis with A3, 5 Why, Ishikawa and FMEA. Corrective actions in the field and in the workshop.'),
    ]
    for head, body in tasks:
        m.bullet(head, body, after=24)

    m.section('PROJECT AND PROGRAMME LEADERSHIP')
    tasks = [
        ('Capital projects',
         '37 concurrent CAPEX projects at Novo Nordisk (DKK 2 to 10 million each): progress, budget, risk and resources across engineering, procurement and installation. '
         'Monthly reporting to management and the owner.'),
        ('Installation projects',
         '11 parallel installation projects at Ventek-Air from specification to formal handover, with a 14-person team and daily visual management.'),
        ('Suppliers and subcontractors',
         'Tender and quotation work, subcontractor management and handover packages at Ventek-Air and ELOHVAC. SAP ERP for cost and fixed assets.'),
        ('Team leadership',
         'Cross-functional coordination of 25 specialists at Novo Nordisk. Management of 5 electricians and 3 apprentices at ELOHVAC.'),
    ]
    for head, body in tasks:
        m.bullet(head, body, after=24)

    m.section('PROFESSIONAL EXPERIENCE')
    jobs = [
        ('CTO for the AI department and electrically authorised mechanical engineer',
         'Data Power Consultant ApS · Copenhagen · 2024 to today',
         [('', 'Responsible for the AI and AI coding department with 4 to 10 people. Technical and industrial applications from requirements to handover.'),
          ('', 'Electrical engineering and ventilation with full P&L responsibility, including piece-rate work and measurement. From November 2026 also the electrical activities of ELOHVAC.'),
          ('', 'Daily planning and development of 5 electricians and 3 apprentices.')]),
        ('Owner and technical director, electrically authorised mechanical engineer',
         'ELOHVAC ApS · Copenhagen · May 2023 to November 2026 (company closed)',
         [('', 'Installation, fault-finding and preventive maintenance on electrical, ventilation and HVAC systems.'),
          ('', 'Quotation and calculation, schedules, materials and subcontractors. LOTO, risk assessment and APV at every site start.')]),
        ('Senior commissioning engineer and project manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg and Bagsværd · November 2022 to July 2024',
         [('', 'FAT, SAT and IQ/OQ/PQ under GMP, FDA and EMA, with zero critical deviations at handover.'),
          ('', 'Cross-functional coordination of 25 specialists and 37 concurrent CAPEX projects.')]),
        ('Project and workshop manager',
         'Ventek-Air · Copenhagen · January 2022 to November 2022',
         [('', '11 concurrent installation projects from specification to formal handover, with a 14-person team.'),
          ('', 'Tenders, subcontractors, safety documentation and handover packages.')]),
        ('Maintenance and operations manager, workshop technician',
         'Biofos (Lynetten) · Copenhagen · August 2017 to January 2022',
         [('', 'Operation and maintenance of pumps, HVAC, HV switchgear and SCADA in 24/7 operation at a wastewater treatment plant.'),
          ('', 'Shift team leadership at management level and team leadership at other levels.')]),
        ('Electromechanical technician and production team leader',
         'ARJ Engineering · Tehran · December 2003 to March 2010',
         [('', 'Led 12 mechanics and technicians in the workshop: shift planning, materials and targets.'),
          ('', 'Fault diagnosis and repair of industrial electrical and mechanical equipment, with root-cause analysis.')]),
    ]
    for title, meta, bullets in jobs:
        m.job(title, meta)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('EDUCATION AND CERTIFICATIONS')
    m.edu('Elautoriseret maskinmester (LV/MV/HV), electrically authorised mechanical engineer', 'Danish Safety Technology Authority · May 2023')
    m.edu('B.Tech (EQF6), technology management and mechanical engineering',
          'Copenhagen School of Marine Engineering & Technology Management · 2017 to 2022')
    m.edu('Refrigeration and air conditioning (AMU)', 'Mercantec · 2021')
    m.edu('PRINCE2, certified', 'AXELOS / PeopleCert')
    m.para('Applied in practice, not certified: Lean, Six Sigma, DMAIC, 5S, PDCA, VSM, A3, Kaizen, SMED, TPM, '
           '5 Why, Ishikawa and FMEA.', after=48)

    m.section('SKILLS AND TOOLS')
    m.models_table('Tools and systems', ('Area', 'Tools'), [
        ('Manufacturing and test', 'Commissioning, FAT, SAT, IQ/OQ/PQ, process piping, instrumentation, tanks, CIP/SIP'),
        ('Controls', 'SCADA, control panels, CTS/BMS, KNX, HV switchgear'),
        ('Maintenance and quality', 'Preventive maintenance, CMMS, spare parts, MTBF, MTTR, OEE, ISO 9001, audits, GMP documentation'),
        ('Improvement', 'PDCA, 5S, Standard Work, A3, FMEA, 5 Why, Ishikawa, DMAIC, VSM'),
        ('Digital and ERP', 'SAP ERP, Microsoft Project, Excel, Python, Claude API'),
    ], widths=(3400, 6946), compact=True)
    m.para('Danish and English, English as working language since 2017. Persian native. Driving licence category B.', after=40)

    # ------------------------------------------------------------ requirement matrix, page 4
    m.page_break()
    m.section('REQUIREMENT MATRIX')
    m.models_table('Posting requirements and my documentation', ('Requirement', 'Documentation and status'),
                   ROWS, widths=(3600, 6746), compact=True)

    m.save(path, title='Advanced Manufacturing Engineer - Danfoss Climate Solutions',
           subject='Application: Advanced Manufacturing Engineer, req 52222')
    print(path)


if __name__ == '__main__':
    os.makedirs(OUT_DIR, exist_ok=True)
    write_inputs()
    build(OUT)
