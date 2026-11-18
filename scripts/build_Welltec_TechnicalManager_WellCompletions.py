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

LETTER = [
    ('Dear Hiring Manager,', False),
    ('On a completion job, the right tool is only part of a sound plan. It has to fit the well design, '
     'barrier requirements, Torque and Drag assumptions and the limits set for the job. If actual '
     'conditions move away from that basis, the crew needs to know what can be decided at the well, '
     'what must be reviewed, and who has the authority to make that call. That is where technical advice '
     'and client support matter: operating staff and clients need clear technical guidance from job planning, '
     'through ongoing jobs and into the review afterward. The client group is broad: operators, IOC and NOC '
     'teams, service companies and drilling contractors, mostly in the Eastern Hemisphere.', True),
    ('The review should start before equipment leaves the base. Put the current well information, approved '
     'design, tool configuration, procedures and acceptance criteria in front of the people who will plan '
     'and execute the job. Check the assumptions that matter, confirm that equipment and people are ready, '
     'and make open questions visible. Safety assurance and quality assurance depend on using current, '
     'checked information. A checklist is useful only if it catches a missing input; it is not a substitute '
     'for technical review of the job plans.', True),
    ('Non-regular work needs an early conversation, not a rushed exception at the end of planning. Bring '
     'the relevant operations and engineering specialists in while there is still time to compare options. '
     'Set out the changed conditions, risks, stop points and contingencies; agree the client interface and '
     'the person who can approve the change. If the technical basis is not clear, the plan is not ready.', True),
    ('During the job, keep the technical conversation close to what is actually happening: record the '
     'conditions, tool response and decisions, and compare them with the programme. When something falls '
     'outside the agreed envelope, pause, review and communicate the decision before work continues. After '
     'an incident investigation, a useful client review includes careful failure analysis: reconstruct the '
     'sequence from the records, separate evidence from theory, and leave with actions that have an owner '
     'and a due date.', True),
    ('Sales support should help the commercial team turn a customer’s requirement into a clear technical '
     'proposal, with the application, assumptions and limitations explained before anyone makes a '
     'commitment. Welltec’s Advanced Well Architecture shows why the system matters: the annular barrier, '
     'flow valve and downhole actuator have to work together in the well design. Training should connect '
     'the tool to the job it will perform, then check understanding before someone works independently. '
     'Across bases, the record and the reasoning should travel with the job, even when local conditions '
     'differ.', True),
    ('The first months should make good use of the mentoring described in the posting: learn the portfolio '
     'and approval routes beside the Global Operations Manager, sit in on planning and post-job reviews, '
     'and take on defined reviews with feedback. Responsibility can grow as product knowledge and '
     'Well Completions, barrier and Torque and Drag competence are demonstrated. That is a practical way '
     'to support Welltec’s Pioneering and Agile approach without relaxing the Dedicated work of safe, '
     'well-evidenced delivery.', True),
    ('Kind regards,', False),
    ('Shahram Ajloo', False),
]

PROFILE = (
    'Technical operations leader and Danish-authorised marine engineer (LV/MV/HV) with more than 20 years '
    'in electrical and mechanical service, plant maintenance, commissioning and project delivery. Work has '
    'ranged from urgent fault-finding and 24/7 plant operations to the coordination of 37 concurrent CAPEX '
    'projects in a GMP environment. Leads technical teams, works across client and contractor interfaces, '
    'and keeps safety, quality and handover records tied to the work. Holds a B.Tech in Technology '
    'Management & Mechanical Engineering. Danish and Persian/Farsi are native languages; English is '
    'professional. Open to relocating to Esbjerg and to occasional international travel.')

STRENGTHS = [
    ('Fault-finding',
     'Electrical and mechanical troubleshooting in service and live plant environments. Uses A3, 5 Why and '
     'Ishikawa to work from symptoms and records toward a checked cause and corrective action.'),
    ('Planning and follow-through',
     'Schedules, resources, contractors, costs and changing interfaces across 37 CAPEX projects, 11 '
     'parallel installations and 24/7 operations.'),
    ('Safety and quality records',
     'LOTO and risk assessment in field work; FAT/SAT, IQ/OQ/PQ and GMP documentation in commissioning. '
     'Novo Nordisk project handovers had no critical findings.'),
    ('Client and stakeholder management',
     'Customer dialogue, quotations and service agreements at ELOHVAC; project coordination among '
     'engineering, procurement, contractors, site teams and management.'),
    ('People and practical instruction',
     'Daily supervision and planning for teams of 5–25, including three apprentices; 1:1 and MUS, '
     'structured training and feedback.'),
    ('Digital work',
     'SAP ERP, Excel/Power Query, Power BI, Python and Claude API. Leads AI coding work, LLM APIs and '
     'agents for technical and industrial applications; engineering and human review are retained.'),
]

EXPERIENCE = [
    ('Owner / Technical Director / Danish-authorised Marine Engineer',
     'ELOHVAC ApS · Copenhagen · May 2023–present',
     '5 electricians and 3 apprentices · full P&L responsibility',
     [
         ('Service and installation',
          'Installs and troubleshoots electrical systems, switchboards, controls and HVAC equipment, from '
          'urgent call-outs through to documented handover and preventive maintenance.'),
         ('Planning and customer work',
          'Prepares quotations and calculations, plans labour and materials, coordinates subcontractors and '
          'follows customer commitments through close-out. Handles measurements and piece-rate work '
          'agreements, including changes to completed work.'),
         ('Team and safe work',
          'Plans and supervises five electricians and three apprentices; carries out 1:1 and MUS meetings, '
          'workplace safety follow-up and structured apprentice training. Applies LOTO, APV and site risk '
          'assessments.'),
         ('Digital tools',
          'Built Python/Claude API tools for quotations, schedules, quality checklists and KPI dashboards; '
          'documented productivity improvement of more than 40%.'),
     ]),
    ('Co-owner and CTO / Technical Lead, AI Department',
     'Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 · alongside ELOHVAC',
     'AI department of 4–10 · matrix leadership across two businesses',
     [
         ('Technical applications',
          'Led customer work from requirements and architecture through integration, commissioning, '
          'documentation and handover to the client’s operations team.'),
         ('AI coding',
          'Led AI coding projects using LLM APIs and agents, with code generation, review and testing built '
          'into delivery.'),
         ('Design and management support',
          'Used AI coding to develop calculations and design options for technical systems and industrial '
          'components, with engineering validation before use. Also used AI-supported workflows for KPI '
          'analysis, meeting notes, management reports and decision papers.'),
         ('Matrix work',
          'Ran this role alongside ELOHVAC and prioritised delivery across both companies.'),
     ]),
    ('Senior Commissioning Engineer / Project Manager, Electrical Systems',
     'Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024',
     '37 concurrent CAPEX projects · 25 specialists · DKK 2–10m per project',
     [
         ('Projects and interfaces',
          'Tracked schedule, cost, risk and resources across engineering, procurement and site work; reported '
          'monthly to management and client, using SAP ERP for assets and costs.'),
         ('Commissioning and qualification',
          'Worked with switchboards, controls, UPS, emergency lighting, fire systems and PDS; supported '
          'FAT/SAT and IQ/OQ/PQ under GMP. No critical findings at project handover.'),
         ('Troubleshooting and energy',
          'Used A3, 5 Why and Ishikawa in problem-solving. A structured PDCA programme reduced energy costs '
          'by 40%.'),
     ]),
    ('Project and Workshop Manager, Ventilation & HVAC',
     'Ventek-Air · Copenhagen · Jan 2022–Nov 2022',
     '14-person team · 11 concurrent projects · DKK 2–10m each',
     [
         ('Project delivery',
          'Managed capacity and progress from specification to formal handover, coordinating tenders, '
          'subcontractors, agreements and safety documentation.'),
         ('Daily work',
          'Ran daily team meetings and bottleneck reviews; standardised work routines to improve delivery '
          'reliability.'),
     ]),
    ('Maintenance & Operations Manager / Workshop Technician',
     'Biofos, Lynetten · Copenhagen · Aug 2017–Jan 2022',
     'Critical electrical and mechanical plant · 24/7 operation',
     [
         ('Plant reliability',
          'Maintained and troubleshot pumps, HVAC, HV switchboards and SCADA; supported spare-parts flow and '
          'workshop standards.'),
         ('Shift safety',
          'Applied LOTO, risk assessments and APV; followed up near misses. Used 5S, Standard Work and PDCA '
          'in the workshop and stores.'),
     ]),
    ('Electromechanic / Production Team Leader',
     'ARJ Engineering · Tehran · Dec 2003–Mar 2010',
     '12 mechanics and technicians',
     [
         ('Workshop work',
          'Planned shifts and materials, diagnosed and repaired industrial electrical and mechanical '
          'equipment, and followed root-cause findings through corrective action.'),
     ]),
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
     'Danish and Persian/Farsi: native · English: professional · Driving licence B · Open to relocate to Esbjerg · Occasional international travel'),
]

GAP = (
    'Direct oilfield work is not documented: no Completions Field Engineer or Service Delivery Manager post; '
    'no hands-on Well Completions design or Well Completions tools, Torque and Drag, well barriers or petroleum '
    'degree. The B.Tech is in Technology Management & Mechanical Engineering. These gaps matter for independent '
    'WCS advice and non-regular job approval; Welltec training and formal sign-off must come first.')


def build(path=OUTPUT):
    m = MasterDoc(os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'), lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('3 November 2026')
    m.meta('Welltec · Global Operations · Well Completions Services · Esbjerg · RCP-001698 · Apply by 30 November 2026')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Technical Manager, Well Completions Services', bold=True, color='1A1A1A')
    for i, (text, body) in enumerate(LETTER):
        m.para(text, after=70 if body else (40 if i == 0 else 45))

    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para(PROFILE, after=65)
    m.section('RELEVANT TECHNICAL WORK')
    for label, body in STRENGTHS:
        m.bullet(label, body, after=22)
    m.section('PROFESSIONAL EXPERIENCE')
    for title, meta, scope, bullets in EXPERIENCE[:2]:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            p = m.bullet(label, body, after=15)
            p.paragraph_format.keep_together = True
    m.section('SELECTED RESULTS')
    m.para('At Novo Nordisk, energy costs fell 40% under a structured PDCA programme, and projects were '
           'handed over with no critical findings. At ELOHVAC, digital tools improved documented '
           'productivity by more than 40%. Other scopes include 37 concurrent CAPEX projects, 25 specialists, '
           '11 parallel installations and a 14-person team.', after=35)

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
    m.section('WELL COMPLETIONS EXPERIENCE')
    m.para(GAP, after=50)

    m.section('FIRST 90 DAYS — LEARNING THE WELLS AND THE WORK')
    m.para('A starting plan to agree with the Global Operations Manager:', after=30)
    for label, body in [
        ('Days 1–30', 'Learn the portfolio and approval route with WCS specialists. Read current procedures and '
         'job packs; attend planning and post-job reviews. Set out the training needed in Well Completions '
         'design and tools, Torque and Drag, well barriers and non-regular jobs.'),
        ('Days 31–60', 'Co-review selected job plans. Check the well data, design basis, tool configuration and '
         'acceptance criteria against controlled documents. Join an incident investigation and follow the '
         'findings into any procedure or training change.'),
        ('Days 61–90', 'Take on defined reviews within delegated authority; broader approvals follow Welltec sign-off.')]:
        p = m.bullet(label, body, after=12)
        p.paragraph_format.keep_together = True

    return m.save(path,
                  title='Application and CV — Technical Manager, Well Completions Services, Welltec (RCP-001698)',
                  subject='Technical Operations · Well Completions · Global Operations · Esbjerg',
                  keywords='Technical Manager, Well Completions Services, Global Operations, safety, quality, commissioning, troubleshooting, Torque and Drag, well barriers',
                  comments='Job-focused cover letter and CV. MasterDoc design. Well Completions domain gaps disclosed.')


if __name__ == '__main__':
    print(build())
