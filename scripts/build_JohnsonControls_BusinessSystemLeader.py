# -*- coding: utf-8 -*-
"""Johnson Controls — Business System Leader (BSL). English posting -> English document.

Form (master/FORMKATALOG.md): opening **AB** (a Kaizen week is easy to enjoy; the Tuesday three months later
is the test), structure **After the workshop** (the event · the standard · the escalation · the number · the
next event), register **The Gemba** (gemba, takt, standard work, andon, kanban, red tag, waste, huddle,
cycle time, sustainment). Culture file: jd/JohnsonControls_BusinessSystemLeader_kultur.txt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Business System Leader · Lean, continuous improvement and daily management'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('14 November 2026')
    m.meta('Johnson Controls · Business System Leader · application through the website')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Business System Leader', bold=True, color='1A1A1A')

    def lp(text, after=40):
        return m.para(text, after=after, line=234)

    # ---------------------------------------------------------------- page 1
    lp('**A Kaizen week is easy to enjoy. The Tuesday three months later is the test.** On that Tuesday the '
       'person who ran the workshop is elsewhere, the order book is full, and someone at the line has to work '
       'to the new standard with nobody watching. If the standard was not written for the person doing the job, '
       'the old way comes back — quietly, and usually within a month.', after=34)

    lp('You are asking for someone to **"lead the deployment of Lean Manufacturing and Continuous Improvement '
       'initiatives across the site"**, to be a **"trusted sparring partner to the Plant Manager"** and an '
       '**"active member of both the local management team and the international BSL community"**. I have spent '
       'twenty years in technical operations where a standard either held or it did not: a plant in 24/7 '
       'operation, 37 capital projects, eleven sites at once, my own company with full P&L. What I have not done '
       'is lead a full Lean transformation inside a factory — stated plainly below, not saved for an interview.',
       after=30)

    lp('**After the workshop. Five parts — and the fifth is decided by how the first four were written down.**',
       after=22)

    lp('**The event.** A Kaizen that ends with a wish list is a meeting with a better name. It ends with one '
       'change, owned by someone who works in that area, written so the next shift can use it — and a date when '
       'somebody comes back to look. I have run improvement as project discipline: 37 capital projects, each with '
       'an acceptance criterion, a document trail and a handover that survived audit.', after=20)

    lp('**The standard.** **Standard Work** is not a document; it is how the job is actually done at 14:00 on a '
       'Friday. Written with the operator, verified by standing there and watching, revised when the process '
       'changes — otherwise it is the old way with a new revision number. The same goes for **visual management '
       'systems and standardized work instructions**: if the board is not read at the start of the shift, it is '
       'decoration — and the intention to **eliminate waste** leaves with the last person who cared.', after=20)

    lp('**The escalation.** **Shopfloor Daily Management** is where continuous improvement either lives or '
       'becomes a slide: a problem raised where it happens, with a named owner and a time, and an **escalation** '
       'route that reaches a person rather than a meeting. To **Build accountability and problem-solving '
       'capabilities at the point of impact**, and to **Teach Problem Solving to the Leadership and across the '
       'plant**, is the part of this job I would spend the most hours on in the first year.', after=20)

    lp('**The number.** Productivity, quality, delivery and cost — same definitions every week, one page, so a '
       'change shows in week two and not in month eleven. Measured after, not promised before: **over 40 % '
       'productivity gain** from digitally supported workflows in my own company, and **over 40 % lower energy '
       'consumption** at Lynetten through measurement and re-commissioning. Both were verified afterwards by '
       'someone else\'s numbers.', after=20)

    lp('**The next event.** Sustainment is an audit with a date: is the standard still there, is the board still '
       'used, has the number moved and stayed. **Track and ensure sustainment of implemented Kaizens** in a '
       'review that says which ones are alive and which quietly died — and choose the next Kaizen from the data, '
       'not from enthusiasm.', after=26)

    lp('**Where my record is thinner, stated plainly.** I have not led a full Lean transformation of a site. I '
       'come from technical operations and projects, not serial manufacturing. **SMED**, **PFEP** and **KANBAN** '
       'I know as methods and have not run them in production. **Digital twins** I have not worked with. My Lean '
       'and Six Sigma is practice, not certification — 5S, standard work, **VSM**, FMEA and DMAIC applied to '
       'processes that were actually failing. What does carry: more than ten years of running operations and '
       'projects to a standard, 37 handovers with zero critical deviations, and AI as something I have built '
       'with — assisted estimation and documentation with a measured productivity gain, and an AI department as '
       'co-owner 2024–2026. Refrigeration is not foreign either: AMU in refrigeration and ventilation technology, '
       'five years at a plant with cooling systems, and respect for anyone who builds an ammonia or CO₂ machine '
       'by hand.', after=26)

    lp('**On the role and the culture.** You describe a role where success depends on the ability to '
       '**"collaborate, coach, and engage teams across the organization to drive sustainable improvements '
       'together"**, on a **"strong presence on the shop floor"**, and on **"translating business strategy into '
       'operational execution and sustainable business results"** — while building **"a culture of problem '
       'solving, accountability, and continuous improvement"**. That is the culture I have tried to build '
       'everywhere: **"teamwork, problem solving, accountability, and continuous learning"**, a willingness to '
       '**"Share best practices across departments"** rather than defend a local optimum, and the kind of '
       'coaching where **"Develop leadership capabilities through coaching, mentoring, and development-focused '
       'feedback"** is a calendar item and not a value statement. I bring a **"continuous learning mindset and '
       'willingness to develop Lean expertise"** — and I am comfortable being measured on **"proven ability to '
       'influence stakeholders and drive accountability across all levels of the organization"**, because '
       'without that the tools stay in the workshop.', after=26)

    lp('**Practical.** Based in Måløv, category B licence and own car, ready to travel and to relocate as we '
       'agree. English is my working language and Danish my first. The application goes through your website — '
       'and now rather than later, because **"We continuously review incoming applications."**', after=12)

    m.meta('Kind regards', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('**Leader with full P&L in his own company since 2023 and twelve years in operations, projects and '
           'technical management** — 25 specialists, 14 fitters across 11 simultaneous sites, 12 technicians, 8 '
           'employees including three apprentices. Authorised maskinmester (LV/MV/HV), B.Tech in Technology '
           'Management, PRINCE2 certified, **Lean and Six Sigma as methods in practice** (DMAIC, 5S, VSM, '
           'standard work, FMEA — no certificate). Improvement with a number attached, measured after the change '
           'and not promised before it.', after=52)

    m.section('THE GEMBA — WHAT I LOOK AT')
    for label, body in [
        ('Takt and flow',
         'Where the work waits: at a machine, behind a missing part, between shifts. Waiting is the '
         'one **waste** nobody puts on the project plan, and usually where the **cycle time** goes. How work is '
         'shared between people matters more than how fast each works: **Yamazumi** in one sentence.'),
        ('Standard work',
         'The same job done the same way by two people on two shifts. If it only exists in the best operator\'s '
         'head, the process is not standardised — it leaves with that operator.'),
        ('Andon and escalation',
         'A stop should be cheap, early and expected. When raising a problem is an act of courage, problems '
         'arrive later and larger — and the numbers look fine right up until they do not.'),
        ('Sustainment',
         'The audit, the date and the name. Ninety days on, either the new standard is still running or the '
         'improvement was a visit, not a change.'),
    ]:
        m.bullet(label, body, after=16)

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director', 'ELOHVAC ApS · Copenhagen · May 2023–present',
         '8 employees incl. 3 apprentices · full P&L · estimating, purchasing and delivery',
         [('Measured improvement, not proposed improvement',
           'Workflow, estimating and documentation rebuilt around digital tools with **over 40 % productivity '
           'gain** measured after the change; **KPI** page with four numbers and one owner each, reviewed weekly.'),
          ('Standard work in a small company',
           'Job templates, handover checklists and a written method for what used to be done from memory — in a '
           'company of eight, unwritten knowledge leaves with the person.')]),
        ('Co-owner and CTO / Technical Lead, AI department',
         'Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 (alongside ELOHVAC)',
         '4–10 people · customer solutions from requirement to go-live',
         [('AI in practice, not in theory',
           'AI-assisted analysis, documentation and reporting built into customer deliveries; models and '
           'workflows handed over with instructions the customer could run without us.'),
          ('Two organisations, one plan',
           'Matrix leadership across two companies with written priority agreements; the company has ceased '
           'trading and the department was closed in order.')]),
        ('Senior Commissioning Engineer / Project Manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · GMP/FDA/EMA',
         [('Documentation that survives an audit',
           '**FAT/SAT**, **IQ/OQ/PQ** and change control with **zero critical deviations** at handover on 37 '
           'projects; deviations closed with a named owner, a date and a written cause — the same discipline '
           'sustainment needs.'),
          ('Coaching specialists',
           '25 specialists and external suppliers steered through acceptance criteria and review; operators and '
           'technicians trained before handover.')]),
        ('Project and Workshop Manager', 'Ventek-Air · Copenhagen · Jan 2022–Nov 2022',
         '14 employees · 11 simultaneous site projects',
         [('Capacity, sequence and waste',
           'Daily plan for 11 sites and 14 fitters against delivery dates, materials and subcontractors — '
           'rework and second visits attacked first, because they were the most expensive **waste** in the week.')]),
        ('Operations and Maintenance Manager', 'Biofos (Lynetten) · Copenhagen · Aug 2017–Jan 2022',
         'Wastewater plant in 24/7 operation · SCADA, PLCs, HV switchgear · pumps and cooling systems',
         [('Improvement through measurement',
           '**Over 40 % lower energy consumption** through measurement, re-commissioning and follow-up; **root '
           'cause** analysis and corrective actions with a named owner while the plant kept running.')]),
        ('Electromechanical Technician / Production Team Lead', 'ARJ Engineering · Tehran · Dec 2003–Mar 2010',
         '12 technicians · machine shop · machinery and equipment',
         [('Workshop standards and training',
           'Calibration, fault finding and repair with documented routines; 5S in a machine shop long before I '
           'knew the word for it; 12 technicians trained and followed up.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=16)

    m.section('EDUCATION, CERTIFICATION AND AUTHORISATION')
    m.edu('PRINCE2 certified project manager', 'AXELOS / PeopleCert · certification held')
    m.edu('LEAN and Six Sigma — methods in practice', 'DMAIC, 5S, VSM, standard work, FMEA · no certificate')
    m.edu('B.Tech, Technology Management and Mechanical Engineering',
          'Copenhagen School of Marine and Technical Engineering · 2017–2022 · GPA 7.6/12')
    m.edu('Authorised maskinmester (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('Refrigeration and ventilation technology · AMU',
          'Mercantec 2021 · STCW, Danish Maritime Authority 2021')
    m.edu('Electrical and mechanical engineering design, electrical engineering',
          'Tehran Technical University · 2000–2003 · EQF 6')

    m.section('LANGUAGES, IT AND PRACTICAL')
    m.para('**Professional English** (working language in documentation, suppliers and international colleagues) '
           '· Danish (first language) · Persian (mother tongue) · **IT**: **Excel** models for capacity, cost and '
           '**KPI** reporting, **ERP** and CMMS, **Python** for own analysis, AI-assisted workflows · Måløv today, '
           'ready to travel and to relocate as agreed · category B licence and own car · available after '
           'agreement.', after=32)

    m.models_table('THE ROLE AS ADVERTISED — WHAT I BRING', ('Requirement', 'Evidence'), [
        ('Bachelor\'s degree in Engineering, Manufacturing, Industrial Engineering or a related field',
         'B.Tech in Technology Management and Mechanical Engineering (2017–2022, GPA 7.6/12) plus an authorised '
         'maskinmester (LV/MV/HV) — engineering rather than industrial engineering.'),
        ('Minimum 10 years in Continuous Improvement, Lean Manufacturing, Production Engineering or Operational '
         'Excellence',
         'Twelve years in operations, production support and technical management, plus eight in a machine shop; '
         '**Lean** and **Six Sigma** methods applied inside that work, not as a job title — an honest difference.'),
        ('Led or actively participated in a full Lean transformation',
         'Participated, not led: improvements inside GMP/FDA projects and in my own company. A full site-wide '
         'Lean transformation I have not run — the main thing I would be learning here.'),
        ('Experience working in a manufacturing environment',
         'Production support in a pharmaceutical plant (37 projects, audits without notice), a machine shop with '
         '12 technicians and a 24/7 process plant — manufacturing, though not serial assembly.'),
        ('Knowledge of Lean principles and Continuous Improvement methodologies',
         'DMAIC, 5S, **VSM**, standard work and FMEA used on processes that were failing, with a measured effect '
         'afterwards; the principles are what I default to when a process misbehaves.'),
        ('Familiarity with 5S, Standard Work, Visual Management and basic problem-solving techniques',
         '5S in a workshop and a technical office; standard work written with the people doing the job; boards '
         'with four numbers and an owner; 5-why and **root cause** as the first reflex.'),
        ('Experience developing leadership capabilities and driving organizational change',
         '**Leadership development** and **change management** through people, not rollouts: 25 specialists on 37 '
         'projects, 14 fitters across 11 sites, three apprentices trained — and the difficult conversations.'),
        ('Strong analytical and organizational skills',
         'One page, four numbers, same definitions weekly; **KPI** reporting built in Excel and Python because '
         'the alternative was guessing in a meeting.'),
        ('Good communication and teamwork abilities',
         'Twenty years at the interfaces where operators, technicians, quality, customers and authorities each '
         'need a different sentence about the same problem — in writing and in the room.'),
        ('Ability to work effectively with shopfloor employees, supervisors and leaders',
         'My working day has always started on the floor: fitters, technicians, operators and apprentices — and '
         'then the same conversation one level up, with the numbers intact.'),
        ('Proven ability to influence stakeholders and drive accountability across all levels',
         'No formal authority over most people I had to move: suppliers, subcontractors, project owners, plant '
         'management. What worked was a written decision, a date and a follow-up that happened.'),
        ('Proactive and hands-on approach to problem solving',
         'Comfortable in the detail: I have climbed into the plant, read the drawing and then written the '
         'decision note — in that order, and often on the same day.'),
        ('Continuous learning mindset and willingness to develop Lean expertise',
         'B.Tech taken alongside full-time work 2017–2022, maskinmester authorisation in 2023, PRINCE2 — and a '
         'genuine appetite for the parts of Lean I have used least, **SMED** and **PFEP** included.'),
        ('Professional English; the role reports to a leader outside the local organisation',
         'English is my working language in documentation, international suppliers and colleagues; Danish is my '
         'first language, which helps with the shop floor in Denmark.'),
        ('Lead the implementation of Continuous Improvement and Lean Manufacturing initiatives across the site',
         'Deployment from the project side: 37 initiatives rolled out across a plant organisation with acceptance '
         'criteria and audits, steered through **strategy deployment** — objectives that reach the area.'),
        ('Initiate, plan and lead Kaizens aligned with operational and business objectives',
         'Improvement run as a project: objective, owner, baseline, change, verification, closure. I have not '
         'facilitated classic **Kaizen** weeks; the discipline around them I have practised for years.'),
        ('Collect, analyze and present operational data to identify improvement opportunities',
         'Data before opinion: capacity, **cycle time**, cost per unit, deviations and **KPI** trends collected, '
         'analysed and presented to people who then had to make a decision on it.'),
        ('Challenge and help departments achieve productivity, quality, delivery and cost targets',
         'All four numbers have been mine at some point, with my own money at risk — which is why I challenge '
         'with a number rather than an opinion, and help before I judge.'),
        ('Support Shopfloor Daily Management, visual management and standardized work instructions',
         'Daily management in practice: a fixed weekly rhythm, a board, named owners, and instructions written '
         'for the person who has to use them at 06:00.'),
        ('Teach Problem Solving to the leadership and across the plant',
         'Teaching as part of delivery: operators and technicians trained before handover on 37 projects, '
         'apprentices taught the trade, and leaders taught to read the numbers they own.'),
        ('Track and ensure sustainment of implemented Kaizens and Continuous Improvement initiatives',
         'Sustainment as an audit with a date and a name; the equivalent discipline is 37 handovers with zero '
         'critical deviations and standards that held when audit came unannounced.'),
        ('Monthly reporting of Kaizen implementation and sustainment activities',
         'Monthly reporting built and run: what started, what is alive, what quietly died and what happens next '
         '— one page, sent whether or not the news was good.'),
        ('Preferred: facilitating Kaizen events, KPI monitoring and performance reporting, hands-on experience '
         'with digital twins and AI',
         '**KPI** monitoring and reporting yes, in Excel, ERP and Python. **Digital twins** no. AI yes, '
         'hands-on: workflows in daily use and an AI department as co-owner 2024–2026.'),
    ], widths=(2500, 7846))

    m.section('FIRST 90 DAYS')
    for b in (
        'Weeks 1–3: on the floor, every shift at least once, with no slides. Learn the process, the takt, the '
        'board and the language people actually use for their problems.',
        'Weeks 4–6: one page per area with the numbers that already exist, and a daily management rhythm the '
        'supervisors own — no new dashboard until the old ones are trusted.',
        'Weeks 7–10: one Kaizen on a real bottleneck, chosen from data, with a written standard, a named owner '
        'and a date to check it is still running.',
        'Weeks 11–13: the sustainment list for everything improved before I arrived — alive or dead — plus the '
        'next three candidates, and a talk with the Plant Manager about what I got wrong.'):
        m.bullet('', b, after=14)

    m.section('WHAT I WOULD ASK')
    for b in (
        'Which site is this for, and how mature is continuous improvement there — Kaizen cadence, daily '
        'management boards, standard work?',
        'What does the Plant Manager need most in six months: a problem-solving system, a pipeline of '
        'improvements, or leadership behaviour on the floor?',
        'How is the BSL community in EMEA organised — what would I share, and what would I learn?'):
        m.bullet('', b, after=14)

    m.para('**A conversation — and a walk along the line first.** +45 93 99 95 14 · ajlooshahram@gmail.com.',
           after=16)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_JohnsonControls_BusinessSystemLeader.docx')
    build(out)
    print(out)
