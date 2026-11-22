# -*- coding: utf-8 -*-
"""SKF Marine — job-first English application and evidence-led CV."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Technical Sales | SKF Marine | Customer Reliability & Sustainable Growth"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv, Denmark")
DATE = "3 November 2026"
RECIPIENT = "SKF Danmark A/S · Hvidovre · SKF Marine"
SUBJECT = "Application: SKF Teknisk salg Marine"

# Employer-first opening, then operating approach, evidence, and role-specific close.
INTRO = (
    "SKF Marine's Danish growth opportunity is to turn advanced shaft-line, bearing and condition "
    "solutions into trusted, lasting customer partnerships. Shipowners, yards and maritime companies "
    "need choices grounded in operating conditions—not a quick product pitch—so the sales process must "
    "connect application fit, reliability, lifecycle value and follow-through. The role's stated purpose "
    "is long-term customer relationships, technical advice grounded in application and customer needs, "
    "supporting higher operational "
    "reliability, better performance and more efficient operations; SKF's technologies also help reduce "
    "energy waste and use resources more efficiently."
)

CULTURE_CONTEXT = (
    "The advertisement describes SKF as investing in Denmark and the Nordics, with close collaboration "
    "with colleagues across the organisation, access to specialists and technical experts, thorough "
    "onboarding, a flexible, hybrid working model and performance-based incentives. That is a useful "
    "operating model for a technical sale: learn the portfolio with its experts, validate an application "
    "before making a promise, and keep the customer relationship active after the agreement."
)

APPROACH = [
    ("Start with the vessel and the operating problem",
     "Map the customer's asset, duty cycle, service window, failure consequences and decision criteria. "
     "Then work with SKF's technical experts to validate whether Simplex, BlueRun, bearings, condition "
     "monitoring or RecondOil fits the application; present options and assumptions in the customer's terms."),
    ("Build the account around a useful next action",
     "For existing customers, keep an account record of stakeholders, current needs, open service issues, "
     "next contact and agreed actions. For new Danish-market opportunities, qualify the operational need, "
     "timing, buying group and value before investing in a proposal."),
    ("Make the commercial case deliverable",
     "Relate technical choices to availability, maintenance, performance and lifecycle cost. Before "
     "negotiation, align technical scope, assumptions, service boundaries, price and decision authority; "
     "after agreement, maintain a clear follow-up path with the customer and delivery specialists."),
]

EVIDENCE_BRIDGE = (
    "The evidence for this approach is practical: ELOHVAC combines direct customer dialogue, quotations, "
    "scope and cost control with full P&L responsibility. Biofos provides 24/7 operating context across "
    "pumps, HVAC, switchgear and SCADA, and a documented energy-cost reduction of 40% through an "
    "improvement programme. A marine-engineering B.Tech and STCW training supply the maritime "
    "foundation; the employment record is in industrial and contracting operations, not shipboard service."
)

CLOSE = (
    "The opportunity is to grow SKF Marine in Denmark by joining customer insight to specialist product "
    "knowledge and disciplined commercial follow-through. The first customer conversations should reveal "
    "which operating priorities, application questions and account opportunities deserve attention."
)

REQUIREMENT_ROWS = [
    ("Marine customers: long-term relationships and technically grounded advice",
     "Build each conversation around the customer's operating duty, service history, constraints and "
     "decision criteria, then agree a practical next step. ELOHVAC demonstrates direct customer dialogue "
     "and service follow-through; no marine account count or sales history is invented."),
    ("Represent SKF Marine shaft-line solutions, Simplex, BlueRun, bearings, condition monitoring and RecondOil",
     "Use the marine-engineering foundation and documented motor/pump portfolio work to learn the "
     "applications, limits and lifecycle value of each SKF offer. Confirm fit, data and claims with the "
     "Nordic product specialists before making a customer recommendation; no previous SKF-product sales is claimed."),
    ("Develop and maintain existing maritime customer relationships",
     "Keep a usable account plan: stakeholders, assets and operating priorities, current service issues, "
     "commitments, next contact and open opportunities. ELOHVAC includes customer-facing service and "
     "commercial accountability; the account cadence is a proposed method, not an invented marine portfolio."),
    ("Identify and develop new business opportunities in the Danish market",
     "Use refit windows, maintenance needs, reliability concerns and resource-efficiency goals as discovery "
     "triggers; qualify need, timing, decision process and value before bidding. ELOHVAC provides "
     "quotation and business-ownership experience, without claiming quantified new-market wins."),
    ("Negotiate agreements, manage key accounts and deliver sustainable growth",
     "Prepare scope, application assumptions, service boundaries, value case, cost and approval route before "
     "negotiations; record commitments and follow through after signature. Full P&L and quotation ownership "
     "are documented in ELOHVAC; no marine key-account growth result is asserted."),
    ("Understand customer operational challenges and translate needs into relevant solutions",
     "Ask about duty, failure modes, access and maintenance constraints before selecting a solution. Biofos "
     "provided 24/7 experience with pumps, HVAC, high-voltage switchgear and SCADA; this supports "
     "operational discovery without pretending to be onboard marine-engineering employment."),
    ("Build trust through dialogue, insight and business understanding",
     "Translate technical detail into clear scope, assumptions, costs and consequences, then keep actions "
     "visible and close the loop with the customer. ELOHVAC requires customer communication alongside "
     "full P&L responsibility, supplier coordination and documented delivery."),
    ("Work in a structured way and progress customer relationships and sales processes",
     "Use qualified opportunities, named owners, next actions and dated follow-up. Ventek-Air used daily "
     "planning and progress meetings across 11 concurrent projects; Novo involved monthly cost, schedule "
     "and risk reporting across 37 CAPEX projects."),
    ("Communicate technical solutions and make their commercial value clear",
     "Connect the application to reliability, maintenance, performance and lifecycle economics, and "
     "validate technical claims with the relevant specialist. At Biofos, an improvement programme "
     "documented a 40% energy-cost reduction; state it as a plant result, not an individual sales win."),
    ("Bring marine-sector sales experience or a technical/trade background with marine-area experience",
     "The B.Tech in Technology Management & Mechanical Engineering is from the Copenhagen School of "
     "Marine Engineering & Technology Management; STCW safety training was completed in 2021–2023. "
     "Technical work has been in industrial/contracting settings, with relevant pumps, motors and uptime-critical systems."),
    ("Speak and write Danish and English fluently",
     "Danish is native; English is professional in written and spoken work, matching the recorded language "
     "distinction. Use Danish for local customer dialogue and English for Nordic specialist coordination "
     "and technical documentation."),
    ("German or other Nordic languages are an advantage",
     "No additional German or Nordic-language proficiency is recorded, so none is claimed. The role's "
     "Nordic specialist network can support cross-border technical alignment while customer communication "
     "is handled in documented Danish and professional English."),
    ("Support higher reliability, better performance, efficient operations and resource use",
     "Frame a value case around operating availability, maintenance burden, energy/resource use and "
     "measurable performance, then agree how the customer will review results. Biofos experience includes "
     "24/7 assets and a documented 40% reduction in energy costs through an improvement programme."),
    ("Collaborate with the Danish office, Nordic Marine organisation and technical specialists",
     "Bring application questions to the right product and engineering experts, agree responsibilities "
     "before customer commitments, and keep the account owner informed through a shared action log. "
     "Novo's 25 specialists were coordinated across project interfaces, not described as direct reports."),
    ("Use thorough onboarding and access to SKF's specialists and technical experts",
     "Use onboarding to learn portfolio boundaries, application evidence, customer references and internal "
     "approval paths; shadow specialists on early customer cases and capture verified answers for reuse. "
     "This is a proposed learning plan, not a claim of existing SKF product certification."),
    ("Work flexibly across customer visits, office and home in a hybrid model",
     "Based in Måløv with a valid manual B driving licence and available for customer visits in Denmark. "
     "The mix of customer, Hvidovre-office and home work can follow the advertised hybrid model; no "
     "unverified travel percentage or commute claim is added."),
    ("Send application and CV in English by 27 November 2026 with the specified subject line",
     "The application and CV are prepared in English for SKF Danmark A/S; the requested email subject is "
     "“SKF Teknisk salg Marine” and the advertised destination is skf.danmark@skf.com. The material is "
     "prepared only; it has not been sent."),
]

PROFILE = (
    "SKF Marine's technical-sales remit depends on linking maritime operating needs to a relevant "
    "portfolio, a clear commercial case and a relationship that continues after the first sale. The "
    "evidence base combines a marine-engineering degree and STCW training; industrial asset-reliability "
    "work with pumps, motors, HVAC and SCADA; customer-facing quotations and full P&L in ELOHVAC; and "
    "product-portfolio responsibility for motors and pumps at ARJ Engineering."
)

EXPERIENCE_RECENT = [
    ("Co-owner & CTO / Technical Lead, AI Division",
     "Data Power Consultant ApS · Copenhagen · 2024–present (concurrent with ELOHVAC)",
     "Technical and industrial customer applications · team of 4–10",
     [("Customer delivery",
       "Led customer projects from needs discovery and system integration through commissioning, "
       "documentation and handover; coordinated specialists and kept customer requirements connected to delivery.")]),
    ("Owner / Technical Director / Authorised Marine Engineer (LV/MV/HV)",
     "ELOHVAC ApS · Copenhagen · May 2023–present",
     "Electrical contracting and service · 5 electricians and 3 apprentices · full P&L",
     [("Commercial and customer ownership",
       "Lead customer discussions, site needs assessment, quotations and calculations, scope and cost control, "
       "supplier/subcontractor coordination, quality assurance and handover."),
      ("Technical service",
       "Electrical systems, switchboards, controls, ventilation and climate installations: installation, "
       "fault-finding, maintenance and documented delivery; manage customer expectations and follow-up.")]),
    ("Senior Commissioning Engineer / Project Manager, Electrical Systems",
     "Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024",
     "37 concurrent CAPEX projects · DKK 2–10m each · 25 specialists coordinated",
     [("Project and stakeholder delivery",
       "Coordinated engineering, procurement and site interfaces; reported schedule, cost and risk monthly; "
       "managed acceptance and handover under GMP/FDA/EMA requirements, with zero critical findings.")]),
    ("Project & Workshop Manager",
     "Ventek-Air · Copenhagen · Jan–Nov 2022",
     "14-person team · 11 concurrent technical installation projects",
     [("Planning and customer delivery",
       "Managed daily capacity and progress reviews, supplier and logistics follow-up, bottleneck analysis "
       "and written change handling through formal handover.")]),
]

EXPERIENCE_EARLIER = [
    ("Head of Operations & Maintenance / Workshop Technician",
     "Biofos (Lynetten) · Copenhagen · Aug 2017–Jan 2022",
     "24/7 utility operations · pumps, HVAC, high-voltage switchgear and SCADA",
     [("Asset reliability",
       "Worked with planned maintenance, failure history, troubleshooting and supplier/contractor coordination; "
       "used SAP and SCADA information to support safe, reliable operations and improvement."),
      ("Energy performance",
       "Contributed to an improvement programme that documented a 40% reduction in energy costs; maintained "
       "operational and safety discipline in a continuously operating plant.")]),
    ("Electromechanical Technician / Production Team Leader",
     "ARJ Engineering · Tehran · Dec 2003–Mar 2010",
     "12-person technical and production team · industrial equipment",
     [("Product portfolio and technical problem solving",
       "Held product-portfolio responsibility for a production line including electric motors, pumps and "
       "submersible pumps; worked across roadmap/business cases, development/launch, and pricing, margin "
       "and investment decisions. Led technical/production staff and used structured fault diagnosis.")]),
]

EDUCATION = [
    ("B.Tech — Technology Management & Mechanical Engineering",
     "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · grade 7.6/12"),
    ("Electrical & Mechanical Design, Electrical Engineering (EQF level 6)",
     "Tehran Technical University · 2000–2003"),
    ("Danish electrical authorisation (LV/MV/HV), held as a marine engineer",
     "Danish Safety Technology Authority · May 2023"),
    ("STCW safety training",
     "Danish Maritime Authority · engine-room watch and designated safety duties · 2021–2023"),
    ("Refrigeration and climate systems (AMU)", "Mercantec · 2021"),
]

LANGUAGES = (
    "Danish — native · English — professional, written and spoken · Persian/Farsi — native · "
    "Driving licence B (manual)"
)

def build(path):
    m = MasterDoc(TEMPLATE, lang="en-GB")

    # Page 1 — role and employer mission first.
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta("SKF Danmark A/S · Hvidovre · SKF Marine · Application in English")
    p = m._p(spacing_after=70, line=260, justify=False)
    m._run(p, SUBJECT, bold=True, color="1A1A1A")
    m.para(INTRO, after=65)
    m.para(CULTURE_CONTEXT, after=65)
    m.section("THE CUSTOMER-VALUE ROUTE")
    for label, body in APPROACH:
        m.bullet(label, body, after=25)
    m.para(EVIDENCE_BRIDGE, after=55)
    m.para(CLOSE, after=45)
    m.para("Kind regards,", after=10, justify=False)
    m.para("Shahram Ajloo", after=0, justify=False)

    # Page 2 — full requirement-by-requirement evidence map for the CV.
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "SKF MARINE — ROLE REQUIREMENTS & EVIDENCE")
    m.models_table("SKF MARINE — CUSTOMER CHALLENGE / METHOD / EVIDENCE / VALUE",
                   ("Requirement in the posting", "Solution, evidence and operating value"),
                   REQUIREMENT_ROWS, widths=(3000, 7346), compact=True)

    # Page 3 — reverse-chronological experience, tied to the role.
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFESSIONAL EXPERIENCE — CUSTOMER, PRODUCT & DELIVERY")
    m.section("CURRENT AND RECENT ROLES")
    for title, meta, scope, bullets in EXPERIENCE_RECENT:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    # Continue the role-focused CV with earlier reliability/product evidence and qualifications.
    m.section("EARLIER OPERATIONS & PRODUCT EVIDENCE")
    for title, meta, scope, bullets in EXPERIENCE_EARLIER:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=26)
    m.section("EDUCATION, AUTHORISATION & MARITIME TRAINING")
    for title, meta in EDUCATION:
        m.edu(title, meta)
    m.section("LANGUAGES & PRACTICAL DETAILS")
    m.para(LANGUAGES, after=35, justify=False)
    m.para("Based in Måløv, Denmark · available for customer visits and the advertised hybrid work model · references available on request.",
           after=35, justify=False)
    # Keep paragraphs and table rows intact for stable rendering.
    for paragraph in m.doc.paragraphs:
        paragraph.paragraph_format.keep_together = True
    for table in m.doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    paragraph.paragraph_format.keep_together = True

    return m.save(
        path,
        title="Application and CV — Technical Sales, SKF Marine | Shahram Ajloo",
        subject="SKF Marine · marine customer relationships · reliability · technical sales",
        keywords="technical sales, SKF Marine, customer relationships, marine engineering, reliability, bearings, condition monitoring",
        comments="Job-first English application and evidence-led CV; official culture claims sourced to user-provided job ad; not submitted.",
    )


if __name__ == "__main__":
    output = os.path.join(ROOT, "Shahram_Ajloo_SKF_Marine_TechnicalSales.docx")
    print(build(output))
