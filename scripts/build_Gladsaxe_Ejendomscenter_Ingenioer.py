# -*- coding: utf-8 -*-
"""Gladsaxe Kommune — Ingeniør eller lignende til Ejendomscenteret.
Samlet masterdesign: jobfokuseret følgebrev på side 1 og dokumenteret CV derefter.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")
OUTPUT = os.path.join(ROOT, "Shahram_Ajloo_Gladsaxe_Ejendomscenter_Ingenioer.docx")

NAME = "SHAHRAM AJLOO"
TITLE = "Elautoriseret maskinmester | HVAC, ejendomsdrift, energi og tekniske anlæg"
CONTACT = ("+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · "
           "Måløv (Ballerup Kommune)")
DATE = "3. november 2026"
RECIPIENT = "Gladsaxe Kommune · Ejendomscenteret · Att. teamleder Jan René Rasmussen"
SUBJECT = "Ansøgning: Ingeniør eller lignende til Ejendomscenteret"

# Side 1 — udelukkende opgaven, løsningen og kommunens behov.
LETTER = [
    ("En skolebygning kan ikke vælge mellem lavt energiforbrug og et godt indeklima; den tekniske drift skal levere begge dele samtidig.", "opening"),
    ("Det kræver, at energidata læses sammen med anlæggets drift, brugernes oplevelser og vedligeholdshistorikken. En afvigelse i forbruget er et signal til undersøgelse — ikke i sig selv en ordre om at ændre setpunktet. Først når årsag, komfort, driftsrisiko og økonomi er belyst, bør et energioptimeringstiltag prioriteres.", "para"),
    ("I Ejendomscenteret skal den tekniske løsning også fungere på tværs af ingeniørgruppen, driftsfolkene på ejendommen, håndværkere og de øvrige byggefagligheder. Den fælles opgave er at finde de rigtige løsninger samlet set: bevare funktion og indeklima, gennemføre planlagt vedligehold og reducere energispild uden at skabe nye driftsproblemer.", "para"),
    ("I praksis vil indsatsen begynde med et samlet billede af hver ejendom: HVAC- og øvrige tekniske anlæg, kendte fejl, vedligeholdsplan, automatik, energiforbrug og henvendelser fra brugerne. Mindre anlægssager beskrives med omfang, ansvar, økonomi, adgang og acceptkriterier; håndværkerens arbejde følges til afprøvning, dokumentation og overdragelse til de daglige driftsfolk.", "para"),
]

SOLUTION = [
    ("Drift før indgreb", "Akutte nedbrud prioriteres efter sikkerhed, konsekvens for bygningens brug og risiko for følgeskader. Fejlårsag og midlertidige foranstaltninger registreres, så den akutte løsning ikke fortrænger den planlagte vedligeholdelse."),
    ("Data med brugerens virkelighed", "Energiforbrug følges mod vejr, driftstid, belægning og relevante målepunkter. Teknikere og brugere inddrages ved tilbagevendende afvigelser; indeklima, energiforbrug og driftsstabilitet vurderes samlet før en ændring gennemføres."),
    ("Små sager, sikker aflevering", "En rekvisition skal beskrive behov, grænseflader, arbejdsmiljø, tidsvindue og hvad der skal være dokumenteret ved aflevering. Efterfølgende kontrolleres både den tekniske funktion og om den forventede effekt kan genfindes i data."),
]

PLAN = ("En realistisk første 90-dages rytme er: dag 1–30, gennemgang af de tildelte ejendomme sammen med driftsfolkene og kortlægning af anlæg, automatik, energidata, fejl og planlagt vedligehold; dag 31–60, prioritering af et lille antal tiltag med baseline, ansvarlig, økonomi og kontrol af indeklima; dag 61–90, gennemførelse eller projektering af de aftalte sager, kontrol af funktion og energidata samt en revideret vedligeholds- og forbedringsliste. De eksisterende værktøjer skal læres og bruges som fælles driftsgrundlag, ikke erstattes af et parallelt system.")

CULTURE = ("Gladsaxe fortsætter kampen på den grønne dagsorden, og det kommunale bygningsarbejde kan omsætte strategien til moderne, bæredygtige og energieffektive bygninger, hvor borgernes og virksomhedernes behov og trivsel er synlige i beslutningerne. Gladsaxestrategien kobler udvikling til social, miljømæssig og økonomisk bæredygtighed. Det passer til en praksis, hvor energi ikke vurderes løsrevet fra funktion, indeklima og levetid. I et stærkt fagligt og socialt fællesskab og en uformel organisation kan faglig sparring og et bredt samarbejde på tværs af ingeniørgruppen og drift hjælpe med at finde de rigtige løsninger samlet set. Et socialt, humoristisk og ukompliceret åbent kontormiljø, hvor kolleger deler viden og erfaring, understøtter medarbejderens udvikling og trivsel. Når kunstig intelligens spiller en stadigt større rolle, bør den bruges som støtte til analyse og prioritering — med datakvalitet og faglig kontrol før en anbefaling påvirker et anlæg.")

CLOSING = ("Opslaget angiver tiltrædelse 1. februar 2027 eller efter nærmere aftale; den konkrete dato afklares i dialog. En samtale kan tage udgangspunkt i, hvordan drift, vedligehold, indeklima og energiforbrug prioriteres mellem de ejendomme, der bliver ansvarsområdet.")

# CV — dokumentation adskilt fra foreslået fremgangsmåde.
PROFILE = ("Gladsaxe søger en teknisk kollega, der kan forbinde ejendommenes HVAC-installationer, planlagt vedligehold, energidata og brugernes indeklima. Shahram Ajloo er elautoriseret maskinmester (LV/MV/HV), B.Tech i Technology Management & Mechanical Engineering, med praktisk erfaring fra HVAC/ventilation, teknisk drift, styring, SCADA, vedligehold og anlægsprojekter. Hos Biofos omfattede ansvaret kritiske pumper, HVAC, højspændingstavler og SCADA-overvågning i 24/7-drift; hos Novo Nordisk blev 37 CAPEX-projekter koordineret, og et PDCA-program reducerede energiomkostningerne med 40 %. I ELOHVAC udføres service og vedligehold på ventilations- og klimaanlæg. Erfaring med Gladsaxes navngivne bygningsautomatik- og ejendomsplatforme samt kommunale skoleejendomme er ikke dokumenteret; SCADA, SAP, CMMS og tekniske styringer giver et relevant udgangspunkt for systemoplæring.")

RESULTS = [
    ("−40 % energiomkostninger", "Novo Nordisk: gennemført via et PDCA-program; data- og omkostningsopfølgning i SAP ERP."),
    ("Kritisk 24/7-drift", "BIOFOS/Lynetten: forebyggende vedligehold, akut fejlfinding og teknisk opfølgning på pumper, HVAC, højspændingstavler og SCADA."),
    ("37 samtidige CAPEX-projekter", "Novo Nordisk: DKK 2–10 mio. pr. projekt; tværfaglig koordinering, test og aflevering."),
    ("Over 40 % produktivitetsløft", "ELOHVAC: AI-værktøjer til tilbudsberegning, tidsplaner, KS-tjeklister og KPI-dashboards."),
]

CAPABILITIES = [
    ("HVAC og teknisk bygningsdrift", "Ventilation, klima, pumper, el, styringer, tavler og fejlfinding fra ELOHVAC og Biofos; forebyggende og akut vedligehold."),
    ("Energidata og forbedring", "PDCA, SAP ERP, CMMS, Power BI, Excel/Power Query og Python; målte effekter skilles fra estimater og forslag."),
    ("Tekniske sager og aflevering", "Tilbud, beregning, planlægning, materialer, underentreprenører, KS, idriftsættelse og afleveringsdokumentation."),
    ("Samarbejde med drift og fag", "Drifts- og vedligeholdelsesansvar, projektkoordinering på tværs af 25 specialister, samt daglig ledelse af tekniske teams på 5+3 og 14 personer."),
]

EXPERIENCE = [
    ("Ejer / teknisk direktør / elautoriseret maskinmester", "ELOHVAC ApS · København · maj 2023 – nu", "5 elektrikere + 3 lærlinge · fuldt P&L",
     [("Service og vedligehold", "Udfører el-tekniske opgaver, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg; følger op fra akut udkald til afleveret anlæg."),
      ("Planlægning og leverandører", "Udarbejder tilbud og beregninger, planlægger arbejdet, styrer materialer og underentreprenører og følger KS samt afleveringsdokumentation."),
      ("Personale og sikkerhed", "Daglig planlægning, 1:1, MUS, lærlingeoplæring og arbejdsmiljøopfølgning for 5 elektrikere og 3 lærlinge; LOTO og risikovurdering."),
      ("Digital understøttelse", "Python- og Claude API-værktøjer til tilbudsberegning, tidsplaner, KS-tjeklister og KPI-dashboards; dokumenteret produktivitetsløft over 40 %.")]),
    ("Medejer og CTO / teknisk ansvarlig for AI-afdelingen", "Data Power Consultant ApS · København · 2024–2026 (sideløbende med ELOHVAC)", "4–10 personer i AI- og AI coding-afdelingen",
     [("Tekniske og industrielle applikationer", "Fra kravafdækning og arkitektur til datamodel, integration, idriftsættelse, dokumentation og overdragelse til kundens drift."),
      ("AI coding til teknisk design", "AI-assisterede beregninger, dimensionering og designvarianter for tekniske anlæg og industrielle komponenter, valideret fagligt før levering."),
      ("AI i arbejdsprocesser", "Indførte fælles standarder for kodegenerering, review og test samt AI-understøttet ledelsesrapportering og KPI-analyse.")]),
    ("Senior idriftsættelsesingeniør / projektleder, elsystem", "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024", "37 samtidige CAPEX-projekter á DKK 2–10 mio. · 25 specialister",
     [("Portefølje og tværfaglig koordinering", "Fremdrift, økonomi, risici og ressourcer koordineret på tværs af engineering, indkøb og anlæg; månedsrapportering til ledelse og bygherre."),
      ("Test, aflevering og energi", "FAT/SAT og IQ/OQ/PQ med nul kritiske fund ved aflevering. PDCA-programmet reducerede energiomkostninger med 40 %; SAP ERP til økonomi, aktiver og omkostninger.")]),
    ("Projekt- og værkstedsleder, ventilation og klima", "Ventek-Air · København · jan. 2022 – nov. 2022", "11 samtidige projekter · 14-personers team",
     [("Planlægning og leverance", "Ledte dagligt montage- og produktionsteamet; koordinerede kapacitet, fremdrift, entreprenører, sikkerhed, kvalitet og dokumentation frem til formel aflevering.")]),
    ("Vedligeholdelses- og driftsleder / værkstedstekniker", "BIOFOS (Lynetten) · København · aug. 2017 – jan. 2022", "Kritisk 24/7-anlæg · pumper, HVAC, højspændingstavler og SCADA",
     [("Drift, automatik og vedligehold", "Forebyggende vedligehold, akut fejlfinding og teknisk opfølgning på pumper, HVAC, højspændingstavler og SCADA-overvågning."),
      ("Forbedring og sikkerhed", "5S, Standard Work og PDCA på værksted og lager; reservedelsflow, LOTO, risikovurdering, APV og nærved-hændelser.")]),
    ("Elektromekaniker / produktionsteamleder", "ARJ Engineering · Teheran · dec. 2003 – mar. 2010", "12 mekanikere og teknikere",
     [("Teknisk fejlfinding og teamkoordinering", "Vagtplanlægning, materialestyring og målopfølgning samt fejldiagnose, reparation og rodårsagsanalyse på industrielle el- og mekaniske anlæg.")]),
]

EDUCATION = [
    ("B.Tech (EQF niveau 6) — Technology Management & Mechanical Engineering", "Copenhagen School of Marine Engineering & Technology Management · 2017–2022"),
    ("El- og maskinteknisk design, elteknik (EQF niveau 6)", "Tehran Technical University · 2000–2003"),
    ("HF — matematik og fysik", "VUC · 2012–2017"),
]
CERTS = [
    ("Elautoriseret maskinmester (LV/MV/HV)", "Sikkerhedsstyrelsen · maj 2023"),
    ("Køleteknik og klimaanlæg (AMU)", "Mercantec · 2021"),
    ("PRINCE2 — certificeret projektleder", "AXELOS / PeopleCert"),
    ("Lean- og Six Sigma-metoder", "Arbejdet med i praksis; ikke certificeret"),
]

METHODS = [
    ("Bygningsdrift og vedligehold", "HVAC · ventilation · klima · pumper · styringer · SCADA · forebyggende vedligehold · akut fejlfinding"),
    ("Energi og data", "PDCA · SAP ERP · CMMS · Power BI · Excel/Power Query · Python · KPI-opfølgning · baseline og effektkontrol"),
    ("Tekniske arbejder", "Tilbud og beregning · projektplan · materialestyring · håndværkere/underentreprenører · KS · idriftsættelse · aflevering"),
    ("Sikkerhed og kvalitet", "Elautorisation LV/MV/HV · LOTO · APV · risikovurdering · FAT/SAT · IQ/OQ/PQ · dokumentation"),
    ("Ledelse og samarbejde", "PRINCE2 · LEAN · Six Sigma-værktøjer · MUS · 1:1 · kompetencematrix · GROW · SBI · RACI"),
]

REQUIREMENTS = [
    ("Ingeniør, maskinmester eller tilsvarende teknisk uddannelse", "Elautoriseret maskinmester (LV/MV/HV) og B.Tech i Technology Management & Mechanical Engineering, Copenhagen School of Marine Engineering & Technology Management, 2017–2022."),
    ("God teknisk viden og erfaring med bygningernes styrende teknologi", "BIOFOS: pumper, HVAC, el-tavler og SCADA-overvågning. ELOHVAC: teknisk HVAC-service. Gladsaxes specifikke bygningsautomatik kræver oplæring."),
    ("Teknisk drift og vedligehold af kommunale ejendomme", "BIOFOS: teknisk drift og vedligehold i kritisk 24/7-procesanlæg. ELOHVAC: HVAC-service for kunder. Kommunal ejendomsdrift er ikke tidligere dokumenteret."),
    ("Projektere og udføre mindre tekniske anlægssager", "ELOHVAC: tilbud, plan, materialer, underentreprenører, udførelse, KS og aflevering. Ventek-Air: koordinering af 11 samtidige anlægsprojekter."),
    ("Betjene bygningsautomatik til energioptimering, styring og overvågning", "BIOFOS: SCADA-overvågning af procesanlæg. Direkte betjening af Gladsaxes bygningsautomatik og Digital Bygningsdata, Dalux, EG Omega eller Energy Projects er ikke dokumenteret."),
    ("Løbende energieffektivisering", "Novo Nordisk: PDCA-program reducerede energiomkostninger med 40 %. Den dokumenterede effekt tilskrives dette forløb, ikke kommunale bygninger."),
    ("Godt indeklima for bygningernes brugere", "ELOHVACs ventilations- og klimaarbejde samt Ventek-Airs ventilationsprojekter giver relevant HVAC-erfaring. Skolebrugeres indeklimamålinger er ikke dokumenteret."),
    ("Kontakt med håndværkere og entreprenører", "ELOHVAC: koordinering af håndværkere, underentreprenører, materialer, sikkerhed og KS. Ventek-Air: entreprenør- og montagekoordinering."),
    ("Løbende dialog med driftsfolk på ejendommene", "BIOFOS-rollen var tæt på daglig drift og vedligehold; Novo Nordisk indebar koordinering med anlæg og drift. Lokale rutiner skal etableres i Gladsaxe."),
    ("Analysere energiforbrugsdata i energistyringssystem", "Novo Nordisk: energirelateret PDCA-opfølgning og 40 % lavere energiomkostninger. Gladsaxes energistyringssystem og dets datakilder skal læres."),
    ("Planlægge energioptimering på baggrund af data", "Overførbar PDCA-praksis; foreslået baseline pr. ejendom, prioritering med hensyn til komfort og drift samt kontrol af målt effekt."),
    ("Afhjælpe akutte nedbrud sammen med kolleger", "BIOFOS: akut fejlfinding i kritisk 24/7-drift på pumper, HVAC og højspændingstavler; ELOHVAC: teknisk service og fejlretning."),
    ("Ansvar for en del af ejendommene, forventeligt skoler", "Selvstændigt teknisk driftsansvar i BIOFOS og ELOHVAC samt koordinering af 37 CAPEX-projekter hos Novo Nordisk. Kommunale skoler er en ny ramme."),
    ("Planlægge vedligehold, renovering og energioptimering af HVAC", "BIOFOS: forebyggende vedligehold; ELOHVAC: HVAC-service; Ventek-Air: ventilationsprojekter. Gladsaxes vedligeholdsplaner er ikke tidligere udarbejdet."),
    ("Bredt tværfagligt samarbejde om samlet ejendomsløsning", "Novo Nordisk: koordinering af 25 specialister på tværs af engineering, indkøb og anlæg. ELOHVAC: samarbejde med kunder, håndværkere og leverandører."),
    ("Moderne, bæredygtige og energieffektive bygninger", "Relevant erfaring med energiopfølgning, HVAC og vedligehold; Novo Nordisk-resultatet var 40 % lavere energiomkostninger dér, ikke et løfte for Gladsaxe."),
    ("Digital Bygningsdata, Dalux, EG Omega og Energy Projects", "SAP ERP, CMMS, Excel/Power Query, Power BI og Python er dokumenteret. Erfaring med de fire navngivne Gladsaxe-systemer er ikke dokumenteret."),
    ("Kunstig intelligens i den fortsatte udvikling", "Som CTO ledte kandidaten AI-arbejde og indførte udviklingsstandarder; ELOHVAC AI-værktøjer øgede produktiviteten over 40 %. Bygningsautomatik er ikke påstået."),
    ("Samarbejde med nære kolleger", "Dokumenteret i BIOFOS-drift, Ventek-Airs 14-personers team og Novo Nordisks tværfaglige koordinering af 25 specialister."),
    ("Gode relationer til eksterne samarbejdspartnere", "ELOHVAC: kunder, leverandører og underentreprenører gennem tilbud, planlægning, kvalitet og aflevering; Ventek-Air: entreprenørkoordinering."),
    ("Tiltrædelse 1. februar 2027 eller efter aftale", "Stillingsopslaget angiver 1. februar 2027 eller efter aftale; konkret tiltrædelsesdato afklares i dialog med Gladsaxe Kommune."),
]

LANGUAGES = "Dansk (modersmål) · Engelsk (professionelt) · Persisk/farsi (modersmål) · Kørekort B"



def build(path=OUTPUT):
    m = MasterDoc(TEMPLATE, lang="da-DK")

    # Side 1: opgaveorienteret ansøgning.
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta(RECIPIENT)
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, SUBJECT, bold=True, color="1A1A1A")
    for text, kind in LETTER:
        m.para(text, after=75)
    for label, body in SOLUTION:
        m.bullet(label, body, after=55)
    m.para(PLAN, after=65)
    m.para(CULTURE, after=65)
    m.para(CLOSING, after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo · +45 93 99 95 14 · ajlooshahram@gmail.com", after=0)

    # CV.
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "TEKNISK PROFIL")
    m.para(PROFILE, after=75)

    m.section("RELEVANTE RESULTATER")
    for label, body in RESULTS:
        m.bullet(label, body, after=30)

    m.section("FAGLIGT MATCH TIL EJENDOMSCENTERET")
    for label, body in CAPABILITIES:
        m.bullet(label, body, after=35)

    m.section("ERHVERVSERFARING")
    for title, meta, scope, bullets in EXPERIENCE[:2]:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "ERHVERVSERFARING (FORTSAT)")
    for title, meta, scope, bullets in EXPERIENCE[2:]:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section("UDDANNELSE")
    for title, meta in EDUCATION:
        m.edu(title, meta)
    m.section("AUTORISATIONER, KURSER OG METODER")
    for title, meta in CERTS:
        m.edu(title, meta)

    m.section("DIGITAL DRIFT OG TEKNISKE METODER")
    m.models_table("VÆRKTØJER OG ANVENDELSE", ("Område", "Dokumenteret praksis"), METHODS)
    m.section("SPROG OG PRAKTISK")
    m.para(LANGUAGES, after=55, justify=False)

    m.page_break()
    m.resume_header(NAME, "Ejendomsdrift | vedligehold | energi | HVAC", CONTACT, "DOKUMENTERET MATCH OG OVERFØRSEL")
    matrix = m.models_table("KRAVMATRIX", ("Krav i stillingsopslaget", "Dokumentation / foreslået tilgang"), REQUIREMENTS, widths=(4100, 6246))
    header_props = matrix.rows[1]._tr.get_or_add_trPr()
    repeat_header = OxmlElement("w:tblHeader")
    repeat_header.set(qn("w:val"), "true")
    header_props.append(repeat_header)


    return m.save(path, title="Ansøgning og CV — Gladsaxe Kommune, Ejendomscenteret", subject=SUBJECT,
                  keywords="Ejendomsdrift; energi; HVAC; SCADA; vedligehold; AI; kommunal drift")


if __name__ == "__main__":
    print(build())
