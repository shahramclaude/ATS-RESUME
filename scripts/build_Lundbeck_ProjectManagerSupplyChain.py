# -*- coding: utf-8 -*-
"""
Lundbeck — Project Manager, Supply Chain Project Management, Requisition 8265 (Valby, Denmark).
One-year temporary position. English (JD language). Cover letter + CV in one document, master design.

Mission-first cover letter (page 1): the document is about the task, the role and the system I
bring from day one — not about me. CV (pages 2-4) documents evidence: profile, management
competences, models & methods, achievements, experience with scope lines, 90-day plan.

Honesty rule (from the Lundbeck revisions): I do NOT claim the two years of pharmaceutical
supply chain / CMC / contract manufacturing experience the JD prefers. My Novo Nordisk tenure
(Nov 2022–Jul 2024) was electrical CAPEX and commissioning across engineering, procurement and
site operations under GMP/FDA/EMA — regulated project delivery in pharma, adjacent to but not
the same as supply chain project management. One concise boundary statement; future-facing
governance work (intake, prioritisation, stage-gate) lives on the 90-day page, not among prior
achievements.

Professional and active Claude coder / AI user: investment models (NPV, IRR, sensitivity,
scenarios), dashboards, digital checklists, documentation flow, automated reporting.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

TEMPLATE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = ("Project Manager, Supply Chain Project Management | Lundbeck | "
         "Requisition 8265")
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv, Denmark")

DATE = "3 November 2026"
RECIPIENT = ("Lundbeck · Valby, Denmark · Att: Trine Munch Agerskov, Director of "
             "Supply Chain Project Management")
SUBJECT = "Application: Project Manager, Supply Chain Project Management — Valby (Requisition 8265)"

# ------------------------------------------------------------------ side 1: cover letter
OPENING = [
    "Lundbeck's Supply Chain Project Management team is on a journey towards a more consistent "
    "and professional approach to project management. The task in this role is to take ownership "
    "of key Supply Chain projects — from definition through execution and implementation — and to "
    "help turn that ambition into practical tools, governance and ways of working: project intake, "
    "prioritisation, portfolio review and a fit-for-purpose stage-gate model. The stakeholders sit "
    "across CMC, QA, Regulatory Affairs, Artwork & Master Data, Production Planning, Contract "
    "Manufacturers and Commercial. The goal is secure operations and resilient supply chains that "
    "keep meeting patient needs worldwide.",
]

BULLETS = [
    ("Clear project structures, plans, milestones and follow-up",
     "A project is only as good as its structure: definition, plan, milestones, named "
     "responsibilities (RACI) and a weekly follow-up rhythm. I build that structure for every "
     "project, track decisions and dependencies in a register, and escalate risks and issues with "
     "an owner and a deadline — so nothing depends on memory or on one person being in the room."),

    ("From complex analysis to a clear recommendation",
     "I structure complex information, weigh options and translate stakeholder input into "
     "concrete actions. Using A3, 5 Whys and Ishikawa, I find the root cause before the "
     "countermeasure; decisions are documented so the next project does not start from scratch."),

    ("Facilitating alignment across functions",
     "Workshops and working sessions only matter if they produce tangible outcomes. I run them "
     "with a clear question and a decision owner, and I close with actions, dates and owners — "
     "across engineering, quality, regulatory, production planning, contract manufacturers and "
     "commercial."),

    ("Driving the project management roadmap",
     "I work on project intake, prioritisation and portfolio review, and on a stage-gate model "
     "that fits the organisation: a portfolio buffer, go/kill decisions at gates, and a "
     "rank-ordered pipeline so resources go to the right projects. Governance is written down so "
     "it outlives the temporary assignment."),
]

MIRROR = ("Against your requirements: a relevant engineering degree (B.Tech, EQF 6, Technology "
          "Management & Mechanical Engineering); project leadership since 2003 for teams of 5 to "
          "25 with full P&L accountability; cross-functional projects end to end (definition, "
          "plan, execution, implementation); solid analytical and stakeholder skills; a pragmatic, "
          "process-improvement mindset; and the ability to work independently, take ownership and "
          "maintain momentum. I am digitally strong: Python, Claude API / Claude Code, Power BI, "
          "Excel/Power Query and SAP ERP, including investment models (NPV, IRR, sensitivity, "
          "scenarios) for development and new business ideas.")

HONEST = ("One thing stated plainly: the JD prefers minimum two years of project management or "
          "consultancy within pharmaceutical supply chain, CMC or contract manufacturing. My Novo "
          "Nordisk time (Nov 2022–Jul 2024) was electrical CAPEX and commissioning across "
          "engineering, procurement and site operations under GMP/FDA/EMA — regulated project "
          "delivery in pharma, adjacent to supply chain project management but not the same thing. "
          "I do not claim the two-year requirement is met. What I bring is regulated technical "
          "project delivery with zero critical findings at handover across 37 concurrent CAPEX "
          "projects, and a willingness to come up to speed on the supply-chain domain with the "
          "team's support.")

CULTURE = ("Why Lundbeck, and why now. The Focused Innovator behaviors — curiosity, adaptability "
           "and accountability — match how I work: explore before recommending, embrace change, "
           "and own the bigger picture beyond my own task. I recognise the Enterprise Leadership "
           "mindset: take the broadest perspective before a decision, merge insights across "
           "functions, and keep patients and colleagues at the heart of it. Lundbeck's patient "
           "purpose — easing the burden of brain disorders — is work I want to contribute to.")

PRACTICAL = ("Practical: based in Måløv, a short commute to Valby, driving licence B, ready to "
             "start on appointment. I am winding down my own company (ELOHVAC ApS), so there are "
             "no competing commitments. Limited travel and the occasional virtual meeting outside "
             "office hours across Lundbeck's sites, partners and service providers work for me.")

CLOSING = ("I would welcome a conversation on site. Thirty minutes with the project management "
           "team is worth more than another page — and I will bring the one-page portfolio baseline "
           "and a draft stage-gate outline I would start with in week one.")

# ------------------------------------------------------------------ CV
PROFILE = ("Project and technical operations leader with 20+ years in regulated manufacturing, "
           "technical operations and maintenance, and leadership responsibility since 2003 for "
           "teams of 5 to 25 with full P&L accountability. I lead cross-functional projects end "
           "to end — definition, plan, execution, implementation — with clear structures, "
           "milestones, RACI and follow-up. Documented results: +40% productivity, −40% energy "
           "cost, zero critical findings at handover across 37 concurrent CAPEX projects (DKK "
           "2–10m each) under GMP/FDA/EMA at Novo Nordisk. Professional and active Claude coder: "
           "I build investment models (NPV, IRR, sensitivity, scenarios), dashboards and digital "
           "checklists that operations run on. B.Tech (EQF 6) Technology Management & Mechanical "
           "Engineering; authorised electrical engineer LV/MV/HV; Danish native, English "
           "professional.")

PRACTICE = [
    ("Cross-functional project leadership",
     "Led 37 concurrent CAPEX projects and 25 specialists across engineering, procurement and site "
     "operations at Novo Nordisk: schedule, cost, risk, resources and monthly reporting to "
     "management and client. FAT/SAT, IQ/OQ/PQ, deviation handling, CAPA and change control in a "
     "live audit trail — zero critical findings at handover under GMP/FDA/EMA."),

    ("Clear structures, plans and follow-up",
     "Project plans with milestones, named responsibilities (RACI), escalation ladder and weekly "
     "follow-up. Introduced tiered daily management in three operations; the visual boards and "
     "same-shift escalation kept running after I left."),

    ("Analysis to decision",
     "A3, 8-step problem solving, PDCA, 5 Whys and Ishikawa: root cause before countermeasure, "
     "decisions documented, options and recommendations turned into actions with owners and dates."),

    ("Stakeholder alignment and facilitation",
     "Workshops and working sessions across engineering, procurement, production, quality, "
     "maintenance and supply chain, closed with tangible outcomes. Alignment and decision-making "
     "across functions, not just information sharing."),

    ("Risk, dependencies, issues and escalation",
     "Risk/dependency/issue register with owner and deadline, escalation to management and client, "
     "follow-up to closure. Unclear assumptions surfaced early, not at handover."),

    ("People leadership without direct authority",
     "SLII (situational leadership), GROW coaching, SBI feedback, 1:1s, competence matrices, "
     "individual development plans and 30-60-90 onboarding. Teams of 5 to 25 across two countries; "
     "psychological safety so near-misses get reported."),

    ("Digital and AI-supported delivery",
     "SAP ERP, CMMS, Power BI, Excel/Power Query, Microsoft 365, Python, Claude API / Claude Code, "
     "prompt and agent design. Automated KPI reporting, digital checklists and documentation flow, "
     "investment models with NPV, IRR and sensitivity — measured productivity above +40%."),

    ("Investment models for development and new business ideas",
     "NPV, IRR, sensitivity and scenario models to compare options, test assumptions and support "
     "go/no-go and prioritisation decisions — built so stakeholders can challenge the inputs, not "
     "just accept the output."),
]

MODELS = [
    ("Project & portfolio leadership",
     "Project intake, prioritisation, portfolio review, stage-gate model, go/kill decisions, "
     "rank-ordered pipeline, portfolio buffer, RACI, milestone plans, critical path, decision logs"),

    ("Problem solving & improvement",
     "A3, 8-step problem solving, PDCA, 5 Whys, Ishikawa/fishbone, FMEA, Standard Work, 5S, "
     "Kaizen, TPM, Kanban/WIP control, Poka-Yoke, Jidoka, Toyota Kata, Hansei, Yokoten, bottleneck "
     "analysis, spaghetti diagram"),

    ("People & team leadership",
     "SLII (situational leadership: directing, coaching, supporting, delegating), GROW coaching, "
     "SBI feedback, 1:1s and performance reviews, competence matrices, individual development "
     "plans, 30-60-90 onboarding, delegation ladder, psychological safety, 360-degree feedback, "
     "absence and recognition conversations"),

    ("Quality & regulatory",
     "GMP/cGMP, FDA expectations, quality management system, SOP and batch record discipline, "
     "deviation, CAPA and change control, audit readiness and inspection support, FAT/SAT, "
     "IQ/OQ/PQ, validation documentation, clean room and gowning discipline, IMS"),

    ("Safety & EHS",
     "Risk assessment (APV), LOTO, safety walks, toolbox talks, near-miss reporting to closure, "
     "stop-the-line authority, warehouse and manufacturing-area discipline, 24/7 operations"),

    ("Digital, ERP & AI",
     "SAP ERP, CMMS, Power BI, Excel/Power Query, Microsoft 365, Python, Claude API / Claude Code, "
     "prompt and agent design, automated KPI reporting, OEE and capacity models, investment models "
     "(NPV, IRR, sensitivity, scenarios), digital checklists, documentation flow"),

    ("Business & finance",
     "Full P&L responsibility, budget and cost control, productivity pipeline with validated "
     "savings, quotations and service agreements (SLA), procurement and supplier negotiation"),
]

ACHIEVEMENTS = [
    ("Zero critical findings at handover",
     "across 37 concurrent CAPEX and plant projects (DKK 2–10m each) under GMP/FDA/EMA."),
    ("+40% productivity",
     "in a technical service operation, delivered through data-driven planning and standard work."),
    ("−40% energy cost",
     "in regulated production — sustained after the project organisation was dissolved."),
    ("Tiered daily management introduced",
     "in three operations — month-end reporting replaced by visual boards and same-shift escalation."),
    ("Teams built across two countries",
     "25 specialists, a 14-person production team, a 12-person workshop, 5 electricians and 3 "
     "apprentices — all with competence matrices and development plans."),
]

EXPERIENCE = [
    ("Owner / Technical Director / Authorised Electrical Installer",
     "ELOHVAC ApS · Copenhagen · May 2023 – Present",
     "5 electricians and 3 apprentices · 40+ service sites across Greater Copenhagen · full P&L, "
     "quotations and supplier agreements",
     [("Full operating responsibility",
       "daily production planning, capacity against the order book, material and spare-part flow, "
       "quality control, on-time delivery and cost — reviewed every morning against standard work, "
       "5S, visual boards and KPIs."),
      ("People leadership",
       "daily planning, 1:1s and performance reviews, competence matrix, safety follow-up and "
       "structured training across shifting sites and priorities."),
      ("AI-supported management",
       "built the digital backbone myself — ERP-based order and spare-part control, Power BI "
       "dashboards and Python/Claude API tools for planning, quotations, checklists and reporting; "
       "productivity above +40%."),
      ("EHS and compliance",
       "risk assessment at every new site, LOTO, near-miss handling and documented service records; "
       "zero critical deviations in the service portfolio.")]),

    ("Senior Commissioning Engineer / Project Manager, Electrical Systems",
     "Novo Nordisk A/S · Kalundborg · Nov 2022 – Jul 2024",
     "37 concurrent CAPEX projects, DKK 2–10m each · 25 specialists across engineering, "
     "procurement and site operations · GMP/FDA/EMA",
     [("Portfolio delivery",
       "schedule, cost, risk, resources and monthly reporting to management and client across "
       "engineering, procurement and site operations."),
      ("Cross-functional leadership of 25 specialists",
       "commissioning and qualification (FAT/SAT, IQ/OQ/PQ, validation documentation) with "
       "deviation handling, CAPA and change control in a live audit trail — zero critical findings "
       "at handover under GMP/FDA/EMA."),
      ("Energy programme",
       "−40% energy cost through structured PDCA, A3 problem solving and standardised work; SAP ERP "
       "for cost, asset and order control."),
      ("Shop-floor reality",
       "daily work in clean room areas, warehouses and manufacturing: work permits, LOTO, gowning "
       "and clean-room discipline, interfaces to Quality, Maintenance and Production.")]),

    ("Project and Workshop Manager, Ventilation & Climate",
     "Ventek-Air · Copenhagen · Jan 2022 – Nov 2022",
     "14-person production and assembly team · 11 concurrent projects (DKK 2–10m) · specification "
     "to formal handover",
     [("Daily leadership and flow",
       "capacity planning and flow control across 11 concurrent projects, from specification to "
       "formal handover."),
      ("Daily huddles and bottleneck analysis",
       "standardised work at every station, with a marked lift in delivery performance and "
       "first-time quality."),
      ("Suppliers and subcontractors",
       "contract basis, safety documentation and handover packages.")]),

    ("Maintenance and Operations Manager / Workshop Technician",
     "Biofos (Lynetten) · Copenhagen · Aug 2017 – Jan 2022",
     "24/7 plant operations · pumps, HVAC, HV switchgear and SCADA · operations and maintenance "
     "budgets in SAP",
     [("24/7 critical operations",
       "uptime, preventive maintenance and fast fault-finding with zero tolerance for unplanned "
       "stops."),
      ("Structured maintenance",
       "standard work, 5S, PDCA preventive maintenance plan, A3 root-cause analysis, spare-part "
       "flow and critical stores."),
      ("Shift operations and safety discipline",
       "LOTO, risk assessment, near-miss reporting and toolbox talks; KPIs and operations budgets "
       "in SAP ERP.")]),

    ("Electromechanical Technician / Production Team Leader",
     "ARJ Engineering · Tehran · Dec 2003 – Mar 2010",
     "12-person production team · shift planning, material control and inventory",
     [("Production team leadership",
       "shift planning, material control, inventory and line-side supply, target management and "
       "situational coaching."),
      ("Technical problem solving",
       "repair and diagnosis of electrical and mechanical systems through structured root cause "
       "analysis.")]),
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
    ("Authorised electrical engineer (LV/MV/HV)",
     "Danish Safety Technology Authority · May 2023"),
    ("Lean practice — 5S, PDCA, value stream mapping, A3 and Kaizen",
     "Applied in operations · 2017 – present"),
    ("Refrigeration Technology & HVAC (AMU)",
     "Mercantec · Mar 2021"),
    ("STCW maritime certificates — engine room watchkeeping (A-III/1), ship security officer "
     "(VI/5), tanker basics (V/1-1, V/1-2)",
     "Danish Maritime Authority · 2021 – 2023"),
    ("Working Environment §16 and Security Awareness (VI/6-1)",
     "Danish Maritime Authority · May 2021"),
]

LANGUAGES = ("Danish (native) · English (professional, written and spoken) · Persian/Farsi (native) · "
             "Driving licence B")

REFERENCES = ("Former managers at Novo Nordisk A/S (Kalundborg) and Biofos (Lynetten) — available on "
              "request.")

KEYWORDS = (
    "Project Manager · Supply Chain Project Management · Project Management · Cross-Functional · "
    "Project Portfolio · Stage-Gate · Project Intake · Prioritisation · Portfolio Review · "
    "Governance · Ways of Working · Milestones · RACI · Risk Management · Dependencies · Escalation · "
    "Facilitation · Workshops · Alignment · Decision-Making · CMC · QA · Regulatory Affairs · Artwork "
    "& Master Data · Production Planning · Contract Manufacturers · Commercial · Supply Chain · "
    "Pharmaceutical · GMP · FDA · EMA · FAT/SAT · IQ/OQ/PQ · Deviation · CAPA · Change Control · "
    "Audit Readiness · Validation · Structured · Systematic · Analytical · Stakeholder Management · "
    "Communication · Ownership · Momentum · Pragmatic · Process Improvement · PDCA · A3 · 5 Whys · "
    "Ishikawa · SLII · GROW · SBI · Competence Matrices · 1:1 · 30-60-90 · Digital tools · Digital · AI · Python · "
    "Claude API · Power BI · Excel/Power Query · SAP ERP · Investment Models · NPV · IRR · Sensitivity "
    "· Scenarios · Valby · Lundbeck · Danish · English · Authorised electrical engineer LV/MV/HV · "
    "B.Tech · Technology Management & Mechanical Engineering"
)

FIRST90 = [
    ("Days 1–7",
     "With the project management team, not in an office: review the current project portfolio, the "
     "intake list, open risks, dependencies and escalations; attend the portfolio review; meet the "
     "Director and key stakeholders across CMC, QA, Regulatory Affairs, Artwork & Master Data, "
     "Production Planning, Contract Manufacturers and Commercial."),

    ("Days 8–30",
     "Baseline on one page: active projects, milestones, status, risks, owners and next decisions "
     "pulled from existing tools rather than memory. Confirm project structures, plans, milestones, "
     "responsibilities and follow-up rhythm with each project owner. Propose a fit-for-purpose "
     "stage-gate outline and intake/prioritisation criteria for discussion with the Director."),

    ("Days 31–60",
     "Run one project through the proposed intake → prioritisation → stage-gate flow with a named "
     "owner, deadline and go/kill decision. Facilitate one alignment workshop with tangible "
     "outcomes. Stand up a risk/dependency/issue register with an escalation path. Begin an "
     "investment-model template (NPV/IRR, sensitivity, scenarios) for business cases."),

    ("Days 61–90",
     "Deliver one project milestone on time with a documented decision and handover. Embed the "
     "portfolio review cadence (weekly/monthly) with the Director. Hand over working tools — intake "
     "template, stage-gate checklist, risk register, investment model — so the system keeps running "
     "after the temporary assignment."),
]


def build(path):
    m = MasterDoc(TEMPLATE, lang="en-GB")

    # ---------------------------------------------------------------- side 1: cover letter
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

    # ---------------------------------------------------------------- side 2+: CV
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
                  title="Application and CV — Project Manager, Supply Chain Project Management, Lundbeck, Valby (Req. 8265)",
                  subject="Project Manager · Supply Chain Project Management · stage-gate · portfolio governance · Valby (Req. 8265)",
                  keywords=("project manager, supply chain project management, stage-gate, portfolio "
                            "governance, project intake, prioritisation, GMP, FDA, EMA, FAT/SAT, "
                            "IQ/OQ/PQ, CAPA, change control, SLII, GROW, SBI, RACI, PDCA, A3, Python, "
                            "Claude API, Power BI, SAP ERP, NPV, IRR"),
                  comments="Master design (navy banners, Calibri 9.5 pt). English, ATS-optimised. "
                           "Cover letter page 1, CV pages 2-4.")


if __name__ == "__main__":
    out = "/home/user/ATS-RESUME/Shahram_Ajloo_Lundbeck_ProjectManagerSupplyChain.docx"
    print("OK", build(out))
