# -*- coding: utf-8 -*-
"""VM Tarm a/s — arbejdende leder til bearbejdningsafdelingen.

Dansk leverance (opslaget er dansk): ansøgning side 1, CV side 2–3.
Policy: master/README.md — ekstrem sikkerhed, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Arbejdende leder · Produktion, maskiner og mennesker på gulvet'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('6. november 2026')
    m.meta('VM Tarm a/s · Bearbejdningsafdelingen · Arbejdende leder')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Arbejdende leder, bearbejdningsafdelingen, VM Tarm a/s', bold=True, color='1A1A1A')
    m.para('Til VM Tarm a/s · att. Anette Aarup Skyttegaard, Career', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('En tankvogn i rustfrit stål bliver ikke færdig, fordi planen var god. Den bliver færdig, fordi nogen '
           'står ved maskinen, da pladen skal bukkes, og fordi nogen dagen før har besluttet, hvad der skulle '
           'skæres først. Bearbejdningsafdelingen er der, hvor forsinkelsen opstår — og hvor den kan ses, længe '
           'før den rammer svejsningen. Det er den slags lederjob, jeg søger: ansvar for 10-12 mennesker og en '
           'maskinpark på omkring 15 maskiner, hvor man ikke kan lede fra et kontor, fordi svaret står på gulvet.',
           after=80)

    m.para('**Jeg ville lede afdelingen på fire faste ting.** Først **overblik skabes ved maskinerne, ikke i et '
           'regneark**: en fast morgenrunde kl. 7 med status på hver maskine — hvad kører, hvad venter på '
           'opstilling, hvem står hvor — så dagen bliver planlagt ud fra virkeligheden og ikke ud fra, hvad der '
           'blev aftalt i sidste uge. For det andet **prioritering skal være en aftalt regel, ikke en '
           'fornemmelse**: sammen med planlæggeren beslutter vi på forhånd, hvad der rykker forrest — en standset '
           'tank i svejsningen, en kunde med leveringsdato — og hvad der ikke gør, så beslutningen ikke afhænger '
           'af, hvem der råber højest den dag. For det tredje **vedligehold er kapacitet, ikke en regning**: en '
           'serviceplan pr. maskine, eksterne montører booket med dato og tidsvindue, og de sliddele der stopper '
           'en maskine — skæredyser, linser, saveblade, bukkeværktøj — på lager, fordi et stop i bearbejdningen '
           'ikke koster én maskine, men hele rækken bagved. For det fjerde **teknologi skal vælges på, hvad den '
           'fjerner**: messer og leverandørdemoer er kun værd noget, hvis vi bagefter kan sige, hvilken opstilling, '
           'hvilket spild eller hvilket manuelt løft der forsvinder — ellers er det en ny maskine oven på de gamle.',
           after=80)

    m.para('Ledelse tæt på produktionen har jeg prøvet i mange år. Siden 2023 har jeg drevet **ELOHVAC** med '
           'fuldt P&L — **fem elektrikere og tre lærlinge** — og jeg har selv stået i arbejdstøjet, når der skulle '
           'løses en opgave, for i en virksomhed i den størrelse er der ingen, der kommer og gør det for en. Før '
           'det var jeg **elektromekaniker og produktionsteamleder på ARJ Engineering** med **12 mekanikere og '
           'teknikere** i et maskinværksted: klargøring, reparation og fejlfinding på industrielt udstyr, '
           'vagtplanlægning, oplæring og mål for den enkelte. Det er den baggrund, jeg kommer med til '
           'bearbejdningen: jeg kan læse en tegning, jeg ved hvad en opstilling tager, og jeg kan tale med en '
           'smed om, hvorfor emnet ikke blev som forventet.', after=80)

    m.para('Planlægning med korte horisonter og mange afhængigheder har jeg prøvet i større skala. I **Ventek-Air '
           'ledede jeg 14 medarbejdere og 11 samtidige projekter** med dagligt tavlemøde, kapacitets- og '
           'flaskehalsanalyse og omprioritering samme dag, når en maskine eller et menneske faldt væk. På **Novo '
           'Nordisk** styrede jeg **37 parallelle anlægsprojekter** med 25 specialister og var med til at '
           'modtage nyt udstyr via **FAT/SAT** — den øvelse, hvor man på forhånd beslutter, hvad en maskine skal '
           'kunne, og derefter måler, om den gør det. Og fra **Lynetten under Biofos** kender jeg '
           'vedligeholdelsesdelen: koordinering af mekanikere og **eksterne montører** i et døgnmiljø, hvor et '
           'stop ikke var en ærgerlig dag, men en driftsforstyrrelse, der blev målt.', after=80)

    m.para('Femten maskiner er også femten sæt opstillinger og et materialeregnskab. Plasma, laser og rørlaser, '
           'save, kantbukkere, CNC-maskiner til at dreje og fræse og en slibemaskine: hver har de deres opstillingstid og deres egen '
           'flaskehals, og rustfrit stål koster penge at skære forkert — en restplade, der bliver væk, er spild, '
           'ingen ser i regnskabet. Derfor ville jeg tidligt have styr på, hvordan programmerne lægges, hvordan '
           'restplader registreres, og hvornår det kan betale sig at bytte rækkefølgen for at spare en opstilling. '
           'Det er ikke et IT-projekt; det er en samtale med den, der står ved maskinen, og et tal, der bliver fulgt '
           'op hver uge.', after=80)

    m.para('Det, der især tiltrækker mig ved VM Tarm, er, at afdelingen ikke er en isoleret ø. Der er 250-300 '
           'kolleger, egen konstruktion, svejsning, montage og service, og bearbejdningen leverer ind til det '
           'hele: pladen, der bliver skåret og bukket forkert, kan ikke rettes i svejsningen. Det er en kort vej '
           'fra tanke til handling i en privatejet virksomhed, og det passer til den måde, jeg arbejder på: '
           'beslutte, prøve, måle, justere — ikke mødes om det først.', after=80)

    m.para('Praktisk: jeg har **kørekort B og egen bil**, og jeg bor i Måløv i dag. Tarm er ikke et pendlerjob for '
           'en leder, der skal stå ved maskinerne kl. 7, så jeg er indstillet på at **flytte til Vestjylland** for '
           'den rigtige stilling — og jeg kan starte efter aftale. Jeg vil gerne høre, hvordan I i dag lægger '
           'rækkefølgen mellem bearbejdning, svejsning og montage, og hvordan vedligeholdelsen bliver planlagt ind '
           'i den — det er der, jeg ville begynde.', after=70)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Arbejdende leder med 20+ års erfaring fra produktion, værksted og teknisk drift — elautoriseret '
           'maskinmester (LV/MV/HV) med B.Tech i teknologiledelse og maskinteknik og en håndværksmæssig baggrund '
           'som elektromekaniker. Har ledet 12 mekanikere i et maskinværksted, 14 medarbejdere med 11 samtidige '
           'projekter og i dag egen virksomhed med fuldt P&L og fem elektrikere og tre lærlinge. Arbejder selv med '
           'i opgaverne, kan læse tegninger og maskinkrav, og har koordineret vedligehold og eksterne montører i '
           '24/7-drift. Bygger egne værktøjer i Python og Claude med over 40 % dokumenteret produktivitetsløft.', after=80)

    m.section('DRIFT, MASKINER OG MENNESKER')
    for label, body in [
        ('Daglig drift og planlægning',
         'Dagsplan lagt ved maskinerne hver morgen ud fra ordrer, opstillingstider og bemanding; tavlemøde, '
         'kapacitets- og flaskehalsanalyse og omprioritering samme dag, når en maskine eller et menneske faldt væk.'),
        ('Ledelse på gulvet',
         '12 mekanikere i et maskinværksted, 14 medarbejdere i Ventek-Air, 5 elektrikere og 3 lærlinge i egen '
         'virksomhed — ledelse i arbejdstøjet, med oplæring og de svære samtaler taget direkte.'),
        ('Vedligehold og montører',
         'Vedligeholdsplan pr. maskine, kritiske sliddele på lager og eksterne montører booket med dato og '
         'tidsvindue; 5S og standard work på værksted og lager, og stop målt og fulgt op i stedet for forklaret.'),
        ('Kvalitet og sikkerhed',
         'Arbejdsmiljø, trivsel og sikkerhed som en del af den daglige runde: APV, instrukser, værnemidler og '
         'afvigelser taget ved maskinen; fejl fundet ved kilden, før emnet går videre til svejsning og montage.'),
        ('Teknologi og investeringer',
         'Kravsspecifikation og modtagelse af nyt udstyr via FAT/SAT på 37 anlægsprojekter; vurdering af, hvad en '
         'ny maskine fjerner af opstilling, spild og manuelt arbejde — og hvad den koster i drift og service.'),
        ('Økonomi og resultater',
         'Fuldt P&L i egen virksomhed: kalkulation, timeforbrug, indkøb og dækning fulgt månedligt; forbedringer '
         'målt før og efter, fx over 40 % produktivitetsløft gennem egne værktøjer.')]:
        m.bullet(label, body, after=25)

    m.models_table('MASKINER, METODER OG VÆRKTØJER', ('Opgave', 'Dokumenteret brug'), [
        ('Maskinpark og vedligehold',
         'Vedligeholds- og serviceplan pr. enhed, reservedelsbehov ud fra kritikalitet, leverandør- og '
         'montørkontakt samt dokumentation for udført service.'),
        ('Planlægning og kapacitet',
         'Dags- og ugeskema pr. maskine og medarbejder, opstillingstider, kapacitets- og flaskehalsanalyse samt '
         'prioriteringsregler aftalt med planlæggeren.'),
        ('Produktionsstyring og 5S',
         'Tavlemøde, standard work, 5S på værksted og lager, PDCA på gentagne fejl og opfølgning på stop og '
         'kassation.'),
        ('Data og værktøjer',
         'Excel og Power Query, Python og Claude til tjeklister, opfølgning og dashboards; SAP til ordrer, '
         'økonomi og aktiver.'),
        ('Ledelse og udvikling',
         'MUS og 1:1, oplæring af nye, kompetence og multi-skilning mellem maskiner, sygefraværsopfølgning '
         'og ansvar givet videre med mandat.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · el-tekniske service- og entrepriseydelser',
         [('Leder og udfører selv',
           'Salg, tilbud, kalkulation, indkøb, fakturering og betalingsopfølgning; daglig drift med kunder, '
           'medarbejdere og leverandører, og selv med i opgaverne når der skal leveres; egne værktøjer i Python '
           'og Claude har givet over 40 % produktivitetsløft.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Udstyr, krav og modtagelse',
           'Kravsspecifikation og FAT/SAT ved modtagelse af nyt produktionsudstyr; fremdrift, økonomi og risiko '
           'rapporteret månedligt til ledelse og bygherre; nul kritiske fund ved aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter · 2–10 mio. kr. pr. opgave',
         [('Korte horisonter og mange afhængigheder',
           'Dagligt tavlemøde, kapacitets- og flaskehalsanalyse og omprioritering samme dag, når en maskine eller '
           'et menneske faldt væk; standardiserede arbejdsgange og leverancer styret til dato.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Lynetten under Biofos · København · aug. 2017–jan. 2022',
         'Kritisk procesanlæg i 24/7-drift · pumper, blæsere, ventilation, transformere, koblingsanlæg og SCADA',
         [('Vedligehold, mekanikere og eksterne montører',
           'Vedligehold, reparation og reservedele koordineret med mekanikere og eksterne leverandører i døgndrift; '
           '5S og standard work på værksted og lager; energiledelse med over 40 % lavere forbrug dokumenteret.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · industrielt udstyr',
         [('Værksted, klargøring og fejlfinding',
           'Klargøring, reparation og fejlfinding på industrielt udstyr med drejning, fräsning og montage; '
           'vagtplanlægning, oplæring og opfølgning på mål for 12 teknikere.')]),
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
    m.para('Dansk: modersmål · Engelsk: professionelt, mundtligt og skriftligt · Persisk: modersmål · Kørekort B og '
           'egen bil · Indstillet på at flytte til Vestjylland · Kan starte efter aftale · SAP og Excel dagligt, '
           'Python til data og systemer · Referencer på forespørgsel.', after=70)

    m.models_table('DET DE EFTERSPØRGER — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Ledelseserfaring fra en produktionsvirksomhed',
         '12 mekanikere og teknikere i et maskinværksted, 14 medarbejdere i Ventek-Air og 5 elektrikere plus 3 '
         'lærlinge i egen virksomhed — rekruttering, oplæring og daglig opfølgning i alle tre.'),
        ('Teknisk forståelse, produktionsmaskiner og håndværksmæssig baggrund',
         'Uddannet elektromekaniker og elautoriseret maskinmester (LV/MV/HV); B.Tech i teknologiledelse og '
         'maskinteknik; arbejdet med drejning, fräsning, montage og fejlfinding på industrielt udstyr.'),
        ('Daglig ledelse og koordinering af 10-12 medarbejdere',
         '12 teknikere i ARJ, 14 medarbejdere på tværs af 11 projekter i Ventek-Air og 8 medarbejdere i egen '
         'virksomhed — samme volumen, samme nærhed til opgaven.'),
        ('Planlægning og prioritering sammen med planlæggeren',
         'Kapacitets- og flaskehalsanalyse med dagligt tavlemøde; prioriteringsregler aftalt på forhånd i stedet '
         'for improviseret, når to opgaver kræver samme maskine.'),
        ('Optimering af produktionen',
         'Standard work, 5S og PDCA med målbare før- og eftertal; automatisering af manuelle arbejdsgange med over '
         '40 % produktivitetsløft dokumenteret i egen virksomhed; flaskehalse fundet ved at måle, hvor emnerne '
         'faktisk ventede, ikke hvor der blev klaget.'),
        ('Aktiv deltagelse i arbejdet på gulvet',
         'Ejer af en håndværksvirksomhed siden 2023, hvor jeg selv står i opgaverne; før det teamleder i et '
         'maskinværksted med reparation og klargøring som dagligt arbejde, ikke som besøg. Jeg tager de svære '
         'opgaver selv og lader rutinen ligge hos dem, der skal blive bedre til den.'),
        ('Maskinvedligeholdelse og koordinering med eksterne montører',
         'Serviceplan pr. maskine, kritiske sliddele på lager og leverandører og montører booket med dato og '
         'tidsvindue i 24/7-drift, hvor et stop blev målt.'),
        ('Teknologisk udvikling og messer',
         'Kravsspecifikation og FAT/SAT ved modtagelse af nyt produktionsudstyr på 37 projekter; teknologivalg '
         'vurderet på, hvad der fjernes af opstilling, spild og manuelt arbejde.'),
        ('Dansk i tale og skrift samt mundtligt engelsk',
         'Dansk er arbejdssproget i tavlemøder, instrukser og dokumentation; engelsk brugt dagligt i møder med '
         'leverandører, rådgivere og udenlandske kolleger gennem 20 år.'),
        ('Empatisk og tydelig kommunikation, også i en omskiftelig hverdag',
         'MUS, 1:1 og daglige tavlemøder på dansk og engelsk; beslutninger taget tæt på opgaven med begrundelse, '
         'så næste skift ikke skal gætte, hvad der blev aftalt.')])
    m.page_break()

    m.models_table('DE FØRSTE 90 DAGE — AFDELINGEN, MASKINERNE OG MENNESKENE',
                   ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'Gå runder ved alle ca. 15 maskiner sammen med den nuværende ledelse og planlæggeren; lær navnene på '
         'medarbejderne og deres maskiner; se flowet fra bearbejdning til svejsning og montage — og skriv ned, '
         'hvad der i dag kun findes i hovedet på nogen.'),
        ('Dag 30',
         'En fast morgenrunde kl. 7 og et ugentligt tavlemøde indført; status pr. maskine, stop og kassation '
         'synlig; aftalte prioriteringsregler med planlæggeren på plads for, hvad der rykker forrest.'),
        ('Dag 60',
         'Vedligeholdsplan pr. maskine med datoer for eksterne montører og liste over kritiske sliddele på lager; '
         'kompetencematrix for de 10-12 medarbejdere, så flere kan køre flere maskiner; første forbedring målt før '
         'og efter.'),
        ('Dag 90',
         'Afdelingen leverer til dato med kendt kapacitet og kendt oppetid; en kort månedlig rapport med stop, '
         'spild og leveringsevne; og en begrundet liste over, hvilke maskiner eller hvilken automatisering der '
         'næste år kan fjerne mest manuelt arbejde.')])

    m.section('BEARBEJDNINGEN LEVERER TIL SVEJSNINGEN, IKKE TIL LAGERET')
    m.para('Det er den vigtigste sætning i den her afdeling. En plade, der bliver skåret tyve minutter for sent, '
           'holder ikke tyve minutter op — den holder den tank op, der ventede på den, og den plads i hallen, som '
           'en anden tank skulle bruge. Derfor måler jeg afdelingen på, hvad der kommer videre i tide, ikke på hvor '
           'travlt der ser ud. Det kræver, at man kender flowet nedstrøms, og det kræver, at man hellere vil '
           'prioritere to opgaver rigtigt end at sige ja til ti.', after=80)

    m.section('MORGENEN STARTER KL. 7 VED MASKINERNE')
    m.para('En arbejdende leder har ikke et mødeværelse som sit vigtigste værktøj. Han har sin egen runde: hvilke '
           'maskiner kører, hvilke står stille og hvorfor, hvem er syg, hvad mangler der materiale til, og hvad '
           'skal være færdigt i dag for at svejsningen kan køre i morgen. Den runde tager tyve minutter og sparer '
           'dage, fordi den fanger problemet, før det bliver en plan, nogen skal lave om.', after=80)

    m.section('KORTE HORISONTER KRÆVER EN REGEL FOR, HVAD DER RYKKER FORREST')
    m.para('Når horisonten er kort, er planen ikke en plan — den er en aftale om rækkefølge, som bliver lavet om '
           'hver dag. Så reglerne skal ligge fast, før dagen begynder: hvad slår hvad, når en standset tank i '
           'svejsningen og en kundeordre kræver samme maskine. Beslutningen skal kunne tages på gulvet af den, '
           'der står med opgaven, og den skal være den samme, uanset hvem der spørger.', after=80)

    m.section('VEDLIGEHOLD ER KAPACITET, IKKE EN REGNING')
    m.para('En laser, der står stille i to dage, fordi en linse ikke var på hylden, er ikke et '
           'vedligeholdelsesproblem. Det er en planlægningsfejl. Derfor en serviceplan pr. maskine, en liste over de '
           'sliddele der reelt stopper produktionen, og et lager der er dimensioneret efter det — ikke efter hvad der '
           'plejer at blive bestilt. Og et stop skal registreres, fordi det er den eneste måde at se, om planen '
           'virker.', after=80)

    m.section('MONTØREN SKAL HAVE EN TID, IKKE ET OPKALD')
    m.para('Eksterne montører kommer ikke, fordi man ringer. De kommer, fordi der står en dato, et tidsvindue og en '
           'maskine, der er gjort klar, og fordi nogen har aftalt, hvad opgaven er, før de kører. Det arbejde har '
           'jeg gjort i 24/7-drift, hvor et stop blev målt i timer, og hvor reservedele og leverandører var en del '
           'af driftsplanen og ikke noget, der blev opdaget.', after=80)

    m.section('TEKNOLOGI SKAL FJERNE ET ARBEJDSSKRIDT, IKKE TILFØJE ET SYSTEM')
    m.para('Messer er gode til at se, hvad der findes, men en ny maskine skal svare på ét spørgsmål: hvilket '
           'skridt forsvinder? Er det opstillingen, en flytning, en efterbearbejdning eller en fejl, der i dag '
           'bliver rettet i hånden? Kan vi ikke svare, bliver investeringen et nyt sted at vedligeholde. Kan vi, '
           'skal den have en plads i planen, en oplært mand og en dato.', after=80)

    m.section('MAN KAN IKKE BÅDE LEDE OG ARBEJDE, HVIS MAN IKKE GIVER SLIP')
    m.para('Faren ved at være arbejdende leder er ikke, at man arbejder for lidt — det er, at man bliver den, der '
           'løser de opgaver, man selv er god til, og først ser afdelingen, når nogen spørger. Derfor en ansvarlig '
           'pr. maskinegruppe, en fast runde og et fast tidspunkt, hvor jeg ser på ugen i stedet for på en maskine. '
           'Jeg tager de svære opgaver, og lader rutinen ligge hos dem, der skal blive bedre til den.', after=80)

    m.section('JEG HAR STÅET PÅ GULVET, FØR JEG FIK ET KONTOR')
    m.para('Jeg har været elektromekaniker med værktøj i hånden, teamleder for 12 mekanikere, driftsleder i '
           'døgndrift og ejer af en virksomhed, hvor der ikke var nogen til at tage opgaven, hvis ikke jeg gjorde. '
           'Det betyder ikke, at jeg skal køre laseren. Det betyder, at jeg ved, hvad jeg beder folk om, at jeg '
           'kan mærke, hvornår en opgave er urealistisk, og at jeg ikke beder nogen om noget, jeg ikke selv ville '
           'tage fat i.', after=80)

    return m.save(path, title='Arbejdende leder, bearbejdningsafdelingen — VM Tarm a/s',
                  subject='Daglig ledelse af 10-12 medarbejdere og en maskinpark på ca. 15 maskiner',
                  keywords='arbejdende leder, produktionsleder, bearbejdning, planlægning, prioritering, '
                           'maskinpark, CNC, laser, kantbukker, vedligehold, montører, tavlemøde, 5S, '
                           'produktionsoptimering, dansk, engelsk')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_VM_Tarm_ArbejdendeLeder.docx')))
