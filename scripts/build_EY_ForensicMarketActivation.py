# -*- coding: utf-8 -*-
"""EY 1739349 — English combined application and CV in stored master design."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Market Activation — AI-enabled Forensic Solutions | EY | Associate Director application'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv, Denmark")
DATE = '1 November 2026'
RECIPIENT = 'EY · Forensic & Integrity Services · European / Regional leadership'
SUBJECT = 'Application: Associate Director — forensic solutions market activation | Requisition 1739349'

# ------------------------------------------------------------------ side 1
INTRO = ['The commercial challenge is not to persuade country teams that AI exists. It is to make a '
 'technology-enabled forensic proposition easier to position, buy and deliver than the manual '
 'alternative — while preserving trust, professional judgement and defensible evidence. Integrity '
 '& Compliance can open the conversation, but growth requires a repeatable activation model across '
 'the wider portfolio, with local leaders owning the client relationship.',
 'The proposed operating model starts with a small set of priority markets and client problems, '
 'not a Europe-wide technology campaign: agree a country sponsor, a proposition and a qualified '
 'pursuit; equip the team with a value case and a credible demo; then connect the sale to a '
 'delivery-ready solution and measure whether the new method is actually used.']

BULLETS = [('The requirement: country-led go-to-market plans and priority pursuits',
  'The response is a market activation charter: target clients, buying problem, sponsor, relevant '
  'solution, route to market and next decision. Country and Regional Forensics leaders select '
  'priorities against pipeline quality and delivery readiness, rather than treating every '
  'territory as equally ready to launch.'),
 ('The requirement: turn forensic technology and AI into client value',
  'The response is a proposition card with the client problem, baseline process, proposed '
  'workflow, benefits to test and limitations. Integrity & Compliance, investigations, monitoring, '
  'forensic data analytics, eDiscovery and third-party or regulatory risk each need their own '
  'buying rationale. Domain specialists validate the claims before they reach a client.'),
 ('The requirement: move manual delivery towards technology-led delivery',
  'The response is an adoption loop: map the current workflow, select a bounded use case, agree '
  'quality gates, run a supported pilot and coach local champions. Track eligible engagements, '
  'actual use, time to first value and quality exceptions. Training attendance alone is not '
  'evidence of adoption.'),
 ('The requirement: shape complex proposals and win opportunities',
  'The response is a pursuit plan with buyer and stakeholder map, value hypothesis, scope, '
  'evidence, delivery owner and commercial assumptions. A bid/no-bid review tests differentiation '
  'and capacity. Specialists own forensic methodology and legal conclusions; commercial leadership '
  'makes the proposition coherent and the next client decision explicit.'),
 ('The requirement: expand pipeline, revenue and cross-border engagements',
  'The response is a shared pipeline view with defined stages, value, probability, sponsor, '
  'solution and next action. A monthly review separates sourced opportunities from influenced '
  'pursuits, follows conversion and identifies where another country can contribute expertise '
  'without confusing account ownership.'),
 ('The requirement: practical playbooks, case studies and compelling demos',
  'The response is a reusable activation kit: discovery questions, proposition, approved evidence, '
  'demo script, objections, pricing assumptions and delivery handoff. Demos use synthetic or '
  'approved data and distinguish model suggestions from verified findings. Case studies require '
  'client permissions and substantiated outcomes.'),
 ('The requirement: influence a distributed, matrixed organisation',
  'The response is named country sponsors, a RACI and an explicit escalation route. Country teams '
  'help shape the offer, retain client ownership and receive hands-on support for their first '
  'pursuit. Leading practices are shared across Europe and, when readiness permits, APAC; '
  'regulatory assumptions are checked locally.'),
 ('The requirement: market presence and commercially useful thought leadership',
  'The response is a cadence of client roundtables, practitioner sessions and short insights '
  'grounded in actual buyer questions. Content links an emerging regulatory concern to a decision '
  'and an actionable offering. Country feedback informs the portfolio; event attendance is '
  'followed through into qualified conversations and opportunities.')]

SYSTEM = ('The proposed dashboard connects revenue growth, pipeline expansion, technology adoption, country '
 'capability and multi-country work. It shows where an offer is being sold but not delivered, or '
 'demonstrated but not bought. Python, Power BI and Claude can support analysis, asset preparation '
 'and reporting, subject to EY-approved tools, confidentiality, human review and evidence '
 'controls.')

MIRROR = ('Transferable evidence: full P&L and client-facing contracting responsibility in ELOHVAC; '
 'practical AI adoption through self-built Python/Claude API tools with a documented productivity '
 'improvement above 40%; coordination of 25 specialists across engineering, procurement and site '
 'operations; and regulated delivery with zero critical findings across 37 CAPEX projects.')

HONEST = ('This is a substantial sector transition. My record does not establish the required 10–15 years '
 'in Forensics, Compliance, Financial Crime or Investigations, professional-services forensic '
 'revenue growth, an established buyer network, or Europe/APAC market leadership. Engineering '
 'compliance is not forensic expertise. The application offers commercial ownership, AI '
 'implementation and change discipline as transferable evidence, not substitutes for those missing '
 'credentials.')

CULTURE = ('EY describes integrated forensic, legal, sector and technology expertise and positions Integrity '
 '& Compliance around appropriate governance and doing what is right, not merely legal. The '
 'commercial implication is clear: sell a defensible client outcome, not an AI claim. Local '
 'expertise and specialist judgement must remain visible as the portfolio scales.')

PRACTICAL = ('Based in Måløv, Denmark. Professional English, native Danish and Persian/Farsi. European hub, '
 'hybrid arrangements and the advertised 30–50% travel requirement would need agreement; '
 'availability and arrangements for the existing business would be settled before appointment.')

CLOSING = ('A useful first discussion would test one market and one proposition: who buys it, why now, what '
 'makes the outcome credible, and what must change in the local delivery workflow?')

# ------------------------------------------------------------------ CV
PROFILE = ('Market activation for technology-enabled services requires commercial ownership, practical '
 'adoption and a reliable delivery handoff. Relevant evidence comes from running a technical '
 'contracting business with full P&L, implementing own AI-supported planning and reporting tools, '
 'and coordinating regulated engineering projects. Authorised electrical engineer (LV/MV/HV), '
 'B.Tech in Technology Management & Mechanical Engineering, with multidisciplinary leadership and '
 'practical Python/Claude API capability. Seeking a sector transition, not presenting as an '
 'established forensic-services executive. No claimed 10–15 years in forensic practice, forensic '
 'sales track record or established European/APAC buyer network. The proposed contribution is a '
 'structured activation model developed with EY country leaders and forensic specialists.')

PRACTICE = [('Commercial ownership — evidence',
  'ELOHVAC: quotations, planning, materials, subcontractors, quality assurance and handover with '
  'full P&L responsibility. Relevant to scoping, client accountability and delivery economics; not '
  'presented as enterprise forensic solution selling.'),
 ('AI adoption — evidence',
  'Built Python/Claude API tools for estimates, schedules, quality checklists and KPI dashboards; '
  'productivity improvement above 40%. Practical understanding of how a tool becomes an adopted '
  'workflow, with review and accountable users.'),
 ('Matrix coordination — transferable evidence',
  'Coordinated 25 specialists across engineering, procurement and site operations at Novo Nordisk. '
  'Clear interfaces, decisions and follow-up; no claim of regional Forensics leadership or APAC '
  'experience.'),
 ('Quality and trust — evidence',
  'FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA with zero critical findings at handover. Relevant habits '
  'are traceability and documented review; pharmaceutical qualification does not establish '
  'eDiscovery or investigations credentials.'),
 ('Forensic portfolio — proposed commercial approach',
  'Work with specialists on Integrity & Compliance, investigations, monitoring, forensic data '
  'analytics, eDiscovery, third-party risk and regulatory risk. Translate validated capabilities '
  'into a buying case without claiming practitioner mastery.'),
 ('Adoption and growth — proposed measurement',
  'Track pipeline stage movement, win rate, revenue, active countries, qualified local sellers, '
  'technology use on eligible engagements and cross-border delivery. Establish baselines before '
  'claiming improvement.')]

MODELS = [('Market activation charter',
  'Country sponsor, client need, regulatory context, priority segment, proposition, pursuit owner, '
  'delivery readiness and first measurable outcome.'),
 ('Proposition and pursuit',
  'Buyer map, baseline workflow, value hypothesis, approved evidence, scope and pricing '
  'assumptions; bid/no-bid gate, specialist review and delivery handoff.'),
 ('Adoption playbook',
  'Current workflow → bounded pilot → quality/evidence gates → local champion coaching → '
  'deployment review → reusable country materials. Track actual use, not attendance.'),
 ('Commercial dashboard',
  'Qualified pipeline, stage conversion, sourced versus influenced pursuits, revenue and '
  'cross-border opportunities; clear ownership and next action for each priority account.'),
 ('AI and forensic safeguards',
  'Synthetic or approved demo data, source provenance, access control, human validation, audit '
  'trail and specialist sign-off. Client-specific evidence and legal requirements govern real '
  'deployments.'),
 ('Leadership cadence',
  'Country sponsor network, RACI, weekly pursuit support, monthly portfolio review and peer case '
  'clinics. Regulatory interpretation and forensic conclusions stay with qualified specialists.')]

ACHIEVEMENTS = [('Above 40% productivity improvement',
  'Self-built Python/Claude API tools for estimates, planning, quality checklists and KPI '
  'reporting in ELOHVAC; not represented as a forensic client case study.'),
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

PRACTICAL_CV = ('Based in Måløv, Denmark. Professional English; native Danish and Persian/Farsi. Hybrid European '
 'hub, work/travel arrangements and the advertised 30–50% travel require agreement. Start date and '
 'arrangements for ELOHVAC to be agreed before appointment.')

REFERENCES = 'Former managers at Novo Nordisk A/S and Biofos (Lynetten) — available on request.'

KEYWORDS = ('Target portfolio and proposed remit: Integrity & Compliance · Anti-bribery and corruption (ABC) '
 '· Third-party risk · Monitoring · Investigations · Ethics programmes · Forensic data analytics · '
 'eDiscovery · Regulatory risk · AI-enabled solutions · Market activation · Go-to-market · '
 'Priority pursuits · Playbooks · Propositions · Case studies · Pipeline development · Revenue '
 'growth · Technology adoption · Country teams · Cross-border opportunities · Thought leadership · '
 'Europe · APAC. These are target-domain terms, not claimed forensic practice credentials.')

# ------------------------------------------------------------ side 4
FIRST90 = [('Days 1–30',
  'Learn the portfolio with forensic specialists; clarify reporting line, commercial mandate and '
  'priority countries. Review approved case studies, delivery capacity and existing pipeline. '
  'Complete sector and compliance onboarding; agree one market and one proposition for a pilot.'),
 ('Days 31–60',
  'With a country sponsor, validate buyer needs and draft the proposition, demo and pursuit plan. '
  'Agree evidence, pricing assumptions, quality gates and a delivery owner. Run enablement '
  'sessions tied to real opportunities, not general technology training.'),
 ('Days 61–90',
  'Support the first qualified pursuit and assess pilot adoption against a baseline. Review '
  'pipeline movement, country participation and delivery readiness. Revise the playbook and '
  'propose expansion only where specialist capacity and buyer evidence support it.'),
 ('Months 3–6',
  'Extend proven assets to additional European markets and assess APAC readiness with local '
  'leadership. Report actual wins, revenue attribution and technology use separately from '
  'activity; no unsubstantiated growth commitment.')]

PARTNER = [('Country Forensics leaders and Regional leadership',
  'Agree market priorities and account ownership. Make sponsorship, resources and next client '
  'decisions visible; country relationships remain central.'),
 ('Forensic specialists and delivery teams',
  'Validate propositions, demos and quality boundaries. Include delivery capacity and evidence '
  'requirements before a proposal is committed.'),
 ('Clients and opportunity teams',
  'Start with the buyer problem, establish the value hypothesis and clarify procurement, '
  'confidentiality and success criteria. Avoid unsupported AI promises.'),
 ('Global and APAC stakeholders',
  'Share approved materials, capability and cross-border opportunities. Adapt to local regulation '
  'and operating models rather than copying a European playbook unchanged.')]


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

    m.models_table("PROPOSED MARKET ACTIVATION MODEL",
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

    m.section("TARGET PORTFOLIO AND COMMERCIAL REMIT")
    m.para(KEYWORDS, after=80)

    # afsluttende side
    m.page_break()
    m.models_table("FIRST 90 DAYS — HOW I WOULD TAKE OWNERSHIP",
                   ("When", "What is in place"), FIRST90)

    m.section("STAKEHOLDER MODEL — COMMERCIAL OWNERSHIP AND SPECIALIST JUDGEMENT")
    for label, body in PARTNER:
        m.bullet(label, body, after=20)

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

    return m.save(path, title="Application and CV — EY Forensic Solutions Market Activation, 1739349",
                  subject="Associate Director application — market activation and AI adoption",
                  keywords="EY, market activation, forensic solutions, AI, commercial enablement",
                  comments="Stored master design. English. Transferable evidence and sector gaps explicit.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_EY_ForensicMarketActivation.docx")
    build(out)
    print("OK " + out)
