# -*- coding: utf-8 -*-
"""
Aalborg Forsyning — Direktør for Energi (200+ medarbejdere, øverste koncernledelse).
Dansk JD. Opgave-først side 1 + CV + 90 dage/parter i ét dokument.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Direktør for Energi | Forsyningssikkerhed og grøn omstilling | Store tekniske anlæg"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = "Aalborg Forsyning · Direktør for Energi · via Curia, Aalborg"
SUBJECT = "Ansøgning: Direktør for Energi — den største transformation af Aalborgs energiforsyning i nyere tid"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Aalborg Forsyning skal gøre det sværeste, en forsyning kan: udskifte en kulbaseret "
    "varmeproduktion med et mere komplekst energimiks, mens 50.000 kunder fortsat skal have varme, "
    "fjernkøling og bygas hver dag, og mens økonomi, organisation og beredskab udvikles i samme "
    "tempo. En transformation af den størrelse vindes ikke på strategien alene, men på at anlæg, "
    "investeringer og beslutninger bliver styret i den rigtige rækkefølge — forsyningssikkerhed "
    "først, og omstillingen bygget ovenpå, mens driften kører.",

    "Nedenfor er systemet, der står klar fra første dag: anlægs- og aktivkort over hele "
    "energiområdet, investeringsportefølje med business case pr. projekt, beredskabs- og "
    "driftsplan, integrationsplan for nye produktionsanlæg og energikilder, kompetencemodel, "
    "interessentkort og en månedlig resultatrapport til direktionen.",
]

BULLETS = [
    ("Kravet: sætte den strategiske retning for energiområdet og sikre gennemførelse",
     "Løsningen er en gennemførelsesplan med få, navngivne initiativer pr. år — hver med ejer, "
     "milepæl, investeringsramme og et tal, der viser, om det virker — og en kvartalsvis revision, "
     "hvor det, der ikke leverer, bliver stoppet."),

    ("Kravet: sikre høj forsyningssikkerhed, stabil drift og et robust beredskab",
     "Løsningen er et anlægs- og aktivkort over energiområdet med kritikalitet, tilstand, "
     "vedligeholdelsesinterval og ansvarlig — og en prioriteringsnøgle, der lægger "
     "forsyningssikkerhed og myndighedskrav over alt andet. Fem år som driftschef på et "
     "24/7-anlæg med nul uplanlagte stop og højspænding, koblingsanlæg, pumper og køl er netop den "
     "disciplin."),

    ("Kravet: samlet resultatansvar og kommercielt fokus",
     "Løsningen er at kende sin dækningsgrad, sin investeringsramme og sin kapacitetsomkostning — "
     "og at styre efter dem i stedet for at forklare dem bagefter. Jeg har haft fuldt P&L-ansvar i "
     "egen virksomhed og budgetansvar som driftschef med månedlig opfølgning i SAP."),

    ("Kravet: lede den kort- og langsigtede energiplanlægning",
     "Løsningen er en energimodel, der kan svare på tre spørgsmål: hvad koster det at levere varme "
     "og køling i 2029, hvad gør en ny kilde ved forsyningssikkerheden, og hvad er "
     "beslutningsrækkefølgen. Modellen ligger i Excel og Power BI og opdateres, når priser og "
     "rammer flytter sig."),

    ("Kravet: fremdrift i den grønne transformation og de væsentlige investeringsprojekter",
     "Løsningen er en investeringsportefølje med business case pr. projekt og en fast "
     "gate-model: beslutning, kontrakt, idriftsættelse, gevinst. Jeg har været projektleder på 37 "
     "anlægsprojekter i 2-10 mio. kr.-klassen og leveret uden kritiske fund — og jeg ved, at "
     "store anlægsprojekter sjældent fejler på teknikken, men på snitfladerne."),

    ("Kravet: udvikle organisation, ledelse og kompetencer i takt med omstillingen",
     "Løsningen er en kompetencemodel pr. faggruppe, en skreven snitflade mellem drift, projekt og "
     "salg og en ledelseskæde, hvor hver leder har tre til fem mål, der kan ses. Kompetencerne skal "
     "være der, når anlæggene er det — ikke omvendt."),

    ("Kravet: styrke kundeoplevelsen og udvikle relevante energiløsninger",
     "Løsningen er at måle kundeoplevelsen på få, stabile tal — svartider, klager, afbrydelser, "
     "fakturakorrekthed — og at udvikle nye løsninger som forsøg på et afgrænset kundesegment, før "
     "de bliver standard. Jeg har bygget en serviceforretning på præcis den logik."),

    ("Kravet: stærke relationer til ejer, bestyrelser, myndigheder, kunder og samarbejdspartnere",
     "Løsningen er et interessentkort, hvor det for hver part står, hvad de skal beslutte, hvornår "
     "de skal inddrages, og hvad de har brug for at se. Ejer og bestyrelse skal have "
     "beslutningsoplæg på én side: hvad vi gør, hvad det koster, hvad det giver — og hvornår vi ved, "
     "om det virkede."),

    ("Kravet: arbejdsmiljø, sikkerhed, compliance, miljø, risikostyring — og følgeskab gennem "
     "forandringer",
     "Løsningen er en risikotavle, der bliver gennemgået fast, sikkerhed som første punkt på "
     "ledelsesmødet, og en forandringsplan, hvor medarbejderne hører om beslutningen, før den bliver "
     "iværksat. Følgeskab kommer af at være synlig på anlæggene."),
]

SYSTEM = (
    "Systemet står klar fra første dag: anlægs- og aktivkort med kritikalitet og tilstand, "
    "investeringsportefølje med business case og gate-model, beredskabs- og driftsplan, "
    "integrationsplan for nye produktionsanlæg og energikilder, kompetencemodel, interessentkort og "
    "en månedlig resultatrapport — ført i Excel og Power BI, med beslutningsoplæg og scenarier "
    "bygget i Python og Claude."
)

MIRROR = (
    "Om profilen: elautoriseret maskinmester (LV/MV/HV) og B.Tech, 20 år i tekniske anlæg og otte "
    "år med personaleansvar — driftschef på et 24/7-anlæg med nul uplanlagte stop i fem år og "
    "budget i SAP, projektleder på 37 anlægsprojekter uden kritiske fund, leder af 14 mand med 11 "
    "samtidige entrepriser og 25 specialister, og indehaver af en servicevirksomhed med fuldt P&L. "
    "Regulerede miljøer, myndighedskrav og komplekse snitflader er arbejdsvilkår, ikke "
    "undtagelser."
)

HONEST = (
    "Det skal siges ligeud: jeg har ikke været direktør i en koncernledelse og ikke ledet en "
    "organisation med mere end 200 medarbejdere. Min ledelse har været på afdelings- og "
    "driftschefniveau med 5-25 medarbejdere og med fuldt ansvar for drift, økonomi og resultater. "
    "Jeg søger stillingen, fordi opgaven er den, jeg har arbejdet mig mod i tyve år — "
    "forsyningssikkerhed og omstilling af store tekniske anlæg — og fordi jeg ved præcis, hvad jeg "
    "skal lære i det første år: den politiske og bestyrelsesmæssige del af rollen."
)

CULTURE = (
    "Aalborg Forsyning er en af Danmarks største multiforsyninger med et samfundsansvar, der "
    "rækker længere end regnskabet: 50.000 varmekunder, kritisk infrastruktur og en omstilling, "
    "borgerne kan se. Organisationen har været gennem en tilpasning af ledelsesstrukturen og skal "
    "nu ledes med ro og retning, mens den forandrer sig. Rollen kræver en synlig og nærværende "
    "leder — og en ærlig forklaring på, hvorfor en beslutning blev taget."
)

PRACTICAL = (
    "Bosat i Måløv — cirka 4 timer og et kvarter i bil til Aalborg. Indstillet på fast ugentlig "
    "tilstedeværelse i Aalborg og på at være tæt på anlæg og ledere fra første uge, og åben for at "
    "drøfte en ordning med bopæl tættere på. Kørekort B og bil, dansk på modersmålsniveau og "
    "engelsk professionelt. Kan tiltræde hurtigst muligt."
)

CLOSING = (
    "I første samtale vil jeg gerne tale om, hvilke tre beslutninger der har størst betydning for "
    "forsyningssikkerheden frem mod 2029 — og hvordan I følger op på, om investeringerne leverer "
    "det, de blev besluttet på."
)

# ------------------------------------------------------------------ CV
PROFILE = (
    "Elautoriseret maskinmester (LV/MV/HV) og B.Tech med 20 år i tekniske anlæg og otte år med "
    "personaleansvar. Fem år som driftschef på et 24/7-anlæg med højspænding, koblingsanlæg, "
    "pumper, HVAC og køl — nul uplanlagte stop og budget i SAP. Projektleder på 37 anlægsprojekter "
    "i GMP-reguleret drift uden kritiske fund. Leder af 14 mand med 11 samtidige entrepriser og 25 "
    "specialister, og indehaver af en servicevirksomhed med fuldt P&L. Arbejder med anlægs- og "
    "aktivkort, investeringsporteføljer, beredskabsplaner og KPI-tavler — og bygger selv de "
    "modeller, beslutningerne hviler på."
)

PRACTICE = [
    ("Forsyningssikkerhed og drift",
     "Anlægs- og aktivkort med kritikalitet, tilstand, vedligeholdelsesinterval og ansvarlig; "
     "prioriteringsnøgle hvor sikkerhed og myndighedskrav kommer før økonomi."),
    ("Investeringer og portefølje",
     "Business case pr. projekt med gate-model — beslutning, kontrakt, idriftsættelse, gevinst — og "
     "kvartalsvis revision af, om gevinsten blev realiseret."),
    ("Energiplanlægning",
     "Energimodel i Excel og Power BI: omkostning pr. leveret enhed, følsomhed på priser og "
     "rammer, forsyningssikkerhed og beslutningsrækkefølge frem mod 2029."),
    ("Integration af nye anlæg",
     "Skrevet integrationsplan pr. ny kilde eller anlæg: grænseflader til drift, driftsoverlevering, "
     "dokumentation, kompetencebehov og ansvar — før anlægget er færdigt."),
    ("Organisation og kompetencer",
     "Kompetencemodel pr. faggruppe, ledelseskæde med tre til fem mål pr. leder og en "
     "forandringsplan, hvor medarbejderne hører om beslutningen, før den iværksættes."),
    ("Interessenter og beslutningsoplæg",
     "Interessentkort over ejer, bestyrelse, myndigheder, kunder og samarbejdspartnere, og "
     "beslutningsoplæg på én side med risiko, økonomi og succeskriterium."),
]

MODELS = [
    ("Anlægs- og aktivkort",
     "Kritikalitet, tilstand, vedligeholdelsesinterval og ansvarlig pr. anlæg i hele "
     "energiområdet"),
    ("Investeringsportefølje",
     "Business case og gate-model pr. projekt — investering, effekt, risiko, tilbagebetaling og "
     "realiseret gevinst"),
    ("Beredskabs- og driftsplan",
     "Scenarier, responstider, vagtordning og øvelser — prøvet af, ikke bare skrevet ned"),
    ("Integrationsplan",
     "Nye produktionsanlæg og energikilder koblet på drift, dokumentation og kompetence med "
     "milepæle og ejer"),
    ("Kompetencemodel",
     "Fag, certifikater og bemanding pr. område — kompetencerne skal være der, når anlæggene er "
     "det"),
    ("Interessentkort",
     "Ejer, bestyrelse, myndigheder, kunder og partnere: hvad de skal beslutte, og hvornår de skal "
     "inddrages"),
    ("Resultatrapport",
     "Månedligt på få tal: forsyningssikkerhed, afbrydelser, økonomi, investeringsfremdrift, "
     "kundetilfredshed og arbejdsmiljø"),
]

ACHIEVEMENTS = [
    ("Nul uplanlagte stop i fem år",
     "24/7-anlæg med højspænding, koblingsanlæg, pumper, HVAC og køl — planlagt og tilstandsbaseret "
     "vedligehold, KPI'er i SAP og prioritering mellem afhjælpning og investering."),
    ("37 anlægsprojekter uden kritiske fund",
     "2-10 mio. kr. i industriel og GMP-reguleret drift: 25 specialister koordineret på tværs af "
     "mekanik, el, proces og indkøb; FAT/SAT, IQ/OQ/PQ, myndighedsdokumentation og "
     "driftsoverlevering."),
    ("14-mands team med 11 samtidige entrepriser",
     "kapacitetsplanlægning, daglige tavlemøder og opfølgning på den enkelte — leverancer, der ikke "
     "gik ud over driften i eksisterende byggeri med brugere omkring os."),
    ("Serviceforretning med fuldt P&L",
     "ELOHVAC: 5 elektrikere og 3 lærlinge, 40+ serviceanlæg, eget kundekartotek og ansvar for "
     "dækningsgrad, bundlinje og investeringer — bygget fra ingenting."),
]

EXPERIENCE = [
    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og "
     "leverandøraftaler",
     [("Drift, indtjening og investeringer",
       "servicekatalog med responstider, aftaler pr. kunde, tilbudsberegning og leverandøraftaler "
       "med fuldt ansvar for dækningsgrad og bundlinje."),
      ("Organisation, sikkerhed og arbejdsmiljø",
       "byggede virksomheden op fra bunden: rekruttering, oplæringsplaner, arbejdsplaner og "
       "sikkerhed som fast punkt på tavlemødet.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2-10 mio. kr. · 25 specialister · GMP/FDA/EMA",
     [("Koordinering, snitflader og aflevering",
       "25 specialister koordineret på tværs af mekanik, el, proces og indkøb; fremdrift og "
       "rapportering til styregruppe; FAT/SAT, IQ/OQ/PQ og aflevering uden kritiske fund."),
      ("Ændringer, dokumentation og myndighedskrav",
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
     "Anvendt i drift, service og projekter · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og projekter · 2017 – nu"),
]

LANGUAGES = ("Dansk (modersmål, skrift og tale) · Engelsk (professionelt, skrift og tale) · "
             "Persisk/farsi · Kørekort B (kategori B)")

PRACTICAL_CV = (
    "Bosat i Måløv — cirka 4 timer og et kvarter i bil til Aalborg. Indstillet på fast ugentlig "
    "tilstedeværelse i Aalborg og på at være tæt på anlæg og ledere fra første uge; åben for at "
    "drøfte en ordning med bopæl tættere på Aalborg. Kørekort kategori B og bil, dansk på "
    "modersmålsniveau og engelsk professionelt. Kan tiltræde hurtigst muligt."
)

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Biofos (Lynetten), Novo Nordisk A/S, "
              "Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Medarbejderne og lederne i energiområdet",
     "Kompetencemodel og en forandringsplan, hvor medarbejderne hører om beslutningen, før den "
     "iværksættes — omstillingen skal bæres af dem, der står med anlæggene."),
    ("Administrerende direktør og koncernledelsen",
     "Beslutningsoplæg på én side med risiko, økonomi og succeskriterium, og en månedlig "
     "resultatrapport på få tal — så ledelsen kan beslutte, ikke bare orientere sig."),
    ("Ejer, bestyrelser og myndigheder",
     "Interessentkort og en fast mødekadence: hvad den enkelte part skal beslutte, hvornår de skal "
     "inddrages, og hvilke dokumenter de har brug for — i god tid før fristen."),
    ("Kunder, overskudsvarmeleverandører og samarbejdspartnere",
     "Faste leveranceaftaler med responstider og en fælles opfølgning på forsyningssikkerhed — "
     "relationen skal kunne holde til en vinter med pres på."),
]

FIRST90 = [
    ("Dage 1–30",
     "Gået alle væsentlige anlæg igennem med driftslederne: tilstand, kritikalitet, kendte risici "
     "og næste beslutning. Mødt ejer, bestyrelsesformand, myndigheder og de væsentligste "
     "overskudsvarmeleverandører. Talt med hver leder i energiområdet om, hvad der driller."),
    ("Dage 30–60",
     "Anlægs- og aktivkort og forsyningssikkerheds-KPI'er på plads; investeringsporteføljen "
     "gennemgået med business case og gate-model; beredskabsplanen testet; første månedlige "
     "resultatrapport til direktionen."),
    ("Dage 60–90",
     "Energiplan frem mod 2029 med beslutningsrækkefølge og følsomheder; integrationsplan for de "
     "næste nye anlæg og energikilder; kompetencemodel og ledelsesmål pr. leder; "
     "interessentkortet i brug."),
    ("Måned 3–6",
     "Forsyningssikkerhed og økonomi målt stabilt over tre måneder, de første "
     "investeringsbeslutninger taget på et ensartet grundlag, og organisationen har en kendt "
     "forandringsplan."),
    ("Måned 6–12",
     "Omstillingen har en synlig fremdrift med milepæle, anlæggene er integreret i driften, og "
     "energiområdet leverer det, det skal — til kunderne, ejeren og medarbejderne."),
]

KEYWORDS = (
    "Direktør for Energi · Aalborg Forsyning · Aalborg · Multiforsyning · Koncernledelse · "
    "Energiområdet · Energiproduktion · Distribution af fjernvarme · Fjernkøling · Bygas · "
    "Strategisk energiplanlægning · Salg og service · Fremtidens energiløsninger · "
    "Forsyningssikkerhed · Stabil drift · Robust beredskab · Resultatansvar · Kommercielt fokus · "
    "Energimiks · Grøn omstilling · Grøn transformation · Investeringsprojekter · "
    "Investeringsportefølje · Vedligeholdelsesaktiviteter · Udviklingsprojekter · "
    "Integration af produktionsanlæg · Energikilder · Beslutningsoplæg · Direktion · Bestyrelser · "
    "Myndighedshåndtering · Interessenthåndtering · Arbejdsmiljø · Sikkerhed · Compliance · Miljø · "
    "Risikostyring · Organisationsudvikling · Forandringsledelse · Følgeskab · Kompetencer · "
    "Kundeoplevelse · Ejer · Regulerede markeder · Politisk tæft · Organisatorisk forståelse · "
    "Strategisk udsyn · Driftsforståelse · Gennemførelseskraft · Beslutningsstyrke · "
    "Uddelegerende · Personaleleder · Integritet · Troværdighed · Synlig leder · Nærværende · "
    "Tydelig kommunikator · Analytisk · Struktureret · Helhedsorienteret · 2029"
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

    m.models_table("ENERGIOMRÅDETS STYRING — ANVENDT I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER OMSTILLINGEN I RYTMEN",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN LEDES ENERGIOMRÅDET — DE FIRE PARTER")
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
    out = os.path.join(ROOT, "Shahram_Ajloo_AalborgForsyning_DirektoerEnergi.docx")
    build(out)
    print("OK " + out)
