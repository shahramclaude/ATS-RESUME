#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Produktionsteknolog til Engineering og Produkt vedligeholdelse —
NOVENCO Building & Industry A/S, Næstved.

Dansk opslag -> DANSK dokument (4 sider). TEMPLATE Gentofte-2027.
SAMME-FIRMA-GENANSØGNING (Director, Project Execution = #449) -> INTET
genbrug: ny fil, ny åbning (BV), nyt register, ny struktur, frisk tekst.

BRUGERSVAR (bindende):
1. CAD = DELVIS: AutoCAD fra el- og maskinteknisk design (reel/nær-reel);
   Inventor og Vault = ukendte -> oplærbare, PDM-logik overføres. ÆRLIGT.
2. Konstruktion/produktionsgrundlag/ETO = DELVIS: produktion/maskinværksted +
   teknisk dokumentation/frigivelse REEL (ARJ/Novo); ETO som overført viden.
3. Hilsen = "Kære ansættende leder," (intet navn i opslaget).
4. Næstved = commute_ok (samme adresse bekræftet 28.11) -> konkret.

STIL (3/3 mod #445 NordicCell): register "Præcision med produktionen for
øje", åbning BV (produktets liv efter lanceringen), struktur "Vedligehold,
tilpasning, understøttelse" (30/60/90). Ingen em dash. 'proven' (i About-
teksten) = BANNED. "elautoriseret maskinmester" i CV-titler som kanonisk.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_Gentofte_DriftslederEjendomme_2027.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'NOVENCO · Produktionsteknolog, Engineering & PMA · Næstved'
BANNER_RESUME = 'KONSTRUKTION · PRODUKTION · DOKUMENTATION · VENTILATION'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('30. november 2026')
    m.meta('NOVENCO Building & Industry A/S · Næstved')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning om stillingen som produktionsteknolog til Engineering '
              'og produktvedligeholdelse', bold=True, color='1A1A1A')
    m.para('Kære ansættende leder,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('En ventilationsløsning forlader ikke tegnebordet, når den går i '
       'produktion. Den møder kunder, der vil have den tilpasset, en '
       'produktion, der vil have den optimeret, og krav til energieffektivitet, '
       'der skærpes år for år. Arbejdet med at udvikle, optimere og '
       'vedligeholde tekniske løsninger er præcis det, der holder en '
       'produktfamilie relevant, længe efter lanceringen er glemt.')

    lp('Rollen som produktionsteknolog i Engineering hos NOVENCO ligger midt i '
       'den bevægelse. Opgaven er at vedligeholde og optimere produkter og '
       'omsætte kundekrav til produktionsklare løsninger, der skaber værdi for '
       'både kunder og produktion, i en hverdag med høj kvalitet, effektiv '
       'produktion og kundetilpassede ventilationsprojekter. Rollen er del af '
       'Engineering To Order og refererer til Engineering Manager, og '
       'produktvedligeholdelse, teknisk support og Engineering-to-Order (ETO) '
       'er de tre ben, rollen står på.')

    lp('Min faglighed er praktisk forankret. Maskinmester med el- og '
       'maskinteknisk design i bagagen, og konstruktion, produktionsgrundlag '
       'og teknisk dokumentation i en produktionsvirksomhed kender jeg '
       'indefra: fra maskinværksted og produktlinje, hvor emnet skulle passe '
       'første gang, til dokumentation og frigivelsesprocesser under '
       'GMP/FDA/EMA-krav, hvor intet blev frigivet uden grundlag. AutoCAD har '
       'jeg arbejdet med fra designfaget, og Autodesk Inventor og Vault er jeg '
       'ny i, men CAD- og dokumentstyringslogikken er den samme, og '
       'oplæringen er kort. ERP-systemer samt dokumentstyring og '
       'frigivelsesprocesser har været en del af arbejdet i årevis, med SAP '
       'som dagligt værktøj siden 2017.')

    lp('De første 90 dage følger opgavens tre sider. Dag 1-30 er '
       'vedligeholdelsen: produktfamilierne, det eksisterende '
       'produktionsgrundlag og dokumentationen gennemgået, og analyser, design '
       'reviews og produktoptimeringer sat i system, før der ændres på noget. '
       'Dag 31-60 er tilpasningen: Engineering-to-Order processer og '
       'produktoptimering taget i brug i praksis, og de første ETO-opgaver '
       'kørt fra design review til frigivelse af produktionsgrundlag. Dag '
       '61-90 er understøttelsen: her kommer teknisk fejlfinding, dokumentopdateringer og '
       'håndtering af engineering changes i en fast rytme med produktionen, og '
       'de første cost-down initiativer og produktforbedringer, der styrker '
       'kvalitet, effektivitet og konkurrenceevne, på bordet.')

    lp('Jeg er teknisk stærk og struktureret, med en analytisk og struktureret '
       'tilgang, der ender i en løsning, og gode samarbejds- og '
       'kommunikationsevner '
       'på dansk og engelsk har fulgt mig gennem hele karrieren. Den store '
       'kontaktflade på tværs af Engineering, Produktion, Supply Chain, Salg og '
       'Projekter tiltaler mig, for det er der, løsningerne bliver gode: et '
       'uformelt og samarbejdsorienteret arbejdsmiljø med fokus på videndeling '
       'er sådan, jeg arbejder bedst. ETO-processen er ikke mit '
       'hverdagssprog endnu, men mønsteret fra kundetilpassede løsninger, '
       'tilbud og aflevering genkender jeg fra ventilation, el og klima, hvor '
       'kundekrav skulle ende som noget, der kunne bygges.')

    lp('NOVENCO er en nøgleposition i en international virksomhed med stærke '
       'tekniske kompetencer, og at arbejde med både '
       'produktvedligeholdelse og kundespecifikke udviklingsopgaver, med faglig '
       'udvikling inden for konstruktion, produktoptimering og ETO-processer '
       'er præcis den næste faglige rejse, jeg søger. Næstved fungerer nemt '
       'fra Måløv, en konkurrencedygtig lønpakke og attraktive '
       'ansættelsesvilkår er i orden, og udsigten til at bidrage til '
       'udviklingen af energieffektive ventilationsløsninger med global '
       'anvendelse trækker. Jeg ser frem til at høre fra dig.', after=44)

    m.para('Med venlig hilsen', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Maskinmester og elteknisk designer med 20+ år i tekniske løsninger, '
           'produktion og dokumentation. Konstruktion og produktionsgrundlag '
           'praktisk forankret fra maskinværksted og projektleverancer, '
           'teknisk dokumentation og frigivelsesprocesser under skærpede '
           'krav, og AutoCAD fra designfaget. SAP dagligt siden 2017. '
           'Ventilationsløsninger i bygninger og industri er velkendt '
           'territorium, og nye CAD-værktøjer er jeg hurtig til.', after=32)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester (el-teknik og ventilation)',
         'Data Power Consultant ApS · København · 2024 – nu (fra nov. 2026 også ELOHVACs '
         'el-tekniske aktiviteter)',
         'AI-afdeling 4-10 personer · el-service og entreprise · 5 elektrikere + 3 lærlinge',
         [('Løsninger fra krav til virkelighed', 'Kundekrav omsat til '
           'tekniske løsninger, der kunne bygges og afleveres: fra '
           'specifikation over designvalg til idriftsættelse med dokumentation '
           'i orden. Teams på 4-10 specialister koordineret, og løsningerne '
           'fulgt hele vejen til kunden.')]),
        ('Ejer / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 – nov. 2026 (virksomheden lukket)',
         'Erhvervskunder · el, ventilation og klima · entreprise · fuldt P&L · serviceaftaler',
         [('Kundetilpassede løsninger', 'Kundespecifikke løsninger på el, '
           'ventilation og klima tegnet, beregnet og bygget pr. opgave: '
           'kundekrav til produktions- og installationsklare løsninger, '
           'omkostninger vurderet undervejs, og aflevering med '
           'dokumentation, som kunden kunne bruge bagefter.')]),
        ('Senior commissioningeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, DKK 2-10 mio. · 25 specialister · GMP/FDA/EMA',
         [('Grundlag og frigivelse', 'Dokumentation, '
           'produktionsgrundlag og frigivelsesprocesser i et miljø, hvor '
           'intet gik i drift uden grundlag: FAT/SAT og IQ/OQ/PQ fra '
           'konstruktion til idriftsættelse, og ændringer håndteret gennem '
           'formelle engineering changes, ikke i hånden.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022 – nov. 2022',
         '11 projekter · 14 mand · underleverandører · montage og aflevering',
         [('Produktion og montage', 'Ventilationsløsninger i bygninger '
           'fulgt fra tegning til montage: 11 projekter, 14 mand og '
           'underleverandører, hvor tegninger og produktionsgrundlag skulle '
           'holde i praksis. Fejlfinding på anlæg før aflevering, og '
           'rettelser gennemført uden at stoppe fremdriften.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · kritiske anlæg · 10 medarbejdere · skiftehold',
         [('Support i døgndrift', 'Fejlfinding og teknisk support til '
           'driften døgnet rundt: pumper, HVAC, procesrør og el analyseret '
           'når noget svigtede, dokumentation opdateret efter hver ændring, '
           'og løsninger vurderet på holdbarhed frem for på hastighed '
           'alene.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('Værksted og produktionsgrundlag', 'Maskinværksted og produktlinje '
           'kendt indefra: emner og maskiner bygget og repareret efter '
           'tegning, produktionsgrundlag vurderet på, om det kunne lade sig '
           'gøre i praksis, og 12 mekanikere og teknikere hjulpet af en '
           'tegning, der var til at forstå.')]),
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
    m.bullet('Konstruktion og dokumentation', 'Konstruktion og '
             'produktionsgrundlag vurderet på, om det kan produceres, og '
             'teknisk dokumentation, tegninger og grundlag holdt ajour, så '
             'produktionen ikke gættede. Design reviews brugt som værktøj, '
             'ikke som ceremoni.', after=10)
    m.bullet('Produktion og fejlfinding', 'Nær produktionen og driften, '
             'fra maskinværksted til procesanlæg, ligger teknisk fejlfinding '
             'som en fast opgave. '
             'Fejl fundet ved rodårsagen, og løsninger der holder i '
             'produktionen, ikke kun på tegningen.', after=10)
    m.bullet('Systemer og frigivelse', 'ERP (SAP dagligt siden 2017), '
             'dokumentstyring og frigivelsesprocesser under skærpede krav, '
             'og CAD som arbejdsredskab: AutoCAD fra designfaget, Inventor '
             'og Vault som næste værktøjer i samme logik.', after=10)
    m.bullet('Samarbejde og formidling', 'Kontaktflade på tværs af '
             'Engineering, Produktion, Supply Chain, Salg og Projekter '
             'trives jeg i. Dansk og engelsk i skrift og tale, og '
             'videndeling som en naturlig del af arbejdet.', after=10)

    m.section('DE FØRSTE 90 DAGE')
    m.para('Planen følger opgaven: vedligeholdelsen, tilpasningen, '
           'understøttelsen.', after=8)
    m.bullet('Dag 1-30 · Vedligeholdelsen', 'Produktfamilierne, '
             'produktionsgrundlaget og dokumentationen gennemgået, og analyser '
             'og design reviews sat i system. Mål: jeg kender produkterne og '
             'grundlaget, før der rettes i det.', after=10)
    m.bullet('Dag 31-60 · Tilpasningen', 'ETO-opgaver kørt fra design review '
             'til frigivelse af produktionsgrundlag, og kundekrav omsat til '
             'produktionsklare løsninger i samarbejde med produktionen. Mål: '
             'flowet fra krav til frigivelse virker.', after=10)
    m.bullet('Dag 61-90 · Understøttelsen', 'Fejlfinding, '
             'dokumentopdateringer og engineering changes i fast rytme med '
             'produktionen, og de første cost-down initiativer belyst. Mål: '
             'produktionen har en teknisk modspiller, den stoler på.',
             after=10)

    m.section('SPROG, VÆRKTØJER OG PRAKTISK')
    m.para('Dansk (modersmål) · engelsk (professionelt) · persisk (modersmål). '
           'AutoCAD; SAP, Excel, CMMS; PRINCE2. Inventor og Vault som '
           'korte oplæringsforløb. Kørekort kategori B (manuelt gear). Bosat '
           'i Måløv; Næstved fungerer nemt derfra.', after=8)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Krav og dokumentation · Produktionsteknolog, NOVENCO',
                   ('Krav i opslaget', 'Dokumentation'),
                   [
        ('Teknisk uddannelse som ingeniør, produktionsteknolog, maskinmester '
         'eller lignende',
         'Maskinmester med elautorisation LV/MV/HV (2023) og B.Tech (EQF6) i '
         'teknologiledelse og maskinteknik (2017-2022), suppleret med el- og '
         'maskinteknisk design fra Tehran Technical University (2000-2003). '
         'Den tekniske uddannelse er på plads, og erfaringen fra '
         'produktionens verden følger med.'),
        ('Erfaring med konstruktion, produktionsgrundlag og teknisk '
         'dokumentation i en produktionsvirksomhed',
         'Produktionsvirksomheden kender jeg indefra fra ARJ Engineering '
         '(2003-2010): maskinværksted og produktlinje, hvor konstruktion og '
         'produktionsgrundlag blev vurderet på, om de kunne lade sig gøre. '
         'Dokumentation og frigivelse har jeg siden kørt i fuldt '
         'format ved Novo Nordisk (2022-2024), og tegningsarbejdet er '
         'praktisk forankret i el- og maskinteknisk design.'),
        ('Kendskab til Engineering-to-Order processer og produktoptimering',
         'Engineering-to-Order processer og produktoptimering er overført '
         'viden for mig: kundetilpassede løsninger på ventilation, el og '
         'klima (ELOHVAC 2023-2026) følger samme mønster fra kundekrav over '
         'designvalg til produktions- og installationsklar løsning, og '
         'produktoptimering har været en del af servicearbejdet på '
         'eksisterende anlæg.'),
        ('Erfaring med ERP-systemer samt dokumentstyring og '
         'frigivelsesprocesser',
         'ERP-systemer samt dokumentstyring og frigivelsesprocesser er daglig '
         'disciplin: SAP dagligt siden 2017, og frigivelse af '
         'produktionsgrundlag under GMP/FDA/EMA-krav ved Novo Nordisk, hvor '
         'FAT/SAT og IQ/OQ/PQ var vejen fra konstruktion til frigivet '
         'anlæg.'),
        ('Praktisk erfaring med Autodesk Inventor, AutoCAD og Vault',
         'AutoCAD har jeg arbejdet med fra el- og maskinteknisk designfag '
         '(2000-2003) og i tegningsarbejdet siden. Autodesk Inventor og Vault '
         'er jeg ny i, og det skriver jeg ligeud: CAD- og '
         'dokumentstyringslogikken er den samme på tværs af værktøjer, og '
         'jeg lærer nye systemer hurtigt.'),
        ('Analytisk tilgang og gode '
         'samarbejds- og kommunikationsevner på dansk og engelsk',
         'Tilgangen bygget på analyse og struktur fra '
         'fejlfinding og projektleverancer, og gode samarbejds- og '
         'kommunikationsevner på dansk og engelsk brugt dagligt: kunder, '
         'leverandører og produktion på tre sprog (dansk, engelsk, persisk).'),
        ('Vedligeholde og forbedre eksisterende produktfamilier gennem '
         'analyser, design reviews og produktoptimeringer',
         'Eksisterende tekniske løsninger vedligeholdt og forbedret gennem '
         'analyser og systematisk gennemgang: serviceaftaler på eksisterende '
         'anlæg (ELOHVAC), tilstandsvurdering og optimering af tekniske '
         'systemer (Biofos, Vestas 2024-2026), og design reviews brugt som '
         'arbejdsform før ændringer.'),
        ('Udarbejde og opdatere teknisk dokumentation, tegninger og '
         'produktionsgrundlag',
         'Udarbejdet og opdateret som en del af arbejdet: teknisk dokumentation, '
         'tegninger og produktionsgrundlag, KS og afleveringsdokumentation '
         '(ELOHVAC), dokumentation der holdt til revision (Novo Nordisk), og '
         'tegninger vurderet i værkstedet på, om de var til at bygge efter '
         '(ARJ).'),
        ('Gennemføre Engineering-to-Order opgaver fra design review til '
         'frigivelse af produktionsgrundlag',
         'Forløbet fra design review til frigivelse kender jeg i praksis fra '
         'CAPEX-projekter (Novo Nordisk 2022-2024): krav gennemgået, løsning '
         'valgt, grundlag frigivet, og først da bygget. ETO-betegnelsen er '
         'ny, men forløbet er velkendt.'),
        ('Understøtte produktionen ved teknisk fejlfinding, dokumentopdateringer '
         'og håndtering af engineering changes',
         'Fejlfinding og dokumentopdateringer som teknisk support til '
         'produktion og drift har været kernen siden 2003: værksted og '
         'produktlinje (ARJ), kritiske anlæg i døgndrift (Biofos), og '
         'engineering changes håndteret gennem formelle kanaler ved Novo '
         'Nordisk.'),
        ('Bidrage til cost-down initiativer og produktforbedringer, der '
         'styrker kvalitet, effektivitet og konkurrenceevne',
         'Cost-down initiativer og produktforbedringer har været en del af '
         'hverdagen som virksomhedsejer: tilbud beregnet til en pris, der '
         'holdt, materialevalg og løsninger vurderet på totaløkonomi, og '
         'forbedringer der styrker kvalitet, effektivitet og konkurrenceevne '
         'sat i værk uden at gå på kompromis med holdbarheden.'),
        ('Omsætte kundekrav til produktionsklare løsninger, der skaber værdi '
         'for både kunder og produktion',
         'Kundekrav omsat til løsninger, der kunne bygges og afleveres, '
         'gennem hele karrieren: fra kundespecifikke løsninger på el, '
         'ventilation og klima (ELOHVAC) til 11 ventilationsprojekter med '
         'produktion og montage (Ventek 2022). Værdien måles på både kunden '
         'og produktionen.'),
        ('Stor kontaktflade på tværs af Engineering, Produktion, Supply Chain, '
         'Salg og Projekter',
         'Kontaktfladen på tværs af funktioner er min faste arbejdsform: '
         'salg og beregning, indkøb og leverandører, produktion og montage '
         'og projekter i drift samlet om samme løsning. Fra Novo Nordisks 25 '
         'specialister til ELOHVACs kunder og underentreprenører.'),
        ('Produktionsvirksomhed',
         'Produktionsvirksomhed og maskinværksted kender jeg indefra fra ARJ '
         'Engineering (2003-2010), og produktionens logik har fulgt mig '
         'gennem Venteks montageforløb og Novo Nordisks fabriksmiljø, hvor '
         'leverancer og deadlines ikke kunne flyttes efter behag.'),
        ('Dokumentstyring og frigivelsesprocesser',
         'Dokumentstyring og frigivelsesprocesser under skærpede krav: '
         'GMP/FDA/EMA ved Novo Nordisk, KS og afleveringsdokumentation i '
         'entreprise (ELOHVAC) og CMMS-dokumentation i drift (Biofos). '
         'Frigivelse sker på grundlag, ikke på mavefornemmelse.'),
        ('Produktoptimering',
         'Produktoptimering som løbende disciplin: eksisterende anlæg '
         'optimeret i servicearbejdet (ELOHVAC), tekniske systemer forbedret '
         'på driftsdata (Biofos, Vestas 2024-2026), og løsninger vurderet på '
         'holdbarhed, energi og totaløkonomi.'),
        ('Teknisk support til produktionen',
         'Support til produktion og drift har været rollen siden '
         '2003, senest som teknisk modspiller for kritiske anlæg døgnet '
         'rundt (Biofos 2017-2022) og som ansvarlig for tekniske løsninger i '
         'entreprise (ELOHVAC 2023-2026). Supporten kommer med hænderne '
         'med.'),
        ('Energieffektive ventilationsløsninger',
         'Ventilation er velkendt territorium: ventilationsløsninger i '
         'bygninger fra projektering til aflevering (Ventek 2022), ventilation '
         'og klima i service (ELOHVAC 2023-2026), og energieffektive løsninger '
         'som en naturlig del af arbejdet med eksisterende anlæg, hvor '
         'forbruget er en del af regnestykket.'),
                   ],
                   widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo — Ansøgning og CV — Produktionsteknolog, '
                       'NOVENCO')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_NOVENCO_Produktionsteknolog.docx')
    build(out)
    print(out)
