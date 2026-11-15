# -*- coding: utf-8 -*-
"""NRGi Rådgivning — Seniorrådgiver, energimærkning (Valby / Aarhus).

Dansk leverance (opslaget er dansk): motiveringsside + CV i ét dokument.
Kultur- og rolleintel: master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md (NRGi-afsnit).
Policy: master/README.md — ekstrem sikkerhed, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Seniorrådgiver · Energimærkning, udbud og bygningsdata'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('5. november 2026')
    m.meta('NRGi Rådgivning · Valby · Seniorrådgiver, energimærkning')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Seniorrådgiver inden for energimærkning', bold=True, color='1A1A1A')
    m.para('Til afdelingsleder Dennis Nedergaard', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('Et energimærke er ikke et stempel. Det er en beslutning om, hvor pengene skal lægges næste år — og i '
           'en kommune med hundreder af bygninger bliver den beslutning truffet hundreder af gange på ét budget. '
           'Derfor er det sjældent selve mærket, der er det svære. Det svære er at få data, krav, udbud og '
           'leverance til at pege samme vej, så kunden kan træffe en beslutning, der holder i ti år. Det er den '
           'opgave, jeg søger hos NRGi Rådgivning — stillingen, der kombinerer energimærkning, '
           'udbudsrådgivning, projektledelse og energiteknisk rådgivning, er præcis den kombination, jeg har '
           'arbejdet i.', after=80)

    m.para('**Jeg vil løse den på fire faste ting.** Først **data før dom**: forbrug, bygningsdele, installationer '
           'og en sammenligning på tværs af porteføljen, så vi ved, hvor energien faktisk forsvinder, og hvilke '
           'bygninger der skal have indsatsen først. Analysen skal ende i et beslutningsgrundlag, ikke i en '
           'rapport, der lægges i en skuffe. Dernæst **udbuddet som styringsværktøj**: en kravspecifikation der '
           'beskriver den leverance, vi faktisk vil have, tildelingskriterier der belønner kvalitet og ikke kun '
           'pris, og kontraktvilkår der hænger sammen med det, der bliver leveret bagefter. Så '
           '**kvalitetssikringen**: kendte fejltyper, stikprøver og ensartethed på tværs af rådgivere og '
           'leverandører, så kvaliteten af et energimærke ikke afhænger af, hvem der tilfældigvis var på sagen. Og '
           'endelig **kunden som beslutningstager**: teknik oversat til økonomi og prioritering, i et sprog både '
           'politikere, driftsfolk og leverandører kan handle på — med interesse­håndtering og fremdrift, når der '
           'er mange parter.', after=80)

    m.para('Jeg har prøvet alle fire dele med ansvar for resultatet. På **Biofos, Lynetten** var jeg i fem år '
           'drifts- og vedligeholdelsesleder på et af landets største anlæg: jeg arbejdede med energiledelse og '
           'energioptimering på store bygnings- og anlægsmasser, hentede data fra SCADA og målere, fandt hvor '
           'forbruget sad, og gennemførte tiltag der samlet gav **over 40 % lavere energiforbrug** — dokumenteret '
           'og fastholdt, ikke et engangsprojekt. Det er præcis den bevægelse, et energimærke skal sætte i gang: '
           'fra måling til handling til effekt. Hos **Novo Nordisk** løftede jeg 37 samtidige kapitalprojekter med '
           '25 specialister og 2–10 mio. kr. pr. projekt: kravspecifikationer og acceptkriterier, leverandør- og '
           'kontraktstyring, beslutningsgrundlag til ledelse og bygherre og auditeret aflevering med **nul kritiske '
           'fund**. I **Ventek-Air** var jeg projekt- og værkstedsleder for 14 medarbejdere og 11 samtidige '
           'projekter med tilbud, kalkuler og underleverandører, og i **ELOHVAC**, som jeg har drevet siden 2023, '
           'har jeg fuldt P&L med fem håndværkere og tre lærlinge: tilbud, kontrakter, indkøb og kundedialog i '
           'samme hverdag.', after=80)

    m.para('Det faglige grundlag er bygningerne og installationerne. Jeg er **elautoriseret maskinmester** med '
           'B.Tech i Technology Management & Mechanical Engineering: varme, ventilation, sanitet, køl og el er '
           'uddannelsens kerne, og elautorisationen på LV, MV og HV betyder, at jeg kan vurdere både '
           'installationerne og den elektrificering, der er svaret på en stor del af energimærkningens '
           'anbefalinger — varmepumper, el til rumvarme og varmt vand, styring og last. Jeg læser en '
           'tilstandsrapport, et el- og varmeregnskab og en driftsteknisk dokumentation og kan se, om tallene '
           'hænger sammen med bygningen.', after=80)

    m.para('Offentlige bygherrer rådgiver jeg for med respekt for, at beslutningen ikke er teknisk, men politisk. '
           'En kommune skal kunne forklare borgerne, hvorfor netop denne skole og ikke den anden blev renoveret '
           'først — og derfor skal analysen være dokumenteret, prioriteringen være begrundet, og usikkerheden være '
           'skrevet ind i oplægget i stedet for at dukke op i byggefasen. De krav, der kommer med EED og EPBD, '
           'gør det ikke nemmere: de rammer mange bygninger på én gang og skal omsættes til en rækkefølge og et '
           'budget. Netop den omsætning er rådgivningens kerne, og det er der, jeg gerne vil være med.', after=80)

    m.para('NRGi taler om at være mere end en leverandør — og om EED og EPBD som de krav, kunderne skal forstå, '
           'prioritere og håndtere. Det er samme rolle, jeg har haft før: den, der oversætter krav til '
           'beslutninger og bliver hængende, til leverancen er i hus. Jeg deler også jeres mission: elektrificering, lavere CO2 '
           'og et klimaneutralt samfund er ikke et budskab for mig, men det arbejde med grøn omstilling, jeg har lavet i '
           'femten år — først som driftsleder på et anlæg, hvor energi var en driftsomkostning, siden som leverandør, hvor '
           'energi var det, kunden betalte for. **"Ingen skaber forandring alene"** passer præcist på den slags '
           'opgaver: et energimærke bliver kun til noget, hvis rådgiver, kunde, driftsfolk og leverandør trækker '
           'samme vej.', after=80)

    m.para('Praktisk: jeg bor i Måløv, har omkring en halv time til Valby og arbejder gerne både fra kontoret, hos '
           'kunden og hjemmefra — den fleksibilitet og mulighed for hjemmearbejde, jeres opslag beskriver, passer '
           'godt til den måde, jeg arbejder på, og jeg dækker også Aarhus-kontoret, når opgaven kræver det. Dansk '
           'er modersmål, engelsk er professionelt, og jeg kan starte efter aftale. Jeg vil gerne høre, hvilke '
           'kommuner og porteføljer teamet arbejder med lige nu, og hvordan I i dag kvalitetssikrer energimærker '
           'på tværs af leverandører — så ved jeg, hvor jeg kan bidrage fra første uge.', after=70)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Senior rådgiver og projektleder med 20+ års erfaring fra energi, tekniske installationer og store '
           'bygnings- og anlægsmasser — elautoriseret maskinmester med B.Tech i Technology Management & Mechanical '
           'Engineering. Fem år som drifts- og vedligeholdelsesleder på et af landets største anlæg med '
           'energiledelse og over 40 % lavere energiforbrug som dokumenteret resultat; 37 samtidige '
           'kapitalprojekter med 25 specialister, kravspecifikationer, leverandør- og kontraktstyring og nul '
           'kritiske fund; 14 medarbejdere og 11 samtidige projekter i ventilation og tekniske installationer; egen '
           'virksomhed med fuldt P&L, tilbud og kontrakter. Analyserer bygninger og data, omsætter krav til '
           'beslutningsgrundlag og holder sammenhængen mellem teknik, økonomi og kontrakt.', after=80)

    m.section('ENERGIMÆRKNING, UDBUD OG RÅDGIVNING')
    for label, body in [
        ('Dataanalyse og beslutningsgrundlag',
         'Forbrugs- og driftstal brudt ned på bygning, system og måler; sammenligning på tværs af portefølje, '
         'prioritering efter effekt og risiko, og et beslutningsgrundlag der kan læses af en politiker og bruges '
         'af en driftsleder.'),
        ('Udbud og kravspecifikation',
         'Kravspecifikation, tildelingskriterier og kontraktvilkår udformet, så de styrer leverancen; '
         'tilbudsvurdering, forhandling og kontraktopfølgning fra egen virksomhed og fra 37 kapitalprojekter med '
         'eksterne leverandører.'),
        ('Kvalitetssikring',
         'Kendte fejltyper, stikprøver og ensartethed på tværs af rådgivere og leverandører; afvigelser lukket '
         'med årsag og dokumentation, og auditeret aflevering med nul kritiske fund under GMP/FDA/EMA.'),
        ('Energiteknisk rådgivning',
         'Varme, ventilation, sanitet, køl og el i bygninger og anlæg; energiledelse, måling og verifikation, '
         'elektrificering af varme og styring — med elautorisation på LV, MV og HV.'),
        ('Projektledelse og interessenter',
         '37 parallelle projekter med 25 specialister i en organisation med mange parter; mødeledelse, '
         'beslutningslog, fremdrift og rapportering til ledelse, bygherre og leverandør.')]:
        m.bullet(label, body, after=25)

    m.models_table('VÆRKTØJER OG METODER', ('Opgave', 'Værktøj og dokumenteret brug'), [
        ('Energi og data',
         'Målinger og driftstal fra SCADA og målere, normalisering og sammenligning mellem bygninger, beregning af '
         'effekt og tilbagebetalingstid; dokumenteret 40 % reduktion på Biofos.'),
        ('Bygning og installation',
         'Varme, ventilation, sanitet, køl og el; tilstandsvurdering af bygningsdele og installationer, '
         'driftsteknisk dokumentation og elautorisation LV/MV/HV.'),
        ('Udbud og kontrakt',
         'Kravspecifikation, acceptkriterier og tildelingsmodel; udbudsmateriale, tilbudsevaluering, kontrakt og '
         'opfølgning på leverance — i egen virksomhed og i kapitalprojekter.'),
        ('Kvalitet og dokumentation',
         'Kontrollister og stikprøver, afvigelseshåndtering med rodårsag og lukning, sporbarhed fra krav til '
         'levering og audit trail der kan læses af andre.'),
        ('Projekt og portefølje',
         'Én plan pr. sag med milepæle, ansvar og beslutningspunkter; porteføljeoversigt med fremdrift, risiko og '
         'ressourcer, rapporteret i fast rytme.'),
        ('Digitale værktøjer',
         'Python, Claude API, SAP og Excel: analyser, normalisering af forbrugsdata, KPI-tavler og '
         'beslutningsoplæg — over 40 % af det administrative arbejde fjernet i egen virksomhed.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 håndværkere og 3 lærlinge · fuldt P&L · private og erhvervsmæssige kunder',
         [('Rådgivning og salg', 'Tilbud, kalkuler, kontrakter og kundedialog; tekniske løsninger vurderet, '
                                 'prioriteret og prissat sammen med kunden.'),
          ('Økonomi og ledelse', 'Budget, dækningsgrad, indkøb og leverandøraftaler; rekruttering, MUS og '
                                 'oplæring af lærlinge.')]),
        ('Senior commissioning engineer / projektleder, elsystemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Krav, kontrakt og leverance', 'Kravspecifikation og acceptkriterier, leverandør- og kontraktstyring, '
                                          'beslutningsgrundlag til ledelse og bygherre; nul kritiske fund ved '
                                          'auditeret aflevering.'),
          ('Rapportering og risiko', 'Status, tid, økonomi og risiko rapporteret månedligt; grænseflader mod '
                                      'andre fag og leverandører styret.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige projekter · 2–10 mio. kr. pr. projekt',
         [('Tilbud og projekter', 'Tilbud, kalkuler, underleverandører og afleveringspakker i ventilation og '
                                   'tekniske installationer; daglige tavlemøder og flaskehalsanalyse.')]),
        ('Drifts- og vedligeholdelsesleder / værkstedsassistent',
         'Biofos, Lynetten · København · aug. 2017–jan. 2022',
         '24/7-anlæg · energiledelse · vand, varme, ventilation, trykluft, højspænding og SCADA',
         [('Energioptimering', 'Energiledelse på store bygnings- og anlægsmasser: data fra målere og SCADA, '
                               'identifikation af de største forbrug, tiltag prioriteret efter effekt — samlet over '
                               '40 % lavere energiforbrug, dokumenteret og fastholdt.'),
          ('Drift, myndighed og dokumentation', 'Skiftplanlægning, tilsyn og forebyggende vedligehold; '
                                                'arbejdsmiljø, myndighedskrav og miljødokumentation i et anlæg, '
                                                'der ikke måtte stoppe.')]),
        ('Elektromekaniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · industrielt udstyr',
         [('Teknisk analyse', 'Fejlfinding, rodårsagsanalyse og korrigerende handlinger på produktionsudstyr; '
                              'vagtplanlægning og opfølgning på mål.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('UDDANNELSE OG AUTORISATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering',
          'Maskinmesterskolen København · 2017–2022 · gennemsnit 7,6/12')
    m.edu('Autoriseret maskin- og elinstallatør (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('El- og maskinkonstruktion, elektroteknik',
          'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Køle- og ventilationsteknik · STCW sikkerhed og maskinvagt',
          'Mercantec 2021 · Søfartsstyrelsen 2021–2023')

    m.section('SPROG, PRAKTIK OG REFERENCER')
    m.para('Dansk: modersmål · Engelsk: professionelt · Persisk: modersmål · Kørekort B · Bor i Måløv, ca. en halv '
           'time fra Valby, og arbejder gerne fra kontoret, hos kunden og hjemmefra · Kan starte efter aftale · SAP '
           'og Excel samt Python i daglig brug · Referencer fra Novo Nordisk, Biofos, Ventek-Air samt kunder og '
           'leverandører i egen virksomhed på forespørgsel.', after=70)

    m.models_table('DET EFTERSPØRGER DE — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Erfaring med energimærkning af større bygninger og bygningsporteføljer',
         'Fem år med energiledelse og energioptimering på store bygnings- og anlægsmasser på Biofos: data fra '
         'målere og SCADA, analyse af bygningsdele og installationer, prioritering på tværs af portefølje og over '
         '40 % lavere forbrug; byggefaglig og installationsteknisk uddannelse som grundlag.'),
        ('Energikonsulent II — kendskab til energimærkningsordningen',
         'Maskinmester med varme, ventilation, sanitet, køl og el som kernefag, dokumenteret arbejde med '
         'bygningers energimæssige tilstand og installationer, samt kendskab til de krav EED og EPBD stiller til '
         'bygningsejere og offentlige bygherrer.'),
        ('Projektledelse af komplekse forløb',
         '37 parallelle kapitalprojekter med 25 specialister og 2–10 mio. kr. pr. projekt; 11 samtidige projekter '
         'med 14 medarbejdere; fuldt P&L og projektansvar i egen virksomhed.'),
        ('Udbud og kontraktuelle forhold',
         'Kravspecifikationer, acceptkriterier og tildelingskriterier; udbudsmateriale, tilbudsevaluering, kontrakt '
         'og opfølgning på leverance — i kapitalprojekter med eksterne leverandører og i egen virksomhed.'),
        ('Kravspecifikationer og beslutningsgrundlag',
         'Krav dokumenteret fra krav til test og levering, med sporbarhed; beslutningsoplæg til ledelse og '
         'bygherre med teknik, økonomi og risiko i samme billede.'),
        ('Analyse af bygninger, data, risici og muligheder',
         'Normalisering af forbrugsdata og sammenligning mellem bygninger og systemer; risikoregister og '
         'prioritering efter effekt og tilbagebetalingstid; over 40 % reduktion realiseret, ikke kun beregnet.'),
        ('Kvalitetssikring af energimærker og leverancer',
         'Kontrollister, stikprøver og afvigelseshåndtering med rodårsag og lukning; auditeret aflevering med nul '
         'kritiske fund under GMP/FDA/EMA.'),
        ('Systematisk tilgang og overblik i komplekse sager',
         'Én plan pr. sag med milepæle, beslutningspunkter og ansvar; porteføljeoversigt med fremdrift og risiko '
         'og fast rapporteringsrytme — også når der er mange parter og skiftende krav.'),
        ('Ejerskab og videndeling',
         'Ejeransvar for egne sager og resultat fra egen virksomhed; metoder og skabeloner delt med kolleger, og '
         'oplæring af lærlinge og nye medarbejdere som fast del af ledergerningen.'),
        ('Rådgivning og sparring for kunder, kolleger og leverandører',
         'Kundedialog og teknisk rådgivning i egen virksomhed; sparring med ledelse, bygherre, leverandører og '
         'myndighed i pharma- og forsyningsprojekter; oplæring og videndeling med kolleger.')])
    m.page_break()

    m.models_table('DE FØRSTE 90 DAGE — DATA, UDBUD OG LEVERANCE', ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'Ind i de kørende sager: læs udbudsmateriale, kravspecifikationer og kvalitetssikringsbillede for de '
         'porteføljer, teamet arbejder med. Mød to kunder og se en bygning fra mærkning til anbefaling. Lær '
         'jeres metoder og skabeloner, før jeg foreslår ændringer.'),
        ('Dag 30',
         'Jeg driver en sag selv fra analyse til beslutningsgrundlag: data normaliseret, de største forbrug og '
         'risici identificeret, og et oplæg kunden kan beslutte på. Ét forbedringsforslag til skabelon eller '
         'kravspecifikation fremlagt for teamet.'),
        ('Dag 60',
         'Et udbud gennemført eller kvalitetssikret med mig som ansvarlig: kravspecifikation, tildelingskriterier '
         'og kontrakt hænger sammen, og kvalitetssikringen er skrevet ind fra start. Stikprøver på leverede '
         'energimærker dokumenteret.'),
        ('Dag 90',
         'Jeg er kundens faste sparringspartner på mine sager og kan løfte rådgivningsforløb alene fra første '
         'analyse til endelig leverance. Teamet har mindst én metode, skabelon eller kontrol, der er blevet bedre af, at jeg '
         'kom — og det kan ses i næste udbud.')])

    m.section('ET MÆRKE ER EN BESLUTNING')
    m.para('Et energimærke beskriver en bygning, men det bliver brugt som et budgetværktøj. Derfor skal mærket '
           'være præcist nok til at bære en investeringsbeslutning: hvilke bygningsdele trækker ned, hvilke '
           'installationer kan skiftes med tilbagebetalingstid, og hvad er rækkefølgen, hvis man kun har råd til en '
           'tredjedel i år. Det er den oversættelse, jeg ser som rådgiverens vigtigste arbejde — og den kræver, at '
           'man både kan læse data og forstå bygningen.', after=80)

    m.section('DATA ER GRUNDLAGET — OGSÅ NÅR DET ER UBEKVEMT')
    m.para('Energidata lyver sjældent, men de fortæller ikke altid sandheden: et forbrug kan se lavt ud, fordi '
           'bygningen står tom, og højt, fordi en styring er sat forkert. Jeg normaliserer, før jeg konkluderer, og '
           'jeg skriver antagelserne ned, så kunden kan se, hvad tallet hviler på. På Biofos var de 40 % ikke et '
           'heldigt år, men et resultat af at måle, prioritere og følge op — og det er den samme disciplin, et '
           'energimærke skal kunne tåle at blive målt på bagefter.', after=80)

    m.section('UDBUD SKAL KUNNE STYRE LEVERANCEN')
    m.para('Et udbud er ikke et dokument, der skal overstås; det er den kontrakt, der afgør, om vi får et godt '
           'energimærke om seks måneder. Derfor skal kravspecifikationen beskrive den leverance, vi vil have — '
           'metode, dokumentation, kvalitetssikring og frister — og tildelingskriterierne skal belønne det, der '
           'betyder noget for kunden, ikke kun den laveste timepris. Jeg har siddet på begge sider af bordet: som '
           'leverandør, der bød ind, og som køber, der skulle vurdere tilbud og holde leverandøren fast på '
           'aftalen.', after=80)

    m.section('KVALITET PÅ TVÆRS AF RÅDGIVERE')
    m.para('Kvaliteten af et energimærke må ikke afhænge af, hvem der tilfældigvis var på sagen. Derfor vil jeg '
           'arbejde med kendte fejltyper, stikprøver og en fast kontrol før levering — og med at dele dem, så hele '
           'teamet og leverandørerne bliver bedre. Det er samme tilgang som i pharma-projekterne, hvor en '
           'manglende underskrift stopper en frigivelse: kontrollen skal være indbygget, ikke tilføjet til sidst.', after=80)

    m.section('KUNDEN SKAL KUNNE BESLUTTE')
    m.para('Kommuner og offentlige bygherrer har mange interessenter og et budget, der skal forsvares politisk. '
           'Derfor skal rådgivningen ende i et oplæg, der kan besluttes: tre prioriterede indsatser, hvad de '
           'koster, hvad de giver, og hvad der sker, hvis man venter. Jeg har lavet den slags oplæg til ledelse og '
           'bygherre i 37 projekter, og jeg ved, at det er formatet — ikke analysens dybde — der afgør, om '
           'beslutningen bliver taget.', after=80)

    m.section('ELEKTRIFICERINGEN KRÆVER TAL')
    m.para('NRGis mission er elektrificering og et klimaneutralt samfund, og i bygninger betyder det varmepumper, '
           'el til rumvarme og varmt vand, styring og fleksibelt forbrug. Jeg har elautorisation på LV, MV og HV og '
           'har arbejdet med både varmesystemer, ventilation og styringer — så jeg kan vurdere, om løsningen '
           'teknisk kan lade sig gøre, om den kan betale sig, og hvordan bæredygtighed bliver et regnestykke '
           'frem for et slide. Det er den kombination, et godt energimærke og et '
           'godt udbud kræver.', after=80)

    m.section('FLEKSIBILITET OG SAMARBEJDE')
    m.para('Jeg arbejder godt med stor fleksibilitet, fordi jeg er vant til at styre min egen tid efter kunder og '
           'deadlines, og fordi jeg har drevet en virksomhed, hvor dagen sjældent blev som planlagt. Et mindre, '
           'fagligt erfarent team passer mig godt: der, hvor man bruger hinanden som sparringspartnere, bliver '
           'kvaliteten bedre for alle — og det er den kultur, jeres opslag beskriver.', after=80)

    return m.save(path, title='Ansøgning og CV — Seniorrådgiver, energimærkning, NRGi Rådgivning',
                  subject='Energimærkning, udbud og bygningsdata for offentlige bygherrer',
                  keywords='energimærkning, udbud, kravspecifikation, energiledelse, bygningsportefølje, '
                           'kvalitetssikring, EED, EPBD')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_NRGi_Seniorraadgiver.docx')))
