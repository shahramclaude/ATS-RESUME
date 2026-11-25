# -*- coding: utf-8 -*-
"""Head Of Tools Coordination & Maintenance — Ørsted Wind Power A/S, Esbjerg (R? / engelsk opslag).

Engelsk opslag -> engelsk dokument, 4 sider i masterdesign: letter p1, CV p2-3, kravmatrix p4.
Deadline 17. december 2026. Intet kontaktnavn i opslaget; brevet er adresseret til hiring team.

STILVALG (style_guard godkendt, 3/3 skift mod #416):
  register     = Care, clarity and accountability (care · clarity · accountability · wellbeing ·
                 collaboration · dependable) — opslagets egne ledelsesord
  åbningsgreb  = AR (mobiliseringsøjeblikket: det øjeblik hvor en kampagne skal bruge værktøjet,
                 og det skal være der, certificeret og klart)
  struktur     = Tool lifecycle (warehouse · maintenance · re-certification · repair · transport)
                 — værktøjets livscyklus som dokumentets rygrad

BRUGERENS KORREKTION + permanent regel: alt tekst humaniseret, menneskeskrevet i brev OG CV.
BANNED: "the right candidate" citeres aldrig. Ingen em dash.

EVIDENSGRÆNSER: ingen offshore wind eller oil and gas på cv'et (skrives ærligt; opslaget inviterer
"transferable skills"). Container solutions og re-certification af offshore-værktøj = ærligt nyt.
Bekræftet (bruger 25.11.2026): kan bo og arbejde i Esbjerg-området.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Esbjerg · Head of Tools Coordination & Maintenance'
BANNER_RESUME = 'Tools, warehouse and maintenance leadership · Esbjerg'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('25 November 2026')
    m.meta('Ørsted Wind Power A/S · Head of Tools Coordination & Maintenance')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Head of Tools Coordination & Maintenance', bold=True, color='1A1A1A')
    m.para('Dear hiring team at Ørsted,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('The moment this role is measured by comes when a campaign mobilises. The specialists '
       'travel out, and the specialized tools and equipment are ready when projects and '
       'campaigns need them: safe, complete, compliant, and ready-to-use. That is the '
       'standard in your posting, and it is a warehouse-and-maintenance standard before it is '
       'anything else. I have spent my career getting equipment ready for the moment someone '
       'else needs it: 37 commissioning projects at Novo Nordisk, service vans that had to '
       'roll every morning, and a workshop where nothing could be missing on Monday.')

    lp('Inside Technical Management, the role runs along one line: priorities across warehouse operations, maintenance, '
       're-certification, repair, and transport. I would read the job in that order. The '
       "posting's team manages specialist tools, equipment, container solutions, and warehouse "
       'activities for Special Tasks & Inspections, and the tools management system is where '
       'the truth about the equipment lives. Accurate inventory, documentation, maintenance '
       'history, and re-certification records matter more than they sound, because the project '
       'that borrows a tool inherits whatever the record says about it.')

    lp('Your posting combines people leadership with hands-on operational involvement, and '
       'that combination is what I know. Leading the team\'s daily work with clear priorities '
       'and task allocation, balancing operational demand, competence, and safety, is the same '
       'job I have done with 5 electricians and 3 apprentices, a 14-person contracting team, '
       '25 specialists across engineering and operations, and 12 mechanics in a workshop. I '
       'lead with care, clarity, and accountability: 1:1s and regular feedback, coaching and '
       'training follow-up, and objectives people can check themselves against. On the '
       'relationship side I have built trusted relationships with suppliers, external service '
       'providers and warehouse organisations at both ends, the contract and the delivery.')

    lp('Two points where I will be honest, since your posting invites transferable skills. '
       'Offshore wind and oil and gas are not on my record, and I will not pretend otherwise. '
       'My industrial background is process and pharma under GMP/FDA/EMA, 24/7 utility '
       'operations, and electrical contracting: warehouse operations, tooling and maintenance '
       'transfer directly, and the offshore context I will learn. And re-certification of '
       'specialist offshore tools has its own rulebook; what I bring is the habit of '
       'maintenance history and documentation that stands up to an audit, from GMP records and '
       'from SAP and CMMS entries since 2022.')

    lp('The team description matters as much as the tasks. As a team, we support one another, '
       'share knowledge, and take pride in delivering safe, dependable solutions for offshore '
       'operations. That is close to how I have run workshops and service teams, and wellbeing '
       'and collaboration are not soft extras in a team that handles heavy equipment. I work in '
       'a structured way with SAP or a similar ERP system, tools management systems, and '
       'Microsoft Office, and I am fluent in spoken and written English. I hold a clean '
       'driving licence and can work primarily on site in Esbjerg with occasional travel; a '
       'move to the area is fine with me. Proven very high employee satisfaction and '
       'motivation, which you list among the benefits, is usually the result of how a team is '
       'run, and that part I take seriously.')

    lp('The first 90 days are sketched on page 3 of the CV as a plan rather than a promise: '
       'learn the tools and the system, then take the priorities, then improve the flow '
       'between warehouse, maintenance and transport. The salary range of kr750,000 to '
       'kr950,000 is noted and sits where I would expect for the responsibility. Continuous '
       'development opportunities for all employees also match what I want next. Ørsted\'s '
       'invitation to shape the future with us is a large one, and I would rather start with '
       'the re-certification calendar. I can be reached on +45 93 99 95 14 or '
       'ajlooshahram@gmail.com, and I am ready for an interview whenever it fits you.',
       after=44)

    lp('Kind regards', after=8)
    lp('Shahram Ajloo', after=8)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFILE')
    m.para('Team leader for tools, warehouse and maintenance operations, with hands-on '
           'maintenance in the background. Recent years: 5 electricians and 3 apprentices in '
           'service and contracting, a workshop and its material flow, and equipment records '
           'in SAP and CMMS. Before that, maintenance and operations on a 24/7 utility plant '
           'and commissioning of 37 projects at Novo Nordisk under GMP/FDA/EMA. PRINCE2, '
           'structured, English as working language, and a habit of building my own small '
           'tools in Python and Claude.', after=32)

    m.section('EXPERIENCE')
    jobs = [
        ('CTO for the AI department and authorised electrical engineer (electrical and ventilation)',
         'Data Power Consultant ApS · Copenhagen · 2024 – present',
         'AI department 4-10 people · electrical and ventilation · 5 electricians + 3 apprentices',
         [('', 'I lead a 4-10 person AI department: the offering, the customers, and how '
               'solutions are built and documented. Investment cases for new services and '
               'monthly KPI follow-up.'),
          ('', '5 electricians and 3 apprentices in daily leadership: planning, 1:1s, training '
               'and safety follow-up with LOTO, APV and risk assessment at site start-up.')]),
        ('Owner / technical director / authorised electrical engineer',
         'ELOHVAC ApS · Copenhagen · May 2023 – November 2026 (company closed)',
         'Commercial customers · electrical, ventilation, climate · contracting · full P&L',
         [('', 'Tenders, pricing, subcontractor and supplier agreements, and monthly budget '
               'follow-up with full P&L responsibility. Material management, KS and handover '
               'documentation in every contract.'),
          ('', 'Personnel management of 5 electricians and 3 apprentices: daily planning, 1:1s '
               'and appraisals, structured training and safety follow-up. Zero critical '
               'deviations in the service agreements.')]),
        ('Senior commissioning engineer / project manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · November 2022 – July 2024',
         '37 CAPEX projects, DKK 2-10 mio. · 25 specialists · GMP/FDA/EMA',
         [('', 'Commissioning and project management on 37 CAPEX projects, DKK 2-10 mio. each. '
               'FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA, with zero critical findings at '
               'handover.'),
          ('', 'Monthly report to leadership and client management: progress, cost, risks and '
               'resources. 25 specialists across engineering, procurement and operations. SAP '
               'ERP for cost data.')]),
        ('Project and workshop manager',
         'Ventek-Air · Copenhagen · January 2022 – November 2022',
         '11 concurrent projects · 14-person team · warehouse and logistics',
         [('', 'Ran 11 concurrent projects and a 14-person team. Daily boards for capacity and '
               'progress, and responsibility for warehouse and logistics, safety documentation '
               'and handover packages in every project.')]),
        ('Maintenance and operations manager / workshop technician',
         'Biofos (Lynetten) · Copenhagen · August 2017 – January 2022',
         '24/7 operations · SCADA, PLC, HV switchgear · shift work',
         [('', 'Maintenance and operations on pumps, HVAC, HV switchgear and SCADA around the '
               'clock. Planned and corrective maintenance, fault finding, and tool and '
               'equipment upkeep in the workshop with 5S and Standard Work.'),
          ('', 'Shift work with LOTO, APV and near-miss reporting, and on-call duty. The '
               'equipment had to be ready at every shift change.')]),
        ('Electromechanical technician / production team leader',
         'ARJ Engineering · Tehran · December 2003 – March 2010',
         '12 mechanics and technicians · machine shop · product line',
         [('', 'Led 12 mechanics and technicians in a machine shop: shift planning, materials '
               'and goals. Fault diagnosis on industrial equipment, root-cause analysis and '
               'corrective actions.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('EDUCATION AND CERTIFICATIONS')
    m.edu('B.Tech (EQF6), Technology Management and Mechanical Engineering',
          'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7.6/12')
    m.edu('Authorised electrical engineer (LV/MV/HV)',
          'Danish Safety Technology Authority · May 2023')
    m.edu('Electrical and mechanical design, electrical engineering (EQF6)',
          'Tehran Technical University · 2000–2003')
    m.edu('PRINCE2, certified project manager', 'AXELOS / PeopleCert')
    m.edu('Refrigeration and air conditioning (AMU)',
          'Mercantec · 2021 · STCW 2021–2023, Danish Maritime Authority')
    m.para('Lean and Six Sigma practice, not certification: DMAIC, 5S, PDCA, VSM, A3, Kaizen, '
           'Standard Work, SMED, TPM, 5 Whys, Ishikawa and FMEA, used in documented work on '
           'maintenance, quality and planning.', after=48)

    m.section('LANGUAGES, TOOLS AND PRACTICALITIES')
    m.para('Danish (native) · English (fluent, spoken and written) · Persian (native). SAP ERP '
           'and CMMS for equipment records, Microsoft Office with Excel and Power Query daily, '
           'Power BI and Python for dashboards and checklists, PRINCE2 for project structure. '
           'Clean B driving licence. Based in Måløv; a move to the Esbjerg area is fine with '
           'me. Available by agreement.', after=48)

    m.section('TOOLS, SYSTEMS AND WAREHOUSE')
    for label, body in [
        ('Equipment records',
         'Inventory, maintenance history and documentation in SAP and CMMS-style systems, kept '
         'accurate enough to hand to an auditor.'),
        ('Warehouse and logistics',
         'Material management and warehouse work on 11 concurrent projects, and stock control '
         'for service vans and a workshop.'),
        ('Maintenance',
         'Planned and corrective maintenance, fault finding, and re-certification habits from '
         'GMP records and 24/7 operations. LOTO, APV and risk assessment.'),
        ('Leadership',
         'Care, clarity and accountability: 1:1s, feedback, coaching and training follow-up. '
         'Teams from 3 to 25 people since 2003.'),
    ]:
        m.bullet(label, body, after=10)

    m.section('THE FIRST 90 DAYS')
    m.para('A plan for the first 90 days, written so the team can hold me to it:', after=12)
    for b in [
        'Days 1-30: Learn the tools, the tools management system and the team. I go through '
        'the inventory and the re-certification calendar with the three employees and the '
        'Esbjerg warehouse manager, and I take the safety procedures first. Target: I can '
        'answer what we hold and what is due.',
        'Days 31-60: Priorities and daily work become mine. Task allocation, maintenance '
        'planning, and the overview of operational risks, dependencies and deadlines for the '
        'coming campaigns. Target: no project asks twice for the same tool.',
        'Days 61-90: Development. Supplier and service-provider relationships tightened, one '
        'measurable improvement to the flow between warehouse, maintenance and transport, and '
        'objectives set with each employee. Target: one process measurably faster.',
    ]:
        m.bullet('', b, after=10)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Ørsted Wind Power A/S · Head of Tools Coordination & Maintenance · Esbjerg',
                   ('Requirement', 'Evidence'), [
        ("leading the team's daily work, setting clear priorities, allocating tasks, and "
         'balancing operational demand, competence, and safety',
         'Daily leadership of 5 electricians and 3 apprentices since 2023, and earlier teams '
         'of 12-25 people (2003-2010, 2022). Priorities set on daily boards, tasks allocated '
         'by competence, and safety in the balance: LOTO, APV and risk assessment at every '
         'start-up.'),
        ('coordinating maintenance, repair, re-certification, optimisation, and transport of '
         'specialist tools, equipment, and container solutions',
         'Maintenance and repair coordinated across service agreements and 11 concurrent '
         'projects (2022-2026). Re-certification habits from GMP records on 37 projects '
         '(2022-2024), and transport planning for a 14-person team with deliveries to several '
         'sites a day. Container solutions are new to me; the coordination pattern is not.'),
        ('ensuring safe, complete, compliant, and ready-to-use equipment is delivered to '
         'projects and campaigns within the agreed scope and schedule',
         '37 commissioning projects at Novo Nordisk delivered within agreed scope and schedule '
         'with zero critical findings at handover, and service agreements where equipment had '
         'to roll the same morning. Safe, complete and ready-to-use is a standard I have '
         'worked to since 2003.'),
        ('maintaining accurate inventory, documentation, maintenance history, and '
         're-certification records in the tools management system',
         'Equipment records in SAP ERP since 2022 and CMMS habits from service contracts: '
         'inventory, maintenance history and documentation kept current. Digitised checklists '
         'and reporting in Python and Claude since 2024, over 40% faster documentation.'),
        ('building effective relationships with internal stakeholders, standard-tool suppliers, '
         'external service providers, and the Esbjerg warehouse manager',
         'Supplier and subcontractor agreements negotiated since 2023, daily stakeholder work '
         'across 25 specialists at Novo Nordisk, and warehouse organisation cooperation on 11 '
         'parallel projects. Relationship work at both ends: the contract and the delivery.'),
        ('developing your team through clear objectives, regular feedback, coaching, training '
         'follow-up, and a strong focus on wellbeing and collaboration',
         'Structured apprenticeship training for 3 electricians (2023-2026), 1:1s and '
         'appraisals for all 8 in the team, and training follow-up documented in skills '
         'matrices since 2003. Wellbeing followed up through APV and near-miss reporting.'),
        ('have people-management experience and lead with care, clarity, and accountability',
         'Over 10 years of people management in total (2003-2010 and 2023-2026): 5 electricians '
         'and 3 apprentices, 14 in contracting, 25 specialists, 12 in a workshop. Clear '
         'objectives, regular 1:1s, and decisions explained where they are made.'),
        ('can coordinate and prioritise many competing tasks while maintaining an overview of '
         'operational risks, dependencies, and deadlines',
         '11 concurrent projects in 2022, 37 parallel CAPEX projects (2022-2024), and service '
         'work with acute call-outs between planned tasks. Overview kept with daily boards, '
         'PRINCE2 structure and risk logs; deadlines met with zero critical findings.'),
        ('bring experience from warehouse operations, tooling, maintenance, offshore wind, oil '
         'and gas, or another relevant industrial environment',
         'Warehouse operations and logistics on 11 concurrent projects, tooling and maintenance '
         'since 2003, and relevant industrial environments: pharma under GMP/FDA/EMA, 24/7 '
         'utility operations, and electrical contracting. Offshore wind and oil and gas are not '
         'on my record. The rest comes from pharma, utility operations and electrical '
         'contracting.'),
        ('communicate clearly and build trusted relationships across teams, suppliers, and '
         'external service providers',
         'Cross-team communication daily since 2003: technicians, engineers, production, '
         'customers and suppliers. As director, negotiations with subcontractors and customers; '
         'as project manager, monthly reporting to leadership and clients (2022-2024).'),
        ('work in a structured way and are comfortable using SAP or a similar ERP system, tools '
         'management systems, and Microsoft Office',
         'Structured by habit: PRINCE2, daily boards and checklists. SAP ERP used since 2022, '
         'CMMS from service contracts, and Microsoft Office with Excel and Power Query every '
         'day. Python and Claude for my own tools since 2024.'),
        ('are fluent in spoken and written English, hold a clean driving licence, and can work '
         'primarily on site in Esbjerg with occasional travel',
         'English as working language at Novo Nordisk (2022-2024) and in international '
         'collaboration, written and spoken. Clean B driving licence. On-site work in Esbjerg '
         'with occasional travel is confirmed, and a move to the area is fine with me.'),
        ('manage specialist tools, equipment, container solutions, and warehouse activities for '
         'Special Tasks & Inspections',
         'Specialist tools and equipment managed in workshops and service operations since '
         '2003, warehouse activities on 11 projects, and site and container logistics from '
         'contracting since 2022. Special Tasks & Inspections is a new context; the management '
         'task is the same.'),
        ('lead three employees and work closely with technical specialists, project teams, '
         'suppliers, service providers, and the Esbjerg warehouse organisation',
         'Teams from 3 to 25 people led since 2003. Close work with technical specialists (25 '
         'at Novo Nordisk), project teams (37 projects), suppliers and service providers '
         '(contracts since 2023), and warehouse organisations daily.'),
    ], widths=(3400, 6946), compact=True)
    m.para('**The advert asks for applications via the online career pages; this letter and CV '
           'accompany that submission. I can be reached on +45 93 99 95 14 or '
           'ajlooshahram@gmail.com.**', after=8)

    m.save(path, title='Head of Tools Coordination and Maintenance - Ørsted')
    print(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_Orsted_HeadOfToolsCoordinationMaintenance.docx'))
