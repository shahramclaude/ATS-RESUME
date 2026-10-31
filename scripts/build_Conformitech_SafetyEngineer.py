# -*- coding: utf-8 -*-
"""
Conformitech ApS — Safety Engineer inden for maskinsikkerhed (Nørresundby / Bramming).
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
Specialiststilling: ledelseserfaringen tones ned, dokumentations- og standardsiden frem.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Safety Engineer | Maskinsikkerhed og CE-mærkning | Nørresundby"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = ("Conformitech ApS · Aurikelvej 8, 9310 Vodskov · sendt til kontakt@conformitech.dk "
             "med emnet »Safety Engineer Nord«")
SUBJECT = "Ansøgning: Safety Engineer inden for maskinsikkerhed — Nord"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Opgaven er at være den faglige rådgiver, der kan svare en maskinfabrikant præcist på, hvad "
    "maskinen kræver — og skrive det ned, så svaret holder ved en myndighedskontrol. Fra "
    "risikovurdering over "
    "sikringsløsning og sikker styring til den færdige CE-dokumentation, med hjemmel i den "
    "konkrete paragraf og det konkrete standardafsnit.",

    "Nedenfor er min læsning af rollen og det system, der står klar fra første dag: "
    "standardsbibliotek med uddrag og paragrafhenvisning pr. maskintype, risikovurdering efter "
    "ISO 12100 med sporbarhed fra fare til foranstaltning, verifikationsmatrix hvor hvert "
    "væsentligt krav peger på dokumentafsnit og prøve, inspektionscheckliste og en fast "
    "leverancekadence — så et projekt kan overdrages uden at gætte.",
]

BULLETS = [
    ("Kravet: rådgivning om CE-mærkning, risikovurderinger og design af sikringsløsninger",
     "Løsningen er at give svaret med hjemmel: hvilken fare, hvilket væsentligt krav, hvilken "
     "standard og hvilken foranstaltning — og hvad den koster i produktionstid. I 37 "
     "anlægsprojekter har jeg skrevet kravspecifikation og acceptkriterier, kørt FAT/SAT og "
     "afleveret uden kritiske fund: samme metode, anden lovgivning."),

    ("Kravet: el på maskiner og elektrisk sikkerhed",
     "Løsningen er el-fagligheden i bund: elautoriseret maskinmester (LV/MV/HV), el-ingeniør i "
     "baggrunden og 20 år med koblingsanlæg, frekvensomformere, motorværn, nødstopkredse og "
     "beskyttelsesleder. Jeg kan læse et el-diagram og se, om EN 60204-1 er fulgt — og ved, hvad "
     "Arbejdstilsynet spørger om."),

    ("Kravet: sikre styresystemer og validering af sikre styringer",
     "Løsningen er at ræsonnere i kategorier og performance level: hvilken risikograf, hvilket PL, "
     "hvilken arkitektur og hvilke komponenter der faktisk kan bære det — og hvilke afprøvninger der "
     "skal dokumenteres. Jeg har arbejdet med PLC, SCADA og sikkerhedsrelaterede styringer i drift "
     "og idriftsættelse; SISTEMA-beregning efter EN ISO 13849-1 er den del, jeg skal lære hos jer."),

    ("Kravet: ATEX i forhold til gældende direktiver og standarder",
     "Løsningen er at gå på zonering og udstyrskategori først: hvor er den eksplosionsfarlige zone, "
     "hvilke tændkilder skal udelukkes, og hvordan bliver det vedligeholdt og dokumenteret. Jeg har "
     "arbejdet i klassificerede miljøer på forsyningsanlæg med arbejdstilladelser og energilukning "
     "som fast regime. ATEX-dokumentation som rådgiver har jeg ikke ejet før — det er en af de "
     "certificeringer, jeg gerne tager."),

    ("Kravet: inspektioner og audits af maskiner og produktionsudstyr",
     "Løsningen er en checkliste pr. maskintype og en rapport, hvor hvert fund har fare, risiko, "
     "krav, løsningsforslag og prioritet — ikke en række iagttagelser. Jeg har kørt "
     "sikkerhedsrunder på 24/7-anlæg og været på modtagersiden af revisioner i 20 år."),

    ("Kravet: dokumentation — risikovurderinger, brugsanvisninger, rapporter, notater og LOTO",
     "Løsningen er dokumentation med struktur og versionsstyring: risikovurdering med sporbarhed, "
     "brugsanvisning opbygget efter EN ISO 20607's logik, LOTO-procedure med rækkefølge, mærkning "
     "og ansvar. Jeg har leveret dokumentationspakker, der skulle stå frem ved en revision uden "
     "bemærkninger — og det er den slags arbejde, jeg gør grundigt."),

    ("Kravet: undervisning i maskinsikkerhed, CE-mærkning, sikre styringer og ATEX",
     "Løsningen er at bygge undervisningen på kundens egne maskiner og egne fund: korte moduler, "
     "cases fra deres produktion, en øvelse i risikovurdering og materiale, de kan bruge bagefter. "
     "Jeg har oplært lærlinge og teknikere og undervist i sikker adfærd; et professionelt "
     "kursuskatalog har jeg ikke stået bag endnu."),
]

SYSTEM = ("Systemet er allerede bygget: standardsbibliotek med paragrafhenvisning pr. maskintype, "
          "risikovurderingsskabelon efter ISO 12100 med sporbarhed fra fare til foranstaltning, "
          "verifikationsmatrix hvor hvert krav peger på dokumentafsnit og prøve, "
          "inspektionscheckliste med prioriteret fundrapport, LOTO- og brugsanvisningsskabeloner, "
          "dokumentregister med version og ejer og en fast leverancekadence — i Safexpert/Excel og "
          "med rapporter genereret i Python og Claude.")

MIRROR = ("Om kravene: elautoriseret maskinmester (LV/MV/HV) med B.Tech i Technology Management & "
          "Mechanical Engineering og el-ingeniør; 20 år med maskiner, el-anlæg og styringer — 37 "
          "anlægsprojekter (2–10 mio. kr.) med kravspecifikation, FAT/SAT og dokumentation uden "
          "kritiske fund under GMP/FDA/EMA; 24/7-drift med SCADA, højspænding, LOTO og "
          "arbejdstilladelser og nul uplanlagte stop i fem år; dansk på modersmålsniveau og engelsk "
          "professionelt.")

HONEST = ("Tre ting skal siges ligeud: jeg har ikke været CE-rådgiver før — jeg har leveret "
          "dokumentation, der skulle holde for myndigheder og kunder, men ikke selv skrevet den "
          "tekniske dossier og underskrevet overensstemmelseserklæringen. Jeg har ikke brugt "
          "Safexpert eller SISTEMA i daglig praksis, og ATEX-dokumentation har jeg ikke ejet. Og jeg "
          "bor i Måløv, så Nord betyder flytning. Til gengæld kommer jeg med det, der er sværest at "
          "lære: el-fagligheden, dokumentationsdisciplinen og evnen til at sige fra.")

CULTURE = ("Hvorfor Conformitech: kvaliteten skal være i top, men løsningerne skal være "
           "pragmatiske, og I stiller altid spørgsmålet »Giver det værdi?«. Det er den rækkefølge, "
           "jeg arbejder i: først hvad kravene faktisk kræver, derefter den løsning der beskytter "
           "operatøren uden at ødelægge produktionen. At I er fem safety engineers i en flad "
           "organisation med korte beslutningsveje, meget sparring og en plads i DS-udvalget — "
           "altså er foran med maskinforordningen — er grunden til, at jeg søger her.")

PRACTICAL = ("Praktisk: bosat i Måløv, søger Nord med flytning for øje — jeg har pendlet til Kalundborg "
             "i to år og ved, hvad lang transport koster. Kørekort B og bil; dansk på "
             "modersmålsniveau, engelsk professionelt; kan tiltræde efter aftale.")

CLOSING = ("I første samtale vil jeg gerne høre, hvordan I fordeler opgaverne mellem Nord og Syd i "
           "dag, og hvor meget af arbejdet der ligger i inspektion, dokumentation og undervisning. "
           "Jeg gennemgår gerne en prøveopgave.")

# ------------------------------------------------------------------ CV
PROFILE = ("Rollen kræver tre ting på én gang: el- og maskinfaglig tyngde nok til at vurdere en "
           "maskine, dokumentationsdisciplin nok til at gøre det skriftligt og revisionsparat, og "
           "fasthed nok til at sige fra over for en kunde, når sikkerheden er på spil. Tyve år med "
           "maskiner, el-anlæg og styringer: 37 anlægsprojekter (2–10 mio. kr.) med kravspecifikation, "
           "FAT/SAT og dokumentation uden kritiske fund under GMP/FDA/EMA, 24/7-drift med SCADA, "
           "højspænding, LOTO og arbejdstilladelser og nul uplanlagte stop i fem år. Elautoriseret "
           "maskinmester (LV/MV/HV), B.Tech i Technology Management & Mechanical Engineering og "
           "el-ingeniør — med dansk på modersmålsniveau og engelsk professionelt.")

PRACTICE = [
    ("Standarder og lovtekst",
     "Læser standard og lovtekst med paragraf og afsnit for øje og omsætter det til en "
     "foranstaltning, der kan bygges og vedligeholdes; ISO 12100, EN 60204-1 og EN ISO 13849 er "
     "arbejdsredskaber, ikke overskrifter."),
    ("Risikovurdering",
     "Risikograf og fareidentifikation systematisk fra alle livsfaser, sporbarhed fra fare over "
     "væsentligt krav til foranstaltning, restrisiko og oplysning til bruger."),
    ("Sikre styringer og validering",
     "Kategori, performance level og arkitektur; SRS-lignende kravspecifikation, afprøvning og "
     "dokumentation af sikkerhedsfunktioner — bygget videre på PLC-, SCADA- og "
     "idriftsættelseserfaring."),
    ("El på maskiner",
     "Nødstopkredse, beskyttelsesleder og potentialeudligning, motorværn, frekvensomformere og "
     "kapsling; elautorisation (LV/MV/HV) og revisioner med Arbejdstilsynet som modpart."),
    ("Dokumentation og sporbarhed",
     "Brugsanvisning efter EN ISO 20607's opbygning, rapporter og notater med version og ejer, "
     "dokumentregister og revisionsparathed — kravspecifikation, FAT/SAT, IQ/OQ/PQ."),
    ("LOTO og sikker adfærd",
     "Energilukning med rækkefølge, mærkning og ansvar, arbejdstilladelser og "
     "sikkerhedsrunder; nærved-hændelser og læring som fast punkt."),
    ("Kunder og undervisning",
     "Rådgivning i øjenhøjde med kundens teknikere og ledelse, oplæg og undervisning med kundens "
     "egne maskiner som cases, og skriftligt materiale der kan bruges bagefter."),
]

MODELS = [
    ("Standard og krav",
     "Standardsbibliotek med uddrag og paragrafhenvisning pr. maskintype; hvert væsentligt krav "
     "sporet til en foranstaltning"),
    ("Risikovurdering",
     "Fareidentifikation i alle livsfaser, risikograf, foranstaltninger i prioriteret rækkefølge, "
     "restrisiko og oplysning til bruger"),
    ("Sikre styringer",
     "Kategori og PL/SIL fastlagt ud fra risikograf, SRS-lignende krav, afprøvning og validering "
     "dokumenteret og versionsstyret"),
    ("Inspektion og audit",
     "Checkliste pr. maskintype, fund med fare, risiko, krav, løsningsforslag og prioritet, "
     "opfølgning til lukket"),
    ("Dokumentation",
     "Dokumentregister med version og ejer, brugsanvisning efter EN ISO 20607's opbygning, "
     "revisionsparat teknisk dossier"),
    ("LOTO",
     "Procedure med energikilder, rækkefølge, mærkning, ansvar og kontrol før arbejdet starter"),
    ("Digitalt",
     "Skabeloner og rapporter genereret med Python og Claude, Safexpert/Excel til registrering — "
     "mindre håndarbejde, mere sporbarhed"),
]

ACHIEVEMENTS = [
    ("Dokumentation uden kritiske fund",
     "37 anlægsprojekter, 2–10 mio. kr., under GMP/FDA/EMA — kravspecifikation, FAT/SAT, "
     "IQ/OQ/PQ og revisionsparat dokumentation."),
    ("Nul uplanlagte stop i fem år",
     "24/7-forsyningsanlægget Lynetten med SCADA, højspænding og koblingsanlæg; planlagt "
     "vedligehold, LOTO og arbejdstilladelser som fast regime."),
    ("25 specialister koordineret",
     "på tværs af mekanik, el, proces og indkøb i 37 samtidige projekter — med klare "
     "acceptkriterier og beslutningslog."),
    ("Sikkerhed håndhævet i praksis",
     "som indehaver og på 24/7-anlæg: arbejdsstop og omprioritering, når sikkerheden var på spil — "
     "også når det kostede tid i planen."),
    ("−40 % energikost og +40 % produktivitet",
     "dokumenterede forbedringer gennem måling, standardarbejde og dataunderstøttet planlægning."),
]

EXPERIENCE = [
    ("Indehaver / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · el- og HVAC-anlæg · fuldt P&L",
     [("El på maskiner og anlæg",
       "dimensionering, fejlfinding og dokumentation på el- og styringsanlæg; elautorisation "
       "(LV/MV/HV) og ansvar for sikker udførelse på kundens anlæg."),
      ("Dokumentation og kundekontakt",
       "tilbud og teknisk afklaring, dokumentation pr. opgave, oplæring af lærlinge og "
       "sikkerhedsmæssige vurderinger på stedet.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister · GMP/FDA/EMA",
     [("Krav, verifikation og aflevering",
       "kravspecifikation og acceptkriterier, FAT/SAT, IQ/OQ/PQ og aflevering uden kritiske fund; "
       "test og dokumentation af sikkerhedsfunktioner på procesanlæg."),
      ("Myndighed og revision",
       "arbejde under GMP/FDA/EMA-krav og myndighedstilsyn; dokumentation der kunne stå frem ved "
       "revision.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Produktion og maskinsikkerhed i praksis",
       "maskiner og værktøj i drift, sikker opstilling og adgangsforhold, instruktion af "
       "medarbejdere og opfølgning på nærved-hændelser.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · budgetter i SAP",
     [("Drift, vedligehold og sikker adgang",
       "LOTO og arbejdstilladelser, energilukning før indgreb, sikkerhedsrunder og "
       "tilstandskontrol; nul uplanlagte stop i fem år."),
      ("Anlæg og dokumentation",
       "ændringer dokumenteret med tegning, reservedel og driftsvejledning; leverandører og "
       "entreprenører styret på sikkerhed og kvalitet.")]),

    ("Elektromekaniker / Produktionsteamleder",
     "ARJ Engineering · Teheran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · skiftplanlægning, materialestyring og lager",
     [("Elektriske og mekaniske systemer",
       "reparation og diagnosticering gennem struktureret root cause-analyse; sikker opstilling og "
       "instruktion ved maskinerne.")]),
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
    ("Arbejdsmiljø §16 og sikkerhedsbevidsthed (VI/6-1)",
     "Søfartsstyrelsen · maj 2021"),
    ("Køleteknik & klimaanlæg (AMU)",
     "Mercantec · mar. 2021"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og produktion · 2017 – nu"),
    ("Lean — værdistrømsanalyse, standardarbejde, 5S og A3",
     "Anvendt i drift og projekter · 2017 – nu"),
]

LANGUAGES = ("Dansk (modersmål, skrift og tale) · Engelsk (professionelt, skrift og tale) · "
             "Persisk/farsi · Kørekort B (kategori B)")

PRACTICAL_CV = ("Bosat i Måløv og søger stillingen i Nørresundby med flytning for øje; har pendlet "
                "Måløv–Kalundborg i to år. Kørekort kategori B og bil, da opgaverne kræver "
                "kørsel til kunder. Dansk på modersmålsniveau og engelsk professionelt i skrift og "
                "tale; kan tiltræde efter aftale; egen virksomhed afvikles ved ansættelse.")

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Novo Nordisk A/S, Biofos (Lynetten), "
              "Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Kunden",
     "Én kontakt med aftalt svartid, en rapport hvor fundet står med fare, krav, løsning og "
     "prioritet — og en tydelig besked, når noget ikke kan forsvares sikkerhedsmæssigt, også når "
     "det forsinker produktionen."),
    ("Teamet",
     "Kollegial sparring før konklusionen låses: anden gennemlæsning af risikovurdering og "
     "dokumentation, og skabeloner og standardbibliotek der bliver delt i stedet for at leve på "
     "den enkelte maskine."),
    ("Myndighed og standard",
     "Sporbarhed hele vejen: hvert væsentligt krav peger på en foranstaltning, en prøve og et "
     "dokumentafsnit — så svaret holder ved Arbejdstilsynet, ved kunden og ved overgangen til "
     "maskinforordning (EU) 2023/1230."),
]

FIRST90 = [
    ("Uge 1–2",
     "Læst Conformitechs eget system igennem — skabeloner, Safexpert-opsætning, "
     "standardsbibliotek og dokumentregister; gennemgået to igangværende projekter fra "
     "risikovurdering til dokumentation. Mødt teamet, ejerne og de nærmeste kunder."),
    ("Uge 3–6",
     "Egen første risikovurdering gennemført med kollegial gennemlæsning; inspektionscheckliste "
     "pr. maskintype prøvet af hos en kunde; egne notater og rapporter lagt ind i den fælles "
     "struktur."),
    ("Uge 7–12",
     "Første selvstændige CE-forløb fra risikovurdering til dokumentation med kollega som "
     "reviewer; LOTO- og brugsanvisningsskabeloner brugt i praksis; påbegyndt CMSE-certificering."),
    ("Måned 3–6",
     "Selvstændig rådgiver på egne kunder med fast svartid; el på maskiner og sikre styringer "
     "dækket uden at skulle sparre hver gang; første undervningsmodul bygget sammen med den "
     "kollega, der i dag står for kurserne."),
    ("Måned 6–12",
     "Egne kunder og egne forløb, CEFS eller tilsvarende certificering gennemført, og "
     "maskinforordningens krav (digital dokumentation, software og opdateringer, væsentlige "
     "ændringer) indarbejdet i de skabeloner, kunderne får udleveret inden 2027."),
]

KEYWORDS = (
    "Maskinsikkerhed · Safety Engineer · CE-mærkning · Teknisk dokumentation · Risikovurdering · "
    "Brugsanvisning · Sikringsløsninger · El på maskiner · Sikre styresystemer · Sikre styringer · "
    "Validering · ATEX · LOTO · Inspektioner · Audits · Rapporter · Notater · Undervisning · "
    "Lovtekst · Standarder · Kundekontakt · Selvstændigt · Initiativ · Dansk · Engelsk · Safexpert · "
    "CMSE · CEFS · FMEA · Maskinforordning · 2023/1230 · Maskindirektiv · 2006/42/EF · ISO 12100 · "
    "EN 60204-1 · EN ISO 13849 · Teknisk dossier · Maskinfabrikanter · Produktionsvirksomheder · "
    "Importører · Rådgivende ingeniørvirksomhed · Pragmatiske · Flad organisation · Sparring · "
    "Nørresundby · Bramming · Dokumentationsarbejde"
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
        m.para(t, after=64, line=228)

    for label, body in BULLETS:
        m.bullet(label, body, after=12, line=228)

    m.para(SYSTEM, after=60, line=228)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=20, line=228)

    m.meta("Med venlig hilsen · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "FAGLIG PROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("METODER OG VÆRKTØJER — ANVENDT I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN BLIVER JEG SELVSTÆNDIG RÅDGIVER",
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
                  title="Ansøgning og CV — Safety Engineer, maskinsikkerhed, Conformitech ApS",
                  subject="Maskinsikkerhed · CE-mærkning · risikovurdering · el på maskiner · "
                          "sikre styringer · dokumentation",
                  keywords=("maskinsikkerhed, safety engineer, ce-mærkning, risikovurdering, "
                            "brugsanvisning, el på maskiner, sikre styringer, atex, loto, "
                            "maskinforordning, conformitech, dansk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1 (krav → løsning), CV side 2-3, 90 dage side 4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_Conformitech_SafetyEngineer.docx")
    print("OK", build(out))
