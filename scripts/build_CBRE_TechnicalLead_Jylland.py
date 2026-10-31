# -*- coding: utf-8 -*-
"""
CBRE Global Workplace Solutions — Technical Lead, Jylland.
Job ID 300246 · GWS Segment · Facilities Management · Aarhus/Midtjylland.
Dansk JD. Bygget i designet fra master-CV'erne og efter den bindende regel:
dokumentet handler om opgaven, missionen og stillingen — ikke om ansøgeren.
Side 1 = "Kravet → Løsningen er" + "Systemet er allerede bygget".
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Technical Lead | CBRE GWS | Jylland"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (flytter til Jylland)")

DATE = "31. oktober 2026"
RECIPIENT = ("CBRE Global Workplace Solutions · GWS Segment · Aarhus · Facilities Management · "
             "Att.: Nino Selmeczi, ansættende leder · Job ID 300246")
SUBJECT = "Ansøgning: Technical Lead med ansvar i Jylland (Job ID 300246)"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Opgaven er enkel at beskrive og svær at gøre godt: en portefølje af industri-, lager- og "
    "logistikejendomme i Jylland, hvor nogen skal se bygningen, før lejeren ringer. Det er faste "
    "runderinger, indmeldte opgaver, leverandører der skal have adgang og lukkes ordentligt af, og en "
    "dokumentation der gør, at en sag ikke forsvinder mellem to telefoner. Rollen er ikke teknisk tung "
    "— den er koordinerende, og kvaliteten ligger i opfølgningen.",

    "Nedenfor er min læsning af stillingen og det system, der ligger klar til at tage den: en mobil "
    "arbejdsdag med runderingsplan pr. ejendom, én opgaveliste med ejer og frist, fast lejerdialog og en "
    "statusrapport, der kan læses på ét blik.",
]

BULLETS = [
    ("Kravet: planlagte runderinger på flere lokationer",
     "Løsningen er en runderingsplan bygget på ejendomstype og kritikalitet: frekvens pr. ejendom, "
     "ruter der følger geografien, og en digital tjekliste pr. område — bygning, fællesarealer, "
     "adgangsveje, udendørsarealer, skiltning og belysning — med foto og note pr. observation, så "
     "rapporten skriver sig selv bagefter."),

    ("Kravet: registrere fejl, mangler og observationer og sikre opfølgning",
     "Løsningen er én opgaveliste for alle ejendomme med kilde, ansvarlig, frist og lukning med "
     "årsag. Intet lukkes uden dokumentation, og hver uge gennemgås de åbne sager, så ingen opgave "
     "bliver hængende, fordi den skiftede hænder."),

    ("Kravet: henvendelser fra lejere og professionel kommunikation",
     "Løsningen er én indgang og et fast svar: kvittering samme dag, hvem der har opgaven, og hvornår "
     "der er nyt. Lejeren skal ikke ringe to steder — og når opgaven skifter ejer undervejs, får "
     "lejeren besked, før han spørger."),

    ("Kravet: koordinere håndværkere, servicepartnere og leverandører",
     "Løsningen er et leverandørkort pr. ejendom: adgang og nøgler, sikkerhedsinstruks, "
     "arbejdstilladelse, kontaktperson og hvad der sidst blev udført. Adgang logges, og aftalt arbejde "
     "følges op med foto og en kort afmeldingsnote, så kunden kan se, at det blev gjort."),

    ("Kravet: mindre praktiske driftsopgaver og vurdering af, hvornår en fagperson skal til",
     "Løsningen er en grænse, der er defineret på forhånd: hvad løses på stedet, og hvad kræver "
     "autorisation eller en specialiseret fagperson. Praktisk forståelse for el, VVS, ventilation og bygninger "
     "betyder, at en opgave bliver beskrevet rigtigt første gang, den skal sendes videre — ikke "
     "sendt rundt mellem tre håndværkere."),
]

SYSTEM = ("Systemet er allerede bygget: runderingsskabelon pr. ejendomstype, tjeklister pr. område, "
          "opgaveliste med ejer, frist og foto, leverandørkort med adgang og sikkerhed, standard svar "
          "til lejere, checklister til ind- og fraflytning og en ugerapport pr. ejendom. Oven i det en "
          "rutine, hvor Python og Claude samler status og åbne sager fra de data, der allerede ligger i "
          "systemet — så tiden går på ejendommene og ikke på at skrive rapporter.")

MIRROR = ("Om kravene: erfaring fra ejendomsservice, drift af erhvervsejendomme og facility management "
          "med mobil arbejdsdag på 40+ serviceanlæg; praktisk anlagt og service over for kunder og lejere i "
          "egen virksomhed; arbejder selvstændigt, struktureret og kan planlægge og prioritere besøg på "
          "flere lokationer; koordinering og dokumentation af åbne opgaver; dansk flydende og engelsk "
          "professionelt; MS Office, SAP, CMMS og digitale opgavestyringssystemer i daglig brug; kørekort "
          "til personbil — og flytning til Jylland, så udgangspunktet er lokalt fra dag et.")

HONEST = ("To ting påvirker opgaven og skal siges ligeud: jeg bor i Måløv i dag og flytter til "
          "Jylland — rollen kan ikke køres fra Sjælland, og jeg vil være bosat i Aarhus-området fra "
          "starten. Og jeg kommer med mere teknisk og ledelsesmæssig baggrund, end rollen kræver; det er "
          "et bevidst valg. Jeg vil tættere på driften og lejerne, og fagligheden skal bruges til at "
          "vurdere, hvornår en opgave skal videre til en specialist — ikke til at løse alt selv.")

CULTURE = ("Hvorfor CBRE: RISE — Respect, Integrity, Service, Excellence — lægger vægten på Service, og "
           "det er netop den del, kunden mærker: at bygningen fremstår sikker, funktionel og "
           "præsentabel, og at der bliver fulgt op. Ambitionen om en ensartet og professionel service på "
           "tværs af ejendommene er samtidig en systemdisciplin: de samme tjeklister, den samme "
           "opfølgning og den samme rapportering på hver lokation.")

PRACTICAL = ("Praktisk: kørekort til personbil og egen bil, klar til den mobile hverdag; dansk på "
             "modersmålsniveau og engelsk professionelt; bosætter mig i Aarhus-området fra start; kort "
             "opsigelse og klar til hurtigt start. Egen virksomhed afvikles ved ansættelse.")

CLOSING = ("Jeg vil gerne høre, hvordan ejendommene i Jylland styres i dag, og bruge den første samtale på "
           "tre spørgsmål: hvor mange lokationer runderingen dækker, hvordan opgaver registreres og "
           "lukkes nu, og hvad kunden ser som en god måned.")

# ------------------------------------------------------------------ CV
PROFILE = ("Rollen kræver fire ting på én gang: overblik over flere ejendomme og lokationer, en fast "
           "runderings- og opfølgningsrytme, professionel kontakt med lejere og leverandører, og "
           "dokumentation der gør, at ingen opgave forsvinder. Alle fire har været en del af arbejdet i "
           "tyve år — med en mobil hverdag på 40+ serviceanlæg i egen autoriseret virksomhed, "
           "leverandør- og entreprenørstyring på et 24/7-site hos Biofos Lynetten og dokumenteret "
           "aflevering af 37 samtidige anlægsprojekter hos Novo Nordisk. Elautoriseret maskinmester "
           "(LV/MV/HV), B.Tech i Technology Management & Mechanical Engineering, SAP og CMMS i drift, "
           "dansk på modersmålsniveau og engelsk professionelt.")

PRACTICE = [
    ("Runderinger og tilsyn",
     "Runderingsplan pr. ejendom med frekvens og rute; tjeklister pr. område — bygning, "
     "fællesarealer, adgangsveje, udendørs, skiltning, belysning, porte og døre; foto og note pr. "
     "observation, så status er dokumenteret, før den bliver efterspurgt."),

    ("Opgaver, opfølgning og dokumentation",
     "Én opgaveliste for alle lokationer med kilde, ansvarlig, frist og lukning med årsag; ugentlig "
     "gennemgang af åbne sager; statusrapport pr. ejendom og en samlet ugerapport til kunden."),

    ("Lejere og kundekontakt",
     "Én indgang til driften, kvittering samme dag, tydelig forventning til tid og næste skridt, og "
     "besked når opgaven skifter ejer — så lejeren oplever fremdrift frem for at skulle spørge igen. "
     "Samarbejde med kundens kontaktpersoner om prioritering og opfølgning."),

    ("Leverandører og adgang",
     "Leverandørkort pr. ejendom med adgang, nøgler, sikkerhedsinstruks og arbejdstilladelse; "
     "adgangslog; afmeldingsnote og foto ved afsluttet arbejde, så aftaler kan dokumenteres over for "
     "kunden."),

    ("Mindre praktiske driftsopgaver",
     "Reparationer og justeringer på stedet inden for egen formåen og sikkerhed; tydelig grænse til det, "
     "der kræver autorisation eller en specialiseret fagperson, så opgaven beskrives rigtigt første "
     "gang."),

    ("Serviceydelser og årshjul",
     "Opfølgning på rengøring, grønne områder, vintertjeneste og affald mod aftalte serviceniveauer; "
     "årshjul for eftersyn og sæsonopgaver, så vintertjeneste og udendørsarbejde er bestilt før "
     "sæsonen."),

    ("Akutte hændelser på en lokation",
     "Første handling er at sikre mennesker og adgang, derefter at få den rette fagperson på stedet og "
     "orientere lejer og kunde samme dag. Skaden lukkes med foto og årsag, så den samme hændelse ikke "
     "gentages næste vinter."),

    ("Ensartet service på tværs af ejendommene",
     "De samme tjeklister, den samme opfølgning og den samme rapportering på hver lokation — så "
     "kvaliteten ikke afhænger af, hvem der tilfældigvis var forbi. Nye lokationer kommer i drift efter "
     "samme skabelon."),

    ("Ind- og fraflytninger",
     "Checkliste og registrering ved ind- og fraflytninger: målerstande, nøgler og adgang, besigtigelse, "
     "skader og udbedring koordineret med leverandør og kunde."),
]

FIRST90 = [
    ("Uge 1–2",
     "Alle lokationer besøgt sammen med den nuværende driftsansvarlige; lejere og kundens "
     "nøglekontakter mødt; åbne sager, leverandøraftaler og adgangsforhold kortlagt, før noget ændres."),
    ("Uge 3–6",
     "Runderingsplan og ruter lagt fast pr. ejendom, tjeklister tilpasset industri-, lager- og "
     "logistikejendomme, og opgaveliste med ejer og frist taget i brug på alle lokationer."),
    ("Uge 7–12",
     "Leverandørkort og adgangsprocedure indført; standard svar til lejere og forventet responstid "
     "aftalt med kunden; første månedsrapport med åbne og lukkede sager samt gentagne fejl."),
    ("Måned 3–6",
     "Ensartet service på tværs af ejendommene dokumenteret med de samme tjeklister; rengøring, grønne "
     "områder, vintertjeneste og affald evalueret mod aftalen; to-tre forbedringer gennemført med "
     "målbar effekt på responstid og gentagne opgaver."),
    ("Måned 6–12",
     "Planen kører uden daglig styring, og data bruges aktivt: runderinger flyttes efter behov, "
     "leverandørindsatsen justeres efter gentagne fejl, og kunden ser færre overraskelser på "
     "ejendommene."),
    ("Måned 12+",
     "Årshjulet for eftersyn, vintertjeneste og udendørsarbejde planlagt et år frem; leverandøraftaler og "
     "serviceniveauer evalueret på data; og en standard for, hvordan en ny lokation kommer i drift uden at "
     "opfinde proceduren igen."),
]

MODELS = [
    ("Rundering & tilsyn",
     "Runderingsplan pr. ejendom, ruteoptimering på tværs af lokationer, tjeklister pr. område, "
     "foto- og notedokumentation, sæsonbaserede eftersyn"),
    ("Opgavestyring",
     "Én opgaveliste med ejer og frist, prioritering efter sikkerhed og lejerpåvirkning, lukning med "
     "årsag, ugentlig gennemgang af åbne sager"),
    ("Lejer & kunde",
     "Én indgang, kvittering og forventningsafstemning, status ved ejerskifte af opgaven, fast "
     "mødekadence med kundens kontaktperson"),
    ("Leverandør & adgang",
     "Leverandørkort, adgangs- og nøglelog, sikkerhedsinstruks og arbejdstilladelse, afmelding med foto, "
     "opfølgning på serviceniveau"),
    ("Serviceydelser",
     "Rengøringskontrol, grønne områder, vintertjeneste, affaldshåndtering, ind- og fraflytningscheckliste"),
    ("Dokumentation & rapportering",
     "Statusrapport pr. ejendom, ugerapport til kunden, Power BI-dashboard, Excel-modeller, "
     "Python og Claude til automatiseret sammenstilling af status og åbne sager"),
    ("Systemer & IT",
     "CMMS og SAP, digitale opgavestyringssystemer, Microsoft Office og Excel, SharePoint som "
     "dokumentbase, mobile tjeklister"),
    ("Økonomi i driften",
     "Budgetopfølgning pr. ejendom, prissammenligning på serviceydelser, godkendelse af udført arbejde "
     "mod aftale, opfølgning på fakturaer og afvigelser"),
    ("Sikkerhed & adfærd",
     "APV og risikovurdering, arbejdstilladelser, sikker adfærd ved leverandørarbejde, "
     "near-miss-opfølgning, adgangskontrol på aktive ejendomme"),
]

ACHIEVEMENTS = [
    ("Mobil hverdag på 40+ anlæg",
     "daglig prioritering mellem adresser i Storkøbenhavn — samme arbejdsform som en portefølje i "
     "Jylland."),
    ("Én indgang for kunderne",
     "tilbud, aftaler og opfølgning i egen virksomhed; kunden har ét nummer og får svar samme dag."),
    ("37 samtidige anlægsprojekter",
     "2–10 mio. kr. hos Novo Nordisk — dokumentation og aflevering uden kritiske fund."),
    ("Leverandør- og entreprenørstyring",
     "kravspecifikation, adgang og sikkerhed på 24/7-site (Biofos) samt kontrol af udført arbejde."),
    ("+40 % produktivitet",
     "gennem standardiserede tjeklister, dataunderstøttet planlægning og egen AI-tooling — målt over "
     "tid."),
    ("Nul uplanlagte stop på 24/7-anlæg",
     "fem år med pumper, HVAC, koblingsanlæg og SCADA — oppetid gennem forebyggende vedligehold og "
     "hurtig fejlfinding."),
    ("Tjeklister og rapporter som system",
     "samme skabelon pr. ejendomstype og automatisk sammenstilling af status — så rapportering tager "
     "minutter, ikke en arbejdsdag."),
]

EXPERIENCE = [
    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "40+ serviceanlæg i Storkøbenhavn · 5 elektrikere og 3 lærlinge · fuldt P&L og leverandøraftaler",
     [("Mobil drift på flere adresser",
       "planlagt og afhjælpende vedligehold med daglig prioritering mellem anlæg; fejlfinding på el, "
       "tavler, styring, ventilation og klima."),
      ("Kunder og opfølgning",
       "tilbud, prissætning og aftaler med kunderne; én indgang, kvittering samme dag og opfølgning "
       "indtil opgaven er lukket."),
      ("Systemer og dokumentation",
       "ERP-baseret ordre- og reservedelsstyring, tjeklister, Power BI og Python/Claude-værktøjer til "
       "status og rapportering."),
      ("Leverandører og indkøb",
       "indkøb af komponenter og serviceydelser, prissammenligning og aftaler; fuldt ansvar for "
       "bundlinjen.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · drifts- og "
     "vedligeholdelsesbudgetter i SAP",
     [("Leverandører og entreprenører",
       "adgang, sikkerhed og arbejdstilladelser på et aktivt anlæg; koordinering af egne teknikere, "
       "entreprenører og leverandører."),
      ("Vedligeholdsplan og opfølgning",
       "PDCA-baseret vedligeholdsplan med fast årshjul, A3-root-cause på større nedetid og KPI'er i "
       "SAP ERP."),
      ("Sikkerhed og arbejdsmiljø",
       "LOTO, risikovurdering, arbejdstilladelser, near-miss-rapportering og værktøjsmøder.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister inden for teknik, indkøb og drift · "
     "GMP/FDA/EMA",
     [("Koordinering på tværs",
       "25 specialister på tværs af mekanik, el, proces og indkøb; beslutninger dokumenteret, så alle "
       "arbejdede efter samme aftale."),
      ("Dokumentation og aflevering",
       "FAT/SAT, IQ/OQ/PQ og valideringsdokumentation med afvigelseshåndtering — nul kritiske fund."),
      ("Projekt og økonomi",
       "tidsplan, økonomi, risiko og månedlig rapportering til ledelse og kunde.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Montage i aktive bygninger",
       "koordinering af håndværkere og adgang i bygninger, hvor driften kørte videre."),
      ("Kvalitet og sikkerhed",
       "standardiseret arbejde, arbejdstilladelser og sikkerhedsdokumentation ved hver station.")]),

    ("Elektromekaniker / Produktionsteamleder",
     "ARJ Engineering · Teheran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · skiftplanlægning, materialestyring og lager",
     [("Praktisk problemløsning",
       "reparation og diagnosticering af elektriske og mekaniske systemer gennem struktureret "
       "root cause-analyse."),
      ("Planlægning",
       "skiftplanlægning, materialestyring og opfølgning på mål.")]),
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

REFERENCES = "Tidligere ledere og kunder hos Biofos (Lynetten), Novo Nordisk A/S (Kalundborg) og egne kunder i ELOHVAC — oplyses ved henvendelse."

KEYWORDS = (
    "Technical Lead · Ejendomsservice · Facility Management · FM · Viceværtservice · Drift af "
    "Erhvervsejendomme · Ejendomsdrift · Runderinger · Tilsyn · Lejere · Kunde · Leverandører · "
    "Servicepartnere · Håndværkere · Adgang · Sikkerhed · Opfølgning · Registrere · Dokumentation · "
    "Koordinere · Opgavestyring · Statusrapportering · Åbne Opgaver · Ind- og Fraflytning · Rengøring · "
    "Grønne Områder · Vintertjeneste · Affald · Serviceydelser · Bygninger · Fællesarealer · "
    "Adgangsveje · Udendørsområder · Porte · Døre · Belysning · Skiltning · Belægninger · "
    "Fælles Installationer · Industri · Lager · Logistik · Ejendomme · Portefølje · Lokationer · "
    "Serviceminded · Proaktiv · Løsningsorienteret · Selvstændig · Struktureret · Fremdrift · "
    "Praktisk Forståelse · IT-Kundskaber · MS Office · Excel · Digitale Opgavestyringssystemer · CMMS · "
    "SAP · SharePoint · Power BI · Kørekort · Jylland · Aarhus · Midtjylland · Dansk · Engelsk · "
    "GWS Segment · CBRE · RISE"
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
        m.para(t, after=60)

    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("ARBEJDSMETODER & VÆRKTØJER — ANVENDT I PRAKSIS",
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

    m.section("KERNEKOMPETENCER & NØGLEORD")
    m.para(KEYWORDS, after=80)

    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER EJENDOMMENE I DRIFT",
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
                  title="Ansøgning og CV — Technical Lead, CBRE GWS Jylland",
                  subject="Ejendomsdrift · runderinger · lejere og leverandører · dokumentation og "
                          "opfølgning · Jylland",
                  keywords=("technical lead, ejendomsservice, facility management, runderinger, lejere, "
                            "leverandører, opfølgning, dokumentation, ms office, opgavestyring, kørekort, "
                            "jylland, dansk, engelsk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1 (krav → løsning), CV side 2-4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_CBRE_TechnicalLead_Jylland.docx")
    print("OK", build(out))
