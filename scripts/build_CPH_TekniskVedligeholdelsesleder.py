# -*- coding: utf-8 -*-
"""
Københavns Lufthavne (CPH) — Teknisk vedligeholdelsesleder,
Mechanical Installation Services / Commercial Maintenance Services.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Teknisk vedligeholdelsesleder | Mechanical Installation Services | CPH"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv")

DATE = "31. oktober 2026"
RECIPIENT = ("Københavns Lufthavne A/S · Airport Infrastructure & Services / Commercial Maintenance "
             "Services · att. Senior Manager Claus Kock Christiansen · claus.christiansen@cph.dk")
SUBJECT = "Ansøgning: Teknisk vedligeholdelsesleder — Mechanical Installation Services"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Opgaven er at holde tretten teknikere i arbejde på en lufthavn, der ikke må stå stille. "
    "Mechanical Installation Services dækker kritiske installationer i de kommercielle områder — og når "
    "en elevator, en rulletrappe eller et rullefortov står, er det ikke en teknisk sag, men en "
    "passageroplevelse og en driftsforstyrrelse. Det er den slags opgave, der bliver løst af "
    "planlægning, kompetence og et team, der ved, hvad der skal ske først.",

    "Nedenfor er min læsning af rollen og det system, der ligger klar: vedligeholdsplan pr. anlægstype "
    "med kritiske reservedele, prioriteringsmodel for opgaver i drift, ISO9001-styring med revision og "
    "afvigelser, kompetencematrix for de 13 teknikere og fast møderytme med de interne kunder.",
]

BULLETS = [
    ("Kravet: stå for og udvikle et team af 13 teknikere",
     "Løsningen er ledelse med faste rammer: 1:1 hver fjerde uge, ugentligt tavlemøde hvor ugen "
     "planlægges og sidste uges tal gennemgås, kompetencematrix og udviklingsplaner, der bliver fulgt op. "
     "Tretten teknikere med forskellige faglige baggrunde har brug for retning og en leder, der er synlig."),

    ("Kravet: planlægning, koordinering og prioritering af teamets opgaver",
     "Løsningen er én samlet kapacitets- og opgaveplan otte uger frem: planlagt forebyggende "
     "vedligehold, eftersyn med frister, akutte sager og projekter — prioriteret efter anlæggets "
     "kritikalitet og efter, hvad lufthavnens drift kan tåle at undvære. Prioritering er en model, ikke et "
     "skøn om morgenen."),

    ("Kravet: faglig sparring, nærværende ledelse, kompetenceudvikling og trivsel",
     "Løsningen er planlagt synlighed: gemba-rundering efter fast rytme, fejlfinding sammen med "
     "teknikerne og svære sager gennemgået frem for bare lukket — plus kompetence- og "
     "autorisationsmatrix med udløbsdatoer, MUS/GRUS med opfølgning og et lærlinge- og talentløft, så "
     "viden ikke kun sidder hos de erfarne."),

    ("Kravet: gode relationer til interne kunder og eksterne samarbejdspartnere",
     "Løsningen er én indgang med aftalte svartider, en fast mødekadence med de interne kunder om "
     "status, åbne sager og næste større arbejde, og leverandøraftaler med responstid og "
     "garantihåndtering. Service bliver målt — ikke antaget."),

    ("Kravet: stabil drift og vedligeholdelse af tekniske installationer i de kommercielle områder",
     "Løsningen er forebyggende vedligehold planlagt efter anlæggets kritiske funktioner og driftstimer, "
     "kritiske reservedele på lager, en alarm- og afvigelseslog med ejer og frist og en fejlhistorik, der "
     "bruges til at rette årsagen frem for symptomet."),

    ("Kravet: ansvar for ISO9001-kvalitetsledelsessystemet for elevator, rulletrapper, rullefortorve og lignende",
     "Løsningen er et system, der bruges dagligt og kan tåle et audit: dokumentstyring med version og "
     "ejer, procedurer der matcher arbejdet på gulvet, intern audit-plan, afvigelser med root cause og "
     "ledelsens gennemgang med målbare mål — kvalitet er dokumentation, der passer med virkeligheden."),

    ("Kravet: bidrage til den strategiske udvikling af Commercial Maintenance Services",
     "Løsningen er at omsætte driftstal til beslutninger: MTBF/MTTR pr. anlægstype, andel "
     "forebyggende vs. afhjælpende arbejde, responstider, gennemførte eftersyn og dækningsgrad på "
     "teamets kapacitet — lagt frem med en anbefaling, ikke bare et regneark."),
]

SYSTEM = ("Systemet er allerede bygget: vedligeholdsplan pr. anlægstype, kapacitets- og opgaveplan otte "
          "uger frem, prioriteringsmodel efter kritikalitet, kompetence- og autorisationsmatrix, "
          "ISO9001-dokumentstyring med intern audit og afvigelseslog samt KPI-tavle med MTBF/MTTR og "
          "responstider — i Excel, Power BI og SharePoint med Python og Claude til rapportering.")

MIRROR = ("Om kravene: ledelse af vedligeholds- og teknikteams i 20 år — 14- og 12-mands tekniske teams, "
          "5 elektrikere og 3 lærlinge med fuldt P&L og drifts- og vedligeholdelsesansvar på "
          "24/7-anlægget Lynetten med nul uplanlagte stop i fem år; kvalitetsledelse og myndighedskrav fra "
          "GMP/FDA/EMA og forsyningsmiljøer; elautoriseret maskinmester (LV/MV/HV).")

HONEST = ("To ting skal siges ligeud: elevatorer, rulletrapper og rullefortove har jeg ikke arbejdet med "
          "som anlægstype før, og ISO9001 har jeg arbejdet under — ikke været systemejer for. Det er de to "
          "ting, jeg vil bruge de første uger på at lære i dybden sammen med teamet og "
          "kvalitetsafdelingen; metoden bag anlæg og kvalitetssystem er den samme som på 24/7-anlæg og i "
          "GMP-miljøer.")

CULTURE = ("Hvorfor CPH: i en 24/7-organisation bliver drift kun stabil, hvis nogen har styr på planen, "
           "reservedelene og kompetencerne, før noget går i stykker. Kulturen I beskriver — hjælpsomhed, "
           "humor og engagement — er ikke et modsætningsforhold til struktur; det er det, der gør, at "
           "tretten teknikere deler viden i stedet for at holde den for sig selv.")

PRACTICAL = ("Praktisk: bosat i Måløv, cirka 30 minutter fra Kastrup; kørekort B og ren straffeattest; "
             "kan blive politigodkendt og holde godkendelsen; dansk på modersmålsniveau; klar til hurtigt "
             "start. Egen virksomhed afvikles ved ansættelse.")

CLOSING = ("Jeg vil gerne høre, hvordan teamet arbejder i dag, og bruge første samtale på to spørgsmål: "
           "hvordan opgaver prioriteres mellem planlagt vedligehold og akutte sager, og hvordan "
           "ISO9001-systemet bruges i hverdagen.")

# ------------------------------------------------------------------ CV
PROFILE = ("Rollen kræver fire ting på én gang: at lede et teknisk team, at prioritere i en kompleks "
           "driftsorganisation, at holde et kvalitetsledelsessystem i live og at levere stabil drift til "
           "interne kunder. Alle fire har været hverdag i 20 år: drifts- og vedligeholdelsesansvar på "
           "24/7-anlægget Lynetten med nul uplanlagte stop i fem år, 14- og 12-mands tekniske teams, 5 "
           "elektrikere og 3 lærlinge med fuldt P&L og 37 anlægsprojekter hos Novo Nordisk under GMP-krav. "
           "Elautoriseret maskinmester (LV/MV/HV), B.Tech i Technology Management & Mechanical "
           "Engineering.")

PRACTICE = [
    ("Ledelse af teknikteams",
     "1:1-hjul, ugentligt tavlemøde, kompetence- og autorisationsmatrix, udviklingsplaner, MUS/GRUS, "
     "situationsbestemt ledelse (SLII) og synlig ledelse i driften."),
    ("Vedligehold og drift",
     "Forebyggende vedligeholdsplan med intervaller og historik, kritiske reservedele, "
     "tilstandskontrol, fejlhistorik og A3-root-cause; PDCA-årshjul og KPI'er i SAP."),
    ("Planlægning og prioritering",
     "Kapacitets- og opgaveplan otte uger frem, prioriteringsmodel efter kritikalitet, håndtering af "
     "akutte sager uden at planlagt arbejde falder bagud."),
    ("ISO9001 og kvalitetsstyring",
     "Dokumentstyring med version og ejer, procedurer der matcher praksis, intern audit-plan, "
     "afvigelser med root cause og opfølgning, ledelsens gennemgang og målbare mål."),
    ("Interne kunder og leverandører",
     "Én indgang med aftalte svartider, mødekadence om status og åbne sager, leverandøraftaler med "
     "responstid, garantisager og prissammenligning."),
    ("Teknisk tyngde",
     "Mekaniske og elektriske installationer, tavler og styring, pumper og HVAC, SCADA og overvågning; "
     "elautorisation LV/MV/HV med egenkontrol og dokumentation."),
    ("Arbejdsmiljø og sikkerhed",
     "APV og risikovurdering, LOTO, arbejdstilladelser og adgang, sikkerhedsrundering, "
     "nærved-hændelser og toolbox-møder i en organisation med skarpe sikkerhedskrav."),
]

PARTNER = [
    ("De 13 teknikere",
     "Kompetencematrix og autorisationer ajour, planlagt arbejde der ikke forsvinder i akutte sager, og "
     "en leder der er til at få fat i. Teknikere bliver ikke i en afdeling, hvor de kun hører om "
     "problemer."),
    ("De interne kunder i de kommercielle områder",
     "Én indgang med aftalte svartider, fast mødekadence om status og åbne sager, og en prioritering der "
     "er forklaret — så de ved, hvornår deres anlæg er på programmet, og hvorfor."),
    ("Leverandører og kvalitetsafdelingen",
     "Serviceaftaler med responstid og garantihåndtering; ISO9001-arbejdet kørt som en plan med audit, "
     "afvigelser og opfølgning — kvalitetssystemet skal matche det arbejde, der faktisk bliver udført."),
]

FIRST90 = [
    ("Uge 1–2",
     "Alle tretten teknikere mødt — på værkstedet og ude på anlæggene; porteføljen, ISO9001-systemet, "
     "de åbne sager og de nuværende KPI'er gennemgået, før noget ændres. Mødt de interne kunder og "
     "kvalitetsafdelingen."),
    ("Uge 3–6",
     "Kapacitets- og opgaveplan otte uger frem lagt; prioriteringsmodel for opgaver aftalt med teamet; "
     "kompetence- og autorisationsmatrix opdateret; 1:1-kalender og ugentligt tavlemøde i gang."),
    ("Uge 7–12",
     "KPI-baseline for MTBF/MTTR, responstider og andel forebyggende arbejde lagt frem for CMS-ledelsen; "
     "ISO9001-gennemgang kørt med afvigelser, ejer og frist; kritiske reservedele og leverandøraftaler "
     "gennemgået."),
    ("Måned 3–6",
     "Forebyggende vedligehold kørende efter plan uden at akutte sager skubber det; eftersyn og "
     "dokumentation ajour; kompetenceudviklingsplaner for alle tretten gennemført og fulgt op."),
    ("Måned 6–12",
     "Teamet leverer stabil drift med faldende akutte sager og dokumenteret højere andel planlagt "
     "arbejde; ISO9001-systemet består audit uden større afvigelser; teamet løfter større "
     "eftersynsarbejde ved siden af driften. Løbende: månedlig drifts- og kvalitetsgennemgang og en fast "
     "post for, hvad der skal forenkles næste måned."),
]

MODELS = [
    ("Ledelse",
     "1:1-hjul, tavlemøde, MUS/GRUS, kompetencematrix, situationsbestemt ledelse (SLII), "
     "GROW-coaching og delegeringstrappe"),
    ("Vedligehold",
     "Forebyggende plan pr. anlægstype, intervaller og historik, kritiske reservedele, "
     "tilstandskontrol, fejlhistorik, PDCA og A3-root-cause"),
    ("Prioritering",
     "Kritikalitetsmodel for anlæg, kapacitetsplan otte uger frem, akut-escaleringstrappe og "
     "kontrol af, at planlagt arbejde ikke forsvinder i driften"),
    ("ISO9001 og kvalitet",
     "Dokumentstyring med version og ejer, procesbeskrivelser, intern audit-plan, afvigelser med "
     "root cause, ledelsens gennemgang og målbare kvalitetsmål"),
    ("KPI og rapportering",
     "MTBF/MTTR, responstid, andel forebyggende vs. afhjælpende, eftersyn til tiden, "
     "teamudnyttelse; Power BI-tavler og SAP/CMMS"),
    ("Kunder og leverandører",
     "Én indgang og svartider, mødekadence med interne kunder, leverandøraftaler med responstid, "
     "garantisager og prissammenligning"),
    ("Sikkerhed",
     "APV og risikovurdering, LOTO, arbejdstilladelser og adgang, sikkerhedsrundering, "
     "nærved-hændelser og toolbox-møder"),
]

ACHIEVEMENTS = [
    ("Nul uplanlagte stop i fem år",
     "på 24/7-forsyningsanlægget Lynetten — forebyggende vedligehold, PDCA og A3-root-cause på nedetid."),
    ("14- og 12-mands tekniske teams ledet",
     "kapacitetsplanlægning, prioritering og daglige tavlemøder i drift og montage."),
    ("5 elektrikere og 3 lærlinge med fuldt P&L",
     "daglig ledelse, kompetenceudvikling og udviklingssamtaler i egen autoriseret virksomhed."),
    ("Nul kritiske afvigelser ved aflevering",
     "37 samtidige anlægsprojekter hos Novo Nordisk under GMP/FDA/EMA-krav — dokumentation og "
     "aflevering uden fund."),
    ("−40 % energikost og +40 % produktivitet",
     "dokumenterede forbedringer via måling, standardarbejde, dataunderstøttet planlægning og egen "
     "AI-tooling."),
]

EXPERIENCE = [
    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · budgetter i SAP",
     [("Vedligehold og KPI",
       "PDCA-baseret vedligeholdsplan med fast årshjul, A3-root-cause på større nedetid og KPI'er i "
       "SAP; nul uplanlagte stop i fem år."),
      ("Prioritering i drift",
       "fejlfinding og reparation på pumper, HVAC, koblingsanlæg og højspænding; prioritering mellem "
       "anlæg, når flere ting stod på én gang."),
      ("Leverandører og sikkerhed",
       "koordinering af egne teknikere, entreprenører og leverandører — LOTO, arbejdstilladelser, "
       "garantisager og nærved-hændelser.")]),

    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og leverandøraftaler",
     [("Personale og driftsplan",
       "daglig ledelse af 5 elektrikere og 3 lærlinge, opgavefordeling, kompetencematrix og "
       "udviklingssamtaler."),
      ("Kunder og økonomi",
       "serviceaftaler og akutte sager med erhvervskunder, Plan og prognose, indkøb og "
       "leverandøraftaler med fuldt ansvar for bundlinjen.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister · GMP/FDA/EMA",
     [("Kvalitet og dokumentation",
       "FAT/SAT, IQ/OQ/PQ og valideringsdokumentation med afvigelseshåndtering — nul kritiske fund; "
       "arbejde under myndighedskrav og revision."),
      ("Projekt og koordinering",
       "plan, økonomi og rapportering; 25 specialister koordineret på tværs af mekanik, el, proces og "
       "indkøb.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Team og fremdrift",
       "14-personers team med kapacitetsplanlægning, flowstyring og daglige tavlemøder over 11 "
       "samtidige entrepriser.")]),

    ("Elektromekaniker / Produktionsteamleder",
     "ARJ Engineering · Teheran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · skiftplanlægning, materialestyring og lager",
     [("Produktionsteam og teknisk problemløsning",
       "skiftplanlægning, materialestyring og målopfølgning; reparation og diagnosticering af "
       "elektriske og mekaniske systemer gennem struktureret root cause-analyse.")]),
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
    ("Køleteknik & klimaanlæg (AMU)",
     "Mercantec · mar. 2021"),
    ("Arbejdsmiljø §16 og sikkerhedsbevidsthed (VI/6-1)",
     "Søfartsstyrelsen · maj 2021"),
    ("Lean — værdistrømsanalyse, standardarbejde, 5S, A3 og Kaizen",
     "Anvendt i drift · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og projekter · 2017 – nu"),
]

LANGUAGES = "Dansk (modersmål, skrift og tale) · Engelsk (professionelt) · Persisk/farsi · Kørekort B (kategori B)"

PRACTICAL_CV = ("Bosat i Måløv — cirka 30 minutter fra Kastrup; kørekort kategori B og ren straffeattest; "
                "kan politigodkendes og opretholde godkendelsen gennem ansættelsen; dansk på "
                "modersmålsniveau; klar til hurtigt start, og egen virksomhed afvikles ved ansættelse.")

REFERENCES = "Tidligere ledere og samarbejdspartnere hos Biofos (Lynetten), Novo Nordisk A/S (Kalundborg) og egne kunder i ELOHVAC — oplyses ved henvendelse."

KEYWORDS = (
    "Teknisk vedligeholdelsesleder · Teknisk Leder · Mechanical Installation Services · Commercial "
    "Maintenance Services · Airport Infrastructure & Services · Vedligehold · Drift · Teknikteam · "
    "13 teknikere · Planlægning · Koordinering · Prioritering · Faglig sparring · Nærværende ledelse · "
    "Kompetenceudvikling · Trivsel · Interne kunder · Eksterne samarbejdspartnere · Strategisk udvikling · "
    "Stabil drift · Tekniske installationer · Anlæg · ISO9001 · Kvalitetsledelsessystem · Elevator · "
    "Rulletrapper · Rullefortorve · Eftersyn · Forebyggende vedligehold · Fejlfinding · Reservedele · "
    "Leverandører · Arbejdsmiljø · Sikkerhed · APV · LOTO · KPI · MTBF · MTTR · Responstid · SAP · "
    "CMMS · Power BI · Kørekort · Straffeattest · Politigodkendelse · Dansk · Måløv"
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

    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "LEDELSESPROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("VEDLIGEHOLDS- OG LEDELSESMETODER — ANVENDT I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER TEAMET I RYTMEN",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN LEDES TEAMET — DE TRE PARTER")
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
                  title="Ansøgning og CV — Teknisk vedligeholdelsesleder, CPH",
                  subject="Mechanical Installation Services · 13 teknikere · ISO9001 · stabil drift",
                  keywords=("teknisk vedligeholdelsesleder, mechanical installation services, cph, "
                            "iso9001, vedligehold, drift, teknikteam, elevator, rulletrapper, dansk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1 (krav → løsning), CV side 2-3, 90 dage side 4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_CPH_TekniskVedligeholdelsesleder.docx")
    print("OK", build(out))
