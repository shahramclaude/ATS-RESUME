# -*- coding: utf-8 -*-
"""Xellia Pharmaceuticals — Utility Supporter, Maintenance (København).

Dansk leverance (opslaget er dansk): opgavefokuseret motiveringsside + CV i ét dokument.
Kultur- og rolleintel: master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md,
afsnit om Xellia (research 05.11.2026).
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Drift og vedligehold af kritiske forsyningssystemer · Damp, vand, HVAC og køl'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('5. november 2026')
    m.meta('Xellia Pharmaceuticals · Dalslandsgade 11, 2300 København S · Maintenance')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Utility Supporter — Black & Clean Utilities, HVAC og køl', bold=True, color='1A1A1A')
    m.para('Til Maintenance-organisationen', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('Et forsyningssystem viser, hvad det er værd, klokken 03.14 om natten. Ikke i et projektmøde og ikke i '
           'årsrapporten, men når en alarm går, en pumpe falder ud, eller dampen ikke holder trykket — og produktionen '
           'venter. Kontinuitet er ikke en strategi, man beslutter; det er en rytme, nogen holder hver dag. Det er den '
           'rytme, jeg gerne vil være en del af hos Xellia, hvor jeres egen historie netop handler om at levere kritisk '
           'medicin til tiden, hver gang.', after=80)

    m.para('**Jeg vil drive området på fire faste ting.** Først den daglige rytme: alarmgennemgang og et kort tavlemøde '
           'om morgenen med de samme tal — driftstimer, aktive alarmer, åbne afvigelser og hvad der venter i dag — så '
           'fejlfinding begynder med viden og ikke med en telefonsamtale. Dernæst vedligeholdelse bygget på '
           'kritikalitet og tilstand frem for kalender alene: hvad må ikke stoppe, hvad koster det at stoppe, og '
           'hvilke reservedele skal ligge på hylden, fordi leveringstiden er længere end produktionens tålmodighed. Så '
           'dokumentation i nuet: SOP\'er der beskriver det, vi faktisk gør, Change Control før ændringen og ikke '
           'efter, og afvigelser lukket med rodårsag og en verifikation af, at tiltaget holdt. Og endelig levetid og '
           'økonomi: en plan for de næste tre til fem år pr. anlæg, hvor reparation holdes op mod udskiftning med '
           'tal på — og hvor OPEX- og CAPEX-behovet kan læses på én side.', after=80)

    m.para('Kedelcentralen og dampen er kernen i det arbejde, og jeg har fem år fra 24/7-drift på et procesanlæg, '
           'hvor alarmer blev behandlet som driftsdata og ikke som støj. Jeg har været på vagt, når anlægget ikke '
           'måtte stoppe — og jeg ved, hvad forskellen er på at udskyde en opgave og at udskyde en risiko. '
           'Processpildevand var en del af den daglige drift og af miljødokumentationen, så jeres miljø- og '
           'myndighedskrav er velkendte for mig.', after=80)

    m.para('Den farmaceutiske del har jeg fra Novo Nordisk, hvor jeg i to år var projektleder og '
           'idriftsættelsesingeniør på 37 samtidige anlægsprojekter under GMP, FDA og EMA: dokumenterede '
           'acceptkriterier, FAT/SAT, IQ/OQ/PQ, håndtering af afvigelser og auditeret aflevering med nul kritiske '
           'fund. Jeg har fået anlæg godkendt, fordi SOP\'en passede med virkeligheden — og det er præcis den tilgang, '
           'Change Control, CAPA og reservedelskritikalitet kræver i en daglig drift.', after=80)

    m.para('Det her er ikke nyt terræn for mig — det er mit fag. Som maskinmester er jeg uddannet i damp- og '
           'vandkredsløb, varmevekslere, køleanlæg og regulering, og jeg har brugt det i både drift og service: '
           'pumper, ventiler, HVAC og højspænding i døgndrift, og tre år med eget ansvar for service, installation og '
           'kunder inden for elkraft og HVAC. Tryk, temperatur, flow og vandkvalitet er parametre, jeg har fulgt hver '
           'dag — og Black & Clean-tankegangen med kritikalitet, renhed og sporbarhed er den samme disciplin, jeg '
           'altid har arbejdet efter.', after=80)

    m.para('Jeg går ind i et team på fem med respekt for den viden, der allerede ligger der — og med en klar '
           'forventning til mig selv: inden for den første måned tager jeg min del af vagtordningen, de forebyggende '
           'planer og opfølgningen på reservedele, og inden for de første tre måneder er jeg den, produktionen ringer '
           'til, når kedelcentralen, køleanlægget eller ventilationen driller. Viden skal deles med vilje, og jeg '
           'deler gerne min: dokumentation, økonomi og digital opfølgning er, hvor jeg hurtigt kan lette hverdagen for '
           'de fire andre.', after=80)

    m.para('Det, der trækker mig mod Xellia, er, at kontinuitet er selve forretningsmodellen. I er blandt de sidste '
           'vestlige producenter af flere essentielle antiinfektiva, og jeres mission — kritisk medicin til tiden, hver '
           'gang — kan kun holdes, hvis forsyningen aldrig blinker. Jeres fire værdier rammer opgaven præcist: '
           '"Make it matter" er den vagt, hvor en ventil bliver skiftet, før den fejler; "Speak truth" er at melde en '
           'afvigelse samme dag; "Own it" er at følge sagen til den er lukket; og "Play to win" er at gøre det sammen '
           'med produktion, teknikere og leverandører. Jeg har også læst, at fabrikken i København er i en planlagt, '
           'gradvis udfasning. Det ændrer ikke opgaven: så længe der produceres, skal damp, vand, luft og køl køre, og '
           'dokumentationen skal holde til det sidste — og den slags kontinuitet er netop det, jeg er god til.', after=80)

    m.para('Praktisk: jeg bor i Måløv, ca. 30 minutter fra Dalslandsgade, og jeg er vant til 24/7-drift med vagter, '
           'weekender og tilkald. Jeg taler dansk og persisk som modersmål og engelsk professionelt, og jeg arbejder i '
           'SAP og Excel dagligt. Jeg er også aktiv Claude-koder og bygger mine egne Python-værktøjer til '
           'vedligeholdelsesopfølgning, reservedelslister og investeringsberegninger med NPV, IRR og scenarier. Jeg kan '
           'starte efter aftale og går ind i 24/7-vagtordningen fra første uge.', after=80)

    m.para('Jeg vil gerne komme til Dalslandsgade, gå ruterne igennem med jer — kedelcentral, rent damp, vand, '
           'trykluft, HVAC og køl — og vise konkret, hvordan jeg ville tage de første 90 dage, og hvilke tal jeg ville '
           'måle på.', after=80)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Drifts- og projektingeniør med 20+ års erfaring fra tekniske anlæg, reguleret produktion og egen '
           'virksomhed — elautoriseret maskinmester med B.Tech i Technology Management & Mechanical Engineering. Fem '
           'år i 24/7-drift med pumper, HVAC, højspænding og SCADA, heraf daglig drift og miljødokumentation på et '
           'procesanlæg for spildevand; to år med GMP-projekter, FAT/SAT, IQ/OQ/PQ og nul kritiske fund hos Novo '
           'Nordisk. Arbejder med kritikalitet, forebyggende planer og reservedele som faste systemer og bygger egne '
           'Python- og Claude-værktøjer til opfølgning og investeringsberegninger.', after=80)

    m.section('DRIFT, VEDLIGEHOLD OG RESULTATER')
    for label, body in [
        ('24/7 drift og fejlfinding',
         'Fem år på et døgnbemandet procesanlæg: alarmer, driftsforstyrrelser, fejlfinding og korrigerende '
         'vedligehold på pumper, varmevekslere, ventiler, HVAC og højspændingsanlæg — med vagtplan, weekender og '
         'tilkald.'),
        ('Forebyggende vedligeholdelse',
         'Vedligeholdelsesplaner bygget på tilstandsdata fra SCADA, kritikalitet og leveringstider; reservedele med '
         'min./maks.-niveauer og varenumre, så kritiske systemer ikke venter på en leverance.'),
        ('Dokumentation og kvalitetssystem',
         'SOP\'er, Change Control, afvigelser og CAPA i daglig brug; FAT/SAT og IQ/OQ/PQ med sporbar dokumentation og '
         'auditeret aflevering. Nul kritiske fund ved aflevering i 37 GMP-projekter.'),
        ('Anlæg, miljø og energi',
         'Drift og optimering af procesanlæg med miljødokumentation; et PDCA-forløb reducerede energiforbruget med '
         '40 %, og 5S og standard work holdt værksted og lager i orden.'),
        ('Økonomi og leverandører',
         'Tre år med fuldt P&L, tilbud, indkøb og serviceaftaler i egen virksomhed; koordinering af eksterne '
         'leverandører og underentreprenører i både drift og projekter, med aftaler der kan følges op på.')]:
        m.bullet(label, body, after=25)

    m.models_table('VÆRKTØJER OG METODER', ('Opgave', 'Værktøj og dokumenteret anvendelse'), [
        ('Drift og overvågning',
         'SCADA og alarmer, driftslog og tavlemøde med faste tal; fejlfinding med A3 og 5 x hvorfor og korrigerende '
         'handling med ejer og frist.'),
        ('Vedligehold og kritikalitet',
         'Kritikalitetsvurdering pr. anlæg, forebyggende planer, reservedelskritikalitet og min./maks.; '
         'levetidsvurdering og reparér-eller-udskift-analyse.'),
        ('Kvalitet og dokumentation',
         'SOP\'er, Change Control, afvigelser, CAPA og inspektionsparathed under GMP/FDA/EMA; FAT/SAT og IQ/OQ/PQ '
         'med sporbarhedsmatrix.'),
        ('Sikkerhed og miljø',
         'LOTO, APV, risikovurdering, arbejdstilladelser og nærhændelser; miljø- og myndighedsdokumentation på et '
         'procesanlæg for spildevand.'),
        ('Projekt og leverandører',
         'Små og mellemstore projekter fra krav til aflevering: tidsplan, økonomi, leverandørstyring, FAT/SAT og '
         'afleveringsforretning.'),
        ('Økonomi og digitalt',
         'OPEX/CAPEX-grundlag med NPV, IRR, følsomhed og scenarier; SAP og Excel i daglig brug; egne Python/Claude-'
         'værktøjer til vedligeholdelses- og reservedelsopfølgning.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · erhvervs- og industrikunder',
         [('Drift, kunder og økonomi', 'Tilbud, prissætning, dækningsgrad og serviceaftaler med responstid, kvalitet '
                                       'og levering som KPI\'er; leverandørforhandling og kontrol af fakturaer.'),
          ('Personale og sikkerhed', 'Daglig planlægning, 1:1, MUS, kompetencematrix og oplæring; LOTO, APV og '
                                     'risikovurdering ved hver opstart.'),
          ('Digitale værktøjer', 'Python og Claude API til tilbud, planlægning, kvalitetschecklister og '
                                 'KPI-dashboard; over 40 % produktivitetsløft i virksomheden.')]),
        ('Senior idriftsættelsesingeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024',
         '37 samtidige anlægsprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Kvalificering og dokumentation', 'Acceptkriterier, FAT/SAT og IQ/OQ/PQ med sporbar dokumentation og '
                                             'håndtering af afvigelser; nul kritiske fund ved aflevering.'),
          ('Koordination og rapportering', 'Fremdrift, økonomi, risiko og ressourcer mellem engineering, indkøb og '
                                           'drift; månedsrapportering til ledelse og bygherre.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter · 2–10 mio. kr. pr. projekt',
         [('Ventilation og anlæg', 'Tilbud, kalkuler, underleverandører og afleveringspakker inden for ventilation og '
                                   'tekniske installationer; daglige tavlemøder og flaskehalsanalyser.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos, Lynetten · København · aug. 2017–jan. 2022',
         '24/7-drift · pumper, HVAC, højspænding, SCADA · spildevandsanlæg med miljødokumentation',
         [('Forebyggende og korrigerende vedligehold', 'Planer fra SCADA-tilstandsdata og driftshistorik; '
                                                       'reservedelslager med varenumre og min./maks.; alarmer og '
                                                       'nedetid registreret og fulgt op.'),
          ('Sikkerhed og miljø', 'LOTO, APV, risikovurdering og nærhændelser i skiftdrift; miljødokumentation og '
                                 'standard work, 5S og PDCA i værksted og lager.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran, Iran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · industrielt udstyr',
         [('Anlæg og fejlfinding', 'Vagtplanlægning, materialestyring og opfølgning på mål; fejlfinding, '
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
    m.edu('Damp- og vandkredsløb, køleanlæg og maskinlære',
          'Maskinmesterskolen København · Mercantec 2021 · Søfartsstyrelsen 2021–2023')
    m.edu('El- og maskinteknisk design, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Lean og procesforbedring: 5S, PDCA, VSM, A3, Kaizen',
          'Løbende kurser og daglig anvendelse i drift og projekter')

    m.section('SPROG, PRAKTISK OG REFERENCER')
    m.para('Dansk og persisk: modersmål · Engelsk: professionelt, skriftligt og mundtligt · Kørekort B · Bopæl i '
           'Måløv, ca. 30 minutter fra Dalslandsgade · Vant til 24/7-drift med vagter, weekender og tilkald · SAP og '
           'Excel i daglig brug · Referencer fra Novo Nordisk og Biofos samt fra samarbejdspartnere i egen virksomhed '
           'oplyses efter aftale.', after=70)

    m.models_table('KRAV I OPSLAGET — MIN DOKUMENTATION', ('Krav', 'Dokumentation'), [
        ('Teknisk baggrund som maskinmester, maskiningeniør eller tilsvarende',
         'Elautoriseret maskinmester (LV/MV/HV) med B.Tech i Technology Management & Mechanical Engineering, EQF 6 — '
         'uddannet på damp- og vandkredsløb, køleanlæg og maskinlære.'),
        ('Stabil og optimal drift af Black & Clean Utilities',
         'Fem år i 24/7-drift af procesanlæg: pumper, varmevekslere, ventiler, HVAC, køleanlæg, luft-, gas- og '
         'vandsystemer samt højspænding. Alarmer og afvigelser håndteret som driftsdata, med kritikalitet og '
         'sporbarhed som styrende princip.'),
        ('Alarmer, fejlfinding og korrigerende vedligehold',
         'Daglig fejlfinding og korrigerende arbejde prioriteret efter konsekvens; A3 og 5 x hvorfor som standard, '
         'med verifikation af at tiltaget holdt.'),
        ('Forebyggende planer, levetid og optimering',
         'Vedligeholdelsesplaner fra tilstandsdata og kritikalitet; levetidsvurdering og reparér-eller-udskift-'
         'analyser med NPV, IRR og scenarier.'),
        ('SOP\'er, GMP-, miljø- og myndighedsdokumentation',
         'To år med GMP/FDA/EMA: SOP\'er, Change Control, afvigelser, CAPA og auditeret aflevering uden kritiske '
         'fund; validering og kvalificering af nye anlæg; miljødokumentation fra spildevandsanlæg.'),
        ('Reservedele til produktionskritiske systemer',
         'Reservedelslager med varenumre, min./maks. og kritikalitet; leveringstider holdt op mod, hvad '
         'produktionen kan tåle.'),
        ('Leverandører, OPEX/CAPEX og mindre projekter',
         'Koordinering af leverandører og underentreprenører i drift, projekter og ombygninger; tre år med fuldt P&L, '
         'budget og investeringsgrundlag i egen virksomhed.'),
        ('Struktureret også ved akutte udfordringer; 24/7-fleksibilitet',
         'Fem år med vagtordning, weekender og tilkald på et anlæg, der ikke måtte stoppe; ro til at prioritere, når '
         'der er tre ting, der haster på samme tid.')])
    m.page_break()

    m.models_table('FØRSTE 90 DAGE — ANLÆG, PLANER OG DOKUMENTATION', ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'Gå ruten med hver af de fem kolleger: kedelcentral, rent damp, vand, trykluft, HVAC og køl. Læs de seneste '
         'tre måneders alarmer og afvigelser og se, hvilke anlæg der bruger tiden. Læs de SOP\'er, der bliver brugt '
         'mest, og de reservedele, der bliver brugt mest.'),
        ('Dag 30',
         'Overblik på én side: anlægsliste med kritikalitet, åbne afvigelser og CAPA\'er, de fem hyppigste '
         'fejlmønstre, reservedelsdækning på de kritiske systemer og status på de forebyggende planer.'),
        ('Dag 60',
         'Forebyggende planer justeret for de tre mest kritiske anlæg. Reservedelsliste og min./maks. gennemgået mod '
         'leveringstider. SOP\'er opdateret der, hvor praksis og tekst ikke stemmer, med Change Control som vej.'),
        ('Dag 90',
         'Levetids- og investeringsplan for de næste tre år pr. anlæg, klar til OPEX/CAPEX-drøftelse. Målt fald i '
         'gentagne fejl på mindst ét system. En skrevet rytme for alarmgennemgang og tavlemøde, som kollegerne kan '
         'køre videre uden mig.')])

    m.section('HVAD BLACK & CLEAN UTILITIES KRÆVER')
    m.para('Skellet mellem black og clean er ikke kosmetisk; det er et skel i risiko. Rene systemer — rent damp, WFI og '
           'de kredse, der har direkte kontakt med produkt — kræver dokumenteret kontrol, kalibrerede sensorer og '
           'sporbarhed, mens de sorte systemer kræver driftssikkerhed og hurtig reparation. Begge steder gælder det '
           'samme: den første, der opdager en afvigelse, er den, der redder dagen. Derfor skal driftsrutinen gøre det '
           'nemt at melde fra, og dokumentationen skal være så enkel, at den bliver brugt i en travl uge.', after=80)

    m.section('KEDELCENTRALEN OG DAMPEN')
    m.para('En kedelcentral er et anlæg med få, men dyre fejl: vandkvalitet, tryk, brænder og følere. Derfor vil jeg '
           'begynde med at forstå vandbehandlingen og den dokumenterede driftstilstand, før jeg ændrer noget — og '
           'derefter sikre, at de forebyggende opgaver ligger fast, at reservedelene til brænder og følere er på '
           'plads, og at driftsjournalen kan læses af en kollega uden forklaring. Damp er ikke et sted, hvor man '
           'improviserer; det er et sted, hvor man planlægger.', after=80)

    m.section('VEDLIGEHOLD DER HOLDER — KRITIKALITET OG LEVETID')
    m.para('Vedligeholdelse bliver først en strategi, når den er ujævnt fordelt: de få anlæg, der kan stoppe '
           'produktionen, skal have mere opmærksomhed end de mange, der kan vente. Derfor en kritikalitetsvurdering pr. '
           'system, forebyggende intervaller baseret på tilstand og historik frem for tradition, og en løbende '
           'levetidsvurdering, hvor reparation holdes op mod udskiftning med tal på driftstab, energi og '
           'reservedelsbehov. Det er også den analyse, der gør en CAPEX-ansøgning nem at sige ja til.', after=80)

    m.section('DOKUMENTATION, GMP OG INSPEKTIONER')
    m.para('Inspektionsparathed opstår ikke i ugen før besøget; den opstår, når SOP\'en beskriver det, folk faktisk '
           'gør, når Change Control er brugt før ændringen, og når afvigelser er lukket med en rodårsag, der kan '
           'forklares for en inspektør. Jeg har arbejdet i GMP-miljøer, hvor en manglende underskrift stopper en '
           'frigivelse, og på et miljøanlæg, hvor myndigheden læser driftsjournalen. Det gør dokumentationen til noget, '
           'man skriver i nuet — ikke noget, man rekonstruerer.', after=80)

    m.section('MILJØ, ENERGI OG SPILDEVAND')
    m.para('På et anlæg som jeres er miljødokumentation og energiforbrug ikke to sideløbende dagsordener; de er samme '
           'drift set fra to sider. Jeg har fem år fra et spildevandsanlæg, hvor miljøkrav var en del af den daglige '
           'rutine, og hvor et PDCA-forløb tog 40 % af energiforbruget. Den slags gevinster kommer sjældent fra et '
           'projekt alene — de kommer fra at måle på det samme anlæg i længere tid og gøre én ting ad gangen.', after=80)

    m.section('ØKONOMI: OPEX, CAPEX OG LEVETID')
    m.para('Jeg vil levere det samme grundlag for økonomi, som jeg forventer af en leverandør: hvad koster det at '
           'vedligeholde, hvad koster det at lade være, og hvad koster det at udskifte — med følsomhed på de antagelser, '
           'der betyder mest. Tre år med fuldt P&L i egen virksomhed har lært mig, at det sjældent er den store post, '
           'der vælter budgettet, men de mange små, som ingen havde regnet på.', after=80)

    m.section('DIGITALT ARBEJDE MED ET KLART FORMÅL')
    m.para('Jeg bruger Python og Claude til det, regnearket er for langsomt til: trække alarm- og driftsdata sammen '
           'til én side, følge reservedelsforbrug mod leveringstider, holde styr på åbne CAPA\'er og lave '
           'investeringsberegninger med NPV, IRR og scenarier. Det erstatter ikke SAP eller kvalitetssystemet, og det '
           'sker inden for jeres procedurer — men det gør opfølgningen hurtig nok til, at den bliver gjort.', after=80)

    return m.save(path, title='Ansøgning og CV — Utility Supporter, Xellia Pharmaceuticals',
                  subject='Drift og vedligehold af kritiske forsyningssystemer i farmaceutisk produktion',
                  keywords='utility supporter, black utilities, clean utilities, HVAC, kedelcentral, GMP, vedligehold')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Xellia_UtilitySupporter.docx')))
