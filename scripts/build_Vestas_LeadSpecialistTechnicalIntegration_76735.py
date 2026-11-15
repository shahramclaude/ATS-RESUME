"""Vestas DfM and manufacturing readiness — application and CV, req. 76735."""
import os
from master_design import MasterDoc
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME='SHAHRAM AJLOO'
TITLE='Technical integration | Quality, industrial systems and improvement'
CONTACT='+45 93 99 95 14 · ajlooshahram@gmail.com'

def build(path):
 m=MasterDoc(os.path.join(ROOT,'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='en-GB')
 m.header_banner(NAME,TITLE,CONTACT);m.meta('Vestas · Blades PE Technical Integration · Requisition 76735')
 p=m._p(spacing_after=80,line=260,justify=False);m._run(p,'Application: Lead Specialist — Technical Integration',bold=True,color='1A1A1A')
 m.para('To the hiring team,',after=50)
 m.para('A blade design is ready for production only when its manufacturing assumptions have been tested with the people and processes that must deliver it repeatedly. The link between product development and the factory needs clear requirements, evidence at each decision point and a practical route for resolving risks before ramp-up.',after=80)
 m.para('I would begin by learning how the layup, infusion, bonding, handling and finishing teams define readiness, and how design, quality and operations make decisions together. Working with the responsible manufacturing specialists, I would map the critical requirements and open issues to project milestones, identify the evidence needed for each review, and make ownership and unresolved decisions visible.',after=80)
 m.para('My contribution would draw on technical implementation and structured problem solving. At Novo Nordisk I coordinated 25 specialists across engineering, procurement and construction on 37 technical CAPEX projects, following risk, resources and progress through commissioning. FAT/SAT and IQ/OQ/PQ concluded without critical deviations at handover; a PDCA programme reduced energy costs by 40%. At Data Power, I led technical application delivery from requirements through integration, commissioning and documented handover.',after=80)
 m.para('For improvement work, I would use PDCA, A3 and the risk-analysis methods I have applied in practice to structure problems with the team, while deferring manufacturing readiness evaluations and technical approval to the appropriately qualified Vestas specialists. Where data is available, a shared view of process risks, evidence and actions can help the programme distinguish an assumption from a verified production requirement.',after=80)
 m.para('This is a substantial specialist transition: my documented background is in electrical systems, technical projects and industrial applications, not blade manufacturing, DfM leadership, production ramp-ups or manufacturing readiness assessments. Experience with MRL, APQP, PFMEA, control plans, MSA and statistical process control is not documented. I would welcome an honest discussion about whether my background could contribute to this work or to a different technical integration role.',after=80)
 m.para('The Lem work location and up to 80 travel days per year would also need to be agreed. I would be pleased to discuss the technical scope and the competencies Vestas needs from day one.',after=70)
 m.meta('Kind regards',after=15);m.meta('Shahram Ajloo',after=0)
 m.page_break();m.resume_header(NAME,TITLE,CONTACT,'TECHNICAL PROFILE')
 m.para('Danish-authorised marine and technical engineer (maskinmester) with experience in technical implementation, commissioning, industrial applications and structured improvement. Combines electrical and mechanical understanding with cross-functional coordination, project controls and practical quality documentation.',after=70)
 m.section('EVIDENCE FOR TECHNICAL INTEGRATION')
 for a,b in [
 ('Cross-functional delivery','Novo Nordisk: coordinated 25 specialists in engineering, procurement and construction across 37 concurrent technical CAPEX projects. Followed resources, risk, cost and progress and reported to management and client.'),
 ('Technical verification','Novo: FAT/SAT and IQ/OQ/PQ in regulated electrical projects; zero critical deviations at handover. This is equipment commissioning experience, not documented product industrialization.'),
 ('Implementation and design support','Data Power: led technical and industrial applications from requirements and integration to commissioning and handover; used AI-assisted calculations and design variants with professional validation.'),
 ('Improvement in operation','Novo PDCA programme reduced energy costs by 40%. BIOFOS used 5S, Standard Work and PDCA in workshop and stores; ARJ involved mechanical/electrical equipment repair and production-team leadership.'),
 ('Digital analysis','Professional Python and Claude coding for estimates, schedules, quality and KPIs at ELOHVAC: over 40% documented productivity improvement. Develops investment models using NPV, IRR and scenarios.')]:m.bullet(a,b,after=25)
 m.models_table('METHODS AND EVIDENCE',('Purpose','Documented practice'),[
 ('Problem solving','PDCA, A3, 5 x why and Ishikawa at Novo; Lean and Six Sigma methods applied in practice, not certified.'),
 ('Risk and coordination','Risk follow-up across Novo CAPEX projects; FMEA in the documented methods bank, without a claimed PFMEA deliverable.'),
 ('Technical handover','FAT/SAT and qualification at Novo; requirements, integration and documented handover at Data Power.'),
 ('Organisation and delivery','PRINCE2 certified project manager; planning and shared priorities across technical teams.')])
 m.section('SPECIALIST SCOPE')
 m.para('Experience in blade process engineering, NPI ramp-up or DfM/MRL ownership is not documented. The role’s specialised manufacturing methods require assessment and development with qualified specialists.',after=60)
 m.page_break();m.section('PROFESSIONAL EXPERIENCE')
 jobs=[
 ('Owner / Technical Director / Danish-authorised marine and technical engineer','ELOHVAC ApS · Copenhagen · May 2023–present','5 electricians and 3 apprentices · full P&L',[
 ('Technical delivery','Manage electrical, ventilation and climate installations, coordinating planning, subcontractors, quality and handover.'),
 ('Digital improvement','Developed Python/Claude API tools for estimating, schedules, quality checklists and KPIs, with over 40% documented productivity improvement.')]),
 ('Co-owner and CTO / Technical Lead, AI department','Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 · alongside ELOHVAC','4–10 people · company ceased November 2026',[
 ('Industrial applications','Led customer requirements, architecture, system integration and commissioning through documentation and operational handover.'),
 ('AI-assisted design','Used AI coding for calculations, sizing and design variants for technical systems and industrial components, with professional validation of outputs.')]),
 ('Senior Commissioning Engineer / Project Manager, electrical systems','Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024','37 concurrent CAPEX projects · 25 specialists · DKK 2–10m each',[
 ('Quality and coordination','Followed risks, progress, resources and cost across engineering, procurement and construction. FAT/SAT and IQ/OQ/PQ with zero critical handover deviations.'),
 ('Improvement','PDCA programme reduced energy costs by 40%; used A3 and root-cause methods and SAP ERP for finance and assets.')]),
 ('Project and Workshop Manager','Ventek-Air · Copenhagen · Jan 2022–Nov 2022','14 people · 11 concurrent technical projects',[
 ('Project execution','Managed capacity, subcontractors and documentation from specification to handover; daily boards and bottleneck analysis supported delivery.')]),
 ('Maintenance and Operations Manager / Workshop Technician','BIOFOS, Lynetten · Copenhagen · Aug 2017–Jan 2022','24/7 operations · electrical and mechanical plant',[
 ('Equipment and improvement','Preventive maintenance, fault-finding and spare-parts flow; 5S, Standard Work, PDCA, LOTO and risk assessment.')]),
 ('Electromechanical Technician / Production Team Leader','ARJ Engineering · Tehran · Dec 2003–Mar 2010','12 mechanics and technicians · machine workshop',[
 ('Workshop','Led shift and material planning and diagnosed and repaired industrial electrical and mechanical equipment.')])]
 for title,meta,scope,bullets in jobs:
  m.job(title,meta,scope=scope)
  for a,b in bullets:m.bullet(a,b,after=15)
 m.section('EDUCATION AND CERTIFICATION')
 for a,b in [('B.Tech, Technology Management & Mechanical Engineering','Copenhagen School of Marine and Technical Engineering · maskinmester programme'),('Electrical and mechanical engineering design, electrical engineering','Tehran Technical University'),('Danish authorisation as marine and technical engineer','Danish Safety Technology Authority · LV/MV/HV'),('PRINCE2 certified project manager','AXELOS / PeopleCert')]:m.edu(a,b)
 m.para('Languages: English (professional); Danish and Persian/Farsi (native). Tools: SAP ERP, Excel, Power BI, Python and Claude API.',after=40)
 m.page_break();m.models_table('FIRST 90 DAYS — PROPOSED LEARNING AND CONTRIBUTION',('When','Actions and outputs'),[
 ('Week 1','Meet manufacturing, quality and development specialists; agree responsibilities and technical decision rights. Learn the blade process flow, safety rules and current programme priorities.'),
 ('By day 30','Map the interfaces between product requirements, process teams and programme milestones. Identify required evidence, open questions and personal training needs with the specialist lead.'),
 ('By day 60','Support an agreed review or improvement with the responsible process experts. Make risks, owners, assumptions and evidence visible; seek technical review before recommendations proceed.'),
 ('By day 90','Evaluate the contribution with the manager and specialists, document lessons and agree the next development priorities. Any readiness gate or manufacturing decision remains with authorised experts.')])
 m.section('FROM DESIGN INTENT TO EVIDENCE')
 for a,b in [
 ('Manufacturing requirements','With product development and process engineers, clarify what must be demonstrated in production and who owns each requirement; avoid assuming that a design is scalable without evidence.'),
 ('Readiness and risk','Support review of manufacturing readiness and technical risks using Vestas’ established frameworks. MRL, APQP, PFMEA and control-plan work requires specialist training and review.'),
 ('Measurement and quality','Work with quality specialists to understand metrology, Measurement System Analysis (MSA), statistical process control and process capability before using them in technical decisions.'),
 ('Implementation','Agree actions and evidence with Operations, Manufacturing Engineering, Quality and Supply Chain; use PDCA and structured follow-up to test improvements in the approved process.')]:m.bullet(a,b,after=30)
 m.section('DIGITAL SUPPORT WITH ENGINEERING REVIEW')
 m.para('I use Python and Claude for technical applications, design calculations and management reporting, and build investment models for development and new business ideas. At Vestas, data access, validation and any AI-assisted work would follow company rules; qualified engineers retain responsibility for technical conclusions.',after=70)
 m.section('SPECIALIST REQUIREMENTS')
 m.para('My experience with Lean, Six Sigma and general FMEA does not establish expertise in blade manufacturing, PFMEA, product launches or production ramp-ups. A lead specialist must bring deep manufacturing competence; the fit and any additional experience would need to be assessed before assigning technical ownership.',after=60)
 return m.save(path,title='Application and CV — Vestas Lead Specialist Technical Integration 76735',subject='Technical integration and manufacturing readiness',keywords='technical integration, manufacturing readiness, Vestas')

if __name__=='__main__':print(build(os.path.join(ROOT,'Shahram_Ajloo_Vestas_LeadSpecialist_TechnicalIntegration_76735.docx')))
