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
TITLE = 'Project Manager | Lundbeck Supply Chain | Delivery and practical governance'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'

DATE = '3 November 2026'
RECIPIENT = 'Lundbeck · Trine Munch Agerskov, Director of Supply Chain Project Management'
SUBJECT = 'Application: Project Manager, Supply Chain Project Management | req. 8265'

# ------------------------------------------------------------------ side 1
INTRO = ['Supply Chain projects need clear decisions and follow-through across functions, without losing sight '
 'of the operations and patients they serve. This role appeals to me because it combines delivery of a '
 'live project with making project management easier for the next team. I would begin with one assigned '
 'project and one agreed improvement to the roadmap, rather than introduce a new set of templates '
 'before understanding the work.']

BULLETS = [('Cross-functional delivery',
  'At Novo Nordisk I coordinated 25 specialists on 37 CAPEX projects of DKK 2–10 million each, '
  'following progress, cost, risks and resources across engineering, procurement and construction.'),
 ('Evidence and implementation',
  'FAT/SAT and IQ/OQ/PQ work under GMP/FDA/EMA at Novo resulted in no critical findings at handover. '
  'That experience supports clear acceptance criteria and follow-up, not a claim of CMC or '
  'pharmaceutical supply chain ownership.'),
 ('Practical digital tools',
  'I am a professional Claude user and coder. My Python/Claude API tools for estimates, schedules, '
  'quality checklists and KPI follow-up have improved productivity by over 40 % in contracting. At '
  'Lundbeck, any use would follow approved systems, data rules and human review.')]

SYSTEM = ('The final page sets out a first 90 days built around a project brief, named owners, milestones and a '
 'short risk/decision log. With the Director and team, I would test one useful improvement to project '
 'intake or review, then adjust it from actual use.')

MIRROR = ('My foundation is a B.Tech in Technology Management & Mechanical Engineering, practical technical '
 'project leadership and regulated handover experience.')

HONEST = ('My Novo role ran from November 2022 to July 2024 and focused on electrical CAPEX and commissioning. '
 'It does not establish the requested two years within pharmaceutical supply chain, CMC or contract '
 'manufacturing. I would welcome a direct discussion of whether that adjacent experience fits the '
 'initial assignments.')

CULTURE = ('Lundbeck’s curiosity, accountability and adaptability translate into a simple working habit for me: '
 'ask what is unclear, own the next action and change the plan when the evidence changes.')

PRACTICAL = ('I live in Måløv and would be based in Valby. The one-year temporary contract, start date, occasional '
 'out-of-hours meetings, limited travel and transition from ELOHVAC would need to be agreed.')

CLOSING = ('I would like to hear which project and which part of the roadmap most need attention during this '
 'one-year assignment.')

# ------------------------------------------------------------------ CV
PROFILE = ('Supply Chain projects need clear scope, decisions and an implementation plan that works across '
 'functions. My background is technical project coordination, regulated commissioning and practical '
 'digital tools. At Novo Nordisk I coordinated 25 specialists on 37 CAPEX projects with FAT/SAT and '
 'documented handover. B.Tech in Technology Management & Mechanical Engineering and authorised '
 'electrical engineer (LV/MV/HV). Professional Claude coder using Python/Claude API for planning and '
 'quality follow-up. Direct pharmaceutical supply chain, CMC and contract-manufacturing project '
 'experience is not established; the fit with the initial assignment needs assessment.')

PRACTICE = [('Cross-functional project execution',
  'Novo: 37 simultaneous CAPEX projects of DKK 2–10 million each, coordinating 25 specialists across '
  'engineering, procurement and construction. Progress, budget, risks and resources followed with '
  'reporting to management and the client. Coordination, not a claimed team of 25 direct reports.'),
 ('Implementation and acceptance',
  'FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA at Novo, with no critical findings at handover. Relevant '
  'discipline for defining acceptance evidence, tracking open findings and preparing a receiving '
  'organisation to take over.'),
 ('Planning across competing demands',
  'Ventek-Air: 11 concurrent projects and a 14-person team, from specification to formal handover. '
  'Daily visual meetings, capacity planning and bottleneck analysis, with tenders, subcontractors and '
  'delivery records.'),
 ('Analysis and recommendations',
  'Excel/Power Query, Power BI and Python; own investment models using NPV/IRR, scenarios and '
  'sensitivity. SAP for finance, assets and costs at Novo. Use explicit assumptions and options; no '
  'claim of pharmaceutical supply-planning model expertise.'),
 ('AI and digital execution',
  'Professional Claude user and coder. Own Python/Claude API tools for estimates, schedules, quality '
  'checklists and KPI dashboards delivered over 40 % productivity improvement in contracting. No claim '
  'that these tools are validated for GxP decisions or already integrated with Lundbeck systems.'),
 ('Accountability and improvement',
  'Full P&L at ELOHVAC, leading 5 electricians and 3 apprentices. PDCA, A3 and 5 Whys in plant/project '
  'work. Relevant to reliable follow-up and practical improvement, not prior ownership of a '
  'pharmaceutical PMO or portfolio-governance roadmap.')]

MODELS = [('Project definition',
  'Agree the problem, scope, intended outcome, sponsor, milestones and acceptance criteria in a short '
  'brief. Build it with the people delivering and receiving the change.'),
 ('Responsibilities and follow-up',
  'A simple responsibility matrix (RACI) can clarify owners and decision rights. Draw on Novo '
  'coordination and Ventek visual planning to close actions across functions.'),
 ('Risks and dependencies',
  'Keep a short log with consequence, next action, owner and escalation date. Tie dependencies to the '
  'plan rather than maintain an unrelated risk report.'),
 ('Workshops and decisions',
  'Proposed approach: share the question and required input before the session. Compare options, '
  'confirm the decision owner and close with agreed actions and dates.'),
 ('Intake and portfolio review',
  'Proposed roadmap contribution: test a concise project-intake brief and a review showing purpose, '
  'capacity needs and decisions. Prioritisation remains with the authorised decision makers.'),
 ('Fit-for-purpose stage-gate',
  'Co-design a small pilot with the Director and team. Agree evidence and approval for the next step, '
  'including relevant quality/regulatory input; do not impose an assumed Lundbeck model.')]

ACHIEVEMENTS = [('37 CAPEX projects at Novo Nordisk',
  'DKK 2–10 million per project, coordinating 25 specialists across engineering, procurement and '
  'construction.'),
 ('No critical findings at regulated handover',
  'FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA at Novo Nordisk.'),
 ('11 projects and a 14-person team at Ventek-Air',
  'Capacity planning, visual meetings and delivery from specification to formal handover.'),
 ('Over 40 % productivity improvement in contracting',
  'Own Python/Claude API tools for estimating, planning, quality documentation and KPI follow-up.')]

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

PRACTICAL_CV = ('Based in Måløv, Ballerup Municipality, Denmark; seeking the Valby-based assignment. The position is a '
 'one-year temporary role. Contract terms, start date, transition from ELOHVAC, limited travel and '
 'occasional virtual meetings outside office hours must be agreed. No immediate availability or '
 'acceptance of a particular schedule is assumed. Native Danish and professional English. No photo or '
 'unrelated personal details included.')

REFERENCES = 'Former managers at Novo Nordisk A/S and Biofos (Lynetten) — available on request.'

PARTNER = [('Director and project management team',
  'Agree the project remit and selected roadmap deliverables. Bring problems with clear options and '
  'consequences. Use the experienced team’s knowledge and keep portfolio priorities with the '
  'appropriate decision owners.'),
 ('CMC, QA and Regulatory Affairs',
  'Ask early which quality, technical and regulatory assessments the change requires. Make those '
  'dependencies visible in the project plan. I bring regulated technical handover experience, not prior '
  'ownership of CMC or regulatory submissions.'),
 ('Artwork & Master Data, Production Planning and Commercial',
  'Clarify how the proposed change affects their inputs, decisions and implementation timing. These are '
  'intended interfaces in the role, not claimed previous functional responsibilities. Check assumptions '
  'with the people who own the process.'),
 ('Contract Manufacturers and other partners',
  'Confirm responsibilities, information needs and dependencies with the relevant Lundbeck owners. '
  'Follow unresolved issues and escalation dates. Contract-manufacturing supply chain management would '
  'be new domain experience for me.')]

FIRST90 = [('First week',
  'Agree one assigned project and a bounded roadmap contribution with the Director. Meet the sponsor, '
  'project team and receiving functions. Review scope, intended result, current plan and open '
  'decisions. Clarify the pharmaceutical supply chain learning needs and who can provide domain '
  'guidance. Record the most urgent actions and owners.'),
 ('By day 30',
  'Agree a project brief, responsibilities, milestones and acceptance criteria with the relevant '
  'functions. Establish a short risk/dependency/decision log and review cadence. Observe current '
  'project intake and portfolio reviews with the PM team. Choose one practical improvement, such as a '
  'clearer intake brief, and agree how its usefulness will be assessed.'),
 ('By day 60',
  'Drive the agreed execution plan, facilitating working sessions to resolve a specific '
  'cross-functional issue. Record options, decisions and follow-up. Test the roadmap improvement on a '
  'live case with the team. Discuss evidence and approval needs for a fit-for-purpose stage-gate pilot, '
  'using existing quality and regulatory processes.'),
 ('By day 90',
  'Review project milestones, open risks and implementation readiness with the sponsor and receiving '
  'functions. Assess whether the pilot has made intake or review decisions clearer without adding '
  'unnecessary work. Agree what to retain, change or stop. Confirm owners, documentation and the next '
  'priorities so improvements can last beyond the one-year assignment.')]

KEYWORDS = ('Cross-functional project management · Scope and milestones · Risks, dependencies and issues · '
 'Stakeholder communication · Analysis and recommendations · Implementation and handover · PDCA and A3 '
 '· Excel/Power Query · Power BI · SAP finance/assets · Python, Claude Code and Claude API. Project '
 'intake, portfolio review and stage-gate design are proposed contributions, not a claimed prior '
 'pharmaceutical PMO mandate.')


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

    for label, body in BULLETS:
        m.bullet(label, body, after=10, line=228)

    m.para(SYSTEM, after=50, line=226)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=10, line=222)

    m.meta("Yours sincerely · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFESSIONAL PROFILE")
    m.para(PROFILE, after=80)

    m.section("EXPERIENCE RELEVANT TO THE ASSIGNMENT")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("PROJECT DELIVERY AND GOVERNANCE — PROPOSED APPROACH",
                   ("Area", "Methods and tools"), MODELS)

    m.section("SELECTED ACHIEVEMENTS")
    for label, body in ACHIEVEMENTS:
        m.bullet(label, body, after=30)

    m.page_break()
    m.section("PROFESSIONAL EXPERIENCE")
    for title, meta, scope, bullets in EXPERIENCE:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=30)

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

    m.section("FROM A WORKING SESSION TO A CLEAR DECISION")
    m.para('A review should help the team decide what happens next. I would bring the project purpose, progress against milestones, unresolved dependencies and the specific decision required into one short view. For each option, show the consequence for delivery, resources and the receiving process, with the relevant specialists checking quality or regulatory implications. A gate should not turn an incomplete assessment into approval: the evidence, remaining conditions and decision authority must be explicit. Workshops should end with an agreed action, owner and date, and a later check that the action was useful. Any digital or AI support should start with a defined need, approved data access and human verification. During a temporary assignment, the tools and records should be simple enough for the team to maintain after the project manager leaves.', after=80)

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
