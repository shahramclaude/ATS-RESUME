# -*- coding: utf-8 -*-
"""Welltec — Technical Manager, Well Completions Services (RCP-001698).
English application and CV in the established MasterDoc design.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT = os.path.join(ROOT, 'Shahram_Ajloo_Welltec_TechnicalManager_WellCompletions.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Technical Operations · Safety, Quality & Commissioning'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'

LETTER_OPENING = [
    'A well-completion job is decided long before the tool reaches the well: the design basis, barrier '
    'envelope, equipment configuration, operating limits and contingencies must agree. During the job, '
    'conditions can diverge from the plan; afterward, the investigation must produce learning that is '
    'specific enough to change the next procedure. For Welltec’s Well Completions Services, technical '
    'assurance has to connect those three moments across clients, commercial teams and operating bases.',
    'The role’s global scope and hands-on mentoring create a clear route to independent technical '
    'responsibility. A disciplined operating system can protect that learning curve while supporting '
    'safe, high-quality delivery from the first assignments:',
]

LETTER_POINTS = [
    ('Before the job — establish a common technical basis',
     'For every planned completion, bring the well data, approved design, barrier philosophy, torque-and-drag '
     'basis, toolstring configuration, operating envelope and client requirements into one controlled review. '
     'Confirm that the procedure, equipment status, personnel competence, interfaces and contingencies match '
     'the approved basis. Record assumptions and unresolved inputs; do not let an unverified assumption become '
     'a field instruction.'),
    ('At the readiness gate — make the decision traceable',
     'Use a documented checklist for the job plan, risk controls, instructions, equipment and acceptance '
     'criteria. Classify routine versus non-regular work against Welltec’s own rules and delegated authority. '
     'For a non-regular job, route the technical basis and deviations to the required engineering and operations '
     'review, with explicit hold points, client alignment and a named approval. No plan should be released on '
     'an informal understanding.'),
    ('During execution — protect the approved envelope',
     'Keep a concise record of actual conditions, tool response, decisions and changes against the plan. If a '
     'limit, barrier assumption or acceptance criterion is challenged, pause at the agreed hold point, make the '
     'risk and options visible, and escalate through the defined technical authority. Resume only when the '
     'decision, revised instruction and required client agreement are documented.'),
    ('After an event — turn evidence into prevention',
     'In a client follow-up after an investigation or incident, build a shared timeline from records and '
     'measurements, separate established facts from hypotheses, test the failure mechanism, and assign '
     'corrective actions to owners and due dates. Feed validated learning into job plans, instructions and '
     'training, then check that the change is used at other bases where it applies.'),
    ('Across clients, sales and bases — teach one controlled method',
     'In technical sales discussions, distinguish validated capability from a proposed application, explain '
     'the assumptions and operational trade-offs, and involve the right specialist before a commitment is '
     'made. Teach through tool demonstrations, job-plan walkthroughs and teach-back; qualify competence against '
     'the task before independent assignment. Keep the technical record consistent across regions and the '
     'Eastern Hemisphere handovers.'),
]

LETTER_CLOSE = (
    'Welltec’s AWA brings together WAB zonal isolation, WFV flow control and DHA actuation; the interfaces '
    'matter as much as each product on its own. Review must therefore trace the proposed configuration back '
    'to the approved completion design and operating limits. That makes the values operational: Pioneering '
    'and Visionary in evaluating alternatives, Dedicated in evidence and qualification, and Agile in meeting '
    'client needs without leaving the approved envelope. The first phase should be spent learning Welltec’s '
    'portfolio and approval system with the Global Operations Manager: observe planning and field reviews, '
    'study controlled procedures and product limits, then take bounded review tasks with feedback. Scope '
    'should expand only as product knowledge, barrier and torque-and-drag competence, and delegated authority '
    'are demonstrated. The result is early contribution without confusing transferable operating discipline '
    'with specialist well completions expertise.')

PROFILE = (
    'Technical operations and project leader with 20+ years across electrical and mechanical service, '
    'industrial operations, commissioning and regulated production. Combines hands-on troubleshooting with '
    'document control, risk review, cross-functional planning, client coordination, technical handover and '
    'team development. At Novo Nordisk, coordinated 37 concurrent CAPEX projects and 25 specialists through '
    'GMP commissioning and qualification, with no critical findings at handover. In critical 24/7 operations, '
    'worked with equipment availability, preventive maintenance, LOTO and root-cause methods. Holds a B.Tech '
    'in Technology Management & Mechanical Engineering and Danish LV/MV/HV electrical authorisation. '
    'Professional English; open to relocation to Esbjerg and occasional international travel. Direct oilfield '
    'completions experience is not documented; the relevant operating evidence and the learning gap are '
    'separated below.')

TRANSFER = [
    ('Technical troubleshooting and failure analysis',
     'Electrical and mechanical fault-finding, preventive maintenance, A3, 5 Why and Ishikawa; separates '
     'symptoms, evidence, causes and corrective action.'),
    ('Planning and controlled execution',
     'Scope, resources, schedule, interfaces, risk and change follow-up across 37 simultaneous CAPEX projects, '
     '11 parallel installations and live 24/7 operations.'),
    ('Safety, quality and assurance',
     'LOTO, APV/risk assessment, FAT/SAT, IQ/OQ/PQ, GMP documentation, deviation follow-up and structured '
     'handover; no critical findings at Novo Nordisk project handover.'),
    ('Client and stakeholder coordination',
     'Documented customer dialogue, offers and service agreements at ELOHVAC; coordination among engineering, '
     'procurement, site teams, contractors and management.'),
    ('Training and operational leadership',
     'Led teams of 5–25, including 3 apprentices; daily planning, 1:1/MUS, structured instruction, feedback '
     'and cross-functional matrix leadership.'),
    ('Digital tools and reporting',
     'SAP ERP, MS Office, Excel/Power Query, Power BI, Python and Claude API. AI coding, LLM APIs and agents '
     'used in technical/industrial applications; outputs reviewed and validated by people.'),
]

EXPERIENCE = [
    ('Owner / Technical Director / Authorised Electrical Engineer',
     'ELOHVAC ApS · Copenhagen · May 2023–present',
     '5 electricians + 3 apprentices · full P&L accountability',
     [('Technical service and troubleshooting',
       'Installation, switchboards, controls, fault-finding and preventive maintenance on electrical, '
       'ventilation and HVAC systems, from urgent call-out to documented handover.'),
      ('Planning, customers and delivery',
       'Prepared quotations and calculations; planned labour, materials and subcontractors; coordinated '
       'customer commitments, quality checks and close-out documentation.'),
      ('People and safe work',
       'Daily planning and supervision of 5 electricians and 3 apprentices; 1:1/MUS, structured training, '
       'LOTO, APV and site risk assessments.'),
      ('Digital improvements',
       'Python/Claude API tools for quotation calculations, schedules, quality checklists and KPI dashboards; '
       'documented productivity improvement over 40%.')]),
    ('Co-owner and CTO / Technical Lead, AI Department',
     'Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 · concurrent with ELOHVAC',
     'AI department of 4–10 · matrix leadership across two businesses',
     [('Technical and industrial applications',
       'Led requirements, architecture, integration, commissioning, documentation and transfer to client '
       'operations.'),
      ('AI coding and LLM solutions',
       'Led AI coding work using LLM APIs and agents; established code generation, review and testing '
       'workflows.'),
      ('Engineering design and management support',
       'AI coding for technical-system and industrial-component design, calculations and sizing, with '
       'engineering validation. Used AI-supported workflows for management reporting, meeting summaries, '
       'KPI analysis and decision papers.'),
      ('Matrix leadership',
       'Prioritised work across two concurrent companies through shared planning and explicit priorities.')]),
    ('Senior Commissioning Engineer / Project Manager, Electrical Systems',
     'Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024',
     '37 concurrent CAPEX projects · 25 specialists · DKK 2–10m per project',
     [('Project and interface control',
       'Tracked progress, cost, risk and resources across engineering, procurement and site execution; '
       'reported monthly to management and client and used SAP ERP for assets and costs.'),
      ('Commissioning and qualification',
       'Electrical systems, switchboards, controls, UPS, emergency lighting, fire systems and PDS; FAT/SAT '
       'and IQ/OQ/PQ under GMP. No critical findings at handover.'),
      ('Energy and problem solving',
       'Structured PDCA programme reduced energy costs by 40%; applied A3, 5 Why and Ishikawa to '
       'troubleshooting and improvement.')]),
    ('Project and Workshop Manager, Ventilation & HVAC',
     'Ventek-Air · Copenhagen · Jan 2022–Nov 2022',
     '14-person team · 11 concurrent projects · DKK 2–10m each',
     [('Execution and handover',
       'Managed project capacity and progress from specification to formal handover; coordinated tenders, '
       'subcontractors, agreements and safety documentation.'),
      ('Daily operations',
       'Used daily boards and bottleneck analysis; standardised work routines to improve delivery reliability.')]),
    ('Maintenance & Operations Manager / Workshop Technician',
     'Biofos, Lynetten · Copenhagen · Aug 2017–Jan 2022',
     'Critical electrical and mechanical plant · 24/7 operations',
     [('Reliability and maintenance',
       'Fault-finding and preventive maintenance on pumps, HVAC, HV switchboards and SCADA; spare-parts flow '
       'and workshop standards.'),
      ('Safety and shift work',
       'Applied LOTO, risk assessment and APV; followed up near misses in shift operations; used 5S, '
       'Standard Work and PDCA.')]),
    ('Electromechanic / Production Team Leader',
     'ARJ Engineering · Tehran · Dec 2003–Mar 2010',
     '12 mechanics and technicians',
     [('Workshop and equipment',
       'Planned shifts and materials, diagnosed and repaired industrial electrical and mechanical equipment, '
       'and applied root-cause and corrective-action methods.')]),
]

EDUCATION = [
    ('B.Tech, Technology Management & Mechanical Engineering',
     'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · EQF 6'),
    ('Electrical and Mechanical Design, Electrical Engineering (EQF 6)',
     'Tehran Technical University · 2000–2003'),
    ('Higher Preparatory Examination, Mathematics and Physics', 'VUC · 2012–2017'),
    ('Danish electrical authorisation, LV/MV/HV', 'Danish Safety Technology Authority · 2023'),
    ('PRINCE2 Certified Project Manager', 'AXELOS / PeopleCert'),
    ('Lean and Six Sigma methods', 'Applied in practice; not certified'),
    ('Languages and mobility',
     'Danish and Persian/Farsi: native · English: professional · Driving licence B · Open to relocate to Esbjerg · Occasional international travel: yes'),
]

GAP = (
    'DOMAIN GAP — No documented work as a Completions Field Engineer or Service Delivery Manager; no '
    'documented Well Completions design or tool experience, Torque & Drag analysis, well-barrier design or '
    'oilfield operations; no Petroleum Engineering or Petroleum Technology degree. The technical degree is '
    'in Technology Management & Mechanical Engineering. These are material gaps for independent WCS advice '
    'and non-regular job approval. The vacancy explicitly describes hands-on onboarding and mentoring; '
    'technical authority should therefore grow only after product, well-barrier, torque-and-drag and '
    'Welltec-specific competence have been demonstrated and formally delegated.')

KEYWORDS = (
    'Technical Manager · Well Completions Services · Global Operations · technical advice · technical guidance · '
    'client support · IOC · NOC · job planning · ongoing jobs · post-job review · incident investigation · '
    'sales support · job plans · procedures · safety assurance · quality assurance · non-regular jobs · '
    'troubleshooting · failure analysis · Well Completions design · Well Completions tools · Torque and Drag · '
    'well barriers · completion tools · technical documentation · risk assessment · commissioning · FAT · SAT · '
    'IQ · OQ · PQ · GMP · LOTO · root cause analysis · CAPEX · stakeholder management · training · '
    'technical handover · English · Esbjerg · international travel')


def build(path=OUTPUT):
    m = MasterDoc(os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'), lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('3 November 2026')
    m.meta('Welltec · Global Operations · Well Completions Services · Esbjerg · Job ref. RCP-001698 · Deadline 30 November 2026')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Technical Manager, Well Completions Services — Technical assurance from plan to post-job learning', bold=True, color='1A1A1A')
    for text in LETTER_OPENING:
        m.para(text, after=65)
    for label, body in LETTER_POINTS:
        m.bullet(label, body, after=25)
    m.para(LETTER_CLOSE, after=75)
    m.meta('Kind regards', after=8)
    m.meta('Shahram Ajloo', after=0)

    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para(PROFILE, after=70)
    m.section('TRANSFERABLE TECHNICAL CONTRIBUTION')
    for label, body in TRANSFER:
        m.bullet(label, body, after=25)
    m.section('PROFESSIONAL EXPERIENCE')
    # Page 2 begins with the current and most recent roles.
    for title, meta, scope, bullets in EXPERIENCE[:2]:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            p = m.bullet(label, body, after=15)
            p.paragraph_format.keep_together = True
    m.section('SELECTED RESULTS')
    m.para('40% lower energy costs through PDCA at Novo Nordisk · no critical findings at Novo project handover · '
           'over 40% documented productivity improvement through ELOHVAC digital tools · 37 concurrent CAPEX '
           'projects / 25 specialists · 11 parallel projects / 14-person Ventek-Air team · 5 electricians and '
           '3 apprentices led at ELOHVAC.', after=40)

    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFESSIONAL EXPERIENCE — CONTINUED')
    for title, meta, scope, bullets in EXPERIENCE[2:]:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            p = m.bullet(label, body, after=15)
            p.paragraph_format.keep_together = True
    m.section('EDUCATION, AUTHORISATION & LANGUAGES')
    for title, meta in EDUCATION:
        m.edu(title, meta)
    m.section('WELL COMPLETIONS — HONEST TECHNICAL GAP')
    m.para(GAP, after=50)

    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROPOSED LEARNING & ASSURANCE PLAN')
    m.para('A proposed onboarding framework, to be aligned with Welltec’s actual management system, product '
           'qualification, delegated technical authority and Global Operations Manager. It does not replace '
           'Welltec procedures or engineering approvals.', after=65)
    m.models_table('FIRST 90 DAYS — LEARN, VERIFY, THEN EXPAND AUTHORITY',
                   ('Period', 'Learning and controlled contribution'),
                   [('Days 1–30',
                     'Work alongside the Global Operations Manager and experienced WCS specialists. Map the '
                     'portfolio and intended applications; study controlled job plans, instructions, equipment '
                     'limits, barrier terminology, torque-and-drag inputs, non-regular job criteria and escalation '
                     'routes. Observe client, planning and post-job reviews; record questions and prerequisites '
                     'for competence sign-off.'),
                    ('Days 31–60',
                     'Complete supervised reviews of selected job packs and technical records. Trace each decision '
                     'to the approved design basis, client requirements, risk controls, tool configuration and '
                     'acceptance criteria. Participate in a post-job or incident review; present facts, open '
                     'questions and actions for specialist review. Teach back a product or procedure only after '
                     'the responsible expert confirms technical accuracy.'),
                    ('Days 61–90',
                     'Take on defined review tasks within the documented delegation matrix. Demonstrate consistent '
                     'handling of assumptions, deviations, hold points, change control and customer communication. '
                     'Agree an individual competence plan for WCS design, tools, Torque & Drag and well barriers. '
                     'Expand independent decisions only after formal qualification and sign-off.')])
    m.section('REVIEW CHECKPOINTS FOR A NON-REGULAR JOB')
    for label, body in [
        ('Basis and inputs', 'Approved well design and current data; assumptions, client constraints and interfaces identified.'),
        ('Technical envelope', 'Tool configuration, operating limits, barrier requirements, torque-and-drag basis and contingencies reviewed by qualified authorities.'),
        ('Execution controls', 'Risk assessment, procedure revision, equipment status, personnel competence, hold points, stop criteria and escalation route confirmed.'),
        ('Approval and record', 'Required technical reviews, client alignment and delegated approval documented before release; changes controlled and captured.'),
        ('Learning loop', 'Actual-versus-plan data, incident evidence, actions, owners and due dates carried into the next controlled revision.')]:
        m.bullet(label, body, after=20)
    m.section('ATS KEYWORDS')
    m.para(KEYWORDS, after=35)

    return m.save(path,
                  title='Application and CV — Technical Manager, Well Completions Services, Welltec (RCP-001698)',
                  subject='Technical Operations · Well Completions · Global Operations · Esbjerg',
                  keywords='Technical Manager, Well Completions Services, Global Operations, technical assurance, safety, quality, commissioning, troubleshooting, Torque and Drag, well barriers',
                  comments='Job-focused cover letter and CV. MasterDoc design. Direct Well Completions domain gaps disclosed.')


if __name__ == '__main__':
    print(build())
