# -*- coding: utf-8 -*-
"""Belden Cekan A/S — QEHS Manager (Gjern, Denmark).

English deliverable (the posting is English): application page + CV in one document.
Policy: master/README.md — extreme confidence, no caveats.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'QEHS Manager · Quality, environment and safety in one system'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('5 November 2026')
    m.meta('Belden Cekan A/S · Gjern · QEHS Manager')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: QEHS Manager, Belden Cekan', bold=True, color='1A1A1A')
    m.para('To Factory Manager Kim Fredriksen', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('Quality, safety and environment are not three systems. They are one way of running a factory, seen from '
           'three angles: do we make what we said we would make, do we do it without hurting anybody, and do we do '
           'it without costing more of the world than we have to. A management system that treats them separately '
           'produces three binders and one floor that works differently — which is why the integrated system you '
           'are building at Belden Cekan is exactly the assignment I want: one set of processes, one risk picture, '
           'and certifications that describe what actually happens in Gjern rather than what was written in 2008.', after=80)

    m.para('**I would run QEHS on four fixed things.** First, **one system, not three binders**: a single process '
           'map for quality, environment and safety — risk register, deviation handling, document control, audit '
           'plan and management review — where ISO 9001, ISO 14001 and ISO 45001 are three sets of requirements '
           'pointing at the same practice, so certification becomes a confirmation instead of a project. Second, '
           '**an audit is a conversation with evidence**: internal and supplier audits that find the problem before '
           'a customer, an authority or a recall does, and findings that are closed with an owner, a date and a '
           'check that it stayed closed. Third, **the Quality Room and the calibration programme are where a '
           'system proves itself**: calibrated instruments, traceable specifications, archived records that can be '
           'produced two years later when someone asks a hard question. Fourth, **ESG data comes from the floor**: '
           'energy, waste, incidents and complaints counted once, in the same place, so the number the group '
           'reports is the number the factory recognises.', after=80)

    m.para('The quality side is my daily trade. At **Novo Nordisk** I worked inside an audited GMP system with '
           '**SOPs, change control, deviations, CAPA and root cause analysis**, qualification to IQ/OQ/PQ and '
           'FAT/SAT, and I delivered **37 parallel capital projects** with 25 specialists and **zero critical '
           'findings** at audit. That is the discipline this role needs: a nonconformity is not a form, it is a '
           'process that failed in a way we can name, correct and prove — and the audit is where you find out '
           'whether your own system is honest.', after=80)

    m.para('Environment and safety I have carried with real consequences attached. For five years I was '
           '**operations and maintenance manager at Lynetten under Biofos**, one of Denmark\'s largest wastewater '
           'plants, in 24/7 operation: **environmental documentation and authority requirements**, permits and '
           'work permits, chemicals, confined spaces, lifting and heavy traffic — and an **APV** and safety '
           'organisation where the work was planned before the shift started, not after the incident. I ran '
           '**energy management on metering and SCADA data** with **more than 40 % lower energy consumption** as a '
           'documented result, which is exactly the kind of number an ESG report is made of: measured at the '
           'source, followed up monthly, and defensible when someone asks how it was calculated.', after=80)

    m.para('Audits and corrective actions across functions are familiar ground. I have run supplier and contractor '
           'follow-up from both sides of the table — as customer in 37 capital projects and as **owner of '
           'ELOHVAC** since 2023, where I carry full P&L with five technicians and three apprentices and answer '
           'for quality, safety and documentation to my own customers. In **Ventek-Air** I was project and '
           'workshop manager for **14 employees and 11 concurrent jobs**, and in **ARJ Engineering** I led **12 '
           'technicians** in a machine workshop building and maintaining production equipment — the same mix of '
           'connectors, special machines and small-series production that Belden Cekan runs, which is why the '
           'shopfloor language in this role is not foreign to me.', after=80)

    m.para('I also know what a small factory needs from this role. With around 40 employees, QEHS cannot be a '
           'department that writes procedures and waits to be asked: it has to be the person who walks the line, '
           'asks the second question, and helps production solve the problem rather than filing it. I have led '
           'teams of five to fourteen and reported to management and customers monthly, so I am comfortable '
           'holding a management team seat with **one direct report** while keeping the factory floor as my main '
           'source of information.', after=80)

    m.para('Belden describes a professional but unpretentious environment where initiatives are expected to reach '
           'fruition, and a Great Place to Work certification that is taken seriously. That matches how I work: '
           'structured, analytical and proactive, with the follow-up that turns an initiative into a standard. And '
           '**lean** is part of the same discipline — standard work, bottleneck analysis, daily boards and visual '
           'management, which I have used to keep eleven concurrent jobs and a 24/7 plant moving without losing '
           'quality.', after=80)

    m.para('Practically: I live in Måløv, Gjern is around three hours away by car, and I plan my weeks around being '
           'at the factory and at home at weekends. I work and write **English** professionally, I have a '
           '**driver\'s licence (B)**, and I can start by agreement. I would like to hear where the integrated '
           'system stands today and which certification is the next milestone — that is where I would begin.', after=70)
    m.meta('Kind regards,', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('Quality, environment and safety manager with 20+ years in audited production, technical operations and '
           '24/7 process plants — authorised machine and electrical installer (LV/MV/HV) with a B.Tech in '
           'Technology Management & Mechanical Engineering. Delivered 37 capital projects inside a GMP system '
           'with zero critical findings: SOPs, change control, deviations, CAPA, calibration and qualification. '
           'Five years owning environmental documentation, authority requirements, APV and safety in a plant that '
           'could not stop, with over 40 % lower energy consumption documented. Structured and analytical, with '
           'the follow-up that makes a certificate mean something.', after=80)

    m.section('QUALITY, ENVIRONMENT AND SAFETY')
    for label, body in [
        ('Integrated management systems',
         'Quality, environment and safety run as one set of processes: risk register, document control, deviation '
         'and change handling, audit plan and management review — with ISO 9001, ISO 14001 and ISO 45001 as '
         'requirements on the same practice.'),
        ('Audits and certification',
         'Internal, supplier and contractor audits planned from risk to verify compliance with the standards; '
         'findings written with evidence, closed with owner and date, and verified afterwards. Audited handover of '
         '37 projects with zero critical findings.'),
        ('Complaints and corrective actions',
         'Complaints and deviations taken through structured problem solving to root cause, with corrective and '
         'preventive action agreed with R&D and production rather than issued to them, and closed only when the '
         'effect is visible in the data.'),
        ('Calibration, specifications and records',
         'Calibration programmes planned and executed against critical instruments; specifications and records '
         'archived so they can be retrieved and defended years later; Quality Room layout, equipment and '
         'procedures owned as a working tool.'),
        ('Safety, environment and ESG data',
         'APV, work permits, LOTO, chemicals and confined spaces in 24/7 operation; environmental documentation and '
         'authority requirements met; energy, waste, incidents and complaints measured at source, followed monthly '
         'and reported to management and group — energy management with over 40 % lower consumption.')]:
        m.bullet(label, body, after=25)

    m.models_table('TOOLS AND METHODS', ('Task', 'Tool and documented use'), [
        ('Management system',
         'Process maps, document control, deviation and change control, management review and KPI follow-up; '
         'GMP-validated documentation practice transferred to ISO 9001/14001/45001 structures.'),
        ('Audit',
         'Audit plans, checklists and evidence sampling; supplier and contractor audits; finding registers with '
         'owner, due date and verification of effectiveness.'),
        ('Quality engineering',
         'Root cause analysis (5-why, Ishikawa), CAPA, acceptance criteria, IQ/OQ/PQ, FAT/SAT; calibration '
         'planning and traceability.'),
        ('Safety and environment',
         'APV and risk assessment, work permits and LOTO, chemical handling, waste and environmental reporting; '
         'safety committee work and incident investigation.'),
        ('Lean and improvement',
         'Standard work, daily boards, bottleneck analysis and visual management; continuous improvement projects '
         'followed until they become the new standard.'),
        ('Data and reporting',
         'SCADA and metering data, Excel and Python for analysis; ESG and KPI reporting to management and group '
         'level; SAP in daily use.')])

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director',
         'ELOHVAC ApS · Copenhagen · May 2023–present',
         '5 technicians and 3 apprentices · full P&L · electrical installation and service',
         [('Quality, safety and documentation',
           'Quality and safety requirements owned towards customers and authorities; documentation delivered with '
           'each job, and deviations corrected before they become complaints.')]),
        ('Senior Commissioning Engineer / Project Manager, Electrical Systems',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · 2–10 million DKK each · GMP/FDA/EMA',
         [('Audited quality system',
           'SOPs, change control, deviations, CAPA and root cause analysis in a GMP system; audited handover with '
           'zero critical findings.'),
          ('Qualification and calibration',
           'IQ/OQ/PQ, FAT/SAT and acceptance criteria across 37 projects; instruments and specifications verified '
           'and documented before handover to operations.')]),
        ('Project and Workshop Manager',
         'Ventek-Air · Copenhagen · Jan 2022–Nov 2022',
         '14 employees · 11 concurrent jobs · 2–10 million DKK per job',
         [('Delivery and quality under pressure',
           'Daily board meetings, bottleneck analysis and re-prioritisation; deliveries checked against acceptance '
           'criteria and safety requirements before they left the workshop.')]),
        ('Operations and Maintenance Manager',
         'Lynetten under Biofos · Copenhagen · Aug 2017–Jan 2022',
         'Process plant in 24/7 operation · pumps, blowers, ventilation, transformers, switchgear and SCADA',
         [('Environment, authority, safety and data',
           'Environmental documentation and authority requirements met; APV, work permits, LOTO and chemicals '
           'managed in a plant that could not stop; energy management on metering and SCADA data with over 40 % '
           'lower consumption, reported and sustained.')]),
        ('Electromechanical Technician / Production Supervisor',
         'ARJ Engineering · Tehran · Dec 2003–Mar 2010',
         '12 mechanics and technicians · machine workshop · industrial equipment',
         [('Production equipment and root cause',
           'Fault finding, root cause analysis and corrective actions on production equipment; shift planning, '
           'training and follow-up on quality and output targets.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('EDUCATION AND AUTHORISATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering',
          'Maskinmesterskolen København · 2017–2022 · GPA 7.6/12')
    m.edu('Authorised machine and electrical installer (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('Electrical and mechanical engineering', 'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Refrigeration, ventilation and safety training · STCW', 'Mercantec 2021 · Danish Maritime Authority 2021')

    m.section('LANGUAGES, PRACTICAL AND REFERENCES')
    m.para('Danish: native · English: professional · Persian: native · Driver\'s licence B · Based in Måløv, Gjern '
           'around three hours away, weeks planned around the factory · Available by agreement · SAP and Excel '
           'daily, Python for data work · References on request.', after=70)

    m.models_table('WHAT THE ROLE ASKS FOR — MY EVIDENCE', ('Requirement', 'Evidence'), [
        ('Experience with quality, safety and environmental management, preferably in manufacturing',
         'Twenty years in manufacturing, technical operations and 24/7 process plants; quality system ownership in '
         'a GMP environment, environmental documentation and authority requirements in a production plant, and '
         'APV and safety organisation with real operational consequences.'),
        ('Certified in, or solid knowledge of, ISO standards',
         'ISO 9001, ISO 14001 and ISO 45001 worked as the framework rather than the paperwork: processes, '
         'deviation handling, audits, management review and certification follow-up — practised in an audited GMP '
         'system and in a plant under environmental permits.'),
        ('Developing, implementing and improving an integrated management system',
         'Procedures, document control and deviation processes built and maintained across 37 projects and a 24/7 '
         'operation; integrating quality, environment and safety is that discipline applied to three standards.'),
        ('Internal audits and supplier audits',
         'Audit preparation and follow-up from the audited side in 37 projects with zero critical findings; '
         'supplier and contractor requirements set, checked and closed in both capital projects and own company.'),
        ('Complaints and corrective actions with R&D and production',
         'Complaints and deviations taken to root cause with CAPA, agreed with the functions that have to change '
         'the process; corrective actions closed with owner, date and verification of effect.'),
        ('Quality Room, calibration programmes and archiving',
         'Calibration and instrument verification planned and executed across 37 projects; specifications and records '
         'archived and retrievable; instrument responsibility held in 24/7 operation.'),
        ('Health and safety committee and lean projects',
         'Safety committee and APV work in a plant with chemicals, confined spaces and heavy traffic; standard '
         'work, daily boards, bottleneck analysis and visual management used as the daily improvement method.'),
        ('ESG reporting plus quality and safety reporting to group',
         'Energy, waste and incident data measured at source and reported monthly to management and customers; '
         'energy management with over 40 % lower consumption documented and sustained.'),
        ('Fluent English, structured, analytical and proactive',
         'English professional in international project environments and in written reporting; structure visible in '
         '37 parallel projects and in audit-ready documentation; analysis in Excel and Python on real operating '
         'data, with problems addressed before they become findings.')])
    m.page_break()

    m.models_table('FIRST 90 DAYS — THE SYSTEM, THE AUDITS AND THE FLOOR', ('Period', 'What happens, and how it is measured'), [
        ('Week 1–2',
         'Walk the factory with production, R&D, the safety committee and the other stakeholders: where quality is '
         'checked today, where '
         'records live, which certificates are in force and which are coming. Read the last audit reports, the '
         'complaint history and the calibration list.'),
        ('Day 30',
         'A one-page picture of the system as it actually works: processes that exist, processes that are '
         'described, and the gap between them. Findings from the last audits checked for whether they stayed '
         'closed, and the ISO 45001 path mapped against today\'s practice.'),
        ('Day 60',
         'The integrated process map agreed with management and the EMEA functions; deviation, document control '
         'and audit plan aligned to one structure. Quality Room and calibration programme reviewed with a '
         'prioritised plan and an owner per item.'),
        ('Day 90',
         'The first internal audit round run on the new structure, with findings closed or scheduled; ESG, quality '
         'and safety reporting delivered to group from one data set; and a factory floor that can name the three '
         'things QEHS is fixing this quarter.')])

    m.section('ONE SYSTEM, THREE ANGLES')
    m.para('Most factories have a quality system, an environmental system and a safety system, and they describe '
           'the same work three times with three different words. That is where the paperwork grows and where the '
           'floor stops reading it. An integrated system starts from the process — how a product is received, '
           'produced, checked, packed and shipped — and then asks the three questions on each step: what does '
           'quality require here, what does the environment require, and what does safety require. One answer per '
           'step, one owner, one record.', after=80)

    m.section('THE AUDIT FINDS IT FIRST, OR SOMEBODY ELSE DOES')
    m.para('Every audit finding that a customer or an authority makes was already there, waiting. That is why I '
           'plan audits from risk rather than from a calendar: the new process, the manual step, the instrument '
           'nobody has looked at, the supplier who changed something quietly. And I write findings so they can be '
           'closed — what was found, what it means, who owns it, by when, and how we will know it stayed closed. '
           'An audit report that ends in a drawer is a cost; one that ends in a changed routine is the cheapest '
           'improvement the factory will make this year.', after=80)

    m.section('THE QUALITY ROOM IS A TOOL, NOT A STORAGE ROOM')
    m.para('The Quality Room and the calibration programme are where a management system stops being words. If the '
           'gauge is out of calibration, the measurement is a guess, and the certificate is a claim nobody can '
           'back up. I have worked in an environment where every instrument, every acceptance criterion and every '
           'record had to be traceable years later — and where an auditor could ask for any of them and expect an '
           'answer in minutes. That is the standard I would hold the Quality Room to: layout that makes the right '
           'thing easy, equipment that is calibrated, and procedures that a new employee can follow.', after=80)

    m.section('SAFETY IS A NUMBER OF SMALL DECISIONS')
    m.para('Nobody is against safety. Accidents happen in the gap between what the procedure says and what is '
           'practical at four o\'clock on a Friday. So the work is to close those gaps: make the safe way the easy '
           'way, ask why somebody stepped around a rule instead of writing them up for it, and report near-misses '
           'because they are free lessons. In a factory of forty people, everyone knows everyone — which makes '
           'safety personal in the best sense, and makes the safety committee the place where the real issues get '
           'solved.', after=80)

    m.section('ESG IS PRODUCTION DATA, NOT A SEPARATE EXERCISE')
    m.para('Environmental, social and governance reporting has a bad reputation because it is often assembled once '
           'a year, in collaboration with finance, from estimates. In a factory, the numbers already exist: kilowatt hours, waste fractions, '
           'chemicals, water, incidents, complaints, training hours. The job is to define them once, measure them '
           'where they arise, and follow them monthly so the annual report is a summary rather than an '
           'investigation. That is exactly how the 40 % energy reduction at Lynetten was achieved and kept: '
           'measured monthly, discussed monthly, improved continuously.', after=80)

    m.section('IMPROVEMENT NEEDS A STANDARD TO LAND IN')
    m.para('Lean tools are only useful if the improvement ends up in the management system. A bottleneck analysis '
           'that does not change a work instruction, a corrective action that does not touch the procedure, and a '
           'safety fix that is not written into the APV will all be gone within a quarter. So I run improvement '
           'with the paperwork attached: what changes, where it is written down, who is trained in it, and how the '
           'next audit will see it. That is also what makes a Great Place to Work certification credible — the '
           'people on the floor can describe what has actually changed.', after=80)

    return m.save(path, title='QEHS Manager — Belden Cekan A/S, Gjern',
                  subject='Quality, environment and safety in one integrated management system',
                  keywords='QEHS, quality, environment, safety, ISO 9001, ISO 14001, ISO 45001, audits, CAPA, '
                           'calibration, ESG, lean')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Belden_QEHSManager.docx')))
