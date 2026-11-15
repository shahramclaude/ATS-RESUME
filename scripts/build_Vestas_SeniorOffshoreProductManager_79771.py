"""Vestas Senior Offshore Product Manager — combined English application and CV."""
import os
from master_design import MasterDoc
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME='SHAHRAM AJLOO'
TITLE='Technical service and commercial delivery | Lifecycle value'
CONTACT='+45 93 99 95 14 · ajlooshahram@gmail.com'

def build(path):
 m=MasterDoc(os.path.join(ROOT,'Shahram_Ajloo_NNE_DepartmentManagerEI.docx'),lang='en-GB')
 m.header_banner(NAME,TITLE,CONTACT);m.meta('Vestas · Turbine Service Product Management · Requisition 79771')
 p=m._p(spacing_after=80,line=260,justify=False);m._run(p,'Application: Senior Offshore Product Manager',bold=True,color='1A1A1A')
 m.para('To the hiring team,',after=50)
 m.para('An offshore service offering is a long-term commitment: the customer needs a clear value proposition, while service teams must be able to deliver it safely and consistently. A product decision should therefore connect customer needs, technical feasibility, cost and risk before it reaches a roadmap or a commercial offer.',after=80)
 m.para('I would begin by listening to regional commercial and service teams, product development and customers to understand where the existing portfolio meets their needs and where it does not. Together we could turn those findings into a prioritised set of requirements, with clear assumptions and owners, for discussion at the relevant product roadmap decisions.',after=80)
 m.para('For a proposed service offering, I would build the case with the people responsible for commercial, engineering and operations: customer outcome, scope, delivery model, risks and cost assumptions. Pricing and positioning would be tested against those assumptions and regional input. Before launch, sales enablement and training need to make the offer understandable; after launch, the team needs an agreed way to follow adoption and actual performance against the business case.',after=80)
 m.para('My experience brings a technical-service perspective to that work. At ELOHVAC I am responsible for P&L, quotations, service delivery and customer-facing technical projects. At Novo Nordisk I coordinated 25 specialists across engineering, procurement and construction on 37 CAPEX projects, reporting progress, resources, risks and costs to management and client. At Data Power I helped deliver technical applications from customer requirements to documented handover. I also build investment models using NPV, IRR and scenarios.',after=80)
 m.para('This role calls for extensive service product management and commercialization experience. My documented background does not include ownership of an offshore wind service-product portfolio, offshore turbine expertise or proven go-to-market launches at global scale. I would welcome a discussion about whether my technical and commercial experience could contribute to this team or to a more suitable role while I develop that specialist knowledge.',after=80)
 m.para('I am based in Måløv; the preferred Aarhus location and working arrangements would need to be agreed. I would be pleased to discuss the commercial decisions and customer outcomes the portfolio needs to support.',after=70)
 m.meta('Kind regards',after=15);m.meta('Shahram Ajloo',after=0)
 m.page_break();m.resume_header(NAME,TITLE,CONTACT,'PROFILE')
 m.para('Danish-authorised marine and technical engineer (maskinmester) with experience in technical services, P&L, customer delivery and cross-functional projects. Connects practical operations with commercial assumptions and structured analysis. The documented background is industrial and technical services, not offshore wind service-product ownership.',after=70)
 m.section('EXPERIENCE THAT SUPPORTS SERVICE VALUE')
 for a,b in [
 ('Service delivery and economics','ELOHVAC: full P&L, quotations, planning, subcontractors, quality and handover for business customers; service work includes electrical, ventilation and climate installations.'),
 ('Customer needs to delivery','Data Power: led an AI and AI-coding department delivering customer technical applications from requirements and architecture through integration, commissioning and handover.'),
 ('Cross-functional decisions','Novo Nordisk: coordinated 25 specialists across engineering, procurement and construction on 37 concurrent CAPEX projects; reported progress, risk, resources and cost to management and client.'),
 ('Operational perspective','BIOFOS: 24/7 electrical and mechanical plant maintenance and fault-finding; experience of spare-parts flow and reliable technical operations.'),
 ('Analysis and improvement','Builds investment models using NPV, IRR and scenarios. Novo PDCA programme reduced energy costs by 40%; ELOHVAC Python/Claude planning and quality tools delivered over 40% documented productivity improvement.')]:m.bullet(a,b,after=25)
 m.models_table('TOOLS FOR A SERVICE-PRODUCT DECISION',('Need','Evidence and proposed application'),[
 ('Commercial assessment','P&L and quotation experience at ELOHVAC; proposed scenario-based business case with commercial and operational specialists.'),
 ('Stakeholder alignment','Novo coordination across engineering, procurement and construction; proposed regional requirements and decision log.'),
 ('Value after launch','Data Power technical applications handed over to customers; proposed adoption and business-case review with service and sales teams.'),
 ('Improvement','PDCA and A3 at Novo; PRINCE2 certified project manager. Digital modelling supports analysis, not an unverified product outcome.')])
 m.page_break();m.section('PROFESSIONAL EXPERIENCE')
 jobs=[
 ('Owner / Technical Director / Danish-authorised marine and technical engineer','ELOHVAC ApS · Copenhagen · May 2023–present','5 electricians and 3 apprentices · full P&L',[
 ('Service and commercial delivery','Lead quotations, planning, materials, subcontractors and quality for business-customer installations and service work; manage financial performance and handover.'),
 ('Digital improvement','Developed Python/Claude tools for estimates, schedules, quality and KPI reporting, delivering a documented productivity gain over 40%.')]),
 ('Co-owner and CTO / Technical Lead, AI department','Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 · alongside ELOHVAC','4–10 people · company ceased November 2026',[
 ('Customer solutions','Led technical and industrial applications from requirements, architecture and integration to commissioning, documentation and handover.'),
 ('Planning and AI','Applied AI to decision material and reporting; managed priorities across the two concurrent businesses using a shared plan.')]),
 ('Senior Commissioning Engineer / Project Manager, electrical systems','Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024','37 concurrent CAPEX projects · 25 specialists · DKK 2–10m each',[
 ('Cross-functional control','Coordinated engineering, procurement and construction; monitored progress, resources, risks and costs and reported to management and client.'),
 ('Quality and efficiency','FAT/SAT and IQ/OQ/PQ without critical deviations at handover. PDCA programme reduced energy costs by 40%; SAP ERP for finance and assets.')]),
 ('Project and Workshop Manager','Ventek-Air · Copenhagen · Jan 2022–Nov 2022','14 people · 11 concurrent technical projects',[
 ('Projects and agreements','Managed capacity, tenders, subcontractors and documentation from specification to handover; used daily boards and bottleneck analysis.')]),
 ('Maintenance and Operations Manager / Workshop Technician','BIOFOS, Lynetten · Copenhagen · Aug 2017–Jan 2022','24/7 operations · electrical and mechanical plant',[
 ('Operational reliability','Preventive maintenance and fault-finding on pumps, HVAC, switchboards and SCADA; spare-parts flow, 5S and LOTO.')]),
 ('Electromechanical Technician / Production Team Leader','ARJ Engineering · Tehran · Dec 2003–Mar 2010','12 mechanics and technicians · machine workshop',[
 ('Technical team','Led shift and material planning and repaired industrial electrical and mechanical equipment.')])]
 for title,meta,scope,bullets in jobs:
  m.job(title,meta,scope=scope)
  for a,b in bullets:m.bullet(a,b,after=15)
 m.section('EDUCATION AND CERTIFICATION')
 for a,b in [('B.Tech, Technology Management & Mechanical Engineering','Copenhagen School of Marine and Technical Engineering · maskinmester programme'),('Electrical and mechanical engineering design, electrical engineering','Tehran Technical University'),('Danish authorisation as marine and technical engineer','Danish Safety Technology Authority · LV/MV/HV'),('PRINCE2 certified project manager','AXELOS / PeopleCert')]:m.edu(a,b)
 m.para('Languages: English (professional); Danish and Persian/Farsi (native). Tools: SAP ERP, Excel, Power BI, Python and Claude API.',after=40)
 m.page_break();m.models_table('FIRST 90 DAYS — PROPOSED START',('When','Actions and outputs'),[
 ('Week 1','Meet product, service operations, commercial and engineering stakeholders. Understand the portfolio, decision rights, current priorities and the information used in existing product decisions.'),
 ('By day 30','Map regional and customer requirements, open questions and portfolio interfaces with responsible colleagues. Review available performance data and identify the most important gaps in understanding.'),
 ('By day 60','With commercial and technical specialists, outline a candidate opportunity: value proposition, delivery assumptions, cost, risks and scenarios. Agree what evidence is needed before any pricing or launch decision.'),
 ('By day 90','Review findings and options with the product lead and affected regions. Propose a prioritised next step, including ownership, sales enablement needs and measures for adoption and business-case performance.')])
 m.section('FROM CUSTOMER NEED TO LIFECYCLE VALUE')
 for a,b in [
 ('Requirements and roadmap','Consolidate regional and customer needs with commercial, service and engineering colleagues. Compare opportunities with business priorities and make trade-offs visible before roadmap decisions.'),
 ('Commercial case and positioning','Clarify scope, customer outcome, cost, risk and lifecycle assumptions. Use scenarios to test viability and work with accountable commercial teams on pricing and positioning.'),
 ('Launch and adoption','Agree go-to-market activities, sales enablement, training and customer communication with the relevant teams. Ensure operational owners can deliver what the offer promises.'),
 ('Performance and improvement','Track adoption and business-case performance against agreed measures and owners; use PDCA to investigate gaps and decide whether the offering needs adjustment.')]:m.bullet(a,b,after=30)
 m.section('DIGITAL SUPPORT FOR DECISIONS')
 m.para('I use Python and Claude to develop planning, quality and reporting tools, and build investment models for development and new business ideas. For Vestas, analysis could support scenario comparison and business-case transparency, subject to approved data, commercial review and human validation.',after=70)
 m.section('RELEVANT EXPERIENCE AND DEVELOPMENT')
 m.para('Technical service, customer solution delivery and project economics are transferable. Extensive offshore WTG service-product management, global portfolio ownership and demonstrated product go-to-market launches are not documented; technical and commercial assumptions would be developed with Vestas specialists.',after=60)
 return m.save(path,title='Application and CV — Vestas Senior Offshore Product Manager 79771',subject='Technical services and lifecycle value',keywords='product management, service, lifecycle, Vestas')

if __name__=='__main__':print(build(os.path.join(ROOT,'Shahram_Ajloo_Vestas_SeniorOffshoreProductManager_79771.docx')))
