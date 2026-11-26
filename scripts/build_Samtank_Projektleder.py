# -*- coding: utf-8 -*-
"""Projektleder — Samtank A/S, Prøvestenen, København (dansk opslag -> dansk dokument).

4 sider i masterdesign: brev side 1, CV side 2-3, kravmatrix side 4.
Kontakt fra opslaget: Management Consultant Majbrit Andersen, tlf. 2628 3821
-> hilsen "Kære Majbrit Andersen,". Kun CV krevet ved ansogning, men brugeren
valgte masterdesign som vanligt. Fortrolig behandling.

STILVALG (style_guard godkendt, 3/3 skift mod #432 Kemp & Lauritzen):
  register    = Forsyningssikkerhed under højrisikovilkår
  åbningsgreb = BI (forsyningstallene: 40 procent af benzinmarkedet lobere
                gennem Samtanks tanke for kandidaten naves)
  struktur    = Idé, beslutning, drift (30/60/90 = idéen · beslutningen · driften)

BRUGERSVAR 26.11 (bindende): Prøvestenen = rimelig kørselsafstand fra Måløv
(bekræftet, skriv konkret). Masterdesign (brev + CV + kravmatrix) uanset
opslagets "vi har blot behov for dit CV". Tank-/rør-erfaring dækkes af
rørsystemer og procesanlæg (Ventek-rør + Biofos-proces); holdes som færdigheder
med CV'ets jobs som dokumentation. TIER/Microsoft Project = reel erfaring.

MASTER-REGLER: "elautoriseret maskinmester (LV/MV/HV)" — ALDRIG "elinstallatør".
Ordet "elinstallatør" optræder KUN som JD-citat i rk2-label (JD'ens egne ord).
Datacenter-værktøjskassen (MASTER_RESUME §5) er sand: UPS, ABA/ABV, fiber,
DS/HD 60364, AB 18, ABT 18, KS, opmåling, underentreprenører.

BRUGERENS KORREKTION: humaniseret brev OG CV. Ingen em dash. Ingen forbudte ord.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Samtank A/S · Projektleder, Prøvestenen'
BANNER_RESUME = 'Projektledelse · anlæg · rørsystemer · sikkerhed · økonomi'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('26. november 2026')
    m.meta('Samtank A/S · Prøvestenen, København · tekniske projekter i højrisikomiljø')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Projektleder til tekniske projekter på Prøvestenen',
           bold=True, color='1A1A1A')
    m.para('Kære Majbrit Andersen,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('Omkring 40 procent af den benzin der tankes i Danmark og næsten en tredjedel '
       'af olien løber gennem Samtanks tanke. Virksomheden har otte tankanlæg i fire '
       'byer, står for losning og lastning af skibe, og forsyner Københavns Lufthavn '
       'med jet fuel via direkte piping fra Prøvestenen. Anlæggene er klassificeret '
       'som højrisiko, og brand- og eksplosionsfare følger med hver beslutning. '
       'Spændende projekter med teknisk høj kompleksitet i en '
       'nichevirksomhed med afgørende betydning for Danmarks forsyningssikkerhed, det '
       'er rammen om den projektlederrolle jeg søger.')

    lp('Samtank A/S står for oplagring i tanke og stiller udleveringsfaciliteter til '
       'rådighed, '
       'og kernen er modtagelse, opbevaring og udlevering af olie- og benzinprodukter. '
       'På Prøvestenen, jeres største terminal, gælder det at driftssikkerhed, '
       'myndighedskrav og sikkerhed er afgørende for succes, og det passer til en '
       'driftsnær rolle med reference til Operations Manager. Jeg bliver en tæt '
       'samarbejdspartner for den lokale driftsleder og får både overordnede '
       'projektstyring og de mere operationelle opgaver i hænderne. Projektbeskrivelser, '
       'beslutningsgrundlag, tidsplaner og ressourceplaner og den tekniske og '
       'økonomiske afklaring af projekterne er kernen i opgaven, og økonomi, indkøb, '
       'kontrakter og koordinering følger med i samme hånd.')

    lp('Eksekveringen er mit håndværk. Effektiv projekteksekvering og fremdrift gennem '
       'koordinering med driften, eksterne rådgivere, leverandører og entreprenører, '
       'og opgaverne er klassiske: indhente og vurdere tilbud samt indgå kontrakter '
       'med eksterne leverandører, og den løbende interessenthåndtering med kunder, '
       'myndigheder, rådgivere. 37 medarbejdere og hovedkontor i Aarhus, ejet '
       'ligeligt af Uno-X Mobility Danmark A/S og OK A.m.b.a, og en projektorganisation '
       'hvor jeg sparrer med kolleger på fire andre lokationer. Kunderne og '
       'myndighederne er ikke lag i en plan, men folk jeg ringer til før problemerne '
       'vokser.')

    lp('Overholdelse af gældende sikkerheds-, kvalitets- og myndighedskrav står '
       'øverst: risikovurderinger, arbejdstilladelser og relevant '
       'myndighedsdokumentation på plads før arbejdet går i gang. Sikkerhed, miljø '
       'og kvalitet '
       'har været min hverdag siden 2017, og et kvalitetssystem efter ISO 9001 kender '
       'jeg både fra audits og fra at bygge dokumentationen selv. I søger erfaring med '
       'mekaniske installationer, tankanlæg, rørsystemer eller lignende; mit ligger i '
       'rørsystemer og procesanlæg: procesrør og pumper i døgndrift hos Biofos, rør og '
       'installationer i entrepriserne hos Ventek, og 37 projekter i GMP-regi hvor '
       'hver samling skal holde. Rollen ligger midt i procesindustrien, olie- og '
       'gasindustrien, energisektoren, kort fortalt en driftskritisk virksomhed med '
       'høje krav til sikkerhed og kvalitet.')

    lp('Som person er jeg pragmatisk og løsningsorienteret med et godt overblik, og '
       'solid økonomisk forståelse har været i brug dagligt siden 2017, fra budget og '
       'kontrakter til den løbende opfølgning. Min bred kontaktflade er bygget op '
       'omkring koordinering af eksterne samarbejdspartnere, og den samme flade bruger '
       'jeg til at kommunikere med både myndigheder, operatører og ledelsen. Jeg '
       'skaber et naturligt følgeskab ved at sætte en klar retning, så projekterne '
       'drives sikkert i mål. Uddannelsen er på plads: maskinmester med '
       'el-autorisationen LV/MV/HV, og PRINCE2 i værktøjskassen.')

    lp('Det der tiltaler mig ved Samtank er kort vej fra idé til handling og en hverdag '
       'med høj faglighed, dygtige kolleger. Stor indflydelse på projekternes '
       'gennemførelse og en varieret og langsigtet portefølje af tekniske projekter '
       'er præcis den byttehandel jeg leder efter. Jeg bor i Måløv, rimelig '
       'kørselsafstand til Prøvestenen i København, og har kørekort B (manuelt gear). '
       'Sproget er på plads: dansk og engelsk i skrift og tale. Jeg er klar til en '
       'fortrolig '
       'samtale, Majbrit, når det passer dig.', after=44)

    m.para('Med venlig hilsen', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Maskinmester og projektleder med 20+ år med projektledelse på tekniske '
           'anlæg: rørsystemer, procesanlæg og el-installationer i driftskritiske '
           'miljøer. Økonomi, kontrakter og interessenthåndtering i samme rolle, '
           'sikkerhed og myndighedskrav som en selvfølge, og projekter der afleveres '
           'uden løse ender. Elautoriseret maskinmester (LV/MV/HV), PRINCE2, '
           'AB18/ABT 18.', after=32)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester (el-teknik og ventilation)',
         'Data Power Consultant ApS · København · 2024 – nu (fra nov. 2026 også ELOHVACs '
         'el-tekniske aktiviteter)',
         'AI-afdeling 4-10 personer · el-service og entreprise · 5 elektrikere + 3 lærlinge',
         [('Drift og leverancer', 'El-service og entreprise styret fra tilbud og '
           'planlægning til aflevering, med 4-10 specialister på opgaverne og '
           'Microsoft Project som planlægningsværktøj. Kundekontakten og økonomien '
           'følger opgaven hele vejen.')]),
        ('Ejer / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 – nov. 2026 (virksomheden lukket)',
         'Erhvervskunder · el, ventilation og klima · entreprise · fuldt P&L · serviceaftaler',
         [('Tilbud, kontrakter og økonomi', 'Tilbudsberegning og kalkulation på egne '
           'projekter, kontrakter med kunder og leverandører, og fuldt P&L med '
           'budgetopfølgning. Serviceaftaler der blev fornyet, og aftaler der holdt '
           'fordi opmålingen og dialogen var i orden.'),
          ('Bemanding og styring', '5 elektrikere og 3 lærlinge planlagt og fulgt, '
           'underentreprenører holdt på aftalen, og rapportering på fremdrift i en '
           'fast kadence.')]),
        ('Senior commissioningeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, DKK 2-10 mio. · 25 specialister · GMP/FDA/EMA',
         [('Projekter og myndighedskrav', '37 projekter gennem alle faser med '
           'commissioning, test og idriftsættelse (FAT/SAT, IQ/OQ/PQ). '
           'Myndighedskrav og dokumentation i GMP-regi overholdt, nul kritiske fund '
           'ved aflevering, og interessenthåndtering på tværs af engineering, indkøb '
           'og drift.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022 – nov. 2022',
         '11 samtidige ventilationsprojekter · 14 mand · underleverandører',
         [('Rør og entrepriser', '11 samtidige projekter med 14 mand og '
           'underentreprenører, rør og installationer koordineret på tværs af fag, og '
           'AB18/ABT 18 som aftalegrundlag. Tilbud vurderet, kontrakter indgået, og '
           'økonomien fulgt pr. projekt.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · kritiske anlæg · 10 medarbejdere · skiftehold',
         [('Driftskritisk sikkerhed', 'Drift og vedligehold af kritiske anlæg døgnet '
           'rundt: pumper, HVAC, procesrør, SCADA og PLC. Risikovurderinger, '
           'arbejdstilladelser, APV og LOTO på tværs af skiftehold, og myndigheds-'
           'kontakter som en del af driften.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('Grundlaget', 'Produktionsafdeling med 12 mekanikere og teknikere: vagtplan, '
           'materialer og mål. Risikostyring og kvalitetssikring i praksis, og '
           'rodårsagsanalyser der ændrede fejlhåndteringen.')]),
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
    m.bullet('Rørsystemer og mekaniske installationer', 'Procesrør, pumper og anlæg i '
             'døgndrift (Biofos 2017-2022), rør og installationer i entrepriser '
             '(Ventek 2022), og el-installationer, tavler og styring i egen virksomhed. '
             'UPS, ABA/ABV og fiber fra opgaverne, DS/HD 60364 som grundlag.',
             after=10)
    m.bullet('Sikkerhed og myndighedskrav', 'Risikovurderinger, arbejdstilladelser og '
             'dokumentation i højrisikomiljøer: LOTO og APV på skiftehold, RAMS på '
             'arbejdsstederne, og kvalitetssystem efter ISO 9001 fra audits og '
             'praksis.', after=10)
    m.bullet('Projektstyring og økonomi', 'PRINCE2, Microsoft Project, SAP ERP og '
             'Excel. Budget, tidsplaner og ressourceplaner i alle sager, AB18/ABT 18 '
             'i kontrakterne, og tilbud vurderet og indgået med eksterne leverandører.',
             after=10)
    m.bullet('Koordinering og interessenthåndtering', 'Drift, rådgivere, leverandører '
             'og entreprenører holdt i samme plan. Kunder, myndigheder og kolleger '
             'på fire lokationer betjent med klar kommunikation og fast opfølgning.',
             after=10)
    m.bullet('Anlæg og aflevering', 'Commissioning, test og idriftsættelse fra FAT/SAT '
             'og IQ/OQ/PQ til afleveringsforretning og 1- og 5-års gennemgang. KS og '
             'dokumentation som en del af leverancen, opmåling og akkord i '
             'entrepriserne.', after=10)

    m.section('DE FØRSTE 90 DAGE')
    m.para('Planen følger kæden: idé, beslutning, drift.', after=8)
    m.bullet('Dag 1-30 · Idéen', 'Anlægget på Prøvestenen, porteføljen og '
             'myndighedskravene lært at kende, med driftslederen på rundering og '
             'gennemgang af de igangværende projekter. Mål: jeg kender anlægget og '
             'projekterne, og de første beslutningsgrundlag er opdateret.', after=10)
    m.bullet('Dag 31-60 · Beslutningen', 'Egne projekter ført med tidsplaner, '
             'ressourceplaner og økonomi, tilbud vurderet og kontrakter på plads. '
             'Mål: strukturen kører, og interessenthåndteringen med kunder og '
             'myndigheder er en fast kadence.', after=10)
    m.bullet('Dag 61-90 · Driften', 'Projekterne i stabil fremdrift, sikkerheds- og '
             'myndighedsdokumentationen ajour, og overdragelse til driften kørt '
             'efter bogen. Mål: projekterne drives sikkert i mål, og porteføljen '
             'er synlig for organisationen.', after=10)

    m.section('SPROG, VÆRKTØJER OG PRAKTISK')
    m.para('Dansk (modersmål) · engelsk (professionelt) · persisk (modersmål). SAP ERP, '
           'Excel, Microsoft Project, SharePoint; PRINCE2. AB18/ABT 18. Kørekort '
           'kategori B (manuelt gear). Bosat i Måløv, omkring 40 minutters kørsel fra '
           'Prøvestenen. Tiltrædelse aftales.', after=32)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Projektleder, Samtank A/S · krav og dokumentation',
                   ('Krav i opslaget', 'Dokumenteret erfaring'),
                   [
        ('Planlægning, styring og gennemførelse af tekniske projekter på Prøvestenen i '
         'København',
         'Tekniske projekter styret fra planlægning til aflevering siden 2003: 37 '
         'CAPEX-projekter (Novo 2022-2024), 11 entrepriser (Ventek 2022), egne '
         'projekter (ELOHVAC 2023-2026) og el-opgaver i drift (2024-2026).'),
        ('Erfaring med tekniske projekter inden for mekaniske installationer, tankanlæg, '
         'rørsystemer eller lignende',
         'Rørsystemer og procesanlæg i praksis: procesrør, pumper og HVAC i døgndrift '
         '(Biofos 2017-2022), rør og installationer i entrepriser (Ventek 2022) og '
         'mekaniske anlæg i produktion (ARJ 2003-2010).'),
        ('Driftsnær projektlederrolle i en højrisikovirksomhed, hvor driftssikkerhed, '
         'myndighedskrav og sikkerhed er afgørende',
         'Driftsnær projektledelse i højrisikomiljøer: 24/7-drift af kritiske anlæg '
         '(Biofos 2017-2022), GMP/FDA/EMA-krav i pharma (Novo 2022-2024) og '
         'sikkerhedsarbejde på byggepladser (Ventek 2022).'),
        ('Tæt samarbejde med den lokale driftsleder; overordnet projektstyring og '
         'operationelle opgaver',
         'Samarbejde med driftsledere og drift i alle nyere jobs: skiftehold og '
         'produktion (Biofos 2017-2022), drift i GMP-projekter (Novo 2022-2024) og '
         'egen bemanding (ELOHVAC 2023-2026). Overordnet styring og praktiske '
         'opgaver i samme arbejdsdag.'),
        ('Økonomi, indkøb, kontrakter og koordinering som en del af rollen',
         'Økonomi, indkøb og kontrakter i hænderne siden 2017: fuldt P&L (ELOHVAC '
         '2023-2026), budget og kontrakter i 37 projekter (Novo 2022-2024) og '
         'indkøb i produktion (ARJ 2003-2010).'),
        ('Udarbejde projektbeskrivelser, beslutningsgrundlag, tidsplaner og '
         'ressourceplaner',
         'Projektbeskrivelser og beslutningsgrundlag udarbejdet i GMP-projekter (Novo '
         '2022-2024), tidsplaner og ressourceplaner for 11 entrepriser (Ventek 2022) '
         'og bemanding af 8 mand (ELOHVAC 2023-2026).'),
        ('Teknisk og økonomisk afklaring af projekterne',
         'Teknisk og økonomisk afklaring før og under projekterne: kalkulation og '
         'prisfastsættelse (ELOHVAC 2023-2026), teknisk afklaring med engineering og '
         'fag på tværs (Novo 2022-2024) og opmåling i entrepriser (Ventek 2022).'),
        ('Effektiv projekteksekvering og fremdrift gennem koordinering med driften, '
         'rådgivere, leverandører og entreprenører',
         'Eksekvering og fremdrift i 11 parallelt kørende entrepriser (Ventek 2022) og '
         '37 samtidige projekter (Novo 2022-2024), koordineret med drift, under-'
         'entreprenører og leverandører i alle led.'),
        ('Indhente og vurdere tilbud samt indgå kontrakter med eksterne leverandører',
         'Tilbud vurderet og kontrakter indgået siden 2017: underentreprenører og '
         'leverandører (Ventek 2022, ELOHVAC 2023-2026) og aftaler styret i '
         'SAP-regi (Novo 2022-2024).'),
        ('Løbende koordinering og interessenthåndtering med kunder, myndigheder, '
         'rådgivere og samarbejdspartnere',
         'Interessenthåndtering i praksis: 25 specialister og flere fag på tværs (Novo '
         '2022-2024), kunder og myndigheder (Biofos 2017-2022) og kunder, rådgivere '
         'og leverandører i egen virksomhed (2023-2026).'),
        ('Overholdelse af sikkerheds-, kvalitets- og myndighedskrav, herunder '
         'risikovurderinger, arbejdstilladelser og myndighedsdokumentation',
         'Sikkerhed, kvalitet og myndighedskrav overholdt i alle led: risikovurderinger '
         'og arbejdstilladelser i døgndrift (Biofos 2017-2022), myndighedsdokumentation '
         'i GMP-regi (Novo 2022-2024) og RAMS på byggepladser (Ventek 2022).'),
        ('Del af Samtanks projektorganisation; sparring med kolleger på fire andre '
         'lokationer og tæt kontakt til hovedkontoret i Aarhus',
         'Vant til matrix og sparring på tværs: 25 specialister på tværs af engineering, '
         'indkøb og drift (Novo 2022-2024), team på tværs af lokationer som ejer '
         '(ELOHVAC 2023-2026) og projektorganisation med faste tavlemøder.'),
        ('Erfaring fra procesindustrien, olie- og gasindustrien, energisektoren eller '
         'anden driftskritisk virksomhed med høje krav til sikkerhed og kvalitet',
         'Procesindustrien og driftskritisk drift dækker erfaringen: spildevandsproces '
         'døgnet rundt (Biofos 2017-2022), farmaceutisk produktion under GMP (Novo '
         '2022-2024) og energirenovering og tekniske anlæg (Ventek, ELOHVAC).'),
        ('Solid økonomisk forståelse og bred kontaktflade med koordinering af eksterne '
         'samarbejdspartnere',
         'Økonomisk forståelse fra budget og P&L (ELOHVAC 2023-2026) og projektøkonomi '
         '(Novo 2022-2024). Bred kontaktflade af kunder, underentreprenører og '
         'leverandører bygget op siden 2003.'),
        ('Teknisk uddannelse som maskinmester, elinstallatør, ingeniør eller lignende',
         'Maskinmester er titlen: elautoriseret maskinmester (LV/MV/HV, 2023), B.Tech '
         '(EQF6) i teknologiledelse og maskinteknik (2017-2022) og elteknik på EQF6 '
         '(2000-2003).'),
        ('Pragmatisk og løsningsorienteret med et godt overblik, der sikrer at '
         'projekterne drives sikkert i mål',
         'Overblikket holdt i 11 parallelt kørende entrepriser (Ventek 2022) og 37 '
         'samtidige projekter (Novo 2022-2024). Pragmatisk stil: korte møder, klare '
         'aftaler og løsninger fundet på stedet.'),
        ('Kommunikation med myndigheder, operatører og ledelsen; skaber et naturligt '
         'følgeskab ved at sætte en klar retning',
         'Myndighedskontakt i drift (Biofos 2017-2022) og GMP-revisioner (Novo '
         '2022-2024), ledelsesrapportering i fast kadence, og teams på op til 25 '
         'personer ført med klar retning siden 2003.'),
        ('Bor i rimelig kørselsafstand til Prøvestenen i København',
         'Kørselsafstanden bekræftet: Måløv ligger omkring 40 minutters kørsel fra '
         'Prøvestenen. Kørekort B (manuelt gear).'),
        ('Behersker dansk og engelsk i skrift og tale',
         'Engelsk og dansk brugt professionelt i skrift og tale: dokumentation og møder '
         'på begge sprog (Novo 2022-2024), kundedialog (Ventek, ELOHVAC 2023-2026) og '
         'teknisk formidling siden 2010. Persisk som modersmål oveni.'),
                   ], widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo · Projektleder, Samtank A/S')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Samtank_Projektleder.docx')
    build(out)
    print(out)
