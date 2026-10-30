# -*- coding: utf-8 -*-
"""
Everllence (formerly MAN Energy Solutions) — Head of Manufacturing, Copenhagen.
Job ID 14172 · Teglholmsgade 41, 2450 København SV · deadline 1 November 2026.
Bygget i designet fra master-CV'erne. Sprog: engelsk (JD-sprog).
Ansøgning + CV i ét dokument. Ansøgningen er adresseret til Andreas Windel,
Head of Production & Logistics, som er navngivet i opslaget.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = ("Head of Manufacturing | Everllence, Copenhagen | Job ID 14172")
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Søborg, Denmark")

DATE = "30 October 2026"
RECIPIENT = ("Andreas Windel · Head of Production & Logistics, Copenhagen · Everllence SE · "
             "Teglholmsgade 41, 2450 København SV")
SUBJECT = "Application: Head of Manufacturing, Copenhagen (Job ID 14172)"

# ------------------------------------------------------------------ side 1
OPENING = [
    "Your posting describes two jobs in one: running the Copenhagen factory to standard on Safety, Quality, "
    "Delivery and Cost this quarter, and rebuilding the organisation so that it arrives at The Valley in 2027 "
    "stronger than it left. The second is the harder one, and it is decided long before the move: in which "
    "leaders own which numbers, how fast a deviation reaches the tier board, and whether the improvement habit "
    "survives a relocation. I have run that combination for twenty years in regulated manufacturing, heavy "
    "technical operations and CAPEX — and I build the system that carries it, in writing, before I need it.",

    "Everllence is a specific factory, not a generic one. Semi-serial production of key components and spare "
    "parts for two-stroke engines designed in Copenhagen since B&W signed with Rudolf Diesel in 1898 — where a "
    "tolerance is measured in hundredths of a millimetre, the test engine at the research centre weighs 272 "
    "tonnes, and the engines designed here power roughly three-quarters of the world's seaborne trade. Moving "
    "that to Trekroner without losing a delivery week is a programme, not a removal.",
]

BULLETS = [
    ("Daily performance, run as a system",
     "Tier-1 to tier-3 boards on Safety, Quality, Delivery and Cost with named owners, escalation inside the "
     "shift and countermeasures tracked to closure — introduced in three operations. OEE, on-time delivery, "
     "first-pass yield and rework reviewed daily instead of at month-end."),

    ("Operational excellence with measured effect",
     "Value stream mapping, standard work, 5S, SMED, TPM, Kanban and Poka-Yoke, with A3, 8-step and "
     "DMAIC/Six Sigma problem solving underneath. Documented: +40% productivity and −40% energy cost in "
     "regulated production, both measured before and after, both sustained after the project team disbanded."),

    ("Transformation and CAPEX, delivered",
     "37 concurrent CAPEX and plant projects (DKK 2–10m each) with schedule, cost, risk and resources; "
     "commissioning and qualification (FAT/SAT, IQ/OQ/PQ) with zero critical findings at handover under "
     "GMP/FDA/EMA. Relocations and site changes are programmes with a critical path, not surprises."),

    ("Leaders and specialists developed on purpose",
     "Coaching, 1:1s, competence matrices and 30-60-90 onboarding for production teams, a 25-specialist "
     "engineering organisation and skilled trades — plus the working relationship with safety organisations, "
     "unionised trades and contractors that Danish industry runs on."),

    ("Digital manufacturing, done not talked",
     "SAP ERP and CMMS as the source of truth, Power BI for the boards, and self-built Python/Claude tooling "
     "for automated KPI reporting, OEE and capacity models and investment cases (NPV, IRR, sensitivity). "
     "Industry 4.0 only pays when the data arrives without anybody retyping it."),
]

MIRROR = ("Against your listed requirements: 20+ years in manufacturing, industrial operations and technical "
          "management, leadership responsibility since 2003 with full P&L · operational performance, productivity "
          "and delivery reliability improved and documented · organisational change and continuous improvement led "
          "in three operations · Lean Manufacturing and Six Sigma problem-solving tools · SAP ERP, digitalisation "
          "and automation · engineering education (B.Tech, EQF 6) plus authorised installer LV/MV/HV · Danish "
          "native, professional English.")

HONEST = ("One thing stated plainly: the largest organisation I have led directly is 25 specialists plus "
          "production teams of 5 to 25, with full P&L responsibility in my own company — I have not yet carried a "
          "site of twelve hundred. What I bring is the operating system, the CAPEX discipline and the habit of "
          "building the leadership team that carries it, and I would rather say that here than have you discover "
          "it in an interview.")

CULTURE = ("Why Everllence, and why this factory. \"Moving big things to zero\" is one of the few decarbonisation "
           "promises in this industry that is measured in delivered engines rather than in slides — two-stroke "
           "engines on ammonia and methanol, heat pumps, carbon capture, electrolysers through Quest One — and "
           "Copenhagen is where that design authority actually sits. The culture described in your posting is the "
           "one I build: a culture of ownership and accountability, open dialogue and constructive challenge, and "
           "decisions that are written down. Add the Danish model — employee representatives and unions as partners, work-life "
           "balance, fifty-five nationalities — and this is a factory I would want my name on.")

PRACTICAL = ("Practical: available for interview during the application period and to start at short notice. "
             "Søborg to Teglholmsgade is a fifteen-kilometre commute, and I am equally ready to be at Trekroner "
             "when the programme needs me there. On appointment I wind down my own company, so there are no "
             "competing commitments.")

CLOSING = ("I would welcome a conversation — and I would rather have it on the floor than in a meeting room. "
           "Give me forty minutes at Teglholmsgade and I will bring the one-page performance baseline and the "
           "relocation-critical-path view I would put in front of the factory leadership team in week one.")

# ------------------------------------------------------------------ CV
PROFILE = ("Manufacturing and operations leader with 20+ years in regulated manufacturing, heavy technical "
           "operations and maintenance, and leadership responsibility since 2003 with full P&L accountability. "
           "Has led production teams, workshops, a 25-specialist engineering organisation and 37 concurrent CAPEX "
           "projects, and runs performance the way a factory needs it — tiered boards on Safety, Quality, "
           "Delivery and Cost, named owners, escalation inside the shift, standard work and A3/8-step problem "
           "solving. Documented results: +40% productivity, −40% energy cost, zero critical deviations at handover "
           "under GMP/FDA/EMA. Professional and active Claude coder: builds the KPI, OEE, capacity and investment "
           "models the operation runs on — digital manufacturing from the data side up. B.Tech in Technology "
           "Management & Mechanical Engineering (EQF 6); authorised electrical installer LV/MV/HV; Danish native, "
           "professional English.")

PRACTICE = [
    ("Performance management that is actually used",
     "Tier-1 to tier-3 huddles against a fixed board — Safety, Quality, Delivery, Cost — with named "
     "countermeasure owners, escalation inside the shift and a monthly management review. OEE, on-time "
     "delivery, first-pass yield and rework rate visible daily. Introduced in three operations and still "
     "running after I left."),

    ("Operational excellence with a verified effect",
     "+40% productivity in a technical service operation and −40% energy cost in regulated production — both "
     "through value stream mapping, standard work, PDCA and A3, both measured before and after, and both "
     "sustained after the project team disbanded."),

    ("CAPEX, commissioning and site change",
     "37 concurrent CAPEX and plant projects (DKK 2–10m each) across engineering, procurement and site "
     "operations; qualification and handover with zero critical findings under GMP/FDA/EMA; work permits, "
     "LOTO, contractor safety and phased go-live in live production."),

    ("Leaders and specialists built, not bought",
     "Competence matrices and individual development plans for a 25-specialist organisation, a 14-person "
     "production team, a 12-person workshop and 5 electricians with 3 apprentices; 30-60-90 onboarding and "
     "apprentice training; absence and retention handled early, not at the exit interview."),

    ("Digital manufacturing and Industry 4.0",
     "SAP ERP and CMMS as source of truth, Power BI for performance transparency, Python and the Claude API for "
     "automated KPI reporting, OEE and capacity models, digital checklists and documentation flow — plus "
     "investment and scenario models (NPV, IRR, sensitivity) for development and new business cases."),
]

FIRST90 = [
    ("Days 1–30",
     "On the floor on every shift: line walks, tier-1 boards, safety observations, open deviations and the "
     "customer-critical backlog. One-page baseline for the factory — Safety, Quality, Delivery, Cost, "
     "productivity per hour, OEE and delivery reliability — taken from SAP and the QMS, not from memory. "
     "Every leader confirmed against the number they own."),
    ("Days 31–60",
     "Tier structure, escalation ladder and countermeasure routine (RACI) agreed with the factory leadership "
     "team and the middle managers who will run it. Two or three Just-Do-It and Kaizen actions closed with "
     "measured effect; standard work and 5S restored at the constraint. Union and employee-representative "
     "dialogue established before anything is announced twice."),
    ("Days 61–90",
     "One A3 on the largest loss with an owner, a deadline and a verified result; the relocation programme to "
     "Trekroner mapped as a critical path — what moves when, what must be qualified, what cannot stop — with "
     "the factory's own leaders named on each workstream. Reporting automated end-to-end so the numbers arrive "
     "daily and the leaders stay on the floor."),
    ("Year 1",
     "Performance held through the transition rather than after it: productivity and delivery reliability "
     "improved against the baseline, a leadership pipeline in place for The Valley, and the digital backbone "
     "(SAP, Power BI, MES-level data) ready to be lifted into the new factory instead of rebuilt there."),
]

MODELS = [
    ("Strategy deployment & performance",
     "Hoshin-style annual targets broken into tier-1 to tier-3 boards, SQDCP boards, visual management, Gemba "
     "walks, escalation ladder, RACI, countermeasure tracking to closure, monthly management review"),
    ("Lean & operational excellence",
     "Value stream mapping, standard work, 5S, SMED, TPM, Kanban and WIP control, Poka-Yoke, Jidoka, Ishikawa, "
     "5 Why, FMEA, A3, 8-step problem solving, Kaizen, DMAIC/Six Sigma tools, Toyota Kata, Hansei and Yokoten"),
    ("Manufacturing engineering & CAPEX",
     "Stage-gate governance, critical path and milestones, schedule and cost control, FAT/SAT, IQ/OQ/PQ, "
     "validation documentation, contractor control, work permits and LOTO, phased go-live in live production"),
    ("Performance economics",
     "OEE, productivity per hour, OTD and delivery reliability, first-pass yield, rework and scrap, cost per "
     "unit, absorption, capacity and bottleneck planning, make-or-buy and business case development "
     "(NPV, IRR, sensitivity)"),
    ("Quality & compliance",
     "Quality management system, ISO 9001 and ISO 13485 awareness, GMP/FDA expectations, SOP and batch record "
     "discipline, deviation, CAPA and change control, audit readiness and inspection support, IMS"),
    ("Safety & EHS",
     "Risk assessment (APV), LOTO, safety walks, toolbox talks, near-miss reporting to closure, stop-the-line "
     "authority, contractor and warehouse discipline, authority requirements across 24/7 operations"),
    ("Digital manufacturing & Industry 4.0",
     "SAP ERP and S/4HANA readiness, CMMS, Power BI, Excel/Power Query, Python, Claude API/Claude Code, "
     "automated KPI reporting, OEE and capacity models, digital checklists and documentation flow, sensor and "
     "machine-data use cases"),
    ("People, leadership & labour relations",
     "Situational leadership (SLII), GROW coaching, SBI feedback, 1:1s and performance reviews, competence "
     "matrices, individual development plans, 30-60-90 onboarding, delegation ladder, psychological safety, "
     "cooperation with employee representatives, safety organisations and unionised trades"),
]

ACHIEVEMENTS = [
    ("Zero critical deviations at handover",
     "across 37 concurrent CAPEX and plant projects (DKK 2–10m each) in regulated production."),
    ("+40% productivity",
     "in a technical service operation, delivered through data-driven planning and standard work."),
    ("−40% energy cost",
     "in regulated production — sustained after the project organisation was dissolved."),
    ("Tiered performance management introduced",
     "in three operations — month-end reporting replaced by visual boards and same-shift escalation."),
    ("Teams built across two countries",
     "25 specialists, a 14-person production team, a 12-person workshop, 5 electricians and 3 apprentices — "
     "all with competence matrices and development plans."),
]

EXPERIENCE = [
    ("Owner / Technical Director / Authorised Electrical Installer",
     "ELOHVAC ApS · Copenhagen · May 2023 – Present",
     "5 electricians and 3 apprentices · 40+ service sites across Greater Copenhagen · full P&L, quotations "
     "and supplier agreements",
     [("Full operating responsibility",
       "daily production planning, capacity against the order book, material and spare-part flow, quality "
       "control, on-time delivery and cost — reviewed every morning against standard work, 5S, visual boards "
       "and KPIs."),
      ("People leadership",
       "daily planning, 1:1s and performance reviews, competence matrix, safety follow-up and structured "
       "training across shifting sites and priorities."),
      ("Digital backbone, built myself",
       "ERP-based order and spare-part control, Power BI dashboards and Python/Claude API tools for planning, "
       "quotations, checklists and reporting; productivity above +40%."),
      ("EHS and compliance",
       "risk assessment at every new site, LOTO, near-miss handling and documented service records; zero "
       "critical deviations in the service portfolio.")]),

    ("Senior Commissioning Engineer / Project Manager, Electrical Systems",
     "Novo Nordisk A/S · Kalundborg · Nov 2022 – Jul 2024",
     "37 concurrent CAPEX projects, DKK 2–10m each · 25 specialists across engineering, procurement and site "
     "operations · GMP/FDA/EMA",
     [("Portfolio delivery",
       "schedule, cost, risk, resources and monthly reporting to management and client across engineering, "
       "procurement and site operations."),
      ("Cross-functional leadership of 25 specialists",
       "commissioning and qualification (FAT/SAT, IQ/OQ/PQ, validation documentation) with deviation handling, "
       "CAPA and change control in a live audit trail — zero critical findings at handover."),
      ("Energy programme",
       "−40% energy cost through structured PDCA, A3 problem solving and standardised work; SAP ERP for cost, "
       "asset and order control."),
      ("Shop-floor reality",
       "daily work in clean room areas, warehouses and manufacturing: work permits, LOTO, contractor control, "
       "gowning discipline, interfaces to Quality, Maintenance and Production.")]),

    ("Project and Workshop Manager, Ventilation & Climate",
     "Ventek-Air · Copenhagen · Jan 2022 – Nov 2022",
     "14-person production and assembly team · 11 concurrent projects (DKK 2–10m) · specification to formal "
     "handover",
     [("Daily leadership and flow",
       "capacity planning and flow control across 11 concurrent projects, from specification to formal "
       "handover."),
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
    ("Lean practice — value stream mapping, standard work, 5S, A3 and Kaizen",
     "Applied in operations · 2017 – present"),
    ("Problem solving — 8-step, A3, DMAIC and Six Sigma tools",
     "Applied in operations and CAPEX projects · 2017 – present"),
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
    "Head of Manufacturing · Manufacturing Leadership · Factory Management · Factory Leadership Team · Middle "
    "Management · Production · Industrial Operations · Operations Management · Operational Excellence · Lean "
    "Manufacturing · Continuous Improvement · Kaizen · 5S · Standard Work · Value Stream Mapping · A3 · Six "
    "Sigma · DMAIC · Problem Solving · Performance Management · KPI · Data-Informed Decision-Making · "
    "Performance Transparency · OEE · OTD · Productivity · Delivery Reliability · Production Economics · Cost · "
    "Safety · Quality · Delivery · SQDCP · Semi-Serial Manufacturing · Organizational Change · Transformation · "
    "Change Management · Stakeholder Management · Cross-Functional · Supply Chain · Engineering · HR · Finance · "
    "Employee Representatives · Unions · Ownership · Accountability · Collaboration · Coaching · People "
    "Development · Competence Development · Digitalization · Digital Manufacturing · Automation · Industry 4.0 · "
    "SAP · S/4HANA · ERP · CMMS · Power BI · CAPEX · Project Management · Commissioning · Validation · Risk "
    "Management · Strategy Deployment · Hoshin · Shopfloor Management · Gemba · Tier Meetings · Visual "
    "Management · TPM · SMED · Kanban · Root Cause Analysis · Quality Management System · ISO 9001 · Strategic · "
    "Copenhagen · Roskilde · The Valley · Everllence · Decarbonization · Marine · Energy · Danish · English"
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
                  title="Application and CV — Head of Manufacturing, Copenhagen, Everllence (Job ID 14172)",
                  subject="Head of Manufacturing · Lean · performance management · The Valley · Copenhagen",
                  keywords=("head of manufacturing, manufacturing leadership, lean manufacturing, operational "
                            "excellence, performance management, continuous improvement, six sigma, industry 4.0, "
                            "digitalization, SAP, CAPEX, change management, employee representatives, Danish, "
                            "English"),
                  comments="Master design (navy banners, Calibri 9.5 pt). English, ATS-optimised. "
                           "Cover letter page 1, CV pages 2-4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_Everllence_HeadOfManufacturing.docx")
    print("OK", build(out))
