"""Philips Denmark commercial leadership application and CV, master format."""
from pathlib import Path
from master_design import MasterDoc
R=Path(__file__).resolve().parent.parent
m=MasterDoc(str(R/'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='en-GB')
n='SHAHRAM AJLOO';t='District and Country Leader | Health Systems · Denmark'
c='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'
m.header_banner(n,t,c);m.meta('Philips · Copenhagen · Job requisition 595336',after=30)
m.para('**Application: District and Country Leader – Denmark**',after=70,justify=False)
m.para('Dear Philips hiring team,',after=65,justify=False)
m.para('For Philips Health Systems in Denmark, sustainable growth depends on understanding healthcare customers’ priorities and bringing clinical, technical and commercial expertise together around them. The country leader must give the sales organisation clear direction, make performance visible and build trust with customers while aligning the Denmark playbook with the Nordic team.',after=65,line=245,justify=False)
m.para('I would approach that responsibility through a consistent commercial rhythm and close collaboration with the people who know the customers and the portfolio:',after=55,line=240,justify=False)
for a,b in [
('Commercial strategy and forecasting','Translate the country strategy into account priorities, revenue objectives and a regular pipeline review. Examine opportunity stage, customer decision process, risks, next actions and forecast assumptions with account owners. Use the review to identify where the team needs support and agree corrective actions when performance moves off plan.'),
('Customers and value','Meet healthcare stakeholders with the relevant clinical, product and service colleagues. Understand the customer’s clinical and operational priorities, procurement process and financial constraints before shaping a proposal. A value-based case should explain the expected benefits and costs, with clinical claims reviewed by the qualified experts.'),
('People and execution','Agree expectations and responsibilities with the commercial team, use regular coaching and feedback, and share what is working across accounts. Performance conversations should develop capability as well as resolve obstacles; clear decisions and follow-through create accountability without losing collaboration.'),
('Country leadership and the Nordics','Build the Denmark country playbook from customer insight, market conditions and the team’s assessment of opportunities. Align priorities, resources and risks with Nordic leaders, and maintain a regular dialogue between commercial, service and other local functions so customer commitments can be delivered.')]:m.bullet(a,b,after=30,line=240)
m.para('My background brings transferable commercial and leadership experience: full P&L responsibility and customer delivery in ELOHVAC, forecasting and contract follow-up in operations or service delivery, and leadership of technical teams. At Novo Nordisk I coordinated 25 specialists across 37 concurrent projects in a regulated environment. AI-assisted planning and quality tools at ELOHVAC contributed to a productivity improvement of over 40%.',after=55,line=245,justify=False)
m.para('Philips’ focus on improving lives through meaningful innovation and its emphasis on impact with care make customer outcomes, quality and integrity essential to commercial execution. I would welcome the opportunity to discuss how my experience can support the Danish organisation and its customers.',after=40,line=245,justify=False)
m.meta('Yours sincerely · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com',after=0)
m.page_break();m.resume_header(n,t,c,'COMMERCIAL LEADERSHIP, CUSTOMERS & EXECUTION')
m.para('Business and technical leader with experience in customer delivery, P&L responsibility, forecasting, contract follow-up and the development of technical teams. Combines structured operational and financial follow-up with cross-functional project leadership and experience working in regulated industry.',after=60,line=245,justify=False)
m.section('EXPERIENCE RELEVANT TO THE ROLE')
for a,b in [
('Commercial responsibility','ELOHVAC: full P&L responsibility, customer quotations, cost estimation, delivery and quality. Experience of forecasting and contract follow-up in operations or service delivery.'),
('People leadership','Lead five electricians and three apprentices at ELOHVAC; previously led 14 people at Ventek-Air. Experience of individual development, feedback and daily planning.'),
('Customer and stakeholder coordination','Experience of customer development and new business in technical services. At Novo Nordisk, coordinated 25 specialists across engineering, procurement and site functions on 37 concurrent projects.'),
('Financial and analytical decisions','Business cases and investment decisions in an industrial product portfolio at ARJ Engineering; practical use of investment models and sensitivity analysis.'),
('Digital improvement','AI-assisted tools for quotations, schedules and quality checks contributed to over 40% productivity improvement at ELOHVAC. PRINCE2 certified; Lean and Six Sigma applied in practice.')]:m.bullet(a,b,after=20,line=240)
m.models_table('DENMARK COMMERCIAL LEADERSHIP — PROPOSED APPROACH',('Priority','Practical action'),[
('Country playbook','Agree strategic account priorities, roles and opportunities with Denmark and Nordic leaders.'),
('Sales performance','Review pipeline, revenue forecast, customer decision milestones, risks and actions with account owners.'),
('Healthcare customers','Work with clinical, product and service colleagues to understand priorities and develop evidence-based value propositions.'),
('Team development','Set expectations, coach regularly and use feedback and performance discussions to strengthen execution.'),
('Delivery and integrity','Align commercial commitments with service capabilities, quality standards and appropriate clinical review.')])
m.section('SELECTED RESULTS')
for a,b in [('Business responsibility','ELOHVAC: full P&L responsibility; leadership of five electricians and three apprentices.'),('Cross-functional delivery','Novo Nordisk: 37 concurrent projects, 25 specialists and zero critical deviations at handover.'),('Operational improvement','ELOHVAC: AI-assisted tools contributed to a productivity improvement of over 40%.')]:m.bullet(a,b,after=15,line=235)
m.page_break();m.section('PROFESSIONAL EXPERIENCE')
m.job('Owner / Technical Director / electrically authorised marine engineer','ELOHVAC ApS · Copenhagen · May 2023–present')
for a,b in [('Commercial and financial responsibility','Full P&L responsibility, customer quotations, cost estimates, materials, subcontractors and quality documentation.'),('People and delivery','Lead five electricians and three apprentices; manage planning, individual development and safety in technical service delivery.'),('Digital improvement','Develop AI-assisted tools for quotations, schedules and quality checks; these contributed to a productivity improvement of over 40%.')]:m.bullet(a,b,after=15,line=240)
m.job('Co-owner and CTO / Head of AI','Data Power Consultant ApS · Copenhagen · 2024–Nov 2026')
m.bullet('Leadership and delivery','Led an AI department of 4–10 people and worked on technical applications from requirements to documentation and handover. The role ran alongside ELOHVAC; the company has ceased operations.',after=15,line=240)
m.job('Senior Commissioning Engineer / Project Manager, electrical systems','Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024')
for a,b in [('Cross-functional projects','Coordinated 25 specialists across 37 concurrent CAPEX projects, monitoring cost, progress, resources and risk across engineering, procurement and site teams.'),('Quality and handover','FAT/SAT and IQ/OQ/PQ in a regulated environment, with zero critical deviations at handover.')]:m.bullet(a,b,after=15,line=240)
m.job('Project and Workshop Manager','Ventek-Air · Copenhagen · Jan 2022–Nov 2022')
m.bullet('Team and delivery','Led 14 people and managed 11 concurrent projects, including capacity planning, subcontractors, safety documentation and handover.',after=15,line=240)
m.job('Maintenance and Operations Lead / Workshop Technician','BIOFOS, Lynetten · Copenhagen · Aug 2017–Jan 2022')
m.bullet('Technical operations','Worked with electrical and mechanical systems, preventive maintenance and fault-finding in a 24/7 environment.',after=15,line=240)
m.job('Electromechanic / Production Team Leader','ARJ Engineering · Tehran · Dec 2003–Mar 2010')
m.bullet('People and portfolio','Led 12 mechanics and technicians; held product-portfolio responsibility for an industrial line, including business cases, pricing and investment decisions.',after=15,line=240)
m.section('EDUCATION, METHODS & LANGUAGES')
for a,b in [('B.Tech, Technology Management and Mechanical Engineering','Copenhagen School of Marine Engineering & Technology Management · 2017–2022'),('Electrical & Mechanical Design, Electrical Engineering','Tehran Technical University · 2000–2003'),('PRINCE2 certified project manager','AXELOS / PeopleCert'),('Electrical authorisation as marine and technical engineer','Danish Safety Technology Authority · 2023')]:m.edu(a,b)
m.para('**Methods:** PRINCE2, Lean and Six Sigma applied in practice; certified in PRINCE2. **Tools:** Excel, SAP ERP and AI-assisted planning tools. **Languages:** Danish, English (professional) and Persian. **Location:** Måløv, Denmark.',after=20,line=235,justify=False)
m.page_break();m.models_table('FIRST 90 DAYS — PROPOSED PRIORITIES',('Period','Focus with the team and Nordic leaders'),[
('Days 1–30','Meet the commercial team, local functions and Nordic leaders. Review the country playbook, current customer priorities, pipeline, forecast and quality requirements.'),
('Days 30–60','Join customer conversations with clinical and product colleagues. Agree account priorities, forecast assumptions, accountabilities and a coaching rhythm.'),
('Days 60–90','Review progress against agreed measures, identify barriers and refine actions with account owners and Nordic leaders. Establish a practical follow-up cadence.'),
('Ongoing','Use customer and team feedback to improve execution; review growth opportunities alongside quality, integrity and delivery commitments.')])
m.section('WORKING ACROSS THE ORGANISATION')
for a,b in [('Commercial team','Provide clear expectations, feedback and support on account plans and complex opportunities.'),('Clinical, product and service colleagues','Develop credible value propositions and confirm customer commitments can be delivered safely and effectively.'),('Nordic and country leaders','Align on the Denmark playbook, performance, resources and cross-functional decisions.')]:m.bullet(a,b,after=25,line=240)
m.save(str(R/'Shahram_Ajloo_Philips_DistrictCountryLeader.docx'))
