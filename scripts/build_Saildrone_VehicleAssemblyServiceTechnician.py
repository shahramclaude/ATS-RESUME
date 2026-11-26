# -*- coding: utf-8 -*-
"""Vehicle Assembly & Service Technician — Saildrone, Copenhagen (English JD -> en-GB document).

4 sider i masterdesign: letter p1, CV p2-3, kravmatrix p4.
No named contact in the JD -> greeting "Dear Saildrone hiring team,".

STILVALG (style_guard godkendt, 3/3 skift mod #420 CBRE):
  register     = High standards at the waterline (hands-on · mission-ready · safety ·
                 clear communication · field reality)
  åbningsgreb  = AV (havets virkelighed som kvalitetsdommer: det, der er næsten rigtigt på
                 værkstedet, bliver forkert i søen; vaner, hænder og ærlige optegnelser)
  struktur     = Assemble, service, deploy (build · service · field deployment)

BRUGERENS KORREKTION + permanent regel: alt tekst humaniseret i letter OG CV, en-GB.
Ingen em dash. Brug sammentrækninger (I'm, don't, it's).

BRUGERBEKRÆFTET 25.11.2026 (ærlige grænser, må ikke pyntes):
  - PET clearance: ingen tidligere godkendelse, klar til processen, ingen forventede hindringer.
  - Maritimt: praktisk sejlads med rigging, mooring og boat handling + STCW. 30+ ft twin-engine
    towing IKKE bekræftet -> ærligt gap.
  - Truck/kran: ingen certifikater -> ærligt gap, willing to certify.
  - Rejse 50-75%: OK. Authorized to work in Denmark: ansat i DK siden 2017.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Saildrone · Vehicle Assembly & Service Technician'
BANNER_RESUME = 'Hands-on electro-mechanical service · assembly and field work'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('25 November 2026')
    m.meta('European Fleet Management · Vehicle Assembly & Service Technician')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Vehicle Assembly & Service Technician, Copenhagen',
           bold=True, color='1A1A1A')
    m.para('Dear Saildrone hiring team,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('On the bench, a connector that seats with a click is finished work. At sea, a month of '
       'salt can still find its way into it, and everything that was almost right in the '
       'workshop turns wrong in a swell. Saildrone vehicles spend extended deployments in '
       'demanding maritime environments, and the difference between a vehicle that comes home '
       'on its own power and one that comes home on a tow is made before launch: by hands, '
       'habits and honest records. That\'s the part of the job I know best.')

    lp('Saildrone is a maritime defense company and the global leader in autonomous unmanned '
       'surface vehicles, and you\'re looking for a hands-on technical leader who sets high '
       'standards, thrives in demanding field environments, and translates heavy industrial '
       'and marine experience into mission success. The Vehicle Assembly & Service Team '
       'constructs and services the USVs and trains others to do the same, and the role '
       'sits right between the people who use the product and the teams who design it. I\'ve '
       'worked in that gap for years: commissioning handovers where operations took over the '
       'equipment on a Tuesday, service calls where the customer wanted an answer the same '
       'day, and workshops where I taught apprentices how it is really done. "Mission-ready, '
       'safe, and reliable" is a standard I know from 24/7 utilities.')

    # NOTE: placeholder above is replaced below (kept build valid during drafting)
    lp('Mechanical and electrical have been my two hands since 2003. Electromechanical '
       'technician, electrician, then authorised electrical engineer (LV/MV/HV) and marine '
       'engineer. Maintaining, troubleshooting and repairing equipment on pumps, motors, HVAC, '
       'switchgear and process lines is the daily work, in field, shipyard or industrial '
       'settings. Instructions and diagrams I read before I open the cabinet, and the '
       'tools go from hand tools to rigging and lifting gear. The marine side is real for me '
       'too: STCW certification and practical sailing, rigging, mooring and boat handling '
       'outside the classroom.')

    lp('There are a few honest edges, and I\'d rather state them. I have not held a '
       'security clearance before, so the PET personnel security clearance would be new; I\'m '
       'ready to start the process and expect no obstacles, having worked on critical supply '
       'infrastructure and GMP-controlled projects for years. No formal forklift or crane '
       'certificates yet, and no towing hours behind a 30+ ft twin-engine powerboat. The '
       'certificates I\'ll happily get, and the powerboat part I\'d build up under your '
       'training and procedures. What I do bring: authorization to work in Denmark without '
       'sponsorship, and a confirmed yes to the 50-75% travel the role needs, across Nordic, '
       'EU and other operating locations.')

    lp('Copenhagen, a flat organizational structure and open communication with leadership '
       'suited me well before I read it in your advert; it\'s how the best workshops I know '
       'work. An ambitious, fast-paced Nordic culture with a technically-proficient group '
       'around me is the right place to keep learning. The role offers comprehensive onboarding and a '
       'clear path for professional growth, and the attractive salary and pension package '
       'with health insurance doesn\'t hurt. What matters most to me is the varied and '
       'exciting daily experience you describe: meaningful challenges and a chance to impact '
       'global autonomous operations, with production readiness and operational performance '
       'as the measure. I\'m service-minded by trade, and a service-minded approach has kept '
       'my contractual commitments on track so far.')

    lp('The first 90 days I have written as a plan on page 3 of the CV: assemble first, then '
       'service, then field deployment. I can start as soon as needed. One practical note: I '
       'work with AI coding tools daily (Python, Claude) and use them for checklists and '
       'documentation, which is also how I\'d develop technical repair content and service '
       'documentation for the team.', after=44)

    m.para('Kind regards,', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFILE')
    m.para('Hands-on electro-mechanical technician and marine engineer, 20+ years in the '
           'field. Assembly, service and fault finding on electro-mechanical systems in '
           'industrial, utility and shipyard-like settings: pumps, motors, HVAC, switchgear, '
           'SCADA and PLC. STCW-certified with practical sailing, rigging and mooring. Used to '
           'training others, documenting the work and standing in for the answer when '
           'something fails. Willing to travel 50-75%.', after=32)

    m.section('EXPERIENCE')
    jobs = [
        ('CTO for the AI department and authorised electrical engineer (electrical and ventilation)',
         'Data Power Consultant ApS · Copenhagen · 2024 – present (ELOHVAC electrical activities '
         'moved here in Nov. 2026)',
         'AI department 4-10 people · electrical service and contracting · 5 electricians + 3 apprentices',
         [('Repair and service', 'Electrical service and fault finding for commercial clients: '
           'panels, controls, automation and planned maintenance on electrical, ventilation and '
           'climate systems. Acute call-outs solved on site, the work written down afterwards.'),
          ('Team and tools', 'AI department of 4-10 people, investment cases and monthly KPI '
           'follow-up. Python and Claude API for dashboards, checklists and reports that the '
           'team actually uses.')]),
        ('Owner / technical director / authorised electrical engineer',
         'ELOHVAC ApS · Copenhagen · May 2023 – November 2026 (company closed)',
         'Commercial customers · electrical, ventilation and climate · contracting · full P&L · service agreements',
         [('Assembly and service', 'From acute call-outs to finished installations: assembly, '
           'panels, controls and fault finding on electrical, ventilation and climate systems. '
           'Scheduled and corrective maintenance in service agreements with response time, quality '
           'and delivery as targets.'),
          ('Contractors and commitments', 'Tenders and pricing, subcontractor and supplier '
           'agreements, monthly budget follow-up. Every commitment delivered as agreed, or the '
           'customer heard the reason from me directly.'),
          ('Teaching the trade', 'Led 5 electricians and 3 apprentices: daily planning, 1:1s, '
           'hands-on demonstrations and structured training. Safety follow-up with LOTO, APV '
           'and risk assessment at site start-up.')]),
        ('Senior commissioning engineer / project manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · November 2022 – July 2024',
         '37 CAPEX projects, DKK 2–10 mio. each · 25 specialists · GMP/FDA/EMA',
         [('Commissioning and repair', 'Process plants commissioned and tested after FAT/SAT and '
           'IQ/OQ/PQ under GMP/FDA/EMA, zero critical findings at handover. Fault finding on '
           'electrical and control systems along the way, root-cause reports when issues had to '
           'stay fixed.'),
          ('Plans and records', 'Commissioning schedules with test and handover, monthly report '
           'on progress, cost, risks and resources to leadership and client management. SAP ERP '
           'for accurate records. 25 specialists across engineering, procurement and operations.')]),
        ('Project and workshop manager', 'Ventek-Air · Copenhagen · January 2022 – November 2022',
         '11 concurrent projects · 14-person team · material logistics and subcontractors',
         [('Coordination', '11 concurrent projects and a 14-person team. Tenders, contract basis, '
           'subcontractors and safety documentation followed through, with daily boards for '
           'capacity and progress. Equipment and materials handled: loading, shipping '
           'preparation and relocation between sites.')]),
        ('Maintenance and operations manager / workshop technician',
         'Biofos (Lynetten) · Copenhagen · August 2017 – January 2022',
         '24/7 operations · SCADA, PLC, HV switchgear · shift work',
         [('Around the clock', 'Maintenance and operations on pumps, HVAC, HV switchgear, SCADA '
           'and PLC, 24/7. Planned and corrective maintenance, fault finding on electro-mechanical '
           'systems day and night, 5S and Standard Work in the workshop.'),
          ('Safety discipline', 'Shift work and on-call duty with LOTO, APV, risk assessment and '
           'near-miss reporting. Heavy components lifted, moved and replaced under safety '
           'controls; production kept running while we worked.')]),
        ('Electromechanical technician / production team leader',
         'ARJ Engineering · Tehran · December 2003 – March 2010',
         '12 mechanics and technicians · machine shop · product line',
         [('Workshop and diagnosis', 'Led 12 mechanics and technicians: shift planning, materials '
           'and goals. Fault diagnosis on industrial electromechanical equipment, root-cause '
           'analysis and corrective actions, plus loading and relocation of machinery in the shop.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('EDUCATION AND CERTIFICATIONS')
    m.edu('B.Tech (EQF6), Technology Management and Mechanical Engineering',
          'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7.6/12')
    m.edu('Authorised electrical engineer (LV/MV/HV)', 'Sikkerhedsstyrelsen (Danish Safety Technology Authority) · May 2023')
    m.edu('Electrical and mechanical design, electrical engineering (EQF6)',
          'Tehran Technical University · 2000–2003')
    m.edu('PRINCE2, certified project manager', 'AXELOS / PeopleCert')
    m.edu('Refrigeration and air conditioning (AMU)',
          'Mercantec · 2021 · STCW 2021–2023: engine-room watchkeeping (A-III/1), designated '
          'security duties (VI/6), ship security officer (VI/5), security awareness (VI/6-1), '
          'tankers (V/1-1, V/1-2), Danish Maritime Authority')

    m.section('COMPETENCES')
    m.bullet('Assembly and service', 'Vehicle-like assembly and service work: panels, controls, '
             'pumps, motors, HVAC, instrument panels and process equipment. Service instructions, '
             'diagrams and tools from hand tools to rigging and lifting gear.', after=10)
    m.bullet('Field operations', 'Field, shipyard and industrial settings, planned and acute. '
             'Deployment-style work away from home (commissioning in Kalundborg and Bagsværd, '
             'service across Copenhagen), and comfortable on docks and vessels with tools in hand.',
             after=10)
    m.bullet('Documentation and standards', 'PRINCE2 planning, accurate records and inventory '
             'practices, KS and handover packages. Technical repair content and standardised '
             'procedures written for others to follow: checklists, service documentation, digital '
             'routines in Python.', after=10)
    m.bullet('Team support', 'Training and leading electricians, apprentices and contractors. '
             'Explaining technical concepts to end users in plain language. Lean and Six Sigma '
             'practice, not certified: DMAIC, 5S, PDCA, VSM, A3, Kaizen, Standard Work, SMED, '
             'TPM, 5 Whys, Ishikawa and FMEA.', after=10)

    m.section('THE FIRST 90 DAYS')
    m.para('A plan you can hold me to:', after=8)
    m.bullet('Days 1-30 · Assemble', 'Learn the vehicle end to end by building and servicing it '
             'beside the team: procedures, safety requirements and records the Saildrone way. '
             'Goal: I can complete an assembly workflow and document it correctly.', after=10)
    m.bullet('Days 31-60 · Service', 'Take on service and repair tasks in the fleet, coordinate '
             'with contractors, and get the PET clearance process moving in parallel. Goal: '
             'service jobs closed on time, with findings written up clearly.', after=10)
    m.bullet('Days 61-90 · Deploy', 'Join a planned deployment or recovery, and bring back '
             'feedback on workflows, in-field assembly procedures and vehicle designs. Goal: '
             'one concrete improvement with a measurable effect on safety, consistency or efficiency.',
             after=10)

    m.section('LANGUAGES, TOOLS AND PRACTICAL')
    m.para('Danish (native) · English (professional, daily working language since 2017) · '
           'Persian (native). SAP ERP, SCADA, PLC, Power BI, Python and Claude API. PRINCE2. '
           'Driving licence B (manual). Practical sailing: rigging, mooring and boat handling, '
           'plus STCW certification. Authorised to work in Denmark. Based in Måløv. Available '
           'immediately, willing to travel 50-75%.', after=32)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Vehicle Assembly & Service · documented experience',
                   ('Requirement', 'Evidence'),
                   [
        ('assembly and service workflows for the Saildrone vehicle fleet',
         'Commissioning and handover of 37 projects (2022-2024) and service contracts with '
         'response-time targets (2023-2026). 5S and Standard Work from the Biofos workshop.'),
        ('mission-ready, safe, and reliable',
         '24/7 operations at Biofos: ready, safe and reliable when the shift needs it. Zero '
         'critical findings at Novo Nordisk handovers, zero critical deviations at ELOHVAC.'),
        ('solid mechanical and electrical skills to maintain, troubleshoot, and repair equipment',
         'Electromechanical technician since 2003, authorised electrical engineer (LV/MV/HV) '
         'since 2023. Fault finding and repair on pumps, motors, HVAC and switchgear.'),
        ('planned domestic and international deployment, recovery, and repair activities',
         'Field work in varied settings: commissioning at Kalundborg/Bagsværd (2022-2024), '
         'service in Copenhagen. Marine deployment is new; the planning discipline is not.'),
        ('explaining and demonstrating vehicle assembly and service procedures',
         'Trained and led electricians and apprentices (5+3) at ELOHVAC, hands-on '
         'demonstrations included. Explaining a procedure until others perform it, since 2010.'),
        ('Represent Saildrone professionally and constructively',
         'Customer-facing since 2023: commercial clients, supplier negotiations, monthly '
         'reports to client management at Novo Nordisk. A daily habit, not an outfit.'),
        ('assess current workflows, in-field assembly procedures, and vehicle designs',
         'Assessing how work is done and suggesting better ways: 5S/Standard Work at Biofos, '
         'digital checklists in Python (2024), PDCA at Novo Nordisk.'),
        ('increases safety, consistency, and overall efficiency',
         'PDCA cut energy costs by 40% at Novo Nordisk; standardised work and digital routines '
         'lifted productivity over 40% at Biofos and ELOHVAC. LOTO, APV at every start-up.'),
        ('5+ years of relevant experience applying electrical and mechanical skills',
         '20+ years of relevant experience, 2003-2026: machine shop, commissioning, 24/7 '
         'utilities, contracting. Electrical and mechanical skills used in all of it.'),
        ('service instructions, diagrams, and use tools from hand tools to rigging or heavy equipment',
         'Followed service instructions and diagrams since 2003, authorised by DS/HD 60364. '
         'Hand tools daily; rigging and lifting gear at Biofos and on installation jobs.'),
        ('third-party contractors, to deliver operational plans and contractual commitments',
         'Subcontractor coordination at Ventek (11 projects, 2022) and ELOHVAC (2023-2026): '
         'plans agreed, work inspected, commitments delivered, or the customer heard why first.'),
        ('explain technical concepts and product knowledge clearly to end users',
         'Explained technical concepts to end users daily since 2023: what failed, what it '
         'costs, what happens next. Monthly reports at Novo Nordisk trained the written part.'),
        ('Strong planning and documentation habits',
         'PRINCE2 since 2017, daily capacity boards at Ventek, accurate records and inventory '
         'practices in SAP ERP and service documentation at ELOHVAC.'),
        ('Eligibility to work in Denmark/EU',
         'Authorised to work in Denmark: employed here since 2017 (Biofos, Novo Nordisk, '
         'Ventek, ELOHVAC, Data Power), resident in Måløv. No sponsorship needed.'),
        ('typically 50–75%',
         'Typically 50-75% travel is fine by me, and I have confirmed it: commissioning travel '
         'to Kalundborg/Bagsværd, daily driving in service work, ready for Nordic and EU.'),
        ('Service-minded approach',
         'From the customer side of the counter since 2023: response times kept, updates given '
         'before being asked, solutions that hold after I leave.'),
        ('global OEM',
         'Complex field operations for large, quality-driven organisations: Novo Nordisk as a '
         'global pharma OEM (37 CAPEX projects) and contract work for industrial clients.'),
        ('technical repair content, service documentation, or standardized procedures',
         'Technical repair content and standardised procedures: KS checklists, service '
         'documentation and digital routines at ELOHVAC (2023-2026), root-cause reports at Biofos.'),
        ('systematically isolate, diagnose, and repair issues on electro-mechanical systems in a marine environment',
         'Systematic isolation and diagnosis on electro-mechanical systems: pumps, HV '
         'switchgear, SCADA and PLC at Biofos (2017-2022). STCW and sailing back the marine side.'),
        ('familiarity with rigging, mooring, and basic boat-handling principles',
         'Practical familiarity with rigging, mooring and boat handling: practical sailing '
         'beyond STCW certification (engine-room watchkeeping, 2021-2023). Steady on docks.'),
        ('heavy equipment loading, shipping preparation, offloading, and relocation',
         'Loading, shipping preparation and relocation of heavy equipment: material logistics '
         'at Ventek (11 projects), receiving at Novo Nordisk, machinery at ARJ.'),
        ('driving forklifts, lifting machines, and crane operation',
         'Honest gap: no forklift or crane certificates yet. I have handled lifting gear and '
         'heavy components since 2003, and I am ready to certify quickly before deployment.'),
        ('30+ ft twin-engine powerboats with vehicles in tow',
         'Honest gap: no towing hours behind a 30+ ft twin-engine powerboat yet. Practical '
         'sailing and boat handling are in place; towing I would build under your training.'),
        ('personnel security clearance through the Danish Security and Intelligence Service (PET)',
         'No prior security clearance, ready to start the PET process immediately. I expect no '
         'obstacles: critical infrastructure (Biofos) and GMP projects (Novo) since 2017.'),
                   ], widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo — application for Vehicle Assembly & Service Technician, '
                       'Saildrone')
    print(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_Saildrone_VehicleAssemblyServiceTechnician.docx'))
