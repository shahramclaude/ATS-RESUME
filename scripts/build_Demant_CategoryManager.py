# -*- coding: utf-8 -*-
"""Demant Category Manager — English combined application and CV in stored master design."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Category Manager – Standard Electronics | Demant | Cost, continuity and supplier value'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv, Denmark")
DATE = '2 November 2026'
RECIPIENT = 'Demant · Mette Buus Pihl, Director of Direct Strategic Procurement · Smørum'
SUBJECT = 'Application: Category Manager – Standard Electronics'

# ------------------------------------------------------------------ side 1
INTRO = ['The Electronics, PCBs & Batteries category must deliver more than a lower quoted price. Category '
 'strategy needs to connect Demant’s business demand with supply-market development, technical '
 'requirements, continuity and measurable value. A sourcing decision only succeeds when the approved '
 'commercial benefit survives qualification, contracting and actual delivery.',
 'The proposed day-one framework is a demand-and-spend baseline, a supplier/risk map, a sourcing '
 'decision log and a value-realisation register. These would be adapted to Demant’s procurement methods '
 'and Strategic Cost & Improvement Program, connecting stakeholder decisions to evidence rather than '
 'adding a parallel procurement process.']

BULLETS = [('Build the category strategy around demand and risk',
  'Segment Electronics, PCBs & Batteries by business demand, technical constraints, supplier dependence '
  'and commercial leverage. Agree priorities with engineering, operations and procurement. Treat '
  'outsourced development and manufacturing as a distinct scope with clear interfaces, capability '
  'requirements and ownership—not simply a purchase-price exercise.'),
 ('Make end-to-end sourcing transparent',
  'Structure market analysis, supplier identification, RFx processes, evaluation and award '
  'recommendations around agreed requirements and weighted criteria. Involve technical and quality '
  'specialists before shortlisting. Compare complete offers on a common scope; document assumptions, '
  'alternatives and the authorised decision.'),
 ('Negotiate value that can be delivered',
  'Prepare negotiations using demand scenarios, cost drivers, total cost, capacity and credible '
  'alternatives. Agree contracting positions with the relevant commercial and legal owners. Scope, '
  'pricing mechanisms, lead times, change notification and performance commitments must be understood '
  'before award; negotiation authority is explicit.'),
 ('Realise and verify improvement',
  'Support the Strategic Cost & Improvement Program with an agreed baseline, named initiative owner and '
  'Finance-validated benefit logic. Separate realised savings from cost avoidance and distinguish price '
  'effects from volume, mix and currency movements. Track implementation cost and qualification timing '
  'before reporting net value.'),
 ('Strengthen stakeholder relationships and supplier collaboration',
  'Use a shared action and decision register to ensure transparency, compliance and strategic '
  'alignment. Review supplier performance and escalation with the responsible stakeholders. Changes to '
  'components, suppliers or manufacturing must follow Demant’s approved technical and quality '
  'processes; sourcing does not replace qualification or release authority.')]

SYSTEM = ('Week one establishes scope, stakeholders, data access and decision rights. By day 30, an initial '
 'category baseline and opportunity/risk shortlist are reviewed. By day 60, a prioritised sourcing or '
 'improvement case has a tested decision trail; day 90 reviews implementation readiness and benefit '
 'evidence. Targets follow the validated baseline, not an invented savings percentage.')

MIRROR = ('Transferable evidence is technical-commercial delivery: full P&L, quotations, materials and '
 'subcontractor interfaces at ELOHVAC; tenders and quotations at Ventek-Air; and coordination of 25 '
 'specialists across 37 CAPEX projects at Novo Nordisk. A PDCA programme reduced energy costs by 40%—an '
 'operational improvement, not a procurement-savings claim. Python/Claude API tools improved '
 'productivity above 40% in technical contracting.')

HONEST = ('The CV does not establish 2–5 years of procurement and category management, solid '
 'electronics-industry sourcing, or ownership of PCB/battery categories and outsourced '
 'development/manufacturing. Electrical engineering and regulated project delivery are relevant '
 'foundations, not substitutes for these entry requirements. A transition needs an explicit fit and '
 'support discussion.')

CULTURE = ('Demant’s values—trust, teamwork, innovative solutions and a can-do attitude—translate into clear '
 'commitments, early cross-functional challenge and open sharing of lessons. In a Denmark/Poland team, '
 'independent ownership should strengthen collective decisions, not become isolated sourcing work.')

PRACTICAL = ('Based in Måløv, with practical access to Smørum and able to attend onsite from the first agreed '
 'working day. Professional English; native Danish and Persian/Farsi. Start date and arrangements for '
 'ELOHVAC would be agreed before appointment.')

CLOSING = ('A useful first discussion would test whether technical-commercial experience and disciplined '
 'improvement can complement the category team, given the direct procurement and electronics-sector '
 'experience the role requires.')

# ------------------------------------------------------------------ CV
PROFILE = ('The task is to align the Electronics, PCBs & Batteries category with business demand, market '
 'development and demonstrable supplier value. The relevant foundation is B.Tech engineering education, '
 'electrical authorisation (LV/MV/HV), technical-commercial contracting and regulated project delivery. '
 'ELOHVAC provides full P&L, quotations, materials and subcontractor interfaces; Novo Nordisk adds '
 'coordination of 25 specialists across 37 simultaneous CAPEX projects and SAP financial/asset/cost '
 'follow-up. Professional Claude user and coder: Python/Claude API tools for estimates, planning, '
 'quality checklists and KPI reporting delivered productivity improvement above 40%. Direct strategic '
 'procurement, electronics-industry sourcing and PCB/battery category ownership are transition gaps, '
 'not established credentials.')

PRACTICE = [('Commercial responsibility — documented evidence',
  'ELOHVAC: full P&L, quotations/calculation, material planning, subcontractors and customer '
  'commitments. Useful for commercial discipline and cost awareness, not a claim of a managed global '
  'electronics spend portfolio.'),
 ('Technical stakeholder coordination — documented evidence',
  'Novo Nordisk: 37 CAPEX projects at DKK 2–10m each, coordination of 25 specialists and reporting of '
  'progress, budgets, risks and resources across engineering, procurement and operations.'),
 ('Tenders and delivery interfaces — documented evidence',
  'Ventek-Air: tenders, quotations and subcontractor agreement basis across 11 concurrent projects with '
  'a 14-person team. Not equivalent to independent end-to-end electronics RFx or award ownership.'),
 ('Quality and change discipline — documented evidence',
  'FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA with zero critical findings at handover. Controlled '
  'acceptance is transferable; hearing healthcare product development, R&D and electronics '
  'qualification are not claimed experience.'),
 ('Analytical improvement — documented evidence',
  'PDCA delivered a 40% reduction in energy costs at Novo Nordisk; SAP supported financial, asset and '
  'cost follow-up. Proposed procurement application uses total-cost scenarios and verified benefit '
  'tracking, without relabelling energy savings as negotiated supplier savings.'),
 ('Leadership and digital methods — evidence and application',
  'Daily huddles, 1:1/MUS and structured training for 5 electricians and 3 apprentices. Python/Claude '
  'tools delivered >40% productivity improvement. Proposed category coordination adds RACI, GROW/SBI '
  'feedback and source-checked analysis, not unreviewed automated supplier decisions.')]

MODELS = [('Demand and category baseline',
  'Map spend, demand, contracts and supplier dependence; verify data completeness and technical '
  'constraints with category stakeholders.'),
 ('Supplier/risk segmentation',
  'Proposed Kraljic-style view of supply risk and business impact; challenge assumptions with '
  'experienced category peers before selecting a strategy.'),
 ('RFx decision trail',
  'Requirements, eligibility, evaluation criteria, complete comparable offers, evidence and award '
  'recommendation; approved technical and commercial reviewers.'),
 ('Negotiation and total cost',
  'Scenario-based total cost, cost-driver assumptions, alternatives and authorised positions; no '
  'unvalidated supplier switch or unsupported target.'),
 ('Value-realisation register',
  'Baseline, initiative owner, timing, one-off costs and Finance sign-off. Separate realised savings, '
  'cost avoidance and price/volume/mix/currency effects.'),
 ('Cross-functional learning',
  'RACI and short decision reviews proposed for the category; documented PDCA/A3 and huddles support '
  'improvement and knowledge exchange.')]

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

PRACTICAL_CV = ('Måløv, Denmark, with practical access to Smørum; onsite attendance from day one of an agreed '
 'appointment. Professional English, native Danish and Persian/Farsi; driving licence B. Start date and '
 'transition from ELOHVAC must be agreed. B.Tech (EQF6) is technical higher education. No 2–5-year '
 'category-management record, solid electronics-industry procurement, PCB/battery category ownership or '
 'outsourced product-development/manufacturing sourcing track record is claimed. These are material fit '
 'gaps requiring explicit discussion, not gaps that an electrical authorisation or generic checklist '
 'can remove.')

REFERENCES = 'Former managers at Novo Nordisk A/S and Biofos (Lynetten) — available on request.'

KEYWORDS = ('Target remit and learning requirements: Category Manager · Standard Electronics · Direct Strategic '
 'Procurement · Electronics, PCBs & Batteries · category strategy · outsourced development and '
 'manufacturing · market analysis · supplier identification · RFx processes · evaluation · award '
 'recommendations · negotiations · contracting · supplier relationship management · Strategic Cost & '
 'Improvement Program. These category-specific terms describe the target role, not prior electronics '
 'procurement expertise.')

# ------------------------------------------------------------ side 4
FIRST90 = [('Week 1',
  'Director confirms category scope, authority, current commitments and priorities. Meet Category '
  'Managers and Program Managers in Denmark/Poland, engineering, quality, operations and Finance. '
  'Review approved procurement methods and contracts. Output: stakeholder/RACI map, immediate '
  'supplier-risk list and individual electronics/category-method learning plan.'),
 ('By day 30',
  'Validate spend and demand data, supplier dependence, contract coverage and known quality/delivery '
  'issues. With experienced peers, develop a first category strategy hypothesis and improvement '
  'shortlist. Baseline value and risk measures with Finance; record missing data and constraints before '
  'setting savings targets.'),
 ('By day 60',
  'Develop one agreed sourcing or cost-improvement case with an experienced category colleague. Test '
  'market analysis, supplier identification, evaluation and award logic against approved requirements. '
  'Prepare negotiation scenarios and contract issues for authorised review. Output: evidence-backed '
  'recommendation, risks and implementation dependencies—not an automatic supplier award.'),
 ('By day 90',
  'Review the category strategy and prioritised roadmap with the Director and stakeholders. For '
  'approved initiatives, verify qualification, contracting and implementation readiness. Review '
  'realised benefit separately from pipeline estimates, supplier actions and unresolved risks. Agree '
  'next-stage targets, capability development and independent responsibilities.')]

PARTNER = [('Director and procurement peers',
  'Align priorities, decision rights and category interfaces. Use professional sparring across Denmark '
  'and Poland to challenge assumptions and share reusable methods; do not imply line management of the '
  'procurement team.'),
 ('Engineering, R&D and quality',
  'Confirm specifications, development/manufacturing interfaces, approved supplier requirements and '
  'qualification evidence. Technical and quality owners decide acceptability; no component substitution '
  'is promised on price alone.'),
 ('Operations and Finance',
  'Operations validates demand, delivery and continuity implications; Finance agrees baseline and '
  'benefit recognition. Maintain one clear view of initiative status, implementation costs and expected '
  'timing.'),
 ('Suppliers and commercial/legal owners',
  'Use structured reviews of performance, commitments and unresolved issues. Prepare negotiations and '
  'contract changes with authorised owners; changes in capacity, pricing, product status or '
  'manufacturing need a controlled response.')]


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

    m.section("TECHNICAL-COMMERCIAL EVIDENCE — PROCUREMENT TRANSITION")
    for label, body in PRACTICE:
        m.bullet(label, body, after=20)

    m.models_table("PROPOSED CATEGORY AND SOURCING FRAMEWORK",
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
    m.models_table("FIRST 90 DAYS — CATEGORY BASELINE, SOURCING AND VALUE",
                   ("When", "What is in place"), FIRST90)

    m.section("STAKEHOLDER MODEL — DECISIONS AND RESPONSIBILITIES")
    for label, body in PARTNER:
        m.bullet(label, body, after=20)

    m.section("SOURCING AND VALUE-REALISATION QUALITY CHECK")
    m.para("Before recommending an award, verify demand assumptions, technical scope, supplier capability, comparable total cost and the required qualification route. Record evaluation evidence, commercial exceptions and the authorised decision. Before reporting a benefit, confirm baseline, realised quantity, price basis, currency treatment, implementation costs and Finance approval. Cost avoidance and negotiated potential remain distinct from realised savings. Sample the trail from RFx offer through contract and actual purchasing evidence to test whether the benefit survives execution. Component, supplier and manufacturing changes follow the approved technical/quality process; category strategy never replaces product release authority. Claude-assisted analysis must retain source evidence and human review within approved data environments.", after=80)

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

    return m.save(path, title="Application and CV — Demant Category Manager Standard Electronics",
                  subject="Category strategy, sourcing decisions and verified supplier value",
                  keywords="Demant, category management, procurement, electronics, sourcing",
                  comments="Stored master design. English. Transferable evidence and sector gaps explicit.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_Demant_CategoryManager.docx")
    build(out)
    print("OK " + out)
