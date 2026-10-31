# -*- coding: utf-8 -*-
"""
HOFOR — Specialiseret maskinmester til fjernvarme (store varmepumper).
Dansk JD. HOFOR beder kun om CV + motiveret afsnit — men den aftalte leverance
er ét dokument: motiveret side 1 (opgave-først) + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Specialiseret maskinmester | Fjernvarme & varmepumper | HOFOR"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv")

DATE = "31. oktober 2026"
RECIPIENT = ("HOFOR A/S · Fjernvarme, varmepumper · att. teamleder Rasmus Storgaard · "
             "tlf. 2795 2892")
SUBJECT = "Motivation og CV: Specialiseret maskinmester — fjernvarme og store varmepumper"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Opgaven er at gøre elektrificeringen af varmeproduktionen driftsikker. Store varmepumper skal "
    "bygges, sættes i drift og holdes i drift — og bygges sådan, at et driftsteam kan vedligeholde dem i "
    "tyve år. Derfor sidder specialisten to steder: i projekteringen som driftsperspektivet, og i "
    "driften som den, der kender anlægget, tallene og de fejl, der kommer igen.",

    "Nedenfor er min læsning af rollen og det system, der ligger klar: driftsmodel med forebyggende "
    "vedligehold, projektmodel med FAT/SAT og overdragelse, dataopsætning til optimering og en fast "
    "planlægningsrytme med driftsteknikerne.",
]

BULLETS = [
    ("Kravet: faglig specialist på store varmepumper og følge anlæggene gennem hele livscyklussen",
     "Løsningen er at behandle varmepumpen som en proces, ikke en komponent: kølemiddel, kompressor, "
     "vekslere, styring og elforsyning skal forstås sammen, og driftshensyn skal ind i designet, før "
     "anlægget findes. Min køletekniske baggrund (AMU, Mercantec) dækker den samme termodynamiske kreds "
     "som varmepumpen — samme proces, modsat retning — og elautorisationen (LV/MV/HV) dækker "
     "elforsyningen og styringen."),

    ("Kravet: delt rolle med arbejdsledelse for teamets driftsteknikere",
     "Løsningen er en fast planlægningsrytme: ugentligt planlægningsmøde med opgaver, prioritet og "
     "ansvarlig, en vedligeholdsplan pr. anlæg med intervaller og historik, og en tavle hvor dagens og "
     "ugens arbejde er synligt for alle. Arbejdsledelse er struktur og tydelighed — ikke mere møde."),

    ("Kravet: forebyggende vedligehold tænkes ind i driften",
     "Løsningen er at planlægge vedligehold ud fra anlæggets kritiske funktioner og driftstimer, ikke ud "
     "fra hvornår noget går i stykker: faste eftersyn, reservedele på de kritiske komponenter, "
     "målepunkter der overvåges, og en plan der tåler, at varmebehovet skifter med vejret."),

    ("Kravet: projektering, design, test, FAT/SAT, idriftsættelse og overdragelse af nye anlæg",
     "Løsningen er en driftspecialist-rolle i projektet: driftshensyn skrevet ind i kravsspecifikationen "
     "tidligt, FAT/SAT med testprotokoller og acceptkriterier, idriftsættelse med justering og "
     "målinger — og en overdragelse, hvor dokumentation, reservedelslister og driftsinstruktion "
     "overleveres, før projektet lukkes. Jeg har kørt FAT/SAT, IQ/OQ/PQ og aflevering med nul kritiske "
     "fund på 37 anlægsprojekter."),

    ("Kravet: analysere driftsdata og identificere optimeringsmuligheder",
     "Løsningen er et lille, fast sæt målepunkter og et månedligt gennemløb: COP, fremløb/retur, "
     "el-forbrug pr. produceret MWh, driftstimer og alarmhistorik — sammenlignet over tid og mod "
     "forventning. Optimering bliver dermed en række beslutninger med tal bag, ikke en mavefornemmelse."),

    ("Kravet: teknisk sparringspartner for teknikere, projektledere, rådgivere og leverandører",
     "Løsningen er at kunne tale alle fire sprog: teknikernes fejlsøgning, projektlederens fremdrift og "
     "økonomi, rådgiverens forudsætninger og leverandørens garantier. Jeg har siddet på alle fire sider "
     "af bordet — som udførende, som bygherre hos Novo Nordisk, som entreprenør med eget P&L og som "
     "driftsansvarlig på Lynetten."),
]

SYSTEM = ("Systemet er allerede bygget: vedligeholdsplan pr. anlæg med intervaller og historik, "
          "planlægningsrytme med driftsteknikerne, KPI-sæt til varmepumper (COP, el pr. MWh, driftstimer, "
          "alarmer), FAT/SAT- og overdragelsescheckliste samt alarm- og afvigelseslog med ejer og "
          "frist — i Excel, Power BI og SharePoint med Python og Claude til analyse og rapportering.")

MIRROR = ("Om kravene: uddannet maskinmester (B.Tech, EQF 6) og elautoriseret (LV/MV/HV) med "
          "køleteknisk AMU; 25 år med tekniske anlæg i drift — pumper, HVAC, køl, koblingsanlæg, "
          "højspænding og SCADA på 24/7-anlægget Lynetten med drifts- og vedligeholdelsesansvar og nul "
          "uplanlagte stop i fem år; og 37 anlægsprojekter hos Novo Nordisk med FAT/SAT og aflevering.")

HONEST = ("To ting skal siges ligeud: jeg har ikke haft fjernvarme og store varmepumper som anlægstype "
          "før — min erfaring er køl, HVAC, pumper, el og procesanlæg i drift og projektering, og "
          "varmepumpen er samme termodynamiske kreds som køleanlægget, bare med fjernvarmeintegration og "
          "en anden skala. Og jeg søger specialistrollen, ikke en lederrolle: arbejdsledelse har jeg "
          "prøvet i 14- og 12-mands teams, men her vil jeg i dybden med anlæggene.")

CULTURE = ("Hvorfor HOFOR: \"Hos os får du plads\" betyder i praksis, at fagligheden må fylde — et "
           "varmepumpeanlæg bliver kun driftssikkert, hvis nogen har plads til at gå i detaljen med "
           "målinger, alarmer og leverandørens dokumentation. Et team med en teamleder, tre maskinmestre "
           "og seks driftsteknikere fungerer på, at viden deles: driftsrutiner, hændelser og "
           "optimeringer skal skrives ned, så næste vagt kan bruge dem.")

PRACTICAL_CV = ("Bosat i Måløv — under 45 minutter til Rådhuspladsen, så rådighedsvagten kan dækkes; "
                "kørekort B (kategori B, personbil); dansk på modersmålsniveau og engelsk professionelt; "
                "kan sikkerhedsgodkendes til \"Fortroligt\" og opretholde godkendelsen gennem "
                "ansættelsen; tiltrædelse hurtigt, egen virksomhed afvikles ved ansættelse.")

PRACTICAL = ("Praktisk: bosat i Måløv — under 45 minutter til Rådhuspladsen, så rådighedsvagten kan "
             "dækkes; kørekort B; dansk på modersmålsniveau og engelsk professionelt; kan "
             "sikkerhedsgodkendes til \"Fortroligt\" og opretholde godkendelsen gennem ansættelsen. "
             "Tiltrædelse hurtigt, egen virksomhed afvikles ved ansættelse.")

CLOSING = ("Jeg vil gerne høre, hvor varmepumpeanlæggene står i dag, og bruge første samtale på tre "
           "spørgsmål: hvilke anlæg der er i drift og på vej, hvordan vedligeholdet styres nu, og hvad "
           "der skal være på plads ved næste overdragelse fra projekt til drift.")

# ------------------------------------------------------------------ CV
PROFILE = ("Rollen kræver fire ting på én gang: at kunne et anlæg i dybden, at lede arbejdet for et "
           "driftsteam, at tænke vedligehold ind i driften og at repræsentere driften i projekteringen. "
           "Alle fire har været hverdag i 25 år: drifts- og vedligeholdelsesansvar på Lynetten (24/7, "
           "pumper, HVAC, koblingsanlæg, højspænding, SCADA), 37 anlægsprojekter hos Novo Nordisk med "
           "FAT/SAT og idriftsættelse, egen virksomhed med 40+ serviceanlæg og fuldt P&L samt "
           "køleteknisk AMU. Elautoriseret maskinmester (LV/MV/HV), B.Tech i Technology Management.")

PRACTICE = [
    ("Drift og anlægsforståelse",
     "Pumper, HVAC, køl, varmevekslere, koblingsanlæg, højspænding og SCADA; fejlfinding på "
     "komponentniveau og forståelse for, hvordan anlæggets dele påvirker hinanden og totaløkonomien."),

    ("Forebyggende vedligehold",
     "Vedligeholdsplan pr. anlæg med intervaller, historik og kritiske reservedele; PDCA-baseret "
     "årshjul, A3-root-cause på nedetid, KPI'er i SAP og nul uplanlagte stop i fem år på Lynetten."),

    ("Arbejdsledelse af teknikere",
     "Daglig og ugentlig planlægning, opgavefordeling og prioritering, kompetencematrix, "
     "sikkerhed og arbejdstilladelser — praktiseret med 14- og 12-mands tekniske teams."),

    ("Projektering, idriftsættelse og sparring",
     "Driftskrav ind i designfasen, FAT/SAT med acceptkriterier, idriftsættelse med justering og "
     "målinger, overdragelse med dokumentation — plus sparring med teknikere, projektledere, rådgivere "
     "og leverandører."),

    ("Driftsdata og optimering",
     "COP, el-forbrug pr. produceret MWh, fremløb/retur, driftstimer og alarmhistorik; målepunkter, "
     "baseline og månedlig gennemgang — optimering som beslutninger med tal bag."),

    ("El, styring og sikkerhed",
     "Elautorisation LV/MV/HV, tavler og styring, DS/HD 60364, LOTO og arbejdstilladelser, APV og "
     "risikovurdering, nærved-hændelser — myndighedskrav og dokumentation i GMP-/forsyningsmiljøer."),
]

FIRST90 = [
    ("Uge 1–2",
     "Alle anlæg gennemgået fysisk med den nærmeste kollega; driftshistorik, alarmer, vedligeholdsplan "
     "og dokumentation læst igennem; mødt alle tre maskinmestre og seks driftsteknikere."),
    ("Uge 3–6",
     "Planlægningsrytme og ugentligt planlægningsmøde aftalt; vedligeholdsplan pr. anlæg opdateret med "
     "intervaller og kritiske reservedele; målepunkter og KPI-sæt besluttet med teamet."),
    ("Uge 7–12",
     "Første måneds analyse af COP, el pr. MWh og alarmer fremlagt for teamet; konkrete "
     "optimeringsforslag med tal; driftskrav formuleret til det næste anlæg i projektering."),
    ("Måned 3–6",
     "Forebyggende vedligehold kørende efter plan uden brandslukning; FAT/SAT- og "
     "overdragelsescheckliste taget i brug på nye anlæg; reservedels- og leverandøraftaler gennemgået."),
    ("Måned 6–12",
     "Anlæggene kører med kendt baseline, dokumenteret forbedring i COP/driftsøkonomi og en "
     "vedligeholdsplan, der holder — også når varmebehovet skifter. Løbende: månedlig driftsgennemgang, "
     "kvartalsvis leverandør- og garantigennemgang og en fast post for, hvad der forenkles næste måned."),
]

MODELS = [
    ("Anlæg og proces",
     "Varmepumpe-/kølekreds (kompressor, vekslere, kølemiddel), pumper, HVAC, varmevekslere, "
     "koblingsanlæg, fjernkølingscentraler som sparring"),
    ("Vedligehold og leverandører",
     "Forebyggende vedligeholdsplan pr. anlæg, intervaller og historik, kritiske reservedele, "
     "serviceaftaler med responstid, garantisager, PDCA-årshjul, A3-root-cause"),
    ("Arbejdsledelse",
     "Ugentligt planlægningsmøde, opgavefordeling og prioritering, tavlemøde, kompetencematrix, "
     "arbejdstilladelser og sikkerhed"),
    ("Projektering og leverance",
     "Driftskrav i design, FAT/SAT med acceptkriterier, idriftsættelse og justering, "
     "overdragelsescheckliste, dokumentation og driftsinstruktion"),
    ("Driftsdata og værktøj",
     "COP og el pr. MWh, driftstimer, fremløb/retur, alarmhistorik, baseline og månedlig "
     "optimeringsgennemgang; Power BI, SAP/CMMS, SharePoint, Python og Claude til analyse"),
    ("El og sikkerhed",
     "LV/MV/HV, tavler og styring, LOTO og arbejdstilladelser, APV og risikovurdering, DS/HD 60364"),
]

ACHIEVEMENTS = [
    ("Nul uplanlagte stop i fem år",
     "på 24/7-anlægget Lynetten — forebyggende vedligehold, PDCA og A3-root-cause på nedetid."),
    ("37 samtidige anlægsprojekter, 2–10 mio. kr.",
     "FAT/SAT, IQ/OQ/PQ, idriftsættelse og aflevering hos Novo Nordisk — nul kritiske fund."),
    ("−40 % energikost",
     "gennem måling, PDCA og standardiseret arbejde på tekniske anlæg — forbedringer, der blev i "
     "driften."),
    ("40+ serviceanlæg, 5 elektrikere og +40 % produktivitet",
     "daglig drift, fejlfinding og vedligehold i egen virksomhed med fuldt P&L- og personalearsvar; "
     "effektiviteten løftet via dataunderstøttet planlægning, standardarbejde og egen AI-tooling."),
]

EXPERIENCE = [
    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · drifts- og "
     "vedligeholdelsesbudgetter i SAP",
     [("Vedligehold og KPI",
       "PDCA-baseret vedligeholdsplan med fast årshjul, A3-root-cause på større nedetid og KPI'er i "
       "SAP ERP; nul uplanlagte stop i fem år."),
      ("Drift, fejlfinding og sikkerhed",
       "fejlfinding og reparation på pumper, HVAC, koblingsanlæg og højspænding; LOTO, arbejdstilladelser, "
       "nærved-hændelser."),
      ("Leverandører og entreprenører",
       "koordinering af egne teknikere, entreprenører og leverandører — adgang, sikkerhed og "
       "garantisager.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister inden for teknik, indkøb og drift · "
     "GMP/FDA/EMA",
     [("Idriftsættelse og aflevering",
       "FAT/SAT, IQ/OQ/PQ og valideringsdokumentation med afvigelseshåndtering — nul kritiske fund."),
      ("Driftsperspektiv i projektering",
       "drifts- og vedligeholdelseshensyn indarbejdet i design og kravsspecifikation, før anlægget blev "
       "bestilt; 25 specialister koordineret og −40 % energikost gennem PDCA.")]),

    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder og leverandører",
     [("Service, drift og arbejdsledelse",
       "planlagt og afhjælpende vedligehold på el, tavler, styring, ventilation, klima og køleanlæg; "
       "daglig ledelse af 5 elektrikere og 3 lærlinge med kompetencematrix og sikkerhed."),
      ("Økonomi og leverandører",
       "budget, indkøb, leverandøraftaler og prissammenligning med fuldt ansvar for bundlinjen.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Kapacitet, kvalitet og planlægning",
       "14-personers produktions- og montageteam med kapacitetsplanlægning, flowstyring, daglige "
       "tavlemøder og dokumentation ved montage i aktive bygninger.")]),

    ("Elektromekaniker / Produktionsteamleder",
     "ARJ Engineering · Teheran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · skiftplanlægning, materialestyring og lager",
     [("Produktionsteam og teknisk problemløsning",
       "skiftplanlægning, materialestyring og målopfølgning med situationel coaching; reparation og "
       "diagnosticering af elektriske og mekaniske systemer gennem struktureret root cause-analyse.")]),
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
    ("Køleteknik & klimaanlæg (AMU) — samme termodynamiske kreds som varmepumper",
     "Mercantec · mar. 2021"),
    ("Arbejdsmiljø §16 og sikkerhedsbevidsthed (VI/6-1)",
     "Søfartsstyrelsen · maj 2021"),
    ("Lean — værdistrømsanalyse, standardarbejde, 5S, A3 og Kaizen",
     "Anvendt i drift · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og projekter · 2017 – nu"),
]

# STCW bevidst udeladt: ikke relevant for fjernvarme/varmepumper

LANGUAGES = "Dansk (modersmål) · Engelsk (professionelt, skriftligt og mundtligt) · Persisk/farsi · Kørekort B (kategori B, personbil)"

REFERENCES = "Tidligere ledere og kolleger hos Biofos (Lynetten), Novo Nordisk A/S (Kalundborg) og egne kunder i ELOHVAC — oplyses ved henvendelse."

KEYWORDS = (
    "Specialiseret maskinmester · Maskinmester · Ingeniør · Fjernvarme · Varmepumper · "
    "Varmeproduktion · Fjernvarmeforsyning · Fjernkølingscentraler · Drift · Vedligehold · "
    "Forebyggende vedligeholdelse · Driftsoptimering · Driftsdata · Analyse · COP · Driftsteknikere · "
    "Arbejdsledelse · Planlægning · Koordinering · Planlægningsmøder · Sparringspartner · Rådgivere · "
    "Leverandører · Projektering · Design · Test · FAT · SAT · Idriftsættelse · Overdragelse · "
    "Fejlfinding · Teknisk dokumentation · Køleanlæg · Køleteknik · HVAC · Pumper · Varmevekslere · "
    "Styring · SCADA · El · Højspænding · Elautoriseret · LV/MV/HV · SAP · CMMS · Power BI · KPI · "
    "Arbejdsmiljø · Sikkerhed · Rådighedsvagt · Sikkerhedsgodkendelse · Fortroligt · Kørekort B · Dansk"
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
        m.para(t, after=55)

    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "SPECIALISTPROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("DRIFTS- OG VEDLIGEHOLDSMETODER — ANVENDT I PRAKSIS",
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

    # 90-dagesplanen som afsluttende side, så tabellen ikke deles over to sider
    m.page_break()
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER ANLÆGGENE I RYTMEN",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("PRAKTISK OM ANSÆTTELSEN")
    m.para(PRACTICAL_CV, after=80)

    m.section("REFERENCER")
    m.para(REFERENCES, after=80, justify=False)

    # 90-dages-tabellen må ikke deles over to sider (header skal følge rækkerne)
    _t = m.doc.tables[-1]
    for _row in _t.rows[:-1]:
        for _c in _row.cells:
            for _p in _c.paragraphs:
                _p.paragraph_format.keep_with_next = True

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
                  title="CV og motivation — Specialiseret maskinmester, HOFOR fjernvarme",
                  subject="Store varmepumper · drift, vedligehold, projektering og idriftsættelse",
                  keywords=("specialiseret maskinmester, maskinmester, fjernvarme, varmepumper, "
                            "drift, vedligehold, optimering, FAT, SAT, idriftsættelse, hofor, dansk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Motiveret side 1 (krav → løsning), CV side 2-4. HOFOR beder kun om CV — "
                           "dokumentet leveres som aftalt: ét samlet dokument.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_HOFOR_SpecialiseretMaskinmester_Varmepumper.docx")
    print("OK", build(out))
