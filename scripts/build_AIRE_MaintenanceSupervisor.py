# -*- coding: utf-8 -*-
"""AIRE Copenhagen — Hands-on Maintenance Supervisor.

English posting → English deliverable: letter page 1, CV pages 2–3, 90-day plan + sections page 4.
Policy: master/README.md — extreme confidence, no caveats.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Maintenance Supervisor · Hands-on leadership of plant, people and preventive maintenance'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('6 November 2026')
    m.meta('AIRE Copenhagen · Hands-on Maintenance Supervisor')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Hands-on Maintenance Supervisor, AIRE Copenhagen', bold=True, color='1A1A1A')
    m.para('For the attention of Jan Hoffmann, Senior Recruitment Specialist, Career', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('A guest at AIRE never sees the plant room. They notice the water, the temperature and the air — and if '
           'any one of those is wrong, they notice nothing else. That is the standard the maintenance team is '
           'measured against, and it is a standard built out of boring things done on time: the dosing checked '
           'before the first guest, the filter cleaned before it is due, the pump that was replaced in February '
           'instead of failing in July. I have spent twenty years doing exactly that, half of it with a spanner in '
           'my hand.', after=80)

    m.para('**I would run the maintenance of a site like AIRE on four fixed things.** First **the plant room decides '
           'the guest experience**: pool chemistry, water temperature and air handling are measured on a schedule '
           'and logged, so the first sign of drift is a number on a sheet — not a complaint at reception. Second '
           '**preventive maintenance is a calendar, not an intention**: every asset gets a task, a frequency and a '
           'name, and the plan survives a busy weekend because it is planned around the weekend rather than '
           'apologised for afterwards. Third **a supervisor works alongside the team**: four technicians need '
           'clear priorities at the start of the shift, feedback on the spot and a supervisor who takes the '
           'awkward job rather than handing it out. Fourth **routines should improve because somebody owns them**: '
           'the same failure twice is a system problem, and the fix is usually a checklist, a stock level or a '
           'spare part — not more effort.', after=80)

    m.para('I am a practical engineer, not a paper one. I trained as an **electromekaniker**, I am a '
           '**state-authorised marine engineer (LV/MV/HV)** with a **B.Tech in technology management and '
           'mechanical engineering**, and since 2023 I have run my own technical company, **ELOHVAC**, with '
           '**five electricians and three apprentices** and full P&L responsibility. That means I have done the '
           'fault-finding myself: panels, motors, pumps, valves, controls and the low-voltage work that has to be '
           'done properly the first time.', after=80)

    m.para('Leading a small technical team is what I have done for most of my career. At **ARJ Engineering** I was '
           'production team leader for **twelve mechanics and technicians** in a machine shop — shift planning, '
           'onboarding, training and follow-up on the individual. At **Ventek-Air** I led **fourteen employees and '
           'eleven parallel projects** with a daily stand-up and priorities that were re-set the same day when a '
           'machine or a person dropped out. I have also stood in for the person above me, which is a bigger part '
           'of a supervisor role than the job description usually admits.', after=80)

    m.para('Water and 24/7 plant is where I would bring something specific. For five years I was maintenance and '
           'operations manager at **Lynetten (Biofos)**, a critical process plant running around the clock: '
           'pumps, blowers, dosing, filtration, valves, transformers, switchgear and SCADA, with condition-based '
           'maintenance, a criticality list, spare parts, external fitters and an **on-call rota** that I both '
           'planned and worked. Standards, 5S and PDCA on the workshop and stores; measured results, including '
           '**more than 40 % lower energy consumption** documented on the plant.', after=80)

    m.para('What attracts me to AIRE is the combination of a guest-facing standard and a technical site that has to '
           'be kept quiet: a close-knit team of around thirty, direct contact with management, a site in the old '
           'Carlsberg brewery buildings where the building itself is part of the product — masonry, heat, humidity, '
           'and a plant that has to work quietly inside it — and maintenance where the quality is felt by guests '
           'in the water rather than read in a report. I have worked in '
           'environments where a stop was measured in hours; here the measure is whether a guest notices anything '
           'at all. I am also looking for a place to grow as the site and the company grow: career growth inside an '
           'international group is worth more to me than a title.', after=80)

    m.para('I am applying for a supervisor role on purpose. I have run a company and carried a manager title; what '
           'I want now is a site, a team of four and a standard that is judged by guests every single day. Close '
           'enough to the work that I can put my hands on it, and steady enough that the routines can actually be '
           'built and kept. The title matters less to me than the size of the job.', after=80)

    m.para('Practical: I live in Måløv, about twenty-five minutes from central Copenhagen, with a **driving licence '
           'and my own car**, so I can be on site promptly for an on-call issue. I am flexible with the **weekend '
           'shift every other weekend**, with evenings, public holidays and holiday cover, and I am comfortable '
           'with the on-call arrangement — I have carried a phone for a plant before. I communicate confidently in '
           '**English** and Danish, and I can start by agreement. I would like to hear how the preventive plan is '
           'built today and where the team loses most of its time — that is where I would begin.', after=70)
    m.meta('Kind regards', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('Hands-on maintenance supervisor with 20+ years in technical operations, plant and workshops — '
           'state-authorised marine engineer (LV/MV/HV), B.Tech in technology management and mechanical '
           'engineering, and a trained electromekaniker. Five years of 24/7 plant maintenance with pumps, dosing, '
           'filtration, ventilation, switchgear and SCADA, an on-call rota and documented results including over '
           '40 % lower energy. Has led twelve mechanics, fourteen employees and, since 2023, an electrical company '
           'with five electricians and three apprentices and full P&L — working in the tool belt alongside the '
           'team. Practical, precise, and used to an invisible technical site.', after=80)

    m.section('PLANT, MAINTENANCE AND PEOPLE')
    for label, body in [
        ('General maintenance, hands-on',
         'Electrical, mechanical, plumbing, ventilation and building systems handled first-hand: fault-finding on '
         'panels, motors, pumps, valves and controls, plus the low-voltage work that has to be done right the '
         'first time.'),
        ('Preventive maintenance',
         'Task, frequency and owner for every asset; condition-based maintenance and a criticality list, so the '
         'work that prevents a failure is planned before the failure sets the agenda.'),
        ('Water and pool systems',
         'Five years with pumps, dosing, filtration, valves and water quality on a 24/7 process plant: measurement '
         'on a schedule, logging, corrective dosing and the discipline of never letting a reading slide.'),
        ('Leading a small team',
         'Twelve mechanics in a machine shop, fourteen employees at Ventek-Air and eight in my own company — '
         'priorities at the start of the shift, onboarding, training, development, feedback and cover when someone is away.'),
        ('On-call and emergencies',
         'Planned and worked an on-call rota on a critical plant: first response to an urgent issue, making the site safe, '
         'calling the right fitter or supplier and writing it down afterwards.'),
        ('Stock, spares and routines',
         'Criticality-based stock of spares, materials and consumables, 5S in the workshop and stores, and routines that get '
         'improved because the same failure twice is treated as a system problem.')]:
        m.bullet(label, body, after=25)

    m.models_table('TOOLS, SYSTEMS AND METHODS', ('Area', 'Documented use'), [
        ('Plant and assets',
         'Asset register with criticality, maintenance plans per unit, spare-parts needs and documentation of '
         'every service carried out.'),
        ('Water and air',
         'Measurement and logging of water quality, temperature and flow; ventilation and air handling from '
         'project work and service; corrective dosing and follow-up.'),
        ('Electrical and controls',
         'LV/MV/HV authorisation, panels and switchgear, motors and drives, sensors and SCADA; fault-finding from '
         'the symptom to the component.'),
        ('Planning, data and follow-up',
         'Daily and weekly plans, stand-up meetings and priorities re-set the same day; Excel, Power Query and '
         'Python for checklists, logs and dashboards with before-and-after results.'),
        ('Safety and compliance',
         'Health and safety instructions, risk assessment, permits and documentation; 5S and standard work on a '
         '24/7 plant with authority requirements.')])

    m.section('PROFESSIONAL EXPERIENCE')
    jobs = [
        ('Owner / Technical Director',
         'ELOHVAC ApS · Copenhagen · May 2023–present',
         '5 electricians and 3 apprentices · full P&L · electrical service and contracting',
         [('Running the work and doing it',
           'Sales, quotations, purchasing, invoicing and payment follow-up with full P&L; daily operations with '
           'customers, employees and suppliers — and in the tool belt when the job has to be delivered; own '
           'Python/Claude tools for checklists and KPIs with over 40 % productivity gain.')]),
        ('Senior Commissioning Engineer / Project Manager, Electrical Systems',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · DKK 2–10 m per project · GMP/FDA/EMA',
         [('Technical acceptance and documentation',
           'Specification, factory and site acceptance testing (FAT/SAT) and IQ/OQ/PQ for new production '
           'equipment; progress, cost and risk reported monthly; zero critical findings at audited handover.')]),
        ('Project and Workshop Manager',
         'Ventek-Air · Copenhagen · Jan 2022–Nov 2022',
         '14 employees · 11 parallel projects · DKK 2–10 m per assignment',
         [('Ventilation, coordination and short horizons',
           'Daily stand-ups, capacity and bottleneck analysis and priorities re-set the same day when a machine '
           'or a person dropped out; subcontractors and handover packages driven to date.')]),
        ('Maintenance and Operations Manager',
         'Lynetten (Biofos) · Copenhagen · Aug 2017–Jan 2022',
         'Critical 24/7 process plant · pumps, blowers, dosing, filtration, ventilation, transformers, switchgear and SCADA',
         [('Plant, water, fitters and on-call',
           'Maintenance, repair and spare parts coordinated with mechanics and external fitters around the clock; '
           'condition-based maintenance and criticality; 5S and standard work in workshop and stores; on-call '
           'rota planned and worked; energy management with over 40 % lower consumption documented.')]),
        ('Electromechanic / Production Team Leader',
         'ARJ Engineering · Tehran · Dec 2003–Mar 2010',
         '12 mechanics and technicians · machine shop · industrial equipment',
         [('Workshop, faults and shift cover',
           'Preparation, repair and fault-finding on industrial equipment with turning, milling, welding and '
           'assembly; shift planning, onboarding and follow-up on targets for 12 technicians.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('EDUCATION AND AUTHORISATION')
    m.edu('B.Tech, Technology Management and Mechanical Engineering',
          'Copenhagen School of Marine and Technical Engineering · 2017–2022 · GPA 7.6/12')
    m.edu('State-authorised Marine Engineer (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('Electrical and Mechanical Construction, Electrical Engineering',
          'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Refrigeration and Ventilation Technology · STCW', 'Mercantec 2021 · Danish Maritime Authority 2021')

    m.section('LANGUAGES, PRACTICALITIES AND REFERENCES')
    m.para('English: professional, spoken and written · Danish: native · Persian: native · Driving licence B and own '
           'car · Måløv, about 25 minutes from central Copenhagen, able to reach the site promptly · Flexible with '
           'weekends, evenings, public holidays and holiday cover · On-call experience from a 24/7 plant · Available '
           'by agreement · References on request.', after=70)

    m.models_table('WHAT THEY ASK FOR — WHAT I HAVE', ('Requirement', 'Evidence'), [
        ('Practical, very hands-on, broad technical skills',
         'Trained electromekaniker, authorised marine engineer LV/MV/HV and owner of an electrical company where '
         'I do the fault-finding myself; electrical, mechanical, plumbing and ventilation work handled first-hand, '
         'and I work independently and take ownership of the site.'),
        ('Around two years of maintenance experience',
         'Five years as maintenance and operations manager on a critical 24/7 plant, plus twenty years of technical '
         'operations, workshops and service in total.'),
        ('At least one year leading or coordinating a small team',
         'Twelve mechanics and technicians in a machine shop, fourteen employees at Ventek-Air and eight in my own '
         'company — onboarding, training, feedback and daily priorities.'),
        ('Electrical work, plumbing, building maintenance or similar',
         'Electrical work with authorisation at LV/MV/HV; plumbing and pipe systems on pumps, valves, dosing and '
         'filtration; building and installation work in electrical contracting and ventilation projects.'),
        ('Pool or water treatment experience',
         'Five years measuring and correcting water quality on a process plant: dosing, filtration, sampling, '
         'logging and the discipline of catching a drift before it becomes a problem.'),
        ('Preventive maintenance to procedures and H&S requirements',
         'Maintenance plans per asset, condition-based maintenance and criticality, 5S and standard work, and '
         'health and safety instructions with risk assessment and documentation.'),
        ('Coordinating with other departments and stock control',
         'Maintenance needs agreed with production, projects and suppliers; criticality-based stock of spares and '
         'consumables kept in the workshop and stores.'),
        ('Improving maintenance routines over time',
         'Routines rebuilt and measured: over 40 % productivity gain from checklists and automated follow-up, and '
         'energy consumption cut by more than 40 % on a 24/7 plant.'),
        ('Focused, detail-oriented and clear with guests and colleagues',
         'Fault-finding from symptom to component with attention to detail and the documentation to match; clear '
         'communication and handovers in Danish and English, to technicians, managers and guests.'),
        ('Comfortable with on-call and reaching the site promptly',
         'On-call rota planned and worked at Lynetten; lives in Måløv about 25 minutes from central Copenhagen, '
         'with a driving licence and own car.')])
    m.page_break()

    m.models_table('THE FIRST 90 DAYS — THE PLANT, THE TEAM AND THE ROUTINES',
                   ('Period', 'What happens, and how it is measured'), [
        ('Weeks 1–2',
         'Walk the site with the Facilities Manager and the four technicians: plant room, pool and water systems, '
         'air handling, electrical rooms and stores. Read the last twelve months of maintenance records, faults '
         'and supplier invoices to see what actually breaks and how often.'),
        ('Day 30',
         'A maintenance plan per asset with task, frequency and owner; the daily priority routine agreed with the '
         'team; water readings and temperatures logged on a fixed schedule; stock list for the parts that stop '
         'the site, checked against the shelf.'),
        ('Day 60',
         'Preventive work scheduled around weekends and holidays instead of colliding with them; clear ownership of '
         'each area among the four technicians; the two most frequent failures addressed with a checklist or a '
         'spare part rather than more effort.'),
        ('Day 90',
         'Reactive work and downtime measured month by month, with reporting to the Facilities Manager; a simple '
         'routine for suppliers and external fitters; and a short list of improvements with cost and effect, so the '
         'next quarter is chosen rather than '
         'discovered.')])

    m.section('THE GUEST NEVER SEES THE PLANT ROOM — THAT IS THE JOB')
    m.para('Everything that makes a bath house work is hidden behind a door that guests never open: pumps, filters, '
           'dosing, heat exchangers, air handling, drains and the electrical boards that feed them. When it works, '
           'nobody notices it, and when it fails, everybody notices within minutes. A maintenance supervisor is '
           'therefore judged on the days nothing happens — and those days are made in advance, with a plan and a '
           'set of readings rather than luck.', after=80)

    m.section('WATER IS THE ONE SYSTEM YOU CANNOT ARGUE WITH')
    m.para('Water quality is chemistry and time: dosing, filtration, circulation, cleaning and disinfection, and '
           'temperature, checked on a schedule and written down. A reading that is slightly off is not a problem yet — it is a warning, and '
           'the job is to act on the warning rather than on the complaint that follows it. I have spent five years '
           'measuring, logging and correcting water on a plant that ran around the clock, and I know that the '
           'difference between a stable pool and a recurring problem is almost always the frequency of the checks.',
           after=80)

    m.section('A PREVENTIVE PLAN IS A CALENDAR, NOT AN INTENTION')
    m.para('Everyone agrees that preventive maintenance matters, and it is still the first thing that gets moved '
           'when a weekend is busy. The only way it survives is if it is in the calendar with a name against it, '
           'planned around the busy periods rather than apologised for afterwards — and if the completion is '
           'visible, so the plan is a fact rather than a document. That is how I ran maintenance on a plant where '
           'a stop cost far more than the service would have.', after=80)

    m.section('FOUR TECHNICIANS AND ONE ON-CALL PHONE — THE ROTA IS THE JOB')
    m.para('A small team covering a site that is open all year works only if the rota is fair, known in advance and '
           'actually staffed: every other weekend, early and late shifts, holidays and the phone at night. It is '
           'also the part of the job where a supervisor earns trust fastest — by taking the unpopular shift, by '
           'being reachable, and by making sure a person who covered last weekend is not the one covering the next.',
           after=80)

    m.section('STOCK AND SPARES: THE CHEAPEST FIX IS THE ONE ON THE SHELF')
    m.para('Most emergency call-outs end with a part somebody had to fetch. A short, criticality-based stock list '
           'for the pumps, valves, seals, sensors and fuses that stop the site is cheaper than the downtime and the '
           'overtime it prevents. I have built that list before, and I keep it honest by reviewing what was '
           'actually used rather than what somebody thought would be needed.', after=80)

    m.section('A SUPERVISOR SHOULD BE THE FIRST ONE IN THE PLANT ROOM')
    m.para('The technicians decide whether the supervisor is credible in the first month, and they decide it on '
           'whether he takes the unpleasant job. I have cleaned strainers, traced faults in a plant room at three '
           'in the morning and carried the tools; that is not team leadership theory, it is the reason people '
           'accept a decision when the shift gets difficult. My job is to make the team able to do the work '
           'without me, and then to be there anyway.', after=80)

    m.section('I HAVE CARRIED THE PHONE BEFORE')
    m.para('At Lynetten I planned and worked the on-call rota for a critical plant: first response, making the '
           'situation safe, calling the right fitter or supplier and writing it down afterwards so the same night '
           'did not happen twice. That experience is why I am comfortable with the flexibility this role asks for '
           '— weekends, late shifts, holidays and the phone — and why I would rather build the routine that '
           'prevents the call than be praised for answering it.', after=80)

    return m.save(path, title='Hands-on Maintenance Supervisor — AIRE Copenhagen',
                  subject='Hands-on maintenance leadership: plant, water systems, preventive maintenance and a small technical team',
                  keywords='maintenance supervisor, hands-on maintenance, preventive maintenance, pool, water '
                           'treatment, electrical, plumbing, facilities, on-call, stock control, team leadership')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_AIRE_MaintenanceSupervisor.docx')))
