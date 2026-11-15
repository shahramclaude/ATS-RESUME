# -*- coding: utf-8 -*-
"""Eaton — Data Center Project Manager, Copenhagen (EMEA Projects).

English posting → English document (en-GB): letter p1, CV p2, education + 90-day plan +
three sections p3, requirement matrix p4.

STILVALG (master/STILREGISTER.md; godkendt af scripts/style_guard.py, 3/3 skift mod #202):
  register      = MARITIM/OFFSHORE — regime, window, safe delivery, crew. Ikke en kostume her:
                  uddannelsen er maskinmester (Copenhagen School of Marine Engineering), STCW-kurser
                  og tyve år med anlæg, der ikke må stoppe. Sproget er "no window without power".
                  Sidst brugt #188.
  åbningsgreb   = J (BREVET) — direkte tiltale til Eaton EMEA Projects, uden om rammen.
                  Sidst brugt: aldrig i denne log (frisk).
  struktur      = DOKUMENTERNE — seks dokumenter, der afgør et datacenterprojekt: scope baseline ·
                  schedule · risk register · cost forecast and variation log · SAT script ·
                  handover pack. Sidst brugt #189.
  kadence       = korte, konstaterende sætninger; ét dokument pr. afsnit; ingen tillægsord om personen.

KULTURSYNKRONISERING (policy 04.11.2026): Eaton's egne begreber bærer teksten — *doing business
right*, *Eaton Business System (EBS)*, *MESH* og *zero-incident safety culture*, *high-performance
culture*, *continuous improvement* / *lessons learned*, *engineered-to-order*, *single point of
contact*, *mission critical*. Kilder: eaton.com (mission, code of ethics, EHS/MESH-policy),
opslaget selv (DCIM/EPMS, MV/LV, UPS, batterier, SAT, EMEA Projects).

Ingen opdigtede fakta. Dokumenteret grundlag: elautoriseret maskinmester LV/MV/HV, el- og
maskinteknisk design (EQF 6), B.Tech; 37 samtidige CAPEX-projekter med budget/prognose i SAP ERP,
FAT/SAT og IQ/OQ/PQ med nul kritiske fund; 11 entrepriser med 14 mand; Lynetten i 24/7-drift med
pumper, HVAC, højspændingstavler og SCADA; fuldt P&L i egen virksomhed siden 2023; MS Project,
Monday og egenudviklede AI-værktøjer.

Policy: master/README.md — job first, candidate only as evidence, no reservations.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Data Center Project Manager · Power, commissioning and handover'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Copenhagen area'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4 November 2026")
    m.meta("Eaton · Data Center Project Manager, EMEA Projects · Copenhagen, Denmark")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Application: Data Center Project Manager", bold=True, color='1A1A1A')
    m.para("To Eaton EMEA Projects", after=70)

    # ---------------------------------------------------------------- page 1
    m.para("Dear EMEA Projects team,", after=60)

    m.para("**A data centre project is decided long before the first UPS is energised** — in the "
           "documents that state what was sold, what will be built, and who signs when it is done. "
           "Your project managers own that chain from purchase order to handover, across **medium "
           "voltage** and **low voltage** distribution, **UPS** and **batteries**, and the "
           "**DCIM**/**EPMS** layer that has to talk to all of it. I have run that chain for twenty "
           "years: electrical scope, **commissioning**, and the discipline of never taking a system "
           "offline that someone depends on.", after=80)

    m.para("Below are the six documents I would own on a **data center** project, and what I bring "
           "to each.", after=80)

    m.para("**1 · The scope baseline.** What the purchase order covers and what the customer heard "
           "are rarely the same sentence. On a **data center** the gap sits in the interfaces — "
           "between **switchgear** and **UPS**, between batteries and controls, between the plant "
           "and the **DCIM** that is meant to see it — in drawings and **schematics** that have to agree "
           "with the panels as built. My first document names those interfaces and the boundary, so the kick-off is about method, not about what was sold. I closed that "
           "gap on 37 concurrent CAPEX projects across engineering, **procurement** and site.",
           after=80)

    m.para("**2 · The schedule.** A schedule that lives only in the planning tool is a wish. I keep "
           "an eight-to-twelve week look-ahead with dependencies, deliveries and hold points, "
           "review it weekly, and report daily from site once the work is live. **MS Project** and "
           "**Monday** are the tools; the rule is one task, one owner, one date — and the "
           "**customer** hears about a slip from us, before they see it.", after=80)

    m.para("**3 · The risk register.** A risk is not a worry; it is an entry with an owner, a "
           "trigger and a date. Four years of 24/7 operation on a treatment plant taught me what an "
           "unplanned outage actually costs, so outages were planned into narrow windows with the "
           "temporary solution designed before it was needed. That is the same habit a live data "
           "hall demands: you do not discover your fallback during the switchover.", after=80)

    m.para("**4 · The cost forecast and the variation log.** Margin on an **engineered-to-order** "
           "project is lost in the small changes nobody priced. Every variation is priced, owned "
           "and approved in the week it appears, the monthly **forecast** reflects it, and the "
           "customer sees the number before it becomes an invoice. I ran that on 37 projects in SAP "
           "ERP, and I run it now with my own P&L.", after=80)

    m.para("**5 · The SAT script.** **Commissioning** is where a project proves itself or finds its "
           "excuses. I write the test before the test: FAT/SAT protocols, IQ/OQ/PQ documentation and "
           "acceptance criteria agreed with the **customer** and **quality** records that stand up in an "
           "audit, with findings closed by root cause. Zero critical findings at **handover** is not "
           "luck — it is the result of hold points witnessed by someone who signs.", after=80)

    m.para("**6 · The handover pack — and the lessons.** **Handover** is a document set, not a "
           "handshake: as-builts, test records, punch list closed, training done, warranty clear. "
           "Then the part Eaton calls **continuous improvement**: what went wrong, what we would do "
           "differently, and what the next project should copy. I build the templates and dashboards "
           "that make that sharing happen instead of being remembered.", after=80)

    m.para("**Safety as a condition of employment** and a **zero-incident** culture are not lines I "
           "need persuading of; they describe how a site has to be run when the equipment is live. "
           "That is also why the **Eaton Business System** way of working — **lessons learned** "
           "shared, not stored — is the part of this role I would use most.", after=80)

    m.para("I am based in Måløv, twenty minutes from Copenhagen, and 50 % travel between customer "
           "construction sites suits me; I hold a driving licence and can work and travel across "
           "**EMEA**. Languages: professional English, native Danish, Persian. I can start at short "
           "notice.", after=60)
    m.meta("Kind regards", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- page 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFILE")
    m.para("Project and commissioning manager with twenty years in **critical infrastructure**: "
           "authorised marine and mechanical engineer at **LV/MV/HV** level, electrical and mechanical design "
           "(EQF 6) and a B.Tech in technology management. 37 concurrent CAPEX projects with schedule, "
           "budget and **forecast** in SAP ERP, 11 contracts with a team of 14, FAT/SAT and IQ/OQ/PQ "
           "with zero critical findings, plus full P&L since 2023.", after=80)

    m.section("POWER, COMMISSIONING AND HANDOVER")
    for label, body in [
        ("Electrical systems",
         "**Switchgear**, panel and **power distribution** work up to high voltage; UPS, emergency "
         "and escape lighting, fire alarm and access control, **automation** and SCADA interfaces."),
        ("Commissioning and SAT",
         "FAT/SAT protocols written before the test, IQ/OQ/PQ documentation, acceptance criteria "
         "agreed with the customer; findings closed by root cause, not by explanation."),
        ("Handover",
         "Handover packs with as-builts, test records and punch list closed; training delivered and "
         "warranty handover agreed — zero critical findings at acceptance."),
    ]:
        m.bullet(label, body)

    m.section("SCHEDULE, RISK AND COST CONTROL")
    for label, body in [
        ("Schedule and look-ahead",
         "Eight-to-twelve week look-ahead with dependencies and hold points; weekly review and daily "
         "site reporting. **MS Project** and **Monday** in daily use."),
        ("Risk and mitigation",
         "**Risk register** with owner, trigger and date; outages planned into narrow windows with "
         "temporary solutions designed in advance, proven in 24/7 operation."),
        ("Cost, margin and variations",
         "Budget and **forecast** monthly in SAP ERP on 37 projects; **variations** priced, owned and "
         "approved in the week they arose; full P&L in own company since 2023."),
    ]:
        m.bullet(label, body)

    m.section("TEAM LEADERSHIP AND STAKEHOLDERS")
    for label, body in [
        ("Teams, internal and external",
         "25 specialists across engineering, procurement and operations; a 14-person contract team; "
         "written mandates, not verbal ones."),
        ("Single point of contact",
         "One voice for the customer on site: daily **progress updates**, decisions recorded, and bad "
         "news delivered with a plan rather than an apology."),
        ("Site safety",
         "LOTO, risk assessment at mobilisation, safety walks and near-miss follow-up; briefings "
         "before every shift change on live plant."),
    ]:
        m.bullet(label, body)

    m.section("EXPERIENCE")
    m.job("Owner / Technical Director", "ELOHVAC ApS · Copenhagen · May 2023–present",
          scope="5 electricians + 3 apprentices · full P&L · design, installation and handover")
    m.bullet("Delivery and commercial responsibility",
              "Projects from quotation to handover with own budget and own risk; subcontractors, "
              "material control and QA — and the decision to decline work that would not carry.")

    m.job("Senior Commissioning Engineer / Project Manager", 
          "Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024",
          scope="Electrical systems · 37 concurrent CAPEX projects · 25 specialists · GMP/FDA/EMA")
    m.bullet("Commissioning in a regulated plant",
              "Project basis, milestones and monthly reporting in SAP ERP; FAT/SAT and IQ/OQ/PQ with "
              "protocols written before the test — zero critical findings at handover.")

    m.job("Project and Workshop Manager", "Ventek-Air · Copenhagen · Jan 2022–Nov 2022",
          scope="14 employees · 11 concurrent contracts · DKK 2–10 m each")
    m.bullet("Parallel delivery under pressure",
              "Daily board meetings and bottleneck analysis; crews and suppliers moved between jobs "
              "when one ran behind, with the customer informed the same day.")

    m.job("Maintenance and Operations Manager", "Biofos (Lynetten) · Copenhagen · Aug 2017–Jan 2022",
          scope="Treatment plant in 24/7 operation · pumps, HVAC, HV switchgear, SCADA")
    m.bullet("Live plant, planned outages",
              "Preventive maintenance and fault-finding around the clock; outages planned into narrow "
              "windows, temporary solutions ready before they were needed. LOTO and APV.")

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
    m.para("**English:** professional, written and spoken · **Danish:** native · **Persian:** native · "
           "**Based in Måløv**, 20 minutes from Copenhagen · **Driving licence B**, able to travel "
           "across **EMEA** · **Available at short notice** · References on request.", after=70)

    m.models_table(
        "FIRST 90 DAYS — FROM HANDOVER OF THE FILE TO THE FIRST HANDOVER TO THE CUSTOMER",
        ["Period", "What happens, and how it is measured"],
        [
            ("Week 1–2",
             "Read the live projects in the portfolio: scope baseline, **schedule**, **risk "
             "register** and the last approved variation on each. Walk two sites with the engineers "
             "and the customer's representative."),
            ("Day 30",
             "Own one project end to end: look-ahead agreed with the customer, hold points defined, "
             "and the interface list — **switchgear**, **UPS**, batteries, **DCIM** — signed off by "
             "all parties."),
            ("Day 60",
             "Weekly cost and **forecast** review in the EMEA format; variation log live on every "
             "active project, and a **SAT** script written for the next commissioning window."),
            ("Day 90",
             "First **handover** completed to the customer's acceptance, with test records, punch "
             "list closed and lessons written into the next project's plan."),
        ],
        widths=(1500, 8830))

    m.section("A SAT SCRIPT IS WRITTEN BEFORE THE EQUIPMENT ARRIVES")
    m.para("The moment to decide what \"tested\" means is when the equipment is still in the factory, "
           "not when the site is full of people waiting for a signature. So the acceptance criteria "
           "are agreed with the customer first, the test protocol is written from those criteria, and "
           "the witnesses are booked before the window opens. I have written protocols that later had "
           "to be defended in an audit; the ones that survived were the ones written first.", after=70)

    m.section("MISSION-CRITICAL MEANS PLANNING THE OUTAGE, NOT THE RECOVERY")
    m.para("On a plant that must not stop, you do not plan the repair — you plan the outage: which "
           "loads move, which bypass is in place, who signs the switching schedule, and what happens "
           "if the temporary supply fails at 03:00. That thinking is what a live data hall needs "
           "during a **commissioning** window, and it is the part of my background I trust most: four "
           "years of 24/7 operation where the fallback was designed before it was needed.", after=70)

    m.section("THE LONGEST LEAD TIME IS THE ONE NOBODY BOOKED")
    m.para("Switchgear, transformers and batteries are not bought when the site is ready; they are "
           "booked when the order is confirmed, and the delivery slot is the real start date of the "
           "**commissioning** plan. So the procurement list is built backwards from the energisation "
           "date: factory witness test booked, shipping slot confirmed, storage and lifting capacity "
           "on site agreed with the **customer**, and the access route checked against what actually "
           "arrives. The projects that run late are rarely the ones with the hardest engineering — "
           "they are the ones that discovered a 16-week lead time in week two.", after=70)

    m.section("THE INTERFACES ARE WHERE THE MARGIN GOES")
    m.para("Most of the money on an **engineered-to-order** project is not lost in the equipment; it "
           "is lost in the interfaces between packages — a control signal nobody owned, a battery "
           "room dimension that moved, a **DCIM** point list that arrived after the panels were "
           "built. Naming those interfaces early, in writing, with an owner for each, is unglamorous "
           "work that shows up directly in **margins** and in how calm the last month of a project "
           "feels.", after=0)

    # ---------------------------------------------------------------- page 4
    m.page_break()
    m.models_table(
        "WHAT THE ROLE REQUIRES — WHAT I HAVE DELIVERED",
        ["Requirement in the posting", "Evidence"],
        [
            ("Bachelor's or Master's degree (or equivalent) in Electrical Engineering",
             "Authorised marine and mechanical engineer (LV/MV/HV), electrical and mechanical design "
             "(EQF 6), B.Tech in technology management."),
            ("Accredited project management certification with construction site focus",
             "The posting asks for the certificate; the practice behind it is 37 CAPEX projects, 11 "
             "contracts and full P&L with site responsibility. I will take the certification Eaton "
             "standardises on."),
            ("Minimum 5 years' construction site management, ideally hands-on data centre projects",
             "Twenty years on site: 11 concurrent contracts with 14 people, 37 projects in a "
             "regulated plant, and own contracting business since 2023."),
            ("Experience in large industrial projects with automation and controls",
             "Automation, controls and SCADA in 24/7 operation and in CAPEX delivery; panel and "
             "**power distribution** design up to high voltage."),
            ("Strong electrical engineering background and training in data centre technologies",
             "High-voltage **switchgear**, **UPS**, emergency lighting, fire alarm, access control and "
             "**power distribution**; cooling and HVAC from refrigeration training and site practice."),
            ("Experience with Power Management, Power Control, Mission Critical or BMS systems",
             "**Mission critical** plant operation with SCADA and building controls; power management "
             "and load priority in live 24/7 systems."),
            ("Professional level of English",
             "Professional written and spoken English; native Danish; engineering documentation "
             "produced in English for international projects."),
            ("Driving licence and able to work and travel within EMEA without restrictions",
             "Driving licence B; based 20 minutes from Copenhagen; able to travel 50 % and across "
             "**EMEA**."),
            ("Advanced expertise with knowledge of the data centre industry or similar technologies",
             "Critical infrastructure rather than data centres specifically: GMP-regulated production "
             "and a 24/7 treatment plant — same regime, same consequence of downtime."),
            ("Proven ability to lead and manage internal and external teams",
             "25 specialists led across engineering, procurement and operations; 14-person contract "
             "team; subcontractors and suppliers managed contractually."),
            ("Strong communication and stakeholder management skills",
             "One voice for the customer on site: daily updates, decisions recorded, and bad news "
             "delivered with a plan."),
            ("Lead end-to-end execution from purchase order to handover, covering design, procurement and implementation",
             "End-to-end in own company and on 37 projects: project basis, **procurement**, site "
             "delivery, **commissioning**, **handover**."),
            ("Build and manage project teams and organise kick-off and regular meetings",
             "Kick-offs with scope baseline and interface list; weekly schedule and cost reviews; "
             "daily board meetings during delivery."),
            ("Develop and maintain schedules and risk registers with proactive mitigation",
             "Look-ahead of 8–12 weeks with hold points; **risk register** with owner, trigger and "
             "date; outages planned into narrow windows."),
            ("Control project costs and margins, manage variations and provide accurate forecasts",
             "Budget and forecast monthly in SAP ERP on 37 projects; **variations** priced and "
             "approved in the week they arose; full P&L since 2023."),
            ("Act as single point of contact for on-site implementation including SAT scripts and commissioning",
             "**Single point of contact** on site for customer, contractor and own crews; **SAT** "
             "protocols written before testing; IQ/OQ/PQ documentation."),
            ("Ensure project success across safety, customer satisfaction, financial performance and timing",
             "LOTO, risk assessment and safety walks on every mobilisation; zero critical findings at "
             "acceptance; projects closed within budget and on the agreed date."),
            ("Drive continuous improvement by sharing lessons learned and recommending better practices",
             "Templates, checklists and dashboards built and shared; 40 % less administration from own "
             "**AI** tools; **lessons learned** written into the next project plan."),
        ],
        widths=(3600, 6746))

    m.section("WHERE I WOULD START")
    m.para("With the file, not the site. First week: read the scope baseline, **schedule** and **risk "
           "register** of every live project in the portfolio and mark where the three disagree — "
           "because that is where the next surprise is booked. Then walk the two nearest sites with "
           "the customer's representative and the installation team, and check the interface list "
           "against what is actually on the floor. After that, the first conversation about "
           "**commissioning** dates is worth having.", after=0)

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_Eaton_DataCenterProjectManager.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_Eaton_DataCenterProjectManager.docx'))
