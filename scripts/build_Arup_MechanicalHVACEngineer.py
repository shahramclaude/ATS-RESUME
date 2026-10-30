# -*- coding: utf-8 -*-
"""
Arup Copenhagen — Mechanical HVAC Engineer - Data Centre (COP00007D).
Bygget i designet fra master-CV'erne. Sprog: engelsk (JD-sprog).
Ansøgning + CV i ét dokument.

Vinkel: han kommer fra leverings- og driftssiden af HVAC (ventilationsprojekter,
renrums-HVAC, 24/7-anlæg) og søger over i rådgivning/design. Ærlig om
designværktøjer — styrken er systemsiden og en LV/MV/HV-autorisation, der gør
ham i stand til at læse hele anlægget, ikke kun luftsiden.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Mechanical HVAC Engineer — Data Centre | Arup, Copenhagen | COP00007D"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Søborg, Denmark")

DATE = "30 October 2026"
RECIPIENT = ("Arup Denmark · Axel Towers, Copenhagen · Att: Building Services — Mechanical · "
             "Mission Critical")
SUBJECT = "Application: Mechanical HVAC Engineer — Data Centre (COP00007D)"

# ------------------------------------------------------------------ side 1
OPENING = [
    "A data centre cooling design is not judged on the day the drawings are approved. It is judged at three in the "
    "morning, years later, when one chiller has tripped and the hall is still supposed to hold its temperature — "
    "and by the commissioning engineer who has to prove that it does. I have been that engineer. Twenty years of "
    "ventilation, cooling and critical plant on the delivery and operations side is the perspective I would bring "
    "into your design teams at Axel Towers.",
    "I am applying to move to the other side of the table. I have specified, installed, commissioned and then "
    "operated HVAC systems — ventilation packages from specification to formal handover, clean-room air in GMP "
    "production, and 24/7 cooling, pumping and control plant where downtime was not an option. What I want now is "
    "to sit where the decisions are actually made: in concept and detailed design, on systems whose failure modes "
    "I already know by heart.",
]

BULLETS = [
    ("Mission critical is my normal",
     "24/7 plant with pumps, chillers, air handling, switchgear and SCADA — uptime, preventive maintenance and "
     "fault-finding under pressure, with zero tolerance for unplanned stops. That is the discipline a data hall "
     "needs: design for the failure, not for the brochure."),

    ("Ventilation and cooling, delivered end to end",
     "11 concurrent ventilation and climate projects from specification to formal handover, leading a 14-person "
     "production and assembly team; ductwork, air distribution, hydronics and controls coordinated with "
     "suppliers, subcontractors and the client."),

    ("Clean-room and regulated environments",
     "HVAC and pressure regimes in GMP clean rooms and warehouses — filtration, air changes, differential "
     "pressure, gowning zones and validation documentation (IQ/OQ/PQ), with zero critical findings at handover "
     "under GMP/FDA/EMA. Temperature, humidity and cleanliness as measurable performance, not as intent."),

    ("Mechanical and electrical in one head",
     "Authorised electrical installer (LV/MV/HV) and B.Tech in Technology Management & Mechanical Engineering. "
     "I can follow a cooling design into its power supply, its controls and its interfaces — which is where most "
     "MEP coordination problems actually live."),

    ("Commissioning and handover, my strongest ground",
     "FAT and SAT, function testing, balancing and verification, as-built documentation and the handover meeting "
     "where the client finally believes the design. Designs I have commissioned are designs whose weak points I "
     "can name in a review."),
]

MIRROR = ("Against your requirements: degree in Mechanical Services / Electrical Engineering (B.Tech, EQF 6, plus "
          "Electrical & Mechanical Design) · 20+ years against the 3+ requested, in ventilation, cooling and "
          "critical plant · Mission Critical, Science & Industry and Healthcare-adjacent experience through GMP "
          "clean rooms and 24/7 technical plant · Danish and Scandinavian standards and authority processes · "
          "multidisciplinary coordination with architects, contractors and authorities · confident English and "
          "native Danish.")

HONEST = ("One thing stated plainly, because it matters in a design office: my career has been in delivery and "
          "operations, not in a consultancy drawing office, and my hands-on Revit and calculation-software "
          "experience is at a basic level rather than a daily one. My design foundation is an engineering degree "
          "and twenty years of building, testing and running the systems; the tools express that knowledge, and I "
          "learn tools quickly — I taught myself Python, Power BI and the Claude API to the point where the "
          "operation runs on them.")

CULTURE = ("Why Arup. Ove Arup's Key Speech is one of the few statements of purpose in this industry that has "
           "aged well — quality of work, total architecture, honourable behaviour, fairness — and a trust-owned "
           "firm is structurally able to put the work before the quarterly number. Your Mission Critical practice "
           "has designed data centres since the industry began, with Uptime Institute accredited tier designers, "
           "and Copenhagen is the Nordic hub for it. That combination — integrated design, real engineering "
           "authority, and projects that people in this city actually use, from Cityringen to BLOX — is where I "
           "want to spend the next twenty years of my working life.")

PRACTICAL = ("Practical: Danish native, professional English, Søborg to Axel Towers is a short commute, and I am "
             "available at short notice. On appointment I wind down my own company, so there are no competing "
             "commitments — and I am equally happy to work on projects outside Denmark.")

CLOSING = ("I would welcome the chance to show how I think: give me a data hall cooling scheme and thirty minutes, "
           "and I will tell you where it will hurt during commissioning — and what I would change in the concept "
           "to prevent it.")

# ------------------------------------------------------------------ CV
PROFILE = ("Mechanical and electrical engineer with 20+ years in ventilation, cooling and critical technical plant "
           "— delivery, commissioning and operations — and leadership responsibility since 2003 with full P&L "
           "accountability. Has specified and delivered ventilation and climate packages from brief to formal "
           "handover, worked with clean-room HVAC and pressure regimes in GMP production, and run 24/7 plant with "
           "chillers, pumps, air handling and SCADA where uptime was the measure. Authorised electrical installer "
           "(LV/MV/HV) with a B.Tech in Technology Management & Mechanical Engineering, which means mechanical and "
           "electrical interfaces are read as one system. Works in BIM-coordinated projects with an engineering "
           "degree as design foundation; builds his own data and calculation tooling (Python, Power BI, Claude "
           "API). Danish native, professional English.")

PRACTICE = [
    ("Mission critical and resilience",
     "24/7 technical plant with cooling, pumping, air handling, HV switchgear and SCADA: redundancy thinking, "
     "failure-mode analysis, preventive maintenance and fault-finding under pressure. Design reviews are where I "
     "ask what happens when the first duty unit falls out."),

    ("Mechanical design delivery",
     "Ventilation and climate packages from specification to formal handover across 11 concurrent projects: air "
     "distribution, ductwork, hydronics, controls and interfaces coordinated with architects, suppliers, "
     "contractors and the client."),

    ("Commissioning and verification",
     "FAT/SAT, IQ/OQ/PQ, function testing, balancing and verification, as-built documentation and handover with "
     "punch-list closure — the stage where a design is either proven or exposed."),

    ("Regulated environments and quality",
     "Clean rooms, warehouses and manufacturing under GMP/FDA/EMA: filtration, air-change rates, differential "
     "pressure, temperature and humidity control, deviation and CAPA handling, audit-ready documentation. Zero "
     "critical findings at handover across 37 CAPEX projects."),

    ("Multidisciplinary coordination",
     "Daily interfaces to architecture, structural, electrical, controls, Quality and Operations; work permits, "
     "LOTO and phased go-live in live production. My electrical authorisation lets me close MEP coordination "
     "issues instead of forwarding them."),

    ("Energy, sustainability and data",
     "−40% energy cost in regulated production through PDCA, A3 and standardised work; measurement and "
     "verification of savings; Power BI and Python tooling for energy, performance and investment cases "
     "(NPV, IRR, sensitivity)."),
]

FIRST90 = [
    ("Days 1–30",
     "Learn Arup's design process, QA and BIM standards by doing: take a defined mechanical package in an "
     "existing project and deliver a section of it end to end under review. Sit in on commissioning and client "
     "presentations from week one — that is where the design intent meets reality."),
    ("Days 31–60",
     "Own a package: calculations, system selection, coordination and documentation, reviewed by a senior "
     "engineer at each gate. Revit and the calculation suite brought to productive daily use in parallel, with "
     "the team's own templates rather than self-invented ones."),
    ("Days 61–90",
     "Deliver a complete mechanical design section through scheme or detailed design with quality sign-off. "
     "Contribute the commissioning and operations perspective into design reviews — failure modes, access, "
     "maintainability, spare capacity — early enough to change the outcome."),
    ("Year 1–2",
     "Trusted mechanical lead on mission critical packages: concept to practical completion, coordinating "
     "multi-disciplinary teams and presenting to clients. Contributing to the MEP team's skills learning in "
     "commissioning, critical plant and Danish authority practice — and taking on projects outside Denmark."),
]

MODELS = [
    ("Mechanical design & systems",
     "Heating, ventilation, air conditioning and cooling; air distribution and ductwork, hydronic systems, "
     "chillers and heat recovery, pumps and public health, fire suppression interfaces, controls and BMS"),
    ("Mission critical & resilience",
     "Redundancy concepts (N+1, 2N), failure-mode and single-point-of-failure review, concurrent "
     "maintainability, UPS and cooling topology interfaces, thermal management of data halls, integrated "
     "systems testing"),
    ("Calculation & documentation",
     "Load and airflow calculations, pressure loss and system sizing, psychrometrics and humidity control, "
     "design reports and specifications, coordination in BIM/Revit environments, as-built and O&M documentation"),
    ("Commissioning & verification",
     "FAT and SAT, IQ/OQ/PQ, function and performance testing, balancing and TAB, measurement and verification, "
     "handover with punch-list closure, operator training"),
    ("Standards, authorities & compliance",
     "Danish building regulations and standards (BR18, DS 428, DS 452), ISO 9001 and ISO 13485 quality "
     "management, Eurocodes and EN standards for "
     "ventilation and cooling, fire strategy interfaces, authority submissions and permits, ATEX and working "
     "environment requirements"),
    ("Electrical interface & controls",
     "Authorised LV/MV/HV installer: switchgear, protection and selectivity, motor and VFD application, SCADA "
     "and BMS integration, LOTO and safe isolation, contractor control on live plant"),
    ("Sustainability & energy",
     "Energy efficiency and heat recovery, measurement and verification, PDCA and A3 improvement, energy-cost "
     "programmes with documented results, lifecycle and investment cases (NPV, IRR, sensitivity)"),
    ("Project delivery & quality",
     "Project management with stage gates, critical path and milestones, budget and cost control, procurement "
     "and supplier management, risk registers, stakeholder management, quality assurance and design review"),
]

ACHIEVEMENTS = [
    ("−40% energy cost",
     "in regulated production through PDCA, A3 problem solving and standardised work — measured, documented "
     "and sustained after the project organisation was dissolved."),
    ("Zero critical findings at handover",
     "across 37 concurrent CAPEX and plant projects (DKK 2–10m each) — commissioning and qualification with "
     "deviation handling and closed punch lists."),
    ("11 ventilation and climate projects",
     "delivered from specification to formal handover with a 14-person production and assembly team, with a "
     "marked lift in delivery performance and first-time quality."),
    ("24/7 plant with zero tolerance for unplanned stops",
     "pumps, HVAC, HV switchgear and SCADA — uptime maintained through preventive maintenance and fast "
     "fault-finding."),
    ("Tiered performance management introduced",
     "in three operations: month-end reporting replaced by visual boards and same-shift escalation."),
]

EXPERIENCE = [
    ("Owner / Technical Director / Authorised Electrical Installer",
     "ELOHVAC ApS · Copenhagen · May 2023 – Present",
     "5 electricians and 3 apprentices · 40+ service sites across Greater Copenhagen · full P&L, quotations "
     "and supplier agreements",
     [("Full operating responsibility",
       "daily planning, capacity against the order book, material flow, quality control, delivery reliability "
       "and cost — reviewed every morning against standard work, 5S, visual boards and KPIs."),
      ("Technical delivery",
       "HVAC, electrical and control systems across service sites: fault diagnosis, system upgrades, "
       "documentation and handover to the customer's operations team."),
      ("Digital backbone, built myself",
       "ERP-based order and spare-part control, Power BI dashboards and Python/Claude API tools for planning, "
       "quotations, checklists and reporting; productivity above +40%."),
      ("Safety and compliance",
       "risk assessment at every new site, LOTO, near-miss handling and documented service records; zero "
       "critical deviations in the service portfolio.")]),

    ("Senior Commissioning Engineer / Project Manager, Electrical Systems",
     "Novo Nordisk A/S · Kalundborg · Nov 2022 – Jul 2024",
     "37 concurrent CAPEX projects, DKK 2–10m each · 25 specialists across engineering, procurement and site "
     "operations · GMP/FDA/EMA",
     [("Portfolio delivery",
       "schedule, cost, risk, resources and monthly reporting to management and client across engineering, "
       "procurement and site operations."),
      ("Commissioning and qualification",
       "FAT/SAT, IQ/OQ/PQ and validation documentation with deviation handling, CAPA and change control in a "
       "live audit trail — zero critical findings at handover."),
      ("Energy programme",
       "−40% energy cost through structured PDCA, A3 problem solving and standardised work; SAP ERP for cost, "
       "asset and order control."),
      ("Clean-room and plant reality",
       "daily work in clean rooms, warehouses and manufacturing: ventilation and pressure regimes, work "
       "permits, LOTO, contractor control and interfaces to Quality, Maintenance and Production.")]),

    ("Project and Workshop Manager, Ventilation & Climate",
     "Ventek-Air · Copenhagen · Jan 2022 – Nov 2022",
     "14-person production and assembly team · 11 concurrent projects (DKK 2–10m) · specification to formal "
     "handover",
     [("Ventilation and climate packages",
       "air distribution, ductwork, hydronics and controls from specification through production, assembly and "
       "formal handover."),
      ("Daily huddles and bottleneck analysis",
       "standardised work at every station, with a marked lift in delivery performance and first-time quality."),
      ("Coordination",
       "suppliers and subcontractors on contract basis, safety documentation and complete handover packages.")]),

    ("Maintenance and Operations Manager / Workshop Technician",
     "Biofos (Lynetten) · Copenhagen · Aug 2017 – Jan 2022",
     "24/7 plant operations · pumps, HVAC, HV switchgear and SCADA · operations and maintenance budgets in SAP",
     [("24/7 critical operations",
       "uptime, preventive maintenance and fast fault-finding with zero tolerance for unplanned stops."),
      ("Structured maintenance",
       "standard work, 5S, PDCA preventive maintenance plan, A3 root-cause analysis, spare-part flow and "
       "critical stores."),
      ("Systems and safety",
       "pumping, ventilation and control systems; LOTO, risk assessment, near-miss reporting and toolbox talks; "
       "KPIs and budgets in SAP ERP.")]),

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
    ("B.Sc.-level — Electrical & Mechanical Design, Electrical Engineering (EQF Level 6)",
     "Tehran Technical University · 2000 – 2003"),
    ("Upper Secondary Examination (HF, mathematics and physics)",
     "VUC · 2012 – 2017"),
]

CERTS = [
    ("Refrigeration Technology & HVAC (AMU)",
     "Mercantec · Mar 2021"),
    ("Danish Electrical Installer Authorisation (LV/MV/HV)",
     "Danish Safety Technology Authority · May 2023"),
    ("Lean practice — value stream mapping, standard work, 5S, A3 and Kaizen",
     "Applied in operations · 2017 – present"),
    ("Problem solving — 8-step, A3, DMAIC and Six Sigma tools",
     "Applied in projects · 2017 – present"),
    ("STCW maritime certificates — engine room watchkeeping (A-III/1), ship security officer (VI/5)",
     "Danish Maritime Authority · 2021 – 2023"),
    ("Working Environment §16 and Security Awareness (VI/6-1)",
     "Danish Maritime Authority · May 2021"),
]

LANGUAGES = ("Danish (native) · English (professional, written and spoken) · Persian/Farsi (native) · "
             "Driving licence B")

REFERENCES = ("Former managers at Novo Nordisk A/S (Kalundborg) and Biofos (Lynetten) — available on request.")

KEYWORDS = (
    "Mechanical Engineer · HVAC Engineer · HVAC · Heating · Ventilation · Air Conditioning · Cooling · Public "
    "Health · Fire Suppression · Building Services · Mechanical Design · Design Packages · Concept Design · "
    "Scheme Design · Detailed Design · Practical Completion · Installation · Commissioning · BIM · Revit · "
    "Calculation Software · Multidisciplinary · MEP · Mission Critical · Data Centre · Data Center · Science & "
    "Industry · Healthcare · Clean Room · Sustainability · Sustainable Building Design · Energy Efficiency · "
    "Heat Recovery · Chillers · AHU · Ductwork · Air Distribution · Hydronic · Pumps · Controls · BMS · SCADA · "
    "Redundancy · N+1 · 2N · Resilience · Thermal Management · Load Calculations · Danish Standards · "
    "Scandinavian Regulations · BR18 · DS 428 · DS 452 · Eurocodes · Authorities · Fire Strategy · Contractor "
    "Coordination · Stakeholder Management · Client Presentation · Quality Assurance · Technical Quality · "
    "Documentation · As-Built · FAT · SAT · IQ/OQ/PQ · Testing · Balancing · TAB · Validation · GMP · ISO 13485 · "
    "Project Management · Budget · Schedule · Risk · Procurement · AutoCAD · Power BI · Python · SAP · "
    "English · Danish"
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

    m.section("WHAT I BRING TO MISSION-CRITICAL MECHANICAL DESIGN")
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

    m.models_table("FIRST 90 DAYS — HOW I WOULD COME UP TO SPEED",
                   ("When", "What is in place"), FIRST90)

    return m.save(path,
                  title="Application and CV — Mechanical HVAC Engineer, Data Centre, Arup Copenhagen (COP00007D)",
                  subject="HVAC design · mission critical · data centre · commissioning · Copenhagen",
                  keywords=("mechanical engineer, hvac, cooling, ventilation, building services, mission critical, "
                            "data centre, design, commissioning, revit, bim, danish standards, energy efficiency, "
                            "danish, english"),
                  comments="Master design (navy banners, Calibri 9.5 pt). English, ATS-optimised. "
                           "Cover letter page 1, CV pages 2-4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_Arup_MechanicalHVACEngineer.docx")
    print("OK", build(out))
