# -*- coding: utf-8 -*-
"""atNorth: Strategy Manager (English posting, supplied 25.11.2026).

English posting -> English document (en-GB). Form (master/FORMKATALOG.md):
opening **E** (Tidsforskydningen: the capacity signed in 2029 is shaped this
quarter), structure **The five conversations** (CEO · Board · business leaders ·
functional teams · the market, each with what the strategy role owes it),
register **The decision brief** (question · assumptions · options · numbers ·
owner and date · trigger).

Kulturfil: jd/atNorth_StrategyManager_kultur.txt.
Prior atNorth applications: Manager of Power and Permits (02.11) and Senior
Technical Lead, Electrical (07.11): no opening, structure or register reused.
Culture values verified at careers.atnorth.com (intel 72/142): Dependable,
Empowering, Flexible. No location or contact person stated in the posting.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, 'Strategy Manager · Nordic data center market',
                    'Måløv, Denmark · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('25 November 2026')
    m.meta('atNorth · Strategy · Strategy Manager')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Strategy Manager', bold=True, color='1A1A1A')
    m.para('Dear Strategy Team at atNorth,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ---------------------------------------------------------------- page 1
    lp('**The capacity a Nordic customer will sign for in 2029 is being shaped this quarter.** '
       'Not by the board resolution itself, but by the assumptions that arrive with it: which '
       'market view the growth plan rests on, where power and sustainability constraints bind '
       'first, and what a business case must prove before capital moves. atNorth, headquartered '
       'in Reykjavik, operates eight data centers across the Nordics with additional sites under '
       'development, so the '
       'distance between a decision and its consequence is measured in years. The posting asks '
       'for strategy development and recommendations that influence critical decisions across '
       'growth, power, sustainability, commercial development, and corporate strategy, to '
       'identify opportunities, solve complex business challenges, and keep the Nordic data '
       'center market in view while doing it.', after=44)

    lp('**The five conversations that carry the role.** With the CEO: which growth bets deserve '
       'capital, and what each business case would have to prove. With the Board: what could '
       'break the plan, which assumptions it rests on, and the downside on one page. With the '
       'business leaders: whether the priorities fit the sites and the pipeline that exist. With '
       'the functional teams: who owns the next step of the initiatives already chosen. With the '
       'market: what customer demand, competitor activity and technology developments say that '
       'the plan does not. The posting calls the role a trusted advisor and thought partner to '
       'senior leadership; that standing is earned by bringing the last conversation into the '
       'first four.', after=44)

    lp('**The first 90 days, as a plan and not a promise.** Days 1 to 30: the current corporate '
       'strategy, the board calendar and the market evidence behind the growth plan, mapped with '
       'the Strategy team and the Director of Strategy, and one-to-one conversations with the '
       'functions that own the inputs. Days 31 to 60: the first decision brief on one growth '
       'question, with market view, options, recommendation, NPV and sensitivity, and a session '
       'where the assumptions are tested in the open. Days 61 to 90: a business case standard '
       'the organisation can reuse, the preparation rhythm for the next Board cycle, and one '
       'strategic initiative launched from concept with owners, dates and a review trigger.',
       after=44)

    lp('**Why atNorth.** The company\'s own description is the argument: cost-effective, scalable '
       'high-density colocation and built-to-suit services, with sustainability at our core, '
       'running on renewable energy and designed according to circular economy principles, '
       'delivering reliable, secure, and high-performance infrastructure through innovative '
       'design and power efficiency in how the sites run. The ambition is to help shape the '
       'future of sustainable digital infrastructure and stay at the forefront of the market as '
       'it grows. A strategy function matters most where capital is heavy and timing is long.',
       after=44)

    lp('**The culture part is concrete, which is rare.** The posting describes world-class '
       'technology with a people-first culture built on collaboration, ownership, and trust, '
       'where curiosity, ownership, and impact are valued, and an open, transparent, and '
       'inclusive culture that is more than a priority. "We don\'t just talk about culture; we '
       'nurture it", through regular one-to-one engagements and monthly wellbeing surveys where '
       'every voice is heard, and weekly gatherings sometimes over a simple breakfast and good '
       'conversation, to shape a sustainable future together. The values page adds a line that '
       'strategy work lives on: ask questions, challenge the status quo and take action.',
       after=44)

    lp('**What I bring to the analysis.** Business cases and financial modelling with DCF, NPV, '
       'IRR, sensitivity and scenarios built in Excel and Python, market analysis and KPI work '
       'assembled with Claude Code, and '
       'decision briefs kept to one page so a meeting can decide rather than discuss. The honest '
       'boundary: my strategy work has been done inside operational and ownership roles, not in '
       'a consulting firm; the analysis has been done with real capital at stake, from a product '
       'line\'s pricing and investment decisions to a company\'s full P&L. The posting asks for '
       'strategic thinking with practical execution to turn ambitious goals into tangible '
       'outcomes; that combination is what the evidence below shows.', after=44)

    lp('Shape atNorth\'s future is the posting\'s headline, and the job is the analysis behind '
       'it. I would welcome a conversation about the assumptions in the growth plan and what the '
       'first decision brief should cover. I am based near Copenhagen in Måløv, work in English, '
       'Danish and Persian, and can start at short notice. I can be reached on +45 93 99 95 14 '
       'or ajlooshahram@gmail.com.', after=16)

    m.meta('Kind regards', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, 'Strategy Manager · corporate strategy, growth and decision support',
                    CONTACT, 'PROFILE')
    m.para('Strategy Manager for a Nordic data centre platform: corporate strategy and strategic '
           'direction, where the market view, the assumptions and the owners sit on the same '
           'page, from the first question to the board decision. B.Tech in technology management '
           'and '
           'mechanical engineering, full P&L and investment decisions in own companies, 37 CAPEX '
           'projects with monthly reporting to client leadership, and AI-assisted analysis in '
           'Python and Claude for business cases and market work.', after=64)

    m.section('THE DECISION BRIEF: HOW I READ A STRATEGY QUESTION')
    for label, body in [
        ('The question',
         'A brief starts with the decision to be taken and the date it must be taken by. '
         'Everything after that is support.'),
        ('The assumptions',
         'The plan rests on assumptions about demand, power, price and timing. Name them, or '
         'the risk paragraph is fiction.'),
        ('The options',
         'One option is a recommendation; two options are a decision. Each with its cost, its '
         'upside, and what would make it wrong.'),
        ('The numbers',
         'NPV with sensitivity and scenarios: what the case looks like if demand, price or lead '
         'time moves. Not one heroic number.'),
        ('The owner and the date',
         'A recommendation without an owner and a date is an opinion. The brief ends with both.'),
        ('The trigger',
         'Every plan needs the conditions that send it back for revision, written before the '
         'situation arrives.'),
    ]:
        m.bullet(label, body, after=16)

    m.section('EXPERIENCE')
    jobs = [
        ('CTO for the AI department and authorised electrical engineer (electrical and ventilation)',
         'Data Power Consultant ApS · Copenhagen · 2024 – present',
         'AI department 4-10 people · electrical and ventilation · full P&L · 5 electricians + 3 apprentices',
         [('Direction for the AI department',
           'Offering, target customers and architecture choices for a 4-10 person AI '
           'department, with investment cases for new services and monthly KPI follow-up on '
           'delivery and how the solutions were used by customers.'),
          ('Decision support with AI tools',
           'Python and Claude API for KPI dashboards, reporting and analysis; investment models '
           'with NPV, sensitivity and scenarios prepared as decision briefs and validated with '
           'technical review before use. Matrix leadership across two parallel organisations '
           'with one shared plan.')]),
        ('Owner / technical director / authorised electrical engineer',
         'ELOHVAC ApS · Copenhagen · May 2023 – November 2026 (company closed)',
         'Commercial customers · electrical, ventilation, climate · contracting · full P&L',
         [('Business development with full P&L',
           'Tenders, pricing and margin decisions against competitors, subcontractor and supplier '
           'agreements, and monthly budget follow-up with reserves and uncertainties listed.'),
          ('Growth and investment decisions',
           'Which services to sell, which equipment to buy and which cases to price, decided with '
           'the company\'s own capital at stake; documented productivity lift over 40% from '
           'AI-assisted calculation, planning and KPI reporting.')]),
        ('Senior commissioning engineer / project manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · November 2022 – July 2024',
         '37 CAPEX projects, DKK 2–10 mio. · 25 specialists · GMP/FDA/EMA',
         [('Analysis and reporting to leadership',
           'Monthly reporting to leadership and client management for 37 CAPEX projects, DKK '
           '2–10 mio. each: progress, cost, risks and resources condensed so decisions could be '
           'taken in the meeting. FAT/SAT and IQ/OQ/PQ under GMP/FDA/EMA, zero critical findings '
           'at handover.'),
          ('Cross-functional initiatives',
           '37 concurrent initiatives from concept to handover across engineering, procurement '
           'and operations; a PDCA programme that cut energy costs by 40%, with SAP ERP for cost '
           'and asset data and A3, 5 Whys and Ishikawa at problem level.')]),
        ('Project and workshop manager',
         'Ventek-Air · Copenhagen · January 2022 – November 2022',
         '11 concurrent projects · 14-person team · DKK 2–10 mio.',
         [('Capacity, pipeline and delivery',
           'Priorities across 11 concurrent projects and a 14-person team, capacity and progress '
           'follow-up on daily boards, and standardised work processes that lifted delivery '
           'performance measurably.')]),
        ('Maintenance and operations manager / workshop technician',
         'Biofos (Lynetten) · Copenhagen · August 2017 – January 2022',
         '24/7 operations · SCADA, PLC, HV switchgear · shift work',
         [('Critical utility operations',
           'Uptime, preventive maintenance and acute fault finding in 24/7 operations on pumps, '
           'HVAC, HV switchgear and SCADA; 5S, Standard Work and PDCA on workshop and store, and '
           'shift work with LOTO, risk assessment and APV as fixed disciplines.')]),
        ('Electromechanical technician / production team leader',
         'ARJ Engineering · Tehran · December 2003 – March 2010',
         '12 mechanics and technicians · machine shop · product line',
         [('Portfolio and business cases',
           'Product line responsibility for electric motors, pumps and submersible pumps: '
           'roadmap, business cases, development and launch plans, and pricing, margin and '
           'investment decisions across the lifecycle.'),
          ('Team leadership and root cause',
           'Leadership of 12 mechanics and technicians: shift planning, materials and goal '
           'management; fault diagnosis, root-cause analysis and corrective actions on '
           'industrial equipment.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=16)

    m.section('EDUCATION AND CERTIFICATIONS')
    m.edu('B.Tech (EQF6), Technology Management and Mechanical Engineering',
          'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7.6/12')
    m.edu('Authorised electrical engineer (LV/MV/HV)',
          'Danish Safety Technology Authority · May 2023')
    m.edu('Electrical and mechanical design, electrical engineering (EQF6)',
          'Tehran Technical University · 2000–2003')
    m.edu('PRINCE2, certified project manager', 'AXELOS / PeopleCert')
    m.edu('Refrigeration and air conditioning (AMU)',
          'Mercantec · 2021 · STCW 2021–2023, Danish Maritime Authority')
    m.para('Lean and Six Sigma as practice, not certification: DMAIC, 5S, PDCA, VSM (Value '
           'Stream Mapping), A3, Kaizen, Standard Work, SMED, TPM, 5 Whys, Ishikawa and FMEA, '
           'used in documented work on maintenance, quality and planning.', after=48)

    m.section('LANGUAGES, TOOLS AND PRACTICALITIES')
    m.para('English (professional working proficiency) · Danish (first language) · Persian '
           '(native). Tools: investment models with NPV, IRR, sensitivity and scenarios in Excel '
           'and Python; Power BI and KPI dashboards; SAP ERP; Claude API and Claude Code for '
           'analysis and documentation; PRINCE2 as project framework, and OKR and RACI for '
           'initiative ownership. Based in Måløv near Copenhagen; available at short notice.',
           after=48)

    m.section('THE FIRST 90 DAYS')
    for b in (
        'Days 1–30: read the corporate strategy, the board calendar and the market evidence '
        'behind the growth plan; map who owns which assumption; one-to-one conversations with '
        'the Director of Strategy, the existing Strategy Manager and the functions that own the '
        'inputs. No new analysis before the baseline is on the table.',
        'Days 31–60: the first decision brief on one growth question: market view, options, '
        'recommendation with NPV and sensitivity, and a session where assumptions are tested in '
        'the open. A one-page template for board preparation agreed with the Strategy team.',
        'Days 61–90: a business case standard the organisation can reuse, the preparation '
        'rhythm for the next Board cycle with owners and dates, and one strategic initiative '
        'launched from concept with a RACI for who decides and a written review trigger.'):
        m.bullet('', b, after=16)

    # ---------------------------------------------------------------- page 4
    m.page_break()
    m.models_table('THE ROLE AS ADVERTISED: WHAT I BRING', ('Requirement', 'Evidence'), [
        ("Lead the development and refinement of atNorth's corporate strategy, ensuring "
         "alignment with long-term business objectives",
         'Strategy work with capital at stake: roadmap, business cases and investment decisions '
         'for a product line at ARJ (2003-2010), and the direction of ELOHVAC and the Data Power AI '
         'department: offering, pricing, investment and resourcing aligned to multi-year goals.'),
        ('Keep a pulse on market trends, customer demand, competitor activity, technology '
         'developments, and broader industry dynamics to identify risks and opportunities',
         'Business development in competitive markets: pricing and tender work at ELOHVAC where '
         'offers competed on price and scope, demand and margin analysis for ARJ product lines, '
         'and a technology watch on AI and LLM developments feeding the Data Power offering '
         'since 2024.'),
        ('Translate market insights and business intelligence into strategic recommendations '
         'that support growth, competitiveness, and long-term value creation',
         'KPI dashboards, monthly reporting and decision briefs built with Python and Claude API '
         'since 2024; market and cost data turned into investment recommendations with NPV, '
         'sensitivity and '
         'scenarios before any decision, supporting long-term value creation rather than single '
         'deals.'),
        ('Partner with executives, business leaders, and functional teams to evaluate strategic '
         'initiatives and priorities across the organisation',
         'Matrix leadership of two parallel organisations with one shared plan; at Novo Nordisk, '
         'progress and resources for 37 projects were evaluated across engineering, procurement '
         'and operations with monthly reporting to leadership and client management.'),
        ('Support strategic planning, decision-making, and Board preparation activities '
         'alongside the Executive Committee and senior leadership team',
         'Decision material at ownership level: full P&L, budget follow-up and investment cases '
         'in own companies since 2023; monthly reporting to leadership and client management at '
         'Novo Nordisk, prepared so the decision could be taken in the meeting itself.'),
        ('Lead strategic projects and cross-functional initiatives from concept through '
         'implementation',
         '37 CAPEX projects, DKK 2–10 mio. each, from concept to handover with FAT/SAT and '
         'IQ/OQ/PQ; AI implementations at Data Power from requirements and architecture to '
         'go-live and handover; a PDCA programme delivering 40% lower energy costs.'),
        ('Develop compelling business cases, market assessments, and strategic presentations '
         'for senior stakeholders',
         'Business cases documented at ARJ (roadmap, pricing, margin, investment decisions) and '
         'in every ELOHVAC tender; presentations to leadership and client management every month; '
         'analysis and drafting with AI tools over 40% faster, with technical review before use.'),
        ("Support the development of power, sustainability, commercial, and geographic growth "
         "strategies that are critical to atNorth's long-term success",
         'Power and sustainability: electrical and energy engineering, 40% lower energy costs via '
         'PDCA at Novo Nordisk and critical power experience from Biofos. Commercial: full P&L, '
         'pricing and margin. Geographic growth analysis is a method I bring, not a prior role.'),
        ('Engage with internal and external stakeholders to gather insights that inform '
         'strategic planning and decision-making',
         'Stakeholder range documented since 2003: customers, subcontractors, suppliers, client '
         'leadership and internal teams across two organisations; insights gathered in 1:1s, '
         'tender work, joint reviews and monthly reporting cycles.'),
        ('Act as a trusted advisor and thought partner to senior leadership on strategic '
         'opportunities and challenges',
         'Advisory work documented as decision briefs and sparring: monthly reporting to Novo '
         'Nordisk leadership and client management, ownership-level decision material in own '
         'companies since 2023, and KPI analysis prepared before the meeting so advice arrived '
         'with its numbers.'),
        ("Bachelor's or Master's degree in Business, Economics, Engineering, Strategy, "
         "Industrial Management, or a related field",
         'B.Tech (EQF6) in Technology Management and Mechanical Engineering, 2017–2022, GPA '
         '7.6/12: engineering with industrial management and economics in one degree, at '
         "bachelor's level."),
        ('5+ years of experience in corporate strategy, management consulting, business '
         'development, strategic planning, or related disciplines',
         'Strategy work over 5+ years inside business ownership and technical leadership: '
         'business development and strategic planning at ELOHVAC and Data Power (2023 to '
         'present) and product portfolio strategy at ARJ (2003–2010). No consulting-firm '
         'background claimed.'),
        ('Demonstrated experience developing business strategies and influencing strategic '
         'decisions at a senior level',
         'Business strategies developed for own companies: offering, pricing, investment and '
         'resourcing for ELOHVAC and the Data Power AI department; senior decisions informed '
         'through documented business cases and monthly decision briefs at Novo Nordisk across 37 projects.'),
        ('Strong analytical and problem-solving capabilities with the ability to turn complex '
         'information into actionable recommendations',
         'A3, 5 Whys, Ishikawa and FMEA applied to technical and commercial problems; '
         'investment models with NPV, IRR, sensitivity and scenarios; data from 37 concurrent projects '
         'condensed to one-page decision recommendations.'),
        ('Experience presenting to executive leadership teams, boards, or senior decision-makers',
         'Presentations to senior decision-makers documented: monthly reporting and project '
         'reviews to Novo Nordisk leadership and client management, and ownership-level decision '
         'presentations in own companies since 2023.'),
        ('Excellent stakeholder management skills and the ability to influence without direct '
         'authority',
         'Influence without direct authority in matrix settings: priorities agreed across '
         'ELOHVAC and Data Power without owning both organisations, and coordination of 25 '
         'specialists across engineering, procurement and operations at Novo Nordisk.'),
        ('Strong communication and presentation skills with the ability to engage audiences '
         'ranging from operational teams to executives',
         'Communication range documented: floor-level coordination with 12 mechanics and '
         'technicians and a 14-person project team, through to leadership reporting; written and '
         'spoken Danish and English, spoken Persian.'),
        ('Professional proficiency in English',
         'English used as working language in documentation, tenders, international supplier '
         'correspondence and analysis workflows; the AI and analysis toolchain since 2024 runs '
         'in English, and this application and CV are written in English.'),
        ('Experience within the data center, energy, utilities, infrastructure, technology, or '
         'other capital-intensive industries is considered a strong advantage',
         'Capital-intensive industries documented: utilities (Biofos, critical wastewater '
         'infrastructure and energy), pharmaceutical manufacturing (Novo Nordisk, 37 CAPEX '
         'projects DKK 2–10 mio.), electrical and HVAC infrastructure (ELOHVAC) and technology '
         '(Data Power). Data centre experience is not claimed.'),
    ], widths=(3400, 6946), compact=True)

    m.para('**I can be reached on +45 93 99 95 14 or ajlooshahram@gmail.com,** and am ready to '
           'talk at short notice.', after=20)

    m.save(path, title='Strategy Manager - atNorth')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_atNorth_StrategyManager.docx')
    build(out)
    print(out)
