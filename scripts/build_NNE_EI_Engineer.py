# -*- coding: utf-8 -*-
"""NNE (Novo Nordisk Engineering) — Electrical & Instrumentation Engineer, Kalundborg (req5138).

English deliverable (JD is English): task-first application page + CV in one document.
The posting asks for no cover letter but for a few sentences on motivation in the CV,
so page 1 carries the motivation and the CV follows it.
Culture and role intel: master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md (NNE section).
Policy: master/README.md — extreme confidence, no caveats.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Electrical & Instrumentation · Instrumented design, commissioning and validation'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('5 November 2026')
    m.meta('NNE A/S · Kalundborg · Electrical & Instrumentation Engineer (req5138)')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Application: Electrical & Instrumentation Engineer', bold=True, color='1A1A1A')
    m.para('Dear Søren Hedegaard', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('An instrument is a promise. That the temperature on the screen is the temperature in the pipe, that the '
           'valve moves when the loop tells it to, and that the safety function works when everything else has '
           'failed. In an API plant that promise is what separates a released batch from a rejected one — and '
           'keeping it is the whole job of an E&I engineer: specify it correctly, document it honestly, test it in '
           'the field and prove it in the qualification. That is the work I want to do at NNE.', after=80)

    m.para('**I work from four fixed points.** First, design out from the P&ID: instrument index and datasheets, '
           'measuring principle chosen for the medium and the range, materials and process connection, hazardous '
           'area and zone, and — where the function is safety-related — the SIL target and the SIS architecture that '
           'follows from it. Second, verify in the field: loop checks against the IO list, calibration, stroke and '
           'response tests on actuators, and functional testing of the interlock before anyone signs anything. '
           'Third, validation with evidence: IQ/OQ/PQ with a traceability matrix from requirement to test, deviations '
           'closed with a cause and a verified corrective action, and change control before the change rather than '
           'after it. Fourth, the vendor and construction interface: agreed scope, agreed interface list, FAT before '
           'shipment, and supervision on site where the work happens — because that is where the detail that nobody '
           'specified becomes a problem.', after=80)

    m.para('I have done this inside Novo Nordisk, your customer. From 2022 to 2024 I was senior commissioning '
           'engineer and project manager for electrical systems in Kalundborg and Bagsværd: 37 parallel capital '
           'projects, 25 specialists and DKK 2–10m per project, with acceptance criteria, IO and instrument '
           'documentation, panel and cable schedules, loop checks, FAT/SAT, IQ/OQ/PQ, deviation handling and audited '
           'handover — zero critical findings under GMP, FDA and EMA. I have stood in the design review, in the '
           'panel workshop and on the steel with the installer, and I have defended the documentation in front of an '
           'inspector.', after=80)

    m.para('The hands-on side is not a gap in my CV, it is where I come from. Five years as maintenance and operations '
           'manager at Biofos on a 24/7 plant: sensors, transmitters, actuators, pumps, HVAC and high-voltage '
           'switchgear, alarms and drift handled from SCADA data, calibration and fault diagnosis on the spot, and '
           'LOTO and permits before anything was touched. Since 2023 I have run ELOHVAC with five electricians and '
           'three apprentices — panels, motor controls, variable speed drives and control systems for heating, '
           'ventilation and cooling — where the specification, the installation, the test and the customer are the '
           'same day\'s work. Before that, twelve technicians and a machine workshop at ARJ.', after=80)

    m.para('The technical foundation fits what you ask for. I am an **authorised marine engineer** — the degree you '
           'list — with Danish electrical authorisation at LV, MV and HV, and a B.Tech in Technology Management & '
           'Mechanical Engineering with electrical engineering studies behind it. Marine engineering is exactly the '
           'discipline that teaches you to trust a measurement: pressure, temperature, flow, level and vibration, '
           'the instrumentation that reads them, and the control loop that acts on them. I read the P&ID, the '
           'single-line diagram, the instrument datasheet and the loop drawing, and I know which of the four '
           'usually disagrees with the other three. A department of a hundred engineers is also a place where '
           'standards travel: what one project documents well, the next one reuses — and I would rather work where '
           'the discipline is bigger than one person.', after=80)

    m.para('NNE\'s values are the ones I already work by. **Take initiative and get things done**: an open point in '
           'the field is closed the same week, not carried to the next milestone. **Be passionate about pharma '
           'engineering expertise**: the datasheet and the test record are the product. **Innovate and create '
           'efficient solutions**: a reusable checklist or template is worth more than a heroic evening. **Team up '
           'and leverage our global knowledge**: the answer often already exists in another discipline or another '
           'country. And **exceed customer expectations**: the customer is Novo Nordisk, and the patient is the '
           'reason the cable is pulled correctly. I also value the way you describe the start here — an onboarding '
           'that is taken seriously, a flat hierarchy and colleagues who answer questions.', after=80)

    m.para('Practically: I live in Måløv, about an hour from Kalundborg, and I will be on site five days a week — in '
           'this discipline the field is where the work is. Danish is my native language and English my professional '
           'one, so I can work in both without switching down. I can start by agreement, and I would welcome a '
           'conversation about which projects the E&I department is staffing over the next year, and where a '
           'commissioning and validation background is most useful to you first. If it is useful, I can also show '
           'how I document a loop from requirement to signed test — that is the part of the job I can demonstrate, '
           'not just describe.', after=70)
    m.meta('Kind regards', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFILE')
    m.para('E&I engineer with 20+ years from electrical and instrumentation work, regulated pharma production and '
           '24/7 technical operations — authorised marine engineer with Danish electrical authorisation (LV/MV/HV) '
           'and a B.Tech in Technology Management & Mechanical Engineering. Two years at Novo Nordisk with 37 parallel '
           'capital projects, loop checks, FAT/SAT and IQ/OQ/PQ and zero critical findings at handover; five years of '
           'hands-on operations with sensors, transmitters, actuators and SCADA at Biofos; three years building '
           'panels, drives and control systems at ELOHVAC.', after=80)

    m.section('INSTRUMENTATION, COMMISSIONING AND VALIDATION')
    for label, body in [
        ('Instrumented design',
         'Instrument index and datasheets, measuring principle and range, materials and process connections, '
         'hazardous-area considerations and safety functions — designed out from the P&ID and checked against the '
         'process before anything is bought.'),
        ('Field verification and commissioning',
         'IO and loop checks against the list, calibration and stroke tests on actuators, functional testing of '
         'interlocks and sequences, SAT and handover — documented while the work happens, not reconstructed later.'),
        ('Validation and qualification',
         'URS and design review, risk assessment and FMEA, IQ/OQ/PQ, traceability matrix, deviation and change '
         'control; audited handover with zero critical findings across 37 GMP projects at Novo Nordisk.'),
        ('Control systems and data',
         'PLC- and SCADA-based systems and BMS/FMS: alarm limits and escalation, trends and condition data, '
         'interface protocols such as Modbus and BACnet; fault finding from sensor to screen.'),
        ('Site supervision and coordination',
         'Construction coordination with contractors and vendors on live plants: scope and interface lists, FAT '
         'before shipment, permits, LOTO and safe work practices, and daily coordination when the work is running.')]:
        m.bullet(label, body, after=25)

    m.models_table('TOOLS AND METHODS', ('Task', 'Tool and documented use'), [
        ('Electrical and instrumentation',
         'P&IDs, single-line diagrams, instrument datasheets and loop drawings, panel and cable schedules, IO lists, '
         'ATEX and hazardous-area requirements; electrical authorisation LV/MV/HV.'),
        ('Functional safety and standards',
         'Safety functions and SIS architecture, SIL targets, interlock testing and documentation to industrial '
         'standards and authority requirements.'),
        ('Testing and qualification',
         'FAT/SAT, IQ/OQ/PQ, calibration and loop checks, acceptance criteria and traceability matrix; deviations '
         'closed with root cause and verified corrective action.'),
        ('Operations and maintenance',
         'Preventive maintenance from condition data, spare-part criticality, calibration routines, LOTO, workplace '
         'assessment and permits in a 24/7 operation.'),
        ('Vendors and construction',
         'Vendor scope and interface lists, FAT and inspection before shipment, supervision and construction '
         'coordination on site with contractors and client representatives.'),
        ('Digital and data',
         'Python, Claude API, SAP and Excel: traceability matrices, IO and deviation logs, alarm statistics and '
         'dashboards — over 40 % of administrative work removed from quoting and follow-up.')])

    m.section('EXPERIENCE')
    jobs = [
        ('Owner / Technical Director',
         'ELOHVAC ApS · Copenhagen, Denmark · May 2023–present',
         '5 electricians and 3 apprentices · full P&L · commercial and industrial customers',
         [('Panels, drives and controls', 'Electrical panels, motor controls, variable speed drives and control '
                                          'systems for heating, ventilation and cooling — specified, installed, '
                                          'tested and handed over with documentation.'),
          ('Customers and people', 'Recruitment, 1:1s and apprentice training alongside budget, quoting and margin; '
                                   'customers informed the same day something changes.'),
          ('Digital operations', 'Python and Claude API for quotations, scheduling, checklists and KPI dashboards; '
                                 'over 40 % productivity gain in the business.')]),
        ('Senior Commissioning Engineer / Project Manager, electrical systems',
         'Novo Nordisk A/S · Kalundborg / Bagsværd, Denmark · Nov 2022–Jul 2024',
         '37 parallel capital projects · 25 specialists · DKK 2–10m each · GMP/FDA/EMA',
         [('Commissioning and qualification', 'Acceptance criteria, FAT/SAT, loop checks and IQ/OQ/PQ with traceable '
                                              'documentation and deviation handling; zero critical findings at '
                                              'handover.'),
          ('Documentation and reporting', 'IO and instrument documentation, panel and cable schedules and as-built '
                                          'records; progress, cost, risk and resources reported monthly to '
                                          'management and client.')]),
        ('Project and Workshop Manager',
         'Ventek-Air · Copenhagen, Denmark · Jan 2022–Nov 2022',
         '14 employees · 11 parallel construction projects · DKK 2–10m each',
         [('Installation and handover', 'Tenders, calculations, subcontractors and handover packages in ventilation '
                                        'and technical installations; daily board meetings and bottleneck analysis.')]),
        ('Maintenance and Operations Manager / Workshop Technician',
         'Biofos, Lynetten · Copenhagen, Denmark · Aug 2017–Jan 2022',
         '24/7 plant · sensors, actuators, pumps, HVAC, high-voltage switchgear, SCADA',
         [('Hands-on operations and fault finding', 'Sensors, transmitters, actuators and switchgear in daily '
                                                    'operation: calibration, troubleshooting, corrective work and '
                                                    'alarm handling from SCADA data in shift teams.'),
          ('Preventive maintenance and safety', 'Plans from condition data, spare-part criticality and LOTO, '
                                                'workplace assessment and permits before every job.')]),
        ('Electromechanical Technician / Production Team Leader',
         'ARJ Engineering · Tehran, Iran · Dec 2003–Mar 2010',
         '12 mechanics and technicians · machine workshop · industrial equipment',
         [('Equipment and team', 'Shift planning and target follow-up; fault diagnosis, root-cause analysis and '
                                 'corrective actions on production equipment.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        m.doc.paragraphs[-1].runs[0].text = 'Scope: '
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('EDUCATION AND AUTHORISATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering',
          'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · EQF 6 · GPA 7.6/12')
    m.edu('Authorised marine and electrical engineer (LV/MV/HV)', 'Danish Safety Technology Authority · May 2023')
    m.edu('Electrical and mechanical design, electrical engineering',
          'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Refrigeration and air conditioning · STCW safety and engine-room watch',
          'Mercantec 2021 · Danish Maritime Authority 2021–2023')

    m.section('LANGUAGES, PRACTICAL AND REFERENCES')
    m.para('Danish: native · English: professional, written and spoken · Persian: native · Driving licence B · Lives in '
           'Måløv, about an hour from Kalundborg, and on site five days a week · Available by agreement · SAP and '
           'Excel in daily use · References from Novo Nordisk and Biofos, and from customers and vendors in my own '
           'company, on request.', after=70)

    m.models_table('WHAT THE ROLE ASKS FOR — MY EVIDENCE', ('Requirement', 'Evidence'), [
        ('Degree in Electrical Engineering, Marine Engineering, Automation or similar',
         'Authorised marine engineer (maskinmester) with a B.Tech in Technology Management & Mechanical Engineering '
         '(EQF 6), electrical engineering studies at Tehran Technical University and Danish electrical '
         'authorisation LV/MV/HV.'),
        ('3+ years in electrical, instrumentation or automation engineering',
         '20+ years: instrument, panel and loop documentation plus FAT/SAT and IQ/OQ/PQ at Novo Nordisk '
         '(2022–2024); panels, drives and control systems at ELOHVAC (2023–); SCADA, sensors and actuators at '
         'Biofos (2017–2022).'),
        ('2+ years of hands-on onsite work',
         'Five years of hands-on operations on a 24/7 plant — calibration, fault finding and corrective work — plus '
         'three years installing and testing systems on customer sites at ELOHVAC.'),
        ('Understanding of process control systems and industrial instrumentation',
         'PLC/SCADA and BMS/FMS platforms, control loops, alarm limits and trends; measuring principles for '
         'pressure, temperature, flow, level and vibration, and actuator and valve behaviour.'),
        ('Industrial standards, sensors, instrumentation and P&IDs',
         'Work to industrial standards and authority requirements in both pharma and utility environments; P&ID, '
         'single-line diagrams, datasheets and loop drawings as daily documents.'),
        ('Commissioning, testing or validation of technical systems',
         'FAT/SAT, loop checks, functional testing, IQ/OQ/PQ and audited handover across 37 capital projects, zero '
         'critical findings; change control and deviations handled under GMP/FDA/EMA.'),
        ('Vendor and client collaboration on validation activities',
         'Worked with vendors and client representatives through design reviews, FAT, site testing and '
         'qualification; FAT before shipment and agreed interface lists as standing practice.'),
        ('Professional level in English and Danish',
         'Danish native and English professional, written and spoken; years of work in English-speaking, '
         'international project organisations, including teams in Bangalore, India.')])
    m.page_break()

    m.models_table('FIRST 90 DAYS — DESIGN, FIELD, DOCUMENTATION', ('Period', 'What happens, and how it is measured'), [
        ('Week 1–2',
         'Read the live project I am placed on: P&IDs, instrument index, IO list, datasheets and the qualification '
         'plan. One day on site with the installers and the client representative. Learn NNE\'s templates and the '
         'project model before adding anything of my own.'),
        ('Day 30',
         'Delivering on my own scope: instruments specified and datasheets approved, loop checks and functional tests '
         'documented in the project system, open points listed with owner and date. One reusable checklist handed to '
         'the team.'),
        ('Day 60',
         'Commissioning and qualification blocks executed and documented for my area, deviations raised and closed '
         'with verified corrective actions, and vendor FATs attended with the interface list signed off.'),
        ('Day 90',
         'I run my area of the discipline independently — design, field verification and qualification — and the '
         'project manager can plan against my dates. At least one template or work instruction improved and shared, '
         'so the next project starts from a better place than mine did.')])

    m.section('THE INSTRUMENT IS A PROMISE')
    m.para('A measurement is only useful if it is right, and it is only right if the whole chain is right: the '
           'tapping point, the impulse line, the transmitter, the wiring, the IO card, the scaling and the loop. Most '
           'commissioning problems are born in the design, and most design problems are born from an assumption '
           'nobody wrote down — the medium is hotter than expected, the line is pressurised differently, the '
           'installation is in a zone nobody classified. My habit is to write the assumption down and check it before '
           'the purchase order goes out.', after=80)

    m.section('SAFETY FUNCTIONS ARE NOT NEGOTIABLE')
    m.para('Where a loop is a safety function, the requirement comes first: what has to happen, how fast, how '
           'reliable, and what proves it afterwards. Then the architecture — the sensor redundancy, the logic, the '
           'final element — and only then the purchase. The same discipline applies to hazardous areas: zone, '
           'equipment category, temperature class and cable entries are not paperwork, they are the reason the plant '
           'does not become the incident. I test interlocks against the written requirement, not against what the '
           'system happens to do.', after=80)

    m.section('COMMISSIONING: THE FIELD DECIDES')
    m.para('A loop is not commissioned when it moves; it is commissioned when it is demonstrated to do the right '
           'thing under the conditions the process actually produces. That means IO checked against the list, '
           'scaling verified with a simulator, the valve stroked and timed, the interlock tested with the real '
           'input, and the result written down at the moment it happened. I have walked out to a panel at the end of '
           'a shift to re-check a wiring list before a signature, and it saved the deviation later. The same discipline '
           'sits in the documentation: every loop has a record that says what was tested, with what, and by whom.', after=80)

    m.section('VALIDATION AND THE AUDIT TRAIL')
    m.para('Qualification is where the E&I engineer proves the design: requirement, risk, test, result, deviation, '
           'closure. A traceability matrix that a colleague who was not in the room can follow is worth more than a '
           'perfect folder nobody reads. In the pharma projects I have worked in, a missing signature stops a batch '
           'release — so documentation is produced with the work, reviewed with the client representative and closed '
           'out before the milestone, not rescued afterwards. That is also where trust with the client is built: the '
           'test is witnessed, the result is agreed on the day, and the record is closed while the memory is fresh.', after=80)

    m.section('VENDORS, SITE AND SUPERVISION')
    m.para('Half of the quality of an instrumented installation is decided before the equipment arrives: a vendor '
           'scope that says what is and is not included, an interface list that both sides have signed, and a FAT '
           'where the thing is actually tested. The other half is decided on site, which is why construction '
           'coordination and supervision belong to the engineer\'s job: right mounting, right orientation, right '
           'cable entries, permits and LOTO in place, and someone who answers when the installer asks a question at '
           '14:30. Keeping the stakeholders — vendor, client representative, contractor and the other disciplines — '
           'in the same picture is half of that job, and it is where a project stays calm.', after=80)

    m.section('SHARING WHAT WORKS')
    m.para('I build my own tools in Python and Claude — traceability matrices that stay in step with the test list, '
           'IO and deviation logs filtered by area and owner, alarm statistics pulled into one page — and I hand them '
           'on rather than keeping them — specifications that already carry the right fields, checks that catch the same '
           'three mistakes, and continuous improvement that shows up in the next project rather than in a slide. At '
           'NNE the same instinct applies across disciplines and countries: what one project learned about a '
           'transmitter or a vendor should not have to be learned again in the next project or in Bangalore. That is '
           'the knowledge sharing your posting asks for, and it is the part of the job I enjoy most.', after=80)

    return m.save(path, title='Application and CV — Electrical & Instrumentation Engineer, NNE',
                  subject='Instrumented design, commissioning and validation in pharma engineering',
                  keywords='E&I engineer, instrumentation, sensors, actuators, P&ID, SIS, ATEX, commissioning, '
                           'validation, IQ OQ PQ, GMP')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_NNE_EI_Engineer.docx')))
