#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Teamleder til Planning & Operations Center — DB Cargo Scandinavia A/S, Høje Taastrup.

Dansk opslag -> DANSK dokument (4 sider). TEMPLATE Gentofte-2027.
DB Cargo = nyt firma. Kontakt: Head of Operations Åsa Stålgard (mail).
Samtaler løbende; opstart hurtigst muligt. QuickApply på Jobindex.
Bias-ønske i opslaget: undlad foto og personlige oplysninger i CV (intet foto
i masterdesignet; kontakt + by holdes, alder/familie/nationalitet nævnes ikke).

KENDTE GAPS (udelad, ikke fabrikeret — se rapport):
- Svensk på professionelt niveau = NEJ (brugersvar fra Saildrone-KIT: svensk NEJ).
- Erfaring med danske og svenske overenskomster inden for jernbanedrift = NEJ
  (overenskomst = alm. kendskab fra ansættelser, ikke jernbanespecifikt).
- Jernbane/godstransport = interesse (logistik-kunder, maritim grunduddannelse).
Sproglinjen i CV'et står ærligt: dansk/engelsk/persisk.

STIL (3/3 mod #447 ARC): register "Robust overblik, fælles fremdrift",
åbning BX (rejsen begynder i planen), struktur "Plan, afvikling, forbedring".
Ingen em dash. KPI'er skrives med lige apostrof i dobbeltciterede strenge.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_Gentofte_DriftslederEjendomme_2027.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'DB Cargo Scandinavia · Teamleder · Planning og Operations Center'
BANNER_RESUME = 'DRIFTSLEDELSE · PLANLÆGNING · TRAFIKAFVIKLING · SAMARBEJDE'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('2. december 2026')
    m.meta('DB Cargo Scandinavia · Høje Taastrup')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning om stillingen som teamleder til Planning og '
              'Operations Center',
           bold=True, color='1A1A1A')
    m.para('Kære Åsa Stålgard,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('Et godstog, der skal køre gennem Danmark, Sverige og Tyskland, '
       'begynder sin rejse i en plan. Planen bliver lagt i Planning og '
       'Operations Center, som opslaget kalder den operationelle nerve i '
       'Skandinaviens jernbanegodstransport, og her skal togproduktionen '
       'planlægges og afvikles sikkert, effektivt og med høj kvalitet på '
       'tværs af Danmark, Sverige og Tyskland. Teamet er bindeleddet mellem '
       'planlægning og drift. Jeg søger stillingen som teamleder, fordi det '
       'er den disciplin, jeg kender bedst: at få planer til at holde, når '
       'driften kører. Rollen er det samlede personale-, drifts- og '
       'udviklingsansvar for centret med reference til Head of Operations, '
       'og horisonten er fremtidens jernbanelogistik.')

    lp('Erfaring fra drift, planlægning og ledelse følger med: jeg har været leder '
       'i drifts- og produktionsorganisationer siden 2003: forsyning, '
       'industri, installation og rådgivning. Dokumenteret ledererfaring med '
       'fokus på udvikling af medarbejdere har jeg med fra alle stationer, '
       'fra oplæring af nye teknikere til lærlinge i ELOHVAC og faglig '
       'opkvalificering i Biofos. Erfaring med ledelse i en drifts- eller '
       'produktionsorganisation lyder som en beskrivelse af mine år hos '
       'Biofos, hvor 10 medarbejdere på skiftehold holdt kritiske anlæg '
       'kørende døgnet rundt, og af Ventek og ELOHVAC, hvor 14 mand kørte '
       'på pladserne, og team, økonomi og kvalitet lå på samme bord.')

    lp('Faste discipliner har fulgt med hele vejen: vagt- og '
       'ferieplanlægning, koordinering af mandskab og materiel, og opfølgning '
       'på mål for tid, kvalitet og økonomi. Performanceopfølgning og '
       'procesforbedringer hører til hverdagen hos mig. Den erfaring med '
       'planlægning, drift eller trafikafvikling, I søger, har jeg fra '
       'planlægning og drift; trafikafvikling i jernbanen er nyt, men '
       'disciplinen med at holde en produktion i bevægelse, når noget bryder '
       'sammen, kender jeg fra døgndriften. Når det sker, gælder det, at '
       'beslutninger skal træffes hurtigt og på et solidt datagrundlag, og i '
       'Biofos lå fejldata og driftsdata åbent foran os. Både analytiske '
       'evner og et stærkt overblik har været i brug hver dag siden da. '
       'Samarbejdet med Asset Management, Service Design, Finance, Safety og '
       'eksterne interessenter svarer til det tværgående arbejde, jeg kender '
       'fra bygherrer, underentreprenører, leverandører og kunder, og Asset '
       'Management har jeg arbejdet med som disciplin om forsyningens anlæg. '
       'Interesse for jernbane- og godstransport har jeg fået med årene, og '
       'logistikbranchen som kunde har gjort transport til noget, jeg følger '
       'med i. Tværgående samarbejde kører jeg på dansk og engelsk.',
       after=44)

    lp('Første måned går til planen: at lede og udvikle medarbejdere i Planning og '
       'Operations Center begynder med at kende den samlede '
       'planlægningsproces fra årsplan til daglig drift indefra sammen med '
       'teamet og følge koordineringen af lokomotiv- og personaleplanlægning. '
       'Rammerne for sikkerhedskrav, arbejdstidsregler og interne procedurer '
       'lærer jeg, som de er. Målet efter 30 dage er effektiv planlægning og '
       'daglig afvikling af togproduktionen som en fælles forståelse i '
       'teamet, og at alle ved, hvor jeg står.', after=44)

    lp('Derefter kommer afviklingen: her handler det om at optimere '
       'ressourceudnyttelse, produktivitet og punktlighed uden at slide '
       'folkene op, og om håndtering af driftsforstyrrelser med klare '
       'beslutningslinjer. Samarbejdet med omverdenen får faste punkter, og '
       'aftaler med Asset Management, Service Design, Finance, Safety og '
       'eksterne interessenter føres ud i en rytme, der holder. Målet efter '
       '60 dage er høj kvalitet i produktions- og trafikafviklingen som en '
       'synlig vane.', after=44)

    lp("Til sidst kommer forbedringen: performance management med "
       "fokus på KPI'er, punktlighed og produktivitet som en fast opfølgning, "
       "og forbedringsinitiativer, standardisering og digitalisering bliver "
       "konkrete forslag fra teamet frem for projekter oppefra. "
       "Digitalisering skal fjerne manuelt arbejde, og AI bruger jeg som "
       "hjælpeværktøj til analyse og rapportering. Målet efter 90 dage er en "
       "enkel rapportering på drift, sikkerhed og udviklingsinitiativer, der "
       "faktisk bliver brugt, og de første bud på udviklingen af nye løsninger "
       "og services i tæt samarbejde med resten af organisationen.")

    lp('Samarbejde, værdier og tempo følges ad hos mig: struktureret og analytisk er '
       'sådan, jeg griber en kompleks plan an, og når presset stiger, er jeg '
       'beslutningsdygtig og robust under pres. I samarbejdet er jeg '
       'relationsskabende og samarbejdsorienteret, og jeg er serviceorienteret '
       'med fokus på både kunder og kolleger, fordi driften kun hænger '
       'sammen, når begge sider er med. Ambitionen er en ledelse, der skaber '
       'engagement, ansvarlighed og resultater. Værdierne tillid, ærlighed, '
       'integritet, loyalitet og respekt er levende ord for mig, og jeg tror '
       'på linjen fra opslaget: de bedste resultater skabes gennem stærkt '
       'samarbejde og fælles ansvar. Som I skriver, er der stor indflydelse '
       'på udviklingen af vores operationelle set-up og mulighed for at præge '
       'både processer, performance og medarbejderudvikling, og det er '
       'rammen, jeg søger. Opslaget søger en engageret og resultatorienteret '
       'teamleder, og det er ambitionen bag min måde at arbejde på. I indkalder til samtaler løbende, og jeg kan tiltræde '
       'hurtigt, så lad os tage snakken.', after=44)

    m.para('Med venlig hilsen', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Teamleder med 20+ års ledelse i drifts- og '
           'produktionsmiljøer, hvor planer skal holde, også når driften '
           'kører døgnet rundt. Skiftehold i en kommunejet forsyning, '
           'montagehold på byggepladser og servicehold med kunder og aftaler '
           'har lært mig at træffe beslutninger hurtigt på et solidt '
           'datagrundlag og holde produktionen i bevægelse, når noget bryder '
           'sammen.', after=32)
    m.para('Jeg planlægger fra årsplan til daglig rutine: vagt- og '
           'ferieplaner, ressourcer og materiel, opfølgning på punktlighed, '
           'kvalitet og økonomi. AI bruger jeg som hjælpeværktøj til analyse '
           'og rapportering. Rollen i Planning og Operations Center taler til '
           'det, jeg kender bedst: at få mennesker, planer og drift til at '
           'hænge sammen, også når arbejdet bevæger sig på tværs af lande.',
           after=32)

    jobs = [
        ('CTO og stifter',
         'Data Power · Måløv · jan. 2024 – nu',
         'AI-udvikling, analyse og forretningsstrategi',
         [('Planlægning og leverancer',
           'Tilbud, aftaler og leverancer planlagt og fulgt til dørs. AI og '
           'analyse som hjælpeværktøj i det daglige arbejde.')]),
        ('Drifts- og serviceleder · elautoriseret maskinmester',
         'ELOHVAC · Ballerup · maj 2023 – nov. 2026',
         '5 elektrikere og 3 lærlinge · service, installation og projekter',
         [('Team og opfølgning',
           'Vagtplaner, opgavefordeling og faste opfølgningsmøder. P&L, KS og '
           'serviceaftaler fulgt op på tid, kvalitet og økonomi.'),
         ('Kunder og aftaler',
           'Tilbud og aftaler gennemgået med kunderne, før de blev givet, '
           'og økonomien i opgaverne fulgt tæt.')]),
        ('Commissioning Manager',
         'Novo Nordisk · Hillerød · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, 2-10 mio. kr. · 25 specialister · GMP, IQ/OQ/PQ',
         [('Tid og kvalitet',
           'CAV- og kritiske systemer leveret med dokumentation og '
           'frigivelse, koordineret med kundens projektteam og '
           'underleverandører. Aftalte datoer blev holdt.'),
         ('Koordinering',
           'Kundens projektteam og underleverandører holdt opdateret, og '
           'dokumentationen fulgte leverancen hele vejen.')]),
        ('Overmontør og entrepriseleder',
         'Ventek · Taastrup · jan. 2022 – nov. 2022',
         '11 projekter · 14 mand og underentreprenører',
         [('Ressourcer og koordinering',
           'Mandskab, materiel og tid planlagt, så flere hold arbejdede '
           'parallelt på samme adresse uden at støde sammen.'),
         ('Planer der holdt',
           'Daglige koordineringer med underentreprenører og leverandører, '
           'så mandskab og materiel var på plads, når arbejdet skulle '
           'udføres.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · kritiske anlæg · 10 medarbejdere · skiftehold',
         [('Døgndrift',
           'Pumper, HVAC, procesrør, el, SCADA og PLC holdt kørende i '
           'døgndrift med 10 medarbejdere på skiftehold. Vagtplaner, fejldata '
           'og reservedelsstyring som faste værktøjer, og driftsforstyrrelser '
           'håndteret med hurtige prioriteringer.'),
         ('Planlægning',
           'Forebyggende vedligehold planlagt på fejldata, og '
           'reservedelsstyring, så reparationer ikke ventede.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('Produktion og bemanding',
           'Produktionsplanlægning, bemanding og materialestyring fra tegning '
           'til færdigt emne. Uddannelse af nye medarbejdere i værkstedet.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.edu('B.Tech (EQF6), teknologiledelse og maskinteknik',
          'Danmark · 2017–2022 · karakter 7,6')
    m.edu('Dansk elautorisation LV/MV/HV som elautoriseret maskinmester',
          'Sikkerhedsstyrelsen · maj 2023')
    m.edu('El- og maskinteknisk design, elteknik (EQF6)',
          'Tehran Technical University · 2000–2003')
    m.edu('PRINCE2, certificeret projektleder', 'AXELOS / PeopleCert')
    m.edu('Køleteknik og klimaanlæg (AMU)',
          'Mercantec · 2021 · STCW 2021–2023, Søfartsstyrelsen')

    m.section('STYRKER I HVERDAGEN')
    m.bullet('Planlægning der holder', 'Vagt- og ferieplaner, projektplaner '
             'og ressourcestyring med blik for hele året, ikke kun den '
             'travle uge.', after=10)
    m.bullet('Beslutninger under pres', 'Akutte fejl i døgndrift håndteret '
             'med klare prioriteringer og data som grundlag frem for '
             'gætterier.', after=10)
    m.bullet('Tværgående samarbejde', 'Asset Management, bygherrer, '
             'underentreprenører, leverandører og kunder i samme '
             'arbejdsflade. Dansk og engelsk som arbejdssprog.', after=10)
    m.bullet('Opfølgning på mål', 'Produktionsmål som MTBF, MTTR og OEE '
             'sammen med økonomi og kvalitet fulgt op i faste rytmer, så '
             'ingen var i tvivl om, hvor vi stod.', after=10)

    m.section('FØRSTE 90 DAGE')
    m.para('Planen følger opgaven: planen, afviklingen, forbedringen.',
           after=8)
    m.bullet('Måned 1 · planen', 'Den samlede planlægningsproces fra årsplan '
             'til daglig drift gennemgået sammen med teamet, koordineringen '
             'af lokomotiv- og personaleplanlægning fulgt, og rammerne for '
             'sikkerhedskrav, arbejdstidsregler og interne procedurer lært '
             'indefra.', after=10)
    m.bullet('Måned 2 · afviklingen', 'Håndtering af driftsforstyrrelser med '
             'klare beslutningslinjer, faste samarbejdspunkter med Asset '
             'Management, Service Design, Finance, Safety og eksterne '
             'interessenter, og ressourceudnyttelse, produktivitet og '
             'punktlighed fulgt tæt.', after=10)
    m.bullet('Måned 3 · forbedringen',
             "Performance management med fokus på KPI'er, punktlighed og "
             "produktivitet sat i system, og forbedringsinitiativer, "
             "standardisering og digitalisering konkret med teamet. Enkel "
             "rapportering på drift, sikkerhed og udviklingsinitiativer.",
             after=10)

    m.section('SPROG, VÆRKTØJER OG PRAKTISK')
    m.para('Dansk (modersmål) · engelsk (professionelt) · persisk '
           '(modersmål). SAP, Excel, CMMS; PRINCE2. Kørekort kategori B '
           '(manuelt gear) og vant til at bevæge mig mellem arbejdssteder. '
           'Bosat i Måløv; Høje Taastrup fungerer nemt derfra.', after=8)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Krav og dokumentation · Teamleder, Planning og '
                   'Operations Center',
                   ('Krav i opslaget', 'Dokumentation'),
                   [
        ('Lede og udvikle medarbejdere i Planning og Operations Center',
         'Personaleledelse siden 2003 med dokumenteret ansvar '
         'for udvikling af medarbejdere: 12 mekanikere (ARJ 2003-2010), 10 '
         'medarbejdere på skiftehold i døgndrift (Biofos 2017-2022), 14 mand '
         'på montage (Ventek 2022) og 5 elektrikere og 3 lærlinge i service '
         '(ELOHVAC 2023-2026). Oplæring, faglig opkvalificering og '
         'lærlingeuddannelse hører med.'),
        ('Optimere ressourceudnyttelse, produktivitet og punktlighed',
         'Ressourcer, mandskab og materiel timet mod milepæle i '
         'Ventek (14 mand, 11 projekter) og Novo (37 leverancer). Fejldata '
         'og reservedelsstyring i Biofos gjorde vedligehold planlagt frem for '
         'reaktivt. Punktlighed som aftalte datoer, der blev holdt.'),
        ('Effektiv planlægning og daglig afvikling af togproduktionen',
         'Daglig drift og planlægning i 24/7-forsyning med '
         'vagtplaner, ferieplanlægning og faste rutiner. PRINCE2-struktur '
         'for planer, og planlægning fra årsplan til daglig rutine som '
         'fast disciplin.'),
        ('Høj kvalitet i produktions- og trafikafviklingen',
         'Kvalitetsstyring (KS) i ELOHVAC, dokumentation og '
         'frigivelse på 37 CAPEX-leverancer hos Novo i GMP-drift. '
         'Produktionsafvikling er erfaring; '
         'trafikafvikling i jernbanen er nyt domæne med samme disciplin.'),
        ('Forbedringsinitiativer, standardisering og digitalisering',
         'Data Power har siden 2024 arbejdet med AI og analyse som '
         'forbedringsværktøj, og standardiserede procedurer er indført i '
         'serviceforretningen. Digitalisering målt på fjernet manuelt '
         'arbejde.'),
        ('Sikkerhedskrav, arbejdstidsregler og interne procedurer',
         'Arbejdsmiljøansvar i Biofos-driften, sikkerhedsudstyr på '
         'Prøvestenen og vagtplanlægning under arbejdstidsregler på '
         'skiftehold med 10 medarbejdere. Jernbanens sikkerhedsregler er '
         'nye for mig.'),
        ('Planlægningsproces fra årsplan til daglig drift',
         'Årlig og månedlig planlægning af vedligehold og '
         'bemanding i Biofos kombineret med PRINCE2-projektstruktur. '
         'Overført til produktionens planlægningsproces.'),
        ('Koordinering af lokomotiv- og personaleplanlægning',
         'Personaleplanlægning som vagt- og ferieplaner for 10 på '
         'skiftehold og 14 mand på montage. Materiel- og '
         'reservedelsplanlægning fra driftssiden; lokomotiver er nyt.'),
        ('Håndtering af driftsforstyrrelser',
         'Døgndrift med akutte fejl, nedbrud og reparationer '
         'håndteret med hurtige prioriteringer (Biofos 2017-2022) og '
         'byggepladsfejl under tidspres (Ventek 2022).'),
        ("Performance management med fokus på KPI'er, punktlighed og "
         'produktivitet',
         'MTBF/MTTR/OEE og produktionsmål fra industrien, '
         'økonomiopfølgning (P&L) for 5 elektrikere og 3 lærlinge og '
         'kvalitetsmål i faste møder. '
         'Målopfølgning som fast rytme, ikke lejlighedsvis.'),
        ('Samarbejde med Asset Management, Service Design, Finance, Safety '
         'og eksterne interessenter',
         'Asset Management som reel erfaring med drift og vedligehold af '
         'forsyningens anlæg (Biofos 2017-2022), Finance via P&L-ansvar '
         '(ELOHVAC), Safety via '
         'arbejdsmiljø og sikkerhedsudstyr, og eksterne interessenter som '
         'bygherrer, underentreprenører, leverandører og kunder.'),
        ('Rapportering på drift, sikkerhed og udviklingsinitiativer',
         'Løbende rapportering på 37 CAPEX-projekter og i driften, KS og '
         'dokumentation, og økonomiopfølgning i faste møder. Rapportering '
         'skrevet til at blive brugt.'),
        ('Beslutninger skal træffes hurtigt og på et solidt datagrundlag',
         'SCADA- og PLC-data fra 24/7-drift, fejldata og driftsdata som '
         'beslutningsgrundlag i døgndriften. Data før mavefornemmelse i '
         'pressede situationer.'),
        ('Dokumenteret ledererfaring med fokus på udvikling af medarbejdere',
         'Fire ledelsesroller siden 2003 med ansvar for trivsel og faglig '
         'udvikling: oplæring af teknikere, lærlinge i ELOHVAC og '
         'opkvalificering i Biofos. Udvikling af medarbejdere som del af '
         'jobbet, ikke et projekt.'),
        ('Analytiske evner og et stærkt overblik',
         'Dataanalyse og AI-udvikling (Data Power), '
         'fejldataanalyse i drift, SAP-overblik og teknisk support på data '
         'fra biler og anlæg.'),
        ('Performanceopfølgning og procesforbedringer',
         'Opfølgning på tid, kvalitet og økonomi i faste '
         'møder (ELOHVAC), og procesforbedringer via standardiserede '
         'arbejdsgange og digitalisering.'),
        ('Erfaring med planlægning, drift eller trafikafvikling',
         'Vagtplaner, projektplaner og '
         'daglig drift i over 20 år. Trafikafvikling som overført viden '
         'fra drift med skarpe krav til tid.'),
        ('Interesse for jernbane- og godstransport',
         'Logistikbranchen som kunde (DSV, Salling Group) og en '
         'maritim grunduddannelse (STCW) har gjort transport til et emne, '
         'jeg følger. Erfaringen er bred industriel drift, ikke jernbane.'),
                   ],
                   widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo · Ansøgning og CV · Teamleder, '
                       'Planning og Operations Center')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_DBCargo_TeamlederPlanningOperations.docx')
    build(out)
    print(out)
