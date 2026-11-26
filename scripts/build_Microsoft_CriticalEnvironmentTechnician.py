# -*- coding: utf-8 -*-
"""Critical Environment Technician (CET) — Microsoft, CO+I Denmark, 3 sites Greater Copenhagen.

English JD -> en-GB document, 4 sider i masterdesign: letter p1, CV p2-3, kravmatrix p4.
No named contact in the JD -> greeting "Dear Microsoft hiring team,".

STILVALG (style_guard godkendt, 3/3 skift mod #421 Saildrone):
  register     = Safety mindset, technical judgment (safety · reliability · procedure ·
                 learning · continuous improvement)
  åbningsgreb  = AW (den uforstyrrede vagt som målet: de fleste dage i et critical environment
                 er begivenhedsløse, og det er præcis pointen; roen er produktet)
  struktur     = By the book (EOPs · MOPs · SOPs) — procedurerne som skelet for 30/60/90

BRUGERENS KORREKTION + permanent regel: alt tekst humaniseret i letter OG CV, en-GB.
Ingen em dash. Brug sammentrækninger.

BRUGERBEKRÆFTET 25.11.2026 (ærlige grænser):
  - Vagtmønster 2-2-7 (2 dage 6-18, 2 nætter 18-6, 7 døgn fri, DI-aftale): "helt fint".
  - Microsoft Cloud Background Check: ingen forventede problemer.
  - Direkte datacenter-erfaring er nyt (opslaget siger det ikke er påkrævet) -> ærligt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Microsoft · Critical Environment Technician (CET)'
BANNER_RESUME = 'Critical environment operations · electrical and mechanical'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('25 November 2026')
    m.meta('CO+I Denmark · Critical Environment Technician, Greater Copenhagen')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Critical Environment Technician (CET), 3 sites Greater Copenhagen',
           bold=True, color='1A1A1A')
    m.para('Dear Microsoft hiring team,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('Most days in a critical environment are uneventful, and that is the point. The '
       'screens stay quiet, the plant runs, and nobody outside notices anything. Keeping it '
       'that way is the work: watch the electrical, mechanical, cooling and control systems '
       'closely enough that the boring days stay boring. I have spent years on that side of '
       'the glass, in a utility that ran 24/7 and could not simply stop, and the calm shift '
       'is still the one I am proud of.')

    lp('You are hiring a Critical Environment Technician to support the safe, reliable, and '
       'efficient operation of Microsoft datacenter infrastructure in Denmark. Microsoft\'s '
       'mission to empower every person and every organization on the planet to achieve more '
       'runs on infrastructure that must not fail, and CO+I builds the culture around it: '
       'safety, reliability, sustainability, inclusion, learning, and continuous improvement. '
       'That list is not wallpaper to me. Model Microsoft values, follow approved procedures, '
       'use STOP WORK authority when needed: those are working instructions, and they match '
       'how I already operate.')

    lp('The technical side of the role I know from the floor up. Electrical, mechanical, '
       'cooling and control systems have been my daily work since 2003: electromechanical '
       'trades, then electrical installations and HVAC/climate as a service owner, and 24/7 '
       'operations on pumps, HV switchgear, SCADA and PLC at Biofos. Maintenance to approved '
       'procedures, preventive as well as corrective, is routine for me, from LOTO and APV '
       'discipline to the work instruction that says exactly how the job is done. '
       'Certifications back it up: authorised electrical engineer (LV/MV/HV), refrigeration '
       'and air conditioning (AMU), and a B.Tech in mechanical engineering. High-availability, '
       'mission-critical environments are the only kind I have worked in.')

    lp('A few honest notes. Direct datacenter experience is not required here, and I will '
       'take you at your word: the datacenter domain is new to me, while the critical '
       'environment behind it is not. Your onboarding and support to build the necessary '
       'domain expertise is exactly what I would lean on in the first months. I am ready for '
       'the Microsoft Cloud Background Check upon hire and expect no issues on my side. The '
       'shift pattern, two days 6:00 AM to 6:00 PM, two nights 6:00 PM to 6:00 AM, and seven '
       'days off following each rotation in accordance with the DI agreement, suits me; I '
       'have confirmed that. Valid driver\'s license (category B) for the trips between the '
       'three sites, and I communicate effectively in English, in speech and in writing.')

    lp('What draws me is the team described around the role: an inclusive environment where '
       'all team members can perform, grow, and succeed, and a high-performing datacenter '
       'operations team built from diverse technical backgrounds. My background is exactly '
       'that kind of diverse. The ideal candidate demonstrates a strong safety mindset, sound '
       'technical judgment, and a structured, procedure-driven environment is where I do my '
       'best work, not a limitation I tolerate. And your own sentence, "You do not need to meet '
       'every requirement to apply", is exactly why I am sending this. I bring the safety, the '
       'judgment and the hands; the datacenter vocabulary I will learn.')

    lp('The first 90 days I have written as a plan on page 3 of the CV, built around your own '
       'documents: learn the book (EOPs, MOPs, SOPs), work the book, then improve the book. '
       'I can start with the next rotation. With shift work, work-life balance matters, and '
       'the 2-2-7 pattern you offer is a genuinely good one. I look forward to the '
       'conversation.', after=44)

    m.para('Kind regards,', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFILE')
    m.para('Technician with 20+ years in critical, high-availability environments. 24/7 '
           'operations and monitoring on pumps, HVAC, HV switchgear, SCADA and PLC; '
           'preventive and corrective maintenance to approved procedures; electrical, '
           'mechanical, cooling and control systems in one pair of hands. Shift-trained, '
           'safety-first, calm in incidents. New to the datacenter domain, not new to what '
           'keeps one alive.', after=32)

    m.section('EXPERIENCE')
    jobs = [
        ('CTO for the AI department and authorised electrical engineer (electrical and ventilation)',
         'Data Power Consultant ApS · Copenhagen · 2024 – present (ELOHVAC electrical activities '
         'moved here in Nov. 2026)',
         'AI department 4-10 people · electrical service and contracting · 5 electricians + 3 apprentices',
         [('Electrical and cooling', 'Electrical service and fault finding for commercial clients: '
           'panels, controls, automation and preventive maintenance on electrical, ventilation and '
           'climate systems. Acute call-outs solved on site, findings written down afterwards.'),
          ('Systems and records', 'AI department of 4-10 people, investment cases and monthly KPI '
           'follow-up. CMMS and digital checklists for maintenance records; Python and Claude API '
           'for dashboards the team actually uses.')]),
        ('Owner / technical director / authorised electrical engineer',
         'ELOHVAC ApS · Copenhagen · May 2023 – November 2026 (company closed)',
         'Commercial customers · electrical, ventilation and climate · contracting · full P&L · service agreements',
         [('Maintenance by the book', 'Preventive and corrective maintenance on electrical, '
           'ventilation and climate systems in service agreements with response time, quality and '
           'delivery as targets. Approved procedures and work instructions in every task, LOTO, '
           'APV and risk assessment at site start-up.'),
          ('Execution with vendors', 'Subcontractor and supplier coordination, tenders and pricing, '
           'monthly budget follow-up. Safe and high-quality execution as the bar; zero critical '
           'deviations in the service agreements.'),
          ('Building capability', 'Led 5 electricians and 3 apprentices: daily planning, 1:1s, '
           'hands-on demonstrations and structured training. Technical capability developed over '
           'time, not hired in.')]),
        ('Senior commissioning engineer / project manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · November 2022 – July 2024',
         '37 CAPEX projects, DKK 2–10 mio. each · 25 specialists · GMP/FDA/EMA',
         [('Commissioning under scrutiny', 'Process plants commissioned and tested after FAT/SAT and '
           'IQ/OQ/PQ under GMP/FDA/EMA, zero critical findings at handover. Safety, compliance and '
           'operational risk assessed and escalated early in every project.'),
          ('Cross-functional work', 'Monthly reports on progress, cost, risks and resources to '
           'leadership and client management; 25 specialists across engineering, procurement and '
           'operations. SAP ERP for accurate records.')]),
        ('Project and workshop manager', 'Ventek-Air · Copenhagen · January 2022 – November 2022',
         '11 concurrent projects · 14-person team · subcontractors and logistics',
         [('Coordination', '11 concurrent projects and a 14-person team. Tenders, contract basis, '
           'subcontractors and safety documentation followed through, daily boards for capacity '
           'and progress. Equipment and materials handled: loading, shipping and relocation.')]),
        ('Maintenance and operations manager / workshop technician',
         'Biofos (Lynetten) · Copenhagen · August 2017 – January 2022',
         '24/7 operations · SCADA, PLC, HV switchgear · rotating shifts',
         [('Monitoring and operations', 'Monitored, operated and maintained pumps, HVAC, HV '
           'switchgear, SCADA and PLC around the clock in a plant that could not stop. Preventive '
           'and corrective maintenance, incident response, troubleshooting and recovery, day and '
           'night.'),
          ('Shift and safety discipline', 'Rotating shifts and on-call duty for 4.5 years: LOTO, '
           'APV, risk assessment and near-miss reporting as routine. Anyone could halt the job '
           'until it was safe, and production waited. 5S and Standard Work in the workshop.')]),
        ('Electromechanical technician / production team leader',
         'ARJ Engineering · Tehran · December 2003 – March 2010',
         '12 mechanics and technicians · machine shop · product line',
         [('Industrial foundation', 'Led 12 mechanics and technicians: shift planning, materials '
           'and goals. Fault diagnosis on industrial electromechanical equipment, root-cause '
           'analysis and corrective actions that were followed up.')]),
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
    m.edu('HF (general upper secondary)', 'VUC · 2012–2017')
    m.edu('Refrigeration and air conditioning (AMU)',
          'Mercantec · 2021 · STCW 2021–2023, Danish Maritime Authority · PRINCE2 (AXELOS/PeopleCert)')

    m.section('COMPETENCES')
    m.bullet('Monitoring and operations', 'Electrical, mechanical, cooling and control systems: '
             'HV switchgear, pumps, HVAC, SCADA, PLC. Rounds, readings and quiet screens as the '
             'daily goal.', after=10)
    m.bullet('Maintenance', 'Preventive and corrective work to approved procedures: EOPs, MOPs and '
             'SOPs as they are written, LOTO and APV discipline, accurate records and inventory '
             'in CMMS and SAP ERP.', after=10)
    m.bullet('Incidents and safety', 'Incident response and recovery in 24/7 operations, escalation '
             'of safety, compliance and operational risks early, STOP WORK thinking as a habit. '
             'Root-cause reports (5 Whys, Ishikawa) so the same failure does not return.', after=10)
    m.bullet('Team and learning', 'Knowledge sharing and training of electricians, apprentices and '
             'contractors. Lean and Six Sigma practice, not certified: DMAIC, 5S, PDCA, VSM, A3, '
             'Kaizen, Standard Work, SMED, TPM, 5 Whys, Ishikawa and FMEA.', after=10)

    m.section('THE FIRST 90 DAYS')
    m.para('A plan built around your own documents:', after=8)
    m.bullet('Days 1-30 · Learn the book', 'Onboarding first: EOPs, MOPs and SOPs read and '
             'understood, the three sites walked, the systems mapped with an experienced '
             'colleague at my side. Goal: I can perform a scheduled round and follow the '
             'documented procedure on my own.', after=10)
    m.bullet('Days 31-60 · Work the book', 'Preventive and corrective maintenance executed to '
             'approved procedures, incidents handled with the team, CMMS records kept current. '
             'Goal: my work orders close on time with accurate documentation.', after=10)
    m.bullet('Days 61-90 · Improve the book', 'Contribute to continuous improvement: knowledge '
             'sharing sessions, procedure feedback where reality does not match the paper, one '
             'concrete improvement. Goal: one suggestion with a measurable effect on safety or '
             'reliability.', after=10)

    m.section('LANGUAGES, TOOLS AND PRACTICAL')
    m.para('Danish (native) · English (professional, daily working language since 2017) · '
           'Persian (native). CMMS, SAP ERP, SCADA, PLC, Power BI, Python. PRINCE2. Valid '
           'driver\'s license B (manual). Shift experience from 24/7 operations, confirmed for '
           'the 2-2-7 rotation. Based in Måløv, Greater Copenhagen. Ready for the Microsoft '
           'Cloud Background Check. Available for the next rotation.', after=32)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Critical Environment Technician · requirements and evidence',
                   ('Requirement', 'Evidence'),
                   [
        ('Monitor, operate, and control critical infrastructure systems, including electrical, mechanical, cooling, and control systems',
         'Monitored and operated critical infrastructure 24/7 at Biofos (2017-2022): pumps, HVAC, '
         'HV switchgear, SCADA and PLC. Electrical, mechanical, cooling and controls in one shift.'),
        ('Perform preventive and corrective maintenance in accordance with approved EOPs, MOPs, and SOPs',
         'Preventive and corrective maintenance on service contracts and in utility operations '
         '(2017-2026) to approved procedures: LOTO, APV and work instructions as written. I follow '
         'the document, and improve it when reality proves it wrong.'),
        ('Respond to incidents, support troubleshooting and recovery activities, and lead response efforts when appropriate',
         'Incident response on call at Biofos (2017-2022) and acute call-outs at ELOHVAC (2023-2026): '
         'troubleshoot, recover, lead when I was first on site. Night work with production waiting.'),
        ('Identify and escalate safety, compliance, and operational risks in line with Microsoft standards',
         'Near-miss reporting and risk assessment at Biofos, zero critical deviations in ELOHVAC '
         'service agreements (2023-2026), GMP compliance at Novo Nordisk. Risks escalated early, '
         'not after.'),
        ('Collaborate with internal teams, vendors, and cross-functional stakeholders to ensure safe and high-quality execution',
         '25 specialists across engineering, procurement and operations at Novo Nordisk (2022-2024), '
         'subcontractors and suppliers at Ventek and ELOHVAC. Safe and high-quality execution in '
         'every handover.'),
        ('Contribute to continuous improvement by sharing knowledge, supporting peers, and developing technical capability over time',
         '5S and Standard Work at Biofos, PDCA with 40% lower energy costs at Novo Nordisk, training '
         '5 electricians and 3 apprentices at ELOHVAC. Knowledge shared, not kept.'),
        ('Upper secondary education (vocational or general upper secondary school) or equivalent practical work experience',
         'HF, general upper secondary (VUC, 2012-2017), plus B.Tech (EQF6) in Technology Management '
         'and Mechanical Engineering. Beyond that, 20+ years of practical technical work since 2003.'),
        ('Some prior experience in technical work',
         'Technical work in demanding environments: industrial maintenance (ARJ, 2003-2010), '
         'electrical and HVAC installations (ELOHVAC, 2023-2026), energy and process facilities '
         '(Biofos, Novo Nordisk, 2017-2024).'),
        ('valid driver\'s license',
         'Driver\'s license category B (manual) since 2003, used daily between sites, customers and '
         'suppliers. Trips between the three Greater Copenhagen sites are part of the rhythm.'),
        ('Ability to work rotating shift patterns in a 24/7 operational environment',
         'Rotating shifts and on-call in a 24/7 environment for 4.5 years (Biofos, 2017-2022), '
         'nights included. The 2-2-7 rotation with seven days off after each block suits me; I have '
         'confirmed it.'),
        ('Ability to communicate effectively in English',
         'English in professional use since 2017: GMP documentation at Novo Nordisk, meetings and '
         'written handovers. I communicate effectively in English, in speech and in writing.'),
        ('Technical certification in electrical, mechanical, HVAC, or a related field',
         'Certifications across the fields: authorised electrical engineer LV/MV/HV (2023), '
         'refrigeration and air conditioning AMU (2021), STCW marine technical (2021-2023), B.Tech '
         'in mechanical engineering.'),
        ('Experience working with CMMS systems',
         'CMMS and maintenance systems in daily use: SAP ERP at Novo Nordisk for records and cost, '
         'service documentation and digital checklists at ELOHVAC, workshop routines at Biofos '
         '(2017-2022). Records kept as the work is done.'),
        ('Experience in high-availability, mission-critical, or safety-critical environments',
         'Direct high-availability experience: 24/7 utility operations at Biofos (2017-2022) where '
         'the plant could not stop, and GMP-controlled commissioning at Novo Nordisk with zero '
         'critical findings at handover.'),
        ('Exposure to industrial, electrical, mechanical, cooling, or control systems',
         'Hands-on across all five since 2003: industrial machinery (ARJ), electrical and cooling '
         '(ELOHVAC, Ventek), mechanical and control systems (Biofos SCADA/PLC, Novo commissioning).'),
        ('strong safety mindset, sound technical judgment',
         'Safety mindset and judgment built in 24/7 operations: LOTO, APV and risk assessment as '
         'routine, decisions documented. Procedure-driven environments are my preference; the '
         'structured way is faster.'),
        ('STOP WORK authority',
         'STOP WORK thinking is how I already work: at Biofos (2017-2022), LOTO and near-miss reporting meant '
         'the job stopped until it was safe, and everyone had that right. I would use the authority '
         'as intended.'),
        ('Microsoft Cloud Background Check',
         'Ready for the Microsoft Cloud Background Check upon hire and for ongoing compliance; I '
         'expect no issues on my side. Background from critical '
         'infrastructure and GMP-controlled projects since 2017.'),
                   ], widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo — application for Critical Environment Technician (CET), '
                       'Microsoft')
    print(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_Microsoft_CriticalEnvironmentTechnician.docx'))
