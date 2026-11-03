# -*- coding: utf-8 -*-
"""Danfoss Power Solutions, req. 52403: English application and CV."""
import os
from master_design import MasterDoc
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Technical leadership | Engineering delivery and innovation'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'

def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('3 November 2026')
    m.meta('Danfoss Power Solutions · Control & Connectivity Solutions · Copenhagen / Northern Europe')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Senior Manager, Technology & Innovation · Req. 52403', bold=True, color='1A1A1A')
    m.para('The next generation of machine controls must connect a clear customer need to a platform that engineering teams can build, validate and support. For Danfoss, that means making deliberate choices across controllers, displays, remote controls and joysticks while keeping safety, connectivity, cost and product readiness visible from the beginning.', after=80)
    m.para('The first task is to bring architects, innovation engineers and portfolio colleagues around the same decisions. I would map the existing technology roadmap against customer and regulatory needs, identify dependencies between electronics, embedded software, communications and mechanical design, and agree where further evidence is needed before committing resources.', after=80)
    for label, body in [
        ('People and technical direction', 'Combine people leadership, regular 1:1s and clear decision ownership to develop specialists and make room for constructive challenge. Technical leads own detailed architecture recommendations; the team agrees priorities and records the trade-offs.'),
        ('From idea to product', 'Create a visible technology pipeline from exploration and proof-of-concept to maturation and product-development handover. Each opportunity needs an owner, customer problem, testable hypothesis, evidence, risk and next decision.'),
        ('Safety and investment', 'Bring functional safety, machinery regulations, cybersecurity and compliance specialists into reviews early. Compare options using lifecycle risk, resource needs and a proportionate business case—not technology enthusiasm alone.'),
        ('Cross-functional decisions', 'Work with Engineering, Portfolio Management, Product Management and Procurement to align architecture principles, platform choices and supplier dependencies. Keep a concise decision log and review unresolved interfaces with the people accountable.')]:
        m.bullet(label, body, after=35)
    m.para('My experience brings technical team leadership, regulated commissioning and electrical/mechanical delivery, rather than a proven track record designing embedded mobile-machine product platforms. I would rely on the architects and relevant safety and security specialists for domain decisions while building the depth required for this portfolio.', after=80)
    m.para('Danfoss’s PLUS+1 ecosystem and operator interfaces show why platform thinking and customer context matter together. In the first 90 days, I would establish the team’s priorities, agree a roadmap baseline and bring a small set of evidence-backed opportunities to review. I would welcome a discussion about the technical leadership the team needs and the Copenhagen/remote arrangements.', after=80)
    m.meta('Yours sincerely,', after=20)
    m.meta('Shahram Ajloo', after=0)

    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'LEADERSHIP PROFILE')
    m.para('Technical leader and electrically authorised marine engineer (maskinmester), with experience coordinating multidisciplinary specialists, leading operational teams and delivering electrical systems in regulated environments. Combines practical plant and controls knowledge with project economics, people development and continuous improvement. Active professional AI and Claude coder, building planning tools and investment models for development and new business ideas.', after=80)
    m.section('LEADERSHIP & ENGINEERING EXPERIENCE')
    for label, body in [
        ('Multidisciplinary delivery', 'Novo Nordisk: coordinated 25 specialists across engineering, procurement and plant in a portfolio of 37 concurrent CAPEX projects, DKK 2–10 million each.'),
        ('People development', 'ELOHVAC: lead five electricians and three apprentices through day-to-day planning, 1:1s and structured training. Ventek-Air: led a team of 14 on 11 concurrent projects.'),
        ('Safety and quality', 'Novo: FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA, with no critical findings at handover. ELOHVAC and Biofos: risk assessments and LOTO in operational work.'),
        ('Practical innovation', 'Built Python/Claude API tools for estimating, scheduling, quality and KPI tracking at ELOHVAC; reported productivity improvement over 40%. Investment modelling includes NPV, IRR and scenario sensitivity.'),
        ('Delivery and resources', 'Full P&L, quotations, subcontractors and material planning at ELOHVAC; progress, risk, resource and cost reporting to management and client at Novo.')]:
        m.bullet(label, body, after=30)
    m.models_table('LEADERSHIP & IMPROVEMENT METHODS', ('Area', 'Evidence from practice'), [
        ('Coaching', 'Situational leadership, 1:1s and apprentice development at ELOHVAC; adapt support to the individual and task.'),
        ('Shared priorities', 'Daily visual planning and bottleneck analysis at Ventek-Air to coordinate capacity and delivery.'),
        ('Learning and quality', 'PDCA, A3 and root-cause analysis at Novo; 5S and Standard Work in Biofos workshop and stores.'),
        ('Risk and resources', 'Progress, cost and risk follow-up across Novo project interfaces; estimating and P&L ownership at ELOHVAC.')])
    m.section('SELECTED RESULTS')
    for label, body in [('25 specialists', 'Coordinated across engineering, procurement and plant at Novo Nordisk.'), ('11 projects / 14 people', 'Led project and workshop capacity from specification to formal handover at Ventek-Air.'), ('40% lower energy costs', 'Delivered through a PDCA improvement programme at Novo Nordisk.')]:
        m.bullet(label, body, after=30)

    m.page_break()
    m.section('PROFESSIONAL EXPERIENCE')
    jobs = [
        ('Owner / Technical Director / Electrically Authorised Marine Engineer', 'ELOHVAC ApS · Copenhagen · May 2023–present', 'Five electricians and three apprentices · full P&L', [
            ('Technical delivery', 'Electrical, ventilation and climate installations: customer quotations, planning, material management, subcontractors, quality assurance and handover.'),
            ('People and operations', 'Daily work allocation, 1:1s and apprentice training; LOTO and site risk assessment. No critical deviations in service agreements.'),
            ('Digital improvement', 'Built Python/Claude API tools for quotations, schedules, quality checks and KPIs; more than 40% productivity improvement in operations.')]),
        ('Senior Commissioning Engineer / Project Manager, Electrical Systems', 'Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024', '37 concurrent CAPEX projects · 25 specialists · DKK 2–10m per project', [
            ('Cross-functional leadership', 'Coordinated engineering, procurement and plant teams; followed progress, cost, risk and resources, and reported monthly to management and the client.'),
            ('Regulated delivery', 'FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA with no critical findings at handover; electrical panels, controls and UPS. Used SAP ERP for cost and assets.'),
            ('Improvement', 'Applied PDCA, A3 and root-cause analysis; energy costs reduced by 40% through a PDCA programme.')]),
        ('Project and Workshop Manager', 'Ventek-Air · Copenhagen · Jan 2022–Nov 2022', '14-person team · 11 concurrent projects', [
            ('Planning and coordination', 'Managed capacity and progress from specification to handover, including tenders, subcontractors, contractual and safety documentation. Daily boards and bottleneck analysis improved delivery.')]),
        ('Maintenance and Operations Manager / Workshop Technician', 'Biofos, Lynetten · Copenhagen · Aug 2017–Jan 2022', 'Critical 24/7 operations · pumps, HVAC, electrical systems and SCADA', [
            ('Reliability', 'Preventive maintenance, troubleshooting and spare-parts flow; applied 5S, Standard Work, PDCA, LOTO and risk assessments.')]),
        ('Electromechanic / Production Team Leader', 'ARJ Engineering · Tehran · Dec 2003–Mar 2010', '12 mechanics and technicians', [
            ('Workshop leadership', 'Shift planning, materials and target follow-up; fault diagnosis and repair of industrial electrical and mechanical equipment.')])]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets: m.bullet(label, body, after=25)
    m.section('EDUCATION & AUTHORISATIONS')
    m.edu('B.Tech, Technology Management & Mechanical Engineering (marine engineering)', 'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · EQF 6')
    m.edu('Electrical and mechanical design, electrical engineering', 'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Electrically authorised marine engineer (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('Refrigeration and air conditioning · STCW safety and engine-room watch', 'Mercantec 2021 · Danish Maritime Authority 2021–2023')
    m.section('LANGUAGES & LOCATION')
    m.para('English: professional working proficiency · Danish and Persian/Farsi: native · Based in Måløv, Denmark. Copenhagen/remote work, travel and employment arrangements to be agreed.', after=70)
    m.section('REFERENCES')
    m.para('Former managers at Novo Nordisk and Biofos available by agreement.', after=70)

    m.page_break()
    m.models_table('FIRST 90 DAYS — PROPOSED APPROACH', ('When', 'People, decisions and outputs'), [
        ('Week 1', 'Meet architects and innovation engineers individually and review the current roadmap, portfolio commitments, architecture decisions and customer priorities with Engineering and Portfolio leaders. Agree expectations and decision rights.'),
        ('By day 30', 'Map platform dependencies and open questions for controllers, displays, remote controls and joysticks. Establish a shared opportunity and risk register, team 1:1s and a regular cross-functional review; identify safety and security expertise needed.'),
        ('By day 60', 'With technical leads, compare a small number of opportunities by customer value, feasibility, maturity, risk and resource needs. Agree proof-of-concept success criteria, owners and review dates with Product Management and Procurement.'),
        ('By day 90', 'Present an evidence-based technology roadmap baseline and recommended next decisions to Engineering and Portfolio leaders. Agree handover criteria for mature opportunities and review team capacity and learning priorities.')])
    m.section('HOW I WOULD LEAD THE WORK')
    for label, body in [
        ('Technical decisions', 'Invite competing views and record assumptions, alternatives and trade-offs. Architects lead the detailed assessment; decisions are made at the agreed level and revisited when evidence changes.'),
        ('Capability and inclusion', 'Hold regular 1:1s, agree development goals, support continuous learning and give clear feedback. Create space for all specialists to contribute, including colleagues working remotely across locations.'),
        ('Innovation discipline', 'Use short learning cycles and PDCA to test a hypothesis, expose uncertainty and decide whether to progress, change direction or stop. Avoid treating a proof-of-concept as a production-ready platform.'),
        ('Business and governance', 'Connect customer and market needs to investment choices and measurable learning. Use scenario and sensitivity analysis where useful, with Finance and technical owners validating assumptions.')]:
        m.bullet(label, body, after=35)
    m.section('TECHNOLOGY CONTEXT')
    m.para('The role requires deep experience in embedded and connected mechatronic systems, system architecture and product platforms. My documented background is in electrical and mechanical plant delivery, controls, operations and technical leadership; it does not establish a track record in embedded product development, mobile-machine platforms, functional safety or cybersecurity. I would work with domain experts and develop that understanding through focused learning.', after=80)
    m.para('Python, Claude Code and Claude API support my own planning and investment modelling, including NPV, IRR and scenario analysis. Any use at Danfoss would follow company data and AI policies, with technical and financial assumptions checked by the relevant experts.', after=80)
    m.section('HANDOVER TO PRODUCT DEVELOPMENT')
    m.para('Agree the evidence, remaining risks, ownership and resources required before a technology moves into product development. Review interfaces and unresolved questions with the receiving team rather than treating handover as a single milestone.', after=80)
    m.section('CORE STRENGTHS')
    m.para('Technical leadership · team development · cross-functional engineering · regulated commissioning · electrical systems · risk and quality · project economics · continuous improvement · PDCA · A3 · Python · Claude Code · investment modelling', after=70)
    return m.save(path, title='Application and CV — Senior Manager, Technology & Innovation, Danfoss (52403)', subject='Technical leadership and technology innovation', keywords='Danfoss, 52403, technical leadership, engineering, innovation')

if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Danfoss_SeniorManagerTechnologyInnovation.docx')))
