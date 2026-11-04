# -*- coding: utf-8 -*-
"""HOFOR A/S — Teamleder til Kundeløsninger (København S).

Motiveret CV + opgave-først motivationsside i ét dokument (masterdesign).
Kultur og fagligt indhold: se master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md,
afsnittet om HOFOR Kundeløsninger (research 04.11.2026).
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Personaleleder · Fra kundebehov til løsning i drift · Data og digitalisering'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('4. november 2026')
    m.meta('HOFOR A/S · Kundeløsninger, Ørestads Boulevard 35 · Områdechef Ditte Bergholdt Asmussen')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Motiveret CV: Teamleder til Kundeløsninger', bold=True, color='1A1A1A')
    m.para('Til Ditte Bergholdt Asmussen', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('Kundeløsninger lever ikke af, at nogen får en god idé. Det lever af, at et behov hos en kunde — eller '
           'et tal i vores egne data — bliver til en løsning, der er testet, taget i brug og stadig virker tre '
           'måneder senere, når ingen fra projektet længere sidder ved bordet. Det er den kæde, teamlederrollen '
           'skal holde kort og forudsigelig, og det er den kæde, jeg vil bygge sammen med teamet fra første uge.',
           after=80)

    m.para('**Forløbet fra problem til implementeret løsning kan bygges som fire porte, som intet initiativ springer '
           'over.** Første port: behovet er bevist — kundeinterviews, henvendelsesdata, forbrugsdata og en tegnet '
           'kunderejse, ikke en fornemmelse i et mødelokale. Anden port: beslutningsgrundlaget holder — hvad vinder '
           'kunden, hvad vinder HOFOR, hvad koster det at drive, og hvad er business casen over tre år. Tredje port: '
           'leverancen er synlig — en prioriteret backlog, korte forløb med demo undervejs for forsyningen og '
           'kundeservice, og en aftalt overlevering til IT/Digitalisering i stedet for en løsning, der opstår ved '
           'siden af. Fjerde port: løsningen er testet, kvalificeret og forankret — testcases, oplæring af dem der '
           'skal bruge den, og en gevinstmåling tre og seks måneder efter, at den er i drift.', after=80)

    m.para('Det bliver de tal, jeg vil styre teamet på sammen med jer: tid fra behov til beslutning, andel af '
           'løsninger der reelt er i brug efter tre måneder, kundeoplevelsen målt på det kunderne faktisk ringer om, '
           'færre gentagne henvendelser og realiserede gevinster frem for planlagte. Uden de tal er digitalisering '
           'et program af aktiviteter; med dem er det en portefølje, der kan styres.', after=80)

    m.para('Jeg kommer med personaleledelsen og udviklingsarbejdet fra to miljøer, der ligner jeres i det, der betyder '
           'noget. I min egen virksomhed har jeg personaleansvar for fem elektrikere og tre lærlinge med daglig '
           'planlægning, 1:1 hver fjortende dag, MUS, kompetencematrix og oplæring, der ender med, at folk kan noget, '
           'de ikke kunne før. Hos Novo Nordisk har jeg ført 37 samtidige CAPEX-projekter igennem med 25 '
           'specialiserede medarbejdere, som jeg ikke havde personaleansvar for — altså ledelse gennem retning, '
           'aftaler og tillid, præcis som når en digitaliseringsindsats skal lykkes på tværs af forsyninger, '
           'kundeservice og IT.', after=80)

    m.para('Kvalificeringsdelen er den, jeg er mest tryg ved, og den er ofte den, der vælter udviklingsprojekter. '
           'Hos Novo stod jeg med FAT/SAT og IQ/OQ/PQ under GMP og FDA/EMA med nul kritiske afvigelser ved '
           'aflevering. Det er samme disciplin, en kundeløsning skal igennem: skrevne acceptkriterier, test med de '
           'rigtige brugere, en plan for hvem der griber ind, når den siger fejl, og dokumentation der gør, at '
           'kundeservice kan svare uden at ringe til udvikleren. Jeg har også selv bygget værktøjerne i Python og '
           'Claude — tilbudsberegning, KS-tjeklister, KPI-dashboards og investeringsmodeller med NPV, IRR og '
           'følsomhed — og ved, hvor lidt en model er værd, hvis den ikke bliver brugt i beslutningen.', after=80)

    m.para('Jeg skal også være tydelig om det, der ikke står i mit CV: jeg kommer fra teknisk drift og entreprise, '
           'ikke fra en kundeservice- eller produktorganisation, og jeg har ikke selv været leder for Product Owners '
           'i et digitalt udviklingsteam. Det, jeg har, er 20 år i en kompleks hverdag med kunder, drift og '
           'leverancer, en dokumenteret evne til at få fagligt forskellige mennesker til at levere sammen, og en '
           'arbejdsmåde der kan sættes i gang med det samme. De første 90 dage er derfor en læringsplan frem for en '
           'færdig strategi: uge 1 til at lytte mig gennem kunderejsen og systemlandskabet, dag 30 med overblik over '
           'porteføljen og teamets kompetencer, dag 60 med prioriteret portefølje og en '
           'kvalificeringspraksis på plads, dag 90 med de første målte gevinster og en udviklingsplan pr. medarbejder.',
           after=80)

    m.para('Det, der trækker mig mod HOFOR, er ikke skalaen alene — over en million kunder, otte kommuner, 150 års '
           'viden — men at kundeløsningerne allerede rører ved folks hverdag: bedre brug af kundedata, '
           'Flexumers der styrer varme smartere, indsatsen for grøn omstilling i etageboliger og Fjernvarmedoktoren, '
           'der diagnosticerer en varmecentral og sender kunden en handlingsplan. Det er præcis den slags løsninger, '
           'hvor teknik, data og kundeoplevelse skal lykkes i samme leverance. Og det passer til den måde, I beskriver '
           'arbejdspladsen på: **plads til fællesskab, plads til udvikling, plads til et bæredygtigt arbejdsliv.** Et '
           'team med videndeling, kollegial sparring og et godt grin i hverdagen kræver ikke mindre styring — det '
           'kræver, at styringen er tydelig nok til, at der er overskud til hinanden.', after=80)

    m.para('Jeg leder med tydelig retning og tillid i udførelsen. I praksis betyder det situationsbestemt ledelse '
           '(SLII), fast 1:1-kadence, SBI-feedback, GROW når en medarbejder skal flytte sig fagligt, en '
           'kompetencematrix der gør huller synlige, og en tavle hvor arbejdet kan ses. Psykologisk tryghed er ikke '
           'en velværeøvelse for mig; det er forudsætningen for, at nogen tør sige, at løsningen ikke virker i '
           'praksis. Følgeskab skabes ved at være tydelig om retningen og troværdig i det daglige — og '
           'samarbejdsrelationer bliver kun holdbare, når man ved, hvad man har med hinanden at gøre.',
           after=80)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Personaleleder med 20+ års erfaring fra teknisk drift, entreprise og projektledelse i komplekse '
           'organisationer — eget P&L-ansvar, personaleansvar og tværgående ledelse af specialister. Arbejder i '
           'spændet mellem forretningsbehov, data og implementering: fra problem til løsning der er testet, '
           'kvalificeret og i brug. Kombinerer personaleledelse, forretningsforståelse og eksekvering i samme rolle. '
           'Bruger SAP, Power BI og egne AI-værktøjer (Python, Claude) til analyser, dashboards og business cases '
           'med NPV, IRR og følsomhed.', after=80)

    m.section('LEDELSE OG RESULTATER')
    for label, body in [
        ('Personaleledelse',
         'Personaleansvar for 5 elektrikere og 3 lærlinge hos ELOHVAC: daglig planlægning, 1:1 hver fjortende dag, '
         'MUS/GRUS, kompetencematrix, oplæring og arbejdsmiljøopfølgning (APV, LOTO, risikovurdering).'),
        ('Ledelse uden formel ledelsesret',
         'Førte 25 specialiserede medarbejdere gennem 37 samtidige CAPEX-projekter hos Novo Nordisk og et 14-mands '
         'team hos Ventek-Air — retning, aftaler, interessenter og fremdrift frem for instrukser.'),
        ('Udviklingsforløb og eksekvering',
         '11 parallelle anlægsprojekter fra specifikation til formel aflevering; daglige tavlemøder og '
         'flaskehalsanalyser med markant løft i leveringsevne. Standardiserede arbejdsgange og A3/PDCA i praksis.'),
        ('Kvalificering og forankring',
         'FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA med nul kritiske afvigelser ved aflevering — skrevne '
         'acceptkriterier, test med brugerne og dokumentation, der bliver brugt bagefter.'),
        ('Data, digitalisering og AI',
         'Byggede Python/Claude-værktøjer til tilbud, tidsplaner, KS og KPI med dokumenteret produktivitetsløft over '
         '40 %. Bygger investeringsmodeller med scenarier til udvikling og nye forretningsidéer.')]:
        m.bullet(label, body, after=30)

    m.models_table('VÆRKTØJER OG METODER', ('Opgave', 'Værktøj og dokumenteret anvendelse'), [
        ('Retning og prioritering',
         '30-60-90-dages plan, månedshjul, beslutningsret og RACI. Brugt ved opstart af nye teams og i '
         'CAPEX-porteføljer, hvor flere projekter konkurrerede om de samme folk.'),
        ('Personaleledelse og udvikling',
         'Situationsbestemt ledelse (SLII), delegeringstrappen, 1:1 hver fjortende dag, MUS/GRUS, GROW og SBI. '
         'Kompetencematrix og udviklingsplan pr. medarbejder; lærlinge ført til svendeprøve.'),
        ('Forløb fra behov til løsning',
         'Problemkort og behovsbevis fra interviews og data, prioriteret backlog i det værktøj teamet bruger '
         '(Azure DevOps eller tilsvarende), korte forløb med demo, beslutningspunkter og gevinstmåling. A3 og '
         '5 x hvorfor i rodårsagsanalyse.'),
        ('Data og kundeindsigt',
         'VOC-interviews, kunderejse, henvendelses- og forbrugsdata, KPI-træ med baseline og effektmåling; Power BI '
         'og Python/Claude til dashboards og investeringsmodeller med NPV, IRR og følsomhed.'),
        ('Kvalitet og test',
         'Acceptkriterier, testcases, FAT/SAT og IQ/OQ/PQ, afvigelseshåndtering med ejer og frist, dokumentation og '
         'oplæring af brugere. 0 kritiske afvigelser ved aflevering under GMP.'),
        ('Interessenter og samarbejde',
         'Interessentkort, RACI og eskaleringstrappe; tavlemøder og Gemba. Samarbejde med IT/Digitalisering, '
         'indkøb, leverandører og forretning i system- og anlægsprojekter med SAP ERP, CMMS og SCADA-data.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L-ansvar · erhvervs- og industrikunder',
         [('Personaleledelse', 'Daglig planlægning, 1:1 og MUS, kompetencematrix, arbejdsmiljø og oplæring af '
                               'lærlinge; situationsbestemt ledelse på skiftende opgaver.'),
          ('Forretning og kunde', 'Tilbud, kalkule, prissætning og serviceaftaler med responstid, kvalitet og '
                                  'leveringsevne som KPI’er — direkte kundedialog om behov og løsningsvalg.'),
          ('Digitale værktøjer', 'Python/Claude API til tilbud, tidsplaner, KS-tjeklister og KPI-dashboard; over '
                                 '40 % produktivitetsløft i virksomheden.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024',
         '37 samtidige CAPEX-projekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Tværgående ledelse', 'Fremdrift, økonomi, risici og ressourcer mellem engineering, indkøb og anlæg; '
                                 'interessentkort og faste beslutningspunkter; rapportering til ledelse og bygherre.'),
          ('Test, kvalitet og forankring', 'FAT/SAT og IQ/OQ/PQ uden kritiske afvigelser ved aflevering; A3 og '
                                           '5 x hvorfor i fejlfinding; PDCA-program reducerede '
                                           'energiomkostningerne med 40 %.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter · DKK 2–10 mio. pr. projekt',
         [('Leverance og arbejdsgange', 'Udbud, tilbud, underentreprenører og afleveringspakker. Daglige '
                                        'tavlemøder og flaskehalsanalyser samt standardiserede arbejdsgange gav et '
                                        'markant løft i leveringsevenen.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos, Lynetten · København · aug. 2017–jan. 2022',
         '24/7-drift · pumper, HVAC, højspændingstavler og SCADA · skiftehold',
         [('Drift, data og standarder', 'Forebyggende vedligehold, akut fejlfinding og reservedelsflow på '
                                        'SCADA-data; 5S, Standard Work og PDCA samt LOTO, APV og risikovurdering i '
                                        'skifteholdsdrift.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted',
         [('Plan, mål og læring', 'Vagtplanlægning, materialestyring og målopfølgning; fejldiagnose, '
                                  'rodårsagsanalyse og korrigerende handlinger på industrielt el- og mekanisk udstyr.')]),
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
    m.edu('Lean og forbedringspraksis: 5S, PDCA, VSM, A3, Kaizen', 'Løbende kurser og anvendelse i drift og projekter')
    m.edu('Køleteknik og klimaanlæg · STCW-sikkerhed og maskinrumsvagt',
          'Mercantec 2021 · Søfartsstyrelsen 2021–2023')

    m.section('SPROG, PRAKTISK OG REFERENCER')
    m.para('Dansk og persisk/farsi: modersmål · Engelsk: professionelt i skrift og tale · Kørekort B · Bopæl i Måløv, '
           'ca. 30 minutter fra Ørestads Boulevard. Fleksibel omkring hjemmearbejde og møder på tværs af '
           'forsyningerne. Referencer fra Novo Nordisk og Biofos oplyses efter aftale.', after=70)

    m.models_table('KRAV I OPSLAGET — MIN DOKUMENTATION', ('Krav', 'Dokumentation'), [
        ('Erfaring med ledelse og udvikling i en kompleks organisation',
         'Personaleledelse i egen virksomhed siden 2023; 25 specialister i 37 CAPEX-projekter i GMP-reguleret '
         'industri; 14-mands team i entreprise. Kompleksitet med myndigheds-, kvalitets- og driftskrav.'),
        ('Motivere og udvikle medarbejdere og forskellige fagligheder',
         'Medarbejderudvikling i fast kadence: 1:1 hver fjortende dag, MUS/GRUS, GROW og SBI, kompetencematrix og '
         'udviklingsplan pr. medarbejder; lærlinge ført til svendeprøve. SLII som ramme for ledelsesstil.'),
        ('Agile projekt- og udviklingsmetoder',
         'Korte forløb med synlig tavle, prioriteret opgaveliste, demo undervejs og retrospektiv — fra entreprise og '
         'forbedringsarbejde (PDCA, Kanban, tavlemøder). Ikke Scrum-roller i en produktorganisation; det lærer jeg '
         'af jeres Product Owners.'),
        ('Digitaliseringsprojekter og forretningsbehov',
         'System- og anlægsprojekter med SAP ERP, CMMS, SCADA-data og adgangskontrol; egne Python/Claude-værktøjer '
         'fra behov til løsning i daglig brug med 40 % produktivitetsløft.'),
        ('Kundebehov, data og analyser til konkrete løsninger',
         'Kundedialog og VOC-interviews i egen virksomhed; KPI-træ med baseline og effektmåling; business cases med '
         'NPV, IRR og følsomhed som beslutningsgrundlag.'),
        ('Test, kvalificering og forankring',
         'Acceptkriterier, testcases og IQ/OQ/PQ under GMP med nul kritiske afvigelser; oplæring af brugere og '
         'dokumentation, der bliver brugt efter aflevering.'),
        ('Sparringspartner for forsyningerne og resten af Kundeområdet',
         'Tværgående interessentledelse mellem teknik, indkøb, ledelse og eksterne parter; interessentkort, RACI '
         'og skreven beslutningsret, så ansvar ikke flyder.'),
        ('Uddannelse er ikke afgørende',
         'Elautoriseret maskinmester og B.Tech i teknologiledelse — men det afgørende er 20 års leverance- og '
         'personaleansvar i en kompleks organisation med myndighedskrav, kvalitetskrav og drift i døgndrift.'),
        ('Tydelig, nysgerrig og involverende leder',
         'Fast 1:1-kadence, feedback i SBI-form, beslutninger kommunikeret med begrundelse og frist — og plads til, '
         'at nogen siger højt, at løsningen ikke virker i praksis.')])
    m.page_break()

    m.models_table('FØRSTE 90 DAGE — TEAM, PORTEFØLJE OG LEVERANCER', ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'Møder hver medarbejder til en kort 1:1 om opgaver, kompetencer og hvad der driller. Gennemgår '
         'henvendelsesdata og den tegnede kunderejse sammen med kundeservice og rådgivning. Aftaler med områdechefen, '
         'hvilke leverancer der vejer tungest i de første tre måneder.'),
        ('Dag 30',
         'Overblik over teamets portefølje: hvilke initiativer er i gang, hvem ejer dem, hvad er status, og hvor '
         'mangler der ejerskab. Kompetencematrix og udviklingsplan pr. medarbejder på plads. Første version af '
         'porteføljetavlen med beslutningspunkter.'),
        ('Dag 60',
         'Prioriteret portefølje fremlagt for forsyningerne og Kundeområdet: hvad fortsætter, hvad stopper, hvad '
         'starter. Fast kadence for afstemning med IT/Digitalisering. Kvalificeringspraksis besluttet — '
         'acceptkriterier, test med brugere og hvem der signerer.'),
        ('Dag 90',
         'Første gevinster målt og dokumenteret, en kundesag kørt hele vejen fra behov til drift som reference, og en '
         'status til områdechefen på tid fra behov til beslutning, andel løsninger i brug efter tre måneder og '
         'kundeoplevelse.')])

    m.section('FRA BEHOV TIL LØSNING — SÅDAN ARBEJDER JEG')
    m.para('Jeg starter altid med at gøre problemet konkret: hvem har det, hvor ofte, hvad koster det i tid og '
           'henvendelser, og hvordan ser kunden det. Først derefter taler vi om en løsning. Så deler jeg forløbet i '
           'leverancer, der hver kan tages i brug, frem for en stor aflevering til sidst, og aftaler ved hver '
           'leverance hvem der tester, hvem der godkender, og hvad der skal være sandt, før vi går videre. Det er '
           'den samme model, jeg brugte i CAPEX-projekter med FAT/SAT og IQ/OQ/PQ — bare med kunder og '
           'medarbejdere i stedet for anlæg.', after=80)

    m.section('KUNDEOPLEVELSE ER ET DRIFTSRESULTAT')
    m.para('En god kundeoplevelse opstår ikke i kampagnen. Den opstår i det øjeblik en kunde ringer, og systemet, '
           'svaret og sagsbehandlingen passer sammen. Derfor måler jeg på det, kunderne faktisk gør: hvor mange der '
           'ringer igen om samme sag, hvor lang tid der går til et brugbart svar, og hvad de selv siger i interviews. '
           'Det er de tal, der viser, om en digitalisering har gjort hverdagen lettere — eller bare flyttet arbejdet.',
           after=80)

    m.section('DATA OG KUNDEINDSIGT SOM BESLUTNINGSGRUNDLAG')
    m.para('Data skal ikke bare være tilgængeligt, det skal kunne bruges i et møde. Jeg arbejder med enkelt '
           'KPI-træ: hvad er baseline, hvad er effekten, og hvem ejer tallet. Power BI til de faste visninger, '
           'Python og Claude når der skal regnes på scenarier og business cases — for eksempel hvad en ny service '
           'betyder i sparede henvendelser, bundlinje og driftsomkostning over tre år. Jeg forventer ikke at eje '
           'dataplatformen; jeg forventer at kunne stille de spørgsmål, som Dataværket, Dynamics 365-platformen og IT '
           'skal kunne svare på.',
           after=80)

    m.section('SAMARBEJDE MED FORSYNINGERNE OG IT/DIGITALISERING')
    m.para('Kundeløsninger lykkes i snitfladerne. Forsyningerne ved, hvad der er teknisk muligt og nødvendigt, IT ved, '
           'hvad der er sikkert og vedligeholdeligt, og kundeservice ved, hvad der bliver svært i praksis. Min rolle '
           'er at sørge for, at alle tre er i rummet, når beslutningen bliver taget, og at der ligger en skreven '
           'aftale om ansvar og overlevering bagefter. Når mange initiativer konkurrerer om de samme få udviklere, '
           'skal prioriteringen være synlig — og det, der ikke bliver til noget, skal siges højt i stedet for at '
           'ligge stille.', after=80)

    m.section('TRIVSEL, LÆRING OG ET BÆREDYGTIGT ARBEJDSLIV')
    m.para('Et team, der skal levere udvikling ved siden af drift, kan ikke leve på sprint og heltemod. Jeg planlægger '
           'med plads til sygdom, ferie og det uforudsete, holder møderne korte og skriver beslutninger ned, så de '
           'ikke skal genforhandles. Læring foregår i hverdagen: faglige gennemgange, sidemandsoplæring, en times '
           'videndeling hver anden uge og plads i MUS til, hvad den enkelte gerne vil kunne om et år.', after=80)

    m.section('AI SOM ARBEJDSVÆRKTØJ — OGSÅ I EN KUNDEORGANISATION')
    m.para('Jeg er professionel og aktiv Claude-koder og bruger det dagligt: analyser af henvendelsesdata, udkast '
           'til kundekommunikation der skal redigeres af et menneske, investeringsmodeller og scenarier. Værdien '
           'ligger ikke i værktøjet, men i at en medarbejder kan løfte blikket fra rapporttræk til kundedialog. Det '
           'forudsætter styr på persondata, roller og godkendelser — en forudsætning, jeg respekterer lige så meget '
           'som gevinsten.', after=80)

    return m.save(path, title='Motiveret CV — Teamleder til Kundeløsninger, HOFOR',
                  subject='Personaleledelse, udviklingsforløb og digitalisering i en kundeorienteret organisation',
                  keywords='teamleder, kundeløsninger, personaleledelse, digitalisering, data, kundeindsigt')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_HOFOR_TeamlederKundeloesninger.docx')))
