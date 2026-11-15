# -*- coding: utf-8 -*-
"""Project Quality and Risk Engineer — NOV Subsea Production Systems, Brøndby (English posting).

English posting -> English document (en-GB), 4 pages: letter p1, CV p2, education + 90-day plan +
method sections p3 (closed by "Where I would start"), 23-row requirement matrix p4. Format per master/README.md: brev -> CV ->
uddannelse/90 dage -> matrix. Rekrutterens/opslagets anvisninger om ansøgningsform følges ikke.

STILVALG (master/STILREGISTER.md; godkendt af scripts/style_guard.py, 3/3 skift mod #209):
  register      = MARITIM/OFFSHORE — regime, vinduer, rækkefølge, "det kan ikke åbnes igen".
                  En subsea-enhed kan ikke serviceres efter udlægning; kvaliteten afgøres i land.
  åbningsgreb   = A (PLACERINGEN) — "inspected twice: once in Brøndby and Kalundborg, and once at
                  300 metres, where nobody can open it again." Sidst #200.
  struktur      = PROBLEMKATALOG — fire navngivne problemer i rollen, hver med pris, metode og bevis.
                  Sidst #201.
  kadence       = længere, forklarende sætninger i brevet; hug i CV'et og matricen.

KULTURSYNKRONISERING (policy 04.11.2026), kilder i master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md §181:
  NOVs mission "we power the industry that powers the world"; SPS-brandet "safe, high-quality,
  technology-driven"; hovedkontor Brøndby og fabrik i Kalundborg (~100 km); NOV Flexibles er en af
  verdens kun tre producenter af fleksible rør — "engineer-driven manufacturing", made to order.
  Derfor: Brøndby/Kalundborg som stedet, hvor fejlen stadig kan ændres; last-out som vinduet;
  API Q1/ISO 29001 som ramme for leverandørkvalitet; API RP 17N (reliability and technical risk)
  som fagligt nabospor. Ingen påstand om at have arbejdet i subsea eller offshore.

Ingen opdigtede fakta. Dokumenteret grundlag: 37 CAPEX-projekter med FAT/SAT og IQ/OQ/PQ, nul
kritiske fund under GMP/FDA/EMA, afvigelser/CAPA/ændringsstyring, KS-dokumentation og SAP, APV og
LOTO, risikovurdering ved pladsopstart, Maskindirektivet med CE og teknisk dokumentation,
11 entrepriser/14 mand, fuldt P&L siden 2023, 24/7-drift med PDCA og 40 % lavere energiforbrug.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Project Quality and Risk Engineer · quality systems, risk and audit'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Copenhagen area'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4 November 2026")
    m.meta("Project Quality and Risk Engineer · Subsea Production Systems · Brøndby, Denmark")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Application: Project Quality and Risk Engineer", bold=True, color='1A1A1A')
    m.para("Dear Hiring Manager,", after=60)

    # ---------------------------------------------------------------- page 1
    m.para("**A subsea system is inspected twice: once in Brøndby and Kalundborg, and once at 300 "
           "metres, where nobody can open it again.** That single fact is the whole argument for "
           "this role. A flexible pipe or a manifold can still be changed while it stands on the "
           "quay; after load-out, every open question becomes a retrieval campaign, a deferred "
           "production day or a claim — and every **offshore** requirement is a promise about a "
           "unit that will be tested by salt water for twenty years. Quality and risk are therefore not "
           "functions that report on what has already happened. They are the last place where a "
           "decision is still cheap, and the discipline of the job is to force that decision before "
           "the unit leaves the yard.", after=80)

    m.para("**One: the requirement that was accepted before anyone could manufacture it.** Most of "
           "the cost of a subsea contract is decided in the tender and the contract review, long "
           "before a drawing exists. So a requirement set is marked line by line — we can do this, "
           "we can do this with a clarification, we cannot do this — and the deviation is written "
           "into the tender instead of being discovered in production fourteen months later. I have "
           "priced, signed and carried the risk of my own contracts since 2023, including work I "
           "declined because the delivery could not be held. A requirement that was never priced is "
           "not a commitment somebody made; it is a gift somebody gave away.", after=80)

    m.para("**Two: the non-conformance that gets closed as a correction.** A dent is hammered out, "
           "the **NCR** is closed, and the reason it happened is still in the process — so it "
           "returns on another project, in front of a customer. My **NCR** and **QDR** entries live "
           "in one register: what was found, what was corrected, the verified **root cause**, the "
           "action, the owner, the date, and when the effect was checked. 5W2H to define the "
           "problem, **5 Why** and **Ishikawa** to get under it, **Pareto** to see which fifth of "
           "the causes produces four fifths of the deviations. On regulated projects I have closed "
           "deviations under GMP/FDA/EMA with **zero critical findings** at handover, with the "
           "authority sitting in the room.", after=80)

    m.para("**Three: the risk register nobody opens after the kick-off.** Forty lines with no owner "
           "is a document, not a control. Every risk I carry is written the same way: cause, "
           "consequence in weeks and in money, a likelihood and consequence class, a threshold that "
           "decides who is allowed to accept it, a **mitigation** with a name and a date, and a "
           "trigger — the observable event that turns the risk into an issue. It is reviewed on a "
           "fixed rhythm, and it is closed only when the mitigation has been shown to work. I have "
           "built that structure for workplace risk (APV), for machinery under the Machinery "
           "Directive with the CE technical file, and across 37 CAPEX projects where a missed date "
           "stopped a production line.", after=80)

    m.para("**Four: the quality plan that lives in a folder.** Every project needs a **PQEP**, and "
           "it is worth exactly what the workshop and the site do with it. Mine is one page: what "
           "is inspected, by whom, at which hold point, against which acceptance criterion, and the "
           "record that closes it — the same page the auditor reads and the same page used at the "
           "bench. That is also how an **audit** stops being annual theatre: the plan is the "
           "checklist, the findings are a trend, and the internal audit finds what the customer "
           "would have found, four weeks earlier. On regulated sites I have been on the inspected "
           "side of authority and customer audits: documents current, answers with evidence, and "
           "the fix verified on the floor rather than in a spreadsheet.", after=80)

    m.para("The toolkit behind that is ordinary and it is in daily use: SAP for project, deviation "
           "and material data; **Excel** for the analysis — **Pareto**, trend and **control charts** "
           "so an action is judged by whether the number moved, not by how the meeting felt; "
           "**PowerPoint** for the report a project manager or a customer can act on; dashboards "
           "built in Excel and with my own AI tools, where Power BI is the same workflow in another "
           "program. **Statistics** without a baseline is decoration, and I only report a change I "
           "can compare with the period before it.", after=80)

    m.para("**Why this company.** NOV SPS is one of three makers of flexible pipe in the world, and "
           "the pipe is made to order, unit by unit — so the quality system is not a certificate on "
           "a wall, it is the only thing that makes the next serial number as good as the last. That "
           "is the work I want: making the system the reason it repeats, and the reason a customer "
           "signs the next frame agreement.", after=80)

    m.para("**Practicalities.** Based in Måløv, 25 minutes from **Brøndby**; **Kalundborg** is a "
           "normal day trip by car, so the occasional travel the role mentions is not a constraint. "
           "Driving licence B. **Danish** native, **English** professional in writing and in "
           "meetings. Available at short notice.", after=60)
    m.meta("Kind regards", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- page 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFILE")
    m.para("Quality and risk engineer from manufacturing and critical infrastructure: authorised "
           "marine and mechanical engineer (maskinmester) at LV/MV/HV level, B.Tech in technology "
           "management. 37 CAPEX projects with **FAT/SAT**, IQ/OQ/PQ and **zero critical findings** "
           "at handover; deviations, CAPA and change control under GMP/FDA/EMA; 11 contracts and 14 "
           "people with full P&L; four years of 24/7 plant operation with 40 per cent lower energy "
           "consumption.", after=80)

    m.section("QUALITY IN A MAKE-TO-ORDER ENVIRONMENT")
    for label, body in [
        ("Requirements and deviations",
         "**Tender** and **contract review** before signature, with a written deviation list; "
         "**NCR** and **QDR** in one register from detection to verified effect."),
        ("Documentation and traceability",
         "Protocols written before the test, IQ/OQ/PQ, as-builts and handover files that a person "
         "who was not in the room can follow."),
        ("Procedures that hold at night",
         "Work instructions written with the people who execute them, tested on the shift with the "
         "least support — that is where a procedure is judged."),
    ]:
        m.bullet(label, body)

    m.section("RISK, ROOT CAUSE AND CONTROL")
    for label, body in [
        ("Register, threshold, trigger",
         "Likelihood and consequence class, **mitigation** with an owner and a date, residual risk "
         "accepted by a named person, trigger defined before it fires."),
        ("Root cause, not symptom",
         "5W2H, **5 Why**, **Ishikawa** and **Pareto** on one A3 page that carries the decision and "
         "the evidence into the same document."),
        ("Effect control",
         "Every action re-measured after a fixed interval and closed with **PDCA** only when the "
         "number moved — 40 per cent higher productivity verified after the changes landed."),
    ]:
        m.bullet(label, body)

    m.section("AUDIT, CUSTOMER AND SUPPLIER")
    for label, body in [
        ("The inspected side",
         "Authority and customer **audit**s under GMP/FDA/EMA — documents current, answers with "
         "evidence, findings closed on the floor, zero critical findings."),
        ("Supplier and subcontractor",
         "Pre-qualification, documentation review and follow-up on site; a supplier's "
         "**non-conformance** is treated as ours, not as theirs."),
        ("Customer interface",
         "Fixed **quality** meetings per contract on open items by age, rework and deviation count "
         "— the numbers a customer can challenge."),
    ]:
        m.bullet(label, body)

    m.section("EXPERIENCE")
    m.job("Owner / Technical Director", "ELOHVAC ApS · Copenhagen · May 2023–present",
          scope="5 electricians + 3 apprentices · full P&L · tender, contract and delivery")
    m.bullet("Commercial and technical risk",
              "**Tender review**, contract terms and deviation lists before signature; supplier and "
              "subcontractor control; one quality plan per project and a close-out file the customer "
              "accepts without a second visit.")

    m.job("Senior Commissioning Engineer / Project Manager",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024",
          scope="37 concurrent CAPEX projects · 25 specialists · GMP/FDA/EMA")
    m.bullet("Deviations, CAPA and acceptance",
              "Deviations closed on verified root cause with CAPA and effect check; FAT/SAT and "
              "IQ/OQ/PQ protocols before the test; milestones and documentation in SAP — **zero "
              "critical findings** at handover.")

    m.job("Project and Workshop Manager", "Ventek-Air · Copenhagen · Jan 2022–Nov 2022",
          scope="14 employees · 11 concurrent contracts · DKK 2–10 m each")
    m.bullet("Eleven contracts, one standard",
              "The same checklist and the same acceptance criteria across eleven parallel contracts; "
              "non-conformances from crews and suppliers in one register with one owner per line.")

    m.job("Maintenance and Operations Manager", "Biofos (Lynetten) · Copenhagen · Aug 2017–Jan 2022",
          scope="Treatment plant in 24/7 operation · pumps, HVAC, HV switchgear, SCADA")
    m.bullet("Risk on a live plant",
              "APV, LOTO, near-miss handling and planned outages with the fallback designed before "
              "it was needed; recurring faults taken to root cause, and 40 per cent lower energy "
              "consumption through PDCA.")

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
           "· **Based in Måløv**, 25 minutes from Brøndby and a day trip to Kalundborg by car · "
           "**Driving licence B** · **Available at short notice** · References on request.", after=70)

    m.models_table(
        "FIRST 90 DAYS — FROM THE PROJECT REGISTER TO A RISK PICTURE A PM CAN STEER BY",
        ["Period", "What happens, and how it is measured"],
        [
            ("Week 1–2",
             "Read the live **PQEP**s, the **NCR**/**QDR** register and the top **risks** of the "
             "projects I am given; walk the interfaces where a requirement becomes a purchase order "
             "— engineering, procurement, Kalundborg production."),
            ("Day 30",
             "One **risk assessment** template and one **NCR** workflow agreed with the project "
             "managers; every open item has an owner, a date and a trigger; the oldest items handled "
             "first, by age rather than by voice."),
            ("Day 60",
             "First customer **quality** meeting run on my own numbers — open items by age, rework, "
             "deviation trend — and a **tender review** delivered with a written deviation list "
             "before signature."),
            ("Day 90",
             "**Internal audit** plan for the next two quarters and one **supplier audit** "
             "completed; mitigation effectiveness re-measured on the items closed in month one, so "
             "management sees a trend instead of a count."),
        ],
        widths=(1500, 8830))

    m.section("A HOLD POINT IS A DECISION, NOT A SIGNATURE")
    m.para("A signature that is given without evidence is worse than a test that is late, because it "
           "hides the question instead of asking it. So I arrive at the hold point knowing the "
           "acceptance criterion, I check the calibration before I check the reading, and I write "
           "the result down while the unit is still on the bench. If the number is outside the "
           "criterion, the answer is no — and the conversation about what that costs happens before "
           "the pipe is packed, not after it is wet.", after=70)

    m.section("THE CLAUSE YOU DID NOT PRICE IS A GIFT YOU GAVE AWAY")
    m.para("Contract review is not a reading exercise; it is the last moment when a requirement can "
           "still be turned into a price, a clarification or a refusal. So every requirement gets a "
           "line, a verdict and a name, and the ones we cannot meet are written into the tender as "
           "deviations — because a deviation in the tender is a commercial position, and the same "
           "deviation in the NCR register is a loss. That is why I read the customer's specification "
           "with production and procurement in the room, not alone at a desk.", after=70)

    m.section("THE AUDIT SHOULD FIND IT BEFORE THE CUSTOMER DOES")
    m.para("An internal audit that only produces a count of findings is a calendar item. The useful "
           "output is a trend: the same clause failing in three projects means the process is wrong, "
           "not the three people. I plan audits from the risk register and from the deviations, I "
           "close findings with evidence and a date, and I re-check them in the next round — the "
           "same discipline that carried FDA and EMA inspections on regulated plants with zero "
           "critical findings.", after=70)

    m.section("WHERE I WOULD START")
    m.para("With the register and the oldest line in it. First week: the projects I am assigned, "
           "their PQEPs, their open NCR and QDR items and their five largest risks — read together "
           "with the project manager who owns them, not alone. Then the tender pipeline: what is "
           "being quoted in the next month, and which requirement in it nobody in production has "
           "seen yet.", after=0)

    # ---------------------------------------------------------------- page 4
    m.page_break()
    m.models_table(
        "WHAT THE ROLE REQUIRES — WHAT I HAVE DELIVERED",
        ["Requirement in the posting", "Evidence"],
        [
            ("Collaborate with all relevant internal processes to raise and manage risks",
             "Risk raised where it is created — engineering, procurement, production, service — in "
             "one register with one owner and a review date."),
            ("Lead risk assessments: impacts and threats to operation reliability and efficiency",
             "Technical risk assessments on 37 CAPEX projects and a 24/7 plant: failure mode, "
             "consequence, detection, mitigation, residual risk."),
            ("Support contingency planning when needed",
             "Fallback supply designed before a planned outage, spare-part criticality against lead "
             "time, and a plan for the day the critical delivery does not arrive."),
            ("Documentation and records of risk analyses, evaluations and mitigation plans",
             "Living register with version, date and evidence link, in SAP and in the project file — "
             "readable by someone who was not in the room."),
            ("Develop and implement a risk assessment approach within internal processes",
             "One template across workplace (APV), machinery (CE file, Machinery Directive) and "
             "project risk — same classes, same thresholds."),
            ("Report risk results to stakeholders, including risk status from a quality perspective",
             "Fixed rhythm with three numbers: new, open past due, closed with effect verified — and "
             "what they mean for the delivery date."),
            ("Develop controls and monitoring, follow up on mitigation effectiveness",
             "An action closed is not an action effective: each mitigation is re-measured after a "
             "fixed interval against the number it was meant to move."),
            ("Provide training and awareness sessions on risk procedures",
             "20-minute toolbox sessions with one procedure and one example from our own site; "
             "apprentices trained on APV and LOTO from their first week."),
            ("Periodic quality meetings with the customer and customer satisfaction follow-up",
             "Fixed customer meetings per contract on open items by age, rework and deviation count "
             "— measured on numbers the customer can challenge."),
            ("Tender review and contract review of the customer's requirements",
             "Every requirement marked can / can with clarification / cannot; deviations written "
             "into the tender before signature, with full P&L risk since 2023."),
            ("NCR and QDR management",
             "Deviation and CAPA handling under GMP/FDA/EMA with zero critical findings: correction, "
             "root cause, action, owner, date, effect check."),
            ("Manage and perform the customer's internal quality audit",
             "Audit-ready as routine: authority and customer inspections, documents current, answers "
             "with evidence, findings closed on the floor."),
            ("Prepare and issue the Project Quality and Execution Plan (PQEP)",
             "One page per project: what is inspected, by whom, at which hold point, the acceptance "
             "criterion and the closing record — used at the bench, not filed."),
            ("Integrate quality and risk into all project phases with engineering and procurement",
             "Gate reviews at requirement, design, purchase, production and load-out; a supplier's "
             "non-conformity is treated as ours."),
            ("Provide training and awareness sessions on quality procedures",
             "Procedures written with the people who execute them, tested on the night shift and "
             "revised when a deviation shows they were unclear."),
            ("Ensure compliance with regulatory requirements, standards and company policy",
             "Compliance matrix with requirement, control, responsible, interval and evidence — "
             "DS/HD 60364, Machinery Directive CE files, GMP/FDA/EMA, internal policy."),
            ("Conduct audits and quality checks throughout project phases",
             "Incoming, in-process and final checks with hold points across 11 concurrent contracts "
             "and 37 projects against the same checklist."),
            ("Degree in mechanical engineering or another relevant engineering discipline, in a manufacturing or industrial environment",
             "Authorised marine and mechanical engineer (maskinmester, EQF 6), B.Tech in technology "
             "management; 12-technician workshop and regulated production at Novo Nordisk."),
            ("Root cause analyses and quality tools: Ishikawa, 5W2H, 5 Why, Pareto, PDCA, control graphs",
             "A3 with 5W2H, 5 Why and Ishikawa for cause, Pareto for ranking, trend and control "
             "charts for effect, PDCA to close — 40 per cent lower energy consumption verified."),
            ("Risk assessment methodologies: identify, evaluate, classify and define mitigation",
             "Likelihood and consequence classes with a threshold that names who may accept the "
             "risk; mitigation with owner, date and a check that it worked."),
            ("Internal and supplier audits; project quality management with customer and non-conformity treatment",
             "Supplier and subcontractor pre-qualification, documentation review and follow-up on "
             "site; customer meetings per contract; non-conformities closed on root cause."),
            ("Fluent English, PowerPoint, intermediate Excel, statistic tools and dashboards",
             "English in writing and meetings; Excel and PowerPoint daily — SAP extracts, Pareto, "
             "KPI dashboards and decision papers; dashboards in Excel and my own AI tools, Power BI "
             "being the same workflow in another tool."),
            ("PMI CRMP or PMP certification, supplier management, API Q1, ISO 9001 reading and internal auditor, fluent Danish",
             "Delivered, not certified: baseline, forecast, risk register, change log and acceptance "
             "protocol, 37 projects; supplier management with full P&L; API Q1 read as ISO 9001 plus "
             "petroleum product realisation — design validation, traceability, NCR/CAPA, management "
             "review; ISO 9001 clauses read against the floor (8.4, 8.7, 10.2, 9.3); Danish native."),
        ],
        widths=(3600, 6746))

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_NOV_ProjectQualityRiskEngineer.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_NOV_ProjectQualityRiskEngineer.docx'))
