# -*- coding: utf-8 -*-
"""Vestas — Team Lead Warehouse Operations, Offshore Service Campaign (f/m/d), req. 79277.

English posting → English deliverable (en-GB): application p1, CV p2, education +
90 days + five sections p3, requirement matrix p4.
Angle: an offshore campaign is decided in the warehouse — the vessel sails on the
weather window, so whatever is missing then is missing for the whole trip.
Policy: master/README.md — job first, candidate only as evidence, no hedges.
Fair-hiring note in the posting: no photo, no date of birth or graduation, no gender
pronouns — education entries therefore carry no years.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Team Lead, Warehouse Operations · Inventory, safety and offshore campaigns'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4 November 2026")
    m.meta("Vestas · Team Lead Warehouse Operations, Offshore Service Campaign · req. 79277")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Application: Team Lead Warehouse Operations, Offshore Service Campaign",
           bold=True, color='1A1A1A')
    m.para("To the hiring team in NCE Supply Chain Operations, Offshore Service Campaign", after=70)

    # ---------------------------------------------------------------- page 1
    m.para("An offshore campaign is decided in the warehouse long before it is decided at sea. The vessel "
           "leaves on the **weather window**, not on the date the plan would have preferred — so whatever is "
           "missing at that moment is missing for the whole trip: an extra sailing, a turbine standing still, "
           "a crew waiting for a spare part that was on the shelf but not on the picking list. The team that "
           "gets those numbers right, every day, is the team I want to lead.", after=80)

    m.para("**A stockkeeper's day is a sequence, not a list.** Tools before consumables, the campaign box "
           "before the ad-hoc request, the return leg before the next departure. I have run that sequence "
           "with **five electricians and three apprentices** in my own business, with **fourteen people** and "
           "eleven concurrent projects before that, with **25 specialists** on 37 capital projects, and with "
           "**twelve technicians** in a machine workshop. Daily allocation, named owners and a number on the "
           "board at the end of the shift — that is how a team stays safe and efficient at the same time.",
           after=80)

    m.para("**A stock figure nobody trusts is worse than no figure at all.** Inventory accuracy is a "
           "discipline of reconciliation: goods received checked against the delivery note, put away in the "
           "right bin, booked the same day, counted on a cycle rather than once a year. I have worked in "
           "**SAP ERP** with cost, asset and stock data and reported from it monthly to management and "
           "client, and I have run purchasing, order book and stock in my own company, where the count had "
           "to be right because I paid for the difference.", after=80)

    m.para("**Critical spares are a promise you keep at three in the morning.** At Lynetten, a 24/7 plant, "
           "the store held the parts that had to be there when a pump or a switchboard failed — "
           "**spare-parts flow and stock control** were part of my job, alongside **5S** and standard work "
           "on store and workshop. Minimum and maximum stock levels set from consumption, obsolete stock cleared, "
           "anything urgent escalated before it became an outage. The part that is not there when the hatch "
           "closes costs a sailing, not a phone call.", after=80)

    m.para("**Safety in a warehouse is decided by layout and by habit.** Forklifts and pedestrians sharing "
           "a floor, racking loaded properly, material handling done with equipment rather than with a back, chemicals "
           "stored as the label says. I have run **toolbox talks**, **risk assessments (APV)**, safety "
           "rounds and **LOTO** on live plant, and written the instruction that made the safe way the quick "
           "way. Incident reporting and near-misses logged without a name attached, because the report is worth more than the "
           "blame.", after=80)

    m.para("**The two KPIs in this role are about the return leg.** Goods receipt on time depends on when "
           "the harbour actually receives and books it; equipment coming back not delivered clean depends on "
           "who washes, checks and books it before it goes on the shelf again. Both are process problems "
           "before they are people problems — so I measure the flow, find where it stops, and change the "
           "standard. In my own operations that cut energy cost by **40 %** through PDCA and lifted "
           "productivity by more than **40 %** through dashboards in **Power BI** and **Python**.", after=80)

    m.para("**Vessels and harbours have their own rules, and I have worked under them.** I hold **STCW** "
           "certificates — watchkeeping in the engine room (A-III/1), designated security duties (VI/6), "
           "ship security officer (VI/5), tanker familiarisation (V/1-1, V/1-2) — so a gangway, a permit to "
           "work on board and a vessel's own safety regime are not foreign territory. Different ports mean "
           "different requirements, and that is a **training matrix** problem: who is cleared for which "
           "harbour, which certificate expires when, who covers the gap. I have built those matrices for "
           "electricians and apprentices, with training booked from the matrix rather than remembered in "
           "December.", after=80)

    m.para("**Material arriving in someone else's harbour is a coordination job, not a delivery.** At Novo "
           "Nordisk I worked the receiving end inside a running **GMP/FDA/EMA** factory, where access, "
           "documentation and storage were agreed before the truck arrived, and I coordinated **37 parallel "
           "projects** across engineering, procurement and site. The habit is the same in a port: call the "
           "other team lead before the goods are on the quay, agree where they are stored, and write it down "
           "while it is still cheap to change.", after=80)

    m.para("**Audits are easier the day the file was built than the day they arrive.** At Novo Nordisk the "
           "handover closed with **zero critical findings** because documentation was produced with the "
           "work, not after it. What I would bring to the Supply Chain Operations Manager is the same "
           "structure, simpler: one page per process with a named owner and a date, a training matrix anyone "
           "can read, and a dashboard showing goods receipt on time and return status without anyone having "
           "to ask for it.", after=80)

    m.para("**Vestas is where that discipline belongs.** Offshore service campaigns run on a supply chain "
           "that has to be right the first time. I am based in **Måløv**, hold a full driving licence, will "
           "travel to the harbours and vessels the campaign serves, and can start at short notice. I would "
           "like to hear which harbour warehouses and campaigns the role covers, how many stockkeepers are "
           "in the team today, and where the two KPIs currently stand — so the first ninety days start from "
           "numbers rather than from assumptions.", after=70)
    m.meta("Yours sincerely", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFILE")
    m.para("Warehouse and operations team leader with 20+ years in materials, stores and "
           "people — **elautoriseret maskinmester (LV/MV/HV)** by trade, with **spare-parts flow, stock "
           "control and 5S** on a 24/7 plant, **SAP ERP** records and reporting at Novo Nordisk, and full "
           "responsibility for purchasing, order book and materials in a contracting business. Led teams of "
           "**5, 12, 14 and 25**, with daily planning, **toolbox talks**, **training matrices** and "
           "audit-ready documentation (**zero critical findings** at GMP handover). Holds **STCW** "
           "certificates for work on board vessels. English and Danish; Måløv; short notice.", after=80)

    m.section("WAREHOUSE, MATERIALS AND SUPPLY CHAIN")
    for label, body in [
        ("Stock and inventory control",
         "Spare-parts flow and stock control on a 24/7 plant: goods received and checked against documents, "
         "booked the same day, minimum and maximum levels set from consumption, cycle counts instead of an "
         "annual surprise."),
        ("SAP and ERP records",
         "SAP ERP for cost, asset and stock data at Novo Nordisk with monthly reconciliation and reporting; "
         "ERP purchasing, order book and supplier follow-up in own business."),
        ("Materials, tools and consumables",
         "Tools and consumables planned per task and per vessel window; requisitions raised against the "
         "programme, deliveries tracked, materials stored off the floor."),
        ("Coordination across sites and teams",
         "37 parallel capital projects coordinated across engineering, procurement and site; arriving "
         "material agreed with the receiving team before it lands, in writing."),
        ("KPIs and continuous improvement",
         "Board and dashboard follow-up on delivery, stock accuracy and response times; PDCA and 5S cut "
         "energy cost 40 % and lifted productivity more than 40 %."),
        ("Audit, structure and standards",
         "One page per process with an owner and a date; documentation produced with the work — zero "
         "critical findings at GMP handover, inspections passed without a scramble."),
    ]:
        m.bullet(label, body, after=25)

    m.section("EXPERIENCE")
    jobs = [
        ("Owner / Technical Director",
         "ELOHVAC ApS · Copenhagen · May 2023–present",
         "5 electricians + 3 apprentices · full P&L · purchasing, order book and materials",
         [("Team, materials and the day's plan",
           "Daily allocation of work to five electricians and three apprentices; tools, materials and "
           "consumables ordered against the programme, deliveries chased, stock kept where the crew can find "
           "it; zero critical deviations in the service agreements."),
          ("Commercial control and reporting",
           "Pricing, purchasing and order book in an ERP system, with follow-up on deliveries, stock and "
           "margin; KPI dashboards in Power BI steer the week rather than report the quarter.")]),
        ("Senior Commissioning Engineer / Project Manager, Electrical Systems",
         "Novo Nordisk A/S · Kalundborg/Bagsværd, Denmark · Nov 2022–Jul 2024",
         "37 parallel capital projects · 25 specialists · GMP/FDA/EMA validated environment",
         [("Inventory records and reporting in SAP",
           "Cost, asset and stock data maintained in SAP ERP with monthly reconciliation and reporting; goods "
           "receipt and documentation checked against delivery."),
          ("Cross-functional alignment",
           "Engineering, procurement and site aligned on 37 concurrent projects; material availability, "
           "access and storage agreed before arrival, and handover closed with zero critical findings.")]),
        ("Project and Workshop Manager",
         "Ventek-Air · Copenhagen · Jan 2022–Nov 2022",
         "14 employees · 11 concurrent projects · DKK 2–10m per project",
         [("Capacity, deliveries and storage",
           "Daily leadership of a 14-person team with two-week look ahead; ordering, deliveries and storage "
           "controlled against the programme, bottlenecks solved at the daily board meeting.")]),
        ("Operations and Maintenance Manager",
         "Lynetten under Biofos · Copenhagen · Aug 2017–Jan 2022",
         "Critical plant in 24/7 operation · store and workshop · HV switchgear, pumps, HVAC, SCADA",
         [("Spare parts, store and 5S",
           "Spare-parts flow and stock control for a plant that could not stop: stock levels from consumption, 5S "
           "and standard work on store and workshop, critical parts on hand across every shift handover."),
          ("Safety on a live site",
           "LOTO, APV risk assessment, safety rounds, near-miss follow-up and toolbox talks; stop-work authority "
           "used when paperwork and task did not match.")]),
        ("Electromechanical Technician / Production Team Leader",
         "ARJ Engineering · Tehran · Dec 2003–Mar 2010",
         "12 mechanics and technicians · machine workshop · industrial plant",
         [("Materials and output",
           "Daily allocation of work to 12 technicians with materials, tools and spare parts controlled "
           "against the week's plan, and output measured per person and per machine.")]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.page_break()
    m.section("EDUCATION AND AUTHORISATION")
    m.edu("B.Tech, Technology Management and Mechanical Engineering",
          "Copenhagen School of Marine Engineering & Technology Management · GPA 7.6/12")
    m.edu("Electrical and Mechanical Engineering Design, Electrical Engineering (EQF 6)",
          "Tehran Technical University")
    m.edu("Danish HV/LV authorisation — elautoriseret maskinmester (LV/MV/HV)",
          "Danish Safety Technology Authority")
    m.edu("Refrigeration and air-conditioning (AMU) · Lean practice: 5S, PDCA, A3, standard work",
          "Mercantec · continuous improvement applied in operations")

    m.section("LANGUAGES, PRACTICALITIES AND REFERENCES")
    m.para("**English: professional**, written and spoken, for briefings, documentation and coordination · "
           "Danish: native · Persian: native · **Based in Måløv, Greater Copenhagen**, willing to travel to "
           "harbours and vessels across North and Central Europe · Full driving licence · **STCW** "
           "certificates for work on board vessels · Available at short notice · References on request.",
           after=70)

    m.models_table("THE FIRST 90 DAYS — STOCK ACCURACY, SAFETY AND THE CAMPAIGN CALENDAR",
                   ("Period", "What happens, and how it is measured"), [
        ("Week 1–2",
         "Walk every harbour warehouse and the vessel flow with the team; read the campaign calendar, the "
         "KPI definitions (GR on time, YMM not delivered cleaned) and the local port requirements; learn "
         "SAP transactions the team actually uses, from the stockkeepers who use them."),
        ("Day 30",
         "Daily rhythm agreed — short briefing, allocated tasks, one number per person on the board; cycle "
         "count started on the highest-risk bins; safety walk with actions and owners; training matrix "
         "rebuilt in one file with expiry dates."),
        ("Day 60",
         "Goods receipt and put-away measured per harbour and the biggest delay fixed at its cause; return "
         "leg standardised — clean, check, book, store; toolbox talks running on a fixed day with attendance "
         "recorded; first improvement measured, not described."),
        ("Day 90",
         "Stock accuracy and on-time goods receipt reported weekly on one dashboard to the Supply Chain "
         "Operations Manager; training matrix driving bookings instead of reacting to them; a written "
         "one-page standard for each core process, and a team that knows what is expected of it before the "
         "next sailing.")])

    m.section("A MISSING PART DOES NOT WAIT FOR THE NEXT MEETING")
    m.para("Every warehouse has a list of things that were not there when they were needed, and the list is "
           "almost never about the shelf — it is about a receipt booked a day late, a return put back "
           "unwashed, a level set three years ago, or a request that arrived as a phone call instead of an "
           "order. So the answer is not a bigger store; it is a standard for each of those four movements, "
           "visible on a board, and a team that is allowed to stop and fix the process when the same "
           "shortage appears twice.", after=80)

    m.section("THE RETURN LEG IS WHERE THE MONEY IS LOST QUIETLY")
    m.para("Outbound is visible: everyone chases the vessel, and the sailing date forces the issue. The "
           "return is where equipment comes back dirty, incomplete, unbooked or simply late, and where the "
           "next campaign pays for it in missing tools and emergency purchases. I have run service "
           "operations where the same logic applied to tools and spare parts after every job: wash, check "
           "against the list, book it back, store it where it belongs — and the cost of the next job drops "
           "because nobody is buying what they already own.", after=80)

    m.section("SAFETY IS A HABIT IN A WAREHOUSE, NOT A POSTER")
    m.para("Stockkeepers work with forklifts, racking, lifting equipment and heavy goods, often against a "
           "departure date — which is exactly when shortcuts appear. The controls that work are physical and "
           "boring: separate walkways, load limits respected, lifting with equipment, housekeeping owned by "
           "a named person, and a briefing every morning that is short enough to be listened to. On top of "
           "that, near-miss reporting without blame, because the report that arrives the same day prevents "
           "the accident next month.", after=80)

    m.section("A TRAINING MATRIX IS A PROMISE ABOUT WHO CAN WORK WHERE")
    m.para("In a campaign that spans ports in several countries, the matrix is not an HR document — it is "
           "the answer to whether the team can sail tomorrow. Who is cleared for which harbour, which "
           "certificate expires before the next campaign, who can operate which equipment, and who covers "
           "when someone is ill. I have maintained competence matrices for electricians and apprentices with "
           "training booked from the matrix, and I would treat the stockkeeper matrix the same way: one "
           "file, one owner, dates that are checked monthly instead of discovered at the gangway.", after=80)

    m.section("STRUCTURE IS WHAT THE OPERATIONS MANAGER SHOULD NOT HAVE TO EXPLAIN TWICE")
    m.para("A supply chain that runs across countries needs standards that survive a change of shift, a "
           "change of port and a new team lead: one page per process, a named owner, a date, and a review "
           "that actually happens. That is how a plant I worked on kept its documentation clean enough for "
           "an audit with zero critical findings, and it is how I would support the Supply Chain Operations "
           "Manager here — building the structure once, in writing, so the operation stops depending on who "
           "is on duty.", after=80)

    m.page_break()

    m.models_table("WHAT THE ROLE REQUIRES — WHAT I HAVE DELIVERED", ("Requirement in the posting", "Evidence"), [
        ('Lead and supervise stockkeepers handling materials, spare parts, tools and consumables',
         'Led 5 electricians + 3 apprentices, 14- and 25-person teams and 12 technicians; materials and tools controlled daily.'),
        ('Plan daily workloads, allocate tasks, brief the team, run toolbox talks, monitor performance',
         'Daily allocation and board meetings in four operations; performance monitoring against the day\'s plan.'),
        ('Accurate inventory records in SAP; support to Service Campaign Operations',
         'SAP ERP at Novo Nordisk: cost, asset and stock data, monthly reconciliation and reporting to client and management.'),
        ('Project meetings, alignment with Service Campaign, operations and schedules for vessels and harbours',
         '37 concurrent projects aligned with engineering, procurement and site; schedules agreed face to face, then written down.'),
        ('Coordinate with other team leads on arriving material, timely storage and warehouse dynamics',
         'Goods receipt checked against delivery, put away and booked; deliveries tracked on 11 concurrent projects.'),
        ('Support offshore operations at different sites across North and Central Europe',
         'Multi-site responsibility today; STCW-certified for work on board vessels; used to travelling to harbours.'),
        ('Support planned and unplanned service events; strong safety culture among stockkeepers',
         '24/7 plant with night call-outs; safety rounds, APV and stop-work authority used when task and paperwork disagreed.'),
        ('Lead the team to report incidents, improve safety standards and advocate process adherence',
         'Near-miss reporting followed up without blame; SOPs, LOTO and APV corrected when practice slipped.'),
        ('Monitor KPIs such as GR on time and YMM not delivered cleaned; drive continuous improvement',
         'KPI boards and Power BI dashboards; productivity up 40 %+ and energy cost down 40 % through PDCA.'),
        ('Own the training matrix; requirements for stockkeepers to operate in different ports',
         'Competence matrices for electricians and apprentices, with training and authorisation booked from the matrix.'),
        ('Support audits and inspections, create structure and develop the offshore operation from a supply chain perspective',
         'Audit-ready documentation built with the work — zero critical findings at GMP handover; one page per process, one owner.'),
        ('Apprenticeship and/or degree in warehouse management or logistics',
         'B.Tech technology management and mechanical engineering (EQF 6) plus 20 years of stores and materials control.'),
        ('Warehouse experience from the wind industry',
         'Store and materials control in a 24/7 process plant and in a contracting business where a missing part stopped the job.'),
        ('Customs knowledge will earn additional points',
         'Receipt control to the letter: goods and documents must agree on every line, and local rules followed, not interpreted.'),
        ('Computer knowledge: SharePoint, Word, Excel, Outlook, TMS, SAP/AX',
         'SAP ERP daily; Excel, Power Query, Power BI and Python for tracking and reporting; Word and Outlook daily.'),
        ('Outstanding communication and team management skills; strong leadership',
         'Briefings in English and Danish for international crews; 1:1s, MUS/GRUS and honest assessments in teams of 5, 12, 14 and 25.'),
        ('Time management, planning, scheduling and system-thinking',
         'Programmes built from capacity, not wishes; two-week look ahead, bottleneck analysis and buffers where they matter.'),
        ('Adherence and compliance with local laws and regulations; instructions turned into action',
         'Worked to GMP/FDA/EMA, DS/HD 60364, AB 18 and Danish working-environment rules; instructions made into SOPs.'),
        ('Knowledge of offshore wind logistics and safety standards',
         'STCW: watchkeeping A-III/1, security duties VI/6, ship security officer VI/5, tanker V/1-1 and V/1-2.'),
        ('Familiarity with SAP or another ERP system',
         'SAP ERP at Novo Nordisk for cost, assets and stock; ERP purchasing and order book in own business.'),
        ('Problem-solving mindset with a relentless focus on efficiency',
         'Root cause before remedy — 5xWhy, Ishikawa, A3 — with productivity up 40 %+ and energy cost down 40 %.'),
        ('Highly organised: collect information, find patterns, structure it and create standards',
         'Information turned into one-page standards, checklists and dashboards; 5S and standard work on store and boards.'),
    ], widths=(3600, 7046))

    return m.save(path, title="Team Lead Warehouse Operations — Vestas",
                  subject="Inventory, safety and offshore service campaigns",
                  keywords="warehouse team lead, inventory, spare parts, SAP, logistics, kpi, "
                           "safety culture, training matrix, offshore, stcw, vestas, denmark")


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Vestas_TeamLeadWarehouse.docx')))
