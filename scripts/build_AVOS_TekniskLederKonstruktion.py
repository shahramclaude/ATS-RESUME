# -*- coding: utf-8 -*-
"""
AVOS A/S (ENVATEK) — Teknisk leder / maskiningeniør til konstruktionsafdelingen, Kalundborg.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Teknisk leder | Konstruktion og mekaniske projekter | Kalundborg"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "31. oktober 2026"
RECIPIENT = ("AVOS A/S · Melbygade 15, 4400 Kalundborg · att. adm. dir. Annemarie H. Petersen · "
             "93 39 06 22 · søgt via QuickApply på Jobindex")
SUBJECT = "Ansøgning: Teknisk leder / maskiningeniør til konstruktionsafdelingen"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Opgaven er at lede en konstruktionsafdeling på to personer, der skal kunne vokse — og selv gå ud "
    "på værkstedet, måle op og få tegningen til at passe med den måde, emnet bliver skåret, drejet og "
    "svejst på. Når modellerne går direkte i produktion, er konstruktion ikke teori: en fejl i en 3D-fil "
    "bliver til spildt materiale og en ordre, der kommer for sent.",

    "Nedenfor er min læsning af rollen og det system, der står klar fra første dag: kapacitets- og "
    "ressourceplan for afdelingen, ordreopfølgning med milepæle og ansvarlig, tegnings- og "
    "dokumentationskontrol, risikovurdering og manual som fast del af hvert projekt og en fast kadence "
    "med værkstedet og med kunderne.",
]

BULLETS = [
    ("Kravet: faglig sparring og ledelse af konstruktionsafdelingen",
     "Løsningen er tæt ledelse i en lille afdeling: 1:1 hver fjerde uge, faglig gennemgang af "
     "igangværende konstruktioner og en leder der sidder ved tegningerne sammen med teamet. Jeg har ledet "
     "5, 12 og 14 mand og ved, at faglig troværdighed er adgangsbilletten til at lede specialister."),

    ("Kravet: ressourceplanlægning og bemanding",
     "Løsningen er en kapacitetsplan pr. uge og pr. medarbejder: hvilke ordrer er i hus, hvad kræver "
     "de i konstruktionstimer, og hvornår skal der ansættes. Ambitionen om at vokse bliver en plan med "
     "roller og tidshorisonter — ikke et ønske."),

    ("Kravet: design og konstruktion af mekaniske projekter — 3D-filer, 2D-tegninger, beregninger, "
     "materialer og overfladebehandling",
     "Løsningen er konstruktionsforståelse kombineret med projektgennemførelse: mekanisk uddannelse i "
     "baggrunden, 20 år med komponenter og anlæg og 37 projekter med kravspecifikation, materialevalg og "
     "dokumentation. 3D CAD og FEM er ikke min daglige værktøjskasse i dag — det er en kompetence, jeg "
     "genopbygger i jeres Inventor-miljø fra første uge."),

    ("Kravet: opmåling på værksted og hos kunder samt mobil 3D-scanning",
     "Løsningen er at måle rigtigt første gang: opmåling dokumenteret med fotos og mål, kontrolmåling før "
     "fremstilling og scanning brugt som grundlag for modellen — ikke som efterrationalisering. Jeg har "
     "målt op på eksisterende anlæg, hvor målene var det eneste, der var sikkert."),

    ("Kravet: risikovurderinger og manualer til CE-mærkning",
     "Løsningen er dokumentation, der skrives som en del af konstruktionen og ikke bagefter: "
     "risikovurdering pr. maskine, manual med drift og vedligeholdelse og en dokumentpakke, der kan "
     "stilles frem ved en revision — jeg har leveret den slags under GMP/FDA/EMA-krav uden kritiske fund."),

    ("Kravet: ordreopfølgning og kundekontakt i projekter inden for offshore, pharma, fødevarer og "
     "vandindustrien",
     "Løsningen er én ordreoversigt med milepæle, ejer og næste handling, og en kundekontakt hvor "
     "afvigelser bliver meldt, før kunden opdager dem — i 20 år har jeg haft de samtaler med "
     "industrikunder og myndigheder."),

    ("Kravet: digital styrke, struktur i en travl hverdag og samarbejde på tværs af koncernen",
     "Løsningen er værktøjer, der bliver brugt: ordre- og kapacitetsoversigt i Excel og Power BI, "
     "automatiseret rapportering bygget med Python og Claude, og en fast mødekadence med "
     "søsterselskaberne, så en kapacitetstoppe i Kalundborg kan løftes af kolleger i koncernen i "
     "stedet for at blive et nej til kunden."),
]

SYSTEM = ("Systemet er allerede bygget: kapacitets- og ressourceplan pr. uge, ordreoversigt med "
          "milepæle og ansvarlig, tegnings- og dokumentationskontrol med version og ejer, "
          "risikovurderings- og manualskabelon til CE, kontrolmåling før fremstilling og KPI'er for "
          "levering til tiden — i Excel, Power BI og CAD/PDM-miljøet, med Python og Claude til "
          "rapportering.")

MIRROR = ("Om kravene: 20 år med mekaniske og elektriske anlæg, projekter og ledelse — 37 "
          "anlægsprojekter (2–10 mio. kr.) med 25 specialister koordineret, 14- og 12-mands teams, 5 "
          "elektrikere og 3 lærlinge med fuldt P&L og 24/7-drift med nul uplanlagte stop i fem år; "
          "elautoriseret maskinmester (LV/MV/HV), B.Tech i Technology Management & Mechanical "
          "Engineering og el-ingeniør. Dansk og engelsk på arbejdsniveau.")

HONEST = ("To ting skal siges ligeud: jeg er ikke uddannet diplomingeniør i maskinteknik — min vej er "
          "elautoriseret maskinmester med B.Tech i Technology Management & Mechanical Engineering og en "
          "el-ingeniøruddannelse — og 3D CAD og FEM har ikke været min daglige værktøjskasse de seneste "
          "år. Til gengæld kommer jeg med projektgennemførelse, dokumentation der holder til CE og "
          "revision, og respekt for hvad værkstedet kan fremstille.")

CULTURE = ("Hvorfor AVOS: I har lavet mekanik siden 1853, og I skriver selv, at dokumentation og "
           "kvalitetssikring er en naturlig del af hverdagen. Det er den kobling, jeg trives i: "
           "konstruktion der bliver til noget i virkeligheden, og korte beslutningsveje, så en fejl kan "
           "rettes samme dag, den bliver opdaget.")

PRACTICAL = ("Praktisk: bosat i Måløv — cirka en time til Kalundborg, en pendling jeg har kørt i to år; "
             "kørekort B og bil; dansk på modersmålsniveau og engelsk professionelt; kan tiltræde "
             "hurtigst muligt, og egen virksomhed afvikles ved ansættelse.")

CLOSING = ("Jeg vil gerne se værkstedet og de igangværende konstruktioner og bruge første samtale på to "
           "spørgsmål: hvordan afdelingen prioriterer mellem kundeordrer og udvikling, og hvordan "
           "3D-modellerne bruges videre i produktionen i dag.")

# ------------------------------------------------------------------ CV
PROFILE = ("Rollen kræver tre ting på én gang: en leder der kan sparre fagligt med en konstruktør, en "
           "projektleder der får ordrerne ud af døren til tiden, og en person der kan gøre "
           "dokumentation og CE-arbejde til en fast del af projektet. Alle tre har været hverdag i 20 "
           "år: 37 anlægsprojekter (2–10 mio. kr.) med 25 specialister koordineret under GMP/FDA/EMA-krav "
           "og nul kritiske fund, 14- og 12-mands teams i produktion og montage, 5 elektrikere og 3 "
           "lærlinge med fuldt P&L og 24/7-drift med nul uplanlagte stop i fem år. Elautoriseret "
           "maskinmester (LV/MV/HV), B.Tech i Technology Management & Mechanical Engineering og "
           "el-ingeniør.")

PRACTICE = [
    ("Ledelse og faglig sparring",
     "1:1-hjul, MUS med opfølgning, faglig gennemgang af igangværende konstruktioner, rolleafklaring og "
     "delegering med opfølgning; situationsbestemt ledelse (SLII)."),
    ("Projekt og ordre",
     "Faseopdelt projektmodel med milepæle, budget og afvigelsesliste med ejer og frist; "
     "ordreopfølgning med næste handling og levering til tiden som styringstal."),
    ("Ressource og bemanding",
     "Kapacitetsplan pr. uge og medarbejder, timer pr. ordre mod kalkule, prioritering mellem ordrer og "
     "en bemandingsplan for vækst med roller og tidshorisonter."),
    ("Dokumentation og CE",
     "Risikovurdering pr. maskine, manual med drift og vedligeholdelse, kravspecifikation og "
     "acceptkriterier; FAT/SAT, IQ/OQ/PQ og revisionsparat dokumentstyring med version og ejer."),
    ("Konstruktion og mekanik",
     "Mekaniske og elektriske komponenter, opmåling på eksisterende anlæg, materiale- og "
     "komponentspecifikation i dialog med værksted og leverandører, tolerancer og fremstillingshensyn."),
    ("Kunder og koncern",
     "Kontakt med industri- og forsyningskunder, myndigheder og leverandører; koordinering på tværs af "
     "søsterselskaber, når kapacitet eller kompetence skal findes uden for huset."),
    ("Digitalt",
     "Excel og Power BI til ordre og kapacitet, SAP/CMMS, rapportering og analyser bygget med Python og "
     "Claude; hurtig indlæring af nye systemer — det er en del af måden, jeg arbejder på."),
]

MODELS = [
    ("Projekt og ordre",
     "Faseopdelt model med milepæle, budget pr. leverance, afvigelsesliste med ejer og frist, "
     "ordreoversigt med næste handling"),
    ("Ressource",
     "Kapacitetsplan pr. uge og medarbejder, timer pr. ordre mod kalkule, bemandingsplan med roller "
     "og tidshorisonter"),
    ("Konstruktion og kontrol",
     "Opmåling dokumenteret med fotos og mål, kontrolmåling før fremstilling, tegnings- og "
     "dokumentationskontrol med version og ejer"),
    ("CE og dokumentation",
     "Risikovurdering pr. maskine, manual med drift og vedligeholdelse, kravspecifikation og "
     "acceptkriterier, revisionsparat dokumentpakke"),
    ("Kvalitet",
     "Egenkontrol, afvigelser med root cause, A3 og PDCA, levering til tiden og kassation som "
     "styringstal"),
    ("Ledelse",
     "1:1-hjul, MUS/GRUS, faglig gennemgang, SLII og coaching efter GROW"),
    ("Værktøjer",
     "Excel og Power BI, PDM/CAD-miljø, SAP/CMMS, Python og Claude til rapportering og analyse"),
]

ACHIEVEMENTS = [
    ("Nul kritiske fund ved aflevering",
     "37 anlægsprojekter hos Novo Nordisk, 2–10 mio. kr., under GMP/FDA/EMA-krav — kravspecifikation, "
     "FAT/SAT, IQ/OQ/PQ og dokumentation uden fund."),
    ("25 specialister koordineret",
     "på tværs af mekanik, el, proces og indkøb i 37 samtidige projekter med plan, økonomi og "
     "rapportering."),
    ("14- og 12-mands teams ledet",
     "kapacitetsplanlægning, flowstyring og daglige tavlemøder i produktion og montage — med "
     "leverancer til aftalt tid."),
    ("5 elektrikere og 3 lærlinge med fuldt P&L",
     "daglig ledelse, kompetenceudvikling, kunde- og leverandørdialog og ansvar for bundlinjen i egen "
     "virksomhed."),
    ("+40 % produktivitet og −40 % energikost",
     "dokumenterede forbedringer via måling, standardarbejde, dataunderstøttet planlægning og egen "
     "AI-tooling."),
]

EXPERIENCE = [
    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister · GMP/FDA/EMA",
     [("Projekt, økonomi og ordre",
       "plan og budget pr. projekt, fremdrift og rapportering til styregruppe; 25 specialister "
       "koordineret på tværs af mekanik, el, proces og indkøb."),
      ("Dokumentation og aflevering",
       "kravspecifikation, FAT/SAT, IQ/OQ/PQ og valideringsdokumentation med afvigelseshåndtering — "
       "nul kritiske fund ved aflevering.")]),

    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og leverandøraftaler",
     [("Kunder, tilbud og økonomi",
       "tilbudsberegning, indkøb og leverandøraftaler, plan og prognose med fuldt ansvar for "
       "bundlinjen."),
      ("Teknisk ansvar",
       "dimensionering, fejlfinding og dokumentation på el- og HVAC-anlæg; opmåling og "
       "løsningsvalg på stedet hos kunden.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Produktion, fremdrift og samspil med værkstedet",
       "14-personers team med kapacitetsplanlægning, daglige tavlemøder og 11 samtidige entrepriser; "
       "tæt dialog med værkstedet om tolerancer, materialer og fremstillingsrækkefølge.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · budgetter i SAP",
     [("Anlæg, opmåling og dokumentation",
       "tilstandsvurdering og opmåling på eksisterende anlæg, reservedele og ændringer dokumenteret; "
       "nul uplanlagte stop i fem år."),
      ("Leverandører og sikkerhed",
       "koordinering af egne teknikere, entreprenører og leverandører — LOTO, arbejdstilladelser, "
       "garantisager og nærved-hændelser.")]),

    ("Elektromekaniker / Produktionsteamleder",
     "ARJ Engineering · Teheran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · skiftplanlægning, materialestyring og lager",
     [("Fremstilling og teknisk problemløsning",
       "skiftplanlægning, materialestyring og målopfølgning; reparation og diagnosticering af "
       "elektriske og mekaniske systemer gennem struktureret root cause-analyse.")]),
]

EDUCATION = [
    ("B.Tech (EQF niveau 6) — Technology Management & Mechanical Engineering",
     "Maskinmesterskolen / Copenhagen School of Marine Engineering & Technology Management · 2017 – "
     "2022 · karakter 7,6/12"),
    ("Elektrisk & mekanisk design, el-ingeniør (EQF niveau 6)",
     "Tehran Technical University · 2000 – 2003 · herunder CAD og konstruktionstegning"),
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
     "Anvendt i drift og produktion · 2017 – nu"),
]

LANGUAGES = ("Dansk (modersmål, skrift og tale) · Engelsk (professionelt, skrift og tale) · "
             "Persisk/farsi · Kørekort B (kategori B)")

PRACTICAL_CV = ("Bosat i Måløv — cirka en time til AVOS i Kalundborg; har pendlet til Kalundborg i to år; "
                "kørekort kategori B og bil; dansk på modersmålsniveau og engelsk professionelt i skrift "
                "og tale; kan tiltræde hurtigst muligt; egen virksomhed afvikles ved ansættelse.")

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Novo Nordisk A/S (Kalundborg), Biofos "
              "(Lynetten), Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Konstruktøren og værkstedet",
     "Faglig gennemgang før tegningen låses, kontrolmål før fremstilling og en fast dialog med "
     "værkføreren om tolerancer og rækkefølge — så konstruktionen passer med den måde, emnet bliver "
     "skåret og svejst på."),
    ("Kunderne",
     "Én kontakt med aftalt svartid, milepæle der bliver meldt, og afvigelser der kommer fra os, før "
     "kunden opdager dem."),
    ("Koncernen",
     "Fast kadence med ENVATEK-selskaberne om kapacitet og kompetencer, så opgaver kan løftes i "
     "fællesskab i stedet for at blive sendt videre som et nej."),
]

FIRST90 = [
    ("Uge 1–2",
     "Gået værkstedet igennem og set, hvordan modellerne bliver brugt i skæring, drejning og svejsning; "
     "gennemgået igangværende ordrer, tegningsgrundlag og dokumentationspraksis. Mødt konstruktøren, "
     "værkføreren og ledelsen."),
    ("Uge 3–6",
     "Ordreoversigt med milepæle og ansvarlig lagt; kapacitetsplan pr. uge etableret; 1:1 og faglig "
     "gennemgang i gang; opmålings- og kontrolmålingsrutine aftalt med værkstedet."),
    ("Uge 7–12",
     "Risikovurderings- og manualskabelon taget i brug på nye ordrer; tegnings- og dokumentationskontrol "
     "med version og ejer indført; første egne konstruktioner leveret til produktion."),
    ("Måned 3–6",
     "Bemandingsplan for vækst lagt med roller og tidshorisonter; levering til tiden målt og forbedret; "
     "CAD- og beregningskompetence genopbygget i jeres systemer, så jeg selv kan løfte opgaverne."),
    ("Måned 6–12",
     "Afdelingen leverer flere ordrer med samme bemanding, dokumentationen er revisionsklar, og "
     "samarbejdet med koncernselskaberne er blevet en fast kapacitetsreserve. Løbende: månedlig "
     "gennemgang af ordrer, timer og levering til tiden."),
]

KEYWORDS = (
    "Teknisk leder · Maskiningeniør · Konstruktionsafdeling · Konstruktør · Konstruktion · Mekaniske "
    "projekter · 3D-filer · 2D-tegninger · Inventor · Opmåling · Maskinkomponenter · Beregning · "
    "Styrkeberegning · FEM · Materialer · Overfladebehandling · 3D-scanning · Risikovurderinger · "
    "Manualer · CE-mærkning · Ordreopfølgning · Ressourceplanlægning · Bemanding · Faglig sparring · "
    "Personaleledelse · Kundekontakt · Tværfagligt samarbejde · Dansk · Engelsk · Digital · Struktureret · "
    "Beslutningsveje · Projektledelse · Kvalitetssikring · Dokumentation · Offshore · Pharma · Fødevarer · "
    "Vandindustrien · ENVATEK · Kalundborg · Måløv"
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

    m.models_table("KONSTRUKTIONS- OG PROJEKTMETODER — ANVENDT I PRAKSIS",
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
                  title="Ansøgning og CV — Teknisk leder / maskiningeniør, AVOS A/S",
                  subject="Konstruktion · mekaniske projekter · CE-dokumentation · ressourceplanlægning",
                  keywords=("teknisk leder, maskiningeniør, konstruktionsafdeling, konstruktion, "
                            "inventor, ce-mærkning, ordreopfølgning, kalundborg, avos, dansk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1 (krav → løsning), CV side 2-3, 90 dage side 4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_AVOS_TekniskLederKonstruktion.docx")
    print("OK", build(out))
