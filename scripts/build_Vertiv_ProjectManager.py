# -*- coding: utf-8 -*-
"""Vertiv — Project Manager, Norway/Nordics (site based: Drangedal or Kristiansand).

English posting -> English document (en-GB). 4 pages: letter p1, CV p2, education + 90-day
plan + method sections p3, 18-row requirement matrix p4.

STILVALG (master/STILREGISTER.md; godkendt af scripts/style_guard.py, 3/3 skift mod #203):
  register      = UPTIME/KONTROLrum — nyt register: responstid, eskalering, alarm, hvem tager
                  telefonen, hvad der sker i det første kvarter. Passer til en virksomhed, hvis
                  produkt ER oppetid ("our solutions ensure that critical systems stay online no
                  matter what") og hvis adfærd er "Act with urgency".
  åbningsgreb   = E (tidsforskydningen) — "Den sidste uge af et datacenterprojekt bliver afgjort
                  i den første." Sidst #187, #195.
  struktur      = DAGSFORLØBET/UGEN — side 1 er mandag 06.40 til fredag eftermiddag på en
                  norsk kundeplads. Sidst #186 (dansk), #194.
  kadence       = korte, konstaterende sætninger, klokkeslæt som ledetråd, ingen tillægsord om
                  personen. Hver dag slutter i et bevis.

KULTURSYNKRONISERING (policy 04.11.2026): Vertiv's egne ord bærer teksten — *Own it*, *Act with
urgency*, *Foster a customer-first mindset*, *Lead by example*, *Drive continuous improvement*,
*transparent and open communication*, Core Principles (**Safety, Integrity, Respect, Teamwork,
Inclusion**), Strategic Priorities (**Customer focus, Operational excellence, High-performance
culture, Innovation, Financial strength**), *mission-critical*, *AC Power*, *Thermal*,
*Infrastructure Solutions*, *switchgear*, *busbar*. Kilder: opslaget selv + Vertiv's
responsible-business rapporter (core principles/behaviours/strategic priorities).

Forbehold (brugerens beslutning 04.11.2026, "dansk permanent resident"): én faktuel matrixrække +
én sætning i "Practicalities" om arbejdstilladelse. Ingen undskyldning, intet "endnu".
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Project Manager · AC power, thermal and commissioning on customer sites'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Copenhagen area'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4 November 2026")
    m.meta("Vertiv · Project Manager, Norway/Nordics · Site based in Drangedal or Kristiansand")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Application: Project Manager – Norway", bold=True, color='1A1A1A')

    # ---------------------------------------------------------------- page 1
    m.para("Dear Vertiv Northern Europe team,", after=60)

    m.para("**The last week of a data centre project is decided in the first one.** Not in the "
           "commissioning window, and not in the conversation about who caused the delay: in the "
           "week where the site is opened, the accesses are agreed, the contractors are briefed and "
           "someone writes down who owns the next step. Below is that week as I run it on a "
           "customer site in **Norway** — Monday morning to Friday afternoon, with the evidence "
           "after each day.", after=80)

    m.para("**Monday, 06.40.** On site before the first crew. I walk the route with the customer's "
           "site manager and the main contractor's supervisor: where material is laid down, where "
           "the isolation points are, which doors are locked at 16.00, and where the **switchgear**, "
           "the **UPS** and the **busbar** run sit relative to the cooling. The week's plan is one "
           "page, agreed before lunch, with one owner per line. That is what **Own it** looks like "
           "on a site: a name, not an intention.", after=80)

    m.para("**Tuesday, 08.00.** Installation starts. **Technical drawings** and **schematic**s "
           "against the floor as built: what can go in as drawn, and what needs an answer today. "
           "Two lists, both written before 11.00 — the questions go to the designer and the "
           "customer the same afternoon, because a question asked on Thursday has already cost two "
           "days. Materials, lifting, cable routes and clearances are checked against the **daily "
           "progress updates** the customer will read at 16.00.", after=80)

    m.para("**Wednesday, 14.10.** Something does not arrive. The delay is not the problem; the "
           "silence is. The escalation path was agreed on Monday, so the call goes out while there "
           "is still time to re-sequence: which crew can work, which delivery can be split, and "
           "which part of the programme can move without touching the **commissioning** date. "
           "Decision recorded, customer informed before they ask. **Act with urgency** means the "
           "same hour, not the same week.", after=80)

    m.para("**Thursday, 09.30.** Start-up and **testing**. The sequence is fixed: pre-checks, "
           "torque and terminations, insulation and continuity, energisation, witness. Every step "
           "has an acceptance criterion and a signature. On critical power nothing is energised "
           "because it is Thursday; it is energised because the test before it passed and the "
           "person who signed it is standing there.", after=80)

    m.para("**Friday, 15.00.** The customer meeting. Punch list closed or dated, the weekly report "
           "in writing, next week's look-ahead agreed with the contractor and the customer's "
           "**on-site representative** in the room. Then the part Vertiv calls **continuous "
           "improvement**: what cost us a day this week, and what the next site should copy. "
           "Transparent and open communication is not a value on a wall when the report says the "
           "truth about a bad Wednesday, and a **high-performance** culture is measurable on site "
           "by one thing: whether Thursday's test passes the first time.", after=80)

    m.para("**That week is not a template I have read about.** Twenty years on site: 37 concurrent "
           "CAPEX projects with schedule, budget and forecast in SAP ERP; eleven contracts running "
           "at once with a team of 14; five electricians and three apprentices in my own company "
           "since 2023 with full P&L; and four years responsible for a plant in 24/7 operation, "
           "where the only acceptable outage was a planned one.", after=80)

    m.para("**AC power and thermal are both on my record.** **UPS**, emergency and escape power, "
           "high-voltage **switchgear**, panels and distribution up to high voltage — and, from "
           "Ventek-Air and my refrigeration and HVAC training, ventilation and cooling delivered on "
           "contract: dimensioning, **installation**, balancing, handover. A data hall is those two "
           "systems arguing over the same square metres, and someone has to settle it on the floor.",
           after=80)

    m.para("**Keeping critical systems online no matter what** is the sentence your customers are "
           "actually paying for. On a site that means availability designed in: redundant paths that "
           "are genuinely separate, cooling that can be serviced without shutting the room, and a "
           "handover pack that tells the next engineer which breaker feeds what. That is the part of "
           "delivery I care about — not the day the equipment arrives, but the year afterwards when "
           "nothing has stopped.", after=80)

    m.para("**Practicalities.** Based in Måløv, twenty minutes from Copenhagen Airport and about "
           "1 h 20 from Oslo; **driving licence** B; willing to travel across **Norway** and the "
           "**Nordics** and to be on site from day one for as long as a mobilisation needs. "
           "**Fluent English**; native Danish, a **Nordic language**, and Norwegian read and "
           "understood on site. I hold permanent residence in Denmark, and the Norwegian work "
           "permit that follows an offer is a process I will run with your HR alongside the "
           "mobilisation, not after it.", after=60)
    m.meta("Kind regards", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- page 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFILE")
    m.para("Site-based project manager in **critical infrastructure**: authorised marine and "
           "mechanical engineer at **LV/MV/HV** level, **electrical engineering** and mechanical "
           "design (EQF 6), B.Tech in technology management. Twenty years of **planning**, "
           "installation, start-up, **commissioning** and **handover** on live sites; 37 concurrent "
           "CAPEX projects; eleven contracts with a team of 14; full P&L since 2023.", after=80)

    m.section("SITE DELIVERY")
    for label, body in [
        ("Mobilisation",
         "Access, laydown, isolation points, RAMS and permits agreed before the first crew arrives; "
         "a one-page week plan with one owner per line."),
        ("Contractors and crews",
         "Subcontractors steered on the floor, not from a site office; 14-person contract team; five "
         "electricians and three apprentices; toolbox talks before every shift."),
        ("Reporting",
         "**Daily progress updates** in writing, weekly look-ahead agreed with customer and "
         "contractor, decisions recorded and dated so nobody re-argues them."),
    ]:
        m.bullet(label, body)

    m.section("AC POWER, THERMAL AND CONTROLS")
    for label, body in [
        ("Power",
         "**UPS**, emergency and escape power, HV **switchgear**, panels and distribution up to high "
         "voltage; energisation sequences, torque control and witness points per step."),
        ("Cooling",
         "Ventilation and HVAC delivery with 14 people and 11 contracts at Ventek-Air; refrigeration "
         "and HVAC (AMU); dimensioning, installation and balancing on site."),
        ("Controls",
         "SCADA, BMS and automation interfaces; alarm lists, escalation paths and what a site does "
         "in the first fifteen minutes."),
    ]:
        m.bullet(label, body)

    m.section("RESPONSE AND ESCALATION")
    for label, body in [
        ("Response time",
         "Escalation path agreed before the first shift; a call at 16.30 gets a decision, not a "
         "promise. Customer hears bad news from us first."),
        ("Live plant",
         "Four years of 24/7 operation: outages planned into narrow windows with the fallback "
         "designed before it was needed."),
        ("Documentation",
         "**Technical drawings** and **schematic**s marked up as built; test records and handover "
         "packs that stand up in an audit."),
    ]:
        m.bullet(label, body)

    m.section("EXPERIENCE")
    m.job("Owner / Technical Director", "ELOHVAC ApS · Copenhagen · May 2023–present",
          scope="5 electricians + 3 apprentices · full P&L · installation and handover")
    m.bullet("Site delivery and commercial risk",
              "Projects from quotation to handover with own budget and own risk; subcontractors, "
              "materials and QA — and the discipline to decline work that cannot be delivered.")

    m.job("Senior Commissioning Engineer / Project Manager",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024",
          scope="Electrical systems · 37 concurrent CAPEX projects · 25 specialists · GMP/FDA/EMA")
    m.bullet("Start-up, testing and acceptance",
              "Project basis, milestones and monthly reporting in SAP ERP; FAT/SAT and IQ/OQ/PQ with "
              "protocols written before the test — zero critical findings at handover.")

    m.job("Project and Workshop Manager", "Ventek-Air · Copenhagen · Jan 2022–Nov 2022",
          scope="14 employees · 11 concurrent contracts · DKK 2–10 m each · ventilation and cooling")
    m.bullet("Thermal delivery under pressure",
              "Daily board meetings and bottleneck analysis; crews and suppliers moved between "
              "contracts when one ran behind, with the customer informed the same day.")

    m.job("Maintenance and Operations Manager", "Biofos (Lynetten) · Copenhagen · Aug 2017–Jan 2022",
          scope="Treatment plant in 24/7 operation · pumps, HVAC, HV switchgear, SCADA")
    m.bullet("Live plant, planned outages",
              "Preventive maintenance and fault-finding around the clock; outages planned into "
              "narrow windows with temporary solutions ready before they were needed. LOTO and APV.")

    m.job("Electromechanical Technician / Production Team Leader",
          "ARJ Engineering · Tehran · Dec 2003–Mar 2010 · 12 mechanics and technicians")

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
    m.para("**English:** fluent, written and spoken · **Danish:** native, a **Nordic language** · "
           "**Persian:** native · **Based in Måløv**, 20 minutes from Copenhagen Airport, about 1 h 20 "
           "from Oslo · **Driving licence B**, ready to travel across **Norway** and the **Nordics** "
           "· **Available at short notice** · References on request.", after=70)

    m.models_table(
        "FIRST 90 DAYS — FROM THE FIRST SITE VISIT TO THE FIRST ACCEPTED DELIVERY",
        ["Period", "What happens, and how it is measured"],
        [
            ("Week 1–2",
             "Read every live project in the portfolio — schedule, scope, open punch items — and be "
             "on the two nearest sites in Norway with the contractors and the customer's "
             "representative."),
            ("Day 30",
             "Own one delivery end to end: week plan with one owner per line, an escalation list with "
             "names and numbers, and the customer report in Vertiv's format."),
            ("Day 60",
             "Cost and progress reviewed weekly on every project I hold; **commissioning** dated with "
             "witnesses booked, and the punch list empty at the point of handover."),
            ("Day 90",
             "First delivery accepted by the customer, with test records, as-builts and lessons "
             "written into the next mobilisation."),
        ],
        widths=(1500, 8830))

    m.section("IN THE FIRST FIFTEEN MINUTES, THE PHONE LIST DECIDES")
    m.para("When something trips at 07.15 on a live site, nobody needs a strategy. They need to know "
           "who to call, who can authorise an isolation, and where the spare is. So that list is "
           "written at mobilisation, printed, and tested: I ring it once before the first energisation "
           "to make sure a human answers. On a plant in 24/7 operation I have been the person on the "
           "other end of that call, and it changes how you write the list.", after=70)

    m.section("A COMMISSIONING SEQUENCE IS NOT A CEREMONY")
    m.para("Commissioning has an order for a reason: the test that could fail comes before the "
           "energy that could hurt. Pre-checks, terminations and torque, insulation, continuity, "
           "then energisation with a witness who signs. When a project is late, the pressure is "
           "always to compress that order. The answer is not to compress it — it is to parallelise "
           "what can run in parallel and to say out loud, in the meeting, which step will not be "
           "skipped and why.", after=70)

    m.section("A SMALL UPGRADE IS NOT A SMALL PROJECT")
    m.para("A two-day upgrade on a live site can stop more than a three-month build, because the build "
           "gets a shutdown window and the upgrade has to happen while everything else keeps "
           "running. So the small job gets the same treatment: isolation plan, fallback, witness, "
           "and the customer's signature before the first cable is touched. The size of the invoice "
           "has nothing to do with the size of the consequence — and the customer who watches you "
           "take a two-day job seriously is the customer who calls you for the large one.",
           after=70)

    m.section("WHEN THE CREW BELONGS TO SOMEONE ELSE, AUTHORITY IS WRITTEN")
    m.para("On a customer site the people in front of me often belong to another company. Then "
           "authority is not something I assume, it is something agreed at mobilisation: who can "
           "call a stop-work, who signs a permit, who speaks to the end customer's operations team, "
           "and what happens if the contractor's supervisor and I disagree at 15.00 on a Friday. It "
           "goes into the site rules in week one, so that nobody has to negotiate it in the middle of "
           "an energisation. Least glamorous document on the site, and the one that prevents the "
           "worst meeting.", after=70)

    m.section("TRAVEL IS PART OF THE DELIVERY, NOT A TAX ON IT")
    m.para("Site based in Drangedal or Kristiansand, then across the **Nordics**: that means Monday "
           "morning on site, not Monday afternoon at a desk. I plan the travel the way I plan a "
           "mobilisation — the week's site days fixed, the admin done outside them, and the crew "
           "knowing which day I am physically there and which day I am on the phone at 16.00 with "
           "the same information.", after=0)

    # ---------------------------------------------------------------- page 4
    m.page_break()
    m.models_table(
        "WHAT THE ROLE REQUIRES — WHAT I HAVE DELIVERED",
        ["Requirement in the posting", "Evidence"],
        [
            ("Lead and coordinate project delivery across key customer sites in Norway",
             "Site-based delivery for twenty years: 11 concurrent contracts with 14 people, 37 CAPEX "
             "projects, and own projects as contractor since 2023."),
            ("Manage planning, installation, start-up, commissioning and testing",
             "The full sequence in own company and on 37 projects: **planning**, installation, "
             "start-up, FAT/SAT and IQ/OQ/PQ — zero critical findings at handover."),
            ("Act as the company's on-site representative for customers and contractors",
             "One voice on site for customer, contractor and own crews; **daily progress updates** "
             "in writing and decisions recorded the day they are taken."),
            ("Ensure all works meet quality, safety and compliance standards",
             "LOTO, risk assessment at mobilisation, safety walks and near-miss follow-up; GMP/FDA "
             "documentation and KS on regulated sites."),
            ("Daily progress updates and clear communication with **stakeholders**",
             "Daily written updates and weekly look-ahead agreed with the customer's representative; "
             "bad news delivered with a plan, not an apology."),
            ("Collaborate with cross-functional teams to deliver on time and within scope",
             "**Cross-functional** delivery across engineering, procurement and site; scope held by a "
             "written baseline, changes priced before they are built."),
            ("Build **customer relationships** and identify improvement or **added value**",
             "Repeat customers in own business and long contract relationships; **customer-first** in "
             "practice means every improvement is offered with a price and a date, so the customer "
             "can say yes."),
            ("Qualification in **electrical engineering** or mechanical engineering (degree or equivalent)",
             "Authorised marine and mechanical engineer (LV/MV/HV), electrical and mechanical design "
             "(EQF 6), B.Tech in technology management."),
            ("5+ years managing technical or construction projects, ideally **critical infrastructure** or **data centre**",
             "Twenty years: 24/7 plant operation, GMP-regulated build, and own contracting business. "
             "Critical infrastructure rather than data halls specifically — same consequence of "
             "downtime."),
            ("Strong electrical knowledge and experience with **AC power** and **thermal** systems",
             "**UPS**, emergency power, HV **switchgear**, panels and distribution; ventilation, "
             "HVAC and refrigeration delivered as contracts, including balancing and handover."),
            ("Excellent organisational, leadership and communication skills",
             "25 specialists led across engineering, procurement and operations; a 14-person contract "
             "team; written mandates and one-page week plans."),
            ("Read and interpret **technical drawings** and **schematic**s",
             "Drawings and schematics read against the floor, marked up as built, and used to raise "
             "questions before they become delays."),
            ("**Microsoft Office** and **project management tools**",
             "**MS Project** and Monday for schedule and look-ahead; Excel and SAP ERP for cost and "
             "progress; own **AI** tools for reporting and checklists."),
            ("Willing to travel extensively in **Norway** and the **Nordics**",
             "Site based, driving licence B, 1 h 20 from Oslo; travel planned as part of the week, "
             "not around it."),
            ("Valid **driving licence**, **fluent English**, **Nordic language** an advantage",
             "Licence B; fluent English written and spoken; native Danish — a Nordic language — with "
             "Norwegian read and understood on site."),
            ("From smaller upgrades to large-scale builds: **AC power**, **thermal**, infrastructure, **switchgear**, **busbar**",
             "DKK 2–10 m contracts to 37-project portfolios; switchgear, distribution, ventilation and "
             "cooling. **Busbar** is the same discipline: torque, clearances, test."),
            ("Hands-on role for a strong electrical background; core principles and behaviours",
             "On the floor, not in a site office. **Safety** first on every mobilisation, **Integrity** "
             "in the report, **Respect** for the crew that has to build it, **Teamwork** with the "
             "contractor, and **Own it** with a name on every line."),
            ("Site based in Drangedal or Kristiansand, able to relocate; no visa sponsorship",
             "Permanent residence in Denmark, 1 h 20 from Oslo, on site from day one. The Norwegian "
             "permit that follows an offer is a process I will run with Vertiv's HR alongside "
             "mobilisation, not after it."),
        ],
        widths=(3600, 6746))

    m.section("WHERE I WOULD START")
    m.para("On the two nearest sites, with the person who hands over the portfolio. First week: read "
           "the open punch items, the last three customer reports and the escalation list of every "
           "project I am given, and check that the names on the list still answer their phones. Then "
           "walk one site with the contractor and one with the customer's representative — because "
           "the gap between those two walks is the whole job.", after=0)

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_Vertiv_ProjectManager.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_Vertiv_ProjectManager.docx'))
