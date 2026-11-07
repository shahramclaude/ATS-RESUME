# -*- coding: utf-8 -*-
"""atNorth — Senior Technical Lead, Electrical.

English posting → English deliverable (en-GB): letter p1, CV p2–3, 90 days + requirement
matrix p4. Policy: master/README.md — job first, candidate only as evidence, no hedges.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = "Senior Technical Lead – Electrical · Critical power and engineering authority"
CONTACT = "+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Copenhagen, Denmark"


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("7 November 2026")
    m.meta("atNorth · Engineering, Design and Operations · Nordic data centre portfolio")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Application: Senior Technical Lead — Electrical", bold=True, color='1A1A1A')
    m.para("To the hiring team at atNorth", after=70)

    # ---------------------------------------------------------------- page 1
    m.para("A data centre is not difficult on a Tuesday afternoon. It is difficult on the afternoon when the "
           "incoming supply is lost, the UPS transfers to battery, and the standby arrangement has to be proven "
           "— a generator that must start on the first attempt, a battery bank that must carry the load, a "
           "protection scheme that must clear the fault without taking the hall with it — and someone must "
           "decide, from a single-line diagram, a protection setting and a switching sequence, what happens "
           "next and in which order. That decision is what an electrical technical authority exists for. It is "
           "the role I am applying for.", after=80)

    m.para("**The authority part I have carried as a signature, not a title.** In Denmark the HV authorisation "
           "is personal and legal: the holder signs for the design, the calculation, the standard applied and "
           "the finished installation before it is energised. I have held that authorisation since 2023 and "
           "carry it in my own company, which means nothing leaves the desk without a signature, and no "
           "installation is energised because a schedule said it should be. Applied across eight sites in "
           "four countries, that discipline is what keeps a portfolio technically identical instead of eight "
           "different opinions.", after=80)

    m.para("**Mission-critical is a discipline I have worked inside, not visited.** For five years I was "
           "operations and maintenance manager at **Lynetten under Biofos**, a critical plant in **24/7 "
           "operation** with **HV switchgear, transformers, pumps, blowers, ventilation and SRO/SCADA**. The "
           "plant could not be taken offline to be understood: fault-finding happened under load, switching "
           "and **LOTO** were planned before anyone opened a panel, and the standby arrangements were tested "
           "rather than assumed. That is the same rule a data centre lives by — the load does not wait for a "
           "convenient moment.", after=80)

    m.para("**Reliability is decided at commissioning and handover, not discovered at three in the morning.** "
           "At **Novo Nordisk** I ran **37 parallel capital projects** with **25 specialists**, from "
           "requirement specification and **design review** through **FAT/SAT** and **IQ/OQ/PQ** to a handover "
           "signed by both sides. The electrical scope included **UPS systems, panels and control, battery-"
           "backed emergency and escape lighting, ABA/ABV and PDS** — and the portfolio closed with **zero "
           "critical findings**. A handover that is documented, tested and accepted is the cheapest reliability "
           "improvement available to any operator.", after=80)

    m.para("**Standards are worth exactly the compliance they actually get.** I have written specifications, "
           "procedures and checklists, and I have watched which of them people follow at two in the morning. "
           "The ones that survive are short, unambiguous, and matched by a tool that makes the compliant way "
           "the quick way. I work to **DS/HD 60364** and the Danish **SB guidance**, and I build the "
           "documentation flow around the standard rather than beside it — because a procedure that is "
           "bypassed is worse than no procedure at all.", after=80)

    m.para("**A root cause is a method, not a meeting.** **A3, 5-Why, Ishikawa, FMEA and PDCA** are the tools I "
           "use on an electrical incident: what failed, what allowed it to fail, what would have caught it, and "
           "which standard or setting changes as a result. Every corrective action gets an owner and a date, "
           "and is verified rather than assumed. The purpose is to change the system so the same fault cannot "
           "recur — not to find the person who was on shift.", after=80)

    m.para("**The engineering base behind that: LV, MV and HV, UPS, protection and power quality.** I have "
           "worked on **transformers, HV and LV switchgear, protection and control, UPS systems, "
           "battery-backed emergency and escape lighting, photovoltaics, metering and load management**. I "
           "measure before I conclude: energy and load data took **over 40 % off consumption** at Lynetten and "
           "**40 % off energy cost** in a Novo Nordisk programme, both because the measurement came first and "
           "the investment came second. **Power quality** is a measurement discipline long before it is an "
           "equipment decision.", after=80)

    m.para("**Advisor to the business, and a teacher by necessity.** I have been the electrical counterpart for "
           "client organisations, consultants, vendors and authorities, translating a protection philosophy "
           "into a sentence a project manager can act on. I have also led **25 specialists, 14 staff, 12 "
           "technicians and a team of 5 electricians and 3 apprentices**, with competence matrices, **technical "
           "mentoring** and one-to-ones built on SLII and GROW. A technical authority that cannot explain "
           "itself is a bottleneck; the point is to leave capability behind at every site.", after=80)

    m.para("I am based in Copenhagen, half an hour from the airport, and **willing to travel across the Nordic "
           "region** as the portfolio requires — with sites under development in Denmark, Finland and Sweden, "
           "that is a weekly rhythm rather than an exception. **Fluent English and native Danish**, with "
           "English as the working language for technical and commercial negotiation. I would like to hear how "
           "technical authority is divided between Design and Operations at atNorth today, and which of your "
           "sites sets the engineering standard the others are measured against.", after=70)
    m.meta("Yours sincerely", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFILE")
    m.para("Electrical engineer by trade and by authorisation — **elautoriseret maskinmester (LV/MV/HV)** with "
           "20+ years in **critical infrastructure in 24/7 operation**, and B.Tech in technology management and "
           "mechanical engineering. Five years as operations and maintenance manager at **Lynetten (Biofos)** "
           "with **HV switchgear, transformers, UPS and SRO/SCADA** under continuous load, and **over 40 % "
           "lower energy consumption** from measurement and load management. Two years delivering **37 capital "
           "projects** with **25 specialists** at Novo Nordisk — design review, **FAT/SAT, IQ/OQ/PQ**, "
           "commissioning and **technical handover**, with **zero critical findings**. Legally the **signatory** "
           "for electrical design and installation in own company since 2023.", after=80)

    m.section("CRITICAL POWER, COMMISSIONING AND ASSURANCE")
    for label, body in [
        ("Technical authority and signatory",
         "Holder of the Danish HV/LV authorisation and legally the signatory for electrical design, "
         "calculations, standards, procedures and the acceptance of finished installations — in own company "
         "and on every project delivered under it."),
        ("Critical power and distribution",
         "HV and LV switchgear, transformers, protection and control, UPS systems, battery-backed emergency and "
         "escape lighting, photovoltaics, metering and load management — maintained and fault-found under load, "
         "not only at handover."),
        ("Commissioning and operational readiness",
         "FAT/SAT, IQ/OQ/PQ, integration testing and documented handover across 37 capital projects, with a "
         "maintenance strategy agreed before acceptance; handover evidence signed by both sides."),
        ("Standards, specifications and procedures",
         "Technical specifications, operational procedures, switching and LOTO routines written to DS/HD 60364 "
         "and the SB guidance — kept short enough to be used on shift, not just filed."),
        ("Incident investigation and root cause",
         "A3, 5-Why, Ishikawa, FMEA and PDCA applied to electrical incidents and performance issues; corrective "
         "actions with owner, date and verification, and the standard changed as a result."),
        ("Teams, mentoring and stakeholders",
         "25 specialists, 14 staff, 12 technicians and 5 electricians plus 3 apprentices led; competence "
         "matrices, technical mentoring and one-to-ones — and direct dialogue with clients, consultants, "
         "vendors and authorities."),
    ]:
        m.bullet(label, body, after=25)

    m.section("EXPERIENCE")
    jobs = [
        ("Owner / Technical Director",
         "ELOHVAC ApS · Copenhagen · May 2023–present",
         "5 electricians and 3 apprentices · full P&L · HV/LV authorisation · electrical service and contracting",
         [("Authority, standards and delivery",
           "Signatory for electrical design, installation and acceptance; LOTO, risk assessment and APV at "
           "site start; specifications and checklists in daily use, with own Python and Claude tooling giving "
           "over 40 % productivity gain.")]),
        ("Senior Commissioning Engineer / Project Manager, Electrical Systems",
         "Novo Nordisk A/S · Kalundborg/Bagsværd, Denmark · Nov 2022–Jul 2024",
         "37 parallel capital projects · 25 specialists · DKK 2–10m each · GMP/FDA/EMA validated environment",
         [("Design review to handover",
           "Requirement specification, design review, FAT/SAT, IQ/OQ/PQ and documented handover for UPS, "
           "panels, control, emergency lighting and PDS; zero critical findings at handover.")]),
        ("Project and Workshop Manager",
         "Ventek-Air · Copenhagen · Jan 2022–Nov 2022",
         "14 employees · 11 concurrent projects · DKK 2–10m per project",
         [("Integration, subcontractors and handover",
           "Daily board meetings and bottleneck analysis; subcontractors and external specialists coordinated "
           "against agreed interfaces; standardised work packages and handover documentation.")]),
        ("Operations and Maintenance Manager",
         "Lynetten under Biofos · Copenhagen · Aug 2017–Jan 2022",
         "Critical plant in 24/7 operation · HV switchgear and transformers · SRO/SCADA · pumps, blowers, ventilation",
         [("Critical operation, switching and resilience",
           "Switching and LOTO planned and authorised; standby arrangements tested; fault-finding under load; "
           "preventive maintenance and spare-part strategy; over 40 % lower energy consumption.")]),
        ("Electromechanical Technician / Production Team Leader",
         "ARJ Engineering · Tehran · Dec 2003–Mar 2010",
         "12 mechanics and technicians · machine workshop · industrial equipment",
         [("Diagnosis and corrective action",
           "Fault diagnosis and repair of industrial electrical and mechanical plant; root-cause analysis and "
           "corrective actions; shift planning, training and performance follow-up.")]),
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
    m.para("English: fluent, technical and commercial · Danish: native · Persian: native · **Full driving licence "
           "and own car** · Based in Copenhagen, **willing to travel across the Nordic region** as required · "
           "Available at short notice · References on request.", after=70)

    m.models_table("THE FIRST 90 DAYS — STANDARDS, ASSURANCE AND READINESS",
                   ("Period", "What happens, and how it is measured"), [
        ("Week 1–2",
         "Walk the Danish sites and the electrical rooms; read single-line diagrams, protection settings, "
         "switching and LOTO procedures; meet Design, Development and Operations; review open incidents, "
         "commissioning status and handover records across the portfolio."),
        ("Day 30",
         "Gap map between the standards as written and the practice on site; the five electrical risks with the "
         "highest consequence identified with owner, next action and a date; assurance gates for design review "
         "and handover agreed with Design and Operations."),
        ("Day 60",
         "One Nordic engineering baseline drafted — specifications, calculations, protection philosophy, "
         "switching and LOTO — reviewed with the sites that have to live with it; incident and RCA template in "
         "use and feeding back into design."),
        ("Day 90",
         "First design assurance review completed to the new baseline on a live project; commissioning and "
         "handover evidence standardised; competence matrix and mentoring plan agreed for the electrical teams "
         "across sites.")])

    m.section("A DATA CENTRE IS A PLANT THAT IS NOT ALLOWED TO STOP")
    m.para("atNorth's customers buy colocation and built-to-suit capacity that runs on renewable energy, across "
           "eight sites and four countries in the Nordics. The electrical standard is what makes that promise "
           "credible at every one of them. And the difference between a data centre and most industrial plants "
           "is not the equipment; it is the consequence. A stopped pump costs production, a stopped cooling loop costs a hall. That consequence "
           "sets the standard for everything upstream of it: how a design is reviewed, how a protection setting "
           "is justified, how a switching order is written, how a handover is accepted, and how an incident is "
           "investigated afterwards. Working for five years in a plant that could not be taken offline teaches "
           "that discipline faster than any framework document.", after=80)

    m.section("THE SIGNATURE IS THE WHOLE JOB")
    m.para("An electrical authority is not valuable because it knows more than the designers. It is valuable "
           "because it says yes or no, in writing, and can defend that decision afterwards. That means reading "
           "the calculation rather than accepting it, checking the standard that was applied rather than the one "
           "that was cited, and refusing to energise an installation because the programme is behind. I have "
           "carried that personal liability since 2023, and I have never found a project where honesty about "
           "the technical state of things cost more than discovering it later.", after=80)

    m.section("STANDARDS ONLY COUNT IF SOMEONE USES THEM")
    m.para("A Nordic portfolio drifts apart in the details: a protection philosophy interpreted differently on "
           "two sites, a switching procedure that exists in three versions, a handover pack that one country "
           "accepts and another does not. The fix is not a longer manual; it is a short baseline, agreed with "
           "the people who operate it, and a review cycle that keeps it current. I have written procedures that "
           "were used and procedures that were bypassed, and the difference was always whether the compliant "
           "route was also the fastest one. **Dependable, empowering and flexible** are the words atNorth uses; "
           "in engineering they translate into a standard that holds, people trusted to apply it, and a "
           "baseline that changes when the evidence does.", after=80)

    m.section("I HAVE BEEN ON THE OPERATIONS SIDE OF A DESIGN DECISION")
    m.para("Most reliability problems are designed in months before they are felt. I have been on the receiving "
           "end of that: equipment that could not be maintained without stopping production, panels with no room "
           "to work in, documentation that did not match what was installed. It is why I insist on the "
           "operations view during design review — access, isolation points, spares, test points and what "
           "someone will actually have to do at two in the morning when nobody is available to ask.", after=80)

    m.page_break()

    m.models_table("WHAT THE ROLE REQUIRES — WHAT I HAVE DELIVERED", ("Requirement in the posting", "Evidence"), [
        ('Technical authority and signatory for electrical designs and standards',
         'Signatory for electrical design and acceptance under the Danish HV/LV authorisation since 2023; specifications, switching and LOTO procedures enforced in own company and on 37 projects.'),
        ('Leadership across LV/MV distribution, UPS, generators, batteries, protection systems and controls',
         'HV/LV switchgear, transformers, protection and control, UPS and battery-backed supplies maintained and fault-found under load in 24/7 operation; standby sequences tested.'),
        ('Design reviews, engineering assurance, commissioning and technical handovers',
         'FAT/SAT, IQ/OQ/PQ and documented handover across 37 projects with 25 specialists; acceptance criteria agreed up front, handover signed by both sides — zero critical findings.'),
        ('Engineering standards, specifications and best-practice frameworks',
         'Specifications, checklists and standard work to DS/HD 60364 and the SB guidance; one documentation flow across sites and shifts, kept in use by 5S and PDCA.'),
        ('Collaboration with design, development and operations teams',
         'Joint design reviews and handover gates with client organisation, consultants and vendors; commissioning run with operations present, so they inherit a plant they have tested.'),
        ('Technical investigations, troubleshooting and root-cause analyses',
         'A3, 5-Why, Ishikawa, FMEA and PDCA on electrical incidents and performance issues; corrective actions with owner and date, verified, and the standard changed as a result.'),
        ('Primary electrical engineering advisor for stakeholders, clients and vendors',
         'Electrical counterpart for client organisations, consultants, suppliers and authorities across 37 capital projects and in own business — queries, change control, acceptance.'),
        ('Evaluating emerging technologies and supporting innovation',
         'Photovoltaics, metering, load management and data-driven optimisation introduced on measured evidence: over 40 % lower consumption at Lynetten, 40 % lower energy cost at Novo.'),
        ('Training, technical mentoring and knowledge sharing',
         '25 specialists, 14 staff, 12 technicians and 5 electricians plus 3 apprentices led; competence matrices, technical mentoring and one-to-ones on SLII and GROW.'),
        ('Asset lifecycle planning, maintenance strategies, resilience and continuous improvement',
         'Preventive maintenance, criticality assessment, spare-part strategy and standby arrangements on a critical plant in 24/7 operation; improvement tracked against uptime and energy.'),
        ("Bachelor's or master's degree in electrical engineering or related discipline",
         'B.Tech in technology management and mechanical engineering (GPA 7.6/12), electrical and mechanical engineering design at EQF 6 — and the Danish HV/LV authorisation.'),
        ('10+ years in mission-critical electrical engineering and senior leadership',
         '20+ years from electromechanical technician and production team leader to operations manager, senior commissioning engineer and owner of an authorised electrical business.'),
        ('Data centre engineering projects and critical electrical infrastructure',
         'Critical electrical infrastructure delivered and operated where an outage is measured in production and in safety: HV/LV distribution, transformers, UPS, battery-backed supplies, protection, power quality.'),
        ('Commissioning, system integration, operational readiness and asset lifecycle',
         'FAT/SAT, IQ/OQ/PQ, integration testing and handover on 37 projects; preventive maintenance, criticality and spares on a critical plant for five years — evidenced by records.'),
        ('Proven technical authority reviewing and approving designs and standards',
         'Signatory authority since 2023: designs reviewed rather than accepted, standards checked against the application, approval refused when the installation did not meet the requirement.'),
        ('Stakeholder management and translating complex technical concepts',
         'Technical counterpart for clients, consultants, vendors and authorities; monthly progress, cost and risk reporting to management and client, in the register each audience needed.'),
        ('Fluent English and willingness to travel across the Nordic region',
         'Fluent English and native Danish for technical and commercial negotiation; based in Copenhagen half an hour from the airport, ready to travel across all five Nordic markets.'),
    ], widths=(3200, 7146))

    m.section("WHAT TECHNICAL AUTHORITY SHOULD HAVE PRODUCED IN A YEAR")
    m.para("In a year this role should be measurable on four things: one electrical baseline that every site "
           "recognises as its own; design reviews that catch access, isolation points and spares before they "
           "become change orders; handovers that operations accept without a list of exceptions; and two or "
           "three engineers at other sites who can defend a protection decision without calling me. If those "
           "four are true, technical authority has become a capability rather than a person.", after=80)

    return m.save(path, title="Senior Technical Lead, Electrical — atNorth",
                  subject="Critical power, commissioning, engineering assurance and electrical technical authority",
                  keywords="senior technical lead, electrical engineering, critical power, ups, lv, mv, "
                           "protection, commissioning, operational readiness, engineering standards, "
                           "data centre, nordics, root cause analysis, mentoring")


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_atNorth_SeniorTechnicalLeadElectrical.docx')))
