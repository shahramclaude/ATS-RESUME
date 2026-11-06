# -*- coding: utf-8 -*-
"""LJM Lind Jensen — Quality Manager (Højmark).

Dansk leverance (opslaget er dansk): ansøgning side 1, CV side 2–3.
Policy: master/README.md — ekstrem sikkerhed, ingen forbehold.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Quality Manager · Kvalitet, standarder og mennesker i en international produktion'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('6. november 2026')
    m.meta('LJM Lind Jensen · Højmark · Quality Manager')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Quality Manager, LJM Lind Jensen', bold=True, color='1A1A1A')
    m.para('Til LJM Lind Jensen · att. chefkonsulent Steen Steensgaard Andersen, Career', after=70)

    # ---------------------------------------------------------------- page 1
    m.para('Et certifikat beviser, at systemet findes. Det beviser ikke, at det bliver brugt. Forskellen står ved '
           'maskinen, når en operator holder et emne op og skal afgøre, om det er godt nok — og på mødet, når '
           'nogen skal sige, at en ordre ikke kan sendes på fredag. Kvalitet er de beslutninger, der bliver taget '
           'der, og en kvalitetschefs arbejde er at gøre den rigtige beslutning til den nemmeste. Det er den '
           'stilling, jeg søger hos LJM.', after=80)

    m.para('**Jeg ville lede kvalitetsområdet på fire faste ting.** Først **kvalitet skal kunne ses ved maskinen**: '
           'en Control Plan og en PFMEA er ikke færdige, når de er skrevet — de er færdige, når operatøren ved, '
           'hvad der bliver kontrolleret, hvornår, og hvordan det bliver registreret, og når en afvigelse bliver '
           'fanget i processen i stedet for hos kunden. For det andet **en afvigelse skal lukkes, ikke forklares**: '
           'containment først, en 8D hvor den egentlige rodårsag bliver fundet med data, og en kontrol bagefter, '
           'der viser, at fejlen ikke kommer igen — ellers er der skrevet en rapport, ikke løst et problem. For det '
           'tredje **standarder skal være ens, ikke bare ens på papir**: samme revisionsstandard, samme '
           'acceptniveau og samme eskaleringsvej i Danmark, Kina og Indien, med lokalt ejerskab og én målestok — '
           'det er det eneste, en OEM-kunde kan bruge til noget. For det fjerde **kunden skal høre det fra os**: '
           'PPAP og APQP leveret til tiden, ærlig eskalering og en leverandørkvalitet, der bygger på kritikalitet '
           'og data, ikke på mavefornemmelse.', after=80)

    m.para('Jeg kommer fra produktion og drift, ikke fra et kvalitetskontor. Jeg er uddannet **elektromekaniker**, '
           'har været **produktionsteamleder på ARJ Engineering** med **12 mekanikere og teknikere** i et '
           'maskinværksted og har siden læst mig til **elautoriseret maskinmester med B.Tech i teknologiledelse og '
           'maskinteknik**. Det betyder, at jeg kan gå ned i en bearbejdnings-, svejse- eller montageproces og tale '
           'med dem, der udfører den, om hvad der faktisk kan variere — og det er forudsætningen for, at en PFMEA '
           'bliver en risikovurdering og ikke en formalitet.', after=80)

    m.para('Det regulerede miljø har jeg fra **Novo Nordisk**, hvor jeg i næsten to år arbejdede i et '
           'GMP/FDA/EMA-system: **37 parallelle kapitalprojekter** med **25 specialister**, kravsspecifikation før '
           'udstyr blev bestilt, **FAT/SAT** og **IQ/OQ/PQ** ved modtagelse og idriftsættelse, afvigelser, '
           'korrigerende handlinger og dokumentation, der skulle kunne stå igennem en inspektion — og **nul '
           'kritiske fund** ved aflevering. Det er den samme logik som APQP, PPAP og 8D, bare med et andet '
           'ordvalg og hårdere konsekvenser, og det er der, jeg har lært, at et system kun er så godt som sin '
           'svageste registrering.', after=80)

    m.para('På **Lynetten under Biofos** drev jeg vedligehold og dokumentation på et kritisk anlæg i 24/7-drift: '
           'standarder, 5S og PDCA, målinger og opfølgning, myndighedskrav og leverandører — og en hverdag hvor et '
           'stop ikke var en afvigelse i et skema, men noget der blev målt i timer. Siden 2023 har jeg drevet '
           '**ELOHVAC** med fuldt P&L, hvor kvalitet er det, kunden siger ja til næste gang, og hvor jeg selv har '
           'bygget de tjeklister, den egenkontrol og den dokumentation, der skulle bruges, i Python og Claude — '
           'med over 40 % produktivitetsløft som resultat af, at arbejdsgangene blev ens.', after=80)

    m.para('Det, der især tiltrækker mig ved LJM, er kombinationen af noget meget konkret og noget meget svært: '
           'avanceret metalbearbejdning til vind, hydraulik, biogas og spildevand, hvor tolerancer og svejsninger '
           'skal holde i årtier — og en organisation med egne fabrikker i Danmark, Kina og Indien, hvor den samme '
           'standard skal gælde. Det er en opgave, der bliver løst med mennesker og med målestok, ikke med flere '
           'dokumenter, og det er den slags lederjob, jeg gerne vil have ansvaret for.', after=80)

    m.para('LJM er en familievirksomhed fra 1964, der har bygget hydrauliske komponenter, pumper, propelomrørere og '
           'beluftere til vind, landbrug, biogas og spildevand — og som i dag er **ISO 9001-certificeret**, '
           '**svejsecertificeret efter ISO 3834-2** og siden 2024 også certificeret efter **ISO 14001 og ISO 45001** '
           'af DNV, ved siden af fabrikkerne i Kina og Indien. Det er en kvalitetsrejse, der er taget over 30 år og '
           'ikke over et kvartal, og det er den slags fundament, man bygger videre på i stedet for at starte '
           'forfra.', after=80)

    m.para('Kvalitet, leveringssikkerhed og langsigtede samarbejder er det fundament, I selv peger på — og de bliver '
           'afgjort på ledergruppe-niveau, ikke i en stabsfunktion. Kvalitetsdialogen med en OEM-kunde er en '
           'ledelsesopgave, og en kvalitetskultur bliver ikke skabt af en strategi, men af at ledelsen bliver ved '
           'med at spørge til det samme tal.', after=80)

    m.para('Praktisk: jeg bor i Måløv, har **kørekort B og egen bil**, og Højmark er ikke et dagligt pendlerjob — '
           'jeg lægger en **ugerytme med base i Højmark og hjem i weekenderne**, og rejser gerne til Kina og Indien, '
           'når det kræver det. Jeg kommunikerer på dansk og engelsk og kan starte efter aftale. Jeg vil gerne '
           'høre, hvordan I i dag deler kvalitetsarbejdet mellem Højmark, Kina og Indien, og hvad der er den '
           'største forskel i acceptniveau — det er der, jeg ville begynde.', after=70)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    # ---------------------------------------------------------------- CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Quality Manager med 20+ års erfaring fra teknisk produktion, værksted og reguleret drift — '
           'elautoriseret maskinmester (LV/MV/HV) med B.Tech i teknologiledelse og maskinteknik og '
           'elektromekaniker i bunden. Har arbejdet i et GMP/FDA/EMA-system med afvigelser, '
           'korrigerende handlinger, FAT/SAT og IQ/OQ/PQ og **nul kritiske fund** ved auditeret aflevering; har '
           'ledet 12 mekanikere i et maskinværksted og 14 medarbejdere i en teknisk virksomhed; driver i '
           'dag egen virksomhed med fuldt P&L og har bygget tjeklister, egenkontrol og dokumentation med over '
           '40 % produktivitetsløft.', after=80)

    m.section('KVALITET, STANDARDER OG MENNESKER')
    for label, body in [
        ('Kvalitetsledelse og system',
         'Kvalitetsarbejde forankret i processen: kontrolpunkter pr. proces, sporbarhed, ledelsesevaluering og '
         'opfølgning på KPI — og et system, der bliver brugt, fordi det er enklere end at springe over.'),
        ('Afvigelser og korrigerende handlinger',
         'Containment, rodårsagsanalyse med data og 8D-forløb, der bliver lukket med en kontrol og ikke med en '
         'forklaring; gentagne fejl fulgt tilbage til proces, udstyr eller oplæring.'),
        ('Audit og compliance',
         'Audits og inspektioner i GMP/FDA/EMA-miljø og i 24/7-drift med myndighedskrav: dokumentation, '
         'sporbarhed, egenkontrol og opfølgning, der kunne stå igennem en ekstern gennemgang.'),
        ('Kunde- og leverandørkvalitet',
         'Kravsspecifikation og accept ved modtagelse af udstyr og komponenter, leverandøropfølgning og '
         'reklamationsbehandling i dialog med kunden — herunder dokumentation ved aflevering.'),
        ('Procesudvikling og forbedring',
         'Forbedringsprojekter på tværs af produktion, teknik og indkøb drevet med LEAN og Six Sigma-principper, '
         'standard work, 5S og PDCA — med før- og eftermålinger og flaskehalse fundet ved at måle, hvor emnerne '
         'faktisk ventede.'),
        ('Ledelse og kultur',
         '12 mekanikere i et maskinværksted, 14 medarbejdere i Ventek-Air og 8 i egen virksomhed — MUS og 1:1, '
         'kompetence, oplæring og en tydelig standard, som alle kender og bliver målt på.')]:
        m.bullet(label, body, after=25)

    m.models_table('KVALITETSVÆRKTØJER OG METODER', ('Område', 'Dokumenteret brug'), [
        ('Risiko og kontrol',
         'PFMEA-tankegang pr. proces, Control Plans oversat til kontrolpunkter ved maskinen og acceptkriterier, '
         'der kan læses af den, der udfører opgaven.'),
        ('Produkt- og procesgodkendelse',
         'APQP- og PPAP-logik fra udstyrsprojekter: kravsspecifikation, FAT/SAT, IQ/OQ/PQ, dokumenteret accept og '
         'sporbarhed hele vejen til aflevering.'),
        ('Afvigelser og 8D',
         'Afvigelses- og CAPA-forløb i GMP/FDA/EMA-system, containment, rodårsag, korrigerende handling og '
         'verifikation af, at fejlen ikke gentages.'),
        ('Audit, data og ledelsesevaluering',
         'Interne gennemgange og eksterne inspektioner, revisionschecklister og opfølgning på fund med ejer og '
         'dato; KPI-tavler og egne dataudtræk i Python og Power Query til kassations- og reklamationsanalyser, '
         'rapporteret til ledelsen.'),
        ('Standarder og certificering',
         'ISO 9001 som arbejdsgrundlag i produktionen, ISO 14001/45001-perspektivet på arbejdsmiljø og miljø samt '
         'svejse- og materialekrav dokumenteret i procedurer og instrukser.')])

    m.section('ERHVERVSERFARING')
    jobs = [
        ('Ejer / teknisk direktør',
         'ELOHVAC ApS · København · maj 2023–nu',
         '5 elektrikere og 3 lærlinge · fuldt P&L · el-tekniske service- og entrepriseydelser',
         [('Kvalitet som kundens næste ordre',
           'Egenkontrol, tjeklister, dokumentation og afvigelseshåndtering bygget op i en virksomhed, hvor der ikke '
           'var et system i forvejen; egne værktøjer i Python og Claude har givet over 40 % produktivitetsløft og '
           'gjort arbejdsgangene ens.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem',
         'Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024',
         '37 parallelle kapitalprojekter · 25 specialister · 2–10 mio. kr. pr. projekt · GMP/FDA/EMA',
         [('Reguleret kvalitet og auditeret aflevering',
           'Kravsspecifikation, FAT/SAT og IQ/OQ/PQ ved modtagelse og idriftsættelse af produktionsudstyr; '
           'afvigelser, CAPA og dokumentation i et FDA/EMA-reguleret system; nul kritiske fund ved aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022–nov. 2022',
         '14 medarbejdere · 11 samtidige anlægsprojekter · 2–10 mio. kr. pr. opgave',
         [('Standarder i produktion og montage',
           'Standardiserede arbejdsgange, tavlemøde og afleveringspakker med dokumenteret kontrol; afvigelser '
           'fanget i produktionen frem for ved montage, og omprioritering samme dag når noget faldt væk.')]),
        ('Drifts- og vedligeholdelsesleder',
         'Lynetten under Biofos · København · aug. 2017–jan. 2022',
         'Kritisk procesanlæg i 24/7-drift · pumper, blæsere, ventilation, transformere, koblingsanlæg og SCADA',
         [('Dokumentation, målinger og myndighedskrav',
           '5S og standard work på værksted og lager, tilstandsbaseret vedligehold med målinger, kalibrering af '
           'måleværktøj og opfølgning, '
           'myndighedskrav og leverandører — og energiledelse med over 40 % lavere forbrug dokumenteret.')]),
        ('Elektromekaniker / produktionsteamleder',
         'ARJ Engineering · Teheran · dec. 2003–mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · industrielt udstyr',
         [('Bearbejdning, svejsning og montage',
           'Klargøring, reparation og fejlfinding på industrielt udstyr med drejning, fræsning, svejsning og '
           'montage; tolerancekrav og funktionskontrol, vagtplanlægning og mål for 12 teknikere.')]),
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
           'egen bil · Ugependling Måløv–Højmark med base i Højmark · Rejser gerne til Kina og Indien · Kan starte '
           'efter aftale · SAP og Excel dagligt, Python til data og systemer · Referencer på forespørgsel.', after=70)

    m.models_table('DET DE EFTERSPØRGER — DET HAR JEG', ('Krav i opslaget', 'Dokumentation'), [
        ('Lederrolle i metalindustrien',
         'Produktionsteamleder for 12 mekanikere i et maskinværksted, leder af 14 medarbejdere i Ventek-Air og '
         'ejer af egen teknisk virksomhed med 8 medarbejdere siden 2023.'),
        ('Solid erfaring med kvalitetsstyring og procesudvikling',
         'Kvalitetsarbejde i et GMP/FDA/EMA-system med afvigelser, CAPA og dokumentation; standard work, 5S og '
         'PDCA med før- og eftermålinger i 24/7-drift og i egen virksomhed.'),
        ('Implementering af kvalitetsledelsessystemer',
         'Bygget egenkontrol, tjeklister, procedurer og dokumentation op fra nul i egen virksomhed; arbejdet i '
         'systemer, hvor certificering var en forudsætning for at levere, og hvor en inspektion var en reel risiko.'),
        ('Kunde- og leverandørkvalitet i internationale miljøer',
         'Kravsspecifikation og accept ved modtagelse af udstyr med leverandører i flere lande; '
         'reklamationsbehandling og dokumentation ved aflevering til bygherre, kunde og øvrige interessenter.'),
        ('Teknisk forståelse for bearbejdning, svejsning og montage',
         'Uddannet elektromekaniker og maskinmester; arbejdet med CNC-drejning, fræsning, svejsning og montage i et '
         'maskinværksted og gennem idriftsættelse af produktionsudstyr.'),
        ('APQP, PPAP, PFMEA, Control Plans, VDA 6.3, 8D og SQM',
         'Samme logik anvendt i praksis: krav før bestilling, FAT/SAT og PPAP-lignende accept, risikovurdering pr. '
         'proces, kontrolpunkter i driften, 8D-forløb og audit af processen med opfølgning på fund.'),
        ('Understøtte indkøring af nye produkter og processer',
         '37 kapitalprojekter med 25 specialister, fra krav og designreview til idriftsættelse i levende '
         'produktion; indkøring planlagt med kontrolpunkter, oplæring og dokumenteret accept.'),
        ('Struktureret håndtering af afvigelser, reklamationer og korrigerende handlinger',
         'Afvigelses- og CAPA-forløb med containment, rodårsag og verifikation; gentagne fejl fulgt tilbage til '
         'proces eller oplæring i stedet for til den enkelte medarbejder.'),
        ('Audits, ledelsesevalueringer og certificeringer',
         'Interne gennemgange og eksterne inspektioner i GMP/FDA/EMA-miljø; revisionschecklister, opfølgning med '
         'ejer og dato og status rapporteret til ledelsen.'),
        ('Tydelig og synlig leder med gennemslagskraft og følgeskab',
         'MUS og 1:1, daglige tavlemøder og beslutninger taget tæt på opgaven med begrundelse; standarder '
         'forankret hos dem, der skal leve op til dem — også på tværs af fagligheder og kulturer.')])
    m.page_break()

    m.models_table('DE FØRSTE 90 DAGE — SYSTEMET, PROCESSERNE OG DE TRE LANDES',
                   ('Periode', 'Hvad der sker, og hvordan det måles'), [
        ('Uge 1–2',
         'Gå runder i bearbejdning, svejsning og montage sammen med kvalitetsorganisationen; læs de væsentligste '
         'kundeafvigelser og de sidste to audits igennem; mød de syv medarbejdere og få deres billede af, hvor '
         'systemet holder, og hvor det bliver omgået.'),
        ('Dag 30',
         'Én fælles revisionsstandard for Højmark, Kina og Indien med samme acceptniveau og eskaleringsvej; '
         'status på åbne 8D-forløb og PPAP-leverancer synlig for ledergruppen; aftalt kadence for kvalitetsmøder '
         'med produktion, teknik, indkøb og salg.'),
        ('Dag 60',
         'Control Plans og PFMEA gennemgået for de fem mest kritiske processer og oversat til kontrolpunkter, '
         'operatørerne kan følge; leverandørkvalitet prioriteret efter kritikalitet; første forbedringsprojekt '
         'målt før og efter.'),
        ('Dag 90',
         'Kvalitetsstrategien lagt frem for direktionen med mål, ejere og datoer; ledelsesevaluering afholdt på et '
         'datagrundlag, der kan bruges; og en plan for, hvordan Kina og Indien bliver auditeret på samme standard '
         'som Højmark.')])

    m.section('ET CERTIFIKAT BEVISER, AT SYSTEMET FINDES')
    m.para('Det er ikke en indvending mod certifikater — det er en påmindelse om, hvad de kan. Et certifikat siger, '
           'at processerne er beskrevet, og at nogen har set dem efter. Det siger ikke, om en operator på natholdet '
           'stopper et emne, fordi han kan se, at noget er ved at drive. Det afgør, om kunden får en reklamation '
           'eller en tanke. Derfor arbejder jeg med to ting på samme tid: systemet, så det er reviserbart, og '
           'adfærden, så det er sandt.', after=80)

    m.section('KVALITET ER EN BESLUTNING VED MASKINEN')
    m.para('Ingen kvalitetschef kontrollerer et emne, der er ved at blive produceret. Det gør den, der står ved '
           'maskinen — eller ingen gør. Så spørgsmålet er, om han ved, hvad der er godt nok, om han har tid til at '
           'se efter, og om han er tryg ved at stoppe. Det sidste er et ledelsesansvar, og det er der, jeg lægger '
           'arbejdet: acceptkriterier ved maskinen, tid i planen til at kontrollere, og en tydelig beskyttelse af '
           'dem, der siger fra.', after=80)

    m.section('EN 8D DER ENDER I EN RAPPORT, KOMMER IGEN')
    m.para('Det er nemt at lukke en afvigelse. Det er sværere at lukke den, så den ikke kommer tilbage. Containment '
           'skal ske med det samme, fordi kunden ikke skal have flere fejlbehæftede emner, mens vi tænker — men '
           'rodårsagen skal findes i data: hvilke emner, hvilken maskine, hvilket skift, hvilken ændring skete '
           'der omkring. Og der skal stå en kontrol tilbage, der kan vise, at virkningen er væk, tre måneder '
           'senere. Det er den kontrol, der gør en 8D færdig, ikke otte punkter i et skema.', after=80)

    m.section('TRE LANDE, ÉN MÅLESTOK')
    m.para('Når kvaliteten er delt mellem Danmark, Kina og Indien, er den sværeste opgave ikke at skrive en '
           'procedure — det er at sikre, at den samme fejl bliver vurderet lige strengt tre steder. Det kræver '
           'samme checkliste, samme acceptniveau og samme eskaleringsvej, og at de lokale ledere ejer standarden '
           'og ikke bare modtager den. Jeg bygger på de kompetencer, der er der i forvejen, og måler på de samme '
           'få tal.', after=80)

    m.section('KUNDEN SKAL HØRE DET FRA OS, IKKE FRA SIN KUNDE IGEN')
    m.para('En OEM-kunde glemmer ikke en fejl, der kom til dem uden varsel. Derfor skal dårlige nyheder gå den '
           'korte vej: vi ringer, før de opdager det, vi har containment med, og vi har en dato. Det er også '
           'grundlaget for leverandørkvaliteten: indgående kontrol og opfølgning prioriteret efter, hvad der '
           'faktisk kan stoppe vores produktion eller nå kunden — ikke efter, hvad der er nemt at kontrollere.',
           after=80)

    m.section('NYE PRODUKTER FEJLER I OVERGANGEN, IKKE I PRODUKTIONEN')
    m.para('De fleste kvalitetsproblemer bliver født, før den første serie kører: et krav, der ikke blev skrevet '
           'ned, et værktøj, der ikke blev prøvet af, en proces, der blev godkendt på papir. Derfor skal kvalitet '
           'ind i APQP-arbejdet tidligt — i kravspecifikation, designreview, prøvekørsel og accept — og der skal '
           'ligge et PPAP, når produktionen starter, ikke en undskyldning bagefter.', after=80)

    m.section('JEG HAR ARBEJDET I ET SYSTEM, HVOR FEJL HAVDE KONSEKVENSER')
    m.para('På Novo Nordisk var dokumentation ikke bureaukrati, den var produktet: hvis en afvigelse ikke var '
           'beskrevet, var den ikke håndteret, og hvis en ændring ikke var godkendt, var den ikke gennemført. Det '
           'har givet mig en vane, som jeg tager med: at skrive det ned, mens det sker, at lukke det, man har åbnet, '
           'og at måle, om det virkede. Det er ikke et system, der gør arbejdet sværere — det er det, der gør det '
           'muligt at sove om natten, når kunden ringer.', after=80)

    return m.save(path, title='Quality Manager — LJM Lind Jensen',
                  subject='Kvalitetsledelse, standarder og international kvalitetsorganisation',
                  keywords='quality manager, kvalitetschef, kvalitetsledelse, ISO 9001, APQP, PPAP, PFMEA, '
                           'Control Plans, VDA 6.3, 8D, SQM, audit, certificering, reklamationer, CAPA, '
                           'metalindustri, dansk, engelsk')


if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_LJM_QualityManager.docx')))
