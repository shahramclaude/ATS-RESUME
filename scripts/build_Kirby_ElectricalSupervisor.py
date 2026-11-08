# -*- coding: utf-8 -*-
"""Kirby Group Engineering — Electrical Supervisor, Denmark.

English posting → English deliverable (en-GB): application p1, CV p2, education +
90 days + four sections p3, requirement matrix p4.
Angle: a site is controlled at the whiteboard and at the moment someone decides the
task can start — and the supervisor who is himself authorised does not wait.
Policy: master/README.md — job first, candidate only as evidence, no hedges.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Electrical Supervisor · Trade leadership, quality and EHS on site'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Copenhagen, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("8 November 2026")
    m.meta("Kirby Group Engineering · Electrical Supervisor · Denmark")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Application: Electrical Supervisor", bold=True, color='1A1A1A')
    m.para("To the Talent Acquisition Team and the Construction Management team in Denmark", after=70)

    # ---------------------------------------------------------------- page 1
    m.para("A site is not controlled from the site office. It is controlled at the **whiteboard**, where the "
           "next trade needs the area, and at the moment someone decides whether a task can start before the "
           "**RAMS** are signed. That decision — made twenty times a day, by the person the crew looks at — is "
           "the job I am applying for.", after=80)

    m.para("**A site supervisor's product is the day: what is complete, what is next, and what is blocked.** "
           "Supporting the Site Manager means knowing the **IFC scope** line by line, tracking progress against "
           "it daily, and making sure the area is **construction complete** before testing and **commissioning** "
           "dates are called. I have run that rhythm with five electricians and three **apprentices** in my own "
           "business, with fourteen people and eleven concurrent projects before that, and with "
           "**25 specialists** across engineering, procurement and site on 37 capital projects.", after=80)

    m.para("**I am an authorised person, not a supervisor waiting for one.** In Denmark I hold the national "
           "HV/LV authorisation as **elautoriseret maskinmester (LV/MV/HV)**, which means the isolation, the "
           "permit and the switching decision sit with me rather than with someone who has to be called to "
           "site. **LOTO**, proving dead, permits for hot work and work near live equipment: I have issued and "
           "signed them, and I have been the one who had to say no when the paperwork was not there.", after=80)

    m.para("**The sectors are the ones I have worked in — mission-critical production that cannot stop.** At "
           "Novo Nordisk I worked inside a **GMP/FDA/EMA** validated **pharmaceutical** environment, where "
           "documentation is not a formality: **FAT/SAT** and **IQ/OQ/PQ**, witness points, and a handover that "
           "closed with **zero critical findings**. Before that, 24/7 operations at Lynetten — pumps, "
           "ventilation, HVAC, high-voltage switchgear and SCADA — where an unplanned stop is measured in hours "
           "of lost production rather than in euros of rework.", after=80)

    m.para("**Quality is cheaper the day the snag is found.** I have worked to inspection and test plans in "
           "effect — the same discipline the **ITP** and the **Quality Control Plan** describe: hold points "
           "agreed, materials checked against the specification, **red-line drawings** updated as the work "
           "moves, and snags logged and cleared to the **walkdown** date instead of discovered at it. When the "
           "same fault appears twice, the answer is a **toolbox talk** with the crew, not a second snag on the "
           "list.", after=80)

    m.para("**Safety leadership is the part you cannot delegate and cannot fake.** Hazards identified before "
           "the task, controls written down, **MIMO**, **working at height** and work with or around "
           "electricity planned rather than improvised, **110V** tools, exclusion zones marked on the board, "
           "and nobody working under another trade working above them. I have run **safety audits**, incident "
           "follow-up and near-miss reporting on a 24/7 plant — the same logic as the **SBO** scheme — and the "
           "culture that makes it work is simple: people report what they see when the answer is a fix, not a "
           "name.", after=80)

    m.para("**A two-week look ahead is a conversation with three other trades.** It only works if the sequence "
           "is agreed face to face — area by area, with access, temporary power and storage settled in advance, "
           "**housekeeping** kept off the floor and materials stored properly rather than where they land. I "
           "have coordinated that on building sites in Copenhagen and inside a running factory, and the rule is "
           "the same: the trade that arrives second should never be the one who discovers the conflict.", after=80)

    m.para("**Commercial acumen comes from having signed the other side of the order.** As owner of an "
           "electrical contracting business I have priced work, taken off quantities, notified variations, "
           "ordered materials against **lead times** and chased **delivery dockets** — and I know what a slipped "
           "delivery does to a programme, because I have paid for it. That is also why I understand the "
           "difference between a scope change and a favour.", after=80)

    m.para("**Leading trades is a people job with a paper trail.** Apprentices assessed honestly, subcontractors "
           "told clearly what is expected and how they are doing, daily returns that reflect who is actually on "
           "site, and a supervisor who is present in the area rather than in the cabin. I work in **English** "
           "and Danish, so I can run a briefing for an international crew and a walkdown with a Danish client on "
           "the same morning.", after=80)

    m.para("**Kirby's portfolio is the right place for that experience.** Pharmaceuticals, **power transmission "
           "and distribution** and **data centre** work all depend on the same three things: electrical "
           "discipline, documentation that survives audit, and a supervisor who keeps the area moving. I would "
           "bring the HV/LV authorisation, the GMP documentation discipline and the trade leadership — and use "
           "the Career Development Programmes to extend it. I am based in Måløv, hold a full driving licence, "
           "and can start at short notice. I would like to hear which Danish project the role sits on, the size "
           "of the trade teams, and where Kirby sees the supervisor's role in the testing and commissioning "
           "sequence.", after=70)
    m.meta("Yours sincerely", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFILE")
    m.para("Site and trade leader with 20+ years in electrical installation, testing and maintenance — "
           "**elautoriseret maskinmester (LV/MV/HV)**, hands-on and authorised for isolation and switching. Ran "
           "crews of up to **14** and **25 specialists**, with daily planning, **toolbox talks**, quality audits "
           "and handover documentation; worked inside a **GMP/FDA/EMA** **pharmaceutical** environment with "
           "**FAT/SAT** and **IQ/OQ/PQ** and **zero critical findings** at handover. Owns a contracting business "
           "with full P&L: take-offs, variations, material **lead times** and **delivery dockets**. Works in "
           "English and Danish; based in Copenhagen, available at short notice.", after=80)

    m.section("SITE SUPERVISION, QUALITY AND EHS")
    for label, body in [
        ("Leading electrical trades on site",
         "Daily planning and coordination of electricians, apprentices and subcontractors; work areas set up, "
         "sequenced and handed over so the next trade can start when the programme says."),
        ("Authorised for isolation and switching",
         "Danish HV/LV authorisation (elautoriseret maskinmester, LV/MV/HV); LOTO, proving dead, permits and "
         "switching decisions taken on site by the person accountable for them."),
        ("Quality control and snag management",
         "Inspection and test discipline from FAT/SAT and IQ/OQ/PQ; hold points agreed, materials checked "
         "against specification, red-line drawings kept current and snags cleared to the walkdown date."),
        ("EHS leadership",
         "RAMS, permits and permits-to-work reviewed before tasks start; MIMO, working at height and live "
         "electrical work planned; safety audits, toolbox talks, near-miss reporting and stop-work authority."),
        ("Progress tracking and reporting",
         "Daily and weekly progress records, two-week look ahead agreed with the Construction Manager, and "
         "construction-complete checks ahead of testing and commissioning dates."),
        ("Commercial and procurement",
         "Own P&L: take-offs, variations notified, requisitions raised, deliveries tracked against the "
         "programme, materials stored off the floor and dockets filed correctly."),
    ]:
        m.bullet(label, body, after=25)

    m.section("EXPERIENCE")
    jobs = [
        ("Owner / Technical Director",
         "ELOHVAC ApS · Copenhagen · May 2023–present",
         "5 electricians + 3 apprentices · full P&L · installation, testing and handover",
         [("Site leadership and quality",
           "Daily planning of crews and apprentices, work sequenced across live commercial sites, "
           "quality control before handover and documentation issued with every installation; zero critical "
           "deviations in the service agreements."),
          ("Electrical discipline and authority",
           "LV/MV/HV authorised work: switchgear, control panels, isolation and proving dead under LOTO; "
           "fault-finding, testing and commissioning of installations to DS/HD 60364.")]),
        ("Senior Commissioning Engineer / Project Manager, Electrical Systems",
         "Novo Nordisk A/S · Kalundborg/Bagsværd, Denmark · Nov 2022–Jul 2024",
         "37 parallel capital projects · 25 specialists · GMP/FDA/EMA validated environment",
         [("Testing, commissioning and handover",
           "FAT/SAT and IQ/OQ/PQ to acceptance with zero critical findings; witness points, punch/snag close-out "
           "and handover documentation inside a validated pharmaceutical environment."),
          ("Coordination across trades and site",
           "25 specialists across engineering, procurement and site on 37 projects; interfaces agreed and dated, "
           "and a daily rhythm that kept construction, testing and commissioning in sequence.")]),
        ("Project and Workshop Manager",
         "Ventek-Air · Copenhagen · Jan 2022–Nov 2022",
         "14 employees · 11 concurrent projects · DKK 2–10m per project",
         [("Crews, programme and procurement",
           "Daily leadership of a 14-person team, two-week look ahead and bottleneck analysis at board "
           "meetings; ordering, deliveries and subcontractor interfaces controlled against the programme.")]),
        ("Operations and Maintenance Manager",
         "Lynetten under Biofos · Copenhagen · Aug 2017–Jan 2022",
         "Critical plant in 24/7 operation · HV switchgear, pumps, HVAC, SCADA",
         [("Safe work on live plant",
           "LOTO, risk assessment and permits for work on and around live equipment; safety rounds, near-miss "
           "follow-up and toolbox talks in a plant that could not be stopped.")]),
        ("Electromechanical Technician / Production Team Leader",
         "ARJ Engineering · Tehran · Dec 2003–Mar 2010",
         "12 mechanics and technicians · machine workshop · industrial plant",
         [("Trade leadership and records",
           "Daily allocation of work to 12 technicians, materials and tools controlled, and performance "
           "recorded against the week's plan.")]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.page_break()
    m.section("EDUCATION AND AUTHORISATION")
    m.edu("B.Tech, Technology Management and Mechanical Engineering",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7.6/12")
    m.edu("Electrical and Mechanical Engineering Design, Electrical Engineering (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("Danish HV/LV authorisation — elautoriseret maskinmester (LV/MV/HV)",
          "Danish Safety Technology Authority · May 2023")

    m.section("LANGUAGES, PRACTICALITIES AND REFERENCES")
    m.para("**English: professional**, written and spoken, for briefings, RAMS and documentation · Danish: "
           "native · Persian: native · **Based in Måløv, Greater Copenhagen** · Full driving licence · Available "
           "at short notice · References on request.", after=70)

    m.models_table("THE FIRST 90 DAYS — CONTROL OF THE AREA",
                   ("Period", "What happens, and how it is measured"), [
        ("Week 1–2",
         "Induction, site rules and Kirby Way understood before anything else; read the IFC scope, the "
         "programme, the Quality Control Plan and the RAMS for my area; walk the area with the Construction "
         "Manager and agree set-up, access, temporary power and storage."),
        ("Day 30",
         "Area set up as agreed and kept that way — everything on wheels, materials off the floor, housekeeping "
         "owned by a named person; two-week look ahead issued and agreed weekly; crew and subcontractor "
         "inductions, training and permits verified before each task."),
        ("Day 60",
         "Quality running to the ITP: hold points witnessed, materials checked against specification, red-line "
         "drawings current and snags logged and cleared as work progresses; first weekly quality and safety "
         "audits completed with actions closed inside the week."),
        ("Day 90",
         "My scope construction complete on the dates the programme needs for testing and commissioning, with "
         "the documentation file in a state that would pass an audit; trades and apprentices assessed, and "
         "lessons learned from my area fed back to the Construction Manager.")])

    m.section("THE RAMS ARE NOT PAPERWORK — THEY ARE THE REASON THE JOB CAN START")
    m.para("A method statement is the crew's licence to work: what we are doing, what could hurt us, and what "
           "we have done about it. When it is written for the task in front of the team it gets read; when it is "
           "a template it gets signed and ignored. So I review it with the people who will do the work, amend it "
           "before the task rather than after an incident, and I would rather lose an hour of production than "
           "start a task I cannot describe safely.", after=80)

    m.section("AN AUTHORISED PERSON ON SITE IS WORTH MORE THAN A PHONE CALL")
    m.para("Every hour a crew stands still waiting for someone to isolate, prove dead and sign, the programme "
           "slides — and the temptation to work around it grows. Holding the HV/LV authorisation myself removes "
           "that delay from my area, and it removes the excuse too: isolation, LOTO and switching are done "
           "properly because the person accountable is standing there, not because nobody could reach the AP.",
           after=80)

    m.section("SNAGS ARE CHEAPER THE DAY THEY ARE FOUND")
    m.para("A snag found during installation costs a conversation and ten minutes. The same snag found at "
           "walkdown costs a return visit, a scaffold, a delay to the commissioning window and a meeting about "
           "who pays. That is the arithmetic behind marking up drawings as the work moves, checking materials "
           "against the specification before they go in, and stopping the crew for a toolbox talk when the same "
           "fault appears twice — the second occurrence is a system problem, not a person problem.", after=80)

    m.section("A TWO-WEEK LOOK AHEAD IS A CONVERSATION WITH THREE OTHER TRADES")
    m.para("The plan on the wall is only true if the trades around it agree with it: who needs the area, who "
           "needs the crane, who needs the power off, and who is working above whom. That is settled at the "
           "whiteboard and in the area, not in a spreadsheet. I have done it on sites where six trades shared "
           "one corridor, and the discipline that makes it work is agreeing the sequence out loud, writing it "
           "down, and telling the person who is going to be inconvenienced before they find out for "
           "themselves.", after=80)

    m.page_break()

    m.models_table("WHAT THE ROLE REQUIRES — WHAT I HAVE DELIVERED", ("Requirement in the posting", "Evidence"), [
        ('Senior Trades qualification or equivalent plus 5+ years site experience in pharmaceutical, industrial or data centre sectors',
         '20+ years on site: GMP pharmaceutical production, industrial plant, commercial installation and a machine workshop; Danish HV/LV authorisation.'),
        ('Can interpret schematics and electrical drawings',
         'Single-line diagrams, panel schedules and wiring schematics read and marked up daily; red-line drawings kept current.'),
        ('Strong understanding of site activities and how they are planned and coordinated',
         'Crews, apprentices and subcontractors planned daily across 11 and 37 concurrent packages; sequence agreed with other trades.'),
        ('Record of success as a Trade Leader',
         'Led 5 electricians and 3 apprentices, a 14-person team, 25 specialists and 12 workshop technicians.'),
        ('Familiarity with materials ordering and lead times',
         'Own P&L: requisitions raised, delivery dates confirmed, materials stored correctly and dockets filed.'),
        ('Strong client focus',
         'Client contact as business owner: expectations agreed in writing, progress reported, problems raised early.'),
        ('Commercial acumen',
         'Priced work, completed take-offs, notified variations and protected margin on projects of DKK 2–10m.'),
        ('Excellent communicator and strong interpersonal skills',
         'Briefings, toolbox talks and walkdowns in English and Danish, with crews, subcontractors and clients.'),
        ('Planner and organised',
         'Written plan with a named owner and a date per action; two-week look ahead agreed weekly and kept visible.'),
        ('Influencer',
         'Gets work done through trades that do not report to him — by agreeing the sequence, being fair and following up.'),
        ('Conscientious',
         'Checks that what is signed is what is done: permits, isolations and materials verified.'),
        ('Decisive and action oriented',
         'Decisions taken on the spot — stop the task, move the crew, escalate — and reviewed afterwards.'),
        ('Team player',
         'Works to the Construction Manager and with other supervisors; escalates early.'),
        ('Attentive to detail and record keeper',
         'Daily progress, audit and inspection records, snag lists and handover documentation that pass an audit.'),
        ('Results oriented with the resilience to work under pressure',
         '37 projects delivered on programme inside a validated environment; holds a schedule without trading away safety.'),
        ('Lead and co-ordinate teams of electrical trade professionals on site',
         'Supervised electrical crews and subcontractors on commercial and industrial sites; covers the area for the Site Manager.'),
        ('Track and record site daily activities and progress',
         'Daily records of work completed, labour on site and blockers; weekly input to the planner.'),
        ('Understand the IFC scope of work and notify variations to the Construction Manager',
         'Works from issued-for-construction packages; scope changes notified before they are executed.'),
        ('Develop a two-week look ahead and coordinate work with other trades',
         'Two-week look ahead issued and agreed weekly; coordination at the whiteboard, access and power settled in advance.'),
        ("Implement the Quality Control Plan based on the 6M's and the ITP on site",
         'Inspection and test discipline from FAT/SAT and IQ/OQ/PQ: hold points witnessed, materials verified, zero critical findings.'),
        ('Identify snags as installation progresses and clear them to the walkdown schedule',
         'Snags logged as work proceeds and closed to the walkdown date; repeated faults met with a toolbox talk.'),
        ('EHS: RAMS, SPAs and permits before any task — MIMO, working at height, live electricity',
         'RAMS reviewed and amended before the task, permits signed, LOTO and proving dead applied; work stopped until the paperwork matched.'),
        ('Safety leadership: toolbox talks, weekly audits, stop-work authority, incidents',
         'Weekly audits and toolbox talks with attendance records; near-miss follow-up and stop-work used when it was needed.'),
        ('Ensure the scope is construction complete for agreed testing and commissioning dates',
         'Commissioning from the receiving side: areas handed over complete for FAT/SAT and IQ/OQ/PQ, dates met.'),
        ('Procurement: delivery tracking, requisitions, IRs and delivery dockets',
         'Requisitions and delivery tracking in own business and on 11 concurrent projects; deliveries checked and stored.'),
        ('HR and subcontractors: daily personnel tracking and trade assessments',
         'Daily labour records, apprentice assessments and subcontractor feedback.'),
    ], widths=(3600, 7046))

    return m.save(path, title="Electrical Supervisor — Kirby Group Engineering",
                  subject="Trade leadership, quality and EHS on site",
                  keywords="electrical supervisor, site supervision, ITP, RAMS, LOTO, LV/MV/HV, gmp, "
                           "pharmaceutical, commissioning, ehs, kirby, denmark")


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Kirby_ElectricalSupervisor.docx')))
