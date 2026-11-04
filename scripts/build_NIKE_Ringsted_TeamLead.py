# -*- coding: utf-8 -*-
"""NIKE, Inc. — Team Lead, NIKE Ringsted (Factory Store, Ringsted Designer Outlet).

English deliverable (JD is English): task-first cover page + CV in one document.
Culture and role intel: master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md,
section on NIKE Ringsted (research 04.11.2026).
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Team leadership · Coaching, standards and service performance'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('4 November 2026')
    m.meta('NIKE, Inc. · NIKE Ringsted, Klosterparks Alle 81, 4100 Ringsted · Team Lead (R-96671)')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Team Lead — NIKE Ringsted', bold=True, color='1A1A1A')
    m.para('Dear Store Leadership Team', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('A factory store is judged before anyone says a word. Whether the size run is complete, whether the wall '
           'is set the way it was planned, whether someone greets you within the first few seconds, and whether the '
           'price on the shelf is the price at the till. The Team Lead role is about making that standard repeatable '
           'on every shift — and coaching a team so it holds on the days when the lead is not standing next to them.',
           after=80)

    m.para('**The system I would run is simple enough to survive a Saturday.** One page of floor standards, walked '
           'in fifteen minutes before opening: size runs complete, replenishment done, new lines set to the visual '
           'plan, promotional prices correct, fitting rooms clear. A ten-minute huddle before every shift with one '
           'focus metric and one product story, so the team knows what today is about and what to say about the '
           'shoe. Observation-based coaching instead of general encouragement: I watch the interaction, and I give '
           'feedback on what worked and what to change next time, in the moment and again in a 1:1. And a weekly '
           'cycle count plus receiving discipline, because inventory accuracy is not paperwork — it is the reason a '
           'consumer finds their size or leaves without it.', after=80)

    m.para('The numbers that tell me whether it works are the ones the store already lives by: conversion, units per '
           'transaction, member sign-ups, share of digital orders placed or collected in store, inventory accuracy, '
           'shrink, and how quickly a delivery reaches the floor. I would schedule against the traffic curve rather '
           'than against habit, so the strongest service sits where the consumers actually are — and so the team is '
           'not asked to do three things at once at 14:00 on a Sunday.', after=80)

    m.para('What I bring is more than fifteen years of leading teams where the standard is visible to a customer and where '
           'getting it wrong has a cost. I have had personal responsibility for five electricians and three '
           'apprentices — daily planning, 1:1s every two weeks, performance reviews, a competence matrix and '
           'training that ends with someone being able to do something they could not do before. I have led 25 '
           'specialists through 37 parallel capital projects without formal authority over any of them, and a '
           '14-person team through eleven simultaneous builds. I have worked shift patterns with nights, weekends '
           'and public holidays on a 24/7 plant, run warehouse and spare-parts flow with 5S and standard work, and '
           'for the past three years I have run my own company with full P&L, quoting, pricing and direct customer '
           'dialogue. Service agreements with response time and quality as KPIs taught me the same thing a sales '
           'floor teaches: a promise is only worth the delivery behind it.', after=80)

    m.para('I will also be straight with you: this would be my first role in retail. I have not been a keyholder, built a '
           'visual merchandising plan or run a launch weekend on a shop floor. What I have is the part that is hard '
           'to teach — coaching adults under pressure, keeping a standard when the store is full, and owning the '
           'result rather than the excuse — plus a plan for the first ninety days: learn the floor and the systems '
           'in the first two weeks, take ownership of one business area by day 30 with a working floor standard, '
           'run the first full monthly initiative launch by day 60, and by day 90 show a measurable movement in '
           'conversion, inventory accuracy or member sign-ups with a development plan for every teammate.', after=80)

    m.para('The reason I want this particular store is the brand behind it. **Serve Athletes**, **Do the Right '
           'Thing**, **Win as a Team**, **Create the Future of Sport** — in a store those four are not posters, they '
           'are behaviour: you serve the first-time runner and the sub-3 marathoner with the same attention, you '
           'follow the standards even when nobody is checking, you cover for a colleague before you are asked, and '
           'you try the new way of doing the morning routine instead of defending the old one. And the line I like '
           'best — *if you have a body, you are an athlete* — is also the simplest test of a team: does every '
           'consumer who walks in get treated as an athlete, whatever they are wearing and whatever they can spend?',
           after=80)

    m.para('Practically: I live in Måløv, about 50 minutes by car from Klosterparks Alle, so no relocation is needed, '
           'and evenings, weekends and holidays are part of the job I am applying for — I have done shift work for '
           'years. I speak Danish natively, English professionally and Persian, which is useful in a store with '
           'international guests. I am also an active Claude coder and build my own tools in Python for planning, '
           'KPI follow-up and simple sales analysis — AI tools that shorten a report from an hour to five minutes and '
           'give the floor more time with consumers.', after=80)

    m.para('I would like to come to Ringsted, walk the floor with you and talk through how I would run the standard '
           'and the coaching in my first ninety days — and hear which of the three areas you need strongest first.',
           after=80)
    m.meta('Kind regards', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('Team leader with 20+ years of experience from technical service, projects and operations — personal '
           'responsibility for teams of 5–14, and cross-functional leadership of 25 specialists. Used to environments '
           'where a customer judges the result immediately and where standards, safety and stock accuracy are not '
           'optional. Coaches through observation, 1:1s and clear standards rather than instruction. Builds his own '
           'Python and Claude tools for planning, KPI follow-up and sales analysis.', after=80)

    m.section('LEADERSHIP AND RESULTS')
    for label, body in [
        ('Personal leadership',
         'Five electricians and three apprentices at ELOHVAC: daily planning, 1:1s every two weeks, performance '
         'reviews, competence matrix, onboarding and training, and workplace-safety follow-up.'),
        ('Leadership without formal authority',
         '25 specialised colleagues across 37 parallel capital projects at Novo Nordisk, and a 14-person team at '
         'Ventek-Air — direction, agreements and follow-up rather than instructions.'),
        ('Standards that hold',
         '5S, standard work and visual management on a 24/7 plant; a documented reduction in energy cost of 40 % '
         'through PDCA; zero critical deviations at handover under GMP/FDA/EMA.'),
        ('Service and sales',
         'Full P&L in his own company with quoting, pricing, margin follow-up and service agreements measured on '
         'response time, quality and delivery — with customer service and sales dialogue every day for three years.'),
        ('Digital and data',
         'Python and Claude tools for quotations, scheduling, quality checklists and KPI dashboards, with a measured '
         'productivity gain above 40 %. Builds investment models with NPV, IRR and scenarios for new business ideas.')]:
        m.bullet(label, body, after=30)

    m.models_table('TOOLS AND METHODS', ('Task', 'Tool and documented use'), [
        ('Coaching and development',
         'Situational Leadership (SLII), delegation ladder, 1:1s every two weeks, performance reviews, GROW and SBI '
         'feedback, competence matrix and a development plan per teammate. Apprentices trained to final trade test.'),
        ('Daily operations',
         'Pre-shift huddle with one focus metric, visual management board, standard work and checklists, Gemba walks '
         'and an escalation ladder with a named owner. Used in workshop, plant and project settings.'),
        ('Product flow and stock accuracy',
         'Receiving routines, cycle counts, spare-parts and warehouse flow, 5S on back-of-house areas, and deviation '
         'handling with an owner and a deadline. Root cause with A3 and 5 Whys.'),
        ('Sales and service performance',
         'Conversion and basket follow-up, traffic-based scheduling, service agreements with response-time KPIs, '
         'customer interviews and complaint follow-up. Pricing and margin work in own company.'),
        ('Quality and compliance',
         'Acceptance criteria, test cases, FAT/SAT and IQ/OQ/PQ, deviation logs and handover documentation. Zero '
         'critical deviations at handover; LOTO, risk assessment and APV in daily use.'),
        ('Brand and consumer journey',
         'Brand ambassador in practice: the athlete experience and the consumer journey from entrance to till set '
         'the standard, and visual merchandising and campaign material decide what the team shows and says.'),
        ('Communication and teamwork',
         'Stakeholder mapping and RACI, written decisions with owner and deadline, and feedback given so it can be '
         'used. Danish native, English professional.')])

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director / authorised marine and electrical engineer',
         'ELOHVAC ApS · Copenhagen, Denmark · May 2023–present',
         '5 electricians and 3 apprentices · full P&L · commercial and industrial customers',
         [('People and standards', 'Daily planning, 1:1s, performance reviews, competence matrix, safety follow-up '
                                   'and apprentice training; situational leadership across changing sites.'),
          ('Customers and sales', 'Quotations, pricing, margin follow-up and service agreements with response time, '
                                  'quality and delivery as KPIs; daily dialogue with customers about needs and '
                                  'solutions.'),
          ('Digital tools', 'Python and Claude API for quotations, schedules, quality checklists and KPI dashboard; '
                            'productivity gain above 40 % in the business.')]),
        ('Senior Commissioning Engineer / Project Manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd, Denmark · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · DKK 2–10m per project · GMP/FDA/EMA',
         [('Cross-functional leadership', 'Progress, cost, risk and resources across engineering, procurement and '
                                          'operations; stakeholder mapping and fixed decision points; monthly '
                                          'reporting to management and client.'),
          ('Test, quality and handover', 'FAT/SAT and IQ/OQ/PQ with zero critical deviations at handover; A3 and '
                                         '5 Whys in fault finding; a PDCA programme cut energy cost by 40 %.')]),
        ('Project and Workshop Manager',
         'Ventek-Air · Copenhagen, Denmark · Jan 2022–Nov 2022',
         '14 employees · 11 parallel construction projects · DKK 2–10m each',
         [('Delivery and ways of working', 'Tenders, quotations, subcontractors and handover packages. Daily board '
                                           'meetings and bottleneck analysis plus standardised work routines gave a '
                                           'clear lift in delivery performance.')]),
        ('Maintenance and Operations Manager / Workshop Technician',
         'Biofos, Lynetten · Copenhagen, Denmark · Aug 2017–Jan 2022',
         '24/7 operations · pumps, HVAC, high-voltage switchgear and SCADA · shift work',
         [('Operations, data and standards', 'Preventive maintenance, urgent fault finding and spare-parts flow on '
                                             'SCADA data; 5S, standard work and PDCA, plus LOTO, risk assessment '
                                             'and APV in shift operations.')]),
        ('Electromechanical Technician / Production Team Leader',
         'ARJ Engineering · Tehran, Iran · Dec 2003–Mar 2010',
         '12 mechanics and technicians · machine workshop',
         [('Planning, targets and learning', 'Shift planning, material control and target follow-up; fault '
                                             'diagnosis, root-cause analysis and corrective actions on industrial '
                                             'electrical and mechanical equipment.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        m.doc.paragraphs[-1].runs[0].text = 'Scope: '
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('EDUCATION AND CERTIFICATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering',
          'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · EQF 6 · GPA 7.6/12')
    m.edu('Authorised marine and electrical engineer (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('Electrical and mechanical design, electrical engineering',
          'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Lean practice: 5S, PDCA, VSM, A3, Kaizen', 'Ongoing courses and daily application in operations and projects')
    m.edu('Refrigeration and air conditioning · STCW safety and engine-room watch',
          'Mercantec 2021 · Danish Maritime Authority 2021–2023')

    m.section('LANGUAGES, PRACTICAL AND REFERENCES')
    m.para('Danish and Persian: native · English: professional, written and spoken · Driving licence B · Lives in '
           'Måløv, about 50 minutes by car from Ringsted Designer Outlet; relocation not required · Available for '
           'day, evening, weekend and holiday shifts · References from Novo Nordisk and Biofos on request.', after=70)

    m.models_table('WHAT THE ROLE ASKS FOR — MY EVIDENCE', ('Requirement', 'Evidence'), [
        ('Coordinate, coach and motivate teammates',
         'Personal leadership of 5 electricians and 3 apprentices with 1:1s, reviews, competence matrix and '
         'training; leadership of 25 specialists and a 14-person team without formal authority.'),
        ('Exceptional consumer service and premium brand experience',
         'Three years running a service business where response time, quality and delivery were the KPIs, and where '
         'the customer decided whether the work was good enough.'),
        ('Sales targets and product sales techniques',
         'Quotations, pricing, margin and upsell decisions in own company; service agreements built and renewed with '
         'customers; product training of colleagues and apprentices.'),
        ('Digital services and promotional campaigns',
         'Builds own digital tools and dashboards; used to launching and following up campaigns and product news in '
         'a commercial setting, with numbers attached to each.'),
        ('Receiving, inventory accuracy and visual presentation',
         'Spare-parts and warehouse flow, cycle counts, 5S and standard work on a 24/7 plant; deviations handled '
         'with owner and deadline. Visual merchandising is new to me.'),
        ('Store standards and compliance',
         'NIKE standards and guidelines would be the frame I hold the team to. Years of documented compliance '
         'under GMP/FDA/EMA, LOTO, risk assessment and APV; zero critical deviations at handover.'),
        ('Effective communicator and collaborative teammate',
         'Stakeholder mapping, RACI, written decisions and feedback that can be used; Danish native, English '
         'professional, Persian.'),
        ('Problem solving with store leadership',
         'A3 and 5 Whys as the default: describe the problem with data, find the root cause, agree the countermeasure '
         'and follow up on the effect. Used in GMP-regulated projects and in 24/7 operations.'),
        ('Flexible with retail hours',
         'Years of shift work with nights, weekends and public holidays on a 24/7 plant; available for day, evening, '
         'weekend and holiday shifts as a condition of the job, not a concession.'),
        ('Retail experience',
         'Not yet, and no keyholder experience. First retail role — offset by 15+ years of leading service teams, '
         'shift work including weekends and holidays, and a 90-day plan for learning the floor and the systems.')])
    m.page_break()

    m.models_table('FIRST 90 DAYS — FLOOR, PEOPLE, NUMBERS', ('Period', 'What happens, and how it is measured'), [
        ('Week 1–2',
         'Learn the floor, the stockroom and the systems: till, order-in-store, click and collect, member sign-up, '
         'replenishment routine. Work the hours the team works, including one full weekend. One 1:1 with every '
         'teammate: what they own, what they are good at, what gets in their way.'),
        ('Day 30',
         'A one-page floor standard in use, walked every morning before opening. One business area owned with clear '
         'responsibility for it. Baseline numbers for conversion, units per transaction, member sign-ups and '
         'inventory accuracy agreed with store leadership.'),
        ('Day 60',
         'First full monthly initiative launch run to plan: product story briefed at the huddle, wall and windows set '
         'to the visual plan, team coached on what to say. Weekly cycle count routine running; back-of-house 5S in '
         'place; development plan agreed with each teammate.'),
        ('Day 90',
         'Measured movement in at least two of the four numbers, a coaching routine that teammates describe as '
         'useful, and a written handover of what works in the area — so the standard does not depend on me being on '
         'the floor.')])

    m.section('THE FLOOR STANDARD I WOULD RUN')
    m.para('Standard before service. Fifteen minutes before opening, the floor is walked against one page: size runs '
           'complete in every key style, replenishment done, new lines set to the visual plan, promotional prices '
           'matching the till, fitting rooms clear, and the entrance ready. The walk has an owner per zone and a '
           'short list of what was fixed — not a general impression. The point is not to police people; it is that a '
           'consumer should never have to ask whether we have their size.', after=80)

    m.section('COACHING THAT SHOWS ON THE FLOOR')
    m.para('Coaching happens where the work happens. I observe a real interaction, then give feedback in SBI form — '
           'the situation, the behaviour, the impact — while it is still fresh, and we agree on one thing to try next '
           'time. Every shift starts with a ten-minute huddle: one focus metric, one product story, one recognition. '
           'Every teammate has a 1:1 every two weeks and a plan for what they want to be able to do in a year. That '
           'is how a team becomes good on the days when the lead is off the floor — and it is how people stay, which '
           'in retail matters more than any single Saturday.', after=80)

    m.section('PRODUCT FLOW, RECEIVING AND INVENTORY ACCURACY')
    m.para('A delivery is only useful once it is on the floor in the right place. Receiving gets a fixed routine: '
           'check against the delivery note, scan in, flag discrepancies the same day, and put the product where the '
           'plan says rather than where there is space. Cycle counts run weekly in a rolling pattern so problems '
           'surface early, and the stockroom follows 5S: everything has a place, and the place is marked. Shrink and '
           'accuracy are managed with the same discipline I used on spare-parts flow at a 24/7 plant, where a missing '
           'part meant a stopped process.', after=80)

    m.section('DIGITAL SERVICES AND MEMBERSHIP')
    m.para('Digital services only work if the team uses them naturally. I would make member sign-up, order-in-store '
           'and click and collect part of the conversation rather than a script at the till: if the size is not on '
           'the shelf, we find it; if the colour is online only, we order it; if the consumer is training for '
           'something, membership gives them a reason to come back. I would follow the share of digital orders and '
           'new members weekly with the team, because what gets looked at gets done.', after=80)

    m.section('TEAM CULTURE, WELLBEING AND RETAIL HOURS')
    m.para('A store team works hard hours in a small space, and the rota is where respect is shown. I plan against '
           'the traffic curve, publish the schedule early, cover breaks properly and keep the promises I make about '
           'time off — including in December. Feedback is given in private and credit in public. And when a shift '
           'goes wrong, we look at the process before we look at the person: that is how a team dares to say that '
           'something is not working, which is exactly when it can still be fixed. Diversity, equity and inclusion '
           'is not a programme on a wall in a store — it shows in who gets trained, who gets the good shifts and '
           'whose idea is tried.', after=80)

    m.section('WHAT I BRING FROM OUTSIDE RETAIL')
    m.para('Nearly two decades in environments where a customer is waiting and the standard is visible: technical service, '
           'construction projects and 24/7 operations. From that I bring three habits that transfer directly — a '
           'written standard instead of verbal expectations, numbers followed weekly rather than quarterly, and '
           'training that ends with someone doing the task alone. I am also an active Claude coder and build my own '
           'Python tools for planning, KPI follow-up and sales analysis; used with care, that is time moved from '
           'spreadsheets to the floor.', after=80)

    return m.save(path, title='Application and CV — Team Lead, NIKE Ringsted',
                  subject='Team leadership, coaching and service performance in a factory store',
                  keywords='team lead, retail, consumer service, coaching, sales floor, inventory accuracy')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_NIKE_Ringsted_TeamLead.docx')))
