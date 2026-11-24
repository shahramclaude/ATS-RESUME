#!/usr/bin/env python3
"""Build Shahram_Ajloo_Splunk_PresalesManager_NorwayDenmark.docx (letter + CV).
Presales Manager, Splunk Norway & Denmark (Splunk is part of Cisco; reports to EMEA
North Presales AVP; no named contact, no deadline). English document.
23.11.2026 user confirmations (unpinned): presales leadership (POC, RFI/RFP, demos,
technical win) = concrete; software sales = technical sales only (NO software claim);
verticals finance/insurance/telco/retail = concrete experience; build anyway on the
AI + CTO + leadership profile. Career: Data Power first."""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_Splunk_PresalesManager_NorwayDenmark.docx"

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
para("Application for Presales Manager, Splunk Norway & Denmark", style="LetterTitle")
para("Dear Splunk Recruitment Team", after=4)

para("A technical win is decided in the room where the customer's hardest question meets "
     "an answer they can trust: strategy and vision presented with business value, backed "
     "by technology that holds up under scrutiny. Leading presales in Norway and Denmark "
     "means building the team that wins those rooms and stepping into them yourself. I am "
     "a Maskinmester with a B.Tech degree in engineering and currently CTO of an AI "
     "department, and I come from the two sides this role bridges: hands-on technical "
     "depth in AI and automation, and leading and developing teams that deliver "
     "customer-facing technical value.")

para("Leading and developing presales work is concrete experience for me: POC planning "
     "and execution, RFI/RFP responses, product demos and solution presentations, and the "
     "technical win in competitive situations, with hiring, coaching and development of "
     "the engineers doing it. I have built an organisation from 4 to 10 people with "
     "defined development plans and shared standards, led 25 specialists through complex "
     "enterprise projects at Novo Nordisk, and mentored technical teams through hands-on "
     "reviews and structured 1:1s. The partnership with sales management and Channel is familiar "
     "territory: account strategies, joint customer meetings and removing technical "
     "obstacles before they slow the deal.")

para("My sales background is technical sales of solutions and services: tenders and bids, "
     "prospecting, customer meetings where the value case decides, and full commercial "
     "responsibility as a company owner. The domain you need is my daily work: AI, from "
     "LLM APIs and AI agents to the data foundations that make them useful, presented to "
     "business and technical audiences alike. I know enterprise customers and their "
     "buying processes from sales and delivery in one or more of the financial services, "
     "insurance, telecommunications and retail sectors, and I develop value and ROI cases "
     "from real numbers: a 40 % reduction in energy costs at Novo Nordisk is one case I "
     "can walk through end to end.")

para("The first 30 days I would spend with the presales teams in Norway and Denmark and "
     "the pipeline: the key accounts, the technical win plans and the material we present. "
     "By day 60 I would own resource prioritization across the Nordics with the other SE "
     "Managers, development plans for each engineer and the RFI/RFP process, and by day 90 "
     "customer-facing initiatives, events and business cases would be running with "
     "measurable business outcomes. I am self-motivated and organised, comfortable on stage at conferences and trade shows, and "
     "I write presentations that carry strategy as well as architecture.")

para("I am based in Måløv, I work in fluent English and native Danish, the language "
     "combination you require, and I can start after notice. I would welcome a "
     "conversation about leading Presales for Splunk in Norway and Denmark, and I can be "
     "reached at +45 93 99 95 14.")

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
para("Maskinmester (B.Tech) and CTO of an AI department with concrete presales leadership "
     "experience: POCs, RFI/RFP responses, demos and solution presentations led and "
     "coached toward the technical win, with engineers hired, mentored and developed. "
     "Bridges commercial and technical sales with deep AI domain knowledge (LLM APIs, AI "
     "agents) and enterprise experience across financial services, insurance, "
     "telecommunications and retail, grounded in ROI cases built from real numbers.")

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
bullet("Presales leadership: Pre-sales teams and SE work led and developed (POC planning and "
       "execution, RFI/RFP responses, demos and solution presentations); hiring, coaching "
       "and development plans; the technical win kept in focus.")
bullet("Technical leadership and vision: strategy and value-based presentations, business "
       "and technical, delivered in customer meetings and on stage at field events; "
       "presales material developed (business cases/ROI, competitive insight).")
bullet("Business knowledge: domain knowledge in AI (LLM APIs, AI agents, data "
       "foundations); business intelligence (Power BI) and operational intelligence from "
       "SCADA and control systems; enterprise customers in financial services, insurance, "
       "telecommunications or retail.")
bullet("Sales partnership: account strategies with sales management and follow-up "
       "opportunities identified; technical sales of "
       "solutions and services (tenders, bids, prospecting); sales process knowledge "
       "including the technical win; obstacles removed with creative, adaptive approaches "
       "and resilience.")
bullet("Team development: high-performing teams built and developed (4-10 AI specialists "
       "today; up to 25); mentoring, coaching and performance plans; resource "
       "planning and prioritisation of resources across regions and stakeholders.")
bullet("Business value: analytical ROI and value cases developed from measured results "
       "(40 % energy "
       "cost reduction; over 40 % productivity improvement); client business goals, "
       "buying processes and industry trends understood.")
bullet("Technical: Python, Claude Code, LLM APIs, AI agents; Power BI, SAP ERP, MS "
       "Office; AI-assisted software development with shared standards.")
bullet("Languages: English (fluent) and Danish (native); the language combination "
       "required.")
bullet("Conditions: based in Måløv (travel across Denmark and Norway as required); "
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
jd_words = ["presales", "pre-sales", "sales", "technical win", "poc", "rfi", "rfp",
  "demos", "presentations", "strategy", "vision", "business value", "roi", "account",
  "customers", "enterprise", "ai", "business intelligence", "operational intelligence",
  "financial services", "insurance", "telecommunications", "retail", "teams", "hiring",
  "coaching", "mentoring", "development", "performance", "leadership", "manager", "cto",
  "bachelor", "degree", "communication", "english", "danish", "competitive", "events",
  "channel", "prioritization", "resources", "opportunities", "business outcomes",
  "analytical", "self-motivated", "resilience", "high-performing"]
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
