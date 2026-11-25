# -*- coding: utf-8 -*-
"""atNorth: Strategy Manager — v2 (25.11.2026, omskrivning efter brugerens rettelse).

v1 (scripts/build_atNorth_StrategyManager.py) bestod alle gates, men brugeren
læste teksten som AI-skrevet ("meget meget tydeligt at en AI har skrevet det").
v2 bruger samme form, samme dokumenterede indhold og samme gates, men skriver
uden AI-tællerne (master/README.md): ingen parallelle kæder, ingen bon mot-
kæder, ingen fede slogan-opsætninger, ingen konstruerede callbacks, ujævn
rytme, sammentrækninger, konkrete handlinger før generaliteter. Grænserne fra
v1 gælder uændret: intet management-consulting, bestyrelsesoplæg, corporate-
strategy-titel, datacenter- eller geographic-growth-strategi-påstande;
"intelligent" og "passionate" forekommer aldrig. v1-ladet urørt.
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
    lp('Shape atNorth\'s future, the headline says. Under it sits a more ordinary job: working '
       'out which assumptions the growth plan and its strategic direction rest on, testing them '
       'before anyone commits money, and putting recommendations in front of the CEO and the '
       'Board that can survive hard questions. atNorth, headquartered in Reykjavik, has eight '
       'data centers across the Nordics and more sites under development, in a Nordic data '
       'center market where decisions taken now show up as signed capacity years later. The '
       'posting lists ten responsibilities around that; strategy development, growth, power, '
       'sustainability, commercial development, and corporate strategy all end up on the same '
       'desk. Mainly it seems to be: identify opportunities, solve complex business challenges, '
       'and write down what we actually know before deciding.', after=44)

    lp('The posting calls the role a trusted advisor and thought partner to senior leadership. '
       'In practice that means several conversations that don\'t sound alike. The CEO will want '
       'to know which growth bets deserve capital and what each business case has to prove. The '
       'Board asks the opposite question: what could break this. Then come the business leaders, '
       'who mostly want to know whether the priorities fit the sites and the pipeline that are '
       'actually there, and the functional teams, who want to know who owns the next step. '
       'Meanwhile the market keeps sending signals nobody ordered: customer demand, competitor '
       'moves, technology developments. Getting that last one into the other four in time is '
       'most of the value.', after=44)

    lp('For the first 90 days I\'d keep it fairly simple. The first month goes to reading the '
       'corporate strategy, the board calendar and whatever market evidence sits behind the '
       'growth plan, and to talking with the people who own the inputs, including the Director '
       'of Strategy and the existing Strategy Manager. No new analysis before that baseline is '
       'on the table. Month two: one growth question, and the first decision brief on it. Market '
       'view, two real options, a recommendation with NPV and sensitivity, and a meeting where '
       'people try to break the assumptions. By month three I\'d want a business case template '
       'the organisation can reuse, a rhythm for the next Board cycle with owners and dates, and '
       'one initiative started from concept.', after=44)

    lp('A few things about atNorth caught my attention. The company describes itself as '
       'providing cost-effective, scalable high-density colocation and built-to-suit services, '
       'with sustainability at our core: renewable energy, circular economy principles, and '
       'reliable, secure, and high-performance infrastructure, with innovative design and power '
       'efficiency in how the sites run. Heavy capital and long lead times, in other words, '
       'which is exactly where strategy work earns its keep. The stated ambition, to help shape '
       'the future of sustainable digital infrastructure and stay at the forefront of the '
       'market, needs analysis that\'s honest about power, sustainability and timing when the '
       'strategic direction is set. Not just growth.', after=44)

    lp('The culture section deserves a word, because most of them don\'t. The posting says '
       'world-class technology with a people-first culture built on collaboration, ownership, '
       'and trust, and that curiosity, ownership, and impact are valued in an open, transparent, '
       'and inclusive culture. Fine words anywhere. What I liked was the detail: "We don\'t just '
       'talk about culture; we nurture it", with regular one-to-one engagements and monthly '
       'wellbeing surveys so that every voice is heard, and a weekly gathering, sometimes over a '
       'simple breakfast and good conversation, to shape a sustainable future together. The '
       'careers site has one line I keep coming back to: ask questions, challenge the status '
       'quo and take action. Having run teams through two companies at once and a closedown '
       'this autumn, I know the difference between a value poster and how people actually talk '
       'to each other.', after=44)

    lp('What I\'d bring is fairly concrete. I build business cases and financial modelling with '
       'DCF, NPV, IRR, sensitivity and scenarios, mostly in Excel and Python, and I use Claude '
       'Code for market analysis and drafting, which mainly means the numbers arrive sooner. '
       'The strategy work so far sat inside operational and ownership roles rather than a '
       'consulting firm: pricing jobs against competitors, deciding which equipment to buy, '
       'running a full P&L, writing the monthly report that client leadership at Novo Nordisk '
       'used when deciding on 37 projects. The posting asks for strategic thinking with '
       'practical execution, and for someone who can turn ambitious goals into tangible '
       'outcomes. That\'s the combination I recognise in my own work, even if the job titles '
       'look different.', after=44)

    lp('I realise this reads differently from a pure strategy CV. I\'d rather explain the path '
       'in a conversation than smooth it over here. If the fit looks interesting, I\'d like to '
       'talk about the assumptions behind the growth plan and what the first decision brief '
       'should cover. I live in Måløv, just outside Copenhagen, can start at short notice, and '
       'work in English, Danish and Persian. You can reach me on +45 93 99 95 14 or '
       'ajlooshahram@gmail.com.', after=16)

    m.meta('Kind regards', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, 'Strategy Manager · corporate strategy, growth and decision support',
                    CONTACT, 'PROFILE')
    m.para('Strategy Manager who keeps the assumptions behind the growth plan visible, tests '
           'them before money moves, and puts recommendations in front of the CEO and the Board '
           'that hold up under questioning. Engineering and business ownership underneath: '
           'B.Tech in technology management and mechanical engineering, a full P&L since 2023, '
           'and 37 CAPEX projects at Novo Nordisk with monthly reporting to leadership.',
           after=64)

    m.section('THE DECISION BRIEF: HOW I READ A STRATEGY QUESTION')
    for label, body in [
        ('The question',
         'I start from the decision that has to be made and the date it has to be made by. '
         'Everything after that is support.'),
        ('The assumptions',
         'Under every plan there are assumptions about demand, power, price and timing. I write '
         'them down early. A risk section that hides them is not much use.'),
        ('The options',
         'Two real options where I can get them, with cost and upside, and a note on what would '
         'make each of them wrong.'),
        ('The numbers',
         'NPV with sensitivity and scenarios, so people can see what happens when demand, price '
         'or lead time moves.'),
        ('Owner, date and trigger',
         'It ends with who does what by when, and the conditions that would send the plan back '
         'for another look.'),
    ]:
        m.bullet(label, body, after=16)

    m.section('EXPERIENCE')
    jobs = [
        ('CTO for the AI department and authorised electrical engineer (electrical and ventilation)',
         'Data Power Consultant ApS · Copenhagen · 2024 – present',
         'AI department 4-10 people · electrical and ventilation · full P&L · 5 electricians + 3 apprentices',
         [('Direction for the AI department',
           'I set the direction for a 4-10 person AI department: what we sold, to whom, how the '
           'solutions were built and how we knew they were used. Investment cases for new '
           'services, and KPI follow-up on delivery every month.'),
          ('Decision support with AI tools',
           'Python and Claude API for KPI dashboards, reports and analysis. Investment models '
           'with NPV, sensitivity and scenarios, written up as short decision briefs and checked '
           'by a person before use. All of it while running two organisations, ELOHVAC and Data '
           'Power, against one shared plan.')]),
        ('Owner / technical director / authorised electrical engineer',
         'ELOHVAC ApS · Copenhagen · May 2023 – November 2026 (company closed)',
         'Commercial customers · electrical, ventilation, climate · contracting · full P&L',
         [('Running the business',
           'Tenders, pricing and margin calls against competitors, agreements with subcontractors '
           'and suppliers, and a monthly budget follow-up where reserves and uncertainties were '
           'listed out in the open.'),
          ('Where the money went',
           'Which services to sell, which equipment to buy, which jobs to price; my own capital '
           'at stake in the answers. The AI tools we used for calculation, planning and KPI '
           'reporting lifted productivity by more than 40%.')]),
        ('Senior commissioning engineer / project manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · November 2022 – July 2024',
         '37 CAPEX projects, DKK 2–10 mio. · 25 specialists · GMP/FDA/EMA',
         [('What went to leadership',
           'A monthly report on 37 CAPEX projects, DKK 2–10 mio. each: progress, cost, risks and '
           'resources, condensed so a decision could be made in the meeting. FAT/SAT and IQ/OQ/PQ '
           'under GMP/FDA/EMA, and no critical findings at handover.'),
          ('Getting 37 things through',
           'Thirty-seven projects at once, from concept to handover, across engineering, '
           'procurement and operations. A PDCA programme cut energy costs by 40%. A3, 5 Whys and '
           'Ishikawa when something went wrong, and SAP ERP for the cost data.')]),
        ('Project and workshop manager',
         'Ventek-Air · Copenhagen · January 2022 – November 2022',
         '11 concurrent projects · 14-person team · DKK 2–10 mio.',
         [('Eleven projects and a workshop',
           'Priorities across 11 concurrent projects and a 14-person team, daily boards for '
           'capacity and progress, and standardised work processes that lifted delivery '
           'performance measurably.')]),
        ('Maintenance and operations manager / workshop technician',
         'Biofos (Lynetten) · Copenhagen · August 2017 – January 2022',
         '24/7 operations · SCADA, PLC, HV switchgear · shift work',
         [('Keeping a treatment plant running',
           'Uptime, planned maintenance and acute fault finding, around the clock, on pumps, '
           'HVAC, HV switchgear and SCADA. 5S, Standard Work and PDCA on the workshop and the '
           'store. Shift work with LOTO, risk assessment and APV as fixed disciplines.')]),
        ('Electromechanical technician / production team leader',
         'ARJ Engineering · Tehran · December 2003 – March 2010',
         '12 mechanics and technicians · machine shop · product line',
         [('A product line with real decisions',
           'Electric motors, pumps and submersible pumps: roadmap, business cases, development '
           'and launch plans, and pricing, margin and investment decisions across the lifecycle.'),
          ('Twelve mechanics and technicians',
           'Shift planning, materials and goal management, plus fault diagnosis and root-cause '
           'analysis when industrial equipment stopped.')]),
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
           '(native). For the analysis: investment models with NPV, IRR, sensitivity and '
           'scenarios in Excel and Python; Power BI and KPI dashboards; SAP ERP; Claude API and '
           'Claude Code, which I use daily; PRINCE2 for project structure, OKR and RACI when '
           'initiatives need owners. Based in Måløv near Copenhagen; available at short notice.',
           after=48)

    m.section('THE FIRST 90 DAYS')
    for b in (
        'Days 1–30: read the corporate strategy, the board calendar and the market evidence '
        'behind the growth plan. Find out who owns which assumption. Talk to the Director of '
        'Strategy, the existing Strategy Manager and the functions that own the inputs. Nothing '
        'new gets analysed before that baseline is on the table.',
        'Days 31–60: write the first decision brief on one growth question. Market view, two '
        'options, a recommendation with NPV and sensitivity, and a meeting where the '
        'assumptions get challenged. Agree a one-page template for board preparation with the '
        'Strategy team.',
        'Days 61–90: a business case standard the organisation can reuse, a preparation rhythm '
        'for the next Board cycle with owners and dates, and one strategic initiative started '
        'from concept, with a RACI for who decides and a written trigger for when the plan goes '
        'back on the table.'):
        m.bullet('', b, after=16)

    # ---------------------------------------------------------------- page 4
    m.page_break()
    m.models_table('THE ROLE AS ADVERTISED: WHAT I BRING', ('Requirement', 'Evidence'), [
        ("Lead the development and refinement of atNorth's corporate strategy, ensuring "
         "alignment with long-term business objectives",
         'I have done this with my own money on the line: the roadmap, business cases and '
         'investment decisions for a product line at ARJ (2003-2010), and setting the direction '
         'for ELOHVAC and the Data Power AI department, offering and resourcing included.'),
        ('Keep a pulse on market trends, customer demand, competitor activity, technology '
         'developments, and broader industry dynamics to identify risks and opportunities',
         'Pricing jobs in tenders at ELOHVAC meant following what competitors did and what '
         'customers would pay; at ARJ the demand and margin analysis sat on my desk. Since 2024 '
         'I have also tracked AI and LLM developments for the Data Power offering.'),
        ('Translate market insights and business intelligence into strategic recommendations '
         'that support growth, competitiveness, and long-term value creation',
         'KPI dashboards, monthly reports and short decision briefs, built with Python and '
         'Claude API since 2024. The step from data to recommendation is where I use investment '
         'models: NPV, sensitivity and scenarios before any decision, aiming at long-term value '
         'creation rather than single deals.'),
        ('Partner with executives, business leaders, and functional teams to evaluate strategic '
         'initiatives and priorities across the organisation',
         'Two parallel organisations, ELOHVAC and Data Power, run against one shared plan. At '
         'Novo Nordisk, progress and resources for 37 projects were evaluated across '
         'engineering, procurement and operations, with monthly reporting to leadership and '
         'client management.'),
        ('Support strategic planning, decision-making, and Board preparation activities '
         'alongside the Executive Committee and senior leadership team',
         'The decision material I have prepared sits at ownership level: full P&L, budget '
         'follow-up and investment cases in my own companies since 2023. At Novo Nordisk the '
         'monthly report went to leadership and client management, written so the decision '
         'could be made in the meeting.'),
        ('Lead strategic projects and cross-functional initiatives from concept through '
         'implementation',
         '37 CAPEX projects of DKK 2–10 mio. each, from concept through handover with FAT/SAT '
         'and IQ/OQ/PQ. At Data Power, AI implementations ran from requirements and architecture '
         'to go-live and handover. A PDCA programme delivered 40% lower energy costs.'),
        ('Develop compelling business cases, market assessments, and strategic presentations '
         'for senior stakeholders',
         'Business cases at ARJ, covering roadmap, pricing, margin and investment decisions, and '
         'a business case in every ELOHVAC tender. Presentations to leadership and client '
         'management every month. The AI tools make the drafting over 40% faster; a person still '
         'reviews before anything goes out.'),
        ("Support the development of power, sustainability, commercial, and geographic growth "
         "strategies that are critical to atNorth's long-term success",
         'Power and sustainability I know from the technical side: electrical and energy '
         'engineering, 40% lower energy costs at Novo Nordisk through PDCA, and critical power '
         'work at Biofos. Commercial is familiar from full P&L, pricing and margin. Geographic '
         'growth analysis is a method I bring, not a prior role.'),
        ('Engage with internal and external stakeholders to gather insights that inform '
         'strategic planning and decision-making',
         'Since 2003 I have worked with customers, subcontractors, suppliers, client leadership '
         'and internal teams, in two organisations at once for the past years. Insights came '
         'from 1:1s, tender work, joint reviews and the monthly reporting cycle.'),
        ('Act as a trusted advisor and thought partner to senior leadership on strategic '
         'opportunities and challenges',
         'The advisory work I have done shows up as decision briefs and sparring: the monthly '
         'reporting to Novo Nordisk leadership and client management, ownership-level material '
         'in my own companies since 2023, and KPI analysis prepared before the meeting so the '
         'advice carried its numbers.'),
        ("Bachelor's or Master's degree in Business, Economics, Engineering, Strategy, "
         "Industrial Management, or a related field",
         'B.Tech (EQF6) in Technology Management and Mechanical Engineering, 2017-2022, GPA '
         '7.6/12. Engineering with industrial management and economics in the same degree, at '
         "bachelor's level."),
        ('5+ years of experience in corporate strategy, management consulting, business '
         'development, strategic planning, or related disciplines',
         'More than five years of strategy work inside ownership and technical leadership: '
         'business development and strategic planning at ELOHVAC and Data Power from 2023, '
         'product portfolio strategy at ARJ from 2003 to 2010. To be clear: no consulting-firm '
         'background.'),
        ('Demonstrated experience developing business strategies and influencing strategic '
         'decisions at a senior level',
         'The strategies I have built were for my own companies: the offering, pricing, '
         'investment and resourcing of ELOHVAC and of the Data Power AI department. At Novo '
         'Nordisk the documented business cases and monthly briefs fed decisions across 37 '
         'projects.'),
        ('Strong analytical and problem-solving capabilities with the ability to turn complex '
         'information into actionable recommendations',
         'A3, 5 Whys, Ishikawa and FMEA when problems need structure, and investment models '
         'with NPV, IRR, sensitivity and scenarios when money is involved. Data from 37 '
         'concurrent projects condensed to one-page recommendations.'),
        ('Experience presenting to executive leadership teams, boards, or senior decision-makers',
         'Monthly reporting and project reviews to Novo Nordisk leadership and client '
         'management, and decision presentations at ownership level in my own companies since '
         '2023. Senior decision-makers, in other words; boards I have not presented to.'),
        ('Excellent stakeholder management skills and the ability to influence without direct '
         'authority',
         'Influence without direct authority is normal in matrix work: setting priorities across '
         'ELOHVAC and Data Power without owning both organisations, and coordinating 25 '
         'specialists across engineering, procurement and operations at Novo Nordisk.'),
        ('Strong communication and presentation skills with the ability to engage audiences '
         'ranging from operational teams to executives',
         'From the workshop floor, with 12 mechanics and technicians and a 14-person project '
         'team, to leadership reporting; the range is deliberate. Written and spoken Danish and '
         'English, spoken Persian.'),
        ('Professional proficiency in English',
         'English is my working language for documentation, tenders and international supplier '
         'correspondence, and the AI and analysis toolchain since 2024 runs in English. This '
         'application and CV are written in English.'),
        ('Experience within the data center, energy, utilities, infrastructure, technology, or '
         'other capital-intensive industries is considered a strong advantage',
         'Capital-intensive work is documented: utilities at Biofos, critical wastewater '
         'infrastructure and energy; pharmaceutical manufacturing at Novo Nordisk with 37 CAPEX '
         'projects of DKK 2–10 mio.; electrical and HVAC infrastructure at ELOHVAC; technology '
         'at Data Power. Data centre experience I do not have.'),
    ], widths=(3400, 6946), compact=True)

    m.para('**I can be reached on +45 93 99 95 14 or ajlooshahram@gmail.com,** and am ready to '
           'talk at short notice.', after=20)

    m.save(path, title='Strategy Manager - atNorth')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_atNorth_StrategyManager_v2.docx')
    build(out)
    print(out)
