"""Baringa Nordic power market advisory: job-focused English application and CV."""
from pathlib import Path
from master_design import MasterDoc
R=Path(__file__).resolve().parent.parent
m=MasterDoc(str(R/'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='en-GB')
n='SHAHRAM AJLOO';t='Manager / Senior Manager | Power Market Advisory · Nordics & Baltics'
c='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'
m.header_banner(n,t,c);m.meta('Baringa · Markets & Transactions · Copenhagen',after=30)
m.para('**Application: Manager / Senior Manager, Power Market Advisory**',after=70,justify=False)
m.para('Dear Baringa hiring team,',after=65,justify=False)
m.para('An investment decision in the Nordic power sector depends on more than a single price forecast. The client needs to understand how market assumptions, the asset’s technical capabilities and commercial arrangements affect value — and which risks could change the outcome. Baringa’s combination of local presence, power-market modelling and transaction advice creates the opportunity to bring those questions together for developers, investors and lenders.',after=65,line=245,justify=False)
m.para('I would contribute technical and operational experience, project leadership and an analytical approach to a team working alongside Baringa’s power-market and transaction specialists. My priorities would be:',after=55,line=240,justify=False)
for a,b in [
('Make market assumptions useful to clients','For market entry and strategy work, agree the client’s decision and geography first. Combine research and stakeholder input with Baringa’s market insights; present assumptions, regulatory questions and areas of uncertainty clearly. Compare the implications of alternative scenarios rather than treating a central forecast as a guarantee.'),
('Connect asset performance to value','For renewable or flexible assets, work with specialists to test how capacity, availability, grid constraints and operating costs influence the commercial case. Assess standalone and co-located options on a consistent basis, and document the assumptions behind revenue perspectives and sensitivities.'),
('Support investment and due diligence','For buy- or sell-side reviews, structure the evidence around market exposure, contracts, technical dependencies and key risks. Bring the relevant specialists together to challenge assumptions and communicate the implications for investors and lenders, including for first-of-a-kind low-carbon projects.'),
('Deliver and develop the practice','Define the scope, ownership, timetable and review points with the client; turn analysis into concise recommendations. Support proposals and the Copenhagen team’s growth through relevant client conversations, and help colleagues develop through feedback and shared working methods.')]:m.bullet(a,b,after=30,line=240)
m.para('The experience behind this approach includes work in high-voltage substation automation and communications, technical operations at BIOFOS, and coordination of 25 specialists across 37 concurrent projects at Novo Nordisk. In ELOHVAC I combine customer delivery and full financial responsibility; AI-assisted planning tools contributed to a productivity improvement of over 40%. I also use investment models and sensitivity analysis to support business decisions.',after=55,line=245,justify=False)
m.para('Baringa’s people-first partnership and its Copenhagen office offer a strong setting for work that combines technical understanding with market expertise. I would welcome a conversation about how that combination could support clients through the energy transition.',after=40,line=245,justify=False)
m.meta('Yours sincerely · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com',after=0)
m.page_break();m.resume_header(n,t,c,'ENERGY, TECHNICAL DELIVERY & CLIENT ADVISORY')
m.para('Technical and operational leader with experience in electrical systems, critical infrastructure, project delivery and business management. Brings a practical view of asset operation and investment decisions, with professional English and Danish. Experienced in leading multidisciplinary teams and using data and AI-assisted tools to improve planning and delivery.',after=60,line=245,justify=False)
m.section('EXPERIENCE RELEVANT TO POWER MARKET ADVISORY')
for a,b in [
('Electrical networks and assets','Direct experience in high-voltage substation automation and communications, as well as 10/0.4 kV distribution networks. Practical application of IEC 61936 and EN 50522.'),
('Technical operations','BIOFOS/Lynetten: pumps, electrical systems, high-voltage panels, SCADA and preventive maintenance in critical 24/7 operations.'),
('Commercial and analytical work','Full P&L responsibility at ELOHVAC, including customer quotations and delivery. Experience using investment models and sensitivity analysis; product-portfolio responsibility and business cases at ARJ Engineering.'),
('Programme and people leadership','Coordinated 25 specialists across 37 concurrent projects at Novo Nordisk. Led 14 employees and 11 concurrent projects at Ventek-Air; five electricians and three apprentices at ELOHVAC.'),
('Digital improvement','AI-assisted tools for quotations, schedules and quality checks contributed to more than 40% productivity improvement at ELOHVAC. Practical use of PRINCE2, Lean and Six Sigma; PRINCE2 certified.')]:m.bullet(a,b,after=20,line=240)
m.models_table('CLIENT ADVISORY — PROPOSED APPROACH',('Client question','Work with Baringa specialists to'),[
('Market entry','Map market design, policy and stakeholders; compare opportunities, risks and local differences across the Nordics and Baltics.'),
('Revenue and valuation','Review wholesale power assumptions and asset-specific revenue drivers; test downside and upside sensitivities for renewable assets.'),
('Flexibility','Compare standalone and co-located flexibility options against technical constraints, commercial arrangements and exposure to market prices.'),
('Commercial due diligence','Structure buy- and sell-side evidence, identify material assumptions and technical dependencies, and communicate risks to investors and lenders.'),
('Practice growth','Develop clear proposals, share insights and coach colleagues, with client needs and delivery quality at the centre.')])
m.section('SELECTED RESULTS')
for a,b in [('Project delivery','Novo Nordisk: 37 concurrent projects, 25 specialists and zero critical deviations at handover.'),('Operational improvement','ELOHVAC: digital tools contributed to a productivity improvement of over 40%.'),('Team leadership','Ventek-Air: 14 employees and 11 concurrent projects; ELOHVAC: five electricians and three apprentices.')]:m.bullet(a,b,after=15,line=235)
m.page_break();m.section('PROFESSIONAL EXPERIENCE')
m.job('Owner / Technical Director / electrically authorised marine engineer','ELOHVAC ApS · Copenhagen · May 2023–present')
for a,b in [('Client delivery and business','Full P&L responsibility for technical services, quotations, cost estimates, subcontractors and quality documentation.'),('People and operations','Lead five electricians and three apprentices; plan delivery, development and safety across electrical, ventilation and climate systems.'),('Digital tools','Develop AI-assisted tools for quotations, schedules and quality checks; these contributed to a productivity improvement of over 40%.')]:m.bullet(a,b,after=15,line=240)
m.job('Co-owner and CTO / Head of AI','Data Power Consultant ApS · Copenhagen · 2024–Nov 2026')
m.bullet('Leadership and delivery','Led an AI department of 4–10 people and worked on technical applications from requirements through documentation and handover. The role ran alongside ELOHVAC; the company has ceased operations.',after=15,line=240)
m.job('Senior Commissioning Engineer / Project Manager, electrical systems','Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024')
for a,b in [('Multidisciplinary delivery','Coordinated 25 specialists on 37 concurrent CAPEX projects; monitored resources, cost, schedule and risk across engineering, procurement and site teams.'),('Quality and commissioning','FAT/SAT and IQ/OQ/PQ in a regulated environment, with zero critical deviations at handover. Work included panels, controls and UPS.')]:m.bullet(a,b,after=15,line=240)
m.job('Project and Workshop Manager','Ventek-Air · Copenhagen · Jan 2022–Nov 2022')
m.bullet('Execution','Led a team of 14 and managed 11 concurrent projects, including planning, subcontractors, safety documentation and handover.',after=15,line=240)
m.job('Maintenance and Operations Lead / Workshop Technician','BIOFOS, Lynetten · Copenhagen · Aug 2017–Jan 2022')
m.bullet('Critical operations','Worked with pumps, HVAC, high-voltage panels, SCADA, preventive maintenance and urgent fault-finding in a 24/7 environment.',after=15,line=240)
m.job('Electromechanic / Production Team Leader','ARJ Engineering · Tehran · Dec 2003–Mar 2010')
m.bullet('Leadership and portfolio','Led 12 technicians and mechanics; product-portfolio responsibility for an industrial line included business cases and investment decisions.',after=15,line=240)
m.section('EDUCATION, METHODS & LANGUAGES')
for a,b in [('B.Tech, Technology Management and Mechanical Engineering','Copenhagen School of Marine Engineering & Technology Management · 2017–2022'),('Electrical & Mechanical Design, Electrical Engineering','Tehran Technical University · 2000–2003'),('PRINCE2 certified project manager','AXELOS / PeopleCert'),('Electrical authorisation as marine and technical engineer','Danish Safety Technology Authority · 2023')]:m.edu(a,b)
m.para('**Methods:** PRINCE2, Lean and Six Sigma applied in practice; certified in PRINCE2. **Tools:** Excel, SAP ERP, SCADA and AI-assisted planning tools. **Languages:** Danish, English (professional) and Persian. **Location:** Måløv, Denmark.',after=20,line=235,justify=False)
m.page_break();m.models_table('FIRST 90 DAYS — PROPOSED PRIORITIES',('Period','Client and team priorities'),[
('Days 1–30','Meet the Copenhagen team and market specialists; understand Baringa’s modelling methods, client priorities and quality standards. Map where technical and operational experience supports current work.'),
('Days 30–60','Contribute to a scoped engagement with agreed responsibilities; review assumptions and risks with the appropriate market, commercial and technical specialists.'),
('Days 60–90','Help translate analysis into a decision-ready client deliverable; support a proposal or knowledge-sharing session and agree development priorities with the team.'),
('Ongoing','Build relationships across the Nordic and Baltic practice and use feedback from clients and colleagues to improve delivery.')])
m.section('WORKING WITH CLIENTS AND COLLEAGUES')
for a,b in [('Developers, investors and lenders','Clarify the investment question, evidence required, assumptions and the decisions the analysis must support.'),('Market and transaction specialists','Combine market modelling and commercial expertise with technical and operational input; review uncertainties together.'),('Junior colleagues','Share practical methods, agree responsibilities and provide regular feedback on delivery.')]:m.bullet(a,b,after=25,line=240)
m.save(str(R/'Shahram_Ajloo_Baringa_PowerMarketAdvisory.docx'))
