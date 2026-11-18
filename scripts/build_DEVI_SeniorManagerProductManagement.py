# -*- coding: utf-8 -*-
"""Danfoss / DEVI — Senior Manager, Product Management, Req 52521.

English combined application + CV. Product-focused style: opening AE; structure
Customer evidence → portfolio choices → launch readiness → in-market performance;
register The Product Decision Record. Candidate-confirmed ARJ portfolio ownership is
separated from unsupported commercial metrics or prior direct reports in Product Management.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")
OUTPUT = os.path.join(ROOT, "Shahram_Ajloo_Danfoss_DEVI_SeniorManagerProductManagement_52521.docx")
NAME = "SHAHRAM AJLOO"
TITLE = "Senior Manager Product Management · technical product portfolio"
CONTACT = "+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark"
DATE = "3 November 2026"
RECIPIENT = "Danfoss · DEVI Product Management · Kolding / Grodzisk Mazowiecki"
SUBJECT = "Senior Manager, Product Management — Req ID 52521"

LETTER = [
    "A thermostat or heating cable is the visible end of a much longer chain of product decisions: whose need matters most, where the product earns its place, what to invest in, and whether engineering, sourcing and manufacturing can deliver it at the right value. It starts with customer, market and competitive insights, turning market insights into clear priorities and future product opportunities. For DEVI, the task is shaping product direction and delivering commercially successful solutions.",
    "The first working instrument should be a shared product decision record, not another status deck. For every material opportunity, it would hold the customer and competitive evidence, target application, portfolio fit, options considered, business case and price/margin assumptions, accountable product owner, R&D and supply dependencies, decision gate, launch readiness and the measure that will test the bet after launch. A regular portfolio review can then make explicit choices to invest, improve, hold or exit.",
    "From idea to market, the gates should match the risk. Confirm the user, installer and channel problem before solution selection; validate desirability and technical feasibility with R&D; test the business case and target economics with commercial and Finance; agree manufacturability, sourcing and quality readiness before release; then review adoption, realized price, margin, quality and customer feedback against the original case. If evidence changes, the roadmap should change with it. These are proposed controls; actual baselines and decision rights should be agreed with DEVI.",
    "The Product Management team needs clear ownership without losing the hands-on connection to customers and technology. A concise roadmap review, regular one-to-ones, product-owner development goals and a visible decision log can give the team direction and room to act. Sales, Marketing, R&D, Manufacturing and Sourcing should each enter at the decision where their evidence matters, with one named owner carrying the choice through. Customer visits and the stated travel allowance can keep that evidence close to the market.",
    "This approach fits Danfoss’ LEAP 2030 priorities — Leading Portfolio, Customers & Growth and Innovative Solutions — and its call to strengthen customer partnerships and competitiveness. Danfoss says “We engineer a better future” by working to increase machine productivity, reduce emissions, lower energy consumption, and enable electrification. DEVI’s stated product quality, technical expertise and long-term reliability belong in that growth case too. The end is commercially successful solutions, turning market needs into solutions that create value.",
    "In the first 30 days, listen across the team, key customers and commercial/R&D/manufacturing partners; map portfolio decision rights, active roadmap, launches, pricing cadence and available performance data. By day 60, agree a baseline and pilot the decision record on one live product opportunity. By day 90, review the pilot with the team, close or revise its next gate, and present a prioritised portfolio view with owners, economics, dependencies and unresolved decisions."
]

PROFILE = (
    "Product and technical leadership across an industrial portfolio and engineering delivery. At ARJ Engineering, "
    "held product/portfolio responsibility for electric motors, pumps and submersible pumps, including lifecycle, "
    "roadmap/business-case, launch and price/margin/investment decisions. Led a 12-person production/technical team; "
    "direct reports have been technical/production staff rather than Product Managers. Later roles add "
    "full-P&L technical service, AI-enabled technical-product design and customer applications, and regulated CAPEX "
    "delivery with 25 specialists. Professional English. Willing to relocate to Kolding and travel up to 30 days/year "
    "for this role."
)

RESULTS = [
    ("Product portfolio ownership", "ARJ Engineering · electric motors, pumps and submersible pumps; lifecycle and commercial decision responsibility."),
    ("37 CAPEX projects · 25 specialists", "Novo Nordisk · parallel engineering delivery, DKK 2–10m per project, FAT/SAT and IQ/OQ/PQ; zero critical findings at handover."),
    ("12-person production team", "ARJ Engineering · direct leadership of mechanics and technicians; production/technical team, not product-manager direct reports."),
    ("Full P&L · 5 electricians + 3 apprentices", "ELOHVAC · technical service and project delivery, team leadership, quotations and operating economics."),
]

EXPERIENCE = [
    ("Owner / Technical Director / Authorised Electrical Engineer", "ELOHVAC ApS · Copenhagen · May 2023–present", "5 electricians + 3 apprentices · full P&L", [
        "Own technical service and project delivery from quotation and scope through planning, materials, subcontractors, quality and handover; manage customer commitments and full P&L.",
        "Lead five electricians and three apprentices through daily planning, one-to-ones, development, safety and quality follow-up; built Python/Claude tools for estimates, schedules, QA and KPI reporting, with a documented productivity improvement above 40%."
    ]),
    ("Co-owner and CTO · Head of AI / AI Coding", "Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 (concurrent with ELOHVAC)", "4–10 people", [
        "Led AI and AI-coding delivery for technical and industrial applications: requirements, architecture, integration, commissioning, documentation and customer handover; developed LLM-API and AI-agent solutions.",
        "Introduced common AI-assisted coding, review and test standards; used AI in management reporting and matrix leadership across two concurrent organisations. Applied AI coding to technical-plant and industrial-component design variants, calculations and sizing, with engineering validation before release to the customer."
    ]),
    ("Senior Commissioning Engineer / Electrical Project Manager", "Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024", "37 concurrent CAPEX projects · DKK 2–10m each · 25 specialists", [
        "Coordinated electrical project scope, cost, risk and resources across engineering, procurement and site; SAP ERP, monthly reporting, FAT/SAT and IQ/OQ/PQ. Handover completed with zero critical findings.",
        "A PDCA programme reduced energy costs by 40%; this was an engineering/operational result, not a product-line margin result."
    ]),
]

EXPERIENCE_MORE = [
    ("Project and Workshop Manager", "Ventek-Air · Copenhagen · Jan–Nov 2022", "11 concurrent projects · 14-person team", [
        "Led daily capacity and delivery reviews from specification to handover; managed schedule, cost and quality across parallel projects."
    ]),
    ("Operations and Maintenance Lead / Workshop Technician", "Biofos (Lynetten) · Copenhagen · Aug 2017–Jan 2022", "24/7 critical process operation · pumps, HVAC, HV switchboards, SCADA", [
        "Preventive maintenance and urgent fault-finding on electrical and mechanical assets; used asset criticality, safety and operational needs to prioritise work.",
        "Applied 5S, Standard Work and PDCA; managed spare-parts flow and worked within LOTO, risk assessment and shift-operation controls."
    ]),
    ("Electromechanic / Production Team Lead", "ARJ Engineering · Tehran · Dec 2003–Mar 2010", "12 mechanics and technicians · product/portfolio remit", [
        "Candidate-confirmed ownership of a production portfolio spanning electric motors, pumps and submersible pumps, from customer/market needs and roadmap/business cases through product development and launch, including price, margin and investment decisions.",
        "Directly led the production/technical team of 12 mechanics and technicians; coordinated schedules, materials, performance and industrial electromechanical troubleshooting. No specific product launch, commercial result or quantified margin has been supplied."
    ]),
]

EDUCATION = [
    ("B.Tech (EQF 6), Technology Management & Mechanical Engineering", "Copenhagen School of Marine Engineering & Technology Management · 2017–2022"),
    ("Electrical authorisation LV/MV/HV · Marine Engineer", "Danish Safety Technology Authority · May 2023"),
    ("PRINCE2 · Certified Project Manager", "AXELOS / PeopleCert"),
    ("Lean and Six Sigma", "Worked with in practice; not certified"),
]

METHODS = [
    ("Product and portfolio", "ARJ industrial electromechanical products · product lifecycle ownership · customer insights and customer and market insights · roadmap/business case · new product development · concept to launch · commercialization · pricing and investment decisions"),
    ("People and delivery", "Direct technical/production leadership and team development · 12-person ARJ team · 5 electricians + 3 apprentices · 14-person Ventek team · matrix leadership"),
    ("Commercial and project", "Full P&L · quotations · project budgets and risks · portfolio performance review (proposed for DEVI) · SAP ERP · PRINCE2 · KPI reporting · investment delivery"),
    ("Engineering and improvement", "Industrial electrical/electromechanical systems · pumps · HVAC · SCADA · FAT/SAT · IQ/OQ/PQ · PDCA · A3 · 5 Whys · Ishikawa"),
    ("Languages and location", "Danish: native · English: professional · Persian: native · relocation to Kolding confirmed for Req 52521 · up to 30 travel days/year confirmed"),
    ("Danfoss / DEVI context", "Global product portfolio · electric heating technology · thermostats/cables · We engineer a better future · LEAP 2030 · Leading Portfolio · Customers & Growth · Innovative Solutions · product quality · technical expertise · long-term reliability")
]

REQUIREMENTS = [
    ("Lead and develop DEVI’s Product Management team; set direction/accountability and remain hands-on", "ARJ portfolio ownership was combined with direct leadership of 12 production/technical employees; ELOHVAC adds 5 electricians + 3 apprentices. Candidate has not directly managed Product Managers, so the transfer plan is to agree decision rights, coaching cadence and ownership with the existing PM team."),
    ("Shape global product strategy and roadmap for thermostats and electric heating cables", "At ARJ, candidate confirms product/portfolio ownership for electric motors, pumps and submersible pumps, including lifecycle and roadmap decisions. This is transferable industrial electromechanical portfolio experience, not prior DEVI thermostat or heating-cable product management."),
    ("Turn customer, market and competitive insights into priorities and product opportunities", "At ARJ, the product remit spanned the lifecycle and roadmap; for DEVI, the proposed evidence record separates customer, installer, channel and competitive signals, with a named owner and portfolio decision."),
    ("Take new products from idea to market", "ARJ product responsibility is confirmed across lifecycle, development and launch for its motor/pump range. Specific launch names, dates, adoption or sales results were not provided and are not asserted."),
    ("Build business cases and set priorities / investment choices", "Candidate confirms ARJ roadmap/business-case and investment decisions. Novo adds delivery discipline across 37 CAPEX projects (DKK 2–10m each), with scope, cost, risk, testing and handover tracked."),
    ("Partner with R&D and commercial teams to deliver successful launches", "Novo coordinated 25 engineering, procurement and site specialists through FAT/SAT and IQ/OQ/PQ; ARJ included product development/launch responsibility. Proposed DEVI stage gates bring R&D and commercial owners together without claiming a prior DEVI launch."),
    ("Review pricing, profitability and product performance; turn gaps into actions", "Candidate confirms price/margin decisions in ARJ portfolio ownership; ELOHVAC adds full P&L and quotation economics. No product-margin baseline or numeric ARJ improvement was provided; review measures should be agreed with Finance and Sales."),
    ("Commercial acumen in pricing, margins, profitability and investment", "ARJ product pricing/margin/investment ownership is candidate-confirmed; ELOHVAC documents full P&L, quotations and cost control. Keep service/project P&L distinct from global product-line profitability."),
    ("B2B product management/strategy in technical, industrial or electronic products", "ARJ's industrial product portfolio was electric motors, pumps and submersible pumps; ELOHVAC and Biofos add technical electrical, electromechanical and industrial operating context. No direct electric-heating portfolio experience is claimed."),
    ("Translate customer and market insight into product roadmaps", "Candidate confirms ARJ lifecycle and roadmap responsibility. For DEVI, the proposed roadmap review links verified needs and alternatives to value, investment, owner, gate and post-launch measures."),
    ("Take products from concept and business case through launch", "Candidate confirms end-to-end ARJ product responsibility covering business cases, development and launch; Data Power adds technical/industrial application delivery from requirements through commissioning and customer handover."),
    ("Lead and develop people; influence across functions and markets", "Direct leadership: 12 mechanics/technicians at ARJ, 5 electricians + 3 apprentices at ELOHVAC and 14 at Ventek; matrix coordination of 25 specialists at Novo. Direct reports were technical/production teams, not product managers."),
    ("Connect customers, technology and the business", "ELOHVAC connects customer requirements, technical scope, quotation, delivery and P&L; Data Power delivered customer technical/industrial applications; ARJ portfolio ownership connected industrial products to lifecycle and commercial decisions."),
    ("Work across Sales, Marketing, R&D, Manufacturing and Sourcing", "Novo delivery brought engineering, procurement and site specialists together; ARJ portfolio role combined product decisions with manufacturing/production leadership. Specific prior direct ownership of Marketing or a global sourcing organization is not claimed."),
    ("Professional fluency in English; effective international customer/colleague relationships", "Master CV records professional English and native Danish and Persian. Data Power customer applications and Novo cross-functional delivery required clear technical documentation, handover and stakeholder communication."),
    ("Lead a global portfolio spanning thermostats and electric heating cables", "DEVI's official catalogue lists thermostats, heating cables and mats; candidate's nearest product-portfolio evidence is ARJ motors/pumps. Apply the lifecycle and commercial discipline while learning DEVI-specific applications and channel economics."),
    ("Full-time, hybrid role based in Kolding or Grodzisk Mazowiecki", "Candidate confirms willingness to relocate to Kolding for this DEVI role. Confirmed Kolding base; exact hybrid cadence and cross-site presence remain to be agreed with Danfoss."),
    ("Travel up to 30 days per year", "Candidate confirms willingness to travel up to 30 days annually for this role; travel should be tied to customer discovery, market reviews and launch/portfolio decisions.")
]


def _add_jobs(m, jobs):
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope)
        for text in bullets:
            m.bullet("", text, after=12, line=210)


def build(path=OUTPUT):
    m = MasterDoc(TEMPLATE, lang="en-GB")
    # Page 1: a role-first product system, with proposals distinct from past evidence.
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta(RECIPIENT)
    p = m._p(spacing_after=55, line=245, justify=False)
    m._run(p, SUBJECT, bold=True)
    m.para("Dear DEVI Hiring Team", after=40, justify=False)
    for text in LETTER:
        m.para(text, after=42, line=210)
    m.meta("Kind regards", after=8)
    m.meta("Shahram Ajloo", after=0)

    # Page 2: profile, selected evidence and recent leadership/product work.
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PRODUCT PORTFOLIO · PEOPLE · COMMERCIAL DELIVERY")
    m.section("PROFILE")
    m.para(PROFILE, after=24, line=205)
    m.section("SELECTED EVIDENCE")
    for label, detail in RESULTS:
        m.bullet(label, detail, after=9, line=195)
    m.section("EXPERIENCE")
    _add_jobs(m, EXPERIENCE)

    # Page 3: earlier roles, qualifications and employer language.
    m.page_break()
    m.resume_header(NAME, "Industrial product ownership · people leadership · global delivery", CONTACT, "EXPERIENCE AND CAPABILITY")
    m.section("EXPERIENCE · CONTINUED")
    _add_jobs(m, EXPERIENCE_MORE)
    m.section("EDUCATION AND CERTIFICATIONS")
    for title, detail in EDUCATION:
        m.edu(title, detail)
    m.section("PRODUCT, COMMERCIAL AND LEADERSHIP PRACTICE")
    m.models_table("EVIDENCE AND WORKING VOCABULARY", ("Area", "Documented experience / context"), METHODS, widths=(2450, 7896), compact=True)
    m.para("Location: Måløv, Denmark · willing to relocate to Kolding for Req 52521 · available for up to 30 travel days/year.", after=10, line=195, justify=False)

    # Page 4: complete evidence mapping for all requirements.
    m.page_break()
    m.resume_header(NAME, "Senior Manager, Product Management · evidence map", CONTACT, "REQUIREMENTS AND EVIDENCE")
    m.para("Product ownership and proposals for DEVI are distinguished from the candidate’s documented roles and outcomes.", after=18, line=195)
    table = m.models_table("JOB REQUIREMENTS AND EVIDENCE", ("Requirement", "Evidence and application"), REQUIREMENTS,
                           widths=(3600, 6746), compact=True)
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    repeat = OxmlElement("w:tblHeader")
    repeat.set(qn("w:val"), "true")
    table.rows[1]._tr.get_or_add_trPr().append(repeat)
    return m.save(path, title="Application and CV — Danfoss DEVI Senior Manager Product Management",
                  subject=SUBJECT,
                  keywords="Danfoss; DEVI; Senior Manager Product Management; product strategy; global product portfolio; roadmap; pricing; profitability; electric heating; Kolding; Req 52521")


if __name__ == "__main__":
    print(build())
