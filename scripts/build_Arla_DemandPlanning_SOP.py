"""Arla RoW demand planning and S&OP application, English master format."""
from pathlib import Path
from master_design import MasterDoc
R=Path(__file__).resolve().parent.parent
m=MasterDoc(str(R/'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='en-GB')
n='SHAHRAM AJLOO';t='Senior Manager, Demand Planning & S&OP | Arla Foods'
c='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'
m.header_banner(n,t,c);m.meta('Arla Foods · Ionut Ciobanoiu, Director · Ref. 111863',after=35)
m.para('**Application: Senior Manager, Demand Planning & S&OP**',after=70,justify=False)
m.para('Dear Ionut Ciobanoiu,',after=65,justify=False)
m.para('A reliable regional demand outlook gives Arla a practical basis for balancing growth, service and the value created from its farmers’ milk. Across Rest of World, that means connecting local market insight with supply and financial decisions without taking ownership of forecasts away from the markets. I would establish a planning rhythm that makes assumptions visible, tests the alternatives and brings clear decisions to the right forum.',after=75,line=250,justify=False)
for a,b in [
('Planning standards and market ownership','Agree a common calendar, submission requirements and performance measures with Global S&OP and the markets. Each market retains its local forecast and explains material changes; the regional view consolidates assumptions and highlights missing inputs and decisions.'),
('A demand outlook that supports decisions','Keep unconstrained demand, financial ambition and the supply-constrained plan distinct. Review movements by market and relevant product group, explain the main drivers and reconcile material gaps with Commercial, Sales, Supply Chain and Finance.'),
('Demand Review and regional S&OP','Use the Demand Review to challenge assumptions and identify risks and opportunities. For regional S&OP, prepare quantified options with the impact on volume, value, service, inventory and capacity, together with financial implications, an owner and a recommended decision.'),
('Transformation, data and adoption','Begin with a baseline of process quality, data and capabilities across markets. Agree a prioritised roadmap with Global S&OP, test improvements with users and scale what works. My experience is in SAP ERP; I would build the role-specific SAP IBP understanding with the planning teams as part of that work.'),
('Alignment without formal authority','Work with General Managers and functional leaders to resolve differences in assumptions, document decisions and follow through on actions. A common framework must leave room for local market conditions while giving the region a consistent view.')]:m.bullet(a,b,after=40,line=245)
m.para('The transferable foundation is practical: forecasting and operational follow-up, full financial responsibility in ELOHVAC, and coordination of 25 specialists across 37 concurrent projects at Novo Nordisk. Digital planning tools in ELOHVAC contributed to a productivity improvement of more than 40%. This experience supports a disciplined approach to data, capacity, financial trade-offs and delivery across functions.',after=55,line=245,justify=False)
m.para('Arla’s farmer-owned model and emphasis on collaboration make the quality of these decisions important beyond the planning cycle. I would welcome the opportunity to discuss how a shared regional process can strengthen decisions while respecting market ownership.',after=50,line=245,justify=False)
m.meta('Yours sincerely',after=10);m.meta('Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com',after=0)
m.page_break();m.resume_header(n,t,c,'PLANNING, BUSINESS PERFORMANCE & CROSS-FUNCTIONAL LEADERSHIP')
m.para('Operations and technical leader with experience in forecasting, financial responsibility, capacity planning and cross-functional project delivery. Background includes SAP ERP, data-supported improvement and leading specialists in regulated industry. Brings a practical approach to decision preparation, disciplined follow-up and building working processes with the people who use them.',after=60,line=245,justify=False)
m.section('RELEVANT EXPERIENCE FOR THE ROLE')
for a,b in [
('Planning and forecasting','Experience with forecasting and operational follow-up. At Ventek-Air, planned capacity across 11 concurrent projects; at Novo Nordisk, coordinated resources and progress across 37 projects.'),
('Financial and commercial decisions','Full profit-and-loss responsibility in ELOHVAC, including quotations, costs, materials and subcontractors. Experience of business cases and investment decisions in an industrial product portfolio.'),
('Stakeholder alignment','Coordinated 25 specialists across engineering, procurement and site work at Novo Nordisk. Experience working across functions to agree priorities and follow up on risks and delivery.'),
('Process improvement and data','Practical use of Lean, Six Sigma and PDCA. AI-assisted tools for quotations, schedules and quality checks contributed to a productivity improvement of more than 40% at ELOHVAC.'),
('Systems','SAP ERP experience at Novo Nordisk; Excel and digital planning tools. Further development in SAP IBP can support the proposed planning process.')]:m.bullet(a,b,after=20,line=240)
m.models_table('REGIONAL PLANNING — PROPOSED WORKING APPROACH',('Focus','Practical output'),[
('Market inputs','Common calendar, documented assumptions and accountable market owners for each forecast.'),
('Demand outlook','Consolidated market view showing unconstrained demand, financial ambition and the supply-constrained plan separately.'),
('Decision preparation','Demand Review identifies material changes; regional S&OP receives quantified options, financial implications and recommended actions.'),
('Performance','Agree definitions and review forecast accuracy, bias and data completeness with the markets and Global S&OP.'),
('Capability','Baseline processes and tools, prioritise improvements and support adoption with markets and functional partners.')])
m.section('SELECTED EXPERIENCE AND RESULTS')
for a,b in [('Financial responsibility','ELOHVAC: full P&L responsibility and leadership of five electricians and three apprentices.'),('Cross-functional delivery','Novo Nordisk: coordination of 25 specialists on 37 concurrent projects; zero critical deviations at handover.'),('Capacity and execution','Ventek-Air: led 14 people and managed 11 concurrent projects.'),('Digital improvement','ELOHVAC: planning and quality tools contributed to a productivity improvement of more than 40%.')]:m.bullet(a,b,after=15,line=235)
m.page_break();m.section('PROFESSIONAL EXPERIENCE')
m.job('Owner / Technical Director','ELOHVAC ApS · Copenhagen · May 2023–present')
for a,b in [('Business management','Full P&L responsibility, quotations, cost estimation, materials, subcontractors and quality documentation.'),('Team and capacity','Lead five electricians and three apprentices; plan work, resources, development and safety.'),('Digital improvement','Develop AI-assisted tools for quotations, schedules and quality checks; these contributed to a productivity improvement of more than 40%.')]:m.bullet(a,b,after=15,line=240)
m.job('Co-owner and CTO / Head of AI','Data Power Consultant ApS · Copenhagen · 2024–Nov 2026')
m.bullet('Technology and delivery','Led an AI department of 4–10 people and worked on technical applications from requirements to documentation and handover. The role ran alongside ELOHVAC; the company has ceased operations.',after=15,line=240)
m.job('Senior Commissioning Engineer / Project Manager, electrical systems','Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024')
for a,b in [('Portfolio coordination','Coordinated 25 specialists across 37 concurrent CAPEX projects, following progress, cost, risks and resources across engineering, procurement and site teams.'),('Systems and quality','Used SAP ERP for financial and cost follow-up. Supported FAT/SAT and IQ/OQ/PQ in a regulated environment, with zero critical deviations at handover.')]:m.bullet(a,b,after=15,line=240)
m.job('Project and Workshop Manager','Ventek-Air · Copenhagen · Jan 2022–Nov 2022')
m.bullet('Capacity and delivery','Led a team of 14 and managed 11 concurrent projects, including resource planning, subcontractors, agreements and handover.',after=15,line=240)
m.job('Maintenance and Operations Lead / Workshop Technician','BIOFOS, Lynetten · Copenhagen · Aug 2017–Jan 2022')
m.bullet('Operations and maintenance','Worked with electrical and mechanical systems, pumps, SCADA and preventive maintenance in a 24/7 environment; supported stock flow and continuous improvement.',after=15,line=240)
m.job('Electromechanic / Production Team Leader','ARJ Engineering · Tehran · Dec 2003–Mar 2010')
m.bullet('Production and commercial responsibility','Led 12 technicians and mechanics, with shift and materials planning. Held product-portfolio responsibility for an industrial line, including business cases and investment decisions.',after=15,line=240)
m.section('EDUCATION, METHODS & LANGUAGES')
for a,b in [('B.Tech, Technology Management and Mechanical Engineering','Copenhagen School of Marine Engineering & Technology Management · 2017–2022'),('Electrical & Mechanical Design, Electrical Engineering','Tehran Technical University · 2000–2003'),('PRINCE2 certified project manager','AXELOS / PeopleCert'),('Authorised marine and technical engineer, electrical','Danish Safety Technology Authority · 2023')]:m.edu(a,b)
m.para('**Methods:** PRINCE2, Lean and Six Sigma applied in practice; certified in PRINCE2. **Languages:** English (professional), Danish and Persian. **Location:** Måløv, Denmark.',after=20,line=240,justify=False)
m.page_break();m.models_table('FIRST 90 DAYS — PROPOSED PRIORITIES',('Period','Focus'),[
('Days 1–30','Meet market and functional stakeholders; map the current planning calendar, forecast ownership, data quality, system landscape and decision forums.'),
('Days 30–60','Agree definitions, submission requirements and a baseline with Global S&OP and markets. Identify the most material gaps between demand, supply and financial ambition.'),
('Days 60–90','Pilot a decision-ready Demand Review and regional S&OP pack with quantified options. Agree a prioritised roadmap, training needs and measures for adoption.'),
('Beyond 90 days','Review effectiveness with markets and functions, improve the process and scale changes based on evidence and local feedback.')])
m.section('WORKING ACROSS THE MATRIX — PROPOSED PARTNERSHIPS')
for a,b in [('Markets and General Managers','Retain local ownership of forecasts; align assumptions, identify risks and clarify regional decisions.'),('Commercial and Sales','Explain drivers of demand, market opportunities and material forecast changes.'),('Supply Chain and Finance','Assess capacity and supply constraints alongside service, inventory, value and financial implications.'),('Global S&OP','Align standards, KPIs, system practices and the capability roadmap; support market adoption.')]:m.bullet(a,b,after=25,line=240)
m.save(str(R/'Shahram_Ajloo_Arla_DemandPlanning_SOP.docx'))
