# -*- coding: utf-8 -*-
"""Jones Engineering — Electrical Supervisor / Electrical Construction Supervisor, 145572.
English combined application + CV; transparent about UK-specific certificates not currently held.
Style: AG (accepted output, not merely installed); workfront → installation → evidence → commissioning;
register The Tagged Circuit Record. Danish authorisation is not represented as a UK ticket.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")
OUTPUT = os.path.join(ROOT, "Shahram_Ajloo_JonesEngineering_ElectricalSupervisor_145572.docx")
NAME = "SHAHRAM AJLOO"
TITLE = "Electrical Construction Supervisor · electrical projects · site teams · commissioning"
CONTACT = "+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark"
DATE = "3 November 2026"
RECIPIENT = "Jones Engineering · Copenhagen · Recruitment Team"
SUBJECT = "Electrical Supervisor — Copenhagen — Req 145572"

OPENING = (
    "A cable run is not productive output until it is installed to the current design, inspected, tagged, tested and ready for commissioning. "
    "The supervisor's job is to make that acceptance path visible before the crew starts."
)

LETTER = [
    "A workfront should be released only when the latest specification and drawing, safe method, access, labour, material and inspection point agree. A daily plan can then assign the work, responsible specialist contractor and acceptance evidence; a weekly look-ahead can expose labour or design constraints early enough to protect programme targets rather than explain a missed target afterwards.",
    "The practical control is one tagged-circuit record linked to the site plan: area and system, design revision, appointed contractor, work status, inspection hold point, tag identifier, test result, snag and owner, and commissioning/handover status. Quality Control, Safety and the construction team should agree the inspection and test path before work is concealed or energised. A performance test is not closed by a verbal update; its result and any corrective action belong in the project record.",
    "Daily coordination should review safe readiness and labour at each active workfront; the weekly review should compare planned with completed work, forecast the next sequence, and assign each design, material, quality or safety constraint an owner and due date. Specialist contractors remain accountable for their scope, while one site record makes dependencies and acceptance visible to the Senior Construction Manager, QC and commissioning. That is how project quality plans, tagging deliverables and productivity targets can support one another.",
    "The commissioning handover starts at installation, not at the end of the programme. Test sheets, tag schedules, inspection records, redlines, snags and retest evidence should reconcile to the same system identifier. In the first 30 days, map scopes, current programme, workfront readiness, quality plans, test packs and open safety/quality actions. By day 60, pilot the daily release and weekly look-ahead on a live area. By day 90, review accepted work, outstanding tests, tagged assets and handover gaps with the construction and commissioning teams; reset the plan using actual site constraints.",
    "Jones Engineering says its quality approach is “ensuring our client’s success”; “Quality is a Core Value” and “Quality underpins every aspect of our project delivery” are operational commitments at each release and inspection point. “Safety is our number one value” belongs there too. “Engineering Through People”, “Get Home Safe” and “Co-operation not competition” fit the work: appointed specialist contractors, QC, Safety and construction colleagues need a shared plan, candid escalation and documented close-out. This is the kind of quality- and safety-led Copenhagen site delivery that makes the role attractive.",
    "Qualification check, stated plainly: I hold Danish LV/MV/HV electrical authorisation as an elautoriseret maskinmester, and I am fluent in English. I do not hold BS 7671:2018/18th Edition, City & Guilds 2391/2394/2395, SSSTS/SMSTS, ECS or Safety Passport, and I do not hold a current First Aid certificate. I am not presenting the Danish authorisation as an equivalent to those UK credentials. Please confirm whether Jones can consider the Danish qualification for this Copenhagen role, or whether the specified UK awards must already be held before appointment/site access."
]

PROFILE = (
    "More than three years of comparable electrical site-supervision and contracting responsibility, confirmed by the candidate, "
    "with the ELOHVAC role documented from May 2023 to present: daily leadership of 5 electricians and 3 apprentices, work planning, "
    "materials, specialist subcontractors, quality records and handover, with full P&L. Additional evidence includes 37 concurrent "
    "electrical CAPEX projects with 25 specialists and zero critical findings at handover, plus 11 installation projects with a 14-person team. "
    "Danish electrical authorisation LV/MV/HV; fluent English. The UK certificates listed in this posting are not currently held."
)

RESULTS = [
    ("37 concurrent electrical CAPEX projects", "Novo Nordisk · 25 cross-functional specialists · FAT/SAT and IQ/OQ/PQ · zero critical findings at handover."),
    ("11 simultaneous installation projects", "Ventek-Air · 14-person team · specification, capacity, subcontractor coordination and formal handover."),
    ("5 electricians + 3 apprentices", "ELOHVAC · daily work planning, quality/safety follow-up and full P&L responsibility."),
    ("Over 40% productivity improvement", "ELOHVAC · Python/Claude tools for estimates, schedules, QA checklists and KPI reporting; not an installation-output claim."),
]

EXPERIENCE = [
    ("Owner / Technical Director / Authorised Electrical Engineer", "ELOHVAC ApS · Copenhagen · May 2023–present", "Electrical contracting · 5 electricians + 3 apprentices · full P&L", [
        "Lead electrical installation/service and project delivery from scope and quotation through planning, materials, specialist subcontractors, site work, quality records and handover.",
        "Direct daily leadership of 5 electricians and 3 apprentices: work allocation, one-to-ones, training, site-start risk assessment, LOTO and quality/safety follow-up.",
        "Own commercial estimates and full P&L; built Python/Claude tools for estimates, schedules, QA checklists and KPI reports, supporting a documented productivity improvement above 40%."
    ]),
    ("Co-owner and CTO · Technical Lead, AI / AI Coding", "Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 (concurrent with ELOHVAC)", "4–10 people", [
        "Led technical and industrial customer applications from requirements and architecture through integration, commissioning, documentation and handover; delivered LLM-API and AI-agent solutions.",
        "Introduced shared AI-assisted coding, review and test standards; used AI in management reporting and matrix leadership; applied AI coding to design options, calculations and sizing for technical plants and industrial components, with engineering validation before customer delivery."
    ]),
    ("Senior Commissioning Engineer / Electrical Project Manager", "Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024", "37 concurrent CAPEX projects · DKK 2–10m each · 25 specialists", [
        "Coordinated electrical scope, progress, cost, risk and resources across engineering, procurement and site; SAP ERP and monthly project reporting.",
        "FAT/SAT, IQ/OQ/PQ, validation documentation and deviation handling; zero critical findings at handover. PDCA programme reduced energy costs by 40% (an operational result, not a project-margin claim)."
    ]),
]

EXPERIENCE_MORE = [
    ("Project and Workshop Manager", "Ventek-Air · Copenhagen · Jan–Nov 2022", "11 concurrent installation projects · 14-person team", [
        "Daily huddles, capacity and bottleneck review; coordinated specification, production, installation, materials, subcontractors, quality and formal handover across parallel projects."
    ]),
    ("Operations and Maintenance Lead / Workshop Technician", "Biofos (Lynetten) · Copenhagen · Aug 2017–Jan 2022", "24/7 critical process operation · pumps, HVAC, HV switchboards, SCADA", [
        "Preventive maintenance and urgent fault-finding on electrical/mechanical plant; used asset criticality and operational need to prioritise work.",
        "Applied 5S, Standard Work and PDCA; LOTO, APV, risk assessment and near-miss follow-up within shift operations."
    ]),
    ("Electromechanic / Production Team Lead", "ARJ Engineering · Tehran · Dec 2003–Mar 2010", "12 mechanics and technicians", [
        "Led the 12-person technical/production team; electrical and mechanical fault-finding, shift planning, materials, root-cause analysis and corrective action."
    ]),
]

EDUCATION = [
    ("B.Tech (EQF 6), Technology Management & Mechanical Engineering", "Copenhagen School of Marine Engineering & Technology Management · 2017–2022"),
    ("Electrical & Mechanical Design, Electrical Engineering (EQF 6)", "Tehran Technical University · 2000–2003"),
    ("HF — Mathematics and Physics", "VUC · 2012–2017"),
    ("Danish electrical authorisation LV/MV/HV", "Sikkerhedsstyrelsen · May 2023 · elautoriseret maskinmester"),
    ("PRINCE2 · certified project manager", "AXELOS / PeopleCert"),
    ("Lean and Six Sigma", "Worked with in practice; not certified"),
    ("STCW engine-room and safety qualifications", "Danish Maritime Authority · 2021–2023; not a UK construction site card"),
]

QUALIFICATION_NOTE = (
    "Not currently held: BS 7671:2018 / 18th Edition; City & Guilds 2391, 2394 or 2395; SSSTS or SMSTS; ECS or Safety Passport; First Aid. "
    "Danish LV/MV/HV authorisation is listed separately and is not represented as a UK equivalent. BS 7671 guidance-note training/knowledge is not claimed."
)

METHODS = [
    ("Electrical/site delivery", "Danish LV/MV/HV authorisation · electrical installation/projects · controls and switchboards · FAT/SAT · IQ/OQ/PQ · commissioning and handover"),
    ("Workface and programme", "Electrical site supervisor · daily work allocation · daily work plans · weekly work plans · daily huddles · weekly look-ahead · construction programme · capacity/bottleneck review · materials · subcontractors · project documentation"),
    ("Quality and safety", "Quality procedures · industry standards · project safety · testing and commissioning · BS 7671:2018 (not held) · C&G 2391 (not held) · C&G 2394 (not held) · C&G 2395 (not held) · QA/checklists · LOTO · APV · risk assessment · near-miss follow-up · test/validation records · corrective actions"),
    ("Project and office tools", "PRINCE2 · SAP ERP · CMMS · Microsoft Office/Excel · Power BI · Power Query · Python · Claude Code"),
    ("English and location", "English: fluent (confirmed) · Danish: native · Persian/Farsi: native · based in Måløv, Copenhagen area · driving licence B"),
    ("Jones Engineering context", "ensuring our client’s success · Engineering Through People · Quality underpins every aspect of our project delivery · Get Home Safe · Safety is our number one value · Co-operation not competition · Relationships are at the heart of our business · customer focused project delivery · continuous training")
]

REQUIREMENTS = [
    ("Own appointed specialist contractors and meet client specifications", "ELOHVAC electrical projects include scope, customer requirements, planning, materials and specialist subcontractors through QA and handover. At Jones, release the scope and acceptance criteria to each contractor before work starts; my documented work leading five electricians and eight team members in total supports this workface coordination."),
    ("Develop and execute project quality plans and procedures", "ELOHVAC maintains QA checklists and handover documentation; Novo's 37 CAPEX projects used FAT/SAT, IQ/OQ/PQ and validation/deviation records, with zero critical findings at handover. Jones-specific plans must govern the site record."),
    ("Cooperate with construction and meet all tagging deliverables", "Tagging-system ownership is not claimed as past experience. A proposed tagged-circuit register links area/system, current drawing, tag ID, inspection/test evidence, snag owner and commissioning status with the construction team; the record structure can be agreed and used with each specialist contractor."),
    ("Support Jones Engineering's commissioning ethos and continuous improvement", "Novo electrical projects passed through FAT/SAT and IQ/OQ/PQ to handover; ELOHVAC closes service/project documentation at handover. PDCA reduced Novo energy costs 40%, an operational improvement rather than commissioning KPI."),
    ("Comply with project specifications, design and relevant standards", "Danish LV/MV/HV-authorised engineer with B.Tech and electrical project delivery. The candidate does not hold BS 7671:2018/18th Edition and does not claim UK standards qualification or equivalence; Jones must confirm eligibility."),
    ("Complete daily and weekly plans and meet or exceed targets", "Direct daily work allocation for 5 electricians and 3 apprentices; Ventek ran daily huddles and capacity review across 11 live projects with 14 people. A weekly look-ahead should expose constraints before target dates."),
    ("Drive productivity as a leading requirement", "ELOHVAC planning/QA/reporting tools improved productivity by over 40%; the figure is for workflow productivity, not installation metres, labour output or Jones site performance."),
    ("Manage day-to-day site activities and supervise site labour", "Candidate confirms 3+ years in a similar electrical site-supervision role. ELOHVAC documents direct daily leadership of 5 electricians and 3 apprentices, site planning, material readiness, quality/safety follow-up and handover."),
    ("Monitor specialist subcontractors and appointed contractors", "ELOHVAC project delivery includes specialist subcontractors, scope, materials, schedule and QA follow-up; Ventek coordinated materials and subcontractor interfaces. The proposed record assigns each scope, hold point, owner and close-out; the documented ELOHVAC team includes 5 electricians and 3 apprentices."),
    ("Assist Senior Construction Manager with programme planning and enforcement", "Novo coordinated scope, risk, cost and resources across 37 simultaneous electrical CAPEX projects; Ventek planned capacity over 11 parallel projects. Escalate constraints with owner, forecast impact and recovery option."),
    ("Manage and coordinate appointed subcontractors", "Direct contracting responsibility at ELOHVAC covers work scopes, materials, sequencing, quality and delivery interfaces. Align contractor look-aheads with construction access and inspection/commissioning dependencies; Ventek delivery coordinated a 14-person team across 11 concurrent projects."),
    ("Manage site safety and quality to company procedures", "ELOHVAC: LOTO, APV, site-start risk assessment and quality records; Biofos: near-miss and risk follow-up in 24/7 shift operations. Apply Jones procedures rather than importing unverified UK credentials."),
    ("Liaise with site Quality Control and Safety", "Novo evidence includes regulated testing, validation and deviation handling; ELOHVAC documents safety checks and QA. Proposed cadence reviews permits, inspection holds, findings and corrective-action owners with QC/Safety. Across 37 CAPEX projects Novo's team recorded zero critical findings at handover."),
    ("Collaborate effectively with the project team", "Novo: cross-functional coordination of 25 specialists in engineering, procurement and site; Ventek: 14-person delivery team. Daily issue/constraint review makes dependencies visible to the wider construction team."),
    ("Supervise performance tests when required", "FAT/SAT and IQ/OQ/PQ across 37 Novo CAPEX projects are documented; ELOHVAC electrical service closes QA/handover records. No claim is made of UK C&G inspection/testing certification."),
    ("Maintain project documentation", "ELOHVAC prepares QA checklists, schedules and handover files; Novo retained commissioning/validation records across 37 projects. A proposed tag-to-test index prevents a test sheet becoming detached from its circuit."),
    ("Attend required meetings", "Daily huddles and capacity reviews at Ventek; direct daily team planning and 1:1s at ELOHVAC; project reporting and cross-functional reviews at Novo. English fluency is confirmed."),
    ("Minimum three years in a similar role", "Candidate confirms 3+ years of comparable electrical site supervision; ELOHVAC electrical contracting/site-delivery leadership runs from May 2023. Use this as comparable experience, not as a claim of a UK title."),
    ("Fluent English", "Candidate confirms fluent spoken and written English; master record previously described professional English. This confirmation supports site meetings, contractor coordination and project records; English was used in Novo's cross-functional work with 25 specialists."),
    ("Electrical installation qualifications", "B.Tech (EQF 6) in Technology Management & Mechanical Engineering, Electrical Engineering studies (EQF 6), and Danish LV/MV/HV electrical authorisation as elautoriseret maskinmester, awarded May 2023. The Danish award is stated accurately, not renamed as a UK electrician certificate."),
    ("BS 7671:2018 / 18th Edition qualification", "Not currently held. The application does not claim an 18th Edition certificate or equivalency; asks Jones whether the Danish LV/MV/HV authorisation can be assessed and what must be completed before site assignment."),
    ("City & Guilds 2391 or 2394/2395", "None of the listed C&G certificates is currently held. FAT/SAT and IQ/OQ/PQ experience is not presented as a C&G inspection/testing qualification."),
    ("Knowledge of BS 7671 guidance notes and installation methods", "The master record documents Danish installation authorisation and electrical project work, not UK BS 7671 guidance-note training. No claim of UK-code knowledge is made; the required local standard must be confirmed with Jones."),
    ("Microsoft Office knowledge", "Excel/Power Query, KPI reporting, schedules, documentation and monthly reporting are documented; the CV lists Microsoft Office/Excel without claiming a specific Jones project system."),
    ("Excellent communication and interpersonal skills", "Daily task allocation, huddles, 1:1/MUS, apprentice training and multi-party project coordination across 25 specialists; fluent English is candidate-confirmed and Danish is native."),
    ("SSSTS or SMSTS mandatory", "Neither SSSTS nor SMSTS is currently held. The CV does not substitute Danish risk assessment/LOTO practice for these UK site-supervision certificates."),
    ("ECS or Safety Passport H&S qualifications mandatory", "Neither an ECS card nor the specified Safety Passport is currently held. Danish electrical authorisation is listed separately and is not presented as a site safety card."),
    ("First Aid desirable", "Candidate confirms no current First Aid certificate. This desirable qualification is disclosed accurately; no course completion or validity date is implied."),
    ("Copenhagen workplace", "Based in Måløv in the Copenhagen area, with driving licence B; the ELOHVAC and earlier project roles are Copenhagen-based, supporting onsite attendance.")
]


def _add_jobs(m, jobs):
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope)
        for text in bullets:
            m.bullet("", text, after=14, line=205)


def build(path=OUTPUT):
    m = MasterDoc(TEMPLATE, lang="en-GB")
    # Page 1: task-first letter with the UK qualification gap disclosed explicitly.
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta(RECIPIENT)
    p = m._p(spacing_after=55, line=245, justify=False)
    m._run(p, SUBJECT, bold=True)
    m.para(OPENING, after=40, line=210)
    m.para("Dear Jones Engineering Recruitment Team", after=35, line=205, justify=False)
    for text in LETTER:
        m.para(text, after=38, line=205)
    m.meta("Yours sincerely", after=8)
    m.meta("Shahram Ajloo", after=0)

    # Page 2: role profile and current/concurrent roles.
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "SITE DELIVERY PROFILE")
    m.section("PROFILE")
    m.para(PROFILE, after=24, line=200)
    m.section("SELECTED DELIVERY EVIDENCE")
    for label, detail in RESULTS:
        m.bullet(label, detail, after=9, line=190)
    m.section("PROFESSIONAL EXPERIENCE")
    _add_jobs(m, EXPERIENCE[:2])

    # Page 3: previous site/project roles, credentials and toolkit.
    m.page_break()
    m.resume_header(NAME, "Electrical installation · teams · testing · handover", CONTACT, "PROJECT EXPERIENCE AND QUALIFICATIONS")
    _add_jobs(m, EXPERIENCE[2:] + EXPERIENCE_MORE)
    m.section("EDUCATION AND PROFESSIONAL CREDENTIALS")
    for title, detail in EDUCATION:
        m.edu(title, detail)
    m.para(QUALIFICATION_NOTE, after=20, line=190)
    m.section("PROJECT DELIVERY TOOLKIT")
    m.models_table("DOCUMENTED PRACTICE AND EMPLOYER CONTEXT", ("Area", "Tools / evidence"), METHODS, widths=(2300, 8046), compact=True)

    # Page 4 (and, if required by the layout, a continuation): one row per job requirement.
    m.page_break()
    m.resume_header(NAME, "Electrical Construction Supervisor · Req 145572 · Copenhagen", CONTACT, "REQUIREMENTS AND EVIDENCE")
    m.para("UK-specific qualification gaps are shown as open requirements; Danish authorisation is not described as an equivalent. For example: BS 7671:2018 (also written BS7671:2018), City & Guilds 2391/2394/2395 and SSSTS/SMSTS are not currently held.", after=16, line=190)
    table = m.models_table("JOB REQUIREMENTS AND DOCUMENTED EVIDENCE", ("Requirement", "Evidence / status"), REQUIREMENTS,
                           widths=(3650, 6696), compact=True)
    return m.save(path, title="Application and CV — Jones Engineering Electrical Supervisor 145572",
                  subject=SUBJECT,
                  keywords="Electrical Supervisor; Electrical Construction Supervisor; Copenhagen; site supervision; project quality; commissioning; British Standard BS 7671:2018; C&G 2391; SSSTS; SMSTS; ECS; Safety Passport")


if __name__ == "__main__":
    print(build())
