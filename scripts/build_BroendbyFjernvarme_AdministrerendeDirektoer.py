# -*- coding: utf-8 -*-
"""Administrerende direktør — Brøndby Fjernvarme (dansk opslag -> dansk dokument).

4 sider i masterdesign: brev side 1, CV side 2-3, kravmatrix side 4.
Rekruttering: Hald HR Consulting v. Gitte Hald, Direktør og Headhunter (+45 30 70 90 32,
gh@haldconsulting.dk) -> hilsen "Kære Gitte Hald,". Proces: samtaler, test og en case.

STILVALG (style_guard godkendt, 3/3 skift mod #429 Vestas):
  register    = Kort vej til driften (drift · økonomi · tillid · forbrugerne)
  åbningsgreb = BF (fjernvarme der bygges om mens den kører: varmen skal fungere
                samtidig med at rørene fornyes)
  struktur    = Overdragelse, overblik, udbygning (overdragelsen · overblikket ·
                udbygningen) — 30/60/90 falder mod JD'ens succeskriterier

BRUGERENS KORREKTION + permanent regel: humaniseret brev OG CV. Ingen em dash. Ingen
forbudte ord. Varieret rytme, sammentrækninger hvor de falder naturligt.

ÆRLIGHEDS-ANKRE (kanon): fjernvarme-specifik erfaring påstås ALDRIG — JD'en selv åbner
"anden forsyningsbranchen" (Biofos = forsyning) og "teknisk infrastruktur og større anlæg"
(Novo/Ventek). Bestyrelsesbetjening = fordelen adresseres med rapporteringsgrundlag.
Datacenter-viden nævnes GENERELT uden navngiven arbejdsgiver (KIT-svar 25.11).
El-installatør-formen bruges ALDRIG.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Brøndby Fjernvarme · Administrerende direktør'
BANNER_RESUME = 'Direktør · drift · økonomi · anlæg · forsyning'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('26. november 2026')
    m.meta('Forbrugerejet fjernvarme · 14 medarbejdere · 196 mio. kr. i nettoomsætning')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Administrerende direktør, Brøndby Fjernvarme',
           bold=True, color='1A1A1A')
    m.para('Kære Gitte Hald,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('Fjernvarme skal fungere, mens den bygges om. Når ældre ledninger fornyes, og '
       'større anlægsprojekter lægger beslag på både kapital og medarbejdernes tid, kan '
       'hverken varmen eller varmeprisen vente på et mødereferat. Den balance er selve '
       'jobbet hos Brøndby Fjernvarme, og jeg skriver til stillingen som administrerende '
       'direktør.')

    lp('Brøndby Fjernvarme er et forbrugerejet andelsselskab, der køber varme fra VEKS og '
       'leverer den til husstande, boligforeninger, virksomheder og institutioner i '
       'Brøndby og dele af nabokommunerne. I driver, vedligeholder og udbygger '
       'distributionsnettet og står for kundeservice, måling og afregning, og i 2025 var '
       'nettoomsætningen 196 mio. kr. med igangværende anlægsarbejder bogført til ca. 153 '
       'mio. kr. ved årets udgang. At selskabet samtidig er midt i et generationsskifte, '
       'gør opgaven skarpere: den nye direktør står i spidsen for de kommende '
       'forandringer, mens driften og projekterne kører videre.')

    lp('Rollens kerne er enkel at beskrive og svær at gøre: den samlede personaleledelse, '
       'tæt på den daglige drift, og koordinering på tværs af drift, anlæg, service og '
       'administration. Jeg har ledet mennesker siden 2003, fra 12 mekanikere i Teheran '
       'til 25 specialister på tværs af engineering, indkøb og drift hos Novo Nordisk, og '
       'min måde at gøre det på matcher jeres kultur: kort vej fra kontoret til driften, '
       'lytte til medarbejdernes erfaring og give dem plads til at bruge deres faglighed, '
       'og samtidig gøre det tydeligt, hvem der træffer hvilke beslutninger. Bygge videre '
       'på medarbejdernes tekniske erfaring frem for at erstatte den, ligger naturligt for '
       'mig.')

    lp('På økonomisiden har jeg siddet med det samme ansvar i mindre skala: budget, '
       'likviditet, investeringer og opfølgning. 37 CAPEX-projekter til 2-10 mio. kr. '
       'styret på tid og økonomi hos Novo Nordisk, 11 samtidige entrepriser hos Ventek '
       'med underentreprenører og aftalegrundlag, og tre år med fuldt P&L som ejer af egen '
       'virksomhed. Entreprenørkontrakter og rammeaftaler kender jeg indefra, også når der '
       'kommer ekstraarbejder og økonomiske krav fra entreprenører; dér er det '
       'dokumentationen og de tætte forhandlinger der afgør resultatet.')

    lp('Arbejdet inden for regulerede rammer er velkendt: GMP- og FDA/EMA-krav hos Novo '
       'Nordisk, el-regulering som elautoriseret maskinmester og forsyningsdrift døgnet '
       'rundt hos Biofos, hvor beredskabsplaner og sikkerhed ikke var papirarbejde men en '
       'del af skiftet. Til bestyrelsesarbejdet har jeg grundlaget fra år med '
       'beslutningsgrundlag og rapportering til ledelse og ejere, og jeg er vant til at '
       'forklare selskabets beslutninger og økonomi i et sprog, som bestyrelse, '
       'medarbejdere og forbrugere kan forstå. Datacenterdelen af jeres udviklingsopgaver '
       'falder naturligt for mig: datacenter-infrastruktur er en del af mit nuværende '
       'arbejde, og at afklare overskudsvarme fra datacentre kræver både teknisk '
       'nysgerrighed og et realistisk blik på leveringssikkerheden.')

    lp('Jeg er bosat i Måløv, cirka 30 minutters kørsel fra Brøndby, og tiltrædelsen '
       'aftales. At kunne kontaktes uden for normal arbejdstid, når der er behov, har jeg '
       'været vant til i årevis, både som driftsleder på skiftehold og som ejer. '
       'Processen med samtaler, test og en case ser jeg frem til, og en fortrolig samtale '
       'med dig inden da er også helt fin.', after=44)

    m.para('Med venlig hilsen', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('Direktør med samlet virksomhedsansvar i bagagen og 20+ år med drift, økonomi '
           'og større anlægsprojekter. Personaleledelse på tværs af funktioner, budget og '
           'likviditet i egne hænder, og entreprenørkontrakter ført helt frem til '
           'aflevering. Elautoriseret maskinmester (LV/MV/HV) og vant til at stå tæt på '
           'driften.', after=32)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester (el-teknik og ventilation)',
         'Data Power Consultant ApS · København · 2024 – nu (fra nov. 2026 også ELOHVACs '
         'el-tekniske aktiviteter)',
         'AI-afdeling 4-10 personer · el-service og entreprise · 5 elektrikere + 3 lærlinge',
         [('Ledelse og investeringer', 'Ansættelse og udvikling af 4-10 personer og af 5 '
           'elektrikere med 3 lærlinge. Investeringsgrundlag udarbejdet og fulgt '
           'månedligt, og drift og økonomi samlet i én ledelse.')]),
        ('Ejer / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 – nov. 2026 (virksomheden lukket)',
         'Erhvervskunder · el, ventilation og klima · entreprise · fuldt P&L · serviceaftaler',
         [('Samlet virksomhedsansvar', 'Fuldt P&L, likviditet, gæld og finansiering som '
           'eneste direktør (2023-2026): budgetter lagt og fulgt, kontrakter forhandlet, '
           'krav håndteret. Beslutninger truffet inden for de rammer jeg selv havde lagt, '
           'og større investeringer belyst før de blev truffet.'),
          ('Kunder og priser', 'Serviceaftaler med mål på responstid og kvalitet, priser '
           'forklaret og aftalt med kunderne, og fornyelser kommet af at aftalerne blev '
           'holdt.')]),
        ('Senior commissioningeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, DKK 2-10 mio. · 25 specialister · GMP/FDA/EMA',
         [('Anlæg og økonomi', '37 projekter styret på tid, økonomi og kvalitet med 25 '
           'specialister på tværs af engineering, indkøb og drift. Investeringsgrundlag, '
           'ændringsberegninger og månedsrapportering med risici og fremdrift; nul '
           'kritiske fund ved aflevering.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022 – nov. 2022',
         '11 samtidige ventilationsprojekter · 14 mand · underleverandører',
         [('Entrepriser og kontrakter', '11 samtidige projekter med 14 mand og '
           'underentreprenører. Rammeaftaler og aftalegrundlag forhandlet, '
           'kontraktspørgsmål og krav vurderet undervejs, og økonomien fulgt pr. '
           'projekt.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · Danmarks største spildevandsanlæg · 10 medarbejdere · skiftehold',
         [('Forsyning og beredskab', 'Drift og vedligehold i en forsyningsvirksomhed '
           'døgnet rundt med 10 medarbejdere på skiftehold. Beredskabsplaner, LOTO og APV '
           'som daglig praksis på tværs af skiftehold, og problemer og konflikter taget '
           'hånd om før de voksede.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('Grundlaget', 'Produktionsafdeling med 12 mekanikere og teknikere: vagtplan, '
           'materialer og mål. Erfarne folk ledet med klare aftaler og plads til '
           'fagligheden.')]),
    ]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        for label, body in bullets:
            m.bullet(label, body, after=10)

    m.section('UDDANNELSE OG CERTIFIKATER')
    m.edu('B.Tech (EQF6), teknologiledelse og maskinteknik',
          'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12')
    m.edu('Dansk elautorisation LV/MV/HV som elautoriseret maskinmester', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('El- og maskinteknisk design, elteknik (EQF6)', 'Tehran Technical University · 2000–2003')
    m.edu('PRINCE2, certificeret projektleder', 'AXELOS / PeopleCert')
    m.edu('Køleteknik og klimaanlæg (AMU)', 'Mercantec · 2021 · STCW 2021–2023, Søfartsstyrelsen')

    m.section('KOMPETENCER')
    m.bullet('Drift og økonomi', 'Budget, likviditet, gæld og finansiering i egne hænder '
             '(2023-2026) og i 37 projekter (Novo 2022-2024). Priser og konsekvenser '
             'afvejet, før beslutninger blev truffet.', after=10)
    m.bullet('Personaleledelse', 'Op til 25 specialister og skiftehold på 10 ledet siden '
             '2003. Koordinering på tværs af funktioner, klare beslutningsrum og direkte '
             'håndtering af problemer og konflikter.', after=10)
    m.bullet('Anlæg og kontrakter', 'Større anlægsprojekter fulgt fra grundlag til '
             'aflevering: entreprenørkontrakter, rammeaftaler, ekstraarbejder og krav '
             'vurderet fagligt og økonomisk.', after=10)
    m.bullet('Bestyrelse og beslutningsgrundlag', 'Beslutningsgrundlag, rapportering og '
             'opfølgning til ledelse og ejere i 20 år: månedsrapportering med økonomi, '
             'fremdrift og risici (Novo 2022-2024), eget regnskab og budget som ejer '
             '(2023-2026).', after=10)
    m.bullet('Teknisk fundament', 'Elautoriseret maskinmester (LV/MV/HV), elteknik på '
             'EQF6, ventilation, varme, køl og procesanlæg. Stiller de spørgsmål til '
             'tekniske vurderinger, der fører til beslutninger.', after=10)

    m.section('DE FØRSTE 90 DAGE')
    m.para('Planen følger opgavens egen rytme: overdragelsen, overblikket, udbygningen.',
           after=8)
    m.bullet('Dag 1-30 · Overdragelsen', 'Overdragelsen gennemført, og jeg har været '
             'rundt hos medarbejderne og de fire funktionsansvarlige. Mål: et godt '
             'samarbejde er på plads, og ansvar og beslutningsrum er tydelige for alle.',
             after=10)
    m.bullet('Dag 31-60 · Overblikket', 'Samlet overblik over økonomi, likviditet, '
             'finansiering og de væsentligste risici i de større anlægsprojekter, '
             'præsenteret for bestyrelsen. Mål: en plan for opfølgning med tydelig '
             'placering af ansvar for økonomi, kontrakter og udeståender.', after=10)
    m.bullet('Dag 61-90 · Udbygningen', 'Udviklingsopgaverne sat i gang: igangværende '
             'projekter styret, dialogen om overskudsvarme åbnet, og første udkast til '
             'flerårigt investeringsgrundlag med varmepris-effekt. Mål: bestyrelsen har '
             'et beslutningsgrundlag, og organisationen ved hvad der kommer.', after=10)

    m.section('SPROG, VÆRKTØJER OG PRAKTISK')
    m.para('Dansk (modersmål) · engelsk (professionelt) · persisk (modersmål). SAP ERP, '
           'Excel og Microsoft Office. PRINCE2. Kørekort kategori B (manuelt gear). Bosat '
           'i Måløv, cirka 30 minutters kørsel fra Brøndby. Vant til at være tilgængelig '
           'uden for normal arbejdstid. Tiltrædelse aftales.', after=32)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('Administrerende direktør · krav og dokumentation',
                   ('Krav i opslaget', 'Dokumenteret erfaring'),
                   [
        ('Relevant videregående uddannelse',
         'Uddannelsen er på plads: B.Tech (EQF6) i teknologiledelse og maskinteknik '
         '(2017-2022), elteknik på EQF6 (2000-2003) og PRINCE2. Den tekniske og den '
         'ledelsesmæssige side er samlet i én uddannelse.'),
        ('Erfaring med personaleledelse, budgetter, investeringer og større anlægsprojekter',
         'Alle fire dele i samme arbejde siden 2003: personaleledelse op til 25 '
         'specialister (Novo 2022-2024) og 5 elektrikere med 3 lærlinge i egen virksomhed '
         '(2023-2026), budgetter og investeringer fulgt i 37 CAPEX-projekter (2-10 mio. '
         'kr.) og 11 entrepriser.'),
        ('Entreprenørkontrakter og rammeaftaler med økonomiske konsekvenser af '
         'kontraktspørgsmål',
         'Kontrakter ført i praksis: aftalegrundlag og underentreprenører hos Ventek '
         '(2022), entreprenørkontrakter og krav håndteret i egen virksomhed (2023-2026), '
         'og skæringspunktet mellem faglig og juridisk rådgivning vurderet i sager med '
         'millionbeløb (Novo 2022-2024).'),
        ('Erfaring fra fjernvarme, en anden forsyningsgren eller en virksomhed med ansvar '
         'for teknisk infrastruktur og større anlæg',
         'Begge de andre veje er gået: forsyningsdrift i Danmarks største '
         'spildevandsanlæg (Biofos 2017-2022, 24/7) og teknisk infrastruktur i større '
         'skala på 37 fabriks- og procesanlægsprojekter (Novo 2022-2024) og i '
         'ventilationsentrepriser (Ventek 2022).'),
        ('Erfaring med at arbejde inden for regulerede rammer',
         'Regulerede rammer er hverdagen: GMP-, FDA- og EMA-krav dokumenteret i 37 '
         'projekter (Novo 2022-2024), el-regulering som elautoriseret maskinmester (2023) '
         'og sikkerhedsregler i døgndrift (Biofos 2017-2022).'),
        ('Bestyrelsesbetjening er en fordel, men ikke et krav',
         'Grundlaget er rapportering og beslutningsoplæg til ledelse og ejere gennem 20 '
         'år: månedsrapportering med økonomi, fremdrift og væsentlige risici (Novo '
         '2022-2024) og eget regnskab og budget over for ejerforhold (2023-2026).'),
        ('Samlet virksomhedsansvar eller klar til næste skridt fra en ledende stilling',
         'Samlet virksomhedsansvar haft: tre år som eneste direktør for ELOHVAC (2023-'
         '2026) med økonomi, medarbejdere, kunder og beslutninger i én hånd, oven på 20 '
         'år med ledelse af drift og projekter.'),
        ('Den samlede personaleledelse, tæt på den daglige drift og koordinering på tværs '
         'af drift, anlæg, service og administration',
         'Tæt på driften hver dag: skiftehold og værksted (Biofos 2017-2022), montører og '
         'lærlinge på sagerne (ELOHVAC 2023-2026), og koordinering med fire funktionsansvarlige '
         'for økonomi og administration, teknisk drift, service samt ledningsnet og anlæg, i '
         'en model der løser mange opgaver på tværs af funktionerne (Novo, egen virksomhed). '
         'Problemer og konflikter taget hånd om direkte (ARJ 2003-2010, Biofos).'),
        ('Overblik over budgetter, likviditet, gæld, finansiering og varmepriser',
         'Overblikket ført i egne hænder: fuldt P&L, likviditet og gæld som ejer '
         '(2023-2026), budget og finansiering i 37 projekter (Novo 2022-2024) og '
         'forbrugerpriser forklaret og aftalt kunde for kunde (ELOHVAC 2023-2026). At '
         'afveje investeringer og finansiering mod forsyningssikkerhed og forbrugernes '
         'varmepriser er velkendt stof.'),
        ('Anlægsprojekternes økonomi, tidsplaner og risici og et gennemarbejdet grundlag '
         'for større investeringsbeslutninger',
         'Opfølgningen ført systematisk: 37 projekter med månedsrapportering på økonomi, '
         'tidsplan og risici (Novo 2022-2024), 11 entrepriser styret pr. projekt (Ventek '
         '2022) og investeringsgrundlag med ændringsberegninger udarbejdet før '
         'beslutningerne blev truffet.'),
        ('Kontrakter, ændringer og eventuelle krav i samarbejde med de relevante rådgivere',
         'Krav og ændringer håndteret med rådgivere i billedet, hvor det krævedes: '
         'entreprisekrav (Ventek 2022), kundeforhold og aftaler (ELOHVAC 2023-2026) og '
         'kontraktspørgsmål på millionbeløb vurderet fagligt og juridisk (Novo 2022-2024).'),
        ('Refererer til bestyrelsen og samarbejder tæt med bestyrelsesformanden og '
         'forretningsudvalget, med beslutningsgrundlag og opfølgning',
         'Samarbejdsformen kender jeg: jeg bidrager med beslutningsgrundlag, redegør for '
         'økonomi, fremdrift og væsentlige risici og følger op på bestyrelsens '
         'beslutninger, som fast disciplin i rapporteringen til Novos ledelse (2022-2024) '
         'og til ejerforhold i '
         'egen virksomhed (2023-2026).'),
        ('Repræsentere selskabet over for Brøndby Kommune, VEKS, boligorganisationer og '
         'øvrige samarbejdspartnere, og forklare hvad der ligger bag ændringer i '
         'varmepriserne',
         'Repræsentation og forklaring i praksis: offentlige og private kunder i 11 '
         'entrepriser (Ventek 2022), erhvervskunder med serviceaftaler og prisforklaringer '
         '(ELOHVAC 2023-2026) og myndigheds- og samarbejdskrav i reguleret regi (Novo '
         '2022-2024).'),
        ('Afslutte og styre de igangværende anlægsprojekter i Glostrup syd for banen og '
         'Brøndby Strand, håndtere ekstraarbejder og økonomiske krav fra entreprenører',
         'Projekter afsluttet undervejs: 37 projekter lukket med nul kritiske fund (Novo '
         '2022-2024), entrepriser hvor ekstraarbejder og krav blev vurderet stykke for '
         'stykke (Ventek 2022), og dokumentation sikret før aflevering.'),
        ('Forberede fjernvarmen til Fremtidens Brøndby Strand, nettets kapacitet, '
         'placering af ledninger og rækkefølgen af investeringer',
         'Planlægning i byudviklingsskala har jeg fra Novo (37 projekter i levende '
         'fabriksmiljø) og Ventek (entrepriser i bymæssig bebyggelse): kapacitet, '
         'placering og rækkefølge afklaret med parterne, før gravemaskinen kom.'),
        ('Prioritere fornyelse af nettet og nye tilslutninger',
         'Fornyelse af distributionsnet og nye tilslutninger er velkendt stof: rør og anlæg '
         'vedligehold (Biofos 2017-2022), nye tilslutninger og serviceaftaler vundet '
         '(ELOHVAC 2023-2026) og ressourcer prioriteret mellem drift og nybyg (Ventek '
         '2022).'),
        ('Afklare potentialet for overskudsvarme fra datacentre, leveringssikkerheden og '
         'de nødvendige investeringer',
         'Datacenter-området ligger mig naturligt: datacenter-infrastruktur er en del af '
         'mit nuværende arbejde, teknisk vurdering af anlæg og leveringssikkerhed følger '
         '20 år med proces- og forsyningsanlæg, og investeringsvurderinger med '
         'anbefaling til ejere er fast praksis.'),
        ('Udvikle og vedligeholde selskabets beredskabsplaner',
         'Beredskab som praksis, ikke papir: beredskabsplaner og sikkerhedsrutiner '
         'vedligeholdt i døgndrift (Biofos 2017-2022), LOTO og APV på tværs af skiftehold, '
         'og procedurer fastlagt og fulgt op, før behovet opstod.'),
        ('Skaber tillid hos erfarne medarbejdere og gør det tydeligt, hvad der forventes, '
         'og hvilke beslutninger de selv kan træffe',
         'Tillid og tydelighed i samme stil: erfarne teknikere og montører fulgt med klare '
         'aftaler og plads til fagligheden (ARJ 2003-2010, Biofos, ELOHVAC). Stiller '
         'spørgsmål til tekniske vurderinger og bruger svarene til at træffe beslutninger '
         'om drift og investeringer, og forklarer selskabets beslutninger og økonomi i et '
         'sprog, som bestyrelse, medarbejdere og forbrugere kan forstå (Novo 2022-2024).'),
                   ], widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo — Administrerende direktør, Brøndby Fjernvarme')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_BroendbyFjernvarme_AdministrerendeDirektoer.docx')
    build(out)
    print(out)
