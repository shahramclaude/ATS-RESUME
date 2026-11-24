#!/usr/bin/env python3
"""Build Shahram_Ajloo_Ocado_LeadEngineeringOpsManager.docx (letter + CV in one document).
Lead Engineering Operations Manager, automated Customer Fulfilment Centre near Copenhagen,
Ocado Group (partner: nemlig — publicly confirmed Aug 2026; named once in the letter).
23.11.2026: no user confirmations needed — all requirements covered by master-CV
(B.Tech = a real bachelor's degree, so the "bachelor desirable" requirement is met honestly).
English document. Career: Data Power (CTO + authorised Maskinmester) first."""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_Ocado_LeadEngineeringOpsManager.docx"

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
para("Application for Lead Engineering Operations Manager, Denmark", style="LetterTitle")
para("Dear Ocado Recruitment Team", after=4)

para("Ocado's mission is to redefine grocery shopping around the world through advanced "
     "e-commerce solutions, giving customers convenience, quality and reliability. In "
     "Denmark that mission is about to become physical: a new automated Customer "
     "Fulfilment Centre near Copenhagen, built with nemlig and "
     "expected to go live in 2028, where the robotics, infrastructure and software of "
     "the Ocado Smart Platform meet real operations. The engineering operation behind it "
     "must be built and led from the first bolt to live trading, and that is the "
     "challenge I am applying for. I am an authorised Maskinmester with a background "
     "across pharmaceutical manufacturing, marine engineering and equipment production, "
     "and I have led shift-based maintenance and technical teams through commissioning, "
     "handover and live operation.")

para("Leading a team of around 30 through a build phase and into live operation is "
     "familiar ground: at Novo Nordisk I led cross-functional teams of 25 specialists "
     "through testing, commissioning and handover of plant under GMP/FDA/EMA with zero "
     "critical deviations, and at Ventek-Air I managed daily operations with a 14-person "
     "team across 11 concurrent projects. A structure with two Engineering Team Managers "
     "and shift-based technicians is one I know how to support: I coach and motivate "
     "through regular 1:1s, situational leadership and visible presence on the floor, "
     "and I build teams, culture and values from the start, as I did when I scaled a workshop "
     "organisation and standardised its ways of working.")

para("Driving performance through KPIs and operational excellence is how I run an "
     "operation: PDCA programmes, A3 and Lean, KPI dashboards and structured management "
     "reporting, with results like a 40 per cent reduction in energy costs at Novo "
     "Nordisk and productivity improvements of over 40 per cent in my own company. "
     "Commercial awareness comes from carrying full P&L responsibility, tender "
     "calculation and customer relationships, and I am used to building trusted "
     "relationships with senior stakeholders and delivery partners on both sides of the table. Technically I "
     "combine electrical authorisation (LV/MV/HV) with a mechanical grounding as an "
     "electro-mechanic, and my Maskinmester education comes from the marine engineering "
     "tradition the role refers to.")

para("The first 30 days I would spend on site with the build: the team, the suppliers, "
     "the technology and the safety structure, and getting to know the European colleagues "
     "and the engineering network behind the site. By day 60 I would own the maintenance "
     "rhythm, the KPIs and the escalation routines together with the two team managers, "
     "and by day 90 concrete proposals for how the operation performs from the first day "
     "of live trading would be ready.")

para("I am based in Måløv, close to Copenhagen, and I can be on site every day as the "
     "role requires. I would welcome a conversation about building the engineering team "
     "and the operation from the ground up. I can be reached at +45 93 99 95 14.")

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
para("Engineering manager with a mechanical and electrical foundation: authorised "
     "Maskinmester (B.Tech) with proven leadership of shift-based maintenance and "
     "technical teams in pharmaceutical manufacturing, marine and industrial operations. "
     "Combines people leadership and KPI-driven performance with commissioning and "
     "handover experience, operational excellence (PDCA, A3, Lean) and commercial "
     "awareness from full P&L responsibility.")

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
bullet("Leadership: proven leadership of shift-based maintenance and technical teams "
       "(8-25 people); coaching, motivation and management of technical teams; 1:1s and "
       "performance reviews (Situational Leadership, GROW).")
bullet("Engineering background: pharmaceutical manufacturing (Novo Nordisk), marine "
       "engineering (STCW certificates, Maskinmester education) and equipment "
       "manufacturing; production management.")
bullet("Performance: KPIs and operational excellence; PDCA, A3, Lean and Standard Work; "
       "KPI dashboards and structured management reporting.")
bullet("Commercial: full P&L responsibility, tender calculation and customer "
       "relationships; trusted relationships with senior stakeholders.")
bullet("Build to live: team building through the build phase and into live operation; "
       "testing (FAT/SAT), commissioning and formal handover.")
bullet("Technology: electrical and mechanical systems, automation and control, SCADA; "
       "CMMS, SAP ERP, Power BI, Python and Claude Code.")
bullet("Languages: Danish (native) and English (fluent); strong understanding of Danish "
       "business culture.")
bullet("Conditions: based in Måløv near Copenhagen; on site daily; driving licence B; "
       "international travel when required.")

# ----------------------------- QUALITY CHECK -----------------------------
full = "\n".join(p.text for p in doc.paragraphs)
banned = ["spearheaded", "leveraged", "passionate", "dynamic", "results-driven",
          "proven track record", "synergy", "cutting-edge", "innovative solutions",
          "seamlessly", "robust", "demonstrated ability", "fast-paced",
          "drevet", "lidenskabelig", "dynamisk", "synergi", "banebrydende",
          "sømløst", "ikke kun", "men også", "\u2014", "passion",
          "not only", "but also", "passionate", "innovative"]
hits = [w for w in banned if w.lower() in full.lower()]
jd_words = ["fulfilment centre", "engineering", "automated", "ocado", "e-commerce",
  "grocery", "reliability", "robotics", "software", "infrastructure", "maintenance",
  "technicians", "shift", "team managers", "leadership", "build phase", "live operation",
  "technology", "performance", "partner", "european", "bachelor", "danish", "english",
  "business culture", "copenhagen", "technical teams", "coach", "motivate", "manage",
  "pharmaceutical", "manufacturing", "production management", "marine engineering",
  "equipment manufacturing", "kpi", "operational excellence", "commercial",
  "stakeholders", "relationships", "quality", "culture", "values", "specialists",
  "colleagues", "nemlig"]
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
