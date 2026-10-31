# -*- coding: utf-8 -*-
"""
FAGTEK A/S — Elteknisk Projektleder (Safe·ion, ABA og brandsikring).
Dansk JD, rekruttering via Compass Human Resources Group.
Designet fra master-CV'erne; bindende regel: dokumentet handler om opgaven,
missionen og stillingen — side 1 er "Kravet → Løsningen er" + det system,
der allerede er bygget.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Elteknisk Projektleder | Safe·ion · FAGTEK"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv")

DATE = "31. oktober 2026"
RECIPIENT = ("FAGTEK A/S · Brogesvej 18, 7441 Bording · via Compass Human Resources Group, "
             "att. Claus Mengel-Niemann, Senior Consultant · tlf. 22 63 33 77")
SUBJECT = "Ansøgning: Elteknisk Projektleder — Safe·ion"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Safe·ion skal bygges, ikke bare drives. Det betyder, at projektlederen er både den tekniske og "
    "den kommercielle motor: finde kunderne og samarbejdspartnerne, besigtige og afklare løsningen, "
    "kalkulere og vinde opgaven, koordinere teknikere og eksterne parter, levere og dokumentere — og "
    "samtidig forme de arbejdsgange, som området skal vokse på.",

    "Nedenfor er min læsning af opgaven og det system, der ligger klar: besigtigelses- og "
    "afklaringsskabelon, kalkulations- og tilbudsmodel, projektmodel med gates, afleveringscheckliste og "
    "en pipeline med ugentlig opfølgning.",
]

BULLETS = [
    ("Kravet: opsøge og følge op på kunder, rådgivere, elinstallatører og samarbejdspartnere",
     "Løsningen er en kunde- og partnerplan med ansvar og næste skridt pr. navn: rådgivere og "
     "elinstallatører får en fast kontakt og aftalte spilleregler, og hvert emne har en "
     "opfølgningsdato — ikke en intention."),

    ("Kravet: besigtige nye opgaver og afklare teknik, materialer og rammer",
     "Løsningen er en besigtigelsesskabelon, der går på det, der afgør økonomien: eksisterende ABA- og "
     "ABV-anlæg, kabelføring og tavleplads, bygningsforhold, adgang og arbejdstider, dokumentation, "
     "grensesnit til andre fag — og en afklaringsrapport, der bliver tilbudets grundlag i stedet for en "
     "hukommelse."),

    ("Kravet: kalkulere, udarbejde tilbud, følge aktivt op og styre økonomien",
     "Løsningen er en kalkulationsmodel med timer, materialer, underleverandører, risiko og dækningsgrad, "
     "tilbud med tydelige forudsætninger og optioner, opfølgning på faste dage — og en månedlig "
     "gennemgang af timer mod kalkule og dækningsgrad pr. projekt, så en sag bliver rettet, mens der "
     "stadig er penge i den."),

    ("Kravet: drive projekter fra ordre til aflevering — med teknikere, eksterne parter, fremdrift og kvalitet",
     "Løsningen er en projektmodel med faser og gates: ordre og materialebestilling, ugentlig "
     "fremdriftsstatus med afvigelser og årsag, test og idriftsættelse, aflevering med dokumentation — én "
     "plan, som kunden, teknikeren og underentreprenøren arbejder efter."),

    ("Kravet: bidrage fagligt og praktisk, når opgaven kræver det",
     "Løsningen er elautorisation (LV/MV/HV) og tyve år med måling, fejlfinding, tavler, styring og "
     "idriftsættelse — besigtigelse og kvalitetssikring med hænderne i det, ikke kun på papir."),

    ("Kravet: udvikle processer og arbejdsgange i takt med, at Safe·ion vokser",
     "Løsningen er et lille, fast procesbibliotek fra start — besigtigelse, tilbud, projektmodel, "
     "aflevering, dokumentation og support til installationspartnere — skrevet kort nok til, at det bliver "
     "brugt, og udbygget, når opgaven kræver det."),
]

SYSTEM = ("Systemet er allerede bygget: besigtigelses- og afklaringsskabelonen, kalkulationsmodellen med "
          "dækningsgrad pr. projekt, tilbudsskabelonen med forbehold og optioner, projektmodellen med "
          "gates og afleveringscheckliste samt pipelinen, der gennemgås hver uge — i Excel, Power BI og "
          "SharePoint, suppleret med Python og Claude til kalkulation, tilbudstekster og rapportering.")

MIRROR = ("Om kvalifikationerne: opslaget peger på elektriker, elinstallatør, maskinmester eller "
          "elektronikfagtekniker — jeg er elautoriseret maskinmester (LV/MV/HV) med elteknisk "
          "projekteringsbaggrund (el-ingeniør, EQF 6) og B.Tech i Technology Management, og har drevet egen "
          "virksomhed med fuldt P&L-ansvar, egne tilbud og kunder samt 37 samtidige anlægsprojekter hos Novo "
          "Nordisk. Kommerciel forståelse er ikke et tillægsord her; det var forretningsmodellen.")

HONEST = ("To ting skal siges ligeud: jeg har arbejdet med ABA/ABV, nød- og panikbelysning, tavler og "
          "dokumentation i el-installation, men har ikke projekteret AWEX-anlæg eller taget brandteknisk "
          "basiskursus — det er kurser, jeg tager, og opslaget kalder det selv en fordel, ikke et krav. Og "
          "jeg er elautoriseret maskinmester, ikke elinstallatør; titlen skal være rigtig.")

RELOCATION = ("Om arbejdsstedet: jeg bor i Måløv i dag, og Bording er ikke et pendlerforhold, der holder — "
              "jeg flytter til Midtjylland ved ansættelse og er bosat i Ikast-/Herning-området fra starten.")

CULTURE = ("Hvorfor FAGTEK: fireogtyve år i faglokaler er opbygget på sikkerhed, service og dokumentation "
           "— præcis de tre ting Safe·ion skal sælge, og DBI-certificeringen forpligter på dokumentationen. "
           "Når kunderne er kommuner, skoler, rådgivere og installatører, afgøres ordren på, om løsningen "
           "virker i praksis og kan dokumenteres bagefter. Et nyt forretningsområde i en virksomhed med tyve "
           "medarbejdere og flad struktur lykkes ikke ved at indføre tung proces, men ved at beslutte "
           "hurtigt og skrive beslutningen ned.")

PRACTICAL = ("Praktisk: dansk på modersmålsniveau, engelsk professionelt; kørekort B og egen bil til "
             "besigtigelser i hele landet; kan starte hurtigt, og egen virksomhed afvikles ved ansættelse.")

CLOSING = ("Jeg vil gerne høre, hvor Safe·ion står i dag, og bruge første samtale på tre spørgsmål: hvilke "
           "kunder og partnere området skal vokse på, hvordan tilbud og projekter følges op nu, og hvad "
           "området skal kunne om tolv måneder.")

# ------------------------------------------------------------------ CV
PROFILE = ("Rollen kræver fire ting på én gang: elteknisk tyngde, selvstændig projektledelse fra første "
           "kundedialog til aflevering, kommerciel forståelse for tilbud og dækningsgrad og lyst til at "
           "bygge processer op fra bunden. Alle fire har været kerneopgaven i tyve år: egen autoriseret "
           "virksomhed med fuldt P&L-ansvar, egne tilbud og kunder, 37 samtidige anlægsprojekter (2–10 mio. "
           "kr.) hos Novo Nordisk og 14- og 12-mands tekniske teams. Elautoriseret maskinmester (LV/MV/HV), "
           "B.Tech i Technology Management & Mechanical Engineering, dansk på modersmålsniveau.")

PRACTICE = [
    ("Kunde- og partnerarbejde",
     "Opsøgende salg til rådgivere, elinstallatører og bygherrer, fast kontakt og aftalte spilleregler, "
     "pipeline med ansvar og næste skridt pr. navn, opfølgning på faste dage."),

    ("Besigtigelse og teknisk afklaring",
     "Besigtigelsesskabelon for ABA/ABV, kabelføring, tavleplads, bygningsforhold, adgang og "
     "dokumentation; afklaringsnotat med forudsætninger og grensesnit, der bliver tilbudets grundlag."),

    ("Kalkulation og tilbud",
     "Kalkulationsmodel med timer, materialer, underleverandører, risiko og dækningsgrad; tilbud med "
     "forbehold og optioner; prisstrategi og opfølgningsplan."),

    ("Projektledelse og leverance",
     "Projektmodel med faser og gates, materialebestilling, ugentlig fremdriftsstatus, koordinering af "
     "egne teknikere og eksterne parter, test og idriftsættelse, aflevering med dokumentation."),

    ("Økonomi og opfølgning",
     "Timer forbrugt mod kalkuleret, afvigelser og årsager, dækningsgrad pr. projekt, udestående og "
     "prognose; månedlig projektgennemgang og budget i SAP/Excel."),

    ("El-teknisk udførelse",
     "Måling, fejlfinding, tavler og styring, el-tekniske installationer, dokumentation og "
     "afleveringsforretning; elautorisation LV/MV/HV med egenkontrol."),

    ("ABA, belysning og sikkerhed",
     "ABA/ABV, nød- og flugtvejsbelysning, PDS og adgangskontrol i el-installation; arbejde efter "
     "brandtekniske forudsætninger og myndighedskrav, dokumenteret ved aflevering."),

    ("Procesopbygning og værktøj",
     "Procesbibliotek for besigtigelse, tilbud, projekt, aflevering og support; Power BI-tavler, "
     "SharePoint som dokumentbase, Python og Claude til kalkulation, tilbudstekst og rapportering."),
]

FAGTEK_EXTRA = [
    ("Faglokaler og maskiner",
     "Procesudsugning, sløjdmaskiner, gasanlæg og maskiner i faglokaler er driftsteknik med "
     "sikkerhedsmæssige krav: dokumenteret eftersyn, funktionstest, udskiftning og sporbarhed. Opgaverne "
     "løses efter samme model som ABA — besigtigelse, afklaring, tilbud, leverance, aflevering med "
     "dokumentation."),
    ("Gas, udsugning og ventilation",
     "Gasanlæg og udsugning kræver kontrol af kapacitet, føring og sikkerhedsfunktioner, og ventilation "
     "kræver luftmængder, tryk og lyd for at holde. Jeg har projekteret, idriftsat og fejlrettet HVAC og "
     "køl i drift og montage — målt, justeret og dokumenteret, ikke antaget."),
    ("Teknisk dokumentation og rådgivning",
     "Dokumentationen skal kunne læses af en rektor, en driftschef og et eftersyn om fem år: hvad er "
     "installeret, hvilke krav gælder, hvornår er der eftersyn, og hvad er næste handling. Det er den "
     "samme dokumentationspakke, Safe·ion skal levere til installationspartnere."),
    ("Service og support til partnere",
     "Installatører skal kunne ringe til én person og få et svar om teknik, levering eller dokumentation. "
     "Én indgang, aftalte svartider og en sag, der bliver lukket — det er den supportmodel, der gør, at "
     "partnere kommer igen med næste opgave."),
]

FIRST90 = [
    ("Uge 1–2",
     "Kunder, rådgivere, elinstallatører og samarbejdspartnere i Safe·ion gennemgået; de åbne tilbud, "
     "sager og leverancer læst igennem, og de tekniske løsninger set på en besigtigelse — før noget ændres."),
    ("Uge 3–6",
     "Besigtigelses- og afklaringsskabelon samt kalkulationsmodel taget i brug på de næste tilbud; "
     "pipeline oprettet med ansvar og opfølgningsdato; projektmodel med faser og gates aftalt med "
     "driftschefen og teknikerne."),
    ("Uge 7–12",
     "Første projekter leveret efter modellen med afleveringsdokumentation; tilbudsopfølgning kørt fast; "
     "procesbiblioteket på plads i en første version og afprøvet på mindst to sager."),
    ("Måned 3–6",
     "Dækningsgrad og timer-forbrug-til-kalkule gennemgået pr. projekt; Standardtilbud og "
     "dokumentationspakke klar til installationspartnere; kurser i ABA/brandteknik gennemført."),
    ("Måned 6–12",
     "Safe·ion har en egen salgs- og leverancemotor: pipeline med kendte kilder, tilbud der bliver fulgt "
     "op, projekter der leveres ens hver gang og tal, der viser, hvad området tjener."),
    ("Løbende",
     "Månedlig projekt- og økonomigennemgang med ledelsen; kvartalsvis gennemgang af kunder, partnere og "
     "procesbibliotek — og en fast post på dagsordenen for, hvad der skal forenkles næste måned."),
]

MODELS = [
    ("Salg og pipeline",
     "Opsøgende salg til rådgivere og elinstallatører, pipeline med faser og næste skridt, "
     "tilbudsopfølgning på faste dage, kunde- og partnerplan, prisstrategi"),
    ("Besigtigelse og afklaring",
     "Besigtigelsesskabelon, afklaringsnotat med forudsætninger, grensesnitsliste, materialebehov og "
     "arbejdstider, dokumentationskrav"),
    ("Kalkulation og tilbud",
     "Kalkulationsmodel med timer, materialer, underleverandører, risiko og dækningsgrad, "
     "tilbudsskabelon med forbehold og optioner"),
    ("Projektmodel",
     "Faser og gates, ordre og materialebestilling, ugentlig fremdriftsstatus, koordinering af teknikere "
     "og eksterne parter, ændringshåndtering og dokumenteret beslutningslog"),
    ("Aflevering og kvalitet",
     "Test og idriftsættelse, afleveringscheckliste, dokumentationspakke, overlevering til kunde og "
     "support til installationspartnere, 1- og 5-års gennemgang"),
    ("Økonomi",
     "Timer mod kalkule, dækningsgrad pr. projekt, udestående og prognose, månedlig projektgennemgang, "
     "budget og SAP/Excel-modeller"),
    ("El og ABA",
     "ABA/ABV, nød- og flugtvejsbelysning, tavler og styring, PDS, fejlfinding og idriftsættelse, "
     "DS/HD 60364, dokumentation efter brandtekniske forudsætninger"),
    ("Processer og værktøj",
     "Procesbibliotek og skabeloner, Lean-principper (PDCA, 5S, A3), Power BI-tavler, SharePoint som "
     "dokumentbase, Python og Claude til kalkulation og rapportering"),
]

ACHIEVEMENTS = [
    ("Egen autoriseret virksomhed med fuldt P&L-ansvar",
     "egne tilbud, kalkulation, prissætning, indkøb og kunder — 5 elektrikere og 3 lærlinge, 40+ "
     "serviceanlæg i Storkøbenhavn."),
    ("37 samtidige anlægsprojekter, 2–10 mio. kr.",
     "fra teknisk afklaring og tilbud til aflevering hos Novo Nordisk — plan, økonomi og dokumentation."),
    ("Nul kritiske afvigelser ved aflevering",
     "FAT/SAT, IQ/OQ/PQ og valideringsdokumentation med afvigelseshåndtering."),
    ("+40 % produktivitet",
     "gennem dataunderstøttet planlægning, standardiseret arbejde og egen AI-tooling — målt og "
     "fastholdt over tid."),
    ("−40 % energikost",
     "på 24/7-anlæg gennem PDCA, måling og standardiseret arbejde — forbedringer, der blev i driften."),
]

EXPERIENCE = [
    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, tilbud, kunder og leverandører",
     [("Salg og tilbud",
       "kundedialog, besigtigelse, kalkulation og tilbud på el-, tavle- og styringsopgaver samt "
       "serviceaftaler; opfølgning til underskrift."),
      ("Projekt og leverance",
       "projekter fra ordre til aflevering med plan, materialebestilling, koordinering af egne teknikere "
       "og underleverandører samt dokumentation."),
      ("Økonomi",
       "budget og prognose, indkøb og leverandøraftaler, prissammenligning og fuldt ansvar for bundlinjen."),
      ("Drift og akutte hændelser",
       "planlagt og afhjælpende vedligehold, fejlfinding på el, tavler, styring, ventilation og klima.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister inden for teknik, indkøb og drift · "
     "GMP/FDA/EMA",
     [("Projektledelse",
       "tidsplan, økonomi, risiko og månedlig rapportering til ledelse og kunde; ændringer håndteret med "
       "beslutningslog."),
      ("Tværfaglig koordinering",
       "25 specialister på tværs af mekanik, el, proces og indkøb — grensesnit aftalt, før arbejdet blev "
       "sat i gang."),
      ("Aflevering og dokumentation",
       "FAT/SAT, IQ/OQ/PQ og valideringsdokumentation med afvigelseshåndtering — nul kritiske fund.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Leverance og kapacitet",
       "kapacitetsplanlægning, flowstyring og daglige tavlemøder over 11 samtidige projekter."),
      ("Kvalitet og sikkerhed",
       "standardiseret arbejde, arbejdstilladelser og dokumentation ved montage i aktive bygninger.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · budgetter i SAP",
     [("Vedligehold og KPI",
       "PDCA-baseret plan med fast årshjul, A3-root-cause på nedetid og KPI'er i SAP ERP."),
      ("Leverandører og entreprenører",
       "koordinering af egne teknikere, entreprenører og leverandører — adgang, sikkerhed og "
       "arbejdstilladelser.")]),

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

LANGUAGES = "Dansk (modersmål, skrift og tale) · Engelsk (professionelt, skriftligt og mundtligt) · Persisk/farsi · Kørekort B"

REFERENCES = "Tidligere ledere og kunder hos Biofos (Lynetten), Novo Nordisk A/S (Kalundborg) og egne kunder i ELOHVAC — oplyses ved henvendelse."

KEYWORDS = (
    "Elteknisk Projektleder · Projektleder · Safe·ion · FAGTEK · ABA · Brandsikring · Brandalarm · "
    "AWEX · Nød- og flugtvejsbelysning · ABV · Elteknisk · Elteknik · Elektriker · "
    "Maskinmester · Elektronikfagtekniker · El · VVS · Tekniske installationer · Besigtigelse · "
    "Teknisk afklaring · Kalkulation · Tilbud · Tilbudsopfølgning · Leads · Kunder · Rådgivere · "
    "Samarbejdspartnere · Ordre · Aflevering · Koordinering · Teknikere · Fremdrift · Kvalitet · "
    "Økonomisk opfølgning · Dækningsgrad · Projektøkonomi · Forretningsudvikling · Kommerciel · "
    "Vækst · Processer · Arbejdsgange · Samarbejdsformer · Ejerskab · Selvstændig · Frihed under "
    "ansvar · Struktureret · Analytisk · Initiativ · Samarbejdsorienteret · Service · Sikkerhed · "
    "Vedligeholdelse · Dokumentation · Procesudsugning · Sløjdmaskiner · Gasanlæg · Ventilation · "
    "Maskiner · Faglokaler · Uddannelsesinstitutioner · Projektering · Rådgivning · Support · "
    "Bording · Midtjylland · Dansk"
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

    for t in (MIRROR, HONEST, RELOCATION, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=55)

    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROJEKTPROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("PROJEKT- OG FORRETNINGSMETODER — ANVENDT I PRAKSIS",
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

    m.section("REFERENCER")
    m.para(REFERENCES, after=80, justify=False)

    m.section("BIDRAG TIL FAGTEKS ØVRIGE TEKNISKE PROJEKTER")
    for label, body in FAGTEK_EXTRA:
        m.bullet(label, body, after=30)

    m.section("KERNEKOMPETENCER & NØGLEORD")
    m.para(KEYWORDS, after=80)

    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER SAFE·ION I DRIFT",
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
                  title="Ansøgning og CV — Elteknisk Projektleder, Safe·ion / FAGTEK",
                  subject="ABA og brandsikring · projektledelse fra kundedialog til aflevering · "
                          "tilbud og projektøkonomi",
                  keywords=("elteknisk projektleder, projektleder, safe·ion, fagtek, aba, brandalarm, "
                            "awex, nød- og flugtvejsbelysning, elteknik, besigtigelse, kalkulation, "
                            "tilbud, projektøkonomi, dansk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1 (krav → løsning), CV side 2-4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_FAGTEK_EltekniskProjektleder.docx")
    print("OK", build(out))
