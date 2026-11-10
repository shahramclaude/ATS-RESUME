# -*- coding: utf-8 -*-
"""Service Sales Manager - Offshore Service Sales — Johnson Controls Global Marine Service Denmark
(GMOS-DK), Aarhus. ENGLISH posting -> English document (en-GB), per master/README.md.

Four pages, fixed format: letter p1, CV p2, education + 90-day plan + method sections + "Where I
would start" p3, requirement matrix p4. The posting says "send us your application today through our
website" — the format is unchanged.

STYLE (master/STILREGISTER.md; approved by scripts/style_guard.py, 3/3 shift vs #220):
  register    = MARITIM/OFFSHORE — regime, weather window, port call, dry dock, mobilisation, crew
                rotation, bed space, class survey. Shifted from commercial (#220) and from the
                technical registers (#219/#214/#213). Last used #210.
  opening     = H (THE DAY) — 07:15 a compressor nameplate photographed three days out of Aarhus;
                11:40 a platform engineer with a door and a bed-space budget; 16:20 an estimate priced
                against a port call and a dry dock; 21:00 an answer from Singapore. Last used #186.
  structure   = THE DECISION CHAIN — the trip, the survey, the estimate, the window, the execution
                and the next cycle. Last used #214.
  cadence     = short sentences; one clock time, one port or one part number in every other line.

CULTURE SYNC (policy 04.11.2026), sources in master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md §192:
  **Johnson Controls Global Marine Service Denmark (GMOS-DK)**, Aarhus — "a branch specialised in
  supplying our customers with innovative service-, retrofit- and parts solutions on a global scale",
  "today we are the market leaders within HVAC/R applications for the marine industry". The posting's
  own words: "trusted partner to offshore operators and marine customers", "global customer
  portfolio", "sales pipeline", "seek out, qualify and close simple, large & complex sales of
  HVAC/R", "Green HVAC/R products and solutions", "more agile, digital and sustainable organisation",
  close work "with technical, operational, and commercial stakeholders across the organization",
  "approximately 30 travel days per year", "ethics, processes, and tools".
  Buyer-side facts (johnsoncontrols.com marine & navy pages, Global Marine & Navy profile brochure,
  ShipServ supplier data): installed base of **more than 10,000 installations** (another JCI brochure:
  **18,000**) — "more than **20 percent** of all larger ocean-going vessels"; a global marine service
  network with a full **24/7** technical support covering **SABROE, STAL, YORK, Gram and Frick**
  compressors; service lines: service on demand, original spare parts, service agreements, compressor
  factory overhauls and exchange, **R22 phase-out and refrigerant conversion**, HVAC&R service and
  survey, **retrofit and upgrade**, controls equipment; segments **Merchant, Fishery, Navy, Offshore
  and Cruise**; **58 ports** globally; JCI marine supplies HVAC equipment into vessels "for over 130
  years"; offshore-specific services include **door services** (specialist engineers for external
  boundary doors offshore, aligned with TR integrity testing to cut cost and bed space) and
  **reinstatement and recommissioning** of dormant ventilation, modules or whole rigs.
  Company scale quoted in the posting: **130,000+ employees**, **2,000+ locations**.

  Third Johnson Controls document (#219 Sabroe/Holme, #220 HVAC sales/Hornslet, this one marine).
  **Nothing is reused from either:** no 1897, 122 °C, 95 °C, 27 MW or 2,300 m² (from #219), and no
  F-gas/GWP argument, no kroner-and-margin cadence and no Danish thesis opening (from #220).

No invented facts. Documented base: four years as **owner of the plant** in 24/7 operation — HVAC,
cooling, pumps, HV switchgear, SRO/SCADA, on-call — and the invoices that follow a failure (Biofos
2017-2022); **own service company since 2023** with full **P&L**, estimates, spare parts, response
times and 5 electricians + 3 apprentices (ELOHVAC); **14 people and 11 concurrent contracts** with
suppliers and subcontractors (Ventek-Air 2022); **37 CAPEX projects** with FAT/SAT, zero critical
findings, change control in SAP and authorities reading the documentation (Novo Nordisk 2022-2024);
**12 technicians** (ARJ 2003-2010); **B.Tech, Technology Management and Mechanical Engineering**
(Copenhagen School of Marine Engineering & Technology Management, EQF 6, 7.6/12), **electrical and
mechanical design** (EQF 6), **Danish authorised marine engineer** LV/MV/HV (May 2023), **refrigeration
and HVAC technology** (AMU 2021), **STCW safety** (2021-2023); Danish native, English professional.
**Deliberate wording:** no claim of having sold service to offshore operators, of having sailed as a
marine engineer, of seagoing service, of CRM system experience (SAP for budgets and change control is
documented; a named CRM is not), or of marine customer references. Relocation to Aarhus is stated as
a prerequisite, because the role is based there.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Service Sales Manager · offshore service sales · marine HVAC/R service, retrofit and parts'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Denmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='en-GB')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("10 November 2026")
    m.meta("Service Sales Manager, Offshore Service Sales · Johnson Controls Global Marine Service "
           "Denmark · Aarhus")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Application: Service Sales Manager, Offshore Service Sales", bold=True, color='1A1A1A')
    m.para("Dear Mohammad,", after=60)

    # ---------------------------------------------------------------- page 1
    m.para("**07:15.** The first message of the day is a photograph of a compressor nameplate on a "
           "vessel three days out of Aarhus: **SABROE**, 1998, still carrying the provision plant. "
           "**11:40** a platform engineer calls about a door that will not seal and a bed-space "
           "budget that will not stretch to a second mobilisation. **16:20** an estimate goes out for "
           "an overhaul exchange, priced once against a port call in Algeciras and once against a dry "
           "dock in March. **21:00** an answer arrives from Singapore, and the day ends where it "
           "started: with a plant that somebody has to keep running.", after=80)

    m.para("**That is a day of service sales. But the order was decided months earlier, in a chain of "
           "small decisions — and the chain is what I would own.** At **GMOS-DK** the portfolio is "
           "global and the equipment is already installed: more than **10,000** installations and "
           "more than **20 per cent** of all larger ocean-going vessels, **SABROE**, **STAL**, "
           "**YORK**, **Gram** and **FRICK** compressors, **58 ports**, and a **24/7** network that "
           "has to answer at the hour the vessel is alongside. That is a service business sold on "
           "timing, not on catalogue pages — and **GMOS-DK** is the **market leader** in HVAC/R for the "
           "marine industry, now moving towards **green** solutions.", after=80)

    m.para("**The trigger.** A leak, an alarm, a **class** survey comment, or a compressor that has "
           "run 40,000 hours. The cost is never measured in kW: it is a hotel bill in port, a standby "
           "vessel, or two days of production lost while a **dry dock** waits for a part that is six "
           "weeks out. The first job in this role is to hear the trigger before the customer has to "
           "explain it twice.", after=80)

    m.para("**The survey.** Somebody has to look at the plant and know which findings are urgent. I "
           "have spent four years walking plants that run around the clock — **HVAC**, cooling, "
           "pumps, switchgear, controls — and reading reports written by people who were not there. "
           "A **survey** that says 'replace everything' is not a survey; it is a wish with a price "
           "list. The useful one says what can wait until the next **port call** and what cannot.", after=80)

    m.para("**The estimate.** Repair, **overhaul** or **exchange** — three answers with three lead "
           "times and three risk profiles, and the customer needs to see all three. An **estimate** "
           "is a plan before it is a price: what is included, what is excluded, what happens if the "
           "shaft is worse than the report suggested. I have written estimates where the margin was "
           "mine to lose, and I have learned to put the bad news in the document rather than in a "
           "phone call three weeks later.", after=80)

    m.para("**The window.** A **ship** gives you an arrival, a departure and nothing in between. A rig "
           "gives you a weather window and a bed-space limit. A **proposal** that ignores the window "
           "is a wish, however competitive the number is. This is where **parts** availability, "
           "engineer mobilisation and the local partner decide whether the sale is real — and where a "
           "seller who has run a service business himself is worth something to the customer.", after=80)

    m.para("**The execution and the next cycle.** **Commissioning**, documentation, and one page that "
           "goes into the service agreement and into the account plan. Then the pipeline: what this "
           "customer will need next year, and what he will need when the refrigerant is no longer "
           "available. The **R22** phase-out and **retrofit** work in this portfolio are not a "
           "campaign; they are a calendar, and somebody has to keep it.", after=80)

    m.para("**What I bring.** Four years as the owner of the plant, in 24/7 operation, paying for the "
           "failures; three years running my own service company with **estimates**, **spare parts**, "
           "response times and a **P&L**; 37 projects delivered with FAT/SAT and zero critical "
           "findings; and a marine engineering education from the Copenhagen School of Marine "
           "Engineering with **STCW** safety training behind it. **English** and **Danish** both work "
           "as working languages.", after=80)

    m.para("**What I have not done.** I have not sold service to **offshore operators**, and I have "
           "not sailed as a marine engineer. I have been the customer who bought exactly this kind of "
           "service, and I remember what made me sign — and what made me go elsewhere. The **CRM** "
           "system you use, I will learn; the habit of documenting progress on an account every week "
           "is already mine.", after=80)

    m.para("**Practicalities.** The role is in **Aarhus**, and I live in Måløv today — that is a "
           "relocation, not a commute, and I am moving for it. **30 travel days** a year is the part "
           "of the job I would enjoy most: a plant read from a report is half a plant. **Danish "
           "authorised marine engineer** (LV/MV/HV), B.Tech in mechanical engineering. Available by "
           "agreement.", after=60)
    m.meta("Kind regards", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- page 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFILE")
    m.para("Service sales and technical operations professional with twenty years in cooling, HVAC "
           "and electrical plant. Owns a service company with full **P&L**: estimates, spare parts, "
           "response times and a customer portfolio — plus four years owning a plant in 24/7 "
           "operation, where downtime arrived with an invoice. Danish authorised marine engineer, "
           "B.Tech in mechanical engineering.", after=80)

    m.section("SERVICE SALES AND CUSTOMER OWNERSHIP")
    for label, body in [
        ("Customer portfolio",
         "Own company since 2023: service agreements with a fixed response time, priced per plant and "
         "renewed on performance rather than on discount."),
        ("Estimates and proposals",
         "Repair, overhaul and exchange options priced with lead times, exclusions and risk — written "
         "so the customer can choose, not so the seller can win on price alone."),
        ("Pipeline discipline",
         "Every account documented weekly: what was quoted, what is open, what the next trigger is "
         "and who owes whom an answer."),
    ]:
        m.bullet(label, body)

    m.section("HVAC/R SERVICE, SPARES AND RETROFIT")
    for label, body in [
        ("Plant in operation",
         "Four years owning HVAC, cooling, pumps, HV switchgear and SRO/SCADA in 24/7 duty, with "
         "on-call and the failure reports that follow."),
        ("Parts and lead times",
         "Spare parts identified from nameplate and drawing, ordered against a window, and chased — "
         "the difference between a repair and a lost week."),
        ("Retrofit and upgrade",
         "Equipment replaced or upgraded on measured performance, with commissioning and "
         "documentation handed over at the end."),
    ]:
        m.bullet(label, body)

    m.section("COMMERCIAL CONTROL AND STAKEHOLDERS")
    for label, body in [
        ("P&L and margin",
         "Full profit and loss responsibility since 2023, with price, hours and material reconciled "
         "per job — no order signed without knowing what it earns."),
        ("Contracts and change",
         "Change control in SAP, supplier requirements and contractual interfaces with engineering, "
         "procurement and operations on 37 capital projects."),
        ("Across the organisation",
         "Technical, operational and commercial stakeholders aligned before the offer left the "
         "building, not after the plant was mobilised."),
    ]:
        m.bullet(label, body)

    m.section("EMPLOYMENT HISTORY")
    m.job("Owner / Technical Director", "ELOHVAC ApS · Copenhagen · May 2023–present",
          scope="5 electricians + 3 apprentices · full P&L · estimates, spares and service agreements")
    m.bullet("Sold, priced and delivered",
              "Service agreements with response times and written terms; zero critical deviations in "
              "the service contracts and an order book delivered as it was sold.")

    m.job("Senior Commissioning Engineer / Project Manager",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · Nov 2022–Jul 2024",
          scope="37 capital projects · 25 specialists · engineering, procurement and operations · SAP")
    m.bullet("Interface management",
              "Changes priced and approved before work started, contractual interfaces kept separate, "
              "and documentation that passed the authority's review.")

    m.job("Project and Workshop Manager", "Ventek-Air · Copenhagen · Jan 2022–Nov 2022",
          scope="14 staff · 11 concurrent contracts · suppliers and subcontractors")
    m.bullet("Eleven customers, eleven agreements",
              "Schedule, price and changes kept apart per job, so no customer paid for another's delay.")

    m.job("Head of Operations and Maintenance", "Biofos (Lynetten) · Copenhagen · Aug 2017–Jan 2022",
          scope="Wastewater plant in 24/7 operation · HVAC, cooling, pumps, HV switchgear, SRO/SCADA")
    m.bullet("The owner's view",
              "Service agreements, inspections and suppliers run for four years — the experience that "
              "makes an estimate credible to a plant owner.")

    m.job("Production Foreman / Electromechanic",
          "ARJ Engineering · Tehran · 2003–2010 · 12 mechanics and technicians")
    m.bullet("First leadership role",
              "Shift planning, allocation and training in a workshop where machines, tools and "
              "drawings were in daily use.")

    # ---------------------------------------------------------------- page 3
    m.page_break()
    m.section("EDUCATION AND AUTHORISATION")
    m.edu("Danish authorised marine engineer — LV/MV/HV authorisation",
          "Danish Safety Technology Authority · May 2023")
    m.edu("B.Tech, Technology Management and Mechanical Engineering (EQF 6)",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7.6/12")
    m.edu("Electrical and Mechanical Design, Electrical Engineering (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("Refrigeration and HVAC technology (AMU) · Lean: 5S, PDCA, VSM, A3 · STCW safety",
          "Mercantec 2021 · Danish Maritime Authority 2021–2023")

    m.section("LANGUAGES, PRACTICALITIES AND REFERENCES")
    m.para("**Danish:** native · **English:** professional, written and verbal · **Persian:** native · "
           "**Lives in Måløv** and applies with **relocation to Aarhus** in view · **Driving licence "
           "B** · **30 travel days a year:** no objection · **Available by agreement** · References on "
           "request.", after=70)

    m.models_table(
        "THE FIRST 90 DAYS — FROM PORTFOLIO TO PIPELINE",
        ["Period", "What happens, and how it is measured"],
        [
            ("Week 1–2",
             "Read the portfolio: the twenty largest **offshore** accounts, what was quoted last "
             "year, what was won and what went to a competitor. Sail the paper trail of three "
             "completed **retrofits** and one **overhaul exchange**."),
            ("Day 30",
             "One page per account: plant on board, age, refrigerant, next **class** date and next "
             "**dry dock** or **port call**. Reviewed with the service engineers before it goes into "
             "the **CRM**."),
            ("Day 60",
             "Three **estimates** in the customer's hands where the window, the **parts** lead time "
             "and the engineering have been agreed internally first — and a documented joint visit "
             "with a service engineer to the two largest operators."),
            ("Day 90",
             "A **sales pipeline** with values, probabilities and dates, an account plan for every "
             "account above a set threshold, and a clear answer to one question: which customers will "
             "need a **retrofit** before their next special survey, and who is going to tell them."),
        ],
        widths=(1500, 8830))

    m.section("A PROPOSAL IS A PLAN, NOT A PRICE")
    m.para("The customer does not buy a compressor; he buys a plant that runs until the next survey "
           "and a bill he can defend. An estimate therefore has to say what is included, what is not, "
           "and what happens if the opening reveals something worse. I have signed estimates from both "
           "sides of the table, and the ones that survived carried the bad news from the start.", after=70)

    m.section("THE WINDOW IS THE PRODUCT")
    m.para("A service sale is only real when it fits between arrival and departure. Engineers have to "
           "be mobilised, parts have to clear customs, and a partner has to be standing at the quay "
           "when the vessel is — otherwise the cheapest offer in the pile is also the most expensive "
           "one. In my own company a missed window cost me the customer, not just the job, and I have "
           "priced every promise against a calendar since.", after=70)

    m.section("SERVICE IS SOLD IN THE YEAR BEFORE IT IS NEEDED")
    m.para("A customer who discovers the refrigerant is unavailable in the month he needs it has no "
           "good options left. The work of this role is to be there earlier — with a **survey**, an "
           "ageing plant list and a plan for what is replaced in which docking. That is also what "
           "makes the account defensible: the competitor quoting the same part arrives with a price, "
           "we arrive with a calendar.", after=70)

    m.section("DOCUMENT IT OR LOSE IT")
    m.para("Accounts, quotes, visits and promises belong in the system, not in a phone. **CRM** "
           "hygiene is not administration; it is how a colleague can cover an account when I am on a "
           "plane, and how a forecast becomes something the business can plan engineers against. My "
           "habit is a weekly update per account, with the next action and the date it is due.", after=70)

    m.section("THE PEOPLE WHO EXECUTE ARE PART OF THE SALE")
    m.para("A service engineer who has been briefed properly is the best sales argument a company "
           "has. I have been on both sides of that briefing — as the engineer who needed to know what "
           "was promised, and as the seller who had to stand behind it. That is why I would rather "
           "bring an engineer to the customer than a brochure.", after=70)

    m.section("WHERE I WOULD START")
    m.para("With the twenty largest **offshore** accounts and their next **dry dock**. First week: "
           "read what was quoted last year, what was lost and to whom; then put a plant list against "
           "every account, with age, refrigerant and the date the rules or the survey force a "
           "decision. That list is the **sales pipeline** — and it is the first thing I would bring to "
           "the service engineers, before I brought anything to a customer.", after=0)

    # ---------------------------------------------------------------- page 4
    m.page_break()
    m.models_table(
        "WHAT THEY ASK FOR — WHAT I HAVE",
        ["Requirement in the posting", "Evidence"],
        [
            ("Ownership of developing and growing **Offshore** Service Sales across a global customer "
             "portfolio",
             "Own company since 2023 with full **P&L**, an order book and a customer portfolio run "
             "personally; four years owning a plant where downtime had a price."),
            ("Identify business opportunities and build long-term customer relationships",
             "Service agreements renewed on performance in own company; 11 concurrent customer "
             "contracts at Ventek-Air, each with its own scope, price and schedule."),
            ("Drive service growth through innovative **HVAC/R** solutions",
             "Plant upgraded on measured performance in own company and in 37 projects; cooling, "
             "**HVAC** and controls treated as a system — retrofit sold as **energy efficiency**, with "
             "**natural refrigerants** where the plant allows it and a **sustainable** case the customer "
             "can budget for."),
            ("Create innovative, competitive, high quality and timely **estimates** and **proposals**",
             "Three years of estimates written and signed on own margin: options, lead times, "
             "exclusions and risk stated, so the price survives the execution."),
            ("Utilise applicable **sales tools** effectively to plan and document progress",
             "Weekly account discipline per customer, with next action and date; SAP for budgets and "
             "change control. The named **CRM** system I will learn — the habit is already there."),
            ("Seek out, qualify and close simple, large and complex sales of **HVAC/R**",
             "Small service jobs and 37 capital projects sold or delivered; qualified on what the "
             "plant actually needs, not on what the catalogue offers."),
            ("Create long-term customer relations and satisfaction",
             "Customers who call again because they know the response time; zero critical deviations "
             "in the service contracts."),
            ("Work to the highest standard using company ethics, processes and tools",
             "Change control in SAP and documentation accepted by authorities under GMP/FDA/EMA — "
             "process discipline is how I have kept 37 projects auditable."),
            ("Travelling to visit clients and potential clients, approximately **30 travel days** per "
             "year",
             "Used to sites across Denmark and to supplier visits; travel is the part of the job I "
             "would want most, and relocation to **Aarhus** is already planned."),
            ("Customer driven, adaptable sales representative with strong communication skills",
             "Selling, pricing and delivering in own name in **Danish** and **English**; short, "
             "factual communication with engineers and buyers alike."),
            ("Experience in **sales tools** and **CRM** systems",
             "Pipeline and account documentation run weekly in own company; SAP documented. A named "
             "**CRM** platform is not on my CV — stated openly, and closed in the first month."),
            ("Knowledge and/or experience within the **marine** segment, **HVAC/R**",
             "Marine engineering education plus four years of **HVAC** and cooling plant in 24/7 "
             "operation. No marine customer portfolio yet — the technical base and the service "
             "instinct are documented."),
            ("Technical flair and interest for industrial or marine refrigeration",
             "Refrigeration and HVAC technology (AMU), electrical and mechanical design, LV/MV/HV "
             "authorisation; **compressor**, controls and **parts** knowledge from own service work, "
             "including legacy **R404A** plants and retrofit planning."),
            ("Ability to operate, understand and advise customers with complex solutions",
             "37 complex installations advised, commissioned and handed over with zero critical "
             "findings — advice given at the plant, not from a desk."),
            ("Fluency in **English** and **Danish**, written and verbal",
             "**Danish** native, **English** professional: tenders, documentation and meetings in "
             "both languages."),
            ("Education as a **Marine Engineer**, Mechanical Engineer, Electrical/Automation Engineer "
             "or similar",
             "**Danish authorised marine engineer** (LV/MV/HV, 2023), **B.Tech** mechanical "
             "engineering from the Copenhagen School of Marine Engineering (7.6/12), electrical and "
             "mechanical design (EQF 6)."),
            ("Work closely with technical, operational and commercial **stakeholders** across the "
             "organisation",
             "Engineering, procurement and operations aligned before offers went out on 37 projects; "
             "service engineers briefed before every mobilisation."),
            ("Responsibility for customer portfolio, **sales pipeline** and **business development**",
             "Portfolio, pipeline and development owned in own company: price, margin, delivery and "
             "the next sale all on the same desk."),
        ],
        widths=(3600, 6746))

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_JohnsonControls_ServiceSalesManagerOffshore.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_JohnsonControls_ServiceSalesManagerOffshore.docx'))
