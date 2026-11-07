# -*- coding: utf-8 -*-
"""Nordic RCC — Lead Portfolio Manager (PMO), Copenhagen Towers, Ørestad.

English posting → English deliverable (en-GB): motivated p1 (the posting asks for a few
sentences on why the role is interesting), CV p2–3, 90 days + requirement matrix p4.
Policy: master/README.md — job first, candidate only as evidence, no hedges.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = "Lead Portfolio Manager · Portfolio governance, budgeting and reporting"
CONTACT = "+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Copenhagen, Denmark"


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("7 November 2026")
    m.meta("Nordic RCC · PMO · Copenhagen Towers, Ørestad")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Application: Lead Portfolio Manager", bold=True, color='1A1A1A')
    m.para("To the Head of PMO and the Nordic RCC leadership team", after=70)

    # ---------------------------------------------------------------- page 1
    m.para("A project portfolio is not a list of projects; it is a set of promises about capacity, money and "
           "deadline that the organisation has made to its owners. The portfolio manager's product is not the "
           "plan — it is the decision: what starts, what waits, what is stopped, and what the leadership team "
           "can safely tell four transmission system operators and their regulators about next quarter. That is "
           "the work I am applying for.", after=80)

    m.para("**Nordic RCC's portfolio has one distinguishing feature: the customers are the system operators.** "
           "Planning data and security analysis for Finland, Norway, Sweden and Denmark cannot be delivered late "
           "or half-finished, and the European **renewable energy** transition adds projects to the portfolio at a "
           "rate the organisation has to absorb without losing discipline. A PMO in that setting earns its place by making the "
           "portfolio predictable — dependencies known, capacity visible, and every commitment costed before it "
           "is made.", after=80)

    m.para("**Optimisation means something specific: every project has to earn its slot.** In a portfolio of "
           "**37 concurrent capital projects** I ran the weekly re-prioritisation myself: which projects were "
           "still strategically justified, which were only still alive because they had started, and which "
           "needed capacity that another project was already using. Stopping or pausing a project is the part of "
           "portfolio management nobody enjoys and every portfolio needs; I have taken those decisions on "
           "evidence and written down what was decided and why.", after=80)

    m.para("**Budgeting and long-term planning work only when Finance and delivery use the same numbers.** I "
           "have owned budgets and monthly forecasts on projects of **DKK 2–10m** and across a portfolio of "
           "**37** in **SAP ERP**, run the monthly close against actuals, and built the resource and cost "
           "scenarios behind the long-term plan in Power BI, Excel/Power Query and Python. Investment cases "
           "with NPV, IRR and sensitivity analysis are part of my own business today, and they are what makes a "
           "recommendation to a leadership team defensible rather than optimistic.", after=80)

    m.para("**Monthly reporting is a compression exercise, not a data dump.** What a leadership team needs is "
           "two pages: what moved, what did not, which dependency is now on the critical path, and what "
           "decision is being asked for. I have delivered that pack monthly for two years to management and "
           "client, with a dependency register where every interface has a named owner, and critical deadlines "
           "flagged early enough that a decision could still change the outcome.", after=80)

    m.para("**Stage-gate is a conversation with a date on it — and the evidence behind it has to survive an "
           "audit.** I have applied a stage-gate model through **FAT/SAT and IQ/OQ/PQ** gates in a "
           "**GMP/FDA/EMA validated environment**, where the documentation had to prove the work years later, "
           "and where the portfolio closed with **zero critical findings**. Best practice is not a folder: it is "
           "a gate with criteria, a decision recorded, and evidence that someone else can follow after you have "
           "left.", after=80)

    m.para("**The tools should serve the decision, not the other way round.** I work daily in **SAP ERP, CMMS, "
           "Power BI, Excel/Power Query and Python**, and where a portfolio or capacity view did not exist I "
           "built it — then handed it over so the team could run it without me. That is also where the "
           "**over 40 % productivity gain** in my own business came from: fewer manual steps between the data "
           "and the decision.", after=80)

    m.para("**Stakeholders are the portfolio's real constraint.** Project managers, experts, Finance, team leads "
           "and external owners all hold part of the truth about what is possible. My job is to be the fixed "
           "point they bring it to: consistent answers, deadlines that mean something, and the difficult "
           "priority conversation held early rather than after the milestone was missed. Nordic RCC's values — "
           "**fellowship, curiosity, respect and transparency** — describe the way that works in practice, "
           "including when the answer is no.", after=80)

    m.para("**A portfolio manager is judged on whether the organisation can run the portfolio without them in "
           "the room.** That is a question of a handful of things done identically every month: one register, "
           "one reporting cadence, one gate model, one set of numbers agreed with Finance. I have built that in "
           "smaller organisations — a gate model project managers actually used, a monthly pack that took two "
           "hours instead of two days, and documentation that survived an audit — and the test is always the "
           "same: is the decision obvious to the next person who reads it?", after=80)

    m.para("I am based in Måløv and can be in **Copenhagen Towers** daily, with **fluent English** and native "
           "Danish and Persian, and I can complete a **background check and national security clearance**. I "
           "would like to hear how the portfolio is sized today against the coming green-transition workstreams, "
           "and where the PMO sees the biggest gap between capacity and commitment.", after=70)
    m.meta("Yours sincerely", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFILE")
    m.para("Portfolio, project and operations leader with 20+ years in technical delivery — **portfolio "
           "governance, budgeting, dependency tracking and monthly reporting** to leadership and client. Ran a "
           "portfolio of **37 concurrent capital projects** with **25 specialists** at Novo Nordisk: stage-gate "
           "governance, resource allocation, monthly cost and risk reporting and **zero critical findings** at "
           "handover. Owns a **full P&L** today, with budget, forecast, investment cases (NPV/IRR) and "
           "**over 40 % productivity gain** from data-driven tooling. Works daily in **SAP ERP, Power BI, "
           "Excel/Power Query and Python**; **fluent English**, native Danish and Persian.", after=80)

    m.section("PORTFOLIO, GOVERNANCE AND FINANCE")
    for label, body in [
        ("Portfolio prioritisation",
         "37 concurrent projects re-prioritised weekly against strategy, capacity and risk; decisions to start, "
         "pause or stop taken on evidence and recorded, with the consequence for the rest of the portfolio."),
        ("Budget, forecast and long-term planning",
         "Project budgets of DKK 2–10m and a portfolio budget in SAP ERP; monthly close against actuals, "
         "resource plans and cost scenarios for the long-term plan, and investment cases with NPV, IRR and "
         "sensitivity."),
        ("Monthly reporting and dependencies",
         "Two-page management and client pack on progress, cost and risk; dependency register with a named "
         "owner per interface, and critical deadlines flagged 90 days ahead of the decision point."),
        ("Stage-gate and audit evidence",
         "Stage-gate model with defined gates, acceptance criteria and recorded decisions; documentation that "
         "proved the work in a GMP/FDA/EMA validated environment — zero critical findings at handover."),
        ("Process improvement and standardisation",
         "Standard work, 5S and PDCA with 5–14 people; handover defects reduced, reporting automated, and "
         "processes documented so they survive the person who built them."),
        ("Tools, data and programming",
         "SAP ERP, CMMS, Power BI, Excel/Power Query and Python in daily use; portfolio and capacity dashboards "
         "built where no tool existed and handed over to the team that runs them."),
    ]:
        m.bullet(label, body, after=25)

    m.section("EXPERIENCE")
    jobs = [
        ("Owner / Technical Director",
         "ELOHVAC ApS · Copenhagen · May 2023–present",
         "5 electricians and 3 apprentices · full P&L · budget, forecast and investment cases",
         [("P&L, pricing and portfolio economics",
           "Budget, monthly forecast, cost control and investment cases with NPV, IRR and scenarios; "
           "prioritisation of a live order book against capacity, with own Python and Claude tooling giving "
           "over 40 % productivity gain.")]),
        ("Senior Commissioning Engineer / Project Manager, Electrical Systems",
         "Novo Nordisk A/S · Kalundborg/Bagsværd, Denmark · Nov 2022–Jul 2024",
         "37 parallel capital projects · 25 specialists · DKK 2–10m each · GMP/FDA/EMA validated environment",
         [("Portfolio governance and reporting",
           "Stage-gate governance from requirement to handover; monthly progress, cost and risk reporting to "
           "management and client; dependency tracking across engineering, procurement and site — zero critical "
           "findings.")]),
        ("Project and Workshop Manager",
         "Ventek-Air · Copenhagen · Jan 2022–Nov 2022",
         "14 employees · 11 concurrent projects · DKK 2–10m per project",
         [("Capacity, sequencing and delivery",
           "Daily board meetings and bottleneck analysis; 11 projects sequenced against one capacity pool, with "
           "subcontractors and interfaces agreed before the work started.")]),
        ("Operations and Maintenance Manager",
         "Lynetten under Biofos · Copenhagen · Aug 2017–Jan 2022",
         "Critical plant in 24/7 operation · maintenance strategy · spare-part and resource planning",
         [("Maintenance portfolio and improvement",
           "Preventive maintenance and replacement planning against criticality and budget; 5S, standard work "
           "and PDCA on workshop and store; energy programme delivering over 40 % lower consumption.")]),
        ("Electromechanical Technician / Production Team Leader",
         "ARJ Engineering · Tehran · Dec 2003–Mar 2010",
         "12 mechanics and technicians · machine workshop · industrial equipment",
         [("Planning, targets and follow-up",
           "Shift planning, material planning and performance follow-up for 12 technicians; root-cause analysis "
           "and corrective actions on industrial plant.")]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section("EDUCATION AND AUTHORISATION")
    m.edu("B.Tech, Technology Management and Mechanical Engineering",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7.6/12")
    m.edu("Electrical and Mechanical Engineering Design, Electrical Engineering (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("Danish HV/LV authorisation — elautoriseret maskinmester (LV/MV/HV)",
          "Danish Safety Technology Authority · May 2023")

    m.section("LANGUAGES, PRACTICALITIES AND REFERENCES")
    m.para("English: fluent, written and spoken · Danish: native · Persian: native · **Based in Måløv**, able to "
           "be in Copenhagen Towers daily · **Background check and national security clearance: yes** · "
           "Available at short notice · References on request.", after=70)

    m.models_table("THE FIRST 90 DAYS — THE PORTFOLIO, THE NUMBERS AND THE GATES",
                   ("Period", "What happens, and how it is measured"), [
        ("Week 1–2",
         "Read the current portfolio, the budget baseline and the last twelve months of reporting; meet "
         "Finance, the project managers, the Nordic Project Support team and the experts; map where capacity, "
         "cost and dependencies are actually tracked today."),
        ("Day 30",
         "One portfolio register with owner, budget, forecast, dependency and next decision per project; the "
         "five dependencies most likely to move the critical path identified with a named owner; reporting "
         "cadence and template agreed with the Head of PMO and Finance."),
        ("Day 60",
         "Monthly pack delivered in the agreed format — progress, cost, dependencies and a clear ask per "
         "decision; resource plan for the next four quarters built with Finance and team leads; stage-gate "
         "criteria reviewed against what the projects actually produce."),
        ("Day 90",
         "First portfolio recommendation taken to the leadership team with cost, risk and sequencing spelled "
         "out; audit evidence trail defined for the gates; and a short list of processes to standardise next, "
         "agreed with the teams that use them.")])

    m.section("A PORTFOLIO IS A SET OF PROMISES, NOT A LIST OF PROJECTS")
    m.para("Every project in a portfolio has already promised something to someone — a date, a capability, a "
           "saving — and the portfolio manager's job is to know whether those promises can all be kept at the "
           "same time. That is why capacity and dependencies matter more than status colours: a portfolio is "
           "only predictable when the same three constraints are visible in every report — who is doing the "
           "work, what it depends on, and what decision is waiting.", after=80)

    m.section("THE REPORT IS ONLY WORTH THE DECISION IT PRODUCES")
    m.para("A monthly report that describes everything and asks for nothing is administration. I write the pack "
           "backwards: start with the decision the leadership team has to take this month, then include only the "
           "evidence that decision needs. It makes the report shorter, the discussion sharper, and the "
           "follow-up unambiguous — because every open item from last month is the first page of the next one.", after=80)

    m.section("STAGE-GATE IS A CONVERSATION WITH A DATE ON IT")
    m.para("A gate that everyone passes is not a gate. In a validated environment I worked with gates that "
           "could stop a project: criteria agreed before the phase began, evidence reviewed by someone who was "
           "not the author, and a recorded decision with a name against it. That is also what makes an audit "
           "straightforward — the documentation shows what was decided, when, and on what basis, and it does "
           "not depend on the memory of the person who was there.", after=80)

    m.section("CAPACITY IS THE ONLY CONSTRAINT THAT CANNOT BE NEGOTIATED")
    m.para("Money can be found, scope can be argued and deadlines can occasionally be moved — the hours of the "
           "people who do the work cannot. That is why resource allocation is the centre of portfolio "
           "management and not a spreadsheet exercise afterwards: who is on which project, at what percentage, "
           "and what happens to the plan when someone leaves or a project turns out to need twice the effort. I "
           "have run that conversation weekly with 5–25 people and a single capacity pool, and the discipline "
           "that makes it work is refusing to load a person above what the calendar supports.", after=80)

    m.section("IN A TRANSMISSION SYSTEM PORTFOLIO, A WRONG NUMBER IS A DECISION")
    m.para("Nordic RCC delivers planning data and security analysis to four transmission system operators. In "
           "that setting a status that is two weeks optimistic, or a dependency nobody registered, does not stay "
           "in the PMO — it travels into a decision about security of supply. It is why I treat the reporting "
           "figures as engineering evidence: dated, traceable to a source, and consistent between the project "
           "plan, the budget and the monthly pack. The same standard applied in a GMP-validated environment, "
           "where documentation had to prove the work years later.", after=80)

    m.page_break()

    m.models_table("WHAT THE ROLE REQUIRES — WHAT I HAVE DELIVERED", ("Requirement in the posting", "Evidence"), [
        ('Continuous optimisation of the portfolio — efficiency and strategic alignment',
         '37 concurrent projects re-prioritised weekly against strategy, capacity and risk; projects cut or paused on evidence, with the decision recorded.'),
        ('Budgeting and long-term planning with Finance; resource allocation',
         'Portfolio and project budgets of DKK 2–10m in SAP ERP; monthly forecast against actuals, and capacity agreed with the delivery teams.'),
        ('Monthly portfolio reporting including dependency tracking to leadership',
         'Two-page monthly pack to management and client on progress, cost and risk; dependency register with one owner per interface and early deadlines.'),
        ('Portfolio recommendations for the leadership team and Head of PMO',
         'Stop, start and accelerate recommendations with cost, risk and sequencing spelled out — presented for decision, not for information.'),
        ('Collaboration between internal and external stakeholders for execution',
         'Joint forums with client organisation, consultants, vendors and authorities across 37 projects; escalations owned by a person and closed in days.'),
        ('Central point of contact for project inquiries from project managers and teams',
         'Single commercial and technical contact for clients, consultants and vendors in own business; queries triaged the same day with owner and date.'),
        ('Dependency overview and support on products, processes and resources',
         'Interface and dependency register at portfolio level; capacity, material and competence gaps surfaced before they became delivery risk.'),
        ('Own and maintain the stage-gate model, governance and project guidance',
         'Gates defined by criteria, decisions recorded, and the same guidance used by project managers and specialists across 37 capital projects.'),
        ('Documented best practice and evidence for future audits',
         'Documentation that proved the work years later in a GMP/FDA/EMA validated environment; audits passed on evidence, zero critical findings.'),
        ('Continuous improvement — inefficiencies removed, processes standardised',
         'Standard work, 5S and PDCA with 5–14 people; reporting steps automated in Python and Excel, giving over 40 % productivity gain in own business.'),
        ('Oversee portfolio and resource management processes and tools',
         'SAP ERP, CMMS, Power BI, Excel/Power Query and Python daily; portfolio and capacity dashboards built where no tool existed, then handed over.'),
        ("Master's degree in economics, engineering or a related field",
         'B.Tech in technology management and mechanical engineering (7.6/12) plus electrical and mechanical engineering design at EQF 6.'),
        ('Proficient in English, written and spoken; other languages a plus',
         'Fluent English for technical, commercial and management reporting; native Danish and native Persian in a company of 23 nationalities.'),
        ('Strong problem-solving and data-driven decisions',
         'Measurement before investment: over 40 % lower energy consumption at Lynetten and 40 % lower energy cost in a Novo Nordisk programme.'),
        ('Teamwork and a collaborative mindset',
         'Delivery through 25 specialists, 14 staff, 12 technicians and 5 electricians plus 3 apprentices; decisions taken with those who live with them.'),
        ("Respect for agreements, deadlines, other people's time and customer needs",
         'Acceptance dates held across 37 projects; customer requirements clarified in writing before work started, deadlines treated as commitments.'),
        ('Structured and orderly in work and approach to tasks',
         'A written plan, a named owner and a date for every action; 5S and standard work on workshop and store, and templates that do not change monthly.'),
        ('Strong interpersonal skills',
         'Direct dialogue with clients, consultants, vendors, authorities and specialists; difficult conversations held early and in person.'),
        ('Advanced Excel and data analysis, preferably with programming',
         'Excel and Power Query at model level, Power BI dashboards and Python in daily use; the reporting and capacity models I needed were built.'),
        ('5–10+ years as project portfolio manager, ideally with renewables',
         'Portfolio ownership since 2017 across 37 concurrent capital projects plus own business since 2023; SAP ERP, CMMS, Power BI and Python owned.'),
        ('Strong financial background; trusted advisor to the leadership team',
         'Full P&L and DKK 2–10m project budgets; forecast, monthly close, cost control and investment cases with NPV, IRR and scenarios.'),
        ('Management reports and presentations, with follow-up on activities',
         'Monthly management and client pack for two years; every action tracked to closure and the next report opened from the open items.'),
        ('Gain and share knowledge of portfolio methods and processes',
         'Competence matrices, mentoring and one-to-ones for 5–25 people; the stage-gate and reporting models documented so others could run them.'),
        ('Experience with both portfolio management and project management',
         '37 projects managed individually and as a portfolio; governance, dependency tracking and resource allocation at portfolio level since 2017.'),
    ], widths=(3600, 7046))

    return m.save(path, title="Lead Portfolio Manager — Nordic RCC",
                  subject="Portfolio governance, budgeting, dependency tracking and monthly reporting",
                  keywords="portfolio management, pmo, stage-gate, governance, budgeting, resource allocation, "
                           "dependency tracking, monthly reporting, excel, python, power bi, nordic rcc")


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_NordicRCC_LeadPortfolioManager.docx')))
