# -*- coding: utf-8 -*-
"""Google Fredericia — combined English cover letter and CV."""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Critical operations | Electrical & mechanical facilities leadership'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'

def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('3 November 2026')
    m.meta('Google · Data Center Operations · Fredericia, Denmark')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Critical Facilities Manager, Data Center Operations', bold=True, color='1A1A1A')
    m.para('The foundation of a reliable data center is a team that understands its plant, recognizes abnormal conditions early and can act safely when the unexpected happens. Power, cooling and controls must be managed as one operating system: every planned intervention needs a clear owner, a sound risk assessment and a credible recovery path.', after=80)
    m.para('At Fredericia, I would begin by listening to the technicians and reviewing the campus operating baseline with the facilities and safety leads. The first priorities would be to understand equipment dependencies, maintenance backlog, operating procedures, open risks and budget commitments—then agree where attention will make the greatest difference to reliability.', after=80)
    for label, body in [
        ('People and safe execution', 'Use regular 1:1s, situational leadership and GROW coaching to develop technicians; make it safe to raise a concern or stop work. Set clear shift handovers, escalation routes and risk controls, including LOTO where applicable.'),
        ('Reliability and response', 'Review electrical distribution, UPS, HVAC, pumps, controls and the generator arrangements with the responsible specialists. Use preventive maintenance, criticality reviews and after-action learning to protect availability and reduce recovery time.'),
        ('Budget and cost of ownership', 'Connect the operational budget and expense forecasting to asset condition, maintenance priorities and deployment plans. Compare total cost of ownership (TCO) over the asset life, not only the initial purchase price; review assumptions with Finance and Engineering.'),
        ('Campus and partners', 'Agree shared priorities with internal and external business partners. For multi-site deployments, identify dependencies and decision owners before scheduling work; use a common risk and action register and escalate conflicts early.')]:
        m.bullet(label, body, after=35)
    m.para('The first week would establish the operating picture; by day 30 the team and its partners would have a baseline and a short list of risks, by day 60 a reviewed cost and reliability plan, and by day 90 agreed improvements and owners. Google’s published research on coaching and psychological safety aligns with the practical leadership needed in an environment where speaking up matters.', after=80)
    m.para('My background combines critical plant operations at Biofos, regulated electrical project delivery at Novo Nordisk and P&L and team leadership at ELOHVAC. It does not establish nine years managing critical facilities or a mission-critical data center portfolio. I would welcome a discussion of those requirements and the practical arrangements for working in Fredericia from Måløv.', after=80)
    m.meta('Yours sincerely,', after=20)
    m.meta('Shahram Ajloo', after=0)

    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'LEADERSHIP PROFILE')
    m.para('Electrically authorised marine engineer (maskinmester) and technical operations leader with experience in electrical and mechanical plant, 24/7 maintenance, regulated commissioning and team management. Background includes budgets and P&L, engineering coordination, preventive maintenance and safety. Active professional AI and Claude coder, building practical planning tools and investment models for development and new business ideas.', after=80)
    m.section('FACILITIES & LEADERSHIP EXPERIENCE')
    for label, body in [
        ('Critical plant operations', 'Biofos Lynetten: maintained pumps, HVAC, high-voltage switchgear and SCADA in a 24/7 operating environment; preventive maintenance, urgent troubleshooting and spare-parts flow.'),
        ('Electrical systems and quality', 'Novo Nordisk: electrical systems including UPS, switchgear and controls. FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA, with no critical findings at handover.'),
        ('People and coaching', 'ELOHVAC: lead five electricians and three apprentices with work planning, 1:1s and structured training. Ventek-Air: led a 14-person team across 11 projects.'),
        ('Budget and partners', 'Full P&L, estimating and subcontractor coordination at ELOHVAC. At Novo, tracked cost, risk and resources with engineering, procurement and plant across 37 concurrent CAPEX projects.'),
        ('Digital improvement', 'Python and Claude API tools for estimates, scheduling, quality checks and KPI dashboards at ELOHVAC; documented productivity improvement over 40%. Excel/Power Query, Power BI and SAP ERP.')]:
        m.bullet(label, body, after=30)
    m.models_table('LEADERSHIP & OPERATIONAL METHODS', ('Area', 'Applied methods and context'), [
        ('Team development', 'Situational leadership, 1:1s and apprentice coaching at ELOHVAC; daily work allocation and safety follow-up.'),
        ('Operational discipline', 'LOTO and risk assessments at ELOHVAC and Biofos; preventive maintenance and near-miss follow-up at Biofos.'),
        ('Continuous improvement', '5S, Standard Work and PDCA in Biofos workshop and stores; A3 and root-cause analysis at Novo.'),
        ('Planning and delivery', 'Daily boards and bottleneck analysis at Ventek-Air; cost and risk reporting across Novo engineering and procurement interfaces.')])
    m.section('SELECTED RESULTS')
    for label, body in [
        ('40% lower energy costs', 'Achieved through a PDCA programme at Novo Nordisk.'),
        ('25 specialists / 37 projects', 'Cross-functional coordination at Novo on CAPEX projects of DKK 2–10 million each.'),
        ('14 people / 11 projects', 'Ventek-Air project and workshop leadership from specification to formal handover.')]:
        m.bullet(label, body, after=30)

    m.page_break()
    m.section('PROFESSIONAL EXPERIENCE')
    jobs = [
        ('Owner / Technical Director / Electrically Authorised Marine Engineer', 'ELOHVAC ApS · Copenhagen · May 2023–present', 'Five electricians and three apprentices · full P&L', [
            ('Facilities and customers', 'Electrical, ventilation and climate installations, fault finding and preventive maintenance; quotations, materials, subcontractors, quality and handover.'),
            ('People and safety', 'Plan daily work, conduct 1:1s and train apprentices; LOTO and site risk assessments. No critical deviations in service agreements.'),
            ('Digital tools', 'Built Python/Claude API tools for quotations, schedules, quality checks and KPIs; over 40% productivity improvement in operations.')]),
        ('Senior Commissioning Engineer / Project Manager, Electrical Systems', 'Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024', '37 concurrent CAPEX projects · 25 specialists · DKK 2–10m per project', [
            ('Engineering and delivery', 'Coordinated engineering, procurement and plant; monitored progress, resources, risk and cost and reported monthly to management and the client.'),
            ('Reliability and improvement', 'FAT/SAT and IQ/OQ/PQ for regulated delivery; electrical panels, controls and UPS. Applied PDCA and root-cause analysis; energy costs reduced by 40%. SAP ERP for costs and assets.')]),
        ('Project and Workshop Manager', 'Ventek-Air · Copenhagen · Jan 2022–Nov 2022', '14-person team · 11 concurrent plant projects', [
            ('Coordination', 'Managed capacity and progress from specification to handover, including tenders, subcontractors, safety and handover documentation. Daily boards and bottleneck analysis improved delivery.')]),
        ('Maintenance and Operations Manager / Workshop Technician', 'Biofos, Lynetten · Copenhagen · Aug 2017–Jan 2022', 'Critical 24/7 operations · pumps, HVAC, high-voltage switchgear and SCADA', [
            ('Maintenance', 'Preventive maintenance and acute fault finding; workshop and stores improvements using 5S, Standard Work and PDCA. Applied LOTO, risk assessments and near-miss follow-up.')]),
        ('Electromechanic / Production Team Leader', 'ARJ Engineering · Tehran · Dec 2003–Mar 2010', '12 mechanics and technicians', [
            ('Workshop leadership', 'Shift planning, materials and target follow-up; fault diagnosis and repair of industrial electrical and mechanical equipment.')])]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets: m.bullet(label, body, after=25)
    m.section('EDUCATION & AUTHORISATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering (marine engineering)', 'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · EQF 6')
    m.edu('Electrical and mechanical design, electrical engineering', 'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Electrically authorised marine engineer (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('Refrigeration and air conditioning · STCW safety and engine-room watch', 'Mercantec 2021 · Danish Maritime Authority 2021–2023')
    m.section('LANGUAGES & PRACTICAL INFORMATION')
    m.para('English: professional working proficiency · Danish and Persian/Farsi: native · Driving licence B. Based in Måløv; working arrangements, travel and any accommodation in Fredericia to be agreed.', after=70)
    m.section('REFERENCES')
    m.para('Former managers at Novo Nordisk and Biofos available by agreement.', after=70)

    m.page_break()
    m.models_table('FIRST 90 DAYS — PROPOSED FACILITIES PLAN', ('When', 'Priorities and outputs'), [
        ('Week 1', 'Meet technicians, safety leads, site leadership and business partners. Review facility responsibilities, site procedures, active risks, equipment dependencies and emergency escalation. Listen before changing established controls.'),
        ('By day 30', 'Agree a baseline of asset condition, preventive maintenance backlog, safety observations and spending commitments with site leads. Set team 1:1s, shift handover expectations and a recurring risk review.'),
        ('By day 60', 'Review budget and expense forecasts with Finance; compare maintenance and deployment options using total cost of ownership and operational risk. Confirm responsibilities across sites and partners before proposing changes.'),
        ('By day 90', 'Present a prioritised reliability and efficiency plan with owners, measures and resource needs. Review emergency response readiness with qualified site personnel and capture lessons from incidents and maintenance work.')])
    m.section('HOW I WOULD LEAD')
    for label, body in [
        ('Trust and accountability', 'Make priorities and decision rights clear. Invite concerns early, use 1:1s and GROW coaching to support development, and close the loop on actions raised by the team.'),
        ('Safety before speed', 'Verify that authorised personnel, permits and isolation procedures are in place. Encourage stop-work decisions and review near misses without discouraging reporting.'),
        ('Continuous improvement', 'Use PDCA and A3 to examine recurring issues; review causes and test changes with the technicians doing the work. Track whether improvements hold without introducing new operational risk.'),
        ('Cross-site coordination', 'Work with facilities, finance, engineering and external partners on resource conflicts and deployment dependencies. Maintain a clear owner and next decision for each material risk.')]:
        m.bullet(label, body, after=35)
    m.section('TECHNICAL & DIGITAL CONTEXT')
    m.para('My documented critical operations experience is in wastewater and regulated industrial facilities, not a hyperscale data center. The CV does not establish nine years in critical facilities management, a prior data center Facilities Manager or Chief Engineer role, or management of a mission-critical facilities portfolio. Google’s site-specific standards, generator systems and data center operating procedures would require focused learning with experienced colleagues.', after=80)
    m.para('As an active AI/Claude coder, I build planning and investment models using Python and Claude, including NPV, IRR and scenario sensitivity. At Google, any use would follow company policies and data controls, with outputs reviewed by the responsible technical and financial specialists.', after=80)
    m.section('EFFICIENCY WITH RELIABILITY')
    m.para('Assess energy and resource improvements alongside availability, safety and asset condition. At Novo Nordisk, a PDCA programme reduced energy costs by 40%; for Google, any proposal would need site data, an agreed baseline and review by the accountable engineering team.', after=80)
    m.section('CORE STRENGTHS')
    m.para('Electrical and mechanical systems · critical operations · HVAC · UPS · SCADA · preventive maintenance · people management · safety · LOTO · P&L · budgeting · engineering coordination · PDCA · root-cause analysis · Python · Claude Code', after=70)
    return m.save(path, title='Application and CV — Critical Facilities Manager, Google Fredericia', subject='Critical facilities and data center operations', keywords='critical facilities, facilities management, operations, leadership, electrical, mechanical')

if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Google_CriticalFacilitiesManager.docx')))
