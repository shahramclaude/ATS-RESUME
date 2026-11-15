# -*- coding: utf-8 -*-
"""Hempel A/S — Solutions Project Manager, Marine Solution Management (Kongens Lyngby).

English posting → English document (en-GB): application page 1, CV page 2,
education + 90-day plan + four sections page 3, requirement matrix page 4.

STILVALG (master/STILREGISTER.md, policy 04.11.2026; godkendt af scripts/style_guard.py,
3/3 skift mod #189):
  register      = KOMMERCIEL-FORRETNINGSMÆSSIG — tal, kunde, beslutning, margin. Passer til en
                  rolle, der sælger løsninger på effekt (fuel, CO2, dokinterval) og til et
                  opslag, hvor KPI'er, business objectives og solution effectiveness er kernesprog.
                  Sidst brugt #179/#181.
  åbningsgreb   = C (STEDET) — Kongens Lyngby som præmis: her køber kunden ikke maling, men et
                  tal, der skal holde efter dokningen. Sidst brugt #176.
  struktur      = MÅLESTOKKEN — hvert afsnit åbner med et tal og hvad det betyder for leverancen
                  (37 · 0 · 11 · 40 % · 5/12/14/25 · 20+). Sidst brugt #181, i en anden variant.
  kadence       = tal først, forklaring bagefter — kort, konkret, kommercielt.

Ingen opdigtede fakta: ingen erfaring fra coatings, skibsfart, hull performance eller
marine service påstås. Overførslen er dokumenteret leverance af tekniske løsninger i drift
(GMP/FDA/EMA), KPI- og BI-opbygning, udrulning/integration og kommercielt ansvar.

Policy: master/README.md — jobbet først, kandidaten kun som bevis, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Solutions Project Manager · Marine solutions, delivery and measurable effect'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("9 November 2026")
    m.meta("Hempel A/S · Solutions Project Manager, Marine Solution Management · Kongens Lyngby")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Application: Solutions Project Manager — Hempel", bold=True, color='1A1A1A')
    m.para("To the Director for Marine Solution Management", after=70)

    # ---------------------------------------------------------------- page 1
    m.para("**In Kongens Lyngby, nobody buys a coating. They buy a number that has to survive a "
           "charter party.** A hull that stays clean across a docking interval, a fuel bill that falls, "
           "a CO₂ line in the annual report that moves in the right direction — and a ship manager who "
           "can defend all three to his own board. A solution is only a solution when that number still "
           "holds a year after we have left the vessel. That is the part of this role I know how to run.",
           after=80)

    m.para("**37 — the number of projects I have carried at once.** At Novo Nordisk I planned and "
           "delivered 37 concurrent CAPEX projects of DKK 2–10 million against one shared pool of 25 "
           "specialists and a fixed window calendar: detailed plans, timelines and budgets, re-forecast "
           "every month, with the date we promised the customer being the date the resources could "
           "actually carry. A solution portfolio is the same discipline with a different vocabulary — "
           "and the failure mode is identical: too many launches, one team, no decision about what "
           "waits.", after=80)

    m.para("**0 — critical findings at customer acceptance.** I have taken technical solutions into "
           "live environments through FAT/SAT, IQ/OQ/PQ and acceptance with the customer's own "
           "inspectors in the room, and I do not treat **testing, deployment and integration** as the "
           "last two weeks of a plan. A solution that has to work inside systems people already use is "
           "designed for the deployment from the beginning: what data it needs, who owns the interface, "
           "what happens on the day it does not start, and how it is rolled back.", after=80)

    m.para("**11 — concurrent contracts under my own P&L.** Since 2023 I have run my own company with "
           "full financial responsibility: quotes, terms, margins, supplier agreements and 11 "
           "subcontracts in parallel. That is where I learned to be the **primary point of contact** for "
           "an **external customer** who has paid for something and expects it on a date — including the "
           "conversation where the answer is no. **Budgets** are not reporting to me; they are the "
           "constraint that decides the solution.", after=80)

    m.para("**40 % — the productivity improvement from moving reporting out of spreadsheets.** "
           "**Tracking KPIs** only changes behaviour when the number sits where people work. I built "
           "capacity, cost and utilisation reporting in **SAP ERP**, **Power BI** and **Python** so that "
           "project success and solution effectiveness could be read in the same place as the delivery, "
           "and I have used that reporting as the argument for stopping things as well as starting them.",
           after=80)

    m.para("**5, 12, 14, 25 — the teams I have led.** "
           "Alignment across **cross-functional** teams is rarely a communications problem; it is a "
           "decision-rights problem. I run it with one plan, one message and a decision log — who decided "
           "what, when, and what it costs if we change it — which is also how I keep technical teams, "
           "sales, service and **senior management** in the same conversation without three versions of "
           "the truth.", after=80)

    m.para("**20+ — the years behind the method, and the reason a one-year contract does not worry me.** "
           "A fixed term is a mandate with a beginning, a middle and an end, and I have delivered to that "
           "shape my whole career: scope agreed, baseline set, risks owned, adoption measured, handover "
           "documented. I am based in Måløv, half an hour from Kongens Lyngby, and I work in **English** "
           "daily — with customers, suppliers and colleagues who do not share my first language.",
           after=80)

    m.para("**The customer's number is the deliverable.** Hempel sells the effect of a coating, not "
           "the coating — fuel saved, emissions avoided, an asset that lasts longer. The project manager's "
           "job is to make that effect deliverable: requirements that can be built, a plan that can be "
           "held, a deployment that can be supported, and a number the customer can take to his own "
           "board. Hempel's growth in Marine has come from exactly that argument, and it is the argument "
           "I want to spend the next year making on the inside.", after=80)

    m.para("**Why this role, and why a fixed term.** I have built the same machinery three times — in "
           "a 24/7 plant, in a pharma portfolio and in my own company: define the effect, agree the "
           "baseline, own the risks, measure it where people work. A one-year contract at Hempel is a "
           "chance to do that where the solutions already exist and the task is to land them with "
           "customers and colleagues. I would rather have twelve months of delivery than thirty-six "
           "months of positioning.", after=80)

    m.para("What I would want to understand first is where the solutions portfolio hurts today: which "
           "initiatives are late, which ones the sales teams cannot explain to a customer, and how "
           "**Marine Performance Advisory** and **Services** receive a solution after launch. That is "
           "where I would start, and it is what I would like to be measured on after twelve months.",
           after=60)
    m.meta("Kind regards", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- page 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFILE")
    m.para("Project manager with 20+ years in delivery, production and contracting — **authorised marine "
           "engineer (LV/MV/HV)** and **full P&L responsibility since 2023**. Has carried **37 concurrent "
           "CAPEX projects** of DKK 2–10 million with 25 specialists to customer acceptance with **zero "
           "critical findings**, coordinated **11 concurrent contracts**, and built KPI reporting in **SAP "
           "ERP**, **Power BI** and **Python** with **over 40 % productivity improvement**.", after=80)

    m.section("PLANS, BUDGETS AND DELIVERY")
    for label, body in [
        ("Project plans, timelines and budgets",
         "37 concurrent projects planned against one capacity pool and a fixed window calendar; monthly "
         "re-forecast, cost at completion and a decision log that shows what a change costs."),
        ("Plan, execute, monitor, close",
         "Every project opened with scope, acceptance criteria and a baseline, and closed with a "
         "documented handover — not with a meeting that ends when the budget does."),
        ("Risk and mitigation",
         "Risk registers with owner, date and cost estimate, reviewed monthly with the customer; "
         "opportunities priced with the same discipline as threats."),
    ]:
        m.bullet(label, body, after=20)

    m.section("SOLUTIONS, TESTING AND INTEGRATION")
    for label, body in [
        ("Testing, deployment and integration",
         "FAT/SAT, IQ/OQ/PQ and acceptance into live GMP/FDA/EMA environments; interfaces, data and "
         "rollback defined before go-live, not after."),
        ("Quality assurance",
         "Delivery packages checked line by line against the specification; deviations contained, "
         "root-caused with A3 and closed — zero critical findings at acceptance."),
        ("KPIs and solution effectiveness",
         "Reporting built in SAP ERP, Power BI and Python: capacity, cost, utilisation and adoption in "
         "one view, used to decide what continues and what stops."),
    ]:
        m.bullet(label, body, after=20)

    m.section("STAKEHOLDERS, CUSTOMERS AND IMPROVEMENT")
    for label, body in [
        ("External customers and partners",
         "Primary point of contact through the lifecycle: weekly site and commissioning calls, monthly "
         "steering with decisions logged, and one voice — including when the message is bad."),
        ("Cross-functional alignment",
         "Sales, engineering, procurement, service and management held to one baseline and one message; "
         "supplier lead times fed back into the plan instead of being found on site."),
        ("Continuous improvement",
         "Workflows, templates and reporting rebuilt from scratch in my own company; best practice "
         "written down as standard work so it survives the person who introduced it."),
    ]:
        m.bullet(label, body, after=20)

    m.section("PROFESSIONAL EXPERIENCE")
    jobs = [
        ("Owner / Technical Director",
         "ELOHVAC ApS · Copenhagen · May 2023–present",
         "5 electricians + 3 apprentices · full P&L · service, production and small projects",
         [("Customers, contracts and margin",
           "Every delivery under own P&L — quotes and terms negotiated, 11 concurrent contracts and "
           "supplier agreements managed, reporting and follow-up built from scratch.")]),
        ("Senior Commissioning Engineer / Project Manager, Electrical Systems",
         "Novo Nordisk A/S · Kalundborg · Nov 2022–Jul 2024",
         "37 concurrent CAPEX projects · 25 specialists · GMP/FDA/EMA",
         [("Portfolio, forecast and acceptance",
           "37 projects of DKK 2–10 million against shared capacity and fixed windows; monthly "
           "re-forecast in SAP ERP; FAT/SAT, IQ/OQ/PQ and punch closure — zero critical findings.")]),
        ("Project and Workshop Manager",
         "Ventek-Air · Copenhagen · Jan 2022–Nov 2022",
         "14 employees · 11 concurrent contracts · DKK 2–10 million",
         [("Delivery under pressure",
           "11 concurrent jobs in a 14-person workshop; daily board meetings and weekly capacity "
           "adjustment against the delivery date.")]),
        ("Maintenance and Operations Manager",
         "Lynetten under Biofos · Copenhagen · Aug 2017–Jan 2022",
         "Critical plant in 24/7 operation · pumps, HVAC, HV switchgear, SCADA",
         [("Uptime, windows and safety",
           "Preventive maintenance inside production windows; emergency response around the clock, 5S, "
           "spare-parts flow, LOTO and APV.")]),
        ("Electromechanical / production team lead",
         "ARJ Engineering · Tehran · Dec 2003–Mar 2010",
         "12 mechanics and technicians · machine workshop · industrial plant",
         [("Plan and output control",
           "12 people planned against the weekly plan with materials and tooling; output measured per "
           "person and per machine.")]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=16)

    # ---------------------------------------------------------------- page 3
    m.page_break()
    m.section("EDUCATION AND AUTHORISATION")
    m.edu("Authorised marine engineer — Danish LV/MV/HV authorisation",
          "Danish Safety Technology Authority · May 2023")
    m.edu("B.Tech, Technology Management and Mechanical Engineering (EQF 6)",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7.6/12")
    m.edu("Electrical and Mechanical Design, Electrical Engineering (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("Lean: 5S, PDCA, VSM, A3, standard work · Refrigeration and HVAC (AMU)",
          "Mercantec · 2021 · applied in capacity control and follow-up")

    m.section("LANGUAGES, PRACTICALITIES AND REFERENCES")
    m.para("**Danish: native** · **English: professional**, written and spoken, working language in "
           "meetings, contracts and documentation · Persian: native · **Based in Måløv**, half an hour "
           "from Kongens Lyngby · Driving licence and car · Available at short notice · References on "
           "request.", after=70)

    m.models_table("THE FIRST 90 DAYS — PORTFOLIO, STAKEHOLDERS, MEASUREMENT",
                   ("Period", "What happens, and how it is measured"), [
        ("Weeks 1–2",
         "Read the live solutions portfolio: scope, baseline, budget, owner and customer for each "
         "initiative. Meet Sales, R&D, Solutions Management, Product Management, Services, Commercial "
         "Excellence and Marine Performance Advisory; sit in on two customer conversations."),
        ("Day 30",
         "One page per initiative: baseline date, cost at completion, top three risks with mitigation, "
         "open decisions and who owns them. Everything where the plan and the business case disagree is "
         "flagged to the Director, Marine Solution Management."),
        ("Day 60",
         "Fixed rhythm: weekly delivery call across functions, monthly portfolio review with Sales and "
         "Services. KPI set agreed for solution effectiveness — adoption, time to value, cost against "
         "budget — and reporting placed where the teams already work."),
        ("Day 90",
         "Two initiatives measurably closer to launch with acceptance criteria met; testing and "
         "deployment checklists in use; a documented handover path into Services and Marine Performance "
         "Advisory; lessons written down as best practice."),
    ], widths=(1500, 8830))

    m.section("A SOLUTION IS JUDGED WHERE IT IS USED, NOT WHERE IT IS LAUNCHED")
    m.para("A launch is an internal event. Adoption is the only proof that the solution was needed. "
           "That is why I want the KPI defined before the build: what number should move, by how much, "
           "for which customer, and who looks at it every month. On a hull-performance solution the "
           "number is fuel and CO₂ and the interval between dockings; the discipline behind it — define "
           "the effect, instrument it, review it with the customer — is the same one I have used where "
           "capacity, cost and utilisation had to move in line with the **business objectives**.", after=70)

    m.section("THE HONEST PART — AND WHAT I BRING INSTEAD")
    m.para("I have not worked in **coatings** or in **marine** service, and I am not going to pretend "
           "that a docking interval means the same to me as it does to a fleet superintendent on day "
           "one. What I bring is the machinery around the domain: requirements taken from the people who own "
           "the problem, testing and integration into systems already in production, and one point of contact "
           "when the plan moves. The domain I learn the way I learned GMP — from the engineers, the data "
           "and the people who do it every day. Hempel sells into more than a hundred countries, so a "
           "solution that works in one market has to survive a **cross-cultural** handover in the next; "
           "that is why **English** is a working language for me, not a translation of Danish.", after=70)

    m.section("THE ONE-YEAR CLOCK IS AN ADVANTAGE, NOT A LIMIT")
    m.para("A fixed-term mandate removes the excuse of a slow start. I would spend the first month "
           "understanding the portfolio, the second making the plan honest, and the remaining ten "
           "delivering against it — with a handover that leaves the next person better equipped than I "
           "found the role. Twelve months is enough to change how a portfolio is run if the decisions are "
           "taken in the first quarter.", after=70)

    m.section("INFLUENCE WITHOUT A BOX ON THE ORG CHART")
    m.para("A solutions project manager rarely owns the people who have to deliver. Mine has been "
           "influence through the plan: a baseline that everyone has contributed to, a risk register "
           "with names in it, and a monthly review where the same numbers are shown to sales, technical "
           "teams and management — in a **global** organisation that shared view is the only way the same "
           "story reaches every market. When the numbers are shared, the conversation stops being about "
           "opinion — including the one about stopping a project nobody believes will land.", after=70)

    # ---------------------------------------------------------------- page 4
    m.page_break()
    m.models_table("WHAT THE ROLE REQUIRES — WHAT I HAVE DELIVERED",
                   ("Requirement in the posting", "Evidence"), [
        ("Developing and managing detailed project plans, timelines and budgets for solution delivery",
         "37 concurrent CAPEX projects of DKK 2–10 million with monthly re-forecast, cost at completion "
         "and a decision log; budgets treated as the constraint, not the report."),
        ("Coordinating cross-functional teams to ensure alignment on project goals and deliverables",
         "Sales, engineering, procurement, service and management held to one baseline and one message; "
         "weekly delivery call, monthly steering, decisions logged with an owner and a date."),
        ("Collaborating with internal stakeholders to define solution requirements and oversee implementation",
         "Requirements taken from the people who own the problem, frozen against a specification, and "
         "delivery packages checked line by line before release."),
        ("Acting as the primary point of contact for external customers and partners during the project lifecycle",
         "Primary customer contact through execution — weekly site and commissioning calls, monthly "
         "steering, one voice; partner and supplier management across 11 concurrent contracts."),
        ("Overseeing the testing, deployment and integration of solutions into existing systems",
         "FAT/SAT, IQ/OQ/PQ and acceptance into live systems; interfaces, data and rollback defined "
         "before go-live, with the customer's own inspectors signing the protocol."),
        ("Ensuring quality assurance processes are followed throughout the project",
         "Delivery packages checked against the specification, deviations contained and root-caused with "
         "A3, punch lists closed protocol by protocol — zero critical findings."),
        ("Tracking key performance indicators to measure project success and solution effectiveness",
         "KPI reporting built in SAP ERP, Power BI and Python — capacity, cost, utilisation and adoption "
         "in one view, with over 40 % productivity improvement."),
        ("Identifying areas for improvement in solution delivery processes and implementing best practices",
         "Workflows, templates and reporting rebuilt from scratch in my own company; improvements written "
         "as standard work so they outlive the person who introduced them."),
        ("Bachelor's degree in Business Administration, Project Management, Information Technology or a related field",
         "B.Tech in Technology Management and Mechanical Engineering (EQF 6), electrical and mechanical "
         "design (EQF 6), and authorised marine engineer (LV/MV/HV)."),
        ("5+ years of experience in project management, solution management or a related role",
         "20+ years of project and delivery management — 37 concurrent projects, 11 concurrent "
         "contracts, and full P&L responsibility since 2023."),
        ("Strong analytical and problem-solving abilities to identify risks and implement mitigation strategies",
         "Risk registers with owner, date and cost estimate; root-cause analysis with A3; monthly reviews "
         "where mitigation is a decision, not a description."),
        ("Proven ability to engage, influence and manage expectations of diverse stakeholders including technical teams, customers and senior management",
         "Influence without formal ownership: shared baseline and shared numbers with technical teams, "
         "sales, service and senior management — including the conversation about stopping a project."),
        ("Excellent communication skills, tailoring messaging to various stakeholders",
         "One plan for the team, one page for management, one voice for the customer — Danish and "
         "English, written and spoken."),
        ("Ability to plan, execute, monitor and close projects effectively",
         "Projects opened with scope and acceptance criteria and closed with documented handover; "
         "acceptance protocols signed by the customer, not by us alone."),
        ("Adaptable, innovative and customer-focused in approach",
         "Structure built from scratch in a new company, reporting automated in Power BI and Python, and "
         "the customer's number used as the definition of success."),
        ("Reporting to the Director for Marine Solution Management, working with Sales, R&D, Business Development, Solutions Management, Product Management, Services, Commercial Excellence and Marine Performance Advisory",
         "Used to a matrix: reporting to a director while delivering with sales, engineering, "
         "procurement and service, and handing over to the team that has to run the solution afterwards."),
        ("One-year fixed-term contract in Kongens Lyngby, application and CV in English",
         "Based in Måløv, half an hour from Kongens Lyngby; available at short notice; English working "
         "language with customers, suppliers and colleagues; a fixed term is a mandate with a deadline."),
    ], widths=(3600, 6746))

    m.section("WHAT TWELVE MONTHS SHOULD LOOK LIKE FROM THE OUTSIDE")
    m.para("One portfolio with a baseline the business trusts. One KPI set that Sales can explain to a "
           "customer and Services can support after launch. One documented path from solution to service. "
           "If those three exist a year from now, the fixed term has done its job — and the team that "
           "stays has something to build on.", after=80)

    return m.save(path, title="Solutions Project Manager — Hempel")


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Hempel_SolutionsProjectManager.docx')
    build(out)
    print(out)
