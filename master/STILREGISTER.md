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

**Aktuel spærring (opdateret efter #204):** de sidste seks dokumenter har brugt **C** (#199),
**A** (#200), **F** (#201), **G** (#202), **J** (#203) og **E** (#204). Til næste byg: **D**,
**I** eller **H** — de greb, der har ligget længst væk. Struktur: *dagsforløbet/ugen* (#204),
*Dokumenterne* (#203), *snitfladerne* (#202), *problemkatalog* (#201) og *ordlisten* (#200) er
brugt for nylig; foretræk **Teserne**, **Før/efter**, **Kunderejsen** eller **Beslutningskæden**.
Register: *uptime/kontrolrum* (#204), *maritim/offshore* (#203), *ingeniør-præcis* (#202),
*produktionslinje* (#201) og *entreprenør* (#200) skal hvile. Næste gang vælg **kommerciel**
(#190, #197), **rådgivende** (#185, #193, #195), **kundeservice** (#186, #196), **GMP**
(#189, #198) eller *teknisk-driftsnær* (#199) igen.

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
