# -*- coding: utf-8 -*-
"""Entreprenør Otto Chrestensen A/S, Arnum/Gram — Projektchef (via Career | a JKS Company).
Dansk opslag -> dansk dokument.

Form (master/FORMKATALOG.md): åbning **AA** (to gravemaskiner i den ene grøft og ingen i den anden — det er
fordelingen fra i sidste uge, ingen så efter i tirsdags), struktur **Fire steder, pengene afgøres**
(tilbuddet · planen · udførelsen · afleveringen), register **Mandskabstavlen** (tavle, sjak, sag, uge,
maskine, formand, lærling, omflytning, ferie, reserve). Kulturfil: jd/OttoChrestensen_Projektchef_kultur.txt.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Projektchef · personale, produktion og anlæg'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('14. november 2026')
    m.meta('Entreprenør Otto Chrestensen A/S · Projektchef · Arnum ved Gram · via Career | a JKS Company')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Projektchef', bold=True, color='1A1A1A')

    def lp(text, after=40):
        return m.para(text, after=after, line=234)

    # ---------------------------------------------------------------- side 1
    lp('**Der står to gravemaskiner i den ene grøft og ingen i den anden. Det er ikke maskinernes skyld, og '
       'sjældent formandens — det er fordelingen, der blev lavet i sidste uge, og som ingen så efter i '
       'tirsdags.** Anlægsarbejde er ikke svært at forstå. Det er svært at holde fordelt: folk, maskiner, uger '
       'og de tilladelser, der altid kommer en dag senere, end planen regnede med.', after=34)

    lp('Stillingen her er netop den fordeling — **ansvar for personale og produktion**, en **faglig og '
       'ledelsesmæssig sparringspartner for entrepriselederne og ledelsen**, og **egne projekter i mindre '
       'omfang**, så man ikke glemmer, hvad det er, man fordeler. Jeg kommer fra entreprenørarbejde i el og '
       'ventilation, ikke fra jord og kloak; det står længere nede, så det ikke først opdages i en samtale.',
       after=30)

    lp('**Fire steder, pengene afgøres.**', after=24)

    lp('**Tilbuddet.** Enhedspris gange mængde — plus det, ingen tilbudsliste viser: jordarterne, vandet i '
       'grøften, adgangsforholdene, og hvem der står med folkene i uge 41. Jeg har regnet og afgivet tilbud med '
       'egen margin på spil siden 2023. Det er ikke kloakkalkuler, men det er samme disciplin: kender jeg ikke '
       'mængden, sætter jeg en risiko ind i stedet for et håb — og skriver den ned, så nogen kan spørge til '
       'den.', after=22)

    lp('**Planen.** Tavlen i skurvognen: hvem, på hvilken sag, i hvilken uge, med hvilken maskine — og hvad der '
       'sker, når en mand bliver syg, eller en gravetilladelse kommer for sent. 11 samtidige anlæg og 14 '
       'montører var min udgave af den tavle; her hedder kolonnerne **sjak**, **formand** og materiel, og '
       'princippet er det samme: en **kapacitet**, der er skrevet ned, kan flyttes. En, der kun findes i hovedet '
       'på to mand, kan ikke.', after=22)

    lp('**Udførelsen.** **Fremdrift** mod plan og dækningsgrad på sagen — to tal om ugen, og en samtale om dem, '
       'før der er en konflikt. **Kvalitet** og **sikkerhed** er ikke en tredje samtale, men en del af den '
       'samme: en grøft er farlig hver gang, uanset hvor mange gange man har gravet den, og en **mangel**, der '
       'opdages af tilsynet i stedet for af os, er dyrere end den, vi selv fandt i tirsdags.', after=22)

    lp('**Afleveringen.** Mangellister, dokumentation, garanti — og den **tillægssag**, der aldrig blev skrevet '
       'ned, fordi ingen havde lyst til at tage samtalen i uge 12. Det er her, et godt projekt bliver et dårligt '
       'renommé. 37 afleveringer med nul kritiske afvigelser lærte mig rækkefølgen: dokumentér undervejs, luk '
       'manglerne mens folkene stadig er på pladsen, og afslut med et skriftligt »det her stod vi tilbage med«.',
       after=28)

    lp('**Hvorfor et familieejet firma.** I en virksomhed af jeres størrelse betyder en dårlig uge noget andet '
       'end i en koncern: der er ingen HR-afdeling, der tager samtalen, og ingen indkøbsafdeling, der finder den '
       'maskine, der står stille. Jeg har selv drevet en virksomhed med otte ansatte og egen ordrebog, og det er '
       'den verden, jeg kender bedst — hvor beslutningen og regningen ligger samme sted, og hvor man ikke kan '
       'gemme sig bag en proces.', after=26)

    lp('**Hvor min erfaring er smallere, sagt ligeud.** Jeg har ikke arbejdet i **anlægsbranchen**, ikke udført '
       '**jord**- eller **kloak**entrepriser og ikke stået i **hovedentreprise** for kommuner og '
       '**forsyningsselskaber**. Til gengæld har jeg siddet på den anden side af bordet: Biofos, Danmarks '
       'største spildevandsvirksomhed, ejet af 15 kommuner, hvor jeg var drifts- og vedligeholdelseschef på '
       'Lynetten i fire et halvt år — pumper, transmissionsledninger, tavleanlæg, 24/7-drift og tilsyn. Jeg ved, '
       'hvad en **kommune** og et forsyningsselskab spørger om, og hvad der bliver lagt mærke til, når sagen '
       'skal afleveres.', after=28)

    lp('**Om rollen og kulturen.** I søger en, der kan **skabe retning og få samarbejdet til at fungere** — og '
       'som sikrer, at **ressourcerne er fordelt rigtigt**, og **skaber rammerne for, at medarbejderne kan '
       'lykkes med deres opgaver**. I beskriver en **familieejet entreprenørvirksomhed gennem generationer**, '
       'hvor **solid erfaring møder nye kræfter**, og hvor der er fokus på **faglig udvikling og uddannelse af '
       'kommende kolleger**. I søger en leder, der er **tilgængelig og tydelig**, som **tilpasser din støtte til '
       'den enkelte medarbejders erfaring og behov** — **den erfarne kollega, den nye medarbejder og '
       'lærlingen** — og som **skaber respekt gennem din adfærd, faglighed og opfølgning**. Det er den slags '
       'leder, jeg selv har haft lyst til at gå til, og den slags, jeg prøver at være: jeg har haft 8 ansatte '
       'inklusive tre lærlinge, 14 montører og 12 teknikere, og jeg har ansat, oplært, fulgt op og sagt farvel. '
       'Jeg har **lyst til at udvikle både medarbejdere, arbejdsformer og dine egne kompetencer** — og til at '
       'kunne **skabe overblik og træffe beslutninger i en hverdag med flere samtidige opgaver** uden at '
       'glemme, at det er mennesker, der graver.', after=26)

    lp('**Praktisk.** Jeg bor i Måløv, har **kørekort B og bil**, og afstanden til Gram skal vi aftale formen på '
       '— fast base, ugentlig pendling eller flytning; det vil jeg hellere tale om i første samtale end gætte '
       'på. Dansk er modersmål, engelsk er arbejdssprog. Ansøgningen er sendt gennem det ansøgningslink, I '
       'henviser til, med CV og denne beskrivelse.', after=12)

    m.meta('Med venlig hilsen', after=6)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('**Leder med fuldt P&L i eget selskab siden 2023, tolv år i drift, entreprise og projekter — og '
           '**ledelse** af 8–25 personer.** 14 '
           'montører på 11 samtidige anlæg, 12 teknikere i et værksted, 25 specialister og 37 kapitalprojekter i '
           'reguleret industri. Elautoriseret maskinmester (LV/MV/HV), B.Tech i teknologiledelse, '
           'PRINCE2-certificeret, LEAN og Six Sigma som metoder i praksis. Bemanding, maskiner, økonomi og '
           'aflevering styret på skrift — prøvet med konsekvenser, ikke på kursus.', after=56)

    m.section('MANDskabstavlen — FIRE KOLONNER')
    for label, body in [
        ('Hvem',
         'Navn, sjak, formand og hvad den enkelte kan — ikke kun hvad der står i planen. Lærlingen skal have en '
         'svend ved siden af, ikke en vagtplan, der ligner en anden.'),
        ('Hvad',
         'Sagen, dens næste milepæl og den ene ting, der kan stoppe den i denne uge: en tilladelse, en '
         'materialelevering, en kran, en lodsejer.'),
        ('Hvornår',
         'Ugen, ikke måneden. En plan, der først bliver forkert om en måned, er allerede forkert nu, og så '
         'koster den penge i stedet for en samtale.'),
        ('Hvad hvis',
         'Reserven: hvem der rykker, hvis maskinen bryder ned, manden bliver syg, eller vandet står højere end '
         'aftalt. Står den ikke på tavlen, findes den ikke den morgen, det gælder.'),
    ]:
        m.bullet(label, body, after=16)

    m.section('TRE SAMTALER')
    for label, body in [
        ('Med den erfarne',
         'Han har gravet flere grøfter, end jeg har set. Jeg spørger, hvad han ville gøre, lytter efter '
         'forskellen på faglighed og vane — og beslutter, når vi er uenige, med begrundelsen sagt højt.'),
        ('Med den nye',
         'Den første uge er ikke en prøve, den er en introduktion: hvem der hedder hvad, hvor materialet står, '
         'hvornår man må spørge (altid) og hvad der absolut ikke er i orden (sikkerhed, dokumentation).'),
        ('Med lærlingen',
         'En lærling, der kun får de kedelige opgaver, lærer de kedelige opgaver. Fast ansvar for noget, han '
         'kan lykkes med, en svend der følger op, og en samtale hver måned om, hvad der er næste skridt.'),
    ]:
        m.bullet(label, body, after=16)

    m.section('ERFARING')
    jobs = [
        ('Ejer / teknisk direktør', 'ELOHVAC ApS · København · maj 2023–nu',
         '8 ansatte inkl. 3 lærlinge · fuldt P&L · tilbud, indkøb og leverance',
         [('Tilbud, økonomi og mennesker i samme hånd',
           'Kalkulation, **tilbud**, indkøb, leverandørforhandling og **udførelse** med **fuldt P&L**: pris, '
           'dækningsgrad og **fremdrift** besluttet og båret af mig, med **over 40 % produktivitetsløft** fra '
           'digitalt understøttede arbejdsgange.'),
          ('Lærlinge og fastholdelse',
           'Tre lærlinge ansat, oplært og fastholdt; **rekruttering**, MUS og daglig **personaleledelse** i en '
           'virksomhed, hvor sygefravær ikke kan dækkes af en ekstra kollega.')]),
        ('Medejer og CTO / teknisk ansvarlig, AI-afdelingen',
         'Data Power Consultant ApS · København · 2024–nov. 2026 (sideløbende med ELOHVAC)',
         '4–10 personer · kundeløsninger fra krav til idriftsættelse',
         [('Data, dokumentation og overdragelse',
           'Krav, datamodeller og rapporter bygget sammen med kunden, så tallene kunne bruges efter '
           'overdragelsen — **analyse** og formidling til folk uden teknisk baggrund.'),
          ('To organisationer, én plan',
           'Matrixledelse mellem to selskaber med skriftlige prioriteringsaftaler; selskabet er ophørt, og '
           'afdelingen er afviklet i ordnede former.')]),
        ('Projekt- og værkstedschef', 'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter · underentreprenører',
         [('Bemanding og materiel på tværs af 11 sager',
           'Daglig **planlægning** af 14 montører og materiel mod leveringsdatoer; **underentreprenører**, '
           'leverandører og byggemøder koordineret, så snitflader ikke blev forsinkelser — **kapacitet** flyttet '
           'mellem sager, når ugen ændrede sig.'),
          ('Kvalitet, sikkerhed og aflevering',
           'Afleveringsforretninger med mangellister og dokumentation; sikkerhed gennemgået ved opstart og '
           'opfølgning på pladsen, ikke i en mappe.')]),
        ('Drifts- og vedligeholdelseschef', 'Biofos (Lynetten) · København · aug. 2017–jan. 2022',
         'Danmarks største spildevandsvirksomhed, ejet af 15 kommuner · 24/7-drift',
         [('Spildevand, ledninger og tilsyn',
           'Drift og vedligehold af anlæg, pumper og **transmissionsledninger** samt tavleanlæg under '
           'myndighedstilsyn; hændelser og korrigerende handlinger med navngiven ejer.'),
          ('Målt effekt',
           '**Over 40 % lavere energiforbrug** gennem måling, indregulering og idriftsættelse — dokumenteret '
           'over fire år; korrigerende handlinger lukket skriftligt, også når svaret var ubekvemt.')]),
        ('Senior commissioning-ingeniør / projektleder, el',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('Aflevering som disciplin',
           '**Projektledelse** af 37 projekter med **FAT/SAT**, **IQ/OQ/PQ** og **change control**; **nul '
           'kritiske afvigelser** ved aflevering, med **dokumentation** der kunne tåle et tilsyn uden varsel.')]),
        ('Elektromekaniker / produktionsleder', 'ARJ Engineering · Tehran · dec. 2003–mar. 2010',
         '12 teknikere · maskinværksted · maskiner og udstyr',
         [('Maskiner, reservedele og oplæring',
           'Fejlfinding, kalibrering og reparation; indkøb og vedligehold af udstyr; oplæring af 12 teknikere '
           '— **arbejdsmiljø** og orden på værkstedet som daglig praksis.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=16)

    m.section('UDDANNELSE, CERTIFICERING OG AUTORISATION')
    m.edu('PRINCE2 — certificeret projektleder', 'AXELOS / PeopleCert · certifikat')
    m.edu('LEAN og Six Sigma — metoder i praksis', 'DMAIC, 5S, VSM, standard work, FMEA · ikke certificeret')
    m.edu('B.Tech, teknologiledelse og maskinteknik',
          'Copenhagen School of Marine and Technical Engineering · 2017–2022 · GPA 7,6/12')
    m.edu('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('Køle- og ventilationsteknik · AMU', 'Mercantec 2021 · STCW, Søfartsstyrelsen 2021')
    m.edu('El- og maskinteknisk design, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6')

    m.section('SPROG, IT OG PRAKTISK')
    m.para('**Dansk** (modersmål) · **engelsk** (arbejdssprog i tale og skrift) · persisk (modersmål) · '
           '**IT**: **ERP** og CMMS, **Excel** til kalkulation, bemanding og dækningsgrad, tidsplaner og '
           'mangellister, **Python** til egen analyse · **Kørekort B og egen bil** · Måløv i dag, afstanden til '
           'Gram aftales · kan starte efter aftale.', after=32)

    m.models_table('STILLINGEN SOM BESKREVET — DET TAGER JEG MED', ('Krav', 'Dokumentation'), [
        ('Solidt fundament i anlægsbranchen',
         'Ikke i **anlægsbranchen** — jeg kommer fra el- og ventilationsentreprise, hvor jeg har stået med 11 '
         'samtidige anlæg, 14 montører, underentreprenører og afleveringer. Fundamentet er entreprise, ikke '
         'jordarter.'),
        ('Erfaring med jord- og kloakarbejde',
         'Ingen udført **jord**- eller **kloak**entreprise. Jeg har været på ejersiden af **spildevand**: fire '
         'et halvt år som driftschef på Lynetten med pumper, transmissionsledninger og tilsyn.'),
        ('Forståelse for sammenhængen mellem tilbud, planlægning, udførelse og økonomi',
         'Sammenhængen er prøvet med egen regning: **tilbud** og kalkulation, **planlægning** af folk og '
         'materiel, **udførelse** og efterkalkulation — i eget selskab siden 2023 og i projektorganisationer '
         'med 25 specialister.'),
        ('Planlægge og koordinere produktionen med entrepriseledere og formænd',
         'Daglig plan for 14 montører og 11 sager, med formænd og underentreprenører i samme ugemøde; i pharma '
         'med 37 projekter og en fast kadence for fremdrift og ændringer.'),
        ('Prioritere bemanding, maskiner og øvrige ressourcer på tværs af projekter',
         '**Bemanding** og materiel flyttet mellem sager uge for uge, når datoer flyttede sig — med en '
         'skriftlig prioritering, så dem, der blev flyttet, vidste hvorfor.'),
        ('Lede medarbejdere med tydelige forventninger, løbende dialog og opfølgning',
         'Otte ansatte, 14 montører, 12 teknikere: **tydelige forventninger, løbende dialog og opfølgning** i '
         'MUS, 1:1 og på pladsen — og afskedigelser, når det var det rigtige.'),
        ('Rekruttering af medarbejdere',
         '**Rekruttering** af elektrikere, montører og lærlinge i eget selskab, inklusive opslag, samtaler, '
         'oplæring og den første måneds opfølgning.'),
        ('Sparre med entrepriselederne om fremdrift, økonomi og udfordringer på deres sager',
         'Sparring som metode: to tal om ugen pr. sag — **fremdrift** mod plan og **dækningsgrad** — og et '
         'spørgsmål, der kommer, før kunden stiller det.'),
        ('Understøtte kvalitet, sikkerhed og gode samarbejdsrelationer',
         '**Kvalitet** dokumenteret undervejs og **sikkerhed** gennemgået ved opstart og fulgt op på pladsen; '
         'samarbejde med bygherre, tilsyn og naboer holdt i gang med information, ikke med undskyldninger.'),
        ('Bidrage til at udvikle arbejdsmetoder og samarbejdet på tværs af organisationen',
         'Metoder indført, hvor de manglede: afleveringschecklister, mangellister med ejer og frist, én ugerytme '
         'og én tavle — **produktivitet** målt pr. time og **over 40 % produktivitetsløft** fra digitalt '
         'understøttede arbejdsgange.'),
        ('Egne projekter i mindre omfang',
         'Egne sager er ikke et problem: i eget selskab har jeg både solgt, planlagt og udført, og på '
         'Lynetten stod jeg selv i driften, når det brændte.'),
        ('Ansvar for personale og produktion',
         '**Ansvar for personale og produktion** har været min kerneopgave siden 2022: 14 montører og 11 sager, '
         'derefter 8 ansatte og egen ordrebog — med regningen for begge dele.'),
        ('Faglig og ledelsesmæssig sparringspartner for entrepriselederne og ledelsen',
         '**Faglig og ledelsesmæssig sparringspartner** har jeg været for projektledere, formænd og '
         'specialister: tal med på bordet, valgmuligheder og en anbefaling — ikke en holdning.'),
        ('Skabe overblik og træffe beslutninger i en hverdag med flere samtidige opgaver',
         '11 samtidige anlæg og 37 projekter i samme kalender lærte mig at beslutte med 80 % af billedet og '
         'skrive ned, hvad jeg gjorde, så beslutningen kunne laves om.'),
        ('Økonomisk forståelse og kunne udfordre og støtte entrepriselederne fagligt',
         '**Økonomisk forståelse** fra fuldt P&L: kalkulation, dækningsgrad, efterkalkulation og likviditet — '
         'og evnen til at spørge til en sag, uden at det bliver en kontrol.'),
        ('Skabe respekt gennem adfærd, faglighed og opfølgning',
         'Respekt er noget, man får af at komme igen og gøre det, man sagde — på pladsen, i mødet og i den '
         'samtale, ingen har lyst til at tage.'),
        ('Samarbejde godt på tværs og få relevante kolleger med i løsningerne',
         'Jeg **samarbejder godt på tværs** og henter hellere to kolleger ind for tidligt end én for sent: '
         'kvalitet, indkøb og projektering har siddet med ved bordet, før beslutningen blev taget.'),
        ('Lyst til at udvikle medarbejdere, arbejdsformer og egne kompetencer',
         'B.Tech taget ved siden af fuldtidsarbejde 2017–2022, maskinmesterautorisation 2023 og PRINCE2 — '
         '**lærling** én gang er ikke nok, hvis man skal lede andres læring.'),
        ('Tilgængelig og tydelig leder, der tilpasser støtten til den enkelte medarbejders erfaring og behov',
         'Den erfarne skal have ansvar, den nye skal have rammer, lærlingen skal have en svend — tre forskellige '
         'måder at lede på samme tavle, og samme krav til sikkerhed for alle tre.'),
        ('Erfaring fra arbejde med den erfarne kollega, den nye medarbejder og lærlingen',
         '8 ansatte inklusive tre lærlinge, 14 montører med vidt forskellig anciennitet og 12 teknikere i et '
         'værksted — oplæring, fastholdelse og den svære samtale har været en del af jobbet.'),
        ('Ansøgning med CV og kort beskrivelse af relevant erfaring og motivation via ansøgningslinket; løbende '
         'behandling',
         'Ansøgningen er sendt gennem det link, I henviser til, med CV og denne beskrivelse — ikke på mail, som '
         'I beder om, og sendt nu fordi I **behandler ansøgninger løbende**.'),
        ('Opgaver i Syd- og Sønderjylland med udgangspunkt i Arnum ved Gram; tiltrædelse aftales',
         '**Gram** og de syd- og sønderjyske opgaver er ikke et problem for mig — men afstanden fra Måløv skal '
         'vi aftale formen på, og det vil jeg gøre i første samtale frem for at gætte i en ansøgning.'),
    ], widths=(2500, 7846))

    m.section('DE FØRSTE 90 DAGE')
    for b in (
        'Uge 1–3: ud i marken med hver entrepriseleder og formand, på deres sager. Lær sjakkene, maskinerne og '
        'sproget — og læs de sidste sagers kalkulationer og afleveringer igennem, før jeg siger ét ord om dem.',
        'Uge 4–6: én tavle og én ugerytme, som alle sager står på: hvem, hvad, hvornår og hvad hvis — med '
        'ejerne navngivet og med de samme to tal pr. sag (fremdrift og dækningsgrad).',
        'Uge 7–10: to forbedringer valgt efter effekt, ikke efter lyst — typisk tilladelser og materialer tidligt '
        'nok, og en mangelproces der lukker, mens folkene er på pladsen.',
        'Uge 11–13: bemandings- og maskinplan for de næste tolv måneder, inkl. hvem der skal rekrutteres hvornår, '
        'og en status til ledelsen på én side.'):
        m.bullet('', b, after=14)

    m.section('DET VILLE JEG SPØRGE OM')
    for b in (
        'Hvor mange sager kører der i dag, og hvor mange entrepriseledere og formænd skal tavlen dække?',
        'Hvor bliver pengene tabt i dag — i tilbuddet, i planlægningen, i udførelsen eller ved afleveringen?',
        'Hvordan er ansvaret for produktionen fordelt i dag mellem ledelsen og entrepriselederne?'):
        m.bullet('', b, after=14)

    m.para('**Jeg kommer gerne til Gram og ser en sag, før vi taler om mig.** Kontakt: +45 93 99 95 14 · '
           'ajlooshahram@gmail.com.', after=16)

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_OttoChrestensen_Projektchef.docx')
    build(out)
    print(out)
