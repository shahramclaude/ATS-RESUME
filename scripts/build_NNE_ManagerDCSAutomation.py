#!/usr/bin/env python3
"""Build Shahram_Ajloo_NNE_ManagerDCSAutomation.docx (letter + CV in one document).
Manager, DCS Automation Department, NNE (Novo Nordisk Engineering), Kalundborg (req5151).
Deadline 10 December 2026. Contact: Senior Manager Ditte Hoeiberg Moeller. English document.
23.11.2026 user confirmations (unpinned, no platforms or year counts invented):
- extra pharma/life science experience beyond Novo Nordisk 20202024 = YES (claimed unpinned;
  the "5+ years" figure is NOT asserted in the document)
- concrete DCS/PLC/IT-OT experience = YES (claimed as categories only, no platform names)
Format per JD: no cover letter required; "why I am applying" included as Motivation block
inside the CV; no photograph. Career: Data Power first."""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_NNE_ManagerDCSAutomation.docx"

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
para("Application for Manager, DCS Automation Department, NNE", style="LetterTitle")
para("Dear Ditte Høiberg Møller", after=4)

para("Pharma facilities that produce medicines for millions of patients are built and "
     "commissioned in Kalundborg, and I have been on the customer side of that work: as "
     "Senior Commissioning Engineer and Project Manager at Novo Nordisk I took electrical "
     "systems from FAT/SAT through GMP qualification to handover, with zero critical "
     "deviations at acceptance. A newly established team in the DCS department now needs "
     "a manager who can lead engineers, stay close to the projects and help define the "
     "department's strategic direction, and that is the role I am applying for. I am a "
     "Maskinmester with a B.Tech degree in engineering, proven leadership of "
     "multidisciplinary teams, and concrete experience with DCS, PLC and IT/OT automation "
     "on top of my commissioning background.")

para("Leading 15 to 25 engineers in a multidisciplinary department is familiar ground: "
     "at Novo Nordisk I led 25 specialists across engineering disciplines through complex "
     "projects, and I lead by example with clear goals, 1:1s and competence development "
     "in daily collaboration. Working across countries is part of my background: my own "
     "career spans Iran and Denmark, and matrix management across parallel organisations "
     "is a working method I use. I stay actively involved in projects to keep up with "
     "technical development, and stakeholder communication with customer representatives "
     "is where my Novo Nordisk years give me a head start, since I know the customer's "
     "expectations from the inside.")

para("Setting strategic direction and translating it into execution is work I have done "
     "both as a company owner and as a project manager: roadmaps, priorities and follow-up "
     "that turn ambition into delivered projects, with PDCA, A3 and Lean as practical "
     "tools. The department's agenda of new ways of working, digital transformation and "
     "emerging technologies matches how I already work: as an active Claude and Python "
     "user I lead digitalisation initiatives and build tools that raise quality and speed, "
     "from AI-assisted documentation to KPI dashboards. My pharma and life science "
     "experience goes beyond the Novo Nordisk years, and my automation foundation covers "
     "DCS, PLC and IT/OT together with SCADA, control systems and commissioning of "
     "production equipment.")

para("The first 30 days I would spend in Kalundborg with the team, the customers and the "
     "projects: learning the department's ways of working and the needs across Denmark "
     "and India. By day 60 I would own the rhythm of team leadership, competence "
     "development and project involvement, with stakeholder communication running "
     "smoothly. By day 90 concrete initiatives for new ways of working and digital tools "
     "would be in motion, aligned with the department's strategic direction.")

para("I am used to the Kalundborg commute from my Novo Nordisk years, and I can be on "
     "site three days a week as the role requires. I would welcome a conversation about "
     "leading the DCS team, and I can be reached at +45 93 99 95 14.")

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

para("Why I am applying", style="CVH1")
para("I want to lead engineers where quality and patient safety set the standard, and "
     "the DCS department's combination of people leadership, technical depth and digital "
     "transformation is where my experience fits. Having commissioned plant at Novo "
     "Nordisk in Kalundborg, I know the customer side of NNE's work and want to build on "
     "that as a manager. Shaping a newly established team's ways of working across "
     "Denmark and India is a challenge that motivates me.")

para("Profile", style="CVH1")
para("Maskinmester (B.Tech) with proven leadership of multidisciplinary engineering teams "
     "and concrete experience with DCS, PLC and IT/OT automation in pharmaceutical "
     "environments. Combines team leadership and competence development with strategic "
     "execution, stakeholder communication and digital transformation (AI, Python); "
     "knows Novo Nordisk's Kalundborg environments from the commissioning side.")

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
bullet("Leadership: proven leadership of high-performing, multidisciplinary teams; "
       "managing 15-25 employees; visionary leadership, leading by example, ambitious goals, 1:1s and "
       "competence development (Situational Leadership, GROW).")
bullet("Pharma, biotech and life science: concrete experience from pharmaceutical production and "
       "complex engineering projects; GMP/FDA/EMA qualification and validation (FAT/SAT, IQ/OQ); API "
       "production context.")
bullet("Automation: concrete experience with DCS (Distributed Control Systems), PLC and "
       "IT/OT solutions; SCADA, control systems and commissioning of production "
       "equipment.")
bullet("Strategy: strategic direction translated into execution; roadmaps, priorities and "
       "follow-up; sustainable results.")
bullet("Ways of working: agile mindset, able to prioritize urgent tasks; innovation and "
       "digital transformation across emerging technologies; PDCA, A3 and Lean.")
bullet("Communication: stakeholder communication with customer representatives; "
       "cross-disciplinary collaboration; international teams (Denmark and India).")
bullet("Digital: digitalisation initiatives led; AI tools (Python, Claude Code), Power "
       "BI, SAP ERP, Excel/Power Query.")
bullet("Languages: English and Danish, written and spoken.")
bullet("Conditions: on site in Kalundborg three days per week; driving licence B; "
       "available after notice.")

# ----------------------------- QUALITY CHECK -----------------------------
full = "\n".join(p.text for p in doc.paragraphs)
banned = ["spearheaded", "leveraged", "passionate", "dynamic", "results-driven",
          "proven track record", "synergy", "cutting-edge", "innovative solutions",
          "seamlessly", "robust", "demonstrated ability", "fast-paced",
          "drevet", "lidenskabelig", "dynamisk", "synergi", "banebrydende",
          "sømløst", "ikke kun", "men også", "\u2014", "passion",
          "not only", "but also", "passionate", "innovative"]
hits = [w for w in banned if w.lower() in full.lower()]
jd_words = ["manager", "dcs", "automation", "distributed control systems", "plc",
  "it/ot", "pharma", "pharmaceutical", "api", "life science", "biotech", "validation",
  "engineering", "multidisciplinary", "teams", "competence development", "denmark",
  "india", "strategic direction", "strategy", "execution", "stakeholder", "customer",
  "kalundborg", "on site", "agile", "innovation", "new ways of working",
  "digital transformation", "emerging technologies", "bachelor", "degree", "english",
  "gmp", "commissioning", "project", "leadership", "high-performing",
  "cross-disciplinary", "prioritize", "motivate", "visionary"]
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
