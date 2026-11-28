# -*- coding: utf-8 -*-
"""Danfoss Climate Solutions · New Product Process Engineer (NPD), req 52809, Tallahassee FL, on-site.

English posting -> English document. Masterdesign (scripts/master_design.py): letter page 1, CV pages 2-3,
requirement matrix page 4. Only facts from the master CV and user confirmations.
Not documented, therefore not claimed: PFMEA facilitation, AIAG/VDA FMEA, APQP/PPAP, control plans, MSA, SPC,
capability studies, CMM, torque and vision systems, 8D, Pareto, 4-Step, MES, US work authorisation,
relocation to Tallahassee, travel willingness for this role. Lean Six Sigma is applied in practice, not certified.
The posting gives no deadline and no named contact; the letter opens with "Dear Hiring Team,".
Double-checks are listed in research/Danfoss_NewProductProcessEngineer_2026-11.md
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
OUT_DIR = os.path.join(ROOT, 'output')
OUT = os.path.join(OUT_DIR, 'Shahram_Ajloo_Danfoss_NewProductProcessEngineer.docx')
KRAV = os.path.join(ROOT, 'jd', 'Danfoss_NewProductProcessEngineer_krav.txt')
KULTUR = os.path.join(ROOT, 'jd', 'Danfoss_NewProductProcessEngineer_kultur.txt')

NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'
BANNER_LETTER = 'New Product Process Engineer (NPD) · Danfoss Climate Solutions, Tallahassee, FL'
BANNER_RESUME = 'Manufacturing readiness, validation and process control from concept to production'

# (requirement from the posting, documentation and status)
ROWS = [
    ("Bachelor's degree in Mechanical, Industrial, Electrical, Manufacturing Engineering, or related engineering discipline, or equivalent relevant experience",
     "Partly documented. B.Tech (EQF6) in technology management and mechanical engineering, Copenhagen School of Marine Engineering & Technology Management, 2017 to 2022, "
     "and the Danish electrical authorisation LV/MV/HV as elautoriseret maskinmester, May 2023. Equivalence to a US engineering bachelor is for Danfoss to assess."),
    ("3+ years of experience in manufacturing/process engineering, industrialization, new product introduction, or project engineering in a manufacturing environment",
     "Documented. Project and process engineering in regulated manufacturing at Novo Nordisk from November 2022 to July 2024, commissioning and validation of process equipment and tanks, "
     "and project management in installation at Ventek-Air from January 2022 and ELOHVAC from May 2023. Industrialisation of a new product line is not in my record."),
    ("Experience coordinating cross-functional projects, actions, risks, schedules, and manufacturing deliverables",
     "Documented. 37 concurrent CAPEX projects at Novo Nordisk with progress, budget, risk and resources across engineering, procurement and installation. "
     "Daily visual management and bottleneck analysis with 14 people at Ventek-Air, with monthly reporting to management."),
    ("Working knowledge of PFMEA and manufacturing quality tools, with experience facilitating or actively participating in PFMEA reviews",
     "Partly documented. FMEA is in my root-cause toolkit alongside A3, 5 Why and Ishikawa, and I have used it in corrective-action work. "
     "I have not facilitated or taken part in a PFMEA review as a formal process FMEA, and that is a gap I would close with the quality team."),
    ("Knowledge of APQP/PPAP, Control Plans, MSA, SPC, capability studies, process validation, and structured root-cause/problem-solving methods",
     "Partly documented. Process validation through FAT, SAT and IQ/OQ/PQ under GMP, FDA and EMA, and root-cause analysis with A3, 5 Why, Ishikawa and FMEA. "
     "APQP, PPAP, control plans, MSA, SPC and capability studies are not documented in my record."),
    ("Strong data analysis, organization, communication, facilitation, and presentation skills",
     "Documented. Monthly reporting to management and the owner at Novo Nordisk, daily planning meetings and facilitation at Ventek-Air, KPI dashboards built in Python and Excel, "
     "and team development conversations and MUS for 5 electricians and 3 apprentices at ELOHVAC."),
    ("Ability to work effectively across Operations, Engineering, Quality, Supply Chain, Maintenance, and external suppliers",
     "Documented. Maintenance and operations at Biofos (2017 to 2022), procurement and engineering coordination at Novo Nordisk, and tender and subcontractor management at Ventek-Air and ELOHVAC. "
     "Quality and supply chain coordination are part of the same project structure."),
    ("Facilitate manufacturing risk assessments and PFMEA activities, ensuring identified risks are addressed through effective process controls, documentation, and validation plans",
     "Partly documented. Risk assessment in regulated projects, including LOTO, risk assessment and APV at site start at ELOHVAC, and documented validation plans and handover packages at Novo Nordisk. "
     "Facilitating PFMEA activities is not documented."),
    ("Drive manufacturing readiness by partnering with engineering, quality, operations, and suppliers on equipment, tooling, process validation, training, and production preparation",
     "Partly documented. Equipment commissioning, FAT and SAT, and process validation under GMP at Novo Nordisk; training of apprentices and electricians; and production preparation in workshop and installation work. "
     "Tooling for production lines is not documented."),
    ("Analyze launch and production challenges, implement corrective actions, and capture lessons learned to strengthen future introductions",
     "Documented. Root-cause analysis with A3, 5 Why and Ishikawa at Novo Nordisk, fault diagnosis with corrective actions at ARJ, and a PDCA programme with 40% lower energy costs at Novo Nordisk. "
     "Lessons learned are written into the project documentation."),
    ("Experience leading NPD/NPI, industrialization, or manufacturing transfer projects (preferred)",
     "Partly documented. Leadership of 37 concurrent CAPEX projects and 11 parallel installation projects. NPD/NPI and manufacturing transfer for a product line are not in my record."),
    ("Experience as a PFMEA facilitator or coordinator and familiarity with AIAG/VDA FMEA methodology (preferred)",
     "Not documented. My FMEA work is root-cause analysis, not PFMEA facilitation, and the AIAG/VDA methodology is not in my record."),
    ("Experience with project management tools and structured project and risk management methods (preferred)",
     "Documented. PRINCE2 certified. Microsoft Project as the planning tool, RACI, and structured risk registers in the CAPEX and installation projects."),
    ("Familiarity with SAP ERP concepts and manufacturing data systems (preferred)",
     "Partly documented. SAP ERP for finance, fixed assets and cost at Novo Nordisk. MES and manufacturing execution data systems are not documented."),
    ("Lean Manufacturing and Six Sigma, and structured problem-solving experience (4-Step, 8D, Pareto, Cause and Effect, 5-Why) (preferred)",
     "Partly documented. Lean and Six Sigma are applied in practice, not certified. 5 Why, Ishikawa and A3 are in use. 4-Step, 8D and Pareto are not in my record."),
    ("Experience with automated assembly or test equipment, controls, PLCs, vision, torque, CMM, or manufacturing test equipment (preferred)",
     "Partly documented. FAT and SAT of test and process equipment at Novo Nordisk and SCADA-supported operation at Biofos. "
     "Led work on PLC-controlled equipment, scope and period not specified. Vision, torque, CMM and automated assembly are not documented."),
    ("Full-time, on-site role in Tallahassee, FL, US",
     "Not confirmed. US work authorisation and relocation to Tallahassee are not documented for this role. Flagged for double-check before any submission."),
    ("English at professional level",
     "Documented. English as working language in international projects since 2017, and professional use today in writing and speech."),
]

KULTUR_PHRASES = [
    'We promote from within',
    'flexibility, autonomy, and support',
    'healthy work-life balance',
    'inclusive work environment where people of all backgrounds are respected',
    'where your career can go with us',
    'launched safely, efficiently, and with the quality our customers expect',
    'manufacturing readiness for new product introductions',
    'long-term operational excellence',
]


def write_inputs():
    with open(KRAV, 'w', encoding='utf-8') as f:
        f.write('# Requirements from Danfoss Climate Solutions, New Product Process Engineer (NPD, req 52809, Tallahassee FL), English, from the posting\n')
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
    m.meta('Danfoss Climate Solutions · Tallahassee, FL, US · req 52809 · posting submitted via the Danfoss careers site')
    m.para('Dear Hiring Team,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    def sub(text):
        p = m._p(spacing_after=20, spacing_before=60, line=260, justify=False, keep_next=True)
        m._run(p, text, bold=True, color='002B5C')
        return p

    # ------------------------------------------------------------ letter, page 1
    lp('A product that works in development can still fail on the line. The posting puts manufacturing readiness for new '
       'product introductions at the centre of the role: new products have to be launched safely, efficiently, and with the quality our customers expect, and the risks '
       'have to be found while the design can still change. That is the job I would want at Danfoss Climate Solutions.')

    sub('Risk before the first part')
    lp('A process FMEA is where the team agrees on the failure modes, the controls and the validation before the process '
       'is frozen. The posting asks for facilitation of PFMEA reviews under the AIAG/VDA method. I know FMEA as a root-cause '
       'tool, and I have used it in corrective-action work, but I have not facilitated a PFMEA under that method. '
       'I would learn the structure with the quality team before the first review, not during it.')

    sub('Evidence the line can keep producing')
    lp('Manufacturing readiness needs evidence that the process holds after handover. In validated environments that means '
       'FAT, SAT and IQ/OQ/PQ, with records that follow the equipment. The quality tools the posting names are APQP, PPAP, '
       'control plans, MSA, SPC and capability studies. Those are the areas where I would work closest with quality, rather than '
       'claim prior use.')

    sub('One readiness plan with named owners')
    lp('Engineering, quality, operations, maintenance and suppliers each carry a different part of a launch. The tool that '
       'keeps them aligned is one readiness plan with owners, dates and open risks, reviewed on a fixed rhythm. '
       'I have run daily planning and monthly reporting on that basis.')

    sub('Lessons that reach the next launch')
    lp('Corrective actions help only when they change the next project. The posting asks for lessons learned that strengthen '
       'future introductions, and that means writing them into the readiness template and the control plan, not into a '
       'closing report. This is how a team builds long-term operational excellence rather than fixing the same launch twice.')

    sub('What is new to me')
    lp('PFMEA facilitation under AIAG/VDA, APQP and PPAP, MSA, SPC, CMM and vision systems, and US plant context are not '
       'part of my documented experience. I would learn them with the people who already run them at this site.')

    lp('The posting says We promote from within, and it describes flexibility, autonomy, and support, a healthy work-life '
       'balance and an inclusive work environment where people of all backgrounds are respected. I would welcome a conversation '
       'about the first launch on the list, and about where your career can go with us.', after=44)
    lp('Kind regards,', after=8)
    lp('Shahram Ajloo', after=8)

    # ------------------------------------------------------------ CV, pages 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFILE')
    m.para('Electrically authorised mechanical engineer (elautoriseret maskinmester, LV/MV/HV, Denmark) with project and process '
           'engineering in regulated manufacturing. Commissioning, FAT, SAT and IQ/OQ/PQ under GMP, FDA and EMA at Novo Nordisk, and '
           'SCADA-supported operation of pumps, HVAC and HV switchgear at Biofos. Managed progress, budget and risk across 37 concurrent '
           'CAPEX projects. PRINCE2 certified. Lean and Six Sigma applied in practice. Danish and English.', after=32)

    m.section('VALIDATION AND READINESS')
    tasks = [
        ('Process validation',
         'FAT, SAT and IQ/OQ/PQ under GMP, FDA and EMA at Novo Nordisk, with zero critical deviations at handover.'),
        ('Commissioning and handover',
         'Commissioning of tanks, process piping, CIP/SIP systems and instrumentation, with validation packages and handover documentation.'),
        ('Risk and controls',
         'LOTO, risk assessment and APV at each site start at ELOHVAC. FMEA used in root-cause analysis and corrective actions.'),
        ('Corrective actions',
         'Fault diagnosis at ARJ and root-cause analysis at Novo Nordisk, with A3, 5 Why and Ishikawa.'),
    ]
    for head, body in tasks:
        m.bullet(head, body, after=24)

    m.section('PROJECT AND PROGRAMME LEADERSHIP')
    tasks = [
        ('Capital projects',
         '37 concurrent CAPEX projects at Novo Nordisk (DKK 2 to 10 million each): progress, budget, risk and resources across engineering, procurement and installation, with monthly reporting to management and the owner.'),
        ('Installation projects',
         '11 parallel installation projects at Ventek-Air from specification to formal handover, with a 14-person team and daily visual management.'),
        ('Suppliers and maintenance',
         'Tender, quotation and subcontractor work at Ventek-Air and ELOHVAC. Maintenance of pumps, HVAC and switchgear at Biofos, with spare-parts flow and 5S on the workshop floor.'),
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
          ('', 'Electrical engineering and ventilation with full P&L responsibility. From November 2026 also the electrical activities of ELOHVAC.'),
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
        ('Validation and test', 'FAT, SAT, IQ/OQ/PQ, GMP documentation, CIP/SIP, process piping, instrumentation, test equipment'),
        ('Controls', 'SCADA, control panels, CTS/BMS, KNX, HV switchgear'),
        ('Maintenance and quality', 'Preventive maintenance, CMMS, spare parts, MTBF, MTTR, OEE, ISO 9001, audits'),
        ('Improvement and risk', 'PDCA, 5S, Standard Work, A3, FMEA in root-cause work, 5 Why, Ishikawa, DMAIC, VSM'),
        ('Digital and ERP', 'SAP ERP, Microsoft Project, Excel, Python, Claude API'),
    ], widths=(3400, 6946), compact=True)
    m.para('Danish and English, English as working language since 2017. Persian native. Driving licence category B.', after=40)

    # ------------------------------------------------------------ requirement matrix, page 4
    m.page_break()
    m.section('REQUIREMENT MATRIX')
    m.models_table('Posting requirements and my documentation', ('Requirement', 'Documentation and status'),
                   ROWS, widths=(3600, 6746), compact=True)

    m.save(path, title='New Product Process Engineer (NPD) - Danfoss Climate Solutions',
           subject='Application: New Product Process Engineer, req 52809')
    print(path)


if __name__ == '__main__':
    os.makedirs(OUT_DIR, exist_ok=True)
    write_inputs()
    build(OUT)
