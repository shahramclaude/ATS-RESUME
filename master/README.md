# Ansøgningssystem — Shahram Ajloo

Formål: hver ny JD behandles ens, hurtigt og med høj ATS-score.

| Fil | Rolle |
|---|---|
| `master/MASTER_RESUME_SHAHRAM_AJLOO.md` | Kanoniske fakta: erfaring, uddannelse, resultater, nøgleordsbank, vinkel pr. jobtype |
| `master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md` | Ledelsesværktøjs-bibliotek, virksomheds-/kultur-intel (CR Electric), ATS-playbook |
| `master/ANSOEGNINGER_LOG.md` | Log over afsendte ansøgninger |
| `scripts/ats_builder.py` | Genbrugelig docx-bygger (Calibri 9,5 pt, A4, 1 side ansøgning + CV, ATS-sikker) |
| `scripts/build_<Firma>_<Stilling>.py` | Indhold pr. ansøgning |
| `Shahram_Ajloo_<Firma>_<Stilling>.docx` | Leverance: ansøgning + CV i ét dokument |

## Arbejdsgang ved ny JD
1. Læs JD, udtræk 25–40 nøgleord + sprog (dansk/engelsk).
2. Research virksomheden (hjemmeside, Jobindex-profil, CVR, nyheder) → kulturord der skal spejles.
3. Vælg vinkel i master-CV'ets tabel, og 6–9 ledelsesværktøjer fra biblioteket.
4. Skriv ansøgningen om **opgaven og missionen** (første uge → dag 30 → dag 90), ikke om personen.
5. Byg med `python3 scripts/build_<Firma>_<Stilling>.py`.
6. Kontrollér: 1 side ansøgning, ingen tabeller, alle JD-ord findes i dokumentet, Jobindex/proceskrav overholdt.
7. Log i `master/ANSOEGNINGER_LOG.md`.
