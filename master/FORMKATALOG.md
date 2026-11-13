# Formkatalog — åbningsgreb, strukturer og registre

Til brug ved hvert byg. Formålet er at gøre det **umuligt at gentage sig selv**: side 1 må ikke bygges
efter samme opskrift to gange i træk, og CV'ets sektionsrækkefølge og rytme skal følge samme register
som brevet.

Kontrolleres af `scripts/style_guard.py`:

```
python3 scripts/style_guard.py --register "<register>" --opening <bogstav> --structure "<struktur>"
```

Kravet er **mindst 2 af 3 skift** mod det senest loggede dokument i `master/STILREGISTER.md`, og
`--register` skal være et, der ikke er brugt i de sidste seks dokumenter.

## Åbningsgreb (side 1, første sætning)

| Kode | Greb | Eksempel fra arkivet | Sidst brugt |
|---|---|---|---|
| A | **Placeringen** — kvaliteten afgøres et andet sted, end man tror | Artelia: ombygningen afgøres ikke på byggepladsen, men i den uge nogen skal lukke en kanal | #238 |
| B | **Negationen** — det er ikke X, der vælter noget; det er Y | "Det er ikke gravemaskinen, der vælter en separatkloakering; det er analysen" · Sukup: det er ikke montagen, der vælter et kundeprojekt, men tilbuddet og kalenderen | #246 |
| C | **Stedet** — beslutningen tages kl. 06.30 ved tavlen | City Container: kl. 06.15 på pladsen i Farum | #235 |
| D | **Tallet** — et beløb, en frist eller en mængde som løftestang | "Kommunen betaler halvdelen af rådgiveren. Ikke én krone af anlægget" · AHH: "To millioner kvadratmeter — ingen leder to millioner kvadratmeter" | #243 |
| E | **Tidsforskydningen** — beslutningen ligger uger eller år før konsekvensen | "Kontakten med spildevand bliver ikke afgjort i brønden. Den bliver afgjort ugen før" · Elos: linjen bestemmes atten måneder før maskinen ankommer | #244 |
| F | **Konsekvensen** — fejlen viser sig et helt andet sted, på et helt andet tidspunkt | Kemp & Lauritzen: el-entreprisen går ikke galt i tavlen, men seks uger senere | #239 |
| G | **Spørgsmålet** — et spørgsmål, kunden eller faget stiller | "Hvornår er en alarm en fejl, og hvornår er den en føler, der driver?" · Rigshospitalet: "Hvornår er et byggeprojekt på et hospital egentlig færdigt?" (#242) | #242 |
| H | **Dagsforløbet** — fire klokkeslæt som bevis | Køge: 07.15 kapacitet · 09.00 udvalget · 12.30 byggepladsen · 15.45 lederen | #231 · make:net 07.00 ud af døren · 9.30 kunden · 13.00 den fredede bygning · 16.15 sedlen (#241) |
| I | **Teserne** — tre påstande, der hver får sit afsnit | HVAC-salg | #220 |
| J | **Citatet fra opslaget** — deres egen overskrift besvares direkte | Bravida Entreprise Øst: opslagets »Er du den, andre projektledere ringer til, når projekterne bliver svære?« besvares med et ja og med de tre spørgsmål, han stiller (kontrakten · hvem har lovet det · hvornår blev det varslet) | #247 |
| **K** | **Modstriden** — deres egen sætning vendes: den er styrken, og den er præcis risikoen | Subra: »Du bliver den tekniske tunge i organisationen og er samtidig ude ved anlæggene« → et anlæg skifter ikke ejer den dag, det idriftsættes, men den dag nogen kan køre det uden at ringe til dem, der byggede det | #248 |
| **L** | **Nummeret / dokumentet** — der er kun et stillingsnummer at holde i hånden, og det flytter brevet over på opgaven | Anonym produktionsvirksomhed via erwin andersen a/s: »02.11.88.« som første ord, fordi navnet er anonymt og opgaven ikke | #249 |
| **M** | **Tabet** — hvad det koster, når det ikke bliver gjort; kundens tab er uret, ikke vores responstid | Advansor: »A rack that stops on a Saturday does not cost a service technician. It costs a display case full of food.« | #250 |
| **N** | **Historien** — et faktum fra deres egen historie vendes til det operative spørgsmål | Volvo Truck Center: »80 år« — den eneste lastbil, der ikke udvikler noget, er den, der står på liften | #251 |

**Ikke brugt for nylig — foretrækkes:** en åbning med en **dato i deres egen historie**, en åbning med
**et tab** (hvad koster det, når det ikke bliver gjort), en åbning med **en læsers situation** (kundens,
teknikerens, borgerens) — og et register uden for de sidste ti. A–N er nu alle brugt mindst én gang.

## Strukturer (hvordan kravene besvares i brevet)

| Struktur | Formen | Sidst brugt |
|---|---|---|
| Beslutningskæden | trigger → survey → estimate → window → eksekvering | #221 |
| Snitfladerne | fem grænseflader, hver med sit afsnit (Artelia: driften · brugerne · projekteringen · entreprenøren · myndigheden og brand) | #238 |
| **Regnestykket** | en økonomi som fem linjer, hver med sit afsnit (K&L: timerne · materialerne · underentreprenøren · risikoen · dækningsgraden) | #239 |
| **Before / in twelve months** | seks linjer "i dag → om tolv måneder", hver med et bevis (Hitachi Energy: decision rights · capacity · one standard · competence · delivery quality) | #240 |
| Målestokken | hvert afsnit åbner med et tal fra virksomheden | #219 |
| Kunderejsen | aftalen · projekteringen · entreprisen · tilslutningen · økonomien | #218 |
| Problemkataloget | fire navngivne problemer i driften, hver med løsning | #223 |
| Før/efter | seks linjer "i dag → om 12 måneder" | #222 |
| **Ordlisten** | seks ord, opgaven består af, hver med et afsnit (AHH: retning · prioritering · snitflade · opfølgning · tillid · stedfortræder) | #243 |
| Teserne | tre til fem påstande om faget | #225 |
| Dokumentrækken | ét dokument pr. afsnit (plan, liste, protokol, mappe) | #232 |
| **Fejltilstandene** | hvad der går galt, og hvad der fanger det (make:net: montøren uden materiale · kunden ringer og ingen hjemme · opgaven vokser · dokumentationen kommer for sent · montøren holder op med at sige noget) | #241 |
| **Ugen** | mandag → fredag med et bevis pr. dag | #229 |
| **To veje** | den dyre og den billige løsning, og hvornår man vælger hvilken | #233 |
| **Budgetlinjen** | hver post i en beslutning, og hvem der ejer den | #231 |
| **Analysens fire spørgsmål** | de fire ting en analysefase skal svare på, i rækkefølge | #234 |
| **De fem tal** | de fem KPI’er der styrer en drift, hver med sit afsnit og sin metode (Elos: tid til produktion · udbytte/scrap · cyklustid · changeover/oppetid · antal opkald til engineering) | #244 |
| **Spørgsmålene kunderne stiller** | fem spørgsmål i rækkefølge, hvert med sit afsnit og sit svar | #237 |
| Faserne | brief · scheme · detailed · tender · installation · commissioning | #227 |
| **Kontrakten, kalenderen, kassen og folkene** | fire snit gennem stillingen — tilbud og risiko · kapacitet og kalender · margin og efterkalkulation · ledelse af projektlederne (Sukup) | #246 |
| **Fordelingen af ansvar** | fem ting der skal fordeles, før et projekt kan lykkes — beslutningen · grænsefladen · afbrydelsen · pengene · afleveringen (Rigshospitalet) | #242 |
| **Dokumentrækken (variant 2)** | ét dokument pr. afsnit, men dokumenterne er rollens egne — mødeprotokollen · tidsplanen · tillægssagen · projektstatusen · sparringssamtalen (Bravida Projekt Supporter) | #247 |
| **Fem overtagelser** | fem dage, hvor et anlæg skifter ejer — prøvekørslen · nøglebundtet · den første alarm · det første år · bygningen (Subra, utility/facility) | #248 |
| **Køen** | virksomheden som fem køer, hver med ejer, tid og pris — ordren · tegningen · indkøbet · værkstedet · ændringen (teknisk chef) | #249 |
| **The route of a case** | én sag gennem fem stationer, hver med sin egen fejlmåde — the call · the diagnosis · the claim · the commissioning · the learning (Advansor, EN) | #250 |
| **Det samme og det forskellige** | fem ting der skal være ens på to enheder, og det der ikke skal — retning · tal · ledere · kunde · sikkerhed (Volvo, to værksteder) | #251 |
| **Udestående — brug snart** | en struktur bygget på **en uge i kalenderen** · en struktur bygget på **en beslutningsdagbog** · en struktur bygget på **en fordeling af ansvar** | — |

## Registre (sproget og verdensbilledet)

| Register | Kendetegn | Sidst brugt |
|---|---|---|
| Teknisk-driftsnær | klokken, vejret, brønden, telefonen | #222 |
| Kundeservice | kunden, teknikeren i bilen, koordinatoren | #223 |
| Maritim/offshore | regime, port call, dry dock, window | #221 |
| Kommerciel | margin, ordrebog, kunde, krone | #220 |
| Konstruktionsbord | komponenter, tryk, temperatur, enheder | #219 |
| Entreprenør | byggeplads, fremdrift, akkord, aflevering | #218 |
| **Rådgivende** | projekteringsgrundlag, standard, myndighed, review | #227 |
| Valideret produktion (GMP) | validering, afvigelse, sporbarhed, audit | #216 |
| Uptime/kontrolrum | alarm, redundans, runbook, kontrolrum | #215 |
| **Forvaltning** | pulje, tilsagn, afhøring, lokaludvalg, politisk behandling | #224 |
| **Maskinrummet** | last, kapacitet, margin, spidsbelastning | #229 |
| **Lærerens** | facitliste, pensum, oplæg, rettelse | #230 |
| **Borgerens** | hverdag, tillid, kerneopgave, naboskab | #231 |
| **Laboratoriet** | hypotese, prøve, reference, reproduktion | #232 |
| **Afløbets** | tærskel, overløbshyppighed, målepunkt, tørvejr | #233 |
| **Ledningsgraven** | grøft, brønd, boring, TV-inspektion, skel, indkørsel | #234 |
| **Pladsen** | plads, vogn, last, hjul, værksted, skift, reservedel | #235 |
| **Sæsonen** | frost, tø, sætning, klipning, løvfald, beredskab, materiel, rute | #237 |
| **Etaperne** | etape, omlægning, midlertidig løsning, afspærring, adgang, vandafbrydelse, spændingsløs, genopretning | #238 |
| **Akkorden** | akkord, styk, opmåling, tildeling, akkordbrev, regulering, merarbejde, sjak, formand, dækningsgrad | #239 |
| **Switchyard** | bay, feeder, busbar, breaker, interlock, AIS/GIS, energisation, outage window | #240 |
| **Servicebilen** | vogn, kasse, materiale, rute, udkald, seddel, timer — montørens dag i syv ord | #241 |
| **Driftsvinduet** | afbrydelse, varsling, sluse, støjzone, midlertidig forsyning, tilbagekobling, driftsejer | #242 |
| **Driftsdøgnet** | vagt, udkald, alarm, responstid, eskalering, logbog, overlevering | #243 |
| **Valideringen** | URS, FAT/SAT, IQ/OQ/PQ, afvigelse, change control, sporbarhed | #244 |
| **Anlægget** | silo, tørrer, transportør, kapacitet, høst, montage, idriftsættelse, aflevering | #246 |
| **Byggemødet** | dagsorden, referat, aktion, frist, mangel, besigtigelse, garanti, tillægssag, tidsfristforlængelse | #247 |
| **Anlægskortet** | anlægsnummer, kritikalitet, interval, målepunkt, alarmgrænse, reservedel, leverandør, serviceaftale | #248 |
| **Tegnestuen** | revision, snit, tolerance, stykkliste, frigivelse, ændringsseddel, målestok | #249 |
| **The Rack** (EN) | rack, gas cooler, compressor, discharge pressure, alarm, controller, refrigerant | #250 |
| **Værkstedshallen** | løftebord, fejlkode, reservedel, servicetime, oppetid, kapacitet, tavle | #251 |
| **Roll-out** | site, connection, transformer, permit, energisation | #225 |
| **Designkontor** | brief, scheme, calculation, schedule, coordination | #226 |
| **Udestående** | **Markedet** (efterspørgsel, pris, konkurrent) · et register fra **borgerens breve** · et register fra **servicebilen** | — |

## Regler, der ikke kan til- eller fravælges

1. **Registeret skal kunne høres.** Læs side 1 op: kan man gætte branchen uden at se firmanavnet?
2. **CV'et arver registeret.** Samme ordforråd i sektionsoverskrifter og bullets — ikke et neutralt CV
   bag et personligt brev.
3. **Ingen form to gange i træk**, og helst ikke inden for de sidste seks dokumenter.
4. **Kulturfilen bestemmer ordvalget**, formkataloget bestemmer formen. Begge dele kontrolleres
   maskinelt før commit.
