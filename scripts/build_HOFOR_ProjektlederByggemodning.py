# -*- coding: utf-8 -*-
"""
HOFOR — Projektleder til byggemodningsprojekter (Byggemodning & Grønne Veje).
Dansk JD. HOFOR beder kun om CV + motiveret afsnit — den faste leverance er
ét dokument: motiveret side 1 (opgave-først) + CV i masterdesignet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Projektleder | Byggemodning & infrastruktur | HOFOR"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv")

DATE = "31. oktober 2026"
RECIPIENT = ("HOFOR A/S · Byggemodning & Grønne Veje · att. interim sektionsleder Line Matthäi · "
             "tlf. 3445 8070 · b2blimat@hofor.dk")
SUBJECT = "Motivation og CV: Projektleder til byggemodningsprojekter"

# ------------------------------------------------------------------ side 1
INTRO = [
    "Opgaven er at holde HOFORs interesser intakte gennem byggemodninger, hvor det er byudviklerens "
    "rådgivere og entreprenører, der fører arbejdet ud i livet. Nordhavn i dag og Østhavn med "
    "Kløverparken, Refshaleøen og Lynetteholm i de kommende år bliver ikke nemmere af at blive store: jo "
    "flere parter, jo tidligere afgøres leverancer, kvalitet og ændringer.",

    "Nedenfor er min læsning af rollen og det system, der ligger klar: kontraktmatrix med krav og "
    "forpligtelser, interessentkort med beslutningsret, fast møde- og rapportkadence, ændringshåndtering "
    "med beslutningslog og en model for, hvornår de rette fagfolk skal ind.",
]

BULLETS = [
    ("Kravet: kontraktstyring — at krav og forpligtelser i byggemodningsaftalerne overholdes",
     "Løsningen er en kontraktmatrix pr. aftale: hvad HOFOR skal levere, hvad byudvikleren skal levere, "
     "hvornår, og hvad der sker, hvis det glider. Den gennemgås ved opstart og ved hver projektmøderunde, "
     "så krav ikke bliver til fortolkning midt i en anlægsfase."),

    ("Kravet: projektmøder med klar forventningsafstemning til byudviklere, rådgivere og entreprenører",
     "Løsningen er en fast kadence med dagsorden, beslutningslog og referat, der bliver sendt ud samme "
     "dag: status på leverancer, åbne tekniske afklaringer, ændringer og næste beslutningspunkt. "
     "Forventningsafstemning er et dokument, ikke en stemning."),

    ("Kravet: planlægge projektforløbet med interne projektdeltagere, interessenter og byudviklere",
     "Løsningen er en fælles plan fra den tidlige analyse- og skitsefase med milepæle, "
     "afhængigheder og hvem der beslutter hvad — så HOFORs fagfolk kommer ind på det tidspunkt, hvor de "
     "kan påvirke løsningen, og ikke når den er projekteret."),

    ("Kravet: projekterne følger HOFORs projektmodel og governance og holdes på rette spor",
     "Løsningen er en styringsmodel, der ligger tæt på HOFORs egen: faseporte med veldefinerede "
     "beslutningsgrundlag, risikolog med ejer og frist, månedlig status på tid, økonomi og kvalitet — og "
     "en eskalering, der sker i tide, fordi den er aftalt på forhånd."),

    ("Kravet: samle trådene på tværs af fagligheder og skabe gode samarbejdsrammer internt",
     "Løsningen er et interessentkort med rolle, ansvar og beslutningsret pr. fagområde — vand, varme, "
     "spildevand, el, trafik og miljø — plus en fast intern koordinationsrytme. Uenigheder bliver "
     "håndteret som en beslutning med en ejer, ikke som en mailtråd."),

    ("Kravet: stå i front for dialogen om leverancer, kvalitet og ændringer",
     "Løsningen er ændringshåndtering med konsekvens før beslutning: hvad ændringen betyder for tid, "
     "pris, teknik og dokumentation, hvem der godkender, og hvordan det bliver skrevet ind i aftalen. "
     "Jeg har siddet på begge sider af bordet — som entreprenør med eget P&L og som bygherre hos Novo "
     "Nordisk med 37 samtidige anlægsprojekter."),

    ("Kravet: komplekse projekter, der udfordrer de tekniske standarder, skal have teknisk holdbare løsninger",
     "Løsningen er teknisk tyngde i mødet med standarderne: elautorisation (LV/MV/HV), el-teknisk "
     "projekteringsbaggrund, 25 år med anlæg, føringsveje, koter og samspil mellem forsyninger — og vane "
     "med at få en afvigelse dokumenteret frem for bare accepteret."),
]

SYSTEM = ("Systemet er allerede bygget: kontraktmatrix pr. aftale, interessentkort med beslutningsret, "
          "faseport-model med beslutningsgrundlag, risikolog med ejer og frist, ændrings- og "
          "beslutningslog samt en månedlig statuspakke på tid, økonomi og kvalitet — i Excel, Power BI og "
          "SharePoint, suppleret med Python og Claude til statusrapportering og opfølgning.")

MIRROR = ("Om kravene: projektledelse i 15 år — 37 samtidige anlægsprojekter (2–10 mio. kr.) hos Novo "
          "Nordisk med kontrakter, ændringer og aflevering, 11 samtidige entrepriser i Ventek-Air og egen "
          "virksomhed med kunder, leverandøraftaler og fuldt P&L-ansvar; facilitering af 25 specialister på "
          "tværs af mekanik, el, proces og indkøb; dansk på modersmålsniveau og kørekort kategori B.")

HONEST = ("To ting skal siges ligeud: jeg har ikke siddet med byggemodningsaftaler og byudviklere før — "
          "min kontrakterfaring er anlægs- og entreprisekontrakter, hvor jeg har styret ændringer, "
          "leverancer og aflevering på bygherrens side; aftaletypen skal læres, metoden er den samme. Og "
          "min baggrund er teknisk og el-faglig snarere end byplanlægning, hvilket her er en fordel: "
          "standardudfordringerne i projekterne er tekniske.")

CULTURE = ("Hvorfor HOFOR: \"små skridt ad gangen\" passer til den måde, byggemodninger faktisk lykkes "
           "på — ikke med ét gennembrud, men med at hver fase bliver afsluttet, før den næste begynder. Og "
           "med ni kolleger på byggemodning med vidt forskellig erfaring er det stærkeste værktøj at "
           "skrive ned, hvad man bliver enig om.")

PRACTICAL = ("Praktisk: bosat i Måløv — tæt på Nordhavn, Refshaleøen og Lynetteholm; kørekort kategori B; "
             "dansk på modersmålsniveau i skrift og tale; kan sikkerhedsgodkendes; tiltrædelse hurtigt, og "
             "egen virksomhed afvikles ved ansættelse.")

CLOSING = ("Jeg vil gerne høre, hvor byggemodningerne i Nordhavn og Østhavn står i dag, og bruge første "
           "samtale på tre spørgsmål: hvor HOFORs interesse typisk bliver udfordret, hvordan ændringer "
           "håndteres i dag, og hvad der skal være på plads, når en byudvikler møder HOFORs tekniske "
           "standarder.")

# ------------------------------------------------------------------ CV
PROFILE = ("Rollen kræver fire ting på én gang: at styre kontrakter og ændringer, at facilitere møder "
           "mellem parter med modsatrettede interesser, at holde en projektmodel og governance i hævd og "
           "at forstå teknikken, når standarderne bliver udfordret. Alle fire har været hverdag i 15 år: "
           "37 samtidige anlægsprojekter hos Novo Nordisk med kontrakter, ændringshåndtering og "
           "aflevering, 11 entrepriser i Ventek-Air, egen virksomhed med fuldt P&L og 25 specialister "
           "faciliteret på tværs af fag. Elautoriseret maskinmester (LV/MV/HV), B.Tech i Technology "
           "Management & Mechanical Engineering.")

PRACTICE = [
    ("Kontrakt- og ændringsstyring",
     "Kontraktmatrix med krav og forpligtelser, ændringshåndtering med konsekvensvurdering før "
     "beslutning, dokumenteret beslutningslog og opfølgning til aftalen er opdateret."),
    ("Projektmodel og governance",
     "Faseporte med beslutningsgrundlag, risikolog med ejer og frist, månedlig status på tid, økonomi og "
     "kvalitet, eskalering aftalt på forhånd."),
    ("Facilitering og interessenter",
     "Interessentkort med rolle, ansvar og beslutningsret, fast mødekadence med dagsorden og referat, "
     "arbejdsformer for uenighed og beslutning."),
    ("Plan og fremdrift",
     "Fælles plan med milepæle og afhængigheder fra analyse- og skitsefase, kritisk vej, "
     "ressourcebehov og hvornår de rette fagfolk skal ind i projektet."),
    ("Teknisk tyngde",
     "El og forsyningsteknik, føringsveje, koter og samspil mellem forsyninger; læsning af teknisk "
     "dokumentation og vurdering af, om en afvigelse er holdbar — eller skal tilbage i projekteringen."),
    ("Projektøkonomi",
     "Budget og prognose, timer og forbrug mod kalkule, fakturering og udestående, "
     "investeringsvurdering og månedlig økonomiopfølgning."),
]

PARTNER = [
    ("Byudvikler og dennes rådgivere",
     "Aftalen og kontraktmatrixen er reference ved hvert møde; ændringer kommer med konsekvens på tid, "
     "pris og teknik, før de bliver godkendt — og godkendelsen bliver skrevet ind i aftalen."),
    ("Entreprenører og udførende parter",
     "Krav til kvalitet, dokumentation og aflevering aftalt ved opstart, ikke ved aflevering; "
     "kontrolpunkter lagt ind i planen, og afvigelser håndteret med frist og ejer."),
    ("HOFORs egne fagfolk",
     "Rolle, ansvar og beslutningsret afklaret tidligt pr. fagområde — vand, varme, spildevand, el, "
     "trafik og miljø — og en fast intern koordinationsrytme, så de rette fagfolk er inde, før "
     "løsningen låses."),
]

FIRST90 = [
    ("Uge 1–2",
     "Alle igangværende byggemodningsprojekter gennemgået med sektionen: aftaler, økonomi, plan, åbne "
     "sager og de tekniske standarder, der bliver udfordret; mødt de ni kolleger på byggemodning og "
     "HOFORs fagfolk."),
    ("Uge 3–6",
     "Kontraktmatrix pr. aftale opdateret og gennemgået med projektets parter; mødekadence og "
     "referatstandard aftalt; risikolog og beslutningslog oprettet på egne projekter."),
    ("Uge 7–12",
     "Egne projekter kørt gennem HOFORs faseporte med opdateret beslutningsgrundlag; første "
     "ændringssag gennemført med konsekvensvurdering og dokumenteret beslutning; statuspakke på tid, "
     "økonomi og kvalitet leveret til sektionsleder."),
    ("Måned 3–6",
     "Planen for de kommende faser i Østhavn lagt med afhængigheder og interne leverancer; "
     "standardudfordringer løst med dokumenteret teknisk begrundelse; økonomi og prognose stabil."),
    ("Måned 6–12",
     "Projekterne leverer til aftalt tid, pris og kvalitet uden overraskelser i afleveringen — og "
     "HOFORs interesser er dokumenteret fastholdt gennem hele forløbet. Løbende: månedlig status, "
     "opdateret risiko og en fast post for, hvad der skal forenkles næste kvartal."),
]

MODELS = [
    ("Kontrakt og ændringer",
     "Kontraktmatrix med krav og forpligtelser, ændringshåndtering med konsekvensvurdering, "
     "beslutningslog, krav om dokumentation og opfølgning"),
    ("Governance",
     "Faseporte med beslutningsgrundlag, risiko- og interessentlog, eskaleringstrappe, "
     "månedlig status på tid, økonomi og kvalitet"),
    ("Facilitering",
     "Interessentkort med beslutningsret, mødekadence og referatstandard, workshop- og "
     "beslutningsmetode, konflikthåndtering med ejer pr. uenighed"),
    ("Plan og fremdrift",
     "Milepæle og afhængigheder, kritisk vej, ressource- og indkøbsbehov, "
     "modenhedsvurdering pr. fagområde"),
    ("Teknik",
     "El og forsyningsteknik, føringsveje og koter, tekniske standarder og afvigelseshåndtering, "
     "DS/HD 60364, dokumentationskrav ved aflevering"),
    ("Økonomi",
     "Budget og prognose, timer mod kalkule, fakturering og udestående, investeringsvurdering "
     "(NPV/IRR) og følsomhed"),
    ("Værktøj",
     "SAP ERP, Power BI-tavler, Excel-modeller, SharePoint som dokumentbase, Python og Claude til "
     "statusrapportering og opfølgning"),
]

ACHIEVEMENTS = [
    ("37 samtidige anlægsprojekter, 2–10 mio. kr.",
     "kontrakter, ændringshåndtering, plan og aflevering hos Novo Nordisk — nul kritiske fund."),
    ("25 specialister faciliteret på tværs af fag",
     "mekanik, el, proces og indkøb — roller og ansvar afklaret tidligt og fulgt op i praksis."),
    ("11 samtidige entrepriser og 14-mands team",
     "kapacitetsplanlægning, fremdrift og dokumentation ved montage i aktive bygninger."),
    ("−40 % energikost og nul uplanlagte stop",
     "dokumenterede forbedringer på 24/7-anlæg gennem PDCA og standardiseret arbejde."),
]

EXPERIENCE = [
    ("Senior Commissioning Engineer / Projektleder, elektriske anlæg",
     "Novo Nordisk A/S · Kalundborg · nov. 2022 – jul. 2024",
     "37 samtidige anlægsprojekter, 2–10 mio. kr. · 25 specialister inden for teknik, indkøb og drift · "
     "GMP/FDA/EMA",
     [("Projektledelse og kontrakter",
       "tidsplan, økonomi, kontrakter og risiko; ændringer håndteret med konsekvensvurdering og "
       "dokumenteret beslutningslog."),
      ("Facilitering på tværs",
       "25 specialister på tværs af mekanik, el, proces og indkøb — roller, ansvar og grensesnit aftalt, "
       "før arbejdet blev sat i gang."),
      ("Aflevering og dokumentation",
       "FAT/SAT, IQ/OQ/PQ og valideringsdokumentation med afvigelseshåndtering — nul kritiske fund.")]),

    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester",
     "ELOHVAC ApS · København · maj 2023 – nu",
     "5 elektrikere og 3 lærlinge · 40+ serviceanlæg · fuldt P&L, kunder, tilbud og leverandøraftaler",
     [("Kunder og kontrakter",
       "kundedialog, besigtigelse, tilbud og aftaler på el- og tavleopgaver; forhandling og opfølgning "
       "til underskrift og aflevering."),
      ("Økonomi og leverandører",
       "budget, prognose, indkøb, leverandøraftaler og prissammenligning med fuldt ansvar for bundlinjen.")]),

    ("Projekt- og værkstedsleder, ventilation & klima",
     "Ventek-Air · København · jan. 2022 – nov. 2022",
     "14-mands produktions- og montageteam · 11 samtidige projekter (2–10 mio. kr.)",
     [("Fremdrift og leverancer",
       "kapacitetsplanlægning, flowstyring og daglige tavlemøder over 11 samtidige entrepriser med "
       "dokumentation ved montage i aktive bygninger.")]),

    ("Drifts- og vedligeholdelseschef / værkstedstekniker",
     "Biofos (Lynetten) · København · aug. 2017 – jan. 2022",
     "24/7 forsyningsanlæg · pumper, HVAC, koblingsanlæg, højspænding og SCADA · budgetter i SAP",
     [("Drift, anlæg og leverandører",
       "PDCA-baseret vedligehold med KPI'er i SAP, nul uplanlagte stop i fem år; koordinering af egne "
       "teknikere, entreprenører og leverandører — adgang, sikkerhed og arbejdstilladelser.")]),

    ("Elektromekaniker / Produktionsteamleder",
     "ARJ Engineering · Teheran · dec. 2003 – mar. 2010",
     "12-mands produktionsteam · skiftplanlægning, materialestyring og lager",
     [("Produktionsteam og teknisk problemløsning",
       "skiftplanlægning, materialestyring og målopfølgning; reparation og diagnosticering af "
       "elektriske og mekaniske systemer gennem struktureret root cause-analyse.")]),
]

EDUCATION = [
    ("B.Tech (EQF niveau 6) — Technology Management & Mechanical Engineering",
     "Maskinmesterskolen / Copenhagen School of Marine Engineering & Technology Management · 2017 – 2022 · "
     "karakter 7,6/12"),
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
     "Anvendt i drift · 2017 – nu"),
    ("Problemløsning — 8-trins, A3, DMAIC og Six Sigma-værktøjer",
     "Anvendt i drift og projekter · 2017 – nu"),
]

LANGUAGES = "Dansk (modersmål, skrift og tale) · Engelsk (professionelt) · Persisk/farsi · Kørekort B (kategori B)"

PRACTICAL_CV = ("Bosat i Måløv — kort til Nordhavn, Refshaleøen og Lynetteholm; kørekort kategori B; dansk "
                "på modersmålsniveau i skrift og tale og engelsk professionelt; har arbejdet i "
                "myndigheds- og GMP-regulerede miljøer; tiltrædelse hurtigt, egen virksomhed afvikles ved "
                "ansættelse.")

REFERENCES = "Tidligere ledere og samarbejdspartnere hos Novo Nordisk A/S (Kalundborg), Biofos (Lynetten) og egne kunder i ELOHVAC — oplyses ved henvendelse."

KEYWORDS = (
    "Projektleder · Byggemodning · Byggemodningsprojekter · Byggemodningsaftaler · Byudviklere · "
    "Kontraktstyring · Kontrakter · Forpligtelser · Leverancer · Kvalitet · Ændringer · "
    "Ændringshåndtering · Projektmøder · Forventningsafstemning · Rådgivere · Entreprenører · "
    "Interessenter · Facilitering · Samarbejde · Projektmodel · Governance · Fremdrift · Planlægning · "
    "Risiko · Økonomi · Statusrapportering · Tekniske standarder · Teknisk holdbare løsninger · "
    "Nordhavn · Østhavn · Kløverparken · Refshaleøen · Lynetteholm · Forsyning · Vand · Varme · "
    "Spildevand · El · Anlæg · Infrastruktur · Aflevering · Dokumentation · SAP · Power BI · "
    "SharePoint · Kørekort B · Dansk · Måløv"
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
        m.bullet(label, body, after=40)

    m.para(SYSTEM, after=80)

    for t in (MIRROR, HONEST, CULTURE, PRACTICAL, CLOSING):
        m.para(t, after=55)

    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # ---------------------------------------------------------------- side 2+
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROJEKTPROFIL")
    m.para(PROFILE, after=80)

    m.section("HVAD ROLLEN KRÆVER — OG HVORDAN DET LØSES")
    for label, body in PRACTICE:
        m.bullet(label, body, after=30)

    m.models_table("PROJEKT- OG STYRINGSMETODER — ANVENDT I PRAKSIS",
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

    # 90-dagesplanen som afsluttende side, så tabellen ikke deles over to sider
    m.page_break()
    m.models_table("FØRSTE 90 DAGE — SÅDAN KOMMER BYGGEMODNINGERNE I RYTME",
                   ("Hvornår", "Hvad er på plads"), FIRST90)

    m.section("SÅDAN ARBEJDES DER MED PARTERNE I ET FORLØB")
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
                  title="Motivation og CV — Projektleder til byggemodningsprojekter, HOFOR",
                  subject="Byggemodning · kontraktstyring · interessentfacilitering · governance",
                  keywords=("projektleder, byggemodning, byggemodningsaftaler, kontraktstyring, "
                            "byudviklere, interessenter, facilitering, governance, nordhavn, østhavn, "
                            "hofor, dansk"),
                  comments="Masterdesign (navy bannere, Calibri 9,5 pt). Dansk, ATS-optimeret. "
                           "Motiveret side 1 (krav → løsning), CV side 2-3, 90-dagesplan side 4.")


if __name__ == "__main__":
    out = os.path.join(ROOT, "Shahram_Ajloo_HOFOR_Projektleder_Byggemodning.docx")
    print("OK", build(out))
