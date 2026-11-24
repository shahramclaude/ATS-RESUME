#!/usr/bin/env python3
"""Build Shahram_Ajloo_EurowindEnergy_TechnicalProjectLead_ControlSystems.docx.
Technical Project Lead - Control Systems Rollout, Eurowind Energy A/S, Hobro
(RiNA platform, Helios Cabinets/Controllers; contact: Tommy Graesborg Nielsen,
Global Senior Manager OT; apply ASAP). English document.
23.11.2026 user confirmations (unpinned): grid compliance = concrete knowledge;
relocation to Hobro area = OK (like Elektro-Isola/Vejle). Clean criminal record NOT
claimed in document - flagged to user instead. Career: Data Power first."""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_EurowindEnergy_TechnicalProjectLead_ControlSystems.docx"

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
para("Application for Technical Project Lead - Control Systems Rollout, Eurowind Energy",
     style="LetterTitle")
para("Dear Tommy Græsborg Nielsen", after=4)

para("A Helios Cabinet leaves the factory, and weeks later data flows correctly from an "
     "energy park to HQ while Operations takes over a documented installation. That "
     "chain, from shipment through installation and configuration to handover, is exactly "
     "the work this role owns. I am a Maskinmester with a B.Tech degree in engineering, "
     "the marine engineer background you ask for, an authorisation covering LV/MV/HV, and "
     "more than twenty years of hands-on work with control systems, electrical "
     "installations and commissioning, from planning to documented handover.")

para("Hands-on with OT is my daily practice: SCADA monitoring and control systems at "
     "Biofos, switchboards and control systems at Novo Nordisk, and commissioning and "
     "fault finding with A3, 5xWhy and Ishikawa in my own contracting work. I configure "
     "equipment and troubleshoot issues myself, verifying that signals and data flows are "
     "correct as part of how I commission, and I document as I go, so the handover to "
     "Operations is a clean package and not a loose end.")

para("Planning technical installations and coordinating multiple parties including "
     "external contractors is portfolio work for me: 37 concurrent plant projects at "
     "Novo Nordisk and 11 at Ventek-Air, each with dependencies, progress and outstanding "
     "work kept visible. Grid compliance is knowledge I use in practice: I work under the "
     "electricity supply regulations (BEK 1649) with an authorisation covering LV/MV/HV. "
     "Every deployment teaches something, and improving the rollout process between "
     "installations is how I already work: standardised methods that measurably improved "
     "delivery capability.")

para("The first 30 days I would spend with the OT Operations team and the first RiNA "
     "deployment end to end: the Helios setup, the installation checklist, the data flow "
     "to HQ and the documentation package. By day 60 I would own my rollout schedule "
     "across parks with autonomy to plan and drive it and with dependencies and progress "
     "visible, and by day 90 the process improvements from the first deployments would be "
     "captured in updated routines.")

para("I am ready to relocate to the Hobro area for this role, and the travel to parks in "
     "Denmark and occasionally abroad suits me. I can start after notice, and I would "
     "welcome a conversation with you about rolling out RiNA across the energy parks. I "
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
para("Maskinmester (B.Tech) with more than twenty years of hands-on technical work across "
     "control systems, SCADA, electrical installations and commissioning: plans and "
     "drives installations from shipment and configuration to documented handover, with "
     "progress tracking and external contractors coordinated. Combines OT troubleshooting "
     "done personally with grid compliance knowledge in practice (BEK 1649, LV/MV/HV "
     "authorisation) and a structured approach to technical documentation and process "
     "improvement.")

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
bullet("Background: marine engineer (Maskinmester, B.Tech) with electrical engineering "
       "focus; authorisation covering LV/MV/HV.")
bullet("OT and control systems: hands-on experience with SCADA, control systems, "
       "automation, OT infrastructure and technical commissioning; equipment configured "
       "and technical issues troubleshot personally.")
bullet("Rollout and installations: deployments planned and coordinated across energy "
       "parks; shipments and installation coordinated with local teams and external "
       "contractors; activities aligned with IT, Operations and CIS stakeholders.")
bullet("Data and configuration: controllers configured to communicate with park assets; "
       "data flows between parks and HQ verified; issues resolved during installation.")
bullet("Grid compliance: knowledge applied in practice under the electricity supply "
       "regulations (BEK 1649); authorisation covering LV/MV/HV.")
bullet("Planning and documentation: progress, dependencies and outstanding work tracked; "
       "structured technical documentation and handover to Operations; rollout process "
       "improved based on experience from each deployment.")
bullet("Collaboration: independent work with colleagues and stakeholders kept informed; "
       "coordination across internal functions and external contractors.")
bullet("Technical: electrical installations, switchboards and control systems, ventilation "
       "and cooling; MS Office, Teams, SharePoint, Power Query; SAP ERP.")
bullet("Languages: English (fluent) and Danish (native).")
bullet("Conditions: ready to relocate to the Hobro area; travel to parks in Denmark and "
       "occasionally abroad accepted; driving licence B; available after notice.")

# ----------------------------- QUALITY CHECK -----------------------------
full = "\n".join(p.text for p in doc.paragraphs)
banned = ["spearheaded", "leveraged", "passionate", "dynamic", "results-driven",
          "proven track record", "synergy", "cutting-edge", "innovative solutions",
          "seamlessly", "robust", "demonstrated ability", "fast-paced",
          "drevet", "lidenskabelig", "dynamisk", "synergi", "banebrydende",
          "sømløst", "ikke kun", "men også", "\u2014", "passion",
          "not only", "but also", "passionate", "innovative"]
hits = [w for w in banned if w.lower() in full.lower()]
jd_words = ["technical project lead", "control systems", "rollout", "deployment",
  "energy parks", "scada", "automation", "ot", "commissioning", "marine engineer",
  "electrical engineer", "hands-on", "configuration", "configure", "troubleshoot",
  "technical issues", "data flows", "installation", "planning", "progress", "dependencies",
  "documentation", "handover", "operations", "contractors", "external", "stakeholders",
  "grid compliance", "structured", "independent", "shipment", "controllers", "park",
  "rina", "autonomy", "troubleshooting", "technical documentation"]
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
