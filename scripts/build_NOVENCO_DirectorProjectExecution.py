#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Director, Project Execution — NOVENCO Building & Industry A/S, Næstved.

Engelsk opslag -> EN-GB dokument i masterdesign (4 sider): letter p1,
CV p2-3, kravmatrix p4. TEMPLATE = CBRE-305257-docx (seneste engelske).

BRUGERSVAR (bindende):
1. Lokation Næstved = commute_ok -> konkret linje i brevet.
2. Hilsen = "Dear Hiring Team," (intet navn i opslaget).
3. International ledelse = REEL -> selvsikkert om internationale/multinationale
   hold; påstå ikke porteføljeledelse i fire lande, men skriv uden hedge om
   cross-functional/cross-cultural ledelse.

STIL (3/3 mod #443 CTR): register "Commercial clarity, calm command",
åbning BT (governance over heroics), struktur "Direction, governance,
capability" (30/60/90). Engelsk: sammentrækninger BINDENDE (curly ’ som i
CBRE-scriptet). INGEN em dash. BANNED: 'proven' forekommer i JD'en men må
ALDRIG bruges i dokumentet. "Authorised Electrical Engineer (LV/MV/HV)".
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_CBRE_TechnicalSupervisor_305257.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'NOVENCO · Director, Project Execution · Næstved'
BANNER_RESUME = 'PROJECT EXECUTION · HVAC · PORTFOLIO & COMMERCIALS'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('28 November 2026')
    m.meta('NOVENCO Building & Industry A/S · Næstved')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Director, Project Execution, NOVENCO', bold=True,
           color='1A1A1A')
    m.para('Dear Hiring Team,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('A project portfolio rarely slips all at once. Requirements shift, '
       'capacity tightens, margins compress, and every change opens a new '
       'contractual interface. What brings it back isn’t heroics. It’s a '
       'fact-based portfolio review, decision rights that are actually clear, '
       'and change control that holds when it’s inconvenient, followed by a '
       'shared recovery plan the whole organisation can execute.')

    lp('The Director of Project Execution at NOVENCO owns exactly that layer. '
       'From order handover to final customer acceptance and satisfaction, the '
       'function has to deliver safe, timely, profitable, and contractually '
       'compliant delivery across markets, and it takes a steady commercial '
       'hand to keep revenue, gross margin, cash flow, working capital, '
       'forecasting, risk, quality, and customer commitments in one picture '
       'rather than eight spreadsheets. I’ve run projects and portfolios from '
       'the technical end since 2003, and the commercial discipline has '
       'followed them all the way.')

    lp('NOVENCO itself is the reason this lands on my desk. Engineering a '
       'Greener and Safer World is a brief I recognise: sustainable systems '
       'with low life-cycle costs, high energy efficiency with minimal '
       'environmental impact, and Reliability for Life Safety for critical '
       'applications, where dependable performance isn’t negotiable. Innovation '
       'Since 1947, with minimal waste and maximum recyclability and a '
       'portfolio built for long service life, exceptional durability, matches '
       'how I think about delivery: what we hand over has to keep working '
       'after we’ve gone.')

    lp('The first 90 days split accordingly. Days 1-30 set the direction: the '
       'portfolio reviewed fact-based, the functional direction, operating '
       'model, governance standards read against reality before anything is '
       'reorganised. Days 31-60 install the governance: change control, '
       'forecast accuracy, and a shared recovery plan for the projects under '
       'pressure, with Sales, Engineering, Supply Chain, Manufacturing, '
       'Finance, installation, and commissioning aligned around common '
       'delivery plans and commercial outcomes. Days 61-90 build the '
       'capability: clear priorities, effective decision rights, succession '
       'planning, and coaching for the team, until the new way of working '
       'becomes a repeatable standard rather than a project of its own.')

    lp('I know what it takes to lead experienced professionals and project '
       'managers across functions, cultures, countries, and competing '
       'commercial priorities. International teams have been my norm: specialists, '
       'technicians and contractors from different countries and cultures '
       'coordinated in English and Danish toward one delivery plan. On the '
       'portfolio side I’ve held accountability for margin, cash, risk, '
       'forecasting, contracts, and customer escalations, from 37 CAPEX '
       'projects in the DKK 2-10 million range with 25 specialists to full '
       'P&L responsibility as an owner. Customer escalations, contractual '
       'negotiations, claims, recovery actions and commercial decisions within '
       'a delegated authority framework are familiar ground; variation orders '
       'and final settlements were part of running an enterprise.')

    lp('The shape of the role also fits how I work: strategic functional '
       'leadership with regular engagement in major projects and customer '
       'relationships, and a team of 8-10 people where I report directly to '
       'the CEO. On paper, a B.Tech in Technology Management and Mechanical '
       'Engineering covers the relevant degree or equivalent experience line, '
       'and PRINCE2 covers the PMP, IPMA, PRINCE2, or comparable certification '
       'note. Næstved works from Måløv without trouble, and I can start by '
       'agreement. NOVENCollege, 25 days’ annual leave plus 5 days Feriefri '
       'after the qualifying period, an auto-enrolment pension scheme and '
       'access to a healthcare scheme are all in order. I look forward to '
       'hearing from you.', after=44)

    m.para('Kind regards', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFILE')
    m.para('Project leader with 20+ years in HVAC, electrical and industrial '
           'delivery, most of it with both a technical and a commercial grip '
           'on the same work. CAPEX portfolios in the DKK 2-10 million range '
           'with 25 specialists, full P&L as owner, and international teams '
           'coordinated across functions and cultures. Ventilation projects '
           'from tender to handover, commissioning under GMP/FDA/EMA '
           'discipline, and PRINCE2 certified. Forecast accuracy, change '
           'control and settlement treated as part of delivery, not paperwork '
           'after it.', after=32)

    m.section('PROFESSIONAL EXPERIENCE')
    jobs = [
        ('CTO, AI Department & Authorised Electrical Engineer (LV/MV/HV)',
         'Data Power Consultant ApS · Copenhagen · 2024 – present (from Nov. 2026 '
         'also ELOHVAC’s electrical activities)',
         'AI department 4-10 people · electrical service and enterprise · '
         'contractor coordination',
         [('Execution and coordination', 'Electrical service and enterprise '
           'planned, executed and handed over with the same discipline as on a '
           'site: quality control at handover, specialist contractors '
           'coordinated on schedules and standards, and documentation prepared '
           'along the way rather than reconstructed at the end.')]),
        ('Owner / Technical Director / Authorised Electrical Engineer',
         'ELOHVAC ApS · Copenhagen · May 2023 – Nov. 2026 (company closed)',
         'Business customers · electrical, ventilation and climate · full P&L · '
         'service agreements',
         [('Commercial control and P&L', 'Full P&L carried the commercial '
           'side: quotes and calculation, budget and monthly follow-up on '
           'margin and cash, service agreements for business customers on '
           'agreed standards, and variation orders settled with clients '
           'directly. Five electricians and three apprentices in the field, '
           'external suppliers on contract.')]),
        ('Senior Commissioning Engineer / Project Manager, Electrical Systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · Nov. 2022 – Jul. 2024',
         '37 CAPEX projects · laboratory and process equipment · GMP/FDA/EMA',
         [('Portfolio and governance', '37 CAPEX projects run as a portfolio, '
           'DKK 2-10 million each: forecasting and risk followed against '
           'approved plans, and every project taken from construction through '
           'FAT/SAT and IQ/OQ/PQ into use with documentation that withstood '
           'revision. 25 specialists and contractors aligned around one '
           'delivery plan per project.')]),
        ('Project & Workshop Manager',
         'Ventek-Air · Copenhagen · Jan. 2022 – Nov. 2022',
         '11 projects · 14 people · subcontractors · tender to handover',
         [('Delivery from tender to handover', 'Ventilation projects in '
           'buildings coordinated from tender to handover: 11 projects, 14 '
           'people and subcontractors planned week by week, deviations raised '
           'early, and acceptance testing with the client at handover. '
           'Commercial outcomes kept in view while the technical work '
           'landed.')]),
        ('Maintenance & Operations Manager / Workshop Technician',
         'Biofos (Lynetten) · Copenhagen · Aug. 2017 – Jan. 2022',
         '24/7 operations · critical plant · 10 people · shift work · CMMS',
         [('Uptime under pressure', 'Pumps, HVAC, process piping and electrical '
           'systems kept running in 24/7 operations with 10 employees on '
           'shift. Preventive and corrective maintenance planned on data, '
           'MTBF and MTTR followed as measures, and recovery actions decided '
           'in the moment when the plant needed them.')]),
        ('Electromechanical Technician / Production Supervisor',
         'ARJ Engineering · Tehran · Dec. 2003 – Mar. 2010',
         '12 mechanics and technicians · machine workshop · production line',
         [('Teams and root causes', 'Maintenance and repair of machines and '
           'production equipment with 12 mechanics and technicians led '
           'day-to-day. Root-cause analyses that changed how failures were '
           'handled, and responsibilities handed over so the team could decide '
           'without waiting for me.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('EDUCATION & CERTIFICATION')
    m.edu('B.Tech (EQF6), Technology Management and Mechanical Engineering',
          'Copenhagen School of Marine Engineering & Technology Management · '
          '2017-2022 · GPA 7.6/12')
    m.edu('Danish electrical authorisation LV/MV/HV (Authorised Electrical Engineer)',
          'Sikkerhedsstyrelsen · May 2023')
    m.edu('Electrical and Mechanical Engineering Design (EQF6)',
          'Tehran Technical University · 2000-2003')
    m.edu('PRINCE2 Certified Project Manager', 'AXELOS / PeopleCert')
    m.edu('Refrigeration and Climate Systems (AMU)',
          'Mercantec · 2021 · STCW 2021-2023, Danish Maritime Authority')

    m.section('COMPETENCIES')
    m.bullet('Portfolio and commercial control', 'Revenue, margin, cash and '
             'forecasting followed in one rhythm: monthly P&L review as owner, '
             'CAPEX forecasts against approved budgets, and working capital '
             'kept visible. Decisions made on numbers that were current, not '
             'on last quarter’s story.', after=10)
    m.bullet('Project execution and handover', 'From order handover through '
             'construction and commissioning to final acceptance: FAT/SAT, '
             'IQ/OQ/PQ, acceptance testing and documentation as part of '
             'delivery. Change control that prices variations instead of '
             'absorbing them.', after=10)
    m.bullet('Teams across functions and cultures', 'Project managers, '
             'specialists, technicians and contractors led across functions '
             'and cultures, in English and Danish. Clear priorities, decision '
             'rights close to the work, and coaching that hands responsibility '
             'over instead of hoarding it.', after=10)
    m.bullet('Contracts, claims and escalations', 'Contractual negotiations, '
             'claims and customer escalations handled at the table: service '
             'agreements, subcontractor contracts, variation orders and '
             'recovery actions within agreed authority. Firm on facts, easy to '
             'work with.', after=10)

    m.section('FIRST 90 DAYS')
    m.para('The plan follows the role: direction, governance, capability.',
           after=8)
    m.bullet('Days 1-30 · Direction', 'A fact-based portfolio review across '
             'the markets, the operating model and governance standards read '
             'against reality, and the functional direction agreed with the '
             'CEO. Goal: one shared picture of the portfolio before any '
             'changes.', after=10)
    m.bullet('Days 31-60 · Governance', 'Change control and forecasting put on '
             'a firm rhythm, a shared recovery plan for the projects under '
             'pressure, and Sales, Engineering, Supply Chain, Manufacturing '
             'and Finance aligned around common delivery plans. Goal: forecast '
             'accuracy you can steer by.', after=10)
    m.bullet('Days 61-90 · Capability', 'Clear priorities, decision rights and '
             'coaching embedded in the team, and the first parts of the '
             'long-term capability roadmap started. Goal: governance that '
             'works as a repeatable standard, not as my habit.', after=10)

    m.section('LANGUAGES, TOOLS & PRACTICAL')
    m.para('Danish (native) · English (professional) · Persian (native). SAP, '
           'Microsoft Office, MS Project, CMMS; PRINCE2. Driving licence B '
           '(manual). Available by agreement.', after=32)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Requirements and documentation · Director, Project '
                   'Execution, NOVENCO',
                   ('Requirement in the posting', 'Documented experience'),
                   [
        ('Extensive leadership experience from international HVAC, mechanical '
         'contracting, EPC, construction, or industrial project delivery',
         'HVAC and mechanical delivery since 2003: ventilation projects from '
         'tender to handover (Ventek 2022), electrical and climate enterprise '
         '(ELOHVAC 2023-2026), industrial plant in 24/7 operations (Biofos '
         '2017-2022) and machine-building production (ARJ 2003-2010). '
         'Construction-side discipline from CAPEX work at Novo Nordisk '
         '(2022-2024). EPC frameworks are adjacent to the enterprise work '
         'rather than claimed as named experience.'),
        ('Accountability for a complex project portfolio: margin, cash, risk, '
         'forecasting, contracts and customer escalations',
         'Accountability for a complex project portfolio, including margin, '
         'cash, risk, forecasting, contracts, and customer escalations: 37 '
         'CAPEX projects of DKK 2-10 million with 25 specialists (Novo Nordisk '
         '2022-2024), and full P&L with cash and contract exposure as owner '
         '(ELOHVAC 2023-2026).'),
        ('Strong financial and organisational judgement turning strategy into '
         'priorities, governance and executable plans',
         'Strong financial and organisational judgement that turns business '
         'strategy into clear priorities, governance, and executable plans: '
         'enterprise budgets and monthly margin follow-up, project forecasting '
         'on CAPEX portfolios, and organisations built around how work '
         'actually flows.'),
        ('Leadership across functions, cultures and countries',
         'The norm has been leading experienced professionals and project '
         'managers across functions, cultures, countries, and competing '
         'commercial priorities: international teams of specialists, technicians '
         'and contractors coordinated in English and Danish, from production '
         'floors in Tehran to commissioning sites in Denmark.'),
        ('A relevant degree or equivalent experience; PMP, IPMA, PRINCE2, or '
         'comparable certification',
         'B.Tech (EQF6) in Technology Management and Mechanical Engineering '
         '(2017-2022, GPA 7.6) covers the relevant degree or equivalent '
         'experience line, and PRINCE2 Certified Project Manager (AXELOS / '
         'PeopleCert) answers the PMP, IPMA, PRINCE2, or comparable '
         'certification note.'),
        ('Lead the Project Execution function: safe, timely, profitable and '
         'contractually compliant delivery',
         'Safe, timely, profitable, and contractually compliant delivery run '
         'as one discipline: safety and permits at 24/7 plant (Biofos '
         '2017-2022), schedule and margin control in enterprise (ELOHVAC '
         '2023-2026), and contract-compliant handover with acceptance testing '
         '(Ventek 2022, Novo Nordisk 2022-2024).'),
        ('Set functional direction, operating model, governance standards and '
         'long-term capability roadmap',
         'Functional direction, operating model and governance standards set '
         'in practice: documentation systems and FAT/SAT/IQ/OQ/PQ governance '
         'at Novo Nordisk to GMP/FDA/EMA standards, service delivery standards '
         'defined at ELOHVAC, and weekly planning and follow-up rhythms across '
         '11 parallel projects at Ventek. Long-term capability built through '
         'structured training and certifications.'),
        ('Own portfolio performance: revenue, gross margin, cash flow, working '
         'capital, forecasting, risk, quality and customer commitments',
         'Revenue, gross margin, cash flow, working capital, forecasting, '
         'risk, quality, and customer commitments have all sat on my desk: '
         'monthly P&L follow-up as owner, CAPEX forecasts against approved '
         'budgets, and quality commitments carried through KS and acceptance '
         'documentation.'),
        ('Lead and develop teams through clear priorities, effective decision '
         'rights, succession planning and coaching',
         'Clear priorities, effective decision rights, succession planning, '
         'and coaching in daily leadership: 12 mechanics at ARJ, 10 shift '
         'employees at Biofos, 5 electricians and 3 apprentices at ELOHVAC, '
         'and 25 specialists coordinated at Novo Nordisk, with structured '
         'training and responsibility handed over early.'),
        ('Align Sales, Engineering, Supply Chain, Manufacturing, Finance, '
         'installation and commissioning around delivery plans',
         'Common delivery plans and commercial outcomes across Sales, '
         'Engineering, Supply Chain, Manufacturing, Finance, installation, and '
         'commissioning: enterprise work where quote, procurement, execution '
         'and settlement had to agree, and CAPEX projects aligning client, '
         'contractors and specialists around one schedule.'),
        ('Guide customer escalations, contractual negotiations, claims and '
         'recovery actions within delegated authority',
         'Customer escalations, contractual negotiations, claims, recovery '
         'actions and commercial decisions within a delegated authority '
         'framework are familiar: variation orders and final settlements '
         'handled in the open with clients, and service agreements '
         'renegotiated when facts changed.'),
        ('Delivery from order handover to final customer acceptance and '
         'satisfaction',
         'Order handover to final customer acceptance and satisfaction has '
         'been the arc of every project: construction through FAT/SAT and '
         'IQ/OQ/PQ into use (Novo Nordisk), acceptance testing with the client '
         'at handover (Ventek), and service levels kept in the years after '
         '(ELOHVAC).'),
        ('Fact-based portfolio review, decision rights, change control and '
         'shared recovery plans',
         'Fact-based portfolio review, clear decision rights, change control '
         'and a shared recovery plan are how I work: data before opinions on '
         'CAPEX portfolios, change requests logged and priced instead of '
         'absorbed, and recovery plans teams can execute without heroics.'),
        ('Improved forecast accuracy and critical projects back within '
         'approved delivery plans',
         'Forecast accuracy treated as a management measure: monthly '
         'forecasting on project economy, risk registers that update instead '
         'of decorate, and critical projects brought back within approved '
         'delivery plans by changing the plan early rather than the date '
         'late.'),
        ('Governance becoming a repeatable standard across countries',
         'Governance that becomes a repeatable standard across countries is a '
         'natural ambition: documentation and quality systems built once and '
         'used everywhere at Novo Nordisk, and service standards at ELOHVAC '
         'written so any technician could follow them.'),
        ('Team of 8-10 people; report directly to the CEO',
         'Teams close to the 8-10 mark have been mine before: 12 mechanics and '
         'technicians at ARJ and 10 employees on shift at Biofos, plus 5 '
         'electricians and 3 apprentices at ELOHVAC. Direct access to '
         'ownership and CEO-level decisions was daily reality as technical '
         'director and owner.'),
        ('Strategic functional leadership with regular engagement in major '
         'projects and customer relationships',
         'Strategic functional leadership with regular engagement in major '
         'projects and customer relationships is the working model I come '
         'from: strategy set at ownership level and followed on the shop '
         'floor, with major customers handled personally rather than '
         'delegated away.'),
        ('Life-safety ventilation solutions, high energy efficiency and low '
         'life-cycle costs',
         'Ventilation is my home turf: 11 ventilation projects delivered in '
         'buildings (Ventek 2022), ventilation and climate systems in service '
         '(ELOHVAC 2023-2026), and indoor climate work since 2003. Life-safety '
         'applications and low life-cycle cost thinking align with how I judge '
         'technical solutions, and sustainability is the frame: high energy '
         'efficiency with minimal environmental impact is the brief I have '
         'worked to.'),
                   ],
                   widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo — Application and CV — Director, Project '
                       'Execution, NOVENCO')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_NOVENCO_DirectorProjectExecution.docx')
    build(out)
    print(out)
