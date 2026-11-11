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
| B | **Negationen** — det er ikke X, der vælter noget; det er Y | "Det er ikke gravemaskinen, der vælter en separatkloakering; det er analysen" | #234 |
| C | **Stedet** — beslutningen tages kl. 06.30 ved tavlen | Lachenmeier | #212 |
| D | **Tallet** — et beløb, en frist eller en mængde som løftestang | "Kommunen betaler halvdelen af rådgiveren. Ikke én krone af anlægget" | #224 |
| E | **Tidsforskydningen** — beslutningen ligger uger eller år før konsekvensen | "Kontakten med spildevand bliver ikke afgjort i brønden. Den bliver afgjort ugen før" | #233 |
| F | **Konsekvensen** — fejlen viser sig et helt andet sted, på et helt andet tidspunkt | "A cable schedule that is one circuit short… fails eleven months later, on a Friday" | #227 |
| G | **Spørgsmålet** — et spørgsmål, kunden eller faget stiller | "Hvornår er en alarm en fejl, og hvornår er den en føler, der driver?" | #232 |
| H | **Dagsforløbet** — fire klokkeslæt som bevis | Køge: 07.15 kapacitet · 09.00 udvalget · 12.30 byggepladsen · 15.45 lederen | #231 |
| I | **Teserne** — tre påstande, der hver får sit afsnit | HVAC-salg | #220 |
| J | **Citatet fra opslaget** — deres egen overskrift besvares direkte | Fjernvarme Fyn: opslagets eget spørgsmål citeres og besvares | #229 |
| **K** | **Modstriden** — deres egen sætning vendes: den er styrken, og den er præcis risikoen | ABC: "I har ikke ret meget 'sådan plejer vi at gøre'" → en afdeling, der er gået fra 1 til 30, mangler ikke rutine, den mangler en facitliste | #230 |

**Ikke brugt for nylig — foretrækkes:** K (modstriden), J (citatet/deres eget sprog), en åbning med et **dokument**
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
| Dokumentrækken | ét dokument pr. afsnit (plan, liste, protokol, mappe) | #232 |
| **Fejltilstandene** | hvad der går galt, og hvad der fanger det | #230 |
| **Ugen** | mandag → fredag med et bevis pr. dag | #229 |
| **To veje** | den dyre og den billige løsning, og hvornår man vælger hvilken | #233 |
| **Budgetlinjen** | hver post i en beslutning, og hvem der ejer den | #231 |
| **Analysens fire spørgsmål** | de fire ting en analysefase skal svare på, i rækkefølge | #234 |
| Faserne | brief · scheme · detailed · tender · installation · commissioning | #227 |
| **Udestående — brug snart** | **Spørgsmålene kunden stiller** (fem spørgsmål i rækkefølge) · en struktur bygget på **et regnestykke** · en struktur bygget på **en uge i kalenderen** | — |

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
| **Roll-out** | site, connection, transformer, permit, energisation | #225 |
| **Designkontor** | brief, scheme, calculation, schedule, coordination | #226 |
| **Udestående** | **Markedet** (efterspørgsel, pris, konkurrent) · et register fra **borgerens breve** · et register fra **en byggepladsdagbog** | — |

## Regler, der ikke kan til- eller fravælges

1. **Registeret skal kunne høres.** Læs side 1 op: kan man gætte branchen uden at se firmanavnet?
2. **CV'et arver registeret.** Samme ordforråd i sektionsoverskrifter og bullets — ikke et neutralt CV
   bag et personligt brev.
3. **Ingen form to gange i træk**, og helst ikke inden for de sidste seks dokumenter.
4. **Kulturfilen bestemmer ordvalget**, formkataloget bestemmer formen. Begge dele kontrolleres
   maskinelt før commit.
