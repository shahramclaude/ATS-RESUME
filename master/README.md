# Ansøgningssystem — Shahram Ajloo

## Faste fakta — rettelser der gælder ALLE ansøgninger (opdateret 31.10.2026)
- **Bopæl: Måløv** (Ballerup Kommune) — *ikke* Søborg. Kontaktlinjen i banneret slutter med "Måløv".
- **Titel: elautoriseret maskinmester** (LV/MV/HV) — *ikke* "autoriseret elinstallatør" / "autoriseret el-installatør". Uddannelsen er B.Tech i Technology Management & Mechanical Engineering (maskinmesterretningen), og elautorisationen er erhvervet oven på den.
- Når et opslag kræver "maskinmester eller el-installatør", skrives det som opslagets eget krav, og svaret er "elautoriseret maskinmester" — aldrig ved at påtage sig titlen elinstallatør.
- Ved tvivl: ret i `master/MASTER_RESUME_SHAHRAM_AJLOO.md`, ikke i det enkelte byggescript.

## Faste regler — gælder ALLE fremtidige ansøgninger (bindende)
1. **Dokumentet handler ikke om ansøgeren — det handler om opgaven, missionen og stillingen.** Ansøgningen (side 1) tager udgangspunkt i det, stillingen skal løse: hvad der skal lykkes, hvilke KPI'er og rammer der styrer det, og hvad der typisk går galt i den slags rolle. "Jeg"/"min" bruges kun som bevis på, at opgaven er forstået, aldrig som præsentation af personen.
2. **Dokumentet skal vise et fast greb om kravet** — hver JD-overskrift besvares med en konkret metode, et system eller et tal fra praksis, så læseren kan se, at opgaven er løst før (ikke at kandidaten er sød).
3. **Dokumentet skal vise, at systemet til dag 1 allerede er bygget:** en konkret 90-dages-plan (uge 1 → dag 30 → dag 60 → dag 90) med ejerskab, møder, målinger og leverancer — ikke hensigter. Læseren skal kunne se, hvad der sker på mandag, hvis han får jobbet.
4. Konsekvens: ingen selvbiografisk indledning, ingen "jeg er en passioneret…", ingen opremsning af personlighed. CV-delen må gerne være faktuel og taldrevet — kravet om opgavefokus gælder især ansøgningen og profilafsnittet.
5. Mangler (geografi, systemer, branche) meldes ærligt på én linje og vendes til en plan — aldrig skjult, aldrig bortforklaret.
6. **Leverancen er altid den samme, uanset hvad opslaget beder om.** Siger JD'en "kun CV", "motiveret CV", "ingen ansøgning" eller lignende, leveres stadig **ét samlet dokument: side 1 = motiveret, opgave-først side, derefter CV i masterdesignet**. CV'et tilpasses så det kan stå alene, men ansøgningssiden udelades aldrig (bruger, 31.10.2026).

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
9. Log i `master/ANSOEGNINGER_LOG.md`.

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
