"""LEO Pharma Maintenance Support Professional: CV with motivation, no cover letter."""
import os
from master_design import MasterDoc
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME='SHAHRAM AJLOO'
TITLE='Maintenance Support Professional · utilities, troubleshooting and regulated documentation'
CONTACT='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'
def build(path):
    m=MasterDoc(os.path.join(ROOT,'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='en-GB')
    m.resume_header(NAME,TITLE,CONTACT,'MOTIVATION AND PROFILE')
    m.para('**Reliable maintenance during a factory transition depends on two things: keeping today’s installations available and retaining the technical evidence needed for a controlled close-down.** LEO Pharma’s Ballerup role interests me because it combines hands-on troubleshooting with compliant documentation and a move to a new production setup. I live in Måløv and would welcome the opportunity to support colleagues across maintenance, engineering and production at Site Ballerup.',after=35)
    m.para('Danish authorised maskinmester (LV/MV/HV), with experience in 24/7 technical operations at Biofos, electrical commissioning and regulated CAPEX projects at Novo Nordisk, and electrical and HVAC service at ELOHVAC. My work includes maintenance of technical installations and production equipment, troubleshooting, quality documentation, continuous improvement and cross-functional coordination. PRINCE2 certified; Lean and Six Sigma methods applied in practice.',after=35)
    m.section('THE MAINTENANCE RECORD — RELEVANT EXPERIENCE')
    for label,body in [
      ('Availability and troubleshooting','Pumps, HVAC, high-voltage switchgear and SCADA at Lynetten; electrical installations, controls and preventive maintenance at ELOHVAC. Experience covers both planned work and operational faults.'),
      ('Documentation and regulated work','FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA at Novo Nordisk, with zero critical deviations at handover across 37 capital projects. Quality assurance and handover records at ELOHVAC.'),
      ('Cause and follow-up','Use A3, 5 Whys and Ishikawa to investigate technical faults; coordinate corrective actions and follow-up. LEO’s specific deviation, CAPA and QMS workflows would require onboarding.'),
      ('Transition and system knowledge','Experienced in technical projects and handover, but no specific old-factory close-down is documented. SAP ERP experience; no documented hands-on experience with PEMAC, Veeva Quality or formal RCM implementation.')]: m.bullet(label,body,after=14)
    m.section('EXPERIENCE')
    jobs=[
      ('Owner / Technical Director / Authorised maskinmester','ELOHVAC ApS · Copenhagen · May 2023–present','8 employees including 3 apprentices · electrical and HVAC service',[('Maintenance and problem solving','Electrical installations, panels, controls, fault finding and preventive maintenance of electrical, ventilation and climate systems, from urgent call-outs to handover.'),('Planning, safety and quality','Plan materials and subcontractors; use LOTO, risk assessment and quality checklists. Responsible for handover documentation and full project P&L.'),('Improvement','Developed AI-assisted schedules, quality checklists and KPI tools; documented productivity improvement of over 40%.')]),
      ('Co-owner and CTO / Technical Lead, AI department','Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 · alongside ELOHVAC','4–10 people · company ceased in November 2026',[('Digital tools and structured delivery','Led AI and AI-coding work; developed technical applications and documentation, with shared standards for review and testing of AI-generated output.')]),
      ('Senior Commissioning Engineer / Project Manager, electrical systems','Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024','37 concurrent CAPEX projects · 25 specialists · GMP/FDA/EMA',[('Technical and regulated delivery','Coordinated engineering, procurement and construction across projects of DKK 2–10 million; FAT/SAT and IQ/OQ/PQ with zero critical deviations at handover.'),('Electrical systems and analysis','Worked with panels, controls, UPS, emergency lighting and fire systems; fault finding and root cause methods including A3, 5 Whys and Ishikawa. SAP ERP and monthly management reporting.')]),
      ('Project and Workshop Manager','Ventek-Air · Copenhagen · Jan 2022–Nov 2022','14-person team · 11 concurrent projects',[('Planning and follow-through','Coordinated capacity, subcontractors, safety documentation and handover packages; daily meetings and bottleneck analysis supported delivery.')]),
      ('Operations and Maintenance Manager / Workshop Technician','Biofos, Lynetten · Copenhagen · Aug 2017–Jan 2022','Critical 24/7 operation · pumps · HVAC · high-voltage switchgear · SCADA',[('Maintenance and availability','Preventive maintenance and urgent fault finding for critical electrical and mechanical installations. Applied LOTO, risk assessment and safety discipline during shift operations.'),('Standardisation','Used 5S, standard work and PDCA for workshop and spare-parts processes; supported reliable spare-parts flow and inventory control.')]),
      ('Electromechanical Technician / Production Team Lead','ARJ Engineering · Tehran · Dec 2003–Mar 2010','12 mechanics and technicians · machine workshop',[('Repair and corrective action','Diagnosed and repaired industrial electrical and mechanical equipment, using root cause analysis and follow-up of corrective actions.')])]
    for title,meta,scope,bullets in jobs:
      m.job(title,meta,scope=scope)
      for label,body in bullets: m.bullet(label,body,after=12)
    m.section('EDUCATION, METHODS AND PRACTICAL')
    for a,b in [('Authorised maskinmester, LV/MV/HV','Danish Safety Technology Authority · May 2023'),('B.Tech, Technology Management and Mechanical Engineering','Copenhagen School of Marine and Technical Engineering · 2017–2022 · GPA 7.6/12'),('PRINCE2 certified project manager','AXELOS / PeopleCert'),('Electrical and mechanical engineering design, electrical engineering','Tehran Technical University · 2000–2003 · EQF 6'),('Refrigeration and ventilation technology','Mercantec AMU · 2021; STCW training 2021–2023')]: m.edu(a,b)
    m.para('**Methods:** Lean and Six Sigma applied in practice, including 5S, PDCA, standard work, 5 Whys and Ishikawa · **Systems:** SAP ERP, Excel, Python and Claude API; PEMAC and Veeva Quality would require training · **Languages:** professional English; Danish and Persian native · **Location:** Måløv, near Ballerup · category B licence.',after=25)
    rows=[
('Technical education and 5+ years in maintenance','Authorised maskinmester and B.Tech; Biofos maintenance and operations 2017–2022, plus ELOHVAC electrical and HVAC service since 2023.'),
('Daily operation and availability of utilities and equipment','At Lynetten supported 24/7 electrical and mechanical installations, including pumps, HVAC, high-voltage switchgear and SCADA, with preventive maintenance.'),
('Troubleshoot breakdowns and operational challenges','Fault finding and repair at Biofos, ELOHVAC and ARJ, supported by electrical and mechanical technical training and root cause methods.'),
('Maintenance documentation and GxP quality processes','Quality and handover documentation at ELOHVAC; FAT/SAT and IQ/OQ/PQ at Novo Nordisk under GMP/FDA/EMA. Would learn LEO’s GxP procedures.'),
('Create, review and technically approve documents in QMS','Technical documentation experience in regulated project work; specific QMS approval permissions and workflows at LEO would require training and authorisation.'),
('Deviation handling, corrective actions and CAPA','Used technical root cause analysis and corrective action follow-up; LEO-specific deviation and CAPA procedures and quality system require onboarding.'),
('Technical SME in root cause analysis','Electrical and mechanical troubleshooting using A3, 5 Whys and Ishikawa. Would contribute technical evidence and work within the site’s investigation process.'),
('CMMS and quality systems such as PEMAC and Veeva Quality','Experience with SAP ERP and structured maintenance work. No documented hands-on use of PEMAC or Veeva Quality; prepared to learn LEO’s CMMS and QMS.'),
('Reliability Centered Maintenance (RCM), an advantage','Preventive maintenance and reliability-focused operations at Biofos; formal RCM implementation experience is not documented and would require development.'),
('Close-down of old factory and transition to new facility','Experience in technical project delivery and handover; specific factory close-down experience is not documented. Would follow site change control and close-down plans.'),
('CAPEX participation, package ownership and smaller OPEX projects','Coordinated 37 CAPEX projects at Novo Nordisk and managed technical work with full P&L at ELOHVAC; scope and authority would be agreed with LEO.'),
('Collaboration, communication and Lean-oriented improvement','Coordinated 25 specialists and worked across engineering, procurement and construction. Applied Lean methods, standard work and PDCA in practical operations.')]
    m.models_table('ROLE REQUIREMENTS — EVIDENCE AND DEVELOPMENT',('Requirement','Evidence'),rows,widths=(2500,7846))
    m.save(path)
if __name__=='__main__':
    p=os.path.join(ROOT,'Shahram_Ajloo_LEOPharma_MaintenanceSupport.docx'); build(p); print(p)
