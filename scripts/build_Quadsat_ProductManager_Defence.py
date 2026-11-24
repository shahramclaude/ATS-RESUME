#!/usr/bin/env python3
"""Build Shahram_Ajloo_Quadsat_ProductManager_Defence.docx (letter + CV in one document).
Product Manager, defence portfolio, Quadsat (R&D), Odense. Recruitment partner: ESBEES /
Soeren Boege Soerensoen. English document.
23.11.2026 user confirmations: eligible for security clearance by the Danish Defense
Intelligence Service = JA (written into the letter); workplace Odense = JA (written in).
Defence industry experience NOT claimed (JD accepts "or another mission-critical technical
domain" — claimed via Biofos critical infrastructure + Novo pharma). Career: Data Power first."""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_Quadsat_ProductManager_Defence.docx"

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
para("Application for Product Manager, Defence Portfolio, Quadsat", style="LetterTitle")
para("Dear Søren Bøge Sørensen", after=4)

para("In the field, everything comes down to one question: where is the RF emitter, and "
     "can the operator trust the answer? Quadsat's defence portfolio combines RF sensing "
     "payloads, drone-based operations, mission control software, signal processing and "
     "geolocation algorithms to deliver exactly that, and since the Series A extension in "
     "July 2025 the defence market has been the company's direction of travel. The "
     "Product Manager who owns this portfolio must move between strategy and detail "
     "every day, and that is the role I am applying for. I am a Maskinmester with a "
     "B.Tech degree in engineering and experience in technical project and product "
     "management, driving development from early concepts through validation and release "
     "to continued improvement in mission-critical domains.")

para("Translating customer, operational and commercial input into development priorities "
     "is the work I know best: at Data Power I take customer solutions from requirements "
     "specification to released product with engineers and end users in the same room, "
     "and my experience covers product development, technical customer dialogue and "
     "roadmaps where scope, timelines, dependencies, risks and progress stay visible to "
     "everyone. I work comfortably with multidisciplinary engineering teams across "
     "software, electrical and mechanical disciplines, and I collaborate closely with "
     "technical leads on feasibility, effort and realistic timelines before anything is "
     "promised. Prioritisation and resource planning across parallel workstreams is "
     "familiar ground from portfolio responsibility for 37 concurrent projects.")

para("My experience is from mission-critical technical domains rather than the defence "
     "industry itself: critical supply infrastructure that could never stand still at "
     "Biofos, and pharmaceutical production with zero critical deviations at Novo "
     "Nordisk, where I led 25 specialists through commissioning and release. The defence "
     "sector demands precision, documentation and trust, and I know those standards from "
     "these operations; I also follow the domain closely, from multi-domain operations "
     "and electronic warfare to the growing need to detect, analyse and locate emitters. "
     "Commercially I bring full P&L responsibility, tender calculation and close "
     "collaboration between technical teams and customers, and as an active Claude and "
     "Python user I use AI to structure roadmaps, analyse input and keep decisions "
     "documented.")

para("The first 30 days I would spend with the team, the products and the users: the "
     "payloads, the software, the algorithms and the operational stories behind them, "
     "together with engineering, commercial teams and partners. By day 60 I would own "
     "the product roadmap rhythm with the R&D Director, with clear priorities and a "
     "status overview the whole organisation can act on. By day 90 the first development "
     "priorities translated from customer insight would be in implementation, with "
     "validation and release plans in place.")

para("I can confirm that I am eligible to be security cleared by the Danish Defense "
     "Intelligence Service, and I am ready to work from Quadsat's base in Odense. I "
     "would welcome a conversation about shaping and driving the defence portfolio, and "
     "I can be reached at +45 93 99 95 14.")

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
para("Engineering background as an authorised Maskinmester (B.Tech) with practical "
     "experience in technical product and project management: translating customer and "
     "market needs into development priorities, roadmaps and released products in "
     "mission-critical domains. Strong technical understanding from multidisciplinary "
     "engineering teams, with full P&L responsibility and structured work on scope, "
     "timelines, dependencies and risks.")

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
bullet("Product management: technical product and project management; product direction, "
       "priorities, positioning and roadmap; end-to-end ownership from concept to release "
       "and continued improvement.")
bullet("Customer insight: translating customer, operational and commercial input into "
       "development priorities; technical customer dialogue and market understanding.")
bullet("Execution: scope, timelines, dependencies, risks and progress kept visible; "
       "development from concept through implementation, validation and release; PRINCE2.")
bullet("Collaboration: multidisciplinary engineering teams (software, RF, electrical, "
       "mechanical); technical leads on feasibility and effort; stakeholders across R&D, "
       "commercial and quality.")
bullet("Mission-critical domains: critical supply infrastructure (24/7) and "
       "pharmaceutical production (GMP); precision, documentation and security awareness.")
bullet("Prioritisation: resource planning and allocation of engineering capacity across "
       "parallel workstreams; portfolio responsibility (37 concurrent projects).")
bullet("Commercial: full P&L responsibility, tender calculation and partner and customer "
       "collaboration.")
bullet("Digital: AI tools (Python, Claude Code), Power BI, SAP ERP, Excel/Power Query; "
       "structured roadmaps and documentation.")
bullet("Languages: English (fluent, written and oral) and Danish (native).")
bullet("Conditions: eligible for security clearance by the Danish Defense Intelligence "
       "Service; work from Quadsat's base in Odense; driving licence B; available after "
       "notice.")

# ----------------------------- QUALITY CHECK -----------------------------
full = "\n".join(p.text for p in doc.paragraphs)
banned = ["spearheaded", "leveraged", "passionate", "dynamic", "results-driven",
          "proven track record", "synergy", "cutting-edge", "innovative solutions",
          "seamlessly", "robust", "demonstrated ability", "fast-paced",
          "drevet", "lidenskabelig", "dynamisk", "synergi", "banebrydende",
          "sømløst", "ikke kun", "men også", "\u2014", "passion",
          "not only", "but also", "passionate", "innovative"]
hits = [w for w in banned if w.lower() in full.lower()]
jd_words = ["product manager", "product management", "roadmap", "defence", "rf",
  "geolocation", "drone", "mission control", "signal processing", "payloads", "portfolio",
  "strategy", "priorities", "positioning", "development", "concept", "implementation",
  "validation", "release", "improvement", "customer", "operational", "commercial",
  "market", "engineering", "technical leads", "feasibility", "timelines", "dependencies",
  "risks", "progress", "prioritisation", "resource planning", "allocation",
  "engineering capacity", "collaboration", "r&d", "production", "quality",
  "stakeholders", "mission-critical", "defence industry", "bachelor", "degree",
  "english", "security cleared", "defense intelligence service", "emitters", "sensing"]
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
