# -*- coding: utf-8 -*-
"""Electrification Project Manager — DFDS (English posting -> en-GB document).

4 pages in master design: letter p1, CV p2-3, requirements matrix p4.
Contact: DFDS Talent Acquisition team (no name in posting) -> "Dear DFDS Talent Acquisition team,".
Location: DFDS HQ, Marmorvej 18, Copenhagen. No deadline ("apply as soon as possible").

STYLE (style_guard approved, 3/3 shifts vs #425 Vestforbraending):
  register     = Shore to grid (berth · cable · grid · transition · hands-on delivery)
  opening      = BA (the ship becomes a building: at berth with the cable on, a ferry
                 behaves like a building on the port's grid)
  structure    = From concept to handover (the project arc: concept · commissioning ·
                 handover)

BRUGERENS KORREKTION + permanent rule: all text humanised in letter AND CV.
No em dash. Varied rhythm, contractions (I'm, I've, I'd, it's), concrete before general.

BRUGERBEKRÆFTET 26.11.2026:
  - Shore power/charging: NO direct experience -> written openly as the development
    area (the posting itself asks for areas needing development).
  - Energy generation infrastructure: YES, direct experience -> written generally, no
    technology or employer pinned.
  - Travel 80-100 days Europe + Türkiye: covered by the standing travel confirmation
    (50-75% accepted for Saildrone; this is less).
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'DFDS · Electrification Project Manager'
BANNER_RESUME = 'Project delivery · power systems · commissioning · MV/HV'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('26 November 2026')
    m.meta('Decarbonisation · electrification infrastructure · project delivery')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Electrification Project Manager', bold=True, color='1A1A1A')
    m.para('Dear DFDS Talent Acquisition team,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- page 1
    lp('When a ferry ties up at the quay and the cable goes on, the engines fall quiet '
       'and the ship behaves, for the hours alongside, like a building on the port\'s '
       'grid. Shore power is where DFDS\' decarbonisation journey stops being a target '
       'and becomes switchgear, cables and schedules. That changeover is what I would '
       'like to help deliver as your Electrification Project Manager.')

    lp('DFDS was founded in 1866 and moves goods in trailers by ferry, road and rail, '
       'plus passengers on short sea and overnight ferry routes; a network with an '
       'annual revenue of DKK 30bn and 16,000 full-time employees. Right now the '
       'company is accelerating our transition towards lower-emission operations '
       'through shore power, charging infrastructure, and energy solutions across the '
       'ferry and logistics network, while safe and reliable operations stay the '
       'baseline. Turning those ambitions into reality takes projects, suppliers and '
       'commissioning dates. That is the part I know.')

    lp('Turning complex technical ambitions into reality is the work: this role sits '
       'where infrastructure, operations, technology and sustainability come '
       'together, and I know that junction. I have led projects from concept '
       'through commissioning and handover since 2003: 37 CAPEX projects at Novo '
       'Nordisk (DKK 2-10 million each, 25 specialists across engineering, procurement '
       'and operations, on a site that never stopped running), 11 simultaneous '
       'infrastructure projects with subcontractors at Ventek-Air, and my own company '
       'with full responsibility for scope, budgets, timelines, suppliers, and '
       'contractors. Acting as the link between technical specialists, operational '
       'teams, and project stakeholders is second nature by now.')

    lp('Electrical power systems are my foundation, including medium- and high-voltage '
       'applications (Danish authorisation as authorised electrical engineer, '
       'LV/MV/HV), and I have worked with energy generation infrastructure directly. '
       'Reviewing technical designs and making sure solutions are safe, scalable, and '
       'operationally robust is the part of project work I enjoy most. The development '
       'area is honest and concrete, since you ask: shore power and charging as a '
       'specialism. I have not owned those installations yet. Power systems, project '
       'execution and contractor management transfer directly; the domain itself I '
       'would learn on your terminals and sites, and fast.')

    lp('Denmark is home (Måløv), and 80-100 travel days per year across Europe and '
       'Türkiye suit me well; I have signed up for more before. Pragmatic, proactive '
       'and execution-oriented are your words, and I would put it this way: I take '
       'ownership of your projects, keep the plan when it holds and change it when it '
       'does not, and bringing multiple stakeholders together around a shared objective '
       'is how I work, fuss or no fuss. Navigating ambiguity and finding workable '
       'solutions is normal work in a fast-moving international environment, and I '
       'sleep fine in it.')

    lp('Be part of the movement is your line, and the movement needs projects that '
       'actually get built. This is a highly visible role and you want someone close '
       'to both the technology and the people delivering it; that is where I like to '
       'be. I would like to hear more about the Decarbonisation & '
       'Energy Security team and what is already in the pipeline. Development happens '
       'first and foremost through activities in the workplace, and the training and '
       'development opportunities that support your growth and ambitions are welcome '
       'on top of that.', after=44)

    m.para('Yours sincerely,', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- pages 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFILE')
    m.para('An authorised electrical engineer (LV/MV/HV) and project manager with 20+ '
           'years of infrastructure delivery behind me: concept, execution, '
           'commissioning and handover. Power systems, energy projects, contractors '
           'and suppliers across industrial, utility and building sites in Denmark and '
           'abroad. Used to being the link between the people who design and the '
           'people who run things.', after=32)

    m.section('EXPERIENCE')
    jobs = [
        ('CTO, AI department and authorised electrical engineer (electrical and ventilation)',
         'Data Power Consultant ApS · Copenhagen · 2024 – present (from Nov 2026 also '
         'ELOHVAC\'s electrical activities)',
         'AI department 4-10 people · electrical service and enterprise · 5 electricians + 3 apprentices',
         [('Leadership and development', 'Hiring, training and goals for the '
           'department\'s 4-10 people, and 5 electricians with 3 apprentices in the '
           'service business. Technical sparring every day, investment proposals with '
           'monthly follow-up.'),
          ('Tools and reporting', 'Workflows and reporting flows built in Python with '
           'AI support, so documentation and follow-up took less time. Data used '
           'actively to steer the business.')]),
        ('Owner / technical director / authorised electrical engineer',
         'ELOHVAC ApS · Copenhagen · May 2023 – Nov 2026 (company closed)',
         'Commercial clients · electrical, ventilation and air conditioning · enterprise · full P&L · service contracts',
         [('Projects and clients', 'Electrical installation projects and service for '
           'commercial clients: switchgear, controls and preventive maintenance on '
           'buildings in use, plus emergency callouts when something stopped.'),
          ('Commercial responsibility', 'Full budget and P&L responsibility. Tenders, '
           'pricing and procurement, and service contracts with targets for response '
           'time, quality and delivery; contracts were renewed because clients got '
           'what they were promised.'),
          ('People', '5 electricians and 3 apprentices with structured training and '
           'technical sparring. Consistent standards; zero critical deviations across '
           'the service contracts.')]),
        ('Senior commissioning engineer / project manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022 – Jul 2024',
         '37 CAPEX projects, DKK 2-10 million · 25 specialists · GMP/FDA/EMA',
         [('Projects and delivery', '37 projects managed on scope, time and budget '
           '(DKK 2-10 million each) with 25 specialists across engineering, '
           'procurement and operations. Monthly reporting to management and client; '
           'zero critical findings at handover. SAP ERP and PRINCE2 as backbone.'),
          ('Commissioning and energy', 'FAT/SAT and qualification protocols (IQ/OQ/PQ) '
           'in GMP environments, on plants that kept running. A PDCA cycle that cut '
           'energy costs by 40%, measured.')]),
        ('Project and workshop manager',
         'Ventek-Air · Copenhagen · Jan 2022 – Nov 2022',
         '11 simultaneous ventilation projects · 14 staff · subcontractors',
         [('Coordination', '11 simultaneous infrastructure projects for public and '
           'private clients. Tenders and contracts, subcontractor coordination and '
           'safety documentation, followed through to handover.')]),
        ('Maintenance and operations manager / workshop technician',
         'Biofos (Lynetten) · Copenhagen · Aug 2017 – Jan 2022',
         '24/7 operations · SCADA, PLC, HV switchgear · shift work',
         [('Operations', 'Operation, monitoring and maintenance of pumps, treatment '
           'plant, HVAC, HV switchgear, SCADA and PLC around the clock. Fault finding '
           'on site, 5S and Standard Work in the workshop.'),
          ('Safety and standards', 'Shift and on-call work with LOTO, safety procedures '
           'and near-miss routines as habits. Technical level kept up through training '
           'and shared procedures.')]),
        ('Electromechanical technician / production manager',
         'ARJ Engineering · Tehran · Dec 2003 – Mar 2010',
         '12 mechanics and technicians · machine workshop · production line',
         [('The basics', 'Leading 12 mechanics and technicians: shift planning, '
           'materials and targets. Fault finding on industrial equipment, root cause '
           'and corrective actions.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('EDUCATION AND CERTIFICATES')
    m.edu('B.Tech (EQF6), Technology Management and Mechanical Engineering',
          'Copenhagen School of Marine Engineering & Technology Management · 2017-2022 · GPA 7.6/12')
    m.edu('Authorised electrical engineer (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('Electrical and mechanical design, electrical engineering (EQF6)',
          'Tehran Technical University · 2000-2003')
    m.edu('PRINCE2, certified project manager', 'AXELOS / PeopleCert')
    m.edu('Refrigeration and air conditioning (AMU)',
          'Mercantec · 2021 · STCW 2021-2023, Danish Maritime Authority')

    m.section('COMPETENCIES')
    m.bullet('Project delivery', 'Concept through commissioning and handover: scope, '
             'budgets, timelines, suppliers and contractors on projects from DKK 2 '
             'million to 10 million and up.', after=10)
    m.bullet('Power systems', 'Electrical power systems including medium- and '
             'high-voltage applications. Danish authorisation as authorised '
             'electrical engineer (LV/MV/HV), 2023.', after=10)
    m.bullet('Commissioning and handover', 'FAT/SAT, IQ/OQ/PQ and qualification '
             'protocols in GMP environments; clean handovers into operations with '
             'zero critical findings at Novo Nordisk.', after=10)
    m.bullet('Contractors and suppliers', 'Tenders, contracts and daily coordination '
             'of subcontractors (Ventek-Air, ELOHVAC); supplier management with '
             'negotiated agreements and follow-up.', after=10)
    m.bullet('Energy', 'Energy generation infrastructure worked with directly, and '
             'energy optimisation with measurable results (40% lower energy cost in '
             'a PDCA cycle at Novo Nordisk).', after=10)
    m.bullet('Stakeholders and communication', 'Technical specialists and senior '
             'business stakeholders, in Danish and English, across functions and '
             'countries.', after=10)

    m.section('THE FIRST 90 DAYS')
    m.para('The plan follows the project arc itself: learn the network, drive the '
           'projects, hand over cleanly.', after=8)
    m.bullet('Day 1-30 · The network', 'Terminals, the project pipeline and the people '
             'behind them learned first: site visits, current shore power and charging '
             'projects, and where Decarbonisation & Energy Security needs project '
             'muscle. Goal: I know the network and the priorities, and the team knows '
             'me.', after=10)
    m.bullet('Day 31-60 · The projects', 'My projects driven from concept into '
             'execution: scope, budgets and timelines locked, suppliers and '
             'contractors aligned, technical reviews done with the specialists. Goal: '
             'every project on my desk has a plan the operations teams recognise.',
             after=10)
    m.bullet('Day 61-90 · The handover', 'First implementations supported into '
             'day-to-day use with the operational teams, and the lessons written down '
             'while they are fresh. Goal: one clean handover, and a short list of '
             'improvements nobody has had time to write down yet.', after=10)

    m.section('LANGUAGES, TOOLS AND PRACTICALITIES')
    m.para('Danish (native) · English (professional) · Persian (native). SAP ERP, '
           'SCADA, PLC, Power BI, Python and AI tools. PRINCE2. Driving licence B '
           '(manual). Based in Måløv, Denmark. Available at short notice. 80-100 '
           'travel days per year across Europe and Türkiye are fine.', after=32)

    # ------------------------------------------------------------- page 4
    m.page_break()
    m.models_table('Electrification project management · requirements and evidence',
                   ('Requirement in the posting', 'Evidence'),
                   [
        ('Hands-on project manager for landside electrification infrastructure',
         'Hands-on project management since 2003: from my own company (ELOHVAC, full '
         'P&L 2023-2026) to 37 CAPEX projects at Novo Nordisk (2022-2024) and 11 '
         'simultaneous infrastructure projects at Ventek-Air (2022). Planning, site, '
         'paperwork and follow-through.'),
        ('Execution of shorepower installations, charging and other electrical and '
         'energy generation infrastructure',
         'Shore power and charging as a specialism is my development area, and I say '
         'so openly. The rest is direct: electrical infrastructure executed in '
         'buildings and industry since 2003, and energy generation infrastructure '
         'worked with directly. The domain I would learn on your sites; the execution '
         'I already know.'),
        ('Leading electrification and energy infrastructure projects from concept '
         'through commissioning and handover',
         'Concept to handover delivered repeatedly: 37 projects from scoping to '
         'handover at Novo Nordisk (2022-2024) with FAT/SAT and qualification '
         'protocols, and enterprise projects taken from first survey to signed '
         'handover in ELOHVAC (2023-2026).'),
        ('Managing project scope, budgets, timelines, suppliers, and contractors',
         'Scope, budgets and timelines managed as project manager (Novo, 37 projects, '
         'DKK 2-10 million each) and as business owner (ELOHVAC, full P&L). Suppliers '
         'and contractors handled through tenders, contracts and daily coordination '
         '(Ventek-Air, 11 projects with subcontractors).'),
        ('Acting as the link between technical specialists, operational teams, and '
         'project stakeholders',
         'The link role is my constant: 25 specialists across engineering, procurement '
         'and operations at Novo Nordisk (2022-2024), clients and subcontractors at '
         'Ventek and ELOHVAC, and shift operations at Biofos (2017-2022). I translate '
         'between the people who design and the people who run.'),
        ('Supporting the development of shore power, charging, and other electrical '
         'infrastructure solutions',
         'Solution development for electrical infrastructure: service concepts and '
         'new technical solutions sold and delivered in ELOHVAC (2023-2026), and '
         'electrical systems developed with engineering at Novo Nordisk. Shore power '
         'and charging I would develop together with your specialists, honestly new '
         'to me.'),
        ('Reviewing technical designs and ensuring solutions are safe, scalable, and '
         'operationally robust',
         'Design review is daily work for an authorised electrical engineer: '
         'installations, switchgear and controls reviewed before and during execution '
         '(ELOHVAC 2023-2026, Ventek 2022), and protocols reviewed line by line in '
         'GMP projects (Novo). Safe, scalable and operationally robust is the '
         'standard I hold.'),
        ('Supporting operational teams during implementation and transition into '
         'day-to-day use',
         'Implementation support for operations: commissioning on running process '
         'plants (Novo 2022-2024), service transitions with response-time targets '
         '(ELOHVAC), and 24/7 operations myself at Biofos (2017-2022). Anyone who has '
         'worked nights knows the price of a bad handover.'),
        ('At least 5 years leading or participating in large-scale infrastructure, '
         'electrification, energy or industrial projects in complex operational '
         'environments',
         '20+ years in industrial, energy and infrastructure projects: 12 mechanics '
         'and production equipment at ARJ (2003-2010), utilities around the clock at '
         'Biofos (2017-2022), 11 projects at Ventek (2022), 37 CAPEX at Novo '
         '(2022-2024), own enterprise 2023-2026.'),
        ('A strong understanding of electrical power systems, including medium- and '
         'high-voltage applications',
         'Electrical power systems are the backbone of my training and work: '
         'electrical engineering at EQF6 level (2000-2003) and Danish authorisation as '
         'authorised electrical engineer (LV/MV/HV, 2023). HV switchgear operated and '
         'maintained at Biofos (2017-2022).'),
        ('The ability to manage contractors, suppliers and multidisciplinary project '
         'teams while maintaining momentum and alignment',
         'Teams and suppliers managed at every level: 12 mechanics (ARJ), 5 '
         'electricians and 3 apprentices (ELOHVAC), 25 specialists across disciplines '
         '(Novo), 14 staff and subcontractors (Ventek). Momentum kept through clear '
         'scopes, short meetings and follow-up.'),
        ('Confidence in engaging with both technical specialists and senior business '
         'stakeholders',
         'Both audiences handled weekly: technical depth with engineers and '
         'electricians on site, and monthly reporting to management and clients (Novo '
         '2022-2024, investment proposals at Data Power 2024-2026). Confidence in the '
         'room comes from knowing the numbers.'),
        ('Strong communication skills and a collaborative approach that enables you to '
         'build trust across functions, cultures and geographies',
         'Communication across cultures is my working life since 2003: Danish and English '
         'daily, teams with many nationalities at Novo and Ventek (2022-2024), and '
         'projects in Denmark and Iran. Trust built by doing what I said, especially '
         'when the news was bad.'),
        ('The ability to balance technical requirements, commercial considerations and '
         'operational realities when making decisions',
         'The balance is the job: technical quality against budget in 37 CAPEX '
         'decisions (Novo), price and performance in tenders (Ventek, ELOHVAC), and '
         'uptime against maintenance windows as operations manager (Biofos).'),
        ('Experience from energy, utilities, transportation, maritime, ports, '
         'terminals or other infrastructure-intensive industries',
         'Energy and utilities: process plants (Novo 2022-2024), utility-scale '
         'operations at Biofos (2017-2022) and energy optimisation with 40% lower '
         'energy cost as result. Maritime: STCW certification (2021-2023) and '
         'practical seamanship from the water side. Ports and terminals I would bring '
         'fresh eyes to.'),
        ('Pragmatic, proactive and execution-oriented; solving problems, navigating '
         'ambiguity and finding workable solutions',
         'Execution first: projects carried through from survey to handover since '
         '2003, including three years with my own company on the line (2023-2026). '
         'Ambiguity handled from the inside: industrial equipment without '
         'documentation (ARJ 2003-2010), commissioning on live plants (Novo), and a '
         'service business where the phone decides the day (ELOHVAC).'),
        ('Take ownership of your projects, stay organised even when managing multiple '
         'priorities, and have the resilience and drive needed in a fast-moving '
         'international environment',
         'Multiple priorities without dropping balls: 11 simultaneous projects '
         '(Ventek 2022), 37 projects across two sites (Novo 2022-2024), and a company '
         'with daily operations and projects at once (2023-2026). International by '
         'default: Danish, English and Persian.'),
        ('Approximately 80-100 travel days per year across Europe and Türkiye; the '
         'role is based in Denmark',
         'Based in Måløv, Denmark, with driving licence B (manual). Travel across '
         'Europe and Türkiye at 80-100 days per year is fine: I have committed to '
         'higher travel before and delivered. Short notice is fine for a start date.'),
        ('Decarbonisation and energy security strategy; net-zero future',
         'Decarbonisation work in practice: energy optimisation with a measured 40% '
         'reduction (Novo 2022-2024), energy generation infrastructure worked with '
         'directly, and the daily engineering that makes emissions targets real rather '
         'than reported, supporting climate ambitions, regulatory compliance and '
         'operational performance at once.'),
                   ], widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo — Electrification Project Manager, DFDS')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_DFDS_ElectrificationProjectManager.docx')
    build(out)
    print(out)
