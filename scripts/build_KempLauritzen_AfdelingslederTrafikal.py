# -*- coding: utf-8 -*-
"""
Kemp & Lauritzen A/S — Forretningsorienteret Afdelingsleder til Trafikal Infrastruktur (Hvidovre + Korsør).
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Afdelingsleder | Trafikal Infrastruktur | Energi Infrastruktur"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = ("Kemp & Lauritzen A/S · Energi Infrastruktur · Divisionsdirektør "
             "Stine Ruberg Christensen · Hvidovre")
SUBJECT = "Ansøgning: Forretningsorienteret afdelingsleder til Trafikal Infrastruktur"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Trafikal infrastruktur er den del af teknikbranchen, hvor arbejdet skal ligge i de vinduer, der "
    "bliver givet: Banedanmark, Metroen, DSB, Sund & Bælt, Lokaltog og Letbanen stiller krav om "
    "sikkerhed, varsling og dokumentation, før en tekniker må gå i gang. En afdeling med fire "
    "projektledere og 25 teknikere leverer kun, hvis kapacitet, kontrakter og økonomi styres som ét "
    "system. Afdelingslederens opgave er derfor ikke selv at stå i sporet, men at gøre det muligt "
    "for de 29 at gøre det sikkert, til tiden og med den indtjening, der er lovet.",

    "Nedenfor er min motivation og ledelsesmæssige tilgang samt systemet, der står klar fra første "
    "dag: portefølje- og kapacitetsmodel pr. måned, prioritetsnøgle for driftsvinduer, KPI-rapport "
    "pr. kontrakt, snitflademodel mod kunderne og én plan for Hvidovre og Korsør.",
]

BULLETS = [
    ("Kravet: ledelse og udvikling af projektledere og teknikere — ledelse af ledere",
     "Løsningen er at lede gennem rammer og forventninger: en skreven forventningsaftale pr. "
     "projektleder om resultat, beslutningsret og eskaleringsgrænse, en fast en-til-en hver anden "
     "uge og et fælles afdelingsmøde, hvor tallene ligger åbent. Jeg har ledet et 14-mands team og "
     "koordineret 25 specialister på tværs af mekanik, el og indkøb."),

    ("Kravet: sikre høj trivsel, motivation og medarbejderengagement — som synlig leder",
     "Løsningen er tilstedeværelse, der kan planlægges: faste dage på begge lokationer, tavlemøde "
     "med sikkerhed og dagens opgaver og MUS med en kompetenceplan pr. medarbejder — for sikkerhed "
     "kan ikke delegeres væk."),

    ("Kravet: økonomisk ansvar for afdelingens omsætning, indtjening og kapacitetsstyring",
     "Løsningen er en månedlig afdelingsrapport på få tal — omsætning, dækningsgrad, "
     "faktureringsgrad og prognose — koblet til en kapacitetsmodel, hvor timer og kompetencer pr. "
     "uge er synlige, før ordrebogen vokser. Jeg har drevet fuldt P&L med plan og prognose og "
     "styret budget i SAP i et 24/7-anlæg."),

    ("Kravet: udvikle kunderelationer og identificere nye forretningsmuligheder",
     "Løsningen er at komme med et fagligt oplæg, ikke bare en faktura: en kvartalsgennemgang pr. "
     "kunde med KPI'er, næste sæsons arbejdsvinduer og forslag til det, kunden endnu ikke har "
     "bestilt. Jeg har bygget en servicebaseret forretning op fra bunden med 40+ anlæg."),

    ("Kravet: sikre høj kvalitet og leveringssikkerhed på tværs af opgaver og kontrakter",
     "Løsningen er én arbejdsgang pr. proces — opstart, ændring, aflevering og dokumentation — "
     "prøvekørt på ét projekt og målt, før den bliver standard, og en afvigelsesliste med ejer og "
     "frist, der gennemgås hver måned. Jeg har arbejdet under GMP/FDA/EMA med revisionsspor og "
     "leveret 37 anlægsprojekter uden kritiske fund."),

    ("Kravet: strategisk ressourceplanlægning og prioritering af afdelingens aktiviteter",
     "Løsningen er en nedskrevet prioritetsnøgle: sikkerhed og trafikale bindinger først, derefter "
     "kontraktkrav og KPI-bøder, planlagt vedligeholdelse og til sidst øvrige opgaver — koblet til "
     "en rullende fireugers plan og en baglog med alder. Når vinduerne flytter sig, ændrer det "
     "planen, ikke dokumentationen."),

    ("Kravet: opfølgning på kontrakter, KPI'er og kundeaftaler",
     "Løsningen er et kontraktkort pr. kunde: ydelser, responstider, KPI-formel, datakilde, "
     "grænseværdi og bod, med en månedlig måling og en navngiven ejer. Som driftschef i Biofos "
     "fulgte jeg KPI'er i SAP og havde nul uplanlagte stop i fem år — måling er ikke en rapport, "
     "det er en beslutning."),

    ("Kravet: tæt samarbejde med kunder, myndigheder og interne interessenter",
     "Løsningen er en snitfladeaftale pr. grænseflade: hvem gør hvad, hvornår varsles der, og "
     "hvilke arbejdsvinduer er aftalt med driften og myndigheden — skriftligt, ikke på husk. Fem "
     "år i et kommunalt ejet selskab med bestyrelse og myndighedstilsyn har lært mig, hvordan "
     "den dialog skal føres."),

    ("Kravet: bidrage til den fortsatte udvikling af forretningsområdet Trafikal Infrastruktur",
     "Løsningen er el-teknisk tyngde som løftestang: elautoriseret maskinmester (LV/MV/HV) og "
     "B.Tech med 20 år i tekniske anlæg — eltavler, højspænding, CTS/BMS, køl og ventilation. "
     "Jeg kan gå ind i en sag fagligt, udfordre en løsning og tale med teknikerne på deres egne "
     "vilkår."),
]

SYSTEM = (
    "Systemet står klar fra første dag: portefølje- og kapacitetsmodel pr. måned, prioritetsnøgle "
    "for driftsvinduer, kontraktkort med KPI-formler og grænseværdier, afdelingsrapport på få tal "
    "og en kalender, hvor Hvidovre og Korsør er planlagt — ført i Excel og Power BI, med oplæg "
    "genereret i Python og Claude."
)

MIRROR = (
    "Om kravene: elautoriseret maskinmester (LV/MV/HV) og B.Tech, 20 år i tekniske anlæg og otte år "
    "med personaleansvar — to år med 5 elektrikere og 3 lærlinge og fuldt P&L, to år som leder af "
    "et 14-mands team med 11 samtidige entrepriser, fem år som driftschef med budget i SAP og nul "
    "uplanlagte stop, to år som projektleder på 37 anlægsprojekter."
)

HONEST = (
    "Det skal siges ligeud: jeg har ikke ledet en afdeling med fire projektledere og 25 teknikere i "
    "trafikal infrastruktur og ikke arbejdet på Banedanmark-, Metro- eller Sund & Bælt-kontrakter. "
    "Ledelse af ledere er hidtil sket i mindre enheder, og min erfaring er tekniske anlæg og "
    "service — ikke jernbaneteknik. Til gengæld har jeg fem år i et kommunalt ejet selskab med "
    "bestyrelse og myndighedstilsyn, bygget en servicebaseret forretning med eget P&L og holdt et "
    "anlæg kørende i fem år uden uplanlagte stop."
)

CULTURE = (
    "Kemp & Lauritzen er 3.000 medarbejdere, ejet af fonden, og kalder sig landets førende digitale "
    "og grønne teknikpartner. Kulturen er beskrevet med ét ord: ordentlighed. I trafikal "
    "infrastruktur betyder ordentlighed, at varslingen er sendt, dokumentationen er ajour, og at "
    "næste hold ikke skal gætte, hvad der blev lavet. Derfor er KPI- og kontraktopfølgning ikke "
    "administration i denne rolle — det er, hvor ordentlighed bliver synlig for kunden."
)

PRACTICAL = (
    "Bosat i Måløv — cirka 35 minutter i bil til Hvidovre og cirka 1 time og 10 minutter til Korsør; "
    "fast ugentlig tilstedeværelse i Korsør er indregnet i planlægningen. Kørekort B og bil, dansk "
    "på modersmålsniveau og engelsk professionelt. Kan tiltræde hurtigst muligt."
)

CLOSING = (
    "I første samtale vil jeg gerne tale om, hvilke kontrakter der i dag har den største risiko for "
    "KPI-bøder — og hvordan I ser kapaciteten, før ordrebogen vokser."
)

# ------------------------------------------------------------------ CV
PROFILE = (
    "Teknisk leder med 20 år i anlæg, service og drift og otte år med personaleansvar: to år med 5 "
    "elektrikere og 3 lærlinge og fuldt P&L, to år som leder af et 14-mands team med 11 samtidige "
    "entrepriser, fem år som driftschef med budget i SAP og nul uplanlagte stop samt to år som "
    "projektleder på 37 anlægsprojekter. Arbejder med kapacitetsmodeller, kontraktkort og KPI-tavler."
)

PRACTICE = [
    ("Ledelse af ledere",
     "Skreven forventningsaftale pr. projektleder om resultat, beslutningsret og "
     "eskaleringsgrænse; en-til-en hver anden uge og fælles afdelingsmøde, hvor tallene er åbne."),
    ("Økonomi og kapacitet",
     "Månedlig afdelingsrapport på omsætning, dækningsgrad, faktureringsgrad og prognose; "
     "kapacitetsmodel med timer og kompetencer pr. uge."),
    ("Driftsvinduer og prioritering",
     "Nedskrevet prioritetsnøgle: sikkerhed og trafikale bindinger → kontraktkrav og KPI-bøder → "
     "planlagt vedligeholdelse → øvrige; rullende fireugers plan."),
    ("Kontrakter og KPI",
     "Kontraktkort pr. kunde med ydelser, responstider, KPI-formel, datakilde, grænseværdi og "
     "bod; månedlig måling med navngiven ejer."),
    ("Kvalitet og leveringssikkerhed",
     "Én arbejdsgang pr. proces prøvekørt og målt før udrulning; afvigelser med ejer og frist."),
    ("To lokationer",
     "Fast ugentlig tilstedeværelse i Korsør, fælles tavlemøde og én arbejdsgang, der gælder "
     "begge steder — standarder frem for lokale løsninger."),
]

MODELS = [
    ("Portefølje og kapacitet",
     "Pr. måned: ordrebog, timer og kompetencer pr. uge, igangværende sager og prognose — "
     "kapaciteten ses, før ordrebogen vokser"),
    ("Prioritetsnøgle",
     "Sikkerhed og trafikale bindinger → kontraktkrav og KPI-bøder → planlagt vedligeholdelse → "
     "øvrige; skrevet ned og kendt af alle"),
    ("Kontraktkort",
     "Pr. kunde: ydelser, responstider, KPI-formel, datakilde, grænseværdi og bod — med ejer"),
    ("Afdelingsrapport",
     "Månedligt på få tal: omsætning, dækningsgrad, faktureringsgrad, afvigelser og næste "
     "beslutning"),
    ("Afvigelsesliste",
     "Hændelse eller KPI-afvigelse med årsag, ejer og frist; lukket med dokumentation"),
    ("Lokationskalender",
     "Hvidovre og Korsør planlagt med faste dage, tavlemøder og fælles standarder"),
]

ACHIEVEMENTS = [
    ("Nul uplanlagte stop i fem år",
     "24/7-anlæg med højspænding, koblingsanlæg, pumper, HVAC og køl — KPI'er i SAP, prioritering "
     "mellem afhjælpning og investering og en driftsorganisation, der ikke blev overrasket."),
    ("40+ serviceanlæg med fuldt P&L",
     "egen virksomhed: serviceaftaler med responstider, udbud, tilbudsberegning, kontrakter og "
     "garantisager — ansvar for både kvalitet, sikkerhed og bundlinje."),
    ("14-mands team med 11 samtidige entrepriser",
     "kapacitetsplanlægning, daglige tavlemøder og tydelig prioritering i eksisterende byggeri med "
     "brugere omkring os."),
    ("37 anlægsprojekter uden kritiske fund",
     "2-10 mio. kr.: 25 specialister koordineret på tværs af mekanik, el, proces og indkøb; "
     "FAT/SAT, IQ/OQ/PQ og aflevering med dokumentation i orden."),
]

EXPERIENCE = [
    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og "
     "leverandøraftaler",
     [("Serviceaftaler, kunder og indtjening",
       "servicekatalog med responstider, aftaler pr. kunde, tilbudsberegning og "
       "leverandøraftaler med fuldt ansvar for dækningsgrad og bundlinje."),
      ("Organisation, sikkerhed og arbejdsmiljø",
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
     "24/7-anlæg · højspænding, koblingsanlæg, pumper, HVAC og køl · budget i SAP",
     [("Drift, vedligehold og driftssikkerhed",
       "planlagt og tilstandsbaseret vedligehold, KPI'er i SAP og nul uplanlagte stop i fem år på "
       "et anlæg, hvor driften ikke kunne vente."),
      ("Sikkerhed, leverandører og beredskab",
       "LOTO og arbejdstilladelser, koordinering af egne teknikere, entreprenører og rådgivere, "
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
    "Bosat i Måløv — cirka 35 minutter i bil til Hvidovre og cirka 1 time og 10 minutter til "
    "Korsør; fast ugentlig tilstedeværelse i Korsør er indregnet. Kørekort kategori B og bil, dansk "
    "på modersmålsniveau og engelsk professionelt. Kan tiltræde hurtigst muligt."
)

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Novo Nordisk A/S, Biofos (Lynetten), "
              "Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Projektlederne",
     "Skreven forventningsaftale om resultat, beslutningsret og eskaleringsgrænse, fast sparring og "
     "en leder, der tager de svære kundesager sammen med dem — ikke i stedet for dem."),
    ("Teknikerne i Hvidovre og Korsør",
     "Tavlemøde med sikkerhed først, kompetenceplan pr. medarbejder og fælles standarder — samme "
     "svar og samme kvalitet, uanset hvor opgaven ligger."),
    ("Kunderne og myndighederne",
     "Kvartalsgennemgang med KPI'er, aftalte arbejdsvinduer og skriftlig varsling i god tid — "
     "driften og trafikken skal ikke overraskes."),
    ("Divisionsdirektøren og de øvrige afdelinger",
     "Én rapport på få tal og aftalte eskaleringsgrænser, så beslutninger kommer op i tide og med "
     "et klart oplæg; fælles ressourcer prioriteret åbent."),
]

FIRST90 = [
    ("Dage 1–30",
     "Mødt projektlederne og nøgleteknikerne, været på plads i både Hvidovre og Korsør og "
     "gennemgået hver kontrakt: hvad er lovet, hvor er KPI-risikoen, og hvor mangler der en ejer "
     "af en beslutning."),
    ("Dage 30–60",
     "Kontraktkort og prioritetsnøgle indført; kapacitetsmodel lagt pr. måned; kadence med hver "
     "projektleder aftalt; første afdelingsrapport til divisionsdirektøren."),
    ("Dage 60–90",
     "Afvigelsesliste i brug med ejer og frist; én arbejdsgang standardiseret på tværs af Hvidovre "
     "og Korsør; kvartalsgennemgang pr. kunde påbegyndt."),
    ("Måned 3–6",
     "Økonomi, faktureringsgrad og KPI'er følges månedligt; kapaciteten ses før ordrebogen; "
     "projektlederne bruger selv værktøjerne."),
    ("Måned 6–12",
     "Afdelingen leverer stabilt på sikkerhed, kvalitet og indtjening, og forretningsområdet har et "
     "fagligt oplæg til kunderne, der rækker ud over det bestilte."),
]

KEYWORDS = (
    "Afdelingsleder · Kemp & Lauritzen · Trafikal Infrastruktur · Energi Infrastruktur · Hvidovre · "
    "Korsør · Projektledere · Teknikere · Ledelse af ledere · Personaleledelse · Trivsel · "
    "Motivation · Medarbejderengagement · Resultater gennem andre · Følgeskab · Synlig og "
    "nærværende · Økonomisk ansvar · Omsætning · Indtjening · Dækningsgrad · Kapacitetsstyring · "
    "Ressourceplanlægning · Prioritering · Kunderelationer · Forretningsmuligheder · "
    "Leveringssikkerhed · Kvalitet · Kontrakter · KPI'er · Kundeaftaler · Interessenter · "
    "Myndigheder · Banedanmark · Metroen · DSB · Sund & Bælt · Lokaltog · Letbanen · Tesla · BMO · "
    "Arbejdsvinduer · Sikkerhed · Ordentlighed · Projektbaseret forretning · Serviceforretning · "
    "Jernbane · Forsyningsområdet · Infrastruktur · El-teknisk · Højspænding · CTS · Maskinmester · "
    "Lean · SAP · Power BI · Python"
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
        m.para(t, after=24, line=218)

    for label, body in BULLETS:
        m.bullet(label, body, after=1, line=208)

    m.para(SYSTEM, after=20, line=212)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=0, line=204)

    m.meta("Med venlig hilsen · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "LEDELSESPROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("AFDELINGENS STYRING — ANVENDT I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER AFDELINGEN I RYTMEN",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN LEDES AFDELINGEN — DE FIRE PARTER")
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
    out = os.path.join(ROOT, "Shahram_Ajloo_KempLauritzen_AfdelingslederTrafikal.docx")
    build(out)
    print("OK " + out)
