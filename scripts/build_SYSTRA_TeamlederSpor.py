# -*- coding: utf-8 -*-
"""SYSTRA Danmark — Teamleder til Spor og Anlæg, Ørestad.

Opgave-først ansøgning + CV i ét dokument (masterdesign).
Kilder til kultur og fagligt indhold: se master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md,
afsnittet om SYSTRA (research 04.11.2026).
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Fagligt koordinerende teamleder · Leverancer, kvalitet og mennesker'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('4. november 2026')
    m.meta('SYSTRA Danmark · Spor og Anlæg · Julie Josefine Feddersen, afdelingschef')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Teamleder til Spor og Anlæg, København (Ørestad)', bold=True, color='1A1A1A')
    m.para('Til Julie Josefine Feddersen', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('Spor og Anlæg leverer rådgivning, hvor kvaliteten afgøres to steder: i grænsefladerne — spor mod '
           'baneafvanding, mod broer og konstruktioner, mod kørestrøm — og i kalenderen, hvor ni kolleger i Ørestad '
           'og seks i Aarhus skal levere til flere baneprojekter samtidig. Derfor handler rollen for mig om at gøre '
           'leverancerne forudsigelige. Den enkelte specialist skal vide, hvad der er vigtigst i dag. Projektlederen '
           'skal kende kapaciteten, før fristen flytter sig. Kunden skal have et svar, der holder, også når der kommer '
           'en hasteopgave ind fra siden.', after=80)

    m.para('**Systemet er allerede bygget, og det kan være i drift i løbet af de første uger.** En ugentlig '
           'leveranceoversigt pr. medarbejder og projekt — opgave, projektleder, ansvarlig, frist og næste beslutning '
           '— som vi gennemgår i et kort tavlemøde. En grænsefladematrix for spor, baneafvanding, broer og '
           'konstruktioner samt kørestrøm, så kvalitetssikring og ændringshåndtering har fast ejer og fast rækkefølge. '
           'Og en skrevet beslutningsret, så specialisterne kan træffe de faglige valg selv, og jeg kun løfter det, '
           'der kræver afdelingslederen eller kunden. Risici får et register med ejer og frist, ikke en plads i en '
           'mailtråd.', after=80)

    m.para('Personaleledelse af fem medarbejdere med høj anciennitet kræver mere lyttetid end styring. Jeg bruger '
           'situationsbestemt ledelse og delegeringstrappen til at afstemme, hvor meget retning og støtte den enkelte '
           'skal have, og 1:1 og MUS til at omsætte trivsel og ønsker til konkrete udviklingsaftaler. GROW bruger jeg '
           'som samtalemodel, når en medarbejder skal finde sin egen vej til en svær opgave, og SBI når noget skal '
           'siges ligeud og ordentligt. Kompetencerne skal stå på en kompetencematrix med to personer på hver kritisk '
           'spordisciplin, så videndeling ikke afhænger af én person. Psykologisk tryghed er i min praksis ikke en '
           'hensigt, men et spørgsmål, der kan stilles højt på et review: »Er vi sikre på den her løsning?« Mellem '
           'Ørestad og Aarhus vil jeg have en fast faglig sparringskadence og fælles metodebeskrivelser, så de to '
           'teams holder samme kvalitetsniveau.', after=80)

    m.para('Arbejdsformen er afprøvet. Hos Novo Nordisk koordinerede jeg 25 specialister på tværs af engineering, '
           'indkøb og anlæg i 37 samtidige CAPEX-projekter, fulgte økonomi og fremdrift og afleverede under GMP-krav '
           'uden kritiske afvigelser. Hos Ventek-Air styrede jeg 14 medarbejdere og 11 parallelle projekter, og hos '
           'ELOHVAC leder jeg i dag fem elektrikere og tre lærlinge med fuldt P&L-ansvar. Jeg har altså prøvet at være '
           'den, der ikke selv ejer alle fag, men ejer planen, kvaliteten og opfølgningen.', after=80)

    m.para('Ét punkt skal siges klart: spordisciplinen er ikke mit dokumenterede fag, og jeg er ikke civilingeniør. '
           'Min baggrund er B.Tech i Technology Management & Mechanical Engineering, maskinmesterretningen (EQF 6), '
           'med elautorisation LV/MV/HV. Derfor har jeg lagt en faglig indkøringsplan frem for at tale om det: '
           'sidemandsoplæring hos afdelingens sporspecialister, Banedanmarks banenormer — BN1-11 om afvanding af '
           'sporarealer, BN1-38 om sporbeliggenhed og sporgeometri, BN1-6 om tværprofiler og BN1-8 om jordarter — '
           'DS/EN 13848 om sporgeometrisk kvalitet samt de CAD- og 3D-modelleringsværktøjer, I bruger. Dag 30: kunne '
           'læse og kvalitetssikre en sporleverance sammen med en specialist. Dag 60: egne reviewbemærkninger og en '
           'første plads i videndelingen. Dag 90: repræsentere afdelingen i projektopfølgningsmøder med bygherre og '
           'entreprenør på de opgaver, hvor jeg er fagligt tryg.', after=80)

    m.para('Jeg er professionel og aktiv Claude-koder og bygger selv værktøjer i Python til KPI, kvalitetstjek, '
           'tidsplaner og investeringsmodeller med NPV, IRR og følsomhed — fx til at belyse levetids- og '
           'driftsomkostninger i et løsningsvalg med et bæredygtigt perspektiv. Innovativt i metoden, konservativt i '
           'dokumentationen. Gevinsten er administrativ: mindre tid '
           'på rutineopfølgning, mere tid til faglig dialog. Det sker inden for jeres systemer og godkendelser.', after=80)

    m.para('Jeg søger stillingen, fordi jeres tre værdier beskriver den måde, jeg arbejder på i forvejen. Excellence er kvaliteten i den leverance, '
           'der forlader huset. Connected Teams er den korte vej mellem Ørestad og Aarhus. Bold Leadership er at tage '
           'en svær prioritering, når tid og kvalitet ikke kan begge blive som ønsket — og at sige det tidligt. '
           'Ordentlighed og hjælpsomhed er nævnt som grundlaget i afdelingen, og det er også sådan, jeg leder: tydelige '
           'aftaler, ingen overraskelser og en leder, der er til at få fat i. Tillid kommer af forudsigelighed, ikke af '
           'at love mest, og jeg er pragmatisk i valget af vej — men ikke i kvaliteten af leverancen. Arbejdet i '
           'ledelsesgruppe med dig og teamlederen i Aarhus vil jeg bruge aktivt til retning, prioritering og udvikling, '
           'frem for at melde beslutninger ud bagefter.', after=80)

    m.para('Jeg vil gerne komme forbi Ørestad og gennemgå, hvordan jeg vil drive leverancer, kapacitet og '
           'kompetenceudvikling i Spor og Anlæg de første 90 dage — og høre, hvor I ser det faglige tyngdepunkt i '
           'teamet de næste par år.', after=80)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Fagligt koordinerende leder med 20+ års erfaring i teknisk anlæg, drift og personaleledelse. Har stået i '
           'spidsen for specialister i GMP-reguleret produktion, entreprise og værksted og er vant til at eje '
           'leverance, økonomi og kvalitet uden selv at eje alle fag. Arbejder datadrevet, med skrevne aftaler og '
           'tætte relationer til projektledere og kunder, og med en aktiv AI-praksis (Python, Claude) til planlægning, '
           'kvalitet og investeringsmodeller.', after=80)

    m.section('LEDELSE — ANSVAR OG RESULTATER')
    for label, body in [
        ('Mennesker og kompetencer',
         'Leder fem elektrikere og tre lærlinge hos ELOHVAC med 1:1, MUS og strukturerede oplæringsforløb. '
         'Har tidligere ledet 14 medarbejdere hos Ventek-Air og 12 teknikere i ARJ.'),
        ('Specialister uden at eje faget',
         'Koordinerede 25 specialister i engineering, indkøb og anlæg hos Novo Nordisk i 37 samtidige '
         'CAPEX-projekter på 2–10 mio. kr. og var bindeled til bygherre og leverandører.'),
        ('Leverance og kapacitet',
         'Planlagde 11 parallelle projekter hos Ventek-Air fra specifikation til aflevering. Tavlemøder og '
         'flaskehalsanalyse gjorde prioriteringer og kapacitet synlige for projektlederne.'),
        ('Kvalitet og økonomi',
         'FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA uden kritiske afvigelser ved aflevering. Fuldt P&L-ansvar hos '
         'ELOHVAC; PDCA-program reducerede energiomkostningerne med 40 % hos Novo.'),
        ('Digital praksis',
         'Professionel og aktiv Claude-koder. Python/Claude API-værktøjer til tilbud, tidsplaner, KS og KPI har '
         'givet et dokumenteret produktivitetsløft på over 40 %. Bygger investeringsmodeller med NPV, IRR og '
         'scenarier til udvikling og nye forretningsidéer.')]:
        m.bullet(label, body, after=30)

    m.models_table('LEDELSESVÆRKTØJER OG METODER', ('Opgave', 'Værktøj og dokumenteret anvendelse'), [
        ('Styre leverancer',
         'Ugentlig leveranceoversigt, tavlemøder, Gemba og visuel KPI-tavle. Brugt hos Ventek-Air (14 medarbejdere, '
         '11 projekter) og ELOHVAC.'),
        ('Udvikle medarbejdere',
         'Situationsbestemt ledelse (SLII), delegeringstrappen, 1:1, MUS/GRUS, GROW og SBI. Brugt i daglig '
         'personaleledelse hos ELOHVAC.'),
        ('Sikre kvaliteten',
         'A3, PDCA, 5 x hvorfor, Ishikawa og FMEA; kvalitetskontrol og afvigelseshåndtering. Brugt hos Novo under '
         'GMP og hos Biofos i 24/7-drift.'),
        ('Samle fag og parter',
         'Grænsefladematrix, RACI og interessentkort med beslutningsret. Brugt mellem engineering, indkøb og anlæg '
         'hos Novo samt mod underentreprenører hos ELOHVAC.'),
        ('Standardisere arbejdet',
         'Standard Work, 5S, VSM, Kaizen og kompetencematrix med to personer pr. kritisk fag. Brugt hos Biofos og '
         'ARJ.'),
        ('Risikostyring og sikkerhed',
         'Risikoregister med ejer og frist, APV, LOTO og risikovurdering ved opstart. Brugt på alle tekniske '
         'opgaver og ved pladsopstart.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L-ansvar · serviceaftaler med responstid som KPI',
         [('Personaleledelse', 'Daglig planlægning, 1:1 og MUS, oplæring af lærlinge og opfølgning på arbejdsmiljø '
                               'og trivsel på skiftende byggepladser.'),
          ('Leverance og kvalitet', 'Tilbud, beregning, materialer, underentreprenører, kvalitetskontrol og '
                                    'afleveringsdokumentation på el-, ventilations- og klimaanlæg.'),
          ('Digitale værktøjer', 'Python/Claude API til tilbud, tidsplaner, KS-tjeklister og KPI-dashboard; over '
                                 '40 % produktivitetsløft i virksomheden.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024',
         '37 samtidige CAPEX-projekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Fremdrift, risiko og grænseflader', 'Fulgte fremdrift, økonomi, risici og ressourcer mellem engineering, '
                                                'indkøb og anlæg; SAP ERP til økonomi og aktiver og månedlig '
                                                'rapportering til ledelse og bygherre.'),
          ('Kvalitet og forbedring', 'FAT/SAT og IQ/OQ/PQ uden kritiske afvigelser ved aflevering; A3 og 5 x hvorfor '
                                     'i fejlfinding; PDCA-program reducerede energiomkostningerne med 40 %.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter · DKK 2–10 mio. pr. projekt',
         [('Kapacitet og prioritering', 'Planlægning fra specifikation til formel aflevering, udbud og tilbud, '
                                        'underentreprenører og afleveringspakker. Daglige tavlemøder og '
                                        'flaskehalsanalyser gav et markant løft i leveringsevnen.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos, Lynetten · København · aug. 2017–jan. 2022',
         '24/7-drift · pumper, HVAC, højspændingstavler og SCADA · skiftehold',
         [('Tilgængelighed og standarder', 'Forebyggende vedligehold, akut fejlfinding, reservedelsflow og lager. '
                                           '5S, Standard Work og PDCA på værksted og lager; LOTO, APV og '
                                           'risikovurdering i skifteholdsdrift.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted',
         [('Plan og mål', 'Vagtplanlægning, materialestyring og målopfølgning; fejldiagnose, rodårsagsanalyse og '
                          'korrigerende handlinger på industrielt el- og mekanisk udstyr.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        m.doc.paragraphs[-1].runs[0].text = 'Omfang: '
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('UDDANNELSE OG AUTORISATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering — maskinmesterretningen',
          'Maskinmesterskolen København · 2017–2022 · EQF 6 · GPA 7,6/12')
    m.edu('El- og maskinteknisk design, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('Køleteknik og klimaanlæg · STCW-sikkerhed og maskinrumsvagt',
          'Mercantec 2021 · Søfartsstyrelsen 2021–2023')

    m.section('SPROG, PRAKTISK OG REFERENCER')
    m.para('Dansk og persisk/farsi: modersmål · Engelsk: professionelt i skrift og tale · Kørekort B · Bopæl i Måløv, '
           'ca. 30 minutter fra Ørestad · Fleksibel ved udsving i opgavemængden og vant til at holde hovedet koldt, '
           'når der skal besluttes hurtigt. Tidligere ledere hos Novo Nordisk og Biofos oplyses efter aftale.', after=70)

    m.models_table('KRAV I OPSLAGET — MIN DOKUMENTATION', ('Krav', 'Dokumentation'), [
        ('Jernbanefagligt tyngdepunkt',
         'Ikke mit dokumenterede fag. Indkøringsplan med Banedanmarks banenormer, DS/EN 13848 og '
         'sidemandsoplæring hos afdelingens sporspecialister er beskrevet nedenfor.'),
        ('Fagligt koordinerende ansvar',
         'Koordinerede 25 specialister og grænseflader mellem engineering, indkøb og anlæg i 37 samtidige '
         'CAPEX-projekter hos Novo Nordisk.'),
        ('Personaleledelse',
         'Fem elektrikere og tre lærlinge i dag, 14 medarbejdere hos Ventek-Air og 12 teknikere i ARJ. '
         '1:1, MUS, situationsbestemt ledelse og GROW i fast brug.'),
        ('Leverancer til tid og økonomi',
         'Fuldt P&L-ansvar hos ELOHVAC, 11 parallelle projekter hos Ventek-Air og SAP-baseret økonomi- og '
         'aktivistyring med månedlig rapportering hos Novo.'),
        ('Kvalitet og ændringshåndtering',
         'FAT/SAT og IQ/OQ/PQ uden kritiske afvigelser; A3, PDCA og 5 x hvorfor i fejlfinding; afvigelser '
         'ført med ejer og frist.'),
        ('CAD og 3D-modellering',
         'Teknisk design og tegning fra el- og maskinteknisk uddannelse. Sporspecifikke CAD- og '
         '3D-værktøjer er en del af indkøringsplanen, ikke af min erfaring.'),
        ('Videndeling mellem Ørestad og Aarhus',
         'Fast faglig sparringskadence og fælles metodebeskrivelser indgår i 90-dagesplanen nedenfor.')],
        )

    m.models_table('FØRSTE 90 DAGE — LEVERANCE OG OPFØLGNING', ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1',
         'Møde de fem medarbejdere, afdelingslederen og teamlederen i Aarhus. Gennemgå igangværende baneprojekter, '
         'leverancefrister og åbne kvalitetsspørgsmål. Aftale mandat, beslutningsret og hvem der kvalitetssikrer '
         'sporfagligt, indtil jeg selv kan.'),
        ('Dag 30',
         'Ugentlig leveranceoversigt og tavlemøde i drift. Grænsefladematrix for spor, baneafvanding, broer og '
         'konstruktioner samt kørestrøm etableret. Individuelle 1:1 gennemført med udviklingsaftaler og '
         'kompetencematrix på de kritiske spordiscipliner.'),
        ('Dag 60',
         'Første egne reviewbemærkninger på sporleverancer og en fast plads i den faglige videndeling. '
         'Kapacitetsbillede pr. måned mod projektporteføljen, så belastning og rekrutteringsbehov kan ses i tid. '
         'Fælles metodebeskrivelser aftalt med Aarhus.'),
        ('Dag 90',
         'Status på leverancer, kvalitet, økonomi og trivsel fremlagt i ledelsesgruppe med afdelingslederen. Opfølgning på de første '
         'forbedringer (A3), på kompetenceplanen og på de kunder og projektledere, hvor opfølgningen skal skærpes.')])

    m.section('FAGLIG INDKØRING I SPORDISCIPLINEN')
    m.para('Jernbane, sporprojektering og baneafvanding er nye fagområder for mig, og det lægges der en plan for '
           'frem for at blive talt uden om. Indkøringen følger fire spor: sidemandsoplæring hos afdelingens '
           'sporspecialister i både Ørestad og Aarhus; Banedanmarks banenormer, herunder BN1-11 afvanding af '
           'sporarealer, BN1-38 sporbeliggenhed og sporgeometri, BN1-6 tværprofiler for ballasteret spor og BN1-8 '
           'jordarter; DS/EN 13848 om sporgeometrisk kvalitet og de tilhørende målemetoder; og de CAD- og '
           '3D-modelleringsværktøjer, som afdelingen bruger i dag. Målet er ikke at blive specialist, men at kunne '
           'stille de rigtige faglige spørgsmål i projekteringen, genkende en kvalitetsmangel og sikre, at svaret '
           'kommer fra rette person — uanset om opgaven er nybygning eller sporfornyelse.', after=80)

    m.section('DIGITALT ARBEJDE MED ET KLART FORMÅL')
    m.para('Jeg bygger værktøjer i Python og Claude til planlægning, kvalitet og analyse samt investeringsmodeller med '
           'NPV, IRR, følsomhed og scenarier. I en rådgivningsorganisation kan det flytte tid fra rutineopfølgning til '
           'faglig dialog: en KPI-tavle der opdaterer sig selv, en tjekliste der følger kvalitetssikringen, og et '
           'beslutningsoplæg der viser levetids- og driftsomkostninger ved to løsninger. Det forudsætter godkendte '
           'systemer, menneskelig kontrol og respekt for kvalitetssystemet.', after=80)

    m.section('SAMARBEJDE, NÅR PLANEN ÆNDRER SIG')
    m.para('Kommer en hasteopgave ind og presser en frist, skal konsekvensen frem i lyset med det samme: hvilken '
           'leverance berøres, hvilke kompetencer er ledige, og hvilken beslutning har projektlederen eller kunden '
           'brug for? Et kort møde med de involverede og en skriftlig aftale om ansvar, frist og tilbagemelding giver '
           'ro — og en kunde, der hører om ændringen fra os før den rammer leverancen.', after=80)

    m.section('SPECIALISTER OG BESLUTNINGER')
    m.para('En leder uden sporfaglig baggrund skal ikke tilsidesætte en specialists faglige valg, når lederen ikke selv '
           'kan vurdere det. Til gengæld skal jeg blive ved med at spørge, indtil konsekvensen er klar: hvad betyder det for '
           'sikkerhed, levetid, tid og økonomi — og hvem skal vide det? Min rolle er at sørge for, at spørgsmålet bliver '
           'stillet i tide, at svaret bliver dokumenteret, og at den beslutning, der hører til ledelsesniveauet, bliver '
           'taget og ikke bare skubbet videre.', after=80)

    m.section('TRIVSEL SOM MÅLEPUNKT')
    m.para('Trivsel skal kunne ses på et tal og ikke kun mærkes på stemningen. Jeg følger trivselsmålinger, sygefravær '
           'og arbejdsmiljø systematisk, tager MUS som en aftale med konkrete punkter og ikke som en hyggesamtale, og '
           'bruger 1:1 til det, der ikke kan vente et år. Når kapaciteten kræver det, er rekruttering og onboarding en del af min opgave — med en '
           'oplæringsplan fra første dag, så nye kolleger hurtigt kan stå på egne ben i projekterne.', after=80)

    m.section('SÅDAN KØRER UGEN I SPOR OG ANLÆG')
    m.para('Mandag opdateres leveranceoversigten, og vi holder et kort tavlemøde om, hvad der er kritisk i denne uge. '
           'Onsdag er der grænseflade-review med baneafvanding, broer og konstruktioner samt kørestrøm på de opgaver, '
           'hvor flere fag mødes. Torsdag går til 1:1 og faglig sparring — på skift mellem Ørestad og Aarhus, så '
           'videndelingen har en fast plads i kalenderen. Fredag følges kvalitet og afvigelser op, og næste uges '
           'kapacitet aftales med projektlederne, inden den bliver en overraskelse for nogen.', after=80)

    m.section('KAPACITET, PRIORITERING OG KUNDEDIALOG')
    m.para('Når to projekter kalder på samme specialist, skal valget være begrundet og synligt: hvad koster det at '
           'flytte opgaven, hvem har fagligheden, og hvad skal kunden vide? Kapacitetsbilledet lægger jeg frem hver '
           'måned og tager diskussionen med projektlederen, før fristen bliver kritisk. Over for kunder og bygherrer '
           'er min linje, at en ændring meldes med konsekvens, alternativ og tidspunkt — ikke som en forklaring '
           'bagefter.', after=80)

    return m.save(path, title='Ansøgning og CV — Teamleder Spor og Anlæg, SYSTRA',
                  subject='Fagligt koordinerende teamledelse, leverancer og kvalitet',
                  keywords='teamleder, spor og anlæg, baneafvanding, jernbane, personaleledelse, kvalitet')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_SYSTRA_TeamlederSporOgAnlaeg.docx')))
