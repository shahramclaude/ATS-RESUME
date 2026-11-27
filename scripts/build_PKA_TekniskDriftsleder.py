# -*- coding: utf-8 -*-
"""Teknisk driftsleder — PKA Ejendomme, Storkøbenhavn (dansk opslag -> DANSK dokument).

4 sider i masterdesign: brev side 1, CV side 2-3, kravmatrix side 4.
Kontaktperson: Driftschef Kim Gustav Hansen, 21 61 04 27 -> "Kære Kim Gustav
Hansen,". Løbende samtaler (lukkes når rette kandidat er fundet); start hurtigst
muligt; løn efter overenskomst med ESL.

SAMME-FIRMA-REGLER: PKA Ejendomme er genansøgning (tidligere Driftschef) ->
intet genbruges; alt indhold skrevet friskt.

STILVALG (style_guard godkendt, 3/3 skift mod #441 Gentofte):
  register    = Teknik i øjenhøjde
  åbningsgreb = BR (den usynlige drift: installationerne fungerer bedst, når
                ingen lægger mærke til dem)
  struktur    = Drift, forbedring, dialog (30/60/90 = driften · forbedringen ·
                dialogen)

BRUGERSVAR 26.11 (bindende):
1. Lokation = commute_ok ("Storkøbenhavn er fint, ~25-35 min fra Måløv") ->
   bekræft konkret i brevet.
2. CTS/BMS og KNX = REEL erfaring ("CTS/BMS og KNX har jeg arbejdet med") ->
   skriv SELVSIKKERT hele vejen (ingen hedge på CTS/BMS/KNX).

MASTER-REGLER: "elautoriseret maskinmester (LV/MV/HV)" — aldrig "autoriseret
elinstallatør"; "el-installatør" KUN i JD-citat (rk7-label). Ingen em dash.
BANNED som egne påstande: passioneret, brænder for, gøre en forskel, dynamisk.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_Gentofte_DriftslederEjendomme_2027.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'PKA Ejendomme · Teknisk driftsleder, Storkøbenhavn'
BANNER_RESUME = 'TEKNISK DRIFT · CTS/BMS · BEBOERKONTAKT'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('26. november 2026')
    m.meta('PKA Ejendomme · Storkøbenhavn')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning om stillingen som teknisk driftsleder', bold=True,
           color='1A1A1A')
    m.para('Kære Kim Gustav Hansen,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('En varmecentral, et ventilationsanlæg og et CTS-anlæg fungerer bedst, '
       'når ingen lægger mærke til dem. Den dag en beboer mærker, at der er '
       'noget galt, er driften allerede blevet personlig, og dér starter '
       'opgaven: stabil drift, fejlfinding og optimering, før nogen behøver at '
       'spørge. De tekniske installationer i bolig- og erhvervsejendomme er '
       'rammen om folks hjem og arbejdspladser, og som I selv skriver: '
       'kvalitet betyder noget hos os, både i de tekniske løsninger og i den '
       'måde, vi møder mennesker på.')

    lp('PKA Ejendomme er ejendomsselskab for pensionskasserne bag PKA og '
       'driver og udvikler bolig- og erhvervsejendomme med et langsigtet '
       'perspektiv: stabile afkast til pensionskassernes medlemmer og '
       'velfungerende hjem og arbejdspladser i samme sætning. Rollen som '
       'teknisk driftsleder ligger midt i den balance, med drift af '
       'ejendommene i det storkøbenhavnske område og varme, ventilation og '
       'øvrige tekniske installationer holdt kørende. En hverdag hvor opgaverne '
       'spænder fra fejlfinding på styringssystemer til en samtale med en '
       'beboer, og hvor det hele skal ende i en velfungerende ejendomsdrift.')

    lp('Teknikken er i orden. CTS/BMS, KNX og bygningsautomatik har jeg '
       'arbejdet med i praksis, side om side med SCADA, PLC og el- og '
       'ventilationsanlæg, og tekniske styringssystemer, fejlfinding, '
       'regulering og energioptimering er discipliner, jeg har i hænderne: fra '
       'indregulering af anlæg til fejl der blev fundet ved rodårsagen. Den '
       'relevante tekniske uddannelse er maskinmester med elautorisation '
       'LV/MV/HV, og den praktiske erfaring med teknisk ejendomsdrift strækker '
       'sig fra kritiske anlæg i døgndrift til serviceaftaler på '
       'erhvervsbygninger.')

    lp('De første 90 dage følger opgavens tre sider. Dag 1-30 er driften: '
       'installationerne, CTS/BMS-anlæggene og serviceaftalerne gennemgået, '
       'viceværternes opgaver kortlagt, og arbejdet fra start struktureret med '
       'vedligeholdelse, dokumentation og opfølgning. Dag 31-60 er '
       'forbedringen: forebyggende vedligeholdelse, energioptimering og '
       'forbedring af driftsøkonomien samlet i konkrete tiltag, og '
       'kvalitetssikre serviceaftaler, teknisk dokumentation og eksterne '
       'leverandørers arbejde gennemgået. Dag 61-90 er dialogen: de '
       'driftsrelaterede henvendelser fra beboere og erhvervskunder følges til '
       'dørs, og planlægge og koordinere opgaver for viceværter med teknisk '
       'sparring og følge op på kvaliteten er en fast rytme.')

    lp('Det menneskelige er halvdelen af opgaven. Emotionel intelligens er '
       'ikke et punkt på listen hos PKA, men måden arbejdet gøres på: '
       'oprigtigt nysgerrig på mennesker, lytter aktivt, spørger ind og gør '
       'sig umage med at forstå andres behov og perspektiver, også når de er '
       'anderledes end mine egne. Erfaringen med koordinering eller ledelse af '
       'medarbejdere har jeg fra hold på op til 25 personer, og serviceminded '
       'og kommunikerer professionelt med beboere, erhvervskunder, kolleger og '
       'samarbejdspartnere er tonen i hverdagen. Opgaverne bliver taget '
       'alvorligt: jeg tager ansvar, er løsningsorienteret og følger '
       'opgaverne til dørs.')

    lp('Fællesskabet tiltaler mig: ordentlighed, at dele viden, hjælpe '
       'hinanden og gøre os umage med opgaverne, og en uformel samarbejdsform '
       'hvor man lærer af hinanden og finder gode løsninger sammen. At få lov '
       'til at præge den tekniske udvikling af ejendommene, samtidig med at '
       'driften kører, og de konkrete opgaver som forebyggende vedligeholdelse, '
       'energioptimering og god driftsøkonomi ligger i hverdagen, er præcis '
       'kombinationen jeg søger. Løn i henhold til overenskomst med ESL '
       'passer, og Storkøbenhavn fungerer fint fra Måløv, cirka 25-35 minutter '
       'væk. Tiltrædelse hurtigst muligt er i orden. Jeg ser frem til at høre '
       'fra dig.', after=44)

    m.para('Med venlig hilsen', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Driftsleder med 20+ år i el, ventilation og bygningers '
           'tekniske anlæg. På styresiden har jeg arbejdet med CTS/BMS, KNX og '
           'bygningsautomatik i drift, SCADA og PLC fra kritiske anlæg i døgndrift, '
           'og '
           'fejlfinding, regulering og energioptimering som daglig disciplin. '
           'Hold på op til 25 personer koordineret, beboer- og kundekontakt i '
           'øjenhøjde, og maskinmester med elautorisation LV/MV/HV.', after=32)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester (el-teknik og ventilation)',
         'Data Power Consultant ApS · København · 2024 – nu (fra nov. 2026 også ELOHVACs '
         'el-tekniske aktiviteter)',
         'AI-afdeling 4-10 personer · el-service og entreprise · 5 elektrikere + 3 lærlinge',
         [('El og koordinering', 'El-service og entreprise på bygninger med '
           'fejlfinding, dokumentation og aflevering pr. sag. Teams på 4-10 '
           'specialister koordineret, og opgaver fulgt til dørs, også når '
           'planen ændrede sig undervejs.')]),
        ('Ejer / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 – nov. 2026 (virksomheden lukket)',
         'Erhvervskunder · el, ventilation og klima · entreprise · fuldt P&L · serviceaftaler',
         [('Driftsøkonomi og service', 'Serviceaftaler på bygningers el-, '
           'ventilations- og klimaanlæg med forebyggende vedligeholdelse som '
           'omdrejningspunkt og energioptimering i de eksisterende anlæg. '
           'Driftsøkonomien fulgt måned for måned, og kundedialogen om løsninger '
           'ført i øjenhøjde.')]),
        ('Senior commissioningeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, DKK 2-10 mio. · 25 specialister · GMP/FDA/EMA',
         [('Styringssystemer og kvalitet', 'El-systemer, styring og regulering '
           'på tekniske anlæg taget fra konstruktion over FAT/SAT og IQ/OQ/PQ '
           'til idriftsættelse. Dokumentation der holdt til revision, og '
           'kvalitetssikring af leverandører og tekniske løsninger som en del '
           'af hverdagen.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022 – nov. 2022',
         '11 projekter · 14 mand · underleverandører · montage og aflevering',
         [('Ventilation og koordinering', 'Ventilationsanlæg i bygninger '
           'koordineret fra montage til aflevering: 11 projekter, 14 mand og '
           'underleverandører planlagt uge for uge. Fejlfinding på anlæg før '
           'aflevering, og opgaver fordelt med blik for både kvalitet og tid.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · kritiske anlæg · 10 medarbejdere · skiftehold',
         [('Stabil drift døgnet rundt', 'Pumper, HVAC, procesrør, el, SCADA og '
           'PLC holdt kørende i døgndrift med 10 medarbejdere på skiftehold. '
           'Forebyggende vedligeholdelse planlagt på fejldata, fejlfinding '
           'undervejs, og reservedelsstyring så reparationer ikke ventede.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('Mennesker og fejlfinding', 'Vedligehold og reparation af maskiner '
           'og anlæg med 12 mekanikere og teknikere. Fejlfinding og '
           'rodårsagsarbejde der ændrede måden fejl blev håndteret på, og '
           'opgaver fulgt til dørs hver gang.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('UDDANNELSE OG CERTIFIKATER')
    m.edu('B.Tech (EQF6), teknologiledelse og maskinteknik',
          'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12')
    m.edu('Dansk elautorisation LV/MV/HV som elautoriseret maskinmester', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('El- og maskinteknisk design, elteknik (EQF6)', 'Tehran Technical University · 2000–2003')
    m.edu('PRINCE2, certificeret projektleder', 'AXELOS / PeopleCert')
    m.edu('Køleteknik og klimaanlæg (AMU)', 'Mercantec · 2021 · STCW 2021–2023, Søfartsstyrelsen')

    m.section('KOMPETENCER')
    m.bullet('Teknik og anlæg', 'Paletten dækker CTS/BMS, KNX og bygningsautomatik i drift, '
             'SCADA og PLC, el, varme, ventilation og køl. Fejlfinding, '
             'regulering og indregulering af anlæg, og tekniske løsninger '
             'vurderet på holdbarhed frem for på pris alene.', after=10)
    m.bullet('Drift og økonomi', 'Forebyggende vedligeholdelse planlagt på '
             'fejldata, energioptimering i eksisterende anlæg og '
             'driftsøkonomi fulgt måned for måned. Dokumentation og '
             'opfølgning som en del af driften, ikke som et ekstra lag.',
             after=10)
    m.bullet('Kontakt og service', 'Driftsrelaterede henvendelser fra beboere '
             'og erhvervskunder taget alvorligt og fulgt til dørs. Serviceminded '
             'dialog, professionel kommunikation og løsninger fundet i øjenhøjde.',
             after=10)
    m.bullet('Koordinering', 'Opgaver planlagt og fordelt for medarbejdere og '
             'leverandører siden 2003: skiftehold, montagehold og servicehold. '
             'Teknisk sparring og kvalitetsopfølgning som en fast del af '
             'ledelsen.', after=10)

    m.section('DE FØRSTE 90 DAGE')
    m.para('Planen følger opgaven: driften, forbedringen, dialogen.', after=8)
    m.bullet('Dag 1-30 · Driften', 'Installationerne, CTS/BMS-anlæggene og '
             'serviceaftalerne gennemgået, og viceværternes opgaver kortlagt. '
             'Mål: jeg kender anlæggene og hverdagen, og de første fejl er '
             'løst.', after=10)
    m.bullet('Dag 31-60 · Forbedringen', 'Forebyggende vedligeholdelse, '
             'energioptimering og driftsøkonomi samlet i konkrete tiltag, og '
             'leverandørernes arbejde kvalitetssikret. Mål: en plan for '
             'forbedringerne, ikke en ønskeseddel.', after=10)
    m.bullet('Dag 61-90 · Dialogen', 'Fast rytme for henvendelser, opfølgning '
             'og møder med beboere og erhvervskunder, og opgaverne for '
             'viceværter planlagt i fællesskab. Mål: beboerne ved, hvem de '
             'kontakter, og oplevelsen følger med.', after=10)

    m.section('SPROG, VÆRKTØJER OG PRAKTISK')
    m.para('Dansk (modersmål) · engelsk (professionelt) · persisk (modersmål). '
           'Værktøjskassen: CTS/BMS, KNX, SCADA, PLC, SAP, Excel; PRINCE2. Kørekort kategori B '
           '(manuelt gear). Bosat i Måløv; Storkøbenhavn fungerer fint, cirka '
           '25-35 minutter væk. Tiltrædelse hurtigst muligt.', after=32)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Krav og dokumentation · Teknisk driftsleder, PKA Ejendomme',
                   ('Krav i opslaget', 'Dokumenteret erfaring'),
                   [
        ('Sikre stabil drift, fejlfinding og optimering af CTS/BMS, KNX, '
         'varme, ventilation og øvrige tekniske installationer',
         'Stabil drift af kritiske anlæg døgnet rundt (Biofos 2017-2022): '
         'pumper, HVAC, el, SCADA og PLC. På styresiden er CTS/BMS, KNX og '
         'bygningsautomatik arbejdet med i drift, og varme og ventilation serviceret (ELOHVAC '
         '2023-2026, Ventek 2022), og fejlfinding på styringssystemer som '
         'fast disciplin.'),
        ('Arbejde med forebyggende vedligeholdelse, energioptimering og '
         'forbedring af driftsøkonomien',
         'Forebyggende vedligeholdelse planlagt på fejldata (Biofos 2017-2022), '
         'energioptimering i eksisterende el- og ventilationsanlæg (ELOHVAC '
         '2023-2026), og driftsøkonomi fulgt måned for måned med '
         'omkostningskontrol på hver sag.'),
        ('Håndtere driftsrelaterede henvendelser fra beboere og erhvervskunder '
         'og følge op',
         'Driftsrelaterede henvendelser håndteret i serviceaftaler med '
         'erhvervskunder (ELOHVAC 2023-2026) og i kundedialogen på projekter '
         '(Ventek 2022, Hansen 2025-2026). Følges op hver gang, også når '
         'svaret ikke er det, kunden håbede på.'),
        ('Kvalitetssikre serviceaftaler, teknisk dokumentation og eksterne '
         'leverandørers arbejde',
         'Serviceaftaler udformet og fulgt op (ELOHVAC 2023-2026), teknisk '
         'dokumentation gennem FAT/SAT og IQ/OQ/PQ (Novo 2022-2024), og '
         'eksterne leverandørers arbejde kvalitetssikret på kontrakt og '
         'opfølgning (Hansen 2025-2026).'),
        ('Planlægge og koordinere opgaver for viceværter samt yde teknisk '
         'sparring og følge op på kvaliteten',
         'Opgaver planlagt og koordineret for hold siden 2003: 10 '
         'medarbejdere på skiftehold (Biofos 2017-2022), 14 mand på montage '
         '(Ventek 2022) og 5 elektrikere og 3 lærlinge i marken (ELOHVAC '
         '2023-2026). Sparring og kvalitetsopfølgning som del af '
         'ledelsen, ikke som tillæg.'),
        ('Samarbejde med beboere, erhvervskunder, teknikere, leverandører og '
         'øvrige interessenter om en velfungerende ejendomsdrift',
         'Samarbejde på tværs af interessenter hver dag: kunder, teknikere og '
         'leverandører (ELOHVAC, Hansen), brugere og bygherrer (Novo 2022-2024) '
         'og underleverandører på montage (Ventek 2022). Målet er fælles: en '
         'velfungerende ejendomsdrift.'),
        ('En relevant teknisk uddannelse som eksempelvis elektriker, '
         'automatiktekniker, el-installatør, maskinmester, VVS-tekniker eller '
         'tilsvarende',
         'Maskinmester (2017) med dansk elautorisation LV/MV/HV som '
         'elautoriseret maskinmester (2023), B.Tech i teknologiledelse og '
         'maskinteknik (2017-2022) og el- og maskinteknisk design (2000-2003). '
         'El, automatik og VVS-faglighed dækket fra flere sider.'),
        ('Erfaring med teknisk ejendomsdrift og gerne kendskab til CTS/BMS, '
         'bygningsautomatik og KNX',
         'Den tekniske ejendomsdrift i praksis: bygningers el-, ventilations- og '
         'klimaanlæg i serviceaftaler (ELOHVAC 2023-2026), ventilationsanlæg '
         'i bygninger (Ventek 2022) og kritiske anlæg i drift (Biofos '
         '2017-2022). På styresiden er CTS/BMS, KNX og bygningsautomatik arbejdet med direkte.'),
        ('Forståelse for tekniske styringssystemer, fejlfinding, regulering og '
         'energioptimering',
         'SCADA og PLC som del af anlæg (Biofos 2017-2022), styring og '
         'regulering på el-systemer (Novo 2022-2024), fejlfinding med '
         'rodårsagsmetoden (ARJ, Biofos) og energioptimering af drift (ELOHVAC '
         '2023-2026). Regulering er ikke en sort boks.'),
        ('Arbejder struktureret med vedligeholdelse, dokumentation og opfølgning',
         'Vedligeholdsplaner og dokumentation holdt ajour (Biofos 2017-2022), '
         'dokumentation der bestod revision (Novo 2022-2024), og opfølgning på '
         'aftaler og sager som fast vane (ELOHVAC, Hansen). Struktur gør '
         'driften roligere.'),
        ('Erfaring med koordinering eller ledelse af medarbejdere',
         'Ledelse og koordinering siden 2003: 12 mekanikere (ARJ 2003-2010), '
         '10 medarbejdere på skift (Biofos 2017-2022), 14 mand (Ventek 2022), '
         '5 elektrikere og 3 lærlinge (ELOHVAC 2023-2026) og 4-10 specialister '
         '(Data Power 2024-nu).'),
        ('Serviceminded og kommunikerer professionelt med beboere, '
         'erhvervskunder, kolleger og samarbejdspartnere',
         'Kundedialog i øjenhøjde gennem hele karrieren: serviceaftaler '
         '(ELOHVAC 2023-2026), leverandørforhandlinger (Hansen 2025-2026) og '
         'samtaler med brugere om tekniske løsninger (Novo 2022-2024). '
         'Kommunikation tilpasset modtageren.'),
        ('Tager ansvar, er løsningsorienteret og følger opgaverne til dørs',
         'Ansvaret taget på egne skuldre i alle led: P&L (ELOHVAC 2023-2026), '
         'driftsansvar i døgndrift (Biofos 2017-2022) og projekter fulgt fra '
         'tilbud til aflevering (Ventek 2022). Opgaverne bliver fulgt til '
         'dørs, også de besværlige.'),
        ('Emotionel intelligens og oprigtigt nysgerrig på mennesker',
         'Skiftesamtaler, kundemøder og vanskelige dialoger håndteret med '
         'lytten før svaret siden 2003: medarbejdere i forskellige fagligheder, '
         'kunder med forskellige behov og samarbejdspartnere med andre '
         'perspektiver. Nysgerrigheden er metoden, ikke en egenskab på papiret.'),
        ('Lytter aktivt, spørger ind og gør sig umage med at forstå andres '
         'behov og perspektiver',
         'Behov og perspektiver forstået før løsningen foreslås: driftsdialog '
         'med kunder (ELOHVAC 2023-2026), brugerbehov i projekter (Novo '
         '2022-2024) og daglig ledelse af folk med forskellige fagligheder '
         '(ARJ, Biofos). Den anden parts virkelighed tæller med.'),
        ('Mulighed for at præge den tekniske udvikling af vores ejendomme',
         'Teknologisk udvikling præget før: nye arbejdsgange og værktøjer '
         'indført (Biofos 2017-2022), en AI-afdeling bygget fra nul (Data '
         'Power 2024-nu) og løsninger valgt på holdbarhed (ELOHVAC 2023-2026). '
         'Udviklingen skal kunne mærkes i driften.'),
        ('Et fagligt fællesskab med ordentlighed, at dele viden, hjælpe '
         'hinanden og gøre os umage med opgaverne',
         'Værkstedskultur bygget på ordentlighed siden 2003: viden delt på '
         'tværs af skift (Biofos), lærlinge lært op i faget (ELOHVAC) og '
         'erfaringer samlet, så samme fejl ikke blev fundet to gange (ARJ).'),
        ('Kvalitet betyder noget hos os, både i de tekniske løsninger og i den '
         'måde, vi møder mennesker på',
         'Kvalitet i tekniske løsninger holdt til revision i GMP/FDA/EMA-'
         'miljøer (Novo 2022-2024) og i serviceaftaler (ELOHVAC 2023-2026), '
         'og måden mennesker mødes på har været med i vurderingen af hver '
         'sag: kvalitet uden kontakt er halvt arbejde.'),
    ], widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo – Ansøgning Teknisk driftsleder, PKA Ejendomme')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_PKA_TekniskDriftsleder.docx')
    build(out)
    print(out)
