# -*- coding: utf-8 -*-
"""Technical Supervisor — CBRE, Hørsholm, Job ID 305257.

Engelsk opslag -> EN-GB dokument i masterdesign (4 sider): brev side 1,
CV side 2-3, kravmatrix side 4. Intet kontaktnavn i opslaget ->
"Dear Hiring Manager,". Ingen lokation-bekræftelse fra brugeren -> lokation
(Hørsholm) nævnes kun neutralt som site, aldrig som kørsel/flytning.

SAMME-FIRMA-REGLER: CBRE er genansøgning (flere tidligere: BusinessDevelopment,
MaintenanceManager_Billund, TechnicalLead_Jylland, TechnicalManager_Aarhus,
TechnicalSupervisor m.fl.) -> intet genbruges; alt indhold skrevet friskt
til 305257. Filnavnet har job-id for at skille fra tidligere CBRE-dokument.

STILVALG (style_guard godkendt, 3/3 skift mod #439 WSA):
  register    = Sikker udførelse af andres arbejde
  åbningsgreb = BP (arbejdstilladelsen først: intet arbejde starter før den
                er i orden)
  struktur    = Sikkerhed, anlæg, service (30/60/90 = the safety baseline ·
                the assets · the service)

ÆRLIG POSITION: permit-to-work/LOTO/APV = REEL (Biofos, skiftehold siden 2017).
CMMS = REEL. Eksterne entreprenører = REEL (Ventek underleverandører, Hansen
leverandørkontrakter). Laboratorieudstyr = Novo (laboratorie- og procesudstyr).
Soft services (cleaning/vending/waste/plants) = ny kategori, kontraktstyringen
overført (kort ærlig note i matrix rk17). Ingen fabrikationer.

BRUGERENS KORREKTION: humaniseret brev OG CV. Ingen em dash. Ingen forbudte
ord som egne påstande. Engelsk: sammentrækninger bindende.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_WSA_SeniorManagerStrategyRDInnovation.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'CBRE · Technical Supervisor, Hørsholm · Job ID 305257'
BANNER_RESUME = 'TECHNICAL SUPERVISION · HSE · MAINTENANCE · CONTRACTORS'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('26 November 2026')
    m.meta('Job ID 305257 · BOE Segment · Hørsholm')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Technical Supervisor, CBRE', bold=True, color='1A1A1A')
    m.para('Dear Hiring Manager,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('On a site with laboratory equipment, no work starts before the permit '
       'is in order. A work permit sounds like paperwork until the day when the '
       'difference between a good shift and an accident lies exactly there: in '
       'whether the requirements were followed before the tools came out. The '
       'Technical Supervisor at CBRE holds that line, ensuring the timely, '
       'effective, and safe execution of technical work while external '
       'contractors carry out the maintenance and repair of laboratory '
       'equipment, buildings, and technical installations.')

    lp('CBRE is the world’s largest commercial real estate services and '
       'investment firm and a provider of critical infrastructure services, '
       'with more than 155,000 employees serving clients in more than 100 '
       'countries. The Building Operations & Experience segment is where this '
       'role sits, at a client site in H\u00f8rsholm, and the brief is concrete: '
       'availability, reliability, and performance of technical assets and '
       'building systems, where issues are identified and resolved promptly, by '
       'in-house team or through specialist contractors. The same desk runs '
       'several outsourced soft services on agreed service standards and serves '
       'as point of contact for both the client and internal stakeholders.')

    lp('Safety and permits are familiar ground. Six years in 24/7 operations at '
       'Biofos meant work permits, LOTO and risk assessments as part of every '
       'shift, with contractor adherence to all safety regulations and '
       'procedures monitored closely. Preparing and issuing work permits, '
       'checking compliance with permit requirements and closing the loop '
       'afterwards is routine I’ve kept since 2003, and keeping a safe '
       'working environment through that system is the craft. The technical '
       'side runs alongside it: building systems, maintenance processes, and '
       'fault diagnosis across HVAC, ventilation, electrical installations, '
       'pumps and process piping, with SCADA and PLC in the picture.')

    lp('The first 90 days follow the three things the role protects. Days 1-30 '
       'set the safety baseline: the HSE Permit-to-Work system read end to end, '
       'contractor routines checked against compliance with relevant '
       'legislation, safety regulations, and CBRE/client procedures, and every '
       'open permit visible in one place. Days 31-60 are for the assets: '
       'availability, reliability, and performance of technical assets and '
       'building systems baselined, preventive and corrective maintenance '
       'placed on one schedule, and Computerized Maintenance Management Systems '
       '(CMMS) data made trustworthy. Days 61-90 turn to the service: the '
       'outsourced soft services measured on agreed service standards, '
       'improvements identified and implemented in maintenance practices, and '
       'monitor service quality in one rhythm toward optimal service delivery.')

    lp('The desk sits between people every day: lead and support technicians '
       'and contractors on a day-to-day basis, act as primary point of contact '
       'for the client, suppliers, and internal stakeholders, and manage '
       'multiple priorities simultaneously without the communication slipping. '
       'Communication and stakeholder management in fluent Danish and English, '
       'written and spoken, is the working language. Reports, maintenance '
       'schedules, and technical documentation get prepared and managed as part '
       'of the job, not after it, and when equipment failures and complex '
       'technical issues land, I’m the one who shows up with a plan and stays '
       'until it runs.')

    lp('The things this role asks for are daily work for me: a safe, efficient, '
       'and compliant workplace kept running through shifts and audits, '
       'operational excellence kept as the normal standard, and service quality '
       'monitored while continuous improvement stayed on the agenda. '
       'Contributing to a positive, inclusive, and safe working environment and '
       'promoting CBRE’s RISE values fit how I lead; the client objectives are '
       'met when the team is safe and the contractors are aligned. I can start '
       'by agreement, and I look forward to hearing from you.', after=44)

    m.para('Kind regards', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFILE')
    m.para('Technical supervisor with 20+ years in maintenance, facilities and '
           'technical service, most of it in regulated, 24/7 environments. '
           'Permit-to-work, LOTO and contractor safety as daily discipline '
           '(Biofos 2017-2022); laboratory and process equipment at Novo '
           'Nordisk; HVAC, electrical and building systems seen from both the '
           'client side and the contractor side. CMMS data treated as part of '
           'the job, not paperwork after it.', after=32)

    m.section('PROFESSIONAL EXPERIENCE')
    jobs = [
        ('CTO, AI Department & Authorised Electrical Engineer (LV/MV/HV)',
         'Data Power Consultant ApS · Copenhagen · 2024 – present (from Nov. 2026 '
         'also ELOHVAC\u2019s electrical activities)',
         'AI department 4-10 people · electrical service and enterprise · '
         'contractor coordination',
         [('Electrical work and contractors', 'Electrical service and enterprise '
           'planned, executed and handed over with the same discipline as on a '
           'site: permits and safety checks before tools, quality control at '
           'handover, and specialist contractors coordinated on schedules and '
           'standards. Documentation prepared and managed along the way.')]),
        ('Owner / Technical Director / Authorised Electrical Engineer',
         'ELOHVAC ApS · Copenhagen · May 2023 – Nov. 2026 (company closed)',
         'Business customers · electrical, ventilation and climate · full P&L · '
         'service agreements',
         [('Service agreements and follow-up', 'Service agreements for business '
           'customers run on agreed standards: planned visits, fault response '
           'and follow-up on quality, with 5 electricians and 3 apprentices in '
           'the field and external suppliers on contract. Compliance with '
           'safety rules and technical legislation on every job, and clients '
           'kept informed when plans changed.')]),
        ('Senior Commissioning Engineer / Project Manager, Electrical Systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · Nov. 2022 – Jul. 2024',
         '37 CAPEX projects · laboratory and process equipment · GMP/FDA/EMA',
         [('Laboratory and process equipment', 'Laboratory equipment, climate '
           'chambers, walk-in coolers and process installations taken from '
           'construction through FAT/SAT and IQ/OQ/PQ into use, with '
           'documentation that withstood revision. Strict permit and safety '
           'regimes, hygienic zones, and 25 specialists and contractors '
           'coordinated across the work.')]),
        ('Project & Workshop Manager',
         'Ventek-Air · Copenhagen · Jan. 2022 – Nov. 2022',
         '11 projects · 14 people · subcontractors · tender to handover',
         [('Contractor coordination', 'Subcontractors and 14 people coordinated '
           'across 11 projects: quality, progress and safety monitored weekly, '
           'deviations raised early, and acceptance testing with the client at '
           'handover. The contractor side of the table, managed on agreements '
           'rather than good intentions.')]),
        ('Maintenance & Operations Manager / Workshop Technician',
         'Biofos (Lynetten) · Copenhagen · Aug. 2017 – Jan. 2022',
         '24/7 operations · critical plant · 10 people · shift work · CMMS',
         [('Permits, CMMS and uptime', 'Work permits issued per shift, LOTO and '
           'risk assessments followed before any task, and contractor '
           'adherence to safety rules monitored on site. Preventive and '
           'corrective maintenance of pumps, HVAC, process piping and electrical '
           'systems, with CMMS data maintained and MTBF, MTTR and uptime '
           'followed as measures.')]),
        ('Electromechanical Technician / Production Supervisor',
         'ARJ Engineering · Tehran · Dec. 2003 – Mar. 2010',
         '12 mechanics and technicians · machine workshop · production line',
         [('Fault diagnosis and teams', 'Maintenance and repair of machines and '
           'production equipment with 12 mechanics and technicians led '
           'day-to-day. Fault diagnosis and root-cause analyses that changed '
           'how failures were handled, and spare parts kept so repairs did not '
           'wait.')]),
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
    m.bullet('Safety and permits', 'Permit-to-work, LOTO, APV and risk '
             'assessments as daily practice from 24/7 operations. Compliance '
             'with permit requirements checked before work and closed after '
             'it, and contractors followed up on safety regulations and '
             'procedures.', after=10)
    m.bullet('Maintenance and assets', 'Preventive and corrective maintenance '
             'of building systems, laboratory and process equipment, HVAC and '
             'electrical installations. Availability, reliability and uptime '
             'followed as measures, and fault diagnosis used to fix causes, '
             'not just symptoms.', after=10)
    m.bullet('Contractors and soft services', 'External contractors and '
             'specialist suppliers managed on schedules, quality and safety. '
             'Soft-service categories are newer to me, but the contract '
             'discipline is not: agreed standards, follow-up and corrective '
             'action.', after=10)
    m.bullet('Clients and documentation', 'Point of contact for clients, '
             'suppliers and internal teams, with reports, maintenance '
             'schedules and technical documentation prepared as part of the '
             'work. Danish, English and Persian.', after=10)

    m.section('FIRST 90 DAYS')
    m.para('The plan follows the role: the safety baseline, the assets, the '
           'service.', after=8)
    m.bullet('Days 1-30 · The safety baseline', 'The HSE Permit-to-Work system '
             'learned end to end, contractor routines and permits checked '
             'against reality, and open work permits visible in one place. '
             'Goal: everyone on site knows how a job gets approved.', after=10)
    m.bullet('Days 31-60 · The assets', 'Technical assets and building systems '
             'walked down and baselined, preventive and corrective maintenance '
             'on one schedule, and CMMS data cleaned up. Goal: the asset '
             'picture matches the plant.', after=10)
    m.bullet('Days 61-90 · The service', 'Soft-service contracts measured on '
             'agreed service standards, service quality monitored in a fixed '
             'rhythm, and the first improvements implemented. Goal: the client '
             'sees the difference in the daily service.', after=10)

    m.section('LANGUAGES, TOOLS & PRACTICAL')
    m.para('Danish (native) · English (professional) · Persian (native). '
           'CMMS, SAP ERP, Microsoft Office, MS Project; PRINCE2. Driving '
           'licence B (manual). Available by agreement.', after=32)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Requirements and documentation · Technical Supervisor, '
                   'CBRE · Job ID 305257',
                   ('Requirement in the posting', 'Documented experience'),
                   [
        ('Technical degree in Electrical Engineering, Mechanical Engineering, '
         'Mechatronics, Building Services Engineering or Facilities Engineering',
         'Authorised Electrical Engineer, LV/MV/HV (Sikkerhedsstyrelsen, May '
         '2023) with a Maskinmester background, B.Tech (EQF6) in Technology '
         'Management and Mechanical Engineering (2017-2022, GPA 7.6) and '
         'Electrical and Mechanical Engineering Design (2000-2003). Electrical '
         'and mechanical covered from both degrees and the authorisation.'),
        ('Minimum of 2 years of experience in a technical maintenance, '
         'facilities, or service-oriented environment',
         '20+ years in exactly that environment: 6 years in 24/7 maintenance '
         'and facilities operations (Biofos 2017-2022), service agreements for '
         'business customers (ELOHVAC 2023-2026), and technical service and '
         'project work since 2003. The minimum of 2 years is met many times '
         'over.'),
        ('Strong knowledge of building systems, maintenance processes, and '
         'fault diagnosis',
         'HVAC, ventilation, electrical installations, pumps and process '
         'piping maintained and repaired (Biofos 2017-2022, ELOHVAC 2023-2026), '
         'maintenance processes built and run (preventive and corrective), and '
         'fault diagnosis with root-cause analyses since 2003 (ARJ, Biofos).'),
        ('Familiarity with health, safety, and environmental regulations and '
         'relevant technical legislation',
         'Work permits, LOTO, APV and risk assessments as daily practice in '
         '24/7 operations (Biofos 2017-2022), audits against ISO 9001/14001 '
         '(Novo 2022-2024), and compliance with technical legislation on '
         'electrical jobs (DS/HD 60364, SB-guidance) as authorised electrician. '
         'Safety rules followed because they work, not because they are '
         'written.'),
        ('Excellent communication and stakeholder management skills',
         'Point of contact for clients, suppliers and internal teams since '
         '2003: customer dialogue on service agreements (ELOHVAC 2023-2026), '
         'supplier negotiations (Hansen 2025-2026), and weekly alignment with '
         '25 specialists and contractors (Novo 2022-2024). Clear updates when '
         'plans change.'),
        ('Experience with Computerized Maintenance Management Systems (CMMS) '
         'and standard Microsoft Office applications',
         'CMMS data maintained as part of daily operations (Biofos 2017-2022): '
         'work orders, schedules and history kept current so planning could '
         'trust them. Microsoft Office daily, plus SAP, MS Project and Power '
         'BI for reporting.'),
        ('Strong organizational skills with the ability to manage multiple '
         'priorities simultaneously',
         '37 parallel CAPEX projects (Novo 2022-2024), 11 parallel projects '
         'with 14 people (Ventek 2022), and service agreements plus enterprise '
         'jobs running side by side (ELOHVAC 2023-2026). Priorities set daily, '
         'and followed up.'),
        ('Fluent in both Danish and English, written and spoken',
         'Danish and English fluent in speech and writing: English as working '
         'language in GMP projects with international stakeholders (Novo '
         '2022-2024) and in technical documentation and audits. Persian as '
         'native language in addition.'),
        ('HSE Permit-to-Work system: preparing and issuing work permits, '
         'compliance with permit requirements',
         'Work permits prepared and issued per shift in 24/7 operations '
         '(Biofos 2017-2022), LOTO applied before any task on live systems, '
         'and compliance with permit requirements monitored with contractors '
         'on site. The permit system is the part of the job I’ve taken most '
         'seriously for years.'),
        ('Timely, effective, and safe execution of technical work carried out '
         'by external contractors',
         'External contractors and subcontractors coordinated across 11 '
         'projects (Ventek 2022), specialist contractors on electrical and '
         'ventilation jobs (ELOHVAC 2023-2026), and contractor safety '
         'monitored on site (Biofos 2017-2022). Execution followed up on '
         'quality, progress and safety, not just on price.'),
        ('Maintenance and repair activities for laboratory equipment, '
         'buildings, and technical installations',
         'Laboratory equipment, climate chambers and process installations '
         'commissioned and maintained (Novo 2022-2024), buildings and '
         'technical installations serviced through agreements (ELOHVAC '
         '2023-2026), and critical plant maintained around the clock (Biofos '
         '2017-2022).'),
        ('Availability, reliability, and performance of technical assets and '
         'building systems',
         'MTBF, MTTR and uptime followed as measures in 24/7 operations '
         '(Biofos 2017-2022), availability of electrical and ventilation '
         'systems as service target (ELOHVAC 2023-2026), and asset condition '
         'monitored through planned maintenance rather than breakdowns.'),
        ('Coordinate preventive and corrective maintenance activities, monitor '
         'service quality',
         'Preventive and corrective maintenance coordinated daily for six '
         'years (Biofos 2017-2022) and across service agreements (ELOHVAC '
         '2023-2026), with quality checked at handover and follow-up done on '
         'every deviation. One schedule, one truth.'),
        ('Identify and implement improvements in maintenance practices, '
         'processes, and performance',
         'Root-cause analyses that changed failure handling (ARJ 2003-2010), '
         'planned maintenance rebuilt around failure data (Biofos 2017-2022), '
         'and 5S and Standard Work used as working methods. Improvements '
         'implemented, not just identified.'),
        ('Primary point of contact for the client, suppliers, and internal '
         'stakeholders',
         'The contact point role is my normal position: client dialogue on '
         'service agreements (ELOHVAC 2023-2026), supplier coordination '
         '(Hansen 2025-2026), and internal coordination across engineering, '
         'procurement and operations (Novo 2022-2024). Reaches and answers, '
         'both directions.'),
        ('Compliance with relevant legislation, safety regulations, and '
         'CBRE/client procedures',
         'GMP- and FDA/EMA-procedures followed strictly (Novo 2022-2024), ISO '
         '9001/14001 audits met (Novo), safety regulations and technical '
         'legislation kept on every job as authorised electrician, and '
         'documentation that withstood revision. New procedures are learned '
         'fast because they matter.'),
        ('Management of outsourced soft services: cleaning, coffee and vending, '
         'waste management, indoor plants',
         'Soft services as a category are new to my CV; the discipline is not: '
         'service agreements and supplier contracts managed on agreed '
         'standards (ELOHVAC 2023-2026, Hansen 2025-2026), where follow-up, '
         'quality checks and corrective action were the method. The categories '
         'change; the contract management does not.'),
        ('Prepare and manage reports, maintenance schedules, and technical '
         'documentation',
         'Maintenance schedules and documentation kept current (Biofos '
         '2017-2022), project documentation through FAT/SAT and IQ/OQ/PQ '
         '(Novo 2022-2024), and monthly reporting on budget and progress '
         '(ELOHVAC, Hansen). Reports prepared as part of the work, not after '
         'it.'),
        ('Lead and support technicians and contractors on a day-to-day basis',
         'Teams led day-to-day since 2003: 12 mechanics and technicians (ARJ '
         '2003-2010), 10 people on shifts (Biofos 2017-2022), 14 people and '
         'subcontractors (Ventek 2022), 5 electricians and 3 apprentices '
         '(ELOHVAC 2023-2026). Support during equipment failures and complex '
         'technical issues included, not delegated away.'),
    ], widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo - Application Technical Supervisor, '
                       'CBRE (Job ID 305257)')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_CBRE_TechnicalSupervisor_305257.docx')
    build(out)
    print(out)
