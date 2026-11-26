# -*- coding: utf-8 -*-
"""Senior Wafer-Scale Cryogenic Probing Engineer — Microsoft Quantum, Denmark lab.

English JD -> en-GB document, 4 sider i masterdesign: letter p1, CV p2-3, kravmatrix p4.
No named contact -> greeting "Dear Microsoft Quantum team,". Anden Microsoft-ansøgning
(#422 CET): intet genbruges derfra — ny åbning, nyt register, ny struktur, ny hilsen.

STILVALG (style_guard godkendt, 3/3 skift mod #422):
  register     = Reproducible by design (practical · methodical · documentation · safety ·
                 rapid evolution)
  åbningsgreb  = AX (målekædens fysik: en lille wiring-fejl i toppen bliver til en eftermiddag
                 tabt i bunden; ground loops og connector-fejl som dagligt materiale)
  struktur     = Chain, bench, memory (cryo-kæden · målebænken · vidensdokumentationen)

BRUGERENS KORREKTION + permanent regel: alt tekst humaniseret i letter OG CV, en-GB.
Ingen em dash. Brug sammentrækninger.

BRUGERBEKRÆFTET 25.11.2026 (byg alligevel, gaps SYNLYDE):
  - Kryogenisk erfaring: INGEN ("nej, kun køleteknik") — må ikke påstås; køleteknik/HVAC som
    naboområde + ærlig rampe-plan. Også i matrix som honest gap.
  - Statsborgerskab: iransk + dansk opholdstilladelse — eksportkontrol (ITAR/EAR/EU Dual Use)
    skrives ærligt med pas-verifikation; Microsoft vurderer eligibilitet.
  - Ingen kandidatgrad i fysik/elektronik -> "equivalent experience"-ruten (B.Tech EQF6 + EQF6
    elteknik + elautorisation + 20+ år). Pyntes ikke.
  - Quantum device physics: ingen erfaring (preferred) — ærligt gap.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Microsoft Quantum · Senior Wafer-Scale Cryogenic Probing Engineer'
BANNER_RESUME = 'Hardware diagnostics and commissioning · methodical hands'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('25 November 2026')
    m.meta('Denmark lab · Microsoft Quantum · wafer-scale cryogenic probing')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Senior Wafer-Scale Cryogenic Probing Engineer',
           bold=True, color='1A1A1A')
    m.para('Dear Microsoft Quantum team,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('In a measurement chain that runs from room temperature down to 1.5 K, a small wiring '
       'fault at the top becomes an afternoon lost at the bottom. Ground loops, connector '
       'faults and system-level failures are the daily material of this work, and the labs '
       'that handle it well stay methodical about hardware, documentation and safety. You '
       'want reliable wafer scale cryogenic measurement capabilities for the Microsoft '
       'Quantum program; keeping a setup like that reproducible is a craft I know from '
       'adjacent ground, and I will come back to exactly how far that adjacency reaches.')

    lp('The program itself is hard not to admire: the world\'s first scalable quantum '
       'computing system, built with a full-stack approach from fundamental physics to cloud '
       'integration, and the chance to help shape transformative technology with theoretical '
       'and experimental physicists, hardware designers, and software engineers around the world. The mission line behind it, to '
       'empower every person and every organization on the planet to achieve more, is the kind '
       'of sentence I take literally. Growth mindset, innovate to empower '
       'others, collaborate to realize our shared goals: that reads like a lab notebook '
       'entry, not a poster. And respect, integrity, and accountability are the right '
       'backbone for a culture of inclusion where everyone can thrive at work and beyond.')

    lp('One line in your responsibilities is my most recent work written out verbatim: '
       'design and build AI agents/copilots to document procedures, hardware configurations, '
       'and maintenance activities. Since 2024 I have built exactly that kind of system with '
       'LLM APIs and agentic frameworks, for checklists, maintenance documentation and '
       'knowledge sharing, with review standards before anything reaches a colleague. The '
       'hardware side underneath it is 20+ years old: diagnostics and fault finding on '
       'electro-mechanical systems since 2003, integration and validation of wiring, '
       'connectors and measurement instrumentation through 37 commissioning projects with zero '
       'critical findings at handover. Add inventory habits, procurement discipline and a '
       'safety record without critical deviations, and the picture is complete.')

    lp('So the honest list, which I would rather write myself. I have not worked with '
       'cryogenic systems; my cold-side background is refrigeration and climate, not 1.5 K, '
       'and the cryogenic ramp would be steep and deliberate. No device physics or quantum '
       'transport measurements either. I hold no Master\'s degree in physics or electronic '
       'engineering; my case is the equivalent-experience route, a B.Tech (EQF6) plus EQF6 '
       'electrical engineering, an authorised electrical engineer certificate and 20+ years '
       'hands-on. On the security side: I am an Iranian national with a Danish residence '
       'permit, ready for the Microsoft Cloud Background Check and able to verify my status '
       'with a valid passport. The export-control eligibility assessment under ITAR/EAR and '
       'the EU Dual Use rules is yours to make; I flag my status early rather than late.')

    lp('What I would bring on day one is the practical, collaborative, and methodical '
       'approach the role asks for, and a record of robust and reliable lab operations in '
       'spirit if not in that exact lab: a 24/7 plant that could not stop, commissioning '
       'with zero critical findings at handover, inventory and procurement run tight, and '
       'safety standards upheld and improved rather than laminated. Smooth lab operations '
       'come from people who document what they do, and that has been my habit for years. A '
       'rapidly evolving technology environment does not unsettle me; I like work where the '
       'answer is not in the back of the book.')

    lp('The first 90 days I have written as a plan on page 3 of the CV, in three steps: '
       'learn the chain, own the bench, build the memory. I can start at short notice, and '
       'I look forward to the conversation, including the hard questions about the cryogenic '
       'gap.', after=44)

    m.para('Kind regards,', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFILE')
    m.para('Hands-on hardware engineer: diagnostics, commissioning and validation of '
           'electro-mechanical and instrumentation systems since 2003. Python and AI agents '
           'built for documentation and maintenance records. Cold-side background is '
           'refrigeration and climate, not cryogenics, and the quantum domain is new to me; '
           'the methodical habits, the diagnostics and the documentation culture transfer '
           'directly.', after=32)

    m.section('EXPERIENCE')
    jobs = [
        ('CTO for the AI department and authorised electrical engineer (electrical and ventilation)',
         'Data Power Consultant ApS · Copenhagen · 2024 – present (ELOHVAC electrical activities '
         'moved here in Nov. 2026)',
         'AI department 4-10 people · AI agents and LLM APIs · electrical service · 5 electricians + 3 apprentices',
         [('AI agents and documentation', 'Built AI agents and copilots with LLM APIs (Claude) for '
           'procedures, checklists, maintenance documentation and knowledge sharing. AI-assisted '
           'development as the department\'s standard process: code generation, review and test '
           'with shared acceptance standards.'),
          ('Python and automation', 'Python in daily use for automation, dashboards and '
           'documentation workflows; version control part of the development routine. For commercial '
           'clients, electrical service and fault finding kept running alongside.')]),
        ('Owner / technical director / authorised electrical engineer',
         'ELOHVAC ApS · Copenhagen · May 2023 – November 2026 (company closed)',
         'Commercial customers · electrical, ventilation and climate · contracting · full P&L · service agreements',
         [('Diagnostics and repair', 'Fault finding on electrical, ventilation and climate systems '
           'from acute call-outs to finished installations. Ground loops, wiring faults and '
           'system-level failures diagnosed to root cause, A3 and 5 Whys when issues had to stay '
           'fixed.'),
          ('Inventory and procurement', 'Hardware inventory, materials and tooling tracked '
           'daily; procurement, supplier coordination and restocking run end to end. LOTO, APV '
           'and risk assessment at site start-up; zero critical deviations in the service '
           'agreements.'),
          ('Teaching and standards', 'Led 5 electricians and 3 apprentices: structured training, '
           'hands-on demonstrations, work instructions written so others could follow them.')]),
        ('Senior commissioning engineer / project manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · November 2022 – July 2024',
         '37 CAPEX projects, DKK 2–10 mio. each · 25 specialists · GMP/FDA/EMA',
         [('Integration and validation', 'Wiring, connectors, panels and measurement '
           'instrumentation integrated and validated after FAT/SAT and IQ/OQ/PQ, zero critical '
           'findings at handover. Electrical systems throughout: switchgear and controls, UPS, emergency '
           'lighting, ABA/ABV, PDS.'),
          ('Multidisciplinary teamwork', '25 specialists across engineering, procurement and '
           'operations; software and engineering teams collaborated with daily. Monthly reports '
           'on progress, cost, risks and resources to leadership and client management. SAP ERP.')]),
        ('Project and workshop manager', 'Ventek-Air · Copenhagen · January 2022 – November 2022',
         '11 concurrent projects · 14-person team · subcontractors and logistics',
         [('Hardware in motion', '11 concurrent projects: equipment and materials handled from '
           'loading and shipping to relocation and restocking, subcontractors coordinated, '
           'safety documentation and handover packages in every project.')]),
        ('Maintenance and operations manager / workshop technician',
         'Biofos (Lynetten) · Copenhagen · August 2017 – January 2022',
         '24/7 operations · SCADA, PLC, HV switchgear · rotating shifts',
         [('Tracking issues to closure', 'Pumps, HVAC, HV switchgear, SCADA and PLC kept running '
           'around the clock: diagnostics, preventive and corrective maintenance, incident '
           'response and recovery. Reservedelsflow and lagerstyring in the workshop; 5S and '
           'Standard Work as routine.'),
          ('Safety as habit', 'LOTO, APV, risk assessment and near-miss reporting across 4.5 '
           'years of shift work. The job stopped until it was safe; everyone had that right.')]),
        ('Electromechanical technician / production team leader',
         'ARJ Engineering · Tehran · December 2003 – March 2010',
         '12 mechanics and technicians · machine shop · product line',
         [('Diagnostic foundations', 'Led 12 mechanics and technicians: shift planning, materials '
           'and goals. Fault diagnosis on industrial electromechanical equipment, root-cause '
           'analysis and corrective actions followed to closure.')]),
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
    m.bullet('Hardware diagnostics', 'Ground loops, wiring faults, connector issues and '
             'system-level failures on electro-mechanical setups. Root-cause analysis (5 Whys, '
             'Ishikawa, A3), issues tracked to closure in records.', after=10)
    m.bullet('Integration and validation', 'Wiring, connectors, filters and measurement '
             'instrumentation integrated and validated; commissioning protocols (FAT/SAT, '
             'IQ/OQ/PQ) executed with documentation that holds.', after=10)
    m.bullet('AI agents and documentation', 'Agents/copilots for procedures, hardware '
             'configurations and maintenance documentation (LLM APIs, Python). Knowledge '
             'sharing and reproducibility as design goals, not afterthoughts.', after=10)
    m.bullet('Inventory and safety', 'Hardware inventory, procurement and restocking in lab-like '
             'environments. Safety standards upheld and improved: LOTO, APV, risk assessment, '
             'near-miss reporting. Lean/Six Sigma practice, not certified: DMAIC, 5S, PDCA, A3, '
             'Standard Work, 5 Whys, Ishikawa, FMEA.', after=10)

    m.section('THE FIRST 90 DAYS')
    m.para('Three steps, named after your own setup:', after=8)
    m.bullet('Days 1-30 · Learn the chain', 'The cryogenic chain from the inside: systems, '
             'instrumentation and safety standards walked with the team, procedures read, '
             'questions written down. Goal: a documented walkthrough of one full measurement '
             'chain, done under supervision.', after=10)
    m.bullet('Days 31-60 · Own the bench', 'Hardware issues diagnosed and resolved on live '
             'setups, assistance in 1.5 K measurement execution, inventory and procurement '
             'routines taken over. Goal: issues I can close alone, records kept current.', after=10)
    m.bullet('Days 61-90 · Build the memory', 'AI agents/copilots for documenting procedures, '
             'hardware configurations and maintenance, plus one safety or workflow improvement. '
             'Goal: one working documentation agent and one improvement with a measurable effect.',
             after=10)

    m.section('LANGUAGES, TOOLS AND PRACTICAL')
    m.para('Danish (native) · English (professional, daily working language since 2017) · '
           'Persian (native). Python, LLM APIs (Claude), AI agent frameworks, SAP ERP, SCADA, '
           'PLC, Power BI. PRINCE2. Valid driver\'s license B (manual). Based in Måløv. Ready '
           'for the Microsoft Cloud Background Check; Iranian national with Danish residence '
           'permit, passport verification ready. Available at short notice.', after=32)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Wafer-scale cryogenic probing · requirements and evidence',
                   ('Requirement', 'Evidence'),
                   [
        ('Build and maintain and utilize wafer-scale cryogenic hardware systems for quantum device screening and measurement',
         'Honest adjacency: no cryogenic systems yet. Hardware build-and-maintain record is '
         'electro-mechanical (pumps, HVAC, switchgear, process skids, 2003-2026), and '
         'utilisation of measurement-critical setups (37 commissioning projects) transfers. The '
         'cryogenic part is the planned ramp.'),
        ('Diagnose, track and resolve hardware issues in cryogenic setups (e.g., ground loops, wiring faults, or system-level failures)',
         'Ground loops, wiring faults and system-level failures are familiar enemies: electrical '
         'fault finding since 2003, root-cause analysis (5 Whys, Ishikawa, A3) at ARJ, Biofos '
         'and Novo Nordisk. Tracking to closure in records is habit; the cryogenic setups '
         'themselves are new.'),
        ('Integrate and validate hardware components such as wiring, connectors, filters, and measurement instrumentation for data acquisition',
         'Integration and validation is my commissioning core: wiring, connectors and measurement '
         'instrumentation tested after FAT/SAT and IQ/OQ/PQ on 37 projects (2022-2024), zero '
         'critical findings at handover. Data-acquisition discipline from SCADA, PLC and '
         'instrumentation work.'),
        ('Assist in 1.5 K measurement execution and collaborate with software and engineering teams to support robust and reliable lab operations',
         '1.5 K execution is new; I would assist, not lead, at first. The collaboration side is '
         'proven: software and engineering teams worked with daily at Novo Nordisk (25 '
         'specialists, 2022-2024) and in an AI department (4-10 people, 2024-2026).'),
        ('Design and build AI agents/copilots to document procedures, hardware configurations, and maintenance activities for knowledge sharing and reproducibility',
         'This line is my recent work verbatim: AI agents and copilots built with LLM APIs '
         '(Claude) for procedures, checklists and maintenance documentation (2024-2026), designed '
         'for knowledge sharing and reproducibility, with review standards before anything shipped.'),
        ('Manage and track hardware inventory',
         'Inventory tracked in real environments: reservedelsflow and lagerstyring at Biofos '
         '(2017-2022), material control and logistics at Ventek (11 projects, 2022), stock and '
         'tooling as ELOHVAC owner (2023-2026). Kept current, not reconstructed later.'),
        ('coordinate procurement and restocking',
         'Procurement and restocking coordinated as owner and project lead: suppliers, prices and '
         'delivery at ELOHVAC (2023-2026), materials for 11 concurrent projects at Ventek (2022).'),
        ('Uphold and improve safety standards and practices in the cryogenic lab environment',
         'Safety practice ingrained and transferable: LOTO, APV, risk assessment and near-miss '
         'reporting (2017-2026), zero critical deviations in service agreements. Cryogenic lab '
         'specifics I would learn from your standards; the uphold-and-improve habit is there.'),
        ('Master\'s or higher degree in Physics, Electronic Engineering or a related field (or equivalent experience)',
         'Honest: no Master\'s degree. The equivalent-experience route: B.Tech (EQF6) Technology '
         'Management and Mechanical Engineering, EQF6 electrical engineering, authorised '
         'electrical engineer (LV/MV/HV), 20+ years hands-on (2003-2026).'),
        ('Hands-on experience with cryogenic systems for electronic characterization',
         'Honest gap: no hands-on cryogenic experience. Cold-side background is refrigeration and '
         'climate (AMU 2021, HVAC work 2023-2026), not 1.5 K systems. Methodical hardware '
         'handling, instrumentation and diagnostics transfer; the ramp would be steep and '
         'deliberate.'),
        ('Proven troubleshooting and diagnostic skills for hardware and measurement setups',
         'Troubleshooting proven over 20+ years: industrial electromechanical diagnostics (ARJ, '
         '2003-2010), 24/7 fault finding (Biofos, 2017-2022), measurement-critical commissioning '
         '(Novo Nordisk, zero critical findings at handover).'),
        ('Proficiency in Python (or similar) for measurement automation and Git for version control and documentation',
         'Python in daily use for automation and documentation (2024-2026); Git part of the '
         'AI-assisted development workflow with code review and shared standards. Measurement '
         'automation is a new context for tools I already use daily.'),
        ('Ability to work collaboratively in a multidisciplinary team and communicate technical findings clearly',
         'Multidisciplinary by default: 25 specialists across engineering, procurement and '
         'operations (2022-2024), electricians, VVS and automation in one team (2023-2026). '
         'Findings communicated clearly in reports and handovers, Danish and English.'),
        ('Experience with device physics and quantum transport measurements',
         'Honest gap on the preferred list: no device physics or quantum transport measurements. '
         'Characterisation fundamentals from electrical instrumentation and commissioning work '
         '(2022-2024) are in place; the quantum physics I would study alongside the team.'),
        ('Experience managing hardware inventory and procurement processes in a lab environment',
         'Closest lab-type environments: workshop and spare-parts control at a 24/7 plant '
         '(2017-2022), equipment receiving and installation at Novo Nordisk (2022-2024). '
         'Procurement processes run end to end as company owner (2023-2026).'),
        ('Experience with AI and agentic frameworks',
         'Direct: LLM APIs and AI agents designed and shipped (2024-2026), AI-assisted development '
         'as department standard, prompt- and agent design as working tools. This qualification I '
         'meet squarely.'),
        ('Microsoft Cloud Background Check',
         'Ready for the Microsoft Cloud Background Check upon hire and every 2 years after. On '
         'export control: Iranian national with Danish residence permit, status verifiable with '
         'valid passport; the ITAR/EAR and EU Dual Use eligibility assessment is Microsoft\'s to '
         'make, and I flag it early.'),
                   ], widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo — application for Senior Wafer-Scale Cryogenic Probing '
                       'Engineer, Microsoft Quantum')
    print(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_MicrosoftQuantum_SeniorWaferScaleCryogenicProbingEngineer.docx'))
