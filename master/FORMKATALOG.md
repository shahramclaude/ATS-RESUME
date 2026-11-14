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
| **O** | **Fraværet** — tjenesten bemærkes kun, når den er væk | Vattenfall: »A wind farm you cannot see is a wind farm you cannot run.« — en data-koncentrator, der stopper kl. 03, gør 40 møller tavse på skærmen | #252 |
| **P** | **Review-kommentaren** — den, der ikke skrev ændringen, skal kunne svare for den | Spirii: »An agent can open the pull request. It cannot sit in the review and answer for it.« — skriveriet flytter mod agenten, ansvaret flytter mod personen | #253 |
| **Q** | **Den anden dato** — den, der ikke står i kontrakten, men i hovedet på brugeren | airteam: kontrakten kan holdes til timen og bygningen være en skuffelse — den morgen personalet møder ind i et lokalt, hvor luften er tung | #254 |
| **R** | **Den næste, der ikke ved noget** — gæsten/borgeren, hvis uvidende oplevelse er målet | Kemp & Lauritzen: kl. 06.15 kommer den første gæst; hun ved ikke, at nogen har målt vandet kl. 06.00, og hun skal ikke vide det | #255 |
| **S** | **Enheden** — gevinsten som måleenhed i stedet for beløb, procent eller dato | Evondos: et projekt måles ikke i euro, men i minutter en plejer ikke bruger på at tælle piller — og det tal skal nogen ind og kontrollere efter overdragelsen | #256 |
| **T** | **Læserens situation** — den, der står i støjen, har kravet; udbudslinjen har kun ordet | FalCom: operatøren i den støjende kabine og montøren i maskinrummet har samme problem — maskinen er højere end den, der skal give ordren | #257 |
| **U** | **Arbejdskraften** — efterspørgslen efter automatisering forklaret med bemanding, ikke teknik | Kardex: det svære i et dansk lager er ikke bygningen, men de tolv mennesker, der skal gå i den — maskinen er svaret, bemandingsproblemet er grunden | #258 |
| **V** | **Variationen** — processtabilitet forklaret som varians, ikke som hastighed | GN Hearing: den sværeste maskine er ikke den langsomste, men den der opfører sig anderledes om tirsdagen — svaret er sjældent nyt udstyr | #259 |
| **W** | **Escaleringen** — det er ikke direktørens timer, der er problemet, men antallet af gange om dagen nogen spørger ham om noget, de selv kunne have afgjort | Anonym COO (Midtjylland): vejen til direktøren går gennem alt — en pris, en leveringsdato, en reklamation, en ansættelse, et indkøb | #260 |
| **X** | **Fejlen før den blev dyr** — fejlkostnadens placering i kæden, ikke tab, fravær eller varians | Zeekr: der er ét sted i en bilforsyningskæde, hvor en fejl stadig er billig — på kajen, før registrering, klargøring og kunde | #261 |

**Ikke brugt for nylig — foretrækkes:** en åbning med en **dato i deres egen historie**, en åbning med
**et tab** (hvad koster det, når det ikke bliver gjort), en åbning med **en læsers situation** (kundens,
teknikerens, borgerens) — og et register uden for de sidste ti. A–X er nu alle brugt mindst én gang — næste åbning skal være **Y**. Tilbage som ubrugte greb: **en dato i deres egen historie**, **en kundes beslutningsøjeblik** (den dag de valgte leverandør) og **et nej, der blev givet i tide**.

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
| **The Runbook and the Roadmap** | fem temaer, hver med to dokumenter — hvad der sker i nat, og hvad der forhindrer den samme nat om to år (Vattenfall, EN) | #252 |
| **Five phrases, taken literally** | fem af opslagets egne sætninger, hver med hvad den kræver om tirsdagen — og hvordan den kan gå galt (Spirii, EN) | #253 |
| **Kanalvejen** | syv stationer fra indtag til drift, hver med sin egen måde at gå galt på — indtag · aggregat · kanaler · spjæld · rum · måling · drift (airteam, DA) | #254 |
| **Hvem opdager det først** | seks fejlkilder i den rækkefølge, de bliver opdaget — gæsten · betjeningen · elregningen · tilsynet · ingen · læreren (Kemp & Lauritzen, DA) | #255 |
| **The Gates** | seks porte fra business case til gevinst, hver med **ét dokument** der gør beslutningen mulig — business casen · planen · styregruppebeslutningen · implementeringen · overdragelsen · gevinsten (Evondos, EN; PMO'et selv som syvende afsnit) | #256 |
| **The requirement behind the requirement** | fem lag fra udbudslinjen til accepten — kravet som skrevet · kravet bag det · hvad miljøet gør ved svaret · hvad integrationen kræver · hvad accepten beviser, plus efterspillet (FalCom, EN) | #257 |
| **The payback page** | fem linjer, der hver skal overleve kundens controller — timerne · kvadratmeterne · fejlene · kapaciteten · prisen for at vente, plus siden efter underskriften (Kardex, EN) | #258 |
| **From the URS to the audit file** | seks led i udstyrslivet, hvert med sit dokument — kravet · leverandøren · udstyret · valideringen · ændringen · journalen (GN Hearing, EN) | #259 |
| **Ugen** | ugerytmen som ledelsessystem, seks faste punkter med hver sin ejer — mandag ordrebogen · tirsdag leverancerne · onsdag indkøbet · torsdag kunderne · fredag tallene · måneden ledelsen (COO, DA) | #260 |
| **Five contracts** | fem kontrakter, hver med løfte, tal og fejlmåde — logistikleverandøren · terminalen · klargøringen · forhandlernettet · transportbenet, plus den aftale man ikke kan skrive: forecastet (Zeekr, EN) | #261 |
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
| **The Data Path** (EN) | concentrator, telemetry, edge, WAN, historian, failover, backup, restore, patch window | #252 |
| **The Review** (EN) | diff, test, rollback, page, retro, person, merge, guardrail, pager | #253 |
| **Indreguleringen** | tryk, luftmængde, spjæld, måling, tolerance, afvigelse, indreguleringsrapport, det første år | #254 |
| **Badevandet** | klor, pH, bundfald, cirkulation, filter, prøve, journal, tilsyn, dosering | #255 |
| **Roll-out** | site, connection, transformer, permit, energisation | #225 |
| **Designkontor** | brief, scheme, calculation, schedule, coordination | #226 |
| **The Decision Log** (EN) | decision log, date, owner, option rejected, gate, benefit, handover, steering group | #256 |
| **The Trial** (EN) | baseline, scenario, noise, attenuation, radio, intercom, operator, acceptance, finding, report | #257 |
| **The Aisle** (EN) | aisle, bin, tote, pick, replenishment, slotting, footprint, cycle time, throughput, uptime | #258 |
| **The Line** (EN) | SMD, reflow, stencil, fixture, AOI, calibration, yield, changeover, first article, transport plate | #259 |
| **Ordrebogen** | ordre, leveringsdato, lager, pluk, fragt, reklamation, dækningsgrad, indkøb, leverandør | #260 |
| **The Quay** (EN) | quay, vessel, terminal, gate-out, VIN, PDI, prep, transport damage, storage, registration | #261 |
| **Udestående** | **Markedet** (efterspørgsel, pris, konkurrent) · et register fra **borgerens breve** · et register fra **servicebilen** | — |

## Regler, der ikke kan til- eller fravælges

1. **Registeret skal kunne høres.** Læs side 1 op: kan man gætte branchen uden at se firmanavnet?
2. **CV'et arver registeret.** Samme ordforråd i sektionsoverskrifter og bullets — ikke et neutralt CV
   bag et personligt brev.
3. **Ingen form to gange i træk**, og helst ikke inden for de sidste seks dokumenter.
4. **Kulturfilen bestemmer ordvalget**, formkataloget bestemmer formen. Begge dele kontrolleres
   maskinelt før commit.
