# -*- coding: utf-8 -*-
"""
CBRE Global Workplace Solutions — Maintenance Manager / Teamleder, Billund.
Job ID 294768 · Hard Services Building Team · reference: Jan Nygaard,
Senior Technical Manager. Dansk JD. Bygget i designet fra master-CV'erne.

Vinkel: dette ER hans kernefag — personaleansvar for et lille teknisk team,
budget, KPI'er, leverandører og coaching, med en el-faglig tyngde der gør ham
i stand til at sparre teknisk og ikke kun administrativt. Geografi (Billund)
og Planon/Smartsheet adresseres ærligt.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Maintenance Manager / Teamleder | CBRE GWS | Billund"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Søborg")

DATE = "31. oktober 2026"
RECIPIENT = ("CBRE Global Workplace Solutions · Hard Services, Bygnings-teamet · Billund · "
             "Att.: Jan Nygaard, Senior Technical Manager · Job ID 294768")
SUBJECT = "Ansøgning: Maintenance Manager / Teamleder — Billund (Job ID 294768)"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Et team på seks-syv håndværkere leverer ikke på sine KPI'er, fordi nogen har skrevet en plan. Det leverer, "
    "fordi nogen hver morgen ved, hvem der laver hvad i dag, hvilke opgaver der er akutte, og hvad der bliver "
    "skubbet — og fordi den, der leder, kan svare fagligt, når en tømrer eller VVS-mand siger, at opgaven ikke "
    "kan løses som beskrevet. Det er den rolle, jeg har haft i tyve år, og det er den, jeg søger her.",

    "Jeg er autoriseret el-installatør med B.Tech i Technology Management & Mechanical Engineering, og jeg har "
    "ledet tekniske teams af netop den størrelse: 5 elektrikere og 3 lærlinge i min egen virksomhed, et "
    "14-mands produktions- og montageteam og en 25-specialist organisation i et GMP-miljø. Fælles for dem alle er, "
    "at resultatet kom gennem andre — ikke gennem mig.",
]

BULLETS = [
    ("Personaleansvar for et teknisk team — prøvet, ikke læst",
     "Daglig ledelse af 5 elektrikere og 3 lærlinge med kompetencematrix, 1:1-samtaler, performanceopfølgning og "
     "rekruttering; 14-mands produktions- og montageteam; og tværfaglig ledelse af 25 specialister. Coaching og "
     "situationsbestemt ledelse er ikke et program, jeg har været på — det er den måde, jeg har drevet teams på."),

    ("Budgetansvar og KPI'er, fulgt op månedligt",
     "Fuldt P&L-ansvar i egen virksomhed: budget, prognose, indkøb og leverandøraftaler. I driftsrollen havde jeg "
     "drifts- og vedligeholdelsesbudgetter i SAP og KPI'er på oppetid, responstid og økonomi — og brugte dem til "
     "at pege på, hvor der skulle handles, ikke bare til at rapportere."),

    ("Teknisk sparring, ikke kun administrativ",
     "Autoriseret el-installatør (LV/MV/HV) med egenkontrol og dokumentationsansvar, suppleret med køle- og "
     "HVAC-teknik (AMU). Jeg kan gå ind i el, tavler, ventilation, varme og køl og vurdere opgaven med "
     "håndværkeren i stedet for at videresende den."),

    ("Akutte hændelser og skiftende prioriteter",
     "24/7-anlæg i fem år med nul tolerance for uplanlagte stop, og i dag 40+ serviceanlæg, hvor dagen bliver "
     "prioriteret om efter, hvad der ringer. Jeg er vant til at beslutte, hvad der skal vente — og til at sige "
     "det højt til den, der venter."),

    ("Forbedring af vedligeholdelsesprocesser",
     "PDCA-baseret vedligeholdsplan med fast årshjul, kritikalitetsvurdering, A3-root-cause og standardarbejde; "
     "−40 % energikost og +40 % produktivitet dokumenteret — begge målt før og efter, og begge fastholdt, efter "
     "projektet var slut."),
]

MIRROR = ("Mod jeres ønsker: erfaring med personaleledelse inden for teknisk drift, vedligehold og facility "
          "management · relevant teknisk baggrund som autoriseret el-installatør og B.Tech i Technology Management "
          "& Mechanical Engineering · dansk og engelsk, skriftligt og mundtligt · vant til mange interessenter og "
          "skiftende prioriteter · struktureret og løsningsorienteret, og motiveret af at skabe resultater gennem "
          "andre.")

HONEST = ("Tre ting, lige ud. Jeg bor i Søborg, og stillingen er i Billund — det er ikke en pendlerløsning, "
          "og jeg søger med en klar forventning om at flytte. "
          "Jeg har ikke arbejdet i Planon eller Smartsheet; jeg har arbejdet i SAP, CMMS og Power BI og bygget "
          "mine egne tjekliste- og rapporteringsflows, så systemer er en tilvænningssag, ikke en barriere — Excel "
          "og Office kører jeg til daglig. Og jeg har ikke været i byggesektoren som sådan; jeg kommer fra teknisk "
          "drift, produktion og anlæg, hvor bygninger, el, VVS og ventilation er de samme installationer, men "
          "kunden og kulturen er en anden, jeg skal lære.")

CULTURE = ("Hvorfor CBRE, og hvorfor Billund. Jeres RISE-værdier — Respect, Integrity, Service, Excellence — er "
           "ikke svære at underskrive for en, der kommer fra en branche, hvor tillid afgør, om kunden ringer "
           "igen. Og det, I skriver om at være stærkt forankret i lokalmiljøet i Billund, mens kunden og "
           "kollegerne er internationale, er præcis den kombination jeg trives i: et lille team med tæt samarbejde "
           "og godt humør — en lokal kultur, som leverer til en global standard. Jeg har prøvet begge yderpunkter — det store "
           "anlægsprojekt og den lille virksomhed — og det er i den lokale forankring, jeg gør den største "
           "forskel.")

PRACTICAL = ("Praktisk: kort opsigelse og klar til at starte hurtigt; dansk på modersmålsniveau og engelsk "
             "professionelt; kørekort B og egen bil. Jeg er indstillet på at flytte til Billund-området og vil "
             "være bosat der fra starten frem for at pendle — et team på seks-syv medarbejdere skal kunne regne "
             "med, at lederen er til stede. Ved ansættelse afvikler jeg min egen virksomhed, så der er ingen "
             "konkurrerende forpligtelser i hverdagen.")

CLOSING = ("Jeg vil gerne møde teamet og se de bygninger, de holder — og jeg vil hellere tale om, hvordan "
           "morgenen starter for de seks-syv medarbejdere, end om min CV-linje. Ring gerne, hvis det er lettere at "
           "tage den første snak over telefonen.")

# ------------------------------------------------------------------ CV
PROFILE = ("Teknisk leder med 20+ års erfaring fra tekniske installationer, 24/7-drift og reguleret produktion — "
           "personaleansvar siden 2003 og fuldt P&L-ansvar. Har ledet tekniske teams af samme størrelse som dette: "
           "5 elektrikere og 3 lærlinge i egen autoriseret virksomhed, et 14-mands produktions- og montageteam og "
           "25 specialister i et GMP-miljø, med kompetencematricer, 1:1-samtaler, performanceopfølgning og "
           "rekruttering. Budget- og KPI-ansvar for drift og vedligehold, leverandører og entreprenører, og "
           "forbedringsarbejde med dokumenteret effekt: −40 % energikost og +40 % produktivitet. Autoriseret "
           "el-installatør (LV/MV/HV), B.Tech i Technology Management & Mechanical Engineering, fortrolig med SAP, "
           "CMMS, Power BI og Office, dansk på modersmålsniveau og engelsk professionelt.")

PRACTICE = [
    ("Ledelse af tekniske medarbejdere",
     "Daglig ledelse, coaching og situationsbestemt ledelse; kompetencematrix og udviklingsplaner; 1:1-samtaler, "
     "performance- og lønopfølgning; rekruttering og onboarding af lærlinge og faglærte."),

    ("Planlægning, koordinering og KPI",
     "Daglig prioritering af opgaver og bemanding, opfølgning på KPI'er for oppetid, responstid og økonomi, og "
     "ugentlig gennemgang af, hvad der blev skubbet og hvorfor. KPI'er med navn på, ikke grafer uden ansvar."),

    ("Drift og vedligehold af bygninger og installationer",
     "El, tavler og koblingsanlæg, LV/MV/HV, nødstrøm, ventilation, varme og køl, vand, trykluft, brand-anlæg og "
     "CTS; forebyggende plan, lovpligtige eftersyn og akutte hændelser på aktive bygninger."),

    ("Budget, indkøb og leverandører",
     "Budgetansvar og prognose, indkøb og prissammenligning, leverandør- og entreprenøraftaler, "
     "sikkerhedsdokumentation og tilsyn; fuldt P&L-ansvar i egen virksomhed med 40+ serviceanlæg."),

    ("Interessenter og kommunikation",
     "Primær kontaktperson mellem kunde, kolleger, leverandører og håndværkere; teknisk og administrativ "
     "sparring på større projekter; tydelig besked, når en opgave kræver mere tid eller flere penge."),

    ("Forbedring og systemer",
     "PDCA, A3-root-cause, 5S og standardarbejde; vedligeholdsprocesser, der bliver fulgt, fordi de er enkle; "
     "CMMS og SAP som kilde til sandheden, Power BI til KPI og økonomi, Python/Claude til automatiseret "
     "rapportering og tjeklister."),
]

FIRST90 = [
    ("Dag 1–5",
     "Præsenterer mig for de seks-syv medarbejdere og for de vigtigste interne kunder i Billund, går en runde på "
     "bygningerne og får overblik over de åbne opgaver, de akutte sager og den gældende sikkerhedsinstruks, før "
     "jeg ændrer noget som helst."),
    ("Uge 1–4",
     "Møder de seks-syv medarbejdere enkeltvis og følger deres arbejdsdag: hvad fylder, hvad irriterer, og hvor "
     "går tiden tabt mellem opgaverne. Gennemgår vedligeholdsplanen, de åbne opgaver, de sidste 12 måneders "
     "akutte hændelser og de KPI'er, teamet bliver målt på."),
    ("Uge 5–8",
     "Overtager den daglige planlægning og opfølgning, så teamet ved, hvad der gælder i dag og i næste uge. "
     "Aftaler med Senior Technical Manager, hvilke KPI'er vi styrer efter, og hvordan status meldes — én "
     "rapporteringsform, ikke fem."),
    ("Uge 9–12",
     "De akutte hændelser falder i antal, fordi årsagen bliver fundet og registreret; to-tre "
     "forbedringer gennemført med målbar effekt på responstid, gentagne fejl eller vedligeholdsomkostning. "
     "Budget grundlag for næste periode lagt frem med tal, ikke skøn."),
    ("Måned 3–6",
     "Vedligeholdsplanen omlagt efter kritikalitet i stedet for efter vane; leverandør- og entreprenøraftaler "
     "gennemgået med blik for pris, responstid og sikkerhedsdokumentation; kompetencematrix og "
     "udviklingssamtaler på plads for hver medarbejder, så udvikling ikke kun sker i hovedet på lederen."),
    ("Måned 6–12",
     "Et team, der selv tager ansvar for planen, og en leder der bliver brugt til det, ledere skal bruges til: "
     "prioritering, udvikling af folk, leverandørforhandling og de projekter, der kræver teknisk dømmekraft. "
     "Stabile KPI'er og en bygningsmasse, der holder — uden at det hele hænger på mig."),
]

MODELS = [
    ("Ledelse & udvikling",
     "Situationsbestemt ledelse, coaching og GROW, 1:1 og performanceopfølgning, kompetencematrix og "
     "udviklingsplaner, rekruttering og onboarding, tavlemøder og daglig styring, arbejdsmiljø og sikker adfærd"),
    ("Drift & vedligehold",
     "Forebyggende vedligeholdsplan og årshjul, lovpligtige eftersyn, akutte hændelser og fejlfinding, "
     "kritikalitetsvurdering, reservedelsstyring, A3-root-cause og fem-hvorfor, 5S og standardarbejde"),
    ("Bygninger & installationer",
     "El, tavler og koblingsanlæg, LV/MV/HV, nødstrøm, VVS, ventilation og klima, varme og køl, brand-anlæg, "
     "CTS/BMS, adgangs- og elevatorgrænseflader, tømrer-, maler- og montagearbejde i projekter"),
    ("Økonomi & indkøb",
     "Budget og budgetopfølgning, prognose og cost-to-complete, indkøb og prissammenligning, leverandør- og "
     "entreprenøraftaler, serviceaftaler og SLA, fakturering og afstemning, investeringscases (NPV, IRR)"),
    ("KPI & rapportering",
     "KPI-definition og baseline, oppetid og responstid, gentagne fejl og nedetid, vedligeholdsomkostning pr. "
     "anlæg, månedlig rapportering, Power BI-dashboards og Excel-modeller, ledelsesrapportering"),
    ("Systemer & IT",
     "SAP ERP og CMMS, Planon- og Smartsheet-principper (asset, arbejdsordrer, planer, opfølgning), Microsoft "
     "Office og Excel, SharePoint som dokumentbase, Power BI, Python og Claude API til automatisering"),
    ("Sikkerhed & compliance",
     "APV og risikovurdering, LOTO og sikringsprocedurer, arbejdstilladelser, entreprenørkontrol på aktive "
     "anlæg, near-miss-opfølgning, myndighedskrav og dokumentationspligt"),
    ("El-fagligt ansvar",
     "Autorisation og egenkontrol, kredsskemaer og el-dokumentation, DS/HD 60364 og EN 61439, måling og test "
     "(isolation, kontinuitet, RCD), fejlfinding og spændingssætning"),
]

ACHIEVEMENTS = [
    ("Team af samme størrelse ledet i dag",
     "5 elektrikere og 3 lærlinge med kompetencematrix, 1:1-samtaler, performanceopfølgning og udvikling."),
    ("+40 % produktivitet",
     "i egen virksomhed gennem dataunderstøttet planlægning, standardarbejde og egen AI-tooling — målt over tid."),
    ("−40 % energikost",
     "i reguleret produktion via struktureret PDCA, A3 og standardiserede løsninger; fastholdt efter projektets "
     "afslutning."),
    ("24/7-drift uden uplanlagte stop",
     "pumper, HVAC, koblingsanlæg, højspænding og SCADA — oppetid gennem forebyggende vedligehold og hurtig "
     "fejlfinding."),
    ("Nul kritiske afvigelser ved aflevering",
     "på 37 samtidige anlægsprojekter (2–10 mio. kr.) — dokumentation og aflevering uden fund."),
]

EXPERIENCE = [
    ("Indehaver / Teknisk direktør / Autoriseret el-installatør",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg i Storkøbenhavn · fuldt P&L, budget og leverandøraftaler",
     [("Personaleansvar",
       "daglig ledelse, 1:1-samtaler, performanceopfølgning, kompetencematrix, sikkerhed og udvikling af både "
       "faglærte og lærlinge."),
      ("Budget, indkøb og leverandører",
       "budget og prognose, indkøb af komponenter og serviceydelser, leverandøraftaler og prissammenligning; "
       "fuldt ansvar for bundlinjen."),
      ("Drift og akutte hændelser",
       "planlagt og afhjælpende vedligehold, fejlfinding på el, tavler, styring, ventilation og klima; "
       "prioritering mellem adresser, når flere ting haster på samme tid."),
      ("Systemer og rapportering",
       "ERP-baseret ordre- og reservedelsstyring, Power BI-dashboards og Python/Claude-værktøjer til "
       "planlægning, tjeklister og rapportering; produktivitetsløft over 40 %.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · drifts- og "
     "vedligeholdelsesbudgetter i SAP",
     [("Vedligeholdsplan og KPI",
       "PDCA-baseret vedligeholdsplan med fast årshjul, A3-root-cause på større nedetid, reservedelsflow og "
       "kritiske lagre; KPI'er og driftsbudgetter i SAP ERP."),
      ("24/7 teknisk drift",
       "oppetid, forebyggende vedligehold og hurtig fejlfinding; koordinering af egne teknikere, entreprenører "
       "og leverandører."),
      ("Sikkerhed og arbejdsmiljø",
       "LOTO, risikovurdering, arbejdstilladelser, near-miss-rapportering og værktøjsmøder.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister inden for teknik, indkøb og drift · "
     "GMP/FDA/EMA",
     [("Tværfaglig ledelse",
       "25 specialister på tværs af mekanik, el, proces og indkøb; tekniske afklaringer og beslutninger "
       "dokumenteret, så alle arbejdede efter samme aftale."),
      ("Projekt og økonomi",
       "tidsplan, økonomi, risiko og månedlig rapportering til ledelse og kunde; −40 % energikost gennem PDCA "
       "og standardiseret arbejde."),
      ("Idriftsættelse og aflevering",
       "FAT/SAT, IQ/OQ/PQ og valideringsdokumentation med afvigelseshåndtering, CAPA og change control — nul "
       "kritiske fund ved aflevering.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Ledelse af håndværkere",
       "14-personers produktions- og montageteam med kapacitetsplanlægning, flowstyring og daglige tavlemøder "
       "over 11 samtidige projekter."),
      ("Kvalitet og sikkerhed",
       "standardiseret arbejde ved hver station, arbejdstilladelser og sikkerhedsdokumentation ved montage i "
       "bygninger, hvor driften kørte videre.")]),

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

REFERENCES = "Tidligere ledere hos Biofos (Lynetten) og Novo Nordisk A/S (Kalundborg) — oplyses ved henvendelse."

KEYWORDS = (
    "Maintenance Manager · Teamleder · Team Leader · Hard Services · Building Team · Bygninger · Vedligehold · "
    "Drift og Vedligehold · Tekniske Installationer · Tømrer · VVS · Maler · Projektopgaver · Personaleledelse · "
    "Ledelse · Coaching · Kompetenceudvikling · Performanceopfølgning · Rekruttering · Medarbejderudvikling · "
    "KPI · Budgetansvar · Budget · Interessenter · Leverandører · Entreprenører · Optimering · Forbedring · "
    "Vedligeholdelsesprocesser · Akutte Hændelser · Fejlfinding · Teknisk Sparring · Administration · Facility "
    "Management · FM · Asset Management · Brand · El · Teknik · Planlægning · Koordinering · Opfølgning · Microsoft "
    "Office · Excel · Smartsheet · Planon · SharePoint · IT-Kompetencer · Systemer · CMMS · SAP · ERP · Power BI · "
    "Struktureret · Løsningsorienteret · Resultater Gennem Andre · Samarbejde · Dansk · Engelsk · Billund · "
    "GWS Segment · CBRE"
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

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=80)

    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "LEDELSESPROFIL")
    m.para(PROFILE, after=80)

    m.section("LEDELSE, BUDGET OG DRIFT — BEVIS, IKKE PÅSTANDE")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("LEDELSESMETODER & FAGLIGE VÆRKTØJER — ANVENDT I PRAKSIS",
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

    m.models_table("FØRSTE 90 DAGE — SÅDAN LEDER JEG TEAMET",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    # ingen afsnit eller tabelrække må knække over en sideskift
    for _p in m.doc.paragraphs:
        _p.paragraph_format.keep_together = True
    for _tbl in m.doc.tables:
        for _row in _tbl.rows:
            for _c in _row.cells:
                for _p in _c.paragraphs:
                    _p.paragraph_format.keep_together = True

    # ingen tabelrække må knække over en sideskift
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
                  title="Ansøgning og CV — Maintenance Manager / Teamleder, CBRE GWS Billund",
                  subject="Personaleledelse · hard services · bygninger og installationer · budget og KPI · "
                          "Billund",
                  keywords=("maintenance manager, teamleder, personaleledelse, hard services, bygninger, "
                            "vedligehold, budget, kpi, leverandører, planon, smartsheet, excel, "
                            "kompetenceudvikling, dansk, engelsk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1, CV side 2-4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_CBRE_MaintenanceManager_Billund.docx")
    print("OK", build(out))
