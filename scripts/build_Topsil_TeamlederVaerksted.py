# -*- coding: utf-8 -*-
"""
Topsil GlobalWafers A/S — Teamleder til højt specialiseret mekanisk værksted.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Teamleder | Mekanisk værksted — produktion, oppetid og udvikling"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "31. oktober 2026"
RECIPIENT = ("Topsil GlobalWafers A/S · Siliciumvej 1, 3600 Frederikssund · att. HR")
SUBJECT = "Ansøgning: Teamleder til højt specialiseret mekanisk værksted"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Opgaven er at lede et værksted, hvor seks specialister — snart syv — holder en 24/7-produktion "
    "kørende med komponenter, der ikke kan undværes. Når produktionslinjen står stille på grund af en "
    "slidt eller manglende komponent, er det ikke et spørgsmål om kroner, men om en kunde, der venter på "
    "wafers. Derfor er værkstedets opgaver ikke bare tekniske — de har en prioritet, og den skal kunne "
    "forklares.",

    "Nedenfor er min læsning af rollen og det system, der står klar fra første dag: kompetencematrix og "
    "udviklingsplaner pr. medarbejder, en kapacitetsplan der skiller akutte sager fra planlagt arbejde, "
    "en reservedelsstrategi efter kritikalitet, en forbedringsportefølje med måling før og efter, og en "
    "fast mødekadence med Vedligehold, Produktion, PTA, Engineering og Indkøb.",
]

BULLETS = [
    ("Kravet: ledelse, motivation og udvikling af medarbejderne — og høj trivsel og engagement",
     "Løsningen er tæt, synlig ledelse: 1:1 hver fjerde uge, udviklingsplaner der bliver fulgt op, "
     "ugentligt tavlemøde og en leder på gulvet. Koordinatoren fordeler de daglige opgaver — min rolle "
     "er rammerne, retningen og de svære samtaler, ikke at tage fordelingen fra ham."),

    ("Kravet: udvikle kompetencer og sikre den langsigtede bemanding af kritiske fagområder",
     "Løsningen er en kompetencematrix, hvor hvert kritisk fag har mindst to personer, der kan løse "
     "opgaven — og en plan for den nye kollega, der starter med at lære af de erfarne, ikke ved at "
     "skulle være selvkørende uge to. Kritisk viden skal ikke gå på pension med én mand."),

    ("Kravet: drive forbedringsprojekter inden for kvalitet, arbejdsmiljø og effektivitet",
     "Løsningen er en forbedringsportefølje med få, prioriterede A3-sager: problem, måling før, "
     "ændring, måling efter og en ejer. Arbejdsmiljø køres som risikovurdering og sikkerhedsrunde med "
     "opgaver, der bliver lukket — ikke som et dokument, der bliver lagt i en mappe."),

    ("Kravet: identificere og implementere muligheder for automatisering og digitalisering",
     "Løsningen er at gå efter håndteringspunkterne: gentagne løft, manuel dokumentation, "
     "registreringer der skrives to gange og planlægning, der kun findes i hovedet på én person. Jeg har "
     "selv bygget rapportering og planlægningsværktøj i Python, Power BI og Claude — det er hverdag, "
     "ikke et projekt."),

    ("Kravet: sikre effektiv planlægning og prioritering af værkstedets opgaver",
     "Løsningen er én plan, hvor akutte opgaver fra produktionen har en fast sluse og en aftalt "
     "svartid, og planlagt arbejde er beskyttet. Prioriteringen sker efter kritikalitet for oppetiden — "
     "ikke efter hvem der råbte højest sidst."),

    ("Kravet: ansvar for reservedelsstrategi, lagerstyring og relevante SAP-processer",
     "Løsningen er en reservedelsstrategi bygget på kritikalitet og levetid: hvad skal ligge på hylden, "
     "hvad kan skaffes på et døgn, og hvad er specialfremstillet. Min/max, lagerklassificering og "
     "SAP-data holdt ajour — jeg har arbejdet med budgetter, indkøb og reservedele i SAP og CMMS."),

    ("Kravet: samarbejde med Vedligehold, Produktion, PTA, Engineering og Indkøb samt leverandører",
     "Løsningen er tydelige grænseflader og fast kadence: hvem bestiller hvad af værkstedet, hvornår "
     "svarer vi, og hvordan bliver en sag, der skal ændres i designet, løftet til Engineering. Én indgang "
     "til værkstedet — også for leverandørerne."),
]

SYSTEM = ("Systemet er allerede bygget: kompetencematrix med kritiske fag og udviklingsplaner, "
          "kapacitetsplan seks uger frem, akutsluse med aftalt svartid, reservedelsstrategi efter "
          "kritikalitet med min/max og SAP-data, forbedringsportefølje med A3 og måling før/efter samt "
          "KPI'er for oppetid, gennemløbstid og efterslæb — i Excel, Power BI og SAP, med Python og "
          "Claude til rapportering.")

MIRROR = ("Om kravene: 20 år i produktion, værksted og drift — 14-mands produktions- og montageteam, "
          "12-mands produktionsteam, daglig ledelse af 5 elektrikere og 3 lærlinge med fuldt P&L, "
          "24/7-drift med nul uplanlagte stop i fem år, 37 anlægsprojekter under GMP-krav; elautoriseret "
          "maskinmester (LV/MV/HV) og B.Tech i Technology Management & Mechanical Engineering.")

HONEST = ("To ting skal siges ligeud: jeg har ikke arbejdet i halvlederproduktion før, og IATF 16949 har "
          "jeg ikke arbejdet under — min kvalitetserfaring kommer fra GMP/FDA/EMA og ISO9001. Det, jeg "
          "tager med, er det, værkstedet bliver målt på: oppetid, kompetencer der ikke forsvinder med én "
          "medarbejder, reservedele der er der, når de skal bruges, og forbedringer der bliver målt.")

CULTURE = ("Hvorfor Topsil: I skriver uformel omgangstone, respekt for den enkelte og life balance — og "
           "i en 24/7-virksomhed er det ikke bløde værdier, det er det, der gør, at folk holder i længden. "
           "Et værksted med specialister kører på faglig stolthed og på, at man kan sige højt, når noget "
           "er svært. Det gode grin og den høje faglighed udelukker ikke hinanden; de forstærker hinanden.")

PRACTICAL = ("Praktisk: bosat i Måløv — cirka 35 minutter til Siliciumvej i Frederikssund; kørekort B og "
             "bil; dansk på modersmålsniveau i skrift og tale; klar til hurtigt start, og egen virksomhed "
             "afvikles ved ansættelse.")

CLOSING = ("Jeg vil gerne se værkstedet og møde teamet, og bruge første samtale på to spørgsmål: hvordan "
           "I prioriterer mellem akutte opgaver fra produktionen og det planlagte arbejde i dag, og "
           "hvilke kompetencer der er kritiske at have på plads om tre år.")

# ------------------------------------------------------------------ CV
PROFILE = ("Rollen kræver tre ting på én gang: ledelse af specialister der ikke skal styres i detaljen, "
           "et værksted der leverer til en produktion, der ikke må stå stille, og en leder der kan gøre "
           "forbedringer og digitalisering til noget, der faktisk bliver gennemført. Alle tre har været "
           "hverdag i 20 år: daglig ledelse af 5 elektrikere og 3 lærlinge med fuldt P&L, 14- og "
           "12-mands produktionsteams, 24/7-drift med nul uplanlagte stop i fem år, reservedele og "
           "budgetter i SAP og 37 anlægsprojekter under GMP/FDA/EMA-krav. Elautoriseret maskinmester "
           "(LV/MV/HV), B.Tech i Technology Management & Mechanical Engineering.")

PRACTICE = [
    ("Ledelse af tekniske specialister",
     "1:1-hjul, MUS med opfølgning, kompetencematrix, udviklingsplaner og delegering med opfølgning; "
     "situationsbestemt ledelse (SLII) og tillidsbaseret ledelse med klare rammer."),
    ("Produktionsmiljø og oppetid",
     "Prioritering efter kritikalitet for produktionen, akutsluse med svartid, beredskab på 24/7-anlæg, "
     "fejlhistorik og A3-root-cause — nul uplanlagte stop i fem år."),
    ("Forbedringsarbejde",
     "A3 og PDCA med måling før og efter, standardarbejde, 5S og værdistrømsanalyse; forbedringer "
     "prioriteret som en portefølje med ejere, ikke som løse idéer."),
    ("Automatisering og digitalisering",
     "KPI- og rapporteringsløsninger i Power BI og Python, AI-assisteret analyse og dokumentation, "
     "SCADA-data og CMMS/SAP som grundlag for beslutninger."),
    ("Reservedele og lager",
     "Reservedelsstrategi efter kritikalitet og levetid, min/max og lagerklassificering, indkøb og "
     "leverandøraftaler, SAP-budgetter og opfølgning på forbrug."),
    ("Planlægning og prioritering",
     "Kapacitetsplan seks uger frem, opgaveportefølje med ejer og frist, håndtering af akutte sager "
     "uden at planlagt arbejde falder bagud."),
    ("Kvalitet og arbejdsmiljø",
     "Egenkontrol og afvigelser med root cause, dokumentstyring med version og ejer, APV, "
     "risikovurdering, sikkerhedsrundering og nærved-hændelser."),
]

MODELS = [
    ("Ledelse",
     "1:1-hjul, MUS/GRUS, kompetencematrix med kritiske fag, udviklingsplaner, SLII og "
     "tillidsbaseret ledelse"),
    ("Værksted og oppetid",
     "Kritikalitetsmodel for opgaver, akutsluse med svartid, kapacitetsplan seks uger frem, "
     "fejlhistorik og A3-root-cause"),
    ("Forbedringer",
     "A3 og PDCA med måling før/efter, standardarbejde, 5S, værdistrømsanalyse og en "
     "forbedringsportefølje med ejere"),
    ("Digitalisering",
     "Power BI-tavler, Python/Claude til rapportering og analyse, SCADA- og CMMS-data, "
     "automatisering af gentagne registreringer"),
    ("Reservedele og SAP",
     "Kritikalitet og levetid som grundlag for lager, min/max og lagerklassificering, "
     "indkøb, leverandøraftaler og budget i SAP"),
    ("Kvalitet",
     "Egenkontrol, afvigelser med root cause, dokumentstyring med version og ejer, intern audit "
     "og ledelsens gennemgang"),
    ("Arbejdsmiljø",
     "APV og risikovurdering, sikkerhedsrundering, LOTO og arbejdstilladelser, nærved-hændelser "
     "og toolbox-møder"),
]

ACHIEVEMENTS = [
    ("Nul uplanlagte stop i fem år",
     "på 24/7-forsyningsanlægget Lynetten — planlagt vedligehold, PDCA og A3-root-cause frem for "
     "brandslukning."),
    ("5 elektrikere og 3 lærlinge med fuldt P&L",
     "daglig ledelse, kompetenceudvikling, udviklingssamtaler og ansvar for bundlinjen i egen "
     "virksomhed."),
    ("14- og 12-mands produktionsteams ledet",
     "kapacitetsplanlægning, flowstyring og daglige tavlemøder i produktion og montage."),
    ("Nul kritiske fund ved aflevering",
     "37 anlægsprojekter hos Novo Nordisk under GMP/FDA/EMA-krav — dokumentation og aflevering uden "
     "fund."),
    ("+40 % produktivitet og −40 % energikost",
     "dokumenterede forbedringer via måling, standardarbejde, dataunderstøttet planlægning og egen "
     "AI-tooling."),
]

EXPERIENCE = [
    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og leverandøraftaler",
     [("Personale og rammer",
       "daglig ledelse af 5 elektrikere og 3 lærlinge, opgavefordeling, kompetencematrix og "
       "udviklingssamtaler."),
      ("Værksted, indkøb og økonomi",
       "plan og prognose, indkøb og leverandøraftaler, lager og reservedele samt fuldt ansvar for "
       "bundlinjen.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Team og fremdrift",
       "14-personers team med kapacitetsplanlægning, flowstyring og daglige tavlemøder over 11 "
       "samtidige entrepriser."),
      ("Proces og forbedring",
       "standardarbejde og 5S i værkstedet; håndteringspunkter og fejlkilder kortlagt med måling før og "
       "efter.")]),

    ("Elektromekaniker / Produktionsteamleder",
     "ARJ Engineering · Teheran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · skiftplanlægning, materialestyring og lager",
     [("Produktionsteam og teknisk problemløsning",
       "skiftplanlægning, materialestyring og målopfølgning; reparation og diagnosticering af "
       "elektriske og mekaniske systemer gennem struktureret root cause-analyse.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · budgetter i SAP",
     [("Drift, reservedele og KPI",
       "PDCA-baseret vedligeholdsplan, kritiske reservedele på lager og KPI'er i SAP; nul uplanlagte "
       "stop i fem år."),
      ("Leverandører og sikkerhed",
       "koordinering af egne teknikere, entreprenører og leverandører — LOTO, arbejdstilladelser, "
       "garantisager og nærved-hændelser.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister · GMP/FDA/EMA",
     [("Kvalitet og dokumentation",
       "FAT/SAT, IQ/OQ/PQ og valideringsdokumentation med afvigelseshåndtering — nul kritiske fund; "
       "arbejde under myndighedskrav og revision."),
      ("Projekt og koordinering",
       "plan, økonomi og rapportering; 25 specialister koordineret på tværs af mekanik, el, proces og "
       "indkøb.")]),
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
    ("Arbejdsmiljø §16 og sikkerhedsbevidsthed (VI/6-1)",
     "Søfartsstyrelsen · maj 2021"),
    ("Køleteknik & klimaanlæg (AMU)",
     "Mercantec · mar. 2021"),
    ("Lean — værdistrømsanalyse, standardarbejde, 5S, A3 og Kaizen",
     "Anvendt i produktion og projekter · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og produktion · 2017 – nu"),
]

LANGUAGES = ("Dansk (modersmål, skrift og tale) · Engelsk (professionelt) · Persisk/farsi · "
             "Kørekort B (kategori B)")

PRACTICAL_CV = ("Bosat i Måløv — cirka 35 minutter til Topsil på Siliciumvej i Frederikssund; kørekort "
                "kategori B og bil; dansk på modersmålsniveau i skrift og tale; klar til hurtigt start; "
                "egen virksomhed afvikles ved ansættelse.")

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Ventek-Air, Biofos (Lynetten), Novo Nordisk A/S "
              "(Kalundborg) og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Teamet i værkstedet",
     "Rammer for, hvem der beslutter hvad, 1:1 og faglig sparring på fast kadence, og en leder der "
     "tager de svære samtaler tidligt — specialister skal udfordres fagligt, ikke styres i detaljen."),
    ("Produktion, Vedligehold, PTA og Engineering",
     "Én indgang til værkstedet med aftalt svartid, akutsluse og fast mødekadence, så en sag der skal "
     "ændres i designet bliver løftet, før den bliver akut."),
    ("Indkøb og leverandører",
     "Reservedelsstrategi efter kritikalitet, leverandøraftaler med leveringstid og alternativer, "
     "og SAP-data der passer med virkeligheden på hylden."),
]

FIRST90 = [
    ("Uge 1–2",
     "Mødt teamet og koordinatoren, gennemgået værkstedets opgavetyper, udstyr og de åbne sager; "
     "gennemgået reservedelslager og de kritiske komponenter sammen med den, der kender dem bedst. "
     "Mødt Vedligehold, Produktion, PTA, Engineering og Indkøb."),
    ("Uge 3–6",
     "Kompetencematrix med kritiske fag og udviklingsplaner lagt sammen med teamet; akutsluse og "
     "svartid aftalt med produktionen; ugentligt tavlemøde og 1:1-kalender i gang."),
    ("Uge 7–12",
     "Kapacitetsplan seks uger frem; reservedelsstrategi og min/max gennemgået med Indkøb; to "
     "forbedringssager valgt med måling før — kvalitet, arbejdsmiljø eller effektivitet."),
    ("Måned 3–6",
     "Onboarding af den nye kollega planlagt og i gang; de første forbedringer målt efter; "
     "arbejdsmiljø og sikkerhedsrunder kørende med opgaver, der bliver lukket."),
    ("Måned 6–12",
     "Værkstedet leverer med kortere gennemløbstid og mindre efterslæb; mindst ét "
     "digitaliseringsinitiativ i drift; kritisk viden dækket af mindst to personer pr. fagområde. "
     "Løbende: månedlig gennemgang af KPI'er og en fast post for, hvad der skal forenkles næste "
     "måned."),
]

KEYWORDS = (
    "Teamleder · Mekanisk værksted · Værksted · Specialister · Mekanikere · Teknikere · Daglig ledelse · "
    "Motivation · Udvikling af medarbejdere · Trivsel · Engagement · Samarbejde · Kompetencer · "
    "Langsigtet bemanding · Kritiske fagområder · Forbedringsprojekter · Kvalitet · Arbejdsmiljø · "
    "Effektivitet · Automatisering · Digitalisering · Planlægning · Prioritering · Reservedelsstrategi · "
    "Lagerstyring · SAP · Interne interessenter · Leverandører · Produktionsmiljø · Tekniske processer · "
    "Struktureret · Tillid · Involvering · Oppetid · Vedligehold · Produktion · PTA · Engineering · "
    "Indkøb · IATF 16949 · ISO · Halvlederindustri · Ultrarent silicium · Maskinmester · Power BI · "
    "CMMS · SCADA · Dansk · Frederikssund · Måløv"
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
    m.resume_header(NAME, TITLE, CONTACT, "LEDELSESPROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("LEDELSES- OG VÆRKSTEDSMETODER — ANVENDT I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER VÆRKSTEDET I RYTMEN",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN LEDES VÆRKSTEDET — DE TRE PARTER")
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
                  title="Ansøgning og CV — Teamleder, mekanisk værksted, Topsil",
                  subject="Værkstedsledelse · oppetid · kompetencer · reservedele · digitalisering",
                  keywords=("teamleder, mekanisk værksted, produktion, oppetid, reservedele, sap, "
                            "kompetenceudvikling, forbedringer, automatisering, topsil, dansk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1 (krav → løsning), CV side 2-3, 90 dage side 4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_Topsil_TeamlederVaerksted.docx")
    print("OK", build(out))
