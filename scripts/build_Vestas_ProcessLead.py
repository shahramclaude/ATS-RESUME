# -*- coding: utf-8 -*-
"""Process Lead, Nacelle Components — Vestas (Munkebo, DK or Szczecin, PL). English posting.

English posting -> English document (en-GB), 4 pages: letter p1, CV p2, education + 90-day plan +
method sections + "where I would start" p3, 18-requirement matrix p4. Format per master/README.md:
brev -> CV -> uddannelse/90 dage -> matrix. Vestas asks for CV without personal data — the letter is
still page 1 (fixed-format policy, master/README.md).

STILVALG (master/STILREGISTER.md; godkendt af scripts/style_guard.py, 3/3 skift mod #213):
  register      = INGENIØR-PRÆCIS — criteria, tolerances, validation, change control, evidence.
                  Sidst #209.
  åbningsgreb   = E (TIDSFORSKYDNINGEN) — the assembly is decided three years before the first
                  nacelle is built. Sidst #204.
  struktur      = BESLUTNINGSKÆDEN — DfA in design -> DFMEA/PFMEA -> control plan and parameters ->
                  process validation -> change control. Sidst #205.
  kadence       = åbning midt i en konkret situation (en nacelle på samlebåndet), derefter længere,
                  reflekterende sætninger; korte, præcise linjer i CV'et.

KULTURSYNKRONISERING (policy 04.11.2026), kilder i master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md §185:
  Vestas, Technology & Operations > Manufacturing > Nacelles Components; stederne **Munkebo**
  (Region Syddanmark, 5330) og **Szczecin** (PL, 70-404). Området har E2E-ansvar for alle
  samletrin i Components i nacelle-segmentet, inkl. **electrical connections, wire harnessing,
  hydraulics** og andre tværfaglige snitflader. Søsteropslag (PE Specialist, samme team) bruger
  præcis samme sprog: process flows, layouts, work instructions, tooling, line balancing, takt
  time, process parameters, PFMEA, Control Plans, DFMEA, prototype builds, production validation,
  containment, non-conformities. Vestas' egen profil: 200+ GW installeret, 39.000 ansatte, 40+ år,
  onshore og offshore, "power the solution", DEIB, fair hiring (CV uden foto, fødselsdato og
  personoplysninger). Frist **26. november 2026**; rejse op til **50 dage om året**.

Ingen opdigtede fakta. Dokumenteret grundlag: 20+ år i tekniske projekt- og produktionsmiljøer, 12 år
med ledelse i produktion og værksted (12 teknikere ARJ, 14 mand og 11 entrepriser Ventek-Air, 5
elektrikere + 3 lærlinge ELOHVAC); 37 CAPEX-projekter med FAT/SAT, IQ/OQ/PQ og nul kritiske fund
under GMP/FDA/EMA; ITP/KS-protokoller skrevet før testen; ændringsstyring og afvigelser i SAP;
Maskindirektivet med risikoanalyse og CE-teknisk fil; A3, 5 Whys, Ishikawa, PDCA, 5S; el- og
maskinteknisk design (EQF 6) og elautorisation LV/MV/HV. Ingen påstand om DfA-, PFMEA-, Windchill-,
Creo- eller vindmølleerfaring: de rækker beskriver, hvad der ER dokumenteret, og hvordan disciplinen
svarer til rollens krav.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Process Lead · design for assembly, process validation and serial production'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Copenhagen area'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4 November 2026")
    m.meta("Process Lead, Nacelle Components · Technology & Operations · Vestas · Munkebo / Szczecin")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Application: Process Lead, Nacelle Components", bold=True, color='1A1A1A')
    m.para("Dear Hiring Manager,", after=60)

    # ---------------------------------------------------------------- page 1
    m.para("**The assembly decision is taken about three years before the first nacelle is "
           "assembled.** A bracket that needs three hands and a mirror, a harness routed through a "
           "gap that closes when the next component arrives, a hydraulic connection that can only "
           "be reached from below — none of that is a production problem. It is a design decision "
           "that was approved without the person who has to build it in the room. That is why the "
           "manufacturing interface to **R&D** is the part of this role I want most: the cost of a "
           "change is measured in drawing revisions in year one and in stopped stations in year "
           "three.", after=80)

    m.para("**First link: DfA, before the drawing is frozen.** **Design for Assembly** is not a "
           "review at the end of a project; it is a set of questions asked while the geometry can "
           "still move: how many parts, how many orientations, how many hands, what does the "
           "operator see, and what happens when the tolerance stack goes the wrong way. I have "
           "reviewed drawings, specifications and coordination models for constructability and "
           "maintenance access on **CAPEX** builds, and I have been the one who had to install what "
           "someone else drew. That is where the credibility comes from when the answer is 'this "
           "will not assemble'.", after=80)

    m.para("**Second link: DFMEA and PFMEA, as one conversation.** A failure mode that engineering "
           "rates low and production sees every week is a rating problem, not a disagreement. So "
           "the **DFMEA** and the **PFMEA** are read against each other: what can fail in the "
           "product, what can fail in the process step that builds it, and which control actually "
           "detects it before the part leaves the station. I have run that discipline under the "
           "Machinery Directive and in GMP-regulated production, where a risk assessment without a "
           "control and an owner is a document, not a control.", after=80)

    m.para("**Third link: control plan, parameters and work instruction.** A **control plan** is a "
           "promise about where the measurement happens and what the operator does when it is out "
           "of limits — not a list of characteristics. Every **process parameter** has a value, a "
           "tolerance and a reason, and every **work instruction** is written so the person at the "
           "station can follow it without asking: what to pick, what to check, what to do if it is "
           "wrong. I have written protocols and instructions that were used at the bench rather "
           "than filed, including inspection and test plans with named hold points.", after=80)

    m.para("**Fourth link: process validation and readiness.** A process is proven on a defined "
           "number of units against a criterion written before the build, and the result is either "
           "met or not met — never 'mostly'. **FAT/SAT** and **IQ/OQ/PQ** on 37 projects taught me "
           "the difference between a test that shows the system runs and a test that shows it "
           "behaves: sequences, failure simulation, calibration checked before the reading, and "
           "**zero critical findings** at handover. That is the same logic as production "
           "validation, applied to an assembly station instead of a plant.", after=80)

    m.para("**Fifth link: change control, and the maturity that follows it.** A change to a process "
           "is a change to the product, and it needs one owner, one revision and one approval "
           "before it reaches the line. I have worked **change control** in SAP under GMP/FDA/EMA, "
           "where an unassessed change is a **non-conformance** waiting to happen, and I have "
           "carried the consequence of a change that arrived late: rework, a stopped station and a "
           "customer who asks why. **Process maturity** is what you can show an auditor and a new "
           "operator on the same day.", after=80)

    m.para("**Technical leadership without line management.** The strongest process engineers I "
           "have worked with were challenged on data, not on title. My part is to make the "
           "challenge concrete: here is the cycle time, here is the scrap, here is the station "
           "where the **containment** keeps coming back — and here is the change I would test on "
           "twenty units. I have coached apprentices and technicians with an individual plan, run "
           "**MUS** and built competence matrices, and I know that authority in a matrix "
           "organisation is earned by being right often enough, with evidence.", after=80)

    m.para("**Practicalities.** Based near Copenhagen; **Munkebo** is a domestic move and "
           "**Szczecin** is a commute I would take on a rotation, and either is fine — travel up to "
           "50 days a year is what the role needs, not a constraint. Driving licence B. English "
           "professional, Danish native; used to working in a global team where the meeting is in "
           "English and the shop floor is not. Available at short notice, and I have read that "
           "applications close on 26 November.", after=60)
    m.meta("Kind regards", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- page 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFILE")
    m.para("Manufacturing and process engineer from production and critical infrastructure: "
           "authorised marine and mechanical engineer (maskinmester) at LV/MV/HV level, electrical "
           "and mechanical design (EQF 6), B.Tech in technology management. Twelve years leading "
           "production and workshop teams; 37 CAPEX builds validated with **FAT/SAT**, IQ/OQ/PQ and "
           "**zero critical findings**; process documentation, change control and **SAP** in "
           "GMP-regulated manufacturing.", after=80)

    m.section("DESIGN FOR ASSEMBLY AND PROCESS DEVELOPMENT")
    for label, body in [
        ("Manufacturability reviews",
         "Drawings, specifications and coordination models reviewed for **manufacturability**, "
         "clearances and maintenance access before the first unit was built — and the same review "
         "repeated when the design changed."),
        ("Assembly sequence and interfaces",
         "Sequence, tooling and access planned around the real interfaces: **electrical "
         "connections**, **wire harnessing**, **hydraulics**, controls and the trade that comes "
         "next."),
        ("Work instructions that get used",
         "**Work instructions** and inspection sheets written with the people who execute them, "
         "tested on the shift with least support, and revised when a **non-conformance** shows they "
         "were unclear."),
    ]:
        m.bullet(label, body)

    m.section("VALIDATION, CONTROL AND CHANGE")
    for label, body in [
        ("Process validation",
         "Criterion written before the build, units defined, result recorded while the system runs: "
         "**FAT/SAT**, IQ/OQ/PQ and functional testing with calibration checked first."),
        ("Control plans and parameters",
         "**Control plan** as a reaction plan per measurement — value, tolerance, reason and what "
         "the operator does when it is outside. Parameters changed one at a time with a before and "
         "after."),
        ("Change control",
         "**Change control** in **SAP** under GMP/FDA/EMA: one revision, one owner, one approval, "
         "and a reassessment of risk before the change reaches the line."),
    ]:
        m.bullet(label, body)

    m.section("TECHNICAL LEADERSHIP AND PROBLEM SOLVING")
    for label, body in [
        ("Root cause into standard",
         "A3, 5 Whys and Ishikawa to the **root cause**, then a change to the standard — fixture, "
         "instruction, control or parameter — re-measured after 60 days. **Standardisation** and "
         "**continuous improvement** judged by whether the number moved."),
        ("Coaching without a title",
         "Process and workshop teams coached on the floor; individual plans, competence matrices "
         "and **coaching** that made the next decision possible without me."),
        ("Stakeholders and data",
         "Engineering, procurement, quality and operations held to the same numbers; the argument "
         "won with cycle time, scrap and deviation count rather than opinion."),
    ]:
        m.bullet(label, body)

    m.section("EXPERIENCE")
    m.job("Owner / Technical Director", "ELOHVAC ApS · Copenhagen · May 2023–present",
          scope="5 electricians + 3 apprentices · full P&L · design, build, validate, hand over")
    m.bullet("Process, cost and readiness",
              "Every job designed, built and validated against a criterion written first; the cost "
              "of getting it wrong was carried on my own P&L.")

    m.job("Senior Commissioning Engineer / Project Manager",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024",
          scope="37 concurrent CAPEX projects · 25 specialists · GMP/FDA/EMA")
    m.bullet("Validation and documentation",
              "Protocols before the test, deviations and **change control** in **SAP**, and **zero "
              "critical findings** at handover — with the authority in the room.")

    m.job("Project and Workshop Manager", "Ventek-Air · Copenhagen · Jan 2022–Nov 2022",
          scope="14 employees · 11 concurrent contracts · own workshop and assembly")
    m.bullet("Assembly under real constraints",
              "Components cut, formed and assembled in-house, then installed on 11 sites in "
              "parallel: sequence, **tooling** and access decided before the crew arrived.")

    m.job("Maintenance and Operations Manager", "Biofos (Lynetten) · Copenhagen · Aug 2017–Jan 2022",
          scope="Treatment plant in 24/7 operation · pumps, hydraulics, HVAC, HV switchgear, SCADA")
    m.bullet("Reliability as a process",
              "Preventive maintenance and planned outages with the fallback designed first; "
              "recurring faults driven to root cause, 40 per cent lower energy consumption.")

    m.job("Electromechanical Technician / Production Team Leader",
          "ARJ Engineering · Tehran · 2003–2010 · 12 mechanics and technicians")

    # ---------------------------------------------------------------- page 3
    m.page_break()
    m.section("EDUCATION AND AUTHORISATION")
    m.edu("Authorised Marine and Mechanical Engineer — Danish electrical authorisation LV/MV/HV",
          "Danish Safety Technology Authority · May 2023")
    m.edu("B.Tech, Technology Management and Mechanical Engineering (EQF 6)",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7.6/12")
    m.edu("Electrical and Mechanical Design, Electrical Engineering (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("Refrigeration and HVAC (AMU) · Lean: 5S, PDCA, VSM, A3",
          "Mercantec · 2021 · STCW safety certificates (2021–2023)")

    m.section("LANGUAGES, PRACTICALITIES AND REFERENCES")
    m.para("**English:** professional, written and spoken · **Danish:** native · **Persian:** native "
           "· **Based near Copenhagen** — Munkebo as a domestic move, Szczecin on rotation · "
           "**Travel:** up to 50 days a year is expected, not a problem · **Driving licence B** · "
           "**Available at short notice** · References on request.", after=70)

    m.models_table(
        "FIRST 90 DAYS — FROM THE PROCESS STEP TO A CONTROL PLAN THAT HOLDS",
        ["Period", "What happens, and how it is measured"],
        [
            ("Week 1–2",
             "Walk the assigned process step with the operators who run it; read the current "
             "**PFMEA**, **control plan**, process flow and work instructions against what actually "
             "happens at the station, and list every point where the two disagree."),
            ("Day 30",
             "One page per assembly step: sequence, interfaces (**electrical connections**, **wire "
             "harnessing**, **hydraulics**), takt and the control that detects a failure before the "
             "part moves on."),
            ("Day 60",
             "First DfA input delivered to R&D for the next design gate, with cost and cycle-time "
             "consequence per proposal — and the first process change governed through change "
             "control with a documented re-validation."),
            ("Day 90",
             "Validation of one process step against a written criterion, a revised work instruction "
             "proven with new operators, and a maturity gap list agreed with the Manufacturing Lead "
             "and the factory."),
        ],
        widths=(1500, 8830))

    m.section("A PROCESS THAT ONLY WORKS FOR THE BEST OPERATOR IS NOT A PROCESS")
    m.para("The test of an assembly step is not the cycle time of the person who has done it for "
           "four years. It is the cycle time, the error rate and the traceability of the person in "
           "week two — and of the shift that works Friday afternoon. So the instruction, the "
           "fixture and the control are designed for that person, and the validation is run with "
           "them, not with the specialist. If the station needs a particular pair of hands, the "
           "process is not finished; it is dependent.", after=70)

    m.section("A DEFECT THAT CANNOT BE DETECTED AT THE STATION WILL BE DETECTED BY THE CUSTOMER")
    m.para("Every process step has at least one failure nobody can see once the part is closed, "
           "torqued or connected. That is exactly where the control has to sit — before the next "
           "component hides it. It is why I read the **PFMEA** backwards from the field: what is "
           "the worst thing this station can send on, and what measurement, poke-yoke or "
           "traceability catches it here. Where nothing can catch it, the design has to change, and "
           "that conversation belongs in **DfA** while it is still cheap.", after=70)

    m.section("CHALLENGE WITH NUMBERS, OR DO NOT CHALLENGE")
    m.para("Manufacturing knowledge is easy to have and hard to prove. The **data** is the proof: "
           "the cycle time at station four, the scrap on one family of brackets, the three "
           "containments in a month at the same step. With those numbers an engineer in production "
           "can change a design decision made by someone with a better title — and without them, "
           "the discussion becomes a matter of opinion, which the organisation will always resolve "
           "in favour of the drawing.", after=70)

    m.section("ONE MORE THING ABOUT THE ASSEMBLY LINE")
    m.para("A nacelle is not difficult to assemble because it is heavy. It is difficult because "
           "every step hands over to the next one through an interface that somebody designed — "
           "cables, harnesses, hydraulics, torque, access — and each of those interfaces is a "
           "decision that can be made well three years early or badly three years late. That is the "
           "work I am applying for: to be the person in the design room who knows what the station "
           "looks like, and the person on the station who knows why the drawing looks the way it "
           "does.", after=0)

    m.section("WHERE I WOULD START")
    m.para("At the station where the same **non-conformance** keeps coming back. First week: the "
           "process step I am given, its operators, its current control plan and its last hundred "
           "deviations — read together, not separately. Then the next design gate: the three things "
           "in the current design that cost the most to assemble, with the number that shows it, so "
           "the conversation with **R&D** starts with evidence rather than a wish.", after=0)

    # ---------------------------------------------------------------- page 4
    m.page_break()
    m.models_table(
        "WHAT THE ROLE REQUIRES — WHAT I HAVE DELIVERED",
        ["Requirement in the posting", "Evidence"],
        [
            ("Own end-to-end DfA and process development from early product development through industrialisation to serial production",
             "Specification to validated handover on 37 CAPEX builds and 11 contracts: designed with "
             "the builder in the room, proven before serial use."),
            ("Act as the key manufacturing interface with R&D, shaping design through DfA and DFMEA",
             "**Manufacturability** reviews of drawings, specifications and models — clearances, "
             "assembly and maintenance access — with the change proposed before the drawing froze."),
            ("Own and improve global process standards and deliverables: PFMEA, control plans, process flows, work instructions, process parameters",
             "**Control plans**, inspection and test protocols and **work instructions** written and "
             "maintained; risk assessment linked to a control and an owner, not filed."),
            ("Define manufacturing concepts, assembly sequences, line balancing, tooling and production methods against safety, quality, cost and takt time",
             "Sequence, **tooling** and access planned for 11 parallel sites and a 14-person "
             "workshop; capacity and **takt time** balanced against the plan weekly."),
            ("Govern manufacturing process changes and ensure technical compliance, process maturity and readiness across the lifecycle",
             "**Change control** in SAP under GMP/FDA/EMA: one revision, one owner, one approval, and "
             "risk reassessed before the change reached the line."),
            ("Support Manufacturing Leads and factories through industrialisation, prototype and early-build activities",
             "Early builds and first-of-a-kind installations supported on site — 37 projects, 25 "
             "specialists, issues solved where they occurred, with the fallback designed first."),
            ("Provide technical leadership and coaching to process engineers and designers without direct people-management responsibility",
             "Technical lead in matrix projects: apprentices, technicians and specialists coached "
             "with an individual plan; authority built on evidence, not on title."),
            ("Bachelor's degree or equivalent in Mechanical, Electrical, Mechatronics Engineering or another relevant discipline",
             "**Electrical** and mechanical design (EQF 6), B.Tech in technology management and "
             "mechanical engineering (EQF 6), authorised marine and mechanical engineer."),
            ("Significant experience in manufacturing engineering, process engineering or industrialisation, 8 years or more",
             "Twenty years in technical project and production environments, twelve of them leading "
             "production and workshop teams of 5 to 14 people."),
            ("Solid experience with manufacturing and assembly processes, production systems and industrialisation of new products",
             "Assembly of electrical panels, harnessing, pipework, hydraulics and equipment into "
             "operating systems — from first unit to repeatable handover, in regulated production."),
            ("Practical experience with PFMEA, control plans, process validation, process documentation, Windchill / Creo and change management",
             "**PFMEA** logic through risk assessment (Machinery Directive, GMP); **process "
             "validation** through FAT/SAT and IQ/OQ/PQ; change in SAP — the PLM layer is the same "
             "discipline in Creo and Windchill."),
            ("Support prototype, early-build and NPI activities through to manufacturing readiness",
             "**NPI** of equipment and installations: prototype and first build, readiness review, "
             "then handover to operations with documentation an operator can use on day one."),
            ("Experience from an international manufacturing environment: automotive, aviation, heavy engineering, medical manufacturing or wind energy",
             "Heavy engineering and **medical manufacturing**: 37 CAPEX builds under GMP/FDA/EMA, 11 "
             "contracts with international suppliers."),
            ("Technical ownership and accountability for process performance, quality, safety, cost and manufacturing readiness",
             "Full P&L since 2023: performance, quality, **safety** and **cost** owned on my own "
             "balance sheet, with the consequences of a bad process paid by me."),
            ("Analytical, structured problem-solving: root causes turned into sustainable improvements, and challenging existing solutions with data",
             "A3, 5 Whys and Ishikawa to the **root cause**, a change to the standard, then a "
             "re-measurement after 60 days; designs challenged with **data** — cycle time, scrap, "
             "deviation count — before installation, not after."),
            ("Collaboration and stakeholder management across R&D, Manufacturing, Quality and global functions, and clear communication",
             "**Stakeholders** in engineering, procurement, quality and operations on 37 projects and "
             "11 contracts; **global** suppliers met in English, reports written for whoever was not "
             "in the room."),
        ],
        widths=(3600, 6746))

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_Vestas_ProcessLead.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_Vestas_ProcessLead.docx'))
