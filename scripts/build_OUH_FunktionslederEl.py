# -*- coding: utf-8 -*-
"""
Region Syddanmark / OUH — Funktionsleder til El-funktionen, Bygningsdrift og -service.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Funktionsleder | El-funktionen | Bygningsdrift og -service"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = ("Region Syddanmark · Odense Universitetshospital · Bygningsdrift og -service · "
             "Afdelingschef Thomas Jelling Pedersen")
SUBJECT = "Ansøgning: Funktionsleder til El-funktionen på OUH"

# ------------------------------------------------------------------ side 1
INTRO = [
    "El-funktionen på OUH driver det, der ikke må svigte: eltavler, lavspændingsgeneratorer og "
    "UPS-anlæg, nød- og panikbelysning, kaldeanlæg og rørpost — anlæg, hvor en fejl ikke er en "
    "generende afbrydelse, men kan ramme en patients behandling. Funktionslederens opgave er "
    "derfor todelt: at de kritiske anlæg er prøvet, dokumenteret og klar, og at de cirka 20 "
    "elektrikere har rammerne til at levere det i en hverdag, hvor akutte behov og planlagt "
    "vedligeholdelse konkurrerer om de samme hænder.",

    "Nedenfor er min motivation og ledelsesmæssige tilgang samt systemet, der står klar fra første "
    "dag: anlægsoversigt med prøveintervaller, prioriteringsnøgle, faglig kadence med tavlemøde, "
    "el-vagtplan med kompetencekrav og en KLS-arbejdsgang for afvigelser og lukning.",
]

BULLETS = [
    ("Kravet: overordnet ansvar for den daglige ledelse, koordinering og udvikling af funktionens "
     "medarbejdere og opgaver",
     "Løsningen er at lede gennem rammer og forventninger: en skreven forventningsaftale pr. "
     "medarbejder om ansvar, kompetence og beslutningsret, fast kadence med hver mand og et "
     "fælles tavlemøde hver morgen med dagens kritiske opgaver. Et arbejdsmiljø præget af "
     "samarbejde, ansvarlighed og faglig stolthed kommer af at kunne løse opgaven ordentligt — og "
     "af en leder, der selv tager de svære sager."),

    ("Kravet: drift og vedligeholdelse af elinstallationer og eltavler med sikker funktion",
     "Løsningen er en tilstandsbaseret el-plan: termografering af tavler med fast interval, "
     "jordfejls- og isolationsmåling, LOTO og arbejdstilladelser ved hver større opgave, og "
     "dokumentation der er opdateret, før nogen spørger. Jeg har stået med koblingsanlæg og "
     "højspænding i et 24/7-anlæg, hvor en tavlefejl stoppede driften."),

    ("Kravet: lavspændingsgeneratoranlæg og UPS-anlæg til nødstrømsforsyning",
     "Løsningen er en prøveplan pr. anlæg: månedlig prøvekørsel med last og log, kvartalsvis "
     "funktionstest af overgange og termografering af batterier. Høj driftsstabilitet er ikke et "
     "håb, men et resultat af, at nogen har prøvet anlægget, før det skal bruges."),

    ("Kravet: nød- og panikbelysning, belysning og lysstyring samt antenne- og kaldeanlæg",
     "Løsningen er en eftersynsplan pr. anlægstype med interval, ansvarlig og dokumentation — "
     "ikke en huskeliste. Anlæggene er ikke svære i sig selv; det svære er at holde 20 mænds "
     "opgaver og myndighedskrav i samme plan uden huller."),

    ("Kravet: el-vagtansvar og deltagelse i OUH's beredskabsvagt som øvrige tekniske ledere",
     "Løsningen er en bemandingsplan med kompetencekrav, varslingskæde og øvelser, så vagten kan "
     "dækkes af flere — ikke af den samme person hver gang. Jeg har haft 24/7-ansvar med "
     "beredskab og ved, at en vagtordning kun holder, hvis den er gennemprøvet."),

    ("Kravet: KLS og fagligt ansvar i overensstemmelse med regler og krav til "
     "kvalitetsledelsessystemet",
     "Løsningen er at behandle KLS som arbejdsredskab: én arbejdsgang pr. proces, "
     "afvigelser registreret med ejer og frist, og lukning først når dokumentationen er på plads. "
     "Jeg har arbejdet under GMP/FDA/EMA med revisionsspor og IQ/OQ/PQ — et "
     "kvalitetsledelsessystem virker kun, når det er nemmere at bruge end at omgå."),

    ("Kravet: struktureret planlægning, prioritering og opfølgning på drifts- og "
     "vedligeholdelsesopgaver — og løbende forbedringer af arbejdsgange",
     "Løsningen er en nedskrevet prioriteringsnøgle — patientsikkerhed og driftskritisk først, "
     "derefter myndighedskrav, planlagt vedligeholdelse og øvrige opgaver — koblet til en "
     "rullende fireugers plan og en baglog med alder. Én arbejdsgang ad gangen prøvekøres og "
     "måles, før den bliver standard."),

    ("Kravet: samarbejde på tværs af faggrupper og funktioner samt med interne og eksterne "
     "leverandører",
     "Løsningen er en snitfladeaftale pr. grænseflade — hvem gør hvad, hvornår varsles der, og "
     "hvilke arbejdsvinduer er aftalt med den kliniske afdeling — plus en leverandørplan pr. fag. "
     "Jeg har koordineret 25 specialister på tværs af mekanik, el, proces og indkøb."),

    ("Kravet: stærk el-teknisk faglighed og kendskab til regler og standarder inden for "
     "elsikkerhed",
     "Løsningen er elautoriseret maskinmester (LV/MV/HV) og B.Tech med 20 år i tekniske anlæg: "
     "eltavler, motorer, højspænding, CTS/BMS, køl og ventilation. Jeg kan selv vurdere en "
     "installation og en entreprenørs løsningsforslag — og sige fra, når sikkerheden kræver det."),
]

SYSTEM = (
    "Systemet står klar fra første dag: anlægsoversigt pr. anlægstype med prøveinterval og "
    "ansvarlig, prioriteringsnøgle og fireugers rullende plan, tavlemøde, el-vagtplan med "
    "kompetencekrav, KLS-arbejdsgang for afvigelser og leverandørplan pr. fag — ført i Excel og "
    "Power BI, med oplæg genereret i Python og Claude."
)

MIRROR = (
    "Om kravene: elautoriseret maskinmester (LV/MV/HV) og B.Tech, 20 år i tekniske anlæg og otte "
    "år med personaleansvar — fem år som driftschef i Biofos med 24/7-drift, højspænding og nul "
    "uplanlagte stop; to år med 5 elektrikere og 3 lærlinge og fuldt P&L; to år som projektleder "
    "på 37 anlægsprojekter."
)

HONEST = (
    "Det skal siges ligeud: jeg har ikke ledet en el-funktion på et hospital og ikke arbejdet i "
    "en politisk ledet organisation — min ledelse er sket i mindre enheder og i et kommunalt ejet "
    "selskab med bestyrelse og myndighedstilsyn, og rørpost har jeg ikke haft som selvstændigt "
    "ansvarsområde. Anlægstyperne lærer jeg i jeres dokumentation og sammen med fagfolkene; "
    "metoden tager jeg med."
)

CULTURE = (
    "Bygningsdrift og -service er en af fire afdelinger i Servicecenteret med cirka 1.300 "
    "medarbejdere, og OUH skal levere stabil drift i det eksisterende byggeri, samtidig med at Det "
    "nye OUH bygges og nye anlæg skal ind i samme vedligeholdelsesplan. Den overgang har jeg prøvet "
    "før — at holde et anlæg kørende, mens der blev bygget omkring det."
)

PRACTICAL = (
    "Bosat i Måløv — cirka 1 time og 45 minutter i bil til Odense, og indstillet på daglig "
    "tilstedeværelse. Kørekort B og bil, dansk på modersmålsniveau og engelsk professionelt. Kan "
    "tiltræde hurtigst muligt og indgå i beredskabsvagten."
)

CLOSING = (
    "I første samtale vil jeg gerne tale om, hvilke anlæg i El-funktionen der i dag har den største "
    "driftsrisiko — og hvordan I ved, at generatorerne og UPS'en virker, når de skal."
)

# ------------------------------------------------------------------ CV
PROFILE = (
    "Elautoriseret maskinmester (LV/MV/HV) og B.Tech med 20 år i tekniske anlæg og otte år med "
    "personaleansvar: fem år som driftschef i Biofos med 24/7-drift, højspænding, koblingsanlæg, "
    "SCADA og nul uplanlagte stop i fem år; to år med 5 elektrikere og 3 lærlinge og fuldt P&L; to "
    "år som projektleder på 37 anlægsprojekter. Arbejder med tilstandsbaseret vedligehold, "
    "prøveplaner og dokumentation — og koder selv de rapporter, ledelsen læser."
)

PRACTICE = [
    ("Personale og faglig udvikling",
     "Skreven forventningsaftale og kompetenceplan pr. medarbejder, fast kadence og tavlemøde — "
     "mandat og værktøj til at løse opgaven uden at gå på kompromis med sikkerheden."),
    ("Elinstallationer og tavler",
     "Termografering med fast interval, isolations- og jordfejlsmåling, LOTO og "
     "arbejdstilladelser; dokumentation opdateret før eftersyn."),
    ("Nødstrøm, UPS og generatorer",
     "Prøveplan pr. anlæg: månedlig prøvekørsel med last, kvartalsvis funktionstest af overgange "
     "og skreven grænseflade til de funktioner, der er afhængige af dem."),
    ("Eftersyn og myndighedskrav",
     "Nød- og panikbelysning, kalde- og antenneanlæg og rørpost i én eftersynsplan med interval, "
     "ansvarlig og dokumentation."),
    ("El-vagt og beredskab",
     "Bemandingsplan med kompetencekrav, varslingskæde og øvelser, så vagten kan dækkes af flere "
     "— ikke af den samme person hver gang."),
    ("KLS og forbedringer",
     "Én arbejdsgang pr. proces, afvigelser med ejer og frist, lukning først ved dokumentation; "
     "én forbedring prøvekørt og målt ad gangen."),
]

MODELS = [
    ("Anlægsoversigt",
     "Pr. anlægstype: prøveinterval, ansvarlig, seneste dokumentation og næste eftersyn"),
    ("Prioriteringsnøgle",
     "Patientsikkerhed og driftskritisk → myndighedskrav → planlagt vedligeholdelse → øvrige; "
     "skrevet ned og kendt af alle"),
    ("Fireugers plan",
     "Rullende plan med baglog og alder pr. opgave — akutte behov ændrer planen, ikke "
     "dokumentationen"),
    ("Tavlemøde",
     "Hver morgen: dagens kritiske opgaver, bemanding, afbrud og hvem der ejer hvad"),
    ("El-vagtplan",
     "Bemanding, kompetencekrav, varslingskæde og øvelseskadence"),
    ("KLS-arbejdsgang",
     "Afvigelse registreret med årsag, ejer og frist; lukket med dokumentation — gennemgået hver "
     "måned"),
]

ACHIEVEMENTS = [
    ("Nul uplanlagte stop i fem år",
     "24/7-anlæg med højspænding, koblingsanlæg, pumper, HVAC og køl — planlagt og "
     "tilstandsbaseret vedligehold, KPI'er i SAP og prioritering mellem afhjælpning og "
     "investering."),
    ("5 elektrikere og 3 lærlinge med fuldt P&L",
     "egen virksomhed: el-teknisk service på 40+ anlæg, udbud, tilbudsberegning, kontrakter og "
     "garantisager — med ansvar for både sikkerhed, kvalitet og bundlinje."),
    ("37 anlægsprojekter uden kritiske fund",
     "2-10 mio. kr. i eksisterende byggeri: 25 specialister koordineret på tværs af mekanik, el, "
     "proces og indkøb; FAT/SAT, IQ/OQ/PQ og aflevering med dokumentation i orden."),
    ("Cirka 40 procent lavere energikostning",
     "optimering af styringer, driftstider og ventilations- og køleanlæg frem for udskiftning — "
     "samme princip som i en belysnings- og lysstyringsopgave."),
]

EXPERIENCE = [
    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7-anlæg · højspænding, koblingsanlæg, pumper, HVAC og køl · budget i SAP",
     [("Drift, vedligehold og driftssikkerhed",
       "planlagt og tilstandsbaseret vedligehold, KPI'er i SAP og nul uplanlagte stop i fem år på "
       "et anlæg, hvor driften ikke kunne vente."),
      ("Sikkerhed, leverandører og beredskab",
       "LOTO og arbejdstilladelser, koordinering af egne teknikere, entreprenører og rådgivere, "
       "garantisager og nærved-hændelser fulgt til lukning.")]),

    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og "
     "leverandøraftaler",
     [("El-teknisk service, sikkerhed og kvalitet",
       "serviceaftaler, responstider og kvalitetsopfølgning; rekruttering, oplæringsplaner og "
       "arbejdsmiljø som fast punkt på tavlemødet."),
      ("Kunder, tilbud og leverandører",
       "tilbudsberegning, udbud og leverandøraftaler med fuldt ansvar for bundlinjen.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2-10 mio. kr. · 25 specialister · GMP/FDA/EMA",
     [("Koordinering, snitflader og aflevering",
       "25 specialister koordineret på tværs af mekanik, el, proces og indkøb; FAT/SAT, IQ/OQ/PQ "
       "og aflevering uden kritiske fund."),
      ("Ændringer, dokumentation og driftsoverlevering",
       "ændringshåndtering og teknisk dokumentation, der bestod revision — og overlevering til "
       "drift med skrevne grænseflader.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2-10 mio. kr.)",
     [("Personale, kapacitet og leverance",
       "14-personers team med kapacitetsplanlægning, daglige tavlemøder og opfølgning på den "
       "enkelte — og 11 samtidige entrepriser i eksisterende byggeri.")]),

    ("Elektromekaniker / Produktionsteamleder",
     "ARJ Engineering · Teheran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · skiftplanlægning, materialestyring og lager",
     [("Fremstilling og teknisk problemløsning",
       "skiftplanlægning, materialestyring og målopfølgning; reparation og diagnosticering gennem "
       "struktureret root cause-analyse.")]),
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
    ("Lean — værdistrømsanalyse, standardarbejde, 5S, A3 og Kaizen",
     "Anvendt i drift, produktion og projekter · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og projekter · 2017 – nu"),
]

LANGUAGES = ("Dansk (modersmål, skrift og tale) · Engelsk (professionelt, skrift og tale) · "
             "Persisk/farsi · Kørekort B (kategori B)")

PRACTICAL_CV = (
    "Bosat i Måløv — cirka 1 time og 45 minutter i bil til Odense; indstillet på daglig "
    "tilstedeværelse og på at indgå i beredskabsvagten. Kørekort kategori B og bil, dansk på "
    "modersmålsniveau og engelsk professionelt. Kan tiltræde hurtigst muligt."
)

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Biofos (Lynetten), Novo Nordisk A/S, "
              "Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Elektrikerne i El-funktionen",
     "Tydelig forventningsaftale og kompetenceplan, fast sparring og en leder, der tager de svære "
     "sikkerhedsspørgsmål sammen med dem — ikke i stedet for dem."),
    ("Afdelingschefen og de øvrige funktionsledere",
     "Én rapport på få tal og aftalte eskaleringsgrænser, så beslutninger kommer op i tide og med "
     "et klart oplæg; fælles standarder på tværs af fagene."),
    ("Kliniske afdelinger og interne samarbejdspartnere",
     "Snitfladeaftale pr. grænseflade: hvem gør hvad, hvornår varsles der, og hvilke "
     "arbejdsvinduer er aftalt — driften skal ikke overraskes."),
    ("Leverandører og rådgivere",
     "Serviceaftaler med responstid og pris, aftalte arbejdsvinduer og ét ansvar pr. grænseflade "
     "— kvalitet dokumenteret ved aflevering."),
]

FIRST90 = [
    ("Dage 1–30",
     "Gået funktionen igennem anlæg for anlæg med den ansvarlige elektriker: prøveintervaller, "
     "kendte fejl, bagloggens alder og hvor der i dag ingen ejer er af en opgave."),
    ("Dage 30–60",
     "Anlægsoversigt og prioriteringsnøgle indført; tavlemøde og kadence med hver medarbejder "
     "aftalt; første månedlige rapport til afdelingschefen og gennemgang af el-vagtplanen."),
    ("Dage 60–90",
     "Prøveplan for generatorer og UPS prøvekørt og dokumenteret; KLS-arbejdsgang for afvigelser "
     "i brug; én arbejdsgang standardiseret med klinikken om varsling og arbejdsvinduer."),
    ("Måned 3–6",
     "Bagloggen er kendt og prioriteret, eftersyn overholdes, og kompetenceplanen for "
     "funktionen er lagt — også med blik på de anlæg, der skal overtages fra Det nye OUH."),
    ("Måned 6–12",
     "Funktionen leverer stabilt på sikkerhed, kvalitet og fremdrift, og el-funktionen er kendt "
     "som den del af bygningsdriften, der kan svare for sig — også når hospitalet bygger videre."),
]

KEYWORDS = (
    "Funktionsleder · El-funktionen · Odense Universitetshospital · Bygningsdrift og -service · "
    "Servicecenteret · Region Syddanmark · Elektrikere · El-teknisk · Elinstallationer · "
    "Eltavler · Eltavleanlæg · Lavspændingsgeneratoranlæg · UPS-anlæg · Nødstrømsforsyning · "
    "Nødbelysning · Panikbelysning · Belysning · Lysstyring · Kaldeanlæg · Antenneanlæg · "
    "Rørpostsystem · El-vagt · Vagtansvar · Beredskabsvagt · KLS · Kvalitetsledelsessystem · "
    "Elsikkerhed · Myndighedskrav · Drift · Vedligeholdelse · Driftsstabilitet · Planlægning · "
    "Prioritering · Opfølgning · Personaleledelse · Personaleansvar · Arbejdsmiljø · Faglig "
    "stolthed · Samarbejde · Ansvar · Sikkerhed · Kvalitet · Leverandører · Arbejdsgange · "
    "Forbedringer · Komplekse tekniske installationer · Højspænding · Koblingsanlæg · LOTO · "
    "Tavlemøde · Maskinmester · Lean · SAP · CTS"
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
        m.para(t, after=52, line=230)

    for label, body in BULLETS:
        m.bullet(label, body, after=1, line=216)

    m.para(SYSTEM, after=50, line=226)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=0, line=210)

    m.meta("Med venlig hilsen · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "LEDELSESPROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("EL-FUNKTIONENS STYRING — ANVENDT I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER EL-FUNKTIONEN I RYTMEN",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN LEDES FUNKTIONEN — DE FIRE PARTER")
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

    from docx.oxml import OxmlElement as _OE
    for _tbl in m.doc.tables:
        for _tr in _tbl._tbl.tr_lst:
            _pr = _tr.get_or_add_trPr()
            _el = _OE("w:cantSplit")
            _pr.append(_el)

    m.save(path)


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_OUH_FunktionslederEl.docx")
    build(out)
    print("OK " + out)
