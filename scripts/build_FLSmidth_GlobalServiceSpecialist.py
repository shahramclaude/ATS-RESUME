# -*- coding: utf-8 -*-
"""FLSmidth · Global Service Specialist - DO/Emico, Flotation PCV, DSG-3 (R29151).

Engelsk opslag -> engelsk dokument. Masterdesign (scripts/master_design.py):
brev side 1, CV side 2-3, kravmatrix side 4.

Kun fakta fra master-CV'et og brugerens svar 28.11.2026:
- rejse op til 70 %, høj højde (fysisk og medicinsk egnet, kan dokumenteres)
- Biofos: procesdrift og teknisk ansvar
- fortykkere, flotation, klaringsbassiner, cykloner, reaktorer: kun kendskab
- mekanisk montage af roterende udstyr: selv udført
- titel: maskinmester (marine engineering & technology management)
Ikke: kedelarbejde, kedelpas, B-4, ITIL, kryogenisk, Snowflake/Databricks, BC, Inventor/Vault.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
OUT_DIR = os.path.join(ROOT, 'output')
OUT = os.path.join(OUT_DIR, 'Shahram_Ajloo_FLSmidth_GlobalServiceSpecialist.docx')

NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Global Service Specialist · DO/EIMCO, Flotation, PCV, DSG-3'
BANNER_RESUME = 'Installation, commissioning and documented handover on process equipment'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('28 November 2026')
    m.meta('FLSmidth A/S · Copenhagen · requisition R29151')
    m.para('Dear FLS hiring team,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    def sub(text):
        p = m._p(spacing_after=20, spacing_before=60, line=260, justify=False, keep_next=True)
        m._run(p, text, bold=True, color='002B5C')
        return p

    # ------------------------------------------------------------ letter, page 1
    lp('FLS works as a performance partner to mining companies. Through full flowsheet '
       'technologies, aftermarket services and digital solutions, the aim is to improve recovery '
       'and maximise uptime. A thickener or flotation cell that starts late or runs below design '
       'costs the customer recovery for every hour it stands, so the first weeks on site decide a '
       'large part of the project. The Global Service Specialist sits where mechanical erection, '
       'I&C and the customer\'s operators meet. That interface is where this job is won or lost.')

    sub('Mechanical completion first')
    lp('Most startup problems on separation equipment trace back to a few mechanical details: '
       'drive alignment, levelness of the rake or the cell bank, strain in the piping, and '
       'whether the instrument signals match the mechanical state. Before power goes on, I '
       'would walk the unit with a punch list where every line carries a mechanical sign-off '
       'and an I&C sign-off. A line is closed only when both exist. Open items go to the '
       'customer in writing at the end of each shift, so nothing is discovered during the first run. '
       'That is how I see safe and efficient project execution in practice.')

    sub('Thickeners and flotation cells are new to me')
    lp('I have not worked on thickeners or flotation cells, and it is better to say so here '
       'than to find out on site. My hands-on work is with pumps, tanks, process piping and '
       'instrumentation, and with the test regimes that go with them: FAT, SAT and '
       'qualification of equipment in a regulated plant. I would start with the FLS '
       'commissioning procedures and the DO and Eimco manuals, read line by line, and test '
       'my understanding on the first unit with the FLS engineer beside me.')

    sub('Startup that holds when the specialist is not there')
    lp('As primary onsite representative, I know the handover has to work with or without me '
       'on the site. With up to 70 percent of the time abroad, that matters more than usual. Each commissioning step gets a record with the test, the reading, the person '
       'and the acceptance criterion. The operators get a short guide for the first shifts, '
       'built around the alarms and control sequences they will meet. Training follows the '
       'order in which the plant will be run. When something fails, it goes to engineering '
       'with the record attached, so the answer comes back with the same reference.')

    sub('Water and energy from the first run')
    lp('Recovery and uptime are not the only numbers. Energy and water use matter to the '
       'customer too, and FLS builds its offer around reducing energy and water consumption, '
       'which is part of sustainable mining operations. At the first stable '
       'operating point I would compare pump duty, the water balance and the air and reagent '
       'feed with the design figures, and report any gap before the plant is handed over. '
       'When the figures do not match, the cause is usually in the control logic or in the '
       'mechanical setup, and that is where I would look first. I would represent FLS with '
       'professionalism and integrity in every review with the customer, including the ones where '
       'the answer is not yet known.')

    sub('The first two weeks on a new site')
    lp('In the first week, the work is the handover pack: which drawings are current, which '
       'tags have changed and which spare parts are on the list. In the second week I walk '
       'the punch list with the customer. From the third week, the work follows the '
       'commissioning sequence, and the customer gets a one-page status showing what is '
       'closed, what is open and what blocks the next step. High-quality technical service means '
       'the customer never has to ask where the project stands.')

    lp('I can work to the travel pattern and the site conditions in the posting, including '
       'high-altitude sites. I am physically and medically fit for them, and I can document this '
       'for the work authorisation. The role asks me to work independently under demanding conditions, and I plan site work around that from the first day. I would welcome a conversation about the first units on '
       'your list and how the commissioning plan fits them.', after=44)
    lp('Yours sincerely', after=8)
    lp('Shahram Ajloo', after=8)

    # ------------------------------------------------------------ CV, pages 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFILE')
    m.para('Elautoriseret maskinmester (LV/MV/HV) with hands-on mechanical and electrical '
           'work from 24/7 industrial operation, GMP-regulated plants and electrical '
           'installations. Erection and alignment of rotating equipment such as pumps and '
           'gears, performed by me. Commissioning and acceptance testing with FAT, SAT and '
           'IQ/OQ/PQ, and documented handover. PRINCE2 certified. I have not worked on '
           'thickeners, flotation cells or mining sites, and the table below says where the '
           'gaps are.', after=32)

    m.section('ON-SITE WORK AND SOLUTIONS')
    tasks = [
        ('Erection and alignment',
         'Rotating equipment such as pumps and gears, erected and aligned by me, with checks '
         'before energising and the record kept with the unit.'),
        ('Pre-commissioning and commissioning',
         'FAT, SAT and IQ/OQ/PQ on tanks, process piping, instrumentation and electrical '
         'systems at Novo Nordisk, with zero critical deviations at handover.'),
        ('Startup and troubleshooting',
         'Root-cause work with 5 Whys, Ishikawa, FMEA and A3. Acute fault-finding on pumps, '
         'HVAC and high-voltage switchgear in 24/7 operation at Biofos.'),
        ('Documentation that the customer can run from',
         'Installation records and handover packs with KS documentation at Ventek-Air and '
         'ELOHVAC. Monthly reporting to management and the client at Novo Nordisk.'),
        ('Coordination of schedules and resources',
         '37 concurrent CAPEX projects at Novo Nordisk, DKK 2 to 10 million each, and 11 '
         'parallel projects with a 14-person team at Ventek-Air.'),
        ('Customer contact on site',
         'Service agreements with response time, quality and delivery KPIs at ELOHVAC, with '
         'daily customer contact and full P&L responsibility.'),
    ]
    for head, body in tasks:
        m.bullet(head, body, after=24)

    m.section('EXPERIENCE')
    jobs = [
        ('CTO for the AI department and electrically authorised marine engineer, electrical and ventilation',
         'Data Power Consultant ApS · Copenhagen · 2024 to present',
         [('', 'Responsible for the AI and AI coding department, 4 to 10 people. Electrical and '
               'ventilation work, including the electrical activities from ELOHVAC since November '
               '2026, with full P&L responsibility.'),
          ('', 'Implementation of technical and industrial applications for customers: '
               'requirements, architecture, integration with existing systems, commissioning and '
               'handover to the customer\'s own operation.'),
          ('', 'AI coding for the design of technical installations and industrial components, '
               'with calculations and design variants checked by engineering review before they '
               'left the team.'),
          ('', 'Matrix leadership of two parallel organisations, ELOHVAC and Data Power, with one '
               'shared plan and written priorities.'),
          ('', 'Managing 5 electricians and 3 apprentices day to day. Akkord and measurement of '
               'completed work.')]),
        ('Owner and technical director, electrically authorised marine engineer',
         'ELOHVAC ApS · Copenhagen · May 2023 to November 2026 (company closed)',
         [('', 'Electrical work for commercial customers: installation, panels, control, '
               'fault-finding and preventive maintenance, from emergency call-outs to handed-over '
               'installations.'),
          ('', 'Tendering, cost calculation, subcontractors, KS documentation and handover records '
               'in all contracts.'),
          ('', 'LOTO, risk assessment and APV at each site start. No critical deviations in the '
               'service agreements.')]),
        ('Senior commissioning engineer and project manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg and Bagsværd · November 2022 to July 2024',
         [('', '37 concurrent projects with progress, budget and risk, across engineering, '
               'procurement and site.'),
          ('', 'Cross-functional leadership of 25 specialists. FAT/SAT and IQ/OQ/PQ under GMP, FDA '
               'and EMA requirements, with zero critical deviations at handover.'),
          ('', 'Electrical systems with panels and control, UPS, emergency and panic lighting, '
               'access control and PDS. Fault-finding with A3, 5 Whys and Ishikawa.'),
          ('', '40 % lower energy costs through a PDCA programme. SAP ERP for finance and asset cost.')]),
        ('Project and workshop manager',
         'Ventek-Air · Copenhagen · January 2022 to November 2022',
         [('', '11 concurrent installation projects from specification to formal handover, while '
               'managing a 14-person team day to day.'),
          ('', 'Tendering, subcontractors, contract basis, safety documentation and handover '
               'packs. Board meetings and bottleneck analysis.')]),
        ('Maintenance and operations manager, workshop technician',
         'Biofos (Lynetten) · Copenhagen · August 2017 to January 2022',
         [('', 'Operation and maintenance of pumps, HVAC, high-voltage switchgear and SCADA in 24/7 '
               'operation, with preventive maintenance and acute fault-finding.'),
          ('', 'Responsibility for process plant equipment at a water treatment plant, alongside '
               'shift operation.'),
          ('', 'Shift work under LOTO, risk assessment, APV and near-miss reporting. 5S, Standard Work '
               'and PDCA in the workshop and stores.')]),
        ('Electromechanic and production team leader',
         'ARJ Engineering · Tehran · December 2003 to March 2010',
         [('', 'Led 12 mechanics and technicians in the workshop: shift planning, materials and '
               'targets.'),
          ('', 'Fault diagnosis and repair of industrial electrical and mechanical equipment, with '
               'root-cause analysis and corrective action.'),
          ('', 'Product responsibility for a production line of electric motors, pumps and submersible pumps.')]),
    ]
    for title, meta, bullets in jobs:
        m.job(title, meta)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('EDUCATION AND AUTHORISATIONS')
    m.edu('Maskinmester (marine engineering & technology management)',
          'Copenhagen School of Marine Engineering & Technology Management · 2017 to 2022')
    m.edu('Electrical and Mechanical Engineering Design, electrical engineering (EQF6)',
          'Tehran Technical University · 2000 to 2003')
    m.edu('Elautoriseret maskinmester (LV/MV/HV)',
          'Danish Safety Technology Authority (Sikkerhedsstyrelsen) · May 2023')
    m.edu('PRINCE2, certified', 'AXELOS / PeopleCert')
    m.edu('Refrigeration and air conditioning (AMU)', 'Mercantec · 2021')
    m.edu('STCW: engine room watchkeeping, safety and tanker qualifications',
          'Danish Maritime Authority · 2021 to 2023. Maritime certificates, not boiler qualifications')
    m.para('Lean and Six Sigma methods applied in practice, not certified: DMAIC, 5S, PDCA, VSM, '
           'A3, Kaizen, Standard Work, SMED, TPM, 5 Whys, Ishikawa and FMEA.', after=48)

    m.section('SKILLS')
    m.models_table('Tools and systems', ('Area', 'Tools'), [
        ('Installation and commissioning', 'FAT, SAT, IQ/OQ/PQ, alignment, pre-commissioning checks, punch lists'),
        ('Fault-finding', 'FMEA, Ishikawa, 5 Whys, A3, PDCA, SCADA'),
        ('Documentation', 'Installation records, commissioning reports, KS documentation, RACI, SAP ERP'),
        ('Project and economics', 'PRINCE2, NPV/IRR, budget and schedule control, scenario analysis'),
        ('Data and AI', 'Python, Power BI, Excel, Claude API, Claude Code'),
        ('Safety and quality', 'LOTO, risk assessment, APV, near-miss reporting, GMP, FDA, EMA'),
    ], widths=(3400, 6946), compact=True)
    m.para('Danish native. English professional, written and spoken, used as the working language '
           'in international projects since 2017. Persian native. Driving licence B, manual gearbox.',
           after=40)

    # ------------------------------------------------------------ requirements matrix, page 4
    m.page_break()
    m.section('REQUIREMENTS MATRIX')
    rows = [
        ('Execute onsite erection, installation, alignment, and commissioning of mechanical systems and I&C activities for thickeners, flotation cells, and related separation equipment.',
         'Erection and alignment of rotating equipment, pumps and gears, done by me. Mechanical and I&C commissioning on tanks and process piping at Novo Nordisk, 2022 to 2024. Thickeners and flotation cells: not worked on yet.'),
        ('Lead pre-commissioning and commissioning processes to ensure equipment meets design, safety, and performance requirements.',
         'FAT, SAT and IQ/OQ/PQ under GMP, FDA and EMA at Novo Nordisk, 2022 to 2024, with zero critical deviations at handover. Punch lists with a sign-off per line are the method I would apply on FLS units.'),
        ('Support operational startup, troubleshooting, and optimization of equipment performance.',
         'Fault-finding with A3, 5 Whys, Ishikawa and FMEA at Novo Nordisk. 24/7 fault-finding on pumps and HVAC at Biofos. 40 % lower energy costs through a PDCA programme.'),
        ('Conduct inspections, testing, calibration, and verification of mechanical and control-related systems.',
         'Inspection and verification of panels, control, UPS and emergency lighting at Novo Nordisk, 2022 to 2024, and SCADA monitoring at Biofos, 2017 to 2022. Instrument calibration records are not part of my documented work.'),
        ('Coordinate onsite project activities, schedules, and resources to ensure timely completion.',
         '37 concurrent CAPEX projects at Novo Nordisk, DKK 2 to 10 million each, with progress, budget and risk. 11 parallel projects with a 14-person team at Ventek-Air in 2022.'),
        ('Collaborate with engineering, manufacturing, and project management teams to resolve technical issues.',
         'Coordination across engineering, procurement and site at Novo Nordisk. Board meetings and bottleneck analysis at Ventek-Air. Subcontractor and contract coordination in all ELOHVAC jobs.'),
        ('Prepare accurate and professional documentation, including installation records, commissioning reports, and service summaries.',
         'Installation records and handover packs with KS documentation at Ventek-Air in 2022 and ELOHVAC from 2023 to 2026. Monthly reports to management and client at Novo Nordisk, in Danish and English.'),
        ('Maintain compliance with all safety, quality, and regulatory standards.',
         'LOTO, risk assessment and APV at Biofos from 2017 to 2022 and at ELOHVAC, 2023 to 2026. GMP, FDA and EMA requirements under IQ/OQ/PQ at Novo Nordisk, with no critical deviations at handover.'),
        ('Serve as the primary onsite point of contact for customers, providing training, guidance, and technical support.',
         'Customer contact on site in ELOHVAC service agreements with response time and quality KPIs. Training of my own team of 5 electricians and 3 apprentices. Training of customer operators is new to me.'),
        ('Represent FLS with professionalism and integrity in all customer interactions.',
         'Service agreements with response time, quality and delivery KPIs, held with full P&L responsibility at ELOHVAC from May 2023 to November 2026. Written handover records for every customer delivery.'),
        ('Strong mechanical background with hands-on experience in Installation & Commissioning (I&C) of industrial process equipment.',
         'Maskinmester in marine engineering and technology management, 2017 to 2022, and an electrical engineering degree from Tehran, 2000 to 2003. I&C on tanks, process piping and instrumentation at Novo Nordisk, and control and panels at Biofos.'),
        ('Experience with thickeners, flotation cells, clarifiers, cyclones, pumps, reactors, or similar industrial equipment.',
         'Pumps from 24/7 operation at Biofos and from the ARJ production line. Thickeners, flotation cells, clarifiers, cyclones and reactors: knowledge only, no hands-on experience.'),
        ('Demonstrated ability to work independently and make informed decisions under pressure.',
         'Acute 24/7 fault-finding at Biofos and emergency call-outs at ELOHVAC from the call to closure. Decisions on site documented with risk assessment at each start.'),
        ('Strong project management skills, including planning, coordination, and documentation.',
         'PRINCE2 certified. Project and workshop management at Ventek-Air with 11 concurrent projects. Budget and schedule control for CAPEX projects at Novo Nordisk.'),
        ('Excellent written and verbal communication skills, including the ability to produce high-quality technical reports.',
         'Technical and management reports at Novo Nordisk. Handover reports and KS documentation in Danish and English. English used as working language since 2017.'),
        ('Ability and willingness to travel internationally up to 70% of the time.',
         'Ready to travel internationally up to 70 percent of the time, as stated in this application, and to work the site rotation the project needs.'),
        ('Professional demeanor with the ability to represent the company effectively onsite.',
         'Leadership of teams on changing sites at ELOHVAC, with situational leadership and written risk assessment at each start. Customer-facing work on service contracts.'),
        ('Experience in commissioning or startup of industrial process systems.',
         'Commissioning and startup of tanks, process piping, instrumentation and electrical systems at Novo Nordisk under GMP, with FAT, SAT and IQ/OQ/PQ records.'),
        ('Background in mining, minerals processing, water treatment, or heavy industrial environments.',
         'Water treatment: 24/7 operation at a water treatment plant at Biofos, with process plant equipment responsibility. Industrial plant at ARJ. No mining or mineral processing experience.'),
        ('Multilingual capabilities or experience working in multicultural settings.',
         'Danish native, Persian native, English professional. English working language in international projects since 2017, and international teams at Novo Nordisk.'),
        ('Ability to meet all medical and physical fitness requirements necessary to obtain work authorization for high-altitude job sites.',
         'Physically and medically fit for high-altitude sites, and able to provide the medical and physical documentation that work authorisation requires.'),
        ('Technical proficiency in mechanical systems and industrial equipment',
         'Pumps, tanks, process piping, HVAC and high-voltage switchgear in operation. Mechanical design training from Tehran and B.Tech studies. Workshop work from 2003 to 2010 on industrial equipment.'),
        ('Strong problem-solving and decision-making abilities',
         'Root-cause analysis with 5 Whys, Ishikawa, FMEA and A3 at Novo Nordisk and Biofos, and in workshop fault diagnosis at ARJ Engineering.'),
        ('Customer service orientation',
         'Service agreements with response time, quality and delivery KPIs at ELOHVAC. Customer handover packs at Ventek-Air and ELOHVAC.'),
        ('Professional communication and reporting skills',
         'Reporting to management and client at Novo Nordisk. Status and board meetings at Ventek-Air. Written handover reports in Danish and English.'),
        ('Ability to perform effectively in high-pressure environments',
         'Shift operation and acute fault-finding in 24/7 operation at Biofos. Emergency call-outs and handover deadlines at ELOHVAC and Ventek-Air.'),
        ('Self-motivation and independence in field operations',
         'Own planning and risk assessment at each site start at ELOHVAC, with situational leadership on changing building sites. Independent work on electrical and mechanical systems at customer sites.'),
    ]
    m.models_table('Job requirements and my documented evidence', ('Requirement', 'Evidence and status'),
                   rows, widths=(3600, 6746), compact=True)

    m.save(path, title='Global Service Specialist - FLSmidth',
           subject='Application Global Service Specialist, DO/EIMCO, R29151')
    print(path)


if __name__ == '__main__':
    os.makedirs(OUT_DIR, exist_ok=True)
    build(OUT)
