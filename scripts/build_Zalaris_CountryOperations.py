# -*- coding: utf-8 -*-
"""Zalaris ASA — country operations lead, Managed Services Denmark (on-site).

English posting → English document (en-GB): application page 1, CV page 2,
education + 90-day plan + four sections page 3, requirement matrix page 4.

STILVALG (master/STILREGISTER.md, policy 04.11.2026; godkendt af scripts/style_guard.py,
3/3 skift mod #190):
  register      = TEKNISK-DRIFTSNÆR — kort, konkret, deadline-nær. Passer til en payroll-drift,
                  hvor måneden har én dato, der ikke kan flyttes, og hvor fejl rettes om natten.
                  Sidst brugt #184.
  åbningsgreb   = B (NEGATIONEN) — "en lønkørsel bedømmes ikke den dag pengene lander, men den dag
                  kalenderen, overenskomsten og kundens nyansættelse er uenige". Sidst brugt #179.
  struktur      = PROBLEMKATALOGET — de tre ting, der går galt i en månedslukning (data for sent ·
                  manuelle handoffs · viden hos én person), hver med løsning og bevis. Sidst #176.
  kadence       = korte sætninger, datofaste eksempler, ingen strategijargon uden tal.

Ingen opdigtede fakta: ingen erfaring fra payroll, HR-outsourcing eller lønadministration påstås;
ingen påstand om SAP HCM/SAP-payroll-konfiguration, dansk lønlovgivning eller AI/RPA-projekter.
Overførslen er drift af kritiske serviceleverancer, P&L, standardisering, automatisering og
kompliansregimer (GMP/FDA/EMA, BEK 1608).

Policy: master/README.md — jobbet først, kandidaten kun som bevis, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Country Operations, Managed Services · Delivery, controls and margin'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("9 November 2026")
    m.meta("Zalaris A/S · Country operations, Managed Services Denmark · on-site, local scope")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Application: country operations, Managed Services Denmark — Zalaris", bold=True,
           color='1A1A1A')
    m.para("To the hiring team for Operations, Denmark", after=70)

    # ---------------------------------------------------------------- page 1
    m.para("**A payroll operation is not judged on the day the money lands. It is judged on the day the "
           "calendar, the collective agreement and the customer's new hire disagree.** That day decides "
           "whether the country organisation is a service or a scramble — and it is built months "
           "earlier, in the cut-off, in the controls and in the person who knows what to do when the file "
           "is wrong. I have run operations where the deadline could not move and the consequences were "
           "measured in something more expensive than a complaint, and I would like to run this one.",
           after=80)

    m.para("**The problems are not mysterious. There are three, and they repeat.**", after=60)

    m.para("**1. The data arrives late, and the exception is created upstream.** By the time the file "
           "reaches the payroll team, the error is already three weeks old and belongs to a manager who "
           "did not register a leave day. The fix is not more checking at the end; it is a **cut-off** "
           "with consequences, a control before the run instead of after it, and a customer who knows "
           "what happens to their next pay slip when they miss the date. I have run delivery like that in "
           "**24/7 operations**, where a missed window became an outage rather than a correction — and in "
           "**GMP/FDA/EMA** projects, where the control before release was the only thing standing between "
           "a deviation and a finding.", after=80)

    m.para("**2. Manual transactions and shadow spreadsheets make the error invisible.** Every hand-off "
           "is a place where an amount can change without anyone owning the change. This is exactly what "
           "**NextGen** is aimed at: standardise the flow, automate what repeats, and put the human "
           "attention where it belongs — **controls, exceptions and advisory**. I have done that from the "
           "inside: rebuilt workflows and templates from scratch in my own company, moved reporting out "
           "of spreadsheets into **SAP ERP**, **Power BI** and **Python**, and measured **over 40 % "
           "productivity improvement** while the volume grew. Automation I have delivered is real, "
           "documented and adopted — not a pilot that ended in a slide.", after=80)

    m.para("**3. The knowledge sits with one person, and the month depends on them not being on holiday.** "
           "That is a succession problem long before it is a payroll problem. I have built competence "
           "matrices, standard work and 1:1s so the answer is in the process and not only in a head, "
           "coached team leads, and taken teams of **5, 12, 14 and 25** through changes they had helped "
           "design. **Team Managers** grow when they own a number and a decision, not a task list.",
           after=80)

    m.para("**Country performance is a P&L with a service attached.** I have carried **full P&L "
           "responsibility since 2023** — quotes, rates, utilisation, supplier cost, month-end close — "
           "and before that budget and cost responsibility for a critical plant and a portfolio of **37 "
           "concurrent projects** of DKK 2–10 million. **Client profitability** is not a report I read; it "
           "is the decision about which services to standardise first, which customers cost more than the "
           "contract says, and where **resource planning** has to change before the margin does.",
           after=80)

    m.para("**Operational readiness is the part everyone skips.** A new customer goes live once, and "
           "whatever was not tested, documented and staffed at that moment becomes a permanent discount "
           "on the contract. I have taken facilities and systems into live operation with FAT/SAT, "
           "IQ/OQ/PQ, written handovers and a punch list closed with the customer — and I have been on "
           "the receiving end of a rushed handover in 24/7 service, so I know what it costs to inherit "
           "one.", after=80)

    m.para("**Growth is delivered by the same team that runs the month.** Partnering with **Sales and KAM** "
           "means answering three questions before signature: can we deliver it, what does it cost us, and "
           "are we ready on day one. I would rather say no to a scope I cannot staff than inherit it at "
           "renewal — and I would rather say yes with a plan the sales team can defend.", after=80)

    m.para("Zalaris describes **short decision paths** and **open communication** as the way the "
           "company works. In an operation with a monthly deadline that is not culture — it is how fast "
           "an exception gets fixed: the person who sees it can say it, and the person who can decide is "
           "reachable. **Everyone matters, aiming high and team spirit** is also a fair description of a "
           "run that cannot afford a weak link.", after=80)

    m.para("I work in **Danish** and **English** every week, I live in Måløv and I am on site by choice "
           "rather than by policy. What I would want to understand first is where the Danish operation "
           "loses its margin today: which customers run on manual workarounds, where the SLA is met but "
           "the rework is not counted, and which part of **NextGen** has landed here and which part is "
           "still a document.", after=60)
    m.meta("Kind regards", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- page 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFILE")
    m.para("Operations leader with 20+ years in critical service delivery, production and contracting — "
           "**authorised marine engineer (LV/MV/HV)** and **full P&L responsibility since 2023**. Has run "
           "a **24/7 plant**, carried **37 concurrent projects** of DKK 2–10 million with 25 specialists, "
           "led teams of **5, 12, 14 and 25**, and rebuilt workflows and reporting in **SAP ERP**, "
           "**Power BI** and **Python** with **over 40 % productivity improvement** — in regulated "
           "environments where a missed control became a finding.", after=80)

    m.section("OPERATIONS, P&L AND SERVICE PERFORMANCE")
    for label, body in [
        ("P&L, budgets and forecasting",
         "Full P&L since 2023: rates, utilisation, supplier cost, month-end close and after-calculation; "
         "monthly re-forecast against a delivery plan that has to hold."),
        ("Service performance and SLAs",
         "Delivery against agreed response times and delivery windows in 24/7 operation; critical issues "
         "handled immediately, recurring ones root-caused with A3 and closed."),
        ("Resource planning and margin",
         "37 concurrent projects planned against one capacity pool; staffing, competence and supplier "
         "cost matched to the contract — margin decided before the invoice."),
    ]:
        m.bullet(label, body, after=20)

    m.section("STANDARDISATION, AUTOMATION AND CONTROLS")
    for label, body in [
        ("Standardise and reduce manual work",
         "Workflows, templates and standard work built from scratch in my own company; repeated manual "
         "steps moved into systems, exceptions handled by people who know the process."),
        ("Automation and data",
         "Reporting automated in SAP ERP, Power BI and Python — capacity, cost and utilisation in one "
         "view, with over 40 % productivity improvement on the routines that used to eat the hour."),
        ("Controls and compliance",
         "Regimes with written controls and traceability: GMP/FDA/EMA, BEK 1608, DS/HD 60364, LOTO — "
         "documented before the work, checked after it, closed with the auditor in the room."),
    ]:
        m.bullet(label, body, after=20)

    m.section("PEOPLE, CUSTOMERS AND CHANGE")
    for label, body in [
        ("Leading managers and teams",
         "5, 12, 14 and 25 people led with 1:1s, competence matrices and development plans; team leads "
         "coached to own a number and a decision."),
        ("Customers under pressure",
         "Primary contact through execution: weekly calls, monthly steering with decisions logged, and "
         "one voice — including when the message is that the date has moved."),
        ("Change and readiness",
         "New customers and changes tested, documented and staffed before go-live; handover packages "
         "written so the receiving team can run the service on day one."),
    ]:
        m.bullet(label, body, after=20)

    m.section("PROFESSIONAL EXPERIENCE")
    jobs = [
        ("Owner / Technical Director",
         "ELOHVAC ApS · Copenhagen · May 2023–present",
         "5 electricians + 3 apprentices · full P&L · service, production and small projects",
         [("P&L, customers and standard work",
           "Every delivery under own P&L — quotes, terms, utilisation and supplier cost; workflows, "
           "templates and reporting built from scratch, with over 40 % productivity improvement.")]),
        ("Senior Commissioning Engineer / Project Manager, Electrical Systems",
         "Novo Nordisk A/S · Kalundborg · Nov 2022–Jul 2024",
         "37 concurrent CAPEX projects · 25 specialists · GMP/FDA/EMA",
         [("Portfolio, forecast and handover",
           "37 projects of DKK 2–10 million against shared capacity and fixed windows; monthly "
           "re-forecast in SAP ERP; handover and punch closure — zero critical findings.")]),
        ("Project and Workshop Manager",
         "Ventek-Air · Copenhagen · Jan 2022–Nov 2022",
         "14 employees · 11 concurrent contracts · DKK 2–10 million",
         [("Capacity and delivery under pressure",
           "11 concurrent jobs in a 14-person workshop; daily board meetings, weekly capacity "
           "adjustment, delivery dates held.")]),
        ("Maintenance and Operations Manager",
         "Lynetten under Biofos · Copenhagen · Aug 2017–Jan 2022",
         "Critical plant in 24/7 operation · pumps, HVAC, HV switchgear, SCADA",
         [("Uptime, windows and safety",
           "Preventive maintenance inside fixed windows; emergency response around the clock, 5S, "
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
           "meetings, contracts and documentation · Persian: native · **Based in Måløv**, on site in the "
           "Copenhagen area daily · Driving licence and car · Available at short notice · References on "
           "request.", after=70)

    m.models_table("THE FIRST 90 DAYS — COUNTRY, RUN, MODEL",
                   ("Period", "What happens, and how it is measured"), [
        ("Weeks 1–2",
         "Sit with the payroll runs, not the slides: read the SLA and the contract for the five largest "
         "customers, watch a month-end from the file arriving to the payslip going out, and list every "
         "manual step and workaround in the chain."),
        ("Day 30",
         "One page per customer: contract scope, SLA actuals, rework and exceptions, cost to serve, and "
         "the three root causes behind the recurring tickets. Where the SLA is met but the margin is "
         "not, it is on the page."),
        ("Day 60",
         "NextGen locally: the standard flow written down, the top manual transactions selected for "
         "automation with an owner and a benefit, and a cut-off and control regime agreed with the "
         "largest customers. Team Managers each own a number."),
        ("Day 90",
         "Measured: exceptions down, manual transactions down, cost to serve per payslip known, one "
         "service onboarding checklist in use, and a succession map for every critical role in the "
         "country organisation."),
    ], widths=(1500, 8830))

    m.section("A PAYROLL RUN IS A PROMISE WITH A DATE ON IT")
    m.para("Nothing about a payroll month is negotiable. The date is fixed, the employees are real, and "
           "a mistake is not a defect report — it is somebody's rent. That is the same shape as a 24/7 "
           "plant, where the window could not move either: you build backwards from the deadline, you put "
           "the controls before the irreversible step, and you rehearse the failure before it happens.",
           after=70)

    m.section("THE EXCEPTION IS THE PRODUCT, NOT THE PROBLEM")
    m.para("In an exception-based model the routine is automated and the people work on what does not "
           "fit — a new collective agreement, a cross-border hire, a customer whose master data has been "
           "wrong for six months. That is where the expertise and the customer trust are created, and it "
           "is also where a country organisation becomes hard to replace. Standardising the other eighty "
           "per cent is what buys the time — and **continuous improvement** is then measured in "
           "transactions removed, not in workshops held.", after=70)

    m.section("CONFIDENTIALITY IS A CONTROL, NOT A POLICY DOCUMENT")
    m.para("Payroll sits on the most sensitive data a company has, and access is the control that "
           "matters most: who can see the file, who can change an amount, and what the log shows "
           "afterwards. I have worked under GMP/FDA/EMA documentation rules and electrical safety regimes "
           "where every deviation was recorded, assigned and closed — the habit transfers directly, and "
           "so does the instinct to check the log rather than the promise.", after=70)

    m.section("THE HONEST PART — AND WHAT TRANSFERS")
    m.para("I have not run a payroll operation, and I am not going to claim a Danish payroll rule I would "
           "have to look up. What I bring is what the role also asks for and what is harder to hire: "
           "**Operations P&L**, service performance against fixed deadlines, standardisation and "
           "automation with a measured benefit, and the leadership of managers in a regulated "
           "environment. The payroll and regulatory expertise I would build with the specialists who "
           "already have it — and hold myself accountable for it commercially, not just politely.",
           after=70)

    m.section("WHAT TWELVE MONTHS SHOULD LOOK LIKE FROM THE OUTSIDE")
    m.para("A Danish operation whose month runs on a written flow instead of a rescue. Team Managers who own "
           "their numbers and a named successor. A cost to serve per payslip that can be defended in a "
           "global review, and a NextGen visible in the transaction count rather than in the strategy deck.", after=80)

    # ---------------------------------------------------------------- page 4
    m.page_break()
    m.models_table("WHAT THE ROLE REQUIRES — WHAT I HAVE DELIVERED",
                   ("Requirement in the posting", "Evidence"), [
        ("Own country performance: Operations P&L, budgets, forecasting, client profitability, resource planning and sustainable margin improvement",
         "Full P&L since 2023 — rates, utilisation, supplier cost and month-end close; 37 concurrent "
         "projects re-forecast monthly; margin decided before the invoice, not after."),
        ("Reliable, accurate and cost-effective delivery against contracts, SLAs and KPIs; act decisively on critical issues and recurring root causes",
         "24/7 operation with fixed windows; critical issues handled immediately, recurring ones "
         "root-caused with A3 and closed; delivery measured against agreed response times."),
        ("Strengthen country payroll, HR and regulatory expertise; advise customers and anticipate compliance risks",
         "Built competence matrices and standard work in regulated environments (GMP/FDA/EMA, BEK 1608); "
         "controls documented before the work and checked after it."),
        ("Lead NextGen locally: standardise processes, reduce manual transactions, focus teams on controls, exceptions and advisory",
         "Workflows and templates rebuilt from scratch in my own company; manual steps moved into "
         "systems and reporting automated in SAP ERP, Power BI and Python."),
        ("Drive productivity and automation through AI, RPA, process redesign and rightshoring",
         "Over 40 % productivity improvement delivered by redesigning routines and automating reporting; "
         "benefit measured in hours and cost, not in pilots."),
        ("Develop people and leaders: coach Team Managers, strengthen succession and future skills",
         "5, 12, 14 and 25 people led with 1:1s, competence matrices and development plans; team leads "
         "coached to own a number and a decision; succession mapped for critical roles."),
        ("Enable profitable growth with Sales and KAM: delivery feasibility, costs and operational readiness",
         "Quotes, terms and delivery feasibility assessed before signature in my own company; scope "
         "refused when it could not be staffed, and priced when it could."),
        ("Secure operational readiness so new customers and changes are tested, documented, staffed and ready for stable BAU",
         "FAT/SAT, IQ/OQ/PQ and handover packages before go-live; punch lists closed with the customer; "
         "receiving team able to run the service on day one."),
        ("Senior operational leadership in payroll, HR outsourcing, managed services or a comparable complex service environment, leading multiple teams or managers",
         "20+ years in critical service delivery and production — 24/7 plant, workshop, project "
         "portfolio and own company; 5, 12, 14 and 25 people led, including team leads."),
        ("Strong financial ownership, customer leadership and understanding of service performance, SLAs, KPIs and commercial priorities",
         "Full P&L accountability with month-end close and after-calculation; KPI reporting built and "
         "used as the decision basis, and the customer present in every steering decision."),
        ("Sound understanding of local payroll, HR and regulatory requirements, with the ability to build expert teams and advise customers",
         "Regulated environments run end to end — GMP/FDA/EMA and electrical safety — with expert teams "
         "built around the rules; payroll rules themselves would be learned from the specialists."),
        ("Lead transformation, organisational change and productivity improvement across distributed teams",
         "Structure, workflows and reporting built from scratch in a new company; change delivered with "
         "the teams, at several addresses and across shifts."),
        ("Excellent stakeholder management and communication skills",
         "One plan for the team, one page for management, one voice for the customer — in Danish and "
         "English, written and spoken."),
        ("Fluency in Danish and English",
         "Danish native; English professional as a working language with customers, suppliers and "
         "colleagues who do not share a first language."),
        ("A relevant degree or equivalent professional experience",
         "B.Tech in Technology Management and Mechanical Engineering (EQF 6), electrical and mechanical "
         "design (EQF 6) and authorised marine engineer (LV/MV/HV) — plus 20+ years of operational "
         "leadership."),
        ("Advantage: standardised nearshore or offshore delivery models, SAP payroll and HR technology, automation, AI or RPA, service onboarding, change orders and complex multi-country customers",
         "Delivery through suppliers and partners at distance; SAP ERP as the data backbone (not SAP HCM "
         "configuration); automation in Power BI and Python; service onboarding and change orders in my "
         "own contracts."),
    ], widths=(3600, 6746))

    return m.save(path, title="Country operations, Managed Services — Zalaris")


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Zalaris_CountryOperations.docx')
    build(out)
    print(out)
