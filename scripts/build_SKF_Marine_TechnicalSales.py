# -*- coding: utf-8 -*-
"""SKF Marine — English application and CV, tailored to the user-supplied Danish vacancy."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Technical Sales | Marine Engineering | Reliability & Customer Partnerships"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv, Denmark")
DATE = "3 November 2026"
RECIPIENT = "SKF Danmark A/S · Hvidovre · SKF Marine"
SUBJECT = "Application: Technical Sales – SKF Marine"

# Page 1: customer problem → commercial approach → relevant evidence.
INTRO = [
    "Marine customers do not buy a component in isolation: they need confidence that a shaft line, "
    "bearing or monitoring solution will support safe, dependable operation over the life of the asset. "
    "The technical sales role at SKF Marine appeals to me because it combines long-term customer "
    "relationships with practical engineering and measurable operating value.",
    "I bring a marine-engineering education and STCW training, alongside hands-on and leadership "
    "experience in uptime-critical industrial operations, electrical and electromechanical systems, "
    "pumps, service work and customer-facing commercial responsibility. In ELOHVAC, I lead customer "
    "dialogue from understanding the need through quotation, planning and delivery, with full P&L "
    "responsibility. At Biofos, I worked with 24/7 operations, maintenance, failure history, pumps, "
    "HVAC and SCADA. These are transferable foundations for a consultative discussion about reliability, "
    "performance, maintenance and lifecycle cost.",
]

BULLETS = [
    ("Understand the operation before proposing a product",
     "I start with the customer's duty, operating constraints, failure modes and decision criteria, then "
     "translate them into a scoped technical and commercial proposal. My experience is in industrial "
     "service and contracting rather than an established marine sales territory."),
    ("Build trust through reliable follow-through",
     "As ELOHVAC owner and technical director, I am accountable for customer communication, quotations, "
     "contract scope, costs and delivery. In 24/7 operations, accurate commitments and documented "
     "follow-up matter as much as the technical fix."),
    ("Develop the account as a long-term relationship",
     "I would combine regular customer contact with structured follow-up on open needs, service issues "
     "and future opportunities—working with SKF's product specialists to connect customer evidence to "
     "the right solution and sustainable commercial value."),
]

LETTER_CLOSE = (
    "My marine connection is through my B.Tech in Technology Management & Mechanical Engineering from "
    "the Copenhagen School of Marine Engineering & Technology Management and STCW training; my "
    "employment experience has been in industrial and contracting environments, not onboard ship "
    "maintenance. I would bring that technical base, commercial ownership and a disciplined learning "
    "approach to SKF's portfolio—including Simplex, BlueRun, bearings, condition monitoring and "
    "RecondOil—building detailed product knowledge with your Nordic specialists. I would welcome a "
    "conversation about the customer needs and growth priorities for SKF Marine in Denmark."
)

PROFILE = (
    "Technical and commercial leader with a marine-engineering degree and experience connecting customer "
    "needs to electrical, electromechanical and industrial service solutions. Full P&L and customer-facing "
    "quotation responsibility in an electrical contracting business; 24/7 operational experience with "
    "pumps, HVAC, switchgear and SCADA; and earlier product-portfolio responsibility for motors and pumps. "
    "Strong in technical discovery, clear commercial communication, delivery follow-through and cross-"
    "functional coordination. Danish native; English professional."
)

CORE = [
    ("Technical customer dialogue",
     "Clarify operating challenges, application and constraints; connect technical options to reliability, "
     "performance, maintenance and commercial value."),
    ("Commercial responsibility",
     "ELOHVAC: full P&L, quotation and cost calculations, scope, customer communication and delivery follow-up."),
    ("Reliability and rotating equipment",
     "24/7 exposure to pumps, motors, HVAC, electrical systems, SCADA, planned maintenance, failure history "
     "and root-cause problem solving."),
    ("Product and lifecycle perspective",
     "ARJ Engineering: responsibility for a production-line portfolio including electric motors, pumps and "
     "submersible pumps across roadmap, business cases, development, launch, pricing, margin and investment."),
    ("Customer and stakeholder coordination",
     "Coordinate customers, technicians, suppliers and specialists; clarify commitments, keep actions owned "
     "and dated, and follow through to handover."),
]

EXPERIENCE_RECENT = [
    ("Co-owner & CTO / Technical Lead, AI Division",
     "Data Power Consultant ApS · Copenhagen · 2024–present (concurrent with ELOHVAC)",
     "Technical and industrial customer applications · team of 4–10",
     [("Customer delivery",
       "Led technical customer projects from needs discovery and system integration through commissioning, "
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
       "Contributed to a documented programme that reduced energy costs by 40%; maintained operational and "
       "safety discipline in a continuously operating plant.")]),
    ("Electromechanical Technician / Production Team Leader",
     "ARJ Engineering · Tehran · Dec 2003–Mar 2010",
     "12-person technical and production team · industrial equipment",
     [("Product portfolio and technical problem solving",
       "Held product-portfolio responsibility for a production line including electric motors, pumps and "
       "submersible pumps; worked across roadmap and business cases, development and launch, and pricing, "
       "margin and investment decisions. Led technical/production staff and used structured fault diagnosis.")]),
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

LANGUAGES = "Danish — native · English — professional, written and spoken · Persian/Farsi — native · Driving licence B"

KEYWORDS = (
    "Technical sales · marine · maritime · marine engineering · customer relationships · long-term relationships · "
    "customer needs · customer insight · technical advice · technical solutions · commercial value · "
    "customer service · existing customers · new business · Danish market · key accounts · account development · "
    "negotiation · agreements · sustainable growth · reliability · performance · efficient operations · "
    "shaft line · Simplex · BlueRun · bearings · condition monitoring · RecondOil · maintenance · lifecycle cost · "
    "motors · pumps · rotating equipment · service · full P&L · quotations · pricing · contract scope · "
    "technical communication · cross-functional coordination · Danish · English · STCW"
)


def build(path):
    m = MasterDoc(TEMPLATE, lang="en-GB")

    # Application letter
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta(RECIPIENT)
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, SUBJECT, bold=True, color="1A1A1A")
    for text in INTRO:
        m.para(text, after=75)
    for label, body in BULLETS:
        m.bullet(label, body, after=28)
    m.para(LETTER_CLOSE, after=70)
    m.para("Kind regards,", after=20, justify=False)
    m.para("Shahram Ajloo", after=0, justify=False)

    # CV, page 2
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "TECHNICAL SALES PROFILE")
    m.para(PROFILE, after=70)
    m.section("CUSTOMER VALUE & TECHNICAL-COMMERCIAL STRENGTHS")
    for label, body in CORE:
        m.bullet(label, body, after=25)
    m.section("PROFESSIONAL EXPERIENCE")
    for title, meta, scope, bullets in EXPERIENCE_RECENT:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    # CV, page 3
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFESSIONAL EXPERIENCE & QUALIFICATIONS")
    for title, meta, scope, bullets in EXPERIENCE_EARLIER:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=24)
    m.section("EDUCATION, AUTHORISATION & MARITIME TRAINING")
    for title, meta in EDUCATION:
        m.edu(title, meta)
    m.section("LANGUAGES & PRACTICAL DETAILS")
    m.para(LANGUAGES, after=45, justify=False)
    m.para("Based in Måløv, Denmark · available for customer visits and hybrid work · references available on request.",
           after=45, justify=False)
    m.section("CORE TECHNICAL & COMMERCIAL TERMS")
    m.para(KEYWORDS, after=60)

    # Keep rows and paragraphs intact for stable pagination.
    for paragraph in m.doc.paragraphs:
        paragraph.paragraph_format.keep_together = True
    for table in m.doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    paragraph.paragraph_format.keep_together = True

    return m.save(
        path,
        title="Technical Sales – SKF Marine | Application and CV | Shahram Ajloo",
        subject="Marine technical sales · customer partnerships · reliability · industrial service",
        keywords="SKF Marine, technical sales, marine engineering, customer relationships, reliability, bearings, condition monitoring",
        comments="English application and tailored CV; master design; claims grounded in master resume; no application submitted.",
    )


if __name__ == "__main__":
    output = os.path.join(ROOT, "Shahram_Ajloo_SKF_Marine_TechnicalSales.docx")
    print(build(output))
