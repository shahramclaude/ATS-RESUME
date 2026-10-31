# -*- coding: utf-8 -*-
"""
Energy Machines ApS — Teknisk Projektleder (Technical Project Manager), København K.
Dansk JD. Ét samlet dokument: opgave-først side 1 + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Teknisk Projektleder | Integrerede energisystemer | København"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")

DATE = "1. november 2026"
RECIPIENT = ("Energy Machines ApS · Nicolai Eigtveds Gade 26, 5., 1402 København K · "
             "att. Morten Rasmussen, Head of Operations")
SUBJECT = "Ansøgning: Teknisk Projektleder — installation af integrerede energisystemer"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Opgaven er at tage et integreret energisystem fra kontrakt til driftsat anlæg: varmepumpe, "
    "geotermisk lager, varmegenvinding og styring monteret, indreguleret og dokumenteret — på en "
    "byggeplads med entreprenører, underleverandører og en kunde, der skal kunne flytte ind. "
    "Projektledelse i den type anlæg handler ikke om at følge en plan, men om at holde økonomien, "
    "tidsplanen og de tekniske grænseflader sammen, når virkeligheden flytter sig.",

    "Nedenfor er min læsning af rollen og det system, der står klar fra første dag: projektmodel "
    "med faseporte og én plan pr. anlæg, økonomimodel med kalkule, indkøbsforpligtelser og ugentlig "
    "prognose, grænsefladematrix mellem fagene, afleveringspakke med testprotokoller og fast "
    "kadence med kunde og entreprenør.",
]

BULLETS = [
    ("Kravet: lede projektplanlægning, udførelse og levering",
     "Løsningen er én plan pr. anlæg, der kan læses af både teknikere og ledelse: milepæle for "
     "projektering, indkøb, montage, idriftsættelse og aflevering, med kritisk vej og "
     "beslutningspunkter. Jeg har kørt 37 samtidige anlægsprojekter (2–10 mio. kr.) og 11 "
     "entrepriser i montage."),

    ("Kravet: supportere tilblivelsen af projektøkonomien med salgsteamet og eksekvere inden for "
     "samme økonomi",
     "Løsningen er at sidde med i kalkulen fra start: mængder, timer, entreprenørydelser, "
     "risikopost og den tekniske forudsætning, prisen bygger på — og så følge samme kalkule gennem "
     "udførelsen med timeforbrug og prognose hver uge. Jeg har haft fuldt P&L i egen virksomhed og "
     "ved, hvor forskellen skabes: i grænsefladerne."),

    ("Kravet: koordinere indkøb, planlægning og logistik med entreprenører og underleverandører — og "
     "justere projektplanerne",
     "Løsningen er en indkøbs- og leveranceplan med leveringstid, montagevindue og ansvarlig, "
     "koblet til byggepladsens rækkefølge: hvad skal være på plads, før næste faggruppe kommer. Når "
     "noget glider, justeres planen med det samme — med konsekvens for tid, pris og grænseflader "
     "skrevet ind."),

    ("Kravet: overvåge mekaniske-, elektriske- og VVS-installationer samt idriftsættelsesaktiviteter",
     "Løsningen er faglig kontrol på pladsen: montagekontrol mod tegning og standard, tilsyn med "
     "el- og VVS-arbejde og en idriftsættelsesplan med forudsætninger, testprotokoller og "
     "acceptkriterier pr. system. Jeg er elautoriseret maskinmester (LV/MV/HV) og har selv stået "
     "med FAT/SAT, IQ/OQ/PQ og indregulering — jeg kan vurdere arbejdet, ikke kun efterspørge det."),

    ("Kravet: sikre overholdelse af kvalitets-, sikkerheds- og kontraktuelle forpligtelser (AB, ABT, "
     "ABR)",
     "Løsningen er at gøre kontrakten operationel: hvem leverer hvad, hvornår er noget en ændring, "
     "hvordan varsles der, og hvad er svarfristen — lagt i projektplanen som punkter med ejer. "
     "Sikkerhed styres med arbejdstilladelser, LOTO og sikkerhedsrunder på projektmødet."),

    ("Kravet: være den centrale kontaktperson for kunder og interessenter",
     "Løsningen er én kontakt og en fast kadence: ugentligt statusnotat med fremdrift, økonomi, "
     "risici og næste beslutning, og et møde hvor kunden kan træffe beslutning på et oplyst "
     "grundlag. I 20 år har jeg været den, kunden ringede til, når noget ikke gik som planlagt."),

    ("Kravet: agil og fleksibel tilgang i et scale-up-miljø, hvor varmepumper og geotermisk lagring "
     "er kerneydelsen",
     "Løsningen er at arbejde i korte rytmer: to-ugers udsnit af planen, en risikoliste der "
     "gennemgås fast, og beslutninger tættest muligt på byggepladsen. Varmepumpen er kølekredsen "
     "vendt om, og jeg har køle-, ventilations- og elkompetence (AMU køleteknik, CTS/BMS) — "
     "geotermisk lagring skal jeg lære hos jer."),
]

SYSTEM = ("Systemet er allerede bygget: projektmodel med faseporte og én plan pr. anlæg, "
          "økonomimodel med kalkule, indkøbsforpligtelser og ugentlig prognose, grænsefladematrix "
          "mellem mekanik, el og VVS, leveranceplan koblet til byggepladsens rækkefølge, møde- og "
          "rapporteringskadence med kunde og entreprenør samt idriftsættelses- og afleveringspakke "
          "med testprotokoller — i Excel/Power BI og projektværktøj, med rapporter genereret i "
          "Python og Claude.")

MIRROR = ("Om kravene: 20 år med tekniske anlæg og projektledelse — 37 samtidige anlægsprojekter "
          "med 25 specialister koordineret, 11 entrepriser med 14 mand, fuldt P&L og 40+ "
          "serviceanlæg i egen virksomhed samt 24/7-drift med nul uplanlagte stop i fem år. "
          "Elautoriseret maskinmester (LV/MV/HV), B.Tech i Technology Management & Mechanical "
          "Engineering og el-ingeniør; dansk på modersmålsniveau og engelsk professionelt.")

HONEST = ("Tre ting skal siges ligeud: jeg har ikke leveret et integreret varmepumpe- og "
          "geotermianlæg som projektleder før — min erfaring er el-, ventilations- og køleanlæg samt "
          "procesanlæg, hvor jeg til gengæld har stået med idriftsættelse og aflevering. Jeg har "
          "arbejdet under AB/ABT-lignende vilkår som leverandør og entreprenør, men ikke selv været "
          "kontraktejer, og EaaS-økonomien — hvor I ejer og driver anlægget — skal jeg sætte mig "
          "ind i.")

CULTURE = ("Hvorfor Energy Machines: jeres filosofi — at energi skal flyttes, ikke genereres — er "
           "den logik, jeg har arbejdet efter i køl, ventilation og varmegenvinding i 20 år. I har "
           "120+ projekter bag jer, tager ansvar fra design til drift og sælger anlæggene som EaaS — "
           "så driftsomkostningen over levetiden er jeres forretning, ikke bare kundens. Det er "
           "projektledelse, hvor anlægget skal køre i femten år.")

PRACTICAL = ("Praktisk: bosat i Måløv, 25 minutter til København K; kørekort B og bil. Dansk på "
             "modersmålsniveau og engelsk professionelt. Kan tiltræde hurtigst muligt; egen "
             "virksomhed afvikles ved ansættelse.")

CLOSING = ("I første samtale vil jeg gerne høre, hvor mange projekter en projektleder har i gang ad "
           "gangen, og hvor stor en del af udførelsen der ligger hos faste entreprenører.")

# ------------------------------------------------------------------ CV
PROFILE = ("Rollen kræver tre ting på én gang: en projektleder der kan holde økonomi og tidsplan, en "
           "el- og HVAC-faglig person der kan vurdere montagen og idriftsættelsen, og en "
           "kontraktflade der bliver styret i stedet for overrasket. Tyve år med tekniske anlæg: 37 "
           "samtidige anlægsprojekter (2–10 mio. kr.) med 25 specialister koordineret, FAT/SAT, "
           "IQ/OQ/PQ og nul kritiske fund ved aflevering, 11 entrepriser med 14-mands montageteam, "
           "fuldt P&L og 40+ serviceanlæg i egen virksomhed samt 24/7-drift med nul uplanlagte stop i "
           "fem år. Elautoriseret maskinmester (LV/MV/HV), B.Tech i Technology Management & "
           "Mechanical Engineering og el-ingeniør.")

PRACTICE = [
    ("Projekt og fremdrift",
     "Faseopdelt model med milepæle, kritisk vej og beslutningspunkter; én plan pr. anlæg, "
     "to-ugers udsnit i udførelsen og ugentlig status til kunde og ledelse."),
    ("Projektøkonomi",
     "Kalkule med mængder, timer, entreprenørydelser og risikopost; timeforbrug, "
     "indkøbsforpligtelser og prognose fulgt ugentligt, ændringssager prissat før udførelse."),
    ("Indkøb og logistik",
     "Leveranceplan med leveringstid, montagevindue og ansvarlig, koblet til byggepladsens "
     "rækkefølge; underleverandører styret på kvalitet, fremdrift og sikkerhed."),
    ("Mekanik, el og VVS",
     "Montagekontrol mod tegning og standard, tilsyn med el- og VVS-arbejde, CTS/BMS og "
     "indregulering; elautorisation (LV/MV/HV) og køle-/ventilationskompetence i baggrunden."),
    ("Idriftsættelse og aflevering",
     "Idriftsættelsesplan med forudsætninger, FAT/SAT og testprotokoller pr. system, "
     "acceptkriterier, afvigelsesliste med ejer og frist og en afleveringspakke med drifts- og "
     "vedligeholdelsesdokumentation."),
    ("Kontrakt og sikkerhed",
     "AB/ABT/ABR-vilkår oversat til punkter i projektplanen — varsling, frist, ændring og "
     "dokumentation; arbejdstilladelser, LOTO, sikkerhedsrunder og nærved-hændelser på dagsordenen."),
    ("Kunder og interessenter",
     "Én kontakt, fast kadence og et statusnotat hvor fremdrift, økonomi, risici og næste "
     "beslutning står på én side; bygherre, entreprenør, underleverandør og drift samlet om samme "
     "plan."),
]

MODELS = [
    ("Plan",
     "Faseporte fra kontrakt til aflevering, kritisk vej, milepæle med ejer og et to-ugers udsnit "
     "i udførelsen"),
    ("Økonomi",
     "Kalkule fra salgsfasen fulgt gennem udførelsen: timeforbrug, indkøbsforpligtelser, prognose "
     "og ændringssager prissat før udførelse"),
    ("Grænseflader",
     "Matrix mellem mekanik, el, VVS og styring: hvem leverer, hvornår, og hvad skal være på plads "
     "før næste fag"),
    ("Indkøb og logistik",
     "Leveranceplan med leveringstid, montagevindue og ansvarlig, koblet til byggepladsens "
     "rækkefølge og kranløft"),
    ("Idriftsættelse",
     "Forudsætningsliste, FAT/SAT, testprotokol og acceptkriterium pr. system; afvigelse med ejer "
     "og frist"),
    ("Kontrakt",
     "Varslings- og ændringslog med hjemmel i AB/ABT/ABR, dokumenteret løbende og ikke ved "
     "aflevering"),
    ("Rapportering",
     "Statusnotat på én side til kunde og ledelse, ugentlig økonomi og risikoliste; genereret med "
     "Python og Claude i stedet for skrevet i hånden"),
]

ACHIEVEMENTS = [
    ("37 anlægsprojekter uden kritiske fund",
     "2–10 mio. kr. hos Novo Nordisk med 25 specialister, plan, budget, FAT/SAT og aflevering "
     "under GMP/FDA/EMA-krav."),
    ("11 entrepriser i montage samtidig",
     "14-mands produktions- og montageteam med kapacitetsplanlægning, daglige tavlemøder og "
     "leverancer til aftalt tid."),
    ("40+ serviceanlæg med fuldt P&L",
     "egen virksomhed med 5 elektrikere og 3 lærlinge: kunder, tilbud, indkøb, leverandøraftaler "
     "og ansvar for bundlinjen."),
    ("Nul uplanlagte stop i fem år",
     "24/7-forsyningsanlæg med SCADA, højspænding og koblingsanlæg — planlagt vedligehold, LOTO og "
     "arbejdstilladelser som fast regime."),
    ("−40 % energikost og +40 % produktivitet",
     "dokumenterede forbedringer gennem måling, standardarbejde og dataunderstøttet planlægning."),
]

EXPERIENCE = [
    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister · GMP/FDA/EMA",
     [("Projekt, økonomi og fremdrift",
       "plan og budget pr. projekt, fremdrift og rapportering til styregruppe; 25 specialister "
       "koordineret på tværs af mekanik, el, proces og indkøb."),
      ("Idriftsættelse og aflevering",
       "kravspecifikation, FAT/SAT, IQ/OQ/PQ, afvigelseshåndtering og aflevering uden kritiske "
       "fund — test og dokumentation af sikkerhedsfunktioner på procesanlæg.")]),

    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og leverandøraftaler",
     [("Kunder, tilbud og økonomi",
       "tilbudsberegning, indkøb og leverandøraftaler, plan og prognose med fuldt ansvar for "
       "bundlinjen; ændringssager prissat, før arbejdet blev udført."),
      ("Teknisk ansvar",
       "dimensionering, fejlfinding og dokumentation på el-, køle- og HVAC-anlæg; opmåling og "
       "løsningsvalg på stedet hos kunden.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Produktion, montage og fremdrift",
       "14-personers team med kapacitetsplanlægning, daglige tavlemøder og 11 samtidige entrepriser; "
       "montage i eksisterende byggeri med hensyn til drift og brugere.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · budgetter i SAP",
     [("Drift, vedligehold og beredskab",
       "planlagt vedligehold, tilstandskontrol og KPI'er i SAP; nul uplanlagte stop i fem år."),
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

PRACTICAL_CV = ("Bosat i Måløv — cirka 25 minutter til København K og kort til byggepladser i "
                "hovedstadsområdet; kørekort kategori B og bil. Dansk på modersmålsniveau og engelsk "
                "professionelt i skrift og tale; kan tiltræde hurtigst muligt eller efter aftale; "
                "egen virksomhed afvikles ved ansættelse.")

REFERENCES = ("Tidligere ledere og samarbejdspartnere hos Novo Nordisk A/S, Biofos (Lynetten), "
              "Ventek-Air og egne kunder i ELOHVAC — oplyses ved henvendelse.")

PARTNER = [
    ("Kunden og bygherren",
     "Én kontakt og et statusnotat på én side hver uge: fremdrift, økonomi, risici og næste "
     "beslutning — så beslutninger kan træffes på et oplyst grundlag i stedet for at blive udskudt."),
    ("Entreprenører og underleverandører",
     "Leveranceplan og grænsefladematrix, så hver faggruppe ved, hvad der skal være på plads før "
     "dem; kvalitet, fremdrift og sikkerhed fulgt på samme møde som økonomien."),
    ("Salg, design og drift internt",
     "Kalkulen bygget sammen med salg og design, så prisen hviler på de rigtige tekniske "
     "forudsætninger — og en overdragelse til drift, hvor anlægget er dokumenteret, indreguleret og "
     "kan køre uden project manager i ryggen."),
]

FIRST90 = [
    ("Uge 1–2",
     "Læst projektporteføljen igennem: kontrakter, kalkuler, tidsplaner og de næste tre "
     "afleveringer. Været på et igangværende anlæg og set montagen; mødt salg, design, drift og de "
     "faste entreprenører."),
    ("Uge 3–6",
     "Overdaget de nærmeste projekter med egen plan, økonomioversigt og grænsefladeliste; "
     "mødekadence og statusnotat etableret med kunderne; risikoliste gennemgået på hvert projekt."),
    ("Uge 7–12",
     "Første projekt leveret eller milepæl nået efter min plan; idriftsættelses- og "
     "afleveringspakke standardiseret, så test, acceptkriterier og dokumentation er ens på tværs af "
     "anlæg; indkøbs- og leveranceplanerne lagt fast."),
    ("Måned 3–6",
     "Projektøkonomien følgt ugentligt på alle egne projekter med prognose og ændringssager prissat "
     "før udførelse; samarbejdet med de faste entreprenører formaliseret med faste møder og "
     "opfølgning på kvalitet."),
    ("Måned 6–12",
     "Egne anlæg leveret til tiden og inden for kalkulen, med dokumentation der kan overdrages til "
     "drift og EaaS-forretning; standarder og skabeloner delt med de øvrige projektledere, så nye "
     "projekter starter længere fremme end det forrige."),
]

KEYWORDS = (
    "Teknisk Projektleder · Technical Project Manager · Projektledelse · Projektplanlægning · "
    "Udførelse · Levering · Projektøkonomi · Salgsteam · Indkøb · Planlægning · Logistik · "
    "Entreprenører · Underleverandører · Projektplaner · Mekaniske · Elektriske · "
    "VVS-installationer · Idriftsættelsesaktiviteter · Kvalitet · Sikkerhed · Kontraktuelle "
    "forpligtelser · Kunder · Interessenter · Lederegenskaber · Organisatoriske · Kommunikative · "
    "Løsninger · Eksekvere · Agil · Fleksibel · Scale-up · Holdspiller · Samarbejdsorienteret · "
    "Vedvarende energisystemer · Varmepumper · Geotermisk lagring · Varmegenvinding · Intelligent "
    "styring · Dansk byggeret · AB · ABT · ABR · Ingeniørvidenskab · Maskinmester · Dansk · Engelsk · "
    "Energy-as-a-Service · Energiomstilling · Bygningsmasse · Kontraktforhandling · Aflevering · "
    "Byggeplads"
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
    m.resume_header(NAME, TITLE, CONTACT, "PROJEKTLEDELSESPROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("PROJEKTMETODER — ANVENDT I PRAKSIS",
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

    m.section("SÅDAN LEDES PROJEKTERNE — DE TRE PARTER")
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
                  title="Ansøgning og CV — Teknisk Projektleder, Energy Machines ApS",
                  subject="Integrerede energisystemer · projektledelse · projektøkonomi · "
                          "idriftsættelse · AB/ABT/ABR",
                  keywords=("teknisk projektleder, project manager, varmepumper, geotermisk lagring, "
                            "projektøkonomi, idriftsættelse, entreprenører, ab, abt, abr, "
                            "energy machines, dansk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Ansøgning side 1 (krav → løsning), CV side 2-3, 90 dage side 4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_EnergyMachines_TechnicalProjectManager.docx")
    print("OK", build(out))
