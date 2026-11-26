# -*- coding: utf-8 -*-
"""Quality Manager, Quality Assurance for Product & Solutions — Terma, Lystrup
(Requisition ID 1631, engelsk opslag -> en-GB dokument).

4 sider i masterdesign: brev side 1, CV side 2-3, kravmatrix side 4.
Kontakt: Hiring Manager, AUG@terma.com (intet navn) -> "Dear Hiring Manager,".
Resume påkrævet, cover letter valgfrit (vi laver masterdesignet alligevel). Ingen foto/
alder (Terma beder om at udelade personlige detaljer) ✓. Ansøgning kun via terma.com.

STILVALG (style_guard godkendt, 3/3 skift mod #430 Brøndby Fjernvarme):
  register    = Mission-critical quality (compliance · customer · delivery · trust)
  åbningsgreb = BG (caught in the proposal review or caught in the field: en
                kvalitetsfejl fanget tidligt koster et møde, fanget sent koster en mission)
  struktur    = Identify, embed, verify (identify · embed · verify)

BRUGERSVAR 26.11 (bindende):
  (1) SECURITY CLEARANCE: "Jeg har dansk permanent opholdstilladelse" -> skriv bekræftelsen
      på fakta-grundlaget: dansk permanent opholdstilladelse, bosat og arbejdet i Danmark
      siden 2010 (7+ år i NATO/EU), klar til vurdering ved FE. Iransk statsborgerskab
      nævnes ikke i brevet (brugerens valg), men nævnes i rapportens tjekpunkter.
  (2) LYSTRUP: flytter til Aarhus-området HVIS jobbet er det rigtige.
  (3) AUDITS + ISO: reel erfaring — well-documented project og process audits + ISO 9001
      QMS skrives selvsikkert (brugeren har kompetencerne; formuleringen er min opgave).

BANNED (README): "proven track record" (står i JD'en! citeres ALDRIG), "demonstrated
ability", robust, dynamic, results-driven, leveraged, spearheaded, innovative solutions,
seamlessly. "Demonstrate/demonstrated"-former undgås helt. Ingen em dash. Sammentrækninger
(I'm, don't, it's, I'd, I'll).
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Terma · Quality Manager, Lystrup'
BANNER_RESUME = 'Audits · compliance · quality assurance · project delivery'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('26 November 2026')
    m.meta('Requisition ID 1631 · Quality Assurance for Product & Solutions')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Quality Manager, Lystrup (Requisition ID 1631)',
           bold=True, color='1A1A1A')
    m.para('Dear Hiring Manager,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('A quality requirement caught in a proposal review costs a meeting. Caught in the '
       'field, it costs a mission. In defense and aerospace there\u2019s no acceptable '
       'version of the second sentence, and that\u2019s the standard I read all the way '
       'through your posting for the Quality Manager role in Lystrup.')

    lp('Terma builds mission-critical solutions for the defense and aerospace industry '
       'with the purpose of securing people through advanced technology: real-world '
       'solutions that matter to the security of people on land, at sea and in the air. '
       'The Quality Manager\u2019s job in that picture is plain: quality standard and '
       'customer requirements are systematically identified and embedded across projects '
       'and product development activities, and you evaluate quality standards and secure '
       'compliance throughout the project life cycle. We care about the work we do and '
       'the people behind it, and quality is essential in every line of the posting.')

    lp('The team is a team of Quality Managers, working within different Business Areas, '
       'developing people and technology, and the work spans proposals, projects and '
       'suppliers: proposal and contract reviews, the Quality Assurance Plan (QAP) with '
       'effective flow-down to suppliers, and milestone meetings. I\u2019ve done that '
       'shape of work since 2003: quality requirements identified early, documented '
       'through the project, and verified at handover. Where I come from the last part is '
       'called FAT/SAT and IQ/OQ/PQ, and the standard is zero critical findings.')

    lp('Two qualifications deserve direct answers. EASA Part 21 and Part 145, or the '
       'EMAR equivalents, are aviation frameworks I know by their logic rather than by '
       'project use; my regulatory background is GMP, FDA and EMA requirements in '
       'pharmaceutical projects, plus STCW maritime rules and Danish electrical '
       'regulation. The regulatory discipline is the same: documented requirements, '
       'flowed down and verified. On the systems side I\u2019m on firm ground: '
       'system-level interactions between mechanical, hardware, and software components '
       'are exactly what SCADA/PLC plants, process equipment and my current work with AI '
       'and embedded systems demand. Audits and quality management systems I know in '
       'practice: well-documented project and process audits, ISO 9001-based systems, '
       'and continuous improvement as a working method.')

    lp('The mindset you describe is work I recognise: an analytical mindset with a '
       'generalist perspective, a structured and objective approach to quality '
       'requirements, and the ability to prioritize when several projects pull at once. '
       'Taking ownership and delivering results with confidence is the only way 37 '
       'parallel projects, or a 24/7 plant, has ever been run. English I use '
       'professionally every day, in writing and verbally; the global business mindset '
       'is a habit from teams in Denmark, Iran and colleagues across Europe.')

    lp('On the conditions at the end of the posting: I hold a Danish permanent residence '
       'permit and have lived and worked in Denmark since 2010, well past the '
       'seven-year NATO/EU requirement. I\u2019m ready for the evaluation by the Danish '
       'Defence Intelligence Service. On location: Lystrup is a move I\u2019m open to for '
       'the right job, and up to two days at home fits how I work. Terma promises great '
       'people, challenging tasks, and the opportunity to make an impact, in a culture '
       'built on trust, collaboration, and knowledge sharing where learning is embedded '
       'in everyday work; that\u2019s the environment I do my best work in. A short talk '
       'with you before the process would be welcome, and my resume is attached as the '
       'posting requires.', after=44)

    m.para('Kind regards,', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFILE')
    m.para('Twenty-plus years at the meeting of quality and project management in '
           'regulated, technical environments: GMP/FDA/EMA documentation, FAT/SAT and IQ/OQ/PQ verification, '
           'and quality requirements managed from proposal to buy-off. System-level '
           'understanding across mechanical, hardware and software. B.Tech (EQF6) '
           'engineering, PRINCE2, and daily practice with audits and ISO 9001 quality '
           'management systems.', after=32)

    m.section('EXPERIENCE')
    jobs = [
        ('CTO, AI Department & Authorised Electrical Engineer',
         'Data Power Consultant ApS · Copenhagen · 2024 – present (ELOHVAC\u2019s '
         'electrical activities added Nov. 2026)',
         'AI department 4-10 people · Python, LLM agents · quality-verified deliveries',
         [('Verification in AI delivery', 'Deliverables verified against requirements '
           'before handover: reviews, documentation and structured follow-up for the '
           'output of 4-10 specialists. ISO 9001-based working methods and documented '
           'processes as the daily standard.')]),
        ('Owner / Technical Director / Authorised Electrical Engineer',
         'ELOHVAC ApS · Copenhagen · May 2023 – Nov. 2026 (company closed)',
         'Commercial customers · HVAC and electrical · full P&L · service agreements',
         [('Customer complaints and quality targets', 'Service agreements with response-'
           'time and quality targets; customer complaints handled and closed with '
           'corrective action and root-cause analysis. Buy-off of every delivery before '
           'the customer saw it.'),
          ('Supplier flow-down', 'Subcontractors and suppliers held to the same '
           'documentation and quality requirements as our own work, with changes and '
           'claims assessed against the contract.')]),
        ('Senior Commissioning Engineer / Project Manager, Electrical Systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · Nov. 2022 – Jul. 2024',
         '37 CAPEX projects, DKK 2-10 m · 25 specialists · GMP/FDA/EMA',
         [('Documented verification', 'FAT/SAT and IQ/OQ/PQ protocols authored and '
           'executed; quality requirements flowed down through 25 specialists and '
           'suppliers. Zero critical findings at handover across 37 projects, and '
           'well-documented project and process audits performed on documentation and '
           'workflows.')]),
        ('Project & Workshop Manager',
         'Ventek-Air · Copenhagen · Jan. 2022 – Nov. 2022',
         '11 parallel ventilation projects · 14 staff · subcontractors',
         [('Requirements in the contract stage', 'Quality requirements identified in '
           'proposal and contract work and flowed down to subcontractors across 11 '
           'parallel projects. Deliverables checked at handover, and extra work and '
           'claims assessed against requirements and documentation.')]),
        ('Maintenance & Operations Manager / Workshop Technician',
         'Biofos (Lynetten) · Copenhagen · Aug. 2017 – Jan. 2022',
         '24/7 operations · SCADA, PLC, HVAC · 10 employees · shifts',
         [('Process control and continuous improvement', 'Process control and documented '
           'routines around the clock: work instructions, safety procedures (LOTO, APV) '
           'and 5S/Standard Work in the workshop. PDCA and root-cause analysis as '
           'standing methods.')]),
        ('Electromechanical Technician / Production Supervisor',
         'ARJ Engineering · Tehran · Dec. 2003 – Mar. 2010',
         '12 mechanics and technicians · machine shop · product line',
         [('The foundation', 'Quality assurance, process control and documentation on the '
           'production line: work instructions, checks and root-cause analysis that '
           'changed how faults were handled.')]),
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
    m.bullet('QMS and continuous improvement', 'ISO 9001-based QMS in daily practice, plus '
             'GMP/FDA/EMA documentation discipline (Novo 2022-2024). Continuous '
             'improvement as method: PDCA, 5S, Standard Work and root-cause analysis.',
             after=10)
    m.bullet('Verification and buy-off', 'FAT/SAT, IQ/OQ/PQ and deliverable verification '
             'against requirements since 2003. Documented evidence, not opinions; zero '
             'critical findings at handover across 37 projects (Novo 2022-2024).',
             after=10)
    m.bullet('Requirements flow-down', 'Customer quality requirements identified early '
             'and flowed down to suppliers and teams: QAP-style structuring from contract '
             'to handover (Ventek 2022, ELOHVAC 2023-2026).', after=10)
    m.bullet('System-level engineering', 'Mechanical, hardware and software interactions: '
             'SCADA/PLC, process equipment, HVAC and AI systems. Root-cause work across '
             'disciplines.', after=10)
    m.bullet('Microsoft and tools', 'Microsoft applications strong: Excel, Word, Outlook, '
             'reporting. SAP ERP (Novo, ELOHVAC) and PRINCE2 for structure.', after=10)

    m.section('THE FIRST 90 DAYS')
    m.para('The plan follows the quality cycle itself: identify, embed, verify.', after=8)
    m.bullet('Days 1-30 · Identify', 'Meet the team of Quality Managers and the Business '
             'Areas; read the standards stack (MIL/NATO, AQAP 2110, ED-109A, DO-178) '
             'against live projects. Goal: requirements mapped across my area, and the '
             'gaps known.', after=10)
    m.bullet('Days 31-60 · Embed', 'QAPs running with effective '
             'flow-down to suppliers; proposal and contract reviews attended; customer '
             'complaints handling familiar. Goal: requirements embedded early, not '
             'checked late.', after=10)
    m.bullet('Days 61-90 · Verify', 'Buy-off discipline in place, compliance evaluations '
             'planned (EASA/EMAR where relevant), and a well-documented audit rhythm '
             'established. Goal: verified deliverables and a trusted quality advisor role '
             'with the projects.', after=10)

    m.section('LANGUAGES, TOOLS AND PRACTICALITIES')
    m.para('Languages: Danish (native), English (professional, fluent in writing and '
           'verbally), Persian (native). Microsoft applications, SAP ERP, Excel; PRINCE2. '
           'Driving licence B (manual). Based in Måløv; open to relocating to the Aarhus '
           'area for the right job. Danish permanent residence permit. Available by '
           'agreement.', after=32)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Quality Manager, Lystrup · requirements and evidence',
                   ('Requirement in the posting', 'Evidence'),
                   [
        ('Bachelor\u2019s or Master\u2019s degree in engineering, software or another '
         'relevant field',
         'Degree covered: B.Tech (EQF6) in Technology Management and Mechanical '
         'Engineering (2017-2022), electrical engineering at EQF6 (2000-2003) and '
         'PRINCE2. Engineering, with software understanding from daily AI work '
         '(2024-now).'),
        ('Minimum 3 years as Quality Manager or Project Manager, managing product '
         'development projects or managing quality requirement fulfilment',
         '20+ years combined: project management on 37 development projects (Novo '
         '2022-2024), quality requirement fulfilment under GMP/FDA/EMA, and '
         'product/service development with quality targets (ELOHVAC 2023-2026). Well past '
         'the 3-year minimum.'),
        ('Knowledge or experience with EASA Part 21 and/or Part 145 (or equivalent EMAR '
         'requirements) would be an advantage',
         'Regulatory work carried in parallel frameworks: GMP, FDA and EMA requirements '
         'applied across 37 projects (Novo 2022-2024), STCW maritime rules (2021-2023) '
         'and Danish electrical regulation (2023). The regulatory discipline is '
         'documented requirements, flowed down and verified.'),
        ('System-level interactions between mechanical, hardware, and software components',
         'Daily ground: SCADA/PLC systems with pumps, HVAC and instrumentation (Biofos '
         '2017-2022), process equipment with controls (Novo 2022-2024), and AI software '
         'with hardware (Data Power 2024-now). System-level thinking across the three is '
         'the working mode.'),
        ('Well-documented audits (project and process audits)',
         'Well-documented project and process audits performed in regulated environments: '
         'GMP work (2022-2024) and quality assurance practice since 2003, always with '
         'documentation, evidence and follow-up in the same trail.'),
        ('Strong skills in Microsoft applications',
         'Microsoft applications in daily use since 2003: Excel, Word, Outlook and '
         'reporting. SAP ERP (Novo 2022-2024, ELOHVAC 2023-2026) and structured '
         'documentation alongside.'),
        ('Experience with Quality Management Systems (ISO 9001 / AS 9100) and Continuous '
         'Improvement is an advantage',
         'ISO 9001-based quality management systems worked in daily practice, plus '
         'GMP/FDA/EMA systems (Novo 2022-2024). Continuous improvement as method: PDCA '
         '(energy case at Novo), 5S and Standard Work (Biofos 2017-2022), root-cause '
         'analysis (ARJ 2003-2010).'),
        ('Internal product development and customer projects, including Quality '
         'Assurance Plans and milestone meetings',
         'Across development and customer projects, quality is managed: 37 development '
         'projects with milestone follow-up (Novo 2022-2024), customer projects with '
         'quality targets (ELOHVAC 2023-2026, Ventek 2022). Quality plans structured like '
         'QAPs: requirements identified, flowed down, verified.'),
        ('Manage Customer Complaints efficiently to maintain high customer satisfaction',
         'Customer complaints handled and closed: service agreements with response-time '
         'and quality targets (ELOHVAC 2023-2026), corrective actions with root-cause '
         'analysis (ARJ, Biofos). Satisfaction maintained by follow-through, not '
         'explanation.'),
        ('Perform Buy-Off, verifying that deliverables meet the required quality standards',
         'Buy-off discipline since 2003: FAT/SAT and IQ/OQ/PQ verification (Novo '
         '2022-2024), deliverable checks at handover (Ventek 2022, ELOHVAC 2023-2026), '
         'zero critical findings at handover across 37 projects.'),
        ('Manage Concessions (Deviations and Waivers) and customers delegation (GQAR, DCMA)',
         'Deviations and changes assessed against contracts and requirements: extra work '
         'and claims evaluated (Ventek 2022), changes calculated and documented (Novo '
         '2022-2024), always with the documentation such delegations require.'),
        ('Compliance with aviation regulatory requirements (EASA Part 21 and/or Part 145, '
         'or equivalent EMAR requirements) where relevant',
         'Regulatory compliance carried before: GMP/FDA/EMA across 37 projects (Novo '
         '2022-2024), maritime STCW (2021-2023) and electrical regulation (2023). '
         'Structured compliance with documented evidence is the method applied to each '
         'framework.'),
        ('Compliance evaluations concerning MIL and NATO quality standards and software '
         'standards (AQAP 2110, ED-109A, DO-178)',
         'Standards evaluated against requirements is familiar work: GMP standards across '
         'projects (Novo 2022-2024), quality standards implemented and documented (ARJ '
         '2003-2010). MIL and NATO quality standards and software standards (AQAP 2110, '
         'ED-109A, DO-178) are the frameworks for the evaluations.'),
        ('Provides input and support to Business Areas and projects, often as a trusted '
         'quality advisor',
         'Advisory role held in practice: quality sparring across engineering, procurement '
         'and operations (Novo 2022-2024), technical guidance to customers and teams '
         '(ELOHVAC 2023-2026). Trusted because the advice comes with documentation.'),
        ('Analytical mindset, generalist perspective, strong drive and natural curiosity',
         'Generalist across disciplines by training and habit: mechanical, electrical, '
         'software and process. Analytical mindset in root-cause work (ARJ, Biofos), and '
         'curiosity that has kept 20+ years of learning going, from SCADA to LLM agents.'),
        ('Structured and objective approach, with the ability to prioritize',
         'Structure where stakes are high: PRINCE2-structured delivery across 37 projects '
         '(Novo 2022-2024), prioritisation across 11 parallel projects (Ventek 2022), '
         'objective documentation standards in GMP.'),
        ('Strong execution skills, solution-oriented manner, taking ownership and '
         'delivering results with confidence',
         'Execution with ownership: 37 projects delivered on time, cost and quality (Novo '
         '2022-2024), company built and run with full responsibility (ELOHVAC 2023-2026), '
         'results delivered in 24/7 operations (Biofos 2017-2022).'),
        ('Global business mindset, acting positive, outgoing and independent',
         'International by default: teams in Denmark and Iran, colleagues across Europe, '
         'professional English daily. Independent and outgoing in customer-facing work '
         '(Ventek 2022, ELOHVAC 2023-2026), positive with the people behind the work.'),
        ('Fluent in English both in writing and verbal at a professional level',
         'English used professionally in writing and verbally: documentation, reporting '
         'and meetings (Novo 2022-2024), customer dialogue (Ventek, ELOHVAC), technical '
         'instruction since 2010. Danish and Persian native.'),
                   ], widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo — Quality Manager, Terma')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Terma_QualityManager.docx')
    build(out)
    print(out)
