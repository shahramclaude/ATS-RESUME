# -*- coding: utf-8 -*-
"""Kardex — Area Sales Manager, Denmark. English posting -> English document.

Form (master/FORMKATALOG.md): opening **U** (the labour force: the hard problem is not the
building, it is the twelve people who have to walk in it), structure **The payback page**
(five lines that must survive the customer's controller, plus the page after the signature),
register **The Aisle** (aisle, bin, tote, pick, replenishment, footprint, cycle time,
uptime, throughput).
Culture file: jd/Kardex_AreaSalesManager_kultur.txt. No deadline — reviewed continuously.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Area Sales Manager · technical selling, business case and territory ownership'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('14 November 2026')
    m.meta('Kardex · Nordic sales · Area Sales Manager, Denmark')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Area Sales Manager', bold=True, color='1A1A1A')

    def lp(text, after=42):
        return m.para(text, after=after, line=236)

    # ---------------------------------------------------------------- page 1
    lp('**The hardest problem in a Danish warehouse is not the building. It is the twelve people who are '
       'supposed to walk in it.** Every automation case that gets signed starts there: a wage bill that keeps '
       'climbing, an advertisement that stays open for months, and a picker who spends more of the shift '
       'walking than picking. The machine is the answer. The staffing problem is the reason.', after=38)

    lp('That makes it a commercial conversation with a technical spine — the only kind I have had for twenty '
       'years. I have sold technical work in my own company since 2023: quotation, solution design, '
       'negotiation, delivery and the year afterwards, with my own money at risk. **"Experience selling '
       'technical and value-based solutions"** reads differently when the invoice is yours.', after=38)

    lp('**The payback page. Five lines — every one of them has to survive the customer\'s own controller.**',
       after=28)

    lp('**The hours.** How many people, how many shifts, how much of the day is spent moving instead of '
       'working. I have run eight employees and 14 fitters, so I know what an hour costs fully loaded — and '
       'that the number has to hold in the customer\'s spreadsheet, not in mine.', after=24)

    lp('**The square metres.** In Greater Copenhagen a square metre of floor is a rent bill, and every metre '
       'of aisle is a metre nobody stores anything in. On eleven simultaneous sites I learned that the '
       'footprint decides the solution long before the equipment does: the aisle you remove is the saving the '
       'customer can see, and the layout that replaces it decides **slotting** and **ergonomics** for the '
       'people who work in it.', after=24)

    lp('**The errors.** A pick that is wrong costs a return, a credit note and a phone call. In a GMP plant '
       'the same logic runs at a higher price: 37 capital projects, documentation written while the work '
       'happened, **zero critical deviations** at handover. Accuracy is a process, not a promise.', after=24)

    lp('**The capacity.** Growth without a new building — higher **throughput** through the same four walls, a '
       'shorter **cycle time** per order and a peak that does not require hiring in December. That is a design '
       'question, and it is answered with numbers before it is answered with a quotation.', after=24)

    lp('**The risk of standing still.** What another year of manual picking costs, priced and put on the same '
       'page as the investment — an **ROI** the customer\'s own controller can audit — with waiting listed as '
       'a cost rather than a neutral choice. Customers do not buy a machine; they buy the difference between '
       'two futures.', after=24)

    lp('**And the page after the signature** — installation, uptime, a **service agreement** that keeps the '
       'promise measurable, and the **total cost of ownership** over ten years rather than the price on day '
       'one. My handovers end with somebody else able to run what was built; a system is only worth its '
       'payback if it is still picking at the promised rate in year three.', after=34)

    lp('**Where my record is thinner, stated plainly.** I have not sold intralogistics or warehouse '
       'automation, and I have no CRM administration from a large sales organisation — my pipeline has been '
       'run in writing and in my own systems, because the company was mine. What I bring instead is a '
       'technical-commercial record with the consequences attached, industrial customers in this region, and '
       'the ability to walk into a building, see where the flow breaks, and put a price on fixing it. A '
       '**vertical lift module**, a carousel and a **warehouse management** integration are new words to me; '
       'the questions underneath them are not.', after=34)

    lp('**Why Kardex, in your words.** A **"global leader in automated storage, retrieval, and material '
       'handling solutions"** with a **"customer-centric approach"**, and a Nordic team that **"combines local '
       'market knowledge with the strength of an international company"** — that is the shape of the job I do '
       'best: the local relationship, the international answer. You write that **"We value teamwork, '
       'entrepreneurship, and long-term customer relationships"**, that the team has **"short decision '
       'paths"** and **"strong team spirit"**, and that the role carries a **"high degree of autonomy and '
       'responsibility"** and **"the freedom and responsibility to drive their own success"**. I have run my '
       'own territory for three years, so **"taking ownership of their territory"** is not a new idea for me.',
       after=32)

    lp('**On the process.** You want someone **"self-driven, commercially minded"** with a **"strong '
       'commercial mindset"**, comfortable **"leading complex sales processes"**, **"creating tailored '
       'solutions"** with internal experts, and able to turn an operation into **"business value"** that will '
       '**"support their operational and business goals"** — while **"sharing market insights"** with the '
       'Nordic team. That is how I sell, and it is why the **"industry-leading technology"**, the **"strong '
       'brand, high employee engagement"** and the **"focus on innovation and continuous development"** you '
       'already have would be working with me rather than against me: the hard part of helping a customer '
       '**"optimize their intralogistics processes"** is not the machine, it is proving the payback. You write '
       'that **"We review applications continuously"**, so this one goes today rather than at the end of the '
       'month.', after=32)

    lp('**Practical.** Måløv, north-west of Copenhagen · **driver\'s licence category B and my own car** · '
       'Danish fluent, English at working level · full Danish territory, including the travel that comes with '
       'it · available after agreement.', after=12)

    m.meta('Kind regards', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('**Technical-commercial seller with his own P&L, 37 capital projects and industrial customers '
           'behind him** — owner since 2023, quoting, designing, negotiating and delivering technical work; '
           'PRINCE2 certified, authorised maskinmester (LV/MV/HV), B.Tech in technology management. Business '
           'case before equipment, footprint and capacity before price, and a handover that still works in '
           'year three. Danish fluently, English at working level, driver\'s licence B.', after=60)

    m.section('THE PAYBACK PAGE — HOW I SELL A TECHNICAL SOLUTION')
    for label, body in [
        ('The hours',
         'Fully loaded cost per hour, per shift, per pick: I have paid wages myself, so I price labour the way '
         'the customer\'s controller does — including the hours nobody invoices.'),
        ('The square metres',
         'The aisle is rent. Removing floor space or freeing it for production is the saving a customer can '
         'see on the lease, and it is the first number I look for in a building.'),
        ('The errors',
         'A wrong pick has a price: return, credit note, phone call, and sometimes a customer. Accuracy is '
         'designed into the process and checked at handover, not promised.'),
        ('The capacity',
         'Growth without building: more volume through the same walls, a peak absorbed without hiring in '
         'December, and a layout that can be extended in the right direction.'),
        ('The cost of waiting',
         'One more year of manual handling is a number, and it belongs on the same page as the investment. '
         'Waiting is a decision, so it gets a line and a price.'),
        ('The page after the signature',
         'Implementation, uptime, service and the rate the system still picks at in year three — the part that '
         'decides whether the reference is usable.'),
    ]:
        m.bullet(label, body, after=16)

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director', 'ELOHVAC ApS · Copenhagen · May 2023–present',
         '8 employees · full P&L · quotation, negotiation and delivery',
         [('Selling technical solutions with the risk attached',
           'Quotations, solution design, negotiation and contract on technical work priced by me and delivered '
           'by my own team; **over 40 % productivity gain** measured in estimating and documentation.'),
          ('A territory of my own',
           'Customer list, pipeline and follow-up built without a sales organisation behind me — prospecting, '
           'offers, price talks and the discipline of a written quotation that has to hold.')]),
        ('Co-owner and CTO / Technical Lead, AI department',
         'Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 (alongside ELOHVAC)',
         '4–10 people · customer solutions from requirement to go-live',
         [('From requirement to a working system',
           'Requirements, architecture, integration, configuration and handover with the customer in the room; '
           'documentation the customer could run afterwards.'),
          ('Two organisations, one plan',
           'Matrix leadership across two companies with written priority agreements; the company has ceased '
           'trading and the department was closed in order.')]),
        ('Senior Commissioning Engineer / Project Manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · GMP/FDA/EMA',
         [('Business case, capacity and proof',
           'Written needs analysis before any equipment; **FAT/SAT**, **IQ/OQ/PQ** and acceptance criteria '
           'agreed in advance; zero critical deviations at handover on 37 projects.')]),
        ('Project and Workshop Manager', 'Ventek-Air · Copenhagen · Jan 2022–Nov 2022',
         '14 employees · 11 simultaneous site projects',
         [('Layout, flow and the space you have',
           'Eleven sites and 14 fitters coordinated daily; ducts, access and available space decided the '
           'solution more often than the specification did.')]),
        ('Operations and Maintenance Manager', 'Biofos (Lynetten) · Copenhagen · Aug 2017–Jan 2022',
         'Wastewater plant in 24/7 operation · SCADA, PLCs, HV switchgear',
         [('Uptime with a number on it',
           '**Over 40 % lower energy consumption** through measurement and re-commissioning; 24/7 duty means '
           'the plant has to keep running while you improve it.')]),
        ('Electromechanical Technician / Production Team Lead', 'ARJ Engineering · Tehran · Dec 2003–Mar 2010',
         '12 technicians · machine shop · machinery and equipment',
         [('Hands-on with the equipment',
           'Fault finding, calibration and repair of machinery and equipment; training and follow-up for 12 '
           'technicians.')]),
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
    m.para('Danish (fluent, first language) · English (working level) · Persian (mother tongue) · **IT**: '
           'quotation and offer workflow, pipeline and follow-up in writing, **Excel** cost, capacity and '
           'payback models, **ERP**, documentation and quality systems · **Driver\'s licence category B and '
           'own car** · Based in Måløv, covering the Danish market · Available after agreement.', after=40)

    m.models_table('THE ROLE AS ADVERTISED — WHAT I BRING', ('Requirement', 'Evidence'), [
        ('Several years of sales experience within automation, intralogistics, warehouse solutions or material handling',
         'Not my industry. My sales record is technical solutions in my own company since 2023, industrial '
         'customers in this region and 37 capital projects — the customer type fits, the product area does not '
         'yet.'),
        ('B2B sales with a successful track record of selling technical solutions',
         'Eight years of quoting, negotiating and delivering technical work to businesses — the last three with '
         'full P&L, 8 employees and a turnover that depended on my own offers; the invoice I sold was mine to '
         'honour.'),
        ('Selling technical and value-based solutions to industrial or logistics customers',
         'Customers have been industrial: process plants, contractors, property and facility owners, and pharma '
         'production — sold on capacity, uptime and cost per hour rather than on a datasheet. That is '
         '**value-based selling** in plain language.'),
        ('Strong commercial drive combined with technical understanding',
         'Both in one person by necessity: I design the solution and price it, then live with the margin. '
         'Authorised maskinmester and B.Tech, with a P&L since 2023.'),
        ('Experience managing complex sales processes',
         'Long cycles with several decision-makers: scope and price negotiated against drawings, **tender** '
         'documents and technical annexes, with a budget owner, a technical **stakeholder** and a delivery '
         'date that had to hold. **Solution selling**, in the sense that the offer describes the operation.'),
        ('Experience building long-term customer relationships',
         'Repeat business is how a small company survives: the same customers, the same contractors and the '
         'same suppliers for years — the relationship was the pipeline.'),
        ('Developing new business opportunities and expanding presence in Denmark',
         'Built the customer base of my own company from zero in three years, in a market where nobody owed me '
         'a meeting or a reference.'),
        ('Managing and developing key customer relationships',
         'A handful of **key account** customers carry most of the revenue in a company of eight; those '
         'relationships were maintained personally, including the difficult conversations about price and '
         'delay.'),
        ('Identifying customer needs and creating tailored solutions together with internal experts',
         'Requirements on site, solution with the fitters, specialists and suppliers who had to build it — 11 '
         'sites, 37 projects, and a configuration that had to be buildable, not just sellable.'),
        ('Leading the sales process from first contact to negotiation and contract signing',
         'First call to signature in my own company, hundreds of times: enquiry, site visit, offer, price talk, '
         'contract, and the delivery that decides whether there is a next one.'),
        ('Representing the company at customer meetings, trade fairs and industry events',
         'Twenty years in front of customers, authorities, contractors and steering groups; comfortable in a '
         'room where the customer brings three people and two of them are sceptical.'),
        ('Sharing market insights and collaborating across the Nordic sales team',
         'Used to working with colleagues and partners across borders in an international group at Novo, and to '
         'sharing what a customer said rather than what I wish he had said.'),
        ('Experience working with CRM systems and a structured sales approach',
         'No CRM administration in a sales organisation — my pipeline has been run in writing and in my own '
         'systems because the company was mine. The structure exists: every offer, date, owner and follow-up.'),
        ('Strong communication and negotiation skills',
         'Same facts at two altitudes, in Danish and English: the operator gets the consequence, the buyer gets '
         'the number, and both get the same date.'),
        ('Ability to understand customer needs and translate them into business value',
         'A needs analysis before equipment, a payback page before price, and a decision the customer can '
         'defend to his own board — the way 37 capital projects were approved.'),
        ('Fluency in Danish and good working proficiency in English',
         'Danish is my first language and the language of every customer meeting; English is my working '
         'language in documentation, suppliers and international colleagues.'),
        ('Valid driver\'s licence, category B',
         'Licence category B and my own car, and daily driving is not a novelty: Måløv to Kalundborg, Esbjerg or '
         'Aalborg in a week is normal when 11 sites and 37 projects are running.'),
        ('Self-driven and commercially minded, taking ownership of a territory',
         'Three years of owning everything: the pipeline, the price, the delivery and the loss when a deal went '
         'elsewhere. Nobody was going to do the follow-up for me.'),
        ('Working closely with internal experts and colleagues in an international organisation',
         'Interface person by habit: engineering on one side, operations on the other, supplier and '
         'subcontractor in the middle — with one list of open questions and an owner per line.'),
        ('Independent role without leadership responsibility, with full responsibility for the sales process',
         'Comfortable as the one who carries the deal alone; I have led teams, and I know the difference '
         'between leading people and carrying a number.'),
        ('Danish market focus within a Nordic sales team',
         'Danish market, Danish customers, Danish contracts — and a Nordic team above me to bring the cases '
         'into when the answer is bigger than one country.'),
        ('Selling to industrial and logistics customers in a global company',
         'Industrial customers by record; logistics by understanding — the plant room and the warehouse solve '
         'the same problem, which is goods and time in too little space.'),
    ], widths=(2500, 7846))

    m.section('THE FIRST CONVERSATION — WHAT I WOULD DO IN IT')
    for label, body in [
        ('The visit',
         'Walk the warehouse before the meeting: where goods arrive, where they wait, who walks furthest, '
         'what is stored on the floor because the shelves are full. The problem is visible before anybody '
         'describes it.'),
        ('The numbers',
         'Orders per day, lines per order, peak month, headcount per shift, square metres and the rent per '
         'square metre. Five numbers, given by the customer, and the case starts to exist.'),
        ('The expert',
         'Bring the internal expert in early — layout, tray heights, load capacity, controls — so the '
         'solution is engineered while the relationship is still warm, not after the offer is sent.'),
        ('The offer',
         'One page of payback and one page of price, with the assumptions visible, the options side by side '
         'and the service agreement priced rather than implied.'),
        ('The no',
         'If a smaller answer is the honest one, say so. A customer who was told not to buy yet is the '
         'customer who calls back in eighteen months — and the one who refers you in the meantime.'),
    ]:
        m.bullet(label, body, after=16)

    m.section('FIRST 90 DAYS')
    for b in (
        'Weeks 1–3: learn the portfolio from the inside — Shuttle, carousel, Miniload, AutoStore — and go on '
        'customer visits with a colleague without taking the pen.',
        'Weeks 4–8: map the Danish installed base and the twenty industrial accounts worth a first call; write '
        'the payback page for two live cases and test it on a controller.',
        'Weeks 9–12: run the first opportunity end to end — site visit, layout and capacity numbers, internal '
        'experts, quotation, negotiation — and put the loss or the win on one page for the Nordic team.'):
        m.bullet('', b, after=16)

    m.section('WHAT I WOULD ASK')
    for b in (
        'Which product line carries the Danish territory today — Remstar, Miniload or AutoStore — and where is '
        'the growth supposed to come from?',
        'How much of the year is expected to be new business, and how much is the installed base?',
        'Is there a Danish technical colleague to build the layout and the numbers with, or does the sales role '
        'carry that too?'):
        m.bullet('', b, after=16)

    m.para('**I would welcome a conversation about the Danish territory.** Contact: +45 93 99 95 14 · '
           'ajlooshahram@gmail.com.', after=20)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Kardex_AreaSalesManager.docx')
    build(out)
    print(out)
