# -*- coding: utf-8 -*-
"""Bavarian Nordic · Global Reliability & Maintenance Specialist (JR101652).

Engelsk opslag -> engelsk dokument. Masterdesign (scripts/master_design.py):
brev side 1, CV side 2-3, kravmatrix side 4.

Kun fakta fra master-CV'et og brugerbekræftelser. Ikke: RCM/FMECA som ledet metode,
CMMS-implementering, metrologi/kalibrering, tysk, rejse 30 dage, flytning til Kvistgaard eller Bern.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
OUT_DIR = os.path.join(ROOT, 'output')
OUT = os.path.join(OUT_DIR, 'Shahram_Ajloo_BavarianNordic_GlobalReliabilityMaintenance.docx')

NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Global Reliability & Maintenance Specialist · JR101652'
BANNER_RESUME = 'Maintenance, reliability and GMP-regulated asset work'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('28 November 2026')
    m.meta('Bavarian Nordic · Global Engineering · Kvistgaard')
    m.para('Dear Global Engineering hiring team,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    def sub(text):
        p = m._p(spacing_after=20, spacing_before=60, line=260, justify=False, keep_next=True)
        m._run(p, text, bold=True, color='002B5C')
        return p

    # ------------------------------------------------------------ letter, page 1
    lp('A GMP plant runs on equipment that has to be available on the day it is needed, and every '
       'maintenance decision leaves a record that an auditor can follow. The role asks for one '
       'global policy that sites can use in real life, so that maintenance moves from reactive and '
       'time-based work toward risk-based, data-driven decisions, without losing the compliance '
       'trail. The first test of that policy is the CMMS, because the asset data it holds decides '
       'what the reliability methods can show.')

    sub('Asset data before method')
    lp('Risk-based maintenance is only as good as the asset list behind it. Before any criticality '
       'ranking, I would check the asset hierarchy, the failure codes and the preventive plans at one '
       'pilot site against its work-order history. Where the history is thin, the ranking is a '
       'hypothesis, and the policy should say so. Once the data is clean, FMEA workshops with the site '
       'team give the first criticality list. RCM is the method I would add where a site needs a full '
       'review of a system, not as a template for every asset.')

    sub('A policy the sites can follow')
    lp('A pragmatic policy has one page of principle, and procedures that a technician can follow at '
       'the equipment. Each change to a preventive plan or a critical spare needs a stated reason, a '
       'named owner and a signature, because that is what GMP expects to see. I would write the '
       'procedures with the Quality function at the first site, check them against the next audit '
       'finding, and then roll them out. That order keeps good engineering practices in the policy '
       'rather than on paper only.')

    sub('Metrology and maintenance in one list')
    lp('Calibration and maintenance intervals often sit in separate systems and drift apart. I would '
       'link them in the CMMS through the asset criticality, and review the shared list with the Global '
       'Metrology Process Owner every quarter. The aim is that a sensor is calibrated because it matters '
       'to the process, not because a calendar says so. The same review gives the Reliability Network a '
       'common language for MTBF, MTTR and OEE, so that a number from one site means the same at the next.')

    sub('A reliability network that works across sites')
    lp('A network needs named people at each site, a short standing meeting, and a shared log of what '
       'was tried and what worked. I would ask each site for one reliability contact, set up a monthly '
       'review of the failure data, and publish the outcome of each initiative, including the ones that '
       'did not work. Sharing what works is the quickest way to build capability without adding '
       'reporting that nobody reads. Stakeholders management and relations matter most in the first '
       'six months, when sites still see the policy as headquarters\' idea.')

    sub('Projects that start with the asset')
    lp('Reliability input has the most effect at design freeze, when changes are still cheap. I would '
       'review each new utility or equipment project with the sites\' maintenance lead, using FMEA and the '
       'lessons from the existing asset base, so that maintainability is in the specification before the '
       'equipment is ordered. The CMMS record for each new asset is set up at handover, not after.')

    lp('I would like to help shape Maintenance and Reliability across Bavarian Nordic, starting with the '
       'CMMS data and the first pilot site. A conversation about which site should go first, and how the '
       'global and local responsibilities split in practice, would be the right next step.', after=44)
    lp('Yours sincerely', after=8)
    lp('Shahram Ajloo', after=8)

    # ------------------------------------------------------------ CV, pages 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFILE')
    m.para('Background in 24/7 industrial plants, with GMP, FDA and EMA '
           'qualification work at Novo Nordisk and preventive maintenance and acute fault-finding at '
           'Biofos. Works with FMEA, root-cause analysis and KPIs (MTBF, MTTR, OEE, spare parts '
           'availability), and with CMMS in maintenance work. Electrically authorised marine engineer '
           '(LV/MV/HV) and PRINCE2 certified. Danish native, English professional. German is not held.',
           after=32)

    m.section('MAINTENANCE AND RELIABILITY WORK')
    tasks = [
        ('Failure analysis and RCA',
         'Root-cause analysis with 5 Whys, Ishikawa, FMEA and A3 on electrical and mechanical faults at '
         'Novo Nordisk and Biofos. Corrective actions tracked to closure.'),
        ('Preventive and corrective work',
         'Preventive maintenance of pumps, HVAC, high-voltage switchgear and SCADA in 24/7 operation at '
         'Biofos, alongside acute fault-finding. Valves, pressure equipment and safety equipment.'),
        ('KPIs in practice',
         'MTBF, MTTR, OEE and spare parts availability in maintenance work, with KPI dashboards in Python '
         'and Power BI that turn the figures into actions.'),
        ('Asset data in CMMS',
         'Work in CMMS on asset data, maintenance plans and work-order history in maintenance work. Asset '
         'management and maintenance strategy and systems.'),
        ('GMP-regulated equipment and utilities',
         'FAT, SAT and IQ/OQ/PQ under GMP, FDA and EMA at Novo Nordisk on tanks, CIP/SIP systems, process '
         'piping, instrumentation, UPS and emergency lighting, with zero critical deviations at handover.'),
        ('Standard work and continuous improvement',
         '5S, Standard Work and PDCA in workshop and stores at Biofos. Lean and Six Sigma methods applied '
         'in practice, not certified.'),
    ]
    for head, body in tasks:
        m.bullet(head, body, after=24)

    m.section('EXPERIENCE')
    jobs = [
        ('CTO for the AI department and electrically authorised marine engineer, electrical and ventilation',
         'Data Power Consultant ApS · Copenhagen · 2024 to present',
         [('', 'Responsible for the AI and AI coding department, 4 to 10 people. Electrical and ventilation work, '
               'including the electrical activities from ELOHVAC since November 2026, with full P&L responsibility.'),
          ('', 'Matrix leadership of two parallel organisations with one shared plan and written priorities.'),
          ('', 'Daily management of 5 electricians and 3 apprentices.')]),
        ('Owner and technical director, electrically authorised marine engineer',
         'ELOHVAC ApS · Copenhagen · May 2023 to November 2026 (company closed)',
         [('', 'Preventive maintenance and fault-finding on electrical, ventilation and HVAC systems, from '
               'emergency call-outs to handed-over installations.'),
          ('', 'KPI dashboards for service and maintenance work, built with AI tools. Productivity gain above 40 % '
               'on quotation, schedules, KS checklists and KPI reporting.'),
          ('', 'LOTO, risk assessment and APV at each site start. Zero critical deviations in service agreements.')]),
        ('Senior commissioning engineer and project manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg and Bagsværd · November 2022 to July 2024',
         [('', '37 concurrent projects with progress, budget and risk, across engineering, procurement and site.'),
          ('', 'Cross-functional leadership of 25 specialists. FAT/SAT and IQ/OQ/PQ under GMP, FDA and EMA.'),
          ('', 'Electrical systems: panels and control, UPS, emergency and panic lighting, access control and PDS. '
               '40 % lower energy costs through a PDCA programme. SAP ERP for finance and asset cost.')]),
        ('Project and workshop manager',
         'Ventek-Air · Copenhagen · January 2022 to November 2022',
         [('', '11 concurrent installation projects from specification to formal handover, managing a 14-person team.'),
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
    m.edu('Refrigeration and air conditioning (AMU)', 'Mercantec · 2021')
    m.para('Lean and Six Sigma methods applied in practice, not certified: DMAIC, 5S, PDCA, VSM, A3, Kaizen, '
           'SMED, TPM, 5 Whys, Ishikawa and FMEA.', after=48)

    m.section('SKILLS')
    m.models_table('Tools and systems', ('Area', 'Tools'), [
        ('Reliability and failure analysis', 'FMEA, Ishikawa, 5 Whys, A3, PDCA, root-cause analysis'),
        ('Systems in use', 'CMMS, asset data, maintenance plans, work orders, SAP ERP'),
        ('KPIs', 'MTBF, MTTR, OEE, spare parts availability, Power BI, Excel'),
        ('GMP and qualification', 'GMP, FDA, EMA, FAT, SAT, IQ/OQ/PQ, CIP/SIP'),
        ('Safety', 'LOTO, APV, risk assessment, near-miss reporting'),
        ('Data and AI', 'Python, Claude API, Claude Code'),
    ], widths=(3400, 6946), compact=True)
    m.para('Danish native, spoken and written. English professional, working language in international projects '
           'since 2017. Persian native. German not held. Driving licence B, manual gearbox.', after=40)

    # ------------------------------------------------------------ requirements matrix, page 4
    m.page_break()
    m.section('REQUIREMENTS MATRIX')
    rows = [
        ('Hold a relevant technical or engineering degree and bring several years of relevant experience within maintenance and/or reliability',
         'Maskinmester (marine engineering & technology management), 2017 to 2022. Maintenance and operations manager at Biofos from August 2017 to January 2022, which is 4 years and 5 months of maintenance work. Electrical and mechanical maintenance at ELOHVAC from 2023 to 2026.'),
        ('Thorough understand of GMP requirements for maintaining equipment, utilities and facilities',
         'GMP, FDA and EMA requirements at Novo Nordisk, 2022 to 2024, with FAT, SAT and IQ/OQ/PQ on tanks, CIP/SIP systems, process piping, instrumentation and UPS. As a site owner under GMP, I have not run maintenance; the qualification work is the basis.'),
        ('Have CMMS/EAM experience and understand how asset data, maintenance plans, work-order history, supports asset performance and reliability',
         'CMMS experience from maintenance work: asset data, maintenance plans and work-order history used to support asset performance. Asset management and maintenance strategy and systems are documented. Leading a CMMS implementation is not in my record.'),
        ('Apply and anchor risk-based maintenance methods, such as RCM and FMECA, and work with the sites to develop initiatives that work in real life and are supported by the CMMS',
         'FMEA and A3 in fault analysis at Novo Nordisk and Biofos, and root-cause work with 5 Whys and Ishikawa. RCM and FMECA as formal methods are not documented in my record; I would start from FMEA workshops with the site team.'),
        ('Can build maintenance capabilities and foster cooperation across sites by sharing what works, working with local teams and influencing change without direct authority',
         'Matrix leadership of two parallel organisations, ELOHVAC and Data Power, with one shared plan and written priorities. Daily planning of a 14-person team at Ventek-Air and of 5 electricians and 3 apprentices.'),
        ('Are able to take initiative and work independently in a global organization, building relations across sites and organizations',
         'Acute fault-finding at Biofos and emergency call-outs at ELOHVAC from the call to handover. Coordination across engineering, procurement and site with 37 concurrent projects at Novo Nordisk, and 11 projects at Ventek-Air.'),
        ('Communicate clearly and confidently in English, both written and spoken',
         'English professional, written and spoken. Working language in international projects since 2017, and used in the Novo Nordisk GMP documentation and FAT/SAT work.'),
        ('German skills for Bern site and Danish skills for Denmark site are a plus',
         'Danish native, for the Denmark site. German is not held, so the Bern site would require language work on my side.'),
        ('Own and develop the Global Maintenance Policy, processes and procedures, aligned with GMP, regulatory expectations and good engineering practices',
         'Standard work and procedures in practice: 5S, Standard Work and PDCA at Biofos, and LOTO, APV and risk assessment procedures at each site start. A multi-site policy at global level is not in my record.'),
        ('Work closely with Maintenance, Engineering, Operations, Quality and Metrology functions across our sites to ensure global processes are both compliant, operationally effective and continuously improved',
         'Coordination across engineering, procurement, site and quality at Novo Nordisk, with zero critical deviations at handover. Metrology and calibration programmes are not documented in my record.'),
        ('Build consistent use and interpretation of maintenance and reliability KPIs, including MTBF/MTTR and OEE, and turn data into actionable improvements',
         'MTBF, MTTR, OEE and spare parts availability used in maintenance work, with KPI dashboards in Python and Power BI. ELOHVAC KPI reporting turned into actions, with a productivity gain above 40 % on AI-supported work.'),
        ('Develop a global reliability framework and methods for asset criticality, maintenance strategies, RCM, RCA, FMEA/FMECA, condition-based and predictive maintenance',
         'RCA with 5 Whys and Ishikawa, FMEA, and SCADA monitoring at Biofos. Asset criticality, RCM and FMECA are not documented as a ranking method. A predictive maintenance programme is not in my record.'),
        ('Through training, procedures and cooperation, aid sites in progressing from predominantly reactive and time-based maintenance toward risk-based, condition-based, predictive and data-driven approaches',
         'Preventive maintenance alongside acute fault-finding at Biofos in 24/7 operation, 2017 to 2022. Training of 5 electricians and 3 apprentices at ELOHVAC and Data Power. Data-driven KPI work in Python and Power BI.'),
        ('Establish a cross-site Reliability Network with designated site resources to build capabilities and share knowledge across sites',
         'Coordination across sites in the Novo Nordisk project portfolio, with 25 specialists in cross-functional leadership. A standing cross-site network with named site contacts is not in my record.'),
        ('Provide reliability, maintainability and lifecycle input to equipment, utility and facility projects from early design, incorporating lessons from existing assets',
         'Project delivery from specification to formal handover at Novo Nordisk (37 CAPEX projects) and Ventek-Air (11 projects), with FAT/SAT and handover packs. Early-design reliability review is not in my record.'),
        ('Represent Maintenance and Reliability during CMMS implementation and ongoing development, improving system use to support maintenance performance',
         'CMMS use in maintenance work, SAP ERP for asset cost at Novo Nordisk, and asset management and maintenance systems. A CMMS implementation role is not in my record.'),
        ('Cross-site collaboration, with approximately 30 travel days per year',
         'Projects across several sites: Novo Nordisk in Kalundborg and Bagsværd, and Biofos and Ventek-Air in Copenhagen. Travel days per year are not stated in my record and need to be discussed.'),
        ('Based in Kvistgaard, Denmark, or Bern, Switzerland, with considerable onsite presence',
         'Based in Denmark, in Måløv, so Kvistgaard is the Denmark option. Bern would require German, which I do not hold, and that would need to be part of the discussion.'),
    ]
    m.models_table('Opslagets krav og min dokumentation', ('Krav', 'Dokumentation og status'),
                   rows, widths=(3600, 6746), compact=True)

    m.save(path, title='Global Reliability & Maintenance Specialist - Bavarian Nordic',
           subject='Application Global Reliability & Maintenance Specialist, JR101652')
    print(path)


if __name__ == '__main__':
    os.makedirs(OUT_DIR, exist_ok=True)
    build(OUT)
