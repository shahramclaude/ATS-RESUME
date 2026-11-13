# -*- coding: utf-8 -*-
"""Advansor A/S (Dover Food Retail / Dover Corporation) — Technical Support Manager,
Aftersales, Brabrand/Aarhus. Requisition JR102696.

English posting -> English document (en-GB), per master/README.md rule 1.

Form (master/FORMKATALOG.md): opening **M** (the loss: a rack that stops on a
Saturday does not cost a service technician, it costs a display case full of
food), structure **The route of a case** (the call · the diagnosis · the claim ·
the commissioning · the learning), register **The Rack** (rack, gas cooler,
compressor, discharge pressure, alarm, controller, refrigerant). Culture file:
jd/Advansor_TechnicalSupportManager_kultur.txt. User decision 13.11.2026: the
document is in English; he relocates for the role.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Technical Support Manager, Aftersales · team, claims and commissioning'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('13 November 2026')
    m.meta('Advansor A/S · Brabrand, Aarhus · requisition JR102696 · via Dover Workday')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Technical Support Manager, Aftersales', bold=True, color='1A1A1A')

    def lp(text, after=60):
        return m.para(text, after=after, line=236)

    # ---------------------------------------------------------------- page 1
    lp('**A rack that stops on a Saturday does not cost a service technician. It costs a display case '
       'full of food.** That is the clock your six Aftersales Engineers are actually working against, '
       'and it is the one the customer reads: not our response time in a system, but how long the '
       'chilled goods were off temperature. With **18 of Europe\'s top 20 retailers** running Advansor '
       'racks, and with **"customers in over 30 countries"**, one call that waits until Monday is a '
       'loss that travels further than the shop it started in.', after=56)

    lp('**Advansor is number one in a refrigerant the rest of the industry is still learning.** Since '
       '2006 you have built more than 20,000 CO2 systems, you are a **"market-leading OEM '
       'manufacturer"** with production in Brabrand, and CO2 has moved from technical experiment to '
       'the standard choice in European food retail. That is exactly why the support function carries weight: '
       'the technology is settled, so what the customer experiences is decided by how fast and how '
       'consistently six engineers, a claims process and a commissioning calendar answer. That is a '
       'leadership job with a screwdriver in the drawer — and I have done both halves. Your own aim is '
       '**"the best customer support"**; the line above it, **"driving both team motivation and '
       'performance"**, is what makes it repeatable.', after=56)

    lp('**One case has five stations.** The call, the diagnosis, the claim, the commissioning and the '
       'learning. I would manage the team by those five, because each one has its own failure mode — '
       'and only one of them is about technical knowledge.', after=44)

    lp('**The call.** Availability is a rota and an escalation path, not a promise. Who answers in '
       'Danish, who answers in English, who is second line at 16:30 on a Friday, and what happens when '
       'the third call in an hour is about the same alarm. I ran a 24/7 duty for five years at '
       'Lynetten, where the alarm did not care that it was Christmas, and I know that availability is '
       'built the week before, not the night it is needed.', after=40)

    lp('**The diagnosis.** Six engineers must reach the same answer from the same symptoms — otherwise '
       'the customer gets six truths. That is a method, written down: pressure and temperature at the '
       'gas cooler, what the controller logged, what changed since the last service visit, and which '
       'three causes account for most of it. I have read PLC and SCADA logs for twenty years; the '
       'medium being CO2 rather than water changes the numbers, not the discipline.', after=40)

    lp('**The claim.** **"Claim handling"** is not a complaint inbox. It is a cost that has to be '
       'explained: what failed, what it cost, who pays, and what stops it happening again. I have '
       'carried warranty and guarantee obligations under **AB 18** in my own company and settled '
       'disputes with suppliers and customers — including the ones where the honest answer was that we '
       'were wrong.', after=40)

    lp('**The commissioning.** **"Commissioning coordination"** across borders is a calendar problem '
       'before it is a technical one: the engineer, the customer, the site, the interpreter and the '
       'start-up window in the same week. At Novo Nordisk I commissioned 37 capital projects with '
       'FAT/SAT and IQ/OQ/PQ and handed every one of them over with zero critical deviations — the '
       'checklist is what makes a start-up repeatable when the person who wrote it is not there.', after=40)

    lp('**The learning.** A failure that happens twice is not a support case, it is a process problem '
       '— and it belongs in R&D, in Sales Engineering and in the installation instructions. That is the '
       'part of **"process optimisation"** that pays: fewer calls, shorter diagnoses, and a claim '
       'frequency that goes down instead of sideways. I have worked that loop with 25 specialists and '
       '37 projects, and I would bring the numbers to the monthly review rather than the anecdotes.', after=56)

    lp('**What I do not have, stated plainly.** I have not worked with transcritical CO2 racks, and I '
       'have not run an OEM helpdesk with tickets from thirty countries. I have a refrigeration '
       'background — køle- og ventilationsteknik from AMU, service and installation of cooling and '
       'ventilation — and a maskinmester degree, which is the marine engineering degree you ask for. '
       'You offer training in CO2; I would spend the first month being trained harder than anyone else '
       'in the building, and I would come out able to take the Saturday call myself.', after=56)

    lp('**Why Advansor, in your own words.** You are **"a highly ambitious company"** with **"more '
       'than 350 competent colleagues"** of **"more than 35 different nationalities"**, and you say '
       'that the company **"values a good working environment, diversity, and teamwork"**. You are '
       '**"Part of the Dover Corporation"**, you were built on **"customer-centric innovation"** and '
       '**"FRESH THINKING"**, and you state the point of the whole business in one line: **"CO2 is the '
       'most climate-friendly refrigerant"** — **"non-toxic, non-flammable and does not affect the '
       'ozone layer"**. **"We know CO2 by heart"** and you have **"rock solid experience"**; what a '
       'support manager can add is **"a strong sense of responsibility to help our customers win"** — '
       'and, in your words, to **"help make a difference to the climate"** — at 07:00 on a Monday.', after=56)

    lp('**Practical.** I live in Måløv today and I am ready to relocate, so my working week is in '
       'Brabrand rather than on the motorway. English is my working language with customers and '
       'suppliers, Danish is my first, and Persian is my mother tongue. Available after agreement; '
       'references on request.', after=24)

    m.meta('Kind regards', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('**Technical leader with refrigeration, commissioning and P&L behind him** — authorised '
           'maskinmester (LV/MV/HV), B.Tech in technology management and mechanical engineering, and '
           'refrigeration and ventilation technology from AMU. More than twenty years of technical '
           'support, troubleshooting and service: **37 capital projects** commissioned with FAT/SAT and '
           'IQ/OQ/PQ, **11 simultaneous site projects** with 14 people, 12 technicians in a machine shop '
           'and eight employees in my own company since 2023. Leads teams of engineers and fitters, and '
           'answers the phone when the alarm goes off.', after=70)

    m.section('THE RACK — HOW I READ A SYSTEM')
    for label, body in [
        ('The pressures',
         'Discharge and suction pressure tell you what the rack is doing before the customer says a '
         'word; a **compressor** short of refrigerant and a blocked filter look the same on the phone '
         'until someone reads the numbers.'),
        ('The setpoint and the alarm',
         'What the controller was asked to hold, what it actually held, and when the alarm was raised '
         'versus when someone acted — three timestamps that separate a fault from a misconfiguration.'),
        ('The log',
         'The controller and **SCADA** log the sequence, not the story: what tripped first, what '
         'restarted, and what was reset by hand. I read logs for a living at Lynetten, 24/7.'),
        ('The last intervention',
         'What changed since the last service visit — a replaced sensor, a new setpoint, a door seal, a '
         'cleaning — because most "new" faults are old work coming back.'),
        ('The spare part',
         'Which component fails, how long it takes to arrive and what the customer loses while it does; '
         'the answer decides whether the case is a repair or an escalation.'),
        ('The repeat',
         'Every case is tagged with a cause, so the third identical claim in a month becomes a '
         'conversation with R&D and Sales Engineering instead of a fourth spare part.')]:
        m.bullet(label, body, after=16)

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director',
         'ELOHVAC ApS · Copenhagen · May 2023–present',
         '5 electricians and 3 apprentices · full P&L · contracting and service',
         [('Service agreements, warranty and claims',
           '**Service agreements**, **warranty** obligations under **AB 18**, **budget** and supplier disputes and '
           '**claim handling**; recruiting, **onboarding** and **coaching** of eight employees; **APV**, '
           '**LOTO** and safety in my own company.')]),
        ('Co-owner and CTO / Technical Lead, AI department',
         'Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 (alongside ELOHVAC)',
         '4–10 people · technical and industrial applications',
         [('Data in the support loop',
           '**KPI** models for response time, case volume and repeat failures; company has ceased '
           'trading.')]),
        ('Senior Commissioning Engineer / Project Manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · GMP/FDA/EMA',
         [('Commissioning and handover',
           '**FAT/SAT**, **IQ/OQ/PQ**, pressure testing and functional testing per component; zero '
           'critical deviations at handover, with **documentation** built as the work progressed.')]),
        ('Project and Workshop Manager',
         'Ventek-Air · Copenhagen · Jan 2022–Nov 2022',
         '14 employees · 11 simultaneous site projects',
         [('Capacity, interfaces and installation',
           '**HVAC** and **cooling** installations coordinated with subcontractors and suppliers; daily '
           'capacity plan for 11 sites and 14 fitters, re-prioritised the same day.')]),
        ('Operations and Maintenance Manager',
         'Biofos (Lynetten) · Copenhagen · Aug 2017–Jan 2022',
         'Wastewater plant in 24/7 operation · pumps, HV switchgear, SCADA',
         [('24/7 operation and energy',
           'On-call duty, **troubleshooting** and root-cause work around the clock; **over 40 % lower '
           'energy consumption** through measurement and re-commissioning.')]),
        ('Electromechanical Technician / Production Team Lead',
         'ARJ Engineering · Tehran · Dec 2003–Mar 2010',
         '12 technicians · machine shop · machinery and equipment',
         [('Machines, maintenance and training',
           'Fault finding, calibration and repair of machines; purchasing and maintenance of equipment; '
           'training and follow-up for 12 technicians.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=16)

    m.section('EDUCATION AND AUTHORISATION')
    m.edu('B.Tech, Technology Management and Mechanical Engineering',
          'Copenhagen School of Marine and Technical Engineering · 2017–2022 · GPA 7.6/12')
    m.edu('Authorised maskinmester (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('Refrigeration and ventilation technology · AMU',
          'Mercantec 2021 · STCW, Danish Maritime Authority 2021')
    m.edu('Electrical and mechanical engineering design, electrical engineering',
          'Tehran Technical University · 2000–2003 · EQF 6')

    m.section('LANGUAGES, IT AND PRACTICAL')
    m.para('English (working language with customers and suppliers) · Danish (first language) · '
           'Persian (mother tongue) · **IT**: **MS Office** with **Excel** models for **KPI**, case '
           'volumes and capacity; **ERP** and **CRM**/ticketing work; **SCADA**, **PLC** and controller '
           'log reading; own **Python** tools for data · **Driving licence B and own car** · Ready to '
           'relocate for the role · Available after agreement · References on request.', after=50)

    m.models_table('THE ROLE AS ADVERTISED — WHAT I BRING', ('Requirement', 'Evidence'), [
        ('Lead the Technical Support Team at HQ, keeping motivation and performance high',
         'Led 25 specialists across 37 parallel projects, 14 fitters on 11 sites, 12 technicians and '
         'eight employees in my own company — one-to-ones every week and a written standard for '
         '"done".'),
        ('Coordinate the Aftersales Engineers outside Denmark',
         'Twenty years of coordinating engineers, subcontractors and suppliers: 11 simultaneous '
         'projects at Ventek-Air and 37 capital projects with consultants and contractors.'),
        ('Deliver consistent, efficient technical support',
         'One diagnostic method, written down, so six engineers reach the same answer: pressures, '
         'setpoint, log, last intervention, spare part, repeat cause.'),
        ('High availability and quick response times',
         'Five years of 24/7 on-call duty at Lynetten: rota, escalation path and a second line named '
         'before the shift started — and an **SLA** we could actually keep, not one we hoped for.'),
        ('Troubleshooting of technical issues raised by customers',
         'Twenty years of fault finding on electrical, mechanical and control systems — from relay '
         'logic in a machine shop to HV switchgear and SCADA.'),
        ('Claim handling',
         '**Warranty** obligations under **AB 18**, supplier disputes and customer settlements in my '
         'own company since 2023 — including the cases where we were at fault.'),
        ('Technical issue resolutions end to end',
         'Case closed only when the cause is tagged and the customer has the fix in writing — the '
         'discipline behind zero critical deviations at handover on 37 projects.'),
        ('Oversee commissioning coordination with customers world-wide',
         '**FAT/SAT**, **IQ/OQ/PQ**, pressure testing and functional testing on 37 capital projects; '
         'commissioning plans written so a start-up could be repeated by someone else.'),
        ('Continuously improve daily operations and support processes',
         'Process work with numbers attached: response time, cases per engineer, repeat claims — '
         'reviewed monthly and changed when the number moves.'),
        ('Optimise claim handling for greater efficiency',
         'Claim categories with cost per category, so the expensive 10 % becomes a design or '
         'installation conversation, not a recurring invoice.'),
        ('Work closely with Customer Support, Sales Engineering, R&D and Sales',
         'Interfaces are daily work: technical sales and service at ELOHVAC; project, operations and '
         'quality at Novo and Lynetten; suppliers in both.'),
        ('Help provide solutions to customer challenges',
         'Solutions argued on the customer\'s economics, not the spec: over 40 % lower energy '
         'consumption at Lynetten came from measuring before recommending.'),
        ('Lead and support clarifications with customers on technical issues',
         'Technical clarifications in Danish and English for twenty years — with contractors, '
         'consultants, authorities and end customers, in writing and on site.'),
        ('Effective troubleshooting and timely solutions',
         'A time box on every diagnosis: what we know now, what we test next, and when the customer '
         'hears from us again — even when the answer is that we do not know yet.'),
        ('5+ years leadership experience in technical or customer support management',
         '**Team leadership** since 2003: production team lead for 12 technicians, operations manager '
         'for five years, project manager for 14 fitters, and owner with **budget** and P&L for eight '
         'employees.'),
        ('Degree in refrigeration, marine engineering, electrical engineering or similar',
         '**Authorised maskinmester** — the Danish marine and technical engineering degree — with '
         'B.Tech in technology management and mechanical engineering, GPA 7.6/12, and an electrical '
         'authorisation (LV/MV/HV).'),
        ('Strong understanding of refrigeration technology',
         'Refrigeration and ventilation technology (AMU, Mercantec 2021) plus practical service and '
         'installation of cooling and HVAC systems; heat pumps and process cooling in service work.'),
        ('Experience with CO2 as a refrigerant — advantage, training offered',
         'Not yet. I know refrigeration on HFC and water-based systems and the physics it shares with '
         'CO2; I would take the training you offer and be able to cover a Saturday call within the '
         'first months.'),
        ('Proactive, structured approach with strong organisational skills',
         'Structures that survive a bad week: one board, one list, one status per project — 37 '
         'projects in GMP and 11 sites in contracting, in the same format.'),
        ('Time management and multiple tasks simultaneously',
         '11 simultaneous site projects with 14 people and three stakeholders each, re-prioritised '
         'every morning; nothing waited for a meeting to be decided.'),
        ('Strong communication skills, verbal and written, in English',
         'English is my working language with suppliers, consultants and customers; documentation, '
         'procedures and training material written for the people who have to use them.'),
        ('Danish not required; additional languages a plus',
         'Danish native, English professional, Persian mother tongue — three languages in a support '
         'team that talks to customers in more than thirty countries.'),
        ('Customer-centric mindset with a sense of urgency',
         'The clock is the customer\'s, not the ticket\'s: a rack off temperature at a retailer is '
         'handled in minutes, and the customer is told what happens next before they ask.'),
        ('Report directly to the Aftersales Manager',
         'Reported to directors and owners in my own company and to project and operations management '
         'in a global group; short written updates, decisions requested, no surprises.'),
        ('Deliver world-class service and support',
         '**Customer satisfaction** built on the boring things: response times kept, documentation '
         'complete, and the same answer from whoever is on duty.'),
        ('Contribute to sustainable CO2 climate solutions',
         'Twenty years in energy and refrigeration where the saving was the product — over 40 % lower '
         'energy consumption at Lynetten, and a working week spent on systems that keep food cold '
         'with the least possible climate impact.'),
    ])

    m.section('FIRST 90 DAYS')
    for b in (
        'Weeks 1–2: sit with each of the six engineers and listen to ten of their live cases; read the '
        'claim history and the commissioning calendar without changing anything.',
        'Weeks 3–6: one written diagnostic standard and one escalation path, tested on real cases; CO2 '
        'training started and logged.',
        'Months 2–3: claim categories with cost per category, and a monthly review with R&D and Sales '
        'Engineering on the three most expensive repeats.',
        'Month 3: response times and repeat rate published monthly, and the first process change made '
        'because the number said so.'):
        m.bullet('', b, after=16)

    m.models_table('HOW I WOULD MEASURE THE ROLE', ('Measure', 'How it is read'), [
        ('Response time',
         'First qualified answer per case, measured from the customer\'s call, not from when the '
         'ticket was assigned.'),
        ('First-time fix',
         'Cases closed without a second visit or call — the fastest way to free capacity in a team of '
         'six.'),
        ('Repeat claims',
         'Cases per cause per quarter; a growing cause goes to R&D, not to spare parts.')])

    m.section('WHAT I WOULD ASK')
    for b in (
        'How many cases per week does the team handle today, and what share of them are claims rather '
        'than support?',
        'Where do the cross-border cases hurt most — language, time zones, or spare parts on the way?',
        'Is the diagnostic knowledge in the team\'s heads today, or is it written down anywhere?'):
        m.bullet('', b, after=16)

    m.para('**I would be glad to visit Brabrand** and sit with the team for an afternoon before we '
           'talk about the role — the questions get better when they are asked in the room. Contact: '
           '+45 93 99 95 14 · ajlooshahram@gmail.com.', after=24)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Advansor_TechnicalSupportManager.docx')
    build(out)
    print(out)
