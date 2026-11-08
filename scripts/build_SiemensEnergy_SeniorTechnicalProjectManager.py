# -*- coding: utf-8 -*-
"""Siemens Energy A/S — Senior Technical Project Manager, Grid Technologies / Substations
(Job ID 305750), Ballerup or Vejle. Deadline 2026-11-10, ongoing selection.

English posting → English deliverable (en-GB): application p1, CV p2, education + 90 days +
sections p3, 16-row requirement matrix p4.

STYLE CHOICE (master/STILREGISTER.md, policy of 04.11.2026; approved by scripts/style_guard.py,
3/3 changes against #184):
  register       = RÅDGIVENDE — decision basis, interfaces, deliverables, stakeholders. Not the
                   technical-drift register of #184 (2Refurb), the engineering-precise of #182
                   (Siemens A/S) or the commercial of #181 (Bravida).
  opening device = F (KONSEKVENSEN) — the concrete loss when the interface fails, first use.
                   The last five used J, I, G, B and A.
  structure      = INTERFACES — the role is advertised as an interface job ("thorough understanding
                   of interfaces and design flow between the sub-systems"), so page 1 owns one
                   interface per paragraph: single-line diagram, layout and 3D, drawings, civil,
                   procurement, supplier QA, installation and commissioning, the site under BEK 1608,
                   design flow, cyber security, bid-to-warranty, and the two locations.
  cadence        = a rule stated as a sentence, then the evidence with a number — advisory, not
                   workshop-floor and not board-room.

Facts: nothing claims substation design authorship, GIS/AIS design, compensation systems or a formal
arbejdsleder appointment. AIS/GIS/compensation/oil-filled appear as the substation scope to be
coordinated; the evidence is HV/MV/LV installation and operation, HV switchgear, cable systems and
terminations, auxiliary systems, commissioning and the BEK 1608 work-procedure discipline.

Policy: master/README.md — job first, candidate only as evidence, no hedges.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Technical project management · HV substations, interfaces and commissioning'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4 November 2026")
    m.meta("Siemens Energy A/S · Grid Technologies, Substations · Senior Technical Project Manager · "
           "Job ID 305750 · Ballerup / Vejle")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Application: Senior Technical Project Manager — Substations", bold=True, color='1A1A1A')
    m.para("To the Substations team, Grid Technologies, Siemens Energy", after=70)

    # ---------------------------------------------------------------- page 1
    m.para("An onshore substation is rarely late because the transformer was late. It is late because the "
           "single-line diagram moved after the layout was frozen, or because a cable termination nobody had "
           "specified arrived with the switchgear. The date is lost in the interfaces, months before it shows "
           "in the schedule — and this role exists to own them.", after=80)

    m.para("**The single-line diagram — one drawing that decides all the others.** The SLD is the contract "
           "between the electrical design and the physical plant: what is connected, at which voltage, "
           "through which switchgear, in which earthing arrangement. Freeze it and the layout, the civil "
           "design, the cable routes and the procurement list all follow; let it drift and every one of "
           "them drifts with it. On **37 capital projects** a change after release was priced, dated and approved "
           "— never absorbed.", after=80)

    m.para("**Layout and the 3D team — space is the constraint nobody can negotiate.** A substation layout is "
           "a sequence of clearances: phase spacing, safety distances, access for a truck and a crane, room "
           "to pull a cable and to change a component. I have laid out electrical rooms and plant space where "
           "nothing could be moved afterwards, with the trades who build what the model shows.", after=80)

    m.para("**Electrotechnical drawings — the drawing is a promise with a revision.** Every drawing in scope "
           "carries a date, a revision and a reason, and the set that goes to site is the set that comes back as "
           "as-built. I have produced handover documentation as part of the work, under **DS/HD 60364** on "
           "installations and under GMP/FDA/EMA where the file itself is inspected.", after=80)

    m.para("**Civil works — your partner's dates are your dates.** Civil input moves more substation "
           "programmes than any electrical detail: foundations for switchgear, trenches and ducts for "
           "**HV and MV cable systems**, access roads, earthing. Coordinates, loads and penetration "
           "openings go to the civil partner as a frozen input with a date, and come back as a construction "
           "sequence the electrical scope can live with.", after=80)

    m.para("**Procurement — the specification is the contract.** Technical procurement of substation "
           "materials is a specification exercise before it is a purchasing exercise: technical data, type "
           "tests, terminal allocations, drawings, documentation and delivery. In my own business I specify, buy "
           "and follow up on every package; under **AB 18** and **ABT 18** I have negotiated as buyer and as "
           "supplier.", after=80)

    m.para("**Supplier QA — read the deliverable, not the promise.** Supplier deliverables are checked "
           "against the specification, not against the supplier's own template: drawings, calculations, "
           "test reports, FAT documentation and interface lists. I have run **FAT/SAT** and **IQ/OQ/PQ** acceptance "
           "with witness points under GMP/FDA/EMA, closed 37 projects with **zero critical findings** — and "
           "refused acceptance when the evidence was missing.", after=80)

    m.para("**Installation and commissioning — planned while the design is still open.** Commissioning input "
           "belongs at the design stage: which tests prove the installation, which protection settings must "
           "be in place before first energisation, which outage window the customer can actually give. I "
           "have planned and run energisation in a **24/7 plant**, where the switching order, the LOTO and "
           "the hold point are the only thing between a plan and an accident.", after=80)

    m.para("**The site under BEK 1608 — where the procedure is planned before the work starts.** The Danish "
           "driftsbekendtgørelse sets the roles: the work procedure is planned by an **arbejdsleder**, "
           "released through a koblingsleder and led on site by a holdleder. I work inside that structure as the "
           "Danish HV/LV authorised person who writes the risk assessment and the instruction, then stands on "
           "the site while the work is done.", after=80)

    m.para("**Design flow — broken into steps somebody can plan.** Design is plannable when it is cut into "
           "steps with an owner and a checkable output: SLD → layout → civil → procurement → drawings → "
           "FAT → site → commissioning → as-built. I have run that breakdown with **25 specialists** across 37 "
           "projects, with a RACI that said who decided what.", after=80)

    m.para("**Cyber security — the basics belong in the project, not in IT afterwards.** A substation is a "
           "control system before it is a building: who may reach which network, which changes are "
           "documented, and what the customer receives at handover. Access control, PDS and change "
           "documentation are project deliverables, not IT concerns after commissioning.", after=80)

    m.para("**From bidding to the end of warranty — the bid has to contain what execution can deliver.** I have "
           "quoted and delivered under own P&L since 2023, closed projects with **1- and 5-year reviews** "
           "ahead of them, and worked two years on the customer's side at Novo Nordisk.", after=80)

    m.para("I live in Måløv, ten minutes from Ballerup, and travel to Vejle or a site when the project needs "
           "it. I would like to hear which substations are in bidding now, how the technical scope is "
           "divided, and where the civil-electrical interface caused the last delay — and I would be glad to "
           "be measured on the first design freeze I own.", after=30)
    m.meta("Yours sincerely", after=0)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- page 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFILE")
    m.para("Technical project manager in electrical infrastructure with 20+ years on HV, MV and LV systems — "
           "**Danish HV/LV authorised engineer (elautoriseret maskinmester, LV/MV/HV)**, electrical "
           "engineering at EQF 6 plus a B.Tech, and full P&L responsibility since 2023. Has run **37 "
           "capital projects** of DKK 2–10m with **25 specialists**, coordinated engineering, procurement, "
           "suppliers and site through **FAT/SAT** and commissioning, and closed them with **zero critical "
           "findings**. Works to **BEK 1608**, **DS/HD 60364** and **AB 18/ABT 18**; reports in SAP ERP and "
           "Power BI. English professional, Danish native.", after=80)

    m.section("ELECTROTECHNICAL SCOPE AND DESIGN INTERFACES")
    for label, body in [
        ("Single-line diagrams, layouts and drawings",
         "Electrical scope defined and documented before installation: distributions, switchgear, cable "
         "routes and clearances, drawing sets with revisions, as-built at handover."),
        ("Substation sub-systems",
         "HV and MV switchgear, transformers, HV/MV cable systems with terminations, auxiliary systems (UPS, "
         "emergency lighting, access control/PDS) and earthing — installed, tested, maintained."),
    ]:
        m.bullet(label, body, after=20)

    m.section("INSTALLATION, COMMISSIONING AND SITE SAFETY")
    for label, body in [
        ("Commissioning and energisation",
         "FAT/SAT at works and on site, first energisation planned with the customer, protection proven "
         "before load, IQ/OQ/PQ with witness points, punch close-out and handover file."),
        ("Work procedures under BEK 1608",
         "Work procedure planned, risk-assessed and instructed before the work starts; LOTO, spændingsløs "
         "verification and hold points; Danish HV/LV authorisation since May 2023."),
    ]:
        m.bullet(label, body, after=20)

    m.section("PROCUREMENT, SUPPLIER QA AND COST")
    for label, body in [
        ("Technical procurement, supplier QA and contract",
         "Specification, technical data and delivery dates per package; deliverables checked against "
         "specification with acceptance refused without evidence; bottom-up costing, monthly "
         "cost-to-complete, variations under AB 18/ABT 18."),
    ]:
        m.bullet(label, body, after=20)

    m.section("EXPERIENCE")
    jobs = [
        ("Owner / Technical Director",
         "ELOHVAC ApS · Copenhagen · May 2023–present",
         "5 electricians + 3 apprentices · full P&L · LV/MV/HV installations, panels and service",
         [("Technical scope and delivery",
           "Every installation specified, planned and handed over under own P&L, with drawings, acceptance "
           "criteria and handover documentation; zero critical deviations in the service agreements."),
          ("Team and site safety",
           "Five electricians and three apprentices led daily; work procedures, LOTO, risk assessment and "
           "instruction at every site start-up.")]),
        ("Senior Commissioning Engineer / Project Manager, Electrical Systems",
         "Novo Nordisk A/S · Kalundborg/Bagsværd, Denmark · Nov 2022–Jul 2024",
         "37 capital projects · 25 specialists · GMP/FDA/EMA validated environment",
         [("Engineering, procurement and site interfaces",
           "37 concurrent electrical capital projects of DKK 2–10m: specification, purchasing, engineering "
           "and site aligned, interfaces closed before installation."),
          ("Testing, acceptance and handover",
           "FAT/SAT and IQ/OQ/PQ with witness points, punch close-out and handover documentation under "
           "FDA/EMA requirements — zero critical findings.")]),
        ("Project and Workshop Manager",
         "Ventek-Air · Copenhagen · Jan 2022–Nov 2022",
         "14 employees · 11 concurrent contracts · DKK 2–10m per contract",
         [("Contracts and supplier coordination",
           "11 concurrent contracts with 14 people: subcontractor scope, deliveries and capacity controlled "
           "against the programme, acceptance documented at handover.")]),
        ("Operations and Maintenance Manager",
         "Lynetten under Biofos · Copenhagen · Aug 2017–Jan 2022",
         "Critical plant in 24/7 operation · HV switchgear, SCADA, pumps, HVAC",
         [("HV plant and switching discipline",
           "HV switchgear, SCADA/SRO, pumps and HVAC in continuous operation; switching orders, LOTO and "
           "risk assessment on every intervention.")]),
        ("Electromechanical Technician / Production Team Leader",
         "ARJ Engineering · Tehran · Dec 2003–Mar 2010",
         "12 mechanics and technicians · machine workshop · industrial plant",
         [("Diagnosis and repair",
           "Fault diagnosis and repair of industrial electrical and mechanical plant with root cause "
           "analysis; 12 technicians planned and measured daily.")]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=16)

    # ---------------------------------------------------------------- page 3
    m.page_break()
    m.section("EDUCATION AND AUTHORISATION")
    m.edu("Electrical and Mechanical Engineering Design, Electrical Engineering (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("B.Tech, Technology Management and Mechanical Engineering",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7.6/12")
    m.edu("Danish HV/LV authorisation — elautoriseret maskinmester (LV/MV/HV)",
          "Danish Safety Technology Authority · May 2023")
    m.edu("Lean practice: 5S, PDCA, A3, standard work · Refrigeration and air-conditioning (AMU)",
          "Mercantec · 2021 · applied in commissioning and project follow-up")

    m.section("LANGUAGES, PRACTICALITIES AND REFERENCES")
    m.para("**English: professional**, written and spoken, for specifications, drawings, FAT/SAT protocols "
           "and management reporting · **Danish: native** · Persian: native · **Based in Måløv**, ten "
           "minutes from Ballerup and available for Vejle and site work through commissioning · Full "
           "driving licence · Available at short notice · References on request.", after=70)

    m.models_table("THE FIRST 90 DAYS — INTERFACES, SCOPE AND SITE",
                   ("Period", "What happens, and how it is measured"), [
        ("Week 1–2",
         "Read the live substation portfolio and the bid pipeline; walk the drawings of two projects in "
         "execution; meet the 3D team, the civil partner, procurement and the site organisation; map the "
         "interface list as it exists today."),
        ("Day 30",
         "One interface register per project: SLD status, layout freeze date, civil inputs, procurement "
         "packages, supplier deliverables and commissioning requirements — each with an owner and a date, "
         "reported in the project management department's format."),
        ("Day 60",
         "Design flow broken into plannable steps per project; the civil-electrical interface frozen in "
         "writing; supplier deliverables reviewed against specification; the first bid supported with a "
         "technical scope that execution can deliver."),
        ("Day 90",
         "A design freeze I own, a commissioning plan written before the installation is complete, and a "
         "supplier QA trail where every deliverable has been read and answered — with the interfaces "
         "visible in the plan, not discovered in the schedule."),
    ], widths=(1500, 8830))

    m.section("AN INTERFACE THAT IS NOBODY'S JOB IS NOBODY'S DATE")
    m.para("Most substation delays are not technical failures; they are ownership failures. The civil "
           "foundation and the earthing design touch each other, the 3D model and the switchgear supplier "
           "touch each other, and the commissioning plan touches all of them. Where two organisations are "
           "competent and neither has the boundary in writing, the boundary is where the programme breaks. "
           "One owner, one line in the register, one date — agreed while everybody is still friendly.",
           after=80)

    m.section("THE DESIGN FREEZE IS THE CHEAPEST DECISION IN THE PROJECT")
    m.para("Every change is cheap in the week before the freeze and expensive in the week after the "
           "foundation is poured. That is why the technical project manager's value is measured in what did "
           "not have to change: a single-line diagram reviewed with operations before it is issued, a layout "
           "with the maintenance access actually drawn, a termination specified with the cable rather than "
           "after it. I have closed 37 projects with zero critical findings by taking those decisions early "
           "and writing them down.", after=80)

    m.section("TWO SITES, ONE ENGINEERING STANDARD")
    m.para("Ballerup and Vejle only behave as one technical organisation if the drawings, the interface "
           "lists and the acceptance criteria are the same in both. That is a documentation discipline "
           "before it is a management decision: one template for the drawing set, one register for the "
           "interfaces, one place where the decisions are logged — so a specialist in Vejle can pick up a "
           "project from Ballerup without a handover meeting.", after=80)

    m.section("A BID IS AN ENGINEERING PROMISE")
    m.para("The same discipline covers an onshore substation, an offshore wind connection, a Power-to-X "
           "plant and an energy transmission project: the technical project manager's contribution to a bid "
           "is not a price but a statement about what can be built, tested and handed over within the hours "
           "and the assumptions in the offer — and what the service handover requires once the warranty is "
           "concluded. "
           "Where that statement is thin, the risk appears later as a variation, a rework or a warranty "
           "case. I have quoted from my own P&L since 2023 and been on the customer's side of a contract at "
           "Novo Nordisk — so I write the technical scope in a bid the way the customer will read it.",
           after=80)

    # ---------------------------------------------------------------- page 4
    m.page_break()
    m.models_table("WHAT THE ROLE REQUIRES — WHAT I HAVE DELIVERED",
                   ("Requirement in the posting", "Evidence"), [
        ("Coordinate overall single-line diagram for the substations and overall substation layouts together with our 3D team",
         "Electrical scope defined on drawings with revisions and clearances: distributions, switchgear, "
         "cable routes and plant space in operating facilities."),
        ("Coordinate all the electrotechnical drawings related to the scope",
         "Drawing sets, as-built and handover documentation produced as part of the work across 37 capital "
         "projects and 11 contracts; DS/HD 60364 as the frame."),
        ("Give input to and plan installation and commissioning phase",
         "Commissioning planned from the design stage: FAT/SAT, protection proven before first energisation, "
         "outage windows agreed with the customer, punch close-out."),
        ("Coordinate technical input and give support to Procurement team within the selection and onboarding process of suppliers",
         "Supplier selection on capability and technical data; onboarding through specification, drawings and "
         "documentation requirements; performance measured afterwards."),
        ("Work proactively in close collaboration with overall project managers as well as other technical project managers and specialists",
         "37 projects run with project managers, engineering, procurement and 25 specialists; RACI, "
         "escalation route and weekly decision log."),
        ("Coordinate the technical procurement of materials for the substation",
         "Technical procurement of switchgear, cable systems, terminations and auxiliary equipment: data, "
         "type tests, drawings, documentation and delivery dates."),
        ("Execute thorough QA of suppliers' project deliverables",
         "Deliverables read against specification — drawings, calculations, test reports, FAT documentation "
         "— with acceptance refused when evidence was missing; zero critical findings."),
        ("Coordinate the civil design input with our civil partners",
         "Coordinates, loads, trenches, ducts and penetration openings issued as frozen input with a date; "
         "construction sequence agreed with the trades that build it."),
        ("Degree in Electrical Engineering (or equivalent) with 5+ years of experience in high voltage substation design and engineering",
         "Electrical engineering degree at EQF 6 plus B.Tech and Danish HV/LV authorisation; 20+ years on "
         "HV, MV and LV systems, 37 capital projects, 11 contracts."),
        ("Broad knowledge within subsystems: Air Insulated Switchgear, Gas Insulated Switchgear, Oil filled components, compensation systems, HV and MV cable systems and their terminations, Auxiliary systems, civil works",
         "HV and MV switchgear, transformers, HV/MV cable systems and terminations, auxiliary systems (UPS, "
         "emergency lighting, access control/PDS) and earthing — installed, tested, maintained."),
        ("Proven experience under rules according to the Danish legislation 1608, and HV substation field experience as an Arbejdsleder or similar, understanding the practicalities on site",
         "Work procedures under BEK 1608: risk assessment and instruction written before the work, LOTO and "
         "spændingsløs verification, hold points; HV plant in 24/7 operation; Danish HV/LV authorisation."),
        ("Basic understanding of cyber security in projects",
         "OT discipline from operating plant: access control and PDS as project deliverables, network and "
         "port changes documented, handover package includes who may reach what."),
        ("Thorough understanding of interfaces and design flow between the sub-systems, and the capability to break design work down into appropriate steps for planning",
         "Design flow cut into steps with owner, input and checkable output — SLD, layout, civil, "
         "procurement, drawings, FAT, site, commissioning, as-built."),
        ("Project and customer focused with strong written and oral communication skills for technical and non-technical colleagues and stakeholders",
         "Two years on the customer side at Novo Nordisk; reporting to management and to the client in SAP ERP "
         "and Power BI; English, Danish and Persian in technical and commercial settings."),
        ("Proven supplier management skills",
         "Suppliers and subcontractors specified, negotiated under AB 18/ABT 18 as buyer and as supplier, and "
         "measured on delivery, quality and response time."),
        ("Fluent English written and spoken; Danish is considered an advantage",
         "English professional, written and spoken, for specifications, protocols and management reporting; "
         "Danish native, with authorities, suppliers and electricians."),
    ], widths=(3600, 6746))

    return m.save(path, title="Senior Technical Project Manager, Substations — Siemens Energy")


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_SiemensEnergy_SeniorTechnicalProjectManager.docx')
    build(out)
    print(out)
