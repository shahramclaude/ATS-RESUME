# -*- coding: utf-8 -*-
"""
Alfa Laval Aalborg A/S — Technical Lead Engineer (Marine Boilers & Heaters).
Aalborg · frist 20.11.2026 · kontakt: Elda Mulalic (Engineering Manager).
Bygget i designet fra master-CV'erne. Sprog: engelsk (JD-sprog).

Vinkel: maskinmester-/marine-engineering-baggrund + 20 års teknisk levering på
tværs af mekanik, el, proces og automation — og ærlig håndtering af, at han bor
i Måløv, mens opslaget prioriterer ansøgere i Aalborg.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Technical Lead Engineer | Alfa Laval, Aalborg | Marine Boilers & Heaters"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv, Denmark")

DATE = "30 October 2026"
RECIPIENT = ("Alfa Laval Aalborg A/S · Marine & Offshore System, Marine Boilers & Heaters · "
             "Att: Elda Mulalic, Engineering Manager")
SUBJECT = "Application: Technical Lead Engineer — Aalborg"

# ------------------------------------------------------------------ side 1
OPENING = [
    "A technical lead owns the part of the project that cannot be delegated: the decisions. Which requirements are "
    "real, which compromise is acceptable, which risk is worth taking, and who has to know before it is taken. "
    "That is the work I have done for twenty years — as project and commissioning lead on 37 concurrent capital "
    "projects in a GMP environment, and as the owner of an authorised electrical company where the technical "
    "decision and the cost of getting it wrong were both mine.",
    "I am a marine engineer by education, and Alfa Laval in Aalborg is one of the few places in Denmark where that "
    "education points directly at the product: boilers, heaters, burners and heat recovery for ships that cannot "
    "afford to lose steam. Marine boilers are systems where mechanical, process, electrical, automation and "
    "manufacturing disciplines meet on the same drawing — which is exactly where I have spent my career.",
]

BULLETS = [
    ("Technical scope, owned end to end",
     "37 concurrent capital projects (DKK 2–10m each): requirements, technical decisions, schedule, cost and "
     "risk, with monthly reporting to management and customer. Deviations were raised, decided and closed — not "
     "carried until handover."),

    ("Multidisciplinary coordination, not just meetings",
     "Engineering, procurement, manufacturing and site operations coordinated across a 25-specialist "
     "organisation; daily interfaces to Quality, Maintenance and Production. I read the electrical drawing as "
     "well as the mechanical one — authorised electrical engineer LV/MV/HV — so interfaces get closed instead of "
     "forwarded."),

    ("Documentation and configuration discipline",
     "SOP and batch record discipline, deviation, CAPA and change control, FAT/SAT, IQ/OQ/PQ and validation "
     "documentation in a live audit trail. Zero critical findings at handover — because the documentation was "
     "written while the work happened, not reconstructed afterwards."),

    ("Risk, trade-offs and value engineering",
     "Technical risk assessed before it becomes a delay; cost targets held through supplier and component "
     "choices; −40% energy cost and +40% productivity delivered through structured PDCA, A3 and standardised "
     "work, both measured before and after."),

    ("Marine engineering as a foundation, not a label",
     "B.Tech in Technology Management & Mechanical Engineering from the Copenhagen School of Marine Engineering "
     "& Technology Management, with STCW engine-room watchkeeping (A-III/1) and maritime safety certificates; "
     "twenty years of steam, pumping, ventilation and 24/7 critical plant from the operations side."),
]

MIRROR = ("Against your requirements: bachelor's-level marine engineering degree (B.Tech, EQF 6) · industrial "
          "equipment, process engineering, manufacturing and capital projects as my daily work · technical risk, "
          "trade-offs and priorities assessed and documented · multidisciplinary engineering leadership across "
          "mechanical, electrical, process and automation · engineering documentation and configuration "
          "management · Lean and Six Sigma problem-solving tools · marine industry and maritime certification · "
          "English professional (working language), Danish native.")

HONEST = ("Two things stated plainly. First, I live in Måløv. Your posting prioritises candidates already in "
          "Aalborg, so I would rather say it in the first paragraph than have it discovered in the second "
          "interview: I am prepared to relocate for this role, and I would expect to be in Aalborg from the "
          "start rather than commuting into the job. Second, my career has been shoreside — I hold the STCW "
          "engine-room certificates of a marine engineer, but I apply as an engineer from the marine school, not "
          "as a former seafarer with sea time to show.")

CULTURE = ("Why Alfa Laval. Heat transfer, separation and fluid handling are three technologies that decide how "
           "much of the world's energy and material actually gets used — and the Aalborg site has been building "
           "marine boilers since Aalborg Industries' days, which Alfa Laval bought in 2011 precisely because that "
           "competence was worth owning. \"Pioneering positive impact\" and a 140-year-old start-up culture is a "
           "combination I recognise from the plants I have run: the engineering has to be old-fashioned solid, and "
           "the way it is improved has to stay curious.")

PRACTICAL = ("Practical: available at short notice, English as my professional working language and Danish as my "
             "native one, driving licence B and fully mobile between sites. On appointment I wind down my own "
             "company, so there are no competing commitments.")

CLOSING = ("I would welcome a conversation with you and Elda Mulalic — and I would rather spend it on a real "
           "project case than on my CV: give me one of your boiler or heater deliveries and I will tell you where "
           "I would put the technical risk, and what I would want decided before design freeze.")

# ------------------------------------------------------------------ CV
PROFILE = ("Marine engineer (B.Tech, Technology Management & Mechanical Engineering) and technical project lead "
           "with 20+ years in regulated manufacturing, process plant and critical technical operations, and "
           "leadership responsibility since 2003 with full P&L accountability. Has owned the technical execution "
           "of 37 concurrent capital projects — requirements, technical decisions, schedule, cost, risk and "
           "handover — coordinating mechanical, electrical, process and manufacturing disciplines across a "
           "25-specialist organisation. Strong on documentation and configuration discipline (deviation, CAPA, "
           "change control, FAT/SAT, IQ/OQ/PQ), on risk and value engineering, and on closing interfaces instead "
           "of forwarding them. Authorised electrical engineer (LV/MV/HV), STCW engine-room certified, Lean and "
           "Six Sigma problem-solving trained. Builds his own data tooling (SAP, Power BI, Python, Claude API). "
           "English professional, Danish native.")

PRACTICE = [
    ("Technical leadership of capital projects",
     "Technical scope owned from requirements to handover on 37 concurrent projects (DKK 2–10m each): "
     "specification, technical decisions, design reviews, supplier and component selection, project schedule, "
     "cost and risk — with the customer as the counterpart, not the audience."),

    ("Multidisciplinary coordination",
     "Mechanical, electrical, process, automation and manufacturing functions aligned across engineering, "
     "procurement and site operations; a 25-specialist organisation led cross-functionally, plus production "
     "teams, workshops and skilled trades. Interfaces documented, owners named, decisions logged."),

    ("Documentation, configuration and quality",
     "Engineering deliverables reviewed and approved; change control, deviation and CAPA handled in a live audit "
     "trail; FAT/SAT, IQ/OQ/PQ and validation documentation; ISO 13485 and GMP expectations; zero critical "
     "findings at handover."),

    ("Risk, value engineering and cost",
     "Technical risk registers, trade-off analysis and issue resolution; cost targets protected through "
     "component and supplier choices; −40% energy cost and +40% productivity delivered and measured in "
     "regulated production and technical service."),

    ("Continuous improvement and standardisation",
     "PDCA, A3, 8-step and DMAIC/Six Sigma problem solving, Kaizen and Just-Do-It actions, standard work and 5S; "
     "lessons learned captured in written standards that survived the project team — introduced in three "
     "operations."),

    ("Customer, sales and service interface",
     "Direct customer dialogue on technical scope, deviations and change orders; quotations, service agreements "
     "(SLA) and supplier negotiations as owner of an authorised company with full P&L responsibility."),
]

FIRST90 = [
    ("Days 1–30",
     "Learn the product before proposing anything: walk the Aalborg production flow, read a boiler and heater "
     "delivery from specification to test, and sit in on a customer FAT. Map which disciplines sign which "
     "deliverable today, and where the technical decisions actually get made."),
    ("Days 31–60",
     "Take technical ownership of one running project end to end: requirements confirmed with the customer, "
     "interfaces and risks logged, design review held with a written decision list. Establish the review and "
     "approval rhythm I will use on every project afterwards."),
    ("Days 61–90",
     "Standardise what is worth standardising: one risk format, one decision log, one lessons-learned routine fed "
     "back into the next order. Two or three improvements closed with measured effect — on engineering hours, "
     "rework or lead time, not on slides."),
    ("Year 1–2",
     "Trusted technical lead across the product range and the primary technical counterpart for Sales, Sourcing, "
     "Service and Manufacturing: fewer surprises at test and handover, shorter decision paths, and standards "
     "that stay in place when the project ends."),
]

MODELS = [
    ("Technical project leadership",
     "Technical scope ownership, requirements management, design reviews and decision logs, gate reviews, "
     "schedule and cost control, stakeholder alignment, supplier and component selection, handover"),
    ("Risk & trade-off management",
     "Technical risk register and FMEA, single-point-of-failure review, trade-off analysis between customer "
     "requirement, quality, cost, manufacturability and schedule, issue escalation and resolution"),
    ("Engineering documentation & configuration",
     "Specifications and design reports, drawing and BOM control, change control and deviation handling, CAPA, "
     "as-built and O&M documentation, validation documentation (FAT/SAT, IQ/OQ/PQ), audit-ready records"),
    ("Multidisciplinary engineering",
     "Mechanical and process (pumps, piping, heat exchangers, pressure equipment, steam and thermal systems), "
     "electrical (LV/MV/HV, switchgear, motors, protection), automation and controls (PLC, SCADA, BMS)"),
    ("Quality, standards & compliance",
     "ISO 9001 and ISO 13485 quality management, GMP/FDA expectations, customer specifications, Danish and EU "
     "requirements, classification and customer class requirements, ATEX and working-environment rules"),
    ("Lean & problem solving",
     "Lean and Six Sigma tools: DMAIC, 8-step and A3 problem solving, root cause (5 Why, Ishikawa), Kaizen and "
     "Just-Do-It, value stream mapping, standard work, 5S, SMED, TPM, Kanban, Poka-Yoke"),
    ("Cost & value engineering",
     "Cost targets and productivity pipeline, make-or-buy, component and supplier optimisation, business cases "
     "and investment models (NPV, IRR, sensitivity), quotation and SLA pricing"),
    ("Data, ERP & tools",
     "SAP ERP and CMMS, Power BI and Excel/Power Query, Python and Claude API for automated reporting, "
     "checklists and technical documentation flows"),
]

ACHIEVEMENTS = [
    ("Zero critical findings at handover",
     "across 37 concurrent capital projects (DKK 2–10m each) — documentation and qualification closed before "
     "handover, not after."),
    ("37 projects delivered in parallel",
     "with schedule, cost, technical risk and monthly reporting — without stopping the running operation."),
    ("−40% energy cost",
     "in regulated production through structured PDCA, A3 problem solving and standardised work — sustained "
     "after the project organisation was dissolved."),
    ("+40% productivity",
     "in a technical service operation through data-driven planning and standard work."),
    ("Standards introduced in three operations",
     "tiered daily management, written countermeasure routines and documentation discipline that outlived the "
     "people who introduced them."),
]

EXPERIENCE = [
    ("Owner / Technical Director / Authorised Electrical Installer",
     "ELOHVAC ApS · Copenhagen · May 2023 – Present",
     "5 electricians and 3 apprentices · 40+ service sites · full P&L, quotations and supplier agreements",
     [("Technical ownership",
       "specification, technical decisions and documentation for every installation; risk assessment, LOTO and "
       "documented service records; zero critical deviations in the portfolio."),
      ("Customer and commercial interface",
       "direct customer dialogue on scope, changes and deviations; quotations, service agreements and supplier "
       "negotiations with full P&L responsibility."),
      ("Delivery and cost",
       "daily planning, capacity against the order book, material and spare-part flow, quality control and cost "
       "— reviewed every morning against standard work, 5S and KPIs."),
      ("Digital backbone, built myself",
       "ERP-based order and spare-part control, Power BI dashboards and Python/Claude API tools for planning, "
       "quotations, checklists and reporting; productivity above +40%.")]),

    ("Senior Commissioning Engineer / Project Manager, Electrical Systems",
     "Novo Nordisk A/S · Kalundborg · Nov 2022 – Jul 2024",
     "37 concurrent capital projects, DKK 2–10m each · 25 specialists across engineering, procurement and site "
     "operations · GMP/FDA/EMA",
     [("Technical lead across disciplines",
       "requirements, technical decisions, design reviews, project schedule, cost and risk for 37 projects in "
       "parallel, with monthly reporting to management and key stakeholders."),
      ("Commissioning and qualification",
       "FAT/SAT, IQ/OQ/PQ and validation documentation with deviation handling, CAPA and change control in a "
       "live audit trail — zero critical findings at handover."),
      ("Energy programme",
       "−40% energy cost through PDCA, A3 problem solving and standardised work; SAP ERP for cost, asset and "
       "order control."),
      ("Process plant in operation",
       "daily work in clean rooms, warehouses and manufacturing: work permits, LOTO, contractor control and "
       "interfaces to Quality, Maintenance and Production.")]),

    ("Maintenance and Operations Manager / Workshop Technician",
     "Biofos (Lynetten) · Copenhagen · Aug 2017 – Jan 2022",
     "24/7 plant operations · pumps, HVAC, HV switchgear and SCADA · operations and maintenance budgets in SAP",
     [("24/7 critical plant",
       "uptime, preventive maintenance and fast fault-finding with zero tolerance for unplanned stops — steam, "
       "pumping, ventilation and control systems."),
      ("Technical standards and documentation",
       "standard work, 5S, PDCA preventive maintenance plan, A3 root-cause analysis, spare-part flow and "
       "critical stores."),
      ("Safety and compliance",
       "LOTO, risk assessment, near-miss reporting and toolbox talks; KPIs and budgets in SAP ERP.")]),

    ("Project and Workshop Manager, Ventilation & Climate",
     "Ventek-Air · Copenhagen · Jan 2022 – Nov 2022",
     "14-person production and assembly team · 11 concurrent projects (DKK 2–10m) · specification to formal "
     "handover",
     [("Production and assembly leadership",
       "capacity planning, flow control and standardised work across 11 concurrent projects, with a marked lift "
       "in delivery performance and first-time quality."),
      ("Technical documentation",
       "specifications, handover packages and safety documentation with suppliers and subcontractors.")]),

    ("Electromechanical Technician / Production Team Leader",
     "ARJ Engineering · Tehran · Dec 2003 – Mar 2010",
     "12-person production team · shift planning, material control and inventory",
     [("Production team leadership",
       "shift planning, material control, inventory and line-side supply, target management and situational "
       "coaching."),
      ("Technical problem solving",
       "repair and diagnosis of electrical and mechanical systems through structured root cause analysis.")]),
]

EDUCATION = [
    ("B.Tech (EQF Level 6) — Technology Management & Mechanical Engineering",
     "Copenhagen School of Marine Engineering & Technology Management · 2017 – 2022 · GPA 7.6/12"),
    ("Electrical & Mechanical Design, Electrical Engineering (EQF Level 6)",
     "Tehran Technical University · 2000 – 2003"),
    ("Upper Secondary Examination (HF, mathematics and physics)",
     "VUC · 2012 – 2017"),
]

CERTS = [
    ("Danish Electrical Installer Authorisation (LV/MV/HV)",
     "Danish Safety Technology Authority · May 2023"),
    ("STCW — Engine Room Watchkeeping (A-III/1)",
     "Danish Maritime Authority · Feb 2022"),
    ("STCW — Basic Tanker Operations (V/1-1, V/1-2) · Ship Security Officer (VI/5) · Security Awareness (VI/6-1)",
     "Danish Maritime Authority · 2021 – 2023"),
    ("Lean practice — value stream mapping, standard work, 5S, A3 and Kaizen",
     "Applied in operations · 2017 – present"),
    ("Problem solving — 8-step, A3, DMAIC and Six Sigma tools",
     "Applied in projects · 2017 – present"),
    ("Refrigeration Technology & HVAC (AMU)",
     "Mercantec · Mar 2021"),
]

LANGUAGES = ("English (professional, written and spoken — working language) · Danish (native) · "
             "Persian/Farsi (native) · Driving licence B")

REFERENCES = ("Former managers at Novo Nordisk A/S (Kalundborg) and Biofos (Lynetten) — available on request.")

KEYWORDS = (
    "Technical Lead Engineer · Technical Lead · Engineering Lead · Marine Engineering · Marine Engineer · "
    "Industrial Equipment · Process Engineering · Manufacturing · Capital Projects · CAPEX · Technical Scope · "
    "Technical Decision-Making · Customer Requirements · Quality Standards · Cost Targets · Safety Requirements · "
    "Project Timelines · Multidisciplinary · Mechanical · Electrical · Process · Automation · Technical Point of "
    "Contact · Stakeholders · Compliance · Technical Standards · Regulations · Customer Specifications · "
    "Engineering Deliverables · Technical Documentation · Configuration Management · Bill of Materials · Design "
    "Reviews · Technical Risk · Risk Management · Issue Resolution · Cost Optimization · Value Engineering · "
    "Sales · Sourcing · Service · Continuous Improvement · Standardization · Lessons Learned · Lean · Six Sigma · "
    "DMAIC · Root Cause Analysis · A3 · Kaizen · FAT · SAT · Commissioning · Validation · GMP · ISO 9001 · "
    "ISO 13485 · Marine Industry · Marine Boilers · Boilers · Burners · Heat Exchangers · Thermal Fluid Heaters · "
    "Exhaust Gas Economizer · Steam · Pumps · Hydraulics · Piping · Pressure Vessels · Welding · SAP · ERP · "
    "PLC · SCADA · Control Systems · Classification Requirements · STCW · Engine Room · Vessel · Ship · "
    "Offshore · Aalborg · English · Danish"
)


def build(path):
    m = MasterDoc(TEMPLATE, lang="en-GB")

    # ---------------------------------------------------------------- side 1
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta(RECIPIENT)

    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, SUBJECT, bold=True, color="1A1A1A")

    for t in OPENING:
        m.para(t, after=80)

    for label, body in BULLETS:
        m.bullet(label, body, after=40)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=80)

    m.meta("Yours sincerely,", after=20)
    m.meta("Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "ENGINEERING PROFILE")
    m.para(PROFILE, after=80)

    m.section("TECHNICAL LEADERSHIP — EVIDENCE, NOT CLAIMS")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("ENGINEERING METHODS & TOOLS — APPLIED IN PRACTICE",
                   ("Area", "Methods and tools"), MODELS)

    m.section("SELECTED ACHIEVEMENTS")
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

    m.section("CERTIFICATIONS & AUTHORISATIONS")
    for t, meta in CERTS:
        m.edu(t, meta)

    m.section("LANGUAGES")
    m.para(LANGUAGES, after=80, justify=False)

    m.section("REFERENCES")
    m.para(REFERENCES, after=80, justify=False)

    m.section("CORE COMPETENCIES & KEYWORDS")
    m.para(KEYWORDS, after=80)

    m.models_table("FIRST 90 DAYS — HOW I WOULD TAKE TECHNICAL OWNERSHIP",
                   ("When", "What is in place"), FIRST90)

    return m.save(path,
                  title="Application and CV — Technical Lead Engineer, Alfa Laval Aalborg",
                  subject="Technical lead · marine boilers and heaters · multidisciplinary engineering · "
                          "capital projects · Aalborg",
                  keywords=("technical lead engineer, marine engineering, boilers, heaters, process, automation, "
                            "multidisciplinary, capital projects, technical risk, documentation, configuration "
                            "management, six sigma, lean, aalborg, english"),
                  comments="Master design (navy banners, Calibri 9.5 pt). English, ATS-optimised. "
                           "Cover letter page 1, CV pages 2-4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_AlfaLaval_TechnicalLeadEngineer.docx")
    print("OK", build(out))
