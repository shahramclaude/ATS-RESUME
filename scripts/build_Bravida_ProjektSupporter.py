# -*- coding: utf-8 -*-
"""Bravida Entreprise Øst (Brøndby) — Projekt Supporter, ny nøglefunktion.

Form (master/FORMKATALOG.md): åbning **J** (citatet fra opslaget: deres egen
overskrift »Er du den, andre projektledere ringer til …?« besvares direkte),
struktur **Dokumentrækken** (mødeprotokollen · tidsplanen · tillægssagen ·
projektstatusen · sparringssamtalen), register **Byggemødet** (dagsorden,
referat, aktion, frist, mangel, besigtigelse). Kulturfil:
jd/Bravida_ProjektSupporter_kultur.txt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Projekt Supporter · entreprise, projektøkonomi og sparring'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('13. november 2026')
    m.meta('Bravida Danmark · Entreprise Øst · Brøndby · via bravida.dk')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Projekt Supporter, Entreprise Øst', bold=True, color='1A1A1A')

    def lp(text, after=60):
        return m.para(text, after=after, line=236)

    # ---------------------------------------------------------------- side 1
    lp('**»Er du den, andre projektledere ringer til, når projekterne bliver svære?«** Ja — men '
       'ikke fordi jeg har svarene på alt. Fordi jeg tager telefonen og stiller de spørgsmål, der '
       'skal stilles, før et problem bliver dyrt: hvad står der i kontrakten, hvem har lovet det, og '
       'hvornår blev det varslet? Den rolle har jeg udøvet i 20 år — som projektleder, som leverandør '
       'med fast pris og som den, der sad på bygherrens side af bordet — jeg har **»håndteret '
       'økonomi, tidsplaner, tillægsarbejder, kontrakter og interessenter«** og ved, hvad der skal til '
       'for at **»få projekterne sikkert i mål«**.', after=56)

    lp('**Hos Bravida Entreprise Øst opretter I en ny nøglefunktion**, hvor rollen skal **»bringe din '
       'projektfaglige tyngde i spil«** og **»bruge den erfaring til at styrke flere projekter '
       'samtidig«**, og hvor den skal **»støtte, udfordre og sparre med vores projektledere og '
       'projektchefer«** og have en **»central rolle som faglig sparringspartner og '
       'støttefunktion«**. Det er den rolle, jeg søger — fordi erfaringen gør mere '
       'gavn på tværs, og fordi det er **»en rolle hvor du stadig er tæt på projekterne«**. Bravida er '
       '**»Nordens førende leverandør af tekniske totalløsninger«** med **»13.000 medarbejdere, heraf '
       '3.000 i Danmark«**, og **»Vi arbejder som ét Bravida på tværs af fag og regioner«** — præcis '
       'den tværfaglighed, en projektorganisation skal kunne trække på, når el, ventilation og VVS '
       'mødes i samme tidsplan.',
       after=56)

    lp('**Fem dokumenter, rollen består af.**', after=46)

    lp('**Mødeprotokollen.** Et byggemøde er ikke et referat af, hvad der blev sagt; det er en liste af '
       'beslutninger med en ejer og en dato. Jeg har siddet med til byggemøder i 37 kapitalprojekter i '
       'en GMP-fabrik og i 11 samtidige anlægsprojekter, og det, der redder et forløb, er '
       '**»systematisk opfølgning på beslutninger og aftaler«** — samme dag, ikke næste møde.', after=40)

    lp('**Tidsplanen.** Ugeplan og hovedtidsplan skal tale samme sprog, ellers opdager man '
       '**»tidsfristforlængelser og byggepladsforlængelser«** for sent til, at de kan dokumenteres. Jeg '
       'har lagt kapacitetsmodel hver morgen for 11 projekter og 14 medarbejdere og ved, hvad en '
       'forskubbet uge koster i tillæg, når den ikke er varslet.', after=40)

    lp('**Tillægssagen.** Her afgøres dækningsgraden. Jeg har selv stået med akkord — opmåling, '
       'tildeling og regulering af mer- og mindrearbejde — og jeg har siddet med **AB 18** som '
       'leverandør med fast pris og garantiansvar. Derfor ved jeg, hvad der skal stå i et '
       '**»tillægsarbejde«**, før det udføres: hjemmel, mængde, pris og konsekvens for tidsplanen — og '
       'hvornår en tvist skal løftes, før den bliver en sag.', after=40)

    lp('**Projektstatusen.** **»Opfølgning på økonomi, kvalitetssikring og projektstatus«** er én side '
       'pr. projekt: forbrug mod kalkule, næste milepæl, de tre største risici og de beslutninger, der '
       'venter. 37 CAPEX-sager og fuldt **P&L** i egen virksomhed siden 2023 har lært mig, at en '
       'status uden tal er en mening.', after=40)

    lp('**Sparringssamtalen.** Den er rollens kerne: **»være en betroet sparringspartner for erfarne '
       'projektledere og projektchefer«** — nogen, der har prøvet det, de står i, og som ikke overtager '
       'ansvaret, men stiller spørgsmålene. Jeg har ledet 25 specialister og 14 medarbejdere og ved, '
       'hvornår man skal give et råd, og hvornår man skal tie og lade projektlederen finde svaret selv.',
       after=56)

    lp('**Det, jeg ikke har, står her.** Jeg har ikke haft titlen projektchef på en entreprise i '
       'Bravidas størrelse og ikke siddet i en koncerns projektorganisation. Til gengæld har jeg stået '
       'med økonomien, tidsplanerne, tillægsarbejderne, kontrakterne og interessenterne i egen '
       'virksomhed med fast pris og i 37 kapitalprojekter med **AB 18** som ramme — og jeg er '
       '**elautoriseret maskinmester (LV/MV/HV)** med ventilation fra Ventek-Air i bagagen, så jeg kan '
       'gå ind i en installationsentreprise uden at skulle have teknikken forklaret.', after=56)

    lp('**Jeres eget sprog er grunden til, at jeg søger.** I beskriver en **»ny funktion med stor '
       'betydning for udviklingen af Enterprise Øst«** og en kultur, hvor **»sikkerhed, trivsel og '
       'fællesskab grundlæggende værdier«**, og hvor **»de bedste resultater skabes gennem '
       'ansvarlighed, engagement og enkelhed«** og med **»videndeling og samarbejde er en naturlig '
       'del af hverdagen«** i et **»stærkt fagligt netværk«**. I skriver, at **»en god bygning gør '
       'forskellen«**, at I leverer **»velfungerende og mere bæredygtige bygninger«**, at I vil være '
       '**»klimaneutral i hele værdikæden i 2045«**, og at den nye funktion skal **»gøre en mærkbar '
       'forskel for projektorganisationen«** — mål, der kun nås, hvis nogen holder styr på tid, penge '
       'og kvalitet i hvert eneste projekt.', after=56)

    lp('**Praktisk:** jeg bor i Måløv, cirka 20 minutter fra Brøndby, og er på plads, når der er '
       'byggemøde. Dansk og engelsk, skriftligt og mundtligt, og jeg kan starte efter aftale.', after=24)

    m.meta('Med venlig hilsen', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('**Erfaren projektleder med entrepriseøkonomi og el-teknisk tyngde** — **elautoriseret '
           'maskinmester (LV/MV/HV)**, B.Tech i teknologiledelse og maskinteknik. 20+ år med tekniske '
           'entrepriser, **37 kapitalprojekter** i en GMP-fabrik, **11 samtidige anlægsprojekter** med '
           '14 medarbejdere og 25 specialister. Arbejder med **økonomi**, **tidsplaner**, '
           '**tillægsarbejder**, **AB 18** og **kvalitetssikring** — og med at gøre andre '
           'projektledere i stand til at holde deres.', after=70)

    m.section('BYGGEMØDET — DAGSORDEN, REFERAT OG OPFØLGNING')
    for label, body in [
        ('Dagsordenen',
         'Faste punkter i samme rækkefølge: **arbejdsmiljø**, fremdrift, **økonomi**, kvalitet, '
         'grænseflader og næste møde — 37 projekter i en fabrik, hvor ingen mødedeltager måtte gætte, '
         'hvad der blev besluttet.'),
        ('Referatet',
         'Beslutning med **ejer og dato**, sendt samme dag og læst op til slut; uenighed blev skrevet '
         'ned som en beslutning, ikke som en stemning — i pharma var uenighed en **afvigelse** med '
         'nummer.'),
        ('Aktionen',
         'Åbne punkter pr. projekt med navn og frist; ved hvert møde blev der lukket før der blev '
         'åbnet nyt — 11 samtidige projekter og 14 medarbejdere i 2022 uden tabte aftaler.'),
        ('Fristen',
         '**Tidsfristforlængelse** og **byggepladsforlængelse** dokumenteret, mens den skete: dato, '
         'årsag, varsling og konsekvens — ellers kan den ikke forhandles bagefter.'),
        ('Manglen og besigtigelsen',
         '**Mangel** registreret ved gennemgang og lukket med billede og dato; **besigtigelse** ved '
         '5-ugers eftersyn, og **garanti** og garantiperiode fulgt op — nul kritiske afvigelser ved '
         'aflevering på 37 projekter.'),
        ('Kvalitetsstyringen',
         '**Kvalitetsstyring** som system, ikke som held: kontrolpunkter, dokumentation og afvigelser '
         'med nummer — **LEAN** og **5S** brugt, hvor det gav overblik på tavlen, aldrig som ritual.')]:
        m.bullet(label, body, after=16)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · entreprise og service',
         [('Entrepriser, kalkulation og kontrakter',
           'Tilbud og **kalkulation** med fast pris, **AB 18** og garantiansvar; **tillægsarbejder**, '
           '**underentreprenører** og **dækningsgrad** fulgt pr. måned; **arbejdsmiljø** med APV og '
           'LOTO.')]),
        ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen',
         'Data Power Consultant ApS · København · 2024–nov. 2026 (sideløbende med ELOHVAC)',
         '4–10 personer · tekniske og industrielle applikationer',
         [('Data i beslutninger',
           'Tekniske applikationer samt **AI** i ledelsesarbejdet — rapportering, beslutningsoplæg '
           'og **KPI**-analyse; selskabet er ophørt.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('Projektstyring fra tilbud til aflevering',
           'Kravspecifikation, **FAT/SAT**, **IQ/OQ/PQ** og aflevering; **byggemøder**, '
           '**kvalitetssikring** og dokumentation bygget undervejs — nul kritiske afvigelser ved '
           'aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter',
         [('Fremdrift, kapacitet og grænseflader',
           'Dagligt tavlemøde, **kapacitetsmodel** og omprioritering samme dag; **ventilation**, '
           'kanaler og montage koordineret med underentreprenører og leverandører.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Biofos (Lynetten) · København · aug. 2017–jan. 2022',
         'Renseanlæg i 24/7-drift · pumper, højspændingstavler, SCADA',
         [('Drift, anlæg og energi',
           'Planlagt vedligehold og akut fejlfinding døgnet rundt; **over 40 % lavere energiforbrug** '
           'gennem måling og indregulering.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 teknikere · maskinværksted · maskiner og materiel',
         [('Maskiner, materiel og oplæring',
           'Fejlfinding, kalibrering og reparation af maskiner; indkøb og vedligehold af materiel; '
           'oplæring og opfølgning for 12 teknikere.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=16)

    m.section('UDDANNELSE OG AUTORISATION')
    m.edu('B.Tech, teknologiledelse og maskinteknik',
          'Maskinmesterskolen København · 2017–2022 · gennemsnit 7,6/12')
    m.edu('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('Køle- og ventilationsteknik · AMU', 'Mercantec 2021 · STCW, Søfartsstyrelsen 2021')
    m.edu('El- og maskinteknisk konstruktion, elteknik',
          'Tehran Technical University · 2000–2003 · EQF 6')

    m.section('SPROG, IT OG PRAKTIK')
    m.para('Dansk og engelsk, skriftligt og mundtligt · Persisk: modersmål · **IT**: **MS Office** med '
           '**Excel**-modeller til tidsplan, kalkule og **projektstatus**, **ERP**-arbejde (sags- og '
           'økonomidel i egen virksomhed), planlægningsværktøjer og egne **Python**-værktøjer til '
           '**KPI** og dækningsgrad · **Kørekort B og egen bil** · Måløv, cirka 20 minutter til '
           '**Brøndby** · Kan starte efter aftale · Referencer på forespørgsel.', after=50)

    m.models_table('OPSLAGETS KRAV — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Sikre opfølgning på økonomi, kvalitetssikring og projektstatus',
         'Én side pr. projekt med forbrug mod kalkule, næste milepæl og tre risici; fulgt månedligt på '
         '37 CAPEX-projekter og i egen virksomhed med fuldt **P&L** siden 2023.'),
        ('Udarbejde og vedligeholde tidsplaner, ugeplaner og projektværktøjer',
         'Hovedtidsplan og ugeplan i samme struktur, opdateret hver uge; **kapacitetsmodel** for 11 '
         'samtidige projekter og 14 medarbejdere — og en tavle, alle kunne læse.'),
        ('Deltage i byggemøder og sikre systematisk opfølgning på beslutninger og aftaler',
         'Byggemøde med fast dagsorden og referat samme dag: beslutning med ejer og dato, aktionsliste '
         'lukket før ny blev åbnet — 37 projekter i GMP og 11 anlægsprojekter.'),
        ('Koordinere med underentreprenører, leverandører og øvrige samarbejdspartnere',
         '**Underentreprenører** og **leverandører** styret mod aftalt dato i 11 entrepriser med 14 '
         'mand; grænseflader skrevet ned, før arbejdet startede — ikke efter.'),
        ('Bidrage til håndtering af tillægsarbejder, tvister og kontraktuelle forhold',
         '**Tillægsarbejder** med hjemmel, mængde og pris før udførelse; akkord med opmåling, tildeling '
         'og regulering af mer- og mindrearbejde; tvist løftet, før den blev en sag.'),
        ('Sparre med projektorganisationen omkring AB18 og entrepriseretlige forhold',
         '**AB 18** som ramme i egen virksomhed med fast pris og garantiansvar, og i 37 '
         'kapitalprojekter med bygherre, rådgivere og entreprenører omkring sig.'),
        ('Bidrage til forhandlinger ved tidsfristforlængelser og byggepladsforlængelser',
         'Forlængelse dokumenteret, mens den skete: dato, årsag, varsling og konsekvens — grundlaget '
         'for at forhandle i stedet for at forklare bagefter.'),
        ('Sikre struktur, fremdrift og opfølgning på tværs af projekterne',
         'Én porteføljeoversigt pr. uge med rødt/gult/grønt, ejer og næste beslutning; 11 samtidige '
         'projekter blev omprioriteret samme dag, når noget skred.'),
        ('Være en betroet sparringspartner for erfarne projektledere og projektchefer',
         'Ledet 25 specialister og 14 medarbejdere med **forventningsaftale** og **faglig sparring** — '
         'rådgivning uden at overtage ansvaret, og samtalen når nogen var gået i stå.'),
        ('Solid erfaring med større entrepriseprojekter',
         '20+ år med tekniske entrepriser: 37 kapitalprojekter i en GMP-fabrik, 11 samtidige '
         'anlægsprojekter med 14 mand og entrepriser med fast pris i egen virksomhed.'),
        ('Arbejdet med projektstyring fra tilbud til aflevering',
         'Kalkulation og tilbud, kontrakt, udførelse, **aflevering** og garantiperiode — hele kæden, '
         'både som leverandør og fra bygherresiden i Novo Nordisk.'),
        ('Stærk forståelse for økonomi, planlægning og kvalitetssikring',
         'Fuldt **P&L** siden 2023, **kvalitetssikring** med egenkontrol og KS-tjekliste og '
         '**projektstatus** på én side pr. måned med afvigelser lukket før overlevering.'),
        ('Indgående kendskab til AB18 og entrepriseretlige forhold',
         '**AB 18** brugt i praksis: tillægsarbejder, mer- og mindrearbejde, akkordregulering og '
         'garantiansvar; 37 projekter med kontraktuelle krav og dokumentationspligt.'),
        ('Erfaring med forhandling af tillægsarbejder og håndtering af projektmæssige udfordringer',
         'Forhandlet tillæg med underentreprenører og kunder, reguleret akkord og løst sager, hvor to '
         'hensyn ikke kunne opfyldes samtidigt — beslutningen blev taget og forklaret.'),
        ('Kendt for at skabe struktur, overblik og fremdrift',
         'Struktur er et dokument, ikke en egenskab: fast dagsorden, aktionsliste, én side pr. projekt '
         'og et ugentligt møde, hvor det røde blev besluttet — prøvet i 11 projekter og 37 sager.'),
        ('Motiveres af at dele din erfaring og styrke andre projektledere',
         'Oplært 12 teknikere, 3 lærlinge og 25 specialister; skrevet standarder sammen med dem, der '
         'skulle arbejde efter dem, og holdt sparring som fast punkt frem for kontrol.'),
        ('Erfaring med el-, ventilations- eller installationsprojekter',
         '**El** i bund som elektriker og elautoriseret maskinmester, **ventilation** fra Ventek-Air '
         'med 11 entrepriser og 14 mand, og **VVS**-, **CTS**- og **BMS**-grænseflader i 20+ år.'),
        ('Kunne begå sig på dansk både i skrift og tale',
         'Dansk og engelsk, skriftligt og mundtligt: referater, tilbud og forhandlinger på dansk i 20+ '
         'år med kunder, underentreprenører og myndigheder; persisk som modersmål.'),
        ('Baggrund som projektleder, senior projektleder eller projektchef',
         'Projektleder i 20+ år: 37 kapitalprojekter som senior idriftsættelsesingeniør og '
         'projektleder, 11 anlægsprojekter som projektleder og entrepriser som ejer og teknisk '
         'direktør.'),
        ('Bruge erfaringen strategisk og rådgivende tæt på projekterne',
         'Rådgivende rolle i praksis: tekniske vejvalg som teknisk ansvarlig og CTO, beslutningsoplæg '
         'på to sider og sparring med projektledere — uden at overtage deres ansvar.'),
        ('Arbejdssted Brøndby hos Bravida Entreprise Øst',
         'Bor i Måløv, cirka 20 minutter fra Brøndby, kørekort B og egen bil — og på plads, når der er '
         '**byggemøde**, uanset om det er klokken 7 eller 15.'),
    ])

    m.section('DE FØRSTE 90 DAGE')
    for b in (
        'Siddet med til byggemøder på tre forskellige projekter og set, hvordan referater, aktioner og '
        'tillæg bliver fulgt op i dag.',
        'Gennemgået porteføljen med projektlederne: én side pr. projekt med økonomi, tidsplan, risici '
        'og de beslutninger, der venter.',
        'Sat en fælles skabelon op for status og referat, så alle projekter rapporterer ens — og '
        'aftalt, hvem der læser den hvornår.',
        'Siddet med i de tillægssager, der kører nu, og set, hvor hjemlen mangler — så næste sag bliver '
        'dokumenteret, før den bliver dyr.'):
        m.bullet('', b, after=16)

    m.section('DET VILLE JEG SPØRGE OM')
    for b in (
        'Hvor mange projekter skal funktionen dække i starten, og hvilke tre har mest brug for det?',
        'Hvordan følges tillægsarbejder op i dag — er der en fast proces, eller afhænger det af den '
        'enkelte projektleder?',
        'Hvilken rolle skal funktionen have i forhandlinger: forberede, sidde med eller overtage?'):
        m.bullet('', b, after=16)

    m.para('**Jeg kommer gerne forbi i Brøndby** og taler igennem, hvordan funktionen tages i brug '
           'fra første uge: hvilke projekter der får mest gavn af den, hvordan status rapporteres, og '
           'hvem der læser referatet dagen efter. Kontakt: +45 93 99 95 14 · '
           'ajlooshahram@gmail.com.', after=24)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Bravida_ProjektSupporter.docx')
    build(out)
    print(out)
