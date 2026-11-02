# -*- coding: utf-8 -*-
"""
COWI Technical Lead, Cables — English combined application/CV.
English JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Technical Lead, Cables | COWI | Electrical projects and delivery'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'

DATE = '2 November 2026'
RECIPIENT = 'COWI · Pia Alrøe, Head of Discipline'
SUBJECT = 'Application: Technical Lead, Cables — requisition 61899'

# ------------------------------------------------------------------ side 1
INTRO = ['A high-voltage cable project needs more than a completed design. Route decisions, cable ratings, '
 'procurement requirements and the construction programme have to agree, and the connection to each '
 'substation must be workable. The Technical Lead needs to keep those interfaces clear through to '
 'testing and handover on Energinet’s projects.',
 'I would start by reviewing the assigned package with the project team: what has been approved, which '
 'assumptions still need checking, and which decisions affect procurement or work on site? That review '
 'would become a short list of actions with named owners and dates, tied to the project programme '
 'rather than a separate reporting exercise.']

BULLETS = [('Keep disciplines working to the same plan',
  'Route design and horizontal directional drilling need input from the relevant electrical, civil, '
  'environmental and landowner specialists. I would bring unresolved interfaces into the planning '
  'meetings early and record the agreed decision. At Novo Nordisk, I coordinated 25 specialists across '
  'engineering, procurement and construction on 37 CAPEX projects of DKK 2–10 million each.'),
 ('Make requirements usable for procurement and construction',
  'A supply or installation package should state the technical requirements, agreed scope, interfaces, testing and '
  'documentation requirements clearly. At Ventek-Air, my work included tenders, quotations, '
  'subcontractors and delivery documentation across 11 concurrent projects. At ELOHVAC, I handle '
  'estimates, materials, planning and subcontractors with full P&L responsibility. This is transferable '
  'experience, not a claim of prior transmission-cable tender evaluation or contract negotiations.'),
 ('Follow the work through testing and handover',
  'Construction meetings should resolve the issues that prevent safe progress, with changes carried '
  'back into the agreed documentation. At Novo, I worked with FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA, '
  'with no critical findings at handover. That experience supports disciplined test coordination and '
  'quality assurance; cable-specific test requirements must be agreed with the responsible '
  'specialists.'),
 ('Be clear about the electrical scope',
  'My background includes high-voltage switchgear in critical plant operations at Biofos, electrical '
  'installation projects and Danish authorisation as an authorised electrical engineer (LV/MV/HV). It '
  'does not establish experience delivering new high-voltage cable installations. Cable ampacity '
  'design, electrical studies, route/HDD design and their standard software applications require a '
  'specific competence assessment and technical support.')]

SYSTEM = ('The final page sets out a practical first 90 days: agree the assignment and review responsibilities, '
 'check the live design and procurement interfaces, then take ownership of an agreed package. I would '
 'use COWI’s and Energinet’s approved systems and review procedures. A clear action list helps the team '
 'follow through; it does not replace checked calculations or design approval.')

MIRROR = ('The foundation is a B.Tech in Technology Management & Mechanical Engineering and experience moving '
 'electrical projects from specification to documented delivery. Alongside the Novo projects, I led a '
 '14-person team at Ventek-Air. I now lead 5 electricians and 3 apprentices at ELOHVAC, with daily '
 'planning, safety follow-up and structured training.')

HONEST = ('The key question is whether the role can use that project-delivery background while the '
 'cable-specific competence is developed and assessed. I would welcome a direct discussion of the '
 'required day-one design responsibility, including experience with establishment of high-voltage '
 'installations, before either side assumes a match.')

CULTURE = ('COWI’s emphasis on curiosity, collaboration and keeping commitments fits the way I want to work: ask '
 'before assuming, make technical uncertainty visible and close the actions agreed with colleagues and '
 'customers. I am also a professional Claude user and coder. My Python/Claude API tools have improved '
 'estimating, planning and quality follow-up productivity by over 40 % in contracting work; they are '
 'not validated cable-design tools.')

PRACTICAL = ('I live in Måløv, in Ballerup Municipality, making Ballerup the preferred assignment base. Project '
 'travel, any regular presence in Erritsø and the transition from ELOHVAC need to be agreed. I work '
 'professionally in English and am a native Danish speaker.')

CLOSING = ('I would like to discuss the first cable package you need support on, the design expertise available '
 'around it and where my electrical project and handover experience could contribute.')

# ------------------------------------------------------------------ CV
PROFILE = ('Cable delivery depends on clear technical interfaces, a realistic programme and evidence that the '
 'installed system meets the agreed requirements. My experience is in electrical project coordination, '
 'critical plant operations and documented handover. Authorised electrical engineer (LV/MV/HV), with a '
 'B.Tech in Technology Management & Mechanical Engineering. At Novo Nordisk I coordinated 25 '
 'specialists on 37 CAPEX projects; at Biofos I worked with high-voltage switchgear in a 24/7 plant. '
 'New HV cable establishment, ampacity calculations and route/HDD design are not documented experience. '
 'Professional Claude coder with practical planning and quality tools.')

PRACTICE = [('Electrical project delivery',
  'Novo: 37 simultaneous CAPEX projects of DKK 2–10 million each, coordinating 25 specialists across '
  'engineering, procurement and construction. Progress, cost, risk and resource follow-up with '
  'reporting to management and the client.'),
 ('Testing and handover',
  'FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA at Novo, with no critical findings at handover. Relevant to '
  'planning tests, closing issues and assembling quality assurance documentation; not evidence of '
  'cable-specific test competence.'),
 ('Installation planning and commercial work',
  'Ventek-Air: 11 concurrent projects and a team of 14, from specification to formal handover. Tenders, '
  'quotations, subcontractors and safety documentation. ELOHVAC adds full P&L, estimating and material '
  'planning.'),
 ('High-voltage operating environment',
  'Biofos: critical electrical and mechanical plant, including high-voltage switchgear, pumps, HVAC and '
  'SCADA. Preventive maintenance, urgent troubleshooting and LOTO. This was not transmission-cable '
  'installation delivery.'),
 ('Technical coordination and people',
  'Daily planning, 1:1 reviews, development conversations and training for 5 electricians and 3 '
  'apprentices at ELOHVAC. Cross-disciplinary coordination at Novo; the 25 specialists were not a '
  'claimed direct-report team.'),
 ('Digital support for delivery',
  'Excel/Power Query, Power BI and SAP for finance/assets. Python/Claude API tools for estimates, '
  'schedules, quality checklists and KPI follow-up: over 40 % productivity improvement in contracting, '
  'not an electrical-study result.')]

MODELS = [('Programme and interfaces',
  'Use an action list linked to the programme. Identify the owner, required decision and due date for '
  'each design, supply and construction interface.'),
 ('Design review',
  'Agree which outputs need specialist calculation, checking and approval. Route constraints, HDD '
  'crossings, cable ratings and substation bay interfaces must be resolved by competent owners.'),
 ('Construction meetings',
  'Draw on Ventek’s daily visual planning and bottleneck analysis. Bring open technical questions, '
  'safety constraints and changes to the people who can resolve them.'),
 ('Quality and handover',
  'Agree inspection, test and document requirements before work starts. Track open findings and '
  'acceptance evidence through to handover.'),
 ('Problem solving',
  'Use PDCA, A3 and 5 Whys from plant/project work on recurring issues. Confirm the cause with evidence '
  'and follow up on the corrective action.'),
 ('Responsibility and review',
  'An agreed responsibility matrix (RACI) can clarify package ownership. Use the client’s existing '
  'escalation and approval process, not a competing system.')]

ACHIEVEMENTS = [('37 CAPEX projects at Novo Nordisk',
  'DKK 2–10 million per project, with coordination of 25 specialists across engineering, procurement '
  'and construction.'),
 ('No critical findings at regulated handover',
  'FAT/SAT and IQ/OQ/PQ work under GMP/FDA/EMA at Novo Nordisk.'),
 ('11 projects and a 14-person team at Ventek-Air',
  'Capacity planning, daily visual meetings and work from specification to handover.'),
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

PRACTICAL_CV = ('Based in Måløv, Ballerup Municipality, Denmark. Ballerup is the preferred Energinet assignment base; '
 'the vacancy also identifies Erritsø. Project travel, attendance arrangements, start date and '
 'transition from ELOHVAC must be agreed. No remote-work entitlement or immediate availability assumed. '
 'Native Danish, professional English and native Persian/Farsi. Category B driving licence.')

REFERENCES = 'Former managers at Novo Nordisk A/S and Biofos (Lynetten) — available on request.'

PARTNER = [('COWI and Energinet',
  'Agree what I own, what needs specialist support and when a decision must be escalated. Keep '
  'commitments visible and raise delays while the team still has options.'),
 ('Design disciplines and substation teams',
  'Coordinate the information needed for cable routes, crossings and routing into the relevant bays. '
  'Environmental and landowner issues belong with the responsible specialists and project organisation; '
  'I do not claim prior consent-negotiation experience.'),
 ('Procurement and contractors',
  'Make technical clarifications traceable to the agreed requirements. Keep supply, installation, '
  'testing and document responsibilities clear. Tender evaluation and contract negotiations for HV '
  'cables need experienced commercial and cable specialists alongside me.'),
 ('Site and commissioning teams',
  'Use construction meetings to resolve blockers and confirm the next safe step. Coordinate factory & '
  'site testing within the agreed remit and follow outstanding findings through to accepted handover.')]

FIRST90 = [('First week',
  'Agree the assignment scope, technical authority and checking arrangements with COWI and the '
  'Energinet project lead. Review the programme and open decisions for one cable package. Meet the '
  'electrical, civil, environmental and procurement contacts. Make the cable-specific competence gaps '
  'explicit and agree a named technical reviewer.'),
 ('By day 30',
  'Trace the package from concept design and cost estimates to route, crossing and substation '
  'interfaces. Check which decisions constrain procurement or site work. Agree who owns ampacity '
  'calculations, electrical studies and design approval. Learn the approved systems and standards. '
  'Establish one current action list with owners and dates.'),
 ('By day 60',
  'Take on the agreed coordination responsibilities for a defined package. Follow procurement '
  'clarifications and construction readiness with the specialists, client and contractors. Facilitate '
  'meetings within the agreed remit and track changes back to the controlled documents. Review progress '
  'and technical learning with the designated reviewer.'),
 ('By day 90',
  'Review the package’s open technical issues, programme risks and test/handover preparation with the '
  'project lead. Check that decisions are supported by the approved design and that acceptance '
  'requirements are understood. Agree any increase in responsibility against demonstrated competence, '
  'not elapsed time alone, and set the next development priorities.')]

KEYWORDS = ('Electrical installations · Technical project delivery · Cost estimates and planning · Procurement '
 'coordination · Subcontractors · FAT/SAT · Quality assurance documentation · Handover · LOTO and risk '
 'assessment · Excel/Power Query · Python and Claude API. Cable-design software and independent HV '
 'cable design responsibility require assessment.')


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

    m.models_table("PROJECT COORDINATION AND REVIEW",
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

    m.section("TECHNICAL FOCUS")
    m.para(KEYWORDS, after=80)

    # afsluttende side
    m.page_break()
    m.models_table("FIRST 90 DAYS — SCOPE, INTERFACES AND DELIVERY",
                   ("When", "What is in place"), FIRST90)

    m.section("WORKING WITH THE PROJECT TEAM")
    for label, body in PARTNER:
        m.bullet(label, body, after=30)

    m.section("FROM DESIGN DECISIONS TO ACCEPTED HANDOVER")
    m.para('Before a package moves to procurement or construction, I would review what is actually ready with the responsible designers. Is the route current, are crossings and substation entries coordinated, and are the cable rating assumptions supported by checked studies? Are environmental and landowner constraints reflected in the programme? The supply and installation requirements should make testing, documentation and acceptance responsibilities clear. I can help coordinate that review and follow the open actions. The technical calculations and approvals must remain with competent, authorised project specialists until my own scope has been assessed. At handover, the evidence should describe the installed arrangement and close the agreed findings, not simply show that a set of forms has been completed.', after=80)

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
    build(os.path.join(ROOT, "Shahram_Ajloo_COWI_TechnicalLeadCables.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_COWI_TechnicalLeadCables.docx"))
