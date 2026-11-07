# -*- coding: utf-8 -*-
"""ABB — Project Manager, Automation Service Projects (Ballerup / Middelfart / Esbjerg).

English posting -> English deliverable. Job-first letter (page 1), CV (pages 2-3),
90-day plan and working sections (page 3), full requirement matrix (page 4).
Policy: master/README.md — job first, candidate only as evidence; full requirement coverage.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Project Manager · Automation service, retrofit and upgrade projects'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Copenhagen, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('7 November 2026')
    m.meta('ABB · Service, Project Management · Req. ID JR00048825 · Ballerup / Middelfart / Esbjerg')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Project Manager, Automation Service Projects', bold=True, color='1A1A1A')
    m.para('To Nicolai Heilskov, Head of Project Management in Service', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('A retrofit on a plant that is still running is a different discipline from a greenfield project. The '
           'customer is not buying new equipment — he is buying the shortest possible interruption to production, a '
           'control system that behaves exactly as the operators expect afterwards, and a supplier who knows which '
           'work has to happen inside the shutdown window and which can be done before it. Service projects are won '
           'on that sequencing, and they are lost on the commercial detail: a change nobody priced, a claim nobody '
           'documented, an aftermarket opportunity nobody followed up. That is the job I am applying for.', after=80)

    m.para('**Tender through handover is the part of the lifecycle I know best.** I have taken scopes from a '
           'requirement document to a priced, planned and resourced project, executed it in a live production '
           'environment, and closed it with documented acceptance — over **37 parallel projects** at **Novo '
           'Nordisk**, with **FAT/SAT and IQ/OQ/PQ** as the gates, change control between them, and **monthly '
           'reporting of progress, cost and risk** to management and the client organisation. The portfolio closed '
           'with **zero critical findings** at handover. That result came from doing the tender and planning work '
           'properly: interfaces specified, assumptions written down, acceptance criteria agreed before anyone '
           'started welding.', after=80)

    m.para('**Automation and OT are my technical home.** For five years I was operations and maintenance manager at '
           '**Lynetten, a utility plant under Biofos** in the Copenhagen area, running a critical site in **24/7 '
           'operation** with **SRO/SCADA** control, pumping stations, blowers, ventilation, transformers and '
           'switchgear. I was the customer side of retrofits before I was the supplier side: deciding what could be '
           'replaced, in which shutdown window, with which fallback, and what the operators had to be trained in '
           'before the change went live. Energy management and load optimisation across the plant delivered **over '
           '40 % lower consumption**, measured. When I say I can hold a technical conversation with an engineering '
           'team about a control system upgrade, it is because I have been the one who had to accept the result.',
           after=80)

    m.para('**Commercial control is where I add margin rather than just report on it.** I run my own electrical '
           'contracting company with **full P&L** — pricing, contract terms, response commitments, invoicing and '
           'payment risk. I have negotiated change orders on work that was already in progress, taken the '
           'conversation when a customer wanted more for the same price, and priced the risk of a response-time '
           'commitment before signing it. Changes get priced and agreed before they are executed; claims get '
           'documented while the evidence is still on site, not reconstructed three months later.', after=80)

    m.para('**Service is a portfolio, not a series of one-off jobs.** In my own company the recurring revenue comes '
           'from service agreements and the follow-on work that a well-run service visit uncovers — the same logic as '
           'ABB\'s aftermarket: a retrofit is the entry point, and the value is in the upgrades, the spares and the '
           'service contract that follow. I have built that pipeline myself, and I know which of my customers were '
           'worth a follow-up call and which were not.', after=80)

    m.para('**Teams and stakeholders across sites.** I led **14 people at Ventek-Air** across **11 concurrent '
           'projects**, with daily prioritisation when a machine or a person dropped out, and I have coordinated '
           'customer organisations, consultants, suppliers and authorities at Novo Nordisk. Remote management is '
           'ordinary in that environment: the project lives in the plan, the reporting and the escalation rhythm, not '
           'in who is in the same building. I also work in Danish and English daily, with **SAP ERP, CMMS, Power BI, '
           'Excel/Power Query and Python** as the toolset behind plans, cost control and forecasting.', after=80)

    m.para('**On compliance I am comfortable being audited.** Quality, HSE and information requirements are not '
           'paperwork that follows the project — they are constraints the plan has to respect. I have worked in a '
           'GMP/FDA/EMA validated environment where documentation was the evidence that work had been done, and I '
           'have carried the HSE responsibility on a 24/7 industrial site: permits, safe systems of work, near-miss '
           'follow-up and the discipline of stopping a job that is not safe. In an automation service context I '
           'treat cybersecurity requirements the same way — access, segmentation and change control agreed before '
           'the engineer connects.', after=80)

    m.para('I am based in Copenhagen, with **Ballerup** as my natural base and willingness to work from Middelfart '
           'or Esbjerg when the projects are there; I have a car and drive across Denmark as a matter of course, and '
           'I am available at short notice. I would welcome the chance to discuss which retrofit and service '
           'portfolios ABB is running in Denmark right now, and where delivery pressure is highest.',
           after=70)
    m.meta('Yours sincerely', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('Technical project manager with 20+ years in **automation, control systems and critical industrial '
           'plant** — **authorised engineer (LV/MV/HV)** with a B.Tech in technology and operations management. Led **37 '
           'capital projects** with 25 specialists at **Novo Nordisk**: tender and requirements, planning and '
           'resourcing, **FAT/SAT and IQ/OQ/PQ**, change control, commissioning and handover, with **monthly '
           'progress, cost and risk reporting** and **zero critical findings** at completion. Five years as '
           'operations and maintenance manager at **Lynetten (Biofos)** on a **24/7 plant with SRO/SCADA**, '
           'pumping stations, transformers and switchgear — **over 40 % lower energy consumption** through load '
           'optimisation. Runs an electrical contracting business with **full P&L**: tenders, contracts, change '
           'orders, claims, service agreements and aftermarket. Works in Danish and English; **SAP ERP, CMMS, Power '
           'BI, Excel/Power Query, Python**.', after=80)

    m.section('AUTOMATION, RETROFIT AND SERVICE DELIVERY')
    for label, body in [
        ('Retrofit and upgrade in live plant',
         'Replacement and upgrade of pumps, blowers, ventilation, transformers and switchgear in 24/7 operation: '
         'shutdown windows, fallback, operator training and acceptance — sequenced so production kept running.'),
        ('Tender to handover',
         'Scope and requirement documents converted into priced, planned and resourced projects; FAT/SAT and '
         'IQ/OQ/PQ as gates; change control between them; handover documentation signed on both sides.'),
        ('OT, control systems and data',
         'SRO/SCADA in daily operation: alarms, regulation, fault finding and version changes; PLC-adjacent '
         'electrical control, instrumentation and the data path from plant to reporting.'),
        ('Financials and forecasting',
         'Project budgets, cost control and monthly forecast versus actual; earned value and commitment tracking; '
         'dashboards and cost models built in Power BI, Excel/Power Query and Python.'),
        ('Commercial and contractual',
         'Full P&L in own company: tender pricing, contract terms, response commitments, change orders, claims and '
         'payment risk — with the documentation trail kept while the work is on site.'),
        ('Customer and aftermarket',
         'Service agreements, recurring visits and follow-on work identified from the service visit; upsell built on '
         'the customer\'s actual constraint rather than a product catalogue.')]:
        m.bullet(label, body, after=25)

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director',
         'ELOHVAC ApS · Copenhagen · May 2023–present',
         '5 electricians and 3 apprentices · full P&L · authorised engineer · LV/MV/HV service and retrofit work',
         [('Service projects, contracts and margin',
           'Tender pricing, contract terms, change orders and payment risk on electrical service and retrofit work; '
           'service agreements and follow-on upgrades; own Python and Claude tooling for costing, checklists and KPI '
           'reporting with over 40 % productivity gain.')]),
        ('Senior Commissioning Engineer / Project Manager, Electrical Systems',
         'Novo Nordisk A/S · Kalundborg/Bagsværd, Denmark · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · DKK 2–10m each · GMP/FDA/EMA validated environment',
         [('Tender to handover in a validated plant',
           'Requirements and design review, FAT/SAT, IQ/OQ/PQ, change control and commissioning for electrical and '
           'control systems; monthly progress, cost and risk reporting to management and client; zero critical '
           'findings at handover.')]),
        ('Project and Workshop Manager',
         'Ventek-Air · Copenhagen · Jan 2022–Nov 2022',
         '14 employees · 11 concurrent projects · DKK 2–10m per project',
         [('Multi-site delivery and recovery',
           'Daily board meeting, capacity and bottleneck analysis, same-day re-prioritisation; standardised work '
           'packages and handover documentation; teams and subcontractors managed across sites.')]),
        ('Operations and Maintenance Manager',
         'Lynetten under Biofos · Copenhagen · Aug 2017–Jan 2022',
         'Critical utility plant in 24/7 operation · SRO/SCADA · pumping, ventilation, transformers, switchgear',
         [('Owner of the plant the retrofits happened in',
           'Criticality assessment, replacement plans, spares and contractors; shutdown planning and fallback; HSE '
           'responsibility including permits, safe systems of work and near-miss follow-up; energy and load '
           'optimisation with over 40 % lower consumption.')]),
        ('Electromechanical Technician / Production Team Leader',
         'ARJ Engineering · Tehran · Dec 2003–Mar 2010',
         '12 mechanics and technicians · machine workshop · industrial equipment',
         [('Technical delivery and team leadership',
           'Fault finding and root-cause analysis on industrial equipment; shift planning, training and performance '
           'follow-up for 12 technicians.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('EDUCATION AND AUTHORISATION')
    m.edu('B.Tech, Technology and Operations Management; Mechanical Engineering',
          'Copenhagen School of Marine and Mechanical Engineering · 2017–2022 · GPA 7.6/12')
    m.edu('Authorised Engineer (el-autorisation), LV/MV/HV', 'Danish Safety Technology Authority · May 2023')
    m.edu('Electrical and Mechanical Design, Electrical Engineering',
          'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Refrigeration and Ventilation Technology · STCW', 'Mercantec 2021 · Danish Maritime Authority 2021')

    m.section('LANGUAGES, PRACTICALITIES AND REFERENCES')
    m.para('Danish: native · English: professional, written and spoken, including technical and commercial '
           'negotiation · Persian: native · Based in Copenhagen; Ballerup, Middelfart and Esbjerg all workable, '
           'with travel across Denmark and occasional Nordic travel · Driving licence B and own car · Home working '
           'days as agreed · Available at short notice · References on request.', after=70)

    m.models_table('THE FIRST 90 DAYS — PROJECTS, MARGIN AND AFTERMARKET',
                   ('Phase', 'What happens, and how it is measured'), [
        ('Week 1–2',
         'Meet the project management colleagues, the engineering and service teams and the customers behind the '
         'three most active retrofits; read the contracts, the change logs and the last two project reviews; find '
         'out where the delivery pressure actually sits.'),
        ('Day 30',
         'Each live project has a plan built from the shutdown window backwards, a forecast against budget and a '
         'named owner per interface; the open change orders are priced and either accepted by the customer or '
         'closed; escalation rhythm agreed with the Head of Project Management.'),
        ('Day 60',
         'Cost control moved from monthly surprise to weekly visibility — commitments, hours and forecast at '
         'completion visible on a dashboard rather than reconstructed at month end; aftermarket follow-up agreed for '
         'every completed service visit.'),
        ('Day 90',
         'Projects delivering to plan with variance visible early; claims documented while the evidence is fresh; a '
         'short list of upgrade opportunities generated from service findings and handed to sales with a price and a '
         'technical rationale.')])

    m.section('THE SHUTDOWN WINDOW IS THE WHOLE PROJECT')
    m.para('In a service retrofit, the plan is not the list of tasks — it is the sequence that fits inside the window '
           'the plant can be down. That means deciding weeks in advance what is pre-assembled, what is tested '
           'offline, what can be commissioned in parallel and what has to be done live; agreeing the fallback with '
           'the operations team; and having the documentation ready so acceptance does not consume the remaining '
           'hours. I have planned and worked those windows from both sides, and the discipline is the same: nothing '
           'on the critical path that has not been proven somewhere else first.', after=80)

    m.section('CHANGE ORDERS ARE WON IN THE FIRST WEEK, NOT THE LAST')
    m.para('Most commercial disputes in retrofit work are not arguments about money; they are arguments about '
           'evidence. The scope change was visible on site for three weeks before anyone wrote it down, and by the '
           'time it became a claim, the photographs, the site instruction and the hours were gone. I run projects so '
           'that the change is priced and accepted while the crew is still standing next to it — which keeps the '
           'relationship intact and the margin where it belongs.', after=80)

    m.section('SERVICE IS WHERE THE NEXT PROJECT COMES FROM')
    m.para('A service visit is the cheapest sales meeting a company will ever have, if anyone captures what it '
           'revealed: an obsolete drive, a spares shortage, a control system two versions behind. I have built that '
           'loop in my own business, and it is the same loop ABB runs at scale — the difference is discipline in '
           'recording it and following up while the finding is still fresh.', after=80)

    m.section('I HAVE BEEN THE CUSTOMER IN A RETROFIT')
    m.para('At Lynetten I was the operations manager who had to accept a supplier\'s retrofit — which means I know '
           'what a customer actually wants from the project manager opposite him: no surprises in the shutdown '
           'window, an honest answer about what will not be finished, a fallback that works if the new system does '
           'not, and a handover pack the night shift can use at 03:00 without calling anyone. That perspective '
           'changes how I write a plan and how I price a risk. A supplier who says "we will manage" gets no second '
           'shutdown window.', after=80)

    m.page_break()
    m.models_table('WHAT THE ROLE REQUIRES — WHAT I HAVE DELIVERED', ('Requirement in the posting', 'Evidence'),
                   widths=(3200, 7146), rows=[
        ('Service, retrofit and upgrade projects from tender to final delivery',
         'Electrical and control retrofits in 24/7 plant: tender pricing, shutdown sequencing, fallback, acceptance; '
         '37 projects from requirement to signed handover at Novo Nordisk.'),
        ('Project planning, scheduling, resource plans and execution',
         'Plans built from dependencies and shutdown windows; 11 concurrent projects resourced and re-prioritised '
         'daily at Ventek-Air; 25 specialists scheduled across 37 projects.'),
        ('Customer relationships and acting as trusted advisor',
         'Primary contact for clients in own company from quote to final invoice; bygherre, consultants and '
         'authorities coordinated in a validated plant environment.'),
        ('Commercial risks, project changes, claims and recovery actions',
         'Change orders priced before execution, claims documented while evidence is on site; recovery plans with '
         'owners, dates and a commercial consequence.'),
        ('Project financials: forecasting, cost control and value optimization',
         'Budgets, monthly forecast versus actual and commitment tracking on 37 projects; full P&L in own company; '
         'cost models and dashboards in Power BI, Excel/Power Query and Python.'),
        ('Aftermarket opportunities and upselling',
         'Service agreements, recurring visits and follow-on upgrades built into the revenue of own company; upsell '
         'driven by the customer\'s operating constraint.'),
        ('Contract management and change management',
         'Contract terms, response commitments and payment risk negotiated and held; change control applied between '
         'FAT/SAT and IQ/OQ/PQ gates and documented at handover.'),
        ('Compliance with quality, cybersecurity and HSE requirements',
         'GMP/FDA/EMA validated environment where documentation proved the work; HSE responsibility on a 24/7 site '
         '— permits, safe systems of work, near-miss follow-up; access and change control agreed before connection.'),
        ('4–7 years of project management in technical, industrial or automation environments',
         'Project management since 2010 and formally from 2017: operations and maintenance leadership, 37 capital '
         'projects, 11 concurrent construction projects, and own company project portfolio since 2023.'),
        ('Leading project teams and driving delivery to milestones, including remote management',
         '25 specialists and 14 staff led across sites; delivery driven on milestone, reporting pack and escalation '
         'rhythm rather than proximity; 12 technicians led at ARJ.'),
        ('Customers and cross-functional stakeholders in complex project environments',
         'Client organisations, consultants, suppliers, authorities and internal engineering functions aligned '
         'through 37 projects and a 24/7 operating organisation.'),
        ('Project planning, budgeting and execution methodologies',
         'Stage-gate delivery with acceptance gates (FAT/SAT, IQ/OQ/PQ), RAID and monthly reporting; budgeting and '
         'forecasting in SAP ERP and Excel/Power Query.'),
        ('Tender phase through commissioning and handover',
         'Requirement documents and tenders turned into priced projects, then executed and commissioned — closure '
         'with documented acceptance and zero critical findings.'),
        ('Automation, OT or industrial control systems, preferably energy, process, power or offshore',
         'SRO/SCADA, instrumentation and electrical control on a critical utility plant in 24/7 operation; energy '
         'and load optimisation with over 40 % measured reduction.'),
        ('Excellent communication in Danish and English; Azure DevOps, Microsoft Project or similar',
         'Danish native and English professional, including technical and commercial negotiation; planning data, '
         'cost control and dashboards in SAP ERP, CMMS, Power BI, Excel/Power Query and Python.'),
        ('PMP, PRINCE2, IPMA or comparable certification considered an advantage',
         'Stage-gate governance practised to that standard: defined gates, acceptance criteria, change control, '
         'RAID, monthly forecast and handover evidence across 37 projects.')])

    m.section('THE PLAN HAS TO SURVIVE CONTACT WITH THE PLANT')
    m.para('Every retrofit plan meets reality on day one: a cable route nobody surveyed, an obsolete card with a '
           'delivery time in weeks, an operator who was not in the design review and does not recognise the screen. '
           'The project manager cannot prevent that; he can make sure it is discovered early, costed quickly and '
           'decided by someone with the authority to decide. That is why I run short cycles with the engineering team '
           'and the customer in the same room — and why I write the decision down on the day it is taken.', after=80)

    m.section('CYBERSECURITY IS A DELIVERY CONSTRAINT, NOT A CHECKBOX')
    m.para('An automation retrofit almost always touches a network, and the fastest way to lose a go-live is to '
           'discover at commissioning that the segmentation, the accounts or the remote access were never agreed. I '
           'treat those requirements as part of the plan from the tender: what has to be in place before the engineer '
           'connects, who approves it on the customer side, and what the fallback is when it is delayed. It is the '
           'same discipline as a permit to work — unglamorous, and the reason the job finishes on time.', after=80)

    return m.save(path, title='Project Manager, Automation Service Projects — ABB',
                  subject='Automation service, retrofit and upgrade project delivery',
                  keywords='project manager, automation, ot, retrofit, upgrade, service projects, tender, '
                           'commissioning, handover, commercial risk, claims, forecasting, aftermarket, hse, '
                           'danish, english')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_ABB_ProjectManagerAutomationService.docx')))
