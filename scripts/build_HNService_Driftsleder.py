# -*- coding: utf-8 -*-
"""HN Service og KRS Service (PHM Danmark) — Driftsleder, ejendomsservice og trappevask.

Dansk leverance (opslaget er dansk): motiveringsside + CV i ét dokument.
Kultur- og rolleintel: master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md (HN/KRS/PHM-afsnit).
Policy: master/README.md — ekstrem sikkerhed, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Driftsleder · Ejendomsservice · Drift, mennesker og kunder'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('5. november 2026')
    m.meta('HN Service og KRS Service (PHM Danmark) · Storkøbenhavn')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Driftsleder til HN Service og KRS Service', bold=True, color='1A1A1A')
    m.para('Til driftschef Jan Lindum Hansen', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('Ejendomsservice er ikke en samling opgaver. Det er et løfte om, at bygningen fungerer i morgen også — at '
           'trappen er vasket, når beboerne kommer hjem, at døren går op, at varmen kører, og at den, der ringer '
           'med et problem, får et menneske i røret, der tager ansvar. Det løfte holdes af medarbejdere, der har '
           'det materiale, den plan og den oplæring, de skal bruge. Det er den slags driftsledelse, jeg gerne vil '
           'stå for hos HN Service og KRS Service.', after=80)

    m.para('**Jeg vil drive den daglige drift på fire faste ting.** Først dagen, der blev planlagt i går: bemanding '
           'og ruter lagt for de otte medarbejdere, nøgler, adgang og materialer på plads, og en plan der nemt kan '
           'lægges om, når der kommer sygdom eller en ekstraopgave — uden at kvaliteten falder. Dernæst kvaliteten, '
           'der kan ses: en klar standard for trappevask og ejendomsservice, kontrolrunder og stikprøver, afvigelser '
           'der bliver lukket med en dato og et navn, og kundens aftale og kontrakthåndtering som det, vi måles på — ikke vores egen '
           'fornemmelse. Så systemet, der bærer opgaven: hver henvendelse bliver oprettet, registreret og fulgt til '
           'ende i Microbizz med timer, billeder og faktura — ingen opgave må leve i et hoved. Og endelig '
           'menneskerne: to medarbejdere med personaleansvar og otte i den daglige koordinering, med MUS og '
           'trivselssamtaler, oplæring af nye, og en leder der selv tager fat, når det brænder.', after=80)

    m.para('Jeg har prøvet alle fire dele med ansvar for resultatet. I **ELOHVAC**, som jeg har drevet siden 2023, '
           'har jeg **fem håndværkere og tre lærlinge** og fuldt P&L: bemanding af skiftende serviceopgaver hos '
           'private og erhverv, besigtigelser, tilbud, indkøb, kvalitet og kundedialog — og en telefon, der bliver '
           'taget, når kunden ringer om noget, der er gået i stykker. Før det var jeg **projekt- og værkstedsleder '
           'i Ventek-Air** for **14 medarbejdere og 11 samtidige opgaver**, og i fem år **drifts- og '
           'vedligeholdelsesleder på Biofos, Lynetten**: et 24/7-anlæg med vand, varme, ventilation, trykluft og '
           'tekniske installationer, hvor jeg planlagde bemanding i skift, førte tilsyn, håndterede akutopkald og '
           'havde arbejdsmiljø, sikkerhed og myndighedskrav i hænderne. Hos **Novo Nordisk** løftede jeg 37 '
           'samtidige opgaver med 25 specialister, hvor kvalitetssikring og dokumentation var en del af leverancen.', after=80)

    m.para('Ejendomsservice kender jeg fra den praktiske side: jeg har selv stået med tekniske installationer, '
           'vedligehold og de mange små opgaver, der skal løses, før nogen opdager, at de var nødvendige. Jeg ved, '
           'hvad det koster at komme tilbage til en opgave, der ikke var lavet ordentligt første gang — og jeg ved, '
           'at kunden sjældent bedømmer os på det store projekt, men på om vi kom, da vi sagde vi ville, og om der '
           'var ryddet op bagefter. **Vinterberedskab** er samme disciplin som den beredskabsplan, jeg har arbejdet '
           'efter i 24/7-drift: en plan, der kan aktiveres samme aften, faste vagter, klare kriterier for hvornår '
           'der rykkes ud, og en log, så vi kan se, hvad der blev gjort og hvornår.', after=80)

    m.para('Som leder er jeg tæt på: jeg vil kende navnene, vide hvordan den enkelte arbejder bedst, og være den, '
           'der rydder forhindringer af vejen, så medarbejderne kan gøre deres arbejde ordentligt. Jeg har været '
           'igennem rekruttering, MUS, løn- og udviklingssamtaler og oplæring af lærlinge — og jeg ved, at '
           'personaleledelse i praksis handler om at være forudsigelig: aftaler bliver holdt, ros bliver givet, og '
           'kritik bliver sagt direkte og på tomandshånd. Nært samarbejde og stærkt kollegaskab kommer ikke af '
           'sig selv; det kommer af, at lederen gør det nemt at gøre det rigtige.', after=80)

    m.para('Administration og IT er ikke mit svage punkt. Jeg har arbejdet i SAP og Excel dagligt, jeg lærer nye '
           'systemer hurtigt — Microbizz vil jeg have lært i bund inden for de første uger — og i egen virksomhed '
           'har jeg bygget værktøjer i Python og Claude API, der fjernede over 40 % af det administrative arbejde i '
           'tilbud og opfølgning. Den tid vil jeg hellere bruge på kunderne og på medarbejderne.', after=80)

    m.para('Fagligt er jeg **elautoriseret maskinmester** med B.Tech i Technology Management & Mechanical '
           'Engineering: varme, ventilation, sanitet og tekniske installationer er uddannelsens kerne, og jeg har '
           'elautorisation på LV, MV og HV. Det betyder, at jeg kan vurdere en opgave fagligt, før jeg sender nogen '
           'af sted — og at jeg kan tale med både håndværkere, leverandører og bygherrer på deres eget sprog.', after=80)

    m.para('Praktisk: jeg bor i Måløv og er mobil i hele Storkøbenhavn, og jeg er på plads, hvor driften er — hos '
           'medarbejderne og ude på ejendommene, ikke ved et skrivebord. Jeg kan starte efter aftale, og jeg vil '
           'gerne høre, hvordan I i dag fordeler opgaverne mellem HN Service og KRS Service, og hvor I gerne vil '
           'hen med ejendomsservice og trappevask — så ved jeg, hvor jeg kan gøre en forskel fra første uge.', after=70)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Drifts- og produktionsleder med 20+ års erfaring fra teknisk drift, service og håndværk — '
           'elautoriseret maskinmester med B.Tech i Technology Management & Mechanical Engineering. Fem år som '
           'drifts- og vedligeholdelsesleder på et 24/7-anlæg med vand, varme, ventilation og tekniske '
           'installationer, hvor bemanding, tilsyn, akutopkald og arbejdsmiljø var den daglige opgave. Siden 2023 '
           'indehaver med fem håndværkere og tre lærlinge og fuldt P&L: serviceopgaver hos private og erhverv, '
           'besigtigelser, tilbud, kvalitet og kundedialog. Har ledet 14 medarbejdere og 11 samtidige opgaver i '
           'Ventek-Air og 37 opgaver med 25 specialister hos Novo Nordisk. Struktureret, serviceminded og tæt på '
           'medarbejderne.', after=80)

    m.section('DRIFT, SERVICE OG KOORDINERING')
    for label, body in [
        ('Daglig drift og bemanding',
         'Planlægning og koordinering af skiftende serviceopgaver: bemanding, ruter og materialer lagt forud, '
         'omlægning ved sygdom og ekstraopgaver, og opfølgning på det udførte — uden at kvaliteten falder.'),
        ('Kvalitet og kunder',
         'Klar standard for det udførte arbejde, kontrol og stikprøver, afvigelser lukket med ansvarlig og dato; '
         'besigtigelser, tilbud og kundedialog med samme svar, uanset hvem der ringer.'),
        ('Personaleledelse',
         'Personaleansvar med MUS, løn- og udviklingssamtaler, oplæring af nye medarbejdere og lærlinge; tæt '
         'daglig dialog om opgaver, trivsel og arbejdsmiljø.'),
        ('Ejendomme og teknik',
         'Varme, ventilation, sanitet, el og tekniske installationer i drift og vedligehold; fejlfinding, '
         'leverandører og håndværkere koordineret, så opgaven bliver løst i første forsøg.'),
        ('Beredskab og sikkerhed',
         'Beredskabsplaner, vagtordning og akut udrykning fra 24/7-drift; LOTO, arbejdstilladelser, '
         'arbejdspladsvurdering og sikkerhed før hver opgave — også når der er travlt.')]:
        m.bullet(label, body, after=25)

    m.models_table('VÆRKTØJER OG METODER', ('Opgave', 'Værktøj og dokumenteret brug'), [
        ('Sagsstyring og systemer',
         'Opgave oprettet, registreret og fulgt til ende med timer, billeder og faktura; Microbizz lært i bund i '
         'opstarten, og SAP og Excel i daglig brug.'),
        ('Planlægning',
         'Ugentlig bemandingsplan pr. medarbejder og ejendom, fast rytme for kontrol og opfølgning, og buffer der '
         'kan flyttes, når dagen ændrer sig.'),
        ('Kunder og aftaler',
         'Besigtigelse, tilbud og kontrakt gennemgået med kunden; aftalt ydelse, frekvens og responstid som facit '
         'for kvaliteten — og for fakturaen.'),
        ('Administration og løn',
         'Timeregistrering, lønbilag og opfølgning på timeforbrug pr. sag; tilbud og kalkulation med dækningsgrad '
         'fra egen virksomhed.'),
        ('Kvalitet og dokumentation',
         'Kontrollister, stikprøver og afvigelseshåndtering med årsag og lukning; dokumentation der kan læses af '
         'kunden og af den, der skal tage over.'),
        ('Digitale værktøjer',
         'Python, Claude API, SAP og Excel: planer, timelister, KPI-tavler og opfølgning — over 40 % af det '
         'administrative arbejde fjernet i egen virksomhed.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 håndværkere og 3 lærlinge · fuldt P&L · private og erhvervsmæssige kunder',
         [('Service og bemanding', 'Planlægning af medarbejdere på skiftende serviceopgaver, indkøb og levering, '
                                   'kvalitet og aflevering — med kunden informeret samme dag, noget ændrer sig.'),
          ('Økonomi og ledelse', 'Budget, tilbud, kalkulation og dækningsgrad; rekruttering, MUS og oplæring af '
                                 'lærlinge.'),
          ('Digitale værktøjer', 'Python og Claude API til tilbud, planer, checklister og KPI-tavler; over 40 % '
                                 'produktivitetsforbedring.')]),
        ('Senior commissioning engineer / projektleder, elsystemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle opgaver · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Kvalitet og dokumentation', 'Acceptkriterier, kontrol og auditeret aflevering med nul kritiske fund; '
                                        'afvigelser og ændringer håndteret med sporbarhed.'),
          ('Kunder og leverandører', 'Status, tid, økonomi og risiko rapporteret månedligt til ledelse og kunde; '
                                      'grænseflader mod andre fag og leverandører.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige opgaver · 2–10 mio. kr. pr. projekt',
         [('Daglig koordinering', 'Bemanding og opgaver fordelt på 11 samtidige sager; daglige tavlemøder, '
                                  'flaskehalsanalyse og tilpasning af planen undervejs.')]),
        ('Drifts- og vedligeholdelsesleder / værkstedsassistent',
         'Biofos, Lynetten · København · aug. 2017–jan. 2022',
         '24/7-anlæg · vand, varme, ventilation, trykluft, pumper, højspænding og SCADA',
         [('Drift, tilsyn og bemanding', 'Skiftplanlægning, tilsyn og forebyggende vedligehold, reservedelskritikalitet '
                                         'og kalibrering; akutopkald og udrykning uden for normal arbejdstid.'),
          ('Sikkerhed og myndighed', 'LOTO, arbejdstilladelser og arbejdspladsvurdering før hver opgave; '
                                     'miljødokumentation og tilsyn i et anlæg, der ikke måtte stoppe.')]),
        ('Elektromekaniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · industrielt udstyr',
         [('Team og oppetid', 'Vagtplanlægning og opfølgning på mål; fejlfinding, rodårsagsanalyse og korrigerende '
                              'handlinger på produktionsudstyr.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('UDDANNELSE OG AUTORISATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering',
          'Maskinmesterskolen København · 2017–2022 · gennemsnit 7,6/12')
    m.edu('Autoriseret maskin- og elinstallatør (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('El- og maskinkonstruktion, elektroteknik',
          'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Køle- og ventilationsteknik · STCW sikkerhed og maskinvagt',
          'Mercantec 2021 · Søfartsstyrelsen 2021–2023')

    m.section('SPROG, PRAKTIK OG REFERENCER')
    m.para('Dansk: modersmål · Engelsk: professionelt · Persisk: modersmål · Kørekort B · Bor i Måløv og mobil i '
           'hele Storkøbenhavn · Kan starte efter aftale · SAP og Excel i daglig brug · Referencer fra Novo Nordisk, '
           'Biofos, Ventek-Air samt kunder og leverandører i egen virksomhed på forespørgsel.', after=70)

    m.models_table('DET EFTERSPØRGER DE — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Erfaring med ejendomsservice, viceværtarbejde eller lignende',
         'Fem år som drifts- og vedligeholdelsesleder på et 24/7-anlæg med vand, varme, ventilation og tekniske '
         'installationer (Biofos); siden 2023 serviceopgaver, besigtigelser og kundedialog i egen virksomhed '
         '(ELOHVAC) — samme type opgaver som en vicevært eller ejendomsservicetekniker løser, men med '
         'ledelsesansvaret; teknisk uddannet med elautorisation LV/MV/HV.'),
        ('Forståelse for den daglige drift af ejendomme og de opgaver, der følger med',
         'Drift, tilsyn, forebyggende vedligehold og fejlfinding i hverdagen; kundehenvendelser og serviceaftaler '
         'fulgt til ende; arbejdsmiljø, myndighedskrav og sikkerhed som en fast del af driften.'),
        ('Erfaring med planlægning og koordinering af opgaver eller medarbejdere',
         'Planlægning af 14 medarbejdere og 11 samtidige opgaver (Ventek-Air), 37 opgaver med 25 specialister (Novo '
         'Nordisk) og daglig bemanding af fem håndværkere og tre lærlinge (ELOHVAC).'),
        ('Tage ansvar og skabe struktur i en travl hverdag',
         'Fuldt P&L og personaleledelse i egen virksomhed; skiftplanlægning og akutopkald i 24/7-drift; fast '
         'ugentlig rytme for plan, kontrol og opfølgning.'),
        ('Gode samarbejdsevner og god dialog med medarbejdere og kunder',
         'Kundedialog i egen virksomhed og i pharma-projekter med ledelse og bygherre; MUS, trivselssamtaler og '
         'oplæring af nye medarbejdere og lærlinge.'),
        ('Serviceminded, løsningsorienteret og godt overblik',
         'Serviceopgaver hos private og erhverv med svar samme dag; omprioritering undervejs uden at tabe kvalitet '
         'eller kunde.'),
        ('Flair for administration og IT-systemer — kendskab til Microbizz er en fordel',
         'SAP og Excel dagligt, Python/Claude API til planer, timelister og KPI-tavler; nye systemer lært i bund '
         'inden for de første uger — Microbizz som det første.'),
        ('Fleksibel og ikke bange for selv at tage fat',
         'Ejerdrevet virksomhed og 24/7-drift: ingen opgave for lille og ingen akutopgave uden for rækkevidde; '
         'arbejdstilladelser og LOTO håndteret på stedet.')])
    m.page_break()

    m.models_table('DE FØRSTE 90 DAGE — DRIFT, MENNESKER OG KUNDER', ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'Ud på ejendommene med medarbejderne og se arbejdet fra deres side. Gennemgang af kørende aftaler, '
         'opgaver, nøgler og adgang, og af Microbizz sammen med driftschefen. De første samtaler med de to '
         'medarbejdere, jeg skal være nærmeste leder for.'),
        ('Dag 30',
         'Microbizz brugt i det daglige: alle henvendelser oprettet og registreret med timer og billeder. Én samlet '
         'bemandings- og opgaveplan for de otte medarbejdere, som driftschefen kan læse, og en fast ugentlig '
         'opfølgning på kvalitet.'),
        ('Dag 60',
         'Kontrol og stikprøver gennemført på de aftaler, vi har, med afvigelser lukket og kunden informeret. '
         'Vinterberedskabet gennemgået: vagter, kriterier for udrykning, materialer og log.'),
        ('Dag 90',
         'Driften kører uden at driftschefen skal ind over hverdagen, og mine tal kan læses af andre: tid pr. '
         'opgave, kvalitet, genopkald og kundetilfredshed. Mindst én arbejdsgang er forbedret og delt — så næste '
         'sæson starter bedre end denne.')])

    m.section('PLANEN LAVES I GÅR')
    m.para('I service er dagen afgjort, før den begynder. Jeg lægger bemanding, ruter og materialer klar dagen før, '
           'så medarbejderne ved, hvor de skal være, og hvad de skal bruge — og så en sygemelding bliver en '
           'omlægning og ikke en krise. Når der kommer ekstraopgaver, prioriterer jeg efter aftale og konsekvens: '
           'det, kunden har betalt for og det, der skaber gener for beboerne, før det, der kan vente til i morgen. '
           'Og jeg fortæller kunden det samme dag, hvis noget flytter sig.', after=80)

    m.section('KVALITET ER NOGET, MAN KAN SE')
    m.para('Trappevask og ejendomsservice bliver bedømt med øjnene. Derfor skal standarden være beskrevet, så den '
           'kan undervises i og kontrolleres: hvad er færdigt, hvordan ser det ud, og hvad gør vi, når det ikke er i '
           'orden. Jeg vil lave kontrolrunder og stikprøver, og jeg vil hellere rette en fejl med det samme og tage '
           'samtalen med medarbejderen bagefter end lade den gå videre til kunden. Et genopkald er dyrere end den '
           'ekstra halve time, det koster at gøre det rigtigt første gang.', after=80)

    m.section('SYSTEMET SKAL BÆRE OPGAVEN')
    m.para('En opgave, der kun findes i hovedet på den, der fik telefonen, er en opgave, der bliver glemt. Derfor '
           'skal hver henvendelse ind i Microbizz med det samme: hvem, hvad, hvor, hvornår — og billeder, når det '
           'giver mening. Så kan vi følge op, få faktureringen rigtig og lære af det, der går igen. Jeg har gjort det '
           'samme i egen virksomhed og fjernet over 40 % af det administrative arbejde med egne værktøjer; den tid '
           'går til kunderne og medarbejderne i stedet.', after=80)

    m.section('TO VIRKSOMHEDER, ÉN DRIFT')
    m.para('HN Service og KRS Service er to lokale virksomheder med omkring 50 medarbejdere hver, og rollen går på '
           'tværs. Det er en fordel, hvis man gør det bevidst: samme standard for trappevask og ejendomsservice, '
           'samme måde at registrere og følge op på, og en fælles bemandingsplan, så en travl uge i den ene '
           'virksomhed kan løftes af ledig kapacitet i den anden. Jeg vil holde de to kulturer og kunderelationer '
           'intakte — det er netop nærheden, kunderne har valgt os for — men lade systemerne og standarderne være '
           'fælles, så driftschefen kan se hele billedet på ét sted. Kunderne er virksomheder, ejendomsselskaber, '
           'boligforeninger og private, og ydelserne spænder fra ejendomsservice og trappevask over rengøring og '
           'ventilation til vinduespolering — det er en bredde, hvor planlægning og faglig forståelse skal gå op i '
           'en højere enhed hver dag.', after=80)

    m.section('MENNESKERNE ER DRIFTEN')
    m.para('To medarbejdere med personaleansvar og otte i den daglige koordinering er ikke en stor organisation — '
           'det er en gruppe mennesker, hvor man kender hinanden, og hvor lederens adfærd smitter med det samme. Jeg '
           'vil være tæt på: vide hvordan den enkelte arbejder, hvad der motiverer, og hvad der driller. MUS og '
           'trivselssamtaler skal være en samtale og ikke en formular, og oplæring af nye skal være planlagt, så '
           'ingen bliver sendt ud på en opgave, de ikke er klædt på til.', after=80)

    m.section('KUNDEN AFGØR, OM VI ER GODE')
    m.para('En ejendomsservicekunde skifter ikke leverandør på grund af prisen alene. Kunden bliver, fordi telefonen '
           'bliver taget, fordi aftalen holder, og fordi der bliver ryddet op efter arbejdet. Derfor vil jeg bruge '
           'tid på besigtigelser og tilbud sammen med driftschefen, så det, vi lover, er det, vi kan levere — og så '
           'kontrakten bliver læst af den, der skal udføre den. Kunderne i Storkøbenhavn kender hinanden; en god '
           'sag giver den næste.', after=80)

    m.section('VINTERBEREDSKAB OG EKSTRAOPGAVER')
    m.para('Vinteren er den periode, hvor service bliver afgjort: kommer vi, før beboerne glider, og har vi saltet, '
           'inden frosten kommer? Jeg vil have planen klar i god tid — faste vagter, kriterier for hvornår der '
           'rykkes ud, materialer og udstyr på plads, og en log over hvad der blev gjort hvornår. Det er den samme '
           'disciplin som i 24/7-drift, hvor en beredskabsplan skal kunne aktiveres samme nat, og hvor det er '
           'loggen, der gør, at vi bagefter kan se, om vi gjorde det rigtige.', after=80)

    return m.save(path, title='Ansøgning og CV — Driftsleder, HN Service og KRS Service',
                  subject='Driftsledelse i ejendomsservice: drift, kvalitet og mennesker',
                  keywords='driftsleder, ejendomsservice, trappevask, bemanding, kvalitet, kunder, Microbizz, '
                           'personaleledelse')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_HNService_Driftsleder.docx')))
