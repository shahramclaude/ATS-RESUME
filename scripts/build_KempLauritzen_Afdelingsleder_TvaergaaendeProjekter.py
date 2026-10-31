# -*- coding: utf-8 -*-
"""
Kemp & Lauritzen — Afdelingsleder til Tværgående Projekter (Hvidovre).
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Afdelingsleder | Tværgående Projekter · Energi & Infrastruktur | Kemp & Lauritzen"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv")

DATE = "31. oktober 2026"
RECIPIENT = ("Kemp & Lauritzen A/S · Energi Infrastruktur · Hvidovre · att. divisionsdirektør "
             "Stine Ruberg Christensen · tlf. 30 68 14 49")
SUBJECT = "Ansøgning: Afdelingsleder — Tværgående Projekter, Hvidovre"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Opgaven er at lede en afdeling, hvor fem projektledere og tredive teknikere skal levere fiber, "
    "E-mobility, højspænding og KLS-D/DAP-arbejde sikkert og med en sund forretning bag. Det er fire "
    "forretninger i én afdeling, og de styres ikke ens: højspænding og DAP tåler ingen slaphed i sikkerhed "
    "og kompetence, mens fiber og E-mobility lever på planlægning, udnyttelsesgrad og kundepleje.",

    "Nedenfor er min læsning af rollen og det system, der ligger klar: kapacitets- og ressourceplan på "
    "tværs af projekter, DAP-styring med kompetencematrix, projektøkonomi pr. sag, kundeporteføljeplan og "
    "fast ledelsesrytme for de fem projektledere.",
]

BULLETS = [
    ("Kravet: personaleledelse og udvikling af 5 projektledere og 30 teknikere",
     "Løsningen er ledelse gennem de fem projektledere: 1:1 hver fjerde uge, ugentlig afdelingsrytme, "
     "kompetencematrix pr. medarbejder og udviklingsplaner, der bliver fulgt op — ikke kun skrevet."),

    ("Kravet: høj medarbejdertrivsel, engagement og kompetenceudvikling",
     "Løsningen er at gøre trivsel målbar og handlingsorienteret: MUS/GRUS med opfølgning, trivselsmåling "
     "der bliver fulgt op i ledergruppen, lærlinge- og talentløft og en fast praksis for vidensdeling "
     "mellem de fem projektledere."),

    ("Kravet: ansvar for afdelingsøkonomi og projektøkonomi",
     "Løsningen er månedlig afdelingsgennemgang: omsætning pr. medarbejder og projekt, udnyttelsesgrad, "
     "dækningsgrad pr. sag, timer mod kalkule, udestående og prognose — med projektlederne som ejere af "
     "tallene."),

    ("Kravet: udvikling og videreudbygning af kundeporteføljen",
     "Løsningen er en kunde- og rammeaftaleplan med ansvar og næste skridt pr. kunde: hvilke "
     "infrastruktur- og energikunder der kan vokse — og hvordan kvalitet bliver argumentet for næste "
     "ordre."),

    ("Kravet: effektiv planlægning og ressourceallokering på tværs af projekter",
     "Løsningen er én kapacitetsplan for de 35 medarbejdere otte uger frem — kompetencer, certifikater, "
     "geografi og udstyr — så ressourcer flyttes, før flaskehalsen opstår."),

    ("Kravet: lovgivning, kvalitetskrav, sikkerhedsstandarder samt KLS-D og DAP-ansvar",
     "Løsningen er et styringssystem, der kan tåle et tilsyn: DAP- og autorisationsforhold dokumenteret "
     "med kompetencebeviser pr. medarbejder, procedurer for arbejde på og nær spændingsanlæg (LOTO, "
     "arbejdstilladelser), intern audit og afvigelser med ejer og frist — og en KLS-D, der bliver brugt "
     "dagligt, ikke en mappe."),

    ("Kravet: høj kvalitet i leverancer og tæt samarbejde med kunder, myndigheder og samarbejdspartnere",
     "Løsningen er aftalte kontrolpunkter pr. projekttype, aflevering med dokumentation og fast "
     "mødekadence med kunder og myndigheder om status, afvigelser og næste godkendelse."),


    ("Kravet: bidrage til afdelingens strategiske udvikling og vækst",
     "Løsningen er en strategi med tre ben — sikkerhed og compliance, kapacitet og kompetencer, kunder og "
     "dækningsgrad — omsat til kvartalsvise mål, der følges op som økonomien."),
]

SYSTEM = ("Systemet er allerede bygget: kapacitetsplan otte uger frem, kompetence- og autorisationsmatrix "
          "pr. medarbejder, DAP- og sikkerhedsprocedurer med kontrolpunkter, projektøkonomimodel med "
          "dækningsgrad pr. sag, kundeplan og fast ledelsesrytme — i Excel, Power BI og SharePoint med "
          "Python og Claude til rapportering.")

MIRROR = ("Om kravene: personaleledelse i 20 år — 5 projektledere og 30 teknikere er samme opgavetype som "
          "14- og 12-mands tekniske teams og 25 specialister på tværs af fag; el-teknisk baggrund i "
          "forsyning, energi og infrastruktur med elautorisation (LV/MV/HV) og koblings- og "
          "højspændingserfaring fra Lynetten; projekt- og driftsledelse med fuldt P&L-ansvar; "
          "kvalitetsstyring og myndighedskrav fra GMP- og forsyningsmiljøer.")

HONEST = ("To ting skal siges ligeud: DAP-godkendelse på 10-0,4 kV samt 30 og 50 kV har jeg ikke på "
          "papir i dag — elautorisationen (LV/MV/HV) og koblings- og højspændingserfaringen er på plads, "
          "og godkendelsen er et formelt forløb, jeg kan gennemgå. Og fiber og E-Mobility er nye områder "
          "for mig, mens højspænding, DAP og KLS-D er kendt terræn.")

CULTURE = ("Hvorfor Kemp & Lauritzen: ordentlighed er den eneste måde, 35 medarbejdere og fire "
           "forretningsben kan levere stabilt på — aftaler og kompetencebeviser i orden, spændingssætning "
           "aldrig som genvej, medarbejdere der udvikles frem for at blive brugt op. Fonden bag gør det "
           "lettere at tænke i år, ikke kvartaler.")

PRACTICAL = ("Praktisk: Måløv, kort til Hvidovre; kørekort B; dansk på modersmålsniveau; kan "
             "sikkerhedsgodkendes; klar til hurtigt start. Egen virksomhed afvikles ved ansættelse.")

CLOSING = ("Jeg vil gerne bruge første samtale på to spørgsmål: hvor kapacitetsflaskehalsene opstår "
           "mellem fiber, E-mobility og højspænding, og hvilke kunder der skal bære væksten.")

# ------------------------------------------------------------------ CV
PROFILE = ("Rollen kræver fire ting på én gang: at lede ledere og faglærte, at styre økonomi pr. sag, at "
           "holde sikkerhed og myndighedskrav i orden og at udvikle kundeporteføljen. Alle fire har været "
           "hverdag i 20 år: daglig ledelse af 5 elektrikere og 3 lærlinge med fuldt P&L, 14- og "
           "12-mands tekniske teams, 25 specialister koordineret på tværs af fag og 37 samtidige "
           "anlægsprojekter hos Novo Nordisk. Elautoriseret maskinmester (LV/MV/HV), B.Tech i Technology "
           "Management & Mechanical Engineering, dansk på modersmålsniveau.")

PRACTICE = [
    ("Personaleledelse og udvikling",
     "1:1-hjul, MUS/GRUS med opfølgning, kompetence- og autorisationsmatrix, udviklingsplaner, "
     "lærlinge- og talentløft, rekruttering og onboarding."),
    ("Afdelings- og projektøkonomi",
     "Omsætning pr. medarbejder og projekt, udnyttelsesgrad, dækningsgrad pr. sag, timer mod kalkule, "
     "udestående og prognose; budget, fakturering og månedlig økonomigennemgang."),
    ("Kapacitet og ressourceallokering",
     "Én samlet kapacitetsplan otte uger frem på tværs af projekter — kompetencer, certifikater, "
     "geografi og udstyr — med flytning af ressourcer, før flaskehalsen opstår."),
    ("Sikkerhed, KLS-D og DAP",
     "DAP- og autorisationsforhold dokumenteret, LOTO, arbejdstilladelser, spændingsløs tilstand, "
     "APV og risikovurdering, intern audit, afvigelseshåndtering med ejer og frist."),
    ("Kvalitet og leverance",
     "Kontrolpunkter pr. projekttype, afleveringsforretning med dokumentation, kvalitetsopfølgning og "
     "kundetilfredshed målt, ikke antaget."),
    ("Kunde og interessenter",
     "Rammeaftale- og kundeplan med ansvar og næste skridt, fast mødekadence med kunder og "
     "myndigheder, eskaleringstrappe og opfølgning på genkøb."),
    ("Projekt- og driftsledelse",
     "Plan, fremdrift, risiko og ændringshåndtering i tekniske organisationer; FAT/SAT, "
     "idriftsættelse og aflevering med nul kritiske fund."),
]

PARTNER = [
    ("De fem projektledere",
     "De ejer deres sager og deres tal. Min rolle er rammerne: hvad der skal være afklaret, før en sag "
     "starter, hvilke beslutninger de må tage selv, og hvornår de skal eskalere — aftalt på forhånd, "
     "ikke under en krise."),
    ("De tredive teknikere",
     "Kompetencematrix, certifikater og en fast praksis for sikkerhed; synlig ledelse på opgaverne og "
     "adgang til den nærmeste leder. Teknikere forlader ikke en afdeling, hvor de bliver udviklet."),
    ("Kunder og myndigheder",
     "Kvalitet i leverancen er salgsargumentet; myndighedskrav bliver håndteret som en plan med frister, "
     "så en godkendelse ikke bliver den ting, der forsinker et helt projekt."),
]

FIRST90 = [
    ("Uge 1–2",
     "Alle fem projektledere og de tredive teknikere mødt — på kontoret og ude på opgaverne; "
     "igangværende sager, DAP- og autorisationsforhold, KLS-D og de nuværende KPI'er gennemgået, før "
     "noget ændres."),
    ("Uge 3–6",
     "Kapacitetsplan otte uger frem lagt; kompetence- og autorisationsmatrix opdateret; 1:1-kalender og "
     "ugentlig afdelingsrytme aftalt med projektlederne."),
    ("Uge 7–12",
     "Dækningsgrad og timer mod kalkule gennemgået pr. sag med hver projektleder; sikkerheds- og "
     "KLS-D-gennemgang kørt; kundeplan med de ti vigtigste kunder lagt."),
    ("Måned 3–6",
     "DAP-forløb gennemført og dokumenteret; udnyttelsesgrad og dækningsgrad forbedret; "
     "kompetenceudviklingsplaner for alle 35 gennemført og fulgt op."),
    ("Måned 6–12",
     "Afdelingen leverer stabilt på økonomi, sikkerhed og kvalitet uden daglig styring; vækst i "
     "kundeporteføljen på rammeaftaler og infrastrukturprojekter; et team, der selv tager ansvar for "
     "planen. Løbende: månedlig økonomi- og sikkerhedsgennemgang og en fast post for, hvad der skal "
     "forenkles næste kvartal."),
]

MODELS = [
    ("Ledelse",
     "1:1-hjul, MUS/GRUS, situationsbestemt ledelse (SLII), GROW-coaching, delegeringstrappe, "
     "kompetencematrix, tavlemøder og visuel ledelse"),
    ("Økonomi",
     "Dækningsgrad pr. sag, timer mod kalkule, udnyttelsesgrad, prognose og budget, "
     "investeringsvurdering (NPV/IRR) og følsomhed; SAP og Power BI"),
    ("Kapacitet",
     "Ressourceplan otte uger frem, kompetence- og certifikatoversigt, kritisk vej og "
     "flaskehalsanalyse, prioritering mellem forretningsben"),
    ("Sikkerhed og DAP",
     "LOTO, arbejdstilladelser, spændingsløs tilstand, APV og risikovurdering, sikkerhedsrundering, "
     "nærved-hændelser, intern audit og afvigelseshåndtering"),
    ("Kvalitet og KLS-D",
     "Kontrolpunkter pr. projekttype, dokumenteret egenkontrol, aflevering med dokumentation, "
     "afvigelser med ejer og frist"),
    ("Kunde og vækst",
     "Rammeaftale- og kundeplan, mødekadence med kunder og myndigheder, genkøb og kundetilfredshed, "
     "prissætning og tilbud"),
    ("Forbedring",
     "PDCA, A3, 5S, standardarbejde, Kaizen og fem-hvorfor — små skridt, der bliver fastholdt"),
]

ACHIEVEMENTS = [
    ("5 elektrikere og 3 lærlinge ledet med fuldt P&L",
     "daglig drift, kompetenceudvikling og udviklingssamtaler i egen autoriseret virksomhed."),
    ("25 specialister faciliteret på tværs af fag",
     "mekanik, el, proces og indkøb — roller og ansvar afklaret tidligt og fulgt op i praksis."),
    ("37 samtidige anlægsprojekter, 2–10 mio. kr.",
     "plan, økonomi og aflevering hos Novo Nordisk — nul kritiske fund ved aflevering."),
    ("Nul uplanlagte stop i fem år",
     "på 24/7-forsyningsanlægget Lynetten — forebyggende vedligehold, PDCA og A3-root-cause."),
    ("+40 % produktivitet og −40 % energikost",
     "dokumenterede forbedringer via dataunderstøttet planlægning, standardarbejde og egen AI-tooling."),
]

EXPERIENCE = [
    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og leverandøraftaler",
     [("Personaleledelse og økonomi",
       "daglig ledelse af 5 elektrikere og 3 lærlinge, kompetencematrix og udviklingssamtaler; budget, "
       "prognose, indkøb og fuldt ansvar for bundlinjen."),
      ("Kunder og leverancer",
       "kundedialog, tilbud, aftaler og leverancer på el-, tavle- og styringsopgaver; opfølgning til "
       "opgaven er lukket og dokumenteret.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister inden for teknik, indkøb og drift · "
     "GMP/FDA/EMA",
     [("Projektledelse og økonomi",
       "tidsplan, økonomi, kontrakter, risiko og månedlig rapportering til ledelse og kunde; ændringer "
       "med konsekvensvurdering og beslutningslog."),
      ("Facilitering og aflevering",
       "25 specialister koordineret på tværs af mekanik, el, proces og indkøb; FAT/SAT, IQ/OQ/PQ og "
       "aflevering med nul kritiske fund.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · budgetter i SAP",
     [("Drift, højspænding og sikkerhed",
       "fejlfinding og reparation på koblingsanlæg og højspænding; LOTO, arbejdstilladelser og "
       "sikkerhedsprocedurer i et forsyningskritisk miljø."),
      ("Vedligehold og leverandører",
       "PDCA-baseret vedligeholdsplan med KPI'er i SAP og nul uplanlagte stop i fem år; koordinering af "
       "teknikere, entreprenører og leverandører.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Team og fremdrift",
       "14-personers team med kapacitetsplanlægning, flowstyring og daglige tavlemøder over 11 samtidige "
       "entrepriser; dokumentation ved montage i aktive bygninger.")]),

    ("Elektromekaniker / Produktionsteamleder",
     "ARJ Engineering · Teheran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · skiftplanlægning, materialestyring og lager",
     [("Produktionsteam og teknisk problemløsning",
       "skiftplanlægning, materialestyring og målopfølgning; reparation og diagnosticering af "
       "elektriske og mekaniske systemer gennem struktureret root cause-analyse.")]),
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
    ("Køleteknik & klimaanlæg (AMU)",
     "Mercantec · mar. 2021"),
    ("Arbejdsmiljø §16 og sikkerhedsbevidsthed (VI/6-1)",
     "Søfartsstyrelsen · maj 2021"),
    ("Lean — værdistrømsanalyse, standardarbejde, 5S, A3 og Kaizen",
     "Anvendt i drift · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og projekter · 2017 – nu"),
]

LANGUAGES = "Dansk (modersmål, skrift og tale) · Engelsk (professionelt) · Persisk/farsi · Kørekort B (kategori B)"

PRACTICAL_CV = ("Bosat i Måløv — kort til Hvidovre og det sjællandske projektområde; kørekort kategori B; "
                "dansk på modersmålsniveau og engelsk professionelt; kan sikkerhedsgodkendes; klar til "
                "hurtigt start, og egen virksomhed afvikles ved ansættelse.")

REFERENCES = "Tidligere ledere og samarbejdspartnere hos Novo Nordisk A/S (Kalundborg), Biofos (Lynetten) og egne kunder i ELOHVAC — oplyses ved henvendelse."

KEYWORDS = (
    "Afdelingsleder · Tværgående Projekter · Personaleledelse · Projektledere · Teknikere · "
    "Medarbejdertrivsel · Engagement · Kompetenceudvikling · Afdelingsøkonomi · Projektøkonomi · "
    "Kundeportefølje · Kunde- og interessenthåndtering · Kapacitetsplanlægning · Ressourceallokering · "
    "Lovgivning · Kvalitetskrav · Sikkerhedsstandarder · KLS-D · DAP · Driftsansvarlig Person · "
    "10-0,4 kV · 30 kV · 50 kV · Højspænding · Fiber · E-Mobility · El-teknisk · Forsyning · Energi · "
    "Infrastruktur · Projekt- og driftsledelse · Forretningsforståelse · Økonomistyring · "
    "Kvalitetsstyring · Myndighedskrav · Arbejdsmiljø · Elautoriseret · LV/MV/HV · SAP · Power BI · "
    "Lean · Kørekort B · Dansk · Måløv"
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

    m.section("KERNEKOMPETENCER & NØGLEORD")
    m.para(KEYWORDS, after=80)

    # afsluttende side: 90 dage + parter + praktik + referencer
    m.page_break()
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER AFDELINGEN I RYTMEN",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN LEDES AFDELINGEN — DE TRE PARTER")
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
                  title="Ansøgning og CV — Afdelingsleder, Tværgående Projekter, Kemp & Lauritzen",
                  subject="El-teknisk afdelingsledelse · højspænding, DAP, fiber og E-Mobility · "
                          "økonomi, sikkerhed og kundeportefølje",
                  keywords=("afdelingsleder, tværgående projekter, personaleledelse, dap, kls-d, "
                            "højspænding, fiber, e-mobility, projektøkonomi, kemp & lauritzen, dansk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1 (krav → løsning), CV side 2-3, 90 dage side 4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_KempLauritzen_Afdelingsleder_TvaergaaendeProjekter.docx")
    print("OK", build(out))
