#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Maskinmester — Sweco, Roskilde. Dansk opslag -> DANSK dokument (4 sider).
TEMPLATE Gentofte-2027.

SWECO = GENANSØGNING (fem tidligere: IndeklimaEnergiingenioerFagansvar,
ProjektlederVandKlima, SeniorEnergiplanlaegger, TekniskProjektlederHVACVVS
x2). INTET GENBRUGES fra dem: ny åbning (CA), nyt register, ny struktur,
nye formuleringer. KIT fra ældre Sweco: indeklima siden 2003, dagslys/
akustik/fugt NEJ (ikke relevant for denne rolle).

Job: Maskinmester, rådgivning og projektering af tekniske installationer og
anlæg; tværfagligt team; byggeri, medicinalindustri, anlæg, veje, energinet,
jernbaner, datacentre, energi; projekter i Finland (tidl. Italien/USA).
Fagledelse som mulighed. Dansk skriftligt og mundtligt. Kontakt Rawi Barakzai
(rawi.barakzai@sweco.dk, 42 82 13 49) -> hilsen "Kære Rawi Barakzai,".
Frist 13. december 2026. Samtaler løbende.

KIT-BÆRENDE: uddannet maskinmester + elaut. (LV/MV/HV) SELVSIKKERT.
"Rådgiverbranchen ELLER beslægtet teknisk rolle" -> den beslægtede rolle
(udførelsesiden), rådgiverbranchen som sådan = hedge. Projektering = design-
siden (AutoCAD, maskinteknisk design) + udførelsessiden; tilsyn/fagtilsyn =
fra entreprenørsiden. GMP/medicinal = Novo (selvsikkert). Jernbaner/data-
centre = projekter man kan bidrage til, ikke erfaring der claims. Lokation
Roskilde = kort tur fra Måløv (Ringsted=ja + Næstved=commute_ok-præcedens;
flagges i rapport). Ingen em dash. Banned: 'gøre en forskel'/'brænder'/
'dynamisk'/'passioneret' findes ikke i dette JD.

STIL (3/3 mod #450 Frederiksberg): register "Jordnær rådgivning, skarp
projektering", åbning CA (løsningen bedømt to gange), struktur "Idéer,
grænseflader, udførelse". Hver matrix-række >= 110 tegn (DYBDE 13.11).
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_Gentofte_DriftslederEjendomme_2027.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Sweco · Maskinmester · Roskilde'
BANNER_RESUME = 'PROJEKTERING · INSTALLATIONER · TVÆRFAGLIGT SAMARBEJDE'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('2. december 2026')
    m.meta('Sweco · Maskinmester · Rådgivning og projektering')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning om stillingen som maskinmester', bold=True,
           color='1A1A1A')
    m.para('Kære Rawi Barakzai,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('En teknisk løsning bliver bedømt to gange: på tegningen og i '
       'driften, når anlægget skal fungere for dem, der skal bruge det. Hos '
       'Sweco er det maskinmesterens opgave at holde de to vurderinger '
       'sammen: rådgivning om og projektering af tekniske installationer og '
       'anlæg, koordinering af grænseflader mellem de tekniske fag og '
       'fagtilsyn, mens løsningen bliver ført ud i livet. Jeg søger '
       'stillingen, fordi jeg har stået på den anden side af tegningen. Jeg '
       'har bygget, idriftsat og drevet de anlæg, som projekteringen skal '
       'holde styr på, og jeg ved, hvor det gør ondt, når en grænseflade '
       'ikke er afstemt. At omsætte kundens behov til løsninger, der '
       'fungerer i praksis, er den disciplin, jeg kender fra udførelsen, og '
       'et tværfagligt team, hvor de tekniske løsninger fungerer sammen på '
       'tværs af fag, er rammen, jeg gerne vil arbejde i.')

    lp('Uddannet maskinmester med elautorisation LV/MV/HV og mere end 20 år '
       'i tekniske installationer: el, VVS og ventilation i service og '
       'entreprise, commissioning af kritiske anlæg i medicinalindustrien '
       'og drift af forsyningsanlæg. I dag er jeg elautoriseret maskinmester '
       'og CTO for AI-afdelingen hos Data Power med ansvar for el-teknik og '
       'ventilation, service og entreprise og 5 elektrikere med 3 '
       'lærlinge. Mindst to års erfaring er dækket mange '
       'gange, og den kommer fra en beslægtet teknisk rolle frem for '
       'rådgiverbranchen; den erfaring fra udførelsesiden er samtidig det, '
       'jeg kan byde ind med. Projektering kender jeg fra designsiden i '
       'AutoCAD og maskinteknisk design, og fra projekter hvor tegningerne '
       'skulle holde helt ind i driften. Kvalitetssikring og dokumentation '
       'har jeg fra 37 commissioning-projekter hos Novo Nordisk, hvor '
       'medicinalindustriens krav til GMP, IQ/OQ/PQ og frigivelse satte '
       'standarden. Fagtilsyn og opfølgning under udførelsen har jeg '
       'praktiseret fra entreprenørsiden på byggepladser med 14 mand og '
       'underentreprenører, og faglig sparring med kolleger og kunder om '
       'valg af tekniske løsninger har været en daglig disciplin i '
       'servicebranchen.')

    lp('De første 90 dage følger projektets rytme: idéer, grænseflader, '
       'udførelse. Første måned går til idéerne og teamet; jeg kommer ind i '
       'de løbende projekter, lærer jeres måde at projektere på, og ser, '
       'hvordan de første idéer bliver til valg, kunden kan stå på. Næste '
       'måned er grænsefladerne: koordinering mellem fagene, dér hvor el, '
       'VVS, ventilation og styring mødes, og hvor projekteringen enten '
       'holder eller knækker. Tredje måned er udførelsen: fagtilsyn og '
       'opfølgning, mens løsningen bliver bygget, udvikling, optimering og '
       'kvalitetssikring af tekniske løsninger undervejs, og faglig sparring '
       'med kolleger og kunder, når valgene skal træffes. I opslaget står '
       'der mulighed for at påtage dig fagledelse, hvis det passer til din '
       'erfaring og dine ambitioner; med ledelseserfaring siden 2003 passer '
       'det til mig. Projekterne spænder over byggeri, medicinalindustrien, '
       'jernbaner, datacentre og energi, og de to første kender jeg bedst: '
       'byggeri fra udførelsen og medicinal fra commissioning. At arbejde '
       'på tværs af landegrænser, som projekterne i Finland, ser jeg som en '
       'mulighed frem for en hindring.', after=44)

    lp('Struktureret og ansvarlig er sådan, jeg arbejder, og nysgerrighed '
       'på nye løsninger er drivkraften bag, at jeg stadig udvikler mig '
       'fagligt, senest med AI som værktøj i analyse og dokumentation. Det, '
       'I skriver om at planlægge og designe fremtidens bæredygtige samfund '
       'og byer, og om at fremme den grønne omstilling, øge potentialet fra '
       'digitalisering og styrke vores samfund, er en ramme, jeg gerne vil '
       'arbejde ind i. Varierede opgaver er en del af tiltrækningen, og det '
       'samme er udsigten til faglig sparring i et hus på tværs af fag. '
       'På dansk kommunikerer jeg professionelt, både skriftligt og mundtligt, '
       'og engelsk bruger jeg dagligt. Roskilde er en overkommelig tur fra '
       'Måløv. I holder samtaler løbende, og jeg kan være med fra start. Jeg '
       'ser frem til at høre fra jer.', after=44)

    m.para('Med venlig hilsen', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Maskinmester med elautorisation og 20+ år i tekniske '
           'installationer: el, VVS og ventilation, commissioning af '
           'kritiske anlæg og drift af forsyningsanlæg. Vant til '
           'tværfagligt samarbejde og til at følge løsninger fra tegning '
           'til drift.', after=32)
    m.para('Projektering, kvalitetssikring og faglig sparring har været en '
           'del af jobbet i alle årene, og jeg tager ansvar for mine '
           'opgaver fra de første idéer til opfølgning under udførelsen. Jeg '
           'trives i det tværfaglige rum, hvor løsningen bliver bedre af '
           'flere fag.', after=32)

    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester (el-teknik og ventilation)',
         'Data Power Consultant ApS · København · 2024 – nu (fra nov. 2026 også ELOHVACs '
         'el-tekniske aktiviteter)',
         'AI-afdeling 4-10 personer · el-service og entreprise · 5 elektrikere + 3 lærlinge',
         [('El-service og entreprise',
           'Tavler, styring og installationer projekteret og udført for '
           'erhvervskunder, med rådgivning om løsningerne og fuldt '
           'ansvar for økonomien.'),
          ('AI og analyse',
           'AI-afdelingen bygger både softwareprodukter og AI-værktøjer, '
           'som hjælper i analyse og dokumentation.')]),
        ('Drifts- og serviceleder · elautoriseret maskinmester',
         'ELOHVAC · Ballerup · maj 2023 – nov. 2026 (virksomheden lukket)',
         '5 elektrikere og 3 lærlinge · service, installation og projekter',
         [('Installation og sparring',
           'El, VVS og ventilation projekteret og udført i tæt dialog med '
           'kunderne. Løsningsvalg drøftet på stedet, KS ført, og '
           'installationerne fulgt til drift.'),
          ('Oplæring',
           'Nye medarbejdere og lærlinge oplært i løbet, og fagligheden '
           'delt på tværs i teamet.'),
          ('Aftaler og økonomi',
           'Tilbud gennemgået med kunderne, før de blev givet, og '
           'serviceaftaler med opfølgning på tid, kvalitet og økonomi.')]),
        ('Commissioning Manager',
         'Novo Nordisk · Hillerød · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, 2-10 mio. kr. · 25 specialister · GMP, IQ/OQ/PQ',
         [('Commissioning og kvalitet',
           'Kritiske anlæg idriftsat i medicinalindustrien med '
           'dokumentation, IQ/OQ/PQ og frigivelse. Tværfagligt samarbejde '
           'med 25 specialister og underentreprenører; aftalte datoer '
           'holdt.'),
          ('Aflevering',
           'Papirerne fulgte leverancen: dokumentation og frigivelse, der '
           'kunne bruges, og 37 projekter afleveret uden løse ender.')]),
        ('Overmontør og entrepriseleder',
         'Ventek · Taastrup · jan. 2022 – nov. 2022',
         '11 projekter · 14 mand og underentreprenører',
         [('Udførelse og tilsyn',
           'Opfølgning under udførelsen på byggepladser med 14 mand og '
           'underentreprenører. Grænseflader mellem fagene koordineret på '
           'pladsen, så arbejdet ikke stødte sammen.'),
          ('Planlægning',
           'Mandskab, materiel og tid planlagt for 14 mand, så arbejdet '
           'kunne køre parallelt på flere adresser.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · kritiske anlæg · 10 medarbejdere · skiftehold',
         [('Driftens side af projekterne',
           'HVAC, pumper, procesrør, el, SCADA og PLC holdt kørende '
           'døgnet rundt. Erfaringen med, hvordan installationer faktisk '
           'opfører sig efter idriftsættelsen, sidder i hænderne; '
           'vedligehold planlagt på fejldata.'),
          ('Struktur i driften',
           'Forebyggende vedligehold styret af fejldata, så reservedelene '
           'var der, når noget gik i stykker.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('Design og produktion',
           'Maskinteknisk design og produktion fra tegning til færdigt '
           'emne i værkstedet med 12 mekanikere, og oplæring af nye '
           'medarbejdere.')]),
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

    m.section('KOMPETENCER')
    m.bullet('Projektering og design', 'El, VVS og ventilation; AutoCAD og '
             'maskinteknisk design. Løsninger tegnet med drift og '
             'udførelse for øje.', after=10)
    m.bullet('Koordinering og grænseflader', 'Tværfagligt samarbejde med '
             'specialister, underentreprenører og kunder. Grænseflader '
             'afstemt, før de bliver dyre.', after=10)
    m.bullet('Kvalitet og dokumentation', 'KS, IQ/OQ/PQ og frigivelse fra '
             '37 commissioning-projekter. Dokumentation, der kan bruges.',
             after=10)
    m.bullet('Fagtilsyn og sparring', 'Opfølgning under udførelsen på '
             'byggeplads og i drift, og faglig sparring om løsningsvalg '
             'med kolleger og kunder.', after=10)

    m.section('FØRSTE 90 DAGE')
    m.para('Planen følger projektet: idéer, grænseflader, udførelse.',
           after=8)
    m.bullet('Måned 1 · idéerne', 'Løbende projekter og teamet lært at '
             'kende, jeres projekteringspraksis forstået, og kundens '
             'behov oversat til konkrete valg.', after=10)
    m.bullet('Måned 2 · grænsefladerne', 'Koordinering mellem fagene sat i '
             'system på egne projekter, og de kritiske mødepunkter mellem '
             'el, VVS, ventilation og styring kortlagt.', after=10)
    m.bullet('Måned 3 · udførelsen', 'Fagtilsyn og opfølgning under '
             'udførelsen i gang, kvalitetssikring ført, og faglig sparring '
             'som fast rutine.', after=10)

    m.section('SPROG OG PRAKTISK')
    m.para('Dansk (modersmål) · engelsk (professionelt) · persisk '
           '(modersmål). AutoCAD, SAP, Excel, CMMS; PRINCE2. Kørekort '
           'kategori B (manuelt gear). Bosat i Måløv; Roskilde er en '
           'overkommelig tur derfra.', after=8)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Krav og dokumentation · Maskinmester, Sweco, Roskilde',
                   ('Krav i opslaget', 'Dokumentation'),
                   [
        ('Uddannet maskinmester',
         'Maskinmester med elautorisation LV/MV/HV (Sikkerhedsstyrelsen, maj '
         '2023), B.Tech (EQF6) i teknologiledelse og maskinteknik '
         '(2017-2022) og el- og maskinteknisk design (2000-2003).'),
        ('Mindst to års erfaring, gerne fra rådgiverbranchen eller en '
         'beslægtet teknisk rolle',
         'Mere end 20 år i tekniske roller: service og entreprise (ELOHVAC '
         '2023-2026), commissioning (Novo 2022-2024), byggeplads (Ventek '
         '2022), døgndrift (Biofos 2017-2022). Rådgiverbranchen som sådan '
         'har jeg ikke været i; den beslægtede tekniske rolle har jeg.'),
        ('Erfaring med tekniske installationer, projektering eller rådgivning',
         'Tekniske installationer i 20+ år: elinstallationer LV/MV/HV, VVS '
         'og ventilation. Projektering fra designsiden (AutoCAD, '
         'maskinteknisk design) og fra udførelsen, hvor løsningen skal '
         'holde. Rådgivning som daglig del af service og tilbud.'),
        ('Trives med at samarbejde med kolleger fra andre fag',
         'Tværfaglige teams er normen: 25 specialister på tværs af fag '
         '(Novo 2022-2024), el, VVS og ventilation i samme entreprise '
         '(ELOHVAC 2023-2026), og montage med underentreprenører (Ventek '
         '2022).'),
        ('Arbejder struktureret og tager ansvar for dine opgaver',
         'PRINCE2-certificeret struktur og ansvar for hele forløb: 37 '
         'leverancer fulgt fra plan til frigivelse (Novo 2022-2024), eget '
         'firma med kunder og økonomi (Data Power 2024-nu).'),
        ('Nysgerrig på nye løsninger og har lyst til at udvikle dig fagligt',
         'AI og analyse som nye værktøjer i arbejdet (Data Power 2024-nu), '
         'AMU-kursus i køleteknik ved siden af fuldtidsarbejde (2021), og '
         'løbende efteruddannelse gennem hele karrieren.'),
        ('Kommunikere professionelt på dansk, både skriftligt og mundtligt',
         'Siden 2017 har dansk været mit daglige arbejdssprog: kundedialog, '
         'tilbudsgivning, dokumentation og rapportering på dansk. Engelsk '
         'brugt parallelt i internationale projekter.'),
        ('Rådgivning om og projektering af tekniske installationer og anlæg',
         'Løsningsvalg rådgivet i dialog med kunder (ELOHVAC 2023-2026), og '
         'installationer projekteret fra tegnebord (AutoCAD, 2000-2003) til '
         'idriftsættelse (Novo 2022-2024).'),
        ('Koordinering af grænseflader mellem de tekniske fag',
         'Grænseflader mellem el, VVS, ventilation og styring koordineret '
         'på byggepladser (Ventek 2022) og i commissioning, hvor kritiske '
         'systemer mødes (Novo 2022-2024).'),
        ('Fagtilsyn og opfølgning under udførelsen',
         'Tilsyn og opfølgning fra entreprenørsiden: 14 mand og '
         'underentreprenører fulgt på pladsen (Ventek 2022), og '
         'idriftsættelse fulgt tæt på anlæggene (Novo 2022-2024).'),
        ('Udvikling, optimering og kvalitetssikring af tekniske løsninger',
         'Optimering af HVAC, pumper og procesanlæg i driften (Biofos '
         '2017-2022), kvalitetssikring via KS og IQ/OQ/PQ (Novo 2022-2024), '
         'og udvikling af løsninger i tæt dialog med kunder (ELOHVAC '
         '2023-2026).'),
        ('Faglig sparring med kolleger og kunder om valg af tekniske '
         'løsninger',
         'Sparring om løsningsvalg hver dag i servicebranchen (ELOHVAC '
         '2023-2026) og på tværs af 25 specialister i commissioning (Novo '
         '2022-2024).'),
        ('Mulighed for at påtage dig fagledelse',
         'Ledelseserfaring siden 2003: 12 mekanikere (ARJ 2003-2010), 10 på '
         'skiftehold (Biofos 2017-2022), 5 elektrikere og 3 lærlinge '
         '(ELOHVAC 2023-2026). Fagledelse er en rolle, jeg kan træde ind i '
         'med det samme.'),
        ('Følge projekterne fra de første idéer til opfølgning under '
         'udførelsen',
         'Hele forløbet som fast rutine: fra idé og tilbud (ELOHVAC '
         '2023-2026) over projektering og planlægning (Ventek 2022, PRINCE2) '
         'til idriftsættelse og opfølgning (Novo 2022-2024). Forløbet er '
         'gentaget 37 gange i medicinalindustrien og 11 gange på '
         'byggeplads.'),
        ('Projekter inden for byggeri, medicinalindustrien, jernbaner, '
         'datacentre og energi',
         'Byggeri fra udførelsen (Ventek 2022), medicinalindustri fra '
         'commissioning (Novo 2022-2024, GMP) og energi/forsyning fra '
         'driften (Biofos 2017-2022). Jernbaner og datacentre er nye '
         'projekttyper, jeg kan bidrage til fra udførelsessiden; '
         'datacenterkendskab har jeg fra commissioning og drift af '
         'kritiske anlæg.'),
        ('Tværfagligt team',
         'Tværfagligt arbejde er udgangspunktet i alle roller: el, VVS og '
         'ventilation (ELOHVAC), commissioning på tværs af fag (Novo), '
         'montage med flere fag på samme adresse (Ventek).'),
        ('Arbejde på tværs af landegrænser (Finland; tidligere Italien og '
         'USA)',
         'International erfaring med kunder og projekter på tværs af '
         'landegrænser (Novo 2022-2024, Data Power 2024-nu) og trivsel ved '
         'at arbejde på engelsk. Finland er en mulighed, jeg tager gerne.'),
        ('Roskilde som arbejdssted',
         'Bosat i Måløv; Roskilde er en overkommelig tur væk, og '
         'kørsel mellem arbejdssteder har været en fast del af min hverdag i '
         'mere end 20 år. Kørekort kategori B (manuelt gear) er i orden.'),
                   ],
                   widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo · Ansøgning og CV · Maskinmester, '
                       'Sweco')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Sweco_Maskinmester.docx')
    build(out)
    print(out)
