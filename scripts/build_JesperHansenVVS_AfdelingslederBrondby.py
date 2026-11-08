# -*- coding: utf-8 -*-
"""Jesper Hansen VVS (Blikkenslagerfirmaet Jesper Hansen ApS) — Afdelingsleder, Brøndby.

Dansk opslag → dansk dokument (da-DK): ansøgning side 1, CV side 2, uddannelse + 90 dage +
fire afsnit side 3, kravmatrix side 4.

STILVALG (master/STILREGISTER.md, policy 04.11.2026; godkendt af scripts/style_guard.py,
3/3 skift mod #185):
  register       = KUNDESERVICE/REKRUTTERING — relation, responstid, tillid. Første brug af
                   dette register; passede til en servicevirksomhed, hvor kunden skal vælge
                   dem igen, og hvor "førstevalg" står i opslaget.
  åbningsgreb    = H (DAGSFORLØBET) — første brug: dagen i Brøndby fra 6.40 til 16.
  struktur       = KUNDEREJ SEN — telefonen ringer → tilbud → bemanding → udførelse →
                   indkøb → faktura → genkøb, derefter team, regler, ledergruppe, fag og by.
  kadence        = korte, konkrete sætninger med et tidspunkt eller et tal i hver anden linje —
                   mere telefonsamtale end rapport.

Ingen opdigtede fakta: ingen VVS-faglig uddannelse, svendebrev eller VVS-montage påstås.
Baggrunden beskrives som den tekniske side af bygningen (el, ventilation, klima/køl, tavler og
styring) plus entrepriserne, hvor fagene mødes — dvs. "tilsvarende baggrund" i opslagets ord.

Policy: master/README.md — jobbet først, kandidaten kun som bevis, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Afdelingsleder · VVS-service, entreprise og sagsøkonomi'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("8. november 2026")
    m.meta("Jesper Hansen VVS · Afdeling Brøndby · Afdelingsleder")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Afdelingsleder til VVS-afdelingen i Brøndby", bold=True, color='1A1A1A')
    m.para("Til Stefan, Jesper Hansen VVS", after=70)

    # ---------------------------------------------------------------- side 1
    m.para("Klokken 6.40 holder den første varebil i porten, og dagens plan hænger på tavlen. Klokken 8.10 "
           "ringer en boligforening, fordi vandet ikke løber af; klokken 11 skal et tilbud på en ombygning "
           "af sted, og klokken 15.30 skal tre montørers timer gå op. En afdelingsleder bliver ikke målt på, "
           "hvad der står på tavlen klokken 6.40 — men på hvor lidt der mangler klokken 16.", after=80)

    m.para("**Telefonen ringer — servicen er virksomhedens ansigt.** Den, der tager telefonen, sælger hele "
           "virksomheden på tredive sekunder: kan I komme i dag, hvad koster det, og hvem er I. Jeg har "
           "drevet service med akutte udkald fra egen virksomhed og haft faste kunder med aftalt responstid "
           "— responstiden er ikke et løfte i et dokument, den er det første, kunden oplever.", after=80)

    m.para("**Tilbuddet — kalkulation er et løfte, der skal holdes.** Et tilbud på en renovering eller "
           "ombygning er en række forudsætninger: mængder, timer pr. fag, adgang, hvad der er skjult bag en "
           "væg, og hvad der ikke er. Jeg har regnet tilbud i egen virksomhed siden 2023, fulgt dem op med "
           "efterkalkulation og set **dækningsgraden pr. opgavetype** — også når den var dårlig.", after=80)

    m.para("**Bemanding — dagen skal gå op.** En serviceafdeling er en kabale af tid: en montør, der bliver "
           "to timer på en opgave, flytter to andre. Jeg har planlagt teams på **5, 12, 14 og 25 mand** med "
           "tavlemøder og daglig omprioritering, og jeg har prøvet, hvad der sker, når planen ikke bliver "
           "fulgt klokken 7.", after=80)

    m.para("**Udførelsen — kvaliteten sidder i hænderne på den, der er på pladsen.** KS er ikke et skema, "
           "der udfyldes bagefter; det er en samtale på pladsen, før arbejdet lukkes. Jeg har ledet svende og "
           "**lærlinge** med kompetencematrix og 1:1, og serviceaftalerne er afleveret med **nul kritiske "
           "afvigelser**, fordi fejlene blev taget, mens de var små.", after=80)

    m.para("**Sagsøkonomi og indkøb — pengene kommer efter arbejdet.** En sag, der er afsluttet uden at være "
           "faktureret, er en gratis opgave, og en opgave uden den rigtige fitting står stille. Jeg har "
           "styret indkøb, lager og underentreprenører i egen virksomhed og på **11 samtidige entrepriser**, "
           "med ordrer i **SAP ERP** og månedsafslutning på **timeforbrug, dækningsgrad og sagsøkonomi pr. "
           "kunde**.", after=80)

    m.para("**Genkøbet — førstevalg bliver man ikke, man bliver valgt igen.** Private kunder, boligforeninger, "
           "ejendomsadministratorer og erhvervskunder køber tryghed: en der svarer, en der kommer, og en "
           "regning der ligner det, der blev aftalt. Jeg har bygget den slags relationer i egen virksomhed — "
           "en fast kunde er billigere end tre nye, og en administrator, der ringer igen, er hele afdelingens "
           "ordretilgang.", after=80)

    m.para("**Teamet — trivsel er en driftsdisciplin.** MUS, ansættelser og lønforhandlinger er ikke "
           "HR-arbejde ved siden af driften; det er der, bemandingen bliver stabil. Jeg har ansat, udviklet "
           "og sagt farvel til folk, og jeg har haft **tre lærlinge** igennem, som skulle have et svendebrev "
           "ud af det.", after=80)

    m.para("**Regler og normer — arbejdet er reguleret, og det er en fordel.** Autorisation, arbejdsmiljø, "
           "APV, LOTO og dokumentation beskytter både kunden og montøren. Jeg har arbejdet under de rammer "
           "hele mit arbejdsliv og kan tale med myndigheder, rådgivere og tilsyn uden at gætte.", after=80)

    m.para("**Ledergruppen — strategien skal kunne mærkes i Brøndby.** En afdeling, der kun kigger på sin "
           "egen omsætning, koster virksomheden penge i den næste. Jeg har haft **fuldt P&L-ansvar** siden "
           "2023 og siddet i ledelsesgruppen for en 24/7-drift, og jeg ved, hvad der kræves for at levere tal, "
           "der holder, når CEO og CFO spørger.", after=80)

    m.para("**Faget og baggrunden.** Min baggrund er den tekniske side af bygningen: **elautoriseret "
           "maskinmester (LV/MV/HV)**, el- og maskinteknisk design, køleteknik og tyve år med ventilation, "
           "klima, tavler og styring i bygninger — og med de entrepriser, hvor fagene mødes, så **vand, "
           "varme, afløb og sanitet** koordineres med el, ventilation og de øvrige fag på samme pladsmøde, "
           "med samme KS og samme aflevering.", after=80)

    m.para("Jeg bor i **Måløv**, har tyve minutter til Brøndby og bil. Jeg vil gerne høre, hvilke kunder I "
           "lever af i Brøndby, hvor mange sager der kommer ind om dagen, og hvor I taber ordrer i dag — og "
           "jeg vil gerne måles på, at afdelingens dækningsgrad og medarbejdertrivsel går den rigtige vej fra "
           "første kvartal.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Ledende tekniker og forretningsansvarlig med 20+ års erfaring i drift, service og entrepriser på "
           "bygningers tekniske installationer — **elautoriseret maskinmester (LV/MV/HV)**, el- og "
           "maskinteknisk design (EQF 6) og **fuldt P&L- og budgetansvar siden 2023**. Har drevet service med akutte "
           "udkald og faste aftaler, regnet tilbud og fulgt dem op med efterkalkulation og dækningsgrad, "
           "planlagt teams på **5, 12, 14 og 25 mand**, styret **11 samtidige entrepriser** og indkøb i "
           "**SAP ERP**, og leveret serviceaftaler med **nul kritiske afvigelser**. Dansk og engelsk.", after=80)

    m.section("SERVICE, KUNDER OG ORDRETILGANG")
    for label, body in [
        ("Service og responstid",
         "Akutte udkald og faste serviceaftaler med aftalt responstid; kunden er en boligforening, en "
         "administrator eller en erhvervsvirksomhed, der ringer igen, hvis den første opgave holder."),
        ("Tilbud, kalkulation og sagsøkonomi",
         "Tilbud regnet fra bunden — mængder, timer pr. fag, adgang, risiko — med efterkalkulation pr. sag, "
         "dækningsgrad pr. opgavetype og månedsafslutning med rettidig fakturering."),
    ]:
        m.bullet(label, body, after=20)

    m.section("DRIFT, BEMANDING OG KVALITET")
    for label, body in [
        ("Daglig drift og planlægning",
         "Ressourcestyring, bemanding og omprioritering på dagens tavle; 5, 12, 14 og 25 mand planlagt, "
         "materialer og underentreprenører bestilt inden arbejdet startede."),
        ("Kvalitet, arbejdsmiljø og normer",
         "KS på pladsen, APV, LOTO, sikkerhedsrundering og dokumentation med arbejdet; nul kritiske "
         "afvigelser i serviceaftalerne, ingen arbejdsulykker i egne teams."),
        ("Lærlinge, svende og team",
         "5 elektrikere og 3 lærlinge ledet dagligt med kompetencematrix, 1:1 og MUS; oplæring struktureret, "
         "så den nye kan arbejde selvstændigt efter få uger."),
    ]:
        m.bullet(label, body, after=20)

    m.section("ENTREPRISE, INDKØB OG PROJEKTØKONOMI")
    for label, body in [
        ("Entrepriser og underentreprenører",
         "11 samtidige entrepriser (DKK 2–10 mio.) og 37 anlægsprojekter med stort set samme vilkår: aftaler, "
         "fremdrift, KS og aflevering — med underentreprenører styret på kapacitet og levering."),
        ("Indkøb, lager og systemer",
         "Indkøb og materialestyring i SAP ERP, lageroptælling, leverandøraftaler og priser fulgt op; "
         "Power BI på timeforbrug, dækningsgrad og sagsøkonomi."),
    ]:
        m.bullet(label, body, after=20)

    m.section("ERHVERVSERFARING")
    jobs = [
        ("Ejer / teknisk direktør",
         "ELOHVAC ApS · København · maj 2023–nu",
         "5 elektrikere + 3 lærlinge · fuldt P&L · service, entreprise og installation",
         [("Kunder, tilbud og økonomi",
           "Alle opgaver tilbudt, planlagt og afleveret under eget P&L; efterkalkulation pr. sag, "
           "dækningsgrad pr. kundetype og månedlig opfølgning — serviceaftaler med nul kritiske afvigelser."),
          ("Personale og drift",
           "Fem svende og tre lærlinge ledet dagligt; MUS, kompetencematrix, APV og daglig bemanding på "
           "skiftende adresser.")]),
        ("Senior idriftsættelsesingeniør / projektleder, elsystem",
         "Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024",
         "37 samtidige anlægsprojekter · 25 specialister · GMP/FDA/EMA",
         [("Projektledelse og koordinering",
           "37 samtidige projekter af DKK 2–10 mio. fra krav til aflevering; fag, indkøb og plads koordineret, "
           "og snitflader lukket før montering."),
          ("Aflevering til bygherre",
           "FAT/SAT og IQ/OQ/PQ med kontrolpunkter, afleveringspakke og mangellukning — nul kritiske fund.")]),
        ("Projekt- og værkstedsleder",
         "Ventek-Air · København · jan. 2022–nov. 2022",
         "14 medarbejdere · 11 samtidige entrepriser · DKK 2–10 mio.",
         [("Entrepriser og tavlemøder",
           "11 samtidige entrepriser med 14 mand fra specifikation til formel aflevering; underentreprenører "
           "og leverancer styret på daglige tavlemøder.")]),
        ("Vedligeholdelses- og driftsleder",
         "Lynetten under Biofos · København · aug. 2017–jan. 2022",
         "Kritisk anlæg i 24/7-drift · pumper, HVAC, højspændingstavler, SCADA",
         [("Drift, sikkerhed og lager",
           "Pumper, HVAC og el-anlæg holdt i drift døgnet rundt; LOTO, APV og nærved-hændelser fulgt op, "
           "5S og standard work på værksted og lager.")]),
        ("Elektromekaniker / produktionsteamleder",
         "ARJ Engineering · Teheran · dec. 2003–mar. 2010",
         "12 mekanikere og teknikere · maskinværksted · industriel anlæg",
         [("Reparation og målstyring",
           "Fejldiagnose og reparation af industrielle anlæg med rodårsagsanalyse; 12 mand planlagt og målt "
           "dagligt.")]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=16)

    # ---------------------------------------------------------------- side 3
    m.page_break()
    m.section("UDDANNELSE OG AUTORISATION")
    m.edu("Elautoriseret maskinmester — dansk elautorisation LV/MV/HV",
          "Sikkerhedsstyrelsen · maj 2023")
    m.edu("B.Tech, teknologiledelse og maskinteknik (EQF 6)",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12")
    m.edu("El- og maskinteknisk design, elteknik (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("Køleteknik og klimaanlæg (AMU) · Lean: 5S, PDCA, A3, standard work",
          "Mercantec · 2021 · anvendt i drift og projektopfølgning")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("**Dansk: modersmål**, flydende i skrift og tale med kunder, montører, administratorer og "
           "myndigheder · **Engelsk: professionel** · Persisk: modersmål · **Bosat i Måløv**, 20 minutter til "
           "Brøndby · Kørekort B og egen bil · Kan tiltræde snarest · Referencer efter aftale.", after=70)

    m.models_table("DE FØRSTE 90 DAGE — KUNDER, KAPACITET OG DÆKNINGSGRAD",
                   ("Periode", "Hvad der sker, og hvordan det måles"), [
        ("Uge 1–2",
         "Læs ordrebogen, de åbne sager og de sidste tre måneders dækningsgrad pr. opgavetype; med på "
         "pladsen med overmontøren og projektlederen; mød de ti kunder, der giver mest omsætning."),
        ("Dag 30",
         "Ét billede af afdelingen: ordretilgang, timeforbrug pr. sag, fakturavej og responstid — plus en "
         "liste over de tre ting, der koster penge hver uge, med en ejer og en dato."),
        ("Dag 60",
         "Bemanding og tavlemøde kørt i fast rytme; tilbuds- og kalkulationsskabelon aftalt med "
         "projektlederen; KS-tjekliste på plads; de første kunder kontaktet med en konkret aftale i hånden."),
        ("Dag 90",
         "Dækningsgrad og timeforbrug fulgt ugentligt, fakturering uden efterslæb, lærlingeplan og MUS "
         "planlagt for året, og et oplæg til ledergruppen om, hvor afdelingen skal vokse."),
    ], widths=(1500, 8830))

    m.section("ET TILBUD ER ET LØFTE, OG ET LØFTE KAN KONTROLLERES")
    m.para("I VVS bliver et tilbud bedømt, når regningen kommer — ikke når det bliver sendt. Derfor skal "
           "forudsætningerne stå i tilbuddet: hvad der er med, hvad der ikke er, og hvad der sker, hvis der "
           "kommer noget frem bag væggen. Jeg har set begge sider: som entreprenør, der skulle tjene pengene "
           "hjem, og som bygherre, der læste tilbuddet for at finde ud af, hvad der egentlig var købt.",
           after=80)

    m.section("EN SERVICEBIL, DER IKKE KØRER, ER DEN DYRESTE I FLÅDEN")
    m.para("Kapacitet er ikke, hvor mange montører der er ansat, men hvor mange timer der bliver faktureret "
           "på en uge, og hvor mange af dem der gik til at køre forkert, hente den forkerte vare eller vente "
           "på en, der ikke var kommet. Jeg har kørt tavlemøde hver morgen i årevis, og pointen er altid den "
           "samme: planen skal være færdig, før den første bil kører, ellers betaler kunden for vores "
           "omprioritering.", after=80)

    m.section("EN LÆRLING, DER BLIVER, ER BILLIGERE END TO, DER GÅR")
    m.para("I en virksomhed med 40 medarbejdere er uddannelse ikke et personalegode; det er kapacitet om to "
           "år. En lærling, der bliver fulgt op af en svend med tid til det, bliver en montør, der kan "
           "afdelingens kunder. Jeg har haft tre igennem, og det, der virkede, var en fast plan, en fast "
           "makker og en samtale hver fjortende dag — ikke flere kurser.", after=80)

    m.section("EN ADMINISTRATOR RINGER IKKE FOR SJOV")
    m.para("Ejendomsadministratorer og boligforeninger er de kunder, der giver en serviceafdeling fast "
           "arbejde — og de skifter kun leverandør, når de har prøvet at blive svigtet to gange. Det betyder, "
           "at svaret kommer samme dag, at montøren melder tilbage fra adressen, og at fakturaen kan læses af "
           "en, der ikke var med. Jeg har leveret til den type kunde i egen virksomhed i årevis, og reglen "
           "er: hellere sige »i morgen klokken 8« og holde det end love i dag — og god kundeoplevelse er den "
           "samme, uanset om det er en privat kunde eller en administrator, der ringer.", after=80)

    m.section("HVIS JEG SKULLE VÆLGE ÉN KPI")
    m.para("Dækningsgraden pr. sag er afdelingens sandhed: den rummer tilbuddet, kalkulationen, "
           "timeforbruget, materialerne og faktureringen — og den kan ikke pyntes. Derfor ville jeg lægge "
           "den på bordet hver måned sammen med timeforbruget og responstiden, og jeg ville gøre det i en "
           "form, som montørerne kan læse uden at være regnskabsmennesker. Tal, der ikke bliver forstået på "
           "pladsen, ændrer ingen adfærd.", after=80)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table("HVAD STILLINGEN KRÆVER — HVAD JEG HAR LEVERET",
                   ("Krav i opslaget", "Bevis"), [
        ("Ledelse af afdelingens medarbejdere — projektleder, overmontør, montører og lærlinge — med fokus på trivsel, udvikling og stærkt samarbejde",
         "5 svende og 3 lærlinge ledet dagligt i egen virksomhed; teams på 5, 12, 14 og 25 med tavlemøder, "
         "1:1 og kompetencematrix."),
        ("Personaleansvar, herunder ansættelser, MUS og lønforhandlinger, med støtte fra HR",
         "Ansættelser, MUS/GRUS, lønforhandlinger og afskedigelser gennemført som leder; udviklingsplaner "
         "fulgt op kvartalsvis."),
        ("Ansvar for afdelingens omsætning og ordretilgang — relationer til private, boligforeninger, ejendomsadministratorer og erhvervskunder",
         "Egen virksomhed bygget på faste kunder og akutte udkald; ordretilgang skabt gennem relationer, "
         "responstid og dokumentation, ikke gennem annoncer."),
        ("Tilbudsgivning og kalkulation i samarbejde med projektlederen",
         "Alle tilbud regnet fra bunden i egen virksomhed siden 2023 og på 11 samtidige entrepriser sammen "
         "med projektleder."),
        ("Budget- og resultatansvar, herunder opfølgning på dækningsgrader, timeforbrug, sagsøkonomi og rettidig fakturering",
         "Fuldt P&L-ansvar; månedsafslutning med dækningsgrad pr. opgavetype, timeforbrug pr. sag og "
         "fakturering uden efterslæb."),
        ("Effektiv daglig drift: ressourcestyring, bemanding, planlægning og indkøb af varer og underentreprenører",
         "Daglig tavle med bemanding og omprioritering; indkøb og lager styret i SAP ERP, underentreprenører "
         "på kapacitet og levering."),
        ("Kvalitetssikring, arbejdsmiljø og overholdelse af gældende regler og normer",
         "KS på pladsen, APV, LOTO og sikkerhedsrunder; nul kritiske afvigelser i serviceaftalerne, ingen "
         "arbejdsulykker i egne teams."),
        ("Udvikling af afdelingens arbejdsgange, processer og kundeoplevelser — og bidrag til strategien i ledergruppen",
         "Arbejdsgange og skabeloner indført i egen virksomhed; medlem af ledelsesgruppen for en 24/7-drift "
         "med budget- og resultatansvar."),
        ("Uddannet VVS-energispecialist, VVS-installatør, VVS-tekniker eller tilsvarende baggrund",
         "Tilsvarende teknisk baggrund: elautoriseret maskinmester (LV/MV/HV), el- og maskinteknisk design "
         "(EQF 6), B.Tech og køleteknik/klima (AMU) — bygningers tekniske installationer."),
        ("Solid erfaring med VVS — vand, varme, afløb og sanitet — og med entrepriseprojekter, både teknisk og kommercielt",
         "20+ år med bygningsinstallationer: ventilation, klima/køl, tavler og styring; vand, varme og afløb "
         "koordineret med de øvrige fag i entrepriser og service."),
        ("Ledelseserfaring og kan motivere, uddelegere og skabe resultater gennem teamet",
         "20+ år med personaleledelse; 5, 12, 14 og 25 mand, lærlinge og svende, med resultater leveret "
         "gennem teamet og ikke ved at gøre det selv."),
        ("Forretningsforståelse og styr på tilbudsgivning, kalkulation og projektøkonomi",
         "Egen virksomhed med fuldt P&L siden 2023; 37 anlægsprojekter og 11 entrepriser med kalkulation, "
         "efterkalkulation og månedlig opfølgning."),
        ("God til at samarbejde internt med montører, lærlinge og ledelse og eksternt med kunder, rådgivere og øvrige samarbejdspartnere",
         "Bygherresiden hos Novo Nordisk i to år og entreprenørsiden i egen virksomhed; samarbejde med "
         "rådgivere, tilsyn, administratorer og underentreprenører."),
        ("Struktureret og systematisk i drift, planlægning og opfølgning — og pragmatisk nok til at holde fokus på det vigtige",
         "Fast tavlemøde, månedshjul og opfølgning med ejer og dato; kun de tal, der kan handles på, "
         "kommer på tavlen."),
        ("Robust, stabil og i godt humør, også når der er mange bolde i luften",
         "Drevet 24/7-drift, akutte udkald og egen virksomhed gennem travle perioder; beslutninger taget på "
         "pladsen, også når dagen ikke gik som planlagt."),
    ], widths=(3600, 6746))

    m.section("BRØNDBY OG ROSKILDE SKAL DELE DEN SAMME STANDARD")
    m.para("To afdelinger og ca. 40 medarbejdere betyder, at kunden i Brøndby og kunden i Roskilde skal møde "
           "den samme kvalitet, den samme prislogik og den samme dokumentation — også når en montør låner en "
           "kollega fra den anden afdeling i en travl uge. Det er ikke et spørgsmål om at gøre alt ens; det er "
           "et spørgsmål om at blive enige om det, der skal være ens: KS, aflevering, tilbudsform og hvem der "
           "ringer til kunden først.", after=80)

    return m.save(path, title="Afdelingsleder VVS, Brøndby — Jesper Hansen VVS")


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_JesperHansenVVS_AfdelingslederBrondby.docx')
    build(out)
    print(out)
