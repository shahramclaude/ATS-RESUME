# -*- coding: utf-8 -*-
"""Novonesis — Maskinmester til tekniske projekter og support af produktionsudstyr.

Bagsværd og Nørrebro · Technical Support · JR113900. Dansk opslag -> dansk dokument, 4 sider.

SÆRLIGT FOR DETTE OPSLAG: Novonesis beder eksplicit om, at man søger UDEN ansøgning og i
stedet skriver et par sætninger i CV'et om, hvorfor man søger. Dokumentet er derfor bygget som
en motiveret CV: side 1 er CV'ets forside med "Motivation for at søge" og en dag på gulvet —
ikke et brev med "Kære ...". Kravet om ét samlet dokument (brugerens faste regel) er holdt:
brev, CV, 90-dages-plan og fuld kravmatrix er stadig med.

STILVALG (master/STILREGISTER.md; godkendt af scripts/style_guard.py, 3/3 skift mod #206):
  register      = TEKNISK-DRIFTSNÆR (klokken-til-nærhed, drift, service, vedligehold). Sidst
                  #199. Rollen er vedligeholdelsesforberedelse og support på gulvet.
  åbningsgreb   = H (DAGSFORLØBET) — 06.50 til 15.10 på fabrikken, minut for minut. Sidst #194.
  struktur      = ORDLISTEN — Novonesis' egne begreber oversat til praksis: Day One Readiness ·
                  masterdata · KLS og eltekniske standarder · reservedelslister · Maskindirektivet
                  · overlevering. Hvert begreb er et tidsstempel i dagen. Sidst #200.
  kadence       = korte, konstaterende sætninger, klokkeslæt som bærende virkemiddel, intet
                  tillægsord om personen; hvert afsnit slutter i et bevis.

KULTURSYNKRONISERING (policy 04.11.2026): Novonesis' egne ord bærer teksten — *Day One
Readiness*, *masterdata*, *KLS*, *eltekniske standarder*, *Maskindirektivet*, *reservedelslister*,
*robuste produktionsløsninger*, *oppetid*, *reparatører, elektrikere og automatikteknikere*,
*bæredygtige løsninger*, *kontinuerlige forbedringer*, *"better our world with biology"*.
Research: Novonesis = Novozymes + Chr. Hansen (januar 2024), 10.000 kolleger i 45+ lande,
Bagsværd (Krogshøjvej 36), procesudstyr til spraytørring, granulering, formulering, tapning og
pakning; vedligeholdelsesorganisation ca. 75 medarbejdere.

Brugerens oplysninger (04.11.2026, spurgt før byg): arbejder med Maskindirektivet (CE,
risikovurdering, teknisk dokumentation) og kender EU 1935/2004 om fødevarekontaktmaterialer.
Ingen opdigtede fakta.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Maskinmester · teknisk support, masterdata og vedligeholdelsesforberedelse'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4. november 2026")
    m.meta("Novonesis · Technical Support, Bagsværd og Nørrebro · JR113900")

    # ---------------------------------------------------------------- side 1
    m.section("MOTIVATION FOR AT SØGE")
    m.para("I beder om en motiveret CV i stedet for en ansøgning, og det følger jeg. Grunden til, "
           "at jeg søger, er enkel: jeg har brugt tyve år på at få produktionsudstyr til at holde — "
           "som elektriker, som maskinmester, som driftsansvarlig og som den, der afleverede det. "
           "Halvdelen af jeres stilling er at gøre nyt udstyr klar til dag ét, og den anden halvdel "
           "er at holde det kørende bagefter. Og det er en produktion, hvor udstyret betyder noget uden "
           "for fabrikken: **biosolutions** og **bæredygtige løsninger** kræver maskiner, der kører, "
           "og dokumentation, der holder — ellers bliver det en god hensigt. Det er netop det arbejde, "
           "hvor de fleste fejl bliver bestemt, længe før nogen reparerer noget.", after=70)

    m.section("EN DAG PÅ GULVET — 06.50 TIL 15.10")
    m.para("**06.50 · Day One Readiness.** Linjen skal køre mandag. Jeg står ved den med "
           "projektintegratoren og den tekniker, der skal overtage den, og går listen igennem: "
           "vedligeholdelsesplan pr. komponent, **servicekontrakter** der dækker det, de skal, "
           "**reservedelslister** der findes i virkeligheden, masterdata der er tastet ind — og den "
           "dokumentation, der gør maskinen til et aktiv frem for et spørgsmålstegn. Day One "
           "Readiness er ikke en tjekliste, der udfyldes fredag; det er en aftale med produktionen om, "
           "hvad der er klar mandag. Jeg har stået på den anden side af den aftale i 37 "
           "CAPEX-projekter med FAT/SAT og IQ/OQ/PQ og **nul kritiske fund** ved aflevering.", after=70)

    m.para("**09.10 · Masterdata.** Ved maskinen med en tekniker, der skal finde delen om to år. Hvad "
           "hedder komponenten, hvilken position sidder den på, hvilket interval gælder, og hvilken "
           "reservedel hører til. Hvis det ikke står rigtigt, koster det hver gang, nogen skal lede "
           "efter det — og det bliver dyrere, hver gang nogen gætter i stedet. Jeg har ført "
           "projektgrundlag, milepæle og økonomi i **SAP** dagligt, og jeg ved, hvor lidt der skal til, "
           "før et masterdatafelt bliver en fejl, der gentager sig.", after=70)

    m.para("**11.00 · KLS og de eltekniske standarder.** Meget af det, der går galt mellem anlæg og "
           "vedligehold, er, at to dokumenter ikke er enige. Derfor er standarderne ikke et "
           "dokumentationskrav for mig, men et arbejdsredskab: samme tavleopbygning, samme mærkning, "
           "samme logik i styringen, så en tekniker kan arbejde i det uden at læse en ny manual hver "
           "gang. Jeg er **elautoriseret maskinmester** på LV/MV/HV og har bygget installationer op "
           "efter standarder, der skulle kunne inspiceres bagefter.", after=70)

    m.para("**13.20 · Reservedelslisterne.** En reservedel er en beslutning om nedetid, ikke en "
           "indkøbslinje. Så listen bygges efter kritikalitet og leveringstid: hvad der stopper "
           "produktionen inden for en time, hvad der kan vente til næste dag, og hvad der aldrig skal "
           "ligge på lager. Jeg har drevet egen virksomhed siden 2023 og ved, hvad en hyldeplads "
           "koster — og hvad den koster at mangle klokken 03.", after=70)

    m.para("**14.40 · Maskindirektivet.** Risikovurdering, CE-dokumentation og tekniske filer er "
           "krav, men det praktiske spørgsmål er det samme: kan en reparatør komme til, og kan han "
           "gøre det sikkert? Afskærmning, sikkerhedsafstande og ergonomi er ikke bløde krav, når en "
           "motor skal skiftes om natten — de er forskellen på en planlagt reparation og en "
           "arbejdsulykke. Jeg har arbejdet med både CE-dokumentation og med den praktiske side på "
           "anlæg, der var i drift, mens de blev ændret.", after=70)

    m.para("**15.10 · Overlevering.** Det, der blev aftalt i dag, står i morgen — hos **reparatører**, "
           "**elektrikere** og **automatikteknikere**, der skal bruge det. Ikke i mit hoved, "
           "ikke i en mail fra i fredags, men i systemet og i den plan, **oppetid** og **driftsikkerhed** "
           "hviler på. Det er også derfor, jeg vil være synlig på fabrikken: den viden, man "
           "bruger i en vedligeholdelsesplan, får man ved at stå ved maskinen, ikke ved at læse om "
           "den.", after=70)

    m.para("**Hvad jeg har prøvet det på.** Fire år som driftsansvarlig på et anlæg i 24/7-drift med "
           "pumper, HVAC, højspændingstavler og **SRO**/**SCADA**; 37 samtidige CAPEX-projekter i "
           "reguleret miljø med 25 specialister, **SAP** og kvalificering; og siden 2023 egen "
           "virksomhed med fem elektrikere, tre lærlinge og fuldt resultatansvar. Uddannet "
           "**maskinmester** med elautorisation LV/MV/HV og el- og maskinteknisk design (EQF 6).",
           after=70)

    m.para("**Praktisk:** bosat i Måløv, ca. 10 minutter fra Bagsværd og ca. 25 minutter fra Nørrebro "
           "· **kørekort B** · dansk modersmål, **engelsk** på samtaleniveau og derover · "
           "**kan tiltræde snarest** · ansøgning sendt via jeres system inden fristen **15. november "
           "2026**.", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Maskinmester med tyve års erfaring fra **produktionsudstyr** og tekniske anlæg: "
           "elautoriseret på LV/MV/HV, el- og maskinteknisk design (EQF 6) og B.Tech i "
           "teknologiledelse. Fire år i 24/7-drift, 37 CAPEX-projekter med **SAP**, FAT/SAT og "
           "IQ/OQ/PQ, og siden 2023 eget ansvar for drift, service og aflevering i egen virksomhed.",
           after=80)

    m.section("TEKNISK SUPPORT OG VEDLIGEHOLD")
    for label, body in [
        ("Fejlfinding på udstyr",
         "Support på eksisterende produktionsudstyr: fejlfinding på el, mekanik og styring, "
         "forbedringer og **ombygninger** — arbejdet gjort færdigt, ikke udskudt til næste hold."),
        ("Forebyggende vedligehold",
         "Vedligeholdelsesplaner pr. komponent med interval, ansvarlig og historik; planlagt arbejde "
         "flyttet fra akut til forudsigeligt."),
        ("Reservedele og kritikalitet",
         "**Reservedelslister** bygget efter kritikalitet og leveringstid; kendskab til hvad der "
         "stopper produktionen, og hvad der kan vente."),
    ]:
        m.bullet(label, body)

    m.section("DOKUMENTATION OG MASTERDATA")
    for label, body in [
        ("Masterdata i SAP",
         "**Masterdata** og **teknisk dokumentation** opdateret i **SAP** sammen med produktion, "
         "integratorer og elsupport; data der kan findes igen af den næste."),
        ("Maskindirektivet",
         "**CE**-dokumentation, risikovurdering og tekniske filer; sikkerhedsafstande, afskærmning og "
         "ergonomi vurderet, før udstyret blev taget i brug."),
        ("Eltekniske standarder",
         "**Eltekniske produktionsanlæg** opbygget og mærket efter standarder, der kan inspiceres; "
         "**KLS**-arbejdsgang understøttet med de data, systemet skal bruge."),
    ]:
        m.bullet(label, body)

    m.section("PROJEKTER OG IDRIFTSÆTTELSE")
    for label, body in [
        ("Day One Readiness",
         "Nyt udstyr klar ved **idriftsættelse**: vedligeholdelsesplan, servicekontrakt og "
         "reservedelsliste på plads, før produktionen får nøglen."),
        ("Integratorer og leverandører",
         "**Projektintegratorer** og leverandører fulgt på dokumentation, test og accept; krav "
         "afklaret, mens løsningen stadig kunne ændres."),
        ("Robuste løsninger",
         "**Robuste produktionsløsninger** valgt på drift, adgang og vedligehold — ikke kun på pris; "
         "fremtidige vedligeholdelsesudgifter synliggjort i beslutningen."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Indehaver / Teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · fuldt resultatansvar · drift, service og aflevering")
    m.bullet("Support, service og ombygninger",
              "Opgaver løst ude hos kunderne med eget budget og egen risiko; **40 % mindre "
              "administration** og **over 40 % produktivitetsløft** via egne værktøjer.")

    m.job("Senior Commissioning Engineer / Project Manager, elsystemer",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024",
          scope="37 samtidige CAPEX-projekter · 25 specialister · GMP/FDA/EMA")
    m.bullet("Idriftsættelse og dokumentation",
              "Projektgrundlag og milepæle i **SAP**; FAT/SAT og IQ/OQ/PQ med protokoller skrevet før "
              "testen — **nul kritiske fund** ved aflevering.")

    m.job("Projekt- og værkstedschef", "Ventek-Air · København · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · 2–10 mio. kr. pr. sag")
    m.bullet("Maskiner og komponenter",
              "Ventilations- og komponentleverancer med luftmængde, tryk og balance som "
              "acceptkriterier; dokumentation afleveret sammen med udstyret.")

    m.job("Drifts- og vedligeholdelseschef", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="Anlæg i 24/7-drift · pumper, VVS, HVAC, højspændingstavler, SCADA")
    m.bullet("Drift, der ikke må stoppe",
              "Forebyggende og tilstandsbaseret **vedligehold** og fejlfinding døgnet rundt; indgreb "
              "planlagt i snævre vinduer med midlertidig løsning klar. LOTO og APV.")

    m.job("Elektromekanisk tekniker / produktionsleder",
          "ARJ Engineering · Teheran · dec. 2003–mar. 2010 · 12 mekanikere og teknikere")

    # ---------------------------------------------------------------- side 3
    m.page_break()
    m.section("UDDANNELSE OG AUTORISATION")
    m.edu("Elautoriseret maskinmester — dansk elautorisation LV/MV/HV",
          "Sikkerhedsstyrelsen · maj 2023")
    m.edu("B.Tech, teknologiledelse og maskinteknik (EQF 6)",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · karakter 7,6/12")
    m.edu("El- og maskinteknisk design, elektroteknik (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("Køle- og VVS-teknik (AMU) · Lean: 5S, PDCA, VSM, A3",
          "Mercantec · 2021 · STCW-sikkerhedskurser (2021–2023)")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("**Dansk:** modersmål · **Engelsk:** samtaleniveau og derover, skriftligt og mundtligt · "
           "**Persisk:** modersmål · **Bosat i Måløv**, ca. 10 min. fra Bagsværd og 25 min. fra "
           "Nørrebro · **Kørekort B** · **Kan tiltræde snarest** · Referencer efter aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA OVERBLIK TIL FØRSTE UDSTYR KLAR TIL DAG ÉT",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–3",
             "Gå runder på begge sites med teknikerne: hvilket udstyr der stopper produktionen, "
             "hvilke **masterdata** der er forkerte, og hvilke reservedele der mangler på hylden."),
            ("Dag 30",
             "Overblik over de kommende projekter og deres **Day One Readiness**-status: hvad der "
             "mangler i vedligeholdelsesplan, **servicekontrakter** og reservedelslister, og hvem der "
             "ejer det."),
            ("Dag 60",
             "Første udstyr taget igennem fra dokumentation til reservedelsliste, med produktionen og "
             "elsupport; **KLS** og de eltekniske standarder gennemgået med dem, der arbejder i dem."),
            ("Dag 90",
             "En fast arbejdsgang for nyt udstyr — hvad der skal være på plads før idriftsættelse — "
             "godkendt af vedligehold og produktion, og brugt på det første projekt."),
        ],
        widths=(1500, 8830))

    m.section("DOKUMENTATION ER DET, DER GØR EN REPARATION TIL EN VEDLIGEHOLDELSESPLAN")
    m.para("En reparation, der ikke er dokumenteret, er en udgift, der kommer igen. Derfor skrives "
           "den færdig, mens hænderne stadig er snavsede: hvad der var i stykker, hvad der blev gjort, "
           "hvilken del der blev brugt, og hvad der stadig mangler. Det tager fem minutter og sparer "
           "den næste tekniker en time — og det er den eneste måde, en vedligeholdelsesplan bliver "
           "bedre år for år i stedet for at blive skrevet om.", after=70)

    m.section("MASKINDIREKTIVET RAMMER DEM, DER SKAL HOLDE MASKINEN")
    m.para("CE-mærkning og teknisk dokumentation bliver ofte behandlet som noget, leverandøren "
           "afleverer, og som ingen læser igen. Men kravene rammer dem, der skal vedligeholde: kan "
           "man komme til at smøre lejet, kan afskærmningen tages af uden at fjerne en sikring, og står "
           "der en advarsel det rigtige sted? Jeg læser dokumentationen med de spørgsmål, fordi det er "
           "der, en dårlig løsning bliver dyr.", after=70)

    m.section("SAP ER IKKE ET SYSTEM, DET ER EN VANE")
    m.para("Det er ikke systemet, der fejler, når masterdata bliver forkerte — det er vanen. Så min "
           "tilgang er kedelig og effektiv: arbejdet registreres, når det gøres, af den, der gør det, "
           "og der er en fast dag, hvor data bliver gennemgået med produktionen. Jeg har brugt **SAP** "
           "dagligt i to år på 37 projekter, og jeg har set, hvad der sker, når opdateringen bliver "
           "noget, man gør fredag eftermiddag.", after=70)

    m.section("DET NYE UDSTYR BLIVER GAMMELT PÅ DAG ÉT")
    m.para("Den dag udstyret kører første gang, er det eneste tidspunkt, hvor alle, der ved noget om "
           "det, stadig er i rummet — leverandøren, integratoren, teknikeren og dem, der har bygget "
           "det. Efter den dag skal viden findes i dokumentationen. Derfor er min prioritet i nye "
           "projekter ikke at komme tidligt i mål, men at der ikke er noget, nogen skal huske om to "
           "år, som de ikke kan slå op.", after=0)

    m.section("HVOR JEG VILLE STARTE")
    m.para("Med de kommende projekter og de maskiner, der stopper produktionen i dag. Første uge: gå "
           "runder på Bagsværd og Nørrebro med de teknikere, der har udstyret i hænderne, og noter "
           "hvor dokumentation, masterdata og virkelighed ikke stemmer. Det er der, den halve stilling "
           "som vedligeholdelsesforberedelse faktisk bliver bestemt — resten er opfølgning.", after=0)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "DET ROLLEN KRÆVER — DET HAR JEG LØST",
        ["Krav i opslaget", "Bevis"],
        [
            ("Sikre dokumentation og opdatering af masterdata med produktionen, projektintegratorer og elsupport-teamet",
             "**Masterdata** og dokumentation opdateret i **SAP** med produktion og leverandører, mens "
             "opgaven blev løst."),
            ("Bidrage til robuste produktionsløsninger og synliggøre fremtidige vedligeholdelsesudgifter",
             "Løsninger valgt på drift, adgang og vedligehold; omkostningen over levetiden lagt frem, "
             "før produktionen valgte."),
            ("Sikre at fremtidigt vedligehold kan gennemføres ergonomisk og sikkerhedsmæssigt forsvarligt og efter gældende lovgivning",
             "**Maskindirektivet** og arbejdsmiljø i praksis: adgang og afskærmning vurderet ved opstart; "
             "LOTO og APV som fast arbejdsgang."),
            ("Sikre Day One Readiness: vedligeholdelsesplaner, servicekontrakter og reservedelslister klar ved idriftsættelse",
             "**Day One Readiness** i 37 projekter: FAT/SAT, IQ/OQ/PQ og **nul kritiske fund** ved "
             "aflevering — med plan og reservedele på plads."),
            ("Understøtte KLS-systemet og eltekniske standarder samt indsamle data og produktionskrav til vedligeholdelsesprogrammer og reservedelsstyring",
             "**KLS** og de **eltekniske standarder** understøttet med de data, systemet skal bruge; "
             "krav fra produktionen omsat til **reservedelsstyring**."),
            ("Yde teknisk support på eksisterende produktionsudstyr ved udfordringer, forbedringer og ombygninger",
             "**Teknisk support** og fejlfinding på el, mekanik og styring; **ombygninger** og "
             "forbedringer udført på anlæg, der var i drift."),
            ("Deltage på tværs af projektfaser og finde robuste løsninger i dialog med interne og eksterne samarbejdspartnere",
             "**Projektintegratorer** og leverandører fulgt gennem alle faser; 25 specialister og 11 "
             "entrepriser samtidigt."),
            ("Være synlig på fabrikken med tæt dialog med produktion og vedligehold",
             "På gulvet, ikke i et mødelokale: runder ved udstyret, dialog med teknikere og "
             "produktion, og beslutninger taget tæt på maskinen."),
            ("Relevant teknisk uddannelse som maskiningeniør eller maskinmester, gerne kombineret med el-teknisk baggrund",
             "**Elautoriseret maskinmester** LV/MV/HV, el- og maskinteknisk design (EQF 6) og B.Tech i "
             "teknologiledelse — på elektrikerbaggrund."),
            ("Kan dokumentere eget arbejde og omsætte tekniske informationer til strukturerede vedligeholdelsesdata",
             "Dokumentation skrevet, mens opgaven blev løst; **teknisk dokumentation** omsat til "
             "intervaller, komponenter og **reservedelslister**."),
            ("Kendskab til Maskindirektivet og struktureret arbejde med teknisk dokumentation",
             "**Maskindirektivet** i praksis: risikovurdering, CE-dokumentation og tekniske filer "
             "gennemgået ved opstart og ombygning."),
            ("Stærk maskinteknisk forståelse kombineret med god forståelse for elteknik",
             "Begge sider i samme stilling: mekanik, pumper og HVAC på den ene side, **eltekniske "
             "produktionsanlæg** og styring på den anden."),
            ("Erfaring med eltekniske produktionsanlæg og kendskab til relevante eltekniske designstandarder",
             "**Eltekniske produktionsanlæg** bygget, idriftsat og fejlfundet; mærket efter standarder, der "
             "kan inspiceres."),
            ("Fluent dansk og engelsk på samtaleniveau",
             "Dansk modersmål; **engelsk** på samtaleniveau og derover, skriftligt og mundtligt, brugt "
             "dagligt i internationale projekter."),
            ("Tager ansvar, arbejder struktureret og trives med at finde løsninger sammen med andre",
             "Eget resultatansvar siden 2023; struktur som vane, og løsninger fundet sammen med dem, der "
             "skal leve med dem."),
            ("Fordel: erfaring med dokumentation inden for vedligehold og opdatering af masterdata",
             "**Vedligehold** dokumenteret i **SAP** og i egne systemer; masterdata holdt opdateret "
             "med produktionen som modpart."),
            ("Fordel: erfaring med SAP",
             "**SAP** dagligt i to år: projektgrundlag, milepæle, økonomi og dokumentation på 37 "
             "projekter."),
            ("Fordel: kendskab til EU 1935/2004 om fødevarekontaktmaterialer, nysgerrighed og løbende forbedringer",
             "**EU 1935/2004** og fødevarekontaktmaterialer kendt fra dokumentationsarbejde; "
             "**kontinuerlige forbedringer** som arbejdsform."),
        ],
        widths=(3600, 6746))

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_Novonesis_Maskinmester.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_Novonesis_Maskinmester.docx'))
