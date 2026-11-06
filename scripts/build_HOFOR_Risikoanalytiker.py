# -*- coding: utf-8 -*-
"""HOFOR — Risikoanalytiker til HOFORs kritiske vandinfrastruktur.

HOFOR beder om et *motiveret CV* (ikke en ansøgning): motiveret forside,
CV side 2–3, 90 dage + afsnit side 4.
Policy: master/README.md — ekstrem sikkerhed, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Risikoanalyse · Kritisk infrastruktur · Beslutningsgrundlag'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('6. november 2026')
    m.meta('HOFOR · Vand Analyse · Sektionen Vand Data & Aktiver · Risikoanalytiker')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Motiveret CV: Risikoanalytiker til kritisk vandinfrastruktur', bold=True, color='1A1A1A')
    m.para('Til Mohamad Hammoud, sektionen Vand Data & Aktiver og direktørområdet Vand & Byudvikling', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('En risiko er ikke et tal i et regneark, før nogen har besluttet, hvad der skal ske, hvis den indtræffer. '
           'Det er den erfaring, jeg tager med fra otte år i drift og projekter på kritisk infrastruktur: en '
           'sandsynlighed er kun interessant, når den er koblet til en konsekvens — en pumpestation i vandforsyningen, '
           'der ikke kan levere, et renseanlæg for spildevand, der skal tages ud af drift, en el-tavle der svigter i et kritisk øjeblik — og til '
           'en beslutning om, hvad vi gør ved det, og hvem der ejer handlingen.', after=80)

    m.para('**Det, jeg kan bidrage med, er risikostyring set fra den side, hvor risikoen bliver til virkelighed.** '
           'Hos **Novo Nordisk** var risiko ikke en dokumentformular, men en fast del af leverancen i **37 '
           'kapitalprojekter** med 2–10 mio. kr. pr. projekt: kravsspecifikation, risikovurdering af kritiske '
           'funktioner, **FAT/SAT og IQ/OQ/PQ**, og **månedlig rapportering af fremdrift, økonomi og risiko** til '
           'ledelse og bygherre. Det endte med **nul kritiske fund** ved aflevering — ikke fordi der ikke var '
           'risici, men fordi de var fundet, beskrevet og håndteret, før de blev til afvigelser.', after=80)

    m.para('På **Lynetten under Biofos** var opgaven at holde et kritisk spildevandsanlæg kørende i 24/7-drift, og '
           'der var risikobilledet konkret: hvilke anlægsdele kan vi ikke undvære, hvad sker der, hvis en pumpe '
           'eller en blæser falder ud, hvor langt er vi fra at måtte lede vandet uden om, og hvad koster det at '
           'have '
           'reservedelen liggende kontra at stå uden. Vi arbejdede med **kritikalitet, sandsynlighed og '
           'konsekvens**, med et risikoregister, der havde en ejer og en dato, og med **energiledelse og '
           'driftsoptimering**, der gav **over 40 % lavere forbrug** — et resultat, der kom af at måle, prioritere '
           'og flytte indsatsen derhen, hvor den betød mest for forsyningssikkerheden.', after=80)

    m.para('**Facilitering er den del af rollen, jeg har mest af.** En risikoanalyse bliver kun brugt, hvis de '
           'rigtige interessenter har siddet i rummet og er blevet enige om, hvad der er usikkert. Jeg har drevet '
           'tværfaglige processer med teknikere, specialister, projektledere, leverandører og ledelse: '
           '**FAT/SAT**-gennemgange i samarbejde med leverandører, tavlemøder i døgndrift, **APV** og sikkerhedsrunder sammen '
           'med arbejdsmiljøgruppen, og den månedlige gennemgang i 37 projekter, hvor nogen skulle fortælle '
           'ledelsen, at en dato ikke holdt. Jeg er vant til at være den, der stiller spørgsmålet \"hvad hvis\", '
           'og som bagefter skriver det ned, så det kan besluttes.', after=80)

    m.para('**Metode og værktøjer.** Jeg arbejder systematisk: risici identificeret, vurderet på sandsynlighed og '
           'konsekvens, prioriteret og lagt i et register med **ejer, handling og frist** — og fulgt op, til '
           'handlingen er lukket. Jeg bygger selv de kvantitative modeller, opgaven kræver, i **Python, Excel og '
           'Power Query**: scenarier, følsomheder, fremskrivninger og dashboards, hvor antagelserne står tydeligt '
           'sammen med tallet. Det er den samme tilgang, jeg brugte til at prissætte risiko i egne kontrakter og '
           'til at beregne, hvor mange opgaver en bemanding reelt kan bære.', after=80)

    m.para('**Kritikalitet har jeg prøvet at lave sammen med dem, der kender anlægget.** På Lynetten sad '
           'teknikerne med ved bordet, da vi gennemgik anlægsdelene: hvad kan vi undvære, hvad kan vi køre uden om, '
           'og hvad står stille, hvis den her falder ud en fredag eftermiddag. Det gav en liste, der var kortere end '
           'den, jeg selv ville have skrevet, og mere præcis — og den blev brugt, fordi de selv havde lavet den. '
           'Den slags gennemgange er kernen i den rolle, I søger: metoden skal være fælles, men viden om '
           'konsekvensen sidder ude på anlæggene.', after=80)

    m.para('**Hvorfor Vand Analyse.** Fordi opgaven er at gøre noget fælles: en ensartet og systematisk tilgang til '
           'risikostyring på tværs af anlæg, forsyninger og projekter, i en ny sektion hvor måden at arbejde '
           'sammen stadig bliver formet. Det er præcis den slags opgave, jeg har løst før — ikke ved at indføre et '
           'system ovenfra, men ved at lave metoden sammen med dem, der skal bruge den, og ved at gøre den så '
           'enkel, at den bliver brugt i en travl hverdag. Og fordi forsyningssikkerhed i hovedstaden er en '
           'samfundsopgave, hvor et kvalificeret beslutningsgrundlag er hele forskellen.', after=80)

    m.para('**Hvad jeg vil måles på efter det første år:** at der ligger én fælles metode, som anlæg og projekter '
           'faktisk bruger; at risikoanalyserne bliver leveret til tiden og med anbefalinger, der bliver besluttet '
           'på; at usikkerheder står tydeligt i beslutningsgrundlaget i stedet for at blive glattet ud; og at '
           'risikoregistret bliver fulgt op, så handlinger bliver lukket og ikke bare beskrevet.', after=80)

    m.para('Praktisk: jeg bor i Måløv, arbejder gerne hybridt efter aftale og kan være på anlæggene, når analysen '
           'kræver det. Jeg kommunikerer tydeligt på dansk, både mundtligt og skriftligt, og kan starte efter '
           'aftale. Jeg vil gerne høre, hvor I er med den fælles metode, og hvilke analyser der haster mest — det '
           'er der, jeg ville begynde.', after=70)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Drifts- og projektleder med 20+ års erfaring fra **kritisk infrastruktur og teknisk tunge anlæg** — '
           '**elautoriseret maskinmester (LV/MV/HV)** med B.Tech i teknologiledelse og maskinteknik. Otte år med '
           '**risikovurderinger som en fast del af drifts- og projektansvaret**: fem år som drifts- og '
           'vedligeholdelsesleder på et spildevandsanlæg i 24/7-drift med kritikalitetsvurdering, risikoregister '
           'og forsyningssikkerhed, og to år som projektleder på **37 kapitalprojekter** med risikostyring, '
           'FAT/SAT og **månedlig risikorapportering** til ledelse og bygherre — **nul kritiske fund** ved '
           'aflevering. Driver siden 2023 egen el-teknisk virksomhed med fuldt P&L, hvor risiko bliver prissat i '
           'kontrakter og modelleret i **Python og Excel**. Vant til at **facilitere tværfaglige processer** og '
           'omsætte komplekse risikobilleder til beslutningsgrundlag for ledelsen.', after=80)

    m.section('RISIKO, ANALYSE OG BESLUTNINGSGRUNDLAG')
    for label, body in [
        ('Risikoanalyse og kritikalitet',
         'Kritikalitetsvurdering af anlægsdele og funktioner i døgndrift; risici vurderet på sandsynlighed og '
         'konsekvens, prioriteret og lagt i register med ejer, handling og frist — og fulgt op til lukning.'),
        ('Risikostyring i projekter',
         'Risikovurdering af kritiske funktioner i 37 kapitalprojekter med 2–10 mio. kr. pr. projekt; FAT/SAT og '
         'IQ/OQ/PQ som kontrolpunkter; månedlig risikorapportering til ledelse og bygherre og nul kritiske fund.'),
        ('Facilitering af tværfaglige processer',
         'Workshops med teknikere, specialister, projektledere og leverandører; tavlemøder i døgndrift; APV og '
         'sikkerhedsrunder med arbejdsmiljøgruppen; beslutninger dokumenteret med ejer og dato.'),
        ('Kvantitative modeller og data',
         'Scenarier, følsomheder og fremskrivninger i Python, Excel og Power Query; dashboards og KPI-tavler '
         'hvor antagelser og usikkerhed står sammen med tallet.'),
        ('Forsyningssikkerhed og kritisk infrastruktur',
         'Kritisk spildevandsanlæg i 24/7-drift med vagtordning og beredskab; prioritering af indsats efter '
         'konsekvens for forsyningen og dokumenteret energiledelse med over 40 % lavere forbrug.'),
        ('Beslutningsgrundlag til ledelsen',
         'Månedlig skriftlig rapportering af fremdrift, økonomi og risiko; anbefalinger med alternativer, '
         'konsekvens og pris — skrevet så en direktionsmedlem kan beslutte på to sider.')]:
        m.bullet(label, body, after=25)

    m.models_table('METODER OG VÆRKTØJER', ('Område', 'Dokumenteret brug'), [
        ('Risikometode',
         'Identifikation, sandsynlighed og konsekvens, risikomatrice, prioritering af risikoreducerende tiltag og '
         'opfølgning på effekt.'),
        ('Risikoregister',
         'Én liste pr. anlæg og projekt med ejer, handling, frist og status; gennemgået på fast kadence med dem, '
         'der ejer handlingerne.'),
        ('Kvantitativ analyse',
         'Scenariemodeller, følsomhedsanalyse og fremskrivning i Python og Excel; tal, der kan reproduceres og '
         'forsvares, når nogen spørger.'),
        ('Facilitering',
         'Workshop-design, mødeledelse og beslutningsreferat; tværfaglige gennemgange med leverandører, '
         'driftsorganisation og ledelse.'),
        ('Dokumentation og krav',
         'Kravsspecifikation, afvigelseshåndtering og sporbarhed fra GMP-miljø (FDA/EMA) og fra '
         'kvalitetsstyring på anlæg.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · el-autorisation · el-tekniske service- og entrepriseydelser',
         [('Risiko i kontrakter og kalkulation',
           'Risiko prissat i aftaler og tilbud: hvad koster en responstid, hvad koster det at tage chancen, og '
           'hvor går grænsen; modeller i Python og Excel til kalkulation og kapacitet; beslutninger truffet på '
           'tal frem for mavefornemmelse.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Risikostyring, leverandører og aflevering',
           'Risikovurdering af kritiske funktioner, kravsspecifikation, FAT/SAT og IQ/OQ/PQ; risici, fremdrift og '
           'økonomi rapporteret månedligt til ledelse og bygherre; nul kritiske fund ved aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter · 2–10 mio. kr. pr. opgave',
         [('Kapacitet, flaskehalse og konsekvens',
           'Kapacitets- og flaskehalsanalyse på 11 samtidige projekter, omprioritering samme dag når en maskine '
           'eller et menneske faldt væk, og dagligt tavlemøde hvor afvigelser blev besluttet og fulgt op.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Lynetten under Biofos · København · aug. 2017–jan. 2022',
         'Kritisk spildevandsanlæg i 24/7-drift · SRO/SCADA · pumper, blæsere, ventilation, transformere, '
         'koblingsanlæg',
         [('Kritikalitet, beredskab og forsyningssikkerhed',
           'Kritikalitetsvurdering af anlægsdele, vedligeholdsplaner, reservedelsbehov og eksterne montører i '
           'døgndrift; vagtordning og beredskab planlagt og prøvet; risikoregister fulgt til lukning; energiledelse '
           'med over 40 % lavere forbrug.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · industrielt udstyr',
         [('Teknisk analyse og fejlfinding',
           'Fejlfinding og årsagsanalyse på industrielt udstyr; vagtplanlægning, oplæring og opfølgning på mål for '
           '12 teknikere.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('UDDANNELSE OG AUTORISATION')
    m.edu('B.Tech, teknologiledelse og maskinteknik',
          'Maskinmesterskolen København · 2017–2022 · gennemsnit 7,6/12')
    m.edu('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('El- og maskinteknisk konstruktion, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Køle- og ventilationsteknik · STCW', 'Mercantec 2021 · Søfartsstyrelsen 2021')

    m.section('SPROG, PRAKTIK OG REFERENCER')
    m.para('Dansk: modersmål, sikkert både mundtligt og skriftligt · Engelsk: professionelt, også teknisk · '
           'Persisk: modersmål · **Kørekort B og egen bil** · Måløv, tæt på anlæggene · Hybrid og hjemmearbejde '
           'efter aftale · Kan starte efter aftale · Referencer på forespørgsel.', after=70)

    m.models_table('DET DE EFTERSPØRGER — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Erfaring med risikostyring fra en teknisk eller infrastrukturtung organisation',
         'Otte år med risikovurdering i drift og projekter: fem år på kritisk spildevandsanlæg i døgndrift og to år '
         'med 37 kapitalprojekter i en GMP-organisation — nul kritiske fund ved aflevering.'),
        ('Mindst tre års relevant erhvervserfaring med risikoanalyser og risikovurderinger',
         'Kritikalitets- og risikovurdering som fast del af driftsansvaret 2017–2022 og af projektansvaret '
         '2022–2024; risikoregister med ejer og frist, prioritering af risikoreducerende tiltag og opfølgning på '
         'effekt.'),
        ('Relevant videregående uddannelse, fx ingeniør, økonom eller anden teknisk eller analytisk uddannelse',
         'B.Tech i teknologiledelse og maskinteknik med analyse, økonomi og projektledelse (7,6/12); elautoriseret '
         'maskinmester (LV/MV/HV); el- og maskinteknisk konstruktion.'),
        ('Erfaring med at drive og facilitere tværfaglige processer',
         'Workshops og gennemgange med teknikere, specialister, projektledere, leverandører og ledelse; FAT/SAT og '
         'IQ/OQ/PQ i 37 projekter; APV og sikkerhedsrunder med arbejdsmiljøgruppen; daglige tavlemøder i '
         'døgndrift.'),
        ('Kan omsætte analyser og data til klare anbefalinger og beslutningsgrundlag',
         'Månedlig rapportering af fremdrift, økonomi og risiko til ledelse og bygherre; anbefalinger med '
         'alternativer, konsekvens og pris; modeller i Python og Excel hvor antagelserne står ved tallet.'),
        ('Forståelse for forsyningssikkerhed og kritisk infrastruktur',
         'Fem år på et kritisk spildevandsanlæg i 24/7-drift med beredskab og vagtordning; prioritering efter '
         'konsekvens for forsyningen og dokumenteret energiledelse med over 40 % lavere forbrug.'),
        ('Erfaring med at opstille simple, kvantitative risikomodeller',
         'Scenarier, følsomheder og fremskrivninger i Python, Excel og Power Query til kalkulation, kapacitet og '
         'prissætning af risiko; modeller bygget, så de kan forklares og reproduceres af andre.'),
        ('Systematisk, metodisk og facilitator — mønstre og afhængigheder',
         'Standard work, 5S og PDCA indført i døgndrift; afvigelser og nærvedhændelser analyseret for sammenhænge; '
         'tværfaglige beslutninger med teknikere, specialister og ledelse i 14-mands- og 25-specialistmiljøer, hvor '
         'leverandører og bygherre blev inddraget tidligt.'),
        ('Kommunikerer tydeligt på dansk, mundtligt og skriftligt',
         'Dansk som modersmål med 20+ års teknisk og kommerciel kommunikation; rapporter og beslutningsoplæg '
         'skrevet til ledelse, myndighed og kunder — og formidlet til de teknikere, der skulle arbejde efter dem.')])
    m.page_break()

    m.models_table('DE FØRSTE 90 DAGE — METODEN, ANALYSERNE OG BESLUTNINGERNE',
                   ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'Mød Risk Manager på drikkevandsområdet, de 13 kolleger i Vand Data & Aktiver og nøglepersoner i drift og '
         'projekter; læs de risikoanalyser, der findes i dag, og find ud af, hvor de bliver brugt — og hvor de '
         'ikke bliver.'),
        ('Dag 30',
         'Kortlagt hvordan risiko i dag vurderes på tværs af anlæg, forsyninger og projekter: metoder, skabeloner, '
         'registre og kadence; en liste over de tre steder, hvor forskellig praksis koster mest i beslutningskraft.'),
        ('Dag 60',
         'Fælles metode skitseret sammen med Risk Manager og de relevante fagmiljøer: én skabelon for '
         'risikoanalyse, én struktur for risikoregister med ejer og frist, og en aftalt kadence for rapportering '
         'til direktørområdet.'),
        ('Dag 90',
         'Første tværfaglige risikoanalyse gennemført efter den fælles metode med anbefalinger, der er besluttet '
         'på; risikorapportering leveret til Vand & Byudvikling; og en plan for, hvordan metoden bliver '
         'videreudviklet sammen med koncernens Risk Manager-netværk.')])

    m.section('EN RISIKO ER IKKE ET TAL, FØR NOGEN HAR BESLUTTET NOGET')
    m.para('En sandsynlighed på 10 % siger ingenting i sig selv. Den bliver først til noget, når den er koblet til, '
           'hvad der sker, hvis den indtræffer — hvor længe forsyningen er påvirket, hvem der bliver ramt, og hvad '
           'det koster at reducere risikoen kontra at leve med den. Det er den kobling, jeg har arbejdet med i '
           'drift og projekter, og det er den, et beslutningsgrundlag skal gøre tydelig for ledelsen.', after=80)

    m.section('FACILITERING BETYDER, AT DE RIGTIGE MENNESKER ER I RUMMET')
    m.para('Den bedste risikoanalyse er ikke den, der er skrevet af én person med adgang til alle data. Det er den, '
           'hvor driftsteknikeren, projektlederen og specialisten har siddet sammen og været uenige om, hvor '
           'sandsynligt noget er — fordi uenigheden er information. Min opgave som facilitator er at gøre det trygt '
           'at sige, at man ikke ved det, og at sørge for, at det, der bliver besluttet, står i referatet med en '
           'ejer.', after=80)

    m.section('USIKKERHED SKAL STÅ TYDELIGT, IKKE GLATTES UD')
    m.para('Et beslutningsgrundlag uden usikkerhed er et grundlag, nogen har pyntet. Jeg har siddet med månedlige '
           'rapporteringer, hvor et forkert tal var lettere at skrive end det rigtige, og jeg har lært at gøre det '
           'modsatte: vise intervallet, skrive antagelserne ned og sige, hvad der ville ændre beslutningen. Det '
           'giver kortere møder og bedre beslutninger — og det gør det muligt at lære af dem bagefter.', after=80)

    m.section('KRITISK INFRASTRUKTUR KRÆVER, AT MAN KENDER KONSEKVENSEN')
    m.para('På Lynetten var der ikke en teoretisk forskel på et anlæg og en forsyning: en pumpe, der stoppede, var '
           'vand, der ikke blev flyttet. Det giver en vane, som jeg tager med i analysearbejdet — at gå ud og se '
           'anlægget, før jeg vurderer risikoen for det, og at spørge dem, der har vagten, hvad de faktisk gør, '
           'når alarmen kommer. En analyse, der ikke passer til virkeligheden på anlægget, bliver ikke brugt.', after=80)

    m.section('KONCERNET METODE VINDER KUN, HVIS DEN ER NEM AT BRUGE')
    m.para('En fælles tilgang til risikostyring bliver ikke indført med et skema. Den bliver indført, når den '
           'sparer den enkelte projektleder tid og giver ledelsen noget, den ikke kunne se før. Derfor vil jeg '
           'bygge metoden sammen med dem, der skal leve med den, holde den kort, og automatisere det, der kan '
           'automatiseres — jeg har selv bygget værktøjer i Python, fordi det var hurtigere end at vente på et '
           'system, og ved, hvor grænsen går, før et værktøj bliver en ekstra byrde.', after=80)

    m.section('EN MODEL SKAL KUNNE FORKLARES AF DEM, DER SKAL BRUGE DEN')
    m.para('En kvantitativ model er kun værd noget, hvis den, der skal træffe beslutningen, kan se, hvad der driver '
           'tallet. Derfor bygger jeg modellerne enkle: få variable, tydelige antagelser og en følsomhed, der viser, '
           'hvad der skal ændre sig, før konklusionen ændrer sig — og jeg bygger dem selv i Python og Excel, så '
           'jeg kan svare på, hvordan tallet er lavet.', after=80)

    m.section('JEG HAR STÅET MED ANSVARET, NÅR RISIKOEN BLEV TIL VIRKELIGHED')
    m.para('Jeg har prøvet at være den, der om natten skulle beslutte, om et anlæg kunne køre videre, og den, der '
           'skulle fortælle en bygherre, at en dato ikke holdt. Det giver en respekt for analysearbejdet, som man '
           'ikke får af at læse om det: beslutninger bliver taget af mennesker, der har travlt, og de bliver taget '
           'bedre, hvis grundlaget er kort, ærligt og peger på en handling.', after=80)

    m.section('HVAD JEG VIL LÆRE, OG HVAD JEG IKKE VIL GÆTTE PÅ')
    m.para('Jeg kender driften, anlæggene og projektorganisationen indefra. Jeg vil bruge de første måneder på at '
           'lære HOFORs metoder, myndighedskrav og den måde, risiko i dag bliver vurderet og rapporteret på i de '
           'forskellige forretningsområder — og på at lære af dem, der har lavet risikoanalyse her i årevis. Den '
           'viden skal ind i metoden, ikke ved siden af den.', after=60)

    return m.save(path, title='Risikoanalytiker — HOFOR, Vand Analyse',
                  subject='Risikoanalyse, risikostyring, kritisk infrastruktur og beslutningsgrundlag',
                  keywords='risikoanalyse, risikovurdering, risikostyring, beslutningsgrundlag, '
                           'risikorapportering, tværfaglig facilitering, forsyningssikkerhed, kritisk '
                           'infrastruktur, kvantitativ model, usikkerhed, dansk')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_HOFOR_Risikoanalytiker.docx')))
