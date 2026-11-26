# -*- coding: utf-8 -*-
"""El-faglig Projektleder til elinstallationer i Datacentre — Kemp & Lauritzen A/S,
Albertslund (dansk opslag -> dansk dokument).

4 sider i masterdesign: brev side 1, CV side 2-3, kravmatrix side 4.
Kontakt fra opslaget: Afdelingschef Martin Stokholm Vinding, tlf. 21186268
-> hilsen "Kære Martin Stokholm Vinding,". Samtaler løbende, ingen frist.

STILVALG (style_guard godkendt, 3/3 skift mod #431 Terma):
  register    = Kritisk infrastruktur (driftssikkerhed · kvalitet · tværfaglighed ·
                ordentlighed)
  åbningsgreb = BH (strømmen der ikke må falde ud: et datacenter har ingen tilladelse
                til nedetid — ikke mens det bygges, ikke mens det idriftsættes)
  struktur    = Tilbud, udførelse, idriftsættelse (tilbuddet · udførelsen ·
                idriftsættelsen)

BRUGERSVAR 26.11 (bindende): TIER begreberne fra Uptime Institute + Microsoft Project =
REEL erfaring (skrives selvsikkert). Kalkia + BIM/Revit-miljøer = ukendte (korte ærlige
fordels-noter). Canalis = ikke i kanon (ærlig note).

MASTER-REGLER: "elautoriseret maskinmester (LV/MV/HV)" — ALDRIG "elinstallatør"/
"el-installatør". "installatør" i JD-citat (rk2-label) er JD'ens eget ord og OK; den
påstås ikke som kandidatens titel. Datacenter-viden nævnes GENERELT uden navngiven
arbejdsgiver (KIT-svar 25.11). Kanonisk værktøjskasse (MASTER_RESUME §5, behandles som
sand): UPS, ABA/ABV, fiber, solcelleanlæg, AB 18, ABT 18, KS/kvalitetssikring,
DS/HD 60364, SB-vejledning, idriftsættelse, opmåling, underentreprenører.

BRUGERENS KORREKTION: humaniseret brev OG CV. Ingen em dash. Ingen forbudte ord.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'
BANNER_LETTER = 'Kemp & Lauritzen · El-faglig projektleder, datacentre'
BANNER_RESUME = 'Projektledelse · el · datacentre · commissioning · kunder'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, BANNER_LETTER,
                    'Måløv · +45 93 99 95 14 · ajlooshahram@gmail.com · '
                    'linkedin.com/in/shahramajloo')
    m.meta('26. november 2026')
    m.meta('Datainfrastruktur · Albertslund · el, UPS, generator og fiber')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: El-faglig projektleder til elinstallationer i datacentre',
           bold=True, color='1A1A1A')
    m.para('Kære Martin Stokholm Vinding,', after=8, line=236)

    def lp(text, after=52):
        return m.para(text, after=after, line=236)

    # ------------------------------------------------------------- side 1
    lp('Et datacenter har ingen tilladelse til nedetid. Ikke mens anlægget bygges, ikke '
       'mens det idriftsættes, og aldrig når det først kører. At drive projekter inden '
       'for kritisk infrastruktur og fremtidens datacentre er derfor en opgave hvor '
       'driftssikkerheden følger med hver beslutning. Ansvar for teknisk '
       'komplekse og forretningskritiske projekter er det jeg søger, som el-faglig '
       'projektleder i Albertslund.')

    lp('Kemp & Lauritzen er Danmarks førende digitale og grønne teknikpartner med 3.000 '
       'medarbejdere, og afdelingen Datainfrastruktur tæller ca. 120 engagerede '
       'medarbejdere, der projekterer, installerer og servicerer moderne '
       'infrastrukturløsninger: datainfrastruktur og nødstrømsinstallationer bestående af '
       'el-, UPS-, generator- og fiber-installationer. I leverer totalentrepriser som '
       'design & build og arbejder på tværs af brand, sikring, HVAC og Engineering. At '
       'Kemp & Lauritzen Fonden ejer virksomheden og investerer i medarbejdere og '
       'samfundet, passer til en arbejdsplads med samarbejde, høj faglighed og '
       'ordentlighed. Et stærkt fagligt miljø med erfarne specialister er præcis sådan '
       'jeg helst arbejder.')

    lp('Rollens opgaver er præcis de faser jeg kender: komplekse projekter fra start til '
       'slut, i kæden design, tilbud, planlægning og implementering, og moderne '
       'datacenterløsninger hvor driftssikkerhed, kvalitet og tværfagligt samarbejde er '
       'afgørende for succes. Jeg har gået den vej før: 37 CAPEX-projekter med '
       'commissioning, test og idriftsættelse hos Novo Nordisk, el-installationer og '
       'UPS-opgaver i el-faget, og kritiske anlæg i døgndrift hos Biofos. Samarbejdet '
       'mellem kunder, rådgivere, entreprenører og tekniske specialister er ikke nyt for '
       'mig; det er hverdagen i en totalentreprise.')

    lp('Regnestykkerne hører med: effekt og belastningsberegninger har jeg lavet siden '
       'el-teknik-uddannelsen og i ventilationens energiberegninger, og kortslutningsberegninger'
       'og selektivitetsstudier ved jeg hvor jeg får hjælp, når Engineering '
       'er inde over. Installationsbekendtgørelsen og relevante standarder, DS/HD 60364 '
       'og SB-vejledningerne, er mit daglige sprog som elautoriseret maskinmester '
       '(LV/MV/HV). TIER begreberne fra Uptime Institute kender jeg fra '
       'datacenter-arbejdet, og Microsoft Project er mit faste planlægningsværktøj. To '
       'ting fra fordelslisten mangler jeg: Kalkia og BIM/Revit-miljøer kender jeg ikke '
       'fra praksis; kalkulation og tilbudsberegning har jeg lavet siden 2017 i SAP og '
       'Excel.')

    lp('Ledelsesansvar og planlægningsansvar for teknikere følger med opgaven, og den '
       'del har jeg stået i siden 2003, fra 12 mekanikere til 25 specialister på tværs af '
       'engineering, indkøb og drift. At skabe struktur, koordinere opgaver og få '
       'projekterne gennemført effektivt og med en høj kundetilfredshed er kernen i '
       'arbejdet, og stillingen giver stor indflydelse på både projekternes gennemførsel '
       'og udviklingen af langvarige kunderelationer. Løbende rapportering på '
       'projekternes fremdrift og resultater til ledelse og kunder har været min faste '
       'kadence siden 2003.')

    lp("Bliv en af 'Kemperne', skriver I, og det tiltaler mig: en hverdag fyldt "
       'med udfordringer, indflydelse og gode muligheder for at udvikle både faglige og '
       'personlige kompetencer, og en linje som tager ansvar i alt vi gør, og '
       'plads til forskellighed. Bosat i Måløv, en kort køretur fra kontoret i '
       'Albertslund, og vant til opgaver i bred geografisk placering med kørekort B '
       '(manuelt gear). Jeg tager gerne den fortrolige samtale med dig, Martin, før '
       'ansøgningen sendes formelt, og ellers ser jeg frem til de løbende samtaler.',
       after=44)

    m.para('Med venlig hilsen', after=0, line=236)
    m.para('Shahram Ajloo', after=0, line=236)

    # ------------------------------------------------------------- side 2-3
    m.page_break()
    m.resume_header(NAME, BANNER_RESUME, CONTACT, 'PROFIL')
    m.para('El-teknisk projektleder med maskinmester-baggrund og 20+ år med kritiske '
           'installationer og tekniske entrepriser. Commissioning, test og idriftsættelse '
           'ført helt frem til aflevering, el og UPS fra kW- til MW-siden, og '
           'datacenter-infrastruktur som en del af det nuværende arbejde. Elautoriseret '
           'maskinmester (LV/MV/HV), PRINCE2, AB18/ABT 18.', after=32)

    m.section('ERHVERVSERFARING')
    jobs = [
        ('CTO for AI-afdelingen og elautoriseret maskinmester (el-teknik og ventilation)',
         'Data Power Consultant ApS · København · 2024 – nu (fra nov. 2026 også ELOHVACs '
         'el-tekniske aktiviteter)',
         'AI-afdeling 4-10 personer · el-service og entreprise · 5 elektrikere + 3 lærlinge',
         [('Datacenter og leverancer', 'Datacenter-infrastruktur en del af det daglige '
           'arbejde, og leverancer styret fra tilbud og planlægning til idriftsættelse '
           'med 4-10 specialister på opgaverne. Microsoft Project som planlægnings-'
           'værktøj.')]),
        ('Ejer / teknisk direktør / elautoriseret maskinmester',
         'ELOHVAC ApS · København · maj 2023 – nov. 2026 (virksomheden lukket)',
         'Erhvervskunder · el, ventilation og klima · entreprise · fuldt P&L · serviceaftaler',
         [('Tilbud og kunder', 'Tilbudsberegning og kalkulation på egne projekter: effekt '
           'og belastningsberegninger, prisfastsættelse og aftaler. Kundeansvar og tætte '
           'relationer med serviceaftaler, UPS-opgaver og el-installationer, fulgt fra '
           'første møde til aflevering.'),
          ('Økonomi og styring', 'Projektøkonomi, ressourcestyring og tidsplaner styret '
           'i alle sager: bemanding af 5 elektrikere og 3 lærlinge, rapportering på '
           'fremdrift, og underentreprenører holdt på aftalen.')]),
        ('Senior commissioningeniør / projektleder, el-systemer',
         'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022 – jul. 2024',
         '37 CAPEX-projekter, DKK 2-10 mio. · 25 specialister · GMP/FDA/EMA',
         [('Commissioning og aflevering', '37 projekter gennem alle faser med commissioning, '
           'test og idriftsættelse (FAT/SAT, IQ/OQ/PQ). Kvalitetssikring dokumenteret, '
           'sikkerhedskrav overholdt, og nul kritiske fund ved aflevering. Stakeholder-'
           'arbejde på tværs af engineering, indkøb og drift.')]),
        ('Projekt- og værkstedsleder',
         'Ventek-Air · København · jan. 2022 – nov. 2022',
         '11 samtidige ventilationsprojekter · 14 mand · underleverandører',
         [('Entrepriser', '11 samtidige projekter med 14 mand og underentreprenører, '
           'koordinering på tværs af fag, og AB18/ABT 18 som aftalegrundlag. Effekt og '
           'belastningsberegninger i ventilationsentrepriserne, og økonomien fulgt pr. '
           'projekt.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker',
         'Biofos (Lynetten) · København · aug. 2017 – jan. 2022',
         '24/7-drift · kritiske anlæg · 10 medarbejdere · skiftehold',
         [('Kritisk drift og sikkerhed', 'Drift og vedligehold af kritiske anlæg døgnet '
           'rundt: pumper, HVAC, procesrør, SCADA og PLC. Risiko- og arbejdsmetode-'
           'beskrivelser som en del af hverdagen, APV og LOTO på tværs af skiftehold, og '
           'fejl fundet før de blev til stop.')]),
        ('Elektromekanisk tekniker / produktionsleder',
         'ARJ Engineering · Teheran · dec. 2003 – mar. 2010',
         '12 mekanikere og teknikere · maskinværksted · produktlinje',
         [('Grundlaget', 'Produktionsafdeling med 12 mekanikere og teknikere: vagtplan, '
           'materialer og mål. Risikostyring og kvalitetssikring i praksis, og '
           'rodårsagsanalyser der ændrede fejlhåndteringen.')]),
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
    m.bullet('El og entreprise', 'El-installation, tavler, styring, UPS, ABA/ABV, fiber, '
             'solcelleanlæg og nød- og panikbelysning. Opmåling, akkord og '
             'underentreprenører fra entreprisearbejdet. DS/HD 60364 og SB-vejledningerne '
             'som grundlag.', after=10)
    m.bullet('Projektstyring', 'PRINCE2, Microsoft Project, SAP ERP og Excel. AB18/ABT 18 '
             'i kontrakterne, RAMS på arbejdsstederne, og rapportering på fremdrift i en '
             'fast kadence.', after=10)
    m.bullet('Commissioning og kvalitet', 'Test og idriftsættelse fra FAT/SAT og IQ/OQ/PQ '
             'til afleveringsforretning og 1- og 5-års gennemgang. KS og dokumentation '
             'som en del af leverancen.', after=10)
    m.bullet('Kunder og relationer', 'Kundeansvar, tilbudsgivning og langsigtede '
             'relationer: serviceaftaler med KPI-mål, fornyelser på leveret kvalitet og '
             'kunder der ringer direkte.', after=10)
    m.bullet('Beregninger', 'Effekt og belastningsberegninger, energiberegninger og '
             'kalkulation. Kortslutningsberegninger og selektivitetsstudier i samspil med '
             'Engineering.', after=10)

    m.section('DE FØRSTE 90 DAGE')
    m.para('Planen følger projektkæden: tilbuddet, udførelsen, idriftsættelsen.',
           after=8)
    m.bullet('Dag 1-30 · Tilbuddet', 'Projekter, kunder og kalkationsrutiner lært at '
             'kende, med på tilbud og kundegennemgange. Mål: jeg kender porteføljen og '
             'de igangværende aftaler, og tilbudsberegningen er i gang.', after=10)
    m.bullet('Dag 31-60 · Udførelsen', 'Egne projekter ført med bemanding, økonomi og '
             'tidsplaner, RAMS på plads på arbejdsstederne. Mål: strukturen kører, og '
             'rapporteringen til ledelse og kunder er en fast kadence.', after=10)
    m.bullet('Dag 61-90 · Idriftsættelsen', 'Commissioning, test og idriftsættelse på de '
             'første afleveringer, kvalitetssikring dokumenteret, og kunderelationerne '
             'udviklet. Mål: afleveringer uden løse ender, og de næste projekter solgt.',
             after=10)

    m.section('SPROG, VÆRKTØJER OG PRAKTISK')
    m.para('Dansk (modersmål) · engelsk (professionelt) · persisk (modersmål). SAP ERP, '
           'Excel, Microsoft Project, SharePoint; PRINCE2. AB18/ABT 18. Kørekort '
           'kategori B (manuelt gear). Bosat i Måløv, kort køretur fra Albertslund, og '
           'vant til opgaver i bred geografisk placering. Tiltrædelse aftales.',
           after=32)

    # ------------------------------------------------------------- side 4
    m.page_break()
    m.models_table('El-faglig projektleder, datacentre · krav og dokumentation',
                   ('Krav i opslaget', 'Dokumenteret erfaring'),
                   [
        ('Projektledelse inden for datacentre, el-infrastruktur, kritiske installationer '
         'eller større tekniske byggeprojekter',
         'Projektledelse på alle fire områder: datacenter-infrastruktur i det nuværende '
         'arbejde, el-infrastruktur og entrepriser siden 2003, kritiske installationer i '
         'døgndrift (Biofos 2017-2022) og 37 tekniske byggeprojekter i procesanlæg (Novo '
         '2022-2024).'),
        ('Uddannet installatør eller maskinmester, eller en tilsvarende teknisk baggrund',
         'Maskinmester er den præcise titel: elautoriseret maskinmester (LV/MV/HV, 2023), '
         'B.Tech (EQF6) i teknologiledelse og maskinteknik (2017-2022) og elteknik på '
         'EQF6 (2000-2003).'),
        ('Bemyndiget elinstallationsansvarlig projektleder gennem alle projektfaser',
         'El-autorisationen LV/MV/HV (2023) er grundlaget for bemyndigelsen, og '
         'projektfaserne er gået igennem igen og igen: design, tilbud, planlægning, '
         'udførelse og idriftsættelse i 37 projekter (Novo 2022-2024), 11 entrepriser '
         '(Ventek 2022) og egen virksomhed (2023-2026).'),
        ('Effekt og belastningsberegninger; kortslutningsberegninger og selektivitetsstudier',
         'Effekt og belastningsberegninger lavet siden el-teknik-uddannelsen og i '
         'energiberegninger for ventilation (Ventek 2022). Kortslutningsberegninger og '
         'selektivitetsstudier løst i samspil med engineering-fag, som modellen også er '
         'her.'),
        ('Tilbudsberegning i Kalkia og tilbudsgivning på projekter og serviceopgaver',
         'Tilbudsberegning siden 2017: kalkulation og pris i SAP og Excel (Novo, ELOHVAC '
         '2023-2026), tilbudsgivning på projekter og serviceopgaver med egen kundekontakt. '
         'Kalkia kender jeg ikke fra praksis; kalkulationen bag er dagligdag for mig.'),
        ('Ansvar for egne projekter og udvikling af tætte kunderelationer',
         'Egne projekter og kunder i hele kæden: serviceaftaler med KPI\'er, tilbud og '
         'aftaler (ELOHVAC 2023-2026), kundeprojekter styret fra første møde (Ventek '
         '2022), og kunder der ringer direkte til mig.'),
        ('Ledelse og koordinering af medarbejdere og eksterne samarbejdspartnere',
         'Ledelse siden 2003: 5 elektrikere og 3 lærlinge (ELOHVAC 2023-2026), 14 mand og '
         'underentreprenører (Ventek 2022), 25 specialister på tværs af engineering, '
         'indkøb og drift (Novo 2022-2024), 10 på skiftehold (Biofos).'),
        ('Projektøkonomi, ressourcestyring og tidsplaner',
         'Økonomi og styring i hænderne: fuldt P&L som ejer (2023-2026), budget og '
         'tidsplaner i 37 projekter (Novo 2022-2024), ressourcestyring af 11 parallelt '
         'kørende entrepriser (Ventek 2022).'),
        ('Løbende rapportering på projekternes fremdrift og resultater til ledelse og kunder',
         'Rapporteringen kørt fast siden 2003: månedsrapportering med økonomi, fremdrift '
         'og risici til Novos ledelse (2022-2024), kunderapportering i serviceaftaler '
         '(ELOHVAC 2023-2026) og opfølgning til ejerforhold (2023-2026).'),
        ('Sikkerhedskrav, kvalitetssikring, test og idriftsættelse',
         'Alle fire i samme arbejde: sikkerhedskrav og RAMS på arbejdsstederne (Biofos '
         '2017-2022), kvalitetssikring og KS-dokumentation (ARJ, Novo), test og '
         'idriftsættelse fra FAT/SAT og IQ/OQ/PQ til aflevering (Novo 2022-2024).'),
        ('Overholdelse af Installationsbekendtgørelsen og relevante standarder',
         'Installationsbekendtgørelsen og DS/HD 60364 som dagligt grundlag i '
         'el-autorisationen (2023) og i el-installationsarbejde siden 2003, suppleret af '
         'SB-vejledningerne og GMP-standarder i pharma-regi (Novo 2022-2024).'),
        ('Risiko- og arbejdsmetodebeskrivelser (RAMS)',
         'Risiko- og arbejdsmetodebeskrivelser udarbejdet som en del af driften: APV, LOTO '
         'og sikkerhedsprocedurer på tværs af skiftehold (Biofos 2017-2022), '
         'arbejdsmetodebeskrivelser på byggepladser (Ventek 2022) og risikovurderinger i '
         'GMP-projekter (Novo 2022-2024).'),
        ('Anvendelse af CRM og Sharepoint',
         'SharePoint og Microsoft-platformen i daglig brug siden 2003. Kundeopfølgning, '
         'tilbud og aftaler kørt systematisk i strukturerede flows (serviceaftaler, '
         'ELOHVAC 2023-2026), og CRM som værktøj er samme disciplin i et nyt system.'),
        ('Stakeholder management',
         'Stakeholder-arbejdet i praksis: 25 specialister og flere fag på tværs i Novo '
         '(2022-2024), kunder, rådgivere og entreprenører i Ventek (2022) og i egen '
         'virksomhed (2023-2026). Interessentkort og klare aftaler frem for lange møder.'),
        ('Kundeansvar og opbygning af langsigtede kunderelationer',
         'Langsigtede relationer bygget over år: serviceaftaler der blev fornyet (ELOHVAC '
         '2023-2026), faste erhvervskunder med gentagne opgaver (Ventek, ELOHVAC), og '
         'kundekontakt fra tilbud til aflevering og 1- og 5-års gennemgang.'),
        ('Risikostyring i komplekse tekniske miljøer',
         'Risikostyring hvor fejl koster: 24/7-drift med beredskabsrutiner (Biofos '
         '2017-2022), risici fulgt i 37 GMP-projekter (Novo 2022-2024) og '
         'rodårsagsanalyser der ændrede praksis (ARJ 2003-2010).'),
        ('Struktureret og relationsskabende projektleder der bevarer overblikket i '
         'komplekse projekter',
         'Overblikket holdt i 11 parallelt kørende entrepriser (Ventek 2022) og 37 '
         'samtidige projekter (Novo 2022-2024). Struktur via PRINCE2 og tavlemøder, '
         'relationer via tid ude hos folkene og aftaler der holder.'),
        ('Kommunikerer professionelt på dansk og engelsk',
         'Dansk og engelsk professionelt i skrift og tale: dokumentation og møder på begge '
         'sprog (Novo 2022-2024), kundedialog (Ventek, ELOHVAC 2023-2026) og teknisk '
         'formidling siden 2010. Persisk som modersmål oveni.'),
        ('Fordele: Kalkia, Microsoft Project, BIM/Revit-miljøer, UPS, Canalis, effekt '
         'installationer, TIER begreberne fra Uptime Institute, Commissioning, AB18- eller '
         'totalentreprisekontrakter',
         'Fordelene fordelt: Microsoft Project som fast værktøj, TIER begreberne fra '
         'Uptime Institute fra datacenter-arbejdet, commissioning fra FAT/SAT og IQ/OQ/PQ '
         '(Novo 2022-2024), UPS og effektinstallationer fra kW- til MW-siden af el-faget, '
         'og AB18/ABT 18 i entreprisearbejdet. Kalkia, BIM/Revit-miljøer og Canalis står '
         'ikke på listen.'),
                   ], widths=(3400, 6946), compact=True)

    m.save(path, title='Shahram Ajloo — El-faglig projektleder, Kemp & Lauritzen')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_KempLauritzen_ElFagligProjektleder.docx')
    build(out)
    print(out)
