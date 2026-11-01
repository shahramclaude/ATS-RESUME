# -*- coding: utf-8 -*-
"""
Rudersdal Kommune — Chef til afdeling for Ejendomsservice.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Chef for Ejendomsservice | Drifts- og serviceorganisation | Rudersdal"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = ("Rudersdal Kommune · Ejendomme og Arealer, Rådhuset, 2840 Holte · "
             "att. områdechef Hans Dyrby Kloch")
SUBJECT = "Ansøgning: Chef for afdeling for ejendomsservice"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Fra 1. januar 2027 samles ejendomsdriften for alle kommunens ejendomme i én afdeling med knap "
    "100 medarbejdere, en nyoprettet teamlederstruktur og medarbejderne boende ude på ejendommene. "
    "Chefens opgave er todelt: at gøre den nye afdeling til en driftssikker serviceorganisation fra "
    "første dag, og at få brugerne på skoler, plejehjem, idrætshaller, daginstitutioner og "
    "kulturhuse til at mærke service frem for organisation.",

    "Nedenfor er min motivation og ledelsesmæssige tilgang samt det system, der står klar fra første "
    "dag: servicekatalog pr. brugergruppe, teamledermøde med skreven beslutningsret, "
    "kritikalitetsbaseret prioritering og opfølgning på arbejdsmiljø, trivsel og økonomi.",
]

BULLETS = [
    ("Kravet: etablere den nye afdeling, så den står robust og driftssikker fra 1. januar 2027",
     "Løsningen er en etableringsplan på 90 dage: ledelsesstruktur, mødekadence, servicekatalog i "
     "høring og et datagrundlag, der kan styres efter — så overgangen bliver en plan og ikke en "
     "overraskelse. Jeg har selv bygget en driftsorganisation op fra bunden."),

    ("Kravet: fortsat lokal tilstedeværelse og service tæt på brugerne",
     "Løsningen er at gøre det lokale styrbart: servicekatalog pr. brugergruppe med svartider, en "
     "tydelig grænse mellem afdelingens og brugernes ansvar og faste tilsyn på hver ejendom. Jeg "
     "har ledet service på 40+ anlæg med aftalte responstider."),

    ("Kravet: skabe høj kvalitet i understøttelsen af brugernes behov",
     "Løsningen er at måle det, brugerne oplever: reaktionstid, tid til udført arbejde og gentagne "
     "fejl — ugens tal i afdelingen, ikke en årsrapport. Fem år med 24/7-drift og nul uplanlagte "
     "stop har lært mig, at kvalitet er planlagt vedligeholdelse frem for heltemod."),

    ("Kravet: personaleansvar for 4-5 teamledere",
     "Løsningen er en fast kadence: en-til-en hver anden uge med to-tre punkter, der bliver fulgt "
     "op, et fælles ledermøde med beslutningslog og en chef, der er synlig ude på ejendommene. Jeg "
     "har selv stået i teamlederens rolle, med vagtplan, sygdom og en bruger der venter."),

    ("Kravet: passe på medarbejderne i det krydspres, de kan opleve",
     "Løsningen er at tage forventningsafstemningen hos brugerne i stedet for at sende presset "
     "nedad: en skreven prioriteringsnøgle og en eskalering, der går til mig — ikke til den enkelte "
     "håndværker. Jeg er uddannet i arbejdsmiljø (§16) og har haft ansvaret for sikkerhed og trivsel "
     "i både 24/7-drift og egen virksomhed."),

    ("Kravet: udvikle processer, arbejdsgange og samarbejde på tværs af organisationen",
     "Løsningen er én side pr. arbejdsgang med navngiven ejer, prøvekørt på en rigtig ejendom før "
     "den bliver standard — og aftalte snitflader til Rudersdal Ejendomme, Park og Vej og Strategi "
     "og Sammenhæng, så brugeren ikke skal kende vores organisation for at få hjælp."),

    ("Kravet: bidrage til energioptimering og kommunens klima- og bæredygtighedsindsatser",
     "Løsningen er energiledelse med forbrug pr. ejendom hver måned: de dyreste bygninger først og "
     "driftsoptimering før investering, inden for de indkøbs- og bæredygtighedspolitikker kommunen "
     "har vedtaget. Jeg har arbejdet med køl, varmegenvinding og varmepumper i drift."),

    ("Kravet: prioritere ressourcer og investeringer med afsæt i data og faglige vurderinger",
     "Løsningen er en kritikalitetsmodel — brugerpåvirkning, bygningens tilstand og sikkerhed — "
     "kombineret med en flerårig vedligeholdelses- og investeringsplan og en månedlig prognose. Så "
     "bliver prioriteringen et fælles beslutningsgrundlag i stedet for en diskussion om, hvem der "
     "råbte højest."),

    ("Kravet: professionel dialog med institutioner, ledere, politikere og eksterne parter",
     "Løsningen er at skrive til det niveau, der læser: én side pr. sag med konsekvens, to "
     "alternativer og en anbefaling — og leverandøraftaler fulgt op på KPI, ikke på mavefornemmelse. "
     "Jeg har rapporteret til styregrupper og bestyrelse og stået med budget og ressourceanvendelse "
     "bagefter."),
]

SYSTEM = (
    "Systemet står klar fra dag ét: servicekatalog pr. brugergruppe, teamledermøde med skrevet "
    "beslutningsret, kritikalitetsbaseret prioriteringsmodel, månedlig økonomi- og driftsrapport og "
    "trivselsmåling med opfølgning — ført i Excel og Power BI sammen med kommunens fagsystemer, og "
    "med rapporter og ledelsesoplæg genereret i Python og Claude."
)

MIRROR = (
    "Om kravene: 20 år i tekniske anlæg og otte år med personaleansvar — 14-mands team med 11 "
    "samtidige opgaver, 5 elektrikere og 3 lærlinge med fuldt P&L, 25 specialister koordineret på "
    "tværs af fag og fem år som drifts- og vedligeholdelseschef i et kommunalt ejet "
    "forsyningsselskab med bestyrelse, budgetter i SAP og 24/7-drift. Elautoriseret maskinmester "
    "(LV/MV/HV) og B.Tech i Technology Management."
)

HONEST = (
    "To ting skal siges ligeud: jeg har ikke ledet knap 100 medarbejdere gennem 4-5 teamledere før, "
    "og jeg har ikke arbejdet i en kommunal forvaltning med politiske udvalg — min ledelse har været "
    "tættere på opgaven og på fagene. Til gengæld har jeg fem år i en politisk ejet organisation, hvor "
    "valgte sad omkring bordet, og ved hvad et vedligeholdelsesefterslæb koster at indhente."
)

CULTURE = (
    "Rudersdal bygger organisationen på tillid og arbejder med lokal frihed og fællesskab på tværs — "
    "præcis den model, I har valgt for ejendomsservice. Den kræver en ledelse, der holder sammen på "
    "det, medarbejderne ikke selv kan se: fælles standarder, fælles tal og et fællesskab for "
    "teamlederne. »Vi lykkes kun i fællesskab« betyder for mig, at den enkelte skole kan mærke, at "
    "der står en afdeling bagved."
)

PRACTICAL = (
    "Bosat i Måløv — cirka 25 minutter i bil til Rådhuset i Holte. Kørekort B og bil, dansk på "
    "modersmålsniveau og engelsk professionelt. Kan tiltræde efter aftale, gerne før 1. januar 2027, "
    "så etableringen planlægges med mig på plads. Testforløbet mellem samtalerne er jeg indforstået "
    "med."
)

CLOSING = (
    "I første samtale vil jeg gerne tale om, hvordan afdelingen er i drift 1. januar uden at "
    "medarbejderne mærker mere forandring end nødvendig — og om hvordan vi måler det."
)

# ------------------------------------------------------------------ CV
PROFILE = (
    "Chef med 20 år i tekniske anlæg og otte år med personaleansvar — heraf fem år som drifts- og "
    "vedligeholdelseschef i et kommunalt ejet selskab med bestyrelse, budgetter i SAP og 24/7-drift, "
    "og to år med egen virksomhed og fuldt P&L. Har ledet service- og driftsorganisationer med "
    "brugere tæt på, bygget en organisation op fra bunden og indført standardarbejde og "
    "dataunderstøttet prioritering. Elautoriseret maskinmester (LV/MV/HV), B.Tech og Lean."
)

PRACTICE = [
    ("Etablering af den nye afdeling",
     "Etableringsplan på 90 dage med ledelsesstruktur, mødekadence, servicekatalog, datagrundlag og "
     "beslutningslog — gennemført som projekt med milepæle og ejer på hver beslutning."),
    ("Service til brugerne",
     "Servicekatalog pr. brugergruppe med svartider, ansvarsgrænse og faste tilsyn; opfølgning på "
     "reaktionstid og gentagne fejl. Fra drift: aftalte responstider på 40+ anlæg og nul uplanlagte "
     "stop i fem år."),
    ("Teamledere og medarbejdere",
     "En-til-en hver anden uge med ledelsesaftale, fælles ledermøde med beslutningslog, oplæring "
     "med to personer pr. kritisk kompetence og arbejdsmiljø som fast punkt."),
    ("Data, prioritering og investeringer",
     "Kritikalitetsmodel (brugerpåvirkning, bygningens tilstand, sikkerhed) med flerårig "
     "vedligeholdelses- og investeringsplan og månedlig prognose."),
    ("Økonomi og politisk niveau",
     "Budget og prognose med fuldt ansvar, én side pr. sag med to alternativer og en anbefaling, og "
     "leverandøraftaler fulgt op på KPI — rapportering til styregrupper og bestyrelse."),
    ("Energi og bæredygtighed",
     "Energiledelse pr. ejendom, driftsoptimering før investering, indkøb og bæredygtighedspolitik "
     "som ramme; køleteknik, varmegenvinding og varmepumper fra drift og AMU-uddannelse."),
]

MODELS = [
    ("Servicekatalog",
     "Én side pr. brugergruppe — skole, plejehjem, hal, daginstitution, kulturhus — med ydelser, "
     "svartider og hvad brugeren selv gør; revideret hvert forår med brugerne"),
    ("Teamledermøde",
     "Fast ugentligt møde med beslutningslog: hvad er besluttet, af hvem, hvornår, og hvad gør vi, "
     "hvis det ikke holder"),
    ("Trivsel og arbejdsmiljø",
     "Måling med opfølgning på faste temaer, sikkerhedsrunder og nærved-hændelser uden skyld — "
     "behandlet som driftsdata, ikke som holdning"),
    ("Prioritering",
     "Kritikalitetsmodel pr. sag og pr. bygning: brugerpåvirkning, tilstand og sikkerhed; "
     "investeringer følger samme model i den flerårige plan"),
    ("Økonomi",
     "Månedlig prognose, forbrug pr. ejendom og opfølgning på forbrugsafvigelser; rapporter "
     "genereret i Python og Claude"),
    ("Snitflader",
     "Aftalt leverance, form og tidspunkt til Rudersdal Ejendomme, Park og Vej og Strategi og "
     "Sammenhæng — prøvekørt, før den bliver standard"),
]

ACHIEVEMENTS = [
    ("Nul uplanlagte stop i fem år",
     "24/7-renseanlæg med SCADA, højspænding og koblingsanlæg — planlagt vedligehold, "
     "tilstandskontrol og KPI'er i SAP, og en driftsorganisation der holdt, også under sygdom."),
    ("5 elektrikere og 3 lærlinge med fuldt P&L",
     "egen virksomhed: rekruttering, oplæring, arbejdsmiljø, kunder, leverandøraftaler og ansvar "
     "for bundlinjen."),
    ("14-mands team med 11 samtidige opgaver",
     "kapacitetsplanlægning, daglige tavlemøder og tydelig prioritering i eksisterende byggeri med "
     "drift og brugere omkring os."),
    ("37 anlægsprojekter uden kritiske fund",
     "2–10 mio. kr. hos Novo Nordisk med 25 specialister koordineret på tværs af mekanik, el, "
     "proces og indkøb — dokumentation der bestod revision."),
]

EXPERIENCE = [
    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7-anlæg · pumper, HVAC, køl, koblingsanlæg og højspænding · budgetter i SAP",
     [("Drift, vedligehold og driftsikkerhed",
       "planlagt vedligehold, tilstandskontrol og KPI'er i SAP; nul uplanlagte stop i fem år på et "
       "anlæg, hvor brugerne ikke kan vente — og hvor politisk valgte sad med omkring bordet."),
      ("Sikkerhed, leverandører og beredskab",
       "koordinering af egne teknikere, entreprenører og rådgivere — LOTO, arbejdstilladelser, "
       "garantisager og nærved-hændelser fulgt til lukning.")]),

    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og leverandøraftaler",
     [("Organisation, rekruttering og arbejdsmiljø",
       "byggede virksomheden op fra bunden: rekruttering, oplæringsplaner og arbejdsplaner, "
       "sikkerhed og arbejdsmiljø som fast punkt."),
      ("Økonomi og kunder",
       "tilbudsberegning, indkøb og leverandøraftaler, plan og prognose med fuldt ansvar for "
       "bundlinjen.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Personale, kapacitet og service",
       "14-personers team med kapacitetsplanlægning, daglige tavlemøder og opfølgning på den enkelte "
       "— og 11 samtidige entrepriser i eksisterende byggeri med brugere omkring os.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister · GMP/FDA/EMA",
     [("Koordinering, snitflader og aflevering",
       "25 specialister koordineret på tværs af mekanik, el, proces og indkøb; fremdrift og "
       "rapportering til styregruppe; FAT/SAT, IQ/OQ/PQ og aflevering uden kritiske fund.")]),

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

PRACTICAL_CV = ("Bosat i Måløv — cirka 25 minutter til Rådhuset i Holte; kørekort kategori B og bil. "
                "Dansk på modersmålsniveau og engelsk professionelt. Kan tiltræde efter aftale.")

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Biofos (Lynetten), Novo Nordisk A/S, "
              "Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Teamlederne",
     "Fast en-til-en med ledelsesaftale, fælles ledermøde med beslutningslog og en chef, der tager "
     "de svære sager, så de ikke lander hos medarbejderne."),
    ("Brugerne ude på ejendommene",
     "Et servicekatalog de kan læse, faste tilsyn og en forventningsafstemning, der bliver taget "
     "oppefra — ikke sendt nedad til den, der står med opgaven."),
    ("Chefkollegerne i Ejendomme og Arealer",
     "Aftalte snitflader til Rudersdal Ejendomme, Park og Vej og Strategi og Sammenhæng, så én "
     "henvendelse fra en skole får ét svar."),
    ("Politikere og centralforvaltning",
     "Én side pr. sag med to alternativer og en anbefaling, og tal der kan forklares — også når "
     "svaret er, at noget tager længere tid end ønsket."),
]

FIRST90 = [
    ("Dage 1–30",
     "Mødt alle 4-5 teamledere og været på hver ejendomstype mindst én gang; gennemgået den nye "
     "teamlederstruktur, de indgåede aftaler og ejendomsstrategien med dens politiske beslutninger."),
    ("Dage 30–60",
     "Servicekatalog pr. brugergruppe i høring hos brugerne; ledelses- og mødekadence besluttet; "
     "datagrundlag på plads: sagstyper, svartider, nedbrud, energiforbrug og sygefravær."),
    ("Dage 60–90",
     "Kritikalitetsmodel og prioritering af ressourcer og investeringer fremlagt for områdechefen; "
     "første trivselsmåling gennemført; etableringsplanen for 1. januar godkendt og kommunikeret."),
    ("Måned 3–6",
     "Afdelingen leverer på svartider og arbejdsgange er prøvekørt med Rudersdal Ejendomme og Park "
     "og Vej; de første energitiltag valgt ud fra forbrug pr. bygning."),
    ("Måned 6–12",
     "Optimeringerne har tal — energi, svartider, gentagne fejl og sygefravær — og medarbejderne "
     "oplever, at den lokale frihed stadig er der, nu med fælles standarder bag sig."),
]

KEYWORDS = (
    "Chef for Ejendomsservice · Ejendomsdrift · Ejendomsservice · Drifts- og serviceorganisation · "
    "Ejendomme og Arealer · Rudersdal Kommune · Rådhuset i Holte · Bygningsmasse · Skoler · "
    "Plejehjem · Idrætshaller · Daginstitutioner · Kulturhuse · Dagtilbud · Idrætsfaciliteter · "
    "Kulturinstitutioner · Administrative bygninger · Svømmehalsdrift · Brugere · Brugernes behov · "
    "Lokal tilstedeværelse · Service · Effektiv service og drift · Servicegen · Faglig kvalitet · "
    "Kvalitet · Teamlederstruktur · 4-5 teamledere · Personaleansvar · Medarbejdere · Motivation · "
    "Sætte retning · Følgeskab · Nærværende leder · Tillid · Ansvar · Ansvar og ansvarlighed · "
    "Arbejdsmiljø · Trivsel · Krydspres · Lokale ledelser · Forventningsafstemning · "
    "Inddragende proces · Ejerskab · Ledelsesfællesskab · Chefkolleger · "
    "Tværgående ledelsessamarbejde · Tværgående · Processer · Arbejdsgange · "
    "Optimeringsmuligheder · Udvikling · Udviklingsorienteret · Selvstændighed · "
    "Ledelsesudvikling · Facility management · Ejendomsstrategi · Vedligeholdelse · "
    "Renoveringsopgaver · Nybyggeri · Køb og salg · Tekniske installationer · Serviceaftaler · "
    "Forsyning · Rengøring · Udearealer · Park og Vej · Rudersdal Ejendomme · Strategi og "
    "Sammenhæng · Energioptimering · Klima · Bæredygtighedsindsatser · Bæredygtige løsninger · "
    "Prioritere ressourcer · Investeringer · Data · Faglige vurderinger · Økonomistyring · "
    "Budgetter · Politiske beslutningsprocesser · Politisk styret organisation · Politikere · "
    "Institutioner · Interessenter · Eksterne samarbejdspartnere · Professionel dialog · Indkøb · "
    "Fagområder · 1. januar 2027 · Vi lykkes kun i fællesskab · Byggeri · Maskinmester · Lean · SAP"
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

    m.para(SYSTEM, after=50, line=226)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=10, line=222)

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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER AFDELINGEN I DRIFT",
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

    from docx.oxml.ns import qn as _qn
    from docx.oxml import OxmlElement as _OE
    for _tbl in m.doc.tables:
        for _tr in _tbl._tbl.tr_lst:
            _pr = _tr.get_or_add_trPr()
            _el = _OE("w:cantSplit")
            _pr.append(_el)

    m.save(path)


if __name__ == "__main__":
    build(os.path.join(ROOT, "Shahram_Ajloo_Rudersdal_ChefEjendomsservice.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_Rudersdal_ChefEjendomsservice.docx"))
