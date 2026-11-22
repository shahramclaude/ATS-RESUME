"""Kirby Electrical Construction Manager application and CV, master format."""
from pathlib import Path
from master_design import MasterDoc
R=Path(__file__).resolve().parent.parent
m=MasterDoc(str(R/'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='en-GB')
n='SHAHRAM AJLOO'; t='Electrical Construction Manager | Denmark'
c='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'
m.header_banner(n,t,c);m.meta('Kirby Group Engineering · Electrical Construction Manager · Denmark',after=30)
m.para('**Application: Electrical Construction Manager**',after=70,justify=False)
m.para('Dear Kirby hiring team,',after=60,justify=False)
m.para('A successful electrical site is built on more than a master programme: people need safe access to the workface, drawings and materials must be ready, and each trade must know what the others need. As the Project Manager’s representative, the construction manager has to connect those details to safety, progress, cost and a clean handover.',after=55,line=245,justify=False)
m.para('For Kirby, I would organise site delivery around four connected routines:',after=45,line=240,justify=False)
for a,b in [
('Start with a buildable plan','Walk the site with the project team, review drawings, access, interfaces and construction sequence, and turn the programme into short-term look-aheads. Agree material and equipment schedules, site establishment and risk assessments with the PM and subcontractors before work starts.'),
('Keep work safe and moving','Use daily walkarounds and a short action plan covering HSEQ, workface readiness, labour, deliveries and constraints. Confirm inductions, toolbox talks, permits, PPE and method statements are in place; intervene when conditions change and coordinate electrical, mechanical and building trades.'),
('Make decisions visible','Keep a site diary, follow up subcontractor allocation and productivity, and update the programme weekly. Record variations promptly with the PM and quantity surveyor, agree actions and owners, and escalate issues affecting safety, quality, budget or schedule.'),
('Build quality into close-out','Use the inspection and test plan to check work progressively, resolve snags before client inspection and maintain marked-up drawings. Coordinate testing, safety-device checks, certification and handover with commissioning engineers; plan demobilisation with the PM.')]:m.bullet(a,b,after=25,line=240)
m.para('My background combines electrical contracting, personnel and subcontractor coordination, and commissioning in regulated industry. At ELOHVAC I manage electrical service delivery, safety, documentation and full P&L, leading five electricians and three apprentices. At Novo Nordisk I coordinated 25 specialists on 37 concurrent CAPEX projects and worked with FAT/SAT and IQ/OQ/PQ, achieving zero critical deviations at handover. At Ventek-Air I led 14 people across 11 concurrent projects from specification to handover.',after=55,line=245,justify=False)
m.para('Kirby’s emphasis on People, Safety, Quality and Delivery, supported by its Zero Harm approach, fits the disciplined site culture I would seek to build. I would welcome an interview to discuss how this experience can support your projects in Denmark.',after=40,line=245,justify=False)
m.meta('Yours sincerely · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com',after=0)
m.page_break();m.resume_header(n,t,c,'ELECTRICAL DELIVERY, SITE COORDINATION & SAFETY')
m.para('Electrically authorised marine and technical engineer and project leader with experience in electrical contracting, technical teams, commissioning and regulated-industry project delivery. Brings practical coordination of people, subcontractors, materials, safety and documentation from planning through handover.',after=60,line=245,justify=False)
m.section('EXPERIENCE RELEVANT TO THE ROLE')
for a,b in [
('Electrical delivery','ELOHVAC: electrical installations, panels, controls, fault-finding and preventive maintenance, supported by planning, materials and subcontractor coordination. Also brings direct experience of 10/0.4 kV distribution work.'),
('Project and contractor management','At least three years of project and contractor management in electrical or related industry. Ventek-Air: 11 concurrent projects from specification to handover; Novo Nordisk: 37 concurrent CAPEX projects, each DKK 2–10 million.'),
('People and interfaces','Lead five electricians and three apprentices at ELOHVAC; previously led 14 people at Ventek-Air. Coordinated 25 specialists across engineering, procurement and site teams at Novo Nordisk.'),
('Safety and commercial control','Site risk assessments, LOTO, safety follow-up, quotations, materials, subcontractors and full P&L responsibility at ELOHVAC. Experience of contract follow-up and forecast in operations or service delivery.'),
('Testing and quality','FAT/SAT and IQ/OQ/PQ in a regulated production environment at Novo Nordisk, with zero critical deviations at handover; quality assurance and handover documentation in technical contracting.')]:m.bullet(a,b,after=20,line=240)
m.models_table('SITE DELIVERY — PROPOSED APPROACH',('Phase','Site leadership actions'),[
('Mobilise','Review drawings, construction sequence, method statements, risk assessments, access, temporary arrangements and material schedules with the PM and subcontractors.'),
('Deliver','Coordinate workfaces and M&E interfaces; use daily safety and productivity checks, site diary and look-ahead plans; report progress and variations to PM and QS.'),
('Inspect and test','Check installation against the inspection and test plan; resolve snags, maintain drawing mark-ups and coordinate client inspection and commissioning.'),
('Hand over','Confirm testing, safety devices, certificates, drawings and completion records with responsible specialists; plan demobilisation and follow-up with the PM.')])
m.section('SELECTED RESULTS')
for a,b in [('Quality','Novo Nordisk: zero critical deviations at handover across documented project work.'),('Team delivery','Ventek-Air: 14-person team and 11 concurrent projects; ELOHVAC: five electricians and three apprentices.'),('Improvement','AI-assisted tools at ELOHVAC contributed to over 40% productivity improvement.')]:m.bullet(a,b,after=15,line=235)
m.page_break();m.section('PROFESSIONAL EXPERIENCE')
m.job('Owner / Technical Director / electrically authorised marine engineer','ELOHVAC ApS · Copenhagen · May 2023–present')
for a,b in [('Electrical contracting','Electrical installation, panels and controls, troubleshooting and preventive maintenance; quotations, planning, materials, subcontractors, quality assurance and handover.'),('Leadership and HSEQ','Lead five electricians and three apprentices; site risk assessment, LOTO, safety follow-up, training and full P&L responsibility.'),('Improvement','AI-assisted quotations, schedules and quality checks contributed to over 40% productivity improvement.')]:m.bullet(a,b,after=15,line=240)
m.job('Co-owner and CTO / Head of AI','Data Power Consultant ApS · Copenhagen · 2024–Nov 2026')
m.bullet('Technical leadership','Led an AI department of 4–10 people, with customer applications, AI coding, LLM APIs and AI agents. Applied AI to technical design and management with professional review. Role alongside ELOHVAC; company has ceased operations.',after=15,line=240)
m.job('Senior Commissioning Engineer / Project Manager, electrical systems','Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024')
for a,b in [('Project delivery','Coordinated 25 specialists on 37 concurrent CAPEX projects, each DKK 2–10 million; tracked progress, cost, risk and resources across engineering, procurement and site teams.'),('Commissioning','FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA, with zero critical deviations at handover.')]:m.bullet(a,b,after=15,line=240)
m.job('Project and Workshop Manager','Ventek-Air · Copenhagen · Jan 2022–Nov 2022')
m.bullet('Construction projects','Led 14 people and 11 concurrent projects, each DKK 2–10 million, from specification to formal handover, including subcontractors, safety documentation and capacity planning.',after=15,line=240)
m.job('Maintenance and Operations Lead / Workshop Technician','BIOFOS, Lynetten · Copenhagen · Aug 2017–Jan 2022')
m.bullet('Technical operations','Electrical and mechanical maintenance, pumps, HVAC, high-voltage panels and SCADA; preventive maintenance and fault-finding in 24/7 operations.',after=15,line=240)
m.job('Electromechanic / Production Team Leader','ARJ Engineering · Tehran · Dec 2003–Mar 2010')
m.bullet('Technical team','Led 12 mechanics and technicians; diagnosed and repaired electrical and mechanical equipment.',after=15,line=240)
m.section('EDUCATION, METHODS & LANGUAGES')
for a,b in [('Electrical authorisation as marine and technical engineer, LV/MV/HV','Danish Safety Technology Authority · May 2023'),('Bachelor (B.Tech), Technology Management and Mechanical Engineering','Copenhagen School of Marine Engineering & Technology Management · 2017–2022'),('Electrical & Mechanical Design, Electrical Engineering','Tehran Technical University · 2000–2003'),('PRINCE2 certified project manager','AXELOS / PeopleCert')]:m.edu(a,b)
m.para('**Methods:** PRINCE2, Lean and Six Sigma applied in practice; certified in PRINCE2. **Tools:** Excel, SAP ERP and AI-assisted planning tools. **Languages:** Danish, English (professional) and Persian. **Location:** Måløv, Denmark.',after=20,line=235,justify=False)
m.save(str(R/'Shahram_Ajloo_Kirby_ElectricalConstructionManager.docx'))
