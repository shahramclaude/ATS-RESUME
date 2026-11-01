# -*- coding: utf-8 -*-
"""
CTR I/S — Chef for Plan & Projekt (Frederiksberg).
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Chef for Plan & Projekt | Fjernvarme, projektportefølje og drift"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = ("CTR I/S · Stæhr Johansens Vej 38, 2000 Frederiksberg · "
             "att. adm. direktør Randi Skogstad")
SUBJECT = "Ansøgning: Chef for Plan & Projekt"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Plan & Projekt skal kunne to ting på samme tid: modne de projekter, der endnu ikke findes, i "
    "dialog med fem ejerkommuner — og gennemføre dem, der er besluttet, på tid, økonomi og kvalitet. "
    "Det er ikke en projektstyringsopgave alene, men en ledelsesopgave: fem medarbejdere med "
    "forskellige fagligheder skal have klare roller og beslutningsgange, og direktionen skal kunne "
    "beslutte på et grundlag, der holder.",

    "Nedenfor er min læsning af stillingen og det system, der står klar fra første dag: projektmodel "
    "med faseporte fra idé til idriftsættelse, porteføljeoversigt med prioritering og kapacitet, "
    "forudsætningslog for plan- og energimodellerne, snitfladematrix mod Kontrakt & Strategi, Driften "
    "og Vedligehold samt et beslutningsoplæg på én side til direktionen.",
]

BULLETS = [
    ("Kravet: personaleledelse af projektledere, planlæggere og faglige specialister",
     "Løsningen er en fast kadence pr. medarbejder: forventningsaftale med målbare punkter, faglig "
     "sparring og en tydelig prioritering. Jeg har ledet 14-mands team og 5 elektrikere med "
     "personaleansvar og koordineret 25 specialister på tværs af fag — faglige specialister skal "
     "ikke styres, men have rammer og modspil."),

    ("Kravet: strategisk planlægning, projektmodning og prioritering af en projektportefølje",
     "Løsningen er at gøre porteføljen synlig og beslutningsparat: hvert initiativ får en fase, en "
     "modenhedsvurdering, et økonomisk spænd og en næste beslutning med dato — gennemgået som fast "
     "punkt, ikke som årlig øvelse. Jeg har kørt 37 samtidige anlægsprojekter og 11 entrepriser og "
     "ved, hvad der sker, når prioritering ikke er besluttet på forhånd."),

    ("Kravet: bygherrerollen samt styring af økonomi, risici, rådgivere og leverandører",
     "Løsningen er at styre på kalkule og forudsætninger: budget, prognose og risikopost pr. projekt, "
     "rådgiver- og leverandørvalg på dokumenteret leverance, og ændringer prissat, før de bliver "
     "merforbrug. Jeg har været leverandørpart i bygherreprojekter i 20 år og haft fuldt P&L — men "
     "har ikke selv siddet som formel bygherre med AB/ABT-kontraktansvar, og den del skal læses "
     "grundigt."),

    ("Kravet: udvikling af projektstyring, beslutningsprocesser og organisatoriske samarbejdsflader",
     "Løsningen er at oversætte CTR's projektmodel til noget, der kan bruges om mandagen: hvem "
     "beslutter hvad, på hvilket grundlag, hvornår, og hvad der sker, hvis beslutningen udskydes. "
     "Roller og beslutningspunkter bliver skrevet ned, prøvet af på et rigtigt projekt og justeret."),

    ("Kravet: systemejerskab for plan- og energimodeller, EnergyPRO, plangrundlag og effektbalance",
     "Løsningen er governance før beregninger: en forudsætningslog hvor hver antagelse har ejer, "
     "kilde og dato, en fast ændringsprocedure og en tydelig bestillingsvej for analyser — så samme "
     "sag ikke får to svar. Jeg har ikke arbejdet med EnergyPRO; forudsætningsstyring har jeg fra "
     "driftsdata, SCADA og teknisk økonomi, og værktøjet lærer jeg."),

    ("Kravet: samarbejde med ejerkommunerne og politisk forståelse",
     "Løsningen er at komme tidligt og med ét grundlag: lokal påvirkning, kapacitetsbehov, "
     "forsyningssikkerhed og økonomi i samme notat og en fast kadence pr. kommune, så dialogen "
     "handler om valg frem for om fakta. Jeg har ikke arbejdet i en politisk styret organisation, men "
     "i 20 år gjort tekniske valg forståelige for kunder og myndigheder."),

    ("Kravet: tydelige snitflader til Kontrakt & Strategi, Driften og Vedligehold — og overlevering "
     "til drift",
     "Løsningen er en snitfladematrix: hvem leverer hvad til hvem, hvornår, og hvad der er "
     "bestillerkompetence contra udførelse. Overlevering til drift bliver et krav i projektplanen fra "
     "dag ét — dokumentation, test og kompetenceoverførsel — ikke noget, der opdages i "
     "idriftsættelsen."),

    ("Kravet: styre eksterne rådgivere og leverandører og afklare, hvilke kompetencer CTR selv skal "
     "råde over",
     "Løsningen er en kompetenceoversigt over husets kernekompetencer og en regel for, hvornår der "
     "købes eksternt: bestillerkompetence bliver i huset, også når opgaven sourcet ud. Jeg har selv "
     "været den eksterne part og ved, hvad en bygherre skal kunne for at få det bestilte."),

]

SYSTEM = ("Systemet er allerede bygget: projektmodel med faseporte fra idé til idriftsættelse, "
          "porteføljeoversigt med modenhed, kapacitet og næste beslutning, forudsætningslog for "
          "plan- og energimodellerne med ejer, kilde og dato, snitfladematrix mod Kontrakt & "
          "Strategi, Driften og Vedligehold og et beslutningsoplæg på én side til direktionen — med "
          "rapporter genereret i Python og Claude.")

MIRROR = ("Om kravene: 20 år i tekniske anlæg — 37 samtidige anlægsprojekter med 25 "
          "specialister og nul kritiske fund, 11 entrepriser med 14-mands team, fem år som drifts- og "
          "vedligeholdelseschef på et 24/7-anlæg med nul uplanlagte stop og fuldt P&L med 40+ "
          "serviceanlæg. Elautoriseret maskinmester (LV/MV/HV) og B.Tech.")

HONEST = ("Tre ting skal siges ligeud: jeg har ikke været formel bygherre med AB/ABT-kontraktansvar — "
          "jeg har siddet på leverandørsiden og styret egen virksomheds kontrakter. Jeg har ikke "
          "arbejdet politisk styret, og EnergyPRO har jeg ikke brugt. Til gengæld kommer jeg med "
          "teknisk indsigt i forsyningsanlæg, dokumenteret projekt- og økonomistyring og erfaring med "
          "at gøre driftskrav gældende, før anlægget er bygget.")

CULTURE = ("Hvorfor CTR: knap 50 medarbejdere, 96 procent medarbejdertilfredshed og kort vej fra idé "
           "til beslutning — den type organisation, hvor en afdelingschef kan skabe forandring uden at "
           "vente på et koncernsekretariat. Og opgaven er ægte: forsyningssikkerhed og varmepris for "
           "340.000 hjem under en portefølje i forandring.")

PRACTICAL = ("Praktisk: bosat i Måløv, 25 minutter til Frederiksberg. Dansk på modersmålsniveau og "
             "engelsk professionelt. Kan tiltræde 1. januar 2027; egen virksomhed afvikles ved "
             "ansættelse. CV er uden billede, som I beder om.")

CLOSING = ("I første samtale vil jeg gerne høre, hvordan I i dag afgør, hvornår et projekt er modent "
           "nok til at blive besluttet.")

# ------------------------------------------------------------------ CV
PROFILE = ("Stillingen kræver en leder, der både kan modne en projektportefølje og gennemføre den: "
           "personaleledelse af faglige specialister, bygherrestyring af økonomi, risici, rådgivere "
           "og leverandører, og et system der gør beslutningsgrundlaget tydeligt for direktion og "
           "bestyrelse. Tyve år i tekniske anlæg: 37 samtidige anlægsprojekter (2–10 mio. kr.) med "
           "25 specialister koordineret og nul kritiske fund, 11 entrepriser med 14-mands team, fem "
           "år som drifts- og vedligeholdelseschef på et 24/7-forsyningsanlæg med nul uplanlagte "
           "stop, og fuldt P&L med 40+ serviceanlæg i egen virksomhed. Elautoriseret maskinmester "
           "(LV/MV/HV), B.Tech i Technology Management & Mechanical Engineering og el-ingeniør.")

PRACTICE = [
    ("Portefølje og prioritering",
     "Porteføljeoversigt med fase, modenhed, økonomisk spænd og næste beslutning med dato; "
     "kapacitet pr. projektleder gjort synlig, så prioritering er en beslutning og ikke en "
     "konsekvens."),
    ("Projektmodning",
     "Modenhedstjek før beslutning: kapacitetsbehov, tekniske muligheder, økonomi, risici og lokale "
     "hensyn belyst i samme grundlag — med tydeligt krav til, hvad der mangler."),
    ("Bygherrestyring",
     "Kalkule, budget og prognose; risikopost med ejer; rådgiver- og leverandørvalg på kompetence "
     "og dokumenteret leverance; ændringer prissat før udførelse."),
    ("Projektmodel og beslutningspunkter",
     "Faseporte fra idé til idriftsættelse med roller, ansvar og beslutningspunkter; prøvet af på et "
     "rigtigt projekt og justeret, så den fungerer i hverdagen."),
    ("Snitflader",
     "Matrix mod Kontrakt & Strategi, Driften og Vedligehold: bestilling, leverance, beslutning og "
     "overlevering — med overlevering til drift som krav fra dag ét."),
    ("Forudsætninger og beregninger",
     "Forudsætningslog med ejer, kilde og dato for plan- og energimodeller; ændringsprocedure og "
     "bestillingsvej for analyser, så samme sag ikke får to svar."),
    ("Ledelse og kompetencer",
     "Forventningsaftaler og faglig sparring pr. medarbejder; kompetenceoversigt over husets "
     "kernekompetencer og en regel for, hvornår der købes eksternt."),
]

MODELS = [
    ("Portefølje",
     "Fase, modenhed, økonomisk spænd, risici og næste beslutning med dato; gennemgang som fast "
     "punkt"),
    ("Modenhed",
     "Tjekliste før beslutning: kapacitetsbehov, teknik, økonomi, risici og lokal påvirkning "
     "belyst samlet"),
    ("Økonomi",
     "Kalkule, budget og prognose pr. projekt; risikopost med ejer og ændringssager prissat før "
     "udførelse"),
    ("Beslutningsoplæg",
     "Én side til direktion og bestyrelse: sag, alternativer, økonomi, risiko og anbefaling med "
     "forbehold"),
    ("Snitflader",
     "Matrix mod Kontrakt & Strategi, Driften og Vedligehold; overlevering til drift som "
     "leverancekrav"),
    ("Forudsætninger",
     "Log med ejer, kilde og versionsdato for plan- og energimodeller; ændring kræver "
     "godkendelse og ny beregning"),
    ("Rapportering",
     "Portefølje- og fremdriftsrapport genereret i Python og Claude i stedet for samlet i hånden — "
     "samme tal til alle"),
]

ACHIEVEMENTS = [
    ("37 anlægsprojekter uden kritiske fund",
     "2–10 mio. kr. hos Novo Nordisk med 25 specialister koordineret, plan og budget pr. projekt, "
     "FAT/SAT, IQ/OQ/PQ og aflevering under GMP/FDA/EMA-krav."),
    ("Nul uplanlagte stop i fem år",
     "24/7-forsyningsanlæg med SCADA, højspænding og koblingsanlæg — vedligehold planlagt i "
     "rullerende uger og KPI'er fulgt i SAP."),
    ("11 entrepriser og 14-mands team samtidig",
     "kapacitetsplanlægning, daglige tavlemøder og leverancer til aftalt tid i eksisterende byggeri "
     "med drift og brugere omkring os."),
    ("Fuldt P&L med 40+ serviceanlæg",
     "egen virksomhed med 5 elektrikere og 3 lærlinge: tilbud, indkøb, leverandøraftaler, budget og "
     "ansvar for bundlinjen."),
    ("+40 % produktivitet og −40 % energikost",
     "dokumenterede forbedringer gennem standardarbejde, Lean-værktøjer og dataunderstøttet "
     "planlægning."),
]

EXPERIENCE = [
    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister · GMP/FDA/EMA",
     [("Projekt, økonomi og fremdrift",
       "plan og budget pr. projekt, fremdrift og rapportering til styregruppe; 25 specialister "
       "koordineret på tværs af mekanik, el, proces og indkøb."),
      ("Aflevering og dokumentation",
       "kravspecifikation, FAT/SAT, IQ/OQ/PQ og afvigelseshåndtering — aflevering uden kritiske "
       "fund, med dokumentation der bestod revision.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · budgetter i SAP",
     [("Drift, vedligehold og anlægsforståelse",
       "planlagt vedligehold, tilstandskontrol og KPI'er i SAP; nul uplanlagte stop i fem år."),
      ("Sikkerhed og leverandører",
       "koordinering af egne teknikere, entreprenører og rådgivere — LOTO, arbejdstilladelser, "
       "garantisager og nærved-hændelser fulgt til lukning.")]),

    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og leverandøraftaler",
     [("Økonomi, kunder og kontrakter",
       "tilbudsberegning, indkøb og leverandøraftaler, plan og prognose med fuldt ansvar for "
       "bundlinjen; ændringssager prissat, før arbejdet blev udført."),
      ("Personale og fagligt ansvar",
       "daglig arbejdsplanlægning med 5 elektrikere og 3 lærlinge, oplæring og faglig "
       "kvalitetssikring, før arbejdet blev afleveret.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Team, kapacitet og fremdrift",
       "14-personers team med kapacitetsplanlægning, daglige tavlemøder og 11 samtidige entrepriser; "
       "montage i eksisterende byggeri med hensyn til drift og brugere.")]),

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

PRACTICAL_CV = ("Bosat i Måløv — cirka 25 minutter til Stæhr Johansens Vej på Frederiksberg og tæt på "
                "metroen; kørekort kategori B og bil. Dansk på modersmålsniveau og engelsk "
                "professionelt. Forventet tiltrædelse 1. januar 2027 passer; egen virksomhed afvikles "
                "ved ansættelse. Dokumentet er uden billede, som CTR beder om.")

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Novo Nordisk A/S, Biofos (Lynetten), "
              "Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Direktionen og bestyrelsen",
     "Beslutningsoplæg på én side med sag, alternativer, økonomi, risiko og anbefaling — og en "
     "porteføljeoversigt, der bliver gennemgået fast, så beslutninger ikke udskydes i mangel af "
     "grundlag."),
    ("Ejerkommunerne",
     "Fast kadence pr. kommune og ét fælles grundlag pr. sag: kapacitetsbehov, lokal påvirkning, "
     "forsyningssikkerhed og økonomi — så dialogen handler om valg frem for om fakta."),
    ("Kontrakt & Strategi, Driften og Vedligehold",
     "Snitfladematrix med bestilling, leverance og beslutningsret; driftskrav og "
     "asset-tilstand taget ind i projektmodningen, og overlevering til drift som leverancekrav fra "
     "dag ét."),
]

FIRST90 = [
    ("Uge 1–2",
     "Læst hele porteføljen igennem: igangværende projekter, sager i modning, forudsætninger bag "
     "plan- og energimodellerne og de beslutninger, der venter. Talt med alle fem medarbejdere og "
     "med Kontrakt & Strategi, Driften og Vedligehold."),
    ("Uge 3–6",
     "Porteføljeoversigt og forudsætningslog etableret med ejer og dato; snitfladerne skrevet ned, "
     "så det er tydeligt, hvem der bestiller hvad; første beslutningsoplæg i ny form til "
     "direktionen."),
    ("Uge 7–12",
     "Projektmodellen omsat til beslutningspunkter, der virker i praksis, og prøvet af på et "
     "igangværende projekt; modenhedstjek taget i brug før nye sager; første fælles grundlag "
     "drøftet med en ejerkommune."),
    ("Måned 3–6",
     "Porteføljen prioriteret med kapacitet og økonomi på plads; rådgiver- og leverandørstyring "
     "formaliseret med bestillerkompetence i huset; medarbejderne har forventningsaftaler og "
     "tydelige roller."),
    ("Måned 6–12",
     "Plan & Projekt leverer både modnede sager og gennemførte projekter til aftalt tid og pris; "
     "styringen er dokumenteret og kan bruges af næste leder — og af CTR's ledelse som fast "
     "beslutningsgrundlag."),
]

KEYWORDS = (
    "Chef for Plan & Projekt · Plan & Projekt · Transmissionsselskab · Fjernvarme · 340.000 hjem · "
    "Ledelsesansvar · Projektportefølje · Komplekse projekter · Forsyningssikkerhed · Varmeprisen · "
    "Grønne omstilling · Decentral varmeproduktion · Idéfase · Forprojekt · Gennemførelse · "
    "Idriftsættelse · Projektmodning · Projektering · Udbud · Etablering · Overlevering til drift · "
    "Systemejerskab · Plan- og energimodeller · EnergyPRO · Plangrundlag · Effektbalance · "
    "Kapacitetsbehov · Varmeplanlægning · Ejerkommunerne · Hovedstadskommuner · Interessenter · "
    "Politisk forståelse · Direktionen · Bestyrelsen · Beslutningsoplæg · Porteføljeoverblik · "
    "Projektmodel · Styringsmodel · Roller · Ansvar · Beslutningspunkter · Beslutningsgange · "
    "Snitflader · Samarbejdsflader · Kontrakt & Strategi · Driften · Vedligehold · Asset Management "
    "· Reinvesteringer · Transmissionsnettet · Rådgivere · Leverandører · Kompetencer · "
    "Personaleledelse · Projektledere · Planlæggere · Faglige specialister · Strategisk planlægning · "
    "Bygherrerollen · Styring af økonomi · Risici · Organisatoriske · Projektstyring · Fremdrift · "
    "Kvalitet · Faglig sparring · Prioritering · Nærværende leder · Involverende leder · Tydelig · "
    "Retning · Ejerskab · Arbejdsfællesskab · Vedholdende · Pragmatiske løsninger · Mindre "
    "organisation · Bred opgaveportefølje · Myndigheder · Forsyningsselskaber · Teknisk eller "
    "akademisk uddannelse · Maskinmester · Ingeniør · Sund balance · Medarbejdertilfredshed · "
    "Frederiksberg · 1. januar 2027"
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

    m.models_table("STYRING AF PLAN & PROJEKT — ANVENDT I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER PLAN & PROJEKT I RYTMEN",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN LEDES OPGAVEN — DE TRE PARTER")
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
                  title="Ansøgning og CV — Chef for Plan & Projekt, CTR I/S",
                  subject="Fjernvarme · projektportefølje · projektmodning · bygherrerolle · "
                          "EnergyPRO · snitflader",
                  keywords=("chef for plan & projekt, ctr, fjernvarme, transmissionsselskab, "
                            "projektportefølje, projektmodning, bygherrerolle, energypro, "
                            "maskinmester, frederiksberg, dansk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1 (krav → løsning), CV side 2-3, 90 dage side 4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_CTR_ChefPlanOgProjekt.docx")
    print("OK", build(out))
