# -*- coding: utf-8 -*-
"""VELUX — Technical Services Manager (Technical Manager), Skjern.

English deliverable (the posting is English): application page + CV in one document.
Policy: master/README.md — extreme confidence, no caveats.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Technical Services Manager · Equipment reliability, engineering and digitalisation'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('6 November 2026')
    m.meta('VELUX · Bækgårdsvej 39, Skjern · Technical Services Manager')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Technical Services Manager, VELUX Skjern', bold=True, color='1A1A1A')
    m.para('To the General Manager and the hiring team at VELUX Skjern', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('A highly automated line does not fail slowly. It stops — and in the minute it stops, every decision that '
           'was not made in the year before shows up at once: the bearing nobody planned to change, the spare part '
           'that was not on the shelf, the alarm that had been dismissed four times, the technician who was the only '
           'one who knew the machine. Technical Services exists to make sure that minute does not happen. That is the '
           'job in Skjern, and it is the job I have done on a plant that could not stop.', after=80)

    m.para('**I would lead Technical Services on four fixed things.** First, **availability is designed, not '
           'repaired**: a maintenance strategy per asset built from criticality and failure mode — what stops the '
           'line, what is cheap to prevent, what is cheaper to run to failure — with uptime, MTBF, MTTR and response '
           'time measured and reviewed monthly, not discovered in a shutdown. Second, **a blueprint has to be '
           'portable**: if Skjern is to be the model for the site in France, the model has to be written down as '
           'standards rather than lived as habits — asset register, maintenance concept, spare-parts policy, data '
           'model, roles and decision rights, aligned with VELUX global standards — so another site can adopt it without '
           'Skjern standing next to them. '
           'Third, **digitalisation only where it removes a decision or a manual step**: condition data, alarm logs '
           'and production data turned into something a technician and a manager can act on — the operational KPIs the '
           'site is measured on — with the before-and-after number attached. Fourth, **engineers and technicians grow through the work**: a competence matrix and capability plan per area, '
           'project engineers with a real mandate, and coaching that makes the team less dependent on any single '
           'person — including me.', after=80)

    m.para('Equipment reliability is my daily trade. For five years I was operations and maintenance manager at '
           '**Lynetten under Biofos**, one of Denmark\'s largest wastewater plants, in **24/7 operation**: pumps, '
           'blowers, ventilation, transformers, switchgear, drives and SCADA, with a maintenance team, a spare-parts '
           'stock and an availability target that was not negotiable. I ran **condition-based maintenance**, '
           '**criticality assessment** per system, **root cause analysis** on repeat failures and **5S and PDCA** on '
           'workshop and stores — equipment stability and process optimisation as a daily discipline rather than a '
           'project — and energy management on metering and SCADA data delivered **more than 40 % lower '
           'consumption**, documented and sustained.', after=80)

    m.para('Building and integrating new equipment is the other half of this role, and I have done it inside a '
           'regulated production environment. At **Novo Nordisk** I ran **37 parallel capital projects** with **25 '
           'highly specialised engineers and specialists**, 2–10 million DKK each, through **FAT/SAT, IQ/OQ/PQ, '
           'installation and commissioning** into live production, with **zero critical findings** at audited '
           'handover. That is where you learn the difference between a machine that works and a machine that is '
           'reliable: acceptance criteria that can be tested, documentation that follows the asset, and a handover '
           'that ends without reservations.', after=80)

    m.para('I have led the teams this role leads. As owner of **ELOHVAC** since 2023 I run **five electricians and '
           'three apprentices** with full P&L and a **driver\'s licence and a car in daily use** for a service '
           'business; before that I led **14 employees and 11 concurrent projects** at **Ventek-Air**, with daily '
           'boards, capacity planning and standardised work, and **12 technicians** at **ARJ Engineering** in a '
           'machine workshop where root cause and follow-up were the daily measure. Digitalisation is not a slide '
           'for me: I build my own tools in **Python and Claude** — KPI dashboards, automated reporting, checklists '
           'and calculation — with **over 40 % documented productivity gain**, and I use them to remove manual work '
           'rather than to add another system to learn.', after=80)

    m.para('VELUX is a family-owned company with foundations behind it, a mature Lean culture and a production site '
           'in Skjern that is being asked to become the reference for another country. That combination is what '
           'attracts me: technical work that has to be good enough to copy, in a company where courage and mutual '
           'respect are stated values rather than posters. Values-based leadership, collaboration and technical excellence '
           'are the three things I would bring as Technical Manager, together with the stakeholders across Operations, '
           'Engineering, Quality and Production that this role sits between. I would like the technical standard in Skjern to be '
           'something a colleague in France can pick up and use — and I would like the people who built it to be '
           'the ones who teach it.', after=80)

    m.para('Practically: I live in Måløv, Skjern is around three hours away by car, and I plan my weeks around being '
           'at the site and at home at weekends. I speak and write fluent **Danish and English**, hold a **B.Tech degree '
           'in Technology Management & Mechanical Engineering** (marine engineering direction) and an electrical '
           'authorisation **LV/MV/HV**, and I can start by agreement. I would like to hear where Skjern\'s biggest '
           'availability losses are today, and which part of the Skjern model is meant to travel to France first — '
           'that is where I would begin.', after=70)
    m.meta('Kind regards,', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('Technical services and maintenance leader with 20+ years in 24/7 critical plant, capital projects and '
           'regulated manufacturing — authorised machine and electrical installer (LV/MV/HV) with a B.Tech in '
           'Technology Management & Mechanical Engineering, the marine engineering direction VELUX asks for. Five '
           'years owning availability, condition-based maintenance, criticality and spare parts on a plant that could '
           'not stop, with over 40 % lower energy consumption documented. Delivered 37 capital projects with 25 '
           'specialists through FAT/SAT, installation and commissioning with zero critical findings. Leads '
           'engineering and technician teams of 5 to 25 and builds the tools that make KPI and condition data '
           'usable — over 40 % productivity gain.', after=80)

    m.section('RELIABILITY, MAINTENANCE AND TECHNICAL DEVELOPMENT')
    for label, body in [
        ('Equipment availability and reliability',
         'Uptime, breakdowns and response times measured monthly on a 24/7 plant; repeat failures taken to root cause '
         'and the maintenance plan built from criticality instead of from the calendar.'),
        ('Maintenance strategy, criticality and spare parts',
         'Condition-based and preventive maintenance per asset group: failure modes identified, criticality ranked by '
         'consequence for production, intervals set from data, and run-to-failure chosen deliberately where it is '
         'cheaper; spare-parts stock, alternatives and lead times built on the same criticality.'),
        ('Technical projects and new equipment',
         '37 capital projects from specification to handover: acceptance criteria, FAT/SAT, IQ/OQ/PQ, installation '
         'and commissioning into live production, with documentation that follows the asset and zero critical '
         'findings at audit.'),
        ('Digitalisation and data',
         'SCADA, metering and CMMS data turned into KPI boards and automated reporting in Excel, Python and Claude; '
         'condition and alarm data used to predict and prioritise rather than to describe the past — over 40 % '
         'productivity gain in my own operation.'),
        ('Lean and continuous improvement',
         '5S, standard work, PDCA, A3 and value stream mapping as daily practice; improvement ideas from technicians '
         'taken to standard with an owner, a date and a number that must move.')]:
        m.bullet(label, body, after=25)

    m.models_table('TOOLS AND METHODS', ('Task', 'Tool and documented use'), [
        ('Maintenance management',
         'CMMS for work orders and history, criticality register, PM and condition-based plans, spare-parts lists; '
         'MTBF, MTTR and uptime as the monthly measures.'),
        ('Reliability engineering',
         'Root cause analysis (5-why, Ishikawa, A3), failure mode thinking, condition monitoring and alarm review; '
         'corrective actions closed with verification of effect.'),
        ('Project and commissioning',
         'Stage gates, acceptance criteria, FAT/SAT, IQ/OQ/PQ, as-built documentation and handover packages; '
         'contractor follow-up to deadline.'),
        ('Digitalisation',
         'Python and Claude for dashboards, automated reporting, calculation and checklists; SAP and Excel for '
         'orders, cost and asset data in daily use.'),
        ('Lean and operational excellence',
         '5S and visual management, standard work, PDCA, value stream mapping and Kaizen; daily boards and '
         'bottleneck analysis in a 24/7 operation.'),
        ('Leadership',
         'Daily boards, one-to-one and appraisal conversations, competence matrix and training plans, technician and '
         'apprentice development — decisions taken where the knowledge is.')])

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director',
         'ELOHVAC ApS · Copenhagen · May 2023–present',
         '5 electricians and 3 apprentices · full P&L · electrical installation, control and service',
         [('Technical service with a P&L',
           'Technical service to business customers with full P&L: fault finding, preventive maintenance, control and '
           'panels; documentation and KPI reporting automated with Python and Claude, over 40 % productivity gain.')]),
        ('Senior Commissioning Engineer / Project Manager, Electrical Systems',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · 2–10 million DKK each · GMP/FDA/EMA',
         [('New equipment into live production',
           'FAT/SAT, IQ/OQ/PQ, installation and commissioning of technical systems into operating production; '
           'acceptance criteria defined and tested and documentation handed over complete, with zero critical '
           'findings at audit; schedules, cost and risk reported monthly to management and client.')]),
        ('Project and Workshop Manager',
         'Ventek-Air · Copenhagen · Jan 2022–Nov 2022',
         '14 employees · 11 concurrent jobs · 2–10 million DKK per job',
         [('Capacity, priorities and standard work',
           'Daily boards, capacity and bottleneck analysis across eleven concurrent jobs; standardised working methods '
           'with a marked lift in delivery performance.')]),
        ('Operations and Maintenance Manager',
         'Lynetten under Biofos · Copenhagen · Aug 2017–Jan 2022',
         'Critical process plant in 24/7 operation · pumps, blowers, ventilation, transformers, switchgear, drives and SCADA',
         [('Availability, maintenance and energy',
           'Availability, breakdown and response time on the monthly board; condition-based maintenance and criticality '
           'across systems; spare-parts flow and 5S on stores; energy management on SCADA data with over 40 % lower '
           'consumption.')]),
        ('Electromechanical Technician / Production Supervisor',
         'ARJ Engineering · Tehran · Dec 2003–Mar 2010',
         '12 mechanics and technicians · machine workshop · industrial equipment',
         [('Machine reliability and people',
           'Fault diagnosis and repair of industrial electrical and mechanical equipment; root cause analysis and '
           'corrective action; shift planning, training and follow-up on output and quality targets for 12 '
           'technicians.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('EDUCATION AND AUTHORISATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering',
          'Maskinmesterskolen København · 2017–2022 · GPA 7.6/12 · marine engineering direction')
    m.edu('Authorised machine and electrical installer (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('Electrical and mechanical engineering', 'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Refrigeration, ventilation and safety training · STCW', 'Mercantec 2021 · Danish Maritime Authority 2021')

    m.section('LANGUAGES, PRACTICAL AND REFERENCES')
    m.para('Danish: native · English: fluent, written and spoken · Persian: native · Driver\'s licence B and car · '
           'Based in Måløv, Skjern around three hours away, weeks planned around the site · Available by agreement · '
           'SAP, Excel and Python daily · References on request.', after=70)

    m.models_table('WHAT THE ROLE ASKS FOR — MY EVIDENCE', ('Requirement', 'Evidence'), [
        ('Proven leadership of technical, engineering, maintenance or project teams',
         'Five years leading operations and maintenance in a 24/7 critical plant; 14 employees and 11 concurrent '
         'projects at Ventek-Air; 12 technicians at ARJ; 25 engineers and specialists across 37 capital projects at '
         'Novo Nordisk, an international GMP/FDA/EMA organisation.'),
        ('Technical qualification — engineering, production technology, marine engineering or similar',
         'B.Tech in Technology Management & Mechanical Engineering, the marine engineering direction, EQF 6; '
         'electrical authorisation LV/MV/HV; hands-on background as electrician and electromechanical technician.'),
        ('Lean principles, operational excellence and continuous improvement',
         '5S, standard work, PDCA, A3, value stream mapping and Kaizen applied daily in 24/7 operation and in project '
         'delivery; improvements taken to standard with an owner, a date and a measure.'),
        ('Experience driving technical development, automation, digitalisation or production improvement',
         'Condition-based maintenance and SCADA-based optimisation with over 40 % lower energy consumption; '
         'digitalisation of documentation, KPI and reporting flows with Python and Claude, over 40 % gain.'),
        ('High equipment availability, reliability and performance',
         'Availability, breakdowns and response times measured monthly on a plant that could not stop; criticality '
         'assessment, spare-parts strategy and root cause on repeat failures.'),
        ('Installing, integrating and optimising new machinery and technology',
         'FAT/SAT, IQ/OQ/PQ, installation and commissioning of technical systems into live production across 37 '
         'projects, with handover documentation complete and zero critical findings.'),
        ('Communicating across levels, building trust, fluent Danish and English',
         'Monthly reporting to management and client; daily cooperation with operations, quality, suppliers and '
         'contractors; Danish native and fluent English in written and spoken reporting to management, auditors and '
         'international suppliers.')])
    m.page_break()

    m.models_table('FIRST 90 DAYS — AVAILABILITY, STANDARDS AND THE BLUEPRINT', ('Period', 'What happens, and how it is measured'), [
        ('Week 1–2',
         'Walk the line with the maintenance technicians and the project engineers: where it stops, why it stopped '
         'last month, and what the shift does when it does. Read the maintenance plan, the breakdown history, the '
         'spare-parts list and the open technical projects. Meet production, quality and the international '
         'colleagues in the forums the role sits in.'),
        ('Day 30',
         'A one-page reliability picture: uptime and losses by asset group, the five failures that cost the most '
         'production, the state of the maintenance plan against criticality, and the three technical projects where '
         'a decision is missing.'),
        ('Day 60',
         'Maintenance strategy agreed per critical asset group with the team and production; spare-parts policy '
         'reviewed on criticality and lead time; competence matrix in place with the training gaps that matter; first '
         'digitalisation step chosen where the manual work is heaviest.'),
        ('Day 90',
         'A monthly reliability and KPI rhythm that the team owns — uptime, MTBF, MTTR, response time, maintenance '
         'backlog; the first improvement measured before and after; and the first draft of the Skjern standard that '
         'is meant to travel to France, written so a colleague who was not in the room can use it.')])

    m.section('A BLUEPRINT IS ONLY WORTH SOMETHING IF IT WORKS IN ANOTHER COUNTRY')
    m.para('Being the reference site is a different assignment from being a good site: a good site runs on the knowledge of '
           'its people, a reference site on standards its people can hand over. So every '
           'improvement in Skjern gets written the moment it works — installation and integration included: what the asset '
           'is, what the failure modes are, '
           'which maintenance intervals were chosen and why, which spare parts are held, which data is collected and '
           'who decides. That document is what a site in France actually receives — the machines they will buy '
           'anyway, but the thinking they cannot buy.', after=80)

    m.section('AVAILABILITY IS A DECISION MADE MONTHS BEFORE THE STOP')
    m.para('Nobody decides to have a breakdown. It is decided earlier, quietly, when a maintenance interval is left '
           'on the calendar because nobody questioned it, when a critical spare is not held because it has not been '
           'needed yet, or when an alarm is acknowledged and forgotten. So the work is to move those decisions to '
           'where they can be seen: a criticality list per asset group, a maintenance plan that reflects failure '
           'modes rather than a supplier\'s default, and a monthly review where the same three questions get asked '
           'of every repeat failure until the answer changes.', after=80)

    m.section('DIGITALISATION THAT ENDS AS A DASHBOARD NOBODY OPENS IS A COST')
    m.para('Condition monitoring, SCADA and CMMS already produce more data than a technical organisation can read, and '
           'analytics only helps if it ends in a decision. '
           'The value is not in collecting more; it is in turning what exists into a decision someone makes on a '
           'Tuesday: this bearing is trending, this line loses two hours a week to one alarm, this spare part has a lead '
           'time that makes the stock level wrong. I build those views myself in Python and Claude, which is why '
           'digitalisation in my teams has a before-and-after number attached instead of a project plan.', after=80)

    m.section('THE TEAM\'S COMPETENCE IS THE REAL SPARE PART')
    m.para('Every technical organisation has a machine that only one person can fix, and every one of those is a '
           'risk with a salary. The answer is not to document faster after they leave; it is a competence matrix that '
           'shows, area by area, who is signed off, who is in training and where the single points of failure are — '
           'and then a training plan built from the production plan rather than from enthusiasm. Project engineers and '
           'engineering specialists grow the '
           'same way: give them a real mandate on a real project, sit next to them at the difficult meeting, and let '
           'them own the result.', after=80)

    m.section('SAFETY AND RELIABILITY ARE THE SAME CONVERSATION')
    m.para('In a highly automated plant the dangerous moments are the interventions: the guard that has to be opened, the '
           'line that has to be jogged, the maintenance that has to happen while production is waiting. LOTO, '
           'permits, risk assessment and near-miss reporting are not paperwork around the work — they are the '
           'conditions that make it possible at the speed it has to happen. I have run that discipline in a '
           '24/7 plant and on construction sites, and I have never seen a team object to it when the standard was '
           'explained and applied consistently.', after=80)

    m.section('VELUX IS A COMPANY THAT MEASURES ITSELF IN DECADES')
    m.para('A family-owned company with foundations behind it, 20 production companies in 12 countries and a '
           'product built around daylight and fresh air, is not optimising for the next quarter. That suits how I '
           'work: build the asset register properly, make the maintenance plan honest, train the people who will still '
           'be there in ten years, and let the numbers improve because the foundation is right. Courage and mutual '
           'respect are useful values in a technical organisation — the courage to say the machine is not ready, and '
           'respect for the technician who says it first.', after=80)

    return m.save(path, title='Technical Services Manager — VELUX, Skjern',
                  subject='Equipment reliability, maintenance strategy, technical projects and digitalisation',
                  keywords='technical services manager, maintenance, reliability, availability, MTBF, MTTR, '
                           'condition-based maintenance, Lean, 5S, PDCA, digitalisation, FAT/SAT, IQ/OQ/PQ, '
                           'engineering, Skjern')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_VELUX_TechnicalServicesManager.docx')))
