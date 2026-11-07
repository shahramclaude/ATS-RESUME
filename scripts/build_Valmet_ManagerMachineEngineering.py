# -*- coding: utf-8 -*-
"""Valmet — Manager, Machine Engineering (Karlstad / Copenhagen).

English posting → English deliverable (en-GB): application p1, CV p2, education +
90 days + four sections p3, requirement matrix p4.
Angle: engineering commits first and everyone downstream inherits it — the manager's
product is capacity in the right place and standards that survive being used by others.
Policy: master/README.md — job first, candidate only as evidence, no hedges.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Manager, Machine Engineering · Engineering delivery, resources and competence'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Copenhagen, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("7 November 2026")
    m.meta("Valmet · Mechanical Engineering, Pulp, Energy and Circularity · Karlstad / Copenhagen")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Application: Manager, Machine Engineering (R61489)", bold=True, color='1A1A1A')
    m.para("To Tuomas Etula and the Mechanical Engineering management team", after=70)

    # ---------------------------------------------------------------- page 1
    m.para("Engineering is the one discipline in a mill project that everybody else has already promised a date "
           "against. By the time a drawing set reaches procurement, manufacturing and site, the decisions that "
           "determine whether the project lands on time have already been taken — and the cost of changing them "
           "has already started to grow. That is the part of machine engineering I am applying to lead: the "
           "twenty engineers across **Karlstad** and **Copenhagen**, and the standard that lets their work be "
           "used by someone who was never in the room.", after=80)

    m.para("**The manager's product is not drawings; it is capacity in the right place and a standard that "
           "survives being handed over.** At Novo Nordisk I led **25 specialists** across engineering, "
           "procurement and site on **37 concurrent CAPEX projects** of DKK 2–10m each. The interfaces between "
           "those functions were the job — not an afterthought once the drawings were issued. When a discipline "
           "is late, the others do not wait politely; they build around the gap, and that is where the cost "
           "and the quality loss appear.", after=80)

    m.para("**I have spent most of my career at the point where engineering meets reality: commissioning.** As "
           "commissioning engineer for electrical systems I received the packages, ran **FAT/SAT** and "
           "**IQ/OQ/PQ** in a **GMP/FDA/EMA** validated environment, and handed over with **zero critical "
           "findings**. That gives a specific view of what an engineering deliverable is worth: not whether it "
           "is complete on paper, but whether the shift team, the supplier and the commissioning engineer can "
           "work from it without coming back with the same question three times.", after=80)

    m.para("**Machine engineering practice, seen from the plant floor.** I am a mechanical engineer by training "
           "— elautoriseret maskinmester — and I began in a machine workshop, repairing industrial plant, before "
           "running **24/7** operations at Lynetten with **pumps, ventilation, HVAC, high-voltage switchgear "
           "and SCADA**. I know what a machine does after the drawing is approved: wear, alignment, access for "
           "maintenance, spare-part reality and the cost of an unplanned stop on a Sunday. It is the perspective "
           "I would want a team of designers and project engineers to be challenged by, because it is the "
           "perspective their customer lives in.", after=80)

    m.para("**Resources and teams, at four sizes.** Twelve technicians in a machine workshop in Tehran, "
           "**14** in a contracting team, **25** specialists across disciplines, and today **5 electricians "
           "plus 3 apprentices** with a full P&L. Competence matrices, one-to-ones, apprentice development and "
           "capacity planned against one pool rather than five optimistic lists — that is how a team stays "
           "deliverable when two projects land in the same week and the third one slips.", after=80)

    m.para("**Change management is a discipline of its own, and it is mostly about the order of the steps.** I "
           "have introduced **5S**, standard work and **PDCA** on a workshop floor and in a store, and the "
           "improvements that held were the ones the people doing the work had helped design. The measured "
           "effects are on the record: **40 % lower energy cost** in a Novo Nordisk programme and **over 40 % "
           "productivity gain** in my own business from removing manual steps between data and decision. "
           "Standardisation only sticks when it makes the next job easier, not when it makes the audit easier.",
           after=80)

    m.para("**Leading across boundaries is something I have done from both sides.** I worked seven years in "
           "industrial production in Tehran before building a career in Denmark, so I have been the person "
           "working in a second language and the person asking others to. Your four principles are ones I "
           "recognise from practice rather than from a slide: **accountability** is a written plan with a named "
           "owner and a date; **courage** is refusing to sign off work you would not put your own name on, "
           "which is easier when the criteria were agreed before the pressure arrived; **trust** is a "
           "near-miss reported without punishment, because a near-miss that is reported is worth more than an "
           "accident that has to be explained; and **collaboration for growth** is measured at the customer's "
           "plant, not in our own meetings.", after=80)

    m.para("**Valmet's side of the equation is engineering at plant scale.** 225 years, more than 19,000 people "
           "and projects across Europe, South America and Asia — pulp, **biomass** and **energy** projects where "
           "resource efficiency is the commercial argument. My own energy work is the same arithmetic in a "
           "smaller building: measure, find where the loss is, fix it in the right order and prove the result "
           "afterwards.", after=80)

    m.para("I am based in Måløv, about half an hour from Copenhagen Airport, and I can work from **Copenhagen** or "
           "travel to **Karlstad** weekly; I am ready to travel internationally when projects require it, and I "
           "accept the background check and the alcohol and drug testing that apply in Sweden. I would like to "
           "hear how the twenty engineers are distributed between the two sites today, how competence is mapped "
           "against the project portfolio, and what would count as success for **Engineering Excellence** in "
           "the first twelve months.", after=70)
    m.meta("Yours sincerely", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFILE")
    m.para("Engineering and operations leader with 20+ years in mechanical and electrical systems across "
           "process, pharmaceutical and contracting environments — team leadership from **5 to 25** people and "
           "a **full P&L** today. Commissioning background: **FAT/SAT** and **IQ/OQ/PQ** in a **GMP/FDA/EMA** "
           "validated environment with **zero critical findings** at handover. **Machine engineering** in "
           "practice — pumps, ventilation, HVAC, switchgear and a machine workshop — combined with competence "
           "matrices, apprentice development, standard work and **PDCA** that delivered **over 40 % lower "
           "energy consumption** and **over 40 % productivity gain**. Professional **English**, native Danish "
           "and Persian.", after=80)

    m.section("ENGINEERING DELIVERY, RESOURCES AND IMPROVEMENT")
    for label, body in [
        ("Engineering deliverables that survive commissioning",
         "Packages used at FAT/SAT and IQ/OQ/PQ; acceptance criteria agreed before the phase began, and a "
         "handover that closed with zero critical findings because the documentation answered the questions "
         "in advance."),
        ("Resource management and competence planning",
         "One capacity pool for 5–25 people; competence matrices, one-to-ones and apprentice development "
         "planned against the project portfolio rather than against optimism."),
        ("Cross-functional interfaces",
         "37 concurrent CAPEX projects with engineering, procurement, suppliers and site in the same plan; "
         "interfaces named, owned and dated instead of discovered at commissioning."),
        ("Machine engineering in operation",
         "Pumps, ventilation, HVAC, high-voltage switchgear and SCADA in 24/7 operation, with availability as the "
         "requirement — specification, installation, fault-finding and preventive maintenance."),
        ("Continuous improvement with numbers",
         "Lean practice with 5–14 people: 5S, standard work, PDCA, A3, value-stream mapping and Kaizen; 40 % lower "
         "energy cost in one programme, over 40 % productivity gain from removing manual steps."),
        ("Standardisation and digital tooling",
         "Checklists, templates and dashboards in Excel, Power BI, Python and SAP ERP built where no tool "
         "existed, documented and handed over so a team can run them without the person who built them."),
    ]:
        m.bullet(label, body, after=25)

    m.section("EXPERIENCE")
    jobs = [
        ("Owner / Technical Director",
         "ELOHVAC ApS · Copenhagen · May 2023–present",
         "5 electricians + 3 apprentices · full P&L · quotations, capacity and delivery",
         [("Team, competence and delivery",
           "Daily planning, one-to-ones and apprentice development against a live order book; quotations and "
           "calculation, supplier and subcontractor management, quality control and handover documentation."),
          ("Improvement and tooling",
           "Standard work and Python/Power BI tooling that cut administrative steps, giving over 40 % "
           "productivity gain; zero critical deviations in the service agreements.")]),
        ("Senior Commissioning Engineer / Project Manager, Electrical Systems",
         "Novo Nordisk A/S · Kalundborg/Bagsværd, Denmark · Nov 2022–Jul 2024",
         "37 parallel capital projects · 25 specialists · GMP/FDA/EMA validated environment",
         [("Engineering interfaces and handover",
           "Cross-disciplinary leadership of 25 specialists across engineering, procurement and site; FAT/SAT "
           "and IQ/OQ/PQ to acceptance, with zero critical findings at handover."),
          ("Energy programme and reporting",
           "PDCA programme delivering 40 % lower energy cost — measurement, root-cause analysis, prioritised "
           "actions and monthly reporting to management and client in SAP ERP.")]),
        ("Project and Workshop Manager",
         "Ventek-Air · Copenhagen · Jan 2022–Nov 2022",
         "14 employees · 11 concurrent projects · DKK 2–10m per project",
         [("Capacity, sequencing and subcontractors",
           "11 projects from specification to formal handover with 14 people and one capacity pool; daily "
           "board meetings, bottleneck analysis and standardised ways of working.")]),
        ("Operations and Maintenance Manager",
         "Lynetten under Biofos · Copenhagen · Aug 2017–Jan 2022",
         "Critical plant in 24/7 operation · pumps, HVAC, HV switchgear, SCADA",
         [("Machine reliability and improvement",
           "Preventive maintenance and replacement planning by criticality; 5S, standard work and PDCA on "
           "workshop and store; energy programme delivering over 40 % lower consumption.")]),
        ("Electromechanical Technician / Production Team Leader",
         "ARJ Engineering · Tehran · Dec 2003–Mar 2010",
         "12 mechanics and technicians · machine workshop · industrial equipment",
         [("Workshop leadership and root cause",
           "Diagnosis and repair of industrial mechanical and electrical plant; shift planning, material "
           "planning and performance follow-up for 12 technicians.")]),
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
    m.para("**English: professional**, written and spoken, in meetings, tender documents and technical "
           "documentation · Danish: native · Persian: native · **Based in Måløv**, able to work from "
           "**Copenhagen** or travel to **Karlstad** weekly · Full driving licence · Available at short notice · "
           "Accept background check and alcohol/drug testing · References on request.", after=70)

    m.models_table("THE FIRST 90 DAYS — ONE TEAM, TWO SITES, ONE STANDARD",
                   ("Period", "What happens, and how it is measured"), [
        ("Week 1–2",
         "Sit with the team in both Karlstad and Copenhagen; read the live project portfolio, the resource "
         "plan and the last year of deliverable quality issues; meet the Global Head, Engineering Excellence "
         "and the project execution leads to understand where engineering is currently the constraint."),
        ("Day 30",
         "One competence and capacity map across the two sites: who can do what, at which level, and where the "
         "pool is one deep; the five interfaces where late deliverables cost the most identified with an owner "
         "each; deliverable standard and review practice agreed with Engineering Excellence."),
        ("Day 60",
         "Standard template and checklist set in use on live projects, not as a proposal; resource plan for "
         "the next two quarters agreed with project execution; two improvement cases started with a baseline "
         "number and a named owner in the team."),
        ("Day 90",
         "First measured effect on on-time delivery or rework on the projects that adopted the standard; "
         "development plans in place for every engineer including the two or three identified as next "
         "specialists; and a short list of what to standardise next, agreed with the global pool rather than "
         "imposed on it.")])

    m.section("A DRAWING SET IS A CONTRACT WITH EVERYONE DOWNSTREAM")
    m.para("Procurement buys from it, manufacturing builds from it, site installs from it and commissioning "
           "proves it. So an engineering deliverable is not finished when it is technically correct — it is "
           "finished when the people downstream can act on it without asking. That is why I would judge the "
           "team's output at the point of use and not at the point of issue, and why the review criteria should "
           "be written by the people who receive the work as well as the people who produce it.", after=80)

    m.section("COMPETENCE IS A CAPACITY NUMBER, NOT A HEADCOUNT")
    m.para("Twenty engineers is not a capacity; twenty engineers with a known spread of experience against a "
           "known portfolio is. On paper everyone can do every task; in a project week, two people can do a "
           "particular one, and one of them is on site. I have run a competence matrix and one-to-ones for "
           "teams from 5 to 25, and the value is not the matrix — it is the conversation it forces about who "
           "is being developed into the next gap, before the gap becomes a delay.", after=80)

    m.section("TWO SITES ARE ONE TEAM ONLY WHEN THE STANDARD IS THE SAME")
    m.para("Karlstad and Copenhagen can share a resource pool, a template or a title and still behave like two "
           "teams. What makes them one is unglamorous: the same review gates, the same deliverable structure, "
           "the same way of recording a decision, and enough rotation that people have met the colleague they "
           "are handing work to. Cross-boundary work is a habit built through small exchanges, not a value "
           "stated in a strategy document.", after=80)

    m.section("IN A PULP MILL, THE ENGINEER'S CUSTOMER IS THE SHIFT TEAM")
    m.para("A pulp mill, a biomass plant or an energy project is ultimately run by people on shift, at three in "
           "the morning, with a manual and a phone. Designs that ignore access, isolation, spare parts and the "
           "sequence of a real maintenance stop become the reason a plant loses hours every year. Twenty years "
           "in 24/7 operations taught me to ask that question during engineering — while it is still cheap to "
           "answer — and to bring the operational view into the review rather than into the complaint "
           "afterwards.", after=80)

    m.page_break()

    m.models_table("WHAT THE ROLE REQUIRES — WHAT I HAVE DELIVERED", ("Requirement in the posting", "Evidence"), [
        ('Lead and develop a team of machine engineers, supporting project execution and competence development',
         'Teams of 5, 12, 14 and 25 people: competence matrices, one-to-ones, apprentice development and capacity planned against a live project portfolio.'),
        ('Ensure high-quality, timely and cost-effective engineering deliverables for sales, procurement, manufacturing and commissioning',
         'Tested where they are used: FAT/SAT and IQ/OQ/PQ acceptance, zero critical findings, packages that construction and supplier could work from.'),
        ('Collaborate with the Global Head, Engineering Excellence and other engineering leaders to improve processes',
         'Process improvement built with the people who use it — 5S, standard work, PDCA and templates agreed with workshop, store and project teams before rollout.'),
        ('Drive a unified global approach to machine engineering; competence and collaboration across the global resource pool',
         'One capacity pool across disciplines in own business and in 37-project portfolios; shared checklists so work does not depend on one person.'),
        ('Partner with internal stakeholders and external engineering companies to secure the right expertise and resources',
         'Subcontractors, consultants, suppliers and authorities on 37 capital projects and 11 contracts; interfaces agreed in writing before start.'),
        ('Deliver an excellent customer experience through engineering and project delivery',
         'Service agreements with response time and quality as measured KPIs, zero critical deviations; client reporting monthly for two years.'),
        ('Support pulp mills, biomass power plants and energy projects',
         '24/7 process plant at Lynetten and 37 CAPEX projects at Novo Nordisk; energy programmes with over 40 % lower consumption.'),
        ('M.Sc. degree in Engineering or a related technical discipline',
         'B.Tech in technology management and mechanical engineering (GPA 7.6/12) plus electrical and mechanical engineering design at EQF 6 and Danish HV/LV authorisation.'),
        ('Strong leadership, decision-making, problem-solving and change management capabilities',
         '20 years of line and project leadership; 5S, standard work and PDCA implemented in four organisations, decisions recorded.'),
        ('Several years of experience within machine engineering',
         'Machine workshop background and 20 years with mechanical and electrical plant: pumps, ventilation, HVAC, switchgear, installation, fault-finding and maintenance.'),
        ('Proven track record in resource and team management',
         'Capacity planned for 5–25 people against 11 and 37 concurrent projects; full P&L today with recruitment and development.'),
        ('Broad knowledge of machine engineering practices, project execution and engineering processes in industry',
         'Process plant, GMP production, contracting and machine workshop — specification, installation, handover and operation.'),
        ('Communicate fluently in English, verbally and in writing; additional language skills a plus',
         'Professional English in meetings, tender documents and technical documentation; native Danish and native Persian.'),
        ('Willing to travel internationally when business needs require it',
         'Based in Måløv, half an hour from Copenhagen Airport; weekly Karlstad travel and international project travel both workable.'),
        ('Motivate and develop engineering talent while ensuring disciplined execution and continuous improvement',
         'Apprentices trained to independent work, specialists developed through one-to-ones, improvement cases owned by the teams.'),
        ('Comfortable leading through change, building trust across teams and balancing multiple priorities',
         'Change on live operations — 5S and standard work without stopping production; priorities re-agreed weekly across 37 projects.'),
        ('Take accountability — act with ownership, set clear expectations and follow through',
         'A written plan, a named owner and a date for every action; open items from last month open the next review, and escalations closed by a person.'),
        ('Lead with courage — champion change, try bold ideas and learn quickly',
         'Stopped and corrected work that would not have passed its own acceptance criteria; introduced tooling and standards before they were requested.'),
        ('Build on trust — listen to understand, be open and create psychological safety',
         'Near-miss reporting and toolbox meetings on a 24/7 plant; a report is met with a fix, not a name.'),
        ('Collaborate for growth — work across boundaries, value diverse perspectives and focus on customer value',
         'Seven years in Iran and a Danish career since; value judged at the customer plant, not in internal meetings.'),
        ('Delegated health, safety and environmental responsibilities as part of people leadership',
         'HSE ownership as line manager: risk assessments (APV), LOTO, safety rounds and near-miss follow-up for teams of 5–14.'),
    ], widths=(3600, 7046))

    return m.save(path, title="Manager, Machine Engineering — Valmet",
                  subject="Engineering delivery, resources and competence",
                  keywords="machine engineering, engineering leadership, resource management, competence "
                           "development, commissioning, continuous improvement, hse, valmet, karlstad, copenhagen")


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Valmet_ManagerMachineEngineering.docx')))
