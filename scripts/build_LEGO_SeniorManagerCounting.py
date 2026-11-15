# -*- coding: utf-8 -*-
"""LEGO Group — Senior Manager, Next-Gen Pre-Pack Counting Lead (Billund, req. 0000039133).

English deliverable (the posting is English): task-first application page + CV in one document.
Culture and role intel: master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md (LEGO section).
Policy: master/README.md — extreme confidence, no caveats.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Senior Manager · Automation for counting and packing technology · Roadmap, qualification, scale-up'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('5 November 2026')
    m.meta('The LEGO Group · Billund · Senior Manager, Next-Gen Pre-Pack Counting Lead (0000039133)')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Senior Manager — Next-Gen Pre-Pack Counting Lead', bold=True, color='1A1A1A')
    m.para('To R&D Pre-Pack Next Gen', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('Counting sounds like the simplest thing in a factory. It is not. Counting is a measurement, and a '
           'measurement is a machine, a specification and a test: what is counted, in which shapes and tolerances, '
           'at what rate, with what accuracy, and what happens to the one element the system cannot see. Get the '
           'specification right and the technology follows; get it wrong, and every prototype runs beautifully on '
           'the sample tray and fails on the real portfolio at three in the morning. Defining that specification — '
           'and proving it with data before it becomes a machine — is the work I want to do in the Next Generation '
           'Packing Equipment programme.', after=80)

    m.para('**I would lead the technical area on four fixed things.** First, **the requirement before the '
           'technology**: a matrix of the element portfolio against the properties that actually decide whether an '
           'element can be counted — shape, colour, transparency, surface, size tolerance, bulk behaviour — so the '
           'roadmap covers the portfolio rather than the handful of elements that happen to be on the table. '
           'Second, **test data decides**: every concept is taken through a designed test — repeatability, false '
           'accepts and false rejects, throughput at the real mix, drift over a shift — and the go/no-go is written '
           'as a number against the requirement rather than as an opinion in a review. Third, **the architecture '
           'and its interfaces**: subsystem boundaries, specifications and performance requirements written down '
           'once, with an interface risk list reviewed like a schedule — most of the cost in a counting line hides '
           'between two subsystems that each met their own specification. Fourth, '
           '**manufacturing readiness**: operating concept, installation plan, maintainability, safety, environmental '
           'compliance and supplier qualification — technology that cannot be maintained at scale is a prototype '
           'with a production budget.', after=80)

    m.para('My background is the one you ask for. I am a **chartered marine engineer** (maskinmester) with a B.Tech '
           'in Technology Management & Mechanical Engineering and Danish electrical authorisation at LV, MV and HV '
           '— mechanical, marine and automation in one degree. I have spent twenty years on the rest of your list '
           'in practice: at **Novo Nordisk** I delivered 37 '
           'parallel capital projects worth DKK 2–10m each, qualifying equipment for production under GMP, FDA and '
           'EMA with acceptance criteria, FAT/SAT, IQ/OQ/PQ, deviation handling and **zero critical findings** at '
           'audited handover; at **ARJ Engineering** I led twelve technicians in a machine workshop, doing fault '
           'diagnosis, root-cause analysis and corrective action on production equipment; at **Biofos** I ran '
           'operations and maintenance on a 24/7 process plant, where the numbers that mattered came from '
           'instrumentation and SCADA and where an unplanned stop was measured in money per hour.', after=80)

    m.para('On **data**, I work the way the role needs. At Biofos I built the picture from meters and SCADA rather '
           'than from impressions — normalised, compared across systems, turned into a priority order — and the '
           'result was **over 40 % lower energy consumption**, documented and held. I use Python daily for exactly '
           'this: pulling test and production data, comparing runs, showing repeatability and drift on one page.',
           after=80)

    m.para('On **operational excellence**, my version is practical: standardised work a new operator can be taught '
           'in a day, bottlenecks found by walking the line rather than waiting for the report, waste removed where '
           'it is cheap to remove, and improvements written down so the next shift inherits them. Running ELOHVAC '
           'with five electricians and three apprentices and full P&L since 2023 taught me to measure improvement '
           'in hours and kroner: the tools I built there removed **over 40 % of the administrative work** from '
           'quoting and follow-up — and it stayed after the project ended.', after=80)

    m.para('On **suppliers, R&D and production sites**, I have done that collaboration from both sides of the '
           'table: specified, bought, tested and qualified supplier equipment, held vendors to a scope at FAT, and '
           'taken new technology from drawing to running line with the people who had to operate it. Tenders, bid '
           'evaluation, contracts and the relationship afterwards decide how fast a good idea becomes an installed '
           'machine.', after=80)

    m.para('Two of your own lines describe my instinct better than I could: "explore functional details while '
           'keeping the wider production system in view" is what a counting problem demands, and **up to five times '
           'more output per square metre** is a system problem, not a gadget problem — solved by specifications, '
           'test data and interfaces rather than by one clever machine. That, plus the habit of turning innovation '
           'into something a production site can run, maintain and improve, is what I would bring.', after=80)

    m.para('Practically: I live in Måløv, about two and a half hours from Billund, and I am prepared to structure '
           'the week around the equipment — on site in Billund through the working week and home at weekends, plus '
           'the four to six weeks of travel the role expects. I can start by agreement, and I would welcome a '
           'conversation about which element families today\'s counting technology struggles with, and where the '
           'programme most needs a lead who can write a specification and then prove it with data.',
           after=70)
    m.meta('Kind regards', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('Automation and equipment manager with 20+ years from production equipment, qualification and technical '
           'operations — chartered marine engineer (B.Tech, EQF 6) with Danish electrical authorisation LV/MV/HV. '
           'Qualified and commissioned production equipment under GMP/FDA/EMA across 37 parallel capital projects '
           'with 25 specialists: acceptance criteria, FAT/SAT, IQ/OQ/PQ and zero critical findings at audited '
           'handover. Led a machine workshop with twelve technicians, ran a 24/7 process plant on instrumentation '
           'and SCADA data with over 40 % documented energy reduction, and holds full P&L with five electricians '
           'and three apprentices since 2023. Data-driven by habit: Python, SCADA, SAP.',
           after=80)

    m.section('AUTOMATION, EQUIPMENT AND PRODUCTION READINESS')
    for label, body in [
        ('Equipment specification and architecture',
         'Requirements, acceptance criteria and interface definitions written before the purchase: what the '
         'machine must do, at which rate and accuracy, and where the boundary sits between connected subsystems.'),
        ('Test, qualification and feasibility',
         'Designed tests for repeatability, throughput and drift; FAT/SAT and IQ/OQ/PQ with traceability; go/no-go '
         'decisions taken on data against a written requirement, not on a demonstration.'),
        ('Production and operational excellence',
         'Standardised work, bottleneck analysis and flow improvement on live production; visual management and '
         'follow-up in a fixed rhythm, with improvements documented so the next shift inherits them.'),
        ('Suppliers and partners',
         'Enquiry, bid evaluation, contract and supplier follow-up; new technology taken from concept to installed '
         'equipment with automation partners, R&D and the production site in the same room.'),
        ('Safety, environment and maintainability',
         'Workplace safety, LOTO and permits, sustainability and environmental compliance, energy performance; '
         'maintainability and '
         'spare-part criticality designed in rather than discovered after commissioning.')]:
        m.bullet(label, body, after=25)

    m.models_table('TOOLS AND METHODS', ('Task', 'Tool and documented use'), [
        ('Data and analysis',
         'Python, Excel and SCADA data: test-run comparison, repeatability and drift, throughput and false-reject '
         'rates, dashboards and one-page decision material.'),
        ('Equipment and automation',
         'PLC-based control, sensors, drives, panels and instrumentation; functional testing against a written '
         'specification; electrical authorisation LV/MV/HV.'),
        ('Qualification and compliance',
         'Acceptance criteria, FAT/SAT, IQ/OQ/PQ, traceability matrix, deviation and change control, audit-ready '
         'documentation under GMP/FDA/EMA.'),
        ('Production systems',
         'SAP for planning and follow-up of equipment and materials, plus Excel and Python reporting; standardised '
         'work, bottleneck and flow analysis, visual management.'),
        ('Projects and suppliers',
         'Scope, plan, cost and risk ownership; tender and bid evaluation, contract terms, FAT and delivery '
         'follow-up with automation suppliers and subcontractors.'),
        ('Leadership and development',
         'Functional leadership of specialists, technicians and apprentices; structured 1:1s, competence plans and '
         'on-the-job training with a next step rather than an instruction.')])

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director',
         'ELOHVAC ApS · Copenhagen, Denmark · May 2023–present',
         '5 electricians and 3 apprentices · full P&L · commercial and industrial customers',
         [('Equipment and delivery', 'Panels, motor controls, drives and control systems specified, installed, '
                                     'tested and handed over with documentation; scope, cost and quality owned end '
                                     'to end.'),
          ('Improvement and data', 'Python and Claude API for quotations, schedules, checklists and KPI dashboards; '
                                   'over 40 % of administrative work removed and over 40 % productivity gain.'),
          ('People', 'Recruitment, 1:1s, apprentice training and mentoring alongside budget, quoting and margin.')]),
        ('Senior Commissioning Engineer / Project Manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd, Denmark · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · DKK 2–10m each · GMP/FDA/EMA',
         [('Equipment qualification', 'Acceptance criteria, FAT/SAT, loop checks, IQ/OQ/PQ, deviation and change '
                                      'control; zero critical findings at audited handover.'),
          ('Suppliers and stakeholders', 'Vendors, consultants and production stakeholders aligned through design, '
                                         'installation and handover; cost, risk and resources reported monthly.')]),
        ('Project and Workshop Manager',
         'Ventek-Air · Copenhagen, Denmark · Jan 2022–Nov 2022',
         '14 employees · 11 concurrent construction projects · DKK 2–10m each',
         [('Execution leadership', 'Tenders, calculations, subcontractors and handover packages in ventilation and '
                                   'technical installations; daily board meetings and bottleneck analysis.')]),
        ('Maintenance and Operations Manager / Workshop Technician',
         'Biofos, Lynetten · Copenhagen, Denmark · Aug 2017–Jan 2022',
         '24/7 process plant · instrumentation, pumps, HVAC, high-voltage switchgear, SCADA',
         [('Data-driven operations', 'Meters and SCADA data normalised and compared across systems, priorities set '
                                     'from measured effect: over 40 % lower energy consumption, documented and '
                                     'held.'),
          ('Reliability and compliance', 'Preventive maintenance from condition data, spare-part criticality, '
                                         'calibration and fault finding; LOTO, permits, workplace assessment and '
                                         'environmental documentation.')]),
        ('Electromechanical Technician / Production Team Leader',
         'ARJ Engineering · Tehran, Iran · Dec 2003–Mar 2010',
         '12 mechanics and technicians · machine workshop · industrial production equipment',
         [('Production equipment', 'Fault diagnosis, root-cause analysis and corrective action on production '
                                   'equipment; shift planning, targets and follow-up in a machine workshop.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('EDUCATION AND AUTHORISATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering',
          'Copenhagen School of Marine Engineering · 2017–2022 · GPA 7.6/12')
    m.edu('Authorised marine and electrical engineer (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('Electrical and mechanical design, electrical engineering',
          'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Refrigeration and air conditioning · STCW safety', 'Mercantec 2021 · Danish Maritime Authority 2021')

    m.section('LANGUAGES, PRACTICAL AND REFERENCES')
    m.para('English: professional, written and spoken · Danish: native · Persian: native · Driving licence B · '
           'Lives in Måløv, prepared to be on site in Billund through the working week — hybrid, with home days '
           'when they fit the equipment — and to travel four to six weeks a year · Available by agreement · SAP, '
           'Python and Excel in daily use · References on request.',
           after=70)

    m.models_table('WHAT THE ROLE ASKS FOR — MY EVIDENCE', ('Requirement', 'Evidence'), [
        ('Background in mechanical/marine engineering, automation or equivalent',
         'Chartered marine engineer (maskinmester) with B.Tech in Technology Management & Mechanical Engineering, '
         'electrical authorisation LV/MV/HV, and twenty years of automation and equipment work.'),
        ('Deep automation expertise in high-volume production or mass manufacturing',
         'Qualified and commissioned production equipment across 37 parallel capital projects under GMP/FDA/EMA; '
         'machine workshop with twelve technicians; 24/7 process plant run on instrumentation and SCADA.'),
        ('Analysing equipment test data to confirm feasibility and drive decisions',
         'Test protocols for repeatability, throughput and drift; FAT/SAT and IQ/OQ/PQ evidence; SCADA and Python '
         'analysis behind a documented 40 % energy and productivity gain.'),
        ('Operational excellence and LEAN principles',
         'Standardised work, bottleneck and flow analysis, visual management and a fixed follow-up rhythm; '
         'improvements documented and held after the project, not just achieved once.'),
        ('Functional leadership with R&D, suppliers and production sites',
         'Specification, tender, FAT and qualification of supplier equipment; new technology taken from concept to '
         'installed equipment with vendors, consultants and the people who operate it.'),
        ('Equipment architecture, interfaces and performance requirements',
         'Interface lists, performance requirements and acceptance criteria defined per subsystem; interface risk '
         'held in one register and reviewed like a schedule.'),
        ('Fluent written and verbal English',
         'English professional, used daily in international project organisations, supplier negotiations and '
         'documentation; Danish native.'),
        ('SAP, environmental compliance and mentoring talent',
         'SAP daily for planning and follow-up; environmental documentation and energy performance in a regulated '
         'plant; mentoring of apprentices, technicians and specialists with structured development plans.')])
    m.page_break()

    m.models_table('FIRST 90 DAYS — REQUIREMENTS, TEST DATA AND THE ROADMAP', ('Period', 'What happens, and how it is measured'), [
        ('Week 1–2',
         'Walk the current counting and packing lines at the production site with the people who run them. Read the '
         'element portfolio and the existing specifications, and learn where today\'s technology fails: which '
         'shapes, which colours, which rates.'),
        ('Day 30',
         'One page that the programme can argue about: the element portfolio mapped to the properties that decide '
         'countability, the requirements that follow, and where today\'s technology meets them — and where it '
         'falls short of the LEGO Group\'s standards. Interface and risk list started.'),
        ('Day 60',
         'Test plan agreed for the first concepts and prototypes: what is measured, with what instrument, against '
         'which acceptance criterion, and who signs. Supplier conversations opened with a specification in hand '
         'rather than a wish list.'),
        ('Day 90',
         'First concept tested and reported as data against the requirement — feasible, not feasible, or feasible '
         'with named conditions. The roadmap has dates, owners and dependencies, and the production site has seen '
         'it.')])

    m.section('A COUNT IS A MEASUREMENT')
    m.para('Every counting problem is a measurement problem in disguise. What property of the element does the '
           'sensor actually see — colour, silhouette, transparency, weight, reflectivity — and how does that '
           'property vary across the portfolio and across a production batch? Once that is written down, the '
           'technology choice becomes almost obvious, and the acceptance criteria write themselves. Without it, '
           'every test is anecdotal, and the project moves forward on the confidence of whoever spoke last.',
           after=80)

    m.section('THE SPECIFICATION IS THE PRODUCT')
    m.para('I would rather spend three weeks on a requirement that is right than three months on a prototype that '
           'answers the wrong question. A good specification says what the equipment must achieve — accuracy, rate, '
           'false-reject rate, uptime, changeover time — under which conditions, and how it will be proven; and what '
           'it must not do, which is where most of the cost and maintenance live. It is also the only fair way to '
           'compare three suppliers, and the only way to know, two years later, whether the investment delivered.',
           after=80)

    m.section('TEST DATA, NOT DEMONSTRATIONS')
    m.para('A demonstration shows what a machine can do once, on a good day, with the vendor present. A test shows '
           'what it does over a shift, on the real mix, after the operator has been on a break and the light has '
           'changed. So I design the test before the concept is built: sample size, run length, what counts as a '
           'false accept and a false reject, and the tolerance that makes the concept pass. When the answer comes '
           'back red, that is a good day for the programme — it is far cheaper than finding out on a ramp-up.',
           after=80)

    m.section('INTERFACES ARE WHERE THE COST HIDES')
    m.para('Two subsystems can each meet their own specification and still fail together, because the boundary '
           'between them was never specified by anyone — a handover point, a singulation step, a control signal or '
           'a data format. My habit is to write every interface down: who delivers what, in which format, at which '
           'rate, and what happens when it does not. It is unglamorous, and it is where five-fold output per square '
           'metre is won or lost.', after=80)

    m.section('FROM PROTOTYPE TO A LINE THAT RUNS')
    m.para('A technology becomes real when a production site can install it, train on it, maintain it and improve '
           'it without the R&D team in the room: an operating concept, an installation plan, spare parts with '
           'criticality, a maintenance routine, safety and environmental compliance, and a ramp-up curve someone '
           'has thought about, including the scalability of the concept. I have handed over equipment an operator could '
           'run from the documentation alone — that is the difference between a pilot and a programme.', after=80)

    m.section('SUPPLIERS ARE PART OF THE DESIGN')
    m.para('Counting technology is rarely built alone: it is built with automation partners, platform owners and '
           'specialist teams who have the mechanics, optics or software you do not, and that partnership decides the '
           'speed of the programme. My approach is '
           'to arrive with a specification rather than a wish list, share the acceptance criteria before the first '
           'prototype, test together at their site as well as ours, and keep the commercial terms simple enough '
           'that both sides want the same outcome — I have evaluated bids and negotiated contracts in my own '
           'company, and held vendors to a scope at FAT.', after=80)

    m.section('PEOPLE MAKE THE ROADMAP HOLD')
    m.para('A roadmap with one owner is a wish; a roadmap with specialists who own their part of it is a plan. I '
           'lead by making the requirement shared and the test visible, so a specialist can disagree with data '
           'instead of opinion. I own my workstream\'s scope, quality, timing and cost, and I mentor deliberately with '
           'continuous learning built into the work: a competence plan per person, real responsibility early, '
           'credit given in public.', after=80)

    return m.save(path, title='Application and CV — Senior Manager, Next-Gen Pre-Pack Counting Lead, LEGO Group',
                  subject='Automation for counting and packing technology: roadmap, qualification and scale-up',
                  keywords='automation, counting technology, equipment architecture, test data, qualification, '
                           'LEAN, suppliers, production readiness')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_LEGO_SeniorManagerCounting.docx')))
