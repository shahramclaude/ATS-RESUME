# -*- coding: utf-8 -*-
"""Project Manager — Syntegon Technology A/S, Sandved (dansk opslag -> DANSK dokument).

4 sider i masterdesign: brev side 1, CV side 2-3, kravmatrix side 4.
Kontaktperson i opslaget: Head of Projects & Planning, Anja N. Andersen
(+45 5138 6440) -> "Kære Anja N. Andersen,". Løn 60-70 tkr./md. i opslaget
(ikke nævnt i dokumentet; CV'ets masterlinje om forventet løn rører vi ikke).
Primær arbejdsplads Sandved eller Silkeborg.

STILVALG (style_guard godkendt, 3/3 skift mod #437 Enity):
  register    = Projekter der leveres som aftalt
  åbningsgreb = BN (projektet som løfte, der holdes hver uge i 4-12 måneder)
  struktur    = Overblik, fremdrift, aflevering (30/60/90 = overblikket ·
                fremdriften · afleveringen)

BRUGERSVAR 26.11 (bindende): lokation = move_if ("kan flytte, hvis jobbet er
rigtigt") — Sandved eller Silkeborg kan begge fungere.

MASTER-REGLER: "elautoriseret maskinmester (LV/MV/HV)" — aldrig "elinstallatør".
BANNED som egne påstande: passioneret, gøre en forskel, dynamisk, demonstreret,
proven track record, vibrant, mission-driven. Ingen em dash nogen steder.
Pharma-erfaringen (Novo: GMP, FDA/EMA, FAT/SAT, IQ/OQ/PQ) er reel og løftes
selvsikkert; "maskinbygger" positioneres ærligt via maskin- og procesanlæg.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_HansenCo_Produktkoordinator.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Syntegon Technology A/S · Project Manager, Sandved'
BANNER_RESUME = 'Projektledelse · komplekse maskinprojekter · økonomi og levering'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('26. november 2026')
    m.meta('Project Manager · Sandved eller Silkeborg')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Project Manager, Syntegon Technology A/S', bold=True,
           color='1A1A1A')
    m.para('Kære Anja N. Andersen,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('Et maskinprojekt til medicinalindustrien er et løfte med en dato på. '
       'Maskinen skal stå i kundens produktion i årevis, og dokumentationen skal '
       'holde lige så længe. Hos Syntegon er opgaverne komplekse, tekniske '
       'projekter fra planlægning til levering: projekter, der typisk løber over '
       '4–12 måneder, med kunden, salg, engineering, automation, indkøb, '
       'produktion, montage, test og service omkring samme tidsplan. Det stiller '
       'krav til den, der skaber struktur, fremdrift og tydelighed: overblik og fremdrift '
       'i en teknisk kompleks hverdag med mange interessenter og afhængigheder.')

    lp('Syntegon er en strategisk lifecycle-partner for medicinal-, biotek- og '
       'fødevareindustrien. Opgaven er udvikling og levering af avancerede '
       'maskiner og produktionsløsninger til medicinalindustrien, og i Sandved '
       'bliver maskinerne tegnet, bygget og samlet. Et stærkt lokalt fællesskab '
       'med omkring 180 engagerede kolleger holder hjulene i gang; globalt er '
       'Syntegon 7.300 medarbejdere på 49 lokationer i mere end 20 lande. '
       'Alligevel er hverdagen præget af korte beslutningsveje, tæt samarbejde '
       'og en uformel omgangstone. Project Manageren er kundens forlængede arm '
       'internt med ansvar for projektets samlede fremdrift, økonomi, ressourcer, '
       'kvalitet og kommunikation, og teamet tæller omkring 10 kolleger under '
       'Head of Projects & Planning.')

    lp('Projektledelse med teknisk tyngde har været omdrejningspunktet siden '
       '2003. PRINCE2 gav metoden, og årene i Ventek gav tempoet: 11 projekter '
       'med 14 mand, fra tilbud over planlægning til montage og aflevering. Hos '
       'Novo Nordisk stod 37 parallelle CAPEX-projekter i 2-10 millioners klassen '
       'på tavlen, 25 specialister på tværs af engineering, indkøb og drift, og '
       'hvert projekt gik gennem konstruktion, udførelse og idriftsættelse med '
       'design reviews, FAT/SAT og dokumenteret opfølgning i GMP- og '
       'FDA/EMA-inspektionsklare miljøer. Solid erfaring med projektledelse og '
       'tekniske løsninger ligger i det, at udarbejde og følge op på tidsplan, '
       'økonomi og ressourceforbrug har været en ugentlig vane, ikke en rapport. '
       'Projekterne er kommet i mål med høj kvalitet til tiden og inden for '
       'budgettet.')

    lp('De første 90 dage har tre konkrete mål, og opgaverne er velkendte: at '
       'lede og koordinere projektgruppen og rapportere projektstatus til '
       'virksomhedens ledergruppe. Overblikket i dag 1-30: projektgruppen '
       'gennemgået, interessenter og afhængigheder kortlagt, og projektøkonomi, '
       'ressourceplanlægning og tidsplaner stående ét sted. Fremdriften i dag '
       '31-60: design reviews, tavlemøder, test og aflevering i en fast rytme '
       'med klare mål, roller og standarder og ansvarlig opfølgning og rettidig '
       'kommunikation, og tidligt nok til at identificere og rapportere risici, '
       'afvigelser og ændringer. Afleveringen i dag 61-90: det første projekt '
       'ført sikkert gennem test og aflevering med tydelig kommunikation og '
       'forventningsafstemning med kunden, aftalte krav, kvalitet og deadlines '
       'dokumenteret, og erfaringerne samlet op som læring og løbende '
       'forbedringer.')

    lp('Den tekniske ballast er på plads. Maskinbygning, automation eller '
       'tekniske produktionsløsninger er ikke fremmede størrelser: procesudstyr, '
       'SCADA og PLC fra driften af biogasanlæg, el og automation fra '
       'medicinalproduktion og montage- og idriftsættelsesforløb fra Ventek og '
       'Novo, som tilsammen er erfaring fra en automatik-, maskinbygger- eller '
       'en anden teknisk projektorganisation. Erfaring fra pharma, medtech, '
       'automation, maskinbygning eller en anden reguleret industri fylder mest: '
       'GMP, dokumentation og FAT/SAT kender jeg fra projekter, hvor kunden stod '
       'klar til at inspicere. Rejseaktivitet i forbindelse med kundebesøg og '
       'test, herunder SAT, tager jeg gerne. Dansk- og engelskkundskaber, '
       'IT-kompetencer, herunder Microsoft Office, og SAP som dagligt værktøj '
       'siden 2017 dækker rapporteringen.')

    lp('Profilen, I søger, er en proaktiv og ansvarlig projektleder, der tager '
       'ansvar, træffer beslutninger og følger op og har ejerskab for projektets '
       'samlede resultat. Afvigelser bliver taget i opløbet, for jeg følger '
       'proaktivt op, når noget afviger fra planen, og presset ændrer ikke tonen: '
       'jeg kommunikerer åbent og respektfuldt. De bedste resultater skabes gennem samarbejde, '
       'og respekt for forskellige fagligheder og perspektiver og stærkt '
       'samarbejde på tværs har båret mine projekter. Kulturen, hvor I holder '
       'vores aftaler, leverer i den forventede kvalitet og siger til i god tid, '
       'hvis noget ikke kan lykkes som planlagt, og hvor man deler viden, lærer '
       'af vores erfaringer, er sådan projektarbejde bør se ud. Arbejdsformen er '
       'struktureret, handlekraftig og løsningsorienteret. At drive komplekse '
       'maskinprojekter sikkert i mål er præcis opgaven i Sandved, og Sandved '
       'eller Silkeborg kan begge fungere: jeg kan flytte, hvis jobbet er '
       'rigtigt. Også vilkårene passer med pension, sundhedsforsikring og '
       'frokostordning, og tiltrædelse kan ske snarest. Jeg ser frem til at høre '
       'fra dig.', after=44)

    m.para('Med venlig hilsen', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Projektleder med maskinteknisk baggrund og 20+ år i tekniske '
           'projekter, fra ventilationsentrepriser til GMP-byggeri. 37 '
           'CAPEX-projekter i 2-10 millioners klassen hos Novo Nordisk, 11 '
           'projekter med 14 mand hos Ventek, og projektøkonomi, tidsplaner og '
           'ressourceplanlægning fulgt tæt i alle led. PRINCE2, FAT/SAT og '
           'dokumentation der holder til revision. Kundens forlængede arm internt '
           'med blik for både teknik, økonomi og aftalte krav.', after=32)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester (el-teknik og ventilation)',
         'Data Power Consultant ApS · København · 2024 – nu (fra nov. 2026 også ELOHVACs '
         'el-tekniske aktiviteter)',
         'AI-afdeling 4-10 personer · el-service og entreprise · 5 elektrikere + 3 lærlinge',
         [('Projekter og teams', 'El-service og entreprise styret fra tilbud til '
           'idriftsættelse med økonomi, tidsplan og aflevering pr. sag. Teams på '
           '4-10 specialister, og opgaver koordineret med kunder og '
           'underleverandører, så aftalerne holder hele vejen.')]),
        ('Ejer / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 – nov. 2026 (virksomheden lukket)',
         'Erhvervskunder · el, ventilation og klima · entreprise · fuldt P&L · serviceaftaler',
         [('Økonomi og aftaler', 'Fuldt P&L-ansvar, serviceaftaler og entreprise '
           'med omkostningskontrol på hver sag. 5 elektrikere og 3 lærlinge '
           'planlagt i det daglige, og leverandører styret på kontrakt, kvalitet '
           'og deadline. Kundedialog og forventningsafstemning var en del af '
           'hverdagen.')]),
        ('Senior commissioningeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, DKK 2-10 mio. · 25 specialister · GMP/FDA/EMA',
         [('Projektstyring i pharma', '37 parallelle CAPEX-projekter med 25 '
           'specialister på tværs af engineering, indkøb og drift. Konstruktion, '
           'udførelse og idriftsættelse med design reviews, FAT/SAT, IQ/OQ/PQ og '
           'dokumentation i GMP- og FDA/EMA-inspektionsklare miljøer, og ugentlige '
           'projektafstemninger om fremdrift, økonomi og risici.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022 – nov. 2022',
         '11 projekter · 14 mand · underleverandører · montage og aflevering',
         [('Projekter fra tilbud til aflevering', '11 projekter med 14 mand og '
           'underleverandører styret på tidsplan, økonomi og kvalitet fra tilbud '
           'over montage til aflevering. Kundedialog og forventningsafstemning '
           'undervejs, og MS Project som planlægningsværktøj.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · kritiske anlæg · 10 medarbejdere · skiftehold',
         [('Drift og vedligehold', 'Forebyggende og korrigerende vedligehold af '
           'kritiske anlæg døgnet rundt: pumper, HVAC, procesrør, SCADA og PLC. '
           'MTBF, MTTR og oppetid fulgt som måltal, reservedelsstyring i orden, '
           'og LOTO, arbejdstilladelser og risikovurderinger på tværs af '
           'skiftehold.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('Produktion og forbedring', 'Produktionsafdeling med 12 mekanikere og '
           'teknikere: vedligehold af maskiner, reservedele og planlægning. '
           'Rodårsagsanalyser der ændrede fejlhåndteringen, og akkord og '
           'opmåling som styringsværktøj.')]),
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
    m.bullet('Projektledelse og økonomi', 'Projektøkonomi, ressourceplanlægning '
             'og tidsplaner styret tæt: budgetopfølgning, rapportering og '
             'opfølgning når noget afviger. PRINCE2 som metode, MS Project, '
             'Excel og SAP som værktøjer.', after=10)
    m.bullet('Tekniske projekter', 'Maskinbygning, automation og tekniske '
             'produktionsløsninger: procesudstyr, el, SCADA og PLC, montage og '
             'idriftsættelse. GMP, dokumentation og FAT/SAT fra '
             'medicinalindustrien.', after=10)
    m.bullet('Kunder og samarbejde', 'Kundedialog og forventningsafstemning som '
             'en del af arbejdet, ikke en ekstra opgave. Koordinering på tværs '
             'af salg, engineering, indkøb, produktion og service, og tydelig '
             'rapportering til ledergruppe.', after=10)

    m.section('DE FØRSTE 90 DAGE')
    m.para('Planen følger opgaven: overblikket, fremdriften, afleveringen.',
           after=8)
    m.bullet('Dag 1-30 · Overblikket', 'Projektgruppen og de igangværende '
             'projekter lært at kende, interessenter og afhængigheder kortlagt, '
             'og økonomi, tidsplaner og ressourcer stående ét sted. Mål: status '
             'er lige så tydelig for ledergruppen som for projektgruppen.',
             after=10)
    m.bullet('Dag 31-60 · Fremdriften', 'Design reviews, tavlemøder og '
             'rapportering i fast rytme, og kundedialogen om ændringer og '
             'forventninger kørende. Mål: afvigelser bliver set og meldt tidligt, '
             'ikke ved aflevering.', after=10)
    m.bullet('Dag 61-90 · Afleveringen', 'Det første projekt ført gennem test og '
             'aflevering med dokumentation på plads, og erfaringerne samlet op '
             'med teamet. Mål: leverance til aftalte krav, kvalitet og deadlines '
             'og en arbejdsform, der holder.', after=10)

    m.section('SPROG, VÆRKTØJER OG PRAKTISK')
    m.para('Dansk (modersmål) · engelsk (professionelt) · persisk (modersmål). '
           'Microsoft Office, SAP (dagligt siden 2017), MS Project, Power BI; '
           'PRINCE2. Kørekort kategori B (manuelt gear). Bosat i Måløv; Sandved '
           'eller Silkeborg kan begge fungere, og jeg kan flytte, hvis jobbet er '
           'rigtigt. Tiltrædelse snarest muligt.', after=32)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Project Manager, Syntegon · krav og dokumentation',
                   ('Krav i opslaget', 'Dokumenteret erfaring'),
                   [
        ('Relevant teknisk eller kommerciel uddannelse, fx ingeniør, '
         'maskiningeniør, maskinkonstruktør, automationsteknolog eller tilsvarende',
         'Maskinmester (2017) og B.Tech i teknologiledelse og maskinteknik fra '
         'Copenhagen School of Marine Engineering & Technology Management '
         '(2017-2022, GPA 7,6) svarer til maskiningeniør eller maskinkonstruktør. '
         'Dertil elautorisation LV/MV/HV (maj 2023) og PRINCE2.'),
        ('Solid erfaring med projektledelse og tekniske løsninger',
         'Siden 2003: 11 projekter med 14 mand som projekt- og værkstedsleder '
         '(Ventek 2022), 37 CAPEX-projekter som projektleder og '
         'commissioningeniør (Novo Nordisk 2022-2024) og entreprise med '
         'økonomistyring (ELOHVAC 2023-2026). Teknik og styring fulgt ad hele '
         'vejen.'),
        ('Ledelse af komplekse, tekniske projekter',
         'Hos Novo Nordisk: 37 parallelle CAPEX-projekter i 2-10 millioners '
         'klassen, 25 specialister på tværs af engineering, indkøb og drift, og '
         'GMP- og FDA/EMA-inspektionsklare miljøer. Kompleksiteten ligger i mange '
         'interessenter, afhængigheder og dokumentation, og den kender jeg.'),
        ('Forståelse for maskinbygning, automation eller tekniske '
         'produktionsløsninger',
         'Procesudstyr, pumper, HVAC og procesrør i drift (Biofos 2017-2022), '
         'SCADA og PLC som del af anlæg, el og automation i medicinalproduktion '
         '(Novo 2022-2024) og ventilations- og tekniske løsninger bygget og '
         'afleveret (Ventek 2022).'),
        ('Projektøkonomi, ressourceplanlægning og tidsplaner',
         'Budgetopfølgning på projekter i 2-10 millioners klassen (Novo '
         '2022-2024), 14 mand planlagt i ugeplaner (Ventek 2022), daglig økonomi '
         'og omkostningskontrol med P&L-ansvar (ELOHVAC 2023-2026) og MS Project, '
         'Excel og SAP som værktøjer.'),
        ('God kommerciel forståelse og erfaring med kundedialog',
         'Tilbud, kontrakter og kundedialog fra Ventek (2022) og ELOHVAC '
         '(2023-2026), hvor forhandlinger med leverandører og kunder hørte til '
         'den daglige drift. Forventningsafstemning i øjenhøjde er en del af '
         'projektledelsen, ikke et tillæg.'),
        ('Stærke koordinations- og kommunikationsevner',
         'Koordinering af 25 specialister på tværs af engineering, indkøb og '
         'drift (Novo 2022-2024), 14 mand og underleverandører (Ventek 2022) og '
         'tværfaglige leverancer med salg, montage og service. Ugentlige '
         'projektafstemninger og tydelig rapportering hele vejen.'),
        ('Gode IT-kompetencer, herunder Microsoft Office',
         'Microsoft Office i det daglige, SAP som dagligt værktøj siden 2017, MS '
         'Project til planlægning og Power BI til opfølgning. Dokumentation og '
         'rapportering sat i system, så tallene er de samme i projektgruppen og i '
         'ledergruppen.'),
        ('Gode dansk- og engelskkundskaber',
         'Dansk og engelsk i skrift og tale fra uddannelse og arbejde i '
         'internationale miljøer. Engelsk brugt som projektsprog i GMP-miljøer, '
         'hvor dokumentation, audits og kommunikation med internationale '
         'interessenter foregik på engelsk.'),
        ('Teknisk baggrund fra en automatik-, maskinbygger- eller en anden '
         'projektorganisation',
         'Novo Nordisk (2022-2024) og Ventek (2022) er tekniske '
         'projektorganisationer med engineering, automation, montage og test i '
         'samme kæde, og ELOHVAC (2023-2026) og ARJ (2003-2010) er maskin- og '
         'el-virksomheder, hvor projekterne blev bygget, ikke kun beskrevet.'),
        ('Pharma, medtech, automation, maskinbygning eller en anden '
         'reguleret industri som baggrund',
         'Novo Nordisk (2022-2024): GMP, FDA/EMA-inspektionsklare faciliteter, '
         'hygiejnezoner, FAT/SAT og IQ/OQ/PQ med dokumentation der holdt til '
         'revision. Pharma er ikke nyt terræn; kravene til dokumentation og '
         'sporbarhed kender jeg indefra.'),
        ('Lede og koordinere projektgruppen gennem hele projektforløbet',
         '25 specialister på tværs af engineering, indkøb og drift (Novo '
         '2022-2024), 14 mand (Ventek 2022), 12 mekanikere og teknikere (ARJ '
         '2003-2010) og 10 medarbejdere på skiftehold (Biofos 2017-2022). '
         'Projektgrupper er blevet ledet gennem hele forløbet, ikke kun i '
         'opstarten.'),
        ('Udarbejde og følge op på tidsplan, økonomi og ressourceforbrug',
         'Månedlig økonomiopfølgning på 37 projekter (Novo 2022-2024), ugeplaner '
         'og timeforbrug på 14 mand (Ventek 2022), daglig driftsøkonomi med P&L '
         '(ELOHVAC 2023-2026) og akkord og opmåling som styringsværktøj (ARJ '
         '2003-2010).'),
        ('Tydelig kommunikation og forventningsafstemning med kunden',
         'Bygherreferie på 37 projekter (Novo 2022-2024) med ugentlige '
         'afstemninger om fremdrift, ændringer og deadlines, kundedialog på '
         'ventilationsprojekter (Ventek 2022) og serviceaftaler med klare '
         'vilkår (ELOHVAC 2023-2026). Projekterne er leveret til tiden og inden '
         'for budget.'),
        ('Planlægge design reviews, tavlemøder, test og aflevering',
         'Design reviews som fast punkt i CAPEX-forløb (Novo 2022-2024), '
         'tavlemøder og daglig koordination i montage og produktion (Ventek, '
         'ARJ) og test og aflevering med FAT/SAT, IQ/OQ/PQ og KS-dokumentation. '
         '5S og Standard Work som arbejdsform.'),
        ('Identificere og rapportere risici, afvigelser og ændringer',
         'Risikovurderinger, GAP-analyser og audits efter ISO 9001/14001 fra '
         'Novo-miljøet (2022-2024), afvigelser håndteret tidligt i drift (Biofos '
         '2017-2022) og præventivt vedligehold som metode til at finde fejl, før '
         'de voksede.'),
        ('Rapportere projektstatus til virksomhedens ledergruppe',
         'Ugentlige projektafstemninger og præsentation af fremskridt for '
         'afdelingsleder og projektsupport (Novo 2022-2024), månedsrapportering '
         'med budget og forbrug (Ventek, ELOHVAC) og direkte rapportering til '
         'ledelse som CTO (Data Power 2024-nu).'),
        ('Rejseaktivitet i forbindelse med kundebesøg og test, herunder SAT',
         'Rejseaktivitet mellem sites og kunder har været en del af arbejdet '
         'siden 2003, og FAT/SAT-forløb med kundernes deltagelse kender jeg fra '
         'Novo (2022-2024). Kundebesøg og test, herunder SAT, også uden for '
         'normal arbejdstid, er velkendt terræn.'),
        ('Projekter, der typisk løber over 4–12 måneder: udvikling og levering af '
         'avancerede maskiner og produktionsløsninger til medicinalindustrien',
         'CAPEX-projekterne hos Novo (2022-2024) løb fra konstruktion til '
         'idriftsættelse over måneder ad gangen med GMP-dokumentation hele vejen, '
         'og Ventek-projekterne (2022) fra tilbud til aflevering. Forløb på 4-12 '
         'måneder med mange interessenter er det terræn, jeg kender bedst.'),
    ], widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo – Ansøgning Project Manager, Syntegon')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_Syntegon_ProjectManager.docx')
    build(out)
    print(out)
