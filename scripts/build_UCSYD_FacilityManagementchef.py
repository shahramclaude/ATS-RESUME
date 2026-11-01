# -*- coding: utf-8 -*-
"""
UC SYD — Facility managementchef.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Facility managementchef | Bygningsdrift, rengøring og skemalægning | Syd- og Sønderjylland"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = ("UC SYD · att. ressourcedirektør Stine Bilstrup Rask · via Genitor, "
             "partner Jesper Lund Madsen")
SUBJECT = "Ansøgning: Facility managementchef"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Facility Managementområdet bliver et nyt chefområde med ca. 65 ledere og medarbejdere, ca. 32 "
    "mio. kr. og tre opgaver, der hidtil har levet hver for sig: bygningsdrift, rengøring og "
    "skemalægning på fire campusser. Opgaven er ikke at gøre de tre ens, men at gøre dem til ét "
    "område, hvor den fælles standard kan mærkes ude på den enkelte campus — i et lokale der passer "
    "til simulation, i et rent og driftssikkert hus, i et skema der hænger sammen med lokalerne.",

    "Nedenfor er min motivation og ledelsesmæssige tilgang samt det system, der står klar fra første "
    "dag: driftsaftale pr. campus, fælles ledergruppe med beslutningslog, tilstandsbaseret "
    "vedligeholdelses- og investeringsplan, kapacitets- og lokaleoverblik og en prioriteret "
    "digitaliseringsrækkefølge.",
]

BULLETS = [
    ("Kravet: samle et nyt chefområde med meget forskellige fagligheder og lokale kulturer",
     "Løsningen er at skrive retningen ned først: et formål, tre til fem fælles standarder og en "
     "beslutningsmodel for, hvad der løses lokalt, og hvad der løftes fælles. Jeg har selv bygget en "
     "virksomhed op og samlet teknikere, montører og leverandører om de samme standarder."),

    ("Kravet: sikre en stabil, professionel og serviceorienteret daglig drift",
     "Løsningen er en driftsaftale pr. campus med svartider, kvalitetskrav og faste tilsyn — og "
     "opfølgning på det, brugerne oplever: reaktionstid, gentagne fejl og rengøringskvalitet. Jeg har "
     "haft driftsansvar på et 24/7-anlæg med nul uplanlagte stop."),

    ("Kravet: lede gennem andre — ca. 65 ledere og medarbejdere via rengøringsledere, "
     "campuskoordinatorer og administrativ leder",
     "Løsningen er ledelseskadence frem for kontrol: ledelsesaftaler med to-tre punkter, fast "
     "ledergruppe med beslutningslog og faste campusdage, så nærværet er planlagt og ikke "
     "tilfældigt. Jeg har koordineret 25 specialister på tværs af fag."),

    ("Kravet: kombinere nærhed til hverdagen med stærkere fælles koncepter og standarder",
     "Løsningen er rækkefølgen: en fælles løsning prøvekøres på én campus, justeres sammen med de "
     "lokale, får en navngiven ejer og en gevinstmåling — og meldes først derefter ud som standard. "
     "Prøvede standarder bliver brugt; pålagte bliver omgået."),

    ("Kravet: styrke den langsigtede bygningsdrift med planlagt vedligehold, klimasikring og "
     "investeringsplaner",
     "Løsningen er en tilstands- og kritikalitetsbaseret vedligeholdelsesplan koblet til en flerårig "
     "investeringsplan med levetid, konsekvens og alternativ pr. sag — med klimasikring som fast "
     "screeningspunkt. Jeg har arbejdet med tilstandskontrol og budget i SAP på anlæg, hvor nedbrud "
     "havde en pris."),

    ("Kravet: drive udvikling gennem digitalisering, AI og teknologiske hjælpemidler",
     "Løsningen er rækkefølgen data → arbejdsgang → værktøj: først måling af rengøring, nedbrud og "
     "lokaleudnyttelse, så en arbejdsgang der virker, og derefter et system. Jeg koder selv i Python "
     "og bruger Claude dagligt — AI skal skåne medarbejderne, ikke være et projekt."),

    ("Kravet: lede Team Skema og sammenhængen mellem skemalægning, lokaleallokering og "
     "kapacitetsudnyttelse",
     "Løsningen er et kapacitetsregnskab pr. campus og lokale og et fast møde med uddannelserne, hvor "
     "konsekvensen af en ændring er regnet igennem først. Jeg har ikke selv skemalagt, men planlagt "
     "kapacitet for 14 mand og 11 samtidige projekter — og ved, hvad det koster at love mere, end "
     "der er plads til."),

    ("Kravet: ansvar for sikkerhed, kriseberedskab og et arbejdsmiljø med faglig stolthed",
     "Løsningen er beredskabsplaner med roller og faste øvelser, arbejdstilladelser og LOTO i "
     "praksis og nærved-hændelser behandlet uden skyld — som driftsdata. Jeg er uddannet i "
     "arbejdsmiljø (§16) og har haft ansvaret i 24/7-drift og egen virksomhed."),

    ("Kravet: løfte Facility Management til en strategisk medspiller i Strategi 2030 — med grøn "
     "omstilling, økonomi og leverandørstyring",
     "Løsningen er at koble FM's viden til kerneopgaven: lokaler til simulation og fleksible "
     "studiemiljøer, rengøring og indeklima som del af studiedagen, energiledelse pr. bygning og "
     "udbud med KPI- og bæredygtighedskrav. Jeg bringer tallene ind i ledelsen som "
     "beslutningsgrundlag — ikke som status."),
]

SYSTEM = (
    "Systemet står klar fra dag ét: driftsaftale pr. campus, ledergruppe med beslutningslog, "
    "tilstandsbaseret vedligeholdelses- og investeringsplan, kapacitets- og lokaleoverblik og "
    "månedlig økonomi- og driftsrapport — ført i Excel og Power BI sammen med UC SYDs fagsystemer, "
    "med rapporter og oplæg genereret i Python og Claude."
)

MIRROR = (
    "Om kravene: 20 år i tekniske anlæg og otte år med personaleansvar i et bredt drifts-, service- "
    "eller facility managementområde — 14-mands team med 11 samtidige opgaver, 5 elektrikere og 3 "
    "lærlinge med fuldt P&L, 25 specialister koordineret på tværs af fag og fem år som drifts- og "
    "vedligeholdelseschef i et kommunalt ejet selskab med bestyrelse, budget i SAP og 24/7-drift. "
    "Elautoriseret maskinmester (LV/MV/HV), B.Tech."
)

HONEST = (
    "Tre ting skal siges ligeud: jeg har ikke ledet 65 medarbejdere gennem flere ledelsesniveauer i "
    "en uddannelsesinstitution, jeg har ikke selv stået med skemalægning, og rengøring som fag har "
    "jeg ikke ledet. Til gengæld har jeg ledet fag, jeg ikke selv udførte, og stået med bygningsdrift, "
    "økonomi, leverandører og beredskab. Jeg bor i Måløv — cirka tre timer fra Esbjerg — og er "
    "indstillet på fast base i Esbjerg og ugentlig tilstedeværelse på alle campusser."
)

CULTURE = (
    "Strategi 2030 siger, at praksis kommer først, og at fokus skal flyttes fra det, der måles, til "
    "det, der mærkes. Det er en gave til et FM-område: et lokale der passer til undervisningen, et "
    "hus der er rent og driftssikkert, og et skema der hænger sammen er netop kvalitet, der mærkes. "
    "»Med hoved, hånd og hjerte« rammer den faglighed, der findes i pedel- og rengøringsområdet."
)

PRACTICAL = (
    "Bosat i Måløv med cirka tre timer til Esbjerg; kørekort B og bil. Kan tiltræde 1. februar 2027 "
    "og deltager gerne i testforløb (NEO-PI-3 og IST-Screening) og referencetagning."
)

CLOSING = (
    "I første samtale vil jeg gerne tale om, hvad der bliver mærkbart på en campus den 1. februar."
)

# ------------------------------------------------------------------ CV
PROFILE = (
    "Chef med 20 år i tekniske anlæg og otte år med personaleansvar — heraf fem år som drifts- og "
    "vedligeholdelseschef i et kommunalt ejet selskab med bestyrelse, budget i SAP og 24/7-drift, og "
    "to år med egen virksomhed og fuldt P&L. Har ledet drifts- og serviceorganisationer med brugere "
    "tæt på, bygget et område op fra bunden og indført standardarbejde, dataunderstøttet "
    "prioritering og digitalisering i praksis. Elautoriseret maskinmester (LV/MV/HV), B.Tech og Lean."
)

PRACTICE = [
    ("Samling af et nyt chefområde",
     "Formål, fælles standarder og beslutningsmodel for lokalt/fælles på plads inden 90 dage — "
     "gennemført som projekt med milepæle og ejer på hver beslutning."),
    ("Drift og service tæt på brugerne",
     "Driftsaftale pr. campus med svartider og kvalitetskrav; tilsyn og brugerdialog gennem "
     "campuskoordinatorerne. Fra drift: aftalte responstider og nul uplanlagte stop i fem år."),
    ("Ledelse gennem andre",
     "Ledelsesaftaler, fast ledergruppe med beslutningslog, faste campusdage og oplæring med to "
     "personer pr. kritisk kompetence."),
    ("Bygningsdrift og investeringer",
     "Tilstands- og kritikalitetsbaseret vedligeholdelsesplan, flerårig investeringsplan med levetid "
     "og konsekvens, klimasikring som screeningspunkt og månedlig prognose."),
    ("Digitalisering og AI",
     "Data → arbejdsgang → værktøj: måling af rengøring, nedbrud og lokaleudnyttelse, dashboards og "
     "AI-genererede rapporter og instrukser; selvkodet i Python og Claude dagligt."),
    ("Økonomi, udbud og leverandører",
     "Budget og prognose med fuldt ansvar, udbud og kontrakter med KPI- og bæredygtighedskrav, "
     "leverandøropfølgning og rapportering til styregrupper og bestyrelse."),
]

MODELS = [
    ("Driftsaftale pr. campus",
     "Ydelser, svartider, kvalitetskrav og hvad den lokale enhed selv gør — gennemgået hvert "
     "halvår med campuskoordinator og brugerrepræsentanter"),
    ("Ledergruppe",
     "Fast møde med beslutningslog: hvad er besluttet, af hvem, hvornår, og hvad gør vi, hvis det "
     "ikke holder — plus faste campusdage i kalenderen"),
    ("Vedligehold og investering",
     "Tilstand og kritikalitet pr. bygning (sikkerhed, drift, brugerpåvirkning) koblet til flerårig "
     "investeringsplan med levetid og konsekvens"),
    ("Kapacitet og lokaler",
     "Lokaleudnyttelse og kapacitet pr. campus som månedstal, drøftet med uddannelserne før "
     "semesterstart"),
    ("Sikkerhed og beredskab",
     "Beredskabsplaner med roller, øvelser i kalenderen, arbejdstilladelser og LOTO samt "
     "nærved-hændelser fulgt til lukning"),
    ("Digitalisering",
     "Prioriteret rækkefølge med gevinstmåling: data før system, prøvekørsel på én campus før "
     "udrulning; rapporter genereret i Python og Claude"),
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
     "2–10 mio. kr. hos Novo Nordisk med 25 specialister koordineret på tværs af mekanik, el, "
     "proces og indkøb — dokumentation der bestod revision."),
]

EXPERIENCE = [
    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7-anlæg · pumper, HVAC, køl, koblingsanlæg og højspænding · budget i SAP",
     [("Drift, vedligehold og driftssikkerhed",
       "planlagt vedligehold, tilstandskontrol og KPI'er i SAP; nul uplanlagte stop i fem år på et "
       "anlæg, hvor driften ikke kunne vente — i en kommunalt ejet virksomhed med bestyrelse."),
      ("Sikkerhed, leverandører og beredskab",
       "koordinering af egne teknikere, entreprenører og rådgivere — LOTO, arbejdstilladelser, "
       "garantisager og nærved-hændelser fulgt til lukning.")]),

    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og leverandøraftaler",
     [("Organisation, rekruttering og arbejdsmiljø",
       "byggede virksomheden op fra bunden: rekruttering, oplæringsplaner og arbejdsplaner, "
       "sikkerhed og arbejdsmiljø som fast punkt."),
      ("Økonomi og kunder",
       "tilbudsberegning, indkøb og leverandøraftaler, plan og prognose med fuldt ansvar for "
       "bundlinjen.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Personale, kapacitet og service",
       "14-personers team med kapacitetsplanlægning, daglige tavlemøder og opfølgning på den enkelte "
       "— og 11 samtidige entrepriser i eksisterende byggeri med brugere omkring os.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister · GMP/FDA/EMA",
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

PRACTICAL_CV = ("Bosat i Måløv — cirka tre timer til Esbjerg; kørekort kategori B og bil. Fast base i "
                "Esbjerg og ugentlig tilstedeværelse på alle fire campusser. Dansk på "
                "modersmålsniveau og engelsk professionelt. Kan tiltræde 1. februar 2027.")

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Biofos (Lynetten), Novo Nordisk A/S, "
              "Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Lederne og medarbejderne i området",
     "Ledelsesaftaler, fast ledergruppe med beslutningslog og faste campusdage — og en chef der "
     "tager de svære sager, så de ikke lander hos den enkelte pedel."),
    ("Campusser og uddannelser",
     "Driftsaftale og kapacitetsmøde pr. campus, hvor lokaler, skema og service ses som én "
     "sammenhæng — og hvor ændringer er regnet igennem, før de meldes ud."),
    ("Direktion, chefgruppe og Fællesområdet",
     "FM's viden om bygninger og hverdag bragt ind i chefgruppen og Ledelsesdialogforum som "
     "beslutningsgrundlag — ikke som status."),
    ("De studerende",
     "Rene, driftssikre og levende rammer, åbningstider der passer til studiedagen og en service, "
     "der svarer, når man henvender sig."),
]

FIRST90 = [
    ("Dage 1–30",
     "Mødt alle ledere og været på alle fire campusser; gennemgået den nye organisering, "
     "driftsopgaverne, Team Skemas kalender og de aftaler, der allerede er indgået."),
    ("Dage 30–60",
     "Fælles formål og tre til fem standarder drøftet med ledergruppen; driftsaftale pr. campus "
     "udkastet; datagrundlag på plads: nedbrud, rengøringskontrol, svartider og lokaleudnyttelse."),
    ("Dage 60–90",
     "Tilstandsbaseret vedligeholdelsesplan og flerårig investeringsplan fremlagt for "
     "ressourcedirektøren; første digitaliseringstiltag prøvekørt på én campus; trivselsmåling "
     "gennemført."),
    ("Måned 3–6",
     "Driftsaftaler gældende på alle campusser; kapacitetsmøde med uddannelserne før semesterstart; "
     "energi- og rengøringsdata i fast månedsrapport."),
    ("Måned 6–12",
     "FM leverer på svartider og kvalitet, investeringsplanen er beslutningsklar, og de fælles "
     "løsninger opleves som hjælp ude på campusserne — ikke som afstand."),
]

KEYWORDS = (
    "Facility managementchef · Chefområde · Facilitetsdrift · Bygningsdrift · Rengøring · "
    "Skemalægning · Team Skema · Campusmiljøer · Campusser · Esbjerg · Kolding · Haderslev · "
    "Aabenraa · Tønder · Studerende · Medarbejdere · Ledere og medarbejdere · UC SYD · "
    "Strategi 2030 · UC SYDs samlede ledelse · Chefgruppen · Ledelsesdialogforum · Fællesområdet · "
    "Ressourcedirektør · Direktion · Chefer · Uddannelser · Nærværende, tydelig og involverende "
    "ledelse · Fagligheder · Lokale kulturer · Fælles retning · Stabil, professionel og "
    "serviceorienteret drift · Service · Arbejdsmiljø · Fælles funktioner · Nærhed til hverdagen · "
    "Fælles koncepter og standarder · Langsigtet bygningsdrift · Planlagt vedligehold · "
    "Investeringsplaner · Prioriteringer · Prioriteringerne · Digitalisering · AI · Teknologiske hjælpemidler · "
    "Faglig stolthed · Følgeskab · Forandring · Samarbejde · Involvering · Sammenhængskraft · "
    "Sammenhæng på tværs · Fysiske rammer · Driftssikkerhed · Ledelseserfaring · "
    "Ledelse gennem andre · Økonomi · Leverandørstyring · Grøn omstilling · Forandringsprocesser · "
    "Teknologiforståelse · Offentligt styret organisation · Tillid · Dialog og deltagelse · "
    "Beslutninger · Beslutningskraft · Organisatorisk tæft · Pedelområdet · Byggetekniker · "
    "Konsulenter · Rengøringsledere · Campuskoordinatorer · Administrativ leder · Pedeller · "
    "Studentermedhjælpere · Lokaleallokering · Kapacitetsudnyttelse · Sikkerhed og kriseberedskab · "
    "Klimasikring · Udbud · Kontrakter · Skemasystemer · Data og kapacitetsstyring · "
    "Bæredygtig drift · Strategisk platform · Levende og velfungerende campusmiljøer · "
    "Læringsfaciliteter · Simulation · Fleksible studiemiljøer · Regional samhørighed · "
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

    m.models_table("OMRÅDETS STYRING — ANVENDT I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER OMRÅDET I DRIFT",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN LEDES OMRÅDET — DE FIRE PARTER")
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
    build(os.path.join(ROOT, "Shahram_Ajloo_UCSYD_FacilityManagementchef.docx"))
    print("OK " + os.path.join(ROOT, "Shahram_Ajloo_UCSYD_FacilityManagementchef.docx"))
