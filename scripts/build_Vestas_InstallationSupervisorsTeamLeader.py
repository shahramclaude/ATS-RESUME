"""Vestas req 80553: combined English motivation, CV and practical 90-day plan."""
import os
from master_design import MasterDoc
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME='SHAHRAM AJLOO'
TITLE='Technical people leadership | Project execution and safety'
CONTACT='+45 93 99 95 14 · ajlooshahram@gmail.com'

def build(path):
 m=MasterDoc(os.path.join(ROOT,'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='en-GB')
 m.header_banner(NAME,TITLE,CONTACT)
 m.meta('Vestas · NCE Onshore CPX · Requisition 80553')
 p=m._p(spacing_after=80,line=260,justify=False);m._run(p,'Team Leader, Installation Supervisors Team 2',bold=True,color='1A1A1A')
 m.para('To the hiring team,',after=60)
 m.para('A supervisor on a construction site needs the authority to make the right call locally and the confidence that support is available when a decision exceeds that authority. For a team spread across projects and countries, the leader’s job is to make that connection dependable: clear expectations, the right people in place, and a reliable route for raising safety and delivery concerns.',after=80)
 m.para('My starting point would be a shared view of project demand, supervisor availability, competence and upcoming decisions. With project and site leaders, I would review resource pressure and changes before they affect delivery; with each supervisor, I would agree objectives, decision boundaries and a regular 1:1. A brief, consistent team check-in and written handovers would make it easier to share learning across locations without taking ownership away from the field.',after=80)
 m.para('The operating discipline comes from experience in technical execution. At Ventek-Air I led 14 people across 11 concurrent projects, using daily meetings and bottleneck analysis to manage capacity. At Novo Nordisk I coordinated 25 specialists across engineering, procurement and construction on 37 technical CAPEX projects, tracking progress, risks and costs. At ELOHVAC I lead five electricians and three apprentices, with responsibility for safety, development, delivery and the business P&L.',after=80)
 m.para('For Vestas, I would pair that experience with the team’s wind-installation expertise. I would work with People & Culture on recruitment and onboarding, use coaching and development plans to support progression, and review safety, quality, cost and delivery with the people closest to the work. Proposed changes would be tested with supervisors and aligned with Vestas procedures before becoming standard practice.',after=80)
 m.para('My documented experience is in technical installations and project execution, rather than wind-turbine installation or direct leadership of an international remote team. I would welcome a discussion about the role’s expectations and the support needed to make that transition. The work base and approximately 40 travel days a year would also need to be agreed.',after=80)
 m.meta('Kind regards',after=15);m.meta('Shahram Ajloo',after=0)
 m.page_break();m.resume_header(NAME,TITLE,CONTACT,'PROFILE')
 m.para('Technical operations and people leader with experience in field-based installations, project coordination, team development and financial accountability. Brings practical electrical and mechanical knowledge together with disciplined planning and a focus on safe, reliable delivery. Danish-authorised marine and technical engineer (maskinmester).',after=70)
 m.section('LEADERSHIP THAT SUPPORTS EXECUTION')
 for a,b in [
 ('People and performance','ELOHVAC: lead five electricians and three apprentices through daily allocation, 1:1s, development discussions, structured training and work-environment follow-up. Situational leadership adapts support and responsibility to the person and task.'),
 ('Resourcing and project delivery','Ventek-Air: led 14 people and managed capacity across 11 concurrent technical projects. Daily meetings and bottleneck analysis supported priorities from specification to handover.'),
 ('Cross-functional coordination','Novo Nordisk: coordinated 25 specialists across engineering, procurement and construction on 37 concurrent CAPEX projects worth DKK 2–10m each. Followed resources, progress, risks and costs; reported to management and client.'),
 ('Safety, quality and improvement','Applied risk assessment, APV and lockout/tagout in technical operations. Novo commissioning used FAT/SAT and IQ/OQ/PQ with zero critical deviations at handover; a PDCA programme reduced energy costs by 40%.'),
 ('Business and digital tools','Full P&L at ELOHVAC; SAP ERP for finance, assets and costs at Novo. Professional AI/Claude coding: Python/Claude API planning and quality tools delivered over 40% productivity improvement at ELOHVAC.')]:m.bullet(a,b,after=25)
 m.models_table('METHODS FOR PEOPLE AND PROJECTS',('Need','Relevant practice'),[
 ('Growth and ownership','1:1, development dialogue, situational leadership, GROW and coaching; clarify expectations and follow up.'),
 ('Capacity and delivery','Daily boards and bottleneck analysis at Ventek-Air; matrix leadership and written priorities across two businesses.'),
 ('Safe execution','Risk assessment, APV and LOTO; support escalation and apply site-specific rules.'),
 ('Improvement','PDCA and A3, with Lean and Six Sigma methods applied in practice; PRINCE2 certified project manager.')])
 m.page_break();m.section('PROFESSIONAL EXPERIENCE')
 jobs=[
 ('Owner / Technical Director / Danish-authorised marine and technical engineer','ELOHVAC ApS · Copenhagen · May 2023–present','5 electricians and 3 apprentices · full P&L',[
 ('People and delivery','Organise work across changing installation sites; conduct 1:1s, development discussions and structured training. Coordinate quotations, materials, subcontractors, quality and handover.'),
 ('Safety and systems','Apply APV, risk assessment and LOTO. Developed Python/Claude API tools for estimating, schedules, quality and KPIs; documented productivity gain over 40%.')]),
 ('Co-owner and CTO / Technical Lead, AI department','Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 · alongside ELOHVAC','4–10 people · company ceased November 2026',[
 ('Teams and priorities','Led the AI and AI-coding department, using a shared plan and written priorities across two concurrent organisations. Used AI for management reporting and decision support.'),
 ('Technical applications','Delivered technical and industrial applications from requirements and integration through commissioning and handover; used AI-assisted development with review and testing.')]),
 ('Senior Commissioning Engineer / Project Manager, electrical systems','Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024','37 simultaneous CAPEX projects · 25 specialists · DKK 2–10m per project',[
 ('Execution and assurance','Coordinated engineering, procurement and construction; monitored time, finance, resources and risk. FAT/SAT and IQ/OQ/PQ with zero critical handover deviations; SAP ERP for finance and assets.')]),
 ('Project and Workshop Manager','Ventek-Air · Copenhagen · Jan 2022–Nov 2022','14 people · 11 simultaneous projects',[
 ('Capacity and handover','Led day-to-day work and coordinated subcontractors, tender documentation and delivery; used daily boards and bottleneck analysis.')]),
 ('Maintenance and Operations Manager / Workshop Technician','BIOFOS, Lynetten · Copenhagen · Aug 2017–Jan 2022','24/7 technical operations · electrical and mechanical systems',[
 ('Maintenance and safety','Preventive maintenance and fault-finding on pumps, HVAC, switchboards and SCADA; LOTO, risk assessment and continuous improvement.')]),
 ('Electromechanical Technician / Production Team Leader','ARJ Engineering · Tehran · Dec 2003–Mar 2010','12 mechanics and technicians',[
 ('Supervision','Led shift and material planning and followed up performance while diagnosing and repairing industrial equipment.')])]
 for title,meta,scope,bullets in jobs:
  m.job(title,meta,scope=scope)
  for a,b in bullets:m.bullet(a,b,after=18)
 m.section('EDUCATION AND CERTIFICATION')
 for a,b in [('B.Tech, Technology Management & Mechanical Engineering','Copenhagen School of Marine and Technical Engineering · maskinmester programme'),('Electrical and mechanical engineering design, electrical engineering','Tehran Technical University'),('Danish authorisation as marine and technical engineer','Danish Safety Technology Authority · LV/MV/HV'),('PRINCE2 certified project manager','AXELOS / PeopleCert'),('STCW safety and engine-room watchkeeping training','Danish Maritime Authority')]:m.edu(a,b)
 m.para('Languages: English (professional); Danish and Persian/Farsi (native). Tools: SAP ERP, Excel, Power BI, Python and Claude API. Lean and Six Sigma methods used in practice; no certification claimed.',after=50)
 m.page_break();m.models_table('FIRST 90 DAYS — PROPOSED START',('When','Action and output'),[
 ('Week 1','Meet the supervisors, project leaders, People & Culture and safety partners. Agree decision rights, communication routes, immediate staffing needs and relevant Vestas procedures.'),
 ('By day 30','Complete individual 1:1s and create a shared view of project assignments, availability, competence and development needs. Agree objectives and escalation routes with the team and manager.'),
 ('By day 60','Review staffing pressures and safety, quality, cost and delivery issues with project leaders. Agree development actions and, with People & Culture, support any recruitment or onboarding needs.'),
 ('By day 90','Review workload, wellbeing, learning and delivery feedback with the team. Test one agreed improvement with supervisors, document the outcome and decide the next steps with management.')])
 m.section('HOW THE LEADERSHIP SYSTEM WORKS')
 for a,b in [
 ('Connection and accountability','Regular 1:1s establish objectives, coaching needs and wellbeing; shared team sessions make room for questions, peer learning and consistent decisions across locations.'),
 ('Resources and change','A capacity and competence overview connects upcoming projects to available supervisors. When plans shift, agree priorities and alternatives with project leaders before reallocating people.'),
 ('Safety, quality, cost and delivery','Review deviations and emerging risks with site and safety stakeholders. Use approved procedures and competent wind specialists for technical decisions; use PDCA to test improvements before standardising.'),
 ('People and Culture','Partner on recruitment, onboarding and development. Define role expectations, assign support and follow up on individual progress; adapt to Vestas processes and local requirements.')]:m.bullet(a,b,after=35)
 m.section('DIGITAL SUPPORT, HUMAN JUDGEMENT')
 m.para('SAP experience is in finance and asset data, not documented Vestas deployment processes. I use Python and Claude for planning, quality and management reporting and build investment models for development and new business ideas. Any use of AI at Vestas would follow company data rules and require human review.',after=70)
 m.section('A CLEAR HANDOVER WHEN PRIORITIES CHANGE')
 m.para('When two sites need the same supervisor, the useful decision is not simply who asks first. I would bring the relevant project leaders together, compare safety, competence, timing and cost, and agree a named owner and next review point. The affected supervisor should receive a clear explanation and have a chance to raise practical concerns.',after=70)
 return m.save(path,title='Application and CV — Vestas Team Leader Installation Supervisors, 80553',subject='People leadership and installation project execution',keywords='team leader, installation, safety, people management, Vestas')

if __name__=='__main__':print(build(os.path.join(ROOT,'Shahram_Ajloo_Vestas_TeamLeader_InstallationSupervisors_80553.docx')))
