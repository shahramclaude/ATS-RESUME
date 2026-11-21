"""Johnson & Johnson Site Contracting EMEA application and CV in master style."""
from pathlib import Path
from master_design import MasterDoc
R=Path(__file__).resolve().parent.parent
m=MasterDoc(str(R/'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='en-GB')
n='SHAHRAM AJLOO'; t='Manager, Site Contracting EMEA | Copenhagen'
c='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'
m.header_banner(n,t,c);m.meta('Johnson & Johnson Innovative Medicine · Denmark · Requisition R-112376',after=30)
m.para('**Application: Manager, Site Contracting EMEA**',after=70,justify=False)
m.para('Dear hiring team,',after=65,justify=False)
m.para('A site cannot begin a study until the agreement, investigator budget and required approvals are in place. The Site Contracting team needs a clear view of those dependencies, timely escalation and the space to negotiate carefully. That balance of speed, quality and compliance supports Innovative Medicine’s work for patients and reflects the responsibility at the heart of Our Credo.',after=65,line=245,justify=False)
m.para('My approach to leading the team would focus on four practical priorities:',after=45,line=240,justify=False)
for a,b in [
('Make delivery visible','Agree ownership and next steps for each agreement, budget and amendment. Review ageing, pending approvals and activation milestones with the team and Clinical Operations; escalate issues early with a clear decision request.'),
('Respect country and site differences','Work with country specialists, Legal and Healthcare Compliance to understand local institution requirements and the applicable regulatory framework, including the EU Clinical Trials Regulation where relevant. Use their guidance to set realistic plans rather than applying a single EMEA assumption.'),
('Support sound negotiations','Give contract owners room to resolve issues and bring Legal, Finance and compliance partners in when terms or investigator grants need escalation. Use the company’s fair market value standards and documented approval routes; ensure the agreed position is clear to the site.'),
('Develop people and improve the process','Use regular coaching and prioritisation to strengthen accountability. Examine recurring bottlenecks with team members and sites; consider standard terms, master agreements and automation where approved. AI-assisted work must protect confidential information and be checked by an accountable person.')]:m.bullet(a,b,after=30,line=240)
m.para('The experience I would bring is in technical delivery and leadership rather than clinical trial site contracting. At Novo Nordisk, I coordinated 25 specialists across 37 concurrent projects in a regulated production environment, with no critical deviations at handover. ELOHVAC adds P&L responsibility, customer delivery and team leadership; my experience also includes forecasting and contract follow-up in operations or service delivery. AI-assisted planning and quality tools contributed to a productivity improvement of over 40% at ELOHVAC.',after=55,line=245,justify=False)
m.para('I would welcome a discussion about how this operational leadership could support the EMEA contracting organisation, alongside the clinical contracting and country expertise of the team.',after=45,line=245,justify=False)
m.meta('Yours sincerely · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com',after=0)
m.page_break();m.resume_header(n,t,c,'PEOPLE LEADERSHIP, DELIVERY & CONTINUOUS IMPROVEMENT')
m.para('Technical and business leader with experience coordinating teams and delivery in regulated industry, managing customer commitments and improving operational processes. Brings financial accountability, AI-assisted ways of working and practical Lean methods to complex, cross-functional work.',after=60,line=245,justify=False)
m.section('EXPERIENCE RELEVANT TO SITE CONTRACTING')
for a,b in [
('People leadership','Lead five electricians and three apprentices at ELOHVAC; led 14 people at Ventek-Air. Set priorities, support individual development and follow up delivery and safety.'),
('Coordination and quality','At Novo Nordisk, coordinated 25 specialists across 37 concurrent CAPEX projects. Managed progress, resources and risks across engineering, procurement and site teams, with zero critical deviations at handover.'),
('Commercial and financial follow-up','Full P&L responsibility, customer quotations and cost estimates at ELOHVAC; experience of forecasting and contract follow-up in operations or service delivery.'),
('AI and improvement','AI-assisted quotations, schedules and quality checks contributed to over 40% productivity improvement at ELOHVAC. Led a 4–10 person AI department at Data Power, with technical review of AI-assisted work.'),
('Clinical context','Background is in technical and operational delivery, including pharmaceutical production projects, not clinical trial contracts or investigator grants. Site start-up and multi-country clinical contracting would be a new domain.')]:m.bullet(a,b,after=20,line=240)
m.models_table('CONTRACTING DELIVERY — PROPOSED LEADERSHIP APPROACH',('Priority','Practical action'),[
('Delivery and activation','Review contract and budget status, site activation dependencies, ageing and escalation owners with the team.'),
('Country requirements','Use country specialists and Legal to confirm local institutional and regulatory requirements before decisions.'),
('Investigator grants','Involve Finance and Healthcare Compliance; use approved fair market value standards and document decisions.'),
('People and partners','Coach contract owners; agree escalation routes with Clinical Operations, sites and CRO partners.'),
('Improvement and AI','Investigate cycle-time bottlenecks; test approved standardisation and automation with human quality checks.')])
m.section('SELECTED RESULTS')
for a,b in [('Leadership','ELOHVAC: full P&L responsibility and leadership of five electricians and three apprentices.'),('Regulated delivery','Novo Nordisk: 37 concurrent projects, coordination of 25 specialists and zero critical deviations at handover.'),('Productivity','AI-assisted tools at ELOHVAC contributed to a productivity improvement of over 40%.')]:m.bullet(a,b,after=15,line=235)
m.page_break();m.section('PROFESSIONAL EXPERIENCE')
m.job('Owner / Technical Director / electrically authorised marine engineer','ELOHVAC ApS · Copenhagen · May 2023–present')
for a,b in [('Delivery and finance','Full P&L responsibility; quotations, cost estimation, materials, subcontractors, quality documentation and customer delivery.'),('People','Lead five electricians and three apprentices, including planning, development and safety.'),('AI and improvement','AI-assisted tools for quotations, schedules and quality checks contributed to productivity improvement of over 40%.')]:m.bullet(a,b,after=15,line=240)
m.job('Co-owner and CTO / Head of AI','Data Power Consultant ApS · Copenhagen · 2024–Nov 2026')
m.bullet('Technical leadership','Led an AI department of 4–10 people, working on customer applications, AI coding, LLM APIs and AI agents. Applied AI to technical design and leadership work with professional review. Role ran alongside ELOHVAC; the company has ceased operations.',after=15,line=240)
m.job('Senior Commissioning Engineer / Project Manager, electrical systems','Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024')
for a,b in [('Project coordination','Coordinated 25 specialists across 37 concurrent CAPEX projects, monitoring cost, progress, resources and risk.'),('Quality','FAT/SAT and IQ/OQ/PQ in a regulated production environment; zero critical deviations at handover.')]:m.bullet(a,b,after=15,line=240)
m.job('Project and Workshop Manager','Ventek-Air · Copenhagen · Jan 2022–Nov 2022')
m.bullet('Team and projects','Led 14 people and managed 11 concurrent projects, including planning, subcontractors, safety documentation and handover.',after=15,line=240)
m.job('Maintenance and Operations Lead / Workshop Technician','BIOFOS, Lynetten · Copenhagen · Aug 2017–Jan 2022')
m.bullet('Operations','Electrical and mechanical maintenance, preventive work and fault-finding in a 24/7 environment.',after=15,line=240)
m.job('Electromechanic / Production Team Leader','ARJ Engineering · Tehran · Dec 2003–Mar 2010')
m.bullet('People and portfolio','Led 12 mechanics and technicians; product-portfolio responsibility including business cases, pricing and investment decisions.',after=15,line=240)
m.section('EDUCATION, METHODS & LANGUAGES')
for a,b in [('Bachelor (B.Tech), Technology Management and Mechanical Engineering','Copenhagen School of Marine Engineering & Technology Management · 2017–2022'),('Electrical & Mechanical Design, Electrical Engineering','Tehran Technical University · 2000–2003'),('PRINCE2 certified project manager','AXELOS / PeopleCert'),('Electrical authorisation as marine and technical engineer','Danish Safety Technology Authority · 2023')]:m.edu(a,b)
m.para('**Methods:** PRINCE2, Lean and Six Sigma applied in practice; certified in PRINCE2. **Tools:** Excel, SAP ERP and AI-assisted planning tools. **Languages:** Danish, English (professional) and Persian. **Location:** Måløv, Denmark.',after=20,line=235,justify=False)
m.save(str(R/'Shahram_Ajloo_JNJ_SiteContracting_EMEA.docx'))
