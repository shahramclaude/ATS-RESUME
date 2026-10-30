# Ansøgningssystem — Shahram Ajloo

Formål: hver ny JD behandles ens, hurtigt og med høj ATS-score.

| Fil | Rolle |
|---|---|
| `master/MASTER_RESUME_SHAHRAM_AJLOO.md` | Kanoniske fakta: erfaring, uddannelse, resultater, nøgleordsbank, vinkel pr. jobtype |
| `master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md` | Ledelsesværktøjs-bibliotek, virksomheds-/kultur-intel (CR Electric), ATS-playbook |
| `master/ANSOEGNINGER_LOG.md` | Log over afsendte ansøgninger |
| `scripts/master_design.py` | **Masterdesign-bygger** — genskaber de uploadede master-CV'er 1:1 (A4, 1,59 cm margen, Calibri 9,5 pt, navy bjælker, tabelblokke). Alle nye ansøgninger bygges hermed |
| `scripts/preview_docx.py` | Offline paginerings- og layoutbevis: docx → PDF/PNG med Carlito (metrisk lig Calibri), viser sidetal, sideskift og fyldningsgrad |
| `scripts/ats_check.py` | **QA-gate**: tekstbokse/spalter/billeder, tabelregel (lineær læserækkefølge: ingen indlejrede tabeller, max 2 kolonner, gridSpan kun i bannerrækker), nøgleordsdækning, tekstlag, kontaktinfo — exit 1 ved blokering |
| `scripts/build_<Firma>_<Stilling>.py` | Indhold pr. ansøgning |
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
- **Struktur:** Profil → Why I am applying (virksomhedens mission + kulturord) → Management competences (værktøj + resultat) → Management models & methods (2-kolonne tabel) → Selected achievements → Professional experience (titel, arbejdsgiver/datoer, bullets) → Education → Certifications & authorisations → Languages → Core keywords (ATS) → First 90 days — the system I bring (tabel).
- **Ansøgningen handler om opgaven og missionen**, ikke om personen, og viser det system han stiller op dag 1 (uge 1 → dag 30 → dag 60 → dag 90).
- **Sprog:** samme sprog som JD'en (dansk for danske opslag, engelsk for engelske).
- **QA før afsendelse:** `preview_docx.py` (sider) + `ats_check.py` (nøgleord og ATS-hygiejne) + visuel kontrol af alle sider. Alle tre skal være grønne.
- **Word-skema:** `w:pPr`/`w:rPr`/`w:tcPr`/`w:tblPr` børn skal stå i skemarækkefølge — `master_design.py` stripper og genopbygger, så filen altid åbner uden reparationsdialog.
