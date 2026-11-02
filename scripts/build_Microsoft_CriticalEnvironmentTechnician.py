# -*- coding: utf-8 -*-
"""Microsoft Critical Environment Technician — English combined application and CV in stored master design."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Critical Environment Technician | Electrical, HVAC and safe mission-critical operations'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv, Denmark")
DATE = '2 November 2026'
RECIPIENT = 'Microsoft · Cloud Operations & Innovation (CO+I) · Greater Copenhagen'
SUBJECT = 'Application: Critical Environment Technician (non shift) — job 200063265'

# ------------------------------------------------------------------ side 1
INTRO = ['Reliable datacenter operations begin before a fault becomes an outage: recognise an abnormal '
 'condition, understand the affected equipment, protect people and follow the approved route to restore '
 'service. Across three Greater Copenhagen sites, the day-role CET must combine hands-on electrical and '
 'mechanical understanding with disciplined maintenance records, safe work and clear coordination with '
 'critical facilities colleagues and vendors.',
 'The proposed day-one work structure is a site-specific equipment familiarisation map, a '
 'maintenance/work-order checklist and an abnormal-condition handover log. These would sit within '
 'Microsoft’s existing CMMS and approved procedures—not alongside them. Electrical systems are the '
 'primary discipline; HVAC, pumps and controls provide a practical foundation for understanding the '
 'interfaces that keep critical infrastructure available.']

BULLETS = [('Recognise abnormal conditions and act safely',
  'Inspect equipment, controls, HVAC, buildings and grounds against approved limits; distinguish an '
  'observation from a diagnosis. Use job hazard assessments (JHAs), environmental health and safety '
  '(EH&S) requirements, toolbox talks and safe isolation before work. LOTO and risk assessment are '
  'established practice; local access, security and switching permissions must be confirmed.'),
 ('Maintain equipment with a traceable work record',
  'Use the computerized maintenance management system (CMMS) to link equipment assets, work order '
  'requests, maintenance history and closure evidence. Plan maintenance against approved methods of '
  'procedure (MOPs) and standard operating procedures (SOPs). Capture readings, defects and follow-up; '
  'closing a work order must reflect verified equipment condition.'),
 ('Troubleshoot within the trained discipline',
  'Hands-on experience covers electrical installations, pumps, HVAC, HV switchgear and SCADA, with UPS '
  'interfaces in regulated projects. Use symptoms, drawings, operating history and authorised '
  'measurements to isolate the problem. Perform planned maintenance and corrective repairs within training; use '
  'telemetry trends to support predictive maintenance only under approved methods.'),
 ('Respond, coordinate and recover under control',
  'For onsite incidents, establish safe conditions, identify affected services and invoke the approved '
  'emergency operating procedures (EOPs). Coordinate facilities professionals and supplier/vendors with '
  'clear actions and status updates. Independent fault-finding is relevant experience; leading '
  'Microsoft incident response requires site-specific training and delegated authority, not an assumed '
  'mandate.'),
 ('Improve procedures and support colleagues',
  'Review recurring defects through PDCA, A3 and 5 Whys; propose changes through the approved review '
  'process. Share troubleshooting logic and verify understanding with less-experienced colleagues. '
  'Procedure improvements and environmental optimisation must preserve safety, redundancy and service '
  'continuity—not bypass controls to gain efficiency.')]

SYSTEM = ('Week one confirms safe access, equipment boundaries and the training/authorisation plan. By day 30, '
 'an agreed asset sample and maintenance workflow have been checked; by day 60, a maintenance cycle and '
 'approved incident exercise test the handover and escalation route. Day 90 reviews repeat defects, '
 'work-order quality and remaining competence gaps before extending independent tasks.')

MIRROR = ('The strongest operational evidence is Biofos: preventive maintenance, urgent fault-finding and '
 'spare-part flow in 24/7 critical plant covering pumps, HVAC, HV switchgear and SCADA. Novo Nordisk '
 'adds UPS/electrical interfaces, FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA with zero critical findings at '
 'handover. B.Tech education and Danish electrical authorisation (LV/MV/HV) support the technical '
 'foundation.')

HONEST = ('Direct datacenter operations, Microsoft’s internal CMMS/telemetry platforms and local EOP/MOP/SOP '
 'authorisations are not established experience. Generator maintenance competence is not claimed. The '
 'entry plan therefore validates the electrical discipline first and develops site-specific competence '
 'before broader independent duties.')

CULTURE = ('Microsoft’s growth mindset and One Microsoft culture fit practical operations: ask when uncertain, '
 'learn from near misses, share findings and help the next technician succeed. Respect, integrity and '
 'accountability mean listening to colleagues, recording the actual condition and owning follow-up—even '
 'when the safe answer is to stop and escalate.')

PRACTICAL = ('Based in Måløv; driving licence B and practical access to Greater Copenhagen. This application is for '
 'the fully onsite, non-shift individual-contributor role, including travel between sites and the '
 'stated travel below 25%. Start date and ELOHVAC arrangements must be agreed; required Microsoft Cloud '
 'background checks remain subject to the formal process.')

CLOSING = ('The first discussion can focus on the electrical maintenance scope, immediate site priorities and the '
 'competence sign-offs needed to turn critical-plant experience into safe, independent CET work.')

# ------------------------------------------------------------------ CV
PROFILE = ('Safe availability of critical infrastructure is the mission: inspect, maintain, troubleshoot and '
 'restore equipment with reliable records and controlled decisions. The foundation is B.Tech Technology '
 'Management & Mechanical Engineering, Danish electrical authorisation (LV/MV/HV), and hands-on '
 'electrical/mechanical work in critical plant and regulated pharmaceutical projects. Biofos covered '
 'pumps, HVAC, HV switchgear, SCADA, preventive maintenance and urgent fault-finding in a 24/7 '
 'operation. Novo Nordisk adds UPS interfaces and controlled FAT/SAT/IQ/OQ/PQ handover. The target is a '
 'hands-on individual-contributor day role, not a people-management appointment. Professional Claude '
 'user and coder: Python/Claude API tools improved productivity above 40% in technical contracting. '
 'Microsoft-specific platforms, datacenter topology and site authorisations require onboarding.')

PRACTICE = [('Mission-critical maintenance — documented evidence',
  'Biofos: preventive maintenance, urgent fault-finding, spare-part flow and inventory in 24/7 critical '
  'plant. Equipment included pumps, HVAC, HV switchgear and SCADA; 5S, Standard Work and PDCA supported '
  'maintenance discipline.'),
 ('Electrical troubleshooting — documented evidence',
  'ELOHVAC: installation, panels, controls, fault-finding and preventive maintenance on electrical, '
  'ventilation and climate systems. Novo Nordisk: electrical systems, UPS and emergency-lighting '
  'interfaces; no generator specialist claim.'),
 ('Safe work and controlled acceptance — evidence',
  'LOTO, workplace risk assessment and near-miss reporting in critical operations; FAT/SAT and IQ/OQ/PQ '
  'under GMP/FDA/EMA with zero critical findings at handover. Electrical authorisation does not replace '
  'Microsoft’s local work permissions.'),
 ('Coordination and practical coaching — evidence',
  'Daily work allocation and structured training for 5 electricians and 3 apprentices; 1:1/MUS and '
  'daily huddles. Experience supports vendor coordination and coaching, without implying line authority '
  'in this individual-contributor role.'),
 ('Improvement and asset information — evidence and application',
  'PDCA reduced energy costs by 40% at Novo Nordisk; SAP used for financial, asset and cost follow-up. '
  'Proposed CMMS use links equipment identity, maintenance history and work orders; Microsoft’s '
  'internal platform is a learning requirement.'),
 ('Digital support — documented evidence and limits',
  'Self-built Python/Claude API tools for estimates, plans, quality checklists and KPI reporting '
  'delivered >40% productivity improvement. In CET work, only approved environments and reviewed '
  'outputs: no external upload of site data, autonomous control or AI-generated switching '
  'instructions.')]

MODELS = [('Safe work preparation',
  'Approved JHA/EH&S and toolbox review; scope, hazards, isolation, competence and escalation. '
  'Documented LOTO/risk-assessment foundation.'),
 ('Maintenance work control',
  'CMMS asset/work-order link, approved MOP/SOP revision, authorised scope, readings, acceptance '
  'criteria and closure evidence.'),
 ('Abnormal-condition response',
  'EOP trigger and escalation, safe state, roles, event timeline and controlled recovery; apply only '
  'within approved competence and authority.'),
 ('Fault diagnosis and learning',
  'Hands-on symptoms and operating history; PDCA/A3/5 Whys for repeat defects. SCADA experience '
  'supports learning the site telemetry workflow.'),
 ('Asset and defect follow-up',
  'Equipment identity, observed condition, corrective action, owner and due date in the existing '
  'system; proposed review of repeat alarms and overdue actions.'),
 ('Knowledge transfer',
  'Documented apprentice training, huddles and 1:1/MUS; proposed teach-back and GROW/SBI feedback for '
  'clear technical coaching.')]

ACHIEVEMENTS = [('24/7 critical-plant maintenance',
  'Biofos: preventive maintenance and urgent fault-finding across pumps, HVAC, HV switchgear and SCADA, '
  'with LOTO and operational risk discipline.'),
 ('Zero critical findings at regulated handover',
  'Novo Nordisk: FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA; coordination of 25 specialists across 37 CAPEX '
  'projects.'),
 ('40% reduction in energy costs',
  'PDCA-based improvement programme at Novo Nordisk; an operational result, not a promised datacenter '
  'efficiency gain.'),
 ('Above 40% productivity improvement',
  'Self-built Python/Claude API tools for technical-contracting estimates, planning, quality checklists '
  'and KPI reporting at ELOHVAC.')]

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

PRACTICAL_CV = ('Måløv, Denmark; professional English, native Danish and Persian/Farsi; driving licence B. Fully '
 'onsite Greater Copenhagen day/non-shift individual-contributor role, with travel between three sites '
 'and stated travel below 25%. Start date and ELOHVAC transition must be agreed. Required Microsoft, '
 'customer/government screening and the Microsoft Cloud Background Check on hire/transfer and every two '
 'years thereafter are acknowledged; no clearance or guaranteed outcome is claimed. Direct datacenter '
 'experience, Microsoft CMMS/telemetry tools, generator maintenance and site switching/incident '
 'authorisations are not claimed; local competence sign-off governs independent work.')

REFERENCES = 'Former managers at Novo Nordisk A/S and Biofos (Lynetten) — available on request.'

KEYWORDS = ('Target operations remit: Critical Environment Technician · CO+I · electrical · mechanical systems · '
 'controls · HVAC · cooling systems · equipment assets · CMMS · work order requests · telemetry · '
 'planned, predictive and corrective maintenance · troubleshooting · incident response · EOPs · MOPs · '
 'SOPs · JHAs · EH&S · toolbox talks. Datacenter procedures and platforms require local training; '
 'generators are a vacancy example, not claimed maintenance expertise.')

# ------------------------------------------------------------ side 4
FIRST90 = [('Week 1',
  'Site lead confirms access/security requirements, safe-work rules, equipment scope and training '
  'authorisations across the three sites. Review electrical/mechanical interfaces, approved procedures '
  'and escalation contacts. Output: competence map, immediate safety questions and familiarisation '
  'plan; no unsupervised tasks before local approval.'),
 ('By day 30',
  'With an authorised colleague, trace selected assets from drawings and physical identity to the CMMS '
  'record, maintenance history and approved MOP/SOP. Review observed defects and spare-part '
  'dependencies. Establish work-order completeness and overdue-action baselines; verify the local '
  'JHA/toolbox process and telemetry access.'),
 ('By day 60',
  'Complete an agreed maintenance cycle within signed-off competence; review readings, acceptance '
  'evidence and return-to-service approval. Participate in an approved EOP tabletop or incident '
  'exercise with the facilities team. Output: tested escalation/handover route, documented learning and '
  'a reviewed recurring-defect improvement proposal.'),
 ('By day 90',
  'Review work-order quality, maintenance compliance, repeat defects and action closure with the site '
  'lead. Confirm cross-site handover consistency without assuming identical equipment or procedures. '
  'Demonstrate the agreed electrical troubleshooting scope, coach a colleague and agree remaining '
  'training before extending independent responsibilities.')]

PARTNER = [('Site lead and critical facilities professionals',
  'Confirm the authorised work scope, permit/isolation arrangements and escalation thresholds. Share '
  'concise status updates; independent execution remains bounded by training, approved procedures and '
  'local decision rights.'),
 ('Supplier/vendors and maintenance specialists',
  'Define work scope, safe access, interfaces and acceptance evidence before work begins. Verify the '
  'observed condition and outstanding defects after service; escalate incomplete or unsafe work rather '
  'than accepting a vendor report as proof of readiness.'),
 ('Incident responders and safety/security colleagues',
  'Use the approved EOP and incident command arrangements. Establish a shared timeline and '
  'responsibilities; preserve evidence and communicate operational impact without speculative '
  'diagnosis. Recovery and return-to-service follow delegated authority.'),
 ('Technicians across the three sites',
  'Share fault history, relevant readings, outstanding work and lessons in the approved systems. Help '
  'less-experienced colleagues understand the troubleshooting method; maintain a growth mindset without '
  'experimenting on live critical equipment.')]


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

    m.section("CRITICAL-PLANT EVIDENCE — HANDS-ON TECHNICAL OPERATIONS")
    for label, body in PRACTICE:
        m.bullet(label, body, after=20)

    m.models_table("SAFE OPERATIONS — METHODS AND WORK CONTROL",
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
    m.models_table("FIRST 90 DAYS — SAFETY, EQUIPMENT AND AUTHORISED PRACTICE",
                   ("When", "What is in place"), FIRST90)

    m.section("OPERATIONS INTERFACES — CLEAR HANDOVERS AND OWNERS")
    for label, body in PARTNER:
        m.bullet(label, body, after=20)

    m.section("MAINTENANCE COMPLETION AND PROCEDURE CHANGE CHECK")
    m.para("Before closing a maintenance work order, confirm the correct asset, approved procedure revision, actual work performed, readings and acceptance evidence. Record unresolved defects and the authorised return-to-service decision. If the observed condition differs from the procedure or expected response, stop, make safe within training and escalate; do not improvise a switching or recovery sequence. A proposed MOP/SOP/EOP change needs competent review, approval and a safe validation method before operational use. Test lessons through approved exercises or controlled work, not experimentation on live equipment. Use repeat-defect and near-miss reviews to improve reliability while preserving local safety and security controls.", after=80)

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

    return m.save(path, title="Application and CV — Microsoft Critical Environment Technician, job 200063265",
                  subject="Safe mission-critical maintenance, troubleshooting and controlled recovery",
                  keywords="Microsoft, CET, CO+I, electrical, HVAC, maintenance, critical infrastructure",
                  comments="Stored master design. English. Transferable evidence and sector gaps explicit.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_Microsoft_CriticalEnvironmentTechnician.docx")
    build(out)
    print("OK " + out)
