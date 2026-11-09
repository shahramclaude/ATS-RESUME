# -*- coding: utf-8 -*-
"""Cavendish Hydrogen ASA — Project Manager, Project & Service (Lind, Herning).

English posting → English document (en-GB): application page 1, CV page 2,
education + 90-day plan + four sections page 3, requirement matrix page 4.

STILVALG (master/STILREGISTER.md, policy 04.11.2026; godkendt af scripts/style_guard.py,
3/3 skift mod #188):
  register      = VALIDERET PRODUKTION (GMP) — dokumentation, sporbarhed, afvigelse, accept,
                  "zero critical findings". Registeret er valgt, fordi denne rolle i praksis er en
                  acceptkæde: kontrakt → baseline → afvigelse → acceptprotokol → Service. Det er
                  det mindst brugte register i serien.
  åbningsgreb   = A (PLACEN) — beslutningen tages et andet sted, end den viser sig: stationen
                  tabes i overdragelsesmappen, ikke på pladsen. Sidst brugt #177.
  struktur      = DOKUMENTERNE — fire dokumenter afgør en station (kontrakten, baseline,
                  risikoregisteret, acceptprotokollen), derefter forecast, plads, hydrogen,
                  Service og rejseafstand. Ny struktur for dette dokument.
  kadence       = kort påstand, derefter dokumentation og tal — mere revisionsspor end brev.

Ingen opdigtede fakta: ingen hydrogen-, brintstation-, ATEX- eller EPC-erfaring påstås. Ingen
påstand om PMP/IPMA/PRINCE2 eller om tysk som arbejdssprog. Erfaringen er dokumenteret i
procesanlæg (GMP/FDA/EMA), 24/7-forsyning, el-infrastruktur og entreprise.

Policy: master/README.md — jobbet først, kandidaten kun som bevis, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Project Manager, Project & Service · Contract, delivery and acceptance'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("9 November 2026")
    m.meta("Cavendish Hydrogen ASA · Project Manager, Project & Service · Lind, 7400 Herning")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Application: Project Manager, Project & Service — Cavendish Hydrogen",
           bold=True, color='1A1A1A')
    m.para("To Dan Østergaard Lauridsen, Director, Projects & Service, EU", after=70)

    # ---------------------------------------------------------------- page 1
    m.para("**A station is not lost on site. It is lost in the handover file.** The scope that was "
           "never priced, the interface nobody owns, the date the customer thought was agreed — all of "
           "it is settled in the weeks between signature and mobilisation, and it only becomes visible "
           "fifteen months later, as a claim, a slip in the schedule, or an acceptance that will not "
           "close. Four documents decide whether that happens. I have spent twenty years keeping them "
           "true, and I would like to do it for your stations.", after=80)

    m.para("**1. The contract is the project's specification, not its preface.** Scope, exclusions, "
           "milestone dates, acceptance criteria, the change mechanism and the notice periods — if "
           "they are not read at handover, they are discovered at acceptance, by which time every "
           "option has a price. I have run **37 concurrent CAPEX projects** of DKK 2–10 million at Novo "
           "Nordisk against **GMP/FDA/EMA** requirements, where the delivery package was checked line "
           "by line before it left the building, and I have signed both sides of a subcontract in my own "
           "company: **11 concurrent contracts**, quotes, terms and the negotiation that follows when "
           "the site is not what the drawing said.", after=80)

    m.para("**2. The baseline is a promise with dates in it.** A schedule that everyone agrees with and "
           "nobody is staffed for is not a plan; it is a wish with a Gantt chart. At Novo Nordisk I "
           "planned 37 projects against one shared pool of 25 specialists, with a monthly cycle, a "
           "rolling 12-month capacity view and a **re-forecast** every month, so the date we gave the "
           "customer was the date the resources could actually carry.", after=80)

    m.para("**3. The risk register is the only place where a problem is still free.** After it happens, "
           "it costs money, schedule or reputation — before, it costs a line and an owner. I have run a "
           "critical plant in **24/7 operation** for more than four years, where the difference between a "
           "planned intervention and an outage was decided by what had been written down while the week "
           "was calm. Every item in my registers carries an owner, a date and a **cost estimate** — "
           "including the **opportunities**, which are the half of the register that usually stays empty.",
           after=80)

    m.para("**4. The acceptance protocol is written in week one, not in the last week.** " 
           "**Commissioning** is where a project is judged, and it is also where every undocumented "
           "decision comes back. I have taken facilities through FAT/SAT, IQ/OQ/PQ and customer "
           "acceptance with **zero critical findings**, closed punch lists with the customer's own "
           "inspectors, and handed over documentation that Service could work from on day one.",
           after=80)

    m.para("**5. The forecast is the page the customer and the board both read.** Cost control is not "
           "the invoice; it is the number you commit to in month three and still defend in month "
           "fifteen. I have carried **full P&L responsibility since 2023** — margin, hourly rates, "
           "utilisation, subcontractor cost and month-end close — and built the reporting that made the "
           "number visible before it became a surprise: **SAP ERP**, **Power BI** and **Python**, with "
           "**over 40 % productivity improvement** on the routines that used to eat the margin.",
           after=80)

    m.para("**6. Service is the project's second customer, and it inherits every shortcut.** A "
           "**handover to Service** is as-built documentation, spares, alarm lists, maintenance intervals, "
           "response times and a technician who has seen the station run. I have received that handover in "
           "24/7 on-call service, so I write it from the side that answers the phone at 03:00.", after=80)

    m.para("**Hydrogen, plainly.** I have not built or commissioned a hydrogen **refuelling station**. "
           "What I have done is take technical facilities from documentation to acceptance in "
           "environments where a deviation is a finding and a shortcut is an incident — pharmaceutical "
           "**process industry** under GMP, water and **energy** infrastructure in 24/7 drift, and "
           "electrical installations at MV/HV. The parts that are new to me — 350 and 700 bar, the "
           "ATEX zones, purging and inerting, the H2Station sequence — I learn the way I learned GMP: "
           "from the engineering, from the test protocols and from the people who built it. What I bring "
           "is the discipline that keeps a station on its date while I do.", after=80)

    m.para("**Lind, Herning — and the distance.** I live in Måløv, roughly three hours by car from "
           "Herning, and I am used to delivering from a distance: **travel** to sites, suppliers and "
           "customers is part of the schedule, not an exception to it, and I hold a driving licence and "
           "a car. **English** is my working language in meetings, documentation and on site. **German** "
           "is not — I would rather say that here than have it discovered in a customer meeting, and I "
           "would put it on the list for the first year.", after=80)

    m.para("I would like to know which stations are in the order book today, where acceptance has been "
           "hardest to close, and whether **change orders** live in the contract or in a spreadsheet — "
           "and I would like to be measured on the four documents: a baseline that holds, a risk "
           "register that is used, changes priced before execution, and an acceptance that closes "
           "without a discussion about scope.", after=60)
    m.meta("Kind regards", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- page 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFILE")
    m.para("Project manager with 20+ years in delivery, production and contracting — **authorised "
           "marine engineer (LV/MV/HV)** and **full P&L responsibility since 2023**. Has carried "
           "**37 concurrent CAPEX "
           "projects** of DKK 2–10 million with 25 specialists to customer acceptance with **zero "
           "critical findings**, coordinated **11 concurrent subcontracts**, run a critical plant in "
           "**24/7 operation**, and built cost reporting in **SAP ERP**, **Power BI** and **Python**.", after=80)

    m.section("CONTRACT, SCHEDULE AND FINANCIALS")
    for label, body in [
        ("Contract handover and scope",
         "Scope, exclusions, acceptance criteria and change mechanism read at handover, not at "
         "acceptance; delivery packages checked line by line before release."),
        ("Baseline, resources and re-forecast",
         "37 concurrent projects planned against 25 specialists and a fixed window calendar; monthly "
         "cycle with rolling 12-month capacity view and a new forecast every month."),
        ("Cost control and margin",
         "Full P&L since 2023: margin, rates, utilisation and subcontractor cost; month-end close and "
         "after-calculation on every project."),
    ]:
        m.bullet(label, body, after=20)

    m.section("COMMISSIONING, QUALITY AND DEVIATIONS")
    for label, body in [
        ("Commissioning and acceptance",
         "FAT/SAT, IQ/OQ/PQ and customer acceptance with zero critical findings; punch lists closed with "
         "the customer's inspectors, protocol by protocol."),
        ("Deviations and traceability",
         "Every deviation logged, contained and root-caused with A3; documentation handed over as a "
         "package Service can use — as-built drawings, spares, alarm lists."),
    ]:
        m.bullet(label, body, after=20)

    m.section("CUSTOMERS, STAKEHOLDERS AND TEAMS")
    for label, body in [
        ("Customer interface",
         "Primary customer contact through execution: weekly site and commissioning calls, monthly "
         "steering with logged decisions, and one voice — including when it is bad news."),
        ("Internal interfaces",
         "Sales, engineering, procurement and service held to one baseline; supplier lead times fed "
         "back into the schedule, not found on site."),
    ]:
        m.bullet(label, body, after=20)

    m.section("PROFESSIONAL EXPERIENCE")
    jobs = [
        ("Owner / Technical Director",
         "ELOHVAC ApS · Copenhagen · May 2023–present",
         "5 electricians + 3 apprentices · full P&L · service, production and small projects",
         [("Contracts, margin and capacity",
           "All work delivered under own P&L — quotes and terms negotiated, 11 concurrent subcontracts "
           "and supplier agreements managed, staffing across changing addresses, and templates, "
           "competence matrix and follow-up built from scratch.")]),
        ("Senior Commissioning Engineer / Project Manager, Electrical Systems",
         "Novo Nordisk A/S · Kalundborg · Nov 2022–Jul 2024",
         "37 concurrent CAPEX projects · 25 specialists · GMP/FDA/EMA",
         [("Projects, schedule and cost at completion",
           "37 projects of DKK 2–10 million planned against shared capacity and fixed windows; monthly "
           "re-forecast in SAP ERP, cost at completion defended in project reviews."),
          ("Deviations and acceptance",
           "Deviations handled with A3 and root-cause analysis; punch closure through FAT/SAT and "
           "IQ/OQ/PQ — zero critical findings.")]),
        ("Project and Workshop Manager",
         "Ventek-Air · Copenhagen · Jan 2022–Nov 2022",
         "14 employees · 11 concurrent contracts · DKK 2–10 million",
         [("Production, bottlenecks and forecasting",
           "11 concurrent jobs in a 14-person workshop; daily board meetings, weekly capacity adjustment.")]),
        ("Maintenance and Operations Manager",
         "Lynetten under Biofos · Copenhagen · Aug 2017–Jan 2022",
         "Critical plant in 24/7 operation · pumps, HVAC, HV switchgear, SCADA",
         [("Maintenance windows, on-call and safety",
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
           "meetings, contracts and documentation · Persian: native · **Based in Måløv**, three hours "
           "from Herning, and travelling to sites, suppliers and customers as the schedule requires · "
           "Driving licence and car · Available at short notice · References on request.", after=70)

    m.models_table("THE FIRST 90 DAYS — CONTRACT, BASELINE, ACCEPTANCE",
                   ("Period", "What happens, and how it is measured"), [
        ("Weeks 1–2",
         "Read every live contract: scope, milestones, acceptance criteria, notice periods and change "
         "log. Meet engineering, procurement, sales and service; visit a station in commissioning; "
         "speak to the customers of the three most difficult projects."),
        ("Day 30",
         "One page per live project: baseline date, cost at completion, top three risks, open change "
         "orders with owner and value. Everything where the forecast and the contract disagree is "
         "flagged to the Director, Projects & Service, EU."),
        ("Day 60",
         "Fixed rhythm: weekly site and commissioning call, monthly forecast reviewed with sales, "
         "engineering, procurement and service. Change-order log where every item carries a price, a "
         "customer reference and a date; acceptance checklist opened at every kick-off."),
        ("Day 90",
         "The two nearest projects measurably closer to acceptance with documented punch closure; risk "
         "register reviewed with the customer on the largest project; handover-to-Service checklist "
         "agreed — as-built, spares, alarms, training, response times."),
    ], widths=(1500, 8830))

    m.section("A COMMISSIONING IS A DOCUMENT BEFORE IT IS A SWITCH-ON")
    m.para("By the time a station is ready to start, the argument about what was included has usually "
           "already been had twice. It is decided by whether the acceptance criteria were written into "
           "the contract, whether the test protocols existed before the first cable was pulled, and "
           "whether the punch list was opened while the trades were still on site. I have closed "
           "acceptance that way at Novo Nordisk with the customer's own inspectors in the room, and it "
           "is the cheapest week of any project.", after=80)

    m.section("THE CHANGE ORDER NOBODY WROTE IS THE ONE YOU FUND")
    m.para("A change is not a claim until someone puts a notice, a price and a date on it — before the "
           "work is done. In my own company that discipline is survival: 11 concurrent subcontracts, "
           "and every extra ordered from a supplier without a written price is margin that leaves the "
           "company quietly. On a station the same rule applies at a different scale: changes are "
           "priced when they are identified, agreed with the customer when they are priced, and then "
           "executed.", after=80)

    m.section("SAFETY IS THE FIRST LINE OF THE SCHEDULE, NOT A PARAGRAPH IN IT")
    m.para("Hydrogen at 350 and 700 bar, hot work, lifting and live electrical work all sit under the "
           "same principle: the dangerous activity is planned before it is permitted. I have worked "
           "under BEK 1608 with written risk assessments, LOTO and work permits, and I have stopped work "
           "on a 24/7 plant when the procedure was not in place. A day lost to a stop is recoverable; a "
           "day lost to an incident is not.", after=80)

    m.section("A HANDOVER TO SERVICE IS A LIST, NOT A MEETING")
    m.para("Service does not need a presentation; it needs the as-built drawings, the spare-parts list "
           "with lead times, the alarm list with priorities, the maintenance intervals, the response "
           "times the customer has been promised, and a technician who has seen the station run. I have "
           "carried the on-call phone for a critical plant, so I know exactly which of those is missing "
           "when a handover is rushed — and it is never the presentation.", after=80)

    # ---------------------------------------------------------------- page 4
    m.page_break()
    m.models_table("WHAT THE ROLE REQUIRES — WHAT I HAVE DELIVERED",
                   ("Requirement in the posting", "Evidence"), [
        ("Leading projects from contract handover to final customer acceptance",
         "37 concurrent CAPEX projects of DKK 2–10 million taken from specification and FAT/SAT to "
         "customer acceptance and punch closure — zero critical findings."),
        ("Managing project plans, schedules, budgets and resources",
         "Monthly cycle with rolling 12-month capacity view and re-forecast; 25 specialists and 11 "
         "concurrent subcontracts planned against the same baseline."),
        ("Ensuring contractual compliance and handling project risks and opportunities",
         "Scope, exclusions, notice periods and acceptance criteria tracked from handover; risk "
         "registers with owner, date and cost estimate — including priced opportunities."),
        ("Driving change orders, claims and commercial negotiations",
         "Change and variation handling in own P&L company: 11 concurrent subcontracts, quotes and "
         "terms negotiated, extras priced in writing before execution."),
        ("Coordinating site execution, commissioning and customer interfaces",
         "Site coordination under BEK 1608, LOTO and APV with suppliers, subcontractors and the "
         "customer's contractors; FAT/SAT and IQ/OQ/PQ run with the customer's inspectors."),
        ("Managing project financials, forecasting and cost control",
         "Full P&L since 2023 — margin, rates, utilisation, subcontractor cost, month-end close; cost at "
         "completion defended monthly in project reviews and reported in SAP ERP."),
        ("Building strong customer and stakeholder relationships",
         "Primary customer contact through execution: weekly site and commissioning calls, monthly "
         "steering with logged decisions, and one voice — also when the message is bad."),
        ("Ensuring a successful handover to Service",
         "Handover packages with as-built documentation, spares, alarm lists and response times; ran "
         "24/7 on-call service and knows what is missing when a handover is rushed."),
        ("Primary customer contact working closely with Sales, Engineering, Procurement, Service, suppliers and subcontractors",
         "Daily interface across sales, engineering, procurement and service; material and supplier lead "
         "times fed back into the schedule instead of being found on site."),
        ("Delivering safely, on time, within budget and in accordance with contractual requirements and quality standards",
         "24/7 operation and GMP/FDA/EMA delivery: written risk assessments, permits and LOTO; deviations "
         "contained, root-caused and closed with A3."),
        ("Bachelor's or master's degree in engineering, project management or a related technical field",
         "Authorised marine engineer (LV/MV/HV); B.Tech in technology management and mechanical "
         "engineering (EQF 6); electrical and mechanical design (EQF 6)."),
        ("Experience managing industrial, infrastructure, energy- or EPC projects",
         "Industrial installations and production, energy and water infrastructure in 24/7 operation, "
         "pharmaceutical process plant under GMP, and 11 concurrent subcontract packages."),
        ("Strong commercial awareness with contract management, change orders and claims",
         "Own company since 2023 with full P&L: contract terms, variations, subcontractor negotiation, "
         "margin and cash; after-calculation on every project."),
        ("Comfortable managing project budgets, forecasting and cost control",
         "Project budgets of DKK 2–10 million re-forecast monthly; cost at completion, earned hours and "
         "utilisation followed in SAP ERP, Power BI and Python."),
        ("International environment, confident English, preferably German and willing to travel",
         "English professional as working language in meetings, contracts and documentation; travel to "
         "sites and suppliers part of the schedule; German is not a working language — stated plainly, "
         "on the list for year one."),
        ("Experience from hydrogen, renewable energy, the process industry or oil and gas",
         "No hydrogen stations. Process industry under GMP/FDA/EMA, energy and water infrastructure and "
         "MV/HV electrical installations — the same documentation, deviation and acceptance discipline, "
         "in a different medium."),
        ("Project management certification such as PMP, IPMA or PRINCE2",
         "No certification yet. Method documented in practice — baseline, forecast, risk register, "
         "change log, acceptance protocol — and I will certify on the company's preferred standard."),
    ], widths=(3600, 6746))

    m.section("THE CUSTOMER DOES NOT BUY A STATION — THEY BUY THE DAY IT WORKS")
    m.para("A **heavy-duty** haulier plans around a ten-minute stop, and an operator plans around the "
           "availability of the whole network: the AFIR requirement of a **zero-emission** refuelling "
           "station every 200 kilometres only works if the stations that are built actually run. That is "
           "why the last week of a project matters more than the first, and why the acceptance protocol, "
           "the spare-parts list and the service handover are not administration — they are the product. "
           "Cavendish has spent twenty-two years and 150-plus stations building that reputation; my job "
           "would be to protect it one delivery at a time.", after=80)

    m.section("WHY THIS ROLE, AND WHY NOW")
    m.para("The last two years have narrowed the portfolio and the organisation, and shifted the "
           "weight from developing the next generation to delivering what has already been signed — which "
           "makes execution the company's whole priority, and it is the part of the job I am best at and "
           "want **ownership** of. I am not looking for a station to design. I am looking for the four "
           "documents that decide whether it is delivered, and the team and the customer that have to "
           "believe them.", after=80)

    return m.save(path, title="Project Manager, Project & Service — Cavendish Hydrogen")


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Cavendish_ProjectManager.docx')
    build(out)
    print(out)
