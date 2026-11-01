# -*- coding: utf-8 -*-
"""
Tekum — El-teknisk serviceleder, Nordjylland (nyoprettet el-afdeling, Aalborg).
Dansk JD. Opgave-først side 1 + CV + 90 dage/parter i ét dokument.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "El-teknisk serviceleder | El-service og drift | Nordjylland"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = ("Tekum · El-afdelingen Nordjylland · Afdelingschef Brian Bisgaard Kristensen · "
             "Aalborg")
SUBJECT = "Ansøgning: El-teknisk serviceleder — opbygningen af Tekums el-afdeling i Nordjylland"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Tekum åbner en el-afdeling i det nordjyske, og stillingen er den, der skal gøre den til en "
    "serviceforretning: et dedikeret serviceteam, aftaler der bliver fulgt op, og en leverance der "
    "holder den tid, der er lovet. En nyoprettet afdeling bliver ikke stærk af at have mange "
    "opgaver, men af at de første tyve sager bliver løst ens, prissat rigtigt og dokumenteret — og "
    "det er den rækkefølge, jeg arbejder i.",

    "Nedenfor er systemet, der står klar fra første dag: servicekatalog med responstider, "
    "kontraktkort med KPI og opfølgning, kapacitetsmodel for serviceteamet, tilbudsmodel med "
    "dækningsgrad, afvigelsesliste med ejer og en månedlig rapport på få tal.",
]

BULLETS = [
    ("Kravet: at træde ind i en nyoprettet stilling og præge afdelingens udvikling",
     "Løsningen er, at jeg har gjort det før: ELOHVAC blev bygget fra ingenting til 5 elektrikere, "
     "3 lærlinge og 40+ serviceanlæg med fuldt P&L. Jeg ved, at det første halve år går med at gøre "
     "få ting ens hver gang — og med at få de første kunder til at anbefale os videre."),

    ("Kravet: erfaring som serviceleder inden for el-teknisk service",
     "Løsningen er otte år med personaleansvar i el-teknisk drift og service: egen serviceforretning "
     "med tilbud, aftaler og teknikerkapacitet, fem år som driftschef på et 24/7-anlæg med "
     "højspænding, koblingsanlæg, pumper og køl — og elautoriseret maskinmester (LV/MV/HV) med "
     "el-teknisk baggrund i service og vedligeholdelse, så jeg kan gå ind i sagen selv."),

    ("Kravet: ledelse af serviceholdet og koordinering af daglige opgaver",
     "Løsningen er fast kadence: et kort tavlemøde hver morgen med dagens sager, mandskab og "
     "sikkerhed, en ugeplan der er skrevet ned inden ugen starter, og en kapacitetsmodel der viser, "
     "hvornår vi skal prioritere, sige nej eller sætte ekstra hænder på."),

    ("Kravet: at udføre kalkulationer og udarbejde tilbud",
     "Løsningen er en tilbudsmodel med fire linjer — tid, materialer, risiko og dækningsgrad — så et "
     "tilbud kan læses og forsvares, og så vi ved, om en sag var værd at vinde. Jeg har beregnet og "
     "solgt service på 40+ anlæg og kender forskellen på en pris, der vinder arbejdet, og en pris der "
     "taber penge."),

    ("Kravet: kvalitetssikring af udført arbejde og overholdelse af deadlines",
     "Løsningen er en skreven kontrolplan pr. opgavetype, egenkontrol med foto og signatur, og en "
     "afvigelsesliste hvor hver sag har ejer og frist. I GMP-reguleret drift har jeg afleveret 37 "
     "anlægsprojekter uden kritiske fund — kvalitet er dokumentation, ikke en mavefornemmelse."),

    ("Kravet: opfølgning på servicekontrakter og sikring af kundetilfredshed",
     "Løsningen er et kontraktkort pr. kunde: ydelser, responstider, KPI-formel, datakilde og "
     "grænseværdi — fulgt op hver måned og med en fast samtale med kunden hvert kvartal. "
     "Kundetilfredshed bliver et tal, vi kender, ikke noget vi hører om til sidst."),

    ("Kravet: træning og udvikling af medarbejdere for at sikre høj faglighed",
     "Løsningen er en kompetencematrix pr. tekniker — hvilke fag, certifikater og opgavetyper den "
     "enkelte kan løse alene — og en oplæringsplan der lukker hullerne. Jeg har selv oplært 3 "
     "lærlinge og bygget et 14-mands team op med sidemandsoplæring."),

    ("Kravet: relationsopbygning og vedligeholdelse hos eksisterende og nye kunder",
     "Løsningen er en kundeplan pr. konto med næste aftale, næste besøg og næste handling, og en "
     "bevidst strategi om at vokse hos de kunder, der allerede er glade for arbejdet. Nye kunder "
     "kommer sjældent fra en kold e-mail — de kommer fra en vellykket sag i nabolaget."),

    ("Kravet: selvstændig, løsningsorienteret, kvalitetsbevidst og teamplayer",
     "Løsningen er den måde, jeg er skruet sammen på: jeg tager ansvar uden at vente på mandat, "
     "løser problemet i marken før jeg skriver om det, og måler mig selv på, om holdet omkring mig "
     "lykkes. Det er også derfor, Tekums model med ansvarlighed, frihed og initiativ som om det var "
     "ens egen virksomhed passer mig."),
]

SYSTEM = (
    "Systemet står klar fra første dag: servicekatalog med responstider og pris pr. opgavetype, "
    "kontraktkort med KPI og opfølgning, kapacitetsmodel for serviceteamet, tilbudsmodel med "
    "dækningsgrad, afvigelsesliste med ejer og frist samt en månedlig rapport på få tal — ført i "
    "Excel og Power BI, med tilbud og kundeoplæg genereret i Python og Claude."
)

MIRROR = (
    "Om kravene: elautoriseret maskinmester (LV/MV/HV) og B.Tech, 20 år i tekniske anlæg og otte år "
    "med personaleansvar — bygget serviceforretning fra bunden med 40+ anlæg og fuldt P&L, ledet et "
    "14-mands team med 11 samtidige entrepriser, fem år som driftschef med budget i SAP og nul "
    "uplanlagte stop samt projektleder på 37 anlægsprojekter."
)

HONEST = (
    "Det skal siges ligeud: jeg har ikke ledet en afdeling i en virksomhed med syv afdelinger, og "
    "jeg har ikke et lokalt netværk af el-kunder i Nordjylland i dag — det skal bygges, og det "
    "kommer til at tage det første år. Til gengæld har jeg prøvet præcis den opgave, stillingen "
    "beskriver, i lille målestok: at få kunder, beregne tilbud, lede teknikere, følge op på aftaler "
    "og tjene penge på el-service."
)

CULTURE = (
    "Tekum er en ung virksomhed i vækst med syv afdelinger og en model, hvor ansvarlighed og frihed "
    "går forud for kontrol, og hvor man skal være agil og fleksibel og træffe beslutninger, som var "
    "det ens egen virksomhed. Den model virker kun, hvis rammerne er tydelige: hvad den enkelte må beslutte "
    "selv, hvornår der skal spørges, og hvordan en sag lukkes. Derfor bygger jeg standarderne sammen "
    "med serviceteamet frem for at præsentere dem — og lader ejerskabet blive nede på holdet."
)

PRACTICAL = (
    "Bosat i Måløv — cirka 4 timer og et kvarter i bil til Aalborg. Jeg er indstillet på fast "
    "ugentlig tilstedeværelse i Nordjylland og på at være der, hvor kunderne og teknikerne er, og "
    "åben for at drøfte en ordning med bopæl tættere på Aalborg. Kørekort B og bil, dansk på "
    "modersmålsniveau og engelsk professionelt. Kan tiltræde hurtigst muligt."
)

CLOSING = (
    "I første samtale vil jeg gerne tale om, hvilke kunder i Nordjylland der i dag køber el-service "
    "uden en aftale — og hvordan vi måler, om den nye afdeling er på plads efter de første tre "
    "måneder."
)

# ------------------------------------------------------------------ CV
PROFILE = (
    "Elautoriseret maskinmester (LV/MV/HV) og B.Tech med 20 år i tekniske anlæg og otte år med "
    "personaleansvar. Har bygget en el-serviceforretning fra bunden med 40+ serviceanlæg og fuldt "
    "P&L, ledet et 14-mands team med 11 samtidige entrepriser, været driftschef på et 24/7-anlæg med "
    "budget i SAP og nul uplanlagte stop og projektleder på 37 anlægsprojekter. Arbejder med "
    "servicekataloger, tilbudsmodeller, kapacitetsplaner og KPI-tavler — og koder selv de oplæg, "
    "ledelsen læser."
)

PRACTICE = [
    ("Servicekatalog og responstider",
     "Ydelse, responstid, pris og grænseflade pr. opgavetype — skrevet ned, prissat og målt, så "
     "serviceniveauet kan sælges uden at gætte."),
    ("Kontraktkort og opfølgning",
     "Pr. kunde: ydelser, responstider, KPI-formel, datakilde, grænseværdi og næste samtale — med "
     "navngiven ejer og månedlig måling."),
    ("Tilbud og kalkulation",
     "Tid, materialer, risiko og dækningsgrad — og en fast prøve på, om tilbuddet kan leveres med "
     "det mandskab og de certifikater, vi har."),
    ("Kapacitet og kompetencer",
     "Ugeplan og kompetencematrix pr. tekniker: hvilke fag og certifikater vi kan løse alene, og "
     "hvor vi skal oplære eller sætte ekstra på."),
    ("Kvalitet og dokumentation",
     "Kontrolplan pr. opgavetype, egenkontrol med foto og signatur samt afvigelsesliste med ejer og "
     "frist — kvalitet, der kan vises frem for kunden."),
    ("Ejerskab i holdet",
     "Skreven forventningsaftale pr. medarbejder om ansvar, kompetence og beslutningsret, og en "
     "gode kommunikations- og samarbejdsevner i hverdagen — så frihed under ansvar bliver en "
     "arbejdsform og ikke et slogan."),
]

MODELS = [
    ("Servicekatalog",
     "Ydelse, responstid og pris pr. opgavetype — grundlaget for både tilbud og leverance"),
    ("Kontraktkort",
     "Pr. kunde: ydelser, KPI-formel, datakilde, grænseværdi og næste kvartalssamtale"),
    ("Tilbudsmodel",
     "Tid, materialer, risiko og dækningsgrad — tilbud, der kan læses og forsvares"),
    ("Kapacitetsmodel",
     "Timer, fag og certifikater pr. uge — serviceteamet bygges op foran ordrebogen"),
    ("Afvigelsesliste",
     "Hver afvigelse med ejer, frist og lukkedato — kvalitet følges, ikke bare konstateres"),
    ("Servicerapport",
     "Månedligt på få tal: aftaler, omsætning, dækningsgrad, responstider og næste beslutning"),
]

ACHIEVEMENTS = [
    ("El-serviceforretning bygget fra bunden",
     "ELOHVAC: 5 elektrikere og 3 lærlinge, 40+ serviceanlæg, eget kundekartotek, tilbud og "
     "serviceaftaler med responstider — og fuldt ansvar for dækningsgrad og bundlinje."),
    ("Nul uplanlagte stop i fem år",
     "24/7-anlæg med højspænding, koblingsanlæg, pumper, HVAC og køl — planlagt og tilstandsbaseret "
     "vedligehold, KPI'er i SAP og prioritering mellem afhjælpning og investering."),
    ("14-mands team med 11 samtidige entrepriser",
     "kapacitetsplanlægning og daglige tavlemøder i eksisterende byggeri med brugere omkring os — "
     "leverancer, der ikke gik ud over driften."),
    ("37 anlægsprojekter uden kritiske fund",
     "2-10 mio. kr. i industriel og GMP-reguleret drift: 25 specialister koordineret på tværs af "
     "mekanik, el, proces og indkøb; FAT/SAT, IQ/OQ/PQ og dokumentation i orden."),
]

EXPERIENCE = [
    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og "
     "leverandøraftaler",
     [("Serviceaftaler, kunder og indtjening",
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
     "Anvendt i drift, service og projekter · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og projekter · 2017 – nu"),
]

LANGUAGES = ("Dansk (modersmål, skrift og tale) · Engelsk (professionelt, skrift og tale) · "
             "Persisk/farsi · Kørekort B (kategori B)")

PRACTICAL_CV = (
    "Bosat i Måløv — cirka 4 timer og et kvarter i bil til Aalborg. Indstillet på fast ugentlig "
    "tilstedeværelse i Nordjylland og på at være synlig hos kunder og teknikere fra første uge; "
    "åben for at drøfte en ordning med bopæl tættere på Aalborg. Kørekort kategori B og bil, dansk "
    "på modersmålsniveau og engelsk professionelt. Kan tiltræde hurtigst muligt."
)

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Biofos (Lynetten), Novo Nordisk A/S, "
              "Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Serviceteamet i Nordjylland",
     "Skreven forventningsaftale og kompetenceplan, fast kadence og et tavlemøde, hvor sikkerhed og "
     "dagens opgaver ligger åbent — en ny afdeling bliver kun stærk, hvis de første teknikere vil "
     "blive."),
    ("Kunderne i Nordjylland",
     "Kontraktkort med responstider og en fast kvartalssamtale; vi skal komme før nedbruddet og "
     "ikke efter regningen."),
    ("Afdelingschefen og Tekums ledelse",
     "Aftalte eskaleringsgrænser, en månedlig rapport på få tal og et klart oplæg, når der skal "
     "besluttes investering i kapacitet eller et nyt servicekoncept."),
    ("De øvrige seks afdelinger",
     "Fælles kompetencer og mandskab prioriteret åbent på tværs af Jylland og Fyn — så kunden får "
     "én aftale og én faktura, uanset hvilken afdeling der løser sagen."),
]

FIRST90 = [
    ("Dage 1–30",
     "Gennemgået alle eksisterende kunder og sager i Nordjylland med afdelingschefen: hvad er "
     "lovet, hvad er prissat, og hvor taber vi penge. Talt med hver tekniker om, hvad der driller i "
     "hverdagen, og været ude hos de ti vigtigste kunder."),
    ("Dage 30–60",
     "Servicekatalog og tilbudsmodel på plads for de opgavetyper, der betyder mest; kontraktkort på "
     "de kunder, vi har aftaler med; kapacitetsmodel lagt pr. uge; første månedlige rapport til "
     "afdelingschefen."),
    ("Dage 60–90",
     "Afvigelsesliste og kontrolplan i brug, kompetencematrix pr. tekniker og en oplæringsplan; "
     "kundeplan med næste aftale pr. konto; mindst to nye serviceaftaler indgået."),
    ("Måned 3–6",
     "El-afdelingen leverer til tiden med kendt dækningsgrad pr. sag, serviceteamet er udvidet med "
     "de rigtige fag, og de første kunder er begyndt at anbefale os videre."),
    ("Måned 6–12",
     "Afdelingen er en selvstændig forretning i Tekum med stabil leverance, lønsomme aftaler og en "
     "salgsmaskine, der kan skaleres sammen med de øvrige afdelinger."),
]

KEYWORDS = (
    "El-teknisk serviceleder · Tekum · Nordjylland · Aalborg · El-afdeling · Nyoprettet stilling · "
    "El-service · Service og vedligehold · El-tekniske installationer · Mekaniske løsninger · "
    "Serviceteam · Ledelse af servicehold · Koordinering · Daglige opgaver · Kalkulationer · "
    "Tilbud · Kvalitetssikring · Deadlines · Servicekontrakter · Kundetilfredshed · "
    "Relationsopbygning · Eksisterende og nye kunder · Træning og udvikling · Faglige kompetencer · "
    "Elektriker · El-installatør · Elautoriseret maskinmester · Anerkende og motivere · "
    "Kommunikation · Samarbejde · Teamplayer · Struktureret · Prioritering · Selvstændig · "
    "Løsningsorienteret · Kvalitetsbevidst · Ansvarlighed · Frihed under ansvar · Agilitet · "
    "Initiativ · Ejerskab · Vækst · Serviceleverance · Dækningsgrad · Lean · SAP · Kørekort B"
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

    m.models_table("EL-SERVICEAFDELINGENS STYRING — ANVENDT I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER EL-AFDELINGEN I RYTMEN",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN LEDES AFDELINGEN — DE FIRE PARTER")
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
    out = os.path.join(ROOT, "Shahram_Ajloo_Tekum_EltekniskServiceleder.docx")
    build(out)
    print("OK " + out)
