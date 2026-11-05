# -*- coding: utf-8 -*-
"""Terma A/S — Maintenance & Tooling Manager (Lystrup, defence and aerospace).

English deliverable (JD is English): task-first application page + CV in one document.
Culture and role intel: master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md,
section on Terma (research 05.11.2026).
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Maintenance and tooling leadership · Equipment availability in defence production'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('5 November 2026')
    m.meta('Terma A/S · Lystrup, Denmark · Maintenance & Tooling Manager')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Maintenance & Tooling Manager', bold=True, color='1A1A1A')
    m.para('Dear Hiring Manager', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('In defence production, the maintenance and tooling departments are not support functions. A machine that '
           'stands still for a day is not an inconvenience — it is a delivery commitment to a customer who audits '
           'us, and a tool that is not available stops a line even when every machine is running. So I would run '
           'the two departments against one number that production actually feels: availability. Of the machines, '
           'of the tools, and of the people who keep them running.', after=80)

    m.para('**The system I would put in place has four parts, and none of them needs a new platform.** First, '
           'criticality: every asset assessed for what its failure would do to delivery, quality and safety — and '
           'the critical ones given a written preventive standard saying what is checked, how often, by whom and '
           'with what evidence. Second, the CMMS as the single source of '
           'truth: every work order and every hour of downtime with a coded reason, so MTBF and MTTR come out of '
           'the system instead of out of somebody\'s memory. Third, tooling treated as a production resource rather '
           'than as equipment: a register with condition and calibration status, a repair and modification '
           'pipeline run with the Senior Tooling Specialist, and an availability target agreed with production. '
           'Fourth, a weekly planning conversation where preventive and corrective work are traded openly with '
           'production — instead of preventive maintenance being what gets cancelled first.', after=80)

    m.para('Around that sit the things that actually move downtime: a critical-spares list based on lead time and '
           'consequence rather than habit, standard fault-finding for the failure modes that cause most of the '
           'hours, TPM and 5S at the machine so operators catch deviations before the technician is called, and A3 '
           'with 5 Whys for every repeat failure — closed when the countermeasure has held for a month, not when '
           'the ticket is closed. Supplier management belongs in the same routine: technical specification, FAT and '
           'SAT, documented acceptance, and follow-up on response time and quality.', after=80)

    m.para('What I bring is the technical depth and the leadership the role describes. I am an authorised marine '
           'engineer — maskinmester with electrical authorisation — with a B.Tech in Technology Management and '
           'Mechanical Engineering, the foundation the posting asks for. At Biofos I ran maintenance and operations '
           'on a 24/7 plant — pumps, HVAC, high-voltage switchgear, SCADA condition monitoring, LOTO, APV and '
           'near-miss routines — and a PDCA programme cut energy cost by 40 %. At Novo Nordisk I worked inside GMP/FDA/EMA requirements across '
           '37 parallel capital projects with 25 specialists — documented acceptance criteria, FAT/SAT, '
           'IQ/OQ/PQ and audited handover with zero critical findings. At ARJ Engineering I led twelve mechanics and technicians in a '
           'machine workshop with shift planning, fault diagnosis and corrective actions on industrial production '
           'equipment. For three years I have run my own company with full P&L, five electricians and three '
           'apprentices — so I know what an idle technician costs and what it takes to keep one.', after=80)

    m.para('Two teams also means one rhythm: a shared weekly capacity and priority board — what is planned, what '
           'is unplanned, who is where, and what we are deliberately not doing this week — because the fastest way '
           'to lose a technician is to give him three priorities. Under it a competence matrix covering electrical, '
           'mechanical, CNC, automation and hydraulics, a named second person for every critical skill, and 1:1s '
           'every two weeks; your own value puts it better: we develop people and technology.', after=80)

    m.para('I will be straight about what is new. I have not worked in defence manufacturing before, and I have not '
           'run a tooling department in an aerospace supply chain with the traceability that follows from it. My '
           'maintenance side comes from a 24/7 process plant, my production-equipment side from a machine workshop '
           'and from validation work in pharmaceutical production, and tooling is the part I would learn fastest by '
           'standing next to your Senior Tooling Specialist in the first weeks. I am also ready to go through the security clearance process with the Danish Defence '
           'Intelligence Service in full, and I am not aware of anything that would stand in the way.', after=80)

    m.para('What draws me to Terma is that the purpose is not a poster. Equipment reliability here decides whether a '
           'radar, a self-protection system or an aerostructure reaches the people who depend on it. I also recognise the culture you describe — trust, '
           'collaboration, knowledge sharing, and a company that has just moved from number 30 to number 16 among '
           'engineering professionals. That is the kind of department I want to lead.', after=80)

    m.para('Practically: I live in Måløv, about 40 minutes by car from Lystrup. I speak Danish natively and English '
           'professionally. I am also an active Claude coder and build my own Python tools for '
           'reliability follow-up — downtime and MTBF dashboards, spare-parts criticality, and investment cases with '
           'NPV, IRR, sensitivity and scenarios when a machine is to be replaced.', after=80)

    m.para('I would like to come to Lystrup, walk the production floor and the tooling store with you, and talk '
           'through the first ninety days and where I see the biggest availability gains.', after=40)
    m.meta('Kind regards', after=10)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('Maintenance and production leader with 20+ years from technical operations, production equipment and '
           'projects — authorised marine engineer (maskinmester) with electrical authorisation and a B.Tech in '
           'Technology Management and Mechanical Engineering. Five years of maintenance responsibility on a 24/7 '
           'plant, two years of equipment qualification under GMP/FDA/EMA, and three years of full P&L in his own '
           'technical company. Works from a register, a standard and a number: criticality, preventive standards, '
           'CMMS discipline and MTBF/MTTR rather than anecdotes.', after=80)

    m.section('MAINTENANCE, TOOLING AND RESULTS')
    for label, body in [
        ('Equipment availability and preventive maintenance',
         'Five years of maintenance responsibility on a 24/7 plant: pumps, HVAC, high-voltage switchgear and '
         'SCADA-monitored equipment. Preventive maintenance from condition data and corrective work prioritised by '
         'consequence.'),
        ('Technical teams led',
         'Twelve mechanics and technicians in a machine workshop; 25 specialists across 37 capital projects; five '
         'electricians and three apprentices with full personnel responsibility.'),
        ('Tooling, workshop and production equipment',
         'Workshop and machine-park responsibility: fault diagnosis, root-cause analysis and corrective actions on '
         'industrial production equipment; jigs, fixtures and test equipment specified and commissioned.'),
        ('Supplier and service management',
         'Technical specification, FAT/SAT and documented acceptance of equipment, suppliers and service '
         'partners under GMP/FDA/EMA.'),
        ('Continuous improvement with measured effect',
         'PDCA, 5S, standard work, VSM, A3 and 5 Whys in daily use. A PDCA programme cut energy cost by 40 %; own '
         'Python/Claude tools took over 40 % of the administrative work out of quoting and KPI follow-up.')]:
        m.bullet(label, body, after=22)

    m.models_table('TOOLS AND METHODS', ('Task', 'Tool and documented use'), [
        ('Asset reliability',
         'Asset register with criticality, preventive standards, failure mode analysis (FMEA) and MTBF/MTTR per asset.'),
        ('CMMS and work orders',
         'CMMS as single source of truth: work orders, coded downtime reasons and spare-parts consumption per '
         'asset. SAP ERP for assets, materials and cost.'),
        ('Tooling control',
         'Tool register with condition, calibration and location; repair and modification pipeline with owner and '
         'deadline; availability target agreed with production.'),
        ('Continuous improvement',
         'PDCA, 5S, TPM, standard work, VSM, Kaizen, A3 and 5 Whys with verified countermeasures; a limited '
         'project funnel with business case and measured effect.'),
        ('Safety and compliance',
         'LOTO, APV/workplace assessment, risk assessment, near-miss reporting and safety walks; documented '
         'procedures and audit readiness under GMP/FDA/EMA.'),
        ('People management',
         'Situational Leadership (SLII), delegation ladder, 1:1s every two weeks, reviews, GROW and SBI feedback, '
         'competence matrix and apprentice development to trade test.')])

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director',
         'ELOHVAC ApS · Copenhagen, Denmark · May 2023–present',
         '5 electricians and 3 apprentices · full P&L · commercial and industrial customers',
         [('Commercial and operational ownership', 'Quoting, pricing, margin follow-up and service agreements with '
                                                  'response time, quality and delivery as KPIs.'),
          ('People and safety', 'Daily planning, 1:1s, reviews, coaching of a field-based team, competence matrix '
                                'and apprentice training; LOTO, risk assessment and APV at every site start.'),
          ('Digital tools', 'Python and Claude API for quotations, scheduling, quality checklists and KPI '
                            'dashboards; productivity gain above 40 % in the business.')]),
        ('Senior Commissioning Engineer / Project Manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd, Denmark · Nov 2022–Jul 2024',
         '37 capital projects · 25 specialists · DKK 2–10m each · GMP/FDA/EMA',
         [('Equipment and supplier qualification', 'FAT/SAT and IQ/OQ/PQ with documented acceptance criteria, '
                                                   'deviation handling and audited handover; zero critical findings '
                                                   'at handover.'),
          ('Performance and improvement', 'Progress, cost, risk and resources across engineering, procurement and '
                                          'operations; A3 and 5 Whys in fault finding.')]),
        ('Project and Workshop Manager',
         'Ventek-Air · Copenhagen, Denmark · Jan 2022–Nov 2022',
         '14 employees · 11 parallel construction projects · DKK 2–10m each',
         [('Throughput and flow', 'Tenders, quotations, subcontractors and handover packages. Daily board meetings, '
                                  'bottleneck analysis and standardised routines lifted delivery performance.')]),
        ('Maintenance and Operations Manager / Workshop Technician',
         'Biofos, Lynetten · Copenhagen, Denmark · Aug 2017–Jan 2022',
         '24/7 plant · pumps, HVAC, switchgear, SCADA · shifts including nights and weekends',
         [('Preventive and corrective maintenance', 'Preventive maintenance planned from SCADA condition data; '
                                                   'spare-parts flow with min/max levels; downtime reasons recorded '
                                                   'and followed.'),
          ('Safety and standards', 'LOTO, risk assessment, APV and near-miss reporting in shift operations; '
                                   'standard work, 5S and PDCA on the workshop and stores.')]),
        ('Electromechanical Technician / Production Team Leader',
         'ARJ Engineering · Tehran, Iran · Dec 2003–Mar 2010',
         '12 mechanics and technicians · machine workshop · industrial equipment',
         [('Production equipment and targets', 'Shift planning, material control and target follow-up; fault '
                                               'diagnosis, root-cause analysis and corrective actions on industrial '
                                               'machinery and production lines.')]),
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
    m.para('Danish: native · English: professional · Persian: native · Driving licence B · Lives in Måløv, about '
           '40 minutes by car from Lystrup; relocation not required · Ready to go through the security clearance '
           'process · References from Novo Nordisk and Biofos on request.', after=70)

    m.models_table('WHAT THE ROLE ASKS FOR — MY EVIDENCE', ('Requirement', 'Evidence'), [
        ('Relevant technical education — marine, mechanical or production engineer',
         'Authorised marine engineer (maskinmester) with electrical authorisation LV/MV/HV and B.Tech in '
         'Technology Management and Mechanical Engineering (EQF 6) — the foundation the posting describes.'),
        ('Experience from maintenance, tooling, production engineering or similar',
         'Five years of maintenance and operations on a 24/7 plant; workshop and machine-park responsibility; two '
         'years of equipment qualification under GMP/FDA/EMA. Aerospace tooling is new to me.'),
        ('Strong leadership of technical teams',
         'Twelve mechanics and technicians; 25 specialists across 37 projects; a 14-person team; five electricians '
         'and three apprentices with full personnel responsibility including hiring, reviews and employee '
         'development.'),
        ('Solid understanding of production equipment and maintenance processes',
         'Preventive standards, criticality, CMMS discipline, MTBF/MTTR, critical spares, fault diagnosis and root '
         'cause on pumps, HVAC, switchgear and machine tools; daily work with contractors and service partners.'),
        ('Structured, proactive, able to prioritise in a dynamic production environment',
         'Weekly capacity and priority board, 12-week resource planning and a written "what we are not doing this '
         'week" list; escalation by exception; five years of 24/7 operations.'),
        ('Danish and English at professional level',
         'Danish native, English professional written and spoken; two years in an international project '
         'organisation with English as the working language.'),
        ('Maintenance management, CMMS, automation, CNC and technical supplier management',
         'CMMS and SAP as daily systems; CNC and automation equipment maintained in workshop and plant settings; '
         'supplier selection and FAT/SAT documented across 37 projects.'),
        ('Security clearance by the Danish Defence Intelligence Service',
         'Ready to go through the process in full and provide the documentation it requires; no known impediments.')])
    m.page_break()

    m.models_table('FIRST 90 DAYS — ASSETS, TOOLING, TEAMS', ('Period', 'What happens, and how it is measured'), [
        ('Week 1–2',
         'On the floor at every production area with the technicians: machine park, tooling store, calibration, '
         'spare-parts store and the maintenance workshop. 1:1 with every technician and with the Senior Tooling '
         'Specialist. Systems walk-through: CMMS, work-order backlog, PM plans and open deviations.'),
        ('Day 30',
         'One-page baseline written: availability per line, PM compliance, open corrective backlog, MTTR and MTBF '
         'for the ten most critical assets, tooling availability, and where the hours actually go. Criticality '
         'list agreed with the Senior Manager Production Equipment.'),
        ('Day 60',
         'Preventive standards rewritten for the critical assets and loaded in the CMMS. Coded downtime reasons in '
         'use, so MTBF/MTTR are system numbers rather than estimates. Tooling register complete with condition, '
         'calibration and repair pipeline. Weekly capacity and priority board running for both departments.'),
        ('Day 90',
         'Measured movement in PM compliance and in availability on at least two critical lines. Critical-spares '
         'list and min/max levels agreed. Competence matrix for both departments with a named second person for '
         'every critical skill, and a training plan for the year. A written handover of the routine, so it does not '
         'depend on me being in the building.')])

    m.section('HOW EQUIPMENT AVAILABILITY IS ACTUALLY BUILT')
    m.para('Availability is not the absence of breakdowns; it is the sum of small decisions made before the '
           'breakdown. Which assets matter, what is done to them and how often, whether the spare is on the shelf '
           'when the lead time is twelve weeks, whether the operator notices the noise on Tuesday instead of the '
           'stop on Friday, and whether the repeat failure is actually fixed or just restarted. That is why I start '
           'with criticality and a written standard rather than with a new tool: a preventive plan that nobody can '
           'audit is a wish, and a CMMS filled in after the fact is a diary, not a control system.', after=80)

    m.section('TOOLING AS A PRODUCTION RESOURCE')
    m.para('Tooling is where a factory loses hours that no maintenance report shows, because the machines are '
           'running and the work still cannot start. So tooling gets the same treatment as the machine park: a '
           'register that is complete and trusted, a preventive and calibration cycle tied to use rather than to '
           'the calendar alone, a repair and modification pipeline with an owner and a date, and an availability '
           'target that production and tooling have agreed on together. The Senior Tooling Specialist owns the '
           'technical judgement; my job is to make sure priorities, capacity and escalation support that judgement '
           'instead of working around it — and that improvements to a tool are recorded, so the next one is better.', after=80)

    m.section('IMPROVEMENT THAT SHOWS UP IN NUMBERS')
    m.para('I keep a short improvement funnel — five projects at a time, no more — each with an owner, a business '
           'case and a measured effect. In maintenance the candidates are usually the same everywhere: the twenty '
           'per cent of failure modes that cause most of the downtime, spare-parts availability against lead time, '
           'the handover between shifts, and the quality of the fault description that reaches the technician. '
           'PDCA, A3 and 5 Whys are the tools, but the discipline is verification: a countermeasure is closed when '
           'the number has held for a month, not when the work order is signed.', after=80)

    m.section('SAFETY, QUALITY AND THE DEFENCE CONTEXT')
    m.para('In a defence company, maintenance work is also a security and quality question. Work on production '
           'equipment happens under documented procedures, with change control before anything is altered, with '
           'traceability of what was done and by whom, and with LOTO, risk assessment, APV and near-miss reporting '
           'as daily routines rather than campaigns. I have worked this way under GMP, FDA and EMA, where a '
           'missing signature stops a release, and in 24/7 operations where a shortcut costs an injury. The '
           'vocabulary changes in aerospace; the discipline does not.', after=80)

    m.section('TWO DEPARTMENTS, ONE RHYTHM')
    m.para('Maintenance and Tooling will always compete for the same technicians, the same hours and the same '
           'goodwill from production and from stakeholders across the plant. Two departments with two separate '
           'priority lists is how that competition becomes friction. So one weekly board, one list of priorities '
           'agreed with the Senior Manager '
           'Production Equipment and production, one escalation route, and a monthly review where each department '
           'reports three numbers and one improvement. The rest is leadership: 1:1s, a competence matrix that shows '
           'who can do what on which equipment, a named second person for every critical skill, and technicians who '
           'are trained on the next machine rather than only on the one they already know.', after=80)

    m.section('DIGITAL WORK AND AI')
    m.para('I am an active Claude coder and build my own tools in Python: downtime and MTBF follow-up pulled from '
           'several sources into one page, spare-parts criticality against lead time and consumption, tooling '
           'status lists, and investment cases with NPV, IRR, sensitivity and scenarios when a machine is replaced '
           'or capacity is expanded. None of it replaces the CMMS — it makes the numbers in it readable in '
           'minutes, which is usually the difference between a report that is used and a report that is filed.', after=80)

    return m.save(path, title='Application and CV — Maintenance & Tooling Manager, Terma',
                  subject='Maintenance and tooling leadership with equipment availability, CMMS discipline and team development',
                  keywords='maintenance manager, tooling, CMMS, availability, MTBF, MTTR, leadership, continuous improvement')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Terma_MaintenanceToolingManager.docx')))
