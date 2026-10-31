# -*- coding: utf-8 -*-
"""
KAB / Frederiksberg Forenede Boligselskaber (FFB) — Driftschef til ejendomsdrift,
Servicecenter Syd, Roskildevej 65, Frederiksberg.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Driftschef | Ejendomsdrift og servicecenter | Frederiksberg"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = ("KAB / FFB · Servicecenter Syd, Roskildevej 65, 2000 Frederiksberg · "
             "att. kundechef Sofie La Cour Mosegaard")
SUBJECT = "Ansøgning: Driftschef til ejendomsdrift på Frederiksberg"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Opgaven er at få 1.100 boliger i FFB Syd til at fungere for de mennesker, der bor i dem — "
    "hver dag, hele året — med 15 medarbejdere i Servicecenter Syd og to driftschefkolleger i "
    "samme organisation. Drift måles på noget andet end ordrer: om varmen virker, om opgangen er "
    "i orden, om en henvendelse bliver besvaret.",

    "Nedenfor er min læsning af rollen og det system, der står klar fra første dag: driftsplan "
    "pr. boligafdeling med tilstand, indsats og ansvarlig, opgavestrøm med svartider, "
    "vedligeholdelses- og investeringsplan med levetid, fast kadence for afdelingsbestyrelserne "
    "og en ledelsesrytme for de 15 medarbejdere — understøttet af data, ikke mavefornemmelser.",
]

BULLETS = [
    ("Kravet: lede, motivere og udvikle 15 medarbejdere i Servicecenter Syd",
     "Løsningen er en ledelsesrytme, der ikke afhænger af, hvor travlt der er: 1:1 hver fjerde "
     "uge, MUS med opfølgning, ugentligt tavlemøde med prioriteter og sikkerhed og "
     "kompetenceplan pr. medarbejder. Jeg har ledet 5-, 12- og 14-mands teams og 25 specialister "
     "— servicefolk flytter sig først, når rammerne er faste."),

    ("Kravet: sikre en effektiv og veldrevet daglig drift af ejendommene",
     "Løsningen er at gøre driften målbar: tilsyn med fast kadence og dokumentation, fejlhistorik "
     "pr. ejendom, akut/planlagt-fordeling og KPI'er for svartid, gennemført vedligehold og "
     "gentagne fejl. Jeg har drevet 24/7-anlæg med nul uplanlagte stop i fem år — samme "
     "disciplin, mindre skala."),

    ("Kravet: samarbejde med afdelingsbestyrelser om drift, vedligeholdelse samt bygge- og "
     "udviklingsprojekter",
     "Løsningen er fast mødekadence pr. afdeling med kort, ensartet dagsorden — status, kommende "
     "opgaver, økonomi og beslutninger — og referat med ansvarlig og frist, så næste møde starter "
     "med det, der blev lovet. I 20 år har jeg forklaret prioriteringer til kunder og myndigheder."),

    ("Kravet: rådgive afdelingsbestyrelserne om løsninger, der understøtter både beboernes behov "
     "og afdelingernes udvikling",
     "Løsningen er to alternativer i stedet for ét: hvad koster det nu, hvad koster det om fem "
     "år, og hvad betyder det for beboerne i mellemtiden — med levetid og driftsomkostning regnet "
     "med. Beslutningsgrundlag, ikke anbefalinger i luften."),

    ("Kravet: bidrage til planlægning og opfølgning på vedligeholdelsesopgaver og investeringer",
     "Løsningen er vedligeholdelsesplan pr. ejendom med tilstandsvurdering, prioritering efter "
     "risiko og økonomi og et budget, der følges månedligt med prognose. Jeg har styret 37 "
     "anlægsprojekter på 2–10 mio. kr. med budget og afvigelser — en investering er først god, når "
     "driften bagefter er billigere."),

    ("Kravet: udvikle en moderne drift, hvor data og teknologi understøtter hverdagen",
     "Løsningen er at tage data i brug der, hvor de sparer tid: opgaver og henvendelser i ét "
     "system, dashboards for svartid, gentagne fejl, energi og vedligeholdelsesstatus og "
     "rapporter, der genereres automatisk. Jeg arbejder dagligt med SAP/CMMS, Excel og Power BI — "
     "og bygger selv rapportering med Python og Claude."),

    ("Kravet: tæt samarbejde med driftschefkollegerne i FFB og specialisterne i KAB-Fællesskabet",
     "Løsningen er at bruge fællesskabet bevidst: ensartede processer og målinger på tværs af de "
     "tre servicecentre, faste fagmøder med KAB's specialister og egne beslutninger inden for "
     "aftalte rammer — så specialisterne bliver løftestang, ikke flaskehals."),
]

SYSTEM = ("Systemet er allerede bygget: driftsplan pr. boligafdeling med tilstand og næste indsats, "
          "opgavestrøm med svartider og ansvarlig, vedligeholdelses- og investeringsplan med "
          "levetid og prioritering, referatstandard for afdelingsbestyrelsesmøder, månedlig "
          "økonomiopfølgning med prognose og et KPI-board for drift, svartid og energi — i "
          "SAP/CMMS, Excel og Power BI, med rapportering i Python og Claude.")

MIRROR = ("Om kravene: 20 år med drift, vedligeholdelse og ledelse — 15-, 14-, 12- og 5-mands "
          "teams, 24/7-anlæg med nul uplanlagte stop i fem år, 40+ serviceanlæg med fuldt P&L, 37 "
          "anlægsprojekter (2–10 mio. kr.) uden kritiske fund, −40 % energikost og +40 % "
          "produktivitet. Elautoriseret maskinmester (LV/MV/HV), B.Tech i Technology Management & "
          "Mechanical Engineering — og bygningsdelen fra ventilation, CTS/BMS, varme og el.")

HONEST = ("Tre ting skal siges ligeud: jeg har ikke arbejdet i en almen boligorganisation eller med "
          "beboerdemokrati før, så afdelingsbestyrelsernes rolle og de politiske processer skal "
          "læres ordentligt i starten. Min ledelseserfaring er teknisk drift og service, ikke "
          "ejendomsadministration med husleje og udlejning. Og mine tal er fra forsyning, pharma "
          "og service — ikke fra boligdrift. Til gengæld har jeg prøvet det svære her: at drive "
          "noget, der ikke må gå ned, og at svare en myndighed eller en bestyrelse klart på, hvad "
          "der bliver gjort og hvornår.")

CULTURE = ("Hvorfor FFB og KAB: I er Frederiksbergs største almene boligorganisation, og I skriver "
           "selv, at trivsel, fællesskab, lederskab og kollegaskab er noget, vi har til fælles. "
           "KAB's værdier — ansvarlighed, gennemskuelighed, fornyelse og dialog — betyder kun "
           "noget, hvis de kan ses i en opgang og i et referat. Med strategien Fælles Værdi og det "
           "digitale program er der et sted at gå hen med de data, der skal gøre driften billigere.")

PRACTICAL = ("Praktisk: bosat i Måløv, 20 minutter til Roskildevej 65; kørekort B og bil, så tilsyn "
             "i boligområderne ikke afhænger af transport; dansk på modersmålsniveau, engelsk "
             "professionelt; tiltrædelse 1. januar 2027 passer.")

CLOSING = ("Jeg vil gerne gå en runde i FFB Syd, møde nogle af de 15 medarbejdere og bruge "
           "første samtale på to spørgsmål: hvordan måles driften i dag på tværs af de tre "
           "servicecentre, og hvilke rammer er aftalt for driftschefens egne beslutninger?")

# ------------------------------------------------------------------ CV
PROFILE = ("Rollen kræver tre ting på én gang: en nærværende leder af servicefolk, en der kan "
           "prioritere vedligeholdelse og investeringer over for en afdelingsbestyrelse, og en "
           "der kan gøre data og teknologi til en del af hverdagen i stedet for et projekt. Alle "
           "tre har været praksis i 20 år: ledelse af 5- til 15-mands teams og 25 specialister, "
           "drift af 24/7-anlæg med nul uplanlagte stop i fem år, 37 anlægsprojekter (2–10 mio. "
           "kr.) med budget og aflevering uden kritiske fund og 40+ serviceanlæg med fuldt P&L. "
           "Elautoriseret maskinmester (LV/MV/HV), B.Tech i Technology Management & Mechanical "
           "Engineering, arbejder dagligt med SAP/CMMS, Power BI, Python og Claude.")

PRACTICE = [
    ("Personaleledelse af servicecenter",
     "1:1-hjul hver fjerde uge, MUS med opfølgning, ugentligt tavlemøde med opgaver, "
     "prioriteter og sikkerhed, kompetenceplan pr. medarbejder og delegering med opfølgning; "
     "situationsbestemt ledelse (SLII) og lærlingeansvar med struktur."),
    ("Daglig drift og tilsyn",
     "Runder og tilsyn med fast kadence og dokumentation, fejlhistorik pr. ejendom, akut/"
     "planlagt-fordeling, KPI'er for svartid og gennemført vedligehold samt opfølgning på "
     "gentagne fejl."),
    ("Vedligeholdelse og investering",
     "Tilstandsvurdering pr. ejendom, prioritering efter risiko og økonomi, vedligeholdelsesplan "
     "med levetid, budget og månedlig prognose; business case med driftsomkostning over levetiden."),
    ("Afdelingsbestyrelser og dialog",
     "Fast mødekadence, ensartet dagsorden, to alternativer pr. beslutning, referat med ansvarlig "
     "og frist, og mundtlig formidling af teknik til ikke-teknikere."),
    ("Bygninger og tekniske installationer",
     "Ventilation, varme, CTS/BMS, el og belysning, VVS og udearealer; fejlfinding, "
     "energirigtig drift og dokumentation — med elautorisation (LV/MV/HV) i baggrunden."),
    ("Data og teknologi",
     "Opgave- og henvendelsesflow i system, dashboards for svartid, gentagne fejl og "
     "energiforbrug, automatiseret rapportering med Python og Claude, SAP/CMMS og Power BI."),
    ("KAB-Fællesskabet og leverandører",
     "Aftaler med fastlagte svartider og kvalitetskrav, opfølgning på leverandørdata, "
     "rammeaftaler og samarbejde med specialister om indkøb, teknik og jura."),
]

MODELS = [
    ("Driftsstyring",
     "Driftsplan pr. boligafdeling med tilstand, indsats og ansvarlig; runder og tilsyn med "
     "fast kadence og dokumentation"),
    ("Opgave og henvendelse",
     "Én indgang, svartid som måltal, prioritering akut/planlagt, opfølgning til opgaven er "
     "lukket og beboeren har fået svar"),
    ("Vedligehold",
     "Tilstandsvurdering, prioritering efter risiko og økonomi, vedligeholdelsesplan med levetid, "
     "SAP/CMMS som system of record"),
    ("Investering og budget",
     "Business case med driftsomkostning over levetiden, budget og månedlig prognose, "
     "afvigelsesliste med ejer og frist"),
    ("Bestyrelsesbetjening",
     "Fast kadence og dagsorden, to alternativer pr. beslutning, referat med ansvarlig og frist, "
     "status først på næste møde"),
    ("Ledelse",
     "1:1-hjul, MUS/GRUS, tavlemøde, kompetenceplan pr. medarbejder, sygefravær og trivsel som "
     "faste punkter"),
    ("Data",
     "KPI-board for svartid, gentagne fejl, gennemført vedligehold og energi; automatiseret "
     "rapportering i Power BI, Python og Claude"),
]

ACHIEVEMENTS = [
    ("Nul uplanlagte stop i fem år",
     "drift og vedligehold på 24/7-forsyningsanlægget Lynetten med SCADA, SAP, højspænding og "
     "koblingsanlæg — planlagt vedligehold og beredskab i stedet for brandslukning."),
    ("15, 14 og 12 mands teams ledet",
     "daglig personaleledelse, kapacitetsplanlægning, tavlemøder og kompetenceudvikling — med "
     "leverancer til aftalt tid."),
    ("40+ serviceanlæg med fuldt P&L",
     "egen virksomhed med 5 elektrikere og 3 lærlinge: kunder, aftaler, økonomi og kvalitet i "
     "bygnings- og HVAC-drift."),
    ("−40 % energikost og +40 % produktivitet",
     "dokumenterede forbedringer gennem måling, standardarbejde, energirigtig drift og "
     "dataunderstøttet planlægning."),
    ("37 anlægsprojekter uden kritiske fund",
     "2–10 mio. kr. hos Novo Nordisk med 25 specialister, budget, FAT/SAT og aflevering under "
     "GMP/FDA/EMA-krav."),
]

EXPERIENCE = [
    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og leverandøraftaler",
     [("Ledelse og drift af serviceforretning",
       "daglig personaleledelse, planlægning af serviceopgaver og udrykninger, kundekontakt og "
       "opfølgning på kvalitet; 40+ anlæg med fast serviceinterval."),
      ("Bygninger, HVAC og energi",
       "ventilation, varme, køl og el i bolig- og erhvervsejendomme; fejlfinding, "
       "energioptimering og dokumentation — med elautorisation (LV/MV/HV).")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister · GMP/FDA/EMA",
     [("Projekt, budget og aflevering",
       "kravspecifikation, fremdrift, økonomi og afvigelser; FAT/SAT, IQ/OQ/PQ og aflevering "
       "uden kritiske fund."),
      ("Koordination af specialister",
       "25 specialister på tværs af mekanik, el, proces og indkøb; mødekadence, beslutningslog og "
       "rapportering til ledelsen.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Produktion, fremdrift og kvalitet",
       "14-personers team med kapacitetsplanlægning, daglige tavlemøder og 11 samtidige "
       "entrepriser; montage i eksisterende byggeri med hensyn til drift og brugere.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · budgetter i SAP",
     [("Drift, vedligehold og beredskab",
       "planlagt vedligehold, tilstandskontrol og KPI'er i SAP; nul uplanlagte stop i fem år."),
      ("Medarbejdere, leverandører og sikkerhed",
       "koordinering af egne teknikere, entreprenører og leverandører — LOTO, "
       "arbejdstilladelser, garantisager og nærved-hændelser.")]),

    ("Elektromekaniker / Produktionsteamleder",
     "ARJ Engineering · Teheran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · skiftplanlægning, materialestyring og lager",
     [("Fremstilling og teknisk problemløsning",
       "skiftplanlægning, materialestyring og målopfølgning; reparation og diagnosticering af "
       "elektriske og mekaniske systemer gennem struktureret root cause-analyse.")]),
]

EDUCATION = [
    ("B.Tech (EQF niveau 6) — Technology Management & Mechanical Engineering",
     "Maskinmesterskolen / Copenhagen School of Marine Engineering & Technology Management · "
     "2017 – 2022 · karakter 7,6/12"),
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
     "Anvendt i drift, produktion og projekter · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og produktion · 2017 – nu"),
]

LANGUAGES = ("Dansk (modersmål, skrift og tale) · Engelsk (professionelt, skrift og tale) · "
             "Persisk/farsi · Kørekort B (kategori B)")

PRACTICAL_CV = ("Bosat i Måløv — cirka 20 minutter til Servicecenter Syd på Roskildevej; kørekort "
                "kategori B og bil, så tilsyn i boligområderne og møder i KAB-Huset kan foregå uden "
                "transportproblemer. Dansk på modersmålsniveau og engelsk professionelt i skrift og "
                "tale; kan tiltræde 1. januar 2027; egen virksomhed afvikles ved ansættelse.")

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Novo Nordisk A/S, Biofos (Lynetten), "
              "Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Beboerne og afdelingsbestyrelserne",
     "Én indgang for henvendelser med aftalt svartid, en fast mødekadence pr. afdeling og et "
     "referat, der gør det muligt at se, hvad der blev besluttet og hvornår det sker. To "
     "alternativer pr. beslutning, med levetid, økonomi og gener regnet ind."),
    ("Servicecentrets medarbejdere",
     "Faste rammer og tydelige prioriteter: 1:1-hjul, tavlemøde hver uge, kompetenceplan pr. "
     "medarbejder og sikkerhed som fast punkt — for et servicecenter flytter sig kun, hvis "
     "medarbejderne ved, hvad der bliver målt på."),
    ("FFB's driftschefer og KAB-Fællesskabet",
     "Ensartede processer og målinger på tværs af de tre servicecentre, fast fagligt samspil med "
     "KAB's specialister og beslutninger truffet inden for aftalte rammer — og løftet videre til "
     "fællesskabet, når en opgave kræver mere, end huset kan."),
]

FIRST90 = [
    ("Uge 1–2",
     "Gået alle 25 boligafdelinger igennem med områdeleder eller nøgleperson; set "
     "servicecentrets opgaver, værksted og lager; læst de seneste referater fra "
     "afdelingsbestyrelserne. Mødt de 15 medarbejdere, de to driftschefkolleger og kundechefen."),
    ("Uge 3–6",
     "1:1-samtaler med alle 15 gennemført; tavlemøde og opgavestrøm med svartider sat i drift; "
     "driftsplan pr. afdeling med tilstand og næste indsats lagt; mødekadence med "
     "afdelingsbestyrelserne aftalt."),
    ("Uge 7–12",
     "Vedligeholdelses- og investeringsplan for 2027 med prioritering og budget lagt frem; "
     "KPI-board for svartid, gentagne fejl og energi i brug; leverandøraftaler gennemgået med "
     "krav til svartid og kvalitet."),
    ("Måned 3–6",
     "Månedlig økonomiopfølgning med prognose indarbejdet; første forbedringer dokumenteret på "
     "energi og gentagne fejl; kompetenceplan for servicecentret på plads — og ensartede "
     "målinger med de to andre centre."),
    ("Måned 6–12",
     "Driften bliver målt, ikke beskrevet: svartider, gennemført vedligehold og "
     "beboertilfredshed som faste tal i ledelsesrapporteringen, og en investeringsrækkefølge for "
     "2028, der er aftalt med afdelingsbestyrelserne."),
]

KEYWORDS = (
    "Driftschef · Ejendomsdrift · Servicecenter · Servicecentre · Beboerdemokrati · "
    "Afdelingsbestyrelser · Beboerne · Boligafdelinger · Lejemål · Almen boligorganisation · "
    "Vedligeholdelse · Vedligeholdelsesopgaver · Investeringer · Bygningsdrift · Bygninger · "
    "Udearealer · Tilsyn · Daglig drift · Driftsorganisation · Personaleledelse · "
    "Ledelsesansvar · Motivere · Udvikle medarbejdere · Data og teknologi · Moderne drift · "
    "Digital · Driftschefkolleger · KAB-Fællesskabet · Specialister · Bygge- og "
    "udviklingsprojekter · Rådgivning · Samarbejde · Nærværende leder · Struktureret · Overblik · "
    "Empatisk · Nysgerrig · Leverandører · Budget · KPI · Frederiksberg"
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
        m.para(t, after=64, line=232)

    for label, body in BULLETS:
        m.bullet(label, body, after=14, line=232)

    m.para(SYSTEM, after=64, line=232)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=24, line=232)

    m.meta("Med venlig hilsen · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "LEDELSESPROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("DRIFTS- OG LEDELSESMETODER — ANVENDT I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER DRIFTEN I RYTMEN",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN LEDES OPGAVEN — DE TRE PARTER")
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
                  title="Ansøgning og CV — Driftschef, FFB / KAB",
                  subject="Ejendomsdrift · servicecenter · afdelingsbestyrelser · "
                          "vedligeholdelse og investeringer · data og teknologi",
                  keywords=("driftschef, ejendomsdrift, servicecenter, beboerdemokrati, "
                            "afdelingsbestyrelser, vedligeholdelse, bygningsdrift, "
                            "frederiksberg, kab, ffb, dansk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1 (krav → løsning), CV side 2-3, 90 dage side 4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_KAB_FFB_Driftschef.docx")
    print("OK", build(out))
