# -*- coding: utf-8 -*-
"""
PKA Ejendomme — Driftschef (bolig- og erhvervsejendomme, Sjælland og Storkøbenhavn).
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Driftschef | Ejendomsdrift, vedligehold og ledelse"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = "PKA Ejendomme · via Hammer Andersen"
SUBJECT = "Ansøgning: Driftschef til PKA Ejendomme"

# ------------------------------------------------------------------ side 1
INTRO = [
    "PKA Ejendomme driver en portefølje med både bolig- og erhvervsejendomme på Sjælland og i "
    "Storkøbenhavn, og driftschefens opgave er at få to ting til at lykkes samtidig: beboerne skal "
    "møde en ren, ryddelig og velvedligeholdt ejendom med et fast og synligt ansigt i hverdagen, og "
    "erhvervslejerne skal have lokaler, der understøtter deres virksomhed. Det er ikke en "
    "servicefornemmelse, men en driftsmodel, hvor kvalitet, responstider og vedligeholdelse er "
    "aftalt og målt, og hvor økonomien pr. ejendom er kendt, før den bliver et problem.",

    "Nedenfor er min motivation og ledelsesmæssige tilgang samt systemet, der står klar fra første "
    "dag: ejendomskort pr. ejendom, servicekatalog med svartider, vedligeholdelsesplan og "
    "driftsbudget med månedlig opfølgning samt faglig kadence med viceværterne.",
]

BULLETS = [
    ("Kravet: lede og udvikle teamet med fokus på trivsel, faglighed og resultater — og lede og "
     "motivere viceværterne på ejendommene",
     "Løsningen er at lede gennem rammer og forventninger: en skreven forventningsaftale pr. "
     "medarbejder om ansvar, service og beslutningsret, fast kadence med hver vicevært og et "
     "fælles tavlemøde hver uge. Viceværten er ejendommens ansigt udadtil og skal derfor have "
     "mandat, værktøj og en leder, der bakker op i svære sager."),

    ("Kravet: bære det tekniske, økonomiske og ledelsesmæssige ansvar for driften af egen "
     "portefølje",
     "Løsningen er en ejendomsmodel, der gør porteføljen styrbar: ejendomskort pr. ejendom med "
     "anlæg, aftaler, nøgletal, kendte fejl og næste beslutning — gennemgået på et fast månedligt "
     "driftsmøde med de øvrige driftschefer. En portefølje kan kun ledes på tal, der er opdaterede."),

    ("Kravet: udarbejde og eksekvere drift- og vedligeholdelsesbudgetter samt forestå "
     "økonomiopfølgning på drifts- og vedligeholdelsesomkostninger",
     "Løsningen er et budget pr. ejendom i tre lag — akut og sikkerhed, lovpligtigt og planlagt "
     "vedligehold — med månedlig opfølgning på forbrug, serviceudgifter og timer. Jeg har drevet "
     "fuldt P&L med plan og prognose og styret vedligeholdelsesbudget i et 24/7-anlæg."),

    ("Kravet: sikre velvedligeholdte ejendomme og sund og god drift i dagligdagen med blik for "
     "ressourceforbrug og langsigtet værdi",
     "Løsningen er en vedligeholdelsesplan pr. ejendom på et, tre og ti år, koblet til "
     "tilstandsvurdering og til Svanemærket bygningsdrift som fælles instruks. Jeg har kørt "
     "tilstandsbaseret vedligehold på pumper, ventilation, køl og koblingsanlæg og sænket "
     "energikostningen cirka 40 procent ved optimering frem for udskiftning."),

    ("Kravet: styre og optimere serviceaftaler og driftsudgifter",
     "Løsningen er et servicekatalog pr. fag med ydelse, responstid, pris og grænseflade, og en "
     "leverandørplan pr. ejendom, der revideres én gang om året. Jeg har både købt serviceaftaler "
     "og skullet levere på dem."),

    ("Kravet: løbende dialog med beboere og erhvervskunder og sikre en tryg oplevelse",
     "Løsningen er aftalte svartider pr. henvendelsestype, en skreven klagevej og svar tilbage "
     "til den enkelte beboer eller lejer — ikke kun til systemet. Jeg har bygget en "
     "serviceforretning op fra bunden."),

    ("Kravet: håndtere mindre vedligeholdelses- og byggesager, om- og tilbygninger samt "
     "forsikringssager",
     "Løsningen er ét kort pr. sag med årsag, løsning, forsikringsdækning, entreprenør, tid og "
     "pris — og lukning først, når dokumentationen er arkiveret. Jeg har gennemført 37 "
     "anlægsprojekter i eksisterende byggeri og håndteret garanti- og forsikringssager."),

    ("Kravet: byggeteknisk værktøjskasse — drift, vedligeholdelse og investeringer i "
     "ejendommene",
     "Løsningen er elautoriseret maskinmester (LV/MV/HV) og B.Tech med 20 år i tekniske anlæg: el "
     "og højspænding, ventilation, køl, varme, pumper og CTS/BMS. Jeg kan selv vurdere en tilstand, "
     "udfordre en entreprenørs løsningsforslag og vælge mellem afhjælpning og investering."),

    ("Kravet: tæt samarbejde med de øvrige driftschefer, bolig- og erhvervsteams og eksterne "
     "samarbejdspartnere",
     "Løsningen er fælles arbejdsgange, der er skrevet ned og prøvekørt: én vej for en "
     "udflytning, én for en skade, én for et lejertilsagn, så samme opgave ikke løses forskelligt "
     "i to teams. Jeg har koordineret 25 specialister på tværs af mekanik, el og indkøb."),
]

SYSTEM = (
    "Systemet står klar fra første dag: ejendomskort på én side pr. ejendom, servicekatalog med "
    "svartider pr. fag, vedligeholdelsesplan, driftsbudget pr. ejendom med månedlig opfølgning, "
    "leverandørplan og ugentlig kadence med viceværterne — ført i Excel og Power BI, med "
    "KPI-tavlen og ledelsesoplæg genereret i Python og Claude."
)

MIRROR = (
    "Om kravene: elautoriseret maskinmester (LV/MV/HV) og B.Tech, 20 år i tekniske anlæg og otte "
    "år med personaleansvar — fem år som driftschef i Biofos med budget i SAP, to år som teknisk "
    "direktør med fuldt P&L og 40+ serviceanlæg, to år som leder for et 14-mands team."
)

HONEST = (
    "Det skal siges ligeud: jeg har ikke været driftschef for en udlejningsportefølje med beboere "
    "og erhvervslejere som kunder, og min erfaring er teknisk drift i 24/7-anlæg og projekter i "
    "eksisterende byggeri. Til gengæld har jeg fem år i et kommunalt ejet selskab med bestyrelse "
    "og myndighedstilsyn, drevet servicevirksomhed med egne kunder og ansvar for drift og "
    "bundlinje — og holdt et anlæg kørende, mens der blev bygget omkring det."
)

CULTURE = (
    "PKA Ejendomme blev etableret i 2023, overtog driften i eget regi i december 2024 og er på få "
    "år vokset til cirka 150 medarbejdere — med viceværterne som det faste og synlige ansigt ude "
    "på ejendommene og en tredobbelt bundlinje som styring. At arbejdsgange og samarbejde stadig "
    "udvikles betyder, at driftschefen skal bygge standarder, ikke bare vedligeholde dem."
)

PRACTICAL = (
    "Bosat i Måløv — cirka 10 minutter i bil til Skovlunde og kort til porteføljen i "
    "Storkøbenhavn og på Sjælland. Kørekort B og bil, dansk på modersmålsniveau og engelsk "
    "professionelt. Kan tiltræde hurtigst muligt."
)

CLOSING = (
    "I første samtale vil jeg gerne tale om, hvilke tre ejendomme der i dag kræver mest "
    "opmærksomhed — og hvordan I måler, at viceværten leverer den oplevelse, beboerne husker."
)

# ------------------------------------------------------------------ CV
PROFILE = (
    "Teknisk leder med 20 år i drift og projekter og otte år med personaleansvar: fem år som "
    "driftschef i Biofos med budget i SAP og nul uplanlagte stop i fem år, to år som teknisk "
    "direktør med 40+ serviceanlæg og fuldt P&L, to år som projektleder på 37 samtidige "
    "anlægsprojekter og to år som projekt- og værkstedsleder for et 14-mands team. Arbejder med "
    "ejendomskort, servicekataloger, vedligeholdelsesplaner og KPI-tavler — og koder selv de "
    "oplæg, ledelsen læser."
)

PRACTICE = [
    ("Ledelse af viceværter",
     "Skreven forventningsaftale pr. medarbejder om ansvar, service og beslutningsret, fast "
     "kadence og ugentligt tavlemøde — mandat og værktøj til at løse sagen i gården."),
    ("Portefølje og ejendomskort",
     "Én side pr. ejendom med anlæg, aftaler, nøgletal, kendte fejl og næste beslutning; "
     "månedligt driftsmøde med de øvrige driftschefer."),
    ("Budget og økonomiopfølgning",
     "Budget pr. ejendom i tre lag — akut og sikkerhed, lovpligtigt, planlagt — med månedlig "
     "opfølgning på forbrug, serviceudgifter og egne timer."),
    ("Vedligehold og langsigtet værdi",
     "Vedligeholdelsesplan på et, tre og ti år på tilstandsvurdering; Svanemærket bygningsdrift "
     "som fælles instruks og energiforbrug som fast punkt."),
    ("Serviceaftaler og leverandører",
     "Servicekatalog pr. fag med ydelse, responstid, pris og grænseflade; årlig revision af "
     "leverandørplanen pr. ejendom."),
    ("Beboere og erhvervslejere",
     "Aftalte svartider pr. henvendelsestype, skreven klagevej og tilbagelevering til den enkelte "
     "— ikke kun til systemet."),
]

MODELS = [
    ("Ejendomskort",
     "Én side pr. ejendom: tekniske anlæg, aftaler, nøgletal, kendte fejl og næste beslutning"),
    ("Servicekatalog",
     "Ydelse, responstid, pris og grænseflade pr. fag — aftalt med beboerne som serviceniveau"),
    ("Vedligeholdelsesplan",
     "Et, tre og ti år pr. ejendom på tilstandsvurdering; akut og lovpligtigt adskilt fra "
     "planlagt vedligehold"),
    ("Driftsbudget",
     "Tre lag pr. ejendom med månedlig opfølgning på forbrug, serviceudgifter og egne timer"),
    ("Leverandørplan",
     "Én plan pr. ejendom pr. fag med performance-review og årlig revision af aftaler"),
    ("KPI-tavle",
     "Svartider, klager, energiforbrug, vedligeholdelsesbaglog og driftsudgifter pr. kvadratmeter"),
]

ACHIEVEMENTS = [
    ("Nul uplanlagte stop i fem år",
     "24/7-anlæg med pumper, ventilation, køl, koblingsanlæg og højspænding — tilstandsbaseret "
     "vedligehold, KPI'er i SAP og prioritering mellem afhjælpning og investering."),
    ("40+ serviceanlæg med fuldt P&L",
     "egen virksomhed: serviceaftaler, udbud, tilbudsberegning, kontrakter og garantisager — "
     "med ansvar for både kvalitet og bundlinje."),
    ("Cirka 40 procent lavere energikostning",
     "målrettet optimering af styringer, driftstider og ventilations- og køleanlæg frem for "
     "udskiftning — samme princip som i en ejendomsportefølje."),
    ("37 anlægsprojekter uden kritiske fund",
     "2-10 mio. kr. i eksisterende byggeri: 25 specialister koordineret på tværs af mekanik, el, "
     "proces og indkøb, FAT/SAT og aflevering med dokumentation i orden."),
]

EXPERIENCE = [
    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og "
     "leverandøraftaler",
     [("Serviceaftaler, kunder og kvalitet",
       "servicekatalog, responstider og aftaler pr. kunde; tilbudsberegning, udbud og "
       "leverandøraftaler med fuldt ansvar for bundlinjen."),
      ("Organisation, rekruttering og arbejdsmiljø",
       "byggede virksomheden op fra bunden: rekruttering, oplæringsplaner, arbejdsplaner og "
       "sikkerhed som fast punkt på tavlemødet.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2-10 mio. kr. · 25 specialister · GMP/FDA/EMA",
     [("Koordinering, snitflader og aflevering",
       "25 specialister koordineret på tværs af mekanik, el, proces og indkøb; fremdrift og "
       "rapportering til styregruppe; FAT/SAT, IQ/OQ/PQ og aflevering uden kritiske fund."),
      ("Ændringer, dokumentation og driftsoverlevering",
       "ændringshåndtering og teknisk dokumentation, der bestod revision — og overlevering til "
       "drift med skrevne grænseflader.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7-anlæg · pumper, HVAC, køl, koblingsanlæg og højspænding · budget i SAP",
     [("Drift, vedligehold og driftssikkerhed",
       "planlagt og tilstandsbaseret vedligehold, KPI'er i SAP og nul uplanlagte stop i fem år på "
       "et anlæg, hvor driften ikke kunne vente."),
      ("Sikkerhed, leverandører og beredskab",
       "koordinering af egne teknikere, entreprenører og rådgivere — LOTO, arbejdstilladelser, "
       "garantisager og nærved-hændelser fulgt til lukning.")]),

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
    "Bosat i Måløv — cirka 10 minutter i bil til Skovlunde og kort til porteføljen i "
    "Storkøbenhavn og på Sjælland. Kørekort kategori B og bil, dansk på modersmålsniveau og "
    "engelsk professionelt. Kan tiltræde hurtigst muligt."
)

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Biofos (Lynetten), Novo Nordisk A/S, "
              "Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Viceværterne",
     "Tydelig forventningsaftale om service og ansvar, fast sparring og en leder, der tager de "
     "svære beboersager sammen med dem — ikke i stedet for dem."),
    ("Den tekniske chef og de øvrige driftschefer",
     "Én rapport på få tal og aftalte eskaleringsgrænser, så beslutninger kommer op i tide og "
     "med et klart oplæg; fælles standarder frem for lokale løsninger."),
    ("Bolig- og erhvervsteams samt økonomi",
     "Skrevne arbejdsgange for udflytning, skade og lejertilsagn — én vej pr. opgave, så kunden "
     "møder samme svar uanset team."),
    ("Leverandører, rådgivere og entreprenører",
     "Serviceaftaler med responstid og pris, aftalte arbejdsvinduer og ét ansvar pr. grænseflade "
     "— kvalitet dokumenteret ved aflevering."),
]

FIRST90 = [
    ("Dage 1–30",
     "Mødt viceværterne og de øvrige driftschefer, gået porteføljen igennem ejendom for ejendom: "
     "hvad er lovet til beboerne, hvor er de kendte fejl, og hvilke sager mangler en ejer."),
    ("Dage 30–60",
     "Ejendomskort og servicekatalog indført på de ejendomme, hvor det haster mest; "
     "vedligeholdelsesplanen lagt i tre lag; første månedlige driftsrapport til den tekniske "
     "chef."),
    ("Dage 60–90",
     "Leverandørplan pr. ejendom revideret, KPI-tavle i brug på tavlemødet, og én arbejdsgang "
     "(skade eller udflytning) standardiseret og prøvekørt på tværs af bolig og erhverv."),
    ("Måned 3–6",
     "Budget, forbrug og svartider følges månedligt pr. ejendom; viceværterne bruger selv "
     "værktøjerne; vedligeholdelsesbagloggen er kendt og prioriteret."),
    ("Måned 6–12",
     "Driften leverer stabilt på service og økonomi, og porteføljens langsigtede værdi er "
     "understøttet af en vedligeholdelsesplan, der kan holdes — også når der kommer nye "
     "ejendomme ind."),
]

KEYWORDS = (
    "Driftschef · PKA Ejendomme · Viceværter · Ejendomsportefølje · Bolig- og erhvervsejendomme "
    "· Sjælland · Storkøbenhavn · Teknisk chef · Daglig drift · Vedligeholdelse · Ejendomsdrift · "
    "Driftsherrerolle · Kvalitet · Beboere · Erhvervskunder · Service · Ledelse og motivation · "
    "Faglig kvalitet · Tryg oplevelse · Ambassadører · Byggeteknisk · Drift- og "
    "vedligeholdelsesbudgetter · Økonomiopfølgning · Serviceaftaler · Driftsudgifter · "
    "Vedligeholdelses- og byggesager · Forsikringssager · Leverandører · Samarbejdspartnere · "
    "Egen portefølje · Langsigtet værdi · Ressourceforbrug · Ordentlighed · Struktureret · "
    "Kvalitetsbevidst · Løsningsorienteret · Selvstændigt · Teamplayer · Ejendomsbranchen · "
    "Udlejer · Administrator · Almen boligorganisation · Bolig- og erhvervsteams · Udlejning · "
    "Projekter · Ejendomsudvikling · Trivsel · Faglighed · Resultater · Om- og tilbygninger · "
    "Svanemærket · Lean · SAP · CTS · Maskinmester"
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

    m.models_table("EJENDOMSDRIFFTENS STYRING — ANVENDT I PRAKSIS",
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

    m.section("SÅDAN LEDES PORTEFØLJEN — DE FIRE PARTER")
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
    out = os.path.join(ROOT, "Shahram_Ajloo_PKAEjendomme_Driftschef.docx")
    build(out)
    print("OK " + out)
