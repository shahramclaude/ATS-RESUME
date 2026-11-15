"""Vestas Global Repair & Lifecycle: combined application and CV, req. 78832."""
import os
from master_design import MasterDoc
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME='SHAHRAM AJLOO'
TITLE='Project management | Technical operations, implementation and value'
CONTACT='+45 93 99 95 14 · ajlooshahram@gmail.com'

def build(path):
 m=MasterDoc(os.path.join(ROOT,'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='en-GB')
 m.header_banner(NAME,TITLE,CONTACT);m.meta('Vestas · Global Repair & Lifecycle · Requisition 78832')
 p=m._p(spacing_after=80,line=260,justify=False);m._run(p,'Project Manager — turning repair initiatives into operational value',bold=True,color='1A1A1A')
 m.para('To the hiring team,',after=50)
 m.para('A repair improvement creates value only when it works in the operation that inherits it. For Global Repair & Lifecycle, that means connecting the business case to a realistic delivery plan, involving the people who will use the outcome, and checking whether the expected benefits actually materialise after handover.',after=80)
 m.para('I would start each initiative by agreeing the problem, scope, decision owner and success measures with the sponsor and operational stakeholders. A concise charter and business case would bring costs, assumptions, risks and dependencies into one place; a plan with named owners and decision points would keep the work aligned as conditions change. At each review, I would present the decision required, the options and their implications rather than simply report activity.',after=80)
 m.para('That approach draws on my work at Novo Nordisk, where I coordinated 25 specialists across engineering, procurement and construction on 37 concurrent technical CAPEX projects. I followed progress, resources, risks and costs, and reported to management and the client. At Ventek-Air, I managed capacity across 11 projects and led 14 people from specification through delivery. At Data Power, technical applications progressed from requirements and integration through commissioning, documentation and handover.',after=80)
 m.para('For Vestas, I would map the handover with the repair and operations teams before implementation: who owns the new process, what training or documentation is needed, and which baseline and measures will show whether it is useful. PRINCE2 governance, stakeholder mapping and a live risk and dependency log provide the structure; PDCA and post-implementation review make the learning usable on the next project.',after=80)
 m.para('My experience is in technical operations, electrical projects and industrial applications rather than wind-turbine component repair. I would build the business case with Vestas’ repair and sustainability specialists, using their technical assumptions rather than treating them as my own. The office location in Jutland and approximately 30 travel days per year would need to be agreed.',after=80)
 m.para('I would welcome a discussion about the projects where disciplined implementation and operational follow-through could most help the team.',after=70)
 m.meta('Kind regards',after=15);m.meta('Shahram Ajloo',after=0)
 m.page_break();m.resume_header(NAME,TITLE,CONTACT,'PROJECT PROFILE')
 m.para('PRINCE2-certified project manager and Danish-authorised marine and technical engineer with experience coordinating technical CAPEX, operations and industrial applications. Brings project controls, stakeholder coordination and hands-on understanding of maintenance and handover to initiatives that need to work beyond completion.',after=70)
 m.section('EXPERIENCE ALIGNED TO THE ROLE')
 for a,b in [
 ('Project control and governance','At Novo Nordisk, followed progress, cost, risks and resources across 37 simultaneous projects worth DKK 2–10m each. Coordinated 25 specialists and reported to management and the client.'),
 ('Cross-functional implementation','Coordinated engineering, procurement and construction; at Data Power, brought technical applications from requirements and integration to commissioning, documentation and operational handover.'),
 ('Operational context','BIOFOS: maintenance and fault-finding in a 24/7 plant, including pumps, HVAC, switchboards and SCADA. Workshop and spare-parts experience supports practical conversations about maintainability and repair.'),
 ('Business and analysis','Full P&L in ELOHVAC; develops investment models using NPV, IRR and scenarios. SAP ERP at Novo for finance, assets and costs; Excel and Power BI in the digital toolkit.'),
 ('Results and improvement','Novo PDCA programme reduced energy costs by 40%; commissioning completed with zero critical deviations at handover. ELOHVAC’s Python/Claude tools for planning, quality and KPIs delivered over 40% productivity improvement.')]:m.bullet(a,b,after=25)
 m.models_table('PROJECT METHODS AND APPLICATION',('Discipline','Approach'),[
 ('Initiation and decisions','PRINCE2 certification; proposed charter, business case, stakeholder map and decision log suited to project scale.'),
 ('Execution and risk','Project planning, risk and resource follow-up at Novo; RACI and dependency tracking to clarify ownership.'),
 ('Handover and benefits','Documented commissioning and handover at Novo and Data Power; proposed baseline, benefit owner and post-implementation review.'),
 ('Improvement','PDCA and A3 in Novo projects; Lean and Six Sigma applied in practice, not claimed as certifications.')])
 m.page_break();m.section('PROFESSIONAL EXPERIENCE')
 jobs=[
 ('Owner / Technical Director / Danish-authorised marine and technical engineer','ELOHVAC ApS · Copenhagen · May 2023–present','5 electricians and 3 apprentices · full P&L',[
 ('Projects and economics','Manage quotations, planning, materials, subcontractors, quality and handover for electrical, ventilation and climate installations; lead personnel and oversee business performance.'),
 ('Digital improvement','Developed Python/Claude API tools for estimates, schedules, quality checklists and KPIs; documented productivity gain over 40%.')]),
 ('Co-owner and CTO / Technical Lead, AI department','Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 · alongside ELOHVAC','4–10 people · company ceased November 2026',[
 ('Delivery and handover','Led industrial and technical application delivery from requirements and architecture to integration, commissioning, documentation and handover.'),
 ('Decision support','Applied AI to management reports and decision material; used written priorities and a combined plan across the two businesses.')]),
 ('Senior Commissioning Engineer / Project Manager, electrical systems','Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024','37 concurrent CAPEX projects · 25 specialists · DKK 2–10m each',[
 ('Coordination and control','Followed progress, cost, risk and resources across engineering, procurement and construction; monthly management and client reporting. SAP ERP for finance, assets and costs.'),
 ('Quality and improvement','FAT/SAT and IQ/OQ/PQ in regulated projects with zero critical deviations at handover; PDCA programme reduced energy costs by 40%.')]),
 ('Project and Workshop Manager','Ventek-Air · Copenhagen · Jan 2022–Nov 2022','14 people · 11 concurrent technical projects',[
 ('Planning and execution','Managed capacity, subcontractors and documentation from specification to handover. Daily boards and bottleneck analysis supported delivery.')]),
 ('Maintenance and Operations Manager / Workshop Technician','BIOFOS, Lynetten · Copenhagen · Aug 2017–Jan 2022','24/7 operations · electrical and mechanical plant',[
 ('Maintenance and reliability','Preventive maintenance, fault-finding and spare-parts flow; 5S, Standard Work and PDCA with LOTO and risk assessment.')]),
 ('Electromechanical Technician / Production Team Leader','ARJ Engineering · Tehran · Dec 2003–Mar 2010','12 mechanics and technicians · machine workshop',[
 ('Repair and team coordination','Led shift and material planning and diagnosed and repaired industrial electrical and mechanical equipment.')])]
 for title,meta,scope,bullets in jobs:
  m.job(title,meta,scope=scope)
  for a,b in bullets:m.bullet(a,b,after=15)
 m.section('EDUCATION AND CERTIFICATION')
 for a,b in [('B.Tech, Technology Management & Mechanical Engineering','Copenhagen School of Marine and Technical Engineering · maskinmester programme'),('Electrical and mechanical engineering design, electrical engineering','Tehran Technical University'),('Danish authorisation as marine and technical engineer','Danish Safety Technology Authority · LV/MV/HV'),('PRINCE2 certified project manager','AXELOS / PeopleCert')]:m.edu(a,b)
 m.para('Languages: English (professional); Danish and Persian/Farsi (native). Digital tools: SAP ERP, Excel, Power BI, Python and Claude API.',after=40)
 m.page_break();m.models_table('FIRST 90 DAYS — PROPOSED START',('Time','Decisions and deliverables'),[
 ('Week 1','Meet the manager, repair operations, engineering and sustainability stakeholders. Understand current projects, governance, decision rights and handover expectations.'),
 ('By day 30','Map project stakeholders, objectives, scope, available baseline data, dependencies and risks. Agree priorities and the format of a charter and decision-ready status report with the sponsor.'),
 ('By day 60','Develop or refine a business case and plan with subject matter experts. Confirm assumptions, costs, responsibilities and milestones; identify operational owner, training needs and benefit measures.'),
 ('By day 90','Review progress and a proposed handover and benefits plan with sponsor and operational team. Record decisions, lessons and next steps; agree who will measure outcomes after implementation.')])
 m.section('FROM A REPAIR IDEA TO A RESULT THE OPERATION CAN USE')
 for a,b in [
 ('Define the opportunity','Work with repair and lifecycle specialists to establish the problem, boundaries and available baseline. Assess service and circularity implications using agreed data; do not assume a particular saving.'),
 ('Build the case','Use cost, timing, resource and scenario assumptions supplied by the relevant functions. Present options and uncertainties to the sponsor with a recommendation and decision request.'),
 ('Deliver through others','Maintain a project plan, risk and dependency log, and clear ownership. Use stakeholder reviews to resolve changes before they become unmanaged impacts on scope, budget or schedule.'),
 ('Transfer and verify','Agree acceptance criteria, documentation, operational ownership and measures before handover. Review actual outcomes against the baseline with the benefit owner and use PDCA to capture learning.')]:m.bullet(a,b,after=30)
 m.section('DIGITAL SUPPORT FOR BETTER DECISIONS')
 m.para('I build Python and Claude tools for planning, quality and management reporting, and investment models for development and new business ideas. For Vestas, an agreed business case and benefits dashboard could make assumptions and changes visible. Any use of AI or company data must follow Vestas rules and be reviewed by accountable people.',after=70)
 m.section('PROJECTS IN A REPAIR AND CIRCULARITY CONTEXT')
 m.para('My documented repair experience is industrial electrical and mechanical equipment, not wind-turbine components. I would therefore rely on Vestas specialists for repair methods, performance assumptions and sustainability data, while bringing disciplined project leadership and operational handover to the work.',after=65)
 return m.save(path,title='Application and CV — Vestas Project Manager, 78832',subject='Project management, repair lifecycle and operational value',keywords='project manager, PRINCE2, lifecycle, Vestas')

if __name__=='__main__':print(build(os.path.join(ROOT,'Shahram_Ajloo_Vestas_ProjectManager_RepairLifecycle_78832.docx')))
