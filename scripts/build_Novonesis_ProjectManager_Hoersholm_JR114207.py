# -*- coding: utf-8 -*-
"""Novonesis JR114207 — CV only; employer requests no cover letter or photo."""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Project & Programme Manager · Cross-functional Delivery · Quality & Change'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-US')
    # Page 1 — CV begins immediately; only the short motivation requested by Novonesis.
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.meta('Novonesis · Project Manager for site Hørsholm · JR114207 · Application deadline 22 November 2026')
    m.para('Technical project manager with programme delivery experience across engineering, production and '
           'regulated environments. At Novo Nordisk, coordinated 37 concurrent CAPEX projects '
           'and 25 specialists across engineering, procurement and site teams, tracking scope, objectives, '
           'timelines, budgets, resources, risk and action plans against measurable outcomes. PRINCE2-certified, '
           'with a B.Tech in Technology Management & Mechanical Engineering and experience in cross-functional '
           'stakeholder engagement, change management and monthly management/client reporting. GMP/FDA/EMA '
           'commissioning and qualification supported controlled handovers that help projects **meet regulatory '
           'and quality standards**.', after=38)

    m.section('MOTIVATION FOR NOVONESIS')
    m.para('I am applying because this role turns Novonesis’ purpose to **better our world with biology** '
           'into practical food-safety initiatives and a stronger quality culture across production sites. I '
           'would bring cross-functional programme discipline from regulated manufacturing projects and work '
           'with site specialists to protect **product integrity and customer trust** as changes are '
           'implemented. The commitments **Explore, Impact, Ownership and Care**—with **empowering and growing '
           'people**, **driving performance**, **well-being and engagement**, and **trust and collaborative '
           'learning**—fit the kind of lasting change I want to help deliver.', after=38)

    m.section('SELECTED PROJECT AND PROGRAMME RESULTS')
    for label, body in [
        ('37 concurrent CAPEX projects', 'Novo Nordisk · DKK 2–10m each · coordinated 25 specialists across two sites, tracking project economics, schedule, resources and risk.'),
        ('Zero critical findings at handover', 'GMP-regulated commissioning and qualification of electrical systems; FAT/SAT and IQ/OQ/PQ records completed with engineering and site stakeholders.'),
        ('Facility improvement: 40% lower energy costs', 'Novo Nordisk · structured PDCA programme with measured operational savings.'),
        ('11 parallel installation projects', 'Ventek-Air · 14-person team · tenders, subcontractors, agreements, delivery, safety documentation and handover.'),
        ('40%+ productivity improvement', 'ELOHVAC · Python/Claude API tools for quotations, schedules, quality checklists and KPI follow-up.')]:
        m.bullet(label, body, after=16)

    m.section('PROJECT GOVERNANCE AND CHANGE')
    m.para('PRINCE2-certified in project management · scope, objectives, schedules, budgets and risk follow-up · '
           'monthly management and client reporting · cross-functional stakeholder coordination · team '
           'development through 1:1s, MUS and structured training · Lean and Six Sigma methods used in practice '
           '(not certified) · English: professional working proficiency.', after=28)

    # Page 2 — current and most relevant cross-functional roles.
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFESSIONAL EXPERIENCE')
    m.job('Owner / Technical Director / Authorised Marine Engineer',
          'ELOHVAC ApS · Copenhagen · May 2023–present',
          scope='5 electricians + 3 apprentices · full P&L responsibility')
    for label, body in [
        ('Project delivery and accountability', 'Own customer projects from quotation and planning through procurement, subcontractor coordination, installation, quality checks and handover; accountable for cost and delivery.'),
        ('People and change', 'Lead daily planning, 1:1s, performance and well-being follow-up, MUS discussions and structured apprentice training. Introduce new work routines with the team.'),
        ('Quality and risk', 'Apply LOTO, APV and site risk assessments; maintain service documentation and close out actions. Zero critical deviations in service agreements.'),
        ('Digital improvement', 'Built Python and Claude API tools for quotations, schedules, quality checklists and KPI dashboards; documented productivity improvement above 40%.')]:
        m.bullet(label, body, after=18)

    m.job('Co-owner and CTO / Technical Lead, AI Department',
          'Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 · concurrent with ELOHVAC',
          scope='AI department of 4–10 · company closed November 2026')
    for label, body in [
        ('Cross-functional programme delivery', 'Led client work from requirements and architecture through integration, commissioning, documentation and operational handover for technical and industrial applications.'),
        ('Change and matrix leadership', 'Prioritised work across two concurrent businesses with one shared delivery plan; aligned technical contributors and client operations around milestones and responsibilities.'),
        ('Digital tools and governance', 'Led AI coding projects using LLM APIs and agents, with generation, review and testing standards; used AI-supported workflows for management reports and decision papers.')]:
        m.bullet(label, body, after=18)

    m.job('Senior Commissioning Engineer / Project Manager, Electrical Systems',
          'Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024',
          scope='37 concurrent CAPEX projects · 25 cross-functional specialists · DKK 2–10m per project')
    for label, body in [
        ('Project and portfolio control', 'Coordinated scope, schedules, cost, resources and risks across engineering, procurement and site execution; maintained monthly status reports for management and the client.'),
        ('Quality and implementation', 'Coordinated FAT/SAT and IQ/OQ/PQ for electrical systems, switchboards, controls, UPS, emergency lighting and fire systems in GMP-regulated production projects.'),
        ('Measured improvement', 'Structured PDCA work reduced energy costs by 40%; applied A3, 5 Why and Ishikawa to problem solving. Handover had no critical findings.')]:
        m.bullet(label, body, after=18)

    # Page 3 — additional project, operations and education evidence.
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFESSIONAL EXPERIENCE — CONTINUED')
    m.job('Project and Workshop Manager, Ventilation & HVAC',
          'Ventek-Air · Copenhagen · Jan 2022–Nov 2022',
          scope='14-person team · 11 concurrent projects · DKK 2–10m each')
    for label, body in [
        ('Tendering and contracts', 'Prepared tenders and offers; coordinated subcontractors, agreement basis, safety documentation and handover packages.'),
        ('Delivery and capacity', 'Managed project progress from specification to formal handover. Daily team meetings and bottleneck reviews supported resource allocation and delivery reliability.')]:
        m.bullet(label, body, after=18)

    m.job('Maintenance & Operations Manager / Workshop Technician',
          'Biofos, Lynetten · Copenhagen · Aug 2017–Jan 2022',
          scope='24/7 critical wastewater operations · pumps, HVAC, HV switchgear and SCADA')
    for label, body in [
        ('Operational continuity', 'Planned preventive maintenance and urgent fault response in a live utility environment; applied LOTO, risk assessment, APV and near-miss follow-up.'),
        ('Standard work and improvement', 'Used 5S, Standard Work and PDCA in the workshop and stores; supported spare-parts flow and maintenance routines.')]:
        m.bullet(label, body, after=18)

    m.job('Electromechanic / Production Team Lead',
          'ARJ Engineering · Tehran · Dec 2003–Mar 2010',
          scope='12 mechanics and technicians')
    m.bullet('Team and production', 'Planned shifts and materials, allocated work, and followed troubleshooting and corrective actions for industrial electrical and mechanical equipment.', after=18)

    m.section('EDUCATION AND CERTIFICATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering', 'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · EQF 6')
    m.edu('Electrical and Mechanical Design, Electrical Engineering', 'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('PRINCE2 Certified Project Manager', 'AXELOS / PeopleCert')
    m.edu('Danish electrical authorisation, LV/MV/HV', 'Danish Safety Technology Authority · 2023')
    m.edu('Lean and Six Sigma methods', 'Applied in practice; not certified')

    m.section('LEADERSHIP AND PROJECT METHODS')
    m.para('Project planning and reporting · stakeholder analysis · risk and change follow-up · CAPEX budgeting · '
           'RACI and matrix coordination · 1:1 and MUS · situational leadership · GROW and SBI · PDCA · A3 · '
           '5S · 5 Why · Ishikawa · SAP ERP · Excel / Power Query · Power BI · Python · Claude API.', after=22)
    m.section('LANGUAGES AND LOCATION')
    m.para('Danish and Persian/Farsi: native · English: professional working proficiency · Driving licence B · '
           'Based in Måløv, Denmark; Hørsholm is within commuting distance. Available to work in the office-first '
           'hybrid setup.', after=25)

    return m.save(path, title='CV — Project Manager for site Hørsholm, Novonesis',
                  subject='Project and programme management · quality · change · JR114207',
                  keywords='project manager, programme management, cross-functional, CAPEX, GMP, PRINCE2, Hørsholm')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Novonesis_ProjectManager_Hoersholm_JR114207.docx')
    print(build(out))
