"""Vestas Installation Supervisor, req. 75841 — combined English application and CV."""
import os
from master_design import MasterDoc
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME='SHAHRAM AJLOO'
TITLE='Installation supervision | Electrical safety, quality and delivery'
CONTACT='+45 93 99 95 14 · ajlooshahram@gmail.com'

def build(path):
 m=MasterDoc(os.path.join(ROOT,'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='en-GB')
 m.header_banner(NAME,TITLE,CONTACT);m.meta('Vestas · NCE Installation Supervisors · Requisition 75841')
 p=m._p(spacing_after=80,line=260,justify=False);m._run(p,'Application: Installation Supervisor',bold=True,color='1A1A1A')
 m.para('To the hiring team,',after=50)
 m.para('Before a site team starts work, the supervisor needs a clear picture of the day: the authorised work, people, interfaces, equipment and conditions. When a schedule changes, that picture must change with it. Safe, high-quality installation depends on resolving uncertainty with the people on site before it becomes a delay or an unsafe decision.',after=80)
 m.para('My approach is to start with the approved work instructions and site plan, then confirm responsibilities and readiness with the installation team and site management. I would use a short daily coordination meeting to make tasks, interfaces and changes visible. If conditions differ from the plan, work must be paused and the issue escalated through Vestas’ procedures before it resumes.',after=80)
 m.para('At ELOHVAC, I lead five electricians and three apprentices on changing installation sites, coordinating work, materials, subcontractors, quality and handover. At Ventek-Air, I led 14 people across 11 technical projects and used daily boards and bottleneck analysis to keep delivery on track. At Novo Nordisk, I coordinated 25 specialists across engineering, procurement and construction, with responsibility for following progress, risks and resources on 37 technical CAPEX projects.',after=80)
 m.para('Quality is as important at handover as it is during installation. I would agree the required checks, evidence and open-item ownership with the Vestas quality and commissioning teams, document progress as work proceeds, and keep the customer and site leadership informed of changes. My Novo commissioning work involved FAT/SAT and IQ/OQ/PQ with zero critical deviations at handover; that experience provides a disciplined starting point for learning Vestas’ own standards.',after=80)
 m.para('My technical experience is in electrical and mechanical installations and plant operations, not documented wind-turbine installation. I would learn Vestas’ equipment, site procedures and required authorisations with qualified colleagues before taking on tasks independently. I am based in Denmark; the advertised travel of up to 180 days per year and practical arrangements would need to be agreed.',after=80)
 m.para('I would welcome a conversation about how my site leadership and technical background could support safe execution from preparation through handover to Service.',after=70)
 m.meta('Kind regards',after=15);m.meta('Shahram Ajloo',after=0)
 m.page_break();m.resume_header(NAME,TITLE,CONTACT,'PROFILE')
 m.para('Danish-authorised marine and technical engineer (maskinmester) with practical electrical and mechanical experience and a record of leading technical installation teams. Coordinates people, subcontractors, safety and documentation across changing sites, with a focus on clear communication and reliable handover.',after=70)
 m.section('EXPERIENCE RELEVANT TO SITE DELIVERY')
 for a,b in [
 ('Daily site leadership','ELOHVAC: lead five electricians and three apprentices, plan work on changing sites, coordinate subcontractors and materials, and follow up on quality, safety and delivery.'),
 ('Electrical and mechanical foundation','Electrical installations, switchboards, controls and fault-finding at ELOHVAC and Novo Nordisk; pumps, HVAC, high-voltage switchboards and SCADA maintenance at BIOFOS.'),
 ('Safety and risk','Apply lockout/tagout (LOTO), risk assessments and APV during technical work and site start-up; follow up on work environment and near misses.'),
 ('Quality and handover','Novo: FAT/SAT and IQ/OQ/PQ in regulated technical projects, with zero critical deviations at handover. Ventek-Air: safety and handover documentation across 11 technical projects.'),
 ('Coordination and customer dialogue','Novo: coordinated 25 specialists across engineering, procurement and construction on 37 concurrent CAPEX projects; reported progress, risk and finances to management and client.'),
 ('Digital tools and improvement','SAP ERP for finance and assets at Novo; Excel and Power BI. Python/Claude tools for schedules, quality checklists and KPIs at ELOHVAC delivered a documented productivity gain over 40%.')]:m.bullet(a,b,after=25)
 m.models_table('WORKING METHODS',('Site need','Practical approach'),[
 ('Safe start','Risk assessment, APV and LOTO in technical work; apply the site-specific permit and procedures required for each task.'),
 ('Daily control','Daily boards and bottleneck analysis at Ventek-Air; proposed brief coordination and clear escalation on site.'),
 ('Team development','Situational leadership, 1:1 and structured training at ELOHVAC; involve experienced specialists in site learning.'),
 ('Quality and learning','FAT/SAT and structured handover at Novo; PDCA and A3 for improvement, with PRINCE2 project-management certification.')])
 m.page_break();m.section('PROFESSIONAL EXPERIENCE')
 jobs=[
 ('Owner / Technical Director / Danish-authorised marine and technical engineer','ELOHVAC ApS · Copenhagen · May 2023–present','5 electricians and 3 apprentices · full P&L',[
 ('Installation and supervision','Lead daily planning, technical work, materials and subcontractors; manage quality and handover for electrical, ventilation and climate installations.'),
 ('People and safety','Provide 1:1s and structured training; use risk assessments, APV and LOTO. Developed Python/Claude planning and quality tools with over 40% documented productivity gain.')]),
 ('Co-owner and CTO / Technical Lead, AI department','Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 · alongside ELOHVAC','4–10 people · company ceased November 2026',[
 ('Implementation','Led technical and industrial applications from requirements and integration to commissioning, documentation and handover; managed priorities across two parallel businesses.'),
 ('Digital practice','Used AI-assisted development with review and testing; applied AI to decision support and management reporting.')]),
 ('Senior Commissioning Engineer / Project Manager, electrical systems','Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024','37 concurrent CAPEX projects · 25 specialists · DKK 2–10m each',[
 ('Coordination and quality','Followed progress, risks, resources and costs across engineering, procurement and construction; FAT/SAT and IQ/OQ/PQ with zero critical deviations at handover. SAP for finance and assets.')]),
 ('Project and Workshop Manager','Ventek-Air · Copenhagen · Jan 2022–Nov 2022','14 people · 11 concurrent technical projects',[
 ('Execution and documentation','Managed capacity, subcontractors and safety documentation from specification to handover; used daily boards and bottleneck analysis.')]),
 ('Maintenance and Operations Manager / Workshop Technician','BIOFOS, Lynetten · Copenhagen · Aug 2017–Jan 2022','24/7 operations · electrical and mechanical plant',[
 ('Plant and safety','Preventive maintenance and fault-finding on pumps, HVAC, high-voltage switchboards and SCADA; LOTO, risk assessment and near-miss follow-up.')]),
 ('Electromechanical Technician / Production Team Leader','ARJ Engineering · Tehran · Dec 2003–Mar 2010','12 mechanics and technicians · machine workshop',[
 ('Technical team','Led shift and material planning and diagnosed and repaired industrial electrical and mechanical equipment.')])]
 for title,meta,scope,bullets in jobs:
  m.job(title,meta,scope=scope)
  for a,b in bullets:m.bullet(a,b,after=15)
 m.section('EDUCATION AND CERTIFICATION')
 for a,b in [('B.Tech, Technology Management & Mechanical Engineering','Copenhagen School of Marine and Technical Engineering · maskinmester programme'),('Electrical and mechanical engineering design, electrical engineering','Tehran Technical University'),('Danish authorisation as marine and technical engineer','Danish Safety Technology Authority · LV/MV/HV'),('PRINCE2 certified project manager','AXELOS / PeopleCert'),('STCW safety and engine-room watchkeeping training','Danish Maritime Authority')]:m.edu(a,b)
 m.para('Languages: English (professional); Danish and Persian/Farsi (native). Tools: SAP ERP, Excel, Power BI, Python and Claude API.',after=40)
 m.page_break();m.models_table('FIRST 90 DAYS — PROPOSED START',('When','Site focus and deliverables'),[
 ('Week 1','Meet site management, experienced supervisors, HSE and quality colleagues. Complete required induction and identify role limits, site risks, reporting routes and Vestas’ approved instructions.'),
 ('By day 30','Follow an experienced supervisor through planning, daily coordination and quality checks. Map site interfaces, required training and the documentation needed for progress and handover.'),
 ('By day 60','Coordinate assigned activities within agreed competence and authority. Review schedule changes, open issues and quality evidence with the responsible site and project leads.'),
 ('By day 90','Review safety, delivery and learning with site management and the team. Agree remaining training and one practical improvement; confirm requirements for handover to Service.')])
 m.section('THE SITE DAY: FOUR POINTS OF CONTROL')
 for a,b in [
 ('Before work','Check the plan, approved instructions, competence, site conditions and interfaces with the responsible team. Escalate uncertainty before work begins; follow Vestas HSE rules and authorisation requirements.'),
 ('During execution','Stay close to the installation team, listen to concerns and share changes. If conditions or scope change, pause and seek the responsible decision before work resumes.'),
 ('Progress and quality','Compare actual progress with the agreed schedule. Record issues and evidence in approved systems, and coordinate quality checks with the people responsible rather than assuming sign-off authority.'),
 ('Customer and handover','Keep site leadership and the customer informed through agreed channels. Confirm open items, documentation and ownership with commissioning and Service before handover.')]:m.bullet(a,b,after=30)
 m.section('TECHNOLOGY THAT SUPPORTS THE TEAM')
 m.para('I work with SAP ERP for financial and asset data and build Python/Claude tools for planning and quality; I also develop investment models for new business ideas. Specific SharePoint, Outlook and Vestas SAP workflow proficiency is not documented and would be assessed during onboarding. AI and site data must follow Vestas rules and remain subject to human review.',after=70)
 m.section('TECHNICAL DEVELOPMENT')
 m.para('My foundation is electrical and mechanical installation and plant operations. Turbine-specific installation, lifting, work at height and Vestas-specific qualifications are not documented in my experience. Site tasks and authorisations must match verified competence and completed training.',after=65)
 return m.save(path,title='Application and CV — Vestas Installation Supervisor, 75841',subject='On-site installation, safety and quality',keywords='installation supervisor, safety, quality, Vestas')

if __name__=='__main__':print(build(os.path.join(ROOT,'Shahram_Ajloo_Vestas_InstallationSupervisor_75841.docx')))
