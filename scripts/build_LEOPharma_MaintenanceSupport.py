"""LEO Pharma job 4919: rebuilt CV with integrated motivation, not a cover letter.
Evidence: master CV. Company context and sources: INTEL §236 / revised entry.
"""
import os
from master_design import MasterDoc
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME='SHAHRAM AJLOO'
TITLE='Maintenance Support Professional · utilities, technical troubleshooting and GxP'
CONTACT='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'

def build(path):
    m=MasterDoc(os.path.join(ROOT,'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='en-GB')
    m.resume_header(NAME,TITLE,CONTACT,'MOTIVATION — RELIABLE OPERATIONS THROUGH CHANGE')
    m.para('**At Site Ballerup, the old factory must remain dependable while its successor takes over.** That transition requires technical problems to be resolved without losing the maintenance history, decisions and evidence that make a controlled close-down possible. I am drawn to LEO Pharma’s purpose in medical dermatology and to the practical task behind it: helping colleagues in maintenance, engineering, production and laboratories keep installations available and documentation reliable.',after=45)
    m.para('I bring 24/7 utilities and maintenance experience from Biofos, regulated electrical commissioning at Novo Nordisk and electrical/HVAC service from ELOHVAC. My work includes maintenance of technical installations and production equipment, plus continuous improvement. Based in Måløv, I would welcome the opportunity to apply that combination at LEO Pharma’s Ballerup site.',after=35)
    m.section('THREE WORKSTREAMS — HOW I WOULD SUPPORT THE SITE')
    for label,body in [
      ('Keep the installations available','At Lynetten, preventive maintenance and urgent fault finding supported 24/7 operation of pumps, HVAC, high-voltage switchgear and SCADA. At ELOHVAC I plan and carry out electrical and ventilation service, including controls and preventive maintenance. At LEO I would prioritise with Operational Maintenance and the affected users, applying site safety procedures before work.'),
      ('Investigate, document and follow up','Novo Nordisk work included FAT/SAT and IQ/OQ/PQ in GMP/FDA/EMA-regulated projects, with zero critical deviations at handover across 37 projects. I have used A3, 5 Whys and Ishikawa for technical fault analysis and corrective actions. At LEO I would document technical findings in its CMMS and QMS, follow up deviations, action items and CAPAs on time, and obtain review and technical approval through authorised site workflows.'),
      ('Transition with control','Project planning and handover on 37 CAPEX projects and 11 Ventek-Air projects provide a basis for coordinating people, dependencies and records. For close-down I would work to LEO’s approved plan with asset owners and quality colleagues: identify affected installations and open actions, maintain records, and support a controlled handover. I have not led a factory close-down; I would learn the site-specific process.')]: m.bullet(label,body,after=18)
    m.section('TECHNICAL FIT AND SYSTEMS')
    m.para('**Qualifications:** elautoriseret maskinmester (Danish electrical authorisation, LV/MV/HV), B.Tech in Technology Management and Mechanical Engineering; PRINCE2 certified. **Methods:** Lean and Six Sigma applied in practice, including 5S, standard work, PDCA, 5 Whys and Ishikawa. **Digital:** SAP ERP, Excel, Python and CMMS familiarity. My records do not document hands-on use of PEMAC or Veeva Quality, or formal RCM implementation; I would learn LEO’s systems and reliability approach. **Languages:** Danish and Persian native; professional English.',after=32)
    m.page_break()
    m.section('RELEVANT EXPERIENCE — MAINTENANCE, DOCUMENTATION AND DELIVERY')
    jobs=[
      ('Owner / Technical Director / elautoriseret maskinmester','ELOHVAC ApS · Copenhagen · May 2023–present','Electrical and HVAC service · 8 employees including 3 apprentices',[('Technical support','Electrical installations, panels, controls, fault finding and preventive maintenance of electrical, ventilation and climate systems, from urgent call-outs to handover.'),('Planning and quality','Plan work, materials and subcontractors; apply LOTO and risk assessment, prepare quality assurance and handover documentation, and manage project economics. AI-assisted schedules, quality checklists and KPI tools delivered over 40% productivity improvement.')]),
      ('Co-owner and CTO / Technical Lead, AI department','Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 · alongside ELOHVAC','4–10 people · company ceased in November 2026',[('Structured digital delivery','Led AI and AI-coding work, including technical applications and documented handover to customers. Introduced shared standards for reviewing and testing AI-generated output.')]),
      ('Senior Commissioning Engineer / Project Manager, electrical systems','Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024','37 concurrent CAPEX projects · 25 specialists · GMP/FDA/EMA',[('Regulated delivery','Coordinated engineering, procurement and construction across projects of DKK 2–10 million each; FAT/SAT and IQ/OQ/PQ, with zero critical deviations at handover.'),('Technical investigation and reporting','Worked with panels, controls, UPS, emergency lighting and fire systems; fault finding with A3, 5 Whys and Ishikawa. Used SAP ERP for finance and assets and reported monthly to management and client.')]),
      ('Project and Workshop Manager','Ventek-Air · Copenhagen · Jan 2022–Nov 2022','14-person team · 11 simultaneous projects',[('Planning and handover','Coordinated capacity, subcontractors, safety documentation and handover packages. Daily meetings and bottleneck analysis supported progress across the sites.')]),
      ('Operations and Maintenance Manager / Workshop Technician','Biofos, Lynetten · Copenhagen · Aug 2017–Jan 2022','24/7 operations · pumps · HVAC · high-voltage switchgear · SCADA',[('Availability and safe work','Preventive maintenance and urgent fault finding in critical electrical and mechanical installations. Used LOTO, risk assessments and shift safety routines.'),('Maintenance improvement','Applied 5S, standard work and PDCA to workshop and spare-parts processes; supported spare-parts flow and inventory control.')]),
      ('Electromechanical Technician / Production Team Lead','ARJ Engineering · Tehran · Dec 2003–Mar 2010','12 mechanics and technicians · industrial machine workshop',[('Faults and corrective action','Diagnosed and repaired industrial electrical and mechanical equipment; performed root cause analysis and followed up corrective actions.')])]
    for title,meta,scope,bullets in jobs:
      m.job(title,meta,scope=scope)
      for label,body in bullets: m.bullet(label,body,after=11)
    m.section('EDUCATION AND PRACTICAL')
    for a,b in [('Elautoriseret maskinmester, LV/MV/HV','Danish Safety Technology Authority · May 2023'),('B.Tech, Technology Management and Mechanical Engineering','Copenhagen School of Marine and Technical Engineering · 2017–2022 · GPA 7.6/12'),('PRINCE2 certified project manager','AXELOS / PeopleCert'),('Electrical and mechanical engineering design, electrical engineering','Tehran Technical University · 2000–2003 · EQF 6'),('Refrigeration and ventilation technology','Mercantec AMU · 2021; STCW training 2021–2023')]: m.edu(a,b)
    m.para('Måløv, Ballerup municipality · category B driving licence · Danish and Persian native; professional English.',after=20)
    m.page_break()
    rows=[
('Maintenance education and 5+ years','Danish elautoriseret maskinmester and B.Tech; preventive maintenance and operations at Biofos 2017–2022, plus electrical/HVAC service at ELOHVAC since 2023.'),
('Old and new installations: daily operation and availability','Biofos: pumps, HVAC, high-voltage switchgear and SCADA in 24/7 operation; ELOHVAC: installation, service and preventive maintenance of technical systems.'),
('Maintenance planning, implementation and development','At Biofos worked with preventive maintenance and standard work; at ELOHVAC plan technical work, materials, subcontractors and quality checks for delivery.'),
('Breakdowns and ad hoc troubleshooting','Fault diagnosis and repair in industrial electrical and mechanical equipment at ARJ; urgent technical fault finding at Biofos and ELOHVAC.'),
('GxP maintenance documentation and records','Novo Nordisk FAT/SAT and IQ/OQ/PQ in GMP/FDA/EMA-regulated projects; quality and handover documents at ELOHVAC. LEO’s procedures need onboarding.'),
('Create, review and technically approve documents in QMS','Regulated technical project and handover experience provides a basis for review; at LEO, document creation and technical approval would follow site training and assigned authority.'),
('CMMS and QMS section documentation','SAP ERP for assets, finance and costs; familiarity with CMMS. Hands-on PEMAC and Veeva Quality experience is not documented; learn site workflows.'),
('Deviations, corrective actions, action items and CAPAs','ARJ: root cause analysis and corrective-action follow-up; Novo Nordisk: regulated testing and zero critical deviations at handover. Learn LEO’s CAPA process and timelines.'),
('Technical SME in root cause analysis','Technical electrical and mechanical fault finding, including A3, 5 Whys and Ishikawa at Novo Nordisk, supports a technical contribution to investigations.'),
('Factory close-down and transition','Coordinated project delivery and handover; have not led a factory close-down. Would work with asset owners and quality on records, open actions and approved transition plans.'),
('CAPEX packages and smaller OPEX projects','Coordinated 37 concurrent capital projects of DKK 2–10 million; managed technical service projects and full P&L at ELOHVAC. Site scope and authority to be agreed.'),
('Reliability Centered Maintenance (RCM)','Preventive maintenance and 24/7 availability experience at Biofos. Formal RCM implementation is not documented; develop this within LEO’s reliability approach.'),
('Cross-functional communication and task management','Coordinated 25 specialists across engineering, procurement and construction at Novo Nordisk; managed 11 simultaneous projects and 14 people at Ventek-Air.'),
('LEAN-oriented culture and optimisation','Applied 5S, PDCA and standard work in operations. AI-supported work at ELOHVAC delivered over 40% productivity improvement; Lean/Six Sigma are practice, not certifications.')]
    m.models_table('LEO PHARMA ROLE — EVIDENCE AND APPROACH',('Requirement','Relevant evidence or approach'),rows,widths=(2500,7846))
    m.section('FIRST WEEKS — LEARN THE SITE, SUPPORT THE TRANSITION')
    for t in ['Meet Operational Maintenance, Engineering, production and laboratory colleagues; understand critical assets, site safety and the current transition plan.', 'Learn the CMMS, QMS and GxP procedures, including documentation permissions and deviation/CAPA follow-up; review priorities with the team lead.', 'Support an agreed maintenance or close-down task, record technical findings and open actions, and review progress with the relevant asset and quality owners.']: m.bullet('',t,after=12)
    m.save(path)

if __name__=='__main__':
    p=os.path.join(ROOT,'Shahram_Ajloo_LEOPharma_MaintenanceSupport.docx'); build(p); print(p)
