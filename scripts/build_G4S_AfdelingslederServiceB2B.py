# -*- coding: utf-8 -*-
"""
G4S — Afdelingsleder, Service B2B (erhvervskunder på Sjælland).
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
TITLE = "Afdelingsleder | Service B2B | G4S"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv")

DATE = "31. oktober 2026"
RECIPIENT = ("G4S · Service B2B · Sjælland · Att.: Nisreen Mahdi, Servicechef · tlf. 24 37 35 31")
SUBJECT = "Ansøgning: Afdelingsleder — Service B2B, Sjælland"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Opgaven er at drive en serviceafdeling, hvor medarbejderne ikke sidder i samme hus som chefen. "
    "Udekørende elektrikere, kontorpersonale og erhvervskunder skal hænge sammen i én rytme: montøren "
    "ved, hvad der skal løses i dag, kunden ved, hvornår der kommer nogen, og lederen ved, hvad der "
    "stopper arbejdet — før det bliver en klage eller en tabt ordre. Det er distanceledelse i praksis, "
    "og det er det, der afgør, om omsætning og bundlinje følger med.",

    "Nedenfor er min læsning af stillingen og det system, der ligger klar til at tage den: "
    "kapacitets- og bemandingsplan, hindringslog, kundemødekadence og en KPI-tavle med de tal, der "
    "styrer en serviceafdeling — udnyttelsesgrad, responstid, genkøb og dækningsgrad.",
]

BULLETS = [
    ("Kravet: distanceledelse af udekørende montører",
     "Løsningen er en fast rytme, der ikke kræver, at man står ved siden af folk: kort digital "
     "morgenafstemning om dagens opgaver, ugentligt tavlemøde hvor sidste uges tal og næste uges "
     "kapacitet gennemgås, 1:1 hver fjerde uge og tydelige rammer for, hvornår man ringer, og hvornår "
     "man selv beslutter. Nærvær i distanceledelse er struktur, ikke tilfældige opkald — og det er den "
     "måde at motivere det bedste frem i folk, man ikke ser hver dag."),

    ("Kravet: fjerne hindringer og skabe struktur i uorden",
     "Løsningen er en hindringslog, hvor montørerne melder ind, hvad der stopper dem — materialer, "
     "adgang, tilladelser, manglende information fra kunden — og hvor hver hindring får en ejer og en "
     "frist. Den gennemgås hver uge. En leder, der fjerner hindringer, får en afdeling, der ikke skal "
     "spørge om lov til at arbejde."),

    ("Kravet: kundekontakt, kundehenvendelser og kundemøder",
     "Løsningen er én indgang med aftalte svartider, en eskaleringstrappe og en fast mødekadence med de "
     "største erhvervskunder, hvor status, åbne sager og næste kvartals behov gennemgås. Kundeoplevelsen "
     "måles — svartid, genkøb og hvad kunderne selv siger — så den ikke bliver en mavefornemmelse."),

    ("Kravet: vækst i omsætning og bundlinje sammen med salg og drift",
     "Løsningen er en afdelingsøkonomi, der bliver gennemgået månedligt: omsætning pr. montør og pr. "
     "time, udnyttelsesgrad, materialeforbrug, pris og dækningsgrad — plus en fast gennemgang med salg om, "
     "hvilke kunder der kan vokse, og hvilke opgaver der skal siges nej til. Samarbejde med kolleger i salg "
     "og drift er en forudsætning, ikke en høflighed."),

    ("Kravet: elektrikerbaggrund og kendskab til sikringsløsninger",
     "Løsningen er faglig tyngde i elautorisationen (LV/MV/HV) og i de anlæg, kunderne har: tavler, "
     "styring, ABA/ABV, adgangskontrol, PDS og nød- og panikbelysning — suppleret med 40+ serviceanlæg og "
     "5 elektrikere i egen virksomhed — så en opgave og en montørs dag kan vurderes uden tre led imellem."),
]

SYSTEM = ("Systemet er allerede bygget: kapacitets- og bemandingsplanen, hindringsloggen med ejer og "
          "frist, 1:1-kalenderen, kundemødeagendaen og KPI-tavlen med udnyttelsesgrad, responstid, "
          "genkøb og dækningsgrad. Det er bygget i Excel, Power BI og SharePoint og suppleret med Python "
          "og Claude til den månedlige rapportering — så ledelsestiden går til medarbejdere og kunder i "
          "stedet for til at samle tal.")

MIRROR = ("Om kravene: erfaren personaleleder med personaleansvar siden 2003 og ledelse af elektrikere i "
          "dag — 5 elektrikere og 3 lærlinge i egen virksomhed samt 14- og 12-mands tekniske teams; "
          "elautoriseret maskinmester (LV/MV/HV), hvilket dækker opslagets krav om elektriker/"
          "elinstallatørbaggrund; situationsbestemt og tydelig kommunikation; vant til at skabe struktur i "
          "uorden og til at måles på omsætning og bundlinje med fuldt P&L-ansvar.")

HONEST = ("To ting påvirker opgaven og skal siges ligeud: jeg har ikke ledet montører i "
          "sikringsbranchen før — min erfaring er el-service og -installation i egen virksomhed og "
          "tekniske teams i drift og produktion, så branchens produkter, certifikater og "
          "myndighedskrav skal læres. Og jeg er elautoriseret maskinmester, ikke uddannet elinstallatør; "
          "elautorisationen er den samme faglige tyngde, men titlen skal være rigtig. Politigodkendelse "
          "efter lov om vagtvirksomhed er uproblematisk.")

CULTURE = ("Hvorfor G4S: at være en del af Danmarks stærkeste hold inden for sikkerhedsløsninger kræver "
           "en afdeling, hvor kvaliteten ikke afhænger af den enkelte montørs dagsform, og hvor kunden "
           "oplever samme standard hver gang. Og når I skriver, at medarbejderne er top engagerede med "
           "høj faglighed, er ledelsesopgaven netop at fjerne det, der står i vejen for den faglighed — "
           "ikke at instruere mere.")

PRACTICAL = ("Praktisk: bosat i Måløv, midt i det sjællandske kørselsområde; erhvervsmæssig kørsel med "
             "egen bil, der stilles til rådighed og afregnes efter statens takster; dansk på modersmålsniveau og engelsk "
             "professionelt; kan godkendes af politiet jf. lov om vagtvirksomhed; kort opsigelse og klar "
             "til hurtigt start. Egen virksomhed afvikles ved ansættelse.")

CLOSING = ("Jeg vil gerne høre, hvordan afdelingen styres i dag, og bruge første samtale på tre spørgsmål: "
           "hvordan montørernes dag bliver planlagt, hvilke tal afdelingen måles på, og hvor "
           "kundehenvendelserne i dag falder mellem to stole.")

# ------------------------------------------------------------------ CV
PROFILE = ("Rollen kræver fire ting på én gang: at lede udekørende faglærte på afstand, at skabe struktur "
           "og fjerne hindringer, at holde kunder tæt på og at måles på omsætning og bundlinje. Alle fire "
           "har været kerneopgaven i tyve år: 5 elektrikere og 3 lærlinge med fuldt P&L-ansvar i egen "
           "autoriseret virksomhed, 14- og 12-mands tekniske teams i produktion og montage, og 37 "
           "samtidige anlægsprojekter hos Novo Nordisk. Elautoriseret maskinmester (LV/MV/HV), B.Tech i "
           "Technology Management & Mechanical Engineering, dansk på modersmålsniveau og engelsk "
           "professionelt.")

PRACTICE = [
    ("Distanceledelse",
     "Fast møderytme (digital morgenafstemning, ugentligt tavlemøde), 1:1 hver fjerde uge, "
     "kompetencematrix, tydelige beslutningsrammer og en eskaleringstrappe — så udekørende medarbejdere "
     "ved, hvornår de skal spørge, og hvornår de skal handle."),

    ("Hindringer og struktur",
     "Hindringslog med ejer og frist, ugentlig gennemgang, standarder for tilbud, materialer og "
     "aflevering, og faste processer for de opgavetyper, der ellers bliver ad hoc."),

    ("Kunde og service",
     "Én indgang og aftalte svartider, kundemødekadence på de største konti, eskaleringstrappe og "
     "opfølgning på genkøb og kundetilfredshed — service målt, ikke antaget."),

    ("Afdelingsøkonomi",
     "Omsætning pr. montør og pr. time, udnyttelsesgrad, materialeforbrug, pris og dækningsgrad; "
     "månedlig økonomigennemgang og budgetopfølgning med fuldt P&L-ansvar."),

    ("Salg og vækst",
     "Fast gennemgang med salg om kundeporterne, mersalg på eksisterende anlæg (service, eftersyn, "
     "opgradering) og prioritering af, hvilke ordrer der er værd at tage."),

    ("Sikring og el-teknik",
     "Tavler og styring, ABA/ABV, adgangskontrol, PDS, nød- og panikbelysning, UPS samt fejlfinding og "
     "aflevering; elautorisation LV/MV/HV med egenkontrol og dokumentationsansvar."),

    ("Medarbejdere og udvikling",
     "Kompetencematrix og udviklingsplaner, rekruttering og onboarding, lærlinge og faglærte på "
     "forskellige niveauer, performanceopfølgning og arbejdsmiljø."),

    ("Rapportering og værktøj",
     "KPI-tavle i Power BI, Excel-modeller til kapacitet og dækningsgrad, Python og Claude til "
     "automatiseret månedsrapportering; tal der kan læses på ét blik."),
]

FIRST90 = [
    ("Uge 1–2",
     "Alle montører og kontorpersonalet mødt — på kontoret og ude på opgaverne; kundeporterne, de åbne "
     "sager, aftalerne og de nuværende KPI'er gennemgået, før noget ændres."),
    ("Uge 3–6",
     "Kapacitets- og bemandingsplan lagt for de næste otte uger; hindringslog indført og gennemgået "
     "ugentligt; møderytme og 1:1-kalender aftalt med medarbejderne."),
    ("Uge 7–12",
     "KPI-tavle med baseline for udnyttelsesgrad, responstid og dækningsgrad; kundemøder holdt med de "
     "største erhvervskunder; første forbedringer gennemført på de hindringer, der fylder mest."),
    ("Måned 3–6",
     "Afdelingsøkonomien gennemgået månedligt med salg og drift; udnyttelsesgrad og responstid forbedret; "
     "kompetencematrix og udviklingssamtaler gennemført for alle medarbejdere."),
    ("Måned 6–12",
     "Afdelingen leverer stabilt på målene uden daglig styring; vækst i omsætning på eksisterende kunder, "
     "sund dækningsgrad og en medarbejdergruppe, der selv tager ansvar for planen — og som bliver "
     "inddraget, før beslutningerne er taget."),
    ("Måned 12+",
     "Afdelingen har en egen rytme: kapacitetsplan, KPI-tavle og kundemøder kører uden lederens "
     "indblanding, kompetencematrixen er opdateret før næste rekruttering, og de kunder, der skal vokse, "
     "er udvalgt på tal."),
    ("Løbende",
     "Månedlig ledelsesrapport med økonomi, KPI'er og åbne sager; kvartalsvis kundegennemgang; og en fast "
     "post på dagsordenen for, hvad der skal forenkles næste måned."),
]

MODELS = [
    ("Distanceledelse",
     "Digital morgenafstemning, ugentligt tavlemøde, 1:1-hjul, delegeringstrappe, beslutningsrammer og "
     "eskaleringstrappe, situationsbestemt ledelse (SLII) og GROW-coaching"),
    ("Struktur & forbedring",
     "Hindringslog med ejer og frist, standardarbejde, 5S, PDCA, A3 og fem-hvorfor, proceskortlægning, "
     "tavlemøder og visuel ledelse"),
    ("Kunde & service",
     "Én indgang og svartider, kundemødekadence, eskaleringstrappe, genkøb og kundetilfredshed, "
     "serviceaftaler med SLA og responstid"),
    ("Økonomi & vækst",
     "Omsætning pr. montør og time, udnyttelsesgrad, dækningsgrad og materialeforbrug, budget og "
     "prognose, prissætning og tilbud, mersalg på eksisterende anlæg"),
    ("El & sikring",
     "Tavler og styring, ABA/ABV, adgangskontrol, PDS, UPS, nød- og panikbelysning, fejlfinding, "
     "idriftsættelse og afleveringsdokumentation, DS/HD 60364"),
    ("Sikkerhed & arbejdsmiljø",
     "APV og risikovurdering, LOTO, arbejdstilladelser og adgang, sikkerhedsrundering, "
     "nærved-hændelser og toolbox-møder"),
    ("Medarbejdere",
     "Kompetencematrix og udviklingsplaner, MUS/GRUS, rekruttering og onboarding, lærlingeoplæring, "
     "performance- og lønopfølgning"),
    ("Rapportering & værktøj",
     "KPI-tavle i Power BI, Excel-modeller, SharePoint som dokumentbase, SAP og CMMS, Python og Claude "
     "til automatiseret månedsrapportering"),
]

ACHIEVEMENTS = [
    ("5 elektrikere og 3 lærlinge ledet i dag",
     "daglig planlægning, 1:1, kompetencematrix og udvikling — i egen autoriseret virksomhed med fuldt "
     "P&L-ansvar."),
    ("Udekørende hverdag på 40+ serviceanlæg",
     "planlægning og prioritering mellem adresser, med responstid og leveringsevne som KPI'er."),
    ("+40 % produktivitet",
     "gennem dataunderstøttet planlægning, standardarbejde og egen AI-tooling — målt over tid og "
     "fastholdt."),
    ("14- og 12-mands tekniske teams",
     "kapacitetsplanlægning, flowstyring og daglige tavlemøder over 11 samtidige projekter."),
    ("Nul kritiske afvigelser ved aflevering",
     "på 37 samtidige anlægsprojekter (2–10 mio. kr.) — dokumentation og aflevering uden fund."),
]

EXPERIENCE = [
    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg i Storkøbenhavn · fuldt P&L, kunder og aftaler",
     [("Personaleansvar",
       "daglig ledelse af 5 elektrikere og 3 lærlinge, 1:1-samtaler, performanceopfølgning, "
       "kompetencematrix, sikkerhed og udvikling."),
      ("Kunder og service",
       "aftaler og serviceopgaver med erhvervskunder, tilbud og prissætning, opfølgning til opgaven er "
       "lukket og genkøb på eksisterende anlæg."),
      ("Økonomi og indkøb",
       "budget og prognose, indkøb af komponenter og serviceydelser, leverandøraftaler og prissammenligning; "
       "fuldt ansvar for bundlinjen."),
      ("Drift og akutte hændelser",
       "planlagt og afhjælpende vedligehold, fejlfinding på el, tavler, styring, ventilation og klima; "
       "prioritering mellem adresser, når flere ting haster.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · drifts- og "
     "vedligeholdelsesbudgetter i SAP",
     [("Vedligeholdsplan og KPI",
       "PDCA-baseret plan med fast årshjul, A3-root-cause på større nedetid og KPI'er i SAP ERP."),
      ("Leverandører og entreprenører",
       "koordinering af egne teknikere, entreprenører og leverandører — adgang, sikkerhed og "
       "arbejdstilladelser."),
      ("Sikkerhed og arbejdsmiljø",
       "LOTO, risikovurdering, arbejdstilladelser, near-miss-rapportering og værktøjsmøder.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister inden for teknik, indkøb og drift · "
     "GMP/FDA/EMA",
     [("Tværfaglig ledelse",
       "25 specialister på tværs af mekanik, el, proces og indkøb; beslutninger dokumenteret, så alle "
       "arbejdede efter samme aftale."),
      ("Projekt og økonomi",
       "tidsplan, økonomi, risiko og månedlig rapportering til ledelse og kunde; −40 % energikost gennem "
       "PDCA og standardiseret arbejde."),
      ("Aflevering",
       "FAT/SAT, IQ/OQ/PQ og valideringsdokumentation med afvigelseshåndtering — nul kritiske fund.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Ledelse af håndværkere",
       "14-personers produktions- og montageteam med kapacitetsplanlægning, flowstyring og daglige "
       "tavlemøder."),
      ("Kvalitet og sikkerhed",
       "standardiseret arbejde, arbejdstilladelser og sikkerhedsdokumentation ved montage i aktive "
       "bygninger.")]),

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

LANGUAGES = "Dansk (modersmål) · Engelsk (professionelt, skriftligt og mundtligt) · Persisk/farsi · Kørekort B"

REFERENCES = "Tidligere ledere og kunder hos Biofos (Lynetten), Novo Nordisk A/S (Kalundborg) og egne kunder i ELOHVAC — oplyses ved henvendelse."

KEYWORDS = (
    "Afdelingsleder · Service B2B · Servicechef · Personaleleder · Distanceledelse · Udekørende · "
    "Montører · Elektrikere · Kontorpersonale · Sikringsbranchen · Sikringsløsninger · Sikkerhed · "
    "Kundehenvendelser · Kundekontakt · Kundemøder · Kundeoplevelser · Drift · Salg · Vækst · Omsætning · "
    "Bundlinje · Målsætninger · Resultater · Struktur · Hindringer · Situationsbestemt · Kommunikation · "
    "Diplomatisk · Nærværende · Motiverende · El · El-teknik · Tavler · Styring · ABA · ABV · "
    "Adgangskontrol · PDS · Nød- og Panikbelysning · UPS · Fejlfinding · Service · Serviceaftaler · SLA · "
    "Responstid · KPI · Udnyttelsesgrad · Dækningsgrad · Budget · Indkøb · Leverandører · Arbejdsmiljø · "
    "APV · LOTO · Lean · 5S · PDCA · A3 · Forbedring · Kompetenceudvikling · Rekruttering · 1:1 · "
    "Tavlemøder · Power BI · Excel · SharePoint · SAP · Python · Claude · Dansk · Engelsk · Kørekort · "
    "Egen bil · Politigodkendelse · Vagtvirksomhed · Sjælland · Måløv · G4S"
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
    m.resume_header(NAME, TITLE, CONTACT, "LEDELSESPROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("LEDELSES- OG DRIFTSMETODER — ANVENDT I PRAKSIS",
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

    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER AFDELINGEN I DRIFT",
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
                  title="Ansøgning og CV — Afdelingsleder, G4S Service B2B Sjælland",
                  subject="Distanceledelse · udekørende elektrikere · kunde og service · omsætning og "
                          "bundlinje",
                  keywords=("afdelingsleder, service b2b, personaleleder, distanceledelse, udekørende, "
                            "elektrikere, sikringsløsninger, kunde, omsætning, bundlinje, kpi, sjælland, "
                            "dansk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1 (krav → løsning), CV side 2-4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_G4S_AfdelingslederServiceB2B.docx")
    print("OK", build(out))
