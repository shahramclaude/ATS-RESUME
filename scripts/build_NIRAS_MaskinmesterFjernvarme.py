#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Erfaren Maskiningeniør/Maskinmester til fjernvarmeprojekter — NIRAS, Allerød.
Dansk opslag -> DANSK dokument (4 s.), standard masterdesign (brev 1, CV 2-3,
kravmatrix 4). TEMPLATE Gentofte-2027.

NIRAS: Energy, Utility & Green Transition (energiforsyning; rådgiver varme-
og energiselskaber). Rollen: fagligt ledende medarbejder inden for
maskinteknisk rådgivning ifm. energicentraler knyttet til
fjernvarmetransmissionssystemer; analyser -> beslutningsgrundlag, deep dive
studier af komponentvalg, tilstandsvurdering on site, komponentudskiftninger,
support ved sikkerhedsnedlukninger, systematisk vedligeholdelsesplanlægning,
leverandørdialog, teknisk sparring med kundernes driftsfolk. Tæt samarbejde
med el- og SRO-teknisk område. Base: hovedkontoret i Allerød. Kontakt:
afdelingschef Jesper Graa Andreasen (60 34 09 80) -> 'Kære Jesper Graa
Andreasen,'. Vurdering LØBENDE (asap). Ingen fast frist.

KIT-BÆRENDE: Maskinmester (IKKE maskiningeniør — 'eller' i opslaget)
SELVSIKKERT. 10+ års erfaring = 20+ år SELVSIKKERT. Fagområder (JD kræver
KUN 'én eller flere'): pumper, ventiler, kedler, elmotorer, frekvensomformere,
røranlæg, målere/transmittere (SRO) = dækket; varmevekslere, trykholdesystemer,
varmepumper = IKKE claimed (ærligt i matrix). FJORNVARME/KRAFTVÆRK/RÅDGIVER-
erfaring = 'en fordel, men ikke et krav' -> ærlig hedge i P3 + matrix. SRO
SELVSIKKERT (Biofos). Flydende dansk SELVSIKKERT. Allerød = commute_ok med
FLAG (ca. halvvejs mellem Roskilde- og Næstved-præcedenserne; kortere end
Næstved).

STIL (3/3 mod #453 HOFOR): register "Dybe dyk, klare valg", åbning CC
(valget der rækker frem i tiden), struktur "Analyse, tilstand, beslutning".
Matrix-rækker >= antal krav (24 krav -> 25 rækker, lærdom fra HOFOR). Alle
rækker >= 110 tegn. Ingen em dash. 'dygtig'/'dygtiggøre'/'brænder'/
'dynamisk'/'passioneret'/'gøre en forskel'/'demonstreret'/'elinstallatør'
bruges ikke.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_Gentofte_DriftslederEjendomme_2027.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'NIRAS · Maskinmester · Fjernvarmeprojekter'
BANNER_RESUME = 'MASKINTEKNIK · ANALYSER · DRIFT OG VEDLIGEHOLD'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('2. december 2026')
    m.meta('NIRAS · Energy, Utility & Green Transition · Allerød')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning som erfaren maskinmester til fjernvarmeprojekter',
           bold=True, color='1A1A1A')
    m.para('Kære Jesper Graa Andreasen,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('Et komponentvalg på en energicentral er en beslutning om de næste '
       'mange år: pumpen, ventilen eller kedlen, der vælges i dag, skal '
       'holde, til nogen igen tager fat om den. I stillingen som erfaren '
       'maskinmester ligger netop de valg i maskinteknisk rådgivning om '
       'energicentraler knyttet til fjernvarmetransmissionssystemer, hvor '
       'forsyningssikkerhed for kritisk forsyningsinfrastruktur er det, '
       'kunderne skal holde styr på. Jeg '
       'søger jobbet, fordi analyser, deep dive studier af komponentvalg og '
       'tilstandsvurdering på stedet er den måde, min driftserfaring kan '
       'blive til beslutningsgrundlag, andre kan handle på. Tyve år med '
       'pumper, ventiler, kedler og røranlæg har lært mig, hvordan '
       'komponenter faktisk opfører sig i drift; nu skal den viden bruges '
       'i rådgivningen. Om jeres miljø står der, at vi løfter hinanden, '
       'deler viden og har korte veje fra idé til handling, og det er '
       'netop sådan, de bedste tekniske valg bliver truffet.')

    lp('Maskinteknikken har jeg mødt på anlæg, der kørte hver dag. Nu er '
       'jeg elautoriseret maskinmester og CTO for AI-afdelingen hos Data '
       'Power med ansvar for el-teknik og ventilation og 5 elektrikere '
       'med 3 lærlinge. På '
       'Biofos holdt jeg pumper, procesrør og kedler kørende i døgndrift, '
       'og SRO-anlægget med målere og transmittere var mit daglige '
       'arbejdsredskab; ventiler og sikkerhedsudstyr har jeg arbejdet med '
       'i årene med VVS og ventilation, og elmotorer og frekvensomformere '
       'hører til el-autoriseringens håndværk. Maskintekniske analyser har '
       'fulgt driftsarbejdet: fejldata, MTBF og MTTR, og i dag '
       'AI-værktøjer, der gør et beslutningsgrundlag konkret frem for et '
       'gæt. Systematiske løsninger til vedligeholdelsesplanlægning har jeg '
       'bygget op i CMMS, planlægning af komponentudskiftninger har været '
       'en del af hverdagen, og teknisk support ved sikkerhedsnedlukninger '
       'kender jeg fra 24/7-driften. Samarbejde og dialog med leverandører '
       'og servicepartnere og teknisk sparring med kundernes driftsfolk har '
       'været omdrejningspunktet som serviceleder; on-site assistance og '
       'arbejde på kontoret er den blanding, jeg har levet i hele tiden. '
       'Rollen er fagligt ledende, og på tværs af fag har jeg taget '
       'ansvar siden 2003.')

    lp("NIRAS' Energy, Utility & Green Transition rådgiver varme- og "
       'energiselskaber, og med en stor og voksende portefølje af projekter '
       'er der brug for flere hænder til drift- og vedligeholdelses-'
       'rådgivningen på energicentraler og kraftværker. At indgå i et '
       'erfarent, tværfagligt hold med høj faglighed og kolleger inden for '
       'det el- og SRO-tekniske område, i et velfungerende fagligt '
       'fællesskab på kontoret i Allerød, er en ramme med korte '
       'beslutninger. Om værdierne står der: vi lytter, vi lærer, vi '
       'leverer. Der er tale om en uformel kultur med stor grad af frihed og '
       'fleksibilitet og mulighed for at sætte dit eget præg; den passer '
       'til en erfaren medarbejder, der har arbejdet selvstændigt med '
       'maskintekniske opgaver længe. En varieret hverdag mellem kontor og '
       'anlæg er en del af tiltrækningen. Rådgivererfaring har '
       'jeg ikke fra tegnestuesiden, og fjernvarme og kraftværk har jeg '
       'mødt fra drifts- og VVS-siden snarere end fra brancherne; de tre '
       'punkter er nævnt som fordele og ikke krav, og til gengæld har jeg '
       'siddet på den side af bordet, hvor rådgivningen skal virke i '
       'drift.')

    lp('Målrettet og struktureret går jeg til opgaverne, og flydende dansk '
       'i skrift og tale er på plads som modersmål; tekniske manualer '
       'læser jeg også på engelsk. Rollen kræver selvstændigt arbejde med '
       'maskintekniske opgaver, og det har været min hverdag længe, både '
       'med kundernes drifts- og vedligeholdelsesfolk i marken og med '
       'papirerne på kontoret. Basen i Allerød er til at nå fra Måløv, og '
       'kundernes anlæg ligger spredt, som on-site-arbejde nu en gang gør. '
       'Da I vurderer henvendelser løbende, håber jeg at høre fra jer '
       'snart.', after=44)

    m.para('Med venlig hilsen', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Maskinmester med elautorisation og 20+ år med maskinteknik på '
           'anlæg, der skal køre hver dag: pumper, ventiler, kedler, '
           'elmotorer og røranlæg. Analyser, tilstandsvurdering og '
           'vedligeholdelsesplanlægning har været en del af jobbet i alle '
           'årene. Jeg trives, når analysen kan følges helt ud til '
           'komponenten.', after=32)
    m.para('Trives tæt på kundernes driftsfolk og vedligeholdelsesfolk, '
           'både på stedet og ved skrivebordet. Ansvar på tværs af fag har '
           'jeg taget, og struktureret aflevering er den måde, opgaverne '
           'bliver gjort færdige på.', after=32)

    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester (el-teknik og ventilation)',
         'Data Power Consultant ApS · København · 2024 – nu (fra nov. 2026 også ELOHVACs '
         'el-tekniske aktiviteter)',
         'AI-afdeling 4-10 personer · el-service og entreprise · 5 elektrikere + 3 lærlinge',
         [('El og styring',
           'Tavler, elmotorer og røranlæg serviceret hos erhvervskunder, '
           'og udskiftninger vurderet og planlagt fra sag til sag.'),
          ('Analyse',
           'AI-værktøjer og MTBF/MTTR fra driftsårene brugt til at gøre '
           'beslutningsgrundlag konkrete.')]),
        ('Drifts- og serviceleder · elautoriseret maskinmester',
         'ELOHVAC · Ballerup · maj 2023 – nov. 2026 (virksomheden lukket)',
         '5 elektrikere og 3 lærlinge · service, installation og projekter',
         [('Komponenter og tilstand',
           'El, VVS og ventilation serviceret: pumper, ventiler, elmotorer '
           'og røranlæg repareret og udskiftet, og tilstanden vurderet ude '
           'hos kundernes anlæg.'),
          ('Sparring og leverandører',
           'Teknisk sparring med kundernes driftsfolk om løsningsvalg, og '
           'leverandører og servicepartnere koordineret på opgaverne.')]),
        ('Commissioning Manager',
         'Novo Nordisk · Hillerød · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, 2-10 mio. kr. · 25 specialister · GMP, IQ/OQ/PQ',
         [('Analyser og valg',
           'Maskintekniske analyser under commissioning, og '
           'beslutningsgrundlag til valg af komponenter før '
           'idriftsættelse.'),
          ('Kvalitet',
           'Dokumentation, IQ/OQ/PQ og frigivelse fulgt for 37 '
           'leverancer, uden løse ender.')]),
        ('Overmontør og entrepriseleder',
         'Ventek · Taastrup · jan. 2022 – nov. 2022',
         '11 projekter · 14 mand og underentreprenører',
         [('Udskiftninger',
           'Komponentudskiftninger planlagt og fulgt på byggeplads, med '
           'tilstandsvurdering af det, der skulle monteres.'),
          ('Planlægning',
           'Mandskab, materiel og tid planlagt for 14 mand, så flere hold '
           'kunne arbejde parallelt.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · kritiske anlæg · 10 medarbejdere · skiftehold',
         [('Drift og SRO',
           'Pumper, kedler, procesrør og ventiler holdt kørende døgnet '
           'rundt, og SRO-anlæg med målere og transmittere betjent.'),
          ('Vedligeholdelsesplanlægning',
           'Forebyggende vedligehold bygget op på fejldata i CMMS, og '
           'reservedelsstyring, så udskiftninger kunne planlægges.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('Produktion',
           'Komponenter produceret efter tegning, elmotorer og pumper '
           'samlet, og fejlfinding løst i værkstedet.'),
          ('Oplæring',
           'Nye medarbejdere oplært i værkstedet, og arbejdet fordelt '
           'for 12 mand.')]),
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

    m.section('FAGLIGT FUNDAMENT')
    m.bullet('Komponenter', 'Pumper, ventiler, kedler, elmotorer, '
             'frekvensomformere og røranlæg: funktion, fejl og udskiftning '
             'kendt fra driften.', after=10)
    m.bullet('Analyser og beslutningsgrundlag', 'Fejldata, MTBF/MTTR, OEE '
             'og AI-værktøjer brugt til at gøre valg konkrete og '
             'dokumenterbare, også når svaret blev, at et komponent skulle '
             'skiftes.', after=10)
    m.bullet('Vedligeholdelsesplanlægning', 'Systematiske løsninger i CMMS, '
             'forebyggende vedligehold på fejldata og planlagte '
             'komponentudskiftninger.', after=10)
    m.bullet('Sparring', 'Teknisk dialog med driftsfolk og '
             'vedligeholdelsesfolk på stedet, og samarbejde med '
             'leverandører og servicepartnere.', after=10)

    m.section('FØRSTE 90 DAGE · ANALYSE, TILSTAND, BESLUTNING')
    m.bullet('Måned 1 · analysen', 'Porteføljen af energicentraler lært at '
             'kende, kollegerne inden for maskinteknik, el og SRO mødt, og '
             'de første maskintekniske analyser taget fat på.', after=10)
    m.bullet('Måned 2 · tilstanden', 'Tilstandsvurdering on site hos '
             'kundernes anlæg, deep dive studier af komponentvalg i gang, '
             'og teknisk sparring med driftsfolkene etableret.', after=10)
    m.bullet('Måned 3 · beslutningen', 'Beslutningsgrundlag afleveret, '
             'planlægning af komponentudskiftninger sat i system, og de '
             'første systematiske løsninger til vedligeholdelsesplanlægning '
             'under opbygning.', after=10)

    m.section('SPROG OG PRAKTISK')
    m.para('Dansk (modersmål, flydende i skrift og tale) · engelsk '
           '(professionelt, tekniske manualer). SAP, CMMS, Excel, '
           'AI-værktøjer; PRINCE2. Kørekort kategori B (manuelt gear). '
           'Bosat i Måløv; base i Allerød og on-site hos kundernes anlæg '
           'er en kombination, der passer mig.', after=8)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Krav og dokumentation · Erfaren Maskiningeniør/Maskinmester, NIRAS',
                   ('Krav i opslaget', 'Dokumentation'),
                   [
        ('Maskiningeniør eller Maskinmester',
         'Maskinmester med elautorisation LV/MV/HV (Sikkerhedsstyrelsen, maj '
         '2023), B.Tech (EQF6) i teknologiledelse og maskinteknik '
         '(2017-2022) og el- og maskinteknisk design (2000-2003).'),
        ('Stærk faglig viden',
         'Fagligheden bygget op over 20+ år: produktion (ARJ 2003-2010), '
         'drift af kritiske anlæg (Biofos 2017-2022), commissioning (Novo '
         '2022-2024) og serviceledelse (ELOHVAC 2023-2026).'),
        ('Systemforståelse',
         'Systemer der skal spille sammen: pumper, styring og røranlæg i '
         'sammenhæng, fra produktion over transmission til afgivelse, '
         'bedømt på døgndrift (Biofos 2017-2022) og commissioning af '
         'kritiske anlæg (Novo 2022-2024).'),
        ('Pumper, ventiler, varmevekslere, trykholdesystemer, kedler, '
         'elmotorer, frekvensomformere, målere, transmittere, varmepumper '
         'og/eller røranlæg',
         'Pumper, ventiler, kedler, elmotorer, frekvensomformere og '
         'røranlæg er driftet, repareret og udskiftet (Biofos 2017-2022, '
         'ELOHVAC 2023-2026); målere og transmittere fra SRO-anlægget '
         '(Biofos). Varmevekslere, trykholdesystemer og varmepumper er ikke '
         'mine kerneområder; her er jeg nærmest på VVS- og køleteknikken.'),
        ('Maskintekniske analyser',
         'Analyser af fejldata, MTBF og MTTR som grundlag for '
         'vedligehold (Biofos 2017-2022), analyse af anlægsdrift med '
         'AI-værktøjer (Data Power 2024-nu) og tekniske analyser under '
         'commissioning (Novo 2022-2024).'),
        ('Beslutningsgrundlag',
         'Beslutningsgrundlag leveret til valg af komponenter og løsninger: '
         'commissioning (Novo 2022-2024), tilbud og løsningsvalg (ELOHVAC '
         '2023-2026) og driftsrapporter på fejldata (Biofos 2017-2022).'),
        ('Deep dive studier af komponentvalg',
         'Dybe gennemgange af komponenter og reservedele har været en del '
         'af driftsarbejdet: reservedelsstyring og valg af komponenter på '
         'fejldata og levetid (Biofos 2017-2022), og udskiftninger vurderet '
         'fra sag til sag (ELOHVAC 2023-2026).'),
        ('Tilstandsvurdering af komponenter on site',
         'Tilstand vurderet ude hos anlæggene hver uge: fejlfinding på '
         'pumper, ventiler og røranlæg på stedet (Biofos 2017-2022, ELOHVAC '
         '2023-2026), og kvalitetsvurdering af komponenter ved montage '
         '(Ventek 2022).'),
        ('Planlægning af komponentudskiftninger',
         'Udskiftninger planlagt, så driften ikke stod stille: '
         'reservedelsstyring og forebyggende udskiftninger (Biofos 2017-2022) '
         'og planlagte udskiftninger på entrepriser (Ventek 2022).'),
        ('Teknisk support ved sikkerhedsnedlukninger',
         'Kritiske anlæg i døgndrift med akutte situationer (Biofos '
         '2017-2022) og vagtordning i servicebranchen (ELOHVAC 2023-2026): '
         'teknisk support, når noget skulle lukkes ned sikkert, er ikke '
         'fremmed.'),
        ('Systematiske løsninger til vedligeholdelsesplanlægning',
         'Forebyggende vedligehold bygget op på fejldata i CMMS (Biofos '
         '2017-2022), og serviceaftaler med faste planer og opfølgning '
         '(ELOHVAC 2023-2026).'),
        ('Samarbejde og dialog med leverandører og servicepartnere',
         'Leverandører, underentreprenører og servicepartnere koordineret i '
         'alle roller: entrepriser (Ventek 2022), serviceaftaler (ELOHVAC '
         '2023-2026) og reservedelsaftaler (Biofos 2017-2022).'),
        ('Teknisk sparring med kundernes driftsfolk',
         'Sparring med driftsfolk har været en del af jobbet hver dag '
         '(ELOHVAC 2023-2026, Ventek 2022), og svarene har skullet kunne '
         'bruges på stedet.'),
        ('Fagligt ledende medarbejder',
         'Ledelse og fagligt ansvar siden 2003: 12 mekanikere (ARJ 2003-2010), '
         '10 medarbejdere på skiftehold (Biofos 2017-2022) og 5 elektrikere '
         'med 3 lærlinge (ELOHVAC 2023-2026).'),
        ('Maskinteknisk rådgivning',
         'Rådgivning om tekniske løsninger i praksis: løsningsvalg drøftet '
         'med kunderne (ELOHVAC 2023-2026), og anbefalinger om komponenter '
         'og vedligehold givet på baggrund af driftsdata (Biofos 2017-2022).'),
        ('El- og SRO-teknisk område',
         'Elautorisation LV/MV/HV (2023) og dagligt arbejde med '
         'SRO-/SCADA-anlæg, PLC, målere og transmittere (Biofos 2017-2022). '
         'El- og SRO-kolleger er dem, jeg har arbejdet tættest med.'),
        ('Flydende dansk i skrift og tale',
         'Dansk som modersmål, og professionelt dansk i kundedialog, '
         'dokumentation og rapportering siden 2017. Engelsk brugt til '
         'tekniske manualer.'),
        ('Arbejde tæt sammen med kundens drifts- og vedligeholdelsesfolk',
         'Kundernes folk har været mine nærmeste samarbejdspartnere: '
         'serviceleder med faste kontaktpunkter (ELOHVAC 2023-2026) og '
         'driftssamarbejde på anlæggene (Biofos 2017-2022).'),
        ('On-site assistance og arbejde på kontoret',
         'Kombinationen er min hverdag: on-site hos kunder og på '
         'byggepladser (Ventek 2022, ELOHVAC 2023-2026) og kontorarbejde '
         'med analyse, planlægning og dokumentation (Biofos 2017-2022, Data '
         'Power 2024-nu).'),
        ('Selvstændigt med maskintekniske opgaver',
         'Selvstændighed er afprøvet i alle led: eget firma (Data Power '
         '2024-nu), driftsansvar for anlæg (Biofos 2017-2022) og '
         'serviceledelse med egne beslutninger (ELOHVAC 2023-2026).'),
        ('Fagligt ansvar på tværs af fag',
         'Tværfagligt ansvar i praksis: commissioning på tværs af 25 '
         'specialister (Novo 2022-2024), el, VVS og ventilation i samme '
         'regi (ELOHVAC 2023-2026) og montage med flere fag (Ventek 2022).'),
        ('Målrettet og struktureret',
         'PRINCE2 som ramme, faste rutiner for planlægning og '
         'dokumentation, og opgaver ført til ende: 37 leverancer (Novo '
         '2022-2024) og 11 entrepriser (Ventek 2022).'),
        ('Mere end 10 års relevant erhvervserfaring',
         'Mere end 20 år i maskintekniske roller (ARJ 2003-2010, Biofos '
         '2017-2022, Ventek 2022, Novo 2022-2024, ELOHVAC 2023-2026), '
         'heraf de seneste tre år som maskinmester med elautorisation.'),
        ('Rådgivererfaring, fjernvarmebranchen og/eller kraftværksbranchen '
         '(en fordel, men ikke et krav)',
         'De tre punkter har jeg ikke: rådgivererfaring er fra kundens side '
         'af bordet, fjernvarme og kraftværk kender jeg fra drifts- og '
         'VVS-siden. Til gengæld har jeg 20+ år med de anlæg, '
         'rådgivningen skal holde i live, og den erfaring er tungere end '
         'branchekendskab på papiret.'),
        ('Base i Allerød og arbejde hos kunderne',
         'Bosat i Måløv; turen til Allerød er overskuelig, og arbejde på '
         'skiftende adresser hos kunder har været en del af min hverdag i '
         'mere end 20 år. Kørekort kategori B (manuelt gear) er i orden.'),
                   ],
                   widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo · Ansøgning og CV · Maskinmester, '
                       'NIRAS, fjernvarmeprojekter')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_NIRAS_MaskinmesterFjernvarme.docx')
    build(out)
    print(out)
