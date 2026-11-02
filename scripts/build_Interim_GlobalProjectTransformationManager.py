# -*- coding: utf-8 -*-
"""Interim Global Project and Transformation Manager — English combined application and CV in stored master design."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Interim Global Project and Transformation Manager | AI adoption and lean execution'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv, Denmark")
DATE = '2 November 2026'
RECIPIENT = 'Interim recruitment team · Confidential international digital services client'
SUBJECT = 'Application: Interim Global Project and Transformation Manager — 14-month assignment'

# ------------------------------------------------------------------ side 1
INTRO = ['This strategy will succeed only when four business tracks become a workable operating model in every '
 'market. A global milestone is not a local change if managers lack capacity, employees do not '
 'understand what it means for their work, or AI remains a demonstration rather than a useful daily '
 'practice. The transformation therefore needs one integrated plan and a credible employee journey, '
 'with decisions kept close to delivery.',
 'The proposed working system is ready to adapt from day one: a track charter, integrated milestone and '
 'dependency map, monthly decision pack, stakeholder-and-communication plan and adoption scorecard. The '
 'supporting track for organisational readiness, governance, change management and communication is '
 'personally owned by the Interim Leader. There is no assumption of a separate PMO organisation to '
 'build or maintain it.']

BULLETS = [('Integrate the four tracks and local market plans',
  'Work with each global track owner to agree scope, workstreams, outcomes, milestones, sequencing and decisions. '
  'Managing Directors and local track anchors validate capacity and market constraints. A dependency is '
  'recorded with both owners, its required date and the consequence of delay; conflicts become '
  'decisions, not colour changes on a slide.'),
 ('Run a lean governance cadence and the steering committee',
  'Use a short weekly track-owner check-in and a monthly operating rhythm with one integrated source of '
  'status. Prepare the steering material personally: outcomes, deviations, dependencies and decisions. '
  'Escalation papers show options, resource/budget implications and a recommendation; the CEO and '
  'steering committee decide where their mandate is required.'),
 ('Lead cultural change and internal communication',
  'Build the communication plan around what employees need to understand, try and influence. Equip '
  'managers with a short narrative, discussion guide, practical examples and answers to recurring '
  'questions. Listen through local sessions and feedback loops; use resistance to surface workload, '
  'trust or capability issues rather than labelling people as blockers.'),
 ('Turn AI adoption into changed daily work',
  'Start with selected workflows and named pilot teams, baseline current effort and quality, then test '
  'approved AI-assisted methods with human review. Measure repeat use, work quality, rework and '
  'employee confidence alongside saved time. Approved tooling, confidentiality and client commitments '
  'are prerequisites; tool access or training attendance alone is not adoption.'),
 ('Report substance to CEO, board and owners',
  'Agree the reporting definitions and decision thresholds early. A concise monthly pack separates '
  'delivered outcomes, forecast benefits, adoption evidence and unresolved risks. Show the connection '
  'between track progress and operating-model change; do not count projected savings as realised value '
  'or create a reporting layer detached from the work.'),
 ('Anchor ownership beyond the interim assignment',
  'Assign a permanent process owner and local adoption owner before scaling each change. Version the '
  'working method, record decisions and train successors through real delivery cycles. Begin handover '
  'early; the last phase tests that local leaders can run the cadence and improvement backlog without '
  'the Interim Leader.')]

SYSTEM = ('The first week establishes mandate, track owners and listening channels. By day 30, the four tracks '
 'and supporting track have a capacity-tested baseline; by day 60, one cross-market workflow pilot '
 'produces adoption evidence; by day 90, leaders decide what to scale, change or stop. Governance stays '
 'proportionate: one plan, a short action/decision log and material prepared for actual choices.')

MIRROR = ('Relevant evidence combines coordination of 25 specialists across 37 CAPEX projects, a 14-person team '
 'delivering 11 concurrent projects, and full P&L with direct people leadership in ELOHVAC. '
 'Professional Claude user and coder: Python/Claude API tools are used for estimates, planning, quality '
 'checklists and KPI reporting, with productivity improvement above 40%. That is practical AI-enabled '
 'work redesign in a small business, not proof of enterprise-wide cultural transformation.')

HONEST = ('The career spans more than 15 years in technical work, but the CV does not establish a record of '
 'leading international strategy implementation across several countries, PE-owner reporting, or '
 'cultural transformation in a digital services organisation. Operational coordination and hands-on AI '
 'development are transferable strengths; the senior transformation track-record requirement remains a '
 'substantive gap.')

CULTURE = ('The brief describes an informal, dynamic, hands-on people business. The proposed approach is to '
 'preserve that speed while making decisions and dependencies explicit: listen locally, co-design '
 'practical changes, give managers ownership and keep governance light. The confidential client has not '
 'been identified, so no company-specific values or internal tools are assumed.')

PRACTICAL = ('Based in Måløv, Greater Copenhagen. Native Danish and Persian/Farsi; professional English. The '
 '14-month commitment, start date, travel and arrangements for ELOHVAC must be agreed before '
 'appointment. Delivery is planned around the stated Q4 2026–Q4 2027 implementation window, not an '
 'invented start date.')

CLOSING = ('An initial discussion should test the required transformation track record and one immediate '
 'implementation challenge: which employee behaviour must change first, what blocks it locally, and '
 'what evidence would convince leaders that the change is taking hold?')

# ------------------------------------------------------------------ CV
PROFILE = ('The assignment requires international strategy implementation, employee commitment and lasting '
 'AI-enabled changes to how a people business sells, delivers and operates. Transferable experience is '
 'operational rather than pure strategy consulting: project coordination, direct people leadership, '
 'full P&L, practical improvement and hands-on AI tooling. B.Tech in Technology Management & Mechanical '
 'Engineering; professional Claude user and coder with Python/Claude API tools embedded in estimates, '
 'planning, quality checklists and KPI reporting. Evidence includes 37 concurrent CAPEX projects with '
 '25 specialists, 11 projects with a 14-person team and productivity improvement above 40% in ELOHVAC. '
 'These support execution and workflow redesign; they do not establish PE-backed, multi-country '
 'digital-services transformation leadership or sustained enterprise-wide cultural adoption.')

PRACTICE = [('Integrated execution — documented evidence',
  'Novo Nordisk: 37 concurrent CAPEX projects, DKK 2–10m each; progress, budget, risks and resources '
  'across engineering, procurement and site operations. Coordination of 25 specialists and zero '
  'critical findings at regulated handover.'),
 ('Hands-on team leadership — documented evidence',
  'ELOHVAC: 5 electricians and 3 apprentices, daily planning, 1:1/MUS, structured learning and full '
  'P&L. Ventek-Air: 14-person team, 11 projects, daily huddles and bottleneck analysis.'),
 ('AI-enabled workflow change — documented evidence',
  'Built Python/Claude API tools for estimates, schedules, quality checklists and KPI dashboards, with '
  'productivity improvement above 40%. This is a small-business result; no invented multinational '
  'adoption rate, sentiment score or PE value-creation result.'),
 ('Cultural change — proposed application',
  'Use local listening, manager-led discussions, skills mapping and pilot feedback to build commitment. '
  'GROW/SBI and structured learning support behaviour change; a proven digital-services cultural '
  'transformation is not established.'),
 ('Governance and stakeholder coordination — transferable practice',
  'Project risk/resource follow-up and monthly management/client reporting provide a foundation. '
  'Proposed CEO/steering committee/board reporting uses concise decision papers; PE-owner reporting is '
  'a development gap, not a previous mandate.'),
 ('Continuous improvement and technical curiosity — evidence',
  'PDCA, 5S, Standard Work, A3 and root-cause analysis in projects and critical operations. Practical '
  'coding supports dialogue with engineers; it is not a claim of leading a software studio, digital '
  'agency or product organisation.')]

MODELS = [('Integrated plan',
  'Four track charters plus the supporting track; outcomes, scope, milestones, dependencies and local '
  'capacity. Global track owners and market anchors share one baseline.'),
 ('Lean governance',
  'Weekly exception review and monthly steering committee; decision rights, RACI and short decision '
  'log. Escalations include options, recommendation and resource/budget trade-offs.'),
 ('Communication and readiness',
  'Stakeholder map, change narrative, manager discussion guide and feedback loop. Readiness checks '
  'cover skills, capacity, understanding and local support.'),
 ('AI adoption scorecard',
  'Baseline workflow effort/quality; eligible users, repeat usage and observed process change. Pair '
  'time saved with rework, output quality and employee confidence under approved data rules.'),
 ('Benefits and sentiment',
  'Name the benefit owner and measurement method; distinguish forecasts from realised results. Combine '
  'short pulse feedback with local discussion, privacy safeguards and follow-up actions.'),
 ('Lasting ownership',
  'Permanent process owner, local anchor and successor; documented decisions and working methods. '
  'Rehearse the operating rhythm without interim support before exit.')]

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

PRACTICAL_CV = 'Based in Måløv, Greater Copenhagen. Professional English, native Danish and Persian/Farsi; driving licence B. Availability for 14 months, exact mobilisation date, market travel and arrangements for ELOHVAC must be agreed. The client and intermediary are not identified in the supplied brief. No PE-owned professional services or consultancy mandate, cross-country strategy-implementation record or digital-agency employment is claimed. The assignment requires an explicit fit discussion before treating transferable project and AI experience as sufficient.'

REFERENCES = 'Former managers at Novo Nordisk A/S and Biofos (Lynetten) — available on request.'

KEYWORDS = ('Assignment remit: International transformation · Strategy implementation · Integrated plan · '
 'Milestones · Lean governance · Monthly operating rhythm · Steering committee · Communication plan · '
 'Global track owners · Managing Directors · Local track anchors · Dependencies · Organisational '
 'readiness · Change management · Cultural transformation · AI adoption · Adoption and sentiment · '
 'Senior Leadership Team · Board and owners · Operating model · Competencies · Ways of working. These '
 'describe the target mandate and proposed approach, not an asserted PE-backed multi-country '
 'transformation track record.')

# ------------------------------------------------------------ side 4
FIRST90 = [('Week 1',
  'CEO and steering committee confirm mandate, outcomes and decision rights. Meet global track owners, '
  'Managing Directors and local anchors; listen to employee concerns. Output: initial dependency map, '
  'meeting rhythm and key unresolved assumptions. No separate PMO team is presumed.'),
 ('By day 30',
  'Co-build track charters, integrated milestones and local capacity plans. Baseline the supporting '
  'track: readiness, communication, skills and adoption measures. CEO approves priorities and '
  'escalation thresholds. Prepare the first concise steering pack and manager communication toolkit.'),
 ('By day 60',
  'Pilot one approved AI-enabled workflow in agreed markets with named owners and local support. '
  'Compare effort, quality, repeat use and employee feedback with the baseline. Resolve cross-track '
  'conflicts through options and recommendations; do not force scaling before capacity and benefits are '
  'credible.'),
 ('By day 90',
  'Review adoption, sentiment, milestone evidence and realised versus forecast benefits with the CEO '
  'and steering committee. Decide what to scale, revise or stop. Permanent owners accept the next '
  'delivery cycle; agree a rolling plan for the rest of the 14-month assignment and begin successor '
  'handover.')]

PARTNER = [('CEO, steering committee, board and owners',
  'Keep the reporting decision-led: what has changed, what is off track and what needs a choice. The '
  'Interim Leader writes the material and facilitates the meeting. Significant resource, budget and '
  'priority conflicts are escalated with clear options and a recommendation.'),
 ('Global track owners',
  'Work hands-on to define scope, sequence and milestones. Keep dependencies visible and agree the '
  'minimum evidence needed to report progress. Resolve cross-track friction early without taking '
  'accountability for business outcomes away from the track owners.'),
 ('Managing Directors and local track anchors',
  'Translate global intent into feasible local plans. Protect delivery capacity, identify local '
  'constraints and agree where adaptation is justified. Equip managers to explain the change, coach '
  'employees and close feedback loops.'),
 ('Employees, engineers and delivery teams',
  'Use real workflows to make AI adoption useful rather than abstract. Listen to concerns about '
  'quality, workload, skills and client trust. Share pilot learning, explain what will and will not '
  'change, and make support accessible during the transition.')]


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

    m.section("EXECUTION AND AI EVIDENCE — TRANSFORMATION SCOPE EXPLICIT")
    for label, body in PRACTICE:
        m.bullet(label, body, after=20)

    m.models_table("PROPOSED TRANSFORMATION OPERATING FRAMEWORK",
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

    m.section("TRANSFORMATION REMIT AND EXPERIENCE BOUNDARIES")
    m.para(KEYWORDS, after=80)

    # afsluttende side
    m.page_break()
    m.models_table("FIRST 90 DAYS — MOBILISATION, READINESS AND ADOPTION",
                   ("When", "What is in place"), FIRST90)

    m.section("CUSTOMER VALUE — CROSS-FUNCTIONAL RESPONSIBILITIES")
    for label, body in PARTNER:
        m.bullet(label, body, after=20)

    m.section("MONTHS 4–14 — SCALE, EMBED AND HAND OVER")
    m.para("Months 4–8: scale only the changes supported by pilot evidence, resolve capacity conflicts and maintain manager-led communication. Track repeat use and sustained process change, not just launch activity. Months 9–12: review whether permanent owners can run the governance, maintain AI-enabled workflows and respond to employee feedback. Months 13–14: rehearse a full operating cycle without interim facilitation, close or transfer open risks and leave a prioritised improvement backlog. The CEO and steering committee accept the handover against agreed evidence; this sequence is indicative and must align with the contracted dates.", after=80)

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

    return m.save(path, title="Application and CV — Interim Global Project and Transformation Manager",
                  subject="Integrated transformation, cultural change and practical AI adoption",
                  keywords="Interim, transformation, AI, adoption, governance, execution",
                  comments="Stored master design. English. Transferable evidence and sector gaps explicit.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_Interim_GlobalProjectTransformationManager.docx")
    build(out)
    print("OK " + out)
