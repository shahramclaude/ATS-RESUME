# -*- coding: utf-8 -*-
"""Bravida — EL-serviceleder til Kalundborg.

Dansk leverance: ansøgning side 1 (opgave-først), CV side 2–3, 90 dage + kravmatrix side 4.
Policy: master/README.md — jobbet først, kandidaten kun som bevis; ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = "EL-serviceleder · Serviceforretning, kalkulation og elteknisk ledelse"
CONTACT = "+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv"


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("7. november 2026")
    m.meta("Bravida Danmark A/S · EL-service · Kalundborg")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: EL-serviceleder til Kalundborg", bold=True, color='1A1A1A')
    m.para("Til Martin Nielsen, tlf. +45 2525 1936", after=70)

    # ---------------------------------------------------------------- side 1
    m.para("En EL-serviceforretning bliver ikke bygget af en ordrebog. Den bliver bygget af de kunder, "
           "der ringer igen — fordi den, der tog telefonen, vidste hvad han talte om, fordi opgaven var "
           "kalkuleret så den kunne betales, og fordi teknikeren stod på adressen på det tidspunkt, der var "
           "aftalt. Bravida vil bygge den forretning i Kalundborg, og det er den opgave, jeg søger.", after=80)

    m.para("**Forretningen skal bygges på kunder, der bliver — ikke på ordrer, der kommer.** Det er den "
           "rækkefølge, jeg har arbejdet efter: først finde ud af, hvilke kunder i oplandet der har et "
           "vedvarende behov, og hvilke opgavetyper de har; derefter sætte en **serviceaftale** op med en "
           "responstid, der kan holdes, og en pris, der kan betales; og til sidst sikre, at der er "
           "**teknikere nok, med den rigtige autorisation**, til at løse opgaven den dag, kunden ringer. "
           "Kommer den rækkefølge i omvendt orden, bliver service en række udrykninger, der ser travle ud "
           "i kalenderen og ikke gør noget ved indtjeningen.", after=80)

    m.para("**Jeg har bygget den slags forretning før — fra første kunde.** I **ELOHVAC ApS** har jeg siden "
           "2023 opbygget en el-teknisk forretning med **5 elektrikere og 3 lærlinge**, fuldt P&L, "
           "**kalkulation og tilbudsberegning**, serviceaftaler med aftalte responstider, prissætning, "
           "materialestyring og betalingsopfølgning. Kundekredsen blev bygget ved at løse de små opgaver "
           "ordentligt og komme igen, og de egne digitale værktøjer til kalkulation, tjeklister og KPI gav "
           "**over 40 % produktivitetsløft** dokumenteret. Det, Bravida skal bygge i Kalundborg, er den "
           "samme opgave — med et stærkere fagligt bagland og flere fag at trække på.", after=80)

    m.para("**Kalkulation er den beslutning, serviceforretningen lever af.** Et tilbud er ikke en pris på "
           "en opgave; det er en aftale om, hvor mange timer der er til rådighed, hvor meget materiale der "
           "skal bruges, hvor svær adgangen er, og hvem der betaler, hvis noget viser sig at være "
           "anderledes. Jeg har regnet tilbud på service, reparation og entreprise, fulgt dem op med "
           "**efterkalkulation** pr. opgave og fulgt **dækningsgraden** pr. kunde og pr. opgavetype — så "
           "næste tilbud blev bedre end det forrige. I Novo Nordisk styrede jeg samtidig **37 "
           "kapitalprojekter** på 2–10 mio. kr. med kravspecifikation, kontrakt, fremdrift, økonomi og "
           "månedlig rapportering — og **nul kritiske fund** ved aflevering.", after=80)

    m.para("**Kalundborg kender jeg indefra.** Fra 2022 til 2024 arbejdede jeg i Novo Nordisk med base i "
           "**Kalundborg**: store produktionsanlæg, hvor adgang, tilladelser, arbejdstilladelser og "
           "sikkerhedsinstrukser er en del af opgaven, og hvor arbejdet foregår på anlæg, der kører "
           "imens. Jeg ved, hvad et nedbrud koster på den slags anlæg, og hvad der skal være styr på, før "
           "en medarbejder overhovedet kommer ind ad porten. Det er den viden, en lokal "
           "EL-serviceforretning skal sælge på — ikke som et tillæg, men som det, der gør, at kunden tør "
           "ringe.", after=80)

    m.para("**Elteknisk tyngde betyder, at jeg kan sige ja, nej og det gør vi sådan.** Jeg er "
           "**elautoriseret maskinmester (LV/MV/HV)** og bærer autorisationen i egen virksomhed. Jeg har "
           "fejlfundet og idriftsat på **transformere, koblingsanlæg, tavler, motorer, pumper og "
           "frekvensomformere**, drevet **SRO/SCADA** i døgndrift på Lynetten og gennemført udskiftning og "
           "idriftsættelse med **FAT/SAT og IQ/OQ/PQ** i et GMP-miljø. Det gør mig i stand til at gå i "
           "detaljen med teknikerne på tavlen, sparre med kunden om løsningen og træffe beslutningen, når "
           "to løsninger er lige dyre og ikke lige gode.", after=80)

    m.para("**Folkene er halvdelen af forretningen.** Jeg har ledet **5 elektrikere og 3 lærlinge** i egen "
           "virksomhed, **14 medarbejdere** i Ventek-Air med 11 samtidige projekter og **12 teknikere** i "
           "ARJ. Planlægning og **bemanding** er en daglig beslutning: hvem har kompetencen, hvem har "
           "kapaciteten, og hvem skal udvikles til at kunne mere om et år. **Arbejdsmiljø** og "
           "**sikkerhed** har jeg haft ansvaret for i døgndrift — sikkerhedsrunder, APV, instrukser og "
           "opfølgning på nærvedhændelser. Bravidas tre ord rammer det, jeg selv arbejder efter: "
           "**engagement, ansvarlighed og enkelhed** — og enkelhed er også en driftsbeslutning, for en "
           "arbejdsgang, der skal forklares to gange, bliver ikke fulgt.", after=80)

    m.para("**Ét Bravida er det, der gør en lokal forretning større end sin egen bemanding.** En "
           "EL-serviceopgave i Kalundborg er sjældent kun el: den hænger sammen med ventilation, VVS, "
           "sprinkler eller automation, og kunden spørger efter ét sted at ringe til. Jeg har selv siddet "
           "med den koordinering i Ventek-Air og i Novo Nordisk, hvor grænsefladerne mellem fag var der, "
           "hvor fejlene opstod — og hvor en navngiven ansvarlig var forskellen mellem en aflevering og en "
           "sag. Jeg vil bruge de øvrige serviceledere, projektledere og specialister aktivt, fordi det "
           "er den hurtigste vej til at kunne løse mere, end afdelingen selv kan.", after=80)

    m.para("Jeg har base i **Måløv**, **kørekort B og egen bil**, og vil være på plads i Kalundborg hver "
           "dag — pendlingen kender jeg fra Novo Nordisk-årene, og den er ikke et problem, den er et valg "
           "om, hvor forretningen skal bygges. Jeg vil gerne høre, hvilke kunder og opgavetyper I vil "
           "bygge forretningen på først, og hvordan I ser bemandingen i Kalundborg om to år.", after=70)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Elautoriseret maskinmester (LV/MV/HV) med 20+ års erfaring fra **EL-branchen** — service, "
           "entreprise, drift og projekter. Byggede og driver **ELOHVAC ApS** med **5 elektrikere og "
           "3 lærlinge**, fuldt P&L, **kalkulation, tilbudsberegning og økonomisk opfølgning** og "
           "**serviceaftaler** med aftalte responstider; egne digitale værktøjer gav **over 40 % "
           "produktivitetsløft**. Fem år som drifts- og vedligeholdelsesleder på **Lynetten under Biofos** "
           "med **SRO/SCADA** og **el-tekniske anlæg** i 24/7-drift og **over 40 % lavere energiforbrug**. "
           "To år som projektleder på **37 kapitalprojekter** i Novo Nordisk med base i **Kalundborg** — "
           "**nul kritiske fund** ved aflevering.", after=80)

    m.section("EL-SERVICE, KALKULATION OG DRIFT")
    for label, body in [
        ("Serviceforretning og serviceaftaler",
         "Opbyggede kundekredsen i egen virksomhed fra første kunde: serviceaftaler med aftalte "
         "responstider, faste kunder og tilbagevendende opgaver — en ordrebog, der kunne planlægges, i "
         "stedet for en række tilfældige udrykninger."),
        ("Kalkulation og tilbudsberegning",
         "Tilbud beregnet på timer, materialer, adgang, dokumentation og risiko og prissat efter "
         "opgavetype; efterkalkulation på hver opgave og dækningsgrad fulgt pr. kunde, så næste tilbud "
         "blev mere præcist end det forrige."),
        ("Økonomiopfølgning og lønsomhed",
         "Fuldt P&L med budget, månedsafslutning, fakturering og betalingsopfølgning; timeforbrug mod "
         "kalkule og materialeforbrug mod tilbud, og afvigelser taget i tide — før de blev til tab."),
        ("Elteknisk tyngde og autorisation",
         "Elautoriseret (LV/MV/HV) med ansvaret for, at arbejdet udføres af kompetente folk efter "
         "gældende krav; transformere, koblingsanlæg, tavler, motorer og pumper i døgndrift; "
         "idriftsættelse og fejlfinding med FAT/SAT og IQ/OQ/PQ."),
        ("Planlægning, bemanding og udvikling",
         "Dagligt tavlemøde, kapacitets- og flaskehalsanalyse og omprioritering samme dag; oplæring af "
         "lærlinge og svende, kompetenceplaner og sikker adfærd på pladsen for 5–14 medarbejdere."),
        ("Kunder, tillid og tværfagligt samarbejde",
         "Kundedialog fra første opkald til afsluttet sag og koordinering med ventilation, VVS og "
         "automation, så kunden havde én aftale og én ansvarlig."),
    ]:
        m.bullet(label, body, after=25)

    m.section("ERHVERVSERFARING")
    jobs = [
        ("Ejer / teknisk direktør",
         "ELOHVAC ApS · København · maj 2023–nu",
         "5 elektrikere og 3 lærlinge · fuldt P&L · el-autorisation · el-tekniske service- og entrepriseydelser",
         [("Forretning, kalkulation og service",
           "Kunder og serviceaftaler opbygget fra første kunde; tilbudsberegning, prissætning og "
           "efterkalkulation pr. opgave; egne digitale værktøjer til kalkulation, tjeklister og KPI med "
           "over 40 % produktivitetsløft.")]),
        ("Senior idriftsættelsesingeniør / projektleder, elsystem",
         "Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024",
         "37 parallelle kapitalprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA",
         [("Projekter, specialister og interessenter",
           "Kravsspecifikation, risikovurdering, FAT/SAT og IQ/OQ/PQ; fremdrift, økonomi og risiko "
           "rapporteret månedligt til ledelse og bygherre — nul kritiske fund ved aflevering.")]),
        ("Projekt- og værkstedsleder",
         "Ventek-Air · København · jan. 2022–nov. 2022",
         "14 medarbejdere · 11 samtidige anlægsprojekter · 2–10 mio. kr. pr. opgave",
         [("Kapacitet, prioritering og leverance",
           "Dagligt tavlemøde, kapacitets- og flaskehalsanalyse og omprioritering samme dag, når en "
           "maskine eller et menneske faldt væk; standardiserede arbejdsgange og afleveringspakker styret "
           "til deadline.")]),
        ("Drifts- og vedligeholdelsesleder",
         "Lynetten under Biofos · København · aug. 2017–jan. 2022",
         "Kritisk spildevandsanlæg i 24/7-drift · SRO/SCADA · pumper, blæsere, transformere, koblingsanlæg",
         [("Drift, el-tekniske anlæg og beredskab",
           "Vagtordning og beredskab planlagt og øvet; fejlfinding på el-tekniske anlæg og styringer; "
           "5S og standard work på værksted og lager; energiledelse med over 40 % lavere forbrug.")]),
        ("Elektromekaniker / produktionsteamleder",
         "ARJ Engineering · Teheran · dec. 2003–mar. 2010",
         "12 mekanikere og teknikere · maskinværksted · industrielt udstyr",
         [("Teknisk drift og fejlfinding",
           "Reparation, klargøring og fejlfinding på industrielt udstyr; vagtplanlægning, oplæring og "
           "opfølgning for 12 teknikere.")]),
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
           "Persisk: modersmål · **Kørekort B og egen bil** · Måløv, med daglig tilstedeværelse i "
           "**Kalundborg** · Køle- og ventilationsteknik og STCW, Mercantec og Søfartsstyrelsen 2021 · "
           "Referencer på forespørgsel.", after=70)

    m.models_table("DE FØRSTE 90 DAGE — KUNDERNE, KALKULEN OG FOLKENE",
                   ("Periode", "Hvad der sker, og hvordan det måles"), [
        ("Uge 1–2",
         "Mød medarbejderne, de øvrige serviceledere i regionen og de vigtigste kunder; gennemgå de åbne "
         "sager, serviceaftalerne, timepriserne og de seneste tolv måneders tilbud og efterkalkulationer."),
        ("Dag 30",
         "Billede af forretningen pr. kunde og opgavetype — dækningsgrad, responstid, antal udrykninger; de "
         "fem kunder, hvor der er mest at hente, udpeget med en konkret plan; prisstruktur og tilbudsproces "
         "aftalt med ledelsen."),
        ("Dag 60",
         "Kalkulations- og tilbudsskabelon indført, så to personer regner samme opgave og får samme pris; "
         "bemandingsplan for de næste seks måneder med svende og lærlinge; sikkerhedsinstrukser og "
         "arbejdsmiljø gennemgået med medarbejderne."),
        ("Dag 90",
         "De første nye serviceaftaler tegnet og de første servicekunder løftet til flere opgavetyper; "
         "økonomi og kundetilfredshed rapporteret i fast rytme; og en plan for, hvem der skal ansættes, og "
         "hvornår.")])

    m.section("SERVICE SÆLGES MELLEM OPGAVERNE, IKKE VED TILBUDSRUNDEN")
    m.para("En servicekunde bliver ikke skabt i et tilbud. Den bliver skabt den dag, teknikeren kommer til "
           "tiden, finder fejlen, forklarer den i et sprog kunden forstår, og efterlader en sag, der er "
           "lukket. Næste opgave kommer, fordi den oplevelse gentog sig. Derfor er servicelederens "
           "vigtigste arbejde at gøre den adfærd til en vane: aftalte responstider, der bliver holdt, "
           "rapporter der kan læses, og en opfølgning på hver større sag, inden kunden selv ringer.", after=80)

    m.section("ET TILBUD ER EN KONTRAKT, DER SKAL KUNNE HOLDES")
    m.para("Kalkulation handler ikke om at ramme den laveste pris — det handler om at ramme den rigtige. "
           "Adgang, arbejdshøjde, dokumentationskrav, responstid og hvad der sker, hvis anlægget ikke kan "
           "slukkes, skal stå i tilbuddet, for det er præcis de punkter, der bliver en diskussion senere. "
           "Jeg har prissat service, reparation og entreprise og fulgt hver opgave op bagefter, og jeg ved, "
           "at den tilbudte pris kun er troværdig, hvis efterkalkulationen bliver lavet.", after=80)

    m.section("KALUNDBORG KRÆVER FOLK, DER KAN GÅ IND PÅ ET ANLÆG")
    m.para("Store produktionsanlæg lukker ikke, fordi en håndværker har en aftale. Adgang, kurser, "
           "tilladelser, arbejdstilladelser og sikkerhedsinstrukser er en del af planlægningen, og en "
           "tekniker uden adgang er en tekniker uden omsætning. Jeg har arbejdet på den slags anlæg i "
           "Kalundborg, og jeg ved, at den tid, der bruges på at få formaliteterne på plads på forhånd, "
           "bliver tjent ind igen den dag, opgaven skal løses.", after=80)

    m.section("STRUKTUREN SKAL BYGGES, FØR DER ER TRAVLT")
    m.para("Det første år i en ny serviceforretning handler om at gøre de få ting ens hver gang: samme "
           "kalkulationsskabelon, samme prisliste, samme ordrebekræftelse, samme vej for materialer og "
           "samme faktureringsfrist. En forretning, der kun kan styres af den ene person, der har hovedet "
           "i den, er ikke en forretning endnu — den er et godt håndværk med en kalender. Det er den "
           "struktur, jeg vil bygge i Kalundborg, mens forretningen stadig er lille nok til, at det kan "
           "gøres uden at stoppe driften.", after=80)

    m.section("SIKKERHED OG ARBEJDSMILJØ ER EN DEL AF LØNSOMHEDEN")
    m.para("En ulykke koster mere end den opgave, den skete på — i penge, i tid og i tillid hos kunden og "
           "hos dem, der skal ud på den næste opgave. Jeg har haft arbejdsmiljøansvaret i døgndrift: "
           "sikkerhedsrunder, APV, instrukser, opfølgning på nærvedhændelser og oplæring af lærlinge, "
           "sådan at sikkerhed blev en del af planlægningen og ikke en seddel, der blev underskrevet "
           "bagefter. Det er samme disciplin, der skal gælde, når en serviceforretning i Kalundborg vokser "
           "hurtigt.", after=80)

    m.section("JEG HAR PRØVET AT STARTE FRA NUL — DET ER IKKE DET SAMME SOM AT DRIVE")
    m.para("Den første kunde, den første ansættelse, den første lærling, den første serviceaftale og den "
           "første måned, hvor regnestykket ikke gik op — det er den erfaring, Bravida får, og den kan ikke "
           "læses ud af et CV, den kan kun bruges. Jeg ved, hvad det koster at ansætte en mand mere, før "
           "ordrebogen bærer ham, og hvornår det er den rigtige beslutning alligevel. I Kalundborg er "
           "spørgsmålet ikke, om forretningen kan bygges, men i hvilken rækkefølge.", after=80)

    m.page_break()

    m.models_table("DET EFTERSPØRGER OPSLAGET — DET HAR JEG", ("Krav i opslaget", "Dokumentation"), [
        ("Bygge og udvikle EL-serviceforretningen i Kalundborg",
         "Opbyggede egen el-teknisk virksomhed fra første kunde til 5 elektrikere og 3 lærlinge med fuldt "
         "P&L, serviceaftaler, prisstruktur og kundekreds — og har arbejdet på de store anlæg i Kalundborg."),
        ("Udvikle eksisterende kunderelationer og identificere nye forretningsmuligheder",
         "Kundekreds udvidet ved at løse små opgaver ordentligt og vende tilbage; opgavetyper udvidet pr. "
         "kunde fra reparation til serviceaftale og entreprise, med dækningsgrad fulgt pr. kunde."),
        ("Beregne, udarbejde og følge op på tilbud og sikre et sundt økonomisk grundlag",
         "Tilbudsberegning på service, reparation og entreprise med timer, materialer, adgang og risiko; "
         "efterkalkulation pr. opgave og pris korrigeret, når kalkulen ikke holdt."),
        ("Lede og koordinere serviceopgaver og mindre EL-projekter fra første kundedialog til afslutning",
         "Serviceopgaver og mindre projekter ført fra første opkald til aflevering og fakturering — med "
         "kunden som den, der ringede tilbage næste gang."),
        ("Sikre den rette planlægning, bemanding, kvalitet og fremdrift på opgaverne",
         "Dagligt tavlemøde, kapacitets- og flaskehalsanalyse og omprioritering samme dag; bemanding "
         "planlagt efter kompetence og autorisation for 5–14 medarbejdere."),
        ("Være en stærk elteknisk sparringspartner for medarbejdere, kunder og kolleger",
         "Elautoriseret maskinmester (LV/MV/HV) med egen autorisation; fejlfinding og idriftsættelse på "
         "transformere, koblingsanlæg, tavler, motorer og styringer — sparring på tavlen, ikke kun i mødet."),
        ("Følge op på økonomi med fokus på kvalitet, kundetilfredshed og lønsomhed",
         "Fuldt P&L med budget, månedsafslutning, fakturering og betalingsopfølgning; time- og "
         "materialeforbrug målt mod kalkule, og afvigelser taget før de blev til tab."),
        ("Solid el-teknisk baggrund og mange års erfaring fra EL-branchen",
         "20+ år i EL-branchen fra elektromekaniker og produktionsteamleder til driftsleder, "
         "idriftsættelsesingeniør og ejer af egen el-teknisk virksomhed."),
        ("Erfaring med EL-service og gerne som serviceleder, projektleder eller tilsvarende",
         "Ejer og leder af serviceforretning siden 2023; projekt- og værkstedsleder for 14 medarbejdere og "
         "11 samtidige projekter; projektleder på 37 kapitalprojekter i Novo Nordisk."),
        ("Erfaring med kalkulation, tilbudsberegning og økonomisk opfølgning",
         "Kalkulation og tilbudsberegning som dagligt arbejde i egen virksomhed; efterkalkulation, "
         "dækningsgrad, budget og månedsafslutning; økonomi og fremdrift rapporteret månedligt i Novo Nordisk."),
        ("Stærk forretningsforståelse og kan se og udvikle muligheder hos kunderne",
         "Forretning bygget fra nul med egen prisstruktur og serviceaftaler; kunders behov omsat til "
         "opgavetyper og aftaler — og tilbud prissat efter, hvad opgaven kræver, ikke hvad den koster at vinde."),
        ("Faglig tyngde til at sparre om el-tekniske løsninger og træffe beslutninger",
         "Bærer elautorisationen og ansvaret for, at arbejdet udføres efter gældende krav; beslutninger "
         "truffet på tavlen og i kontrakten, også når sikkerhed og pris pegede hver sin vej."),
        ("Stærk i kommunikationen og god til at skabe tillidsfulde relationer",
         "Kundedialog på dansk fra første opkald til afsluttet sag, også når en opgave gik skævt; oplæring "
         "og samtaler med egne teknikere og lærlinge; samarbejde med andre fag i Ventek-Air og Novo Nordisk."),
        ("Motiveres af at bygge noget op, skabe struktur og drive udviklingen fremad",
         "Byggede en virksomhed op fra første kunde og satte struktur på kalkulation, ordrer, materialer og "
         "fakturering; egne værktøjer bygget i Python og Claude, før der var et system."),
        ("Uddannelse som eksempelvis elinstallatør eller maskinmester",
         "B.Tech i teknologiledelse og maskinteknik, gennemsnit 7,6/12, og elautoriseret maskinmester "
         "(LV/MV/HV), Sikkerhedsstyrelsen 2023."),
        ("Ledelse af teknikere, projekterfaring og fokus på udvikling",
         "5 elektrikere og 3 lærlinge i egen virksomhed, 14 medarbejdere i Ventek-Air og 12 teknikere i "
         "ARJ; lærlinge og svende udviklet gennem oplæring og kompetenceplaner."),
        ("Samarbejde på tværs af fag og regioner med sparring fra andre ledere og specialister",
         "Tværfaglig koordinering med ventilation, VVS og automation i Ventek-Air og i Novo Nordisk, hvor "
         "grænseflader mellem fag blev navngivet og aftalt, før de blev et problem."),
        ("Trivsel og sikkerhed i et godt arbejdsmiljø med engagement og ansvarlighed",
         "Arbejdsmiljøansvar i 24/7-drift med sikkerhedsrunder, APV og opfølgning på nærvedhændelser; "
         "sikker adfærd indarbejdet i den daglige planlægning sammen med medarbejderne."),
    ], widths=(3200, 7146))

    m.section("OM ET ÅR SKAL FORRETNINGEN SES PÅ TRE TAL")
    m.para("Dækningsgraden pr. opgave, responstiden på serviceaftalerne og hvor mange kunder der har fået "
           "mere end én opgave. De tre tal viser, om forretningen er bygget på kunder, der bliver, eller på "
           "travle uger. Jeg vil gerne måles på dem — og på at der om et år står en eller to i Kalundborg, "
           "der kan tage over, når jeg er et andet sted.", after=80)

    return m.save(path, title="EL-serviceleder — Bravida, Kalundborg",
                  subject="EL-service, serviceforretning, kalkulation, tilbudsberegning og elteknisk ledelse",
                  keywords="el-serviceleder, el-service, serviceforretning, kalkulation, tilbudsberegning, "
                           "kalundborg, bravida, elautoriseret maskinmester, økonomiopfølgning, "
                           "arbejdsmiljø, kunderelationer")


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Bravida_ELServicelederKalundborg.docx')))
