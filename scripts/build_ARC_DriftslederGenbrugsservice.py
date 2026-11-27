#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Driftsleder til Genbrugsservice — ARC (Amager Ressourcecenter), København.

Dansk opslag -> DANSK dokument (4 sider). TEMPLATE Gentofte-2027.
ARC = nyt firma. To stillinger; konkret ansvarsområde aftales i rekrutteringen.
Kontakt: genbrugschef Marcus Müller, 51371501. Frist 10. december 2026.
37 timer/uge + rådighedsvagter. Løn efter gældende overenskomst og aftaler i ARC.

BRUGERSVAR (bindende):
1. Kommunesamarbejde = REEL -> selvsikkert (kanonisk belæg: Biofos er kommunejet
   forsyningsselskab; offentlige ejere/samarbejdspartnere i driften siden 2017).
   Ingen opdigtede kommunenavne/perioder ud over kanon.
2. Lokation (nærgenbrugsstationer i København) = commute_ok -> konkret.

STIL (3/3 mod #446 NOVENCO): register "Synlig ledelse, fælles retning",
åbning BW (omstillingen på gadeplan), struktur "Nærvær, aftaler, overblik".
H4-læring (§277): adjektivstakke brydes OGSÅ i kulturfraser -> 'stabil,
effektiv og sikker drift' erstattes af 'effektiv og sikker drift året rundt'.
Ingen em dash. "elautoriseret maskinmester" i CV-titler som kanonisk.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_Gentofte_DriftslederEjendomme_2027.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'ARC · Driftsleder til Genbrugsservice · København'
BANNER_RESUME = 'DRIFTSLEDELSE · SERVICE · ARBEJDSMILJØ · SAMARBEJDE'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('1. december 2026')
    m.meta('ARC · Genbrugsservice · København')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning om stillingen som driftsleder til Genbrugsservice',
           bold=True, color='1A1A1A')
    m.para('Kære Marcus Müller,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('En af de københavnske nærgenbrugsstationer er stedet, hvor den grønne omstilling bliver til '
       'hverdag. Stationerne drives og udvikles i tæt samarbejde med '
       'Københavns Kommune, og her kan københavnerne aflevere ting, andre '
       'kan få glæde af, '
       'deltage i workshops og lokale aktiviteter om genbrug. Formålet er at '
       'gøre genbrug til en større del af københavnernes hverdag, og det '
       'mærkes i den daglige drift. Bag den oplevelse står engagerede genbrugsvejledere, og bag '
       'dem en drift, der skal holde med høje krav til service, arbejdsmiljø '
       'og sikker drift. At udvikle borgernes muligheder for genbrug er '
       'samtidig den grønne omstilling på gadeplan.')

    lp('Stillingerne som driftsleder i Genbrugsservice hviler, som I skriver, '
       'på god personaleledelse og evnen til at få samarbejdet til at fungere, '
       'og det er præcis kernen i det, jeg kan. Rollen er synlig i hverdagen '
       'og tæt på genbrugsvejledernes arbejde, og opgaven lyder som der står: '
       'sætter en tydelig retning, inddrager medarbejderne i løsningerne og '
       'følger op på det, I aftaler. På alle sider fylder samarbejdet: '
       'medarbejdere, lederkolleger, administrativ driftssupport og vores '
       'ejerkommuner, og udvikle medarbejdernes faglighed og skabe et godt '
       'arbejdsmiljø er en del af stillingen, ikke et ekstra lag.')

    lp('Personaleledelse, fx fra en drifts- eller serviceorganisation, har '
       'været mit håndværk siden 2003: skiftehold i en forsyning under '
       'offentligt ejerskab, montagehold på byggepladser og servicehold med '
       'ansvar for kundernes anlæg. Jeg lytter til kommunernes behov, bringer '
       'erfaringerne fra driften ind i dialogen og afstemmer forventninger, '
       'og når aftalen er på plads, bliver den omsat til klare opgaver og '
       'fulgt til dørs. Det er en disciplin, jeg kender fra arbejdet med '
       'offentlige ejere og kommunale samarbejdspartnere, hvor driften skulle '
       'levere det, der blev aftalt, hver gang.')

    lp('De første 90 dage har tre navne. Første måned er nærværet: '
       'arbejdsstederne gennemgået, medarbejderne lyttet til, og hverdagen '
       'oplevet fra begge sider af skranken, før noget ændres. Næste fase er '
       'aftalerne: ejerkommunernes behov afstemt, forventninger gjort '
       'konkrete, og samarbejdet om drift og udvikling sat i en fast rytme '
       'med opfølgning på fælles aftaler. Sidste fase er overblikket: '
       'stabil og effektiv drift året rundt, med vagt- og ferieplanlægning og '
       'opfølgning på arbejdsmiljø og service på plads, budget og regnskab på '
       'dit område, som der står, gennemgået, og økonomiopfølgning som en '
       'naturlig del af ledelsen.')

    lp('Ledelseslinjen fra opslaget, at man skaber tillid ved at være '
       'tilgængelig og tydelig i din ledelse, er sådan jeg selv har ledet: '
       'jeg lytter, giver brugbar sparring og tager ansvar for de '
       'beslutninger, der skal træffes. At samle mennesker med forskellige '
       'fagligheder og interesser om en løsning, der fungerer i praksis, er '
       'det, jeg er bedst til, og en travl dag på en station ændrer ikke på '
       'tonen. Næste linje i opslaget passer også: arbejder struktureret, '
       'kan prioritere mellem den daglige drift og udviklingsopgaverne, og '
       'min interesse for den grønne '
       'omstilling, genbrug og affaldsområdet er reel nok til, at søgningen '
       'kom af sig selv.')

    lp('Første linje i opslaget passer på mig: kørekort til kategori B og '
       'kan bevæge dig mellem arbejdsstederne, og 37 timer om ugen med '
       'rådighedsvagter kender jeg '
       'fra driften, hvor vagtplanen ikke altid spørger, om det passer. Et '
       'Et selvstændigt lederjob med en varieret hverdag tæt på medarbejderne '
       'og mulighed for at præge udviklingen af dit område, som der står, er '
       'præcis det, jeg '
       'søger, og faglig sparring, en uformel omgangstone og på at hjælpe '
       'hinanden på tværs er sådan et lederteam skal være. Løn og '
       'ansættelsesvilkår følger gældende overenskomst og aftaler i ARC, og '
       'tiltrædelse efter aftale passer. København fungerer nemt fra Måløv. '
       'Jeg ser frem til at høre fra dig.', after=44)

    m.para('Med venlig hilsen', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Driftsleder med 20+ år i personaleledelse, service og sikker '
           'drift, fra skiftehold i en kommunejet forsyning til servicehold '
           'med kunder og aftaler. Tillid bygget ved at være synlig og '
           'tilgængelig, budget og regnskab ført som en del af ledelsen, og '
           'samarbejde med offentlige ejere og kommunale samarbejdspartnere '
           'som en fast disciplin. Trivsel og arbejdsmiljø følger med, også '
           'når der er travlt.', after=32)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester (el-teknik og ventilation)',
         'Data Power Consultant ApS · København · 2024 – nu (fra nov. 2026 også ELOHVACs '
         'el-tekniske aktiviteter)',
         'AI-afdeling 4-10 personer · el-service og entreprise · 5 elektrikere + 3 lærlinge',
         [('Ledelse på tværs', 'Teams på 4-10 specialister ledet med tydelig '
           'retning og opfølgning, og opgaver fordelt på tværs af '
           'arbejdssteder. Trivsel og faglighed fulgt i samme rytme som '
           'fremdriften, og aftaler med kunder og leverandører holdt i '
           'orden.')]),
        ('Ejer / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 – nov. 2026 (virksomheden lukket)',
         'Erhvervskunder · el, ventilation og klima · entreprise · fuldt P&L · serviceaftaler',
         [('Service, økonomi og aftaler', 'Personaleledelse af 5 elektrikere '
           'og 3 lærlinge med vagtplanlægning og daglig koordinering, '
           'budget og regnskab ført måned for måned, og serviceaftaler '
           'forventningsafstemt med kunderne og fulgt til dørs. Arbejdsmiljø '
           'og sikkerhed håndteret på hver enkelt opgave.')]),
        ('Senior commissioningeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, DKK 2-10 mio. · 25 specialister · GMP/FDA/EMA',
         [('Faglighed og koordinering', '25 specialister og leverandører '
           'koordineret på tværs af mange arbejdssteder, med fagligheden i '
           'højsædet og dokumentation, der holdt til revision. Aftaler med '
           'bygherrer og rådgivere afstemt, før arbejdet gik i gang.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022 – nov. 2022',
         '11 projekter · 14 mand · underleverandører · montage og aflevering',
         [('Mennesker i fremdrift', '14 mand og underleverandører planlagt '
           'uge for uge på tværs af 11 arbejdssteder, med ferieplanlægning '
           'og ressourcer holdt i balance. Samarbejdet med bygherrer og '
           'kolleger bar projekterne, når planerne ændrede sig.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · kritiske anlæg · 10 medarbejdere · skiftehold · kommunejet forsyning',
         [('Drift med offentlige ejere', 'Driftsledelse i en kommunejet '
           'forsyning: 10 medarbejdere på skiftehold, vagtplaner der holdt '
           'året rundt, og arbejdsmiljø og sikkerhed fulgt tæt i en drift '
           'uden lukkedage. På ejersiden blev aftaler og forventninger '
           'afstemt i hverdagen, ikke et møde i ny og næ.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('Første ledelsesår', 'Personaleledelse af 12 mekanikere og '
           'teknikere, daglig koordinering og oplæring, og et arbejdsmiljø '
           'hvor alle hjalp hinanden, når det spidsede til. Her lærte jeg, '
           'at synlighed i hverdagen er selve ledelsen.')]),
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
    m.bullet('Personaleledelse og trivsel', 'Personaleledelse siden 2003 med '
             'trivsel, faglighed og samarbejde som kernen. Tydelig retning, '
             'medarbejdere inddraget i løsningerne, og opfølgning på det, der '
             'aftales. Faglig udvikling fulgt op, også i travle perioder.',
             after=10)
    m.bullet('Drift og arbejdsmiljø', 'Stabil og sikker drift året rundt med '
             'vagtplanlægning, ferieplanlægning og opfølgning på '
             'arbejdsmiljø og service som faste discipliner. Erfaring fra '
             'drift uden lukkedage, og fra steder med mange brugere og '
             'høje krav.', after=10)
    m.bullet('Samarbejde og aftaler', 'Ejerkommuner og offentlige '
             'samarbejdspartnere mødt med lydhørhed og klare forventninger: '
             'behov lyttet til, aftaler omsat til klare opgaver og fulgt til '
             'dørs. Kundedialog og bygherresamarbejde i samme ånd.', after=10)
    m.bullet('Økonomi og overblik', 'Budget og regnskab ført som en del af '
             'ledelsen, med økonomiopfølgning måned for måned og prioritering '
             'mellem daglig drift og udviklingsopgaver. Struktur i overblikket '
             'uden stivhed i hverdagen.', after=10)

    m.section('DE FØRSTE 90 DAGE')
    m.para('Planen følger opgaven: nærværet, aftalerne, overblikket.', after=8)
    m.bullet('Dag 1-30 · Nærværet', 'Arbejdsstederne gennemgået, '
             'medarbejderne lyttet til, og hverdagen oplevet fra begge sider. '
             'Mål: jeg kender menneskerne og stederne, før der ændres på '
             'noget.', after=10)
    m.bullet('Dag 31-60 · Aftalerne', 'Ejerkommunernes behov afstemt, '
             'forventninger gjort konkrete, og samarbejdet om drift og '
             'udvikling sat i fast rytme. Mål: aftaler, der kan følges op '
             'uden fortolkningsrum.', after=10)
    m.bullet('Dag 61-90 · Overblikket', 'Vagtplanlægning, arbejdsmiljø og '
             'økonomiopfølgning på plads, og budget og regnskab gennemgået '
             'for området. Mål: en drift, der kører, også når jeg ikke står '
             'lige der.', after=10)

    m.section('SPROG, VÆRKTØJER OG PRAKTISK')
    m.para('Dansk (modersmål) · engelsk (professionelt) · persisk (modersmål). '
           'SAP, Excel, CMMS; PRINCE2. Kørekort kategori B (manuelt gear) og '
           'vant til at bevæge mig mellem arbejdssteder. Bosat i Måløv; '
           'København fungerer nemt derfra.', after=8)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Krav og dokumentation · Driftsleder, Genbrugsservice, ARC',
                   ('Krav i opslaget', 'Dokumentation'),
                   [
        ('Erfaring med personaleledelse, fx fra en drifts- eller '
         'serviceorganisation',
         'Personaleledelse siden 2003, netop fra drifts- og '
         'serviceorganisationer: 12 mekanikere (ARJ 2003-2010), 10 '
         'medarbejdere på skiftehold i døgndrift (Biofos 2017-2022), 14 mand '
         'på montage (Ventek 2022) og 5 elektrikere og 3 lærlinge i '
         'service (ELOHVAC 2023-2026).'),
        ('Samarbejde med ejerkommunerne om drift og udvikling med opfølgning '
         'på fælles aftaler',
         'At samarbejde med offentlige ejere er erfaring, ikke teori: Biofos '
         '(2017-2022) er en kommunejet forsyning, hvor driften løbende blev '
         'afstemt med ejere og kommunale interessenter. Erfaringerne fra '
         'driften blev bragt ind i dialogen, og aftaler fulgt op på samme '
         'måde som med kunder og bygherrer i entreprise.'),
        ('Lede og udvikle medarbejdere og styrke trivsel, faglighed og '
         'samarbejde på tværs af arbejdsstederne',
         'Ledelse og udvikling af medarbejdere på tværs af arbejdssteder: '
         'skiftehold, montagehold og servicehold, med trivsel, faglighed og '
         'samarbejde fulgt lige så systematisk som økonomien. Oplæring og '
         '1:1-samtaler har været en del af rytmen siden 2003.'),
        ('Stabil og effektiv drift året rundt med vagt- og ferieplanlægning '
         'samt opfølgning på arbejdsmiljø og service',
         'Effektiv og sikker drift året rundt er hverdagen fra Biofos: '
         'vagtplanlægning og ferieplanlægning for 10 medarbejdere på '
         'skiftehold, arbejdsmiljø og sikkerhed fulgt tæt (LOTO, APV, '
         'risikovurdering), og service målt på, om anlægget kørte, når det '
         'skulle.'),
        ('Budget og regnskab på området og opfølgning på økonomien',
         'Budget og regnskab ført som en del af ledelsen: fuldt P&L-ansvar '
         '(ELOHVAC 2023-2026) med månedlig økonomiopfølgning, '
         'omkostningsstyring i drift (Biofos) og budgetansvar på '
         'projekter. Tallene er et ledelsesværktøj, ikke en rapport.'),
        ('Udvikle borgernes muligheder for genbrug med medarbejdere, kolleger '
         'og kommunale samarbejdspartnere',
         'Udvikling af borgernes muligheder er den grønne omstilling i '
         'praksis, og den type opgaver kender jeg fra arbejdet med '
         'energioptimering og bæredygtige løsninger i eksisterende anlæg '
         '(ELOHVAC, Biofos), altid udviklet sammen med medarbejdere og '
         'samarbejdspartnere frem for på skrivebordet.'),
        ('Synlig i hverdagen og tæt på medarbejdernes arbejde',
         'Synlighed i hverdagen er min ledelsesform: fra værkstedsgulvet i '
         'Teheran til vagtgangen på Lynetten har jeg været tæt på det '
         'praktiske arbejde, og medarbejderne vidste, hvor de kunne finde '
         'mig. Tillid bygges på nærhed, ikke på mails.'),
        ('Sætte tydelig retning, inddrage medarbejderne og følge op',
         'Tydelig retning med inddragelse og opfølgning er arbejdsformen: '
         'aftaler indgået i fællesskab, beslutninger kommunikeret klart, og '
         'opfølgning på det, der blev aftalt, også når hverdagen pressede på. '
         'Det gælder både på skiftehold og i projekter.'),
        ('Udvikle medarbejdernes faglighed og skabe et godt arbejdsmiljø, '
         'også under travlhed',
         'Faglighed og arbejdsmiljø udviklet sideløbende: struktureret '
         'oplæring af lærlinge og nye medarbejdere (ELOHVAC, ARJ), '
         'arbejdsmiljøopfølgning og sikkerhedsrunder i drift (Biofos), og et '
         'miljø hvor faglig sparring var en del af jobbet, ikke et kursus.'),
        ('Lytte til kommunernes behov, bringe driftserfaring ind i dialogen '
         'og afstemme forventninger',
         'At lytte til den anden side af bordet og bringe driftserfaring ind '
         'i dialogen har været metoden i aftaler med kunder, bygherrer og '
         'offentlige ejere: behov afdækket, realiteterne fra driften lagt '
         'frem, og forventninger afstemt før aftalen, ikke efter.'),
        ('Aftaler omsat til klare opgaver og fulgt til dørs',
         'Aftaler omsat til klare opgaver og fulgt til dørs gennem hele '
         'karrieren: serviceaftaler specificeret i besøg og responstider '
         '(ELOHVAC), entreprisekontrakter fulgt på udførelse (Ventek), og '
         'fælles aftaler i drift fulgt op i faste møder (Biofos).'),
        ('Skabe tillid ved at være tilgængelig og tydelig i ledelsen',
         'Tillid skabt ved tilgængelighed og tydelighed: åben dør, klare '
         'beslutninger og ord, der holder. Medarbejdere, kunder og '
         'samarbejdspartnere har vidst, hvor de havde mig, også når svaret '
         'ikke var det, de håbede på.'),
        ('Lytte, give brugbar sparring og tage ansvar for beslutninger',
         'Sparring og ansvar følges ad i min ledelse: lyttende i 1:1 og på '
         'gulvet, brugbar sparring på det konkrete arbejde, og ansvar taget '
         'for beslutninger, når de skulle træffes. Tolv år som underviser '
         'har finpudset evnen til at gøre komplekst forståeligt.'),
        ('Samle mennesker med forskellige fagligheder og interesser om '
         'løsninger, der fungerer i praksis',
         'At samle forskellige fagligheder om en fælles løsning er kernen i '
         'tværfaglige hold: elektrikere, mekanikere, montører, specialister '
         'og administrative funktioner samlet om samme opgave, fra 37 '
         'CAPEX-projekter til serviceaftaler på tværs af fag.'),
        ('Arbejde struktureret og prioritere mellem daglig drift og '
         'udviklingsopgaver',
         'Struktur og prioritering mellem drift og udvikling er en øvelse, '
         'jeg kender godt: drift der kører døgnet rundt sideløbende med '
         'udviklingsopgaver som energioptimering og nye arbejdsgange. '
         'Prioriteringerne er synlige, så alle ved, hvad der venter.'),
        ('Interesse for den grønne omstilling, genbrug og affaldsområdet',
         'Interessen for den grønne omstilling, genbrug og affaldsområdet er '
         'reel: fire år i en forsyning med miljøet som kerneopgave (Biofos), '
         'energioptimering i eksisterende anlæg som fast disciplin (ELOHVAC), '
         'og genbrug som naturlig tankegang fra et fag, hvor ting repareres '
         'før de kasseres.'),
        ('Kørekort til kategori B og kan bevæge sig mellem arbejdsstederne',
         'Kørekort kategori B (manuelt gear) i orden, og vant til at bevæge '
         'mig mellem arbejdssteder: byggepladser i Storkøbenhavn, stationer '
         'og anlæg fordelt på flere lokationer, og kundebesøg i hele '
         'hovedstadsområdet.'),
        ('37 timer om ugen med rådighedsvagter',
         '37 timer om ugen med rådighedsvagter passer til den rytme, jeg '
         'kender: skiftehold og vagtordninger i døgndrift (Biofos 2017-2022), '
         'hvor tilgængelighed var en del af aftalen. Jeg er vant til, at '
         'driften ikke følger kontortiden.'),
                   ],
                   widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo — Ansøgning og CV — Driftsleder, '
                       'Genbrugsservice, ARC')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_ARC_DriftslederGenbrugsservice.docx')
    build(out)
    print(out)
