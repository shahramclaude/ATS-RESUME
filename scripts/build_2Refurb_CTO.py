# -*- coding: utf-8 -*-
"""2Refurb — CTO, Silkeborg (posted on LinkedIn; rolling hiring, hire when the match is found).

English posting → English deliverable (en-GB): application p1, CV p2, education + 90 days +
sections p3, 16-row requirement matrix p4.

STYLE CHOICE (master/STILREGISTER.md, policy of 04.11.2026; approved by scripts/style_guard.py:
3/3 changes against #182):
  register       = TEKNISK-DRIFTSNÆR — the test bench and the night shift, not the boardroom.
                   Deliberately not the engineering-precise register of #182 (Siemens) nor the
                   commercial one of #181 (Bravida).
  opening device = J (BREVET) — the letter opens on 2Refurb's own sentence ("we sell the
                   engineering judgement behind them") and answers it directly, without a frame.
                   First use of J; I (theses) went out with #182, G (question) with #181, B is banned.
  structure      = KOMPONENTENS VEJ — one component followed through the company's own process:
                   intake → failure modes → test and inspection → quality in production → warranty
                   → sales and procurement → R&D and digital → certification → the electric area →
                   the management team and the two sites. A new structure, not the glossary (#182),
                   the timeline (#181), the decision chain (#179) or the before/after (#178).
  cadence        = a short operational statement, then one concrete example with a number —
                   flatter and more workshop-like than the Siemens letter.

Wind industry: the posting calls it a strong plus. Nothing here claims wind-sector employment or
turbine-site work; the evidence is electro-mechanical and electrical component work (pumps, motors,
switchgear, panels, control, SCADA) and the testing/acceptance discipline around it.

Policy: master/README.md — job first, candidate only as evidence, no hedges.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Technical leadership · Electrical and electro-mechanical engineering, testing and standards'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4 November 2026")
    m.meta("2Refurb · CTO · Silkeborg, Denmark (and Council Bluffs, Iowa)")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Application: CTO — the technical foundation behind the engineering judgement",
           bold=True, color='1A1A1A')
    m.para("To 2Refurb and Martin Frølich Olesen", after=70)

    # ---------------------------------------------------------------- page 1
    m.para("You write that 2Refurb does not sell parts off a shelf, but the engineering judgement behind "
           "them. That sentence is the job: judgement only becomes a product when it is written down, "
           "testable, and repeatable by the technician who opens the next unit in Silkeborg or Council "
           "Bluffs. Below is how I would build that foundation — following one component through your "
           "own process.", after=80)

    m.para("**Intake — the condition of the unit sets the scope.** Everything promised later is decided when "
           "the part is opened: what it is, what it failed from, and whether it is worth the hours. I have "
           "spent twenty years on that decision in electrical and electro-mechanical plant — pumps, motors, "
           "switchgear, control panels, SCADA — inspecting, fault-finding and writing down why a part was "
           "kept, repaired or replaced.", after=80)

    m.para("**Failure modes — a library, not a memory.** Component types, failure modes, refurbishment "
           "methods and acceptance criteria belong in something a new technician can use on day one. I "
           "have worked to **A3, 5-why and Ishikawa** in a validated production environment where an "
           "undocumented deviation is a finding, and built the standard work that kept **24/7 plant** "
           "running at Lynetten.", after=80)

    m.para("**Test and inspection — the protocol is the product.** A refurbished part is only as good as the "
           "test that releases it: what is measured, with which instrument, at which load, against which "
           "limit, recorded where. I have witnessed and signed **FAT/SAT** and **IQ/OQ/PQ** under "
           "GMP/FDA/EMA — protocols that do not accept \"it works\" as evidence — and I have been the one "
           "who refuses acceptance when the evidence is not there.", after=80)

    m.para("**Quality in production — caught at the station, not at the end.** Built-in quality means the "
           "measurement happens while the unit is still open: first-off checks, hold points, and a "
           "technician who is allowed to stop a job. Across **37 concurrent capital projects** the "
           "deviations we discussed were the ones caught early — **zero critical findings at handover** is "
           "a habit, not a final inspection.", after=80)

    m.para("**Warranty and complaints — the failure is data.** A claim is an engineering question with a "
           "date on it: what failed, how it failed, whether it is the component, the method or the "
           "application — and whether the standard has to change. Root cause with 5-why and Ishikawa, the "
           "corrective action written into the method, and an answer the customer's engineers can check "
           "themselves.", after=80)

    m.para("**Sales, operations and procurement — feasibility before the quote leaves the building.** The "
           "engineering input behind a commercial decision is a yes, a no or a yes-if: can this unit be "
           "brought back to specification, what does the test require, what must the customer documentation "
           "say. I have quoted, costed and delivered from my own P&L since 2023, so the judgement arrives "
           "with the number attached.", after=80)

    m.para("**R&D, improvement and digital — good engineering has to scale.** Which component types fail, at "
           "what hours, from what cause, at what cost: that only becomes knowledge when it sits in one "
           "place. I have built the reporting layer myself — **SAP ERP** for orders and cost, **Power BI** "
           "and **Python** for dashboards and quote calculation — and measured **above 40 % productivity "
           "gain** from letting the routine work flow through the system instead of through me.", after=80)

    m.para("**Certification and documentation — the licence to keep selling.** A certificate is what allows "
           "the part to go back into a turbine and the company to keep quoting. Danish **HV/LV** "
           "authorisation, **DS/HD 60364** and the SB guidance are my working frame; the documentation "
           "discipline comes from pharma, where the file itself is inspected.", after=80)

    m.para("**The electric area — where I strengthen you.** Electrical engineering at EQF 6, twenty years of "
           "electrical and electro-mechanical work, and a Danish HV/LV authorisation: **switchgear, motors, "
           "control systems, panels, SCADA**, and instruments in hand. Wind turbine components — "
           "**converters, motors, switchgear, sensors, control electronics** — are electro-mechanical "
           "assemblies, and testing, judging and documenting them is the discipline I have practised at "
           "component and at plant level.", after=80)

    m.para("**The management team — and two sites.** A CTO in a company this size sits in the management team "
           "with a sales team relying on his judgement, and works between Silkeborg and Council Bluffs. I "
           "have run a business with full P&L, been part of the management team of a 24/7-plant operation, "
           "and worked in English, Danish and Persian across countries. I live in Måløv and travel where the "
           "role requires it.", after=80)

    m.para("I would like to hear which component families cause you the most warranty work today, where the "
           "test protocols are thinnest, and how far the digital systems reach into the workshop — and I "
           "would be glad to bring the first standard with me.", after=60)
    m.meta("Yours sincerely", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- page 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFILE")
    m.para("Technical leader in electrical and electro-mechanical engineering with 20+ years at the plant "
           "and the test bench — **Danish HV/LV authorised engineer (elautoriseret maskinmester, "
           "LV/MV/HV)**, electrical engineering at EQF 6 plus a B.Tech, and full P&L responsibility since "
           "2023. Has written standards, test and acceptance criteria into daily work across **37 capital "
           "projects** with **25 specialists**, closed them with **zero critical findings**, driven root "
           "cause with **A3, 5-why and Ishikawa**, and built the digital layer in **SAP ERP, Power BI and "
           "Python** on **above 40 % productivity gain**. English professional, Danish native.", after=80)

    m.section("TECHNICAL STANDARDS, TEST AND QUALITY")
    for label, body in [
        ("Standards and acceptance criteria",
         "Methods, work instructions and acceptance tests written down: what passes, what is rejected, who "
         "signs — applied to service agreements and to 37 capital projects."),
        ("Testing and inspection",
         "FAT/SAT witnessed at works and on site, IQ/OQ/PQ with witness points under GMP/FDA/EMA, protection "
         "proven before load, acceptance refused without evidence."),
        ("Root cause and improvement",
         "Fault diagnosis of pumps, motors, switchgear, panels and SCADA with 5-why, Ishikawa and A3; "
         "corrective action written into the method; 5S, standard work and PDCA in 24/7 operation."),
    ]:
        m.bullet(label, body, after=20)

    m.section("ELECTRICAL, ELECTRO-MECHANICAL AND DIGITAL")
    for label, body in [
        ("HV, MV and LV",
         "HV/LV authorisation (LV/MV/HV) and DS/HD 60364/SB: switchgear, transformers, boards, cable "
         "systems, earthing, selectivity."),
        ("Control, instrumentation and rotating equipment",
         "Control panels, interlocks, sensors and SCADA/SRO operated, tested and fault-found; pumps, motors, "
         "fans and HVAC diagnosed, repaired or replaced."),
        ("Data, digital and commercial",
         "SAP ERP for orders, assets and cost; Power BI and Python (incl. AI tooling) for quoting, KPIs and "
         "checklists — above 40 % productivity gain; feasibility and specification before the price."),
    ]:
        m.bullet(label, body, after=20)

    m.section("EXPERIENCE")
    jobs = [
        ("Owner / Technical Director",
         "ELOHVAC ApS · Copenhagen · May 2023–present",
         "5 electricians + 3 apprentices · full P&L · LV/MV/HV installations, panels and service",
         [("Technical standards and delivery",
           "Every job specified, quoted and handed over under own P&L; methods and acceptance criteria "
           "written down, after-calculation per job, zero critical deviations in service agreements."),
          ("Team and safety",
           "Five electricians and three apprentices led daily; competence matrix, LOTO, risk assessment and "
           "health and safety at every site start-up.")]),
        ("Senior Commissioning Engineer / Project Manager, Electrical Systems",
         "Novo Nordisk A/S · Kalundborg/Bagsværd, Denmark · Nov 2022–Jul 2024",
         "37 capital projects · 25 specialists · GMP/FDA/EMA validated environment",
         [("Testing, acceptance and root cause",
           "FAT/SAT and IQ/OQ/PQ with witness points across 37 concurrent electrical capital projects; A3 and "
           "Ishikawa on deviations; zero critical findings at handover."),
          ("Technical input and improvement",
           "Specification, purchasing, engineering and site aligned; 40 % energy-cost reduction through a "
           "PDCA programme; monthly reporting in SAP ERP.")]),
        ("Project and Workshop Manager",
         "Ventek-Air · Copenhagen · Jan 2022–Nov 2022",
         "14 employees · 11 concurrent contracts · DKK 2–10m per contract",
         [("Workshop and handover",
           "14-person workshop and 11 concurrent contracts from specification to formal handover; "
           "subcontractor scope and acceptance documentation at daily board meetings.")]),
        ("Operations and Maintenance Manager",
         "Lynetten under Biofos · Copenhagen · Aug 2017–Jan 2022",
         "Critical plant in 24/7 operation · pumps, motors, HV switchgear, SCADA",
         [("Plant and failure modes",
           "Pumps, motors, HVAC, HV switchgear and SCADA kept running; failure modes recorded and preventive "
           "work planned from them, with 5S on workshop and store.")]),
        ("Electromechanical Technician / Production Team Leader",
         "ARJ Engineering · Tehran · Dec 2003–Mar 2010",
         "12 mechanics and technicians · machine workshop · industrial plant",
         [("Diagnosis and repair",
           "Fault diagnosis and repair of industrial electrical and mechanical plant with root cause "
           "analysis and corrective action; 12 technicians planned and measured daily.")]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=20)

    # ---------------------------------------------------------------- page 3
    m.page_break()
    m.section("EDUCATION AND AUTHORISATION")
    m.edu("Electrical and Mechanical Engineering Design, Electrical Engineering (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("B.Tech, Technology Management and Mechanical Engineering",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7.6/12")
    m.edu("Danish HV/LV authorisation — elautoriseret maskinmester (LV/MV/HV)",
          "Danish Safety Technology Authority · May 2023")
    m.edu("Lean practice: 5S, PDCA, VSM, A3, Kaizen · Refrigeration and air-conditioning (AMU)",
          "Mercantec · 2021 · applied in operations, testing and project follow-up")

    m.section("LANGUAGES, PRACTICALITIES AND REFERENCES")
    m.para("**English: professional**, written and spoken, for specifications, test protocols, customer "
           "documentation and management reporting · **Danish: native** · Persian: native · **Based in "
           "Måløv**, willing to travel to Silkeborg, Council Bluffs and customer sites · Full driving "
           "licence · Available at short notice · References on request.", after=70)

    m.models_table("THE FIRST 90 DAYS — STANDARDS, TEST AND DIGITAL",
                   ("Period", "What happens, and how it is measured"), [
        ("Week 1–2",
         "Read the component portfolio, the current test and inspection protocols, the warranty log and the "
         "certification file; spend the days at the bench and in the workshop, not in the office."),
        ("Day 30",
         "A map of component families against failure modes, refurbishment method, acceptance criteria and "
         "warranty history — with the gaps marked; the three protocols that cause most rework identified."),
        ("Day 60",
         "Revised test and inspection protocols issued for the highest-volume families; hold points and "
         "first-off checks in production; root-cause template in use for every warranty claim."),
        ("Day 90",
         "The knowledge base in one place, owned and versioned; warranty claims answered with an engineering "
         "report; the first dashboard live on failure modes, cost per refurbishment and claim rate."),
    ], widths=(1500, 8830))

    m.section("A REFURBISHED PART IS A CLAIM YOU HAVE TO PROVE")
    m.para("The customer's engineers do not buy a repaired component; they buy the confidence that it will "
           "run for the hours they need it to. That confidence is built from three things and nothing else: "
           "a defined method, a test that reproduces the service load, and a record that travels with the "
           "part. When all three exist, the price discussion changes character — the argument is about "
           "hours and risk instead of about the invoice.", after=80)

    m.section("THE FAILURE-MODE LIBRARY IS THE COMPANY'S REAL ASSET")
    m.para("A refurbishment business knows something its customers do not: how a specific component family "
           "actually fails in the field, and what that failure costs. Written down per family — failure "
           "mode, hours to failure, inspection point, method, acceptance limit — that knowledge prices "
           "work, predicts warranty exposure and tells R&D where to look. Left in the heads of two "
           "experienced people, it walks out of the door with them.", after=80)

    m.section("TWO SITES, ONE STANDARD")
    m.para("A workshop in Silkeborg and a workshop in Council Bluffs only behave as one company if the "
           "standard travels: the same method, the same acceptance test, the same record, in a language both "
           "teams can use. That is a documentation problem before it is a management problem — one version "
           "of the instruction, one template for the test report, one place where the failure history is "
           "written. I have worked across countries and languages, and the rule that held was always the "
           "same: what is not written down is not shared.", after=80)

    m.section("WHAT A SCRAP CONTAINER ACTUALLY COSTS")
    m.para("The mission is to keep good components in operation instead of in the scrap container — wind "
           "turbines running, waste avoided — and that is an engineering target with a number behind it: every unit that is scrapped although it could "
           "have been refurbished is a lost margin, and every unit that is returned and fails again is a "
           "warranty claim and a customer who stops believing the judgement. Both are controlled the same "
           "way — a defined method, a test that reproduces the load, and a record. Standards are not "
           "bureaucracy in this business; they are the difference between a repair and a promise.", after=80)

    # ---------------------------------------------------------------- page 4
    m.page_break()
    m.section("THE TEST BENCH AND THE CUSTOMER'S ENGINEER ARE THE SAME CONVERSATION")
    m.para("Selling engineering judgement means the person who sets the acceptance criterion can defend it "
           "in a meeting with a customer's technical department. I have done both sides: signed the "
           "protocol and then explained to a customer why the evidence was insufficient to accept the "
           "installation. That is the same skill in two rooms, and it is what makes a small technical "
           "organisation credible next to an OEM.", after=80)

    m.models_table("WHAT THE ROLE REQUIRES — WHAT I HAVE DELIVERED",
                   ("Requirement in the posting", "Evidence"), [
        ("Own the technical knowledge base and standards — component types, failure modes, refurbishment methods and acceptance criteria",
         "Methods, acceptance tests and work instructions written down in own business and across 37 capital "
         "projects; failure modes recorded, not remembered."),
        ("Make sure testing and inspection protocols are fit for purpose, and build quality into production so issues are caught early",
         "FAT/SAT and IQ/OQ/PQ protocols with witness points and hold points; first-off checks at the station; "
         "zero critical findings at handover."),
        ("Lead the technical response to complaints and warranty claims, including root cause analysis",
         "Root cause with A3, 5-why and Ishikawa on deviations and repeat failures; corrective action written "
         "into the method and the customer answered with evidence."),
        ("Give Sales, Operations and Procurement the engineering input behind their decisions — feasibility, specifications and customer documentation",
         "Feasibility, specification and customer documentation produced before the price; supplier and "
         "subcontractor scope negotiated under AB 18 and ABT 18."),
        ("Drive R&D, continuous improvement and the digital systems that connect people, processes and data",
         "SAP ERP, Power BI and Python built into quoting, KPI and checklist work with above 40 % "
         "productivity gain; 5S, PDCA and standard work in 24/7 operation."),
        ("Keep certifications, compliance and technical documentation in order",
         "Danish HV/LV authorisation, DS/HD 60364 and SB guidance as the working frame; documentation "
         "inspected under GMP/FDA/EMA with zero critical findings."),
        ("Be a major contributor to the management team",
         "Owner and technical director with full P&L since 2023; member of the management team of a 24/7 "
         "plant operation and of cross-functional project leadership with 25 specialists."),
        ("Own the technical side of everything we deliver, in Denmark and the US",
         "Technical ownership across sites and countries: Copenhagen, Kalundborg, Tehran and suppliers "
         "abroad; work in English, Danish and Persian, with travel built into the role."),
        ("Strengthen the competences within the electric area",
         "Electrical engineering at EQF 6 plus Danish HV/LV authorisation: HV/MV/LV installations, "
         "switchgear, panels, control systems, SCADA, fault finding and testing."),
        ("An electrical engineer (BSc/MSc or equivalent) with hands-on experience in power electronics, converters, control systems or industrial electronics",
         "Electrical engineering degree at EQF 6 (bachelor level) plus B.Tech; hands-on control systems, "
         "industrial electronics, panels and control equipment in operation and commissioning."),
        ("As comfortable at the test bench as in a technical discussion with a customer's engineers",
         "Witnessed and signed FAT/SAT and IQ/OQ/PQ; fault finding with instruments at the plant; the same "
         "person who explains the evidence to the customer's technical department."),
        ("Structured: you document, standardise and share knowledge rather than keep it in your head",
         "Work instructions, competence matrices and checklists in own business; documentation produced with "
         "the work in a validated production environment, where the file is the proof."),
        ("Experienced with testing, quality and root cause analysis",
         "Testing and acceptance across 37 capital projects and 11 contracts; quality systems, deviation "
         "handling, 5-why, Ishikawa and A3 in daily use."),
        ("Curious about how automation and data can make good engineering scale",
         "Built AI-assisted quoting, dashboards and checklists in Python and Power BI with measurable "
         "productivity gain; reporting automated on SAP ERP data."),
        ("Fluent in English; Danish is an advantage",
         "English professional, written and spoken, for specifications, protocols and management reporting; "
         "Danish native."),
        ("Experience from the wind industry is a strong plus",
         "Component-level electro-mechanical work — motors, pumps, switchgear, panels, control electronics — "
         "with the testing, acceptance and root-cause discipline a refurbishment operation lives from."),
    ], widths=(3600, 6746))

    return m.save(path, title="CTO — 2Refurb, Silkeborg")


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_2Refurb_CTO.docx')
    build(out)
    print(out)
