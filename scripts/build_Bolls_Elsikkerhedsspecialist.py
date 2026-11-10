# -*- coding: utf-8 -*-
"""Bolls ApS — el-sikkerhedsspecialist, Stenløse.

Dansk opslag → dansk dokument (da-DK): ansøgning side 1, CV side 2, uddannelse + 90 dage +
fire afsnit side 3, kravmatrix side 4.

STILVALG (master/STILREGISTER.md, policy 04.11.2026; godkendt af scripts/style_guard.py,
3/3 skift mod #192):
  register      = RÅDGIVENDE — beslutningsgrundlag, leverance, interessent. Rollen er test plus
                  rådgivning, og kunden skal kunne handle på svaret. Sidst brugt #185.
  åbningsgreb   = G (SPØRGSMÅLET) — "hvilken standard gælder for det produkt, der ligger på
                  bordet?" Sidst brugt #181.
  struktur      = BESLUTNINGSKÆDEN — én beslutning følges fra kravafklaring over standardvalg,
                  måling, afvigelse og rapport til CE-mærkning og kundens næste produkt.
                  Sidst brugt #179.
  kadence       = kort spørgsmål, derefter hvad beslutningen betyder for målingen og for kunden.

Ingen opdigtede fakta: ingen erfaring med IEC 62368/60335-test, TRF-rapporter, EMC, RED eller MIL
påstås. Det dokumenterede grundlag er elautorisation LV/MV/HV, DS/HD 60364, BEK 1608,
verifikationsprotokoller (FAT/SAT, IQ/OQ/PQ), måleteknik og dokumentation i GMP-miljø.

Policy: master/README.md — jobbet først, kandidaten kun som bevis, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'El-sikkerhedsspecialist · Test, standarder og kundekontakt'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("9. november 2026")
    m.meta("Bolls ApS · El-sikkerhedsspecialist · Ved Gadekæret 11F, 3660 Stenløse")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: el-sikkerhedsspecialist — Bolls", bold=True, color='1A1A1A')
    m.para("Til direktør Kim Boll Jensen", after=70)

    # ---------------------------------------------------------------- side 1
    m.para("**Hvilken standard gælder for det produkt, der ligger på bordet?** Det spørgsmål afgør mere "
           "end selve testen: det afgør, hvilke grænseværdier der er gældende, under hvilke betingelser "
           "der skal måles, og hvad der kan skrives i den rapport, kunden sender videre til sit marked. "
           "Svarer man forkert, er det ikke en måling, der er forkert — det er hele godkendelsen, der "
           "skal laves om. Derfor er beslutningskæden i et testlaboratorium det, jeg gerne vil arbejde "
           "inde i.", after=80)

    m.para("**Kæden starter ved kravafklaringen.** Inden der bliver målt noget, skal produktet "
           "klassificeres: hvilke direktiver det er omfattet af, hvilken produktfamilie det hører til, og "
           "hvilke funktioner der gør det til noget andet, end kunden selv tror. Jeg har prøvet den "
           "samtale fra den anden side af bordet — 37 samtidige anlægsprojekter, hvor kravene skulle "
           "afklares, før udstyret blev bestilt — og ved, at den time tidligt i forløbet er den billigste "
           "i hele projektet.", after=80)

    m.para("**Derefter skal standarden læses, ikke skimmes.** Grænseværdier, tolerancer, "
           "opstilling, konditionering og undtagelser står sjældent i den paragraf, man finder først. Jeg "
           "har arbejdet efter **DS/HD 60364** og **BEK 1608**, hvor en bestemmelse ikke er en "
           "anbefaling, og hvor forskellen mellem \"bør\" og \"skal\" afgør, om anlægget må sættes i drift. "
           "Den samme disciplin vil jeg bruge på **IEC-standarder** og på at lære **TRF-rapporter** at "
           "kende — rapporter, hvor sporet fra krav til måling til konklusion skal kunne følges af en "
           "tredjemand.", after=80)

    m.para("**Målingen skal kunne forsvares.** Det betyder **kalibrering** og kendt "
           "**måleusikkerhed**, dokumenteret opstilling og en registrering, der gør prøven "
           "**reproducerbar** — også hvis kunden eller et marked spørger et halvt år senere. Jeg har sat "
           "anlæg i drift med **FAT/SAT** og **IQ/OQ/PQ**, hvor hver måling var et bilag, og hvor en "
           "måling uden **sporbarhed** ikke talte som bevis.", after=80)

    m.para("**Når et produkt ikke består, er svaret en rådgivning — ikke en dom.** Kunden skal have at "
           "vide, hvorfor det fejlede, hvor i konstruktionen årsagen sidder, og hvad der kan rettes, uden "
           "at produktet skal designes om. Jeg har stået i den samtale mange gange med en afvigelse i "
           "hånden: rodårsagsanalyse med **A3**, en konkret ændring, og en opfølgning der viser, at "
           "ændringen virkede. Det er også den slags rådgivning, der gør, at en kunde kommer igen med "
           "næste produkt.", after=80)

    m.para("**Dokumentationen er leverancen.** Rapporten er ikke et referat af dagen; den er det bevis, "
           "kunden **CE-mærker** på. Derfor skal den skrives, så den kan læses af en tekniker, en "
           "indkøber og en myndighed på samme tid — og så konklusionen står et sted, hvor ingen er i tvivl. "
           "Jeg skriver dansk til daglig, har skrevet teknisk dokumentation på engelsk i årevis, og er "
           "vant til at formidle det samme resultat til tre forskellige modtagere uden at ændre "
           "indholdet.", after=80)

    m.para("**Derfor er det et lille hus med et bredt laboratorium, jeg gerne vil ind i.** CE-mærkning, "
           "EMC, miljøtest og international **typegodkendelse** hænger sammen i den samme "
           "godkendelsesrejse, og en **el-sikkerhedstest**, der bliver lavet uden at kende naboens krav, "
           "koster kunden en runde mere. Jeg vil gerne være den, der kender både sin egen del og "
           "konsekvensen for de andre — og som på sigt kan tage **godkendelser** videre på flere områder.",
           after=80)

    m.para("**Hvad jeg kommer med.** **Elautorisation LV/MV/HV**, el- og maskinteknisk design (EQF 6), "
           "B.Tech og 20+ års arbejde med måling, fejlfinding, verifikation og dokumentation i miljøer, "
           "hvor en fejl ikke måtte blive en sag. Jeg har ikke kørt IEC 62368- eller 60335-test før, og "
           "jeg vil hellere sige det nu end finde ud af det i laboratoriet — til gengæld er vejen fra "
           "måleteknik og standardlæsning til el-sikkerhedstest kort for mig, og **EMC, RED og MIL** er "
           "netop de områder, opslaget selv peger på som den næste udvidelse.", after=80)

    m.para("Et mindre hus betyder korte beslutninger, og det passer mig: jeg har drevet egen virksomhed "
           "siden 2023, hvor der ikke var nogen, der tog beslutningen for mig. Jeg bor i Måløv, har ca. "
           "25 minutter til Stenløse og kan tiltræde snarest. Stillingen har jeg set hos TechJob.",
           after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("El- og maskinteknisk specialist med 20+ års erfaring i test, idriftsættelse og dokumentation "
           "— **elautoriseret maskinmester (LV/MV/HV)**, el- og maskinteknisk design (EQF 6), B.Tech i "
           "teknologiledelse og maskinteknik. Har verificeret og sat anlæg i drift med **FAT/SAT** og "
           "**IQ/OQ/PQ** i **GMP/FDA/EMA**-miljøer med **nul kritiske fund**, arbejdet efter **DS/HD "
           "60364** og **BEK 1608**, bygget måle- og rapporteringssystemer i **SAP ERP**, **Power BI** og "
           "**Python** — og rådgivet kunder i egen virksomhed siden 2023.", after=80)

    m.section("TEST, MÅLING OG VERIFIKATION")
    for label, body in [
        ("Verifikation og accepttest",
         "FAT/SAT og IQ/OQ/PQ på nye anlæg: protokoller skrevet før testen, målinger dokumenteret som "
         "bilag, afvigelser lukket med rodårsag — nul kritiske fund."),
        ("Måleteknik og fejlfinding",
         "Fejlfinding på motorer, styringer, frekvensomformere og følere; måling som grundlag for "
         "beslutning, ikke som formalitet, med kendt usikkerhed og kalibreret udstyr."),
        ("Standarder og grænseværdier",
         "Arbejde efter DS/HD 60364 og BEK 1608, hvor forskellen mellem \"bør\" og \"skal\" afgør, om et "
         "anlæg må sættes i drift."),
    ]:
        m.bullet(label, body, after=20)

    m.section("DOKUMENTATION OG RAPPORTERING")
    for label, body in [
        ("Sporbar dokumentation",
         "Registrering med udstyr, metode, resultat og tid, så prøven kan reproduceres af en anden; "
         "afvigelser dokumenteret og lukket med A3 og rodårsagsanalyse."),
        ("Rapporter, der kan bruges",
         "Leverancepakker og afleveringsdokumentation skrevet til tre modtagere samtidig: teknikeren, "
         "indkøberen og myndigheden — med konklusionen ét sted."),
        ("Data og systemer",
         "Rapportering bygget i SAP ERP, Power BI og Python; over 40 % produktivitetsløft ved at flytte "
         "rutinearbejde ind i systemet."),
    ]:
        m.bullet(label, body, after=20)

    m.section("KUNDER, RÅDGIVNING OG ANSVAR")
    for label, body in [
        ("Rådgivning til kunder",
         "Primær kontakt i hele leverancen: hvad der fejler, hvorfor, og hvad der kan rettes uden at "
         "designe produktet om — formidlet så en ikke-specialist kan handle på det."),
        ("Selvstændigt ansvar",
         "Fuldt P&L-ansvar siden 2023, 5 elektrikere og 3 lærlinge; beslutninger taget tæt på kunden "
         "uden en mellemleder."),
        ("Mindre team, fælles ansvar",
         "Vant til at arbejde i små enheder, hvor man ikke kan henvise videre — og hvor den faglige "
         "retning bliver til i samtalen, ikke i et dokument."),
    ]:
        m.bullet(label, body, after=20)

    m.section("ERHVERVSERFARING")
    jobs = [
        ("Ejer / teknisk direktør",
         "ELOHVAC ApS · København · maj 2023–nu",
         "5 elektrikere + 3 lærlinge · fuldt P&L · service, produktion og mindre projekter",
         [("Kunder, dokumentation og ansvar",
           "Service, måling og dokumentation under eget P&L; rådgivning af kunder om fejl, "
           "grænseværdier og udbedring — og ansvar for at rådet holder.")]),
        ("Senior idriftsættelsesingeniør / projektleder, elsystem",
         "Novo Nordisk A/S · Kalundborg · nov. 2022–jul. 2024",
         "37 samtidige anlægsprojekter · 25 specialister · GMP/FDA/EMA",
         [("Verifikation og afvigelser",
           "FAT/SAT og IQ/OQ/PQ på nye anlæg; afvigelser lukket med A3 og rodårsagsanalyse — nul "
           "kritiske fund ved accept.")]),
        ("Projekt- og værkstedsleder",
         "Ventek-Air · København · jan. 2022–nov. 2022",
         "14 medarbejdere · 11 samtidige entrepriser · DKK 2–10 mio.",
         [("Prøvning og leverance",
           "11 samtidige opgaver med prøvekørsel, dokumentation og aflevering til kunden; daglige "
           "tavlemøder og ugentlig kapacitetstilpasning.")]),
        ("Vedligeholdelses- og driftsleder",
         "Lynetten under Biofos · København · aug. 2017–jan. 2022",
         "Kritisk renseanlæg i 24/7-drift · pumper, køl, HVAC, højspændingstavler, SCADA",
         [("Måling, fejlfinding og sikkerhed",
           "Fejlfinding på el- og maskinanlæg døgnet rundt under BEK 1608, DS/HD 60364, LOTO og APV; "
           "målinger og afvigelser registreret og lukket.")]),
        ("Elektromekaniker / produktionsteamleder",
         "ARJ Engineering · Teheran · dec. 2003–mar. 2010",
         "12 mekanikere og teknikere · maskinværksted · industriel anlæg",
         [("Prøvning og output",
           "12 mand og ugens prøveplan; output og kvalitet målt pr. medarbejder og pr. maskine.")]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=16)

    # ---------------------------------------------------------------- side 3
    m.page_break()
    m.section("UDDANNELSE OG AUTORISATION")
    m.edu("Elautoriseret maskinmester — dansk elautorisation LV/MV/HV",
          "Sikkerhedsstyrelsen · maj 2023")
    m.edu("B.Tech, teknologiledelse og maskinteknik (EQF 6)",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12")
    m.edu("El- og maskinteknisk design, elteknik (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("Lean: 5S, PDCA, VSM, A3, standard work · Køleteknik og klimaanlæg (AMU)",
          "Mercantec · 2021 · A3 og standard work anvendt i afvigelser og dokumentation")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("**Dansk: modersmål** · **Engelsk: professionelt**, skriftligt og mundtligt, herunder teknisk "
           "dokumentation og standarder · Persisk: modersmål · **Bosat i Måløv**, ca. 25 minutter til "
           "Stenløse · Kørekort B og bil · Kan tiltræde snarest eller efter aftale · Referencer efter "
           "aftale.", after=70)

    m.models_table("DE FØRSTE 90 DAGE — STANDARDER, MÅLINGER OG KUNDER",
                   ("Periode", "Hvad der sker, og hvordan det måles"), [
        ("Uge 1–2",
         "Læs jeres testmetoder og de standardsæt, der bruges mest; sid med på to testkørsler fra "
         "opstilling til rapport. Notér, hvor et standardskift ville ændre resultatet."),
        ("Dag 30",
         "Én oversigt over de standarder og produktfamilier, huset tester mest, med de grænseværdier og "
         "betingelser, der styrer dem. Første selvstændige testkørsel gennemført med gennemlæst rapport."),
        ("Dag 60",
         "Rapportskabelon og registreringspraksis foreslået, så målinger, usikkerhed og afvigelser står "
         "samme sted hver gang; TRF-formatet gennemgået og prøvet på en kundesag."),
        ("Dag 90",
         "Selvstændig kundesag fra kravafklaring til underskrevet rapport; egen målekontrol og "
         "kalibreringsstatus dokumenteret, og en plan for, hvilke nye områder — EMC, RED eller MIL — jeg "
         "tager fat på først."),
    ], widths=(1500, 8830))

    m.section("EN STANDARD ER EN KONTRAKT MED ET MARKED")
    m.para("Kunden køber ikke en måling; kunden køber adgang til et marked. Derfor er standardtolkningen "
           "den egentlige ydelse: hvilken udgave af standarden er gældende, hvilke undtagelser må man "
           "bruge, og hvad betyder det for testen i morgen. Jeg har læst bestemmelser, hvor en detalje "
           "flyttede et helt anlægs accept, og jeg er vant til at skrive konklusionen, så den holder, "
           "når nogen læser den efter mig.", after=70)

    m.section("MÅLINGER UDEN SPORBARHED ER MENINGER")
    m.para("Et laboratorieresultat er kun så stærkt som sit spor: hvilket instrument, hvilken "
           "opsætning, hvilken usikkerhed og hvem der udførte prøven. Det er den samme logik som i en "
           "GMP-verifikation, og derfor falder overgangen fra FAT/SAT og IQ/OQ/PQ til IEC-rapportering "
           "naturligt for mig — det er det samme håndværk med en anden adresse.", after=70)

    m.section("EN FEJL ER EN RÅDGIVNING, IKKE EN DOMM")
    m.para("Når et produkt ikke består, har kunden brug for to ting: en præcis forklaring og en rettelse, "
           "der kan produceres. Jeg har siddet med afvigelser, hvor den første løsning var teknisk rigtig "
           "og kommercielt umulig, og fundet den version, der kunne bygges. Rådgivning er ikke at være "
           "enig — det er at give kunden et valg, han kan handle på.", after=70)

    m.section("STANDARDISERINGSARBEJDE ER RÅDGIVNING MED LÆNGERE HORISONT")
    m.para("At sidde i et udvalg under **Dansk Standard** eller i en **ERFA-gruppe** er ikke en "
           "tillidserklæring — det er den måde, man får indflydelse på, hvordan kravene bliver læst om "
           "to år. Jeg har siddet i møder, hvor en formulering blev ændret, og hvor ændringen senere "
           "betød noget for, hvordan vi kunne dokumentere vores arbejde. Den slags arbejde tager jeg "
           "gerne, hvis huset vil bruge tiden på det.", after=70)

    m.section("DET JEG IKKE HAR PRØVET — OG HVORFOR REJSEN ER KORT")
    m.para("Jeg har ikke kørt IEC 62368 eller 60335, ikke skrevet TRF-rapporter og ikke testet EMC. Det "
           "skal stå klart. Til gengæld har jeg i 20+ år målt, fejlfundet, verifikationstestet og "
           "dokumenteret på udstyr, hvor en fejl kunne blive en ulykke, og hvor sporet efter prøven var "
           "det, der blev revideret. Fagområdet er nyt; håndværket er det ikke — og det er netop den "
           "kombination, opslaget beskriver som nøglen i et mindre hus.", after=70)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table("HVAD STILLINGEN KRÆVER — HVAD JEG HAR LEVERET",
                   ("Krav i opslaget", "Bevis"), [
        ("El-sikkerhedstest og rådgivning til kunder gennem hele processen",
         "Måling, fejlfinding og verifikation i 20+ år samt rådgivning af kunder i egen virksomhed — "
         "med ansvar for, at rådet holder, når produktet er i drift."),
        ("Læse og tolke standarder, og erfaring med eller mod på at arbejde med IEC TRF-rapporter",
         "Standardarbejde efter DS/HD 60364 og BEK 1608; rapporter og protokoller skrevet, så en "
         "tredjemand kan følge krav → måling → konklusion. TRF-formatet læres i de første uger."),
        ("Kunderådgivning: formidle resultater og løsninger, så kunderne føler sig trygge i deres produktudvikling",
         "Primær kundekontakt i hele leverancer: hvad der fejler, hvorfor, og hvad der kan rettes — "
         "formidlet så både tekniker, indkøber og ledelse kan handle."),
        ("Teknisk baggrund som ingeniør, tekniker, maskinmester, elektronikfaglig profil eller lignende",
         "Elautoriseret maskinmester (LV/MV/HV), B.Tech i teknologiledelse og maskinteknik (EQF 6), "
         "el- og maskinteknisk design (EQF 6)."),
        ("Erfaring med måleteknik, test, elektronik, el-sikkerhed eller tekniske standarder",
         "Måleteknik og fejlfinding på motorer, styringer, frekvensomformere og følere; FAT/SAT og "
         "IQ/OQ/PQ; arbejde under BEK 1608 og DS/HD 60364."),
        ("Struktureret arbejde med dokumentation og rapportering",
         "Registrering med udstyr, metode, resultat og tid; afvigelser lukket med A3; leverancepakker "
         "skrevet til tre modtagere samtidig."),
        ("God til at forklare tekniske problemstillinger, så alle kan være med",
         "Teknisk formidling på dansk og engelsk til fagfolk, indkøb og ledelse — i møder, "
         "dokumentation og på pladsen."),
        ("Flydende dansk, skriftligt og mundtligt",
         "Dansk modersmål; al kundedialog og dokumentation kan føres på dansk, og teknisk engelsk er "
         "arbejdssprog ved siden af."),
        ("Fordel: erfaring med IEC-standarder",
         "Ikke IEC-produktstandarder. Dokumenteret standardarbejde er dansk og europæisk "
         "installationspraksis (DS/HD 60364, BEK 1608) samt GMP/FDA/EMA-krav."),
        ("Fordel: erfaring med TRF-rapporter",
         "Ikke TRF endnu. Tilsvarende: testprotokoller og verifikationsrapporter, hvor hvert krav "
         "kunne følges til en måling og en konklusion."),
        ("Fordel: erfaring med CE-mærkning",
         "Ikke CE-mærkning som dokumentudsteder. Tilsvarende: overensstemmelse og dokumentation for "
         "anlæg, der skulle godkendes og sættes i drift."),
        ("Fordel: erfaring med EMC, RED, MIL, miljøtest eller lignende",
         "Ikke EMC, RED eller MIL. Miljø- og driftstest er prøvet i form af idriftsættelse og "
         "belastningsprøver; de øvrige områder er præcis dem, jeg vil udvide profilen med."),
        ("Nøgleperson i testlaboratoriet med ansvar for el-sikkerhedsområdet i et mindre team",
         "Vant til små enheder med direkte ansvar: 5 medarbejdere og 3 lærlinge i egen virksomhed, og "
         "fagligt ansvar uden mellemleder."),
        ("Præge den faglige udvikling af el-sikkerhedsområdet fremadrettet",
         "Byggede arbejdsgange, skabeloner og rapporteringssystem op fra bunden i egen virksomhed; "
         "faglig retning taget i samarbejde med dem, der skulle arbejde i den."),
        ("Tæt på kunder, produkter og beslutninger — ikke én ud af mange",
         "Egen virksomhed siden 2023 med fuldt P&L: beslutninger taget tæt på kunden, uden at nogen "
         "skulle spørges først."),
        ("Mulighed for at udvide profilen til EMC-test, radio (RED), MIL-test, miljøtest eller akustiske og optiske målinger",
         "Har udvidet fagligt før — fra el-installation til verifikation og GMP-dokumentation — og vil "
         "tage EMC eller RED som det første nye område."),
    ], widths=(3600, 6746))

    m.section("ET LILLE HUS ER EN FAGLIG MULIGHED, IKKE EN BEGRÆNSNING")
    m.para("I et mindre testcenter bliver specialisten ikke et led i en proces; specialisten er processen. "
           "Det betyder, at kvaliteten af rådgivningen er synlig for kunden med det samme, og at den "
           "faglige retning bliver til i samtaler mellem få mennesker. Jeg har prøvet begge dele — store "
           "anlægsprojekter med 25 specialister og en hverdag, hvor jeg selv besluttede og selv stod til "
           "ansvar — og det er den sidste, jeg søger tilbage til.", after=80)

    m.section("HVOR JEG VILLE STARTE")
    m.para("Med at læse jeres mest brugte testmetoder og se to kørsler fra opstilling til rapport, så jeg "
           "ved, hvor standarden og virkeligheden skiller. Derefter tage den første kundesag selv — og "
           "hellere spørge om det, jeg ikke ved, end at skrive en konklusion, nogen skal forsvare "
           "bagefter.", after=80)

    return m.save(path, title="El-sikkerhedsspecialist — Bolls")


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Bolls_Elsikkerhedsspecialist.docx')
    build(out)
    print(out)
