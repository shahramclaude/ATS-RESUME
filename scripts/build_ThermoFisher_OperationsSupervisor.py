# -*- coding: utf-8 -*-
"""Thermo Fisher Scientific — Operations Supervisor, Day (Roskilde). Job ID R-01372520.
Cover letter + CV in one document, English (JD language), ATS-optimised."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ats_builder import Application

a = Application()

DATE = "30 October 2026"
RECIPIENT = ("Thermo Fisher Scientific · Roskilde, Denmark · Hiring Manager, Operations · "
             "Job ID R-01372520 · Fully onsite · thermofisher.com")
SUBJECT = "Application: Operations Supervisor, Day — Roskilde (Job ID R-01372520)"

OPENING = [
    "**In a regulated plant, a shift is decided before the first batch record is signed.** It is decided at the "
    "tier-1 board at 07:00 — whether the line runs to standard, the clean room is released, and every operator "
    "knows what good looks like today. That is the job you describe: daily production operations, quality and "
    "safety standards, team development and continuous improvement inside a strict GMP and FDA framework. The "
    "system for it is already built:",

    "Roskilde means real, highly automated production, PPI as the way work is improved, and GMP discipline as the "
    "floor everyone stands on. My first 90 days follow that order: week 1 on the floor and at the boards, day 30 "
    "with tiered daily management live, day 90 with measurable gains in safety, quality and delivery.",
]

POINTS = [
    ("Daily production operations and tiered daily management",
     "Tier-1 huddle at the line, visual SQDIP board (Safety, Quality, Delivery, Inventory, Productivity), named "
     "owners per countermeasure, escalation within the shift, Gemba walk that ends where the problem is. "
     "Documented: 25 technicians across 37 parallel CAPEX projects, a 14-person team, 5 operators + 3 apprentices "
     "with full P&L. Effect: deviations caught in hours, not at month-end."),

    ("PPI, Lean and operational excellence",
     "PPI 8-step problem solving and A3, Kaizen events and Just-Do-It actions, value stream mapping, standard "
     "work, 5S, visual management, SMED, TPM, Poka-Yoke, 5 Why, Ishikawa — root cause before countermeasure, "
     "RACI ownership and an escalation ladder everyone knows. Documented: +40% productivity, −40% "
     "energy cost through structured PDCA, zero critical deviations at handover. Added to that: takt and bottleneck "
     "analysis, capacity planning against the order book, Kanban discipline and changeover reduction. Effect: "
     "more output from the same assets."),

    ("GMP, FDA and quality management systems",
     "FAT/SAT, IQ/OQ/PQ, deviation handling, CAPA, change control, SOP and batch documentation, gowning and "
     "clean-room behaviour, audit readiness — Novo Nordisk under GMP/FDA/EMA, zero critical findings at handover; "
     "24/7 critical operations under IMS."),

    ("Safety and EHS as the first KPI",
     "LOTO, risk assessment, safety walks, near-miss reporting followed to closure, toolbox talks, and a "
     "stop-the-line right people actually use. Effect: everyone goes home the way they came."),

    ("Team development and supportive leadership",
     "Situational leadership (SLII), GROW coaching, SBI feedback, 1:1s and development reviews, competence "
     "matrices, 30-60-90 onboarding, operator and apprentice training, psychological safety so the near-miss is "
     "reported. Effect: capable people who stay."),


    ("Cross-functional work, ERP and AI-supported management",
     "Deliberate interfaces to Quality, Engineering, Supply Chain and Finance — one shared plan, written "
     "follow-up. SAP ERP and CMMS as source of truth, Power BI and Office for the boards, plus my own tools as a "
     "professional, active Claude coder (Python, Claude API): shift dashboards, OEE and capacity models, "
     "automated KPI reporting and investment models for development and new business ideas — so the supervisor "
     "spends the shift on the floor, not in spreadsheets."),

]

MIRROR = ("**Mirrored to your requirements:** 20+ years in operations management (5+ required), 20 years of "
          "supervisory responsibility for teams of 5 to 25 (2+ required) · Lean and continuous improvement as a "
          "daily system · problem-solving, decision-making and time management proven in 24/7 critical operations "
          "· cross-functional communication, Danish and English · SAP ERP, Office, Power BI · clean rooms, "
          "warehouses, manufacturing · documented safety and regulatory commitment.")

HONEST = ("**Two things, plainly:** my supervisory years are in technical production, maintenance and project "
          "operations inside GMP — I have run the daily management system, the people and the compliance, but not "
          "yet a moulding or filling line; that flow I will learn in weeks, because the system around it is the "
          "one I already run. And my Danish is native, my written English professional.")

CULTURE = ("**Why Thermo Fisher Scientific, and why Roskilde:** because PPI is the most complete version of what I "
           "already practise — 8-step problem solving, tiered accountability, Gemba, standard work, a project "
           "funnel and a bronze-to-gold maturity model, supervisors trained in Leading Through PPI. The 4i "
           "Values mirror my own principles: Integrity as open communication, Intensity as "
           "speed with excellence, Innovation as turning knowledge into something better for the customer, and "
           "Involvement as one global team. A site among the most automated in the world, where you can see the "
           "production from your desk, is where a supervisor makes a difference.")

PRACTICAL = ("**Practical:** day shift, fully onsite in Roskilde, short notice; on appointment I wind down my own "
             "company, so there are no competing commitments. Danish and English, driving licence B, easy commute "
             "from Måløv. I would welcome a conversation about the site's PPI maturity and where the next 12 "
             "months of improvement should land.")

PROFILE = ("Operations and production leader with 20+ years in regulated manufacturing, technical operations and "
           "maintenance, including 20 years of supervisory responsibility for teams of 5 to 25 and full P&L "
           "accountability. Documented Lean and operational excellence results: +40% productivity through "
           "data-driven planning and standard work, −40% energy cost through structured PDCA, zero critical "
           "deviations at handover under GMP/FDA/EMA. Runs daily management the way PPI expects it — tiered "
           "huddles, SQDIP boards, Gemba walks, escalation paths, A3 and 8-step problem solving, standard work, "
           "5S, VSM, SMED, TPM and Kaizen — and develops people through situational leadership (SLII), GROW "
           "coaching, SBI feedback, 1:1s and competence matrices. ERP (SAP), CMMS, Power BI and Microsoft "
           "Office; professional and active Claude coder (Python, Claude API) building shift dashboards, OEE "
           "and capacity models and investment/scenario models. B.Tech in Technology Management & Mechanical "
           "Engineering (EQF 6), authorised electrical engineer LV/MV/HV. Danish fluent, English professional.")

TOOLBOX = [
    ("Operational excellence and PPI-equivalent methods",
     "PPI 8-step problem solving · A3 thinking · Kaizen events and Just-Do-It actions · value stream mapping · "
     "standard work · 5S and visual management · tiered daily management and huddles · Gemba walks · project "
     "funnel and idea hopper · maturity thinking (bronze–silver–gold) · DMAIC and Six Sigma tools · SMED · TPM · "
     "Kanban and WIP control · Poka-Yoke · Jidoka · 5 Why · Ishikawa · FMEA · Toyota Kata · Yokoten "
     "(best-practice sharing)."),
    ("Performance management and KPIs",
     "SQDIP boards (Safety, Quality, Delivery, Inventory, Productivity) · OEE, OTD, first-pass yield, deviation "
     "and rework rate, MTBF/MTTR · daily, weekly and monthly review cadence · escalation ladder · RACI · "
     "countermeasure tracking to closure · capacity planning against the order book · monthly management "
     "reporting."),
    ("People leadership and team development",
     "Situational leadership (SLII) · GROW coaching · SBI feedback · 1:1s, performance and development reviews · "
     "competence matrices and individual development plans · structured onboarding (30-60-90) · operator and "
     "apprentice training with checklists · psychological safety · recognition and motivation · absence and "
     "wellbeing conversations · conflict handling · change leadership."),
    ("Quality, compliance and EHS",
     "GMP/cGMP and FDA expectations · quality management systems · SOP and batch documentation discipline · "
     "deviation handling, CAPA and change control · audit readiness and inspection support · FAT/SAT, IQ/OQ/PQ · "
     "clean-room and gowning discipline · risk assessment (APV), LOTO, near-miss reporting, toolbox talks, "
     "safety walks · ISO 13485 awareness · IMS."),
    ("Systems, data and AI",
     "SAP ERP · CMMS · Power BI · Excel/Power Query · Microsoft 365 · Python · Claude API/Claude Code · "
     "prompt and agent design · automated KPI reporting · OEE and capacity models · investment and scenario "
     "models (NPV/IRR, sensitivity) · digital checklists and documentation flow."),
    ("Business and interfaces",
     "P&L and budget responsibility · cost control · supplier and subcontractor management · cross-functional "
     "planning with Quality, Engineering, Supply Chain and Finance · customer and service-level follow-up."),
]

EXPERIENCE = [
    {"job": "Owner / Technical Director / Authorised Electrical Installer",
     "meta": "ELOHVAC ApS · Copenhagen, Denmark · May 2023 – Present",
     "bullets": [
         "Full P&L responsibility for a technical service and installation operation: daily production planning, "
         "capacity against the order book, material and spare-part flow, quality control and on-time delivery.",
         "Supervision and development of 5 electricians and 3 apprentices: daily planning, 1:1s and performance "
         "reviews, competence matrix, safety follow-up and structured training — situational leadership across "
         "shifting sites and priorities.",
         "Standard work, 5S on workshop and stores, visual boards and KPI follow-up for response time, first-time "
         "quality and delivery performance.",
         "Digital and AI-supported management: ERP-based order and spare-part control, Power BI dashboards, and "
         "own Python/Claude API tools for planning, quotations, checklists and reporting — documented productivity "
         "gain above 40%.",
         "EHS and compliance: risk assessment at every new site, LOTO, near-miss handling, documented service "
         "records; zero critical deviations in the service portfolio.",
     ]},
    {"job": "Senior Commissioning Engineer / Project Manager, Electrical Systems",
     "meta": "Novo Nordisk A/S · Kalundborg / Bagsværd, Denmark · Nov 2022 – Jul 2024",
     "bullets": [
         "37 concurrent CAPEX and plant projects (DKK 2–10m each): schedule, cost, risk and resources across "
         "engineering, procurement and site operations, with monthly reporting to management and the client.",
         "Cross-functional leadership of 25 highly specialised colleagues; commissioning and qualification "
         "(FAT/SAT, IQ/OQ/PQ) under GMP/FDA/EMA — zero critical deviations at handover, with deviation handling, "
         "CAPA and change control in a regulated documentation flow.",
         "−40% energy cost through a structured PDCA programme with A3 problem solving and standard work; SAP ERP "
         "for cost, asset and order control.",
         "Daily coordination in clean rooms, technical areas and warehouses: work permits, LOTO, gowning and "
         "clean-room discipline, and interfaces to Quality, Maintenance and Production.",
     ]},
    {"job": "Project and Workshop Manager, Ventilation & Climate",
     "meta": "Ventek-Air · Copenhagen, Denmark · Jan 2022 – Nov 2022",
     "bullets": [
         "11 concurrent projects (DKK 2–10m) from specification to formal handover; daily leadership of a "
         "14-person production and assembly team with capacity planning and flow control.",
         "Daily huddles and bottleneck analysis; standardised work at every station with a marked lift in delivery "
         "performance and first-time quality.",
         "Supplier and subcontractor management, contract basis, safety documentation and handover packages.",
     ]},
    {"job": "Maintenance and Operations Manager / Workshop Technician",
     "meta": "Biofos (Lynetten wastewater treatment plant) · Copenhagen, Denmark · Aug 2017 – Jan 2022",
     "bullets": [
         "24/7 critical operations: pumps, HVAC, high-voltage switchgear and SCADA — uptime, preventive "
         "maintenance and fast fault-finding under zero tolerance for unplanned stops.",
         "Introduced structured maintenance routines (standard work, 5S), PDCA-based preventive maintenance and "
         "A3 root-cause analysis; spare-part flow and stores management for critical operations.",
         "Shift operations with safety discipline: LOTO, risk assessment, near-miss reporting and toolbox talks; "
         "documented KPIs and operations budgets in SAP ERP.",
     ]},
    {"job": "Electromechanical Technician / Production Team Leader",
     "meta": "ARJ Engineering · Tehran, Iran · Dec 2003 – Mar 2010",
     "bullets": [
         "Led a 12-person production team in a machine workshop: shift planning, material control, target "
         "management and situational coaching.",
         "Fault diagnosis and repair of industrial electrical and mechanical systems; structured root-cause "
         "analysis and corrective action.",
     ]},
]

EDUCATION = [
    "B.Tech (EQF level 6), Technology Management & Mechanical Engineering — Copenhagen School of Marine "
    "Engineering & Technology Management, 2017–2022 · GPA 7.6/12 (ECTS).",
    "Danish electrical authorisation LV/MV/HV — Danish Safety Technology Authority "
    "(Sikkerhedsstyrelsen), May 2023.",
    "Electrical & Mechanical Design, Electrical Engineering (EQF level 6) — Tehran Technical University, "
    "2000–2003.",
    "Refrigeration & HVAC technology (AMU) — Mercantec, 2021.",
    "Upper secondary (HF, mathematics/physics) — VUC, 2012–2017.",
    "STCW: engine-room watch (A-III/1), designated safety duties (VI/6), ship security officer (VI/5), security "
    "awareness (VI/6-1), tanker basic (V/1-1, V/1-2) — Danish Maritime Authority, 2021–2023.",
    "Lean practice: 5S, PDCA, value stream mapping, A3 and Kaizen.",
    "Languages: Danish (native), English (professional), Persian/Farsi (native) · Driving licence B.",
]

CORE = [
    "Daily production operations: tiered huddles, SQDIP boards, Gemba walks, escalation and countermeasure "
    "follow-up in a regulated manufacturing environment.",
    "Quality and compliance: GMP/FDA and quality management systems, SOP and batch documentation, deviation, "
    "CAPA and change control, audit readiness.",
    "Lean and continuous improvement: 8-step problem solving, A3, Kaizen, VSM, standard work, 5S, SMED, TPM, "
    "visual management.",
    "Team development: situational leadership, coaching, 1:1s, competence matrices, operator and apprentice "
    "training, 30-60-90 onboarding.",
    "Safety and EHS: risk assessment, LOTO, near-miss reporting, toolbox talks, safety walks, clean-room and "
    "warehouse discipline.",
    "People and organisation: supervisory leadership, team development, coaching, decision-making, organizational "
    "and time management, strong interpersonal skills across functions and levels.",
    "Data and systems: ERP (SAP), CMMS, Power BI, Microsoft Office, Python/Claude API for dashboards, OEE, "
    "capacity and investment models.",
]

KEYWORDS = (
    "operations supervisor · operations management · manufacturing · production · production supervisor · "
    "shift · daily management · tier meetings · daily huddles · visual management · Gemba · KPI · SQDIP · OEE · "
    "OTD · lean manufacturing · continuous improvement · operational excellence · PPI · Practical Process "
    "Improvement · 8-step problem solving · kaizen · 5S · value stream mapping · standard work · SMED · TPM · "
    "root cause analysis · A3 · DMAIC · Six Sigma · problem solving · decision making · time management · "
    "GMP · cGMP · FDA · quality management system · ISO 13485 · CAPA · deviation · change control · batch "
    "record · SOP · audit readiness · clean room · warehouse · EHS · safety · regulatory compliance · "
    "organizational skills · interpersonal skills · "
    "pharmaceutical · medical device · regulated manufacturing · ERP · SAP · Microsoft Office · Excel · "
    "Power BI · cross-functional · team development · coaching · situational leadership · performance "
    "management · competence development · employee engagement · change leadership · Python · Claude API · "
    "AI · Danish · English"
)

a.cover_letter(
    date=DATE, recipient=RECIPIENT, subject=SUBJECT, opening=OPENING, points=POINTS,
    mirror=MIRROR, honest=HONEST, culture=CULTURE, practical=PRACTICAL,
    signoff="Sincerely,",
    signature="Shahram Ajloo",
    contact="+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark",
)

a.resume(
    name="Shahram Ajloo",
    title="Operations Supervisor · Lean & Operational Excellence (PPI) · GMP-Regulated Manufacturing",
    contact="+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark — Roskilde",
    profile=PROFILE, toolbox=TOOLBOX,
    toolbox_title="Leadership and operational toolkit — all applied in practice",
    experience=EXPERIENCE, education=EDUCATION, core=CORE,
    core_title="Core competencies for operations supervision",
    keywords=KEYWORDS,
    profile_title="Profile",
    experience_title="Professional experience",
    education_title="Education and certifications",
    keywords_title="Keywords (ATS)",
)

out = "/home/user/Claude/Shahram_Ajloo_ThermoFisher_OperationsSupervisor_EN.docx"
a.save(out,
       title="Application and CV — Operations Supervisor, Day, Thermo Fisher Scientific Roskilde (R-01372520)",
       subject="Operations Supervisor · Lean/PPI · GMP manufacturing · Roskilde",
       keywords=("operations supervisor, operations management, manufacturing, GMP, FDA, lean, continuous "
                 "improvement, PPI, kaizen, 5S, standard work, root cause analysis, ERP, SAP, Power BI"),
       comments="Cover letter + CV in one document. English, ATS-optimised.")
print("OK", out)
