#!/usr/bin/env python3
"""Build Shahram_Ajloo_EuropeanEnergy_HeadOfProjectManagement_PtX.docx (letter + CV in one).
Head of Project Management and Organisational Development, Power-to-X, European Energy,
HQ Soeborg (Workday JR100384; contact Mads Nygaard; EVP Rene Alcaraz Frederiksen). English.
23.11.2026: zero gaps — PMO experience framed via portfolio governance (Novo, 37 CAPEX),
consultant experience via Data Power Consultant ApS. No photograph in CV (JD request).
Career: Data Power first."""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_EuropeanEnergy_HeadOfProjectManagement_PtX.docx"

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
para("Application for Head of Project Management and Organisational Development, "
     "Power-to-X", style="LetterTitle")
para("Dear Mads Nygaard", after=4)

para("At Kassø, the world's first large-scale commercial e-methanol plant is producing "
     "42,000 tonnes a year from biogenic CO2 and solar-powered hydrogen, and next to it "
     "in Esbjerg sits European Energy's first green hydrogen facility. As the two plants "
     "move from pioneering construction into consolidated operation and a wider "
     "portfolio, the PMO behind them must become best-in-class: frameworks, stage gates, "
     "governance and reporting that hold as the business grows across PtX, Biogas and "
     "Ammongas. Building that PMO and developing the organisation around it is the role "
     "I am applying for. I am a Maskinmester with a B.Tech degree in engineering and "
     "portfolio and project governance from capital-intensive environments, and I have "
     "built frameworks, standards and reporting that teams use in their daily work.")

para("Project management frameworks are familiar ground: at Novo Nordisk I held "
     "portfolio responsibility for 37 concurrent CAPEX projects with transparency on "
     "priorities, progress, budget and risks across engineering, procurement and "
     "construction, with stage-gated qualification (FAT/SAT, IQ/OQ) and monthly "
     "management reporting, and I developed the templates, decision principles and "
     "procedures behind them. Budget governance across screening, development and CAPEX "
     "phases is work I know from both the project side and the owner side: as a company "
     "owner I have carried full P&L responsibility, approval flows and change control, "
     "and I prepare material for steering and investment forums with calculation models "
     "for investments and scenarios.")

para("Organisational development in project management is how I have raised delivery "
     "capability: standardised working methods, lessons learned turned into usable tools "
     "and checklists, and facilitated workshops with teams on flow and quality. Digital "
     "initiatives are close to my hands: as an active Claude and Python user I lead "
     "digitalisation projects that lighten administration and reporting, from "
     "AI-assisted tender calculation to KPI dashboards. I lead, develop and motivate "
     "through clear direction, 1:1s and psychological safety, and the strategic and "
     "commercial understanding comes from translating ambitions into roadmaps and "
     "operating models in my own business. European Energy's values of trust, courage, "
     "ambition and agility describe the way I work.")

para("The first 30 days I would spend on the projects and the people: the two PtX "
     "facilities, the current PMO practices, and the leadership team's priorities across "
     "the business unit. By day 60 I would have an assessment of the Project Management "
     "Framework and a plan for adapting it to the business, with governance for budget "
     "planning, approvals and change control in place. By day 90 the first "
     "organisational development initiatives would be running: workshop formats, "
     "lessons-learned routines and management reporting that give the leadership team "
     "transparency on priorities, progress, risks and opportunities.")

para("I am based in Måløv with easy access to Søborg, and I can start after notice. I "
     "would welcome a conversation about building the PMO and shaping the organisation "
     "behind the next PtX plants. I can be reached at +45 93 99 95 14.")

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
para("Engineering degree (Maskinmester, B.Tech) with experience in portfolio and project "
     "governance, PMO frameworks and organisational development from capital-intensive "
     "environments in energy, infrastructure and industry. Combines structured planning and management "
     "reporting with digitalisation leadership (AI, Python), facilitated workshops and "
     "team leadership, plus management consultant experience from Data Power Consultant "
     "ApS.")

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
bullet("PMO and framework: project management frameworks across the full project "
       "lifecycle; stage-gate governance, decision principles, templates, procedures and "
       "management reporting; document control; portfolio governance (37 concurrent CAPEX "
       "projects).")
bullet("Budget governance: planning, approvals, follow-up and change control across "
       "screening, development and CAPEX phases; full P&L experience; interfaces to "
       "Finance and Procurement.")
bullet("Strategy and execution: ambitions translated into roadmaps, operating models and "
       "clear responsibilities; complex topics structured into concrete tasks; interface for digital initiatives.")
bullet("Organisational development: process improvement and business transformation; "
       "facilitation, communication and stakeholder management; workshops, knowledge "
       "sharing and lessons learned into standards, "
       "tools and practical guidance.")
bullet("Team leadership: leading, developing and motivating teams (8-25 people); 1:1s and "
       "performance reviews (Situational Leadership, GROW).")
bullet("Leadership material: material for steering committees and investment forums; decision "
       "papers, KPI reporting and calculation models for investments (DCF and scenarios).")
bullet("Digital: digitalisation projects led; AI tools (Python, Claude Code), Power BI, "
       "SAP ERP, Excel/Power Query.")
bullet("Languages: English (fluent, clear and concise) and Danish (native).")
bullet("Conditions: based in Måløv near Søborg; driving licence B; available after notice.")

# ----------------------------- QUALITY CHECK -----------------------------
full = "\n".join(p.text for p in doc.paragraphs)
banned = ["spearheaded", "leveraged", "passionate", "dynamic", "results-driven",
          "proven track record", "synergy", "cutting-edge", "innovative solutions",
          "seamlessly", "robust", "demonstrated ability", "fast-paced",
          "drevet", "lidenskabelig", "dynamisk", "synergi", "banebrydende",
          "sømløst", "ikke kun", "men også", "\u2014", "passion",
          "not only", "but also", "passionate", "innovative"]
hits = [w for w in banned if w.lower() in full.lower()]
jd_words = ["project management", "organisational development", "pmo", "framework",
  "stage-gate", "governance", "decision principles", "templates", "procedures",
  "management reporting", "document control", "portfolio", "priorities", "progress",
  "risks", "opportunities", "budget planning", "approvals", "change control", "strategy",
  "roadmaps", "operating models", "digital initiatives", "workshops", "knowledge sharing",
  "lessons learned", "standards", "tools", "steering committees", "investment forums",
  "planning", "strategic", "commercial", "complex", "facilitation", "communication",
  "stakeholder management", "digitalisation", "process improvement",
  "business transformation", "capital-intensive", "energy", "infrastructure", "industry",
  "management consultant", "engineering", "english", "power-to-x", "ptx", "biogas",
  "ammongas", "søborg"]
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
