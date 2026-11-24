#!/usr/bin/env python3
"""Build Shahram_Ajloo_HitachiEnergy_DocumentationSpecialist.docx (letter + CV in one).
Documentation Specialist, Hitachi Energy Grid Integration (Nordic OU), Ballerup/Middelfart
(Workday R0140633; travel to Vaesteraas and Vaasa). English document.
23.11.2026: zero gaps — all requirements covered by master-CV (2+ years documentation
management via GMP/afleveringsdokumentation; Danish+English fluent; travel confirmed).
No "Why I am applying" block needed here (NNE-specific format). Career: Data Power first."""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_HitachiEnergy_DocumentationSpecialist.docx"

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
para("Application for Documentation Specialist, Hitachi Energy Grid Integration",
     style="LetterTitle")
para("Dear Hitachi Energy Recruitment Team", after=4)

para("Substations can be energised only when their documentation is complete: every "
     "requirement tracked, every document checked against it, every risk and opportunity "
     "visible. That discipline is what holds delivery together in Grid Integration's "
     "projects for distribution and transmission grids, serving the energy transition "
     "across hydrogen, data centers and e-mobility, and it is the work I want to do. I "
     "am a Maskinmester with a B.Tech degree in engineering and more than two years of "
     "experience with documentation management across complex projects, from "
     "GMP-qualified plants to enterprise deliveries, and I am meticulous by working "
     "method, not by promise.")

para("Managing documentation deliverables through a project is familiar ground: at Novo "
     "Nordisk I was responsible for quality documentation, acceptance tests and handover "
     "documentation under GMP/FDA/EMA, where every document was reviewed towards "
     "requirements before release, and in Ventek-Air and ELOHVAC I built handover "
     "packages and customer documentation from specification to final delivery. Being "
     "the contact point for documentation requirements is a role I know from both sides: "
     "towards customers, engineering functions and vendors, defining what documentation "
     "suppliers must deliver and following it up. I work in document management systems "
     "daily, and I use AI tools in Python and Claude to check, structure and report "
     "documentation faster without losing precision.")

para("Costs, risks and follow-up throughout the project are part of how I run "
     "documentation work: planned delivery, clear reporting and regular contact with "
     "stakeholders, with storage and submission at the right project phases. I "
     "contribute to continuous improvement with concrete tools: PDCA, A3 and "
     "standardised checklists, and I communicate clearly in Danish and English, in "
     "writing and in person. The team works from Ballerup, Middelfart, Västerås and "
     "Vaasa, and I am prepared to travel to the Swedish and Finnish offices as the work "
     "requires.")

para("The first 30 days I would spend on the systems and the requirements: the document "
     "management setup, the documentation requirements of the current projects and the "
     "engineering functions behind the documents. By day 60 I would own the "
     "documentation follow-up for my projects with clear reporting on delivery, cost and "
     "risk, and by day 90 suggestions for continuous improvement of templates, workflows "
     "and vendor requirements would be in place.")

para("I live in Måløv, close to the Ballerup office, and I can start after notice. I "
     "would welcome a conversation about the documentation work in Grid Integration, and "
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
para("Maskinmester (B.Tech) with an engineering background and more than two years of "
     "experience in documentation management across complex technical projects: "
     "documentation deliverables, requirements, review and follow-up in document "
     "management systems. Meticulous and pro-active; strong verbal and written "
     "communication in Danish and English; used to working with engineering functions, "
     "customers and vendors.")

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
bullet("Documentation management: documentation deliverables managed through projects; "
       "requirements, estimate costs and risks, follow-up and reporting; 2+ years of "
       "experience (GMP/FDA/EMA and enterprise deliveries).")
bullet("Contact point: documentation requirements within the company and towards "
       "customers and stakeholders; requirements defined for vendors and followed up.")
bullet("Document systems: administrate and check documentation in document management "
       "systems; review towards requirements; structured interaction with engineering "
       "functions.")
bullet("Delivery follow-up: planned documentation delivery monitored through project "
       "execution; clear reporting; store and submit project documentation by project phase.")
bullet("Risk and improvement: risks and opportunities identified; continuous improvement "
       "(PDCA, A3, standardised checklists).")
bullet("Engineering: electrical engineering background; high-voltage switchboards and "
       "10/0,4 kV systems; authorised Maskinmester (LV/MV/HV).")
bullet("Communication: strong verbal and written abilities; Danish (native) and English "
       "(fluent).")
bullet("Conditions: based in Ballerup (Middelfart possible); travel to Västerås and Vaasa "
       "as needed; driving licence B; available after notice.")

# ----------------------------- QUALITY CHECK -----------------------------
full = "\n".join(p.text for p in doc.paragraphs)
banned = ["spearheaded", "leveraged", "passionate", "dynamic", "results-driven",
          "proven track record", "synergy", "cutting-edge", "innovative solutions",
          "seamlessly", "robust", "demonstrated ability", "fast-paced",
          "drevet", "lidenskabelig", "dynamisk", "synergi", "banebrydende",
          "sømløst", "ikke kun", "men også", "\u2014", "passion",
          "not only", "but also", "passionate", "innovative"]
hits = [w for w in banned if w.lower() in full.lower()]
jd_words = ["documentation", "deliverables", "requirements", "document management systems",
  "vendors", "stakeholders", "engineering functions", "review", "administrate",
  "monitoring", "follow-up", "reporting", "project execution", "store", "submit",
  "risks", "opportunities", "continuous improvement", "meticulous", "pro-active",
  "communication", "danish", "english", "bachelor", "degree", "engineering",
  "substations", "distribution", "transmission", "grids", "grid integration",
  "hitachi energy", "ballerup", "middelfart", "västerås", "vaasa", "cost", "estimate",
  "technical", "project phase", "hydrogen", "data centers", "e-mobility"]
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
