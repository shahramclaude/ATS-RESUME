# -*- coding: utf-8 -*-
"""Arla Foods — Logistics Operations Manager, Vejle (ref. 112195). English posting -> English document.

Form (master/FORMKATALOG.md): opening **Y** (shelf life: milk has no delivery date, it has a shelf
life — and the last days on the shelf are the ones the customer judges), structure **Choose it,
contract it, steer it — or end it** (the 3PL partner lifecycle), register **The Cold Chain**
(cold chain, shelf life, pallet, batch, picking, replenishment, temperature, hold, inventory accuracy).
Culture file: jd/Arla_LogisticsOperationsManager_kultur.txt. Reviewed on an ongoing basis.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Logistics Operations Manager · 3PL performance, cold chain and operational reliability'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('14 November 2026')
    m.meta('Arla Foods · Warehouse & Outbound Logistics · Logistics Operations Manager · Vejle · ref. 112195')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Logistics Operations Manager', bold=True, color='1A1A1A')

    def lp(text, after=40):
        return m.para(text, after=after, line=234)

    # ---------------------------------------------------------------- page 1
    lp('**Milk does not have a delivery date. It has a shelf life.** A pallet that leaves the site twelve hours '
       'earlier is worth more than a discount that arrives twelve hours later, and the last days on the shelf '
       'are the ones the customer judges you on. Everything in this job — picking, temperature, transport '
       'slots, inventory accuracy — is a way of protecting that clock.', after=36)

    lp('You are asking someone to **"lead and develop the Danish 3PL warehouse and transport setup"**, where '
       '**"customer requirements, warehouse execution, transportation, and production planning must come '
       'together seamlessly"**. I have spent twenty years making exactly those interfaces work in technical '
       'operations — eleven simultaneous sites, 37 capital projects, a 24/7 plant and my own company with full '
       '**P&L** since 2023. What I have not done is run a 3PL setup in dairy, and I say so below rather than '
       'later.', after=36)

    lp('**Choose it, contract it, steer it — or end it. Four phases, and each one has a document.**', after=26)

    lp('**Choose it.** Decision material, not opinion: capacity per pallet position, cost per pallet in and '
       'out, temperature regimes, distance to the production sites, what happens in the peak week, and what it '
       'would cost to leave. I have compared suppliers and subcontractors this way with my own margin at '
       'stake, and I have learned that the cheapest quote is usually a forecast that was never going to '
       'hold.', after=22)

    lp('**Contract it.** **Service level**, **completion rate**, **inventory accuracy**, damage and the '
       'escalation route — in writing, with a consequence attached. A service level without a penalty is a '
       'wish; a penalty without an escalation route is an argument.', after=22)

    lp('**Steer it.** A weekly hour with the provider and the numbers on one page, plus the two operations that '
       'actually move them: what went short, and what arrived late. Data first, then the conversation — and '
       'escalations handled while they can still be solved cheaply, not after the customer has noticed.', after=22)

    lp('**Or end it.** The phase nobody writes about: how to re-tender or exit without risking a Christmas. A '
       'transition plan, a second source, a hand-over date and a file that lets the next provider start on day '
       'one. I have closed a department and wound down a company in order — the same discipline, at a smaller '
       'scale.', after=30)

    lp('**The daily reality behind those four phases.** Somebody has to answer when the transport does not '
       'arrive, the pick is short, the temperature log shows a gap, or quality puts a batch on **hold** at '
       'four in the afternoon. That is **"managing operational escalations and resolving supply chain '
       'challenges proactively"** in practice: the person who finds the problem owns it until it is closed, '
       'and the fix is written down so the next person does not rediscover it.', after=34)

    lp('**Where my record is thinner, stated plainly.** I have not managed 3PL warehousing or transport, I have '
       'no dairy or food-safety background — no HACCP — and I have not designed a warehouse network. What I '
       'bring is the operating core: performance management with four numbers and a weekly cadence, '
       '**escalations** run so that bad news travels first, a compliance culture from GMP/FDA where '
       'documentation and audits were daily conditions (**zero critical deviations** at handover on 37 '
       'projects), supplier and subcontractor negotiation with my own money at risk, **Lean** and **Six Sigma** '
       'in practice, a **digital transformation** that produced **over 40 % productivity gain**, and a '
       'refrigeration background from AMU and five years on a 24/7 plant. The dairy vocabulary I would learn in '
       'weeks; the discipline of a number that somebody owns takes years, and I have built it three times.',
       after=32)

    lp('**Why Arla, in your words.** A cooperative owned by around **8,000 farmers in seven countries**, '
       'headquartered in **Aarhus**, with **revenue of EUR 15.1 billion** in 2025 and brands like Arla, Lurpak, '
       'Castello and Puck, does not get to be approximate about logistics: the product is fresh, the clock is short, and **"collaboration is the '
       'core of culture"** because the alternative is waste. You offer a **"collaborative and ambitious '
       'environment"** where **"development, ownership, and continuous improvement are key drivers of '
       'success"** and where **"everyone feels valued and empowered"**. **"Shape the Future of Dairy"** is a '
       'better line than most, because it is a supply chain promise: fresh food, short clock, no room for '
       'approximation.', after=30)

    lp('**On the role itself.** I recognise the four things you describe: **"operational performance '
       'management"** now, **"strategic and tactical network warehouse design"** as the next step, '
       '**"developing robust decision material and recommendations for 3PL partner decisions"**, and '
       '**"ensuring high customer service levels and operational reliability"**. I also recognise the harder '
       'sentence — that you need someone who can **"build relationships and influence stakeholders across '
       'organizational boundaries"**, **"turn network insights into practical changes and measurable business '
       'improvements"**, and **"prioritize and make decisions in a fast-paced environment"** without breaking '
       '**"compliance with quality, food safety, and safety standards"**. That last constraint is the one I '
       'take most seriously: in a regulated plant, a shortcut in documentation is the most expensive saving '
       'available.', after=30)

    lp('**Practical.** English is my working language and Danish is my first, so the floor, the drivers and the '
       'Danish authorities all get the same conversation. I live in Måløv today and **am ready to relocate** to '
       'the Vejle area for this role; category B licence and own car. **"We review applications on an ongoing '
       'basis"**, so this one goes now rather than later.', after=10)

    m.meta('Kind regards', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('**Operations leader with full P&L, 37 capital projects and 24/7 production behind him** — owner '
           'since 2023 with purchasing, capacity, delivery and cost in one hand; prior head of operations and '
           'maintenance on a plant that never stops. PRINCE2 certified, authorised maskinmester (LV/MV/HV), '
           'B.Tech in technology management, refrigeration background from AMU. Performance managed with four '
           'numbers on one page and a weekly cadence — and escalations handled before the customer notices.',
           after=56)

    m.section('THE COLD CHAIN — HOW I KEEP A PROMISE MOVING')
    for label, body in [
        ('The clock',
         'Shelf life is the only KPI the customer sees. Everything upstream — pick time, dispatch slot, '
         'transport temperature — is judged by how many days are left when the pallet arrives.'),
        ('The accuracy',
         'Inventory accuracy is the honest number: if the system and the rack disagree, every other KPI is a '
         'guess. Count, reconcile, and make the cause visible rather than the error.'),
        ('The short pick',
         'A short pick is a promise about to break — usually because **replenishment** of the pick face came '
         'too late. It is closed the same day, with the customer told before the transport leaves.'),
        ('The temperature',
         'A gap in the log is an incident, not a rounding error. It gets an owner, a cause and a written '
         'closure, because the next audit will ask for exactly that.'),
        ('The escalation',
         'Raised while it can still be solved cheaply, with two options and a recommendation, and closed with '
         'a date — never left to become the customer\'s problem.'),
        ('The provider',
         'A partner is steered with numbers, a weekly hour and an **SLA** with a consequence, not with '
         'goodwill. What gets measured, gets discussed; what gets discussed, improves.'),
    ]:
        m.bullet(label, body, after=14)

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director', 'ELOHVAC ApS · Copenhagen · May 2023–present',
         '8 employees · full P&L · purchasing, capacity and delivery',
         [('Service level with my own money at risk',
           'Promised dates, dispatch, suppliers and cost per job decided and delivered by me; a late '
           'subcontractor or a missed slot was my loss, not a slide in a review.'),
          ('Measured improvement',
           '**Over 40 % productivity gain** from digital tools in estimating, documentation and reporting — '
           'delivered, not proposed.')]),
        ('Co-owner and CTO / Technical Lead, AI department',
         'Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 (alongside ELOHVAC)',
         '4–10 people · customer solutions from requirement to go-live',
         [('Systems, data and go-live',
           'Requirements, integration and go-live of customer systems with documentation the customer could '
           'run; standards agreed for what is accepted.'),
          ('Two organisations, one plan',
           'Matrix leadership across two companies with written priority agreements; the company has ceased '
           'trading and the department was closed in order.')]),
        ('Senior Commissioning Engineer / Project Manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · GMP/FDA/EMA',
         [('Compliance as a daily condition',
           'Documented acceptance, **FAT/SAT**, **IQ/OQ/PQ** and change control; **zero critical deviations** '
           'at handover on 37 projects in a plant where auditors arrive unannounced.')]),
        ('Project and Workshop Manager', 'Ventek-Air · Copenhagen · Jan 2022–Nov 2022',
         '14 employees · 11 simultaneous site projects',
         [('Coordination across sites and partners',
           'Daily plan for 11 sites, 14 fitters, subcontractors and material deliveries — where a late '
           'arrival became a delayed building within hours.')]),
        ('Operations and Maintenance Manager', 'Biofos (Lynetten) · Copenhagen · Aug 2017–Jan 2022',
         'Wastewater plant in 24/7 operation · SCADA, PLCs, HV switchgear · pumps and refrigeration',
         [('Uptime, cost and corrective action',
           '**Over 40 % lower energy consumption** through measurement and re-commissioning; incidents closed '
           'with a named owner while the plant kept running.')]),
        ('Electromechanical Technician / Production Team Lead', 'ARJ Engineering · Tehran · Dec 2003–Mar 2010',
         '12 technicians · machine shop · machinery and equipment',
         [('Spare parts, calibration and training',
           'Stock, purchasing and calibration records for a workshop of 12; fault finding and corrective '
           'actions documented.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=14)

    m.section('EDUCATION, CERTIFICATION AND AUTORISATION')
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
    m.para('English (working language) · Danish (first language) · Persian (mother tongue) · **IT**: **ERP** and '
           '**WMS**-adjacent systems, **Excel** models for capacity, **cost per unit** and forecast, CMMS, BI '
           'dashboards, **Python** for own analysis · Måløv today, **ready to relocate** to the Vejle area · '
           'category B licence and own car · available after agreement.', after=36)

    m.models_table('THE ROLE AS ADVERTISED — WHAT I BRING', ('Requirement', 'Evidence'), [
        ('Experience from logistics, supply chain, warehousing, transportation or operations management',
         'Operations management is the through-line: 24/7 plant operations, 11 simultaneous sites with '
         'material and transport coordination, and a company where dispatch and delivery are the daily '
         'product.'),
        ('Experience with 3PL management across both warehousing and transportation',
         'No 3PL setup managed. My provider management has been subcontractors, suppliers and carriers on '
         'technical projects — the same steering, without the dairy and without a 3PL contract.'),
        ('Strategic or tactical network design, capacity planning and implementation of network changes',
         'Capacity planned and changed repeatedly: 11 sites re-sequenced, 37 projects phased, a company scaled '
         'from its first contract to 8 employees, with **forecasting** and capacity in the same weekly '
         'conversation. Network design for warehouses I have not done.'),
        ('Understanding of the end-to-end value chain from production to customer delivery',
         'From the machine to the handover: requirements, production, commissioning, documentation, delivery '
         'and the first year of operation — the same chain, measured in a different unit.'),
        ('Experience leading teams directly or through external partners',
         'Direct **team leadership**: 8 employees, 14 fitters, 25 specialists, 12 technicians. Indirect: '
         'subcontractors and suppliers who had to deliver to my date with my margin at stake.'),
        ('Strong stakeholder management and cross-functional collaboration',
         'Twenty years at the interfaces where engineering, operations, quality, customers and authorities '
         'each need a different sentence about the same problem — in writing and in the room.'),
        ('A structured and data-driven approach to performance management',
         'Four numbers on one page, every week, with an owner for each: if it is not on the page, it is not '
         'managed — and if nobody owns it, it is not a number.'),
        ('Experience with operational KPIs and continuous improvement methodologies',
         '**KPI** work on lead time, delivery precision and cost; **Lean** and **Six Sigma** methods (5-why, '
         'FMEA, standard work, DMAIC) used on processes that were actually failing.'),
        ('The ability to prioritize and make decisions in a fast-paced environment',
         'Decisions taken in minutes on site, then written down: what was decided, by whom, and what was '
         'rejected. In a plant that runs 24/7, waiting for consensus is a decision in itself.'),
        ('Strong communication skills in English; Danish is an advantage',
         'English is my working language in documentation, suppliers and international colleagues; Danish is '
         'my first language — the floor, the drivers and the authorities get the same answer.'),
        ('Lead and develop a small operational team',
         'Small teams are what I have led: eight employees including three apprentices, twelve technicians, '
         'fourteen fitters — with objectives, 1:1s, training and a named successor before I left.'),
        ('Own and develop performance across 3PL warehousing and 3PL transportation',
         'Performance ownership is familiar; the 3PL framing is not. What I would do on day one is read the '
         'contract against what is actually delivered — the gap is always the first agenda item.'),
        ('Develop robust decision material and recommendations for 3PL partner decisions',
         'Decision material as one page: options, cost per unit, capacity, risk and a recommendation with the '
         'case against it written down — the way 37 capital projects were approved.'),
        ('Ensure high customer service levels and operational reliability',
         'Delivery precision and service level tracked as the first two numbers; in my own company a missed '
         'date was a phone call from the customer, not a report.'),
        ('Coordinate activities across production sites, logistics providers, customers and commercial teams',
         'Coordinated production sites, suppliers, subcontractors and customers across 11 live sites at once, '
         'with the commercial team in the same weekly conversation.'),
        ('Monitor and improve KPIs: service level, completion rate, inventory accuracy, productivity, cost',
         'The five are the right five. I have run three of them directly (service level, productivity, cost) '
         'and would expect inventory accuracy to be the one that teaches me the most in the first month.'),
        ('Drive continuous improvement initiatives across processes and systems',
         'Improvement with a number attached: over 40 % lower energy consumption at Lynetten, over 40 % '
         'productivity gain in my own company — both measured after the change, not promised before it.'),
        ('Manage operational escalations and resolve supply chain challenges proactively',
         'Escalation as a routine, not a crisis: raised early, with two options and a recommendation, and '
         'closed with a date and a cause. Bad news travels first in my teams.'),
        ('Ensure compliance with quality, food safety and safety standards',
         'Food safety (HACCP) is new to me. The compliance habit is not: GMP/FDA documentation, audits without '
         'notice, deviations closed with an owner, and zero critical findings at handover.'),
        ('Future potential for strategic and tactical network warehouse design',
         'The part I would grow into — and the part I am most interested in: capacity, flow, geography and '
         'cost per pallet, decided on data rather than on habit.'),
        ('Based in Vejle, Denmark; permanent role reporting to the Director for Warehouse & Outbound Logistics',
         'I live in Måløv today and am ready to relocate to the Vejle area for the role — present on site is '
         'the only version of this job that works.'),
        ('English application; applications reviewed on an ongoing basis',
         'Applied in English, through the channel in the posting, and sent now rather than at the deadline — '
         'your process closes when the right candidate appears, and that is a fair way to run it.'),
    ], widths=(2500, 7846))

    m.section('FIRST 90 DAYS')
    for b in (
        'Weeks 1–3: sit with the team, the 3PL partner and the transport providers — read the contract, walk '
        'the warehouse, ride a route. Then compare what the contract promises with what the week actually '
        'delivers.',
        'Weeks 4–6: one page with the five KPIs, their owners and the definitions everyone agrees on; a weekly '
        'hour with the provider, and an escalation route that is written down before it is needed.',
        'Weeks 7–10: one improvement chosen for effect — short picks, dispatch cut-off or inventory accuracy — '
        'closed in the system and measured after, not just described.',
        'Weeks 11–13: the first decision paper for a 3PL or capacity choice, with the option of doing nothing '
        'costed; and a written note to Janni on what I got wrong in the first quarter.'):
        m.bullet('', b, after=14)

    m.section('WHAT I WOULD ASK')
    for b in (
        'Which 3PL partners are in scope today, and where does the contract hurt most when it is tested?',
        'How many production sites feed the Vejle setup, and which customers are the hardest to serve on time?',
        'Is the network design ambition a 2027 question, or something the team expects to work on next year?'):
        m.bullet('', b, after=14)

    m.para('**I would welcome a conversation about the setup and the numbers behind it.** +45 93 99 95 14 · '
           'ajlooshahram@gmail.com.', after=16)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Arla_LogisticsOperationsManager.docx')
    build(out)
    print(out)
