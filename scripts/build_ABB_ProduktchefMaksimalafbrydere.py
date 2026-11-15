# -*- coding: utf-8 -*-
"""ABB A/S — Produktchef, maksimalafbrydere og fremtidens el-infrastruktur (Ballerup).

Opgave-først ansøgning + CV i ét dokument (masterdesign).
Kultur og fagligt indhold: se master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md,
afsnittet om ABB (research 04.11.2026).
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Elautoriseret maskinmester · Produktansvar, teknisk rådgivning og marked'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('4. november 2026')
    m.meta('ABB A/S · Electrification, Ballerup · Afdelingschef Klaus Lund')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Produktchef — maksimalafbrydere og fremtidens el-infrastruktur (JR00052245)',
           bold=True, color='1A1A1A')
    m.para('Til Klaus Lund', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('En maksimalafbryder bliver sjældent valgt af den, der sælger den. Rådgiveren specificerer den, '
           'tavlebyggeren skal have selektivitet og kommunikation til at passe, installatøren monterer den, og '
           'grossisten skal have den på lager. Produktchefens opgave er at gøre det valg enkelt og velbegrundet i det '
           'danske marked — og at få den globale produktstrategi til at passe til danske normer, vaner og kunder. Det '
           'er ikke et formidlingsproblem. Det er et beslutningsproblem, og det kan bygges.', after=80)

    m.para('**Systemet er allerede bygget, og det kan være i drift i løbet af de første uger.** En produktbog pr. '
           'serie — Tmax XT og Emax 2 med Ekip-relæer og kommunikationsmoduler — hvor valget kan træffes på fire '
           'linjer: anvendelse, mærkestrøm, brydeevne (Icu/Ics) og selektivitet, plus hvilke kommunikationsmoduler '
           '(Modbus, Profinet, EtherNet/IP, IEC 61850) og hvilket tilbehør der hører til. Et konkurrentkort, der '
           'stiller vores serie op mod de alternativer, kunden reelt overvejer, så salget kan svare på prisspørgsmålet '
           'med andet end rabat. En win/loss-log på de tilbud, hvor et produktvalg blev afgjort, og en fast '
           'kundeinterview-kadence — fem kunder om måneden — der gør behov og indvendinger til data i stedet for '
           'mavefornemmelse. Og et træningsmodul på 20 minutter pr. produktområde, som salgsteamet kan bruge '
           'dagen efter.', after=80)

    m.para('Alt det arbejder ind i de KPI’er, jeg vil måles på sammen med salg og ordre: hit rate på tilbuddene, hvor '
           'ofte et tilbud indeholder det rigtige produkt og tilbehør, tid fra kundespørgsmål til teknisk svar, andelen '
           'af ordrer med kommunikationsmodul eller Ekip-tilvalg, og hvor mange sager der ender som reklamation på '
           'grund af forkert valg. Det er de tal, der viser, om produktchefrollen virker.', after=80)

    m.para('Jeg kommer med den tekniske side i hånden. Som elautoriseret maskinmester med elektriker- og '
           'elektromekanikerbaggrund har jeg projekteret og kvalitetssikret lavspændingstavler, hvor '
           'maksimalafbrydere, indstilling af beskyttelse og selektivitet var en del af leverancen, og jeg har stået i '
           'den danske el-branche som entreprenør med kunder i både industri, erhverv og service — med tilbud, '
           'kalkule, prissætning og leverandørdialog mod grossister som en daglig del af arbejdet. Jeg har også '
           'trænet lærlinge og kolleger gennem flere år, så teknisk formidling er ikke noget, jeg skal lære i rollen.',
           after=80)

    m.para('Samtidig skal jeg være tydelig om, hvad der ikke står på CV’et: jeg har ikke haft en formel produktchef- '
           'eller produktmarketingrolle før, og jeg har ikke ejet en global produktportefølje. Det, jeg har, er '
           'produktkendskab fra brugssiden, kommerciel erfaring fra egen virksomhed og flere års arbejde i '
           'grænsefladerne mellem teknik, indkøb og kunder — blandt andet 37 CAPEX-projekter og 25 specialister hos '
           'Novo Nordisk. Indkøringen har jeg lagt som en plan: dag 30 med produktbogen og et gennemløb af porteføljen '
           'sammen med de nordiske produktorganisationer; dag 60 med konkurrentkort, første kundeinterviews og '
           'prissætningsnotat; dag 90 med træningsmoduler, en produkt- og markedsplan for det danske marked og de '
           'første tal på hit rate og produktvalg.', after=80)

    m.para('Jeg søger, fordi rollen ligger præcis i spændet mellem det tekniske og det kommercielle, og fordi '
           'ABB’s værdier beskriver den måde, jeg arbejder på: **Care** for kunden, **Curiosity** om det, der kan '
           'gøres bedre, **Collaboration** på tværs af salg, ordre og produktorganisation — og **Courage** til at sige, '
           'hvornår et produktvalg er forkert, også når kunden allerede har besluttet sig. Den decentraliserede ABB Way '
           'med ansvar tæt på kunden passer godt til en rolle, hvor beslutningerne skal træffes tæt på det danske '
           'marked og ikke på et hovedkontor.', after=80)

    m.para('Jeg er professionel og aktiv Claude-koder og bruger Python og Claude til produktdata, prissætning og '
           'business cases med NPV, IRR og følsomhed — fx når en ny serie eller et nyt segment skal vurderes mod '
           'volumen, margin og supportbehov. Det giver salget og ledelsen et beslutningsgrundlag på én side i stedet '
           'for en mavefornemmelse, og det sker naturligvis inden for jeres systemer og godkendelser.', after=80)

    m.para('Jeg vil gerne komme forbi Ballerup og gennemgå, hvordan jeg vil bygge produktbogen, konkurrentkortet og '
           'træningsmaterialet de første 90 dage — og høre, hvor I ser det største potentiale i den danske portefølje.',
           after=80)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Elautoriseret maskinmester med 20+ års erfaring fra den danske el-branche — som selvstændig entreprenør '
           'med fuldt P&L-ansvar og som projektleder i GMP-reguleret industri. Arbejder i spændet mellem teknisk '
           'rådgivning og kommercielle beslutninger: produktvalg, tilbud, kalkule, prissætning og kundedialog. Bruger '
           'SAP, KPI-styring og egne AI-værktøjer (Python, Claude) til produktdata, prissætning og business cases.',
           after=80)

    m.section('KOMMERCIELT ANSVAR OG RESULTATER')
    for label, body in [
        ('Økonomi og prissætning',
         'Fuldt P&L-ansvar hos ELOHVAC med tilbud, kalkule, prissætning og opfølgning på dækningsgrad. Serviceaftaler '
         'med responstid, kvalitet og leveringsevne som KPI’er.'),
        ('Kunder og kanal',
         'Daglig dialog med erhvervs- og industrikunder samt leverandører og grossister. Projekterer og kvalitetssikrer '
         'lavspændingstavler, hvor maksimalafbrydere, beskyttelsesindstilling og selektivitet var en del af leverancen.'),
        ('Teknisk rådgivning og formidling',
         'Rådgiver kunder om løsningsvalg og dokumentation og har trænet lærlinge og kolleger gennem flere år. '
         'Oplæring og teknisk formidling er en fast del af ledelsesarbejdet.'),
        ('Projekter og grænseflader',
         'Koordinerede 25 specialister i 37 samtidige CAPEX-projekter hos Novo Nordisk mellem engineering, indkøb og '
         'anlæg — med FAT/SAT og IQ/OQ/PQ uden kritiske afvigelser.'),
        ('Digital praksis',
         'Professionel og aktiv Claude-koder. Python/Claude-værktøjer til tilbud, tidsplaner, KS og KPI har givet et '
         'dokumenteret produktivitetsløft på over 40 %. Bygger investeringsmodeller med NPV, IRR og scenarier.')]:
        m.bullet(label, body, after=30)

    m.models_table('VÆRKTØJER OG METODER', ('Opgave', 'Værktøj og dokumenteret anvendelse'), [
        ('Produktvalg og positionering',
         'Produktbog med valgmatrix (anvendelse, mærkestrøm, Icu/Ics, selektivitet, kommunikation), værdibudskab og '
         'kundesegment. Bygger på tavleerfaring og kundedialog fra ELOHVAC.'),
        ('Marked og konkurrenter',
         'VOC-interviews, konkurrentkort, win/loss-log og ABC-analyse af porteføljen. Fem kundeinterviews pr. måned '
         'som fast kadence i planen.'),
        ('Salgsunderstøttelse',
         'Battlecards, FAQ på tekniske indvendinger, træningsmodul pr. produktområde og fælles tilbudsmaler. '
         'Kobles til hit rate og andel af ordrer med tilvalg.'),
        ('Prissætning og business case',
         'Kalkule, dækningsgrad og prissætningsnotat; investeringsmodeller med NPV, IRR og følsomhed. Brugt i egen '
         'virksomhed med fuldt P&L-ansvar og hos Novo i CAPEX-sager.'),
        ('Kvalitet og dokumentation',
         'A3, PDCA, 5 x hvorfor og Ishikawa; teknisk dokumentation og afvigelser med ejer og frist. Brugt under GMP '
         'og i drift af kritiske anlæg.'),
        ('Ledelse og interessenter',
         'Situationsbestemt ledelse (SLII), delegeringstrappen, GROW og SBI; RACI og interessentkort på tværs af '
         'salg, ordre og produktorganisation.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L-ansvar · erhvervs- og industrikunder',
         [('Kommercielt ansvar', 'Tilbud, kalkule, prissætning, leverandør- og grossistdialog samt opfølgning på '
                                 'dækningsgrad og serviceaftaler.'),
          ('Teknisk rådgivning', 'Løsningsvalg, tavler og beskyttelsesindstilling, dokumentation og aflevering på '
                                 'el-, ventilations- og klimaanlæg.'),
          ('Digitale værktøjer', 'Python/Claude API til tilbud, tidsplaner, KS-tjeklister og KPI-dashboard; over '
                                 '40 % produktivitetsløft i virksomheden.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024',
         '37 samtidige CAPEX-projekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Grænseflader og fremdrift', 'Fulgte fremdrift, økonomi, risici og ressourcer mellem engineering, indkøb og '
                                        'anlæg; SAP ERP til økonomi og aktiver; rapportering til ledelse og bygherre.'),
          ('Test og kvalitet', 'FAT/SAT og IQ/OQ/PQ uden kritiske afvigelser ved aflevering; A3 og 5 x hvorfor i '
                               'fejlfinding; PDCA-program reducerede energiomkostningerne med 40 %.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter · DKK 2–10 mio. pr. projekt',
         [('Tilbud og leverance', 'Udbud, tilbud, underentreprenører og afleveringspakker. Daglige tavlemøder og '
                                   'flaskehalsanalyser gav et markant løft i leveringsevnen.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos, Lynetten · København · aug. 2017–jan. 2022',
         '24/7-drift · pumper, HVAC, højspændingstavler og SCADA · skiftehold',
         [('Driftssikkerhed og standarder', 'Forebyggende vedligehold, akut fejlfinding og reservedelsflow. 5S, '
                                            'Standard Work og PDCA samt LOTO, APV og risikovurdering i skifteholdsdrift.')]),
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
    m.edu('Elautoriseret maskinmester (LV/MV/HV), stærkstrøm', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('Køleteknik og klimaanlæg · STCW-sikkerhed og maskinrumsvagt',
          'Mercantec 2021 · Søfartsstyrelsen 2021–2023')

    m.section('SPROG, PRAKTISK OG REFERENCER')
    m.para('Dansk og persisk/farsi: modersmål · Engelsk: professionelt i skrift og tale · Kørekort B · Bopæl i Måløv, '
           'ca. 10 minutter fra Ballerup. Tidligere ledere hos Novo Nordisk og Biofos oplyses efter aftale.', after=70)

    m.models_table('KRAV I OPSLAGET — MIN DOKUMENTATION', ('Krav', 'Dokumentation'), [
        ('El-teknisk uddannelse (maskinmester, el-installatør, el-ingeniør)',
         'Opslaget accepterer elinstallatør, maskinmester eller el-ingeniør. Min vej er elautoriseret maskinmester '
         '(LV/MV/HV), stærkstrøm, med B.Tech i Technology Management & Mechanical Engineering, EQF 6, og '
         'elektriker-/elektromekanikerbaggrund.'),
        ('Erfaring med el-materiel og kendskab til den danske el-branche',
         'Ti år som entreprenør og tekniker i Danmark med tavler, beskyttelse, kabler og føringsveje; kunder i '
         'erhverv, industri og service samt dialog med grossister.'),
        ('Produktansvar og global strategi i dansk kontekst',
         'Ikke haft formel produktchefrolle. Kommercielt ansvar for tilbud, kalkule og prissætning i egen virksomhed; '
         'indkøringsplan nedenfor.'),
        ('Understøtte salg med produktvalg og tilbud',
         'Teknisk rådgivning og tilbudsarbejde i daglig praksis; produktbog, battlecards og træningsmodul som første '
         'leverancer.'),
        ('Marked, kunder og konkurrenter',
         'VOC-interviews, konkurrentkort og win/loss-log indgår i 90-dagesplanen; markedskendskab fra egen drift og '
         'kundedialog.'),
        ('Formidling og træning',
         'Har trænet lærlinge og kolleger gennem flere år og skrevet teknisk dokumentation på dansk og engelsk.'),
        ('Ordre, logistik og systemer',
         'SAP ERP til økonomi, aktiver og ressourcer; ordre- og leverandørflow i egen virksomhed; CMMS og digitale '
         'tjeklister.'),
        ('Maksimalafbrydere og tavler',
         'Kommunikationsløsninger: tavler og lavspænding med maksimalafbrydere og beskyttelsesindstilling fra '
         'praksis. Ekip-relæer, '
         'kommunikationsmoduler og serieporteføljen indgår i indkøringen — ikke i tidligere produktansvar.')])
    m.page_break()

    m.models_table('FØRSTE 90 DAGE — PRODUKT, MARKED OG SALG', ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1',
         'Møde salg, ordre og logistik samt de nordiske produktorganisationer. Gennemgå den danske portefølje, de '
         'seneste tilbud og de kendte reklamationer. Aftale mandat, beslutningsret og hvilke KPI’er rollen måles på.'),
        ('Dag 30',
         'Produktbog for Tmax XT og Emax 2 med valgmatrix, tilbehør og kommunikationsmoduler på plads. Første '
         'kundeinterviews gennemført, og baseline for hit rate og produktvalg lagt frem for salget.'),
        ('Dag 60',
         'Konkurrentkort og prissætningsnotat klar. Win/loss-log i brug på tilbud, og en fast kadence for '
         'produktspørgsmål fra salget. Første træningsmodul afprøvet med salgskollegerne.'),
        ('Dag 90',
         'Produkt- og markedsplan for det danske marked fremlagt: segmenter, værdibudskaber, kampagneplan og '
         'prioriterede produktinitiativer. Status på hit rate, tilvalgsgrad og antal sager med forkert produktvalg.')])

    m.section('TEKNISK GRUNDLAG — AFBRYDERE, SELEKTIVITET OG KOMMUNIKATION')
    m.para('Produkterne kender jeg fra tavlen: maksimalafbrydere efter EN/IEC 60947-2 med termomagnetiske eller '
           'elektroniske relæer, indstilling af beskyttelse, brydeevne (Icu/Ics) og selektivitet mellem trin i '
           'installationen. Kommunikationssiden er den, jeg vil lære hurtigst muligt i dybden: Ekip-relæer og '
           'kommunikationsmoduler til Modbus, Profinet, EtherNet/IP og IEC 61850 samt data via ABB Ability. Det er netop '
           'den kombination, kunderne efterspørger, når tavlen skal levere energi- og tilstandsbillede og ikke bare '
           'beskyttelse.', after=80)

    m.section('FORBEDRINGARBEJDE MED ET MÅL')
    m.para('Jeg tager udgangspunkt i de sager, hvor et produktvalg gik galt: forkert brydeevne, manglende tilvalg, '
           'selektivitet der ikke holdt i praksis, eller et tilbehør der kom for sent. Dem gennemgår jeg med A3 og 5 x '
           'hvorfor, finder den del af kæden der svigtede — rådgivning, tilbud, ordre eller lager — og retter den, så '
           'den samme fejl ikke gentages. Det er den samme fremgangsmåde, jeg brugte til at fjerne kritiske afvigelser '
           'i GMP-regulerede projekter.', after=80)

    m.section('SAMARBEJDE PÅ TVÆRS AF SALG, ORDRE OG PRODUKTORGANISATION')
    m.para('Produktchefrollen lykkes i grænsefladerne. Salg skal have svar inden for samme dag, ordre skal vide, hvad '
           'der kan leveres, og produktorganisationen skal have danske behov tilbage som prioriteret input — ikke som '
           'enkeltsager. Jeg bruger et interessentkort og en skreven beslutningsret, så det er tydeligt, hvem der '
           'beslutter hvad, og så en kunde ikke får to forskellige svar fra to kolleger.', after=80)

    m.section('PRODUKTMARKEDSFØRING DER KAN MÅLES')
    m.para('Produktmarkedsføring i el-branchen handler sjældent om at råbe højest. Den handler om at være til stede der, '
           'hvor valget bliver truffet: hos rådgiveren i projekteringsfasen, hos installatøren på værkstedet, hos '
           'grossisten bag disken og på de faglige sider, hvor tavlebyggere læser med. Jeg vil bygge kampagner i tre '
           'lag — produktmateriale i form af en valgguide og et teknisk notat pr. serie, en kort case fra et dansk '
           'anlæg, og et webinar eller '
           'frokostmøde hos en grossist — og koble hvert lag til et måltal: antal downloads, antal leads, andel af '
           'tilbuddene hvor produktet indgår, og hvor mange af dem der bliver til ordrer. Uden de tal er kampagnen en '
           'mening; med dem er den et styringsværktøj.', after=80)

    m.section('DIGITALT ARBEJDE MED ET KLART FORMÅL')
    m.para('Jeg bygger værktøjer i Python og Claude til produktdata, prissætning, hit rate-opfølgning og business '
           'cases med NPV, IRR, følsomhed og scenarier. I en produktrolle kan det flytte tid fra rapporttræk til '
           'kundedialog: et dashboard der viser, hvilke tilbud der ikke konverterer, og en model der viser, hvad et nyt '
           'segment koster at åbne. Det forudsætter godkendte systemer, datakvalitet og respekt for ABB’s processer.',
           after=80)

    return m.save(path, title='Ansøgning og CV — Produktchef maksimalafbrydere, ABB',
                  subject='Produktansvar, teknisk rådgivning og kommerciel indsigt',
                  keywords='produktchef, maksimalafbrydere, el-materiel, produktstrategi, marked, salg')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_ABB_ProduktchefMaksimalafbrydere.docx')))
