# -*- coding: utf-8 -*-
"""
Elos Medtech Pinol A/S — Process Development Manager, Gørløse.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Process Development Manager | Produktionsudstyr, automatisering og validering"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "31. oktober 2026"
RECIPIENT = ("Elos Medtech Pinol A/S · Engvej 33, 3330 Gørløse · att. Engineering Manager Peter Gad · "
             "24 61 07 27 · søgt via QuickApply på Jobindex")
SUBJECT = "Ansøgning: Process Development Manager"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Opgaven er at gøre teknologiske investeringer til produktion, der virker: en ny afdeling skal "
    "omsætte automationsstrategi og investeringslyst til udstyr og processer, der er robuste nok til at "
    "køre hver dag, skalerbare nok til at følge væksten og dokumenteret nok til at bestå en revision i "
    "en medicoteknisk virksomhed. Det er ikke et udviklingsprojekt ved siden af driften — det er "
    "forudsætningen for driften.",

    "Nedenfor er min læsning af rollen og det system, der står klar fra første dag: en prioriteret "
    "projektportefølje med fasegates og business case, en automationsroadmap med få satsningsområder, "
    "URS/FAT/SAT og IQ/OQ/PQ kørt som standard, en kompetence- og rolleplan for den nye afdeling og en "
    "fast kadence med produktion, kvalitet og supply chain.",
]

BULLETS = [
    ("Kravet: fagligt og personalemæssigt ansvar for en ny afdeling af projektledere, "
     "automationsspecialister og finmekanikere",
     "Løsningen er at bygge afdelingen op med teamet, ikke over det: rolleafklaring og "
     "beslutningsret først, 1:1 hver fjerde uge, kompetencematrix og udviklingsplaner — og en leder der "
     "er på fabrikken, for en ny afdeling bliver formet af de første hundrede beslutninger."),

    ("Kravet: ejerskab for automationsstrategien og prioritering af afdelingens roadmap",
     "Løsningen er en roadmap med få, navngivne satsningsområder, business case pr. initiativ og en "
     "prioritering efter effekt, risiko og hvor moden processen er. Roadmap bliver revideret hvert "
     "kvartal med produktionsledelsen — ellers bliver den en PowerPoint, der ikke flytter noget."),

    ("Kravet: sikre fremdrift på investerings- og udviklingsprojekter",
     "Løsningen er én porteføljetavle med fasegates: behov og business case, koncept, realisering, "
     "validering, idriftsættelse. Kapacitet afstemt mod efterspørgsel, begrænset antal igangværende "
     "projekter og et ugentligt fremdriftsmøde, hvor projekterne bliver reddet, før de glider."),

    ("Kravet: ansvar for implementering af nyt produktionsudstyr og nye produktionsprocesser",
     "Løsningen er leverandørstyring efter kravspecifikation: URS og acceptkriterier før indkøb, "
     "FAT/SAT før udstyret kommer ind på fabrikken, ramp-up med produktionsmedejerskab og en "
     "idriftsættelsesplan, hvor driften er trænet, før udstyret kører alene."),

    ("Kravet: sikre validering og dokumentation af produktionsudstyr",
     "Løsningen er IQ/OQ/PQ kørt efter fast skabelon med sporbarhed fra krav til test til afvigelse: "
     "jeg har leveret FAT/SAT, IQ/OQ/PQ og valideringsdokumentation på 37 anlægsprojekter under "
     "GMP/FDA/EMA-krav — uden kritiske fund ved aflevering."),

    ("Kravet: teknisk problemløsning, procesoptimering og løbende forbedringer i kvalitet, "
     "leveringssikkerhed og produktivitet",
     "Løsningen er at arbejde med data og årsag: OEE, scrap og gennemløbstid målt før og efter, A3 og "
     "root cause i stedet for hurtige løsninger, og standardarbejde der holder forbedringen på plads, "
     "efter projektet er lukket. Jeg har taget +40 % produktivitet og −40 % energikost hjem på den "
     "måde."),

    ("Kravet: samarbejde med produktion, kvalitet, supply chain og øvrige engineering-funktioner",
     "Løsningen er tydelige grænseflader og fast kadence: hvem ejer hvad i et udstyrsprojekt, hvornår "
     "kvalitet skal ind i designfasen i stedet for ved aflevering, og hvordan produktionens akutte "
     "behov bliver håndteret uden at roadmap stopper."),
]

SYSTEM = ("Systemet er allerede bygget: porteføljetavle med fasegates og business case, "
          "automationsroadmap med kvartalsvis revision, URS/FAT/SAT- og IQ/OQ/PQ-skabeloner med "
          "sporbarhed, kompetencematrix og udviklingsplaner, OEE- og scrap-KPI'er samt "
          "leverandørvurdering — i Excel, Power BI og projektværktøjer, med Python og Claude til "
          "analyse og dokumentation.")

MIRROR = ("Om kravene: 20 år i reguleret produktion, drift og projekter — 37 samtidige anlægsprojekter "
          "(2–10 mio. kr.) med 25 specialister under GMP/FDA/EMA-krav, daglig ledelse af 5 elektrikere og "
          "3 lærlinge med fuldt P&L, 14- og 12-mands teams i produktion og montage samt 24/7-drift med "
          "nul uplanlagte stop i fem år; elautoriseret maskinmester (LV/MV/HV) og B.Tech.")

HONEST = ("Tre ting skal siges ligeud: jeg har ikke været personaleleder for ingeniører før — jeg har "
          "ledet teknikere og lærlinge og koordineret 25 specialister som projektleder; jeg har ikke "
          "bygget specialmaskiner i den skala, I gør; og min medico-erfaring er Novo Nordisks "
          "GMP/FDA/EMA-verden, ikke ISO 13485. Det, jeg tager med, er valideringsdisciplinen, "
          "projektstyringen og den vane at få udstyr til at køre stabilt i produktion.")

CULTURE = ("Hvorfor Elos: I har lavet dentalimplantater siden 1975 sammen med professor Brånemark, og "
           "det siger noget om, hvad virksomheden er bygget på — præcision i mikrometer og tålmodighed "
           "med dokumentation. I en international medicoorganisation bliver engineering ikke målt på, hvor "
           "smart en løsning er, men på om den kan valideres, driftes og forsvares over for en "
           "myndighed. Det er den slags engineering, jeg har arbejdet i.")

PRACTICAL = ("Praktisk: bosat i Måløv — cirka 30 minutter til Engvej i Gørløse; kørekort B og bil; dansk "
             "på modersmålsniveau i skrift og tale; fysisk tilstedeværelse på fabrikken er en "
             "selvfølge; klar til hurtigt start, og egen virksomhed afvikles ved ansættelse.")

CLOSING = ("Jeg vil gerne se fabrikken og møde afdelingen, og bruge første samtale på to spørgsmål: "
           "hvordan I i dag prioriterer mellem roadmap og de akutte opgaver fra produktionen, og hvor "
           "I mener, automatisering giver den største effekt først.")

# ------------------------------------------------------------------ CV
PROFILE = ("Rollen kræver tre ting på én gang: en leder der kan bygge en ny afdeling af specialister, "
           "en projektleder der får investeringer omsat til udstyr der kører, og en fagperson der kan "
           "validere og dokumentere det hele i et reguleret miljø. Alle tre har været hverdag i 20 år: 37 "
           "anlægsprojekter (2–10 mio. kr.) med 25 specialister under GMP/FDA/EMA-krav og nul kritiske "
           "fund, daglig ledelse af 5 elektrikere og 3 lærlinge med fuldt P&L, 14- og 12-mands teams og "
           "24/7-drift med nul uplanlagte stop i fem år. Elautoriseret maskinmester (LV/MV/HV), B.Tech i "
           "Technology Management & Mechanical Engineering.")

PRACTICE = [
    ("Ledelse af tekniske teams og specialister",
     "1:1-hjul, MUS med opfølgning, kompetencematrix og udviklingsplaner, rolleafklaring og "
     "beslutningsret; situationsbestemt ledelse (SLII) og delegering med opfølgning."),
    ("Projekt- og porteføljestyring",
     "Fasegates med business case, kapacitetsplan seks uger frem, begrænset igangværende arbejde, "
     "risikolog med ejer og ugentlig fremdriftsopfølgning på økonomi, tid og leverancer."),
    ("Automatisering og digitalisering",
     "Behov og modenhed vurderet før investering; data fra SCADA og produktionslinjer omsat til "
     "KPI-tavler i Power BI; rapportering og analyse bygget med Python og Claude."),
    ("Validering og dokumentation",
     "URS, FAT/SAT, IQ/OQ/PQ og afvigelseshåndtering med sporbarhed fra krav til test; dokumentstyring "
     "med version og ejer og revision som vilkår, ikke som gæst."),
    ("Produktionsudstyr og procesoptimering",
     "Fejlfinding og optimering på mekaniske og elektriske systemer, A3 og root cause, OEE, scrap og "
     "gennemløbstid som styringstal."),
    ("Kvalitet og leveringssikkerhed",
     "Egenkontrol, afvigelser og korrigerende handlinger, standardarbejde og 5S der holder "
     "forbedringen fast, samt leverandøropfølgning på kvalitet og leveringstid."),
    ("Samarbejde på tværs",
     "Produktion, kvalitet, indkøb og supply chain i faste fora; én indgang til afdelingen, og "
     "kvalitet ind i designfasen i stedet for ved aflevering."),
]

MODELS = [
    ("Portefølje og gates",
     "Fasegate-model: behov/business case → koncept → realisering → validering → idriftsættelse, "
     "med kapacitetsplan og begrænset WIP"),
    ("Automatisering",
     "Automatiseringstrappe og modenhedsvurdering, business case pr. initiativ, "
     "automatiseringsroadmap revideret kvartalsvis med produktionsledelsen"),
    ("Udstyr og leverandører",
     "URS og acceptkriterier, FAT/SAT før idriftsættelse, leverandørvurdering, "
     "idriftsættelses- og træningsplan for driften"),
    ("Validering",
     "IQ/OQ/PQ, sporbarhed fra krav til test og afvigelse, dokumentstyring med version og ejer, "
     "revisionsparat dokumentation"),
    ("Forbedringer",
     "A3 og root cause, DMAIC, standardarbejde og 5S, OEE/scrap/gennemløbstid målt før og efter"),
    ("Ledelse",
     "1:1-hjul, MUS/GRUS, kompetencematrix, udviklingsplaner, SLII og coaching efter GROW"),
    ("Værktøjer",
     "Excel og Power BI, projektværktøjer og porteføljetavle, SAP/CMMS, Python og Claude til "
     "analyse og dokumentation"),
]

ACHIEVEMENTS = [
    ("Nul kritiske fund ved aflevering",
     "37 anlægsprojekter hos Novo Nordisk, 2–10 mio. kr., under GMP/FDA/EMA-krav — FAT/SAT, IQ/OQ/PQ "
     "og valideringsdokumentation med afvigelseshåndtering."),
    ("25 specialister koordineret",
     "på tværs af mekanik, el, proces og indkøb i 37 samtidige projekter med plan, økonomi og "
     "rapportering."),
    ("Nul uplanlagte stop i fem år",
     "på 24/7-forsyningsanlægget Lynetten — planlagt vedligehold, PDCA og A3-root-cause i stedet for "
     "brandslukning."),
    ("+40 % produktivitet og −40 % energikost",
     "dokumenterede forbedringer via måling, standardarbejde, dataunderstøttet planlægning og egen "
     "AI-tooling."),
    ("5 elektrikere og 3 lærlinge med fuldt P&L",
     "daglig ledelse, kompetenceudvikling og udviklingssamtaler i egen virksomhed — med ansvar for "
     "både mennesker og bundlinje."),
]

EXPERIENCE = [
    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister · GMP/FDA/EMA",
     [("Validering og dokumentation",
       "FAT/SAT, IQ/OQ/PQ og valideringsdokumentation med afvigelseshåndtering — nul kritiske fund; "
       "arbejde under myndighedskrav og revision."),
      ("Projekt og koordinering",
       "plan, økonomi og rapportering; 25 specialister koordineret på tværs af mekanik, el, proces og "
       "indkøb.")]),

    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og leverandøraftaler",
     [("Personale og rammer",
       "daglig ledelse af 5 elektrikere og 3 lærlinge, opgavefordeling, kompetencematrix og "
       "udviklingssamtaler."),
      ("Leverandører og økonomi",
       "tilbud, indkøb og leverandøraftaler, plan og prognose med fuldt ansvar for bundlinjen; "
       "tekniske løsninger valgt på levetid og drift, ikke på indkøbspris.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Team, fremdrift og proces",
       "14-personers team med kapacitetsplanlægning, flowstyring og daglige tavlemøder; "
       "standardarbejde og 5S indført med måling før og efter.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · budgetter i SAP",
     [("Drift, data og KPI",
       "PDCA-baseret vedligeholdsplan, fejlhistorik og KPI'er i SAP; nul uplanlagte stop i fem år."),
      ("Leverandører og sikkerhed",
       "koordinering af egne teknikere, entreprenører og leverandører — LOTO, arbejdstilladelser, "
       "garantisager og nærved-hændelser.")]),

    ("Elektromekaniker / Produktionsteamleder",
     "ARJ Engineering · Teheran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · skiftplanlægning, materialestyring og lager",
     [("Produktionsteam og teknisk problemløsning",
       "skiftplanlægning, materialestyring og målopfølgning; reparation og diagnosticering af "
       "elektriske og mekaniske systemer gennem struktureret root cause-analyse.")]),
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
    ("Køleteknik & klimaanlæg (AMU)",
     "Mercantec · mar. 2021"),
    ("Arbejdsmiljø §16 og sikkerhedsbevidsthed (VI/6-1)",
     "Søfartsstyrelsen · maj 2021"),
    ("Lean — værdistrømsanalyse, standardarbejde, 5S, A3 og Kaizen",
     "Anvendt i produktion og projekter · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i produktion og projekter · 2017 – nu"),
]

LANGUAGES = ("Dansk (modersmål, skrift og tale) · Engelsk (professionelt) · Persisk/farsi · "
             "Kørekort B (kategori B)")

PRACTICAL_CV = ("Bosat i Måløv — cirka 30 minutter til Elos Medtech Pinol på Engvej i Gørløse; kørekort "
                "kategori B og bil; dansk på modersmålsniveau i skrift og tale; fysisk tilstedeværelse på "
                "fabrikken er en selvfølge; klar til hurtigt start; egen virksomhed afvikles ved "
                "ansættelse.")

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Novo Nordisk A/S (Kalundborg), Biofos "
              "(Lynetten), Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Afdelingen",
     "Rolleafklaring, beslutningsret og udviklingsplaner fra start; faglig sparring på fast kadence og "
     "en leder der tager de svære samtaler tidligt — specialister skal udfordres, ikke detaljestyres."),
    ("Produktion og kvalitet",
     "Kvalitet ind i designfasen, ikke ved aflevering; produktionens akutte behov håndteret i en aftalt "
     "sluse, så roadmap og driftsstøtte ikke konkurrerer om de samme timer."),
    ("Leverandører og supply chain",
     "Kravspecifikation og acceptkriterier før indkøb, leverandørvurdering på kvalitet og leveringstid, "
     "og en idriftsættelse hvor reservedele og dokumentation er på plads."),
]

FIRST90 = [
    ("Uge 1–2",
     "Mødt afdelingen og den enkelte medarbejder, gennemgået igangværende projekter, udstyrsportefølje "
     "og de åbne afvigelser; gået fabrikken igennem med produktion og kvalitet. Mødt Peter Gad og "
     "produktionsledelsen."),
    ("Uge 3–6",
     "Porteføljetavle med fasegates og status lagt; roadmap og satsningsområder gennemgået med "
     "produktionsledelsen; rolleafklaring i afdelingen aftalt; 1:1-kalender og ugentligt "
     "fremdriftsmøde i gang."),
    ("Uge 7–12",
     "Business case og acceptkriterier som standard i nye projekter; valideringsskabeloner og "
     "sporbarhed gennemgået med kvalitet; KPI-baseline for OEE, scrap og gennemløbstid lagt."),
    ("Måned 3–6",
     "Mindst ét udstyrsprojekt ført til idriftsættelse med dokumentation i orden; prioriteringen mellem "
     "roadmap og driftsstøtte aftalt med produktionen; kompetenceplan for afdelingen på plads."),
    ("Måned 6–12",
     "Roadmap leverer målbar effekt på mindst to satsningsområder; afdelingen er kendt som den, "
     "produktionen ringer til, når noget skal løses — og som den, der kommer med løsningen før "
     "problemet gentager sig."),
]

KEYWORDS = (
    "Process Development Manager · Produktionsprocesser · Produktionsudstyr · Projektledere · "
    "Automationsspecialister · Finmekanikere · Medicotekniske produkter · Dentalindustrien · Fagligt "
    "ansvar · Personalemæssigt ansvar · Investering · Specialmaskiner · Automatisering · Digitalisering · "
    "Procesforbedringer · Teknisk support · Skalerbare produktionsløsninger · Konkurrencedygtige "
    "produktionsløsninger · Automationsstrategi · "
    "Produktionsledelsen · Projektportefølje · Automation roadmap · Fremdrift · Investeringsprojekter · "
    "Udviklingsprojekter · Implementering · Teknisk problemløsning · Procesoptimering · Validering · "
    "Dokumentation · IQ/OQ/PQ · FAT/SAT · URS · Løbende forbedringer · Kvalitet · Leveringssikkerhed · "
    "Produktivitet · OEE · Supply chain · Engineering · Reguleret produktion · Medicoindustrien · "
    "Ingeniør · ISO 13485 · GMP · FDA · SAP · Power BI · Dansk · Gørløse · Måløv"
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

    m.models_table("UDVIKLINGS- OG VALIDERINGSMETODER — ANVENDT I PRAKSIS",
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
                  title="Ansøgning og CV — Process Development Manager, Elos Medtech Pinol",
                  subject="Produktionsudstyr · automatisering · validering · reguleret produktion",
                  keywords=("process development manager, produktionsudstyr, automatisering, "
                            "validering, iso 13485, gmp, projektportefølje, elos medtech, dansk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1 (krav → løsning), CV side 2-3, 90 dage side 4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_ElosMedtech_ProcessDevelopmentManager.docx")
    print("OK", build(out))
