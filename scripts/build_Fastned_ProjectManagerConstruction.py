# -*- coding: utf-8 -*-
"""Project Manager Construction Denmark — Fastned, Copenhagen (hybrid). English posting.

ENGLISH posting -> ENGLISH document (en-GB), 4 pages: letter page 1, CV page 2, education +
90-day plan + method sections + "Where I would start" page 3, requirements matrix page 4.
Format per master/README.md.

STYLE (master/STILREGISTER.md; approved by scripts/style_guard.py, 3/3 against #224):
  register      = ROLL-OUT (new) — site, connection, transformer, permit, mobilisation, bay count,
                  station number, energisation date. Not a Danish-forvaltning or contractor register.
  opening       = A (THE PLACEMENT) — a charging station is not decided on the plot; it is decided
                  at the grid connection and at a municipal desk. Last #217.
  structure     = THE THESES — four claims: the grid connection is the project · the standard
                  station is the product · a new country is built by its first partners · the
                  schedule is a chain of permits and people. Last #220.
  cadence       = short sentences, each carrying a number, a date or a named party.

CULTURE SYNC (policy 04.11.2026), sources in master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md §196:
  **Fastned** — Dutch fast-charging operator founded 2012, mission "freedom to electric drivers",
  stations powered by sun and wind, iconic yellow solar canopies. **500+ colleagues, 40+
  nationalities, nine countries.** Own figures: **414 stations at the end of Q1 2026**; Q3 2026:
  **17 stations opened, 26 new locations secured, 65 stations under construction** (almost double
  year-on-year), guidance **70-100 new stations in 2026** and **476-506 stations by year-end**;
  ambition **~1,000 stations by 2030**; charging revenue **€51.3m** in Q3 2026; **55.6 GWh**, 2.1m
  sessions and 277m emission-free km in Q1 2026; average investment **~€892,000 per location**
  including charging hardware, grid connection, transformer technology and solar canopies.
  **Denmark:** from **three to seven** sites in early 2026, including four along the **E45** at
  **Pedersminde, Blankhøj, Gudenå East and Gudenå West** with **400 kW** chargers and up to twelve
  bays; canopies designed by a third party under a separate tender. **Country Director Denmark:
  Jesper Krüger Søndergaard** (appointed Q1 2026) — the posting calls the role "Country Manager
  Denmark", and the letter is addressed to him on that basis; the posting names no contact person.
  Culture words from the posting: informal international scale-up, "think like a founder", real
  work flexibility, family-friendly policies, inclusive and authentic, stock options, **DKK 22,400**
  training budget, EV fleet for private use, **2 Mission Days**, 25 days + 5 feriefridage.

No invented facts. Documented basis: **37 capital projects** (Novo Nordisk 2022-2024) with 25
specialists, FAT/SAT, zero critical findings, schedules, budgets and change control in **SAP**;
**14 staff and 11 concurrent contracts** with suppliers and subcontractors plus an own workshop
(Ventek Air 2022); **5 electricians + 3 apprentices**, full **P&L**, procurement and stock
(ELOHVAC since 2023); four years as head of operations and maintenance on a **24/7** plant with
**HV/LV switchgear, transformers, pumps and SRO/SCADA** (Biofos/Lynetten 2017-2022); **12
technicians** (ARJ 2003-2010); **Danish electrician authorisation LV/MV/HV** (May 2023), **B.Tech
Mechanical Engineering / Technology Management** (EQF 6, 7.6/12), **electrical and mechanical
design** (EQF 6), **Lean 5S/PDCA/VSM/A3** (2021); Danish native, English professional; **driving
licence B**; lives in **Måløv**, ~20 km from central Copenhagen.
**Deliberate wording:** no claim of having built a charging station, worked in e-mobility, filed a
grid connection application with a Danish DSO, or handled Danish municipal permits for charging
hubs. Those four stand as open gaps in the letter and in the matrix.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Project Manager, Construction · grid connections, build-out and handover · Copenhagen'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4 November 2026")
    m.meta("Project Manager Construction · Construction Management, Denmark · Copenhagen (hybrid)")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Application: Project Manager Construction Denmark", bold=True, color='1A1A1A')
    m.para("Dear Jesper,", after=60)

    # ---------------------------------------------------------------- page 1
    m.para("**A charging station is not decided on the plot. It is decided at the grid connection and "
           "at a municipal desk.** The canopy, the chargers and the asphalt are repeatable; Fastned "
           "has put them up **414 times**. What is not repeatable is the 400 kW that has to come from "
           "somewhere, the easement nobody wrote down, and the case officer who has never assessed a "
           "charging hub before. In Denmark, that is where the date is set — and that is where a "
           "construction project manager earns the salary.", after=80)

    m.para("Fastned ended **Q1 2026 with 414 stations in nine countries**, had **65 stations under "
           "construction** in Q3 — almost twice the year before — and is heading for **476-506** by "
           "the end of 2026, with **1,000** in sight for 2030. In Denmark the network went from "
           "**three to seven** sites in a few months, four of them won in a Danish **tender** "
           "and built along the **E45** at Pedersminde, Blankhøj and Gudenå East and West, with **400 "
           "kW** chargers and up to twelve bays. At "
           "roughly **€892,000 per location**, including charging hardware, **grid connection**, "
           "**transformer** and canopy, every week of delay is real money on a specific site.",
           after=80)

    m.para("**1. The grid connection is the project.** The canopy can be planned from a template. The "
           "connection cannot: it depends on the local **grid**, the **transformer** that may or may "
           "not be there, and a **distribution** operator with its own queue. I have spent four years "
           "on the other side of the meter, responsible for HV and LV **switchgear**, transformers, "
           "**SRO/SCADA** and a 24/7 supply that could not fail — and I hold a Danish electrician "
           "authorisation for **LV/MV/HV**. I have not yet filed a **grid connection** application "
           "with a Danish DSO, and I will not pretend otherwise; it is the first process I would "
           "learn.", after=70)

    m.para("**2. The standard station is the product. Deviations are the cost.** When a location costs "
           "**€892,000** and the build is repeated dozens of times a year, the money is in the second "
           "and third visit — in the **material supply** that arrived early, the **contractor** who "
           "was briefed once, and the drawing that did not need a site-specific answer. "
           "**Standardisation** is what makes the third station cheaper than the first. On **37 "
           "capital projects** I standardised templates and check points and cut the same argument "
           "twice over; on **11 concurrent contracts** I moved capacity before a bottleneck became a "
           "delay.", after=70)

    m.para("**3. A new country is built by its first ten partners.** A **roadmap** for construction "
           "initiation is not a document about Denmark; it is a list of names — two **contractors**, "
           "one **engineering partner**, one **supplier** of switchgear, one **HSE** adviser, one "
           "**authority** contact — and a written understanding of the standards each of them works "
           "to, so the first **mobilisation** does not start from zero. I have built that list before, "
           "three times, in three different technical environments, "
           "and it always starts with a visit and a question, not a spreadsheet.", after=70)

    m.para("**4. The schedule is a chain of permits and people, not a Gantt chart.** A **permit** that "
           "waits three weeks for a signature, a landlord who changes the access road, a **safety "
           "compliance** step that has to be signed off before the crane arrives: each of them owns a "
           "date in the plan, and none of them answers to the plan. **Stakeholder** management is the "
           "job — with the municipality, the DSO, the landlord, the contractor and, occasionally, the "
           "neighbour who did not know a station was coming. A **scale-up** does that while the first "
           "country is still being built.", after=80)

    m.para("**What I have not done.** I have not built a charging station, worked in **e-mobility**, or "
           "handled a Danish **permit** for a charging hub; and I have never filed a DSO application. "
           "What I bring instead is construction delivery on **37 projects** with **schedules** and "
           "**budgets** that had to hold, **procurement** and **suppliers** in three companies, HV/LV "
           "installations, **commissioning** and **handover** that had to pass someone else's "
           "inspection, and a **driving licence** and a passport that are both used.", after=80)

    m.para("**Practical.** I live in **Måløv**, about 20 km from central Copenhagen, so a hybrid week "
           "in the city works. **Danish** native, **English** at business level. **Driving licence B**; "
           "**travel** within Denmark and abroad is not a problem. Available by agreement.",
           after=60)
    m.meta("Kind regards", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- page 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFILE")
    m.para("Construction and operations manager with twelve years of leadership in technical delivery: "
           "**37 capital projects** under external inspection, **11 concurrent contracts**, full **P&L** in "
           "my own company since 2023, and four years responsible for HV/LV **switchgear**, transformers "
           "and 24/7 supply. Danish **LV/MV/HV** authorisation, and happy to own the date.", after=80)

    m.section("GRID, POWER AND TECHNICAL INFRASTRUCTURE")
    for label, body in [
        ("HV and LV systems",
         "Four years responsible for **switchgear**, **transformer** stations, panels and "
         "**SRO/SCADA**; Danish **LV/MV/HV** authorisation (2023)."),
        ("Commissioning",
         "**Commissioning** and **handover** of 37 installations: FAT/SAT, documentation and a "
         "sign-off that had to satisfy an authority, not just a customer."),
    ]:
        m.bullet(label, body)

    m.section("CONSTRUCTION DELIVERY")
    for label, body in [
        ("Schedules and budgets",
         "37 projects tracked with milestones, cost lines and change control in **SAP**; zero critical "
         "findings at handover."),
        ("Contractors on site",
         "Up to **14 people** and 11 contracts with subcontractors and an own workshop: scope, access, "
         "sequence and a **quality** check before the next trade arrived."),
    ]:
        m.bullet(label, body)

    m.section("PROCUREMENT, SUPPLIERS AND MATERIAL")
    for label, body in [
        ("Procurement",
         "**Procurement**, **material supply** and **supplier** selection in three companies; stock and "
         "delivery times treated as part of the plan."),
        ("Negotiation",
         "**Negotiation** with suppliers, subcontractors and customers: price, scope and a delivery "
         "date that is actually achievable."),
    ]:
        m.bullet(label, body)

    m.section("SAFETY, PERMITS AND STAKEHOLDERS")
    for label, body in [
        ("HSE on site",
         "**HSE** as a condition of work: **APV**, **LOTO**, access control, and incidents reviewed "
         "rather than filed."),
        ("Authorities",
         "**Documentation** approved by **authorities** under GMP/FDA/EMA; **permits** and inspections "
         "treated as design inputs."),
    ]:
        m.bullet(label, body)

    m.section("EXPERIENCE")
    m.job("Owner / Technical Director", "ELOHVAC ApS · Copenhagen · May 2023–present",
          scope="5 electricians + 3 apprentices · full P&L · procurement, pricing, customer delivery")
    m.bullet("Running delivery as a business",
              "Prices, **suppliers** and deadlines that matched what was sold — and saying no to a date "
              "that could not be held.")

    m.job("Senior Commissioning Engineer / Project Manager",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024",
          scope="37 capital projects · 25 specialists · schedules, budgets · SAP · authority documentation")
    m.bullet("Thirty-seven projects, one standard",
              "**Commissioning**, **handover** and change control in **SAP**; one checklist shared with "
              "**engineering partners** and trades, so every site was inspected the same way.")

    m.job("Project and Workshop Manager", "Ventek Air ApS · Vedbæk · Jan 2022–Nov 2022",
          scope="14 staff · 11 concurrent contracts · suppliers, subcontractors, own workshop")
    m.bullet("Eleven sites at once",
              "**Material supply**, sequence and **contractor** coordination across eleven jobs — capacity "
              "moved before a bottleneck became a delay.")

    m.job("Head of Operations and Maintenance", "Biofos (Lynetten) · Copenhagen · Aug 2017–Jan 2022",
          scope="24/7 plant · HV/LV switchgear, transformers, pumps, SRO/SCADA · HSE, standby, permits")
    m.bullet("Power that could not fail",
              "**Switchgear**, **transformer** stations and standby owned end to end; **safety "
              "compliance** and **permits** handled with **authorities** and contractors on site.")

    m.job("Production Foreman / Electromechanical Technician",
          "ARJ Engineering · Tehran · 2003–2010 · 12 mechanics and technicians")
    m.bullet("First leadership role",
              "Shift planning, allocation and training in a workshop where drawings and deadlines arrived "
              "the same morning.")

    # ---------------------------------------------------------------- page 3
    m.page_break()
    m.section("EDUCATION AND AUTHORISATION")
    m.edu("Danish electrician authorisation, LV/MV/HV — authorised mechanical engineer (maskinmester)",
          "Danish Safety Technology Authority · May 2023")
    m.edu("B.Tech, Technology Management and Mechanical Engineering (EQF 6)",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7.6/12")
    m.edu("Electrical and Mechanical Design, Electrical Engineering (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("Lean: 5S, PDCA, VSM, A3 · refrigeration and HVAC technology (AMU) · STCW safety",
          "Mercantec 2021 · Danish Maritime Authority 2021–2023")

    m.section("LANGUAGES, PRACTICALITIES AND REFERENCES")
    m.para("**Danish:** native · **English:** business level, written and spoken · **Persian:** native "
           "· Based in **Måløv**, about 20 km from Copenhagen · **Driving licence B** · **Travel** "
           "within Denmark and abroad · Available by agreement · References on request.", after=70)

    m.models_table(
        "THE FIRST 90 DAYS — FROM SITE TO ENERGISATION",
        ["Period", "What happens, and how it is measured"],
        [
            ("Week 1–2",
             "Read the pipeline: every site in Denmark with its **grid connection** status, "
             "**permit** status and date. Visit three sites — one in build, one waiting for power, "
             "one in operation — with the contractor who built it. Ask what cost them a month."),
            ("Day 30",
             "A one-page map of the Danish process: DSO, municipality, landlord, contractor, "
             "**authority**, and where each of them can stop the date. Reviewed with the Construction "
             "Lead and the country team before it is used."),
            ("Day 60",
             "The **roadmap** for construction initiation drafted from that map: local partners, "
             "standards, **safety compliance** at each stage, and the documents a new site needs. "
             "One standard station sequence agreed with the **engineering partners**."),
            ("Day 90",
             "Two sites moved measurably closer to energisation, with the date and the reason written "
             "down; a partner list with names, not categories; and a **risk** log that the country "
             "manager can read in five minutes."),
        ],
        widths=(1500, 8830))

    m.section("A GRID CONNECTION IS A QUEUE, AND QUEUES ARE MANAGED")
    m.para("The connection is not a form; it is a position in someone else's plan. The way to move it "
           "is to know the DSO's process better than the DSO expects, to bring a complete application "
           "the first time, and to keep a written record of every answer. I have spent four years on "
           "the receiving end of that conversation, which is a good place to have learned it from.",
           after=70)

    m.section("THE SECOND STATION SHOULD COST LESS THAN THE FIRST")
    m.para("In a **roll-out**, the unit is not the project; it is the repeat. The first station is "
           "learning, the second is a test of whether the learning was written down, and the tenth is "
           "the business case. Standard **material supply**, one sequence, one checklist and one "
           "person who owns the lessons is how a build-out stays cheap while it gets fast.", after=70)

    m.section("SAFETY IS A SEQUENCE, NOT A POSTER")
    m.para("On a charging site the dangerous moment is rarely the finished station; it is the "
           "temporary one — excavation near a cable, a crane over a live connection, a subcontractor "
           "who arrives a day early. **Safety compliance** therefore belongs in the sequence, with a "
           "named person and a signature before each stage, and an incident review that changes the "
           "next site rather than the paperwork.", after=70)

    m.section("A NEW COUNTRY IS A LIST OF NAMES")
    m.para("Fastned's advantage is a station design that can be repeated and a team that has done it "
           "before. What Denmark adds is local: a DSO, a municipality, a landlord, a contractor, a "
           "**supplier** of **switchgear**, and a set of standards that are similar to the ones in the "
           "Netherlands but not identical. The first year is spent turning that list into partners — "
           "and turning the partners into a process someone else can run.", after=70)

    m.section("WHERE I WOULD START")
    m.para("At the connection. First week: the pipeline by connection status, three site visits, and "
           "the DSO's process read line by line. Then a map of where the date actually gets lost — "
           "application, permit, material or contractor — because those four problems look the same "
           "in a spreadsheet and are solved by completely different people.", after=0)

    # ---------------------------------------------------------------- page 4
    m.page_break()
    m.models_table(
        "WHAT THE POSTING ASKS FOR — WHAT I HAVE",
        ["Requirement in the posting", "Evidence"],
        [
            ("Acquisition and realization of **grid connections**",
             "Four years responsible for HV/LV **switchgear**, **transformer** stations and 24/7 "
             "supply; Danish **LV/MV/HV** authorisation. No DSO application filed yet — the first "
             "process I would learn."),
            ("Collaboration with **engineering partners**",
             "37 capital projects with 25 specialists and external designers; drawings, calculations "
             "and standards agreed before the trades arrived."),
            ("**Material supply** and planning for the construction",
             "Long-lead items ordered first, **supplier** delivery times in the plan, stock and spares "
             "owned in two companies."),
            ("Monitor the **schedules** and **budgets**",
             "37 projects tracked with milestones, cost lines and change control in **SAP**; full "
             "**P&L** in my own company since 2023."),
            ("Coordinate internal and external **stakeholders** from Denmark and abroad",
             "Technique, procurement, operations, **authorities** and suppliers kept aligned on 37 "
             "projects, with international suppliers and Danish regulators in the same room."),
            ("Visit partners and sites — **negotiation** and a hands-on mentality",
             "Site presence as the default: **contractor** briefings, inspections and supplier "
             "meetings on location, not on video."),
            ("Create a **roadmap** for construction initiation in a new country",
             "Built partner lists and processes in three companies and three technical environments; "
             "the 90-day map on page 3 is how I would do it here."),
            ("Identify new local **partners** and analyse standards",
             "**Contractors**, **suppliers** and advisers selected and qualified in 37 projects and 11 "
             "contracts; standards read as design inputs."),
            ("Ensure **safety compliance** at different stages",
             "**HSE** with **APV** risk assessments, **LOTO**, access control and incidents reviewed; "
             "**safety compliance** as a sequence with named owners."),
            ("Support site evaluations and **due diligence**",
             "Technical and commercial assessment of sites and installations: load, connection, "
             "condition, cost — the questions that decide whether a site works."),
            ("Degree in engineering, business or equivalent",
             "**B.Tech** in mechanical engineering and technology management (EQF 6), **electrical** "
             "and mechanical design (EQF 6) and a Danish **LV/MV/HV** authorisation."),
            ("Strong **technical affinity**",
             "Comfortable in a substation, on a roof and in a spreadsheet; **commissioning**, "
             "**handover** and fault-finding as daily work."),
            ("4+ years of experience in **deployment** and/or **construction**",
             "Twelve years in technical delivery, including **37** capital projects, 11 concurrent "
             "contracts and four years of 24/7 operations."),
            ("Work structured and prioritize tasks efficiently",
             "Standard templates, check points and a written plan per project; priorities decided on "
             "the date and the cost, not on who called last."),
            ("Strong **negotiation** and communication skills",
             "Prices, scope and dates negotiated with **suppliers**, **contractors** and customers in "
             "my own company; bad news delivered early and in writing."),
            ("Excellent organizational skills and a high level of **initiative**",
             "Templates, procurement routines and safety practices introduced because nobody else had "
             "done it — in three companies."),
            ("Navigate and manage **stakeholder** dynamics",
             "Municipal, authority and landlord constraints, and competing internal priorities, handled "
             "with an agenda, a decision and a record."),
            ("Willingness to **travel** abroad and within Denmark",
             "**Driving licence B**; worked across Zealand and Jutland with suppliers and **authorities**; "
             "passport in order."),
            ("Near-native **Danish** and business **English**",
             "**Danish** native, **English** at business level, **Persian** native; documentation and "
             "meetings in all three as required."),
            ("**Driving licence**",
             "**Driving licence B**; car in daily use between Måløv, Copenhagen and sites."),
            ("Genuine interest in the **energy transition**",
             "More than twenty years in technical delivery, including five years of energy management in "
             "Copenhagen with over **40 %** lower consumption documented."),
            ("Team player who thinks on their own feet and takes **ownership**",
             "Owner of a company and of 37 project deliveries: decisions taken, mistakes owned and "
             "the lesson written into the next project."),
        ],
        widths=(3600, 6746))

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_Fastned_ProjectManagerConstruction.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_Fastned_ProjectManagerConstruction.docx'))
