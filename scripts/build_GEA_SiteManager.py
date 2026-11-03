# -*- coding: utf-8 -*-
"""GEA Liquid Technologies — Site Manager, Skanderborg. Combined English application and CV."""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Site Manager | Installation, contractors and project delivery'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'

def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('3 November 2026')
    m.meta('GEA Liquid Technologies · Project Execution · Skanderborg · Attn. Jørgen Pedersen')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Site Manager', bold=True, color='1A1A1A')
    m.para('A successful installation starts before the first contractor arrives. Building readiness, access, equipment, materials, drawings and safe work methods must agree with the sequence on the schedule. On site, the priority is to keep the teams moving safely, resolve interfaces quickly and hand a tested, documented plant to commissioning.', after=80)
    m.para('At GEA, I would establish a site work breakdown structure (WBS) with the Project Manager and engineering, then turn it into a rolling look-ahead plan. A short daily coordination meeting would identify constraints, owners and dates; a shared action and risk register would bring customer decisions and subcontractor issues into the open before they affect the critical work.', after=80)
    for label, text in [
        ('Safety and people', 'Agree site HSE requirements, risk assessments, permits and lifting plans with competent specialists before work starts. Use clear briefings, situational leadership and regular one-to-ones to support teams across disciplines and cultures.'),
        ('Progress and commercial control', 'Track labour hours, material deliveries, earned progress and remaining work against the baseline. Use Earned Value Management (EVM) where agreed, with forecasts and early escalation of deviations. Assess change orders for hours, cost and schedule before approval.'),
        ('Quality and handover', 'Agree inspection points, non-conformity reports, site audits and document ownership with Quality and engineering. Close open items and compile SAT evidence before handover to commissioning engineers; capture lessons learned for the next installation.'),
        ('Preparation between sites', 'Review assembly cost estimates, material needs, logistics, contractor audits, User Requirement Specifications (URS), requests for quotation (RFQs) and purchase orders with the responsible sales and procurement colleagues.')]:
        m.bullet(label, text, after=35)
    m.para('The first week would establish the project baseline and readiness gaps; by day 30 the site rhythm and reporting would be operating, by day 60 corrective actions tracked, and by day 90 lessons translated into practical improvements. My background is electrical and multidisciplinary plant delivery; dairy processing, sanitary welding and Navisworks require a focused introduction with GEA specialists.', after=80)
    m.para('GEA’s Skanderborg Bryghus project shows the value of connecting engineering, installation and customer needs through to a working process plant. I would welcome a conversation about the first site priorities and the practical arrangements for Skanderborg and site travel from Måløv.', after=80)
    m.meta('Yours sincerely,', after=20)
    m.meta('Shahram Ajloo', after=0)

    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('Electrically authorised marine engineer (maskinmester), technical project and people leader with hands-on electrical and mechanical operations experience. Led installation teams and coordinated engineering, procurement and site interfaces in regulated and commercial settings. Experience includes contractor coordination, cost control, safety, FAT/SAT and documented handover. Active professional AI and Claude coder, building planning tools and investment models for development and new business ideas.', after=70)
    m.section('SITE DELIVERY & LEADERSHIP')
    for label, text in [
        ('Teams and subcontractors', 'ELOHVAC: lead five electricians and three apprentices; allocate work, coach through 1:1s and manage subcontractors. Ventek-Air: led a 14-person team across 11 projects.'),
        ('Project coordination', 'Novo Nordisk: coordinated 25 specialists across engineering, procurement and plant on 37 concurrent CAPEX projects, DKK 2–10 million each; tracked progress, resources, risks and costs.'),
        ('HSE and quality', 'LOTO, workplace risk assessments and safety briefings in installation and operations. Novo: FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA, with no critical findings at handover.'),
        ('Costs and suppliers', 'ELOHVAC: estimates, quotations, material planning, subcontractors, quality documentation and full P&L. Ventek-Air: tenders, contractual documentation and handover packages.'),
        ('Digital tools', 'Python and Claude API tools for estimates, schedules, quality checklists and KPI dashboards; over 40% productivity improvement in ELOHVAC operations. Excel/Power Query, Power BI and SAP ERP.')]:
        m.bullet(label, text, after=30)
    m.models_table('LEADERSHIP & IMPROVEMENT METHODS', ('Area', 'Methods applied'), [
        ('People and work', 'Situational leadership, 1:1s and structured apprentice training at ELOHVAC; daily visual planning and bottleneck analysis at Ventek-Air.'),
        ('Safe execution', 'LOTO, risk assessments and follow-up on near misses at ELOHVAC and Biofos.'),
        ('Improvement', '5S, Standard Work and PDCA at Biofos; A3 and root-cause analysis at Novo Nordisk.'),
        ('Project and cost', 'Progress, risk and resource follow-up across engineering and procurement at Novo; estimating and P&L at ELOHVAC.')])
    m.section('SELECTED ACHIEVEMENTS')
    for label, text in [
        ('37 concurrent CAPEX projects', 'Coordinated delivery and 25 specialists at Novo Nordisk; no critical findings at handover.'),
        ('11 projects, 14 people', 'Led Ventek-Air project and workshop resources from specification to formal handover.'),
        ('40% lower energy costs', 'PDCA improvement programme at Novo Nordisk.')]:
        m.bullet(label, text, after=30)

    m.page_break()
    m.section('PROFESSIONAL EXPERIENCE')
    jobs = [
        ('Owner / Technical Director / Electrically Authorised Marine Engineer', 'ELOHVAC ApS · Copenhagen · May 2023–present', 'Five electricians and three apprentices · full P&L', [
            ('Installation and delivery', 'Electrical, ventilation and climate installations; quotations, planning, material management, subcontractors, quality assurance and handover documentation.'),
            ('People and safety', 'Daily work allocation, 1:1s and apprentice training; LOTO and site risk assessments. No critical deviations in service agreements.'),
            ('AI and planning', 'Built Python/Claude API tools for quotations, schedules, quality checks and KPIs; over 40% operational productivity improvement.')]),
        ('Senior Commissioning Engineer / Project Manager, Electrical Systems', 'Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024', '37 concurrent CAPEX projects · 25 specialists · DKK 2–10m per project', [
            ('Execution', 'Coordinated engineering, procurement and plant teams; monitored progress, resources, risk and costs and reported monthly to management and the client.'),
            ('Testing and improvement', 'FAT/SAT and IQ/OQ/PQ in GMP-regulated delivery. Used PDCA and root-cause analysis; energy costs reduced by 40%. SAP ERP for costs and assets.')]),
        ('Project and Workshop Manager', 'Ventek-Air · Copenhagen · Jan 2022–Nov 2022', '14-person team · 11 concurrent plant projects', [
            ('Delivery', 'Managed capacity and progress from specification to formal handover, including tenders, subcontractors, contractual and safety documentation. Daily boards and bottleneck analysis improved delivery.')]),
        ('Maintenance and Operations Manager / Workshop Technician', 'Biofos, Lynetten · Copenhagen · Aug 2017–Jan 2022', 'Critical 24/7 operations · pumps, HVAC, electrical systems and SCADA', [
            ('Reliability and safety', 'Preventive maintenance, troubleshooting and spare-parts flow. Applied 5S, Standard Work, PDCA, LOTO and risk assessments.')]),
        ('Electromechanic / Production Team Leader', 'ARJ Engineering · Tehran · Dec 2003–Mar 2010', '12 mechanics and technicians', [
            ('Workshop leadership', 'Shift planning, materials and target follow-up; fault diagnosis and repair of industrial electrical and mechanical equipment.')])]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, text in bullets: m.bullet(label, text, after=25)
    m.section('EDUCATION & AUTHORISATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering (marine engineering)', 'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · EQF 6')
    m.edu('Electrical and mechanical design, electrical engineering', 'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Electrically authorised marine engineer (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('Refrigeration & air conditioning · STCW safety and engine-room watch', 'Mercantec 2021 · Danish Maritime Authority 2021–2023')
    m.section('LANGUAGES & PRACTICAL INFORMATION')
    m.para('English: professional working proficiency · Danish and Persian/Farsi: native · Driving licence B. Based in Måløv; Skanderborg attendance, site travel and any accommodation arrangements to be agreed.', after=60)
    m.section('REFERENCES')
    m.para('Former managers at Novo Nordisk and Biofos available by agreement.', after=60)

    m.page_break()
    m.models_table('FIRST 90 DAYS — SITE EXECUTION', ('When', 'Actions and deliverables'), [
        ('Week 1', 'With the Project Manager and HSE/Quality leads, review scope, contract, baseline, site readiness, risks, customer interfaces and handover requirements. Meet team and contractors; assign owners and due dates to open issues.'),
        ('By day 30', 'Agree a WBS, activity sequence and rolling look-ahead with engineering and site teams. Establish daily coordination, HSE briefings, labour-hour capture, material/equipment readiness and weekly progress and cost reporting.'),
        ('By day 60', 'Review forecast against budget and baseline; use agreed EVM measures where data permits. Resolve delivery constraints and non-conformities with accountable owners; review change orders, site audits and supplier quality with the PM.'),
        ('By day 90', 'Review readiness for SAT and commissioning handover against inspection and documentation requirements. Record lessons learned and agree one improvement to site planning or documentation with the team.')])
    m.section('WORKING WITH THE PROJECT TEAM')
    for label, text in [
        ('Project Manager and engineering', 'Agree decisions, technical interfaces and design clarifications early; escalate safety, scope, cost or schedule risks with options and an owner.'),
        ('Customer and contractors', 'Coordinate access, building readiness, deliveries and work sequences. Adapt briefings to the teams on site and confirm that responsibilities are understood.'),
        ('Quality, HSE and commissioning', 'Set hold points and safe work expectations before execution; keep inspection records and open-item status visible through handover.'),
        ('Procurement and sales', 'Support assembly estimates and procurement preparation: URS, RFQs, purchase orders and contractor audits with the accountable specialists.')]:
        m.bullet(label, text, after=35)
    m.section('TECHNICAL DEVELOPMENT & DIGITAL TOOLS')
    m.para('The direct experience is electrical installations, multidisciplinary project delivery and mechanical maintenance. Food and dairy processing, hygienic design, piping installation, sanitary weld quality, lifting operations and Navisworks / 3D viewers need role-specific assessment and training; qualified colleagues retain responsibility for specialist decisions. Excel and project reporting provide a foundation for learning GEA’s EVM approach.', after=80)
    m.para('As an active AI/Claude coder, I build tools for planning, quality and analysis, including investment models with NPV, IRR and scenario sensitivity. At GEA, any AI use would be subject to company policy, appropriate data protection and human verification.', after=80)
    m.section('SITE HANDOVER DISCIPLINE')
    m.para('Keep the current drawing revision, inspection status, open issues and customer decisions together in the agreed project system. Before handover, review responsibilities with commissioning and Quality so that outstanding items have an owner and a clear route to closure.', after=80)
    m.section('CORE SKILLS')
    m.para('Site management · assembly teams · installation supervision · subcontractors · material handling · logistics · WBS · schedules · HSE · risk assessments · progress reporting · EVM · cost estimation · financial forecasts · change orders · non-conformity reports · site audits · SAT · commissioning · continuous improvement · Excel · Claude Code', after=60)
    return m.save(path, title='Application and CV — Site Manager, GEA Liquid Technologies', subject='Site installation, safety and project delivery', keywords='site manager, installation, subcontractors, HSE, WBS, SAT, project delivery')

if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_GEA_SiteManager.docx')))
