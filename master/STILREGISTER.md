# Stilregister — sprog, struktur og åbninger pr. ansøgning

**Formål:** forhindre at alle ansøgninger lyder ens. Bindende krav: se `master/README.md` →
*BINDENDE POLICY — VARIERET SPROG, STIL OG KULTURTILPASNING (bruger, 04.11.2026)*.

Hvert byg **starter** med at læse denne fil (hvad er brugt for nylig?) og **slutter** med at
skrive en ny linje i tabellen nederst (hvad blev brugt nu?). Valget skal desuden være kørt
gennem `scripts/style_guard.py` (se punkt 4b), før dokumentet bygges.

---

## 1. Før skrivning — kulturundersøgelse (obligatorisk, 10 minutter)

Skriv svarene ned i `master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md` med kilde:

1. **Mission/formål** — hvordan beskriver de selv, hvorfor de findes? (careers-site, årsrapport, "about")
2. **Værdier og ledelsesprincipper** — er der navngivne værdier, leadership principles, code of conduct?
3. **Sprogtone** — formel eller uformel? teknisk eller kommerciel? kort eller fortællende? (læs 2–3 af deres egne tekster, ikke kun opslaget)
4. **Deres egne begreber** — 5–8 ord de bruger om sig selv, kunderne, produktet, medarbejderne (fx "profitable growth", "ét Bravida", "mission-critical", "value creation")
5. **Hvad de er stolte af / presset på** — nyheder, strategi, tal de fremhæver, kriser de taler om
6. **Rollenes KPI-sprog** — hvilke mål nævnes i opslaget, og hvilke måleenheder bruger de?
7. **Kultur-signaler om ledelse** — DEIB, sikkerhed, bæredygtighed, læring, "remote/flexible", fagforening, tone om fejl

8. **Sproglig synkronisering** — hvilke **5–8 af deres egne ord** skal bære dokumentet, og hvilken
   af deres sætninger om missionen skal brevet svare på? Skriv begge dele ned, før første afsnit
   skrives. Oversæt ikke deres sprog til generisk konsulentdansk.
9. **Formen** — hvilke **seks formgreb** skal være anderledes end sidst: åbningsgreb, struktur,
   kadencer, sektionsoverskrifternes tone, måden kravene besvares på i side 1, og hvordan CV'et
   spejler registret? Mindst to af de tre loggede valg (register, åbning, struktur) skal skifte.

**Beslut derefter tre ting og skriv dem i byggets docstring:** register, åbningsgreb, struktur.

---

## 2. Stilmenu — registre (vælg ét pr. virksomhed)

| Register | Lyder som | Passer til | Undgå |
|---|---|---|---|
| **Teknisk-driftsnær** | kort, konkret, "klokken tre om natten"-nærhed | drift, service, vedligehold, forsyning | strategi-jargon, konsulentord |
| **Kommerciel-forretningsmæssig** | tal, margin, kunde, beslutning | salg, indkøb, forretningsudvikling, P&L | teknik-dybde uden pointe |
| **Ingeniør-præcis** | definitioner, grænseflader, tolerancer, standarder | rådgivning, projekt, kvalitet, compliance | følelser, billedsprog |
| **Maritim/offshore** | regime, værvindue, sikkerhed, besætning | offshore, vind, marine, service-kampagner | landjordens metaforer |
| **Valideret produktion (GMP)** | dokumentation, sporbarhed, afvigelse, "nul kritiske fund" | pharma, medico, fødevare, kvalitet | "hurtigt og smidigt" |
| **Entreprenør** | byggeplads, fremdrift, kalkulation, håndværk | udførende bygge/el/VVS, totalentreprise | corporate-engelsk |
| **Rådgivende** | udbud, beslutningsgrundlag, interessent, leverance | rådgiverhuse, PMO, programmer | "vi bygger det selv"-tone |
| **Produktionslinje (takt og kapacitet)** | takt, udsyn, bemanding, gennemløb, spild, efterkalkulation | serieproduktion, byggefirmaer, ferieboliger, montage, kapacitetsstyring | strategi-jargon og "visioner" |
| **Kundeservice/rekruttering** | menneske først, relation, responstid, tillid | serviceafdelinger, kundecentre, HR-nær ledelse | teknisk tunge afsnit |
| **Uptime/kontrolrum** | responstid, eskalering, alarm, hvem tager telefonen, det første kvarter | mission-critical drift, kundesites, servicekontrakter | strategi-sprog, "visioner", følelser |

## 3. Stilmenu — åbningsgreb (skal skifte hver gang, se log nedenfor)

| # | Greb | Eksempel på form |
|---|---|---|
| A | **Placen/misplaceringen** — beslutningen tages et andet sted, end man tror | "En offshore-kampagne bliver afgjort på lageret, længe før den bliver afgjort på havet." |
| B | **Negation-maximen** — "X er ikke Y, det er Z" | "En serviceafdeling bliver ikke bygget af et organisationsdiagram." |
| C | **Stedet først** — byen/anlægget som præmis | "I Kalundborg er bygherren ikke en tilfældig kunde." |
| D | **Tallet** — ét konkret tal som indgang | "Fjorten mennesker i drift har ikke brug for en plan, der holder hele året." |
| E | **Tidsforskydningen** — beslutningen ligger før/efter det, man tror | "Et udbud bliver afgjort, længe før tilbuddene kommer ind." |
| F | **Konsekvensen** — hvad der sker, når det svigter (konkret tab) | "Det, der mangler, når lugen lukkes, koster en sejlads — ikke en telefonsamtale." |
| G | **Spørgsmålet** — ét skarpt spørgsmål, som rollen skal svare på | "Hvem ejer snitfladen mellem to fag, når ingen af dem har mandatet?" |
| H | **Dagsforløbet** — en time/dag i rollen, minut for minut | "Klokken 06.40 står lastbilen i porten, og ingen har lukket den ind." |
| I | **Teserne** — 3–5 påstande, som dokumentet beviser én for én | "Tre ting afgør den her rolle: … " |
| J | **Brevet** — direkte tiltale til den ansættende leder, uden om rammen | "Kære [navn], I skriver, at …" (kun hvor tonen er uformel) |

## 4. Stilmenu — strukturer for side 1

| Struktur | Form | Passer til |
|---|---|---|
| **Beslutningskæden** | følg én beslutning fra udløser til konsekvens | indkøb, projekt, kvalitet, strategi |
| **Dagsforløb/ugen** | kronologi: mandag morgen → fredag eftermiddag | drift, service, vagt, produktion |
| **Problemkatalog** | "de tre ting der går galt" + løsning pr. punkt | ledelse, turnaround, opbygning |
| **Kunderejsen** | telefon → tilbud → udførelse → faktura → genkøb | service, salg, kundeansvar |
| **Målestokken** | hver sektion åbner med et tal og hvad det betyder | KPI-tunge roller, forbedring |
| **Før/efter** | afdelingen i dag vs. om 12 måneder, punkt for punkt | opbygningsroller, chefforløb |
| **Teserne** | 4–5 teser med bevis og resultat | senior-roller, rådgivning |
| **Ordlisten** | virksomhedens egne begreber oversat til praksis | stærk kultur/genkendelig retorik |

---

## 4b. Maskinkontrol — `scripts/style_guard.py`

Stilvalget kontrolleres, før dokumentet bygges:

```
python3 scripts/style_guard.py --register "<register>" --opening <A-J> --structure "<struktur>"
python3 scripts/style_guard.py --list        # de seneste dokumenters valg
```

Hård fejl: samme åbningsgreb eller struktur som seneste dokument · samme register som seneste
dokument · færre end to af de tre skiftet. Advarsel: greb/register/struktur brugt inden for de
seneste få dokumenter (kræver et markant anderledes udtryk). Exitkode 1 = vælg om, før der bygges.

## 5. Log — hvad er allerede brugt (nyeste nederst)

| PR | Virksomhed | Register | Åbningsgreb | Struktur side 1 | Undgå næste gang |
|---|---|---|---|---|---|
| #173 | Atea Danmark (Team Manager, Hardware Ops) | Teknisk-driftsnær | D (tallet: 14) | Problemkatalog | tal-åbning, "fjorten mennesker" |
| #174 | Artelia (Projektleder Energi & Industri) | Rådgivende | E (tidsforskydning: udbud) | Beslutningskæden | udbud/tidlig-beslutning |
| #175 | Kirby Group Engineering (Electrical Supervisor) | Entreprenør | B (negation: "ikke fra site office") | Beslutningskæden | negation-maxime, "whiteboard" |
| #176 | Bravida (Afdelingschef, tværfaglig enhed) | Entreprenør | C (stedet først: Kalundborg) | Problemkatalog | sted-åbning, "snitflader" |
| #177 | Vestas (Team Lead Warehouse, OFS Campaign) | Maritim/offshore | A (placen: lageret, ikke havet) | Dagsforløb | "besluttet et andet sted end man tror" |
| #178 | Bravida (VVS-serviceleder, Kalundborg) | Entreprenør/kundeservice | B (negation: organisationsdiagram) | Før/efter | negation-maxime (igen), "opbygning fra nul" |
| #179 | Siemens Gamesa (Functional Lead, Procurement) | Kommerciel | B (negation: prismødet) | Beslutningskæden | negation-maxime (tredje gang), prismøde |
| #181 | Bravida (Projektchef, stor el-entreprise, Brøndby) | Kommerciel-forretningsmæssig | G (spørgsmålet: hvornår tabes pengene) | Målestokken som tidslinje (uge 1 → fase 2 → aflevering) | spørgsmålsåbning, tidslinje-struktur, "en ændring er en gave" |
| #182 | Siemens (Project Manager, Electrification & Automation, Ballerup) | Ingeniør-præcis | I (teserne: tre ting afgør leverancen) | Ordlisten (maturation → Ballerup) | tese-åbning, opslagsværksstruktur, engelsk |
| #184 | 2Refurb (CTO, Silkeborg + Council Bluffs) | Teknisk-driftsnær | J (brevet: deres egen sætning besvares) | Komponentens vej (intake → return to service) | brev-åbning, processtruktur, vind-komponenter uden vind-erfaring |
| #185 | Siemens Energy (Senior Technical PM, Substations, Ballerup/Vejle) | Rådgivende | F (konsekvensen: hvornår går datoen tabt) | Snitfladerne rollen ejer (SLD → pladsen) | konsekvens-åbning, snitflade-struktur, BEK 1608 som ramme |
| #186 | Jesper Hansen VVS (Afdelingsleder, Brøndby) | Kundeservice/rekruttering | H (dagsforløbet: 6.40 → 16) | Kunderejsen (telefon → genkøb) | dagsforløbs-åbning, kunderejse, VVS uden VVS-uddannelse |
| #187 | Domea (Driftsleder, Rødovre) | Entreprenør (møde- og planstyret) | E (tidsforskydningen: beslutning et år før opgaven) | Før/efter (i dag → om 12 måneder) | tidsforskydnings-åbning, før/efter-struktur, beboerdemokrati som metode |
| #188 | GreyBird Pilot Academy (Planlægning og produktion, Kolind) | Maritim/offshore (regime, vinduer, rækkefølge) | D (tallet: 12 fly, 13 på vej, 40 instruktører, 200 studerende, syv baser) | Teserne (fem påstande om planlægning) | tal-åbning, tese-struktur, luftfart uden flyveerfaring |
| #189 | Cavendish Hydrogen (Project Manager, Project & Service, Herning) | Valideret produktion (GMP) | A (placen: stationen tabes i overdragelsesmappen, ikke på pladsen) | Dokumenterne (kontrakt → baseline → risikoregister → acceptprotokol) | placerings-åbning, dokumentstruktur, hydrogen uden hydrogen-erfaring |
| #190 | Hempel (Solutions Project Manager, Kongens Lyngby) | Kommerciel-forretningsmæssig | C (stedet: Kongens Lyngby — kunden køber et tal, ikke maling) | Målestokken (37 · 0 · 11 · 40 % · 5/12/14/25 · 20+) | sted-åbning, målestok-struktur, marine/coatings uden brancheerfaring |
| #191 | Zalaris (Country operations, Managed Services Denmark) | Teknisk-driftsnær | B (negationen: lønkørslen bedømmes ikke den dag pengene lander) | Problemkatalog (tre ting der går galt i en månedslukning) | negations-åbning, problemkatalog, payroll uden payroll-erfaring |
| #192 | Cembrane/Ovivo (Maintenance Technician, Lynge) | Ingeniør-præcis | F (konsekvensen: ovnen stopper ikke ved ovnen) | Ordlisten (oppetid · PM · sporbarhed · serviceaftaler · reservedele) | konsekvens-åbning, ordliste-struktur, membranfabrik uden SiC-erfaring |
| #193 | Bolls ApS (El-sikkerhedsspecialist, Stenløse) | Rådgivende | G (spørgsmålet: hvilken standard gælder?) | Beslutningskæden (kravafklaring → standard → måling → rapport → CE) | spørgsmåls-åbning, beslutningskæde, testcenter uden IEC/TRF-erfaring |
| #194 | Stryhns Gruppen A/S (Teamleder, vedligehold, Havnsø) | Entreprenør | H (dagsforløbet: kl. 06.10 står en pakkelinje stille) | Før/efter (seks par: nedbrud · opgavefordeling · viden · vagtplan · KPI) | dagsforløbs-åbning, før/efter-struktur, fabrik uden fødevareerfaring |
| #195 | Dines Jørgensen & Co. A/S (VVS-/HVAC-ingeniør, Hillerød) | Rådgivende | E (tidsforskydningen: afgjort før tegningen) | Snitfladerne (seks grænseflader i en renovering) | tidsforsyndings-åbning, snitflade-struktur, rådgiverrolle uden VVS-installatøruddannelse |
| #196 | Secma (Teamlead, medicoteknisk service, Skævinge) | Kundeservice | I (teserne: tre ting afgør, om sagen løses i dag) | Kunderejsen (henvendelse → afklaring → udførelse → afslutning → næste gang) | tese-åbning, kunderejse, serviceværksted uden medicoteknisk erfaring |
| #197 | VEKS I/S (Energiplanlægger, Glostrup/Køge) | Kommerciel-forretningsmæssig | D (tallet: tolv kommuner hæfter solidarisk) | Beslutningskæden med ny vinkel (potentiale → pris → projektforslag → beslutningsgrundlag → udrulning) | tal-åbning, økonomisk beslutningskæde, energiplanlægger uden varmeplan-erfaring |
| #198 | VEKS I/S (Projektleder, Projekt, Glostrup) | Valideret produktion (GMP) | B (negation: et projekt styres ikke af sin tidsplan) | Komponentens vej som anlæggets vej (behov → grundlag → plan → kontrakt → udførelse → aflevering) | negation-åbning, anlæggets vej, projektleder uden certificering |
| #199 | Kalundborg Forsyning (Projektleder, anlæg, Kalundborg) | Teknisk-driftsnær | C (stedet først: Kalundborg og symbiosen) | Målestokken (hver sektion åbner med et tal) | steds-åbning, tal-struktur, forsynings-PM uden bygherreerfaring |

**Aktuel spærring (opdateret efter #209):** de sidste seks dokumenter har brugt **J** (#203),
**E** (#204), **D** (#205), **I** (#206), **H** (#207/#208) og **F** (#209). Til næste byg:
**A**, **B** eller **C** — de greb, der har ligget længst væk. Struktur: *målestokken* (#209),
*ordlisten* (#207/#208), *før/efter* (#206) og *beslutningskæden* (#205) er brugt for nylig;
foretræk **Teserne**, **Kunderejsen**, **Problemkatalog** eller **Beslutningskæden** med ny
vinkel. Register: *ingeniør-præcis* (#209), *teknisk-driftsnær* (#207/#208), *rådgivende* (#206)
og *GMP* (#205) skal hvile. Næste gang vælg **kommerciel** (#190, #197), **kundeservice**
(#186, #196), *entreprenør* (#200), *produktionslinje* (#201) eller *maritim/offshore* (#203).

**Note om Siemens-familien:** tre ansøgninger i alt (#179 Siemens Gamesa, #182 Siemens A/S); skift
register og åbning igen næste gang — samme koncern læser måske flere af dem.

**Note om Bravida-serien:** samme arbejdsgiver er nu dækket tre gange med tre forskellige registre
(#176 entreprenør/sted-åbning, #178 entreprenør-kundeservice/negation, #181
kommerciel-forretningsmæssig/spørgsmål). Ved næste Bravida-opslag: brug **ikke** ét af de tre
registre igen, og skift både åbning og struktur — ellers ligner ansøgningerne hinanden i rekrutterens
indbakke.

**Sprog:** de sidste fire dokumenter har alle åbnet i en rytme med to korte led og en tilspidsning.
Næste dokument skal have en anden kadence — fx længere, mere fortællende sætninger i side 1 og
kortere, hug-agtige sætninger i CV'et (eller omvendt), afhængigt af virksomhedens tone.
| #200 | H. Skjøde Knudsen (Projektchef, totalentrepriser, Sjælland) | Entreprenør | A (placen/misplaceringen: beslutningen tages i kalkulation og projektering) | Ordlisten (ordholdenhed · ordentlighed · åben, sund dialog · frihed under ansvar · købmandskab) | ordliste efter virksomhedens egne værdiord, kalkulations-åbning, totalentreprise uden projektcheferfaring i skala |
| #201 | Skanlux Byggefirma (Produktionschef, Nykøbing Falster) | Produktionslinje (takt og kapacitet) — nyt register | F (konsekvensen: en stille håndværker koster en families sommer) | Problemkatalog (fire ting der går galt, hver med pris, løsning og bevis) | konsekvens-åbning, problemkatalog, serieproduktion af unikke huse uden produktionscheftitel |
| #202 | Fortrolig klient via UnikRecruitment (Operations & Project Manager, København) | Ingeniør-præcis | G (spørgsmålet: hvem ejer snitfladen, når detaljen ikke kan bygges som tegnet) | Snitfladerne (fem grænseflader, hver med en definition af "færdig") | spørgsmåls-åbning, snitflade-struktur, indretning uden brancherfaring — og bevidst ulig Skanlux-brevet (#201) til samme rekrutterer |
| #203 | Eaton (Data Center Project Manager, EMEA Projects, København — engelsk opslag) | Maritim/offshore | J (brevet: direkte tiltale, første sætning er en påstand om hvornår projektet er afgjort) | Dokumenterne (seks dokumenter fra scope baseline til handover pack — ét dokument pr. afsnit, hvert med bevis) | dokument-åbning, dokumentrække som struktur, engelsk EMEA-datacenter-PM uden hands-on DC-erfaring (mission critical-ækvivalens i stedet) |
| #204 | Vertiv (Project Manager, Norway/Nordics, Drangedal/Kristiansand — engelsk opslag) | Uptime/kontrolrum — nyt register | E (tidsforskydningen: den sidste uge afgøres i den første) | Dagsforløbet/ugen (mandag 06.40 → fredag 15.00 på kundepladsen, hver dag slutter i et bevis) | uge-struktur i engelsk, klokkeslæt som virkemiddel, norsk arbejdstilladelse uden visumsponsorering |
| #205 | Cellerator / Novo Nordisk Fonden (Teknisk driftsansvarlig, Facility, Lyngby — dansk opslag) | Valideret produktion (GMP) | D (tallet: syv dage — vagttelefonen har man en uge ad gangen) | Beslutningskæden (alarm 02.40 → eftersyn → service → dokumentation i SAP/DALUX-FM → strategi ugen efter) | tal-åbning, beslutningskæde i drift, DALUX-FM og tilkaldevagt som dokumenteret erfaring |
| #206 | Novafos (Maskiningeniør, driftsoptimering og udvikling af vandforsyningen, Hørsholm) | Rådgivende | I (teserne: tre ting afgør, om en optimering bliver til noget i driften) | Før/efter (vandforsyningen i dag → om tolv måneder, seks par) | tese-åbning, før/efter-struktur, PowerBI uden PowerBI-erfaring (Excel + egne AI-værktøjer) |
| #207 | Novonesis (Maskinmester, Technical Support, Bagsværd og Nørrebro) | Teknisk-driftsnær | H (dagsforløbet: 06.50 → 15.10 på fabrikken) | Ordlisten (Day One Readiness · masterdata · KLS og eltekniske standarder · reservedelslister · Maskindirektivet · overlevering) — hvert begreb er et tidsstempel | **FEJL: brevformen blev droppet, fordi opslaget bad om "ingen ansøgning". Rettet i #208 — se policy 10.11.2026.** |
| #208 | Samme opslag, rettet (Novonesis, Bagsværd og Nørrebro) | Teknisk-driftsnær | H (dagsforløbet 06.50 → 15.10, nu som brev til Jane Mark) | Ordlisten (samme seks begreber som tidsstempler i dagen) | brevform genindført, "Kære …" og "Med venlig hilsen", samme indhold og samme stilvalg |
| #209 | Resident Engineer, hyperscale datacenter-campus, Fredericia (kunde ikke navngivet) | Ingeniør-præcis | F (konsekvensen: en punch list er udskudte beslutninger, ikke fejl) | Målestokken (5 levels · 0 non-conformances · 1 drawing at a time · 14 trades · 37 projects · 24 hours) | konsekvens-åbning, tal-struktur, hyperscale uden hyperscale-erfaring, engelsk MEP-acceptrolle |
| #210 | NOV Subsea Production Systems (Project Quality and Risk Engineer, Brøndby) | Maritim/offshore | A (placeringen: inspiceret to gange — i Brøndby og Kalundborg og på 300 m, hvor ingen kan åbne det igen) | Problemkatalog (fire navngivne problemer: kravet før produktion · NCR som korrektion · riskregister uden ejer · PQEP i en mappe) | placerings-åbning, problemkatalog, subsea uden subsea-erfaring, kvalitetsrolle uden PMI-certificering og API Q1-erfaring |
| #211 | ABC – Rådgivende Ingeniører (Fagleder, Commissioning, Glostrup) | Rådgivende | G (spørgsmålet: hvornår er en bygning færdig — og hvem besvarer det?) | Dokumenterne (Cx-planen · grænsefladelisten · testprotokollen · afvigelseslisten og afleveringsmappen) | spørgsmåls-åbning, dokumentstruktur, commissioning uden Cx-leder-titel, rådgiverrolle uden ansættelse i rådgivervirksomhed |
| #212 | Lachenmeier Monsun (Teamkoordinator, produktionen, Sønderborg — via Career/JKS) | Produktionslinje | C (stedet: beslutningen tages ved tavlen kl. 06.30, ikke i et mødelokale) | Dagsforløbet (06.30 tavlen · 09.00 flytningen · 11.30 spørgsmålet ved maskinen · 13.00 flowet · 15.00 notatet) | steds-åbning, dagsforløbsstruktur, smede-/metalværksted uden smedeerfaring, flytning til Sønderborg som forudsætning |
| #213 | Danfoss, Orbital & Gear Solutions (Supervisor, Quality, Nordborg) | Teknisk-driftsnær | J (brevet: opslagets egen overskrift "Vil du skabe resultater gennem mennesker?" besvares) | Snitfladerne (produktion · engineering · procurement og leverandører · økonomi og Cost of Quality) | brev-åbning, snitflade-struktur, 22-mands kvalitetsteam uden kvalitetsledertitel, Cost of Quality fra eget regnskab, flytning til Nordborg |
| #214 | Vestas, Nacelles Components (Process Lead, Munkebo/Szczecin — engelsk opslag) | Ingeniør-præcis | E (tidsforskydningen: samlebeslutningen tages tre år før den første nacelle samles) | Beslutningskæden (DfA → DFMEA/PFMEA → control plan og parametre → process validation → change control og maturity) | tidsforskydnings-åbning, beslutningskæde i procesudvikling, DfA/PFMEA/Windchill uden værktøjserfaring, vindmøller uden vind-erfaring |
| #215 | Banedanmark, Trafikdivisionen (Sektionschef, Banedanmarks Driftscenter, Trafiktårnet, København) | Uptime/kontrolrum | D (tallet: kundepunktlighed ved 2:59 · 75,0 % · 11,2 procentpoint — afgjort i det første kvarter) | Teserne (fem påstande: det første kvarter · to led samme sted · signalsystem som kompetenceopgave · trafikinformation som beslutning · chef uden tårn får svaret bagefter) | tal-åbning, tese-struktur, jernbane uden togledererfaring, diplomkrav nævnt som forpligtelse |
| #216 | Aeven, Datacenter Ejby, Glostrup (Operation Specialist, dansk opslag) | Valideret produktion (GMP) | B (negationen: et datacenter går sjældent ned, fordi strømmen forsvinder — Uptime Institutes 70 % menneskelige fejl) | Ordlisten (Tier III · PM · MOP/SOP/EOP · change management · on call · dokumentation/revision · energi · dansk ledet) | negations-åbning, ordliste-struktur, datacenter uden datacentererfaring, AOS nævnt som opstartscertificering |
| #217 | Banedanmark, Sikring & Strøm (Fagchef, København/Fredericia — dansk opslag) | Rådgivende | A (placen: kørestrømsanlæggets kvalitet afgøres i projekteringsgrundlaget, ikke i anlægget) | Problemkatalog (budgettet prøves først i byggefasen · læringen bliver i projektet · standarden bliver ikke brugt) | placerings-åbning, problemkatalog, kørestrøm/sikring uden jernbaneerfaring, anden Banedanmark-ansøgning |
| #218 | Nexel (Andel — driftselskab for Cerius og Radius Elnet), Sjælland (Manager, kundeprojekter 10-0,4 kV — dansk opslag) | Entreprenør | F (konsekvensen: en forkert tilslutning går ikke galt i elnettet, men i kalenderen) | Kunderejsen (aftalen · projekteringen · entreprisen · tilslutningen · økonomien · afslutningen og næste gang) | konsekvens-åbning, kunderejse-struktur, netselskab uden netdriftserfaring, 16-18-mands team som ledelse gennem fagligt ansvarlige |
| #219 | Johnson Controls (Sabroe), Holme/Aarhus (Lead Engineer, køleanlæg og varmepumper — dansk opslag) | Konstruktionsbord | G (spørgsmålet: hvor mange steder kan en komponent skiftes, uden at nogen skal regne efter?) | Målestokken (1897 · 122 °C · 95 °C · 27 MW · 2 300 m²) | spørgsmåls-åbning, målestok-struktur, produktudvikling uden produktudviklererfaring, komponent- og enhedssprog |
| #220 | Johnson Controls, Hornslet/Holme (Sales Engineer - HVAC — dansk opslag) | Kommerciel-forretningsmæssig | I (teserne: ordren vindes på driftsomkostningen, den der kan sige nej får næste opkald, service er en del af tilbuddet) | Snitfladerne (kunden · teknikken · tilbuddet · kontrakten med EPO · driften og service) | tese-åbning, snitflade-struktur, salg uden salgsværktøjer, F-gas som salgsargument |
| #221 | Johnson Controls Global Marine Service Denmark (GMOS-DK), Aarhus (Service Sales Manager, Offshore Service Sales — engelsk opslag) | Maritim/offshore | H (dagsforløbet: 07:15 navneskilt fra et skib tre dage ude, 11:40 platformingeniør, 16:20 tilbud mod havn og dok, 21:00 svar fra Singapore) | Beslutningskæden (trigger · survey · estimate · window · eksekvering og næste cyklus) | dagsforløbs-åbning, beslutningskæde, marint salg uden marine kunder, CRM som ærlig mangel |
| #222 | HOFOR, Smedeholmen, Herlev (Teamleder for Spildevand Ledninger, sektionen Spildevand Egen Drift — dansk opslag) | Teknisk-driftsnær | E (tidsforskydningen: kontakten med spildevand afgøres ugen før, ikke i brønden) | Før/efter (sikker drift · arbejdsmiljø og spildevandskontakt · spulevogne og tilsyn · digitalisering · faglighed og opkvalificering — i dag → om 12 måneder) | tidsforskydnings-åbning, før/efter-struktur, kloakledningsnet uden netdriftserfaring (ærligt: ingen spulevogn, ingen TV-inspektion), BIM og sikkerhedsgodkendelse udeladt efter brugerens beslutning |
| #223 | airteam a/s, Roskilde + Københavns Lufthavn (Service-projektleder til serviceafdelingen — dansk opslag) | Kundeservice | B (negationen: det er ikke anlægget, der vælter en serviceafdeling, men de fem minutter ingen havde planlagt) | Problemkataloget (teknikeren med et halvt svar · koordinatoren der lover en tid · det lille projekt der aldrig bliver et projekt · kunden der hører om det som en regning) | negations-åbning, problemkatalog, ventilationsbranchen uden montagefag og uden VVS-installatør, lufthavnens adgangsregler som åben mangel |
| #224 | Københavns Kommune, Klima-, Miljø- og Teknikforvaltningen, Bygningsfornyelse/MKB, Islands Brygge (Projektleder til grøn omstilling — solceller i boligforeninger, dansk opslag) | Forvaltning — nyt register | D (tallet: kommunen betaler halvdelen af rådgiveren, ikke én krone af anlægget) | Ordlisten (Solcellepuljen · den opsøgende indsats · generalforsamlingen · bag-måler · evalueringen · samarbejdet) | tal-åbning, ordliste i forvaltningssprog, solceller uden solcelleprojektering, EU-fonde og politisk-administrativt system som åbne mangler |
| #225 | Fastned, Copenhagen/Hovedstaden (Project Manager Construction Denmark — engelsk opslag, hybrid) | Roll-out — nyt register | A (placeringen: ladestationen afgøres ikke på grunden, men ved nettilslutningen og ved en kommunal skranke) | Teserne (nettilslutningen er projektet · standardstationen er produktet · et nyt land bygges af de første ti partnere · tidsplanen er en kæde af tilladelser og mennesker) | placerings-åbning, tese-struktur, elbilinfrastruktur uden e-mobilitetserfaring, DSO-ansøgning og dansk ladetilladelse som åbne mangler |
| #226 | Arup, Copenhagen (Axel Towers) — Senior Electrical Engineer, COP00005M (engelsk opslag) | Designkontor — nyt register | F (konsekvensen: en kabelliste med én kreds for lidt fejler ikke på tegningen, men elleve måneder senere på pladsen) | Faserne (brief · scheme design · detailed design · tender og entreprenørreview · installation og commissioning · people og skills network) | konsekvens-åbning, fase-struktur, 8 års projekteringserfaring og BIM-authoring som åbne mangler, rådgivermiljø uden rådgivererfaring |
| #229 | Fjernvarme Fyn, Odense (Teamleder for el-teamet — 6 automatikteknikere og 13 elektrikere, dansk opslag) | Maskinrummet — nyt register (last, margin, reservedele, spidsbelastning) | J (opslagets eget spørgsmål citeres og besvares i første linje) | Ugen (mandag planlægning · tirsdag sikker udførelse · onsdag rådighed · torsdag menneskerne · fredag opfølgning), et bevis pr. dag | citat-åbning, uge-struktur, fjernvarme/elkedler uden fjernvarme-erfaring, PET-godkendelse som åben formalitet |
| #230 | ABC – Rådgivende Ingeniører A/S, Glostrup (Fagleder, HVAC — dansk opslag, ung installationsafdeling 1 → 30 på 1,5 år) | Lærerens — nyt register (facitliste, pensum, oplæg, rettelse, kompetence) | K (modstriden: deres egen sætning om at de ikke har »sådan plejer vi at gøre« vendes — netop derfor mangler afdelingen en facitliste) | Fejltilstandene (fem navngivne fejl i projekteringen, hver med det, der fanger den) | modstrids-åbning, fejltilstandsstruktur, lærerregister, 7 års rådgiverprojektering og BIM-authorering som åbne mangler |
| #231 | Køge Kommune, Teknik- og Miljøforvaltningen (Chef for Ejendomme — 9 ledere, dansk opslag, rekruttering via Genitor) | Borgerens — nyt register (hverdag, tillid, kerneopgave) | H (dagsforløbet: 07.15 kapacitetsberegninger · 09.00 udvalget · 12.30 byggepladsen · 15.45 lederen) | Budgetlinjen (fem poster i en ejendomsbeslutning, hver med en ejer blandt de ni ledere) | dagsforløbs-åbning, budgetlinje-struktur, borgerregister, chef i politisk styret organisation som åben mangel, 9 ledere som åben mangel |
| #232 | WSA – WS Audiology, Lynge (Technical Facility Specialist med BMS-viden, dansk opslag) | Laboratoriet — nyt register (hypotese, prøve, reference, reproduktion) | G (spørgsmålet: hvornår er en alarm en fejl, og hvornår er den en føler, der driver) | Dokumentrækken (alarmlog · trendkurve · ændringslog · tjekliste · fejlrapport der bliver til en model) | spørgsmåls-åbning, dokumentrække, laboratorieregister, ATES og blokprogrammering som åbne mangler |
| #233 | Novafos A/S, Birkerød (Projektleder til overløbsbygværker — måling og renovering, dansk opslag, 9 kommuner) | Afløbets — nyt register (tærskel, overløbshyppighed, målepunkt, driftsmedarbejderens adgang) | E (tidsforskydning: overløbet sker i et skybrud i august, beslutningen tages i tørvejr i februar) | To veje (vandstandsmåler · flowmåler — og den tredje og dyreste vej: at bygge om uden at måle først) | tidsforsknings-åbning, to-veje-struktur, afløbsregister, GIS og hydraulik samt projektering af bygværker fra net-siden som åbne mangler |

**Note om formvalg (permanent instruks 04.11.2026):** formen er ikke en skabelon. Kataloget over
ubrugte åbningsgreb, strukturer og registre står i **`master/FORMKATALOG.md`**, og hvert byg skal
vælge en kombination, der ikke er brugt i de sidste seks dokumenter — kontrolleret af
`scripts/style_guard.py`. Kulturfilen `jd/<x>_kultur.txt` bestemmer ordvalget og kontrolleres af
`scripts/policy_check.py --kultur-file` (mindst 60 % af virksomhedens egne udtryk skal genfindes).

**Aktuel spærring (opdateret efter #226):** de sidste seks dokumenter har brugt **F** (#226),
**A** (#225), **D** (#224), **B** (#223), **E** (#222) og **H** (#221). Til næste byg: **G** eller
**J** — helst **G** (spørgsmålet, sidst #219). Struktur: *faserne* (#226), *teserne* (#225),
*ordlisten* (#224), *problemkataloget* (#223) og *før/efter* (#222) er brugt for nylig; foretræk
**Dagsforløb**, **Målestokken** eller **Kunderejsen** med ny vinkel. Register: *designkontor* (#226),
*roll-out* (#225), *forvaltning* (#224), *kundeservice* (#223), *teknisk-driftsnær* (#222) og
*maritim/offshore* (#221) skal hvile; næste gang vælg *produktionslinje* (#212), *valideret
produktion/GMP* (#216), *uptime/kontrolrum* (#215), *ingeniør-præcis* (#209) eller *entreprenør*
(#218). Undgå: konsekvens-, placerings-, tal- og negationsåbninger, fase-, tese-, ordliste- og
problemkatalog-strukturer samt klokkeslæt-, pulje- og spændingsmetaforik.

**Note om Johnson Controls-serien:** tre dokumenter på to dage — #219 (Sabroe/Holme, fagligt:
*konstruktionsbord · G · målestokken*, 1897/122 °C/95 °C/27 MW), #220 (HVAC-salg/Hornslet:
*kommerciel · I · snitfladerne*, F-gas/kroner/ordrebog) og #221 (marine service-salg/Aarhus:
*maritim · H · beslutningskæden*, port calls/klokkeslæt/10.000 anlæg). Alt tre skiftede hver gang, og
**intet tal og ingen formulering er genbrugt** på tværs. Til en fjerde JCI-ansøgning: register uden
for de tre, åbning uden for G/I/H og struktur uden for målestok/snitflader/beslutningskæde.

**Note om teknisk register:** #214 (*ingeniør-præcis*), #219 (*konstruktionsbord*) og #213
(*teknisk-driftsnær*) er tre beslægtede registre. Forskellen skal kunne høres: #214 taler om
grænseflader, tolerancer og standarder, #219 om komponenter, tryk, temperatur og enheder, #213 om
hvem der tager telefonen. Til endnu et teknisk opslag: vælg et register uden for alle tre, og læg
målingen et andet sted end i åbningen — fx i CV'et, ikke i side 1.

**Note om kunderejsen:** #196 og #218 deler struktur, men ikke greb. #196 var *kundeservice ·
H · rejsen som kundens møde med os*; #218 er *ent**Note om "ingen ansøgning"-fælden:** #222 (HOFOR) er anden gang et opslag bad om *kun CV* —
første gang var #207 (Novonesis), hvor brevformen blev droppet, og fejlen blev rettet i #208. Reglen
står fast: brevet er side 1, også når opslaget kalder det "et par ord om motivation". Det, der
skifter, er længden — #222 har kortere afsnit og en tidligere overgang til det praktiske.

reprenør · F · rejsen som projektets faser med
beløb, dato og entreprenør på*. Til en tredje kunderejse: læg rejsen i kundens kalender (uge for
uge), ikke i vores faser, og skift både åbning og register.

**Note om Banedanmark-serien:** to ansøgninger til samme arbejdsgiver på to dage — #216
(sektionschef, Driftscenter: *uptime/kontrolrum · D (2:59) · teserne*) og #217 (fagchef, Sikring &
Strøm: *rådgivende · A · problemkataloget*). Alt tre skiftede, og **intet tal eller nogen formulering
fra #216 er genbrugt**: #216 brugte kundepunktlighed og driftssprog, #217 bruger elektrificeringstal,
projektering og fagsprog. Til en tredje Banedanmark-ansøgning: vælg et register uden for begge,
en åbning uden for A/B/D og en struktur uden for problemkatalog/ordliste/teser/beslutningskæde, og
undgå både "2:59" og "41 → 80 procent".

**Sprog:** #214 åbnede med en tidsforskydning, #215 med et tal fra deres resultatplan, #216 med en
negation bygget på en ekstern statistik, #217 med en placering (kvaliteten afgøres et andet sted).
Næste dokument skal skifte rytme igen — fx en åbning med et spørgsmål kunden stiller, eller et
konsekvensgreb, og en kadence med længere, fortællende sætninger i side 1 og korte hug i CV'et.
