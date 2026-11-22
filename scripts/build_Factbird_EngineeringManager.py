"""Factbird people-focused Engineering Manager application and CV."""
from pathlib import Path
from master_design import MasterDoc
R=Path(__file__).resolve().parent.parent
m=MasterDoc(str(R/'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='en-GB')
n='SHAHRAM AJLOO'; t='Engineering Manager | People, AI & manufacturing insight'
c='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'
m.header_banner(n,t,c);m.meta('Factbird · Engineering Manager · Copenhagen',after=30)
m.para('**Application: Engineering Manager**',after=70,justify=False)
m.para('Dear Factbird hiring team,',after=60,justify=False)
m.para('A developer should know what is expected, have a trusted person to discuss obstacles with, and see a realistic route to growth. As Factbird scales its manufacturing intelligence platform, the Engineering Manager can make those conditions consistent without taking technical decisions away from Tech Leads and Architects.',after=55,line=245,justify=False)
m.para('My approach would begin with the people and build only the structure that helps them do better work:',after=45,line=240,justify=False)
for a,b in [
('Development and trust','Hold regular 1:1s to understand motivation, strengths, workload and blockers. Use the twice-yearly Individual Development Plan to agree a small number of goals, stretch opportunities and mentoring, and revisit progress between formal conversations. Partner with Tech Leads on technical growth while retaining accountability for the person’s overall development.'),
('Fair performance management','Set clear expectations and give specific, timely feedback. When performance falls short, listen to the individual, agree the gap and support needed, document an improvement plan and review progress at agreed dates with People & Culture. Recognise strong contributions as carefully as issues are addressed.'),
('Measures that start conversations','Combine team-level delivery, quality and wellbeing signals with context from developers, Product and Tech Leads. Share a concise view of trends, risks and recommendations with the Director of Engineering; avoid using a single metric or code volume as an individual ranking.'),
('Change and AI-assisted work','Agree with technical leaders what should change and why, test a small improvement, gather feedback and check adoption. AI can reduce routine work, but it also raises the importance of review, testing, data protection and the ability to explain decisions. Define skills and expectations with the team, not by assuming a tool makes expertise unnecessary.')]:m.bullet(a,b,after=25,line=240)
m.para('My background combines developer people-management responsibilities and Agile product work with product and design colleagues, technical leadership of a 4–10 person AI department at Data Power, and hands-on operational understanding from manufacturing environments. At ELOHVAC, AI-assisted planning and quality tools contributed to a productivity improvement of over 40%.',after=55,line=245,justify=False)
m.para('Factbird’s commitment to making production data useful on the shop floor, and its open, collaborative culture, make this a compelling opportunity to connect people development with a product that solves practical problems. I would welcome an interview to discuss the role.',after=40,line=245,justify=False)
m.meta('Yours sincerely · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com',after=0)
m.page_break();m.resume_header(n,t,c,'DEVELOPER LEADERSHIP, AI & PRACTICAL IMPROVEMENT')
m.para('People and technical leader with experience in developer development and performance, Agile product collaboration, AI-assisted work and industrial operations. Builds practical routines that connect individual growth, team delivery and customer outcomes.',after=55,line=245,justify=False)
m.section('EXPERIENCE RELEVANT TO FACTBIRD')
for a,b in [
('Developer people leadership','Experience of regular 1:1s, coaching, mentoring, career discussions, recruitment interviews, team placement, employment contracts, performance improvement and annual salary adjustments for developers.'),
('Technical and AI leadership','Co-owner and CTO responsible for a 4–10 person AI department at Data Power. Introduced AI-assisted code generation, review and testing standards; technical customer applications, LLM APIs and AI agents.'),
('Agile and product collaboration','Direct experience of Agile product development with product and design counterparts, and coordinating technical work around customer needs.'),
('Manufacturing and operations','Novo Nordisk: coordinated 25 specialists on 37 concurrent CAPEX projects in a regulated environment. BIOFOS: technical operations, SCADA and preventive maintenance. Understands the operational context in which reliable production information is useful.'),
('People and measurable improvement','Lead five electricians and three apprentices at ELOHVAC; previously led 14 people at Ventek-Air. AI-assisted planning and quality tools contributed to over 40% productivity improvement at ELOHVAC.')]:m.bullet(a,b,after=20,line=240)
m.models_table('PEOPLE LEADERSHIP AT FACTBIRD — PROPOSED APPROACH',('Focus','Practical action'),[
('1:1s and development','Support onboarding, understand each developer’s goals and blockers, and agree development actions with the individual and relevant Tech Lead.'),
('Performance and fairness','Set expectations; give specific feedback and early support. Document improvement actions and review dates with People & Culture.'),
('Organisation and Agile','Work with the Director, Tech Leads, Architects and Product on team needs; introduce small changes, review impact and retire unhelpful process.'),
('AI and capability','Agree safe AI use and review standards with technical leaders; build skills in verification, testing and explaining decisions.'),
('Metrics and reporting','Discuss delivery, quality and team health in context; report trends, risks and recommendations without reducing people to a score.')])
m.section('SELECTED RESULTS')
for a,b in [('AI and operations','Data Power: led an AI department of 4–10; ELOHVAC: AI-assisted tools contributed to over 40% productivity improvement.'),('Cross-functional delivery','Novo Nordisk: 25 specialists, 37 concurrent projects and zero critical deviations at handover.'),('Team leadership','ELOHVAC: five electricians and three apprentices; Ventek-Air: 14 people.')]:m.bullet(a,b,after=15,line=235)
m.page_break();m.section('PROFESSIONAL EXPERIENCE')
m.job('Owner / Technical Director / electrically authorised marine engineer','ELOHVAC ApS · Copenhagen · May 2023–present')
for a,b in [('People and delivery','Lead five electricians and three apprentices, including planning, individual development and safety; full P&L responsibility.'),('AI-assisted improvement','Develop tools for quotations, schedules and quality checks; these contributed to a productivity improvement of over 40%.')]:m.bullet(a,b,after=15,line=240)
m.job('Co-owner and CTO / Head of AI','Data Power Consultant ApS · Copenhagen · 2024–Nov 2026')
for a,b in [('AI team and applications','Led an AI department of 4–10 people; worked on customer-facing technical and industrial applications, including LLM APIs and AI agents.'),('Ways of working','Introduced AI-assisted coding, review and testing standards; used AI with professional review for technical design and management work. Role ran alongside ELOHVAC; the company has ceased operations.')]:m.bullet(a,b,after=15,line=240)
m.job('Senior Commissioning Engineer / Project Manager, electrical systems','Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024')
m.bullet('Cross-functional delivery','Coordinated 25 specialists across 37 concurrent CAPEX projects; FAT/SAT and IQ/OQ/PQ in a regulated environment, with zero critical deviations at handover.',after=15,line=240)
m.job('Project and Workshop Manager','Ventek-Air · Copenhagen · Jan 2022–Nov 2022')
m.bullet('People and projects','Led 14 people and managed 11 concurrent projects, including capacity planning and handover.',after=15,line=240)
m.job('Maintenance and Operations Lead / Workshop Technician','BIOFOS, Lynetten · Copenhagen · Aug 2017–Jan 2022')
m.bullet('Operations','Electrical and mechanical operations, preventive maintenance, SCADA and fault-finding in a 24/7 environment.',after=15,line=240)
m.job('Electromechanic / Production Team Leader','ARJ Engineering · Tehran · Dec 2003–Mar 2010')
m.bullet('Technical team','Led 12 mechanics and technicians; diagnosis and repair of industrial equipment.',after=15,line=240)
m.section('EDUCATION, METHODS & LANGUAGES')
for a,b in [('Bachelor (B.Tech), Technology Management and Mechanical Engineering','Copenhagen School of Marine Engineering & Technology Management · 2017–2022'),('Electrical & Mechanical Design, Electrical Engineering','Tehran Technical University · 2000–2003'),('PRINCE2 certified project manager','AXELOS / PeopleCert'),('Electrical authorisation as marine and technical engineer','Danish Safety Technology Authority · 2023')]:m.edu(a,b)
m.para('**Methods:** Agile product collaboration; PRINCE2, Lean and Six Sigma applied in practice, certified in PRINCE2. **Tools:** AI-assisted development and planning, Python, Claude API, Excel. **Languages:** Danish, English (professional) and Persian. **Location:** Måløv, Denmark.',after=20,line=235,justify=False)
m.save(str(R/'Shahram_Ajloo_Factbird_EngineeringManager.docx'))
