# -*- coding: utf-8 -*-
"""Alstom: Project Quality and Safety Manager (Req ID 535229), Kobenhavn.

English posting -> English document (en-GB). Form (master/FORMKATALOG.md):
opening **AO** (The inspector's folder: what the customer's inspector opens the
folder to, and when that content was made), structure **Who signs for what**
(the outstanding "fordeling af ansvar": five places where quality
responsibility lands, each with what the other party owns and what I own),
register **The Car History Book** (defect, rework, sign-off, compliance,
traceability, closure). Style variation 3/3 vs #413.

Kulturfil: jd/Alstom_ProjectQualityAndSafetyManager_kultur.txt (29 phrases,
26 from the posting and 3 verified on alstom.com: "an agile, inclusive and
responsible culture", "Mobility by nature", "We take our rules for compliance
and safety extremely seriously").

Honest boundaries (never claimed): railway/depot experience, ISO9001 and
ISO22163 knowledge, Special Processes qualification, formal quality auditing,
German, Master's level degree, car history book experience. Banned words
(incl. "passionate" from the posting's own headline) are never used, and the
human voice rules from master/README.md apply: no slogan openers, no parallel
chains, no aphorism chains, uneven rhythm.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'

MOTTO = 'The record decides'
BANNER_LETTER = 'DSB/IC5 depot, Copenhagen · Project Quality and Safety Manager'
BANNER_RESUME = 'Quality, safety and handover in the depot · IC5 for DSB'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv, Denmark · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('25 November 2026')
    m.meta('Alstom · Copenhagen · Req ID 535229')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Project Quality and Safety Manager', bold=True, color='1A1A1A')
    m.para('Dear Quality and Safety Team at Alstom,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ---------------------------------------------------------------- page 1
    lp('The folder on the table at a customer inspection decides more than the meeting does. '
       "When DSB's people come to the Copenhagen depot to look at an IC5 set, they open the "
       'records: what was inspected against the Quality Control Plan, what was found, what went '
       'back for rework and got checked again, and who signed it off. That is Quality '
       "activities in the DSB/IC5 project depot in practice, and it's why I'm writing. Alstom "
       'puts it plainly: we build what millions depend on daily, rail transportation systems '
       "that can't afford to fail. The industry's most diverse portfolio of high-speed trains, "
       'metros, trams, maintenance services and integrated systems all leans on the same thing, '
       'that the record holds.', after=44)

    lp('Start with the team. Managing the Site Industrial Quality team is people work before '
       'it is process work: the daily inspections, the check after rework, quality related '
       'fleet checks when the sets need them, and every result recorded in the industrial '
       'digital tools as required. Around that team sits the rest of the business; the posting '
       'has the onsite quality and safety teams, and project customer satisfaction teams in the '
       'same daily circle, and PI site quality process implementation as the frame all of it '
       'works inside. I have led teams like this more than once: five electricians and three '
       'apprentices at ELOHVAC, a fourteen-person workshop at Ventek-Air, twenty-five '
       'specialists at Novo Nordisk. The posting wants someone who thrives on ensuring '
       'excellence in every phase of project delivery. In my experience it means being on '
       'the floor and knowing what the last shift did.',
       after=44)

    lp("The other half of the job is the stuff that arrives. Deliveries from the Origin site "
       "have to be at the right quality level before the depot spends days on them, and Special "
       "Processes are where the Engineering Team's evidence matters more than anyone's eyes. I "
       'know that pattern from commissioning at Novo Nordisk: FAT/SAT and IQ/OQ/PQ protocols '
       'were exactly this, agreed inspection points and written proof, and thirty-seven '
       'projects went out the door with zero critical findings. Reporting of defects and '
       'product compliance, the check after rework especially for Special Processes, is the '
       'same discipline pointed the other way. And the Zero Defect Program is improvement work '
       'with a name on it: at Novo Nordisk a PDCA programme cut energy costs by 40%, and the '
       'defects that repeat got their own line in the report.', after=44)

    lp("The customer side is where it gets visible. Leading customer inspections means being "
       "the one who walks the set with DSB's inspector and can answer for the CHB, the car "
       'history book, without hunting for papers; the inspection and delivery of new trains to '
       'the customer is the same walk a few steps earlier. The posting measures success in '
       'three lines that fit how I have worked: project quality and safety milestones within '
       'agreed timelines, Effective collaboration and leadership across multidisciplinary '
       'teams, and Reduction in non-conformities and measurable improvement in process '
       'efficiency. Those three are what a monthly report should be able to show.', after=44)

    lp('The posting is headed More Than a Job: A Mission, and the rest of it '
       'holds up: sharp, committed teams solving complex challenges that '
       'shape the future of mobility, cutting-edge digital quality systems and global safety '
       'standards, and the promise of continuous learning and international exposure while you '
       'enhance sustainable mobility from our Copenhagen hub. Alstom\'s own pages add what I '
       'would actually be joining: an agile, inclusive and responsible culture, Mobility by '
       'nature, and one plain line I liked: "We take our rules for compliance and safety '
       'extremely seriously." A company that celebrates diversity across the 63 countries it '
       'operates in, and creates an inclusive workplace for everyone while running on the '
       'seamless integration of business and technology, is a straightforward place to do '
       'quality work. When the system runs, the train moves, and '
       'the city connects; the posting says that feeling stays with you. I have had a version '
       'of it after a clean handover.', after=44)

    lp("What I'd bring is narrower and deeper than the posting's ideal profile. Railway is new "
       'to me; quality and safety work in regulated, critical operations is not: GMP/FDA/EMA '
       'handovers at Novo Nordisk, quality problem-solving with A3, 5 Whys, Ishikawa and FMEA '
       'in daily use, and the safety toolbox of a 24/7 utility. Two honest gaps to say out '
       'loud: ISO9001 and ISO22163 are not on my record yet, and I do not speak German. '
       'English and Danish I do, Danish as my first language. My degree is B.Tech at EQF6 '
       "level, not a Master's, with electrical engineering beside it and a Danish authorisation "
       'LV/MV/HV on top. If that mix fits the depot, I would like to talk about what the first '
       'customer inspection has to prove. I live in Måløv, a short ride from the Copenhagen '
       'hub, and can start at short notice. You can reach me on +45 93 99 95 14 or '
       'ajlooshahram@gmail.com.', after=16)

    m.meta('Kind regards', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFILE')
    m.para('Project Quality and Safety Manager. My background is commissioning, handover and '
           'quality work in regulated operations: 37 projects at Novo Nordisk under GMP/FDA/EMA '
           'with zero critical findings, quality assurance in every contract at ELOHVAC, and '
           'safety work in 24/7 operations at Biofos. I record inspection work in the tools the '
           'site uses: SAP ERP, CMMS, Power BI, Excel and Python.', after=32)

    m.section('EXPERIENCE')
    jobs = [
        ('CTO for the AI department and authorised electrical engineer (electrical and ventilation)',
         'Data Power Consultant ApS · Copenhagen · 2024 – present',
         'AI department 4-10 people · electrical and ventilation · full P&L · 5 electricians + 3 apprentices',
         [('', 'I set the direction for a 4-10 person AI department: the offering, the customers, '
               'and how the solutions were built and documented. Investment cases for new '
               'services and monthly KPI follow-up.'),
          ('', 'Python and Claude API for dashboards, checklists and reports. ELOHVAC and Data '
               'Power ran against one shared plan. A person reviewed everything before it went '
               'to a customer.')]),
        ('Owner / technical director / authorised electrical engineer',
         'ELOHVAC ApS · Copenhagen · May 2023 – November 2026 (company closed)',
         'Commercial customers · electrical, ventilation, climate · contracting · full P&L',
         [('', 'Tenders, pricing, subcontractor and supplier agreements, and the budget '
               'follow-up each month. Quality assurance and handover documentation in every '
               'contract.'),
          ('', 'Led 5 electricians and 3 apprentices. Daily planning, 1:1s, training, and '
               'safety follow-up: LOTO, APV, risk assessment at site start-up. The service '
               'agreements closed with zero critical deviations.')]),
        ('Senior commissioning engineer / project manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · November 2022 – July 2024',
         '37 CAPEX projects, DKK 2–10 mio. · 25 specialists · GMP/FDA/EMA',
         [('', 'Commissioning and project management on 37 CAPEX projects, DKK 2–10 mio. each. '
               'FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA, with zero critical findings at handover.'),
          ('', 'Monthly report to leadership and client management: progress, cost, risks and '
               'resources. 25 specialists across engineering, procurement and operations. SAP '
               'ERP for cost data.')]),
        ('Project and workshop manager',
         'Ventek-Air · Copenhagen · January 2022 – November 2022',
         '11 concurrent projects · 14-person team · DKK 2–10 mio.',
         [('', 'Ran 11 concurrent projects and a 14-person team. Daily boards for capacity and '
               'progress. Safety documentation and handover packages in every project.')]),
        ('Maintenance and operations manager / workshop technician',
         'Biofos (Lynetten) · Copenhagen · August 2017 – January 2022',
         '24/7 operations · SCADA, PLC, HV switchgear · shift work',
         [('', 'Maintenance and operations on pumps, HVAC, HV switchgear and SCADA, around the '
               'clock. Planned maintenance and fault finding, and 5S and Standard Work in the '
               'workshop. Shift work with LOTO, APV and near-miss reporting.')]),
        ('Electromechanical technician / production team leader',
         'ARJ Engineering · Tehran · December 2003 – March 2010',
         '12 mechanics and technicians · machine shop · product line',
         [('', 'Led 12 mechanics and technicians in a machine shop: shift planning, materials, '
               'goals. Fault diagnosis on industrial equipment, root-cause analysis and '
               'corrective actions.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('EDUCATION AND CERTIFICATIONS')
    m.edu('B.Tech (EQF6), Technology Management and Mechanical Engineering',
          'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7.6/12')
    m.edu('Authorised electrical engineer (LV/MV/HV)',
          'Danish Safety Technology Authority · May 2023')
    m.edu('Electrical and mechanical design, electrical engineering (EQF6)',
          'Tehran Technical University · 2000–2003')
    m.edu('PRINCE2, certified project manager', 'AXELOS / PeopleCert')
    m.edu('Refrigeration and air conditioning (AMU)',
          'Mercantec · 2021 · STCW 2021–2023, Danish Maritime Authority')
    m.para('Quality and problem-solving tools in practice, not certification: A3, 5 Whys, '
           'Ishikawa, FMEA, PDCA, DMAIC, 5S, Standard Work, SMED and TPM, used in documented '
           'work on maintenance, quality and planning.', after=48)

    m.section('LANGUAGES, TOOLS AND PRACTICALITIES')
    m.para('Danish (first language) · English (professional working proficiency) · Persian '
           '(native) · German (not spoken). Tools: SAP ERP, CMMS, Power BI and KPI dashboards, '
           'Excel and Python, Claude API and Claude Code for checklists and reports, PRINCE2 '
           'for project structure, LOTO, APV and risk assessment as working habits. Based in '
           'Måløv near Copenhagen; available at short notice.', after=48)

    m.section('QUALITY AND SAFETY WORK')
    for label, body in [
        ('Inspections',
         'Inspection work against written plans: IQ/OQ/PQ protocols, control-plan checklists, '
         'and the check after rework with its own sign-off. Customer inspections and handover '
         'walks included.'),
        ('Safety',
         'LOTO, APV, risk assessment and near-miss reporting, from 24/7 operations and from '
         'site work. Toolbox meetings and follow-up with the team.'),
        ('Digital tools',
         'SAP ERP, CMMS, Power BI, Excel, Python and Claude tools. Inspection results go into '
         'the systems the site already uses.'),
        ('Root cause',
         'A3, 5 Whys, Ishikawa and FMEA when something fails. The report should carry the root '
         'cause and the corrective action, not just the part that was replaced.'),
        ('Handover',
         'IQ/OQ/PQ protocols and handover packages across 37 projects. The check after rework '
         'gets its own sign-off.'),
    ]:
        m.bullet(label, body, after=10)

    m.section('THE FIRST 90 DAYS')
    m.para('My plan for the first 90 days:', after=12)
    for b in (
        'Days 1-30: walk the depot. Learn the PI site quality process as it actually runs, the '
        'Quality Control Plan for the sets in work, and who signs for what today. Talk to the '
        'Site Industrial Quality team, the onsite quality and safety teams, and the people who '
        'own the customer relationship. No new process before I can explain the old one.',
        'Days 31-60: first quality related investigations alongside the team, and the first '
        'pass at the Zero Defect Program: what defects repeat, what the record misses, what the '
        'industrial digital tools do not capture. Agree with the team what the check after '
        'rework looks like in practice.',
        'Days 61-90: run one customer inspection end to end with the team, and leave three '
        'things behind: a cleaner car history book rhythm, a defect report the Engineering '
        'Team can act on, and quality and safety milestones we can actually measure.'):
        m.bullet('', b, after=10)

    # ---------------------------------------------------------------- page 4
    m.page_break()
    m.models_table('Alstom · Req ID 535229 · Project Quality and Safety Manager', ('Requirement', 'Evidence'), [
        ('cover Quality activities in the DSB/IC5 project depot',
         'Commissioning and handover quality for 37 projects at Novo Nordisk (FAT/SAT, '
         'IQ/OQ/PQ, zero critical findings) and quality assurance in every ELOHVAC contract. '
         'The depot setting is new; the quality work is not.'),
        ('Work closely with teams across the business such as the onsite quality and safety '
         'teams and project customer satisfaction teams',
         'Cross-functional work at Novo Nordisk around 37 projects, monthly reporting to '
         'leadership and client management; two parallel organisations on one plan since 2023.'),
        ('manage the Site Industrial Quality team',
         'Leadership with numbers: 5 electricians and 3 apprentices at ELOHVAC (planning, '
         '1:1s, training), a 14-person workshop at Ventek-Air, 25 specialists at Novo Nordisk, '
         'and 12 mechanics and technicians at ARJ.'),
        ('ensure PI site quality process implementation',
         'Standardised work processes across 11 concurrent projects at Ventek-Air that lifted '
         'delivery measurably, quality checklists and quality-assurance routines at ELOHVAC, '
         'and documented acceptance standards for AI output at Data Power.'),
        ('support the inspection and delivery of new trains to the customer',
         'Commissioning at Novo Nordisk (SAT acceptance, IQ/OQ/PQ) and 11 projects from '
         'specification to formal handover at Ventek-Air. Trains are new; the '
         'inspection-and-delivery walk is not.'),
        ('support with quality related fleet checks',
         'Inspection routines from 24/7 operations at Biofos (planned maintenance checks, '
         'fault finding, SCADA data) and scheduled quality checks in ELOHVAC service '
         'agreements. Fleet terminology is new; check discipline with a record is not.'),
        ('support Improvement of Zero Defect Program',
         'Handovers recorded zero critical findings across 37 GMP projects, zero critical '
         'deviations in ELOHVAC service agreements, and a PDCA programme that cut energy '
         'costs by 40% at Novo Nordisk.'),
        ('reporting of defects and ensure product compliance (check after rework), especially '
         'for Special Processes',
         'Root-cause analysis and corrective actions (ARJ), rework verification at Biofos and '
         'ELOHVAC, and GMP handover checks where a defect found late becomes a deviation. '
         "Special Processes are Alstom's world; the pattern is familiar."),
        ('perform inspections and ensure product compliance (check after rework) according to '
         'Quality Control Plan',
         'IQ/OQ/PQ protocols under GMP/FDA/EMA (37 projects, zero critical findings) and LOTO '
         'and risk assessment routines at Biofos and ELOHVAC. The Quality Control Plan wording '
         'is new; working to a plan someone else can audit is not.'),
        ('lead customer inspections',
         'SAT and handover walks at Novo Nordisk with client management present, formal '
         'handover of 11 projects at Ventek-Air, and handover inspections with 1- and 5-year '
         'follow-up reviews at ELOHVAC. Leading the walk is how those were run.'),
        ('maintain the CHB (car history book)',
         'IQ/OQ/PQ protocols and handover packages across 37 projects at Novo Nordisk, '
         'quality assurance and documentation routines in every ELOHVAC contract, and release '
         "records at Data Power. The CHB itself is Alstom's to teach."),
        ('take part in quality related investigations',
         'Investigations run on named tools: A3, 5 Whys and Ishikawa at Novo Nordisk problem '
         'level, FMEA in risk work, root-cause '
         'analysis and corrective actions at ARJ, and near-miss reporting as a fixed practice '
         'at Biofos. Written so the next reader can follow.'),
        ('record inspection results in the industrial digital tools as required',
         'SAP ERP for cost and asset data at Novo Nordisk, CMMS at Biofos, Power BI and KPI '
         'dashboards, and Python and Claude API for digital checklists and reports since 2024 '
         '(over 40% faster documentation).'),
        ("Master's degree in Engineering (electromechanical, electrical, electronics) or equivalent",
         'B.Tech (EQF6) Technology Management and Mechanical Engineering (2017-2022), '
         'electrical engineering (EQF6) at Tehran Technical University (2000-2003), and Danish '
         'LV/MV/HV authorisation (2023).'),
        ('Expertise in managing Quality and problem-solving tools',
         'The tools are named and used in practice: A3, 5 Whys, Ishikawa, FMEA, PDCA, DMAIC, '
         '5S, Standard Work, SMED and TPM in practice '
         'across Novo Nordisk, Ventek-Air, Biofos and ELOHVAC since 2017, not as '
         'certification.'),
        ('Knowledge of Quality standards (ISO9001, ISO22163)',
         'Honest gap: ISO9001 and ISO22163 are not on my record. Documented is GMP/FDA/EMA '
         'quality systems (IQ/OQ/PQ, deviations, zero critical findings across 37 projects) '
         'and quality assurance in contracts.'),
        ('Fluency in English and Danish; German would be an asset',
         'Danish first language, English working language (documentation, tenders, supplier '
         'correspondence), Persian native; education in Denmark since 2012. German is not '
         'spoken, and I would not pretend otherwise.'),
        ('Experience in Quality auditing and Process management would be an asset',
         'Process management documented (standardised work, written procedures, handover '
         'packages); formal quality auditing is not on my record. Handovers under GMP meant '
         'the audited side too: 37 projects, zero critical findings.'),
        ('Achievement of project quality and safety milestones within agreed timelines',
         '37 CAPEX projects of DKK 2-10 mio. delivered to handover on plan, 11 concurrent '
         'projects at Ventek-Air, and zero critical findings at every handover. Timelines held '
         'with daily boards and monthly reporting.'),
        ('Effective collaboration and leadership across multidisciplinary teams',
         '25 specialists across engineering, procurement and operations at Novo Nordisk, a '
         '14-person team at Ventek-Air, 5 electricians and 3 apprentices at ELOHVAC, and 12 '
         'technicians at ARJ.'),
        ('Reduction in non-conformities and measurable improvement in process efficiency',
         'Non-conformities tracked in the monthly report: zero critical findings at handover '
         '(37 projects), a PDCA programme cutting energy costs by 40%, and AI-assisted '
         'documentation over 40% faster since 2024.'),
    ], widths=(3400, 6946), compact=True)

    m.para('**I can be reached on +45 93 99 95 14 or ajlooshahram@gmail.com,** and am ready to '
           'talk at short notice.', after=20)

    m.save(path, title='Project Quality and Safety Manager - Alstom')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Alstom_ProjectQualityAndSafetyManager_v2.docx')
    build(out)
    print(out)
