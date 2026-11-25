# -*- coding: utf-8 -*-
"""Teamleder for elektrikerteamet, Koncern IT (KIT), Københavns Kommune (dansk opslag, frist 09.12.2026).

Dansk opslag -> dansk dokument, 4 sider i masterdesign: brev side 1, CV side 2-3, kravmatrix side 4.
Kontaktpersoner fra opslaget: kontorchef Johannes Leidesdorff og teknisk projektleder Pernille Stage Keil.

STILVALG (style_guard godkendt, 3/3 skift mod #414):
  register     = Den gode stemning (trivsel · omgangtone · balance · sjov · nysgerrigt fagligt miljø
                 · videreuddannelse) — opslagets eget ordforråd om kulturen
  åbningsgreb  = AP (trivselsmålingen som første billede) — det første, opslaget fortæller om teamet,
                 er ikke teknikken, men trivselsscoren
  struktur     = De to strømme (planlagt arbejde og pludseligt opståede opgaver i samme uge)

BRUGERENS KORREKTION + permanent regel: alt tekst humaniseret, menneskeskrevet tone i brev OG CV.

EVIDENSGRÆNSER (brugerbekræftelser 25.11.2026, master §1):
  elautoriseret maskinmester LV/MV/HV — ALDRIG autoriseret elinstallatør (skrives ærligt, opslagets
  ufravigelige krav adresseres direkte). ITIL: ærligt gap. Datacenter-infrastruktur (UPS, strøm,
  køling, nødstrøm, overvågning af serverrum) er bekræftet kompetence uden navngiven arbejdsgiver.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Netværksdrift og Datacenter · Teamleder for elektrikerteamet'
BANNER_RESUME = 'El, infrastruktur og trivsel i Team Elektriker · KIT'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('25. november 2026')
    m.meta('Koncern IT, Københavns Kommune · Teamleder for elektrikerteamet')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Teamleder for elektrikerteamet', bold=True, color='1A1A1A')
    m.para('Kære Johannes Leidesdorff og Pernille Stage Keil,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('I har fuld kraft på maskinerne, skriver I, og resten af opslaget passer med det. '
       'Det første, I fortæller om Team Elektriker, er faktisk ikke teknikken: at teamet i '
       'reglen har en af KITs højeste scorer, når der er trivselsundersøgelser. Team Elektriker '
       'består af seks elektrikere, og jeg læser stillingen som to ting på én gang: at passe på '
       'en funktion, der allerede kører godt, og at få el-opgaverne løst, mens den bliver ved. '
       'Begge dele har jeg prøvet.')

    lp('Opgaverne kommer i to slags, og I har selv et navn for det: en god balance mellem '
       'planlagte og pludseligt opståede opgaver. Min hverdag med el-service hos erhvervskunder '
       'var bygget på samme måde. Et sjak med elektrikere og lærlinge, et telefonnummer der '
       'ringer midt i det hele, og en plan tydelig nok til, at folk selv kunne flytte rundt på '
       'den. Bag planen lå regnestykket: fuldt P&L-ansvar, akkord og opmåling, budgetopfølgning '
       'hver måned. Et godt øje til økonomien har jeg haft i praksis. Arbejdet hos jer løber fra '
       'datacenteret og helt ud på kommunens godt 1.100 lokationer på det kablede og trådløse '
       'netværk, og det mønster genkender jeg.')

    lp('El-faget er fundamentet. Tavler, styring, føringsveje, kabeltræk, fiber, PDS, UPS og '
       'adgangskontrol, og drift og vedligehold af datacenter-infrastruktur med strøm, køling, '
       'nødstrøm og overvågning af serverrum. Det, I kalder en dyb elektrikerfaglighed og '
       'forståelse for infrastrukturområdet, ligger der. Den faglige del af ledelsesopgaven tager '
       'jeg alvorligt: kontorchefen skal kunne spørge mig til el-faget og få et svar, der holder, '
       'og teamet skal kunne mærke, at nogen tager det faglige ansvar.')

    lp("To ting skal jeg være ærlig om, før vi spilder hinandens tid. Den ene: I skriver "
       "'uddannet elektriker og autoriseret el-installatør' som et ufravigeligt krav. Min "
       'autorisation er en dansk elautorisation LV/MV/HV som elautoriseret maskinmester fra '
       'Sikkerhedsstyrelsen, og jeg er elektriker og elektromekaniker fra bunden. Men '
       'autoriseret elinstallatør er jeg ikke, og det påstår jeg ikke at være. Vurder selv, om '
       'elautorisationen og fagligheden dækker det, I skal bruge. Den anden: kendskab til '
       'ITIL-processerne har jeg ikke på papiret. Dem må jeg lære hos jer, og implementeringen '
       'af nye tiltag er en lederopgave, jeg kender fra kvalitets- og driftssystemer, der var '
       'nye, før jeg kom.')

    lp("Som I skriver: 'Vi kan nemlig godt lide at have det sjovt, mens vi løser vores "
       "opgaver.' Den slags står sjældent i opslag, og når den gør, er det som regel, fordi "
       'det passer. En god omgangtone med plads til alle lægger jeg vægt på, og på at folk '
       'siger tingene ligeud, før de vokser sig store. At skabe og vedligeholde den gode '
       'stemning i løbet af arbejdsdagen er en del af jobbet hos mig, ikke en bonus. Socialt '
       'samvær og et nysgerrigt fagligt miljø på tværs af kompetencer er ikke bløde ord i min '
       'verden; det er sådan fejl undgår at blive gemt væk. Rammen, I beskriver, kan jeg også '
       'lide: snittet mellem autonomi i opgaveløsningen og aktiv, synlig ledelse. Det er dér, '
       'jeg arbejder bedst. Og et balanceret familieliv ved siden af et sjovt kontor passer '
       'mig fint.')

    lp("KIT's mål om at skabe en mærkbar forskel i Københavns Kommune tiltaler mig. At gøre "
       'digitalisering enklere og styrke grønnere og mere brugervenlige IT-løsninger, mens I '
       'leverer stabil og sikker IT-drift til over 45.000 medarbejdere hver dag, er en bund, '
       'man kan stå på som fagmand.')

    lp('De første 90 dage står som en plan side 3 i CV\'et, ikke som løfter. De første 30 dage '
       'lærer jeg teamet, opgaverne og ITIL-processerne at kende. Derefter tager jeg fat i '
       'planlægningen af de to strømme og på økonomien. Til sidst udviklingsdelen sammen med '
       'kontorchefen, for teamets fortsatte udvikling er en del af opgaven. En ambition om at '
       'blive en endnu bedre leder følger med mig, og jeg er ikke bleg for at inddrage din '
       'chef, når der er behov for det. Stillingen er på 37 timer om ugen efter gældende '
       'overenskomst, og jeg kan starte den 1. februar 2027. Ring endelig, hvis der er noget, '
       'I vil have uddybet, inden I læser videre.', after=44)

    lp('Med venlig hilsen', after=8)
    lp('Shahram Ajloo', after=8)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Teamleder for elektrikere med el-faget fra bunden. De seneste år med personaleledelse '
           'af fem elektrikere og tre lærlinge, el-service og entreprise for erhvervskunder, og '
           'drift og vedligehold af datacenter-infrastruktur: UPS, strøm, køling, nødstrøm og '
           'overvågning af serverrum. Før det 24/7-drift på renseanlæg med SCADA og HV-tavler, '
           'commissioning af 37 projekter på Novo Nordisk under GMP/FDA/EMA og værkstedsledelse '
           'for 12 teknikere. Elautoriseret maskinmester (LV/MV/HV) og PRINCE2-certificeret; '
           'jeg bygger selv små værktøjer i Python og Claude til planlægning og opfølgning.',
           after=32)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester (el-teknik og ventilation)',
         'Data Power Consultant ApS · København · 2024 – nu',
         'AI-afdeling 4-10 personer · el-service og entreprise · 5 elektrikere + 3 lærlinge',
         [('', 'Leder AI-afdelingen med 4 til 10 personer: tilbud, kunder, og hvordan løsninger '
               'bliver bygget og dokumenteret. Investeringstilbud på nye forretninger og '
               'månedlig KPI-opfølgning.'),
          ('', 'El-service og entreprise for erhvervskunder: installation, tavler, styring, '
               'fejlfinding og vedligehold på el, ventilation og klima. UPS, fiber, PDS, '
               'ABA/ABV og adgangskontrol hører med.'),
          ('', 'Fem elektrikere og tre lærlinge i den daglige ledelse. Planlægning, 1:1, MUS, '
               'oplæring og arbejdsmiljø: LOTO, APV og risikovurdering ved opstart.')]),
        ('Ejer / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 – nov. 2026 (virksomheden lukket)',
         'Erhvervskunder · el, ventilation og klima · entreprise · fuldt P&L',
         [('', 'El-tekniske opgaver fra akutte udkald til afleveret anlæg: installation, tavler, '
               'styring, fejlfinding og forebyggende vedligehold.'),
          ('', 'Tilbud og beregning, planlægning, materialestyring, underentreprenører, KS, '
               'dokumentation og aflevering med fuldt P&L-ansvar. Akkordbreve og opmåling '
               'hørte også til.'),
          ('', 'Personaleledelse af 5 elektrikere og 3 lærlinge: daglig planlægning, 1:1 og MUS, '
               'struktureret oplæring og arbejdsmiljøopfølgning. Nul kritiske afvigelser i '
               'serviceaftalerne.')]),
        ('Senior commissioningeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, DKK 2-10 mio. · 25 specialister · GMP/FDA/EMA',
         [('', 'Commissioning og projektledelse på 37 CAPEX-projekter, DKK 2-10 mio. pr. stk. '
               'FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA, nul kritiske fund ved afleveringen.'),
          ('', 'Månedsrapport til ledelse og kunde: fremdrift, økonomi, risici og ressourcer. '
               '25 specialister på tværs af engineering, indkøb og drift. SAP ERP til '
               'økonomidata.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022 – nov. 2022',
         '11 samtidige projekter · 14 mand · DKK 2-10 mio.',
         [('', '11 samtidige projekter og et team på 14 mand. Daglige tavler for kapacitet og '
               'fremdrift. Sikkerhedsdokumentation og afleveringspakker i hvert projekt.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · SCADA, PLC, HV-tavler · skiftehold',
         [('', 'Vedligehold og drift af pumper, HVAC, HV-tavler og SCADA døgnet rundt. Planlagt '
               'vedligehold og fejlfinding, og 5S og Standard Work i værkstedet. Skiftehold med '
               'LOTO, APV og nærved-hændelser.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('', 'Ledelse af 12 mekanikere og teknikere i maskinværksted: vagtplan, materialer og '
               'mål. Fejlfinding på industrielt udstyr, analyse af rodårsag og korrigerende '
               'handlinger.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('UDDANNELSE OG CERTIFIKATER')
    m.edu('B.Tech (EQF6), teknologiledelse og maskinteknik',
          'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12')
    m.edu('Dansk elautorisation LV/MV/HV som elautoriseret maskinmester',
          'Sikkerhedsstyrelsen · maj 2023')
    m.edu('El- og maskinteknisk design, elteknik (EQF6)',
          'Tehran Technical University · 2000–2003')
    m.edu('PRINCE2, certificeret projektleder', 'AXELOS / PeopleCert')
    m.edu('Køleteknik og klimaanlæg (AMU)',
          'Mercantec · 2021 · STCW 2021–2023, Søfartsstyrelsen')
    m.para('Lean- og Six Sigma-praksis uden certifikat: DMAIC, 5S, PDCA, VSM, A3, Kaizen, '
           'Standard Work, SMED, TPM, 5xHvorfor, Ishikawa og FMEA, brugt i dokumenteret arbejde '
           'med vedligehold, kvalitet og planlægning.', after=48)

    m.section('SPROG, VÆRKTØJER OG PRAKTISK')
    m.para('Dansk (modersmål) · engelsk (professionelt) · persisk (modersmål). Værktøjer: '
           'SAP ERP, CMMS, Power BI og KPI-opfølgning, Excel og Python, Claude til tjeklister og '
           'rapporter, PRINCE2 til projektstruktur. Kørekort B. Bor i Måløv og tager gerne '
           'opgaver i Storkøbenhavn og på Sjælland. Kan starte 1. februar 2027.', after=48)

    m.section('KOMPETENCER')
    for label, body in [
        ('El og infrastruktur',
         'Tavler, styring, føringsveje, kabeltræk, fiber, PDS, UPS, ABA/ABV, adgangskontrol og '
         'nød- og panikbelysning. DS/HD 60364 og SB-vejledningen som faglig basis.'),
        ('Datacenter-infrastruktur',
         'Drift og vedligehold af UPS, strøm, køling, nødstrøm og overvågning af serverrum.'),
        ('Ledelse',
         'Daglig personaleledelse, 1:1 og MUS, situationsbestemt ledelse (SLII), GROW og SBI i '
         'samtalerne, tavlemøder og visuel ledelse.'),
        ('Metoder og ITIL',
         'PRINCE2, Lean-praksis (5S, PDCA, A3, 5xHvorfor, Ishikawa, FMEA), risikovurdering og '
         'APV. Kendskab til ITIL-processerne står ikke på mit cv endnu; processerne lærer jeg '
         'hos jer.'),
    ]:
        m.bullet(label, body, after=10)

    m.section('DE FØRSTE 90 DAGE')
    m.para('En plan for de første 90 dage, som I kan holde mig op på:', after=12)
    for b in [
        'Dag 1-30: Lære teamet og opgaverne at kende. Jeg tager med ud på opgaver, gennemgår '
        'det løbende arbejde og lærer ITIL-processerne hos jer. Aftaler med kontorchefen, '
        'hvordan den faglige dialog skal køre, og hvornår jeg kalder på hjælp.',
        'Dag 31-60: Planlægning af de to strømme. Det planlagte arbejde sat i system, de akutte '
        'opgaver prioriteret åbent, så alle kan se, hvad der er vigtigst. 1:1 med alle seks og '
        'et kig på budget og økonomi omkring teamet.',
        'Dag 61-90: Udvikling. Forslag til hvor I kan blive endnu bedre, en plan for teamets '
        'videreuddannelse og min egen, og en samtale med kontorchefen om hvor teamet skal hen '
        'det næste års tid.',
    ]:
        m.bullet('', b, after=10)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Koncern IT · Teamleder for elektrikerteamet · Netværksdrift og Datacenter',
                   ('Krav i opslaget', 'Dokumenteret erfaring'), [
        ('har B-kørekort, hvilket er et ufravigeligt krav',
         'B-kørekort (manuelt gear) dokumenteret og brugt i job siden 2003, hvor opgaverne '
         'kræver bil mellem adresser. Bor i Måløv og kører gerne til opgaver på kommunens godt '
         '1.100 lokationer.'),
        ('er uddannet elektriker og autoriseret el-installatør',
         'Også ufravigeligt krav i opslaget. Ærligt svar: elautoriseret maskinmester med dansk '
         'elautorisation LV/MV/HV fra '
         'Sikkerhedsstyrelsen (maj 2023), elektriker og elektromekaniker fra bunden siden 2003. '
         'Autoriseret elinstallatør er jeg ikke, og det påstår jeg ikke at være (se også side 1).'),
        ('har en del erfaring fra en tilsvarende opgave',
         'Direkte personaleledelse af 5 elektrikere og 3 lærlinge siden 2023 med el-opgaver hos '
         'erhvervskunder, drift og vedligehold af datacenter-infrastruktur (UPS, strøm, køling, '
         'nødstrøm, overvågning), og før det 14 mand i entreprise og 12 i værksted.'),
        ('har en dyb elektrikerfaglighed og forstår infrastrukturområdet',
         'El-faget fra bunden siden 2003: tavler, styring, føringsveje, kabeltræk, fiber, PDS, '
         'UPS, ABA/ABV og adgangskontrol. DS/HD 60364 og SB-vejledningen som basis. Infrastruktur '
         'til datacenter og 1.100 lokationer er den samme disciplin i forskellig skala.'),
        ('har kendskab til ITIL-processerne og ved, hvordan man som leder understøtter '
         'implementeringen af nye tiltag',
         'Kendskab til ITIL-processerne har jeg ikke på papiret, og det stod også på side 1. '
         'Implementeringen af nye tiltag kender jeg: nye kvalitets- og driftssystemer indført på '
         'Biofos og Novo Nordisk (GMP/FDA/EMA fra 2022), og nye arbejdsgange via PDCA med 40% '
         'lavere energiforbrug som resultat.'),
        ('helt sikkert har en ambition om at blive en endnu bedre leder',
         'PRINCE2 taget ved siden af jobbet, og løbende efteruddannelse i ledelse (SLII, GROW, '
         'SBI). Over 10 års personaleledelse i alt (2003-2010 og 2023-2026), og ambitionen om at '
         'blive en endnu bedre leder er grunden til, jeg søger netop et team med jeres kultur.'),
        ('arbejder struktureret og har et godt øje for de enkelte indsatsers og projekters mål',
         '37 CAPEX-projekter styret med faste mål for tid, økonomi og kvalitet, 11 samtidige '
         'entrepriser med daglige tavler for kapacitet og fremdrift, og PRINCE2 som ramme. Målene '
         'for den enkelte indsats følges op i 1:1 og på tavlen.'),
        ('ikke er bleg for at inddrage din chef, når der er behov for det',
         'Månedsrapport til ledelse og kunde som projektleder siden 2022, og tæt dialog med '
         'bestyrelse og kunder som direktør. Jeg siger til, når noget kræver en beslutning oven '
         'på, hellere en dag for tidligt end en uge for sent.'),
        ('daglig direkte personaleledelse, herunder den faglige del af ledelsesopgaven, for de '
         'seks kolleger i teamet',
         'Daglig personaleledelse af 5 elektrikere og 3 lærlinge (2023-2026) og tidligere 12 '
         'mekanikere og teknikere. Planlægning, 1:1, MUS og oplæring, og den faglige del af '
         'ledelsesopgaven: jeg tager selv el-spørgsmålene og står på mål for svaret.'),
        ('har et godt øje til økonomien omkring teamet',
         'Fuldt P&L-ansvar siden 2023, budgetopfølgning hver måned, akkordbreve og opmåling, og 37 '
         'projekter på DKK 2-10 mio. med omkostningsopfølgning i SAP ERP. Økonomien omkring '
         'teamet følger jeg månedligt, ikke ved årsafslutningen.'),
        ('er fagligt ansvarlig for teamets elektrikeropgaver over for kontorchefen',
         'Elautoriseret maskinmester (LV/MV/HV) med over 20 års el-tekniske opgaver. Som ejer og '
         'teknisk direktør bar jeg det faglige ansvar over for kunder og myndighedsdialog; over '
         'for en kontorchef er opgaven den samme, bare tættere på.'),
        ('sørger for en god balance mellem planlagte og pludseligt opståede opgaver',
         'Hverdagen som el-serviceleder var netop de to strømme: 11 samtidige projekter og et sjak '
         'på 8 mand med akutte udkald imellem. Balancen blev holdt med en plan, alle kunne flytte '
         'rundt på, og en åben prioritering, når noget måtte vige.'),
        ('har en stor rolle i at sikre teamets trivsel, som i reglen har en af KITs højeste scorer',
         'Trivsel i praksis: 1:1 og MUS til alle 8 i teamet, arbejdsmiljøopfølgning med APV og '
         'nærved-hændelser på skiftehold og byggeplads, og struktureret oplæring af 3 lærlinge. '
         'Et team der fungerer, kan ses i kvaliteten: nul kritiske afvigelser 2023-2026.'),
        ('er i tæt dialog med kontorchefen om både de daglige opgaver og teamets fortsatte '
         'udvikling',
         'Som direktør i tæt dialog med bestyrelse og kunder hver uge, og som projektleder med '
         'månedsrapport til ledelsen siden 2022. Udvikling af teamet: struktureret oplæring, '
         'kompetencematricer og forslag til videreuddannelse, fx efteruddannelse af lærlinge.'),
        ('drive og opdatere vores LAN-netværk',
         'El-siden af netværksarbejdet kender jeg: strøm, UPS og føringsveje til udstyr, fiber og '
         'PDS-kabling, og opdatering af installationer hos erhvervskunder siden 2023. '
         'Datacenter-infrastruktur med overvågning og nødstrøm er bekræftet erfaring fra driften.'),
        ('står for elektrikeropgaver i den forbindelse',
         'El-opgaver for datacenter og lokationer: installation, tavler, fejlfinding og '
         'vedligehold fordelt på mange adresser. 11 projekter på flere adresser samtidig og '
         'service hos erhvervskunder med UPS, fiber, PDS og adgangskontrol i blandingen.'),
        ('nysgerrig, kreativ og metodisk omkring din lederopgave',
         'Nysgerrig: jeg bygger selv værktøjer i Python og Claude til tjeklister og rapportering '
         '(siden 2024). Metodisk: PRINCE2, A3 og 5xHvorfor til problemløsning. Kreativ: nye '
         'arbejdsgange indført via PDCA med målbart fald i energiomkostninger på 40%.'),
    ], widths=(3400, 6946), compact=True)
    m.para('**Kontorchef Johannes Leidesdorff (20 58 27 80) og teknisk projektleder Pernille '
           'Stage Keil (29 29 05 28) er opslagets kontaktpersoner. Jeg kan træffes på +45 93 99 '
           '95 14 eller ajlooshahram@gmail.com.**', after=8)

    m.save(path, title='Teamleder for elektrikerteamet - Koncern IT')
    print(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_KoncernIT_TeamlederElektrikerteamet.docx'))
