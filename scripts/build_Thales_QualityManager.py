# -*- coding: utf-8 -*-
"""Thales Quality Manager Lyngby — English combined application and CV in stored master design."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Quality Manager | Thales AEC Lyngby | Evidence-led assurance and controlled delivery'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv, Denmark")
DATE = '2 November 2026'
RECIPIENT = 'Thales Aerospace Communications · Lyngby · Quality hiring team'
SUBJECT = 'Application: Quality Manager — Lyngby, job 67916007'

# ------------------------------------------------------------------ side 1
INTRO = ['The Lyngby Quality System must give clients, authorities and project teams a consistent answer: which '
 'requirements apply, what evidence demonstrates compliance, and who is authorised to approve the next '
 'step? System and SW projects need timely validation without allowing schedule pressure to bypass the '
 'agreed development process. Quality ownership therefore starts with traceable decisions, clear review '
 'gates and controlled records.',
 'The proposed framework is ready to adapt to Thales’ approved processes: a Quality System '
 'applicability map, Project Quality Plan checklist, deliverable-and-validation schedule, risk/action '
 'register and audit follow-up log. It connects Lyngby with AEQ Quality and the Quality System Manager '
 'through a common evidence trail, rather than creating a separate local standard.']

BULLETS = [('Own the Quality System and align the sites',
  'Confirm document ownership, applicability, revision status and approval responsibilities with the '
  'Quality System Manager and Rungis/Troyes. Compare local practice with the approved system; record '
  'gaps, owners and closure evidence. Training must confirm understanding of changed responsibilities, '
  'not merely that a document was circulated.'),
 ('Build the Project Quality Plan into the schedule',
  'With the Project Manager, define project reviews, validation steps, required inputs and decision '
  'criteria before milestones are committed. Maintain one deliverable register for internal, client and '
  'authorities deliverables, with reviewer, approval authority and due date. Late or incomplete '
  'evidence is escalated visibly, not silently carried into the next phase.'),
 ('Assure Software Plans and software processes',
  'Review the proposed Software Plans with experienced aerospace/software specialists against customer '
  'expectations and DO-178C applicability. Audit implementation against the approved plans and retain '
  'objective evidence. Embedded systems development and certification are specialist experience gaps in '
  'this application, so this is a proposed assurance method, not a claim of prior DO-178C practice.'),
 ('Maintain risk analysis and verify corrective action',
  'Use project risk indicators, an action owner and an effectiveness check to make risk analysis a live '
  'management tool. PDCA, A3 and 5 Whys help distinguish a recurring process weakness from an isolated '
  'error. Feedback to the project group should improve the process and product without weakening '
  'approved controls.'),
 ('Validate prototypes, records and client documents',
  'Agree authorised acceptance criteria and review the completeness of evidence before validation. '
  'Confirm how prototype identity, embedded software versions, control mark and archive records are '
  'linked under Thales’ configuration rules. Quality review supports traceability; it does not '
  'substitute for engineering verification or delegated release authority.'),
 ('Provide a reliable interface to clients and authorities',
  'Maintain a single log of requests, commitments, submissions and decisions. Coordinate answers with '
  'project and technical owners and communicate unresolved questions early. The unique point of contact '
  'needs a clear mandate and escalation path, particularly while aeronautical requirements and '
  'site-specific approval rules are being learned.')]

SYSTEM = ('Week one establishes the approval boundaries and the local-to-group interfaces. By day 30, priority '
 'deliverables and system gaps have owners; by day 60, one project’s evidence trail and one process '
 'audit have been tested with the appropriate specialists. By day 90, management can review closure '
 'effectiveness and decide what to standardise. No claim of instant aerospace qualification or '
 'certification approval is made.')

MIRROR = ('Transferable evidence is regulated engineering delivery: 37 concurrent CAPEX projects of DKK 2–10m '
 'each, coordination of 25 specialists, and FAT/SAT plus IQ/OQ/PQ under GMP/FDA/EMA with zero critical '
 'findings at handover. ELOHVAC adds full P&L, quality documentation and direct people leadership. '
 'Professional Claude user and coder: Python/Claude API tools for estimates, planning, quality '
 'checklists and KPI reporting delivered productivity improvement above 40%.')

HONEST = ('The CV does not establish aerospace Quality System ownership, embedded software development '
 'assurance, DO-178C practice, or Doors, Helix and PLM experience. It also does not establish five '
 'years specifically in aerospace or a comparable regulated quality role. GMP project validation is '
 'relevant evidence, not an equivalent qualification; these gaps require an explicit discussion of the '
 'role’s entry requirements.')

CULTURE = ('Thales’ purpose, “Building a future we can all trust”, makes evidence and honest escalation central '
 'to the quality role. Its published emphasis on training, expertise sharing and an inclusive, '
 'respectful workplace supports constructive audit conversations: challenge the process, listen to the '
 'specialists and keep unresolved risks visible.')

PRACTICAL = ('Based in Måløv, with practical access to Lyngby. Professional English, native Danish and '
 'Persian/Farsi; driving licence B. Regular trips to other sites, customers and subcontractors, hybrid '
 'arrangements and the transition from ELOHVAC would be agreed before appointment.')

CLOSING = ('A useful first discussion would clarify the immediate quality priorities at Lyngby and whether the '
 'role can accommodate a regulated-engineering transition, given the aerospace and embedded-software '
 'experience it calls for.')

# ------------------------------------------------------------------ CV
PROFILE = ('Quality at Thales AEC Lyngby requires a coherent site system, effective process assurance and timely '
 'validation of project evidence. The relevant foundation is B.Tech engineering education, electrical '
 'authorisation (LV/MV/HV), regulated CAPEX delivery and disciplined technical handover. At Novo '
 'Nordisk, responsibilities covered 37 simultaneous projects, coordination of 25 specialists and '
 'FAT/SAT plus IQ/OQ/PQ under GMP/FDA/EMA, with zero critical findings at handover. Direct people '
 'leadership and full P&L come from technical contracting, not an aerospace Quality Manager '
 'appointment. Professional Claude user and coder, with Python/Claude API tools for quality checklists, '
 'planning and KPI reporting. Aerospace standards, embedded systems development assurance and '
 'requirement-management/PLM tools remain domain-learning gaps, not claimed competence.')

PRACTICE = [('Regulated validation — documented evidence',
  'Novo Nordisk: FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA with zero critical findings at handover. '
  'Evidence of controlled acceptance and documentation, not a claim of aeronautical certification '
  'experience.'),
 ('Project interfaces — documented evidence',
  '37 concurrent CAPEX projects with 25 specialists across engineering, procurement and site '
  'operations. Progress, budget, risks and resources coordinated and reported to management and '
  'client.'),
 ('Quality documentation — documented evidence',
  'ELOHVAC: quality assurance and handover records for electrical, ventilation and climate '
  'installations; zero critical deviations in service agreements. Customer commitments and '
  'subcontractor interfaces managed with full P&L.'),
 ('Audit and Quality System ownership — proposed application',
  'Use approved criteria, objective evidence, findings and action-effectiveness reviews. Site-level '
  'ownership of an aerospace Quality System and independent software-process audits are not established '
  'by the CV.'),
 ('Improvement and team development — evidence and method',
  'Daily huddles, structured apprentice training, 1:1/MUS and PDCA/5S in technical operations. Proposed '
  'quality leadership adds a skills matrix, GROW/SBI feedback and A3/5 Whys reviews with project '
  'teams.'),
 ('Digital assurance support — evidence and boundaries',
  'Python/Claude API tools improved productivity above 40% in technical contracting. Proposed use is '
  'approved checklist and report support, never unreviewed compliance decisions. Doors, Helix and PLM '
  'tools require training; proprietary engineering data stays within approved environments.')]

MODELS = [('Quality System consistency',
  'Applicability map, document owner/revision, training needs and change approval; liaison with Quality '
  'System Manager, AEQ Quality and Rungis/Troyes.'),
 ('Project Quality Plan',
  'Validation steps, project reviews, criteria, inputs, reviewer and decision authority aligned with '
  'the project schedule. One deliverable register tracks readiness.'),
 ('Process auditing',
  'Audit plan against approved Software Plans and development processes; evidence, finding, owner, due '
  'date and effectiveness check. Aerospace expertise validates the criteria.'),
 ('Risk and corrective action',
  'Risk analysis with indicators and action thresholds; PDCA/A3/5 Whys for causes and recurrence. Track '
  'risk changes and verify outcomes, not just action completion.'),
 ('Traceability and archive',
  'Confirm requirements, review evidence and configuration identity through approved requirement '
  'management and PLM tools. Preserve controlled prototype/software records under site rules.'),
 ('Client and authority interface',
  'Single request/commitment log, submission status, approved responses and escalation. Decision rights '
  'remain explicit; no assumed certification or release mandate.')]

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

PRACTICAL_CV = ('Based in Måløv, Denmark, with access to Lyngby for the local site role. Professional English, written '
 'and spoken; native Danish and Persian/Farsi. Driving licence B. Hybrid working and regular travel to '
 'Thales sites, customers and subcontractors would be agreed. Start date and arrangements for ELOHVAC '
 'settled before appointment. No aerospace/DO-178C, Doors/Helix or PLM expertise is claimed. A '
 'transition would require a supported competence plan and explicit limits on independent audit and '
 'validation authority.')

REFERENCES = 'Former managers at Novo Nordisk A/S and Biofos (Lynetten) — available on request.'

KEYWORDS = ('Target remit and learning requirements: Quality Manager · Quality System · AEQ Quality · System and '
 'SW projects · Project Quality Plan · Project reviews · Software Plans · DO-178C · Development process '
 '· Project risk indicators · Risk analysis · Prototypes · Embedded systems development · Control mark '
 '· Rungis/Troyes · Training · Auditing · Requirement management · Doors · Helix · PLM tools. EN9100, '
 'DO-178, DO-254, DO-160, DO-262 and DO-256 are standards named in the vacancy; knowledge and '
 'applicability must be established with Thales specialists, not inferred from GMP experience.')

# ------------------------------------------------------------ side 4
FIRST90 = [('Week 1',
  'Quality System Manager and site leadership agree scope, decision rights and specialist support. Meet '
  'Project Managers and software/configuration leads; review the approved quality documents. Output: '
  'authority/interface map and individual aerospace/tools learning plan, including requirements and PLM '
  'workflows.'),
 ('By day 30',
  'Map local Quality System applicability and priority deliverables with AEQ Quality and Rungis/Troyes. '
  'Review one Project Quality Plan against its schedule. Baseline overdue reviews, evidence '
  'completeness and open findings; standards and audit criteria require competent specialist '
  'confirmation.'),
 ('By day 60',
  'With an experienced assurance colleague, sample one project’s requirements-to-review trail and '
  'conduct an agreed development-process audit. Verify configuration and archive controls on a selected '
  'prototype/software record. Output: evidence-based findings, named actions and targeted training; do '
  'not imply independent certification readiness.'),
 ('By day 90',
  'Review risk indicators, overdue deliverables, action closure and effectiveness with the Quality '
  'System Manager and project leads. Test the client/authority communication log and approve any '
  'procedure changes through normal governance. Assess the remaining competence gaps before extending '
  'validation or audit authority.')]

PARTNER = [('Quality System Manager, AEQ Quality and other sites',
  'Agree what is common, which local adaptations are permitted and how changes are approved. Use '
  'regular liaison with Rungis/Troyes to resolve conflicting interpretations before they become '
  'competing versions of the process.'),
 ('Project Manager and project group',
  'Integrate review gates and evidence preparation into the schedule. Resolve ownership of missing '
  'inputs early. Feedback should improve product and process development while keeping cost, schedule '
  'and assurance decisions transparent.'),
 ('Software, systems and configuration specialists',
  'Validate standards applicability, Software Plans, requirement links, prototype identity and '
  'controlled archives with domain experts. Quality checks process conformity and evidence; engineering '
  'retains its technical accountabilities.'),
 ('Clients, authorities and subcontractors',
  'Keep a traceable record of questions, agreed responses, document submissions and outstanding '
  'decisions. Verify content with authorised owners before communicating it; escalate disagreements and '
  'do not make commitments outside the agreed mandate.')]


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

    m.section("REGULATED ENGINEERING EVIDENCE — AEROSPACE EXPERTISE NOT CLAIMED")
    for label, body in PRACTICE:
        m.bullet(label, body, after=20)

    m.models_table("PROPOSED QUALITY ASSURANCE FRAMEWORK",
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

    m.section("QUALITY REMIT AND DOMAIN-LEARNING REQUIREMENTS")
    m.para(KEYWORDS, after=80)

    # afsluttende side
    m.page_break()
    m.models_table("FIRST 90 DAYS — QUALITY BASELINE, ASSURANCE AND LEARNING",
                   ("When", "What is in place"), FIRST90)

    m.section("CUSTOMER VALUE — CROSS-FUNCTIONAL RESPONSIBILITIES")
    for label, body in PARTNER:
        m.bullet(label, body, after=20)

    m.section("PROCESS CHANGE ACCEPTANCE TEST")
    m.para("Before a procedure change is rolled out, confirm the approved requirement, document owner, affected projects and training needs. Test a sample deliverable from its requirement and revision through review evidence, approval and controlled archive. Record where traceability breaks and verify the correction on a second sample. A closed action is not automatically an effective action; check recurrence and impact on the agreed validation schedule. Independent release, certification and audit authority must follow Thales’ delegation and competence rules, not a job title alone.", after=80)

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

    return m.save(path, title="Application and CV — Thales Quality Manager Lyngby",
                  subject="Quality System consistency, project validation and evidence-led assurance",
                  keywords="Thales, quality, validation, assurance, regulated engineering",
                  comments="Stored master design. English. Transferable evidence and sector gaps explicit.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_Thales_QualityManager.docx")
    build(out)
    print("OK " + out)
