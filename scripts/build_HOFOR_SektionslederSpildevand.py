# -*- coding: utf-8 -*-
"""
HOFOR A/S — Sektionsleder til Spildevands- og byggemodningsprojekter.
Dansk JD (motiveret CV). Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Sektionsleder | Personaleledelse af tekniske specialister | København"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = ("HOFOR A/S · Ørestads Boulevard 35, 2300 København S · "
             "att. områdechef Trine Sannem Mønsted")
SUBJECT = "Motiveret CV: Sektionsleder — Spildevands- og byggemodningsprojekter"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Sektionen skal vokse, mens projekterne bliver flere, og den faglige ledelse ligger hos tre "
    "projektchefer. Sektionslederens opgave er derfor ikke at lede projekterne, men at lede "
    "menneskene og kapaciteten: 17-20 projektledere, specialister og byggeledere skal have et godt "
    "arbejdsmiljø, en tydelig prioritering og den rette person på det rette projekt — også når "
    "strukturen omkring dem justeres.",

    "Nedenfor er min motivation og ledelsesmæssige tilgang samt det system, der står klar fra første "
    "dag: kompetence- og kapacitetsoversigt, en-til-en-kadence med udviklingsaftaler, "
    "rekrutterings- og oplæringsplan, bemandingsforum med projektcheferne og trivselsmåling med "
    "opfølgning.",
]

BULLETS = [
    ("Kravet: sikre et godt fysisk og psykisk arbejdsmiljø med fokus på trivsel, dialog og samarbejde",
     "Løsningen er at gøre arbejdsmiljøet konkret: fast trivselsmåling med opfølgning på de tre "
     "vigtigste temaer, arbejdsmiljø som punkt i hver en-til-en-samtale og en leder, der er synlig på "
     "pladsen. Jeg er uddannet i arbejdsmiljø (§16) og har haft ansvar for sikkerhed og trivsel i "
     "24/7-drift og i egen virksomhed."),

    ("Kravet: lede, udvikle og rekruttere medarbejdere — sektionen skal vokse de kommende år",
     "Løsningen er en rekrutteringsplan, der følger porteføljen: hvilke kompetencer der skal til, "
     "hvornår de skal være ansat, hvordan de kommer godt ind, og hvem der oplærer hvem. Jeg har "
     "rekrutteret og oplært både elektrikere og lærlinge, mens opgaverne kom ind."),

    ("Kravet: sikre den rette bemanding og prioritering af ressourcer",
     "Løsningen er en kapacitetsmodel pr. måned med kompetence, belægning og næste behov — så "
     "bemanding bliver en beslutning i fællesskab med projektcheferne og ikke en brandslukning. Jeg "
     "har planlagt kapacitet for 14-mands montageteam med 11 samtidige entrepriser og koordineret 25 "
     "specialister på tværs af fag."),

    ("Kravet: samarbejde tæt med projektcheferne i en matrixorganisation",
     "Løsningen er at gøre matrixen eksplicit: hvem har den faglige retning, hvem har "
     "personaleledelsen, hvordan træffes beslutningen om at flytte en medarbejder, og hvordan "
     "håndteres uenighed. Det bliver skrevet ned og prøvet af i praksis — en matrix fejler sjældent på "
     "vilje, men på uklarhed."),

    ("Kravet: understøtte udviklingsarbejdet i området — fælles arbejdsgange og processer",
     "Løsningen er at oversætte fælles arbejdsgange til noget, medarbejderne bruger: en proces "
     "indføres med en ejer, en instruktion på én side og en prøvekørsel på et rigtigt projekt. Jeg har "
     "standardiseret afleverings- og dokumentationspakker på tværs af 37 anlægsprojekter."),

    ("Kravet: samarbejde på tværs af HOFOR, bl.a. med plan- og driftsafdelinger",
     "Løsningen er en fast snitflade mod plan og drift: hvad skal drift og plan have leveret, hvornår "
     "og i hvilken form, aftalt før projekterne starter. Jeg kommer selv fra driftssiden — fem år på "
     "et 24/7-anlæg — og ved, hvad der irriterer driften, når et anlæg bliver overdraget."),

    ("Kravet: erfaring fra en kompleks organisation eller matrixstruktur, struktureret med overblik og "
     "beslutningskraft",
     "Løsningen er at lede på skriftlighed og rytme: en månedlig sektionsgennemgang, en beslutningslog "
     "med ejer og frist og prioriteter meldt ud, før de bliver et problem. Jeg har arbejdet i "
     "GMP-regulerede anlægsorganisationer og i egen virksomhed."),

    ("Kravet: tillidsbaseret og involverende ledelse med oprigtig interesse for mennesker og deres "
     "udvikling",
     "Løsningen er en tilgang, hvor forventninger aftales i stedet for pålægges: hver medarbejder har "
     "en udviklingsaftale med to til tre punkter, og jeg spørger, før jeg instruerer. Det er ikke et "
     "princip, jeg har læst mig til, men noget jeg måtte lære som ung teamleder."),

    ("Kravet: navigere sikkert mellem ledelse på flere niveauer og skabe følgeskab om retningen",
     "Løsningen er at være tydelig om, hvad der er min beslutning, hvad der er projektchefens, og hvad "
     "der besluttes i ledergruppen — og at stå ved den. Jeg har refereret til styregrupper i 37 "
     "projekter og selv siddet på den side, der skulle levere."),
]

SYSTEM = ("Systemet er allerede bygget: kompetence- og kapacitetsoversigt over sektionen, fast "
          "en-til-en-kadence med udviklingsaftaler, trivselsmåling med opfølgning på faste temaer, "
          "rekrutterings- og oplæringsplan koblet til porteføljen, bemandingsforum med projektcheferne "
          "og en beslutningslog med ejer og frist — ført i Excel/Power BI og HR-systemet, med "
          "opgørelser og status genereret i Python og Claude.")

MIRROR = ("Om kravene: 20 år i tekniske anlæg, otte år med personaleansvar — 14-mands team, 5 "
          "elektrikere og 3 lærlinge med fuldt P&L, 25 specialister koordineret på tværs af fag og fem "
          "år som drifts- og vedligeholdelseschef på et 24/7-renseanlæg. Elautoriseret maskinmester "
          "(LV/MV/HV), B.Tech og Lean/SAP i daglig brug.")

HONEST = ("To ting skal siges ligeud: jeg har ikke ledet 17-20 projektledere og byggeledere i en "
          "matrixorganisation med tre projektchefer — min ledelse har været tættere på opgaven, med "
          "mindre teams. Og jeg har ikke arbejdet med byggemodning i en bygherreorganisation. Til "
          "gengæld har jeg fem år på driftssiden af et renseanlæg og ved, hvad et anlæg kræver, når det "
          "er overdraget.")

CULTURE = ("Hvorfor HOFOR: I giver plads — til at forfølge de store ideer og til at tage de små, til "
           "at dyrke detaljen og til at tegne de store linjer. For en sektionsleder er det præcis den "
           "balance, der gør arbejdet værd: medarbejderne skal have plads, og sektionen skal levere. Og "
           "jeres portefølje bliver boende i byen i generationer.")

PRACTICAL = ("Praktisk: bosat i Måløv, 25 minutter til Ørestads Boulevard 35; kørekort B og bil. "
             "Dansk på modersmålsniveau og engelsk professionelt. Kan tiltræde hurtigst muligt og er "
             "til rådighed i uge 46 og 47. CV'et er uden billede, som I beder om.")

CLOSING = ("I første samtale vil jeg gerne høre, hvordan I i dag fordeler arbejdet mellem den "
           "personaleledelsesmæssige og den faglige ledelse, når en byggeleder er presset på to "
           "projekter samtidig.")

# ------------------------------------------------------------------ CV
PROFILE = ("Stillingen kræver en personaleleder, der kan få 17-20 projektledere, specialister og "
           "byggeledere til at trives og levere i en matrixorganisation — og holde bemanding og "
           "prioritering sammen med tre projektchefer, mens sektionen vokser. Otte år med "
           "personaleansvar: 14-mands team med 11 samtidige entrepriser, 5 elektrikere og 3 lærlinge "
           "med fuldt P&L, 25 specialister koordineret på tværs af fag og fem år som drifts- og "
           "vedligeholdelseschef på et 24/7-renseanlæg. Elautoriseret maskinmester (LV/MV/HV) og "
           "B.Tech.")

PRACTICE = [
    ("Personaleledelse",
     "En-til-en-kadence med udviklingsaftale og faglig sparring; forventninger aftalt frem for "
     "pålagt, og beslutninger forklaret."),
    ("Arbejdsmiljø og trivsel",
     "Trivselsmåling med opfølgning på faste temaer, arbejdsmiljø som fast punkt i samtalerne, "
     "sikkerhedsrunder og nærved-hændelser uden skyld."),
    ("Rekruttering og oplæring",
     "Plan koblet til porteføljen: kompetencebehov, timing, onboarding og oplæring med to personer pr. "
     "kritisk kompetence."),
    ("Kapacitet og bemanding",
     "Kapacitetsmodel pr. måned med kompetence, belægning og næste behov; bemandingsforum med "
     "projektcheferne og beslutninger med ejer og frist."),
    ("Matrix og snitflader",
     "Skrevet beslutningsret: hvem har faglig retning, hvem har personaleledelse, hvordan flyttes en "
     "medarbejder, og hvordan håndteres uenighed."),
    ("Processer og arbejdsgange",
     "Fælles arbejdsgange oversat til én sides instruktion, prøvekørt på et rigtigt projekt og "
     "justeret, før det bliver meldt ud som standard."),
]

MODELS = [
    ("Sektionsoversigt",
     "Kompetence, belægning og udviklingsbehov pr. medarbejder; opdateret før bemandingsforum hver "
     "måned"),
    ("Udviklingsaftaler",
     "To til tre punkter pr. medarbejder med fokus på faglighed, samarbejde og næste skridt; fulgt "
     "op hver anden måned"),
    ("Trivsel og arbejdsmiljø",
     "Måling med opfølgning på faste temaer, sikkerhedsrunder og nærved-hændelser uden skyld — "
     "behandlet som driftsdata, ikke som holdning"),
    ("Rekruttering",
     "Behov fra porteføljen, profil, proces og onboarding; oplæringsplan med to personer pr. kritisk "
     "kompetence"),
    ("Matrix",
     "Én side med beslutningsret: faglig retning, personaleledelse, flytning af medarbejdere og "
     "eskalering"),
    ("Opfølgning",
     "Månedlig gennemgang af bemanding, sygefravær, trivsel og leverancer; rapporter genereret i "
     "Python og Claude"),
]

ACHIEVEMENTS = [
    ("14-mands team med 11 samtidige entrepriser",
     "kapacitetsplanlægning, daglige tavlemøder, tydelig prioritering og leverancer til aftalt tid i "
     "eksisterende byggeri med drift og brugere omkring os."),
    ("5 elektrikere og 3 lærlinge med fuldt P&L",
     "egen virksomhed: rekruttering, oplæring, arbejdsmiljø, kunder, leverandøraftaler og ansvar for "
     "bundlinjen."),
    ("Nul uplanlagte stop i fem år",
     "24/7-renseanlæg med SCADA, højspænding og koblingsanlæg — planlagt vedligehold, KPI'er i SAP "
     "og en driftsorganisation, der holdt, også under sygdom."),
    ("37 anlægsprojekter uden kritiske fund",
     "2–10 mio. kr. hos Novo Nordisk med 25 specialister koordineret på tværs af mekanik, el, proces "
     "og indkøb, FAT/SAT og dokumentation der bestod revision."),
    ("+40 % produktivitet og standardiserede arbejdsgange",
     "dokumenterede forbedringer gennem standardarbejde, Lean og dataunderstøttet planlægning."),
]

EXPERIENCE = [
    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Personale, kapacitet og trivsel",
       "14-personers team med kapacitetsplanlægning, daglige tavlemøder, oplæring, arbejdsmiljø og "
       "opfølgning på den enkelte — og 11 samtidige entrepriser i eksisterende byggeri.")]),

    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og leverandøraftaler",
     [("Rekruttering, oplæring og arbejdsmiljø",
       "personaleansvar for 5 elektrikere og 3 lærlinge, oplæringsplaner og arbejdsplaner; sikkerhed "
       "og arbejdsmiljø som fast punkt."),
      ("Økonomi og kunder",
       "tilbudsberegning, indkøb og leverandøraftaler, plan og prognose med fuldt ansvar for "
       "bundlinjen.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 spildevandsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · budgetter i SAP",
     [("Drift, vedligehold og anlægsforståelse",
       "planlagt vedligehold, tilstandskontrol og KPI'er i SAP; nul uplanlagte stop i fem år på et "
       "anlæg, hvor spildevandet ikke kan vente."),
      ("Sikkerhed, leverandører og beredskab",
       "koordinering af egne teknikere, entreprenører og rådgivere — LOTO, arbejdstilladelser, "
       "garantisager og nærved-hændelser fulgt til lukning.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister · GMP/FDA/EMA",
     [("Koordinering og aflevering",
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

PRACTICAL_CV = ("Bosat i Måløv — cirka 25 minutter til Ørestads Boulevard 35; kørekort kategori B og "
                "bil. Dansk på modersmålsniveau og engelsk professionelt. Kan tiltræde hurtigst muligt "
                "eller efter aftale. CV'et er uden billede, som HOFOR beder om.")

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Biofos (Lynetten), Novo Nordisk A/S, "
              "Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Medarbejderne i sektionen",
     "Fast en-til-en-kadence med udviklingsaftale, tydelig prioritering og en leder, der er synlig — "
     "og som tager den svære samtale, når den er nødvendig."),
    ("Projektcheferne",
     "Bemandingsforum hver måned og en skreven beslutningsret: faglig retning hos dem, "
     "personaleledelse hos mig, og en aftalt vej, når en medarbejder skal flyttes."),
    ("Plan, drift og resten af HOFOR",
     "Aftalt leverance, form og tidspunkt fra projekt til plan og drift, og fælles arbejdsgange "
     "prøvekørt, før de bliver standard."),
]

FIRST90 = [
    ("Uge 1–2",
     "Mødt alle i sektionen og talt med hver enkelt om opgaver, trivsel og udviklingsønske; gennemgået "
     "porteføljen med de tre projektchefer og set, hvor belastningen reelt ligger."),
    ("Uge 3–6",
     "Kompetence- og kapacitetsoversigt færdig; bemandingsforum og beslutningslog etableret; "
     "trivselstemaer valgt og målt første gang, så vi har et udgangspunkt."),
    ("Uge 7–12",
     "Rekrutteringsplan for væksten lagt; oplæringsplan med to personer pr. kritisk kompetence; "
     "matrixens beslutningsret skrevet ned og prøvet af i en konkret sag."),
    ("Måned 3–6",
     "Udviklingsaftaler for alle, første runde gennemført; arbejdsmiljø og sygefravær fulgt fast; "
     "fælles arbejdsgange indført med ejer og instruktion på én side."),
    ("Måned 6–12",
     "Sektionen vokser uden at trivslen falder: bemanding, oplæring og prioritering hænger sammen, "
     "og projektcheferne oplever, at de får den kapacitet, de er lovet."),
]

KEYWORDS = (
    "Sektionsleder · Spildevands- og byggemodningsprojekter · Personaleleder · Trivsel · Samarbejde · "
    "Projekteksekvering · Spildevand · Overfladevand · Byområder · Byggemodning · Grønne veje · "
    "Ledningsrenoveringer · Hovedstadsområdet · HOFOR · Bæredygtige løsninger · Robust forsyning · "
    "Byggeri & Anlæg · Vand- og Spildevandsprojekter · Vandforsyning · Infrastruktur · Projektledere · "
    "Specialister · Byggeledere · Anlægsprojekter · Klimatilpasning · Interessenthåndtering · Vækst · "
    "Organisering · Ansvarsområder · Strategisk ledelse · Faglig ledelse · Projektchefer · Fremdrift · "
    "Tværgående ledelse · Udvikling · Kapacitetsstyring · Matrixorganisation · Ledergruppe · "
    "Matrixstruktur · Fysisk og psykisk arbejdsmiljø · Rekruttere · Bemanding · Prioritering af "
    "ressourcer · Prioritere · Arbejdsgange · Processer · Plan- og driftsafdelinger · Overblik · "
    "Træffe beslutninger · Relationsorienteret · Sammenhæng på tværs af fagligheder · Tillidsbaseret · "
    "Involverende · Menneskers udvikling · Kommunikerer tydeligt · Følgeskab · Mål og strategier · "
    "Ledelse på flere niveauer · Motiveret CV · Ledelsesmæssig tilgang · Inkluderende kultur · "
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

    m.models_table("SEKTIONENS STYRING — ANVENDT I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER SEKTIONEN I RYTMEN",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN LEDES SEKTIONEN — DE TRE PARTER")
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
                  title="Motiveret CV — Sektionsleder, Spildevands- og byggemodningsprojekter, HOFOR A/S",
                  subject="Personaleledelse · arbejdsmiljø · kapacitetsstyring · matrixorganisation · "
                          "rekruttering · byggeri og anlæg",
                  keywords=("sektionsleder, hofor, spildevand, byggemodning, matrixorganisation, "
                            "personaleledelse, arbejdsmiljø, kapacitetsstyring, rekruttering, "
                            "maskinmester, dansk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Motiveret CV side 1 (krav → løsning), CV side 2-3, 90 dage side 4. "
                           "Uden billede.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_HOFOR_SektionslederSpildevand.docx")
    print("OK", build(out))
