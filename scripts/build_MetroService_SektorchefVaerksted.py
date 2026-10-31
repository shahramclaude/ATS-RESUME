# -*- coding: utf-8 -*-
"""
Metro Service A/S — Sektorchef, værkstedet for det rullende materiel (København).
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Sektorchef | Rullende materiel & teknisk vedligeholdelse | København"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = ("Metro Service A/S · att. Rene Sievers · base København · "
             "sendt via Metro Services rekrutteringssystem")
SUBJECT = "Ansøgning: Sektorchef — værkstedet for det rullende materiel"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Hver dag skal det nødvendige antal tog være klar til drift i morgen- og "
    "eftermiddagsmyldretiden — og det krav afgøres af, hvor godt værkstedet planlægger forebyggende "
    "og akut vedligeholdelse, og af hvor hurtigt fire førstelinjeledere og ca. 40 teknikere kan "
    "flytte kapacitet, når forudsætningerne ændrer sig klokken halvotte.",

    "Nedenfor er min læsning af stillingen og det system, der står klar fra første dag: "
    "kapacitetsmodel pr. uge, prioriteringsnøgle for forebyggende og akut arbejde, tavlemøder med "
    "førstelinjelederne, afvigelseslog med ejer og frist, kompetencekort og en fast ledelseskadence "
    "— så struktur og retning ikke afhænger af, hvem der er på vagt.",
]

BULLETS = [
    ("Kravet: effektiv planlægning af forebyggende og akut vedligeholdelse",
     "Løsningen er en fast planlægningsrytme: forebyggende arbejde lagt ud på uger og måneder, akut "
     "arbejde ind i samme kapacitetsmodel og en prioriteringsnøgle — sikkerhed, driftsklarhed, "
     "planlagt vedligeholdelse, udvikling — som alle fire førstelinjeledere bruger ens. Jeg har "
     "drevet 24/7-drift med SAP og nul uplanlagte stop i fem år."),

    ("Kravet: efterlevelse af sikkerhedskrav, procedurer og dokumentationskrav",
     "Løsningen er at gøre sikkerhed til en fast dagsordenspost: LOTO og arbejdstilladelser før "
     "arbejdet begynder, sikkerhedsrunder med fast kadence, nærved-hændelser rapporteret uden skyld "
     "og en afvigelsesliste, hvor hver post har ejer og frist, til den er lukket. Under GMP/FDA/EMA "
     "leverede jeg 37 projekter uden kritiske fund."),

    ("Kravet: lede, støtte og udvikle førstelinjelederne i det daglige",
     "Løsningen er en fast en-til-en-kadence med hver førstelinjeleder: forventningsaftale med tre "
     "til fire målbare punkter, opfølgning, og et rum hvor problemer kommer op, før de bliver "
     "hændelser. Ærligt: jeg har ikke haft fire formelle mellemledere under mig, men ledet 14-mands "
     "teams og 5 elektrikere med personaleansvar."),

    ("Kravet: opfølgning på bemanding, budgetter, leverandører og resultater",
     "Løsningen er et månedligt opfølgningshjul: bemanding og overarbejde, budget i SAP, "
     "leverandørernes leveringsevne og responstid samt tre til fem KPI'er for gennemført "
     "vedligeholdelse og gentagne fejl — med én forbedringssag pr. måned med ejer og slutdato. Jeg "
     "har haft fuldt P&L og hentet +40 % produktivitet."),

    ("Kravet: være en synlig leder, der skaber tillid og tager ansvar for beslutninger",
     "Løsningen er at være på værkstedet hver dag: en kort morgenrunde ved tavlen, en fast gåtur hvor "
     "jeg taler med teknikerne og ikke kun med lederne, og beslutninger skrevet ned med begrundelse, "
     "så de kan efterprøves."),

    ("Kravet: teknisk indsigt i komplekse mekaniske eller elektriske systemer",
     "Løsningen er elautoriseret maskinmester (LV/MV/HV) med 20 år i komplekse mekaniske og "
     "elektriske systemer: koblingsanlæg og højspænding, frekvensomformere, motorværn, pumper, køl, "
     "ventilation og CTS/SCADA — nok til at vurdere, om en gentagen fejl er et komponentproblem eller "
     "en procedurefejl, og følge kvalificeret op på resultaterne."),

    ("Kravet: struktur og retning, når planer ændrer sig med kort varsel",
     "Løsningen er at beslutte på forhånd, hvad der viger: en skreven prioriteringsnøgle, et fast "
     "eskaleringsløb fra tekniker til førstelinjeleder til mig og akutkapacitet, der er reserveret, "
     "før ugen begynder — så et defekt tog ikke spiser den planlagte vedligeholdelse."),

    ("Kravet: stabilitet, kvalitet og engagement gennem overdragelsen i september 2027",
     "Løsningen er at gøre viden og dokumentation til en del af driften nu: kompetencekort med to "
     "personer på hvert kritisk fag, procedurer skrevet ned og prøvet af og en ledelseskadence, der "
     "holder, uanset hvem der ejer kontrakten efter 2027. Jeg har bygget og afviklet organisationer "
     "ved ejerskifte, men ikke en operatøroverdragelse af den her størrelse."),
]

SYSTEM = ("Systemet er allerede bygget: kapacitetsmodel pr. uge med forebyggende og akut arbejde i "
          "samme plan, prioriteringsnøgle og eskaleringsløb, tavlemøde hver morgen, en-til-en-kadence "
          "med hver førstelinjeleder, afvigelseslog med ejer og frist, kompetencekort med to personer "
          "pr. kritisk fag og et månedligt opfølgningshjul for bemanding, budget (SAP) og KPI'er — "
          "opfølgningen genereret i Python og Claude.")

MIRROR = ("Om kravene: 20 år i teknisk drift og vedligeholdelse, heraf fem år som drifts- og "
          "vedligeholdelseschef på et 24/7-anlæg med nul uplanlagte stop og SAP som styresystem; otte "
          "år med personaleansvar og P&L; 37 anlægsprojekter uden kritiske fund. Elautoriseret "
          "maskinmester (LV/MV/HV), B.Tech i Technology Management & Mechanical Engineering, Lean i "
          "daglig brug.")

HONEST = ("Tre ting skal siges ligeud: jeg kommer ikke fra transportbranchen og har ikke arbejdet med "
          "rullende materiel — mine anlæg er forsyning, pharma og installation, hvor kravene til "
          "oppetid og dokumentation er de samme. Jeg har ikke ledet fire formelle førstelinjeledere, "
          "men 14-mands teams. Og jeg har ikke prøvet en operatøroverdragelse som jeres.")

CULTURE = ("Hvorfor Metro Service: jeres opgave er ikke at levere et produkt, men at gøre byen mobil "
           "hver dag — og det er den slags drift, hvor \"godt nok\" bliver opdaget af passagererne. I "
           "beskriver et professionelt lederteam med fokus på samarbejde, sikkerhed og kvalitet, et "
           "fagligt miljø med engagerede specialister og fokus på trivsel — netop den kombination, "
           "jeg selv har skullet holde oppe i pressede perioder.")

PRACTICAL = ("Praktisk: bosat i Måløv, 25 minutter til base København; kørekort B og bil. Dansk på "
             "modersmålsniveau og engelsk professionelt. Straffeattest uploades inden første samtale, "
             "som I beder om. Kan tiltræde efter aftale.")

CLOSING = ("I første samtale vil jeg gerne høre, hvad der i dag er den største flaskehals for at have "
           "togene klar til myldretid.")

# ------------------------------------------------------------------ CV
PROFILE = ("Stillingen kræver tre ting: en leder der kan lede gennem fire førstelinjeledere og skabe "
           "trivsel og ansvar, en planlægger der kan holde forebyggende og akut vedligeholdelse i "
           "samme kapacitetsmodel, og en teknisk person der kan stille kvalificerede spørgsmål til "
           "komplekse mekaniske og elektriske systemer. Tyve år i teknisk drift og vedligeholdelse, "
           "heraf fem år som drifts- og vedligeholdelseschef på et 24/7-forsyningsanlæg med nul "
           "uplanlagte stop, SAP og højspænding; 37 anlægsprojekter uden kritiske fund; 14-mands "
           "produktions- og montageteam og 11 samtidige entrepriser; fuldt P&L med 5 elektrikere og "
           "3 lærlinge. Elautoriseret maskinmester (LV/MV/HV), Lean og SAP i daglig brug.")

PRACTICE = [
    ("Forebyggende og akut vedligeholdelse",
     "Vedligeholdelsesplanlægning i rullerende uger og måneder, akut arbejde ind i samme "
     "kapacitetsmodel, og reserveret akutkapacitet, der er besluttet før ugen begynder."),
    ("Kapacitetsstyring og prioritering",
     "Kapacitet pr. uge målt på timer, kompetencer og reservedele; skreven prioriteringsnøgle — "
     "sikkerhed, driftsklarhed, planlagt vedligeholdelse, udvikling — brugt ens af alle ledere."),
    ("Sikkerhed og dokumentation",
     "LOTO og arbejdstilladelser før arbejdet starter, sikkerhedsrunder med fast kadence, "
     "nærved-hændelser uden skyld; dokumentation og sporbarhed som en del af arbejdet (GMP/FDA/EMA)."),
    ("Kvalitet, hændelser og afvigelser",
     "Afvigelseslog med ejer, frist og lukkekriterium; hændelser analyseret med root cause og "
     "gentagne fejl fulgt som KPI — ikke som notat."),
    ("Bemanding og kompetencer",
     "Kompetencekort med to personer pr. kritisk fag, bemandings- og overarbejdsopfølgning, "
     "oplæringsplan og tydelige forventningsaftaler pr. medarbejder og leder."),
    ("Budget, leverandører og resultater",
     "Budgetopfølgning i SAP, leverandørernes leveringsevne og responstid på kontrakt, og tre til "
     "fem KPI'er pr. måned med en forbedringssag, der bliver afsluttet."),
    ("Ledelse og forandring",
     "En-til-en-kadence med målbare forventninger, tavlemøde hver morgen, synlighed på værkstedet "
     "og beslutninger dokumenteret med begrundelse — også når forudsætningerne ændrer sig midt i "
     "ugen."),
]

MODELS = [
    ("Planlægning",
     "Forebyggende og akut vedligeholdelse i én kapacitetsmodel; ugeplan med timer, kompetencer og "
     "reservedele"),
    ("Prioritering",
     "Skreven nøgle: sikkerhed → driftsklarhed → planlagt vedligeholdelse → udvikling; "
     "eskaleringsløb tekniker → førstelinjeleder → sektorchef"),
    ("Hændelser",
     "Log med ejer, frist og lukkekriterium; root cause på gentagne fejl og hændelser gennemgået på "
     "tavlemødet"),
    ("Sikkerhed",
     "LOTO og arbejdstilladelser, sikkerhedsrunder, nærved-hændelser uden skyld og opfølgning på "
     "afvigelser"),
    ("Kompetencer",
     "Kompetencekort med to personer pr. kritisk fag, oplæringsplan og vikardækning ved ferie og "
     "sygdom"),
    ("Økonomi og leverandører",
     "Budget i SAP, overarbejde og bemanding pr. måned, leveringsevne og responstid pr. "
     "leverandør"),
    ("Opfølgning",
     "Tavlemøde hver morgen, en-til-en hver anden uge, månedligt opfølgningshjul med KPI'er; "
     "rapporter genereret med Python og Claude"),
]

ACHIEVEMENTS = [
    ("Nul uplanlagte stop i fem år",
     "24/7-forsyningsanlæg med SCADA, højspænding og koblingsanlæg — planlagt vedligehold, "
     "tilstandskontrol og KPI'er i SAP som fast regime."),
    ("37 anlægsprojekter uden kritiske fund",
     "2–10 mio. kr. hos Novo Nordisk under GMP/FDA/EMA-krav, 25 specialister koordineret og "
     "dokumentation, der bestod revision."),
    ("14-mands team og 11 entrepriser samtidig",
     "kapacitetsplanlægning, daglige tavlemøder og leverancer til aftalt tid i eksisterende "
     "byggeri med drift og brugere omkring os."),
    ("40+ serviceanlæg med fuldt P&L",
     "egen virksomhed med 5 elektrikere og 3 lærlinge: budgetter, leverandøraftaler, kunder og "
     "ansvar for bundlinjen."),
    ("+40 % produktivitet og −40 % energikost",
     "Lean-værktøjer, standardarbejde og dataunderstøttet planlægning med dokumenteret effekt."),
]

EXPERIENCE = [
    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · vedligehold i SAP",
     [("Planlægning og kapacitet",
       "forebyggende vedligeholdelse planlagt i rullerende uger, akut arbejde prioriteret ind i "
       "samme kapacitet, reservedele og vikardækning sikret — nul uplanlagte stop i fem år."),
      ("Sikkerhed, kvalitet og leverandører",
       "koordinering af egne teknikere, entreprenører og leverandører; LOTO, arbejdstilladelser, "
       "garantisager og nærved-hændelser fulgt til lukning.")]),

    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og leverandøraftaler",
     [("Personale, drift og økonomi",
       "personaleansvar for 5 elektrikere og 3 lærlinge, oplæring og arbejdsplaner; budgetter, "
       "leverandøraftaler og fuldt ansvar for bundlinjen."),
      ("Teknisk ansvar",
       "dimensionering, fejlfinding og dokumentation på el-, køle- og HVAC-anlæg; opmåling og "
       "løsningsvalg på stedet hos kunden.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister · GMP/FDA/EMA",
     [("Projekt, økonomi og fremdrift",
       "plan og budget pr. projekt, fremdrift og rapportering til styregruppe; 25 specialister "
       "koordineret på tværs af mekanik, el, proces og indkøb."),
      ("Idriftsættelse og dokumentation",
       "kravspecifikation, FAT/SAT, IQ/OQ/PQ og afvigelseshåndtering — aflevering uden kritiske "
       "fund, med dokumentation der bestod revision.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Værksted, produktion og fremdrift",
       "14-personers team med kapacitetsplanlægning, daglige tavlemøder og 11 samtidige entrepriser; "
       "tæt dialog med værkstedet om tolerancer, materialer og fremstillingsrækkefølge.")]),

    ("Elektromekaniker / Produktionsteamleder",
     "ARJ Engineering · Teheran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · skiftplanlægning, materialestyring og lager",
     [("Fremstilling og teknisk problemløsning",
       "skiftplanlægning, materialestyring og målopfølgning; reparation og diagnosticering af "
       "elektriske og mekaniske systemer gennem struktureret root cause-analyse.")]),
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
    ("Køleteknik & klimaanlæg (AMU)",
     "Mercantec · mar. 2021"),
    ("Arbejdsmiljø §16 og sikkerhedsbevidsthed (VI/6-1)",
     "Søfartsstyrelsen · maj 2021"),
    ("Lean — værdistrømsanalyse, standardarbejde, 5S, A3 og Kaizen",
     "Anvendt i drift, produktion og projekter · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og projekter · 2017 – nu"),
]

LANGUAGES = ("Dansk (modersmål, skrift og tale) · Engelsk (professionelt, skrift og tale) · "
             "Persisk/farsi · Kørekort B (kategori B)")

PRACTICAL_CV = ("Bosat i Måløv — 25 minutter til base København; kørekort kategori B og bil, og vant "
                "til at møde tidligt. Dansk på modersmålsniveau og engelsk professionelt. "
                "Straffeattest uploades i karriereprofilen inden første samtale. Kan tiltræde efter "
                "aftale; egen virksomhed afvikles ved ansættelse.")

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Biofos (Lynetten), Novo Nordisk A/S, "
              "Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Førstelinjelederne",
     "En-til-en hver anden uge med forventningsaftale, opfølgning og plads til at bringe problemer "
     "op tidligt; jeg leder gennem dem og tager den svære beslutning, når den ligger mellem "
     "niveauerne."),
    ("Teknikerne og specialisterne i Maintenance",
     "Synlighed på værkstedet hver dag, kompetencekort med to personer pr. kritisk fag og "
     "nærved-hændelser rapporteret uden skyld — faglighed skal kunne bruges, ikke bare beundres."),
    ("Drift, øvrige ledere og operatøren",
     "Fast kadence med driftsledelsen om, hvad der skal være klar hvornår, og en fælles "
     "prioriteringsnøgle — så værkstedet og driften trækker i samme retning, også når planen "
     "ændrer sig med kort varsel."),
]

FIRST90 = [
    ("Uge 1–2",
     "Gået værkstedet igennem og talt med alle fire førstelinjeledere og så mange teknikere som "
     "muligt; læst vedligeholdelsesplan, åbne afvigelser, hændelser det seneste år og "
     "bemandingssituationen; set hvordan myldretidskravet bliver fulgt op i dag."),
    ("Uge 3–6",
     "Egen kapacitetsmodel og prioriteringsnøgle i brug; tavlemøde og en-til-en-kadence etableret; "
     "afvigelseslisten gennemgået post for post med ejer og frist; første sikkerhedsrunde gennemført "
     "med førstelinjelederne."),
    ("Uge 7–12",
     "Månedligt opfølgningshjul på plads med bemanding, budget (SAP), leverandører og tre til fem "
     "KPI'er; kompetencekort over kritiske fag færdigt, så vikardækning er kendt; første "
     "forbedringssag gennemført og effekten målt."),
    ("Måned 3–6",
     "Forebyggende vedligeholdelse gennemført som planlagt og akutarbejde nedbragt; "
     "leverandøropfølgning formaliseret; trivsel og sygefravær fulgt som fast punkt i "
     "ledelseskadencen; forventningsaftaler og udviklingsplaner for alle fire førstelinjeledere."),
    ("Måned 6–12",
     "Stabil drift og dokumenteret kvalitet ind i overdragelsen til den nye operatør i september "
     "2027: procedurer skrevet ned og prøvet af, viden delt med to personer pr. kritisk fag, og et "
     "værksted der kan levere myldretid uden at hænge på enkeltpersoner."),
]

KEYWORDS = (
    "Sektorchef · Rullende materiel · Værksted · Vedligeholdelse · Forebyggende og akut "
    "vedligeholdelse · Vedligeholdelsesplanlægning · Kapacitetsstyring · Kapacitet · Ressourcer · "
    "Prioriteringer · Forudsætninger · Planlægning · Sikkerhedskrav · Procedurer · "
    "Dokumentationskrav · Kvalitet · Hændelser · Afvigelser · Førstelinjeledere · Trivsel · Ansvar · "
    "Bemanding · Budgetter · Leverandører · Resultater · Løbende forbedringer · Processer · Synlig "
    "leder · Tillid · Beslutninger · Performance · Teknisk indsigt · Maskinmester · Ingeniør · "
    "Teknisk håndværksbaggrund · Transportbranchen · Lean · SAP · Personaleledelseskompetencer · "
    "Lede gennem andre ledere · Mekaniske eller elektriske systemer · Komplekse systemer · "
    "Sikkerhedskritiske miljøer · Forandring · Engagement · Tog · Drift · Morgen- og "
    "eftermiddagsmyldretiden · Koordinering · Medarbejdere · Planer · Operatør · September 2027 · "
    "Københavns Metro · Metro Service · Specialister · Maintenance · Struktur og retning · "
    "Kvalificeret opfølgning"
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

    m.para(SYSTEM, after=56, line=228)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=18, line=228)

    m.meta("Med venlig hilsen · Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "LEDELSESPROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("VEDLIGEHOLDELSESSTYRING — ANVENDT I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER VÆRKSTEDET I RYTMEN",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN LEDES VÆRKSTEDET — DE TRE PARTER")
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
                  title="Ansøgning og CV — Sektorchef, værkstedet for det rullende materiel, "
                        "Metro Service A/S",
                  subject="Vedligeholdelse · kapacitetsstyring · sikkerhedskritiske miljøer · "
                          "ledelse af førstelinjeledere · forandring",
                  keywords=("sektorchef, rullende materiel, metro service, vedligeholdelse, "
                            "kapacitetsstyring, førstelinjeledere, sikkerhed, kvalitet, sap, lean, "
                            "maskinmester, dansk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1 (krav → løsning), CV side 2-3, 90 dage side 4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_MetroService_SektorchefVaerksted.docx")
    print("OK", build(out))
