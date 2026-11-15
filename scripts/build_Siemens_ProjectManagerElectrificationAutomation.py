# -*- coding: utf-8 -*-
"""Siemens A/S — Project Manager, Electrification & Automation (Job ID 525564), Ballerup.

English posting → English deliverable (en-GB): application p1, CV p2, education +
90 days + three sections p3, requirement matrix + two sections p4.

STYLE CHOICE (master/STILREGISTER.md, policy of 04.11.2026):
  register      = INGENIØR-PRÆCIS (definitions, interfaces, tolerances, standards) — first
                  use of this register in the log; deliberately not the commercial register
                  used for #181 (Bravida) or the contractor register of #176/#178.
  opening device = I (TESERNE) — three theses stated up front and proved one by one. Not
                  used before; G (question) went out with #181, B (negation) is still banned.
  structure     = ORDLISTEN — page 1 walks the role's own vocabulary (maturation, scope,
                  schedule, cost to complete, risk and opportunity, commissioning,
                  framework, multidisciplinary, language, location) and gives evidence per
                  term. Not used before; the last four builds used Målestokken,
                  Beslutningskæden, Før/efter and Problemkatalog.
  cadence       = short declarative definitions, then one long evidential sentence —
                  reversed from the Bravida letter (#181), which opened long and closed short.

Policy: master/README.md — job first, candidate only as evidence, no hedges.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Project management · Substation automation, control and protection'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4 November 2026")
    m.meta("Siemens A/S · Smart Infrastructure, Electrification & Automation · Project Manager · "
           "Job ID 525564 · Ballerup")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Application: Project Manager, Electrification & Automation", bold=True, color='1A1A1A')
    m.para("To the Project Execution team, Electrification & Automation, Siemens Smart Infrastructure", after=70)

    # ---------------------------------------------------------------- page 1
    m.para("Three things decide whether a substation package is delivered on the date it was promised: "
           "whether the scope was closed before the schedule was opened, whether commissioning was planned "
           "while the design was still on paper, and whether the person who signs the handover sat in the "
           "room where the technical decisions were made. The rest of this letter is about those three, in "
           "the vocabulary the role is advertised in.", after=80)

    m.para("**Maturation — a project is cheapest to change before it is a project.** By the time a package "
           "is handed over for execution, its interfaces are either defined or inherited: civil works, "
           "protection settings, telecom, the customer's control room and the outage window the grid will "
           "actually give you. At Novo Nordisk I matured electrical scope across **37 concurrent capital "
           "projects** with 25 specialists, specification and purchasing aligned before site start — "
           "nothing left to be clarified during commissioning.", after=80)

    m.para("**Scope — a boundary with a name on it.** The Electrification & Automation package ends "
           "somewhere: at the civil contractor, at the panel builder, at the supplier's terminal strip, at "
           "the customer's own SCADA. I have owned those boundaries on **11 concurrent contracts** and "
           "across 37 projects, and the rule does not change: every interface has one owner, written down, "
           "before the first cable is pulled.", after=80)

    m.para("**Schedule — a list of decisions, not of dates.** A date only holds if the decisions behind it "
           "are taken: the FAT date depends on the drawing being released, which depends on the customer's "
           "comment, which depends on who is allowed to sign. I plan backwards from commissioning and the "
           "outage window, keep the critical path in the meeting where the decision is actually taken, and "
           "report the three dates that matter rather than the hundred that look fine.", after=80)

    m.para("**Cost to complete — a forecast you are willing to defend in writing.** A price is a promise; "
           "cost to complete is a position you take every month and are measured on. I have run a P&L "
           "since 2023, costed hours, materials, access and risk from the bottom up, and followed every "
           "project with after-calculation, gross margin per customer and monthly reporting in **SAP ERP** "
           "and **Power BI**.", after=80)

    m.para("**Risk and opportunity — two columns, one meeting.** Most registers are read for what can go "
           "wrong; the money is usually on the other side — a variation that was never priced, an outage "
           "window that can be moved, a scope the customer will need in any case. I have handled both "
           "under **AB 18** and **ABT 18** as contractor and as buyer, and the discipline is identical: "
           "dated, owned, and re-read before the gate.", after=80)

    m.para("**Commissioning — where the drawing meets the plant.** Commissioning is not a phase at the "
           "end; it is the test of whether the design was finished. I have commissioned electrical systems "
           "through **FAT/SAT** and **IQ/OQ/PQ** under GMP/FDA/EMA, closed 37 projects with **zero critical "
           "findings**, and run **HV switchgear** and **SCADA** in a plant that could not stop — where a "
           "protection setting is a document long before it is a relay.", after=80)

    m.para("**Framework — a promise about how you report.** A project management framework is not "
           "administration; it is the agreed way a gate is passed and a status is trusted. Having sat on "
           "the customer's side at Novo Nordisk, I know what a gate review is for: to stop a project from "
           "spending money on a premise that nobody has confirmed.", after=80)

    m.para("**Multidisciplinary — led by making the interface somebody's job.** Engineers, procurement, "
           "suppliers, commissioning and the customer's own organisation rarely disagree about the goal; "
           "they disagree about where the boundary runs. I have led **25 specialists** and teams of **5, "
           "12, 14 and 25**, with mandates written down, decisions logged, and the difficult conversation "
           "held early instead of escalated late.", after=80)

    m.para("**English is the project language; Danish is the site language.** I write and speak "
           "professional English for contracts, minutes and technical documentation, and Danish natively "
           "with electricians, suppliers and authorities — and I have worked where the specification was "
           "written in one language and the terminal strip labelled in another.", after=80)

    m.para("**Ballerup is ten minutes from my door.** Hybrid only works when presence is where the risk "
           "is: in the FAT hall, at the first energisation, in the meeting where the customer changes his "
           "mind. I live in Måløv, ten minutes from Ballerup, with a car and full availability through "
           "commissioning.", after=80)

    m.para("I would like to hear which projects are in maturation now, how the EA scope is cut against "
           "engineering and the suppliers, and where the last handover left something open — and I would "
           "be glad to be measured on the first commissioning I run.", after=60)
    m.meta("Yours sincerely", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- page 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFILE")
    m.para("Project manager and electrical engineer with 20+ years in electrical infrastructure — "
           "**Danish HV/LV authorised engineer (elautoriseret maskinmester, LV/MV/HV)** by trade, with full "
           "P&L responsibility since 2023. Has run **37 concurrent capital projects** of DKK 2–10m with "
           "**25 specialists**, delivered **11 concurrent contracts** from maturation to handover, and "
           "closed projects through **FAT/SAT** and **IQ/OQ/PQ** with **zero critical findings**. Schedule "
           "and cost in **SAP ERP** and **Power BI**; English professional, Danish native; Måløv.", after=80)

    m.section("PROJECT EXECUTION AND GOVERNANCE")
    for label, body in [
        ("Lifecycle, schedule and delivery",
         "37 capital projects and 11 contracts from maturation to final handover; programme planned "
         "backwards from commissioning and the outage window."),
        ("Cost, profitability and forecast",
         "Bottom-up costing, after-calculation per project and a monthly cost-to-complete to customer and line."),
        ("Risk, contract and framework",
         "Dated risk register read both ways; AB 18 and ABT 18 variations; gate evidence produced with the work."),
    ]:
        m.bullet(label, body, after=18)

    m.section("ELECTRICAL SCOPE — POWER DISTRIBUTION, CONTROL AND PROTECTION")
    for label, body in [
        ("HV, MV and LV distribution",
         "HV/LV authorisation (LV/MV/HV) and DS/HD 60364: switchgear, transformers, boards, earthing, selectivity."),
        ("Control, protection and commissioning",
         "HV switchgear and SCADA/SRO operated and fault-found in 24/7 plant; FAT/SAT, energisation and "
         "acceptance evidence."),
        ("Engineering, procurement and supplier interfaces",
         "EA boundary coordinated against civil, panel builders, telecom/SCADA and the customer: one owner per line."),
    ]:
        m.bullet(label, body, after=18)

    m.section("EXPERIENCE")
    jobs = [
        ("Owner / Technical Director",
         "ELOHVAC ApS · Copenhagen · May 2023–present",
         "5 electricians + 3 apprentices · full P&L · LV/MV/HV installations and service",
         [("Commercial ownership and delivery",
           "Every project quoted, planned and handed over under own P&L; after-calculation per job, gross "
           "margin per customer, service agreements with zero critical deviations."),
          ("Team, quality and safety",
           "Five electricians and three apprentices led daily; competence matrix, LOTO, risk assessment and "
           "health and safety at every site start-up.")]),
        ("Senior Commissioning Engineer / Project Manager, Electrical Systems",
         "Novo Nordisk A/S · Kalundborg/Bagsværd, Denmark · Nov 2022–Jul 2024",
         "37 capital projects · 25 specialists · GMP/FDA/EMA validated environment",
         [("Project execution on the customer side",
           "37 concurrent electrical capital projects of DKK 2–10m from maturation to handover; "
           "specification, procurement, engineering and site aligned, interfaces closed before "
           "installation."),
          ("Commissioning, acceptance and handover",
           "FAT/SAT and IQ/OQ/PQ with witness points, punch close-out and handover documentation under "
           "FDA/EMA requirements — zero critical findings.")]),
        ("Project and Workshop Manager",
         "Ventek-Air · Copenhagen · Jan 2022–Nov 2022",
         "14 employees · 11 concurrent contracts · DKK 2–10m per contract",
         [("Contracts from specification to handover",
           "11 concurrent contracts run with 14 people: subcontractor scope, deliveries and capacity "
           "controlled against the programme, cost and progress reported weekly.")]),
        ("Operations and Maintenance Manager",
         "Lynetten under Biofos · Copenhagen · Aug 2017–Jan 2022",
         "Critical plant in 24/7 operation · HV switchgear, SCADA, HVAC, pumps",
         [("Electrical plant, safety and uptime",
           "HV switchgear, SCADA/SRO, pumps and HVAC kept running in continuous operation; LOTO, APV, "
           "near-miss follow-up and 5S on workshop and store.")]),
        ("Electromechanical Technician / Production Team Leader",
         "ARJ Engineering · Tehran · Dec 2003–Mar 2010",
         "12 mechanics and technicians · machine workshop · industrial plant",
         [("Planning and output",
           "Daily allocation of 12 technicians against the week's plan, materials and tools controlled, "
           "output measured per person and per machine.")]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    # ---------------------------------------------------------------- page 3
    m.page_break()
    m.section("EDUCATION AND AUTHORISATION")
    m.edu("B.Tech, Technology Management and Mechanical Engineering",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7.6/12")
    m.edu("Electrical and Mechanical Engineering Design, Electrical Engineering (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("Danish HV/LV authorisation — elautoriseret maskinmester (LV/MV/HV)",
          "Danish Safety Technology Authority · May 2023")
    m.edu("Refrigeration and air-conditioning (AMU) · Lean practice: 5S, PDCA, A3, standard work",
          "Mercantec · 2021 · applied in project follow-up and operations")

    m.section("LANGUAGES, PRACTICALITIES AND REFERENCES")
    m.para("**English: professional**, written and spoken, for contracts, minutes, FAT/SAT protocols and "
           "technical documentation · **Danish: native** · Persian: native · **Based in Måløv, ten minutes "
           "from Ballerup**, available on site through commissioning and energisation · Full driving "
           "licence · Available at short notice · References on request.", after=70)

    m.models_table("THE FIRST 90 DAYS — PROJECTS, INTERFACES AND COMMISSIONING",
                   ("Period", "What happens, and how it is measured"), [
        ("Week 1–2",
         "Read the live project list, the contract summaries and the escalation log; walk the projects in "
         "execution and the ones in maturation; meet engineering, procurement, the commissioning leads and "
         "the customers who own the outage windows."),
        ("Day 30",
         "One page per project: scope boundary and interface owner, cost to complete against budget, the "
         "three dates that drive the programme, and the open risks and opportunities with a name and a "
         "date. Reporting aligned with the Siemens framework and the business unit's guidelines."),
        ("Day 60",
         "Gate readiness checked on the projects approaching a decision point; the interface list agreed "
         "with engineering and procurement in writing; supplier and subcontractor delivery performance "
         "measured, and the first variation priced before it is executed."),
        ("Day 90",
         "A commissioned scope delivered to the customer's acceptance, a forecast I have signed, and a "
         "project portfolio where every open item has an owner and a date — reported in the format the "
         "business unit already uses."),
    ], widths=(1500, 8830))

    m.section("A SUBSTATION PACKAGE IS WON OR LOST IN THE INTERFACES")
    m.para("The failure mode in substation automation is never the relay that was ordered; it is the "
           "interface that two competent companies each believed the other had closed. Civil works that "
           "arrive late, a telecom link nobody specified, a control-room protocol agreed verbally, a "
           "protection setting that arrives after the first energisation. The remedy is unglamorous: an "
           "interface list, one owner per line, agreed with the counterpart before the design is frozen — "
           "and reviewed at the gates, because interfaces move when the design moves.", after=80)

    m.section("THE OUTAGE WINDOW IS THE REAL SCHEDULE")
    m.para("On a grid project the calendar is not the constraint; the window in which the customer will "
           "let you take the plant out of service is. That window is booked months ahead, shared with "
           "other work, and lost if the FAT slips. So the FAT is the milestone that matters, the drawing "
           "release is what protects the FAT, and the customer's comment round is what protects the "
           "drawing. Planning backwards from the window turns a list of dates into a sequence of "
           "decisions — and that is the only kind of schedule that survives contact with a live grid.",
           after=80)

    m.section("HANDOVER IS A DOCUMENT, NOT A MEETING")
    m.para("A project is handed over when the customer can operate, maintain and prove it without calling "
           "the project team: as-built drawings, protection settings, test protocols, spare-part lists, "
           "training and the punch list formally closed. I have produced that file under GMP/FDA/EMA, "
           "where the evidence is inspected, and I have closed 37 projects with zero critical findings — "
           "not because the documentation was written at the end, but because it was written with the "
           "work.", after=80)

    m.section("WHAT I WOULD BE MEASURED ON IN THE FIRST YEAR")
    m.para("Three numbers: projects delivered inside the committed window, cost to complete within the "
           "forecast I signed, and handovers accepted without a re-open. A fourth matters as much and is "
           "harder to put in a report: that the engineers, the suppliers and the customer's operations "
           "team would take the next project with me again. That is how a project organisation grows, and "
           "it is the reason I am applying to this one rather than to a role with a smaller scope.",
           after=60)

    # ---------------------------------------------------------------- page 4
    m.page_break()
    m.models_table("WHAT THE ROLE REQUIRES — WHAT I HAVE DELIVERED",
                   ("Requirement in the posting", "Evidence"), [
        ("Execute multiple projects from maturation and planning through execution, commissioning and final handover",
         "37 concurrent capital projects of DKK 2–10m and 11 concurrent contracts run end to end."),
        ("Ownership of project schedule, cost, profitability, quality and contractual deliverables",
         "Full P&L since 2023; after-calculation and monthly cost-to-complete; zero critical findings at "
         "handover."),
        ("Coordinate the substation automation, control and protection scope across engineering, procurement, customers and suppliers",
         "The EA package boundary owned on 11 contracts and 37 projects; one owner per interface, in writing."),
        ("Identify and manage project risks and opportunities throughout the lifecycle",
         "Dated, owned risk register read for both sides; variations priced before execution under AB 18."),
        ("Ensure projects are executed and reported in accordance with the project management framework and business unit guidelines",
         "Gate documentation and acceptance evidence produced with the work; reporting in SAP ERP, Power BI "
         "and the unit's format."),
        ("Experience in project management within power distribution, automation, protection, electrical infrastructure or relevant technical projects",
         "20+ years in electrical infrastructure: HV/MV/LV, HV switchgear, SCADA, 24/7 plant, 37 projects, "
         "11 contracts."),
        ("A technical background, preferably within electrical engineering, automation or a related field",
         "Danish HV/LV authorised engineer (maskinmester, LV/MV/HV); B.Tech plus an electrical engineering "
         "degree."),
        ("Strong commercial understanding and the ability to manage schedules, costs and project risks",
         "Owner of a contracting business since 2023: quotes, margin per job type, supplier terms, variations."),
        ("The ability to lead multidisciplinary teams, coordinate stakeholders and make sound decisions",
         "25 specialists across 37 projects and teams of 5, 12, 14 and 25; mandates written, decisions logged."),
        ("A structured, proactive and independent way of working with resilience in a fast-paced international environment",
         "Deadlines kept across a validated pharma build, 24/7 plant and an own business; Danish and "
         "international settings."),
        ("Professional proficiency in English; Danish is an advantage",
         "English professional, written and spoken, for contracts, minutes and FAT/SAT protocols; Danish "
         "native."),
        ("Work closely with customers, engineers, suppliers and other stakeholders to deliver complex projects",
         "Two years on the customer side at Novo Nordisk: specification, procurement, engineering and supplier "
         "quality aligned."),
        ("A strong technical foundation, a learning mindset and ambition to develop into the role",
         "Took the HV/LV authorisation in 2023 and the B.Tech in 2022 while running operations."),
    ], widths=(2750, 7580))

    m.section("SIEMENS IS REBUILDING THE GRID THIS COUNTRY WILL RUN ON")
    m.para("The Danish power grid is being expanded and modernised at a pace set by electrification and "
           "digitalisation, and every substation in that programme is a promise about capacity that "
           "somebody has to keep. That "
           "is the part of the work I want: not a single product, but the delivery of a scope that other "
           "people's supply depends on. Siemens builds that with a framework, a portfolio and a supply "
           "chain — and the project manager's job is to make the framework hold on the specific project, "
           "with the specific customer, in the specific window.", after=80)

    return m.save(path, title="Project Manager, Electrification & Automation — Siemens Ballerup")


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Siemens_ProjectManagerElectrificationAutomation.docx')
    build(out)
    print(out)
