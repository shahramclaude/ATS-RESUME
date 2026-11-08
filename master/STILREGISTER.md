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
| **Kundeservice/rekruttering** | menneske først, relation, responstid, tillid | serviceafdelinger, kundecentre, HR-nær ledelse | teknisk tunge afsnit |

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

**Aktuel spærring (opdateret efter #185):** åbningsgreb **B (negation-maxime)** er fri igen (tre
dokumenter er gået), men de sidste fire har brugt **I, J, F** og tidligere **G** — brug B kun, hvis intet
andet passer. Til næste byg foretrækkes **H (dagsforløbet)** eller **A/E (placen/tidsforskydningen)** med
en ny vinkel. Struktur: de sidste seks er *Målestokken, Ordlisten, Komponentens vej, Snitfladerne* plus
ældre — til næste byg foretrækkes **Kunderejsen**, **Teserne** eller **Problemkatalog** med ny vinkel.
Register: **rådgivende** er nu brugt to gange (#174, #185) — skift udtrykket tydeligt, hvis det kommer
igen; *valideret produktion (GMP)* og *kundeservice* er de mindst brugte.

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
