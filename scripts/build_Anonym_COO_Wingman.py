# -*- coding: utf-8 -*-
"""Anonym produktionsvirksomhed, Midtjylland — COO / wingman til direktøren (erwin andersen a/s, 02.11.89).
Dansk opslag -> dansk dokument.

Form (master/FORMKATALOG.md): åbning **W** (escaleringen: hvor mange gange om dagen spørger nogen
direktøren om noget, de selv kunne have afgjort), struktur **Ugen** (mandag ordrebogen · tirsdag
leverancerne · onsdag indkøbet · torsdag kunderne · fredag tallene · måneden ledelsen), register
**Ordrebogen**.
Brugerbeslutninger 14.11.2026: »Jeg flytter gerne« (Midtjylland), og skalaafgrænsningen skal stå ærligt
i brevet som i #256/#259.
Kulturfil: jd/Anonym_COO_Wingman_kultur.txt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'COO · drift, købmandskab og ledelse af en produktionsvirksomhed'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('14. november 2026')
    m.meta('Stilling 02.11.89 · COO / wingman til direktøren · erwin andersen a/s')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: COO', bold=True, color='1A1A1A')

    def lp(text, after=42):
        return m.para(text, after=after, line=236)

    # ---------------------------------------------------------------- side 1
    lp('**Spørgsmålet er ikke, hvor mange timer direktøren arbejder — men hvor mange gange om dagen nogen '
       'spørger ham om noget, de selv kunne have afgjort.** I en ejerledet virksomhed på knap 50 mand går vejen '
       'til direktøren gennem alt: en pris, en leveringsdato, en reklamation, en ansættelse, et indkøb. Hver af '
       'de beslutninger tager et stykke af den tid, der skulle bruges på nye markeder.', after=38)

    lp('Det er den tid, stillingen skal give tilbage — og det er den slags arbejde, jeg har lavet i otte år: '
       '**fuldt ejerskab over drift og performance i organisationen**, først i mit eget selskab, hvor jeg '
       'sælger, prissætter, køber ind og leverer med egen økonomi på spil, og før det på 11 samtidige anlæg '
       'med 14 montører og 37 kapitalprojekter med 25 specialister.', after=38)

    lp('**Ugen. Seks faste punkter — og en virksomhed, der ved, hvad den gør på hver af dem.**', after=28)

    lp('**Mandag: ordrebogen.** Hvad er solgt, hvad er lovet, og hvad kan vi ikke levere i denne uge. '
       'Ordrebogen er ikke et salgsdokument; den er virksomhedens løfte, og **leveringssikkerhed** måles på, '
       'om løftet holder — ikke på, om nogen huskede at fortælle om det.', after=24)

    lp('**Tirsdag: leverancerne.** Hvad går ud, hvad mangler, og hvem ringer til kunden før kunden ringer til '
       'os. 11 samtidige anlæg og 37 afleveringer lærte mig, at en forsinkelse, der meldes i tide, koster en '
       'samtale — og en, der opdages af kunden, koster kunden.', after=24)

    lp('**Onsdag: indkøbet.** Pris, leveringstid, kvalitet og en nummer to på det, der betyder mest. '
       '**Indkøbs- og supplystrategi** er ikke et system, det er en beslutning om, hvilke leverandører man ikke '
       'kan undvære i en uge — og hvad alternativet koster, før man får brug for det.', after=24)

    lp('**Torsdag: kunderne.** Kundeservice, reklamationer og det næste salg. En reklamation, der bliver lukket '
       'samme uge med en forklaring, er billigere end en, der bliver rigtig i tredje forsøg — og den er det '
       'bedste salgsargument, man har.', after=24)

    lp('**Fredag: tallene.** Dækningsgrad, timer, lager og likviditet — fire tal, ikke tyve. Min egen '
       'virksomhed har lært mig, at **købmandskab** er evnen til at se, hvilke to af dem der er galt på vej, '
       'før regnskabet gør det.', after=24)

    lp('**Måneden: ledelsen.** Medarbejderudvikling, kompetencer og **de rigtige ressourcer i teamet** — '
       'hvem der er klar til mere, hvem der skal have hjælp, og hvad der skal være anderledes om et kvartal. '
       'Det er her, **ordentlighed** bliver til resultater i stedet for et ord på en væg.', after=32)

    lp('**Hvor min erfaring er smallere, sagt ligeud.** Jeg har ikke været COO i en produktionsvirksomhed med '
       '50 ansatte. Skalaen har været: 8 ansatte i mit eget selskab, 14 montører og 11 samtidige anlæg, 25 '
       'specialister og 37 projekter på Novo Nordisk, 12 teknikere i et værksted. Det, der vokser med opgaven, '
       'er ikke driften eller købmandskabet — dem har jeg prøvet med konsekvenser — men antallet af mennesker, '
       'man skal kende for at kunne lede dem. Det tager tid, og derfor **flytter jeg gerne** for at være der '
       'fysisk fra første dag.', after=32)

    lp('**Om opgaven og kulturen.** I skriver, at stillingen skal **give direktøren tid og plads til at skabe '
       'vækst på nye markeder**, at organisationen \u201dbindes sammen\u201d, og at virksomheden skal levere på '
       '**kvalitet, økonomi og leveringssikkerhed**. I nævner **driftsoptimering og godt købmandskab**, '
       '**koncept- og forretningsudvikling**, **afsætning** — og at du skal **motivere, udvikle og '
       'indsatsstyre en kompleks, men samtidig fagligt meget kompetent medarbejderstab**. Det er den samme '
       'opgave, jeg har løst i mindre målestok — og det er den, jeg gerne '
       'vil løse på knap 50 mand: **optimere driften og styrke processerne på tværs af hele virksomheden**, '
       'så de hænger sammen og udføres som aftalt.', after=30)

    lp('**Om menneskerne.** I beskriver **en organisation præget af ordentlighed og fokus på muligheder, '
       'indsats og resultater**, en ledelse der **»ved, hvad den vil, siger hvad den gør, og gør hvad den '
       'siger«**, og en leder med **sunde værdier og holdninger**, som organisationen kan spejle sig i. Det er '
       'den type leder, jeg selv har haft lyst til at gå til — en, der kan stå på egne ben, tage beslutningen '
       'og fortælle om den bagefter. I nævner **en høj grad af ordentlighed** som forudsætning, og I leder '
       'efter **én af de få**, der gerne vil **sidde forrest i bussen**; min tilgang er, at det følger med '
       '**gennemslagskraft, gode kontakt- og forhandlingsevner** og **en stærk kommerciel og økonomisk '
       'forståelse** — og at et menneske, man gerne vil se igen, er et menneske, der siger tingene, som de er.',
       after=30)

    lp('**Praktisk.** Jeg bor i Måløv i dag, **flytter gerne** til Midtjylland og har bil og kørekort B. Dansk '
       'er modersmål, engelsk er arbejdssprog. Ansøgningen er mærket **stilling 02.11.89**, og CV’et er '
       'vedlagt i sin fulde længde.', after=12)

    m.meta('Med venlig hilsen', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('**Leder med fuldt P&L, otte år med egen virksomhed og tolv års erfaring med drift, indkøb og '
           'projekter i reguleret industri** — 37 kapitalprojekter, 25 specialister, 14 montører, 12 teknikere. '
           'Elautoriseret maskinmester (LV/MV/HV), B.Tech i teknologiledelse, PRINCE2-certificeret. '
           'Ordrebog, leveringssikkerhed, dækningsgrad og medarbejderudvikling som daglig praksis — og et '
           'købmandskab, der er prøvet med egne penge.', after=60)

    m.section('UGEN — SÅDAN STYRER JEG DRIFTEN')
    for label, body in [
        ('Mandag: løftet',
         'Ordrebogen gennemgået linje for linje: hvad er solgt, hvad er lovet, hvad er i fare. Den samtale '
         'tager tyve minutter og sparer ugen for overraskelser.'),
        ('Tirsdag: leverancen',
         'Hvad går ud, hvad mangler, hvem ringer til kunden. En forsinkelse, der meldes først, er en aftale; '
         'en, der opdages, er en klage.'),
        ('Onsdag: indkøbet',
         'Pris, tid, kvalitet og en nummer to på de kritiske varer. Indkøb er risikostyring med en faktura '
         'på.'),
        ('Torsdag: kunden',
         'Reklamationer lukket med en forklaring, ikke en undskyldning — og et opkald til den kunde, der '
         'ikke har klaget endnu.'),
        ('Fredag: tallene',
         'Dækningsgrad, timer, lager, likviditet. Fire tal på én side, samme fire hver uge, så ændringer '
         'bliver synlige i uge to og ikke i regnskabet i måned elleve.'),
        ('Måneden: menneskerne',
         'Kompetencer, belastning, hvem der er klar til mere — og den ene stilling, der skal besættes, før '
         'den bliver et problem.'),
    ]:
        m.bullet(label, body, after=16)

    m.section('ERFARING')
    jobs = [
        ('Ejer / teknisk direktør', 'ELOHVAC ApS · København · maj 2023–nu',
         '8 ansatte · fuldt P&L · salg, indkøb og leverance',
         [('Købmandskab med egen økonomi på spil',
           'Tilbud, kalkulation, indkøb, leverandørforhandling og leverance med **fuldt P&L**; pris, '
           'dækningsgrad og likviditet besluttet af mig, og konsekvensen båret af mig.'),
          ('Drift, kapacitet og mennesker',
           '5 elektrikere og 3 lærlinge planlagt mod en ordrebog, der flytter sig; ansættelser, oplæring og '
           'daglig styring — og **over 40 % produktivitetsløft** målt i kalkulation og dokumentation.')]),
        ('Medejer og CTO / teknisk ansvarlig, AI-afdelingen',
         'Data Power Consultant ApS · København · 2024–nov. 2026 (sideløbende med ELOHVAC)',
         '4–10 personer · kundeløsninger fra krav til idriftsættelse',
         [('To organisationer, én plan',
           'Matrixledelse mellem to selskaber med skriftlige prioriteringsaftaler; selskabet er ophørt, og '
           'afdelingen er afviklet i ordnede former.'),
          ('Leverance og økonomi i samme hånd',
           'Krav, arkitektur, integration, idriftsættelse og overdragelse for kunder — med timeforbrug, '
           'fakturering og indkøb som en del af beslutningen.')]),
        ('Senior commissioning-ingeniør / projektleder, el',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('Projekter, kvalitet og leveringssikkerhed',
           'Skriftlig behovsanalyse før udstyr, **FAT/SAT**, **IQ/OQ/PQ** og **change control**; nul kritiske '
           'afvigelser ved aflevering på 37 projekter.')]),
        ('Projekt- og værkstedschef', 'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter',
         [('Kapacitet, underentreprenører og fremdrift',
           'Daglig plan for 11 anlæg og 14 montører; underentreprenører, leverandører og byggemøder '
           'koordineret, så snitflader ikke blev forsinkelser.')]),
        ('Drifts- og vedligeholdelseschef', 'Biofos (Lynetten) · København · aug. 2017–jan. 2022',
         'Renseanlæg i 24/7-drift · SCADA, PLC, HV-tavleanlæg',
         [('Drift med et tal på',
           '**Over 40 % lavere energiforbrug** gennem måling, indregulering og idriftsættelse; 24/7-vagt, '
           'hændelser og korrigerende handlinger med navngiven ejer.')]),
        ('Elektromekaniker / produktionsleder', 'ARJ Engineering · Tehran · dec. 2003–mar. 2010',
         '12 teknikere · maskinværksted · maskiner og udstyr',
         [('Værksted, kvalitet og oplæring',
           'Fejlfinding, kalibrering og reparation; rodårsagsanalyse og korrigerende handlinger; indkøb og '
           'vedligehold af udstyr; oplæring af 12 teknikere.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=16)

    m.section('UDDANNELSE, CERTIFICERING OG AUTORISATION')
    m.edu('PRINCE2 — certificeret projektleder', 'AXELOS / PeopleCert · certifikat')
    m.edu('LEAN og Six Sigma — metoder i praksis', 'DMAIC, 5S, VSM, standard work, FMEA · ikke certificeret')
    m.edu('B.Tech, teknologiledelse og maskinteknik',
          'Copenhagen School of Marine and Technical Engineering · 2017–2022 · GPA 7,6/12')
    m.edu('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('Køle- og ventilationsteknik · AMU', 'Mercantec 2021 · STCW, Søfartsstyrelsen 2021')
    m.edu('El- og maskinteknisk design, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6')

    m.section('SPROG, IT OG PRAKTISK')
    m.para('Dansk (modersmål) · engelsk (arbejdssprog) · persisk (modersmål) · **IT**: økonomi- og '
           'kalkulationsmodeller i **Excel**, **ERP** og **CMMS**, ordre- og tilbudsflow, KPI-tavler, '
           '**Python** til egen analyse · **Kørekort B og egen bil** · **flytter gerne** til Midtjylland · '
           'kan starte efter aftale.', after=40)

    m.models_table('STILLINGEN SOM BESKREVET — DET TAGER JEG MED', ('Krav', 'Dokumentation'), [
        ('Medansvar for at drive og udvikle en produktionsvirksomhed, reference til direktøren',
         'Drevet egen virksomhed med fuldt resultatansvar siden 2023 og været teknisk ansvarlig i en '
         'projektorganisation med 25 specialister — altid med en ejer eller direktør som modpart.'),
        ('Optimere driften og styrke processerne på tværs af hele virksomheden',
         'Processer bygget op, hvor de manglede: ordrebog, tilbudsflow, indkøbsaftaler, afleveringschecklister '
         'og en fast ugerytme. **Procesoptimering** og **effektivisering** målt på tid og fejl — i eget '
         'selskab og i projektorganisationer med 11–37 samtidige opgaver.'),
        ('Synlig og proaktiv lederrolle i hele resultatkæden',
         'Fra tilbud til aflevering i egen virksomhed: jeg har stået på byggepladsen, i kundemødet og i '
         'banken samme uge, fordi der ikke var andre til det.'),
        ('Organisationen skal bindes sammen og performe på kvalitet, økonomi og leveringssikkerhed',
         'Tre tal, én tavle: kvalitet (nul kritiske afvigelser på 37 projekter), økonomi (fuldt P&L) og '
         'levering (11 anlæg og 37 afleveringer til aftalt dato).'),
        ('Motivere, udvikle og indsatsstyre en kompleks og fagligt stærk medarbejderstab',
         '8 ansatte inkl. 3 lærlinge uddannet og fastholdt, 14 montører styret i daglig drift, 25 specialister '
         'koordineret. **Personaleledelse** med MUS/GRUS, 1:1 og kompetenceplaner — og **driftsansvar** for '
         'den daglige bemanding.'),
        ('Ledelse og medarbejderudvikling i en virksomhed på knap 50 medarbejdere',
         'Skalaen er ikke 50 endnu, men ledelse er prøvet i fire størrelser: 8 ansatte med lærlinge, 14 '
         'montører, 25 specialister og 12 teknikere — med ansættelse, oplæring, MUS og afskedigelser som en '
         'del af ansvaret.'),
        ('Sørge for de rigtige ressourcer i teamet',
         'Ansættelser, oplæring og omfordeling i eget selskab; i projekterne bemanding, kompetencematrix og '
         'tidlig rekruttering, før kapaciteten blev et problem.'),
        ('Indkøbs- og supplystrategi',
         'Indkøb og leverandørforhandling med egen margin: **supply chain**, pris, leveringstid, service og '
         'en nummer to på kritiske varer — **forhandling** frem for accept, og en aftale der holder i en uge '
         'uden leverandøren.'),
        ('Koncept- og forretningsudvikling',
         'Nye forretningsben i eget selskab (service, dokumentation, AI-assisteret projektering) og '
         'kundeløsninger udviklet fra behov til produktionssat løsning.'),
        ('Afsætning og udbygning af den eksisterende kundemasse',
         'Kundebasen opbygget fra nul på tre år uden en salgsorganisation bag mig — gentagne kunder er den '
         'eneste vækst, et lille selskab kan tåle at tabe.'),
        ('Driftsoptimering og godt købmandskab',
         'Dækningsgrad, timeforbrug og likviditet styret ugentligt i eget selskab; **over 40 % lavere '
         'energiforbrug** på Lynetten gennem måling og indregulering.'),
        ('Selvstændigt resultatansvar uden at blive holdt i hånden',
         'Ingen har holdt mig i hånden siden 2023: beslutningerne, risikoen og regningen har været mine, '
         'og det er den arbejdsform, jeg søger videre i.'),
        ('Gennemslagskraft samt gode kontakt- og forhandlingsevner',
         'Forhandlet med kunder, leverandører, underentreprenører og myndigheder i tyve år — på dansk og '
         'engelsk, med den samme beslutning i mødet og ikke i næste møde.'),
        ('Stærk kommerciel og økonomisk forståelse',
         'Kalkulation, budget, investeringsvurdering og likviditet som dagligt arbejde, med **nøgletal** på '
         'én side hver fredag; B.Tech i teknologiledelse og 37 kapitalprojekter med business case.'),
        ('Høj grad af vedholdenhed',
         'Projekter afsluttet, hvor de var sværest — 37 afleveringer med nul kritiske afvigelser og 11 anlæg '
         'i drift, også da tidsplanen ikke tillod det.'),
        ('Skabe struktur og synergier på tværs af virksomheden',
         'Struktur indført, hvor den gav en beslutning: én ordrebog, én ugerytme, ét sted at se tallene — og '
         'intet procesværk, der ikke ændrede noget.'),
        ('Kvalitetsprodukter til byggebranchen i hele Danmark',
         'Byggebranchen er min hverdag i dag: el- og ventilationsentrepriser, byggemøder, andre fag, '
         'tidsplaner og afleveringsforretninger — på Sjælland og opgaver i hele landet.'),
        ('Ekstremt god kundeserviceoplevelse',
         'I en virksomhed på 8 mand er kundeservice ikke en afdeling, det er telefonen: svar samme dag, '
         'aftale skriftligt, og opfølgning efter afleveringen.'),
        ('Ordentlighed og sunde værdier og holdninger som leder',
         'Løn, aftaler og afvigelser håndteret åbent; lærlinge fastholdt og uddannet, underentreprenører '
         'betalt til tiden, og dårlige nyheder sagt først.'),
        ('Vækst på nye markeder, mens driften kører',
         'Drevet virksomhed gennem vækst og gennem afviklingen af et sideløbende selskab uden at stoppe '
         'leverancerne — forandring og drift i samme kalender.'),
        ('Anonym produktionsvirksomhed i Midtjylland, ejerledet',
         'Kender ikke virksomheden endnu, og gætter ikke på den: det, der er beskrevet — ejerledet, knap 50 '
         'mand, byggebranchen — er den type virksomhed, jeg selv kommer fra.'),
        ('Ansøgning med stillingsnummer 02.11.89 og detaljeret CV',
         'Stilling 02.11.89 står i brevhovedet, og CV’et er vedlagt i sin fulde længde med perioder, tal og '
         'afgrænsninger — også dem, der ikke er til min fordel.'),
    ], widths=(2500, 7846))

    m.section('SÅDAN MÅLER JEG, OM DET VIRKER')
    for label, body in [
        ('Leveringssikkerhed',
         'Andel af ordrer leveret til den dato, der stod i ordrebekræftelsen — ikke den dato, nogen huskede '
         'bagefter. Måles hver uge, samme dag.'),
        ('Dækningsgrad pr. ordre',
         'Pris minus materialer, timer og fragt på den enkelte ordre. En samlet dækningsgrad skjuler de tre '
         'kunder, der trækker gennemsnittet ned.'),
        ('Lager og likviditet',
         'Hvor mange gange lageret drejer rundt, og hvor mange dages penge der står i det. Det er den samme '
         'beslutning set fra to sider.'),
        ('Menneskerne',
         'Sygefravær, overarbejde og hvem der er blevet bedt om mere, end de har fået hjælp til. Tallet, der '
         'kommer før de andre, er antallet af opsigelser.'),
    ]:
        m.bullet(label, body, after=16)

    m.section('DE FØRSTE 90 DAGE')
    for b in (
        'Uge 1–3: gå med i hele kæden — sælger, kundeservice, lager, produktion, montage. Lyt, mål og '
        'skriv ned; ingen ændringer før, jeg kan se, hvad der bliver gjort i dag.',
        'Uge 4–6: én side med fire tal (ordrebog, leveringssikkerhed, dækningsgrad, lager) og en fast '
        'ugerytme med dem, der ejer tallene.',
        'Uge 7–10: to forbedringer valgt efter effekt, ikke efter lyst — typisk indkøbsaftaler og '
        'afleveringsflowet — med ejer, dato og effekt opgjort.',
        'Uge 11–13: medarbejderkortet: hvem er klar til mere, hvor er der en flaskehals, og hvilken stilling '
        'skal besættes først. Derefter en status til direktøren på én side om måneden.'):
        m.bullet('', b, after=16)

    m.section('DET VILLE JEG SPØRGE OM')
    for b in (
        'Hvor i resultatkæden gør det ondt i dag: ordrebogen, leverancerne, indkøbet eller kunderne?',
        'Hvor mange beslutninger bliver i dag sendt videre til direktøren, som en afdelingsleder kunne have '
        'taget selv?',
        'Er der en produktionschef og en indkøbsansvarlig under COO’en, eller skal de roller bygges op?'):
        m.bullet('', b, after=16)

    m.para('**Jeg kommer gerne til en samtale i Midtjylland.** Kontakt: +45 93 99 95 14 · '
           'ajlooshahram@gmail.com.', after=20)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Anonym_COO_Wingman.docx')
    build(out)
    print(out)
