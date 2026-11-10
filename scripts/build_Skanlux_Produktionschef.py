# -*- coding: utf-8 -*-
"""Skanlux Byggefirma A/S — produktionschef, Nykøbing Falster (premium ferieboliger).

Dansk opslag → dansk dokument (da-DK): ansøgning side 1, CV side 2, uddannelse + 90 dage +
tre afsnit side 3, kravmatrix side 4.

STILVALG (master/STILREGISTER.md; godkendt af scripts/style_guard.py, 3/3 skift mod #200):
  register      = PRODUKTIONSLINJE (TAKT OG KAPACITET) — nyt register i menuen. Ordforråd fra
                  fabrikken overført på byggeplads: takt, stationer, bemanding, udsyn, gennemløb,
                  spild, svind, efterkalkulation. Rollen er produktion af 125–150 skræddersyede
                  ferieboliger om året, og opslagets egne ord er kapacitetsudnyttelse,
                  produktionsomkostninger og standardisering.
  åbningsgreb   = F (KONSEKVENSEN) — hvad det koster, når det svigter, konkret: en håndværker, der
                  står stille, koster ikke en uge, men den families sommer.
  struktur      = PROBLEMKATALOG — fire ting, der går galt i netop denne produktion (kapacitet
                  mellem grunde · fem byggeledere, fem planer · kostpris opdaget for sent ·
                  Arbejdstilsynet og 3F), hver med hvad det koster, hvad jeg gør, og bevis.
  kadence       = korte, verbale sætninger; ét tal pr. afsnit; ingen tillægsord om personen.

KULTURSYNKRONISERING (policy 04.11.2026): virksomhedens egne ord bærer dokumentet —
  *skræddersyede ferieboliger bygget direkte på grunden (ikke præfabrikerede moduler)*,
  *egne håndværkere, egen tegnestue og faste samarbejdspartnere*, *kvalitet*, *FSC-certificeret træ*,
  *korte beslutningsveje*, *ejerledet*, *vækst*, *professionelisering af byggeorganisationen*.
  Konkret greb: modsætningen mellem det unikke hus og den gentagelige produktion — *"det, der skal
  standardiseres, er ikke huset, men beslutningerne omkring det."*

Ingen opdigtede fakta. Dokumenteret grundlag: fuldt P&L i egen virksomhed siden 2023 (5 elektrikere
+ 3 lærlinge), 11 samtidige entrepriser med 14 mand, 37 CAPEX-projekter med budget/prognose i SAP
ERP, KS og nul kritiske fund ved aflevering, arbejdsmiljø (APV, LOTO, sikkerhedsrunderinger),
kompetencematrix og oplæring af lærlinge.

Kravhuller: opslaget gør byggefaglig baggrund til et "eventuelt" og skriver udtrykkeligt, at
erfaring vægter højere end uddannelse. Derfor intet forbeholdsafsnit (policy 04.11.2026: som
udgangspunkt ingen forbehold; spørg kun ved formelle, hårde krav).

Policy: master/README.md — jobbet først, kandidaten kun som bevis.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Produktionschef · Byggeri, kapacitet og fremdrift'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4. november 2026")
    m.meta("Skanlux Byggefirma A/S · Produktionschef · Englandsvej 7, 4800 Nykøbing Falster")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: produktionschef", bold=True, color='1A1A1A')
    m.para("Til Michael Kjærgaard, UnikRecruitment — videre til Skanlux Byggefirma A/S", after=70)

    # ---------------------------------------------------------------- side 1
    m.para("**Når en håndværker står stille i en uge, koster det ikke en uge.** Det koster den "
           "familie, hvis hus ikke er klar til sommer, og den næste grund sin start. Skanlux bygger "
           "125–150 **poolhuse** og **ferieboliger** om året, **skræddersyede** og bygget direkte på "
           "grunden med "
           "**egne håndværkere** og faste samarbejdspartnere. Det er den slags **produktion**, hvor "
           "kapaciteten ikke styres af en plan i hovedet, men af et tal, nogen har skrevet ned. Det er "
           "**kapacitetsstyring**, og den fejler stille: den samme uge kan gå tabt på fem "
           "adresser, uden at nogen opdager det før fredag.",
           after=80)

    m.para("Stillingen er ny, og det er ikke en tilfældig detalje: produktionen skal kunne bære "
           "mere, end den gør i dag, uden at kvaliteten bliver det, der bliver slækket på. Det "
           "arbejde begynder med at gøre kapaciteten synlig — hvem er hvor, hvornår, og hvad venter "
           "de på. Nedenfor står de fire steder, hvor jeg først ville kigge, fordi det er der, "
           "**fremdrift**en og **økonomien** forsvinder i den type virksomhed.", after=80)

    m.para("**1 · Kapaciteten står stille mellem to grunde.** En tømrer, der er færdig på en adresse "
           "og ikke kan komme videre, er den dyreste medarbejder i virksomheden. Det sker, når "
           "grunden ikke er klar, når materialet kommer i uge 34 i stedet for 32, eller når de næste "
           "huse ikke er lagt i rækkefølge. Jeg arbejder med **udsyn** på 8–12 uger pr. byggesag: "
           "hvilke fag skal ind, i hvilken rækkefølge, og hvad skal være leveret to uger før. 11 "
           "samtidige entrepriser med 14 mand og daglige tavlemøder lærte mig, at en flaskehals er "
           "billig i uge 30 og dyr i uge 35.", after=80)

    m.para("**2 · Fem byggeledere kører fem planer.** Skanlux har **byggeledere** Øst og Vest. Det er "
           "styrken — nærhed til grundene — men det bliver en svaghed, hvis hver byggesag har sit "
           "eget format for **tidsplaner**, **rekvisitioner** og status. Én fast ramme for det ugentlige "
           "**tidsplansmøde** med fire faste punkter, én rekvisition og én måde at melde "
           "afvigelser på giver dig noget, der kan lægges sammen — og giver dig mulighed for at se, "
           "hvilken byggeleder der mangler mandskab, før han selv opdager det. **Standardisering** "
           "handler ikke om at gøre arbejdet ens; den handler om at gøre rapporteringen "
           "sammenlignelig.", after=80)

    m.para("**3 · Kostprisen bliver opdaget for sent.** Ændringer i **kostpriser** er dyre, når de "
           "først bliver fundet ved **efterkalkulationer**ne. Min regel er enkel: enhver ændring "
           "prissættes i samme uge, den opstår, og skrives i en log med en ejer. Så kan "
           "efterkalkulationen bruges til at prisfastsætte det næste hus i stedet for at forklare "
           "det sidste. Jeg har fulgt budget og prognose månedligt på 37 projekter i SAP ERP og "
           "drevet egen virksomhed med fuldt P&L-ansvar — jeg ved, hvad en uafklaret ændring koster, "
           "når den først ligger i regnskabet.", after=80)

    m.para("**4 · Arbejdstilsynet og 3F er en del af produktionen.** Kommer **Arbejdstilsynet** på "
           "besøg, er svaret ikke en mappe, der blev lavet dagen før. Det er en opdateret APV, "
           "risikovurderinger pr. plads, stillads og lift med **certificering** i orden og en "
           "liste over **bemanding** og kurser, der viser, hvem der må gå i gang. Jeg har haft "
           "arbejdsmiljøansvaret på egne byggepladser: LOTO, APV, sikkerhedsrunderinger og "
           "opfølgning på nærved-hændelser. Den samme disciplin gælder over for **3F**: aftaler, der "
           "bliver overholdt, og en ledelse, der melder ud, før der bliver spurgt.", after=80)

    m.para("**Det, der skal standardiseres, er ikke huset.** Skanlux' produkt er skræddersyet — "
           "arkitektur, lys, udsigt og terræn. Det er ikke der, tiden bliver tabt. Den bliver tabt i "
           "beslutningerne omkring huset: hvornår grunden er klar, hvornår materialet er bestilt, "
           "hvem der godkender en ændring, og hvornår kunden får besked. Standarder for de fire ting "
           "giver plads til det skræddersyede, fordi processen ikke skal opfindes igen for hver "
           "bolig.", after=80)

    m.para("Jeg bor i Måløv og kender køreturen til Nykøbing Falster; den tager jeg, fordi arbejdet "
           "ligger på pladserne og ikke ved et skrivebord. Jeg kan tiltræde snarest og vil gerne "
           "bruge de første uger sammen med **byggechef** Michael Dan Julsbo og byggelederne Øst og "
           "Vest.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Produktions- og projektleder med 20+ års ansvar for **produktion**, **bemanding** og "
           "**økonomi** i byggeri, entreprise og reguleret drift — **elautoriseret maskinmester** "
           "(LV/MV/HV), el- og maskinteknisk design (EQF 6), B.Tech i teknologiledelse og "
           "maskinteknik. Fuldt P&L i egen virksomhed siden 2023, 11 samtidige entrepriser med 14 "
           "mand, 37 CAPEX-projekter med budget og prognose, og nul kritiske fund ved aflevering.",
           after=80)

    m.section("PRODUKTION, KAPACITET OG TIDSPLAN")
    for label, body in [
        ("Udsyn og bemanding",
         "Udsynsplan 8–12 uger pr. sag med fag, rækkefølge og leverancedatoer; bemanding flyttet "
         "mellem sager efter flaskehals, ikke efter vane."),
        ("Ugentligt tidsplansmøde",
         "Fast dagsorden, skrevne beslutninger og ændringer i samme referat; fremdrift målt på "
         "milepæle, så en glidning bliver synlig i den uge, den opstår."),
        ("Byggeledere og formænd",
         "Ledelse af byggeledere, formænd og 14-mands entrepriseteam på skiftende pladser; "
         "situationsbestemt ledelse (SLII) og delegering med skrevet mandat."),
    ]:
        m.bullet(label, body)

    m.section("ØKONOMI, KOSTPRISER OG EFTERKALKYLATION")
    for label, body in [
        ("Produktionsomkostninger",
         "Opfølgning på timer, materialer og **ressourceforbrug** pr. enhed; afvigelser forklaret "
         "med årsag og handling, før de nåede regnskabet."),
        ("Ændringer i kostpriser",
         "Ændringslog med pris, ejer og godkendelse i samme uge som ændringen; konsekvens for "
         "kostpris og tidsplan vurderet ved kilden."),
        ("Efterkalkulation",
         "Efterkalkulation brugt som prisfastsættelse af næste sag: ressourcetræk pr. fag holdt op "
         "mod kalkulen, og afvigelsen skrevet ned, mens sagen var frisk."),
    ]:
        m.bullet(label, body)

    m.section("HÅNDVÆRKERE OG ARBEJDSMILJØ")
    for label, body in [
        ("Egne håndværkere",
         "Personaleansvar for timelønnede: ansættelser, bemanding, oplæring og MUS; 5 elektrikere "
         "og 3 lærlinge med kompetencematrix og plan for **uddannelse** og **certificering**."),
        ("Underentreprenører",
         "Rammeaftale og **prisforhandlinger** i egen virksomhed; **samarbejdsaftaler**, "
         "ansvarsgrænser og udskiftning, når leveringsevnen ikke holdt."),
        ("Kvalitet og arbejdsmiljø",
         "**Kvalitetssikring** med KS-plan og egenkontrol pr. fag; LOTO, APV, risikovurdering ved "
         "pladsopstart og sikkerhedsrunderinger med opfølgning."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Ejer / teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · fuldt P&L · udbud, kalkulation og underentreprenører")
    m.bullet("Produktion og forretning i egen hånd",
              "Sager fra tilbud til aflevering med eget budget og egen risiko; **rekvisitioner**, "
              "materialestyring og **arbejdsgange** — og ansvaret for at sige nej, når kalkulen "
              "ikke holdt.")

    m.job("Senior idriftsættelsesingeniør / projektleder, elsystem",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024",
          scope="37 samtidige CAPEX-projekter · 25 specialister · GMP/FDA/EMA")
    m.bullet("Fremdrift, økonomi og leverance",
              "Projektgrundlag, milepæle og månedsrapportering i SAP ERP; **kvalitetskontrol** og "
              "aflevering med protokoller skrevet før testen — nul kritiske fund.")

    m.job("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · DKK 2–10 mio.")
    m.bullet("Kapacitet i pressede uger",
              "Daglige tavlemøder og flaskehalsanalyser; mandskab og underentreprenører flyttet "
              "mellem sager, når en entreprise trak mere end planlagt.")

    m.job("Vedligeholdelses- og driftsleder", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="Anlæg i 24/7-drift · pumper, HVAC, højspændingstavler, SCADA")
    m.bullet("Drift, der ikke må stoppe",
              "Forebyggende vedligehold og akut fejlfinding i døgndrift; 5S og standard work på "
              "værksted og lager, LOTO og APV.")

    m.job("Elektromekaniker / produktionsteamleder",
          "ARJ Engineering · Teheran · dec. 2003–mar. 2010 · 12 mekanikere og teknikere")

    # ---------------------------------------------------------------- side 3
    m.page_break()
    m.section("UDDANNELSE OG AUTORISATION")
    m.edu("Elautoriseret maskinmester — dansk elautorisation LV/MV/HV",
          "Sikkerhedsstyrelsen · maj 2023")
    m.edu("B.Tech, teknologiledelse og maskinteknik (EQF 6)",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12")
    m.edu("El- og maskinteknisk design, elteknik (EQF 6)", "Tehran Technical University · 2000–2003")
    m.edu("Køleteknik & klimaanlæg (AMU) · Lean: 5S, PDCA, VSM, A3",
          "Mercantec · 2021 · STCW sikkerhedskurser (2021–2023)")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("**Dansk:** modersmål · **Engelsk:** professionelt, skriftligt og mundtligt · **Persisk:** "
           "modersmål · **Bosat i Måløv**, kører til Nykøbing Falster · **Kan tiltræde snarest** · "
           "Referencer efter aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA OVERBLIK TIL FØRSTE KVARTAL MED TAL",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–2",
             "Møde **byggeledere** Øst og Vest, gennemgå **tidsplaner** og "
             "**efterkalkulationer** på de sidste ti huse og finde de tre steder, hvor "
             "**kapacitetsudnyttelse** går tabt i dag."),
            ("Dag 30",
             "Én fælles ramme for det ugentlige **tidsplansmøde**, én **rekvisition** og "
             "**udsyn**splan otte uger frem for de næste femten sager."),
            ("Dag 60",
             "Log for ændringer i **kostpriser** pr. sag; første **efterkalkulation** gennemgået med "
             "byggechefen, og kursusmatrix for alle håndværkere lagt frem."),
            ("Dag 90",
             "**Kapacitetsplan** for næste kvartal med **bemanding** pr. fag — og tal for udnyttelse, "
             "spild og leverance pr. hus til ledelsen."),
        ],
        widths=(1500, 8830))

    m.section("EFTERKALKYLATIONEN SKAL LÆRE OS NOGET OM DET NÆSTE HUS")
    m.para("En efterkalkulation, der kun fortæller, at sagen blev dyrere, er en regning uden "
           "adresse. Den skal svare på tre ting: hvilket fag trak flere timer, hvilken ændring var "
           "ikke prissat, og hvad koster det samme hus næste gang. Det kræver, at timerne er "
           "registreret pr. fag og ikke pr. plads, og at ændringerne har været i en log undervejs. "
           "Jeg har gjort det på 37 projekter, hvor budget og prognose blev opdateret hver måned — "
           "ikke fordi det var sjovt, men fordi det er den eneste måde, en kalkule bliver bedre på "
           "den anden side.", after=70)

    m.section("UNDERENTREPRENØRER ER EN KAPACITET, IKKE EN UNDSKYLDNING")
    m.para("Når egne håndværkere er booket, er underentreprenøren det, der afgør, om huset bliver "
           "færdigt. Derfor er **rammeaftaler** og **samarbejdsaftaler** et kapacitetsværktøj og ikke "
           "kun et indkøbsdokument: en fast aftale med pris og responstid gør det muligt at sige "
           "\"I kommer tirsdag\" i stedet for \"hvor er I?\". I egen virksomhed har jeg forhandlet "
           "priser og vilkår og skiftet leverandør, når leveringsevnen faldt — og det gør man med "
           "en aftale, der var skrevet, før det blev nødvendigt.", after=70)

    m.section("STILLADSKURSET ER EN DEL AF BEMANDINGSPLANEN")
    m.para("Et **stilladskursus** bliver dyrt, hvis det bliver booket, fordi nogen opdager det i "
           "uge 40. Det skal stå i samme plan som **bemanding**en: hvem har hvad, hvornår udløber "
           "det, og hvem skal have det, før vi sætter ham på en opgave. Jeg har arbejdet med "
           "kompetencematrix, oplæring af tre lærlinge og sikkerhedsdokumentation, hvor manglende "
           "**certificering** betød, at en mand ikke måtte gå i gang — og det er billigere at "
           "planlægge end at forklare.", after=0)

    m.section("HVOR JEG VILLE STARTE")
    m.para("På pladserne. Første uge vil jeg køre med to **byggeledere** — én Øst, én Vest — og se, "
           "hvor timen faktisk går hen: venter folk på materiale, på en beslutning eller på den næste "
           "grund? Derefter sætte det ugentlige **tidsplansmøde** op med fire faste punkter og et "
           "**udsyn**, der viser de næste otte uger. **Kapacitet** bliver først et tal, når nogen "
           "skriver det ned hver uge — og det er den vane, jeg tager med.", after=0)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "HVAD STILLINGEN KRÆVER — HVAD JEG HAR LEVERET",
        ["Krav i opslaget", "Bevis"],
        [
            ("Ledende rolle i byggebranchen med ansvar for produktion og byggeprojekter",
             "Fuldt P&L siden 2023; 11 samtidige entrepriser med 14 mand; 37 CAPEX-projekter."),
            ("Daglig ledelse, koordinering og optimering af produktionen",
             "Daglige tavlemøder og flaskehalsanalyser på 11 entrepriser; mandskab flyttet mellem sager."),
            ("Produktionsstyring, kapacitetsplanlægning og koordinering af ressourcer",
             "Udsynsplan 8–12 uger pr. sag, bemanding pr. fag og leverancekontrol to uger før."),
            ("Kapacitetsudnyttelse af egne håndværkere og underentreprenører",
             "Folk flyttet efter flaskehals; underentreprenør sat ind, før eget mandskab stod stille."),
            ("Personaleansvar for timelønnede håndværkere, bemanding, tilgang og afgang",
             "5 elektrikere og 3 lærlinge samt 14-mands team: ansættelser, vagtplan, oplæring, MUS."),
            ("Lede og udvikle produktionsorganisationen og sikre kompetencer og ressourcer",
             "Kompetencematrix pr. fag, oplæringsplan og kursusoversigt koblet til bemandingen."),
            ("Underentreprenører: rammeaftaler, prisforhandlinger og samarbejdsaftaler",
             "Rammeaftaler og priser forhandlet i egen virksomhed; underentreprenør skiftet ved svigt."),
            ("Kvalitet, fremdrift og tidsplaner på tværs af alle byggesager",
             "Milepæle, ugentlig fremdrift og kvalitetstjek pr. fase; nul kritiske fund ved aflevering."),
            ("Økonomi og fremdrift pr. projekt, produktionsomkostninger og ressourceforbrug",
             "Budget, prognose og milepæle pr. projekt; månedsrapport og omkostning pr. enhed."),
            ("Deltage i vurdering og håndtering af ændringer i kostpriser",
             "Ændringslog med pris, ejer og godkendelse i samme uge som ændringen."),
            ("Deltagelse i processen omkring efterkalkulationer",
             "Efterkalkulation brugt til at prisfastsætte næste sag; ressourcetræk pr. fag."),
            ("Afholdelse af ugentlige tidsplansmøder",
             "Ugentligt tidsplansmøde med fast dagsorden; beslutninger i samme referat."),
            ("Daglig sparring og byggepladsbesøg med byggeledere og underentreprenører",
             "Gemba på pladsen, daglig sparring og faste besøg med tjekliste og opfølgning."),
            ("Rekvisitioner, nye arbejdsgange samt standardisering af processer",
             "Ét rekvisitionsflow; nye arbejdsgange indført med instruktion og opfølgning."),
            ("Kontaktperson mellem virksomheden, Arbejdstilsynet og 3F",
             "Arbejdsmiljøansvar: APV, LOTO, sikkerhedsrunder og opfølgning på nærved-hændelser."),
            ("Uddannelse og certificering, herunder stilladskurser",
             "Kursusmatrix: stillads, lift, LOTO og førstehjælp planlagt efter bemandingen."),
            ("Forretningsforståelse og balance mellem kvalitet, økonomi og fremdrift",
             "Fuldt P&L og egne kalkuler; prioriteret efter dækning med kvalitet som bundlinje."),
            ("Struktureret og handlingsorienteret; følgeskab og eksekvering",
             "Få faste møder og opgaver med navn og dato; eksekvering fulgt op ugen efter."),
            ("Tydelig i din kommunikation",
             "Status i klart sprog, også når den er dårlig; beslutningsgrundlag på én side."),
            ("Relationsskabende og samarbejdsorienteret",
             "Bygherrer, byggeledere, underentreprenører og egne folk i 20+ år; meldt ud i tide."),
            ("Robust og bevarer overblikket i en travl hverdag",
             "Nedbrud og omprioritering i døgndrift; prioritering efter konsekvens."),
            ("Bidrage til udvikling og professionalisering af Skanlux Byggefirma",
             "Standarder og dashboards indført og delt; forbedring dokumenteret i tal."),
            ("Eventuelt en relevant byggefaglig baggrund",
             "El- og maskinteknisk baggrund (EQF 6), B.Tech; byggefaglig praksis fra entreprise."),
        ],
        widths=(3600, 6746))

    m.section("SÆSONEN ER EN DEADLINE, INGEN HAR SKREVET NED")
    m.para("En **feriebolig** har en kunde med en plan: sommerferien. Det gør maj og juni til de "
           "måneder, hvor en uges forsinkelse ikke bare flytter et møde — den flytter en families "
           "ferie. Derfor skal **kapacitetsplanlægning** læses baglæns fra den dato, huset skal stå "
           "færdigt: hvornår skal taget være på, hvornår skal el og VVS ind, og hvornår skal grunden "
           "være klar. Jeg har planlagt baglæns fra faste idriftsættelsesdatoer før, og en fast dato "
           "er en fast dato — også når den er en sommerferie.", after=0)

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_Skanlux_Produktionschef.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_Skanlux_Produktionschef.docx'))
