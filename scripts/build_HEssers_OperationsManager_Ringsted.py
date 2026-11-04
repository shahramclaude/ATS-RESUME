# -*- coding: utf-8 -*-
"""H.Essers — Operations Manager, Ringsted (warehousing, healthcare and chemicals).

English deliverable (JD is English): task-first cover page + CV in one document.
Culture and role intel: master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md,
section on H.Essers Ringsted (research 04.11.2026).
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Operations leadership · GxP discipline, site performance and customer P&L'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('4 November 2026')
    m.meta('H.Essers · Warehousing, Ringsted · Operations Manager')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Operations Manager — Ringsted', bold=True, color='1A1A1A')
    m.para('Dear Hiring Team', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('A warehouse like Ringsted is judged on five things, and none of them are visible from the office. Orders '
           'that leave complete and on time — the OTIF number. Stock records that match what is on the rack when a '
           'customer asks. '
           'Temperature, dangerous goods and safety handled without a single deviation. A cost per unit that holds '
           'when volumes move. And customers who renew because the operation did what it promised in the tender. '
           'The Operations Manager role is to make those five true on every shift, and to build a team that keeps '
           'them true when the site doubles in size.', after=80)

    m.para('**The operating rhythm I would run is deliberately boring.** A daily tier board at the start of each shift '
           'with five numbers on it — orders shipped versus plan, lines picked per hour, stock accuracy, open '
           'deviations and near-misses — reviewed in ten minutes with the shift leads, and escalated by exception to '
           'me rather than in a long meeting. A structured handover between shifts so nothing lives only in one '
           'person\'s head. A Gemba walk with the shift lead every morning, because the floor tells you about a '
           'blocked dock before the report does. And a deviation and CAPA routine where every incident gets a root '
           'cause with A3 and 5 Whys, a named owner, a deadline and a check that the fix actually held.', after=80)

    m.para('Around that sit the things that decide whether the site makes money: a KPI tree that ties the floor '
           'numbers to the customer contract — cost per order, cost per pallet, overtime share, absence, and '
           'throughput per labour hour — so improvement work is chosen where it moves the P&L and the profitability of '
           'each customer contract, not where it is easiest. A capacity plan that looks twelve weeks ahead at the ramp-up the site is heading into. A '
           'continuous improvement funnel with a limited number of active projects, each with a business case and a '
           'measured effect. And quarterly reviews with each customer where we show the numbers before they ask, '
           'because that is what turns an operation into a partnership.', after=80)

    m.para('What I bring is the combination the role needs: P&L ownership, site leadership in regulated production, '
           'and a working knowledge of what GxP actually demands. At Novo Nordisk I worked under GMP, FDA and EMA '
           'requirements across 37 parallel capital projects with 25 specialists — documented acceptance criteria, '
           'FAT/SAT and IQ/OQ/PQ, deviation handling and zero critical findings at handover. At Biofos I ran '
           'maintenance and operations on a 24/7 plant with spare-parts and warehouse flow, 5S and standard work, '
           'LOTO, risk assessment and APV as daily routines, and shift patterns that included nights and weekends. '
           'For the past three years I have run my own company with full P&L, quoting, pricing, margin follow-up and '
           'service agreements measured on response time and quality — which is the closest thing to a customer '
           'contract with a penalty clause that a small business offers.', after=80)

    m.para('I will be straight about the gap: I have not run a third-party logistics site with a customer portfolio '
           'of this kind, and my warehouse experience comes from spare-parts and materials flow inside regulated '
           'operations rather than from high-volume pick-and-pack. What I do have is site accountability in a '
           'regulated environment, a way of working that produces numbers rather than narratives, and fifteen years '
           'of leading shift-based teams. The first ninety days are therefore a learning plan with dates: weeks 1–2 '
           'on the floor in every function and every shift, including a weekend; day 30 with a baseline of the five '
           'tier-board numbers and a signed-off picture of contract obligations per customer; day 60 with a '
           'prioritised improvement funnel, a stock accuracy routine and a safety plan for the phase-2 expansion; '
           'day 90 with measured movement in at least two of the five numbers and a development plan for every shift '
           'lead.', after=80)

    m.para('What drew me to H.Essers is that the Ringsted site is not a mature operation being polished — it is a '
           'site being built, with healthcare and chemicals in temperature-controlled space, dangerous goods '
           'approvals, and a second phase that will multiply the footprint. That is a leadership job more than an '
           'administration job. And the values you describe fit how I prefer to work: **family values** since 1928 '
           'mean people are not a line in the budget; **Lifelong Learning** and the Academy match the way I '
           'have always developed apprentices and shift leads; **innovation** and "It\'s transpossible" only mean '
           'something if someone tests the idea on the floor and measures whether it worked; and **diversity and '
           'inclusion** show in who gets trained, who gets the good shifts and whose idea is tried.', after=80)

    m.para('Practically: I live in Måløv, about 50 minutes by car from Ringsted, so no relocation is needed. I speak '
           'Danish natively, English professionally and Persian, which helps in a site with international customers '
           'and colleagues. I am also an active Claude coder and build my own Python tools for KPI follow-up, '
           'capacity models and investment cases with NPV, IRR and scenarios — useful when a new customer or a new '
           'warehouse phase has to be priced before it is signed.', after=80)

    m.para('I would like to come to Ringsted and walk the site with you — the docks, the temperature zones and the '
           'dangerous goods area — and talk through how I would run the first ninety days and where I see the '
           'biggest operational gains in the current setup.', after=80)
    m.meta('Kind regards', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('Operations leader with 15+ years from regulated production, technical service and projects — strategic and '
           'operational responsibility, full P&L ownership, site accountability on a 24/7 plant, and cross-functional '
           'leadership of 25 specialists. '
           'Works from a daily tier board and a small set of KPIs, with GxP documentation, deviation handling and '
           'safety routines as a matter of course rather than a project. Builds his own Python and Claude tools for '
           'KPI follow-up, capacity planning and business cases.', after=80)

    m.section('OPERATIONS AND RESULTS')
    for label, body in [
        ('P&L and commercial ownership',
         'Full P&L in his own company since 2023: quoting, pricing, margin follow-up, service agreements measured on '
         'response time, quality and delivery, and direct negotiation with commercial and industrial customers.'),
        ('Site and shift leadership',
         'Maintenance and operations leadership on a 24/7 plant with shift patterns including nights, weekends and '
         'public holidays; daily board meetings, bottleneck analysis and standard work routines.'),
        ('GxP and quality systems',
         '37 capital projects under GMP/FDA/EMA with 25 specialists: documented acceptance criteria, FAT/SAT, '
         'IQ/OQ/PQ, deviation and CAPA handling — zero critical findings at handover.'),
        ('Stock and flow discipline',
         'Spare-parts and warehouse flow with cycle counts, 5S on storage areas, receiving routines and deviations '
         'closed with owner and deadline. SAP ERP for materials, assets and cost follow-up.'),
        ('Continuous improvement',
         '5S, standard work and PDCA in daily use; a PDCA programme reduced energy cost by 40 %. A3 and 5 Whys as the '
         'default for root cause, with the countermeasure verified afterwards.')]:
        m.bullet(label, body, after=30)

    m.models_table('TOOLS AND METHODS', ('Task', 'Tool and documented use'), [
        ('Daily performance management',
         'Tier board with five metrics per shift (shipped vs. plan, productivity, stock accuracy, open deviations, '
         'near-misses), structured shift handover and escalation by exception. Used in workshop, plant and projects.'),
        ('People management and leadership',
         'Situational Leadership (SLII), delegation ladder, 1:1s every two weeks, performance reviews, GROW and SBI '
         'feedback, competence matrix and cross-training plan. Apprentices trained to final trade test.'),
        ('Quality and compliance',
         'Deviation and CAPA handling, A3 root cause, 5 Whys and Ishikawa, document control and audit readiness. '
         'FAT/SAT and IQ/OQ/PQ under GMP; zero critical findings at handover.'),
        ('Safety and environment',
         'LOTO, risk assessment, APV/workplace assessment, near-miss reporting, toolbox talks and safety walks. '
         'Applied daily on a 24/7 plant and in contractor-heavy projects.'),
        ('Continuous improvement',
         'PDCA, 5S, standard work, VSM, Kaizen and a limited project funnel with business case and measured effect. '
         'Cost per unit and labour productivity as steering numbers.'),
        ('Customer and stakeholders',
         'Customer reviews on their numbers, stakeholder mapping and RACI, written decisions with owner and '
         'deadline. Investment cases with NPV, IRR and scenarios for new business and capacity.')])

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director',
         'ELOHVAC ApS · Copenhagen, Denmark · May 2023–present',
         '5 electricians and 3 apprentices · full P&L · commercial and industrial customers',
         [('Commercial ownership', 'Quoting, pricing, margin follow-up and service agreements with response time, '
                                   'quality and delivery as KPIs; direct customer dialogue on needs, scope and cost.'),
          ('People and safety', 'Daily planning, 1:1s, performance reviews, coaching and motivating a shift-based team, competence matrix, '
                                'apprentice training, '
                                'LOTO, risk assessment and APV at every site start.'),
          ('Digital tools', 'Python and Claude API for quotations, schedules, quality checklists and KPI dashboard; '
                            'productivity gain above 40 % in the business.')]),
        ('Senior Commissioning Engineer / Project Manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd, Denmark · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · DKK 2–10m per project · GMP/FDA/EMA',
         [('GxP and interfaces', 'Progress, cost, risk and resources across engineering, procurement and operations; '
                                  'documented acceptance criteria and audited handover throughout.'),
          ('Performance and improvement', 'FAT/SAT and IQ/OQ/PQ with zero critical deviations at handover; A3 and '
                                          '5 Whys in fault finding; a PDCA programme cut energy cost by 40 %.')]),
        ('Project and Workshop Manager',
         'Ventek-Air · Copenhagen, Denmark · Jan 2022–Nov 2022',
         '14 employees · 11 parallel construction projects · DKK 2–10m each',
         [('Throughput and flow', 'Tenders, quotations, subcontractors and handover packages. Daily board meetings '
                                  'and bottleneck analysis plus standardised working routines lifted delivery '
                                  'performance.')]),
        ('Maintenance and Operations Manager / Workshop Technician',
         'Biofos, Lynetten · Copenhagen, Denmark · Aug 2017–Jan 2022',
         '24/7 operations · warehouse and spare-parts flow · shift work including nights and weekends',
         [('Stock, storage and routines', 'Receiving and spare-parts flow with cycle counts, 5S on storage areas and '
                                          'min/max levels; preventive maintenance planned from SCADA data.'),
          ('Safety and standards', 'LOTO, risk assessment, APV and near-miss reporting in shift operations; standard '
                                   'work and PDCA on the workshop and store.')]),
        ('Electromechanical Technician / Production Team Leader',
         'ARJ Engineering · Tehran, Iran · Dec 2003–Mar 2010',
         '12 mechanics and technicians · machine workshop',
         [('Planning and targets', 'Shift planning, material control and target follow-up; fault diagnosis, '
                                   'root-cause analysis and corrective actions on industrial equipment.')]),
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
    m.edu('Lean practice: 5S, PDCA, VSM, A3, Kaizen', 'Ongoing courses and daily application in operations')
    m.edu('Refrigeration and air conditioning · STCW safety and engine-room watch',
          'Mercantec 2021 · Danish Maritime Authority 2021–2023')

    m.section('LANGUAGES, PRACTICAL AND REFERENCES')
    m.para('Danish and Persian: native · English: professional, written and spoken · Driving licence B · Lives in '
           'Måløv, about 50 minutes by car from Ringsted; relocation not required · Available for shift-based site '
           'leadership, including early starts and weekend cover when the operation needs it · References from Novo '
           'Nordisk and Biofos on request.', after=70)

    m.models_table('WHAT THE ROLE ASKS FOR — MY EVIDENCE', ('Requirement', 'Evidence'), [
        ('Full P&L ownership of operations and customers',
         'Full P&L in his own company for three years — pricing, margin and profitability per customer, cost control '
         'and service agreements with penalty-style performance terms.'),
        ('Supply chain or warehousing experience, +5 years, ideally GxP',
         'Five years in regulated operations with warehouse, storage and spare-parts flow; two years in a GMP/FDA/EMA '
         'environment with audited handovers. High-volume pick-and-pack is new to me.'),
        ('Translating the strategic vision into actionable plans',
         'Ran 37 capital projects and 11 construction projects in parallel with documented plans, decision points '
         'and reported effect; annual plans and 90-day plans as a standard tool.'),
        ('KPI monitoring, returns and continuous improvement',
         'Tier boards, OTD and productivity follow-up, deviation and CAPA routines, A3/PDCA with verified '
         'countermeasures; 40 % reduction in energy cost through PDCA.'),
        ('A safe and high-performing work environment',
         'LOTO, APV, risk assessment and near-miss reporting in daily use on a 24/7 plant and in contractor-heavy '
         'projects; accident and deviation follow-up with named owners.'),
        ('Building customer relationships and new business opportunities',
         'Trust-based customer relationships from three years of direct commercial dialogue, quotations and '
         'renewals; stakeholder mapping and written agreements. New business with NPV/IRR cases.'),
        ('Motivate, coach and develop teams to the next level',
         'Personal leadership of 5 electricians and 3 apprentices; 25 specialists and a 14-person team without formal '
         'authority; SLII, 1:1s, reviews, competence matrix and cross-training.'),
        ('Proactive, hands-on, challenging the status quo',
         'Rebuilt working routines at workshop, plant and project level; introduced Python/Claude tools where '
         'spreadsheets were the norm — innovative, but measured and with a documented productivity effect.')])
    m.page_break()

    m.models_table('FIRST 90 DAYS — SITE, CUSTOMERS, NUMBERS', ('Period', 'What happens, and how it is measured'), [
        ('Week 1–2',
         'On the floor in every function and on every shift, including one weekend: goods-in, put-away, picking, '
         'packing, dispatch, returns and the temperature and dangerous-goods areas. A short 1:1 with each shift lead '
         'and with the customer-facing roles. Systems walk-through: WMS, TMS and the customer portal.'),
        ('Day 30',
         'Baseline of the five tier-board numbers on one page. Contract obligations per customer written down '
         '(service levels, cut-off times, temperature ranges, reporting). Open issues from the last six months '
         'collected and classified: capacity, quality, systems or people.'),
        ('Day 60',
         'Prioritised improvement funnel agreed with site and regional leadership: at most five active projects, each '
         'with an owner, a business case and a measure. Stock accuracy routine with rolling cycle counts in place. '
         'Safety plan for the phase-2 expansion and the dangerous goods area.'),
        ('Day 90',
         'Measured movement in at least two of the five numbers, a customer review held on our own numbers rather '
         'than theirs, and a development plan per shift lead with cross-training mapped against the ramp-up. Written '
         'handover of what works, so the rhythm does not depend on me being in the building.')])

    m.section('THE OPERATING RHYTHM I WOULD RUN')
    m.para('Daily, weekly, monthly — three rhythms, no more. Daily: tier board and handover per shift, Gemba walk '
           'with the shift lead, deviations raised and owned the same day. Weekly: stock accuracy check, labour '
           'efficiency and overtime review against the volume forecast, and a short improvement stand-up where the five projects '
           'report one number each. Monthly: customer numbers sent before the review, cost per order and per pallet '
           'closed, safety statistics and near-miss trend, and one page to the regional organisation. Anything that '
           'cannot be read in ten minutes does not belong on the board.', after=80)

    m.section('GxP, GDP AND SAFETY IN ONE SYSTEM')
    m.para('In healthcare and chemical logistics, quality and safety are not two parallel tracks — they are the same '
           'routine seen from two angles, and operational excellence is what you get when both hold. Documented '
           'procedures, trained operators, temperature monitoring with '
           'alarms and defined responses, segregation and handling of dangerous goods, deviation and CAPA with '
           'verified effectiveness, change control before anything is altered, and audit readiness every day rather '
           'than the week before an inspection. I have worked this way under GMP, FDA and EMA, where a missing '
           'signature stops a handover, and I would rather spend an hour on the routine than a week on the finding.',
           after=80)

    m.section('CUSTOMERS AND COMMERCIAL GROWTH')
    m.para('A third-party site grows in two ways: the customers you have give you more volume, and the customers you '
           'do not have yet believe you can handle theirs. Both are built on the same thing — being able to show, '
           'with numbers, what the operation delivered last quarter and what it will deliver next. I would run '
           'quarterly reviews on our own data, bring improvement ideas to the customer instead of waiting for '
           'complaints, and prepare new business with a capacity and cost model rather than a gut feeling: what does '
           'this customer need in square metres, shifts, temperature zones and systems — and what does it earn at '
           'the price we can defend. That is also how customer satisfaction becomes sustainable growth instead of a '
           'single good quarter.', after=80)

    m.section('PEOPLE, LIFELONG LEARNING AND SHIFT CULTURE')
    m.para('Warehouse teams are built on shift leads. If the shift lead cannot run the board, cover an absence and '
           'say something difficult to a colleague, the site will always need the manager in the room. So I invest '
           'where it shows: a competence matrix with cross-training against the ramp-up plan, a named successor for '
           'every key function, 1:1s every two weeks, reviews that end with a concrete next step, and internal '
           'promotion before external hiring where the potential is there. The Academy and the Lifelong Learning '
           'vision are useful only if the training plan is tied to what the site actually needs next year — '
           'otherwise it is a catalogue.', after=80)

    m.section('DIGITAL AND AI IN A WAREHOUSE CONTEXT')
    m.para('I am an active Claude coder and build my own tools in Python: KPI follow-up pulled together from several '
           'sources into one page, capacity and labour models against a volume forecast, and investment cases with '
           'NPV, IRR and sensitivity for a new customer or a new warehouse phase. On a site this size, that is the '
           'difference between a two-day exercise and a two-hour one when a customer asks a question — and it lets '
           'the shift leads spend their time on the floor instead of in spreadsheets.', after=80)

    return m.save(path, title='Application and CV — Operations Manager, H.Essers Ringsted',
                  subject='Operations leadership with P&L ownership, GxP discipline and customer growth',
                  keywords='operations manager, warehousing, P&L, GxP, KPI, continuous improvement, leadership')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_HEssers_OperationsManager_Ringsted.docx')))
