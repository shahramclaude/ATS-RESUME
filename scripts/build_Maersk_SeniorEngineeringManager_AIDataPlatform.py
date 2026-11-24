#!/usr/bin/env python3
"""Build Shahram_Ajloo_Maersk_SeniorEngineeringManager_AIDataPlatform.docx (letter + CV).
Senior Engineering Manager, AI & Data Platform, A.P. Moller - Maersk, Copenhagen
(Esplanaden 50; Workday R194570). English document.
23.11.2026 user confirmations (unpinned, no specific technologies invented):
- concrete data platforms/pipelines experience = YES (claimed as categories)
- cloud/DevOps = LIGHT familiarity only (mirrored honestly as familiarity, not expertise)
AI/agentic AI strength: LLM APIs, AI agents, Python/Claude (CTO of AI department).
Career: Data Power first."""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_Maersk_SeniorEngineeringManager_AIDataPlatform.docx"

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
para("Application for Senior Engineering Manager, AI & Data Platform, Maersk",
     style="LetterTitle")
para("Dear Maersk Recruitment Team", after=4)

para("Agentic AI is only as good as the data foundation underneath it: pipelines that "
     "hold, governed data layers that teams can query, and platforms that stay reliable "
     "at global scale. That is the combination Maersk is building for intelligent supply "
     "chain solutions, and the Senior Engineering Manager who can lead engineers across "
     "data, platform and AI while owning delivery and quality is the leader I want to be "
     "in that journey. I am a Maskinmester with a B.Tech degree in engineering and more "
     "than twelve years of technology leadership, and I lead the AI department at Data "
     "Power today, where LLM APIs, AI agents and data-driven applications go from "
     "requirements to running systems.")

para("Leading high-performing engineering teams across data, platform and AI domains is "
     "my daily work: I manage 4-10 engineers and AI specialists with delivery outcomes, "
     "quality standards and engineering practices as my responsibility, and before that I "
     "led 25 specialists through complex enterprise projects at Novo Nordisk. Agile "
     "execution, prioritization and alignment with product and business stakeholders come "
     "from portfolio work on 37 concurrent projects and from carrying full P&L "
     "responsibility as a company owner. I stay close to the code and the architecture: "
     "as an active Claude and Python user I review, structure and build alongside my "
     "teams, and I know what it takes to move a solution from concept through validation "
     "to reliable operation.")

para("Data platforms and pipelines are concrete experience for me: I have built data "
     "structures, integration flows and analytics layers that power KPI dashboards and "
     "decisioning, with governed, queryable data and self-service reporting as the goal. "
     "On cloud platforms and DevOps practices I have working familiarity from deploying "
     "AI solutions, and I complement that with deep AI platform understanding: what AI "
     "and machine learning use cases need from data, and how agentic workflows consume it. Cost and "
     "efficiency thinking runs through my delivery: reusable components over duplication, "
     "and pragmatic trade-offs between cost, speed and quality in every decision.")

para("The first 30 days I would spend with the teams and the platform: the architecture, "
     "the pipelines in flight, the enterprise use cases and the stakeholders across "
     "Product, SAP and Infrastructure. By day 60 I would own the delivery rhythm, "
     "engineering practices and observability within my teams, and by day 90 concrete "
     "proposals for reusable components, cost optimization and agentic AI enablement "
     "would be aligned with the enterprise strategy.")

para("I am based in Måløv with easy access to Esplanaden, and I can start after notice. "
     "I would welcome a conversation about leading the AI and Data Platform teams, and I "
     "can be reached at +45 93 99 95 14.")

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
para("Maskinmester (B.Tech, science/engineering discipline) with more than twelve years "
     "of technology leadership across "
     "data, platform and AI domains: currently CTO of an AI department delivering LLM "
     "APIs, AI agents and data-driven applications. Combines engineering leadership and "
     "delivery ownership with concrete data platform and pipeline experience, AI/ML "
     "platform understanding and working familiarity with cloud and DevOps practices.")

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
bullet("AI and Data Platform delivery: data platforms, data products and AI-enabled "
       "applications delivered; agentic AI enablement (LLM APIs, AI agents); integrated "
       "data foundations for end-to-end visibility.")
bullet("Data and analytics: data platforms and pipelines (integration flows, governed "
       "data layers); democratized data access, self-service reporting and dashboards "
       "(Power BI, KPI platforms); reliable and secure data foundations for analytics and "
       "AI.")
bullet("Platform and architecture: alignment with enterprise architecture; reusable "
       "platform components and engineering standards; SAP and non-SAP integration "
       "context.")
bullet("Engineering leadership: high-performing teams across data engineering, platform and AI "
       "(4-10 engineers today; up to 25); delivery outcomes, quality standards and "
       "engineering practices; Agile execution and prioritization.")
bullet("Operational excellence: scalability, reliability and performance at scale; "
       "observability, automation and DevOps practices (working familiarity); governance "
       "for performance, availability and cost optimization.")
bullet("Cost and efficiency: cost optimization mindset; reusable services over "
       "duplication; trade-offs between cost, speed and quality; full P&L experience.")
bullet("Collaboration: cross-functional delivery with Product, SAP, Infrastructure and "
       "Data teams; stakeholder management; influence across competing priorities.")
bullet("Technical: Python, Claude Code, LLM APIs, AI agents; Power BI, SAP ERP, "
       "Excel/Power Query; cloud deployment familiarity.")
bullet("Languages: English (fluent) and Danish (native).")
bullet("Conditions: based in Måløv near Copenhagen (Esplanaden); driving licence B; "
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
jd_words = ["senior engineering manager", "engineering manager", "ai", "data platform",
  "data platforms", "pipelines", "analytics", "agentic ai", "ai/ml", "machine learning",
  "llm", "agents", "cloud", "devops", "data engineering", "self-service", "dashboards",
  "reporting", "governed", "architecture", "enterprise", "sap", "scalability",
  "reliability", "performance", "observability", "automation", "governance", "cost",
  "optimization", "teams", "leadership", "agile", "prioritization", "stakeholders",
  "product", "infrastructure", "cross-functional", "delivery", "outcomes", "quality",
  "standards", "practices", "bs", "degree", "science", "engineering"]
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
