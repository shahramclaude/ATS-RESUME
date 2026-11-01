# -*- coding: utf-8 -*-
"""
Delpro A/S — Teamleder med el-teknisk baggrund (Vamdrup / projekter i hele DK).
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Teamleder, el-teknisk | Højspænding & projekter i hele Danmark"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = ("DELPRO A/S · Bavnevej 50, 6580 Vamdrup · att. Ressource Manager Simon Albeck")
SUBJECT = "Ansøgning: Teamleder med el-teknisk baggrund — projektafdelingen"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Teamlederrollen i projektafdelingen er en spillende træner: sikre fremdrift, kvalitet og "
    "tidsplaner og samtidig selv stå med i opgaveudførelsen på højspændingsinstallationer rundt om i "
    "Danmark — med koordinering af udstyr og komponenter og dokumentation, der holder ved aflevering.",

    "Nedenfor er min læsning af stillingen og det system, der står klar fra første dag: ugeplan med "
    "tavlemøde, materialeliste og indkøbsplan koblet til tidsplanen, dokumentationspakke med "
    "måleprotokoller, et fast afrapporteringsformat til Projektleder og Site Manager, "
    "sikkerhedsgodkendelser og LOTO på plads før arbejdet starter samt en hindringslog, der flytter "
    "problemet videre samme dag.",
]

BULLETS = [
    ("Kravet: sikre fremdrift, kvalitet og overholdelse af tidsplaner",
     "Løsningen er en ugeplan, der bliver gennemgået ved tavlen hver morgen — hvad der skal være "
     "færdigt i dag, hvad der mangler, og hvem der tager det. Jeg har kørt 37 samtidige "
     "anlægsprojekter med 25 specialister og 11 entrepriser med 14-mands team."),

    ("Kravet: deltage aktivt i opgaveudførelsen sammen med teamet",
     "Løsningen er at være på værktøjet, når det gælder: opmåling, fejlfinding, idriftsættelse og de "
     "svære punkter, hvor teamet har brug for en erfaren hånd ved siden af sig. Jeg er uddannet "
     "elektromekaniker og har arbejdet side om side med 5 elektrikere og 3 lærlinge."),

    ("Kravet: koordinere og bestille udstyr og komponenter",
     "Løsningen er en materialeliste pr. opgave, der bliver bestilt ud fra tidsplanen og ikke ud fra "
     "mavefornemmelse: kabler, tavler, komponenter og specialdele med leveringstid, montagevindue og "
     "ansvarlig — og en status, der følges, til varen er på pladsen."),

    ("Kravet: udarbejde nødvendig dokumentation",
     "Løsningen er at skrive dokumentationen, mens arbejdet sker: måleprotokoller, prøveark, "
     "as-built-opdateringer og afvigelsesliste med ejer og frist. Under GMP/FDA/EMA-krav leverede jeg "
     "37 projekter med nul kritiske fund."),

    ("Kravet: opgaver inden for højspændingsinstallationer og komponenter (en fordel, ikke et krav)",
     "Løsningen er min faglige base: elautoriseret maskinmester (LV/MV/HV), uddannet el-ingeniør og "
     "med fem år på et 24/7-forsyningsanlæg med koblingsanlæg, højspænding, frekvensomformere, "
     "motorværn og relæer. Jeg kan læse et diagram og vurdere en kobling — og give den oplæring, en "
     "teamleder skal kunne give."),

    ("Kravet: skabe godt samarbejde internt og med eksterne partnere og afrapportere til Projektleder "
     "og Site Manager",
     "Løsningen er et fast statusformat på én side — fremdrift, timer, materialer, hindringer og næste "
     "beslutning — sendt samme dag, som ugen slutter, så Projektleder og Site Manager kan beslutte på "
     "et oplyst grundlag."),

    ("Kravet: ansvar, proaktivitet, omstillingsparathed og overblik i udfordrende situationer",
     "Løsningen er at have besluttet på forhånd, hvad der viger, når to opgaver kolliderer: sikkerhed "
     "først, derefter det, der holder tidsplanen. Hindringer bliver logget med ejer og frist, og jeg "
     "melder tidligt ud, hvis en dato ikke kan holdes."),

    ("Kravet: projekter rundt om i Danmark med rejsedage og overnatninger — og dansk og engelsk",
     "Løsningen er, at rejsearbejde er kendt og accepteret: jeg har pendlet Måløv–Kalundborg i to år "
     "og boet ude i forbindelse med anlægsarbejde. Dansk på modersmålsniveau og engelsk professionelt "
     "med kunder og leverandører."),
]

SYSTEM = ("Systemet er allerede bygget for teamet: ugeplan med morgenmøde ved tavlen, materialeliste "
          "og indkøbsplan koblet til tidsplanen, dokumentationspakke med måleprotokoller, prøveark og "
          "as-built-opdatering, hindrings- og afvigelseslog med ejer og frist, statusnotat på én side "
          "til Projektleder og Site Manager hver uge og LOTO og arbejdstilladelser på plads før "
          "arbejdet starter — ført i Excel/Power BI, med rapporter genereret i Python og Claude.")

MIRROR = ("Om kravene: elautoriseret maskinmester (LV/MV/HV) og uddannet el-ingeniør, med tyve år i "
          "el-, køle- og HVAC-anlæg og fem år som drifts- og vedligeholdelseschef på et "
          "24/7-anlæg med koblingsanlæg og højspænding. Jeg har ledet 14-mands produktions- og "
          "montageteam, 5 elektrikere og 3 lærlinge, kørt 37 samtidige anlægsprojekter og 11 "
          "entrepriser — og arbejdet med dokumentation, der skulle bestå revision og aflevering.")

HONEST = ("To ting skal siges ligeud: jeg er ikke uddannet elektriker, men el-ingeniør og "
          "elautoriseret maskinmester — den praktiske del har jeg fra tretten år som elektromekaniker "
          "og indehaver af en el-virksomhed. Og jeg bor i Måløv, cirka tre timer fra Vamdrup: flytning "
          "er ikke udelukket, men det skal vi tale om, ikke gætte om.")

CULTURE = ("Hvorfor DELPRO: I arbejder mellem 10 og 400 kV på forsyningsnet, vindmølleparker og "
           "industri og er certificeret efter ISO 9001, 14001 og 45001 — så dokumentation og sikkerhed "
           "er styret, ikke bare ønsket. Og I beskriver et team med højt til loftet, respektfuld tone og "
           "frihed under ansvar, hvor gode initiativer bliver påskønnet: det er den slags miljø, hvor en "
           "teamleder kan tage ansvar.")

PRACTICAL = ("Praktisk: bosat i Måløv; kørekort B og bil og vant til at køre langt. Rejsedage og "
             "overnatninger accepteres som en fast del af stillingen — og jeg har bemærket, at I har "
             "Servicecenter Øst i Taastrup tæt på min bopæl. Dansk på modersmålsniveau og engelsk "
             "professionelt. Kan tiltræde hurtigst muligt.")

CLOSING = ("I første samtale vil jeg gerne høre, hvordan teamet i dag bliver sat sammen på en opgave, og "
           "hvor mange projekter der typisk kører samtidig i projektafdelingen.")

# ------------------------------------------------------------------ CV
PROFILE = ("Stillingen kræver en teamleder, der både kan holde fremdrift og selv stå med i "
           "opgaveudførelsen på højspændingsinstallationer, der bliver udført rundt om i Danmark. Tyve "
           "år i el-, køle- og HVAC-anlæg: elautoriseret maskinmester (LV/MV/HV), uddannet "
           "el-ingeniør og med fem år på et 24/7-forsyningsanlæg med koblingsanlæg, højspænding og "
           "SCADA. Ledelsesmæssigt: 14-mands produktions- og montageteam, 5 elektrikere og 3 lærlinge "
           "med fuldt P&L, 37 samtidige anlægsprojekter med 25 specialister og 11 entrepriser. "
           "Dokumentation, der bestod revision, og nul kritiske fund.")

PRACTICE = [
    ("Fremdrift og tidsplaner",
     "Ugeplan gennemgået ved tavlen hver morgen, milepæle med ejer og en hindringslog, der bliver "
     "tømt — ikke arkiveret."),
    ("Spillende træner",
     "Selv på værktøjet ved opmåling, fejlfinding og idriftsættelse; oplæring af lærlinge og yngre "
     "elektrikere ved at vise frem for at fortælle."),
    ("Udstyr og komponenter",
     "Materialeliste pr. opgave, indkøb ud fra tidsplanen, leveringstid og montagevindue fulgt til "
     "varen er på pladsen; leverandøraftaler og alternativer ved forsinkelse."),
    ("Højspænding og el-teknik",
     "Koblingsanlæg, højspænding, frekvensomformere, motorværn, relæer og tavler; LV/MV/HV-autorisation "
     "og el-ingeniørbaggrund."),
    ("Dokumentation",
     "Måleprotokoller, prøveark, as-built-opdatering og afvigelsesliste med ejer og frist; "
     "sporbarhed som arbejdsform, ikke som afslutning."),
    ("Sikkerhed på pladsen",
     "LOTO, arbejdstilladelser og sikkerhedsgennemgang før arbejdet starter; nærved-hændelser "
     "rapporteret uden skyld."),
    ("Samarbejde og afrapportering",
     "Statusnotat på én side hver uge til Projektleder og Site Manager, faste møder med kunde og "
     "entreprenør og aftaler skrevet ned, før arbejdet begynder."),
]

MODELS = [
    ("Ugeplan",
     "Opgaveliste med ansvarlig, frist og afhængigheder; tavlemøde hver morgen og justering samme "
     "dag"),
    ("Materialer",
     "Materialeliste pr. opgave med leveringstid og montagevindue; bestilling ud fra tidsplan, ikke "
     "lagerstatus alene"),
    ("Dokumentation",
     "Måleprotokol, prøveark og as-built opdateret løbende; afvigelse med ejer og lukkekriterium"),
    ("Sikkerhed",
     "LOTO og arbejdstilladelse før opstart, sikkerhedsgennemgang ved nye opgaver og nærved-hændelser "
     "uden skyld"),
    ("Afrapportering",
     "Statusnotat på én side hver uge: fremdrift, timer, materialer, hindringer og næste beslutning"),
    ("Hindringer",
     "Hindringslog med ejer, frist og konsekvens; eskalering til Projektleder eller Site Manager "
     "samme dag"),
    ("Opfølgning",
     "Timer og materialeforbrug mod kalkule pr. uge; afvigelser forklaret, før de bliver til tab — "
     "rapporter genereret med Python og Claude"),
]

ACHIEVEMENTS = [
    ("37 anlægsprojekter uden kritiske fund",
     "2–10 mio. kr. hos Novo Nordisk med 25 specialister koordineret, FAT/SAT, IQ/OQ/PQ og "
     "dokumentation, der bestod revision under GMP/FDA/EMA."),
    ("14-mands team og 11 entrepriser samtidig",
     "kapacitetsplanlægning, daglige tavlemøder og leverancer til aftalt tid i eksisterende byggeri "
     "med drift og brugere omkring os."),
    ("40+ serviceanlæg med fuldt P&L",
     "egen el-virksomhed med 5 elektrikere og 3 lærlinge: kunder, tilbud, indkøb, leverandøraftaler "
     "og ansvar for bundlinjen."),
    ("Nul uplanlagte stop i fem år",
     "24/7-forsyningsanlæg med koblingsanlæg, højspænding og SCADA — planlagt vedligehold, "
     "arbejdstilladelser og LOTO som fast regime."),
    ("+40 % produktivitet og −40 % energikost",
     "dokumenterede forbedringer gennem standardarbejde, Lean-værktøjer og dataunderstøttet "
     "planlægning."),
]

EXPERIENCE = [
    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og leverandøraftaler",
     [("Spillende ledelse og oplæring",
       "daglig arbejdsplanlægning side om side med 5 elektrikere og 3 lærlinge, oplæring på "
       "opgaven og faglig kvalitetssikring af arbejdet, før det blev afleveret."),
      ("Kunder, indkøb og økonomi",
       "tilbudsberegning, indkøb og leverandøraftaler, plan og prognose med fuldt ansvar for "
       "bundlinjen; ændringssager prissat, før arbejdet blev udført.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · koblingsanlæg, højspænding, pumper, HVAC og SCADA · budgetter i SAP",
     [("Højspænding og anlæg",
       "koblingsanlæg, højspænding, frekvensomformere og motorværn; fejlfinding og "
       "tilstandsvurdering med nul uplanlagte stop i fem år."),
      ("Sikkerhed og leverandører",
       "koordinering af egne teknikere, entreprenører og leverandører — LOTO, arbejdstilladelser, "
       "garantisager og nærved-hændelser fulgt til lukning.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister · GMP/FDA/EMA",
     [("Fremdrift, økonomi og dokumentation",
       "plan og budget pr. projekt, fremdrift og rapportering til styregruppe; kravspecifikation, "
       "FAT/SAT, IQ/OQ/PQ og aflevering uden kritiske fund.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Team, produktion og montage",
       "14-personers team med kapacitetsplanlægning, daglige tavlemøder og 11 samtidige entrepriser; "
       "montage i eksisterende byggeri med hensyn til drift og brugere.")]),

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
     "Anvendt i drift og projekter · 2017 – nu"),
]

LANGUAGES = ("Dansk (modersmål, skrift og tale) · Engelsk (professionelt, skrift og tale) · "
             "Persisk/farsi · Kørekort B (kategori B)")

PRACTICAL_CV = ("Bosat i Måløv; kørekort kategori B og bil, og vant til at køre langt. Rejsedage og "
                "overnatninger accepteres som en fast del af stillingen. Dansk på modersmålsniveau og "
                "engelsk professionelt. Kan tiltræde hurtigst muligt; egen virksomhed afvikles ved "
                "ansættelse.")

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Novo Nordisk A/S, Biofos (Lynetten), "
              "Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Teamet",
     "Ugeplan og morgenmøde ved tavlen, tydelig fordeling af opgaver og en teamleder der selv tager "
     "de svære punkter — faglighed skal vises, ikke forklares."),
    ("Projektleder og Site Manager",
     "Statusnotat på én side hver uge og aftaler skrevet ned, før arbejdet begynder; tidlig melding, "
     "hvis en dato ikke kan holdes, i stedet for en overraskelse ved aflevering."),
    ("Kunder, leverandører og eksterne parter",
     "Aftaler på skrift, leveringstid og montagevindue fulgt til varen er på pladsen, og en "
     "dokumentationspakke der kan overdrages uden at nogen skal ringe bagefter."),
]

FIRST90 = [
    ("Uge 1–2",
     "Været med på en igangværende opgave og set arbejdet fra stillads og tavle; gennemgået "
     "tidsplaner, materialelister, dokumentationskrav og sikkerhedsregler med Ressource Manager, "
     "Projektleder og Site Manager."),
    ("Uge 3–6",
     "Egen ugeplan, materialeliste og statusnotat i brug på mine opgaver; hindringslog etableret; "
     "sikkerhedsgennemgang og LOTO-rutiner prøvet af på pladsen sammen med teamet."),
    ("Uge 7–12",
     "Første opgave leveret til tiden og med dokumentationen i orden; måleprotokoller og as-built "
     "opdateret løbende; oplæringsplan for lærlinge og yngre elektrikere aftalt."),
    ("Måned 3–6",
     "Kørt selvstændigt på flere opgaver rundt i landet med stabil fremdrift; materialeforbrug og "
     "timer fulgt mod kalkule; samarbejdet med Projektleder og Site Manager formaliseret i fast "
     "kadence."),
    ("Måned 6–12",
     "Teamet leverer uden at hænge på enkeltpersoner: procedurer og dokumentationsskabeloner delt, "
     "kompetencer spredt på flere hænder og afvigelser brugt som forbedringer frem for gentagelser."),
]

KEYWORDS = (
    "Teamleder · El-teknisk baggrund · El-tekniske projektopgaver · Projektafdelingen · Struktureret · "
    "Løsningsorienteret · Højspændingsinstallationer · Højspændingsarbejde · Komponenter · Spillende "
    "træner · Fremdrift · Kvalitet · Tidsplaner · Opgaveudførelsen · Teamet · Koordinere og bestille "
    "udstyr · Dokumentation · Samarbejde · Eksterne partnere · Ressource Manager · Projektleder · Site "
    "Manager · Vamdrup · Projekter rundt om i Danmark · Rejsedage · Overnatninger · Elektriker · "
    "Forsyningsoperatør · Supervisor · Arbejdsleder · Ansvar · Proaktivt · Omstillingsparat · Overblik "
    "· Udfordrende situationer · Relationer · Dansk og engelsk · Højt til loftet · Humoristisk men "
    "respektfuld omgangstone · Trivsel · Faglig udvikling · Åbent og uformelt arbejdsmiljø · Frihed "
    "under ansvar · Initiativer · DELPRO · Hovedkontor · Maskinmester · LV/MV/HV · El-ingeniør · "
    "Koblingsanlæg · LOTO · Arbejdstilladelser · As-built · Måleprotokoller · Tavlemøde · Lean · SAP"
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
        m.bullet(label, body, after=10, line=228)

    m.para(SYSTEM, after=56, line=228)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=18, line=228)

    m.meta("Med venlig hilsen · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "FAGLIG PROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("TEAMETS STYRESYSTEM — ANVENDT I PRAKSIS",
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
                  title="Ansøgning og CV — Teamleder med el-teknisk baggrund, DELPRO A/S",
                  subject="Højspændingsinstallationer · projektafdeling · spillende træner · "
                          "dokumentation · projekter i hele Danmark",
                  keywords=("teamleder, el-teknisk, højspænding, højspændingsinstallationer, "
                            "projektafdeling, dokumentation, vamdrup, delpro, maskinmester, "
                            "arbejdsleder, dansk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1 (krav → løsning), CV side 2-3, 90 dage side 4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_Delpro_TeamlederElteknisk.docx")
    print("OK", build(out))
