# -*- coding: utf-8 -*-
"""Project Director — Novo Nordisk Engineering (NNE), Kalundborg, req5155
(English posting -> en-GB document).

4 pages in master design: letter p1, CV p2-3, requirement matrix p4.
Contact: department Director Julia Loisel, +45 3079 2767 -> "Dear Julia Loisel,".
Deadline 5 January 2027; interviews on a running basis. Applications only via the
online recruitment system; no cover letter needed (a few sentences about why in the
CV), no photo (fair hiring). Brugeren valgte masterdesign som vanligt (gældende
beslutning fra Samtank: masterdesign uanset kun-CV-notits).

SAMME-FIRMA-REGLER: tidligere NNE-ansogning (Department Manager EI) findes ->
intet genbruges. Alt indhold skrevet frisk til dette opslag.

STILVALG (style_guard godkendt, 3/3 skift mod #434 Hansen & Co):
  register    = Complexity, calm and predictable delivery
  åbningsgreb = BK (den urokkelige dato: handover-datoen der ikke rykker sig,
                før kandidaten nævnes)
  struktur    = Direction, integration, handover (30/60/90 = the direction ·
                the integration · the handover)

BRUGERSVAR 26.11 (bindende): Kalundborg fem dage on-site -> "kan flytte til
Kalundborg-omraadet hvis jobbet er rigtigt" (Lystrup-moenstret, skriv som fakta).
Novo Nordisk (Kalundborg/Bagsvaerd) 2022-2024 = reel CAPEX-erfaring paa kundesiden.
AI/Claude-kodning er reel praksis -> "use AI responsibly while judging its output
critically" matcher aerkeligt.

MASTER-REGLER (engelsk): "Authorised electrical engineer (LV/MV/HV)" — never
"authorised elinstaller". Degree: B.Tech (EQF6) + EQF6 electrical design = "or
similar background"; paaastaar aldrig M.Sc.

BRUGERENS KORREKTION: humaniseret brev OG CV. Ingen em dash. Ingen forbudte ord.
Engelsk: sammentrækninger er BINDENDE.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'NNE · Project Director, Kalundborg (req5155)'
BANNER_RESUME = 'Project delivery · pharma CAPEX · teams · governance · handover'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('26 November 2026')
    m.meta('req5155 · Project Portfolio & Management · Kalundborg, Denmark')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Project Director, Kalundborg (req5155)',
           bold=True, color='1A1A1A')
    m.para('Dear Julia Loisel,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- page 1
    lp('The handover date is the one thing in a pharma project that doesn\u2019t move. '
       'Requirements pull in different directions, scopes shift under pressure, and a '
       'team of specialists needs one clear direction before the date arrives. '
       'Directing strategic key projects within Pharma CAPEX is the work I want, and '
       'Kalundborg is ground I know well: I ran CAPEX projects here in 2022-2024.')

    lp('At NNE you design, build and optimise pharmaceutical manufacturing facilities '
       'that are essential to the health and well-being of patients everywhere, with '
       '2,000+ employees across Denmark, India, and the US. I\u2019ve worked the other '
       'side of that table. 37 CAPEX projects in Novo Nordisk\u2019s Kalundborg and '
       'Bagsværd organisation taught me the pharma engineering value chain and its '
       'industry specifics from the inside: API production, GMP, FDA and EMA '
       'documentation, FAT/SAT '
       'and IQ/OQ/PQ, and handovers where zero critical findings was the standard. My '
       'degree is a B.Tech (EQF6) in engineering, and I\u2019ve kept learning since.')

    lp('The role\u2019s shape is familiar ground. What that looks like in practice: '
       'executing highly complex, large projects from initiation through execution to '
       'handover, the kind I did in 37 projects with 25 specialists across engineering, '
       'procurement and operations. Setting the direction means frameworks, governance '
       'and ways of working that produce predictable results, and I keep strategy and '
       'daily decisions in the same room. I bring PRINCE2 and '
       'CAPEX governance habits, and \u2018Our Engineering Model\u2019 I\u2019ll pick '
       'up in weeks. The real task is integration across the disciplines with a firm '
       'focus on objectives and progress, and project teams of typically 7\u201315 '
       'members are my normal range.')

    lp('Your description of the environment reads like my last years: a '
       'cross-disciplinary and ever-changing setting, a fast-paced atmosphere with '
       'many stakeholders and widely differing requirements. I navigate ambiguity, '
       'manage risks, align priorities and move forward with confidence because the '
       'plan is written down and the risks are named early. Strategic work with '
       'customer teams and management, external contractors and local authorities has '
       'been part of my job since 2003, and communicating transparently with '
       'stakeholders while understanding customer interests is how I keep alignment '
       'through the project lifecycle. I build solid networks internally and '
       'externally, because effective collaboration and knowledge sharing is what '
       'makes a matrix work. High-quality deliverables balancing scope, '
       'resources and budget is the standard I hold; ambitious timelines are met by '
       'trimming scope smartly, not by hope. New frameworks and a new rhythm are easy '
       'to adopt when the direction is clear.')

    lp('When the pace picks up, I stay calm and effective. Reliable and accountable is '
       'the short version: following through on commitments comes first, and I address '
       'issues before they become obstacles. I stay close to where the work happens so '
       'my pragmatic and solution-focused decisions stay balanced with strategic '
       'understanding. Mentoring is part of the job for me, and I lead by example and '
       'apply lessons learned instead of repeating mistakes. Openness to learning '
       'keeps me current: I\u2019m always seeking external inspiration and benchmarks, '
       'and I use AI daily in my coding and analysis, use AI responsibly while judging '
       'its output critically, exactly as you ask.')

    lp('Why NNE? The projects here are essential to patients, and I want to build '
       'trust, engagement and shared purpose around work that matters, in an '
       'environment where people can contribute, develop and perform at their best. '
       'On practicalities: I can be on-site five days a week, and I\u2019m ready to '
       'move to the Kalundborg area for the right role. Your award-nominated '
       'onboarding programme tells me the start is taken seriously here. I\u2019ll '
       'submit through the online recruitment system as asked, and I\u2019d welcome '
       'a chat first. I\u2019ll text you to arrange a convenient time.', after=44)

    m.para('Kind regards', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- page 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFILE')
    m.para('For 20+ years I\u2019ve managed projects across pharma CAPEX, '
           'critical utilities and technical contracts. I\u2019ve led 37 CAPEX '
           'projects across the full project life cycle in Novo Nordisk\u2019s '
           'Kalundborg and Bagsværd organisation: GMP/FDA/EMA compliance, commissioning '
           'and handover with zero critical findings. B.Tech (EQF6) engineering, '
           'PRINCE2, and high-level stakeholder management across project teams, '
           'customers and authorities. I\u2019m applying because projects that land on '
           'time are the work I do best, and NNE\u2019s project environment is where I '
           'want to do it.', after=32)

    m.section('EXPERIENCE')
    jobs = [
        ('CTO, AI department / Authorised Electrical Engineer (LV/MV/HV)',
         'Data Power Consultant ApS · Copenhagen · 2024 – present (from Nov. 2026 also '
         'ELOHVAC\u2019s electrical activities)',
         'AI department, 4-10 people · electrical service and contracting · 5 '
         'electricians + 3 apprentices',
         [('Delivery and direction', 'Deliverables directed from tender and planning '
           'through to handover, with 4-10 specialists engaged. AI tools used daily in '
           'coding and analysis, responsibly and with critical judgement of the '
           'output. PRINCE2 habits and Microsoft Project as the planning backbone.')]),
        ('Owner / Technical Director / Authorised Electrical Engineer (LV/MV/HV)',
         'ELOHVAC ApS · Copenhagen · May 2023 – Nov. 2026 (company closed)',
         'Business customers · electrical, ventilation and climate · contracting · '
         'full P&L · service agreements',
         [('Negotiation and customer interests', 'Tenders, negotiations and contracts '
           'with customers and suppliers run by me, expectations aligned through '
           'transparent follow-up, and scope, resources and budget balanced on every '
           'job. Service agreements renewed on delivered quality.'),
          ('Resources and control', '5 electricians and 3 apprentices planned and '
           'followed, subcontractors held to the agreement, and project control '
           'practised weekly on cost and progress.')]),
        ('Senior Commissioning Engineer / Project Manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · Nov. 2022 – Jul. 2024',
         '37 CAPEX projects, DKK 2-10 million each · 25 specialists · GMP/FDA/EMA',
         [('Full project life cycle', '37 CAPEX projects taken from initiation through '
           'execution to handover: commissioning, test and start-up (FAT/SAT, '
           'IQ/OQ/PQ), compliance with industry standards documented, and zero '
           'critical findings at handover. Resource planning and project control '
           'across 25 specialists in engineering, procurement and operations.')]),
        ('Project & Workshop Manager',
         'Ventek-Air · Copenhagen · Jan. 2022 – Nov. 2022',
         '11 concurrent ventilation projects · 14 people · subcontractors',
         [('Complex projects, clear plans', '11 concurrent projects run from start to '
           'finish with clear responsibility split, external contractors coordinated '
           'on agreements and deadlines, and risks managed before they became '
           'obstacles. AB18/ABT 18 as the contract basis.')]),
        ('Maintenance & Operations Manager / Workshop Technician',
         'Biofos (Lynetten) · Copenhagen · Aug. 2017 – Jan. 2022',
         '24/7 operations · critical plant · 10 employees · shift work',
         [('Close to where the work happens', 'Operation and maintenance of critical '
           'plant around the clock: pumps, HVAC, process piping, SCADA and PLC. '
           'Work methods and risk assessments written with the shift teams, and local '
           'authority contact as part of running the plant.')]),
        ('Electromechanical Technician / Production Manager',
         'ARJ Engineering · Tehran · Dec. 2003 – Mar. 2010',
         '12 mechanics and technicians · machine shop · production line',
         [('The foundation', 'Production department with 12 mechanics and technicians: '
           'schedules, materials and targets. Risk management and quality assurance '
           'in practice, and root-cause analyses that changed how we handled faults.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('EDUCATION AND CERTIFICATES')
    m.edu('B.Tech (EQF6), Technology Management and Mechanical Engineering',
          'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7.6/12')
    m.edu('Danish electrical authorisation LV/MV/HV as Authorised Electrical Engineer',
          'Sikkerhedsstyrelsen · May 2023')
    m.edu('Electrical and Mechanical Engineering Design, electrical (EQF6)',
          'Tehran Technical University · 2000–2003')
    m.edu('PRINCE2, certified project manager', 'AXELOS / PeopleCert')
    m.edu('Refrigeration and climate systems (AMU)',
          'Mercantec · 2021 · STCW 2021–2023, Danish Maritime Authority')

    m.section('COMPETENCIES')
    m.bullet('Project direction', 'PRINCE2, Microsoft Project and CAPEX governance '
             'from initiation to handover. Frameworks, ways of working and predictable '
             'reporting established early; scope, resources and budget balanced '
             'weekly, not at the gate meeting.', after=10)
    m.bullet('Pharma and compliance', 'GMP/FDA/EMA documentation, FAT/SAT and IQ/OQ/PQ, '
             'and compliance with industry standards as daily practice (Novo Nordisk '
             '2022-2024). The pharma engineering value chain seen from both the '
             'customer and the contractor side.', after=10)
    m.bullet('Stakeholder management', 'Customer teams and management, external '
             'contractors and local authorities engaged at strategic level. '
             'Negotiations run on transparent interests rather than positions, and '
             'alignment kept through the project lifecycle.', after=10)
    m.bullet('Teams and mentoring', 'Teams of 7-15 as the normal range and matrices '
             'up to 25 specialists. Lead by example, apply lessons learned instead of '
             'repeating, and grow the team through mentoring. An engaging work '
             'environment built on '
             'integrity and respect.', after=10)
    m.bullet('Tools and AI', 'SAP ERP, Excel, Microsoft Project, SharePoint. AI tools '
             'in daily coding and analysis, used responsibly and with critical '
             'judgement of the output. Danish and English in writing and speech; '
             'Persian as a second native language.', after=10)

    m.section('THE FIRST 90 DAYS')
    m.para('The plan follows the role: direction, integration, handover.', after=8)
    m.bullet('Days 1-30 · The direction', 'Portfolio, governance and \u2018Our '
             'Engineering Model\u2019 learned in context, with time on site and in '
             'the project teams. Goal: I know the portfolio and the frameworks, and '
             'the direction for my projects is clear.', after=10)
    m.bullet('Days 31-60 · The integration', 'Disciplines brought into one plan, '
             'stakeholders mapped, and risks named early with the team. Goal: the '
             'project team works as one, and customer interests are aligned with the '
             'plan.', after=10)
    m.bullet('Days 61-90 · The handover', 'Delivery rhythm established, project '
             'control running, and lessons learned feeding back into how we work. '
             'Goal: predictable results on the first milestones, and a team that '
             'performs at its best.', after=10)

    m.section('LANGUAGES, TOOLS AND PRACTICALS')
    m.para('Danish (native) · English (professional) · Persian (native). PRINCE2, SAP '
           'ERP, Microsoft Project, SharePoint, Excel. Authorised Electrical Engineer '
           '(LV/MV/HV). Driving licence B (manual gear). Based in Måløv; ready to '
           'relocate to the Kalundborg area for the right role. Available by '
           'agreement.', after=32)

    # ------------------------------------------------------------- page 4
    m.page_break()
    m.models_table('Project Director, NNE (req5155) · requirements and documentation',
                   ('Requirement in the posting', 'Documented experience'),
                   [
        ('Degree in Engineering (M.Sc. or B.Sc.) or similar background',
         'Engineering degrees at EQF6 level: B.Tech (EQF6) in Technology Management '
         'and Mechanical Engineering (2017-2022) and Electrical and Mechanical '
         'Engineering Design, electrical, EQF6 (2000-2003). Not an M.Sc.; the '
         'background is engineering and it is documented.'),
        ('Significant experience in project management, preferably within pharma '
         'engineering or a related field',
         '20+ years of project management: pharma CAPEX (Novo Nordisk 2022-2024), '
         'critical utilities (Biofos 2017-2022) and technical contracting (Ventek '
         '2022, ELOHVAC 2023-2026). Pharma engineering is the most recent and most '
         'relevant chapter.'),
        ('Experience leading large, highly complex projects across the full project '
         'life cycle',
         'Full project life cycle documented: 37 CAPEX projects from initiation '
         'through execution to handover (Novo Nordisk 2022-2024), 11 concurrent '
         'contracting projects with subcontractors (Ventek 2022) and own portfolio '
         '(ELOHVAC 2023-2026).'),
        ('Thorough understanding of the pharma engineering value chain and industry '
         'specifics',
         'The value chain from the inside: GMP, FDA and EMA requirements, FAT/SAT and '
         'IQ/OQ/PQ, commissioning and handover discipline (Novo Nordisk 2022-2024), '
         'plus the contractor side from own contracting work. Industry specifics are '
         'not theory for me.'),
        ('High-level skills in stakeholder management, including customer relations '
         'and negotiations across various levels',
         'Stakeholder management at all levels: 25 specialists across engineering, '
         'procurement and operations (Novo 2022-2024), customer negotiations and '
         'agreements (ELOHVAC 2023-2026), and authorities and operators (Biofos '
         '2017-2022).'),
        ('Experience with resource planning, project control, and compliance with '
         'industry standards',
         'Resource planning of 25 specialists (Novo 2022-2024), 14 people and '
         'subcontractors (Ventek 2022) and 8 employees (ELOHVAC 2023-2026). Control on '
         'cost and progress is run weekly, and compliance with industry standards '
         'documented through GMP audits.'),
        ('Directing strategic key projects and executing highly complex, large '
         'projects within Pharma CAPEX',
         'Pharma CAPEX directed and executed: 37 projects of DKK 2-10 million each in '
         'Novo Nordisk\u2019s Kalundborg and Bagsværd organisation (2022-2024), with '
         'strategic priority setting against production needs and budgets.'),
        ('Setting the direction and establish the frameworks, governance and ways of '
         'working needed to deliver predictable results',
         'Frameworks and governance built in practice: PRINCE2 as method, project '
         'control routines established early (Novo 2022-2024), and service agreement '
         'governance designed and run (ELOHVAC 2023-2026). Predictable reporting is '
         'a habit, not an event.'),
        ('Turning a project environment into a clear plan and organization; navigate '
         'ambiguity, manage risks, align priorities',
         'Clear plans out of moving parts: 37 concurrent projects (Novo 2022-2024) '
         'and 11 parallel contracting projects (Ventek 2022). Risks named early, '
         'priorities aligned with stakeholders, and decisions made close to the work.'),
        ('Interacting, negotiating and coordinating at a strategic level with the '
         'customer team, external contractors and local authorities',
         'Strategic interaction since 2003: customer teams and management (Novo '
         '2022-2024, ELOHVAC 2023-2026), external contractors and subcontractors '
         '(Ventek 2022, ELOHVAC 2023-2026) and local authority contact in operations '
         '(Biofos 2017-2022).'),
        ('Aligning expectations and priorities throughout the project lifecycle by '
         'communicating transparently with stakeholders',
         'Transparent communication as working style: monthly reporting on progress, '
         'cost and risks to management (Novo 2022-2024), customer follow-up in '
         'service agreements (ELOHVAC 2023-2026), and stakeholder alignment at every '
         'milestone.'),
        ('Ensuring high-quality deliverables balancing scope, resources and budget, '
         'and adapt to ambitious timelines',
         'Balancing act documented: 37 projects delivered at scope, on budget bands '
         'of DKK 2-10 million, with zero critical findings at handover (Novo '
         '2022-2024). Ambitious timelines handled by staging work smartly, not by '
         'cutting verification.'),
        ('Mentoring and lead by example and actively applying lessons learned',
         'Since 2003 I\u2019ve mentored and led by example: apprentices trained '
         '(ELOHVAC 2023-2026), teams led '
         'through 10 people (Biofos), 14 (Ventek) and 25 (Novo). Lessons learned fed '
         'back through root-cause analyses that changed how faults were handled '
         '(ARJ 2003-2010).'),
        ('Valuable integration across the disciplines in the project team, typically '
         '7-15 members, with a firm focus on objectives and progress',
         'Integration across disciplines is the daily work: engineering, procurement '
         'and operations in one plan (Novo 2022-2024). Team sizes from 4-10 people up '
         'to 25 specialists, so typically 7-15 members is the core of the range. '
         'Objectives and progress kept visible through structured follow-up.'),
        ('Build trust, engagement and shared purpose; an environment where people can '
         'contribute, develop and perform at their best',
         'Trust built on presence and straight answers: teams that stayed with me '
         'across companies (ELOHVAC 2023-2026), and engagement created in an '
         'operations environment with shifts and critical plant (Biofos 2017-2022).'),
        ('Calm and effective when the pace picks up; reliable and accountable; close '
         'to where the work happens',
         'Calm under pace practised in 24/7 operations (Biofos 2017-2022) and in 37 '
         'parallel projects (Novo 2022-2024). Accountability on P&L and contracts '
         '(ELOHVAC 2023-2026), and decisions made on site, not from a distance.'),
        ('Inclusive, treating everyone with integrity and respect; supportive mentor '
         'together with line management',
         'Teams with many nationalities and backgrounds where I treat everyone with '
         'integrity and respect (Ventek, Novo, ELOHVAC). Mentoring happens alongside '
         'line management as owner and director, and apprentices developed to skilled '
         'staff.'),
        ('Curious and eager to learn; seeking external inspiration and benchmarks; '
         'use AI responsibly while judging its output critically',
         'Learning is ongoing: B.Tech completed while working full time, PRINCE2 '
         'added mid-career, and AI tools adopted early in daily coding and analysis. '
         'I use AI responsibly while judging its output critically, and I benchmark '
         'against external practice.'),
        ('Minimum 8-10 years of experience; on-site presence at the workplace in '
         'Kalundborg five days a week',
         '20+ years of experience, comfortably above the minimum. On-site five days a '
         'week is workable: I ran CAPEX projects in Kalundborg 2022-2024 and I am '
         'ready to move to the Kalundborg area for the right role.'),
                   ], widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo · Project Director, NNE (req5155)')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_NNE_ProjectDirector.docx')
    build(out)
    print(out)
