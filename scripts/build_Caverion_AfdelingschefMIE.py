# -*- coding: utf-8 -*-
"""
Caverion A/S — Afdelingschef til Marine, Industri og Energi (MIE), Esbjerg.
Dansk JD (kun CV efterspurgt — leveres som ét samlet dokument). Opgave-først side 1 + CV.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Afdelingschef | Marine, Industri og Energi | Servicesalg og drift"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = ("Caverion A/S · Marine, Industri og Energi · Head of Marine, Industry and Energy "
             "Karsten Krogsøe · Esbjerg")
SUBJECT = "Ansøgning: Afdelingschef til Caverions Marine-, Industri- og Energiforretning"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Caverion bygger en serviceafdeling op inden for Marine, Industri og Energi — ikke et "
    "vedligeholdelsesteam, men en forretning med egne serviceaftaler, egne koncepter og egen "
    "teknikerkapacitet, der skal kunne vokse uden at kvaliteten falder. Opgaven har derfor to sider: "
    "den kommercielle, hvor kunderne i Esbjerg, Fredericia og Odense skal have et tilbud, de kan "
    "sige ja til, og den operationelle, hvor den samme aftale skal leveres med den dækningsgrad, "
    "der blev regnet hjem.",

    "Nedenfor er systemet, der står klar fra første dag: servicekatalog med responstider og pris pr. "
    "fag, kontraktkort med KPI og dækningsgrad, kapacitetsmodel for teknikerne, vækstpipeline for "
    "nye aftaler og en skreven integrationsplan for de serviceaktiviteter, der allerede findes.",
]

BULLETS = [
    ("Kravet: erfaring med at opbygge og udvikle en serviceforretning",
     "Løsningen er den forretning, jeg selv har bygget: ELOHVAC fra bunden til 5 elektrikere, 3 "
     "lærlinge og 40+ serviceanlæg med fuldt P&L — kundekreds, serviceaftaler, tilbudsberegning og "
     "ansvar for både bundlinje og kvalitet. En serviceafdeling bliver skalerbar af definerede, "
     "prissatte og målte ydelser, ikke af flere hænder alene."),

    ("Kravet: stærke kommercielle kompetencer og blik for vækstmuligheder",
     "Løsningen er en vækstpipeline, der følges som ordrebogen: hver kunde har en næste aftale i sig "
     "— et eftersyn, en udvidelse af anlægget, et nyt fagområde — med ejer, værdi og næste handling. "
     "Vækst i service kommer fra de kunder, der allerede er glade for arbejdet."),

    ("Kravet: kundeudvikling og opbygning af stærke, langsigtede relationer",
     "Løsningen er en fast kvartalsgennemgang pr. kunde med KPI'er, hændelser og forslag til næste "
     "sæsons arbejde — ikke et møde, hvor vi forklarer, hvorfor fakturaen ser ud, som den gør. I et "
     "marked med marine- og energikunder, hvor nedbrud koster produktion, er relationen bygget på, "
     "at vi kommer før nedbruddet."),

    ("Kravet: forståelse for og erfaring med tekniske servicekontrakter",
     "Løsningen er et kontraktkort pr. aftale: ydelser, responstider, KPI-formel, datakilde, "
     "grænseværdi, bod og dækningsgrad — så kontrakten kan styres på tal og ikke på mavefornemmelse. "
     "Jeg har stået på begge sider af bordet: købt serviceaftaler som driftschef i Biofos og solgt "
     "dem som indehaver af ELOHVAC."),

    ("Kravet: evnen til at omsætte strategi til konkrete initiativer og målbare resultater",
     "Løsningen er en serviceplan med tre til fire initiativer ad gangen, hver med ejer, forventet "
     "effekt i kroner og en prøvekørsel på én kunde, før det bliver standard. Strategi, der ikke kan "
     "oversættes til en handling på mandag, bliver ikke gennemført."),

    ("Kravet: erfaring med både drift og forretningsudvikling",
     "Løsningen er fem år som driftschef på et 24/7-anlæg med budget i SAP og nul uplanlagte stop, "
     "kombineret med egen virksomhed, hvor drift og forretning var samme regnestykke. Installation "
     "og idriftsættelse er hjemmebane fra 37 anlægsprojekter, og jeg har holdt et anlæg kørende, "
     "mens der blev bygget omkring det — samme disciplin som service i et produktionsmiljø."),

    ("Kravet: personaleledelse og evnen til at skabe følgeskab",
     "Løsningen er at lede gennem rammer og forventninger: en skreven forventningsaftale pr. "
     "medarbejder om ansvar, kompetence og beslutningsret, fast kadence og et tavlemøde hver "
     "morgen, hvor dagens opgaver og sikkerheden ligger åbent. Jeg har ledet 5 elektrikere og 3 "
     "lærlinge, et 14-mands team og 25 specialister på tværs af fag."),

    ("Kravet: høj grad af selvstændighed, handlekraft og initiativ — opbygge processer fra bunden",
     "Løsningen er at starte med det, der giver kunden og forretningen værdi i uge et: én "
     "servicebeskrivelse, én kontraktstruktur og én måde at lukke en sag på — og så bygge videre. "
     "Jeg har bygget en virksomhed op fra ingenting, og jeg ved, at det første år går med at gøre "
     "få ting ens hver gang."),

    ("Kravet: struktureret, resultatorienteret tilgang og samarbejde på tværs i MIE-ledelsen",
     "Løsningen er en månedlig ledelsesrapport på få tal — aftaler indgået, omsætning, dækningsgrad, "
     "responstider, kapacitet og næste beslutning — plus en skreven snitflade til de øvrige "
     "forretningsområder, så den samme kunde ikke får to forskellige tilbud. Elautoriseret "
     "maskinmester (LV/MV/HV) og B.Tech med 20 år i tekniske anlæg betyder, at jeg kan gå ind i "
     "sagen selv, når det brænder."),
]

SYSTEM = (
    "Systemet står klar fra første dag: servicekatalog med responstider og pris pr. fag, "
    "kontraktkort med KPI og dækningsgrad, kapacitetsmodel for teknikerne, vækstpipeline for nye "
    "aftaler og koncepter samt en månedlig ledelsesrapport — ført i Excel og Power BI, med tilbuds- "
    "og kundeoplæg genereret i Python og Claude."
)

MIRROR = (
    "Om kravene: elautoriseret maskinmester (LV/MV/HV) og B.Tech, 20 år i tekniske anlæg og otte år "
    "med personaleansvar — bygget serviceforretning fra bunden med 40+ anlæg og fuldt P&L, ledet et "
    "14-mands team med 11 samtidige entrepriser, fem år som driftschef med budget i SAP og nul "
    "uplanlagte stop samt to år som projektleder på 37 anlægsprojekter."
)

HONEST = (
    "Det skal siges ligeud: jeg har ikke bygget en serviceafdeling i en virksomhed af Caverions "
    "størrelse og ikke arbejdet med marine- eller offshorekunder — mine anlæg har været industri, "
    "forsyning og pharma, ikke skibe. Til gengæld har jeg prøvet den opgave, stillingen beskriver, i "
    "lille målestok: at få kunder, definere ydelser, sætte priser, bygge teknikerkapacitet og tjene "
    "penge på det."
)

CULTURE = (
    "Caverion vokser i disse år gennem opkøb — GK's serviceaktiviteter, BS Sikring og Elteknik, "
    "DI-Teknik og CS electric i Esbjerg — og MIE er netop det sted, hvor marine, industri og energi "
    "mødes i et af Danmarks stærkeste energi- og offshoremiljøer. En ny afdelingschef skal derfor "
    "ikke opfinde kompetencerne, men samle dem: de eksisterende serviceaktiviteter skal integreres i "
    "én aftalemodel, én dokumentationspraksis og én kundeoplevelse. Kulturen beskrives som uformel, "
    "og derfor bygger jeg standarder sammen med teknikerne frem for at præsentere dem."
)

PRACTICAL = (
    "Bosat i Måløv — cirka 3 timer i bil til Esbjerg og kortere til Fredericia og Odense. Jeg er "
    "indstillet på fast ugentlig tilstedeværelse i Esbjerg og på at være synlig der i starten, og "
    "åben for at drøfte en ordning med bopæl tættere på. Kørekort B og bil, dansk på "
    "modersmålsniveau og engelsk professionelt. Kan tiltræde hurtigst muligt."
)

CLOSING = (
    "I første samtale vil jeg gerne tale om, hvilke serviceaftaler MIE i dag leverer uden at have "
    "prissat dem ordentligt — og hvordan I måler, om den nye afdeling er lønsom om tolv måneder."
)

# ------------------------------------------------------------------ CV
PROFILE = (
    "Elautoriseret maskinmester (LV/MV/HV) og B.Tech med 20 år i tekniske anlæg og otte år med "
    "personaleansvar. Har bygget en serviceforretning fra bunden med 40+ serviceanlæg og fuldt P&L, "
    "ledet et 14-mands team med 11 samtidige entrepriser, været driftschef på et 24/7-anlæg med "
    "budget i SAP og nul uplanlagte stop og projektleder på 37 anlægsprojekter. Arbejder med "
    "servicekataloger, kontraktkort, kapacitetsmodeller og KPI-tavler — og koder selv de oplæg, "
    "ledelsen læser."
)

PRACTICE = [
    ("Servicekatalog og SLA",
     "Ydelse, responstid, pris og grænseflade pr. fag — skrevet ned, prissat og målt, så "
     "serviceniveauet kan sælges uden at gætte."),
    ("Kontraktkort",
     "Pr. kunde: ydelser, responstider, KPI-formel, datakilde, grænseværdi, bod og dækningsgrad — "
     "med navngiven ejer og månedlig måling."),
    ("Teknikerkapacitet",
     "Kapacitets- og kompetencemodel pr. uge: hvilke fag, hvilke certifikater og hvilke "
     "opgaver — så egen kapacitet kan bygges op i takt med aftalerne."),
    ("Vækstpipeline",
     "Næste aftale pr. kunde med ejer, værdi og næste handling; nye servicekoncepter prøvekørt på "
     "én kunde, før de bliver standard."),
    ("Lønsom drift",
     "Dækningsgrad pr. kontrakt og pr. sag, faktureringsgrad og prognose — service skal tjene "
     "penge, ikke kun løse opgaver."),
    ("Integration og processer",
     "Én aftalemodel, én dokumentationspraksis og én måde at lukke en sag på, når eksisterende "
     "serviceaktiviteter lægges sammen."),
]

MODELS = [
    ("Servicekatalog",
     "Ydelse, responstid, pris og grænseflade pr. fag — grundlaget for både salg og leverance"),
    ("Kontraktkort",
     "Pr. kunde: ydelser, KPI-formel, datakilde, grænseværdi, bod og dækningsgrad"),
    ("Kapacitetsmodel",
     "Timer, fag og certifikater pr. uge — teknikerkapaciteten bygges op foran ordrebogen"),
    ("Vækstpipeline",
     "Næste aftale pr. kunde med ejer, værdi og næste handling; nye koncepter prøvekørt på én "
     "kunde"),
    ("Servicerapport",
     "Månedligt på få tal: aftaler indgået, omsætning, dækningsgrad, responstider og næste "
     "beslutning"),
    ("Integrationsplan",
     "Eksisterende serviceaktiviteter samlet i én aftalemodel og én dokumentationspraksis — med "
     "milepæle og ejer"),
]

ACHIEVEMENTS = [
    ("Serviceforretning bygget fra bunden",
     "ELOHVAC: 5 elektrikere og 3 lærlinge, 40+ serviceanlæg, eget kundekartotek, serviceaftaler "
     "med responstider og fuldt ansvar for dækningsgrad og bundlinje."),
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
     "Anvendt i drift, produktion og projekter · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og projekter · 2017 – nu"),
]

LANGUAGES = ("Dansk (modersmål, skrift og tale) · Engelsk (professionelt, skrift og tale) · "
             "Persisk/farsi · Kørekort B (kategori B)")

PRACTICAL_CV = (
    "Bosat i Måløv — cirka 3 timer i bil til Esbjerg. Indstillet på fast ugentlig tilstedeværelse i "
    "Esbjerg og på at være synlig der i starten; åben for at drøfte en ordning med bopæl tættere på "
    "Fredericia eller Odense. Kørekort kategori B og bil, dansk på modersmålsniveau og engelsk "
    "professionelt. Kan tiltræde hurtigst muligt."
)

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Biofos (Lynetten), Novo Nordisk A/S, "
              "Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Teknikerne og de kommende servicemedarbejdere",
     "Skreven forventningsaftale og kompetenceplan, fast kadence og et tavlemøde, hvor sikkerhed og "
     "dagens opgaver ligger åbent — kapaciteten skal bygges med folk, der vil blive."),
    ("Kunderne i marine, industri og energi",
     "Kvartalsgennemgang med KPI'er, hændelser og forslag til næste sæsons arbejde — vi skal komme "
     "før nedbruddet, ikke efter regningen."),
    ("MIE-ledelsesteamet og de øvrige forretningsområder",
     "Én månedlig rapport på få tal og en skreven snitflade, så den samme kunde ikke får to "
     "forskellige tilbud — fælles ressourcer prioriteret åbent."),
    ("Head of MIE og de øvrige ledere i Caverion",
     "Aftalte eskaleringsgrænser og et klart oplæg, når der skal besluttes investering i kapacitet "
     "eller nye koncepter."),
]

FIRST90 = [
    ("Dage 1–30",
     "Gennemgået alle eksisterende serviceaftaler og kunder med den ansvarlige: hvad er lovet, "
     "hvad er prissat, hvor taber vi penge, og hvilke kunder har en næste aftale i sig. Været "
     "synlig i Esbjerg og talt med teknikerne om, hvad der driller i hverdagen."),
    ("Dage 30–60",
     "Servicekatalog og kontraktkort på plads for de aftaler, der betyder mest; kapacitetsmodel "
     "lagt pr. uge; vækstpipeline med de første ti kunder; første månedlige servicerapport til "
     "Head of MIE."),
    ("Dage 60–90",
     "Integrationsplan for de eksisterende serviceaktiviteter med milepæle og ejer; ét nyt "
     "servicekoncept prøvekørt på én kunde; afvigelsesliste i brug og dækningsgraden kendt pr. "
     "kontrakt."),
    ("Måned 3–6",
     "Aftaleporteføljen vokser med lønsomme aftaler, teknikerkapaciteten følger ordrebogen, og "
     "processerne er ens — også når der kommer nye kunder ind fra Fredericia og Odense."),
    ("Måned 6–12",
     "Afdelingen er en forretning med kendt dækningsgrad, stabil leverance og en salgsmaskine, der "
     "kan skaleres sammen med resten af MIE."),
]

KEYWORDS = (
    "Afdelingschef · Caverion · Marine, Industri og Energi · MIE · Esbjerg · Fredericia · Odense · "
    "Serviceafdeling · Serviceforretning · Serviceaftaler · Tekniske servicekontrakter · "
    "Servicekoncepter · Kundetilfredshed · Kvalitet · Lønsom drift · Dækningsgrad · Omsætning · "
    "Vækst · Vækstmuligheder · Kommercielle kompetencer · Kundeudvikling · Kunderelationer · "
    "Langsigtede relationer · Tilbudsarbejde · Salgsaktiviteter · Forretningsudvikling · Drift · "
    "Processer · Skalerbarhed · Organisering · Teknikerkapacitet · Personaleledelse · Følgeskab · "
    "Engagement · Selvstændighed · Handlekraft · Initiativ · Resultatorienteret · Struktureret · "
    "Samarbejde på tværs · Marine · Industri · Energi · Offshore · Grøn omstilling · El-teknisk · "
    "Højspænding · CTS · Maskinmester · Lean · SAP"
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

    m.models_table("SERVICEAFDELINGENS STYRING — ANVENDT I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER SERVICEAFDELINGEN I RYTMEN",
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
    out = os.path.join(ROOT, "Shahram_Ajloo_Caverion_AfdelingschefMIE.docx")
    build(out)
    print("OK " + out)
