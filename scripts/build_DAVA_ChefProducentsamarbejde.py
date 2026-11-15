# -*- coding: utf-8 -*-
"""DAVA Foods — Chef for Producentsamarbejde, Hadsund. Dansk opslag -> dansk dokument.

Form (master/FORMKATALOG.md): åbning **Z** (producenten er ikke en leverandør, man køber æg af — han er den,
der om få uger skal beslutte, hvor mange dyr der skal i huset, og han beslutter det ud fra det, han hørte
sidste gang, nogen ringede), struktur **Besøget** (tallene før du kører · stalden · referatet · næste sæson),
register **Staldgangen** (stald, hus, indsætning, hold, sortering, udbytte, velfærd, tilsyn, foder,
leverance). Kulturfil: jd/DAVA_ChefProducentsamarbejde_kultur.txt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Chef for Producentsamarbejde · producentrelationer, data og kapacitet'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('14. november 2026')
    m.meta('DAVA Foods · Chef for Producentsamarbejde · Hadsund · rekruttering via Sensu')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Chef for Producentsamarbejde', bold=True, color='1A1A1A')

    def lp(text, after=40):
        return m.para(text, after=after, line=234)

    # ---------------------------------------------------------------- side 1
    lp('**En producent er ikke en leverandør, man køber æg af. Han er den, der om få uger skal beslutte, hvor '
       'mange dyr der skal sættes ind i huset — og han beslutter det ud fra det, han hørte sidste gang, nogen '
       'ringede ham op.** Derfor er stillingen ikke en salgsrolle og ikke en kontrolfunktion. Den er en '
       'samtale, der skal ende med noget, producenten kan handle på: et tal han kan genkende, en sammenligning '
       'med hans eget sidste hold, og en aftale der stadig holder, når sæsonen gør ondt.', after=36)

    lp('I søger en, der bliver **DAVA Foods’ ansigt udadtil over for producenterne** og '
       '**producenternes primære indgang til organisationen** — et **centralt bindeled til virksomhedens '
       'ægproducenter**, med **direkte reference '
       'til virksomhedens direktion** og med **pakkeri og kvalitet** som de vigtigste interne medspillere. Jeg '
       'har ikke en landbrugsfaglig uddannelse og har ikke arbejdet i landbrugs- eller fødevarebranchen. Det '
       'står nedenfor, så det ikke først opdages i en samtale. Det, jeg har, er tyve år i de grænseflader, hvor '
       'en leverandør eller underentreprenør, en kunde og en myndighed skal have det samme svar i tre '
       'forskellige formater — og hvor relationen holder, fordi tallene er rigtige og aftalerne bliver fulgt op '
       'på skrift.', after=36)

    lp('**Besøget. Fire dele — og den fjerde er den, der afgør, om der kommer et femte.**', after=26)

    lp('**Tallene, før du kører.** **Kvalitet**, **sortering** og **udbytte** pr. leverance, målt mod '
       'producentens eget sidste hold og mod gennemsnittet — ikke mod en målsætning, han ikke har været med til '
       'at sætte. Kommer jeg med et tal, jeg ikke selv kan forklare, er besøget allerede tabt. Jeg har bygget '
       'målingen sådan før: fire tal på én side, de samme fire hver uge, med en navngiven ejer.', after=22)

    lp('**Stalden.** Ind ad døren, kigge sig omkring, lytte først — og derefter to ting, der kan ændres, ikke '
       'ti. Tyve år med besøg på andres arbejdsplads, byggemøder og tilsyn har lært mig, at den, der peger på '
       'elleve fejl i første besøg, får ret — og kommer ikke igen. To ting, aftalt, med en dato, giver '
       'følgeskab.', after=22)

    lp('**Referatet.** Inden for to dage: hvad vi blev enige om, hvem der gør hvad, hvornår — og hvad DAVA '
       'Foods gør i mellemtiden. Det er her, **Code of Conduct, dyrevelfærd og kvalitetskrav** bliver '
       '**handlingsplaner og dokumentation** i stedet for en mappe, og det er den samme disciplin, jeg har '
       'arbejdet under i GMP/FDA-miljøer: afvigelser med ejer, frist og skriftlig lukning, og nul kritiske '
       'afvigelser ved aflevering på 37 kapitalprojekter.', after=22)

    lp('**Næste sæson.** **Forsyningssikkerhed og kapacitetsplanlægning**: hvor mange producenter, hvor meget '
       'volumen, hvornår kommer toppen, og hvad gør vi, hvis én falder fra i maj. Kontrakten — '
       '**avlskontrakt** og producentaftale — indgås og følges op sammen med **indkøb** og ledelsen, med de '
       'betingelser der skal til for at holde, også når prisen flytter sig.', after=30)

    lp('**Hvor min erfaring er smallere, sagt ligeud.** Ingen landbrugsfaglig uddannelse, ingen erfaring fra '
       'landbrug eller fødevareproduktion, ingen producentaftaler, ingen **Power BI**, ingen '
       '**klimaberegninger** eller **ESG**-rapportering efter et anerkendt rammeværk, og ingen '
       'dyrevelfærdsaudits. Det, der kan bære, er noget andet: jeg har stået på den anden side af bordet over '
       'for leverandører og underentreprenører med egen margin på spil, jeg har haft dokumentations- og '
       'auditdisciplin som daglig betingelse, jeg har planlagt kapacitet for 11 samtidige anlæg og 14 '
       'montører, og jeg har målt og dokumenteret energiforbedringer på over 40 % — tal, der blev verificeret '
       'bagefter, ikke fortalt i en præsentation.', after=30)

    lp('**Om rollen og kulturen.** I spørger, om man **brænder for landbrug og stærke '
       'producentrelationer** — og det er ikke et spørgsmål om at kunne lide landbrug på afstand. I beskriver '
       'et **stabilt, vidensbaseret og fremtidssikret '
       'producentsamarbejde**, hvor **data og knowhow aktivt i dialogen med producenterne** skal blive '
       '**sparring og konkrete indsigter** — og hvor målet er at være **producenternes foretrukne '
       'sparringspartner**. Det er ikke et mål, man erklærer; det er noget, man får, fordi man kom med noget '
       'brugbart og holdt, hvad man sagde. Jeg er **relationsskabende, udadvendt og tillidsvækkende**, og jeg '
       'er **god til at lytte, skabe følgeskab og opbygge langvarige relationer** — også til mennesker med en '
       'helt anden baggrund end min. Jeg **navigerer naturligt på tværs af værdikæden**, og jeg er vant til at '
       'arbejde på tværs af funktioner som **indkøb, bæredygtighed og kommercielle funktioner**, og til at være '
       '**bindeled mellem produktionsenheden og producenterne**. At DAVA Foods er **Nordens førende aktør inden '
       'for æg og ægprodukter** og en del af **Danish Agro**-koncernen gør opgaven større, ikke mindre — og et '
       '**professionelt, uformelt og værdibaseret arbejdsmiljø** er den ramme, jeg selv arbejder bedst i.',
       after=30)

    lp('Jeg tænker i **værdikæde**: fra producentens hold til sorteringen, pakkeriet, hylden og kundens '
       'krav — og jeg ved, at den, der sidder i midten, skal kunne svare alle tre steder uden at ændre '
       'fakta.', after=26)

    lp('**Praktisk.** Jeg bor i Måløv, har **kørekort B og bil** og kører gerne til Jylland fast — '
       'producentbesøg er en del af arbejdet, ikke et tillæg til det. Dansk er modersmål, engelsk er '
       'arbejdssprog i både tale og skrift. CV’et er vedlagt, og jeg kommer gerne til en første samtale i '
       'Hadsund.', after=12)

    m.meta('Med venlig hilsen', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('**Leder med fuldt P&L i eget selskab siden 2023 og tolv år i drift, indkøb og projekter i '
           'reguleret industri** — 37 kapitalprojekter, 25 specialister, 14 montører, 12 teknikere. '
           'Elautoriseret maskinmester (LV/MV/HV), B.Tech i teknologiledelse, PRINCE2-certificeret, LEAN og '
           'Six Sigma som metoder i praksis. Leverandørstyring med egen margin, audit- og '
           'dokumentationsdisciplin, kapacitetsplanlægning og data på én side — prøvet med konsekvenser, ikke '
           'på kursus.', after=60)

    m.section('TALLENE, JEG VILLE LÆGGE PÅ BORDET')
    for label, body in [
        ('Udbytte pr. hold',
         'Mod producentens eget sidste hold og mod gennemsnittet — samme definition hver gang, så et fald '
         'betyder noget, og så producenten kan se, om det er ham eller sæsonen.'),
        ('Sorteringsfordelingen',
         'Hvor stor en del af leverancen ender uden for det bedste segment, og hvad det koster i kroner. Det '
         'er det tal, der flytter adfærd i stalden, fordi det kan handles på i næste uge.'),
        ('Leverance og volumen',
         'Aftalt mod leveret, uge for uge, med udsving markeret. **Forsyningssikkerhed** er ikke en '
         'månedsrapport; det er et løfte, der holder i den uge, hvor toppen rammer pakkeriet.'),
        ('Responstiden',
         'Hvor lang tid der går, fra en producent ringer, til han har et svar eller en dato. Det er den eneste '
         'KPI, producenten selv mærker — og den, der afgør, om man bliver den foretrukne indgang.'),
    ]:
        m.bullet(label, body, after=16)

    m.section('ERFARING')
    jobs = [
        ('Ejer / teknisk direktør', 'ELOHVAC ApS · København · maj 2023–nu',
         '8 ansatte · fuldt P&L · salg, indkøb og leverance',
         [('Leverandører, aftaler og egen margin',
           'Pris, leveringstid og kvalitet forhandlet og fulgt op skriftligt, med alternativer på det '
           'kritiske — **leverandørsamarbejde** med regningen hos mig, når en aftale ikke holdt.'),
          ('Kunderne som primær indgang',
           'Én telefon, én indgang: tilbud, ændringer, reklamationer og opfølgning håndteret af mig, med svar '
           'samme dag og aftalen bekræftet på mail — **relationer**, der blev gentagne ordrer.')]),
        ('Medejer og CTO / teknisk ansvarlig, AI-afdelingen',
         'Data Power Consultant ApS · København · 2024–nov. 2026 (sideløbende med ELOHVAC)',
         '4–10 personer · kundeløsninger fra krav til idriftsættelse',
         [('Data, dokumentation og overdragelse',
           'Krav, datamodeller og rapporter bygget sammen med kunden, så tallene kunne forsvares og bruges '
           'efter overdragelsen — **analyse** og formidling til folk uden teknisk baggrund.'),
          ('To organisationer, én plan',
           'Matrixledelse mellem to selskaber med skriftlige prioriteringsaftaler; selskabet er ophørt, og '
           'afdelingen er afviklet i ordnede former.')]),
        ('Senior commissioning-ingeniør / projektleder, el',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('Audit, afvigelser og handlingsplaner',
           '**Projektledelse** af 37 parallelle kapitalprojekter med **FAT/SAT**, **IQ/OQ/PQ** og '
           '**change control** og dokumentation, der kunne tåle et tilsyn uden '
           'varsel; **audits** lukket med navngiven ejer, frist og skriftlig opfølgning — nul kritiske '
           'afvigelser ved aflevering på 37 projekter.')]),
        ('Projekt- og værkstedschef', 'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter',
         [('Kapacitet og leveringsplanlægning',
           'Daglig plan for 11 anlæg og 14 montører mod leveringsdatoer, materialer og underentreprenører — '
           '**kapacitetsplanlægning** i den uge, hvor to opgaver ville lande samme dag.')]),
        ('Drifts- og vedligeholdelseschef', 'Biofos (Lynetten) · København · aug. 2017–jan. 2022',
         'Renseanlæg i 24/7-drift · SCADA, PLC, HV-tavleanlæg · køleanlæg',
         [('Målt effekt, verificeret bagefter',
           '**Over 40 % lavere energiforbrug** gennem måling, indregulering og idriftsættelse — et tal, der '
           'blev dokumenteret over fire år; 24/7-vagt, hændelser og korrigerende handlinger med navngiven ejer.')]),
        ('Elektromekaniker / produktionsleder', 'ARJ Engineering · Tehran · dec. 2003–mar. 2010',
         '12 teknikere · maskinværksted · maskiner og udstyr',
         [('Værksted, kvalitet og oplæring',
           'Fejlfinding, kalibrering og reparation med rodårsagsanalyse; indkøb og vedligehold af udstyr; '
           'oplæring af 12 teknikere.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=16)

    m.section('DET JEG SKAL LÆRE — OG HVORDAN')
    for label, body in [
        ('Branchen og sproget',
         'Hold, indsætning, foder, velfærd, avlskontrakt: lært af dem, der bruger ordene — og af de sidste '
         'tolv måneders audits og handlingsplaner.'),
        ('Tallene fra pakkeri og kvalitet',
         'Hvilke data findes i dag, hvor kommer de fra, og hvilke to tal kan producent og pakkeri måle ens.'),
        ('ESG og klimarapportering',
         'Jeg kan måle, dokumentere og verificere; rammeværket skal læres — og det starter med at finde ud '
         'af, hvem der ejer kravene i dag.'),
    ]:
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
    m.para('**Dansk** (modersmål) · **engelsk** (arbejdssprog i tale og skrift) · persisk (modersmål) · '
           '**IT**: **Excel** som arbejdsredskab til udbytte, kalkulation og kapacitet, **ERP** og CMMS, '
           'KPI-tavler, **Python** til egen **analyse** · **Power BI** har jeg ikke arbejdet i · **Kørekort B '
           'og egen bil**, kører gerne fast til Jylland · Måløv i dag · kan starte efter aftale.', after=36)

    m.models_table('STILLINGEN SOM BESKREVET — DET TAGER JEG MED', ('Krav', 'Dokumentation'), [
        ('Landbrugsfaglig uddannelse som agronom, jordbrugsteknolog, cand.agro. eller produktionsleder — '
         'eller tilsvarende praktisk og kommerciel baggrund',
         'Ingen landbrugsfaglig uddannelse. Min er elautoriseret maskinmester (LV/MV/HV) og B.Tech i '
         'teknologiledelse — den praktisk-kommercielle vej, opslaget selv åbner for, med eget selskab og '
         'fuldt P&L siden 2023.'),
        ('Solid erfaring fra landbrugs- eller fødevaresektoren',
         'Ingen. Jeg kommer fra teknisk drift, pharma og byggeri, ikke fra **landbrug** eller '
         '**fødevaresektoren** — og jeg søger ikke på et håb om, at det ikke bliver opdaget.'),
        ('Erfaring med leverandør- eller producentsamarbejde',
         'Leverandør- og underentreprenørsamarbejde i tyve år, de sidste tre med egen margin: aftaler, '
         'opfølgning, alternativer og en nummer to på det kritiske. Producentaftaler har jeg ikke indgået.'),
        ('God forståelse for de processer og værdikæder, der knytter sig til produktionen',
         'Værdikæden fra krav til leverance er min hverdag: behov, produktion, kontrol, dokumentation, '
         'levering og det første år i drift — i pharma med sporbarhedskrav på hvert trin.'),
        ('Stærk på data: kan indsamle, analysere og formidle data',
         'Fire tal på én side, samme fire hver uge, hver med en ejer; **Excel**-modeller til udbytte og '
         'kapacitet, **Python** til egen **analyse** — og formidling til dem, der ikke arbejder med tal.'),
        ('Kan kombinere data med faglig knowhow, erfaring og indsigt, så det bliver sparring og værdi',
         'Et tal uden en handling er en rapport. Mønstret er: hvad siger tallet, hvad kan producenten gøre '
         'ved det i næste uge, og hvad gør vi selv i mellemtiden — ellers bliver det ikke til sparring.'),
        ('Erfaring med Excel, Power BI eller lignende dataværktøjer',
         '**Excel** og **Python** dagligt, ERP og CMMS som datakilder, KPI-tavler bygget selv. **Power BI** '
         'har jeg ikke arbejdet i — værktøjet lærer jeg, logikken i et tal, der kan forsvares, har jeg.'),
        ('Erfaring med klima- og ESG-rapportering',
         'Ingen rapportering efter et ESG-rammeværk. Jeg har målt, dokumenteret og verificeret '
         'energiforbedringer på over 40 % på Lynetten — datadelen af opgaven, ikke rapporteringsstandarden.'),
        ('Dansk og engelsk på professionelt niveau, både i skrift og tale',
         'Dansk som modersmål og engelsk som arbejdssprog i dokumentation, leverandørmøder og internationale '
         'organisationer — skriftligt og mundtligt, også når det er svært.'),
        ('Kørekort og indstillet på regelmæssige producentbesøg, primært i Jylland',
         '**Kørekort B** og egen bil, og tyve år med besøg på andre folks arbejdsplads i hele landet. Jeg '
         'kører gerne til **Jylland** fast; hvor mange dage om ugen, der skal ligge i Hadsund, vil jeg gerne '
         'have aftalt.'),
        ('Opbygge og vedligeholde tillidsbaserede relationer til producenterne og være deres primære indgang',
         'I eget selskab var jeg den primære indgang for kunder og leverandører: én telefon, svar samme dag, '
         'aftalen på skrift. **Stærke, tillidsbaserede relationer** og **stakeholder**-ledelse på tværs af '
         'fag er bygget af gentagne gode svar.'),
        ('Sikre et stabilt og langsigtet producentsamarbejde med fokus på forsyningssikkerhed og '
         'kapacitetsplanlægning',
         '**Kapacitetsplanlægning** med konsekvens: 11 samtidige anlæg, 14 montører, 37 projekter i samme '
         'kalender, og en plan for hvad der sker, hvis en part falder fra.'),
        ('Indsamle, analysere og formidle data om kvalitet, sortering og udbytte',
         'De tre tal er de rigtige. Jeg har arbejdet med kvalitetstal, kassation og leveringspræcision med '
         'samme princip: én definition, samme dag, hver uge — og et tal producenten kan genkende.'),
        ('Fungere som bindeled mellem producenterne og særligt pakkeri og kvalitet',
         '**Bindeled mellem produktionsenheden og producenterne** er præcis den rolle, jeg har haft mellem '
         'værksted, projekt og kunde: oversætte det samme problem til tre sprog uden at ændre fakta.'),
        ('Samarbejde med planteavlere om frø, kerner og bælgfrugter: avlskontrakter, høst- og '
         'leveringsplanlægning og kvalitetsopfølgning',
         'Ingen erfaring med **avlskontrakt** eller planteavl. Leveringsplanlægning mod en sæson og en '
         'høsttop er strukturelt det samme som at planlægge mod en byggesæson — kendskabet til afgrøden er '
         'det, jeg skal lære.'),
        ('Arbejde med klimaberegninger og ESG-datarapportering på producentniveau',
         '**Klimaberegninger** på producentniveau har jeg ikke lavet. Det, jeg har, er måledisciplin: '
         'målepunkt, baseline, verifikation og et tal, der stadig var rigtigt, da andre regnede efter.'),
        ('Indgå og følge op på producent- og avlskontrakter i samarbejde med indkøb og ledelse',
         'Kontrakter og aftaler indgået og fulgt op med indkøb og ledelse i eget selskab — inklusive '
         'genforhandling, sanktioner og den samtale, hvor en aftale skal ændres uden at relationen ryger.'),
        ('Følge op på Code of Conduct, dyrevelfærd og kvalitetskrav, herunder audits, handlingsplaner og '
         'dokumentation',
         '**Dyrevelfærd** er nyt for mig. **Audits, handlingsplaner og dokumentation** er det ikke: '
         'GMP/FDA-tilsyn uden varsel, afvigelser med ejer og frist, og nul kritiske afvigelser ved aflevering '
         'på 37 projekter.'),
        ('Identificere og udvikle nye producenter samt understøtte eksisterende producenter i omstilling og '
         'udvikling',
         'Kundebasen opbygget fra nul i eget selskab, og underentreprenører udviklet fra lejlighedsvis til '
         'fast samarbejdspartner. Rekruttering af producenter kræver branchens sprog — det er min '
         'læringskurve, ikke min erfaring.'),
        ('Bidrage til udvikling og optimering af værktøjer og processer for producentsamarbejdet',
         'Processer og værktøjer bygget, hvor de manglede: ordrebog, afleveringschecklister, '
         'kapacitetsmodel og en ugerytme — og **over 40 % produktivitetsløft** fra digitalt understøttede '
         'arbejdsgange i eget selskab.'),
        ('Relationsskabende, udadvendt og tillidsvækkende med lytteevne og følgeskab',
         'Tyve år med kunder, leverandører, håndværkere og myndigheder, hvor tillid var det eneste, der '
         'gjorde næste opgave mulig: kom med noget brugbart, sig sandheden tidligt, og hold, hvad du lover.'),
        ('Analytisk, grundig og struktureret, selvstændig med ejerskab og forretningsforståelse på tværs af '
         'værdikæden',
         'Struktur, der ender i en beslutning: én side, tre valgmuligheder og en anbefaling med modargumentet '
         'skrevet ned — og **forretningsforståelse** med eget P&L som målestok, ikke som teori.'),
    ], widths=(2500, 7846))

    m.section('DE FØRSTE 90 DAGE')
    for b in (
        'Uge 1–3: med i stalden og i pakkeriet. Lær navne, hold og sprog — og læs de sidste tolv måneders '
        'data igennem, før jeg siger ét ord om dem.',
        'Uge 4–6: én side med fire tal pr. producent (udbytte, sortering, leverance, responstid), samme '
        'definitioner som pakkeri og kvalitet bruger i dag, og en fast kadence for, hvornår de går ud.',
        'Uge 7–10: de første ti besøg med data under armen og højst to aftaler med hjem hver gang — plus en '
        'skriftlig opfølgning inden for to dage, hver gang, uden undtagelse.',
        'Uge 11–13: kapacitetsbilledet for de næste tolv måneder: antal producenter, volumen, sæsonens top og '
        'de huller, der skal lukkes med nye producenter eller ændrede aftaler. Status til direktionen på én '
        'side.'):
        m.bullet('', b, after=14)

    m.section('DET VILLE JEG SPØRGE OM')
    for b in (
        'Hvor mange producenter er tilknyttet i dag, og hvad er den største udfordring set fra deres side af '
        'bordet?',
        'Skal rollen have fast base i Hadsund, eller kan den køres med faste rejsedage og producentbesøg?',
        'Er Power BI på vej ind, eller skal det bygges — og hvilke ESG-krav rapporterer I efter i dag?'):
        m.bullet('', b, after=14)

    m.para('**Jeg kommer gerne til en samtale i Hadsund — eller ud i en stald, hvis det er der, beslutningen '
           'bliver taget.** Kontakt: +45 93 99 95 14 · ajlooshahram@gmail.com.', after=16)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_DAVA_ChefProducentsamarbejde.docx')
    build(out)
    print(out)
