# -*- coding: utf-8 -*-
"""
CBRE Global Workplace Solutions — Technical Manager, Aarhus.
Job ID 300765 · GWS Segment · Facilities Management · Aarhus/Midtjylland.
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
TITLE = "Technical Manager | CBRE GWS | Aarhus"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (flytter til Aarhus-området)")

DATE = "31. oktober 2026"
RECIPIENT = ("CBRE Global Workplace Solutions · GWS Segment · Aarhus · Facilities Management · "
             "Job ID 300765")
SUBJECT = "Ansøgning: Technical Manager — Aarhus (Job ID 300765)"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Opgaven er den tekniske drift af en kundes sites fra Nordjylland til Slagelse — mange "
    "lokationer, spredt geografi og et ansvar, der kun består, hvis hver installation har en plan og "
    "hver opgave har en ejer. Det er forebyggende vedligehold, der bliver gennemført før fejlen, "
    "underleverandører der bliver styret og ikke bare bestilt, lovpligtige eftersyn der aldrig løber "
    "over, og en KPI-rapport der kan læses af både kunden og Contract Manager.",

    "Nedenfor er min læsning af stillingen og det system, der ligger klar til at tage den: "
    "site-portefølje med kritikalitet, vedligeholdsplan med årshjul, leverandørmatrix med "
    "serviceniveauer og en rapportering, der bygger på registreringer frem for på husk.",
]

BULLETS = [
    ("Kravet: teknisk nøgleperson for kunden — og stabil drift på tværs af sites",
     "Løsningen er et site-porteføljekort pr. lokation: hvilke installationer der er kritiske for "
     "kundens drift, deres alder og tilstand, hvad der kræver årligt eftersyn, og hvad der skal være "
     "på lager. Kritikalitet styrer runderingsfrekvens og responstid — ikke omvendt — så indsatsen "
     "lægges der, hvor et stop koster mest."),

    ("Kravet: planlægge og følge op på forebyggende og afhjælpende vedligehold",
     "Løsningen er en PDCA-baseret vedligeholdsplan med fast årshjul i CMMS: arbejdsordrer med "
     "frister, udførte opgaver lukket med årsag og dokumentation, og A3-root-cause når den samme fejl "
     "kommer igen. Afhjælpende opgaver registreres, så de bliver statistik og ikke bare historie."),

    ("Kravet: koordinere og styre underleverandører og serviceaftaler",
     "Løsningen er en leverandørmatrix pr. site: aftalt serviceniveau, responstid, pris, adgang, "
     "sikkerhedsinstruks og dokumentation. Leverandøren afmelder med foto og note, og faktura "
     "afstemmes mod det udførte arbejde — så en serviceaftale bliver en målt leverance, ikke et "
     "abonnement."),

    ("Kravet: teknisk sparringspartner for kunde og team",
     "Løsningen er faglig dybde i el, VVS og ventilation: elautoriseret maskinmester (LV/MV/HV), "
     "tavler, nødstrøm, CTS, varme, køl og ventilation, suppleret med AMU i køle- og HVAC-teknik. Det "
     "gør det muligt at kvalificere en opgave, før den sendes videre — og at sige nej til en løsning, "
     "der ikke holder om to år."),

    ("Kravet: lovkrav, myndighedskrav, sikkerhed — og KPI-rapportering med forbedringer",
     "Løsningen er en compliance-matrix pr. site: hvilke anlæg der kræver hvilke eftersyn og hvilken "
     "dokumentation, med udløbsdatoer og ansvarlig. Oven på den en KPI-tavle med oppetid, responstid, "
     "gentagne fejl og energiforbrug, som rapporteres månedligt og bruges til at identificere "
     "forbedrings- og optimeringsmuligheder, så tallene flytter indsatsen."),
]

SYSTEM = ("Systemet er allerede bygget: site-porteføljekortet, vedligeholdsplanen med årshjul og "
          "arbejdsordrer, compliance-matrixen med eftersyn og udløbsdatoer, leverandørmatrixen med "
          "serviceniveauer og afmeldingskontrol, KPI-tavlen i Power BI og den mobile dagsplan, der "
          "lægger ruten mellem lokationerne efter kritikalitet og aftalte besøg. Oven i det en rutine, "
          "hvor Python og Claude samler status og afvigelser fra CMMS og Excel — så tiden går på "
          "sites og ikke på at skrive rapport.")

MIRROR = ("Om kravene: teknisk baggrund — opslaget peger på maskinmester eller el-installatør, og jeg er "
          "elautoriseret maskinmester (LV/MV/HV) med B.Tech i Technology Management & Mechanical "
          "Engineering; erfaring med teknisk "
          "drift, ejendomsdrift og facility management gennem tyve år, senest med 40+ serviceanlæg og "
          "fuldt P&L-ansvar; solid erfaring med el, VVS og ventilation; selvstændig, løsningsorienteret "
          "og vant til mange bolde i luften; dansk på modersmålsniveau og engelsk professionelt; "
          "kørekort B og egen bil.")

HONEST = ("To ting påvirker opgaven og skal siges ligeud: jeg bor i Måløv i dag og flytter til "
          "Aarhus-området — en portefølje fra Nordjylland til Slagelse kan ikke styres fra Sjælland. Og "
          "min driftserfaring er bygget op i kundens egen organisation og i egen virksomhed, ikke inde i "
          "en FM-udbyder; systemerne og fagligheden er de samme, men CBRE's processer, økonomimodel og "
          "rapporteringskrav skal læres — det gør man ved at gå med ud på sites de første uger.")

CULTURE = ("Hvorfor CBRE: RISE — Respect, Integrity, Service, Excellence — passer til en rolle, hvor "
           "man repræsenterer kunden på dennes egne lokationer, og hvor tillid er det, der gør, at en "
           "fejl bliver meldt i tide. Og formuleringen om løsninger, der virker i praksis, er præcis "
           "den standard, teknisk drift skal måles på: ikke hvad der står i aftalen, men hvad der "
           "faktisk kører på site mandag morgen.")

PRACTICAL = ("Praktisk: kørekort B og egen bil, og vant til en mobil hverdag med kørsel mellem "
             "adresser; dansk på modersmålsniveau og engelsk professionelt; bosat i Jylland — nærmere "
             "bestemt Aarhus-området — fra start; kort opsigelse og klar til hurtigt start. Egen "
             "virksomhed afvikles ved ansættelse.")

CLOSING = ("Jeg vil gerne høre, hvordan porteføljen styres i dag, og bruge den første samtale på tre "
           "spørgsmål: hvilke sites og installationer der er kritiske for kunden, hvor de fleste "
           "afhjælpende opgaver kommer fra, og hvilke KPI'er Contract Manager bliver målt på.")

# ------------------------------------------------------------------ CV
PROFILE = ("Rollen kræver fire ting på én gang: teknisk dybde i el, VVS og ventilation, en "
           "vedligeholdsplan der bliver gennemført på mange lokationer, styr på underleverandører og "
           "serviceaftaler, og dokumentation nok til at lovkrav og KPI'er holder. Alle fire har været "
           "kerneopgaven i tyve år — med 40+ serviceanlæg og fuldt P&L-ansvar i egen autoriseret "
           "virksomhed, 24/7-drift med SAP og KPI'er på Biofos Lynetten og 37 samtidige anlægsprojekter "
           "hos Novo Nordisk. Elautoriseret maskinmester (LV/MV/HV), B.Tech i Technology Management & "
           "Mechanical Engineering, dansk på modersmålsniveau og engelsk professionelt.")

PRACTICE = [
    ("Teknisk drift på flere sites",
     "Site-portefølje med kritikalitet og tilstand; runderings- og responstid styret efter, hvad et "
     "stop koster kunden; ensartede tjeklister og registrering på hver lokation, så status er "
     "sammenlignelig på tværs af sites."),

    ("Forebyggende og afhjælpende vedligehold",
     "PDCA-baseret vedligeholdsplan med årshjul og arbejdsordrer i CMMS; lovpligtige eftersyn bundet "
     "til anlæg og dato; A3-root-cause og fem-hvorfor på gentagne fejl; reservedelsflow og kritiske "
     "lagre."),

    ("Underleverandører og serviceaftaler",
     "Leverandørmatrix med serviceniveau, responstid og pris; adgang, sikkerhedsinstruks og "
     "arbejdstilladelse på aktive sites; afmelding med foto og afstemning af faktura mod udført "
     "arbejde."),

    ("Lovkrav, myndighedskrav og sikkerhed",
     "Compliance-matrix pr. site med eftersyn, dokumentation og udløbsdatoer; APV og risikovurdering, "
     "LOTO og sikringsprocedurer, entreprenørkontrol og near-miss-opfølgning."),

    ("KPI, rapportering og optimering",
     "Oppetid, responstid, gentagne fejl, energiforbrug og omkostning pr. site i Power BI; månedlig "
     "rapportering til Contract Manager og kunde; forbedringskandidater udpeget på data — energi, "
     "kritikalitet og reservedelsforbrug."),

    ("Projekter og teknisk udvikling",
     "Teknisk sparring på større projekter: kravspecifikation, FAT/SAT og aflevering med dokumentation; "
     "37 samtidige anlægsprojekter på 2–10 mio. kr. gennemført uden kritiske fund."),

    ("Kundemøder og rapportering",
     "Fast mødekadence med kundens kontaktpersoner: status på åbne sager, kommende eftersyn, "
     "økonomi og de forbedringer der er gennemført — kort nok til at blive læst, konkret nok til at "
     "blive brugt."),

    ("Mobil hverdag og planlægning",
     "Ruteplanlægning mellem lokationer, prioritering når flere sager haster, og fjernsupport hvor "
     "opgaven kan løses uden kørsel — så rejsetiden bliver brugt på de sites, hvor den gør en "
     "forskel."),
]

FIRST90 = [
    ("Uge 1–2",
     "Alle sites besøgt med den nuværende tekniske ansvarlige; kundens nøglepersoner mødt; åbne "
     "arbejdsordrer, serviceaftaler og compliance-status gennemgået, før noget ændres."),
    ("Uge 3–6",
     "Site-porteføljekort og compliance-matrix etableret for hele porteføljen; vedligeholdsplanen lagt i "
     "årshjul med udløbsdatoer; leverandørmatrix med serviceniveauer på plads for de væsentligste "
     "aftaler, og de aftaler der ikke kan dokumenteres, sat i gang med en plan."),
    ("Uge 7–12",
     "KPI-tavle med baseline for oppetid, responstid og gentagne fejl; månedlig rapport i fast form til "
     "Contract Manager og kunde; de første afhjælpende sager lukket med årsag og dokumentation."),
    ("Måned 3–6",
     "Forebyggende andel af arbejdsordrerne øget, og gentagne fejl faldet; to-tre "
     "optimeringskandidater gennemført med målbar effekt på energi eller responstid; leverandøraftaler "
     "gennemgået på pris og leverance, og kritiske reservedele lagt på lager efter kritikalitet."),
    ("Måned 6–12",
     "Porteføljen kører på plan uden daglig styring; compliance uden overskridelser; kunden ser stabil "
     "drift og færre overraskelser, og forbedringerne er dokumenteret med før/efter-tal."),
    ("Måned 12+",
     "Årshjulet ruller et år frem med investeringsbehov dokumenteret pr. site; energiforbrug og "
     "kritikalitet bruges til at prioritere næste års indsats — og en ny lokation kan onboardes uden at "
     "opfinde proceduren igen."),
]

MODELS = [
    ("Vedligehold & drift",
     "Forebyggende vedligeholdsplan og årshjul, lovpligtige eftersyn, kritikalitetsvurdering, "
     "arbejdsordrer i CMMS, reservedelsflow og kritiske lagre, A3-root-cause og fem-hvorfor"),
    ("Installationer",
     "El, tavler og koblingsanlæg, LV/MV/HV, nødstrøm og UPS, VVS, ventilation og klima, varme og køl, "
     "brand-anlæg, CTS/BMS, trykluft, elevatorgrænseflader"),
    ("Leverandørstyring",
     "Serviceniveau og SLA, responstid og eskalation, adgang og arbejdstilladelse, sikkerhedsinstruks, "
     "afmelding med dokumentation, fakturakontrol mod udført arbejde"),
    ("Compliance",
     "Eftersynsmatrix med udløbsdatoer, DS/HD 60364 og EN 61439, APV og risikovurdering, LOTO, "
     "entreprenørkontrol, myndighedsdokumentation og near-miss-opfølgning"),
    ("KPI & rapportering",
     "Oppetid og responstid, gentagne fejl og nedetid, omkostning pr. site, energiforbrug pr. anlæg, "
     "månedlig ledelsesrapport, Power BI-dashboards og Excel-modeller"),
    ("Optimering",
     "PDCA og 5S, standardarbejde, energikortlægning og ELO/EOS-tiltag, investeringscases med NPV og "
     "payback, før/efter-målinger"),
    ("Projekter",
     "Kravspecifikation, FAT/SAT, IQ/OQ/PQ, afvigelseshåndtering og aflevering med dokumentation; "
     "tid, økonomi og risiko styret i fast rapporteringsformat"),
    ("Systemer & IT",
     "SAP ERP og CMMS, Microsoft Office og Excel, SharePoint som dokumentbase, Power BI, Python og "
     "Claude til automatiseret status og rapportering"),
]

ACHIEVEMENTS = [
    ("40+ serviceanlæg drevet i dag",
     "el, tavler, styring, ventilation og klima — med daglig prioritering mellem adresser og fuldt "
     "P&L-ansvar."),
    ("Nul uplanlagte stop på 24/7-anlæg",
     "fem år med pumper, HVAC, koblingsanlæg, højspænding og SCADA — oppetid gennem forebyggende "
     "vedligehold og hurtig fejlfinding."),
    ("Nul kritiske afvigelser ved aflevering",
     "på 37 samtidige anlægsprojekter (2–10 mio. kr.) — dokumentation og aflevering uden fund."),
    ("−40 % energikost",
     "i reguleret produktion via PDCA, A3 og standardiserede løsninger; fastholdt efter projektets "
     "afslutning."),
    ("+40 % produktivitet",
     "gennem dataunderstøttet planlægning, standardarbejde og egen AI-tooling — målt over tid."),
    ("Arbejdsordrer og eftersyn som system",
     "tjeklister, arbejdsordrer og compliance-status på ét sted — så et eftersyn ikke kan løbe over, og "
     "så status på ti sites kan læses på én side."),
    ("Leverandøraftaler målt, ikke antaget",
     "serviceniveau, responstid og pris fulgt op pr. aftale, og faktura afstemt mod det arbejde, der "
     "faktisk blev afmeldt med dokumentation."),
]

EXPERIENCE = [
    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "40+ serviceanlæg i Storkøbenhavn · 5 elektrikere og 3 lærlinge · fuldt P&L og leverandøraftaler",
     [("Teknisk drift på flere adresser",
       "planlagt og afhjælpende vedligehold, fejlfinding på el, tavler, styring, ventilation og klima; "
       "daglig prioritering mellem anlæg og kunder."),
      ("Leverandører og serviceaftaler",
       "indkøb af komponenter og serviceydelser, prissammenligning, aftaler og kontrol af udført "
       "arbejde; fuldt ansvar for bundlinjen."),
      ("Kunder og rapportering",
       "én indgang til kunderne, tilbud og opfølgning indtil opgaven er lukket; status og økonomi "
       "rapporteret i fast form."),
      ("Systemer og dokumentation",
       "ERP-baseret ordre- og reservedelsstyring, tjeklister, Power BI og Python/Claude-værktøjer til "
       "status og rapportering; produktivitetsløft over 40 %.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · drifts- og "
     "vedligeholdelsesbudgetter i SAP",
     [("Vedligeholdsplan og KPI",
       "PDCA-baseret vedligeholdsplan med fast årshjul, A3-root-cause på større nedetid, reservedelsflow "
       "og kritiske lagre; KPI'er og driftsbudgetter i SAP ERP."),
      ("Leverandører og entreprenører",
       "koordinering af egne teknikere, entreprenører og leverandører på et aktivt anlæg — adgang, "
       "sikkerhed og arbejdstilladelser."),
      ("Sikkerhed og arbejdsmiljø",
       "LOTO, risikovurdering, arbejdstilladelser, near-miss-rapportering og værktøjsmøder.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister inden for teknik, indkøb og drift · "
     "GMP/FDA/EMA",
     [("Teknisk sparring og tværfaglig styring",
       "25 specialister på tværs af mekanik, el, proces og indkøb; tekniske afklaringer dokumenteret, så "
       "alle arbejdede efter samme aftale."),
      ("Idriftsættelse og dokumentation",
       "FAT/SAT, IQ/OQ/PQ og valideringsdokumentation med afvigelseshåndtering, CAPA og change control "
       "— nul kritiske fund."),
      ("Projekt og økonomi",
       "tidsplan, økonomi, risiko og månedlig rapportering til ledelse og kunde; −40 % energikost "
       "gennem PDCA og standardiseret arbejde.")]),

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
    "Technical Manager · Teknisk Manager · GWS Segment · Facilities Management · Facility Management · "
    "Teknisk Drift · Ejendomsdrift · Vedligehold · Forebyggende Vedligehold · Afhjælpende Vedligehold · "
    "Tekniske Installationer · El · VVS · Ventilation · Varme · Køl · Tavler · Nødstrøm · CTS · Brand · "
    "Sites · Lokationer · Portefølje · Kørsel · Underleverandører · Serviceaftaler · Serviceniveau · "
    "Leverandørstyring · Koordinering · Styring · Teknisk Sparringspartner · Sparring · Kunde · Team · "
    "Lovkrav · Myndighedskrav · Sikkerhed · Compliance · Eftersyn · Dokumentation · KPI · Rapportering · "
    "Forbedring · Optimering · Energi · Kritikalitet · Arbejdsordrer · CMMS · SAP · Power BI · Excel · "
    "Microsoft Office · Systemer · Struktureret · Selvstændig · Løsningsorienteret · Overblik · "
    "Samarbejde · Tillid · Dansk · Engelsk · Kørekort · Aarhus · Midtjylland · Nordjylland · Jylland · "
    "Slagelse · Contract Manager · CBRE · RISE"
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
    m.resume_header(NAME, TITLE, CONTACT, "TEKNISK PROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("TEKNISKE METODER & VÆRKTØJER — ANVENDT I PRAKSIS",
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

    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER PORTEFØLJEN I DRIFT",
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
                  title="Ansøgning og CV — Technical Manager, CBRE GWS Aarhus",
                  subject="Teknisk drift · vedligehold · underleverandører og serviceaftaler · "
                          "lovkrav og KPI · Jylland",
                  keywords=("technical manager, teknisk drift, vedligehold, el, vvs, ventilation, "
                            "underleverandører, serviceaftaler, kpi, lovkrav, sikkerhed, aarhus, jylland, "
                            "dansk, engelsk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1 (krav → løsning), CV side 2-4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_CBRE_TechnicalManager_Aarhus.docx")
    print("OK", build(out))
