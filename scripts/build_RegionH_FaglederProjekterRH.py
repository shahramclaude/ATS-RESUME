# -*- coding: utf-8 -*-
"""
Region Hovedstaden — Fagleder for projekter, Drift og Byg, Rigshospitalet (Center for Ejendomme).
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Fagleder for projekter | Drift og Byg | Rigshospitalet"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = ("Region Hovedstaden · Center for Ejendomme, Drift og Byg, Rigshospitalet · "
             "via Dansk HR Service, Christopher Sunddahl")
SUBJECT = "Ansøgning: Fagleder for projekter til Drift og Byg på Rigshospitalet"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Drift og Byg på Rigshospitalet gennemfører bygge- og renoveringsprojekter, mens hospitalet "
    "er i drift — og den betingelse styrer alt andet: en plan, der ikke tager højde for, at der "
    "ligger patienter på den anden side af væggen, er ikke en plan. Faglederens opgave er ikke at "
    "være den skarpeste projektleder i teamet, men at skabe rammerne, så projektlederne kan lykkes: "
    "tydelige forventninger, en portefølje der kan overskues, og en chef der ved, hvor der skal "
    "besluttes.",

    "Nedenfor er min motivation og ledelsesmæssige tilgang samt systemet, der står klar fra første "
    "dag: porteføljeoversigt på én side pr. projekt, prioriteringsnøgle, faglig kadence, "
    "snitflademodel mod driften og fast ledelsesrapport til ejendomschefen.",
]

BULLETS = [
    ("Kravet: lede og udvikle projektteamet gennem faglig sparring, tydelige forventninger og "
     "løbende opfølgning",
     "Løsningen er at lede mennesker gennem rammer og forventninger: fast kadence med hver "
     "projektleder og en skreven forventningsaftale om ansvar, beslutningsret og hvornår der "
     "eskaleres. Projektgennemgangen er til for at sparre og udfordre, ikke for at kontrollere: "
     "hvad er næste beslutning, hvad er risikoen, og hvad har du brug for af mig."),

    ("Kravet: sikre kvalitet og fremdrift i projektporteføljen med blik for økonomi, tidsplaner "
     "og risici",
     "Løsningen er én side pr. projekt: næste beslutning, økonomi mod budget, den tidskritiske "
     "vej, største risiko og navngiven ejer — gennemgået på et fast porteføljemøde hver måned. Jeg "
     "har stået med 37 samtidige anlægsprojekter og truffet de prioriteringer, der holder en "
     "portefølje i gang."),

    ("Kravet: skabe gode rammer for prioritering og ressourcefordeling på tværs af projekterne",
     "Løsningen er en prioriteringsnøgle, der er skrevet ned og kendt: patientsikkerhed og "
     "driftsstabilitet først, derefter myndighedskrav, tidskritiske projekter og øvrige — koblet "
     "til en kapacitetsmodel pr. måned, som jeg fører sammen med fagkoordinatoren, og en "
     "beslutningslog med ejer og frist."),

    ("Kravet: styrke samarbejdet mellem projektområdet, den tekniske drift, supportfunktionerne "
     "og hospitalets øvrige interessenter",
     "Løsningen er en snitflademodel pr. projekt: grænsefladeejer i driften, afbrudsplan, "
     "varsling til den kliniske afdeling i god tid og skriftligt, så den daglige drift ikke bliver "
     "overrasket. Jeg har drevet teknik videre, mens der blev bygget omkring mig."),

    ("Kravet: bidrage til fælles metoder, arbejdsgange og kvalitet i den måde, projekterne "
     "gennemføres på",
     "Løsningen er én arbejdsgang pr. proces — projektstart, ændring, aflevering og dokumentation "
     "— prøvekørt på ét projekt og målt, før den bliver standard. Standardarbejde, 5S og A3 er min "
     "daglige værktøjskasse, ikke et udviklingsprojekt."),

    ("Kravet: være sparringspartner for ejendomschefen og viceejendomschefen med et klart billede "
     "af, hvordan projekterne udvikler sig",
     "Løsningen er en fast ledelsesrapport på få tal — fremdrift, økonomi, risiko og næste "
     "beslutning — med eskaleringsgrænser aftalt på forhånd, så en sag kommer op i tide og får "
     "den opmærksomhed, den kræver."),

    ("Kravet: solid erfaring fra byggeprojekter og projektledelse — komplekse projekter sikkert "
     "fra beslutning til aflevering",
     "Løsningen er 37 anlægsprojekter i eksisterende byggeri med FAT/SAT, IQ/OQ/PQ og aflevering "
     "uden kritiske fund, plus fem år i 24/7-drift, hvor nedbrud havde en pris. Jeg kender både "
     "bygherrens og driftsherrens side af bordet."),

    ("Kravet: offentlig bygherrefunktion, udbud, kontrakter og projektopfølgning",
     "Løsningen er udbud, kontrakter og leverandøropfølgning fra egen virksomhed med fuldt P&L, "
     "og kontraktstyring på store anlægsprojekter — inklusive garantisager. Den offentlige "
     "bygherrerolle skal læres i jeres rammer; metoden er den samme."),

    ("Kravet: teknisk forståelse for bygninger og installationer i en hospitalsvirkelighed",
     "Løsningen er elautoriseret maskinmester (LV/MV/HV) og B.Tech med 20 år i tekniske anlæg: el "
     "og højspænding, ventilation, køl, pumper, CTS/BMS og styringer. Jeg kan udfordre fagligt og "
     "læse en teknisk løsning — og ved, hvornår jeg skal lade specialisterne svare."),
]

SYSTEM = (
    "Systemet står klar fra første dag: porteføljeoversigt på én side pr. projekt, prioriteringsnøgle "
    "for hvad der går foran, faglig kadence med hver projektleder, snitflademodel mod driften og "
    "hospitalets afdelinger, beslutningslog med ejer og frist samt en månedlig ledelsesrapport på "
    "fremdrift, økonomi og risiko — ført i Excel og Power BI sammen med Center for Ejendommes "
    "systemer, med oplæg genereret i Python og Claude."
)

MIRROR = (
    "Om kravene: elautoriseret maskinmester (LV/MV/HV) og B.Tech, 20 år i tekniske anlæg og otte "
    "år med personaleansvar — 37 anlægsprojekter med 25 specialister, 14-mands team, 5 "
    "elektrikere og 3 lærlinge med fuldt P&L og fem år som driftschef i Biofos med budget i SAP."
)

HONEST = (
    "Det skal siges ligeud: jeg har ikke ledet projektledere i en hospitalsorganisation og ikke "
    "arbejdet i en offentlig bygherrefunktion med regionspolitisk styring. Min ledelse af ledere er "
    "hidtil sket i mindre enheder, og mine projekter har været i drift og GMP-regulerede miljøer. "
    "Til gengæld har jeg fem år i et kommunalt ejet selskab med bestyrelse og "
    "myndighedstilsyn — og prøvet at holde teknik i drift, mens der blev bygget."
)

CULTURE = (
    "Center for Ejendomme hedder fra 1. januar 2027 Ejendomme og Byggerier, når Region Hovedstaden "
    "og Region Sjælland lægges sammen — og Rigshospitalet er den matrikel, hvor mindst må gå galt. "
    "Derfor er prioriteringsnøglen ikke et dokument, men daglig praksis. Jeg kommer ikke for at "
    "lave om på organisationen, men for at gøre porteføljen styrbar — også i et år med ny struktur."
)

PRACTICAL = (
    "Bosat i Måløv — cirka 25 minutter i bil til Rigshospitalet og cirka 20 minutter til Glostrup. "
    "Arbejdsdage på begge matrikler passer fint. Kørekort B og bil, dansk på modersmålsniveau og "
    "engelsk professionelt. Kan tiltræde hurtigst muligt eller efter aftale."
)

CLOSING = (
    "I første samtale vil jeg gerne tale om, hvilke tre beslutninger i porteføljen der haster mest "
    "lige nu — og hvordan I i dag får dem løftet til ejendomschefen."
)

# ------------------------------------------------------------------ CV
PROFILE = (
    "Teknisk leder med 20 år i anlæg, projekter og drift og otte år med personaleansvar: to år som "
    "projektleder på 37 samtidige anlægsprojekter i eksisterende byggeri, fem år som driftschef i "
    "Biofos med budget i SAP og 24/7-drift, to år som teknisk direktør med fuldt P&L og to år som "
    "projekt- og værkstedsleder for et 14-mands team. Arbejder med porteføljeoversigter, "
    "prioriteringsnøgler og beslutningslog — og koder selv de oplæg, ledelsen læser."
)

PRACTICE = [
    ("Ledelse af projektledere",
     "Fast kadence og skreven forventningsaftale pr. medarbejdere i teamet; sparring på næste "
     "beslutning, risiko og behov frem for kontrol af detaljer."),
    ("Porteføljestyring",
     "Én side pr. projekt med næste beslutning, økonomi mod budget, tidskritisk vej, risiko og "
     "ejer; månedligt porteføljemøde med beslutningslog."),
    ("Prioritering og kapacitet",
     "Nedskrevet prioriteringsnøgle (patientsikkerhed og driftsstabilitet → myndighedskrav → "
     "tidskritiske projekter) og kapacitetsmodel pr. måned med fagkoordinator."),
    ("Snitflader i drift",
     "Grænsefladeejer, afbrudsplan og skriftlig varsling til den kliniske afdeling i god tid; fast "
     "vej for hvem der beslutter hvad."),
    ("Metoder og arbejdsgange",
     "Én arbejdsgang pr. proces (projektstart, ændring, aflevering, dokumentation), prøvekørt på "
     "ét projekt og målt før den bliver standard."),
    ("Rapportering til ledelsen",
     "Månedlig ledelsesrapport på fremdrift, økonomi, risiko og næste beslutning med aftalte "
     "eskaleringsgrænser; oplæg på én side genereret i Python og Claude."),
]

MODELS = [
    ("Porteføljeoversigt",
     "Én side pr. projekt: næste beslutning, økonomi mod budget, tidskritisk vej, største risiko "
     "og navngiven ejer"),
    ("Prioriteringsnøgle",
     "Patientsikkerhed og driftsstabilitet → myndighedskrav → tidskritiske projekter → øvrige; "
     "skrevet ned og kendt af alle"),
    ("Faglig kadence",
     "En-til-en med hver projektleder + fagligt teammøde med beslutningslog — sparring på næste "
     "beslutning, ikke statusophobning"),
    ("Snitflademodel",
     "Pr. projekt: grænsefladeejer i driften, afbrudsplan og skriftlig varsling til klinikken"),
    ("Metodebog",
     "Én arbejdsgang pr. proces (projektstart, ændring, aflevering, dokumentation) med prøvekørsel "
     "og måling før udrulning"),
    ("Ledelsesrapport",
     "Månedligt på få tal: fremdrift, økonomi, risiko og næste beslutning — med aftalte "
     "eskaleringsgrænser"),
]

ACHIEVEMENTS = [
    ("37 anlægsprojekter uden kritiske fund",
     "2-10 mio. kr. hos Novo Nordisk i eksisterende byggeri: 25 specialister koordineret på tværs "
     "af mekanik, el, proces og indkøb, fremdrift og rapportering til styregruppe, FAT/SAT, "
     "IQ/OQ/PQ og aflevering uden kritiske fund."),
    ("Nul uplanlagte stop i fem år",
     "24/7-anlæg med SCADA, højspænding og koblingsanlæg — planlagt vedligehold, tilstandskontrol "
     "og KPI'er i SAP, også i perioder hvor der blev bygget omkring driften."),
    ("14-mands team med 11 samtidige opgaver",
     "kapacitetsplanlægning, daglige tavlemøder og tydelig prioritering i eksisterende byggeri "
     "med brugere omkring os."),
    ("5 elektrikere og 3 lærlinge med fuldt P&L",
     "egen virksomhed: udbud, tilbudsberegning, kontrakter, garantisager og ansvar for "
     "bundlinjen."),
]

EXPERIENCE = [
    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2-10 mio. kr. · 25 specialister · GMP/FDA/EMA",
     [("Koordinering, snitflader og aflevering",
       "25 specialister koordineret på tværs af mekanik, el, proces og indkøb; fremdrift og "
       "rapportering til styregruppe; FAT/SAT, IQ/OQ/PQ og aflevering uden kritiske fund."),
      ("Ændringer, dokumentation og driftsoverlevering",
       "ændringshåndtering og teknisk dokumentation, der bestod revision — og overlevering til "
       "drift med skrevne grænseflader.")]),

    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og leverandøraftaler",
     [("Udbud, kontrakter og økonomi",
       "tilbudsberegning, udbud, leverandøraftaler, plan og prognose med fuldt ansvar for "
       "bundlinjen."),
      ("Organisation, rekruttering og arbejdsmiljø",
       "byggede virksomheden op fra bunden: rekruttering, oplæringsplaner og arbejdsplaner, "
       "sikkerhed og arbejdsmiljø som fast punkt.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7-anlæg · pumper, HVAC, køl, koblingsanlæg og højspænding · budget i SAP",
     [("Drift, vedligehold og driftssikkerhed",
       "planlagt vedligehold, tilstandskontrol og KPI'er i SAP; nul uplanlagte stop i fem år på et "
       "anlæg, hvor driften ikke kunne vente."),
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

PRACTICAL_CV = ("Bosat i Måløv — cirka 25 minutter i bil til Rigshospitalet og cirka 20 minutter "
                "til Glostrup; arbejdsdage på begge matrikler passer fint. Kørekort kategori B og "
                "bil, dansk på modersmålsniveau og engelsk professionelt. Kan tiltræde hurtigst "
                "muligt eller efter aftale.")

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Novo Nordisk A/S, Biofos (Lynetten), "
              "Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Projektlederne",
     "Tydelig forventningsaftale, fast sparring og en leder, der tager de svære interessentmøder "
     "sammen med dem — ikke i stedet for dem."),
    ("Ejendomschefen og viceejendomschefen",
     "Én rapport på få tal og aftalte eskaleringsgrænser, så beslutninger kommer op i tide og "
     "med et klart oplæg."),
    ("Den tekniske drift og supportfunktionerne",
     "Snitflademodel pr. projekt med grænsefladeejer, afbrudsplan og fælles prioritering — "
     "driften skal ikke overraskes."),
    ("Hospitalets kliniske afdelinger, rådgivere og entreprenører",
     "Varsling i god tid og skriftligt, aftalte arbejdsvinduer og ét ansvar pr. grænseflade."),
]

FIRST90 = [
    ("Dage 1–30",
     "Mødt projektlederne en-til-en, gennemgået hele porteføljen og været på begge matrikler: hvad "
     "er lovet, hvad haster, og hvor er der i dag ingen ejer af en beslutning."),
    ("Dage 30–60",
     "Porteføljeoversigt på én side pr. projekt og prioriteringsnøgle indført; faglig kadence med "
     "hver projektleder aftalt; første månedlige ledelsesrapport til ejendomschefen."),
    ("Dage 60–90",
     "Snitflademodel prøvekørt på to projekter mod den tekniske drift; én arbejdsgang "
     "(projektstart eller aflevering) standardiseret; beslutningslog i brug på alle væsentlige "
     "sager."),
    ("Måned 3–6",
     "Porteføljen har styr på økonomi, tid og risiko; projektlederne bruger selv værktøjerne; "
     "kapacitetsmodellen bruges i prioriteringen sammen med fagkoordinatoren."),
    ("Måned 6–12",
     "Overgangen til Ejendomme og Byggerier gennemført uden at projekterne taber fart, og "
     "afleveringerne holder — også når hospitalet bygger videre."),
]

KEYWORDS = (
    "Fagleder for projekter · Drift og Byg · Rigshospitalet · Center for Ejendomme · Region "
    "Hovedstaden · Projektledere · Projektteamet · Bygge- og renoveringsprojekter · "
    "Hospitalsorganisation · Hospitalsvirkelighed · Daglig drift · Kompleksitet · Klare rammer · "
    "Faglig sparring · Tydelige forventninger · Løbende opfølgning · Kvalitet · Fremdrift · "
    "Projektportefølje · Økonomi · Tidsplaner · Risici · Prioritering · Ressourcefordeling · "
    "Samarbejde · Teknisk drift · Supportfunktioner · Interessenter · Fælles metoder · "
    "Arbejdsgange · Fagkoordinator · Koordinering · Beslutninger · Byggeprojekter · "
    "Projektledelse · Beslutning til aflevering · Ledet projektledere · Ledelseserfaring · "
    "Resultater gennem andre · Offentlig bygherrefunktion · Udbud · Kontrakter · Projektopfølgning "
    "· Følgeskab · Retning · Faglighed · Perspektiver · Kompetencer · Trivsel · Fysiske rammer · "
    "Tekniske installationer · Rådgivere · Entreprenører · Sammenhæng · Lokal ledelse · "
    "Ejendomschef · Viceejendomschef · Fagledere · Glostrup · København Ø · Dansk HR Service · "
    "QuickApply · Jobindex · Maskinmester · Lean · SAP"
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
        m.bullet(label, body, after=2, line=222)

    m.para(SYSTEM, after=50, line=226)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=0, line=218)

    m.meta("Med venlig hilsen · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "LEDELSESPROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("PROJEKTOMRÅDETS STYRING — ANVENDT I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER PROJEKTERNE I RYTMEN",
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
    out = os.path.join(ROOT, "Shahram_Ajloo_RegionH_FaglederProjekterRH.docx")
    build(out)
    print("OK " + out)
