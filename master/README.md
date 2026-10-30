# Ansøgningssystem — Shahram Ajloo

Formål: hver ny JD behandles ens, hurtigt og med høj ATS-score.

| Fil | Rolle |
|---|---|
| `master/MASTER_RESUME_SHAHRAM_AJLOO.md` | Kanoniske fakta: erfaring, uddannelse, resultater, nøgleordsbank, vinkel pr. jobtype |
| `master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md` | Ledelsesværktøjs-bibliotek, virksomheds-/kultur-intel (CR Electric), ATS-playbook |
| `master/ANSOEGNINGER_LOG.md` | Log over afsendte ansøgninger |
| `scripts/ats_builder.py` | Genbrugelig docx-bygger (Calibri 9,3 pt, A4, 1 side ansøgning + CV, ATS-sikker) |
| `scripts/ats_check.py` | **QA-gate**: tabeller/tekstbokse/spalter, nøgleordsdækning, tekstlag, kontaktinfo — exit 1 ved blokering |
| `scripts/build_<Firma>_<Stilling>.py` | Indhold pr. ansøgning |
| `Shahram_Ajloo_<Firma>_<Stilling>.docx` | Leverance: ansøgning + CV i ét dokument |

## Arbejdsgang ved ny JD
1. Læs JD, udtræk 25–40 nøgleord + sprog (dansk/engelsk).
2. Research virksomheden (hjemmeside, Jobindex-profil, CVR, nyheder) → kulturord der skal spejles.
3. Vælg vinkel i master-CV'ets tabel, og 6–9 ledelsesværktøjer fra biblioteket.
4. Skriv ansøgningen om **opgaven og missionen** (første uge → dag 30 → dag 90), ikke om personen.
5. Byg med `python3 scripts/build_<Firma>_<Stilling>.py` (leverer både .docx og .pdf fra samme indholdsmodel).
6. Kør QA-gaten på begge filer:
   `python3 scripts/ats_check.py <fil> --words-file jd_words.txt`
   Krav: 0 manglende nøgleord, 0 tabeller/tekstbokse/spalter, kontaktinfo i brødteksten, ansøgning = 1 side.
7. Visuelt tjek: render PDF-sider til PNG og læs dem — ingen spalter, ingen afrevne overskrifter, ingen tomme halve sider.
8. Log i `master/ANSOEGNINGER_LOG.md`.

## Leverance-standard (v2, gælder fremover)
- **To filer, samme indhold:** `.docx` (redigerbar, Workday-venlig) + `.pdf` (identisk layout, tekstlag intakt). Ansøger uploader den fil, portalen foretrækker.
- **Ansøgning = præcis 1 side**, CV = 2 sider, i alt 3 — kontrolleret både i DOCX (beregnet) og PDF (faktisk sidetal).
- **CV-struktur:** Profil → Areas of expertise (kompetenceblokke, ikke "keyword dump") → **Selected achievements** (6 dokumenterede resultater) → Professional experience med *Scope-linje* pr. job → Education → Certifications → Languages.
- **Ingen "Keywords (ATS)"-sektion længere** — nøgleordene skal stå i kontekst; det er både bedre for ATS-matchning og for et menneske, der læser.
- **Fortroligt sprog, ingen fyld:** "I have owned / I have run / documented: X" — ikke adjektiver om sig selv.
