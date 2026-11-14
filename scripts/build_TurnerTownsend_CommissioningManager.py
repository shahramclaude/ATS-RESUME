# -*- coding: utf-8 -*-
"""Turner & Townsend — Commissioning (Cx) Manager, Data Center Projects, Fredericia. English posting ->
English document.

Form (master/FORMKATALOG.md): opening **AC** (the last signature on a data center is not the contractor's but
the one that says the systems did what the design promised — under the conditions that will actually occur),
structure **From dead to live** (the paper · the dead check · the first energisation · the sequence · the
failure you cause on purpose · the sign-off), register **The Witness Point** (witness point, hold point, step,
sequence, failover, load bank, retest, deviation, punch list, sign-off).
Culture file: jd/TurnerTownsend_CommissioningManager_kultur.txt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Commissioning Manager · testing, verification and sign-off of critical systems'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('4 November 2026')
    m.meta('Turner & Townsend · Commissioning (Cx) Manager, Data Center Projects · Fredericia, Denmark')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Commissioning Manager', bold=True, color='1A1A1A')

    def lp(text, after=34):
        return m.para(text, after=after, line=232)

    # ---------------------------------------------------------------- page 1
    lp('**The last signature on a data center is not the contractor\'s. It is the one that says the systems did '
       'what the design promised — under the conditions that will actually occur, including the ones nobody is '
       'keen to test.** That signature matters in plants where '
       'nothing was accepted because someone said it worked.', after=30)

    lp('You are looking for a Commissioning Manager to run the Cx process **"on behalf of the Turner & Townsend '
       'Project management & Consultancy team"** on **"a large, complex, Data Center project in Denmark"**, with '
       '**"a daily, on-site presence"** and **"travel within the EU for off site factory testing & witnessing"**. '
       'I have not commissioned a data center; I have commissioned, verified and handed over critical technical '
       'systems — **37 capital projects**, FAT/SAT, IQ/OQ/PQ and change control, with **zero critical deviations** '
       'at handover. The difference is stated plainly below rather than discovered in an interview.', after=26)

    lp('**From dead to live. Six rungs — and the fifth is the one that tells you whether the building is really '
       'redundant.**', after=20)

    lp('**The paper.** **Manage, deliver and obtain approval on relevant project commissioning documents** — '
       '**test scripts** and **compliance statements** written before anything is energised, with acceptance '
       'criteria a third party could read, and a list of who witnesses what. My experience includes acceptance and '
       'validation documentation under GMP/FDA requirements; the discipline is the same whether the plant '
       'makes medicine or megawatts.', after=18)

    lp('**The dead check.** **Equipment installation oversight** before the first cable is live: what is '
       'installed against what was designed, labelled as the schedule says, and segregated the way the drawing '
       'requires. Most of what fails later was visible then, quietly, in a photograph nobody took.', after=18)

    lp('**The first energisation.** Controlled, planned, with one named person owning the switch and a written '
       'sequence. Nobody energises "to see if it works" — that is how a commissioning programme loses a week and '
       'an argument with the insurer.', after=18)

    lp('**The sequence.** Functional testing against the **sequence of operations**, step by step, with a '
       '**witness point** signed where it says signed and a deviation raised where it does not. Everything I '
       'commissioned was tested against a written sequence, and the **issues log** decided the schedule, not the '
       'meetings.', after=18)

    lp('**The failure you cause on purpose.** **Failover**, **redundancy** and the black-building test: the only '
       'evidence that the design is redundant, and the test everyone would rather schedule next month. I would '
       'rather find it with the load bank on a Tuesday than have the client find it on a Sunday.', after=18)

    lp('**The sign-off.** **Verify the integrity and performance of critical systems**, close the **punch list**, '
       'hand over documentation the operator can actually run from, and then approve the finalisation of the '
       'project on evidence rather than on schedule pressure.', after=24)

    lp('**Where my record is thinner, stated plainly.** I have not commissioned a data center, and ten years as '
       'a commissioning engineer by job title would not be true: that title is November 2022 to July 2024. What I '
       'have is twenty years of installing, testing and handing over technical systems — machine shop from 2003, '
       'operations and re-commissioning at Lynetten 2017–2022, eleven sites at once in 2022, my own company since '
       '2023. My control systems are SCADA and PLC in 24/7 operation and in GMP/FDA plants, not BMS on a '
       'hyperscale campus, and I have not used commercial Cx software; my documentation lives in versioned '
       'files with named sign-offs. **Google Drive**, shared folders and email are everyday tools — the '
       'documentation control behind them is the part that matters.', after=24)

    lp('**On the role and the culture.** T&T describes itself as a **"global professional services company"** '
       'delivering **"net zero and digital solutions"** alongside programme and cost management — and this role '
       'sits on the client side with **"an ability to manage expectations, influence change, and report/update '
       'accurately on progress"** as the core skill. That is the part I recognise: **"influencing skills"** and '
       '**"strong communication"** with contractors who are late, vendors who are optimistic and clients who are '
       'rightly nervous. I bring a **"team attitude"**, I am **"self-motivated"**, and I am used to '
       '**"independent work with challenging tasks"** in an **"international environment"** where the reporting '
       'line is not always in the same building.', after=24)

    lp('**Practical.** Danish first language, professional English, category B licence and own car. I live in '
       'Måløv, and for a role with **"daily, on-site presence in Denmark"** I am open to relocating — Fredericia '
       'is a place to live in, not a commute to survive. The role also requires travel for **"factory testing & witnessing"** within '
       'the EU; I would discuss the frequency and practical arrangements at interview.', after=12)

    m.meta('Kind regards', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('**Commissioning and handover of critical technical systems, and '
           'experience in installation and operations dating back to 2003** — 37 capital projects, 25 specialists, FAT/SAT, IQ/OQ/PQ and '
           'change control, **zero critical deviations** at handover. Authorised maskinmester (LV/MV/HV), B.Tech '
           'in Technology Management, PRINCE2 certified, **Lean and Six Sigma** as methods in practice. Twenty '
           'years of documentation that had to survive somebody else reading it.', after=52)

    m.section('THE WITNESS POINT — WHAT I SIGN FOR')
    for label, body in [
        ('Hold before witness',
         'A **hold point** is a promise that the next step waits until someone has seen the step before it. If '
         'the programme quietly skips one, the paper still looks complete — and the defect arrives six months '
         'later with a warranty argument attached.'),
        ('Step, not system',
         'Every system I have accepted was signed off in steps: isolated, powered, exercised, loaded, failed over. '
         'A single "commissioned" tick at the end of a package is a signature without evidence.'),
        ('Deviation, retest, close',
         'A **deviation** with a number, an owner and a date; a **retest** with the same witness present; a '
         'closure in writing. That loop is why 37 handovers passed audit with no critical findings.'),
        ('Redundancy is a test',
         'A redundant design that has never been failed on purpose is a design with an intention. The **failover** '
         'test is uncomfortable, takes planning and load, and is the only thing a client can actually trust.'),
        ('Handover to the operator',
         'Documentation written for the person who runs the building at 03:00, not for the auditor at 10:00 — '
         'and a walk-through with them before I leave, because the last **sign-off** is theirs to live with.'),
    ]:
        m.bullet(label, body, after=16)

    m.section('EXPERIENCE')
    jobs = [
        ('Senior Commissioning Engineer / Project Manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · GMP/FDA/EMA',
         [('Commissioning and handover as a discipline',
           '**FAT/SAT**, **IQ/OQ/PQ** and **change control** across 37 projects, with acceptance criteria, '
           'witnessed tests and deviation closure; **zero critical deviations** at handover in a regulated environment where '
           'documentation must stand up to review.'),
          ('Contractors and vendors',
           'Suppliers and contractors coordinated across projects: technical clarification, factory '
           'acceptance, site tests and documentation in the package before payment — and an **issues log** that '
           'drove the weekly meeting rather than followed it.')]),
        ('Owner / Technical Director', 'ELOHVAC ApS · Copenhagen · May 2023–present',
         '8 employees incl. 3 apprentices · full P&L · installation, commissioning and handover',
         [('Installation, testing and the customer\'s signature',
           'Electrical and ventilation installations installed, tested and handed over with my own margin at risk: '
           '**test** at the panel, documentation the customer keeps, and a callback if it is wrong.'),
          ('Method and measurement',
           'Workflow and documentation rebuilt around digital tools with **over 40 % productivity gain** measured '
           'after the change; every job ends with a signed handover, not a phone call.')]),
        ('Co-owner and CTO / Technical Lead, AI department',
         'Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 (alongside ELOHVAC)',
         '4–10 people · customer solutions from requirement to go-live',
         [('Systems integration and go-live',
           'Requirements, integration and go-live of customer systems, with acceptance criteria agreed before '
           'build and documentation the customer could run; AI-assisted analysis and reporting in delivery.'),
          ('Two organisations, one plan',
           'Matrix leadership across two companies with written priority agreements; the company has ceased '
           'trading and the department was closed in order.')]),
        ('Project and Workshop Manager', 'Ventek-Air · Copenhagen · Jan 2022–Nov 2022',
         '14 employees · 11 simultaneous site projects',
         [('Eleven sites, one schedule',
           'Daily plan for 11 sites and 14 fitters against delivery dates, materials and subcontractors; '
           'commissioning and handover squeezed into the same calendar as installation.')]),
        ('Operations and Maintenance Manager', 'Biofos (Lynetten) · Copenhagen · Aug 2017–Jan 2022',
         'Wastewater plant in 24/7 operation · SCADA, PLCs, HV switchgear · pumps and cooling systems',
         [('Control systems in critical operation',
           'SCADA and PLC-controlled process in 24/7 duty under regulatory supervision; **verification** of '
           'performance through measurement, re-commissioning and documented corrective action.'),
          ('Improvement with a number',
           '**Over 40 % lower energy consumption** through measurement, re-tuning and follow-up — proved after '
           'the change, not promised before it.')]),
        ('Electromechanical Technician / Production Team Lead', 'ARJ Engineering · Tehran · Dec 2003–Mar 2010',
         '12 technicians · machine shop · machinery and equipment',
         [('Machines, calibration and acceptance',
           'Installation, fault finding, calibration and acceptance of machinery and equipment; corrective '
           'actions documented, and 12 technicians trained to the same routine.')]),
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
    m.para('**Professional English** (working language in documentation, vendors and international colleagues) · '
           'Danish (first language) · Persian (mother tongue) · **IT**: **Google Drive** and shared documentation, '
           '**Excel** for schedules, **issues log** and reporting, **ERP** and CMMS, **Python** for own analysis · '
           'Måløv today, open to relocating for daily presence in **Fredericia** · category B licence and own car · '
           'available after agreement.', after=32)

    m.models_table('THE ROLE AS ADVERTISED — WHAT I BRING', ('Requirement', 'Evidence'), [
        ('10 years\' experience of industrial equipment and systems commissioning and management',
         'Twenty years in installation, operations and handover; commissioning by job title since November 2022. '
         '**Management** of the package, the vendors and the schedule is the part I have done longest.'),
        ('Proficiency in mechanical and electrical equipment and systems',
         'Authorised maskinmester (LV/MV/HV) with mechanical engineering behind it: switchgear, motors, pumps, '
         'HVAC, refrigeration and the control layer that ties them together.'),
        ('Familiarity with control systems for critical infrastructures',
         'SCADA and PLC in 24/7 operation and in GMP/FDA production, with alarm handling, interlocks and '
         'documented setpoints. BMS on a data center campus I have not worked with.'),
        ('Experienced in Quality Control and verification',
         '**Quality control** and **verification** as a written loop: criteria before the test, witnesses during '
         'it, deviation and retest after it, closure on paper. 37 handovers, zero critical deviations.'),
        ('Familiarity with Google Drive, email and similar tools',
         '**Google Drive** and shared folders for documentation, version controlled with named owners; email and '
         'calendar as the coordination layer. The discipline behind the folder is what I bring.'),
        ('A team attitude, self-motivated, willing to support other groups and projects',
         'A **"team attitude"** in a small company means answering the phone for someone else\'s project; I have '
         'done that for eight years with my own name on the invoice.'),
        ('Influencing skills and strong communication with clients, contractors, management and colleagues',
         'Twenty years of explaining the same problem to a fitter, a contractor, a quality department and a '
         'client — in writing, in a meeting, and in a plant at night when the wording matters.'),
        ('Ability to manage expectations, influence change and report accurately on progress',
         'Progress reported as it is: percent complete that can be defended, slippage named in the week it '
         'happens, and bad news delivered by me before it is discovered by someone else.'),
        ('Strong planning and organisation skills',
         'Eleven simultaneous sites and 37 projects in one calendar, sequenced against materials, people and '
         'access — the same skill set a **commissioning schedule** needs, at a different scale.'),
        ('Lead daily and weekly commissioning meetings internally, with vendors and with the client',
         'Weekly technical and progress meetings run for 37 projects with contractors and suppliers: agenda, '
         'decisions written down, actions with an owner and a date.'),
        ('Manage, deliver and obtain approval on commissioning documents such as test scripts and compliance '
         'statements',
         '**Test scripts**, acceptance criteria and validation documents authored and approved: FAT/SAT, IQ/OQ/PQ, '
         'change control — documents that had to satisfy a regulator as well as a client.'),
        ('Manage the receipt, review and compliance of commissioning documentation to achieve the necessary '
         'sign-off',
         'Documentation received, reviewed and refused when it was wrong; **sign-off** granted on evidence, and '
         'the gap written into the **issues log** with a date instead of a promise.'),
        ('Manage the commissioning schedule',
         'Schedules built and defended: test sequence, witness availability, vendor mobilisation and the '
         'dependencies that decide whether the last test happens this month or next quarter.'),
        ('Manage a team of commissioning engineers and vendors',
         '25 specialists coordinated across 37 projects, 14 fitters across 11 sites, and suppliers and '
         'contractors steered to the same acceptance criteria.'),
        ('Equipment installation oversight',
         '**Installation oversight** from the drawing to the label: what was specified, what arrived, what was '
         'fitted, and what the photograph shows before the ceiling closes.'),
        ('Supervise the installation of new equipment, systems and facilities',
         'Installations supervised in live plants where a shutdown window is measured in hours, with contractors '
         'working to a permit and a sequence agreed the day before.'),
        ('Inspect and verify the correct functioning of electrical, mechanical and environmental control systems',
         '**Inspection and verification** of electrical and mechanical systems, including control and '
         'environmental functions, by test rather than by certificate: it works when it has been made to work.'),
        ('Conduct tests to ensure operational efficacy',
         'Testing at the panel, at the load and in the failure case; performance verified against the design '
         'intent, with the result written down whether it flattered the installer or not.'),
        ('Prepare and deliver commissioning reports, progress, issues log and risks',
         '**Reports**, progress, **issues log** and **risk** register produced weekly on 37 projects — plus the '
         'monthly version for a steering group that read the first page and asked about the second.'),
        ('Manage the close-out of commissioning risks and issues with contractors and vendors',
         '**Close-out** with contractors and vendors: defect lists agreed item by item, responsibility settled on '
         'evidence, and the last payment tied to the last signature — which is what makes close-out happen.'),
        ('Verify the integrity and performance of critical systems',
         'Integrity verified by test and by documentation: what the system does, what it does when a part of it '
         'fails, and what the operator can prove afterwards.'),
        ('Approve the finalisation of the project based on successful testing',
         'Approval on evidence, not on calendar: 37 handovers signed only when the deviation list was closed and '
         'the documentation was in the folder.'),
        ('Ensure adherence to regulatory compliance and budget requirements',
         '**Regulatory compliance** under GMP/FDA and Danish electrical safety as an authorised person; **budget** '
         'responsibility as an owner with full P&L since 2023 and on capital projects with approved business cases.'),
        ('Travel within the EU for off-site factory testing and witnessing',
         'Factory acceptance testing is where a defect is still cheap: My FAT/SAT experience provides a basis for reviewing '
         'equipment before shipment; EU factory travel is a requirement to discuss.'),
        ('Daily, on-site presence on a large, complex data center project in Fredericia, Denmark',
         'Daily presence is how this work is done — it cannot be run from a spreadsheet. I live in Måløv and am '
         'open to relocating for **Fredericia**; the practical arrangement I would agree with you in a first '
         'conversation.'),
    ], widths=(2500, 7846))

    m.section('FIRST 90 DAYS')
    for b in (
        'Weeks 1–3: read what exists — Cx plan, scripts, schedule, issues log, contract packages — and walk the '
        'site with the contractors. No new template until I know why the current one looks the way it does.',
        'Weeks 4–6: one schedule everyone recognises, with witness points named, hold points agreed and the '
        'client told which tests decide the handover date.',
        'Weeks 7–10: the issues log as the working document of the weekly meeting — every open item with an '
        'owner, a date and a consequence; and the first integrated test run where the client can watch.',
        'Weeks 11–13: a documented readiness view for the next milestone, the risk list cut to the five that '
        'matter, and a first report to Turner & Townsend that says plainly what will slip and why.'):
        m.bullet('', b, after=14)

    m.section('WHAT I WOULD ASK')
    for b in (
        'Which phase is the project in — shell and core, fit-out, or integrated systems testing — and which '
        'packages are mine to commission?',
        'Is the Cx role contracted on the client side of a multi-package delivery, and who signs the acceptance '
        'at the end: the client, the contractor or both?',
        'How much of the load and failure testing is already planned, and is there an agreed window for the '
        'black-building test?'):
        m.bullet('', b, after=14)

    m.para('**A conversation, and a walk on site before we talk about me:** +45 93 99 95 14 · '
           'ajlooshahram@gmail.com.', after=16)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_TurnerTownsend_CommissioningManager.docx')
    build(out)
    print(out)
