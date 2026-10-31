# -*- coding: utf-8 -*-
"""
Thermo Fisher Scientific — Operations Supervisor, Day (Roskilde, R-01372520).
v2: executive-grade, ATS-first. Renders the SAME content model to .docx and .pdf.

Design rules
  * One column, no tables, no text boxes, no icons — safe for Workday/ATS parsing.
  * Real text in the PDF text layer (not an image), selectable and extractable.
  * Keyword coverage in context (Areas of expertise + experience), no "keyword dump" heading.
  * Page 1 = cover letter about the operation; CV follows from page 2.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

DATE = "30 October 2026"
RECIPIENT = ("Thermo Fisher Scientific · Roskilde, Denmark · Hiring Manager, Operations · "
             "Job ID R-01372520 · Fully onsite")
SUBJECT = "Application: Operations Supervisor, Day — Roskilde (R-01372520)"

# ----------------------------------------------------------------------------- letter
OPENING = [
    "A regulated site is not run from a meeting room. It is run at 07:00, at the tier-1 board, where the shift "
    "agrees what is true today: which line is running to standard, which deviation is still open, which material "
    "is not at the line, and who owns each countermeasure before the next huddle. Your posting describes that "
    "responsibility precisely — daily production operations, quality and safety standards, team development and "
    "continuous improvement inside a strict GMP and FDA framework, supported by PPI. That is the operation I have "
    "been running for twenty years, and the system for it here is already built:",

    "Roskilde is real production, highly automated, with PPI as the way work is improved. The first ninety days "
    "follow that order: week one on the floor and at the boards, day thirty with tiered daily management and "
    "escalation live, day ninety with gains that hold without me standing next to them.",
]

POINTS = [
    ("Running the day",
     "Tiered huddles, visual boards for Safety, Quality, Delivery, Inventory and Productivity, named owners, "
     "escalation inside the shift and Gemba walks that end where the problem is. That cadence has run over 37 "
     "concurrent CAPEX projects worth DKK 2–10m each, a 14-person production team and 25 specialists — with "
     "deviations caught in hours, not at month-end."),

    ("Improving the day",
     "Lean manufacturing and process improvement are my working method, in PPI's own logic: 8-step problem solving "
     "and A3, Kaizen events and Just-Do-It actions, value stream mapping, standard work, 5S, visual management, "
     "SMED, TPM and Poka-Yoke — root cause before countermeasure, ownership fixed by RACI. Results I can defend: +40% productivity in a "
     "technical service operation and −40% energy cost in regulated production."),

    ("Protecting the day",
     "Quality is documentation you can audit years later: SOP and batch record discipline, deviation and CAPA, "
     "change control, clean room and gowning behaviour, FAT/SAT and IQ/OQ/PQ. At Novo Nordisk that closed with "
     "zero critical findings at handover under GMP/FDA/EMA; in 24/7 critical operations it kept the plant "
     "running without unplanned stops."),

    ("Safety before output",
     "LOTO, risk assessment, safety walks and toolbox talks mean little without near-miss reporting followed to "
     "closure and a stop-the-line right people actually use. In my operations that is measured like every other "
     "KPI: an unsafe shift is a failed shift, whatever the output."),

    ("The team around the line",
     "Situational leadership, GROW coaching, SBI feedback, 1:1s and development reviews, competence matrices, "
     "30-60-90 onboarding and structured operator and apprentice training — with the psychological safety that "
     "makes the near-miss get reported. I have built teams of 5 to 25 in two countries; capable people who stay "
     "are the only sustainable capacity plan."),

    ("Across functions and systems",
     "Cross-functional work is deliberate: daily interfaces to Quality, Engineering, Supply Chain and Finance on "
     "one shared plan and written "
     "follow-up; SAP ERP and CMMS as the source of truth, Power BI and Office for the boards — plus my own "
     "tooling as a professional, active Claude coder (Python, Claude API): shift dashboards, OEE and capacity "
     "models, investment models for development and new business ideas. The supervisor belongs on the floor."),
]

MIRROR = ("**Against your requirements:** 20+ years in operations management (5+ required), leading teams of "
          "5–25 since 2003 (2+ required) · Lean and continuous improvement as a daily system, not a certificate · "
          "problem-solving, decision-making, organizational skills, time management proven in 24/7 critical "
          "operations · clear written and verbal communication, strong interpersonal skills, Danish and English · "
          "ERP (SAP), Office, Power BI · clean rooms, warehouses, manufacturing · safety and regulatory "
          "compliance, GMP/FDA quality management systems from Novo Nordisk.")

HONEST = ("**Two things, plainly.** My supervisory years are in technical production, maintenance and project "
          "operations inside GMP — I have owned the daily management system, the people and the compliance, but "
          "not yet a moulding or filling line; that product flow I will learn in weeks, because the system around "
          "it is the one I already run. And my written English is professional, not native: boards, records and "
          "reviews I produce are concise and audit-ready — better to say that than have it found out in week two.")

CULTURE = ("**Why Thermo Fisher Scientific, and why Roskilde.** PPI is the most complete version of what I already "
           "practise: 8-step problem solving, tiered accountability, Gemba, standard work, a project funnel and a "
           "bronze-to-gold maturity model, with supervisors trained in Leading Through PPI — improvement as a "
           "system, not a series of campaigns. The 4i Values read like an operating standard I recognise: "
           "Integrity as open communication and honoured commitments, Intensity as speed with excellence, "
           "Innovation as turning knowledge into something measurably better for the customer, Involvement as one "
           "team that listens. A site among the most automated in the world, where you can see the production from "
           "your desk, is where a supervisor moves a number — and the mission is the one I already work under.")

PRACTICAL = ("**Practical:** day shift, fully onsite in Roskilde, start at short notice; on appointment I wind down "
             "my own company, so there are no competing commitments. Driving licence B, easy commute from Måløv. "
             "I would welcome a conversation about where the next twelve months of improvement should land.")

# ----------------------------------------------------------------------------- CV
NAME = "Shahram Ajloo"
TITLE = "Operations Supervisor · Lean / Operational Excellence (PPI) · GMP-Regulated Manufacturing"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv, Denmark (commutable to Roskilde)")

PROFILE = ("Operations and production leader with 20+ years in regulated manufacturing — pharmaceutical and "
           "technical production — with "
           "leadership responsibility since 2003 for teams of 5 to 25 and full P&L accountability. Runs daily management the way PPI expects it — tiered huddles, SQDIP boards, Gemba, "
           "escalation paths, A3 and 8-step problem solving, standard work — and develops people through "
           "situational leadership, coaching and competence matrices. Documented results: +40% productivity, "
           "−40% energy cost, zero critical deviations at handover under GMP/FDA/EMA. Professional and active "
           "Claude coder: builds the dashboards, OEE and capacity models and investment models the operation runs "
           "on. B.Tech in Technology Management & Mechanical Engineering (EQF 6); authorised electrical engineer "
           "LV/MV/HV; Danish native, English professional.")

EXPERTISE = [
    ("Lean & operational excellence",
     "PPI 8-step problem solving · A3 · Kaizen events & Just-Do-It · value stream mapping · standard work · 5S & "
     "visual management · tiered daily management · Gemba walks · SMED · TPM · Kanban/WIP · Poka-Yoke · "
     "Ishikawa & 5 Why · FMEA · DMAIC/Six Sigma tools · Toyota Kata · Yokoten · SQDIP, OEE, OTD, MTBF/MTTR · "
     "RACI, escalation ladders, countermeasure tracking to closure."),
    ("Quality, compliance & EHS",
     "GMP/cGMP and FDA expectations · quality management system and ISO 13485 · medical device and "
     "pharmaceutical manufacturing · regulated manufacturing · SOP and batch "
     "documentation · deviation handling, CAPA and change control · audit readiness and inspection support · "
     "FAT/SAT, IQ/OQ/PQ · clean room and gowning discipline · risk assessment (APV) · LOTO · near-miss reporting "
     "to closure · toolbox talks and safety walks · IMS."),
    ("People, systems & business",
     "Situational leadership (SLII) · GROW coaching · SBI feedback · 1:1s, performance and development reviews · "
     "competence matrices and individual development plans · organizational skills and time management · "
     "30-60-90 onboarding · operator and apprentice "
     "training · psychological safety · change leadership · SAP ERP · CMMS · Microsoft Office/Power BI · "
     "Python/Claude API (OEE, capacity, investment NPV/IRR models) · P&L, budget and cost control."),
]

ACHIEVEMENTS = [
    "**Zero critical deviations at handover** across 37 concurrent CAPEX and plant projects (DKK 2–10m each) "
    "under GMP/FDA/EMA — delivered with deviation handling, CAPA and change control in a live audit trail.",
    "**+40% productivity** in a technical service operation through data-driven planning, standard work and "
    "self-built AI tooling; the same operation reported response time, first-time quality and delivery daily "
    "instead of monthly.",
    "**−40% energy cost** in regulated production through a structured PDCA programme with A3 problem solving and "
    "standardised work — improvement sustained after the project team disbanded.",
    "**Tiered daily management introduced** in three operations, replacing month-end reporting with visual boards, "
    "named countermeasures and same-shift escalation.",
    "**Teams built and developed** across two countries — 25 specialists, a 14-person production team, a "
    "12-person workshop and 5 electricians with 3 apprentices — with competence matrices and individual "
    "development plans.",
    "**Reporting automated** with SAP ERP, CMMS, Power BI and Python/Claude API, removing manual consolidation "
    "from the shift and freeing supervisor time for the floor.",
]

EXPERIENCE = [
    {"job": "Owner / Technical Director / Authorised Electrical Installer",
     "meta": "ELOHVAC ApS · Copenhagen, Denmark · May 2023 – Present",
     "scope": "Full P&L · 5 electricians + 3 apprentices · service and installation operations",
     "bullets": [
         "Own daily operations end to end: production planning, capacity against the order book, material and "
         "spare-part flow, quality control, on-time delivery and cost — reviewed every morning against standard "
         "work, 5S, visual boards and KPI follow-up on response time, first-time quality and delivery.",
         "Supervise and develop 5 electricians and 3 apprentices: daily planning, 1:1s and performance reviews, "
         "competence matrix, safety follow-up and structured training across shifting sites and priorities.",

         "Built the digital backbone myself — ERP-based order and spare-part control, Power BI dashboards, and "
         "Python/Claude API tools for planning, quotations, checklists and reporting.",
         "EHS and compliance: risk assessment at every new site, LOTO, near-miss handling, documented service "
         "records; zero critical deviations in the service portfolio.",
     ]},
    {"job": "Senior Commissioning Engineer / Project Manager, Electrical Systems",
     "meta": "Novo Nordisk A/S · Kalundborg / Bagsværd, Denmark · Nov 2022 – Jul 2024",
     "scope": "37 concurrent CAPEX projects (DKK 2–10m each) · 25 specialists · GMP/FDA/EMA",
     "bullets": [
         "Coordinated 37 concurrent CAPEX and plant projects across engineering, procurement and site operations: "
         "schedule, cost, risk, resources and monthly reporting to management and client.",
         "Led 25 highly specialised colleagues cross-functionally in clean room areas, warehouses and manufacturing: "
         "work permits, LOTO and gowning discipline, with commissioning and qualification (FAT/SAT, IQ/OQ/PQ), "
         "deviation handling, CAPA and change control — zero critical findings at handover.",
         "Delivered −40% energy cost through a structured PDCA programme with A3 problem solving and standard "
         "work; SAP ERP for cost, asset and order control.",
     ]},
    {"job": "Project and Workshop Manager, Ventilation & Climate",
     "meta": "Ventek-Air · Copenhagen, Denmark · Jan 2022 – Nov 2022",
     "scope": "11 concurrent projects (DKK 2–10m) · 14-person production and assembly team",
     "bullets": [
         "Daily leadership of a 14-person production and assembly team: capacity planning, flow control and "
         "delivery performance from specification to formal handover.",
         "Introduced daily huddles and bottleneck analysis; standardised work at every station with a marked lift "
         "in delivery performance and first-time quality.",
         "Managed suppliers and subcontractors, contract basis, safety documentation and handover packages.",
     ]},
    {"job": "Maintenance and Operations Manager / Workshop Technician",
     "meta": "Biofos (Lynetten) · Copenhagen, Denmark · Aug 2017 – Jan 2022",
     "scope": "24/7 critical operations · pumps, HVAC, HV switchgear, SCADA · IMS",
     "bullets": [
         "Ran critical electrical and mechanical operations with zero tolerance for unplanned stops: uptime, "
         "preventive maintenance and fast fault-finding around the clock.",
         "Introduced structured maintenance routines (standard work, 5S), PDCA-based preventive maintenance and root "
         "cause analysis (A3); owned spare-part flow and stores for critical operations.",
         "Shift operations with safety discipline: LOTO, risk assessment, near-miss reporting and toolbox talks; "
         "KPIs and operations budgets in SAP ERP.",
     ]},
    {"job": "Electromechanical Technician / Production Team Leader",
     "meta": "ARJ Engineering · Tehran, Iran · Dec 2003 – Mar 2010",
     "scope": "12-person production team · machine workshop",
     "bullets": [
         "Led a 12-person production team: shift planning, material control, target management and situational "
         "coaching.",
         "Diagnosed and repaired industrial electrical and mechanical systems using structured root cause analysis "
         "and corrective action.",
     ]},
]

EDUCATION = [
    "B.Tech (EQF level 6), Technology Management & Mechanical Engineering — Copenhagen School of Marine "
    "Engineering & Technology Management, 2017–2022 · GPA 7.6/12 (ECTS).",
    "Electrical & Mechanical Design, Electrical Engineering (EQF level 6) — Tehran Technical University, "
    "2000–2003.",
    "Upper secondary (HF, mathematics/physics) — VUC, 2012–2017.",
]

CERTS = [
    "Danish electrical authorisation LV/MV/HV — Danish Safety Technology Authority, May 2023.",
    "Lean practice: 5S, PDCA, value stream mapping, A3 and Kaizen.",
    "Refrigeration & HVAC technology (AMU) — Mercantec, 2021.",
    "STCW: engine-room watch (A-III/1), designated safety duties (VI/6), ship security officer (VI/5), security "
    "awareness (VI/6-1), tanker basic (V/1-1, V/1-2) — Danish Maritime Authority, 2021–2023.",
]

LANGUAGES = ("Danish (native) · English (professional, written and spoken) · Persian/Farsi (native) · "
             "Driving licence B")

# ----------------------------------------------------------------------------- DOCX
def render_docx(path):
    from ats_builder import Application
    from docx.shared import Pt, RGBColor

    class Tight(Application):
        """Same ATS-safe layout, tuned so the letter holds exactly one page."""

        def para(self, text, before=0, after=2.7, line=11.45):
            return super().para(text, before, after, line)

        def bullet(self, label, body, after=1.7, line=11.15):
            return super().bullet(label, body, after, line)

    a = Tight(size=9.1)          # letter body (holds exactly one page)
    a.cover_letter(
        date=DATE, recipient=RECIPIENT, subject=SUBJECT, opening=OPENING, points=POINTS,
        mirror=MIRROR, honest=HONEST, culture=CULTURE, practical=PRACTICAL,
        signoff="Sincerely,", signature=NAME,
        contact="+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark",
    )

    a.size = 9.3                 # CV body
    a.name(NAME, page_break=True)
    p = a._p(after=0.5, line=11.6)
    r = p.add_run(TITLE)
    r.font.size = Pt(9)
    r.font.bold = True
    r.font.color.rgb = __import__("ats_builder").ACCENT
    a.meta(CONTACT)

    a.heading("Profile", before=7)
    a.para(PROFILE, after=2)

    a.heading("Areas of expertise")
    for label, body in EXPERTISE:
        a.bullet(label, body)

    a.heading("Selected achievements")
    for line in ACHIEVEMENTS:
        a.bullet(None, line)

    a.heading("Professional experience")
    for item in EXPERIENCE:
        a.job(item["job"], item["meta"])
        p = a._p(after=1.5, line=10.4, keep=True)
        r = p.add_run("Scope: " + item["scope"])
        r.font.size = Pt(8.3)
        r.font.italic = True
        r.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
        n = len(item["bullets"])
        for i, b in enumerate(item["bullets"]):
            par = a.bullet(None, b)
            # keep the first two bullets with their heading, and never leave one bullet alone
            if i == 0:
                par.paragraph_format.keep_with_next = True

    a.heading("Education")
    for line in EDUCATION:
        a.bullet(None, line)

    a.heading("Certifications and training")
    for line in CERTS:
        a.bullet(None, line)

    a.heading("Languages and practical")
    for line in [LANGUAGES]:
        a.bullet(None, line)

    a.save(path,
           title="Application and CV — Operations Supervisor, Day, Thermo Fisher Scientific Roskilde (R-01372520)",
           subject="Operations Supervisor · Lean/PPI · GMP manufacturing · Roskilde",
           keywords=("operations supervisor, operations management, manufacturing, GMP, FDA, lean, continuous "
                     "improvement, PPI, kaizen, 5S, standard work, root cause analysis, ERP, SAP, Power BI"),
           comments="Cover letter + CV in one document. English, ATS-optimised.")
    return path


# ----------------------------------------------------------------------------- PDF
def render_pdf(path):
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
    from reportlab.lib.colors import HexColor
    from reportlab.lib import colors
    from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer,
                                    PageBreak, HRFlowable)

    INK = HexColor("#1A1A1A")
    META = HexColor("#555555")
    ACC = HexColor("#0077C8")

    base = ParagraphStyle("base", fontName="Helvetica", fontSize=9.2, leading=11.3,
                          textColor=INK, alignment=TA_LEFT, spaceAfter=0)
    body = ParagraphStyle("body", parent=base, alignment=TA_JUSTIFY, spaceAfter=2.6)
    bullet = ParagraphStyle("bullet", parent=base, alignment=TA_JUSTIFY, leftIndent=10,
                            bulletIndent=1, spaceAfter=1.9, leading=11.1)
    meta = ParagraphStyle("meta", parent=base, fontSize=8.3, leading=10.4, textColor=META)
    subj = ParagraphStyle("subj", parent=base, fontName="Helvetica-Bold", fontSize=10,
                          leading=12, spaceBefore=2, spaceAfter=3)
    h = ParagraphStyle("h", parent=base, fontName="Helvetica-Bold", fontSize=8.6, leading=10.4,
                       spaceBefore=6.5, spaceAfter=2.2)
    nm = ParagraphStyle("nm", parent=base, fontName="Helvetica-Bold", fontSize=17, leading=19)
    ti = ParagraphStyle("ti", parent=base, fontName="Helvetica-Bold", fontSize=9, leading=11,
                        textColor=ACC, spaceAfter=1)
    job = ParagraphStyle("job", parent=base, fontName="Helvetica-Bold", fontSize=9.3, leading=11.2,
                         spaceBefore=4, spaceAfter=0, keepWithNext=1)
    meta2 = ParagraphStyle("meta2", parent=meta, keepWithNext=1)
    scope = ParagraphStyle("scope", parent=base, fontName="Helvetica-Oblique", fontSize=8.2,
                           leading=10, textColor=META, spaceAfter=1.4, keepWithNext=1)
    bulletk = ParagraphStyle("bulletk", parent=bullet, keepWithNext=1)

    def rule():
        return HRFlowable(width="100%", thickness=0.5, color=HexColor("#C9C9C9"),
                          spaceBefore=0, spaceAfter=2)

    def bold(t):
        return f"<b>{t}</b>"

    doc = BaseDocTemplate(path, pagesize=A4, leftMargin=1.6 * cm, rightMargin=1.6 * cm,
                          topMargin=1.2 * cm, bottomMargin=1.05 * cm,
                          title="Application and CV — Operations Supervisor, Day (R-01372520)",
                          author=NAME, subject="Thermo Fisher Scientific, Roskilde",
                          keywords="operations supervisor, GMP, lean, PPI, continuous improvement")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame])])

    s = []
    s.append(Paragraph(DATE, meta))
    s.append(Paragraph(RECIPIENT, meta))
    s.append(Paragraph(SUBJECT, subj))
    for t in OPENING:
        s.append(Paragraph(t.replace("**", ""), body))
    s.append(Spacer(1, 2))
    for label, txt in POINTS:
        s.append(Paragraph(f"<b>{label}.</b> {txt}", bullet, bulletText="\u2022"))
    s.append(Spacer(1, 2))
    for t in (MIRROR, HONEST, CULTURE, PRACTICAL):
        s.append(Paragraph(t.replace("**", ""), body))
    s.append(Spacer(1, 3))
    s.append(Paragraph("Sincerely,", body))
    s.append(Paragraph(f"<b>{NAME}</b>", ParagraphStyle("sig", parent=base, fontSize=10, leading=12)))
    s.append(Paragraph("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
                       "Måløv, Denmark", meta))

    s.append(PageBreak())
    s.append(Paragraph(NAME.upper(), nm))
    s.append(Paragraph(TITLE, ti))
    s.append(Paragraph(CONTACT, meta))

    def section(title, flows):
        flows.append(Paragraph(title.upper(), h))
        flows.append(rule())

    section("Profile", s)
    s.append(Paragraph(PROFILE, body))
    section("Areas of expertise", s)
    for label, txt in EXPERTISE:
        s.append(Paragraph(f"<b>{label}:</b> {txt}", bullet, bulletText="\u2022"))
    section("Selected achievements", s)
    for line in ACHIEVEMENTS:
        s.append(Paragraph(line.replace("**", ""), bullet, bulletText="\u2022"))
    section("Professional experience", s)
    for item in EXPERIENCE:
        s.append(Paragraph(item["job"], job))
        s.append(Paragraph(item["meta"], meta2))
        s.append(Paragraph("Scope: " + item["scope"], scope))
        n = len(item["bullets"])
        for i, b in enumerate(item["bullets"]):
            sty = bulletk if i == 0 else bullet
            s.append(Paragraph(b, sty, bulletText="\u2022"))
    section("Education", s)
    for line in EDUCATION:
        s.append(Paragraph(line, bullet, bulletText="\u2022"))
    section("Certifications and training", s)
    for line in CERTS:
        s.append(Paragraph(line, bullet, bulletText="\u2022"))
    section("Languages and practical", s)
    s.append(Paragraph(LANGUAGES, bullet, bulletText="\u2022"))

    doc.build(s)
    return path


if __name__ == "__main__":
    out_dir = "/home/user/Claude"
    d = render_docx(os.path.join(out_dir, "Shahram_Ajloo_ThermoFisher_OperationsSupervisor_v2.docx"))
    p = render_pdf(os.path.join(out_dir, "Shahram_Ajloo_ThermoFisher_OperationsSupervisor_v2.pdf"))
    print("OK", d)
    print("OK", p)
