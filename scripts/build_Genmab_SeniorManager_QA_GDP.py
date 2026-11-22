"""Genmab QA GDP application and detailed CV: factual experience and proposed steps separated."""
from pathlib import Path
from master_design import MasterDoc
R=Path(__file__).resolve().parent.parent
N='SHAHRAM AJLOO';T='Senior Manager, Quality Assurance – GDP | Denmark'
C='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'
def build(letter,filename):
 m=MasterDoc(str(R/'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='en-GB')
 if letter:
  m.header_banner(N,T,C);m.meta('Genmab · Senior Manager, Quality Assurance – GDP · Denmark',after=30)
  m.para('**Application: Senior Manager, Quality Assurance – GDP**',after=70,justify=False)
  m.para('Dear Genmab hiring team,',after=60,justify=False)
  m.para('Patients depend on the quality of a medicine throughout its journey, not only when it leaves a manufacturing site. Genmab’s expanding commercial network therefore needs clear oversight of storage, transportation and external partners, with decisions supported by evidence and the right quality expertise.',after=55,line=245,justify=False)
  m.para('My background is in technical project delivery and commissioning in regulated pharmaceutical production, rather than a dedicated pharmaceutical QA or GDP role. At Novo Nordisk I worked with FAT/SAT and IQ/OQ/PQ for electrical systems, coordinating 25 specialists across 37 concurrent CAPEX projects with zero critical deviations at handover. I would bring that documentation discipline, risk awareness and cross-functional approach to learning the distribution quality domain.',after=55,line=245,justify=False)
  m.para('The way I would contribute, working within Genmab’s procedures and with qualified GDP and audit colleagues, is:',after=45,line=240,justify=False)
  for a,b in [
   ('Partner oversight','Review the approved vendor assessment, quality agreement and performance evidence with the responsible QA colleagues. Record open questions, owners and follow-up dates; escalate changes or recurring issues rather than allowing uncertainty to remain unresolved.'),
   ('Audit and inspection readiness','Support qualified auditors in preparing records and tracking observations and actions. Develop the required audit capability through appropriate training and supervised practice before undertaking audits independently.'),
   ('Quality events and distribution','Work with QA, Supply Chain and external partners to collect facts for deviations, change controls and product complaints. Support risk assessments for storage, transport and shipping lane qualification, using approved procedures and escalating quality decisions to authorised colleagues.'),
   ('Reliable follow-through','Maintain clear documentation and action ownership for cross-functional work, including recall readiness, shipment release, EU serialization, SOP updates and training. Confirm responsibilities and approvals with experienced process owners before acting.')]:m.bullet(a,b,after=25,line=240)
  m.para('Genmab’s science-led purpose makes careful quality work meaningful: a reliable record and a timely escalation can protect both product integrity and patient supply. I would welcome a discussion of where my regulated-project and technical quality experience could contribute to your team.',after=40,line=245,justify=False)
  m.meta('Yours sincerely · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com',after=0)
  m.page_break()
 m.resume_header(N,T,C,'QUALITY, TECHNICAL DELIVERY & CROSS-FUNCTIONAL COORDINATION')
 m.para('Technical and project leader based in Denmark, with experience of commissioning and qualification of electrical systems in regulated pharmaceutical production, operational quality documentation, risk assessment and technical supplier coordination. B.Tech in technology management and mechanical engineering; professional English. Background is technical delivery rather than dedicated GDP quality assurance or GxP auditor work.',after=60,line=245,justify=False)
 m.section('RELEVANT EXPERIENCE AND TRANSFERABLE CAPABILITIES')
 for a,b in [
  ('Regulated work and qualification','At Novo Nordisk, performed project work involving FAT/SAT and IQ/OQ/PQ for electrical systems under GMP/FDA/EMA; zero critical deviations at handover. Coordinated specialists across engineering, procurement and site functions.'),
  ('Quality, documentation and risk','Experience of quality assurance, handover documents, risk assessments and technical problem-solving in operational and project settings. Uses A3, 5 Whys, Ishikawa and PDCA to investigate issues and improve work.'),
  ('Partners and customer issues','Coordinates subcontractors, suppliers and customer delivery in ELOHVAC. Experience with complaint and warranty handling and international supplier dialogue across roles; the context is technical service rather than pharmaceutical product complaints.'),
  ('Cross-functional execution','Coordinated 25 specialists across 37 simultaneous CAPEX projects at Novo Nordisk, tracking progress, cost, resources and risk. Communicates across disciplines and follows actions through to handover.'),
  ('Systems and improvement','SAP ERP and Excel for operational follow-up; AI-assisted planning, quality checks and documentation tools at ELOHVAC contributed to over 40% productivity improvement. PRINCE2 certified; Lean and Six Sigma applied in practice.')]:m.bullet(a,b,after=25,line=240)
 m.models_table('GDP QUALITY — PROPOSED APPROACH, NOT PRIOR ROLE EXPERIENCE',('Area','How I would work with qualified colleagues'),[
  ('Audits and vendors','Support audit preparation and action follow-up with qualified GxP auditors; review vendor risk and quality agreements under established procedures.'),
  ('Issues and change','Gather facts and support documentation of deviations, change controls, external notifications and complaints; refer quality decisions to authorised QA.'),
  ('Storage and transport','Support GDP risk assessments and shipping lane qualification with Supply Chain and experienced quality specialists.'),
  ('Product protection','Follow approved recall, shipment release and EU serialization processes with the responsible process owners; do not release independently without authorisation.'),
  ('Quality systems','Help maintain SOPs, work instructions, GDP training records and inspection readiness in line with assigned responsibilities.')])
 m.page_break();m.section('PROFESSIONAL EXPERIENCE — QUALITY AND TECHNICAL DELIVERY')
 m.job('Owner / Technical Director / electrically authorised marine engineer','ELOHVAC ApS · Copenhagen · May 2023–present')
 for a,b in [('Quality and delivery','Electrical installation, controls, troubleshooting and maintenance; quality assurance, customer delivery, subcontractor coordination and handover documentation.'),('Risk and people','Site risk assessment, LOTO and safety follow-up; lead five electricians and three apprentices, with full P&L responsibility.'),('Improvement','AI-assisted tools for quotations, schedules, quality checks and KPIs contributed to over 40% productivity improvement.')]:m.bullet(a,b,after=20,line=240)
 m.job('Co-owner and CTO / Head of AI and AI coding','Data Power Consultant ApS · Copenhagen · 2024–Nov 2026')
 for a,b in [('Technical applications','Led an AI department of 4–10 people; worked on customer technical and industrial applications from requirements and integration to documentation and handover.'),('Controlled use of AI','Introduced AI-assisted coding, review and testing standards; used LLM APIs and AI agents and applied professional review to technical design and management information. Role ran alongside ELOHVAC; the company has ceased operations.')]:m.bullet(a,b,after=20,line=240)
 m.job('Senior Commissioning Engineer / Project Manager, electrical systems','Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024')
 for a,b in [('GMP-related delivery','FAT/SAT and IQ/OQ/PQ for electrical systems under GMP/FDA/EMA; zero critical deviations at handover.'),('Coordination and risk','Coordinated 25 specialists on 37 concurrent CAPEX projects, monitoring progress, financials, resources and risk across engineering, procurement and site functions.'),('Structured improvement','Used A3, 5 Whys and Ishikawa in troubleshooting; a PDCA programme reduced energy costs by 40%.')]:m.bullet(a,b,after=20,line=240)
 m.job('Project and Workshop Manager','Ventek-Air · Copenhagen · Jan 2022–Nov 2022')
 m.bullet('Planning and handover','Led 14 people and 11 concurrent projects from specification to formal handover; coordinated subcontractors and safety and handover documentation.',after=20,line=240)
 m.page_break();m.section('PROFESSIONAL EXPERIENCE — OPERATIONS AND TECHNICAL QUALITY')
 m.job('Maintenance and Operations Lead / Workshop Technician','BIOFOS, Lynetten · Copenhagen · Aug 2017–Jan 2022')
 for a,b in [('Reliability','Electrical and mechanical operations including pumps, HVAC, high-voltage panels and SCADA; preventive maintenance and acute fault-finding in 24/7 operations.'),('Safety and improvement','Applied 5S, Standard Work and PDCA to workshop and stock flow, with LOTO and risk assessment in shift operations.')]:m.bullet(a,b,after=20,line=240)
 m.job('Electromechanic / Production Team Leader','ARJ Engineering · Tehran · Dec 2003–Mar 2010')
 for a,b in [('Team and technical problems','Led 12 mechanics and technicians; shift and materials planning, fault diagnosis, root-cause analysis and corrective action on industrial equipment.'),('Product portfolio','Responsibility for a line of motors and pumps, including business cases, development and launch, pricing and investment decisions.')]:m.bullet(a,b,after=20,line=240)
 m.section('EDUCATION, METHODS & LANGUAGES')
 for a,b in [('Bachelor (B.Tech), Technology Management and Mechanical Engineering','Copenhagen School of Marine Engineering & Technology Management · 2017–2022'),('Electrical & Mechanical Design, Electrical Engineering','Tehran Technical University · 2000–2003'),('Electrical authorisation as marine and technical engineer, LV/MV/HV','Danish Safety Technology Authority · May 2023'),('PRINCE2 certified project manager','AXELOS / PeopleCert'),('Refrigeration and air conditioning','Mercantec · AMU · 2021'),('HF, mathematics and physics','VUC · 2012–2017'),('STCW maritime safety and engineering courses','Danish Maritime Authority · 2021–2023')]:m.edu(a,b)
 m.para('**Methods:** PRINCE2, Lean and Six Sigma applied in practice; certified in PRINCE2. **Tools:** Excel, SAP ERP, Power BI and AI-assisted documentation. **Languages:** Danish and Persian (native); English (professional). **Location:** Måløv, Denmark.',after=35,line=240,justify=False)
 m.models_table('PROPOSED LEARNING & CONTRIBUTION — FIRST 90 DAYS',('Period','Priorities with the QA manager and qualified colleagues'),[
  ('Days 1–30','Understand Genmab’s quality system, GDP procedures, responsibilities and escalation routes. Meet QA, Supply Chain and Commercial Operations; review training and role-specific qualification requirements.'),
  ('Days 30–60','Support assigned quality documentation and partner follow-up under supervision. Observe audit preparation and follow-up; review storage and shipping risks with experienced GDP colleagues.'),
  ('Days 60–90','Review progress and remaining qualification needs with the manager. Contribute to approved improvements and take on only tasks for which training and authorisation have been confirmed.')])
 m.save(str(R/filename))
build(True,'Shahram_Ajloo_Genmab_SeniorManager_QA_GDP.docx')
build(False,'Shahram_Ajloo_Genmab_SeniorManager_QA_GDP_CV.docx')
