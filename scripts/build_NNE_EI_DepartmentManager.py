# -*- coding: utf-8 -*-
"""NNE (Novo Nordisk Engineering) — Department Manager, Electrical & Instrumentation (E&I), Kalundborg.

English deliverable (JD is English): task-first application page + CV in one document.
The posting says no cover letter is required but asks for a few sentences on motivation in the CV,
so page 1 carries the motivation and the CV follows it.
Culture and role intel: master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md (NNE section).
Policy: master/README.md — extreme confidence, no caveats.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Electrical & Instrumentation · People leadership and project execution'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('5 November 2026')
    m.meta('NNE A/S · Kalundborg · Department Manager, Electrical & Instrumentation (req5128)')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Department Manager — Electrical & Instrumentation', bold=True, color='1A1A1A')
    m.para('Dear Jannick Kartman', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('Electrical and instrumentation is where the process becomes controllable. A cable schedule, an instrument '
           'index, a loop drawing and a control philosophy decide whether a batch can be released — and in an API '
           'plant that is not a documentation detail, it is the product. An E&I department exists to make that true '
           'project after project, with people who are technically excellent and who stay. That is the department I '
           'want to lead at NNE.', after=80)

    m.para('**I would run the department on four fixed things.** First, one capacity board: every engineer and every '
           'consultant visible against the projects they serve, with a named owner per discipline scope and a weekly '
           'look at what is committed, what is coming, and where the next bottleneck is. Second, technical excellence '
           'you can audit: discipline standards for instrument index, loop and cable documentation, ATEX and panel '
           'design, plus design reviews at fixed milestones and FAT/SAT and IQ/OQ/PQ checklists that the project can '
           'reuse instead of writing from scratch. Third, competency development that is planned rather than '
           'accidental — a matrix per engineer across instrument types, control systems, electrical design and '
           'qualification work, with the senior specialists mentoring and the next hire decided before the gap '
           'appears. Fourth, one team across Denmark and Bangalore: overlapping hours, one source of truth, written '
           'handovers, and scope agreed before work travels.', after=80)

    m.para('I have led this discipline inside your customer\'s organisation. From 2022 to 2024 I was senior '
           'commissioning engineer and project manager for electrical systems at Novo Nordisk, with 37 parallel '
           'capital projects, 25 specialists and DKK 2–10m per project in Kalundborg and Bagsværd: acceptance '
           'criteria, FAT and SAT, IQ/OQ/PQ, deviation handling and audited handover with zero critical findings — '
           'under GMP, FDA and EMA. I have sat in the design reviews, walked the panels, signed the loop checks and '
           'defended the documentation in front of an inspector. That is exactly the work an E&I department at NNE '
           'delivers to Novo Nordisk every day, and I know both sides of the table.', after=80)

    m.para('My leadership comes from twenty years of building teams that deliver. I am the owner and technical '
           'director of ELOHVAC with five electricians and three apprentices and full P&L — recruitment, 1:1s, '
           'competence matrix, apprentices and customers in the same week. Before that I led 14 employees and 11 '
           'parallel construction projects at Ventek-Air, and 12 mechanics and technicians at ARJ. I have managed '
           'resource allocation across projects where two sites both needed the same specialist on the same Tuesday, '
           'and I have learned that the answer is a plan made in advance, not a phone call made in panic.', after=80)

    m.para('The electrical discipline is my profession, not an adjacent interest. I hold a B.Tech in Technology '
           'Management and Mechanical Engineering with electrical engineering studies from Tehran Technical '
           'University, and I am an authorised marine engineer with Danish electrical authorisation at LV, MV and HV '
           '— so I can challenge a protection philosophy, read the single-line diagram and the P&ID, and hold a '
           'technical conversation with the instrument engineer and the electrician in the same hour. Danish is my '
           'native language, English is my professional one; I have worked in English-speaking project organisations '
           'for years and I am used to the Indian collaboration model from the Novo Nordisk projects.', after=80)

    m.para('**On dividing the week between projects and the department.** The trap in a role like this is becoming '
           'the best project engineer in the department at the expense of the department. My rule is simple: the '
           'calendar is the resource plan. Two fixed days for department work — capacity, competence, reviews and '
           'the conversations that cannot be moved — and project time blocked and visible, so nobody has to guess '
           'where I am. And every technical decision I make in a project becomes a standard or a template '
           'afterwards, so the next project does not need me in the same place.', after=80)

    m.para('NNE\'s values describe the manager this role needs: **take initiative and get things done** — a department '
           'that answers in hours, not weeks; **be passionate about pharma engineering expertise** — the technical '
           'standard is the product; **innovate and create efficient solutions** — standardise what repeats, so '
           'engineers spend their hours on what is actually new; **team up and leverage our global knowledge** — '
           'Bangalore is not a cost centre, it is half the department; and **exceed customer expectations** — Novo '
           'Nordisk is the customer, and the patient is the reason the cable is pulled correctly. I also value what '
           'you say about people: a people business, flat hierarchy, and a start that is taken seriously. I lead the '
           'same way — visible, on site, and with the door open.', after=80)

    m.para('Practically: I live in Måløv, about an hour from Kalundborg, and I will be on site five days a week — that '
           'is where an engineering department is led. I can start by agreement, and I can be reached '
           'on +45 93 99 95 14. I would welcome a conversation about how the E&I department is organised today, where '
           'the capacity pressure is greatest, and what the next two years of Kalundborg projects will demand of the '
           'discipline.', after=70)
    m.meta('Kind regards', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('Department manager and E&I project engineer with 20+ years from electrical and instrumentation work, '
           'regulated pharma production and technical operations — authorised marine engineer with Danish electrical '
           'authorisation (LV/MV/HV) and a B.Tech in Technology Management & Mechanical Engineering. Twenty years of '
           'people leadership: 37 capital projects with 25 specialists and zero critical findings at Novo Nordisk, 14 '
           'employees at Ventek-Air, five electricians and three apprentices with full P&L at ELOHVAC. Runs '
           'departments on capacity, competence and documentation — and delivers projects while doing it.', after=80)

    m.section('LEADERSHIP, E&I DELIVERY AND RESULTS')
    for label, body in [
        ('Department and resource management',
         'Capacity and competence ownership: resource allocation across 37 parallel projects, 14 employees in a '
         'project organisation, five electricians with full P&L; recruitment, 1:1s and succession planned before the '
         'gap appears.'),
        ('E&I project execution',
         'Senior commissioning engineer and project manager for electrical systems at Novo Nordisk: instrument and '
         'IO documentation, panel and cable schedules, loop checks, FAT/SAT, IQ/OQ/PQ and audited handover — DKK '
         '2–10m per project, zero critical findings, GMP/FDA/EMA.'),
        ('Technical standards and quality',
         'Discipline standards and design reviews at fixed milestones; documented acceptance criteria, deviation '
         'handling and traceability from requirement to test — written so a colleague who was not in the room can '
         'approve it.'),
        ('GMP, GEP and audit readiness',
         'Two years inside a GMP/FDA/EMA organisation with change control, CAPA and inspections as daily conditions; '
         'good engineering practice applied so the documentation is produced with the work, not after it.'),
        ('Digital tools that free up hours',
         'Python, Claude API, SAP and Excel in daily use: traceability matrices, IO and deviation logs, alarm and '
         'capacity statistics, dashboards and investment cases with NPV and IRR — over 40 % of the administrative '
         'work removed from quoting and follow-up.')]:
        m.bullet(label, body, after=25)

    m.models_table('TOOLS AND METHODS', ('Task', 'Tool and documented use'), [
        ('Electrical and instrumentation',
         'Single-line diagrams, panel and cable design, instrument index and loop documentation, IO lists, ATEX '
         'considerations and electrical authorisation LV/MV/HV.'),
        ('Control and automation',
         'PLC and SCADA-based systems, BMS/FMS, sensor and control loops, alarm limits and escalation; interface '
         'protocols such as Modbus and BACnet.'),
        ('Qualification and validation',
         'URS and design review, risk assessment and FMEA, FAT/SAT, IQ/OQ/PQ, traceability matrix, deviation and '
         'change control — with acceptance documented at every gate.'),
        ('Project and portfolio',
         'Stage plans, milestone plans and shutdown schedules; resource and capacity planning across a portfolio of '
         'parallel projects, with named owners and a weekly committed-versus-coming review.'),
        ('People and organisation',
         '1:1s and performance dialogues, competence matrix per engineer, onboarding and mentoring by senior '
         'specialists, recruitment and retention in a competitive engineering market.'),
        ('Safety and compliance',
         'LOTO, workplace assessment, permits and near-miss reporting; GMP/GEP and authority requirements built into '
         'plan and contract.')])

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director',
         'ELOHVAC ApS · Copenhagen, Denmark · May 2023–present',
         '5 electricians and 3 apprentices · full P&L · commercial and industrial customers',
         [('People and profit', 'Recruitment, 1:1s, competence matrix and apprentice training alongside budget, '
                                'quoting, margin and purchasing; customers informed the same day something changes.'),
          ('Technical delivery and digital', 'Electrical panels, motor controls, variable speed drives and control '
                                            'systems, tested and documented; Python and Claude API for quotations, '
                                            'scheduling and KPI dashboards — over 40 % productivity gain.')]),
        ('Senior Commissioning Engineer / Project Manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd, Denmark · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · DKK 2–10m each · GMP/FDA/EMA',
         [('Commissioning and qualification', 'Acceptance criteria, FAT/SAT and IQ/OQ/PQ with traceable '
                                              'documentation and deviation handling; zero critical findings at '
                                              'handover.'),
          ('Coordination and reporting', 'Progress, cost, risk and resources across engineering, procurement and '
                                         'operations; monthly reporting to management and to the client.')]),
        ('Project and Workshop Manager',
         'Ventek-Air · Copenhagen, Denmark · Jan 2022–Nov 2022',
         '14 employees · 11 parallel construction projects · DKK 2–10m each',
         [('Team and delivery', 'Tenders, calculations, subcontractors and handover packages in ventilation and '
                                'technical installations; daily board meetings and bottleneck analysis.')]),
        ('Maintenance and Operations Manager / Workshop Technician',
         'Biofos, Lynetten · Copenhagen, Denmark · Aug 2017–Jan 2022',
         '24/7 plant · pumps, HVAC, high-voltage switchgear, SCADA · shift teams and technical staff',
         [('Operations and maintenance', 'Preventive maintenance from SCADA condition data; alarm handling, fault '
                                         'diagnosis and corrective work prioritised by consequence in shift '
                                         'operations.'),
          ('Safety and standards', 'LOTO, workplace assessment, risk assessment and near-miss reporting; standard '
                                   'work, 5S and PDCA on the workshop floor.'),
          ('Shift teams', 'Planned shifts, training and cover for a 24/7 operation — twelve technicians across '
                          'rotations, with competence and availability balanced every week.')]),
        ('Electromechanical Technician / Production Team Leader',
         'ARJ Engineering · Tehran, Iran · Dec 2003–Mar 2010',
         '12 mechanics and technicians · machine workshop · industrial equipment',
         [('Team and equipment', 'Shift planning, material control and target follow-up; fault diagnosis, '
                                 'root-cause analysis and corrective actions on production equipment.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        m.doc.paragraphs[-1].runs[0].text = 'Scope: '
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('EDUCATION AND AUTHORISATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering',
          'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · EQF 6 · GPA 7.6/12')
    m.edu('Authorised marine and electrical engineer (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('Electrical and mechanical design, electrical engineering',
          'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Refrigeration and air conditioning · STCW safety and engine-room watch',
          'Mercantec 2021 · Danish Maritime Authority 2021–2023')

    m.section('LANGUAGES, PRACTICAL AND REFERENCES')
    m.para('Danish: native · English: professional, written and spoken · Persian: native · Driving licence B · Lives in '
           'Måløv, about an hour from Kalundborg, and on site five days a week · Available by agreement · SAP and '
           'Excel in daily use · References from Novo Nordisk and Biofos, and from customers and partners in my own '
           'company, on request.', after=70)

    m.models_table('WHAT THE ROLE ASKS FOR — MY EVIDENCE', ('Requirement', 'Evidence'), [
        ('At least 5 years of leadership experience',
         'Twenty years: owner with full P&L and 5 electricians plus 3 apprentices (2023–), 14 employees at '
         'Ventek-Air (2022), 12 technicians at ARJ (2003–2010) and 37 projects with 25 specialists at Novo Nordisk '
         '(2022–2024).'),
        ('BSc or MSc in Electrical Engineering, Automation or related',
         'B.Tech in Technology Management & Mechanical Engineering (EQF 6) with electrical and mechanical design and '
         'electrical engineering studies at Tehran Technical University, plus Danish electrical authorisation at '
         'LV, MV and HV.'),
        ('Leading and developing a team of around 11 employees and consultants',
         'Led teams of 5, 12 and 14 plus consultants and subcontractors; competence matrix, 1:1s, mentoring and '
         'recruitment as standing practice — and strong professional relationships with customers and stakeholders '
         'built in every project.'),
        ('Managing resource allocation across projects and portfolios',
         'Allocated 25 specialists across 37 parallel capital projects at Novo Nordisk, and staffed 11 parallel '
         'construction projects from a 14-person organisation at Ventek-Air.'),
        ('Project contribution with technical and managerial leadership',
         'Hands-on in the discipline while leading: design reviews, FAT/SAT, loop checks, testing and commissioning, '
         'IQ/OQ/PQ and audited handover — zero critical findings.'),
        ('Driving competency development with senior specialists',
         'Built competency matrices and apprentice programmes, and worked alongside senior specialists in pharma '
         'projects and technical operations.'),
        ('Fluency in written and spoken Danish and English',
         'Danish native, English professional written and spoken, Persian native; years in English-speaking, '
         'international project organisations, including teams in Bangalore, India.'),
        ('Knowledge of GMP and GEP requirements',
         'Two years in a GMP/FDA/EMA organisation: change control, deviations, CAPA, audit readiness and '
         'documentation produced as part of the delivery — good engineering practice in daily use.')])
    m.page_break()

    m.models_table('FIRST 90 DAYS — CAPACITY, COMPETENCE AND DELIVERY', ('Period', 'What happens, and how it is measured'), [
        ('Week 1–2',
         'Meet every engineer and consultant in the department: what they own, what they are good at, and where the '
         'work hurts. Read the live project list, the capacity picture and the last two handovers. One day on site '
         'in Kalundborg with the E&I team, boots on.'),
        ('Day 30',
         'One page: who is allocated where, what is committed for the next quarter, which competencies are thin, and '
         'the three biggest risks in the discipline. Weekly capacity review running with named owners, and a '
         'standing slot with the Bangalore counterpart.'),
        ('Day 60',
         'Discipline standards agreed for instrument index, loop documentation and panel design, with two design '
         'review gates that projects actually use. Competence matrix complete, one recruitment decided and one '
         'senior specialist paired as mentor.'),
        ('Day 90',
         'A resourcing plan for the next two quarters that the portfolio manager can plan against, at least one '
         'reusable package (review checklist or test template) in use across two projects, and a written way of '
         'working between Denmark and Bangalore that does not depend on me being in the room.')])

    m.section('THE DISCIPLINE IS THE PRODUCT')
    m.para('In E&I the deliverable is not a drawing; it is certainty. Certainty that the instrument is specified for '
           'the medium and the hazardous area, that the loop will control what the process needs, that the panel is '
           'buildable and maintainable, that the cable is sized and labelled, and that it can all be traced from the '
           'requirement to a signed test. When that certainty is present, commissioning is short and qualification '
           'is quiet. When it is missing, every hour saved in design is paid back three times on site.', after=80)

    m.section('RESOURCE ALLOCATION: ONE BOARD, NAMED OWNERS')
    m.para('Capacity is the scarcest resource in pharma engineering, and it is invisible until someone makes it '
           'visible. One board, updated weekly, showing every person against every project, the committed hours and '
           'the incoming demand for the next two quarters — with a named owner per discipline scope and a rule for '
           'who decides when two projects want the same specialist. That is how 25 specialists were shared across 37 '
           'parallel projects without anyone working two full-time jobs.', after=80)

    m.section('TECHNICAL EXCELLENCE YOU CAN AUDIT')
    m.para('Excellence in this discipline is repeatable: standard templates for the instrument index, loop and cable '
           'documentation, panel and ATEX design, and qualification; design reviews at three gates — concept, '
           'detailed design and pre-FAT — with someone from another discipline in the room; and checklists that make '
           'FAT/SAT and IQ/OQ/PQ a confirmation rather than a discovery. Every standard we write once is an hour '
           'returned to every future project, and it is how a department grows without diluting its quality.', after=80)

    m.section('GROWING ENGINEERS, NOT JUST FILLING ROLES')
    m.para('A department of eleven people is a department of eleven careers. I want a competence matrix that shows '
           'each engineer\'s depth across instrument types, control systems, electrical design and qualification '
           'work, and a plan for the next step — whether that is specialist depth or project leadership. Senior '
           'specialists should be mentoring by default, and the difficult projects should be where someone grows, not '
           'where someone drowns. I have trained apprentices, technicians and engineers, and I have hired for '
           'attitude as often as for experience.', after=80)

    m.section('DENMARK AND BANGALORE, ONE TEAM')
    m.para('Distributed engineering only works when the interfaces are designed as carefully as the panels. That means '
           'overlapping hours for the handover, one source of truth for documents and status, written scope before '
           'work travels, and the same standards in both places — plus the discipline to say what is decided and '
           'what is still open. I have run projects where engineering, procurement and operations sat in different '
           'countries, and the ones that went well were the ones where the interface was owned by a person with a '
           'name, not by a process diagram.', after=80)

    m.section('GMP, GEP AND THE AUDIT TRAIL')
    m.para('In an API plant, GMP and good engineering practice are the same thing done honestly: requirements before '
           'design, design before purchase, tests before release, and a record of every deviation with a root cause '
           'and a verified corrective action. I have worked where a missing signature stops a batch release, and I '
           'have handed over systems that were inspected without a critical finding. A department that produces its '
           'documentation while it works never needs a rescue operation before an audit.', after=80)

    m.section('DIGITAL WORK THAT GIVES HOURS BACK')
    m.para('I build my own tools in Python and Claude: traceability matrices that stay in step with the test list, IO '
           'and deviation logs filtered by area and owner, capacity and alarm statistics pulled into one page, and '
           'investment cases with NPV, IRR and scenarios. It does not replace the validated systems or the '
           'engineering judgement, and it stays inside the procedures — but it makes follow-up fast enough that '
           'engineers actually do it.', after=80)

    return m.save(path, title='Application and CV — Department Manager, Electrical & Instrumentation, NNE',
                  subject='People leadership and project execution in electrical and instrumentation engineering',
                  keywords='E&I, department manager, electrical, instrumentation, GMP, GEP, IQ OQ PQ, FAT, SAT, '
                           'resource allocation, competence development')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_NNE_EI_DepartmentManager.docx')))
