# -*- coding: utf-8 -*-
"""Eurowind Energy — Technical Operations Manager, Technical Asset Performance DK (Hobro).

English deliverable (the posting is English): application page + CV in one document.
Policy: master/README.md — extreme confidence, no caveats.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Technical Operations Manager · Asset performance, HV and operations data'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('5 November 2026')
    m.meta('Eurowind Energy A/S · Hobro · Technical Asset Performance DK')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Technical Operations Manager — Technical Asset Performance DK', bold=True,
           color='1A1A1A')
    m.para('To Laurits H Østergaard, Manager, Technical Asset Performance DK', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('A wind farm is a power plant that nobody is standing next to. That is the whole difficulty of asset '
           'performance: the asset does not tell you it is degrading, the data does — and only if someone has '
           'decided in advance which number means what, who is watching it, and what happens when it moves. '
           'A portfolio of that size is kept reliable by a technical organisation where every asset has a number, '
           'every incident has a cause and every shutdown has a plan. That is the work I want to do in '
           'Technical Asset Performance DK.', after=80)

    m.para('**I would run the technical area on four fixed things.** First, **every asset has a number and the '
           'number has an owner**: availability, production against the expected curve, downtime hours, failure '
           'frequency and cost per MWh — built up from infrastructure level to component level, so a gearbox, a '
           'transformer or an inverter is not an anonymous part of a site total but an item with a history, a '
           'condition and a next action. Second, **an incident is closed when the cause is**: evidence before '
           'action, root cause rather than the first plausible explanation, and a check three months later that '
           'the same failure has not come back under a different name. Third, **shutdowns are planned backwards '
           'from the date**: scope, spare parts, crews, permits, service providers and grid constraints in one '
           'plan, with the outage window used for everything that cannot be done live. Fourth, **data nobody '
           'uses is not monitoring**: alarm rationalisation, parameters that mean the same thing across sites, '
           'and reports that a manager, a service provider and an investor can all read without translation.', after=80)

    m.para('The electrical side is where I am strongest. I hold the Danish authorisation for **LV, MV and HV '
           'installations**, and at **Lynetten under Biofos** — one of Denmark\'s largest wastewater plants, in '
           '24/7 operation — I was operations and maintenance manager for an asset base of pumps, blowers, '
           'ventilation, **transformers, switchgear, protection and drives**, with **SCADA** on everything that '
           'moved. Five years of keeping a plant running that was not allowed to stop taught me the discipline '
           'this role is built on: condition before failure, isolation and permits before work, and a fault '
           'history that is written down while the fault is happening.', after=80)

    m.para('Data and monitoring are not a side interest for me. At Lynetten I ran **energy management on '
           'metering and SCADA data** rather than on assumptions: where did the energy go, which assets drew it, '
           'and what gave the largest effect per krone — the documented result was **more than 40 % lower energy '
           'consumption**, and it held because the follow-up became a routine and not a project. I clean, join '
           'and compare operational data in **Python and Excel**, and I build the views that make a portfolio '
           'readable: availability, downtime causes, production against expectation, and the trend that says a '
           'component is on its way out before it takes the string with it.', after=80)

    m.para('Commissioning and integration I have done from the inside. At **Novo Nordisk** I ran **37 parallel '
           'capital projects** worth 2–10 million DKK each, with 25 specialists: FAT and SAT, IQ/OQ/PQ, '
           'acceptance criteria, punch lists, change control and handover to operations — with **zero critical '
           'findings** at audit. I have also supervised contractors through production shutdowns, where the '
           'window is fixed, the crews are many and the cost of a day is visible on a chart. An asset is not in '
           'operation when the contractor leaves; it is in operation when the data, the documentation and the '
           'alarm list agree.', after=80)

    m.para('Working with service providers and contractors is a large part of my daily work, and so is the '
           'commercial side of it. I have been on both sides of the table — as **project and workshop manager at '
           'Ventek-Air** for **14 employees and 11 concurrent jobs**, and as owner of **ELOHVAC** since 2023, '
           'where I carry full P&L with five technicians and three apprentices. That is where I learned to read a '
           'service contract for what it actually covers, to ask for the failure report rather than the invoice, '
           'and to weigh a repair against a replacement with numbers instead of instinct. When I report upward, '
           'it is in the language the decision is made in: what it costs, what it risks, and what it earns.', after=80)

    m.para('Eurowind says it plainly: **"the wind is never standing still"**, and the culture is one where people '
           'speak up and where growing is part of the job. That fits how I work. A technical operations manager '
           'who only answers questions is a reporting function; the value is in taking a complex topic — an '
           'underperforming string, a recurring converter fault, a maintenance campaign that keeps slipping — '
           'from identification to a closed action that someone else can audit.', after=80)

    m.para('Practically: I live in Måløv, Hobro is around three hours away by car, and I plan my weeks around the '
           'office and the sites, with travel to parks a few times a year as the role requires. '
           'I have a **driver\'s licence (B)**, I work and write **English** professionally, and I am ready to '
           'take the **full GWO package** with the onboarding so I can get out to the turbines from the start. I '
           'can start by agreement. I would like to hear which parks and which asset types are giving the team '
           'the most technical trouble right now — that is where I would begin.', after=70)
    m.meta('Kind regards,', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('Technical operations and maintenance manager with 20+ years in technical asset management, '
           'electrical infrastructure and 24/7 operations — authorised machine and electrical installer (LV/MV/HV) '
           'with a B.Tech in Technology Management & Mechanical Engineering. Five years as operations and '
           'maintenance manager on a national-scale plant with transformers, switchgear, protection, drives and '
           'SCADA, where energy management on metering data delivered over 40 % lower consumption. 37 capital '
           'projects commissioned under GMP with zero critical findings; full P&L since 2023. Structured, '
           'analytical and commercial about the decisions the data is meant to support.', after=80)

    m.section('ASSET PERFORMANCE, HV AND OPERATIONS DATA')
    for label, body in [
        ('End-to-end technical asset management',
         'Asset registers built from infrastructure down to component level, with condition, history, criticality '
         'and next action per item; maintenance prioritised by criticality and condition rather than by calendar, so '
         'that reliability is a managed outcome and not a hope.'),
        ('Troubleshooting, root cause and incidents',
         'Fault finding on electrical and mechanical systems with evidence before action: measurements, trend '
         'data and history first, then root cause, corrective action and a follow-up that proves the failure did '
         'not return.'),
        ('Maintenance planning and shutdowns',
         'Major maintenance campaigns and production stops planned backwards from the fixed date — scope, spares, '
         'crews, permits, service providers and isolation — with the window used for everything that cannot be '
         'done live.'),
        ('Commissioning and integration',
         'FAT/SAT, IQ/OQ/PQ, acceptance criteria, punch lists, change control and handover to operations in 37 '
         'capital projects; new assets integrated with documentation, alarm lists and data that agree.'),
        ('Monitoring, data and performance',
         'SCADA and metering data cleaned, joined and compared in Python and Excel; availability, downtime causes '
         'and production against expectation turned into views that operations, service providers and management '
         'use — and the basis for continuous optimisation of reliability and output across the portfolio.')]:
        m.bullet(label, body, after=25)

    m.models_table('TOOLS AND METHODS', ('Task', 'Tool and documented use'), [
        ('Electrical assets and HV',
         'Transformers, switchgear, protection, drives and motors in 24/7 operation; authorisation for LV, MV and '
         'HV; isolation, LOTO and safe switching as daily practice.'),
        ('Condition and maintenance',
         'Condition-based maintenance, criticality ranking, spare-part criticality against lead times, vibration '
         'and temperature as early indicators, shutdown scope built from the register.'),
        ('Data and platforms',
         'SCADA, meters and historian data; Python for data analysis — cleaning, joining and comparing — and Excel '
         'for the working model; KPI views for availability, downtime and energy.'),
        ('Commissioning and quality',
         'FAT/SAT, IQ/OQ/PQ, acceptance criteria and punch lists, change control before the change, as-built '
         'documentation and handover.'),
        ('Contractors and service providers',
         'Scope, SLA and reporting requirements set in the contract; failure reports and evidence requested '
         'rather than invoices; performance reviewed on the numbers.'),
        ('Reporting and economics',
         'Monthly reporting to management and customers; cost per unit, OPEX against CAPEX trade-offs, and '
         'business cases that survive being questioned; SAP and Excel daily.')])

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director',
         'ELOHVAC ApS · Copenhagen · May 2023–present',
         '5 technicians and 3 apprentices · full P&L · private and commercial customers',
         [('Commercial and technical',
           'Panels, drives and control systems specified, installed, tested and handed over; budget, pricing and '
           'supplier terms owned end-to-end, with the customer informed the same day something changes.')]),
        ('Senior Commissioning Engineer / Project Manager, Electrical Systems',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · 2–10 million DKK each · GMP/FDA/EMA',
         [('Commissioning and handover',
           'FAT/SAT, IQ/OQ/PQ and acceptance criteria across 37 projects; zero critical findings at audit, and '
           'assets handed to operations with documentation that matched the installation.'),
          ('Shutdowns and contractors',
           'Contractors supervised through fixed production stops; interfaces to other trades and suppliers held '
           'to scope, sequence and quality.')]),
        ('Project and Workshop Manager',
         'Ventek-Air · Copenhagen · Jan 2022–Nov 2022',
         '14 employees · 11 concurrent jobs · 2–10 million DKK per job',
         [('Delivery under pressure',
           'Daily board meetings, bottleneck analysis and re-prioritisation across 11 concurrent jobs; deliveries '
           'checked against acceptance criteria before they left the workshop.')]),
        ('Operations and Maintenance Manager',
         'Lynetten under Biofos · Copenhagen · Aug 2017–Jan 2022',
         'Process plant in 24/7 operation · pumps, blowers, ventilation, transformers, switchgear, drives and SCADA',
         [('Operations, people and condition',
           'Shift planning and daily leadership of operations staff; condition-based maintenance and live fault '
           'history with the plant running through it.'),
          ('HV, contractors and performance data',
           'Transformers, switchgear and protection maintained under permit and isolation discipline; contractors '
           'and authority requirements managed in a plant that could not stop; energy management on metering and '
           'SCADA data with over 40 % lower consumption, documented and sustained.')]),
        ('Electromechanical Technician / Production Supervisor',
         'ARJ Engineering · Tehran · Dec 2003–Mar 2010',
         '12 mechanics and technicians · machine workshop · industrial equipment',
         [('Uptime and root cause',
           'Shift planning and follow-up on targets; fault finding, root cause analysis and corrective actions on '
           'production equipment.')]),
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

    m.section('LANGUAGES, PRACTICAL AND REFERENCES')
    m.para('Danish: native · English: professional · Persian: native · Driver\'s licence B · Based in Måløv, '
           'Hobro around three hours away, weeks planned around office and sites · Ready to complete the full '
           'GWO package · Available by agreement · SAP and Excel daily, Python for data work · References on '
           'request.', after=70)

    m.models_table('WHAT THE ROLE ASKS FOR — MY EVIDENCE', ('Requirement', 'Evidence'), [
        ('A technical education',
         'Authorised machine and electrical installer (LV/MV/HV) with a B.Tech in Technology Management & '
         'Mechanical Engineering; 20+ years in technical operations and maintenance.'),
        ('Experience within asset management',
         'Asset base of pumps, blowers, ventilation, transformers, switchgear, protection and drives managed in '
         '24/7 operation for five years; asset registers, condition, criticality and cost per unit as the '
         'working model.'),
        ('Wind, BESS, PV and HV',
         'HV, MV and LV assets owned and maintained under authorisation: transformers, switchgear, protection, '
         'drives and grid connection, plus commissioning of electrical systems in 37 projects. Asset performance '
         'is the same discipline on any generating asset, renewable energy parks included: availability, '
         'production against curve, downtime and cost per MWh — applied to a different prime mover.'),
        ('A hands-on mindset, strong toolbox, autonomous end-to-end',
         'Fault finding on site as well as in the data; panels, drives and control systems installed and tested '
         'personally; 37 projects taken from scope to audited handover, and full P&L since 2023 — technical '
         'topics owned from identification to closed action.'),
        ('Troubleshooting, root cause analysis and incident handling',
         'Root cause discipline built in a plant that could not stop: measurements and history first, corrective '
         'action documented, and follow-up that confirms the failure has not returned.'),
        ('Planning and coordinating major maintenance and shutdowns',
         'Condition-based maintenance and shutdown scope in 24/7 operation; contractors supervised through fixed '
         'production stops, with one plan, one sequence and one daily coordination.'),
        ('Commissioning and integration of new assets',
         'FAT/SAT, IQ/OQ/PQ, acceptance criteria, punch lists and handover in 37 projects with zero critical '
         'findings; new assets integrated with alarm lists, documentation and data that agree.'),
        ('Operational data, monitoring platforms and technical reporting',
         'SCADA and metering data analysed in Python and Excel; availability, downtime causes and production '
         'against expectation turned into views that are used; monthly reporting to management, customers and other '
         'stakeholders, with the numbers documented so an investor question can be answered line by line.'),
        ('English, driver\'s licence (B), travel, service providers',
         'English professional in international project environments; licence B and ready to travel to parks a '
         'few times a year; service providers and contractors steered by scope, SLA and reporting requirements '
         'rather than by invoice.')])
    m.page_break()

    m.models_table('FIRST 90 DAYS — THE REGISTER, THE CAUSES AND THE DATA', ('Period', 'What happens, and how it is measured'), [
        ('Week 1–2',
         'Read the portfolio and the contracts: which parks, which asset types, which service agreements, which '
         'numbers are reported today and to whom. Out on site with the surveillance team and with a service '
         'provider while they work.'),
        ('Day 30',
         'A one-page asset view per park — availability, downtime causes, production against expectation, open '
         'incidents and their age. The technical topics with the highest cost or repetition ranked, and the first '
         'two taken as owner.'),
        ('Day 60',
         'Two or three recurring failures taken to root cause with documented corrective actions; alarm and '
         'parameter conventions compared across sites; the maintenance campaign and the next shutdown scoped '
         'backwards from the date.'),
        ('Day 90',
         'A portfolio view that the team, the service providers and management read the same way; repeat failures '
         'falling, downtime causes named rather than summarised, and at least one technical improvement '
         'documented before and after so it can be defended to an investor.')])

    m.section('AN ASSET IS ONLY AS GOOD AS ITS NUMBER')
    m.para('A portfolio of parks produces an enormous amount of data and very little information unless someone '
           'decides in advance what is being measured. Availability without the definition behind it is a '
           'number that can be argued about; production without the expected curve is a number without a '
           'verdict. My first job in any asset organisation is to make those definitions explicit and '
           'comparable across sites, so that a weak asset shows up as a fact and not as an opinion in a meeting.', after=80)

    m.section('AN INCIDENT IS CLOSED WHEN THE CAUSE IS')
    m.para('The expensive incident is rarely the first one. It is the same one, three months later, with a '
           'different work order number. Closing an incident properly means evidence before action: what the '
           'data showed before the trip, what was found on site, what was changed, and how we will know it '
           'worked. It also means writing it down while it is happening, because a fault history reconstructed '
           'from memory is worth very little when the manufacturer asks a hard question about warranty.', after=80)

    m.section('SHUTDOWNS ARE PLANNED BACKWARDS')
    m.para('An outage window is the most valuable hour a technical organisation has, and it is decided weeks '
           'before it starts. Scope that needs the turbine stopped, spare parts with the right lead time, crews '
           'and permits, service providers on the same sequence, and the grid side agreed — all in one plan, '
           'with a named owner per line. If the plan is built forwards from what people happen to be free to do, '
           'the window is used on the easy work and the expensive work waits another year.', after=80)

    m.section('DATA NOBODY USES IS NOT MONITORING')
    m.para('A dashboard nobody opens is a cost, not a control. Monitoring earns its place when it changes what '
           'someone does on Monday: this string is underperforming against its neighbours, this converter has '
           'tripped four times in a month, this temperature is drifting. That means alarm rationalisation, '
           'parameters with the same meaning on every site, and reports short enough to be read. The same '
           'discipline makes investor clarification easy — the number is already defined, the trend is already '
           'there, and the answer takes minutes instead of a week of digging.', after=80)

    m.section('COMMISSIONING IS WHERE THE COST IS DECIDED')
    m.para('Most of the lifetime cost of an asset is set before it enters operation: what was tested, what was '
           'documented, what was left on a punch list and forgotten. I run commissioning as a set of acceptance '
           'criteria rather than a sequence of visits — FAT before it ships, SAT on site, the functions proven '
           'against the specification, the alarm list agreed with operations, and the documentation handed over '
           'in a state that someone can actually use two years later. That is also where a new park or a new '
           'turbine type stops being a project and becomes an asset in the portfolio.', after=80)

    m.section('THE COMMERCIAL CASE IS A TECHNICAL DECISION')
    m.para('A technical recommendation without a price is a preference. I have carried a P&L and negotiated '
           'supply and service contracts, so I know what a day of downtime costs and what a spare part in stock '
           'costs to sit there. The question I ask in every asset decision is the same: what does this buy, '
           'what does it cost, and what is the probability it is needed? That is the balance this role is asked '
           'to hold, and it is the one I am most comfortable defending to a manager, a service provider or an '
           'investor.', after=80)
    m.section('THE TEAM IS THE ASSET THAT DOES NOT APPEAR IN THE REGISTER')
    m.para('A technical asset organisation runs on people who are allowed to say what they actually think about '
           'a machine. I lead by being specific — what we know, what we do not know yet, and who does what by '
           'when — and by making sure the person who finds the problem gets the credit for it. Eurowind writes '
           'that it wants people to speak up and to grow; in my experience that is built by what a manager does '
           'with the first inconvenient piece of information he receives, not by what is written about culture.',
           after=80)

    return m.save(path, title='Technical Operations Manager — Eurowind Energy, Technical Asset Performance DK',
                  subject='Asset performance, HV infrastructure, operations data and commissioning',
                  keywords='technical asset management, asset performance, HV, switchgear, transformers, SCADA, '
                           'root cause analysis, maintenance, shutdowns, commissioning, renewable energy, data')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Eurowind_TechnicalOperationsManager.docx')))
