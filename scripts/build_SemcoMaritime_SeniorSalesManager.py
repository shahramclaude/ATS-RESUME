# -*- coding: utf-8 -*-
"""
Semco Maritime — Senior Sales Manager, Renewables Service.
English JD. One combined document: task-first page 1 + CV in the master design.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Senior Sales Manager | Renewables Service | Offshore wind and technical service"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv, Denmark")

DATE = "31 October 2026"
RECIPIENT = ("Semco Maritime A/S · Esbjerg Brygge 30, 6700 Esbjerg · Renewables Division / "
             "Renewables Service")
SUBJECT = "Application: Senior Sales Manager for Renewables Service"

# ------------------------------------------------------------------ page 1
INTRO = [
    "The job is to turn technical capability into signed, profitable service contracts: qualify early, "
    "run the tender with a strategy that has already decided why we win, negotiate terms that still make "
    "sense two years into execution, and hand over an award operations can deliver. In offshore wind "
    "service, the difference between a good and a bad contract is decided long before the signature — in "
    "the qualification, the scope and the risk review.",

    "Below is how I read the role and the system that stands ready from day one: a qualified pipeline with "
    "go/no-go criteria, a bid model linking win themes to cost and risk, an account plan with a decision "
    "map, a negotiation brief with fallbacks agreed in advance, and a handover pack signed off by "
    "operations.",
]

BULLETS = [
    ("Requirement: end-to-end ownership of strategic sales opportunities — from qualification to award "
     "and handover",
     "The answer is project ownership as a discipline: 37 capital projects of EUR 0.3–1.3m each, run end "
     "to end from requirement and specification through supplier selection, negotiation, delivery and "
     "acceptance, with no critical findings at handover. A sales process is a project with a decision at "
     "the end."),

    ("Requirement: developing and executing winning strategies for key tenders",
     "The answer is a bid model that decides the win before the price: customer pain and selection "
     "criteria mapped, win themes attached to each criterion, a price-to-win view, a risk register with "
     "owners and a governance gate before submission — so the team writes to a strategy, not a template."),

    ("Requirement: building relationships with strategic customers and developing key accounts",
     "The answer is an account plan per customer: their decision process and stakeholders, the services "
     "we can grow into, the next three opportunities and what we owe them before the next conversation. "
     "I have carried 40+ service accounts, where the renewal was won in the twelve months before the "
     "contract ran out."),

    ("Requirement: leading customer negotiations with technical, operational, legal, procurement and "
     "finance stakeholders",
     "The answer is preparation: a brief with target, fallback and walk-away agreed internally, technical "
     "scope frozen before commercial terms, and change orders priced before the work starts — so the margin "
     "is not negotiated away during delivery."),

    ("Requirement: growth through cross-selling, upselling and framework agreements",
     "The answer is a service ladder: what the customer buys today, what the next natural service is, and "
     "a framework agreement that makes it easy to say yes. I have built recurring agreements in a business "
     "where the alternative was one-off call-outs."),

    ("Requirement: high-quality commercial proposals, risk assessments and governance approvals",
     "The answer is a proposal that can be defended: scope and assumptions written down, cost model "
     "traced to them, risks quantified with owners, and an approval pack a director can read in ten "
     "minutes — in GMP/FDA/EMA environments an unsupported claim is not an option."),

    ("Requirement: promoting a strong culture of safety, quality, compliance and integrity",
     "The answer is that safety is a commercial argument, not a slide: LOTO, permits to work, risk "
     "assessments and near-miss reporting are how we keep the right to operate on an offshore asset — and "
     "how we win the next contract. I have worked in 24/7 operations where a shortcut was never cheaper."),
]

SYSTEM = ("The system is already built: qualified pipeline with go/no-go criteria, bid model linking win "
          "themes to cost and risk, account plans with decision maps, negotiation briefs with fallbacks "
          "agreed, handover packs signed off by operations and a dashboard for pipeline value, hit rate "
          "and margin — in Excel and Power BI, with Python and Claude for analysis.")

MIRROR = ("On the requirements: 20 years of commercial and technical ownership — full P&L with 5 "
          "electricians, 3 apprentices and 40+ service accounts, 37 capital projects (EUR 0.3–1.3m) with "
          "25 specialists coordinated, 24/7 operations with zero unplanned stops for five years; "
          "authorised marine and electrical engineer (LV/MV/HV), B.Tech in Technology Management & "
          "Mechanical Engineering.")

HONEST = ("Two things said plainly: I have not sold offshore wind service before, and I have not held a key "
          "account role inside a large B2B sales organisation. What I bring is the other half of the job — "
          "commercial ownership of a technical business, where every contract had to be delivered by people "
          "I led, at a margin I answered for.")

CULTURE = ("Why Semco Maritime: change as a journey and answers from pragmatic solutions is exactly "
           "where service contracts are won or lost — in the details of scope, access, response time and "
           "risk that somebody has to be willing to commit to. Safety as a core value is a commercial "
           "position too: the customers who care most about their assets ask hardest about ours.")

PRACTICAL = ("Practical: based in Måløv, 25 minutes from Copenhagen Airport and 30 minutes from a "
             "Copenhagen office; driving licence B; fluent English and Danish; up to 30 travel days a year "
             "is fine; own company will be wound down upon employment.")

CLOSING = ("I would like to hear how you qualify an opportunity today, where you see the Renewables "
           "Service pipeline coming from over the next two years, and what a new Senior Sales Manager "
           "should have achieved after twelve months to be called a success.")

# ------------------------------------------------------------------ CV
PROFILE = ("The role needs three things at once: someone who can qualify and win complex B2B "
           "opportunities, someone who understands what it costs to deliver the contract afterwards, and "
           "someone who can hold a customer relationship for years. All three have been my working day "
           "for 20 years: full P&L in my own technical service company with 5 electricians, 3 apprentices "
           "and 40+ service accounts; 37 capital projects (EUR 0.3–1.3m) with 25 specialists coordinated "
           "under GMP/FDA/EMA requirements; and 24/7 operations with zero unplanned stops for five years. "
           "Authorised marine and electrical engineer (LV/MV/HV), B.Tech in Technology Management & "
           "Mechanical Engineering.")

PRACTICE = [
    ("Commercial ownership",
     "P&L accountability, pricing and margin follow-up, tender and quotation work, supplier and "
     "subcontractor agreements, and a monthly review of pipeline, hit rate and delivery cost."),
    ("Opportunity and tender management",
     "Qualification with go/no-go criteria, bid plan with win themes per selection criterion, "
     "price-to-win view, risk register with owners and a governance gate before submission."),
    ("Contract negotiation",
     "Target, fallback and walk-away agreed before the meeting; technical scope frozen early; terms for "
     "response time, availability, liability and payment negotiated with legal and finance input."),
    ("Key account management",
     "Account plans with decision maps and stakeholder roles, quarterly reviews, service ladders for "
     "upselling and framework agreements that convert one-off work into recurring revenue."),
    ("Technical service delivery",
     "24/7 service on electrical and mechanical installations: response times, maintenance plans, "
     "critical spares, root cause and reporting the customer can put in front of their board."),
    ("Risk, compliance and safety",
     "Risk assessments, permits to work and LOTO, quality documentation and audit readiness; "
     "GMP/FDA/EMA environments where claims must be evidenced."),
    ("Cross-functional leadership",
     "Bid teams across engineering, operations, procurement, legal and finance; 25 specialists "
     "coordinated in 37 parallel projects, with one plan and one reporting line to the customer."),
]

MODELS = [
    ("Pipeline",
     "Qualification scorecard with go/no-go criteria, stage gates from lead to award, CRM hygiene, "
     "pipeline value and hit rate reviewed monthly"),
    ("Bid",
     "Win themes per selection criterion, price-to-win analysis, cost model traced to scope and "
     "assumptions, risk register with owners, approval pack before submission"),
    ("Negotiation",
     "Brief with target, fallback and walk-away; scope freeze; term sheet review with legal and "
     "finance; change orders priced before execution"),
    ("Account",
     "Account plan with decision map and stakeholder roles, service ladder, quarterly review and "
     "framework agreement roadmap"),
    ("Delivery interface",
     "Handover pack signed off by operations: scope, assumptions, cost baseline, risks, contacts and "
     "contractual obligations"),
    ("Safety and compliance",
     "Risk assessment, permits to work, LOTO, near-miss reporting and audit-ready documentation"),
    ("Tools",
     "Excel and Power BI for pipeline and margin, CRM and ERP/SAP, Python and Claude for analysis, "
     "reporting and tender documentation"),
]

ACHIEVEMENTS = [
    ("40+ service accounts and full P&L",
     "built and retained in my own company: recurring service agreements, pricing, renewals and "
     "account development with industrial customers."),
    ("37 capital projects delivered",
     "EUR 0.3–1.3m each, with 25 specialists coordinated — no critical findings at handover under "
     "GMP/FDA/EMA requirements."),
    ("Zero unplanned stops for five years",
     "on a 24/7 utility plant — planned maintenance, root cause discipline and a service model the "
     "customer could rely on."),
    ("+40% productivity and −40% energy cost",
     "documented improvements through measurement, standard work, data-driven planning and my own "
     "AI tooling."),
    ("5 electricians and 3 apprentices led",
     "daily management, competence development and customer relationships — with responsibility for "
     "both the people and the bottom line."),
]

EXPERIENCE = [
    ("Owner / Technical Director / Authorised marine and electrical engineer",
     "ELOHVAC ApS · Copenhagen · May 2023 – present",
     "5 electricians and 3 apprentices · 40+ service installations · full P&L, customers, tenders and "
     "supplier agreements",
     [("Commercial ownership",
       "quotations, pricing, supplier and subcontractor agreements, budget and forecast with full "
       "responsibility for the bottom line."),
      ("Customers and accounts",
       "service agreements and emergency call-outs for commercial customers; renewals, upselling and "
       "long-term relationships built on response time and documentation.")]),

    ("Senior Commissioning Engineer / Project Manager, Electrical Systems",
     "Novo Nordisk A/S · Kalundborg · Nov 2022 – Jul 2024",
     "37 parallel capital projects, EUR 0.3–1.3m · 25 specialists · GMP/FDA/EMA",
     [("Projects and commercial control",
       "plan, budget and reporting to the steering group; 25 specialists and suppliers coordinated "
       "across mechanical, electrical, process and procurement."),
      ("Documentation and handover",
       "requirements, FAT/SAT, IQ/OQ/PQ and validation documentation with deviation handling — zero "
       "critical findings at handover.")]),

    ("Project and Workshop Manager, Ventilation & Climate",
     "Ventek-Air · Copenhagen · Jan 2022 – Nov 2022",
     "14-person production and installation team · 11 parallel projects (EUR 0.3–1.3m)",
     [("Delivery and customer interface",
       "11 parallel contracts with capacity planning, daily board meetings and handover to the client; "
       "scope and change handling agreed in writing before execution.")]),

    ("Head of Operations and Maintenance / Workshop Technician",
     "Biofos (Lynetten) · Copenhagen · Aug 2017 – Jan 2022",
     "24/7 utility plant · pumps, HVAC, switchgear, high voltage and SCADA · SAP budgets",
     [("Service model and KPIs",
       "PDCA-based maintenance plan, failure history and KPIs in SAP; zero unplanned stops for five "
       "years."),
      ("Suppliers and safety",
       "coordination of technicians, contractors and suppliers — LOTO, permits to work, warranty claims "
       "and near-miss reporting.")]),

    ("Electromechanical Technician / Production Team Leader",
     "ARJ Engineering · Tehran · Dec 2003 – Mar 2010",
     "12-person production team · shift planning, material control and stock",
     [("Production team and technical problem solving",
       "shift planning, material control and performance follow-up; repair and diagnostics through "
       "structured root cause analysis.")]),
]

EDUCATION = [
    ("B.Tech (EQF level 6) — Technology Management & Mechanical Engineering",
     "Copenhagen School of Marine Engineering & Technology Management · 2017 – 2022 · grade 7.6/12"),
    ("Electrical & Mechanical Design, Electrical Engineering (EQF level 6)",
     "Tehran Technical University · 2000 – 2003"),
    ("Higher Preparatory Examination — Mathematics and Physics",
     "VUC · 2012 – 2017"),
]

CERTS = [
    ("Authorised marine and electrical engineer (LV/MV/HV)",
     "Danish Safety Technology Authority · May 2023"),
    ("Refrigeration and climate systems (AMU)",
     "Mercantec · Mar 2021"),
    ("Working environment §16 and safety awareness (VI/6-1)",
     "Danish Maritime Authority · May 2021"),
    ("Lean — value stream mapping, standard work, 5S, A3 and Kaizen",
     "Applied in operations and projects · 2017 – present"),
    ("Problem solving — 8-step, A3, DMAIC and Six Sigma tools",
     "Applied in operations and projects · 2017 – present"),
]

LANGUAGES = ("English (professional, written and spoken) · Danish (native) · Persian/Farsi · "
             "Driving licence B")

PRACTICAL_CV = ("Based in Måløv, Denmark — 25 minutes from Copenhagen Airport and about 30 minutes from "
                "a Copenhagen office; driving licence B; up to 30 travel days a year is not a problem; "
                "available at short notice; own company will be wound down upon employment.")

REFERENCES = ("Former managers and business partners at Novo Nordisk A/S (Kalundborg), Biofos "
              "(Lynetten), Ventek-Air and customers of ELOHVAC — available on request.")

PARTNER = [
    ("The customer",
     "One account plan, one point of contact and a quarterly conversation about their assets rather "
     "than our products — because a service contract is renewed long before it expires."),
    ("Operations and engineering",
     "Scope, access and response times agreed with the people who will deliver, before the price is "
     "set; a handover pack they sign, not one they receive."),
    ("Legal, procurement and finance",
     "Terms reviewed early, risks quantified with owners and an approval pack that is short enough to "
     "be read and complete enough to be defended."),
]

FIRST90 = [
    ("Week 1–2",
     "Met the Renewables Service team, tendering, legal and operations; read the current pipeline, "
     "framework agreements and the last three losses. Visited an asset or a service job to see what the "
     "contract actually promises."),
    ("Week 3–6",
     "Qualification scorecard and go/no-go criteria agreed; pipeline reviewed opportunity by opportunity "
     "with the sales team; account plans started for the three most strategic customers."),
    ("Week 7–12",
     "Own bid on a live tender with win themes, price-to-win and a risk register; negotiation brief "
     "standardised; handover pack agreed with operations."),
    ("Month 3–6",
     "Two to three strategic opportunities moved a stage; account plans in use and reviewed quarterly; "
     "pipeline value and hit rate reported monthly."),
    ("Month 6–12",
     "Signed contracts from the strategic pipeline, at margin and with delivery terms operations can "
     "keep; at least one framework agreement or cross-sell developed with an existing customer."),
]

KEYWORDS = (
    "Senior Sales Manager · Renewables Service · Offshore wind · Strategic sales opportunities · "
    "Pipeline · Opportunity identification · Qualification · Tender management · Contract negotiation · "
    "Contract award · Handover · Key account management · Account planning · Customer relationships · "
    "Value proposition · Commercial strategy · Market dynamics · Risk assessment · Governance approvals · "
    "Cross-selling · Upselling · Framework agreements · Commercial proposals · Compliance · Integrity · "
    "Safety · B2B sales · Stakeholders · P&L · Service agreements · Technical service · Response time · "
    "SLA · SAP · Power BI · English · Danish · Esbjerg · Copenhagen · Aarhus"
)


def build(path):
    m = MasterDoc(TEMPLATE, lang="en-GB")

    # ---------------------------------------------------------------- page 1
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta(RECIPIENT)

    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, SUBJECT, bold=True, color="1A1A1A")

    for t in INTRO:
        m.para(t, after=80)

    for label, body in BULLETS:
        m.bullet(label, body, after=20)

    m.para(SYSTEM, after=80)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=35)

    m.meta("Kind regards · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- page 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "COMMERCIAL PROFILE")
    m.para(PROFILE, after=80)

    m.section("WHAT THE ROLE REQUIRES — AND HOW IT IS ANSWERED")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("COMMERCIAL AND SERVICE METHODS — APPLIED IN PRACTICE",
                   ("Area", "Methods and tools"), MODELS)

    m.section("SELECTED RESULTS")
    for label, body in ACHIEVEMENTS:
        m.bullet(label, body, after=30)

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

    m.section("CORE COMPETENCES & KEYWORDS")
    m.para(KEYWORDS, after=80)

    # closing page
    m.page_break()
    m.models_table("FIRST 90 DAYS — HOW THE PIPELINE GETS IN MOTION",
                   ("When", "What is in place"), FIRST90)

    m.section("HOW THE ROLE IS WORKED — THE THREE INTERFACES")
    for label, body in PARTNER:
        m.bullet(label, body, after=30)

    m.section("PRACTICAL INFORMATION")
    m.para(PRACTICAL_CV, after=80)

    m.section("REFERENCES")
    m.para(REFERENCES, after=80, justify=False)

    # no paragraph or table row may break across a page
    for _p in m.doc.paragraphs:
        _p.paragraph_format.keep_together = True
    for _tbl in m.doc.tables:
        for _row in _tbl.rows:
            for _c in _row.cells:
                for _p in _c.paragraphs:
                    _p.paragraph_format.keep_together = True

    from docx.oxml.ns import qn as _qn
    from docx.oxml import OxmlElement as _OE
    for _tbl in m.doc.tables:
        for _tr in _tbl._tbl.findall(_qn("w:tr")):
            _trPr = _tr.find(_qn("w:trPr"))
            if _trPr is None:
                _trPr = _OE("w:trPr")
                _tr.insert(0, _trPr)
            if _trPr.find(_qn("w:cantSplit")) is None:
                _trPr.insert(0, _OE("w:cantSplit"))

    return m.save(path,
                  title="Application and CV — Senior Sales Manager, Renewables Service, Semco Maritime",
                  subject="Offshore wind service · tenders · contract negotiation · key accounts",
                  keywords=("senior sales manager, renewables service, offshore wind, tender management, "
                            "contract negotiation, key account management, semco maritime, english"),
                  comments="Master design (navy banners, Calibri 9.5 pt). English, ATS-optimised. "
                           "Application page 1 (requirement → answer), CV pages 2-3, 90 days page 4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_SemcoMaritime_SeniorSalesManager.docx")
    print("OK", build(out))
