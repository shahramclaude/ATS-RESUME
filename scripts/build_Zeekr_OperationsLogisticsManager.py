# -*- coding: utf-8 -*-
"""Zeekr (Geely) — Operations & Logistics Manager, Copenhagen. English posting -> English document.

Form (master/FORMKATALOG.md): opening **X** (the error before it became expensive — the one place
in the chain where a mistake is still cheap), structure **Five contracts** (the provider · the
terminal · the preparation · the dealer network · the transport leg — plus the plan you cannot write
a contract for), register **The Quay** (quay, vessel, terminal, gate-out, VIN, PDI, prep, transport
damage, storage, registration).
Culture file: jd/Zeekr_OperationsLogisticsManager_kultur.txt. No deadline — ongoing selection.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Operations & Logistics Manager · P&L, supply chain and operational turnaround'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('14 November 2026')
    m.meta('Zeekr EU · Sales and Commercial Operations · Operations & Logistics Manager · Copenhagen')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Operations & Logistics Manager', bold=True, color='1A1A1A')

    def lp(text, after=40):
        return m.para(text, after=after, line=234)

    # ---------------------------------------------------------------- page 1
    lp('**There is one place in a vehicle supply chain where a mistake is still cheap: on the quay, before the '
       'car is registered, before it is prepared, before the customer has seen it.** Ten metres further down '
       'the chain the same mistake becomes a workshop booking, a re-registration, a discount — or a customer '
       'who tells the story for years. Most of this job is deciding where those points are, putting a check '
       'there, and making the check cheap enough that nobody skips it.', after=36)

    lp('I have spent twenty years building that discipline in technical operations, where an error is '
       'expensive and the only defence is a gate somebody owns — and since 2023 I have run it with **my own '
       'money at risk**: full **P&L**, purchasing, price, capacity and delivery in one hand. Your chain runs '
       '**"from vehicle importation and distribution to dealer deliveries"**, and **"operational excellence '
       'across the entire supply chain"** is exactly the discipline I know how to install. What I do not bring '
       'is the automotive chain itself — that is stated plainly below.', after=36)

    lp('**Five contracts. Each has a promise, a number that proves it, and a way of failing.**', after=26)

    lp('**1. The logistics provider.** Lead time and **delivery precision** in the contract, damage and '
       'demurrage priced, and a monthly review with the numbers rather than the anecdotes. In my own company '
       'every supplier term — price, lead time, service, who carries the risk — is negotiated, because a late '
       'subcontractor is my loss.', after=22)

    lp('**2. The terminal.** Storage days, **gate-out**, keys, **VIN** control, security, and the cost of a car '
       'that sits still. A compound is working capital with weather on it: every extra day of **storage** is '
       'money that has already been spent once.', after=22)

    lp('**3. The preparation.** Throughput, first-time-right and rework — the **PDI** is the last cheap gate '
       'before the dealer. My acceptance discipline comes from **FAT/SAT** and **IQ/OQ/PQ**: the criteria are '
       'agreed before the unit arrives, and nothing is signed on trust.', after=22)

    lp('**4. The dealer network.** Allocation rules that are written down, an ordering discipline both sides can '
       'live with, and a **delivery** promise the network believes. 37 handovers with zero critical deviations '
       'taught me that a promise kept once buys the next three orders.', after=22)

    lp('**5. The transport leg.** Damage rate, ETA accuracy and cost per unit — and one owner for the '
       'hand-over point where a transporter\'s responsibility ends and ours begins. Eleven sites and 14 fitters '
       'moving at once is where I learned to make that point explicit.', after=30)

    lp('**And the one you cannot write a contract for: the forecast.** Allocation and supply planning with '
       'Sales and Regional Supply is a negotiation about **working capital** as much as about cars — the '
       'difference between a healthy pipeline and a yard full of the wrong specification is one honest '
       'planning meeting a month.', after=34)

    lp('**Where my record is thinner, stated plainly.** I have no automotive background, no vehicle logistics '
       'and no experience with the **Danish Luxury Tax** or registration regime, and I have not run a dealer '
       'network. What I bring instead is the operating core of the role: full **P&L** and **budget** '
       'ownership since 2023, supplier negotiation, inventory and capacity planning, **Lean** and **Six Sigma** '
       'methods in practice, a **digital transformation** delivered (AI in estimating, documentation and '
       'reporting, **over 40 % productivity gain** measured), and team leadership from 8 to 25 people. The '
       'automotive vocabulary I would learn in weeks; the discipline of a gate that somebody owns takes years '
       'to build, and I have built it three times.', after=32)

    lp('**Why Zeekr, in your words.** A **"premium electric vehicle and technology solutions brand"** from '
       'Geely, founded in Europe in 2023 with **over 160 colleagues**, aiming to **"accelerate the shift to '
       'fully electrified mobility"** with a **"customer-centric approach"** — and with the ambition that '
       'operations should deliver **"sustainable business growth and customer satisfaction"**. You are asking '
       'for **"both strategic leadership and hands-on execution"**, **"a trusted advisor to the Country '
       'Director"** who can **"drive operational scalability"** and **"establish performance metrics and '
       'governance processes"** — '
       'which is another way of saying: build the operating system of a young company while it grows. That is '
       'the work I have done in a company of eight and in project organisations of 37 parallel builds, and it '
       'is what attracts me: **"ongoing selection"** means the market decides, and I would rather be measured '
       'than described.', after=30)

    lp('**On the culture and the process.** You ask for **"the courage to lead with trust and care"** and for '
       'someone who does not mind **"getting your hands dirty"**, in an **"international and multicultural '
       'environment"** where people **"embrace the diversity of people, perspectives, and styles"** — that is '
       'the environment I have worked in from Tehran to Copenhagen, on the floor and in the boardroom. '
       '**"Continuous improvement initiatives"**, **"digital transformation projects"** and **"robust controls, '
       'compliance standards, and risk management processes"** are the three lines in your posting I would '
       'start on in week one, and **"a culture of accountability, collaboration, customer focus, and '
       'continuous improvement"** is built with four numbers on one page and a weekly rhythm, not with a '
       'slogan. I am applying through your recruitment system, as required, and **"we look forward to hearing '
       'from you"** cuts both ways — so do I.', after=30)

    lp('**Practical.** Måløv, 25 minutes from Copenhagen · English working language, Danish fluent (and the '
       'language of dealers, authorities and the tax system I would have to learn) · category B licence and own '
       'car · available after agreement.', after=10)

    m.meta('Kind regards', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('**Operations leader with full P&L, 37 capital projects and a technical supply chain behind him** — '
           'owner since 2023 with purchasing, pricing, capacity and delivery in one hand; prior head of '
           'operations and maintenance in 24/7 production and senior project manager in a GMP/FDA environment. '
           'PRINCE2 certified, authorised maskinmester (LV/MV/HV), B.Tech in technology management. KPIs, '
           'governance and weekly rhythm rather than monthly surprises.', after=56)

    m.section('THE QUAY — WHERE I PUT THE CHECK')
    for label, body in [
        ('The gate',
         'Every hand-over point gets an owner and a check that takes under a minute. A check that costs more '
         'than it saves gets skipped, and then it is decoration.'),
        ('The number',
         'Lead time, delivery precision, days in storage, damage and cost per unit — four of them on one '
         'page, every week, owned by the person who can move them.'),
        ('The contract',
         'The promise, the penalty and the exit in writing before the first car moves; a service level '
         'without a consequence is a wish.'),
        ('The variance',
         'Find the cause before changing the plan: a late transporter, a wrong specification, a compound '
         'queue. The fix is usually upstream of the symptom.'),
        ('The customer',
         'The dealer and the driver judge the whole chain on one sentence — the date. If the date slips, they '
         'hear it from us first.'),
        ('The escalation',
         'Raised while it can still be solved cheaply, with two options and a recommendation, never as a '
         'problem alone.'),
    ]:
        m.bullet(label, body, after=14)

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director', 'ELOHVAC ApS · Copenhagen · May 2023–present',
         '8 employees · full P&L · purchasing, pricing and delivery',
         [('Operational ownership with the risk attached',
           'Purchasing, supplier terms, capacity, price and delivery decided with my own margin at risk; '
           '**budget** and cash followed weekly.'),
          ('Measured improvement',
           '**Over 40 % productivity gain** from digital tools in estimating, documentation and reporting — '
           'a transformation delivered, not proposed.')]),
        ('Co-owner and CTO / Technical Lead, AI department',
         'Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 (alongside ELOHVAC)',
         '4–10 people · customer solutions from requirement to go-live',
         [('Digital transformation in practice',
           'Requirements, architecture, integration and go-live of technical applications, with documented '
           'rollback and standards for what is accepted.'),
          ('Two organisations, one plan',
           'Matrix leadership across two companies with written priority agreements; the company has ceased '
           'trading and the department was closed in order.')]),
        ('Senior Commissioning Engineer / Project Manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · GMP/FDA/EMA',
         [('Delivery precision under regulation',
           'Written requirements, **FAT/SAT**, **IQ/OQ/PQ** and change control; **zero critical deviations** '
           'at handover on 37 projects.')]),
        ('Project and Workshop Manager', 'Ventek-Air · Copenhagen · Jan 2022–Nov 2022',
         '14 employees · 11 simultaneous site projects',
         [('Capacity, logistics and sequence',
           'Daily plan for 11 sites and 14 fitters; materials, subcontractors and transport coordinated so '
           'interfaces did not become delays.')]),
        ('Operations and Maintenance Manager', 'Biofos (Lynetten) · Copenhagen · Aug 2017–Jan 2022',
         'Wastewater plant in 24/7 operation · SCADA, PLCs, HV switchgear',
         [('Uptime and cost in the same number',
           '**Over 40 % lower energy consumption** through measurement and re-commissioning; incidents and '
           'corrective actions closed with a named owner.')]),
        ('Electromechanical Technician / Production Team Lead', 'ARJ Engineering · Tehran · Dec 2003–Mar 2010',
         '12 technicians · machine shop · machinery and equipment',
         [('Inventory, calibration and training',
           'Spare parts and equipment purchasing, calibration records and fault finding; training and '
           'follow-up for 12 technicians.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=14)

    m.section('EDUCATION, CERTIFICATION AND AUTHORISATION')
    m.edu('PRINCE2 certified project manager', 'AXELOS / PeopleCert · certification held')
    m.edu('LEAN and Six Sigma — methods in practice', 'DMAIC, 5S, VSM, standard work, FMEA · no certificate')
    m.edu('B.Tech, Technology Management and Mechanical Engineering',
          'Copenhagen School of Marine and Technical Engineering · 2017–2022 · GPA 7.6/12')
    m.edu('Authorised maskinmester (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('Refrigeration and ventilation technology · AMU',
          'Mercantec 2021 · STCW, Danish Maritime Authority 2021')
    m.edu('Electrical and mechanical engineering design, electrical engineering',
          'Tehran Technical University · 2000–2003 · EQF 6')

    m.section('LANGUAGES, IT AND PRACTICAL')
    m.para('English (working language) · Danish (fluent, first language) · Persian (mother tongue) · **IT**: '
           '**ERP**, **Excel** models for capacity, cost and **budget** follow-up, CMMS, BI dashboards, '
           '**Python** for own analysis · Måløv, 25 minutes from Copenhagen · category B licence and own car · '
           'available after agreement.', after=36)

    m.models_table('THE ROLE AS ADVERTISED — WHAT I BRING', ('Requirement', 'Evidence'), [
        ('Bachelor\'s degree in supply chain, logistics, engineering, business administration or related',
         'B.Tech in technology management and mechanical engineering, plus authorised maskinmester (LV/MV/HV) '
         '— a technical degree with economics and management in it, not a logistics degree.'),
        ('8–10+ years of progressive leadership within logistics, supply chain or related industries',
         'Twelve years of operational leadership: 8 employees and full P&L, 14 fitters on 11 sites, 25 '
         'specialists across 37 projects, 12 technicians in a workshop — technical supply chains, not vehicle '
         'ones.'),
        ('Proven track record of leading teams and driving operational transformation at pace',
         'Transformation delivered three times: processes built in my own company, digital tools with over '
         '40 % productivity gain, and 24/7 operation re-commissioned to over 40 % lower energy use.'),
        ('Inventory management, distribution, transportation, demand planning and operational excellence',
         'Inventory, materials and capacity planned against a moving order book; distribution and transport '
         'coordinated across 11 simultaneous sites and 37 project deliveries.'),
        ('External logistics providers and complex stakeholder environments',
         'Suppliers, subcontractors, authorities and steering groups negotiated and coordinated for twenty '
         'years — including the ones who could stop a project with a single phone call.'),
        ('Strong financial and analytical acumen, turning data into decisions',
         'Full P&L, budget, cash and cost per unit followed weekly in my own company; four numbers on one '
         'page driving the week rather than a monthly report explaining it.'),
        ('Automotive industry experience',
         'None. My industry is technical installation and regulated production — the same mechanics of '
         'allocation, lead time, damage and working capital, without the cars.'),
        ('Key understanding of the Danish Luxury Tax system',
         'Not my area. Registration and luxury tax rules, VIN-level documentation and the authorities behind '
         'them would be the first thing I learned properly — and I would own that learning rather than '
         'delegate it.'),
        ('Develop and execute the Danish operations and logistics strategy',
         'Strategy written as a plan with owners and numbers: cost, capacity, service level and the sequence '
         'of what changes first — the way 37 projects and 11 sites were run.'),
        ('Trusted advisor to the Country Director on performance, risks and opportunities',
         'Advised owners and directors for years, including the meetings where the message was unwelcome and '
         'the alternative had to be on the table the same day.'),
        ('Drive operational scalability for network expansion and product launches',
         'Grew a company from its first contract to 8 employees and a fixed customer base, and scaled project '
         'delivery to 37 parallel builds without adding overhead that did not pay.'),
        ('Establish performance metrics and governance processes across all functions',
         'Governance with a weekly cadence: one page, four KPIs, named owners, decisions logged with the date '
         'and the option that was rejected.'),
        ('Lead business planning for logistics costs, inventory, capacity and investments',
         'Business cases with NPV/IRR logic, sensitivity and the cost of waiting in them; capacity and '
         'inventory planned before the quarter that needs them.'),
        ('Own the end-to-end vehicle supply chain from factory allocation to dealer and customer delivery',
         'Not owned end to end for vehicles. Owned end to end for equipment: specification, purchase, '
         'transport, installation, acceptance and handover to the user — allocation to delivery, in another '
         'industry.'),
        ('Oversee inbound logistics, port operations, warehousing, transportation, vehicle preparation, distribution',
         'Inbound goods, warehousing and transport coordinated daily across 11 sites; preparation and '
         'acceptance were mine as commissioning lead, with the criteria agreed in writing.'),
        ('Balance inventory levels and vehicle flow against demand and working capital',
         'Inventory and materials balanced against orders and cash in my own company — the same trade-off: '
         'stock costs money today to protect a delivery tomorrow.'),
        ('Lead forecasting, allocation and supply planning with Sales and Regional Supply',
         'Forecast, capacity and allocation agreed with the people who sold the work, every week, in writing '
         '— the argument is always about the same thing: who carries the risk of being wrong.'),
        ('Monitor and improve logistics KPIs: lead time, delivery precision, inventory aging, transport performance, cost',
         'Delivery precision and lead time tracked on 37 projects and 11 sites; in my own company the same '
         'four numbers decided whether the week was good.'),
        ('Drive continuous improvement using Lean, Six Sigma and best practice',
         '**Lean** and **Six Sigma** methods in practice — 5-why, FMEA, standard work, DMAIC — used on '
         'processes that were failing, not as a certificate on a wall.'),
        ('Lead digital transformation projects within logistics and operational systems',
         'Built the digital layer myself: AI and automation in estimating, documentation and reporting with '
         'over 40 % productivity gain, plus customer systems from requirement to go-live at Data Power.'),
        ('Establish controls, compliance standards and risk management across operations',
         'Controls and documented evidence in a GMP/FDA environment where an auditor could arrive any day: '
         'zero critical deviations at handover on 37 projects.'),
        ('Lead, develop and inspire the Operations & Logistics team, with objectives, recruitment and succession',
         'Hired, trained and kept 8 employees including 3 apprentices, and led 12 technicians and 25 '
         'specialists — with objectives, 1:1s and a named successor for my own role before I left.'),
        ('Foster a culture of accountability, collaboration, customer focus and continuous improvement',
         'Accountability made visible: every action has an owner and a date; every complaint is answered the '
         'same day; nobody is blamed for bad news delivered early.'),
        ('Operational liaison with regional HQ, providers, distribution partners and dealers; negotiate SLAs',
         'Interface role for twenty years — engineering, operations, suppliers and authorities — with the '
         'service levels and the consequences written down before the work starts.'),
        ('Collaborate with Sales, Marketing, Finance, Aftersales, Customer Experience and Network Development',
         'Comfortable in the commercial room: I have priced the work, sold it, delivered it and explained the '
         'margin to the bank — the same conversation, in a different industry.'),
        ('Own the operational budget, logistics spend and cost control, with executive reporting',
         '**Budget** and cost control under full P&L; executive reporting as one page of numbers, risks and '
         'decisions needed — never a slide about how busy we were.'),
        ('Leadership competencies: strategy, commercial acumen, executive communication, people, change',
         'The ten competencies are the job description of an owner in a small company: strategy on Monday, '
         'a difficult customer on Tuesday, a wage negotiation on Wednesday and the numbers on Friday.'),
        ('Submit the CV in English, located in Copenhagen, through the recruitment system',
         'This CV is in English, I live 25 minutes from Copenhagen — and this application is submitted '
         'through your recruitment system, as your GDPR process requires.'),
    ], widths=(2500, 7846))

    m.section('WHERE THE MONEY USUALLY HIDES')
    for label, body in [
        ('Days in storage',
         'Every day a car waits is interest, insurance, compound rent and one more chance of damage. The '
         'count is the cheapest saving in the chain and the first number I would put on the page.'),
        ('Damage and rework',
         'Transport damage and preparation rework are found late by definition. Moving one inspection '
         'upstream usually costs less than the paint it saves.'),
        ('The specification mix',
         'Cars that are right but wrong for the market: the most expensive inventory is the one nobody '
         'ordered. Allocation discipline and forecast honesty are the cure.'),
        ('Transport utilisation',
         'A transporter that is 80 % full costs 100 %. Consolidation, route and ETA accuracy are negotiated '
         'terms, not acts of God.'),
        ('The forecast error',
         'Measure it openly, month by month. A forecast nobody scores is a wish, and every function plans '
         'against it anyway.'),
    ]:
        m.bullet(label, body, after=14)

    m.section('FIRST 90 DAYS')
    for b in (
        'Weeks 1–4: walk the chain in person — port, compound, preparation, transporter, three dealers. Map '
        'every hand-over point and the owner of each, and put the four numbers on one page.',
        'Weeks 5–8: take over the live contracts and read the service levels against what is actually being '
        'delivered; the gap between the two is the first saving and the first risk.',
        'Weeks 9–12: one allocation and forecasting cycle run with Sales and Regional Supply, with working '
        'capital in the conversation from the start; and the luxury tax and registration process learned to '
        'the point where I can explain it to a dealer.',
        'Week 13: the first monthly page to the Country Director — four numbers, three risks, two decisions '
        'and one improvement — and a written note on what I got wrong in the first quarter.'):
        m.bullet('', b, after=14)

    m.section('THE PAGE THE COUNTRY DIRECTOR GETS')
    for label, body in [
        ('Four numbers, one page',
         'Delivery precision, days in storage, cost per unit and inventory health — with the trend and the '
         'reason it moved, not a dashboard that needs an interpreter.'),
        ('Three risks, ranked',
         'Only the ones that could stop a delivery or a launch this quarter, each with an owner and the date '
         'the decision is needed.'),
        ('Two decisions',
         'What I need from the leadership team this month, stated as options with a recommendation — never as '
         'a status update.'),
        ('One improvement',
         'The single thing we changed last month, what it was worth, and whether it held. A chain improves '
         'one gate at a time.'),
    ]:
        m.bullet(label, body, after=14)

    m.section('WHAT I WOULD ASK')
    for b in (
        'Which port and compound are used today, and what does a car cost per day while it waits?',
        'How many dealers are live, and how is allocation decided when supply is short?',
        'What does the Danish leadership team need in the first year: volume, network, or cost per unit?',
        'Who owns the relationship with the importer and the compound today, and where does that '
        'responsibility move if this role takes it?'):
        m.bullet('', b, after=14)

    m.para('**I would welcome a conversation about the chain and the numbers behind it.** +45 93 99 95 14 · '
           'ajlooshahram@gmail.com.', after=16)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Zeekr_OperationsLogisticsManager.docx')
    build(out)
    print(out)
