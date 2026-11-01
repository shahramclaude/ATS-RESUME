# -*- coding: utf-8 -*-
"""
ISS Danmark — Operational Manager, stor nordisk kontrakt (Ballerup).
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Operational Manager | Integreret FM | Drift gennem ledere"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = ("ISS Danmark · Ballerup · att. Nordic Key Account Director Alexander Kapsch-Tuxen "
             "· Req. 41664")
SUBJECT = "Ansøgning: Operational Manager på en stor nordisk kontrakt"

# ------------------------------------------------------------------ side 1
INTRO = [
    "En integreret FM-kontrakt vindes ikke på den enkelte ydelse, men på kontrakten: på at "
    "rengøring, reception, mødeservice og udendørs spiller sammen med de tekniske services, og på "
    "at kunden oplever ét ansvar og ét svar. Opgaven som Operational Manager er at gøre kontrakten "
    "styrbar — hvert KPI med ejer, måling og fast gennemgang, og én plan pr. lokation på ét ark.",

    "Nedenfor er min motivation og ledelsesmæssige tilgang samt systemet, der står klar fra første "
    "dag: kontraktmodel med KPI-katalog, ledelsesaftaler med de to Service Managers, "
    "snitflademodel mellem Soft FM, Hard FM og Food & Beverage, månedlig kontraktrapport og en "
    "forbedringspipeline med business case.",
]

BULLETS = [
    ("Kravet: lede, udvikle og sætte retning for Service Managers og driftsorganisationen",
     "Løsningen er at lede gennem rammerne, ikke gennem svarene: en skreven ledelsesaftale med "
     "hver Service Manager om resultat, beslutningsret og eskaleringsgrænse, et ledermøde med "
     "beslutningslog og en kvartalsvis retningssamtale. Ledere vokser af klare rammer, ikke af "
     "kontrol — det har jeg selv prøvet som indehaver."),

    ("Kravet: stabil, effektiv og kontraktmæssig serviceleverance på tværs af kundens danske "
     "lokationer",
     "Løsningen er én kontraktmodel på ét ark pr. lokation: ydelser, svartider, kadence og ansvar "
     "— gennemgået hver måned på stedet. Jeg har drevet 24/7-drift med KPI'er i SAP og nul "
     "uplanlagte stop i fem år; stabil leverance er en arbejdsmetode, ikke held."),

    ("Kravet: økonomisk performance — budgetopfølgning, ressourceoptimering, produktivitet og "
     "omkostningsstyring",
     "Løsningen er at måle enhedsomkostninger pr. ydelse og lokation, følge prognosen månedligt og "
     "hente produktiviteten i standardarbejde og efterspørgselsbaseret bemanding — ikke i at skære "
     "timer. Jeg har haft fuldt P&L og løftet produktiviteten 40 %."),

    ("Kravet: systematisk opfølgning på KPI'er, kvalitetsmål, kundetilfredshed og kontraktlige "
     "forpligtelser",
     "Løsningen er et KPI-katalog med ejer, måling, datakilde og grænseværdi, kvalitetskontrol "
     "efter fast skema og en månedlig rapport på få tal — så en afvigelse bliver set, før den "
     "bliver en kundesag. Samme greb holdt et renseanlæg stabilt i fem år."),

    ("Kravet: forbedringsinitiativer, der skaber værdi for både kunden og ISS",
     "Løsningen er en forbedringspipeline, hvor hvert initiativ har en business case med kroner, "
     "risiko og ejer, og hvor der kun køres tre ad gangen — prøvekørt på én lokation og målt, før "
     "det rulles ud. Lean og standardarbejde er min daglige værktøjskasse."),

    ("Kravet: understøtte kontraktens udvikling gennem innovation, bæredygtighed og kommercielle "
     "muligheder",
     "Løsningen er at gøre kontrakten til en platform: energiopitmering og tilstandsbaseret "
     "vedligehold dokumenteret i kroner, ESG-data kunden kan rapportere på, og nye ydelser der "
     "løser et problem, kunden allerede betaler for."),

    ("Kravet: stærkt samarbejde på tværs af serviceområder, lokationer og centrale "
     "supportfunktioner",
     "Løsningen er en snitflademodel: for hver berøringsflade — rengøring mod teknik, reception og "
     "mødeservice mod Food & Beverage, lokation mod account team — er der en grænsefladeejer og en "
     "skreven eskalationsvej. Integrerede kontrakter fejler i sømmene, ikke i fagene."),

    ("Kravet: udvikle organisationen — engagement, arbejdsmiljø, kompetenceudvikling og "
     "sikkerhedskultur",
     "Løsningen er at måle på det, der driver folk: nærvær og gennemtræk som faste KPI'er, "
     "onboarding med to personer på hver kritisk kompetence og en sikkerhedskultur, hvor "
     "nærved-hændelser meldes og lukkes — LOTO og arbejdsmiljø §16 med."),

    ("Kravet: teknisk tyngde i Hard FM — tekniske services og vedligehold af en bygningsmasse",
     "Løsningen er elautoriseret maskinmester (LV/MV/HV) med 20 år i tekniske anlæg: el og "
     "højspænding, ventilation, køl, pumper, CTS/BMS og styringer, kritikalitetsbaseret "
     "vedligehold og tilstandsvurdering. Jeg kan gå i dialog om løsningen — og ved, hvornår jeg "
     "ikke skal."),

    ("Kravet: struktureret, analytisk og datadrevet arbejdsform med målbare resultater i et "
     "internationalt miljø",
     "Løsningen er dashboards på de tal, der styrer leverancen, og rapporter der genereres "
     "automatisk, så tiden går til drift frem for til at samle data. Jeg koder selv i Python, "
     "bruger Claude dagligt og arbejder på dansk og engelsk."),
]

SYSTEM = (
    "Systemet står klar fra første dag: kontraktmodel pr. lokation, KPI-katalog med ejer, måling "
    "og grænseværdi, ledelsesaftaler med de to Service Managers, ugentligt driftmøde på tværs af "
    "Soft FM, Hard FM og Food & Beverage, månedlig kontraktrapport på KPI, økonomi og sikkerhed "
    "samt en forbedringspipeline med business case — ført i Excel og Power BI sammen med ISS' "
    "systemer og genereret i Python og Claude. Mobiliseringsplanen mod opstart 4. januar 2027 "
    "ligger klar uge for uge."
)

MIRROR = (
    "Om kravene: elautoriseret maskinmester (LV/MV/HV) og B.Tech, 20 år i tekniske anlæg, otte år "
    "med personaleansvar — 5 elektrikere og 3 lærlinge med fuldt P&L, 14-mands team, 37 "
    "anlægsprojekter og fem år som driftschef i Biofos med budget i SAP og 24/7-drift."
)

HONEST = (
    "Det skal siges ligeud: jeg har ikke stået i en kommerciel integreret FM-kontrakt med nordisk "
    "kundeansvar før, og min ledelse af ledere er hidtil sket i mindre enheder. Rengøring og soft "
    "FM har jeg købt og styret som leverance, ikke selv leveret. Det, jeg bringer, er teknisk "
    "drift på højt niveau, økonomi med fuldt ansvar og evnen til at bygge styring, der holder."
)

CULTURE = (
    "ISS' værdier — samhørighed, ærlighed, ansvarlighed, kvalitet og iværksætterånd — passer på "
    "den måde, jeg leder på: iværksætterånden har jeg selv prøvet som indehaver, og ansvarlighed "
    "er den eneste valuta i drift. I »A Place to Be You« er det løftet om at blive den, man vil, "
    "der holder folk: uddannelse, karriereveje og en leder, der er der."
)

PRACTICAL = (
    "Bosat i Måløv — cirka 10 minutter i bil til Ballerup, og rejseaktivitet til kundens danske "
    "lokationer er accepteret. Kørekort B og bil, dansk på modersmålsniveau og engelsk "
    "professionelt. Opstart 4. januar 2027 passer med en ryddelig overlevering."
)

CLOSING = (
    "I første samtale vil jeg gerne tale om, hvor kontraktens tre vigtigste sømme er i dag — og "
    "hvilke KPI'er der ikke må glippe efter opstart."
)

# ------------------------------------------------------------------ CV
PROFILE = (
    "Teknisk leder med 20 år i anlæg og drift og otte år med personaleansvar: fem år som drifts- "
    "og vedligeholdelseschef i Biofos med budget i SAP, leverandørstyring og 24/7-drift, to år som "
    "indehaver og teknisk direktør med fuldt P&L og to år som projektleder på 37 samtidige "
    "anlægsprojekter. Arbejder med KPI-kataloger, standardiserede processer og dashboards, og "
    "koder selv de rapporter, ledelsen læser."
)

PRACTICE = [
    ("Ledelse gennem ledere",
     "Ledelsesaftaler med resultat, driftsansvar, beslutningsret og eskaleringsgrænse; fast "
     "ledermøde med beslutningslog; retningssamtale pr. kvartal."),
    ("Kontrakt og leverance",
     "Kontraktmodel pr. lokation med ydelser, svartider og kadence; månedlig gennemgang på stedet; "
     "kvalitetskontrol efter fast skema."),
    ("Økonomi og produktivitet",
     "Budget, prognose, enhedsomkostninger pr. ydelse og optimering af driftsprocesser; "
     "produktivitet hentet i standardarbejde og efterspørgselsbaseret bemanding; fuldt P&L i SAP."),
    ("Hard FM og teknisk drift",
     "El, højspænding, HVAC, køl, pumper og CTS/BMS; kritikalitets- og tilstandsbaseret "
     "vedligehold med nul uplanlagte stop i fem år."),
    ("Snitflader og samarbejde",
     "Grænsefladeejer og skreven eskaleringsvej for hver berøringsflade mellem Soft FM, Hard FM, "
     "Food & Beverage og account team."),
    ("Data og rapportering",
     "Dashboards og automatiseret månedsrapportering i Power BI; Python og Claude i daglig brug "
     "til analyser, oplæg og instrukser."),
]

MODELS = [
    ("Kontraktmodel",
     "Pr. lokation på ét ark: ydelser, svartider, kadence og ansvar — revideret ved "
     "kontraktændring, ikke kun ved klage"),
    ("KPI-katalog",
     "Hver indikator har ejer, måling, datakilde og grænseværdi; status samles i én månedlig "
     "rapport på få tal"),
    ("Ledelsesaftale",
     "Skrevet aftale med hver Service Manager om resultat, beslutningsret og eskaleringsgrænse, "
     "fulgt op hvert kvartal"),
    ("Snitflademodel",
     "Ved hver berøringsflade: grænsefladeejer, aftalt respons og en skreven vej for eskalering"),
    ("Forbedringspipeline",
     "Business case med kroner, risiko og ejer; tre initiativer ad gangen, prøvekørt på én "
     "lokation og målt før udrulning"),
    ("Mobilisering",
     "Frem mod kontraktstart: bemanding, oplæring, udstyr, kvalitetsskemaer og første måling pr. "
     "lokation i et uge-for-uge-skema"),
]

ACHIEVEMENTS = [
    ("Nul uplanlagte stop i fem år",
     "24/7-anlæg med SCADA, højspænding og koblingsanlæg — planlagt vedligehold, tilstandskontrol "
     "og KPI'er i SAP, og en driftsorganisation der holdt, også under sygdom."),
    ("5 elektrikere og 3 lærlinge med fuldt P&L",
     "egen virksomhed: rekruttering, oplæring, arbejdsmiljø, kunder, leverandøraftaler og ansvar "
     "for bundlinjen."),
    ("14-mands team med 11 samtidige opgaver",
     "kapacitetsplanlægning, daglige tavlemøder og tydelig prioritering i eksisterende byggeri med "
     "drift og brugere omkring os."),
    ("37 anlægsprojekter uden kritiske fund",
     "2-10 mio. kr. hos Novo Nordisk med 25 specialister koordineret på tværs af mekanik, el, "
     "proces og indkøb — FAT/SAT og dokumentation der bestod revision."),
]

EXPERIENCE = [
    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7-anlæg · pumper, HVAC, køl, koblingsanlæg og højspænding · budget i SAP",
     [("Drift, vedligehold og driftssikkerhed",
       "planlagt vedligehold, tilstandskontrol og KPI'er i SAP; nul uplanlagte stop i fem år på et "
       "anlæg, hvor driften ikke kunne vente."),
      ("Sikkerhed, leverandører og beredskab",
       "koordinering af egne teknikere, entreprenører og rådgivere — LOTO, arbejdstilladelser, "
       "garantisager og nærved-hændelser fulgt til lukning.")]),

    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og "
     "leverandøraftaler",
     [("Organisation, rekruttering og arbejdsmiljø",
       "byggede virksomheden op fra bunden: rekruttering, oplæringsplaner og arbejdsplaner, "
       "sikkerhed og arbejdsmiljø som fast punkt."),
      ("Økonomi og kunder",
       "tilbudsberegning, indkøb og leverandøraftaler, plan og prognose med fuldt ansvar for "
       "bundlinjen.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2-10 mio. kr.)",
     [("Personale, kapacitet og leverance",
       "14-personers team med kapacitetsplanlægning, daglige tavlemøder og opfølgning på den "
       "enkelte — og 11 samtidige entrepriser i eksisterende byggeri.")]),

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

PRACTICAL_CV = ("Bosat i Måløv — cirka 10 minutter i bil til Ballerup. Rejseaktivitet til kundens "
                "danske lokationer er forventet og accepteret. Kørekort kategori B og bil, dansk "
                "på modersmålsniveau og engelsk professionelt. Opstart 4. januar 2027 passer med "
                "en ryddelig overlevering i mit nuværende ansvar.")

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Biofos (Lynetten), Novo Nordisk A/S, "
              "Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("De to Service Managers",
     "Skreven ledelsesaftale, beslutningsret og et ledermøde med beslutningslog — og en chef, der "
     "tager de svære kundesager selv."),
    ("Kunden og dennes interessenter",
     "Fast kadence på operationelt og taktisk niveau med de samme tal, vi selv styrer på — ingen "
     "overraskelser i en statusrapport."),
    ("Food & Beverage Manager og det nordiske account team",
     "Aftalte snitflader, fælles leverancekalender og én indgang til kunden, så kontrakten "
     "fremstår som én leverance og ikke tre."),
    ("Leverandørerne",
     "Rammeaftaler, performance-review og en plan for, hvad der udbydes hvornår — langsigtet frem "
     "for akut."),
]

FIRST90 = [
    ("Frem mod 4.1.2027",
     "Mobiliseringsplan uge for uge med kunden og account teamet: bemanding, oplæring, udstyr, "
     "kvalitetsskemaer og første måling pr. lokation."),
    ("Dage 1–30",
     "Mødt alle ledere og nøglemedarbejdere, været på hver dansk lokation og læst kontrakten "
     "igennem: hvad er lovet, hvad måles, og hvor er afvigelserne i dag."),
    ("Dage 30–60",
     "KPI-katalog og kontraktmodel på plads; ledelsesaftaler med de to Service Managers indgået; "
     "første månedlige kontraktrapport kørt."),
    ("Dage 60–90",
     "Snitflademodel mellem Soft FM, Hard FM og Food & Beverage indført; én standardiseret "
     "arbejdsgang prøvekørt på en lokation; forbedringspipeline med de første tre business cases."),
    ("Måned 3–6",
     "Stabil leverance dokumenteret på KPI og kundetilfredshed; produktivitetsgevinster målt pr. "
     "ydelse; de første rammeaftaler forhandlet."),
    ("Måned 6–12",
     "Kontrakten udvikler sig kommercielt — nye ydelser, energigevinster og ESG-data — og "
     "organisationen driver selv forbedringerne, mens jeg holder retning og økonomi."),
]

KEYWORDS = (
    "Operational Manager · ISS Danmark · Ballerup · Nordisk kontrakt · Facility Management · "
    "Integrerede Facility Management-kontrakter · Soft FM · Hard FM · Food & Beverage · "
    "Serviceområder · Samlet leverance · Rengøring · Reception · Mødeservice · Kontorservices · "
    "Affaldshåndtering · Vinduespolering · Udendørsarealer · Tekniske services og vedligehold · "
    "Service Managers · Driftsorganisation · Ledelse gennem andre ledere · Driftsleder · "
    "Ledelsesansvar · Selvstændighed · Kontraktmæssig serviceleverance · Standardiserede "
    "processer · Høj kvalitet · Løbende forbedringer · Kundeorienteret serviceleverance · "
    "KPI-opfølgning · Kvalitetsmål · Kundetilfredshed · Kontraktlige forpligtelser · Økonomistyring "
    "· Budgetansvar · Budgetopfølgning · Ressourceoptimering · Produktivitetsforbedringer · Aktiv "
    "omkostningsstyring · Effektivisering · Forbedringsinitiativer · Kontraktudvikling · "
    "Kommerciel forståelse · Kommercielle muligheder · Innovation · Bæredygtighed · Centrale "
    "supportfunktioner · Medarbejderengagement · Arbejdsmiljø · Kompetenceudvikling · "
    "Sikkerhedskultur · Sikkerhed · Samarbejde · Interessenter · Relationsdannelse · Tydelig og "
    "nærværende leder · Følgeskab · Tillid · Involvering · Klare forventninger · Strategiske "
    "beslutninger · Implementering · Struktureret · Analytisk · Datadrevet · Målbare resultater · "
    "Internationalt samarbejdsmiljø · Dansk og engelsk · Nordic Key Account Director · Account "
    "Team · Tilstedeværelse · Rejseaktivitet · Kompleks driftsorganisation · Servicebranchen · "
    "OneISS · Lean · SAP"
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
        m.bullet(label, body, after=2, line=220)

    m.para(SYSTEM, after=50, line=226)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=0, line=216)

    m.meta("Med venlig hilsen · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "LEDELSESPROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("KONTRAKTENS STYRING — ANVENDT I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER KONTRAKTEN I DRIFT",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN LEDES KONTRAKTEN — DE FIRE PARTER")
    for label, body in PARTNER:
        m.bullet(label, body, after=30)

    m.section("PRAKTISK OM ANSÆTTELSEN")
    m.para(PRACTICAL_CV, after=80)

    m.section("REFERENCER")
    m.para(REFERENCES, after=0)

    m.save(path)


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_ISS_OperationalManager.docx")
    build(out)
    print("OK", out)
