# -*- coding: utf-8 -*-
"""Maersk People Operations Manager R201007 — English combined application and CV in stored master design."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'People Operations – Manager | Maersk | Care, consistency and service delivery'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv, Denmark")
DATE = '2 November 2026'
RECIPIENT = 'Maersk · Global Operations Team · People Advisory Services · Hiring team'
SUBJECT = 'Application: People Operations – Manager — R201007'

# ------------------------------------------------------------------ side 1
INTRO = ['A caring employee experience depends on operational reliability: a colleague’s request must reach the '
 'right advisor, the answer must reflect the applicable policy, and the underlying record must be '
 'accurate. Across countries, consistent service cannot mean ignoring local requirements. The '
 'management task is to connect care, clear ownership and controlled processes throughout the '
 'Hire-to-Retire lifecycle.',
 'The proposed operating framework is ready to adapt to GOT’s existing governance: a '
 'demand-and-capacity view, case triage and escalation rules, an advisor coaching rhythm and a small '
 'service-quality dashboard. It is an operational leadership proposal, not a claim of established HR '
 'domain expertise. Policy, benefits and local compliance decisions stay with the authorised '
 'specialists.']

BULLETS = [('Lead and develop People Operations Advisors',
  'Use individual goals, regular 1:1 conversations, skills matrices and structured feedback to support '
  'team engagement. GROW and SBI provide a proposed coaching framework; agree decision rights and '
  'escalation routes across locations. Plan coverage with Europe PA Managers and Hub PA Managers rather '
  'than leaving handoffs to personal networks.'),
 ('Allocate resources and manage service delivery',
  'Review workload distribution, case assignment, age and complexity against available skills and '
  'country coverage. Separate urgent employee-impacting cases from routine requests. Service levels '
  'should reflect agreed priorities and capacity; a faster closure is not a success if the employee '
  'must reopen the case.'),
 ('Protect data integrity and audit readiness',
  'Map the controls around Workday and other HR systems with process owners. Confirm access, '
  'validation, correction and approval responsibilities before changing workflows. Sample completed '
  'cases for documentation and record accuracy; resolve errors through controlled processes, not '
  'unofficial spreadsheets.'),
 ('Improve employee experience and case resolution',
  'Use PDCA, A3 and 5 Whys to investigate repeat contacts, delays and rework. Pilot one improvement '
  'with advisors and the relevant HR process owner. Review timeliness, accuracy and employee feedback '
  'together, with no invented targets before a baseline is established.'),
 ('Support employee self-service and recruitment operations',
  'Test whether guidance is clear, accurate and accessible, with content owners approving policy '
  'statements. Map recruitment handoffs and recurring blockers without assuming ownership of local '
  'employment rules. Training on tools, processes and policies needs practice, feedback and an '
  'escalation path, not only a launch message.'),
 ('Align stakeholders and change across geographies',
  'Keep a shared decision and dependency log between GOT and other EEO workstreams. Agree '
  'responsibilities with Europe and Hub PA Managers, communicate changes before they affect service, '
  'and use a tested case journey to verify that a standardisation effort works locally as well as '
  'globally.')]

SYSTEM = ('The first week establishes service boundaries, capacity and control ownership. By day 30, the team '
 'has agreed definitions and a baseline; by day 60, one approved process improvement is tested; by day '
 '90, leaders can assess service quality, case flow and adoption against evidence. HR experts validate '
 'the content and compliance of every proposed change.')

MIRROR = ('Transferable evidence includes direct leadership of 5 electricians and 3 apprentices with 1:1/MUS and '
 'structured training, a 14-person project team, and coordination of 25 specialists across 37 regulated '
 'CAPEX projects. Full P&L, workload planning and disciplined handover provide an operational '
 'foundation. Professional Claude user and coder, with Python/Claude API tools delivering a '
 'productivity improvement above 40% in technical contracting.')

HONEST = ('The decisive gap is the requested 10+ years in HR operations and generalist roles: that experience is '
 'not established by this CV. Nor are Workday HR administration, payroll, works council practice or '
 'multi-country People Advisory leadership. Technical operations and line management are transferable '
 'strengths, not substitutes for that requirement; suitability would depend on Maersk accepting a '
 'cross-functional transition.')

CULTURE = ('Maersk’s Constant Care, Humbleness, Uprightness, Our Employees and Our Name translate here into early '
 'risk recognition, listening to advisors, honest records, fair treatment and dependable commitments. '
 'Care includes recognising when an employee needs an informed specialist rather than an answer outside '
 'the manager’s competence.')

PRACTICAL = ('Based in Måløv, Denmark, with access to Copenhagen for this site-based role. Native Danish and '
 'Persian/Farsi; professional English, written and spoken. Start date and arrangements for the existing '
 'business would be agreed before appointment.')

CLOSING = ('A useful first conversation would clarify whether this position requires an established HR '
 'subject-matter leader from day one, or whether strong operational leadership with a structured HR '
 'learning path could be relevant.')

# ------------------------------------------------------------------ CV
PROFILE = ('The People Operations remit requires reliable service, engaged advisors and accurate employee records '
 'across countries. Transferable experience comes from technical operations leadership, direct people '
 'management, full P&L and regulated project delivery. B.Tech in Technology Management & Mechanical '
 'Engineering and Danish electrical authorisation (LV/MV/HV) describe the actual professional '
 'background, not an HR qualification. Practical methods include workload planning, daily huddles, '
 '1:1/MUS, training, PDCA and root-cause analysis. Professional Claude user and coder with '
 'Python/Claude API tools for estimates, planning, quality checklists and KPI reporting. This is a '
 'proposed transition into HR service leadership; 10+ years of HR operations/generalist experience and '
 'Workday HR administration are not established.')

PRACTICE = [('People leadership — documented evidence',
  'ELOHVAC: 5 electricians and 3 apprentices, daily allocation, 1:1/MUS, structured training and safety '
  'follow-up. Ventek-Air: 14-person team, capacity planning and daily huddles. These are '
  'line-management examples, not People Advisory roles.'),
 ('Operational coordination — documented evidence',
  '37 concurrent CAPEX projects with 25 specialists, covering progress, budget, risks and resources '
  'across engineering, procurement and site operations. Transferable to clear responsibilities and '
  'dependency management, not HR policy ownership.'),
 ('Quality and accuracy — documented evidence',
  'FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA with zero critical findings at handover. This demonstrates '
  'controlled documentation and review discipline; employment law and employee-data controls require '
  'separate HR expertise.'),
 ('Continuous improvement — documented evidence',
  '5S, Standard Work, PDCA and root-cause analysis in critical plant operations. Proposed HR use: '
  'investigate repeat cases and rework with advisors and process owners before selecting a solution.'),
 ('Stakeholder management — transferable practice',
  'Customer, supplier and multidisciplinary delivery coordination, with management reporting and clear '
  'handover. Proposed application: shared priorities and escalation between GOT, EEO workstreams and '
  'country/hub managers.'),
 ('Digital working — evidence and boundaries',
  'Python/Claude API tools improved productivity above 40% in technical contracting. Employee personal '
  'data must not enter unapproved AI services; start with approved, non-personal templates. Workday HR, '
  'payroll and works council experience remain gaps.')]

MODELS = [('Demand and capacity',
  'Case inflow, age, complexity, skills and location coverage; agreed workload distribution and case '
  'assignment. Use existing systems and avoid parallel employee records.'),
 ('Advisor development',
  '1:1, goals, skills matrix, structured learning and feedback. Proposed GROW/SBI coaching supports '
  'autonomy within competence and policy boundaries.'),
 ('Quality and control',
  'Process-owner-approved checks, access rights, correction routes and documented approvals. Sample for '
  'accuracy and audit readiness; escalate sensitive or local-compliance questions.'),
 ('Service and improvement',
  'KPIs and service levels with definitions, owner and baseline. Review timeliness, reopened cases, '
  'quality and employee feedback; PDCA/A3/5 Whys guide corrective action.'),
 ('Self-service and knowledge',
  'Named content owner, approval and review date; clear guidance and accessible escalation. Test '
  'comprehension and resolution, not only self-service usage.'),
 ('Cross-country change',
  'RACI, decision log, dependencies and communication/training plan. Local HR experts validate policy '
  'and compliance before standardisation is rolled out.')]

ACHIEVEMENTS = [('Above 40% productivity improvement',
  'Self-built Python/Claude API tools for estimates, planning, quality checklists and KPI '
  'reporting in ELOHVAC; used for technical contracting and daily delivery.'),
 ('37 concurrent CAPEX projects',
  'DKK 2–10m each, with coordination of 25 specialists and zero critical findings at handover '
  'under GMP/FDA/EMA.'),
 ('11 concurrent installation projects',
  'Specification to formal handover with a 14-person team, daily huddles and bottleneck analysis.'),
 ('40% reduction in energy costs',
  'PDCA-based improvement programme in regulated production, with SAP used for financial, asset '
  'and cost follow-up.')]

EXPERIENCE = [('Owner / Technical Director / Authorised Electrical Engineer',
  'ELOHVAC ApS · Copenhagen · May 2023 – Present',
  '5 electricians and 3 apprentices · full P&L',
  [('Client and commercial responsibility',
    'Quotations and calculation, planning, materials, subcontractors, quality assurance and '
    'handover documentation for electrical, ventilation and climate installations.'),
   ('AI-enabled working methods',
    'Python/Claude API tools for estimates, schedules, checklists and KPI dashboards; productivity '
    'improvement above 40%.'),
   ('People and quality',
    'Daily allocation, individual follow-up and structured apprentice training. LOTO, risk '
    'assessment and zero critical deviations in service agreements.')]),
 ('Senior Commissioning Engineer / Project Manager, Electrical Systems',
  'Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022 – Jul 2024',
  '37 concurrent CAPEX projects, DKK 2–10m each · 25 specialists',
  [('Multidisciplinary delivery',
    'Progress, budget, risks and resources across engineering, procurement and site operations; '
    'monthly reporting to management and client.'),
   ('Regulated quality',
    'FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA, with zero critical findings at handover. Electrical '
    'systems, UPS and emergency-lighting interfaces.'),
   ('Improvement and data',
    '40% reduction in energy costs through PDCA; SAP ERP for financial, asset and cost control.')]),
 ('Project and Workshop Manager',
  'Ventek-Air · Copenhagen · Jan 2022 – Nov 2022',
  '11 concurrent projects · 14-person team',
  [('Delivery and commercial interfaces',
    'Specification to formal handover, capacity and progress control, tenders and quotations, '
    'subcontractors, agreement basis and handover records.'),
   ('Working methods',
    'Daily huddles, bottleneck analysis and standardised workflows improving delivery '
    'performance.')]),
 ('Maintenance and Operations Manager / Workshop Technician',
  'Biofos (Lynetten) · Copenhagen · Aug 2017 – Jan 2022',
  '24/7 critical plant · pumps, HVAC, HV switchgear and SCADA',
  [('Operations and improvement',
    'Preventive maintenance, urgent fault-finding, spare-part flow and inventory; 5S, Standard '
    'Work and PDCA.'),
   ('Safe operations', 'LOTO, risk assessment and near-miss reporting in shift operations.')]),
 ('Electromechanical Technician / Production Team Leader',
  'ARJ Engineering · Tehran · Dec 2003 – Mar 2010',
  '12 mechanics and technicians',
  [('Team leadership and problem solving',
    'Shift planning, materials and targets; fault diagnosis, root-cause analysis and repair of '
    'electrical and mechanical plant.')])]

EDUCATION = [('B.Tech (EQF Level 6) — Technology Management & Mechanical Engineering',
  'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7.6/12'),
 ('Electrical & Mechanical Design, Electrical Engineering (EQF Level 6)',
  'Tehran Technical University · 2000–2003'),
 ('Upper Secondary Examination — mathematics and physics', 'VUC · 2012–2017')]

CERTS = [('Danish electrical authorisation — authorised electrical engineer (LV/MV/HV)',
  'Danish Safety Technology Authority · May 2023'),
 ('Refrigeration Technology & HVAC', 'Mercantec · 2021'),
 ('Lean practice — 5S, PDCA, VSM, A3, Kaizen', 'Applied in operations and projects'),
 ('STCW maritime safety and engine-room certificates', 'Danish Maritime Authority · 2021–2023')]

LANGUAGES = ("Danish (native) · English (professional, written and spoken) · Persian/Farsi (native) · "
             "Driving licence B")

PRACTICAL_CV = ('Based in Måløv, Denmark; Copenhagen is a practical location for site-based work. Native Danish and Persian/Farsi; professional English, written and spoken. Driving licence B. Start date and arrangements for ELOHVAC would be agreed before appointment. A transition would need a mutually agreed HR learning plan, named specialist support and explicit limits on policy, payroll and local-compliance responsibility until competence has been demonstrated. Confidentiality and approved access to employee information are prerequisites, not optional onboarding tasks.')

REFERENCES = 'Former managers at Novo Nordisk A/S and Biofos (Lynetten) — available on request.'

KEYWORDS = ('Target remit: People Operations Manager · Global Operations Team · People Advisory Services · '
 'Hire-to-Retire · People Operations Advisors · HR operational services · Recruitment operations · '
 'Workday · Data integrity · Audit readiness · Employee queries · Policies · Benefits · Local '
 'compliance · KPIs and service levels · Employee self-service · HR projects · EEO workstreams · Europe '
 'PA Managers · Hub PA Managers. HR terms describe the target role and learning requirements, not a '
 'claimed HR track record.')

# ------------------------------------------------------------ side 4
FIRST90 = [('Week 1',
  'With the hiring manager and HR process owners, agree role boundaries and the HR learning plan. Meet '
  'advisors and country/hub managers; review service scope, queue ownership and escalation. Establish '
  'access and confidentiality requirements before handling employee information.'),
 ('By day 30',
  'Map one Hire-to-Retire case journey with advisors, including recruitment operations handoffs and '
  'local exceptions. Agree service-level/KPI definitions, capacity baseline and quality-sampling rules. '
  'Output: validated ownership map, advisor development priorities and a prioritised issue log.'),
 ('By day 60',
  'Pilot one process improvement approved by the responsible HR expert. Test case assignment, knowledge '
  'content or escalation clarity on an agreed case type. Provide training, capture advisor/employee '
  'feedback and compare quality and rework with the baseline; stop changes that create compliance '
  'risk.'),
 ('By day 90',
  'Review timeliness, quality, case age, reopened requests, team engagement and self-service outcomes '
  'with GOT and PA Managers. Agree what to standardise, what must remain local and who owns the next '
  'decisions. Assess learning progress and remaining HR capability gaps before extending '
  'responsibility.')]

PARTNER = [('People Operations Advisors',
  'Protect time for learning and regular feedback. Clarify expectations, listen to workload concerns '
  'and recognise good judgement, including appropriate escalation. Do not make advisors absorb an '
  'unrealistic coverage model through hidden overtime.'),
 ('Europe PA Managers and Hub PA Managers',
  'Agree country-to-hub interfaces, case ownership, coverage and escalation expectations. Resolve '
  'competing priorities through a shared decision route and transparent evidence rather than informal '
  'workarounds.'),
 ('GOT and other EEO workstreams',
  'Maintain shared initiatives, dependencies and change communications. Process owners approve '
  'standards and training content; establish a clear route for resolving conflicting instructions '
  'before advisors receive them.'),
 ('Employees and specialist HR partners',
  'Treat employee queries with care, discretion and clear follow-up. Complex policy, benefits, payroll '
  'or local compliance matters require the appropriate authorised specialist. Communicate what is '
  'known, what needs validation and when the employee can expect an update.')]


def build(path):
    m = MasterDoc(TEMPLATE, lang="en-GB")

    # ---------------------------------------------------------------- side 1
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta(RECIPIENT)

    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, SUBJECT, bold=True, color="1A1A1A")

    for t in INTRO:
        m.para(t, after=24, line=218)

    for label, body in BULLETS:
        m.bullet(label, body, after=1, line=208)

    m.para(SYSTEM, after=20, line=212)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=0, line=204)

    m.meta("Yours sincerely · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFESSIONAL PROFILE")
    m.para(PROFILE, after=80)

    m.section("TRANSFERABLE LEADERSHIP EVIDENCE — HR EXPERIENCE NOT CLAIMED")
    for label, body in PRACTICE:
        m.bullet(label, body, after=20)

    m.models_table("PROPOSED PEOPLE OPERATIONS FRAMEWORK",
                   ("Area", "Methods and tools"), MODELS)

    m.section("SELECTED ACHIEVEMENTS")
    for label, body in ACHIEVEMENTS:
        m.bullet(label, body, after=20)

    m.section("PROFESSIONAL EXPERIENCE")
    for title, meta, scope, bullets in EXPERIENCE:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=20)

    m.section("EDUCATION")
    for t, meta in EDUCATION:
        m.edu(t, meta)

    m.section("CERTIFICATIONS & AUTHORISATIONS")
    for _i, (t, meta) in enumerate(CERTS):
        _p_ = m.edu(t, meta)
        if _i < len(CERTS) - 1:
            _p_.paragraph_format.keep_with_next = True

    m.section("LANGUAGES")
    m.para(LANGUAGES, after=80, justify=False)

    m.section("TARGET PEOPLE OPERATIONS REMIT")
    m.para(KEYWORDS, after=80)

    # afsluttende side
    m.page_break()
    m.models_table("FIRST 90 DAYS — LEARNING, CONTROL AND SERVICE QUALITY",
                   ("When", "What is in place"), FIRST90)

    m.section("CUSTOMER VALUE — CROSS-FUNCTIONAL RESPONSIBILITIES")
    for label, body in PARTNER:
        m.bullet(label, body, after=20)

    m.section("PROCESS CHANGE ACCEPTANCE TEST")
    m.para("Before a process change is scaled, confirm that the responsible HR owner has approved its policy content, the local implications have been checked and advisors know the exception route. Test a case end to end: employee request, assignment, validation, system update, response and closure. Record defects and reopenings rather than treating volume as proof of success. Any tool or automation must preserve access controls, confidentiality and the audit trail. Employee experience is assessed together with service accuracy, not traded away for a faster dashboard.", after=80)

    m.section("PRACTICAL")
    m.para(PRACTICAL_CV, after=80)

    m.section("REFERENCES")
    m.para(REFERENCES, after=80, justify=False)

    # ingen afsnit eller tabelrække må knække over en sideskift
    for _p in m.doc.paragraphs:
        _p.paragraph_format.keep_together = True
    for _tbl in m.doc.tables:
        for _row in _tbl.rows:
            for _c in _row.cells:
                for _p in _c.paragraphs:
                    _p.paragraph_format.keep_together = True

    from docx.oxml import OxmlElement as _OE
    for _tbl in m.doc.tables:
        for _tr in _tbl._tbl.tr_lst:
            _pr = _tr.get_or_add_trPr()
            _el = _OE("w:cantSplit")
            _pr.append(_el)

    return m.save(path, title="Application and CV — Maersk People Operations Manager R201007",
                  subject="People leadership, controlled service delivery and continuous improvement",
                  keywords="Maersk, people operations, service delivery, leadership, improvement",
                  comments="Stored master design. English. Transferable evidence and sector gaps explicit.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_Maersk_PeopleOperationsManager.docx")
    build(out)
    print("OK " + out)
