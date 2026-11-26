# -*- coding: utf-8 -*-
"""Head of Analytics Engineering — Vestas, Copenhagen S (Job ID 80792, engelsk opslag ->
en-GB dokument). 4 sider i masterdesign: brev side 1, CV side 2-3, kravmatrix side 4.

Ingen kontaktperson i opslaget -> "Dear Vestas Hiring Team,". Upload via deres system.

STILVALG (style_guard godkendt, 3/3 skift mod #428 Uggerly VVS):
  register    = Scale and trust (scalable · standardised · trusted data · measurable value)
  åbningsgreb = BE (the meeting where two slides disagree: one number is wrong and the
                room moves on)
  struktur    = Roadmap, team, platform (the roadmap · the team · the platform)

BRUGERENS KORREKTION + permanent regel: humaniseret brev OG CV. Engelsk: sammentrækninger
(I'm, don't, it's, I'd, I'll) — BINDENDE. Ingen em dash. Ingen forbudte engelske ord:
spearheaded, leveraged, passionate, dynamic, results-driven, proven track record, synergy,
cutting-edge, innovative solutions, seamlessly, robust, demonstrated ability, "in today's
fast-paced world". "Demonstrated ability" er JD-sprog OG forbudt -> brug kun "ability to
lead engineering teams".

BRUGERSVAR 26.11: (1) SQL + datamodeller/databaser bruges DAGLIGT i AI-arbejdet -> skrives
som reel erfaring, men IKKE som 8-12 års BI-karriere. (2) Cloud-data-platforme (Snowflake/
Databricks): ingen erfaring -> ærlig grænse med keywords på plads (brugerens valg).

Grænserne skrives ligeud og selvsikkert (Quantum-mønster), uden undskyldningssprog og uden
forbudte vendinger ("X is new to me", "I need to learn", "hopefully").
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Vestas · Head of Analytics Engineering'
BANNER_RESUME = 'Analytics engineering · team leadership · SQL and data · delivery'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('26 November 2026')
    m.meta('Job ID 80792 · Reporting & Analytics Centre of Excellence')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Head of Analytics Engineering, Copenhagen S',
           bold=True, color='1A1A1A')
    m.para('Dear Vestas Hiring Team,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('Every leadership team has sat in the meeting where two slides disagree. Both '
       'numbers look credible, one of them is wrong, and the room moves on anyway. That '
       'meeting is what the Reporting & Analytics (R&A) Centre of Excellence at Vestas '
       'is built to end, and it\u2019s the reason I\u2019m writing about the Head of '
       'Analytics Engineering role, Job ID 80792.')

    lp('The CoE brief is a scalable, standardised, and high-quality analytics '
       'environment that delivers a single source of truth across the organisation: '
       'performance transparency, accelerating decision-making, and reducing manual '
       'reporting. Data-driven performance management and decision-making across Vestas '
       'is the purpose, and the operating model matters as much as the tools: '
       'business-facing analytics, governance and data definitions, analytics '
       'engineering, and operations in a single integrated operating model. Modern '
       'engineering practices applied to Finance\u2019s numbers is the kind of problem '
       'I move for.')

    lp('The role owns the analytics engineering strategy, roadmap, and delivery for the '
       'global Performance Analytics Engineering function, and it develops a team of '
       'Analytics Engineers with technical excellence, collaboration, and consistent '
       'performance. I\u2019ve led engineering teams for twenty years: 4-10 people '
       'building AI products at Data Power today, 25 specialists across engineering, '
       'procurement and operations at Novo Nordisk, 14 in installation projects, 12 in '
       'manufacturing. Team names change; what doesn\u2019t change is the work: setting '
       'direction, hiring, coaching and holding a delivery standard, and I don\u2019t do '
       'it from a distance.')

    lp('Two entries on the requirements list deserve a straight answer. On Snowflake and '
       'Databricks, the modern cloud data platforms from the posting, I\u2019ll be plain: '
       'the platforms I\u2019ve run are cloud AI infrastructure at Data Power and '
       'SCADA/PLC operational data platforms at Biofos. The databases and data models our '
       'products run on are mine to design, and data architecture, data modelling, and '
       'SQL are my daily tools in that work. On the 8-12+ years in Data Analytics and BI: '
       'my record is twenty-plus years of data-heavy engineering with the last two in AI '
       'and analytics leadership, plus a B.Tech degree in engineering (EQF6). The years '
       'are on the table and the comparison is yours to make.')

    lp('Solid partnership and collaboration skills have been the daily mode: working '
       'effectively across business and technology teams until the numbers mean the same '
       'thing in both rooms. High attention to detail is a professional habit; GMP '
       'documentation, FAT/SAT protocols, zero critical findings at handover. Sound '
       'business acumen came the expensive way, running a company with full P&L '
       'responsibility. A strategic mindset isn\u2019t a slogan where I work; it\u2019s '
       'what owning an AI roadmap at a small firm forces on you every week.')

    lp('Vestas offers a modern technology environment and the chance to build enterprise '
       'analytics at scale, with a good pay and benefits package and room for professional '
       'growth and development in a purpose-driven business. If the picture I\u2019ve laid '
       'out fits what the CoE needs, I\u2019d welcome the conversation. I\u2019m on +45 93 '
       '99 95 14, and I\u2019ll come prepared for the technical questions.', after=44)

    m.para('Kind regards,', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFILE')
    m.para('Analytics and engineering leader who builds data products and the teams '
           'behind them. CTO for an AI department of 4-10 people, with SQL and data '
           'models under everything we ship, and before that twenty years of engineering, '
           'operations and project delivery. B.Tech (EQF6), PRINCE2, and used to sitting '
           'between business and technology until decisions rest on numbers both sides '
           'trust.', after=32)

    m.section('EXPERIENCE')
    jobs = [
        ('CTO, AI Department',
         'Data Power Consultant ApS · Copenhagen · 2024 – present (ELOHVAC\u2019s '
         'electrical activities added Nov. 2026)',
         'AI department 4-10 people · Python, LLM agents, SQL · data products for clients',
         [('Data and delivery', 'Databases and data models designed for the products we '
           'ship; SQL in daily use. AI agents and analytics products delivered to '
           'clients, investment cases followed up monthly. The team hired, coached and '
           'scaled from 4 to 10.')]),
        ('Owner / Technical Director',
         'ELOHVAC ApS · Copenhagen · May 2023 – Nov. 2026 (company closed)',
         'Commercial customers · HVAC and electrical · full P&L · service agreements',
         [('Business and reporting', 'Full P&L, pricing and monthly reporting run by me: '
           'contribution margin on every quote, budgets and cash flow followed closely. '
           'Service agreements measured on response time and quality, renewed on '
           'delivery.'),
          ('Team and standards', '5 electricians and 3 apprentices led with structured '
           'training and clear expectations. Standard work and quality routines, and the '
           'customers stayed.')]),
        ('Senior Commissioning Engineer / Project Manager, Electrical Systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · Nov. 2022 – Jul. 2024',
         '37 CAPEX projects, DKK 2-10 m · 25 specialists · GMP/FDA/EMA',
         [('Governance and analytics', '37 projects steered on time, cost and quality '
           'with 25 specialists across engineering, procurement and operations. Monthly '
           'reporting, change calculation and SAP ERP follow-up; zero critical findings '
           'at handover. PRINCE2 as the shared structure.')]),
        ('Project & Workshop Manager',
         'Ventek-Air · Copenhagen · Jan. 2022 – Nov. 2022',
         '11 parallel ventilation projects · 14 staff · subcontractors',
         [('Portfolio', '11 parallel projects for public and private clients, resources '
           'prioritised weekly across all of them. Quotes, contracts and project '
           'economics followed per project, and manual reporting rebuilt into one '
           'structured overview.')]),
        ('Maintenance & Operations Manager / Workshop Technician',
         'Biofos (Lynetten) · Copenhagen · Aug. 2017 – Jan. 2022',
         '24/7 operations · SCADA, PLC, HV switchgear · 10 employees · shifts',
         [('Operational data platforms', 'SCADA and PLC platforms operated around the '
           'clock: pumps, treatment plant, HVAC, process pipes and instrumentation. '
           'Operational data used for maintenance planning; 5S and Standard Work '
           'introduced in the workshop.')]),
        ('Electromechanical Technician / Production Supervisor',
         'ARJ Engineering · Tehran · Dec. 2003 – Mar. 2010',
         '12 mechanics and technicians · machine shop · product line',
         [('The foundation', 'Production supervision with 12 mechanics and technicians: '
           'schedules, materials and targets. Root-cause analysis changed how faults were '
           'handled.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('EDUCATION AND CERTIFICATIONS')
    m.edu('B.Tech (EQF6), Technology Management and Mechanical Engineering',
          'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7.6/12')
    m.edu('Authorised electrical engineer (LV/MV/HV)', 'Sikkerhedsstyrelsen · May 2023')
    m.edu('Electrical and mechanical design, electrical engineering (EQF6)',
          'Tehran Technical University · 2000–2003')
    m.edu('PRINCE2, certified project manager', 'AXELOS / PeopleCert')
    m.edu('Refrigeration & AC (AMU)', 'Mercantec · 2021 · STCW 2021–2023, Danish Maritime Authority')

    m.section('COMPETENCIES')
    m.bullet('Team leadership', 'Engineering teams of 4-25 people led since 2003: '
             'hiring, coaching, delivery standards. 3 apprentices trained to journeymen, '
             'engineers developed into specialists.', after=10)
    m.bullet('SQL & data modelling', 'SQL, databases and data models in daily use in the '
             'AI team\u2019s work (2024-now). Data-heavy engineering throughout: process '
             'data, calculations, SAP and Excel reporting since 2003.', after=10)
    m.bullet('Delivery & governance', 'PRINCE2-structured delivery across 37 GMP '
             'projects (Novo 2022-2024), portfolio management of 11 parallel projects '
             '(Ventek 2022), zero critical findings at handover.', after=10)
    m.bullet('Business partnership', 'Finance-side experience with money at stake: full '
             'P&L as owner (2023-2026), budget follow-up in every project role, '
             'investment cases with monthly follow-up.', after=10)
    m.bullet('Modern AI engineering', 'Python, Claude and LLM agents in daily production '
             '(Data Power 2024-now). Cloud AI infrastructure operated by the team I '
             'lead.', after=10)

    m.section('THE FIRST 90 DAYS')
    m.para('The plan follows the role itself: roadmap, team, platform.', after=8)
    m.bullet('Days 1-30 · Roadmap', 'Listening first: the portfolio, the Product Owners, '
             'the definitions behind the numbers. Draft the analytics engineering '
             'strategy with the pain points mapped. Goal: a roadmap the team recognises.',
             after=10)
    m.bullet('Days 31-60 · Team', 'Delivery rhythm and team development in place: 1:1s, '
             'technical standards, consistent performance conversations. Goal: the team '
             'ships predictably and knows the bar.', after=10)
    m.bullet('Days 61-90 · Platform', 'Technology stack governed and architecture '
             'standards agreed; data sourcing and platform evolution with Digital '
             'underway. Goal: fewer manual reports, one trusted number in the leadership '
             'pack.', after=10)

    m.section('LANGUAGES, TOOLS AND PRACTICALITIES')
    m.para('Languages: Danish (native), English (professional), Persian (native). SQL and '
           'databases daily; Python, SAP ERP, Excel/Office; PRINCE2. Driving licence B '
           '(manual). Based in Måløv, greater Copenhagen. A start date at short notice '
           'works for me.', after=32)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Head of Analytics Engineering · requirements and evidence',
                   ('Requirement in the posting', 'Evidence'),
                   [
        ('Degree in IT, data, or engineering',
         'Engineering degree covered: B.Tech (EQF6) in Technology Management and '
         'Mechanical Engineering (2017-2022), electrical engineering at EQF6 (2000-2003) '
         'and authorised electrical engineer status (2023). Technical rigour applied to '
         'data problems for 20+ years.'),
        ('8-12+ years experience in Data Analytics and BI',
         'Counted straight: two years in AI and analytics leadership (Data Power '
         '2024-now) on top of 20+ years of data-heavy engineering (process data, '
         'calculations, SAP reporting since 2003). The engineering depth carries the '
         'analytics; the CV shows the years.'),
        ('Building and delivering analytical solutions that support business '
         'decision-making',
         'Analytical solutions shipped daily: SQL databases and data models feeding '
         'Python/LLM products (Data Power 2024-now), management reporting and budget '
         'follow-up (ELOHVAC 2023-2026, full P&L), and 37 projects steered with monthly '
         'reporting (Novo 2022-2024).'),
        ('Data architecture, data modelling, and SQL',
         'Daily tools at Data Power (2024-now): the databases and data models our AI '
         'products run on are designed by me, with SQL as the working language. '
         'Enterprise data warehousing programmes I haven\u2019t owned; the modelling '
         'discipline transfers.'),
        ('Experience with modern cloud data platforms (Snowflake, Databrick and similar)',
         'Platform record: cloud AI infrastructure operated daily (Data Power 2024-now) '
         'and SCADA/PLC operational data platforms (Biofos 2017-2022). Snowflake and '
         'Databricks aren\u2019t on my list; the databases and data models our products '
         'run on are.'),
        ('Ability to lead engineering teams',
         'Engineering teams led for 20+ years: 4-10 in AI (Data Power 2024-now), 25 '
         'specialists across engineering, procurement and operations (Novo 2022-2024), 14 '
         'in installation projects (Ventek 2022), 12 in manufacturing (ARJ 2003-2010), 8 '
         'in own company (2023-2026). Hiring, coaching and delivery standards throughout.'),
        ('Experience operating cloud and data platforms for analytics',
         'Platform operations in practice: 24/7 operational data platforms with SCADA and '
         'PLC (Biofos 2017-2022) and cloud AI infrastructure run daily by my team (Data '
         'Power 2024-now), with monitoring, uptime and change control as everyday '
         'disciplines.'),
        ('Scalable analytics architectures delivering trusted, high-quality data',
         'Trusted output as the standard: zero critical findings at handover across 37 '
         'GMP projects (Novo 2022-2024), quality systems in medical-device work '
         '(FDA/ISO13485), and scalable AI solution architectures built data-first (Data '
         'Power 2024-now).'),
        ('Translate complex business challenges into practical solutions that create '
         'measurable value',
         'Translation with numbers attached: airflow and energy calculations on a PDCA '
         'cycle at Novo, investment cases with monthly follow-up (Data Power 2024-now), '
         'and business cases for new service concepts (ELOHVAC 2023-2026).'),
        ('Solid partnership and collaboration across business and technology teams',
         'Partnership as daily mode: 25 specialists across engineering, procurement and '
         'operations (Novo 2022-2024), customer-facing delivery (Ventek 2022, ELOHVAC '
         '2023-2026), and AI products built with the client in the room (Data Power).'),
        ('Strategic mindset, aligning analytics capabilities and technology with '
         'long-term business objectives',
         'Strategy set at CTO level: AI roadmap and technology choices for Data Power '
         '(2024-now), technical direction as owner (2023-2026), and portfolio priorities '
         'across 37 projects (Novo 2022-2024).'),
        ('Sound business acumen and business management principles',
         'Acumen earned with money at stake: full P&L and liquidity as owner (ELOHVAC '
         '2023-2026), pricing and contribution margin on own quotes (Ventek 2022), and '
         'budget responsibility in every project-management role.'),
        ('Identify opportunities to transform data into strategic analytical assets',
         'Opportunities turned into products: AI agents and data products delivered to '
         'clients (Data Power 2024-now), process data used to cut energy use at Novo '
         '(PDCA cycle), and manual reporting rebuilt into one structured overview (Ventek '
         '2022).'),
        ('High attention to detail, accuracy, quality, and consistency',
         'Detail as professional habit: GMP/FDA/EMA documentation with zero critical '
         'findings (Novo 2022-2024), FAT/SAT and IQ/OQ/PQ protocols, and quality measured '
         'in service agreements (ELOHVAC 2023-2026).'),
        ('Own the analytics engineering strategy, roadmap, and delivery',
         'Strategies owned before: AI department strategy and delivery (Data Power '
         '2024-now), technical roadmap as CTO/owner (2023-2026), and PRINCE2-structured '
         'delivery across 37 projects (Novo 2022-2024).'),
        ('Manage and develop a team of Analytics Engineers; technical excellence, '
         'collaboration, and consistent performance',
         'Team development with results: 3 apprentices trained to journeymen (ELOHVAC '
         '2023-2026), 4-10 AI engineers hired and coached (Data Power 2024-now), and '
         'standard work raising consistency (Biofos 2017-2022).'),
        ('Portfolio of analytical products and solutions; design, development, '
         'deployment, and operation of analytical solutions with Product Owners, aligned '
         'with business priorities',
         'Portfolio management is familiar ground: 11 parallel projects aligned to client '
         'priorities (Ventek 2022), a 37-project portfolio with governance (Novo '
         '2022-2024), and product-style delivery with owners in the AI team (Data Power '
         '2024-now).'),
        ('Own and govern the analytical technology stack, architectural standards',
         'Governance with teeth: architectural and quality standards enforced in GMP '
         'environments (Novo 2022-2024), technology stack choices owned as CTO (Data '
         'Power 2024-now), SAP ERP and PRINCE2 as shared standards.'),
        ('Collaborate with Digital and business stakeholders, efficient data sourcing, '
         'scalable analytical products',
         'Cross-team platform work: data sourcing and integrations built between AI '
         'products and client systems (Data Power 2024-now), SCADA and data platform '
         'upgrades (Biofos 2017-2022), and structured reporting rolled out (Ventek 2022).'),
                   ], widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo — Head of Analytics Engineering, Vestas')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Vestas_HeadOfAnalyticsEngineering.docx')
    build(out)
    print(out)
