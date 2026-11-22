"""Vestas 75841 detailed application and CV, with fair-hiring fields omitted."""
from pathlib import Path
from master_design import MasterDoc
R=Path(__file__).resolve().parent.parent
N='SHAHRAM AJLOO';T='Installation Supervisor | Safety, quality & site delivery'
C='+45 93 99 95 14 · ajlooshahram@gmail.com'
def build(letter,filename):
 m=MasterDoc(str(R/'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='en-GB')
 if letter:
  m.header_banner(N,T,C);m.meta('Vestas · Installation Supervisor · Requisition 75841',after=30)
  m.para('**Application: Installation Supervisor**',after=65,justify=False)
  m.para('Dear Vestas hiring team,',after=60,justify=False)
  m.para('A safe installation day starts before the first task: the team needs to understand the work, conditions, interfaces and controls. When a delivery or schedule changes, the supervisor has to reassess readiness with the people involved rather than let pressure create unsafe work or rework.',after=55,line=245,justify=False)
  m.para('For Vestas’ onshore installation projects, I would focus on four practical routines:',after=40,line=240,justify=False)
  for a,b in [
   ('Prepare with the team','Review the approved work package, site plan, competence requirements and safety controls with the site manager and installation team. Confirm material and equipment readiness, work areas and interfaces with other trades. If the plan or conditions change, stop and resolve uncertainty through the agreed Vestas procedures.'),
   ('Lead the site day','Use short daily briefings to agree responsibilities, sequence, risks and immediate constraints. Stay available to the team, listen to concerns, share schedule changes and keep the project team informed. Adapt the plan with the responsible people, keeping HSE and quality ahead of pace.'),
   ('Check quality as work progresses','Agree the required inspections, records and open-item ownership with the quality and commissioning teams. Follow up on deviations, document progress in approved systems and verify the evidence needed for handover to Service.'),
   ('Build trust across interfaces','Keep customer and project stakeholders updated through agreed channels, ask for input from experienced colleagues and contractors, and communicate clearly across disciplines and cultures. Use lessons from each task to improve the next without departing from approved instructions.')]:m.bullet(a,b,after=25,line=240)
  m.para('My background combines electrical and mechanical work, site-based personnel leadership and commissioning. At ELOHVAC I lead five electricians and three apprentices, coordinating safety, materials, subcontractors and customer delivery. At Ventek-Air I led 14 people across 11 concurrent projects. At Novo Nordisk I coordinated 25 specialists on 37 concurrent projects and worked with FAT/SAT and IQ/OQ/PQ, with zero critical deviations at handover.',after=55,line=245,justify=False)
  m.para('Vestas’ commitment to safety, collaboration and accountability provides the framework I would bring to each site. My experience is in technical installations and operations; I would learn turbine-specific equipment, procedures and authorisations with qualified colleagues. I would welcome an interview about supporting safe delivery from preparation through handover.',after=40,line=245,justify=False)
  m.meta('Kind regards · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com',after=0)
  m.page_break()
 m.resume_header(N,T,C,'TECHNICAL PROFILE & SITE LEADERSHIP')
 m.para('Electrically authorised marine and technical engineer with electrical and mechanical installation, technical operations, commissioning and people leadership experience. Coordinates personnel, subcontractors, materials, risk, quality and handover across changing project sites. Brings practical customer communication and structured follow-up to multidisciplinary field work.',after=60,line=245,justify=False)
 m.section('EXPERIENCE RELEVANT TO VESTAS INSTALLATION')
 for a,b in [
  ('Site leadership and teamwork','Lead five electricians and three apprentices at ELOHVAC; previously led 14 people at Ventek-Air. Plan work, support skills development, communicate priorities and coordinate subcontractors and materials.'),
  ('Electrical and mechanical foundation','Electrical installation, switchboards, controls and troubleshooting; mechanical and electrical operations including pumps, HVAC, high-voltage panels and SCADA. Direct experience of 10/0.4 kV distribution work.'),
  ('HSE and safety','Use risk assessments, APV and lockout/tagout (LOTO) during technical work and site start-up. Experience of work-environment follow-up, near-miss awareness and safe shift operations.'),
  ('Quality, commissioning and handover','FAT/SAT and IQ/OQ/PQ on electrical systems in regulated Novo Nordisk projects, with zero critical deviations at handover. Technical quality assurance and handover documentation in ELOHVAC and Ventek-Air.'),
  ('Progress, coordination and collaboration','At Novo Nordisk, coordinated 25 specialists on 37 concurrent CAPEX projects, tracking cost, progress, resources and risks across engineering, procurement and site teams. At Ventek-Air, daily huddles and bottleneck analysis supported 11 concurrent projects.'),
  ('Customers and digital tools','Customer quotations, delivery and follow-up at ELOHVAC; SAP ERP for finance and assets at Novo Nordisk, Excel, Power BI and AI-assisted schedules and quality checks. Professional English.')]:m.bullet(a,b,after=20,line=240)
 m.section('SITE METHODS AND WORKING PRACTICES')
 m.para('**Safety and quality:** risk assessment, APV, LOTO, FAT/SAT, IQ/OQ/PQ and structured handover. **Coordination:** daily huddles, planning, RACI, stakeholder communication and escalation. **Improvement:** Lean, Six Sigma, PDCA, A3, 5 Whys and Ishikawa applied in practice; PRINCE2 certified. **People:** situational leadership, 1:1s, feedback and structured training.',after=35,line=240,justify=False)
 m.models_table('PROPOSED APPROACH ON A VESTAS SITE',('Site priority','Practical action with responsible colleagues'),[
  ('Safe start','Check the approved task, competence, conditions and controls; stop and escalate if conditions or scope change.'),
  ('Daily coordination','Agree work sequence, interfaces, materials and constraints with the installation team and site management.'),
  ('Quality and progress','Follow up on checks, schedule and open items; record evidence in approved systems and involve the responsible quality team.'),
  ('Handover to Service','Coordinate testing, outstanding actions, required records and ownership with commissioning and Service.')])
 m.page_break();m.section('PROFESSIONAL EXPERIENCE — SITE DELIVERY AND TECHNICAL LEADERSHIP')
 m.job('Owner / Technical Director / electrically authorised marine engineer','ELOHVAC ApS · Copenhagen · May 2023–present')
 for a,b in [
  ('Installation and customer delivery','Coordinate electrical installations, panels, controls and technical services, including quotations, materials, subcontractors, quality assurance and handover.'),
  ('People and safety','Lead five electricians and three apprentices through daily planning, 1:1s and structured training. Apply risk assessment, APV and LOTO and follow up on work environment and safety.'),
  ('Digital improvement','Develop AI-assisted quotation, scheduling, quality-check and KPI tools. These contributed to a productivity improvement of over 40%; full P&L responsibility.')]:m.bullet(a,b,after=20,line=240)
 m.job('Co-owner and CTO / Head of AI and AI coding','Data Power Consultant ApS · Copenhagen · 2024–Nov 2026')
 for a,b in [('Technical applications','Led an AI department of 4–10 people. Worked on technical and industrial applications from requirements and integration to commissioning, documentation and handover.'),('Responsible digital work','Introduced AI-assisted coding, review and testing; used LLM APIs and AI agents and applied professional review to technical design and management reporting. The role ran alongside ELOHVAC; the company has ceased operations.')]:m.bullet(a,b,after=20,line=240)
 m.job('Senior Commissioning Engineer / Project Manager, electrical systems','Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024')
 for a,b in [('Project coordination','Coordinated 25 specialists across 37 concurrent CAPEX projects, each DKK 2–10 million; monitored progress, costs, risk and resources across engineering, procurement and site teams.'),('Commissioning and quality','FAT/SAT and IQ/OQ/PQ for electrical systems under GMP/FDA/EMA; zero critical deviations at handover. Used SAP ERP for finance and assets.'),('Improvement','Used A3, 5 Whys and Ishikawa for problem-solving; a PDCA programme reduced energy costs by 40%.')]:m.bullet(a,b,after=20,line=240)
 m.job('Project and Workshop Manager','Ventek-Air · Copenhagen · Jan 2022–Nov 2022')
 m.bullet('Team and execution','Led 14 people and 11 concurrent projects from specification to handover; capacity planning, subcontractors, daily huddles, safety documentation and bottleneck analysis.',after=20,line=240)
 m.page_break();m.section('PROFESSIONAL EXPERIENCE — OPERATIONS AND TECHNICAL WORK')
 m.job('Maintenance and Operations Lead / Workshop Technician','BIOFOS, Lynetten · Copenhagen · Aug 2017–Jan 2022')
 for a,b in [('Plant operations','Maintained electrical and mechanical systems including pumps, HVAC, high-voltage panels and SCADA; preventive maintenance and acute fault-finding in 24/7 operations.'),('Safety and continuous improvement','Used LOTO, risk assessments and near-miss follow-up in shift operations; applied 5S, Standard Work and PDCA to workshop and stock flow.')]:m.bullet(a,b,after=20,line=240)
 m.job('Electromechanic / Production Team Leader','ARJ Engineering · Tehran · Dec 2003–Mar 2010')
 for a,b in [('Team and technical delivery','Led 12 mechanics and technicians; shift planning, materials and targets, diagnosis and repair of electrical and mechanical equipment.'),('Product and investment','Product-portfolio responsibility for a motors and pumps line, including business cases, pricing and investment decisions.')]:m.bullet(a,b,after=20,line=240)
 m.section('EDUCATION & PROFESSIONAL QUALIFICATIONS')
 for a,b in [('Bachelor (B.Tech), Technology Management and Mechanical Engineering','Copenhagen School of Marine Engineering & Technology Management'),('Electrical & Mechanical Design, Electrical Engineering','Tehran Technical University'),('Electrical authorisation as marine and technical engineer, LV/MV/HV','Danish Safety Technology Authority'),('PRINCE2 certified project manager','AXELOS / PeopleCert'),('Refrigeration and air conditioning','Mercantec · AMU'),('STCW safety and engine-room watchkeeping training','Danish Maritime Authority')]:m.edu(a,b)
 m.para('**Methods:** Lean and Six Sigma applied in practice; PRINCE2 certified. **Tools:** SAP ERP, Excel, Power BI, Python and AI-assisted planning. **Language:** English (professional).',after=30,line=240,justify=False)
 m.models_table('PROPOSED FIRST 90 DAYS — INSTALLATION SUPERVISION',('Period','Actions with the site team'),[
  ('Days 1–30','Complete required induction, understand Vestas HSE and quality procedures, meet site teams and identify role-specific training and authorisations. Observe planning and handover with an experienced supervisor.'),
  ('Days 30–60','Coordinate assigned activities within agreed competence and authority. Follow progress, interfaces and open items with installation, project, quality and commissioning colleagues.'),
  ('Days 60–90','Review safety, quality, schedule and lessons with the team. Confirm outstanding training, improve an agreed site routine and prepare documented handover to Service.')])
 m.para('**Technical development:** The experience above is in electrical and mechanical installations and plant operations. Turbine-specific equipment and site procedures would be learned with qualified Vestas colleagues and within required authorisations.',after=20,line=240,justify=False)
 m.save(str(R/filename))
build(True,'Shahram_Ajloo_Vestas_InstallationSupervisor_75841_Udvidet.docx')
build(False,'Shahram_Ajloo_Vestas_InstallationSupervisor_75841_CV_Udvidet.docx')
