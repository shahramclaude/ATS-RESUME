#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Maskinmester til drift og overvågning af forsyningen (Driftsmester i
kontrolrummet) — Frederiksberg Forsyning. Dansk opslag -> DANSK dokument
(4 sider). TEMPLATE Gentofte-2027.

Frederiksberg Forsyning = nyt firma; 100 % ejet af Frederiksberg Kommune,
ca. 160 medarbejdere, ca. 750 mio. kr. i nettoomsætning. Forsyningsarter:
vand, fjernvarme, gas, fjernkøl og spildevand. Tre varmepumpeanlæg
(overskudsvarme fra blødgøringsvandværk + to dobbeltvirkende fjernkøl/
fjernvarme). Klimatilpasningsanlæg med Frederiksberg Kommune. Kontrolrum
døgnbemandet, maskinmestre i treholdsskift, team med 7 andre driftsmestre.
Referencer til Simon Hougaard, leder af Drift og Planlægning. Kontakt:
koordinator Michael Beck, 30 76 65 81. Frist 6. december 2026.
Sikkerhedsgodkendelse til fortroligt er en forudsætning (længere proces).
Straffeattest og referencer indhentes. Arbejdssted Stæhr Johansens Vej 38.

KIT-BÆRENDE (bindende):
- Biofos = kommunejet forsyning -> forsyningserfaring SELVSIKKERT (ARC-læring).
- Sikkerhedsgodkendelse -> "dansk permanent opholdstilladelse" (Terma-KIT).
- Lokation Frederiksberg = commute_ok (CTR-KIT); "én times kørsel" opfyldt.
- Fjernvarmeinstallationer = INTERESSE (CTR-KIT), ikke erfaring -> hedge.
- Erfaring med treholdsskift = ordret NEJ (skiftehold ja) -> ærlig hedge
  ("fordel, ikke krav" i opslaget). Kedelpassercertifikat = nej -> udeladt
  (fordel, ikke krav). SRO = funktion via SCADA/PLC (hedge).
- BANNED-ord i JD citeres aldrig: "Brænder du for teknik" ('brænder').

STIL (3/3 mod #449 Hyperscale): register "Ro i kontrolrummet, fart på
forsyningen", åbning BZ (byen sover, forsyningen kører), struktur
"Anlæggene, vagten, optimeringen". Hilsen: "Kære Michael Beck,".
Ingen em dash. Ingen fede mini-heads. Ingen status-prefixer i matrix.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_Gentofte_DriftslederEjendomme_2027.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Frederiksberg Forsyning · Driftsmester · Kontrolrummet'
BANNER_RESUME = 'DRIFT · FORSYNING · KONTROLRUM · VEDLIGEHOLD'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('2. december 2026')
    m.meta('Frederiksberg Forsyning · Drift og overvågning')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning om stillingen som maskinmester til drift og '
              'overvågning af forsyningen',
           bold=True, color='1A1A1A')
    m.para('Kære Michael Beck,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('Klokken er fem om morgenen på Frederiksberg, og byen sover stadig. '
       'Vandet er i hanerne, varmen i rørene og fjernkølingen i nettet, '
       'fordi kontrolrummet har været bemandet hele natten. Et velfungerende '
       'kontrolrum er en forudsætning for, at vi kan levere sikker forsyning, '
       'som der står i opslaget, og kontrolrummet er døgnbemandet og drives '
       'af maskinmestre i treholdsskift. At sikre stabil og fremtidssikret '
       'forsyning til hele Frederiksberg er opgaven, jeg søger som '
       'maskinmester til drift og overvågning af forsyningen, i et team med '
       'syv andre driftsmestre.')

    lp('Uddannet maskinmester med elautorisation og mere end 20 år i teknisk '
       'drift bag mig, heraf seks år i en kommunejet forsyning: Biofos, hvor '
       '10 medarbejdere på skiftehold holdt kritiske anlæg kørende døgnet '
       'rundt, og hvor SCADA og PLC var vinduet ind til driften. Erfaring '
       'fra forsyningsbranchen har jeg dermed fra en virksomhed med samme '
       'ejerstruktur som jeres, og døgnbemanding, vagtplaner og '
       'rådighedsvagt kender jeg som en del af hverdagen. Driftsforstyrrelser '
       'blev mødt med hurtige prioriteringer, og uden for vagten gik tiden '
       'med at deltage i vedligehold og optimeringsopgaver på anlæggene: '
       'pumper, HVAC, procesrør og el. Mit kendskab til SRO-anlæg kommer fra '
       'SCADA- og PLC-arbejdet, og varmepumper og køl ligger i forlængelse '
       'af min køleteknik fra AMU i 2021 og årene med HVAC i service. '
       'Erfaring med treholdsskift har jeg ikke ordret, men skiftehold i '
       'døgndrift kender jeg indefra, og det er den samme disciplin: sove '
       'på skæve tidspunkter og være skarp, når alarmen går.')

    lp('De første 90 dage fordeler sig på anlæggene, vagten og '
       'optimeringen. Første måned er anlæggene og selve opgaven, at drifte '
       'og overvåge vores forsyningsanlæg fra kontrolrummet sammen med '
       'holdet: de tre varmepumpeanlæg, blødgøringsvandværket og '
       'klimatilpasningsanlæggene rundt om i byen, og jeg tager godt imod '
       'grundig sidemandsoplæring, også fordi nye anlæg læres hurtigst på '
       'den måde. Fra Biofos kender jeg spildevand og kritiske pumpeanlæg '
       'indefra, fjernvarme har jeg arbejdet med som interesse, og gas og '
       'fjernkøl bliver nye bekendtskaber. Måned to er vagten: '
       'treholdsskiftet, alarmbilledet og rutinerne, og at reagere hurtigt '
       'og korrekt på alarmer og driftsforstyrrelser skal sidde på rygraden, '
       'før de 60 dage er gået. Tredje måned er optimeringen, hvor jeg '
       'bidrager med nye vinkler til struktur og processer, og det '
       'overordnede fokus er, som der står, at sikre optimal drift og '
       'udføre vedligehold på alle vores forsyningsarter.', after=44)

    lp('Simon Hougaard siger, at han tror på nærværende ledelse, klare '
       'rammer og stærkt samarbejde, og at når medarbejderne trives og '
       'føler sig værdsat, skaber vi de bedste resultater sammen. Det '
       'genkender jeg fra de steder, jeg har triveds bedst: en organisation '
       'med uformel omgangstone og et godt arbejdsfællesskab, et fagligt '
       'team med kollegial opbakning og fleksibel vagtplan, og varierende '
       'opgaver og stort ansvar. Medarbejdertrivsel, udvikling og diversitet '
       'fornemmer jeg i opslaget, og en forsyning, hvor forsyningssikkerhed, '
       'innovation og samfundsansvar går hånd i hånd, og hvor den tredobbelte '
       'bundlinje er rammen om investeringerne i grøn omstilling, '
       'digitalisering og moderne faciliteter, er et sted, jeg gerne vil '
       'stå i kontrolrummet. Så det praktiske: jeg trives i et treholdsskift, '
       'jeg kan arbejde både alene og i mindre teams, og jeg arbejder '
       'struktureret og bevarer overblikket i pressede situationer. Jeg har '
       'kørekort (kategori B) og bor i Måløv, inden for én times kørsel fra '
       'Frederiksberg, og rådighedsvagt kender jeg fra døgndriften. Til '
       'sikkerhedsgodkendelsen har jeg dansk permanent opholdstilladelse og '
       'er indstillet på hele forløbet, også den længere tid, I nævner. I '
       'indkalder løbende til samtaler, og jeg kan være med fra start. Jeg '
       'ser frem til at høre fra jer.', after=44)

    m.para('Med venlig hilsen', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Maskinmester med elautorisation og 20+ år i teknisk drift, '
           'herunder seks år i en kommunejet forsyning med døgndrift, '
           'skiftehold og SCADA-overvågning. Vant til alarmer, '
           'driftsforstyrrelser og vedligehold på kritiske anlæg, og til at '
           'arbejde både alene og i mindre teams. Jeg er vant til at '
           'dokumentere det, jeg gør, og til at sige til, når noget ser '
           'forkert ud.', after=32)
    m.para('Kontrolrummet er ikke fremmed for mig: overvågning, hurtige '
           'prioriteringer og sikker rutine på skift har været en del af '
           'min hverdag siden 2017. Uden for vagten arbejder jeg praktisk '
           'med vedligehold og optimering, og jeg bidrager gerne med nye '
           'vinkler til struktur og processer.', after=32)

    jobs = [
        ('CTO og stifter',
         'Data Power · Måløv · jan. 2024 – nu',
         'AI-udvikling, analyse og forretningsstrategi',
         [('Forretning og drift',
           'Tilbud, aftaler og leverancer planlagt og fulgt til dørs. AI '
           'brugt som hjælpeværktøj i det daglige arbejde.')]),
        ('Drifts- og serviceleder · elautoriseret maskinmester',
         'ELOHVAC · Ballerup · maj 2023 – nov. 2026',
         '5 elektrikere og 3 lærlinge · service, installation og projekter',
         [('Service og installation',
           'El, HVAC og køl i service og installation for erhvervskunder. '
           'Vagtplaner, KS og serviceaftaler med opfølgning på tid, '
           'kvalitet og økonomi.'),
          ('Aftaler og økonomi',
           'Serviceaftaler holdt i hævd, og økonomi og kvalitet fulgt op '
           'i faste møder med teamet.')]),
        ('Commissioning Manager',
         'Novo Nordisk · Hillerød · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, 2-10 mio. kr. · 25 specialister · GMP, IQ/OQ/PQ',
         [('Kritiske systemer',
           'CAV- og kritiske anlæg idriftsat med dokumentation og '
           'frigivelse. Koordinering med kundens projektteam og '
           'underleverandører; aftalte datoer holdt.'),
          ('Dokumentation',
           'Dokumentation og frigivelse fulgte leverancen hele vejen, og '
           'samarbejdet med 25 specialister og underleverandører blev '
           'holdt stramt.')]),
        ('Overmontør og entrepriseleder',
         'Ventek · Taastrup · jan. 2022 – nov. 2022',
         '11 projekter · 14 mand og underentreprenører',
         [('Entreprise og koordinering',
           'Mandskab, materiel og tid planlagt på byggepladser, så flere '
           'hold arbejdede parallelt uden at støde sammen.'),
          ('Daglig koordinering',
           'Underentreprenører og leverandører koordineret, så materiel '
           'og mandskab var på plads, når arbejdet skulle udføres.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · kritiske anlæg · 10 medarbejdere · skiftehold',
         [('Døgnedrift og kontrolrum',
           'Pumper, HVAC, procesrør, el, SCADA og PLC holdt kørende '
           'døgnet rundt med 10 medarbejdere på skiftehold. Overvågning '
           'og alarmer fra kontrolrummet, og driftsforstyrrelser '
           'prioriteret med det samme.'),
          ('Vedligehold og vagt',
           'Forebyggende vedligehold planlagt på fejldata, og '
           'reservedelsstyring, så reparationer ikke ventede. Vagtplaner, '
           'rådighedsvagt og arbejdsmiljø som faste discipliner.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('Produktion og oplæring',
           'Produktionsplanlægning, materialestyring og oplæring af nye '
           'medarbejdere i værkstedet.')]),
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

    m.section('STYRKER OG VÆRKTØJER')
    m.bullet('Drift og overvågning', 'SCADA, PLC og daglig driftsopfølgning '
             'på kritiske anlæg. Hurtige prioriteringer, når alarmen går.',
             after=10)
    m.bullet('Vedligehold', 'Forebyggende vedligehold planlagt på fejldata, '
             'reservedelsstyring og reparationer uden unødig ventetid.',
             after=10)
    m.bullet('Skiftehold og vagt', 'Vagtplaner, rådighedsvagt og sikker '
             'rutine på skift i døgnbemandet drift.', after=10)
    m.bullet('Sikkerhed og miljø', 'Arbejdsmiljøansvar og sikkerhedsrutiner '
             'fra både døgndrift og byggeplads.', after=10)
    m.bullet('Overblik og dokumentation', 'SAP, Excel og CMMS til '
             'opfølgning; PRINCE2 til struktur. Jeg dokumenterer, så andre '
             'kan overtage.', after=10)

    m.section('DE FØRSTE 90 DAGE')
    m.para('Planen følger driften: anlæggene, vagten, optimeringen.',
           after=8)
    m.bullet('Uge 1-4 · anlæggene', 'Varmepumpeanlæg, blødgøringsvandværk '
             'og klimatilpasningsanlæg lært at kende sammen med holdet, '
             'med grundig sidemandsoplæring.', after=10)
    m.bullet('Uge 5-8 · vagten', 'Treholdsskiftet, alarmbilledet og '
             'rutinerne på plads, så alarmer og driftsforstyrrelser mødes '
             'hurtigt og korrekt.', after=10)
    m.bullet('Uge 9-12 · optimeringen', 'Vedligehold og optimeringsopgaver '
             'på anlæggene med egne hænder, og nye vinkler til struktur '
             'og processer, hvor de kan bruges.', after=10)

    m.section('SPROG OG PRAKTISK')
    m.para('Dansk (modersmål) · engelsk (professionelt) · persisk '
           '(modersmål). SAP, Excel, CMMS, SCADA/PLC; PRINCE2, og kørekort '
           'kategori B (manuelt gear). Bosat i Måløv; Frederiksberg er '
           'inden for én times kørsel.', after=8)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Krav og dokumentation · Driftsmester, Kontrolrummet, '
                   'Frederiksberg Forsyning',
                   ('Krav i opslaget', 'Dokumentation'),
                   [
        ('Uddannet maskinmester',
         'Maskinmester med elautorisation LV/MV/HV (Sikkerhedsstyrelsen, maj '
         '2023), B.Tech (EQF6) i teknologiledelse og maskinteknik '
         '(2017-2022) og el- og maskinteknisk design (2000-2003).'),
        ('Drifte og overvåge forsyningsanlæg fra kontrolrummet',
         'Overvågning via SCADA og PLC i døgnbemandet forsyning (Biofos '
         '2017-2022): kritiske anlæg fulgt fra kontrolrummet, skift og '
         'alarmhåndtering som del af driften.'),
        ('Deltage i vedligehold og optimeringsopgaver på anlæggene',
         'Forebyggende vedligehold planlagt på fejldata og '
         'reservedelsstyring (Biofos 2017-2022), og optimering af pumper, '
         'HVAC, procesrør og el. Praktisk vedligehold i alle seks år.'),
        ('Trives i et treholdsskift',
         'Skiftehold i døgndrift siden 2017 (Biofos, 10 medarbejdere på '
         'skiftehold). Treholdsskift ordret er nyt for mig; vagtrutinen og '
         'skiftet mellem dag, aften og nat kender jeg som disciplin.'),
        ('Kan arbejde både alene og i mindre teams',
         'Alene på vagt i døgndrift (Biofos 2017-2022) og i mindre hold på '
         'service og montage: 5 elektrikere og 3 lærlinge (ELOHVAC '
         '2023-2026), 14 mand på pladsen (Ventek 2022).'),
        ('Arbejder struktureret og bevarer overblikket i pressede '
         'situationer',
         'Akutte fejl og nedbrud i 24/7-drift prioriteret under pres (Biofos '
         '2017-2022). PRINCE2 giver strukturen; skiftet giver roen.'),
        ('Bidrager med nye vinkler til struktur og processer',
         'Standardiserede arbejdsgange indført i service (ELOHVAC '
         '2023-2026), og AI og analyse som nye vinkler (Data Power '
         '2024-nu).'),
        ('Reagere hurtigt og korrekt på alarmer og driftsforstyrrelser',
         'SCADA-alarmer og akutte driftsforstyrrelser håndteret i '
         'døgndriften (Biofos 2017-2022) med hurtige prioriteringer og '
         'efterfølgende dokumentation.'),
        ('Treholdsskift som erfaring (fordel, ikke krav)',
         'Skiftehold i døgnedrift (Biofos 2017-2022) og vagtmønstre under '
         'overenskomst. Ordret treholdsskift er ikke på cv’et endnu; '
         'overgangen er kort.'),
        ('Kendskab til SRO-anlæg (fordel, ikke krav)',
         'SRO-funktionen som sådan: overvågning, regulering og styring via '
         'SCADA og PLC (Biofos 2017-2022). Specifikke SRO-platforme er nye '
         'for mig.'),
        ('Forsyningsbranchen som erfaring (fordel, ikke krav)',
         'Biofos (2017-2022) er en kommunejet forsyning som jeres: '
         'spildevand, kritiske anlæg, døgnbemanding og forpligtelser over '
         'for en offentlig ejer.'),
        ('Kørekort (kategori B)',
         'Kørekort kategori B (manuelt gear). Jeg har kørt mellem '
         'arbejdssteder i drift, service og entreprise i mere end 20 år, '
         'ofte med værktøj og materialer i bilen.'),
        ('Bor maks. én times kørsel fra Frederiksberg',
         'Bosat i Måløv; Frederiksberg er inden for én times kørsel, og '
         'turen tages gerne tidligt, når vagten kalder. Adressen ved '
         'Fasanvej Metro er nem at nå med både bil og metro.'),
        ('Sikkerhedsgodkendelse til fortroligt er en forudsætning',
         'Dansk permanent opholdstilladelse og indstillet på hele '
         'godkendelsesforløbet, også den længere tid, processen tager.'),
        ('Grundig sidemandsoplæring tilbydes',
         'Modtager den gerne: nye anlæg læres hurtigst på den måde. Har '
         'selv oplært nye medarbejdere (ARJ 2003-2010) og lærlinge '
         '(ELOHVAC 2023-2026).'),
        ('Nysgerrig på teknik og lyst til at lære nye anlæg at kende',
         'Nye anlæg er en fast del af historien: CAV og kritiske systemer '
         '(Novo 2022-2024), HVAC og køl (ELOHVAC 2023-2026), SCADA og PLC '
         '(Biofos 2017-2022).'),
        ('Drift af varmepumpeanlæg, blødgøringsvandværk og '
         'klimatilpasningsanlæg',
         'Varmepumpeanlæg og fjernkøl er nye anlæg for mig; HVAC, køl '
         '(AMU 2021) og pumpeanlæg er velkendte. Spildevand og '
         'pumpeanlæg kender jeg indefra (Biofos 2017-2022).'),
        ('Forståelse for flere forsyningsarter: vand, fjernvarme, gas, '
         'fjernkøl og spildevand',
         'Spildevand og kritiske pumpeanlæg fra driften (Biofos '
         '2017-2022). Fjernvarme som interesse og kendskab; gas og fjernkøl '
         'som nye områder, jeg ser frem til.'),
                   ],
                   widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo · Ansøgning og CV · Driftsmester, '
                       'Frederiksberg Forsyning')


if __name__ == '__main__':
    out = os.path.join(ROOT,
                       'Shahram_Ajloo_FrederiksbergForsyning_DriftsmesterKontrolrum.docx')
    build(out)
    print(out)
