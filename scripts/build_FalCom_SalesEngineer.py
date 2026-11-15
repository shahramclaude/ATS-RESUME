# -*- coding: utf-8 -*-
"""FalCom A/S (GN Group) — Sales Engineer, Ballerup. English posting -> English document.

Form (master/FORMKATALOG.md): opening **T** (a reader's situation: the operator in the
noise — and the fitter in the plant room, who has the same problem), structure
**The requirement behind the requirement** (five layers from tender line to acceptance),
register **The Trial** (baseline, scenario, noise, attenuation, radio, operator,
acceptance, finding, report).
Culture file: jd/FalCom_SalesEngineer_kultur.txt. Deadline 15/16 Nov 2026.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Sales Engineer · technical discovery, solution design and field trials'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('14 November 2026')
    m.meta('FalCom A/S, GN Group · Sales · Sales Engineer · Ballerup · requisition R30550')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Sales Engineer', bold=True, color='1A1A1A')

    def lp(text, after=42):
        return m.para(text, after=after, line=236)

    # ---------------------------------------------------------------- page 1
    lp('**An operator in a tracked vehicle and a fitter in a plant room have the same problem: the machine is '
       'louder than the person who has to give the instruction.** For the operator the answer is a headset '
       'that lets the engine through at a level that is safe and the voice through at a level he can act on. '
       'For the fitter it is a drawing, a schedule and a phone call at 06.40. Both of them find out whether '
       'the answer was right while standing in the noise — and the requirement that arrives in writing is '
       'almost never the one that decides.', after=38)

    lp('That is your posting, and it is the work I have been doing without the title: **the technical '
       'conversation before the signature**. The commercial dialogue belongs to the Business Development '
       'Manager, and **you "manage the technical discussions"**. You ask whether I can **"translate complex '
       'requirements into practical solutions"** — that is not a line I would have to learn: I have run that '
       'side in my own company since 2023, on 37 capital projects and on customer solutions where the '
       'requirement was one paragraph and the answer had to be a working system.', after=38)

    lp('**The requirement behind the requirement. Five layers — and each one is where a deal is won or lost.**',
       after=28)

    lp('**1. The requirement as written.** A tender line says "headset, noise-cancelling" and a price. It is '
       'the easiest thing in the deal to answer, and the fastest way to the wrong answer. At Novo Nordisk '
       'every change began with a written needs analysis, not a product: 37 projects were approved on it.',
       after=24)

    lp('**2. The requirement behind it.** What the user cannot do today. The only reliable way to find it is '
       'to ask the person who does the job, in their place, with their gloves on — 14 fitters, 25 specialists, '
       '12 technicians and a hall full of operators have taught me more about requirements than any '
       'specification.', after=24)

    lp('**3. What the environment does to the answer.** Dust, sweat, gloves, weight, battery, a cable that '
       'vibrates loose, a radio nobody can reach. In 24/7 operation I learned that the environment always '
       'beats the datasheet: it has to work on the worst day, handled by somebody who never read the manual.',
       after=24)

    lp('**4. What integration demands.** A headset is a system problem: **radio**, **intercom**, cabling, '
       '**configuration**, existing fleet, and whoever owns the fleet. Twenty years at exactly those '
       'interfaces — SCADA and PLC in operation, customer systems from requirements through integration to '
       'go-live, other trades on eleven simultaneous sites.', after=24)

    lp('**5. What acceptance proves.** A trial worth the name has a baseline taken before, a scenario hard '
       'enough, and an **acceptance** criterion agreed before anybody puts the equipment on. FAT/SAT and '
       'IQ/OQ/PQ taught me the discipline; at Lynetten the same discipline produced **over 40 % lower energy '
       'consumption** — the measurement was the argument.', after=24)

    lp('**And after the signature:** feedback that reaches Product and R&D while it still matters, and assets '
       'reused instead of rebuilt. My documentation is written while the work happens, and my templates are '
       'three pages because a fourth would not get used.', after=34)

    lp('**Where my record is thinner, stated plainly.** I have not held a pre-sales title, and I have not '
       'worked inside defence, tactical communication or hearing protection: my acoustics come from '
       'ventilation and engine rooms, not from hearing-protection standards. What I bring instead is a '
       'technical-commercial record with the consequences attached — quotation, solution, delivery, handover '
       '— plus regulated delivery and the habit of learning a product range from the engineers who built it.',
       after=34)

    lp('**Why FalCom, in your words.** GN began in 1869 laying telegraph cables to bring continents closer, '
       'and that is still the business: **"bringing people closer"** through technology that **"enhances '
       'hearing and sight"**. **"Built on 150 years of innovation"**, now eight brands in 100 countries — and '
       'FalCom is the part of that heritage that has to work when everything else fails: **"tactical '
       'communication and hearing-protection solutions"**, where you want to increase **"technical '
       'credibility, solution quality, and win probability"** and, as you write, deliver **"quality outcomes '
       'for our customers"**. You write that **"you will be part '
       'of an evolving organization"**, that **"your contribution is appreciated"**, that **"We trust our '
       'people"** and that you encourage **"flexible work whenever possible"** — in my own company the '
       'contribution was visible in the order book every month, and I am comfortable being judged on it.',
       after=32)

    lp('**On the process.** You say you value **"transferable skills"**, that applicants receive '
       '**"equal consideration for employment"** inside **"an inclusive recruitment process"**, and you add '
       '**"We encourage you to apply"** — I read that as an invitation rather than a formality, because my '
       'way into this work was not a pre-sales title. So I would rather show it than describe it: give me one '
       'real opportunity and I will bring the discovery questions, the configuration and the risk list — and '
       'on the **"field trials, and evaluations"** the **"technical proof points"** that make a technical '
       'decision-maker comfortable.', after=32)

    lp('**Practical.** I live in Måløv, about ten minutes from Lautrupbjerg, so in-person collaboration is the '
       'easy choice. **PRINCE2 certified**; English working language, Danish first; travel to sites and '
       'trials no obstacle; a background check is none either; I can start at short notice.', after=12)

    m.meta('Kind regards', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('**Technical-commercial engineer with a P&L, 37 capital projects and a customer-facing record '
           'behind him** — own company since 2023 quoting, designing and delivering technical work; PRINCE2 '
           'certified, authorised maskinmester (LV/MV/HV), B.Tech in technology management. Requirements into '
           'configurations, configurations into trials, trials into acceptance — with GMP/FDA documentation '
           'as the standard for proof. English working language, ten minutes from Ballerup.', after=60)

    m.section('THE TRIAL — HOW I RUN A TECHNICAL SALE')
    for label, body in [
        ('The baseline',
         'Measure the situation before the solution: what happens today, how often it fails, what it costs '
         'the user. Without a baseline a trial proves nothing but enthusiasm.'),
        ('The scenario',
         'The hard case, not the demo case: the operator with gloves, the noise at full load, the cable that '
         'has to survive a vehicle. If it holds there, it holds.'),
        ('The operator',
         'The person who will use it has the requirement; the person who signs has the budget. Both are in '
         'the room, and they are not told the same story in the same words.'),
        ('The risk',
         'Integration, product readiness, delivery date — named early, priced early, and closed or accepted '
         'in writing before the order, never after.'),
        ('The finding',
         'One page: what was measured, what was expected, what differed, what it means for the next '
         'opportunity. Written the same week, not the same quarter.'),
        ('The report',
         'The customer gets the truth in their own language, the sales team gets the numbers, Product and '
         'R&D get the gaps. A trial nobody wrote down is a favour, not a reference.'),
    ]:
        m.bullet(label, body, after=16)

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director', 'ELOHVAC ApS · Copenhagen · May 2023–present',
         '8 employees · full P&L · technical sales, quotation and delivery',
         [('Technical sales with the consequences attached',
           'Quotations, solution design, customer dialogue and negotiation on technical work — priced by me, '
           'delivered by my own team, and answered for when the site turned out to be different from the '
           'drawing.'),
          ('Commercial and technical risk in one place',
           'Scope, price, capacity and delivery date decided together, with the risk named before the '
           'signature; **over 40 % productivity gain** measured in estimating and documentation.')]),
        ('Co-owner and CTO / Technical Lead, AI department',
         'Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 (alongside ELOHVAC)',
         '4–10 people · customer solutions from requirement to go-live',
         [('From one paragraph to a working system',
           'Requirements, architecture, integration, configuration, demonstration and handover with '
           'customers in the room; documentation the customer could run afterwards.'),
          ('Two organisations, one plan',
           'Matrix leadership across two companies with written priority agreements; the company has ceased '
           'trading and the department was closed in order.')]),
        ('Senior Commissioning Engineer / Project Manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · GMP/FDA/EMA',
         [('Proof, not opinion',
           'Written needs analysis before any solution; **FAT/SAT**, **IQ/OQ/PQ**, **validation** and '
           '**acceptance** criteria agreed before delivery; zero critical deviations at handover on 37 '
           'projects.')]),
        ('Project and Workshop Manager', 'Ventek-Air · Copenhagen · Jan 2022–Nov 2022',
         '14 employees · 11 simultaneous site projects',
         [('Interfaces and site reality',
           '11 sites and 14 fitters, subcontractors and other trades coordinated daily; noise, space and '
           'access decided more than the datasheet did.')]),
        ('Operations and Maintenance Manager', 'Biofos (Lynetten) · Copenhagen · Aug 2017–Jan 2022',
         'Wastewater plant in 24/7 operation · SCADA, PLCs, HV switchgear',
         [('Measured improvement',
           '**Over 40 % lower energy consumption** through measurement and re-commissioning; 24/7 duty, '
           'incidents and operational users with no patience for theory.')]),
        ('Electromechanical Technician / Production Team Lead', 'ARJ Engineering · Tehran · Dec 2003–Mar 2010',
         '12 technicians · machine shop · machinery and equipment',
         [('Hands-on with the equipment',
           'Fault finding, calibration and repair of machinery and **equipment**; training and follow-up for '
           '12 technicians.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=16)

    m.section('EDUCATION, CERTIFICATION AND AUTHORISATION')
    m.edu('PRINCE2 certified project manager', 'AXELOS / PeopleCert · certification held')
    m.edu('B.Tech, Technology Management and Mechanical Engineering',
          'Copenhagen School of Marine and Technical Engineering · 2017–2022 · GPA 7.6/12')
    m.edu('Authorised maskinmester (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('Refrigeration and ventilation technology · AMU',
          'Mercantec 2021 · STCW, Danish Maritime Authority 2021')
    m.edu('Electrical and mechanical engineering design, electrical engineering',
          'Tehran Technical University · 2000–2003 · EQF 6')

    m.section('LANGUAGES, IT AND PRACTICAL')
    m.para('English (working language) · Danish (first language) · Persian (mother tongue) · **IT**: '
           '**CRM** and quotation workflow, **Excel** cost and configuration models, **ERP**, documentation and '
           'quality systems, **Python** for own analysis · Måløv, ten minutes from Lautrupbjerg · Travel to '
           'customer sites and trials · Background check: no objection · Start at short notice.', after=40)

    m.models_table('THE ROLE AS ADVERTISED — WHAT I BRING', ('Requirement', 'Evidence'), [
        ('Customer-facing technical-commercial role: pre-sales, systems or solution engineering',
         'Technical sales in my own company since 2023 — quotation, solution design and negotiation — plus '
         'customer solutions at Data Power from requirements to go-live. No pre-sales title held.'),
        ('Communicate credibly with operational users and with technical decision-makers',
         'Twenty years of both: fitters, technicians and operators on the floor, and directors, authorities '
         'and steering groups in the meeting — the same facts, in two languages, at two altitudes.'),
        ('Present, facilitate technical discussions and make complex information clear',
         'Presented FAT/SAT results, commissioning findings and business cases to mixed audiences; the rule '
         'is one page, three numbers, and the decision that follows from them.'),
        ('Customer-focused: listen carefully, understand operational needs, translate them into solutions',
         'Requirements were gathered on site, with the people doing the work — 11 sites, 37 projects, 25 '
         'specialists — and then written down so both sides could disagree with them.'),
        ('Structured problem-solving and industry insight to assess challenges and identify risks',
         'Risk named before the signature, not after: scope, integration, capacity, delivery date and price, '
         'each with an owner and a mitigation in writing.'),
        ('Partner with Business Development Managers from discovery to proposal, trial, negotiation, handover',
         'The commercial dialogue belongs to the seller; the technical one to me — that split is exactly how '
         'I have worked with customers and suppliers in my own business.'),
        ('Manage technical discovery with customers, end users, partners and technical stakeholders',
         'Discovery as a structured conversation: what is done today, by whom, with what equipment, where it '
         'fails, and what "good" would look like — then the configuration.'),
        ('Translate operational requirements into viable solution configurations',
         'Requirements into a configuration, with the cost consequence priced: quotations, variants and '
         'technical solutions built for 11 sites and for customer systems at Data Power.'),
        ('Deliver technical presentations, demonstrations, workshops, field trials and evaluations',
         'Field work is my normal: commissioning, re-commissioning, **field trial** conditions in a 24/7 '
         'plant, and demonstrations to the people who would have to use the result.'),
        ('Turn product capabilities into customer-relevant operational value, differentiators, proof points',
         'The value I can defend is measured: over 40 % lower energy consumption at Lynetten and over 40 % '
         'productivity gain in my own company — both numbers a customer could audit.'),
        ('Support technical content for tenders, proposals, compliance responses and presentations',
         'Tenders, **RFPs**, quotations and technical annexes written by me for eight years of my own contracts, plus '
         'the **compliance** documentation that made 37 GMP projects close without critical deviations.'),
        ('Identify and manage technical, integration, product-readiness and delivery risks early',
         'Early risk is cheap risk: interfaces mapped before mobilisation, readiness checked at FAT rather '
         'than on site, and a delivery date only promised once capacity was reserved.'),
        ('Coordinate technical contributions across Product, R&D, Operations and external partners',
         'Coordinated specialists, suppliers, subcontractors and internal engineering across 37 projects, 11 '
         'sites and two companies — with one list of open technical questions and one owner per line.'),
        ('Capture customer feedback and develop reusable technical sales assets',
         'Feedback into templates, checklists and standard solutions that were used again: three-page '
         'business case, decision log, handover checklist — assets, not documents.'),
        ('Report to the Head of Sales and work closely with Business Development Managers',
         'Reported to owners, directors and steering groups my whole career; used to a sales organisation '
         'where the technical role reports into the commercial line and wins with it.'),
        ('Work with Product, R&D, Engineering, Operations and external partners',
         'Interface person by habit: engineering on one side, operations on the other, and the partner or '
         'subcontractor in the middle who also has a deadline.'),
        ('Spend significant initial time with Engineering and R&D to learn the products',
         'How I have learned every product I have sold: from the people who built it, in their workshop, '
         'until I could explain the limitation as clearly as the feature.'),
        ('Create solution clarity, manage technical risks, communicate across audiences in an evolving organisation',
         'Structure without bureaucracy — one page per opportunity, one decision log, one weekly forum — '
         'built to survive an organisation where roles and processes are still moving.'),
        ('Tactical communications, hearing protection, defence technology, connectivity or related field',
         'Not my background. The transferable part is real: **noise**, **attenuation** as a requirement, '
         '**radio** and **intercom** integration, and users whose equipment must work when it matters.'),
        ('English working language; full-time at the Ballerup headquarters',
         'English is my working language and Danish my first; the office is ten minutes from home, so '
         'presence is the default rather than the exception.'),
        ('Flexible work: in-person collaboration when it is better than hybrid',
         'Twenty years of site work have made me prefer the room: the fastest technical decision I know is '
         'three people and a drawing, not a thread.'),
        ('Background check as part of the recruitment process',
         'No objection; clean record, authorised maskinmester and documented employment history — happy to '
         'complete the check at the earliest opportunity.'),
    ], widths=(2500, 7846))

    m.section('FIRST 90 DAYS')
    for b in (
        'Weeks 1–3: sit with Engineering and R&D — build the product map, the configuration options and the '
        'limitations written down in my own words; ride along on two customer calls without speaking.',
        'Weeks 4–6: take the discovery questions into live opportunities and write the first baseline — what '
        'the customer does today, what it costs, what "good" would look like.',
        'Weeks 7–10: own the technical content of one tender or proposal end to end, with the risk section '
        'written early enough to price it.',
        'Weeks 11–13: run or document one field trial properly — baseline, scenario, acceptance criterion, '
        'finding — so the next trial starts from a template instead of a blank page.'):
        m.bullet('', b, after=16)

    m.section('WHAT I WOULD ASK')
    for b in (
        'Which markets does this role cover, and how much of the year is spent at customer sites?',
        'Where does the technical answer meet Product and R&D today — is there a route for feedback, or is '
        'it still informal?',
        'What does a good first year look like: win rate on strategic opportunities, or credibility with the '
        'technical stakeholders?'):
        m.bullet('', b, after=16)

    m.para('**I would welcome a conversation about the opportunities ahead.** Contact: +45 93 99 95 14 · '
           'ajlooshahram@gmail.com.', after=20)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_FalCom_SalesEngineer.docx')
    build(out)
    print(out)
