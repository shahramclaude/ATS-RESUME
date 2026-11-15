# -*- coding: utf-8 -*-
"""Oracle — Senior Project Manager, Utilities Network Management and DERMS.

English posting -> English deliverable. Job-first letter (page 1), CV (pages 2-3),
90-day plan (page 3), full requirement matrix (page 4).
Policy: master/README.md — job first, candidate only as evidence; full requirement coverage.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Senior Project Manager · Utilities technology delivery · Network operations and DER'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Copenhagen, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('7 November 2026')
    m.meta('Oracle · Oracle Utilities Consulting · Senior Project Manager, Utilities Network Management and DERMS')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Senior Project Manager, Utilities Network Management and DERMS',
           bold=True, color='1A1A1A')
    m.para('To the hiring team, Oracle Utilities Consulting', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('A Network Management System or a DERMS programme is not difficult because the software is complex. It is '
           'difficult because five workstreams — functional, integration, infrastructure, data and testing — meet in '
           'the same cutover weekend, in front of a control room that cannot stop operating, while the customer\'s '
           'sponsor needs to make a go-live decision he can defend. The project manager\'s job is to make that '
           'decision possible: dependencies visible, readiness evidenced, and the commercial position of the '
           'engagement secure. That is the delivery problem I am applying to solve.', after=80)

    m.para('**Three things decide whether a utility technology programme lands.** The first is the **dependency '
           'chain**: what must be true before integration testing can start, what the network operations team needs '
           'before it can accept a new control environment, and which decisions sit with the customer rather than '
           'with us. I plan from those dependencies backwards, not from a work breakdown forwards. The second is '
           '**go-live readiness as evidence rather than optimism**: cutover rehearsals, a fallback that has been '
           'tested, data and interfaces signed off, and a support transition that is agreed before the last defect '
           'list is closed. The third is **stakeholder arithmetic** — a sponsor, a control room, an IT organisation '
           'and a system integrator all carrying different risk, and a project manager who translates between them '
           'without losing the commercial position.', after=80)

    m.para('**My delivery record is in critical infrastructure, where the system and the operation are the same '
           'thing.** For five years I was operations and maintenance manager at **Lynetten, a wastewater utility '
           'plant under Biofos** — a municipally owned utility serving the Copenhagen area — running a critical '
           'plant in **24/7 operation** with **SRO/SCADA** control, pumping stations, transformers, switchgear and '
           'instrumentation. I owned the operational readiness of that estate: what the control system had to show, '
           'what had to alarm, what happened when a signal disappeared, and how the shift team kept the network '
           'running while systems were changed underneath them. Energy management and load optimisation across '
           'pumping delivered **over 40 % lower consumption**, measured and documented.', after=80)

    m.para('**I have delivered enterprise and OT system implementations across the full lifecycle.** At **Novo '
           'Nordisk** I led a portfolio of **37 parallel capital projects** worth DKK 2–10m each, with **25 '
           'specialists**, covering electrical systems, control systems and their integration into a validated '
           'production environment: requirements, design reviews, **FAT/SAT**, **IQ/OQ/PQ**, change control, and '
           '**monthly reporting of progress, cost and risk to management and the client organisation**. The '
           'portfolio closed with **zero critical findings** at handover — not because the risks were absent, but '
           'because they were found, owned and closed before they became deviations. That is the same discipline a '
           'NMS or DERMS implementation needs: interfaces and acceptance criteria defined early, tested against '
           'evidence, and traced to a requirement somebody signed.', after=80)

    m.para('**Commercially I have carried the number, not just reported it.** I run my own electrical contracting '
           'company with **full P&L**: pricing, contract terms, response commitments, invoicing, payment risk and '
           'the margin that survives year two. I know what an over-optimistic estimate costs a consultancy, because '
           'I have had to deliver against my own. In delivery terms that means scope changes are priced and agreed '
           'before they are worked, and recovery plans have owners, dates and a commercial consequence.', after=80)

    m.para('**Technically I can hold the conversation.** I am an **authorised marine and mechanical engineer '
           '(LV/MV/HV)** with a B.Tech in technology and operations management, and I have spent twenty years '
           'between electrical networks, control systems and data. I built my own tooling in **Python and Claude** '
           'for load and capacity calculations, checklists and reporting dashboards — over **40 % productivity gain** '
           '— which means I can sit with a solution architect, interrogate an interface specification, and tell when '
           'a plan is optimistic because somebody has not yet done the integration thinking.', after=80)

    m.para('**Across organisational boundaries is where I have done most of my work.** Leading 14 people at '
           'Ventek-Air across 11 concurrent construction projects, coordinating customer organisations, consultants, '
           'suppliers and authorities at Novo Nordisk, and managing a 24/7 shift organisation at Lynetten — in each '
           'case the delivery risk sat in the interfaces between organisations, not inside any one of them. I coach '
           'the project managers and specialists around me for the same reason: capability is what remains after the '
           'engagement ends.', after=80)

    m.para('I am based in Copenhagen, work in English professionally — including technical negotiation and '
           'regulatory reporting in an FDA/EMA environment — and am available at short notice. I would welcome the '
           'chance to discuss how Oracle Utilities Consulting is positioning NMS and DERMS delivery in the Nordics, '
           'and where the pressure points are in your current engagements.', after=70)
    m.meta('Yours sincerely', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('Technical project and programme manager with 20+ years in **critical utility infrastructure** — '
           '**authorised engineer (LV/MV/HV)** with a B.Tech in technology and operations management. Five years as '
           'operations and maintenance manager at **Lynetten (Biofos)**, a municipally owned utility running a '
           '**24/7 plant with SRO/SCADA control**, pumping stations, transformers and switchgear; **over 40 % lower '
           'energy consumption** through load optimisation. Two years leading a portfolio of **37 enterprise and OT '
           'system projects** with 25 specialists — requirements, FAT/SAT, **IQ/OQ/PQ**, change control and '
           '**monthly progress, cost and risk reporting** to management and client — closed with **zero critical '
           'findings**. Runs an electrical contracting company with **full P&L** (pricing, contracts, margin). '
           'Comfortable with architects and engineers on interface design, and with sponsors on the decisions they '
           'have to defend.', after=80)

    m.section('UTILITIES DELIVERY, SYSTEMS AND NETWORK OPERATIONS')
    for label, body in [
        ('Utility operations and network control',
         'Critical plant in 24/7 operation with SRO/SCADA: what the control environment must show, what alarms, how '
         'the shift organisation keeps service running while systems change, and how operational readiness is '
         'evidenced before acceptance.'),
        ('System implementation lifecycle',
         'Requirements and design review, FAT/SAT, IQ/OQ/PQ, change control and handover for electrical, control and '
         'integration scope across 37 projects — acceptance criteria traced to a signed requirement.'),
        ('Governance, risk and reporting',
         'Stage governance with named owners; RAID log reviewed on a fixed cadence; monthly reporting of progress, '
         'cost and risk to management and client; recovery plans with owners, dates and consequences.'),
        ('Commercial and contract management',
         'Full P&L in own company: pricing, contract terms, response commitments, invoicing and payment risk; scope '
         'changes priced and agreed before work starts.'),
        ('Data, interfaces and integration',
         'Interface specifications and data quality as delivery risks in their own right; measured baselines '
         '(energy, capacity, availability) used to prove a change worked rather than assert it.'),
        ('Teams across boundaries',
         '14 staff at Ventek-Air across 11 concurrent projects; 25 specialists in a matrix at Novo Nordisk; 12 '
         'technicians at ARJ; coaching project managers and specialists as a standing part of the role.')]:
        m.bullet(label, body, after=25)

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director',
         'ELOHVAC ApS · Copenhagen · May 2023–present',
         '5 electricians and 3 apprentices · full P&L · authorised engineer (el-autorisation) · LV/MV/HV electrical '
         'service and contracting',
         [('Commercial and delivery responsibility',
           'Carries the authorisation and the liability for work executed to standard; service contracts, pricing, '
           'response commitments, invoicing and payment risk; own Python and Claude tooling for load calculation, '
           'checklists and KPI reporting with over 40 % productivity gain.')]),
        ('Senior Commissioning Engineer / Project Manager, Electrical Systems',
         'Novo Nordisk A/S · Kalundborg/Bagsværd, Denmark · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · DKK 2–10m each · GMP/FDA/EMA validated environment',
         [('Portfolio delivery and client governance',
           'Requirements and design review, FAT/SAT and IQ/OQ/PQ for electrical and control systems; integration '
           'into a validated production environment with change control; monthly progress, cost and risk reporting '
           'to management and client organisation; zero critical findings at handover.')]),
        ('Project and Workshop Manager',
         'Ventek-Air · Copenhagen · Jan 2022–Nov 2022',
         '14 employees · 11 concurrent construction projects · DKK 2–10m per project',
         [('Capacity, dependencies and recovery',
           'Daily board meeting, capacity and bottleneck analysis, same-day re-prioritision when a machine or a '
           'person dropped out; standardised work packages and handover documentation held to date.')]),
        ('Operations and Maintenance Manager',
         'Lynetten under Biofos · Copenhagen · Aug 2017–Jan 2022',
         'Critical wastewater utility plant in 24/7 operation · SRO/SCADA · pumping stations, blowers, ventilation, '
         'transformers, switchgear',
         [('Operational readiness and control systems',
           'Criticality assessment, maintenance and replacement plans, spares and external contractors across a '
           '24/7 estate; on-call and emergency response planned and exercised; SCADA alarms prioritised by service '
           'consequence; energy and load optimisation with over 40 % lower consumption.')]),
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
    m.para('English: professional, written and spoken, including technical negotiation and regulatory reporting · '
           'Danish: native · Persian: native · Based in Copenhagen, Denmark; mobile across the Nordics and '
           'internationally · Driving licence B and own car · Available at short notice · References on request.',
           after=70)

    m.models_table('THE FIRST 90 DAYS — DEPENDENCIES, READINESS AND GO-LIVE',
                   ('Phase', 'What happens, and how it is measured'), [
        ('Week 1–2',
         'Meet the customer sponsor, the control-room and operations leads, Oracle solution architects and the '
         'integration partner; read the statement of work, the plan, the RAID log and the last two steering packs; '
         'walk the scope that is in trouble, not the scope that is green.'),
        ('Day 30',
         'Dependency map agreed across functional, integration, infrastructure, data and test workstreams, with a '
         'named owner per interface and a decision log for everything that sits with the customer; recovery plan for '
         'the two highest-risk items agreed with the sponsor.'),
        ('Day 60',
         'Go-live readiness defined as evidence — cutover rehearsal, tested fallback, interface sign-off, data '
         'quality thresholds and an agreed support transition; reporting pack reduced to what the steering group '
         'actually decides on; commercial position on changes restated and agreed.'),
        ('Day 90',
         'Delivery on a plan the team believes in, with variance visible early rather than reported late; lessons '
         'captured from the last engagement and fed into the next estimate; and the project managers around me '
         'coached on the two things that decide utility go-lives — interface discipline and readiness evidence.')])

    m.section('READINESS IS EVIDENCE, NOT OPTIMISM')
    m.para('Every go-live I have been part of has been decided on evidence: a cutover that has been rehearsed, a '
           'fallback that has been tested with the operations team in the room, interfaces signed off against '
           'specification, data quality measured against a threshold agreed in advance, and support ownership '
           'settled before the last defect is closed. Where a programme slips, it is usually because one of those '
           'five was assumed rather than proven. Delivery planning that names the evidence, and risk management that '
           'treats an unproven assumption as a risk, is what separates a plan from a hope.', after=80)

    m.section('UTILITY CLIENTS BUY CERTAINTY, NOT ENTHUSIASM')
    m.para('A control-room manager does not want a roadmap. He wants to know what changes on Monday, what stays the '
           'same, who he calls at 03:00 if it does not work, and whether the network can be restored the old way if '
           'the new system is not there. A sponsor wants to know which decision is his, what it costs, and who carries '
           'the accountability if it does not work. Most of the value a project manager adds is answering those '
           'questions before they are asked — in writing, with a date.', after=80)

    m.section('TECHNICAL DEPTH IS WHAT MAKES A PLAN CREDIBLE')
    m.para('Plans become fiction where interfaces, data and non-functional requirements meet. I have spent twenty '
           'years on the other side of that boundary — commissioning control systems with architects, engineers and '
           'functional specialists, integrating them into a validated environment, and living with the result in '
           '24/7 operation. I do not need to design the '
           'solution, but I need to be able to ask the question that exposes an interface nobody has specified, and '
           'to recognise the point where "we will handle it in testing" is really "we have not decided".', after=80)

    m.section('ESCALATION IS A PROCESS, NOT A PERSONALITY')
    m.para('An escalation works when it arrives early, with the facts, the options and a recommended course of '
           'action — and when the person receiving it can decide. I have run escalation both ways: as the supplier '
           'explaining a slipping date to a client organisation, and as the client holding a contractor to a '
           'commitment. It taught me to keep the relationship and the problem separate, and to put the '
           'recommendation in writing before the meeting rather than after it. Mentoring is how that skill '
           'spreads: the escalation that never reaches me is the one that was handled well.', after=80)

    m.page_break()
    m.models_table('WHAT THE ROLE REQUIRES — WHAT I HAVE DELIVERED', ('Requirement in the posting', 'Evidence'),
                   widths=(3200, 7146), rows=[
        ('Complex utilities projects and programmes',
         'Five years of 24/7 utility operations; 37 capital projects with requirements, budgets, risk and monthly '
         'reporting; 11 concurrent projects.'),
        ('NMS or equivalent network management delivery',
         'SRO/SCADA control across a 24/7 utility network: alarms, visibility, restoration decisions, and changing '
         'that environment without interrupting service.'),
        ('Oracle Utilities or comparable platforms',
         'SAP for asset and economy data, SRO/SCADA for network control, own Python tooling for load and capacity — '
         'requirement, interface and acceptance work that carries across platforms.'),
        ('DERMS project delivery',
         'Distributed assets and demand: load and energy optimisation across a distributed pumping estate with over '
         '40 % measured reduction; dispatch under constraint.'),
        ('Enterprise implementations, full lifecycle',
         'Requirements, design review, FAT/SAT, IQ/OQ/PQ, change control and handover on electrical, control and '
         'integration scope — zero critical findings.'),
        ('Readiness: go-live and support transition',
         'Readiness as a gate: cutover and fallback tested, interfaces and data signed off, shift team trained, '
         'support transition agreed before closure.'),
        ('Functional, integration and test workstreams',
         'Electrical, control, integration and validation workstreams on 37 projects, interfaces and acceptance '
         'criteria defined before execution.'),
        ('Governance and reporting across partners',
         'Stage governance with named owners, RAID log on fixed cadence, monthly progress, cost and risk reporting '
         'a steering group can decide on.'),
        ('Risk, resource and commercial management',
         'Full P&L in own company: pricing, contract terms, invoicing and payment risk; resource planning across 25 '
         'specialists; changes priced before work starts.'),
        ('Early warning and practical recovery',
         'Same-day re-prioritisation when capacity dropped; recovery plans with owners, dates and a commercial '
         'consequence; deviations closed before handover.'),
        ('Multidisciplinary teams across boundaries',
         '25 specialists in a Novo Nordisk matrix; 14 staff at Ventek-Air; customer, supplier and authority '
         'interfaces run as delivery risks.'),
        ('Senior stakeholders and escalations',
         'Monthly escalation to management and client; difficult conversations held with owners and dates rather '
         'than optimism; auditors faced with evidence.'),
        ('Consulting, bids and coaching capability',
         'Customer-facing scoping, estimation and commercial terms in own company; technical input to proposals; '
         'managers and specialists coached in four organisations.'),
        ('Billing, customer care and metering',
         'Requirement, integration and acceptance discipline on enterprise systems consuming asset, economy and '
         'customer data; SAP daily; the same method carries to CC&B, C2M, Customer Cloud Service and Meter Data '
         'Management.'),
        ('Technical credibility and distribution',
         'Authorised engineer (LV/MV/HV), B.Tech technology and operations management; transformers, switchgear, '
         'protection and pumping in operation and maintenance.'),
        ('Clear written and spoken English',
         'Twenty years of professional English: technical negotiation, client and regulatory reporting in an '
         'FDA/EMA environment, written decision documents for management.')])

    m.section('DISTRIBUTED ENERGY CHANGES THE OPERATING MODEL, NOT JUST THE SOFTWARE')
    m.para('DERMS — the management of distributed energy resources — is not an integration project with a nicer name. '
           'It changes who can act on the electricity distribution network and when: visibility of assets the '
           'operator does not own, constraints that appear at the edge, flexibility that has to be trusted before '
           'it is dispatched. The delivery questions that follow are concrete — who is '
           'allowed to curtail, what evidence proves the asset responded, what happens when the signal fails, and '
           'how the control room keeps authority while the model changes. Those are the questions I would put on the '
           'table at design stage rather than at go-live.', after=80)

    m.section('LESSONS LEARNED ONLY COUNT IF THEY CHANGE THE NEXT ESTIMATE')
    m.para('Every engagement produces lessons; most of them die in a slide at the close-out meeting. I have built '
           'the habit the other way round: the same three things that went wrong get written into the checklist, the '
           'estimate template, the technical project management and programme management approach, and the delivery '
           'plan of the next enterprise software upgrade, and the effect is measured on the next '
           'engagement rather than asserted at the end of this one. That is also how capability is built in a '
           'consulting team — not by a training course, but by making the next plan better than the last.', after=80)

    return m.save(path, title='Senior Project Manager, Utilities Network Management and DERMS — Oracle',
                  subject='Utility technology programme delivery, NMS and DERMS, governance and go-live readiness',
                  keywords='senior project manager, utilities, network management system, derms, oracle utilities, '
                           'electricity distribution, programme delivery, governance, go-live readiness, scada, '
                           'stakeholder management, consulting')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Oracle_SeniorProjectManagerNMS_DERMS.docx')))
