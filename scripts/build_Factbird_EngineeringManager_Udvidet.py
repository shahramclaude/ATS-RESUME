"""Expanded Factbird application and CV using the verified master and resume audit."""
from pathlib import Path
from master_design import MasterDoc
R=Path(__file__).resolve().parent.parent
N='SHAHRAM AJLOO';T='Engineering Manager | People, AI & manufacturing insight'
C='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'
def make(include_letter,output):
 m=MasterDoc(str(R/'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='en-GB')
 if include_letter:
  m.header_banner(N,T,C);m.meta('Factbird · Engineering Manager · Copenhagen',after=30)
  m.para('**Application: Engineering Manager**',after=70,justify=False)
  m.para('Dear Factbird hiring team,',after=60,justify=False)
  m.para('Factbird gives manufacturers a clearer picture of what happens on the shop floor. Engineering needs the same clarity about its people: what each developer is working towards, what is getting in the way, and how the organisation can help. The new Engineering Manager role can create that clarity while Tech Leads and Architects retain ownership of technical direction.',after=55,line=245,justify=False)
  m.para('I would focus the role on four practical commitments:',after=45,line=240,justify=False)
  for a,b in [
   ('Give every developer a useful development conversation','Use regular 1:1s to understand strengths, motivation, workload and blockers. Translate the twice-yearly Individual Development Plan into specific learning goals, mentoring and stretch assignments; revisit progress between reviews. Work with Tech Leads on technical coaching while keeping responsibility for each person’s overall development.'),
   ('Make performance management fair and actionable','Agree expectations and give specific feedback early. If performance falls short, listen, identify the gap, agree support and an improvement plan, document decisions and review progress at agreed intervals with People & Culture. Recognise good work and apply the same care and consistency across the group.'),
   ('Use measures to support judgement','Review team delivery, quality and wellbeing signals with developers, Product and Tech Leads. Discuss trends and obstacles rather than ranking people by code volume. Give the Director of Engineering a concise picture of progress, risks, capacity and recommendations.'),
   ('Bring people through change','Agree the purpose and ownership of a change with Engineering leadership, explain it to the teams, test it on a small scale and review adoption. As AI-assisted development evolves, build skill in verification, review, testing and responsible data use rather than assuming tools replace engineering judgement.')]:m.bullet(a,b,after=25,line=240)
  m.para('The experience behind this approach spans developer 1:1s, coaching, recruitment and performance improvement, as well as Agile product work with product and design colleagues. At Data Power, I led an AI department of 4–10 and introduced AI-assisted coding, review and testing standards. At ELOHVAC, AI tools for planning and quality contributed to a productivity improvement of over 40%. Manufacturing and regulated project work add an understanding of the environment Factbird serves.',after=55,line=245,justify=False)
  m.para('Factbird’s emphasis on ownership, customer understanding and open collaboration makes this an opportunity to connect people development with a product that helps manufacturing teams act. I would welcome an interview to discuss how to build that support for your developers.',after=40,line=245,justify=False)
  m.meta('Yours sincerely · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com',after=0)
  m.page_break()
 m.resume_header(N,T,C,'ENGINEERING LEADERSHIP PROFILE')
 m.para('People and technical leader with experience developing employees, coordinating multidisciplinary delivery and building AI-assisted ways of working. Combines developer leadership and Agile product collaboration with industrial operations, customer delivery, financial accountability and continuous improvement. Brings an understanding of the manufacturing environment behind Factbird’s real-time data and its users’ need for clear, actionable information.',after=60,line=245,justify=False)
 m.section('LEADERSHIP COMPETENCIES FOR FACTBIRD')
 for a,b in [
 ('Developer development and performance','Experience of developer 1:1s, coaching, mentoring and career conversations; recruitment interviews, team placement, employment contracts, performance improvement and annual salary adjustments. Focus on clear expectations, useful feedback and follow-up.'),
 ('People leadership and team development','Personnel leadership of five electricians and three apprentices at ELOHVAC, 14 people at Ventek-Air and 12 mechanics and technicians at ARJ. Direct personnel responsibility has also included team leaders or middle managers who led staff.'),
 ('Technical and AI leadership','Led a Data Power AI and AI-coding department of 4–10. Experience of customer requirements, AI-assisted coding, LLM APIs and agents, review and testing, professional validation of output, technical applications and handover.'),
 ('Agile and cross-functional collaboration','Direct Agile product development with product and design counterparts. Coordinate priorities and interfaces across technical, operational and customer stakeholders; align people ownership with technical expertise.'),
 ('Change and improvement','Practical Lean and Six Sigma methods to identify bottlenecks, investigate causes and improve workflows. Experience includes daily huddles and standardised work at Ventek-Air, and PDCA in technical operations.'),
 ('Planning, decisions and commercial control','Full P&L, quotations, resources, subcontractors and customer delivery at ELOHVAC; general experience of forecast and contract follow-up. Use KPIs and performance metrics, risk assessment, stakeholder analysis and structured reporting to support decisions.')]:m.bullet(a,b,after=25,line=240)
 m.section('LEADERSHIP METHODS & TOOLS — APPLIED IN PRACTICE')
 for a,b in [
 ('Developing people','Situational leadership, GROW and SBI, 1:1s, development conversations, feedback, delegation and competence mapping; attention to psychological safety and clear accountability.'),
 ('Project and team coordination','PRINCE2, matrix leadership, RACI, stakeholder analysis, visual management, daily huddles, escalation and 30–60–90-day planning. PRINCE2 is certified.'),
 ('Continuous improvement','Lean and Six Sigma methods including DMAIC, 5S, Kaizen, PDCA, A3, value-stream mapping, Standard Work, 5 Whys, Ishikawa and FMEA; methods are applied in practice, not certified.'),
 ('Digital decision support','Excel, Power BI, SAP ERP, CMMS, Python and Claude API; AI-assisted reporting, decision briefs, meeting summaries, KPI analysis and technical design with professional review.')]:m.bullet(a,b,after=20,line=240)
 m.page_break();m.section('PROFESSIONAL EXPERIENCE — LEADERSHIP & AI')
 m.job('Owner / Technical Director / electrically authorised marine engineer','ELOHVAC ApS · Copenhagen · May 2023–present')
 for a,b in [
 ('People and operating rhythm','Lead five electricians and three apprentices; coordinate daily work, 1:1s, development conversations, structured learning and safety across changing worksites.'),
 ('Business and delivery','Full P&L responsibility for customer quotations, cost estimation, materials, subcontractors, quality and handover documentation. Coordinate electrical, ventilation and climate work from planning to delivery.'),
 ('AI and measurable productivity','Develop AI-assisted quotation, scheduling, quality-check and KPI tools using Python and Claude API. These tools contributed to a productivity improvement of over 40%.'),
 ('Quality and risk','Use risk assessment and LOTO alongside operational follow-up. Manage customer commitments and balance capacity, safety and delivery.')]:m.bullet(a,b,after=20,line=240)
 m.job('Co-owner and CTO / Head of AI and AI coding','Data Power Consultant ApS · Copenhagen · 2024–Nov 2026')
 for a,b in [
 ('Organisation and people','Led an AI department of 4–10 people. Set priorities across the department and coordinated parallel commitments with ELOHVAC using a shared plan and written priorities.'),
 ('Technical and industrial customer applications','Worked from requirements and architecture through data modelling, integration and commissioning, followed by documentation and handover to customer operations.'),
 ('AI-assisted development','Introduced code generation, review and testing practices with shared acceptance standards for AI output. Worked with LLM APIs and AI agents on customer solutions, from process mapping through implementation.'),
 ('Engineering design and management support','Used AI coding for calculations, sizing and design variants for technical systems and industrial components, with professional validation. Applied AI to management reporting, decision briefs, meeting summaries and KPI analysis.'),
 ('Context','The Data Power role ran alongside ELOHVAC. The company has ceased operations.')]:m.bullet(a,b,after=20,line=240)
 m.section('DEVELOPER & PRODUCT LEADERSHIP — EXPERIENCE ACROSS ROLES')
 for a,b in [
 ('People management','Regular 1:1s, coaching and mentoring; career discussions, recruitment interviews, team placement, employment contracts, performance improvement and annual salary adjustments for developers.'),
 ('Agile product work','Direct participation in Agile product development with product and design counterparts; collaboration across skills and priorities to support usable solutions.')]:m.bullet(a,b,after=20,line=240)
 m.page_break();m.section('PROFESSIONAL EXPERIENCE — OPERATIONS & DELIVERY')
 m.job('Senior Commissioning Engineer / Project Manager, electrical systems','Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024')
 for a,b in [
 ('Cross-functional delivery','Coordinated 25 specialists across 37 concurrent CAPEX projects, each DKK 2–10 million, with progress, cost, resource and risk follow-up across engineering, procurement and site teams.'),
 ('Quality in a regulated environment','FAT/SAT and IQ/OQ/PQ for electrical systems under GMP/FDA/EMA; zero critical deviations at handover. Worked with technical documentation and reporting to management and client.'),
 ('Evidence-led improvement','Used A3, 5 Whys and Ishikawa for troubleshooting; a PDCA programme reduced energy costs by 40%. SAP ERP supported financial, asset and cost follow-up.')]:m.bullet(a,b,after=20,line=240)
 m.job('Project and Workshop Manager','Ventek-Air · Copenhagen · Jan 2022–Nov 2022')
 for a,b in [
 ('Team and capacity','Led 14 people and managed 11 concurrent projects from specification to formal handover; planned capacity, resources and progress across the portfolio.'),
 ('Delivery routines','Used daily huddles, bottleneck analysis and standardised workflows; coordinated subcontractors, tendering, agreements, safety documentation and handover packages.')]:m.bullet(a,b,after=20,line=240)
 m.job('Maintenance and Operations Lead / Workshop Technician','BIOFOS, Lynetten · Copenhagen · Aug 2017–Jan 2022')
 for a,b in [('Operational context','Electrical and mechanical operations, pumps, HVAC, high-voltage panels and SCADA; preventive maintenance and acute troubleshooting in a 24/7 environment.'),('Standard work and safety','Applied 5S, Standard Work and PDCA in workshop and stock flow; worked with LOTO, risk assessment and safe shift operations.')]:m.bullet(a,b,after=20,line=240)
 m.job('Electromechanic / Production Team Leader','ARJ Engineering · Tehran · Dec 2003–Mar 2010')
 for a,b in [('Team leadership','Led 12 mechanics and technicians, with shift planning, materials, targets and technical problem-solving.'),('Product and business decisions','Product-portfolio responsibility for a line of motors and pumps, including roadmap, business cases, development and launch, pricing, margin and investment decisions.')]:m.bullet(a,b,after=20,line=240)
 m.section('SELECTED RESULTS')
 for a,b in [('Productivity','ELOHVAC: more than 40% improvement supported by AI-assisted tools.'),('Quality and resources','Novo Nordisk: zero critical deviations at handover and 40% lower energy costs via a PDCA programme.'),('Scale and coordination','25 specialists and 37 concurrent projects at Novo Nordisk; 14 people and 11 concurrent projects at Ventek-Air.')]:m.bullet(a,b,after=15,line=235)
 m.page_break();m.section('EDUCATION, QUALIFICATIONS & LANGUAGES')
 for a,b in [('Bachelor (B.Tech), Technology Management and Mechanical Engineering','Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · EQF 6'),('Electrical & Mechanical Design, Electrical Engineering','Tehran Technical University · 2000–2003'),('Electrical authorisation as marine and technical engineer, LV/MV/HV','Danish Safety Technology Authority · May 2023'),('PRINCE2 certified project manager','AXELOS / PeopleCert'),('Refrigeration and air conditioning','Mercantec · AMU · 2021'),('HF, mathematics and physics','VUC · 2012–2017'),('STCW maritime safety and engineering courses','Danish Maritime Authority · 2021–2023')]:m.edu(a,b)
 m.para('**Languages:** Danish and Persian (native); English (professional). **Driving licence:** B. **Location:** Måløv, Denmark.',after=40,line=240,justify=False)
 m.models_table('FACTBIRD — PROPOSED FIRST 90 DAYS',('Period','Priorities and outputs'),[
 ('Days 1–30','Meet each developer for a 1:1 and listen to Tech Leads, Architects, Product and People & Culture. Map responsibilities, development goals, existing review cycles and the main delivery and team-health concerns.'),
 ('Days 30–60','Agree expectations and development actions with individuals and technical partners. Review onboarding, feedback, Agile routines and available measures; establish a concise baseline and identify one or two improvements to trial.'),
 ('Days 60–90','Review feedback and adoption with developers and leadership. Refine development plans and escalation routes; share a contextual view of team health, delivery risks and recommendations with the Director of Engineering.'),
 ('Ongoing','Work with technical leaders on responsible AI use, verification and new skills. Use individual and team signals for conversations and support, not a single ranking or code-volume target.')])
 m.section('PARTNERSHIPS AND LEADERSHIP RHYTHM')
 for a,b in [('Developers','Maintain regular, confidential 1:1s; recognise contributions, remove obstacles and track agreed development actions.'),('Tech Leads, Architects and Product','Clarify the boundary between people and technical decisions; connect technical coaching, product priorities and team capacity.'),('People & Culture and Director of Engineering','Apply consistent, fair employment practices and performance support; share proportionate, actionable information and recommendations.')]:m.bullet(a,b,after=20,line=240)
 m.save(str(R/output))
make(True,'Shahram_Ajloo_Factbird_EngineeringManager_Udvidet.docx')
make(False,'Shahram_Ajloo_Factbird_EngineeringManager_CV_Udvidet.docx')
