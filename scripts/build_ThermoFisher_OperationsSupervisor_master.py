# -*- coding: utf-8 -*-
"""
Thermo Fisher Scientific — Operations Supervisor, Day (Roskilde, R-01372520).
Bygget i PRÆCIS designet fra master-CV'erne (navy bannere, Calibri 9,5 pt,
blå punkter, Area | Tools-tabel, EDUCATION / CERTIFICATIONS / LANGUAGES /
CORE KEYWORDS-sektioner). Sprog: engelsk (JD-sprog). Ansøgning + CV i ét dokument.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

TEMPLATE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = ("Operations Supervisor, Day | Thermo Fisher Scientific, Roskilde | "
         "Job ID R-01372520")
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Søborg, Denmark")

DATE = "30 October 2026"
RECIPIENT = ("Thermo Fisher Scientific · Roskilde, Denmark · Att: Hiring Manager, Operations · "
             "Fully onsite")
SUBJECT = "Application: Operations Supervisor, Day — Roskilde (R-01372520)"

OPENING = [
    "A GMP plant is not run from a meeting room. It is run at 07:00, at the tier-1 board, where the shift agrees "
    "what is true today: which line runs to standard, which deviation is still open, which material is not at the "
    "line, and who owns each countermeasure before the next huddle. Your posting describes that responsibility — "
    "daily production operations, quality and safety standards, team development and continuous improvement in a "
    "strict GMP and FDA framework, delivered through PPI. It is the operation I have run for twenty years, and the "
    "system for it is already built:",

    "Roskilde is real, highly automated production. My first ninety days follow that order: week one on the floor "
    "and at the boards, day thirty with tiered daily management and escalation live, day ninety with gains in "
    "safety, quality and delivery that hold without me standing next to them.",
]

BULLETS = [
    ("Running the day",
     "Tiered huddles, visual SQDIP boards, named owners, escalation inside the shift and Gemba walks that end "
     "where the problem is — over 37 concurrent CAPEX projects (DKK 2–10m each), a 14-person production team and "
     "25 specialists. Deviations caught in hours, not at month-end."),

    ("Improving the day",
     "PPI's own logic is my working method: 8-step problem solving and A3, Kaizen and Just-Do-It, value stream "
     "mapping, standard work, 5S, SMED, TPM and Poka-Yoke, root cause before countermeasure, ownership fixed by "
     "RACI. Documented: +40% productivity, −40% energy cost in regulated production."),

    ("Protecting the day",
     "Quality is documentation you can audit years later: SOP and batch record discipline, deviation handling, "
     "CAPA, change control, clean room and gowning, FAT/SAT and IQ/OQ/PQ — zero critical findings at handover at "
     "Novo Nordisk under GMP/FDA/EMA."),

    ("Safety before output",
     "Risk assessment, LOTO, safety walks and toolbox talks only matter with near-miss reporting followed to "
     "closure and a stop-the-line right people actually use. It is measured like every other KPI: an unsafe shift "
     "is a failed shift."),

    ("The team around the line",
     "Situational leadership, GROW coaching and SBI feedback, 1:1s and development reviews, competence matrices, "
     "30-60-90 onboarding, operator and apprentice training — with the psychological safety that makes the "
     "near-miss get reported. Teams of 5 to 25 in two countries."),

    ("Capacity, flow and changeover",
     "Takt and bottleneck analysis, capacity planning against the order book, line-side material and Kanban "
     "discipline, changeover reduction and standard work at every station — more output from the same assets "
     "before anyone buys capacity."),

    ("Across functions and systems",
     "Daily interfaces to Quality, Engineering, Supply Chain and Finance on one plan; SAP ERP and CMMS as source "
     "of truth, MS Office (Excel, PowerPoint, Word) and Power BI for the boards — plus my own tooling as a professional, active "
     "Claude coder: OEE and capacity models, shift dashboards and investment models with NPV, IRR and sensitivity "
     "for development and new business ideas."),
]

MIRROR = ("Mirrored against your requirements: 20+ years in operations management and supervisory experience since "
          "2003 for teams of 5–25 (2+ required) · Lean, continuous improvement and operational excellence as a "
          "daily system · problem-solving, decision-making, organizational skills and time management proven in "
          "24/7 critical operations · clear written and verbal communication, Danish and English · ERP (SAP) and "
          "Microsoft Office Suite · clean rooms, warehouses and manufacturing · safety and regulatory compliance "
          "with GMP, FDA and quality management systems from Novo Nordisk.")

HONEST = ("Two things, plainly. My supervisory years are in technical production, maintenance and project operations "
          "inside GMP — I have owned the daily management system, the people and the compliance, but not yet a "
          "moulding or filling line; that flow I will learn in weeks, because the system around it is the one I "
          "already run. And my written English is professional, not native; the boards and records I produce are "
          "concise and audit-ready.")

CULTURE = ("Why Thermo Fisher Scientific, and why Roskilde. PPI is the most complete version of what I already "
           "practise — 8-step problem solving, tiered accountability, Gemba, standard work, a project funnel and a "
           "bronze-to-gold maturity model, with supervisors trained in Leading Through PPI. The 4i Values read "
           "like an operating standard I recognise: Integrity as open communication and honoured commitments, "
           "Intensity as speed with excellence, Innovation as turning knowledge into something measurably better "
           "for the customer, Involvement as one global team. A site among the most automated in the world, where "
           "production is visible from your desk, is where a supervisor can move a number.")

PRACTICAL = ("Practical: day shift, fully onsite in Roskilde, short notice; on appointment I wind down my own "
             "company, so there are no competing commitments. Driving licence B, easy commute from Søborg.")

PROFILE = ("Operations and production leader with 20+ years in regulated manufacturing, technical operations and "
           "maintenance, and leadership responsibility since 2003 for teams of 5 to 25 with full P&L "
           "accountability. Runs daily management the way PPI expects it — tiered huddles, SQDIP boards, Gemba, "
           "escalation paths, A3 and 8-step problem solving, standard work — and develops people through "
           "situational leadership, coaching and competence matrices. Documented results: +40% productivity, "
           "−40% energy cost, zero critical deviations at handover under GMP/FDA/EMA. Professional and active "
           "Claude coder: builds the shift dashboards, OEE and capacity models and investment models the "
           "operation runs on. B.Tech in Technology Management & Mechanical Engineering (EQF 6); authorised "
           "electrical installer LV/MV/HV; Danish native, English professional.")

WHY = ("Because the mission is measurable here. Thermo Fisher enables customers to make the world healthier, "
       "cleaner and safer, and the Roskilde site makes that concrete in plastic ware, cell-culture and "
       "bioprocessing products where a deviation is not a delay but a patient risk. PPI gives a supervisor the "
       "right to fix what is wrong using a shared method — a project funnel, tiered accountability and a maturity "
       "model from bronze to gold — and the 4i Values make the standard of behaviour explicit. That combination, "
       "on a site among the most automated in the world and with a short distance from the line to the director's "
       "office, is where twenty years of regulated operations and a continuous-improvement habit belong.")

COMPETENCIES = [
    ("People leadership and team development",
     "Situational leadership (Hersey & Blanchard) adapted to task and maturity level. GROW coaching and SBI "
     "feedback. Systematic 1:1s, performance and development reviews, competence matrices and individual "
     "development plans. 30-60-90 onboarding, operator and apprentice training with checklists and own-account "
     "tasks. Psychological safety as the precondition for near-miss reporting. Teams of 5, 12, 14 and 25 in two "
     "countries."),

    ("Daily management and operational performance",
     "Tier-1 to tier-3 huddles, SQDIP boards, visual management, Gemba walks, escalation ladders and RACI. KPI "
     "set covering OEE, on-time delivery, first-pass yield, deviation and rework rate, MTBF/MTTR, absence and "
     "safety. Countermeasures tracked to closure with named owners and a monthly management review."),

    ("Lean, PPI and structured problem solving",
     "PPI 8-step problem solving, A3 thinking, Kaizen events and Just-Do-It actions, value stream mapping, "
     "standard work, 5S, SMED, TPM, Kanban and WIP control, Poka-Yoke, Ishikawa and 5 Why, FMEA, DMAIC/Six Sigma "
     "tools, Toyota Kata and Yokoten for spreading improvement. Results documented in productivity and energy."),

    ("Quality, GMP and regulatory compliance",
     "GMP/cGMP and FDA expectations, quality management systems and ISO 13485 awareness, SOP and batch record "
     "discipline, deviation handling, CAPA and change control, audit readiness and inspection support, FAT/SAT "
     "and IQ/OQ/PQ, clean room and gowning discipline. Zero critical deviations at handover at Novo Nordisk."),

    ("Safety, EHS and clean-room discipline",
     "Risk assessment (APV), LOTO, safety walks and toolbox talks, near-miss reporting followed to closure, "
     "stop-the-line authority, warehouse and manufacturing-area discipline, IMS and authority requirements across "
     "24/7 critical operations."),

    ("Digital, ERP and AI-supported operations",
     "SAP ERP and CMMS as source of truth; Power BI and Microsoft Office for boards and reporting; Python and "
     "Claude API/Claude Code for automated KPI reporting, OEE and capacity models, digital checklists and "
     "documentation flow; investment and scenario models (NPV, IRR, sensitivity) for development and new business "
     "cases. Documented productivity gain above 40% in planning and reporting."),
]

FIRST90 = [
    ("Days 1–7",
     "On the floor on the shift, not in an office: line walk with the operators, tier-1 huddle observation, "
     "SQDIP board review, open deviations and CAPAs, safety observations, and the top five losses documented with "
     "the team that owns them."),
    ("Days 8–30",
     "Baseline on one page: OEE, OTD, first-pass yield, deviation and rework rate, absence, and backlog by line — "
     "pulled from SAP and the QMS rather than from memory. Escalation ladder, tier structure and countermeasure "
     "ownership (RACI) confirmed with Quality, Maintenance and Supply Chain."),
    ("Days 31–60",
     "Two or three PPI Just-Do-It and Kaizen actions closed with measured effect; standard work and 5S restored at "
     "the bottleneck; shift handover and deviation reporting made auditable; competence matrix and 30-60-90 "
     "onboarding for every team member live."),
    ("Days 61–90",
     "One A3 on the largest loss with an owner, a deadline and a verified result — plus the reporting automated "
     "end-to-end (SAP ERP, Power BI, Python/Claude API) so the numbers arrive daily and the supervisors stay on the "
     "floor."),
]

MODELS = [
    ("People & team leadership",
     "Situational leadership (SLII), GROW coaching, SBI feedback, 1:1s and performance reviews, competence "
     "matrices, individual development plans, 30-60-90 onboarding, delegation ladder, psychological safety, "
     "360-degree feedback, recognition and absence conversations"),
    ("Daily management & KPIs",
     "Tiered huddles (tier 1–3), SQDIP boards, visual management, Gemba walks, escalation ladder, RACI, "
     "countermeasure tracking to closure, OEE, OTD, first-pass yield, deviation and rework rate, MTBF/MTTR, "
     "monthly management wheel"),
    ("PPI, Lean & problem solving",
     "PPI 8-step problem solving, A3, Kaizen events, Just-Do-It actions, value stream mapping, standard work, "
     "5S, visual management, SMED, TPM, Kanban and WIP control, Poka-Yoke, Jidoka, Ishikawa, 5 Why, FMEA, "
     "DMAIC/Six Sigma tools, Toyota Kata, Hansei and Yokoten"),
    ("Quality & regulatory",
     "GMP/cGMP, FDA expectations, quality management system, ISO 13485 awareness, SOP and batch record discipline, "
     "deviation, CAPA and change control, audit readiness and inspection support, FAT/SAT, IQ/OQ/PQ, clean room "
     "and gowning discipline, IMS"),
    ("Safety & EHS",
     "Risk assessment (APV), LOTO, safety walks, toolbox talks, near-miss reporting to closure, stop-the-line "
     "authority, warehouse and manufacturing-area discipline, authority requirements"),
    ("Projects & change",
     "Project management and stage-gate governance, critical path and milestones, schedule and cost control, "
     "stakeholder management, change management and change leadership (Kotter/ADKAR), supplier and subcontractor "
     "management, business case development"),
    ("Digital, ERP & AI",
     "SAP ERP, CMMS, Power BI, Excel/Power Query, Microsoft 365, Python, Claude API/Claude Code, prompt and agent "
     "design, automated KPI reporting, OEE and capacity models, investment models (NPV, IRR, sensitivity, "
     "scenarios), digital checklists and documentation flow"),
    ("Business & finance",
     "Full P&L responsibility, budget and cost control, productivity pipeline with validated savings, quotations "
     "and service agreements (SLA), procurement and supplier negotiation"),
]

ACHIEVEMENTS = [
    ("Zero critical deviations at handover",
     "across 37 concurrent CAPEX and plant projects (DKK 2–10m each) under GMP/FDA/EMA — deviation handling, CAPA "
     "and change control in a live audit trail."),
    ("+40% productivity",
     "in a technical service operation through data-driven planning, standard work and self-built AI tooling; the "
     "same operation reported response time, first-time quality and delivery daily instead of monthly."),
    ("−40% energy cost",
     "in regulated production through a structured PDCA programme with A3 problem solving and standardised work — "
     "sustained after the project team disbanded."),
    ("Tiered daily management introduced",
     "in three operations: month-end reporting replaced by visual boards, named countermeasures and same-shift "
     "escalation."),
    ("Teams built and developed",
     "across two countries — 25 specialists, a 14-person production team, a 12-person workshop and 5 electricians "
     "with 3 apprentices — with competence matrices and individual development plans."),
]

EXPERIENCE = [
    ("Owner / Technical Director / Authorised Electrical Installer",
     "ELOHVAC ApS · Copenhagen · May 2023 – Present",
     [("Full operating responsibility",
       "daily production planning, capacity against the order book, material and spare-part flow, quality control, "
       "on-time delivery and cost — reviewed every morning against standard work, 5S, visual boards and KPIs."),
      ("People leadership of 5 electricians and 3 apprentices",
       "daily planning, 1:1s and performance reviews, competence matrix, safety follow-up and structured training "
       "across shifting sites and priorities."),
      ("AI-supported management",
       "built the digital backbone myself — ERP-based order and spare-part control, Power BI dashboards and "
       "Python/Claude API tools for planning, quotations, checklists and reporting; productivity gain above 40%."),
      ("EHS and compliance",
       "risk assessment at every new site, LOTO, near-miss handling and documented service records; zero critical "
       "deviations in the service portfolio.")]),

    ("Senior Commissioning Engineer / Project Manager, Electrical Systems",
     "Novo Nordisk A/S · Kalundborg & Bagsværd · Nov 2022 – Jul 2024",
     [("37 concurrent CAPEX and plant projects (DKK 2–10m each)",
       "schedule, cost, risk, resources and monthly reporting to management and client across engineering, "
       "procurement and site operations."),
      ("Cross-functional leadership of 25 specialists",
       "commissioning and qualification (FAT/SAT, IQ/OQ/PQ, validation documentation) with deviation handling, "
       "CAPA and change control in a "
       "live audit trail — zero critical findings at handover under GMP/FDA/EMA."),
      ("Energy programme",
       "−40% energy cost through structured PDCA, A3 problem solving and standardised work; SAP ERP for cost, "
       "asset and order control."),
      ("Shop-floor reality",
       "daily work in clean room areas, warehouses and manufacturing: work permits, LOTO, gowning and clean-room "
       "discipline, interfaces to Quality, Maintenance and Production.")]),

    ("Project and Workshop Manager, Ventilation & Climate",
     "Ventek-Air · Copenhagen · Jan 2022 – Nov 2022",
     [("14-person production and assembly team",
       "daily leadership, capacity planning and flow control across 11 concurrent projects (DKK 2–10m) from "
       "specification to formal handover."),
      ("Daily huddles and bottleneck analysis",
       "standardised work at every station with a marked lift in delivery performance and first-time quality."),
      ("Suppliers and subcontractors",
       "contract basis, safety documentation and handover packages.")]),

    ("Maintenance and Operations Manager / Workshop Technician",
     "Biofos (Lynetten) · Copenhagen · Aug 2017 – Jan 2022",
     [("24/7 critical operations",
       "pumps, HVAC, high-voltage switchgear and SCADA — uptime, preventive maintenance and fast fault-finding "
       "with zero tolerance for unplanned stops."),
      ("Structured maintenance",
       "standard work, 5S, PDCA preventive maintenance plan, A3 root-cause analysis, spare-part flow and "
       "critical stores."),
      ("Shift operations and safety discipline",
       "LOTO, risk assessment, near-miss reporting and toolbox talks; KPIs and operations budgets in SAP ERP.")]),

    ("Electromechanical Technician / Production Team Leader",
     "ARJ Engineering · Tehran · Dec 2003 – Mar 2010",
     [("12-person production team",
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
    ("Lean practice — 5S, PDCA, value stream mapping, A3 and Kaizen",
     "Applied in operations · 2017 – present"),
    ("Refrigeration Technology & HVAC (AMU)",
     "Mercantec · Mar 2021"),
    ("STCW — Engine Room Watchkeeping (A-III/1)",
     "Danish Maritime Authority · Feb 2022"),
    ("STCW — Designated Security Duties (VI/6)",
     "Danish Maritime Authority · Apr 2023"),
    ("STCW — Ship Security Officer (VI/5)",
     "Danish Maritime Authority · May 2021"),
    ("STCW — Basic Tanker Operations (V/1-1, V/1-2)",
     "Danish Maritime Authority · May 2021"),
    ("STCW — Security Awareness (VI/6-1) · Maritime Safety, Working Environment (§16)",
     "Danish Maritime Authority · May 2021"),
]

LANGUAGES = "Danish (native) · English (professional, written and spoken) · Persian/Farsi (native) · Driving licence B"

KEYWORDS = (
    "Operations Supervisor · Operations Management · Manufacturing · Production · Daily Management · Tier Meetings · "
    "SQDIP · Visual Management · Gemba · KPI · OEE · OTD · Lean Manufacturing · Continuous Improvement · Operational "
    "Excellence · PPI · Practical Process Improvement · 8-Step Problem Solving · Kaizen · 5S · Value Stream Mapping · "
    "Standard Work · SMED · TPM · Root Cause Analysis · A3 · DMAIC · Six Sigma · Problem Solving · Decision Making · "
    "Time Management · GMP · cGMP · FDA · Quality Management System · ISO 13485 · CAPA · Deviation · Change Control · "
    "Batch Record · SOP · Audit Readiness · Clean Room · Warehouse · EHS · Safety · Regulatory Compliance · "
    "Pharmaceutical · Medical Device · Regulated Manufacturing · ERP · SAP · Microsoft Office · Excel · Power BI · "
    "Cross-Functional · Team Development · Coaching · Situational Leadership · Performance Management · Competence "
    "Development · Employee Engagement · Change Leadership · Python · Claude API · AI · Investment Models · NPV · IRR · "
    "Roskilde · Thermo Fisher Scientific · Danish · English"
)


def build(path):
    m = MasterDoc(TEMPLATE, lang="en-GB")

    # ---------------------------------------------------------------- page 1
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta(RECIPIENT)

    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, SUBJECT, bold=True, color="1A1A1A")

    for t in OPENING:
        m.para(t, after=80)

    for label, body in BULLETS:
        m.bullet(label, body, after=30)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL):
        m.para(t, after=80)

    m.meta("Yours sincerely,", after=20)
    m.meta("Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- page 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "LEADERSHIP PROFILE")
    m.para(PROFILE, after=80)

    m.section("WHY I AM APPLYING TO THERMO FISHER SCIENTIFIC")
    m.para(WHY, after=80)

    m.section("MANAGEMENT COMPETENCIES — ALL TOOLS APPLIED IN PRACTICE")
    for label, body in COMPETENCIES:
        m.bullet(label, body, after=30)

    m.models_table("MANAGEMENT MODELS & METHODS — APPLIED IN PRACTICE",
                   ("Area", "Tools"), MODELS)

    m.section("SELECTED ACHIEVEMENTS")
    for label, body in ACHIEVEMENTS:
        m.bullet(label, body, after=30)

    for title, meta, bullets in EXPERIENCE:
        m.job(title, meta)
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

    m.section("CORE KEYWORDS (ATS)")
    m.para(KEYWORDS, after=80)

    m.models_table("FIRST 90 DAYS — THE SYSTEM I BRING",
                   ("When", "What is in place"), FIRST90)

    return m.save(path,
                  title="Application and CV — Operations Supervisor, Day, Thermo Fisher Scientific, Roskilde",
                  subject="Operations Supervisor · PPI · GMP manufacturing · Roskilde (R-01372520)",
                  keywords=("operations supervisor, operations management, manufacturing, GMP, FDA, lean, PPI, "
                            "continuous improvement, kaizen, 5S, standard work, ERP, SAP, Power BI"),
                  comments="Master design (navy banners, Calibri 9.5 pt). English, ATS-optimised.")


if __name__ == "__main__":
    out = "/home/user/Claude/Shahram_Ajloo_ThermoFisher_OperationsSupervisor.docx"
    print("OK", build(out))
