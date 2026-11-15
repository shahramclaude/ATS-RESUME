# -*- coding: utf-8 -*-
"""Enity A/S — Sales Executive (Account Executive), Køge.

Dansk opslag → dansk dokument: ansøgning p1, CV p2–3, 90 dage + kravmatrix p4.
Vinkel: energisalg afgøres foran målerskabet, ikke i mødelokalet — teknisk indsigt
skal blive en dokumenterbar besparelse, og new logos kræver egen markedsadgang.
Policy: master/README.md — jobbet først, kandidaten kun som bevis, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Sales Executive · Teknisk salg, energidata og new logos'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv, Danmark'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("7. november 2026")
    m.meta("Enity A/S · Salg · Køge · via GlobeSearch")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Sales Executive", bold=True, color='1A1A1A')
    m.para("Til VP of Commercial Growth og Enitys ledelse", after=70)

    # ---------------------------------------------------------------- side 1
    m.para("Et energisalg bliver sjældent afgjort i mødelokalet. Det bliver afgjort foran målerskabet, i "
           "teknikrummet eller på taget, hvor det står klart, om forbruget kommer fra en forkert styring, en "
           "gammel pumpe eller en driftsrutine, som ingen har rørt siden 2019. Det er den samtale, jeg har "
           "ført i tyve år — og det er den samtale, jeg vil føre for Enity.", after=80)

    m.para("**Enity sælger ikke software alene, og det er netop pointen.** Platformen er differentieret ved, at "
           "nogen hjælper kunden med at forstå, hvad data betyder, og hvad der skal gøres ved det. Jeg har "
           "stået på den anden side af den samtale: som den, der skulle levere besparelsen og dokumentere den "
           "bagefter. Jeg ved, hvor et værdicase knækker — ikke i præsentationen, men et år senere, når "
           "forbruget ikke faldt, fordi ingen tog ansvar for driften af løsningen.", after=80)

    m.para("**New logos betyder egen adgang til markedet — og den har jeg bygget fra nul.** Siden maj 2023 har "
           "jeg drevet ELOHVAC med **fuldt P&L-ansvar**, fem elektrikere og tre lærlinge. Hver kunde i den "
           "virksomhed er kommet gennem min egen dialog med driftsansvarlige, facility managers, tekniske "
           "chefer og indkøbere i Storkøbenhavn, ikke gennem et leadflow. En leadgenerator giver møder; den "
           "giver ikke adgang til den person, der ejer anlægget og budgettet. Det sidste er salgsarbejdet, og "
           "det er det, jeg søger her — som **Account Executive** med ansvar for new logos på Sjælland.", after=80)

    m.para("**Teknisk indsigt er kun en fordel, når den bliver et tal på bundlinjen.** Jeg regner tilbud og "
           "værdicases med investering, **payback** og følsomhed, fordi en driftschef og en økonomidirektør "
           "skal kunne se det samme tal og nå samme konklusion. Effekten har jeg leveret: **40 % lavere "
           "energiomkostninger** gennem et PDCA-program hos Novo Nordisk og **over 40 % lavere forbrug** i et "
           "energiprogram på Lynetten i 24/7-drift. Begge steder målt, rapporteret og dokumenteret — den samme "
           "form for dokumentation, Enity leverer til kundernes grønne rapportering.", after=80)

    m.para("**Discovery foregår ude i bygningen, fordi det er der, spildet sidder.** Med hovedmåler og "
           "bimålere bliver et forbrugsprofil til en historie om driftstider, natforbrug, tomgang og "
           "samtidighed. Jeg går anlægget efter på samme måde: **tavler, ventilation, HVAC, SRO og SCADA**, "
           "og jeg bygger selv de **Power BI**-visninger, der gør profilen læsbar for en driftschef uden at "
           "han skal ringe til en ingeniør. Det er den halve løsning, der skaber tillid nok til at tale om den "
           "anden halve.", after=80)

    m.para("**En pipeline er en kapacitetsbeslutning, ikke en liste.** Jeg driver i dag ordrebog, "
           "**tilbud** og **forecast** med ugentlig opfølgning: hvilke sager er i hvilket stadie, hvad er "
           "næste handling, og hvornår falder svaret. Det holder to ting ærlige — at **forecast**et passer med, "
           "hvad der faktisk kan leveres, og at der ikke bliver solgt arbejde, som kapaciteten ikke kan bære. "
           "Uden den disciplin bliver et godt salg et driftsproblem, og kunden husker kun det sidste.", after=80)

    m.para("**Der er to beslutningstagere i hver sag, og de køber ikke det samme.** Den tekniske vil vide, om "
           "løsningen kan stå i ti år og hvem der rykker ud, når den ikke gør. Den kommercielle vil vide, hvad "
           "det koster, hvad der kommer tilbage, og hvornår. Som ejer har jeg ført begge samtaler selv — med "
           "driftschefen om, hvad der faktisk fejler, og med **indkøberen** om pris, vilkår og hvad der sker, "
           "når anlægget står stille i uge 32.", after=80)

    m.para("**Sælgeren må ikke love mere, end installationen kan levere.** Projektering, **dimensionering** og "
           "**kvalitetssikring** er ikke en backoffice-funktion, der kommer efter aftalen; det er det, der gør "
           "aftalen holdbar. Jeg er selv den tekniske modpart, kan dimensionere og kvalitetssikre og står "
           "bagefter med ansvaret ved afleveringen. Når **teknik** og rådgivning sidder tæt på salget, bliver "
           "salgscyklussen kortere, fordi kunden ikke skal vente på svar.", after=80)

    m.para("**Enity har et fundament, de fleste salgsroller ikke får.** En dansk **CleanTech**-virksomhed med over "
           "25 års erfaring inden for **energioptimering**, ejerskab af **OK**, mere end 22.500 ejendomme på "
           "platformen, Gazelle-status "
           "og en egen AI- og innovationsafdeling — plus kontorer i Viby og Duisburg. Det gør **Sjælland** til "
           "hjemmebane og den tyske forretning til en reel mulighed, som jeg kan tage del i på **engelsk** "
           "og **dansk**.", after=80)

    m.para("Jeg bor i Måløv, har kørekort og kan være i **Køge** og ude hos kunderne på Sjælland hver dag. Jeg "
           "vil gerne høre, hvilke segmenter new logos-arbejdet skal bæres af i det første år — private og "
           "offentlige bygningsporteføljer eller også produktionslinjer og vognparker — hvordan teknik og "
           "energirådgivning er organiseret omkring salget, og hvor mange nye kunder der skal lukkes for at "
           "kalde væksten accelereret.", after=70)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Teknisk sælger og forretningsansvarlig med 20+ års erfaring i el, energi og bygningsdrift — i dag "
           "ejer af ELOHVAC med **fuldt P&L-ansvar**, ordrebog, tilbud og forecast. **Elautoriseret "
           "maskinmester (LV/MV/HV)** med hænderne i tavler, styring, ventilation, HVAC og SCADA, og med "
           "**dokumenterede besparelser**: 40 % lavere energiomkostninger hos Novo Nordisk og over 40 % lavere "
           "forbrug på Lynetten. Bygger værdicases med payback og følsomhed, arbejder i **SAP ERP, Power BI, "
           "Excel og Python**, og kommunikerer professionelt på **dansk** og **engelsk**.", after=80)

    m.section("SALG, KUNDER OG FORRETNING")
    for label, body in [
        ("New logos og egen markedsadgang",
         "Kundebasen i egen virksomhed er skabt fra nul gennem direkte dialog med driftsansvarlige, facility "
         "managers, tekniske chefer og indkøbere — uden leadflow, udelukkende på møder, referencer og "
         "opfølgning."),
        ("Fra teknisk problem til værdicase",
         "Forbrugs- og fejlanalyse omsat til investering, payback og driftseffekt; tilbudt løsning beskrevet "
         "i kundens egne driftsmæssige konsekvenser, ikke i produktblade."),
        ("Discovery ude i bygningen",
         "Anlæg gennemgået på stedet: tavler, ventilation, HVAC, SRO/SCADA, driftstider og natforbrug; "
         "målinger og Power BI-visninger gjort læsbare for både teknik og ledelse."),
        ("Tilbud, forhandling og closing",
         "Beregning og tilbud på el-tekniske opgaver fra akutte udkald til afleveret anlæg; pris, vilkår, "
         "responstid og ansvar forhandlet på plads, før arbejdet startede, med serviceaftaler som gentagen "
         "forretning."),
        ("Pipeline, opfølgning og forecast",
         "Ordrebog og tilbudspipeline med ugentlig opfølgning i SAP ERP og Excel; næste handling og dato på "
         "hver sag, og et forecast der følger den faktiske kapacitet."),
        ("Teknik, rådgivning og kvalitetssikring i samme spor",
         "Projektering, dimensionering og KS løftet i samme spor som salget — med underentreprenører, "
         "leverandører og rådgivere koordineret, og dokumentationen klar ved aflevering."),
    ]:
        m.bullet(label, body, after=25)

    m.section("ERHVERVSERFARING")
    jobs = [
        ("Ejer / teknisk direktør",
         "ELOHVAC ApS · København · maj 2023–nu",
         "5 elektrikere + 3 lærlinge · fuldt P&L · ordrebog, tilbud og forecast",
         [("Salg og kundeforhold",
           "El-tekniske opgaver for erhvervskunder, fra akutte udkald til afleveret anlæg; tilbud og "
           "beregning, pris og vilkår, og en serviceaftale der holder kunden i drift bagefter."),
          ("Energi, data og værdi",
           "Forbrugsprofiler og fejlfinding på tavler, styring, ventilation og klimaanlæg; tiltag prioriteret "
           "efter payback, og effekten dokumenteret i Power BI og Python-værktøjer med over 40 % "
           "produktivitetsløft i det administrative arbejde.")]),
        ("Senior idriftsættelsesingeniør / projektleder, elsystem",
         "Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024",
         "37 parallelle CAPEX-projekter · 25 specialister · GMP/FDA/EMA",
         [("Energiprogram med dokumenteret effekt",
           "PDCA-program der gav 40 % lavere energiomkostninger: måling, årsagsanalyse, prioriterede tiltag "
           "og månedlig rapportering til ledelse og bygherre."),
          ("Interessenter og aflevering",
           "Fremdrift, økonomi og snitflader på tværs af teknik, indkøb og drift; afleveringsdokumentation "
           "uden kritiske afvigelser.")]),
        ("Projekt- og værkstedsleder",
         "Ventek-Air · København · jan. 2022–nov. 2022",
         "14 medarbejdere · 11 samtidige anlægsprojekter · DKK 2–10 mio.",
         [("Tilbud og aftalegrundlag",
           "Udbud og tilbud på 11 anlægsprojekter med underentreprenører og aftalegrundlag; daglig "
           "kapacitetsstyring og leveringsevne som måltal.")]),
        ("Vedligeholdelses- og driftsleder",
         "Lynetten under Biofos · København · aug. 2017–jan. 2022",
         "Kritisk anlæg i 24/7-drift · højspænding · SRO/SCADA",
         [("Energi i 24/7-drift",
           "Pumper, HVAC og højspændingstavler med oppetid som krav; energiprogram og 5S/PDCA på værksted og "
           "lager med over 40 % lavere forbrug.")]),
        ("Elektromekaniker / produktionsteamleder",
         "ARJ Engineering · Teheran · dec. 2003–mar. 2010",
         "12 mekanikere og teknikere · industrianlæg",
         [("Levering til kunder",
           "Fejldiagnose, reparation og korrigerende handlinger på industrielle anlæg; vagt-, materiale- og "
           "målopfølgning for 12 mand.")]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section("UDDANNELSE OG AUTORISATION")
    m.edu("B.Tech, teknologiledelse og maskinteknik",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12")
    m.edu("El- og maskinteknisk design, elteknik (EQF6)",
          "Tehran Technical University · 2000–2003")
    m.edu("Dansk elautorisation LV/MV/HV — elautoriseret maskinmester",
          "Sikkerhedsstyrelsen · maj 2023")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("Dansk: modersmål, flydende i skrift og tale · **Engelsk: professionelt** i møder, tilbud og "
           "dokumentation · Persisk: modersmål · **Bosat i Måløv**, kan være i Køge og hos kunder på Sjælland "
           "hver dag · Kørekort B · Kan tiltræde snarest muligt · Referencer efter aftale.", after=70)

    m.models_table("DE FØRSTE 90 DAGE — NEW LOGOS PÅ SJÆLLAND",
                   ("Periode", "Hvad der sker, og hvordan det måles"), [
        ("Uge 1–2",
         "Lær platformen og værdicaset på kundens præmisser: gennemgå EMS, måleteknologi og de cases, der "
         "allerede er vundet og tabt; mød teknik og energirådgivning og aftal, hvordan en sag kvalificeres, "
         "før den bliver en projektering."),
        ("Dag 30",
         "Egen målrettet liste over segmenter og adresser på Sjælland — bygningsporteføljer, offentlige "
         "ejendomme og erhverv — med en første bølge af møder booket gennem eget netværk og Enitys "
         "leadgenerering; pipeline defineret med stadier, kriterier og næste handling."),
        ("Dag 60",
         "Første discovery-forløb gennemført ude i bygningen med måling, forbrugsprofil og værdicase med "
         "payback; tilbud afgivet i Enitys format; forecast på plads med ugentlig opfølgning og fælles "
         "vurdering med VP of Commercial Growth."),
        ("Dag 90",
         "Første aftaler lukket, og et mønster der kan gentages: hvilke segmenter svarer, hvilke indvendinger "
         "går igen, og hvor i processen sagerne tabes — omsat til justeret målretning, kortere tid fra "
         "første møde til tilbud og et forecast, der kan stå ved siden af kvartalets mål.")])

    m.section("SALG TIL BYGNINGER HANDLER OM DRIFT, IKKE OM TEKNOLOGI")
    m.para("Den, der ejer problemet, er ikke altid den, der ejer budgettet. Driftschefen mærker spildet hver "
           "dag, men ejendomsdirektøren underskriver, og indkøb stiller spørgsmål til vilkårene. Derfor "
           "starter jeg med at finde ud af, hvem der faktisk kan sige ja — og hvad den person bliver målt på i "
           "år. Er svaret CO2-rapportering, sælger jeg ikke en energibesparelse; så sælger jeg et tal, der kan "
           "stå i en rapport uden at nogen skal forklare det bagefter.", after=80)

    m.section("ET TILBUD ER EN KONTRAKT OM DRIFT")
    m.para("Forskellen på en løsning, der holder, og en der bliver slukket efter et halvt år, ligger næsten "
           "altid efter underskriften: hvem kigger på tallene, hvem reagerer, når et forbrug stiger en "
           "tirsdag morgen, og hvad er aftalt om opfølgning. Jeg har siddet med serviceaftaler og responstider "
           "i min egen virksomhed, og det er den del, jeg sælger med — ikke som merydelse, men som det, der gør "
           "besparelsen til en besparelse.", after=80)

    m.section("DET, DER GØR EN NEW-LOGO-SAG LANG, ER SJÆLDENT PRISEN")
    m.para("Sager går i stå, fordi beslutningsgrundlaget er uklart: hvilke målere der skal op, hvem der giver "
           "adgang til teknikrummet, hvad der skal ske med eksisterende aftaler, og hvordan gevinsten "
           "fordeles mellem ejer og lejer. Jeg tager de spørgsmål tidligt, skriftligt og med en navngiven "
           "ansvarlig på kundens side — og i offentlige forløb med udbudsprocessen for øje, så tilbuddet "
           "passer til den ramme, kunden reelt kan købe inden for.", after=80)

    m.section("I DUISBURG SÆLGES DER IKKE PÅ DANSK")
    m.para("En dansk **SaaS**-platform med aktiviteter i Tyskland kræver, at værdicaset, dokumentationen og møderne "
           "kan holde på engelsk — uden at nuancerne forsvinder på vejen. Jeg arbejder på engelsk i det "
           "daglige, har al dokumentation og rapportering på begge sprog og er vant til at møde en teknisk "
           "modpart, der stiller flere og mere præcise spørgsmål end den danske.", after=80)

    m.page_break()

    m.models_table("HVAD STILLINGEN KRÆVER — HVAD JEG HAR LEVERET", ("Krav i opslaget", "Bevis"), [
        ('Drive hele salgsprocessen for new logos fra første kontakt og discovery til tilbud, forhandling og closing',
         'Egen virksomhed siden 2023: kundebase skabt fra nul, tilbud og beregning, pris og vilkår forhandlet, aftale lukket og afleveret — fuldt P&L-ansvar.'),
        ('Forstå kundens bygninger, energisystemer og driftsmæssige udfordringer og omsætte dem til løsninger og værdicases',
         'Tavler, styring, ventilation, HVAC og SRO/SCADA gennemgået på stedet; forbrugsprofiler omsat til investering, payback og driftseffekt.'),
        ('Opbygge relationer til både tekniske og kommercielle beslutningstagere',
         'Begge samtaler ført som ejer: driftsansvarlige og tekniske chefer om anlæg og oppetid, indkøbere og ledelse om pris, vilkår og risiko.'),
        ('Skabe nye muligheder gennem markedet, eget netværk og Enitys leadgenerering',
         'Kunder erhvervet på møder, referencer og opsøgende arbejde i Storkøbenhavn — netværket er bygget gennem ni år i dansk el- og energidrift.'),
        ('Samarbejde tæt med teknikere og energirådgivere om projektering, dimensionering og kvalitetssikring af løsningen',
         'Projektering, dimensionering og KS løftet i eget regi med underentreprenører og rådgivere; det, der blev lovet i salget, blev afleveret og dokumenteret.'),
        ('Opbygge og drive en kvalificeret pipeline med høj disciplin omkring prioritering, opfølgning og forecast',
         'Ordrebog, tilbudspipeline og ugentlig opfølgning i SAP ERP og Excel med næste handling og dato på hver sag; forecast afstemt mod kapacitet.'),
        ('Ansvarlig for at udvikle nye kunder og kommercielle relationer på Sjælland',
         'Bosat i Måløv med kunder i Storkøbenhavn og på Sjælland gennem de sidste ni år; kørekort og daglig tilstedeværelse hos kunderne.'),
        ('Selv kunne skabe adgang til markedet, udvikle relationer og drive egne muligheder fremad',
         'Ingen leadmotor i egen virksomhed: adgang skabt ved opsøgning, referencer og opfølgning, og hver sag drevet til beslutning uden indkøbsafdeling bag sig.'),
        ('Relevant teknisk eller kommerciel uddannelse, hvor dokumenterede resultater og erfaring vægtes højere',
         'Elautoriseret maskinmester (LV/MV/HV) og B.Tech i teknologiledelse og maskinteknik (7,6/12) — plus dokumenterede resultater i både salg og energi.'),
        ('Kombinationen af teknisk forståelse og kommercielt drive',
         'Teknisk: autorisation LV/MV/HV, tavler, styring, HVAC, SCADA. Kommercielt: fuldt P&L, ordrebog, tilbud og forhandling i egen virksomhed siden 2023.'),
        ('Komfortabel i kundedialogen og motiveret af at åbne nye kunder og udvikle new logos',
         'Alle kundeforhold i egen virksomhed er nye forhold, åbnet i direkte dialog; første møde foregår hos kunden, ofte i teknikrummet.'),
        ('Teknisk baggrund eller solid erfaring med løsninger inden for energi, IoT, bygninger, installationer eller beslægtede områder',
         'Tyve år i el, energi og bygningsdrift: installationer, måling, SRO/SCADA og energiprogrammer med over 40 % lavere forbrug.'),
        ('Erfaring med salg eller et tydeligt kommercielt potentiale og motiveres af new business og new logos',
         'Salg og forretning som ejer: tilbudsberegning, prissætning, forhandling og serviceaftaler — resultatet måles i ordrebog og P&L, ikke i aktivitet.'),
        ('Trives i den direkte kundedialog og kan omsætte tekniske problemstillinger til klar forretningsmæssig værdi',
         'Fejlfinding og forbrugsanalyse oversat til kundens beslutningsgrundlag: hvad det koster, hvad der kommer tilbage, og hvornår.'),
        ('Arbejder selvstændigt, struktureret og vedholdende',
         'Driver virksomhedens salg, drift og levering alene med fem elektrikere og tre lærlinge; skriftlig plan og dato på hver sag, også når svaret udebliver.'),
        ('Disciplin i arbejdet med pipeline, opfølgning og forecast',
         'Ugentlig pipelinegennemgang med stadier, næste handling og sandsynlighed; forecast holdt op mod kapacitet, så der ikke sælges mere, end der kan leveres.'),
        ('Kommunikerer professionelt på dansk og engelsk i skrift og tale',
         'Dansk som modersmål og professionelt engelsk i møder, tilbud og dokumentation — relevant for Enitys aktiviteter i Duisburg.'),
        ('Trives i et tæt samarbejde mellem salg, teknik og rådgivning',
         'Salg, teknik og KS i samme spor i egen virksomhed; i større organisationer 25 specialister og tværfaglige snitflader på 37 projekter.'),
    ], widths=(3600, 7046))

    return m.save(path, title="Sales Executive — Enity A/S",
                  subject="Teknisk salg, energidata og new logos",
                  keywords="salg, new logos, pipeline, forecast, energidata, EMS, cleantech, "
                           "energioptimering, bygninger, måleteknologi, køge, sjælland, dansk, engelsk")


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Enity_SalesExecutive.docx')))
