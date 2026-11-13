# -*- coding: utf-8 -*-
"""Hitachi Energy — Engineering Manager, Grid & Power Quality Solutions and Service (HBUEU).

English posting -> English document (en-GB), per master/README.md rule 1.

Form (master/FORMKATALOG.md): opening **K** (the contradiction: their own sentence about
inclusion turned into the operational problem of a team in three countries), structure
**Before / in twelve months** (six lines, each with evidence), register **Switchyard** (new:
bay, feeder, busbar, breaker, interlock, AIS/GIS, energisation, outage window).
Culture file: jd/HitachiEnergy_EngineeringManager_kultur.txt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Engineering Manager · lead engineers, three countries'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('13 November 2026')
    m.meta('Hitachi Energy · Grid & Power Quality Solutions and Service, HBUEU · Ballerup, Denmark')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Engineering Manager, Project Management Engineering', bold=True, color='1A1A1A')

    # ---------------------------------------------------------------- page 1
    m.para('**You write that inclusion drives our culture of innovation and collaboration. In an '
           'engineering department spread across Vaasa, Västerås and Ballerup, inclusion is not a '
           'value statement — it is the only reason a lead engineer in one country knows what was '
           'decided in another country on Tuesday.** Distance does not create that problem. Distance '
           'reveals it: two teams solve the same interface in two ways, the customer hears two '
           'answers, and the rework lands three weeks later in the bay where the panel was ordered '
           'to the wrong cable schedule.', after=60)

    m.para('**Hitachi Energy is building the infrastructure of the energy transition — hydrogen, data '
           'centers and e-mobility** — and this role does not design the substation. It makes sure the '
           'people who do can decide, in time, to the same standard, in three countries. That is the '
           'job I have done at a smaller scale: 25 specialists across 37 parallel capital projects, 14 '
           'technicians and fitters on 11 simultaneous site projects, 8 employees in my own company. '
           'The constraint was never knowledge. It was the decision nobody had been given the right to '
           'make.', after=60)

    m.para('**Six lines I would be measured on: today, and in twelve months.**', after=50)

    m.para('**Decision rights.** Today an interface question travels up until it meets someone willing '
           'to answer, and the answer stays in that head. In twelve months each lead engineer has a '
           'written map of what they decide alone, what they decide with a peer in another country, '
           'and what comes to me — with a name and a date on the ones that come to me. I have run that '
           'map on 37 projects.', after=44)

    m.para('**Capacity.** Today resource demand is described once someone is already overloaded. In '
           'twelve months there is a rolling twelve-month view per country and competence, so a lead '
           'engineer sees in March what the fourth quarter will ask for. The method is the one I used '
           'daily with 11 site projects and 14 people: capacity analysis in the morning, '
           're-prioritisation the same day, one plan everyone can read.', after=44)

    m.para('**One engineering standard.** Today three countries have three good practices and one '
           'shared problem: each is locally right and collectively expensive. In twelve months one '
           'written standard for documentation and interface control covers all teams — built with the '
           'engineers, not sent to them, which is how 5S and standard work became real on a workshop '
           'floor and in a 24/7 plant.', after=44)

    m.para('**Competence with a successor behind every key person.** Today the department knows who is '
           'competent; it does not know who is next. In twelve months there is a competence matrix per '
           'team, a named successor for each critical role and a development plan per engineer — the '
           'tool I built for 12 technicians and 3 apprentices, where the point was that the work could '
           'continue without me.', after=44)

    m.para('**Delivery quality, measured before the customer measures it.** Today quality appears when '
           'a customer complains. In twelve months the department reports first-time-right and rework '
           'per project, and a lead engineer can show me the trend before I ask. I have delivered 37 '
           'capital projects with zero critical deviations at handover and cut energy consumption by '
           'over 40 per cent in a 24/7 plant — both came from measurement, not from effort.',
           after=60)

    m.para('**What I do not have, said plainly.** I have not designed an **AIS** or **GIS** '
           '**substation**, and I am not a substation engineer. What I have is a high-voltage '
           'background: authorised **LV/MV/HV** (Danish Safety Technology Authority, 2023), five years '
           'of **high voltage** switchgear and **switchgear** operations in a 24/7 plant, and twelve '
           'years in the **energy** sector. The technology I would learn from your lead engineers; the '
           'leadership of the engineers working on it is what I bring.', after=60)

    m.para('**Your own words are why I am applying.** **»Inclusion drives our culture of innovation and '
           'collaboration«** is written as an equation: **»Diversity + Collaboration = Great '
           'Innovation«** — and an equation can be tested. It holds when a **lead engineer** in '
           'Västerås asks a colleague in Vaasa for a review before the deadline, not after. '
           '**»Safety and integrity«**, **»taking responsibility for your own actions while caring for '
           'your colleagues and the business«**, is the leadership I practised in 24/7 operations, '
           'where the shortcut is always available and never acceptable. **»We push boundaries, we '
           'break records and we never give up«** is the culture; what makes it survive three '
           'countries is that processes exist to **»capture and share best practices«**, that '
           '**»developing people, driving performance, and taking ownership«** is spent on people, that '
           '**»zero harm«** and **Diversity 360** carry numbers, and that a **»life-long learning '
           'culture«** has a matrix behind it rather than a poster. That is how **»high-quality '
           'engineering delivery«** and **»customer commitments«** become one conversation inside a '
           'company **»advancing a sustainable energy future for all«** and working towards **»abundant, '
           'secure, affordable, and sustainable electricity for all«**.', after=60)

    m.para('**Practical.** I live in Måløv, fifteen minutes from the **Ballerup** office, so Denmark is '
           'my base and I would travel to Vaasa and Västerås as a fixed part of the month. Danish and '
           '**English** fluently, not Finnish or Swedish — the working language would be English, and '
           'I am used to technical documentation and negotiation in it. Available after notice. What I '
           'would want to understand first is how lead engineers are allocated today: by country, by '
           'project or by competence.', after=50)

    m.meta('Kind regards', after=15)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('**Engineering and operations leader** — authorised **LV/MV/HV** engineer, B.Tech in '
           'Technology Management and Mechanical Engineering (7.6/12). Twenty years in electrical '
           'engineering, operations and project delivery. Led **25 specialists** across **37 parallel '
           'capital projects**, **14 employees plus subcontractors** on **11 simultaneous site '
           'projects**, and an **8-person company with full P&L** since 2023. Built competence '
           'matrices, standards and KPI routines; cut energy consumption by **more than 40 per cent** '
           'in a 24/7 plant.', after=70)

    m.section('SWITCHYARD — ENGINEERING DELIVERY ACROSS SITES AND COUNTRIES')
    for label, body in [
        ('Lead engineers and specialists',
         'Led **25 specialists** across 37 parallel capital projects in a regulated plant, with '
         'engineering, procurement and site organisations as counterparts; every **interface** named '
         'in a matrix with an owner and a date.'),
        ('Capacity and resource demand',
         '**Capacity management** daily: analysis each morning, re-prioritisation the same day and one '
         'plan for 11 simultaneous site projects with 14 people and subcontractors.'),
        ('Standards, competence and succession',
         '**5S**, standard work and PDCA in a workshop and in 24/7 operations; **competence matrix** '
         'per team with a **succession** behind critical roles — 12 technicians and 3 apprentices '
         'trained to a written standard.'),
        ('Quality and delivery',
         '**37** capital projects at DKK 2-10m each with **zero critical deviations** at handover under '
         'GMP/FDA/EMA; **KPI** reporting monthly with deviation explanations to management and client.'),
        ('High voltage and energy',
         'Five years of **high voltage** switchgear, protection and **switchgear** operation in a 24/7 '
         'plant; **over 40 per cent** lower energy consumption through measurement and '
         're-commissioning.')]:
        m.bullet(label, body, after=16)

    m.section('PROFESSIONAL EXPERIENCE')
    jobs = [
        ('Owner / Technical Director',
         'ELOHVAC ApS · Copenhagen · May 2023 – present',
         '5 electricians and 3 apprentices · full P&L · electrical contracting',
         [('Engineering, customers and economics',
           'Tenders and **cost** calculation, change management, **quality**, **commissioning** and '
           '**schedule**; **safety** with risk assessment, LOTO and safety walks.')]),
        ('Co-owner and CTO / Technical Head of the AI department',
         'Data Power Consultant ApS · Copenhagen · 2024 – Nov 2026 (in parallel with ELOHVAC)',
         '4-10 people · technical and industrial applications',
         [('Engineering management with AI',
           'Technical applications for industrial clients, AI-assisted design workflows and AI in '
           'management reporting, decision briefs and **KPI** analysis; the company has closed.')]),
        ('Senior Commissioning Engineer / Project Manager, Electrical Systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022 – Jul 2024',
         '37 parallel capital projects · 25 specialists · GMP/FDA/EMA',
         [('Specification, delivery and handover',
           'Requirement specifications, FAT/SAT and IQ/OQ/PQ; deviations closed with name and date, no '
           'critical findings at handover.')]),
        ('Project and Workshop Manager',
         'Ventek-Air · Copenhagen · Jan 2022 – Nov 2022',
         '14 employees · 11 simultaneous site projects',
         [('Schedule, capacity and subcontractors',
           'Daily board meeting, **capacity** analysis and same-day re-prioritisation; subcontractor '
           '**interfaces** and handover packages.')]),
        ('Operations and Maintenance Manager',
         'Biofos (Lynetten) · Copenhagen · Aug 2017 – Jan 2022',
         '24/7 treatment plant · pumps, high voltage switchgear, SCADA',
         [('Operations, standards and energy',
           'Maintenance and modification in live operation; **over 40 per cent** lower energy '
           'consumption; **5S** and **safety** practice introduced as standard.')]),
        ('Electromechanical Technician / Production Team Leader',
         'ARJ Engineering · Tehran · Dec 2003 – Mar 2010',
         '12 technicians · machine workshop · fleet and equipment',
         [('Workshop, equipment and training',
           'Fault diagnosis, calibration and repair; procurement and maintenance of machines and '
           'vehicles; training and target follow-up for 12 technicians.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=16)

    m.section('EDUCATION AND AUTHORISATION')
    m.edu('B.Tech, Technology Management and Mechanical Engineering',
          'Copenhagen School of Marine Engineering and Technology Management · 2017-2022 · GPA 7.6/12')
    m.edu('Authorised LV/MV/HV engineer (elautoriseret maskinmester)',
          'Danish Safety Technology Authority · May 2023')
    m.edu('Refrigeration and ventilation technology · vocational (AMU)',
          'Mercantec 2021 · STCW, Danish Maritime Authority 2021')
    m.edu('Electrical and Mechanical Design, Electrical Engineering',
          'Tehran Technical University · 2000-2003 · EQF 6')

    m.section('LANGUAGES, IT AND PRACTICAL')
    m.para('Danish (native) and **English** (professional, written and spoken) · Persian (native) · '
           '**IT**: ERP-based project and finance systems, CMMS, Excel and own **Python** tools for '
           '**KPI**, checklists and reporting; familiar with BIM-based project collaboration and IEC '
           'documentation practice · **Driving licence B and own car** · Måløv, 15 minutes from the '
           '**Ballerup** office; travel to **Vaasa** and **Vasteras** accepted · Available after '
           'notice.', after=50)

    m.models_table("THE POSTING'S REQUIREMENTS — WHAT I HAVE", ('Requirement', 'Evidence'), [
        ('Lead the Project Management Engineering lead engineers team across Finland, Sweden and Denmark',
         'Led specialist teams and their leaders for twenty years: **25 specialists** across 37 '
         'projects, 14 employees on 11 site projects, 8 employees in my own company.'),
        ('Regular travel between our offices and leading employees based across all locations',
         'Two years of weekly commuting to a plant 110 km from home, and teams spread over several '
         'sites with one plan, one board and a fixed weekly rhythm per location.'),
        ('Provide strategic leadership',
         'Direction set as three goals per quarter rather than thirty, translated into monthly **KPI** '
         'follow-up with named owners.'),
        ('Develop and empower your team',
         '**Competence development** through a **competence matrix**, appraisal cycles, 1:1s and a '
         'delegation ladder; 12 technicians and 3 apprentices trained to a written standard.'),
        ('Ensure high-quality engineering delivery that meets business requirements and customer commitments',
         '**37** capital projects with zero critical deviations at handover; **customer commitments** '
         'tracked as delivery milestones in every monthly report.'),
        ('Work closely with cross-functional teams to drive performance',
         'Engineering, procurement, site and client organisations in one **cross-functional** meeting '
         'series with one decision log — in 37 projects and in my own company.'),
        ('Strengthen engineering capabilities',
         'Standards for documentation and interface control written with the engineers who use them; 5S '
         'and standard work introduced on a workshop floor and in 24/7 operations.'),
        ('Contribute to the development of innovative customer solutions',
         'Customer solutions from requirement to handover in 37 projects; today also AI-assisted '
         'design and calculation workflows in my own company.'),
        ('Collaborate with other departments to manage supplies from an engineering perspective',
         '**Interfaces** to procurement and suppliers named in a matrix in every project; supplier '
         'deliveries followed weekly against **schedule**.'),
        ('Analyse resource demand for capacity management',
         '**Capacity management** daily in 11 simultaneous projects: demand per competence, '
         're-prioritisation the same day, rolling plan.'),
        ('Develop team priorities and set goals for team members to achieve operational results',
         'One board per team with three priorities and an owner each; **performance goals** tied to '
         'the board and reviewed monthly, with an appraisal and development plan for every employee.'),
        ('Build operational capacity through people management and deploy the necessary frameworks',
         'Grew a company to 8 employees and a workshop to 12 technicians, with recruitment, training '
         'and **succession** planned early; **frameworks** for quality, safety and documentation built '
         'from scratch and introduced into a GMP organisation.'),
        ('Ensure processes and tools are in place to capture and share best practices',
         'Every project closed with three written improvements entering the standard, shared at a fixed '
         'agenda item; processes plus tools I built myself — checklists, **KPI** dashboards and '
         '**Python** reporting used daily by the teams.'),
        ('Ensure policies, practices and procedures are understood and followed',
         'Compliance as a management routine: audits, safety walks and deviation handling with name and '
         'date — zero critical findings at handover.'),
        ('Develop the team and build the capacity required by the strategic plan',
         'Development plans aligned to what the organisation needed next, not what was convenient; two '
         'technicians moved into leading roles.'),
        ('Bachelor of Engineering or equivalent relevant professional experience',
         '**B.Tech** in Technology Management and Mechanical Engineering (GPA 7.6/12), authorised '
         '**LV/MV/HV** engineer and twenty years of professional practice.'),
        ('Knowledge of substation technology AIS and GIS',
         'Not a substation designer: my high-voltage experience is switchgear, protection and operation '
         'in a 24/7 plant, plus twelve years in the **energy** sector. **AIS** and **GIS** would be '
         'learned from your lead engineers.'),
        ('Communication, negotiation and interpersonal abilities',
         '**Negotiation** with clients, subcontractors, suppliers and internal **stakeholders** for '
         'twenty years; briefs of one to two pages and minutes with name and date, in Danish and '
         '**English**.'),
        ('Strategic mindset combined with strong problem-solving capabilities',
         'Strategy translated into measurable routines; problem-solving with 5xWhy, Ishikawa and A3, and '
         'with data before opinion.'),
        ('Previous experience in the energy sector',
         'Twelve years in **energy** and utilities: a 24/7 treatment plant, a pharma capital programme '
         'and an electrical contracting company since 2023.'),
        ('Fluency in English, both written and spoken',
         '**English** as working language for documentation, FAT/SAT and supplier negotiation; Danish '
         'native, Persian native.'),
        ('Willingness to work in one of the Hitachi Energy offices in Vaasa, Vasteras, Ballerup or Middelfart',
         '**Ballerup** is fifteen minutes from my home; **Middelfart** and travel across the **Nordic** '
         'countries are acceptable, and I would be present where the teams are.')])

    m.section('FIRST 90 DAYS')
    for b in (
        'Visited the three locations, sat with each lead engineer and mapped what they decide today, '
        'what they escalate and what nobody owns.',
        'Built the first capacity view per country and competence, and tested it against the projects '
        'already running.',
        'Chosen two standards to harmonise first — documentation and interface control, with '
        '**standardisation** owned by the engineers who write them, not by the manager.'):
        m.bullet('', b, after=16)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_HitachiEnergy_EngineeringManager.docx')
    build(out)
    print(out)
