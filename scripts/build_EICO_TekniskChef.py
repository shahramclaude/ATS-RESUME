# -*- coding: utf-8 -*-
"""EICO — Teknisk chef, Teknik & Serviceafdelingen, Brønderslev.

Dansk leverance: ansøgning side 1 (opgave-først), CV side 2–3, 90 dage + kravmatrix side 4.
Policy: master/README.md — jobbet først, kandidaten kun som bevis; ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = "Teknisk chef · Teknisk service, fejlfinding og ledelse af et lille team"
CONTACT = "+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv"


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("7. november 2026")
    m.meta("EICO · Teknik & Serviceafdelingen · Brønderslev · via Kompetent")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Teknisk chef, EICO, Brønderslev", bold=True, color='1A1A1A')
    m.para("Til Partner Louise Andersen, Kompetent, tlf. 2060 2350", after=70)

    # ---------------------------------------------------------------- side 1
    m.para("Et produkt er ikke solgt færdigt, når ordren er bekræftet. Det er først færdigt, når emhætten "
           "hænger som den skal, når kunden ringer om en fejl og får et svar samme dag, og når den samme fejl "
           "ikke dukker op igen på næste sending. Teknik & Service er der, hvor EICOs produkter bliver "
           "vurderet af dem, der bruger dem hver dag — og det er den afdeling, jeg søger at lede.", after=80)

    m.para("**Tre medarbejdere skal ikke ledes fra et mødelokale.** En **arbejdende leder** er ikke den, der "
           "arbejder mest; det er den, der tager de sager, de andre ikke kan løse, og som samtidig gør "
           "arbejdsgangen så tydelig, at ingen behøver spørge, hvad der kommer først. Det kræver to ting: at "
           "man selv kan faget, og at der ligger en struktur, der holder, når tre kunder ringer samtidig, og "
           "to af dem har en montør stående på adressen.", after=80)

    m.para("**Fejlfinding er håndværk, og det er min baggrund.** Jeg er uddannet elektromekaniker og har "
           "arbejdet med reparation og fejlfinding på industrielt udstyr som **produktionsteamleder for 12 "
           "teknikere** i ARJ, før jeg blev **elautoriseret maskinmester (LV/MV/HV)**. Jeg har fejlfundet på "
           "**koblingsanlæg, "
           "transformere, motorer, frekvensomformere og tavler**, drevet **SRO/SCADA** i døgndrift på "
           "Lynetten og idriftsat styringer i et GMP-miljø. Jeg læser et **el-diagram**, jeg måler efter på "
           "anlægget, og jeg kan forklare kunden, hvad der er galt, uden at det lyder som en undskyldning.", after=80)

    m.para("**Ventilation har jeg arbejdet med fra kanal til styring.** I **Ventek-Air** ledede jeg **14 "
           "medarbejdere** og **11 samtidige projekter** med luftmængder, tryk, balancering, idriftsættelse og "
           "de **montører**, der står på pladsen og ringer, når noget ikke opfører sig som tegningen. Det er "
           "den samme samtale, EICOs serviceafdeling fører hver dag: en mand på en stige med et spørgsmål, "
           "der skal besvares, mens han stadig er der — ikke i en mail i morgen.", after=80)

    m.para("**Reklamationer er data, ikke bare omkostninger.** Den samme fejl på det samme produktnummer er "
           "ikke tre sager; det er én sag, der er opstået tre gange. I egen virksomhed har jeg haft "
           "**garanti- og reklamationssager** på egne leverancer og på materialer fra leverandører, og lært "
           "at en sag først er lukket, når årsagen er skrevet ned: produkt, serienummer, montageforhold og "
           "hvad der faktisk var galt. Det er det datagrundlag, der gør en **reklamation** til en "
           "**kvalitetsforbedring** hos den internationale leverandør i stedet for til en diskussion om "
           "kreditnotaen.", after=80)

    m.para("**Dialogen med en international leverandør bliver stærkere af, at der bliver stillet krav.** Jeg "
           "har arbejdet med kravsspecifikationer, FAT/SAT og afvigelser i et GMP-miljø, hvor en leverandør "
           "skulle dokumentere, hvad produktet kunne, før det blev taget i brug — og hvor manglende "
           "dokumentation var en sag og ikke en detalje. Den disciplin gælder også for en distributør: "
           "reservedelslister, fejlkoder, montagevejledninger og en fejlrapport, der er så præcis, at "
           "producenten kan handle på den.", after=80)

    m.para("**Kunder, forhandlere og montører skal tale med en, der har prøvet det.** Jeg har siddet på begge "
           "sider af den telefon: som den håndværker, der ringede til en leverandør og manglede et svar, og "
           "som den, der skulle svare, når en kunde havde en vare, der ikke virkede. **Teknisk support** før, "
           "under og efter salg handler om at stille de rigtige spørgsmål med det samme — produkt, model, "
           "installation, fejlkode — så svaret kan bruges første gang, og så hverken forhandler eller "
           "servicepartner skal ringe igen.", after=80)

    m.para("**Struktur i en travl hverdag er et system, ikke en personlig egenskab.** Jeg vil lægge et fast "
           "**sagsflow**: modtagelse, triage efter produkt og alvor, en **svartid** der er aftalt og ikke "
           "improviseret, en ejer på hver sag, og en lukning hvor årsagen bliver registreret. Så kan vi måle "
           "på det, der betyder noget — svartid, genbesøg, returprocent og **kundetilfredshed** — og færre "
           "unødige **omkostninger** kommer ikke af at arbejde hurtigere, men af at fjerne de sager, der ikke "
           "burde være opstået.", after=80)

    m.para("**Digitalisering og AI er noget, jeg har bygget, ikke noget jeg har læst om.** Jeg bruger "
           "**Python og Claude Code** til at bygge de værktøjer, der mangler: kalkulation, tjeklister, "
           "KPI-rapportering og opgavestyring — og til at gøre det skriftlige arbejde hurtigere, fra "
           "opsummering af en sag til første udkast til et svar. I egen virksomhed gav det **over 40 % "
           "produktivitetsløft** dokumenteret, fordi viden blev søgbar i stedet for at sidde i hovedet på den, "
           "der havde prøvet det før.", after=80)

    m.para("Jeg bor i Måløv i dag, og Brønderslev er ikke et pendlerjob for en arbejdende leder, der selv skal "
           "gå i fejlfinding om morgenen. Jeg er derfor indstillet på at **flytte til Vendsyssel** for den "
           "rigtige stilling, og jeg kan starte efter aftale. Jeg vil gerne høre, hvilke produktgrupper der i "
           "dag giver flest sager, og hvordan reklamationsdata finder vej tilbage til leverandørerne — det er "
           "der, jeg ville begynde.", after=70)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Elautoriseret maskinmester (LV/MV/HV) med 20+ års erfaring fra **teknisk service, fejlfinding og "
           "drift** — uddannet elektromekaniker og med B.Tech i teknologiledelse og maskinteknik. Har ledet "
           "**12 teknikere** i et maskinværksted, **14 medarbejdere** med 11 samtidige projekter og driver i "
           "dag egen virksomhed med **5 elektrikere og 3 lærlinge**, fuldt P&L og **serviceaftaler** med "
           "aftalte **svartider**. Stærk på **el-diagrammer, elektriske styringer, SRO/SCADA og "
           "ventilation**, og på at omsætte **reklamationsdata** til kvalitetsforbedringer. Bygger egne "
           "værktøjer i **Python og Claude** med **over 40 % produktivitetsløft**.", after=80)

    m.section("TEKNISK SERVICE, FEJLFINDING OG LEDELSE")
    for label, body in [
        ("Teknisk fejlfinding og el-dokumentation",
         "Fejlfinding på koblingsanlæg, transformere, motorer, frekvensomformere, tavler og styringer; "
         "el-diagrammer læst og målt efter, og fejlen forklaret i et sprog kunden kan bruge."),
        ("Reklamationer, garanti og leverandører",
         "Garanti- og reklamationssager på egne leverancer og på materialer fra leverandører; årsag "
         "registreret med produkt, serienummer og montageforhold, og opfølgning samlet i en sag pr. "
         "produktnummer i stedet for enkeltsager."),
        ("Ledelse af et mindre teknisk team",
         "5 elektrikere og 3 lærlinge i egen virksomhed, 12 teknikere i ARJ og 14 medarbejdere i Ventek-Air — "
         "tydelige ansvarsområder, faglig sparring i det daglige og oplæring, der gør den enkelte i stand til "
         "at løse sagen selv næste gang."),
        ("Struktur, svartider og sagsstyring",
         "Dagligt tavlemøde, kapacitets- og flaskehalsanalyse og omprioritering samme dag; aftalte svartider "
         "og KPI fulgt på svartid, genbesøg og returprocent — målt, ikke fortalt."),
        ("Kunder, forhandlere og servicepartnere",
         "Support før, under og efter salg fra egen virksomhed og fra Ventek-Air; koordinering med montører, "
         "eksterne servicepartnere og leverandører, så kunden havde ét sted at ringe til."),
        ("Digitalisering, automatisering og AI",
         "Egne værktøjer bygget i Python og Claude Code til kalkulation, tjeklister, KPI og sagsflow; AI "
         "brugt til opsummering og udkast, så skriftligt arbejde ikke står i vejen for fejlfindingen."),
    ]:
        m.bullet(label, body, after=25)

    m.section("ERHVERVSERFARING")
    jobs = [
        ("Ejer / teknisk direktør",
         "ELOHVAC ApS · København · maj 2023–nu",
         "5 elektrikere og 3 lærlinge · fuldt P&L · el-autorisation · service- og entrepriseydelser",
         [("Service, sager og økonomi",
           "Serviceaftaler med aftalte svartider, prissætning og efterkalkulation; garanti- og "
           "reklamationssager håndteret til årsagen var skrevet ned; egne værktøjer med over 40 % "
           "produktivitetsløft.")]),
        ("Senior idriftsættelsesingeniør / projektleder, elsystem",
         "Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024",
         "37 parallelle kapitalprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA",
         [("Krav, afvigelser og leverandører",
           "Kravsspecifikation, afvigelser og ændringssager fulgt til lukning; FAT/SAT og IQ/OQ/PQ med "
           "dokumenteret accept — nul kritiske fund ved aflevering.")]),
        ("Projekt- og værkstedsleder",
         "Ventek-Air · København · jan. 2022–nov. 2022",
         "14 medarbejdere · 11 samtidige anlægsprojekter · ventilation, luftmængder og idriftsættelse",
         [("Ventilation, montører og fremdrift",
           "Dagligt tavlemøde, kapacitets- og flaskehalsanalyse og omprioritering samme dag; montører og "
           "eksterne parter koordineret, så opgaven blev afsluttet og ikke efterladt halvt.")]),
        ("Drifts- og vedligeholdelsesleder",
         "Lynetten under Biofos · København · aug. 2017–jan. 2022",
         "Kritisk anlæg i 24/7-drift · SRO/SCADA · pumper, blæsere, ventilation, transformere, koblingsanlæg",
         [("Drift, fejlfinding og beredskab",
           "Fejlfinding på el-tekniske anlæg og styringer under driftspres; vagtordning og beredskab planlagt "
           "og øvet; energiledelse med over 40 % lavere forbrug.")]),
        ("Elektromekaniker / produktionsteamleder",
         "ARJ Engineering · Teheran · dec. 2003–mar. 2010",
         "12 mekanikere og teknikere · maskinværksted · industrielt udstyr",
         [("Reparation, fejlfinding og oplæring",
           "Reparation, klargøring og fejlfinding på industrielt udstyr med årsagsanalyse; vagtplanlægning, "
           "oplæring og opfølgning for 12 teknikere.")]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section("UDDANNELSE OG AUTORISATION")
    m.edu("B.Tech, teknologiledelse og maskinteknik",
          "Maskinmesterskolen København · 2017–2022 · gennemsnit 7,6/12")
    m.edu("Elautoriseret maskinmester (LV/MV/HV)", "Sikkerhedsstyrelsen · maj 2023")
    m.edu("El- og maskinteknisk konstruktion, elteknik",
          "Tehran Technical University · 2000–2003 · EQF 6")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("Dansk: modersmål, sikkert både mundtligt og skriftligt · Engelsk: professionelt, også teknisk · "
           "Persisk: modersmål · **Kørekort B og egen bil** · Måløv i dag, **indstillet på at flytte til "
           "Vendsyssel** · Køle- og ventilationsteknik og STCW, Mercantec og Søfartsstyrelsen 2021 · "
           "Opstart efter aftale · Referencer på forespørgsel.", after=70)

    m.models_table("DE FØRSTE 90 DAGE — SAGERNE, SVARTIDERNE OG TEAMET",
                   ("Periode", "Hvad der sker, og hvordan det måles"), [
        ("Uge 1–2",
         "Sid ned med de tre medarbejdere og gennemgå de åbne sager; træk de sidste tolv måneders "
         "reklamationer ud pr. produktgruppe og se, hvilke fejl der kommer igen; gennemgå svartider, "
         "reservedelsflow og de servicepartnere og leverandører, der bruges mest."),
        ("Dag 30",
         "Billede af sagsmængden og de fem fejl, der koster mest — med produktnummer, årsag og hvad der "
         "allerede er gjort; prioritetsregler og svartider aftalt med teamet, og en ejer på hver sagstype."),
        ("Dag 60",
         "Sagsflowet indført fra modtagelse til lukning med årsag registreret; fejlfindingsnoter gjort "
         "søgbare, så den næste ikke starter forfra; fast kadence med de største leverandører om produktfejl; "
         "AI-assisteret opsummering af sager taget i brug."),
        ("Dag 90",
         "Svartider, genbesøg og returprocent målt og faldende; første kvalitetsrapport sendt til en "
         "leverandør med data i stedet for fornemmelser; og en plan for, hvad teamet skal kunne om et år.")])

    m.section("EN FEJL, DER KOMMER IGEN, ER EN KVALITETSFELJ")
    m.para("Tre ens sager på samme produktnummer er ikke tre kundesager — det er én fejl, der er kommet igen, "
           "og den bliver dyrere for hver gang, fordi den koster en medarbejder, en reservedel, en retur og "
           "lidt af kundens tillid. Derfor skal årsagen registreres, når sagen lukkes, og der skal være en "
           "fast vej fra serviceafdelingen tilbage til den internationale leverandør: hvor mange, hvilke "
           "serienumre, hvilke montageforhold. Det er den rapport, der flytter noget hos en producent.", after=80)

    m.section("DEN DER RINGER, SKAL TALE MED EN DER HAR PRØVET DET")
    m.para("En forhandler, der ringer med en vare, der ikke virker, har ikke brug for en sagsbehandler — han "
           "har brug for en, der kan spørge ind til det rigtige og sige, hvad der skal prøves først. Den "
           "samtale går hurtigere, når den, der tager telefonen, selv har stået med en tavle, en emhætte eller "
           "en styring. Jeg har siddet på begge sider, og jeg ved, at et godt svar ofte handler om at stille "
           "tre rigtige spørgsmål frem for at sende en ny vare. Det er den forskel, der bliver til en "
           "**kundeoplevelse**, som forhandleren husker og bruger næste gang.", after=80)

    m.section("RESERVEDELE OG SERVICE PARTNERE ER EN DEL AF SVARTIDEN")
    m.para("En sag er ikke løst, når fejlen er fundet — den er løst, når den rigtige del er på vej, og når den "
           "servicepartner, der skal montere den, har fået det, han skal bruge. Derfor hører reservedelslager, "
           "leveringstider og partner-koordinering med til sagsstyringen og ikke til et andet regnskab. Jeg "
           "har styret materialeflow og eksterne montører i egen virksomhed og i døgndrift, og jeg ved hvor "
           "svartiden i praksis bliver tabt: mellem to systemer, hvor ingen har ejerskab.", after=80)

    m.section("AI SKAL FJERNE ARBEJDE, IKKE TILFØJE ET SYSTEM")
    m.para("Digitalisering bliver kun en forbedring, hvis den fjerner en opgave, nogen sidder med i dag. Jeg "
           "starter altid med at se, hvor tiden går: gentagne svar på de samme spørgsmål, manuel indtastning "
           "af de samme data, sagsnotater, der skal skrives to gange. Derfra bygger jeg det mindste, der løser "
           "det — i Python og med Claude — og måler, om svartiden eller antallet af genbesøg faktisk faldt. "
           "Teknologien er ikke målet; det er de minutter, den giver tilbage til fejlfindingen.", after=80)

    m.section("JEG HAR VÆRET MONTØREN, DER RINGEDE TIL EN LEVERANDØR")
    m.para("Jeg har stået på en adresse med en vare, der ikke virkede, og ventet på et svar, der kom for sent. "
           "Det er den oplevelse, jeg vil have, at EICOs kunder og forhandlere ikke har. Den tekniske vej til "
           "det er kort: en der tager telefonen, som selv kan faget, og som kan sige, hvad der skal prøves "
           "først — og en sag, der bliver lukket med en årsag, så den samme telefon ikke ringer igen om en "
           "måned.", after=80)

    m.section("ET LILLE TEAM KRÆVER EN LEDER, DER ER DER")
    m.para("Tre medarbejdere betyder ikke mindre ledelse, men tættere ledelse. Der er ikke plads til et "
           "mellemled, og der er ikke nogen, der kan tage en dårlig dag for én. Det passer til den måde, jeg "
           "altid har arbejdet på: tæt på opgaverne, med ansvaret placeret tydeligt, og med en "
           "opfølgning hver uge på de tal, der viser, om det går den rigtige vej.", after=80)

    m.page_break()

    m.models_table("DET EFTERSPØRGER OPSLAGET — DET HAR JEG", ("Krav i opslaget", "Dokumentation"), [
        ("Lede og udvikle afdelingens tre medarbejdere med fokus på trivsel og faglig sparring",
         "5 elektrikere og 3 lærlinge i egen virksomhed, 12 teknikere i ARJ og 14 medarbejdere i Ventek-Air; "
         "tydelige ansvarsområder, daglig sparring og oplæring, så den enkelte kan løse sagen selv næste gang."),
        ("Sikre struktur, prioritering og fremdrift i tekniske henvendelser, serviceopgaver og reklamationssager",
         "Dagligt tavlemøde, kapacitets- og flaskehalsanalyse og omprioritering samme dag; sagsflow med "
         "modtagelse, triage, svar, årsag og lukning — indført i egen virksomhed og i døgndrift."),
        ("Yde teknisk rådgivning og selvstændigt diagnosticere komplekse problemstillinger inden for hvidevarer, ventilation og elektriske produkter",
         "Elautoriseret maskinmester (LV/MV/HV) og uddannet elektromekaniker; fejlfinding på elektriske "
         "produkter, styringer og tavler; ventilation fra kanal til styring med luftmængder, tryk og "
         "idriftsættelse i Ventek-Air."),
        ("Sikre professionel support til kunder, forhandlere, montører og servicepartnere før, under og efter salg",
         "Support fra egen virksomhed og fra Ventek-Air til kunder, montører og samarbejdspartnere; selv "
         "siddet på håndværkerens side af den samme telefon og ved, hvilke oplysninger der skal til, før "
         "svaret kan bruges."),
        ("Varetage den tekniske dialog med internationale leverandører og følge op på produktfejl og kvalitetsproblemer",
         "Garanti- og reklamationssager på materialer fra leverandører med årsag, serienummer og "
         "montageforhold; leverandørdialog og afvigelser fulgt til lukning i egen virksomhed og i Novo "
         "Nordisk."),
        ("Identificere tilbagevendende produktfejl og omsætte reklamationsdata til konkrete kvalitetsforbedringer",
         "Sager samlet pr. produktnummer i stedet for enkeltvis; årsag registreret ved lukning, og de "
         "tilbagevendende fejl brugt som grundlag for den tekniske dialog om produkt og montage."),
        ("Optimere serviceprocesser og sagsstyring med kortere svartider og færre unødige omkostninger",
         "Serviceaftaler med aftalte svartider, prissætning og efterkalkulation; svartid, genbesøg og "
         "returprocent fulgt som KPI — og over 40 % produktivitetsløft gennem egne værktøjer."),
        ("Bidrage til digitalisering og automatisering, herunder anvendelse af AI i service- og reklamationsprocesserne",
         "Egne værktøjer bygget i Python og Claude Code til kalkulation, tjeklister, KPI og sagsflow; AI "
         "brugt til opsummering af sager og første udkast til svar — bygget og taget i brug, ikke planlagt."),
        ("Solid teknisk baggrund, gerne som elektriker eller tilsvarende el-teknisk erfaring",
         "Uddannet elektromekaniker og elautoriseret maskinmester (LV/MV/HV); 20+ år med el-tekniske "
         "produkter, anlæg og styringer samt ventilation fra montage til idriftsættelse."),
        ("Praktisk erfaring med teknisk fejlfinding, elektriske styringer og el-diagrammer",
         "Fejlfinding på koblingsanlæg, transformere, motorer, frekvensomformere og tavler; el-diagrammer "
         "læst og målt efter; SRO/SCADA i 24/7-drift med alarmer, regulering og fejlfinding."),
        ("Erfaring med at koordinere og prioritere opgaver i en teknisk servicefunktion",
         "11 samtidige projekter i Ventek-Air og 5–14 medarbejdere med daglig prioritering; serviceopgaver og "
         "udrykninger koordineret i egen virksomhed med aftalte responstider."),
        ("Erfaring med at lede medarbejdere i et mindre team",
         "Team på 3 lærlinge og 5 elektrikere i dag, 12 teknikere i ARJ og 14 medarbejdere i Ventek-Air — "
         "ledelse i arbejdstøjet med oplæring, samtaler og de svære sager taget direkte."),
        ("Operationel lederrolle, hvor man både tager ansvar for driften og selv bidrager aktivt",
         "Arbejdende leder i egen virksomhed siden 2023 og på gulvet i døgndrift på Lynetten: selv i "
         "fejlfindingen, selv i kundesagerne og med ansvaret for drift, økonomi og personale samtidig."),
        ("Erfaring med reklamationshåndtering og teknisk leverandørsamarbejde er en fordel",
         "Garanti- og reklamationssager håndteret til årsagen var skrevet ned — mod kunder, montører og "
         "leverandører — med dokumentation nok til at føre en sag og til at få en kreditnota igennem."),
        ("Struktureret, ansvarsbevidst og handlekraftig med rolig og løsningsorienteret tilgang",
         "Struktur bygget som system: sagsflow, prioritetsregler og KPI i egen virksomhed; fejlfinding under "
         "driftspres i 24/7-drift, hvor beslutningen skulle tages, før kunden mærkede den."),
        ("Tydelig og nærværende leder, der skaber tillid gennem faglig indsigt og klar kommunikation",
         "Fagligt nærvær som leder: selv i fejlfindingen, selv i de svære kundesager; oplæring og sparring i "
         "det daglige for 5–14 medarbejdere og daglig tavlemødekadence."),
        ("Samarbejdsorienteret, serviceminded og motiveret af at udvikle medarbejdere og arbejdsgange",
         "Tværfagligt samarbejde med montører, servicepartnere, leverandører og kunder; medarbejdere udviklet "
         "gennem oplæring og kompetenceplaner, og arbejdsgange ændret sammen med dem, der skulle bruge dem."),
        ("Interesse for nye teknologier og muligheder i digitalisering og automatisering",
         "Python og Claude Code i daglig brug til værktøjer, rapportering og AI-assisteret sagsbehandling; "
         "teknologivalg begrundet i hvilken opgave, den fjerner — ikke i hvad den hedder."),
    ], widths=(3200, 7146))

    return m.save(path, title="Teknisk chef — EICO, Brønderslev",
                  subject="Teknisk service, fejlfinding, reklamationshåndtering og ledelse af teknisk team",
                  keywords="teknisk chef, teknisk service, fejlfinding, reklamation, hvidevarer, ventilation, "
                           "elautoriseret maskinmester, svartid, kvalitetsforbedring, digitalisering, ai, "
                           "brønderslev, eico")


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_EICO_TekniskChef.docx')))
