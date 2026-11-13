# -*- coding: utf-8 -*-
"""Vattenfall BA Wind — OT O&M Manager, Infrastructure (REF13257I), Kolding, Denmark.

English posting -> English document. Form (master/FORMKATALOG.md): opening **O**
(the absence: a wind farm you cannot see is a wind farm you cannot run — the
service is only noticed when it is gone), structure **The Runbook and the
Roadmap** (five themes, each with today's runbook and the road ahead), register
**The Data Path** (concentrator, telemetry, edge, backhaul, historian, failover,
backup, restore). Culture file: jd/Vattenfall_OTOandM_kultur.txt.
User decisions 13.11.2026: build it although the stated deadline has passed;
Kolding, and he relocates.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'OT O&M Manager, Infrastructure · service ownership across sites'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('13 November 2026')
    m.meta('Vattenfall · Business Area Wind · OT Infrastructure · Kolding · REF13257I')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: OT O&M Manager, Infrastructure', bold=True, color='1A1A1A')

    def lp(text, after=60):
        return m.para(text, after=after, line=236)

    # ---------------------------------------------------------------- page 1
    lp('**A wind farm you cannot see is a wind farm you cannot run.** When a data concentrator stops '
       'forwarding at three in the morning, nobody in the control room asks which server it was; they '
       'ask why forty turbines went quiet on the screen — and how long it will take before someone can '
       'act on them again. That is the product this role owns: not servers, but the operator\'s ability '
       'to see, decide and act — what you call **"secure connectivity, monitoring, control and '
       'operational data exchange"**. It is also why the service is invisible on the days it works, and '
       'unforgiving on the day it does not.', after=56)

    lp('**"You do not need to be the technical expert in every infrastructure domain"**, you write. I '
       'would go one step further: the owner of this service should be able to read the architecture, '
       'challenge a recommendation and still let the specialist make the call. I have run '
       'operations that could not stop — a wastewater plant in 24/7 duty for five years, with SCADA, '
       'PLCs, HV switchgear and on-call rota — and I have been the one called at 03:00. What I have not '
       'done is own an OT estate for a wind fleet. That is the gap, and it is a gap of scale and '
       'domain, not of method.', after=56)

    lp('**Two documents, five themes.** A service owner is judged on two documents: the runbook — what '
       'happens tonight — and the roadmap — what stops us having the same night in two years. I would '
       'hold both for each of the five themes below.', after=44)

    lp('**Availability and recovery.** *Runbook:* a written escalation path, a named second line and a '
       'tested restore, not a backup that exists. *Roadmap:* redundancy designed into the **"Edge-to-'
       'Wide-Area connectivity solutions"** so a single link is not a single point of failure. I have '
       'run a plant where an unplanned stop cost production by the hour; the restore procedure was '
       'rehearsed, not hoped for.', after=40)

    lp('**Incidents and recurring problems.** *Runbook:* one incident owner, one timeline, one customer '
       'message per hour while it burns. *Roadmap:* **"incidents, recurring problems and improvement '
       'needs"** closed as a class, not one by one — the third identical alarm in a month is a design '
       'conversation with Engineering, not a fourth ticket — **"driven through to sustainable '
       'resolution"**. That discipline is what took 37 capital projects to handover with zero critical '
       'deviations.', after=40)

    lp('**Lifecycle and the estate.** *Runbook:* patching windows agreed with Operations, and an '
       'inventory that is true — every concentrator, every gateway, every version. *Roadmap:* a '
       'replacement plan with years and money attached, so the end of support is a decision taken in '
       'advance rather than an incident taken on the night.', after=40)

    lp('**Cost and governance.** *Runbook:* a monthly page — availability, incidents by cause, backlog, '
       'run cost. *Roadmap:* the budget conversation held with numbers that Operations recognises, so '
       'growth in the fleet is matched by growth in the service. Governance is not a meeting; it is the '
       'decision log that shows who decided what, and when.', after=40)

    lp('**People and interfaces.** *Runbook:* a rota people can live with, and specialists who are '
       'allowed to be the expert. *Roadmap:* a competence plan across OT, IT, Cybersecurity, '
       'Procurement, projects and suppliers, so the service does not depend on one person\'s memory. I '
       'have led 25 specialists, 14 fitters, 12 technicians and eight employees — and learned that '
       '**"empowering technical specialists"** is a discipline, not a phrase in a values deck.', after=56)

    lp('**What I would need to learn, and how fast.** The wind domain: how a wind farm\'s OT estate is '
       'segmented, what the cyber baseline requires, and which dependencies sit between site, control '
       'centre and enterprise. My starting point is real — SCADA and PLC operations, HV and LV systems, '
       'networked control in a plant that could not stop, and a maskinmester degree behind it — but I '
       'would spend the first months on site and in the architecture reviews rather than in the '
       'slideware.', after=56)

    lp('**Why Vattenfall, in your own words.** Yours is **"a leading European utility"** that has been '
       '**"electrifying industries, powering homes and transforming life through innovation"** for '
       '**"more than 100 years"**, with **"fossil freedom"** as the strategy rather than a slogan. BA '
       'Wind carries **"24GW of capacity"** and calls itself **"one of the most exciting pipelines in '
       'the industry"**; the OT team is **"the operational backbone of Business Area Wind"**, and you '
       'are explicit that **"leadership, Accountability and Proactivity"** weigh as much as technical '
       'depth. That is the job description I recognise: **"the structure and momentum needed"** to '
       '**"keep the service fit for future business requirements"** — in a team of **"1,700+ colleagues '
       'from 50+ nationalities"** with **"an open, supportive culture"** and **"a healthy work-life '
       'balance"**.', after=56)

    lp('**Practical.** I live in Måløv today and I am ready to relocate, so my working week is in '
       'Kolding. English is my working language with suppliers and international colleagues, Danish is '
       'my first language, and Persian is my mother tongue. Available after agreement and happy to go '
       'through the screening your critical-infrastructure role requires; references on request.', after=24)

    m.meta('Kind regards', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('**Operations and service leader with control systems, 24/7 duty and full P&L behind him** — '
           'authorised maskinmester (LV/MV/HV), B.Tech in technology management and mechanical '
           'engineering. Five years as operations and maintenance manager of a plant in 24/7 duty with '
           'SCADA, PLCs and HV switchgear; **37 capital projects** commissioned and handed over with '
           'FAT/SAT and IQ/OQ/PQ; 25 specialists, 14 fitters and eight employees led. Works in service '
           'performance, incident and problem follow-up, lifecycle and cost — with the numbers on one '
           'page.', after=70)

    m.section('THE DATA PATH — HOW I READ AN OT SERVICE')
    for label, body in [
        ('The concentrator',
         'Where the site becomes data: if it stops, the operator is blind while every turbine turns. '
         'That hop is what the service is really measured on.'),
        ('The telemetry',
         'Which signals matter, how often they arrive, and what happens when they arrive late — '
         '**monitoring** that nobody reads is a licence, not a control.'),
        ('The edge link',
         'Site to wide area, and the failover behind it: one link with no alternative is a single point '
         'of failure with a business case attached.'),
        ('The historian',
         'Where the evidence lives after an incident; without a reliable **backup** and a tested '
         '**restore**, every post-incident review becomes a discussion about memory.'),
        ('The patch window',
         '**Lifecycle** managed with Operations, not against them: a maintenance window agreed in '
         'advance is a change; the same patch without a window is an outage.'),
        ('The service page',
         'Availability, incidents by cause, backlog and cost — one page that lets a decision be taken '
         'in a meeting.')]:
        m.bullet(label, body, after=16)

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director',
         'ELOHVAC ApS · Copenhagen · May 2023–present',
         '5 electricians and 3 apprentices · full P&L · contracting and service',
         [('Service, cost and accountability',
           '**Service management** with agreements, response times and cost per case; full **P&L** and '
           'budget responsibility; recruiting, onboarding and coaching of eight employees; APV, LOTO '
           'and safety.')]),
        ('Co-owner and CTO / Technical Lead, AI department',
         'Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 (alongside ELOHVAC)',
         '4–10 people · technical and industrial applications',
         [('Data, monitoring and reporting',
           'Monitoring and **KPI** models for technical services; company has ceased trading.')]),
        ('Senior Commissioning Engineer / Project Manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · GMP/FDA/EMA',
         [('Commissioning, interfaces and handover',
           '**FAT/SAT**, **IQ/OQ/PQ** and handover across 37 projects; zero critical deviations, and '
           'documentation built while the work was done rather than after it.')]),
        ('Project and Workshop Manager',
         'Ventek-Air · Copenhagen · Jan 2022–Nov 2022',
         '14 employees · 11 simultaneous site projects',
         [('Capacity and supplier interfaces',
           'Daily capacity plan for 11 sites and 14 fitters; subcontractors and suppliers coordinated '
           'so interfaces did not become delays.')]),
        ('Operations and Maintenance Manager',
         'Biofos (Lynetten) · Copenhagen · Aug 2017–Jan 2022',
         'Wastewater plant in 24/7 operation · SCADA, PLCs, HV switchgear',
         [('24/7 operation, incidents and energy',
           'On-call duty and **incident management** around the clock; root-cause follow-up and planned '
           'maintenance; **over 40 % lower energy consumption** through measurement and '
           're-commissioning.')]),
        ('Electromechanical Technician / Production Team Lead',
         'ARJ Engineering · Tehran · Dec 2003–Mar 2010',
         '12 technicians · machine shop · machinery and equipment',
         [('Assets, maintenance and training',
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
    m.para('English (working language) · Danish (first language) · Persian (mother tongue) · **IT**: '
           '**SCADA** and **PLC** operations and log analysis, industrial networks and **monitoring**, '
           '**MS Office** with **Excel** models for availability and cost, **ERP** and ticketing systems, '
           'own **Python** tools for data · **Driving licence B and own car** · Ready to relocate for '
           'Kolding · Available after agreement · References on request.', after=50)

    m.models_table('THE ROLE AS ADVERTISED — WHAT I BRING', ('Requirement', 'Evidence'), [
        ('End-to-end accountability for the OT Infrastructure service area',
         'Owned a 24/7 operation and a company with full **P&L**: availability, incidents, cost and '
         'improvement on one page, signed by me.'),
        ('Lead and develop the service area teams and set clear priorities',
         '25 specialists, 14 fitters, 12 technicians and eight employees led; priorities set weekly '
         'and specialists left in charge of their own expertise.'),
        ('Empower technical specialists to deliver',
         'The technical call stayed with the specialist; priorities, risk and money stayed with me — '
         'and both were written down so nobody had to guess.'),
        ('Risks, incidents and recurring problems driven to resolution',
         '**Incident management** in 24/7 duty with root-cause follow-up: the same failure twice became '
         'a change in design, not a third repair.'),
        ('Own the service strategy and roadmap, including budget and lifecycle',
         'Roadmap and **budget** written from an asset inventory: what is end-of-life, what it costs '
         'and which year it must happen — the discipline of 37 CAPEX projects.'),
        ('Operational governance using performance, risks, KPIs and technical input',
         'Monthly **KPI** page with availability, incidents by cause and backlog; decisions logged with '
         'owner and date, reviewed before the next period.'),
        ('Manage stakeholders across OT, Operations, IT, Cybersecurity, Procurement and suppliers',
         'Twenty years across disciplines: electrical, mechanical, control and suppliers at Lynetten; '
         'consultants, contractors and quality at Novo; customers and vendors in my own company.'),
        ('Manage critical incidents and operational risks with leadership and escalation',
         'On-call leadership for five years: escalation path named before the shift, one incident '
         'owner, and the plant informed before it asked.'),
        ('Make lessons learned result in sustainable improvements',
         'Every significant incident ended in a written change — procedure, spare part, training or '
         'design — tracked to closure; that is how 37 projects reached handover clean.'),
        ('Drive continuous improvement and challenge existing ways of working',
         '**Continuous improvement** measured, not claimed: over 40 % lower energy consumption at '
         'Lynetten came from challenging the existing setpoints with data.'),
        ('Keep the service reliable, resilient and fit for the future',
         'Resilience built before it is needed: redundancy, tested **restore**, a rota that survives '
         'holidays — learned where the alarm did not care what day it was.'),
        ('5+ years in operational management, O&M, IT/OT service management or asset management',
         'Operations and maintenance manager for five years, project and workshop management, service '
         'ownership and full P&L since 2023 — asset-intensive throughout.'),
        ('Leading technical teams or services with a track record of improving performance',
         'Teams of specialists and fitters led through measured improvements: energy, capacity, '
         'handover quality and delivery on the agreed date.'),
        ('Good understanding of OT infrastructure, sufficient to lead specialists',
         '**Operational technology** in daily use for five years — **SCADA**, **PLC**, industrial '
         'networks and **monitoring** — on the operator side, where a wrong decision stopped production; '
         'enough to challenge a recommendation and know when to defer.'),
        ('Service management: performance, incident and problem management, lifecycle, risk',
         'Service agreements with response times and **SLA**, incident and problem follow-up, lifecycle '
         'planning and **risk management** with a named owner — not a spreadsheet.'),
        ('Strong stakeholder management and communication across functions and suppliers',
         'English and Danish in writing and in the room: technical teams, suppliers, authorities and '
         'management — including the conversations where the message was not welcome.'),
        ('Relevant degree in engineering, technology, business or equivalent experience',
         '**Authorised maskinmester** (LV/MV/HV) and B.Tech in technology management and mechanical '
         'engineering, GPA 7.6/12 — plus twenty years of practice.'),
        ('Fluency in English, written and spoken',
         'English is my working language with suppliers and colleagues abroad; documentation, '
         'procedures and reporting written in English for years.'),
        ('Central server infrastructure, asset data concentrators, backup and restore',
         'Not my domain yet. I have run the operational side of SCADA and PLC estates, including '
         '**backup** and **restore** tests, on **onshore** assets and in 24/7 plant; the difference now '
         'is the architecture, not the discipline.'),
        ('Communication backbone and Edge-to-Wide-Area connectivity',
         'Networks and remote sites at Ventek-Air (11 sites) and Lynetten (24/7): **connectivity** and '
         '**failover** in **onshore** plant as operational risk, and the **WAN** hop as the dependency '
         'it is — the same logic an **offshore** fleet depends on.'),
        ('Challenge recommendations and make informed decisions',
         'Recommendations tested with three questions: what does it protect, what does it cost, and what '
         'happens if we wait — then decided, and written down with the reasoning.'),
        ('Create clarity and set priorities for specialists',
         'One board, one list, one status: what is being worked on, what is waiting and what has been '
         'dropped — visible to the team and to Operations.'),
        ('Provide direction during incidents and operational pressure',
         'Calm is a procedure: contain, communicate, restore, review. Practised through five years of '
         'nights when the plant was down and the phone did not stop.'),
        ('Collaborate across functions and be solution-oriented',
         'Solutions arrived at with the people who have to live with them — Operations, IT, suppliers — '
         'rather than announced to them afterwards.'),
        ('Motivated by improving reliability, resilience and ways of working over time',
         'The part of the job I keep coming back to: the second year is better than the first, because '
         'the failures of the first were written down and designed out.'),
    ])

    m.section('FIRST 90 DAYS')
    for b in (
        'Weeks 1–2: read the architecture, the incident history and the risk register; a shift in the '
        'control room and a site visit — without changing anything.',
        'Weeks 3–6: one page per theme with availability, incidents by cause, backlog and run cost, so '
        'the service area has a baseline everybody recognises.',
        'Months 2–3: escalation and incident ownership written down and tested; the three recurring '
        'problems with the highest cost taken to Engineering with a proposal each.',
        'Month 3: roadmap draft with lifecycle years and budget, reviewed with Operations, IT, '
        'Cybersecurity and Procurement.'):
        m.bullet('', b, after=16)

    m.section('WHAT I WOULD ASK')
    for b in (
        'Which dependency hurts most today — the site link, the concentrator estate, or the OT/IT '
        'interface?',
        'What does the lifecycle look like in three years, and is the money set aside for it?'):
        m.bullet('', b, after=16)

    m.para('**I would welcome the chance to visit Kolding and the OT team.** Contact: +45 93 99 95 14 · '
           'ajlooshahram@gmail.com.', after=24)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Vattenfall_OTOandM.docx')
    build(out)
    print(out)
