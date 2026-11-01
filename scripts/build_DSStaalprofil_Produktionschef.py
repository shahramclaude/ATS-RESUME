# -*- coding: utf-8 -*-
"""
DS Stålprofil A/S — Produktionschef, fabrik i Hobro (ca. 45 medarbejdere, ledergruppe).
Dansk JD. Opgave-først side 1 + CV + 90 dage/parter i ét dokument.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Produktionschef | Produktion, kvalitet og logistik | Lean og automatisering"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = "DS Stålprofil A/S · Produktion, Hobro"
SUBJECT = "Ansøgning: Produktionschef til DS Stålprofil — produktion, kvalitet og logistik i Hobro"

# ------------------------------------------------------------------ side 1
INTRO = [
    "DS Stålprofil søger en produktionschef, der både kan holde en fabrik kørende hver dag og "
    "flytte den: sikker drift, leveringssikkerhed og kvalitet som grundlag — og digitalisering, "
    "automatisering og procesoptimering som den vej, konkurrencekraften skal komme fra. Det er to "
    "opgaver, der let kommer til at konkurrere om den samme tid, og rækkefølgen er afgørende: "
    "stabilitet før forandring, og forandring i små nok bidder til at produktionen ikke mærker det "
    "som risiko.",

    "Nedenfor er systemet, der står klar fra første dag: tavle med sikkerhed, levering, kvalitet og "
    "produktivitet pr. skift; KPI-kort med formel og grænseværdi; Lean-forbedringstavle med "
    "prioriteret bakke; kvalitetsafvigelser med ejer og frist; bemandings- og kompetenceplan; og et "
    "investerings- og automatiseringskatalog med business case pr. tiltag.",
]

BULLETS = [
    ("Kravet: en sikker, stabil og effektiv drift med høj kvalitet og leveringssikkerhed",
     "Løsningen er én tavle pr. skift med fire tal — sikkerhed, levering, kvalitet og produktivitet "
     "— hvor afvigelsen bliver en sag med ejer og frist, inden den bliver en krise. Fem år som "
     "driftschef på et 24/7-anlæg med nul uplanlagte stop og budget i SAP er netop den disciplin: "
     "stabilitet er noget, man bygger om morgenen."),

    ("Kravet: ledelse af både ledere, funktionærer og timelønnede medarbejdere",
     "Løsningen er skreven forventningsaftale pr. leder og funktionær om ansvar, kompetence og "
     "beslutningsret — og en fast kadence, hvor lederen rapporterer på sine tal, ikke på sin "
     "aktivitet. Jeg har ledet et 14-mands team med 11 samtidige entrepriser, 25 specialister på "
     "tværs af fag og et 12-mands produktionsteam i skift."),

    ("Kravet: dokumenterede resultater med Lean, procesoptimering og forandringsledelse",
     "Løsningen er værdistrømsanalyse på de tre produkter, der fylder mest, standardarbejde på de "
     "kritiske stationer og en forbedringstavle, hvor bakken prioriteres efter effekt pr. "
     "indsats. Gevinsterne hentes i små, hyppige træk — ikke i ét stort projekt, der først giver "
     "noget om et år."),

    ("Kravet: udvikling af produktionen gennem digitalisering, automatisering og procesoptimering",
     "Løsningen er et automatiseringskatalog med business case pr. tiltag: investering, forventet "
     "effekt i timer og kroner, risiko og tilbagebetalingstid — så ledergruppen kan beslutte i den "
     "rigtige rækkefølge. Jeg har selv automatiseret rapportering og tilbudsoplæg i Python og "
     "Claude, og jeg ved, at gevinsten oftest ligger i data og arbejdsgange, før den ligger i "
     "maskiner."),

    ("Kravet: videreudvikling af kvalitetsarbejdet og høje standarder",
     "Løsningen er en kontrolplan pr. proces, egenkontrol med dokumentation, afvigelsesliste med "
     "root cause og lukning — og en kvalitetschef, der har tal at lede på. I GMP-reguleret drift har "
     "jeg afleveret 37 anlægsprojekter uden kritiske fund og ført ændringshåndtering, der bestod "
     "revision."),

    ("Kravet: et sikkert arbejdsmiljø med fokus på trivsel, engagement og nul-ulykker",
     "Løsningen er sikkerhed som første punkt på skiftets tavlemøde, nærved-hændelser fulgt til "
     "lukning, sikkerhedsrunde med AMO hver måned og LOTO på de maskiner, hvor det gælder. "
     "Nul-ulykker kommer ikke af en kampagne, men af at hver enkelt ved, hvad der er farligt i "
     "netop hans station."),

    ("Kravet: konstruktivt samarbejde med tillidsrepræsentanter og arbejdsmiljøorganisationen",
     "Løsningen er et fast møde med TR og AMO hver måned med samme dagsorden og skrevne referater, "
     "og at forandringer bliver drøftet, før de er besluttet — ikke efter. Samarbejde med tillidsvalgte "
     "har jeg haft i alle mine lederroller, og det har aldrig været det, der stoppede en "
     "forbedring."),

    ("Kravet: ansvar for budgetter, KPI'er og opfølgning samt medlemskab af ledergruppen",
     "Løsningen er en månedsprognose, der bliver justeret frem for forklaret, og et oplæg til "
     "ledergruppen på én side: hvad vi gør, hvad det koster, hvad det giver, og hvornår vi ved, om "
     "det virkede. Jeg har haft fuldt P&L-ansvar i egen virksomhed og budgetansvar som driftschef."),

    ("Kravet: forretningsforståelse, produktionsøkonomi samt stærk indsigt i ERP, BI og digitale "
     "løsninger",
     "Løsningen er at kende sin dækningsgrad pr. produktgruppe og sin kapacitetsomkostning pr. "
     "time — og at kunne trække det selv. Jeg arbejder dagligt i ERP og Excel, bygger KPI-tavler i "
     "Power BI og koder selv de scripts, der gør rapporteringen to minutter i stedet for to dage."),
]

SYSTEM = (
    "Systemet står klar fra første dag: skifttavle med sikkerhed, levering, kvalitet og "
    "produktivitet, KPI-kort med formel og grænseværdi, Lean-forbedringstavle med prioriteret "
    "bakke, kvalitetsafvigelser med ejer og frist, bemandings- og kompetenceplan samt et "
    "automatiseringskatalog med business case — ført i Excel og Power BI, med rapporter og oplæg "
    "genereret i Python og Claude."
)

MIRROR = (
    "Om kravene: elautoriseret maskinmester (LV/MV/HV) og B.Tech, 20 år i tekniske anlæg og otte år "
    "med personaleansvar — ledet 14 mand med 11 samtidige entrepriser, 25 specialister og et "
    "12-mands produktionsteam, fem år som driftschef med budget i SAP og nul uplanlagte stop samt "
    "37 anlægsprojekter uden kritiske fund. Lean, procesoptimering og KPI-styring er arbejdsform, "
    "ikke et kursus."
)

HONEST = (
    "Det skal siges ligeud: jeg har ikke været produktionschef på en stålprofilfabrik, og jeg har "
    "ikke ledet 45 medarbejdere i én produktionsenhed med kvalitet og logistik under samme hat. "
    "Mine anlæg har været forsyning, pharma og industri, og min produktion har været montage og "
    "værksted frem for valsning og profilering. Til gengæld har jeg gjort det, stillingen "
    "beskriver, i mindre målestok: holdt en produktion kørende, løftet produktiviteten, bygget "
    "kvalitetsstyring og ledet både ledere, funktionærer og timelønnede."
)

CULTURE = (
    "DS Stålprofils kultur beskrives med tre ord — ordentlighed, samarbejde og høj faglighed — og "
    "med korte beslutningsveje og plads til initiativ. Det er en kultur, hvor en produktionschef "
    "skal være på gulvet og ikke kun i mødelokalet, og hvor forandringer skal kunne forklares for "
    "den mand, der står ved maskinen. Derfor bygger jeg standarder sammen med medarbejderne og "
    "tillidsvalgte frem for at præsentere dem — og jeg måler mig selv på, om holdet omkring mig "
    "lykkes."
)

PRACTICAL = (
    "Bosat i Måløv — cirka 3 timer og 45 minutter i bil til Hobro. Jeg er indstillet på fast "
    "ugentlig tilstedeværelse på fabrikken og på at være der, hvor driften er, og åben for at "
    "drøfte en ordning med bopæl tættere på Hobro. Kørekort B og bil, dansk på modersmålsniveau og "
    "engelsk professionelt. Kan tiltræde hurtigst muligt."
)

CLOSING = (
    "I første samtale vil jeg gerne tale om, hvor i produktionen leveringssikkerheden i dag er "
    "sårbar — og hvilke tre forbedringer der ville kunne mærkes på bundlinjen inden for det første "
    "halve år."
)

# ------------------------------------------------------------------ CV
PROFILE = (
    "Elautoriseret maskinmester (LV/MV/HV) og B.Tech med 20 år i tekniske anlæg og otte år med "
    "personaleansvar. Har ledet et 14-mands team med 11 samtidige entrepriser, 25 specialister og "
    "et 12-mands produktionsteam, været driftschef på et 24/7-anlæg med budget i SAP og nul "
    "uplanlagte stop, projektleder på 37 anlægsprojekter og bygget egen servicevirksomhed med fuldt "
    "P&L. Arbejder med Lean, standardarbejde, KPI-tavler og KPI-kort — og koder selv den "
    "rapportering, ledelsen læser."
)

PRACTICE = [
    ("Sikkerhed og stabil drift",
     "Skifttavle med sikkerhed, levering, kvalitet og produktivitet; afvigelser med ejer og frist; "
     "LOTO og arbejdstilladelser på de kritiske maskiner."),
    ("Lean og forbedringer",
     "Værdistrømsanalyse, standardarbejde, 5S og en forbedringstavle, hvor bakken prioriteres "
     "efter effekt pr. indsats — små, hyppige træk frem for ét stort projekt."),
    ("Kvalitetsstyring",
     "Kontrolplan pr. proces, egenkontrol med dokumentation, afvigelsesliste med root cause og "
     "lukning — og KPI'er, kvalitetschefen kan lede på."),
    ("Bemanding og kompetencer",
     "Bemandings- og kompetenceplan pr. skift: hvilke stationer den enkelte kan køre alene, og hvor "
     "der skal oplæres, før der skæres."),
    ("Digitalisering og automatisering",
     "Automatiseringskatalog med business case pr. tiltag — investering, effekt i timer og kroner, "
     "risiko og tilbagebetalingstid; rapportering bygget i Power BI og Python."),
    ("Produktionsøkonomi og ledergruppe",
     "Dækningsgrad pr. produktgruppe, kapacitetsomkostning pr. time og månedsprognose, der bliver "
     "justeret frem for forklaret — oplæg til ledergruppen på én side."),
]

MODELS = [
    ("Skifttavle",
     "Sikkerhed, levering, kvalitet og produktivitet pr. skift — afvigelse bliver sag med ejer "
     "og frist"),
    ("KPI-kort",
     "Pr. nøgletal: formel, datakilde, grænseværdi og ansvarlig — så tallet kan styres, ikke kun "
     "læses"),
    ("Forbedringstavle",
     "Prioriteret bakke af Lean-tiltag med effekt pr. indsats og gevinst fulgt til realisering"),
    ("Kvalitetsafvigelser",
     "Afvigelse, root cause, korrigerende handling, ejer og lukkedato — kvalitet følges, ikke "
     "konstateres"),
    ("Bemandings- og kompetenceplan",
     "Stationer, fag og certifikater pr. skift — kapaciteten planlægges, før ordrebogen kræver "
     "det"),
    ("Automatiseringskatalog",
     "Investering, effekt, risiko og tilbagebetalingstid pr. tiltag — beslutningsgrundlag for "
     "ledergruppen"),
]

ACHIEVEMENTS = [
    ("Nul uplanlagte stop i fem år",
     "24/7-anlæg med højspænding, koblingsanlæg, pumper, HVAC og køl — planlagt og tilstandsbaseret "
     "vedligehold, KPI'er i SAP og prioritering mellem afhjælpning og investering."),
    ("14-mands team med 11 samtidige entrepriser",
     "kapacitetsplanlægning, daglige tavlemøder og opfølgning på den enkelte — leverancer, der ikke "
     "gik ud over driften i eksisterende byggeri med brugere omkring os."),
    ("37 anlægsprojekter uden kritiske fund",
     "2-10 mio. kr. i industriel og GMP-reguleret drift: 25 specialister koordineret på tværs af "
     "mekanik, el, proces og indkøb; FAT/SAT, IQ/OQ/PQ og dokumentation i orden."),
    ("Serviceforretning med fuldt P&L",
     "ELOHVAC: 5 elektrikere og 3 lærlinge, 40+ serviceanlæg, eget kundekartotek og ansvar for "
     "dækningsgrad, bundlinje og investeringer — to regnskaber, der skulle hænge sammen."),
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
      ("Ændringer, dokumentation og driftsoverlevering",
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
     "Anvendt i drift, produktion og projekter · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og projekter · 2017 – nu"),
]

LANGUAGES = ("Dansk (modersmål, skrift og tale) · Engelsk (professionelt, skrift og tale) · "
             "Persisk/farsi · Kørekort B (kategori B)")

PRACTICAL_CV = (
    "Bosat i Måløv — cirka 3 timer og 45 minutter i bil til Hobro. Indstillet på fast ugentlig "
    "tilstedeværelse på fabrikken og på at være synlig i produktionen fra første uge; åben for at "
    "drøfte en ordning med bopæl tættere på Hobro. Kørekort kategori B og bil, dansk på "
    "modersmålsniveau og engelsk professionelt. Kan tiltræde hurtigst muligt."
)

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Biofos (Lynetten), Novo Nordisk A/S, "
              "Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Produktionslederen, kvalitetschefen og de nærmeste ledere",
     "Skreven forventningsaftale om ansvar, kompetence og beslutningsret og en fast kadence, hvor "
     "lederen rapporterer på sine tal — ledelse af ledere kræver rammer, ikke kontrol."),
    ("Medarbejderne på gulvet og tillidsrepræsentanterne",
     "Fast månedligt møde med TR og AMO med samme dagsorden og skrevne referater; forandringer "
     "drøftet, før de er besluttet — og sikkerhed som første punkt på skiftets tavlemøde."),
    ("Den administrerende direktør og ledergruppen",
     "Oplæg på én side: hvad vi gør, hvad det koster, hvad det giver, og hvornår vi ved, om det "
     "virkede — med budget og månedsprognose, der bliver justeret frem for forklaret."),
    ("Kunder, leverandører og logistik",
     "Leveringssikkerhed målt pr. uge og en logistikplan, der tåler, at produktionen ikke er "
     "færdig til tiden — så kunden hører det fra os, før han opdager det selv."),
]

FIRST90 = [
    ("Dage 1–30",
     "Gået fabrikken igennem med produktionslederen og kvalitetschefen: hvor stopper flowet, hvor "
     "kommer afvigelserne fra, og hvad siger de sidste tre måneders leveringstal. Talt med TR, AMO "
     "og hver leder om, hvad der driller i hverdagen."),
    ("Dage 30–60",
     "Skifttavle og KPI-kort på plads med formel, datakilde og grænseværdi; afvigelsesliste i brug "
     "med ejer og frist; bemandings- og kompetenceplan pr. skift; første oplæg til ledergruppen."),
    ("Dage 60–90",
     "Værdistrømsanalyse på de tre vigtigste produktgrupper; de første fem Lean-tiltag prioriteret "
     "efter effekt pr. indsats; automatiseringskatalog med business case for de næste tre "
     "investeringer."),
    ("Måned 3–6",
     "Leveringssikkerhed og kvalitet målt stabilt over tre måneder, to til tre forbedringer "
     "realiseret med dokumenteret gevinst, og en produktionsorganisation, hvor hver leder kender "
     "sine tal."),
    ("Måned 6–12",
     "Produktionen er digitaliseret der, hvor det giver mest, automatiseringsprojekterne er i gang "
     "med kendt business case, og DS Stålprofil har en produktionschef, der kan vækste fabrikken "
     "uden at sænke kvaliteten."),
]

KEYWORDS = (
    "Produktionschef · DS Stålprofil · Hobro · Produktion · Kvalitet · Logistik · Ledergruppe · "
    "Konkurrencekraft · Effektiv drift · Digitalisering · Automatisering · Ledelsesmæssig "
    "udvikling · Performance management · Løbende forbedringer · Leveringssikkerhed · "
    "Produktivitet · Ressourceudnyttelse · Procesoptimering · Kvalitetsarbejde · Kvalitetsstyring · "
    "Arbejdsmiljø · Trivsel · Engagement · Nul-ulykker · Investeringsprojekter · "
    "Automatiseringsprojekter · Tillidsrepræsentanter · Arbejdsmiljøorganisationen · Budgetter · "
    "KPI'er · Strategisk udvikling · Produktionsledelse · Ledelse af ledere · Funktionærer · "
    "Timelønnede medarbejdere · Lean · Forandringsledelse · Forretningsforståelse · "
    "Produktionsøkonomi · ERP · BI · Digitale løsninger · Dansk · Engelsk · Følgeskab · "
    "Kommunikation · Klare forventninger · Gennemslagskraft · Strategisk overblik · Operationel "
    "handlekraft · Ordentlighed · Samarbejde · Faglighed · Initiativ · Handlekraft"
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

    m.models_table("PRODUKTIONENS STYRING — ANVENDT I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER PRODUKTIONEN I RYTMEN",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN LEDES FABRIKKEN — DE FIRE PARTER")
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
    out = os.path.join(ROOT, "Shahram_Ajloo_DSStaalprofil_Produktionschef.docx")
    build(out)
    print("OK " + out)
