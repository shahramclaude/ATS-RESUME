#!/usr/bin/env python3
"""Build Shahram_Ajloo_BavarianNordic_BioriskManagementEngineer.docx (letter + CV).
Biorisk Management Engineer, Bavarian Nordic, Kvistgaard (Workday JR101623; no named
contact; apply via platform only). English document.
23.11.2026 user confirmations (unpinned, all concrete): containment/biosafety (cleanrooms,
HEPA, pressure cascades, decontamination, bioprocess equipment); FMEA/HAZOP/LOPA + design
reviews; physical security systems (access control, CCTV, intrusion detection).
Trumps from master: Novo Nordisk GMP/FDA/EMA + CQV chain (FAT/SAT/IQ/OQ/PQ) + HVAC/
ventilation. Career: Data Power first."""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

OUT = "Shahram_Ajloo_BavarianNordic_BioriskManagementEngineer.docx"

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
para("Application for Biorisk Management Engineer, Bavarian Nordic, Kvistgaard",
     style="LetterTitle")
para("Dear Bavarian Nordic Recruitment Team", after=4)

para("A containment system is only as strong as the weakest point between the first "
     "design sketch and daily operations: one unsealed penetration, one wrong pressure "
     "cascade or one untested HEPA filter, and the barrier is theatre. Keeping containment "
     "strong is engineering work, and it is work I know. I am a Maskinmester with a B.Tech "
     "degree in engineering at bachelor's or master's level and more than "
     "twenty years of engineering in industrial "
     "environments, including pharmaceutical production at Novo Nordisk and HVAC, "
     "ventilation and electrical systems where the details decide.")

para("Containment strategies are concrete experience for me: cleanrooms and HEPA "
     "filtration, pressure cascades, decontamination and waste handling, and the "
     "bioprocess-adjacent utilities that keep them running, combined with deep HVAC and "
     "ventilation practice from design to commissioning. I assess facilities, equipment "
     "and processes and turn risk assessments and regulations into engineering controls "
     "that are practical, maintainable and verifiable. GMP-aligned engineering is my "
     "daily standard: at Novo Nordisk I worked under GMP, FDA and EMA requirements where "
     "documentation and traceability were part of every handover.")

para("Risk-based commissioning, qualification and verification is a chain I have run end "
     "to end: FAT, SAT, IQ, OQ and PQ with acceptance criteria defined and critical "
     "systems tested before release. Design reviews and formalised risk assessments are "
     "familiar ground: FMEA, HAZOP and LOPA alongside structured problem solving, and I "
     "challenge solutions that could compromise containment. I also work with the systems "
     "around it: access control, CCTV and intrusion detection integrated with zoning and "
     "automation, and cross-functional technical projects with Engineering, Operations, "
     "Quality, EHS and external partners.")

para("The first 30 days I would spend in the facilities and the project pipeline: the "
     "containment basis of design, existing gaps and the expansions shaping vaccine "
     "production at the Kvistgaard site. By day 60 I would own my part of design reviews, "
     "BRM input to new laboratories and BSL-3 projects, and the qualification test "
     "strategies, and by day 90 containment awareness would be growing through advice and "
     "training while improvement projects ran with clear, traceable documentation.")

para("Kvistgaard is a manageable commute from Måløv, and I can start after notice. I "
     "would welcome a conversation about bringing engineering strength to biorisk "
     "management at Bavarian Nordic, and I can be reached at +45 93 99 95 14.")

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
para("Maskinmester (B.Tech) with more than twenty years of engineering across "
     "pharmaceutical and industrial environments: containment-minded HVAC, utilities and "
     "electrical systems from design through risk assessment to verified handover. "
     "Concrete experience with cleanrooms, HEPA filtration, pressure cascades, "
     "decontamination and CQV (FAT/SAT/IQ/OQ/PQ), design reviews with FMEA, HAZOP and "
     "LOPA, and physical security systems integrated with facility controls.")

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
bullet("Containment engineering: biorisk management driven from the engineering side, "
       "linking BRM, facility and process engineering, utilities, security and "
       "operations; facilities, equipment and processes assessed; risk assessments and "
       "regulations turned into practical, maintainable and verifiable engineering "
       "controls; containment strategies (pressure cascades, HVAC, HEPA filtration, "
       "decontamination, waste inactivation).")
bullet("Projects and design: BRM basis of design for laboratories, production "
       "facilities, expansions and BSL-3 projects; design reviews and risk assessments "
       "(FMEA, HAZOP, LOPA); solutions that could compromise containment constructively "
       "challenged; risk controls tested, documented and handed over to operations.")
bullet("Existing facilities: containment gaps and improvement opportunities spotted; "
       "changes supported with GMP, operability and business continuity balanced; "
       "engineering expertise contributed to investigations, deviations, CAPAs, audits "
       "and inspections; containment awareness built through advice and training.")
bullet("CQV: risk-based commissioning, qualification and verification (FAT, SAT, IQ, "
       "OQ, PQ); acceptance criteria and test strategies for containment-critical "
       "systems defined; hands-on testing and troubleshooting when it matters.")
bullet("Biosafety and biosecurity: biosafety risk assessment and containment strategies "
       "(concrete experience); access control, CCTV, intrusion detection and zoning "
       "integrated with containment systems together with Security, IT and Automation.")
bullet("Technical: HVAC, ventilation and cooling, HEPA and cleanroom-near "
       "installations, bioprocess-adjacent utilities; electrical installations, "
       "switchboards and control systems; MS Office, Teams, SharePoint.")
bullet("Regulated industry: pharmaceutical and biomanufacturing experience (GMP, FDA, "
       "EMA at Novo Nordisk); "
       "CQV documentation discipline; traceable documentation from requirement to "
       "handover.")
bullet("Languages: English (fluent) and Danish (native).")
bullet("Conditions: based in Måløv (commute to Kvistgaard); driving licence B; "
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
jd_words = ["biorisk", "biosafety", "biosecurity", "containment", "engineering",
  "facilities", "utilities", "equipment", "processes", "risk assessments", "regulations",
  "engineering controls", "pressure cascades", "hvac", "hepa", "filtration",
  "decontamination", "waste inactivation", "design reviews", "fmea", "hazop", "lopa",
  "laboratories", "production facilities", "bsl", "commissioning", "qualification",
  "verification", "fat", "sat", "iq", "oq", "pq", "acceptance criteria", "test strategies",
  "testing", "troubleshooting", "gmp", "deviations", "capa", "audits", "inspections",
  "training", "access control", "cctv", "intrusion detection", "zoning", "security",
  "automation", "cleanrooms", "bioprocess", "bachelor", "master", "degree",
  "pharmaceutical", "biomanufacturing", "vaccine", "cqv", "documentation", "project",
  "handover"]
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
