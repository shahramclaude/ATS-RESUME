# -*- coding: utf-8 -*-
"""
Sensori Group — Electrical Package Manager (Denmark, on site).
Designet fra master-CV'erne. Sprog: engelsk (JD-sprog). Ansøgning + CV i ét dokument.

Vinkel: pakken afleveres ikke den dag sidste tavle sættes under spænding, men den dag
kunden kan åbne én mappe og finde hver testattest, hver variation med sin værdiansættelse
og hver mangel med sin underskrift — og slutafregningen stemmer med den tidsplan, der
faktisk blev leveret. Ærlig om at erfaringen er egen P&L og bygherresiden, ikke en
hovedentreprenørs månedlige værdiansættelser.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Electrical Package Manager — Sensori, Denmark | Scope, Programme, Cost, Quality, Close-out"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv, Denmark")
DATE = "1 November 2026"
RECIPIENT = ("Sensori Group · Denmark (on site) · Att: Electrical Delivery / Talent Acquisition")
SUBJECT = "Application: Electrical Package Manager"

# ------------------------------------------------------------------ side 1
INTRO = ['An electrical package is complete only when the installation, programme, accounts and records '
 'tell the same story. Energisation without signed inspections, unresolved variations or a missing '
 "O&M manual leaves the client with an unfinished package. Sensori's brief requires those "
 'workstreams to be controlled together, from mobilisation rather than reconstructed at handover.',
 'The delivery model below connects site leadership to commercial discipline: one scope baseline, '
 'measurable progress, controlled changes and evidence-led close-out. Its foundation is electrical '
 'installation and commissioning, 37 concurrent CAPEX projects in regulated production, and full '
 'P&L responsibility in an electrical contracting business.']

BULLETS = [('The requirement: own the package — scope, programme, cost, quality and close-out',
  'The answer is one package control sheet, live from mobilisation: WBS with percent complete, '
  'committed against earned against forecast cost, open QA and safety items, top risks and the '
  'next decision — reviewed weekly with the Project Manager. Evidence: 37 concurrent CAPEX '
  'projects (DKK 2–10m each), with zero critical findings at handover.'),
 ('The requirement: co-manage site safety and drive a strong QHSE culture',
  'The answer is to build the safety file at mobilisation, not at close-out: risk assessments, '
  'method statements, inductions, permits and the LOTO register indexed as the client will receive '
  'them, with safety a fixed item on the weekly coordination meeting and every action on an '
  'owner.'),
 ('The requirement: establish the QA file with the QA Manager and keep it compliant',
  'The answer is an inspection and test plan per system with declared hold and witness points '
  'before anything is energised, a non-conformance log closed with evidence, and a QA file '
  'complete the day the last panel is signed. FAT/SAT and IQ/OQ/PQ under GMP trained exactly '
  'that.'),
 ('The requirement: drive the package programme with the Project Manager and client milestones',
  'The answer is a three-week lookahead pulled from the master programme every week, a constraints '
  'log naming what is missing — design information, access, power, materials — and recovery '
  'measures proposed before the milestone is missed rather than after it.'),
 ('The requirement: control all package costs and issue weekly cost reports',
  'The answer is a weekly cost report reconciling hours by cost code against labour on site, '
  'subcontractor accruals against measured progress, goods receipting against purchase orders in '
  'the same week, and variations with a status each. Full P&L in my own company taught me that '
  'cycle.'),
 ('The requirement: run day-to-day site activity, subcontractor performance and manpower',
  'The answer is an allocation board by area reviewed at the morning huddle, a manpower histogram '
  'measured against the programme, and one coordination meeting with a fixed agenda — programme, '
  'manpower, snags, safety, materials, queries — and minutes with owners.'),
 ('The requirement: operate the in-progress snagging system and weekly punch lists',
  'The answer is a snag register live from first fix, not compiled at the end: location, system, '
  'subcontractor, owner, date, photograph, status. Punch lists are distributed the day they '
  'return, and an item closes only when it is re-inspected and signed — never on a promise.'),
 ('The requirement: weekly progress reporting and material deliveries aligned to the programme',
  'The answer is one report in one shape every week: progress rolled up from supervisor reports, '
  'the three things actually at risk, the dates that moved, deliveries tracked against the '
  'milestone and a dated photographic diary. I build these in Power BI and Python; Claude does the '
  'roll-up in minutes.'),
 ('The requirement: close out final account, O&M manuals, punch list, safety and QA files',
  'The answer is a close-out matrix opened on day one with an owner and a date against every line: '
  'final account reconciled, O&M compiled from submittals already in the QA file, punch list at '
  'zero, safety and QA files indexed, plant relocated and receipted. Close-out is a column in the '
  'weekly report, not a phase.')]

SYSTEM = ('One package control sheet links the WBS, programme, cost forecast, risks, safety, QA and '
 'close-out. Supervisor updates feed one weekly review; every exception carries an owner, due date '
 'and decision. Sensori procedures and reporting templates would govern the implementation.')

MIRROR = ('The technical foundation is an authorised electrical engineer (LV/MV/HV), B.Tech (EQF 6), '
 'electrical and mechanical systems knowledge and multidisciplinary site delivery. Danish is '
 'native and English professional. Excel, SAP, Power BI, Python and Claude support scheduling, '
 'analysis and reporting; technical and commercial outputs remain subject to human verification.')

HONEST = ('The experience is in electrical contracting, client-side CAPEX delivery and commissioning, not '
 'ownership of a hyperscale main-contractor package. A continuous five-to-ten-year record '
 'specifically managing large electrical installation packages, formal industrial relations '
 'negotiations and contractor/QS valuations is not claimed. Sensori-specific commercial procedures '
 'and project interfaces would be explicit onboarding priorities.')

CULTURE = ('Sensori names integrity, care and excellence and combines design, construction and maintenance '
 'with self-delivery. Applied to this package, that means honest forecasts, safe work fronts, '
 'coaching electricians and apprentices, and records the eventual operator can use. Its announced '
 'European expansion includes Denmark: consistent delivery controls matter as that business grows.')

PRACTICAL = ('Based in Måløv, Denmark; driving licence B. Site location, travel pattern and start date can be '
 'agreed. The role would be the priority, with arrangements for ELOHVAC agreed before appointment.')

CLOSING = ('A useful first discussion would be a review of the live package: where are programme, cost and '
 'close-out diverging, and which decision restores control?')

# ------------------------------------------------------------------ CV
PROFILE = ('The package requires linked control of scope, programme, cost, safety, quality and handover. '
 'Relevant delivery experience combines electrical installation and contracting at ELOHVAC, 37 '
 'concurrent CAPEX projects at Novo Nordisk and 11 parallel installation projects at Ventek-Air. '
 'Authorised electrical engineer (LV/MV/HV), with a B.Tech in Technology Management & Mechanical '
 'Engineering, full P&L responsibility and multidisciplinary team leadership. Electrical and '
 'mechanical interfaces understood through installation, commissioning and critical plant '
 'operations. Professional Claude user and coder: Python/Claude API tools for estimates, planning, '
 'checklists and KPI reporting.')

PRACTICE = [('Package and programme control',
  'Proposed package routine: Scope broken to WBS, percent complete rolled up from supervisor '
  'reports, three-week lookahead against client and consultant milestones, constraints log with '
  'named recovery measures — reviewed weekly with the project manager on one page.'),
 ('Cost control and commercial reporting',
  'Proposed package routine: Weekly cost report: direct labour by cost code, subcontractor '
  'accruals against measured progress, goods receipting matched to purchase orders, plant, '
  'variations with valuation status. Full P&L owner, including month-end and final accounts.'),
 ('Quality and compliance files',
  'Evidence: FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA, deviation handling and zero critical findings '
  'at handover. Application: inspection and test plans, hold points and signed QA records.'),
 ('Safety and QHSE',
  'Proposed package routine: Risk assessments and method statements, inductions, permits to work, '
  'LOTO register, weekly safety walks with actions and owners, near-miss reporting without blame, '
  'safety file closed out as a handover item.'),
 ('Subcontractor and multi-contractor coordination',
  'Proposed package routine: Weekly coordination meetings with fixed agenda and minutes, manpower '
  'histogram against programme, quality trends per subcontractor, direct labour allocation by '
  'area, hours issued weekly.'),
 ('Commissioning, energisation and close-out',
  'Proposed package routine: Switching and energisation sequences, permits, integrated testing, '
  'snag register to zero with re-inspection, O&M compiled from submittals, final account '
  'reconciled, plant relocated and receipted.')]

MODELS = [
    ("Package control",
     "WBS and scope baseline, percent complete by WBS, control sheet reviewed weekly, decision log and "
     "top-five risk register, interface matrix to mechanical, controls and commissioning"),
    ("Programme / schedule",
     "Master programme interface, three-week lookahead, constraints log, milestone tracking against "
     "consulting engineers and client dates, recovery measures with owners"),
    ("Cost / plant and equipment",
     "Weekly cost report, earned value by WBS, labour hours by cost code, subcontractor accruals and "
     "valuations, goods receipting, variations register, forecast at completion"),
    ("QA, safety and QHSE",
     "Inspection and test plans, hold and witness points, inspection records, test certificates, "
     "non-conformance log, safety file built at mobilisation, permits, LOTO register, close-out of both "
     "files"),
    ("Snagging and handover",
     "Live snag register by location and system, weekly punch lists from supervisors, distribution to "
     "subcontractors, re-inspection and sign-off, O&M compilation, material and plant relocation"),
]

ACHIEVEMENTS = [('37 concurrent CAPEX projects',
  'DKK 2–10m each; multidisciplinary leadership of 25 specialists and zero critical findings at '
  'handover.'),
 ('11 parallel installation projects',
  'DKK 2–10m each, with a 14-person team from specification to formal handover.'),
 ('Measured improvement',
  '40% lower energy costs through PDCA; above 40% productivity improvement through own '
  'AI-supported planning tools.')]

EXPERIENCE = [('Owner / Technical Director / Authorised Electrical Engineer',
  'ELOHVAC ApS · Copenhagen · May 2023 – Present',
  '5 electricians and 3 apprentices · full P&L',
  [('Contract delivery',
    'Quotations, planning, materials, subcontractors, quality assurance and handover '
    'documentation; full P&L responsibility.'),
   ('Technical and people leadership',
    'Electrical installation, distribution boards, controls, fault-finding and HVAC interfaces; '
    'daily allocation, individual follow-up and apprentice training.'),
   ('Safety and digital tools',
    'LOTO, risk assessment and documented quality control. Python/Claude API tools for estimates, '
    'planning, checklists and KPI dashboards; productivity improvement above 40%.')]),
 ('Senior Commissioning Engineer / Project Manager, Electrical Systems',
  'Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022 – Jul 2024',
  '37 concurrent CAPEX projects, DKK 2–10m each · 25 specialists · GMP/FDA/EMA',
  [('Project control',
    'Progress, budget, risk and resources across engineering, procurement and site; monthly '
    'reporting to management and client.'),
   ('Commissioning and quality',
    'FAT/SAT, IQ/OQ/PQ, validation documentation and deviation handling; zero critical findings at '
    'handover.'),
   ('Electrical systems and improvement',
    'Distribution boards, controls, UPS, emergency lighting and fire-system interfaces. SAP cost '
    'and asset control; 40% reduction in energy costs through PDCA.')]),
 ('Project and Workshop Manager',
  'Ventek-Air · Copenhagen · Jan 2022 – Nov 2022',
  '14-person team · 11 concurrent installation projects (DKK 2–10m) · specification to handover',
  [('Parallel project delivery',
    '11 projects from specification through production, assembly and formal handover, with '
    'capacity, material and subcontractor control.'),
   ('Daily huddles and bottleneck analysis',
    'standardised work at every station, with a marked lift in delivery performance and first-time '
    'quality.')]),
 ('Maintenance and Operations Manager / Workshop Technician',
  'Biofos (Lynetten) · Copenhagen · Aug 2017 – Jan 2022',
  '24/7 plant operations · pumps, HVAC, HV switchgear and SCADA · budgets in SAP',
  [('24/7 critical operations',
    'uptime, preventive maintenance and fast fault-finding with zero tolerance for unplanned '
    'stops.'),
   ('Structured maintenance',
    'standard work, 5S, PDCA maintenance plan, A3 root-cause analysis, spare-part flow and '
    'critical stores.'),
   ('Systems and safety',
    'LV/HV distribution and control systems; LOTO, risk assessment, near-miss reporting and '
    'toolbox talks; KPIs and budgets in SAP ERP.')]),
 ('Electromechanical Technician / Production Team Leader',
  'ARJ Engineering · Tehran · Dec 2003 – Mar 2010',
  '12-person production team · shift planning, material control and inventory',
  [('Team leadership',
    'shift planning, material control, inventory and line-side supply, target management and '
    'situational coaching.'),
   ('Technical problem solving',
    'diagnosis and repair of electrical and mechanical systems through structured root cause '
    'analysis.')])]

EDUCATION = [('B.Tech (EQF Level 6) — Technology Management & Mechanical Engineering',
  'Copenhagen School of Marine Engineering & Technology Management · 2017 – 2022 · GPA 7.6/12'),
 ('Electrical & Mechanical Design, Electrical Engineering (EQF Level 6)',
  'Tehran Technical University · 2000 – 2003'),
 ('Upper Secondary Examination (HF, mathematics and physics)', 'VUC · 2012 – 2017')]

CERTS = [('Danish Electrical Authorisation LV/MV/HV — Authorised Electrical Engineer',
  'Danish Safety Technology Authority · May 2023'),
 ('Refrigeration Technology & HVAC (AMU)', 'Mercantec · Mar 2021'),
 ('Lean and structured improvement — 5S, PDCA, VSM, A3, Kaizen',
  'Applied in operations and projects'),
 ('STCW maritime safety and engine-room certificates', 'Danish Maritime Authority · 2021–2023')]

LANGUAGES = ("Danish (native) · English (professional, written and spoken) · Persian/Farsi (native) · "
             "Driving licence B")

PRACTICAL_CV = (
    "On-site role in Denmark: based in Måløv with car and driving licence B — Greater Copenhagen, Jutland "
    "and Nordic travel arrangements to be agreed. Danish native, professional English. Start date and "
    "arrangements for the existing business to be agreed before appointment."
)

REFERENCES = ("Former managers at Novo Nordisk A/S (Kalundborg) and Biofos (Lynetten) — available on "
              "request.")

KEYWORDS = ('Electrical Package Manager · Commercial Records · QHSE · Site QA · Regulatory Requirements · '
 'Electrical Labour · Resource Allocation · Policies and Procedures · Manpower Levels · Weekly '
 'Progress Reports · Design Shortages · Third-Party Hold-ups · Site Meetings · Project Reviews · '
 'Engineering Reviews · Material and Plant Relocations · Trade Qualification · Third-Level '
 'Qualification · Design-and-Build Delivery · Industrial Relations · Multi-Contractor Environments '
 '· Health and Safety Legislation · Best Practice · IT Literacy · Project Scheduling · Reporting '
 'Tools · Written and Verbal Communication · Strict Deadlines · Large-Scale Projects')

# ------------------------------------------------------------ side 4
FIRST90 = [
    ("Days 1–30",
     "Read the package: scope, WBS, programme, budget, subcontractor orders and the QA and safety "
     "templates in use. Walk the site with the supervisors and Safety Advisor, and rebuild the package "
     "control sheet so scope, programme, cost, QA, safety and close-out sit in one place from week one."),
    ("Days 31–60",
     "Own the weekly rhythm: coordination meeting with fixed agenda and minutes, three-week lookahead, "
     "cost report reconciled to hours on site and goods receipted, progress report in one shape. Open the "
     "close-out matrix with an owner and a date against every line."),
    ("Days 61–90",
     "First full reporting cycle with forecast at completion, snag register live and punch lists returning "
     "weekly, QA file current with ITPs signed before energisation, safety file indexed as the client will "
     "receive it."),
    ("Year 1",
     "Trusted owner of the electrical package to handover: final account reconciled, O&M manuals compiled, "
     "punch list at zero, safety and QA files accepted — and the Danish delivery standard fed back into "
     "Sensori's Nordic business as it grows."),
]

PARTNER = [
    ("Sensori's electrical team",
     "The supervisors and electricians set the pace of the package: clear allocation by area, hours issued "
     "weekly, and a direct conversation about productivity instead of a report about it."),
    ("Subcontractors and suppliers",
     "Programme, manpower and quality measured weekly; snags distributed the day they are raised; "
     "deliveries tracked against the milestone and receipted the same week."),
    ("Client and consulting engineers",
     "Milestones, delays, design information and third-party hold-ups on one page every week — with the date that "
     "moved and the decision needed, not a narrative."),
    ("QA, safety and commercial",
     "QA Manager, Safety Advisor and commercial team work from the same structure I use on site: ITPs, "
     "NCRs, safety records and valuations each traceable to a WBS item and a date."),
]


def build(path):
    m = MasterDoc(TEMPLATE, lang="en-GB")

    # ---------------------------------------------------------------- side 1
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta(RECIPIENT)

    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, SUBJECT, bold=True, color="1A1A1A")

    for t in INTRO:
        m.para(t, after=24, line=218)

    for label, body in BULLETS:
        m.bullet(label, body, after=1, line=208)

    m.para(SYSTEM, after=20, line=212)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=0, line=204)

    m.meta("Yours sincerely · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFESSIONAL PROFILE")
    m.para(PROFILE, after=80)

    m.section("WHAT THE PACKAGE REQUIRES — AND HOW IT IS DELIVERED")
    for label, body in PRACTICE:
        m.bullet(label, body, after=20)

    m.models_table("PACKAGE CONTROL — METHODS APPLIED IN PRACTICE",
                   ("Area", "Methods and tools"), MODELS)

    m.section("SELECTED ACHIEVEMENTS")
    for label, body in ACHIEVEMENTS:
        m.bullet(label, body, after=20)

    m.section("PROFESSIONAL EXPERIENCE")
    for title, meta, scope, bullets in EXPERIENCE:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            if "ELOHVAC" in meta and label == "Technical and people leadership":
                m.page_break()
            m.bullet(label, body, after=20)

    m.section("EDUCATION")
    for t, meta in EDUCATION:
        m.edu(t, meta)

    m.section("CERTIFICATIONS & AUTHORISATIONS")
    for _i, (t, meta) in enumerate(CERTS):
        _p_ = m.edu(t, meta)
        if _i < len(CERTS) - 1:
            _p_.paragraph_format.keep_with_next = True

    m.section("LANGUAGES")
    m.para(LANGUAGES, after=80, justify=False)

    m.section("CORE COMPETENCIES & KEYWORDS")
    m.para(KEYWORDS, after=80)

    # afsluttende side
    m.page_break()
    m.models_table("FIRST 90 DAYS — HOW I WOULD TAKE OWNERSHIP",
                   ("When", "What is in place"), FIRST90)

    m.section("SITE OPERATIONS — ELECTRICAL WORKS AND INTERFACES")
    for label, body in PARTNER:
        m.bullet(label, body, after=20)

    m.section("PRACTICAL")
    m.para(PRACTICAL_CV, after=80)

    m.section("REFERENCES")
    m.para(REFERENCES, after=80, justify=False)

    # ingen afsnit eller tabelrække må knække over en sideskift
    for _p in m.doc.paragraphs:
        _p.paragraph_format.keep_together = True
    for _tbl in m.doc.tables:
        for _row in _tbl.rows:
            for _c in _row.cells:
                for _p in _c.paragraphs:
                    _p.paragraph_format.keep_together = True

    from docx.oxml import OxmlElement as _OE
    for _tbl in m.doc.tables:
        for _tr in _tbl._tbl.tr_lst:
            _pr = _tr.get_or_add_trPr()
            _el = _OE("w:cantSplit")
            _pr.append(_el)

    return m.save(path, title="Application and CV — Electrical Package Manager, Sensori",
                  subject="Electrical package · data centre · programme · cost · QA · safety · close-out",
                  keywords=("electrical package manager, electrical installation, data centre, mission "
                            "critical, programme, cost control, variations, valuations, QA file, safety "
                            "file, snagging, punch list, close-out, subcontractors, LV, MV, HV, "
                            "commissioning, danish, english"),
                  comments="Master design (navy banners, Calibri 9.5 pt). English, ATS-optimised. "
                           "Cover letter page 1, CV pages 2-3, close-out page 4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_Sensori_ElectricalPackageManager.docx")
    build(out)
    print("OK " + out)
