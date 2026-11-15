# -*- coding: utf-8 -*-
"""Siemens Gamesa — Functional Lead, Procurement (Finished & Third-Party Blades), Job ID 306541.

English posting → English deliverable (en-GB): application p1, CV p2, education +
90 days + four sections p3, requirement matrix p4.
Angle: a supplier is chosen before the price meeting — when the number of sources and
the contract terms decide who carries the risk of a stopped line.
Policy: master/README.md — job first, candidate only as evidence, no hedges.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Procurement and supplier management · Contracts, cost and delivery'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4 November 2026")
    m.meta("Siemens Gamesa Renewable Energy A/S · Functional Lead, Procurement · Job ID 306541")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Application: Functional Lead, Procurement — Finished and Third-Party Blades",
           bold=True, color='1A1A1A')
    m.para("To the Procurement leadership team in Operations, Siemens Gamesa", after=70)

    # ---------------------------------------------------------------- page 1
    m.para("A supplier is not chosen at the price meeting. It is chosen the day someone decides how many "
           "sources a component will have, which of them carries the risk of a stopped line, and what the "
           "contract says when the volume does not arrive as promised. In blades that decision is made "
           "years before the first mould is qualified — and it is the decision this role owns.", after=80)

    m.para("**Make-or-buy is a capacity decision before it is a cost comparison.** What a company keeps "
           "inside is what it can control when the schedule slips; what it buys is what it has to be able "
           "to specify, inspect and hold to account. I have made that call in my own business every month — "
           "carry the electricians and apprentices, or buy the trade — and I have bought the trade on eleven "
           "concurrent projects where a **late delivery was not an inconvenience but a stopped site**. The "
           "arithmetic only works if the supplier's capacity, not just the price, is part of the "
           "calculation.", after=80)

    m.para("**A single source is a decision with a date on it.** One supplier is cheaper until it is not: "
           "the qualification is paid once, and the exposure is carried for the life of the programme. A "
           "portfolio that holds a regional option and a second source costs more on paper and less in "
           "reality, because the alternative to dual sourcing is a line standing still while a commercial "
           "discussion is settled. That is the trade I would defend in a **Make-or-Buy** review: not the "
           "lowest quote, but the lowest exposure over the years the component is needed.", after=80)

    m.para("**Contracts are written for the day something goes wrong.** I have worked with **AB 18** and "
           "**ABT 18**, total-enterprise structures, subcontractor agreements, warranties and variations, "
           "and I have negotiated both as buyer and as supplier — which is the fastest way to learn which "
           "clauses get tested. A **Master Purchase Agreement** or a **Development Agreement** is the same "
           "craft at a larger scale: scope, volumes, price mechanism, change control, quality gates, "
           "liability and exit, agreed while everyone is still friendly.", after=80)

    m.para("**Cost transparency is worth more than a discount.** A price is one number; cost is the "
           "freight, the rework, the expediting, the downtime and the engineering hours spent chasing. I "
           "have costed work from the bottom up — hours, materials, access, risk — followed it with "
           "**after-calculation** per job and tracked **gross margin** per customer and per job type, so "
           "the next quote was sharper than the last. In **SAP ERP** the same discipline shows up as one "
           "version of the numbers for purchasing, projects and finance.", after=80)

    m.para("**Supplier performance is managed between reviews, not at them.** A supplier who is late once "
           "is a data point; a supplier who is late every month is a decision nobody took. I work with a "
           "short set of measures — **on-time delivery**, quality at receipt, response time on the things "
           "that stop a job — reviewed monthly with the supplier's own people, escalated early and "
           "documented, and followed up with root-cause work (**5xWhy**, **Ishikawa**) rather than a "
           "renewed promise.", after=80)

    m.para("**Quality standards are how you see a manufacturing process from the outside.** I have worked "
           "to **GMP/FDA/EMA** requirements and to **FAT/SAT** and **IQ/OQ/PQ**, which means I have stood in "
           "a supplier's works, read their process documentation, agreed hold points and refused an "
           "acceptance that was not evidenced — and closed projects with **zero critical findings**. That "
           "is the same discipline a blade supplier qualification demands: the process is qualified before "
           "the product is, and the paperwork is the proof.", after=80)

    m.para("**Procurement delivers through other people's priorities.** At Novo Nordisk I coordinated **37 "
           "capital projects** with **25 specialists** across engineering, purchasing, quality and site, "
           "and the projects that ran well were the ones where the buyer was in the room when the "
           "specification was written. I have worked in Danish and English, in Tehran and in Copenhagen, "
           "with suppliers and colleagues from different cultures and technical traditions — and the rule "
           "does not change: say what you need, in writing, early enough to be useful.", after=80)

    m.para("**Leading a procurement team is leading experts.** A category lead knows more about the market "
           "than the manager does, and the manager's job is to make that knowledge usable: clear mandates, "
           "honest reviews, a development plan per person and cover when someone is away. I have led teams "
           "of **5, 12, 14 and 25** with **MUS/GRUS** reviews, **competence matrices** and training booked "
           "from the matrix rather than from memory — and I have coached people into roles they did not "
           "think they were ready for.", after=80)

    m.para("**Siemens Gamesa is where that discipline meets a market that will not wait.** Blades are the "
           "longest lead item in the turbine and the hardest to move between suppliers, so the portfolio "
           "decisions taken now decide the delivery performance of 2029. What I bring is the commercial "
           "craft, the cost discipline and the supplier management; and a blade is exactly the kind of product "
           "where the process is the quality — the conversation I know how to have with a supplier. I am "
           "based in Måløv, prepared to work "
           "from **Aalborg** and to travel to Pamplona and Shanghai, and available at short notice.",
           after=70)
    m.meta("Yours sincerely", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFILE")
    m.para("Commercial and technical leader with 20+ years in operations, purchasing and supplier "
           "management — **elautoriseret maskinmester (LV/MV/HV)** by trade, with full P&L responsibility "
           "since 2023. Has bought and managed suppliers on **11 concurrent projects** and across **37 "
           "capital projects** with 25 specialists, negotiated under **AB 18** and **ABT 18**, and worked "
           "to **GMP/FDA/EMA** quality standards with **FAT/SAT**, **IQ/OQ/PQ** and **zero critical "
           "findings**. Runs purchasing, order book and stock in **SAP ERP**, builds cost and KPI models in "
           "**Power BI** and **Python**, and has led teams of **5, 12, 14 and 25**. English and Danish; "
           "available at short notice.", after=80)

    m.section("PROCUREMENT, SUPPLIERS AND CONTRACTS")
    for label, body in [
        ("Sourcing and supplier portfolio",
         "Supplier selection for installation, ventilation and electrical packages on 11 and 37 concurrent "
         "projects: capacity checked before price, a second source kept alive on anything that could stop a "
         "site, and the portfolio reviewed as risk."),
        ("Negotiation and contract management",
         "AB 18, ABT 18, total-enterprise and subcontractor agreements negotiated as buyer and as supplier; "
         "scope, price mechanism, change control, quality gates, warranty and liability agreed in writing."),
        ("Cost transparency and value creation",
         "Bottom-up costing of hours, materials, access and risk with after-calculation per job and gross "
         "margin per customer and job type; savings found in total cost, not in a discount on the invoice."),
        ("Supplier performance management",
         "On-time delivery, quality at receipt and response time measured monthly with suppliers; root-cause "
         "work on repeat deviations, escalation documented and development plans where justified."),
        ("Quality and manufacturing process",
         "Supplier acceptance through FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA: process documented before "
         "product, hold points witnessed and acceptance refused when it was not evidenced."),
    ]:
        m.bullet(label, body, after=25)

    m.section("EXPERIENCE")
    jobs = [
        ("Owner / Technical Director",
         "ELOHVAC ApS · Copenhagen · May 2023–present",
         "5 electricians + 3 apprentices · full P&L · purchasing, suppliers and contracts",
         [("Purchasing, suppliers and margin",
           "Supplier selection and negotiation for every project; orders, deliveries and stock in SAP ERP, "
           "with gross margin per customer and per job type reported monthly and used to steer the next "
           "quote."),
          ("Team, quality and safety",
           "Daily leadership of five electricians and three apprentices, competence matrix and apprentice "
           "assessments, LOTO and risk assessment at site start-up; zero critical deviations in the service "
           "agreements.")]),
        ("Senior Commissioning Engineer / Project Manager, Electrical Systems",
         "Novo Nordisk A/S · Kalundborg/Bagsværd, Denmark · Nov 2022–Jul 2024",
         "37 capital projects · 25 specialists · GMP/FDA/EMA validated environment",
         [("Buyer-side interface and cross-functional delivery",
           "Specification, purchasing, quality and site aligned on 37 concurrent projects; supplier "
           "documentation and delivery dates verified against the contract, and escalation handled before "
           "the programme moved."),
          ("Acceptance and supplier quality",
           "FAT/SAT and IQ/OQ/PQ with witness points, punch close-out and handover documentation; supplier "
           "audits at the works, projects closed with zero critical findings.")]),
        ("Project and Workshop Manager",
         "Ventek-Air · Copenhagen · Jan 2022–Nov 2022",
         "14 employees · 11 concurrent projects · DKK 2–10m per project",
         [("Subcontractors and programme",
           "11 ventilation projects from specification to handover with 14 people; subcontractor scope, "
           "agreements, deliveries and capacity controlled against the programme at daily board meetings.")]),
        ("Operations and Maintenance Manager",
         "Lynetten under Biofos · Copenhagen · Aug 2017–Jan 2022",
         "Critical plant in 24/7 operation · spare parts, store, HVAC and HV switchgear",
         [("Spare parts and supply risk",
           "Critical spares held against failure, minimum and maximum levels set from consumption and "
           "suppliers measured on delivery; 5S and standard work on store and workshop."),
          ("Safety and records",
           "LOTO, APV risk assessment, near-miss follow-up and toolbox talks; documentation produced with "
           "the work, not after it.")]),
        ("Electromechanical Technician / Production Team Leader",
         "ARJ Engineering · Tehran · Dec 2003–Mar 2010",
         "12 mechanics and technicians · machine workshop · industrial plant",
         [("Materials, suppliers and output",
           "Materials, tools and spare parts bought and controlled against the week's plan, with output "
           "measured per person and per machine across 12 technicians.")]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.page_break()
    m.section("EDUCATION AND AUTHORISATION")
    m.edu("B.Tech, Technology Management and Mechanical Engineering",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7.6/12")
    m.edu("Electrical and Mechanical Engineering Design, Electrical Engineering (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("Danish HV/LV authorisation — elautoriseret maskinmester (LV/MV/HV)",
          "Danish Safety Technology Authority · May 2023")
    m.edu("Refrigeration and air-conditioning (AMU) · Lean practice: 5S, PDCA, A3, standard work",
          "Mercantec · 2021 · applied in operations and procurement follow-up")

    m.section("LANGUAGES, PRACTICALITIES AND REFERENCES")
    m.para("**English: professional**, written and spoken, for contracts, negotiations and documentation · "
           "Danish: native · Persian: native · **Based in Måløv, Greater Copenhagen**, prepared to work "
           "from Aalborg and to travel to Pamplona and Shanghai · Full driving licence · Available at short "
           "notice · References on request.", after=70)

    m.models_table("THE FIRST 90 DAYS — PORTFOLIO, CONTRACTS AND COST",
                   ("Period", "What happens, and how it is measured"), [
        ("Week 1–2",
         "Read the Make-or-Buy strategy, the blade category plan and the existing agreements; meet the "
         "category leads and the internal customers in engineering, quality and operations; map spend, "
         "suppliers and single-source exposure for finished and third-party blades."),
        ("Day 30",
         "A one-page view of the portfolio: who supplies what, where the second source is real and where it "
         "is on paper, and which contracts expire or come up for renegotiation in the next twelve months; "
         "KPI definitions agreed with suppliers and with internal stakeholders."),
        ("Day 60",
         "Sourcing plan for the coming year agreed with engineering and operations — regional options, "
         "qualification pipeline, negotiation calendar; cost transparency built on a should-cost model per "
         "component family instead of last year's price."),
        ("Day 90",
         "Supplier performance reviewed face to face with the strategic suppliers on delivery, quality and "
         "response; a development plan per strategic supplier with named owners and dates; and the "
         "value-creation targets for the year documented in a way that can be measured monthly.")])

    m.section("A SUPPLIER IS A DEPENDENCY, NOT A LINE IN THE LEDGER")
    m.para("Every purchase is a decision to depend on somebody, and the only question is whether that "
           "dependency is understood. The failures I have seen — and paid for — were not caused by a bad "
           "price; they were caused by a single source nobody had challenged, a capacity assumption nobody "
           "had verified, or a contract that was silent on the one thing that then happened. So the first "
           "work in a new category is not a tender: it is finding out which dependencies the business is "
           "actually carrying, and which of them it has chosen to carry.", after=80)

    m.section("THE WORST COST IS THE LINE THAT STOPS")
    m.para("A component that arrives late costs the difference between the quoted price and the expedited "
           "one; a component that is not available costs the shift, the turbine and the customer's "
           "confidence. That is why I argue for cost transparency rather than a discount: the number that "
           "matters is the total cost of the supply over the programme, including freight, inspection, "
           "rework, expediting and the engineering hours spent chasing. A supplier who is two per cent "
           "more expensive and predictable is usually the cheaper supplier.", after=80)

    m.section("A CONTRACT IS A PLAN FOR DISAGREEMENT")
    m.para("Nobody negotiates the clause they need on the day they sign it; they need it eighteen months "
           "later, when the volume dropped, the specification changed or the quality slipped. So a Master "
           "Purchase Agreement should read as a set of agreed answers: what is fixed, what is indexed, what "
           "counts as a change, what evidence closes an acceptance, and what happens if it is not met. I "
           "have negotiated on both sides of that table, and the agreements that held were the ones where "
           "the mechanism was written down rather than the goodwill.", after=80)

    m.section("CROSS-CULTURAL IS A PRACTICE, NOT A VALUE")
    m.para("Working across countries means writing more down and assuming less: an agreed minute after "
           "every review, a single source of truth for the numbers, and a habit of checking that the other "
           "side understood the same thing you did. I have worked in Danish, English and Persian, in Tehran "
           "and Copenhagen, with suppliers who negotiate differently — and the discipline that works "
           "everywhere is the same: be specific, be early, and put the commitment in writing while the "
           "relationship is still good.", after=80)

    m.page_break()

    m.models_table("WHAT THE ROLE REQUIRES — WHAT I HAVE DELIVERED", ("Requirement in the posting", "Evidence"), [
        ('Define and execute the global sourcing strategy for finished and third-party blades',
         'Defined sourcing for installation, ventilation and electrical packages on 11 and 37 concurrent projects with internal customers and suppliers.'),
        ('Align sourcing strategy with the Blades Make-or-Buy strategy',
         'Make-or-buy decided monthly in own business — carry the trade or buy it — with capacity, qualification cost and exposure as the arithmetic.'),
        ('Lead a competitive supplier portfolio with regional and dual-source options to mitigate risk',
         'Second sources kept alive on anything that could stop a site; portfolio reviewed as risk, including single-source exposure and lead time.'),
        ('Own commercial relationships with strategic suppliers and negotiate Development and Master Purchase Agreements',
         'AB 18, ABT 18, total-enterprise and subcontractor agreements negotiated as buyer and supplier: scope, price mechanism, quality gates, liability.'),
        ('Secure competitive pricing and cost transparency and achieve value-creation targets',
         'Bottom-up costing with after-calculation per job and gross margin per customer and job type in SAP ERP; savings built on total cost.'),
        ('Manage supplier performance across cost, quality, delivery and service',
         'On-time delivery, quality at receipt and response time measured monthly with suppliers; repeat deviations taken to root cause, not to a new promise.'),
        ('Collaborate closely with cross-functional teams to enhance supplier performance',
         '37 projects coordinated with engineering, purchasing, quality and site; the buyer in the room when the specification was written.'),
        ('Keep a keen eye on market trends and supplier capabilities',
         'Capacity and capability checked at the supplier, not in the tender: site visits, process documentation and a view of who can still deliver in two years.'),
        ('Substantial experience in strategic procurement or supplier management in an engineering-intensive or manufacturing environment',
         '20+ years in technical operations and contracting: purchasing, subcontractor agreements and supplier follow-up on projects of DKK 2–10m and capital projects.'),
        ('Proven ability to drive results through strategic supplier partnerships and cross-cultural collaboration',
         'Supplier relationships built over years in own business; work in Danish, English and Persian, in Tehran and Copenhagen, with suppliers across countries.'),
        ('Strong track record in commercial negotiations, contract management and supplier development',
         'Negotiated as buyer and as supplier under AB 18/ABT 18; supplier development through measured reviews, root-cause work and agreed improvement plans.'),
        ('Experience in leading and coaching international procurement teams and fostering professional growth',
         'Led 5, 12, 14 and 25 people with MUS/GRUS reviews, competence matrices, team development plans and training booked from the matrix.'),
        ('Sound understanding of manufacturing processes, quality standards and supply-chain risk management',
         'FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA with zero critical findings; process documentation, hold points and acceptance evidence as the basis for approval.'),
        ('Wind-industry experience, specifically blade or composite, is a plus',
         'Not from wind or composites; the process discipline comes from validated manufacturing (GMP) and supplier acceptance at the works.'),
    ], widths=(3600, 7046))

    m.section("A SECOND SOURCE IS QUALIFIED BEFORE YOU NEED IT")
    m.para("Dual sourcing fails when it is decided in a crisis, because qualifying a supplier takes longer than "
           "the crisis lasts: samples, process approval, first-article inspection and a ramp-up that has to be "
           "witnessed. So the second source belongs in the annual plan with a date and a budget, not on a "
           "slide in a risk workshop. The honest question in a Make-or-Buy review is not whether a second "
           "source is affordable, but whether the programme can survive without one — and the cost of spare "
           "capacity is visible, while the cost of the capacity that is not there is not.", after=80)

    m.section("THE ROLE SITS IN AALBORG, AND I AM PREPARED TO BE THERE")
    m.para("The role sits in Aalborg with interfaces to Pamplona and Shanghai, and I am based in Måløv. I am "
           "prepared to work from Aalborg, and the practical arrangement — how the week is split and how "
           "much of the interface is run remotely — is something I would want agreed early rather than "
           "discovered. Procurement is a job done face to face at the supplier and at the internal "
           "customer, so I would expect to travel; I would rather say that now than in month three.",
           after=80)

    return m.save(path, title="Functional Lead Procurement — Siemens Gamesa",
                  subject="Supplier portfolio, contracts, cost and delivery",
                  keywords="procurement, supplier management, sourcing strategy, negotiation, contract "
                           "management, make or buy, cost transparency, supplier performance, sap, "
                           "siemens gamesa, denmark")


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_SiemensGamesa_FunctionalLeadProcurement.docx')))
