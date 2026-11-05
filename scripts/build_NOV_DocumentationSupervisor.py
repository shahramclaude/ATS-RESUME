# -*- coding: utf-8 -*-
"""NOV (National Oilwell Varco) — Documentation Supervisor, Kalundborg.

English deliverable (the posting is English): application page + CV in one document.
Policy: master/README.md — extreme confidence, no caveats.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Documentation Supervisor · Document control, digitalisation and a team that delivers'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('5 November 2026')
    m.meta('NOV · Kalundborg · Documentation Supervisor')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Documentation Supervisor, NOV Kalundborg', bold=True, color='1A1A1A')
    m.para('To the Head of Document Control, NOV Kalundborg', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('A manufacturing data book outlives everyone who made it. The pipe leaves Kalundborg and goes to a field '
           'somewhere; ten or twenty years later an operator, a surveyor or an auditor asks which material went into '
           'it, which test it passed and who signed for it. The only thing that still answers is the book. That is why '
           'documentation is not the last step of production — it is a production discipline of its own, and it needs '
           'a supervisor who has had their name on documents that had to be right the first time, and who has been '
           'the one standing between a team and a deadline.', after=80)

    m.para('**I would run the team on four fixed things.** First, **one definition of complete**: a document set per '
           'order that can be checked at the door — which documents, in which order, at which revision, signed by '
           'whom, filed where — so completeness is a checklist and not an opinion, and deadline management is a plan '
           'rather than a negotiation. Second, **the week is planned, '
           'not discovered**: the production plan translated into documentation demand, the documentation workflows '
           'measured end to end, capacity known per assistant, and the bottleneck visible on Tuesday instead of at '
           'three o\'clock on Friday. Third, '
           '**digitalise where the rework is**: find the repeated manual step — collation, compiling, naming, '
           'printing, scanning, indexing, retrieval — simplify it, then automate it, and only then talk about systems. '
           'Fourth, '
           '**change is made with the team**: six experienced documentation assistants know exactly where the flow '
           'breaks, and a change they helped design survives the quarter.', after=80)

    m.para('Production documentation is what I have delivered for twenty years, and in an audited form. At **Novo '
           'Nordisk** in Kalundborg and Bagsværd I ran **37 parallel capital projects** as commissioning engineer and '
           'project manager with 25 specialists: **FAT/SAT, IQ/OQ/PQ, as-built drawings, material and calibration '
           'certificates**, assembled into handover packages that had to be complete because auditors read them — '
           'handed over with **zero critical findings**. That is the standard a data book lives under: every page '
           'traceable, every revision controlled, every certificate retrievable years later in minutes.', after=80)

    m.para('I have led the people who produce that paperwork. As **owner of ELOHVAC** since 2023 I run **five '
           'electricians and three apprentices** with full P&L, and quality assurance and handover documentation are '
           'what the customer pays for; a missing document is an unpaid invoice. In **Ventek-Air** I led **14 '
           'employees and 11 concurrent projects** with daily boards, safety documentation and handover packages, and '
           'in **ARJ Engineering** **12 technicians** in a machine workshop where the job record was the only proof '
           'the work met specification. Skilled-trade teams have their own voice and their own professional pride; '
           'leading them means being present, keeping engagement through transitions, and being clear about what good '
           'looks like.', after=80)

    m.para('Digitalisation is where I stopped waiting for permission. I build my own tools in **Python and Claude** — '
           'quotation calculation, time plans, quality checklists, KPI dashboards and automated reporting — with a '
           'documented productivity gain of **over 40 %**, and I ran energy management on metering and SCADA data to '
           '**more than 40 % lower consumption**. Applied to documentation it is the same work: simplification before '
           'systems, one template, one '
           'naming standard, an index that generates itself, scanning that files where it belongs, and retrieval '
           'that finds a certificate in under a minute. Automation is not a project you buy; it is the repetitive '
           'hour you take out of the week.', after=80)

    m.para('NOV Flexibles is one of three manufacturers of flexible pipe systems in the world, made to order, with a '
           'shopfloor that runs from smiths to engineers and PhDs to unskilled workers. That mix only works when the '
           'documentation is unambiguous, and it is exactly where a documentation team needs a leader who understands '
           'the product, the process and the people. Your culture of not being content with the status quo, of '
           'continuous improvement, collaboration and accountability, and of freedom with responsibility is the '
           'mandate this role is built on — and because the position is new, the standard for the team is something I '
           'get to help set rather than inherit.', after=80)

    m.para('Practically: I live in Måløv, Brøndby is about ten minutes away and Kalundborg around an hour and a '
           'quarter by car — a drive I know well from my Novo Nordisk years at the Kalundborg site. Danish native, '
           'professional **English**, **driver\'s licence (B)**, available by agreement. I would like to hear where '
           'the documentation flow costs the most time today, and which paper step the team would most like to be '
           'rid of first — that is where I would start.', after=70)
    m.meta('Kind regards,', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('Documentation and operations leader with 20+ years in audited manufacturing, capital projects and 24/7 '
           'process plants — authorised machine and electrical installer (LV/MV/HV), B.Tech in Technology Management '
           '& Mechanical Engineering. Delivered 37 capital projects at Novo Nordisk in Kalundborg with FAT/SAT, '
           'IQ/OQ/PQ, as-built and certificate packages and zero critical findings at audit. Led teams of 5 to 14 in '
           'skilled-trade environments with quality, safety and handover documentation as the deliverable. Builds '
           'Python and Claude tools that remove manual steps — over 40 % documented productivity gain.', after=80)

    m.section('DOCUMENTATION, PRODUCTION AND DIGITALISATION')
    for label, body in [
        ('Document control and data books',
         'Document sets assembled per order and per project: drawings, test protocols, material and calibration '
         'certificates, signed records and as-built documentation — revision controlled, indexed and archived so '
         'that any document can be produced on request, years after handover.'),
        ('Deadlines, workload and completeness',
         'Production plans translated into documentation demand; work distributed against known capacity per person; '
         'bottlenecks re-prioritised the same day rather than reported at the end of the week; one checkable '
         'definition of a complete set, with the check placed before dispatch and rework causes counted.'),
        ('Digitalisation and automation',
         'Python and Claude tools for checklists, dashboards, automated reporting and document handling; '
         'paper-based steps mapped, measured and replaced one at a time, with the before-and-after time documented '
         'the way a production improvement is.'),
        ('Team leadership in skilled trades',
         'Five electricians and three apprentices with full P&L; 14 employees and 11 concurrent projects; 12 '
         'technicians in a machine workshop. Daily direction, one-to-one conversations, coaching and clear feedback '
         'through changing priorities.'),
        ('Stakeholders across the factory',
         'Daily working interface with manufacturing, engineering, quality, supply chain and project teams; '
         'requirements agreed in writing, escalation handled early, and the issue resolved with the function that '
         'owns the data rather than passed back and forth.')]:
        m.bullet(label, body, after=25)

    m.models_table('TOOLS AND METHODS', ('Task', 'Tool and documented use'), [
        ('Document control',
         'Document registers, revision control, distribution lists and archive structures; handover packages for 37 '
         'capital projects, retrievable and audit-ready.'),
        ('Workload and flow',
         'Weekly capacity planning against the production plan, visual boards, bottleneck analysis and standard work '
         'for recurring documentation routines.'),
        ('Digitalisation',
         'Python and Claude for templating, automated collation, KPI dashboards, checklists and reporting; digital '
         'checklists replacing paper forms in daily use.'),
        ('Quality and audit',
         'Acceptance criteria, FAT/SAT, IQ/OQ/PQ, as-built and certificate verification; deviations to root cause '
         'with action closed and verified.'),
        ('Systems',
         'SAP ERP for orders, cost and asset data; Excel/Power Query for reconciliation; CMMS for maintenance records; '
         'scanning and electronic archiving in daily use.'),
        ('Leadership',
         'Daily board meetings, one-to-one and appraisal conversations, coaching of apprentices and new employees, '
         'and task handover so absence never stops the flow.')])

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director',
         'ELOHVAC ApS · Copenhagen · May 2023–present',
         '5 electricians and 3 apprentices · full P&L · electrical installation and service',
         [('Documentation as the deliverable',
           'Quality assurance and handover documentation owned towards customers: checklists, test records and '
           'as-built material delivered with each job, with document handling automated in Python and Claude tools — '
           'over 40 % documented productivity gain.')]),
        ('Senior Commissioning Engineer / Project Manager, Electrical Systems',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · 2–10 million DKK each · GMP/FDA/EMA',
         [('Documentation packages, planning and audit',
           'FAT/SAT, IQ/OQ/PQ, as-built drawings and material and calibration certificates assembled into complete '
           'handover packages, audited with zero critical findings; schedules converted into documentation milestones '
           'with monthly reporting to management and client in SAP and Excel.')]),
        ('Project and Workshop Manager',
         'Ventek-Air · Copenhagen · Jan 2022–Nov 2022',
         '14 employees · 11 concurrent jobs · 2–10 million DKK per job',
         [('Handover packages and daily direction',
           'Safety documentation and handover packages per project; daily board meetings, capacity planning and '
           'bottleneck analysis across eleven concurrent jobs delivered to deadline.')]),
        ('Operations and Maintenance Manager',
         'Lynetten under Biofos · Copenhagen · Aug 2017–Jan 2022',
         'Process plant in 24/7 operation · pumps, blowers, ventilation, transformers, switchgear and SCADA',
         [('Records, authority requirements and data',
           'Plant documentation and authority requirements maintained in 24/7 operation; maintenance records, asset data '
           'and energy reporting from metering and SCADA, with over 40 % lower consumption documented.')]),
        ('Electromechanical Technician / Production Supervisor',
         'ARJ Engineering · Tehran · Dec 2003–Mar 2010',
         '12 mechanics and technicians · machine workshop · industrial equipment',
         [('Job records and root cause',
           'Job records and test documentation per unit as the proof of work to specification; shift planning, '
           'training and corrective actions on production equipment.')]),
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
    m.para('Danish: native · English: professional · Persian: native · Driver\'s licence B and car · Based in Måløv, '
           'Brøndby ten minutes and Kalundborg around an hour and a quarter by car · Available by agreement · SAP, '
           'Excel and Python daily · References on request.', after=70)

    m.models_table('WHAT THE ROLE ASKS FOR — MY EVIDENCE', ('Requirement', 'Evidence'), [
        ('Proven team leadership experience',
         'Five electricians and three apprentices with full P&L since 2023; 14 employees and 11 concurrent jobs at '
         'Ventek-Air; 12 technicians at ARJ; 25 specialists led across 37 capital projects at Novo Nordisk.'),
        ('Factory or manufacturing environment, ideally production or union-represented employees',
         'Twenty years in manufacturing and technical operations: machine workshop, 24/7 process plant and flexible '
         'pipe and pharma production; skilled-trade teams with their own professional standards and shopfloor voice.'),
        ('5+ years of production documentation, workflows, workload coordination and deadlines',
         'Two decades in which documentation was the deliverable: job records and test documentation in the '
         'workshop, plant and authority documentation in 24/7 operation, and FAT/SAT, IQ/OQ/PQ and as-built packages '
         'in capital projects, with capacity planned against the production plan.'),
        ('Manufacturing Data Books, compilation and archiving',
         'Handover packages built from drawings, protocols, material and calibration certificates and signed records — '
         'revision controlled, indexed and archived, retrievable on request; audited with zero critical findings.'),
        ('Monitoring progress, workflow and productivity, addressing bottlenecks',
         'Visual boards and weekly capacity planning; rework and missing-document causes counted and corrected; flow '
         'measured before and after each change so improvement is a number, not an impression.'),
        ('Digitalisation and automation of paper-based workflows',
         'Python and Claude tools replacing manual steps in checklists, reporting and document handling, with over '
         '40 % documented productivity gain; energy management automated on SCADA and metering data.'),
        ('Coaching, feedback and leading change',
         'One-to-one and appraisal conversations, structured onboarding of apprentices and new employees, and change '
         'introduced through the people who have to live with it; cross-functional work in capital projects and in '
         '24/7 operation, with requirements agreed in writing and issues escalated early.'),
        ('Professional Danish and English, digital literacy, quality and safety',
         'Danish native and professional English in written and spoken reporting to management, auditors and clients; '
         'SAP, Excel, Python and archiving systems in daily use; quality and safety standards held in every handover.')])
    m.page_break()

    m.models_table('FIRST 90 DAYS — THE FLOW, THE TEAM AND THE FIRST AUTOMATION', ('Period', 'What happens, and how it is measured'), [
        ('Week 1–2',
         'Shadow each assistant through a complete order cycle and a complete data book: where documents are '
         'created, who signs, where they wait, where they are printed, and where they are archived. Read the last '
         'audit findings, the rework log and the delivery deadlines for the coming quarter.'),
        ('Day 30',
         'A one-page map of the flow as it actually runs: volumes per week, lead time per document type, the three '
         'places where time is lost and the three causes of rework. Capacity per assistant measured, not assumed, '
         'and the weekly board redesigned around the production plan.'),
        ('Day 60',
         'One definition of a complete document set agreed with Quality and Manufacturing, with the completeness '
         'check moved to before dispatch. Workload model in place and the worst bottleneck fixed; naming, '
         'templating and archive structure standardised.'),
        ('Day 90',
         'First automation live and measured — for example automatic collation and indexing, generated covering '
         'lists or scanned filing that lands in the right place. Documentation KPIs on the board: on-time delivery, '
         'rework percentage, right-first-time and retrieval time; and a coaching plan so every assistant knows '
         'which part of the flow they own.')])

    m.section('A DATA BOOK IS THE FACTORY\'S MEMORY')
    m.para('A flexible pipe is made to order and cannot be checked afterwards by looking at it. Everything that '
           'makes it trustworthy — the material batch, the weld, the pressure test, the acceptance signature — '
           'exists only as a record. So the Manufacturing Data Book (MDB) is not an administrative product running '
           'alongside '
           'the factory; it is the part of the product that travels with it, and it is the last thing production '
           'touches before the pipe leaves the site. When it is right, nobody notices. When it '
           'is wrong, the pipe is stuck at a quay, a claim is opened, or an audit finds the gap years later. That '
           'asymmetry is what I plan the team\'s week around.', after=80)

    m.section('A DOCUMENTATION TEAM IS MEASURED AT THE DEADLINE, NOT IN THE MEETING')
    m.para('Everyone can be busy and still deliver nothing on Friday. So the work is planned from the production '
           'plan backwards: which orders will need which documents, when the test results arrive, how many hours of '
           'compilation that is, and who has the capacity. A board that shows the next two weeks per assistant '
           'turns a deadline into a schedule, and it also makes the honest conversation possible early — when a '
           'date has to move, it moves on Tuesday with a reason, not on Friday with an apology. That is what '
           'protects a team of six from the two things that wear documentation departments down: invisible '
           'overload and constant firefighting.', after=80)

    m.section('AUTOMATION STARTS WHERE THE REWORK IS')
    m.para('Automation projects fail when they start with the software and end with a process nobody uses. I start '
           'at the other end: sit with the person doing the task, count how many times a week it is repeated, how '
           'long it takes and how often it is done twice. Then the fix is usually small — a template that fills '
           'itself, a naming rule that sorts correctly, a scan that files where it belongs, an index generated '
           'from the folder instead of typed. I build those tools myself in Python and Claude, which is why this '
           'is not a wish list: I have taken manual hours out of quoting, time planning, checklists and reporting, '
           'and measured the gain at over 40 %.', after=80)

    m.section('CHANGE WITHOUT THE TEAM IS JUST A NEW PROCEDURE')
    m.para('Six assistants who have done this work for years know more about the flow than any process map, and '
           'they will tell you where it breaks if they believe it changes something. A supervisor needs a technical '
           'understanding and a process understanding strong enough to review their work, answer the awkward question '
           'and troubleshoot where it happens, instead of routing it back as a query. So the sequence is: ask, '
           'listen, take the three worst irritations first, fix them visibly, and then write the procedure that '
           'locks the improvement in. Coaching is the same discipline — short conversations, specific feedback, a '
           'clear expectation of what good looks like, and credit given where the work was actually done. In a '
           'newly created position this matters double: the team is not only learning a new leader, it is learning '
           'a new organisation around itself, and that has to be handled with clarity rather than tempo.', after=80)

    m.section('THE LAST PAGE IS THE ONE THAT FAILS')
    m.para('Documentation sets almost never fail in the middle. They fail at the end — a certificate that was '
           'never signed, production records printed from an old folder, a page missing from the index, a test '
           'report that stayed with the supplier. Quality standards and compliance are not demonstrated by a binder on '
           'a shelf; they are demonstrated by a set that is complete, signed and found in the archive in the minute it '
           'is asked for. So the completeness check belongs at the last page and before '
           'dispatch, done by someone who did not compile the set, against a list that is short enough to be used. '
           'That single discipline — a second pair of eyes against a fixed list, at the door — is what turned 37 '
           'capital projects at Novo Nordisk into handovers with zero critical findings, and it is the cheapest '
           'quality system a documentation department will ever install.', after=80)

    return m.save(path, title='Documentation Supervisor — NOV, Kalundborg',
                  subject='Production documentation, document control, digitalisation and team leadership',
                  keywords='documentation supervisor, document control, manufacturing data book, MDB, production '
                           'documentation, archiving, digitalisation, automation, team leadership, Kalundborg')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_NOV_DocumentationSupervisor.docx')))
