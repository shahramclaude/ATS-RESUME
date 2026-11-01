# -*- coding: utf-8 -*-
"""Prysmian R-36374 — English combined application and CV in stored master design."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = 'Sr Sales Manager Denmark | Prysmian | Profitable growth and technical customer value'
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv, Denmark")
DATE = '1 November 2026'
RECIPIENT = 'Prysmian · Att: Sales Director Sweden & Denmark / Recruitment'
SUBJECT = 'Application: Sr Sales Manager Denmark — R-36374'

# ------------------------------------------------------------------ side 1
INTRO = ['Profitable growth in the Danish cable market requires more than a competitive price per metre. '
 'Customers need the right technical choice, dependable availability and a commercial agreement '
 'that works through quotation, delivery and installation. Prysmian’s opportunity is to turn those '
 'requirements into stronger key accounts and new business without buying revenue through margin '
 'erosion.',
 'The proposed commercial system starts with a market and account map, a qualified opportunity '
 'pipeline and a pricing discipline linked to actual cost-to-serve. It connects customer needs to '
 'technical support, supply chain and delivery capacity, so the promise made in the negotiation is '
 'the experience the customer receives.']

BULLETS = [('The requirement: develop and execute the Danish sales strategy',
  'The response is a market plan agreed with the Sales Director Sweden & Denmark: priority '
  'customer segments, addressable needs, competitive position and account actions. Wholesalers, '
  'contractors, installers, utilities and industrial buyers require different propositions and '
  'decision routes; priorities should follow evidence and accessible opportunities.'),
 ('The requirement: drive revenue, profitability and market share',
  'The response is an account-level growth bridge distinguishing retention, cross-selling, new '
  'business and price/mix. Revenue is reviewed with contribution margin and cost-to-serve, not in '
  'isolation. Market share claims require a credible market baseline; until that exists, report '
  'internal sales performance and qualified customer evidence separately.'),
 ('The requirement: pursue new business opportunities',
  'The response is a prospecting rhythm built around customer projects, buying triggers and unmet '
  'requirements. Each opportunity has an owner, buying process, scope, timing, value hypothesis '
  'and next action. A bid/no-bid review prevents activity from becoming an unqualified quotation '
  'backlog.'),
 ('The requirement: develop key accounts and customer relationships',
  'The response is an account plan with stakeholder map, current business, growth potential, '
  'service issues and agreed next steps. Regular customer reviews address availability, '
  'specification, delivery and technical support. Installer-side experience helps translate '
  'product capability into what matters on site, without assuming an existing manufacturer-level '
  'buyer network.'),
 ('The requirement: lead negotiations and commercial agreements',
  'The response is a negotiation brief covering value, margin floor, volume assumptions, payment '
  'terms, delivery commitments and escalation. Concessions are exchanged for defined commitments '
  'rather than given away. Quotation validity and any relevant material-price adjustment mechanism '
  'are clarified with Prysmian’s commercial rules before an offer is approved.'),
 ('The requirement: understand trends, customer needs and competition',
  'The response is a structured market log: demand signals, lost-order reasons, competitor '
  'propositions and specification requirements. Technical conversations cover application, '
  'installation constraints and relevant cable/fire-performance documentation, validated by '
  'specialists. Customer insight feeds account priorities rather than remaining anecdotal.'),
 ('The requirement: work across functions to deliver growth',
  'The response is a shared opportunity-to-order review with sales, technical support, supply '
  'chain and finance. Long-lead or non-standard needs are assessed before commitments are made; '
  'open issues have an owner and date. Excellent customer experience depends on a deliverable '
  'promise, not only on a persuasive proposal.'),
 ('The requirement: analytical, hands-on commercial leadership',
  'The response is a weekly pipeline and account-action review and a monthly performance '
  'conversation covering revenue, margin, conversion, forecast and delivery concerns. Power BI and '
  'Python support analysis; Claude helps structure research, proposals and follow-up under '
  'approved data rules, with human verification of all customer-facing claims.')]

SYSTEM = ('The working toolkit is an account segmentation model, key account plan, opportunity '
 'qualification checklist, negotiation brief and growth/margin dashboard. Targets and baselines '
 'would be agreed after reviewing the existing Danish business. The aim is a repeatable commercial '
 'rhythm that strengthens relationships and profitable delivery, not a reporting layer detached '
 'from customers.')

MIRROR = ('Relevant evidence: authorised electrical engineer (LV/MV/HV), technical installation experience, '
 'full P&L and client-facing contracting responsibility in ELOHVAC, quotations and subcontractor '
 'coordination, and multidisciplinary leadership across engineering, procurement and site '
 'operations. Professional Claude user and coder with Python/Claude API tools and a documented '
 'productivity improvement above 40%.')

HONEST = ('The commercial experience is in an electrical contracting business, not a cable manufacturer’s '
 'national sales organisation. A proven Danish wholesale key-account portfolio, an established '
 'utilities buyer network, quantified sales-growth or market-share wins, and leadership of a '
 'dedicated B2B sales team are not established by my CV. The application offers technical customer '
 'insight, P&L ownership and disciplined execution as transferable strengths, not a substitute '
 'sales track record.')

CULTURE = ('Prysmian’s published Connect, to Lead strategy connects cabling solutions to the energy '
 'transition and digital transformation, with value-added services and long-term partnerships. The '
 'commercial implication is to sell a dependable solution rather than a cable specification alone. '
 'The role’s emphasis on inclusion also means making room for different specialist perspectives '
 'before committing to the customer.')

PRACTICAL = ('Based in Måløv, Denmark; Albertslund is a practical local work location. Native Danish, '
 'professional English and native Persian/Farsi; driving licence B. Hybrid arrangements, any '
 'Nässjö travel and start date would be agreed. Arrangements for ELOHVAC would be settled before '
 'appointment.')

CLOSING = ('A useful first discussion would review one priority account: where is the growth opportunity, '
 'what prevents the next order, and what commitment would make the customer relationship both '
 'stronger and more profitable?')

# ------------------------------------------------------------------ CV
PROFILE = ('Prysmian’s Danish sales remit calls for profitable growth, key account development and '
 'deliverable customer commitments. Transferable experience combines electrical contracting with '
 'full P&L, quotations, customer delivery and technical installation knowledge. Authorised '
 'electrical engineer (LV/MV/HV), B.Tech in Technology Management & Mechanical Engineering, with '
 'practical understanding of electrical works and multidisciplinary project coordination. '
 'Professional Claude user and coder, using Python/Claude API tools for estimates, planning, '
 'checklists and KPI reporting. This is a move from contracting into manufacturer-side sales '
 'leadership, not a claim of an established national cable-sales portfolio. Relevant strengths are '
 'customer-side technical insight, commercial ownership and data-supported follow-through.')

PRACTICE = [('Commercial acumen — B2B ownership evidence',
  'ELOHVAC: quotations, calculations, materials, subcontractors, quality assurance and handover '
  'with full P&L. Relevant to commercial accountability and client delivery; not presented as '
  'national cable-channel sales leadership.'),
 ('Technical customer understanding — evidence',
  'Electrical installation, distribution boards, controls, fault-finding and HVAC interfaces. An '
  'installer-side view of practical product selection and delivery requirements, supported by '
  'LV/MV/HV authorisation.'),
 ('Account development — proposed approach',
  'Segment accounts by current business, potential and service needs. Map decision-makers, '
  'understand buying criteria and agree a customer review cadence. Danish wholesale relationships '
  'and utility buyer access must be developed, not presumed.'),
 ('Negotiation and margin — proposed approach',
  'Prepare value case, scope, alternatives, margin boundaries and delivery terms before '
  'negotiations. Relate concessions to commitments; validate non-standard terms with the '
  'appropriate commercial authority.'),
 ('Stakeholder management and communication — evidence and application',
  'Experience coordinating 25 specialists and 11 parallel installation projects. Apply clear '
  'interfaces and decision ownership between sales, technical support, supply chain and finance.'),
 ('Data-driven commercial analytics and AI — evidence',
  'Python/Claude API tools for estimates, planning and KPI, with productivity improvement above '
  '40%. Proposed sales application: pipeline hygiene, win/loss analysis and account action '
  'tracking under approved confidentiality rules.')]

MODELS = [('Market and segment plan',
  'Customer needs, buying channels, accessible opportunities and competitor propositions; '
  'prioritised account actions agreed with the Sales Director Sweden & Denmark.'),
 ('Key account plan',
  'Stakeholder map, current business and potential, buying criteria, service concerns, '
  'cross-selling opportunities and named next actions.'),
 ('Qualified pipeline',
  'Stage definitions, decision process, scope, expected value, timing, margin assumptions and next '
  'action; forecast reviewed against evidence, not optimism.'),
 ('Negotiation discipline',
  'Client value and alternatives, margin floor, volume and delivery assumptions, terms and '
  'concession exchange; approval boundaries for commercial agreements.'),
 ('Delivery and customer experience',
  'Opportunity-to-order handoff, technical validation, availability and lead-time checks, issue '
  'ownership and customer follow-up.'),
 ('Performance review',
  'Revenue and contribution margin, mix, conversion, forecast quality and service concerns; market '
  'share tracked only against a substantiated market baseline.')]

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

PRACTICAL_CV = ('Based in Måløv, Denmark; driving licence B. Native Danish and Persian/Farsi, professional '
 'English. Albertslund is a practical local work location; hybrid arrangements and travel '
 'connected with Nässjö to be agreed. Start date and arrangements for the existing business '
 'settled before appointment.')

REFERENCES = 'Former managers at Novo Nordisk A/S and Biofos (Lynetten) — available on request.'

KEYWORDS = ('Target sales remit: Sales strategy · Revenue growth · Profitability · Market share expansion · '
 'Business development · Key account management · Strategic negotiations · Commercial agreements · '
 'Customer experience · Market trends · Competitor activities · Cross-functional teams · B2B · '
 'Electrical · Cable · Infrastructure · Construction · Industrial sectors · Danish electrical '
 'distribution market · Wholesalers · Contractors · Installers · Utilities · Technical products · '
 'Solution-based offerings. Channel terms describe the target market, not a claimed established '
 'buyer network.')

# ------------------------------------------------------------ side 4
FIRST90 = [('Days 1–30',
  'Learn the Danish portfolio, customer base, pricing rules and supply chain with the Sales '
  'Director and specialists. Review existing pipeline, margin and service issues. Visit priority '
  'customers and agree the first account/market baseline.'),
 ('Days 31–60',
  'Complete segmentation and plans for agreed priority accounts. Qualify new opportunities and '
  'test a proposition with technical and supply-chain colleagues. Introduce a concise pipeline '
  'rhythm and negotiation brief using existing Prysmian systems.'),
 ('Days 61–90',
  'Review first qualified pursuits, customer feedback and forecast accuracy. Identify where '
  'delivery, specification or commercial terms block conversion. Agree evidence-based targets and '
  'a focused growth plan rather than promising ungrounded market-share gains.'),
 ('Months 3–6',
  'Expand account actions and prospecting where customer evidence supports it. Report actual '
  'orders, profitability and relationship progress separately from activity. Feed market learning '
  'into the joint Sweden/Denmark commercial organisation.')]

PARTNER = [('Sales Director Sweden & Denmark',
  'Agree priorities, targets, approval boundaries and forecasts. Present commercial choices with '
  'customer evidence, margin implications and next decisions.'),
 ('Key customers and industry stakeholders',
  'Listen to how products are specified, bought and installed. Build trust through technically '
  'validated advice, clear agreements and dependable follow-up.'),
 ('Technical support and supply chain',
  'Bring application requirements and project timing into discussions before quoting. Resolve '
  'availability and non-standard specification questions before committing.'),
 ('Finance and wider commercial teams',
  'Maintain a common view of pricing, margin and terms. Share opportunities and customer feedback '
  'while respecting account ownership and data confidentiality.')]


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

    m.section("TARGET MARKET AND COMMERCIAL REMIT")
    m.para(KEYWORDS, after=80)

    # afsluttende side
    m.page_break()
    m.models_table("FIRST 90 DAYS — HOW I WOULD TAKE OWNERSHIP",
                   ("When", "What is in place"), FIRST90)

    m.section("CUSTOMER VALUE — CROSS-FUNCTIONAL RESPONSIBILITIES")
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

    return m.save(path, title="Application and CV — Prysmian Sr Sales Manager Denmark, R-36374",
                  subject="Sales strategy, profitable growth and key account development",
                  keywords="Prysmian, sales strategy, electrical, B2B, key accounts, commercial leadership",
                  comments="Stored master design. English. Transferable evidence and sector gaps explicit.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_Prysmian_SrSalesManagerDenmark.docx")
    build(out)
    print("OK " + out)
