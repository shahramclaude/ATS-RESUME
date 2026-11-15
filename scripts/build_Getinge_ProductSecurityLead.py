"""Getinge Product Security Lead — combined application, CV and proposed start."""
import os
from master_design import MasterDoc
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME='SHAHRAM AJLOO'
TITLE='Technical delivery | Software, quality and cross-functional coordination'
CONTACT='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'

def build(path):
 m=MasterDoc(os.path.join(ROOT,'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='en-GB')
 m.header_banner(NAME,TITLE,CONTACT);m.meta('Getinge IT Solutions · Digital Health Solutions R&D · Copenhagen')
 p=m._p(spacing_after=80,line=260,justify=False);m._run(p,'Application: Product Security Lead',bold=True,color='1A1A1A')
 m.para('To the hiring team,',after=50)
 m.para('Product security in healthcare has to work across the life of a product, not just at a release review. Engineering teams need security requirements they can act on, quality and regulatory colleagues need traceable evidence, and risks need an accountable owner and a clear route to decision. That coordination matters when technology supports clinical care.',after=80)
 m.para('I would start by understanding the existing secure software development lifecycle (SSDLC), the products it covers and how engineering, architects, quality and regulatory teams use it. With the responsible cybersecurity experts, I would map requirements, decision points and evidence, identify where teams need support, and agree a practical improvement backlog. Threat-model and security-architecture reviews must be led and approved by people with the appropriate specialist competence.',after=80)
 m.para('My contribution draws on two related but distinct areas. At Data Power Consultant I led a 4–10-person AI and AI-coding department, delivering industrial applications from requirements and integration to commissioning and handover; the team used review and testing standards for AI-assisted software. At Novo Nordisk I coordinated 25 specialists across technical projects and worked with FAT/SAT and IQ/OQ/PQ in a regulated environment, with zero critical deviations at handover. This was electrical commissioning, not medical-device cybersecurity.',after=80)
 m.para('There is a material gap against your requirements: my documented experience does not establish five years in product security, security engineering or software engineering, nor ownership of an SSDLC, threat modelling, security architecture or medical-device cybersecurity compliance. Familiarity with the specific security regulations, standards, maturity frameworks and DevSecOps tools in the posting is not documented. I would welcome a conversation about whether my implementation and coordination background could support a different role or a development pathway at Getinge.',after=80)
 m.para('I am interested in how Digital Health Solutions connects practical engineering, risk ownership and evidence to support safe, dependable products for healthcare teams.',after=65)
 m.meta('Kind regards',after=15);m.meta('Shahram Ajloo',after=0)
 m.page_break();m.resume_header(NAME,TITLE,CONTACT,'PROFILE')
 m.para('Technical leader and Danish-authorised marine and technical engineer (maskinmester) with experience in AI-assisted software delivery, industrial systems, quality documentation and cross-functional project coordination. Brings structured implementation and regulated-project experience; product cybersecurity leadership is not documented.',after=70)
 m.section('RELEVANT TECHNICAL AND DELIVERY EXPERIENCE')
 for a,b in [
 ('Software delivery and review','Data Power Consultant: led a 4–10-person AI and AI-coding department, delivering technical and industrial applications from requirements, architecture and integration through commissioning and handover. AI-assisted development included code review and testing against shared acceptance standards.'),
 ('Regulated project discipline','Novo Nordisk: FAT/SAT and IQ/OQ/PQ for electrical projects under GMP/FDA/EMA, with zero critical deviations at handover. This experience concerns commissioning documentation, not software or medical-device security compliance.'),
 ('Cross-functional coordination','Novo: coordinated 25 specialists in engineering, procurement and construction across 37 concurrent CAPEX projects, following progress, resources, risks and cost and reporting to management and client.'),
 ('Operational improvement','Applied PDCA, A3 and root-cause analysis at Novo. At ELOHVAC, Python/Claude API tools for estimates, plans, quality and KPIs achieved over 40% documented productivity improvement.'),
 ('Leadership and adoption','At ELOHVAC, lead five electricians and three apprentices using 1:1s, structured training and clear work allocation. At Data Power, used common priorities and review practices across technical work.')]:m.bullet(a,b,after=25)
 m.models_table('METHODS FOR DELIVERY AND IMPROVEMENT',('Need','Documented contribution'),[
 ('Requirements to handover','Data Power: customer requirements, integration, commissioning and documented handover for technical applications.'),
 ('Risk and evidence','Novo: technical project risk follow-up and regulated commissioning evidence; no cybersecurity risk ownership claimed.'),
 ('Learning and adoption','PDCA and A3 in Novo improvement work; 1:1 and structured training in ELOHVAC.'),
 ('Coordination','PRINCE2 certified project manager; cross-functional project reporting and stakeholder coordination.')])
 m.page_break();m.section('PROFESSIONAL EXPERIENCE')
 jobs=[
 ('Co-owner and CTO / Technical Lead, AI department','Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 · alongside ELOHVAC','4–10 people · company ceased November 2026',[
 ('Technical applications','Led customer requirements, architecture, system integration and commissioning through documentation and handover; delivered LLM API and AI-agent solutions.'),
 ('Development practice','Introduced AI-assisted coding with code review and testing against shared standards; used AI to support management reporting and decisions.')]),
 ('Owner / Technical Director / Danish-authorised marine and technical engineer','ELOHVAC ApS · Copenhagen · May 2023–present','5 electricians and 3 apprentices · full P&L',[
 ('Technical delivery','Lead electrical, ventilation and climate installation projects, including planning, safety, quality and handover.'),
 ('Digital tools','Developed Python/Claude API tools for estimating, schedules, quality and KPI reporting; documented productivity gain over 40%.')]),
 ('Senior Commissioning Engineer / Project Manager, electrical systems','Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024','37 concurrent CAPEX projects · 25 specialists · DKK 2–10m each',[
 ('Coordination and quality','Followed risk, progress, resources and cost across engineering, procurement and construction; FAT/SAT and IQ/OQ/PQ with zero critical handover deviations.'),
 ('Improvement','PDCA programme reduced energy costs by 40%; A3 and root-cause analysis; SAP ERP for finance and assets.')]),
 ('Project and Workshop Manager','Ventek-Air · Copenhagen · Jan 2022–Nov 2022','14 people · 11 concurrent technical projects',[
 ('Delivery','Managed capacity, subcontractors and documentation from specification to handover, using daily boards and bottleneck analysis.')]),
 ('Maintenance and Operations Manager / Workshop Technician','BIOFOS, Lynetten · Copenhagen · Aug 2017–Jan 2022','24/7 operations · electrical and mechanical systems',[
 ('Reliability and safety','Preventive maintenance, fault-finding and spare-parts flow; 5S, Standard Work, LOTO and risk assessment.')]),
 ('Electromechanical Technician / Production Team Leader','ARJ Engineering · Tehran · Dec 2003–Mar 2010','12 mechanics and technicians · machine workshop',[
 ('Workshop','Led shift and material planning and repaired industrial electrical and mechanical equipment.')])]
 for title,meta,scope,bullets in jobs:
  m.job(title,meta,scope=scope)
  for a,b in bullets:m.bullet(a,b,after=15)
 m.section('EDUCATION AND CERTIFICATION')
 for a,b in [('B.Tech, Technology Management & Mechanical Engineering','Copenhagen School of Marine and Technical Engineering · maskinmester programme'),('Electrical and mechanical engineering design, electrical engineering','Tehran Technical University'),('Danish authorisation as marine and technical engineer','Danish Safety Technology Authority · LV/MV/HV'),('PRINCE2 certified project manager','AXELOS / PeopleCert')]:m.edu(a,b)
 m.para('Languages: English (professional); Danish and Persian/Farsi (native). Tools: Python, Claude API, SAP ERP, Excel and Power BI.',after=40)
 m.page_break();m.models_table('FIRST 90 DAYS — PROPOSED LEARNING AND SUPPORT',('When','Actions and outputs'),[
 ('Week 1','Meet cybersecurity, engineering, architecture, quality and regulatory leads. Clarify product scope, existing governance, decision rights and the boundaries of my contribution.'),
 ('By day 30','Map the existing SSDLC, responsibilities and evidence flow with the accountable specialists. Identify unanswered questions and personal learning needs; do not independently approve security or compliance decisions.'),
 ('By day 60','Support an agreed improvement in documentation or cross-team coordination under specialist direction. Record the owner, dependencies and review process; learn the applicable regulatory requirements with quality and regulatory colleagues.'),
 ('By day 90','Review the usefulness of that support with stakeholders, record lessons and agree next steps. Security, architecture and regulatory conclusions remain with authorised experts.')])
 m.section('COORDINATION AROUND THE PRODUCT LIFECYCLE')
 for a,b in [
 ('Governance and architecture','Make review ownership, open decisions and escalation routes visible. Threat modelling and security architecture assessments require qualified cybersecurity reviewers.'),
 ('Risk and regulatory evidence','Work with quality and regulatory specialists to map applicable requirements and evidence. FDA cybersecurity guidance, EU MDR, IEC 81001-5-1, IEC 62443-4-1, NIS2 and the Cyber Resilience Act require specialist interpretation.'),
 ('Development teams','Translate agreed actions into clear owners, deadlines and feedback; support teams in adopting approved processes without substituting coordination for technical security controls.'),
 ('Maturity and operations','Learn how Getinge assesses maturity and handles vulnerabilities. OWASP SAMM, BSIMM, DevSecOps, SAST, DAST, SCA and SBOM management are areas for assessment and learning, not claimed prior expertise.')]:m.bullet(a,b,after=30)
 m.section('PROFESSIONAL AI DEVELOPMENT')
 m.para('I build Python and Claude tools for technical applications, planning and reporting, and investment models for development and new business ideas. Any AI use at Getinge would follow approved data-handling and development policies, with human review; AI does not establish security assurance or regulatory compliance.',after=70)
 m.section('EXPERIENCE BOUNDARY')
 m.para('Five years of qualifying product-security or software-engineering work, medical-device cybersecurity implementation, audits with notified bodies and CISSP, CSSLP or CISM certification are not documented. Novo GMP/FDA commissioning experience should not be presented as FDA medical-device cybersecurity experience.',after=60)
 return m.save(path,title='Application and CV — Getinge Product Security Lead',subject='Technical delivery and regulated project coordination',keywords='product security, software, risk, Getinge')

if __name__=='__main__':print(build(os.path.join(ROOT,'Shahram_Ajloo_Getinge_ProductSecurityLead.docx')))
