# -*- coding: utf-8 -*-
"""Lars Pedersen & Søn A/S — Afdelingsleder for egenproduktion (jord, kloak, beton).

Dansk opgave-først ansøgning + CV i ét dokument (masterdesign).
Kultur og virksomhedsintel: master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md,
afsnittet om Lars Pedersen & Søn (research 05.11.2026).
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Afdelingsledelse af egenproduktion · Kalkulation, fremdrift og kultur'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('5. november 2026')
    m.meta('Lars Pedersen & Søn A/S · Veggerbyvej 33, 9541 Suldrup · Indehaver René Thomasbjerg')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Afdelingsleder for egenproduktion — jord, kloak og beton', bold=True, color='1A1A1A')
    m.para('Til René Thomasbjerg', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('En egenproduktion er en butik med to bundlinjer: økonomien i den enkelte sag og kulturen på holdet. '
           'Fagentrepriser taber penge på tre måder — sager der aldrig skulle have været taget, kalkuler der ikke '
           'holder i virkeligheden, og mandskab der er sat forkert på opgaven. Derfor handler afdelingslederrollen '
           'ikke først om at skaffe flere sager, men om at kunne se forskel på en god og en dårlig sag, før tilbuddet '
           'bliver sendt, og om at have et hold, der gider levere den kvalitet, der blev lovet.', after=80)

    m.para('**Jeg vil drive afdelingen på fire faste ting, som ikke kræver nye systemer.** Først en triage af sagerne inden '
           'der bydes: kunde og betalingshistorik, jordbund og kloaktype, adgangsforhold, tidsplan, egen kapacitet og '
           'hvor meget der skal lægges hos underentreprenører — og en skreven profil for, hvad vi siger nej til. '
           'Dernæst en kalkulation, hvor dækningsgraden er synlig pr. fag og pr. sag, med risikotillæg for de forhold, '
           'ingen kan se på en tegning. Så en opstart med KS-plan, tidsplan, bemandingsplan, sikkerhed og '
           'materialebestilling på plads, før det første spadestik tages. Og endelig en ugentlig produktionstavle pr. '
           'sag, hvor timer brugt mod kalkule, fremdrift og afvigelser står side om side — så en sag bliver rød i uge '
           'tre og ikke i uge ni.', after=80)

    m.para('Efter aflevering kommer den del, der afgør, om afdelingen bliver bedre år for år: en afterkalkule pr. sag '
           'med to linjer — hvad vi troede, og hvad der skete — og et punkt i næste tilbud, der er rettet efter det. '
           'De tal, jeg vil stå til ansvar for sammen med dig, er dækningsgrad pr. sag og pr. fag, afvigelsen mellem '
           'tilbud og afterkalkule, hit rate, produktivitet i timer pr. enhed, sygefravær, KS-afvigelser og hvor mange '
           'sager der kommer igen fra den samme bygherre.', after=80)

    m.para('Jeg kommer med den kommercielle og den personalemæssige side af rollen. I tre år har jeg drevet egen '
           'virksomhed med fuldt P&L: tilbud, kalkule, prissætning, dækningsgrad, underentreprenører, '
           'leverandørforhandling og de konsekvenser, det har, når en aftale ikke holdes. Jeg har stået på bygherrens '
           'side af bordet og på entreprenørens, og jeg ved, hvor forskelligt den samme sag ser ud alt efter, hvilken '
           'stol man sidder på. Personalemæssigt har jeg haft ansvar for både timelønnede og faglærte — fem '
           'elektrikere og tre lærlinge med ansættelser, MUS, sygesager, kompetencematrix og oplæring — og jeg har '
           'ledet 25 specialister og funktionærer gennem 37 samtidige anlægsprojekter uden at have personaleansvar for '
           'dem. Det er de to slags ledelse, rollen kræver, og jeg har prøvet dem begge.', after=80)

    m.para('Jeg skal være tydelig om tre ting. Den første: jeg er ikke uddannet ingeniør eller bygningskonstruktør. '
           'Jeg er elautoriseret maskinmester med en B.Tech i teknologiledelse og maskinteknik, og min faglige bund '
           'er el, ventilation og tekniske anlæg — ikke jord, kloak og beton. Den anden: jeg har ikke stået i spidsen '
           'for en egenproduktion i netop de fag før, og jeg vil hellere lære kloak- og betonfagene af jeres '
           'projektledere og formænd end lade som om, jeg allerede kan dem. Den tredje: jeg bor i Måløv, og Suldrup '
           'er omkring tre timer væk. Det er en flytning, ikke en pendling, og det skal vi have talt om i første '
           'samtale frem for at opdage senere.', after=80)

    m.para('Det, jeg til gengæld ved, er, hvordan en fagentreprise-afdeling tjenes hjem: at kalkulationen har et '
           'risikotillæg, at timerne bliver fulgt hver uge og ikke hver kvartal, at maskiner og mandskab bliver sat '
           'efter, hvor de koster mindst at flytte, og at en bygherre kommer igen, fordi aftaler blev holdt — også når '
           'det regnede i tre uger. De første 90 dage har jeg lagt som en plan: uge 1–2 på sagerne og på gulvet med '
           'hver formand og projektleder, dag 30 med overblik over ordrebeholdning, igangværende sager og '
           'dækningsgrad pr. sag, dag 60 med triage- og kalkulationsproces på plads og den første afterkalkule, dag 90 '
           'med kapacitetsplan for de næste tolv uger, en udviklingsplan pr. medarbejder og en anbefaling til dig om, '
           'hvilke sagstyper afdelingen skal satse på — og hvilke vi skal lade ligge.', after=80)

    m.para('Det, der trækker mig mod Lars Pedersen & Søn, er kombinationen af en virksomhed med tre generationer bag '
           'sig og en nyoprettet afdeling, hvor retningen ikke er låst endnu. I har en sund økonomi og en klar '
           'ambition om at udvikle egenproduktionen, og I har allerede jord, kloak, beton og murer i huset — det er '
           'ikke en afdeling, der skal opfindes, men en, der skal strammes op, have en tydelig kultur og en '
           'kapacitet, der kan følge med. At skulle stå i spidsen for det og svare direkte til indehaveren er præcis '
           'den slags ansvar, jeg søger.', after=80)

    m.para('Jeg er også professionel og aktiv Claude-koder og bruger Python og Claude til tilbudsoversigter, '
           'dækningsgradsopfølgning og kapacitetsberegning, og til investeringsmodeller med NPV, IRR, følsomhed og '
           'scenarier, når der skal regnes på maskiner eller ekstra kapacitet — og til den ene oversigt, som både du og '
           'projektlederne kan se, hvor sagerne står henne. Det er ikke et system, der skal indføres; det er et '
           'værktøj, der gør et eksisterende regneark hurtigere og lettere at læse.', after=80)

    m.para('Jeg vil gerne komme til Suldrup og tale med dig og den øvrige ledelse om, hvordan egenproduktionen skal '
           'udvikles de næste par år — og høre, hvilke sager I i dag siger nej til, og hvorfor.', after=80)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Ledelses- og entrepriseerfaring med 20+ år fra dansk byggeri, teknik og drift — fuldt P&L-ansvar i egen '
           'virksomhed, personaleansvar for både timelønnede og faglærte samt tværgående ledelse af 25 specialister '
           'gennem 37 anlægsprojekter. Arbejder fra tilbud til afterkalkule, med dækningsgrad, fremdrift og kultur '
           'som de faste styringspunkter. Bruger SAP, KPI-tavler og egne AI-værktøjer (Python, Claude) til kalkule og '
           'økonomiopfølgning.', after=80)

    m.section('KOMMERCIELT ANSVAR OG RESULTATER')
    for label, body in [
        ('P&L og kalkulation',
         'Fuldt P&L-ansvar i egen virksomhed siden 2023: tilbud, kalkule, prissætning, dækningsgrad, '
         'leverandørforhandling og afterkalkule pr. sag — med serviceaftaler målt på responstid, kvalitet og '
         'leveringsevne.'),
        ('Personaleledelse',
         'Fem elektrikere og tre lærlinge, herunder ansættelser, MUS/GRUS, sygesager, kompetencematrix og oplæring; '
         'desuden 25 funktionærer og specialister i 37 samtidige CAPEX-projekter uden formelt personaleansvar.'),
        ('Entreprise og bygherre',
         'Tilbud og afleveringspakker, underentreprenører, aftalegrundlag og KS; daglig dialog med bygherrer, '
         'rådgivere og leverandører i både egen virksomhed og i anlægsprojekter under GMP.'),
        ('Fremdrift og kvalitet',
         '11 parallelle anlægsprojekter og et 14-mands team med daglige tavlemøder og flaskehalsanalyser, der gav et '
         'markant løft i leveringsevnen; nul kritiske afvigelser ved aflevering i GMP-regulerede projekter.'),
        ('Forbedring og data',
         'PDCA-program reducerede energiomkostningerne med 40 %. A3 og 5 x hvorfor i fejlfinding. Egne '
         'Python/Claude-værktøjer har givet over 40 % produktivitetsløft i egen virksomhed.')]:
        m.bullet(label, body, after=30)

    m.models_table('VÆRKTØJER OG METODER', ('Opgave', 'Værktøj og dokumenteret anvendelse'), [
        ('Sagsvurdering og tilbud',
         'Triage før tilbud ud fra kunde, forhold, tidsplan, kapacitet og underentreprenørbehov; kalkule med '
         'dækningsgrad pr. fag og risikotillæg; skreven profil for hvilke sager vi takker nej til.'),
        ('Sagsøkonomi og opfølgning',
         'Ugentlig produktionstavle pr. sag med timer mod kalkule, fremdrift, materialer og afvigelser; '
         'afterkalkule pr. sag med læring ind i næste tilbud. SAP ERP til økonomi og aktiver.'),
        ('Bemanding og kapacitet',
         'Kapacitetsplan 12 uger frem, fordeling mellem egne folk og underentreprenører, kompetencematrix og '
         'lærlingeplan; fraværsopfølgning og vagt-/bemandingsplanlægning.'),
        ('Personaleledelse',
         'Situationsbestemt ledelse (SLII), delegeringstrappen, 1:1 hver fjortende dag, MUS/GRUS, SBI-feedback og '
         'GROW; udviklingsplan pr. medarbejder. Lærlinge ført til svendeprøve.'),
        ('Kvalitet, sikkerhed og jura',
         'KS-plan, afvigelser med ejer og frist, dokumentation og afleveringsforretning; APV, LOTO, risikovurdering '
         'og nærved-hændelser; AB 18/ABT 18 og underentreprenøraftaler.'),
        ('Kultur og tavlemøder',
         'Daglige eller ugentlige tavlemøder med få tal, Gemba på pladsen og eskalering ved undtagelse; synlig '
         'ledelse på byggepladsen frem for mails fra kontoret.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L-ansvar · erhvervs- og industrikunder',
         [('Kommercielt ansvar', 'Tilbud, kalkule, prissætning, dækningsgrad og leverandørforhandling; '
                                 'serviceaftaler og kundedialog om løsningsvalg, pris og tid.'),
          ('Personale og drift', 'Ansættelser, 1:1 og MUS, kompetencematrix, oplæring af lærlinge, arbejdsmiljø og '
                                 'bemanding på skiftende opgaver.'),
          ('Digitale værktøjer', 'Python/Claude API til tilbud, tidsplaner, KS-tjeklister og KPI-dashboard; over '
                                 '40 % produktivitetsløft i virksomheden.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024',
         '37 samtidige anlægsprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Økonomi og fremdrift', 'Fremdrift, økonomi, risici og ressourcer mellem engineering, indkøb og anlæg; '
                                   'månedsrapportering til ledelse og bygherre.'),
          ('Kvalitet og aflevering', 'FAT/SAT og IQ/OQ/PQ med nul kritiske afvigelser ved aflevering; projektledelse '
                                     'af 25 specialister uden personaleansvar.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter · DKK 2–10 mio. pr. projekt',
         [('Leverance og arbejdsgange', 'Udbud, tilbud, underentreprenører og afleveringspakker; daglige tavlemøder '
                                        'og flaskehalsanalyser samt standardiserede arbejdsgange gav et markant løft i '
                                        'leveringsevnen.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos, Lynetten · København · aug. 2017–jan. 2022',
         '24/7-drift · spildevandsanlæg med pumper, HVAC, højspændingstavler og SCADA · skiftehold',
         [('Tekniske anlæg og drift', 'Forebyggende vedligehold, akut fejlfinding og reservedelsflow; 5S, Standard '
                                      'Work og PDCA på værksted og lager.'),
          ('Sikkerhed', 'LOTO, APV, risikovurdering og nærved-hændelser i skifteholdsdrift.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted',
         [('Plan og mål', 'Vagtplanlægning, materialestyring og målopfølgning; fejldiagnose, rodårsagsanalyse og '
                          'korrigerende handlinger på industrielt udstyr.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        m.doc.paragraphs[-1].runs[0].text = 'Omfang: '
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('UDDANNELSE OG AUTORISATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering — maskinmesterretningen',
          'Maskinmesterskolen København · 2017–2022 · EQF 6 · GPA 7,6/12')
    m.edu('Elautoriseret maskinmester (LV/MV/HV), stærkstrøm', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('El- og maskinteknisk design, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Entrepriseret og aftalegrundlag: AB 18, ABT 18, KS og arbejdsmiljø', 'Anvendt i egen virksomhed og i anlægsprojekter')
    m.edu('Lean og forbedringspraksis: 5S, PDCA, VSM, A3, Kaizen', 'Løbende kurser og daglig anvendelse i drift og projekter')

    m.section('SPROG, PRAKTISK OG REFERENCER')
    m.para('Dansk og persisk/farsi: modersmål · Engelsk: professionelt i skrift og tale · Kørekort B · Bopæl i Måløv. '
           'Suldrup er ca. tre timer herfra, så stillingen forudsætter en flytning, og det vil jeg gerne drøfte åbent i '
           'første samtale. Referencer fra Novo Nordisk og Biofos samt fra samarbejdspartnere i egen virksomhed oplyses '
           'efter aftale.', after=70)

    m.models_table('KRAV I OPSLAGET — MIN DOKUMENTATION', ('Krav', 'Dokumentation'), [
        ('Uddannelse som ingeniør eller bygningskonstruktør',
         'Ikke opfyldt i den form. Elautoriseret maskinmester med B.Tech i Technology Management & Mechanical '
         'Engineering (EQF 6) — teknisk tung uddannelse, men ikke byggefaglig. Står her, så det kan vurderes tidligt.'),
        ('Personaleledelse af timelønnede og funktionærer',
         'Fem elektrikere og tre lærlinge med ansættelser og afskedigelser, MUS, personalesager, sygesager og '
         'oplæring; 25 funktionærer og '
         'specialister ledet gennem 37 projekter; 14-mands entrepriseteam.'),
        ('Resultater i tidligere stillinger',
         'Eget P&L med dækningsgrad og afterkalkule; nul kritiske afvigelser ved aflevering i GMP-projekter; 40 % '
         'lavere energiomkostning via PDCA; 40 % produktivitetsløft via egne digitale værktøjer.'),
        ('Tilbuds- og sagsøkonomi samt kalkulation',
         'Tilbud, kalkule, prissætning og dækningsgrad i egen virksomhed i tre år; SAP ERP til økonomi, aktiver og '
         'omkostninger; månedsrapportering til ledelse og bygherre.'),
        ('Samarbejde med projektledere og repræsentation over for bygherrer',
         'Daglig dialog med bygherrer, rådgivere og underentreprenører; koordinering mellem projektledere, og '
         'forståelse for hvordan fag-, hoved- og totalentreprise adskiller sig i ansvar og risiko; '
         'produktion og indkøb gennem RACI og faste beslutningspunkter.'),
        ('Motivation for kultur og kapacitetsudvikling',
         'Opbygget egen virksomhed fra nul med 8 medarbejdere; lavet kompetencematricer, lærlingeplaner og '
         'tavlemødekultur i både værksted, entreprise og produktion. Arbejdet med trivsel som et tal, der kan '
         'følges, ikke som en stemning.'),
        ('En tillidsvækkende og involverende ledelsesstil',
         'Involverende i beslutningerne og tydelig om ansvaret: 1:1 hver anden uge, SBI-feedback tæt på '
         'opgaven, beslutninger skrevet ned med ansvarlig og dato — og de samme fem spørgsmål til alle.'),
        ('Netværk inden for jord, kloak og beton',
         'Ikke et branchenetværk i de fag — mit netværk er el, ventilation, industri og forsyning. Det er et af de '
         'områder, hvor jeg skal lære af jeres formænd og projektledere i starten.'),
        ('Økonomisk overblik på tilbuds-, sags- og virksomhedsniveau',
         'Bygget økonomiske oversigter på alle tre niveauer i egen virksomhed; vane med at se en enkelt sag i '
         'forhold til hele forretningsområder og virksomhedens samlede kapacitet og likviditet.')])
    m.page_break()

    m.models_table('FØRSTE 90 DAGE — SAGER, ØKONOMI OG HOLD', ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'Ud på alle igangværende sager med hver projektleder og formand. Gennemgang af ordrebeholdningen, de seneste '
         '20 tilbud og de sager, der har kostet penge. Møde med hver medarbejder i afdelingen til en kort 1:1 om '
         'opgaver, kompetencer og hvad der driller.'),
        ('Dag 30',
         'Overblik på én side: igangværende sager, ordrebeholdning, dækningsgrad pr. sag og pr. fag, og hvor '
         'timerne brænder af. Skreven triage-profil med kriterier for, hvad afdelingen byder på, og hvad vi takker nej '
         'til — godkendt af dig.'),
        ('Dag 60',
         'Triage- og kalkulationsproces i brug på alle nye tilbud. Ugentlig produktionstavle pr. sag kørende. Første '
         'afterkalkule gennemført og lært videre ind i næste tilbud. Bemandingsplan for de kommende uger aftalt med '
         'projektlederne.'),
        ('Dag 90',
         'Kapacitetsplan for de næste tolv uger inkl. underentreprenører og lærlinge. Udviklingsplan pr. medarbejder '
         'og en kompetencematrix, der viser, hvem der kan hvad på hvilke opgavetyper. Anbefaling til dig om de strategiske valg: hvilke '
         'sagstyper og kundesegmenter afdelingen skal satse på — og hvilke vi skal lade ligge.')])

    m.section('SÅDAN TJENER EN FAGENTREPRISE PENGE')
    m.para('Der er tre steder, pengene bliver tjent eller tabt, og ingen af dem er i produktionen alene. Det første er '
           'udvælgelsen: en sag med dårlige jordforhold, ingen adgang til pladsen og en bygherre, der vil have alt på '
           'én gang, bliver ikke bedre af at blive vundet. Det andet er kalkulen: hvis risikotillægget ikke er der, '
           'eller hvis timeforbruget er sat efter den bedste uge i stedet for den normale, er tabet allerede besluttet, '
           'før maskinen starter. Det tredje er opfølgningen: en sag, der først bliver rød i uge ni, kan ikke '
           'reddes — en sag, der bliver rød i uge tre, kan stadig.', after=80)

    m.section('TRIAGE — HVILKE SAGER VI SIGER JA TIL')
    m.para('Jeg vil have en kort, skriftlig profil for, hvad afdelingen byder på: hvilke sagstyper, hvilke '
           'størrelser, hvilke bygherrer og hvilke geografiske områder der giver mening i forhold til kapacitet og '
           'dækning. Ved hver forespørgsel går vi de samme fem punkter igennem — forhold og adgang, tid og sæson, '
           'egen kapacitet mod underentreprenører, betalingsforhold og teknisk risiko. Er svaret rødt på to af dem, '
           'siger vi pænt nej tak og bruger tiden på noget, der kan tjenes. Det er også det, der gør et nej nemt at '
           'sige til en kunde, man gerne vil beholde.', after=80)

    m.section('KULTUR OG BEMANDING I EN FAGENTREPRISE')
    m.para('Kulturen i en egenproduktion bliver ikke skabt på et kontor. Den bliver skabt af, hvordan formanden bliver '
           'talt til om morgenen, om der bliver ryddet op efter sig, og om der er styr på materialer og maskiner, når '
           'folk møder ind. Jeg vil være synlig på pladserne, holde 1:1 med både timelønnede og funktionærer, tage '
           'sygesager tidligt og ordentligt, og sørge for at lærlinge får opgaver, der gør dem dygtigere i stedet for '
           'kun at gøre dem hurtige. Og når der er travlt — og det er der i byggeriet — er svaret planlægning, ikke '
           'overtid indtil det knækker.', after=80)

    m.section('SIKKERHED OG KVALITET PÅ PLADSEN')
    m.para('Jord, kloak og beton er håndværk med tunge løft, åbne udgravninger, maskiner og trafik omkring sig. APV '
           'og risikovurdering er ikke et dokument, der skal opdateres én gang om året; det er en samtale, der bliver '
           'ført, hver gang forholdene ændrer sig. KS-planen følger sagen fra opstart til aflevering, med afvigelser '
           'der får en ejer og en frist, og dokumentationen i orden, så 1- og 5-års gennemgangen ikke bliver en '
           'overraskelse. Jeg har prøvet begge dele: nul kritiske fund ved aflevering i GMP-projekter og 24/7-drift, '
           'hvor sikkerhed var en forudsætning for at få lov at arbejde.', after=80)

    m.section('ØKONOMISK OVERBLIK PÅ TRE NIVEAUER')
    m.para('Tilbudsniveau: hvad koster det at byde, og hvad skal dækningsgraden være, før det er interessant. Sagsniveau: '
           'hvor langt er vi, hvad har vi brugt, hvad kommer det til at koste at gøre færdigt. Virksomhedsniveau: hvad '
           'binder kapaciteten, og hvordan ser likviditeten ud, når materialer og løn skal betales, før bygherren '
           'betaler. Det sidste er det, de fleste glemmer, og det er der, en ellers sund afdeling kommer i problemer.',
           after=80)

    m.section('DIGITALT ARBEJDE MED ET KLART FORMÅL')
    m.para('Jeg bruger Python og Claude til at trække tal sammen på tværs — timer pr. sag mod kalkule, dækningsgrad pr. '
           'fag, kapacitet i de næste uger — og til at lave den ene oversigt, som både indehaver og projektledere kan '
           'læse på to minutter. Det erstatter ikke et ERP-system, men det gør opfølgningen hurtigere, og det sker '
           'inden for jeres systemer og godkendelser.', after=80)

    return m.save(path, title='Ansøgning og CV — Afdelingsleder for egenproduktion, Lars Pedersen & Søn',
                  subject='Afdelingsledelse med kalkulation, fremdrift og kultur i fagentrepriser',
                  keywords='afdelingsleder, egenproduktion, jord, kloak, beton, kalkulation, P&L')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_LarsPedersenSon_AfdelingslederEgenproduktion.docx')))
