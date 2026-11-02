# -*- coding: utf-8 -*-
"""
Danfoss Drives NPI & Industrialization — English combined application/CV.
English JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'S/C Project Manager | Danfoss Drives | NPI & Industrialization'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'

DATE = '3 November 2026'
RECIPIENT = 'Danfoss Drives · Supply Chain Technology Center, Gråsten'
SUBJECT = 'Application: S/C Project Manager – NPI & Industrialization | req. 52586'

# ------------------------------------------------------------------ side 1
INTRO = ['A new drive is ready for launch when the manufacturing process, materials and people are ready as '
 'well as the product design. The project manager needs to bring those pieces together early enough to '
 'resolve problems before they become production delays. At Danfoss Drives, that means a shared plan '
 'across R&D, Product Management, Manufacturing Engineering, Procurement, Quality and Operations, with '
 'clear decisions at each stage.',
 'I would start with the project already in motion: what is committed for launch, which requirements '
 'remain open, and what evidence will Operations need before accepting the handover? The aim would be a '
 'practical readiness plan with named owners and milestones, using Danfoss’s existing processes rather '
 'than adding a parallel reporting system.']

BULLETS = [('Bring the functions to a common decision',
  'A milestone is useful only if the people delivering it agree on the dependencies and know what has '
  'to be decided. At Novo Nordisk, I coordinated 25 specialists across engineering, procurement and '
  'construction on 37 CAPEX projects of DKK 2–10 million each. That work involved following progress, '
  'costs and risks and bringing unresolved issues to management and the client. It is the strongest '
  'basis for my contribution to cross-functional execution at Danfoss.'),
 ('Make readiness visible before handover',
  'I would work with the functional owners to define what must be ready: materials, process '
  'documentation, equipment, quality evidence and trained operators. My experience with FAT/SAT and '
  'IQ/OQ/PQ under GMP/FDA/EMA at Novo taught me to follow the evidence through to acceptance. Those '
  'projects had no critical findings at handover. Danfoss’s product-launch criteria will be different '
  'and need to be learned with the team.'),
 ('Connect the schedule to the work on the floor',
  'A project plan should reflect the real capacity and constraints of the people doing the work. At '
  'Ventek-Air, I led a 14-person team across 11 concurrent projects from specification to formal '
  'handover, using daily visual planning and bottleneck analysis. Earlier, I led 12 mechanics and '
  'technicians in a repair workshop. I would bring that practical view into discussions about '
  'manufacturing readiness and changes to production setups.'),
 ('Keep changes and priorities under control',
  'When a product or component changes, the team needs to understand the effect on materials, process, '
  'cost and timing before committing to the next step. I would make those dependencies visible and ask '
  'the relevant owners to agree the response. My present ELOHVAC role combines estimates, material '
  'planning, subcontractors and full P&L responsibility, so I am used to following both the technical '
  'work and its commercial consequences.')]

SYSTEM = ('The first 90 days on the final page are built around one assigned project: agree ownership and '
 'acceptance criteria, establish the current readiness position, then resolve a specific obstacle with '
 'the functional team. I would keep a short record of risks, decisions and next actions, tied to the '
 'agreed milestones and escalated when a decision is outside the team’s remit.')

MIRROR = ('My technical foundation is a B.Tech in Technology Management & Mechanical Engineering and Danish '
 'authorisation as an authorised electrical engineer (LV/MV/HV). My background combines technical '
 'project delivery, workshop leadership and critical plant operations. It gives me a practical '
 'understanding of how engineering choices, material availability, maintenance and daily work affect '
 'one another.')

HONEST = ('I have not led a documented drive-product NPI programme or a full industrialization launch across '
 'global manufacturing sites. Agile and Scrum delivery experience is also not documented. The relevant '
 'starting point is my industrial project leadership and regulated handover experience, with a clear '
 'learning plan for Danfoss’s product, manufacturing and launch processes.')

CULTURE = ('Danfoss’s “Frontline passion” and “Run the business like your own” make sense to me as working '
 'habits: listen to the people closest to the process, take responsibility for the next step and keep '
 'cost and quality in view. I am also a professional Claude user and coder. My Python/Claude API tools '
 'for estimates, planning, quality checklists and KPI follow-up have improved productivity by over 40 % '
 'in contracting. Any use at Danfoss would need to fit approved systems, data rules and a real '
 'operational need.')

PRACTICAL = ('I live in Måløv. This is an on-site role in Gråsten, so a sustainable attendance or relocation '
 'arrangement and the transition from ELOHVAC would need to be agreed. I work professionally in English '
 'and am a native Danish speaker.')

CLOSING = ('I would welcome a discussion about the next launch the Technology Center needs to prepare for, and '
 'where the project most needs someone to bring people and decisions together.')

# ------------------------------------------------------------------ CV
PROFILE = ('New Product Introduction needs an agreed path from product development to production and handover to '
 'Operations. My experience is in technical project coordination, workshop leadership and regulated '
 'commissioning. At Novo Nordisk I coordinated 25 specialists on 37 CAPEX projects; at Ventek-Air I led '
 'a team of 14 across 11 projects. B.Tech in Technology Management & Mechanical Engineering and '
 'authorised electrical engineer (LV/MV/HV). Direct drive-product NPI and global industrialization '
 'leadership would be new responsibilities. Professional Claude coder with practical tools for planning '
 'and quality follow-up.')

PRACTICE = [('Cross-functional project execution',
  'Novo: coordination of 25 specialists across engineering, procurement and construction on 37 CAPEX '
  'projects of DKK 2–10 million each. Follow-up on progress, cost, risks and resources, with reporting '
  'to management and the client.'),
 ('Readiness and acceptance evidence',
  'FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA at Novo, with no critical findings at handover. Experience '
  'establishing whether technical work is ready for acceptance and following open issues through to '
  'closure.'),
 ('Capacity and delivery planning',
  'Ventek-Air: 11 concurrent projects and a 14-person team from specification to formal handover. Daily '
  'visual meetings, bottleneck analysis, tenders, subcontractors and delivery documentation.'),
 ('Business flows and operational constraints',
  'ELOHVAC: estimates, planning, materials, subcontractors and full P&L. Biofos: maintenance, '
  'spare-part flow and inventory in critical 24/7 plant. ARJ Engineering: leadership of 12 workshop '
  'technicians and mechanics.'),
 ('Improvement with evidence',
  'PDCA, 5S, A3 and 5 Whys in plant and project work. At Novo, a PDCA programme reduced energy costs by '
  '40 %. This is an operating-cost result, not a claimed improvement in drive manufacturability or '
  'factory yield.'),
 ('Digital working and follow-up',
  'Excel/Power Query, Power BI and SAP for finance, assets and costs. Python/Claude API tools for '
  'estimates, schedules, quality checklists and KPI follow-up: over 40 % productivity improvement in '
  'contracting.')]

MODELS = [('Readiness and milestones',
  'Agree evidence and acceptance criteria with each function. Track what is ready, what is missing and '
  'which dependency affects the next milestone.'),
 ('Ownership across functions',
  'A simple responsibility matrix (RACI) can clarify who delivers, who reviews and who decides. Use the '
  'established project organisation and decision process.'),
 ('Risk and change follow-up',
  'Keep risks, assumptions, dependencies and decisions visible. When scope changes, review the effect '
  'on materials, capacity, cost and timing with the responsible functions.'),
 ('Working meetings',
  'Draw on Ventek’s visual planning and bottleneck analysis. Use meeting time to resolve obstacles and '
  'confirm next actions rather than repeat status reports.'),
 ('Problem solving',
  'Use PDCA/A3/5 Whys on a recurring problem. Confirm the cause with the people doing the work, try a '
  'solution and check its effect.'),
 ('Handover to Operations',
  'Build the acceptance plan with Operations early. Follow test findings, documentation and training '
  'requirements to named owners before asking for sign-off.')]

ACHIEVEMENTS = [('37 CAPEX projects at Novo Nordisk',
  'DKK 2–10 million per project; coordination of 25 specialists across engineering, procurement and '
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

PRACTICAL_CV = ('Based in Måløv, Ballerup Municipality, Denmark. The position is on-site at the Supply Chain '
 'Technology Center in Gråsten. A sustainable attendance/relocation arrangement, start date and '
 'transition from ELOHVAC must be agreed; no relocation commitment or remote-work arrangement is '
 'assumed. Native Danish, professional English and native Persian/Farsi. Category B driving licence.')

REFERENCES = 'Former managers at Novo Nordisk A/S and Biofos (Lynetten) — available on request.'

PARTNER = [('R&D and Product Management',
  'Clarify which requirements are fixed, which remain open and what each change means for the launch. '
  'Bring choices to the appropriate decision owner rather than let different functions plan against '
  'different assumptions.'),
 ('Manufacturing Engineering and Operations',
  'Review manufacturability, scalability, capacity, process readiness and training needs with those '
  'accountable for the solution. The project manager coordinates the commitments; specialist '
  'engineering decisions stay with the responsible experts.'),
 ('Procurement and Quality',
  'Connect material availability and supplier dependencies to the project milestones. Make quality '
  'evidence and acceptance responsibilities explicit, so the team knows what must be resolved before '
  'the next step.'),
 ('Sponsor and wider project organisation',
  'Keep stakeholder communication direct and timely. Where regional or functional priorities conflict, '
  'explain the impact and the decision needed. Cross-region launch coordination would be new; I would '
  'learn the local responsibilities and work through the agreed owners.')]

FIRST90 = [('First week',
  'Agree the assigned NPI project, decision rights and expectations with the sponsor. Meet the R&D, '
  'Product Management, Manufacturing Engineering, Procurement, Quality and Operations owners. Review '
  'the current plan and walk the relevant process with the people who know it. Record the most urgent '
  'unresolved decisions and their owners.'),
 ('By day 30',
  'Build a shared readiness view within the existing project system: manufacturing, materials, '
  'processes, capacity and quality evidence against agreed milestones. Learn the product, business '
  'flows and launch process with the functional owners. Confirm the main risks and dependencies, '
  'establish a short decision cadence and agree what Operations needs at handover.'),
 ('By day 60',
  'Resolve one agreed readiness obstacle with the relevant functions, such as a late material '
  'clarification or an incomplete equipment acceptance requirement. Track the effect on the project '
  'plan and confirm what is still needed before the next build. Review a live product or component '
  'change with its owners and make the consequences and required decisions clear.'),
 ('By day 90',
  'Review milestone performance, open risks and readiness evidence with the sponsor and Operations. '
  'Check whether the project’s next step is supported by the agreed criteria and whether actions are '
  'being closed. Agree the next priorities, any required escalation and further learning needs. Record '
  'lessons with the team for the next project.')]

KEYWORDS = ('Technical project management · Cross-functional coordination · Milestones and priorities · Risks and '
 'dependencies · Stakeholder communication · Material planning · FAT/SAT · Quality documentation · '
 'Handover · PDCA and A3 · SAP finance/assets · Excel/Power Query · Python and Claude API.')


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

    m.models_table("PROJECT LEADERSHIP AND READINESS",
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
    m.models_table("FIRST 90 DAYS — PEOPLE, READINESS AND DELIVERY",
                   ("When", "What is in place"), FIRST90)

    m.section("WORKING WITH THE PROJECT TEAM")
    for label, body in PARTNER:
        m.bullet(label, body, after=30)

    m.section("READINESS REVIEW — FROM PLAN TO EVIDENCE")
    m.para('I would start a readiness review by asking the functional owners to show the evidence behind the plan. Are the product and process requirements clear enough for the next activity? Are materials, equipment, capacity and quality checks aligned with the planned build? Do the people receiving the new process know what they are accepting and what remains open? Where the answers differ, the project needs a decision, an owner and a date, not a more confident status colour. Cost, quality, manufacturability and scalability must be considered together with Manufacturing Engineering and Operations. A conditional next step may be reasonable, but the conditions and decision authority should be explicit. The review should use Danfoss’s established criteria; it is not a proposed replacement for its launch governance.', after=80)

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
    build(os.path.join(ROOT, "Shahram_Ajloo_Danfoss_SCProjectManagerNPI.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_Danfoss_SCProjectManagerNPI.docx"))
