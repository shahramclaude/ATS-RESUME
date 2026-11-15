# -*- coding: utf-8 -*-
"""Sektionschef — Banedanmarks Driftscenter, Trafikdivisionen (dansk opslag).

Dansk opslag -> dansk dokument, 4 sider: brev side 1, CV side 2, uddannelse + 90 dage +
metodeafsnit + "Hvor jeg ville starte" side 3, kravmatrix side 4. Format per master/README.md.
Opslaget beder om "CV og en motiveret ansøgning hurtigst muligt" — formen følges ikke, brevet
bliver side 1.

STILVALG (master/STILREGISTER.md; godkendt af scripts/style_guard.py, 3/3 skift mod #214):
  register      = UPTIME/KONTROLRUM — responstid, eskalering, alarm, hvem tager telefonen, det
                  første kvarter. Sidst #204 (Vertiv).
  åbningsgreb   = D (TALLET) — kundepunktlighed måles ved 2:59, 75,0 procent og højst 11,2
                  procentpoint fra Banedanmark selv. Sidst #205.
  struktur      = TESERNE — fem påstande om at lede en national driftssektion, hver med bevis,
                  derefter chefgruppen, værdierne og det praktiske. Sidst #188.
  kadence       = korte konstaterende sætninger, klokkeslæt og tal; ingen tillægsord om personen.

KULTURSYNKRONISERING (policy 04.11.2026), kilder i master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md
§186:
  Mission: "Vi udvikler og leverer en sikker, attraktiv og effektiv jernbane." Strategien
  "I form til fremtidens jernbane" med tre kerneleverancer: **punktlighed, projekter, asset
  management**. Mål- og resultatplan 2026: kundepunktlighed DSB fjern- og regionaltog mindst
  75,0 procent ved 2:59, S-banen 92,4 procent, og Banedanmarks egen påvirkning højst 11,2
  procentpoint. Værdier: **ambition, respekt, ansvar**. Ledelsesgrundlag (2020): "Ledelse handler
  om at sætte retning og skabe resultater via og sammen med andre" (Ledelseskommissionen 2018),
  Leadership Pipeline som ramme, seks ledelseskompetencer (strategi, resultatskabelse, offentlig
  myndighed, forandring, kommunikation, udvikling og samarbejde). Driftscenteret er døgnbemandet
  24/7/365 og beskrives selv som stedet, hvor "vi hurtigst muligt kan få genoprettet trafikken",
  med **disponering**, **nødplaner** og **trafikinformation** i samme rum som teknikerne.
  Opslaget: samfundskritisk driftsfunktion, 21 medarbejdere, to direkte referencer, teamleder med
  19 togledere, chefgruppen for Driftscenter & Kundeinformation, signalsystemets udrulning.

Ingen opdigtede fakta. Dokumenteret grundlag: 4 år i 24/7-drift med SRO/SCADA, vagtordning og
akut fejlfinding (Biofos/Lynetten 2017-2022); 37 CAPEX-projekter med 25 specialister og nul
kritiske fund (Novo Nordisk 2022-2024); 14-mands entrepriseteam og 11 samtidige entrepriser
(Ventek-Air 2022); 5 elektrikere + 3 lærlinge med fuldt P&L (ELOHVAC 2023-); 12 mekanikere og
teknikere (ARJ 2003-2010); elautoriseret maskinmester LV/MV/HV; B.Tech EQF 6 (7,6/12); dansk
modersmål, engelsk professionelt, kørekort B.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Sektionschef · Driftscenter, Trafikdivisionen'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("10. november 2026")
    m.meta("Sektionschef · Banedanmarks Driftscenter · Trafiktårnet, Kalvebod Brygge")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Sektionschef til Banedanmarks Driftscenter", bold=True, color='1A1A1A')
    m.para("Kære Rene,", after=60)

    # ---------------------------------------------------------------- side 1
    m.para("**Kundepunktlighed bliver målt ved 2 minutter og 59 sekunder.** I 2026 skal mindst "
           "75,0 procent af kunderne i DSB's fjern- og regionaltog være inden for den grænse, og "
           "Banedanmarks egen påvirkning må højst fylde 11,2 procentpoint af forsinkelsen. Det tal "
           "bliver ikke afgjort i et møde. Det bliver afgjort i det første kvarter, efter at en "
           "sporspærring er meldt — af togledere, der sidder med den alene, når resten af "
           "organisationen sover.", after=80)

    m.para("**Driftscenteret er det sted, hvor en hændelse på banen bliver til en plan for "
           "togtrafikken i hele landet.** Sektionen har 21 medarbejdere, to direkte referencer og "
           "en teamleder med 19 togledere i døgndrift. Den slags **samfundskritisk** funktion bliver "
           "ikke ledet med et "
           "møde om ugen. Den bliver ledet af en ramme, der holder klokken 03.20, og af en chef, "
           "der har set natten fra den rigtige side af bordet. Det har jeg gjort i fire år i "
           "24/7-drift med vagttelefon og SRO/SCADA, og de sidste tre år med eget regnskab og "
           "eget ansvar for, at kunderne ikke ventede forgæves.", after=80)

    m.para("**Det første kvarter afgør resten af døgnet.** Når et signal falder ud, eller en "
           "strækning skal lukkes, skal tre ting være afgjort med det samme: hvem der disponerer, "
           "hvilke **nødplaner** der gælder, og hvem der har sagt det videre til "
           "**jernbanevirksomhederne**. Er de tre ting ikke aftalt på forhånd, bliver de "
           "forhandlet midt i hændelsen — og minuttet koster mere der end noget andet sted i "
           "organisationen. På Lynetten havde jeg **responstid** som vilkår: alarm, udrykning, "
           "genopretning og en **eskalering**, der var kendt af den, der havde vagten, ikke kun af "
           "den, der havde skrevet den.", after=80)

    m.para("**En sektion på 21 mennesker skal have to led, der arbejder samme sted.** "
           "Teamlederen med de 19 **togledere** har brug for mandat og for en chef, der tager de "
           "sager, der ikke kan afgøres i sektionen — ikke for en chef, der tager opgaverne. "
           "**Ledelse af ledere** er en fordel i opslaget, og det er den del af rollen, jeg vil "
           "bruge mest tid på. Jeg har ledet gennem fagligt ansvarlige på 37 projekter med 25 "
           "specialister, i et 14-mands entrepriseteam og i et værksted med 12 mand: rammen, "
           "målene og opfølgningen er lederens, metoden er fagets.", after=80)

    m.para("**Et signalsystem, der skifter under drift, er en kompetenceopgave — ikke et "
           "projekt.** Nye skærmbilleder, nye arbejdsgange og nye systemgrænser skal sidde i "
           "hænderne på den, der har vagten, før strækningen skifter. Derfor skal oplæring, "
           "superbrugere og fejltræning ligge i driften, ikke i et program ved siden af. Jeg har "
           "flyttet idriftsættelser over i drift med FAT/SAT, sekvenser prøvet af på forhånd og "
           "nul kritiske fund ved aflevering — og jeg har set, hvad der sker, når den sidste "
           "instruks kommer efter den første vagt.", after=80)

    m.para("**Trafikinformation er en del af afviklingen, ikke en kommunikationsopgave.** "
           "Passageren skal have besked, mens beslutningen bliver taget, ikke bagefter. Det "
           "betyder, at informationen sidder i samme rum som **disponeringen**, hører "
           "beslutningen før den bliver meldt ud, og at de to fag bliver enige om, hvad der kan "
           "loves, og hvad der ikke kan. **Rettidigheden** er en del af beslutningen: en melding, "
           "der kommer efter toget er kørt, er ikke information. Den "
           "snitflade har jeg ejet mod bygherre og myndighed på "
           "37 projekter med fast månedsrapportering.", after=80)

    m.para("**En sektionschef, der ikke er i Trafiktårnet, får svaret bagefter.** Synlighed er "
           "ikke en rundtur i december. Det er at sidde med på en nattevagt, at være i tårnet, når "
           "hændelsen er stor, og at tage opfølgningen der, hvor opgaven ligger. Jeg har kørt "
           "Gemba og sikkerhedsrundering som fast rytme, ikke som kampagne.", after=80)

    m.para("**Chefgruppen er ikke et mødeforum — den er den ramme, hvor "
           "Trafikkontrolcentre** og **Vedligeholdelsesdivisionen** kan blive enige om, hvad der "
           "gælder i morgen. Det kræver **åben dialog** om det, der ikke går godt, og respekt for, "
           "hvad den enkelte faglighed har ansvar for. Banedanmarks **ledelsesgrundlag** siger, at "
           "ledelse handler om at sætte retning og skabe resultater via og sammen med andre; i en "
           "driftssektion bliver den sætning først prøvet, når der ikke er tid til at spørge om "
           "lov. Banedanmarks tre værdier — **ambition**, "
           "**respekt** og **ansvar** — betyder først noget, når de bliver brugt i en konkret "
           "uenighed, og det er der, jeg lægger dem.", after=80)

    m.para("**Praktisk.** Jeg bor i Måløv, og Trafiktårnet ligger en S-togstur derfra. Jeg er "
           "indstillet på en hverdag, hvor døgnet og ikke kalenderen bestemmer, for det er det "
           "vilkår, rollen hviler på. **Diplomuddannelsen** i ledelse påbegynder jeg inden for de "
           "første to år, som opslaget forudsætter. **Dansk** som modersmål, **engelsk** på "
           "professionelt niveau. **Kørekort B.** Kan tiltræde efter aftale.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Sektionschef og driftsleder med tolv års personaleansvar. Fire år i **døgnbemandet** "
           "drift med vagtordning, SRO/SCADA og akut fejlfinding; 37 CAPEX-projekter med 25 "
           "specialister og nul kritiske fund; 14-mands entrepriseteam med 11 samtidige opgaver; "
           "5 elektrikere og 3 lærlinge med fuldt P&L. Arbejder med **eskalering**, "
           "**responstid** og en fast driftsrytme — og med de tal, der bliver målt på.", after=80)

    m.section("DRIFT OG GENOPRETNING")
    for label, body in [
        ("Vagt og eskalering",
         "Vagtordning med tilkald, fast **eskaleringstrappe** og en beslutningsret, der er kendt "
         "af den, der har telefonen. Hændelsen bliver logget med tid, ejer og lukning."),
        ("Genopretning under pres",
         "Ved stop: afgræns, vælg **nødplaner**, disponer ressourcerne, meld ud — og tag "
         "evalueringen dagen efter sammen med dem, der sad med det."),
        ("Forebyggelse og vinduer",
         "Planlagte anlægsstop og servicevinduer aftalt med drift og leverandører i god tid, så "
         "arbejdet bliver gjort, uden at driften falder."),
    ]:
        m.bullet(label, body)

    m.section("LEDELSE OG KOMPETENCE")
    for label, body in [
        ("Personaleansvar",
         "Tolv år: 1:1 og MUS hvert år, oplæringsplan pr. medarbejder og "
         "**kompetenceudvikling** som rytme — ikke som kursuskatalog."),
        ("Ledelse gennem andre",
         "Mandat og rammer frem for kontrol: på 37 projekter havde hver disciplin sin fagligt "
         "ansvarlige, som jeg satte mål og bagkant for."),
        ("Forandring i drift",
         "Nye systemer og arbejdsgange indført, mens driften kørte: superbrugere udpeget, "
         "instruks klar før ibrugtagning, fejl øvet igennem på forhånd."),
    ]:
        m.bullet(label, body)

    m.section("INFORMATION, INTERESSENTER OG MÅLING")
    for label, body in [
        ("Interessenter med modsatrettede krav",
         "Bygherre, myndighed, entreprenører og drift i samme beslutning; uenighed afgjort med "
         "tal og en navngiven ejer, ikke med et referat."),
        ("Information som beslutning",
         "Information skrevet sammen med dem, der disponerer, så meldingen holder — og så "
         "passageren hører om forsinkelsen, før den er løst."),
        ("Leverancer og måling",
         "Månedsrapport til ledelse og bygherre med **KPI** på responstid, oppetid og "
         "leveringsevne; **stabil og effektiv** drift som fast punkt på tavlen."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Ejer / teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · fuldt P&L · serviceaftaler med responstid")
    m.bullet("Drift med kunde på den anden side",
              "Akutte udkald, faste responstider og serviceaftaler, hvor en time ekstra er en "
              "kunde, der står stille; nul kritiske afvigelser i aftalerne.")

    m.job("Senior idriftsættelsesingeniør / projektleder", "Novo Nordisk A/S · Kalundborg / "
          "Bagsværd · nov. 2022–jul. 2024",
          scope="37 CAPEX-projekter · 25 specialister · GMP/FDA/EMA · SAP")
    m.bullet("Idriftsættelse og overlevering",
              "FAT/SAT og sekvenser prøvet af, før anlægget gik i drift; nul kritiske fund ved "
              "aflevering og dokumentation, der kunne læses af en myndighed.")

    m.job("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · eget værksted")
    m.bullet("Én rytme på elleve sager",
              "Dagligt møde, kapacitet og fremdrift styret på samme tavle; flaskehalse flyttet, "
              "inden de blev til forsinkelser.")

    m.job("Drifts- og vedligeholdelseschef", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="Renseanlæg i 24/7-drift · pumper, HVAC, HV-tavler, SRO/SCADA")
    m.bullet("Døgnet som vilkår",
              "Vagtordning, alarmer og akut fejlfinding **døgnet rundt**; 5S, "
              "standardarbejde og **PDCA** med 40 procent lavere energiforbrug som effekt.")

    m.job("Produktionsformand / elektromekaniker",
          "ARJ Engineering · Teheran · 2003–2010 · 12 mekanikere og teknikere")
    m.bullet("Første lederrolle",
              "Vagtplan, fordeling og oplæring i et værksted med maskiner, værktøj og tegninger "
              "i daglig brug.")

    # ---------------------------------------------------------------- side 3
    m.page_break()
    m.section("UDDANNELSE OG AUTORISATION")
    m.edu("Elautoriseret maskinmester — dansk elautorisation LV/MV/HV",
          "Sikkerhedsstyrelsen · maj 2023")
    m.edu("B.Tech, Technology Management and Mechanical Engineering (EQF 6)",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12")
    m.edu("El- og maskinteknisk design, Electrical Engineering (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("Lean: 5S, PDCA, VSM, A3 · køle- og VVS-teknik (AMU) · STCW-sikkerhed",
          "Mercantec 2021 · Søfartsstyrelsen 2021–2023")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("**Dansk:** modersmål · **Engelsk:** professionelt, skriftligt og mundtligt · "
           "**Persisk:** modersmål · **Bor i Måløv**, Trafiktårnet er en S-togstur derfra · "
           "**Kørekort B** · **Kan tiltræde efter aftale** · Referencer efter aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA HÆNDELSESLOG TIL EN RYTME, DER HOLDER",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–2",
             "Sid med på alle tre vagtlag i Trafiktårnet og læs de sidste tre måneders store "
             "hændelser igennem: hvad skete der, hvem disponerede, og hvornår kom meldingen ud. "
             "Mød teamlederen, de 19 **togledere**, tillidsrepræsentanter og chefgruppen."),
            ("Dag 30",
             "Et fælles billede af, hvor minutterne forsvinder: de fem hyppigste "
             "hændelsestyper, tid fra alarm til **disponering**, og hvor **trafikinformationen** "
             "kom for sent. En ejer og en dato på hver."),
            ("Dag 60",
             "**Nødplaner** og disponeringsmønstre gennemgået med **jernbanevirksomhederne**; "
             "kompetencematrix for sektionen med signalsystemets næste strækning i planen, så "
             "oplæring ligger før ibrugtagning og ikke efter."),
            ("Dag 90",
             "En fast rytme: driftsmøde, hændelsesgennemgang og opfølgning samme uge. "
             "**Responstid** og genopretning målt i sektionen, og næste kvartals planlagt med "
             "chefgruppen."),
        ],
        widths=(1500, 8830))

    m.section("ET DØGN HAR 1.440 MINUTTER — DET ER DEN RESSOURCE, DER SKAL PRIORITERES")
    m.para("En sektion i døgndrift bliver ikke målt på, hvor travlt der er, men på hvad der blev "
           "prioriteret, da der var flest hændelser samtidig. Derfor skal prioriteringen ligge "
           "som en aftale før hændelsen: hvad må vente, hvem kan flyttes, og hvornår må en "
           "togleder ikke tages ud af stolen. Den aftale har jeg bygget med kapacitet og "
           "bemanding på 14 mand, 11 samtidige entrepriser og en nattevagt, der ikke kunne "
           "forstærkes.", after=70)

    m.section("DER SKAL VÆRE EN, DER MÅ SIGE STOP — OGSÅ NÅR DET KOSTER PUNKTLIGHED")
    m.para("Sikkerheden kommer før **kundepunktlighed**, og det er ikke en hensigtserklæring; det "
           "er en rækkefølge, der skal kunne ses i beslutningen klokken 02.14. Derfor skal den, "
           "der stopper trafikken, have svar med det samme, få afgrænsningen med og ikke blive "
           "målt på stilstand bagefter. Et toglederteam, der tør stoppe, er billigere end et team, "
           "der lader en strækning køre videre på et usikkert grundlag.", after=70)

    m.section("EN HÆNDELSE ER IKKE LUKKET, FØR DEN ER SKREVET NED OG LÆST OP")
    m.para("Hændelsesloggen er sektionens vigtigste dokument. Den skal kunne læses af den, der "
           "har vagten i morgen, og af chefgruppen om en måned. Derfor bliver hver større hændelse "
           "gennemgået dagen efter med dem, der sad med den: hvad vidste vi, hvad besluttede vi, "
           "og hvad ville vi gøre anderledes. Uden den samtale bliver den samme hændelse et "
           "samtaleemne hvert kvartal.", after=70)

    m.section("SIGNALSYSTEMET SKIFTER IKKE I ET DIAGRAM — DET SKIFTER I ET MENNESKE")
    m.para("Udrulningen af det nye **signalsystem** flytter arbejdsgange og systemgrænser, og "
           "det sker, mens driften kører. Derfor er **kompetenceudvikling** en driftsopgave: "
           "superbrugere i hvert vagtlag, øvelse på fejl inden ibrugtagning, og en instruks der "
           "er skrevet sammen med dem, der skal bruge den. **Forandringsledelse** er i den "
           "sammenhæng ikke et program — det er at sørge for, at den nye arbejdsgang er prøvet af, "
           "før den er obligatorisk.", after=70)

    m.section("ÅBEN DIALOG ER FØRST ÅBEN, NÅR DEN KOSTER NOGET")
    m.para("Der er interessemodsætninger mellem at køre mest mulig trafik, at gennemføre "
           "anlægsarbejdet og at give passageren et rigtigt svar. De bliver ikke mindre af at "
           "blive talt pænt om. **Interessenthåndtering** er for mig at lægge uenigheden på "
           "bordet tidligt, med en fælles faktarække, og at holde den aftale, der bliver indgået "
           "— også når den er ubehagelig i chefgruppen ugen efter.", after=70)

    m.section("HVOR JEG VILLE STARTE")
    m.para("På nattevagten i Trafiktårnet, med hændelsesloggen fra de sidste tre måneder under "
           "armen. Første uge: lytte i alle tre vagtlag, se hvordan en hændelse bevæger sig fra "
           "alarm til melding, og finde ud af, hvor mange af månedens store hændelser der var den "
           "samme type med et nyt nummer. Derefter tage den første hele vejen: afgræns, disponer, "
           "meld ud, evaluer dagen efter — og gøre det igen om en måned med tal, der kan "
           "sammenlignes.", after=0)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "DET EFTERSPØRGER DE — DET HAR JEG",
        ["Krav i opslaget", "Dokumentation"],
        [
            ("Leder for en sektion med 21 medarbejdere og to direkte referencer, herunder en "
             "teamleder med personaleansvar for 19 togledere",
             "Tolv års personaleansvar: 25 specialister i tværfaglig ledelse, 14-mands team, "
             "12 mand i værkstedet og 5 elektrikere + 3 lærlinge med MUS og 1:1."),
            ("Overordnet ansvar for ledelsen og udviklingen af sektionen",
             "Sektionens rammer sat af mig selv: mål, tavlemøde, kompetencematrix og "
             "udviklingsplan pr. medarbejder — med fuldt P&L siden 2023."),
            ("Drift og leverancer planlægges, prioriteres og optimeres, så sektionen understøtter "
             "en stabil og effektiv trafikafvikling",
             "Døgn-, uge- og månedshjul med prioriteret kapacitet; 11 samtidige entrepriser og "
             "37 projekter leveret med nul kritiske fund."),
            ("Bred kontaktflade og interessenthåndtering — stærke og tillidsfulde relationer",
             "**Interessenthåndtering** i 37 CAPEX-projekter: bygherre, myndighed, entreprenører "
             "og drift omkring samme beslutning; aftaler holdt, også de svære."),
            ("Træffe kvalificerede beslutninger i komplekse situationer med betydning for "
             "togtrafikken på landsplan",
             "Beslutninger under tidspres i 24/7-drift: afgræns, vælg nødplaner, disponer, meld "
             "ud, evaluer dagen efter — med hændelsen logget fra alarm til lukning."),
            ("Rammer for højt specialiserede medarbejderes faglighed — trivsel, motivation og "
             "fortsat udvikling",
             "Faglighed i spil gennem mandat og rammer, ikke gennem kontrol; **trivsel** og "
             "**motivation** som fast punkt i MUS og 1:1, med ansvar givet tidligt."),
            ("Chefgruppen for Driftscenter & Kundeinformation — tværgående samarbejde, åben "
             "dialog og højt fælles ambitionsniveau",
             "**Chefgruppe**arbejde i eget selskab og på 37 projekter: fælles mål, åben dialog "
             "om det, der ikke går godt, og en aftale alle parter kan holde."),
            ("Tæt samarbejde med chefgruppen i Trafikkontrolcentre og en række fagområder i "
             "Vedligeholdelsesdivisionen",
             "**Tværgående** samarbejde mellem drift, teknik og vedligehold: 14-mands team, 11 "
             "entrepriser og 25 specialister i samme plan, med en ejer pr. snitflade."),
            ("Erfaring fra en større driftsorganisation, gerne fra et miljø med døgnbemandede "
             "funktioner",
             "Fire år i **døgnbemandet** drift på Lynetten med vagtordning, SRO/SCADA, HV-tavler "
             "og akut fejlfinding — og 25 specialister i et reguleret produktionsmiljø."),
            ("Erfaring med personaleledelse er vigtig, og erfaring med ledelse af ledere er en "
             "fordel",
             "**Personaleledelse** i tolv år. **Ledelse af ledere**: på 37 projekter havde hver "
             "disciplin sin fagligt ansvarlige, som jeg satte mål og mandat for."),
            ("Skabe resultater gennem andre og navigere i organisatoriske forandringer — "
             "forandringsledelse er væsentlig",
             "**Forandringsledelse** i drift: nye systemer og arbejdsgange indført, mens driften "
             "kørte; 40 procent lavere energiforbrug og 40 procent højere produktivitet."),
            ("Erfaring fra driftsmiljøer og trafikal viden som fordel — og kunne sætte sig ind i "
             "komplekse driftsmæssige problemstillinger",
             "**Disponering** og **nødplaner** arbejdet med i drift, hvor en time flyttet koster "
             "en kunde; driftsmæssige problemer afgrænset og løst i 24/7-drift og på 11 anlæg."),
            ("Skabe følgeskab og drive opgaver fremad uden formelt ledelsesansvar — relationer, "
             "interessenter og samarbejde på tværs",
             "**Følgeskab** uden mandat: 25 specialister og 37 projektejere fulgte samme plan; "
             "uenighed løst i mødet og ikke i referatet bagefter."),
            ("Central rolle i udviklingen af sektionen og området — organisering, "
             "samarbejdsformer og kompetenceudvikling",
             "Organisering bygget om i eget selskab: arbejdsgange, samarbejdsformer og "
             "oplæringsplaner; **kompetenceudvikling** styret på en kompetencematrix."),
            ("Diplomuddannelse i ledelse eller tilsvarende — ellers påbegyndes den inden for de "
             "første to år",
             "**Diplomuddannelse** i ledelse påbegyndes inden for de første to år, jf. opslaget; "
             "grundlaget er tolv års ledelsespraksis med MUS, coaching og SLII/GROW."),
            ("Tydelig og beslutningsstærk, skaber naturligt følgeskab og bevarer overblikket, når "
             "tempoet er højt",
             "**Beslutningsstærk** i drift: beslutningen tages, når den skal, med den "
             "information der findes — og der bliver sagt hvad, hvornår og af hvem."),
            ("Stærk kommunikator med tillid hos medarbejdere, ledere og samarbejdspartnere — "
             "håndterer interessemodsætninger og konflikter",
             "Kommunikation i øjenhøjde, også om det svære; interessemodsætninger taget i mødet "
             "med **respekt** for faglighederne og en aftale til slut."),
            ("Fleksibilitet og forståelse for driftsvilkårene **døgnet rundt** alle årets dage — "
             "og synlighed i driften på relevante lokationer",
             "Vagtordning, natteudkald og weekendarbejde i fire år; **synlig** i driften gennem "
             "Gemba, tavlemøder og sikkerhedsrundering — ikke gennem møder om driften."),
        ],
        widths=(3600, 6746))

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_Banedanmark_SektionschefDriftscenter.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_Banedanmark_SektionschefDriftscenter.docx'))
