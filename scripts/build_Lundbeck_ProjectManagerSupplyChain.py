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
TITLE = 'Project Manager | Supply Chain | Cross-functional delivery and digital tools'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'

DATE = '3 November 2026'
RECIPIENT = 'Lundbeck · Trine Munch Agerskov, Director of Supply Chain Project Management'
SUBJECT = 'Application: Project Manager, Supply Chain Project Management | req. 8265'

# ------------------------------------------------------------------ side 1
INTRO = ['Lundbeck needs project management that keeps work moving across functions and gives the team a '
 'consistent way to make decisions. The combination of hands-on delivery and developing practical tools '
 'is what draws me to this assignment.',
 'At Novo Nordisk, I coordinated 25 specialists across engineering, procurement and construction on 37 '
 'CAPEX projects, with regulated testing and handover. I would bring that experience to an agreed '
 'Supply Chain project, alongside the analytical and digital skills I use to turn complex work into '
 'clear plans and follow-up.',
 'I am a professional Claude coder and build Python/Claude API tools for estimating, scheduling and '
 'quality documentation. They have improved productivity by over 40% in contracting. I would like to '
 'put that practical approach to work with your team in Valby: deliver the project, test useful '
 'improvements and leave tools colleagues can maintain.']




HONEST = ('Pharmaceutical experience: Novo Nordisk, Nov 2022–Jul 2024, in electrical CAPEX and commissioning; '
 'this is adjacent to, rather than two years within, pharmaceutical supply chain, CMC or contract '
 'manufacturing.')




# ------------------------------------------------------------------ CV
PROFILE = ('Supply Chain projects move forward when the technical work, decisions and receiving organisation are '
 'aligned. My contribution is cross-functional project delivery backed by pharmaceutical commissioning '
 'experience, commercial responsibility and hands-on digital development. At Novo Nordisk I coordinated '
 '25 specialists across 37 CAPEX projects and worked with FAT/SAT and regulated handover. At Ventek-Air '
 'I led a 14-person team across 11 projects. B.Tech in Technology Management & Mechanical Engineering; '
 'professional Claude coder building tools that support planning, analysis and quality follow-up.')

PRACTICE = [('Keeping several workstreams moving',
  'At Novo Nordisk, followed progress, budgets, risks and resources across engineering, procurement and '
  'construction. Reported to management and the client, bringing technical delivery and commercial '
  'consequences into the same project discussion.'),
 ('Taking work through to acceptance',
  'Worked with FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA at Novo, with no critical findings at handover. '
  'Experience carrying technical work through testing and documented acceptance is central to my '
  'approach to implementation.'),
 ('Turning constraints into a workable plan',
  'At Ventek-Air, managed 11 concurrent projects from specification to formal handover. Used daily '
  'visual meetings, capacity planning and bottleneck analysis with a 14-person team to coordinate work '
  'and improve delivery performance.'),
 ('Building useful digital tools',
  'Developed Python/Claude API tools for estimates, schedules, quality checklists and KPI dashboards in '
  'ELOHVAC. Over 40% productivity improvement in contracting. Professional use of Claude Code, '
  'supported by practical coding and workflow design.'),
 ('Making the numbers useful',
  'Work with Excel/Power Query, Power BI and Python, including investment models with NPV/IRR, '
  'scenarios and sensitivity. Used SAP at Novo for finance, assets and cost control. Connect analysis '
  'to the options and consequences a decision maker needs to understand.'),
 ('Taking responsibility for delivery',
  'Full P&L at ELOHVAC, covering quotations, planning, materials, subcontractors and customer delivery. '
  'Lead 5 electricians and 3 apprentices with daily allocation, individual follow-up and structured '
  'training.')]

MODELS = [('Visual planning and bottleneck analysis',
  'Ventek-Air: daily huddles and capacity/follow-up routines across 11 projects. A practical foundation '
  'for keeping dependencies and the next action visible.'),
 ('PDCA and structured problem solving',
  'Novo/Biofos: PDCA improvement work; A3, 5 Whys and Ishikawa for technical problems. Start with '
  'evidence, work through the cause and check the result.'),
 ('Acceptance and documentation',
  'Novo: FAT/SAT and IQ/OQ/PQ in a regulated environment. Follow requirements, test findings and '
  'handover documentation through to acceptance.'),
 ('Standard Work and 5S',
  'Biofos: workshop and inventory practices supporting maintenance and spare-part flow. Experience '
  'making a way of working usable in daily operations.'),
 ('Individual follow-up and learning',
  'ELOHVAC: daily planning, 1:1/development conversations and apprentice training. Clear expectations, '
  'support and follow-through on agreed actions.')]

ACHIEVEMENTS = [('Regulated delivery', 'No critical findings at handover in Novo FAT/SAT and IQ/OQ/PQ work.'),
 ('Measurable improvement', '40% reduction in energy costs through a PDCA programme at Novo.'),
 ('Tools used in real work',
  'Over 40% productivity improvement through own Python/Claude API tools in contracting.')]

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

PRACTICAL_CV = ('Based in Måløv, within reach of Valby. The position is a one-year temporary assignment. Start date, '
 'transition from ELOHVAC, limited travel and occasional meetings outside office hours to be agreed.')

REFERENCES = 'Former managers at Novo Nordisk A/S and Biofos (Lynetten) — available on request.'

PARTNER = [('Director and PM colleagues',
  'Agree the scope of the roadmap work and how it supports current projects. Bring a short '
  'recommendation with options, resource implications and the decision needed. Use the team’s '
  'experience to judge what is worth standardising.'),
 ('CMC, QA and Regulatory Affairs',
  'Establish the technical, quality and regulatory input required for each change. Put reviews and '
  'approvals in the plan early and agree the information needed, the owner and the decision date.'),
 ('Artwork & Master Data, Production Planning and Commercial',
  'Walk through how the change reaches their processes. Identify the inputs, sequencing and '
  'implementation dates that must line up. Bring conflicting assumptions into one working session and '
  'record the agreed way forward.'),
 ('Contract Manufacturers and other partners',
  'Align information needs, delivery commitments and open issues with the relevant Lundbeck owners. '
  'Keep external dependencies in the project plan and escalate when a late answer threatens the next '
  'milestone.')]

FIRST90 = [('First week — take ownership',
  'With the Director, select the first project and one roadmap priority. Read the existing material and '
  'meet the sponsor and functional owners. Produce a one-page project brief: outcome, scope, '
  'milestones, responsibilities and the first decisions needed. Agree who signs it off and book the '
  'first working session.'),
 ('By day 30 — agree the plan',
  'Review the brief with the functions involved and establish the delivery plan. Record risks, '
  'dependencies and issues with owners and escalation dates. Agree acceptance criteria with the '
  'receiving team. Review the current intake and portfolio process with PM colleagues; select one live '
  'case on which to test a simpler project-intake brief.'),
 ('By day 60 — execute and test',
  'Run the project’s working sessions around decisions and obstacles. Follow the agreed actions into '
  'execution and implementation. Pilot the intake brief and a concise portfolio review with the '
  'Director and team. Use the pilot to define what a fit-for-purpose stage-gate should ask for at the '
  'next decision, building on existing approval processes.'),
 ('By day 90 — review and hand over the routine',
  'Review milestone progress and implementation readiness with the sponsor. Resolve or escalate the '
  'remaining decisions. Compare the roadmap pilot with the previous approach: is the decision clearer, '
  'is key information missing, and is the preparation effort proportionate? Agree the version to '
  'retain, an owner and the next review date. Build the remaining assignment plan around delivery and '
  'adoption.')]

KEYWORDS = ('Cross-functional project management · Planning and implementation · Risks, dependencies and '
 'milestones · Stakeholder communication · Analysis and recommendations · FAT/SAT · PDCA, A3 and 5 Whys '
 '· SAP finance/assets · Excel/Power Query · Power BI · Python · Claude Code and Claude API.')


def build(path):
    m = MasterDoc(TEMPLATE, lang="en-GB")

    # ---------------------------------------------------------------- side 1
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta(RECIPIENT)

    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, SUBJECT, bold=True, color="1A1A1A")

    for t in INTRO:
        m.para(t, after=64, line=232)

    m.meta("Yours sincerely · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFESSIONAL PROFILE")
    m.para(PROFILE, after=80)

    m.section("PROJECT DELIVERY — EVIDENCE FROM PRACTICE")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("METHODS USED IN PRACTICE",
                   ("Area", "Methods and tools"), MODELS)

    m.section("RESULTS")
    for label, body in ACHIEVEMENTS:
        m.bullet(label, body, after=30)

    m.page_break()
    m.section("PROFESSIONAL EXPERIENCE")
    for title, meta, scope, bullets in EXPERIENCE:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=30)

    m.para(HONEST, after=80)

    m.section("EDUCATION")
    for t, meta in EDUCATION:
        m.edu(t, meta)

    m.section("AUTHORISATIONS & CERTIFICATIONS")
    for _i, (t, meta) in enumerate(CERTS):
        _p_ = m.edu(t, meta)
        if _i < len(CERTS) - 1:
            _p_.paragraph_format.keep_with_next = True

    m.section("LANGUAGES")
    m.para(LANGUAGES, after=80, justify=False)

    m.section("PROJECT AND DIGITAL FOCUS")
    m.para(KEYWORDS, after=80)

    # afsluttende side
    m.page_break()
    m.models_table("FIRST 90 DAYS — LIVE PROJECT AND ROADMAP PILOT",
                   ("When", "What is in place"), FIRST90)

    m.section("WORKING WITH THE PROJECT TEAM")
    for label, body in PARTNER:
        m.bullet(label, body, after=30)

    m.section("A PRACTICAL START ON THE ROADMAP")
    m.para('For a project-intake pilot, I would ask for a concise description of the problem, the outcome sought, the sponsor, the functions involved and the decision needed next. Add the main dependencies, initial resource needs and the consequence of postponing the work. This should give the Director and team enough to compare requests and discuss prioritisation without building a business case before the question is clear. In a portfolio review, keep attention on decisions: which projects need capacity, which are blocked and what has changed since the last review? Agree the evidence required at a stage-gate with the functions responsible for quality and approval. Test the routine on real work before widening it. For digital support, begin with approved data and a clear use case, check outputs with the responsible colleagues and keep an identifiable owner. The test of the one-year assignment is that projects progress and the team can continue using the improvements afterwards.', after=80)

    m.section("PRACTICAL ARRANGEMENTS")
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

    m.save(path)


if __name__ == "__main__":
    build(os.path.join(ROOT, "Shahram_Ajloo_Lundbeck_ProjectManagerSupplyChain.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_Lundbeck_ProjectManagerSupplyChain.docx"))
