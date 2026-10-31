# -*- coding: utf-8 -*-
"""
Thermo Fisher Scientific — Operations Supervisor, Day (Roskilde, R-01372520).
Bygget i PRÆCIS designet fra master-CV'erne (navy bannere, Calibri 9,5 pt,
blå punkter, Area | Tools-tabel, EDUCATION / CERTIFICATIONS / LANGUAGES /
KEYWORDS-sektioner). Sprog: engelsk (JD-sprog). Ansøgning + CV i ét dokument.

Redaktionelle principper (gælder også ved genbrug til nye JD'er):
  * Ansøgningen handler om opgaven, missionen og det system han stiller op —
    ikke om ham. Maks. 1 side, korte punktlinjer.
  * CV'et dokumenterer: profil → ledelse i praksis (resultater) → metoder →
    resultater → erfaring med SCOPE pr. stilling → uddannelse → certifikater.
  * Ingen gentagelse mellem sektioner: tabellen = værktøjer, bulletlinjerne =
    effekt/bevis, ACHIEVEMENTS = overskrifter med tal.
  * Nøgleord står i kontekst; den afsluttende liste er til ATS-parseren.
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
           "Måløv, Denmark")

DATE = "30 October 2026"
RECIPIENT = ("Thermo Fisher Scientific · Roskilde, Denmark · Att: Hiring Manager, Operations · "
             "Fully onsite")
SUBJECT = "Application: Operations Supervisor, Day — Roskilde (R-01372520)"

# ------------------------------------------------------------------ side 1
OPENING = [
    "A GMP plant is not run from a meeting room. It is decided at 07:00, at the tier-1 board, where the shift "
    "agrees what is true today: which line is running to standard, which deviation is still open, which material "
    "is not at the line, and who owns each countermeasure before the next huddle. That is the responsibility in "
    "your posting — daily operations, quality and safety standards, team development and continuous improvement "
    "in a strict GMP and FDA framework, delivered through PPI. It is the operation I have run for twenty years, "
    "and the system for it is already built.",

    "Roskilde is not a generic site. It runs some of the most automated production in the world — plastic ware, "
    "cell-culture and bioprocessing products — where a deviation is not a delay but a patient risk, and where "
    "the distance from the line to the director's office is deliberately short. That is a site where a supervisor "
    "can still move a number within a quarter.",
]

BULLETS = [
    ("Running the shift to standard",
     "Tier-1 and tier-2 huddles, a visual SQDIP board, named owners, escalation inside the shift and Gemba walks "
     "that end where the problem is — proven across 37 concurrent CAPEX projects (DKK 2–10m each), a 14-person "
     "production team and 25 specialists. Deviations are caught in hours, not at month-end."),

    ("PPI as the working method, not a programme",
     "8-step problem solving and A3, Kaizen and Just-Do-It, value stream mapping, standard work, 5S, SMED and "
     "Poka-Yoke; root cause before countermeasure, ownership fixed by RACI. Documented: +40% productivity and "
     "−40% energy cost in regulated production."),

    ("Quality and safety that survive an audit",
     "SOP and batch record discipline, deviation handling, CAPA, change control, clean room and gowning, FAT/SAT "
     "and IQ/OQ/PQ — zero critical findings at handover at Novo Nordisk under GMP/FDA/EMA. Safety is measured "
     "like every other KPI: an unsafe shift is a failed shift."),

    ("The team around the line",
     "Situational leadership, GROW coaching and SBI feedback, 1:1s, competence matrices and 30-60-90 onboarding, "
     "with the psychological safety that makes a near-miss get reported — teams of 5 to 25 in two countries."),
]

MIRROR = ("Against your listed requirements: 20+ years in operations management and supervisory experience since "
          "2003 for teams of 5–25 · Lean and continuous improvement run as a daily system, not a project · "
          "ERP (SAP) and the full MS Office suite · daily work in clean rooms, warehouses and manufacturing · "
          "quality management systems, GMP and FDA from Novo Nordisk · Danish native, professional English.")

HONEST = ("One thing stated plainly: my supervisory years sit in technical production, maintenance and project "
          "operations inside GMP, not on a moulding or filling line. The daily management system, the people and "
          "the compliance I have owned; the line itself I will learn in weeks, because the system around it is "
          "already the one I run.")

CULTURE = ("Why Thermo Fisher Scientific, and why now. PPI is the most complete version of what I already practise "
           "— 8-step problem solving, tiered accountability, Gemba, standard work, a project funnel and a "
           "bronze-to-gold maturity model, with supervisors trained in Leading Through PPI. The 4i Values are an "
           "operating standard I recognise: Integrity in open communication and honoured commitments, Intensity as "
           "speed with excellence, Innovation as knowledge turned into something measurably better for the "
           "customer, and Involvement as one global team.")

PRACTICAL = ("Practical: day shift, fully onsite in Roskilde, short notice, driving licence B and an easy commute "
             "from Måløv. On appointment I wind down my own company, so there are no competing commitments.")

CLOSING = ("I would welcome a conversation on site. Thirty minutes on the floor with the shift is worth more than "
           "another page of prose — and I will bring the one-page baseline and the tier-1 board I would stand up in "
           "week one.")

# ------------------------------------------------------------------ CV
PROFILE = ("Operations and production leader with 20+ years in regulated manufacturing, technical operations and "
           "maintenance, and leadership responsibility since 2003 for teams of 5 to 25 with full P&L "
           "accountability. Runs daily management the way PPI expects it — tiered huddles, SQDIP boards, Gemba, "
           "escalation paths, A3 and 8-step problem solving, standard work — and develops people through "
           "situational leadership, coaching and competence matrices. Documented results: +40% productivity, "
           "−40% energy cost, zero critical deviations at handover under GMP/FDA/EMA. Professional and active "
           "Claude coder: builds the shift dashboards, OEE, capacity and investment models the operation runs on. "
           "B.Tech in Technology Management & Mechanical Engineering (EQF 6); authorised electrical engineer "
           "LV/MV/HV; Danish native, English professional.")

PRACTICE = [
    ("Daily management in practice",
     "tier-1 to tier-3 huddles against a fixed SQDIP board, named countermeasure owners and escalation inside the "
     "shift; OEE, on-time delivery, first-pass yield, deviation and rework rate reviewed daily instead of at "
     "month-end. Introduced in three operations and still running after I left."),

    ("Improvement with a verified effect",
     "+40% productivity in a technical service operation and −40% energy cost in regulated production — both "
     "through PDCA, A3 and standardised work, both measured before and after, and both sustained after the "
     "project team disbanded."),

    ("Compliance treated as routine",
     "SOP and batch record discipline, deviation and CAPA handling, change control, audit readiness and "
     "inspection support; zero critical findings at handover across 37 CAPEX projects, in a live GMP/FDA/EMA "
     "audit trail with documentation that could be read years later."),

    ("People developed on purpose",
     "competence matrices and individual development plans for 25 specialists, a 14-person production team and "
     "5 electricians with 3 apprentices; 30-60-90 onboarding, apprentice training and structured 1:1s. Absence "
     "and retention handled early, not at the exit interview."),

    ("AI-supported operations (the differentiator)",
     "self-built tooling on SAP ERP, Power BI, Python and the Claude API: automated KPI reporting, OEE and "
     "capacity models, digital checklists and documentation flow, plus investment models with NPV, IRR and "
     "sensitivity for development and new business cases."),
]

FIRST90 = [
    ("Days 1–7",
     "On the floor on the shift, not in an office: line walk with the operators, tier-1 huddle observation, "
     "SQDIP board review, open deviations and CAPAs, safety observations, and the top five losses documented "
     "with the team that owns them."),
    ("Days 8–30",
     "Baseline on one page: OEE, OTD, first-pass yield, deviation and rework rate, absence and backlog by line — "
     "pulled from SAP and the QMS rather than from memory. Escalation ladder, tier structure and countermeasure "
     "ownership (RACI) confirmed with Quality, Maintenance and Supply Chain."),
    ("Days 31–60",
     "Two or three PPI Just-Do-It and Kaizen actions closed with measured effect; standard work and 5S restored "
     "at the bottleneck; shift handover and deviation reporting made auditable; competence matrix and 30-60-90 "
     "onboarding live for every team member."),
    ("Days 61–90",
     "One A3 on the largest loss with an owner, a deadline and a verified result — plus reporting automated "
     "end-to-end (SAP ERP, Power BI, Python/Claude API) so the numbers arrive daily and the supervisors stay on "
     "the floor."),
]

MODELS = [
    ("People & team leadership",
     "Situational leadership (SLII), GROW coaching, SBI feedback, 1:1s and performance reviews, competence "
     "matrices, individual development plans, 30-60-90 onboarding, delegation ladder, psychological safety, "
     "360-degree feedback, absence and recognition conversations"),
    ("Daily management & KPIs",
     "Tiered huddles (tier 1–3), SQDIP boards, visual management, Gemba walks, escalation ladder, RACI, "
     "countermeasure tracking to closure, OEE, OTD, first-pass yield, deviation and rework rate, MTBF/MTTR, "
     "monthly management review"),
    ("PPI, Lean & problem solving",
     "PPI 8-step problem solving, A3, Kaizen events, Just-Do-It actions, value stream mapping, standard work, "
     "5S, SMED, TPM, Kanban and WIP control, Poka-Yoke, Jidoka, Ishikawa, 5 Why, FMEA, DMAIC/Six Sigma tools, "
     "Toyota Kata, Hansei and Yokoten"),
    ("Quality & regulatory",
     "GMP/cGMP, FDA expectations, quality management system, ISO 13485 awareness, SOP and batch record "
     "discipline, deviation, CAPA and change control, audit readiness and inspection support, FAT/SAT, "
     "IQ/OQ/PQ, validation documentation, clean room and gowning discipline, IMS"),
    ("Safety & EHS",
     "Risk assessment (APV), LOTO, safety walks, toolbox talks, near-miss reporting to closure, stop-the-line "
     "authority, warehouse and manufacturing-area discipline, authority requirements across 24/7 operations"),
    ("Projects & change",
     "Project management and stage-gate governance, critical path and milestones, schedule and cost control, "
     "stakeholder management, change management and change leadership (Kotter/ADKAR), supplier and "
     "subcontractor management, business case development"),
    ("Digital, ERP & AI",
     "SAP ERP, CMMS, Power BI, Excel/Power Query, Microsoft 365, Python, Claude API/Claude Code, prompt and "
     "agent design, automated KPI reporting, OEE and capacity models, investment models (NPV, IRR, sensitivity, "
     "scenarios), digital checklists"),
    ("Business & finance",
     "Full P&L responsibility, budget and cost control, productivity pipeline with validated savings, quotations "
     "and service agreements (SLA), procurement and supplier negotiation"),
]

ACHIEVEMENTS = [
    ("Zero critical deviations at handover",
     "across 37 concurrent CAPEX and plant projects (DKK 2–10m each) under GMP/FDA/EMA."),
    ("+40% productivity",
     "in a technical service operation, delivered through data-driven planning and standard work."),
    ("−40% energy cost",
     "in regulated production — sustained after the project organisation was dissolved."),
    ("Tiered daily management introduced",
     "in three operations — month-end reporting replaced by visual boards and same-shift escalation."),
    ("Teams built across two countries",
     "25 specialists, a 14-person production team, a 12-person workshop, 5 electricians and 3 apprentices — all "
     "with competence matrices and development plans."),
]

EXPERIENCE = [
    ("Owner / Technical Director / Authorised Electrical Installer",
     "ELOHVAC ApS · Copenhagen · May 2023 – Present",
     "5 electricians and 3 apprentices · 40+ service sites across Greater Copenhagen · full P&L, quotations "
     "and supplier agreements",
     [("Full operating responsibility",
       "daily production planning, capacity against the order book, material and spare-part flow, quality control, "
       "on-time delivery and cost — reviewed every morning against standard work, 5S, visual boards and KPIs."),
      ("People leadership",
       "daily planning, 1:1s and performance reviews, competence matrix, safety follow-up and structured training "
       "across shifting sites and priorities."),
      ("AI-supported management",
       "built the digital backbone myself — ERP-based order and spare-part control, Power BI dashboards and "
       "Python/Claude API tools for planning, quotations, checklists and reporting; productivity above +40%."),
      ("EHS and compliance",
       "risk assessment at every new site, LOTO, near-miss handling and documented service records; zero critical "
       "deviations in the service portfolio.")]),

    ("Senior Commissioning Engineer / Project Manager, Electrical Systems",
     "Novo Nordisk A/S · Kalundborg · Nov 2022 – Jul 2024",
     "37 concurrent CAPEX projects, DKK 2–10m each · 25 specialists across engineering, procurement and site "
     "operations · GMP/FDA/EMA",
     [("Portfolio delivery",
       "schedule, cost, risk, resources and monthly reporting to management and client across engineering, "
       "procurement and site operations."),
      ("Cross-functional leadership of 25 specialists",
       "commissioning and qualification (FAT/SAT, IQ/OQ/PQ, validation documentation) with deviation handling, "
       "CAPA and change control in a live audit trail — zero critical findings at handover under GMP/FDA/EMA."),
      ("Energy programme",
       "−40% energy cost through structured PDCA, A3 problem solving and standardised work; SAP ERP for cost, "
       "asset and order control."),
      ("Shop-floor reality",
       "daily work in clean room areas, warehouses and manufacturing: work permits, LOTO, gowning and clean-room "
       "discipline, interfaces to Quality, Maintenance and Production.")]),

    ("Project and Workshop Manager, Ventilation & Climate",
     "Ventek-Air · Copenhagen · Jan 2022 – Nov 2022",
     "14-person production and assembly team · 11 concurrent projects (DKK 2–10m) · specification to formal "
     "handover",
     [("Daily leadership and flow",
       "capacity planning and flow control across 11 concurrent projects, from specification to formal handover."),
      ("Daily huddles and bottleneck analysis",
       "standardised work at every station, with a marked lift in delivery performance and first-time quality."),
      ("Suppliers and subcontractors",
       "contract basis, safety documentation and handover packages.")]),

    ("Maintenance and Operations Manager / Workshop Technician",
     "Biofos (Lynetten) · Copenhagen · Aug 2017 – Jan 2022",
     "24/7 plant operations · pumps, HVAC, HV switchgear and SCADA · operations and maintenance budgets in SAP",
     [("24/7 critical operations",
       "uptime, preventive maintenance and fast fault-finding with zero tolerance for unplanned stops."),
      ("Structured maintenance",
       "standard work, 5S, PDCA preventive maintenance plan, A3 root-cause analysis, spare-part flow and "
       "critical stores."),
      ("Shift operations and safety discipline",
       "LOTO, risk assessment, near-miss reporting and toolbox talks; KPIs and operations budgets in SAP ERP.")]),

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
    ("Lean practice — 5S, PDCA, value stream mapping, A3 and Kaizen",
     "Applied in operations · 2017 – present"),
    ("Refrigeration Technology & HVAC (AMU)",
     "Mercantec · Mar 2021"),
    ("STCW maritime certificates — engine room watchkeeping (A-III/1), ship security officer (VI/5), "
     "tanker basics (V/1-1, V/1-2)",
     "Danish Maritime Authority · 2021 – 2023"),
    ("Working Environment §16 and Security Awareness (VI/6-1)",
     "Danish Maritime Authority · May 2021"),
]

LANGUAGES = ("Danish (native) · English (professional, written and spoken) · Persian/Farsi (native) · "
             "Driving licence B")

REFERENCES = ("Former managers at Novo Nordisk A/S (Kalundborg) and Biofos (Lynetten) — available on request.")

KEYWORDS = (
    "Operations Supervisor · Operations Management · Manufacturing · Production · Day Shift · Onsite · "
    "Daily Management · Tier Meetings · SQDIP · Visual Management · Gemba · KPI · OEE · OTD · Lean Manufacturing · "
    "Continuous Improvement · Operational Excellence · PPI · Practical Process Improvement · 8-Step Problem "
    "Solving · Kaizen · 5S · Value Stream Mapping · Standard Work · SMED · TPM · Root Cause Analysis · A3 · "
    "DMAIC · Six Sigma · Problem Solving · Decision Making · Time Management · GMP · cGMP · FDA · Quality "
    "Management System · ISO 13485 · CAPA · Deviation · Change Control · Batch Record · SOP · Validation · "
    "Audit Readiness · Clean Room · Warehouse · EHS · Safety · Regulatory Compliance · Pharmaceutical · Medical "
    "Device · Regulated Manufacturing · ERP · SAP · Microsoft Office · MS Office · Excel · Power BI · "
    "Cross-Functional · Team Development · Coaching · Situational Leadership · Performance Management · "
    "Competence Development · Employee Engagement · Change Management · Change Leadership · Inventory · "
    "Assembly · Supplier Management · Budget · Productivity · Schedule · Documentation · Training · Python · "
    "Claude API · AI · Investment Models · NPV · IRR · Roskilde · Thermo Fisher Scientific · Danish · English"
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
    m.resume_header(NAME, TITLE, CONTACT, "LEADERSHIP PROFILE")
    m.para(PROFILE, after=80)

    m.section("MANAGEMENT COMPETENCES — EVIDENCE, NOT CLAIMS")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("MANAGEMENT MODELS & METHODS — APPLIED IN PRACTICE",
                   ("Area", "Tools"), MODELS)

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

    m.models_table("FIRST 90 DAYS — THE SYSTEM I BRING",
                   ("When", "What is in place"), FIRST90)

    return m.save(path,
                  title="Application and CV — Operations Supervisor, Day, Thermo Fisher Scientific, Roskilde",
                  subject="Operations Supervisor · PPI · GMP manufacturing · Roskilde (R-01372520)",
                  keywords=("operations supervisor, operations management, manufacturing, GMP, FDA, lean, PPI, "
                            "continuous improvement, kaizen, 5S, standard work, ERP, SAP, Power BI, clean room, "
                            "warehouse, CAPA, deviation, ISO 13485"),
                  comments="Master design (navy banners, Calibri 9.5 pt). English, ATS-optimised. "
                           "Cover letter page 1, CV pages 2-4.")


if __name__ == "__main__":
    out = "/home/user/Claude/Shahram_Ajloo_ThermoFisher_OperationsSupervisor.docx"
    print("OK", build(out))
