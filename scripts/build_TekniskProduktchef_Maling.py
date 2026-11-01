# -*- coding: utf-8 -*-
"""
Teknisk produktchef — maling og overfladebehandling til det professionelle marked (Søborg).
Rekrutteres via Curia. Dansk JD. Opgave-først side 1 + CV + 90 dage/parter i ét dokument.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Teknisk produktchef | Produktudvikling, test og teknisk dokumentation | Byggematerialer"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = "Produktafdelingen · Søborg · via Curia, att. Bo Prangsgaard"
SUBJECT = "Ansøgning: Teknisk produktchef — maling og handelsvarer til det professionelle marked"

# ------------------------------------------------------------------ side 1
INTRO = [
    "En teknisk produktchef i maling og overfladebehandling skal kunne tre ting på samme tid: "
    "læse markedet og håndværkeren, holde styr på hvad et produkt faktisk kan præstere, og gøre den "
    "viden brugbar for salg, indkøb, produktion og kunder. Det er ikke et formidlingsjob alene — det "
    "er et dokumentations- og beslutningsjob, hvor den tekniske påstand skal kunne stå for en test, "
    "og hvor den gode idé først er noget værd, når den er prissat, prøvet og skrevet ned.",

    "Nedenfor er systemet, der står klar fra første dag: sortimentskort pr. vare med teknisk "
    "position, pris og livsfase; test- og benchmarkprotokol med acceptkriterier; "
    "dokumentationsmodel med versionsstyrelse; lanceringsmodel med gate-review; og en "
    "supportsagsmodel, hvor hver reklamation bliver til data.",
]

BULLETS = [
    ("Kravet: følge markedet for maling og tilbehør og omsætte kundebehov og markedstendenser til "
     "konkrete produktønsker",
     "Løsningen er en fast rytme, hvor markedet bliver til krav: kundebesøg og håndværkerdialog "
     "hvert kvartal, en konkurrentbenchmark pr. produktkategori, og et produktønske der altid "
     "formuleres med kundebehov, teknisk krav, volumenforventning og ét acceptkriterium. Jeg har "
     "bygget en serviceforretning ved at spørge kunderne, hvad de faktisk havde brug for."),

    ("Kravet: bistå udvikling og indkøb med afprøvning, test og benchmarking af produkter",
     "Løsningen er en testprotokol, der kan gentages: hvad der prøves, på hvilket underlag, ved "
     "hvilken temperatur og fugtighed, med hvilken metode og hvilket acceptkriterium — og en "
     "benchmark, der altid kører det nye produkt side om side med det, vi sælger i dag. I "
     "GMP-reguleret drift har jeg dokumenteret 37 anlægsprojekter med FAT/SAT og IQ/OQ/PQ — samme "
     "disciplin gælder en testrække."),

    ("Kravet: følge salget af sortimentet og bidrage med teknisk indsigt i produktudvikling og "
     "lanceringer",
     "Løsningen er et sortimentskort pr. vare med omsætning, dækningsgrad, vækst, lagerbinding og "
     "livsfase — gennemgået hver måned — så beslutningen om at udfase, videreudvikle eller lancere "
     "bygger på tal og ikke på den, der råber højest. Jeg har drevet egen virksomhed med fuldt "
     "P&L og ved, hvad en vare koster at holde på lageret."),

    ("Kravet: vedligeholde tekniske datablade, anvisninger og produktbrochurer på høj faglig og "
     "korrekt standard",
     "Løsningen er en dokumentationsmodel med fast skabelon: hvem der ejer dokumentet, hvilken "
     "standard og testmetode der henvises til, hvornår det skal revideres, og hvordan en ændring "
     "slår igennem alle sprog og kanaler. Dokumentation uden ejer og revisionsdato er forkert inden "
     "for et år."),

    ("Kravet: udarbejde undervisningsmateriale og gennemføre intern og ekstern undervisning i "
     "produkter og anvendelse",
     "Løsningen er et undervisningskoncept bygget på tre niveauer — hvad produktet er, hvornår det "
     "skal bruges, og hvad der går galt — med øvelser, fejlshow og en kort prøve til sidst. Jeg har "
     "oplært 3 lærlinge og et 14-mands team og stået for intern undervisning i sikkerhed og "
     "arbejdsgange — det, der bliver husket, er det, deltagerne selv har prøvet."),

    ("Kravet: yde teknisk support til salg og kunder samt bidrage i dialogen med leverandører ved "
     "lanceringer, udviklingsprojekter og reklamationer",
     "Løsningen er en supportsagsmodel: hver henvendelse registreres med produkt, anvendelse, "
     "underlag og årsag, løses inden for aftalt tid og gøres op månedligt — så reklamationer bliver "
     "til produktforbedringer i stedet for enkeltsager. Garantisager og leverandørdialog har jeg "
     "håndteret i fem år."),

    ("Kravet: struktureret og analytisk arbejde med naturlig opfølgning på projekter",
     "Løsningen er en projektliste på én side: hvad, hvem, hvornår, hvad er blokeret, og næste "
     "beslutning — gennemgået hver uge. Jeg har koordineret 11 samtidige entrepriser og 37 "
     "anlægsprojekter; det, der ikke står på listen med en dato, bliver ikke gjort."),

    ("Kravet: formidle tekniske emner klart på dansk og engelsk og tale til større forsamlinger",
     "Løsningen er at skrive og tale i samme rækkefølge: hvad er problemet, hvad gør produktet, "
     "hvad siger dokumentationen, og hvad skal kunden gøre nu. Jeg har præsenteret for styregrupper, "
     "leverandører og håndværkere — og holder gerne oplæg for 50 mand."),

    ("Kravet: teknisk nysgerrighed kombineret med kommerciel forståelse og fokus på kundens behov",
     "Løsningen er at regne på sagen, før man anbefaler den: hvad koster produktet at føre, hvad "
     "giver det pr. m² og pr. år, og hvad vælger kunden i morgen. Jeg bygger selv modellerne i "
     "Excel, Power BI og Python og bruger Claude dagligt til at gøre analyse, dokumentudkast og "
     "beregninger færdige på en time i stedet for en dag."),
]

SYSTEM = (
    "Systemet står klar fra første dag: sortimentskort med pris, dækningsgrad og livsfase; test- og "
    "benchmarkprotokol med acceptkriterier; dokumentationsmodel med ejer og versionsstyrelse; "
    "lanceringsmodel med gate-review; supportsagsmodel med reklamationsstatistik — ført i Excel og "
    "Power BI, med datablade og analyser udarbejdet i Python og Claude."
)

MIRROR = (
    "Om kravene: elautoriseret maskinmester (LV/MV/HV) og B.Tech med 20 år i tekniske anlæg og "
    "materialer — 37 anlægsprojekter uden kritiske fund, fem år som driftschef med ansvar for "
    "tekniske krav, leverandører og garantisager, egen virksomhed med fuldt P&L og undervisning af "
    "lærlinge og teknikere."
)

HONEST = (
    "Det skal siges ligeud: jeg har ikke arbejdet i maling- eller overfladeindustrien, og jeg har "
    "ikke stået for et sortiment af maling og handelsvarer til det professionelle marked. Min "
    "baggrund er elektriske og mekaniske anlæg, dokumentation og kvalitetsstyring, og mine kunder "
    "har været industri, forsyning, pharma og håndværkere. Det, jeg bringer, er metoden: at gøre en "
    "teknisk påstand målbar, dokumentere den og formidle den til dem, der skal sælge og bruge "
    "produktet."
)

CULTURE = (
    "Huset i Søborg er et af de ældste navne i dansk farve- og overfladebehandling — grundlagt i "
    "1928, med rustbeskyttelsen Stålhud til de første store broer og senere produkter, håndværkere i "
    "dag kender ved navn. Her er produkterne ikke ligegyldige: en fejl på et datablad får "
    "konsekvenser på en byggeplads, og omtalen går gennem malere. Kulturen er fri og uformel med "
    "korte beslutningsveje og høj faglighed — derfor kommer jeg med tal og testresultater."
)

PRACTICAL = (
    "Bosat i Måløv — cirka 20 minutter i bil til Søborg, med kendskab til håndværkermiljøerne i "
    "Storkøbenhavn fra egen virksomhed og fra driften. Kørekort B og bil. Kan tiltræde hurtigst "
    "muligt."
)

CLOSING = (
    "I første samtale vil jeg gerne tale om, hvilke produkter der i dag bærer omsætningen, og "
    "hvilke der bærer dokumentationen — og hvordan I afgør, om et nyt produkt skal ind i "
    "sortimentet."
)

# ------------------------------------------------------------------ CV
PROFILE = (
    "Elautoriseret maskinmester (LV/MV/HV) og B.Tech med 20 år i tekniske anlæg, materialer og "
    "kvalitetsstyring. Har dokumenteret 37 anlægsprojekter uden kritiske fund, været driftschef med "
    "ansvar for tekniske krav, leverandører og garantisager, ledet 14 mand med 11 samtidige "
    "entrepriser og bygget egen virksomhed med fuldt P&L. Arbejder med sortiments- og "
    "produktanalyser, test- og benchmarkprotokoller, teknisk dokumentation og undervisning — og "
    "bygger selv analyserne i Excel, Power BI og Python."
)

PRACTICE = [
    ("Marked og produktønsker",
     "Kundebesøg og håndværkerdialog hvert kvartal, konkurrentbenchmark pr. kategori og et "
     "produktønske formuleret med kundebehov, teknisk krav, volumen og acceptkriterium."),
    ("Test og benchmarking",
     "Testprotokol med underlag, klima, metode og acceptkriterium — og altid side om side med det "
     "produkt, vi sælger i dag."),
    ("Sortiment og salgsopfølgning",
     "Sortimentskort pr. vare med omsætning, dækningsgrad, vækst, lagerbinding og livsfase — "
     "grundlag for at udfase, videreudvikle eller lancere."),
    ("Teknisk dokumentation",
     "Fast skabelon med ejer, standardhenvisning, revisionsdato og ændringslog — så datablade, "
     "anvisninger og brochurer er korrekte på alle sprog."),
    ("Undervisning og formidling",
     "Tre niveauer: hvad produktet er, hvornår det bruges, og hvad der går galt — med øvelser, "
     "fejlshow og prøve; holdt for lærlinge, teknikere og leverandører."),
    ("Support og reklamationer",
     "Supportsag med produkt, anvendelse, underlag og årsag, løst inden for aftalt tid og gjort op "
     "månedligt som statistik — reklamationer bliver til produktforbedringer."),
]

MODELS = [
    ("Sortimentskort",
     "Pr. vare: teknisk position, pris, dækningsgrad, vækst, lagerbinding og livsfase"),
    ("Produktønske",
     "Kundebehov, teknisk krav, volumenforventning og acceptkriterium på én side"),
    ("Test- og benchmarkprotokol",
     "Underlag, klima, metode, acceptkriterium — og referenceprodukt kørt side om side"),
    ("Lanceringsmodel",
     "Gate-review: produktkrav, dokumentation, pris, undervisning og support klar før lancering"),
    ("Dokumentationsmodel",
     "Ejer, standardhenvisning, revisionsdato og ændringslog pr. datablad og anvisning"),
    ("Reklamationsstatistik",
     "Årsagskode, produkt, anvendelse og lukketid — gjort op månedligt som forbedringsgrundlag"),
]

ACHIEVEMENTS = [
    ("37 anlægsprojekter uden kritiske fund",
     "2-10 mio. kr. i industriel og GMP-reguleret drift: FAT/SAT, IQ/OQ/PQ, teknisk dokumentation "
     "og aflevering — 25 specialister koordineret på tværs af mekanik, el, proces og indkøb."),
    ("Nul uplanlagte stop i fem år",
     "24/7-anlæg med højspænding, koblingsanlæg, pumper, HVAC og køl — planlagt og tilstandsbaseret "
     "vedligehold, KPI'er i SAP og leverandør- og garantisager fulgt til lukning."),
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
     [("Produkt, pris og kunder",
       "servicekatalog med ydelsesbeskrivelser, prissætning, aftaler pr. kunde og leverandøraftaler "
       "med fuldt ansvar for dækningsgrad og bundlinje."),
      ("Organisation, sikkerhed og oplæring",
       "byggede virksomheden op fra bunden: rekruttering, oplæringsplaner, undervisning i sikkerhed "
       "og arbejdsgange samt arbejdsplaner.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2-10 mio. kr. · 25 specialister · GMP/FDA/EMA",
     [("Koordinering, snitflader og aflevering",
       "25 specialister koordineret på tværs af mekanik, el, proces og indkøb; fremdrift og "
       "rapportering til styregruppe; FAT/SAT, IQ/OQ/PQ og aflevering uden kritiske fund."),
      ("Dokumentation og ændringshåndtering",
       "ændringshåndtering og teknisk dokumentation, der bestod revision — og overlevering til "
       "drift med skrevne grænseflader.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7-anlæg · højspænding, koblingsanlæg, pumper, HVAC og køl · budget i SAP",
     [("Drift, vedligehold og driftssikkerhed",
       "planlagt og tilstandsbaseret vedligehold, KPI'er i SAP og nul uplanlagte stop i fem år på "
       "et anlæg, hvor driften ikke kunne vente."),
      ("Leverandører, garantisager og beredskab",
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
    "Bosat i Måløv — cirka 20 minutter i bil til Søborg. Kørekort kategori B og bil, dansk på "
    "modersmålsniveau og engelsk professionelt. Kan tiltræde hurtigst muligt."
)

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Biofos (Lynetten), Novo Nordisk A/S, "
              "Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Produkt- og indkøbschefen",
     "Produktønske på én side med kundebehov, teknisk krav, volumen og acceptkriterium — så "
     "beslutningen kan tages på et grundlag, ikke på en fornemmelse."),
    ("Salg, kunder og det professionelle marked",
     "Teknisk support med aftalt svartid og en fast runde hos malere og forhandlere — produktet "
     "skal kunne forklares på en byggeplads, ikke kun i et datablad."),
    ("Udvikling, indkøb og leverandører",
     "Test- og benchmarkresultater som fælles sprog ved lanceringer, udviklingsprojekter og "
     "reklamationer — og en klar eskalering, når et produkt ikke lever op til det aftalte."),
    ("Produktion og marketing",
     "Dokumentation, undervisningsmateriale og produktpåstande, der er godkendt teknisk, før de "
     "går ud — så salg og produktion taler om det samme produkt."),
]

FIRST90 = [
    ("Dage 1–30",
     "Lært sortimentet at kende vare for vare og talt med salg, produktion, indkøb og marketing om, "
     "hvor de oplever, at produkterne svigter. Været ude hos malere og forhandlere og hørt, hvordan "
     "produkterne faktisk bliver brugt."),
    ("Dage 30–60",
     "Sortimentskort og salgsopfølgning på plads pr. vare; test- og benchmarkprotokol skrevet ned; "
     "dokumentationsmodellen gennemgået med ejer og revisionsdato pr. datablad; supportsagsmodel i "
     "brug."),
    ("Dage 60–90",
     "De første tre produkter testet og benchmarket mod reference; undervisningsmateriale på niveau "
     "1 klar og afprøvet internt; lanceringsmodel med gate-review på plads for de næste "
     "produktprojekter."),
    ("Måned 3–6",
     "Sortimentet er gennemgået med beslutning pr. vare, dokumentationen er opdateret og entydig, og "
     "salg og kunder oplever en teknisk support, der svarer inden for aftalt tid."),
    ("Måned 6–12",
     "Et produktønske fra markedet er ført hele vejen til lancering på et dokumenteret grundlag, og "
     "videndelingen om produkterne er blevet en fast del af husets måde at arbejde på."),
]

KEYWORDS = (
    "Teknisk produktchef · Maling · Overfladebehandling · Byggematerialer · Handelsvarer · "
    "Professionelt marked · Produktafdeling · Produkt- og indkøbschef · Marked · Markedstendenser · "
    "Kundebehov · Produktønsker · Udvikling · Indkøb · Afprøvning · Test · Benchmarking · "
    "Produktydelse · Anvendelsesforhold · Sortiment · Salgsopfølgning · Produktudvikling · "
    "Lanceringer · Teknisk datablad · Anvisninger · Produktbrochurer · Faglig standard · "
    "Undervisningsmateriale · Intern undervisning · Ekstern undervisning · Teknisk support · "
    "Leverandører · Reklamationer · Struktureret · Analytisk · Opfølgning · Projekter · Formidling · "
    "Dansk · Engelsk · Undervisning · Produktpræsentationer · Kundemøder · Samarbejde på tværs · "
    "Teknisk nysgerrighed · Kommerciel forståelse · Kundeoplevelse · Ingeniør · Maskinmester · "
    "Håndværkermiljøer · Byggepladser · Kvalitetsstyring · Dokumentation · Lean · KPI · ERP · "
    "Power BI · Python · Claude"
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
    m.resume_header(NAME, TITLE, CONTACT, "FAGLIG PROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("PRODUKTARBEJDETS STYRING — ANVENDT I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER PRODUKTARBEJDET I RYTMEN",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN ARBEJDES DER — DE FIRE PARTER")
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
    out = os.path.join(ROOT, "Shahram_Ajloo_TekniskProduktchef_Maling.docx")
    build(out)
    print("OK " + out)
