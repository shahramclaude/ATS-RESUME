# -*- coding: utf-8 -*-
"""
Lundbeck Supply Chain Project Management — English combined application/CV.
English JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Project Manager | Lundbeck Supply Chain | Execution, analysis and AI'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'

DATE = '3 November 2026'
RECIPIENT = 'Lundbeck · Trine Munch Agerskov, Director of Supply Chain Project Management'
SUBJECT = 'Application: Project Manager, Supply Chain Project Management | req. 8265'

# ------------------------------------------------------------------ side 1
INTRO = ['For Supply Chain, a project is successful when the change works in operations—not when the plan is '
 'complete. Lundbeck needs someone to keep the functions aligned through implementation while helping '
 'the PM team establish clearer intake, priorities and decision points.',
 'That combination is why I am applying. At Novo Nordisk, I coordinated engineering, procurement and '
 'construction across 37 CAPEX projects and worked with regulated testing and handover. Alongside '
 'project delivery, I build Python and Claude tools that save time in planning and quality follow-up. I '
 'would bring both to the Valby team: disciplined execution and practical improvements that colleagues '
 'can use.']




HONEST = ('My pharmaceutical experience is in electrical CAPEX and commissioning (Novo Nordisk, Nov 2022–Jul '
 '2024); the role’s specific two-year pharmaceutical supply chain/CMC/contract-manufacturing '
 'requirement remains a point to discuss.')




# ------------------------------------------------------------------ CV
PROFILE = ('Reliable Supply Chain execution depends on clear priorities, timely decisions and a receiving '
 'organisation ready for the change. I bring technical project leadership in pharmaceutical operations, '
 'experience coordinating specialist teams and practical digital development. My work at Novo Nordisk '
 'covered electrical CAPEX, commissioning and regulated handover; at ELOHVAC it combines delivery, '
 'commercial responsibility and building tools for the people doing the work. B.Tech in Technology '
 'Management & Mechanical Engineering. Professional Claude coder using Python, Claude Code and the '
 'Claude API.')

PRACTICE = [('Cross-functional delivery',
  'Novo Nordisk: coordinated 25 specialists across engineering, procurement and construction. Followed '
  'project progress, budgets, risks and resources, with monthly reporting to management and the '
  'client.'),
 ('Implementation and quality',
  'Novo Nordisk: FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA, with no critical findings at handover. Worked '
  'across technical delivery, testing and documentation through to acceptance.'),
 ('Planning under competing demands',
  'Ventek-Air: led a 14-person team across 11 concurrent projects, from specification to formal '
  'handover. Used capacity planning and daily bottleneck analysis to keep work moving.'),
 ('Analysis for decisions',
  'Excel/Power Query, Power BI and Python, with investment models covering NPV/IRR, scenarios and '
  'sensitivity. SAP experience in finance, assets and cost control at Novo Nordisk.'),
 ('Digital tools that are used',
  'ELOHVAC: developed Python/Claude API tools for estimates, schedules, quality checklists and KPI '
  'reporting. Over 40% productivity improvement in contracting. Professional, hands-on use of Claude '
  'Code.'),
 ('Ownership beyond the project plan',
  'ELOHVAC: full P&L, quotations, material planning, subcontractors and customer delivery. Daily '
  'planning and development of 5 electricians and 3 apprentices.')]

MODELS = [('Visual planning',
  'Ventek-Air: daily meetings and capacity planning across concurrent projects; bottleneck analysis to '
  'identify where work needed help.'),
 ('PDCA',
  'Novo Nordisk: improvement programme that reduced energy costs by 40%. Biofos: continuous improvement '
  'in workshop and plant operations.'),
 ('A3, 5 Whys and Ishikawa',
  'Novo Nordisk: structured diagnosis and root-cause work on technical problems.'),
 ('FAT/SAT and qualification',
  'Novo Nordisk: test and acceptance work under GMP, including IQ/OQ/PQ and documented handover.'),
 ('Standard Work and 5S',
  'Biofos: maintenance workshop and inventory routines, supporting spare-part flow and reliable daily '
  'work.'),
 ('1:1 reviews and training',
  'ELOHVAC: regular individual follow-up, development conversations and structured apprentice '
  'training.')]

ACHIEVEMENTS = [('37 CAPEX projects', 'DKK 2–10 million each at Novo Nordisk, with coordination of 25 specialists.'),
 ('40% lower energy costs', 'PDCA improvement programme at Novo Nordisk.'),
 ('Over 40% higher productivity in contracting',
  'Own Python/Claude API tools for estimating, planning, quality and KPI follow-up.')]

EXPERIENCE = [('Owner / Technical Director / Authorised Electrical Engineer',
  'ELOHVAC ApS · Copenhagen · May 2023 – Present',
  '5 electricians and 3 apprentices · full P&L',
  [('Client and commercial responsibility',
    'Quotations and calculation, planning, materials, subcontractors, quality assurance and handover '
    'documentation for electrical, ventilation and climate installations.'),
   ('AI-enabled working methods',
    'Python/Claude API tools for estimates, schedules, checklists and KPI dashboards; productivity '
    'improvement above 40%.'),
   ('People and quality',
    'Daily allocation, individual follow-up and structured apprentice training. LOTO, risk assessment '
    'and zero critical deviations in service agreements.')]),
 ('Senior Commissioning Engineer / Project Manager, Electrical Systems',
  'Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022 – Jul 2024',
  '37 concurrent CAPEX projects, DKK 2–10m each · coordination of 25 specialists',
  [('Multidisciplinary delivery',
    'Progress, budget, risks and resources across engineering, procurement and site operations; monthly '
    'reporting to management and client.'),
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
    'Daily huddles, bottleneck analysis and standardised workflows improving delivery performance.')]),
 ('Maintenance and Operations Manager / Workshop Technician',
  'Biofos (Lynetten) · Copenhagen · Aug 2017 – Jan 2022',
  '24/7 critical plant · pumps, HVAC, HV switchgear and SCADA',
  [('Operations and improvement',
    'Preventive maintenance, urgent fault-finding, spare-part flow and inventory; 5S, Standard Work and '
    'PDCA.'),
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

LANGUAGES = ('Danish (native) · English (professional, written and spoken) · Persian/Farsi (native) · Driving '
 'licence B')

PRACTICAL_CV = ('Based in Måløv; Valby is the intended workplace. The one-year contract, start date, transition from '
 'ELOHVAC, limited travel and occasional out-of-hours meetings are to be agreed.')

REFERENCES = 'Former managers at Novo Nordisk A/S and Biofos (Lynetten) — available on request.'

PARTNER = [('CMC, QA and Regulatory Affairs',
  'Agree the technical, quality and regulatory assessments needed before implementation. Build their '
  'inputs and approvals into the project plan early.'),
 ('Artwork & Master Data, Production Planning and Commercial',
  'Map the inputs and dates that must line up for the change to reach operations and markets. Resolve '
  'conflicting assumptions in a shared working session.'),
 ('Contract Manufacturers and other partners',
  'Coordinate commitments and information needs with the responsible Lundbeck owners. Track external '
  'dependencies alongside the internal plan.')]

FIRST90 = [('Week 1 | Define',
  'With the Director, agree the first project, sponsor and one roadmap deliverable. Meet the functional '
  'owners and review the material already available. Deliver a short project brief covering outcome, '
  'scope, decision rights, milestones and the immediate open questions.'),
 ('Day 30 | Baseline',
  'Agree the delivery plan and acceptance criteria with the receiving functions. Establish the risk, '
  'dependency and decision log. Hold a weekly working session for the active project. Review existing '
  'intake and portfolio routines with the PM team and choose one live case for a pilot.'),
 ('Day 60 | Deliver and test',
  'Move the agreed project activities into implementation. Facilitate decisions where functional plans '
  'conflict and escalate unresolved dependencies. Run the intake/portfolio pilot; agree the evidence '
  'and decision owner for a fit-for-purpose stage-gate with the relevant functions.'),
 ('Day 90 | Review and embed',
  'Review milestone delivery and implementation readiness with the sponsor. Evaluate the pilot with the '
  'PM team, agree changes and assign the owner of the continuing routine. Publish the next delivery '
  'priorities and a handover record that can be maintained through the rest of the one-year '
  'assignment.')]

KEYWORDS = ('Project planning and execution · Cross-functional coordination · Risks, dependencies and milestones · '
 'Stakeholder communication · Analysis and recommendations · Regulated handover · PDCA/A3 · SAP '
 'finance/assets · Excel/Power Query · Power BI · Python · Claude Code and Claude API.')


LETTER_ROWS = [('Start with the decision',
  'Agree the outcome, scope and sponsor of the first project. Establish which decisions are '
  'outstanding, who owns them and which functions need to contribute before the work moves on.'),
 ('Keep execution connected',
  'Build the plan with the functional owners. Link milestones to dependencies and acceptance criteria, '
  'then use working sessions to resolve the issues that threaten implementation.'),
 ('Develop the roadmap through use',
  'With the Director and PM team, select one intake or portfolio-review improvement. Test it on a live '
  'project, examine whether it improves the decision and retain what helps.'),
 ('Leave a usable handover',
  'Document the decisions, tools and ownership as the work progresses. A one-year assignment should '
  'leave projects moving and colleagues able to continue without rebuilding the approach.')]

LETTER_CLOSE = ('The following CV sets out the delivery experience and tools behind this approach; the final page '
 'turns it into a first-90-days working plan. I would welcome a conversation about the projects that '
 'need attention first and the priorities for the Supply Chain Project Management roadmap.')

REVIEW_ROWS = [('Project intake',
  'Decision to start: what problem is being solved, why now, what is in scope and who sponsors it? '
  'Include the initial capacity needs and major dependencies.'),
 ('Prioritisation and portfolio review',
  'Decision on resources or sequence: compare the need, capacity and consequence of delay. Bring '
  'blocked projects and conflicting demands to the Director and agreed decision owners.'),
 ('Stage-gate',
  'Decision to proceed: state the evidence required, the remaining conditions and who approves. '
  'Incorporate the relevant functional quality and regulatory reviews.'),
 ('Weekly project follow-up',
  'Decision or action: show progress against milestones, overdue actions and risks requiring attention. '
  'Every open issue has an owner, next action and due date.'),
 ('Pilot evaluation',
  'Decision to retain or change the routine: check whether key information was available, decisions '
  'were reached and preparation effort was proportionate. Record the feedback and the next review '
  'date.')]

DIGITAL = ('Use digital support where it removes a real delay: preparing analysis, organising project information '
 'or drafting material for review. My starting tools are Python, Excel/Power Query, Power BI and Claude '
 'Code/API. At Lundbeck, data access and tool choice must follow the approved environment, with outputs '
 'checked by the responsible colleague. The deliverable is a usable workflow with an owner and '
 'documentation—not an extra system the team has to maintain.')

def build(path):
    m = MasterDoc(TEMPLATE, lang="en-GB")
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta(RECIPIENT)
    p = m._p(spacing_after=100, line=260, justify=False)
    m._run(p, SUBJECT, bold=True)
    for text in INTRO:
        m.para(text, after=100)
    m.models_table("THE ASSIGNMENT — DELIVERY AND THE PM ROADMAP",
                   ("Priority", "How I would approach it"), LETTER_ROWS)
    m.para(LETTER_CLOSE, after=100)
    m.meta("Yours sincerely · Shahram Ajloo", after=0)

    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROJECT PROFILE")
    m.para(PROFILE, after=100)
    m.section("RELEVANT DELIVERY EXPERIENCE")
    for label, body in PRACTICE:
        m.bullet(label, body, after=50)
    m.models_table("METHODS — WHERE I HAVE USED THEM",
                   ("Method", "Evidence from practice"), MODELS)
    m.section("SELECTED RESULTS")
    for label, body in ACHIEVEMENTS:
        m.bullet(label, body, after=40)

    m.page_break()
    m.section("PROFESSIONAL EXPERIENCE")
    for title, meta, scope, bullets in EXPERIENCE:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)
    m.para(HONEST, after=80)
    m.section("EDUCATION")
    for title, meta in EDUCATION:
        m.edu(title, meta)
    m.section("AUTHORISATIONS & CERTIFICATIONS")
    for title, meta in CERTS:
        m.edu(title, meta)
    m.section("LANGUAGES")
    m.para(LANGUAGES, after=70, justify=False)
    m.section("DIGITAL AND PROJECT TOOLS")
    m.para(KEYWORDS, after=70)

    m.page_break()
    m.models_table("FIRST 90 DAYS — PROJECT DELIVERY AND ONE ROADMAP PILOT",
                   ("When", "Work and tangible output"), FIRST90)
    m.models_table("WORKING FORMAT FOR THE ROADMAP PILOT",
                   ("Review", "Information and decision"), REVIEW_ROWS)
    m.section("FUNCTIONAL ALIGNMENT")
    for label, body in PARTNER:
        m.bullet(label, body, after=35)
    m.section("DIGITAL SUPPORT THAT THE TEAM CAN USE")
    m.para(DIGITAL, after=80)
    m.section("LOCATION AND ASSIGNMENT")
    m.para(PRACTICAL_CV, after=70)
    m.meta(REFERENCES, after=0)

    for paragraph in m.doc.paragraphs:
        paragraph.paragraph_format.keep_together = True
    for table in m.doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    paragraph.paragraph_format.keep_together = True
    m.save(path)


if __name__ == "__main__":
    build(os.path.join(ROOT, "Shahram_Ajloo_Lundbeck_ProjectManagerSupplyChain.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_Lundbeck_ProjectManagerSupplyChain.docx"))
