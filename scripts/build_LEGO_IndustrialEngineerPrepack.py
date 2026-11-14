"""LEGO Prepack application; candidate facts sourced from the master CV."""
import os
from master_design import MasterDoc
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME='SHAHRAM AJLOO'
TITLE='Industrial Engineer · production preparation and practical improvement'
CONTACT='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'
def build(path):
    m=MasterDoc(os.path.join(ROOT,'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='en-GB')
    m.header_banner(NAME,TITLE,CONTACT)
    m.meta('4 November 2026')
    m.meta('The LEGO Group · Industrial Engineer, Prepack · Job ID 0000039085 · Billund')
    p=m._p(spacing_after=80,line=260,justify=False); m._run(p,'Application: Industrial Engineer, Prepack',bold=True,color='1A1A1A')
    def lp(t): m.para(t,after=36,line=235)
    lp('**The first person to use a packing instruction is not the person who wrote it.** It is the colleague on the factory floor who needs to know what belongs in the pack, how the work is done and what to do when something does not fit. If that instruction leaves a question unanswered, the product may be ready while the process is not.')
    lp('Your Prepack team prepares **packing solutions** for new LEGO products and connects product development, engineering and manufacturing. I would bring technical project experience, structured documentation and a habit of testing an improvement with the people who use it. At Novo Nordisk I coordinated 25 specialists across 37 capital projects; at Ventek-Air I planned work across 11 concurrent sites; and in my own company I have developed quality checklists, schedules and digital tools for practical delivery.')
    lp('**From product to pack.** I would start by understanding the product requirements and how the factory works today. With the relevant colleagues, I would check the production data, prepare a clear packing instruction and identify questions or inconsistencies before release. During implementation I would listen to the people doing the work, document issues and follow up on agreed changes. Quality, efficiency and cost all matter, but the first task is to understand their trade-offs in your actual process.')
    lp('I have not worked directly with LEGO packing or packaging processes, and I would need to learn your products, systems and manufacturing requirements. My transferable experience is in preparing technical work, coordinating across disciplines and delivering reliable documentation in regulated projects. At ELOHVAC, AI-assisted estimating, schedules, quality checklists and KPI tools produced a documented productivity improvement of **over 40%**. Lean and Six Sigma are methods I have applied in practice; PRINCE2 is my project-management certification.')
    lp('The Novelty Operations team’s emphasis on **sharing knowledge**, **taking ownership** and asking questions is important to me. I would join ready to learn from colleagues with product and packaging expertise, take responsibility for my own tasks and contribute practical improvements. My background includes leadership, but I am applying for the hands-on work of preparing production data and supporting packing processes, not assuming a people-management remit.')
    lp('I understand this is an **18-month temporary position** in Billund and that no relocation package is offered. I live in Måløv and am open to relocating for the role. I work in Danish and English and would welcome a conversation about the team’s current products and priorities.')
    m.meta('Kind regards',after=6); m.meta('Shahram Ajloo',after=0)
    m.page_break(); m.resume_header(NAME,TITLE,CONTACT,'PROFILE')
    m.para('Technical engineer and project leader with experience in production preparation, documentation and cross-functional coordination. B.Tech in Technology Management and Mechanical Engineering; Danish authorised maskinmester (LV/MV/HV); PRINCE2 certified. Experience includes 37 concurrent capital projects, 11 simultaneous site projects and AI-assisted workflow improvement. Seeking to apply these skills to LEGO Prepack while learning its packing processes.',after=45)
    m.section('THE PACKING INSTRUCTION — MY APPROACH')
    for label,body in [
      ('Understand the product','Clarify the requirements with product development and manufacturing; identify what the factory needs before a packing solution can be prepared.'),
      ('Prepare the data','Check the available production data and document assumptions, questions and changes so that colleagues can follow the same information.'),
      ('Support implementation','Work with operators and engineers to identify practical issues, record them and follow through on an agreed solution.'),
      ('Learn and simplify','Use feedback and Lean principles to look for unnecessary steps while maintaining quality and a clear instruction.')]: m.bullet(label,body,after=12)
    m.section('EXPERIENCE')
    jobs=[
      ('Owner / Technical Director','ELOHVAC ApS · Copenhagen · May 2023–present','8 employees including 3 apprentices · full P&L',[('Planning and documentation','Plan electrical and HVAC work, coordinate materials and subcontractors, and maintain quality assurance and handover documentation.'),('Digital process improvement','Developed AI-assisted estimating, schedules, quality checklists and KPI tools, achieving a documented productivity gain of over 40%.')]),
      ('Co-owner and CTO / Technical Lead, AI department','Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 · alongside ELOHVAC','4–10 people · company ceased in November 2026',[('Requirements and handover','Translated customer requirements into technical applications and integration; provided documentation so customer teams could take over.'),('Structured delivery','Led AI and AI-coding work with shared standards for review and testing of AI-generated output.')]),
      ('Senior Commissioning Engineer / Project Manager, electrical systems','Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024','37 concurrent CAPEX projects · 25 specialists · GMP/FDA/EMA',[('Cross-functional preparation','Coordinated engineering, procurement and construction across projects of DKK 2–10 million; tracked progress, risk and resources.'),('Verification and documentation','FAT/SAT and IQ/OQ/PQ under regulated requirements; zero critical deviations at handover and monthly reporting to management and client.')]),
      ('Project and Workshop Manager','Ventek-Air · Copenhagen · Jan 2022–Nov 2022','14-person team · 11 simultaneous projects',[('Work ready to deliver','Coordinated planning, materials, subcontractors, safety documentation and handover packages; used daily meetings and bottleneck analysis.')]),
      ('Operations and Maintenance Manager / Workshop Technician','Biofos, Lynetten · Copenhagen · Aug 2017–Jan 2022','24/7 operations · SCADA · pumps · HVAC · high-voltage switchgear',[('Standard work','Applied 5S, standard work and PDCA to workshop and spare-parts processes, alongside maintenance and technical fault finding.')]),
      ('Electromechanical Technician / Production Team Lead','ARJ Engineering · Tehran · Dec 2003–Mar 2010','12 mechanics and technicians · machine workshop',[('Production and problem solving','Coordinated schedules and materials; diagnosed and repaired industrial electrical and mechanical equipment and followed up corrective actions.')])]
    for title,meta,scope,bullets in jobs:
      m.job(title,meta,scope=scope)
      for label,body in bullets: m.bullet(label,body,after=12)
    m.section('EDUCATION, TOOLS AND PRACTICAL')
    for a,b in [('B.Tech, Technology Management and Mechanical Engineering','Copenhagen School of Marine and Technical Engineering · 2017–2022 · GPA 7.6/12'),('Authorised maskinmester, LV/MV/HV','Danish Safety Technology Authority · 2023'),('PRINCE2 certified project manager','AXELOS / PeopleCert'),('Electrical and mechanical engineering design, electrical engineering','Tehran Technical University · 2000–2003 · EQF 6'),('Refrigeration and ventilation technology','Mercantec AMU · 2021; STCW training 2021–2023')]: m.edu(a,b)
    m.para('**Methods:** Lean and Six Sigma in practice: 5S, PDCA, standard work and VSM · **Tools:** Excel, SAP ERP, Python and Claude API · **Languages:** professional English; Danish and Persian native · **Location:** Måløv; open to relocating to Billund for the 18-month role without a relocation package · category B licence.',after=25)
    rows=[
('Prepare packing solutions for new products','Would learn LEGO’s product requirements and packing processes with the Prepack team, then prepare solutions with engineering and manufacturing colleagues.'),
('Create production data, packing instructions and documentation','Experienced in structured schedules, quality checklists and handover documents. LEGO-specific packing instructions and data require training and review.'),
('Work across product development, engineering and manufacturing','Coordinated engineering, procurement and construction across 37 Novo Nordisk projects; would learn LEGO’s interfaces and involve the right owners.'),
('Support implementation of packing processes in factories','At Ventek-Air coordinated work, materials and handover across 11 sites. I would apply the same follow-through while learning factory packing processes.'),
('Solve practical production and packing challenges','Technical fault finding at Biofos and ARJ, plus cross-functional project work, provide a problem-solving foundation; direct packing experience is not claimed.'),
('Simplify processes and improve ways of working','Applied 5S, standard work and PDCA at Biofos; AI-assisted workflows and quality checklists at ELOHVAC contributed over 40% productivity improvement.'),
('Relevant degree or practical experience','B.Tech in Technology Management and Mechanical Engineering and electrical/mechanical engineering education, supported by practical engineering and operations work.'),
('Understanding of manufacturing or supply chain','Machine workshop experience at ARJ, material coordination at Ventek-Air and spare-parts processes at Biofos provide a foundation for learning LEGO production.'),
('Comfort with data, documentation and structured processes','Used Excel, SAP ERP, schedules, quality checklists and regulated project documentation. FAT/SAT and IQ/OQ/PQ support an evidence-based approach.'),
('Written and spoken English','Professional English for technical work and communication; Danish and Persian are native languages. Comfortable discussing questions and recording decisions.'),
('Problem solving, learning and collaboration','Worked with 25 specialists on 37 projects; would ask packaging experts and production colleagues for guidance rather than assume knowledge of LEGO systems.'),
('Packing or packaging experience','No direct LEGO packing or packaging-process experience is claimed. The role offers training; I would learn the products, instructions and factory requirements.'),
('Lean or continuous improvement','Lean and Six Sigma methods applied in practice, including 5S, PDCA, standard work and VSM; certification is PRINCE2, not Lean or Six Sigma.'),
('18-month temporary role in Billund','Based in Måløv and open to relocating for the 18-month position, with no relocation package; practical timing can be agreed in conversation.')]
    m.models_table('THE ROLE — EVIDENCE AND APPROACH',('Requirement','Evidence'),rows,widths=(2500,7846))
    m.section('FIRST 90 DAYS')
    for t in ['Learn the products, packing processes, systems and manufacturing requirements with the Prepack team; ask how instructions are used on the factory floor.', 'Prepare assigned production data and documentation with a colleague’s review; follow a packing solution through its handover to manufacturing.', 'Take ownership of agreed tasks, log questions and improvement ideas, and follow up on a small practical improvement with the people who use the process.']: m.bullet('',t,after=12)
    m.save(path)
if __name__=='__main__':
    p=os.path.join(ROOT,'Shahram_Ajloo_LEGO_IndustrialEngineerPrepack.docx'); build(p); print(p)
