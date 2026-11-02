# -*- coding: utf-8 -*-
"""atNorth Manager of Power and Permits — English combined application and CV in stored master design."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Manager of Power and Permits – Nordics | atNorth | Capacity, consent and delivery confidence'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv, Denmark")
DATE = '2 November 2026'
RECIPIENT = 'atNorth · Director of Site Development · via Rebecca Saks, Compass HRG'
SUBJECT = 'Application: Manager of Power and Permits – Nordics — reference 2607.243'

# ------------------------------------------------------------------ side 1
INTRO = ['A development pipeline becomes a deliverable customer commitment only when power capacity, grid '
 'access and permits converge on a credible date. Across the Nordics, atNorth needs a common decision '
 'framework that distinguishes an attractive site from one with an executable power and permitting '
 'path—and makes the remaining constraints visible before commercial commitments are made.',
 'The proposed day-one structure is a site-by-site power-and-permits register, an evidence-based '
 'readiness gate and an integrated decision calendar. It connects capacity, connection milestones, '
 'contractual conditions, permit dependencies and heat-reuse options to an accountable specialist and '
 'next decision. Common Nordic governance should make country-specific requirements visible, not assume '
 'that five jurisdictions share one approval process.']

BULLETS = [('Lead specialists with clear ownership',
  'Agree outcomes, interfaces and decision rights across energy, site development and heat reuse. '
  'Combine specialist autonomy with weekly portfolio reviews, regular 1:1s and visible escalation. Use '
  'monthly wellbeing survey themes to address workload and collaboration, closing the feedback loop '
  'without turning individual responses into performance scores.'),
 ('Separate power feasibility from secured capacity',
  'Assess grid connection options with the responsible technical specialists and relevant TSOs/DSOs. '
  'Record available evidence, connection conditions, reinforcement dependencies, costs and dates; '
  'distinguish indicative capacity from an executed agreement and energised supply. Advise senior '
  'stakeholders on scenarios and business implications, not just headline MW.'),
 ('Connect permitting to the critical path',
  'Build a country-specific register of building, environmental and emissions requirements with local '
  'advisers and public authorities. Identify submissions, dependencies, conditions and outstanding '
  'decisions. Integrate the permit path into site selection and development; a planned submission is '
  'not a consent, and consent conditions may still constrain operations.'),
 ('Make energy offerings commercially robust',
  'Prepare pricing strategies and PPAs with Finance, Legal and energy specialists. Test volume, load '
  'shape, tenor, price exposure, delivery profile and allocation of risk against customer demand. '
  'Negotiate within an agreed mandate with grid operators, power producers and utilities; do not treat '
  'electrical authorisation as evidence of PPA trading expertise.'),
 ('Develop heat reuse as a deliverable value case',
  'Assess heat quantity, temperature, seasonality, offtaker demand, connection investment and operating '
  'responsibilities. Evaluate alternative energy through technical, commercial and regulatory '
  'scenarios. Align customer power offerings and local-community benefit with contracts and credible '
  'implementation milestones, not an unqualified sustainability claim.')]

SYSTEM = ('Week one establishes the portfolio baseline, team mandate and highest-risk commitments. By day 30, '
 'priority sites have a verified constraint map; by day 60, one site has a tested readiness gate and a '
 'reviewed energy/heat-reuse case. Day 90 reviews Nordic governance, unresolved risks and the '
 'development roadmap with the Director of Site Development.')

MIRROR = ('Transferable evidence combines electrical authorisation (LV/MV/HV), full P&L and specialist '
 'leadership. Novo Nordisk: 37 concurrent CAPEX projects of DKK 2–10m each, coordination of 25 '
 'specialists and regulated handover with zero critical findings. ELOHVAC: 5 electricians and 3 '
 'apprentices, technical contracting and customer commitments. PDCA reduced energy costs by 40%; '
 'Python/Claude API tools improved contracting productivity above 40%.')

HONEST = ('The CV does not establish a 7+ year power/utilities/grid-development track record, TSO/DSO '
 'negotiations, Nordic permit ownership, infrastructure agreements or PPA/heat-offtake contracting. '
 'Electrical and CAPEX experience is a foundation, not a substitute for those requirements. This is a '
 'transition profile requiring an explicit discussion of entry expectations and specialist support.')

CULTURE = ('atNorth’s Dependable, Empowering and Flexible values call for transparent commitments, trusted '
 'specialists and practical adaptation. Its stated one-to-one engagements, monthly wellbeing surveys and weekly '
 'connection should become a working leadership rhythm: listen, act on constraints and share decisions '
 'across countries without diluting local expertise.')

PRACTICAL = ('Based in Måløv; a Danish atNorth base would be the preferred arrangement. Professional English and '
 'native Danish/Persian. The stated 4–6 Nordic travel days per month, actual base, start date and '
 'transition from ELOHVAC would be agreed; immediate availability is not assumed.')

CLOSING = ('A useful first discussion would clarify the most constrained sites and whether technical-commercial '
 'leadership can complement the existing specialists, given the grid, permitting and energy-contracting '
 'experience this end-to-end role requires.')

# ------------------------------------------------------------------ CV
PROFILE = 'Power availability, grid capacity and permitting must support credible Nordic development and customer commitments. The foundation is B.Tech engineering education, Danish electrical authorisation (LV/MV/HV), full P&L and specialist leadership. Novo Nordisk: 37 CAPEX projects, coordination of 25 specialists, budget/risk follow-up and regulated handover. ELOHVAC adds direct people leadership and technical contracting. Professional Claude coder: Python/Claude API tools delivered >40% productivity improvement. Nordic grid negotiations, permit portfolios, PPAs and heat-offtake contracts are learning gaps, not prior appointments.'

PRACTICE = [('Specialist leadership — documented evidence',
  'Novo Nordisk: coordination of 25 specialists across engineering, procurement and site operations. '
  'ELOHVAC: direct leadership of 5 electricians and 3 apprentices, daily planning, 1:1/MUS and '
  'structured training.'),
 ('Portfolio delivery and risk — documented evidence',
  '37 concurrent CAPEX projects at DKK 2–10m each; progress, budget, risk and resource follow-up with '
  'management/client reporting. Ventek-Air adds 11 parallel projects and a 14-person team—not a Nordic '
  'grid-capacity portfolio.'),
 ('Technical-commercial judgement — documented evidence',
  'ELOHVAC: quotations, materials, subcontractors, customer commitments and full P&L. Ventek-Air: '
  'tenders and agreement basis. These support scope and risk discipline, not a claimed record of '
  'utility, PPA or infrastructure-agreement negotiations.'),
 ('Electrical and regulated systems — documented evidence',
  'LV/MV/HV authorisation; critical plant including HV switchgear, HVAC and SCADA at Biofos; '
  'UPS/electrical interfaces and FAT/SAT/IQ/OQ/PQ at Novo. Regulatory project acceptance is not '
  'ownership of Nordic building/environmental/emissions permits.'),
 ('Energy improvement — evidence and boundary',
  'PDCA programme reduced energy costs by 40% at Novo Nordisk. Relevant improvement discipline; no '
  'claim of delivered datacenter heat reuse, alternative-energy development or electricity-market '
  'trading.'),
 ('Leadership and digital methods — evidence and proposal',
  'Documented huddles, apprentice training and 1:1/MUS; proposed RACI, GROW/SBI feedback and portfolio '
  'gates. Python/Claude tools delivered >40% productivity improvement; prospective analysis uses '
  'approved data environments, source evidence and specialist review.')]

MODELS = [('Power-and-permits register',
  'Per site: demand, capacity evidence, grid milestones, agreements, permit conditions, heat-reuse '
  'dependencies, owner and next decision.'),
 ('Readiness gate',
  'Evidence status: indicative/conditional/contracted/energised for power; '
  'submission/decision/conditions for permits. Escalate unresolved customer-commitment risk.'),
 ('Integrated critical path',
  'Country-specific grid, permit, construction and customer dates; approved local advisers validate '
  'requirements and realistic lead times.'),
 ('Commercial scenarios',
  'Finance/Legal review of pricing, PPAs, connection cost, load shape and risk allocation. Heat-reuse '
  'case includes offtaker demand, temperature and infrastructure cost.'),
 ('Specialist-team rhythm',
  'RACI, weekly coordination and regular 1:1s; monthly wellbeing themes become agreed workload/support '
  'actions. GROW/SBI proposed for feedback.'),
 ('Evidence-led improvement',
  'Documented PDCA/A3/5 Whys; proposed portfolio review tests assumptions, action closure and reusable '
  'learning across Nordic sites.')]

ACHIEVEMENTS = [('37 concurrent CAPEX projects',
  'DKK 2–10m each; coordination of 25 specialists across engineering, procurement and site operations '
  'at Novo Nordisk.'),
 ('Direct leadership and full P&L',
  'ELOHVAC: 5 electricians and 3 apprentices, technical contracting, customer commitments and '
  'structured training.'),
 ('40% reduction in energy costs',
  'PDCA-based improvement at Novo Nordisk; operational energy savings, not an electricity procurement '
  'or PPA result.'),
 ('Above 40% productivity improvement',
  'Python/Claude API tools for estimates, planning and KPI reporting in '
  'technical contracting.')]

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

PRACTICAL_CV = ('Måløv, Denmark; Danish atNorth location preferred, actual base to be agreed. Professional English, '
 'native Danish and Persian/Farsi; driving licence B. Role includes approximately 4–6 travel days per '
 'month across the Nordics; arrangements, start date and ELOHVAC transition must be agreed. B.Tech '
 '(EQF6), Technology Management & Mechanical Engineering; authorised electrical engineer (LV/MV/HV). No '
 '7+ year grid-development/utility portfolio, TSO/DSO negotiation, Nordic permit ownership or '
 'PPA/heat-offtake contracting is claimed. Specialist support and the feasibility of this transition '
 'require explicit agreement.')

REFERENCES = 'Former managers at Novo Nordisk A/S and Biofos (Lynetten) — available on request.'

KEYWORDS = ('Target remit and learning requirements: power availability · grid capacity · grid access · power '
 'feasibility · grid connection options · TSOs · DSOs · utilities · public authorities · infrastructure '
 'agreements · permitting · building, environmental and emissions matters · PPAs · pricing strategies · '
 'heat reuse · alternative energy · site selection · Nordic governance. These describe the role and '
 'proposed work, not an existing Nordic grid/permit portfolio or energy-contracting track record.')

# ------------------------------------------------------------ side 4
FIRST90 = [('Week 1',
  'Director of Site Development confirms scope, decision rights and priority customer commitments. Meet '
  'energy/site-development/heat-reuse specialists and Development, Sales, Finance, Legal, Public '
  'Affairs and Operations. Hold first 1:1s; map current workload and expertise. Output: portfolio '
  'register, escalation map and individual grid/permitting learning plan.'),
 ('By day 30',
  'Validate priority-site demand, grid/capacity evidence, agreement status and permit conditions with '
  'local specialists. Map TSO/DSO/municipal interfaces and decision dates. Baseline readiness, '
  'unresolved dependencies and at-risk commitments; agree evidence thresholds and escalation rules '
  'rather than inventing a MW target.'),
 ('By day 60',
  'Pilot the readiness gate on one development/customer opportunity. Review a power-option comparison '
  'and an energy/heat-reuse value case with Finance, Legal and technical owners. Engage relevant '
  'external parties under an agreed mandate. Output: documented recommendation, assumptions and '
  'approved next actions—not a promised permit or secured capacity.'),
 ('By day 90',
  'Review the Nordic roadmap, critical-path constraints, commercial exposures and team capacity with '
  'the Director. Evaluate the pilot and standardise only the governance that transfers across '
  'jurisdictions. Check wellbeing-action follow-up and specialist development. Agree future targets and '
  'responsibilities with remaining competence gaps visible.')]

PARTNER = [('Director of Site Development and Nordic specialists',
  'Manager owns coordination and escalation; specialists validate technical and local-regulatory '
  'evidence. Agree delegated authority and resource needs; regular 1:1s support ownership rather than '
  'repeated status collection.'),
 ('Development, Sales and Operations',
  'Embed power and permit readiness in site selection, development and customer offers. Development '
  'owns delivery dependencies, Sales needs an approved commitment boundary, and Operations tests '
  'whether the proposed solution can be operated reliably.'),
 ('Finance, Legal and Public Affairs',
  'Finance validates scenarios and commercial value; Legal reviews agreements, risk allocation and '
  'permit/contract conditions. Public Affairs supports transparent engagement and local-community '
  'interests without substituting for formal authority decisions.'),
 ('Grid operators, utilities, municipalities and heat partners',
  'Build relationships around verifiable requirements, realistic timelines and a clear negotiation '
  'mandate. Distinguish stakeholder support from binding agreements/permits. Heat-reuse partners need '
  'aligned demand, investment and operating responsibilities.')]


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

    m.section("SPECIALIST LEADERSHIP — TECHNICAL AND COMMERCIAL EVIDENCE")
    for label, body in PRACTICE:
        m.bullet(label, body, after=20)

    m.models_table("PROPOSED NORDIC POWER AND PERMITTING GOVERNANCE",
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
    m.models_table("FIRST 90 DAYS — READINESS, ALIGNMENT AND DECISIONS",
                   ("When", "What is in place"), FIRST90)

    m.section("CROSS-FUNCTIONAL OWNERSHIP AND EXTERNAL RELATIONSHIPS")
    for label, body in PARTNER:
        m.bullet(label, body, after=20)

    m.section("POWER AND PERMIT READINESS — DECISION QUALITY CHECK")
    m.para("Before a site or customer commitment passes a readiness gate, trace the stated capacity and date to current grid evidence, agreement conditions and the integrated delivery plan. Confirm permit status, outstanding conditions and local specialist/legal interpretation; do not equate a submitted application with permission to build or operate. Test energy and heat-reuse assumptions against actual load/offtake profiles, investment, risk allocation and contractual responsibilities. Record unresolved dependencies, decision authority and the approved commitment boundary. A common register improves transparency; it cannot create grid capacity, accelerate a regulator by assumption or turn an indicative discussion into a binding agreement.", after=80)

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

    return m.save(path, title="Application and CV — atNorth Manager of Power and Permits Nordics, 2607.243",
                  subject="Power and permitting readiness, specialist leadership and Nordic governance",
                  keywords="atNorth, power, permitting, Nordic governance, specialist leadership",
                  comments="Stored master design. English. Transferable evidence and sector gaps explicit.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_atNorth_ManagerPowerPermits.docx")
    build(out)
    print("OK " + out)
