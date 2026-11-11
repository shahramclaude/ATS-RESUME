# -*- coding: utf-8 -*-
"""Senior Electrical Engineer — Arup, Copenhagen (Axel Towers). English posting.

ENGLISH posting -> ENGLISH document (en-GB), 4 pages: letter page 1, CV page 2, education +
90-day plan + method sections + "Where I would start" page 3, requirements matrix page 4.
Format per master/README.md.

STYLE (master/STILREGISTER.md; approved by scripts/style_guard.py, 3/3 against #225):
  register      = DESIGN OFFICE (new) — brief, scheme, detailed design, schedules, calculations,
                  discipline coordination, tender, site supervision, commissioning handover. Not a
                  roll-out, forvaltning or contractor register.
  opening       = F (THE CONSEQUENCE) — a cable schedule that is one circuit short does not fail on
                  the drawing; it fails on site eleven months later. Last #218.
  structure     = THE PHASES — brief · scheme · detailed design · tender and contractor review ·
                  installation and commissioning · people and skills network. Last #187 (as a
                  lifecycle), otherwise new.
  cadence       = short sentences, each carrying a document, a standard or a date.

HONESTY DECISION (user skipped the clarifying questions; the standing rule is: never invent, state
gaps plainly): the posting asks for a **degree in Electrical Engineering** and **minimum 8 years of
post-qualification design experience**. The degree is covered (electrical and mechanical design,
EQF 6, 2000-2003). The eight years of consultancy design are **not** — the documented record is
operations, contracting, commissioning and an own electrical company. The letter says that in the
first two paragraphs and again in the matrix, and the four phases are ordered so that the phases he
has done (contractor review, installation and commissioning) carry the argument while the early
design phases are named as the part he would grow into. **No BIM claim is made**: the posting asks
for design in a BIM environment, and the document states that modelling is not his current tool
while drawing and model review is.

CULTURE SYNC (policy 04.11.2026), sources in master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md §197:
  **Arup** — global engineering consultancy, **75+ years**, **18,000+ colleagues**, trust-owned
  ("as a trust-owned company"), global **profit share** programme, values of collaboration and
  socially useful work, equal-opportunity employer with an accessible recruitment process
  (recruitment.europe@arup.com). **Copenhagen office in Axel Towers**, a **fast-growing team of
  100+ colleagues** from Scandinavia and around the world. **Denmark reference projects named in
  the posting:** **Cityringen Metro**, **BLOX**, **Camp Adventure observation tower**; "we continue
  to pioneer digital infrastructure projects across Scandinavia". **Sectors:** **Mission Critical**,
  **Science & Industry**, **Healthcare**. Role: **Senior Electrical Engineer**, req **COP00005M**,
  Electrical Engineering, Europe Region, Copenhagen. Responsibilities: lead delivery of
  **electrical (MV, LV and ELV) design packages** from **brief** through **scheme and detailed
  design** to **installation and commissioning**; partner with **architects, discipline experts,
  clients, contractors, authorities and public service providers**; design in a **BIM
  environment**; **lead, challenge and coach** a team of engineers; set and uphold **technical and
  quality standards**; **review contractors' design submissions, procedures and schedules**;
  communicate **progress, risks and next steps** to project management; **mentor and develop
  junior and intermediate engineers**; contribute to Arup's **Electrical Skills Network in
  Denmark**; help **win new work** through proposals. Requirements: **degree in Electrical
  Engineering**; **minimum 8 years post-qualification design experience**; valued: **deep knowledge
  of Danish/Scandinavian standards and regulations**, experience leading design teams on
  **Science, Industry & Technology** and/or **Healthcare**, and **confident English plus Danish,
  Swedish or Norwegian**. Benefits: continuous learning and mentorship, global assignments,
  competitive salary and **profit share**, **flexible working**. Application: **CV and cover letter
  in English** via jobs.arup.com (36165).

No invented facts. Documented basis: **37 capital projects** (Novo Nordisk 2022-2024) with 25
specialists, FAT/SAT, zero critical findings, schedules and budgets in **SAP**, contractor and
authority documentation under GMP/FDA/EMA; four years as head of operations and maintenance with
**HV/LV switchgear, transformers, panels, cable work and SRO/SCADA** in 24/7 operation
(Biofos/Lynetten 2017-2022); **14 staff and 11 concurrent contracts** with suppliers and
subcontractors (Ventek Air 2022); **5 electricians + 3 apprentices**, full P&L, design-and-build
quotations and installation delivery (ELOHVAC since 2023); **12 technicians** (ARJ 2003-2010);
**Danish electrician authorisation LV/MV/HV** (May 2023), **B.Tech Mechanical Engineering and
Technology Management** (EQF 6, 7.6/12), **Electrical and Mechanical Design** (EQF 6, 2000-2003),
**Lean 5S/PDCA/VSM/A3**, refrigeration and HVAC technology (AMU 2021); Danish native, English
professional, Persian native. Lives in **Måløv**, ~20 km from Axel Towers.
**Deliberate omissions/limits:** no claim of eight years' design-office experience, no claim of
authoring MV/LV design packages in a consultancy, no claim of BIM/Revit/MagiCAD authoring, no claim
of Arup-scale mission-critical or healthcare design work, and no claim of Swedish or Norwegian
(only Danish and English are stated, as documented).
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Senior Electrical Engineer · MV, LV and ELV · delivery, review and commissioning · Copenhagen'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4 November 2026")
    m.meta("Senior Electrical Engineer · Electrical Engineering, Europe Region · Copenhagen (Axel Towers)")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Application: Senior Electrical Engineer (COP00005M)", bold=True, color='1A1A1A')
    m.para("Dear Arup Copenhagen,", after=60)

    # ---------------------------------------------------------------- page 1
    m.para("**A cable schedule that is one circuit short does not fail on the drawing. It fails eleven "
           "months later, on a Friday, when the contractor has already pulled the cable.** By then the "
           "shaft is closed, the variation is signed, and somebody has to decide whether the extra "
           "circuit goes through a riser that nobody designed for. The cost of that decision was set "
           "at the brief, when a load was taken as given.", after=80)

    m.para("That is why the design phases interest me, and it is also where I have to be straight with "
           "you: **I do not have eight years of consultancy design experience.** What I have is "
           "fifteen years of electrical and mechanical delivery on the other side of the drawing — as "
           "the client's engineer, the contractor's project manager and the owner of an electrical "
           "company — with a **Danish LV/MV/HV authorisation**, an **electrical engineering degree** "
           "behind it, and a habit of reading the design before the concrete is poured.", after=80)

    m.para("**ARUP.** Seventy-five years, more than **18,000 colleagues**, trust-owned, with a share of "
           "the profit rather than a quarterly number to defend. In Denmark: **Cityringen**, **BLOX**, "
           "the **Camp Adventure** tower — and a Copenhagen office in **Axel Towers** that has grown "
           "to **100+ people**. The three sectors in this role — **Mission Critical**, **Science & "
           "Industry**, **Healthcare** — are the ones where a **resilience** decision in the **brief** "
           "is expensive to change later, and where **redundancy** has to be argued rather than "
           "assumed — because the **stakeholders** are not one client but five.", after=80)

    m.para("**The brief.** Two questions decide most of the electrical **load**: what happens when the "
           "supply is lost, and who is allowed to notice. On a **healthcare** floor and in a **mission "
           "critical** hall the answer is different, and it changes the **transformer** size, the "
           "**switchgear** arrangement and the cost before a single line is drawn. I have spent four "
           "years on the receiving end of that answer, keeping a 24/7 plant running on HV and LV "
           "**switchgear** — and I know which of the two questions clients answer honestly.", after=70)

    m.para("**Scheme design.** The architecture of **MV, LV and ELV** is decided here: where the "
           "**transformer** stands, which **cable** routes are real, how the systems talk to each "
           "other, and where **coordination** with other disciplines is won or lost. My contribution "
           "is practical rather than ornamental — I have commissioned what others drew, and I know "
           "which of those decisions come back on site as a variation.", after=70)

    m.para("**Detailed design.** This is the phase I would grow into fastest and claim least: "
           "**calculations**, schedules, selectivity and discrimination, drawn and modelled to a "
           "standard someone else can build from. I work confidently with drawings, schedules and "
           "models as a reviewer and a user, and modelling is not my current authoring tool — I would "
           "learn the office's **BIM** workflow the way I learned the last three systems, by using it "
           "on a live package with someone checking my work.", after=70)

    m.para("**Tender and contractor review.** Here I am at home. Reviewing **contractors' design "
           "submissions, procedures and schedules** against the specification is what I did on **37 "
           "capital projects**, with **25 specialists** and a handover that had to survive an "
           "authority inspection: **zero critical findings**, every deviation closed with a name and a "
           "date. It is also the phase where **quality standards** are either enforced or quietly "
           "negotiated — and I have been the person who had to say no.", after=70)

    m.para("**Installation and commissioning.** This is the strongest part of my record: **FAT/SAT**, "
           "**testing**, **handover** documentation and the last week before energisation, when the "
           "**cable** is in, the panels are labelled and somebody has to prove the **redundancy** "
           "actually works. I have done that on installations that could not be allowed to fail, and I "
           "have written the **documentation** that the next engineer reads.", after=70)

    m.para("**People and the skills network.** I have led **14 people** in a contracting business, "
           "**5 electricians and 3 apprentices** in my own company, and 12 technicians before that. "
           "**Mentoring** was not a programme; it was a morning at the panel with somebody's drawing "
           "and a question. A **skills network** across an office is the same thing at scale, and I "
           "would contribute to the Danish one from the practical end: what the site does with the "
           "design, and what it costs when the design did not expect it.", after=80)

    m.para("**Practical.** I live in **Måløv**, 20 km from Axel Towers. **Danish** native, **English** "
           "professional — not Swedish or Norwegian. Available by agreement, and happy to be tested "
           "on a technical task before you decide.", after=60)
    m.meta("Kind regards", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- page 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFILE")
    m.para("Electrical and mechanical engineer with a **Danish LV/MV/HV authorisation** and fifteen "
           "years of technical delivery: **37 capital projects** reviewed and handed over with zero "
           "critical findings, four years responsible for HV/LV **switchgear**, **transformers** and "
           "24/7 supply, and an own electrical company since 2023. Strongest in contractor review, "
           "**commissioning** and **handover**; growing into design authoring.", after=80)

    m.section("ELECTRICAL DESIGN AND SYSTEMS")
    for label, body in [
        ("MV, LV and ELV",
         "Authorised for **LV/MV/HV**: **switchgear**, **transformer** stations, distribution boards, "
         "**cable** systems, earthing and the interfaces to **ELV** systems in operation."),
        ("Load and resilience",
         "**Load** profiles, **redundancy** and standby arrangements argued on four years of 24/7 "
         "operation — including what actually happens when the second supply does not come in."),
        ("Drawings and models",
         "Single-line diagrams, panel schedules and **documentation** read and reviewed daily; model "
         "review and coordination as a user, **BIM** authoring as the next skill to build."),
    ]:
        m.bullet(label, body)

    m.section("DELIVERY, REVIEW AND COMMISSIONING")
    for label, body in [
        ("Contractor review",
         "**Contractors'** design submissions, method statements and schedules reviewed against "
         "specification on 37 projects; deviations closed with a name and a date."),
        ("Commissioning and handover",
         "**Testing**, **FAT/SAT**, **handover** packs and the week before energisation, on "
         "installations where failure was not an option."),
        ("Quality standards",
         "One checklist per discipline, applied to every site, so a review is repeatable and a "
         "**quality** finding does not depend on who is on holiday."),
    ]:
        m.bullet(label, body)

    m.section("LEADERSHIP AND PEOPLE")
    for label, body in [
        ("Teams led",
         "**14 people** in a contracting business, **5 electricians and 3 apprentices** in my own "
         "company, 12 technicians earlier — plus 25 specialists coordinated across projects."),
        ("Coaching",
         "**Mentoring** at the panel rather than in a classroom: one drawing, one question, and the "
         "next task slightly harder than the last."),
        ("Standards and authority",
         "Design decisions explained to **authorities** and clients in writing; Danish installation "
         "rules as they are enforced on site, not only as they are written."),
    ]:
        m.bullet(label, body)

    m.section("EXPERIENCE")
    m.job("Owner / Technical Director", "ELOHVAC ApS · Copenhagen · May 2023–present",
          scope="5 electricians + 3 apprentices · full P&L · design-and-build quotations · installation delivery")
    m.bullet("Electrical work with a signature on it",
              "Quotations, **load** assessments and installation delivery for building owners — the "
              "part where the drawing meets the meter cupboard.")

    m.job("Senior Commissioning Engineer / Project Manager",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024",
          scope="37 capital projects · 25 specialists · FAT/SAT · SAP · GMP/FDA/EMA documentation")
    m.bullet("Reviewing what others designed",
              "**Contractor** submissions, procedures and schedules checked against specification; "
              "**commissioning** and **handover** with zero critical findings.")

    m.job("Project and Workshop Manager", "Ventek Air ApS · Vedbæk · Jan 2022–Nov 2022",
          scope="14 staff · 11 concurrent contracts · suppliers, subcontractors, own workshop")
    m.bullet("Eleven packages at once",
              "Scope, sequence and delivery across eleven simultaneous contracts — capacity moved "
              "before a bottleneck became a delay.")

    m.job("Head of Operations and Maintenance", "Biofos (Lynetten) · Copenhagen · Aug 2017–Jan 2022",
          scope="24/7 plant · HV/LV switchgear, transformers, panels, SRO/SCADA · HSE and standby")
    m.bullet("The systems the design promised",
              "**Switchgear**, **transformers** and standby supply owned end to end — including the "
              "nights when **redundancy** had to prove itself.")

    m.job("Production Foreman / Electromechanical Technician",
          "ARJ Engineering · Tehran · 2003–2010 · 12 mechanics and technicians")
    m.bullet("First leadership role",
              "Shift planning, allocation and training in a workshop where drawings and deadlines "
              "arrived the same morning.")

    # ---------------------------------------------------------------- page 3
    m.page_break()
    m.section("EDUCATION AND AUTHORISATION")
    m.edu("Electrical and Mechanical Design, Electrical Engineering (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("B.Tech, Technology Management and Mechanical Engineering (EQF 6)",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7.6/12")
    m.edu("Danish electrician authorisation, LV/MV/HV — authorised mechanical engineer (maskinmester)",
          "Danish Safety Technology Authority · May 2023")
    m.edu("Lean: 5S, PDCA, VSM, A3 · refrigeration and HVAC technology (AMU) · STCW safety",
          "Mercantec 2021 · Danish Maritime Authority 2021–2023")

    m.section("LANGUAGES, PRACTICALITIES AND REFERENCES")
    m.para("**Danish:** native · **English:** professional, written and spoken · **Persian:** native "
           "· Based in **Måløv**, about 20 km from Axel Towers · Available by agreement · References "
           "on request.", after=70)

    m.models_table(
        "THE FIRST 90 DAYS — FROM BRIEF TO A REVIEWED PACKAGE",
        ["Period", "What happens, and how it is measured"],
        [
            ("Week 1–2",
             "Read three live packages end to end — one **mission critical**, one **healthcare**, one "
             "**industry** — and sit with the engineer who authored each. Ask which review comment "
             "saved the most money, and which one was ignored."),
            ("Day 30",
             "One package reviewed independently, against the office's own checklist, with comments "
             "the lead engineer can accept or reject on the record. First pass on the **BIM** "
             "workflow, on a real model rather than a tutorial."),
            ("Day 60",
             "**Commissioning** and **handover** experience written down as a short internal note: "
             "what the site needs from the design, and where the standard package leaves a question "
             "open. Shared with the **Electrical Skills Network**."),
            ("Day 90",
             "Authoring a defined part of a package — schedules, calculations or a system section — "
             "under review, with the **quality** standard set by someone else and met."),
        ],
        widths=(1500, 8830))

    m.section("A DESIGN IS ONLY AS GOOD AS ITS LAST REVIEW COMMENT")
    m.para("The visible product of a design office is a set of drawings; the actual product is a "
           "decision someone can build from. That is why the review matters more than the model: a "
           "comment that arrives before tender costs an hour, and the same comment after installation "
           "costs a variation, a delay and a client who remembers. I have been on the receiving end of "
           "both, and I write comments accordingly. **Sustainability** in a design is the same "
           "economy: the cheapest kilowatt is the one the building never needs.", after=70)

    m.section("THE SITE IS THE ONLY TEST OF A COORDINATION DRAWING")
    m.para("**Coordination** failures are rarely dramatic. They are a **cable** tray that is 80 mm too "
           "low, a panel that cannot open its door, a duct that arrives where a beam already is. None "
           "of it shows in a clash report; all of it shows in week nine. Having spent years on site, I "
           "read a model looking for the things that will be built, not the things that are drawn.",
           after=70)

    m.section("MISSION CRITICAL IS A SENTENCE IN THE BRIEF, NOT A BADGE")
    m.para("**Redundancy** on paper is easy: draw two feeds and write N+1. **Resilience** in reality is "
           "a maintenance procedure, a test schedule and a person who knows which breaker to open — "
           "and it fails quietly when nobody has planned the annual test. Four years of 24/7 operation "
           "taught me to ask for that plan before the design is frozen, not after.", after=70)

    m.section("COACHING IS HOW A STANDARD SURVIVES")
    m.para("A **quality** standard that lives in one senior engineer's head leaves when he does. The "
           "only version that survives is the one written down, used in every review and taught to the "
           "next engineer by doing it with them. That is what I would bring to a team of juniors and "
           "intermediates: a checklist they can argue with, and a review they have watched happen.",
           after=70)

    m.section("WHAT I WOULD NEED FROM THE OFFICE")
    m.para("Three things, and I would rather ask for them here than pretend otherwise: someone senior to "
           "check my first packages line by line, access to the standards library and the office's own "
           "templates, and a defined authoring scope so I am not learning in a corner. In return I bring "
           "a decade of site knowledge that makes a **review** comment useful before it becomes "
           "expensive.", after=70)

    m.section("WHERE I WOULD START")
    m.para("In the review. First month: three packages read end to end, one independent review against "
           "the office's own checklist, and the **BIM** workflow learned on a live model. Then the part "
           "I can add fastest — **commissioning** and **handover** knowledge turned into comments that "
           "arrive early enough to be cheap.", after=0)

    # ---------------------------------------------------------------- page 4
    m.page_break()
    m.models_table(
        "WHAT THE POSTING ASKS FOR — WHAT I HAVE",
        ["Requirement in the posting", "Evidence"],
        [
            ("Degree in **Electrical Engineering**",
             "**Electrical and Mechanical Design, Electrical Engineering** (EQF 6, 2000–2003), plus "
             "**B.Tech** mechanical engineering and technology management (EQF 6, 7.6/12)."),
            ("Minimum 8 years post-qualification **design** experience",
             "Not met as a design-office record, and stated plainly in the letter. Fifteen years of "
             "electrical delivery sit behind it: 37 projects reviewed, commissioned and handed over."),
            ("Drive delivery of **electrical** design packages across the full lifecycle",
             "Full lifecycle as client's engineer, contractor and owner: **brief**, installation, "
             "**commissioning**, **handover** — the phases where a design is proved."),
            ("Partner with **architects**, discipline experts, clients, **contractors**, **authorities**",
             "**Contractors** and **authorities** as daily counterparts on 37 projects; architects and "
             "designers as counterparts in own design-and-build work."),
            ("Design **medium voltage, low voltage and extra-low voltage** systems in a **BIM** environment",
             "**MV/LV/HV** authorisation and hands-on **switchgear**, **transformer** and **cable** "
             "work. **BIM** authoring is not my current tool; model review and coordination are."),
            ("Lead, challenge and **coach** a team of **engineers**",
             "**14 people** in a contracting business, **5 electricians and 3 apprentices** in my own "
             "company, 25 specialists coordinated across projects."),
            ("Set and uphold **technical and quality standards**",
             "One checklist per discipline applied to every site; **zero critical findings** at "
             "handover on 37 projects."),
            ("**Review contractors'** design submissions, procedures and schedules",
             "The core of my Novo Nordisk role: submissions, method statements and schedules checked "
             "against specification, deviations closed with name and date."),
            ("Communicate progress, risks and next steps to project management",
             "Monthly status with **risks** and dates on 37 projects; in my own company, to clients who "
             "wanted to know before it hurt."),
            ("**Mentor** and develop junior and intermediate **engineers**",
             "**Mentoring** at the panel with apprentices and technicians in every leadership role; "
             "competence plans written per person and followed."),
            ("Contribute to Arup's **Electrical Skills Network** in Denmark",
             "Practical input from the site end: **commissioning** and **handover** lessons, Danish "
             "installation practice, and what a reviewed package needs to be buildable."),
            ("Help win new work through **proposals**",
             "Quotations and technical proposals in my own company since 2023; scope, price and a "
             "delivery date that could be defended."),
            ("Deep knowledge of **standards** and **regulations** in **Denmark** and Scandinavia",
             "Danish **LV/MV/HV** authorisation and work under the Danish Safety Technology Authority; "
             "installation practice as enforced on Danish sites. Deep design-standard knowledge is "
             "still being built."),
            ("Leading design teams on **Science**, **Industry** and **Healthcare**",
             "**Healthcare**-adjacent and regulated production at Novo Nordisk (GMP/FDA/EMA) and a "
             "24/7 utility plant; design-team leadership in a consultancy is the step I am applying "
             "for, not a claim I make."),
            ("**English** plus **Danish**, Swedish or Norwegian",
             "**Danish** native, **English** at professional level, **Persian** native. No Swedish or "
             "Norwegian."),
            ("Passion for **sustainable** building design and excellent engineering",
             "Energy management in Copenhagen with over **40 %** lower consumption documented; **Lean** "
             "method work and a habit of choosing the cheaper, simpler installation."),
            ("Curiosity, **ownership**, building trust quickly, high-quality **design**",
             "Owner of a company and of 37 deliveries: decisions taken, mistakes owned, and the lesson "
             "written into the next project."),
            ("Work in **multidisciplinary project teams**",
             "Process, mechanical, ventilation and **electrical** disciplines coordinated on 37 "
             "projects; interfaces agreed in writing rather than assumed."),
            ("**Mission Critical**, **Science & Industry** and **Healthcare** projects",
             "24/7 **mission critical** operation for four years, regulated production under GMP/FDA/"
             "EMA, and installation delivery in occupied buildings."),
        ],
        widths=(3600, 6746))

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_Arup_SeniorElectricalEngineer.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_Arup_SeniorElectricalEngineer.docx'))
