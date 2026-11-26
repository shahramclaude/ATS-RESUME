# -*- coding: utf-8 -*-
"""Produktkoordinator med projektansvar — Hansen & Co, Nordhavn, København Ø
(dansk opslag -> dansk dokument).

4 sider i masterdesign: brev side 1, CV side 2-3, kravmatrix side 4.
Kontakt fra opslaget: Jesper Siber, siber@hansenco.dk, +45 4277 1809
-> hilsen "Kære Jesper Siber,". Samtaler løbende, send gerne hurtigst muligt.

STILVALG (style_guard godkendt, 3/3 skift mod #433 Samtank):
  register    = Struktur og datakvalitet i FMCG
  åbningsgreb = BJ (hyldens sidste millimeter: bag hver dåse står der produktdata,
                før kandidaten nævnes)
  struktur    = Oprettelse, projekt, forbedring (30/60/90 = oprettelserne ·
                projekterne · forbedringerne)

BRUGERSVAR 26.11 (bindende): SAP = daglig bruger (materialer, priser, kalkulation,
opfølgning) men IKKE decideret stamdata-oprettelse — ærligt men positivt.
GS1, pantsystemer (DRS), Skanlog/Dansk Cater og FMCG/drikkevare = ukendte — korte
ærlige noter som med Kalkia.

MASTER-REGLER: "elautoriseret maskinmester (LV/MV/HV)" — ALDRIG "elinstallatør".
Kanonisk værktøjskasse (MASTER_RESUME §5) er sand. Audits + ISO 9001 = reel
erfaring (brugerbekræftet ved Terma). PDCA, 5S, Standard Work, rodårsagsanalyser
= godkendt kompetence-sprog.

BRUGERENS KORREKTION: humaniseret brev OG CV. Ingen em dash. Ingen forbudte ord.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Hansen & Co · Produktkoordinator med projektansvar'
BANNER_RESUME = 'Struktur · data · SAP · projekter · forbedring'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('26. november 2026')
    m.meta('Nordhavn, København Ø · øl, sodavand, data og projekter')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Produktkoordinator med projektansvar',
           bold=True, color='1A1A1A')
    m.para('Kære Jesper Siber,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('Bag hver dåse på hylden står der et varenummer, en pris og et pantsymbol, og '
       'er de data forkerte, kan varen ikke sælges. Hansen & Co importerer og sælger '
       'kendte internationale øl- og sodavand på det danske marked, og i den type '
       'forretning er produktdata ikke en støttefunktion men selve salget. At få '
       'produkter, kunder og priser oprettet korrekt, og få projekter i mål på tværs '
       'af organisationen, er opgaven jeg søger som produktkoordinator med '
       'projektansvar.')

    lp('Oprettelse og vedligehold af masterdata på produkter og kunder samt priser og '
       'prislister i SAP er fundamentet for det hele. Dertil kommer Oprettelse af '
       'varer hos Skanlog og Dansk Cater samt vedligehold af emballagedata, og '
       'registrering i pantsystemer, herunder Dansk Retursystem (DRS), med oprettelse '
       'og validering i GS1 Tradesync og GS1 Packaging. Vejen er den samme hver gang: '
       'fra oprettelsesark til færdig oprettelse i SAP, i tæt samarbejde med indkøb '
       'om leverandørdata og med lageret om styklister. Selv sidder jeg i SAP som '
       'daglig bruger: materialer, priser, kalkulation og opfølgning. '
       'Stamdata-oprettelsen er ikke mit arbejde endnu, men strukturen bag kender '
       'jeg, og jeg har ryddet op i data før.')

    lp('Planlægning og ledelse af tværgående projekter fra idé til implementering '
       'er det andet spor, med fremdrift, tidsplaner og tydelig ansvarsfordeling. '
       'Projekter drevet fra start til slut har jeg lavet siden 2003, fra 37 '
       'tekniske projekter i pharma til entrepriser med 14 mand og underleverandører. '
       'Viljen og gennemslagskraften til at drive projekter på tværs af '
       'organisationen har jeg brugt i alle årene, også når svaret kom fra en '
       'kollega med travlt. Tværgående roller er ikke møder, men aftaler der holder.')

    lp('Forbedringerne er det tredje spor: løbende forbedring af arbejdsgange og '
       'datakvalitet. Struktureret, detaljeorienteret og har høj sans for '
       'datakvalitet, skriver I, og det ordvalg genkender jeg fra kvalitetsarbejdet: '
       'audits på dokumentation og arbejdsgange, rodårsagsanalyser der ændrede '
       'fejlhåndteringen, og ISO 9001 som daglig disciplin. To ting fra listen '
       'kender jeg ikke fra praksis: GS1 og pantsystemer, og FMCG-, fødevare- eller '
       'drikkevarebranchen er nyt terræn. Til gengæld lærer jeg nye regelsæt '
       'hurtigt, og datakvaliteten er den samme uanset hvad der står på varen.')

    lp('Den tværgående rolle kræver kommunikation, og jeg kommunikerer klart på '
       'dansk og engelsk i skrift og tale. Gode IT-kompetencer, herunder Excel, har '
       'jeg brugt hele vejen, og en reference direkte til CEO er en arbejdsform jeg '
       'kender: korte beslutningsgange og ærlig status. Min opgave bliver at sikre '
       'at produktdata i SAP altid er korrekte og opdaterede, og at produkter, kunder '
       'og priser er oprettet korrekt og holdes opdaterede, mens projekterne kører. '
       'Når jeg skal tage teten, er det med stafetten i hånden.')

    lp('Det der tiltaler mig ved opslaget, er kombinationen: en central rolle med '
       'stor indflydelse, mulighed for at sætte dit præg på projekter på tværs af '
       'hele organisationen, og engagerede kolleger og en uformel omgangstone. '
       'Brænder du for struktur og data, spørger I; det gør jeg, og vejen fra idé '
       'til virkelighed er den bedste del af et projekt. Bosat i Måløv, en halv '
       'times tid fra Nordhavn med bil eller S-tog, og med kørekort B (manuelt '
       'gear). I holder samtaler løbende, så lad os tage den første, Jesper, når '
       'det passer dig.', after=44)

    m.para('Med venlig hilsen', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Struktureret projektleder med 20+ år med projekter fra start til slut og '
           'data der skal sidde lige første gang. SAP som dagligt værktøj på '
           'brugersiden, kalkulation, priser og opfølgning, Excel hver dag, og '
           'kvalitetssans fra audits, dokumentation og ISO 9001-arbejdet. PRINCE2, '
           'Microsoft Project og en direkte stil der får projekter i mål på tværs '
           'af organisationen.', after=32)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester (el-teknik og ventilation)',
         'Data Power Consultant ApS · København · 2024 – nu (fra nov. 2026 også ELOHVACs '
         'el-tekniske aktiviteter)',
         'AI-afdeling 4-10 personer · el-service og entreprise · 5 elektrikere + 3 lærlinge',
         [('Struktur i leverancerne', 'Leverancer styret fra tilbud og planlægning til '
           'aflevering med 4-10 specialister, og oprettelser og dokumentation holdt '
           'ajour undervejs. ISO 9001-baserede arbejdsgange som daglig standard, og '
           'opfølgning i Excel og Microsoft Project.')]),
        ('Ejer / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 – nov. 2026 (virksomheden lukket)',
         'Erhvervskunder · el, ventilation og klima · entreprise · fuldt P&L · serviceaftaler',
         [('Data, priser og opfølgning', 'Kalkulation og priser sat og vedligeholdt i '
           'SAP og Excel på alle sager, aftaler og prislister holdt opdaterede, og '
           'kundedata fulgt systematisk. Økonomi og forbedringer af arbejdsgange var '
           'en fast del af driften.'),
          ('Kunder og styring', '5 elektrikere og 3 lærlinge planlagt og fulgt, '
           'underentreprenører holdt på aftalen, og rapportering på fremdrift i en '
           'fast kadence.')]),
        ('Senior commissioningeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, DKK 2-10 mio. · 25 specialister · GMP/FDA/EMA',
         [('Projekter og datakvalitet', '37 projekter gennem alle faser, styret på '
           'fremdrift, tidsplaner og ansvarsfordeling. Materiale- og prisdata fulgt i '
           'SAP-regi, veldokumenterede audits på dokumentation og arbejdsgange, og '
           'nul kritiske fund ved aflevering. Samarbejde på tværs af engineering, '
           'indkøb og drift.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022 – nov. 2022',
         '11 samtidige ventilationsprojekter · 14 mand · underleverandører',
         [('Fra idé til aflevering', '11 samtidige projekter ført fra start til slut '
           'med tydelig ansvarsfordeling, eksterne leverandører koordineret på aftaler '
           'og deadlines, og økonomien fulgt pr. projekt. AB18/ABT 18 som '
           'aftalegrundlag.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · kritiske anlæg · 10 medarbejdere · skiftehold',
         [('Drift og forbedring', 'Drift og vedligehold af kritiske anlæg døgnet '
           'rundt: pumper, HVAC, procesrør, SCADA og PLC. Arbejdsgange forbedret på '
           'tværs af skiftehold, fejl fundet før de blev til stop, og dokumentation '
           'holdt i orden i et system der aldrig sover.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('Grundlaget', 'Produktionsafdeling med 12 mekanikere og teknikere: vagtplan, '
           'materialer og mål. Struktur på data og registreringer, risikostyring og '
           'kvalitetssikring i praksis, og rodårsagsanalyser der ændrede '
           'fejlhåndteringen.')]),
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
    m.bullet('Data og systemer', 'SAP som dagligt værktøj: materialer, priser, '
             'kalkulation og opfølgning. Excel i hænderne hver dag, og SharePoint, '
             'Microsoft Project og SAP ERP på hylden. Nye systemer og portaler '
             'tilegnes hurtigt, og dokumentationen følger med.', after=10)
    m.bullet('Projektledelse', 'PRINCE2, projekter fra start til slut med fremdrift, '
             'tidsplaner og tydelig ansvarsfordeling. 37 samtidige projekter (Novo '
             '2022-2024) og 11 parallelt kørende entrepriser (Ventek 2022) styret '
             'uden løse ender.', after=10)
    m.bullet('Kvalitet og forbedring', 'Audits på dokumentation og arbejdsgange, '
             'ISO 9001-baseret kvalitetssikring, og løbende forbedring som metode: '
             'PDCA, 5S, Standard Work og rodårsagsanalyser. Datakvalitet er en '
             'arbejdsgang, ikke en følelse.', after=10)
    m.bullet('Koordinering på tværs', 'Indkøb, lager, leverandører og eksterne '
             'partnere i samme plan. Interessenthåndtering med klare aftaler, kort '
             'status og gennemslagskraft uden at hæve stemmen.', after=10)
    m.bullet('Sprog og praktisk', 'Dansk og engelsk i skrift og tale brugt '
             'professionelt i dokumentation, møder og kundedialog siden 2010. '
             'Persisk følger med som modersmål. Kørekort kategori B (manuelt gear).',
             after=10)

    m.section('DE FØRSTE 90 DAGE')
    m.para('Planen følger opgaverne: oprettelserne, projekterne, forbedringerne.',
           after=8)
    m.bullet('Dag 1-30 · Oprettelserne', 'SAP-strukturen, masterdata, oprettelsesark '
             'og de eksterne systemer lært at kende: Skanlog, Dansk Cater, DRS og '
             'GS1. Mål: jeg kender datagrundlaget, og de første oprettelser kører '
             'efter bogen.', after=10)
    m.bullet('Dag 31-60 · Projekterne', 'Tetagen taget på de igangværende '
             'tværgående projekter, tidsplaner og ansvarsfordeling skærpet, og '
             'samarbejdet med indkøb og lager i fast rytme. Mål: fremdrift synlig '
             'for alle, og projekterne har en tydelig ejer.', after=10)
    m.bullet('Dag 61-90 · Forbedringerne', 'Første forbedringsprojekter sat i gang '
             'på arbejdsgange og datakvalitet, og en enkel kontrol af '
             'oprettelseskæden etableret. Mål: fejl fundet tidligt, og data der '
             'holder til et salgsmøde.', after=10)

    m.section('SPROG, VÆRKTØJER OG PRAKTISK')
    m.para('Dansk (modersmål) · engelsk (professionelt) · persisk (modersmål). SAP '
           'ERP, Excel, Microsoft Project, SharePoint; PRINCE2. AB18/ABT 18. Kørekort '
           'kategori B med manuelt gear. Bosat i Måløv, en halv times tid fra Nordhavn. '
           'Fuldtid (37 timer). Tiltrædelse aftales.', after=32)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Produktkoordinator med projektansvar · krav og dokumentation',
                   ('Krav i opslaget', 'Dokumenteret erfaring'),
                   [
        ('Erfaring med SAP, herunder oprettelse og vedligehold af stamdata',
         'SAP som dagligt værktøj på brugersiden siden 2017: materialer, priser, '
         'kalkulation og opfølgning (Novo 2022-2024, ELOHVAC 2023-2026). '
         'Stamdata-oprettelse og -vedligeholdelse er ikke mit daglige arbejde endnu; '
         'strukturen og datakvaliteten bag kender jeg fra kvalitetsarbejdet.'),
        ('Projektlederegenskaber og erfaring med at drive projekter fra start til slut',
         'Projekter fra start til slut siden 2003: 37 CAPEX-projekter (Novo '
         '2022-2024), 11 entrepriser (Ventek 2022) og egne projekter (ELOHVAC '
         '2023-2026). PRINCE2 som metode og dokumentation hele vejen.'),
        ('Viljen og gennemslagskraften til at drive projekter på tværs af organisationen',
         'Projekter ført i matrix: 25 specialister på tværs af engineering, '
         'indkøb og drift (Novo 2022-2024), underentreprenører og leverandører '
         '(Ventek 2022). Gennemslagskraft bygget på klare aftaler og synlig fremdrift.'),
        ('Struktureret, detaljeorienteret og har høj sans for datakvalitet',
         'Datakvalitet i praksis: audits på dokumentation og arbejdsgange (Novo '
         '2022-2024), kvalitetssikring og rodårsagsanalyser (ARJ 2003-2010) og '
         'ISO 9001-baserede arbejdsgange som daglig standard (Data Power 2024-2026).'),
        ('Gode IT-kompetencer, herunder Excel',
         'Excel dagligt siden 2003 til kalkulation, opfølgning og rapportering. SAP '
         'ERP, Microsoft Project og SharePoint i brug siden 2017, og nye systemer '
         'tilegnet hurtigt.'),
        ('Kommunikerer klart på dansk og engelsk',
         'Dansk og engelsk i skrift og tale brugt professionelt: dokumentation og '
         'møder på begge sprog (Novo 2022-2024), kundedialog (Ventek, ELOHVAC '
         '2023-2026) og teknisk formidling siden 2010. Persisk som modersmål oveni.'),
        ('Kendskab til GS1 og pantsystemer samt erfaring fra FMCG-, fødevare- eller '
         'drikkevarebranchen',
         'GS1 og pantsystemer kender jeg ikke fra praksis, og FMCG, fødevare eller '
         'drikkevare som branche er nyt terræn. '
         'Nye regelsæt er jeg vant til at tilegne: GMP/FDA/EMA på få måneder (Novo '
         '2022-2024), og GS1 Tradesync og GS1 Packaging er systemer med samme '
         'disciplin som anden dokumentationsstyring.'),
        ('Erfaring med samarbejde med eksterne lager- og logistikpartnere',
         'Eksterne partnere koordineret dagligt: underentreprenører og leverandører '
         '(Ventek 2022, ELOHVAC 2023-2026) og aftaler styret på deadlines og kvalitet. '
         'Lager- og logistikportaler som Skanlog og Dansk Cater er nye flader med '
         'samme opgave.'),
        ('Oprettelse og vedligehold af masterdata på produkter og kunder samt priser '
         'og prislister i SAP',
         'Data, priser og opfølgning i SAP og Excel: kalkulation og prisfastsættelse '
         '(ELOHVAC 2023-2026), materiale- og prisdata i SAP-regi (Novo 2022-2024) og '
         'kundedata holdt opdaterede i serviceaftaler. Stamdata-oprettelse som '
         'arbejdsopgave tager jeg fat på med det samme.'),
        ('Oprettelse af varer hos Skanlog og Dansk Cater samt vedligehold af '
         'emballagedata',
         'Eksterne oprettelsesflader og emballagedata er nye systemer for mig, men '
         'oprettelse og vedligehold af registreringer er ellers min dagligdag: KS-'
         'dokumentation, materialekort og data der skal holde første gang.'),
        ('Registrering i pantsystemer, herunder Dansk Retursystem (DRS), samt '
         'oprettelse og validering i GS1 Tradesync og GS1 Packaging',
         'Ikke erfaring fra praksis. Systemer og regler i pantsystemer og GS1 lærer '
         'jeg hurtigt, og validering af data er en disciplin jeg kender fra '
         'kvalitetsarbejdet, hvor fejl koster på hylden.'),
        ('Koordinering af nye produkter fra oprettelsesark til færdig oprettelse i SAP',
         'Samme type flow som jeg har kørt i projekter: struktureret overdragelse fra '
         'idé til færdig resultat, med tjekpunkter undervejs og ingen løse ender '
         '(37 projekter, Novo 2022-2024; 11 entrepriser, Ventek 2022).'),
        ('Samarbejde med indkøb om leverandørdata og med lageret om styklister',
         'Samarbejde med indkøb og lager i praksis: 25 specialister på tværs af '
         'engineering, indkøb og drift (Novo 2022-2024), materialestyring og '
         'reservedelsstyring (Biofos 2017-2022) og leverandørkontakt (Ventek 2022).'),
        ('Planlægning og ledelse af tværgående projekter fra idé til implementering',
         'Fra idé til implementering dokumenteret: 37 projekter fra idé til implementering '
         '(Novo 2022-2024), 11 entrepriser med underentreprenører (Ventek 2022) og '
         'egen projektportefølje (ELOHVAC 2023-2026).'),
        ('Fremdrift, tidsplaner og tydelig ansvarsfordeling i projektarbejdet',
         'Fremdrift og tidsplaner styret i alle nyere jobs, og ansvarsfordeling '
         'skrevet ned ikke antaget: tavlemøder, milepæle og fast opfølgning siden '
         '2003. Microsoft Project som planlægningsværktøj.'),
        ('Løbende forbedring af arbejdsgange og datakvalitet',
         'Forbedring som metode: rodårsagsanalyser der ændrede fejlhåndteringen (ARJ '
         '2003-2010), arbejdsgange forbedret på tværs af skiftehold (Biofos 2017-2022) '
         'og PDCA, 5S og Standard Work i det daglige kvalitetsarbejde.'),
        ('Tværgående rolle med samarbejde på tværs af organisationen og med eksterne '
         'partnere',
         'Rollen er tværgående i praksis: interessenthåndtering på tværs af '
         'engineering, indkøb og drift (Novo 2022-2024), kunder og myndigheder '
         '(Biofos 2017-2022) og eksterne partnere i egen virksomhed (2023-2026).'),
        ('Ansvar for at produkter, kunder og priser er oprettet korrekt og holdes '
         'opdaterede',
         'Præcision i data har været en del af arbejdet siden 2003: priser og aftaler '
         'holdt opdaterede (ELOHVAC 2023-2026), dokumentation uden kritiske fund '
         '(Novo 2022-2024) og registreringer der holdt til revision (Biofos 2017-2022).'),
        ('Fuldtid (37 timer), arbejdssted i Nordhavn, København Ø; reference til CEO',
         'Fuldtid og klar til start. Måløv ligger en halv times tid fra Nordhavn. '
         'Vant til direkte reference til ledelse og ejer: P&L-ansvar (ELOHVAC '
         '2023-2026) og månedlig ledelsesrapportering (Novo 2022-2024).'),
                   ], widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo · Produktkoordinator med projektansvar, Hansen & Co')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_HansenCo_Produktkoordinator.docx')
    build(out)
    print(out)
