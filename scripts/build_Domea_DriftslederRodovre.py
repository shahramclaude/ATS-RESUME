# -*- coding: utf-8 -*-
"""Domea — Driftsleder, Rødovre (dansk opslag, frist 15. november 2026).

Dansk opslag → dansk dokument (da-DK): ansøgning side 1, CV side 2, uddannelse + 90 dage +
fire afsnit side 3, kravmatrix side 4.

STILVALG (master/STILREGISTER.md, policy 04.11.2026; godkendt af scripts/style_guard.py,
3/3 skift mod #186):
  register       = ENTREPRENØR — drift, vedligehold, udførelse og opfølgning; ikke
                   kundeservice-registret fra #186, det rådgivende fra #185 eller det
                   teknisk-driftsnære fra #184. Udtrykket er denne gang møde- og planstyret:
                   beslutning → plan → opgave → opfølgning, ikke værkstedstone.
  åbningsgreb    = E (TIDSFORSKYDNINGEN) — beslutningen ligger et år før opgaven og et år før
                   beboeren mærker den. Sidst brugt #174.
  struktur       = FØR/EFTER — afdelingen i dag og om tolv måneder, punkt for punkt, fordi
                   opslaget selv kalder området "i udvikling" og teamet "under opbygning".
                   Sidst brugt #178.
  kadence        = to korte sætninger pr. pointe: i dag / om tolv måneder — en plan, ikke en
                   personlighed.

Ingen opdigtede fakta: ingen erfaring med almen bolig eller afdelingsbestyrelser påstås.
Beboerdemokrati besvares som metode (dagsorden, beslutningsreferat, opfølgning) og som
interesse — opslaget spørger netop efter "erfaring med eller interesse for".

Policy: master/README.md — jobbet først, kandidaten kun som bevis, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Driftsleder · Daglig drift, vedligeholdelsesplaner og medarbejderudvikling'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("8. november 2026")
    m.meta("Domea Rødovre · Driftsleder · Boligafdelinger i Rødovre")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Driftsleder til Domea Rødovre", bold=True, color='1A1A1A')
    m.para("Til kundechef Simon Bødker", after=70)

    # ---------------------------------------------------------------- side 1
    m.para("Den vedligeholdelse, der bliver udført til næste forår, bliver besluttet på et møde i november — "
           "af en bestyrelse, der skal kunne se, hvad pengene går til, inden for en ramme, der allerede er "
           "lagt. Driftslederens arbejde sidder i den forskydning: beslutningen ligger et år før opgaven, og "
           "opgaven ligger et år før beboeren mærker den. Derfor handler rollen lige så meget om at gøre "
           "beslutninger forståelige, som om at få dem udført.", after=80)

    m.para("**Driften i dag — og om tolv måneder.** I dag bliver opgaverne løst, fordi nogen husker dem. Om "
           "tolv måneder bliver de løst, fordi de står i en plan med en ansvarlig og en dato: hvad der er "
           "akut, hvad der er periodisk, og hvad der er et mindre projekt, der skal besluttes. Jeg har drevet "
           "**24/7-drift** i mere end fire år og ved, at overblik er en liste, der bliver gennemgået — ikke en "
           "egenskab.", after=80)

    m.para("**Medarbejderne i dag — og om tolv måneder.** Syv medarbejdere med hver deres rytme og fag, og en "
           "ejendomsmester, der skal kunne løfte opgaverne videre, når jeg ikke er der. Om tolv måneder skal "
           "hver af dem vide, hvad de bliver målt på, og hvad de er på vej til. Jeg har ledet **5, 12, 14 og "
           "25 mand** med MUS, 1:1 og kompetencematrix, og lært at udvikling sker i hverdagen, ikke på "
           "kursus.", after=80)

    m.para("**Bestyrelserne i dag — og om tolv måneder.** Beboerdemokratiet er ikke en formalitet, der skal "
           "overstås; det er den proces, der afgør, om en istandsættelse bliver forstået eller bare vedtaget. "
           "Om tolv måneder skal bestyrelsen have en dagsorden, der er til at læse, et regnestykke, der er "
           "til at forstå, og et referat, der bliver fulgt op — også når svaret er nej.", after=80)

    m.para("**Økonomien i dag — og om tolv måneder.** Vedligeholdelsesplaner, budget og regnskab er én kæde: "
           "en udskiftning, der bliver udskudt i år, bliver dyrere næste år. Om tolv måneder skal hver post "
           "kunne forklares med en tilstand og en konsekvens, ikke med et skøn. Jeg har haft **fuldt "
           "P&L-ansvar** siden 2023 og rapporteret månedligt til ledelse og bygherre.", after=80)

    m.para("**Arbejdsgangene i dag — og om tolv måneder.** I dag forsvinder en henvendelse nogle gange mellem "
           "to telefoner. Om tolv måneder har den et sagsnummer, en ejer og en melding tilbage, når den er "
           "løst — og **servicekoordinatoren** og jeg kigger på den samme tavle. Jeg har indført 5S og "
           "standard work på værksted og lager og set, hvad det gør ved svartiden.", after=80)

    m.para("**Beboerne i dag — og om tolv måneder.** En beboer måler driften i det, der ikke sker: at "
           "vandet løber, at varmen virker, at opgangen er ryddet. Om tolv måneder skal beboeren vide, hvem "
           "der kommer, hvornår og hvorfor — og have fået svar, inden de ringer anden gang. Det er den samme "
           "disciplin som i en serviceaftale med aftalt responstid, og den kan måles.", after=80)

    m.para("**Håndværkere og indkøb i dag — og om tolv måneder.** I dag bestiller vi den håndværker, der "
           "tager telefonen. Om tolv måneder bestiller vi den, der har leveret til tiden de sidste tre gange, "
           "til en pris vi kender, med dokumentation der kan lægges i mappen. Jeg har styret "
           "underentreprenører og indkøb i egen virksomhed og på **11 samtidige entrepriser**.", after=80)

    m.para("**Rollerne omkring mig — servicekoordinator, kundechef og ejendomsmester.** Tre personer og en "
           "driftsleder kan let komme til at mene det samme om tre forskellige sager. Derfor aftaler vi "
           "grænserne først: hvem der ringer til beboeren, hvem der bestiller håndværkeren, og hvem der "
           "skriver til bestyrelsen. Det er den aftale, der holder, når ugen er travl.", after=80)

    m.para("**Sikkerhed og dokumentation — det, der ikke må gå galt.** Arbejdsmiljø, APV, sikkerhedsrundering "
           "og dokumentation på arbejdet er ikke papir ved siden af driften; det er der, en sag bliver "
           "lukket, så den ikke kommer igen. Jeg har arbejdet med **LOTO**, nærved-hændelser og eksterne "
           "tilsyn og ved, hvordan en myndighed læser en mappe.", after=80)

    m.para("**Domea — 95.000 boliger og en ambition om at gøre det bedre og billigere at bo.** Domea "
           "administrerer for almene boligorganisationer, der tilsammen ejer godt 95.000 boliger, og i den "
           "drift forvalter man beboernes penge, og det er den forskel, der gør rollen interessant: kvaliteten skal "
           "kunne ses i hverdagen, og økonomien skal kunne forklares i en bestyrelse. Jeg bor i **Måløv**, "
           "har ca. 20 minutter til Rødovre, bil og mulighed for **aftenmøder**.", after=80)

    m.para("Jeg vil gerne høre, hvilke boligafdelinger der ligger i området, hvordan vedligeholdelsesplanerne "
           "bliver lavet i dag, og hvad der fylder mest i bestyrelserne lige nu — og jeg vil gerne måles på, "
           "at planen holder, og at medarbejderne bliver længere, end de ellers ville.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Drifts- og vedligeholdelsesleder med 20+ års erfaring i teknisk drift, service og mindre projekter "
           "— **elautoriseret maskinmester (LV/MV/HV)**, el- og maskinteknisk design (EQF 6), B.Tech og "
           "**fuldt P&L-ansvar siden 2023**. Har drevet **24/7-anlæg** med vedligeholdelsesplaner, "
           "reservedelslager og 5S, ledet teams på **5, 12, 14 og 25 mand** med MUS og kompetencematrix, "
           "fulgt op på budget, timeforbrug og sagsøkonomi i **SAP ERP** og **Power BI** og siddet i "
           "ledelsesgruppen for en 24/7-drift. Dansk og engelsk.", after=80)

    m.section("DRIFT, VEDLIGEHOLDELSE OG OPFØLGNING")
    for label, body in [
        ("Daglig drift og prioritering",
         "Drift af kritisk anlæg døgnet rundt: akut fejlfinding, forebyggende vedligehold og en plan, der "
         "bliver gennemgået hver uge — ikke en liste, der bliver husket."),
        ("Vedligeholdelsesplaner og mindre projekter",
         "Planer pr. anlæg og komponent med interval, ansvarlig og dato; mindre projekter styret fra "
         "behov til aflevering med tid, pris og dokumentation."),
        ("Økonomi, budget og opfølgning",
         "Budget- og resultatansvar med månedsafslutning på timeforbrug, dækningsgrad og sagsøkonomi; "
         "rapportering til ledelse og bygherre i SAP ERP og Power BI."),
    ]:
        m.bullet(label, body, after=20)

    m.section("MEDARBEJDERE, SAMARBEJDE OG KOMMUNIKATION")
    for label, body in [
        ("Ledelse og udvikling",
         "5, 12, 14 og 25 medarbejdere ledet med MUS/GRUS, 1:1, kompetencematrix og udviklingsplaner; "
         "lærlinge og svende fulgt til selvstændigt arbejde."),
        ("Møder og beslutninger",
         "Afdelings-, budget- og statusmøder ledet med dagsorden, beslutningsreferat og opfølgning med ejer "
         "og dato; beslutninger forklaret i et sprog, modtageren kan bruge."),
        ("Samarbejdsflader",
         "Kunder, bygherrerepræsentanter, rådgivere, tilsyn og underentreprenører — og egne teams; konflikter "
         "løst på pladsen, før de blev en sag."),
    ]:
        m.bullet(label, body, after=20)

    m.section("SIKKERHED, KVALITET OG SYSTEMER")
    for label, body in [
        ("Arbejdsmiljø og sikkerhed",
         "APV, LOTO, sikkerhedsrunder, nærved-hændelser og værneudstyr; arbejdet dokumenteret, så et tilsyn "
         "kan følge det; ingen arbejdsulykker i egne teams."),
        ("Kvalitet og dokumentation",
         "KS på opgaven, afleveringsdokumentation og mangellukning; nul kritiske afvigelser i "
         "serviceaftalerne og i afleverede projekter."),
        ("Systemer",
         "SAP ERP til ordrer, økonomi og lager; Power BI til KPI'er og opfølgning; 5S og standard work på "
         "værksted og lager."),
    ]:
        m.bullet(label, body, after=20)

    m.section("ERHVERVSERFARING")
    jobs = [
        ("Ejer / teknisk direktør",
         "ELOHVAC ApS · København · maj 2023–nu",
         "5 elektrikere + 3 lærlinge · fuldt P&L · service, vedligehold og mindre projekter",
         [("Drift, kunder og økonomi",
           "Alle opgaver planlagt og afleveret under eget P&L; vedligeholdelsesaftaler med aftalt responstid, "
           "efterkalkulation pr. sag og månedlig opfølgning."),
          ("Medarbejdere og arbejdsmiljø",
           "Fem svende og tre lærlinge ledet dagligt; MUS, kompetencematrix, APV og sikkerhed på skiftende "
           "adresser.")]),
        ("Senior idriftsættelsesingeniør / projektleder, elsystem",
         "Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024",
         "37 samtidige anlægsprojekter · 25 specialister · GMP/FDA/EMA",
         [("Projekter, møder og økonomi",
           "37 samtidige projekter af DKK 2–10 mio. fra krav til aflevering; møder ledet med dagsorden og "
           "beslutningslog, økonomi og fremdrift rapporteret månedligt."),
          ("Aflevering og dokumentation",
           "Afleveringspakke, mangellukning og dokumentation under FDA/EMA-krav — nul kritiske fund.")]),
        ("Projekt- og værkstedsleder",
         "Ventek-Air · København · jan. 2022–nov. 2022",
         "14 medarbejdere · 11 samtidige entrepriser · DKK 2–10 mio.",
         [("Værksted, plan og levering",
           "14-mands værksted og 11 samtidige opgaver fra specifikation til aflevering; daglige tavlemøder og "
           "flaskehalsanalyse.")]),
        ("Vedligeholdelses- og driftsleder",
         "Lynetten under Biofos · København · aug. 2017–jan. 2022",
         "Kritisk anlæg i 24/7-drift · pumper, HVAC, højspændingstavler, SCADA",
         [("Vedligehold, sikkerhed og lager",
           "Forebyggende vedligehold og akut fejlfinding døgnet rundt; 5S, standard work og reservedelsflow; "
           "LOTO, APV og nærved-hændelser fulgt op.")]),
        ("Elektromekaniker / produktionsteamleder",
         "ARJ Engineering · Teheran · dec. 2003–mar. 2010",
         "12 mekanikere og teknikere · maskinværksted · industriel anlæg",
         [("Reparation og målstyring",
           "Fejldiagnose og reparation med rodårsagsanalyse; 12 mand planlagt og målt dagligt.")]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=18)

    # ---------------------------------------------------------------- side 3
    m.page_break()
    m.section("UDDANNELSE OG AUTORISATION")
    m.edu("Elautoriseret maskinmester — dansk elautorisation LV/MV/HV",
          "Sikkerhedsstyrelsen · maj 2023")
    m.edu("B.Tech, teknologiledelse og maskinteknik (EQF 6)",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12")
    m.edu("El- og maskinteknisk design, elteknik (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("Lean: 5S, PDCA, A3, standard work · Køleteknik og klimaanlæg (AMU)",
          "Mercantec · 2021 · anvendt i drift, lager og opfølgning")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("**Dansk: modersmål**, flydende i skrift og tale med beboere, bestyrelser, håndværkere og "
           "myndigheder · **Engelsk: professionel** · Persisk: modersmål · **Bosat i Måløv**, ca. 20 minutter "
           "til Rødovre · Kørekort B og bil · **Aftenmøder er en del af rollen og passer ind** · Kan tiltræde "
           "snarest · Referencer efter aftale.", after=70)

    m.models_table("DE FØRSTE 90 DAGE — OVERBLIK, PLAN OG MENNESKER",
                   ("Periode", "Hvad der sker, og hvordan det måles"), [
        ("Uge 1–2",
         "Med på runderne i boligafdelingerne med ejendomsmesteren; læs vedligeholdelsesplaner, budget og de "
         "sidste mødeprotokoller fra afdelingsbestyrelserne; mød servicekoordinatoren og kundechefen."),
        ("Dag 30",
         "Ét samlet overblik pr. boligafdeling: tilstand, åbne opgaver, planlagte indsatser og økonomisk "
         "ramme — med en ansvarlig og en dato på hver linje, og en liste over de tre ting, der haster mest."),
        ("Dag 60",
         "Fast ugentlig driftsgennemgang med ejendomsmester og servicekoordinator; sagsgangen fra henvendelse "
         "til lukket sag lagt om, så beboeren får en melding tilbage; første bestyrelsesmøde afholdt med "
         "dagsorden og referat."),
        ("Dag 90",
         "Vedligeholdelsesplan og budgetramme for næste år gennemgået med kundechefen; medarbejderudvikling "
         "aftalt for alle syv (MUS-plan for året); serviceniveauet beskrevet, så det kan måles."),
    ], widths=(1500, 8830))

    m.section("EN BESLUTNING, DER IKKE ER FORSTÅET, BLIVER EN KLAGE")
    m.para("I en boligafdeling bliver en istandsættelse ikke vurderet på, hvor godt den er udført, men på "
           "om den var det, beboerne havde fået forklaret. Derfor skal materialet til bestyrelsen kunne læses "
           "af en, der ikke er håndværker: hvad der er i stykker, hvad det koster at vente, og hvad "
           "alternativet er. Jeg har siddet på den anden side af bordet som bygherre og skal forklare et "
           "fagligt valg til nogen, der skulle beslutte det.", after=80)

    m.section("VEDLIGEHOLDELSE ER ET SPØRGSMÅL OM TID, IKKE OM LYST")
    m.para("En pakning, der skiftes i tide, koster en formiddag. Den samme pakning, der først bliver skiftet, "
           "når den er gået, koster en vandskade, en forsikringssag og en beboer, der skal genhuses. "
           "Vedligeholdelsesplanen er den eneste mekanisme, der flytter penge fra den dyre kategori til den "
           "billige — og den virker kun, hvis intervallet er sat efter tilstand og ikke efter vane.", after=80)

    m.section("SYV MEDARBEJDERE ER SYV GRUNDE TIL, AT DRIFTEN HOLDER")
    m.para("En ejendomsmester og seks ejendomsfunktionærer er ikke en ressource, der skal fordeles; det er "
           "syv mennesker, der hver især ved noget om bygningerne, som ikke står i nogen plan. Opgaven som "
           "leder er at få den viden ud af hovedet og ind i planen — og at gøre det i en tone, hvor man "
           "stadig fortæller, hvad man ser, når man ser det.", after=80)

    m.section("TILSYNET KOMMER UDEN AT BESTILLE TID")
    m.para("Arbejdsmiljø og brandforhold bliver ikke bedømt på hverdagen, men på den dag, nogen kigger. Så "
           "dokumentationen skal være klar, når hverdagen er travl: APV opdateret, runder gennemført og "
           "afvigelser lukket med en dato. Det er ikke bureaukrati; det er det, der gør, at en driftsleder "
           "kan sige, at huset er i orden, og mene det.", after=80)

    m.section("EN HENVENDELSE ER EN KÆDE, IKKE EN TELEFON")
    m.para("Når en beboer ringer om en utæthed, er der fire led: den, der tager telefonen; den, der vurderer "
           "og bestiller; den, der udfører; og den, der melder tilbage. Falder ét led ud, ringer beboeren "
           "igen — og næste gang til en anden. Derfor skal kæden være beskrevet, og der skal være en, der "
           "ejer den. Det arbejde har jeg gjort i service, i drift og i egen virksomhed, og det er der, "
           "kundetilfredsheden bliver skabt — ikke i den store plan.", after=80)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table("HVAD STILLINGEN KRÆVER — HVAD JEG HAR LEVERET",
                   ("Krav i opslaget", "Bevis"), [
        ("Lede, understøtte og udvikle medarbejdere i det daglige arbejde",
         "5, 12, 14 og 25 medarbejdere ledet dagligt med MUS/GRUS, 1:1, kompetencematrix og "
         "udviklingsplaner; oplæring sket i hverdagen."),
        ("Koordinere og følge op på drift, vedligeholdelse og mindre projekter",
         "24/7-drift med forebyggende vedligehold og akut fejlfinding; mindre projekter styret fra behov til "
         "aflevering med tid, pris og dokumentation."),
        ("Følge op på økonomi, budgetter og vedligeholdelsesplaner",
         "Fuldt P&L-ansvar siden 2023; budget, timeforbrug og sagsøkonomi fulgt månedligt i SAP ERP og "
         "Power BI, med vedligeholdelsesplaner pr. anlæg."),
        ("Skabe et tæt samarbejde med afdelingsbestyrelserne gennem dialog, kommunikation og opfølgning",
         "Beslutningsfora ledet med dagsorden, referat og opfølgning (bygherre, ledelsesgruppe, "
         "brugerkoordinering); materiale skrevet, så ikke-fagfolk kan beslutte på det."),
        ("Deltage i og afholde afdelings-, budget- og regnskabsmøder",
         "Afdelingsmøder, budgetmøder og statusmøder afholdt gennem 20 år; økonomi forklaret i mødet, ikke "
         "bagefter, og referatet fulgt op med ejer og dato."),
        ("Bidrage til udvikling af arbejdsgange, processer og serviceniveauer",
         "5S, standard work og sagsgang indført på værksted, lager og i service; svartid og afvigelser målt "
         "og forbedret med PDCA."),
        ("Nærmeste leder for en ejendomsmester og seks ejendomsfunktionærer, som du skal understøtte i deres arbejde og udvikling",
         "Teamledelse af samme størrelsesorden: 5 elektrikere og 3 lærlinge dagligt, 12 teknikere og "
         "14-mands værksted — med faglig sparring og opfølgning på den enkelte."),
        ("Daglig drift og vedligeholdelse af en række boligafdelinger i tæt samarbejde med en servicekoordinator og kundechefen",
         "Drift af flere adresser og anlæg samtidig; aftaler om hvem der kontakter kunden, bestiller "
         "håndværkeren og lukker sagen, aftalt skriftligt."),
        ("Erfaring med at skabe gode rammer for samarbejde og opgaveløsning",
         "Daglig tavle, faste møder og fælles prioritering i drift og projekt; teams på tværs af fag og "
         "adresser koordineret mod samme plan."),
        ("Kommunikerer klart og professionelt både mundtligt og skriftligt",
         "Dansk som modersmål og engelsk professionelt; dokumentation, afleveringspakker, referater og "
         "tilbud skrevet i et sprog, modtageren kan handle på."),
        ("Trives med mange forskellige samarbejdsrelationer",
         "Beboere og brugere, bygherre, rådgivere, tilsyn, håndværkere, underentreprenører og egne teams — "
         "ofte i samme uge og med modstridende ønsker."),
        ("Erfaring med eller interesse for at arbejde i en organisation med beboerdemokratiske processer",
         "Interesse og metode: beslutningsprocesser med dagsorden, beslutningsreferat og opfølgning, hvor "
         "beslutningen skal kunne forklares for dem, den gælder — og efterleves bagefter."),
        ("Arbejder struktureret og følger op på aftaler og opgaver",
         "Planer med ansvarlig og dato, månedshjul og opfølgning på hver post; opgaver lukket med en melding "
         "tilbage, ikke bare med en faktura."),
        ("Forståelse for økonomi, planlægning og prioritering",
         "Budget, kalkulation og efterkalkulation i egen virksomhed; prioritering mellem akutte og planlagte "
         "opgaver inden for en fast ramme, dokumenteret med tal."),
        ("Deltage i aftenmøder med afdelingsbestyrelserne",
         "Aften- og udvalgsmøder er en del af rollen og passer ind; bosat i Måløv med ca. 20 minutter til "
         "Rødovre og egen bil."),
    ], widths=(3600, 6746))

    m.section("RØDOVRE ER EN PORTEFØLJE, IKKE EN BYGNING")
    m.para("Flere boligafdelinger betyder, at den samme standard skal gælde på flere adresser med forskellig "
           "alder, forskellige installationer og forskellige bestyrelser. Det holder kun, hvis planen er "
           "bygget pr. afdeling og runderne følger samme skabelon — så en kollega kan tage en afdeling, de "
           "ikke kender, og stadig se, hvad der er i orden, og hvad der ikke er.", after=80)

    m.section("TRIVSEL ER EN DRIFTSINDIKATOR, IKKE EN STEMNING")
    m.para("Sygefravær, gennemtræk af medarbejdere og antallet af sager, der bliver liggende, hænger sammen. "
           "Derfor hører MUS og trivsel hjemme i samme møde som planen og økonomien: en ejendomsfunktionær, "
           "der er blevet lovet en ekstra mand i en måned, skal have ham — ellers bliver næste samtale om "
           "noget andet end arbejdet. Jeg har ledet teams gennem travle perioder ved at holde den slags "
           "aftaler, ikke ved at holde humøret oppe.", after=80)

    return m.save(path, title="Driftsleder, Domea Rødovre")


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Domea_DriftslederRodovre.docx')
    build(out)
    print(out)
