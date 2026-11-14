# -*- coding: utf-8 -*-
"""Spirii — Engineering Manager (Copenhagen, Nørrebro).

English posting -> English document. Form (master/FORMKATALOG.md): opening **P**
(the review comment: an agent can open the pull request, it cannot sit in the
review and answer for it), structure **Five phrases, taken literally** (five of
their own sentences, each with what it requires on a Tuesday), register
**The Review** (diff, test, rollback, page, retro, person).
Culture file: jd/Spirii_EngineeringManager_kultur.txt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Engineering Manager · teams, delivery and agent-written code'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('14 November 2026')
    m.meta('Spirii · Digital Development · Engineering Manager · Copenhagen · via thehub.io')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Engineering Manager', bold=True, color='1A1A1A')

    def lp(text, after=60):
        return m.para(text, after=after, line=236)

    # ---------------------------------------------------------------- page 1
    lp('**An agent can open the pull request. It cannot sit in the review and answer for it.** That is '
       'the line your description draws when it makes agentic development the way Spirii builds '
       'software: the writing moves towards the agents, and the accountability moves towards the person '
       'who approves what was written. A team does not become **"a high-performing team"** because it '
       'ships faster. It becomes one because somebody can say, on a Thursday, which change should not '
       'have been merged — and why.', after=56)

    lp('**"You own the people, the health of the team and the soundness of its engineering"**, you '
       'write — and that you **"do this through others"**, with Tech Leads and Senior Engineers carrying '
       'the technical decisions. I have run units that way. At Lynetten the people who owned the PLCs '
       'and the SCADA system knew more about them than I ever will; my part was the rota, the risk, the '
       'standard and the escalation. That is the **"a listen, learn, and lead culture"** in practice, '
       'and it only works if the manager is the first to change his mind in public.', after=56)

    lp('**Five phrases from your description, taken literally** — each a different job, each with its '
       'own way of going wrong.', after=44)

    lp('**"You own the people."** The full cycle, including the parts managers skip: hiring for the gap '
       'rather than a replica of the last person; onboarding that produces a first-week win; '
       'one-to-ones that are not status meetings; reviews with no surprises, because the feedback came '
       'in March. And **"handling underperformance early and fairly"** — named in week three, in '
       'writing, with the standard, the gap and the date. At ELOHVAC I hired five electricians and '
       'three apprentices; at Novo Nordisk the same cycle ran for 25 specialists across 37 projects.', after=32)

    lp('**"The health of the team."** A team works **"at a sustainable pace"** when the schedule is '
       'designed for it: a rota that survives holidays, a backlog that can be finished, an on-call list '
       'with a named second line, and no heroics used as a plan. Five years of 24/7 duty taught me that '
       'the crew which stays is never the one that works the most nights.', after=32)

    lp('**"The soundness of its engineering."** Quality is a standard, not a mood, and **"quality '
       'stays high"** only if somebody signs. Architecture, security, operational readiness, '
       'observability and technical debt are the manager’s signature even when the design belongs to '
       'the Tech Lead. What ships must be **"tested, observable and ready to run in production"** and '
       '**"incidents lead to real learning"**: 37 capital projects reached handover with zero critical '
       'deviations, because the documentation was written while the work was done.', after=32)

    lp('**"Moving beyond individual experiments to shared practice."** This is the phrase I have lived. '
       'At Data Power, AI-assisted development was the process and not a perk: generation, review and '
       'test inside the delivery flow, with written rules for when AI output is accepted, so two '
       'reviewers of the same generated change reached the same answer. The practices that make agents '
       'useful are unglamorous: work specified by acceptance criteria before anyone prompts, changes '
       'small enough to hold in the head, a test that fails first, and a review that asks what breaks '
       'rather than who wrote it. What a team learns that way is worth handing on, which is why '
       '**"share what you learn with other teams"** is a habit and not a quarterly review.', after=32)

    lp('**"Delivery flow, reliability, and team health"** — and not gut feeling. **"Turn priorities '
       'into clear commitments, make trade-offs visible, and protect the team so committed work gets '
       'finished"** is a discipline with three artefacts: one page per team showing what enters, what '
       'leaves and how long it takes; incidents counted by cause rather than by count; load shown as '
       'overtime and on-call rather than as sentiment. When a commitment changed, it changed in writing '
       'that week: what slipped, why, and what we stopped instead.', after=56)

    lp('**What your description does not ask for, and an EV platform needs.** A charger is electrical '
       'infrastructure before it is software. As authorised maskinmester I read the installation, the '
       'protection, the meter and the grid connection behind a charging point — and I know what the '
       'hardware can and cannot report. When a session fails, "is it the charger or the platform?" is '
       'answered faster by someone who has stood at the cabinet — not a substitute for a software '
       'background, but the other half of your domain.', after=32)

    lp('**Where my record is thinner, stated plainly.** My formation is electrical and control '
       'systems; the software I have owned is delivery — architecture, data model, integration, go-live '
       '— and AI-assisted development as standard practice in a department of four to ten. Distributed '
       'systems at your scale, AWS and containers: that vocabulary I would build at the pace of the '
       'engineers who already speak it.', after=56)

    lp('**Why Spirii, in your own words.** Founded in 2019, **22+ markets**, and part of Edenred since '
       '2024 — which turns a Danish platform into one that has to be right about money in forty-five '
       'countries. Your people describe the culture as **"kind, relaxed, and hectic"**; your standard '
       'is **"careful planning, thorough testing"**, with a stated bias towards **"market-leading over '
       'market-first"**; your principle is **"humans behind the wheel first"**, and the promise is '
       '**"powerful connections"** between chargers, cars, drivers and money.', after=56)

    lp('**Practical.** I live in Måløv and reach Nørrebro in under half an hour, so this is a permanent '
       'Copenhagen role for me rather than a commute to be negotiated. Danish first language, English '
       'working language, Persian mother tongue. Available now; references on request.', after=24)

    m.meta('Kind regards', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('**Engineering leader with a P&L, a people cycle and two years of AI-assisted development '
           'behind him** — authorised maskinmester (LV/MV/HV), B.Tech in technology management and '
           'mechanical engineering. Co-owner and CTO of an AI department of 4–10, where agentic '
           'development was the working method; eight employees, five of them hired by me, at ELOHVAC; '
           '25 specialists across **37 capital projects** at Novo Nordisk; five years of 24/7 duty '
           'with SCADA and PLC estates. Ledger, rota, review and roadmap — on one page.', after=70)

    m.section('THE REVIEW — HOW I READ A CHANGE')
    for label, body in [
        ('The diff',
         'Small, one purpose, written so a reviewer can hold it in the head. Size is a management '
         'variable, not a matter of taste.'),
        ('The test',
         'A test that fails first is the only evidence that it tests anything. **Automated testing** '
         'as a rule of the flow, never a phase at the end.'),
        ('The rollback',
         'Every change ships with its undo: a written procedure on a 24/7 plant, a **deployment** '
         'that goes back on a **platform** — both rehearsed.'),
        ('The page',
         '**Observability**: what pages a human, what waits until Monday, which alert is noise. If '
         'nobody acts on it, it is not **monitoring**.'),
        ('The retro',
         'An **incident** ends in a change — test, guardrail, runbook or design — tracked to closure. '
         'Otherwise it was an outage with minutes taken.'),
        ('The person',
         'Every review is feedback to someone: specific, timely, about the work. That is how a senior '
         'engineer becomes a **tech lead**.'),
    ]:
        m.bullet(label, body, after=16)

    m.section('EXPERIENCE')
    jobs = [
        ('Co-owner and CTO / Technical Lead, AI department',
         'Data Power Consultant ApS · Copenhagen · 2024–Nov 2026 (alongside ELOHVAC)',
         '4–10 engineers · customer applications · LLM APIs and AI agents',
         [('Architecture, data model and go-live',
           '**Cloud-based solutions** end to end: requirements, architecture, data model, **API** '
           'integration, **deployment** and handover, so the customer could run what we built.'),
          ('Agentic development as shared practice',
           '**AI-assisted development** as the standard way of working: code generation, **code '
           'review** and testing under written rules for when AI output is accepted.'),
          ('LLM APIs and AI agents in production',
           'Customer solutions on **LLM** APIs and agents, from process mapping to a running service; '
           'AI also in management reporting and **KPI** analysis.'),
          ('Matrix leadership through a wind-down',
           'Two organisations, one plan and written agreements on priority; the company has ceased '
           'trading, and the department closed in order.')]),
        ('Owner / Technical Director',
         'ELOHVAC ApS · Copenhagen · May 2023–present',
         '8 employees · 5 electricians and 3 apprentices · full P&L',
         [('The people cycle, with the paperwork',
           'Hiring, **onboarding**, one-to-ones, apprenticeship **feedback** and **performance '
           'review**s; full **P&L**, **budget** and customer commitments.'),
          ('AI in daily operations',
           'AI tools in estimating, documentation and design work: **over 40 % productivity gain**, '
           'measured rather than claimed.')]),
        ('Senior Commissioning Engineer / Project Manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · GMP/FDA/EMA',
         [('Delivery, predictability and handover',
           '**FAT/SAT**, **IQ/OQ/PQ** and handover across 37 projects; zero critical deviations, and '
           'documentation written while the work was done.')]),
        ('Project and Workshop Manager',
         'Ventek-Air · Copenhagen · Jan 2022–Nov 2022',
         '14 employees · 11 simultaneous site projects',
         [('Capacity and interfaces',
           'Daily capacity plan for 11 sites and 14 fitters; subcontractors and suppliers coordinated '
           'so interfaces did not become delays.')]),
        ('Operations and Maintenance Manager',
         'Biofos (Lynetten) · Copenhagen · Aug 2017–Jan 2022',
         'Wastewater plant in 24/7 operation · SCADA, PLCs, HV switchgear',
         [('24/7 operation, incidents and energy',
           'On-call duty and **incident management** around the clock; root-cause follow-up and '
           'planned maintenance; **over 40 % lower energy consumption** through measurement and '
           're-commissioning.')]),
        ('Electromechanical Technician / Production Team Lead',
         'ARJ Engineering · Tehran · Dec 2003–Mar 2010',
         '12 technicians · machine shop · machinery and equipment',
         [('Assets, maintenance and training',
           'Fault finding, calibration and repair of machines; purchasing and maintenance of '
           'equipment; training and follow-up for 12 technicians.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=16)

    m.section('EDUCATION AND AUTHORISATION')
    m.edu('B.Tech, Technology Management and Mechanical Engineering',
          'Copenhagen School of Marine and Technical Engineering · 2017–2022 · GPA 7.6/12')
    m.edu('Authorised maskinmester (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('Refrigeration and ventilation technology · AMU',
          'Mercantec 2021 · STCW, Danish Maritime Authority 2021')
    m.edu('Electrical and mechanical engineering design, electrical engineering',
          'Tehran Technical University · 2000–2003 · EQF 6')

    m.section('LANGUAGES, IT AND PRACTICAL')
    m.para('English (working language) · Danish (first language) · Persian (mother tongue) · **IT**: '
           '**LLM** APIs and **AI agents**, **AI-assisted development** with review standards, '
           '**Python** for own tools, **API** integration and data models, version control and code '
           'review workflows, **SCADA** and **PLC** estates, **observability** and log analysis, '
           '**Excel** models, **ERP** · Driving licence B and own car · Available now.', after=50)

    m.models_table('THE ROLE AS ADVERTISED — WHAT I BRING', ('Requirement', 'Evidence'), [
        ('Lead 1–2 engineering teams of 6–12 engineers and make them a high-performing team',
         'Teams of four to ten engineers, 25 specialists, 14 fitters and a company of eight led — one page per team with commitments, status and risk.'),
        ('Own the people, the health of the team and the soundness of its engineering',
         'Three ledgers at once — people, team health (load, on-call, pace) and engineering quality (decisions, standards, technical debt) — reviewed monthly.'),
        ('Do it through others: Tech Leads and Senior Engineers guide the technical work',
         'The technical call stayed with the specialist: PLC owners at Lynetten, discipline engineers at Novo, the senior electrician on site. I held standard, date, risk.'),
        ('Good decisions get made, quality stays high and the team keeps getting better',
         'Decisions recorded with reason, owner and date — what we chose, what we rejected, what would change our mind — so nobody reopens it a year later.'),
        ('Work closely with a Product Manager and a Designer on delivery',
         'Delivery planned with whoever owns scope: across 37 capital projects, design, process and quality each held their part, joined by a weekly written status.'),
        ('Full people cycle: hiring, onboarding, one-to-ones, feedback, career development, reviews',
         'Five electricians and three apprentices hired at ELOHVAC, onboarding written, one-to-ones and apprenticeship reviews run; same cycle for 4–10 engineers.'),
        ('Handling underperformance early and fairly',
         'Named in week three, not in the exit interview: the standard, the gap, what changes and by when, in writing, with support attached to it.'),
        ('A team that trusts each other, takes ownership and works at a sustainable pace',
         'A rota that survives holidays, a backlog that can be finished and no heroics as a plan: five years of 24/7 duty taught me pace is scheduled, not hoped for.'),
        ('Help engineers grow, including senior engineers stepping into technical leadership',
         'Senior people given their own decisions and meetings, with the authority written down: discipline leads ran the reviews at Novo, the senior ran the site.'),
        ('Accountable for delivery, predictability and quality, and how it improves over time',
         'Predictability as promised date against handover date, quality as deviations at handover: 37 projects, zero critical deviations, compared quarter on quarter.'),
        ('Define with Product what good looks like and track delivery flow, reliability, team health',
         'Defined “done” with the scope owners, then tracked delivery flow, reliability by cause and team health as overtime and on-call — one page per team.'),
        ('Turn priorities into clear commitments, make trade-offs visible, protect the team',
         'Commitments written with date and scope; every change shown as a trade-off — what slipped, why, what we stopped instead — so promised work got finished.'),
        ('Agentic development every day, moving beyond individual experiments to shared practice',
         'At Data Power agentic development was the process, not a trial: generation, review and test inside the flow, rules written down so practice was shared.'),
        ('Adapt how work flows as agents take on more of the building',
         'Changed how work was specified (acceptance criteria before the prompt), reviewed (small, one purpose) and assured (a failing test before the change was accepted).'),
        ('Shared practices for quality, security and data handling — accountable for what ships',
         'Written rules for what an agent may see, what a human must review and what must pass before merge — and I signed for what shipped, generated or not.'),
        ('Bring your team’s needs across engineering, test tools and share what you learn',
         'Ran the same pilot on two workstreams before standardising, kept a one-page note of what worked and handed it to the other team before it became policy.'),
        ('Quality of engineering decisions: architecture, security, readiness, observability, debt',
         'Accountable for all five even where the design was someone else’s: what breaks, who is paged, what we owe in two years — asked before the merge.'),
        ('What ships is tested, observable and ready for production; incidents lead to real learning',
         'That was the gate on every customer handover; each incident ended in a guardrail, a test, a runbook or a design change, tracked to closure with an owner.'),
        ('Work with other Engineering Managers and Tech Leads to keep platform and practice coherent',
         'One standard across parallel workstreams: a shared handover checklist, one definition of done, and a monthly forum where the leads compared decisions.'),
        ('Partner with Product, Design, other departments and external consultants',
         'Twenty years of stakeholder management in cross-functional settings — consultants at Novo, suppliers at Ventek-Air, customers in my own company, authorities.'),
        ('Communicate clearly and early about progress, risks and trade-offs',
         'A weekly one-page status: what moved, what did not, what is at risk, what I need. Bad news travels first, or it travels last.'),
        ('Care about people and build teams that grow, thrive and deliver',
         'Three apprentices and five electricians hired and trained, specialists left in charge of their expertise; the team delivers when the manager is away.'),
        ('High bar for quality, ownership of results, excited about AI as the new way to build',
         'The bar shows in what I refused to hand over; results carry numbers. AI in daily use since 2024 — AI agents, LLM APIs and AI-assisted development.'),
        ('Technical enough to challenge a design, read an incident and spot risk',
         'Reads the architecture, the log and the incident timeline: five years of SCADA and PLC estates, plus API and data-model reviews in the AI department.'),
        ('Communicate clearly with engineers, product people and leadership alike',
         'Same message at three altitudes: engineers get the constraint, product the trade-off, leadership the number — Danish and English, written and in the room.'),
        ('Development of digital cloud-based solutions in an agile start-up environment',
         'Customer applications end to end in a small company — requirements, architecture, data model, API integration, deployment — short cycles, scope moving weekly.'),
        ('Responsibility for leading a team of developers',
         'A department of 4–10 engineers led: standards set, their work in code review, hiring, one-to-ones, technical direction and delivery — for two years.'),
        ('Relevant technical graduate degree at minimum bachelor level (engineer)',
         'B.Tech in technology management and mechanical engineering, GPA 7.6/12, plus authorised maskinmester (LV/MV/HV) — a technical degree, applied engineering.'),
        ('3+ years as an Engineering Manager with direct reports, incl. hiring, coaching, performance',
         'Direct reports since 2023 at ELOHVAC (eight, five hired by me) and 2024–Nov 2026 at Data Power (4–10): hiring, coaching, feedback, performance reviews.'),
        ('Background as a software engineer (backend or full-stack) building cloud-based solutions',
         'My formation is electrical and control systems; the software I have owned is delivery — architecture, data model, integration, go-live — and AI-assisted development.'),
        ('Distributed systems — microservices and APIs — and running them reliably in production',
         'Worked where systems fail: API integrations to customer platforms, data models that had to hold, services that had to stay up, an estate where one dead node stopped output.'),
        ('Improving engineering practices: automated testing, CI/CD, observability, incident management',
         'Practices changed in the order that pays: a failing test first, one deployment path with a rollback, alerts that page a human, incidents reviewed within the week.'),
        ('Familiarity with DORA metrics or similar ways of measuring delivery',
         'Delivery measured with what the systems could count: lead time from agreement to go-live, deployment frequency, change failures, time to restore — DORA’s four.'),
        ('Making senior engineers and tech leads more effective rather than doing their work',
         'The lead owned the design, the meeting and the decision; I owned the standard and the consequence. Where I wanted the keyboard, the answer was a review.'),
        ('Leading a team’s adoption of AI-assisted or agentic development, changing practices',
         'Adoption led from individual prompt experiments to shared rules for reviewing generated code, with a department working that way daily for two years.'),
        ('Experience with AWS and containerised workloads',
         'Hosting and containers were run by the engineers who owned them; my decisions were the deployment ones — what goes live, when, and how it comes back.'),
        ('Experience from eMobility products',
         'Charging is electrical infrastructure before software: as authorised maskinmester I read installation, protection, meter, grid connection and what the hardware reports.'),
        ('Leading a team through organisational change',
         'Led through the wind-down of a company and the closing of a department: people told early, work redistributed in writing, everyone leaving with a reference.'),
        ('Fluent English, written and spoken',
         'Working language for two decades: documentation, customer handovers, supplier negotiations and technical reviews. Danish first language, Persian mother tongue.'),
    ], widths=(2500, 7846))

    m.section('FIRST 90 DAYS')
    for b in (
        'Weeks 1–2: sit in the stand-ups and reviews, read the last ten merged changes and the last '
        'ten incidents, ask every engineer what slows them down. Change nothing yet.',
        'Weeks 3–6: one page per team with delivery flow, reliability and team health as a baseline '
        'everybody recognises; the people cycle audited, every engineer with a next step and a date.',
        'Months 2–3: agentic practice written as rules, not preferences — what is specified, what a '
        'human reviews, what must pass before merge — piloted with two seniors, then the team.',
        'Month 3: next quarter’s commitments agreed with Product and Design, with trade-offs and the '
        'on-call and overtime budget in the same document.'):
        m.bullet('', b, after=16)

    m.section('WHAT I WOULD ASK')
    for b in (
        'Where does agentic development stand today — individual experiments or shared practice — and '
        'what is actually blocking the move?',
        'What does "something went wrong" look like in the platform, and who is paged when it does?',
        'What has already been tried on delivery flow and team health, and why did it not stick?',
        'Which of the two teams is furthest from where you want the practice to be, and who inside it '
        'already knows the answer?'):
        m.bullet('', b, after=16)

    m.para('**I would welcome the chance to meet the teams in Nørrebro.** Two innovation days a month, '
           'a pension at 11 % and 32 days of holiday say you intend people to stay; the job is to make '
           'that possible while shipping. Contact: +45 93 99 95 14 · ajlooshahram@gmail.com.', after=24)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Spirii_EngineeringManager.docx')
    build(out)
    print(out)
