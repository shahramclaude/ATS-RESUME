# -*- coding: utf-8 -*-
"""Jones Engineering — Electrical Package Manager, Copenhagen, 145571.
One master-design document: task-focused application on page 1, evidence-led CV after it.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")
OUTPUT = os.path.join(ROOT, "Shahram_Ajloo_JonesEngineering_ElectricalPackageManager_145571.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Electrical Package Manager | Electrical projects · labour · commissioning · handover"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv, Denmark")
DATE = "3 November 2026"
RECIPIENT = "Jones Engineering · Copenhagen · Recruitment Team"
SUBJECT = "Application: Electrical Package Manager — Copenhagen — 145571"

# Page 1 — address the delivery challenge, not the applicant.
OPENING = ("Three checks must agree before an electrical workfront opens: released information, available labour and materials, and an agreed inspection point.")

LETTER = [
    "Once work is under way, those checks have to keep pace with changing interfaces and project milestones. A crew waiting on a drawing, access or a delivery is a schedule problem; an installation that advances without the right inspection or safety control becomes a quality and handover problem. Package control has to connect the workface to the project plan every day.",
    "The working record should give the Project Manager and supervisors one reliable view of scope, labour by area, earned progress, material status, design constraints, quality holds, safety actions and changes. At the daily coordination, each workfront leaves with a supervisor, crew, prerequisites and next hold point. At the weekly review, actual hours and progress are compared with the package baseline; a constraint has an owner, due date and recovery decision before it threatens a milestone.",
    "Quality and safety are planned into release and close-out. Method statements, permits and task briefings precede the work; inspection and test points are agreed before concealment or energisation; test evidence, snags and corrective actions remain linked to the system and responsible trade. Commissioning and handover then follow the installation record rather than a last-minute reconstruction.",
    "In the first 30 days, establish the package baseline and walk the workfronts with supervisors and the wider team. By day 60, run a dependable daily labour and constraint check plus weekly progress, cost, quality and safety reviews. By day 90, have commissioning readiness, open items, changes and handover evidence visible in the same forecast, with named owners and dates.",
    "Jones describes its aim as high quality, customer focused project delivery and its core value as Engineering Through People. Relationships are at the heart of our business; clear decisions at each interface protect those relationships. Get Home Safe belongs in every workfront release. The Copenhagen team describes a fast paced, process driven environment where teamwork is key to success. Continuous training and work-life balance are supported by developing the team while planning realistic work fronts. Reliable, safe delivery is a practical way of contributing to a sustainable future.",
]

PROFILE = (
    "Jones Engineering needs package control that connects workforce, project interfaces, quality, safety and milestones through commissioning and handover. The relevant experience is more than 3 years in electrical contracting and project delivery as ELOHVAC owner/technical director (May 2023–present): full P&L, project scoping and quotation, planning, materials, subcontractors, quality and handover, with daily leadership of 5 electricians and 3 apprentices. Earlier delivery includes 37 concurrent CAPEX projects (DKK 2–10m each) with 25 specialists and zero critical findings at handover, plus 11 concurrent installation projects with a 14-person team. B.Tech in Technology Management & Mechanical Engineering; Danish electrical authorisation LV/MV/HV."
)

RESULTS = [
    ("37 concurrent CAPEX projects", "DKK 2–10m each; 25 cross-functional specialists coordinated; FAT/SAT and qualification records; zero critical findings at handover."),
    ("11 simultaneous installation projects", "Ventek-Air: 14-person team, from specification through production and installation to formal handover."),
    ("5 electricians + 3 apprentices", "ELOHVAC: daily labour planning, technical delivery and full P&L responsibility across 40+ service installations."),
    ("Over 40% productivity improvement", "ELOHVAC: Python/Claude tools for estimates, schedules, QA checklists and KPI dashboards."),
]

EXPERIENCE = [
    ("Owner / Technical Director / Elautoriseret Maskinmester", "ELOHVAC ApS · Copenhagen · May 2023–Present", "Electrical contracting · 5 electricians + 3 apprentices · 40+ service installations · full P&L",
     [("Electrical project delivery", "Scope and quotation, calculation, work planning, materials, subcontractors, site execution, quality checks and handover documentation for electrical, ventilation and climate projects."),
      ("Team and labour coordination", "Daily allocation and follow-up for 5 electricians and 3 apprentices; individual conversations, MUS, structured apprentice training and work-environment follow-up."),
      ("Commercial and safety control", "Full P&L, estimates and cost follow-up; LOTO, risk assessments, site-start checks and documented quality. Service delivery improved productivity by over 40% through in-house planning and reporting tools.")]),
    ("Co-owner and CTO / Technical Lead, AI Department", "Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 (concurrent with ELOHVAC)", "4–10 people · AI and AI coding teams",
     [("Technical applications and delivery standards", "Led technical/industrial application work from requirements and architecture to integration, commissioning, documentation and handover; introduced shared AI-assisted coding, review and test standards."),
      ("AI-assisted technical design", "Used AI coding for calculations, dimensioning and design options for technical systems and industrial components, with engineering validation before delivery; AI-supported reporting and matrix leadership.")]),
    ("Senior Commissioning Engineer / Project Manager, Electrical Systems", "Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024", "37 concurrent CAPEX projects · DKK 2–10m each · 25 specialists · GMP/FDA/EMA",
     [("Project, budget and stakeholder control", "Coordinated progress, budgets, risks and resources across engineering, procurement and site; reported monthly to management and client."),
      ("Commissioning and acceptance", "FAT/SAT, IQ/OQ/PQ, validation documentation and deviation handling; zero critical findings at handover. PDCA programme reduced energy costs by 40%; SAP ERP supported asset and cost reporting.")]),
    ("Project and Workshop Manager, Ventilation & Climate", "Ventek-Air · Copenhagen · Jan–Nov 2022", "11 concurrent installation projects · DKK 2–10m each · 14-person team",
     [("Specification to formal handover", "Coordinated offers, capacity, production, assembly, materials, subcontractors, safety, quality and documentation across 11 live projects; daily huddles and bottleneck analysis.")]),
    ("Maintenance and Operations Manager / Workshop Technician", "Biofos (Lynetten) · Copenhagen · Aug 2017–Jan 2022", "24/7 operations · pumps, HVAC, HV switchgear and SCADA",
     [("Critical plant and safe work", "Preventive maintenance, urgent fault-finding, 5S, Standard Work and PDCA; LOTO, risk assessments, APV and near-miss follow-up. Five years without unplanned stops.")]),
    ("Electromechanical Technician / Production Team Leader", "ARJ Engineering · Tehran · Dec 2003–Mar 2010", "12-person workshop team",
     [("Electrical trade and team leadership", "Electrical/mechanical diagnosis and repair, shift planning, material control and root-cause problem solving; coordinated a 12-person technician team.")]),
]

EDUCATION = [
    ("B.Tech (EQF Level 6) — Technology Management & Mechanical Engineering", "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7.6/12"),
    ("Electrical & Mechanical Design, Electrical Engineering (EQF Level 6)", "Tehran Technical University · 2000–2003"),
    ("HF — Mathematics and Physics", "VUC · 2012–2017"),
]

CREDENTIALS = [
    ("Danish electrical authorisation LV/MV/HV", "Sikkerhedsstyrelsen · May 2023 · held as elautoriseret maskinmester"),
    ("PRINCE2 — certified project manager", "AXELOS / PeopleCert"),
    ("Refrigeration Technology & HVAC (AMU)", "Mercantec · 2021"),
    ("Lean and Six Sigma methods", "Applied in practice; not certified"),
    ("STCW engine-room and safety certificates", "Danish Maritime Authority · 2021–2023"),
]

METHODS = [
    ("Package/project controls", "PRINCE2 · scope and estimate · schedule and resource planning · risk and change follow-up · full P&L"),
    ("Electrical delivery", "LV/MV/HV · distribution boards · controls · HVAC interfaces · FAT/SAT · IQ/OQ/PQ · commissioning · handover"),
    ("Quality and safety", "QA records · LOTO · risk assessment · APV · site-start checks · deviation and near-miss follow-up · documentation"),
    ("People and coordination", "Daily labour allocation · 1:1 · MUS · apprentice training · daily huddles · stakeholder and subcontractor coordination"),
    ("Digital and reporting", "SAP ERP · CMMS · Power BI · Excel/Power Query · Python · Claude API · schedules · checklists · KPI dashboards"),
]

REQUIREMENTS = [
    ("Overall responsibility for the package team", "ELOHVAC: technical and commercial lead for electrical delivery, planning and handover; 5 electricians + 3 apprentices across 40+ service installations, with full P&L."),
    ("Labour control and coordination", "Daily allocation for 5 electricians and 3 apprentices; Ventek-Air capacity planning for 14 people across 11 concurrent projects."),
    ("Regular liaison with key stakeholders", "Novo: coordinated 25 specialists across engineering, procurement and site on 37 projects; monthly reports to management/client, plus ELOHVAC client and trade interfaces with project stakeholders."),
    ("Maintain quality standards and internal procedures", "FAT/SAT, IQ/OQ/PQ, validation and deviation records across 37 Novo projects, with zero critical findings at handover; ELOHVAC adds QA and handover files."),
    ("Maintain health and safety standards", "ELOHVAC LOTO, site-start risk assessment and work-environment follow-up; Biofos APV and near-miss process in 24/7 operations, with no unplanned stops in five years."),
    ("Electrical delivery from pre-construction to commissioning and handover", "ELOHVAC: estimate, scope, planning, materials, execution, QA and handover; Novo: FAT/SAT and qualification through acceptance across 37 concurrent projects."),
    ("Deliver on time and within budget", "Full P&L at ELOHVAC; schedule, budget and risk tracking at Novo; 37 projects reached handover with zero critical findings and 11 Ventek projects had formal handover."),
    ("Manage and develop an existing cross-functional team", "Daily leadership for 5 electricians + 3 apprentices, with training, 1:1 and MUS; led 14 at Ventek and coordinated 25 specialists at Novo."),
    ("Electrical trade background", "Electromechanical trade work and 12-person team leadership at ARJ; B.Tech in Technology Management & Mechanical Engineering; Danish electrical authorisation LV/MV/HV."),
    ("3–5 years in a similar role", "Since May 2023 (3+ years), ELOHVAC technical director in electrical contracting, labour, costs, subcontractors, QA and handover; project leadership also dates to 2022."),
    ("Experience managing electrical projects", "Novo: 37 concurrent electrical CAPEX projects, DKK 2–10m each, through commissioning with zero critical findings; ELOHVAC delivers from estimate through handover."),
    ("Delegation and organisation", "Plans and assigns work for ELOHVAC's 5+3 team; coordinated 11 parallel Ventek projects with 14 people and a 37-project, 25-specialist Novo portfolio, demonstrating organisational skills in concurrent delivery."),
    ("Lead and mentor a cross-functional team", "Structured apprentice training, 1:1 and MUS for ELOHVAC's 8-person team; led 14 at Ventek and coordinated 25 specialists across functions at Novo."),
    ("Collaborate with the wider project team", "Coordinated engineering, procurement and site across 37 Novo projects; aligned clients, suppliers, trades, production and installation teams at ELOHVAC/Ventek."),
    ("Strong written communication", "Monthly management/client reports, project and validation records at Novo; ELOHVAC estimates, schedules, QA files and client handover documentation."),
    ("Strong oral communication", "Daily huddles, toolbox talks, task allocation, 1:1s and stakeholder coordination with 25 specialists; Danish native and English professional."),
    ("Onsite in Copenhagen", "Based in Måløv in the Copenhagen area, with driving licence B; ELOHVAC and earlier project roles are Copenhagen-based, supporting onsite work."),
    ("Develop knowledge and skills through training and CPD", "PRINCE2, Danish electrical authorisation LV/MV/HV and applied Lean/Six Sigma; apprentice training and team development support continuous learning."),
    ("Contribute to a sustainable future and respect for people", "Novo PDCA reduced energy costs by 40%; safe work, apprentice development and documented handover support people, resource efficiency and responsible delivery."),
]

LANGUAGES = "Danish (native) · English (professional, written and spoken) · Persian/Farsi (native) · Driving licence B"
KEYWORDS = (
    "Electrical Package Manager · Electrical projects · Package team · Labour control · Labour coordination · "
    "Project stakeholders · Quality standards · Health and safety · Internal procedures · Pre-construction · "
    "Commissioning · Handover · On time · Within budget · Cross-functional team · Electrical trade · "
    "Delegation · Organisational skills · Lead and mentor · Wider project team · Written communication · "
    "Oral communication · Copenhagen · CPD · Continuous training · LV/MV/HV · FAT/SAT · LOTO · PRINCE2 · P&L"
)


def build(path=OUTPUT):
    m = MasterDoc(TEMPLATE, lang="en-GB")

    # Page 1 — application letter.
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta(RECIPIENT)
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, SUBJECT, bold=True, color="1A1A1A")
    m.para(OPENING, after=70, line=215)
    for t in LETTER:
        m.para(t, after=60, line=208)
    m.meta("Yours sincerely", after=18)
    m.meta("Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # CV, page 2 onwards.
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PACKAGE DELIVERY PROFILE")
    m.para(PROFILE, after=70)

    m.section("SELECTED DELIVERY RESULTS")
    for label, body in RESULTS:
        m.bullet(label, body, after=25)

    m.section("PROFESSIONAL EXPERIENCE")
    for title, meta, scope, bullets in EXPERIENCE[:2]:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=22)

    m.page_break()
    m.resume_header(NAME, "Electrical projects | teams | commissioning", CONTACT, "PROJECT DELIVERY EXPERIENCE")
    for title, meta, scope, bullets in EXPERIENCE[2:]:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=20)

    m.section("EDUCATION")
    for title, meta in EDUCATION:
        m.edu(title, meta)
    m.section("AUTHORISATIONS, CERTIFICATIONS & METHODS")
    for title, meta in CREDENTIALS:
        m.edu(title, meta)
    m.section("PROJECT DELIVERY TOOLKIT")
    m.models_table("APPLIED METHODS AND DIGITAL TOOLS", ("Area", "Evidence / tools"), METHODS)
    m.section("LANGUAGES")
    m.para(LANGUAGES, after=55, justify=False)

    m.page_break()
    m.resume_header(NAME, "Electrical Package Manager | Copenhagen", CONTACT, "EVIDENCE AGAINST THE ROLE")
    m.section("DOCUMENTED DELIVERY EVIDENCE")
    matrix = m.models_table("ROLE EVIDENCE", ("Requirement", "Evidence / application"), REQUIREMENTS, widths=(4100, 6246), compact=True)
    # Mark the two-column column-label row as a repeating header in Word.
    header_props = matrix.rows[1]._tr.get_or_add_trPr()
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    repeat_header = OxmlElement("w:tblHeader")
    repeat_header.set(qn("w:val"), "true")
    header_props.append(repeat_header)

    return m.save(path, title="Application and CV — Jones Engineering, Electrical Package Manager 145571",
                  subject=SUBJECT,
                  keywords="Electrical Package Manager; electrical delivery; labour control; commissioning; handover; safety; quality; Copenhagen")


if __name__ == "__main__":
    print(build())
