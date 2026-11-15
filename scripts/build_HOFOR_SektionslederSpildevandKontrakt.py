# -*- coding: utf-8 -*-
"""HOFOR A/S — Sektionsleder til HOFOR Spildevand Kontrakt (Smedeholm / Kløvermarken).

Dansk leverance. Opslaget beder om et **motiveret CV** uden ansøgning:
motivationsside først, derefter CV i samme dokument.
Kultur- og rolleintel: master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md (HOFOR-afsnit).
Policy: master/README.md — ekstrem sikkerhed, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Sektionsleder · Spildevand, kontraktstyring og sikker drift'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('5. november 2026')
    m.meta('HOFOR A/S · Spildevand Kontrakt · Smedeholm (Herlev) og Kløvermarken')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Motiveret CV: Sektionsleder til HOFOR Spildevand Kontrakt', bold=True, color='1A1A1A')
    m.para('Til områdechef Thomas Jensen', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('Spildevand tager ikke fri. Det er den slags drift, hvor en stoppet pumpestation klokken tre om natten '
           'bliver et problem for tusind mennesker, inden nogen har haft mulighed for at ringe til nogen — og hvor '
           'den ro, der kendetegner en velfungerende drift, er noget, nogen har arbejdet for. Den ro bliver skabt i '
           'en sektion som den, I nu opbygger: kontrakter der er skrevet, så de kan følges op, entreprenører der '
           'ved, hvad de er hyret til, arbejdsmiljø der er taget al Vor, og et budget der hænger sammen med det, '
           'driften faktisk laver. Det er den slags ledelse, jeg søger hos HOFOR — i en forsyning, der skal understøtte en bæredygtig udvikling i hovedstadsområdet, ikke kun holde driften kørende.', after=80)

    m.para('**Jeg vil bygge og lede sektionen på fire faste ting.** Først **kontrakterne som driftsinstruks**: for '
           'hver udliciteret opgave en tydelig afgrænsning, målbare krav til kvalitet og responstid, en fast '
           'tilsynsrytme og en opfølgning, hvor betaling følger det leverede — ikke det lovede. Dernæst '
           '**arbejdsmiljøet som ledelsesarbejde**: jeg vil være den, der går forrest på sikker drift, fordi en '
           'sektionsleder, der kun taler om sikkerhed til møder, ikke ændrer adfærd på stedet. Hændelser skal '
           'efterforskes for at lære, ikke for at fordele skyld, og entreprenører skal have de samme krav som egne '
           'folk. Så **økonomien**: budget og driftsøkonomi fulgt på den enkelte opgave, aktivering af anlæg '
           'dokumenteret og afstemt med den, der fører regnskabet, og en månedlig opfølgning der kan læses af både '
           'driftsfolk og ledelsesgruppen i Spildevand. Og endelig **menneskerne**: to teams med medarbejdere og '
           'ledere med forskellig faglighed, anciennitet og uddannelsesbaggrund skal have en tydelig retning, en '
           'fast kadence og en leder, der er til stede på begge lokationer.', after=80)

    m.para('Jeg har prøvet alle fire dele med ansvar for resultatet — og på netop det område, sektionen skal '
           'understøtte. I fem år var jeg **drifts- og vedligeholdelsesleder på Lynetten under Biofos**, et af landets '
           'største spildevandsanlæg: 24/7-drift med vand, slam, pumper, ventilation og højspænding, personaleledelse '
           'af skiftende teams, arbejdsmiljø og sikker drift i hverdagen, entreprenører og leverandører på pladsen, '
           'myndighedskrav og miljødokumentation — og et anlæg, der ikke måtte stoppe. Jeg førte tilsyn, '
           'prioriterede vedligehold efter tilstand, gennemførte energiledelse med **over 40 % lavere energiforbrug** '
           'som dokumenteret resultat og lærte, at den bedste dokumentation er den, der bliver skrevet, mens arbejdet '
           'foregår.', after=80)

    m.para('Kontrakt- og økonomisiden har jeg fra to sider af bordet. Hos **Novo Nordisk** løftede jeg **37 '
           'parallelle kapitalprojekter** med 25 specialister og 2–10 mio. kr. pr. projekt: leverandør- og '
           'kontraktstyring, acceptkriterier, afvigelser og auditeret aflevering med **nul kritiske fund**. I '
           '**Ventek-Air** var jeg projekt- og værkstedsleder for **14 medarbejdere og 11 samtidige opgaver** med '
           'tilbud, underleverandører og afleveringspakker, og i **ELOHVAC**, som jeg har drevet siden 2023, har jeg '
           'fuldt P&L med fem håndværkere og tre lærlinge — dér er udlicitering, indkøb, kontrakter og økonomi ikke '
           'teori, men det, der afgør, om måneden går op. Jeg ved, hvordan en entreprenør læser en kontrakt, og '
           'hvor de gråzoner opstår, der koster penge og tid senere.', after=80)

    m.para('At **opbygge noget nyt** har jeg gjort før, og det er den del, der tiltrækker mig mest. En ny sektion '
           'skal ikke starte med et organisationsdiagram, men med et kort: hvilke opgaver, kontrakter og lokationer '
           'skal sektionen bære, hvem gør hvad i dag, og hvor falder bolden mellem to stole? Derfra kommer '
           'arbejdsdelingen, tilsynsrutinen og den faste kadence med **Indkøb, Vand Planlægning og Vand Analyse** af '
           'sig selv. Jeg vil hellere bruge de første uger på at forstå driften på Kløvermarken og Smedeholm end på '
           'at tegne en struktur, der ikke passer til virkeligheden — og jeg vil gerne være lokationsansvarlig på '
           'Smedeholm med den nærhed, det kræver. Ledelse gennem nærvær og tydelighed er ikke et slogan for mig: '
           'det betyder, at medarbejderne ved, hvad der forventes i morgen, og at de ser mig på pladsen, når '
           'forventningen skal indfries.', after=80)

    m.para('HOFORs arbejdspladsløfte — **"Hos os får du plads"** — rammer noget, jeg lægger vægt på som leder: plads '
           'til fællesskab på tværs af fagligheder, plads til udvikling, og plads til et arbejdsliv, der også holder '
           'om ti år. Jeg deler også jeres udgangspunkt i, at beslutninger træffes på et **oplyst grundlag**, og at '
           '**data og analyser** er fundamentet for prioritering. Det er præcis den måde, jeg har arbejdet på: målinger '
           'og driftstal fra SCADA og målere, sammenlignet og brugt til at vælge de rigtige indsatser først — og en '
           'opfølgning, der viser, om det virkede.', after=80)

    m.para('Praktisk: jeg bor i Måløv, har ti minutter til Smedeholm og omkring en halv time til Kløvermarken, og '
           'kørekort B til at komme rundt mellem lokationerne. Jeg er indforstået med **sikkerhedsgodkendelse til '
           '"Fortroligt"** og kan gennemgå den og opretholde den gennem ansættelsen. **Microsoft Dynamics 365** '
           'kender jeg godt: sager, kontrakter og økonomi er den samme opbygning som i SAP og de øvrige '
           'ERP-systemer, jeg har indført og arbejdet i som leder, så sektionen får et system, der bliver brugt og '
           'ikke bare fyldt. Jeg kommunikerer sikkert på dansk og begår mig på engelsk. Jeg vil gerne høre, hvilke kontrakter '
           'og opgaver sektionen skal tage over først — så ved jeg, hvor jeg skal begynde.', after=70)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Drifts- og sektionsleder med 20+ års erfaring fra spildevand, teknisk drift og entreprise — '
           'elautoriseret maskinmester med B.Tech i Technology Management & Mechanical Engineering. Fem år som '
           'drifts- og vedligeholdelsesleder på et af landets største spildevandsanlæg med 24/7-drift, '
           'personaleledelse af skiftende teams, arbejdsmiljø, entreprenører, myndighedskrav og over 40 % lavere '
           'energiforbrug som dokumenteret resultat. Har styret kontrakter, leverandører og økonomi i 37 '
           'kapitalprojekter under GMP og i egen virksomhed med fuldt P&L siden 2023. Leder gennem nærvær, tydelig '
           'kommunikation og følgeskab — på flere lokationer og på tværs af fagligheder.', after=80)

    m.section('DRIFT, KONTRAKT OG ARBEJDSMILJØ')
    for label, body in [
        ('Kontraktstyring og udlicitering',
         'Afgrænsning, kvalitets- og responstidskrav, tilsynsrytme og opfølgning pr. kontrakt; betaling knyttet til '
         'det leverede — effektiv kontraktstyring, hvor ændringer er dokumenteret, før arbejdet udføres.'),
        ('Sikker drift og arbejdsmiljø',
         'Arbejdsmiljø som ledelsesopgave i 24/7-drift: APV, arbejdstilladelser, LOTO, hændelses­undersøgelse med '
         'læring og skærpede krav til entreprenører på pladsen.'),
        ('Økonomi og aktivering',
         'Budget og driftsøkonomi fulgt pr. opgave og lokation, aktivering af anlæg dokumenteret og afstemt, '
         'månedlig opfølgning der kan læses af driftsfolk og ledelse; fuldt P&L i egen virksomhed.'),
        ('Personaleledelse på flere lokationer',
         'To teams med medarbejdere og ledere med forskellig faglighed og anciennitet: tydelig retning, engagement, fast '
         'kadence, MUS og udvikling, og nærvær på begge lokaliteter.'),
        ('Interessenter og data',
         'Indkøb, planlægning, analyse og entreprenører i samme rytme; driftstal fra SCADA og målere brugt som '
         'grundlag for prioritering og opfølgning — ikke som rapportering bagefter.')]:
        m.bullet(label, body, after=25)

    m.models_table('VÆRKTØJER OG METODER', ('Opgave', 'Værktøj og dokumenteret brug'), [
        ('Kontrakt og leverandør',
         'Kontraktgennemgang, KPI\'er og tilsynsplan, leverandørmøder og afvigelsesopfølgning; udbudsmateriale og '
         'tilbudsevaluering fra egen virksomhed og fra kapitalprojekter.'),
        ('Drift og vedligehold',
         'Tilstandsbaseret vedligehold, reservedelskritikalitet, kalibrering og fejlretning; skiftplanlægning og '
         'beredskab i 24/7-drift med akutopkald uden for normal arbejdstid.'),
        ('Arbejdsmiljø og sikkerhed',
         'APV, arbejdstilladelser, LOTO, kemikalier og løft; hændelsesundersøgelse med rodårsag og lukkede '
         'handlinger; sikkerhedsorganisation og entreprenørkrav.'),
        ('Økonomi og systemer',
         'Budget, timeforbrug og driftsøkonomi pr. opgave; SAP og Excel i daglig brug, Microsoft Dynamics 365\'s '
         'logik med sager, kontrakter og økonomi.'),
        ('Data og analyse',
         'SCADA- og målerdata normaliseret og sammenlignet; energiledelse med over 40 % reduktion, KPI-tavler og '
         'opfølgning bygget i Python og Excel.'),
        ('Ledelse',
         'MUS og udviklingssamtaler, kompetencematrix pr. medarbejder, 1:1 i fast rytme, delegering med klare '
         'rammer, prioritering af sektionens ressourcer og tydelig opfølgning; administration af sager og kontrakter i '
         'faste systemer.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 håndværkere og 3 lærlinge · fuldt P&L · private og erhvervsmæssige kunder',
         [('Økonomi og kontrakter', 'Budget, tilbud, kontrakter, indkøb og underleverandører; dækningsgrad og '
                                    'timeforbrug fulgt pr. sag, og kunden informeret samme dag noget ændrer sig.'),
          ('Drift og sikkerhed', 'Tavler, drev og styringer specificeret, installeret og testet; arbejdsmiljø og '
                                 'sikkerhed på pladsen uden undtagelser.')]),
        ('Senior commissioning engineer / projektleder, elsystemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Kontrakt og leverandør', 'Leverandør- og kontraktstyring, acceptkriterier, afvigelser og auditeret '
                                      'aflevering med nul kritiske fund.'),
          ('Opfølgning', 'Tid, økonomi og risiko rapporteret månedligt til ledelse og kunde; grænseflader mod andre '
                         'fag styret.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige opgaver · 2–10 mio. kr. pr. projekt',
         [('Drift og koordinering', 'Tilbud, underleverandører og afleveringspakker; daglige tavlemøder, '
                                     'flaskehalsanalyse og omprioritering uden at tabe kvalitet.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Lynetten under Biofos · København · aug. 2017–jan. 2022',
         'Spildevandsanlæg i 24/7-drift · vand, slam, pumper, ventilation, højspænding og SCADA',
         [('Drift, personale og tilsyn', 'Skiftplanlægning og personaleledelse af driftsmedarbejdere; tilsyn, '
                                         'forebyggende vedligehold og akutopkald; arbejdsmiljø og sikker drift i '
                                         'hverdagen.'),
          ('Entreprenører og myndighed', 'Entreprenører og leverandører koordineret på pladsen; miljødokumentation, '
                                         'arbejdstilladelser og myndighedskrav overholdt i et anlæg, der ikke måtte '
                                         'stoppe.'),
          ('Energi og økonomi', 'Energiledelse på store anlægsmasser med data fra målere og SCADA: over 40 % lavere '
                                'energiforbrug, dokumenteret og fastholdt.')]),
        ('Elektromekaniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · industrielt udstyr',
         [('Team og oppetid', 'Vagtplanlægning og opfølgning på mål; fejlretning, rodårsagsanalyse og korrigerende '
                              'handlinger på produktionsudstyr.')]),
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
    m.edu('Køle- og ventilationsteknik · STCW sikkerhed', 'Mercantec 2021 · Søfartsstyrelsen 2021')

    m.section('SPROG, PRAKTIK OG REFERENCER')
    m.para('Dansk: modersmål · Engelsk: professionelt · Persisk: modersmål · Kørekort B · Bor i Måløv, ti minutter '
           'fra Smedeholm og ca. en halv time fra Kløvermarken · Indforstået med sikkerhedsgodkendelse til '
           '"Fortroligt" · Kan starte efter aftale · SAP og Excel dagligt, Python til data og opfølgning · '
           'Referencer på forespørgsel.', after=70)

    m.models_table('DET EFTERSPØRGER DE — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Erfaring med ledelse i en driftsorienteret organisation',
         'Fem år som drifts- og vedligeholdelsesleder på et spildevandsanlæg i 24/7-drift; projekt- og '
         'værkstedsleder for 14 medarbejdere og 11 samtidige opgaver; indehaver med fuldt P&L og fem håndværkere '
         'og tre lærlinge siden 2023.'),
        ('Personaleledelse af driftsmedarbejdere',
         'Skiftplanlægning, MUS, udviklingssamtaler, oplæring og daglig ledelse af driftsmedarbejdere og teknikere; '
         'rekruttering og lærlingeansvar i egen virksomhed.'),
        ('Erfaring med arbejdsmiljøledelse',
         'APV, arbejdstilladelser, LOTO og hændelsesarbejde i 24/7-drift; arbejdsmiljø som fast punkt på '
         'ledelsesmøder og ude på pladsen, også over for entreprenører.'),
        ('Forståelse for økonomistyring',
         'Budget, driftsøkonomi og dækningsgrad fulgt pr. opgave; aktivering og afstemning dokumenteret; fuldt P&L '
         'med ansvar for bundlinjen siden 2023.'),
        ('Erfaring med udlicitering af driftsopgaver',
         'Underleverandører og entreprenører styret gennem afgrænsning, kvalitetskrav, tilsyn og opfølgning; '
         'udbudsmateriale, tilbudsevaluering og kontrakt i egen virksomhed og i kapitalprojekter.'),
        ('Professionel kontraktstyring og samarbejde med Indkøb, Planlægning og Analyse',
         'Kontrakter og leverandører styret i 37 projekter under GMP med nul kritiske fund; tværfagligt samarbejde '
         'med indkøb, planlægning, myndighed og entreprenører i både drift og projekt.'),
        ('Frontfigur for arbejdsmiljø og sikker drift',
         'Sikkerhed og arbejdsmiljø ledet i praksis på en 24/7-lokalitet: tilladelser før arbejde, tydelige krav, '
         'læring af hændelser og konsekvent opfølgning — også når det koster en dag.'),
        ('Opfølgning på aktivering og økonomi i spildevandsdriften',
         'Driftsøkonomi og anlægsaktiver fulgt i et spildevandsanlæg med 24/7-drift; investeringer og aktivering '
         'dokumenteret og afstemt med økonomifunktionen i 37 kapitalprojekter.'),
        ('Analytisk, nysgerrig og beslutter på et oplyst grundlag',
         'Energiledelse bygget på målinger og SCADA-data frem for antagelser; økonomi og drift fulgt pr. opgave med '
         'tal, der kan læses af andre; analyse af rodårsager ved afvigelser og hændelser.'),
        ('Dansk og engelsk, Microsoft Dynamics 365, kørekort',
         'Dansk modersmål og engelsk professionelt; SAP og Excel dagligt; D365 med sager, kontrakter og økonomi '
         '— samme opbygning som de ERP-systemer, jeg har indført og brugt; kørekort B og mobil mellem '
         'Smedeholm og Kløvermarken.')])
    m.page_break()

    m.models_table('DE FØRSTE 90 DAGE — KORTET, KONTRAKTERNE OG KULTUREN', ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'Ud på Kløvermarken og Smedeholm med medarbejdere og ledere, og ud på anlæggene med dem, der har '
         'vagten. Gennemgang af de kontrakter, opgaver og lokationer sektionen skal bære, og af hvordan '
         'arbejdsmiljøet bliver fulgt i dag.'),
        ('Dag 30',
         'Et kort over sektionen: opgaver, kontrakter, lokationer, ansvar og de steder, hvor bolden falder mellem to '
         'stole. Arbejdsdeling og tilsynsrytme lagt fast, og den faste kadence med Indkøb, Vand Planlægning og Vand '
         'Analyse aftalt.'),
        ('Dag 60',
         'Kontrakterne gennemgået med krav, KPI\'er og tilsynsplan; økonomien fulgt pr. opgave og lokation på ét '
         'ark, som ledelsesgruppen kan læse. Sikkerheden på begge lokaliteter verificeret, og hændelses­gangen '
         'justeret.'),
        ('Dag 90',
         'Sektionen leverer uden at nogen skal spørge, hvem der har ansvaret; mine tal kan læses af andre, og '
         'entreprenørerne ved, hvad de bliver målt på. Mindst én arbejdsgang er forbedret og delt, så næste '
         'kontrakt starter bedre end min første.')])

    m.section('EN SEKTION BYGGES PÅ ET KORT')
    m.para('Når en sektion er ny, er den største risiko ikke, at folk arbejder for lidt — det er, at to mennesker '
           'arbejder på den samme opgave uden at vide det, eller at en opgave ingen ejer har. Derfor begynder jeg med '
           'kortet: opgave, kontrakt, lokation, ejer, rytme. Det tager et par uger at lave ordentligt, og derefter er '
           'det både styringsværktøj og introduktion for den næste, der skal ind i sektionen. Organisationen kommer '
           'bagefter — og bliver bedre, fordi den er bygget på virkeligheden.', after=80)

    m.section('KONTRAKTEN ER EN DRIFTSINSTRUKS')
    m.para('En udliciteret opgave er kun så god som den kontrakt, der beskriver den. Derfor skal en kontrakt sige, '
           'hvad der er med, hvad der ikke er, hvad der måles på, hvor hurtigt der skal reageres, hvordan der '
           'dokumenteres, og hvad der sker, når det ikke holder. Når de ting står der, bliver tilsynet en samtale om '
           'tal i stedet for en diskussion om fortolkning — og entreprenøren får en fair ramme at levere i. Jeg har '
           'været på begge sider, og jeg ved, at begge parter tjener på tydelighed.', after=80)

    m.section('ARBEJDSMILJØ ER EN LEDELSESOPGAVE')
    m.para('Sikkerhed bliver ikke bedre af at stå i en politik. Den bliver bedre, når lederen er på pladsen, spørger '
           'ind til, hvordan opgaven faktisk bliver løst, og reagerer, når svaret ikke er godt nok — også når det '
           'forsinker noget. I spildevandsdrift er der tunge løft, lukkede rum, kemikalier, trafik og arbejde i al '
           'slags vejr, og det skal være planlagt, før dagen begynder. Jeg vil have, at hændelser bliver meldt, '
           'fordi vi lærer af dem, og at både egne folk og entreprenører ved, at en farlig genvej ikke er en genvej.',
           after=80)

    m.section('TAL FRA DRIFTEN SLÅR MENINGER')
    m.para('HOFOR leverer drikkevand og håndterer spildevand for mere end en million mennesker i hovedstadsområdet '
           '— en opgave for forsyningen, hvor der ikke er noget at hente på at gætte. HOFOR siger selv, at beslutninger '
           'træffes på et oplyst grundlag, og at data og analyser er fundamentet. '
           'Det er også min erfaring: da jeg skulle nedbringe energiforbruget på Lynetten, startede det ikke med en '
           'holdning, men med målinger — hvor forsvandt energien hen, hvilke anlæg trak mest, og hvad gav den største '
           'effekt pr. krone. Resultatet blev over 40 %, og det holdt, fordi opfølgningen blev en fast rytme og ikke '
           'et projekt. Den samme tilgang vil jeg bruge på sektionens tid, økonomi og kontrakter.', after=80)

    m.section('TO TEAMS OG FLERE LOKATIONER')
    m.para('At lede to teams med forskellige fagligheder og ledere imellem mig kræver noget andet end at lede ti '
           'ens medarbejdere: det kræver en tydelig retning, som lederne kan oversætte til deres eget område, og tæt '
           'kontakt. Jeg holder en fast kadence på '
           'hver lokation, er til stede på Smedeholm som lokationsansvarlig og bruger Kløvermarken lige så '
           'bevidst — for forskellige steder har forskellige problemer, og de bliver ikke løst på et videomøde.',
           after=80)

    m.section('ENTREPRENØREN ER EN DEL AF ANLÆGGET')
    m.para('Når en stor del af driften er udliciteret, er entreprenøren ikke en ekstern part, men en del af '
           'anlægget — og hans sikkerhed og kvalitet er vores. Derfor skal entreprenører introduceres ordentligt, '
           'have de samme sikkerhedskrav som egne folk og møde samme tydelige opfølgning, og til gengæld få en fair '
           'kontrakt og en partner, der siger til i god tid.', after=80)

    m.section('FORANDRING KRÆVER FØLGESKAB')
    m.para('En ny sektion er en forandring for dem, der bliver en del af den, og for dem, der skal samarbejde med '
           'den. Følgeskab får man ikke ved at forklare en struktur, men ved at vise, hvad den løser: færre '
           'irriterende opgaver, klarere ansvar og en leder, der tager de svære samtaler selv. Jeg bruger tid på at '
           'lytte først — til driften, til lederne, til Indkøb og Analyse — og når jeg så beslutter noget, står jeg '
           'ved det og forklarer hvorfor. Det er også den måde, jeg bedst respekterer forskellige fagligheder på. Og '
           'når forandringen er gennemført, skal den kunne mærkes i hverdagen — i færre genopgaver, kortere '
           'ventetid og en drift, der kører, også den uge hvor ingen har tid.', after=80)

    return m.save(path, title='Motiveret CV — Sektionsleder, HOFOR Spildevand Kontrakt',
                  subject='Spildevandsdrift, kontraktstyring og sikker drift på flere lokationer',
                  keywords='sektionsleder, spildevand, kontraktstyring, udlicitering, arbejdsmiljø, økonomistyring, '
                           'aktivering, personaleledelse')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_HOFOR_SektionslederSpildevandKontrakt.docx')))
