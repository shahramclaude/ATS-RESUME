# -*- coding: utf-8 -*-
"""Artelia Danmark — Projektleder med teknisk baggrund til komplekse projekter i drift, Søborg.

Form (master/FORMKATALOG.md): åbning **A** (placeringen: kvaliteten afgøres et andet sted,
end man tror), struktur **Snitfladerne** (driften · brugerne · projekteringen · entreprenøren ·
myndigheden og brand), register **Etaperne** (nyt: etape, omlægning, midlertidig løsning,
afspærring, adgangsvej, vandafbrydelse, spændingsløs, genopretning).
Kulturfil: jd/Artelia_ProjektlederKomplekseProjekter_kultur.txt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Projektleder · komplekse projekter i drift'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('12. november 2026')
    m.meta('Artelia Danmark · Buddingevej 272, 2860 Søborg · att. afdelingsleder Mads Emil Andersen, HVAC & Utilities')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Projektleder, komplekse projekter i drift', bold=True, color='1A1A1A')

    # ---------------------------------------------------------------- side 1
    m.para('**En ombygning i drift bliver ikke afgjort på byggepladsen.** Den bliver afgjort i den uge, '
           'hvor nogen skal lukke en ventilationskanal, der betjener et område, der ikke må lukkes — '
           'og hvor det viser sig, om nogen havde tænkt på køleanlægget, brandalarmen og den '
           'midlertidige strømforsyning, før mødet blev aflyst. Jeg har siddet på den anden side af '
           'den beslutning i 20+ år: som driftsleder for et anlæg, der ikke måtte stoppe, og som '
           'projektleder i en fabrik, der kørte videre, mens vi byggede.', after=60)

    m.para('**Artelia er 1.400 rådgivere i Danmark og en del af en koncern på over 10.000 i mere end 40 '
           'lande** — starkast i Nordics med Olav Olsen og HNIT. Opgaverne i denne stilling ligger i '
           'lufthavne, transportbygninger, industri og produktion, hvor adgangsforhold, '
           'passagerflow og kritiske funktioner skal tænkes ind fra første dag. Det er den slags '
           'projekter, jeg kender fra indersiden af bygherreorganisationen — ikke fra tilbudssiden.',
           after=60)

    m.para('**Fem snitflader, der afgør, om et projekt i drift lykkes.**', after=50)

    m.para('**Driften.** Den skal køre, mens vi bygger. Fem år på Lynetten i 24/7-drift betyder, at jeg '
           'har prøvet at være den, der skulle sige ja til at tage en pumpestrøm, en ventilationskreds '
           'eller et kontrolanlæg ud — og som skulle stå med ansvaret, hvis det ikke kom tilbage til '
           'tiden. Isolering, LOTO, skriftlig tilladelse og en genopretningsplan, der er godkendt '
           'inden nedlukningen, er ikke bureaukrati; det er det, der gør, at næste nedlukning er '
           'tidsmæssigt aftalt og ikke politisk.', after=44)

    m.para('**Brugerne.** I en lufthavn er brugeren passageren, i en produktionsvirksomhed er han '
           'operatøren, og i et hospital er hun den, der ikke kan flyttes. Jeg har arbejdet i en '
           'GMP-fabrik, hvor adgangsprocedurer og dokumentationskrav gjaldt også for entreprenøren, '
           'og hvor en ændring i et rum skulle godkendes, før nogen tog en vinkelsliber frem. '
           'Brugerne skal inddrages, før låsen er bestilt — bagefter er det bare en klage.', after=44)

    m.para('**Projekteringen.** Jeg bliver ikke nødvendigvis den, der projekterer. Men jeg skal kunne '
           'læse et projekteringsgrundlag og se, hvor det ikke hænger sammen: en kanal, der kræver 40 '
           'cm mere, end der er plads til; en tavle, der ikke kan udvides i den eksisterende '
           'elsekant; et CTS-punkt, som driften aldrig får kalibreret. I 37 kapitalprojekter var min '
           'rolle at stille de spørgsmål, der gjorde, at 25 specialister kunne projektere noget, der '
           'kunne bygges — og at afvise det, der ikke kunne.', after=44)

    m.para('**Entreprenøren.** Jeg har været ham, der skulle have adgang, materialer og tid — og '
           'kender derfor prisen på en etape, der ikke kan udføres som planlagt. Entrepreneuren skal '
           'have en plan, han kan tro på, og en ændring, der er godkendt, før han udfører den. Jeg har '
           'siddet med budget 2–10 mio. kr. pr. projekt, AB 18 og ændringshåndtering fra begge sider '
           'af bordet, og i egen virksomhed med fuldt P&L siden 2023.', after=44)

    m.para('**Myndigheden og brand.** Brand, ABA/ABV, nød- og panikbelysning, arbejdsmiljø og '
           'dokumentation er ikke en fase til sidst; det er de krav, der ændrer etaperne. Jeg har '
           'afleveret 37 projekter med nul kritiske afvigelser, fordi dokumentationen blev bygget '
           'undervejs — og fordi 1- og 5-års gennemgangen er lettere, når nogen har tænkt over det i '
           'uge tre.', after=60)

    m.para('**Jeg er ikke rådgivende ingeniør, og jeg har ikke haft et projekt i en lufthavn.** Det skal '
           'være sagt. Det, jeg har, er teknisk baggrund som **elautoriseret maskinmester (LV/MV/HV)**, '
           'projekter i eksisterende anlæg under drift, entreprise og drift fra begge sider af bordet '
           'samt to år med 37 parallelle projekter i en GMP-fabrik, hvor ingenting måtte standses. '
           'Rådgiverrollen lærer jeg — spørgsmålene og rækkefølgen har jeg med.', after=60)

    m.para('**Jeres eget sprog er grunden til, at jeg søger:** **»ikke langt til handling«**, en '
           '**åben og involverende kultur**, **korte beslutningsveje og handlekraftige ledere**, en '
           'arbejdskultur bygget på **høj faglighed, tillid og dialog** og en **uformel omgangstone**. '
           'I skriver selv, at **Projektmodellen er vores værktøj og vejviser**, at **Artelia Akademi** '
           'understøtter udviklingen, og at **vi rekrutterer de fleste ledere internt** — det er en '
           'organisation, hvor metode er fælles gods og ikke den enkeltes hovedpine. Der er **frihed '
           'under ansvar**, og **trivsel, samarbejde og arbejdsforhold prioriteres højt**; der er **et '
           'stærkt fagligt netværk**, og **mangfoldighed som en styrke** er ikke kun en sætning i '
           'opslaget. Og I skriver det, stillingen virkelig kræver: **driften skal opretholdes under '
           'ombygningen**, og **du ser ikke driften som en forhindring, men som en grundlæggende '
           'forudsætning**. Det er præcis den indstilling, der gør, at man finder **kritiske '
           'grænseflader, før de bliver til problemer** — og at man, som I selv formulerer det, kan '
           '**tage ansvar og følger aftaler helt til dørs**.', after=60)

    m.para('**Praktisk:** jeg bor i Måløv, 20 minutter fra Søborg og 30 fra Valby, har kørekort B og '
           'bil og kan arbejde fra begge kontorer. Dansk og engelsk, skriftligt og mundtligt. Jeg kan '
           'starte efter aftale. Det, jeg gerne vil høre om, er, hvordan I i dag vægter '
           'projekteringsledelse mod udførelsesledelse i den type opgaver — og hvem der sidder med '
           'driftsorganisationen, når etapeplanen skal godkendes.', after=50)

    m.meta('Med venlig hilsen', after=15)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('**Projektleder med teknisk baggrund** — **elautoriseret maskinmester (LV/MV/HV)**, B.Tech i '
           'teknologiledelse og maskinteknik. Har ført **37 parallelle kapitalprojekter** på 2–10 mio. '
           'kr. i en GMP-fabrik i drift, ledet **11 samtidige anlægsprojekter** med **14 medarbejdere** '
           'og drevet egen virksomhed med **fuldt P&L** siden 2023. Ansvarsområder: **projektering**, '
           '**udbud**, **udførelse**, **tilsyn**, **aflevering**, **økonomi** og **interessenter** — '
           'med **dokumenteret effektivisering over 40 %** gennem måling og systematisk opfølgning.',
           after=70)

    m.section('ETAPERNE — PROJEKTER, DER KØRER SAMTIDIG MED DRIFTEN')
    for label, body in [
        ('Etaper og omlægninger',
         'Arbejdet deles i etaper, der kan udføres, mens anlægget kører: **omlægninger** aftalt i '
         'skriftlig rækkefølge, **midlertidige løsninger** med en ejer og en varighed, og en '
         'genopretningsplan, der er godkendt, før nedlukningen begynder.'),
        ('Afspærring og adgang',
         '**Adgangs**forhold planlagt som en del af projektet: hvem der må være hvor, hvornår, og '
         'hvordan en **afspærring** flytter sig, når etape to starter — i en GMP-fabrik med '
         'adgangskontrol og i egen virksomhed på skiftende byggepladser.'),
        ('Vandafbrydelse og spændingsløs',
         '**Spændingsløs** og **vandafbrydelse** som planlagte hændelser med **sikkerhed** i '
         'centrum, LOTO, tavlelås, '
         'varslingstid til driften, kontrolmåling før og efter og en navngiven, der må kvittere for '
         'genindkobling — fem år i 24/7-drift uden at anlægget stod uden grund.'),
        ('Økonomi og ændringer',
         '**Budget** 2–10 mio. kr. pr. projekt, **risici** i et register med ejer og dato, '
         '**leverancer** i en plan og ændringer godkendt før udførelse; fuldt **P&L** siden 2023 '
         'med månedlig afvigelsesforklaring.'),
        ('Interessenterne',
         '**Bygherre**, **brugere**, **driftsorganisation**, **rådgiver**, **entreprenør** og '
         'myndighed holdt i samme plan gennem **koordinering** på **projekterings-, status- og '
         'koordineringsmøder**, med '
         'beslutningslog, navn på ejer og dato for næste svar.'),
        ('Bygbarheden',
         'Krav, der kan bygges: FAT/SAT og **tilsyn** før aflevering, mangellister lukket med navn og '
         'dato og **nul kritiske afvigelser** i 37 projekter under GMP/FDA/EMA.')]:
        m.bullet(label, body, after=16)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · entreprise og service',
         [('Entreprise, økonomi og kunder',
           '**Udbud** og **tilbud**, ændringshåndtering, underentreprenører og **aflevering**; '
           '**økonomi** og **kvalitet** fulgt månedligt; arbejdsmiljø med APV, LOTO og '
           'sikkerhedsrundering.')]),
        ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen',
         'Data Power Consultant ApS · København · 2024–nov. 2026 (sideløbende med ELOHVAC)',
         '4–10 personer · tekniske og industrielle applikationer',
         [('AI i projekt- og ledelsesarbejde',
           '**AI coding** til tekniske anlæg og industrielle komponenter, kundeløsninger med '
           'LLM-API\'er og AI i ledelsesarbejdet — ledelsesrapportering, beslutningsoplæg og '
           'KPI-analyse; selskabet er ophørt.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('Projektering, udførelse og aflevering',
           'Kravspecifikation, **projektering** med 25 specialister, FAT/SAT, IQ/OQ/PQ og '
           '**aflevering** — i en fabrik der kørte videre, og med nul kritiske afvigelser.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter',
         [('Fremdrift i flere parallelle projekter',
           'Dagligt **tavlemøde**, kapacitetsanalyse og omprioritering samme dag; **udbud**, '
           'underentreprenører og afleveringspakker med **dokumentation**.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Biofos (Lynetten) · København · aug. 2017–jan. 2022',
         'Renseanlæg i 24/7-drift · pumper, bassiner, SCADA',
         [('Drift, der ikke må stoppe',
           'Vedligehold og ombygning udført i **drift**: isolering, LOTO, varsling og '
           'genopretning; **over 40 % lavere energiforbrug** gennem måling og indregulering.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 teknikere · maskinværksted · maskiner og materiel',
         [('Værksted og materiel',
           'Fejlfinding, kalibrering og reparation; indkøb og vedligehold af maskiner og bilpark; '
           'oplæring og målopfølgning for 12 teknikere.')]),
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
    m.para('Dansk og engelsk, skriftligt og mundtligt · Persisk: modersmål · **IT**: ERP-baserede '
           'projekt- og økonomisystemer, Excel, egne **Python**-værktøjer til tid, **KPI** og '
           'rapportering; **mødeledelse** med referat, beslutningslog og navn på ejer; kendskab til **BIM**-baseret projektsamarbejde og dokumentationsflow · '
           '**Kørekort B og egen bil** · Måløv, 20 minutter fra Søborg · Kan starte efter aftale.',
           after=50)

    m.models_table('OPSLAGETS KRAV — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Drive projekter fra de første afklaringer til projektering, udførelse og aflevering',
         '37 kapitalprojekter fra krav til **aflevering**, 11 anlægsprojekter fra specifikation til '
         'formel aflevering og egen virksomhed, hvor jeg både afklarer, projekterer og afleverer.'),
        ('Projekter i bygninger og anlæg, hvor driften skal opretholdes under ombygningen',
         '5 år i 24/7-drift på Lynetten og 2 år i en GMP-fabrik, der kørte videre under '
         'ombygningen — **drift** og byggeri i samme bygning, hver dag.'),
        ('Erfaring som projektleder eller projekteringsleder',
         '**Projektleder** for 37 parallelle kapitalprojekter og for 11 samtidige anlægsprojekter '
         'med 14 medarbejdere; **projektering** styret med 25 specialister og FAT/SAT.'),
        ('Teknisk baggrund inden for VVS, ventilation, CTS, el, byggeri eller installationer',
         '**Elautoriseret maskinmester (LV/MV/HV)** med **el** i bund, **ventilation** fra '
         'Ventek-Air og køleteknik/klima fra AMU; **CTS**-sætpunkter, alarmer og tidsprogrammer '
         'arbejdet med i drift.'),
        ('Erfaring med ombygning i eksisterende bygninger eller anlæg',
         'Ombygning og modernisering i eksisterende bygninger og anlæg i 20+ år — eksisterende '
         'elsekanter, kanaler og tavler er den ramme, jeg har arbejdet i, ikke undtagelsen.'),
        ('Trives i projekter, hvor driften skal opretholdes under udførelsen',
         'Døgndrift i 5 år med akut fejlfinding om natten og projekter i 11 samtidige forløb, hvor en '
         'aftale — ikke en mulighed, man tog sig.'),
        ('Styre økonomi, tidsplan, kvalitet og interessenter',
         '**Budget** 2–10 mio. kr. pr. projekt, tidsplan med milepæle, kvalitet via KS og '
         'afleveringspakke og interessenthåndtering med beslutningslog — alle fire i samme '
         'månedsrapport.'),
        ('Forståelse for tekniske installationer og tværfaglige afhængigheder',
         'El, ventilation, køl, CTS, brand og konstruktioner koordineret i 37 projekter med 25 '
         'specialister — afhængighederne blev navngivet i en matrix, før de blev til forsinkelser.'),
        ('Bevare overblikket, når forudsætningerne ændrer sig',
         'Da forudsætningerne skred i 11 samtidige projekter, blev rækkefølgen besluttet på tavlen '
         'kl. 6.30 samme dag — ikke i en mail tre dage senere.'),
        ('Kommunikere klart og respektfuldt med tekniske og ikke-tekniske interessenter',
         'Dansk og engelsk på alle niveauer: værkstedet, driftsorganisationen, bygherren, '
         'myndigheden og direktionen — beslutningsoplæg på 1-2 sider og referater med navn og dato.'),
        ('Omsætte komplekse problemstillinger til tydelige beslutninger og handlinger',
         'Metoden er den samme hver gang: 3 alternativer, konsekvens for tid, pris og drift, og en '
         'anbefaling — beslutningsgrundlaget forelå, når mødet startede.'),
        ('Tage ansvar og følge aftaler helt til dørs',
         'Mangellister lukket med navn og dato, 1- og 5-års gennemgange fulgt op og nul kritiske '
         'afvigelser ved aflevering i 37 projekter.'),
        ('Skabe en tydelig retning for projektteamet',
         '1 side pr. projekt: mål, næste milepæl, hvem der ejer hvad — brugt i 37 projekter og i 11 '
         'samtidige anlægsprojekter med 14 medarbejdere og underentreprenører.'),
        ('Inddrage drift og brugere på de rigtige tidspunkter',
         'Driften inddraget før låsen blev bestilt: i 24/7-drift som den, der skulle sige ja, og i '
         'GMP som den, der skulle godkende en ændring i et rum.'),
        ('Opdage kritiske grænseflader, før de bliver til problemer',
         '**Grænseflader** navngivet i en matrix ved projektstart — el mod ventilation, CTS mod '
         'brand, entreprenør mod drift — med en ejer og en frist for hver.'),
        ('Sikre realistiske etaper og gennemførelsesplaner',
         '**Etaper** lagt efter driftens vinduer, ikke efter entreprenørens ønske; 11 samtidige '
         'projekter styret i faser med midlertidige løsninger, varighed og genopretning planlagt på '
         'forhånd.'),
        ('Levere løsninger, der både fungerer teknisk og kan gennemføres i praksis',
         '**Bygbarhed** prøvet af, før det blev besluttet: som entreprenør på skiftende byggepladser '
         'og som driftsleder, der skulle overtage det bagefter.'),
        ('Koordinere tekniske fag som ventilation, VVS, el, CTS, konstruktioner og brand',
         '**Ventilation**, **el**, **CTS**, **brand** og **konstruktioner** i samme plan i 37 '
         'projekter; VVS og køl fra Ventek-Air og AMU-køleteknik.'),
        ('Lede projekterings-, status- og koordineringsmøder',
         'Fast kadence: projekteringsmøde med fagdisciplinerne, statusmøde med beslutninger og '
         'koordineringsmøde på pladsen — i 37 projekter uden at møderne blev målet i sig selv.'),
        ('Håndtere interessenter med forskellige behov og prioriteringer',
         '**Interessenter** med modstridende krav — produktion mod byggeri, drift mod fremdrift, '
         'økonomi mod kvalitet — håndteret ved at gøre konflikten eksplicit og beslutte den et sted.'),
        ('Samarbejde tæt med bygherre, brugere og driftsorganisation',
         '**Bygherre** og **driftsorganisation** i samme rum i 20+ år: i Novo Nordisk som bygherres '
         'projektleder, i Biofos som driftsleder og i egen virksomhed som begge dele.'),
        ('Følge projektet gennem projektering, udbud, udførelse, tilsyn og aflevering',
         'Hele kæden: **udbud** og kontrakt, **udførelse**, **tilsyn** og **aflevering** — i 37 '
         'projekter og i 11 anlægsprojekter med underentreprenører og afleveringspakker.'),
        ('Bidrage til planlægning af etaper, omlægninger og midlertidige løsninger',
         '**Omlægninger** planlagt som selvstændige hændelser med varsling, kontrol og genopretning; '
         '**midlertidige løsninger** med en ejer, en varighed og en dato for, hvornår de fjernes.'),
        ('Stille de rigtige spørgsmål og udfordre projektets forudsætninger',
         'Spørgsmålene stillet tidligt: hvad koster det at bygge det her, mens anlægget kører — og '
         'hvad koster det at lade være. Det spørgsmål har sparet flere projekter end en ekstra '
         'rådgiver.'),
        ('Sikre, at løsningerne er byg- og gennemførlige',
         'Løsninger prøvet mod virkeligheden, før de blev tegnet færdige: plads, adgang, løft, '
         'rækkefølge og nedlukningsvinduer — i 37 projekter og i egen udførelse hver uge.'),
        ('Erfaring fra lufthavne, transport, industri, hospitaler, laboratorier, datacentre eller andre driftskritiske miljøer',
         '**Industri** og **driftskritiske** miljøer: GMP-fabrik i drift i to år, renseanlæg i 24/7 i '
         'fem år og egen virksomhed med akutte udkald. **Lufthavne** er ikke på CV\'et — det står '
         'også i brevet.')])

    m.section('DE FØRSTE 90 DAGE')
    for b in (
        'Læst projekterne igennem med afdelingsledelsen og valgt de to, hvor grænsefladerne er '
        'dårligst beskrevet — og skrevet dem ned, før de bliver til forsinkelser.',
        'Sat én side op pr. projekt: etaper, nedlukningsvinduer, beslutningslog og næste milepæl med '
        'navn og dato.',
        'Gået en runde med driftsorganisationen på det første projekt og spurgt, hvad de plejer at '
        'få at vide for sent — og rettet møderækkefølgen efter svaret.'):
        m.bullet('', b, after=16)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Artelia_ProjektlederKomplekseProjekter.docx')
    build(out)
    print(out)
