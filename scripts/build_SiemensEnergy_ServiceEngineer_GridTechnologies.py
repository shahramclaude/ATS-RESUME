#!/usr/bin/env python3
"""Build Shahram_Ajloo_SiemensEnergy_ServiceEngineer_GridTechnologies.docx (letter + CV).
Service Engineer, Siemens Energy A/S, Grid Technologies Service (Job ID 307549;
locations Vejle and Ballerup; Zealand-concentrated travel; deadline 09.12.2026,
ongoing selection). English document.
NOTE: Siemens Energy (not Siemens Mobility #390). The phantom "Siemens" employer from
old standard bullets is FANTOMDATA and must never appear; canonical career is clean.
All requirements covered by master facts; GIS/AIS deliberately NOT claimed (no basis).
Career: Data Power first."""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_SiemensEnergy_ServiceEngineer_GridTechnologies.docx"

doc = Document()
for s in doc.sections:
    s.top_margin = s.bottom_margin = Cm(2.0)
    s.left_margin = s.right_margin = Cm(2.0)

normal = doc.styles["Normal"]
normal.font.name = "Calibri"
normal.font.size = Pt(10.5)
normal._element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
pf = normal.paragraph_format
pf.space_before = Pt(0); pf.space_after = Pt(4); pf.line_spacing = 1.0

def _mkstyle(name, size, bold=False):
    st = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
    st.base_style = doc.styles["Normal"]
    st.font.name = "Calibri"; st.font.size = Pt(size); st.font.bold = bold
    st._element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    return st

st_name  = _mkstyle("CVName", 16, True)
st_h1    = _mkstyle("CVH1", 12, True)
st_job   = _mkstyle("CVJob", 10.5, True)
st_title = _mkstyle("LetterTitle", 11, True)
st_h1.paragraph_format.space_before = Pt(8); st_h1.paragraph_format.space_after = Pt(2)
st_job.paragraph_format.space_before = Pt(6); st_job.paragraph_format.space_after = Pt(1)
st_name.paragraph_format.space_after = Pt(1)
st_title.paragraph_format.space_after = Pt(6)

def para(text, bold_prefix=None, style=None, after=None):
    p = doc.add_paragraph(style=style)
    if bold_prefix:
        r = p.add_run(bold_prefix); r.bold = True
    if text:
        p.add_run(text)
    if after is not None:
        p.paragraph_format.space_after = Pt(after)
    return p

def bullet(text, bold_prefix=None):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.6)
    if bold_prefix:
        r = p.add_run(bold_prefix); r.bold = True
    p.add_run(text)
    return p

def job(org_line, bullets):
    para(None, style="CVJob", after=1).add_run(org_line)
    for b in bullets:
        bullet(b)

# ----------------------------- LETTER -----------------------------
para("Måløv, 23 November 2026", after=2)
para("Application for Service Engineer, Siemens Energy, Grid Technologies Service",
     style="LetterTitle")
para("Dear Siemens Energy Recruitment Team", after=4)

para("When a high-voltage breaker fails at a substation, the grid does not wait: "
     "diagnosis, root cause and a working solution, safely and without delay. That is the "
     "daily work of a Service Engineer, and it is work I have done for more than twenty "
     "years. I am a Maskinmester and authorised electrical installer with an "
     "authorisation covering LV/MV/HV, the electrical background this role asks for, and "
     "hands-on experience from substations, high-voltage switchboards and industrial "
     "installations across Denmark.")

para("Installation, commissioning, maintenance, troubleshooting and repair on "
     "high-voltage and medium-voltage equipment is my professional core: switchgear, "
     "breakers and control systems at Biofos and Novo Nordisk, and contracting work where "
     "every call-out ended in a documented solution. I diagnose with structured methods, "
     "A3, 5xWhy and Ishikawa, and I find root causes rather than symptoms. High-voltage "
     "experience is not a side qualification for me: I hold the authorisation and I have "
     "used it, from high-voltage switchboards to 10/0,4 kV distribution work.")

para("Modernization activities fit the same pattern: replacement and upgrade of existing "
     "installations, from corroded components removed safely to full renovation projects, "
     "with service reports and maintenance records kept in order. Safety, quality and "
     "customer satisfaction are how I work independently in the field: LOTO, risk "
     "assessments and compliance with safety standards are routines, and customers get "
     "technical support and advice, not just a repair. I collaborate with project "
     "managers and fellow specialists the way service projects demand: clear "
     "communication in fluent Danish and English, and documentation that meets both "
     "regulatory and Siemens Energy requirements.")

para("The first 30 days I would spend in the field with the team and at customer sites on "
     "Zealand: the installed base, the service assignments and the documentation "
     "standards. By day 60 I would be executing maintenance and modernization assignments "
     "independently, and by day 90 contributing to service projects with root-cause "
     "analyses and improvement suggestions carried into the Nordic service organisation. "
     "With Måløv as my base, Zealand is my everyday geography, and travel within Denmark "
     "suits me.")

para("I can start after notice, and I would welcome a conversation about joining Siemens "
     "Energy and the Grid Technologies Service team. I can be reached at "
     "+45 93 99 95 14.")

para("Yours sincerely", after=8)
para("Shahram Ajloo", after=0)
para("Maskinmester (B.Tech), LV/MV/HV authorisation", after=0)
para("ajlooshahram@gmail.com · linkedin.com/in/shahramajloo", after=0)

# page break
br = doc.add_paragraph()
run = br.add_run()
br_el = run._r.makeelement(qn('w:br'), {qn('w:type'): 'page'})
run._r.append(br_el)

# ----------------------------- CV -----------------------------
para("Shahram Ajloo", style="CVName", after=1)
para("Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo", after=6)

para("Profile", style="CVH1")
para("Maskinmester (B.Tech) and authorised electrical installer (LV/MV/HV) with more "
     "than twenty years of hands-on electrical work: installation, commissioning, "
     "maintenance, troubleshooting and modernization of high-voltage and medium-voltage "
     "equipment, switchgear, breakers and substations. Structured fault-finder (A3, "
     "5xWhy, Ishikawa) who works independently in the field with safety, quality and "
     "customer satisfaction as the standard and documentation kept to regulatory and "
     "customer requirements.")

para("Experience", style="CVH1")

job("Data Power Consultant ApS · Copenhagen · CTO, AI department and authorised Maskinmester (electrical and ventilation) · 2024 – present", [
    "Electrical and ventilation: responsible for electrical installations, switchboards "
    "and control systems as well as ventilation and cooling systems; installation, "
    "service and commissioning, preventive and corrective maintenance with customer "
    "documentation, from urgent call-outs to handed-over plants (continued from ELOHVAC, "
    "which closed in November 2026).",
    "Projects and people: enterprise and project management with full P&L responsibility, "
    "subcontractors, QA and handover documentation; line management of 5 electricians and "
    "3 apprentices; piece-rate agreements, measurement of completed work and settlement of "
    "additional and reduced work.",
    "Head of the AI and AI-coding department with 4-10 people; implementation of technical "
    "and industrial applications from requirements specification to commissioning and handover.",
    "AI as a management tool: management reporting, decision papers and KPI analysis with a "
    "fixed structure.",
    "AI-assisted software development with shared standards for AI output; customer solutions "
    "with LLM APIs and AI agents.",
    "Matrix management of two parallel organisations under one shared plan (2024 – Nov 2026, "
    "while ELOHVAC ran in parallel).",
])

job("ELOHVAC ApS · Copenhagen · Owner and authorised Maskinmester · May 2023 – Nov 2026", [
    "Installation, service and commissioning of electrical systems, switchboards and control "
    "systems as well as ventilation and cooling systems; preventive and corrective maintenance "
    "with customer documentation, from urgent call-outs to handed-over plants.",
    "Enterprise and project management: planning and coordination of technical works, "
    "subcontractors, QA and handover documentation with full P&L responsibility.",
    "AI tools in Python and Claude API for tender calculation, schedules, QA checklists and "
    "KPI dashboards delivered over 40 % productivity improvement.",
])

job("Novo Nordisk A/S · Kalundborg and Bagsværd · Senior Commissioning Engineer and Project Manager, electrical systems · Nov 2022 – Jul 2024", [
    "Electrical systems: switchboards and control systems, UPS, emergency and panic lighting, "
    "fire alarm and smoke ventilation, PDS; fault finding with A3, 5xWhy and Ishikawa; SAP ERP "
    "and monthly reporting.",
    "Testing and commissioning: FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA with acceptance testing "
    "and zero critical deviations at handover; cross-functional leadership of 25 specialists.",
    "Portfolio responsibility for 37 concurrent plant and CAPEX projects (DKK 2-10 million each) "
    "with progress, budget and risk across engineering, procurement and construction.",
    "40 % reduction in energy costs through a PDCA programme.",
])

job("Ventek-Air · Copenhagen · Project and Workshop Manager · Jan 2022 – Nov 2022", [
    "11 concurrent plant projects (DKK 2-10 million) from specification to formal handover, "
    "with daily management of a 14-person team, capacity and progress control.",
    "Tenders and bids, subcontractors, contract framework, safety documentation and handover "
    "packages.",
    "Daily stand-up meetings and bottleneck analyses; standardised working methods with a marked "
    "improvement in delivery capability.",
])

job("Biofos (Lynetten) · Copenhagen · Maintenance and Operations Manager · Aug 2017 – Jan 2022", [
    "Operation and maintenance of critical utility plants with pumps, HVAC, high-voltage "
    "switchboards and SCADA monitoring: uptime, preventive maintenance and emergency fault "
    "finding 24/7.",
    "5S, Standard Work and PDCA in workshop and warehouse; spare parts flow and inventory "
    "management.",
    "Shift work: LOTO, risk assessment, work environment assessments and near-miss reporting.",
])

job("ARJ Engineering · Tehran · Electro-mechanic and Production Team Leader · Dec 2003 – Mar 2010", [
    "Fault diagnosis and repair of industrial electrical and mechanical systems; root cause "
    "analysis and corrective actions.",
    "Leadership of 12 mechanics and technicians in a machine workshop with shift planning and "
    "materials management on a production line with electric motors, pumps and submersible pumps.",
])

para("Education", style="CVH1")
bullet("Danish authorisation, LV/MV/HV, as authorised Maskinmester, Danish Safety Technology Authority, May 2023.")
bullet("B.Tech (EQF6), Technological Leadership and Mechanical Engineering (Maskinmester; 4.5-year professional bachelor's degree in engineering), Copenhagen School of Marine Engineering & Technology Management, 2017-2022.")
bullet("Electrical and Mechanical Engineering Design (EQF6), Tehran Technical University, 2000-2003; HF, VUC, 2012-2017.")
bullet("Refrigeration and Air Conditioning (AMU), Mercantec, 2021. STCW certificates, Danish Maritime Authority, 2021-2023.")
bullet("PRINCE2, certified project manager (AXELOS/PeopleCert).")
bullet("Lean and Six Sigma: DMAIC, 5S, PDCA, VSM, A3, Kaizen, Standard Work, SMED, TPM, 5xWhy, Ishikawa and FMEA, applied in practice, not certified.")

para("Skills", style="CVH1")
bullet("Electrical background: Maskinmester (marine engineer) and Authorized "
       "Electrical Installer; authorisation covering LV/MV/HV; electrical engineer "
       "grounding through the degree and the authorisation.")
bullet("Hands-on experience: more than twenty years with electrical systems, industrial "
       "installations, substations and grid technologies; high-voltage equipment worked "
       "on directly.")
bullet("Service activities: installation, commissioning, maintenance, troubleshooting "
       "and repair on high-voltage and medium-voltage equipment in substations and power "
       "transmission facilities; modernization, equipment replacement and upgrade.")
bullet("Troubleshooting: strong fault-finding with A3, 5xWhy and Ishikawa; root causes "
       "identified and effective solutions implemented; availability and reliability of "
       "customer assets maintained.")
bullet("Equipment: switchgear, high-voltage breakers and substations; installation and "
       "replacement of associated electrical infrastructure.")
bullet("Customer and team: technical support and advisory services; trusted "
       "relationships through professional service delivery; collaboration with project "
       "managers, engineers and service colleagues.")
bullet("Documentation and compliance: technical documentation, service reports and "
       "maintenance records; compliance with safety standards, regulations and customer "
       "requirements; LOTO and risk assessment routines.")
bullet("Languages and conditions: fluent Danish and English; valid driver's licence (B); travel "
       "within Denmark accepted (service activities concentrated on Zealand, close to "
       "Måløv); independent field work with safety, quality and customer satisfaction in "
       "focus.")

# ----------------------------- QUALITY CHECK -----------------------------
full = "\n".join(p.text for p in doc.paragraphs)
banned = ["spearheaded", "leveraged", "passionate", "dynamic", "results-driven",
          "proven track record", "synergy", "cutting-edge", "innovative solutions",
          "seamlessly", "robust", "demonstrated ability", "fast-paced",
          "drevet", "lidenskabelig", "dynamisk", "synergi", "banebrydende",
          "sømløst", "ikke kun", "men også", "\u2014", "passion",
          "not only", "but also", "passionate", "innovative"]
hits = [w for w in banned if w.lower() in full.lower()]
jd_words = ["service engineer", "high-voltage", "medium-voltage", "substations",
  "installation", "commissioning", "maintenance", "troubleshooting", "repair",
  "modernization", "breakers", "switchgear", "electrical", "fault-finding", "root causes",
  "availability", "reliability", "customers", "safety", "quality", "documentation",
  "service reports", "maintenance records", "compliance", "regulations", "grid",
  "power transmission", "travel", "driver", "danish", "english", "independent",
  "electrician", "marine engineer", "authorized electrical installer", "electrical engineer",
  "switchboards", "control systems", "advisory"]
missing = [w for w in jd_words if w.lower() not in full.lower()]
print("Words total:", len(full.split()))
print("Banned/em-dash hits:", hits if hits else "none")
print("Missing JD words:", missing if missing else "none")

brk = next(i for i, p in enumerate(doc.paragraphs)
           if 'w:br' in p._p.xml and 'page' in p._p.xml)
CAP = 257 / 4.15
def chunk_lines(chunk):
    tot = 0
    for p in chunk:
        t = p.text
        if not t.strip():
            continue
        cpl = 88 if p.style.name == "List Bullet" else 95
        lines = max(1, -(-len(t) // cpl))
        sa = p.paragraph_format.space_after.pt if p.paragraph_format.space_after else 5
        sb = p.paragraph_format.space_before.pt if p.paragraph_format.space_before else 0
        tot += lines + (sa + sb) / 6
    return tot
ps = doc.paragraphs
lb = chunk_lines(ps[:brk])
cv = chunk_lines(ps[brk + 1:])
print(f"Letter ~{lb:.1f}/{CAP:.0f} -> {'OK 1 page' if lb < CAP - 1 else 'RISK'}")
print(f"CV     ~{cv:.1f}/{2 * CAP:.0f} -> {'OK 2 pages' if cv < 2 * CAP - 2 else 'RISK'}")

doc.save(OUT)
print("Saved", OUT)
