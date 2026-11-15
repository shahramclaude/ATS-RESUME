"""Tailored LEGO Engineering Management System application; evidence from master CV."""
import os
from master_design import MasterDoc
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME='SHAHRAM AJLOO'
TITLE='Engineering management systems · process development and digital enablement'
CONTACT='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'
def build(path):
    m=MasterDoc(os.path.join(ROOT,'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='en-GB')
    m.header_banner(NAME,TITLE,CONTACT)
    m.meta('4 November 2026')
    m.meta('The LEGO Group · Manager, Engineering Management System Development · Job ID 0000039738 · Billund')
    p=m._p(spacing_after=80,line=260,justify=False); m._run(p,'Application: Engineering Management System Development',bold=True,color='1A1A1A')
    def lp(t): m.para(t,after=36,line=235)
    lp('**A process has two owners: the person named on the page and the person who must use it on a busy day.** If they cannot recognise the same work, the management system has an interface problem. The solution is not another document; it is a clear decision about ownership, an understandable route through the work and a way to learn when the route fails.')
    lp('LEGO is developing an **Engineering Management System** that connects governance, processes, standards, performance and knowledge. The opportunity is to translate the **Engineering Delivery System** into practical guidance that engineering teams trust and use. I would bring experience from 37 capital projects at Novo Nordisk, technical operations at Biofos and the processes I have built in my own engineering and AI businesses.')
    lp('**From need to trusted practice.** First, listen to the people doing the work and the process owner: where does an engineer need a decision, where does work pass to another team, and what evidence is already available? Then map the interface and agree ownership. Develop a proportionate process, standard or template with its users; test it on actual work; and assign a review date before publishing it. A **transparent improvement backlog** makes the decisions and dependencies visible.')
    lp('At ELOHVAC, I rebuilt workflows around AI-assisted estimating, schedules, quality checklists and KPI reporting; the documented productivity improvement was **over 40%**. At Novo Nordisk, I coordinated 25 specialists across 37 simultaneous capital projects under GMP/FDA/EMA requirements, with zero critical deviations at handover. At Data Power, I led an AI and AI-coding department and introduced shared standards for reviewing and testing AI-generated output. These are different scales of system, but the common task is making responsibilities and evidence usable in daily work.')
    lp('I would work with the Management System Lead on priorities and governance and with the Management System Lead Professional on digital enablement, not duplicate either role. My contribution would be to translate stakeholder needs into requirements for workflows, automation, reporting and knowledge structures, agree changes with process owners and specialists, and follow up on whether they reduce duplication and local workarounds.')
    lp('My experience is strongest in technical operations, regulated projects and developing practical processes within smaller organisations. I have not led an enterprise-wide engineering management system transformation; nor should my experience be read as expertise in named platforms such as SharePoint, Confluence, Jira or Power BI. I have applied Lean and Six Sigma methods in practice and am PRINCE2 certified. For AI, I would agree access, review and human validation with the relevant owners before deploying a solution.')
    lp('The LEGO Group describes a system that is **coherent, practical, trusted and actively used**. That is the standard I would use: not simply how many documents are published, but whether users can find the right version, understand the interface and know who can change it. I am based in Måløv and open to relocating to the Billund area. I work in Danish and English and would welcome a conversation about the team’s priorities.')
    m.meta('Kind regards',after=6); m.meta('Shahram Ajloo',after=0)
    m.page_break(); m.resume_header(NAME,TITLE,CONTACT,'PROFILE')
    m.para('Engineering and operations leader connecting process, people and digital tools. Authorised Danish maskinmester (LV/MV/HV); B.Tech in Technology Management and Mechanical Engineering; PRINCE2 certified. Experience includes 37 concurrent capital projects, 25 specialists, regulated handover and AI-assisted process improvement with over 40% productivity gain. Lean and Six Sigma applied in practice, not certified.',after=45)
    m.section('THE INTERFACE — HOW I DEVELOP A PROCESS')
    for label,body in [
      ('Need and owner','Listen to users and process owners; clarify the outcome, decision rights and where work crosses a team boundary.'),
      ('Standard and guidance','Turn a requirement into a practical sequence, checklist or template; distinguish mandatory controls from useful guidance.'),
      ('Evidence and feedback','Agree a baseline, collect feedback from users and use reporting to identify duplication, workarounds and unclear ownership.'),
      ('Change and lifecycle','Put improvement opportunities in a backlog, agree a priority and owner, then review whether the change works in practice.')]: m.bullet(label,body,after=12)
    m.section('EXPERIENCE')
    jobs=[
      ('Owner / Technical Director','ELOHVAC ApS · Copenhagen · May 2023–present','8 employees including 3 apprentices · full P&L', [('Process and digital tools','Developed AI-assisted estimating, schedules, quality checklists and KPI dashboards; documented productivity improvement of over 40%.'),('Delivery and people','Lead electricians and apprentices; coordinate planning, subcontractors, quality assurance and handover documentation for electrical and HVAC work.')]),
      ('Co-owner and CTO / Technical Lead, AI department','Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 · alongside ELOHVAC','4–10 people · company ceased in November 2026', [('AI and governance','Led AI and AI-coding delivery, introducing shared standards for code review, testing and acceptance of AI output.'),('User requirements to go-live','Translated customer requirements into technical and industrial applications, integration and documentation so customer teams could take over operations.')]),
      ('Senior Commissioning Engineer / Project Manager, electrical systems','Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024','37 concurrent CAPEX projects · 25 specialists · GMP/FDA/EMA', [('Governance and delivery','Coordinated engineering, procurement and construction; tracked progress, budgets, risks and resources across projects of DKK 2–10 million each.'),('Evidence and quality','Worked with FAT/SAT and IQ/OQ/PQ in a regulated environment; zero critical deviations at handover. Monthly reporting to management and client.')]),
      ('Project and Workshop Manager','Ventek-Air · Copenhagen · Jan 2022–Nov 2022','14-person team · 11 simultaneous projects',[('Standard work and coordination','Led daily planning, subcontractor coordination, safety documentation and handover packages; used daily meetings and bottleneck analysis to improve delivery.')]),
      ('Operations and Maintenance Manager / Workshop Technician','Biofos, Lynetten · Copenhagen · Aug 2017–Jan 2022','Critical 24/7 operations · SCADA · pumps · HVAC · high-voltage switchgear',[('Operational discipline','Applied 5S, standard work and PDCA to workshop and spare-parts processes, alongside preventive maintenance, fault finding and safety routines.')]),
      ('Electromechanical Technician / Production Team Lead','ARJ Engineering · Tehran · Dec 2003–Mar 2010','12 mechanics and technicians · machine workshop',[('Team and technical problem solving','Led scheduling and material coordination; diagnosed and repaired industrial electrical and mechanical equipment and followed up corrective actions.')])]
    for title,meta,scope,bullets in jobs:
      m.job(title,meta,scope=scope)
      for label,body in bullets: m.bullet(label,body,after=12)
    m.section('EDUCATION, METHODS AND PRACTICAL')
    for a,b in [('PRINCE2 certified project manager','AXELOS / PeopleCert'),('B.Tech, Technology Management and Mechanical Engineering','Copenhagen School of Marine and Technical Engineering · 2017–2022 · GPA 7.6/12'),('Authorised maskinmester, LV/MV/HV','Danish Safety Technology Authority · 2023'),('Electrical and mechanical engineering design, electrical engineering','Tehran Technical University · 2000–2003 · EQF 6'),('Refrigeration and ventilation technology','Mercantec AMU · 2021; STCW training 2021–2023')]: m.edu(a,b)
    m.para('**Methods:** Lean and Six Sigma in practice: PDCA, 5S, standard work, VSM, DMAIC and FMEA · **Digital:** Python, Claude API, AI-assisted development, Excel, SAP ERP · **Languages:** Danish and Persian native; professional English · **Location:** Måløv; open to relocating to Billund · category B licence.',after=25)
    rows=[
('Management systems and process improvement','Developed operational workflows, checklists and reporting at ELOHVAC; standard work and PDCA at Biofos. Enterprise-wide EMS transformation would be a new scale.'),
('Processes, standards, templates and guidance','Created quality checklists, project schedules and reporting tools, and shared AI code review and test standards. Focus: a usable process with a clear owner.'),
('Stakeholder and user requirements','At Data Power, translated customer needs into technical applications, integration and handover; at Novo Nordisk coordinated engineering, procurement and construction.'),
('Process management and continuous improvement','Applied Lean and Six Sigma methods including 5S, PDCA and standard work in practice. Digital workflows at ELOHVAC improved productivity by over 40%.'),
('Cross-functional influence and facilitation','Coordinated 25 specialists across 37 capital projects and led daily planning for 14 people across 11 sites. Use shared priorities and documented follow-up.'),
('Structured communication and follow-through','Reported monthly to management and the client on Novo Nordisk projects; produced documentation and handover material for customer operations at Data Power.'),
('Digital systems, analytics and reporting','Python, Claude API, Excel and SAP ERP; built quality checklists, KPI dashboards and AI-assisted tools. Named LEGO platforms would require onboarding.'),
('Engineering, industrial and regulated experience','Authorised maskinmester with 24/7 operations at Biofos and FAT/SAT and IQ/OQ/PQ at Novo Nordisk under GMP/FDA/EMA requirements.'),
('AI-enabled productivity and governance','Led an AI development team and established review and test standards for AI-generated output; apply human validation before accepting generated results.'),
('Document control, audit and compliance','GMP/FDA/EMA project environment and handover documentation, with zero critical deviations. I would learn LEGO’s specific ISO-based system and controls.'),
('EMS architecture and ownership','Would map processes, governance, capability, performance and knowledge with owners and users; identify interfaces and agree responsibility before changing content.'),
('Lifecycle, knowledge and digital requirements','Would establish ownership, review dates and feedback with the system leads, then define user needs for findable content, workflow and reporting.'),
('Adoption, maturity and improvement backlog','Would baseline a small set of measures with owners, track feedback and local workarounds, and maintain a prioritised backlog with accountable owners.'),
('Engineering degree or equivalent experience','B.Tech in Technology Management and Mechanical Engineering, authorisation as maskinmester, and practical leadership in engineering and technical operations.')]
    m.models_table('THE ROLE — EVIDENCE AND APPROACH',('Requirement','Evidence'),rows,widths=(2500,7846))
    m.section('FIRST 90 DAYS')
    for t in ['Listen: meet the Management System Lead, Lead Professional, process owners and users; review the EMS roadmap and current content.', 'Map: select one priority interface, identify owners, duplicated guidance and user needs; agree a baseline and a small, visible backlog.', 'Test: develop a practical improvement with users, coordinate digital requirements with the Lead Professional, and review adoption and feedback with the owner.']: m.bullet('',t,after=12)
    m.save(path)
if __name__=='__main__':
    p=os.path.join(ROOT,'Shahram_Ajloo_LEGO_EngineeringManagementSystem.docx'); build(p); print(p)
