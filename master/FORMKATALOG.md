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
| D | **Tallet** — et beløb, en frist eller en mængde som løftestang | "Kommunen betaler halvdelen af rådgiveren. Ikke én krone af anlægget" · AHH: "To millioner kvadratmeter — ingen leder to millioner kvadratmeter" · Jones Engineering: tre vilkår før en workface kan åbnes — released drawings, available labour/materials, agreed inspection points | #243 · Jones Engineering |
| E | **Tidsforskydningen** — beslutningen ligger uger eller år før konsekvensen | "Kontakten med spildevand bliver ikke afgjort i brønden. Den bliver afgjort ugen før" · Elos: linjen bestemmes atten måneder før maskinen ankommer | #244 |
| F | **Konsekvensen** — fejlen viser sig et helt andet sted, på et helt andet tidspunkt | Kemp & Lauritzen: el-entreprisen går ikke galt i tavlen, men seks uger senere | #239 |
| G | **Spørgsmålet** — et spørgsmål, kunden eller faget stiller | "Hvornår er en alarm en fejl, og hvornår er den en føler, der driver?" · Rigshospitalet: "Hvornår er et byggeprojekt på et hospital egentlig færdigt?" (#242) | #242 |
| H | **Dagsforløbet** — fire klokkeslæt som bevis | Køge: 07.15 kapacitet · 09.00 udvalget · 12.30 byggepladsen · 15.45 lederen | #231 · make:net 07.00 ud af døren · 9.30 kunden · 13.00 den fredede bygning · 16.15 sedlen (#241) |
| I | **Teserne** — tre påstande, der hver får sit afsnit | HVAC-salg | #220 |
| J | **Citatet fra opslaget** — deres egen overskrift besvares direkte | Bravida Entreprise Øst: opslagets »Er du den, andre projektledere ringer til, når projekterne bliver svære?« besvares med et ja og med de tre spørgsmål, han stiller (kontrakten · hvem har lovet det · hvornår blev det varslet) | #247 |
| **K** | **Modstriden** — to samtidige mål eller krav, der kun løses sammen gennem den daglige praksis | Subra: »Du bliver den tekniske tunge i organisationen og er samtidig ude ved anlæggene« → et anlæg skifter ikke ejer den dag, det idriftsættes, men den dag nogen kan køre det uden at ringe til dem, der byggede det; Gladsaxe: en skolebygning kan ikke vælge mellem lavt energiforbrug og godt indeklima | #248 · Gladsaxe Kommune |
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
| **Y** | **Holdbarheden** — en fysisk tidsgrænse i produktet fungerer som hele kædens ur | Arla: mælk har ikke en leveringsdato, men en holdbarhed — en palle, der kører tolv timer tidligere, er mere værd end en rabat, der kommer tolv timer senere | #262 |
| **Z** | **Beslutningen i den anden ende** — modpartens næste beslutning som dokumentets ur, ikke din egen leverance | DAVA Foods: en producent er ikke en leverandør, man køber æg af, men den der om få uger skal beslutte, hvor mange dyr der skal sættes i huset — ud fra det, han hørte sidste gang, nogen ringede | #263 |
| **AA** | **Ubalancen i fordelingen** — den samme ressource står stille to steder på én gang, og det er ledelsens regnestykke, ikke materiellets | Otto Chrestensen: der står to gravemaskiner i den ene grøft og ingen i den anden — det er fordelingen fra i sidste uge, ingen så efter i tirsdags | #264 |
| **AB** | **Tiden efter** — forbedringen måles ikke i workshoppen, men i den almindelige tirsdag tre måneder senere | Johnson Controls: en Kaizen-uge er let at holde af; tirsdagen tre måneder senere er prøven — nogen skal arbejde efter den nye standard uden at blive set | #265 |
| **AC** | **Beslutningen før driftsstoppet** — oppetiden afgøres af den prioritering, der træffes, mens anlægget stadig kører | Samtank: vedligeholdelsesvalget før næste fejl eller terminalvindue; sikkerhed og forsyning afgøres før arbejdet starter | Samtank |

**Ikke brugt for nylig — foretrækkes:** en åbning med en **dato i deres egen historie**, en åbning med
**et tab** (hvad koster det, når det ikke bliver gjort), en åbning med **en læsers situation** (kundens,
teknikerens, borgerens) — og et register uden for de sidste ti. **A–Z, AA og AB** er nu brugt mindst én gang — næste åbning skal være **AC**, eller et af de ubrugte greb nedenfor (**en dato i deres egen historie**, **en kundes beslutningsøjeblik**, **et nej, der blev givet i tide**). Tilbage som reelt ubrugte greb: **en dato i deres egen historie**, **en kundes beslutningsøjeblik** (den dag de valgte leverandør) og **et nej, der blev givet i tide**.

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
| **Choose it, contract it, steer it — or end it** | fire faser i en leverandørs livscyklus, inkl. exit — beslutningsmaterialet · aftalen · den ugentlige styring · re-udbud og overdragelse (Arla, EN) | #262 |
| **Besøget** | fire dele af ét besøg, hver med sit krav til forberedelse og opfølgning — tallene før du kører · stalden · referatet · næste sæson (DAVA Foods, DA) | #263 |
| **Fire steder, pengene afgøres** | fire faser fra opslagets egen sætning om sammenhængen mellem tilbud, planlægning, udførelse og økonomi — tilbuddet · planen · udførelsen · afleveringen (Otto Chrestensen, DA) | #264 |
| **After the workshop** | forbedringens fem faser med sustainment som prøven — the event · the standard · the escalation · the number · the next event (Johnson Controls, EN) | #265 |
| **Criticality → portfolio → adoption → value** | kritikalitet og vedligeholdsbasis · fælles prioritering på tværs · standard og gennemførelse · projekt-/omkostningsoverblik · dokumenteret gevinst (Samtank) | Samtank |
| **Bruger → måling → tiltag → drift** | arbejdsgangen for en bygning: brugernes signal · energidata og automatik · lille teknisk sag · effekt og overdragelse | Gladsaxe Kommune |
| **Workfront readiness → weekly control → handover** | adgang, tegninger, arbejdskraft og materialer · fast ugentlig styring af stakeholdere, tid, omkostning, kvalitet og sikkerhed · commissioning og aflevering | Jones Engineering |
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
| **The Cold Chain** (EN) | cold chain, shelf life, pallet, batch, picking, replenishment, temperature, hold, inventory accuracy | #262 |
| **Staldgangen** | stald, hus, indsætning, hold, sortering, udbytte, velfærd, tilsyn, foder, leverance | #263 |
| **Mandskabstavlen** | tavle, sjak, sag, uge, maskine, formand, lærling, omflytning, ferie, reserve | #264 |
| **The Gemba** (EN) | gemba, takt, standard work, andon, kanban, red tag, waste, huddle, cycle time, sustainment | #265 |
| **Driftskompasset** | anlægskritikalitet, vedligeholdsvindue, prioritet, reservedel, ændring, beslutningsejer, portefølje, omkostning, gevinst | Samtank |
| **Bygningspulsen** | brugere, energidata, indeklima, automatik, vedligehold, komfort, drift | Gladsaxe Kommune |
| **Package Execution** | workfront, scope, labour, interfaces, hold points, commissioning, handover, forecast | Jones Engineering |
| **Udestående** | **Markedet** (efterspørgsel, pris, konkurrent) · et register fra **borgerens breve** · et register fra **servicebilen** | — |

## Regler, der ikke kan til- eller fravælges

1. **Registeret skal kunne høres.** Læs side 1 op: kan man gætte branchen uden at se firmanavnet?
2. **CV'et arver registeret.** Samme ordforråd i sektionsoverskrifter og bullets — ikke et neutralt CV
   bag et personligt brev.
3. **Ingen form to gange i træk**, og helst ikke inden for de sidste seks dokumenter.
4. **Kulturfilen bestemmer ordvalget**, formkataloget bestemmer formen. Begge dele kontrolleres
   maskinelt før commit.

## #267 — LEGO Engineering Management System Development
- Åbning **AD**: en proces har en formel ejer og en faktisk bruger.
- Struktur **From need to trusted practice**: behov, interface, standard, afprøvning og opfølgning.
- Register **The Interface**: ownership, interface, lifecycle, backlog, feedback, adoption.

## #268 — LEGO Industrial Engineer, Prepack
- Åbning **AE**: pakkeinstruktionens første bruger og det ubesvarede spørgsmål.
- Struktur **From product to pack**: krav, data, instruktion, implementering og læring.
- Register **The Packing Instruction**: packing instruction, production data, factory, product requirements, implementation, improvement.

## #269 — LEO Pharma Maintenance Support Professional
- Åbning **AF**: holde anlægget kørende og bevare dokumentationen under overgang.
- Struktur **Keep running, close responsibly**: drift, fejlsøgning, evidens, overgang.
- Register **The Maintenance Record**: maintenance, root cause, corrective action, GxP, CMMS, QMS, close-down.
- CV med integreret motivation; intet følgebrev, jf. opslaget.

## #269 revision — LEO Pharma Maintenance Support
- Åbning **AG**: den eksisterende fabrik skal forblive driftssikker under overgangen.
- Struktur **Keep, investigate, transition**: driftssikkerhed, teknisk undersøgelse og opfølgning, kontrolleret overgang.
- Register **The Shift Handover**: anlæg, fejl, evidens, åbne handlinger, ejer, overdragelse.

## #272 — Aalborg Portland Mechanical Supervisor
- Åbning **AH**: forberedelse inden et planlagt stop.
- Struktur **Før-stop-under-efter**: arbejdsomfang og ressourcer, sikker udførelse, opfølgning og læring.
- Register **Vedligeholdsordren**: arbejdsordre, rekvisition, reservedele, mekanikere, inspektion, stop og sikkerhed.

## #273 — MME Nordic Product Manager
- Åbning **AI**: en produktionsplatform vurderes af både slutbrugerens behov og fabrikkens virkelighed.
- Struktur **Fra brugerbehov til platform**: kundeindsigt, produktanalyse, teknologivalg, scenarie, roadmap.
- Register **Produktbeslutningen**: behov, segment, materiale, proces, antagelse, risiko og prioritering.

## #274 — LIEWOOD Operations & Logistics Team Lead
- Åbning **AJ**: én leverancekæde, selv når to teams og et lager deler arbejdet.
- Struktur **One flow, two teams**: prioritet/backup, inbound/outbound-overdragelse, afvigelser/forenkling.
- Register **The Daily Flow**: handover, capacity, priority, owner, delivery window, exception, next action.

## Vestas Field Operations Team Leader — req. 75708
- Åbning **AK**: deployment-planen er kun troværdig, når mennesker er klar og støttet.
- Struktur **People, readiness, deployment**: trivsel og udvikling, compliance og kompetencer, bemanding og opfølgning.
- Register **The Readiness Conversation**: skills, availability, country requirements, wellbeing, 1:1, deployment, budget, follow-up.

## Nykredit Run Operations Lead — revision 04.11.2026
- Åbning **Fejlen i overdragelsen**: driftsstop bør ikke starte med en jagt på løsningens ejer.
- Struktur **Overblik, aftale, kontrol**: portefølje og ejere, tværgående driftsaftale, kontroller og læring.
- Register **Driftsaftalen**: overdragelse, ansvar, miljø, adgang, hændelse, eskalation, støtte og forbedring.

## Weibel — Produktionsleder, elektronikproduktion
- Åbning **Det næste skift**: den voksende produktion skal kunne overtage en plan, der holder.
- Struktur **Plan, signal, forbedring**: kapacitet og bemanding, data og afvigelser, handling og opfølgning.
- Register **Fra afvigelse til kapacitet**: skifteoverdragelse, ordrestatus, flaskehals, kvalitetskontrol, baseline, ansvar og effekt.

## Valcon — Associate Partner, Operational Transformation
- Åbning **The four-way commitment**: én kundetransformation kræver kompetencer, relationer, levering og en service, der udvikles.
- Struktur **Shape, deliver, expand**: behov og baseline, leverance og kompetencer, relation og udvikling.
- Register **From decision to measurable change**: process, baseline, scope, owner, adoption, pipeline, handover, outcomes.

## Aluline — Produktionsleder, anodisering — revision
- Åbning **Emnet på kanten**: et CNC-bearbejdet emne repræsenterer allerede værdi før anodisering.
- Struktur **Sikker drift, sporbar kvalitet, læring**: plan og anlæg, afvigelser og kundekrav, sikker kompetenceopbygning.
- Register **Badet og emnet**: bad, kontrol, dosering, titrering, lagtykkelse, tolerancer, sporbarhed, kassation, bemyndigelse.

## EICO — Teknisk chef — revision
- Åbning **Når fejlen står i køkkenet**: kundens behov er en løsning, ikke en intern overdragelse.
- Struktur **Afklar, løs, lær**: produkt og installation, teknisk løsning og kommunikation, gentagne fejl og forbedringer.
- Register **Fra sag til løsning**: typeskilt, symptom, sagsansvar, svartid, servicepartner, garanti, reservedel, fejlkode.

## COWI — Technical Lead, Substation Automation, 61798
- Åbning **The handoff between systems**: den samlede stationsløsning afhænger af klare tekniske grænseflader.
- Struktur **Interfaces, evidence, readiness**: ejere og grænseflader, krav og leverancer, sikkerhed og teknisk klarhed.
- Register **The interface record**: scope, interface, dependency, deliverable, owner, requirement, issue, site authorisation.

## NNE — Director for PLC Systems, req5144
- Åbning **Seventy people, one delivery**: saml ledere og specialistkompetencer om kvalitet og leverance.
- Struktur **Direction, capacity, capability**: strategi og prioriteringer, projektressourcer, faglig udvikling.
- Register **The capability bridge**: leadership rhythm, project demand, competence, capacity, specialists, controls, validation.

## Royal Unibrew — Teamleder Filling Faxe, req3180
- Åbning **Sikkerhed før start**: prioriteringer skal kunne ses i hvert skift.
- Struktur **Sikker start, stabilt skift, læring**: bemanding og risiko, standard og performance, fælles forbedring.
- Register **Dagens linje**: skift, tavlemøde, opfølgning, standard, afvigelse, ansvarlig, sikkerhed, kvalitet.

## Fairpris — Head of Service
- Åbning **Efter installationen**: kunden mærker løsningens værdi, når den fungerer og får støtte.
- Struktur **Lyt, saml, forbedr**: kunderejse, fælles sagsansvar, feedback og systemforbedring.
- Register **Service der følger med**: kontakt, sag, ejer, support, eskalation, tilbagemelding, svartid, kundeoplevelse.

## Dalux — Development Team Lead
Opening **Quality and growth together**: dependable construction software depends on decisions, quality and team growth. Structure **Align, enable, improve**. Register **Delivery through people**: product trio, trade-offs, capacity, 1:1s and developer experience.

## Palsgaard — Electrician Maintenance Manager — 03.11.2026
- Åbning **AD — Driftsprøven**: stabil drift bevises i den almindelige produktionsdag efter vedligeholdet, ikke ved selve indgrebet.
- Struktur **Signal → prioritering → udførelse → læring**: fra afvigelse/planlagt arbejde til beslutning, sikker eksekvering, dokumenteret lukning og tilbageføring til PM/KPI.
- Register **Elvedligeholdets kontrolsløjfe**: tavle, fejl, arbejdsordre, eftersyn, dokumentation, kompetence, oppetid.
- Kulturankre: Palsgaards egne “Loyalty - Responsibility - Commitment”, “Heart working people”, kunde-/kvalitets-/sikkerheds-/energisprog; kulturfil i `jd/Palsgaard_ElectricianMaintenanceManager_kultur.txt`.

## Danfoss / DEVI — Senior Manager, Product Management, Req 52521 — 03.11.2026
- Åbning **AE — The product promise is decided before launch**: the installed thermostat/heating cable is the final output of upstream portfolio, customer, price, design, sourcing and launch choices.
- Struktur **Customer evidence → portfolio choices → launch readiness → in-market performance**: buyer/user/installer signal to the portfolio bet, stage gates and post-launch review.
- Register **The Product Decision Record**: segment/customer, need, competitive evidence, product option, case, price/margin, owner, gate, manufacturing/sourcing readiness, launch and in-market value.
- Kulturankre: DEVI product quality/technical expertise/long-term reliability; Danfoss LEAP 2030, Leading Portfolio, Customers & Growth, Innovative Solutions, customer partnership and electrification language. Intel §59.

## Jones Engineering — Electrical Supervisor, Copenhagen, 145572 — 03.11.2026
- Opening **AG — output accepted, not merely installed**: electrical productivity is a finished, inspected and traceable installation, not cable physically laid.
- Structure **Ready to build → install to specification → prove and tag → hand over to commissioning**.
- Register **The Tagged Circuit Record**: area/system, revision, contractor, workfront, inspection point, tag, test, snag, owner and commissioning status.
- Explicit qualification note: Danish LV/MV/HV authorisation is not presented as BS 7671, C&G 2391/2394/2395, SSSTS/SMSTS, ECS/Safety Passport or First Aid; candidate chose transparent application. Intel §57.

## Prinfo / partner — produktionsleder
- Åbning **Fra ordre til levering**: prioriteringer, kvalitet og distribution for en mindre virksomhed.
- Struktur **Planlæg, følg op, forbedr**: mennesker og kapacitet; kvalitet og ansvar; forbedring med ejerleder.
- Register **Sikker drift og bedre flow**: ordre, vagtplan, kapacitet, underleverandør, kvalitet, likviditet og levering.

## PRONOR — Servicechef / afdelingsleder KBH
- Åbning **Når anlægget stopper**: industrikundens behov for sikker og stabil drift.
- Struktur **Lyt, prioritér, følg til dørs**: sagsbillede, ansvar, udførelse og vækst.
- Register **Fra driftsstop til drift**: anlæg, teknikere, reservedele, værksted, fejl, tilbagemelding, kvalitet.

## Gentofte Ejendomme — driftsleder
Åbning **Når brugeren åbner døren** tager afsæt i velfungerende rammer; struktur **Retning, råderum, relationer** for selvstyrende team og brugere; register **Bygninger der fungerer i hverdagen** med lokation, vedligehold, budget, forventningsafstemning og fagligt råderum.

## Nexel — manager kundeprojekter — revision
Åbning **Når en kunde skal tilsluttes**: sammenhæng mellem aftale, netprojekt og aflevering. Struktur **Fælles retning, fælles metode, sikker aflevering**. Register **Fra kundeaftale til dokumenteret net**: kapacitet, projekt, entreprenør, økonomi, dokumentation og sikkerhed.

## Siemens Energy — Head of Primary Engineering 306962
Opening **A safe substation is designed as a system**; structure **People, interfaces, assurance**; register **The primary engineering interface**: capacity, design authority, interfaces, verification, risk and engineering hubs.

## DIS/CREADIS — senior stærkstrømsingeniør
Åbning **Forbindelsen til elnettet**; struktur **Krav, valg, verificering**; register **Fra netkrav til verificeret anlæg**: tilslutning, tekniske grænseflader, dokumenterede designvalg og test.

## Aceve / KlarPris — Development Lead
Opening **The tradesperson waits for the answer**: practical price/material information during a working day. Structure **Clarify, build, learn**; register **From request to trusted delivery**: acceptance, backlog, dependencies, people, migration, AI quality and stakeholder updates.

## Coor Property — driftschef / Operations Manager
Åbning **Den drift kunden mærker**: ejendomsleverancen skal understøtte kundens kerneforretning; struktur **Retning, indsigt, handling**; register **Leverancen mellem mennesker og aftaler**: teamledere, kunde, kontrakt, forecast og opfølgning.

## Coor Property — revideret driftschefansøgning
Åbning **Den aftalte leverance**; struktur **Hold, kunde, forretning**; register **Ledelse gennem ansvar**. Konkret opfølgning på medarbejdere, aftaler, sikkerhed, økonomi og forbedringer uden at fremstille forslag som etablerede processer.

## Coor Property — ny opbygning
Åbning **Når ejendommen fungerer**; struktur **Hold, kunde, økonomi**; register **Driftschefens beslutninger**. Konkrete handlinger om beslutningsrum, kundeaftaler og forecast; forslag til første tre måneder.

## Coor Property — selvstændigt CV
Tosidet CV: relevant profil, ledelse og driftsansvar, kronologisk erhvervserfaring, uddannelse og metoder. Fokus på dokumenterede ansættelser og generelt bekræftede kompetencer.

## Coor Property — genopbygget CV
To sider, enkelt spalte uden tabeller; korte tekstafsnit og punkter, klar kronologi og dokumenterede resultater. Ingen ansøgning eller 90-dagesplan i CV'et.

## Coor Property — masterformat genoprettet
Uploadet `Resume.pdf` som visuel reference: kombineret ansøgning og CV, navy bannere, blå punkttegn, lederprofil, kompetencer og erhvervshistorik. Konkrete opgaveforslag adskilt fra dokumenteret erfaring.

## Coor Property 398149 — sammenhæng i driften
Navy masterformat; jobfokuseret brev med tre korte faglige afsnit om ledelse, kundeaftale og økonomi; separat CV med erfaring, uddannelse og handlingsforslag.

## Københavns Kommune — varmeforsyning
Klar, saglig myndighedsstil i masterformat. Fire punkter fra datagrundlag til proces og samarbejde; CV med overførbar teknisk dokumentation, økonomi og el-/varmeforståelse.

## København — varmeforsyning, master-CV-genopbygning
Ansøgningens arbejdsforløb: sagsoplysning, samfundsøkonomi, myndighed og politisk behandling, fagligt samarbejde og borgerdialog. CV'et bruger masterdesign og uddyber dokumenteret teknik, tal og projektleverancer.

## Mølleåværket — drift i samspil med udvikling
Masterbanner og blå punkter; brev om driftsfællesskab, sikkerhed, myndighedskrav, vedligehold og økonomi; CV med relevant renseanlægsdrift og personaleledelse.

## Mølleåværket — genopbygget efter tidligere CV
Masterformat, jobfokuseret handlingsbrev og uddybet CV med kompetencer, erfaring, uddannelse og fremadrettede prioriteringer.

## Mølleåværket — RegionH FaglederProjekterRH-reference
Fire sider: brev, profil og rolle/styringsmodel/resultater, erfaring og uddannelse, 90-dagesplan og samarbejde; samme navy/blue design og tabelform som referencen.

## Mølleåværket — professionelt sprog
RegionH-form beholdt; CV'ets kompetencer, resultater og erhvervserfaring formuleret mere naturligt og direkte efter brugerens kritik.

## Mølleåværket — genfremsendt stillingsopslag
Jobrettet ansøgning, CV-profil, kompetencer, styringstabel og dokumenterede resultater efterfulgt af erhvervserfaring og foreslået 90-dagesplan i RegionH-format.

## Arla — regional demand planning
Brev med beslutningsrytme og konkrete opgaver, CV med overførbar erfaring, foreslået planlægningsmodel og 90-dagesplan; navy masterformat.

## Mølleåværket — drift og ledelse
Fornyet brev, CV og praktisk 90-dagesplan efter brugerens kritik; dokumenteret erfaring adskilt fra foreslået indsats i navy RegionH-design.

## Vestforbrænding — HaloSep
Brev om sikker, stabil procesdrift og holdledelse, CV med relevante dokumenterede erfaringer, planlægningsmodel og 90-dagesforslag i navy masterformat.

## Baringa — Nordic Power Market Advisory
Investeringsbeslutningen som åbning, rådgivningstabel pr. klientspørgsmål, dokumenteret teknisk/ledelsesmæssig erfaring og praktisk introduktionsplan i masterformat.

## NIRAS — maskinteknisk rådgivning
Brev organiseret efter analyse, komponentvalg, sikker udskiftning og vedligehold; CV med overførbar teknisk erfaring og foreslået projektforløb i masterformat.

## Philips — District and Country Leader
Joborienteret engelsksproget brev og CV med praktisk kommerciel ledelsesramme og foreslået 90-dagesplan i masterformat; ingen opdigtede medtech-salgscases.

## Johnson & Johnson — Site Contracting EMEA
Tre sider med jobrettet brev, CV og kompakt handlingsramme for kontraktlevering i masterlayout. Forslag til legal/compliance-samarbejde adskilt fra faktisk teknisk erfaring.

## Bavarian Nordic — Automatiktekniker
To-siders CV med indledende motivation og praktisk supporttabel; ingen separat ansøgning, i overensstemmelse med stillingsopslaget. Svendebrev separat og ikke fremstillet.

## Bavarian Nordic — Drug Substance Engineering Specialist
To-siders målrettet CV med overførbar idriftsættelseserfaring og separat markeret fremadrettet ramme for GMP, ekspertstøtte og teknisk samarbejde.

## Kirby — Electrical Construction Manager
Tre siders ansøgning og CV; praktiske byggepladsrutiner og fasetabel frem for generiske ledelsesudsagn. Konkrete dokumenterede projektbeløb i DKK, uden påstand om EUR 5 mio.-erfaring.

## Factbird — Engineering Manager
Tre siders jobfokuseret ansøgning og CV med menneskeledelse og AI-assisteret udvikling; foreslået ledelsesmodel og dokumenterede resultater holdes adskilt.
