# -*- coding: utf-8 -*-
"""
Jakon A/S — Projektleder med håndværksmæssig baggrund.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Projektleder | Renovering & ombygning | Byggeleder på pladsen"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "31. oktober 2026"
RECIPIENT = ("Jakon A/S · Baltorpbakken 9, 2750 Ballerup · att. afdelingschef Lau Jensen · "
             "indsendt til job@jakon.dk med mærkning »Ansøgning – Projektleder«")
SUBJECT = "Ansøgning: Projektleder med håndværksmæssig baggrund"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Opgaven er at levere renoverings- og ombygningsprojekter, hvor bygherren kan se med egne øjne, "
    "at det bliver gjort ordentligt — og hvor tidsplan og økonomi holder, fordi nogen har styr på "
    "rækkefølgen. Projektlederen hos Jakon er tæt på byggepladsen: daglig ledelse af håndværkerne, "
    "koordinering af underentreprenører og leverandører og en dialog med bygherre og rådgiver, der "
    "bygger på fakta frem for forhåbninger.",

    "Nedenfor er min læsning af rollen og det system, der står klar fra første dag: én projektplan med "
    "milepæle og afhængigheder, økonomiopfølgning pr. fag, mangel- og kvalitetslister der lukkes før "
    "aflevering, fast koordinationsmøde med underentreprenørerne og en afleveringspakke, driften kan "
    "overtage.",
]

BULLETS = [
    ("Kravet: planlægning og styring af projekter — egne eller i team",
     "Løsningen er én plan, alle arbejder efter: milepæle, afhængigheder og en rullende fireugersplan "
     "pr. fag, hvor underentreprenører og leverancer er lagt ind før arbejdet starter — ikke efter at "
     "det er forsinket."),

    ("Kravet: daglig ledelse på byggepladsen",
     "Løsningen er fast rytme: morgenmøde med formændene, ugeplan på tavlen, sikkerhedsrundering og "
     "beslutninger taget på pladsen samme dag. En projektleder, der er til stede, hører om problemet, "
     "før det bliver en sag."),

    ("Kravet: økonomi- og tidsstyring",
     "Løsningen er budget pr. fag og leverance, månedlig prognose og en afvigelsesliste med ejer og "
     "frist — plus ændringssager prissat, før arbejdet bliver udført, så merarbejde ikke bliver en "
     "diskussion ved aflevering."),

    ("Kravet: koordinering med underentreprenører og leverandører",
     "Løsningen er et ugentligt koordinationsmøde med referat, leveranceplan og en tydelig "
     "arbejdsgrænseflade pr. fag: hvem gør hvad, hvornår, og hvad der skal være færdigt før næste "
     "faggruppe kommer ind."),

    ("Kravet: samarbejde og dialog med bygherrer og rådgivere",
     "Løsningen er fast rapportering i et format, bygherren kan bruge: fremdrift, økonomi, åbne sager "
     "og beslutninger, der mangler svar — med en beslutningslog, så det er tydeligt, hvad der er "
     "aftalt, og hvornår."),

    ("Kravet: håndværksmæssig baggrund og erfaring som projektleder eller byggeleder",
     "Løsningen er 20 år i de fag, der bygges med: håndværksmæssig baggrund som elektromekaniker, "
     "elautoriseret maskinmester og B.Tech — 14-mands montageteam over 11 samtidige entrepriser og 37 "
     "anlægsprojekter hos Novo Nordisk, hvor underentreprenører og specialister blev koordineret under "
     "GMP-krav."),

    ("Kravet: skabe struktur i projekter og tage ansvar for opgaven",
     "Løsningen er kvalitet lukket systematisk: mangelgennemgang med fotos, ejer og frist, egenkontrol "
     "pr. fag og en afleveringsmappe med drifts- og vedligeholdelsesdokumentation — for det er den, "
     "bygherren lever med bagefter."),
]

SYSTEM = ("Systemet er allerede bygget: projektmodel med faser og beslutningspunkter, tidsplan med "
          "milepæle og rullende uger, økonomi pr. fag med prognose, mangel- og kvalitetsliste med ejer og "
          "frist, ugentligt koordinationsmøde med underentreprenørerne og en afleveringspakke inkl. "
          "driftsdokumentation — i Excel, Power BI og Dalux/Byggeweb-lignende platforme, med Python og "
          "Claude til rapportering.")

MIRROR = ("Om kravene: 20 år i tekniske entrepriser og drift — 14-mands montageteam over 11 samtidige "
          "entrepriser, 37 anlægsprojekter (2–10 mio. kr.) med 25 specialister og underentreprenører "
          "koordineret, daglig ledelse af 5 elektrikere og 3 lærlinge med fuldt P&L samt 24/7-drift uden "
          "uplanlagte stop i fem år; elautoriseret maskinmester (LV/MV/HV).")

HONEST = ("To ting skal siges ligeud: jeg er ikke uddannet bygningskonstruktør, og mine "
          "renoveringsprojekter har været de tekniske fag — el, ventilation, køl og HVAC — ikke "
          "storentreprise som hovedentreprenør. Det, jeg kommer med, er det modsatte: en bygherre- og "
          "driftsvinkel på håndværket, hvor det er installationerne, der afgør, om bygningen fungerer "
          "bagefter.")

CULTURE = ("Hvorfor Jakon: I skriver ordentlighed, omsorg og pragmatik — og ordentlighed er ikke et "
           "sprog, det er en beslutning, der tages hver dag: ændringer bliver dokumenteret, håndværkerne "
           "får en plan de kan arbejde efter, og bygherren hører om en afvigelse fra os, før de ser den. "
           "Flad struktur virker kun, når nogen tør sige, at tidsplanen ikke holder.")

PRACTICAL = ("Praktisk: bosat i Måløv — cirka 10 minutter fra hovedkontoret på Baltorpbakken i samme "
             "kommune, og på byggepladser i hele hovedstadsområdet fra dag ét; kørekort B; dansk på "
             "modersmålsniveau; klar til hurtigt start, og egen virksomhed afvikles ved ansættelse.")

CLOSING = ("Jeg vil gerne se en af jeres igangværende renoveringer og bruge første samtale på to "
           "spørgsmål: hvordan projektleder og byggeleder deler ansvaret i dag, og hvor I gerne vil have "
           "projektstyringen skarpere — på økonomi, fremdrift eller mangler ved aflevering.")

# ------------------------------------------------------------------ CV
PROFILE = ("Rollen kræver tre ting på én gang: en håndværksmæssig forståelse for rækkefølgen i "
           "arbejdet, en projektleder der er på pladsen hver dag, og styr på økonomi og fremdrift. Alle "
           "tre har været hverdag i 20 år: 14-mands montageteam over 11 samtidige entrepriser, 37 "
           "anlægsprojekter hos Novo Nordisk med 25 specialister og underentreprenører under GMP-krav, "
           "daglig ledelse af 5 elektrikere og 3 lærlinge med fuldt P&L og 24/7-drift uden uplanlagte "
           "stop i fem år. Elautoriseret maskinmester (LV/MV/HV), B.Tech i Technology Management & "
           "Mechanical Engineering.")

PRACTICE = [
    ("Projektstyring",
     "Faseopdelt plan med milepæle og beslutningspunkter, rullende fireugersplan, "
     "afhængighedsstyring og en beslutningslog, så åbne spørgsmål har en ejer og en dato."),
    ("Økonomi og tid",
     "Budget pr. fag og leverance, månedlig prognose, afvigelsesliste med ejer, ændringssager prissat "
     "før udførelse og opfølgning på timeforbrug mod kalkule."),
    ("Byggepladsledelse",
     "Morgenmøde med formænd, ugeplan på tavlen, arbejdsgrænseflader mellem fag og daglig "
     "tilstedeværelse — beslutninger bliver taget på pladsen, ikke i indbakken."),
    ("Underentreprenører og leverandører",
     "Ugentligt koordinationsmøde med referat, leveranceplan, kontrol af faglig kvalitet og "
     "samarbejde med faggrupper som tømrer, murer, VVS og el om tid, plads og rækkefølge."),
    ("Kvalitet og aflevering",
     "Egenkontrol pr. fag, mangelgennemgang med fotos, ejer og frist, prøver og dokumentation før "
     "aflevering samt en afleveringsmappe, driften kan overtage."),
    ("Bygherre og rådgiver",
     "Fast rapportering om fremdrift, økonomi og åbne sager; møder med referat og en tydelig "
     "grænseflade mellem bygherre, rådgiver og entreprenør."),
    ("Teknisk tyngde",
     "El, ventilation, køl, HVAC og styring; elautorisation LV/MV/HV, egenkontrol og "
     "dokumentationskrav — og øje for hvad driften får brug for efter overlevering."),
]

MODELS = [
    ("Projektmodel",
     "Faser og beslutningspunkter, milepæle, afhængighedskæde, rullende fireugersplan og "
     "risikolog med ejer"),
    ("Økonomi",
     "Budget pr. fag, kalkule mod timeforbrug, månedsprognose, afvigelsesliste og ændringssager "
     "prissat før udførelse"),
    ("Byggeplads",
     "Morgenmøde, ugeplan på tavle, arbejdsgrænseflader mellem fag, leveranceplan og "
     "sikkerhedsrundering"),
    ("Kvalitet",
     "Egenkontrol pr. fag, mangelgennemgang med fotos og frist, prøver og dokumentation, "
     "afleveringspakke inkl. drifts- og vedligeholdelsesdokumentation"),
    ("Samarbejde",
     "Referat og beslutningslog, mødekadence med bygherre og rådgiver, ugentligt "
     "koordinationsmøde med underentreprenører"),
    ("Værktøjer",
     "Excel og Power BI til økonomi og fremdrift, Dalux/Byggeweb-lignende projektplatforme, "
     "MS Project-principper og Python/Claude til rapportering"),
    ("Sikkerhed",
     "APV og risikovurdering, arbejdstilladelser, LOTO, sikkerhedsrundering og "
     "nærved-hændelser"),
]

ACHIEVEMENTS = [
    ("11 samtidige entrepriser og 14-mands montageteam",
     "kapacitetsplanlægning, flowstyring og daglige tavlemøder — projekter i 2–10 mio. kr.-klassen "
     "leveret ved siden af hinanden."),
    ("37 anlægsprojekter hos Novo Nordisk",
     "25 specialister og underentreprenører koordineret på tværs af mekanik, el, proces og indkøb — "
     "nul kritiske fund ved aflevering under GMP/FDA/EMA-krav."),
    ("Nul uplanlagte stop i fem år",
     "på 24/7-forsyningsanlægget Lynetten — planlagt vedligehold, PDCA og A3-root-cause i stedet for "
     "brandslukning."),
    ("5 elektrikere og 3 lærlinge med fuldt P&L",
     "daglig ledelse, opgavefordeling, kompetenceudvikling og ansvar for bundlinjen i egen "
     "virksomhed."),
    ("+40 % produktivitet og −40 % energikost",
     "dokumenterede forbedringer via måling, standardarbejde, dataunderstøttet planlægning og egen "
     "AI-tooling."),
]

EXPERIENCE = [
    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Team og fremdrift",
       "kapacitetsplanlægning, flowstyring og daglige tavlemøder over 11 samtidige entrepriser på "
       "byggepladser i hovedstadsområdet."),
      ("Koordinering",
       "underentreprenører og leverancer afstemt med bygherre og rådgiver; afvigelser taget op på "
       "mødet, ikke i en mail bagefter.")]),

    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister · GMP/FDA/EMA",
     [("Projekt og koordinering",
       "plan, økonomi og rapportering; 25 specialister og underentreprenører koordineret på tværs af "
       "mekanik, el, proces og indkøb."),
      ("Aflevering og dokumentation",
       "FAT/SAT, IQ/OQ/PQ og valideringsdokumentation med afvigelseshåndtering — nul kritiske fund og "
       "en dokumentationspakke, driften kunne overtage.")]),

    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og leverandøraftaler",
     [("Personale og plan",
       "daglig ledelse af 5 elektrikere og 3 lærlinge, opgavefordeling, kompetencematrix og "
       "udviklingssamtaler."),
      ("Kunder og økonomi",
       "serviceaftaler og akutte sager med erhvervskunder, plan og prognose, indkøb og "
       "leverandøraftaler med fuldt ansvar for bundlinjen.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · budgetter i SAP",
     [("Drift og prioritering",
       "PDCA-baseret vedligeholdsplan og KPI'er i SAP; fejlfinding på pumper, HVAC og "
       "højspænding — nul uplanlagte stop i fem år."),
      ("Leverandører og sikkerhed",
       "koordinering af egne teknikere, entreprenører og leverandører — LOTO, arbejdstilladelser, "
       "garantisager og nærved-hændelser.")]),

    ("Elektromekaniker / Produktionsteamleder",
     "ARJ Engineering · Teheran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · skiftplanlægning, materialestyring og lager",
     [("Produktionsteam og teknisk problemløsning",
       "skiftplanlægning, materialestyring og målopfølgning; reparation og diagnosticering gennem "
       "struktureret root cause-analyse.")]),
]

EDUCATION = [
    ("B.Tech (EQF niveau 6) — Technology Management & Mechanical Engineering",
     "Maskinmesterskolen / Copenhagen School of Marine Engineering & Technology Management · 2017 – "
     "2022 · karakter 7,6/12"),
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
     "Anvendt i drift og projekter · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og projekter · 2017 – nu"),
]

LANGUAGES = ("Dansk (modersmål, skrift og tale) · Engelsk (professionelt) · Persisk/farsi · "
             "Kørekort B (kategori B)")

PRACTICAL_CV = ("Bosat i Måløv i Ballerup Kommune — cirka 10 minutter fra Jakons hovedkontor på "
                "Baltorpbakken og tæt på byggepladser i hele hovedstadsområdet; kørekort kategori B; "
                "dansk på modersmålsniveau; klar til hurtigt start, og egen virksomhed afvikles ved "
                "ansættelse.")

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Ventek-Air, Novo Nordisk A/S (Kalundborg), "
              "Biofos (Lynetten) og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Bygherre og rådgiver",
     "Fast rapportering om fremdrift, økonomi og åbne sager, beslutningslog og en dialog, hvor dårlige "
     "nyheder kommer først — ikke til mødet efter."),
    ("Håndværkere og underentreprenører",
     "En plan de kan arbejde efter, klare arbejdsgrænseflader mellem fag og en leder på pladsen, der "
     "tager beslutningen samme dag i stedet for at sende den videre."),
    ("Økonomi, kvalitet og aflevering",
     "Budget pr. fag med prognose, ændringssager prissat før udførelse, mangelgennemgang med frist og "
     "en afleveringspakke inkl. driftsdokumentation."),
]

FIRST90 = [
    ("Uge 1–2",
     "Mødt projektteamet, afdelingschefen og de faggrupper, jeg skal arbejde med; gennemgået de "
     "igangværende sager — plan, økonomi, mangellister og de næste milepæle — før noget ændres."),
    ("Uge 3–6",
     "Overtaget styring af et afgrænset projekt eller en projektpakke; fireugersplan og "
     "afvigelsesliste med ejer og frist indført; koordinationsmøde med underentreprenørerne lagt fast."),
    ("Uge 7–12",
     "Økonomi pr. fag og månedsprognose på plads; mangel- og kvalitetsliste kørt som fast "
     "gennemgang; afleveringspakken standardiseret, så driften får dokumentationen med."),
    ("Måned 3–6",
     "Egne projekter leveret med tidsplan og økonomi fulgt til dørs; ændringssager dokumenteret "
     "løbende; bygherre og rådgiver orienteret på fast kadence uden overraskelser."),
    ("Måned 6–12",
     "Flere projekter i drift samtidig med stabil kvalitet og faldende mængde af mangler ved "
     "aflevering; metoderne delt med kollegerne i teamet, så det ikke afhænger af én person."),
]

KEYWORDS = (
    "Projektleder · Byggeleder · Håndværksmæssig baggrund · Bygningskonstruktør (krav i opslaget) · "
    "Renovering · Ombygning · Transformation · Hovedentreprise · Storentreprise · Byggeplads · Daglig "
    "ledelse · Projektstyring · Planlægning · Koordinering · Økonomistyring · Tidsstyring · "
    "Underentreprenører · Leverandører · Bygherre · Rådgivere · Mangellister · Kvalitetssikring · "
    "Aflevering · Dokumentation · Drifts- og vedligeholdelsesdokumentation · Struktur · Samarbejde · "
    "Løsningsorienteret · Ansvar · Faglighed · Ordentlighed · Omsorg · Flad struktur · Dalux · Power BI · "
    "Excel · SAP · Sikkerhed · Arbejdsmiljø · APV · LOTO · Dansk · Ballerup · Måløv"
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

    m.models_table("PROJEKT- OG BYGGEPLADSMETODER — ANVENDT I PRAKSIS",
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
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER PROJEKTERNE I RYTMEN",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN STYRES ET BYGGEPROJEKT — DE TRE PARTER")
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
                  title="Ansøgning og CV — Projektleder, Jakon A/S",
                  subject="Renovering og ombygning · byggeleder på pladsen · økonomi og fremdrift",
                  keywords=("projektleder, byggeleder, renovering, ombygning, hovedentreprise, "
                            "storentreprise, underentreprenører, bygherre, jakon, ballerup, dansk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1 (krav → løsning), CV side 2-3, 90 dage side 4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_Jakon_Projektleder.docx")
    print("OK", build(out))
