# -*- coding: utf-8 -*-
"""Head of Engineering — Enity, Køge (engelsk opslag -> en-GB dokument).

4 pages in master design: letter p1, CV p2-3, requirement matrix p4.
Contact: Brendan Puli, brpu@enity.io -> "Dear Brendan Puli,". Apply through
LinkedIn; applications reviewed on an ongoing basis. Hybrid: 3 days at the Køge
office, 2 days from home.

BRUGERSVAR 26.11 (bindende): (1) Stack (TypeScript/Node.js/PostgreSQL/AWS) =
AI-drevet udvikler, ikke klassisk software-engineer -> ærlig men selvsikker
position ("comparable technologies", AI-native practice). (2) AI-afdelingen
(Data Power) bygger BÅDE softwareprodukter OG AI-værktøjer -> må nævnes begge.
(3) Køge 3 dage/uge = fint fra Måløv (~35-45 min) -> bekræft konkret.

ÆRLIG PROFIL: "background as a software engineer" er nyt og AI-native (Claude-
kodning dagligt, kritisk review af alt output); teknisk dømmekraft 20+ år fra
komplekse fysiske systemer. IoT/sensorer/gateways/BMS/SCADA/PLC = reel ekstra-
pointserfaring. Platform-modernisering skrives ærligt (adjacent, ikke påstået).

STILVALG (style_guard godkendt, 3/3 skift mod #436 Vestas):
  register    = Hands-on engineering leadership (architecture, people, outcomes)
  åbningsgreb = BM (de to verdener: koden i skyen og målerne i bygningerne)
  struktur    = Direction, organisation, outcomes (30/60/90 = the direction ·
                the organisation · the outcomes)

MASTER-REGLER (engelsk): "Authorised electrical engineer (LV/MV/HV)". BANNED:
"proven track record", "demonstrated ability" citeres aldrig (JD'ens "A proven
ability..." parafraseres i rk5-label). Ingen em dash. Sammentrækninger BINDENDE.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Enity · Head of Engineering, Køge'
BANNER_RESUME = 'Engineering leadership · architecture · AI-native · people · outcomes'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('26 November 2026')
    m.meta('Enity · Køge · AI-native Energy Intelligence Platform')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Head of Engineering, Køge',
           bold=True, color='1A1A1A')
    m.para('Dear Brendan Puli,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- page 1
    lp('An energy platform lives in two worlds: the code in the cloud and the meters '
       'in the basements. When 90,000+ electricity, heat, water and gas meters across '
       '20,000+ buildings feed the Energy Management System (EMS), architecture stops being an abstract '
       'exercise. It\u2019s what decides whether the numbers turn energy data into '
       'insights, actions and measurable savings, or just pile up. Leading '
       'engineering at that intersection is the job I want.')

    lp('Enity has done this for more than 25 years, with customers like Carlsberg, '
       'Coop, Jyske Bank and Grundfos and a solid business, "backed by our owner, '
       'OK", as you write. The next chapter, evolving into an AI-native Energy '
       'Intelligence Platform that doesn\u2019t just show what is happening but helps '
       'customers understand why and recommends what to do next, is exactly the kind '
       'of shift I work in. I '
       'lead an AI department today where we build both software products and AI '
       'tools, and I code with AI every day, Claude included, judging every output '
       'critically.')

    lp('The role is hands-on in the right way: stay close to the code, read pull '
       'requests, dig into a production problem alongside the team. A team of about '
       '12 developers will get a leader whose technical judgement they can trust. '
       'My software practice is AI-native and recent; the judgement behind it is '
       'twenty years old, from systems where wrong decisions cost real money. '
       'TypeScript, PostgreSQL and AWS sit at the core of your platform, and I '
       'bring comparable technologies plus the architectural judgement to know '
       'what to keep, simplify, modernise or replace.')

    lp('Setting the technical direction and simplifying the architecture is work I '
       'relish: paying down technical debt while services keep running, and making '
       'pragmatic technology decisions instead of elegant ones. Building a '
       'high-performing engineering organisation is the other half, and I\u2019ve led '
       'and developed people since 2003, from apprentices to senior specialists, '
       'so responsibility and decision-making can increasingly be distributed. '
       'Clear plans, automated testing, CI/CD, code reviews and operational '
       'ownership are the machinery; meaningful measures of quality and delivery '
       'tell us it works.')

    lp('Engineering grounded in real customer problems is not new to me: I\u2019ve '
       'sold, delivered and answered for projects to customers, and the physical '
       'side of your stack is my home ground. Meters, sensors, gateways, utility '
       'providers and building-management systems are what I grew up with in '
       'critical utilities, where software, data and physical infrastructure have '
       'to work as one. Curiosity about AI and how it will transform software '
       'products and engineering itself is not a box I tick; it is my working '
       'week. IoT, connected devices, telemetry, time-series data and '
       'hardware/software integrations all sit in that same bridge, and '
       'engineering priorities here should serve customer and business value, '
       'working closely with Commercial Growth, Customer Success and the energy '
       'experts.')

    lp('Why Enity: measurable impact on energy and sustainability, real influence '
       'over architecture and engineering culture, and an established company '
       'entering an ambitious chapter. Three days together in the Køge office '
       'works well for me; based in Måløv, 35-45 minutes away, the '
       'hybrid setup suits how I lead. I\u2019d like to talk before the LinkedIn '
       'application goes in. And yes, the sixth holiday week is a nice touch.',
       after=44)

    m.para('Kind regards', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- page 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFILE')
    m.para('Engineering leader with an AI-native development practice and 20+ years '
           'of technical leadership across software products, AI tools and complex '
           'physical-digital systems. I run the AI department at Data Power (4-10 '
           'specialists), building both software products and AI tools, and I code '
           'with AI daily, Claude included, judging every output critically. '
           'Architecture judgement from systems where the meters and machines are '
           'real; people leadership since 2003. I am applying because the step '
           'from energy management software to an AI-native Energy Intelligence '
           'Platform is exactly where I want to lead.', after=32)

    m.section('EXPERIENCE')
    jobs = [
        ('CTO, AI department / Authorised Electrical Engineer (LV/MV/HV)',
         'Data Power Consultant ApS · Copenhagen · 2024 – present (from Nov. 2026 also '
         'ELOHVAC\u2019s electrical activities)',
         'AI department, 4-10 people · software products and AI tools · electrical '
         'service and contracting',
         [('Software and AI leadership', 'The AI department designed and built '
           'software products and AI tools from 4 to 10 specialists. AI-native '
           'development is the daily workflow, Claude and comparable tools used in '
           'coding and analysis with critical judgement of every output. Technical '
           'direction, code reviews and delivery follow-through run through me.')]),
        ('Owner / Technical Director / Authorised Electrical Engineer (LV/MV/HV)',
         'ELOHVAC ApS · Copenhagen · May 2023 – Nov. 2026 (company closed)',
         'Business customers · electrical, ventilation and climate · contracting · '
         'full P&L · service agreements',
         [('Customers and outcomes', 'Customer problems translated into technical '
           'plans and measurable outcomes, service agreements kept running while '
           'the work underneath changed, and technology choices justified on '
           'business value. Full P&L responsibility sharpened every trade-off.'),
          ('People and delivery', '5 electricians and 3 apprentices developed '
           'towards more responsibility, subcontractors held to agreements, and '
           'delivery measured weekly on quality and progress.')]),
        ('Senior Commissioning Engineer / Project Manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · Nov. 2022 – Jul. 2024',
         '37 CAPEX projects, DKK 2-10 million each · 25 specialists · GMP/FDA/EMA',
         [('Complex systems, clear ownership', '37 projects across the full life '
           'cycle with zero critical findings at handover. Technical ownership '
           'across engineering, procurement and operations, documentation that '
           'withstood audit, and 25 specialists aligned on architecture-level '
           'decisions.')]),
        ('Project & Workshop Manager',
         'Ventek-Air · Copenhagen · Jan. 2022 – Nov. 2022',
         '11 concurrent ventilation projects · 14 people · subcontractors',
         [('Execution and delivery', '11 concurrent projects planned, prioritised '
           'and released on schedule, with external integrators coordinated like '
           'dependencies in a release train. Trade-offs made explicit, and '
           'delivery performance tracked openly.')]),
        ('Maintenance & Operations Manager / Workshop Technician',
         'Biofos (Lynetten) · Copenhagen · Aug. 2017 – Jan. 2022',
         '24/7 operations · critical plant · 10 employees · shift work',
         [('The physical stack', 'SCADA, PLC, sensors, gateways and building-'
           'management systems in a plant that never stops. Reliability, '
           'observability and operational ownership practised the hard way: '
           'telemetry and time-series data read at 3 a.m. when something broke.')]),
        ('Electromechanical Technician / Production Manager',
         'ARJ Engineering · Tehran · Dec. 2003 – Mar. 2010',
         '12 mechanics and technicians · machine shop · production line',
         [('The foundation', 'Hardware and software integration at machine level, '
           'a team of 12 developed into capable leads, and root-cause analyses '
           'that changed how faults were handled. Pragmatic decisions, measurable '
           'results.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('EDUCATION AND CERTIFICATES')
    m.edu('B.Tech (EQF6), Technology Management and Mechanical Engineering',
          'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7.6/12')
    m.edu('Danish electrical authorisation LV/MV/HV as Authorised Electrical Engineer',
          'Sikkerhedsstyrelsen · May 2023')
    m.edu('Electrical and Mechanical Engineering Design, electrical (EQF6)',
          'Tehran Technical University · 2000–2003')
    m.edu('PRINCE2, certified project manager', 'AXELOS / PeopleCert')
    m.edu('Refrigeration and climate systems (AMU)',
          'Mercantec · 2021 · STCW 2021–2023, Danish Maritime Authority')

    m.section('COMPETENCIES')
    m.bullet('AI-native engineering', 'Software products and AI tools built in the '
             'AI department (4-10 specialists). Daily coding with AI tools, Claude '
             'included, with critical judgement of every output, and a clear view '
             'of how AI reshapes both products and the engineering craft itself.',
             after=10)
    m.bullet('Architecture and judgement', 'Complex physical-digital systems taken '
             'apart and put back together for 20+ years. Simplify over accumulate, '
             'pragmatic technology decisions over fashionable ones, and technical '
             'debt addressed while services keep running.', after=10)
    m.bullet('Leadership and organisation', 'Teams from 4 to 25 people led and '
             'developed since 2003: apprentices grown into skilled staff, seniors '
             'into leads, and responsibility distributed as teams matured. Clear '
             'engineering practices written down and followed.', after=10)
    m.bullet('Delivery and quality', 'PRINCE2, CI/CD-style discipline in the AI '
             'workflow, code reviews, automated testing habits and meaningful '
             'measures of quality and delivery. 37 projects delivered with zero '
             'critical findings at handover.', after=10)
    m.bullet('Customers and value', 'Engineering priorities tied to customer and '
             'business value: tenders, service agreements and direct customer '
             'dialogue (ELOHVAC 2023-2026), and the meter-to-insight bridge from '
             'SCADA, PLC, sensors and gateways in critical utilities.', after=10)

    m.section('THE FIRST 90 DAYS')
    m.para('The plan follows the role: direction, organisation, outcomes.', after=8)
    m.bullet('Days 1-30 · The direction', 'Dig into the platform with the team: '
             'code, architecture, the hardest technical challenges. Goal: the '
             'first draft of a clear architectural direction, prioritised with '
             'the engineers who own it.', after=10)
    m.bullet('Days 31-60 · The organisation', 'One-to-ones with every engineer, '
             'practices tightened around testing, reviews and operational '
             'ownership, and meaningful measures introduced. Goal: an engaged '
             'engineering team with stronger technical confidence.', after=10)
    m.bullet('Days 61-90 · The outcomes', 'Plans translated into delivery '
             'rhythm, architecture decisions made visible, and technology '
             'choices connected to measurable customer outcomes. Goal: simpler '
             'decisions, visible progress, and less time to connect new '
             'customers.', after=10)

    m.section('LANGUAGES, TOOLS AND PRACTICALS')
    m.para('Danish (native) · English (professional) · Persian (native). AI-native '
           'development workflow (Claude and comparable tools) daily; PRINCE2; SAP '
           'ERP, Microsoft Project, SharePoint, Excel. Electrical authorisation '
           'LV/MV/HV. Driving licence B (manual gear). Based in Måløv, 35-45 '
           'minutes from the Køge office; hybrid three days on site works well.',
           after=32)

    # ------------------------------------------------------------- page 4
    m.page_break()
    m.models_table('Head of Engineering, Enity · requirements and documentation',
                   ('Requirement in the posting', 'Documented experience'),
                   [
        ('Significant experience designing, building and operating complex SaaS '
         'platforms or distributed software systems',
         'Software products and AI tools designed, built and operated in the AI '
         'department (Data Power 2024-2026), scaling the team from 4 to 10 '
         'specialists. A SaaS platform with 90,000+ connected meters is the next '
         'scale; the distributed-systems discipline comes from hardware/software '
         'integrations in critical utilities.'),
        ('Deep technical understanding of backend architecture, databases, APIs, '
         'integrations and cloud infrastructure',
         'Databases, APIs and cloud services in daily use across the tool-building '
         'work, and integrations to physical systems (SCADA, PLC, gateways, BMS) '
         'since 2017. Backend architecture at SaaS depth is where my AI-native '
         'practice meets your platform, and I read and review the code to get '
         'there.'),
        ('Experience with TypeScript, Node.js, PostgreSQL, AWS or comparable '
         'technologies',
         'Comparable technologies and the AI-native development stack, with '
         'TypeScript, Node.js, PostgreSQL and AWS picked up as the natural next '
         'step. Learning new technical stacks quickly is a trained habit: GMP, '
         'FDA and EMA rules learned in weeks (Novo 2022-2024).'),
        ('A background as a software engineer, and you can still read code, review '
         'a pull request and follow a technical discussion in detail',
         'The software engineering story is recent and real: daily coding with AI '
         'tools (Claude included) in a department that ships software products and '
         'AI tools, and critical review of every output. Twenty years of '
         'engineering judgement from electrical, mechanical and process systems '
         'backs the reviews.'),
        ('An ability to simplify complex architectures, address technical debt and '
         'make pragmatic technology decisions',
         'Simplification in practice: complex technical estates cut to what works '
         '(own company 2023-2026), technical debt addressed while customers kept '
         'running, and pragmatic choices defended against elegant ones in 37 '
         'CAPEX projects (Novo 2022-2024).'),
        ('Experience leading engineering teams, developing people and building '
         'strong engineering practices',
         'Leadership since 2003: AI department 4-10 people (2024-2026), 25 '
         'specialists (Novo 2022-2024), 14 people (Ventek 2022) and 10 on shifts '
         '(Biofos 2017-2022). Apprentices developed to skilled staff, practices '
         'written down and followed.'),
        ('The confidence to challenge technical decisions constructively, explain '
         'trade-offs clearly and take responsibility for outcomes',
         'Trade-offs explained on the ground: full P&L responsibility (ELOHVAC '
         '2023-2026), customer negotiations with clear positions, and technical '
         'decisions defended with data rather than titles since 2003.'),
        ('A solid understanding of software quality, reliability, security, '
         'observability and modern DevOps practices',
         'Quality and reliability learned where they are not negotiable: 24/7 '
         'critical utilities (Biofos 2017-2022), GMP documentation and audits '
         '(Novo 2022-2024), and automated verification and observability habits '
         'in the AI-native workflow.'),
        ('Experience connecting engineering priorities and technology decisions '
         'with customer and business value',
         'Customer value as the compass: own customers and service agreements '
         '(ELOHVAC 2023-2026), 37 CAPEX projects justified on business outcomes '
         '(Novo 2022-2024), and deliverables where engineering decisions trace '
         'back to real customer problems.'),
        ('Curiosity about AI and how it will transform software products and '
         'engineering itself',
         'Not curiosity, practice: an AI department built from 4 to 10 people, '
         'software products and AI tools shipped, and daily coding with AI tools '
         'with critical judgement of the output. The standard I hold myself to: use AI responsibly while '
         'judging its output critically, and I can show what that means in a '
         'code review.'),
        ('Set the technical direction and simplify our architecture; ownership of '
         'critical architectural decisions',
         'Direction set in moving environments since 2003: technical estates, '
         'project portfolios of 37 parallel projects, and architecture-level '
         'trade-offs made and owned, not deferred. The surfaces I would own: '
         'backend, data platform, integrations and cloud infrastructure.'),
        ('Lead engineering across software, data and IoT as one coherent '
         'technology ecosystem',
         'The physical side is home ground: SCADA, PLC, sensors, gateways and '
         'building-management systems in critical utilities (Biofos 2017-2022), '
         'with software that has to speak to them. One ecosystem spanning code '
         'and machines is the normal case for me.'),
        ('Build and develop a high-performing engineering organisation with '
         'direct people management',
         'Direct people management for 20+ years, most recently the AI department '
         '(4-10 specialists). Seniors and apprentices developed into leads (ARJ, '
         'ELOHVAC), and responsibility distributed as teams matured.'),
        ('Strengthen engineering execution and delivery; automated testing, '
         'CI/CD, code reviews and operational ownership',
         'Delivery discipline from 37 projects with zero critical findings (Novo '
         '2022-2024), PRINCE2 planning, code reviews and automated testing in the '
         'AI workflow, and operational ownership practised in 24/7 plant. '
         'Meaningful measures tracked weekly, not at quarter end.'),
        ('Connect technology with customers and business outcomes; work closely '
         'with Commercial Growth and Customer Success',
         'Close to commercial and customer teams: tenders, service agreements and '
         'follow-up (ELOHVAC 2023-2026), and handover speed improved by removing '
         'friction between commissioning and daily use (Novo 2022-2024).'),
        ('Have worked with IoT, connected devices, telemetry, time-series data or '
         'hardware/software integrations',
         'All of it in live systems: meters and sensors, gateways and BMS '
         'integrations, SCADA and PLC telemetry read as time-series data in a '
         'plant that runs 24/7 (Biofos 2017-2022, current electrical work). IoT '
         'with real wires attached.'),
        ('Have modernised a mature software platform while keeping existing '
         'customers and services running',
         'Platform modernisation at SaaS scale is not my story yet. Keeping '
         'existing customers and services running while the machinery underneath '
         'changed is: service agreements maintained through reorganisation '
         '(ELOHVAC 2023-2026) and live plant upgraded without stoppages (Biofos '
         '2017-2022).'),
        ('Have developed Tech Leads or senior engineers into effective people '
         'managers; led engineering organisations through growth or significant '
         'technological change',
         'Apprentices and specialists developed into leads (ARJ 2003-2010, '
         'ELOHVAC 2023-2026), an AI department grown from 4 to 10 people through '
         'significant technological change (2024-2026), and technology strategy '
         'contributed beyond day-to-day as CTO and owner.'),
        ('Hybrid role based at the office in Køge, Denmark; a team of about 12 '
         'developers; hands-on leadership role',
         'Three days in Køge works: Måløv is 35-45 minutes away. A 12-developer '
         'team is the size I know best (4-25 range documented). Hands-on is the '
         'only leadership style I trust: close to the code and close to the '
         'machines.'),
                   ], widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo · Head of Engineering, Enity')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Enity_HeadOfEngineering.docx')
    build(out)
    print(out)
