# -*- coding: utf-8 -*-
"""
TÅRNBYFORSYNING A/S — vandingeniør, vandforsyning (Kastrup).
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Vandingeniør | Vandforsyning, anlægsprojekter og myndighedsdialog"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "31. oktober 2026"
RECIPIENT = ("TÅRNBYFORSYNING A/S · Gemmas Alle 39, 2770 Kastrup · att. driftsleder Bjarne Andersen · "
             "32 46 20 30 · søgt via QuickApply på Jobindex")
SUBJECT = "Ansøgning: vandingeniør til vandforsyningen"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Opgaven er at holde styr på vandet fra indvinding til vandhane: anlægsprojekter der skal styres "
    "både teknisk og økonomisk, indberetninger der skal være rigtige første gang, tal der skal kunne "
    "afstemmes i en benchmarking, og en drikkevandssikkerhed der er dokumenteret, når myndigheden "
    "spørger. Det er ikke ét fag — det er projekter, drift, data og myndighedskontakt på samme tid.",

    "Nedenfor er min læsning af rollen og det system, der står klar fra første dag: projektmodel med "
    "budget og fremdrift pr. anlæg, indberetnings- og dokumentationskalender, dataudtræk der kan "
    "afstemmes til benchmarking og økonomiske rammer, prøvetagnings- og afvigelseslog og en fast "
    "svartid på borgerhenvendelser.",
]

BULLETS = [
    ("Kravet: anlægsprojekter med teknisk og økonomisk styring",
     "Løsningen er en projektmodel med faser, budget pr. leverance, tidsplan og "
     "afvigelsesliste med ejer og frist — 37 samtidige anlægsprojekter i 2–10 mio. kr.-klassen er "
     "gennemført på den måde, med plan, økonomi og rapportering til styregruppen."),

    ("Kravet: dialog med og indberetning til overliggende myndigheder",
     "Løsningen er at levere dokumentation, der er sporbar fra krav til test til afvigelse: jeg har "
     "arbejdet under GMP/FDA/EMA-krav, myndighedstilsyn og revision på Novo Nordisk og i "
     "forsyningsmiljøet, hvor indberetninger og tilsyn er en fast del af året."),

    ("Kravet: levere data til benchmarking og økonomiske rammer for vandselskabet",
     "Løsningen er data, der kan afstemmes: definerede KPI'er, én kilde til hvert tal og et udtræk "
     "der følger myndighedens og benchmarkets definitioner — ikke et regneark, der bliver rettet, "
     "indtil det passer."),

    ("Kravet: arbejde med selskabets vandstrategi",
     "Løsningen er at gøre strategien konkret: vandspild, anlægsinvesteringer og forsyningssikkerhed "
     "omsat til indsatser med ejer, effektmål og business case, så prioriteringen kan forklares "
     "politisk og økonomisk."),

    ("Kravet: vandspild, vandanalyser og dokumenteret drikkevandssikkerhed",
     "Løsningen er et prøvetagnings- og kontrolprogram med fast kadence, log pr. prøve og afvigelse, "
     "og en dokumentstyring med version og ejer, så drikkevandssikkerheden er dokumenteret som praksis "
     "og ikke som mappe."),

    ("Kravet: besvarelse af borgerhenvendelser",
     "Løsningen er fagligt svar med en aftalt svartid: hvad der er årsag, hvad der bliver gjort, og "
     "hvornår borgeren hører næste gang. Jeg har svaret erhvervskunder og borgere i egen virksomhed "
     "og ved, at et godt svar er et svar, der kan forstås uden at kende anlægget."),

    ("Kravet: ingeniør eller lignende akademisk uddannelse samt erfaring med drikkevand og/eller "
     "spildevand",
     "Løsningen er elautoriseret maskinmester (B.Tech, EQF 6) og el-ingeniør — og fem år på "
     "24/7-forsyningsanlægget Lynetten, hvor spildevand, pumper, højspænding og SCADA var hverdagen, "
     "med nul uplanlagte stop i fem år."),
]

SYSTEM = ("Systemet er allerede bygget: projektmodel med budget og fremdrift pr. anlæg, kalender for "
          "indberetninger og tilsyn, KPI- og dataudtræk til benchmarking, prøvetagnings- og "
          "afvigelseslog, dokumentstyring med version og ejer samt en fast svartid på "
          "borgerhenvendelser — i Excel, Power BI og SAP/CMMS, med Python og Claude til analyse og "
          "rapportering.")

MIRROR = ("Om kravene: 20 år i forsyning, drift og projekter — fem år som drifts- og "
          "vedligeholdelseschef på 24/7-forsyningsanlægget Lynetten med nul uplanlagte stop, 37 "
          "anlægsprojekter (2–10 mio. kr.) med 25 specialister under myndighedskrav og dokumentation "
          "uden kritiske fund; elautoriseret maskinmester (LV/MV/HV), B.Tech og el-ingeniør.")

HONEST = ("To ting skal siges ligeud: min vanderfaring er spildevand, ikke drikkevandsbehandling — "
          "indvinding, vandværksdrift og vandanalyser vil jeg skulle lære i jeres anlæg — og "
          "drikkevandssikkerhed har jeg ikke ejet før, men arbejdet under tilsvarende "
          "dokumentationskrav. Det er derfor, jeg vil bruge de første uger sammen med driftslederen og "
          "vandoperatørerne, før jeg foreslår noget.")

CULTURE = ("Hvorfor Tårnby Forsyning: I skriver, at alle hjælper alle, og at der er kort mellem "
           "afdelingerne — for en afdeling med en driftsleder, fem vandoperatører og tre ingeniører er "
           "det ikke en floskel, det er arbejdsformen. Vandværket har ligget på Gemmas Alle siden 1929, "
           "og det er en god påmindelse om, at det, vi bygger og dokumenterer i dag, skal kunne drives af "
           "andre om tyve år.")

PRACTICAL = ("Praktisk: bosat i Måløv — cirka 30 minutter til Gemmas Alle i Kastrup; kørekort B og bil; "
             "dansk på modersmålsniveau i skrift og tale; 37 timer med betalt frokost passer fint; klar "
             "til hurtigt start, og egen virksomhed afvikles ved ansættelse.")

CLOSING = ("Jeg vil gerne se vandværket og møde afdelingen, og bruge første samtale på to spørgsmål: "
           "hvordan I i dag arbejder med vandspild og prøvetagning, og hvor I ser de største "
           "anlægsopgaver de næste par år — og hvordan indberetningerne til myndigheden bliver løftet i "
           "dag.")

# ------------------------------------------------------------------ CV
PROFILE = ("Rollen kræver fire ting på én gang: anlægsprojekter styret teknisk og økonomisk, "
           "indberetninger der holder ved et tilsyn, data der kan afstemmes i en benchmarking, og en "
           "dokumenteret drikkevandssikkerhed. Det tekniske og det dokumentationsmæssige har været "
           "hverdag i 20 år: fem år som drifts- og vedligeholdelseschef på 24/7-forsyningsanlægget "
           "Lynetten med nul uplanlagte stop, 37 anlægsprojekter (2–10 mio. kr.) med 25 specialister "
           "under GMP/FDA/EMA-krav og nul kritiske fund, og 40+ serviceanlæg med fuldt P&L i egen "
           "virksomhed. Elautoriseret maskinmester (B.Tech, EQF 6) og el-ingeniør.")

PRACTICE = [
    ("Anlægsprojekter",
     "Faseopdelt projektmodel med budget pr. leverance, tidsplan, risikolog og afvigelser med ejer og "
     "frist; aflevering med dokumentation og prøver, driften kan overtage."),
    ("Myndighed og dokumentation",
     "Indberetninger og tilsyn håndteret som en fast kalender; sporbarhed fra krav til test til "
     "afvigelse, dokumentstyring med version og ejer og revisionsparat dokumentation."),
    ("Data, KPI og benchmarking",
     "Definerede KPI'er med én kilde pr. tal, udtræk der følger myndighedens og benchmarkets "
     "definitioner, og Power BI-tavler der bliver brugt i den månedlige opfølgning."),
    ("Drift af forsyningsanlæg",
     "24/7-drift med pumper, HVAC, koblingsanlæg, højspænding og SCADA; forebyggende vedligehold, "
     "fejlhistorik og A3-root-cause — nul uplanlagte stop i fem år."),
    ("Kvalitet og prøver",
     "Prøvetagnings- og kontrolprogram med fast kadence, log pr. prøve og afvigelse, "
     "korrigerende handlinger og opfølgning på, om ændringen virkede."),
    ("Teknisk tyngde",
     "Elektriske og mekaniske installationer, tavler og styring, pumper og ventiler, måling og "
     "regulering; elautorisation LV/MV/HV med egenkontrol og dokumentation."),
    ("Borgere og kunder",
     "Fagligt svar med aftalt svartid, også når svaret er, at der ikke er en hurtig løsning; "
     "erhvervskunder og borgere i egen virksomhed og i forsyningsmiljøet."),
]

MODELS = [
    ("Projekt",
     "Faseopdelt model med budget pr. leverance, tidsplan, risikolog og afvigelsesliste med ejer og "
     "frist; afleveringspakke med dokumentation og prøver"),
    ("Myndighed",
     "Indberetnings- og tilsynskalender, sporbarhed fra krav til test til afvigelse, "
     "dokumentstyring med version og ejer"),
    ("Data",
     "KPI-definitioner med én kilde pr. tal, udtræk til benchmarking og økonomiske rammer, "
     "Power BI-tavler og månedlig opfølgning"),
    ("Drift",
     "Forebyggende vedligeholdsplan, kritikalitet og kritiske reservedele, PDCA-årshjul, "
     "KPI'er i SAP og beredskab på 24/7-anlæg"),
    ("Kvalitet",
     "Prøvetagningsprogram, afvigelser med root cause, korrigerende handlinger og opfølgning på "
     "effekt; Lean, A3 og 5S"),
    ("Økonomi",
     "Budget og prognose, kalkule mod timeforbrug, business case for investeringer og "
     "leverandøraftaler"),
    ("Værktøjer",
     "Excel og Power BI, SAP/CMMS, SCADA-data, Python og Claude til analyse og rapportering"),
]

ACHIEVEMENTS = [
    ("Nul uplanlagte stop i fem år",
     "på 24/7-forsyningsanlægget Lynetten — planlagt vedligehold, PDCA og A3-root-cause frem for "
     "brandslukning."),
    ("Nul kritiske fund ved aflevering",
     "37 anlægsprojekter hos Novo Nordisk, 2–10 mio. kr., under GMP/FDA/EMA-krav — FAT/SAT, IQ/OQ/PQ "
     "og valideringsdokumentation."),
    ("25 specialister koordineret",
     "på tværs af mekanik, el, proces og indkøb i 37 samtidige projekter med plan, økonomi og "
     "rapportering til styregruppe."),
    ("+40 % produktivitet og −40 % energikost",
     "dokumenterede forbedringer via måling, standardarbejde, dataunderstøttet planlægning og egen "
     "AI-tooling."),
    ("40+ serviceanlæg og fuldt P&L",
     "drift, kundekontakt, indkøb, lager og leverandøraftaler i egen autoriseret virksomhed — med "
     "ansvar for både teknik og bundlinje."),
]

EXPERIENCE = [
    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · budgetter i SAP",
     [("Drift, data og KPI",
       "PDCA-baseret vedligeholdsplan med fast årshjul, fejlhistorik og KPI'er i SAP; nul uplanlagte "
       "stop i fem år."),
      ("Myndighed, leverandører og sikkerhed",
       "arbejde under myndighedskrav og tilsyn; koordinering af egne teknikere, entreprenører og "
       "leverandører — LOTO, arbejdstilladelser og garantisager.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister · GMP/FDA/EMA",
     [("Projekt, økonomi og rapportering",
       "plan og budget pr. projekt, fremdrift og rapportering til styregruppe; 25 specialister "
       "koordineret på tværs af mekanik, el, proces og indkøb."),
      ("Dokumentation og aflevering",
       "FAT/SAT, IQ/OQ/PQ og valideringsdokumentation med afvigelseshåndtering — nul kritiske fund "
       "ved aflevering.")]),

    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og leverandøraftaler",
     [("Kunder, økonomi og leverandører",
       "serviceaftaler og akutte sager med erhvervskunder, plan og prognose, indkøb og "
       "leverandøraftaler med fuldt ansvar for bundlinjen."),
      ("Teknisk ansvar",
       "dimensionering, fejlfinding og dokumentation på el- og HVAC-anlæg; egenkontrol og "
       "myndighedsforhold i en autoriseret virksomhed.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Projekter og fremdrift",
       "11 samtidige entrepriser med kapacitetsplanlægning, daglige tavlemøder og aflevering til "
       "bygherre.")]),

    ("Elektromekaniker / Produktionsteamleder",
     "ARJ Engineering · Teheran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · skiftplanlægning, materialestyring og lager",
     [("Teknisk problemløsning",
       "reparation og diagnosticering af elektriske og mekaniske systemer gennem struktureret root "
       "cause-analyse samt skiftplanlægning og materialestyring.")]),
]

EDUCATION = [
    ("B.Tech (EQF niveau 6) — Technology Management & Mechanical Engineering",
     "Maskinmesterskolen / Copenhagen School of Marine Engineering & Technology Management · 2017 – "
     "2022 · karakter 7,6/12"),
    ("Elektrisk & mekanisk design, el-ingeniør (EQF niveau 6)",
     "Tehran Technical University · 2000 – 2003"),
    ("HF — matematik og fysik",
     "VUC · 2012 – 2017"),
]

CERTS = [
    ("Elautoriseret maskinmester (LV/MV/HV)",
     "Sikkerhedsstyrelsen · maj 2023"),
    ("Køleteknik & klimaanlæg (AMU)",
     "Mercantec · mar. 2021"),
    ("Arbejdsmiljø §16 og sikkerhedsbevidsthed (VI/6-1)",
     "Søfartsstyrelsen · maj 2021"),
    ("Lean — værdistrømsanalyse, standardarbejde, 5S, A3 og Kaizen",
     "Anvendt i drift og projekter · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og projekter · 2017 – nu"),
]

LANGUAGES = ("Dansk (modersmål, skrift og tale) · Engelsk (professionelt) · Persisk/farsi · "
             "Kørekort B (kategori B)")

PRACTICAL_CV = ("Bosat i Måløv — cirka 30 minutter til Gemmas Alle i Kastrup; kørekort kategori B og "
                "bil; dansk på modersmålsniveau i skrift og tale; klar til hurtigt start; egen "
                "virksomhed afvikles ved ansættelse.")

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Biofos (Lynetten), Novo Nordisk A/S "
              "(Kalundborg), Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Driftslederen og vandoperatørerne",
     "Anlægget kendes bedst af dem, der passer det hver dag; projekter og ændringer bliver aftalt med "
     "driften først, så det, der bliver bygget, også kan vedligeholdes."),
    ("Myndigheden og leverandørerne",
     "Indberetninger og tilsyn som en fast kalender, dokumentation der er sporbar, og leverandøraftaler "
     "hvor krav og acceptkriterier er skrevet ned før indkøb."),
    ("Borgerne",
     "Fagligt svar med aftalt svartid: hvad årsagen er, hvad der bliver gjort, og hvornår de hører "
     "næste gang — også når svaret er, at det tager tid."),
]

FIRST90 = [
    ("Uge 1–2",
     "Gået vandværket og anlæggene igennem med driftslederen og vandoperatørerne; læst "
     "indvindingstilladelse, prøvetagningsprogram, drikkevandssikkerheden og de seneste "
     "indberetninger. Mødt afdelingens to ingeniører og de øvrige afdelinger."),
    ("Uge 3–6",
     "Overtaget de anlægsprojekter, der ligger tættest på; projektmodel med budget, plan og "
     "afvigelsesliste lagt for dem; kalender for indberetninger og tilsyn etableret."),
    ("Uge 7–12",
     "Dataudtræk til benchmarking og økonomiske rammer dokumenteret med definitioner og én kilde pr. "
     "tal; prøvetagnings- og afvigelseslog gennemgået med driften; svartid på borgerhenvendelser "
     "aftalt."),
    ("Måned 3–6",
     "Egne anlægsprojekter leveret med dokumentation og aflevering; vandstrategien omsat til 3–5 "
     "indsatser med ejer og effektmål; første forbedring på vandspild eller prøvetagning målt."),
    ("Måned 6–12",
     "Indberetninger og dokumentation kører uden forsinkelser, og et tilsyn finder dokumentationen i "
     "orden; data til benchmarking er afstemt og forklaret; min rolle er kendt som den, der kan løfte "
     "en sag fra teknisk problem til beslutningsgrundlag."),
]

KEYWORDS = (
    "Vandingeniør · Vandforsyning · Drikkevand · Spildevand · Anlægsprojekter · Teknisk styring · "
    "Økonomisk styring · Myndigheder · Indberetning · Benchmarking · Økonomiske rammer · Vandselskab · "
    "Vandstrategi · Vandspild · Vandanalyser · Drikkevandssikkerhed · Borgerhenvendelser · Ingeniør · "
    "Akademisk uddannelse · Driftsleder · Vandoperatører · Anlæg · Drift · Vandværk · Prøver · "
    "Dokumentation · KPI · Service · Samarbejde · Fjernvarme · Fjernkøl · Indvinding · SCADA · SAP · "
    "Power BI · Excel · Dansk · Kastrup · Måløv"
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
        m.bullet(label, body, after=20)

    m.para(SYSTEM, after=80)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=35)

    m.meta("Med venlig hilsen · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "FAGLIG PROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("ARBEJDSMETODER — ANVENDT I PRAKSIS",
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
    for _i, (t, meta) in enumerate(CERTS):
        _p_ = m.edu(t, meta)
        if _i < len(CERTS) - 1:
            _p_.paragraph_format.keep_with_next = True

    m.section("SPROG")
    m.para(LANGUAGES, after=80, justify=False)

    m.section("KERNEKOMPETENCER & NØGLEORD")
    m.para(KEYWORDS, after=80)

    # afsluttende side
    m.page_break()
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER OPGAVERNE I RYTMEN",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN ARBEJDES DER — DE TRE PARTER")
    for label, body in PARTNER:
        m.bullet(label, body, after=30)

    m.section("PRAKTISK OM ANSÆTTELSEN")
    m.para(PRACTICAL_CV, after=80)

    m.section("REFERENCER")
    m.para(REFERENCES, after=80, justify=False)

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
                  title="Ansøgning og CV — vandingeniør, TÅRNBYFORSYNING A/S",
                  subject="Vandforsyning · anlægsprojekter · myndighed · benchmarking · drikkevandssikkerhed",
                  keywords=("vandingeniør, vandforsyning, drikkevand, anlægsprojekter, myndighed, "
                            "benchmarking, vandspild, dokumentation, tårnby forsyning, dansk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1 (krav → løsning), CV side 2-3, 90 dage side 4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_TaarnbyForsyning_Vandingenioer.docx")
    print("OK", build(out))
