#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Electrical Supervisor — Hyperscale Data Centre (Europe; Copenhagen, Cologne,
Gavle, Charleroi). English posting -> EN-GB document (4 pages).

Unnamed contact -> "Dear Hiring Team," (hiring_team precedent).
Package: up to EUR 85k + accommodation + allowance + travel + flights.
Posting states "EU/UK PASSPORT NECESSARY - NO VISA SPONSORSHIP GIVEN".

HONEST POSITION (user skipped the clarifying questions -> neutral default):
- Nationality/passport is NEVER mentioned (standard practice; "udelad").
  The user is an Iranian citizen with a Danish residence permit (Quantum-KIT),
  NOT an EU/UK passport holder. This eligibility gate is flagged to the user
  in the report and PR body. Nothing about passports or work rights is claimed.
- Travel between the project's locations is written as general willingness
  (Saildrone-KIT: travel 50-75% = yes). No specific relocation claims.
- Revit = new to him (Kemp-KIT: Revit unknown) -> honest hedge. AutoCAD real.
- Languages line stays truthful: Danish/English/Persian. No Swedish claimed.

STIL (3/3 mod #448 DB Cargo): register "Safe hands, clean records",
opening BY (the power must not blink), structure "Site, standards, handover".
Banned words never quoted even when the JD uses them ("make a difference",
"dynamic"). English contractions are binding. No em dash anywhere.
Apostrophes are curly (U+2019) in script AND jd files.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_CBRE_TechnicalSupervisor_305257.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Hyperscale Data Centre · Electrical Supervisor · Europe'
BANNER_RESUME = 'ELECTRICAL SUPERVISION · HSQE · COMMISSIONING · SUBCONTRACTORS'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('2 December 2026')
    m.meta('Hyperscale Data Centre · Electrical Supervisor')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application for the position of Electrical Supervisor',
           bold=True, color='1A1A1A')
    m.para('Dear Hiring Team,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('A hyperscale data centre answers to one unforgiving rule: the power '
       'must not blink. Everything electrical underneath that rule, on a '
       'landmark Hyperscale Data Centre facility in Europe, has to be built, '
       'supervised and handed over without shortcuts, and that is '
       'where this role is a pivotal role in our project development and '
       'implementation process, as the brief puts it: working closely with '
       'the Construction and Project Manager on the coordination and '
       'operation of the site to deliver the completion of projects. I’m '
       'applying because site supervision of electrical works is the craft '
       'I’ve practised for years, on construction sites where subcontractors, '
       'plant and materials had to line up every single day.')

    lp('The electrical trade background that’s called essential is formal in '
       'my case: Authorised Electrical Engineer, LV/MV/HV (Sikkerhedsstyrelsen, '
       'May 2023), a B.Tech in Technology Management and Mechanical '
       'Engineering, and electrical and mechanical design training from '
       '2000-2003. The minimum 3-5 years’ experience in a similar role is '
       'covered many times over. I’ve supervised direct labour resources and '
       'subcontractors on construction sites (Ventek: 14 men and '
       'subcontractors across 11 projects), led 5 electricians and 3 '
       'apprentices in service and installation (ELOHVAC, 2023-2026), and '
       'managed 12 mechanics in a workshop (ARJ, 2003-2010). The daily '
       'management, supervision, and reporting of people, plant and '
       'materials allocations is the everyday rhythm of those jobs, and I '
       'manage and coordinate sub-contractors on site the same way: clear '
       'briefings, firm follow-up. HSQE is not a binder on the shelf in 24/7 '
       'utilities; site operations there run in strict compliance with '
       'company HSQE requirements and standards, with the safe execution of '
       'works as the first priority. Complying with building regulations, '
       'National Rules for Electrical Installations, Health and Safety and '
       'environmental standards is the Danish daily: DS/HD 60364 and the SB '
       'guidance, which my authorisation is built on, plus AB 18 and ABT 18 '
       'on the construction side. As-Built records I know from commissioning: '
       'compilation of accurate information for handover, documentation '
       'packs that had to be right the first time, and recording performance '
       'and progress of site operations and subcontractors as we went. '
       'Microsoft Office, Excel and SAP are tools I use daily. Revit is the '
       'one name in the brief I’d be new in; my drawing background is AutoCAD '
       'from design work.', after=44)

    lp('In the first month it’s the site that teaches: inductions, the HSQE '
       'routines as they are, the crews and subcontractors introduced '
       'properly, and every part of the electrical scope walked before '
       'anything changes. By the second month it’s standards: works carried '
       'out to the drawings and the rules, compliance and administration '
       'procedures kept simple and followed, and performance and progress '
       'recorded so nobody has to guess. The third month is handover: '
       'As-Built records compiled accurately, snag lists closed, and the '
       'documentation the client needs to run the facility. I work with '
       'minimum supervision, within a fast-paced team environment, and the '
       'goal for the 90 days is plain: works delivered to a high standard, '
       'HSQE intact, and records that don’t need fixing later.')

    lp('The culture part of the brief I recognise myself in: work-life '
       'balance that’s real, professional growth through training and '
       'development programs, and collaborating with industry leaders on '
       'projects that matter for a sustainable future. As you put it, '
       'recognising the contributions and respecting our people is core to '
       'our culture and values, and I’d be glad to join an equal '
       'opportunities employer that means it. Organisational and planning '
       'skills are what I rely on when several crews compete for the same '
       'morning, and communication skills and interpersonal skills, with the '
       'ability to build effective working relationships, decide whether '
       'subcontractors follow the plan or improvise. Travel between the '
       'project’s locations suits me; I’m used to working away from home '
       'base and across different sites. My CV is attached, and I look '
       'forward to hearing from you.', after=44)

    m.para('Kind regards,', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFILE')
    m.para('An electrical supervisor with 20+ years in electrical delivery: '
           'authorisation at LV/MV/HV level, construction sites with '
           'subcontractors and direct labour, and commissioning of critical '
           'systems where the documentation had to stand up to scrutiny.',
           after=32)
    m.para('Planning, HSQE and handover are the three disciplines I run a '
           'site by. SAP, Microsoft Office and CMMS are daily tools; PRINCE2 '
           'gives the project spine. I’m used to fast-paced environments, '
           'minimum supervision and travel between sites.', after=32)

    jobs = [
        ('CTO, AI Department & Authorised Electrical Engineer (LV/MV/HV)',
         'Data Power Consultant ApS · Copenhagen · 2024 – present (from Nov. 2026 '
         'also ELOHVAC\u2019s electrical activities)',
         'AI department 4-10 people · electrical service and enterprise · '
         'contractor coordination',
         [('Electrical work and contractors',
           'Electrical service and enterprise planned and executed for '
           'commercial clients, with offers and deliveries followed through '
           'to the end.'),
          ('AI and analysis',
           'The AI department builds both software products and AI tools, '
           'used as daily support for analysis and reporting.')]),
        ('Service and Operations Manager · Authorised Electrical Engineer',
         'ELOHVAC · Ballerup · May 2023 – Nov 2026',
         '5 electricians and 3 apprentices · service, installation, projects',
         [('Supervision and installation',
           'Electricians and apprentices supervised on service, installation '
           'and project work. Subcontractors coordinated, KS kept, offers '
           'and agreements followed through on time, quality and cost.')]),
        ('Commissioning Manager',
         'Novo Nordisk · Hillerød · Nov 2022 – Jul 2024',
         '37 CAPEX projects, DKK 2-10m · 25 specialists · GMP, IQ/OQ/PQ',
         [('Commissioning and documentation',
           'Critical systems commissioned with full documentation and '
           'release: IQ/OQ/PQ records, as-built packages and handover '
           'information that had to be accurate the first time. Agreed '
           'dates were kept.')]),
        ('Site Foreman and Enterprise Manager',
         'Ventek · Taastrup · Jan 2022 – Nov 2022',
         '11 projects · 14 men and subcontractors',
         [('Site supervision',
           'Labour, plant and materials coordinated daily on '
           'construction sites. Subcontractors briefed and followed up, '
           'site operations kept safe, progress reported to the project '
           'management.')]),
        ('Maintenance and Operations Manager / Workshop Technician',
         'Biofos (Lynetten) · Copenhagen · Aug 2017 – Jan 2022',
         '24/7 operations · critical plant · 10 employees · shift work',
         [('Critical plant around the clock',
           'Pumps, HVAC, process piping, electrical, SCADA and PLC kept '
           'running 24/7 with 10 people on shift. Permits, safety routines '
           'and environmental standards were part of daily practice, and '
           'breakdowns were prioritised fast.')]),
        ('Electromechanical Technician / Production Manager',
         'ARJ Engineering · Tehran · Dec 2003 – Mar 2010',
         '12 mechanics and technicians · machine shop · production line',
         [('Production and people',
           'Production planning, materials control from drawing to finished '
           'part, and training of new staff in the workshop.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('EDUCATION & CERTIFICATION')
    m.edu('Authorised Electrical Engineer (LV/MV/HV)',
          'Sikkerhedsstyrelsen · May 2023')
    m.edu('B.Tech (EQF6), Technology Management and Mechanical Engineering',
          'Denmark · 2017–2022 · GPA 7.6')
    m.edu('Electrical and Mechanical Engineering Design (EQF6)',
          'Tehran Technical University · 2000–2003')
    m.edu('PRINCE2, certified project manager', 'AXELOS / PeopleCert')
    m.edu('Refrigeration and climate systems (AMU)',
          'Mercantec · 2021 · STCW 2021–2023, Danish Maritime Authority')

    m.section('COMPETENCIES')
    m.bullet('Site supervision', 'Direct labour, subcontractors, plant and '
             'materials coordinated daily on construction and service '
             'sites.', after=10)
    m.bullet('HSQE and compliance', 'Permits, safety procedures and '
             'environmental standards from 24/7 utilities; National Rules '
             'for Electrical Installations (DS/HD 60364) as the working '
             'standard.', after=10)
    m.bullet('Commissioning and handover', 'As-built documentation, accurate '
             'records and release procedures from 37 commissioning '
             'projects.', after=10)
    m.bullet('Tools', 'Microsoft Office, SAP, CMMS, AutoCAD; PRINCE2. Revit '
             'is new to me; the drawing background transfers.', after=10)

    m.section('FIRST 90 DAYS')
    m.para('The plan follows the work: the site, standards, handover.',
           after=8)
    m.bullet('Days 1-30 · The site', 'Inductions done, HSQE routines learned '
             'as they are, crews and subcontractors introduced, and the '
             'electrical scope walked end to end before anything changes.',
             after=10)
    m.bullet('Days 31-60 · Standards', 'Works executed to drawings and '
             'rules, compliance and administration procedures running '
             'without drama, and performance and progress recorded so nobody '
             'guesses.', after=10)
    m.bullet('Days 61-90 · Handover', 'As-Built records compiled accurately, '
             'snag lists closed, and the documentation package the client '
             'needs to run the facility.', after=10)

    m.section('LANGUAGES, TOOLS & PRACTICAL')
    m.para('Danish (native) · English (professional) · Persian (native). '
           'Microsoft Office, SAP, CMMS; PRINCE2. AutoCAD from design work; '
           'Revit is new to me. Driving licence B (manual). Available by '
           'agreement.', after=32)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Requirements and documentation · Electrical Supervisor, '
                   'Hyperscale Data Centre',
                   ('Requirement in the posting', 'Documented experience'),
                   [
        ('Essential: electrical trade background',
         'Authorised Electrical Engineer, LV/MV/HV (Sikkerhedsstyrelsen, May '
         '2023), B.Tech (EQF6) in Technology Management and Mechanical '
         'Engineering (2017-2022) and Electrical and Mechanical Engineering '
         'Design (2000-2003). The trade background is formal, not picked up '
         'along the way.'),
        ("Minimum 3-5 years’ experience in a similar role",
         '20+ years in electrical delivery and supervision: 14 men and '
         'subcontractors on 11 construction projects (Ventek 2022), 5 '
         'electricians and 3 apprentices in service and installation '
         '(ELOHVAC 2023-2026), 12 mechanics in a workshop (ARJ 2003-2010) '
         'and 10 people on shift in 24/7 operations (Biofos 2017-2022).'),
        ('Proficiency in using Microsoft Office required',
         'Microsoft Office and Excel in daily use since 2003, alongside SAP and '
         'CMMS. '
         'Reporting and administration run through these tools every week.'),
        ('Experience in Revit would be advantageous',
         'Not yet worked in Revit; the drawing background is AutoCAD from '
         'design work (2000-2003), so drawings and models are familiar '
         'territory. Honest about the gap; the transfer is real.'),
        ('Excellent organisational and planning skills',
         'Planning across 37 CAPEX projects (Novo 2022-2024, DKK 2-10m '
         'each) and 11 parallel construction projects (Ventek 2022). '
         'PRINCE2 certified; planning from annual schedules to the daily '
         'briefing.'),
        ('Excellent communication skills and ability to work well in a team '
         'environment',
         'Communication with clients, project management, '
         'subcontractors and site crews happens daily in Danish and English. '
         'Cross-disciplinary teams of up to 25 specialists (Novo).'),
        ('Excellent interpersonal skills; build effective working '
         'relationships',
         'Teams built and kept together: 10 on shift (Biofos 2017-2022), 14 '
         'on site (Ventek 2022), 5 electricians and 3 apprentices '
         '(ELOHVAC 2023-2026). Relationships with subcontractors run on '
         'clear briefs and firm follow-up.'),
        ('Reporting to Construction and or Project Manager',
         'Used to clear reporting lines: commissioning under project '
         'management (Novo 2022-2024) and site progress reporting (Ventek '
         '2022). PRINCE2 gives the shared language.'),
        ('Ability to work with minimum supervision, within a fast-paced team '
         'environment',
         'Self-directed site work across multiple parallel projects '
         '(Ventek 2022) and independent operation of a 24/7 utility site '
         '(Biofos 2017-2022). The fast pace is the normal pace.'),
        ('Ensure all site operations are carried out in strict compliance '
         'with company HSQE requirements and standards',
         'HSQE disciplines from 24/7 utilities under public ownership '
         '(Biofos 2017-2022): permits, safety procedures, work environment '
         'and environmental standards as daily practice, not paperwork.'),
        ('Daily management, supervision, and reporting, of direct labour '
         'resources, plant, safe execution of works and materials '
         'allocations',
         'Day-to-day management of 12 mechanics (ARJ 2003-2010), 10 on shift '
         '(Biofos 2017-2022) and 14 on site (Ventek 2022). Plant and '
         'materials allocations planned so repairs did not wait; safe '
         'execution of works never traded for speed.'),
        ('Manage and coordinate sub-contractors on site',
         'Subcontractors coordinated on construction sites (Ventek 2022) '
         'and in service and installation work (ELOHVAC 2023-2026), '
         'including their part of the HSQE routines.'),
        ('Post construction survey and compilation of accurate information '
         'to prepare As-Built records',
         'As-built packages and handover documentation from 37 commissioning '
         'projects (Novo 2022-2024); measuring-up and accurate records from '
         'service and construction work (ELOHVAC, Ventek).'),
        ('Carry out company compliance and administration procedures',
         'KS (quality systems), documentation and release procedures in GMP '
         'environments (Novo 2022-2024) and service agreements with '
         'administrative follow-up (ELOHVAC 2023-2026).'),
        ('Recording performance and progress of site operations and '
         'subcontractors',
         'Progress and performance followed up in fixed meeting rhythms: '
         'milestone tracking across 37 projects (Novo), P&L and quality '
         'follow-up (ELOHVAC), '
         'daily site reporting (Ventek).'),
        ('Complying with building regulations, National Rules for Electrical '
         'Installations, Health and Safety and environmental standards',
         'Danish National Rules for Electrical Installations (DS/HD 60364, '
         'SB guidance) as the basis of the authorisation (2023); building '
         'regulations and environmental standards from AB 18/ABT 18 '
         'construction work and 24/7 utility operations.'),
        ('High standard of works',
         'Documented quality discipline: IQ/OQ/PQ and release on 37 GMP '
         'projects, KS on electrical installation, and first-time-right '
         'documentation on handover.'),
        ('Scope covered: electrical installations, plant and materials',
         'LV/MV/HV authorisation with hands-on work across pumps, HVAC, '
         'process piping, electrical panels, SCADA and PLC systems '
         '(Biofos 2017-2022) and critical electrical systems (Novo '
         '2022-2024).'),
                   ],
                   widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo - Application Electrical Supervisor, '
                       'Hyperscale Data Centre')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_HyperscaleDC_ElectricalSupervisor.docx')
    build(out)
    print(out)
