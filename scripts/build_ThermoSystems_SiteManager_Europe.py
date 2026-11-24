#!/usr/bin/env python3
"""Build Shahram_Ajloo_ThermoSystems_SiteManager_Europe.docx (letter + CV).
Site Manager (Europe), Thermo Systems (control systems integration; Odense/Dublin/Berlin
offices; Energy, Life Sciences, Mission Critical). English document.
23.11.2026 user confirmations (unpinned): RFIs, redlines, as-builts = concrete experience;
Teams/SharePoint = daily use. Site installation leadership + safety + electrical contractors
+ GC-led job sites all grounded in master (Novo, Ventek, Biofos, ELOHVAC/Data Power).
Career: Data Power first."""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_ThermoSystems_SiteManager_Europe.docx"

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
para("Application for Site Manager (Europe), Thermo Systems", style="LetterTitle")
para("Dear Thermo Systems Recruitment Team", after=4)

para("When installation week arrives on a project, the plan either holds in the field or "
     "it does not: drawings current and version-controlled, crews and trades coordinated, "
     "safety enforced and every change documented before it costs schedule. That field "
     "discipline is what Thermo Systems projects need from a Site Manager, and it is how I "
     "have worked for years. I am a Maskinmester with a B.Tech degree in engineering and "
     "an authorisation covering LV/MV/HV, and I have spent more than twenty years in "
     "industrial field work and project execution: electrical installations, switchboards, "
     "control systems, ventilation and commissioning, from urgent call-outs to "
     "handed-over plants.")

para("On-site coordination of installation activities with safety, quality and execution "
     "as one discipline is my daily practice: I have led field teams and subcontractors on "
     "manufacturing and energy sites, from utility plants at Novo Nordisk and Biofos to my "
     "own contracting business where I managed electrical contractors and full project "
     "delivery. Safety-first is not a slogan for me: LOTO, risk assessments, work "
     "environment assessments and near-miss reporting are routines I enforce and follow, "
     "and handover documentation and punch lists are closed before I call a project done.")

para("Schedule monitoring and field coordination come from running 11 concurrent plant "
     "projects and a portfolio of 37 at Novo Nordisk: short-interval planning, daily and "
     "weekly coordination meetings, risk identification and corrective action before "
     "milestones slip. As the site's point of contact for customers, general contractors "
     "and subcontractors I keep communication, documentation and escalation consistent, "
     "and my change management covers the full loop: RFIs, redlines, as-built "
     "documentation and the field data behind change orders, with accurate inputs for "
     "cost, schedule and scope adjustments.")

para("The first 30 days I would spend on site and in the drawings: the project plan, "
     "installation sequences, drawing status and the key stakeholders across customers, "
     "contractors and the Project Manager. By day 60 I would own the daily coordination "
     "rhythm, version control of field documentation and readiness tracking, and by day 90 "
     "the reporting and documentation would run to Thermo Systems standards with risks and "
     "milestones visible at a glance. I work fluently with collaboration tools including "
     "Teams and SharePoint and with scheduling and progress tracking in practice.")

para("I am based in Måløv and ready for the travel and site presence this role requires, "
     "and I can start after notice. I would welcome a conversation about leading "
     "installation execution on Thermo Systems projects in Europe, and I can be reached at "
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
para("Maskinmester (B.Tech) with more than twenty years of industrial field and project "
     "execution: site coordination of installation activities with safety, quality and "
     "schedule alignment across electrical, controls and utility scopes. Experienced with "
     "electrical contractors and GC-led job sites, change management (RFIs, redlines, "
     "as-builts) and commissioning readiness, from planning through punch list closure to "
     "documented handover.")

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
bullet("Site installation leadership: day-to-day coordination of installation "
       "activities; safety-first culture (LOTO, risk assessment, work environment "
       "assessments, near-miss); installation quality, inspections and punch list "
       "completion.")
bullet("Schedule and field coordination: progress tracked against project schedules and "
       "short-interval plans; risk identification and corrective actions; daily and weekly "
       "site meetings including trade coordination; site constraints communicated to "
       "project leadership.")
bullet("Stakeholder liaison: on-site point of contact for customers, general contractors "
       "and subcontractors; coordination with safety and quality representatives; "
       "consistent communication, documentation and escalation.")
bullet("Engineering and drawing control: version control of installation drawings and "
       "field documentation; constructability and design issues resolved with engineering; "
       "RFIs, redlines and as-built documentation (concrete experience).")
bullet("Change management and commercial support: field-driven scope changes identified; "
       "change order documentation and field data collection; accurate inputs for cost, "
       "schedule and scope adjustments; supplementary and reduced work settled.")
bullet("Project manager coordination and reporting: execution and schedule alignment; "
       "regular site updates with progress, risks and key milestones; reporting and "
       "documentation to set standards.")
bullet("Material, workface and readiness: material deliveries, staging and inventory "
       "management on site; workface planning so crews have tools, materials and access; "
       "commissioning readiness, installation completion and punch list closure.")
bullet("Technical: electrical installations, switchboards and control systems, ventilation "
       "and cooling; MS Office, Teams, SharePoint (daily use), Power Query; SAP ERP; "
       "scheduling and progress tracking in practice.")
bullet("Languages: English (fluent) and Danish (native).")
bullet("Conditions: based in Måløv; high travel and site presence across Europe accepted; "
       "driving licence B; available after notice.")

# ----------------------------- QUALITY CHECK -----------------------------
full = "\n".join(p.text for p in doc.paragraphs)
banned = ["spearheaded", "leveraged", "passionate", "dynamic", "results-driven",
          "proven track record", "synergy", "cutting-edge", "innovative solutions",
          "seamlessly", "robust", "demonstrated ability", "fast-paced",
          "drevet", "lidenskabelig", "dynamisk", "synergi", "banebrydende",
          "sømløst", "ikke kun", "men også", "\u2014", "passion",
          "not only", "but also", "passionate", "innovative"]
hits = [w for w in banned if w.lower() in full.lower()]
jd_words = ["site manager", "site", "installation", "safety", "quality", "execution",
  "coordination", "schedule", "field", "drawings", "version control", "redlines", "rfis",
  "as-built", "change management", "change order", "customers", "general contractors",
  "subcontractors", "stakeholders", "documentation", "escalation", "punch list",
  "commissioning", "readiness", "material", "inventory", "risks", "milestones",
  "corrective", "communication", "collaboration", "teams", "sharepoint", "scheduling",
  "progress", "electrical contractors", "industrial", "manufacturing", "energy",
  "tracking", "inspections"]
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
