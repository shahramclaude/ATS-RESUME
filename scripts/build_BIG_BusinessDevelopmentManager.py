# -*- coding: utf-8 -*-
"""BIG Business Development Manager — English combined application and CV in stored master design."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Business Development Manager | BIG Copenhagen | Qualified pipeline and credible proposals'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv, Denmark")
DATE = '2 November 2026'
RECIPIENT = 'BIG – Bjarke Ingels Group · Business Development Director · Copenhagen'
SUBJECT = 'Application: Business Development Manager — Europe and Australasia'

# ------------------------------------------------------------------ side 1
INTRO = ['A diverse project pipeline is only valuable when opportunities fit BIG’s design ambition, client '
 'needs and commercial capacity. Across Europe and Australasia, business development must connect '
 'market intelligence and relationships to a clear acquisition decision: why this project, why this '
 'team and what will make the proposal credible?',
 'The proposed day-one structure is an opportunity scorecard, a pursuit calendar, a '
 'client-and-consultant relationship map and a submission compliance matrix. These would be adapted to '
 'BIG’s existing CRM and review routines, giving Partners a concise view of strategic fit, next '
 'decisions, resources and commercial exposure—not a parallel reporting system.']

BULLETS = [('Qualify the right opportunities',
  'Assess client objectives, funding/procurement route, regional relevance, design potential, team '
  'capacity and competitive position. Separate researched evidence from assumptions; recommend pursue, '
  'hold or decline with a named next action. Go-to-market strategies should reflect specific client and '
  'consultant relationships, not just a country list.'),
 ('Lead teaming and submission production',
  'For PQ/RFQs/RFPs/RFIs, map eligibility, evaluation criteria, references, consultant roles, deadlines '
  'and approvals before production. Agree responsibilities with Partners and Associates; use a '
  'compliance matrix and version-controlled evidence. InDesign production requires a supported learning '
  'plan, not an unsupported superuser claim.'),
 ('Convert approaches into direct commissions',
  'Build a client-specific pitch around the problem, a relevant BIG project and the proposed team’s '
  'contribution. Prepare client visits with a shared brief and capture decisions and follow-up. '
  'Participation in conferences, lectures and events should have a relationship objective and an accountable '
  'next step.'),
 ('Protect the commercial proposition',
  'Prepare fee proposals from scope, deliverables, programme, resources, assumptions and exclusions. '
  'Review contracts and negotiation positions with the Director of Bidding & Project Commercials and '
  'Legal. Technical contracting and full P&L provide a commercial foundation, not a record of '
  'negotiating international architectural appointments.'),
 ('Keep relationships and pipeline actionable',
  'Maintain CRM ownership, opportunity stage, source, expected decision and next contact. Provide '
  'regular status updates for Partners and MD, highlighting decisions rather than activity totals. '
  'Coordinate marketing material with Communications; use approved AI support for research synthesis '
  'and checks, never invented references or unreviewed client claims.')]

SYSTEM = ('Week one aligns priorities and decision rights with the Business Development Director. By day 30, a '
 'first market shortlist and submission baseline are reviewed; by day 60, a live pursuit and client '
 'follow-up cycle have been tested. Day 90 reviews conversion, effort and learning before scaling. '
 'Targets must follow the actual pipeline baseline, not invented win-rate promises.')

MIRROR = ('Relevant evidence comes from building-services contracting: ELOHVAC combines customer dialogue, '
 'estimates, materials, subcontractors and full P&L; Ventek-Air adds tenders and quotations across 11 '
 'concurrent projects with 14 staff. Novo Nordisk adds coordination of 25 specialists across 37 CAPEX '
 'projects. Python/Claude API tools for estimates, planning and KPI reporting improved productivity '
 'above 40%.')

HONEST = ('The degree is B.Tech in Technology Management & Mechanical Engineering, not architecture. '
 'Architectural business development across Europe/Australasia, InDesign superuser proficiency, Adobe '
 'Creative Cloud and hands-on CRM/CMS experience are not documented; technical contracting does not '
 'establish the requested 3–5 years in a similar architecture-sector role.')

CULTURE = ('BIG describes broad idea generation followed by rigorous selection, and a multidisciplinary BIG LEAP '
 'approach. Applied here: invite design, engineering and commercial perspectives early, then select '
 'pursuits on evidence. A diverse team needs shared criteria and clear ownership without closing down '
 'ideas prematurely.')

PRACTICAL = ('Based in Måløv, with access to BIG HQ in Copenhagen. Professional English and native Danish/Persian; '
 'no German proficiency claimed. The preferred 1 December 2026 start and arrangements for ELOHVAC would '
 'need agreement.')

CLOSING = ('A first conversation should test whether technical-commercial building-industry experience can '
 'complement this team, and whether the role can accommodate the architecture-market and '
 'production-tool learning curve.')

# ------------------------------------------------------------------ CV
PROFILE = ('The mission is to turn market intelligence, client relationships and strong teaming into a qualified '
 'project pipeline for BIG across Europe and Australasia. The transferable foundation is '
 'technical-commercial work in the building industry: customer dialogue, estimates, tenders, '
 'subcontractor coordination and full P&L at ELOHVAC and Ventek-Air. Novo Nordisk adds '
 'multidisciplinary coordination of 25 specialists across 37 simultaneous CAPEX projects. B.Tech '
 'engineering education and electrical authorisation support technical understanding, not architectural '
 'design credentials. Professional Claude user and coder: Python/Claude API tools for estimates, '
 'planning and KPI reporting delivered productivity improvement above 40%. International architectural '
 'acquisitions, InDesign superuser proficiency and CRM/CMS practice are learning gaps, not claimed '
 'experience.')

PRACTICE = [('Client and commercial interfaces — evidence',
  'ELOHVAC: customer dialogue, estimates, materials, subcontractors and delivery with full P&L. A '
  'foundation for scope clarity and commercial follow-through, not a claimed network of international '
  'developer clients.'),
 ('Tenders and quotations — evidence',
  'Ventek-Air: specification-to-handover work, tenders and quotations across 11 concurrent projects and '
  'a 14-person team. Architectural prequalifications and competition submissions are a different '
  'production context.'),
 ('Multidisciplinary coordination — evidence',
  'Novo Nordisk: 37 CAPEX projects, DKK 2–10m each, and coordination of 25 specialists across '
  'engineering, procurement and site operations; progress, budgets, risks and resources reported to '
  'management and client.'),
 ('Leadership and collaboration — evidence and method',
  'Direct leadership of 5 electricians and 3 apprentices; daily huddles, structured training and '
  '1:1/MUS. Proposed pursuit coordination uses a responsibility matrix, short reviews and explicit '
  'decision ownership rather than implied authority over Partners.'),
 ('AI and research support — evidence and boundaries',
  'Python/Claude API tools delivered >40% productivity improvement in technical contracting. Proposed '
  'market research keeps sources, dates and uncertainty visible. Client data and unpublished project '
  'material stay within approved environments.'),
 ('Architecture-sector tools — learning requirements',
  'Adobe Creative Cloud, InDesign superuser capability, Microsoft Suite workflows and CRM systems must '
  'be assessed against BIG’s requirements. CMS Client Management Software is a stated plus, not a '
  'documented qualification here.')]

MODELS = [('Opportunity scorecard',
  'Strategic fit, client need, route to commission, team capability, capacity and commercial risk; '
  'Partner-approved pursue/hold/decline recommendation.'),
 ('Pursuit compliance matrix',
  'PQ/RFQs/RFPs/RFIs criteria, required references, consultant inputs, owners, review dates and '
  'approved final issue.'),
 ('Relationship and CRM cadence',
  'Named relationship owner, last discussion, next action and decision stage; weekly exceptions and '
  'regular Partner/MD status updates.'),
 ('Fee and contract review',
  'Scope-to-resource assumptions, deliverables, exclusions and approval route with commercial '
  'leadership and Legal before negotiation commitments.'),
 ('Evidence-based improvement',
  'PDCA from technical operations; proposed pursuit retrospectives compare effort, feedback and stage '
  'progression without claiming an established BIG method.'),
 ('Inclusive team coordination',
  'Documented huddles and 1:1/MUS; proposed RACI, GROW/SBI feedback and clear review gates support '
  'specialist contributions and timely decisions.')]

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

PRACTICAL_CV = ('Based in Måløv, Denmark; full-time Copenhagen HQ role. English professional, written and spoken; '
 'Danish and Persian/Farsi native. German is not claimed. B.Tech is an engineering qualification, not '
 'an architecture degree. Availability for the preferred 1 December 2026 start, travel and transition '
 'from ELOHVAC must be agreed. No established Europe/Australasia architecture-client network, InDesign '
 'superuser or CRM/CMS expertise is claimed; entry expectations and support need an explicit fit '
 'discussion.')

REFERENCES = 'Former managers at Novo Nordisk A/S and Biofos (Lynetten) — available on request.'

KEYWORDS = ('Target remit: Business Development Manager · direct acquisitions · prequalifications · direct '
 'commissions · client relations · consultant relations · fee proposals · contracts · market research · '
 'marketing material · CRM databases. Europe and Australasia are the target markets, not a claimed '
 'existing network. Architecture-sector acquisition experience, Adobe Creative Cloud/InDesign and '
 'CRM/CMS production capability require explicit assessment and support.')

# ------------------------------------------------------------ side 4
FIRST90 = [('Week 1',
  'Business Development Director confirms priority markets, live pursuits and decision rights. Meet '
  'Partners, Associates, MD, Bidding & Project Commercials, Communications and Legal. Review CRM '
  'stages, proposal templates and approval routes. Output: stakeholder map, immediate deadline list and '
  'InDesign/CRM learning assessment.'),
 ('By day 30',
  'Produce an evidence-linked shortlist for one agreed European and one Australasia market segment. Map '
  'relevant clients and consultants; review opportunity fit with the responsible Partner. Baseline '
  'submission completeness, overdue next actions and stage definitions. Calibrate research criteria '
  'against BIG’s existing strategy.'),
 ('By day 60',
  'Coordinate an agreed live pursuit with experienced architecture-BD and production support. Test the '
  'compliance matrix, teaming responsibilities and fee-review route. Prepare client visits or pitches '
  'and record the agreed follow-up. Output: reviewed submission or pitch, current CRM record and '
  'lessons from actual feedback.'),
 ('By day 90',
  'Review qualified opportunities, stage progression, proposal effort, on-time submissions and '
  'relationship follow-through with the Director. Separate won/lost decisions from opportunities still '
  'pending. Recommend where to concentrate or stop effort; agree remaining competence development '
  'before extending independent production responsibility.')]

PARTNER = [('Business Development Director, Partners and MD',
  'Directors align priorities; Partners validate strategic and design fit and lead relationships where '
  'appropriate. Provide concise recommendations and explicit decisions needed. Regular updates should '
  'make the pipeline usable, not increase reporting burden.'),
 ('Associates and consultant teams',
  'Agree relevant references, team composition, responsibilities and capacity before promising a '
  'response. Give specialists an early chance to challenge the brief; freeze the approved proposition '
  'before final production.'),
 ('Bidding & Project Commercials and Legal',
  'Validate scope, fee assumptions, contractual exposure and negotiation authority. Flag liability, '
  'intellectual property, payment and programme issues for qualified review rather than accepting them '
  'to keep a pursuit moving.'),
 ('Communications, clients and external network',
  'Align marketing material and project narratives with approved facts and image rights. Host visits '
  'around client interests and meaningful dialogue. Represent BIG at agreed events, capture relevant '
  'connections and assign prompt follow-up.')]


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

    m.section("BUILDING-INDUSTRY EVIDENCE — COMMERCIAL AND TEAM COORDINATION")
    for label, body in PRACTICE:
        m.bullet(label, body, after=20)

    m.models_table("PROPOSED PURSUIT AND RELATIONSHIP FRAMEWORK",
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

    m.section("TARGET REMIT AND LEARNING REQUIREMENTS")
    m.para(KEYWORDS, after=80)

    # afsluttende side
    m.page_break()
    m.models_table("FIRST 90 DAYS — PIPELINE, PURSUITS AND RELATIONSHIPS",
                   ("When", "What is in place"), FIRST90)

    m.section("PARTNERSHIP MODEL — SHARED DECISIONS, CLEAR OWNERS")
    for label, body in PARTNER:
        m.bullet(label, body, after=20)

    m.section("SUBMISSION AND PIPELINE QUALITY CHECK")
    m.para("Before issuing a submission, confirm eligibility and evaluation criteria, authorised project references, consultant commitments and the correct version of fee and scope assumptions. Check names, figures, image rights and mandatory attachments against the compliance matrix. Obtain design, commercial and Legal approvals where required, then record the issued version and next client decision in CRM. For research, retain the original source and distinguish a verified procurement notice from a speculative lead. AI can accelerate draft review; it must not invent awards, project credits or client statements. A complete submission is not automatically a competitive one: record evaluator feedback and use it to improve the next pursuit.", after=80)

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

    return m.save(path, title="Application and CV — BIG Business Development Manager",
                  subject="Qualified pipeline, client relationships and disciplined proposal production",
                  keywords="BIG, business development, proposals, client relations, building industry",
                  comments="Stored master design. English. Transferable evidence and sector gaps explicit.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_BIG_BusinessDevelopmentManager.docx")
    build(out)
    print("OK " + out)
