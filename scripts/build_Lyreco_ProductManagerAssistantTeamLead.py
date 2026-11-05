# -*- coding: utf-8 -*-
"""Lyreco Danmark A/S — Product Manager Assistant Team Lead, Roskilde.

Dansk leverance (opslaget er dansk): opgavefokuseret motiveringsside + CV i ét dokument.
Kultur- og rolleintel: master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md,
afsnit om Lyreco (research 05.11.2026).
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Produktdata, proces og teamledelse · SAP, datakvalitet og katalogflow'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('5. november 2026')
    m.meta('Lyreco Danmark A/S · Lykkegårdsvej 10, 4000 Roskilde · Product Marketing')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Product Manager Assistant Team Lead', bold=True, color='1A1A1A')
    m.para('Til Merchandise Director Eva Bech Lynggaard', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('Et sortiment på flere tusinde varenumre består ikke af varer. Det består af data. Kunden ser prisen, '
           'alternativet, billedet og leveringstiden, før hun ser produktet — og er ét felt forkert, er det ikke en '
           'intern detalje, men en reklamation hos kundeservice, en prisliste der ikke kan bruges, eller en kampagne '
           'der falder til jorden. Det er præcis der, Product Manager Assistant-teamet afgør, om forretningen ser '
           'professionel ud. Rollen som team lead er at gøre den rigtighed til en vane i stedet for en '
           'tilfældighed.', after=80)

    m.para('**Jeg vil drive teamet på fire faste ting, og ingen af dem kræver nye systemer.** Først én definition af '
           '"korrekt" pr. dataobjekt: hvad skal der som minimum stå på et produkt, et alternativ, en leverandør, et '
           'leverandørhierarki og en pris, hvem ejer feltet, og hvad er konsekvensen, når det mangler. Dernæst én '
           'indgang til ændringer: anmodninger fra salg, kundeservice, indkøb og lager skal ind i samme kø med '
           'prioritet og frist i stedet for at komme som mails til den, der tilfældigvis er på arbejde. Så kontrol '
           'før udgivelse frem for efter en klage — faste udtræk der sammenligner prislister, alternative varer, '
           'billeder og obligatoriske felter, så fejlen findes, før kunden gør. Og endelig én tavle for teamet: hvad '
           'er i gang, hvad venter på hvem, og hvem dækker hvem i næste uge.', after=80)

    m.para('Konkret er det de opgaver, der står i opslaget: oprettelse, ændring og vedligeholdelse af produkter, '
           'alternativer og prognoser; leverandørdata og leverandørhierarkier, der hænger sammen med det, indkøb '
           'forhandler på; produktforespørgsler og reklamationer fra salg, kundeservice, indkøb og lager; afvigelser '
           'på leverandørfakturaer, der bliver gjort klar som beslutningsgrundlag for Product Managers i stedet for '
           'at ligge som en bunke bilag; prismateriale til tilbudssystemerne og prislister, der bliver løftet rigtigt '
           'både lokalt og til hovedkontoret; og katalogprocesser, hvor produktinformation, billeder og content '
           'holder kvaliteten. Det er mange små opgaver — og netop derfor skal de have én rytme.', after=80)

    m.para('Tre medarbejdere betyder, at hver kompetence skal have en anden person bag sig. Derfor en '
           'kompetencematrix over SAP, STEP, prislister, katalog og reklamationsflow, skrevne arbejdsgange på det, '
           'der bliver gjort sjældent, en ugentlig prioriteringstavle og 1:1 hver fjortende dag med feedback tæt på '
           'opgaven. Jeg vil også have aftalt med salg, kundeservice, indkøb og lager, hvad de kan forvente af os, og '
           'hvornår — en kort intern aftale slår mange undskyldninger. Og når nogen holder ferie, skal svaret være i '
           'processen, ikke i en kollegas hoved.', after=80)

    m.para('Jeg kommer med den operationelle og den koordinerende side af rollen. SAP har jeg brugt dagligt til '
           'materialer, aktiver, omkostninger og rapportering, og jeg er vant til at arbejde med data, hvor fejl '
           'skal kunne spores: som projektleder på 37 samtidige anlægsprojekter med 25 specialister under GMP, FDA og '
           'EMA har jeg dokumenteret acceptkriterier, håndteret afvigelser og leveret uden kritiske fund. I min egen '
           'virksomhed står jeg selv for varenumre, prislister, leverandøraftaler, tilbud og kontrol af '
           'leverandørfakturaer — inklusive de afvigelser, der skal findes, før regnskabet gør. Og jeg bygger mine '
           'egne værktøjer i Python og med Claude til at trække lister ud, sammenligne dem og finde de poster, hvor '
           'noget mangler eller ikke stemmer; det har taget over 40 % af det administrative arbejde ud af min egen '
           'hverdag.', after=80)

    m.para('Jeg skal være ærlig om to ting. Jeg har ikke arbejdet i product marketing før, og jeg har ikke brugt '
           'STEP eller Zendesk — det er systemer, jeg lærer på uger, ikke år, og SAP har jeg som nævnt brugt i '
           'dagligdagen. Og jeg har ledet håndværkere og teknikere, ikke tre funktionærer i en administrativ proces. '
           'Forskellen er reel: her er der mindre brandslukning og mere prioritering, kvalitet og tålmodighed med '
           'detaljen. Men opgaven er den samme — tydelige forventninger, tæt feedback, og en plan for hvem der '
           'dækker hvad, så teamet ikke afhænger af én person.', after=80)

    m.para('Det, der trækker mig mod Lyreco, er kombinationen af noget meget gammelt og noget meget konkret: en '
           'familieejet virksomhed siden 1926, et katalog siden 1959 og SAP siden 1999 — det er tre lag af '
           'struktur, som de fleste ikke har. Ovenpå det en bæredygtighedsambition, hvor 90 % af omsætningen skal '
           'komme fra Sustainable Selection i 2026. Bæredygtighed kan kun dokumenteres med data, og derfor hænger '
           'arbejdet i '
           'jeres team direkte sammen med den dagsorden. Jeg genkender også jeres fire værdier — excellence, passion, '
           'respect og agility — som fire ting, der kun betyder noget, hvis de er synlige i den daglige leverance.', after=80)

    m.para('Praktisk: jeg bor i Måløv og har ca. 40 minutter til Lykkegårdsvej. Jeg taler dansk og persisk som '
           'modersmål og engelsk professionelt, skriftligt og mundtligt, og jeg arbejder i Excel dagligt ved siden af '
           'mine egne Python-værktøjer. Jeg vil gerne komme til Roskilde og tale om, hvordan teamet bliver stærkere '
           'på datakvalitet og proces — og høre, hvor I i dag bruger mest tid på at rette op efter fejl.', after=80)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Leder med 20+ års erfaring fra teknik, projekter og egen virksomhed — vant til at arbejde i systemer, '
           'hvor data skal være korrekte og sporbare, og til at koordinere mellem faglige miljøer med forskellige '
           'prioriteter. Daglig bruger af SAP og Excel; bygger egne Python- og Claude-værktøjer til udtræk, '
           'sammenligning og kvalitetskontrol af lister og priser. Leder et lille hold med faste 1:1, '
           'kompetencematrix og skrevne arbejdsgange, så opgaver kan løses på tværs ved ferie og fravær.', after=80)

    m.section('KOORDINERING, DATA OG RESULTATER')
    for label, body in [
        ('Data- og dokumentationskvalitet',
         '37 samtidige anlægsprojekter under GMP/FDA/EMA med dokumenterede acceptkriterier, afvigelser med ejer og '
         'frist og auditeret aflevering — nul kritiske fund. Samme disciplin bruges på prislister og varedata.'),
        ('Systemer i daglig brug',
         'SAP til materialer, aktiver, omkostninger og rapportering; Excel til udtræk, pivottabeller og kontrol; '
         'egne Python/Claude-værktøjer til at sammenligne lister og finde manglende eller afvigende poster.'),
        ('Koordinering på tværs',
         'Bindeled mellem salg, indkøb, produktion, rådgivere og ledelse i både projekter og egen virksomhed; RACI, '
         'beslutninger med ansvarlig og dato, og ugentlige tavlemøder som fast rytme.'),
        ('Personaleansvar og udvikling',
         'Fem elektrikere og tre lærlinge med ansættelser, MUS, sygesager og oplæring; 25 specialister og '
         'funktionærer ledet gennem projekter; kompetencematrix og oplæring så opgaver kan flyttes mellem personer.'),
        ('Procesforbedring med effekt',
         'PDCA, 5S, standard work, A3 og 5 x hvorfor i daglig brug; et PDCA-forløb reducerede energiforbruget med '
         '40 %, og egne digitale værktøjer har løftet produktiviteten med over 40 % i egen virksomhed.')]:
        m.bullet(label, body, after=25)

    m.models_table('VÆRKTØJER OG METODER', ('Opgave', 'Værktøj og dokumenteret anvendelse'), [
        ('Produkt- og stamdata',
         'Én definition af "korrekt" pr. dataobjekt, obligatoriske felter, dataejerskab og fast kontroludtræk før '
         'udgivelse. SAP (materialer, leverandører, priser) og Excel/Python til sammenligning af lister.'),
        ('Ændrings- og opgaveflow',
         'Én indgang og én kø for anmodninger med prioritet, ejer og frist; Zendesk- og SAP-baserede sager; '
         'ugentlig prioriteringstavle og eskaleringsregler, når noget haster.'),
        ('Katalog og kampagner',
         'Kvalitetssikring af produktinformation, billeder og indhold før publicering; prislister og prismateriale '
         'til tilbudssystemer kontrolleret mod aftalte priser og kampagneperioder.'),
        ('Personaledelse',
         'Situationsbestemt ledelse (SLII), delegeringstrappen, 1:1 hver fjortende dag, MUS/GRUS, SBI-feedback og '
         'GROW; kompetencematrix og skrevne arbejdsgange, så teamet kan dække hinanden.'),
        ('Proces og forbedring',
         'PDCA, 5S, standard work, proceskort, A3 og 5 x hvorfor med verifikation af, at tiltaget holder; et '
         'begrænset antal forbedringer ad gangen med ejer og målt effekt.'),
        ('Rapportering og interessenter',
         'Faste nøgletal på en side til ledelsen, skriftlige beslutninger med ansvarlig og dato, og aftaler med '
         'salg, kundeservice, indkøb og lager om hvad de kan forvente og hvornår.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · erhvervs- og industrikunder',
         [('Varer, priser og leverandører', 'Varenumre, prislister, tilbud og leverandøraftaler; kontrol af '
                                            'leverandørfakturaer og afvigelser, før de rammer regnskabet.'),
          ('Personale og drift', 'Ansættelser, 1:1, MUS, kompetencematrix og oplæring af lærlinge; daglig '
                                 'prioritering af opgaver mellem fem mand og tre lærlinge.'),
          ('Digitale værktøjer', 'Python og Claude API til tilbud, planlægning, kvalitetschecklister og '
                                 'KPI-dashboard; over 40 % produktivitetsløft i virksomheden.')]),
        ('Senior idriftsættelsesingeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024',
         '37 samtidige anlægsprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Dokumentation og kvalitet', 'Acceptkriterier, FAT/SAT og IQ/OQ/PQ med sporbar dokumentation og '
                                        'håndtering af afvigelser; nul kritiske fund ved aflevering.'),
          ('Koordinering og rapportering', 'Fremdrift, økonomi, risiko og ressourcer mellem engineering, indkøb og '
                                           'drift; månedsrapportering til ledelse og bygherre.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter · 2–10 mio. kr. pr. projekt',
         [('Tilbud og ordreflow', 'Tilbud, kalkuler, underleverandører og afleveringspakker; daglige tavlemøder og '
                                  'flaskehalsanalyser løftede leveranceevnen.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos, Lynetten · København · aug. 2017–jan. 2022',
         '24/7-drift · reservedelslager med varenumre og min./maks. · SCADA, pumper, HVAC, højspænding',
         [('Varedata og lager', 'Reservedele og materialer med varenumre, min./maks.-niveauer og løbende '
                                'optælling; registrering af nedetid og afvigelser.'),
          ('Sikkerhed og standarder', 'LOTO, APV, risikovurdering og nærhændelser i skiftdrift; standard work, 5S '
                                      'og PDCA i værksted og lager.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran, Iran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · industrielt udstyr',
         [('Plan og mål', 'Vagtplanlægning, materialestyring og opfølgning på mål; fejlfinding, '
                          'rodårsagsanalyse og korrigerende handlinger på produktionsudstyr.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        m.doc.paragraphs[-1].runs[0].text = 'Omfang: '
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('UDDANNELSE OG AUTORISATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering',
          'Maskinmesterskolen København · 2017–2022 · EQF 6 · GPA 7,6/12')
    m.edu('Elautoriseret maskinmester (LV/MV/HV), stærkstrøm', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('El- og maskinteknisk design, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Entreprenørret og aftalegrundlag, AB 18, ABT 18, KS og arbejdsmiljø',
          'Anvendt i egen virksomhed og i anlægsprojekter')
    m.edu('Lean og procesforbedring: 5S, PDCA, VSM, A3, Kaizen',
          'Løbende kurser og daglig anvendelse i drift og projekter')

    m.section('SPROG, PRAKTISK OG REFERENCER')
    m.para('Dansk og persisk: modersmål · Engelsk: professionelt, skriftligt og mundtligt · Kørekort B · Bopæl i '
           'Måløv, ca. 40 minutter fra Lykkegårdsvej · Fast bruger af Excel, SAP og egne Python/Claude-værktøjer · '
           'Referencer fra Novo Nordisk og Biofos samt fra samarbejdspartnere i egen virksomhed oplyses efter '
           'aftale.', after=70)

    m.models_table('KRAV I OPSLAGET — MIN DOKUMENTATION', ('Krav', 'Dokumentation'), [
        ('Erfaring med personaleledelse eller med at skabe resultater gennem andre',
         'Fem elektrikere og tre lærlinge med fuldt personaleansvar i tre år; 25 specialister og funktionærer ledet '
         'gennem 37 projekter; kompetencematrix, MUS, 1:1 og kompetenceudvikling som faste rutiner.'),
        ('Synlig og nærværende leder, der skaber struktur, retning og engagement',
         'Ugentlig prioriteringstavle, 1:1 hver fjortende dag, skrevne arbejdsgange og fast videndeling; ledelse '
         'på gulvet frem for i mails — og trivsel som noget, der bliver talt om hver uge, ikke kun til MUS.'),
        ('Erfaring fra koordinerende eller administrativ rolle, gerne Product Management eller indkøb',
         'Koordineret tilbud, indkøb, underleverandører og aflevering i egen virksomhed og i 37 projekter; arbejdet '
         'med varedata, prislister og leverandøraftaler. Product marketing er nyt for mig.'),
        ('Planlægning, struktur og processtyring',
         'Bygget planer, kompetencematricer og arbejdsgange op fra nul i egen virksomhed; PDCA og standard work som '
         'daglig praksis, ikke som kampagne.'),
        ('Sans for detaljer og datakvalitet',
         'Sporbar dokumentation uden kritiske fund under GMP/FDA/EMA; kontrol af leverandørfakturaer og prislister; '
         'egne kontrollister og udtræk, der finder manglende felter og afvigelser.'),
        ('Professionel kommunikation med mange forskellige interessenter',
         'Daglig dialog med kunder, rådgivere, underleverandører, produktion og ledelse; engelsk som arbejdssprog i '
         'to år i international projektorganisation.'),
        ('Kompleks organisation med mange opgaver og deadlines',
         '37 samtidige projekter og 11 samtidige sager med faste beslutningspunkter; prioriteter skrevet ned og '
         'delt, så de kan efterprøves.'),
        ('Erfaren bruger af Microsoft Office og Excel; SAP samt gerne STEP og Zendesk; engelsk flydende',
         'SAP dagligt til materialer, aktiver og omkostninger; Excel til udtræk, pivottabeller og kontrol; '
         'Python/Claude til de tunge sammenligninger. STEP og Zendesk skal jeg lære — engelsk er professionelt.')])
    m.page_break()

    m.models_table('FØRSTE 90 DAGE — DATA, FLOW OG TEAM', ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'Sidde med hver af de tre medarbejdere og se deres opgaver i SAP og STEP. Gennemgå de seneste 20 '
         'anmodninger, reklamationer og prislistekørsler og se, hvor de kom fra, og hvor lang tid de tog. Møde med '
         'salg, kundeservice, indkøb og lager om, hvad de oplever som det største problem.'),
        ('Dag 30',
         'Overblik på én side: opgavemængde pr. uge, gennemløbstid, antal fejl fundet efter publicering og de fem '
         'hyppigste årsager. Kompetencematrix for teamet med huller markeret, og en aftale med Product Managers om '
         'hvad der skal prioriteres først.'),
        ('Dag 60',
         'Én indgang og én kø for anmodninger i brug med prioritet og frist. Kontroludtræk før udgivelse på plads '
         'for priser, alternative varer og obligatoriske felter. Skrevne arbejdsgange på de opgaver, der kun gøres '
         'sjældent, så ferie og sygdom ikke stopper flowet.'),
        ('Dag 90',
         'Målt forbedring i gennemløbstid og i antal fejl fundet efter publicering, plus en dækningsplan, hvor hver '
         'opgave har en navngivet anden person. Forslag til dig om, hvilke processer der skal automatiseres næste '
         'gang — og hvilke der bare skal have en klarere aftale.')])

    m.section('SÅDAN HOLDER ET SORTIMENT AF DATA')
    m.para('I en engrosforretning er stamdata ikke en teknisk detalje; det er den måde, sortimentet bliver solgt på. '
           'Et produkt uden korrekt alternativ stopper en ordre, en pris der ikke er opdateret koster penge på hver '
           'linje, og et manglende billede eller en forkert varetekst giver en reklamation, som nogen skal besvare. '
           'Derfor starter jeg med felterne og ejerskabet: hvad er obligatorisk, hvem må ændre hvad, og hvordan '
           'beviser vi, at det er kontrolleret. Først derefter giver det mening at tale om automatisering.', after=80)

    m.section('FLOWET MELLEM SALG, INDKØB OG LAGER')
    m.para('Salg, kundeservice, indkøb og lager spørger om de samme ting hver dag — og de spørger, fordi de ikke ved, '
           'hvornår de får svar. Den mest effektive forbedring er sjældent en ny proces, men en aftale: hvad kan de '
           'forvente af teamet, og hvornår. Med en synlig kø, en fast svartid og en navngivet person på hver type '
           'sag falder antallet af rykkere, og teamet får arbejdsro til det, der kræver koncentration.', after=80)

    m.section('SOM BINDELED TIL PRODUCT MANAGERS')
    m.para('Værdien af assistentteamet måles i sidste ende hos Product Managers: får de det, de skal beslutte efter, '
           'eller får de en fil, de selv skal grave i? Derfor vil jeg aftale en fast ugentlig kontaktflade pr. '
           'produktområde, en form for sag der altid kommer med en anbefaling og ikke bare et spørgsmål, og et '
           'kort grundlag ved afvigelser — hvad er problemet, hvor mange varer og kunder rammer det, hvad koster '
           'det, og hvilke muligheder er der. Det er den slags arbejde, der gør et assistentteam til noget, '
           'forretningen bruger aktivt i stedet for noget, den går uden om.', after=80)

    m.section('TEAMET PÅ TRE')
    m.para('Tre personer er nok til at løse opgaverne og for lidt til at tåle, at én er væk. Så jeg investerer i det, '
           'der gør holdet bredt: en kompetencematrix, der viser hvem der kan hvad, skriftlige arbejdsgange på det '
           'sjældne, oplæring i hinandens opgaver i fredstid, og en fast daglig eller ugentlig kontaktflade, hvor '
           'prioriteter bliver justeret, før de bliver et problem. 1:1 hver fjortende dag og feedback tæt på opgaven '
           'er ikke et personaleprogram; det er den måde, en lille enhed bliver ved med at være fleksibel.', after=80)

    m.section('KATALOG OG KAMPAGNER UDEN FEJL')
    m.para('Kampagner og kataloger er de steder, hvor en datafejl bliver dyr, fordi den rammer mange kunder på én '
           'gang. Derfor en fast tjekliste før publicering — priser og kampagneperioder kontrolleret mod aftalen, '
           'alternative varer på plads, billeder og indhold i den rigtige kvalitet, og prislister løftet korrekt til '
           'både lokalt og hovedkontor-niveau. Det arbejde er kedeligt, når det lykkes, og meget synligt, når det '
           'ikke gør — og det er præcis derfor, det skal ligge i en rutine og ikke i hukommelsen.', after=80)

    m.section('MÅL OG OPMÆRKSOMHEDSPUNKTER')
    m.para('Jeg vil følge fem tal: gennemløbstid pr. anmodning, andel sager løst inden for aftalt tid, fejl fundet '
           'efter publicering, andel produkter med komplette data, og hvor mange opgaver der kan løses af mere end '
           'én person. De kan alle trækkes ud af systemerne uden nyt værktøj, og de fortæller tilsammen, om teamet '
           'bliver hurtigere og mindre sårbart — ikke bare travlere. Dem rapporterer jeg månedligt på én side til dig '
           'og til Product Managers: hvad gik godt, hvad gik galt, og hvad ændrer vi.', after=80)

    m.section('DIGITALT ARBEJDE MED ET KLART FORMÅL')
    m.para('Jeg bruger Python og Claude til at trække lister ud og sammenligne dem: priser mod aftalte priser, '
           'produkter mod obligatoriske felter, fakturaer mod ordrebekræftelser, og produktdata mod det, der ligger '
           'i katalog og webshop. Det erstatter ikke SAP eller STEP, og det sker inden for jeres systemer og '
           'godkendelser — men det gør en kontrol, der ellers tager en dag, til noget der tager en time, og det er '
           'forskellen på at kontrollere alt og at kontrollere det, der betyder noget.', after=80)

    return m.save(path, title='Ansøgning og CV — Product Manager Assistant Team Lead, Lyreco',
                  subject='Produktdata, datakvalitet og teamledelse i Product Marketing',
                  keywords='product manager assistant, team lead, SAP, STEP, Zendesk, produktdata, Excel, datakvalitet')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Lyreco_ProductManagerAssistantTeamLead.docx')))
