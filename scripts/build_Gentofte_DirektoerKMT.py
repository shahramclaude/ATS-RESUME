# -*- coding: utf-8 -*-
"""
Gentofte Kommune — Direktør for Klima, Miljø og Teknik.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Direktør | Klima, miljø og teknik | Drift, anlæg og politisk betjening"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = ("Gentofte Kommune · Gentofte Rådhus · att. kommunaldirektør Torben Frølich")
SUBJECT = "Ansøgning: Direktør for Klima, Miljø og Teknik"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Klima, Miljø og Teknik er den del af kommunen, borgerne møder hver dag: vejen, fortovet, "
    "affaldet, varmen, byggesagen, kysten. Fire afdelinger, over 400 medarbejdere og to udvalg med "
    "otte mål for 2026-2029. Direktørens opgave er at holde driften kørende, mens de store sager — "
    "kystbeskyttelse, klimasikring og separatkloakering, varmeforsyningen, Sportsparken og "
    "sagsbehandlingstiden — løftes med økonomi og tid, der holder.",

    "Nedenfor er min motivation og ledelsesmæssige tilgang samt det system, der står klar fra første "
    "dag: porteføljeoversigt med næste beslutning og risiko, beslutningsoplæg på én side til de to "
    "udvalg, udvalgsårshjul og ledelseskadence med de fire chefer.",
]

BULLETS = [
    ("Kravet: lede et direktørområde med fire afdelinger og over 400 medarbejdere",
     "Løsningen er at lede på rammerne: fast kadence med de fire chefer, en skreven beslutningsret "
     "for hvad der løses i afdelingen og hvad der løftes i området, og en portefølje, der viser, hvor "
     "ledelsesopmærksomheden er bundet. Jeg har selv bygget en virksomhed op."),

    ("Kravet: betjene den politiske ledelse med troværdighed, lydhørhed og pondus",
     "Løsningen er at levere beslutningsgrundlag, ikke meninger: én side pr. sag med konsekvens, to "
     "alternativer og en anbefaling, scenarier hvor økonomi og tid er regnet med, og et udvalgsårshjul, "
     "så ingen sag kommer bag på nogen. Jeg har rapporteret til bestyrelser og haft budgetansvaret."),

    ("Kravet: skabe overblik i en meget stor og kompleks opgaveportefølje",
     "Løsningen er en portefølje på ét sted: alle anlægs-, klima- og vedligeholdelsesprojekter med "
     "fase, næste beslutning, økonomi og risiko — gennemgået månedligt med cheferne. Jeg har "
     "koordineret 37 anlægsprojekter uden kritiske fund."),

    ("Kravet: kortere sagsbehandlingstider og større borgertillid på byggesagsområdet",
     "Løsningen er at måle køen, ikke kun sagen: liggetider pr. trin, kapacitet mod tilgang, "
     "standardtekster og digital understøttelse — og offentliggjorte mål, så tilliden kan følges. Jeg "
     "har indført standardarbejde og Lean."),

    ("Kravet: kystbeskyttelse, klimasikring, separatkloakering og overløb — samtænkt med begrønning "
     "og byudvikling",
     "Løsningen er en prioriteret plan pr. opland med konsekvens og pris, koblet til byudviklingen og "
     "de medejede selskaber, så gaden kun graves op én gang. Fem år med kloak, pumpestationer og "
     "24/7-drift har lært mig, hvad overløb koster."),

    ("Kravet: udvikling af varmeforsyningen og det professionelle medejerskab af forsyningsselskaberne",
     "Løsningen er fast ejerskabsdialog med Novafos, Biofos, Gentofte Gladsaxe Fjernvarme og CTR om "
     "økonomi, risiko og beslutningsret — og en direktør, der selv har siddet på den anden side af "
     "bordet: jeg var fem år i Biofos I/S, et af de selskaber, Gentofte er medejer af."),

    ("Kravet: store byggerier, ejendomme og vedligeholdelse i tæt samspil med brugerne",
     "Løsningen er brugerkrav, der skrives ned før tegningen: hvad skolen, plejehjemmet eller "
     "institutionen skal kunne bagefter, et brugerpanel pr. projekt og en overlevering, hvor drift er "
     "med fra start. Jeg har ledet service på 40+ anlæg."),

    ("Kravet: trafik, veje, fortove og cykelstier — fremkommelighed og trafiksikkerhed",
     "Løsningen er tilstand og kritikalitet som grundlag: hvor er risikoen størst, hvad kan "
     "vedligeholdelse klare, og hvad kræver anlæg — planlagt sammen med grave- og klimaprojekter. Jeg "
     "har arbejdet med tilstandskontrol og KPI'er i SAP."),

    ("Kravet: beredskab, kriser og levering af basale ydelser under ulykker og katastrofer",
     "Løsningen er beredskabsplaner med scenarier, roller og øvelser i kalenderen og et tæt "
     "samarbejde med Beredskab Øst. Jeg er uddannet i arbejdsmiljø og sikkerhed (§16)."),

    ("Kravet: direktionsmedlem i en enhedsdirektion, der prioriterer på tværs",
     "Løsningen er at tage ansvar for helheden før søjlen: byde ind med KMT's viden om arealer, "
     "bygninger og forsyning i de andre områders sager og holde fast i fælles prioriteringer — og "
     "sige til, når noget ikke hænger."),
]

SYSTEM = (
    "Systemet står klar fra dag ét: porteføljeoversigt med næste beslutning og risiko, "
    "beslutningsoplæg på én side, udvalgsårshjul for de to udvalg, månedlig ledelsesrapport på få tal "
    "og en skreven beslutningsret mellem afdelingerne — ført i Excel og Power BI sammen med kommunens "
    "fagsystemer, med oplæg og analyser genereret i Python og Claude."
)

MIRROR = (
    "Om kravene: 20 år i tekniske anlæg og otte år med personaleansvar, heraf fem år som drifts- og "
    "vedligeholdelseschef i Biofos I/S — et fælleskommunalt selskab med bestyrelse, 24/7-drift, "
    "myndighedstilsyn og budget i SAP — og to år som teknisk direktør med fuldt P&L. Elautoriseret "
    "maskinmester (LV/MV/HV), B.Tech."
)

HONEST = (
    "Det skal siges ligeud: jeg har ikke været direktør i en kommunal forvaltning, ikke ledet chefer "
    "med eget personaleansvar, og min uddannelse er en professionsbachelor som maskinmester frem for "
    "en lang videregående uddannelse. Det, jeg har, er driftsforståelse fra gulvet, økonomi med fuldt "
    "ansvar og fem år i et fælleskommunalt selskab, hvor politisk valgte sad med omkring bordet."
)

CULTURE = (
    "KMT beskriver sig som en modig og ordentlig organisation, hvor den, der er tættest på opgaven, "
    "ved bedst. Det er den slags organisation, jeg er vant til at lede: fem år med havarier, der ikke "
    "spørger om lov, har lært mig, at ordentlighed er at sige tingene tidligt — og at mod og "
    "følgeskab opstår, når man lader medarbejderne løse det, de er bedst til."
)

PRACTICAL = (
    "Bosat i Måløv — cirka 20 minutter i bil til Gentofte Rådhus. Kørekort B og bil. Kan tiltræde "
    "1. januar 2027 og deltager gerne i testforløb og referencetagning."
)

CLOSING = (
    "I første samtale vil jeg gerne tale om, hvor de 400 medarbejderes ledelsesopmærksomhed reelt er "
    "bundet i dag — og hvilke tre sager der skal være løst om et år."
)

# ------------------------------------------------------------------ CV
PROFILE = (
    "Direktør- og driftschefprofil med 20 år i tekniske anlæg og otte år med personaleansvar: fem år "
    "som drifts- og vedligeholdelseschef i Biofos I/S — et fælleskommunalt selskab med bestyrelse, "
    "24/7-drift, myndighedstilsyn og budget i SAP — to år som teknisk direktør med fuldt P&L og to år "
    "som projektleder på 37 samtidige anlægsprojekter. Arbejder med porteføljestyring, økonomi og "
    "prioritering, beredskab og dataunderstøttet ledelse. Elautoriseret maskinmester (LV/MV/HV), "
    "B.Tech."
)

PRACTICE = [
    ("Ledelse og organisation",
     "Kadence med fire chefer, skreven beslutningsret mellem afdeling og område, ledelsesaftaler og "
     "kompetenceudvikling; bygget en virksomhed op fra bunden."),
    ("Politisk betjening og økonomi",
     "Beslutningsoplæg på én side med to alternativer og en anbefaling, udvalgsårshjul og scenarier "
     "med økonomi og tid — plus budgetansvar, prognose og opfølgning i SAP."),
    ("Anlæg, ejendomme og drift",
     "Portefølje med fase, næste beslutning og risiko; brugerkrav skrevet før tegningen, brugerpanel "
     "og overlevering med drift fra start — 37 anlægsprojekter uden kritiske fund."),
    ("Klima, kloak og vand",
     "Prioriteret plan pr. opland for klimasikring, separatkloakering og overløb, samtænkt med "
     "byudvikling og gravearbejder; fem år med kloak, pumpestationer og renseanlæg."),
    ("Forsyning og medejerskab",
     "Fast ejerskabsdialog om økonomi, risiko og beslutningsret; kendskab til selskaberne indefra — "
     "fem år i Biofos I/S — og kontraktstyring med KPI-opfølgning."),
    ("Beredskab, sikkerhed og data",
     "Beredskabsplaner med scenarier og øvelser, arbejdsmiljø §16, LOTO og nærved-hændelser; "
     "måling og dashboards samt AI-genererede oplæg, selvkodet i Python og Claude."),
]

MODELS = [
    ("Portefølje",
     "Alle anlægs-, klima- og vedligeholdelsesprojekter i ét overblik med fase, næste beslutning, "
     "økonomi og risiko; gennemgang hver måned med de fire chefer"),
    ("Beslutningsoplæg",
     "Én side: situation, konsekvens, to alternativer og en anbefaling; beslutningslog med ejer og "
     "frist — samme skabelon til direktion og udvalg"),
    ("Udvalgsårshjul",
     "Hvilke sager der kommer til Klima-, Miljø og Teknikudvalget og Byplanudvalget hvornår, og "
     "hvornår borgerne og brugerne inddrages"),
    ("Brugerinddragelse",
     "Brugerkrav skrevet ned før tegningen, brugerpanel pr. byggesag og overlevering hvor drift og "
     "brugere er med fra start"),
    ("Beredskab",
     "Scenarier (stormflod, skybrud, strømsvigt, cyber) med roller, mødekadence og øvelser i "
     "kalenderen; nærved-hændelser fulgt til lukning"),
    ("Opfølgning",
     "Månedlig rapport på få tal: sagsbehandlingstid, trafiksikkerhed, overløb, økonomi og trivsel; "
     "rapporter genereret i Python og Claude"),
]

ACHIEVEMENTS = [
    ("Nul uplanlagte stop i fem år",
     "24/7-renseanlæg i Biofos I/S med SCADA, højspænding og koblingsanlæg — planlagt vedligehold, "
     "tilstandskontrol og KPI'er i SAP, og en driftsorganisation der holdt, også under sygdom."),
    ("37 anlægsprojekter uden kritiske fund",
     "2-10 mio. kr. hos Novo Nordisk med 25 specialister koordineret på tværs af mekanik, el, proces "
     "og indkøb; FAT/SAT og dokumentation der bestod revision."),
    ("Fuldt P&L i egen virksomhed",
     "5 elektrikere og 3 lærlinge, 40+ serviceanlæg: rekruttering, økonomi, leverandøraftaler og "
     "ansvar for bundlinjen."),
    ("14-mands team med 11 samtidige opgaver",
     "kapacitetsplanlægning, daglige tavlemøder og tydelig prioritering i eksisterende byggeri med "
     "drift og brugere omkring os."),
]

EXPERIENCE = [
    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos I/S (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 spildevandsanlæg · pumper, HVAC, køl, koblingsanlæg og højspænding · budget i SAP",
     [("Drift, vedligehold og driftssikkerhed",
       "planlagt vedligehold, tilstandskontrol og KPI'er i SAP; nul uplanlagte stop i fem år på et "
       "anlæg, hvor spildevandet ikke kan vente — i et fælleskommunalt selskab med bestyrelse."),
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
     "14-mands produktions- og montageteam · 11 samtidige projekter (2-10 mio. kr.)",
     [("Personale, kapacitet og fremdrift",
       "14-personers team med kapacitetsplanlægning, daglige tavlemøder og opfølgning på den enkelte "
       "— og 11 samtidige entrepriser i eksisterende byggeri med brugere omkring os.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2-10 mio. kr. · 25 specialister · GMP/FDA/EMA",
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

PRACTICAL_CV = ("Bosat i Måløv — cirka 20 minutter i bil til Gentofte Rådhus; kørekort kategori B og "
                "bil. Dansk på modersmålsniveau og engelsk professionelt. Kan tiltræde 1. januar 2027.")

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Biofos I/S (Lynetten), Novo Nordisk A/S, "
              "Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Cheferne og medarbejderne i KMT",
     "Fast kadence med de fire chefer, skreven beslutningsret mellem afdeling og område og en "
     "direktør, der er synlig — og som tager de svære sager selv."),
    ("Den politiske ledelse og de to udvalg",
     "Udvalgsårshjul, beslutningsoplæg på én side med to alternativer og tal, der kan forklares — "
     "også når svaret er, at noget tager længere tid."),
    ("Direktionen og resten af kommunen",
     "KMT's viden om arealer, bygninger og forsyning bragt ind i de andre områders sager tidligt, "
     "frem for til sidst."),
    ("Forsyningsselskaber, borgere og Beredskab Øst",
     "Fast ejerskabsdialog om økonomi, risiko og beslutningsret; åben kommunikation under hændelser "
     "og borgerdialog, før graven er åben."),
]

FIRST90 = [
    ("Dage 1–30",
     "Mødt de fire chefer og været på alle afdelinger; gennemgået de otte udvalgsmål, "
     "anlægsporteføljen og beredskabsplanerne med Beredskab Øst."),
    ("Dage 30–60",
     "Én samlet portefølje med næste beslutning og risiko; udvalgsårshjul for begge udvalg lagt; "
     "måling af sagsbehandlingstid og trafiksikkerhed på plads."),
    ("Dage 60–90",
     "Prioriteret plan for kystbeskyttelse, klimasikring og separatkloakering pr. opland fremlagt; "
     "første trivselsmåling gennemført; beslutningsret mellem afdeling og område skrevet ned."),
    ("Måned 3–6",
     "Varmeforsyningen og ejerskabsdialogen med de fire selskaber i fast kadence; "
     "vedligeholdelsesplan for veje, fortove og cykelstier besluttet."),
    ("Måned 6–12",
     "KMT leverer på sagsbehandlingstid og fremkommelighed, de store sager har beslutninger med "
     "økonomi og tid, der holder — og medarbejderne oplever, at den åbne kultur er beholdt.",
    ),
]

KEYWORDS = (
    "Direktør for Klima, Miljø og Teknik · Klima, Miljø og Teknik · Gentofte Kommune · Gentofte · "
    "Klima og klimatilpasning · Byplanlægning · Store byggeriprojekter · Ejendomme · Trafik · "
    "Natur og miljø · Affald og forsyning · 400 medarbejdere · Ledere · Politisk ledelse · "
    "Direktionshold · Sammen om Gentofte · Sammen om ledelse · MED- og TRIO-samarbejde · "
    "Fællessekretariatet · Affald og Genbrug · Klima · Park og Vej · Gentofte Ejendomme · "
    "Bus- og Hjælpemiddeldepot · Plan og Byg · Natur og Miljø · Klima-, Miljø og Teknikudvalget · "
    "Byplanudvalget · Kystbeskyttelse · Stormflod · Grundvand · Trafiksikkerhed · Fremkommelighed · "
    "Beredskab · Kriser · Katastrofer · Klimasikring · Overløb · Begrønning · Byudvikling · "
    "Sagsbehandlingstid · Borgertilliden · New European Bauhaus · Gentofte Sportspark · Plejehjem · "
    "Anlægsprojekter · Vedligeholdelse · Novafos · Biofos · Gentofte Gladsaxe Fjernvarme · CTR · "
    "Beredskab Øst · Aktivt ejerskab · Forsyningsselskaber · Energiforsyning · Varmeforsyningen · "
    "Separatkloakering · Borgernes tillid · Troværdighed · Lydhørhed · Personlig pondus · Scenarier · "
    "Økonomi · Budgetansvar · Økonomistyring · Robust · Relationelle kompetencer · "
    "Kommunikative evner · Integritet · Ordentlighed · Mod og ordentlighed · Trivsel · Følgeskab · "
    "Maskinmester · Lean · SAP"
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

    m.models_table("DIREKTØROMRÅDETS STYRING — ANVENDT I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER OMRÅDET I STYRING",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN LEDES OMRÅDET — DE FIRE PARTER")
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
    build(os.path.join(ROOT, "Shahram_Ajloo_Gentofte_DirektoerKMT.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_Gentofte_DirektoerKMT.docx"))
