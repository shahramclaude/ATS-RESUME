#!/usr/bin/env python3
"""Build Shahram_Ajloo_Valmet_ManagerMachineEngineering.docx (letter + CV, one document).
Manager, Machine Engineering, Valmet (R61489) — Karlstad / Copenhagen.
23.11.2026: Maskinmester = 4.5-year professional bachelor (B.Tech), presented honestly
(no M.Sc. claim); base = Karlstad or Copenhagen (both OK); international travel = yes;
no pulp experience (transferable industrial machinery). English document.
"""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_Valmet_ManagerMachineEngineering.docx"

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
para("Application for Manager, Machine Engineering (R61489)", style="LetterTitle")
para("Dear Tuomas Etula", after=4)

para("Valmet's promise to customers is that everything works together, and that is the "
     "job in one sentence: roughly 20 machine engineers in Karlstad and Copenhagen "
     "deliver the engineering behind pulp mills, biomass power plants and energy "
     "projects, and the solutions only come together when people, processes and "
     "resources are led as one system across the global resource pool. My foundation "
     "is mechanical and electrical engineering with leadership attached to it: from "
     "hands-on work on industrial machinery to leading teams of up to 25 specialists "
     "through commissioning and handover.")

para("Deliverables are familiar ground: specification, calculation and design, "
     "manufacturing and installation, through commissioning and formal handover. At "
     "Novo Nordisk I led 37 concurrent CAPEX projects (DKK 2 to 10 million each) with "
     "progress, budget and risk across engineering, procurement and construction, with "
     "FAT/SAT and IQ/OQ acceptance testing and zero critical deviations at handover. "
     "At Ventek-Air I ran 11 concurrent installation projects from specification to "
     "formal handover with a 14-person team, and in ELOHVAC and now at Data Power I "
     "carry full P&L responsibility for technical delivery, including quality "
     "documentation and collaboration with external engineering partners. My degree is "
     "the Danish Maskinmester qualification: a 4.5-year professional bachelor's degree "
     "in engineering (B.Tech) in technological leadership and mechanical engineering, "
     "built on a trade background as an electro-mechanic.")

para("On the people side I lead with structure and trust: situational leadership, "
     "regular 1:1s and psychological safety are working tools, and competence "
     "development happens through deliberate onboarding, coaching and knowledge "
     "sharing. I have led teams through change, from scaling a workshop organisation "
     "to standardising ways of working with PDCA, A3 and Lean, and I treat continuous "
     "improvement as part of daily operations instead of separate projects. Valmet's "
     "Leadership Principles describe how I already work: take accountability, lead "
     "with courage, build on trust and collaborate for growth. "
     "My background is international: with education and "
     "early career in Iran and my professional career in Denmark; English is my "
     "working language alongside Danish and Farsi, and I travel internationally when "
     "business needs require it.")

para("The first 30 days I would spend in Karlstad and Copenhagen with the team, the "
     "running projects and the Engineering Excellence processes. By day 60 I would "
     "own the rhythm of resource planning, deliverable reviews and individual "
     "development plans. By day 90 I would bring concrete proposals for a more "
     "unified and flexible global resource pool and ways of working, ready for the "
     "next projects in Europe, South America and Asia.")

para("I am based in Måløv with easy access to Copenhagen, and I am open to being based "
     "in Karlstad as well. I would welcome a conversation with you about leading the "
     "machine engineering team and contributing to the 'Lead the Way' journey. I can "
     "be reached at +45 93 99 95 14.")

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
para("Engineering manager with a mechanical and electrical foundation: Maskinmester "
     "(B.Tech) and electro-mechanic trade background, with leadership of engineering "
     "teams from 8 to 25 people across projects, workshops and commissioning. "
     "Combines people leadership, project execution and continuous improvement with "
     "hands-on knowledge of industrial machinery, process plants and energy systems.")

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
bullet("Machine engineering: industrial machinery, pumps and mechanical systems, ventilation and "
       "cooling, electrical systems and switchboards; electro-mechanic foundation.")
bullet("Engineering management: team management of engineering teams (8-25 people), resource planning, "
       "competence development, 1:1s and performance reviews (Situational Leadership, GROW).")
bullet("Project execution and engineering processes: PRINCE2, portfolio and CAPEX projects, progress, budget and risk, "
       "FAT/SAT and IQ/OQ, commissioning and formal handover; deliverables for sales, procurement, manufacturing and construction.")
bullet("Continuous improvement: PDCA, A3, Lean and Standard Work; problem-solving and change management (Kotter, "
       "Tuckman) and process development.")
bullet("Collaboration: internal stakeholders and external engineering partners, cross-functional "
       "teams, matrix management, decision papers and KPI reporting.")
bullet("Quality and safety: QA documentation, LOTO, risk assessment, work environment (APV) and "
       "near-miss routines.")
bullet("Digital: SAP ERP, CMMS, Power BI, Excel/Power Query, Python and Claude Code; AI in "
       "engineering and management.")
bullet("Languages: Danish (native), English (fluent, written and spoken), Farsi (native).")
bullet("Conditions: based near Copenhagen and open to Karlstad/Sweden; international travel when "
       "required; driving licence B.")

# ----------------------------- QUALITY CHECK -----------------------------
full = "\n".join(p.text for p in doc.paragraphs)
banned = ["spearheaded", "leveraged", "passionate", "dynamic", "results-driven",
          "proven track record", "synergy", "cutting-edge", "innovative solutions",
          "seamlessly", "robust", "demonstrated ability", "fast-paced",
          "drevet", "lidenskabelig", "dynamisk", "synergi", "banebrydende",
          "sømløst", "ikke kun", "men også", "\u2014", "passion",
          "not only", "but also", "passionate", "innovative"]
hits = [w for w in banned if w.lower() in full.lower()]
jd_words = ["machine engineering", "leadership", "project execution", "continuous improvement",
  "pulp mills", "biomass", "energy projects", "engineers", "competence", "deliverables",
  "sales", "procurement", "manufacturing", "construction", "commissioning", "quality",
  "cost", "resource", "team management", "change management", "problem", "decision",
  "English", "travel", "global", "stakeholders", "external engineering", "psychological safety",
  "accountability", "courage", "trust", "collaborate", "karlstad", "copenhagen",
  "engineering processes", "industrial", "KPI", "budget", "B.Tech", "maskinmester",
  "electrical", "switchboards", "FAT/SAT", "development plans", "flexible", "unified",
  "customer", "handover", "matrix", "Lean", "PDCA", "A3"]
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
