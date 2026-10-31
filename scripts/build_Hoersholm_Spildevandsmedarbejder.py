# -*- coding: utf-8 -*-
"""
Hørsholm Kommune — spildevandsmedarbejder, Team Forsyning (Center for By og Miljø).
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Spildevandsmedarbejder | Myndighed, projekter og drift | Team Forsyning"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "31. oktober 2026"
RECIPIENT = ("Hørsholm Kommune · Center for By og Miljø · Team Forsyning · att. konstitueret teamleder "
             "Josephine Fie Legarth · 2347 6808 · jol393@horsholm.dk")
SUBJECT = "Ansøgning: spildevandsmedarbejder til Team Forsyning"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Opgaven er at holde styr på spildevandet i en kommune, hvor der bygges om på hele systemet: "
    "separatkloakering og klimatilpasning i hele kommunen, byudvikling hvor regn- og spildevand skal "
    "håndteres rigtigt fra første skitse, nye regler om terrænnært grundvand og et fælles "
    "vandressourcecenter med Novafos og fire andre kommuner. Det er både myndighedsarbejde, projekter og "
    "borgerservice — og det er opgaver, der har en borger i den anden ende.",

    "Nedenfor er min læsning af rollen og det system, der står klar fra første dag: en sagsportefølje "
    "med frister og status, tilladelser behandlet efter en fast skabelon med vilkår der kan håndhæves, "
    "en dokumentpakke pr. projekt der kan lægges frem for politikere og tilsyn, og en fast svartid på "
    "borgerhenvendelser.",
]

BULLETS = [
    ("Kravet: spildevandstilladelser til private, erhverv og forsyning",
     "Løsningen er en fast struktur pr. sag: oplysninger, vurdering, vilkår, klagevejledning og "
     "arkivering — så en tilladelse kan findes igen om fem år og holde, hvis den bliver påklaget. Jeg "
     "har arbejdet med dokumentation, hvor sporingen fra krav til vurdering var selve pointen."),

    ("Kravet: separatkloakerings- og klimatilpasningsprojekter",
     "Løsningen er projektstyring med plan, økonomi og afvigelser, og et teknisk blik for hvad der kan "
     "bygges og driftes: jeg har gennemført 37 anlægsprojekter i 2–10 mio. kr.-klassen med "
     "kravspecifikation, myndighedskrav og aflevering uden kritiske fund."),

    ("Kravet: miljøvurderinger og planarbejde på spildevandsområdet",
     "Løsningen er at kunne læse og skrive fagligt grundlag, ikke kun konklusioner: beskrivelse af "
     "miljøpåvirkning, alternativer og vilkår formuleret, så både politikere og rådgivere kan arbejde "
     "videre med det. Jeg har skrevet og kvalitetssikret teknisk dokumentation under skarpe "
     "myndighedskrav."),

    ("Kravet: terrænnært grundvand og implementering af nye regler",
     "Løsningen er at sætte sig ind i reglerne først og derefter omsætte dem til praksis: hvad skal "
     "borgeren gøre, hvad skal kommunen vurdere, og hvordan bliver det forklaret, så det ikke ender som "
     "en klage. Nye krav skal lande i en arbejdsgang — ikke i en mappe."),

    ("Kravet: politisk betjening, daglig drift og borgerservice",
     "Løsningen er et beslutningsgrundlag, der kan læses af ikke-fagfolk: faglig indstilling, økonomi, "
     "risici og alternativer — og svar til borgerne med en aftalt svartid, også når svaret er, at der "
     "går tid. Jeg har stået i den slags samtaler med både kunder og myndigheder i 20 år."),

    ("Kravet: relevant uddannelse som ingeniør eller lignende",
     "Løsningen er elautoriseret maskinmester med B.Tech (EQF 6) og el-ingeniøruddannelse — plus fem år "
     "på 24/7-spildevandsanlægget Lynetten, hvor spildevand, pumper, SCADA og myndighedskrav var "
     "hverdagen."),

    ("Kravet: struktur, selvstændighed og en bred opgaveportefølje",
     "Løsningen er et system, der holder styr på mange sager på én gang: én portefølge med "
     "frister og status, ugentlig gennemgang og en fast rytme for, hvad der bliver lukket — også de "
     "sager, der ikke råber højest."),
]

SYSTEM = ("Systemet er allerede bygget: sagsportefølje med frister og status, tilladelsesskabelon med "
          "vilkår og klagevejledning, projektmodel med plan, økonomi og afvigelser, dokumentpakke pr. "
          "sag og en fast svartid på borgerhenvendelser — i Excel, Power BI og kommunens "
          "sagsbehandlingssystemer, med Python og Claude til overblik og rapportering.")

MIRROR = ("Om kravene: 20 år i spildevand, drift og projekter — fem år som drifts- og "
          "vedligeholdelseschef på 24/7-spildevandsanlægget Lynetten med nul uplanlagte stop i fem år, "
          "37 anlægsprojekter (2–10 mio. kr.) med 25 specialister under myndighedskrav og dokumentation "
          "uden kritiske fund; elautoriseret maskinmester (LV/MV/HV), B.Tech og el-ingeniør.")

HONEST = ("Tre ting skal siges ligeud: jeg har ikke siddet med myndighedsbehandling af "
          "spildevandstilladelser før, jeg har ikke lavet miljøvurderinger efter VVM-reglerne, og jeg "
          "har ikke været ansat i en kommune. Det, jeg har, er forståelsen for anlæggene og for, hvad "
          "der skal stå i et dokument for at det holder — og lysten til at lære jeres sagsgange "
          "ordentligt, før jeg foreslår ændringer.")

CULTURE = ("Hvorfor Hørsholm: et nyetableret team, hvor der stadig er plads til at præge kulturen og den "
           "faglige retning, er en sjælden mulighed — og uformel tone og godt kollegialt samarbejde er "
           "ikke et plus, det er en forudsætning for at løse en opgaveportefølje, hvor alle skal kunne "
           "svare for hinandens sager. For mig betyder det, at man deler viden i stedet for at holde på "
           "den.")

PRACTICAL = ("Praktisk: bosat i Måløv — cirka 30 minutter til Hørsholm; kørekort B og bil; dansk på "
             "modersmålsniveau i skrift og tale; kan tiltræde hurtigst muligt, og egen virksomhed "
             "afvikles ved ansættelse.")

CLOSING = ("Jeg vil gerne høre, hvordan I i dag fordeler sagerne mellem de to grupper, og hvordan en "
           "spildevandstilladelse bliver behandlet hos jer — og hvordan I arbejder med de nye regler om "
           "terrænnært grundvand, så jeg ved, hvor jeg kan begynde at bidrage fra første uge.")

# ------------------------------------------------------------------ CV
PROFILE = ("Rollen kræver tre ting på én gang: drift og anlæg forstået indefra, sager der bliver "
           "behandlet og dokumenteret, så de holder, og en person der kan forklare det faglige for "
           "borgere, politikere og rådgivere. Det har været hverdag i 20 år: fem år som drifts- og "
           "vedligeholdelseschef på 24/7-spildevandsanlægget Lynetten med nul uplanlagte stop, 37 "
           "anlægsprojekter (2–10 mio. kr.) med 25 specialister under GMP/FDA/EMA-krav og nul kritiske "
           "fund samt egen virksomhed med kunder, myndighedsforhold og dokumentation. Elautoriseret "
           "maskinmester (B.Tech, EQF 6) og el-ingeniør.")

PRACTICE = [
    ("Sagsbehandling og dokumentation",
     "Fast struktur pr. sag: oplysninger, vurdering, vilkår, klagevejledning og arkivering; "
     "dokumentstyring med version og ejer, så en sag kan findes og forsvares år efter."),
    ("Spildevand og anlæg",
     "Driftserfaring fra 24/7-rensning: pumper og pumpestationer, HVAC, koblingsanlæg, højspænding og "
     "SCADA — og forståelse for, hvad et anlæg kan, når nogen beder om en ny løsning."),
    ("Projekter",
     "Faseopdelt projektmodel med plan, budget pr. leverance, afvigelsesliste med ejer og frist og "
     "aflevering med dokumentation, driften kan overtage."),
    ("Miljø og myndighed",
     "Myndighedskrav, tilsyn og revision som vilkår; miljøpåvirkning, vilkår og alternativer beskrevet "
     "fagligt og læsbart, så beslutningen kan træffes på et oplyst grundlag."),
    ("Politisk betjening",
     "Beslutningsoplæg med faglig indstilling, økonomi, risici og alternativer; møder med referat og "
     "en beslutningslog, så det er tydeligt, hvad der er aftalt og hvornår."),
    ("Borgere og parter",
     "Fagligt svar med aftalt svartid, også når svaret er, at der går tid; dialog med lodsejere, "
     "rådgivere og forsyning, hvor aftaler bliver skrevet ned."),
    ("Data og overblik",
     "Portefølge- og fristoverblik i Excel og Power BI, KPI'er for sager til tiden og rapportering "
     "bygget med Python og Claude; hurtig indlæring af nye systemer."),
]

MODELS = [
    ("Sager",
     "Portefølje med frister og status, tilladelsesskabelon med vilkår og klagevejledning, "
     "journalisering og dokumentstyring med version og ejer"),
    ("Projekter",
     "Faseopdelt model med plan, budget pr. leverance, afvigelsesliste med ejer og frist, "
     "afleveringspakke med dokumentation"),
    ("Myndighed",
     "Lovgrundlag og vilkår omsat til arbejdsgang, tilsyn og revision som fast rytme, "
     "sporbarhed fra krav til vurdering"),
    ("Politisk betjening",
     "Beslutningsoplæg med indstilling, økonomi, risici og alternativer; referat og beslutningslog"),
    ("Drift",
     "Forebyggende vedligeholdsplan, kritikalitet, PDCA-årshjul, KPI'er i SAP og beredskab på 24/7-anlæg"),
    ("Kvalitet",
     "Afvigelser med root cause, korrigerende handlinger og opfølgning på effekt; Lean, A3 og 5S"),
    ("Værktøjer",
     "Excel og Power BI, sagsbehandlings- og GIS-systemer, SAP/CMMS, Python og Claude til overblik"),
]

ACHIEVEMENTS = [
    ("Nul uplanlagte stop i fem år",
     "på 24/7-forsyningsanlægget Lynetten — planlagt vedligehold, PDCA og A3-root-cause frem for "
     "brandslukning."),
    ("Nul kritiske fund ved aflevering",
     "37 anlægsprojekter hos Novo Nordisk, 2–10 mio. kr., under GMP/FDA/EMA-krav — kravspecifikation, "
     "FAT/SAT, IQ/OQ/PQ og dokumentation."),
    ("25 specialister koordineret",
     "på tværs af mekanik, el, proces og indkøb i 37 samtidige projekter med plan, økonomi og "
     "rapportering."),
    ("40+ serviceanlæg og fuldt P&L",
     "kunder, myndighedsforhold, indkøb og dokumentation i egen autoriseret virksomhed — ansvar for "
     "både teknik og bundlinje."),
    ("+40 % produktivitet og −40 % energikost",
     "dokumenterede forbedringer via måling, standardarbejde, dataunderstøttet planlægning og egen "
     "AI-tooling."),
]

EXPERIENCE = [
    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 spildevandsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · budgetter i SAP",
     [("Drift og myndighed",
       "PDCA-baseret vedligeholdsplan, fejlhistorik og KPI'er i SAP; arbejde under myndighedskrav og "
       "tilsyn; nul uplanlagte stop i fem år."),
      ("Anlæg og ændringer",
       "fejlfinding og ændringer på pumper, HVAC og koblingsanlæg; dokumentation og "
       "arbejdstilladelser, så ændringen kunne findes igen bagefter.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister · GMP/FDA/EMA",
     [("Projekter, økonomi og rapportering",
       "plan og budget pr. projekt, fremdrift og rapportering til styregruppe; 25 specialister "
       "koordineret på tværs af mekanik, el, proces og indkøb."),
      ("Dokumentation",
       "kravspecifikation, FAT/SAT, IQ/OQ/PQ og valideringsdokumentation med afvigelseshåndtering — "
       "nul kritiske fund ved aflevering.")]),

    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og leverandøraftaler",
     [("Kunder og myndighedsforhold",
       "tilbud, aftaler og dokumentation over for erhvervskunder og myndighed i en autoriseret "
       "virksomhed; plan og prognose med fuldt ansvar for bundlinjen."),
      ("Teknisk ansvar",
       "dimensionering, fejlfinding og dokumentation på el- og HVAC-anlæg; løsningsvalg i dialog med "
       "kunden på stedet.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Projekter og fremdrift",
       "11 samtidige entrepriser med kapacitetsplanlægning, daglige tavlemøder og aflevering til "
       "bygherre.")]),

    ("Elektromekaniker / Produktionsteamleder",
     "ARJ Engineering · Teheran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · skiftplanlægning, materialestyring og lager",
     [("Teknisk problemløsning",
       "reparation og diagnosticering af elektriske og mekaniske systemer gennem struktureret root "
       "cause-analyse samt skiftplanlægning og materialestyring.")]),
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
     "Anvendt i drift og projekter · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og projekter · 2017 – nu"),
]

LANGUAGES = ("Dansk (modersmål, skrift og tale) · Engelsk (professionelt) · Persisk/farsi · "
             "Kørekort B (kategori B)")

PRACTICAL_CV = ("Bosat i Måløv — cirka 30 minutter til Hørsholm; kørekort kategori B og bil; dansk på "
                "modersmålsniveau i skrift og tale; kan tiltræde hurtigst muligt; egen virksomhed "
                "afvikles ved ansættelse.")

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Biofos (Lynetten), Novo Nordisk A/S "
              "(Kalundborg), Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Borgerne og lodsejerne",
     "Et svar de kan forstå, med en aftalt tidshorisont — også når svaret er, at der går tid, eller at "
     "de selv skal gøre noget. Det er dér, en kommune bliver vurderet."),
    ("Politikerne og centerledelsen",
     "Beslutningsoplæg med indstilling, økonomi, risici og alternativer, så beslutningen kan træffes på "
     "et oplyst grundlag — og gennemført bagefter, også når den går en anden vej end min anbefaling."),
    ("Novafos, rådgiverne og de andre kommuner",
     "Faste aftaler og dokumenterede tal, så samarbejdet om separatkloakering, klimatilpasning og "
     "vandressourcecenter hviler på fakta og ikke på antagelser."),
]

FIRST90 = [
    ("Uge 1–2",
     "Mødt teamet og de to grupper; gennemgået sagsporteføljen, de åbne tilladelser og de igangværende "
     "kloakerings- og klimaprojekter; læst op på kommunens spildevandsplan og de nye regler om "
     "terrænnært grundvand. Mødt Novafos-kontakten og de øvrige teams i centret."),
    ("Uge 3–6",
     "Overtaget en afgrænset del af sagsbehandlingen med sidemandsoplæring; tilladelsesskabelon og "
     "frister gennemgået; egen portefølgeoversigt med status lagt."),
    ("Uge 7–12",
     "Behandler tilladelser selvstændigt med faglig gennemgang; dokumentation og arkivering ensartet; "
     "borgerhenvendelser besvaret inden for aftalt svartid."),
    ("Måned 3–6",
     "Bidrager med fagligt grundlag til et politisk oplæg og til et kloakerings- eller klimaprojekt; "
     "arbejdsgangen for terrænnært grundvand er prøvet i praksis."),
    ("Måned 6–12",
     "Kan løfte hele sagsområder selvstændigt, og teamet kan svare for hinandens sager;"
     " dokumentationen holder ved et tilsyn, og borgerne møder et klart svar."),
]

KEYWORDS = (
    "Spildevandsmedarbejder · Spildevand · Separatkloakering · Klimatilpasning · Miljøvurderinger · "
    "Spildevandstilladelser · Terrænnært grundvand · Planlægning · Politisk betjening · Drift · "
    "Borgerservice · Myndighedsarbejde · Miljø · Team Forsyning · Center for By og Miljø · Novafos · "
    "Vandressourcecenter · Kommune · Forsyningsselskab · Rådgivningsvirksomhed · Ingeniør · Biolog · "
    "Geolog · Miljøtekniker · Miljøteknolog · Struktureret · Selvstændig · Løsningsorienteret · "
    "Opgaveportefølje · Serviceorienteret · Politikere · Borgere · Kommunikation · Sagsbehandling · "
    "Dokumentation · Journalisering · GIS · KPI · SAP · SCADA · Power BI · Dansk · Hørsholm · Måløv"
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
    m.resume_header(NAME, TITLE, CONTACT, "FAGLIG PROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("ARBEJDSMETODER — ANVENDT I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER SAGERNE I RYTMEN",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN ARBEJDES DER — DE TRE PARTER")
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
                  title="Ansøgning og CV — spildevandsmedarbejder, Hørsholm Kommune",
                  subject="Spildevand · myndighed · projekter · politisk betjening · borgerservice",
                  keywords=("spildevandsmedarbejder, spildevand, separatkloakering, klimatilpasning, "
                            "miljøvurderinger, tilladelser, hørsholm kommune, dansk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1 (krav → løsning), CV side 2-3, 90 dage side 4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_Hoersholm_Spildevandsmedarbejder.docx")
    print("OK", build(out))
