# -*- coding: utf-8 -*-
"""Køge Kommune — Chef for Ejendomme, Teknik- og Miljøforvaltningen.

Form (master/FORMKATALOG.md): åbning **H** (dagsforløbet: fire klokkeslæt som bevis),
struktur **Budgetlinjen** (hver post i en beslutning og hvem der ejer den), register
**Borgerens** (hverdag, tillid, kerneopgave). Kulturfil:
jd/KoegeKommune_ChefEjendomme_kultur.txt. Ansøgningsfrist 2.12.2026, tiltrædelse 1.2.2027.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Chef for Ejendomme · drift, byggeri og ledelse gennem ledere'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('8. november 2026')
    m.meta('Køge Kommune · Teknik- og Miljøforvaltningen · Chef for Ejendomme · Torvet 1')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Chef for Ejendomme', bold=True, color='1A1A1A')
    m.para('Til teknik- og miljødirektør Kristian Nabe-Nielsen', after=70)

    # ---------------------------------------------------------------- side 1
    m.para('**Kl. 07.15** ligger **kapacitetsberegninger** for **dagtilbud**, **skoler** og '
           'plejeboliger på bordet: 63.328 køgeboere i dag, 67.695 i 2037 — og hver ny kvadratmeter '
           'bliver til et byggeri, en **serviceaftale** og en regning, nogen betaler i tredive år. '
           '**Kl. 09.00** sidder jeg i **Teknik- og Ejendomsudvalget** og skal forklare, hvorfor det '
           'ene projekt flytter sig og det andet ikke. **Kl. 12.30** står jeg på byggepladsen for at se, '
           'om det, der blev besluttet i februar, stadig er rigtigt i november. **Kl. 15.45** har en af '
           'de **ni ledere** en sag, der ikke kan vente — og mit svar skal gøre ham i stand til at tage '
           'den næste selv.', after=80)

    m.para('**Stillingen handler ikke om, at jeg kan mest om bygninger. Den handler om, at ni ledere '
           'skal kunne mere, fordi jeg er der.** Køge er **en kommune i vækst**, og **Kommuneplan '
           '2025-37** lægger rammerne for de næste tolv år. Et **dagtilbud**, der åbner for sent, '
           'koster en familie en hverdag. En **skole** uden plads koster en klasse. **Plejecentre** uden '
           '**tilgængelighed** koster en beboer et bad. Det er de '
           '**kerneopgaver**, en chef for Ejendomme sjældent ser — og altid betaler for.', after=70)

    m.para('**Jeg ville lede området efter fem budgetlinjer — og hver linje har en ejer blandt de ni '
           'ledere.**', after=60)

    m.para('**1. Areal — den linje, ingen ser, men alle betaler.** **Arealoptimering** er ikke et '
           'spareprojekt; det er spørgsmålet om, hvilke kvadratmeter af den samlede '
           '**ejendomsportefølje** kommunen skal eje, leje og afstå. Jeg har selv siddet med lager, værksted og bemanding på 14 medarbejdere og 11 '
           'samtidige projekter og ved, at tom kapacitet koster hver måned, den står tom.', after=60)

    m.para('**2. Byggeri — den linje, der låses i briefen.** I en **bygherrefunktion** bliver 80 % af '
           'driftsudgiften besluttet, før første spadestik. Jeg har leveret og modtaget **37 '
           'kapitalprojekter** med FAT/SAT og **nul kritiske fund** og ved, hvad der skal stå i '
           'kravspecifikationen, for at det også holder i år ti.', after=60)

    m.para('**3. Drift og vedligeholdelse — den linje, der vokser, når de to første var forkerte.** '
           'Fem år i 24/7-drift på et kritisk anlæg har lært mig, at **vedligeholdelse** ikke er en '
           'omkostning, man skærer i; det er den udgift, man flytter. Jeg har styret det efter '
           'kritikalitet, med **over 40 % lavere energiforbrug** som dokumenteret resultat.', after=60)

    m.para('**4. Service og rengøring — den linje, borgeren møder først.** Et rent lokale og et '
           'fungerende indeklima er den del af kommunen, borgeren faktisk rører ved. Jeg har haft '
           '**serviceaftaler**, leverandører og eget værksted under mig og ved, at kvaliteten her '
           'afgøres af **kontrakter**, der kan læses af den, der gør arbejdet.', after=60)

    m.para('**5. Energi — den linje, der betaler sig selv tilbage.** **Energiprojekter** er den '
           'sjældne post, hvor politikernes spørgsmål og driftschefens svar peger samme vej. Jeg har '
           'indreguleret pumper og ventilation og drevet **energiledelse** på et 24/7-anlæg med over '
           '40 % lavere forbrug — og kan gøre rede for, hvad der blev målt, og hvad der blev sparet.',
           after=70)

    m.para('**Fremtidens Rådhus er ikke et byggeri; det er en forandring.** Én indgang for borgeren '
           'betyder færre skranker, andre arbejdsgange og ledere, der skal flytte medarbejdere, de '
           'ikke selv har valgt. Jeg har prøvet den slags forandring fra den svære side: 5S og '
           'standard work indført på et værksted, hvor det ændrede, hvordan folk arbejdede — og jeg '
           'ved, at det kun holder, når medarbejderne har været med til at definere den.', after=80)

    m.para('**Ledelseskraft er ikke et program. Det er ni ledere i en ledergruppe, der ved, hvad de '
           'ejer.** At **lede gennem ledere** er ikke nyt for mig: formænd og værkstedsledere, som '
           'selv havde folk under sig, har refereret til mig, og jeg har ledet 12–14 faglærte '
           'direkte. Det er mindre end ni ledere i en politisk styret organisation, og det skal stå '
           'klart. Det, '
           'jeg kan, er at skabe **fælles retning** og **gensidig ansvarlighed** ved at give mandat '
           'og forventning i samme sætning, at holde **ro og overblik**, når tre sager haster lige '
           'meget, og at have **mod til at prioritere**, når prioriteringen er upopulær. Et chefjob '
           'er et tillidsmandat, og **tillid** gives kun til en, der har svaret, når der blev spurgt.', after=70)

    m.para('**Politik, økonomi og helhed.** Jeg har været **driftsleder**, projektleder og ejer og har '
           'siddet på begge sider af bordet: som '
           'virksomhedsejer med fuldt P&L og som den, der skulle levere til en bygherre med '
           '**myndigheder**, **rådgivere** og **håndværkere** omkring sig. Jeg ved, at en sag til '
           '**Økonomiudvalget** — eller til et hvilket som helst andet **udvalg** — skal kunne læses på to '
           'sider, og at et svar, der ikke kan '
           'kvalitetssikres, bliver et problem i næste **udvalgsmøde**. **Politiske ambitioner, '
           'organisatoriske behov og kommunens investeringer** skal passe sammen i samme dokument — '
           'det er den håndværksmæssige del af chefjobbet, og synlige **resultater** er den eneste '
           'valuta, der tæller i en politisk hverdag.', after=70)

    m.para('Jeg bor i Måløv, 45 minutter fra Torvet 1, har kørekort og bil og kan være i Køge hver '
           'dag. Jeg kan tiltræde 1. februar 2027 og vil gerne høre, hvordan I i dag vejer '
           '**vedligeholdelse** mod nybyg, når budgettet skal lægges — det er der, jeg ville begynde.',
           after=70)

    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Leder med 20+ års erfaring fra tekniske anlæg, byggeri og drift — **elautoriseret '
           'maskinmester (LV/MV/HV)** med B.Tech i teknologiledelse og maskinteknik. Har ledet **12–14 '
           'medarbejdere og ledere** i to virksomheder, koordineret **25 specialister** på **37 '
           'kapitalprojekter** med nul kritiske fund, drevet et kritisk anlæg i **24/7-drift** med '
           '**over 40 % lavere energiforbrug** og driver siden 2023 egen virksomhed med **5 '
           'elektrikere, 3 lærlinge, fuldt P&L og elautorisationen**. Arbejder med **økonomistyring**, '
           '**kontrakter** og **serviceaftaler** som en fast del af lederrollen.', after=80)

    m.section('BORGERENS HVERDAG — DRIFT, BYGGERI OG SERVICE')
    for label, body in [
        ('Drift og vedligeholdelse i døgndrift',
         'Kritisk anlæg i 24/7-drift: vedligeholdsplaner, reservedele, eksterne montører og '
         'prioritering efter kritikalitet; 5S og standard work på værksted og lager.'),
        ('Byggeri, bygherre og aflevering',
         '37 kapitalprojekter modtaget og afleveret med FAT/SAT og nul kritiske fund; '
         'kravspecifikation, økonomi og fremdrift rapporteret månedligt til ledelse og bygherre.'),
        ('Service, leverandører og kontrakter',
         'Serviceaftaler, priser og betalingsvilkår i egen virksomhed; leverandører og håndværkere '
         'fulgt på tid, pris og kvalitet — og leverancer afvist, når de ikke holdt kontrakten.'),
        ('Energi og indeklima',
         'Energiledelse med over 40 % lavere forbrug på et 24/7-anlæg; indregulering af pumper og '
         'ventilation, måling og opfølgning — indeklima og driftsøkonomi vejet sammen.'),
        ('Økonomi og prioritering',
         'Fuldt P&L siden 2023: budget, dækningsgrad, timeregistrering og betalingsopfølgning for 8 '
         'medarbejdere; projektbudgetter på 2–10 mio. kr. styret i 37 projekter.'),
        ('Ledelse af ledere og faglærte',
         'Formænd og værkstedsledere med egne folk samt 12–14 faglærte direkte; MUS, kompetenceplaner '
         'og mandat med forventning i samme sætning.')]:
        m.bullet(label, body, after=25)

    m.models_table('ØKONOMI, STYRING OG PRIORITERING', ('Område', 'Dokumenteret brug'), [
        ('Budget og opfølgning',
         'Fuldt P&L og lønbudget siden 2023; 37 projektbudgetter på 2-10 mio. kr. med månedlig '
         'opfølgning på fremdrift, økonomi og risiko.'),
        ('Økonomistyring og prioritering',
         'Kritikalitetsmodel i døgndrift: udskudt vedligeholdelse gjort op i kroner og risiko hver '
         'måned; investeringer valgt, hvor de blev tjent ind — over 40 % lavere energiforbrug.'),
        ('Kontrakter og indkøb',
         'Serviceaftaler, priser og betalingsvilkår forhandlet og fulgt; leverandører og håndværkere '
         'målt på tid, pris og kvalitet — og afvist, når kontrakten ikke blev holdt.'),
        ('Beslutningsgrundlag',
         'Én til to sider til ledelse og bygherre: sag, alternativer, økonomi, risiko og anbefaling; '
         'referater med navn og dato, så næste møde starter samme sted.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · elautorisation · service- og entrepriseydelser',
         [('Forretning, kontrakter og drift',
           'Budget, prissætning, **serviceaftaler** og betalingsopfølgning; kvalitet og '
           'arbejdsmiljø i leverancen; kunder, **leverandører** og **håndværkere** i daglig '
           'koordinering.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · GMP/FDA/EMA',
         [('Projekter, interessenter og aflevering',
           'Kravspecifikation, FAT/SAT og aflevering af elektriske anlæg og styringer; '
           '**myndigheder**, **rådgivere** og entreprenører koordineret; nul kritiske fund ved '
           'aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere og formænd · 11 samtidige anlægsprojekter',
         [('Kapacitet, fremdrift og ledelse gennem ledere',
           'Dagligt tavlemøde, kapacitetsanalyse og omprioritering samme dag; arbejdet fordelt '
           'gennem formændene, ikke over deres hoveder.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Lynetten under Biofos · København · aug. 2017–jan. 2022',
         'Kritisk anlæg i 24/7-drift · SRO · ventilation, pumper, transformere, koblingsanlæg',
         [('Drift, vedligeholdelse og energi',
           'Vedligeholdsplaner og kritikalitet i døgndrift; arbejdsmiljø og sikkerhedsrunder; '
           'energiledelse med over 40 % lavere forbrug; 5S og standard work indført.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 teknikere og værkstedsledere · maskinværksted · industrielt udstyr',
         [('Teknisk service og ledelse',
           'Fejlfinding og reparation på industrielt udstyr; vagtplanlægning, oplæring og opfølgning '
           'på mål for 12 teknikere.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=25)

    m.section('UDDANNELSE OG AUTORISATION')
    m.edu('B.Tech, teknologiledelse og maskinteknik',
          'Maskinmesterskolen København · 2017–2022 · gennemsnit 7,6/12')
    m.edu('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('Køle- og ventilationsteknik · AMU', 'Mercantec 2021 · STCW, Søfartsstyrelsen 2021')
    m.edu('El- og maskinteknisk konstruktion, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6')

    m.section('SPROG, PRAKTIK OG REFERENCER')
    m.para('Dansk: modersmål · Engelsk: professionelt, også teknisk · Persisk: modersmål · '
           '**Kørekort B og egen bil** · Måløv, 45 minutter fra Torvet 1 · Kan tiltræde 1. februar '
           '2027 · Referencer på forespørgsel.', after=70)

    m.models_table('OPSLAGETS KRAV — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Solid ledelseserfaring',
         'Fem år som drifts- og vedligeholdelsesleder i 24/7-drift, projekt- og værkstedsleder for '
         '14 medarbejdere i 2022 og ejer af egen virksomhed med 8 ansatte siden 2023 — ledelse i '
         '20+ år.'),
        ('Erfaring med at lede gennem andre ledere',
         'I 2022 havde jeg 14 medarbejdere og formænd i Ventek-Air, og i ARJ refererede 12 teknikere '
         'og værkstedsledere til mig; arbejdet blev fordelt gennem dem med mandat og forventning, '
         'ikke over deres hoveder.'),
        ('Strategisk udsyn og kan omsætte beslutninger til organisatorisk handling',
         '37 kapitalprojekter omsat fra krav til aflevering med nul kritiske fund; 5S og standard '
         'work indført på værksted og lager, så beslutningen blev en arbejdsgang og ikke et oplæg.'),
        ('Stærk forståelse for økonomi, styring og prioritering af ressourcer',
         'Fuldt P&L i egen virksomhed siden 2023 med budget, dækningsgrad og betalingsopfølgning; '
         'projektbudgetter på 2–10 mio. kr. styret i 37 projekter med månedlig rapportering.'),
        ('Kan håndtere større projekter og komplekse processer med mange interessenter',
         '37 parallelle kapitalprojekter med 25 specialister, bygherre, myndigheder og entreprenører; '
         '11 samtidige anlægsprojekter i 2022; nul kritiske fund ved aflevering.'),
        ('Organisatorisk forståelse og ansvar for kommunens samlede kerneopgaver',
         '5 år med driftsansvar i 24/7 på et kritisk forsyningsanlæg, hvor et stop blev bemærket i hele '
         'byen; 37 kapitalprojekter under GMP/FDA/EMA og dansk arbejdsmiljølovgivning med '
         'dokumenteret efterlevelse.'),
        ('Kommunikerer klart og troværdigt med politikere, ledere, medarbejdere og samarbejdspartnere',
         'Dansk modersmål og engelsk professionelt; 20+ år med korte skriftlige oplæg til ledelse og '
         'bygherre, beslutningsreferater med navn og dato og mundtlig fremlæggelse for ikke-tekniske '
         'modtagere.'),
        ('Kan træffe beslutninger og fastholde fokus, når forskellige interesser er i spil',
         'Leverancer afvist i 11 samtidige projekter, når de ikke holdt kontrakten; prioritering efter '
         'kritikalitet i 5 års døgndrift, hvor opgaverne haster lige meget, og kun én kan vindes tid '
         'på.'),
        ('Mod og gennemslagskraft til at udfordre eksisterende praksis',
         '5S og standard work indført, hvor arbejdet før lå i hovedet på den enkelte; manuelle '
         'arbejdsgange erstattet af egne værktøjer med over 40 % færre timer til følge.'),
        ('Relevant faglig ballast og ledelsesmæssig efteruddannelse',
         'Elautoriseret maskinmester (LV/MV/HV) 2023; B.Tech i teknologiledelse og maskinteknik '
         '2017-2022 med 7,6/12; køle- og ventilationsteknisk AMU 2021; el- og maskinteknisk '
         'konstruktion 2000-2003, EQF 6.'),
        ('Planlægning og udvikling af kommunens ejendomme',
         '37 kapitalprojekter fra behov til aflevering og 11 samtidige anlægsprojekter ledet i 2022 — '
         'behovsafdækning, krav, fremdrift, økonomi og aflevering i samme model.'),
        ('Ejendomsportefølje og arealoptimering',
         'Lager, værksted og kapacitet styret mod ordreindgang i egen virksomhed og i Ventek-Air; '
         'tom kapacitet og udskudt vedligeholdelse gjort op i kroner hver måned i 11 projekter.'),
        ('Kommunalt byggeri og bygherrefunktion',
         'Bygherre- og modtagerside i 37 kapitalprojekter: kravspecifikation, FAT/SAT, '
         'afleveringsgennemgang og nul kritiske fund — og entreprenørside i egne sager siden 2023.'),
        ('Byggeteknisk rådgivning',
         'Byggetekniske vurderinger af el, ventilation, VVS og styring i 37 projekter og i egen '
         'virksomhed; rådgivere udfordret på løsninger, der ikke kunne driftes, og **tilsyn** med, at '
         'det leverede holdt det skrevne.'),
        ('Drift og vedligeholdelse af kommunens bygninger',
         'Fem år med vedligeholdsansvar i 24/7-drift: planer, reservedele, eksterne montører og '
         'kritikalitet; arbejdsmiljø og sikkerhedsrunder fulgt til dørs med over 40 % lavere '
         'energiforbrug.'),
        ('Service- og rengøringsopgaver',
         'Serviceaftaler, priser og kvalitetskrav skrevet og fulgt i egen virksomhed; leverandører '
         'og håndværkere styret på tid, pris og kvalitet i 8 medarbejderes daglige arbejde.'),
        ('Direkte ledelsesansvar for ni ledere og videreudvikling af ledergruppen',
         'Formænd og værkstedsledere med egne folk samt 12-14 faglærte direkte; MUS og '
         'kompetenceplaner med et konkret næste skridt pr. person — grundlaget for at lede ni ledere '
         'er det samme, blot større.'),
        ('Politisk betjening af Teknik- og Ejendomsudvalget og Økonomiudvalget',
         'Beslutningsoplæg med sag, alternativer, økonomi, risiko og anbefaling på to sider, i 20+ år '
         'til ledelse og bygherre; vant til at fremlægge for modtagere uden teknisk forudsætning.'),
        ('Robust økonomistyring af en betydelig driftsøkonomi',
         'Fuldt P&L og lønbudget for 8 medarbejdere siden 2023; projektbudgetter på 2-10 mio. kr. pr. '
         'projekt i 37 projekter med månedlig opfølgning på fremdrift, økonomi og risiko.'),
        ('Balance mellem drift, vedligeholdelse, udvikling og investeringer',
         'Prioriteringsmodel efter kritikalitet i døgndrift, hvor udskudt vedligeholdelse blev gjort '
         'op med navn og udgift; 40 % lavere energiforbrug som følge af investeringer, der blev '
         'tjent ind.'),
        ('Styrke samarbejdet med kommunens øvrige forvaltninger',
         'Grænseflader til produktion, kvalitet, vedligehold og eksterne parter i 37 projekter; i egen '
         'virksomhed er samarbejdet med bygherre, rådgiver og andre fag den daglige form.'),
        ('Konstruktive relationer til brugere, rådgivere, leverandører og håndværkere',
         'Brugere og driftsfolk inddraget, før løsninger blev låst; rådgivere og håndværkere fulgt på '
         'pladsen i 11 samtidige projekter; leverandørdialog drevet i 20+ år.'),
        ('Bidrage aktivt til den samlede ledelse af Teknik- og Miljøforvaltningen',
         'Ledelse af tværfaglige leverancer med 25 specialister og 11 samtidige projekter; vant til at '
         'dele ansvaret for helheden og til at blive udfordret på egne beslutninger.')])

    m.save(path)


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_KoegeKommune_ChefEjendomme.docx')
    build(out)
    print(out)
