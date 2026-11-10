# -*- coding: utf-8 -*-
"""Resident Engineer — hyperscale data centre campus, Fredericia (Danish site, English posting).

English posting -> English document (en-GB), 4 pages: letter p1, CV p2, education + 90-day plan +
method sections p3, 18-row requirement matrix p4. Format per master/README.md: brev -> CV ->
uddannelse/90 dage -> matrix. Rekrutterens/opslagets anvisninger om ansøgningsform følges ikke.

STILVALG (master/STILREGISTER.md; godkendt af scripts/style_guard.py, 3/3 skift mod #208):
  register      = INGENIØR-PRÆCIS — kriterier, accept, dokumentation, tolerancer, grænseflader.
                  Rollen ER en acceptfunktion: ITP'er, NCR'er, punch list, handover pack.
  åbningsgreb   = F (KONSEKVENSEN) — "A punch list is not a list of defects. It is a list of
                  decisions that were postponed." Sidst #201.
  struktur      = MÅLESTOKKEN — hver sektion åbner med et tal og hvad det betyder (5 niveauer ·
                  0 åbne NCR'er · 1 tegning · 14 fag · 37 projekter · 24 timer). Sidst #199.
  kadence       = korte, præcise sætninger; definitioner og acceptkriterier frem for tillægsord.

KULTURSYNKRONISERING (policy 04.11.2026): opslagets eget sprog bærer teksten — *client's
technical representative*, *hyperscale*, *MEP*, *walkdowns*, *approved methods*, *QA/QC*,
*inspection and test plans*, *non-conformances*, *punch-list*, *RFIs*, *submittals*, *material
approvals*, *shop drawings*, *coordination models*, *constructability*, *Levels 1-5
commissioning*, *factory and site acceptance tests*, *integrated systems testing*, *O&M manuals*,
*handover packages*, *programme*, *flag risks early*. Kunden er ikke navngivet i opslaget og
nævnes ikke i dokumentet.

Ingen opdigtede fakta. Dokumenteret grundlag: elautoriseret maskinmester LV/MV/HV, 37 CAPEX-
projekter med FAT/SAT og nul kritiske fund, 11 entrepriser/14 mand, 25 specialister, 24/7-drift
med HVAC/pumper/HV/SCADA, SAP, fuldt P&L siden 2023.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Resident Engineer · MEP, QA/QC and commissioning on site'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Copenhagen area'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4 November 2026")
    m.meta("Resident Engineer · Hyperscale data centre campus · Fredericia, Denmark")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Application: Resident Engineer", bold=True, color='1A1A1A')
    m.para("Dear Project Manager,", after=60)

    # ---------------------------------------------------------------- page 1
    m.para("**A punch list is not a list of defects. It is a list of decisions that were postponed.** "
           "Every item on it was once a question that could have been answered in a week: an RFI "
           "nobody closed, a hold point nobody witnessed, a clearance nobody measured. By the time it "
           "reaches the list, it is a trade standing still, a test that cannot start, and a "
           "**handover** date somebody has to move. On a **hyperscale** campus that postponement "
           "happens in a thousand places at once — which is why the **resident engineer**'s real job "
           "is not to find defects at the end, but to force the decision while it is still cheap.",
           after=80)

    m.para("**5 levels.** **Commissioning** runs from Level 1 to Level 5, and every level asks a "
           "different question: does it pass the **factory acceptance test**, does it start on site, does it function, "
           "does the whole system stay up when one part fails, and does the building still perform "
           "in operation. My part is the same at each level — read the script before the witness, "
           "check the evidence against the acceptance criterion, and do not sign until the number in "
           "front of you is the number in the test. I have written **factory acceptance** and **site "
           "acceptance** protocols before the test was run on 37 projects, with **zero critical "
           "findings** at handover.", after=80)

    m.para("**0 open non-conformances.** A **non-conformance** closed because the contractor pushed "
           "is not closed; it is rescheduled. So every **ITP** on my sites has named hold points, "
           "every hold point has a witness, and every **NCR** is closed on root cause with a date and "
           "a name attached. The **punch-list** gets the same treatment: an item is closed when "
           "someone has seen it working, not when someone has promised it will be.", after=80)

    m.para("**1 drawing at a time.** **RFIs**, **submittals**, **material approvals**, **shop "
           "drawings** and **coordination models** are reviewed against the specification and against "
           "the space that actually exists: can it be installed, can it be maintained, and does it "
           "collide with the next trade. An answer that arrives after the installation window is not "
           "an answer; it is a **design change** with a price. I keep the response inside the "
           "**programme**, and I say no in writing rather than late.", after=80)

    m.para("**14 trades.** Supervision on a campus is not standing behind one crew. It is a daily "
           "**walkdown** of the areas where the sequence is about to break: **power distribution**, "
           "**generators**, **UPS**, **switchgear**, **chillers** and **cooling systems**, **building "
           "management** controls and everything that has to be finished before the next trade can "
           "start. I ran 11 concurrent contracts with 14 people; the method is the same at any scale "
           "— one owner, one date, and a written record of what was agreed on the floor.", after=80)

    m.para("**37 projects on programme.** Progress is tracked against the **programme**, not against "
           "the impression of the site: what was planned this week, what was installed, and what that "
           "does to the next three. Risks are **flagged early** — the delivery that will not arrive, "
           "the access that will not be granted, the witness who cannot come — and reported with a "
           "date and an owner, not as a concern. Budget and **forecast** in SAP on 37 projects; full "
           "P&L in my own company since 2023.", after=80)

    m.para("**24 hours.** The report goes out the day it happened. Daily progress, weekly look-ahead, "
           "and any risk that changes the date in the same 24 hours it is found. Bad news delivered "
           "with a plan costs a conversation; bad news delivered late costs a fortnight.", after=80)

    m.para("**The MEP side is my own trade.** Authorised marine and mechanical engineer at LV/MV/HV "
           "level, electrical and mechanical design (EQF 6), B.Tech in technology management — plus "
           "ventilation, HVAC and refrigeration delivered as contracts, and four years responsible "
           "for a plant in 24/7 operation with pumps, HV switchgear and SCADA. **Generators**, "
           "**UPS**, **switchgear**, **chillers** and controls are systems I have installed, tested "
           "and handed over, not systems I have only read about.", after=80)

    m.para("**Practicalities.** Based in Måløv; Fredericia is about two hours by car and I will be "
           "resident on site through the working week for as long as the build needs it. Driving "
           "licence B. Danish native and professional English — on a Danish campus run in English "
           "with Danish subcontractors, both matter. Available at short notice.", after=60)
    m.meta("Kind regards", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- page 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFILE")
    m.para("Site-based engineer with twenty years in **MEP** and **critical infrastructure**: "
           "authorised marine and mechanical engineer at LV/MV/HV level, electrical and mechanical "
           "design (EQF 6), B.Tech in technology management. 37 CAPEX projects with **FAT/SAT**, IQ/OQ/PQ "
           "and **zero critical findings** at handover; 11 contracts with a team of 14; four years of "
           "24/7 plant operation; full P&L since 2023.", after=80)

    m.section("SITE SUPERVISION AND QUALITY")
    for label, body in [
        ("Inspections and walkdowns",
         "Daily **walkdowns** against **drawings**, **specifications** and approved methods; issues "
         "recorded the day they are seen, with an owner and a date."),
        ("QA/QC and ITPs",
         "**Inspection and test plans** with named hold points and witnesses; **QA/QC** enforced on "
         "the floor, not audited after the fact."),
        ("Non-conformances and punch-list",
         "**NCRs** closed on root cause, **punch-list** items closed only when seen working; the "
         "close-out file that stands up when the client asks."),
    ]:
        m.bullet(label, body)

    m.section("TECHNICAL MANAGEMENT")
    for label, body in [
        ("RFIs and submittals",
         "**RFIs**, **submittals**, **material approvals** and technical queries answered inside the "
         "**programme**; answers in writing so nobody re-argues them later."),
        ("Shop drawings and models",
         "**Shop drawings** and **coordination models** reviewed for **constructability**, clearances "
         "and compliance with the specification before the trade mobilises."),
        ("Design changes and interfaces",
         "**Design changes** and site instructions priced and recorded; design, construction and "
         "commissioning held to the same interface list."),
    ]:
        m.bullet(label, body)

    m.section("COMMISSIONING AND HANDOVER")
    for label, body in [
        ("Levels and witnesses",
         "**Commissioning** witnessed level by level, from **factory acceptance** through **site "
         "acceptance** to **integrated systems testing**; no signature without the criterion met."),
        ("Test records and O&M",
         "**O&M manuals**, test results and commissioning documentation reviewed for completeness and "
         "accuracy — not accepted because they arrived."),
        ("Handover packages",
         "**Handover packages** complete: as-builts, test records, punch list closed, training done, "
         "warranty clear — zero critical findings at acceptance."),
    ]:
        m.bullet(label, body)

    m.section("EXPERIENCE")
    m.job("Owner / Technical Director", "ELOHVAC ApS · Copenhagen · May 2023–present",
          scope="5 electricians + 3 apprentices · full P&L · installation, testing and handover")
    m.bullet("Site delivery and commercial risk",
              "Projects from quotation to handover with own budget and own risk; subcontractors, "
              "material control and QA — and the decision to decline work that cannot be delivered.")

    m.job("Senior Commissioning Engineer / Project Manager",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024",
          scope="Electrical systems · 37 concurrent CAPEX projects · 25 specialists · GMP/FDA/EMA")
    m.bullet("Witnessing and acceptance",
              "**FAT/SAT** and IQ/OQ/PQ with protocols written before the test; milestones and reporting in "
              "SAP ERP — **zero critical findings** at handover.")

    m.job("Project and Workshop Manager", "Ventek-Air · Copenhagen · Jan 2022–Nov 2022",
          scope="14 employees · 11 concurrent contracts · DKK 2–10 m each · ventilation and cooling")
    m.bullet("Parallel delivery under pressure",
              "Crews and suppliers moved between contracts when one ran behind; the customer informed "
              "the same day, with a plan rather than an apology.")

    m.job("Maintenance and Operations Manager", "Biofos (Lynetten) · Copenhagen · Aug 2017–Jan 2022",
          scope="Treatment plant in 24/7 operation · pumps, HVAC, HV switchgear, SCADA")
    m.bullet("Live plant, planned outages",
              "Preventive maintenance and fault-finding around the clock; outages planned into narrow "
              "windows with the fallback designed before it was needed. LOTO and APV.")

    m.job("Electromechanical Technician / Production Team Leader",
          "ARJ Engineering · Tehran · Dec 2003–Mar 2010 · 12 mechanics and technicians")

    # ---------------------------------------------------------------- page 3
    m.page_break()
    m.section("EDUCATION AND AUTHORISATION")
    m.edu("Authorised Marine and Mechanical Engineer — Danish electrical authorisation LV/MV/HV",
          "Danish Safety Technology Authority · May 2023")
    m.edu("B.Tech, Technology Management and Mechanical Engineering (EQF 6)",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7.6/12")
    m.edu("Electrical and Mechanical Design, Electrical Engineering (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("Refrigeration and HVAC (AMU) · Lean: 5S, PDCA, VSM, A3",
          "Mercantec · 2021 · STCW safety certificates (2021–2023)")

    m.section("LANGUAGES, PRACTICALITIES AND REFERENCES")
    m.para("**English:** professional, written and spoken · **Danish:** native · **Persian:** native "
           "· **Based in Måløv**, Fredericia about two hours by car — resident on site through the "
           "working week · **Driving licence B** · **Available at short notice** · References on "
           "request.", after=70)

    m.models_table(
        "FIRST 90 DAYS — FROM THE FIRST WALK TO A HANDOVER PACK THAT STANDS UP",
        ["Period", "What happens, and how it is measured"],
        [
            ("Week 1–2",
             "Read the specification, the approved methods and the live **ITPs** for my areas; walk "
             "every area with the **general contractor** and the **subcontractors**, and open a risk "
             "list with an owner per line."),
            ("Day 30",
             "Every area has a current status against the **programme**; open **RFIs** and "
             "**submittals** reviewed for age, not just for content, and the oldest ones closed first."),
            ("Day 60",
             "Hold points and witnesses agreed for the next commissioning window; **punch-list** from "
             "the first systems closed to zero, with the evidence in the file."),
            ("Day 90",
             "First system handed over complete: test records, **O&M manuals**, as-builts and training "
             "signed off — and a reporting rhythm the Project Manager can use without asking."),
        ],
        widths=(1500, 8830))

    m.section("THE WITNESS IS THE POINT")
    m.para("A hold point that gets signed without a witness is worse than a hold point that is late, "
           "because it hides a question instead of asking it. So I arrive at the test knowing the "
           "criterion, I check the instrument calibration before I check the reading, and I write the "
           "result down while the system is still running. If the number is wrong, the answer is no — "
           "and the conversation about what it costs happens before the next pour, not after it.",
           after=70)

    m.section("AN RFI ANSWERED LATE IS A CHANGE ORDER")
    m.para("Every question on site has a date after which answering it costs money. That date is not "
           "in the RFI system; it is in the installation sequence. So the register is reviewed by age "
           "and by what it blocks, not by who shouted loudest, and the ones that stop a trade this "
           "week get answered this week. A resident engineer who only responds is a mailbox with a "
           "hard hat.", after=70)

    m.section("A CLOSED ITEM FOR THE WRONG REASON COMES BACK")
    m.para("Punch items get closed for three reasons: it is fixed, someone promised it will be fixed, "
           "or everyone is tired. Only the first one survives commissioning. I close on evidence — a "
           "photograph, a test, a measurement, a signature — because the item that comes back during "
           "integrated testing comes back at the worst possible moment, in front of the client, with "
           "the programme already tight.", after=70)

    m.section("A PERMIT TO WORK IS A SCHEDULE, NOT PAPER")
    m.para("On a campus, construction and energisation overlap for months, and that overlap is where "
           "the serious accidents live. Switching, isolation and LOTO are therefore planned with the "
           "same rigour as the installation: who holds the key, who signs the permit, which live "
           "boards are out of bounds, and what happens if the temporary supply is needed at 03.00. As "
           "an electrician and an authorised engineer at LV/MV/HV level I have worked on both sides of "
           "that permit — the one that issues it and the one that has to trust it.", after=70)

    m.section("MEP IS WHERE THE PROGRAMME IS ACTUALLY WON")
    m.para("On a data hall the structure can be ahead and the project still late, because power, "
           "cooling and controls have to be commissioned in an order that does not forgive a missing "
           "cable or an unlabelled valve. That is why the MEP sequence is planned backwards from the "
           "commissioning dates, and why the trades are walked every day rather than audited every "
           "month.", after=70)

    # ---------------------------------------------------------------- page 4
    m.page_break()
    m.models_table(
        "WHAT THE ROLE REQUIRES — WHAT I HAVE DELIVERED",
        ["Requirement in the posting", "Evidence"],
        [
            ("Be the client's technical representative on site, reporting to the Project Manager",
             "Client-side and contractor-side on the same projects: one voice for the customer on "
             "site, with decisions recorded and bad news delivered with a plan."),
            ("Oversee MEP installation: power distribution, generators, UPS, switchgear, chillers, cooling systems and building management controls",
             "**Power distribution**, **switchgear**, **UPS** and emergency power installed and "
             "tested; **chillers**, **cooling systems** and HVAC delivered as contracts; BMS and "
             "SCADA in daily use."),
            ("Carry out regular site inspections and walkdowns",
             "Daily **walkdowns** on 11 concurrent contracts; findings recorded the day they were "
             "seen, with an owner and a date."),
            ("Review work against drawings, specifications and approved methods",
             "**Drawings** and **specifications** read against the floor as built; as-builts marked "
             "up and issued, not kept in a notebook."),
            ("Review and enforce QA/QC procedures",
             "**QA/QC** enforced on site through **ITPs** and hold points; GMP/FDA documentation and "
             "KS on regulated sites."),
            ("Witness inspection and test plans (ITPs)",
             "**ITP** hold points witnessed with the criterion in hand; calibration checked before "
             "the reading was accepted."),
            ("Close out non-conformances and punch-list items",
             "**NCRs** closed on root cause; **punch-list** closed on evidence — zero critical "
             "findings at handover on 37 projects."),
            ("Review and respond to RFIs, submittals, material approvals and technical queries in line with the programme",
             "**RFIs** and **submittals** answered against the installation sequence; **material "
             "approvals** checked for compliance before the delivery, not after."),
            ("Manage design changes and site instructions",
             "**Design changes** priced, recorded and dated; variations approved in the week they "
             "arose, with full P&L responsibility in my own company."),
            ("Coordinate between design, construction and commissioning teams",
             "**Design team**, construction and commissioning held to one interface list — 25 "
             "specialists across engineering, procurement and site."),
            ("Review contractor shop drawings and coordination models for constructability and compliance",
             "**Shop drawings** and **coordination models** reviewed for **constructability**, "
             "clearances and maintenance access before the trade mobilised."),
            ("Support Levels 1-5 commissioning, witnessing factory and site acceptance tests and integrated systems testing",
             "**FAT/SAT** witnessed and written before the test; functional and **integrated systems "
             "testing** on critical power and cooling, with IQ/OQ/PQ documentation."),
            ("Review commissioning documentation, test results and O&M manuals",
             "**O&M manuals** and test records reviewed line by line; incomplete packages returned "
             "rather than accepted."),
            ("Ensure complete, accurate handover packages",
             "**Handover packages** with as-builts, test records, punch list closed and training done "
             "— the file the operator actually uses on day one."),
            ("Track installation progress against the programme and flag risks early",
             "Progress tracked weekly against the **programme** with a look-ahead; **risks** flagged "
             "with a date and an owner in the same 24 hours they appeared."),
            ("Work daily with the general contractor, specialist subcontractors, design teams and the commissioning team",
             "**General contractor** and **subcontractors** steered from the floor; 14-person "
             "contract team and 11 contracts run in parallel."),
            ("Work hands-on at the centre of the build, from early works through to handover",
             "On site, not in a site office: installation, testing and handover done with the crews, "
             "in my own company since 2023."),
            ("Deliver a hyperscale data centre campus on site in Fredericia, Denmark",
             "Critical infrastructure rather than hyperscale by name: 24/7 plant, GMP-regulated build "
             "and mission-critical power and cooling — the same consequence of downtime, at a "
             "different scale. Danish native, professional English."),
        ],
        widths=(3600, 6746))

    m.section("WHERE I WOULD START")
    m.para("With the areas closest to energisation. First week: the specification and approved methods "
           "for those areas, the open RFI and NCR registers sorted by age, and a walk with the "
           "contractor's site manager to see which of the two lists is telling the truth. Then the "
           "risk list, written the way I would want to receive it — one line, one owner, one date.",
           after=0)

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_ResidentEngineer_Fredericia.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_ResidentEngineer_Fredericia.docx'))
