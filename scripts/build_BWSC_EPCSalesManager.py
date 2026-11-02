# -*- coding: utf-8 -*-
"""BWSC EPC Sales Manager — English combined application and CV in stored master design."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'EPC Sales Manager | BWSC | From qualified opportunity to executable contract'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv, Denmark")
DATE = '2 November 2026'
RECIPIENT = 'BWSC · Att: Zaid Younis, Director of EPC Sales'
SUBJECT = 'Application: EPC Sales Manager'

# ------------------------------------------------------------------ side 1
INTRO = ['BWSC’s return to engine-based EPC must win projects that remain profitable through execution and '
 'operation. A compelling offer is only the beginning: customer needs, project readiness, supplier '
 'commitments and contractual exposure must align before a commercial promise becomes a delivery '
 'obligation. The opportunity is to use BWSC’s full lifecycle knowledge to sell reliable power, '
 'not simply installed capacity.',
 'The proposed commercial process is ready to be adapted to BWSC’s governance: an opportunity '
 'qualification sheet, bid/no-bid gate, proposal responsibility matrix, commercial risk register '
 'and award-to-execution checklist. One evidence trail connects early project development to '
 'tendering, negotiation and contract award.']

BULLETS = [('Identify and progress EPC and O&M opportunities',
  'Map selected markets, customers, partners and suppliers with the Director of EPC Sales. Qualify '
  'need, decision-makers, procurement route, funding status, site readiness and timing. Each '
  'pursuit has a next decision, evidence owner and stop condition; a large pipeline is not the '
  'same as a credible one.'),
 ('Shape winning bids and competitive proposals',
  'Agree project strategy and commercial positioning before mobilising the proposal teams. Use a '
  'compliance matrix and RACI to connect engineering, procurement, O&M, finance and legal. Review '
  'scope, interfaces, assumptions, exclusions and delivery capacity together, so a competitive '
  'proposal is also executable.'),
 ('Protect commercial, contractual and financial value',
  'Build a cost and cash-flow bridge with supplier quote validity, contingency, payment milestones '
  'and sensitivities. Legal and finance validate securities, liability, performance guarantees and '
  'approval limits. A negotiation brief sets objectives, alternatives and concession exchanges; '
  'unresolved exposure is escalated, not hidden in price.'),
 ('Turn lifecycle experience into customer value',
  'Bring service, operation and maintenance specialists into project development early. Test '
  'maintainability, spares, training, operating assumptions and acceptance criteria against the '
  'proposed plant scope. Any availability, efficiency or emissions commitment needs technical '
  'validation and a clear contractual measurement basis.'),
 ('Convert opportunities into awarded projects',
  'Maintain a decision-led customer dialogue and stakeholder map, including local partners and '
  'critical suppliers. Keep cross-functional teams aligned through concise pursuit reviews and '
  'action logs. After award, hand over the signed scope, deviations, guarantees, cash-flow '
  'assumptions and customer commitments to project execution.'),
 ('Build a repeatable Commercial organization',
  'Review stage progression, bid effort, win/loss reasons, margin and cash exposure with senior '
  'management. Use consistent templates and lessons learned, not a parallel reporting system. '
  'Python and Claude can support research, proposal consistency and scenario analysis under '
  'approved data rules; people remain accountable for every commitment.')]

SYSTEM = ('The first week establishes the pursuit baseline and approval boundaries. By day 30, priority '
 'opportunities have evidence-based qualification; by day 60, one live pursuit has an integrated '
 'bid plan; by day 90, the team has tested the commercial reviews and handover package. Measures '
 'distinguish activity from qualified progression and awarded business. No unsupported promise of '
 'a major EPC win within 90 days.')

MIRROR = ('Relevant evidence combines full P&L and quotation responsibility in ELOHVAC, 37 concurrent CAPEX '
 'projects of DKK 2–10m each with coordination of 25 specialists, and 11 installation projects '
 'with a 14-person team. Professional Claude user and coder: Python/Claude API tools for '
 'estimates, schedules, quality checklists and KPI reporting have delivered a productivity '
 'improvement above 40%.')

HONEST = ('The CV does not establish a proven track record of securing international turnkey EPC '
 'power-plant contracts or a separate financial degree. The offer is B.Tech engineering education, '
 'practical commercial ownership and delivery discipline; the EPC-sales track-record requirement '
 'remains a genuine gap to discuss, not a claimed credential.')

CULTURE = ('BWSC’s trustworthiness, credibility and integrity translate into transparent risk ownership and '
 'commitments the delivery team can honour. Its published lifecycle strategy makes O&M expertise '
 'part of the sales proposition. Open knowledge sharing and cross-cultural collaboration should '
 'improve the bid before it reaches the customer.')

PRACTICAL = ('Based in Måløv, with a practical commute to Allerød. Professional English, native Danish and '
 'Persian/Farsi. Regular international travel and arrangements for the existing business would be '
 'agreed before appointment. Application submission is through BWSC’s online recruitment system, '
 'not email.')

CLOSING = ('A useful first discussion would test one priority pursuit: what must be true for BWSC to bid, '
 'what makes the offer distinctive, and which risks must be resolved before signature?')

# ------------------------------------------------------------------ CV
PROFILE = ('BWSC’s EPC sales mission is to turn qualified demand into profitable, executable engine-based '
 'power-plant contracts. The transferable foundation is technical contracting with full P&L, '
 'quotations, customer delivery, procurement interfaces and disciplined handover. Authorised '
 'electrical engineer (LV/MV/HV), B.Tech in Technology Management & Mechanical Engineering, with '
 'leadership across regulated CAPEX delivery and critical operations. Professional Claude user and '
 'coder, building Python/Claude API tools for estimates, planning and KPI reporting. The intended '
 'contribution is practical commercial understanding grounded in how technical commitments are '
 'delivered. International EPC sales wins and a separate financial qualification are not '
 'established by this CV.')

PRACTICE = [('Commercial ownership — evidence',
  'ELOHVAC: full P&L, quotations, calculations, material planning, subcontractors, quality '
  'assurance and customer handover. Direct accountability for technical contracting, without '
  'presenting it as utility-scale EPC contract award experience.'),
 ('Cross-functional coordination — evidence',
  '37 concurrent CAPEX projects with 25 specialists across engineering, procurement and site '
  'operations. Progress, budget, risks and resources reported to management and client; zero '
  'critical findings at regulated handover.'),
 ('Proposal leadership — evidence and application',
  'Ventek-Air: tenders, quotations, subcontractor coordination and specification-to-handover '
  'delivery across 11 projects. Proposed EPC application: compliance matrix, RACI, review gates '
  'and a single assumptions register.'),
 ('Analytical and strategic skills — proposed commercial use',
  'Prioritise accessible opportunities and test cost, cash and risk sensitivities before '
  'committing bid resources. Maintain visible distinctions between customer evidence, assumptions '
  'and decisions. SAP ERP experience supports financial and asset follow-up.'),
 ('Communication, negotiation and stakeholder management — application',
  'Technical customer dialogue and delivery coordination provide a practical foundation. Use '
  'stakeholder maps, decision logs and negotiation briefs with legal and finance; international '
  'EPC negotiations are a development area, not a proven sales record.'),
 ('Leadership and digital improvement — evidence',
  'Led 5 electricians and 3 apprentices, a 14-person installation team and a 12-person workshop '
  'team in different roles. Daily huddles, 1:1/MUS, 5S and PDCA support follow-through. '
  'Python/Claude API tools improved productivity above 40%.')]

MODELS = [('Opportunity qualification',
  'Customer problem, selected market, stakeholders, funding/procurement route, project readiness '
  'and next decision; Director-approved bid/no-bid gate.'),
 ('Bid and proposal governance',
  'RACI, compliance matrix, responsibility schedule, supplier inputs and staged '
  'technical/commercial reviews. One version of scope and assumptions.'),
 ('Commercial risk and finance',
  'Cost bridge, cash-flow scenarios, contingencies, quote validity and approval thresholds. '
  'Legal/finance own validation of guarantees, liability and securities.'),
 ('Customer and partner dialogue',
  'Stakeholder map, value case, decision process and negotiation brief. Clear commitments and '
  'written clarification of deviations.'),
 ('Contract-to-execution handover',
  'Signed scope, exclusions, interfaces, commercial assumptions, key dates, guarantees and risk '
  'owners; joint review with execution and O&M.'),
 ('Team and improvement cadence',
  'Weekly pursuit review, named actions and monthly portfolio decisions. GROW/SBI for coaching, '
  'PDCA/A3 for lessons learned; proposed methods, not claimed BWSC standards.')]

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

PRACTICAL_CV = ('Based in Måløv, Denmark; Allerød is a practical work location. Professional proficiency in '
 'English, written and spoken; native Danish and Persian/Farsi. Driving licence B. Regular travel '
 'activity, start date and arrangements for ELOHVAC would be agreed before appointment. No age, '
 'photograph or unnecessary personal data included. Submit only via BWSC’s online recruitment '
 'system; Zaid Younis (zayo@bwsc.dk) is the contact for questions, not an email application route.')

REFERENCES = 'Former managers at Novo Nordisk A/S and Biofos (Lynetten) — available on request.'

KEYWORDS = ('Target role: Business development · EPC projects · Engine-based power plants · O&M opportunities '
 '· Lead generation · Project development · Tendering · Bid and proposal activities · Commercial '
 'positioning · Contract award · Profitable growth · Customers, partners and suppliers · '
 'Cross-functional teams · Project execution · International markets. These describe the target '
 'remit and proposed operating model, not a claimed international EPC sales portfolio.')

# ------------------------------------------------------------ side 4
FIRST90 = [('Week 1',
  'Director of EPC Sales: agree selected markets, decision rights, existing systems and '
  'confidentiality rules. Review current pursuits with proposal, engineering, O&M, legal and '
  'finance leads. Output: baseline pipeline and unresolved questions, not an imposed new process.'),
 ('By day 30',
  'Qualify agreed priority opportunities through customer conversations and internal evidence '
  'checks. Complete stakeholder maps, readiness/funding questions and initial risk screens. '
  'Director approves pursue/hold/stop decisions. Measures: qualification completeness, stage '
  'evidence and next-decision clarity.'),
 ('By day 60',
  'Pilot an integrated bid plan on one suitable live pursuit. Proposal lead owns deliverables; '
  'engineering and suppliers validate scope/cost; finance/legal validate cash, terms and exposure. '
  'Output: reviewed compliance matrix, value case and negotiation boundaries; record unresolved '
  'issues.'),
 ('By day 90',
  'Review customer feedback, pursuit progression, bid effort and risk closure with the Director. '
  'Test the award-to-execution checklist against a live or previous contract. Agree improvements '
  'and realistic commercial targets; report awards only when secured, separately from pipeline '
  'progress.')]

PARTNER = [('Director of EPC Sales and senior management',
  'Own market priorities, bid/no-bid approvals and commercial mandate. Bring concise decision '
  'papers showing customer evidence, alternatives, risk and cash implications; escalate before '
  'approval limits are crossed.'),
 ('Customers, local partners and suppliers',
  'Build relationships through credible technical questions, reliable follow-up and respect for '
  'different cultures. Clarify who decides, who funds and who delivers. Do not assume an existing '
  'international developer network.'),
 ('Proposal teams and technical specialists',
  'Use the compliance matrix to connect customer requirements to engine selection, '
  'balance-of-plant interfaces, commissioning and validated performance assumptions. The sales '
  'role coordinates expertise rather than substitutes for it.'),
 ('Legal, finance, O&M and project execution',
  'Resolve material terms and lifecycle obligations before signature. Execution accepts the '
  'commercial handover, including exclusions, guarantees, supplier commitments and open actions; '
  'O&M tests the operability of the promise.')]


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

    m.section("TRANSFERABLE EVIDENCE — AND THE PROPOSED COMMERCIAL APPROACH")
    for label, body in PRACTICE:
        m.bullet(label, body, after=20)

    m.models_table("PROPOSED COMMERCIAL OPERATING MODEL",
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

    m.section("TARGET EPC COMMERCIAL REMIT")
    m.para(KEYWORDS, after=80)

    # afsluttende side
    m.page_break()
    m.models_table("FIRST 90 DAYS — PURSUIT GOVERNANCE AND DELIVERABLES",
                   ("When", "What is in place"), FIRST90)

    m.section("CUSTOMER VALUE — CROSS-FUNCTIONAL RESPONSIBILITIES")
    for label, body in PARTNER:
        m.bullet(label, body, after=20)

    m.section("HANDOVER ACCEPTANCE TEST")
    m.para("Before a pursuit is treated as execution-ready, the receiving project manager should be able to trace each material customer commitment to the signed contract, an approved cost assumption and a named delivery owner. Test the checklist on a previous project first; unresolved items stay visible in the risk register with an agreed decision route.", after=80)

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

    return m.save(path, title="Application and CV — BWSC EPC Sales Manager",
                  subject="EPC opportunity development, bid governance and commercial handover",
                  keywords="BWSC, EPC, O&M, business development, proposals, negotiation",
                  comments="Stored master design. English. Transferable evidence and sector gaps explicit.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_BWSC_EPCSalesManager.docx")
    build(out)
    print("OK " + out)
