# -*- coding: utf-8 -*-
"""Centrica Energy — Senior Portfolio Manager (Aalborg / Copenhagen / Antwerp).

English posting → English deliverable: letter page 1, CV pages 2–3, 90-day plan + sections page 4.
Policy: master/README.md — extreme confidence, no caveats.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Senior Portfolio Manager · Asset-backed trading, pricing and portfolio risk'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Copenhagen'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('6 November 2026')
    m.meta('Centrica Energy · Senior Portfolio Manager · Aalborg / Copenhagen / Antwerp')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Senior Portfolio Manager, Centrica Energy (R0084135)', bold=True, color='1A1A1A')
    m.para('For the Portfolio Management team', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('A power purchase agreement is a long-term bet on how a machine will behave: how often the wind drops, '
           'how much a battery has degraded by year nine, how much output a grid operator will actually let '
           'through on a Sunday in July. The price is set by a model. The truth is in the asset. I have spent '
           'twenty years on the asset side — running 24/7 plant, commissioning new equipment and cutting energy '
           'consumption by more than 40 % on a live site — and the last three years building the commercial models '
           'that turn those numbers into prices. That is where I want to sit: pricing profitable offtake against real '
           'asset behaviour, across the power markets Centrica Energy trades.', after=80)

    m.para('**I would work the portfolio on four fixed things.** First **every contract is priced on assumptions '
           'about the asset**, so the assumptions have to be written down, owned and tested against what the plant '
           'actually delivers: availability, degradation, curtailment, grid limits and a forecasting assumption that is '
           'tested rather than inherited. Second **every contract is a position and has to be measured every day**: '
           'volume, price, imbalance, counterparty, tenor and the hedging position behind it on one sheet, one number that '
           'Origination, Trading and Risk all read the same way, and a performance evaluation every month. Third **the interface between Origination and Trading is where the money leaks** — '
           'a structure that is brilliant in the term sheet and unbookable in the systems costs more than the '
           'margin it promised, so the contract has to be designed with the desk that has to run it. Fourth **a '
           'new market is a project**: legal, systems, settlement, credit and operations, with a named owner and a '
           'date — which is the discipline I have spent my career applying to technical portfolios.', after=80)

    m.para('On the asset side I know what a trading model is describing. For five years I was maintenance and '
           'operations manager at **Lynetten (Biofos)**, a critical plant running around the clock: pumps, '
           'blowers, transformers, switchgear, SCADA and the energy bill that came with them. I built the '
           'measurement and the follow-up that cut consumption by **more than 40 %**, and I learned where '
           'availability disappears: in the winter, at shift change, at the component nobody stocked. At **Novo '
           'Nordisk** I commissioned **37 capital projects worth DKK 2–10 m each** with 25 specialists, through '
           'specification, **FAT/SAT, IQ/OQ/PQ** and handover into live production — which is the same question an '
           'offtaker asks: will this asset do what the contract says, and who carries the risk if it does not?',
           after=80)

    m.para('On the commercial side I have carried a P&L since 2023 as owner of **ELOHVAC**, an electrical contracting '
           'company with **five electricians and three apprentices**. Every quotation I sign is a small version of '
           'the same trade: a price agreed today against a cost and an availability that move, a '
           'margin that is real only if the job runs the way I modelled it, and a customer who notices in week '
           'three. I have priced, negotiated, re-priced when copper moved, chased the payment and carried the '
           'result. That is a small portfolio, but it is mine and it is run with ownership, and it has taught me more '
           'about risk than any '
           'spreadsheet.', after=80)

    m.para('The quantitative part is where I have invested deliberately. I build my own tools in **Python** — '
           'pricing and margin models, capacity and consumption models, checklists and dashboards that replaced '
           'manual work and delivered **over 40 % productivity gain** — and I work daily in **Excel and Power '
           'Query** with data that has to be reconciled before it can be trusted. I am comfortable with an API, a '
           'SCADA export and a price series in the same afternoon, and I have no patience for a dashboard nobody '
           'opens. What I bring is the half of the trade that is hardest to hire: the assets, the contracts, the '
           'costs and the operational reality the models are trying to describe — and the habit of arguing with '
           'the assumptions until they hold.', after=80)

    m.para('What attracts me to Centrica Energy is the scale and the direction: a **pan-European portfolio above '
           '20 GW** across wind, solar and battery storage, where portfolio optimisation is the product; a business '
           'built on integrating renewables and flexible assets into the grid through the energy transition and the '
           'sustainability that follows from it; and a role that sits exactly where asset and market meet. Copenhagen is one of the three locations and happens to be '
           'twenty-five minutes from my door, and the chance to work across Aalborg, Copenhagen and Antwerp with '
           'origination and trading is the kind of scope I have been building towards from the technical side.',
           after=80)

    m.para('Practical: I live in Måløv, twenty-five minutes from central Copenhagen, with a **driving licence and my '
           'own car**, and I am available by agreement. I work in **English** and Danish professionally, and I am '
           'used to reporting to a management team in writing, on a date, with the numbers attached. I would like '
           'to hear how the portfolio is priced today and where the assumptions are weakest — that is where I '
           'would start.', after=70)
    m.meta('Kind regards', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('Commercially accountable engineer with 20+ years in energy, technical operations and asset management — '
           'state-authorised marine engineer (LV/MV/HV) with a B.Tech in technology management and mechanical '
           'engineering. Five years running a critical 24/7 energy plant, where measurement and follow-up cut '
           'consumption by over 40 %; three years as owner of an electrical contracting business with full P&L, '
           'pricing, contracts, margin and payment risk; and two years commissioning 37 capital projects worth '
           'DKK 2–10 m each against specification, acceptance and handover. Builds his own pricing, capacity and '
           'follow-up models in Python and Power Query, and reads a market price series and a plant trend with the '
           'same suspicion.', after=80)

    m.section('ASSETS, CONTRACTS AND DATA')
    for label, body in [
        ('Pricing and commercial models',
         'Quotation and margin models built from cost, capacity and risk; re-pricing when input costs moved; '
         'budgets and monthly follow-up where the variance had to be explained, not smoothed.'),
        ('Contracts and counterparties',
         'Contract terms negotiated, documented and delivered: scope, price, indexation, payment terms and '
         'liability — with the customer conversation that follows when reality differs from the offer.'),
        ('Portfolio risk and follow-up',
         '37 parallel capital projects with risk registers, monthly reporting of progress, cost and risk to '
         'management; energy consumption, tariffs and load profiles measured and reduced by over 40 %.'),
        ('Asset performance',
         'Availability, downtime and criticality on a 24/7 plant: condition-based maintenance, spare-parts policy '
         'and measured before-and-after results rather than opinions.'),
        ('Data and programming',
         'Python for pricing, capacity and reporting models; Excel and Power Query for reconciliation; dashboards '
         'and automated reports that replaced manual work with over 40 % productivity gain.'),
        ('Stakeholders and delivery',
         'Work agreed across commercial sales, engineering, suppliers, authorities and operations — 25 '
         'specialists, subcontractors and external fitters coordinated to a date.')]:
        m.bullet(label, body, after=25)

    m.models_table('TOOLS AND METHODS', ('Area', 'Documented use'), [
        ('Pricing and margin',
         'Bottom-up cost and capacity models, sensitivity on the two or three inputs that actually move the '
         'result, and a price that survives the first month of delivery.'),
        ('Energy and consumption',
         'Metering and SCADA data, load profiles, tariffs and efficiency measures with measured effect; over 40 % '
         'lower consumption documented on a live site.'),
        ('Risk and reporting',
         'Risk registers, monthly management reporting, deviation analysis and corrective actions with an owner '
         'and a date.'),
        ('Systems and integration',
         'Requirements, acceptance testing (FAT/SAT, IQ/OQ/PQ) and handover into operations — the point where a '
         'contract becomes something a system has to run.'),
        ('Programming and analysis',
         'Python (pandas-style data work, models and reports), Excel and Power Query; automation of recurring '
         'manual tasks.')])

    m.section('PROFESSIONAL EXPERIENCE')
    jobs = [
        ('Owner / Technical Director',
         'ELOHVAC ApS · Copenhagen · May 2023–present',
         '5 electricians and 3 apprentices · full P&L · electrical service and contracting',
         [('Pricing, contracts and margin under uncertainty',
           'Every quotation a position on cost and availability; pricing, negotiation, re-pricing on input costs, '
           'invoicing and payment follow-up with full P&L; own Python/Claude models for pricing, checklists and '
           'KPIs with over 40 % productivity gain.')]),
        ('Senior Commissioning Engineer / Project Manager, Electrical Systems',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · DKK 2–10 m per project · GMP/FDA/EMA',
         [('Portfolio, acceptance and handover',
           'Specification, factory and site acceptance testing and IQ/OQ/PQ for new production equipment; '
           'progress, cost and risk reported monthly to management; zero critical findings at audited handover.')]),
        ('Project and Workshop Manager',
         'Ventek-Air · Copenhagen · Jan 2022–Nov 2022',
         '14 employees · 11 parallel projects · DKK 2–10 m per assignment',
         [('Capacity, bottlenecks and short horizons',
           'Daily stand-ups, capacity and bottleneck analysis and priorities re-set the same day when a machine or '
           'a person dropped out; subcontractors and handover packages driven to date.')]),
        ('Maintenance and Operations Manager',
         'Lynetten (Biofos) · Copenhagen · Aug 2017–Jan 2022',
         'Critical 24/7 energy and process plant · pumps, blowers, transformers, switchgear and SCADA',
         [('Asset performance, energy and availability',
           'Availability and criticality on a plant that could not stop; energy metering, tariffs and efficiency '
           'measures with over 40 % lower consumption documented; maintenance, spares and external fitters '
           'coordinated around the clock; on-call rota planned and worked.')]),
        ('Electromechanic / Production Team Leader',
         'ARJ Engineering · Tehran · Dec 2003–Mar 2010',
         '12 mechanics and technicians · machine shop · industrial equipment',
         [('Technical delivery and team coordination',
           'Repair and fault-finding on industrial equipment with turning, milling, welding and assembly; shift '
           'planning, onboarding and follow-up on targets for 12 technicians.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('EDUCATION AND AUTHORISATION')
    m.edu('B.Tech, Technology Management and Mechanical Engineering',
          'Copenhagen School of Marine and Technical Engineering · 2017–2022 · GPA 7.6/12')
    m.edu('State-authorised Marine Engineer (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('Electrical and Mechanical Construction, Electrical Engineering',
          'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Refrigeration and Ventilation Technology · STCW', 'Mercantec 2021 · Danish Maritime Authority 2021')

    m.section('LANGUAGES, PRACTICALITIES AND REFERENCES')
    m.para('English: professional, spoken and written · Danish: native · Persian: native · Based in Måløv, 25 '
           'minutes from central Copenhagen, and open to Aalborg and Antwerp · Driving licence B and own car · '
           'Available by agreement · Reporting in writing, to a date, with the numbers attached · References on '
           'request.', after=70)

    m.models_table('WHAT THEY ASK FOR — WHAT I HAVE', ('Requirement', 'Evidence'), [
        ('Solid understanding of end-to-end asset business trade processes',
         'Contract lifecycle handled end to end in my own company — offer, terms, delivery, invoice, payment and '
         'the argument afterwards — and equipment taken from specification through acceptance into operations.'),
        ('Strong data handling and interpretation',
         'Python and Power Query models for pricing, capacity and reporting; metering and SCADA data reconciled '
         'and turned into decisions; data analytics where the number has to survive a challenge; over 40 % '
         'productivity gain from replacing manual work.'),
        ('Degree in economics, finance, physics, engineering or related',
         'B.Tech in technology management and mechanical engineering, plus state authorisation as a marine '
         'engineer (LV/MV/HV) and a technical degree in electrical and mechanical construction.'),
        ('Minimum five years in power trading, asset management or similar',
         'Five years as maintenance and operations manager on a 24/7 energy plant, and 20+ years of technical asset '
         'management, commissioning and commercial responsibility for technical portfolios.'),
        ('Experience in pricing renewable portfolios',
         'Pricing built on cost, capacity and risk: quotation and margin models in my own business, and energy '
         'consumption, tariffs and efficiency measures modelled on a live site with over 40 % documented effect.'),
        ('Programming in Python, VBA, R or similar',
         'Python is my working tool: pricing and capacity models, checklists, automated reports and dashboards, '
         'built and maintained by the person who uses them.'),
        ('Optimising agreements for renewable and flexible assets',
         'Asset performance and flexibility on a 24/7 plant: availability, criticality, downtime and load managed '
         'with measured results rather than assumptions.'),
        ('Managing portfolio risk across asset classes and markets',
         '37 capital projects with risk registers and monthly reporting; risk management in a P&L where price, '
         'cost, capacity and payment risk land in the same month.'),
        ('New contract structures, products and markets',
         'New service products and pricing models introduced in a small business; new markets entered with due '
         'diligence on legal, credit, settlement and operational requirements before the first contract.'),
        ('Relationship-building across the asset value chain',
         'Clear communication across sales, engineering, suppliers, authorities, fitters and customers, including '
         '25 specialists and multiple subcontractors coordinated to a fixed date.')])
    m.page_break()

    m.models_table('THE FIRST 90 DAYS — THE PORTFOLIO, THE PROCESSES AND THE MARKETS',
                   ('Period', 'What happens, and how it is measured'), [
        ('Weeks 1–2',
         'Read the contracts: the ten largest positions by value and risk, their pricing assumptions, tenor, '
         'indexation and the systems they are booked in. Sit with Origination and the desk and listen to where the '
         'handover between them is slow.'),
        ('Day 30',
         'One page per material position: asset assumption, price, volume, counterparty, tenor and the exposure '
         'that follows. Agreed definitions with Risk and Trading, so the same number means the same thing in every '
         'meeting.'),
        ('Day 60',
         'The two or three assumptions that carry the most value tested against actual asset performance; a '
         'proposal for one contract structure that prices flexibility better than today; a shortlist of markets '
         'worth entering, with the operational and settlement requirements attached.'),
        ('Day 90',
         'A pricing and review rhythm that Origination can use before a term sheet is signed; a working list of '
         'model and process improvements with an owner and a date; and a documented view of where the portfolio '
         'earns its margin and where it merely carries risk.')])

    m.section('A CONTRACT IS PRICED ON ASSUMPTIONS ABOUT THE ASSET')
    m.para('Every model of a wind farm, a solar park or a battery is a set of assumptions about physical behaviour: '
           'how often it is available, how it degrades, when it is curtailed and what the grid will accept. Those '
           'assumptions are usually somebody\'s best estimate from a year when everything went well. The commercial '
           'value of a portfolio manager is to know which assumptions actually carry the money — and to have a '
           'view on them that is better than the seller\'s.', after=80)

    m.section('EVERY CONTRACT IS A POSITION — MEASURE IT DAILY')
    m.para('Once a contract is signed it stops being a document and becomes an exposure: volume, price, imbalance, '
           'counterparty and tenor, moving every day with the market and with the asset. If that exposure is only '
           'visible when somebody builds a spreadsheet for a meeting, it is not managed. One sheet, one number, '
           'refreshed on a rhythm everyone knows, with the exceptions flagged rather than buried.', after=80)

    m.section('THE INTERFACE BETWEEN ORIGINATION AND TRADING IS WHERE THE MONEY LEAKS')
    m.para('A structure that looks elegant in a term sheet can be unbookable, unpriceable or unhedgeable by the '
           'desk that has to run it — and the cost of that gap never appears in the margin calculation. The fix is '
           'boring and effective: a collaborative process where the people who will operate the contract are in the '
           'room while it is designed, and the operational consequences are written into the term sheet before it '
           'is signed.', after=80)

    m.section('A NEW MARKET IS A PROJECT, NOT A DECISION')
    m.para('Entering a market for asset-backed trading is not a strategic wish; it is a list: legal entity, '
           'balancing responsibility, nomination and settlement, credit lines, IT integration, and the operational '
           'rules that differ from the last country. I have run portfolios of 37 projects and a business of my own '
           'on that discipline — an owner, a date and a cost per line — and it is the difference between a market '
           'entry and a market intention.', after=80)

    m.section('THE MODEL SHOULD BE BUILT BY THE PEOPLE WHO USE IT')
    m.para('A pricing model that lives with an analyst and is explained twice a year is a bottleneck. The version '
           'that works is the one the portfolio manager can change himself when a contract clause changes: '
           'transparent, versioned and reconcileable to the numbers in the systems. I build my own tools in Python '
           'and Power Query, and I have never accepted a report I could not reproduce.', after=80)

    m.section('I HAVE BEEN ON THE OTHER SIDE OF THE METER')
    m.para('For five years my job was to make a plant run, and to explain why it did not. That is where I learned '
           'what availability costs, how quickly a component failure turns into an unplanned position, and why the '
           'person who signs the contract should have stood in the plant room at three in the morning at least '
           'once. It is a perspective a trading desk rarely has in-house, and it is the one I would bring to a '
           'portfolio of assets I am now asked to price.', after=80)

    m.section('WHAT I WOULD BE JUDGED ON IN YEAR ONE')
    m.para('Three things: that the portfolio\'s assumptions are documented and tested rather than inherited; that '
           'Origination and Trading use the same numbers and the same definitions because a process made it '
           'easier; and that at least one structure or one market has moved from idea to booked business with my '
           'name on the working file. Everything else — the reporting, the meetings, the spreadsheets — exists to '
           'make those three happen.', after=80)

    return m.save(path, title='Senior Portfolio Manager — Centrica Energy',
                  subject='Asset-backed trading: pricing, portfolio risk and the operational reality behind the model',
                  keywords='senior portfolio manager, power markets, PPA, offtake, renewable, battery storage, '
                           'pricing, portfolio risk, origination, trading, Python, data, contracts')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Centrica_SeniorPortfolioManager.docx')))
