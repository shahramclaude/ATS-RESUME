# -*- coding: utf-8 -*-
"""Evondos Group — Senior Project Manager, PMO (hybrid, Denmark possible).

English posting -> English document. Form (master/FORMKATALOG.md): opening **S**
(the unit: a business case measured in minutes given back, not in euros),
structure **The Gates** (six gates from business case to benefits, each one a
decision with a document), register **The Decision Log**.
Culture file: jd/Evondos_SeniorProjectManager_kultur.txt.
User answers 14.11.2026: PRINCE2 held; organisational change only — no M&A claim.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Senior Project Manager · PMO, cross-functional delivery, regulated projects'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('14 November 2026')
    m.meta('Evondos Group · PMO · Senior Project Manager · hybrid, Denmark')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Senior Project Manager', bold=True, color='1A1A1A')

    def lp(text, after=44):
        return m.para(text, after=after, line=236)

    # ---------------------------------------------------------------- page 1
    lp('**A project at Evondos is not measured in euros. It is measured in minutes a care worker does not '
       'spend counting pills, and in how many people can stay in their own home one month longer.** '
       'You put it in four lines: **"Time for care staff to care, not administer"**. That unit changes how '
       'a PMO behaves: the business case has to name whose time is given back, the steering group has to '
       'see that number rather than a percentage of completion, and somebody has to check it after '
       'handover. **"Give Time Back"** is measurable, and the project office is where it is kept.', after=40)

    lp('You are building a PMO that does not create bureaucracy — **"structure and momentum without '
       'creating unnecessary bureaucracy"** — and you say it plainly: **"Build, don\'t just maintain"**. '
       'That is the version I know how to run. 37 parallel capital projects with a written business case '
       'before a drawing, stage gates with named owners, and documentation written while the work was '
       'done rather than after it. All 37 reached handover with zero critical deviations, because the '
       'gates were decisions and not meetings.', after=40)

    lp('**Six gates. Each is a decision, and each has one document that makes the decision possible.**',
       after=32)

    lp('**The business case.** Whose time, how much of it, and what would make the case false. If nobody '
       'can name the care worker or the municipality whose hours change, it is not a case yet — it is an '
       'ambition with a spreadsheet. At Novo Nordisk every change passed a written needs analysis before '
       'it became a drawing; 37 projects were approved on that basis.', after=28)

    lp('**The plan.** Scope, dependencies and the date on one page, with the owners named. Eleven '
       'simultaneous sites and 14 fitters taught me that the plan is not the Gantt chart; it is the list '
       'of what has to be true for the next step to happen — and who is responsible for each line.',
       after=28)

    lp('**The steering decision.** Two or three options, the trade-off named, one recommendation, and the '
       'consequence of waiting. **"Challenge assumptions constructively"** means bringing the number that '
       'disagrees, in the meeting rather than after it, and then accepting the decision and writing it '
       'down with the date and the owner.', after=28)

    lp('**Implementation across functions.** Business, product, technology, operations, quality and '
       'regulatory do not fail in parallel; they fail at the interfaces. In a GMP environment the quality '
       'and regulatory route was part of the plan from week one — FAT/SAT, IQ/OQ/PQ, documentation and '
       'handover — because a late quality gate does not delay a project, it stops it.', after=28)

    lp('**Handover.** A project is finished when somebody else can run what was built, without my '
       'number. That is why I write documentation *while* the work happens: the test of a handover is '
       'whether an operator who was not in the project can use it on a Monday morning.', after=28)

    lp('**Benefits.** The number after the go-live, measured the same way it was promised. At Lynetten '
       'that discipline produced **over 40 % lower energy consumption** — not from a target, but from '
       'measuring, adjusting set points and re-commissioning until the meter agreed. A PMO that tracks '
       '**"benefits tracking"** to the end is rare, and it is the fastest way to earn the next mandate.',
       after=40)

    lp('**The PMO itself.** **"templates and playbooks"** are only worth something if they stop the same '
       'conversation happening twice. The ones I have built and used were three pages: a business case '
       'template that forces the beneficiary to be named, a decision log that records what was rejected as '
       'well as what was chosen, and a handover checklist that quality and operations both sign.', after=40)

    lp('**Where my record is thinner, stated plainly.** I have not led a post-merger integration, and my '
       'regulatory work is pharmaceutical GMP/FDA/EMA rather than EU MDR for devices. What I have done is '
       'run two organisations on one plan through a wind-down — matrix leadership across two companies, '
       'written priority agreements, specialists reallocated and a department closed in order. The '
       'discipline of an integration is the same: one plan, named owners, a decision log, and honest '
       'reporting to a steering group. The M&A context would be new.', after=40)

    lp('**Why Evondos, in your words.** **"European market leader in medication management"** — 120 '
       'million doses to the right person at the right time, 50,000+ people and 700+ municipalities, '
       'regions and care organisations in eight markets, all resting on **"safe and reliable medication '
       'services"**. That is not a startup story; it is an operating company with a mission. Your CEO says '
       '**"Innovation should always serve a human purpose"** — the freedom to live healthier, more '
       'independent lives — and your careers site says **"Together we are strong"** and promises **"just the '
       'right dose of freedom"**. The sentence that decides it for me is '
       '**"turning ambitious plans into results across countries, functions and organisations"** — the job '
       'I have been doing in one country.', after=40)

    lp('**Practical.** I am based in Måløv, 20 minutes from Evondos\' Copenhagen office, so a Danish '
       'contract needs no relocation and no sponsorship. **PRINCE2 certified**; English is my working '
       'language, Danish my first, Persian my mother tongue. Available after agreement and happy to travel '
       'across the markets.', after=16)

    m.meta('Kind regards', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('**Project and programme manager with 37 capital projects, a full P&L and regulated delivery '
           'behind him** — PRINCE2 certified, authorised maskinmester (LV/MV/HV), B.Tech in technology '
           'management. Stage gates, business cases and handovers in a GMP/FDA environment; 25 '
           'specialists led; two organisations run on one plan; **over 40 % measured** improvement '
           'delivered and documented. Decision log, dependency list, benefits check — on one page.',
           after=64)

    m.section('THE DECISION LOG — HOW I RUN A PROJECT')
    for label, body in [
        ('The decision',
         'Every entry has a date, an owner and the option that was rejected. A project that cannot show '
         'what it decided against cannot explain itself six months later.'),
        ('The dependency',
         'The interface is where projects die: one list, one owner per line, reviewed weekly. Late is a '
         'date, not an opinion.'),
        ('The number',
         'One page for the steering group: scope, date, budget, top three risks, and the decision needed '
         'today. If the number is uncomfortable, it travels first.'),
        ('The escalation',
         'Raised when it can still be solved cheaply — with two options and a recommendation, never with '
         'a problem alone.'),
        ('The handover',
         'Finished means somebody else can run it. Documentation is written while the work happens, and '
         'quality and operations sign the same checklist.'),
        ('The benefit',
         'Checked after go-live, against the business case, and reported to the same people who approved '
         'it. Otherwise nobody learns anything.'),
    ]:
        m.bullet(label, body, after=16)

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director', 'ELOHVAC ApS · Copenhagen · May 2023–present',
         '8 employees · 5 electricians and 3 apprentices · full P&L',
         [('Budget, commitments and delivery',
           'Full **P&L** and **budget** responsibility; quotations, purchasing and delivery dates owned '
           'end to end; hiring, onboarding and performance of eight employees.'),
          ('Measured improvement',
           'AI tools in estimating, documentation and design work: **over 40 % productivity gain**, '
           'measured rather than claimed.')]),
        ('Co-owner and CTO / Technical Lead, AI department',
         'Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 (alongside ELOHVAC)',
         '4–10 people · customer applications · LLM APIs and AI agents',
         [('Two organisations, one plan',
           'Matrix leadership across two companies with written agreements on priority; the company has '
           'ceased trading and the department was closed in order.'),
          ('Delivery from scope to handover',
           'Customer solutions from requirements and **business case** to architecture, integration, '
           'go-live and handover, with documentation the customer could run from.')]),
        ('Senior Commissioning Engineer / Project Manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · GMP/FDA/EMA',
         [('37 projects, stage gates and quality',
           'Written needs analysis before drawing; **FAT/SAT**, **IQ/OQ/PQ** and **validation** in a '
           'regulated environment; zero critical deviations at handover across 37 projects.')]),
        ('Project and Workshop Manager', 'Ventek-Air · Copenhagen · Jan 2022–Nov 2022',
         '14 employees · 11 simultaneous site projects',
         [('Capacity, dependencies and suppliers',
           'Daily capacity plan for 11 sites and 14 fitters; subcontractors and suppliers coordinated so '
           'interfaces did not become delays.')]),
        ('Operations and Maintenance Manager', 'Biofos (Lynetten) · Copenhagen · Aug 2017–Jan 2022',
         'Wastewater plant in 24/7 operation · SCADA, PLCs, HV switchgear',
         [('Continuous improvement with a number',
           '**Over 40 % lower energy consumption** through measurement and re-commissioning; incident and '
           'maintenance management in 24/7 duty.')]),
        ('Electromechanical Technician / Production Team Lead', 'ARJ Engineering · Tehran · Dec 2003–Mar 2010',
         '12 technicians · machine shop · machinery and equipment',
         [('Standards, training and equipment',
           'Fault finding, calibration and repair; purchasing and maintenance of equipment; training and '
           'follow-up for 12 technicians.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=16)

    m.section('EDUCATION, CERTIFICATION AND AUTHORISATION')
    m.edu('PRINCE2 certified project manager', 'AXELOS / PeopleCert · certification held')
    m.edu('B.Tech, Technology Management and Mechanical Engineering',
          'Copenhagen School of Marine and Technical Engineering · 2017–2022 · GPA 7.6/12')
    m.edu('Authorised maskinmester (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('Refrigeration and ventilation technology · AMU',
          'Mercantec 2021 · STCW, Danish Maritime Authority 2021')
    m.edu('Electrical and mechanical engineering design, electrical engineering',
          'Tehran Technical University · 2000–2003 · EQF 6')

    m.section('LANGUAGES, IT AND PRACTICAL')
    m.para('English (working language) · Danish (first language) · Persian (mother tongue) · **IT**: '
           'project and portfolio tools, **Excel** models for business cases and benefits, **ERP**, '
           'documentation and quality systems, **Python** for own analysis · Based in Måløv, 20 minutes '
           'from Evondos Copenhagen · Hybrid and travel across markets · Available after agreement.',
           after=44)

    m.models_table('THE ROLE AS ADVERTISED — WHAT I BRING', ('Requirement', 'Evidence'), [
        ('Lead complex cross-functional projects from scope and business case to handover and benefits',
         '37 capital projects from written needs analysis to handover, and a benefits number checked '
         'afterwards: over 40 % lower energy consumption at Lynetten, measured.'),
        ('Lead post-merger and new market entry integration projects across functions and countries',
         'Led two organisations on one plan through a wind-down, with written priority agreements and a '
         'department closed in order. Not an acquisition — but the same machinery.'),
        ('Own project plans, budgets, risks, dependencies and governance',
         'Plan, **budget** and **risk** list owned on 37 projects and in my own company; every '
         '**milestone** and dependency on one list, with an owner per line, reviewed weekly.'),
        ('Ensure stakeholders have a clear view of progress',
         'One page per project for the **steering group**: scope, date, budget, top three risks and the '
         'decision needed now. Bad news travels first, not last.'),
        ('Turn complex information into clear recommendations for steering groups',
         'Recommendations arrive as two or three options with a named trade-off and a price, so the '
         'decision can be taken in the meeting instead of deferred to the next one.'),
        ('Challenge assumptions constructively',
         'I bring the number that disagrees — the alternative that is cheaper, the date that cannot hold '
         '— before the decision, and then commit to the decision that is taken.'),
        ('Help drive timely decisions',
         'Every decision gets a date and an owner in the **decision log**, including what was rejected; '
         'the log is what the next steering group reads first.'),
        ('Build alignment across business, product, technology, operations, quality and regulatory',
         'Twenty years of interfaces: GMP quality and regulatory at Novo, suppliers at Ventek-Air, '
         'customers and authorities in my own company — aligned in writing, not in corridors.'),
        ('Strengthen PMO ways of working: lessons learned into processes, templates and playbooks',
         'Built and used three templates — business case, **decision log**, handover checklist — each '
         'written after a lesson, not before one, and short enough to be used.'),
        ('Turn strategic priorities into clear plans, well-informed decisions and measurable results',
         'Strategy became a plan and then a number: capacity plans for 11 sites, stage gates for 37 '
         'projects, and a measured 40 % energy reduction instead of a target.'),
        ('A strong track record of complex cross-functional projects, including budgets',
         '37 parallel projects with budgets under my control, 25 specialists coordinated, and full '
         '**P&L** in my own company since 2023.'),
        ('Hands-on experience of M&A, post-merger integration or similarly complex organisational change',
         'Organisational change: two parallel organisations run on one plan with written priorities, and '
         'a company wound down and a department closed without losing people. No post-merger integration '
         'led.'),
        ('Experience in medical devices, pharmaceuticals or another regulated industry',
         'Five years in **GMP/FDA/EMA**-regulated pharmaceutical projects at Novo Nordisk, with '
         '**validation**, audits, **compliance** and documentation as daily conditions rather than a '
         'phase.'),
        ('Practical understanding of how quality and regulatory requirements influence processes',
         'Quality was a gate, not a department: **IQ/OQ/PQ** before handover, deviations closed with a '
         'named owner, and a plan that assumed a late quality gate would stop the project.'),
        ('Strong communication and influencing skills, confidence to challenge constructively',
         'Same message at three altitudes — engineers get the constraint, product the trade-off, '
         'leadership the number — in Danish and English, written and in the room.'),
        ('Communicate effectively with senior leaders and other stakeholders',
         'Reported to directors and steering groups for years, including the conversations where the '
         'message was unwelcome and the alternative had to be presented the same day.'),
        ('A recognised project management certification, such as PMP, PRINCE2 or IPMA',
         '**PRINCE2 certified**, applied in practice on 37 capital projects and in my own contracting '
         'business: product-based planning and stage boundaries, not a certificate on a wall.'),
        ('A driven, pragmatic approach: structure and momentum without unnecessary bureaucracy',
         '**Structure without** administration for its own sake: three templates, one page per project, '
         'one weekly forum — everything else was removed if it did not change a decision.'),
        ('Lean or Six Sigma certification',
         'No certificate. The practice is there — measurement, standardisation and waste removal — and '
         'it produced over 40 % lower energy consumption and 40 % productivity gain.'),
        ('Experience in market entry, product or service launches',
         'Launches at project level: 11 sites and 37 handovers delivered to the agreed date and quality, '
         'and customer solutions taken from scope to go-live. Not a market entry.'),
        ('Experience with EU MDR',
         'Not my area: my regulatory record is pharmaceutical GMP/FDA/EMA and medical-technical projects '
         'in a hospital context, not device regulation under EU MDR.'),
        ('Experience building and developing a PMO function',
         'Built the toolkit rather than the department: stage gates, business case, decision log and '
         'handover checklist, used across 37 projects and in my own company.'),
        ('Work closely with teams across the business and with senior leadership',
         'Worked on the floor and in the steering room on the same day for twenty years — from fitters '
         'and specialists to directors and authorities.'),
        ('Report to the Head of PMO and own strategic projects at different stages',
         'Took projects at every stage: from an unwritten need to a stalled site to a handover that had '
         'to happen on a date that had already been promised.'),
    ], widths=(2500, 7846))

    m.section('FIRST 90 DAYS')
    for b in (
        'Weeks 1–2: read the live project list, the last three steering papers and the post-mortems; '
        'meet the owners in business, product, technology, operations, quality and regulatory. Change '
        'nothing.',
        'Weeks 3–6: one page per strategic project — scope, date, budget, top three risks, decision '
        'needed — so the Head of PMO and the steering group see the portfolio the same way.',
        'Months 2–3: the decision log introduced on two projects, with what was rejected written down; '
        'the handover checklist tested on the next one that finishes.',
        'Month 3: benefits check on one delivered project, reported to the people who approved it — and '
        'one template retired, because a PMO that only adds process becomes the bureaucracy it was meant '
        'to prevent.'):
        m.bullet('', b, after=16)

    m.section('WHAT I WOULD ASK')
    for b in (
        'Which integrations are running now, and what is the hard part — systems, people, or the '
        'commercial case?',
        'Where does the PMO sit today: does it own delivery, or advise the business on it?',
        'How is a benefit proven at Evondos — who checks the minutes given back, and when?'):
        m.bullet('', b, after=16)

    m.para('**I would welcome a conversation about the portfolio and the integrations ahead.** Contact: '
           '+45 93 99 95 14 · ajlooshahram@gmail.com.', after=20)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Evondos_SeniorProjectManager.docx')
    build(out)
    print(out)
