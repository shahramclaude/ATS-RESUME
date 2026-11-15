# -*- coding: utf-8 -*-
"""Atea Danmark — Senior Manager, Project Execution & Engagement (Ballerup).

Danish deliverable (the posting is Danish): application page + CV in one document.
Policy: master/README.md — extreme confidence, no caveats.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Senior Manager · Ledelse af erfarne specialister, kapacitet og kundeværdi'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('6. november 2026')
    m.meta('Atea Danmark · Ballerup · Senior Manager, Project Execution & Engagement')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Senior Manager, Project Execution & Engagement', bold=True, color='1A1A1A')
    m.para('Til Christina Rasch, Director, Atea Consulting', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('Hos Atea siger I, at tingene bliver sagt direkte. Så lad mig begynde der: den sværeste del af den her '
           'stilling er ikke at lede projekter. Det er at lade være. Femten erfarne projektledere og Transformation '
           '& Change Leads har ikke brug for en chef, der tager opgaven ud af hænderne på dem, når den bliver svær — '
           'de har brug for en, der gør det lettere at gøre den godt, og som tager de beslutninger, der kræver en '
           'leder: retningen, prioriteringen, mandatet og den samtale, ingen af dem skal tage alene.', after=80)

    m.para('**Jeg ville lede teamet på fire faste ting.** Først **retning, der kan gentages**: én side pr. rolle om, '
           'hvad en god leverance er, hvad mandatet er, hvornår der eskalæres, og hvad kvalitetsbarren er — så '
           'femten erfarne ikke hver især opfinder standarden, men kan måles på den samme. For det andet **kapacitet '
           'og forecasting er ledelse, ikke administration**: pipeline afstemt med Salg, bemanding pr. konsulent, '
           'tidsregistrering og fakturering som en fast månedlig rytme og udnyttelsesgraden synlig, før den bliver et '
           'problem i regnskabet. For det tredje **kundeværdi skal kunne dokumenteres**: hver større leverance har '
           'en defineret effekt og et bevis, og vi spørger kunden, om det virkede, i stedet for at antage det. For '
           'det fjerde **forandring holdes fast, når interessenter og interesser mødes**: en brændende platform, der kan forklares '
           'på to minutter, navngivne ejere, en ugentlig rytme — og den svære samtale taget direkte og tidligt, med '
           'humor som smøremiddel og ikke som undskyldning.', after=80)

    m.para('At lede specialister, der ved mere end jeg, er den ledelsesopgave jeg har løst i flest år. På **Novo '
           'Nordisk** styrede jeg **37 parallelle kapitalprojekter** med **25 højt specialiserede medarbejdere** om '
           'bordet, 2–10 mio. kr. pr. projekt, med månedlig rapportering til ledelse og bygherre og **nul kritiske '
           'fund** ved aflevering. Det var ikke mig, der tegnede den bedste løsning — det var mit ansvar, at den kunne '
           'tegnes, at ressourcer og mandat var aftalt, og at kvaliteten blev efterprøvet, før nogen '
           'skrev under.', after=80)

    m.para('Det kommercielle har jeg haft i hænderne hver dag siden 2023, hvor jeg driver **ELOHVAC** med fuldt '
           'P&L: tilbud og kalkulation, prissætning af service, kontrakt, tidsregistrering, fakturering og den '
           'månedlige opfølgning på, om det nu også gav det, vi sagde. Med **fem elektrikere og tre lærlinge** og '
           'erhvervskunder, der forventer, at telefoner bliver taget, og kunderelationer, der skal holde i mere end én '
           'ordre, er jeg vant til at måle på leverance og '
           'dækning på samme tid — og til at tage den ubehagelige snak med en kunde eller en medarbejder, inden den '
           'bliver dyrere.', after=80)

    m.para('Før det ledede jeg **14 medarbejdere og 11 samtidige projekter** i **Ventek-Air**, hvor vi indførte '
           'daglige tavlemøder, standardiserede arbejdsgange og en projektledelse, der var enkel nok til at blive fulgt, '
           'med et markant løft i leveringsevnen, og **12 '
           'teknikere** i **ARJ Engineering**, hvor oplæring og opfølgning var den daglige målestok. Og i fem år var '
           'jeg drifts- og vedligeholdelsesleder på **Lynetten under Biofos** — et kritisk anlæg i 24/7-drift, hvor '
           'forandring ikke er et projekt, men noget, der skal holde, når vagten skifter: 5S, standard work og PDCA '
           'indført indefra, med medarbejderne og ikke hen over hovedet på dem.', after=80)

    m.para('Engagement-delen af titlen tager jeg bogstaveligt. Femten erfarne medarbejdere forlader ikke en '
           'arbejdsplads, fordi opgaverne er for svære — de gør det, fordi retningen er uklar, fordi de ikke kan se, '
           'hvad deres faglighed betyder for kunden, eller fordi ingen har spurgt, hvad de synes. Så det første, jeg '
           'ville gøre, er at tage en samtale med hver enkelt om, hvad de ejer, og hvad de gerne vil være bedre til '
           'om et år. Det er billigt, det tager to uger, og det er den enkeltbeslutning, der flytter mest i et team '
           'af specialister.', after=80)

    m.para('I beskriver selv behovet som stærkere sammenhæng mellem mennesker, kundeleverancer og forretning — og det '
           'er præcis den sammenhæng, jeg har skullet bygge i alle mine lederroller. Atea er flad, og gennemslagskraft '
           'kommer ikke med titlen. Det er præcis den slags organisation, jeg '
           'trives i: hvor man skal overbevise med faglighed og relationer, hvor dialogen er direkte, og hvor der er '
           'kort fra en god idé til en beslutning. At Atea Danmark samtidig har **ISO 37001** — den højeste '
           'internationale antibestikkelsescertificering — siger noget om, hvor lidt der er til forhandling, når det '
           'gælder integritet i kundeforhold og indkøb; det er en kultur, jeg kan stå inde for uden at skulle '
           'fortolke den. Og høj faglighed kræver ikke højtidelighed. Jeg har aldrig haft behov for at være den '
           'klogeste i rummet — kun for at være den, der sørger for, at de klogeste kan arbejde.', after=80)

    m.para('Praktisk: jeg bor i Måløv, og Atea i Ballerup er omtrent ti minutter væk. Jeg taler og skriver **dansk** '
           'som modersmål og **engelsk** professionelt, og jeg kan starte hurtigst muligt eller efter aftale. Jeg vil '
           'gerne høre, hvordan I i dag følger op på kundeværdien i de største leverancer, og hvor i '
           'serviceporteføljen behovet for nye, skalerbare ydelser er størst — det er der, jeg ville begynde.', after=70)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Leder af erfarne specialister med 20+ års erfaring fra tekniske leverancemiljøer, kapitalprojekter og '
           '24/7-drift — elautoriseret maskinmester (LV/MV/HV) med B.Tech i teknologiledelse og maskinteknik. Har '
           'ledet 25 højt specialiserede medarbejdere på 37 parallelle projekter med nul kritiske fund og driver i '
           'dag egen virksomhed med fuldt P&L, tilbud, fakturering og forecasting. Coacher erfarne medarbejdere frem '
           'for at overtage deres arbejde og omsætter kundebehov til serviceydelser, der kan sælges.', after=80)

    m.section('LEDELSE AF ERFARNE SPECIALISTER OG LEVERANCER')
    for label, body in [
        ('Retning, mandat og forventninger',
         'Én side pr. rolle med hvad en god leverance er, hvad mandatet dækker, hvornår der eskalæres, og hvilke '
         'kvalitetskrav der ikke er til forhandling — samme standard for alle, så faglighed kan udfolde sig inden for '
         'en ramme, der er kendt.'),
        ('Kapacitet, forecasting og økonomi',
         'Pipeline og bemanding afstemt med salg og leveranceledelse; udnyttelsesgrad og dækning fulgt månedligt; '
         'tilbud, kalkulation, tidsregistrering og fakturering som en fast rytme, så økonomien er en ledelsesdisciplin '
         'og ikke en overraskelse.'),
        ('Kundeleverancer og dokumenterbar værdi',
         'Leverancer styret på kvalitet, økonomi og effekt med aftalte acceptkriterier og en afsluttende samtale med '
         'kunden om, hvad det flyttede; 37 kapitalprojekter afleveret med nul kritiske fund og månedlig rapportering '
         'til ledelse og bygherre.'),
        ('Forandring og følgeskab',
         '5S, standard work og PDCA indført i 24/7-drift og standardiserede arbejdsgange i et projektmiljø med 11 '
         'samtidige opgaver — forandring gennemført med medarbejderne, med en forklarlig platform og en rytme, der '
         'holder, når hverdagen presser.'),
        ('Coaching af erfarne medarbejdere',
         'MUS og 1:1 med udviklingsplaner, sparring på svære kundesager og beslutninger, og ansvar givet videre med '
         'mandat i stedet for kontrol; oplæring af lærlinge og nye medarbejdere, så kompetencen ikke hænger på én '
         'person.'),
        ('Kommerciel udvikling af services',
         'Salg, prissætning og produktificering af tekniske ydelser i egen virksomhed; kundebehov omsat til '
         'gentagelige leverancer med en defineret scope, pris og kvalitet — og tilbudsmateriale, der kan stå alene '
         'uden sælgeren i rummet.')]:
        m.bullet(label, body, after=25)

    m.models_table('VÆRKTØJER OG METODER', ('Opgave', 'Værktøj og dokumenteret brug'), [
        ('Porteføljestyring',
         '37 parallelle projekter med fælles fremdriftsbillede, risikolog, ressourceallokering og månedlig '
         'rapportering til ledelse og bygherre.'),
        ('Kapacitet og økonomi',
         'Pipeline-, bemandings- og dækningsopfølgning; tilbud og kalkulation, tidsregistrering, fakturering og '
         'månedsafslutning på eget P&L.'),
        ('Leverancemodel',
         'Acceptkriterier, stage gates, FAT/SAT og afleveringspakker; afvigelser og ændringer håndteret med ejer, '
         'dato og konsekvens for tid og økonomi.'),
        ('Forandringsledelse',
         'Brændende platform, interessentkort, navngivne ejere og ugentlig rytme; 5S, standard work og PDCA som '
         'praktisk forandringsmetode i drift.'),
        ('People leadership',
         'MUS og 1:1, udviklingsplaner, rekruttering, oplæring og sygefraværsopfølgning — samt de svære samtaler, '
         'taget direkte og tidligt.'),
        ('Data og digitalisering',
         'SAP og Excel til økonomi og opfølgning, Python og Claude til KPI-dashboards, tilbudsberegning og '
         'automatiseret rapportering med over 40 % dokumenteret produktivitetsløft.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · el-tekniske service- og entrepriseydelser',
         [('Salg, leverance og økonomi',
           'Tilbud, kalkulation og kontrakt med erhvervskunder; prissætning af service, tidsregistrering, fakturering '
           'og månedlig opfølgning på dækning og leveringsevne; dokumentationsflow og KPI-dashboards automatiseret '
           'med egne værktøjer.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Portefølje, specialister og kunde',
           'Tværfaglig ledelse af 25 højt specialiserede medarbejdere på tværs af 37 projekter; fremdrift, økonomi og '
           'risiko rapporteret månedligt til ledelse og bygherre; auditeret aflevering med nul kritiske fund.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter · 2–10 mio. kr. pr. opgave',
         [('Retning og leveringsevne',
           'Daglige tavlemøder, kapacitets- og flaskehalsanalyse og standardiserede arbejdsgange med markant løft i '
           'leveringsevne; udbud, underentreprenører og afleveringspakker styret til deadline.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Lynetten under Biofos · København · aug. 2017–jan. 2022',
         'Kritisk procesanlæg i 24/7-drift · pumper, blæsere, ventilation, transformere, koblingsanlæg og SCADA',
         [('Forandring i drift og data',
           '5S, standard work og PDCA indført på værksted og lager med medarbejderne; KPI-opfølgning på '
           'tilgængelighed, nedbrud og responstider; energiledelse med over 40 % lavere forbrug dokumenteret.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · industrielt udstyr',
         [('Oplæring og resultater gennem andre',
           'Vagtplanlægning, oplæring og opfølgning på mål for 12 teknikere; fejlfinding, rodårsagsanalyse og '
           'korrigerende handlinger på produktionsudstyr.')]),
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
    m.para('Dansk: modersmål · Engelsk: professionelt · Persisk: modersmål · Kørekort B og bil · Bor i Måløv, Atea i '
           'Ballerup ca. ti minutter væk · Kan starte hurtigst muligt eller efter aftale · SAP og Excel dagligt, '
           'Python til data og dashboards · Referencer på forespørgsel.', after=70)

    m.models_table('DET EFTERSPØRGER DE — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Dokumenteret personaleledelse og resultater gennem erfarne specialister',
         '25 højt specialiserede medarbejdere på tværs af 37 projekter; 14 medarbejdere og 11 samtidige opgaver; 12 '
         'teknikere; 5 elektrikere og 3 lærlinge med fuldt P&L — ledelse af fagligt stærke medarbejdere i fire '
         'forskellige miljøer, med opfølgning på teamets performance og trivsel.'),
        ('Erfaring med projektledere eller konsulenter',
         'Porteføljeledelse af 37 parallelle projekter med specialister som primær ressource; samarbejde med '
         'rådgivere, underentreprenører og leverandører som kravstiller og bygherre — og som sælger af egne '
         'serviceydelser.'),
        ('Ledet transformation eller væsentlige forandringer med følgeskab',
         '5S, standard work og PDCA indført i 24/7-drift; standardiserede arbejdsgange i et projektmiljø med 11 '
         'samtidige opgaver; dokumentations- og KPI-arbejde digitaliseret med over 40 % produktivitetsløft.'),
        ('Solid forståelse for projekt- og programledelse',
         'Stage gates, acceptkriterier, FAT/SAT, afleveringspakker, ændrings- og afvigelseshåndtering på 37 '
         'kapitalprojekter — brugt til at udfordre og coache, ikke til at overtage leverancen.'),
        ('Kommerciel forståelse og udvikling eller salg af professionelle services',
         'Fuldt P&L siden 2023: tilbud, kalkulation, prissætning, kontrakt, fakturering og dækningsopfølgning; '
         'serviceydelser produktificeret, så de kan sælges uden sælgeren i rummet.'),
        ('Erfaring fra consulting, IT eller viden- og leveranceintensiv organisation',
         'Tyve år i videnintensive og leveranceintensive miljøer med specialister, kunder og deadlines: '
         'kapitalprojekter i GMP-miljø, anlægsentrepriser og teknisk service — hvor værdien skabes af '
         'medarbejdernes faglighed og kundens tillid.'),
        ('Stærk kommunikation på dansk og engelsk',
         'Dansk modersmål og professionelt engelsk i skrift og tale; månedlig rapportering til ledelse, bygherre og '
         'kunder; tilbud og kontrakter skrevet, så de kan læses af en travl kunde.'),
        ('Autoritet gennem retning, troværdighed og relationer',
         'Ansvar givet videre med mandat, forventninger skrevet ned og kvalitet efterprøvet — og beslutninger taget i '
         'rummet, hvor de hører til, frem for at blive sendt opad.'),
        ('Psykologisk tryghed kombineret med høje forventninger',
         'Fejl taget op som læring i stedet for skyld i 24/7-drift og på byggepladser; høje krav fastholdt gennem '
         'tydelige acceptkriterier og opfølgning, ikke gennem kontrol.')])
    m.page_break()

    m.models_table('DE FØRSTE 90 DAGE — RETNING, KAPACITET OG KUNDEVÆRDI', ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'Individuelle samtaler med alle 15: hvad de ejer, hvad de er stolte af, hvor de går fast, og hvad de savner '
         'fra en leder. Læs de sidste kvartalsleverancer, projektporteføljen, udnyttelsesgraden og de kunder, hvor '
         'dialogen har været svær. Mød Salg og Consulting-ledelsen med samme spørgsmål.'),
        ('Dag 30',
         'Ét billede af teamet som det faktisk fungerer: kapacitet mod pipeline, hvilke leverancer der skaber '
         'dokumenterbar kundeværdi, hvor kvaliteten koster penge, og de tre steder, hvor mandat og '
         'beslutningsveje er uklare.'),
        ('Dag 60',
         'Én side pr. rolle med retning, mandat og kvalitetsbarre aftalt med teamet og Consulting-ledelsen; forecast '
         'og bemanding i fast månedlig rytme med Salg; en kort liste over services, der kan produktificeres, med ejer '
         'og første kunde.'),
        ('Dag 90',
         'Teamet måler på det samme: kundeværdi, kvalitet, udnyttelsesgrad og medarbejdertrivsel i én månedlig '
         'opfølgning; den første forandring gennemført med teamet og ikke hen over det; og en ledelseskultur, hvor '
         'den svære samtale bliver taget i tide — også når den er ubehagelig.')])

    m.section('ERFARNE MEDARBEJDERE SKAL IKKE LEDES GENNEM OPGAVER')
    m.para('Den klassiske fejl i en lederstilling som denne er at blive den bedste projektleder i teamet. Det føles '
           'nyttigt i den første måned, og i den tredje er der femten medarbejdere, der venter på, at chefen tager '
           'beslutningen, og en chef, der ikke har tid til at lede. Min opgave er en anden: sikre at mandatet er '
           'tydeligt, at standarden er kendt, at ressourcerne er der, og at den beslutning, der kræver en leder, '
           'bliver taget af mig — hurtigt og med en begrundelse, der kan gentages.', after=80)

    m.section('KAPACITET ER EN KUNDEOPLEVELSE')
    m.para('Utilstrækkelig bemanding viser sig altid hos kunden først: en projektleder, der løber for stærkt, en '
           'leverance, der glider, en faktura der kommer for sent, fordi tiden aldrig blev registreret. Derfor hører '
           'kapacitet, forecasting, tidsregistrering og fakturering hjemme i den samme månedlige rytme som '
           'kundedialogen — ikke i et regneark, der åbnes, når kvartalet er slut. Det er også den rytme, der gør det '
           'muligt at sige nej i tide og ja med overskud. Jeg har siddet med den månedsafslutning, hvor timerne ikke var '
           'registreret, og fakturaen blev sendt i sidste øjeblik — og jeg har prøvet den modsatte version, hvor '
           'tallene var der, før nogen spurgte. Det er den version, jeg vil lede efter.', after=80)

    m.section('VÆRDI SKAL KUNNE SES, IKKE BARE SIGES')
    m.para('En leverance, der er leveret til tid og pris, er ikke det samme som en kunde, der fik noget ud af den. Så '
           'jeg vil have, at større leverancer starter med et aftalt effektmål og slutter med en samtale om, hvad der '
           'faktisk flyttede sig — og at svaret kommer tilbage i porteføljen, så det næste tilbud bygger på erfaring '
           'og ikke på mavefornemmelse. Det er også den eneste måde, en serviceportefølje bliver skalerbar: man '
           'beholder det, der virker, og skærer det væk, der bare lyder godt.', after=80)

    m.section('FORANDRING HOLDER IKKE AF SIG SELV')
    m.para('En transformation, hvor interesser og perspektiver mødes, bliver ikke gennemført med et '
           'kommunikationsoplæg. Den bliver gennemført med en platform, der kan forklares på to minutter, en '
           'prioriteret liste over, hvad der skal være anderledes om 90 dage, en navngiven ejer på hver ting og en '
           'ugentlig rytme, hvor man kan se, om det skrider. Og med en leder, der bliver ved, når entusiasmen falder '
           'i uge seks — det er der, de fleste forandringer dør, og det er der, jeg har prøvet det før. Konkret betyder '
           'det, at jeg hellere tager den svære samtale med en erfaren projektleder i uge tre end opdager problemet i '
           'et kvartalsregnskab i juni.', after=80)

    m.section('HUMOR ER ET ARBEJDSREDSKAB, IKKE EN UNDSKYLDNING')
    m.para('En flad organisation med direkte dialog kræver mennesker, der kan sige det svære uden at gøre det '
           'farligt, og som kan grine af sig selv bagefter. Jeg har ledet værksteder og byggepladser, hvor tonen er '
           'rå og humoren er en del af arbejdsmiljøet, og jeg har siddet i møder i GMP-miljøer, hvor hvert ord bliver '
           'skrevet ned. Begge steder gælder det samme: man kan sige næsten hvad som helst, hvis man mener det og '
           'kommer med en løsning. Det er den slags leder, jeg er, og det er den slags kollega, jeg gerne vil være.',
           after=80)

    m.section('SALG OG LEVERANCE SKAL TALE SAMME SPROG')
    m.para('Når et salg sælger noget, leverancen ikke kan bære, betaler projektlederen regningen. Derfor vil jeg '
           'bruge tid på grænsefladen til Salg: hvad er scope, hvad er ikke, hvad er antagelserne, og hvad koster en '
           'ændring. Ikke som kontrol, men som fælles håndværk — et tilbud, der er skrevet, så det kan leveres, er '
           'den billigste kvalitetssikring, en serviceforretning har. Og når kunden kommer igen, skal det være, fordi '
           'leverancen kunne mærkes, ikke fordi rabatten var god.', after=80)

    return m.save(path, title='Senior Manager, Project Execution & Engagement — Atea Danmark',
                  subject='Ledelse af erfarne specialister, kapacitet, kundeværdi og forandring',
                  keywords='senior manager, personaleledelse, projektledelse, transformation, change, følgeskab, '
                           'kapacitet, forecasting, fakturering, kundeværdi, consulting, coaching, P&L')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Atea_SeniorManagerProjectExecution.docx')))
