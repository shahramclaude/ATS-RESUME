# Ansøgningssystem — Shahram Ajloo

## Faste fakta — rettelser der gælder ALLE ansøgninger (opdateret 12.11.2026)
- **Bopæl: Måløv** (Ballerup Kommune) — *ikke* Søborg. Kontaktlinjen i banneret slutter med "Måløv".
- **Titel: elautoriseret maskinmester** (LV/MV/HV) — *ikke* "autoriseret elinstallatør" / "autoriseret el-installatør". Uddannelsen er B.Tech i Technology Management & Mechanical Engineering (maskinmesterretningen), og elautorisationen er erhvervet oven på den.
- Når et opslag kræver "maskinmester eller el-installatør", skrives det som opslagets eget krav, og svaret er "elautoriseret maskinmester" — aldrig ved at påtage sig titlen elinstallatør.
- **Akkord (bruger, 12.11.2026):** han har **selv stået med akkord** — akkordbreve, opmåling, tildeling til sjak og regulering. Det må skrives som dokumenteret erfaring i alle dokumenter, hvor opslaget kræver akkordforståelse.
- **Sideløbende stilling (bruger, 12.11.2026): medejer af IT-virksomheden Data Power Consultant ApS, København, 2024 – nov. 2026**, hvor han var **CTO / teknisk ansvarlig for AI- og AI coding-afdelingen** (4-10 personer). Afdelingen leverede **både kundeløsninger med LLM/AI og AI-assisteret softwareudvikling**. Selskabet er **ophørt**, han er trådt ud, og i dag driver han **kun ELOHVAC**. De to stillinger kørte **samtidig** — ELOHVAC-forløbet er ikke afbrudt, og Data Power må aldrig fremstilles som et hul i det.
- Data Power Consultant ApS skal stå som **selvstændig, sideløbende post** i CV'et med periode (2024 – nov. 2026) og rolle — ikke som en bisætning i ELOHVAC-posten, og ikke som "tidligere stilling" uden periode.
- **AI coding til design (bruger, 12.11.2026):** professionel brug af **AI coding til design af tekniske anlæg og industrielle komponenter** hører til Data Power-posten og til Digital/AI-banken — beskrevet som beregning, dimensionering og designvarianter med faglig validering af output. Det er en kompetence i sig selv, ikke kun et værktøj under ELOHVAC.
- **Resultater for Data Power (bruger, 12.11.2026):** brugeren har godkendt, at der vælges et par konkrete resultater om **implementering af tekniske og industrielle applikationer** og om **professionel brug af AI i ledelsesarbejde og matrixledelse**. De er formuleret procesnært og dokumenterbart (krav, arkitektur, idriftsættelse, overdragelse, standarder for AI-output, én samlet plan for to sideløbende organisationer) — **uden opdigtede procenter, kundetal eller kroner**. Den eneste målte effekt, der må bruges, er fortsat **over 40 % produktivitetsløft** fra AI-værktøjerne i ELOHVAC-posten.
- **Ledelses-, personaleledelses- og projektledelsesværktøjer (bruger, 14.11.2026 — gælder ALLE dokumenter):** han har **arbejdet med de fleste** værktøjer inden for ledelse, personaleledelse og projektledelse, heriblandt **PRINCE2**, **LEAN** og **Six Sigma**. Det må skrives som **»arbejdet med« / »anvendt i praksis«** i alle dokumenter, hvor opslaget spørger til metoder eller værktøjer — også når opslaget kalder det et krav eller en bonus. **Skriv aldrig »certificeret i LEAN/Six Sigma«** og aldrig et certifikat, han ikke selv har nævnt: kun **PRINCE2** er et certifikat (bekræftet 14.11.2026). Ved en bonuslinje som »Lean or Six Sigma certification« svarer dokumentet: metoderne er brugt i praksis, certificeringen er der ikke.
- **Skal IKKE i CV'et (bruger, 12.11.2026):** CVR-nummer og kundenavne. De bruges ikke, heller ikke som pladsholder.
- **Slutmåned er november 2026 (bruger, 12.11.2026)** — perioden skrives i CV'et som *2024 – nov. 2026*.
- Ved tvivl: ret i `master/MASTER_RESUME_SHAHRAM_AJLOO.md`, ikke i det enkelte byggescript.

## BINDENDE POLICY — PERMANENT INSTRUKS, FORNYET 13.11.2026 (bruger, gælder alle fremtidige dokumenter)

Brugeren har gentaget den permanente instruks og skærpet den. Den gælder **hvert eneste** CV og hver
eneste ansøgning herfra, og den er **maskinelt håndhævet** — nedenstående tabel viser hvor.

| # | Instruks (brugerens ord) | Sådan opfyldes den | Kontrol |
|---|---|---|---|
| 1 | *„Be creative, progressive, and unique; use different styles of building the cover letter“* | Åbningen, strukturen og registret vælges fra `master/FORMKATALOG.md`, og de tre ting skal skifte mod det forrige dokument | `style_guard.py` — **3/3 skift**, ellers stop |
| 2 | *„Adapt and synchronize the resume's language … with the individual company“* | `jd/<Stilling>_kultur.txt` med virksomhedens egne formuleringer, brugt **ordret** i brevet | `policy_check.py --kultur-file` — **100 %** skal genfindes (tidligere 60 %) |
| 3 | *„Research the company's culture deeply … mission and needs“* | Kultur-, ledelses- og organisationsresearch med **kilde** i `master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md` (§-nummer) **før** der bygges | slutkontrol pkt. 5 + INTEL-§ i commit |
| 4 | *„Entirely job-focused, not candidate-focused“* | Første afsnit tager udgangspunkt i opgaven, virksomheden eller kravet — aldrig i ansøgeren | `policy_check.py` — **kandidat-først åbning blokerer** (nyt 13.11.2026) |
| 5 | *„ALL the requirements … nothing overlooked or addressed superficially“* | Én kravrække pr. krav i opslaget, og hver række dokumenteres med **≥ 110 tegn** metode + ansvar + resultat | `policy_check.py` — **kravdækning og 110 tegn blokerer** (tidligere advarsel) |
| 6 | *„demonstrate precisely how … my experience will enable me to solve the specific challenges“* | Hver række besvarer **krav → problem i opgaven → metode → resultat**, med tal hvor de findes | `policy_check.py` — rækker uden tal markeres |
| 7 | *„Do not focus on describing how intelligent, talented, ambitious or impressive I am“* | Forbudte rosord og personbeskrivelser; ingen selvbiografisk indledning | `policy_check.py` — **blokerende** ved ros-/personord |
| 8 | *„make the employer recognize that I am the right solution … not simply another candidate“* | Dokumentet slutter med, hvad der sker på mandag: **90 dage** med ejer, kadence og leverance — ikke en hensigt | slutkontrol pkt. 3 |

**Konsekvens for byggeprocessen — rækkefølgen er fast:**
1. Læs opslaget og skriv `jd/<Stilling>_krav.txt` — **alle** krav, ordret, også de skjulte (én pr. linje).
2. Research virksomheden (mission, strategi, ledelsessprog, tone, pres) → skriv **§ i INTEL med kilde**.
3. Skriv `jd/<Stilling>_kultur.txt` — virksomhedens egne udtryk, ordret.
4. Vælg form i `FORMKATALOG.md` og kør `style_guard.py` **før** der bygges.
5. Byg dokumentet; hver sætning om ansøgeren skal pege på en opgave i stillingen.
6. Kør `policy_check.py` (krav + kultur) og `ats_check.py`; intet må være gult eller rødt.
7. Læs alle sider visuelt. Først derefter commit, PR og — på brugerens ord — merge.

**Ældre dokumenter:** de tre nyeste (#242, #243, #244) er efterkontrolleret og består 100 %-reglen,
110-tegnsreglen og åbningsreglen. Skal et ældre dokument genbruges, køres `--allow-thin` for at se
forskellen — men et dokument, der skal sendes, bygges om efter reglerne ovenfor.

## BINDENDE POLICY — DATA POWER-POSTEN SKAL MED I ALLE CV'ER (bruger, 12.11.2026)

Posten er **obligatorisk i hvert eneste CV**, uanset stillingstype, og den skal stå som **selvstændig,
sideløbende post** — ikke som en bisætning under ELOHVAC og ikke som et hul i ELOHVAC-forløbet.

**Kanonisk post (brug disse formuleringer eller tættere varianter på dem):**

> **Data Power Consultant ApS · København — Medejer og CTO / teknisk ansvarlig for AI-afdelingen ·
> 2024 – nov. 2026 (sideløbende med ELOHVAC)**
> - **Medejer** af IT-virksomheden og ansvarlig for **AI- og AI coding-afdelingen** med **4-10 personer**.
> - **Implementering af tekniske og industrielle applikationer** for kunder: kravafdækning, arkitektur,
>   datamodel, integration og idriftsættelse, afsluttet med dokumentation og overdragelse.
> - **Kundeløsninger med LLM-API'er og AI-agenter** fra proceskortlægning til produktionssat løsning.
> - **AI-assisteret softwareudvikling** som fast del af udviklingsprocessen: kodegenerering, review og
>   test med fælles standarder for, hvornår AI-output accepteres.
> - **AI coding til design af tekniske anlæg og industrielle komponenter**: beregning, dimensionering
>   og designvarianter med faglig validering af output.
> - **AI som værktøj i ledelsesarbejdet**: ledelsesrapportering, beslutningsoplæg, mødeopsummering og
>   KPI-analyse med samme struktur hver gang.
> - **Matrixledelse i praksis**: to sideløbende organisationer med én samlet plan og skriftlige
>   aftaler om, hvad der går forud.
> - **Selskabet er ophørt**, stillingen er afsluttet, og i dag drives kun ELOHVAC.

**Regler for posten:**
- **Aldrig udelades.** Også i CV'er til ikke-tekniske stillinger — der fremhæves matrixledelse, AI i
  ledelsesarbejdet og kundeleverancer; i tekniske stillinger fremhæves applikationer og AI coding til
  design.
- **Perioden skrives altid** (2024 – nov. 2026) og ordet **sideløbende**, så læseren ikke tror, at ELOHVAC
  stoppede.
- **By: København**, periode **2024 – nov. 2026** (slutmåned bekræftet af brugeren 12.11.2026).
- **CVR og kundenavne skal ikke i CV'et** — de skrives ikke, og de opfindes ikke.
- **Ingen nye procenter.** Den eneste målte effekt, der må citeres, er **over 40 % produktivitetsløft**
  fra AI-værktøjerne i ELOHVAC-posten.
- Kompetencerne skal også ind i nøgleordsbanken, så ATS-matchning kan bruge dem: *AI coding,
  LLM-API'er, AI-agenter, industrielle applikationer, matrixledelse, AI i ledelsesarbejdet*.
- **Maskinelt tjek:** `scripts/policy_check.py` advarer nu, hvis dokumentet ikke indeholder
  »Data Power« — så posten ikke kan glemmes i et byg.

## BINDENDE POLICY — SKRIV MED EKSTREM SIKKERHED (bruger, 05.11.2026)

Et tvivlende, forsigtigt eller undskyldende dokument giver **ingen samtaleindkaldelse**. Ansøgningen og CV'et skal være skrevet, så den ansættende leder er overbevist om, at Shahram er den bedste kandidat til stillingen.

- **Aldrig forbehold, aldrig huller, aldrig "ikke endnu".** Disse vendinger er forbudt i alle dokumenter: "jeg har ikke arbejdet med X", "X er nyt for mig", "det skal jeg lære", "det er ikke det samme som", "ikke i en farmaceutisk fabrik før", "jeg har ikke været driftsansvarlig for", "jeg skal være ærlig om", "tæt nok på". Også i KRAV-/evidence-tabellen: den indeholder **kun dokumentation**, aldrig en note om, hvad der mangler.
- **Brugeren søger kun stillinger, hvor kompetencerne er til stede.** Der er derfor intet at indrømme — opgaven er at formulere kompetencen konkret og selvsikkert, ikke at beskrive fraværet af den.
- **Konkret og afsluttende:** systemer, årstal, tal, metoder, ansvar og resultater i korte, færdige sætninger. Ingen "jeg tror", "jeg vil gerne forsøge", "forhåbentlig", "jeg håber".
- **Sikkerhed, ikke superlativ.** Første person, aktiv form, præcise fagtermer og rolig autoritet. Ingen selvros om personlighed ("bedste", "enestående", "perfekt"), men absolut ingen forbehold. Dokumentets troværdighed er det, der giver indkaldelsen.
- **Opdigtede fakta er stadig forbudt** (se regel 7 og master-fakta): systemnavne, anlægsnumre, certificeringer og resultater må ikke opfindes. Forskellen er, at det **reelle** skrives som en styrke — aldrig som et forbehold.
- **Ved tvivl om en kompetence: spørg brugeren — skriv ikke et forbehold.** Han har kompetencerne; formuleringen er min opgave.
- Denne policy erstatter den tidligere regel 5 ("mangler meldes ærligt på én linje").

## BINDENDE POLICY — JOBBET FØRST, KANDIDATEN KUN SOM BEVIS (bruger, 07.11.2026)

Gælder **alle** fremtidige CV'er og ansøgninger. Præciserer og udvider regel 1–5 ovenfor; ved konflikt går denne policy forud.

- **Udgangspunktet er stillingen, ikke ansøgeren.** Virksomhedens mission, stillingens formål, organisationens mål og de krav, opgaven stiller, er fundamentet for hele dokumentet — ansøgning som CV.
- **Alle krav i opslaget skal adresseres. Intet må overses eller behandles overfladisk.** Hver enkelt kompetence, ansvarsområde, forventning og kvalifikation i JD'en — også dem, der står i en bisætning, i en personprofil eller i et "det er en fordel, hvis"-afsnit — skal have en konkret, dokumenteret besvarelse. KRAV-/evidence-tabellen dækker **samtlige** kravpunkter, ét punkt pr. krav, ikke et udvalg.
- **Vis hvordan, ikke hvem.** For hvert krav skal dokumentet vise, hvilket problem eller hvilken udfordring i stillingen kravet svarer til, hvilken metode eller erfaring der løser den, og hvilket resultat det gav — konkret og målbart hvor det findes. Formlen er krav → opgavens problem → løsning → resultat.
- **Ingen selvbeskrivelse af personlige egenskaber.** Ingen afsnit om at være intelligent, talentfuld, ambitiøs, engageret eller "den rette type". Personlige kvaliteter må kun optræde som adfærd knyttet til en konkret arbejdsopgave (fx "jeg har selv siddet med vagten, da …").
- **Målet med dokumentet:** den ansættende leder skal se ansøgeren som **løsningen på stillingens udfordringer**, ikke som endnu en kandidat, der beskriver sig selv.
- Praktisk kontrol før levering: (1) læs opslaget igennem og tjek, at hvert eneste krav har en række i KRAV-tabellen og en konkret formulering i ansøgningen; (2) tjek, at hver formulering om ansøgeren peger på en opgave i stillingen; (3) fjern enhver sætning, der kun handler om, hvor god ansøgeren er.

### Håndhævelse — obligatorisk trin i hvert byg (07.11.2026)

Policyen kontrolleres maskinelt, så den ikke afhænger af hukommelse:

1. For hvert opslag skrives **`jd/<Stillingsnavn>_krav.txt`** med **ét krav pr. linje** — taget ordret eller næsten ordret fra opslaget, inkl. punkter fra personprofilen og "det er en fordel, hvis". Ansættelsesvilkår (løn, sikkerhedsgodkendelse, kørekort) medtages ikke som kompetencekrav.
2. Før commit køres:
   ```
   python3 scripts/policy_check.py <dokument.docx> --krav-file jd/<Stillingsnavn>_krav.txt
   ```
   Den skal svare **✓ Policy 'jobbet først' opfyldt**. Fejler den, rettes dokumentet — ikke kravfilen.
3. Kontrollen verificerer: (a) at der findes en kravmatrix i dokumentet, (b) at matricen har **mindst lige så mange rækker som der er krav** i opslaget, (c) at **hvert krav kan genfindes** i en konkret række (ordoverlap med bøjnings- og sammensætningshensyn), og (d) at der **ikke** står selvrosende personbeskrivelse (fx "intelligent", "talentfuld", "ambitiøs", "enestående", "fremragende", "passioneret").
4. `scripts/ats_check.py --words-file …` køres som før for nøgleordsdækning. Begge checks skal være grønne, før der committes.

## BINDENDE POLICY — KULTURSYNKRONISERET, KREATIV FORM (bruger, 04.11.2026, permanent)

Gælder **alle** fremtidige CV'er og ansøgninger. Supplerer og skærper policyen om varieret sprog,
stil og kulturtilpasning ovenfor; ved konflikt går denne policy forud.

- **Sproget og "litteraturen" synkroniseres med den enkelte virksomhed.** Register, ordforråd,
  sætningsrytme, metaforer og sektionsoverskrifter vælges efter **deres** egne tekster — ikke efter
  vanen og ikke efter forrige dokument. Et dokument skal kunne genkendes som skrevet **til** denne
  virksomhed, ikke som det forrige med et nyt firmanavn.
- **Formen skal være kreativ, progressiv og ny hver gang.** Der er ingen fast skabelon for side 1.
  Variationen skal sidde i mere end ordvalget: åbningsgreb, sektionsrækkefølge, kadence (korte hug
  vs. lange forklarende sætninger), hvordan kravene besvares (løbende prosa, teser, problemkatalog,
  dagsforløb, ordliste, snitflader, dokumentrækkefølge), og hvordan CV'et spejler samme register.
  Mindst to af de tre stilvalg skal skifte fra forrige dokument — maskinelt kontrolleret af
  `scripts/style_guard.py`.
- **Dyb kulturresearch er obligatorisk, hver gang.** Mission og formål, strategi og organisatoriske
  mål, ledelsesprincipper, hvordan de beskriver kunder, medarbejdere og produkter, tone, bæredygtig-
  heds- og DEIB-sprog, hvad de er stolte af, og hvad de er presset på. Kilder: opslaget, careers-site,
  årsrapport, ejerforhold, fagpresse, nyheder. Funnene skrives i
  `master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md` **med kilde** og skal kunne peges på i teksten.
  Opslaget alene er ikke nok.
- **Arbejdsgiverens opgave er fundamentet; kandidaten er beviset.** Stillingens formål, virksomhedens
  mission og de krav, opgaven stiller, bærer hele dokumentet. Hver formulering om ansøgeren skal
  pege på en opgave i stillingen.
- **Alle krav skal besvares — også de skjulte.** Punkter i personprofilen, i bisætninger og i
  "det er en fordel, hvis" er lige så bindende som hovedopgaverne. Intet krav må mangle en konkret
  formulering i ansøgningen og en række i kravmatrixen; intet krav må besvares overfladisk med et
  nøgleord alene.
- **Vis løsningen, ikke personen.** Formlen er **krav → opgavens problem → metode/erfaring →
  resultat**. Resultatet skal være konkret og målbart, hvor det findes.
- **Ingen selvbeskrivelse.** Intet om at være intelligent, talentfuld, ambitiøs, engageret,
  "den rette type" eller "en stærk kandidat". Personlige egenskaber må kun optræde som adfærd knyttet
  til en konkret arbejdsopgave.
- **Målet:** den ansættende leder skal se ansøgeren som **løsningen på stillingens udfordringer** —
  ikke som endnu en kandidat, der beskriver sig selv.

### Forbehold og kravhuller — besluttes pr. opslag (bruger, 04.11.2026)

De to hensyn kan støde sammen: den 05.11.2026-policy forbyder forbehold, og kravdækningskravet
forbyder, at et krav bare ignoreres. Reglen er derfor:

- **Som udgangspunkt: ingen forbeholdsafsnit.** Når match er tæt, besvares hvert krav med
  dokumenteret erfaring, metode og resultat — også krav, der kun er delvist dækket, formuleres som
  den kompetence, der faktisk findes, knyttet til opgaven.
- **Spørg brugeren, før der bygges**, hvis et **formelt, hårdt krav** reelt ikke er opfyldt (fx en
  navngiven uddannelse, en certificering eller en autorisation). Beslutningen om, hvordan det
  håndteres, er hans — ikke min.
- **Hvis han vælger åbenhed:** det står **faktuelt** i kravmatrixen som én række og højst som ét
  kort afsnit, formuleret som hvad der *i stedet* er dokumenteret. Aldrig som en undskyldning,
  aldrig som "endnu", aldrig som et selvstændigt tema i brevet.
- **Hvis han vælger det ikke:** kravet besvares med den nærmeste dokumenterede kompetence, og
  rækken beskriver, hvad der er leveret — ikke hvad der mangler. Intet opdigtes.
- **Uanset valg:** kravet skal have en række i matrixen, og formuleringen skal være sand.

### Slutkontrol før commit (fire spørgsmål, alle skal kunne besvares med ja)

1. **Kunne dette dokument være sendt til en anden virksomhed?** Hvis ja: kulturresearch og sproglig
   synkronisering er ikke gennemført — byg om.
2. **Ligner det noget, vi har sendt før?** Sammenlign åbning, struktur og register med de seneste
   seks linjer i `master/STILREGISTER.md`.
3. **Er hver sætning om ansøgeren et svar på et krav i opslaget?** Sætninger, der kun handler om,
   hvor god han er, slettes.
4. **Er der et krav i JD'en uden en række i matrixen og uden en konkret formulering i brevet?**
   Hvis ja: færdiggør før commit — ikke efter.

## BINDENDE POLICY — PERMANENT INSTRUKS, BEKRÆFTET OG MASKINELLT HÅNDHÆVET (bruger, 04.11.2026)

Brugeren har gentaget instruksen som **permanent** for alle fremtidige CV'er og ansøgninger. Den
erstatter ikke afsnittene ovenfor, men skærper dem og gør dem **obligatoriske at kontrollere**:

1. **Sprog og stil skifter per virksomhed.** Register, ordforråd, rytme og sektionsoverskrifter
   vælges efter virksomhedens egne tekster. Aldrig samme form to gange i træk.
2. **Kreativ, progressiv og ny form hver gang.** Formen er ikke en skabelon: åbningsgreb,
   sektionsrækkefølge, kadence og måden kravene besvares på skal kunne varieres uendeligt.
   Kataloget over tilgængelige former står i **`master/FORMKATALOG.md`**, og rotationen kontrolleres
   af `scripts/style_guard.py` (mindst 2 af 3 skift mod forrige dokument).
3. **Dyb kulturresearch hver gang** — mission, formål, strategi, organisatoriske mål, ledelsesprincipper,
   tone, bæredygtigheds- og DEIB-sprog, hvad de er stolte af, hvad de er presset på. Kilder ud over
   opslaget. Funnene skrives i `master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md` med **§-nummer og kilde**.
4. **Arbejdsgiveren er fundamentet; kandidaten er beviset.** Stillingens formål, virksomhedens mission
   og kravene bærer hele dokumentet. Hver sætning om ansøgeren skal pege på en opgave i stillingen.
5. **Alle krav besvares — også de skjulte**, og intet krav må besvares overfladisk med et nøgleord.
6. **Formlen er krav → opgavens problem → metode/erfaring → resultat**, med tal hvor de findes.
7. **Ingen selvbeskrivelse.** Intet om at være intelligent, talentfuld, ambitiøs eller "den rette".

### Ny obligatorisk fil: `jd/<Stillingsnavn>_kultur.txt`

Ved hvert byg skrives **arbejdsgiverens egne udtryk** — mission, værdier, kulturord, deres eget
sprog om kunder, medarbejdere og produkter — **ét udtryk pr. linje**, taget ordret fra deres egne
tekster. Filen er grundlaget for den sproglige synkronisering og kontrolleres maskinelt:
**alle udtrykkene skal kunne genfindes i dokumentet (100 %, skærpet 13.11.2026).**

### Udvidet kontrol før commit — to checks, ét kald

```
python3 scripts/policy_check.py <dokument.docx> \
        --krav-file   jd/<Stillingsnavn>_krav.txt \
        --kultur-file jd/<Stillingsnavn>_kultur.txt
python3 scripts/ats_check.py    <dokument.docx> --words-file jd/<Stillingsnavn>_words.txt --expect-pages 4
```

`policy_check.py` kontrollerer nu fire ting ud over selvros:

| Kontrol | Regel | Effekt |
|---|---|---|
| Kravdækning | hvert krav i kravfilen skal genfindes i en matrixrække | blokerende |
| **Dybde** | hver rækkes dokumentation skal være **≥ 110 tegn** | **blokerende** (13.11.2026) |
| **Resultat** | rækker uden ét eneste tal markeres | advarsel |
| **Kultursynkronisering** | **100 %** af `_kultur.txt` skal genfindes i dokumentet | blokerende |

### Slutkontrol (supplerer de fire spørgsmål ovenfor)

5. **Kunne en sætning i dokumentet være skrevet til en konkurrent?** Hvis ja: kulturfilen er ikke brugt.
6. **Står der et tal eller et konkret resultat i hver matrixrække, hvor et sådant findes?**
7. **Er der en matrixrække, der kun består af et nøgleord og en titel?** Den skal uddybes eller fjernes.
8. **Står Data Power Consultant ApS-posten i CV'et** med periode, by, rolle og AI-kompetencerne — som
   selvstændig, sideløbende post? (Se den bindende policy ovenfor.)

## Faste regler — gælder ALLE fremtidige ansøgninger (bindende)
1. **Dokumentet handler ikke om ansøgeren — det handler om opgaven, missionen og stillingen.** Ansøgningen (side 1) tager udgangspunkt i det, stillingen skal løse: hvad der skal lykkes, hvilke KPI'er og rammer der styrer det, og hvad der typisk går galt i den slags rolle. "Jeg"/"min" bruges kun som bevis på, at opgaven er forstået, aldrig som præsentation af personen.
2. **Dokumentet skal vise et fast greb om kravet** — hver JD-overskrift besvares med en konkret metode, et system eller et tal fra praksis, så læseren kan se, at opgaven er løst før (ikke at kandidaten er sød).
3. **Dokumentet skal vise, at systemet til dag 1 allerede er bygget:** en konkret 90-dages-plan (uge 1 → dag 30 → dag 60 → dag 90) med ejerskab, møder, målinger og leverancer — ikke hensigter. Læseren skal kunne se, hvad der sker på mandag, hvis han får jobbet.
4. Konsekvens: ingen selvbiografisk indledning, ingen "jeg er en passioneret…", ingen opremsning af personlighed. CV-delen må gerne være faktuel og taldrevet — kravet om opgavefokus gælder især ansøgningen og profilafsnittet.
5. **Ingen forbehold (bruger, 05.11.2026).** Dokumentet skriver aldrig, hvad kandidaten *ikke* har gjort, ikke "endnu" og ikke "skal lære". Hvert krav i opslaget besvares med dokumenteret erfaring, metode og resultat — se den bindende policy om ekstrem sikkerhed øverst i dette dokument. Geografi, systemer og branche beskrives som noget, han kender og har arbejdet i; opdigtede fakta er fortsat forbudt.
6. **Leverancen er altid den samme, uanset hvad opslaget beder om.** Siger JD'en "kun CV", "motiveret CV", "ingen ansøgning" eller lignende, leveres stadig **ét samlet dokument: side 1 = motiveret, opgave-først side, derefter CV i masterdesignet**. CV'et tilpasses så det kan stå alene, men ansøgningssiden udelades aldrig (bruger, 31.10.2026).

7. **Hele produktet skal være humaniseret** (bruger, 02.11.2026). Ansøgning, CV, profil, overskrifter og opstartsplan skal lyde naturligt og troværdigt som en erfaren fagpersons egne ord — ikke som en AI-skabelon. Brug konkret, ligefremt sprog, naturlig sætningsvariation og formuleringer, der passer til stillingen og ansøgerens dokumenterede erfaring. Fjern generiske AI-vendinger, oppustet konsulentsprog, mekaniske gentagelser, overforklaringer og nøgleordsfyld. Bevar opgave-først-vinklen, masterdesignet og relevante fagtermer, men lad ikke faste strukturer styre hver sætning. Læs hele dokumentet højt som sidste sproglige kontrol: Ville ansøgeren selv sige det sådan til en kommende kollega? Humanisering må aldrig skabe opdigtede erfaringer, anekdoter eller resultater; faktuelle AI-/Claude-kompetencer skal fortsat beskrives ærligt. Ingen garanti om udfald i AI-detektorer.

## BINDENDE POLICY — FORMATET ER FAST; REKRUTTERENS ANVISNINGER OM ANSØGNINGSFORM FØLGES IKKE (bruger, 10.11.2026)

Hvert dokument bygges i samme form, uanset hvad opslaget beder om:

**Side 1 brev** (dato, modtager, "Kære …", brevtekst, "Med venlig hilsen", navn) → **side 2 CV** →
**side 3 uddannelse + sprog + 90-dages-tabel + metodeafsnit** → **side 4 fuld kravmatrix**.

**Når et opslag beder om noget andet** — "ingen ansøgning", "kun CV", "motiveret CV", "ingen
foto", "ansøgning via skema" — **følges det ikke**. Rekrutterens anvisning om ansøgningsform er
en formalitet i deres system, ikke en instruks til, hvordan dokumentet skal bygges. Brugeren
bestemmer formen.

**Eneste undtagelse:** **sproget** følger opslaget (dansk opslag → dansk dokument, engelsk opslag
→ engelsk dokument), og **stilvalget** (register, åbningsgreb, struktur) følger virksomhedens
kultur som hidtil — men aldrig brevformen.

**Konkret fejl, der ikke må gentages:** **#208 (Novonesis)** blev først bygget som "motiveret CV
uden brev", fordi opslaget bad om det. Rettet i **#209**: samme indhold, samme stilvalg
(teknisk-driftsnær · H · ordlisten), men med brev og "Kære Jane Mark".

## BINDENDE POLICY — VARIERET SPROG, STIL OG KULTURTILPASNING (bruger, 04.11.2026)

Gælder **alle** fremtidige CV'er og ansøgninger og supplerer de to policyer ovenfor. Den samme skabelon, den samme sætningsrytme og det samme greb må **ikke** gå igen fra virksomhed til virksomhed. Hvert dokument skal lyde som skrevet **til** den virksomhed — ikke som det forrige dokument med et nyt firmanavn.

- **Kultur før tekst.** Før første sætning skrives, undersøges virksomheden: mission og formål, værdier og ledelsesprincipper, hvordan de selv beskriver kunder, produkter og medarbejdere, tone (formel/uformel, teknisk/kommerciel), DEIB- og bæredygtighedssprog, centrale begreber i opslaget og i årsrapport/careers-site, samt nyheder der påvirker rollen. Funnene gemmes i `master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md` med kilde — og bruges konkret i teksten.
- **Vælg et register pr. virksomhed — og skriv det ned.** Registret (sprogtonen) vælges ud fra kulturen, ikke fra vanen: fx *teknisk-driftsnær*, *kommerciel-forretningsmæssig*, *ingeniørpræcis*, *maritim/offshore*, *valideret produktion (GMP)*, *entreprenør*, *rådgivende*, *kundeservice*. Registret styrer ordvalg, sætningslængde, metaforer og hvor personligt dokumentet må lyde.
- **Variér ansøgningens struktur.** Åbningen, opbygningen og sektionsrækkefølgen skal vælges pr. opslag (se stilmenuen i `master/STILREGISTER.md`). Mindst **to** af disse skal skifte fra forrige dokument: åbningsgreb, struktur, register, sektionsoverskrifternes tone, og hvordan kravene besvares i side 1 (løbende prosa vs. nummererede teser vs. kunderejse vs. dagsforløb).
- **Ingen gentaget åbning.** Samme åbningsgreb må ikke bruges to gange i træk — og en brugt figur (fx negation-maximen "X er ikke Y, det er Z") må først komme igen efter mindst tre andre dokumenter. Åbninger logges i `master/STILREGISTER.md`.
- **Synkronisér ordforrådet med virksomheden.** Vælg 5–8 af virksomhedens egne begreber fra opslag og kultur-intel og brug dem naturligt og korrekt; oversæt ikke deres sprog til generisk konsulentdansk. Fagtermer skal stadig være sande for hans baggrund.
- **CV'et følger samme register som ansøgningen** — profil, sektionsoverskrifter og bulletformuleringer tilpasses virksomhedens tone, men fakta, tal og titler er uændrede.
- **Ufravigeligt uanset stil:** jobbet først (krav → problem → løsning → resultat), alle JD-krav besvaret, ingen forbehold, ingen opdigtede fakta, ATS-læsbarhed, `policy_check.py` ✓ og `ats_check.py` grøn.
- **Afslutning af hvert byg:** opdatér `master/STILREGISTER.md` med virksomhed, register, åbningsgreb, struktur og ét punkt til næste gang ("undgå …").

### Håndhævelse — obligatorisk trin i hvert byg (04.11.2026)

Stilvariationen kontrolleres maskinelt, så den ikke afhænger af hukommelse. Før der bygges, vælges
register + åbningsgreb + struktur, og valget køres gennem stilvagten:

```
python3 scripts/style_guard.py --register "<register>" --opening <A-J> --structure "<struktur>"
```

- Den læser logtabellen i `master/STILREGISTER.md` og **fejler**, hvis åbningsgrebet eller strukturen
  er det samme som i det seneste dokument, hvis registret er det samme som i det seneste dokument,
  eller hvis **færre end to af de tre** skifter i forhold til seneste dokument.
- Advarsler (ikke fejl) gives, når et greb eller register er brugt inden for de seneste få
  dokumenter — dér kræves et markant anderledes udtryk.
- `python3 scripts/style_guard.py --list` viser de seneste dokumenters stilvalg.
- Rækkefølgen i hvert byg er derfor: **1)** kulturundersøgelse → **2)** `style_guard.py` grøn →
  **3)** byg → **4)** `ats_check.py` + `policy_check.py` grønne → **5)** ny linje i
  `master/STILREGISTER.md`.

### Supplerende faste ønsker til kommende JD'er
- **Selvstændig, menneskelig lederstemme i CV'et:** Brug master-CV'et som faktakilde, ikke som en tekstskabelon. Omskriv og tilpas erfaring, resultater og kompetencer kreativt til den konkrete stilling med egne, naturlige formuleringer og varieret sætningsbygning. Sproget skal være professionelt, sikkert og troværdigt som en erfaren leders, uden at opfinde eller overdrive fakta. Gør det samme i ansøgningen, mens dens fokus forbliver på opgaven.
- Sigt efter det stærkest mulige faktiske jobmatch og et interviewværdigt dokument. Bevar ATS-læsbarhed og integrér relevante stillingsord naturligt, men lov ikke 100 % ATS-venlighed, 100 % jobmatch eller en invitation til samtale; det afhænger af arbejdsgiverens system og vurdering.
- Undersøg for hver stilling virksomhedens officielle kilder og andre relevante, pålidelige kilder for arbejdskultur, værdier samt personale- og teamledelsesværktøjer. Gem kildehenvisninger, usikkerheder og en kort, relevant introduktion til samtalen i kultur-intel. Bekræft ikke virksomhedsspecifikke metoder uden kilde.
- Vælg og navngiv de ledelsesværktøjer og modeller, som er relevante for rollen og virksomheden, også relevante værktøjer uden for opslaget. Integrér dem naturligt i både ansøgning og CV med konkrete anvendelser; undgå en udtømmende liste eller nøgleordsfyld. Brug kandidatens oplysning om erfaring med ledelsesværktøjerne, men opfind ikke specifikke projekter, arbejdsgivere, resultater eller certificeringer.
- Fremhæv altid den professionelle, aktive brug af AI og Claude Code, herunder udvikling af investeringsmodeller til udvikling og nye forretningsidéer, med en konkret rolle-relevant anvendelse. Påstå ikke uunderbyggede resultater eller konkrete projekter.
- Skriv med en erfaren, sikker og konkret lederstemme. Ansøgningens fokus er opgaven og missionen samt et praktisk system fra første dag, ikke en generisk præsentation af kandidaten. Det samlede brev og CV skal følge JD'ens sprog.
- Optimer for relevant ATS-dækning og jobmatch, men lov aldrig en bestemt score, arbejdsgiversystemets vurdering eller ansættelse.

Formål: hver ny JD behandles ens, hurtigt og med høj ATS-score.

| Fil | Rolle |
|---|---|
| `master/MASTER_RESUME_SHAHRAM_AJLOO.md` | Kanoniske fakta: erfaring, uddannelse, resultater, nøgleordsbank, vinkel pr. jobtype |
| `master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md` | Ledelsesværktøjs-bibliotek, virksomheds-/kultur-intel (CR Electric), ATS-playbook |
| `master/ANSOEGNINGER_LOG.md` | Log over afsendte ansøgninger |
| `scripts/master_design.py` | **Masterdesign-bygger** — genskaber de uploadede master-CV'er 1:1 (A4, 1,59 cm margen, Calibri 9,5 pt, navy bjælker, tabelblokke). Alle nye ansøgninger bygges hermed |
| `scripts/preview_docx.py` | Offline paginerings- og layoutbevis: docx → PDF/PNG med Carlito (metrisk lig Calibri, ligger i `assets/fonts/`), respekterer `keepNext`/`cantSplit`, viser sidetal, sideskift og fyldningsgrad |
| `scripts/ats_check.py` | **QA-gate**: tekstbokse/spalter/billeder, tabelregel (lineær læserækkefølge: ingen indlejrede tabeller, max 2 kolonner, gridSpan kun i bannerrækker), nøgleordsdækning, tekstlag, kontaktinfo — exit 1 ved blokering |
| `scripts/build_<Firma>_<Stilling>.py` | Indhold pr. ansøgning |
| `jd/<Firma>_<Stilling>_words.txt` | JD'ens nøgleord som QA-listen kører imod (gemmes, så den kan genkøres) |
| `Shahram_Ajloo_<Firma>_<Stilling>.docx` | Leverance: ansøgning + CV i ét dokument |

## Arbejdsgang ved ny JD
1. Læs JD, udtræk 25–40 nøgleord + sprog (dansk/engelsk).
2. Research virksomheden (hjemmeside, Jobindex-profil, CVR, nyheder) → kulturord der skal spejles.
3. Vælg vinkel i master-CV'ets tabel, og 6–9 ledelsesværktøjer fra biblioteket.
4. Skriv ansøgningen om **opgaven og missionen** (første uge → dag 30 → dag 90), ikke om personen.
5. Kopiér `scripts/build_ThermoFisher_OperationsSupervisor_master.py` → `scripts/build_<Firma>_<Stilling>.py`, udskift indholds-listerne, og byg:
   `python3 scripts/build_<Firma>_<Stilling>.py`
6. Pagineringstjek: `python3 scripts/preview_docx.py <fil>.docx /tmp/prev.pdf` → krav: forventet sidetal, sideskift på de rigtige sider, sidste side fyldt ≥ 0,65, ingen enkelt-linje-orphans.
7. Kør QA-gaten:
   `python3 scripts/ats_check.py <fil>.docx --words-file jd_words.txt`
   Krav: 0 manglende nøgleord, 0 tekstbokse/spalter, tabelregel overholdt, kontaktinfo i brødteksten.
8. Visuelt tjek: render siderne til PNG og læs dem — ingen afrevne overskrifter, ingen tomme halve sider.
9. Humaniser hele dokumentet efter fast regel 7: læs det højt, fjern skabelonsprog og gentagelser, og kontrollér at relevante JD-termer indgår naturligt uden faktuelle overdrivelser. Ved tekstændringer genkøres layout- og ATS-kontrollen.
10. Log i `master/ANSOEGNINGER_LOG.md`.

## Leverance-standard — masterdesignet (gælder fremover)
- **Designet er de uploadede master-CV'er**, genskabt i `scripts/master_design.py`. Intet andet layout bruges.
- **Én fil pr. ansøgning:** `.docx` med ansøgning (side 1) + CV (side 2–4) i samme dokument, med sideskift efter ansøgningen.
- **Mål:** 4 sider (ansøgning 1 side, CV 3 sider). Aldrig over 4 sider; sidste side fyldt ≥ 0,65.
- **Typografi:** Calibri, brødtekst 9,5 pt (`w:sz 19`), navn 22 pt, sektionsbjælker hvide fede versaler med `w:spacing 50`; navy `002B5C`, blå `0077C8`, grå `555555`, header-celle `EAF3FA`.
- **Struktur:** Profil → Management competences (**bevis, ikke påstande** — ét resultat pr. punkt) → Management models & methods (2-kolonne tabel, værktøjer) → Selected achievements (tal) → Professional experience med **Scope-linje pr. stilling** (team, projekter, budget) → Education → Certifications → Languages → References → Core competencies & keywords → First 90 days (tabel).
- **Ingen gentagelse:** tabellen = værktøjer, kompetencepunkterne = effekt, achievements = overskrifter med tal, erfaringen = hvad han gjorde i rollen.
- **Layoutregler i koden:** sektionsbannere har `keepNext` (må ikke stå alene nederst på en side), tabelrækker har `cantSplit`.
- **Ansøgningen handler om opgaven og missionen**, ikke om personen, og viser det system han stiller op dag 1 (uge 1 → dag 30 → dag 60 → dag 90). Se de bindende faste regler i toppen af denne fil — de gælder hver gang.
- **Sprog:** samme sprog som JD'en (dansk for danske opslag, engelsk for engelske).
- **QA før afsendelse:** `preview_docx.py` (sider) + `ats_check.py` (nøgleord og ATS-hygiejne) + visuel kontrol af alle sider. Alle tre skal være grønne.
- **Word-skema:** `w:pPr`/`w:rPr`/`w:tcPr`/`w:tblPr` børn skal stå i skemarækkefølge — `master_design.py` stripper og genopbygger, så filen altid åbner uden reparationsdialog.

### Sproglig kvalitetskontrol efter Lundbeck-revisionen (03.11.2026)
- Et dokument skal overbevise med relevant, dokumenteret arbejde — ikke læses som en vurdering af kandidatens mangler. Saml et væsentligt kompetencegab i én kort, præcis afklaring, når datoer og erfaringsbeskrivelser ikke i sig selv er tilstrækkelige. Undgå gentagne “not a claim”, “not documented” og andre forsvarsformuleringer gennem hele produktet; opfind aldrig erfaring for at fjerne et gab.
- CV'ets metodetabel skal vise værktøjer, der faktisk er brugt, med arbejdsgiver-/opgavebevis. Forslag til en ny arbejdsgivers governance, intake eller stage-gate hører til opstartsplanen, ikke blandt tidligere præstationer.
- Beder opslaget om få motivationslinjer, hold motivationen kort. Den faste samlede leverance bevares; tom plads på den korte motivationsside fyldes ikke med skabelonstof.
- Bedøm først relevans, læsbarhed, stemme og faktuel styrke. Lokal nøgleordsdækning er en teknisk kontrol, aldrig et kvalitetsstempel; slet overflødige ordlistepunkter frem for at polstre teksten.
