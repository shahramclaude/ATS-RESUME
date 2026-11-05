# -*- coding: utf-8 -*-
"""Schneider Electric — Senior Project Manager, Major Project Execution (Ballerup, req. 113267).

English deliverable (the posting is English): task-first application page + CV in one document.
Culture and role intel: master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md (Schneider Electric section).
Policy: master/README.md — extreme confidence, no caveats.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Senior Project Manager · Large-scale execution, commissioning and handover'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('5 November 2026')
    m.meta('Schneider Electric Danmark A/S · Ballerup · Senior Project Manager, Major Project Execution '
           '(113267)')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Senior Project Manager, Major Project Execution', bold=True, color='1A1A1A')
    m.para('To Customer Projects, Solutions and Services', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('A large project is not delivered at the end. It is delivered in the order in which things are built — '
           'the dependency that was planned, the subcontractor who arrived when the predecessor was finished, the '
           'panel that was tested before it left the workshop, and the commissioning that proves the building does '
           'what the functional description promised. Where that order is right, the project looks calm. Where it '
           'is wrong, the last three weeks are spent explaining. Keeping it right is the job I am applying for.',
           after=80)

    m.para('**I run projects on four fixed things.** First, the **plan with its dependencies**: predecessors, '
           'float, critical path and a three-week look-ahead that the site actually works to — in MS Project and on '
           'the wall, with the same dates in both places. Second, the **money and the buy-out**: scope split into '
           'packages, subcontracts that say what is and is not included, and monthly follow-up on earned value, '
           'committed cost and forecast, so a deviation is a number in week 20 rather than a surprise in month 11. '
           'Third, the **interfaces and the site**: one coordination meeting a day with the trades, permits, LOTO '
           'and safe work practices in place, and one named owner for every interface — because interface risk is '
           'the risk that most often becomes a delay. Fourth, **commissioning and the handover**: FAT before '
           'shipment, SAT on site, loop checks, IQ/OQ/PQ where the customer is regulated, change control that is '
           'written before the change rather than after, and an as-built package an operator can actually use.',
           after=80)

    m.para('I have done this from the contractor side, which is the side this role sits on — construction, '
           'infrastructure, building technology and automation, from design to handover. At **ELOHVAC**, which I '
           'have owned since 2023, I hold full P&L with five electricians and three apprentices: tender, buy-out, '
           'subcontractors, procurement, cash and margin — and the customer relationship that decides whether the '
           'next project comes. At **Ventek-Air** I was project and workshop manager for **14 people and 11 '
           'concurrent construction projects** of DKK 2–10m each, with daily board meetings and bottleneck '
           'analysis. And at **Novo Nordisk**, from 2022 to 2024, I delivered **37 parallel capital projects** with '
           '25 specialists under GMP, FDA and EMA: acceptance criteria, procurement and vendor management, FAT/SAT, '
           'IQ/OQ/PQ, deviations, change control and an audited handover with **zero critical findings**.', after=80)

    m.para('The technical base is the one you prefer. I am a **chartered marine and electrical engineer** '
           '(maskinmester, B.Tech Technology Management & Mechanical Engineering) with Danish electrical '
           'authorisation at **LV, MV and HV** — so BMS, electrical systems, automation and SCADA are not adjacent '
           'disciplines to me, they are the material I have spent twenty years building with. I have commissioned '
           'HVAC and BMS installations, walked panels with the panel builder, signed loop checks, tuned control '
           'loops against a setpoint, and used SCADA and trend data to prove that a system does what it was bought '
           'to do. That is also why I can hold a subcontractor to a scope: I know what the work involves, and I can '
           'see when it has not been done.', after=80)

    m.para('On the commercial and compliance side, nothing in this role is new to me. **Quality assurance and '
           'change management**: a documented change is cheaper than a rebuilt installation. **Compliance**: in '
           'pharma, a missing signature stops a batch release, so documentation is produced with the work and '
           'closed before the milestone. **Reporting**: one page a month that a steering group can read — status, '
           'earned value, forecast, top five risks with owners, and the decisions I need. **Tendering and '
           'pre-sales**: I have priced and won work in my own company, which makes me a better judge of what a bid '
           'can actually be delivered for.', after=80)

    m.para('Schneider\'s own language fits the way I work. **IMPACT** — Inclusion, Mastery, Purpose, Action, '
           'Curiosity, Teamwork — is a description of a good site: mastery is the commissioning that holds, action '
           'is the decision taken this week instead of next, curiosity is asking why the third loop will not settle, '
           'and teamwork is the electrician, the BMS engineer and the customer\'s operator agreeing on a result '
           'rather than defending a scope. **Buildings of the Future** is where I want to be: a building that is '
           'electrified, measured and controlled is also a building that can be handed over with proof instead of '
           'promises — and where sustainability is a number in a report rather than a claim in a brochure. And the **Trust Charter** is how a project survives a bad week — transparency, safety and '
           'doing what you said, especially when the schedule is under pressure.', after=80)

    m.para('Practically: I live in Måløv, five minutes from Ballerup, and I expect to be on site most days — in '
           'this role the site is the office, and the hybrid setup suits me: most days on site, the rest wherever the '
           'work gets done. Danish is my native language and English my professional one, and MS Project, Excel and '
           'the wider Microsoft Office set are everyday digital tools for me; for planning and reporting I '
           'also build my own tools in Python where off-the-shelf reports do not answer the question. I can start by '
           'agreement, and I would welcome a conversation about which major projects your execution team is running '
           'in Denmark over the next year, and where a commissioning background is most useful first.', after=70)
    m.meta('Kind regards', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('Senior project manager with 20+ years from electrical, automation and building-technology delivery on '
           'the contractor side — chartered marine and electrical engineer (B.Tech, EQF 6) with Danish electrical '
           'authorisation LV/MV/HV. Delivered 37 parallel capital projects with 25 specialists under GMP/FDA/EMA: '
           'procurement, FAT/SAT, loop checks, IQ/OQ/PQ, change control and audited handover with zero critical '
           'findings. Ran 14 people and 11 concurrent construction projects at Ventek-Air, and has held full P&L '
           'with five electricians and three apprentices since 2023.', after=80)

    m.section('PROJECT EXECUTION, COMMISSIONING AND HANDOVER')
    for label, body in [
        ('Planning and dependencies',
         'Work breakdown, predecessors, float and critical path; three-week look-ahead with the trades, milestone '
         'plan against the customer, and one set of dates used by site, supplier and steering group alike.'),
        ('Procurement and subcontracting',
         'Scope split into packages, enquiry and bid evaluation, subcontract terms that state inclusions and '
         'exclusions, and vendor management through FAT, delivery and site works.'),
        ('Financial follow-up',
         'Budget, committed cost, earned value and forecast, monthly; change orders priced and approved before the '
         'work, and cash and margin managed with full P&L responsibility since 2023.'),
        ('Commissioning and qualification',
         'FAT/SAT, IO and loop checks, functional testing of sequences and interlocks, IQ/OQ/PQ with traceability, '
         'deviation handling and handover with as-built documentation and operator training.'),
        ('Reporting and governance',
         'One-page monthly report and a short weekly status to the site: plan against actual, cost against '
         'forecast, top risks with owners, and the decisions needed from the steering group.'),
        ('Site leadership and safety',
         'Multidisciplinary teams and subcontractors on live sites: daily coordination, permits, LOTO and safe work '
         'practices, quality inspections and one named owner per interface.')]:
        m.bullet(label, body, after=25)

    m.models_table('TOOLS AND METHODS', ('Task', 'Tool and documented use'), [
        ('Planning and control',
         'MS Project and Excel: WBS, dependencies and critical path, look-ahead, progress and earned value; '
         'Python-generated status packs where standard reports fall short.'),
        ('BMS, electrical and automation',
         'BMS/FMS and SCADA platforms, PLC-based control, panels, drives and instrumentation; loop tuning and '
         'functional testing against a written functional description; electrical authorisation LV/MV/HV.'),
        ('Quality and compliance',
         'ITP and inspection plans, FAT/SAT protocols, IQ/OQ/PQ, traceability matrix, deviation and change control; '
         'GMP/FDA/EMA requirements and audit-ready documentation.'),
        ('Procurement and contract',
         'Enquiry packages, bid comparison, subcontract terms and vendor follow-up; claims and variations '
         'documented as they occur, not reconstructed at the end.'),
        ('Reporting and stakeholders',
         'One-page monthly report: status, earned value, forecast, top five risks with owners and the decisions '
         'required; steering group, customer, consultants and authorities kept on the same information.'),
        ('Digital and data',
         'Python, Claude API, SAP and Excel: progress dashboards, deviation logs, alarm and energy statistics — '
         'over 40 % of administrative work removed from quoting and follow-up in my own company.')])

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director',
         'ELOHVAC ApS · Copenhagen, Denmark · May 2023–present',
         '5 electricians and 3 apprentices · full P&L · commercial and industrial customers',
         [('Delivery and commercial', 'Tender, buy-out, subcontractors and financial follow-up on electrical and '
                                      'HVAC projects; quality, safety and handover owned end to end.'),
          ('Customers and people', 'Recruitment, 1:1s and apprentice training alongside budget, quoting and margin; '
                                   'customers informed the same day something changes.'),
          ('Digital operations', 'Python and Claude API for quotations, schedules, checklists and KPI dashboards; '
                                 'over 40 % productivity gain in the business.')]),
        ('Senior Commissioning Engineer / Project Manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd, Denmark · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · DKK 2–10m each · GMP/FDA/EMA',
         [('Commissioning and qualification', 'Acceptance criteria, FAT/SAT, loop checks, IQ/OQ/PQ, deviation and '
                                              'change control; zero critical findings at audited handover.'),
          ('Stakeholders and reporting', 'Client, consultants, vendors and authorities coordinated through design, '
                                         'execution and handover; progress, cost, risk and resources reported '
                                         'monthly.')]),
        ('Project and Workshop Manager',
         'Ventek-Air · Copenhagen, Denmark · Jan 2022–Nov 2022',
         '14 employees · 11 concurrent construction projects · DKK 2–10m each',
         [('Execution leadership', 'Tenders, calculations, subcontractors and handover packages in ventilation and '
                                   'technical installations; daily board meetings and bottleneck analysis.')]),
        ('Maintenance and Operations Manager / Workshop Technician',
         'Biofos, Lynetten · Copenhagen, Denmark · Aug 2017–Jan 2022',
         '24/7 plant · HVAC, pumps, high-voltage switchgear, SCADA · 24-hour operation',
         [('Operations and fault finding', 'Sensors, actuators and switchgear in daily operation: calibration, '
                                           'troubleshooting, corrective work and alarm handling from SCADA data.'),
          ('Safety and maintenance', 'Plans from condition data, spare-part criticality, LOTO, workplace assessment '
                                     'and permits before every job.')]),
        ('Electromechanical Technician / Production Team Leader',
         'ARJ Engineering · Tehran, Iran · Dec 2003–Mar 2010',
         '12 mechanics and technicians · machine workshop · industrial equipment',
         [('Equipment and team', 'Shift planning and target follow-up; fault diagnosis, root cause and corrective '
                                 'action on production equipment.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('EDUCATION AND AUTHORISATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering',
          'Copenhagen School of Marine Engineering · 2017–2022 · EQF 6 · GPA 7.6/12')
    m.edu('Authorised marine and electrical engineer (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('Electrical and mechanical design, electrical engineering',
          'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Refrigeration and air conditioning · STCW safety', 'Mercantec 2021 · Danish Maritime Authority 2021')

    m.section('LANGUAGES, PRACTICAL AND REFERENCES')
    m.para('Danish: native · English: professional · Persian: native · Driving licence B · Lives in Måløv, five '
           'minutes from Ballerup, on site most days · Available by agreement · MS Project, SAP and Excel daily · '
           'References on request.', after=70)

    m.models_table('WHAT THE ROLE ASKS FOR — MY EVIDENCE', ('Requirement', 'Evidence'), [
        ('Large-scale construction or building-technology projects, contractor side',
         '11 concurrent construction projects of DKK 2–10m (Ventek-Air), 37 parallel capital projects under GMP '
         '(Novo Nordisk) and an owner-led electrical/HVAC business with full P&L since 2023.'),
        ('Onsite leadership through the full lifecycle',
         'Design reviews, procurement and vendor management, site coordination, FAT/SAT, loop checks, IQ/OQ/PQ and '
         'audited handover — the full lifecycle, zero critical findings.'),
        ('BMS, electrical, SCADA or integrated building solutions',
         'Commissioned HVAC, BMS (building management systems) and electrical installations; PLC/SCADA and '
         'BMS/FMS, panels, drives and instrumentation; authorisation LV/MV/HV.'),
        ('Execution, QA, change management and compliance',
         'ITP and inspection plans, acceptance criteria, change control before the change, deviations with root '
         'cause, and audit-ready documentation under GMP/FDA/EMA.'),
        ('Project planning tools and dependencies',
         'WBS, predecessors, float and critical path in MS Project and Excel; three-week look-ahead and milestone '
         'plans agreed with the customer.'),
        ('Procurement, subcontracting and financial follow-up',
         'Enquiry packages, bid evaluation, subcontract terms and vendor follow-up; committed cost, earned value and '
         'forecast with full P&L responsibility.'),
        ('Stakeholder management and interfaces',
         'Steering group, client, consultants, authorities, vendors and trades on one set of information; monthly '
         'one-page reporting with named risk owners.'),
        ('Willing to be onsite, driving execution and stakeholders',
         'On site by preference and by habit: daily coordination with trades and subcontractors, permits and LOTO '
         'before work, and the customer\'s representative met face to face rather than by email.'),
        ('Fluent Danish and English; MS Project',
         'Danish native, English professional; MS Project, SAP and Excel daily, plus Python tooling for dashboards '
         'and status packs.')])
    m.page_break()

    m.models_table('FIRST 90 DAYS — CONTROL, SITE AND HANDOVER', ('Period', 'What happens, and how it is measured'), [
        ('Week 1–2',
         'Read the live project end to end: contract, scope split, plan and dependencies, procurement status, open '
         'changes and the commissioning strategy. Walk the site with the supervisors and the customer\'s '
         'representative. Learn Schneider\'s execution model and reporting before proposing anything.'),
        ('Day 30',
         'One plan with real dependencies and a three-week look-ahead in use on site; the top ten risks listed with '
         'owners and dates; commercial status (committed, forecast, open changes) on one page. Any interface that '
         'is already late is on that page too, with a decision attached.'),
        ('Day 60',
         'Procurement and subcontract packages under control: scope signed, FATs scheduled, deliveries matching the '
         'plan. Monthly report running in a fixed format that the steering group can read without a meeting.'),
        ('Day 90',
         'The project runs on its own numbers, not on my presence: plan, cost, risk and commissioning status '
         'trusted by the customer. At least one execution method improved and shared with the team, so the next '
         'major project starts better than mine did.')])

    m.section('THE PLAN IS A PROMISE TO THE SITE')
    m.para('A schedule that the trades do not believe is worse than no schedule, because it hides the problem. I '
           'build plans from the work backwards, with the durations the people doing the work agree to, and I keep '
           'the number of open dependencies small enough that someone can actually chase them. When the plan moves, '
           'everybody hears it the same day — subcontractor, customer and steering group — because a delay '
           'communicated in week 20 is a rescheduling, and the same delay communicated in month 11 is a dispute.',
           after=80)

    m.section('MONEY IS A TECHNICAL DISCIPLINE')
    m.para('Cost overruns rarely start in the accounts; they start in a scope line nobody wrote down. I buy out '
           'packages with inclusions and exclusions spelled out, price variations before the work rather than after, '
           'and follow committed cost against earned value monthly, so the forecast is a trend rather than a hope. '
           'Running my own company has made me unsentimental about this: margin is decided in the buy-out and in '
           'the change log, not at the final account.', after=80)

    m.section('INTERFACES ARE WHERE PROJECTS SLIP')
    m.para('Most delays on a large site are not caused by slow trades; they are caused by two scopes assuming the '
           'other one had done it. So every interface gets a name, a date and a piece of paper: who delivers what, '
           'to whom, by when, and what the test is. On a live building that discipline shows up as a short daily '
           'coordination with the contractors, permits and LOTO in place before work starts, and a supervisor who '
           'knows the answer when the question arrives at 14:30.', after=80)

    m.section('COMMISSIONING IS WHERE THE PROJECT TELLS THE TRUTH')
    m.para('You can argue about progress; you cannot argue with a loop that will not hold its setpoint. That is why I '
           'want commissioning planned from week one: what will be tested, with what instrument, against which '
           'acceptance criterion, and who signs. FAT before shipment, SAT on site, interlocks tested against the '
           'written requirement, and trend data kept as evidence. The handover package is the product the customer '
           'keeps for the next twenty years, and it should be possible for an operator who was not in the room to '
           'run the building from it.', after=80)

    m.section('QUALITY, SAFETY AND COMPLIANCE IN ONE SYSTEM')
    m.para('Quality, safety and compliance are not three processes; they are the same habit of writing down what was '
           'agreed and proving it was done. Inspection and test plans, permits and workplace assessments, change '
           'control and deviations all live in the same documentation and are closed before the milestone, not '
           'after. In the pharma projects I delivered, an inspector could follow any requirement to a signed test '
           'result — and that is the standard I would bring to a major project at Schneider.', after=80)

    m.section('ONE PAGE THE STEERING GROUP CAN READ')
    m.para('Reporting is not administration; it is how a project keeps its mandate. Once a month I want one page: '
           'where we are against the plan, cost against forecast, the top five risks with a name and a date, what '
           'is waiting for a decision, and what I need from the steering group. If a project is in trouble, that '
           'page says so before anyone has to ask — because the value of a project manager is measured by how early '
           'the bad news arrives, not by how rarely it does.', after=80)

    m.section('TENDERING MAKES YOU A BETTER DELIVERER')
    m.para('Having priced and won work myself, I read a tender the way the delivery team will: where the risk is '
           'hidden, which scope line is optimistically thin, and what the customer actually needs rather than what '
           'the specification lists. That is useful in pre-sales — and it is the reason I can commit to a date in '
           'a bid meeting and still be comfortable with it when the contract is signed.', after=80)

    return m.save(path, title='Application and CV — Senior Project Manager, Schneider Electric',
                  subject='Large-scale project execution, commissioning and handover',
                  keywords='senior project manager, project execution, commissioning, BMS, SCADA, procurement, '
                           'subcontracting, change management, handover')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Schneider_SeniorProjectManager.docx')))
