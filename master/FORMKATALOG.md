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
| A | **Placeringen** — kvaliteten afgøres et andet sted, end man tror | "A charging station is not decided on the plot… at the grid connection" | #225 |
| B | **Negationen** — det er ikke X, der vælter noget; det er Y | "Det er ikke anlægget, der vælter en serviceafdeling" | #223 |
| C | **Stedet** — beslutningen tages kl. 06.30 ved tavlen | Lachenmeier | #212 |
| D | **Tallet** — et beløb, en frist eller en mængde som løftestang | "Kommunen betaler halvdelen af rådgiveren. Ikke én krone af anlægget" | #224 |
| E | **Tidsforskydningen** — beslutningen ligger uger eller år før konsekvensen | "Kontakten med spildevand bliver ikke afgjort i brønden. Den bliver afgjort ugen før" | #222 |
| F | **Konsekvensen** — fejlen viser sig et helt andet sted, på et helt andet tidspunkt | "A cable schedule that is one circuit short… fails eleven months later, on a Friday" | #226 |
| G | **Spørgsmålet** — et spørgsmål, kunden eller faget stiller | "Hvor mange steder kan en komponent skiftes, uden at nogen skal regne efter?" | #219 |
| H | **Dagsforløbet** — fire klokkeslæt som bevis | GMOS-DK 07:15 → 21:00 | #221 |
| I | **Teserne** — tre påstande, der hver får sit afsnit | HVAC-salg | #220 |
| J | **Citatet fra opslaget** — deres egen overskrift besvares direkte | Danfoss: "Vil du skabe resultater gennem mennesker?" | #213 |

**Ikke brugt for nylig — foretrækkes:** J (citatet/deres eget sprog), en åbning med et **dokument**
(fx "På side 14 i jeres udbud står…"), en åbning med en **modstrid** ("I skriver X; virkeligheden på
pladsen er Y"), eller en åbning med en **dato i deres egen historie**.

## Strukturer (hvordan kravene besvares i brevet)

| Struktur | Formen | Sidst brugt |
|---|---|---|
| Beslutningskæden | trigger → survey → estimate → window → eksekvering | #221 |
| Snitfladerne | kunden · teknikken · tilbuddet · kontrakten · driften | #220 |
| Målestokken | hvert afsnit åbner med et tal fra virksomheden | #219 |
| Kunderejsen | aftalen · projekteringen · entreprisen · tilslutningen · økonomien | #218 |
| Problemkataloget | fire navngivne problemer i driften, hver med løsning | #223 |
| Før/efter | seks linjer "i dag → om 12 måneder" | #222 |
| Ordlisten | seks ord, opgaven består af, hver med et afsnit | #224 |
| Teserne | tre til fem påstande om faget | #225 |
| Faserne | brief · scheme · detailed · tender · installation · commissioning | #226 |
| Dokumentrækken | ét dokument pr. afsnit (plan, liste, protokol, mappe) | #211 |
| **Udestående — brug snart** | **Fejltilstandene** (hvad der går galt, og hvad der fanger det) · **Ugen** (mandag → fredag med et bevis pr. dag) · **To veje** (den dyre og den billige løsning, og hvornår man vælger hvilken) · **Spørgsmålene kunden stiller** (fem spørgsmål i rækkefølge) · **Budgetlinjen** (hver post i en beslutning, og hvem der ejer den) | — |

## Registre (sproget og verdensbilledet)

| Register | Kendetegn | Sidst brugt |
|---|---|---|
| Teknisk-driftsnær | klokken, vejret, brønden, telefonen | #222 |
| Kundeservice | kunden, teknikeren i bilen, koordinatoren | #223 |
| Maritim/offshore | regime, port call, dry dock, window | #221 |
| Kommerciel | margin, ordrebog, kunde, krone | #220 |
| Konstruktionsbord | komponenter, tryk, temperatur, enheder | #219 |
| Entreprenør | byggeplads, fremdrift, akkord, aflevering | #218 |
| Rådgivende | projekteringsgrundlag, standard, myndighed | #217 |
| Valideret produktion (GMP) | validering, afvigelse, sporbarhed, audit | #216 |
| Uptime/kontrolrum | alarm, redundans, runbook, kontrolrum | #215 |
| **Forvaltning** | pulje, tilsagn, afhøring, lokaludvalg, politisk behandling | #224 |
| **Roll-out** | site, connection, transformer, permit, energisation | #225 |
| **Designkontor** | brief, scheme, calculation, schedule, coordination | #226 |
| **Udestående** | **Laboratoriet** (prøve, usikkerhed, reproducerbarhed) · **Maskinrummet** (last, kapacitet, margin) · **Markedet** (efterspørgsel, pris, konkurrent) · **Borgerens** (hverdag, tillid, naboskab) · **Lærerens** (kompetence, oplæring, prøve) | — |

## Regler, der ikke kan til- eller fravælges

1. **Registeret skal kunne høres.** Læs side 1 op: kan man gætte branchen uden at se firmanavnet?
2. **CV'et arver registeret.** Samme ordforråd i sektionsoverskrifter og bullets — ikke et neutralt CV
   bag et personligt brev.
3. **Ingen form to gange i træk**, og helst ikke inden for de sidste seks dokumenter.
4. **Kulturfilen bestemmer ordvalget**, formkataloget bestemmer formen. Begge dele kontrolleres
   maskinelt før commit.
