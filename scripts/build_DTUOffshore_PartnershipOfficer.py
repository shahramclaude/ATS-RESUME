# -*- coding: utf-8 -*-
"""DTU Offshore — Partnership Officer, industry collaboration and research funding.

English deliverable (JD is English): task-first cover page + CV in one document.
Culture and role intel: master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md,
section on DTU Offshore (research 05.11.2026).
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Industry partnerships · Energy and offshore technology · From capability to funded collaboration'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('5 November 2026')
    m.meta('DTU Offshore · DTU Lyngby Campus · New Projects Director Charlotte Nørgaard Larsen')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Partnership Officer — industry collaboration and research funding', bold=True,
           color='1A1A1A')
    m.para('Dear Charlotte Nørgaard Larsen', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('Industry partnerships rarely fail because the science is not good enough. They fail because nobody '
           'translated the capability into the language the partner makes decisions in: which operational problem '
           'does this solve, what does it cost, what does the partner have to put in, when will there be something '
           'to show, and who owns what afterwards. A Partnership Officer is that translation — a person who can sit '
           'with a researcher in Lyngby and a technical director in Esbjerg in the same week and leave both with the '
           'same understanding of what has been agreed.', after=80)

    m.para('**The partnership system I would build has four parts, and it can be in place within the first quarter.** '
           'First, a partner map of the Danish energy ecosystem — utilities, developers, technology providers, '
           'consultancies, authorities and the industry bodies — segmented by what each of them needs to solve and '
           'what they are able to co-fund. Second, a one-page capability brief per conversation: the industry problem '
           'in their words, what DTU Offshore can actually do about it, what the partner must contribute, what the '
           'result looks like in twelve and twenty-four months, and an indicative cost. Third, a pipeline with named '
           'stages — first meeting, scoped project, funding route chosen, agreement signed — with an owner, a next step '
           'and a date on every entry, and a reason logged on the ones we lose. Fourth, a '
           'repeatable agreement routine with DTU\'s legal and technology transfer colleagues on IP, publication rights, '
           'confidentiality and background knowledge, so a negotiation takes weeks instead of quarters.', after=80)

    m.para('The funding routes I would work with are the ones that already sit around the centre: EUDP, the '
           'Innovation Fund Denmark and its missions, Horizon Europe consortia, the Danish Energy Agency programmes, '
           'and the contract-research and sponsorship model DTU Offshore was built on with the DUC partners. The centre has already run a CCS programme with TotalEnergies, BlueNord, '
           'Nordsøfonden and Ørsted, hosted an international summer school on underground hydrogen storage and runs a '
           'recurring CCS conference. What it needs is someone who turns those assets into the next five agreements.',
           after=80)

    m.para('What I bring is the commercial half of that job, with enough technical depth to be credible in the room. '
           'For three years I have run my own company with full P&L: quoting, pricing, contract negotiation, '
           'subcontractors and the consequences when a promise is not kept. I have worked '
           'inside a GMP-regulated pharmaceutical environment on 37 parallel capital projects with 25 specialists, '
           'where a missing signature stops a handover, and I have led maintenance and operations on a 24/7 utility '
           'plant handling wastewater, pumps, HVAC and high-voltage switchgear. That is where I learned what a '
           'utility\'s technical organisation actually worries about, and how long it takes them to make a decision. '
           'I am also a marine engineer by training, with STCW certificates in engine-room watch and ship safety — '
           'offshore operations are the environment I was educated for.', after=80)

    m.para('I will be plain about the two places where my profile does not match the posting. I do not hold a '
           'master\'s degree: my highest qualification is a B.Tech in Technology Management and Mechanical Engineering '
           'at EQF 6, plus the Danish authorisation as marine and electrical engineer. And I have not yet attracted '
           'research funding or built a consortium in my own name — my commercial results are contract research in '
           'the private-market sense: tenders won, agreements signed, projects delivered and renewed. If the degree '
           'is a formal requirement you cannot set aside, my application ends there, and I would rather you knew it '
           'from page one. If it is a proxy for technical judgment and the ability to close an agreement, then I '
           'would like the conversation, because that part I have done for twenty years.', after=80)

    m.para('The first ninety days are straightforward: weeks 1–2 with each research group to learn what is '
           'genuinely sellable and what is still too early; day 30 with a partner map and a pipeline of the twenty '
           'most relevant Nordic organisations, ranked by need, budget and relationship; day 60 with three capability '
           'briefs tested on real partners and one funding route chosen for a specific project; day 90 with the first '
           'scoped agreement in negotiation and a dashboard of meetings, opportunities, proposals and signed value.',
           after=80)

    m.para('DTU Offshore does not sell a product; it sells access to knowledge, facilities and decades of North Sea '
           'experience, in a field where the decisions are large and the timelines long. That is a harder sale than '
           'most, and the kind I find worth doing. '
           'DTU\'s own values describe the way I work: **innovation** as testing a new route instead of '
           'repeating the last one, **credibility** because a claim without evidence is worthless to an industrial '
           'partner, and **commitment** because partnerships die of neglect rather than rejection. The flat, '
           'trust-based culture at DTU fits someone who has run a small business: freedom with responsibility is '
           'the deal I am used to.', after=80)

    m.para('Practically: I live in Måløv, about 25 minutes by car from Lyngby, and I work in Danish, English and '
           'Persian. I am an active Claude coder and build my own tools in Python: pipeline overviews, partner and '
           'market screening, and business cases with NPV, IRR and sensitivity when a collaboration has to be priced. '
           'I would welcome the chance to walk you through how I would build the partner pipeline and the first three '
           'capability briefs.', after=80)
    m.meta('Kind regards', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('Commercial and technical professional with 20 years from the Danish energy, utility and process industry '
           '— full P&L and contract responsibility in his own company, 25 specialists led across 37 capital projects '
           'in GMP-regulated production, and operations leadership on a 24/7 wastewater and energy plant. Marine '
           'engineer by training with STCW offshore certificates. Translates technical capability into a commercial '
           'case: scope, cost, risk, ownership and what the partner gets in twelve months.', after=80)

    m.section('COMMERCIAL AND TECHNICAL RESULTS')
    for label, body in [
        ('Revenue and contracts',
         'Three years with full P&L in his own company: tenders, quotations, pricing, contract negotiation, '
         'subcontractor agreements and delivery obligations with commercial and industrial customers.'),
        ('Complex delivery',
         '37 parallel capital projects of DKK 2–10m with 25 specialists across engineering, procurement and '
         'operations; audited handovers with zero critical findings under GMP/FDA/EMA.'),
        ('Energy and utilities',
         'Operations and maintenance leadership on a 24/7 wastewater plant with pumps, HVAC, high-voltage switchgear '
         'and SCADA; a PDCA programme cut energy cost by 40 % in a GMP production environment.'),
        ('Technical credibility',
         'Authorised marine and electrical engineer (LV/MV/HV); STCW engine-room watch, ship safety officer and '
         'tanker certificates; electrical and mechanical design background; LOTO, APV and risk assessment in daily use.'),
        ('Digital and analysis',
         'Python and Claude tools for pipeline and KPI overviews, market and partner analysis, and business cases '
         'with NPV, IRR and sensitivity; measured productivity gain above 40 % in his own business.')]:
        m.bullet(label, body, after=30)

    m.models_table('TOOLS AND METHODS', ('Task', 'Tool and documented use'), [
        ('Partnership development',
         'Business development in the energy sector: partner mapping segmented by need, budget and relationship temperature; a one-page capability brief per '
         'conversation; pipeline stages from first meeting to signed agreement, with owner, next step and date.'),
        ('Value proposition',
         'Problem in the partner\'s own words, what the centre can deliver, what the partner contributes, result at '
         '12 and 24 months, indicative cost, and a written note of what is out of scope.'),
        ('Funding and agreements',
         'Working knowledge of EUDP, Innovation Fund Denmark, Horizon Europe and Danish Energy Agency routes; '
         'contract negotiation, delivery terms, confidentiality and IP split agreed in writing with DTU legal.'),
        ('Stakeholder management',
         'Stakeholder mapping and RACI, decision logs with owner and deadline, escalation ladder, and a fixed '
         'follow-up cadence per partner — with internal and external stakeholders from utilities, contractors, '
         'authorities and management.'),
        ('Technical grounding',
         'Energy systems and electrical safety (LV/MV/HV), thermodynamics and refrigeration, water and wastewater '
         'processes, offshore and marine operations, plus A3 and 5 Whys for root cause.'),
        ('Facilitation and coaching',
         'Workshops with researchers and partners to turn a capability into a scoped project; coaching colleagues '
         'new to industry dialogue with GROW and the situational leadership approach (SLII) I use with my own team.'),
        ('Analysis and reporting',
         'KPI trees, dashboards and one-page decision documents; NPV, IRR and scenario models; Python and Claude for '
         'data work. Danish native, English professional.')])

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director',
         'ELOHVAC ApS · Copenhagen, Denmark · May 2023–present',
         'Full P&L · 5 electricians and 3 apprentices · commercial and industrial customers',
         [('Commercial responsibility', 'Tenders, quotations, pricing, contract terms and margin follow-up; service '
                                        'agreements with response time, quality and delivery as KPIs; direct '
                                        'negotiation with customers and suppliers.'),
          ('Technical scope', 'Electrical installations, switchboards, control and energy systems for commercial and '
                              'industrial customers; documentation and handover to the customer\'s technical '
                              'organisation.'),
          ('People and safety', 'Daily planning, 1:1s, performance reviews, apprentice training, LOTO, risk '
                                'assessment and APV at every site start.')]),
        ('Senior Commissioning Engineer / Project Manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd, Denmark · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · DKK 2–10m each · GMP/FDA/EMA',
         [('Cross-functional delivery', 'Progress, cost, risk and resources across engineering, procurement and '
                                        'operations; decision points with named owners; monthly reporting to '
                                        'management and client.'),
          ('Regulated quality', 'FAT/SAT and IQ/OQ/PQ with zero critical deviations at handover; A3 and 5 Whys in '
                                'fault finding; PDCA programme cut energy cost by 40 %.')]),
        ('Maintenance and Operations Manager / Workshop Technician',
         'Biofos, Lynetten · Copenhagen, Denmark · Aug 2017–Jan 2022',
         '24/7 wastewater treatment · pumps, HVAC, high-voltage switchgear and SCADA · shift work',
         [('Utility operations', 'Preventive maintenance, urgent fault finding and spare-parts flow on a plant treating '
                                 'wastewater for the Copenhagen area; 5S, standard work and PDCA in daily use.'),
          ('Data and compliance', 'Operating data from SCADA used for planning and optimisation; LOTO, APV, risk '
                                  'assessment and near-miss reporting in shift operations.')]),
        ('Project and Workshop Manager',
         'Ventek-Air · Copenhagen, Denmark · Jan 2022–Nov 2022',
         '14 employees · 11 parallel construction projects',
         [('Contracts and delivery', 'Tenders, quotations, subcontractors, delivery terms and handover packages; '
                                     'daily board meetings and bottleneck analysis lifted delivery performance.')]),
        ('Electromechanical Technician / Production Team Leader',
         'ARJ Engineering · Tehran, Iran · Dec 2003–Mar 2010',
         '12 mechanics and technicians · machine workshop',
         [('Planning and customers', 'Shift planning, material control and target follow-up; fault diagnosis and '
                                     'corrective actions on industrial equipment for external customers.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        m.doc.paragraphs[-1].runs[0].text = 'Scope: '
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('EDUCATION AND CERTIFICATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering (EQF 6) — marine engineering',
          'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7.6/12')
    m.edu('Authorised marine and electrical engineer (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('Electrical and mechanical design, electrical engineering',
          'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('STCW certificates: engine-room watch (A-III/1), designated security duties (VI/6), ship security '
          'officer (VI/5), tanker familiarisation (V/1-1, V/1-2)', 'Danish Maritime Authority · 2021–2023')
    m.edu('Refrigeration and air conditioning · Lean practice (5S, PDCA, VSM, A3)', 'Mercantec 2021 · ongoing')

    m.section('LANGUAGES, PRACTICAL AND REFERENCES')
    m.para('Danish and Persian: native · English: professional, written and spoken (working language for all technical '
           'documentation and for project work in international teams) · Driving licence B · '
           'Lives in Måløv, about 25 minutes by car from DTU Lyngby · References from Novo Nordisk and Biofos on '
           'request · Prepared for the security and export-control screening mentioned in the posting.', after=70)

    m.models_table('WHAT THE ROLE ASKS FOR — MY EVIDENCE', ('Requirement', 'Evidence'), [
        ('Master\'s degree or higher in engineering or applied sciences',
         'Not held. B.Tech in Technology Management and Mechanical Engineering (EQF 6) plus Danish authorisation as '
         'marine and electrical engineer — stated plainly so it can be assessed early.'),
        ('Technical understanding of energy, offshore, CCS, hydrogen or storage',
         'Energy systems, high-voltage installations and energy optimisation in GMP production (−40 % energy cost); '
         'marine engineering with STCW offshore certificates; water processes from five years at Biofos. CCS and '
         'hydrogen would be learned from the centre\'s researchers.'),
        ('Several years in the energy sector or a technology-driven business',
         'Twenty years in Danish energy, utility and process industry: utility plant operations, energy projects in '
         'regulated production, and own company delivering electrical and energy work to industry.'),
        ('Success in attracting funding or selling technology development',
         'Commercial track record from own company — tenders won, contracts signed, agreements renewed — and 37 '
         'projects delivered under GMP. Research funding and consortium building are the part I have not done.'),
        ('Strategic partnerships and long-term stakeholder relationships',
         'Long-standing customer and supplier relationships built over three years of service contracts; '
         'stakeholder mapping and decision logs across utilities, contractors and authorities.'),
        ('Network in the energy industry',
         'Working network among Danish contractors, industrial customers, utility technical organisations and '
         'suppliers; not an academic network, and not yet at executive level across the whole sector.'),
        ('Communication with executives and researchers',
         'Negotiates contracts and delivery terms in Danish and English and writes the commercial documentation '
         'himself; reports to management and client on capital projects and puts decisions on one page.')])
    m.page_break()

    m.models_table('FIRST 90 DAYS — PARTNERS, PIPELINE, FIRST AGREEMENT', ('Period', 'What happens, and how it is measured'), [
        ('Week 1–2',
         'Meet every research group and both directors: what is ready for industry, what needs a partner to become '
         'ready, and which facilities can be shown. Read the current partner agreements and the last three years of '
         'EUDP and Innovation Fund applications to see what has worked and what has not.'),
        ('Day 30',
         'Partner map of Danish and Nordic utilities, developers, technology providers, consultancies and authorities '
         '— ranked by need, budget and relationship temperature. A pipeline of the twenty most relevant '
         'organisations, each with a named owner and a next step with a date.'),
        ('Day 60',
         'Three capability briefs written with the researchers and tested on real partners. One funding route chosen '
         'for a specific project and the application plan agreed with the research lead. Agreement checklist for IP, '
         'publication and confidentiality aligned with DTU legal.'),
        ('Day 90',
         'First scoped project in negotiation, a dashboard of meetings held, qualified opportunities, proposals '
         'submitted and signed value, and a written note on which segments respond and which do not.')])

    m.section('HOW I BUILD A PARTNERSHIP PIPELINE')
    m.para('Partnership work is a sales process with a long cycle, and it only works if it is treated like one. Every '
           'organisation on the map gets a record: who the technical entry point is, who controls the budget, what '
           'they are measured on this year, which of our capabilities touches that, and when we last spoke. Stages are '
           'simple and honest — contacted, met, scoped, funding route chosen, agreement in negotiation, signed, '
           'delivered, renewed. The aim is strategic alliances, not transactions. Nothing is allowed to sit in "in dialogue" for six months: either there is a next '
           'step with a date, or it is parked with a reason. I would rather run twenty relationships properly than '
           'sixty badly.', after=80)

    m.section('TRANSLATING RESEARCH INTO A VALUE PROPOSITION')
    m.para('Researchers describe what they can do; partners buy what it changes. So the brief starts on the partner\'s '
           'side of the table: the operational or regulatory problem, what it costs them today, and what a solution '
           'would be worth — in reduced downtime, lower chemical consumption, fewer interventions, a permit that can '
           'be obtained, or a decommissioning cost that falls. Only then does the science come in, described in terms '
           'of what can be tested, in which facility, over what period, and what the partner has to provide: samples, '
           'data, site access, co-funding or a person. If we cannot describe the outcome without jargon, the partner '
           'will not take it to their investment committee, and I would say so in the meeting rather than after it.',
           after=80)

    m.section('THE FUNDING LANDSCAPE')
    m.para('Different money wants different things. EUDP funds demonstration and applied energy projects with industry '
           'partners and expects a clear commercial pathway. Innovation Fund Denmark and its missions want '
           'societal impact and strong consortia. Horizon Europe wants European added value and partners from several '
           'countries. Contract research and sponsorship want a defined deliverable at a defensible price. The '
           'Partnership Officer\'s contribution is to pick the route that fits the maturity of the technology and the '
           'appetite of the partner — not to bend every idea towards the programme with the nearest deadline.', after=80)

    m.section('TECHNICAL GROUNDING — WHAT I CAN DISCUSS WITHOUT NOTES')
    m.para('Electrical energy systems and safety, high-voltage installations, protection and switchgear; energy '
           'optimisation and measurement in production; thermodynamics, refrigeration and heat pumps; pumps, '
           'separators and water treatment processes from five years on a wastewater plant; offshore and marine '
           'operations from a marine engineering education with STCW certificates. Energy storage and hydrogen sit '
           'close to that: the 2027 summer school already covers CO2 storage, underground hydrogen storage, '
           'compressed-air storage and geothermal in one programme. Where my knowledge stops — subsurface '
           'behaviour, geomechanics, caprock integrity, CO2 phase behaviour in chalk — I would be the person asking '
           'the researcher the question the partner will ask, and making sure the answer comes back in language the '
           'partner can use.', after=80)

    m.section('DIGITAL AND AI IN PARTNERSHIP WORK')
    m.para('I am an active Claude coder and build my own tools in Python: pipeline and CRM overviews that show what '
           'has moved this month, partner and market screening from public sources, and business cases with NPV, IRR '
           'and sensitivity when a collaboration has to be priced before it is proposed. In a centre with a '
           'portfolio of partners and a handful of funding deadlines a year, that is the difference between '
           'reporting what happened and knowing what to do next.', after=80)

    return m.save(path, title='Application and CV — Partnership Officer, DTU Offshore',
                  subject='Industry collaboration, research funding and energy partnerships',
                  keywords='partnership officer, industry collaboration, research funding, energy, offshore, CCS')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_DTUOffshore_PartnershipOfficer.docx')))
