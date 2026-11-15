# -*- coding: utf-8 -*-
"""Bravida — Projektchef til stor el-entreprise, Brøndby (reachmee rmjob=11830).

Dansk opslag → dansk dokument (da-DK): ansøgning side 1, CV side 2, uddannelse +
90 dage + fire afsnit side 3, kravmatrix side 4.

STIL (jf. master/STILREGISTER.md, bindende policy 04.11.2026):
- register: kommerciel-forretningsmæssig (adskiller sig fra entreprenør-registret i
  Bravida-byggene #176 og #178 — samme arbejdsgiver, tre forskellige stemmer)
- åbningsgreb: G (spørgsmålet)
- struktur side 1: Målestokken som tidslinje — uge 1 → måned 1 → fase 2 → aflevering,
  hvor hvert afsnit åbner med det tidspunkt og det tal, beslutningen falder på
- kadence: længere, mere fortællende sætninger i ansøgningen, kortere og hug-agtige
  sætninger i CV'et (omvendt af de sidste fire dokumenter)
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Projektchef · El-entreprise, projektøkonomi og ledelse af projektledere'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4. november 2026")
    m.meta("Bravida Danmark A/S · El-entreprise · Brøndby")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Projektchef til stor el-entreprise", bold=True, color='1A1A1A')
    m.para("Til rekrutteringen i Bravida, Brøndby", after=70)

    # ---------------------------------------------------------------- side 1
    m.para("Hvornår begynder en el-entreprise egentlig at tabe penge? Sjældent på afleveringsdagen, hvor "
           "regnskabet gøres op. Det sker tidligere: i uge 3, hvor en ændring bliver udført, fordi det er "
           "nemmere end at varsle den; i uge 11, hvor fremdriften reddes med mandskab, der ikke er ført ind "
           "i kalkulationen; og i uge 30, hvor alle omkring bordet er enige om, at det nok skal gå. "
           "Projektchefens arbejde er at gøre de tal synlige, mens der stadig er tid til at handle — og gøre "
           "det, så projektlederne har lyst til at lægge dem frem.", after=80)

    m.para("**Uge 1 — det, der blev solgt.** En entreprise arves af den, der regnede den. Derfor læser jeg "
           "kalkulationen før fremdriftsplanen: mængder, timer pr. fag, adgang, forudsætninger om "
           "tid og rækkefølge og det **AB 18**- eller totalentreprisegrundlag, kunden har skrevet under på. "
           "I min egen virksomhed har jeg selv regnet tilbuddene og selv stået med regningen, når "
           "forudsætningerne ikke holdt — og den erfaring gør, at jeg kan se på en projektleders tilbud, hvor "
           "det er tyndslidt, før den første arbejdsseddel er skrevet.", after=80)

    m.para("**Måned 1 — hvert projekt på én side.** En projektchef, der selv skal regne, er en projektleder "
           "med for mange projekter. Derfor skal hver projektleder kunne fremlægge sit projekt på én side: "
           "**dækningsgrad** pr. fase, timer mod kalkule, udestående og ikke-faktureret, **tillæg** varslet "
           "eller ikke, næste milepæl og den ventende beslutning. Den side gennemgår vi på et fast "
           "**månedshjul**. På **37 samtidige kapitalprojekter** med **25 specialister** var det, der holdt "
           "projekterne på sporet, ikke flere møder, men at det samme tal betød det samme for alle.",
           after=80)

    m.para("**Fase 2 — ændringerne.** Midt i en stor el-entreprise ændrer byggeriet sig, og arbejdet bliver "
           "mere, end der blev solgt. En ændring, der udføres uden "
           "at være varslet, er ikke en service; det er en gave, og gaven bliver dyrere, jo længere man "
           "venter med at sende den. Derfor dokumenteres ændringer samme uge, de opdages, med begrundelse og "
           "konsekvens for tid og penge, og kunden får besked, mens arbejdet stadig kan stoppes — det er den "
           "eneste måde, en kunderelation kan holde.", after=80)

    m.para("**Onsdag i uge 12 — økonomi og fremdrift på samme bord.** Den klassiske fejl er ikke, at "
           "økonomien og planen er forkerte; det er, at de styres i to forskellige møder med to uger "
           "imellem — så optimerer man det ene og betaler med det andet. Jeg har lagt økonomien ind i "
           "fremdriftsmødet: samme tavle, samme tal, samme beslutning, og data hentet i **SAP ERP** og "
           "**Power BI**, så opgørelsen er færdig, når mødet starter. I egen drift gav det **over 40 % "
           "produktivitetsløft**.", after=80)

    m.para("**Kundemødet — forventningsafstemning, ikke status.** En kunde, der bliver overrasket over en "
           "regning eller en forsinkelse, holder penge tilbage. Derfor "
           "er kundemødet ikke et referat, men en afstemning af, hvad der er købt, ændret og på vej, og hvad "
           "det betyder for datoen. Jeg har siddet på bygherrens side i **Novo Nordisk** i to år i "
           "Kalundborg, hvor entrepriser blev afleveret under **GMP/FDA/EMA**-krav — og jeg ved, hvad kunden "
           "skriver ned, når han kommer hjem: ikke hvad der blev lovet, men hvad der blev holdt.", after=80)

    m.para("**Pladsen — den samtale en projektleder ikke altid kan tage.** Når en tavle ikke kan "
           "ibrugtages som planlagt, når en føringsvej ikke kan følge den aftalte linjeføring, eller når "
           "montøren og rådgiveren ikke er enige, hjælper det ikke at sende endnu en mail. Som "
           "**elautoriseret maskinmester (LV/MV/HV)** kan jeg gå ind i det eltekniske selv: fordelinger, "
           "styringer, fejlfinding og **DS/HD 60364**. Montørerne mærker forskellen på en chef, der har "
           "prøvet det, og en der har fået det refereret.", after=80)

    m.para("**Teamet — retning, ikke kontrol.** Projektledere skal ikke styres; de skal vide, hvor deres "
           "mandat går, hvornår de skal eskalere, og hvad der bliver målt på dem. Jeg har ledet "
           "**25 specialister** og teams på **5, 12, 14 og 25 mand** med **MUS** og 1:1-samtaler, "
           "**kompetencematrix** og faglig sparring — og den sværeste samtale, den om en projektleder uden "
           "styr på sit tal, tages tidligt.", after=80)

    m.para("**Kulturen — enkelhed er et ledelsesværktøj.** Bravida skriver **engagement, ansvarlighed og "
           "enkelhed** som en naturlig del af kulturen. For en projektchef betyder "
           "enkelhed, at den samme beslutning ikke skal tages to gange, at rapporteringen ikke skal opfindes "
           "for hver kunde, og at sikkerheden — **APV**, **LOTO**, risikovurdering før opstart — er samme "
           "procedure på alle Bravidas pladser. Trivsel og sikkerhed hører sammen i den ligning: mine "
           "serviceaftaler er afleveret med **nul kritiske afvigelser** — ikke af mere kontrol, men af færre "
           "regler, som til gengæld blev fulgt.", after=80)

    m.para("**Bravida og Brøndby — hvorfor her.** En koncern med **13.000 medarbejdere**, heraf **3.000 i "
           "Danmark**, i **180+ byer**, noteret på **Nasdaq Stockholm** og med en målsætning om at være "
           "**klimaneutral** i værdikæden i 2045 har noget, en mindre virksomhed ikke har: fagene og "
           "regionerne at trække på, når opgaven kræver mere end ét fag, og et netværk med sparring. Jeg bor "
           "i **Måløv** med 20 minutter til Brøndby og kørekort. Jeg vil gerne høre entreprisens størrelse, "
           "antallet af projektledere og hvordan I måler dækningsgrad undervejs — så de første 90 dage "
           "starter med jeres tal, ikke mine.", after=26)
    m.meta("Med venlig hilsen", after=0)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Projekt- og forretningsansvarlig leder med 20+ års erfaring i el-entreprise og teknisk drift. "
           "Fuldt P&L siden 2023. **Elautoriseret maskinmester (LV/MV/HV)**. Har styret **37 samtidige "
           "CAPEX-projekter** og **25 specialister**, 11 samtidige entrepriser med 14 mand og leveret med "
           "**nul kritiske afvigelser**. Kalkulation, AB 18, totalentreprise og dækningsgrad pr. fase. "
           "SAP ERP, Power BI og månedshjul. Bosat i Måløv — 20 minutter fra Brøndby.", after=80)

    m.section("PROJEKTØKONOMI OG STYRING")
    for label, body in [
        ("Økonomi og dækningsgrad",
         "Kalkulation, efterkalkulation og dækningsgrad pr. opgave og fase; månedlig opgørelse af timer "
         "mod kalkule, udestående og ikke-faktureret arbejde."),
        ("Fremdrift og beslutninger",
         "Økonomi og fremdrift i samme møde og på samme tavle; næste milepæl og den ventende beslutning "
         "med navn og dato."),
        ("Tillæg og ændringer",
         "Ændringer dokumenteret samme uge, de opdages, med begrundelse og konsekvens for tid og penge — "
         "varslet før arbejdet udføres."),
        ("Kontraktgrundlag",
         "AB 18 og ABT 18, totalentreprise og underentreprenører; krav, grænseflader og ansvar læst "
         "igennem, før kalkulationen lægges."),
        ("Elteknisk tyngde",
         "LV/MV/HV, fordelinger, styringer og fejlfinding til DS/HD 60364; elteknisk sparring på pladsen, "
         "når beslutningen ikke kan vente på et møde."),
        ("Kunde og interessenter",
         "Forventningsafstemning med kunden på skrift, status uden overraskelser, og koordinering med "
         "rådgivere, bygherre og egne fag."),
    ]:
        m.bullet(label, body, after=25)

    m.section("ERHVERVSERFARING")
    jobs = [
        ("Ejer / teknisk direktør",
         "ELOHVAC ApS · København · maj 2023–nu",
         "5 elektrikere + 3 lærlinge · fuldt P&L · kalkulation og aflevering",
         [("Forretning og økonomi",
           "Egne tilbud og kalkulationer, løbende efterkalkulation og dækningsgrad; alt salg og alle kunder "
           "selv. Nul kritiske afvigelser i serviceaftalerne."),
          ("Ledelse og sikkerhed",
           "Daglig ledelse af fem elektrikere og tre lærlinge; kompetencematrix, MUS, APV og LOTO ved "
           "opstart på nye pladser.")]),
        ("Senior idriftsættelsesingeniør / projektleder, elsystem",
         "Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024",
         "37 kapitalprojekter · 25 specialister · GMP/FDA/EMA",
         [("Projekt- og økonomistyring",
           "37 samtidige projekter på 2–10 mio. kr. med kravspecifikation, kontrakt, fremdrift og "
           "økonomi; månedlig rapportering til ledelse og bygherre i SAP ERP."),
          ("Aflevering og kvalitetssikring",
           "FAT/SAT og IQ/OQ/PQ med nul kritiske fund; arbejde på anlæg i drift med adgangs- og "
           "tilladelsesprocedurer.")]),
        ("Projekt- og værkstedsleder",
         "Ventek-Air · København · jan. 2022–nov. 2022",
         "14 medarbejdere · 11 entrepriser · DKK 2–10 mio.",
         [("Entrepriser og kapacitet",
           "11 samtidige entrepriser fra specifikation til aflevering; underentreprenører, materialer og "
           "fremdrift styret på daglige tavlemøder.")]),
        ("Vedligeholdelses- og driftsleder",
         "Lynetten under Biofos · København · aug. 2017–jan. 2022",
         "24/7-anlæg · HVAC, pumper, højspændingstavler, SRO/SCADA",
         [("Anlæg, fejlfinding og oppetid",
           "Forebyggende vedligehold og akut fejlfinding på tavler, pumper og HVAC; reservedelsflow og "
           "lagerstyring med 5S og standard work."),
          ("Sikkerhed og arbejdsmiljø",
           "LOTO, APV, sikkerhedsrunderinger og nærved-hændelser i et anlæg, der ikke kunne stoppes.")]),
        ("Elektromekaniker / produktionsteamleder",
         "ARJ Engineering · Teheran · dec. 2003–mar. 2010",
         "12 teknikere · maskinværksted · industrianlæg",
         [("Team og målopfyldelse",
           "Daglig fordeling til 12 teknikere; materialer og værktøj styret mod ugens plan, output målt "
           "pr. medarbejder og pr. maskine.")]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.page_break()
    m.section("UDDANNELSE OG AUTORISATION")
    m.edu("B.Tech, teknologiledelse og maskinteknik",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12")
    m.edu("El- og maskinteknisk design, elteknik (EQF6)", "Tehran Technical University · 2000–2003")
    m.edu("Dansk elautorisation LV/MV/HV — elautoriseret maskinmester", "Sikkerhedsstyrelsen · maj 2023")
    m.edu("Køleteknik og klimaanlæg (AMU) · Lean: 5S, PDCA, A3, standard work",
          "Mercantec · 2021 · anvendt i drift og projektstyring")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("Dansk: modersmål, flydende i skrift og tale · Engelsk: professionelt · Persisk: modersmål · "
           "**Bosat i Måløv**, 20 minutter fra Brøndby · Kørekort B og egen bil · Kan tiltræde hurtigt · "
           "Referencer efter aftale.", after=70)

    m.models_table("DE FØRSTE 90 DAGE — TALLENE, TEAMET OG KUNDEN",
                   ("Periode", "Hvad der sker, og hvordan det måles"), [
        ("Uge 1–2",
         "Læs kalkulation og kontrakt på entreprisen; gå pladsen igennem med projektlederne og "
         "formanden; mød kunden med den nuværende status — ikke med et løfte. Kortlæg de fem største "
         "økonomiske og tidsmæssige risici med navn og dato."),
        ("Dag 30",
         "Hvert projekt præsenteret på én side: dækningsgrad, timer mod kalkule, udestående, tillæg og "
         "næste milepæl. Månedshjulet fastlagt, og eskaleringstrappen for projektlederne skrevet ned og "
         "aftalt med dem."),
        ("Dag 60",
         "Ændringer og tillæg varslet og dokumenteret samme uge, de opstår; kundemøderne ændret fra status "
         "til forventningsafstemning; sikkerhedsprocedure og APV ens på alle pladser i entreprisen."),
        ("Dag 90",
         "Dækningsgrad og fremdrift rapporteret på ét ark til regionen; projektlederne vurderet med "
         "kompetencematrix og udviklingspunkter; entreprisen har en opdateret prognose for både tid og "
         "penge, som kunden har set.")])

    m.section("EN STOR ENTREPRISE TABES I DETALJERNE, IKKE I STRATEGIEN")
    m.para("Der findes ikke en el-entreprise, der er gået ned på en forkert strategi alene. Den er gået ned "
           "på to hundrede små beslutninger, som hver især virkede rimelige: en ekstra mand på pladsen for "
           "at hente en uge, et tillæg der blev sparret til senere, en mangel der blev udbedret uden at "
           "blive registreret, et materialekøb der blev hastet igennem for at holde en dato. Projektchefens "
           "værdi ligger i at gøre de beslutninger synlige, mens de stadig er små — og i at have et system, "
           "hvor de bliver registreret, uden at nogen føler sig kontrolleret.", after=80)

    m.section("KUNDEN KØBER IKKE EN PLAN — KUNDEN KØBER EN, DER HOLDER DEN")
    m.para("En bygherre med en stor el-entreprise på sit anlæg har typisk prøvet at få en plan, der blev "
           "flot præsenteret og stille ændret. Det, der giver genkøb, er noget andet: at datoen holder, "
           "at ændringen bliver varslet, før den bliver dyr, at dokumentationen er i hus ved aflevering, og "
           "at den, der ringer, ved hvad han taler om. Min erfaring med at sidde på bygherrens side i et "
           "GMP-miljø har lært mig, hvor lidt der skal til, før tilliden forsvinder — og hvor stor en "
           "entreprise der kan vindes tilbage ved at holde det, man har sagt.", after=80)

    m.section("SIKKERHED ER IKKE EN KAMPAGNE, DET ER EN PROCEDURE")
    m.para("På en stor el-entreprise kommer sikkerheden ikke fra et opråb i januar, men fra den samme "
           "procedure på hver plads: risikovurdering før opstart, LOTO, APV, arbejdstilladelser og en "
           "formand, der kan stoppe arbejdet uden at blive spurgt om lov. Jeg har stået med ansvaret på et "
           "24/7-anlæg og i pharma-projekter, hvor nærved-hændelser blev meldt, fordi melderen blev hørt — "
           "og det er den slags, der gør forskellen mellem en afvigelse og en ulykke.", after=80)

    m.section("PROJEKTLEDERE BLIVER IKKE GOD AF AT BLIVE HOLDT ØJE MED")
    m.para("En projektleder, der ved, hvad der bliver målt på ham, hvornår han skal eskalere, og hvem han "
           "kan få sparring af, når tallet ikke stemmer, tager bedre beslutninger end en, der skal spørge om "
           "lov til alt. Jeg har drevet team af specialister, teknikere og svende og ved, at den ledelse, "
           "der virker på en byggeplads, også virker på et projektkontor: aftal grænsen, følg op, og tag "
           "den svære samtale tidligt — den bliver hverken lettere eller kortere af at vente.", after=80)

    m.section("MØDET, DER AFGØR UGEN, VARER TYVE MINUTTER")
    m.para("Et ugentligt projektmøde skal ikke være et statusmøde, hvor hver projektleder læser sin rapport "
           "op. Det skal være tyve minutter, hvor tre spørgsmål besvares: hvad er den næste beslutning, hvem "
           "tager den, og hvad koster det at vente. Resten kan stå på papir. Jeg har kørt tavlemøder på den "
           "måde i drift og i projekt, og gevinsten er ikke mødet — den er, at problemet kommer op, mens det "
           "stadig er en beslutning og ikke en efterregning.", after=80)

    m.page_break()

    m.models_table("HVAD STILLINGEN KRÆVER — HVAD JEG HAR LEVERET", ("Krav i opslaget", "Bevis"), [
        ('Overordnet ansvar for økonomi, fremdrift og styring af el-entreprisen',
         'Fuldt P&L siden 2023 med egne kalkulationer; 37 kapitalprojekter på 2–10 mio. kr. med fremdrift, økonomi og rapportering.'),
        ('Ledelse og koordinering af teamet af projektledere',
         'Ledet 25 specialister på 37 projekter og teams på 5, 12, 14 og 25; mandat, eskaleringstrappe og kompetencematrix.'),
        ('Opbygning og vedligeholdelse af stærke og professionelle kunderelationer',
         'Kunderelationer bygget fra nul i egen virksomhed: aftaler indgået, status på skrift og genkøb som salgsmotor.'),
        ('Løbende dialog og forventningsafstemning med kunden',
         'Kundemøder som afstemning af, hvad der er købt og ændret — ikke som referat; bygherresiden kendt fra Novo Nordisk.'),
        ('Tæt samarbejde med montører og teknikere omkring udførelsen',
         'Daglig ledelse af svende, lærlinge og teknikere; tavlemøder på pladsen og beslutninger taget, hvor arbejdet sker.'),
        ('Sikring af god kommunikation og koordinering på tværs af projektets interessenter',
         '37 projekter koordineret med engineering, indkøb, kvalitet, rådgivere og bygherre; interfacesaftaler med navn og dato.'),
        ('Elteknisk sparring og håndtering af problemstillinger undervejs i projektet',
         'Elautoriseret maskinmester (LV/MV/HV): fordelinger, styringer og fejlfinding til DS/HD 60364 — sparring direkte på pladsen.'),
        ('7+ års erfaring med større entrepriser, gerne inden for el',
         '20+ år i el-entreprise og teknisk drift: 11 samtidige entrepriser, 37 CAPEX-projekter og egen virksomhed med fuldt P&L.'),
        ('En elteknisk baggrund og solid forståelse for faget',
         'Elautoriseret maskinmester (LV/MV/HV), B.Tech maskinteknik; fem år med tavler, pumper og HVAC i 24/7-drift.'),
        ('Dokumenteret erfaring med økonomisk ansvar på større projekter',
         'P&L, dækningsgrad, budgetter og udestående i egen virksomhed; projektøkonomi og månedlig rapportering på 37 CAPEX-projekter.'),
        ('Erfaring med at lede og sætte retning for projektledere',
         'Ledelse af 25 specialister og faglige nøglepersoner: mandat, prioritering mellem projekter, MUS og 1:1 med udviklingspunkter.'),
        ('Stærke kommunikative kompetencer og en naturlig evne til at skabe relationer',
         'Forhandling og dialog på dansk og engelsk med bygherre, rådgivere, underentreprenører og egne folk — på skrift og på pladsen.'),
        ('En kommerciel forståelse og blik for både kunden og den gode projektøkonomi',
         'Priser sat, tillæg varslet og margin fulgt pr. kunde og opgavetype; kunder fastholdt ved at levere det, der stod i aftalen.'),
        ('Tager naturligt ansvar og formår at skabe tillid omkring dig',
         'Ansvaret for egen virksomheds økonomi og mennesker siden 2023; nul kritiske afvigelser og nul overraskelser i serviceaftalerne.'),
        ('Kan tilpasse dialogen — med kunden, om projektøkonomi med en projektleder og på pladsen med montører',
         'Samme sag talt tre steder: bygherremøde i GMP-miljø, økonomiopfølgning med projektledere og fejlfinding på tavlen med montøren.'),
    ], widths=(3600, 7046))

    m.section("EN PROGNOSE ER EN MENING, INDTIL DEN ER SKREVET NED")
    m.para("Alle store entrepriser har en prognose. Forskellen er, om den er et regneark, som nogen opdaterer "
           "op til mødet, eller en aftale om, hvad der er sandsynligt, som projektlederen har skrevet under på. "
           "Jeg vil have den skrevet ned, dateret og med de forudsætninger, der gør den rigtig eller forkert — "
           "så en ændring i fremdriften kan slås op i stedet for at blive diskuteret, og så kunden hører om "
           "den, mens den stadig kan planlægges ind i hans egen byggesag.", after=80)

    m.section("DET STØRSTE PROJEKT ER ALTID DET NÆSTE")
    m.para("En projektchef bliver målt på den entreprise, han afleverer — og ansat på den næste. Derfor "
           "slutter et projekt ikke ved afleveringsforretningen: manglerne skal lukkes, dokumentationen skal "
           "være i hus, 1- og 5-års gennemgangen skal kunne gennemføres uden at lede efter filer, og kunden "
           "skal kunne sige, at det gik som aftalt. Det er den opsparing, der gør, at den næste store "
           "entreprise kommer i udbud med en reference og ikke med en forklaring.", after=80)

    m.section("BRØNDBY LIGGER TYVE MINUTTER FRA MIN DØR")
    m.para("På en el-entreprise af den størrelse bliver projektchefen ikke sjældent den, der sidder i møder og "
           "får pladsen refereret. Jeg bor i Måløv, har tyve minutter til Brøndby, og kan være på pladsen, når "
           "der er noget, der ikke kan vente til næste møde — det være sig en tavle, der ikke kan "
           "ibrugtages, eller en kunde, der har brug for at se, at nogen kommer. Det er en praktisk detalje "
           "for nogen. For en projektchef er det arbejdsformen.", after=80)

    return m.save(path, title="Projektchef el-entreprise — Bravida Brøndby",
                  subject="Projektøkonomi, projektledelse og elteknisk sparring",
                  keywords="projektchef, el-entreprise, projektledelse, daekningsgrad, kalkulation, ab 18, "
                           "projektokonomi, sap erp, bravida, broendby")


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Bravida_ProjektchefElEntreprise.docx')))
