# -*- coding: utf-8 -*-
"""
CBRE Global Workplace Solutions — Business Development Manager, København.
Job ID 277446 · GWS Segment · Facilities Management · dansk JD.
Bygget i designet fra master-CV'erne — og efter den bindende regel:
dokumentet handler om opgaven, missionen og stillingen, ikke om ansøgeren.
Side 1 = "Kravet → Løsningen er" + "Systemet er allerede bygget".
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Business Development Manager | CBRE GWS | København"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Søborg")

DATE = "31. oktober 2026"
RECIPIENT = ("CBRE Global Workplace Solutions · GWS Segment · København · "
             "Facilities Management · Job ID 277446")
SUBJECT = "Ansøgning: Business Development Manager — CBRE GWS, København (Job ID 277446)"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Opgaven er ikke at sælge en ydelse. Den er at bygge en pipeline af større, komplekse FM-aftaler, hvor "
    "hver sag løber 6–18 måneder, har fire til otte beslutningstagere og bliver vundet på en business case, "
    "kunden kan forsvare over for sin CFO. Det kræver to ting på samme tid: at kunne regne på, hvad hard FM "
    "koster og kan levere i en produktions-, logistik- eller infrastrukturvirksomhed — og at kunne drive en "
    "proces, der ikke handler om at ringe flest gange, men om at kvalificere rigtigt og gå videre.",

    "Nedenfor er min læsning af stillingen og det salgssystem, der ligger klar: målkundemodel, "
    "kvalificeringskriterier, business case for hard FM, stage-gates og en forecast, der kan stå til ansvar.",
]

BULLETS = [
    ("Kravet: dokumenteret hard FM-erfaring",
     "Løsningen er teknisk troværdighed i mødet med kundens drifts- og teknikchef. Jeg har selv stået med "
     "anlæggene — el og tavler, VVS, ventilation, varme og køl, brand og CTS, både på 24/7-site og i 40+ "
     "serviceanlæg — og er autoriseret el-installatør (LV/MV/HV). Derfor kan business casen bygges på "
     "reelle tal: asset-tilstand, backlog, responstider, energiforbrug og hvad nedetid koster kunden."),

    ("Kravet: strategisk B2B-salg og løsningssalg",
     "Løsningen er at sælge på problemet og totalomkostningen, ikke på timen. Jeg har bygget en kundebase "
     "fra nul i egen virksomhed — aftaler solgt, prissat og forhandlet med både tekniske og kommercielle "
     "beslutningstagere — og har stået på leverandørsiden i større projekter med udbud, kontraktvilkår og "
     "aflevering som fast ramme."),

    ("Kravet: identificere og opsøge nye kunder og strategiske samarbejdspartnere",
     "Løsningen er en målkundemodel med stage-gates og exit-kriterier: en sag flytter sig kun, når behov, "
     "beslutningskompetence, tidsplan og budget er dokumenteret. Konti segmenteres på branche og trigger — "
     "udbud, kontraktudløb, ny fabrik eller lager, ESG-krav — og forecast vægtes pr. stage."),

    ("Kravet: lange salgsforløb med C-level og stakeholder management",
     "Løsningen er en mange-trådet account plan: hvem ejer budgettet, hvem bliver målt på driften, hvem kan "
     "stoppe sagen, og hvad hver af dem skal kunne forsvare internt. MEDDIC og SPIN afdækker "
     "beslutningskriterierne tidligt, og hvert møde forlader kunden med en aftalt næste handling."),

    ("Kravet: udbud, kontraktforhandling og overlevering til drift",
     "Løsningen er at være bindeled mellem kunde og interne specialister og behandle udbuddet som et "
     "projekt: svarmatrix, ansvarsfordeling og tidsplan, så svaret står færdigt før fristen. Kommercielt "
     "arbejdes der med SLA, indeksregulering, ansvarsgrænser og margin — og overleveringen til drift aftales "
     "før underskrift: mobiliseringsplan og 90 dages overdragelse."),
]

SYSTEM = ("Systemet er allerede bygget: målkundemodellen med 40–60 konti segmenteret på branche og "
          "trigger, kvalificeringsscorecardet, business case-modellen for hard FM (omkostning pr. m², "
          "asset-tilstand, backlog, responstid, energi) med Power BI-visning, stage-gate-planen med "
          "exit-kriterier, den vægtede forecast og overleveringschecklisten. Oven i det en rutine, hvor "
          "Python og Claude genererer den ugentlige pipeline- og forecast-oversigt — så sælgerens tid går "
          "til kunderne.")

MIRROR = ("Om kravene: strategisk B2B-salg og løsningssalg fra egen virksomhed med fuldt P&L-ansvar; "
          "hard FM-faglighed som autoriseret el-installatør (LV/MV/HV) med drift af 40+ serviceanlæg og et "
          "24/7-site; kommerciel forståelse og modenhed i salgsrollen fra pris, indkøb og margin; "
          "selvstændig opbygning af kundebase; dansk på modersmålsniveau og engelsk professionelt.")

HONEST = ("To ting påvirker opgaven og skal siges ligeud: jeg har ikke solgt integrerede FM-kontrakter "
          "fra en FM-udbyder før — min salgserfaring er tekniske service- og driftsaftaler fra egen "
          "virksomhed og leverandørsiden i større projekter, og udbyderens prisliste, marginmodel og "
          "mobiliseringsmaskine skal læres. Til gengæld har jeg stået på kundens side af bordet i udbud og "
          "kontraktforhandlinger, og det er den halvdel, der afgør, om et tilbud bliver valgt. Netværket i "
          "FM bygges konto for konto — det er hunter-opgaven.")

CULTURE = ("Hvorfor CBRE: RISE — Respect, Integrity, Service, Excellence — er de rigtige ord i et salg, "
           "hvor en aftale først er god, når driften kan levere den bagefter. Og jeres vækstmål, der har "
           "for vane at blive indfriet, beskriver netop, hvad opgaven kræver: en pipeline der kan gentages "
           "og skaleres, og en sælger der selv skaber mulighederne.")

PRACTICAL = ("Praktisk: bosat i Søborg, så de tre faste dage på ét af jeres sites er uden forhindringer; "
             "kørekort B og egen bil; dansk på modersmålsniveau og engelsk professionelt; kort opsigelse og "
             "klar til hurtigt start; egen virksomhed afvikles ved ansættelse.")

CLOSING = ("Jeg vil gerne høre, hvordan I arbejder med pipeline i dag, og bruge første samtale på tre "
           "spørgsmål: hvilke segmenter der er prioriteret de næste tolv måneder, hvordan en kvalificeret "
           "mulighed defineres internt, og hvad der kendetegner de aftaler, I har vundet.")

# ------------------------------------------------------------------ CV
PROFILE = ("Rollen kræver fire ting på én gang: hard FM-faglighed nok til at tale med kundens "
           "drifts- og teknikchef, kommercielt ejerskab over pris og margin, en struktureret pipeline "
           "med forecast der holder, og evnen til at drive et udbud og en kontraktforhandling i mål "
           "sammen med specialister og legal. Alle fire har været en del af arbejdet i tyve år — med "
           "fuldt P&L-ansvar og personaleansvar siden 2003: 40+ serviceanlæg og 5 elektrikere i egen "
           "autoriseret virksomhed, 37 samtidige anlægsprojekter på 2–10 mio. kr. hos Novo Nordisk og "
           "24/7-drift på Biofos Lynetten. Autoriseret el-installatør (LV/MV/HV), B.Tech i Technology "
           "Management & Mechanical Engineering, dansk på modersmålsniveau og engelsk professionelt.")

PRACTICE = [
    ("Målkunder og segmentering",
     "Produktion, logistik, lager og infrastruktur segmenteret på branche, ejendomsmasse og "
     "kritikalitet; triggerbaseret prospektering — udbud, kontraktudløb, nyetablering, "
     "ejendomstransaktioner, ESG- og energikrav; 40–60 prioriterede konti med account plan på de 15 "
     "vigtigste."),

    ("Kvalificering før der bruges tid",
     "Exit-kriterier pr. stage: behov dokumenteret, beslutningskompetence identificeret, tidsplan og "
     "budget afklaret, konkurrencesituationen kendt. MEDDIC og SPIN som samtalestruktur, så "
     "beslutningskriterierne kommer på bordet i møde to og ikke i møde ni."),

    ("Business case for hard FM",
     "Totalomkostning i stedet for timepris: omkostning pr. m², asset-tilstand og backlog, responstid "
     "og SLA-niveau, energiforbrug, nedetidskostnad i produktion og logistik; NPV, IRR og payback, så "
     "kundens CFO kan godkende sagen på tal."),

    ("Pipeline, forecast og rapportering",
     "En sund pipeline med fokus på kvalitet og margin: stage-gate 0–6 med vægtet forecast, win-rate og "
     "cyklustid som styringstal; ugentlig gennemgang, hvor ingen sag står grøn uden en aftalt næste "
     "handling med kunden; månedlig performance- og forecast-rapportering i Power BI."),

    ("Udbud og kontraktforhandling",
     "Udbud som projekt: kravspecifikation, svarmatrix, ansvarsfordeling og tidsplan; kommercielle "
     "vilkår — SLA og KPI-bonus, indeksregulering, ansvarsgrænser, exit — afstemt med drift, finance "
     "og legal før tilbud afgives."),

    ("Overlevering til drift",
     "Mobiliseringsplan og RACI før underskrift; KPI-ejerskab overdraget til driftslederen på et "
     "fælles møde; 90-dages overdragelse med statusmøder, så kundens første kvartal ikke bliver "
     "sælgerens løfte, men driftsorganisationens leverance."),

    ("Teknisk salgsstøtte og specialister",
     "Kan gå i dybden med el, tavler, ventilation, varme og køl, brand og CTS, så specialisterne "
     "bruges på det, de er bedst til, og kunden ikke skal forklares sin egen drift to gange."),
]

FIRST90 = [
    ("Uge 1–2",
     "Onboarding på kundebasen: nuværende kontrakter, prisliste og marginer, win/loss på de seneste "
     "24 måneder, og møder med drift, specialister og finance — så et tilbud kan bygges på det, "
     "organisationen faktisk kan levere."),
    ("Uge 3–6",
     "Målkundeliste på 40–60 konti segmenteret og trigger-analyseret; top 15 får account plan med "
     "beslutningskort, mulig kontraktværdi og næste handling. Kvalificeringsscorecard og "
     "business case-skabelon taget i brug."),
    ("Uge 7–12",
     "10–15 kvalificerede dialoger i gang med kunder i produktion, logistik, lager og infrastruktur; "
     "forecast indført med stage-gates og ugentlig gennemgang; standardmateriale til første møde "
     "klar, så specialister kan kobles på tidligt."),
    ("Måned 3–6",
     "Første 2–3 sager i udbuds- eller tilbudsfase med aftalt svarmatrix og tidsplan; win/loss-review "
     "gennemført; prisliste og marginmodel kalibreret med drift og finance; netværk mod rådgivere, "
     "mæglere og entreprenører etableret som leadkanal."),
    ("Måned 6–12",
     "Pipeline dækker kvoten med mindst 3x vægtet værdi; 1–2 kontrakter vundet; overleveringsmodellen "
     "kørt mindst én gang med kunde og drift, så referencen kan bruges i næste sag."),
    ("Måned 12+",
     "En gentagelig motor: kontotriggere, netværkskanaler og partnerhenvisninger giver løbende nye "
     "muligheder; forecast-præcision over 80 %, og en win-rate der kan dokumenteres pr. segment."),
]

MODELS = [
    ("Prospektering & segmentering",
     "ICP-definition, branchesegmentering (produktion, logistik, lager, infrastruktur), "
     "triggerbaseret prospektering, kontobaseret salg, offentlige udbud, netværk og partnerkanaler"),
    ("Kvalificering",
     "MEDDIC/MEDDPICC, SPIN, BANT, exit-kriterier pr. stage, go/no-go-vurdering, "
     "konkurrent- og alternativanalyse"),
    ("Værdi & business case",
     "Totalomkostning (TCO), omkostning pr. m², asset-tilstand og backlog, SLA- og "
     "responstidsmodellering, energiforbrug og ESG-krav, NPV/IRR og payback"),
    ("Pipeline & forecast",
     "Stage-gate 0–6, vægtet forecast, win-rate og cyklustid, CRM-hygiejne, ugentlig pipeline-review, "
     "Power BI-dashboards og Excel-modeller"),
    ("Udbud & kontrakt",
     "Udbudsproces, kravspecifikation og svarmatrix, SLA/KPI-modellering, indeksregulering, "
     "ansvarsgrænser, exit-vilkår, kommerciel risikovurdering"),
    ("Interessenter & C-level",
     "Beslutningskort og mange-trådet account plan, CFO/COO/indkøb, forhandling med BATNA og ZOPA, "
     "fast mødekadence, skriftligt beslutningsgrundlag til hver interessent"),
    ("Overlevering & mobilisering",
     "Mobiliseringsplan og RACI, 90-dages overdragelse, KPI-ejerskab, kunde-onboarding, "
     "statusmøder mellem salg og drift"),
    ("Systemer & data",
     "CRM, Excel-modeller, Power BI, Python og Claude til prospektering, tilbuds- og forecastmodeller, "
     "automatiseret ugentlig rapportering"),
]

ACHIEVEMENTS = [
    ("Kundebase bygget fra nul",
     "40+ serviceanlæg i Storkøbenhavn i egen virksomhed — aftaler solgt, prissat og forhandlet med "
     "både tekniske og kommercielle beslutningstagere."),
    ("Fuldt P&L-ansvar",
     "pris, indkøb, margin og leverandøraftaler; budget og prognose fulgt månedligt med forklaring på "
     "enhver afvigelse."),
    ("+40 % produktivitet",
     "gennem dataunderstøttet planlægning, standardarbejde og egen AI-tooling — målt over tid og "
     "fastholdt."),
    ("37 samtidige anlægsprojekter",
     "2–10 mio. kr. hos Novo Nordisk med udbud, tilbud og aflevering — nul kritiske fund."),
    ("Leverandørsiden i kundens udbud",
     "kravspecifikation, FAT/SAT og kontraktvilkår på 24/7-site (Biofos) og i GMP-miljø — den erfaring "
     "gør det lettere at se, hvor et tilbud bliver valgt eller vraget."),
]

EXPERIENCE = [
    ("Indehaver / Teknisk direktør / Autoriseret el-installatør",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "40+ serviceanlæg i Storkøbenhavn · 5 elektrikere og 3 lærlinge · fuldt P&L, pris og "
     "leverandøraftaler",
     [("Kunder og aftaler",
       "opbygning af kundebase fra nul, tilbud og prissætning, forhandling af service- og "
       "vedligeholdelsesaftaler samt leverandøraftaler."),
      ("Budget, pris og margin",
       "budget og prognose, indkøb og prissammenligning, fuldt ansvar for bundlinjen."),
      ("Drift og akutte hændelser",
       "planlagt og afhjælpende vedligehold, fejlfinding på el, tavler, styring, ventilation og klima; "
       "prioritering mellem adresser, når flere ting haster på samme tid."),
      ("Systemer og rapportering",
       "ERP-baseret ordre- og reservedelsstyring, Power BI-dashboards og Python/Claude-værktøjer til "
       "tilbud, planlægning og rapportering; produktivitetsløft over 40 %.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · drifts- og "
     "vedligeholdelsesbudgetter i SAP",
     [("Leverandører og entreprenører",
       "kravspecifikation, tilbudsevaluering og kontraktopfølgning på et 24/7-site med høj "
       "kritikalitet; koordinering af egne teknikere, entreprenører og leverandører."),
      ("Vedligeholdsplan og KPI",
       "PDCA-baseret vedligeholdsplan med fast årshjul, A3-root-cause på større nedetid, reservedelsflow "
       "og kritiske lagre; KPI'er og driftsbudgetter i SAP ERP."),
      ("Sikkerhed og arbejdsmiljø",
       "LOTO, risikovurdering, arbejdstilladelser, near-miss-rapportering og værktøjsmøder.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister inden for teknik, indkøb og drift · "
     "GMP/FDA/EMA",
     [("Tværfaglig styring",
       "25 specialister på tværs af mekanik, el, proces og indkøb; tekniske afklaringer og beslutninger "
       "dokumenteret, så alle arbejdede efter samme aftale."),
      ("Projekt og økonomi",
       "tidsplan, økonomi, risiko og månedlig rapportering til ledelse og kunde; −40 % energikost "
       "gennem PDCA og standardiseret arbejde."),
      ("Aflevering og dokumentation",
       "FAT/SAT, IQ/OQ/PQ og valideringsdokumentation med afvigelseshåndtering, CAPA og change control "
       "— nul kritiske fund ved aflevering.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Ledelse af håndværkere",
       "14-personers produktions- og montageteam med kapacitetsplanlægning, flowstyring og daglige "
       "tavlemøder over 11 samtidige projekter."),
      ("Kvalitet og sikkerhed",
       "standardiseret arbejde ved hver station, arbejdstilladelser og sikkerhedsdokumentation ved "
       "montage i bygninger, hvor driften kørte videre.")]),

    ("Elektromekaniker / Produktionsteamleder",
     "ARJ Engineering · Teheran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · skiftplanlægning, materialestyring og lager",
     [("Produktionsteam",
       "skiftplanlægning, materialestyring og målopfølgning med situationel coaching."),
      ("Teknisk problemløsning",
       "reparation og diagnosticering af elektriske og mekaniske systemer gennem struktureret "
       "root cause-analyse.")]),
]

EDUCATION = [
    ("B.Tech (EQF niveau 6) — Technology Management & Mechanical Engineering",
     "Maskinmesterskolen / Copenhagen School of Marine Engineering & Technology Management · 2017 – 2022 · "
     "karakter 7,6/12"),
    ("Elektrisk & mekanisk design, el-ingeniør (EQF niveau 6)",
     "Tehran Technical University · 2000 – 2003"),
    ("HF — matematik og fysik",
     "VUC · 2012 – 2017"),
]

CERTS = [
    ("Autoriseret el-installatør (LV/MV/HV)",
     "Sikkerhedsstyrelsen · maj 2023"),
    ("Køle- og HVAC-teknik (AMU)",
     "Mercantec · mar. 2021"),
    ("Arbejdsmiljø §16 og sikkerhedsbevidsthed (VI/6-1)",
     "Søfartsstyrelsen · maj 2021"),
    ("Lean — værdistrømsanalyse, standardarbejde, 5S, A3 og Kaizen",
     "Anvendt i drift · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og projekter · 2017 – nu"),
    ("STCW — maskinrumsvagt (A-III/1), skibssikkerhedsofficer (VI/5)",
     "Søfartsstyrelsen · 2021 – 2023"),
]

LANGUAGES = "Dansk (modersmål) · Engelsk (professionelt, skriftligt og mundtligt) · Persisk/farsi · Kørekort B"

REFERENCES = "Tidligere ledere og kunder hos Biofos (Lynetten), Novo Nordisk A/S (Kalundborg) og egne kunder i ELOHVAC — oplyses ved henvendelse."

KEYWORDS = (
    "Business Development Manager · Business Development · GWS Segment · Facilities Management · "
    "Facility Management · Hard FM · Hard Services · Løsningssalg · Strategisk B2B-salg · B2B-salg · "
    "Salg · Hunter · Kundeportefølje · Pipeline · Forecast · Performance · Margin · Kvalitet · "
    "Stakeholder Management · Beslutningstagere · C-level · Interessenter · Udbud · "
    "Kontraktforhandlinger · Kommercielle Beslutningsprocesser · Kommerciel Forståelse · "
    "Markedsanalyse · Prospektering · Kunde Relationer · Samarbejdspartnere · Specialister · "
    "Overlevering til Drift · Mobilisering · Produktion · Logistik · Lager · Infrastruktur · "
    "Ejendomme · Porteføljer · Drift · Vedligehold · El · VVS · Ventilation · Varme · Køl · "
    "Brand · CTS · Asset Management · KPI · SLA · Totalomkostning · TCO · Business Case · NPV · "
    "Excel · Power BI · CRM · Microsoft Office · SAP · Python · Claude · Selvstændigt · Struktureret · "
    "Rådgivende · Langsigtet · Skalérbar · Gentagelig · Dansk · Engelsk · København · CBRE"
)


def build(path):
    m = MasterDoc(TEMPLATE, lang="da-DK")

    # ---------------------------------------------------------------- side 1
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta(RECIPIENT)

    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, SUBJECT, bold=True, color="1A1A1A")

    for t in INTRO:
        m.para(t, after=80)

    for label, body in BULLETS:
        m.bullet(label, body, after=40)

    m.para(SYSTEM, after=80)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=50)

    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)


    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "KOMMERCIEL PROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("SALGSMETODER & VÆRKTØJER — ANVENDT I PRAKSIS",
                   ("Område", "Metoder og værktøjer"), MODELS)

    m.section("UDVALGTE RESULTATER")
    for label, body in ACHIEVEMENTS:
        m.bullet(label, body, after=30)

    m.section("ERHVERVSERFARING")
    for title, meta, scope, bullets in EXPERIENCE:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=30)

    m.section("UDDANNELSE")
    for t, meta in EDUCATION:
        m.edu(t, meta)

    m.section("AUTORISATIONER & CERTIFICERINGER")
    for t, meta in CERTS:
        m.edu(t, meta)

    m.section("SPROG")
    m.para(LANGUAGES, after=80, justify=False)

    m.section("REFERENCER")
    m.para(REFERENCES, after=80, justify=False)

    m.section("KERNEKOMPETENCER & NØGLEORD")
    m.para(KEYWORDS, after=80)

    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER PIPELINEN I GANG",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    # ingen afsnit eller tabelrække må knække over en sideskift
    for _p in m.doc.paragraphs:
        _p.paragraph_format.keep_together = True
    for _tbl in m.doc.tables:
        for _row in _tbl.rows:
            for _c in _row.cells:
                for _p in _c.paragraphs:
                    _p.paragraph_format.keep_together = True

    from docx.oxml.ns import qn as _qn
    from docx.oxml import OxmlElement as _OE
    for _tbl in m.doc.tables:
        for _tr in _tbl._tbl.findall(_qn("w:tr")):
            _trPr = _tr.find(_qn("w:trPr"))
            if _trPr is None:
                _trPr = _OE("w:trPr")
                _tr.insert(0, _trPr)
            if _trPr.find(_qn("w:cantSplit")) is None:
                _trPr.insert(0, _OE("w:cantSplit"))

    return m.save(path,
                  title="Ansøgning og CV — Business Development Manager, CBRE GWS København",
                  subject="Strategisk B2B-salg · løsningssalg · hard FM · pipeline og forecast · "
                          "udbud og kontrakt · København",
                  keywords=("business development manager, løsningssalg, b2b-salg, hard fm, facility "
                            "management, pipeline, forecast, udbud, kontraktforhandlinger, c-level, "
                            "stakeholder management, dansk, engelsk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1 (krav → løsning), CV side 2-4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_CBRE_BusinessDevelopmentManager.docx")
    print("OK", build(out))
