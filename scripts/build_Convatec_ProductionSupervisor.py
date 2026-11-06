# -*- coding: utf-8 -*-
"""Convatec (Infusion Care, Osted) — Production Supervisor, day shift.

English deliverable (the posting is English): application page + CV in one document.
Policy: master/README.md — extreme confidence, no caveats.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Production Supervisor · Medical devices, clean room and the shift that delivers'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('6 November 2026')
    m.meta('Convatec · Infusion Care, Osted · Production Supervisor, day shift')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Production Supervisor, Convatec', bold=True, color='1A1A1A')
    m.para('To the Production Manager and the hiring team at Convatec, Osted', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('An infusion set is a small device with an unusually direct line to a person. Somebody connects it in the '
           'morning, trusts it for a day, and never thinks about the shift that produced it. That trust is decided '
           'in the clean room, a thousand times per shift, at the machine and at the documentation — and the '
           'supervisor is the person who makes the right decision the easy one and the shortcut the difficult one. '
           'That is the job I want, and it is the job I have been doing in different regulated settings for twenty '
           'years.', after=80)

    m.para('**I would run the shift as team leader for the operators and coordinators on four fixed things.** First, '
           '**the shift starts before the shift**: the staffing model checked against the production plan, resources '
           'and quality demands matched to the production targets, absence and holidays known early, vacation planning '
           'done months ahead with the resource coordinators instead of in the week it hurts. Second, **training is '
           'the flexibility you actually have**: a live cross-training matrix per machine and process group, so '
           'sickness, summer and overtime never depend on one person, and competence is signed off rather than '
           'assumed. Third, **the numbers are honest and visible**: output against plan, the three components an '
           'OEE is built from — availability, performance, quality — plus absence and deviations, on a board the '
           'shift can read at handover, not in a report a month later. Fourth, **GMP, GDP and 5S are the job, not '
           'an audit**: records written in the room while the work happens, deviations raised on the shift they '
           'occur, CAPA closed at the point of cause, and a 5S standard that is visible the moment you walk in.',
           after=80)

    m.para('Regulated production is my home ground. At **Novo Nordisk** in Kalundborg and Bagsværd I worked inside '
           'a **GMP/FDA/EMA** system for nearly two years: SOPs, change control, deviations, **CAPA**, root cause '
           'analysis, qualification to IQ/OQ/PQ and FAT/SAT — and I delivered **37 parallel capital projects** with '
           '25 specialists through audited handover with **zero critical findings**. I have worked inside GMP '
           'production buildings where gowning, airlocks and controlled areas are part of an ordinary working day, '
           'and where a record that is written afterwards is worth nothing.', after=80)

    m.para('The people side is not a theory for me either. Since 2023 I have run **ELOHVAC** with full P&L and '
           '**five electricians and three apprentices**: recruitment, one-to-one and appraisal conversations, '
           'training plans, absence follow-up, overtime approval, budgets, and the conversations nobody enjoys. Before that I '
           'led **14 employees and 11 concurrent projects** at **Ventek-Air** with daily board meetings and capacity '
           'planning, and **12 technicians** at **ARJ Engineering** in a machine workshop where shift planning, '
           'training and output targets were the daily measurement. Skilled-trade teams tell you quickly whether a '
           'leader is present; mine have stayed, and the apprentices I trained are still in the trade.', after=80)

    m.para('Standards and improvement I have practised where they cost something. For five years I was operations '
           'and maintenance manager at **Lynetten under Biofos**, a critical plant in 24/7 shift operation: 5S, '
           'standard work and PDCA on the workshop and the stores, safety discipline with LOTO and APV, and '
           'KPI follow-up on availability, breakdowns and response times. Energy management on metering and SCADA '
           'data delivered **more than 40 % lower consumption**, documented — which is what continuous improvement '
           'looks like when it is finished rather than started. In my own company I build the measurement tools '
           'myself in Python and Claude, and the same habit applies on a shift: the number on the board is the '
           'number we act on, not the one that makes the month look good.', after=80)

    m.para('Convatec makes single-use devices for people managing a chronic condition, and the Osted site has just '
           'been expanded with new cleanroom capacity and a new machine park. Growth like that puts pressure exactly '
           'where a supervisor stands: new equipment, new operators, more documentation, same quality standard. Your '
           'values — **improve care, deliver results, grow together, own it, do what\'s right** — describe the '
           'leader a shift in a controlled environment needs, and **forever caring** is a promise that is kept or '
           'broken at the machine, by the operator, on my shift.', after=80)

    m.para('Practically: I live in Måløv, Osted is about forty-five minutes by car, and I work the day shift without '
           'drama — **driver\'s licence (B)**, fluent **Danish and English**, and I can start by agreement. I would '
           'like to hear where the shift stands on cross-training and absence today, and which machine group is the '
           'hardest to staff in a holiday week — that is where I would start.', after=70)
    m.meta('Kind regards,', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('Production and operations leader with 20+ years in regulated manufacturing, capital projects and 24/7 shift '
           'operation — authorised machine and electrical installer (LV/MV/HV) and B.Tech degree in Technology '
           'Management & Mechanical Engineering. Nearly two years inside a GMP/FDA/EMA system at Novo Nordisk with '
           'SOPs, deviations, CAPA, change control and qualification, and 37 capital projects handed over with zero '
           'critical findings. Led 5 to 14 people with full P&L: recruitment, one-to-ones, training plans, absence '
           'follow-up and staffing against a model. Lean practice in 5S, standard work and PDCA, with KPI and OEE '
           'logic on a board the shift can read.', after=80)

    m.section('PRODUCTION, PEOPLE AND QUALITY')
    for label, body in [
        ('Shift leadership and daily operations',
         'Daily board meetings with output against plan, machine status, quality issues and staffing for the next '
         'shift; priorities set with the production manager and resource coordinator, the handover written so the '
         'next shift starts informed, and the process streamlined wherever it costs a step.'),
        ('Staffing, absence and training',
         'Staffing against an agreed model, absence and absenteeism followed up individually and early, overtime '
         'approved with a reason, vacations planned months ahead against the production plan; and a competence matrix per machine '
         'group showing who is signed off, who is in training and who is the only person who can run a line.'),
        ('People management',
         'Recruitment, 1-1 meetings and appraisal conversations, employee development agreed with the '
         'production manager, and the difficult conversations held early and fairly — disciplinary actions handled '
         'by procedure, not by mood.'),
        ('GMP, GDP and quality systems',
         'Records completed in the room as the work happens, deviations raised on the shift, NC and CAPA taken to '
         'root cause and closed at the point of cause; audit-ready documentation from 37 projects with zero critical '
         'findings in a GMP/FDA/EMA system, written as if the accreditation body were already in the room.'),
        ('Continuous improvement and 5S',
         '5S, standard work, PDCA, A3 and value stream mapping used as daily practice, not as a campaign; '
         'improvement ideas raised by the shift and taken forward with production management and support functions '
         'until they are standard.')]:
        m.bullet(label, body, after=25)

    m.models_table('TOOLS AND METHODS', ('Task', 'Tool and documented use'), [
        ('KPI and OEE',
         'Output against plan, availability, performance and quality from production, SCADA and asset data; absence, '
         'deviations and rework on the same board, followed weekly.'),
        ('Quality system',
         'SOPs, change control, deviations, NC and CAPA, root cause analysis (5-why, Ishikawa, A3); qualification to '
         'IQ/OQ/PQ and acceptance through FAT/SAT in a GMP/FDA/EMA environment.'),
        ('Lean',
         '5S and visual management, standard work, PDCA, value stream mapping and Kaizen; continuous improvements '
         'followed on a daily board until they become standard, and the nerve to streamline a process that works but '
         'costs a step too many.'),
        ('People and staffing',
         'Recruitment and onboarding, one-to-one and appraisal conversations, competence matrix and cross-training '
         'plans, absence follow-up and vacation planning.'),
        ('Systems',
         'SAP ERP for orders, cost and asset data; time attendance, absence and overtime approval owned as a manager; '
         'Excel and Python for the follow-up that the standard reports do not show.'),
        ('Safety',
         'APV and risk assessment, LOTO, work permits and near-miss reporting in 24/7 operation; safety rounds and '
         'toolbox talks as part of the week.')])

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director',
         'ELOHVAC ApS · Copenhagen · May 2023–present',
         '5 electricians and 3 apprentices · full P&L · electrical installation and service',
         [('People, staffing and delivery',
           'Recruitment, one-to-ones, training plans, absence follow-up and overtime approval for a team of eight; '
           'deliveries planned against customer deadlines and quality requirements, with documentation delivered '
           'with each job.')]),
        ('Senior Commissioning Engineer / Project Manager, Electrical Systems',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · 2–10 million DKK each · GMP/FDA/EMA',
         [('Regulated quality, planning and audit',
           'SOPs, change control, deviations and CAPA in a GMP system; IQ/OQ/PQ and FAT/SAT across 37 projects, '
           'handed over with zero critical findings; schedules broken into milestones and reported monthly in SAP.')]),
        ('Project and Workshop Manager',
         'Ventek-Air · Copenhagen · Jan 2022–Nov 2022',
         '14 employees · 11 concurrent jobs · 2–10 million DKK per job',
         [('Prioritisation and daily direction',
           'Daily board meetings, capacity and bottleneck analysis across eleven concurrent jobs; priorities re-balanced '
           'the same day when a machine or a person was lost.')]),
        ('Operations and Maintenance Manager',
         'Lynetten under Biofos · Copenhagen · Aug 2017–Jan 2022',
         'Process plant in 24/7 shift operation · pumps, blowers, ventilation, transformers, switchgear and SCADA',
         [('Shift operation, 5S and KPIs',
           '24/7 shift rota with absence cover and handover discipline; 5S, standard work and PDCA on workshop and '
           'stores; availability, breakdown and response time on the board, with over 40 % lower energy consumption '
           'documented.')]),
        ('Electromechanical Technician / Production Supervisor',
         'ARJ Engineering · Tehran · Dec 2003–Mar 2010',
         '12 mechanics and technicians · machine workshop · industrial equipment',
         [('Shift planning and competence',
           'Shift planning, training and follow-up on output and quality targets for 12 technicians; root cause '
           'analysis and corrective action on production equipment.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('EDUCATION AND AUTHORISATION')
    m.edu('B.Tech degree, Technology Management & Mechanical Engineering',
          'Maskinmesterskolen København · 2017–2022 · GPA 7.6/12')
    m.edu('Authorised machine and electrical installer (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('Electrical and mechanical engineering', 'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Refrigeration, ventilation and safety training · STCW', 'Mercantec 2021 · Danish Maritime Authority 2021')

    m.section('LANGUAGES, PRACTICAL AND REFERENCES')
    m.para('Danish: native · English: fluent, written and spoken · Persian: native · Driver\'s licence B and car · '
           'Based in Måløv, Osted around forty-five minutes by car · Day shift, Monday to Friday, onsite · Available '
           'by agreement · SAP, Excel and Python daily · References on request.', after=70)

    m.models_table('WHAT THE ROLE ASKS FOR — MY EVIDENCE', ('Requirement', 'Evidence'), [
        ('5+ years of people management in production',
         'Eight people with full P&L since 2023 — hiring, terminations, overtime approval and absence follow-up owned '
         'end to end; 14 employees and 11 concurrent jobs at Ventek-Air; 12 technicians in a machine workshop at ARJ; '
         '25 specialists led across 37 capital projects at Novo Nordisk.'),
        ('Medical device, pharma or life science production',
         'Nearly two years inside a GMP/FDA/EMA system at Novo Nordisk: SOPs, deviations, CAPA, change control, '
         'IQ/OQ/PQ and audit, with zero critical findings across 37 projects — regulated manufacturing where the '
         'record is part of the product, and an auditor can ask for any part of it.'),
        ('Managing employees in a production environment',
         'Recruitment, one-to-ones, appraisal and development conversations, training and cross-training plans, '
         'absence follow-up, overtime approval and disciplinary conversations — held in skilled-trade teams where '
         'expectations are explicit.'),
        ('Planning, prioritisation and reporting on daily operations',
         'Daily boards and capacity planning across 11 concurrent jobs and a 24/7 shift rota; production plans '
         'broken into milestones and reported weekly and monthly to management and client.'),
        ('KPIs and OEE',
         'Availability, performance and quality measured from production, SCADA and asset data; output against plan, '
         'deviations and absence on one board — and the discipline to explain a number that moved for the wrong '
         'reason.'),
        ('Lean Six Sigma and continuous improvement',
         '5S, standard work, PDCA, A3, value stream mapping, Kaizen and root cause analysis applied daily; energy '
         'management on metering and SCADA data with over 40 % lower consumption documented.'),
        ('QMS, GMP, GDP, NC, CAPA and a safe work environment',
         'Deviations and NC raised and closed in a GMP system, CAPA verified for effect; 5S and visual standards '
         'owned on workshop and stores; APV, LOTO, work permits and near-miss reporting in live operation.'),
        ('Staffing model, cross-training, vacation and absence',
         'Staffing against an agreed model, competence matrix per machine group, vacation planned months ahead with '
         'the resource coordinators, and absence followed up individually and early.'),
        ('Fluent English, SAP competence, collaboration',
         'Fluent English in written and spoken reporting to management, auditors and clients; SAP in daily use and '
         'competence built in the team; cross-functional work with engineering, quality, supply chain and projects.')])
    m.page_break()

    m.models_table('FIRST 90 DAYS — THE SHIFT, THE MATRIX AND THE BOARD', ('Period', 'What happens, and how it is measured'), [
        ('Week 1–2',
         'Walk the line on every machine group, at the machine and in the documentation. Read the shift handover, the '
         'deviation log, the absence figures and last quarter\'s output against plan. Sit with the coordinators and '
         'the Production Manager, and get the ProMark registrations and approvals caught up so nothing waits at '
         'period end.'),
        ('Day 30',
         'A one-page picture of the shift as it actually runs: staffing against the model, competence per machine '
         'group, where the handover loses information, the three absence drivers and the two machine groups that are '
         'hardest to cover.'),
        ('Day 60',
         'Cross-training plan agreed and started, with named people and dates; vacation plan for the next peak '
         'locked with the resource coordinators; board redesigned around output against plan, OEE components, '
         'quality and absence — readable in five minutes at handover.'),
        ('Day 90',
         'Team staffed and trained to the model with absence trending down; one improvement from the shift taken from '
         'idea to standard with production management; NC and CAPA closed within the agreed time; 5S and GMP '
         'standards visibly held — and every operator able to say what the shift is measured on.')])

    m.section('QUALITY IS DECIDED AT THE MACHINE, NOT AT THE AUDIT')
    m.para('A medical device cannot be inspected into compliance. By the time quality assurance looks at a batch, '
           'the decisions have already been made — how the machine was set, whether the deviation was raised, whether '
           'the record was written while it was true. So the supervisor\'s work is to make the correct behaviour the '
           'cheapest one: equipment that is in calibration, instructions that can be followed in a gown, a deviation '
           'that is reported without punishment, and a shift that knows the difference between a small problem '
           'written down and a small problem hidden.', after=80)

    m.section('THE HANDOVER IS A QUALITY DOCUMENT')
    m.para('Most production losses I have seen were not made on a machine; they were inherited at a handover. A '
           'machine left in a doubtful state, a batch with a question mark, a training gap nobody mentioned. So the '
           'handover gets written the way a GMP record is written: what ran, what stopped, what was deviated, what '
           'the next shift must watch. Ten honest lines at the end of a shift save the next shift two hours of '
           'finding out.', after=80)

    m.section('ABSENCE IS A PLANNING PROBLEM BEFORE IT IS A PERSONNEL PROBLEM')
    m.para('A team that is short-staffed every Monday will have high absence, and no amount of reminders fixes it. '
           'The order is: staff to the model, cross-train so cover exists, plan holidays against the production plan, '
           'approve overtime with a reason, and then follow up individually with the people who are away — early, '
           'concretely, and with the same conversation for everyone. Most absence falls when the shift stops feeling '
           'like a place where being away is easier than being there.', after=80)

    m.section('TRAINING IS THE ONLY REAL FLEXIBILITY')
    m.para('Flexibility in a cleanroom does not come from asking people to do more; it comes from a competence matrix '
           'that shows, machine group by machine group, who is signed off, who is in training and where the single '
           'points of failure are. Then the training plan is written from the production plan: the next peak, the '
           'next holiday, the next new line. An operator signed off on three machine groups is worth more to the '
           'shift than any overtime budget, and the operator knows it.', after=80)

    m.section('IMPROVEMENT HAS TO END IN A STANDARD')
    m.para('Ideas from a shift are the cheapest improvement a factory has, and they die in the same way every time: '
           'nobody owns them, nothing is measured, and the next audit finds the old practice. So an idea gets an '
           'owner, a date and a number it should move; when it works it is written into the standard work and the '
           'training, and when it does not, we say so and stop. That discipline is also what makes a value like "own '
           'it" real on a shopfloor — the shift can point at the thing that changed because they raised it.', after=80)

    m.section('A SHIFT IS MANAGED IN THE FIRST HOUR')
    m.para('Most of what a shift becomes is decided before the machines are running: who is where, which line starts '
           'first, what the plan assumes, who is short, and what was left over from yesterday. So the first hour is '
           'where I spend my presence — walk the line, read the handover, agree the priorities with the coordinators '
           'and the Production Manager, and fix the staffing before the first stoppage instead of during it. After '
           'that the shift runs itself, and my job is to be visible, ask the second question, and take the decisions '
           'that need a leader rather than a meeting.', after=80)

    return m.save(path, title='Production Supervisor — Convatec, Osted',
                  subject='Production supervision, clean room quality, staffing and continuous improvement',
                  keywords='production supervisor, medical devices, clean room, GMP, GDP, CAPA, 5S, OEE, Lean, '
                           'staffing, cross-training, absence follow-up, ProMark, SAP, shift leadership')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Convatec_ProductionSupervisor.docx')))
