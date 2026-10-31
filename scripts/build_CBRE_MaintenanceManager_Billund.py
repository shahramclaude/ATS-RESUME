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
           "Måløv")

DATE = "31. oktober 2026"
RECIPIENT = ("CBRE Global Workplace Solutions · Hard Services, Bygnings-teamet · Billund · "
             "Att.: Jan Nygaard, Senior Technical Manager · Job ID 294768")
SUBJECT = "Ansøgning: Maintenance Manager / Teamleder — Billund (Job ID 294768)"

# ------------------------------------------------------------------ side 1
# ALT på side 1 handler om opgaven og stillingen — ikke om ansøgeren.
INTRO = [
    "Opgaven i Billund er ikke at skrive en vedligeholdsstrategi. Den er at holde en bygningsmasse kørende "
    "hver dag med et team på seks-syv faglærte, en budgetramme, nogle KPI'er nogen spørger ind til hver "
    "måned, og en kunde der mærker det med det samme, hvis en dør, et tag eller et toilet ikke virker. Det er "
    "en driftsopgave med ledelse i midten — tømrer-, VVS- og malerarbejde, projekter, brand, el, teknik og "
    "asset management — og den bliver løst eller ikke løst af arbejdsgangene omkring de seks-syv mennesker.",

    "Nedenfor er min læsning af stillingen og det system, der allerede ligger klar til at tage den: planen, "
    "møderne, målingerne et team kan se sig selv i, og budgettet der kan forklares i én tabel.",
]

BULLETS = [
    ("Kravet: daglig ledelse af seks-syv faglærte",
     "Løsningen er en fast møderytme og en kompetencematrix. Ugen lægges på et kort tavlemøde mandag morgen: "
     "hvad skal løses, hvem gør hvad, hvad er akut, og hvad bliver skubbet. Hver medarbejder — tømrer, VVS, "
     "maler — har en linje i matrixen med næste skridt aftalt, 1:1 hver fjerde uge og performanceopfølgning på "
     "faste punkter, så kompetenceudvikling og rekruttering bliver en plan og ikke en reaktion."),

    ("Kravet: KPI'er og budgetansvar for drift og vedligehold",
     "Løsningen er ét tal pr. opgave og én ejer pr. tal: oppetid, responstid, gentagne fejl og økonomi på en "
     "tavle, hvor medarbejderen kan se sin egen linje. Budgettet følges månedligt med prognose og "
     "cost-to-complete, så afvigelser bliver forklaret i den måned, de opstår — ikke opdaget i december."),

    ("Kravet: effektiv drift og vedligehold af bygninger og installationer",
     "Løsningen er en kritikalitetsstyret vedligeholdsplan med årshjul for lovpligtige eftersyn — el, brand, "
     "VVS, ventilation, adgang og elevatorgrænseflader — og et fast format for, hvad der registreres på "
     "runderne. Asset, arbejdsordre og lukning med årsag: samme logik som Planon og Smartsheet, uanset system."),

    ("Kravet: akutte hændelser og skiftende prioriteter",
     "Løsningen er, at en sag først lukkes, når årsagen er registreret: A3-root-cause og fem-hvorfor, så den "
     "samme fejl ikke kommer igen næste måned. Prioriteringen bliver sagt højt til den, der venter — og "
     "beslutningen om, hvad der kan vente, står skriftligt samme dag."),

    ("Kravet: leverandører, entreprenører og teknisk sparring på projekter",
     "Løsningen er én indgang til teamet og en skriftlig opgavegrænse, før arbejdet starter: hvem gør hvad, "
     "hvornår, med hvilken sikkerhedsdokumentation og til hvilken pris. Fagligt kan jeg gå ind i el, "
     "ventilation, varme og køl med håndværkeren — LV/MV/HV-autorisation og AMU i køle-/HVAC-teknik — i "
     "stedet for at videresende spørgsmålet."),
]

SYSTEM = ("Systemet er allerede bygget, og det er derfor, jeg kan sige det så konkret: vedligeholdsplanen ligger "
          "som skabelon med kritikalitet og årshjul, KPI-tavlen med baseline og navn på hver linje, "
          "budgetmodellen med prognose og cost-to-complete, og 90-dagesplanen på side 4. Oven i det en "
          "rapporteringsrutine, hvor Python og Claude genererer den ugentlige oversigt ud af de data, der "
          "allerede ligger i CMMS og Excel — så ledelsestiden går til teamet. Bygget til præcis denne type "
          "opgave: mange små opgaver, få hænder, én fast kunde.")

MIRROR = ("Om kravene: personaleledelse i teknisk drift, vedligehold og FM i tyve år; elautoriseret maskinmester "
          "(LV/MV/HV) og B.Tech i Technology Management & Mechanical Engineering; dansk på modersmålsniveau og "
          "engelsk professionelt; Microsoft Office og Excel dagligt, SAP, CMMS og Power BI; struktureret, "
          "løsningsorienteret og vant til at skabe resultater gennem andre.")

HONEST = ("To ting påvirker opgaven og skal siges ligeud: jeg har ikke arbejdet i Planon eller Smartsheet, men i "
          "SAP, CMMS og Power BI og med egne tjekliste- og rapporteringsflows — asset-, arbejdsordre- og "
          "opfølgningslogikken er den samme, og Office og Excel er daglig kost. Og baggrunden er teknisk drift, "
          "produktion og anlæg, ikke byggesektoren: installationerne er de samme, men kunden, entreprenørkulturen "
          "og de tømrer- og malerfaglige traditioner læres ved at gå med ud på opgaverne de første uger.")

CULTURE = ("Hvorfor CBRE, og hvorfor Billund: RISE — Respect, Integrity, Service, Excellence — er de rigtige ord "
           "for en drift, hvor tillid afgør, om kunden ringer igen, og hvor Service er den forskel, brugerne mærker "
           "samme dag. Og jeres stærke forankring i lokalmiljøet i Billund, hvor lokal kultur og internationalt "
           "samarbejde går hånd i hånd, er netop den arbejdsform opgaven kræver: lille team, tæt samarbejde, godt "
           "humør og korte beslutningsveje.")

PRACTICAL = ("Praktisk om opgaven: kort opsigelse og klar til hurtigt start; dansk på modersmålsniveau og engelsk "
             "professionelt; kørekort B og egen bil. Jeg flytter til Billund-området og er bosat der fra starten "
             "frem for at pendle — et team på seks-syv skal kunne regne med, at lederen er på bygningen. Egen "
             "virksomhed afvikles ved ansættelse, så der er ingen konkurrerende forpligtelser.")

CLOSING = ("Jeg vil gerne se bygningerne og møde teamet, og bruge den første samtale på tre spørgsmål: hvilke "
           "KPI'er teamet måles på i dag, hvor de akutte sager kommer fra, og hvad der skal være på plads om 90 "
           "dage, før det er en succes. Ring gerne.")

# ------------------------------------------------------------------ CV
PROFILE = ("Rollen kræver fire ting på én gang: daglig ledelse af et lille faglært team, styr på drift og "
           "vedligehold af bygninger og installationer, budget- og KPI-ansvar, og en person der kan stå mellem "
           "kunde, leverandør og entreprenør. Alle fire har været kerneopgaven i tyve år — med fuldt P&L-ansvar "
           "og personaleansvar siden 2003: 5 elektrikere og 3 lærlinge i egen autoriseret virksomhed, et "
           "14-mands produktions- og montageteam og 25 specialister i et GMP-miljø, alle med kompetencematrix, "
           "1:1-samtaler og performanceopfølgning. Elautoriseret maskinmester (LV/MV/HV), B.Tech i Technology "
           "Management & Mechanical Engineering, SAP og CMMS i drift, Power BI til KPI, dansk på modersmålsniveau "
           "og engelsk professionelt.")

PRACTICE = [
    ("Daglig ledelse, coaching og udvikling",
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
     "Overblik før der ændres noget: de seks-syv medarbejdere og de vigtigste interne kunder mødt, runde på "
     "bygningerne, og de åbne opgaver, akutte sager og den gældende sikkerhedsinstruks gennemgået."),
    ("Uge 1–4",
     "En-til-en med alle seks-syv og en arbejdsdag fulgt hos hver: hvad fylder, hvad irriterer, og hvor går tiden "
     "tabt mellem opgaverne. Vedligeholdsplanen, de åbne opgaver, de sidste 12 måneders akutte hændelser og de "
     "nuværende KPI'er kortlagt."),
    ("Uge 5–8",
     "Daglig planlægning og opfølgning overtaget, så teamet ved, hvad der gælder i dag og i næste uge. KPI-sæt og "
     "rapporteringsform aftalt med Senior Technical Manager — én rapporteringsform, ikke fem."),
    ("Uge 9–12",
     "Akutte hændelser faldet i antal, fordi årsagen registreres; to-tre forbedringer gennemført med målbar effekt "
     "på responstid, gentagne fejl eller vedligeholdsomkostning. Budgetgrundlag for næste periode lagt frem med "
     "tal, ikke skøn."),
    ("Måned 3–6",
     "Vedligeholdsplanen omlagt efter kritikalitet i stedet for efter vane; leverandør- og entreprenøraftaler "
     "gennemgået på pris, responstid og sikkerhedsdokumentation; kompetencematrix og udviklingssamtaler på plads "
     "for hver medarbejder."),
    ("Måned 6–12",
     "Teamet ejer planen selv, og lederen bruges til det, ledere skal bruges til: prioritering, udvikling af folk, "
     "leverandørforhandling og de projekter, der kræver teknisk dømmekraft. Stabile KPI'er og en bygningsmasse, "
     "der holder — uden at det hele hænger på én person."),
    ("Måned 12+",
     "Årshjulet kører af sig selv: lovpligtige eftersyn planlagt et år frem, investeringsbehov dokumenteret med "
     "kritikalitet og pris, kompetencematrix opdateret før næste rekruttering — og en rapportering til Senior "
     "Technical Manager, der kan læses på ét blik."),
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
    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
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
    ("Elautoriseret maskinmester (LV/MV/HV)",
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

    m.para(SYSTEM, after=80)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=80)

    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "LEDELSESPROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
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

    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER TEAMET I DRIFT",
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
