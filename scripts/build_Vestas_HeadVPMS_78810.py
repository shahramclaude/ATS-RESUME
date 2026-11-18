"""Vestas Head of VPMS, req. 78810 — application, CV and 90-day proposal."""
import os
from master_design import MasterDoc
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME='SHAHRAM AJLOO'
TITLE='Technical operations | Continuous improvement and leadership'
CONTACT='+45 93 99 95 14 · ajlooshahram@gmail.com'

def build(path):
 m=MasterDoc(os.path.join(ROOT,'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='en-GB')
 m.header_banner(NAME,TITLE,CONTACT);m.meta('Vestas · Global Manufacturing · Requisition 78810')
 p=m._p(spacing_after=80,line=260,justify=False);m._run(p,'Application: Head of Vestas Production Management System',bold=True,color='1A1A1A')
 m.para('To the hiring team,',after=50)
 m.para('A production system earns its place when the people running the work use it to make better decisions every day. Across different factories, the challenge is to establish shared standards and clear measures without losing the local knowledge needed to make those standards work.',after=80)
 m.para('My first step would be to understand the existing VPMS with plant and functional leaders: which routines help teams manage safety, quality, delivery, cost and productivity, and where implementation is difficult. Together we could establish a baseline, agree the few gaps that matter most and identify the support sites need before proposing changes.',after=80)
 m.para('A useful deployment rhythm would connect strategy to site priorities, a named owner and a practical review on the shop floor. Maturity assessments and audits should identify evidence and support gap closure, not become an exercise in scoring. I would use PDCA and A3 to structure problems, standard work to make improvements repeatable, and coaching to help leaders develop their own teams.',after=80)
 m.para('That approach builds on documented technical and operational work. At Novo Nordisk, I coordinated 25 specialists across engineering, procurement and construction on 37 CAPEX projects; a PDCA programme reduced energy costs by 40%. At BIOFOS I applied 5S, Standard Work and PDCA in workshop and stores. At Ventek-Air I led 14 people across 11 projects, using daily boards and bottleneck analysis to manage capacity and delivery.',after=80)
 m.para('The scope of this position is substantially broader than my documented experience. My CV does not establish 15 years of leadership in global manufacturing, ownership of a production system across multiple plants, or a large-scale international manufacturing transformation. I would welcome an open discussion about whether my technical leadership and improvement background could be relevant to Vestas, including in a role with a different scope.',after=80)
 m.para('Aarhus, Taranto and Szczecin are listed as possible bases. I live in Måløv, Denmark; the work location and practical arrangements would need to be agreed. I would be pleased to discuss the priorities and leadership experience Vestas needs for this mandate.',after=70)
 m.meta('Kind regards',after=15);m.meta('Shahram Ajloo',after=0)
 m.page_break();m.resume_header(NAME,TITLE,CONTACT,'LEADERSHIP PROFILE')
 m.para('Danish-authorised marine and technical engineer (maskinmester) and technical operations leader with experience in team development, project delivery and structured improvement. Brings hands-on industrial and maintenance experience together with P&L, safety and cross-functional coordination.',after=70)
 m.section('EXPERIENCE RELEVANT TO OPERATIONAL EXCELLENCE')
 for a,b in [
 ('Daily management and people','At Ventek-Air, led 14 people across 11 technical projects; daily boards and bottleneck analysis supported capacity and delivery. At ELOHVAC, lead five electricians and three apprentices with 1:1s, training and work-environment follow-up.'),
 ('Improvement with evidence','At Novo Nordisk, a PDCA programme reduced energy costs by 40%. At BIOFOS, applied 5S, Standard Work and PDCA in workshop and stores; at ARJ led a 12-person workshop team.'),
 ('Cross-functional execution','At Novo, coordinated 25 specialists across engineering, procurement and construction on 37 concurrent CAPEX projects, tracking resources, risk, progress and cost and reporting to management and client.'),
 ('Safety and quality','Applied APV, risk assessment and LOTO in technical operations. Novo commissioning included FAT/SAT and IQ/OQ/PQ, with zero critical deviations at handover.'),
 ('Business and digital capability','Full P&L at ELOHVAC. Python/Claude tools for estimating, schedules, quality and KPIs produced a documented productivity gain over 40%; also builds investment models for development and new business ideas.')]:m.bullet(a,b,after=25)
 m.models_table('IMPROVEMENT METHODS IN PRACTICE',('Purpose','Relevant experience'),[
 ('Daily flow','Daily boards and bottleneck analysis at Ventek-Air; 5S and Standard Work at BIOFOS.'),
 ('Problem solving','PDCA, A3, 5 x why and Ishikawa at Novo. Lean and Six Sigma methods used in practice; certification not claimed.'),
 ('People development','Situational leadership, 1:1 and structured training at ELOHVAC; GROW coaching as a leadership tool.'),
 ('Planning and controls','PRINCE2 certified project manager; project controls and cross-functional coordination at Novo.')])
 m.section('SCOPE OF EXPERIENCE')
 m.para('Production-team leadership and local improvement experience are documented; multi-plant production-system deployment and global manufacturing transformation leadership are not.',after=60)
 m.page_break();m.section('PROFESSIONAL EXPERIENCE')
 jobs=[
 ('Owner / Technical Director / Danish-authorised marine and technical engineer','ELOHVAC ApS · Copenhagen · May 2023–present','5 electricians and 3 apprentices · full P&L',[
 ('Operations and people','Lead planning, personnel, subcontractors, quality and handover for electrical, ventilation and climate installations; use 1:1s and structured training.'),
 ('Digital improvement','Developed Python/Claude API tools for estimates, schedules, quality and KPIs with over 40% documented productivity improvement.')]),
 ('Co-owner and CTO / Technical Lead, AI department','Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 · alongside ELOHVAC','4–10 people · company ceased November 2026',[
 ('Implementation','Led technical and industrial applications from requirements and system integration to commissioning, documentation and handover.'),
 ('Planning and decision support','Used AI-assisted reporting and written priorities across two concurrent businesses; set standards for review and testing of AI-assisted software.')]),
 ('Senior Commissioning Engineer / Project Manager, electrical systems','Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024','37 concurrent CAPEX projects · 25 specialists · DKK 2–10m each',[
 ('Cross-functional coordination','Followed progress, cost, risk and resources across engineering, procurement and construction; FAT/SAT and IQ/OQ/PQ with zero critical deviations at handover.'),
 ('Improvement','Applied PDCA, A3 and root-cause analysis; a PDCA programme reduced energy costs by 40%. SAP ERP for finance and assets.')]),
 ('Project and Workshop Manager','Ventek-Air · Copenhagen · Jan 2022–Nov 2022','14 people · 11 concurrent technical projects',[
 ('Capacity and delivery','Led day-to-day planning, subcontractors and documentation from specification to handover; daily boards and bottleneck analysis supported delivery.')]),
 ('Maintenance and Operations Manager / Workshop Technician','BIOFOS, Lynetten · Copenhagen · Aug 2017–Jan 2022','24/7 operations · electrical and mechanical plant',[
 ('Standard work and safety','Preventive maintenance and fault-finding, spare-parts flow, 5S and Standard Work in workshop and stores; LOTO and risk assessment.')]),
 ('Electromechanical Technician / Production Team Leader','ARJ Engineering · Tehran · Dec 2003–Mar 2010','12 mechanics and technicians · machine workshop',[
 ('People and workshop','Led shifts, material planning and performance follow-up while diagnosing and repairing industrial electrical and mechanical equipment.')])]
 for title,meta,scope,bullets in jobs:
  m.job(title,meta,scope=scope)
  for a,b in bullets:m.bullet(a,b,after=15)
 m.section('EDUCATION AND CERTIFICATION')
 for a,b in [('B.Tech, Technology Management & Mechanical Engineering','Copenhagen School of Marine and Technical Engineering · maskinmester programme'),('Electrical and mechanical engineering design, electrical engineering','Tehran Technical University'),('Danish authorisation as marine and technical engineer','Danish Safety Technology Authority · LV/MV/HV'),('PRINCE2 certified project manager','AXELOS / PeopleCert')]:m.edu(a,b)
 m.para('Languages: English (professional); Danish and Persian/Farsi (native). Digital tools: SAP ERP, Excel, Power BI, Python and Claude API.',after=40)
 m.page_break();m.models_table('FIRST 90 DAYS — PROPOSED APPROACH',('When','Actions and outputs'),[
 ('Week 1','Meet the VPMS team, manufacturing leadership and site representatives. Understand current standards, strategy, decision rights and the measures already in use.'),
 ('By day 30','Visit or speak with representative sites across the manufacturing network. Review existing maturity assessments and site priorities; identify differences and agree a baseline with the responsible leaders.'),
 ('By day 60','Work with plant leaders to select a limited number of gaps and agree owners, measures and support. Review how coaching, standard work and problem solving are embedded locally.'),
 ('By day 90','Review evidence and feedback with site leaders and the VPMS team. Propose a prioritised deployment and capability plan, including practical follow-up and a way to share lessons across sites.')])
 m.section('FROM A GLOBAL STANDARD TO DAILY PRACTICE')
 for a,b in [
 ('Strategy and governance','Connect business priorities to a manageable set of operational objectives. Clarify decision rights, site ownership and review cadence with manufacturing leadership.'),
 ('Assess and close gaps','Use existing maturity criteria and audits to compare the intended standard with actual practice. Agree evidence, actions, owners and dates with the site rather than relying on scores alone.'),
 ('Build capability','Coach plant leaders around real problems, using GROW, PDCA and A3 where suitable. Support local teams in developing standard work that can be maintained after the initial intervention.'),
 ('Learn across sites','Identify practices worth benchmarking, test their transfer with the receiving teams, and monitor safety, quality, delivery, cost and productivity before wider replication.')]:m.bullet(a,b,after=30)
 m.section('DATA AND SUSTAINMENT')
 m.para('I use Python and Claude for planning, quality and management reporting and build investment models for new ideas. Any VPMS dashboard or AI-assisted analysis should use approved data and support decisions by plant teams, with human validation and clear responsibility for the underlying measures.',after=70)
 m.section('LEADERSHIP SCOPE')
 m.para('My experience includes workshop leadership, technical operations and improvement initiatives. It does not document the 15 years in global manufacturing, multi-plant production-system rollout or large-scale international cultural transformation specified for this director role.',after=60)
 return m.save(path,title='Application and CV — Vestas Head of VPMS 78810',subject='Operational improvement and technical leadership',keywords='VPMS, Lean, continuous improvement, Vestas')

if __name__=='__main__':print(build(os.path.join(ROOT,'Shahram_Ajloo_Vestas_HeadVPMS_78810.docx')))
