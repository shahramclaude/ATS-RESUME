#!/usr/bin/env python3
"""Build Shahram_Ajloo_Coloplast_ProductDevelopmentProjectManager.docx (letter + CV).
Product Development Project Manager, Coloplast A/S, Humlebaek (req 62149; contact:
Majk Kruszewski, Senior Director Product Development; continuous screening, apply ASAP).
English document.
23.11.2026 user confirmations (unpinned, all concrete): R&D/product development project
leadership 5+ years; full chain concept - detailed development - verification -
manufacturing transfer; Design Control documentation. Regulated industry: Novo Nordisk
GMP/FDA/EMA (master). Career: Data Power first."""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_Coloplast_ProductDevelopmentProjectManager.docx"

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
para("Application for Product Development Project Manager, Coloplast",
     style="LetterTitle")
para("Dear Majk Kruszewski", after=4)

para("Every product that reaches a patient carries the trail of decisions behind it: "
     "concept choices, design trade-offs, verification evidence and a production line "
     "that was ready on the day of transfer. Leading the Product Development workstream "
     "means owning that trail from defined scope to launch-ready solutions. I am a "
     "Maskinmester with a B.Tech degree in engineering and more than fifteen years of "
     "technical project leadership, and I come from a regulated industry: at Novo Nordisk "
     "I led commissioning and project execution under GMP, FDA and EMA requirements, "
     "where documentation reviewed against requirements before release was the daily "
     "standard.")

para("Leading a multidisciplinary R&D development team is concrete experience for me: "
     "I led "
     "25 specialists across engineering disciplines through complex projects at Novo "
     "Nordisk, built an AI department from 4 to 10 people, and run my own technical "
     "company with full P&L responsibility. Scope translated into deliverables, "
     "milestones, dependencies and decision points is how I plan: portfolio "
     "responsibility for 37 concurrent projects taught me to keep risks, issues and "
     "critical dependencies visible and to make trade-offs across quality, "
     "manufacturability, time and cost explicit before they become surprises.")

para("Taking products through concept development, detailed development, verification "
     "and transfer into manufacturing is work I have done end to end: requirements and "
     "specifications developed with the team, verification evidence delivered through "
     "FAT/SAT and IQ/OQ/PQ, and designs transferred to production with manufacturing "
     "readiness confirmed. Design Control documentation is familiar ground: structured "
     "records, reviews against requirements and traceability from input to verified "
     "output. Partnering with manufacturing so that design and manufacturing readiness "
     "run from the outset is how my projects have been run.")

para("The first 30 days I would spend inside the project and the workstream: the scope, "
     "the concept status, the team and the verification plan. By day 60 I would own the "
     "integrated workstream plan, the resource forecast aligned with line managers and "
     "the risk picture, and by day 90 decisions, trade-offs and recommendations would be "
     "flowing clearly to the project organisation while deliverables reached the required "
     "maturity on schedule. I ask the difficult questions early, and I keep ownership "
     "clear when decisions need broader alignment.")

para("Humlebæk is an easy commute from Måløv, and I can start after notice. I would "
     "welcome a conversation with you about leading Product Development workstreams at "
     "Coloplast, and I can be reached at +45 93 99 95 14.")

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
para("Maskinmester (B.Tech) with more than fifteen years of technical project leadership "
     "in regulated environments: leads multidisciplinary development teams from defined "
     "scope to verified, transferable and launch-ready deliverables. Concrete experience "
     "across the full product chain (concept, detailed development, verification, "
     "manufacturing transfer) with Design Control documentation, risk and dependency "
     "management and trade-offs across quality, time and cost.")

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
bullet("Product Development workstream: early development through design "
       "verification, design transfer and launch readiness led; scope translated into "
       "deliverables, milestones, dependencies and decision points; workstream plan "
       "integrated with the overall project plan.")
bullet("Team leadership: multidisciplinary development teams built and led (25 "
       "specialists at Novo Nordisk; 4-10 specialists today); clear ownership of "
       "deliverables created; risks, issues and critical dependencies actively managed.")
bullet("Product chain: concept development, detailed development, verification and "
       "transfer into manufacturing (concrete experience end to end); product concepts, "
       "designs, requirements, specifications and verification evidence (FAT/SAT, "
       "IQ/OQ/PQ).")
bullet("Design Control: Design Control documentation in structured form (concrete "
       "experience); traceability from requirements to verified output; documentation "
       "reviewed against requirements before release.")
bullet("Manufacturing integration: partnership with manufacturing development; Design "
       "for Manufacturing and manufacturing-readiness activities from the outset; design "
       "transfer to production.")
bullet("Decisions and trade-offs: timely decisions within mandate; technical "
       "recommendations, assumptions and trade-offs made visible across product "
       "performance, quality, manufacturability, sustainability, time and cost; "
       "escalation when broader alignment is needed.")
bullet("Planning and communication: project planning, risk management and dependency "
       "management; resource and OPEX forecasts aligned with line managers; progress, "
       "risks and decisions communicated clearly to project organisations and "
       "stakeholders.")
bullet("Regulated industry: medical devices and pharmaceuticals experience (GMP, FDA, "
       "EMA at Novo Nordisk); documentation discipline and verification culture from "
       "requirements to release.")
bullet("Languages: English (fluent) and Danish (native).")
bullet("Conditions: based in Måløv (easy commute to Humlebæk); driving licence B; "
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
jd_words = ["product development", "project manager", "workstream", "scope",
  "deliverables", "milestones", "dependencies", "decision points", "multidisciplinary",
  "development team", "risks", "issues", "design verification", "design transfer",
  "launch readiness", "concept", "detailed development", "verification", "manufacturing",
  "transfer", "design control", "documentation", "requirements", "specifications",
  "product concepts", "designs", "design for manufacturing", "manufacturing readiness",
  "trade-offs", "quality", "manufacturability", "sustainability", "time", "cost",
  "mandate", "escalation", "resource", "opex", "capacity", "stakeholder", "communication",
  "engineering", "bachelor", "degree", "medical devices", "pharmaceuticals", "regulated",
  "r&d", "development", "planning", "risk management", "program", "project plan",
  "verification evidence", "launch"]
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
