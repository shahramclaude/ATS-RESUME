# -*- coding: utf-8 -*-
"""Senior Manager, Strategy, R&D and Innovation — WSA (WS Audiology).

Engelsk opslag -> EN-GB dokument i masterdesign (4 sider): brev side 1,
CV side 2-3, kravmatrix side 4. Intet kontaktnavn i opslaget ->
"Dear Hiring Manager,". Ingen lokation i opslaget -> lokation nævnes slet
ikke (master-regler: flytning/kørsel er stillingsspecifikke bekræftelser).

SAMME-FIRMA-REGLER: WSA er genansøgning (tidligere TechnicalFacilitySpecialist)
-> intet genbruges; alt indhold skrevet friskt til Strategy, R&D & Innovation.

STILVALG (style_guard godkendt, 3/3 skift mod #438 Syntegon):
  register    = Fra signaler til innovation med effekt
  åbningsgreb = BO (fremtiden besluttes i de valg, der træffes nu)
  struktur    = Retning, signaler, beslutninger (30/60/90 = the direction ·
                the signals · the decisions)

ÆRLIG POSITION: strategirollen er et stræk. Broen er CTO-teknologiretning
(Data Power, AI-afdeling fra 0 -> softwareprodukter + AI-værktøjer), 37
CAPEX-investeringsvalg (Novo), 20+ år på tværs af industrier = rollens
eftertragtede "outside-in perspective". "Management consulting" claimes IKKE
(kort ærlig note); Board-level = næste skridt (præsenteret for direktioner
og kundedirektører). Master's claimes IKKE (B.Tech = technology-related
field, "an advantage, not required").

BRUGERENS KORREKTION: humaniseret brev OG CV. Ingen em dash. Ingen forbudte
ord som egne påstande. Engelsk: sammentrækninger bindende.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_Enity_HeadOfEngineering.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'WSA · Senior Manager, Strategy, R&D and Innovation'
BANNER_RESUME = 'STRATEGY · R&D · INNOVATION · TECHNOLOGY-LED CHANGE'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('26 November 2026')
    m.meta('Global R&D · strategy and innovation')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Senior Manager, Strategy, R&D and Innovation',
           bold=True, color='1A1A1A')
    m.para('Dear Hiring Manager,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('The technologies that will reshape hearing care are barely emerging '
       'today. That\u2019s not a reason to wait; it\u2019s the reason the choices made '
       'now carry more weight than the plan written last year. WSA\u2019s ambition '
       'isn\u2019t simply to respond to that future but to help create it, and the '
       'work sits at the intersection of technology, strategy and execution, '
       'where ambition stops being a paragraph and starts being direction.')

    lp('At WSA, innovative hearing aids and hearing health services reach '
       'people everywhere, with 12,000 colleagues in 130 countries working to unlock '
       'human potential by bringing back hearing. The part of this role that '
       'draws me is its stated mission: help shape the future of R&D and turn '
       'strategy into innovation with impact. That asks for an outside-in '
       'perspective on the long-term R&D agenda, the nerve to challenge and '
       'sharpen strategic choices, and the craft to translate emerging '
       'technologies, customer needs and industry dynamics into clear priorities '
       'and action.')

    lp('My route here runs through technology strategy rather than a strategy '
       'consultancy. As CTO for an AI department built from the ground up, I\u2019ve '
       'decided where the technology should go next, framed the questions worth '
       'asking, and moved ideas from exploration toward tangible customer and '
       'business value: software products and AI tools in customers\u2019 hands, not '
       'slide decks. Before that, 37 CAPEX projects at Novo Nordisk, DKK 2-10 '
       'million each, were exercises in where to invest, accelerate or hold '
       'back, and 20+ years across marine engineering, pharma, energy and AI '
       'give me the outside-in lens this role explicitly calls for.')

    lp('The first 90 days break into three moves. Days 1-30 set the direction: '
       'partner with the CTO, R&D leadership and Strategy, read the long-term '
       'agenda closely, and frame the questions that matter before answers are '
       'proposed. Days 31-60 anticipate what comes next: an outside-in scan of '
       'technologies, scientific developments, business models and market shifts '
       'that could transform hearing care, then translate these signals into '
       'strategic implications and shape the first meaningful innovation '
       'programs. Days 61-90 deliver the decisions: clear choices and actionable '
       'recommendations in key management forums, and transformation initiatives '
       'moving on efficiency, commonality and collaboration across global R&D.')

    lp('What the CTO needs from this role is simple: turn complex technological '
       'questions into simple and compelling narratives, clear choices and '
       'actionable recommendations. I do that weekly, because management, '
       'customers and engineers all need the same truth in different shapes. '
       'Stakeholder leadership across functions, geographies and levels of '
       'seniority has been the job since 2003, from 25 specialists across '
       'engineering, procurement and operations at Novo to 14-person project '
       'teams with suppliers in the same room. Executive and Board-level '
       'presentations are the natural next step from the management forums and '
       'customer directors I\u2019ve presented to for years.')

    lp('The culture WSA describes, where innovation, curiosity, speed and '
       'disciplined execution reinforce each other, is the one I work best in; '
       'so is the promise that we care for one another, welcome diversity and '
       'celebrate our successes. An AI department started from nothing and '
       'turned into products customers pay for is my proof that strategy can '
       'become innovation on a budget. The chance to shape the future of R&D in '
       'a field that gives people their hearing back is why I\u2019m writing. I look '
       'forward to hearing from you.', after=44)

    m.para('Kind regards', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFILE')
    m.para('CTO who turns technology into direction. An AI department built from '
           'zero into software products and AI tools, 37 CAPEX projects steered '
           'at Novo Nordisk, and 20+ years reading technology-intensive '
           'organisations from the inside and from the outside. B.Tech in '
           'technology management, PRINCE2, and a habit of turning complex '
           'technical questions into clear choices that management can act on.',
           after=32)

    m.section('PROFESSIONAL EXPERIENCE')
    jobs = [
        ('CTO, AI Department & Authorised Electrical Engineer (LV/MV/HV)',
         'Data Power Consultant ApS · Copenhagen · 2024 – present (from Nov. 2026 '
         'also ELOHVAC\u2019s electrical activities)',
         'AI department 4-10 people · software products and AI tools · electrical '
         'service and enterprise',
         [('Technology direction and innovation', 'Set the technology direction '
           'and roadmap for an AI department built from scratch: which products and tools to '
           'build, what to stop, and how ideas moved from exploration into '
           'software products and AI tools in customers\u2019 hands. Daily AI-native '
           'development practice with critical review of every output, and '
           'choices explained to management without the jargon.')]),
        ('Owner / Technical Director / Authorised Electrical Engineer',
         'ELOHVAC ApS · Copenhagen · May 2023 – Nov. 2026 (company closed)',
         'Business customers · electrical, ventilation and climate · full P&L · '
         'service agreements',
         [('Business and technology choices', 'Full P&L ownership meant the '
           'portfolio choices were mine: which services to sell, where to invest '
           'in the team (5 electricians and 3 apprentices), and how to price and '
           'negotiate. Direct dialogue with customers about priorities and '
           'investment, and suppliers managed on shared goals.')]),
        ('Senior Commissioning Engineer / Project Manager, Electrical Systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · Nov. 2022 – Jul. 2024',
         '37 CAPEX projects, DKK 2-10 million each · 25 specialists · GMP/FDA/EMA',
         [('Investment portfolio in a regulated industry', '37 parallel CAPEX '
           'projects with 25 specialists across engineering, procurement and '
           'operations: decisions on where to invest and accelerate, trade-offs '
           'owned rather than deferred, and reporting to senior stakeholders in '
           'GMP- and FDA/EMA-inspectable environments. FAT/SAT, IQ/OQ/PQ and '
           'documentation that withstood revision.')]),
        ('Project & Workshop Manager',
         'Ventek-Air · Copenhagen · Jan. 2022 – Nov. 2022',
         '11 projects · 14 people · subcontractors · tender to handover',
         [('Outside-in to customers\u2019 operations', '11 projects run from tender '
           'to handover with 14 people and subcontractors. The outside view on '
           'how customers\u2019 organisations really run, and partnerships with '
           'suppliers where shared goals decided the outcome. MS Project for '
           'plans, weekly alignment for decisions.')]),
        ('Maintenance & Operations Manager / Workshop Technician',
         'Biofos (Lynetten) · Copenhagen · Aug. 2017 – Jan. 2022',
         '24/7 operations · critical plant · 10 people · shift work',
         [('Technology-intensive operations', 'Pumps, HVAC, process piping, SCADA '
           'and PLC kept running around the clock with 10 people on shifts. '
           'Complexity translated into priorities a shift team could act on, and '
           'MTBF, MTTR and uptime followed as measures, not slogans.')]),
        ('Electromechanical Technician / Production Supervisor',
         'ARJ Engineering · Tehran · Dec. 2003 – Mar. 2010',
         '12 mechanics and technicians · machine workshop · production line',
         [('Continuous improvement', 'Production workshop with 12 mechanics and '
           'technicians: maintenance, spare parts and planning. Root-cause '
           'analyses that changed how failures were handled, and results '
           'followed week by week rather than at year end.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('EDUCATION & CERTIFICATION')
    m.edu('B.Tech (EQF6), Technology Management and Mechanical Engineering',
          'Copenhagen School of Marine Engineering & Technology Management · '
          '2017-2022 · GPA 7.6/12')
    m.edu('Danish electrical authorisation LV/MV/HV (Authorised Electrical Engineer)',
          'Sikkerhedsstyrelsen · May 2023')
    m.edu('Electrical and Mechanical Engineering Design (EQF6)',
          'Tehran Technical University · 2000-2003')
    m.edu('PRINCE2 Certified Project Manager', 'AXELOS / PeopleCert')
    m.edu('Refrigeration and Climate Systems (AMU)',
          'Mercantec · 2021 · STCW 2021-2023, Danish Maritime Authority')

    m.section('COMPETENCIES')
    m.bullet('Strategy and technology', 'Technology strategy set at CTO level: '
             'where to invest, where to accelerate and what to stop. Complexity '
             'translated into strategic insight, and priorities that survive '
             'contact with reality.', after=10)
    m.bullet('Innovation', 'An AI department started from nothing: innovation '
             'programs from idea to software products and AI tools with tangible '
             'customer and business value. AI-native development with critical '
             'judgement of every output.', after=10)
    m.bullet('Executive communication', 'Complex technological questions turned '
             'into simple narratives for management, customers and engineers. '
             'Reporting lines to directors and management forums are familiar '
             'ground; Board-level is the natural next step.', after=10)
    m.bullet('Stakeholders', 'Across functions, geographies and levels: 25 '
             'specialists at Novo, 14-person project teams at Ventek, suppliers '
             'and technology partners negotiated on shared goals. Danish, '
             'English and Persian.', after=10)

    m.section('FIRST 90 DAYS')
    m.para('The plan follows the role: the direction, the signals, the decisions.',
           after=8)
    m.bullet('Days 1-30 · The direction', 'The R&D agenda, the organisation and '
             'the key forums learned closely, with the CTO and R&D leadership. '
             'Goal: the questions that matter are framed, and my map of where R&D '
             'stands matches theirs.', after=10)
    m.bullet('Days 31-60 · The signals', 'An outside-in scan running: '
             'technologies, scientific developments, business models and market '
             'shifts, with the first strategic implications on paper and '
             'innovation programs taking shape. Goal: fresh perspectives are '
             'entering the agenda, not just the inbox.', after=10)
    m.bullet('Days 61-90 · The decisions', 'Clear choices and actionable '
             'recommendations delivered in key management forums, and the first '
             'transformation initiatives moving. Goal: decisions made faster '
             'because the questions got sharper.', after=10)

    m.section('LANGUAGES, TOOLS & PRACTICAL')
    m.para('Danish (native) · English (professional) · Persian (native). '
           'Microsoft Office, SAP, Power BI for analytics, MS Project; AI-native development '
           'tooling (Claude, daily); PRINCE2. Driving licence B (manual). '
           'Available by agreement.', after=32)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Requirements and documentation · Senior Manager, '
                   'Strategy, R&D and Innovation, WSA',
                   ('Requirement in the posting', 'Documented experience'),
                   [
        ('Partner with the CTO, R&D leadership and Strategy to develop and '
         'evolve our R&D strategy',
         'Technology direction set at CTO level since 2024 (Data Power): which '
         'products and tools to build, what to stop, and how the AI practice '
         'evolved as the field moved. The partnership with senior technical '
         'leadership is my daily habitat, not a new forum.'),
        ('Frame the questions that matter and facilitate strategic choices on '
         'where to invest, accelerate or challenge established thinking',
         '37 parallel CAPEX projects at Novo Nordisk (2022-2024), DKK 2-10 '
         'million each, were exactly that exercise: where to invest, what to '
         'accelerate and which established habits to challenge. Trade-offs made '
         'and owned with 25 specialists in the room.'),
        ('Accelerate R&D transformation: efficiency, commonality and '
         'collaboration across global R&D',
         'Common AI tooling and templates adopted across projects at Data Power '
         '(2024-present) instead of each team reinventing; standardised work and '
         'shared documentation at Novo across engineering, procurement and '
         'operations. Efficiency and commonality driven by showing the better '
         'way, not mandating it.'),
        ('Foster a culture where innovation, curiosity, speed and disciplined '
         'execution reinforce each other',
         'The AI department at Data Power runs on exactly that mix: fast '
         'iterations with critical review of every output, curiosity about new '
         'models weekly, and disciplined execution in customer deliveries. Built '
         'from zero people to 4-10.'),
        ('Anticipate what comes next: technologies, scientific developments, '
         'business models and market shifts',
         'Betting on AI-native development in 2023-2024, before it became '
         'standard practice, is the clearest example: reading where technology '
         'was moving and building an offer around it. Earlier: SCADA/PLC and '
         'process control kept current through years of technology change in '
         'critical plant.'),
        ('Translate emerging technologies, customer needs and industry dynamics '
         'into clear priorities and action',
         'At Data Power, emerging AI capability becomes concrete priorities: '
         'which tool to build for which customer problem, sequenced against '
         'capacity. At Novo, industry dynamics (GMP/FDA-EMA demands) translated '
         'into project priorities across 37 parallel tracks.'),
        ('Engage with start-ups, technology partners, suppliers and experts',
         'Suppliers and technology partners engaged for years: 10 supplier '
         'contracts negotiated at Hansen (2025-2026), AI tooling partnerships at '
         'Data Power, experts drawn in per topic. Start-up engagement is the '
         'part I would grow fastest; the habit of bringing fresh perspectives '
         'into the organization is the same.'),
        ('Turn strategy into innovation: translate strategic priorities into '
         'meaningful innovation programs',
         'The AI department at Data Power IS such a program: strategic priority '
         '(AI-native capability) turned into meaningful innovation programs that '
         'shipped software products and AI tools to customers from 2024 onward.'),
        ('Move ideas from exploration toward tangible customer and business value',
         'Software products and AI tools in customers\u2019 hands (Data Power '
         '2024-present), service agreements sold and delivered (ELOHVAC '
         '2023-2026), and 11 customer projects brought from tender to handover '
         '(Ventek 2022). Exploration that never reaches value has never '
         'interested me.'),
        ('Enable great executive decisions: executive and Board-level topics and '
         'key management forums',
         'Leadership audiences served since 2003: reporting to '
         'department management and project support at Novo (2022-2024), '
         'customer directors at Hansen (2025-2026), and management forums as '
         'CTO. Board-level presentations are the next step from forums I have '
         'run for years.'),
        ('Turn complex technological questions into simple and compelling '
         'narratives, clear choices and actionable recommendations',
         'The daily craft of a CTO explaining AI and electrical engineering to '
         'managers and customers: complex technological questions turned into '
         'simple narratives, clear choices and actionable recommendations. The '
         'same skill carried a 37-project portfolio into monthly management '
         'reporting.'),
        ('5+ years of relevant experience in R&D strategy, innovation, corporate '
         'strategy, management consulting or strategic program leadership',
         '20+ years of technical leadership, and the strategic program '
         'leadership half is concrete: 37 parallel CAPEX projects steered '
         '(2022-2024), technology strategy owned as CTO (2024-present), '
         'business strategy with P&L (2023-2026). Management consulting is the '
         'one lane I have not worked in; the strategic work is real.'),
        ('Experience working with technology-intensive R&D organizations and '
         'senior executive stakeholders',
         'Novo Nordisk (2022-2024): one of the most technology-intensive and '
         'regulated R&D environments in Denmark, with senior stakeholders in '
         'engineering, procurement and operations. Data Power (2024-present): a '
         'small, fast R&D organisation building its own tools.'),
        ('Strong analytical and problem-solving capabilities, with the ability '
         'to translate complexity into strategic insight',
         'Root-cause analyses that changed failure handling (ARJ 2003-2010), '
         'GAP analyses and risk assessments in GMP environments (Novo '
         '2022-2024), and data-driven prioritisation as CTO. Decisions built on '
         'evidence first, story second.'),
        ('Excellent communication and storytelling skills, including executive '
         'and Board-level presentations',
         'Years of presenting project status, technology choices and business '
         'cases to department managers, directors and customer executives (Novo '
         '2022-2024, Hansen 2025-2026). Storytelling with numbers: what '
         'changed, what it means, what we do next.'),
        ('Strong stakeholder leadership across functions, geographies and levels '
         'of seniority',
         '25 specialists across engineering, procurement and operations (Novo '
         '2022-2024), 14-person teams with subcontractors (Ventek 2022), cross-'
         'functional work with sales, production and service (Hansen '
         '2025-2026), and international environments in Danish, English and '
         'Persian since 2003.'),
        ('Drives Results: consistently delivers strong outcomes, even in '
         'challenging or demanding circumstances',
         '37 projects delivered in GMP/FDA-EMA environments with zero critical '
         'findings (Novo 2022-2024); a company built and run through closure '
         'without dropping customers (ELOHVAC 2023-2026); 24/7 plant kept '
         'running on shifts (Biofos 2017-2022).'),
        ('Collaborates: builds effective partnerships and works across teams to '
         'achieve shared goals',
         'Supplier partnerships where shared goals decided the outcome (Ventek '
         '2022, Hansen 2025-2026), cross-functional project groups led since '
         '2003, and an AI department grown by hiring and developing people '
         '(Data Power 2024-present).'),
        ('A Master\u2019s degree in engineering or a technology-related field '
         '(an advantage, not required)',
         'B.Tech (EQF6) in Technology Management and Mechanical Engineering '
         '(2017-2022, GPA 7.6), Maskinmester with electrical authorisation '
         'LV/MV/HV (2023) and PRINCE2. A Master\u2019s degree is not claimed; the '
         'technology-related field is covered from two directions.'),
    ], widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo - Application Senior Manager Strategy '
                       'R&D and Innovation, WSA')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_WSA_SeniorManagerStrategyRDInnovation.docx')
    build(out)
    print(out)
