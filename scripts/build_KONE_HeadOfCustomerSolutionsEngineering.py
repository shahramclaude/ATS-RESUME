#!/usr/bin/env python3
"""Build Shahram_Ajloo_KONE_HeadOfCustomerSolutionsEngineering.docx (letter + CV).
Head of Customer Solutions Engineering, KONE Nordics (Workday R0666806; 4 Nordic
locations; deadline 13.12.2026, may be filled earlier). English document.
Salutation: hiring manager Sonja Lipsanen (contact for questions: Moa Lardner).
23.11.2026 user confirmation (unpinned): new construction AND modernization businesses =
concrete experience with both. LEAN = in practice, not certified (mirror honestly).
Career: Data Power first."""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_KONE_HeadOfCustomerSolutionsEngineering.docx"

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
para("Application for Head of Customer Solutions Engineering, KONE Nordics",
     style="LetterTitle")
para("Dear Sonja Lipsanen", after=4)

para("Two billion journeys every day depend on equipment that was either built right the "
     "first time or modernised right the second, and that reality sits at the heart of "
     "KONE's new construction and modernization business. Leading Customer Solutions "
     "Engineering means giving the engineers who own those solutions the competencies, "
     "structure and technical standards to deliver competitive, compliant answers to every "
     "customer. I am a Maskinmester with a B.Tech degree in engineering and more than "
     "fifteen years of technical leadership, from utility plants and production sites to "
     "an engineering department I built and developed, and my work has been to turn "
     "engineering capability into measurable delivery.")

para("Building and developing engineering organisations is concrete experience for me: I "
     "grew an AI and software department from 4 to 10 people with competence development "
     "and shared standards, led 25 specialists through complex projects at Novo Nordisk, "
     "and ran my own company with full P&L responsibility, costing and profitability in "
     "every tender. Operational performance follows the same pattern: key performance "
     "indicators monitored, LEAN methodologies in practice (5S, Standard Work, PDCA) and "
     "a 40 % reduction in energy costs as one measurable result. I lead change by bringing "
     "people along: standardised ways of working that improved delivery capability, and "
     "matrix leadership across two parallel organisations under one shared plan.")

para("Technical excellence with compliance runs through my career: electrical systems, "
     "switchboards, control systems, ventilation and cooling delivered under safety "
     "requirements, regulations and industry standards, with documentation and handover "
     "as part of the solution lifecycle. Supporting sales and delivery with competitive, "
     "cost-effective solutions is what tenders and bids taught me, and I understand both "
     "sides of the business you are in: commissioning of new plants and modernization of "
     "existing installations. Translating customer needs into engineering solutions and "
     "working cross-functionally in matrix organisations with global stakeholders is my "
     "normal, not my exception.")

para("The first 30 days I would spend with the Customer Solutions Engineering teams "
     "across the Nordics: the competency map, current ways of working, KPIs and the flow "
     "from sales to delivery. By day 60 I would own the operational rhythm and the "
     "development plans for people and processes, and by day 90 concrete transformation "
     "initiatives, improved First Time Right performance and stronger knowledge sharing "
     "would be running with measurable targets.")

para("I am based in Måløv and ready for the travel the role requires, and I can start "
     "after notice. I would welcome a conversation with you and the recruitment team "
     "about leading Customer Solutions Engineering at KONE, and I can be reached at "
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
para("Maskinmester (B.Tech) with more than fifteen years of technical and organisational "
     "leadership in engineering environments: builds and develops engineering teams (4-10 "
     "specialists today; up to 25), sets technical standards and drives operational "
     "performance with LEAN methods in practice. Business-minded with full P&L experience "
     "(costing, profitability, commercial awareness) and a track record of change "
     "initiatives, matrix collaboration and compliance-led technical delivery.")

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
bullet("Organisation leadership: engineering organisations built and developed "
       "(4-10 specialists today; up to 25); competencies, capabilities and resources "
       "planned; resource planning and allocation for business priorities; competence "
       "development, knowledge sharing and succession planning.")
bullet("Operational performance: key performance indicators monitored; continuous "
       "improvement, efficiency and productivity; LEAN methodologies in practice (5S, "
       "Standard Work, PDCA); engineering output and First Time Right discipline (zero "
       "critical deviations at handover).")
bullet("Strategy and transformation: strategic development and transformation "
       "initiatives; improved processes and ways of working; "
       "organizational development and change led from plan to daily practice.")
bullet("Technical excellence and compliance: engineering policies, safety requirements, "
       "local regulations and industry standards across the solution lifecycle "
       "(electrical, switchboards, control systems, ventilation and cooling).")
bullet("Sales and delivery support: competitive, cost-effective and customer-focused "
       "technical solutions; tenders, costing and profitability; early customer "
       "engagement and needs translated into engineering solutions.")
bullet("Stakeholders and matrix: communication and collaboration with sales, delivery "
       "and regional/global "
       "functions; resources managed in matrix organisations; strong cross-functional "
       "networks.")
bullet("Business understanding: commercial awareness, costing and profitability; full "
       "P&L responsibility; technical excellence balanced with commercial priorities.")
bullet("New construction and modernization: concrete experience with both, commissioning "
       "of new plants and modernization of existing installations; maintenance across "
       "the full life cycle of technical installations.")
bullet("Languages: English (fluent) and Danish (native).")
bullet("Conditions: based in Måløv (travel across the Nordics as required); driving "
       "licence B; available after notice.")

# ----------------------------- QUALITY CHECK -----------------------------
full = "\n".join(p.text for p in doc.paragraphs)
banned = ["spearheaded", "leveraged", "passionate", "dynamic", "results-driven",
          "proven track record", "synergy", "cutting-edge", "innovative solutions",
          "seamlessly", "robust", "demonstrated ability", "fast-paced",
          "drevet", "lidenskabelig", "dynamisk", "synergi", "banebrydende",
          "sømløst", "ikke kun", "men også", "\u2014", "passion",
          "not only", "but also", "passionate", "innovative"]
hits = [w for w in banned if w.lower() in full.lower()]
jd_words = ["head of customer solutions engineering", "customer solutions", "engineering",
  "bachelor", "degree", "leadership", "teams", "people", "competencies", "capabilities",
  "resources", "operational performance", "key performance indicators", "continuous",
  "improvement", "efficiency", "productivity", "transformation", "lean", "first time right",
  "technical excellence", "compliance", "policies", "safety", "regulations", "standards",
  "solution", "sales", "delivery", "competitive", "cost-effective", "customer",
  "stakeholders", "competence development", "knowledge sharing", "succession",
  "resource planning", "change", "organizational", "matrix", "commercial", "costing",
  "profitability", "communication", "english", "travel", "new construction",
  "modernization", "maintenance", "lean"]
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
