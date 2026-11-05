# -*- coding: utf-8 -*-
"""Novo Nordisk A/S — BMS Supporter (Adv. Utilities Professional), DPM Bagsværd.

English deliverable (JD is English): task-first application page + CV in one document.
Culture and role intel: master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md,
section on Novo Nordisk DPM Bagsværd (research 05.11.2026).
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'BMS, utilities and validation · Improvements in an aseptic filling plant'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('5 November 2026')
    m.meta('Novo Nordisk A/S · Site Bagsværd, DPM BA · BMS Supporter (Adv. Utilities Professional)')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: BMS Supporter — Facility and Utility Projects', bold=True, color='1A1A1A')
    m.para('Dear Ehab El-sayed', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('In an aseptic filling factory the utilities are not building services. WFI, clean steam, compressed air and '
           'HVAC are the conditions that make a batch valid, and a change in the BMS is therefore a GMP change before '
           'it is an engineering one. That is the part of this role I find worth doing: one line in a specification '
           'becomes a thousand details on the floor — tag lists, alarm limits, I/O checks, calibration, '
           'requalification — and it all has to be right before the line restarts.', after=80)

    m.para('**I would work the projects from four fixed points.** First, plan backwards from the production stop. The '
           'two annual stops are the deadline, not the start, so everything that can be prepared is prepared before '
           'the factory stops: user requirements, design review, FAT, contractor access, spare parts, test scripts '
           'and permits. During the stop there should be execution and verification left — nothing else, because the '
           'stop has no slack. Second, every alarm must have a reason: what is monitored, at which limit, with what '
           'consequence and who acts on it. A cleanroom where the alarm list has grown for ten years hides the one '
           'signal that matters, and alarm rationalisation is one of the cheapest quality improvements available. '
           'Third, validation is written alongside the change, not afterwards — requirements, risk assessment, '
           'IQ/OQ/PQ and a traceability matrix that can be read by someone who was not in the room. Fourth, '
           'contractors on a live plant: one coordination meeting a day during the stop, one plan, one accountable '
           'person per scope, and access, permits and cleanroom behaviour agreed before anyone arrives.', after=80)

    m.para('I have done this work in your own organisation. From 2022 to 2024 I was at Novo Nordisk as senior '
           'commissioning engineer and project manager on electrical systems, with 37 parallel capital projects and '
           '25 specialists in Kalundborg and Bagsværd: documented acceptance criteria, FAT and SAT, IQ/OQ/PQ, '
           'deviation handling and audited handover with zero critical findings. Before that, five years of '
           'maintenance and operations on a 24/7 plant at Biofos — pumps, HVAC, high-voltage switchgear and '
           'SCADA-based condition monitoring, LOTO, APV, near-miss routines and a PDCA programme that took 40 % off '
           'the energy cost. That is where I learned that a control system is only as good as the sensor loop behind '
           'it, and that an alarm nobody trusts is worse than no alarm at all.', after=80)

    m.para('What I would bring to Facility and Utility Projects is the combination of the three disciplines this role '
           'sits between. I am an authorised marine engineer with electrical authorisation and a B.Tech in Technology '
           'Management and Mechanical Engineering, so I can read the P&ID and the electrical drawing as well as the '
           'automation specification. I have run projects in a GMP environment where the documentation is part of the '
           'deliverable, not an appendix. And I am used to speaking to both the automation engineer and the skilled '
           'worker on the floor — the same message, in the language each of them needs, which is most of what '
           'coordination actually is.', after=80)

    m.para('I will be straight about the gap. I have not worked with BMS or FMS in a pharmaceutical plant before, and '
           'I have not owned utility systems in an aseptic facility. Your posting calls BMS/FMS useful but not '
           'essential, and I read that correctly: the system I would have to learn, the discipline around it — change '
           'control, validation, alarms, shutdown planning — is what I have been doing for years. I would spend the '
           'first weeks with your engineers and skilled workers in the plant and in the system, and I would rather '
           'ask one question too many in week two than discover the answer during a stop.', after=80)

    m.para('What draws me back to Novo Nordisk is that the purpose is measurable. The products made in Bagsværd — insulin, GLP-1 and weight-management medicines — are '
           'the reason a utility project matters to patients, and the Novo Nordisk Way is unusually concrete about it: we never '
           'compromise on quality and business ethics, we are open and honest, and we speak up. That last part is not '
           'a slogan in a factory that cannot stand still — it is the mechanism that stops a small deviation from '
           'becoming a stopped line, and it fits the way I work anyway.', after=80)

    m.para('Practically: I live in Måløv, about ten minutes from Bagsværd. I speak Danish natively and English '
           'professionally, written and spoken, which is the working reality in an international organisation. I am '
           'available for both production stops, including the July/August and December/January periods, and I am '
           'used to shutdown work from 24/7 operations. I am also an active Claude coder and build my own Python '
           'tools for documentation and follow-up — traceability matrices, test and deviation logs, and investment '
           'cases with NPV, IRR and scenarios when equipment is to be replaced.', after=80)

    m.para('I would like to come to Bagsværd, walk the utility areas with you and your team, and talk through how I '
           'would prepare the next stop — and where I think the quickest quality gains are in the alarm and '
           'documentation setup.', after=80)
    m.meta('Kind regards', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('Project and commissioning engineer with 20+ years from technical operations, regulated production and '
           'utilities — authorised marine engineer (maskinmester) with electrical authorisation and a B.Tech in '
           'Technology Management and Mechanical Engineering. Two years at Novo Nordisk with 37 parallel capital '
           'projects under GMP/FDA/EMA, FAT/SAT and IQ/OQ/PQ, zero critical findings at handover; five years of '
           'maintenance and operations on a 24/7 plant with SCADA, HVAC, pumps and high-voltage switchgear. Works '
           'from requirements, alarm lists and a shutdown plan.', after=80)

    m.section('UTILITIES, VALIDATION AND RESULTS')
    for label, body in [
        ('Validation and qualification',
         'FAT/SAT and IQ/OQ/PQ across 37 capital projects with documented acceptance criteria, deviation handling and '
         'audited handover; zero critical findings. Traceability from requirement to test, written for the next '
         'reader rather than for the auditor.'),
        ('Control systems and monitoring',
         'Five years with SCADA-based condition monitoring, sensor loops, alarm handling and remote operation on a '
         '24/7 plant; fault finding on instrumentation, pumps, HVAC and switchgear with root cause and corrective '
         'action.'),
        ('Shutdown and stop planning',
         'Planned and executed work in 24/7 operations with a fixed window: preparation, permits, contractors, test '
         'scripts and verification sequenced so the restart is not delayed.'),
        ('Contractors and stakeholders',
         'Coordinated external contractors, suppliers and internal operations across 37 projects and 11 construction '
         'projects; one plan, named owners and a daily coordination point.'),
        ('Improvement with measured effect',
         'PDCA, 5S, standard work, A3 and 5 Whys in daily use. A PDCA programme cut energy cost by 40 %; own '
         'Python/Claude tools have taken over 40 % of the administrative work out of documentation and follow-up.')]:
        m.bullet(label, body, after=25)

    m.models_table('TOOLS AND METHODS', ('Task', 'Tool and documented use'), [
        ('Validation and change control',
         'URS, risk assessment, IQ/OQ/PQ, traceability matrix and deviation handling; change control before anything '
         'is altered, and acceptance documented at FAT/SAT.'),
        ('Automation and alarms',
         'SCADA and PLC-based systems, sensor and control loops, alarm limits and escalation. Alarm list reviewed as '
         'a quality document, not as a notification feed.'),
        ('Project management in production',
         'Stage plans, shutdown schedules, test scripts and readiness checks; daily coordination with operations '
         'and contractors.'),
        ('Technical documentation',
         'P&ID and electrical drawings, functional descriptions, as-built documentation and handover packages; '
         'decisions written with owner and deadline.'),
        ('Safety',
         'LOTO, APV/workplace assessment, risk assessment, permits and near-miss reporting; contractor safety '
         'briefings before work starts in a production area.'),
        ('Improvement and data',
         'PDCA, 5S, standard work, VSM, A3 and 5 Whys with verified countermeasures; KPI follow-up and investment '
         'cases with NPV, IRR, sensitivity and scenarios.')])

    m.section('EXPERIENCE')
    jobs = [
        ('Senior Commissioning Engineer / Project Manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd, Denmark · Nov 2022–Jul 2024',
         '37 capital projects · 25 specialists · DKK 2–10m each · GMP/FDA/EMA',
         [('Qualification and documentation', 'Acceptance criteria, FAT/SAT and IQ/OQ/PQ with traceable documentation '
                                             'and deviation handling; zero critical findings at handover.'),
          ('Coordination and reporting', 'Progress, cost, risk and resources across engineering, procurement and '
                                         'operations; monthly reporting to management.')]),
        ('Owner / Technical Director',
         'ELOHVAC ApS · Copenhagen, Denmark · May 2023–present',
         '5 electricians and 3 apprentices · full P&L · commercial and industrial customers',
         [('Commercial and operational ownership', 'Quoting, pricing, margin follow-up and service agreements with '
                                                  'response time, quality and delivery as KPIs.'),
          ('People and safety', 'Daily planning, 1:1s, reviews, competence matrix and apprentice training; LOTO, '
                                'risk assessment and APV at every site start.'),
          ('Digital tools', 'Python and Claude API for quotations, schedules, checklists and KPI dashboards; 40 % '
                            'productivity gain.')]),
        ('Project and Workshop Manager',
         'Ventek-Air · Copenhagen, Denmark · Jan 2022–Nov 2022',
         '14 employees · 11 parallel construction projects · DKK 2–10m each',
         [('Throughput and flow', 'Tenders, quotations, subcontractors and handover packages; daily board meetings '
                                  'and bottleneck analysis lifted delivery performance.')]),
        ('Maintenance and Operations Manager / Workshop Technician',
         'Biofos, Lynetten · Copenhagen, Denmark · Aug 2017–Jan 2022',
         '24/7 plant · pumps, HVAC, switchgear, SCADA · shifts including nights and weekends',
         [('Operation and maintenance', 'Preventive maintenance planned from SCADA condition data; alarm handling, '
                                       'fault diagnosis and corrective work prioritised by consequence.'),
          ('Safety and standards', 'LOTO, risk assessment, APV and near-miss reporting in shift operations; standard '
                                   'work, 5S and PDCA on the workshop and stores.')]),
        ('Electromechanical Technician / Production Team Leader',
         'ARJ Engineering · Tehran, Iran · Dec 2003–Mar 2010',
         '12 mechanics and technicians · machine workshop · industrial equipment',
         [('Equipment and targets', 'Shift planning, material control and target follow-up; fault diagnosis, '
                                    'root-cause analysis and corrective actions on industrial machinery.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('EDUCATION AND CERTIFICATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering',
          'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · EQF 6 · GPA 7.6/12')
    m.edu('Authorised marine and electrical engineer (LV/MV/HV)',
          'Danish Safety Technology Authority · May 2023')
    m.edu('Electrical and mechanical design, electrical engineering',
          'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Refrigeration and air conditioning · STCW safety and engine-room watch',
          'Mercantec 2021 · Danish Maritime Authority 2021–2023')

    m.section('LANGUAGES, PRACTICAL AND REFERENCES')
    m.para('Danish: native · English: professional, written and spoken · Persian: native · Driving licence B · SAP and Excel in daily use · Lives '
           'in Måløv, about ten minutes from Site Bagsværd · Available for both annual production stops, including '
           'July/August and December/January · References from Novo Nordisk and Biofos on request.', after=70)

    m.models_table('WHAT THE ROLE ASKS FOR — MY EVIDENCE', ('Requirement', 'Evidence'), [
        ('Relevant technical background, e.g. mechanical engineering',
         'Authorised marine engineer (maskinmester) with electrical authorisation LV/MV/HV and B.Tech in Technology '
         'Management and Mechanical Engineering (EQF 6).'),
        ('Strong Danish and English, international environment',
         'Danish native, English professional written and spoken, Persian native; two years in an international '
         'project organisation with English as the working language.'),
        ('Communication and collaboration at all levels of the organisation',
         'Coordinated 25 specialists, operations, procurement, contractors and management across 37 projects; '
         'written decisions with owner and deadline.'),
        ('Proactive and ambitious, flexible during the two production stops',
         'Five years of 24/7 operations and shutdown work; planned and executed work in fixed windows where the '
         'restart could not slip. Available for July/August and December/January.'),
        ('Validation of systems (useful)',
         'FAT/SAT and IQ/OQ/PQ across 37 projects with acceptance criteria, risk assessment and FMEA, deviation '
         'handling and audited handover; zero critical findings.'),
        ('BMS/FMS experience (useful)',
         'Not in a pharmaceutical plant before. SCADA-based monitoring, sensor loops, alarm handling and '
         'requalification from a 24/7 process plant; the system I would learn first, the discipline I know.'),
        ('Pharmaceutical industry experience (useful)',
         'Two years at Novo Nordisk in a GMP/FDA/EMA environment, with documentation, change control, compliance and '
         'audit readiness as daily conditions.'),
        ('Driving changes from specification to implementation',
         'Delivered 37 capital projects and 11 construction projects from requirements through FAT/SAT to handover, '
         'with contractors and operations coordinated to a fixed date.')])
    m.page_break()

    m.models_table('FIRST 90 DAYS — SYSTEM, STOP, DOCUMENTATION', ('Period', 'What happens, and how it is measured'), [
        ('Week 1–2',
         'Walk the utility areas with the engineers and skilled workers: WFI, clean steam, compressed air, HVAC and '
         'the plant rooms. Sit with the BMS in daily operation — alarm list, active alarms, history and the points '
         'that are bypassed. Read the last two stops\' documentation and the open deviations.'),
        ('Day 30',
         'One-page baseline: the twenty most frequent alarms and what they actually mean, open changes in the system, '
         'the age of the documentation, and where the maintenance and requalification plans have drifted. 1:1 with '
         'each colleague I will depend on.'),
        ('Day 60',
         'First alarm review completed with an agreed list of signals to remove, re-limit or re-route. Validation '
         'template and traceability matrix for BMS changes agreed with QA. Contractor plan and readiness checklist '
         'for the next stop drafted with the team.'),
        ('Day 90',
         'Next production stop planned to the hour with test scripts, permits, access and named owners. Two '
         'improvements delivered and documented — one in the system, one in the routine — and a written handover of '
         'the way I work, so it does not depend on me being in the building.')])


    m.section('WHY THE UTILITIES ARE THE PROCESS')
    m.para('A cleanroom is not clean because it was built that way; it is clean because the air handling, the pressure '
           'cascades and the monitoring behind them keep doing what they were qualified to do. The same is true of '
           'WFI and clean steam: the specification lives in a control loop, a sensor and an alarm limit, and when one '
           'drifts, the batch is at risk long before anyone sees a deviation. So I treat the monitoring system as part '
           'of the product, not part of the building.', after=80)

    m.section('PLANNING BACKWARDS FROM THE STOP')
    m.para('A stop is a project with a fixed end date and no possibility of extension, so the plan is built back from '
           'the restart. What is left for the stop itself is execution and verification — installation, loop checks, '
           'functional tests, documentation and release. Everything else belongs before it: design review, FAT, '
           'spare parts on site, contractor induction, permits, area access, and a test script read by someone other '
           'than its author. Twice a year is a rhythm, and a rhythm can be prepared.', after=80)

    m.section('ALARMS, SENSORS AND DATA INTEGRITY')
    m.para('An alarm is a decision someone has to make at three in the morning. If there are four hundred of them, '
           'nobody makes it. So the alarm list is a quality document: what is critical, what is informative, what is '
           'a maintenance message dressed as an alarm, and which signals were muted so long ago that nobody remembers '
           'why. Behind every alarm sits a sensor, and behind every sensor a calibration, a trend and an audit trail.',
           after=80)

    m.section('VALIDATION AND CHANGE CONTROL')
    m.para('The cheapest change is the one documented while it is designed. I write requirements, risk assessment, '
           'test cases and the traceability matrix as the project moves, not at the end, because that is the only way '
           'the documentation survives a change of scope. Change control comes before the work; deviations are raised '
           'when they happen, not when they surface at handover; and acceptance criteria are agreed with the people '
           'who will run the plant afterwards.', after=80)

    m.section('CONTRACTORS ON A LIVE PLANT')
    m.para('External specialists are necessary and expensive, and on a live aseptic plant they are also the biggest '
           'variable. So: one plan for everyone, one coordination meeting a day during execution, one accountable '
           'person per scope, and access, permits, LOTO, cleanroom behaviour and waste handling agreed before the '
           'first toolbox talk. Contractors who know what is expected of them deliver faster than contractors managed '
           'by phone.', after=80)

    m.section('LEADING WITHOUT A TEAM')
    m.para('This role has no direct reports, and that changes what leadership is. It becomes the quality of the '
           'one-page description someone else works from, the speed with which QA and operations hear about a change '
           'before it happens, and the willingness to say that a plan will not hold before the stop rather than after. '
           'I have led 25 specialists and 12 technicians with formal responsibility, and I have run projects where my '
           'only authority was the plan and the credibility behind it.', after=80)

    m.section('DIGITAL WORK AND AI')
    m.para('I am an active Claude coder and build my own tools in Python: traceability matrices that stay in step with '
           'the test list, deviation and punch-list logs filtered by area and owner, alarm statistics pulled into one '
           'page, and investment cases with NPV, IRR, sensitivity and scenarios when equipment is replaced. None of it '
           'replaces the validated systems; it shortens the documentation work.', after=80)

    return m.save(path, title='Application and CV — BMS Supporter, Novo Nordisk Bagsværd',
                  subject='BMS, utilities and validation in aseptic filling',
                  keywords='BMS, FMS, utilities, WFI, clean steam, HVAC, validation, IQ OQ PQ, GMP, project management')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_NovoNordisk_BMSSupporter.docx')))
