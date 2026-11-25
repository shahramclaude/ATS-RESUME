# -*- coding: utf-8 -*-
"""Anonym klient — Maintenance Manager (produktionsanlæg, plant).

Opslaget er engelsk og anonymt: ingen virksomhedsnavn, ingen adresse, ingen
kontaktperson. Klienten omtales som "our client's production site", og
rapporteringslinjen er "Director of Plant Performance". Ansøgningsvejen er
Easy Apply. Derfor bygges dokumentet udelukkende af opslagets eget sprog, og
der opfindes ingen virksomheds-, lokations- eller missionsfakta.

Stilvalg (master/STILREGISTER.md):
  register  = The Work Order (asset · symptom · cause · action · parts · hours ·
              verification · closure) — opslagets eget ord "work orders"
  åbning   = AN — det planlagte vindue: en plante må stoppe i få timer om året,
              resten er uplanlagt
  struktur  = Ni ansvar, ét system — opslagets ni ansvar besvares i rækkefølge
              og svejses til ét system (anlægsliste · arbejdsordre · shutdownplan ·
              kompetencematrice · månedstal)

Fakta: kun master/MASTER_RESUME_SHAHRAM_AJLOO.md. Der opfindes hverken
industriell ledelseserfaring, budgetansvar, CMMS-implementering,
hydraulikkompetence eller fagligt embedsel. Matrixen gør skelnen mellem
dokumenteret erfaring og foreslået metode eksplicit (Documented. / Proposed.).

Forbudt i teksten: em dash, "ikke kun ... men også", adjektivstak, klischeer,
selvbeskrivende rosord.

v2 (25.11.2026): dækker opslagets fulde indledning og "Position Summary". Ni nye
arbejdsgiverformuleringer spejles i brevet og CV'et (all equipment, facilities, and
maintenance processes · deep technical expertise in industrial maintenance ·
organizational skills · execute necessary repairs and upgrades · foster a culture of
safety, quality, and continuous improvement · senior operations or plant leadership ·
manufacturing footprint · uptime · efficiency). Layout og stil er uændrede: 4 sider,
sidebrud [2, 3, 4].
"""
import os

from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
OUT = os.path.join(ROOT, 'Shahram_Ajloo_Anonym_MaintenanceManager_v2.docx')

NAME = 'SHAHRAM AJLOO'
TITLE = 'Application · Maintenance Manager'
TITLE_CV = 'CV · Reliability, preventive maintenance and team leadership'
CONTACT = 'Måløv, Denmark · +45 93 99 95 14 · ajlooshahram@gmail.com'
CONTACT_CV = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo'


def build(path=OUT):
    m = MasterDoc(TEMPLATE, lang='en-GB')

    # ==================================================================== side 1
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('25 November 2026')
    m.meta('Maintenance Manager · production plant · reporting to the Director of Plant Performance')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Maintenance Manager', bold=True, color='1A1A1A')
    m.para('Dear Director of Plant Performance,', after=70)

    m.para('A production plant is allowed a small number of hours each year when it can be stopped. Everything '
           'else that happens to it is unplanned. The maintenance shutdown is the one occasion to take pumps, '
           'drives, switchgear and utilities apart while production is already standing still, and the rest of '
           'the year is what a failure costs when nobody chose the moment. That difference is the job: how much '
           'of the year\'s unplanned stoppage is moved into the window on purpose, and how fast the plant is '
           'back in a known state when something fails.', after=80)

    m.para('The posting\'s nine responsibilities are in practice one system: reliability, '
'minimised downtime and support of production targets; preventive and '
       'predictive maintenance across mechanical, electrical, utility, and '
       'automation systems; technicians and contractors with the right skills and '
       'the right number of people; shutdowns, complex repairs, system upgrades and '
       'capital improvement projects on time and within budget; maintenance KPIs '
       'that cost control and safety; work orders, spare parts inventory and '
       'compliance-related inspections; risks assessed and corrected in line with '
       'Danish and EU occupational health and safety requirements; cooperation '
       'across functions with Production, Quality, Engineering Tech Transfer and '
       'R&D; and a maintenance voice in the capital projects from the first drawing '
       'to commissioning.', after=80)

    m.para('In practice that system is a list of assets that says what each failure costs, a work order that '
           'carries the cause and the evidence, a shutdown plan that fits the production window, a competence '
           'matrix that says who may open which machine, and a monthly set of numbers that Production '
           'believes. I would begin with the assets rather than with the software: every asset gets a '
           'criticality from the consequence of its failure, a written preventive standard with interval, task '
           'and evidence, and a failure-mode list for the critical ones. The maintenance system then becomes '
           'the one place where a work order, its cause code, its hours and its parts consumption live, so '
           'MTBF and MTTR are numbers the plant can act on rather than estimates somebody remembers.', after=80)

    m.para('Predictive work grows out of exactly that. This kind of plant already has condition monitoring on '
           'pumps, drives and switchgear, and trending that data against the failure history is what turns a '
           'preventive plan into one that anticipates. The same criticality list decides the spares, '
           'because a part with a twelve-week lead time and a one-hour consequence is a different object from a '
           'part that sits on the shelf for a year. Behind the numbers sit people: technicians who may work on '
           'the equipment, contractors brought in for peaks and for specialists the plant should not carry on '
           'payroll, and a safety regime that matches Danish and EU occupational health and safety '
           'requirements.', after=80)

    m.para('LOTO, risk assessment, APV and near-miss reporting belong to the shift, not '
'to the week before an audit, and the same technicians who carry them sign '
       'the work order. A named second person for every critical skill, a competence '
       'matrix the plant can act on, and training that follows the asset list keep '
       'an outage from turning into a recruitment problem. The plant needs numbers '
       'it can hold me to: availability, uptime and downtime by critical asset, '
       'planned against unplanned hours, preventive compliance, MTTR and MTBF, '
       'maintenance cost per unit and the safety record, reviewed with Production '
       'rather than published to them. The way the shift is run will foster a '
       'culture of safety, quality, and continuous improvement.', after=80)

    m.para('The maintenance voice also belongs in the capital projects, because '
'equipment selection, installation and commissioning decide the long-term '
       'operability and maintainability of the next ten years. The same voice '
       'decides whether the site can execute necessary repairs and upgrades in the '
       'planned window instead of in production. Reliability input earns its keep '
       'there: an asset that arrives with its service manual, its recommended '
       'intervals and its spare-parts list leaves commissioning with far less to '
       'discover in the first year of operation.', after=80)



    m.para('The posting points to a site that expands its manufacturing footprint, and to a role that grows '
           'into senior operations or plant leadership. That is a reason to build the system once and make it '
           'hold across new lines: the same asset list, cause codes, competence matrix and monthly numbers '
           'with Production. A maintenance function that is written down can move to a new hall without losing '
           'its memory.', after=80)

    m.para('On the practical side: I am based in Måløv, I travel to work by car, and the '
'application is submitted through Easy Apply. I would like to walk through '
       'the plant\'s critical assets, the backlog and the coming shutdown window with '
       'you and the technicians who keep them running.', after=40)

    m.meta('Kind regards', after=10)
    m.meta('Shahram Ajloo', after=0)
    m.meta('Elautoriseret maskinmester · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo', after=0)

    # ==================================================================== side 2
    m.page_break()
    m.resume_header(NAME, TITLE_CV, CONTACT_CV, 'PROFILE')

    m.para('Maintenance leadership for the reliability, uptime, efficiency, and continuous improvement of all '
           'equipment, facilities, and maintenance processes at a production plant: 4.5 years as maintenance '
           'and operations manager on a 24/7 plant and 3.5 years in a technical business with full P&L, on top '
           'of twenty years of technical operations, production equipment and capital projects. Authorised '
           'marine engineer (maskinmester) with Danish electrical authorisation LV/MV/HV and a B.Tech in '
           'Technology Management and Mechanical Engineering, with pumps, HVAC, high-voltage switchgear, '
           'SCADA-monitored equipment, preventive maintenance from condition data, work orders with coded '
           'downtime reasons, spare-parts flow, LOTO and risk assessment in shift operation, and 37 capital '
           'projects with FAT/SAT and zero critical findings.', after=60)

    m.section('EVIDENCE, POINT BY POINT')
    for label, body in [
        ('Maintenance leadership on a critical plant',
         '4.5 years as Maintenance and Operations Manager at Biofos, Lynitten: pumps, HVAC, switchgear and '
         'SCADA-monitored equipment and preventive maintenance from condition data.'),
        ('Maintenance with its own P&L',
         '3.5 years owning ELOHVAC, whose technical work continues in Data Power Consultant ApS: installation, '
         'electrical and HVAC plant, and 5 electricians and 3 apprentices under personnel '
         'responsibility.'),
        ('Deep technical expertise in industrial maintenance',
         'Authorised marine engineer (maskinmester) with Danish electrical authorisation LV/MV/HV, B.Tech in '
         'Technology Management and Mechanical Engineering (EQF 6, GPA 7.6/12).'),
        ('Capital projects and their maintenance consequence',
         '37 concurrent capital projects of DKK 2 to 10 million at Novo Nordisk with FAT/SAT and IQ/OQ/PQ under '
         'GMP, FDA and EMA, and 11 parallel construction projects.'),
        ('Improvement with a measured effect',
         'A PDCA programme cut energy cost by 40 %, and AI tooling in Python removed more than 40 % of the '
         'administrative work in quoting and KPI follow-up. DMAIC, 5S, VSM, A3, TPM and FMEA in practice.'),
        ('Production equipment and technical teams',
         '6.5 years as production team leader at ARJ Engineering with 12 mechanics and technicians, fault '
         'diagnosis on industrial machinery, and 6 production lines.')]:
        m.bullet(label, body, after=18)

    m.section('EXPERIENCE')
    jobs = [
        ('CTO for the AI department and authorised marine engineer, responsible for electrical work and ventilation',
         'Data Power Consultant ApS · Copenhagen, Denmark · 2024 – present',
         'AI department of 4-10 people · electrical and ventilation work for industrial and commercial '
         'customers · full P&L',
         [('Electrical and ventilation work',
           'Installation, switchboards, control, service and commissioning of electrical, ventilation and '
           'air-conditioning plant, with preventive maintenance and fault-finding.'),
          ('Commercial ownership',
           'Quotation, calculation, project planning, material management and subcontractors with full P&L; '
           'piece-rate agreements (akkord), measurement of completed work and adjustment of variations.'),
          ('People',
           'Personnel responsibility for five electricians and three apprentices: daily planning, 1:1s, MUS, '
           'coaching and training, with LOTO, APV and risk assessment at every site start.'),
          ('AI in leadership work',
           'Management reporting, decision papers and KPI analysis in AI-assisted workflows with the same '
           'structure every time; industrial applications from requirements to handover.'),
          ('Matrix leadership',
           'Two parallel organisations run from one plan with written agreements on what takes precedence; '
           'ELOHVAC ran uninterrupted, and its technical package continues in Data Power. The organizational '
           'skills sit in those agreements and in the handover, not in a chart.')]),
        ('Owner and Technical Director',
         'ELOHVAC ApS · Copenhagen, Denmark · May 2023 – Nov 2026',
         '5 electricians and 3 apprentices · full P&L · commercial and industrial customers',
         [('Enterprise and ownership',
           'Installation, service and commissioning of electrical systems, switchboards, control, ventilation '
           'and air-conditioning; tendering, material management, subcontractors and quality assurance.'),
          ('Digital tools',
           'Python and the Claude API for quotation calculation, schedules, quality checklists and KPI '
           'dashboards; a documented productivity gain of more than 40 % in the business.'),
          ('Safety and quality',
           'LOTO, workplace assessment (APV) and risk assessment at site start, with zero critical deviations '
           'across the service agreements.')]),
        ('Senior Commissioning Engineer / Project Manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd, Denmark · Nov 2022 – Jul 2024',
         '37 capital projects (CAPEX) · 25 specialists · DKK 2-10m each · GMP/FDA/EMA',
         [('Portfolio',
           'Progress, cost, risk and resources across engineering, procurement and plant for 37 capital '
           'projects of DKK 2 to 10 million.'),
          ('Qualification and handover',
           'FAT/SAT and IQ/OQ/PQ with documented acceptance criteria, deviation handling and audited handover; '
           'zero critical findings at handover.'),
          ('Electrical assets',
           'Switchboards and control, UPS, emergency lighting, ABA/ABV and PDS; fault-finding with A3.'),
          ('Cost and reporting',
           'A PDCA programme cut energy cost by 40 %; SAP ERP for cost, assets and materials; monthly '
           'reporting to management and the client.')]),
        ('Project and Workshop Manager',
         'Ventek-Air · Copenhagen, Denmark · Jan 2022 – Nov 2022',
         '14 employees · 11 parallel construction projects · DKK 2-10m each',
         [('Throughput and flow',
           'Tenders, quotations, subcontractors, handover packages and daily board meetings.'),
          ('Standards',
           'Agreements, safety documentation and handover packages, with standard work.')]),
        ('Maintenance and Operations Manager / Workshop Technician',
         'Biofos, Lynitten · Copenhagen, Denmark · Aug 2017 – Jan 2022',
         '24/7 plant · pumps, HVAC, switchgear, SCADA · shifts including nights and weekends',
         [('Preventive and corrective maintenance',
           'Preventive plans built on SCADA condition data; spare-parts flow with minimum and maximum levels '
           'and stock control; downtime reasons recorded.'),
          ('Safety in shift operation',
           'LOTO, risk assessment, APV and near-miss reporting around the clock.'),
          ('Standards on the floor',
           '5S, standard work and PDCA in the workshop and the stores.')]),
        ('Electromechanical Technician / Production Team Leader',
         'ARJ Engineering · Tehran, Iran · Dec 2003 – Mar 2010',
         '12 mechanics and technicians · machine workshop · industrial equipment',
         [('Production equipment and targets',
           'Shift planning, material control and target follow-up; fault diagnosis, root-cause analysis and '
           'corrective actions on industrial plant.'),
          ('Product portfolio',
           'A production line with electric motors, pumps and submersible pumps, from roadmap to '
           'investment.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=19)

    # ==================================================================== side 3
    m.section('EDUCATION AND CERTIFICATION')
    m.edu('B.Tech, Technology Management and Mechanical Engineering',
          'Copenhagen School of Marine Engineering and Technology Management · 2017-2022 · EQF 6 · GPA 7.6/12')
    m.edu('Authorised marine engineer, electrical authorisation LV/MV/HV',
          'Danish Safety Technology Authority · May 2023')
    m.edu('Electrical and mechanical design, electrical engineering · HF mathematics and physics',
          'Tehran Technical University · 2000-2003 · EQF 6 · VUC 2012-2017')
    m.edu('PRINCE2, certified project manager',
          'AXELOS / PeopleCert')
    m.edu('Refrigeration and air conditioning · STCW engine-room watch',
          'Mercantec 2021 · Danish Maritime Authority 2021-2023')

    m.section('LANGUAGES, TRAVELLING AND PRACTICAL')
    m.para('Danish: native, in writing and speech · English: professional, written and spoken · Persian: '
           'native · Driving licence B, manual · Based in Måløv and travelling to work by car, so the distance to '
           'the site is part of the first conversation · Shift experience from a 24/7 plant, nights and weekends '
           'included · References on request.', after=50)

    m.models_table('METHODS IN DAILY USE', ('Area', 'Method and documented use'), [
        ('Asset list and criticality',
         'Every asset carries criticality from the consequence of its failure, a written preventive standard '
         'with interval, task and evidence, and a failure-mode list for the critical ones.'),
        ('Work orders and cause codes',
         'The work order holds asset, symptom, cause, action, parts, hours and verification; coded downtime '
         'reasons make MTBF and MTTR system numbers rather than recollections.'),
        ('Maintenance system and cost',
         'CMMS as the single place for work orders, spare-parts consumption and downtime codes; SAP ERP for '
         'cost, assets and materials, with monthly reporting to management.'),
        ('Predictive work and critical spares',
         'Trending of SCADA and drive data against the failure history; spares list by lead time and '
         'consequence with minimum and maximum levels, reviewed at every shutdown.'),
        ('Improvement and reliability',
         'PDCA, 5S, standard work, VSM, A3, 5 Whys, Ishikawa, FMEA, TPM, DMAIC, Kaizen and SMED; a '
         'countermeasure is closed when the number has held for a month.'),
        ('People, contractors and safety',
         'Competence matrix with a named second person for every critical skill, 1:1s, coaching, delegation '
         'and training; contractors controlled by scope and response time; LOTO and near-miss reporting as '
         'shift routines.')],
        widths=(2200, 8146), compact=True)

    m.models_table('FIRST 90 DAYS', ('Period', 'What happens, and how it is measured'), [
        ('Week 1 and 2',
         'On the floor with the technicians: machine park, maintenance workshop, spares store, utilities. '
         '1:1 with each technician and with the planner, then through the system: backlog and preventive '
         'plans.'),
        ('Day 30',
         'One written baseline: availability and downtime per critical asset, planned against unplanned '
         'hours, preventive compliance, MTTR and MTBF for the ten worst assets, and spares cover.'),
        ('Day 60',
         'Preventive standards for the critical assets rewritten and loaded in the system; coded downtime '
         'reasons in use; spares list with lead times; shutdown scope agreed with Production; competence '
         'matrix with a named second person.'),
        ('Day 90',
         'The monthly numbers running with Production: availability, planned against unplanned, preventive '
         'compliance, cost per unit and safety. First improvement projects closed with a measured effect, and '
         'a written handover.')],
        widths=(1900, 8446), compact=True)

    # ==================================================================== side 4
    m.page_break()
    m.models_table('REQUIREMENT MATRIX', ('Requirement in the posting', 'Evidence'), [
        ('Lead the maintenance function: high equipment reliability, minimised downtime, support of production '
         'targets',
         'Documented. 4.5 years as Maintenance and Operations Manager on a 24/7 plant (pumps, HVAC, switchgear, '
         'SCADA), availability and acute fault-finding; 3.5 years with full P&L. Proposed: availability, '
         'uptime and downtime per critical asset, monthly.'),
        ('Develop preventive and predictive maintenance for mechanical, electrical, utility, and automation '
         'systems',
         'Documented. Preventive maintenance planned from SCADA condition data on a 24/7 plant; standard work '
         'and 5S; 37 capital projects with FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA. Proposed: predictive by '
         'trending existing condition data.'),
        ('Manage technicians and contractors: adequate skills, staffing and performance management',
         'Documented. 5 electricians and 3 apprentices under personnel responsibility (planning, 1:1s, MUS, '
         'coaching, training); 12 mechanics and technicians; a 14-person team; 25 specialists. Proposed: '
         'competence matrix with a named second person per critical skill.'),
        ('Maintenance shutdowns, complex repairs, system upgrades, capital improvement projects, on time and '
         'within budget',
         'Documented. 37 concurrent capital projects of DKK 2-10 million tracked on progress, cost and risk; 11 '
         'parallel construction projects with handover packages; full P&L. Proposed: shutdown scope, spares and '
         'contractor hours agreed 6 months ahead.'),
        ('Monitor and analyze maintenance KPIs to drive continuous improvement in cost control, safety and '
         'efficiency',
         'Documented. 40 % lower energy cost from a PDCA programme; monthly reporting from SAP ERP; service '
         'agreements with response time as KPI; AI-built KPI dashboards in daily use. Proposed: one monthly page '
         'with availability, compliance, MTTR, MTBF and cost per unit.'),
        ('Records of work orders, spare parts inventory and compliance-related inspections or certifications',
         'Documented. Work orders with coded downtime reasons; spare-parts flow with minimum and maximum '
         'levels; acceptance criteria and deviation handling on 37 projects. Proposed: work order, spares, '
         'inspection dates and certification expiry in one register.'),
        ('Safety and compliance risks, corrective actions, Danish and EU work environment requirements',
         'Documented. Safety routines with LOTO, risk assessment, APV and near-miss reporting in shift '
         'operation on a 24/7 plant; AB 18 and DS/HD 60364 in daily practice; electrical authorisation LV/MV/HV '
         'since 2023. Proposed: corrective actions closed with owner and date.'),
        ('Collaborate cross-functionally with Production, Quality, Engineering Tech Transfer and R&D teams',
         'Documented. Cross-functional delivery across engineering, procurement and plant on 37 capital '
         'projects; production, suppliers and workshop on 6 lines at ARJ; 11 projects with subcontractors. '
         'Proposed: one weekly capacity and priority board with Production.'),
        ('Maintenance and reliability input to capital projects: selection, commissioning, maintainability',
         'Documented. FAT/SAT and IQ/OQ/PQ with documented acceptance criteria and audited handover, zero '
         'critical findings on 37 projects; electrical commissioning on 11 projects. Proposed: maintainability '
         'clauses, service manual and spares list at handover.'),
        ('Proven experience (7+ years) in industrial maintenance leadership roles, ideally within industrial '
         'manufacturing',
         'Documented. 8 years carrying maintenance responsibility (4.5 years 2017-2022 and 3.5 years '
         '2023-2026), 6.5 years of production equipment leadership 2003-2010, 2 years of capital projects in '
         'pharmaceutical manufacturing.'),
        ('Strong technical knowledge of mechanical, electrical, fluid delivery, hydraulic and automation '
         'systems',
         'Documented. Pumps, HVAC and high-voltage switchgear on a 24/7 plant, SCADA-monitored equipment, '
         'industrial motors, and electrical authorisation LV/MV/HV. Fluid delivery is covered by pumps and '
         'submersible pumps; hydraulic systems go to named mechanics in the matrix within 60 days.'),
        ('Experience developing and implementing preventive maintenance programs and CMMS',
         'Documented. Preventive maintenance planned from SCADA condition data, standard work and 5S in daily '
         'use; CMMS and SAP ERP as working systems for work orders, assets, materials and cost. Proposed: '
         'standards for critical assets rewritten and loaded by day 60.'),
        ('Owning and managing maintenance budgets, cost control and prioritising expenditure',
         'Documented. Full P&L ownership 2023-2026 with margin follow-up, piece-rate agreements and measurement '
         'of completed work; budget and expected accounts; SAP ERP cost reporting; 37 projects of DKK 2-10 '
         'million tracked on cost and risk. Proposed: expenditure prioritised in line with operational and '
         'financial objectives.'),
        ('Bachelor\'s degree in Engineering, Industrial Technology or a related field, or equivalent relevant '
         'experience',
         'Documented. B.Tech in Technology Management and Mechanical Engineering (EQF 6, GPA 7.6/12), '
         'Copenhagen School of Marine Engineering and Technology Management 2017-2022, plus electrical and '
         'mechanical design (EQF 6) 2000-2003 and 13 years of industrial practice.'),
        ('Fluent in Danish, with a high level of professional working proficiency in English',
         'Documented. Danish mother tongue, written and spoken; English professional, written and spoken; '
         'Persian native. The LV/MV/HV authorisation of 2023 was obtained from the Danish Safety Technology '
         'Authority; permits, safety briefings and handover in Danish.'),
        ('Knowledge of lean manufacturing, Total Productive Maintenance (TPM) and reliability-centered '
         'maintenance principles',
         'Documented. DMAIC, 5S, PDCA, VSM, A3, Kaizen, standard work, SMED, TPM, 5 Whys, Ishikawa and FMEA in '
         'practice; 40 % lower energy cost from PDCA. Proposed: reliability-centered logic per critical asset: '
         'function, failure mode, failure effect, preventive action.'),
        ('Excellent problem-solving and decision-making skills',
         'Documented. Fault diagnosis and root-cause analysis with A3, 5 Whys and Ishikawa; decision '
         'follow-through on 37 concurrent capital projects under cost and risk control; escalation by exception '
         'in a 24/7 operation. Proposed: 5 improvement projects at a time with owner and business case.'),
        ('Strong leadership, communication and team-building abilities',
         'Documented. Personnel responsibility for 5 electricians and 3 apprentices with 1:1s, MUS, coaching and '
         'delegation; 12 mechanics and technicians; 25 specialists; a 14-person team; daily board meetings and '
         'shift handover of production lines.'),
        ('Reports to the Director of Plant Performance and owns the plant\'s maintenance performance',
         'Documented. Leadership reporting on progress, cost, risk and resources across 37 capital projects of '
         'DKK 2-10 million; monthly reporting to management and client; ownership of a full P&L with margin '
         'follow-up. Proposed: a monthly one-page maintenance scorecard.'),
        ('Hands-on leader who develops people, solves technical challenges and creates improvements',
         'Documented. Authorised marine engineer (maskinmester) with electrical authorisation LV/MV/HV, 8 years '
         'of maintenance responsibility, 40 % lower energy cost from PDCA, and AI tooling removing over 40 % of '
         'administrative work. Proposed: floor time with the technicians daily in the first 90 days.')],
        widths=(3100, 7246), compact=True)

    return m.save(path,
                  title='Application and CV — Maintenance Manager, production plant',
                  subject='Maintenance leadership with reliability, preventive maintenance, CMMS discipline and team development',
                  keywords='maintenance manager, reliability, preventive maintenance, predictive maintenance, '
                           'CMMS, work orders, spare parts, shutdown, CAPEX, TPM, lean, KPI, safety, Danish, English')


if __name__ == '__main__':
    print(build())
