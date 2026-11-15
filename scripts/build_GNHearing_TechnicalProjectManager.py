# -*- coding: utf-8 -*-
"""GN Hearing — Technical Project Manager, Production Support & Technical Purchasing, Præstø.
English posting -> English document.

Form (master/FORMKATALOG.md): opening **V** (variation: the hardest machine is not the
slowest, it is the one that behaves differently on Tuesday), structure **From the URS to
the audit file** (requirement · supplier · equipment · validation · change · record),
register **The Line** (SMD, reflow, stencil, fixture, AOI, calibration, yield, changeover,
first article, transport plate).
Culture file: jd/GN_Hearing_TechnicalProjectManager_kultur.txt. Deadline 5/6 Dec 2026.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Technical Project Manager · regulated production, validation and technical purchasing'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('14 November 2026')
    m.meta('GN Hearing · Component Manufacturing Engineering, Global Operations · Præstø · R30687')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Technical Project Manager', bold=True, color='1A1A1A')

    def lp(text, after=42):
        return m.para(text, after=after, line=236)

    # ---------------------------------------------------------------- page 1
    lp('**The hardest machine on a production line is not the slowest one. It is the one that behaves '
       'differently on Tuesday.** A line that runs at 94 % one week and 78 % the next has not got a speed '
       'problem — it has a variation problem, and the answer is almost never new equipment. It is a worn '
       'fixture, a stencil that should have been cleaned, a calibration that drifted, a supplier who changed '
       'the plating, or a change that nobody wrote down before making it.', after=38)

    lp('Your phrase for it is **"production continuity"**, and at Præstø it is earned on a fully automated '
       'line where transport plates move between cells and the hybrids do not get a second attempt. That is a '
       'discipline of small things, kept by the person who writes the change down **before** the change is '
       'made — and who can then show an auditor what was installed, when, and why.', after=38)

    lp('**From the URS to the audit file. Six links — and a project is only as strong as the weakest.**',
       after=28)

    lp('**The requirement.** What the equipment has to do, in numbers, agreed before a supplier is called — '
       'cycle time, capacity, tolerance, interfaces, calibration interval, documentation. At Novo Nordisk '
       'every change began with a written needs analysis, and 37 capital projects were approved on that '
       'document rather than on a datasheet.', after=24)

    lp('**The supplier.** Price is one of five terms. Lead time, service level, spare parts, training and a '
       '**statement of work** that says who does what — negotiated from evidence, not accepted from a '
       'quotation. I have bought equipment, tooling and subcontractor capacity with my own margin at risk '
       'since 2023.', after=24)

    lp('**The equipment.** Installation, calibration protocol and first article before production is handed '
       'back to Operations. **FAT/SAT** was my standard in the pharma projects: the machine proves itself in '
       'the factory and again on the floor, with the acceptance criteria written in advance.', after=24)

    lp('**The validation.** IQ/OQ/PQ, and the documentation produced while the work happens rather than '
       'reconstructed afterwards. In a GMP/FDA/EMA environment this was not a phase at the end — a late '
       'quality gate does not delay a project, it stops it.', after=24)

    lp('**The change.** Change control with a risk assessment, agreed with Operations and Quality, then the '
       'SOP and the training before the change touches the line. The expensive version of a change is the '
       'one that arrives on the floor as a surprise on a Thursday; the difference between moving fast and '
       '**"manufacturing change responsibly"** is a document and a signature, not a delay.', after=24)

    lp('**The record.** **Audit-ready** means a stranger can follow the equipment from requirement to '
       'decommissioning without asking me a question: what was installed, when, by whom, calibrated when, '
       'changed why. All 37 of my handovers closed with **zero critical deviations** because the file was '
       'built as the work went, not after it.', after=32)

    lp('**Where my record is thinner, stated plainly.** I have not worked in SMD/PCBA production, and I do '
       'not hold **ISO 13485** — my regulated record is pharmaceutical (GMP/FDA/EMA) rather than medical '
       'devices. My electronics are power, control, test and calibration: switchgear, PLC, instrumentation '
       'and commissioning. What transfers is everything else in your posting — equipment projects with '
       'FAT/SAT and IQ/OQ/PQ, technical purchasing and supplier negotiation with my own money at risk, change '
       'control with Operations and Quality, and a documentation habit that survives an audit.', after=32)

    lp('**Why Præstø and GN Hearing.** The site is one of the few places in Europe where the hardest part of '
       'a hearing aid is manufactured in Denmark: the hybrid, on a fully automated line, with cobots moving '
       'the transport plates and around sixty people running production round the clock, and where the '
       'promise is **"uninterrupted production"**. You say the point of the team is **"reliable, compliant, '
       'and scalable manufacturing of medical electronic devices"**, and '
       'that the role must **"connect engineering, operations, quality, and suppliers"** to deliver '
       '**"robust manufacturing solutions"** and **"stable and scalable production"** through **"equipment '
       'upgrades, validation activities, and supplier collaboration"** — with **"audit-ready equipment '
       'records"** as the proof. That is the same chain I have worked my whole career, in another regulated '
       'industry.', after=30)

    lp('**On the transition.** I have read that GN is selling its Hearing business to Amplifon. Ownership '
       'change is when disciplined project work pays for itself, and it does not change the first quarter: '
       'keep the line running, document the equipment, make the next transfer boring.', after=30)

    lp('**On the process.** No photo in this CV, as you ask. You note that **"applications are assessed '
       'continuously"**, that you value **"transferable skills"** and **"practical problem-solving, clear '
       'collaboration, and a continuous-improvement mindset"**, that the team exists to **"deliver quality '
       'outcomes"**, that every applicant gets **"equal consideration for employment"** and that **"your '
       'contribution is appreciated"**. **"We encourage you to apply"** is why this letter is one page of '
       'substance: GN **"brings people closer"** with technology that **"enhances the senses of hearing and '
       'sight"**, and what I can add in Præstø is a production that keeps running while it changes.',
       after=12)

    m.meta('Kind regards', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('**Project manager for equipment and production change in regulated industry** — 37 capital '
           'projects, 25 specialists coordinated, zero critical deviations at handover; company owner with '
           'full P&L, technical purchasing and supplier negotiation since 2023. FAT/SAT, IQ/OQ/PQ, change '
           'control and audit-ready documentation as daily practice. PRINCE2 certified, authorised '
           'maskinmester (LV/MV/HV), B.Tech in technology management. English working language.', after=60)

    m.section('THE LINE — HOW I KEEP A PROCESS STABLE')
    for label, body in [
        ('The variation',
         'Find out why Tuesday differs from Monday before changing anything: fixture, stencil, calibration, '
         'material batch, operator sequence. The cause is upstream of the symptom — it shows up as **yield** '
         'long before it shows up as a complaint.'),
        ('The first article',
         'Every new setup proves itself on one piece with the acceptance criteria agreed in writing before '
         'the run — not after the first scrap bin.'),
        ('The calibration',
         'Instruments have an interval, a certificate and an owner. A calibration that drifts unnoticed is '
         'scrap produced with confidence.'),
        ('The change',
         'Written before it happens: what changes, why, the risk, who agreed, which SOP is updated and who '
         'is trained. A change without that is an incident waiting for a date.'),
        ('The supplier',
         'Price, lead time, service level, spare parts and SOW in one negotiation, with the technical '
         'requirements attached — and a second source qualified where the risk justifies it.'),
        ('The record',
         'The equipment file grows while the work happens: drawings, FAT/SAT, calibration, change notes, '
         'training. Audit-ready is a habit, not a project in the last month.'),
    ]:
        m.bullet(label, body, after=16)

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director', 'ELOHVAC ApS · Copenhagen · May 2023–present',
         '8 employees · full P&L · technical purchasing and delivery',
         [('Technical purchasing and supplier terms',
           'Equipment, materials and subcontractor capacity bought and negotiated with my own margin at '
           'risk: price, lead time, service level and who carries the risk when the date slips.'),
          ('Capacity and change under pressure',
           'Eight employees, 5 electricians and 3 apprentices planned against a moving order book; '
           '**over 40 % productivity gain** measured in estimating and documentation.')]),
        ('Co-owner and CTO / Technical Lead, AI department',
         'Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 (alongside ELOHVAC)',
         '4–10 people · customer solutions from requirement to go-live',
         [('Software and hardware upgrades delivered',
           'Requirements, architecture, integration and go-live of technical applications, including '
           'changes to running customer environments with a documented rollback.'),
          ('Two organisations, one plan',
           'Matrix leadership across two companies with written priority agreements; the company has ceased '
           'trading and the department was closed in order.')]),
        ('Senior Commissioning Engineer / Project Manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · GMP/FDA/EMA',
         [('Equipment projects, validation and handover',
           'Written needs analysis and **URS**-style requirements before purchase; **FAT/SAT**, **IQ/OQ/PQ** '
           'and **change control** in a regulated environment; zero critical deviations at handover on 37 '
           'projects.')]),
        ('Project and Workshop Manager', 'Ventek-Air · Copenhagen · Jan 2022–Nov 2022',
         '14 employees · 11 simultaneous site projects',
         [('Layout, interfaces and sequence',
           'Eleven sites and 14 fitters planned daily; layout, access and sequence decided whether a change '
           'cost an hour or a week.')]),
        ('Operations and Maintenance Manager', 'Biofos (Lynetten) · Copenhagen · Aug 2017–Jan 2022',
         'Wastewater plant in 24/7 operation · SCADA, PLCs, HV switchgear',
         [('Uptime as the deliverable',
           '**Over 40 % lower energy consumption** through measurement, calibration and re-commissioning '
           'while the plant ran 24/7; corrective actions closed with a named owner.')]),
        ('Electromechanical Technician / Production Team Lead', 'ARJ Engineering · Tehran · Dec 2003–Mar 2010',
         '12 technicians · machine shop · machinery and equipment',
         [('Calibration and first-line quality',
           'Fault finding, calibration and repair of industrial electrical and mechanical equipment; root '
           'cause analysis and **corrective action**; training for 12 technicians.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=16)

    m.section('EDUCATION, CERTIFICATION AND AUTHORISATION')
    m.edu('PRINCE2 certified project manager', 'AXELOS / PeopleCert · certification held')
    m.edu('LEAN and Six Sigma — methods in practice', 'DMAIC, 5S, VSM, standard work, FMEA · no certificate')
    m.edu('B.Tech, Technology Management and Mechanical Engineering',
          'Copenhagen School of Marine and Technical Engineering · 2017–2022 · GPA 7.6/12')
    m.edu('Authorised maskinmester (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('Refrigeration and ventilation technology · AMU',
          'Mercantec 2021 · STCW, Danish Maritime Authority 2021')
    m.edu('Electrical and mechanical engineering design, electrical engineering',
          'Tehran Technical University · 2000–2003 · EQF 6')

    m.section('LANGUAGES, IT AND PRACTICAL')
    m.para('English (working language) · Danish (first language) · Persian (mother tongue) · **IT**: **ERP** '
           'and **BOM** handling, **Excel** capacity and cost models, CMMS, documentation and quality systems, '
           '**Python** for own analysis · Måløv · Præstø is about seventy minutes by car, the same as '
           'Kalundborg was for twenty months · category B licence and own car · available after agreement.',
           after=40)

    m.models_table('THE ROLE AS ADVERTISED — WHAT I BRING', ('Requirement', 'Evidence'), [
        ('Relevant technical degree in electrical, electronic, mechanical or manufacturing engineering',
         'Authorised maskinmester (LV/MV/HV) and B.Tech in technology management and mechanical engineering, '
         'with electrical design as the first degree — the technical base the role describes.'),
        ('Production engineering, manufacturing or technical projects in a regulated industry',
         '37 capital projects in GMP/FDA/EMA-regulated pharma production, 11 site projects and a company '
         'delivering technical work under contract — a regulated record, though pharmaceutical.'),
        ('Knowledge of electronics manufacturing: SMD, PCBAs, assemblies, power supplies, electromechanical components',
         'Not SMD production and not a **cleanroom** electronics line. My electronics are power and control — '
         'switchgear, PLC, instrumentation, electromechanical equipment, test and calibration — and I know '
         'what a board survives: **power supply** sizing, the **assembly** sequence, what a **reflow** '
         'profile or an **AOI** alarm does to a waiting shift.'),
        ('Coordinating technical teams and resources across engineering, operations, quality and suppliers',
         '25 specialists coordinated across electrical, mechanical, quality and operations at Novo, 14 '
         'fitters on 11 sites, and suppliers and subcontractors in my own company.'),
        ('Quality frameworks, validation, change management, technical purchasing and supplier negotiations',
         '**IQ/OQ/PQ**, **FAT/SAT**, deviations and **change control** from pharma; technical purchasing and '
         'supplier negotiation with a full P&L since 2023.'),
        ('Knowledge of ISO 13485',
         'Not held. My framework was GMP with FDA/EMA expectations — document control, validation, audits and '
         'traceability — which is the same discipline with a different standard number.'),
        ('Scope and deliver production engineering projects: processes, test environments, line layouts',
         'Projects scoped from a written needs analysis, then delivered to a layout, a test setup and a date: '
         '37 of them, each with acceptance criteria agreed before the equipment arrived.'),
        ('Manage equipment transfers, capacity expansions, hardware and software upgrades',
         'Equipment specified, installed and commissioned on live plants, plus software and hardware '
         'upgrades at Data Power with documented rollback — the transfer done without stopping production, '
         'and **automation** added only where it removes a step that fails.'),
        ('Coordinate manufacturing changes and risk assessments with Operations and Quality',
         'Change assessed with the operations owner and quality before it happens, with the SOP updated and '
         'training done; the aim was always that no shift was surprised.'),
        ('Support automated test equipment and calibration protocols for PCBAs and sub-assemblies',
         'Calibration and test as a discipline from ARJ and from commissioning: intervals, certificates, '
         'first-article checks — but not on PCBAs specifically.'),
        ('Manage technical sourcing for equipment, tooling, production components and test stations',
         'Sourcing from requirement to signed order in my own company: specification, supplier comparison, '
         'negotiation, delivery follow-up and acceptance.'),
        ('Build supplier relationships and negotiate pricing, lead times, service levels and statements of work',
         'Five-term negotiations with my own margin at risk; a supplier who is late on a fixed price is a '
         'loss I have carried personally, not a slide in a review.'),
        ('Validation and documentation: IQ/OQ/PQ, change controls, SOPs, audit-ready equipment records',
         'Documentation written while the work happened, never reconstructed; zero critical deviations at '
         'handover on 37 projects in a plant where auditors arrive unannounced.'),
        ('Connect engineering, operations, quality and suppliers to deliver robust manufacturing solutions',
         'Four-party alignment is the job I have done on every project: the engineer, the shift, the quality '
         'inspector and the supplier each need a different sentence about the same change.'),
        ('Work in Component Manufacturing Engineering within Global Operations',
         'Used to a matrix: local site, central engineering, group quality — the site owns the plant, the '
         'centre owns the standard, which is the pull this role describes.'),
        ('Work closely across Manufacturing Operations, Quality, Supply Chain and external partners',
         'Operations was always my counterpart rather than my customer: the line runs while you change it, '
         'and supply chain is told before, not after.'),
        ('Practical problem-solving, clear collaboration and a continuous-improvement mindset',
         'Fault finding on the floor first, standardisation second, documentation third — with LEAN and Six '
         'Sigma methods (5-why, FMEA, standard work) as the tools rather than the language.'),
        ('Experience from medical devices, automotive or aerospace',
         'Pharmaceutical production rather than medical devices or automotive: same regulatory weight, same '
         'validation and change control, different product and different authority.'),
        ('Full-time role on site in Præstø, Denmark',
         'Måløv to Præstø is about seventy minutes, the same commute as Kalundborg for twenty months; I am '
         'on site by choice, with a car and a category B licence.'),
        ('English working language in an international organisation',
         'English is my working language in documentation, suppliers and international colleagues; I worked '
         'in an English-language project organisation at Novo and in Danish on the floor.'),
        ('CV submitted without a photo',
         'No photo, no birth date and no personal details beyond contact — as you ask, and as it should be '
         'in a process where the work is what is being assessed.'),
        ('Short application possible: CV plus a few sentences of motivation',
         'Took the long route because the interesting part is in the six links; the short version is page '
         'one, and it is three sentences.'),
        ('GN values: bringing people closer, technology that enhances hearing and sight',
         'The product is a person hearing their family again — a better reason to keep a line running than a '
         'KPI, and why the documentation is worth it.'),
    ], widths=(2500, 7846))

    m.section('FIRST 90 DAYS')
    for b in (
        'Weeks 1–6: walk the line with the operators, read a year of change records and open deviations, '
        'learn which equipment has no second source — then take one live project over end to end.',
        'Weeks 7–10: one sourcing case to signature with the five terms written down, and a second-source '
        'recommendation for the component with the worst lead time.',
        'Weeks 11–13: one change delivered the full route — risk assessment, Operations and Quality sign-off, '
        'SOP, training, audit-ready file — so the next one has a template that the floor accepts.'):
        m.bullet('', b, after=16)

    m.section('WHAT I WOULD ASK')
    for b in (
        'Which equipment on the line is single-sourced today, and what would a week of downtime cost?',
        'Which changes are queued for next year, and which of them has no validation resource attached?'):
        m.bullet('', b, after=16)

    m.para('**I would welcome a conversation about the line.** +45 93 99 95 14 · ajlooshahram@gmail.com.',
           after=14)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_GNHearing_TechnicalProjectManager.docx')
    build(out)
    print(out)
