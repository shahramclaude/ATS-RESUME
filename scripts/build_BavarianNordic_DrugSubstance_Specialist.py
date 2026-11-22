"""English role-focused CV for Bavarian Nordic Drug Substance Engineering Specialist."""
from pathlib import Path
from master_design import MasterDoc
R=Path(__file__).resolve().parent.parent
m=MasterDoc(str(R/'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='en-GB')
n='SHAHRAM AJLOO'; t='Engineering Specialist | Technical delivery & regulated manufacturing'
c='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'
m.resume_header(n,t,c,'TECHNICAL PROFILE & MOTIVATION')
m.meta('Bavarian Nordic · Kvistgaard · Drug Substance Manufacturing · JR101588',after=30)
m.para('Reliable vaccine manufacturing depends on equipment that works as intended, changes that are properly assessed and practical knowledge shared across teams. The opportunity to support Material & Sterile Operation brings together the work I value: solving technical problems, improving performance and coordinating engineering work in a regulated production setting.',after=60,line=245,justify=False)
m.para('Electrically authorised marine and technical engineer with a B.Tech in technology management and mechanical engineering. Experience includes commissioning electrical systems in pharmaceutical production, FAT/SAT and IQ/OQ/PQ under GMP at Novo Nordisk, technical maintenance and structured troubleshooting, as well as team and project leadership. My experience is centred on technical equipment and facilities rather than drug substance process ownership or CIP/SIP specialist work.',after=60,line=245,justify=False)
m.section('RELEVANT EXPERIENCE')
for a,b in [
('Equipment introduction and qualification','At Novo Nordisk, worked with FAT/SAT and IQ/OQ/PQ on electrical systems in a regulated production environment; coordinated specialists and engineering, procurement and site teams across 37 concurrent CAPEX projects. Zero critical deviations at handover.'),
('Troubleshooting and improvement','At BIOFOS, maintained electrical and mechanical systems including pumps, HVAC and SCADA in a 24/7 environment. At Novo Nordisk, applied structured problem-solving methods and a PDCA programme that reduced energy costs by 40%.'),
('Technical leadership and collaboration','Led 14 people at Ventek-Air and lead five electricians and three apprentices at ELOHVAC. Experience includes planning, supporting individual development, risk assessment and handover documentation.'),
('Industrial equipment and automation','Experience with electrical panels, controls and mechanical equipment; has led work involving industrial PLC and control systems. Would work with equipment owners on the interaction of process equipment, piping, valves, instrumentation and automation.'),
('Quality and safe work','GMP-related commissioning and qualification, risk assessment and documented handover. Practical Lean and Six Sigma methods include A3, 5 Whys and Ishikawa; PRINCE2 certified.')]:m.bullet(a,b,after=20,line=240)
m.models_table('HOW I WOULD SUPPORT DRUG SUBSTANCE OPERATIONS',('Priority','Proposed approach with the team'),[
('Process reliability','Work with Manufacturing, Engineering and Automation to understand recurring issues, assess risks and test improvements against production and quality needs.'),
('CIP/SIP systems','Work alongside established cleaning and sterilisation subject matter experts to understand process boundaries, equipment and approved strategies before suggesting changes.'),
('Equipment lifecycle','Coordinate specifications, supplier interfaces, FAT/SAT and qualification activities within assigned responsibilities; agree acceptance criteria and handover with Quality and equipment owners.'),
('Validation and transfer','Support the relevant experts with technical evidence for validation, PPQ or technology transfer; use approved procedures and decision authorities.'),
('Quality and capability','Escalate deviations, document technical findings and involve Quality on CAPAs, change control and inspection preparation; share learning with colleagues.')])
m.page_break();m.section('PROFESSIONAL EXPERIENCE')
m.job('Owner / Technical Director / electrically authorised marine engineer','ELOHVAC ApS · Copenhagen · May 2023–present')
for a,b in [('Technical delivery','Electrical installations, panels, controls, troubleshooting and preventive maintenance for business customers; planning, quality assurance and handover documentation.'),('People and improvement','Lead five electricians and three apprentices; risk assessments and safety. AI-assisted quotation, scheduling and quality tools contributed to over 40% productivity improvement.')]:m.bullet(a,b,after=15,line=240)
m.job('Co-owner and CTO / Head of AI','Data Power Consultant ApS · Copenhagen · 2024–Nov 2026')
m.bullet('Technical leadership','Led an AI department of 4–10 people working on technical customer applications, AI coding, LLM APIs and AI agents. Applied AI to technical design and leadership with professional review. Alongside ELOHVAC; the company has ceased operations.',after=15,line=240)
m.job('Senior Commissioning Engineer / Project Manager, electrical systems','Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024')
for a,b in [('Commissioning and quality','FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA on electrical systems; zero critical deviations at handover.'),('Cross-functional delivery','Coordinated 25 specialists on 37 concurrent CAPEX projects, tracking progress, costs, resources and risks across engineering, procurement and site teams.'),('Improvement','Used A3, 5 Whys and Ishikawa for troubleshooting; a PDCA programme reduced energy costs by 40%.')]:m.bullet(a,b,after=15,line=240)
m.job('Project and Workshop Manager','Ventek-Air · Copenhagen · Jan 2022–Nov 2022')
m.bullet('Projects and team','Led 14 people and managed 11 concurrent projects from specification to handover, including subcontractors and safety documentation.',after=15,line=240)
m.job('Maintenance and Operations Lead / Workshop Technician','BIOFOS, Lynetten · Copenhagen · Aug 2017–Jan 2022')
m.bullet('Technical operations','Electrical and mechanical maintenance, including pumps, HVAC, high-voltage panels and SCADA; preventive maintenance and acute fault-finding in 24/7 operations.',after=15,line=240)
m.job('Electromechanic / Production Team Leader','ARJ Engineering · Tehran · Dec 2003–Mar 2010')
m.bullet('Industrial equipment','Fault diagnosis and repair of electrical and mechanical equipment; led 12 mechanics and technicians.',after=15,line=240)
m.section('EDUCATION, METHODS & LANGUAGES')
for a,b in [('Bachelor (B.Tech), Technology Management and Mechanical Engineering','Copenhagen School of Marine Engineering & Technology Management · 2017–2022'),('Electrical & Mechanical Design, Electrical Engineering','Tehran Technical University · 2000–2003'),('Electrical authorisation as marine and technical engineer','Danish Safety Technology Authority · 2023'),('PRINCE2 certified project manager','AXELOS / PeopleCert')]:m.edu(a,b)
m.para('**Methods:** Lean, Six Sigma and PDCA applied in practice; certified in PRINCE2. **Languages:** Danish, English (professional) and Persian. **Location:** Måløv, Denmark.',after=20,line=235,justify=False)
m.save(str(R/'Shahram_Ajloo_BavarianNordic_DrugSubstance_Specialist_CV.docx'))
