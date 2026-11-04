# -*- coding: utf-8 -*-
"""Arkil / Randstad — formand Silkeborg, reference 14507."""
import os
from master_design import MasterDoc
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Projektledelse | Mandskab, fremdrift og sikkerhed'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv (Ballerup Kommune)'

def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('4. november 2026')
    m.meta('Arkil · Anlægsafdelingen Silkeborg · via Kerem Özdemir, Randstad')
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, 'Ansøgning: Projektstyrende formand · ref. 14507', bold=True, color='1A1A1A')
    m.para('På en stor anlægsplads bliver dagens resultat afgjort af, om sjakket kan arbejde sikkert, og om bemanding, maskiner, materialer og næste aktivitet passer sammen. Formandens opgave er at være til stede, skabe fremdrift og tage fat i afklaringerne, før de bliver til ventetid eller usikre beslutninger.', after=80)
    m.para('Jeg vil begynde med at gennemgå entreprisegrundlag, tegninger, tidsplan og pladsens risici med projektlederen og de erfarne folk på pladsen. Derefter skal en kort fælles plan vise, hvad der skal ske, hvem der gør hvad, og hvilke leverancer eller beslutninger der kan spænde ben.', after=80)
    for label, body in [
        ('Sjak og sikkerhed', 'Aftale dagens opgaver og grænseflader med sjak og leverandører. Bruge korte tavlemøder, klare instruktioner og løbende sparring; følge op på APV, afspærring og pladsens sikkerhedsplan sammen med de ansvarlige, før arbejdet sættes i gang.'),
        ('Plan og fremdrift', 'Sammenholde bemanding, maskiner, materialer og adgang med næste uges arbejde. Registrere hindringer med ansvarlig og frist, og løfte konsekvenser for tid og økonomi til projektlederen, inden planen skrider.'),
        ('Bygherre og økonomi', 'Holde bygherredialog og byggemøder konkrete: fremdrift, åbne spørgsmål og næste aftale. Bidrage til tilbudsgivning og kalkulation ved at gennemgå tegningsmateriale, mængder og forudsætninger sammen med de fagligt ansvarlige.'),
        ('Jord og anlæg', 'Ved jordflytning, vejprojekter og eventuel bykloakering skal metoder, ledningsoplysninger, udgravning og maskinsikkerhed afklares med erfarne anlægsfolk og efter Arkils procedurer. Arbejdet må ikke starte på antagelser.')]: m.bullet(label, body, after=35)
    m.para('I den første uge vil jeg lære pladsen og sjakket at kende; inden dag 30 skabe et fælles overblik over planen og åbne risici; inden dag 60 følge op på de vigtigste hindringer; og inden dag 90 sammen med projektlederen justere den daglige opfølgning, så den faktisk hjælper pladsen.', after=80)
    m.para('Min baggrund er ledelse af tekniske entrepriser og anlægsprojekter, ikke dokumenteret formandsansvar for tunge jord- og vejentrepriser. Det er et væsentligt fagligt spring, som jeg gerne vil drøfte åbent med Randstad. Jeg bor i Måløv; tilstedeværelse i Midt- og Vestjylland, rejser og eventuel lokal base skal aftales, før et forløb kan planlægges.', after=80)
    m.meta('Med venlig hilsen', after=20)
    m.meta('Shahram Ajloo', after=0)

    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Teknisk projekt- og personaleleder med erfaring i at planlægge entrepriser, koordinere specialister og følge økonomi og fremdrift. Elautoriseret maskinmester med praktisk baggrund inden for el, mekanik og drift. Søger en projektstyrende rolle med ansvar for mennesker og leverancer; min dokumenterede entrepriseerfaring er teknisk frem for tung jord og vej.', after=80)
    m.section('LEDELSE OG PROJEKTER I PRAKSIS')
    for label, body in [
        ('Mandskab og samarbejde', 'ELOHVAC: daglig ledelse af fem elektrikere og tre lærlinge med opgavefordeling, 1:1, MUS og oplæring. Ventek-Air: ledede et team på 14 med 11 samtidige projekter.'),
        ('Fremdrift og kapacitet', 'Ventek-Air: planlagde ressourcer fra specifikation til aflevering. Daglige tavlemøder og flaskehalsanalyse understøttede bedre levering.'),
        ('Økonomi og bygherre', 'Novo Nordisk: fulgte fremdrift, økonomi, ressourcer og risici på 37 samtidige CAPEX-projekter til 2–10 mio. kr. pr. projekt; rapporterede til ledelse og bygherre.'),
        ('Tilbud og leverandører', 'ELOHVAC: tilbud, beregning, materialer og underentreprenører med fuldt P&L. Ventek-Air: udbud, aftalegrundlag, sikkerheds- og afleveringsdokumentation.'),
        ('Sikkerhed og digitale værktøjer', 'LOTO, APV og risikovurdering i ELOHVAC og Biofos. Egne Python/Claude API-værktøjer til tilbud, tidsplaner og kvalitet; dokumenteret produktivitetsløft over 40 % i ELOHVAC.')]: m.bullet(label, body, after=30)
    m.models_table('LEDELSESVÆRKTØJER — ANVENDT I PRAKSIS', ('Område', 'Metoder og erfaring'), [
        ('Mennesker', 'Situationsbestemt ledelse, 1:1 og struktureret oplæring hos ELOHVAC.'),
        ('Fremdrift', 'Daglige tavlemøder og flaskehalsanalyse hos Ventek-Air; planlægning af kapacitet.'),
        ('Sikkerhed', 'LOTO, APV og risikovurdering hos ELOHVAC og Biofos; opfølgning på nærved-hændelser.'),
        ('Forbedring', 'PDCA og A3 hos Novo; 5S og Standard Work i Biofos værksted og lager.')])
    m.section('UDVALGTE RESULTATER')
    for label, body in [('14 medarbejdere / 11 projekter', 'Kapacitetsstyring og daglig ledelse hos Ventek-Air.'), ('25 specialister / 37 projekter', 'Koordinering hos Novo Nordisk på tværs af engineering, indkøb og anlæg.'), ('40 % lavere energiomkostninger', 'Resultat af PDCA-program hos Novo Nordisk.')]: m.bullet(label, body, after=30)

    m.page_break()
    m.section('ERHVERVSERFARING')
    jobs = [
        ('Indehaver / teknisk direktør / elautoriseret maskinmester', 'ELOHVAC ApS · København · maj 2023–nu', '5 elektrikere og 3 lærlinge · fuldt P&L-ansvar', [
            ('Entrepriser og mennesker', 'Daglig planlægning, opgavefordeling og oplæring. Tilbud, materialer, underentreprenører, kvalitet og aflevering af el-, ventilations- og klimaanlæg.'),
            ('Digitalt overblik', 'Python/Claude API til tilbud, tidsplaner, KS og KPI; produktivitetsløft over 40 % i virksomheden.')]),
        ('Senior idriftsættelsesingeniør / projektleder, elsystem', 'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024', '37 samtidige CAPEX-projekter · 25 specialister · 2–10 mio. kr. pr. projekt', [
            ('Projektopfølgning', 'Koordinerede engineering, indkøb og anlæg; fulgte økonomi, fremdrift, risici og ressourcer og rapporterede til ledelse og bygherre.'),
            ('Test og aflevering', 'FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA uden kritiske fund ved aflevering. SAP ERP til økonomi og aktiver.')]),
        ('Projekt- og værkstedsleder', 'Ventek-Air · København · jan. 2022–nov. 2022', '14 medarbejdere · 11 samtidige anlægsprojekter', [
            ('Plan og fremdrift', 'Kapacitetsstyring fra specifikation til formel aflevering; udbud og tilbud, underentreprenører og aftalegrundlag. Daglige tavlemøder og flaskehalsanalyse.')]),
        ('Vedligeholdelses- og driftsleder / værkstedstekniker', 'Biofos, Lynetten · København · aug. 2017–jan. 2022', '24/7-drift · pumper, HVAC, højspændingstavler og SCADA', [
            ('Drift og sikkerhed', 'Forebyggende vedligehold, akut fejlfinding og reservedelsflow; 5S, Standard Work og PDCA samt LOTO og risikovurdering.')]),
        ('Elektromekaniker / produktionsteamleder', 'ARJ Engineering · Teheran · dec. 2003–mar. 2010', '12 mekanikere og teknikere', [
            ('Team og værksted', 'Vagtplanlægning, materialestyring og målopfølgning; fejldiagnose og reparation af industrielt el- og mekanisk udstyr.')])]
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope=scope)
        m.doc.paragraphs[-1].runs[0].text = 'Omfang: '
        for label, body in bullets: m.bullet(label, body, after=25)
    m.section('UDDANNELSE OG AUTORISATION')
    m.edu('B.Tech, Technology Management & Mechanical Engineering — maskinmesterretningen', 'Maskinmesterskolen København · 2017–2022 · EQF 6')
    m.edu('El- og maskinteknisk design, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Elautoriseret maskinmester (LV/MV/HV)', 'Sikkerhedsstyrelsen · maj 2023')
    m.edu('Køleteknik og klimaanlæg · STCW-sikkerhed og maskinrumsvagt', 'Mercantec 2021 · Søfartsstyrelsen 2021–2023')
    m.section('SPROG OG PRAKTISK')
    m.para('Dansk og persisk/farsi: modersmål · Engelsk: professionelt · Kørekort B · Bopæl i Måløv. Tilstedeværelse, rejser, eventuel lokal base og overgang fra ELOHVAC aftales.', after=70)
    m.section('REFERENCER')
    m.para('Tidligere ledere hos Novo Nordisk og Biofos oplyses efter aftale.', after=70)

    m.page_break()
    m.models_table('FØRSTE 90 DAGE — FORSLAG TIL OPSTART', ('Tid', 'Handlinger og leverancer'), [
        ('Uge 1', 'Forudsat aftale om fremmøde: møde projektleder, sjak og sikkerhedsansvarlige. Gennemgå kontrakt, tegninger, tidsplan, pladsforhold og godkendte sikkerhedsprocedurer; afklare beslutningsrum.'),
        ('Inden dag 30', 'Sammen med de erfarne anlægsfolk danne overblik over bemanding, maskiner, leverancer, økonomi og kommende aktiviteter. Aftale daglig koordinering og opfølgning på hindringer og bygherrebeslutninger.'),
        ('Inden dag 60', 'Følge op på fremdrift og konsekvenser for tid og økonomi med projektlederen. Gennemgå erfaringer fra pladsen, sikkerhed og leverancer med sjakket; justere planen efter aftale.'),
        ('Inden dag 90', 'Evaluere samarbejde, opgavefordeling og den daglige plan med holdet og projektlederen. Beskrive åbne risici, læringsbehov og forslag, som kan styrke næste fase.')])
    m.section('SAMARBEJDE PÅ PLADSEN')
    for label, body in [
        ('Sjak og leverandører', 'Aftal klare opgaver og forventninger ved dagens start; lyt til erfaringerne på pladsen og følg op, når mandskab, maskiner eller leverancer ændrer sig.'),
        ('Projektleder og bygherre', 'Hold byggemøder og bygherredialog konkrete. Gør konsekvenser for tid og økonomi synlige og få beslutninger og ansvar bekræftet.'),
        ('Sikkerhed først', 'Stands og afklar usikre forhold med de kompetente ansvarlige. Jordarbejde, eksisterende ledninger, udgravninger og maskiner kræver instruktion og de gældende sikkerhedsforanstaltninger.'),
        ('Ledelse og læring', 'Brug situationsbestemt ledelse, 1:1 og tavlemøder til at udvikle samarbejdet. Efter en afvigelse kan PDCA og årsagsanalyse hjælpe med at finde en holdbar løsning.')]: m.bullet(label, body, after=35)
    m.section('TEKNISK UDGANGSPUNKT OG DIGITALE VÆRKTØJER')
    m.para('Min dokumenterede erfaring er el- og mekaniske entrepriser, teknisk projektstyring og spildevandsdrift. Tidligere ansvar som formand for store jordflytnings-, vej- eller hovedentrepriser er ikke dokumenteret. Den særlige faglighed og eventuelle uddannelseskrav skal afklares med Arkil, og de erfarne anlægsfolk inddrages i alle faglige beslutninger.', after=80)
    m.para('Jeg er aktiv professionel AI-/Claude-koder og bygger Python/Claude-værktøjer til beregning, planlægning, kvalitet og investeringsmodeller med NPV, IRR og scenarier. Anvendelse hos Arkil kræver godkendte data og systemer samt menneskelig kontrol; et værktøj erstatter ikke pladsens faglige eller sikkerhedsmæssige vurdering.', after=80)
    m.section('FRA TILBUD TIL FREMDRIFT')
    m.para('Sammen med projektlederen vil jeg gennemgå tilbudsforudsætninger, tegninger og aftalte leverancer før opstart. Under udførelsen skal ændringer og forhold på pladsen følges op mod planen og dokumenteres efter virksomhedens procedurer. Det skaber et bedre grundlag for aftaler med bygherre og for en aflevering, hvor åbne punkter har en ansvarlig.', after=80)
    m.section('FAGLIGE FOKUSOMRÅDER')
    m.para('Projektstyrende formand · anlægsprojekter · jordflytning · vejprojekter · hovedentrepriser · bemanding · sjak · sikkerhed · bygherredialog · byggemøder · tilbudsgivning · kalkulation · fremdrift · leverandører', after=70)
    return m.save(path, title='Ansøgning og CV — Formand, Arkil Silkeborg, ref. 14507', subject='Projektledelse og sikker fremdrift', keywords='formand, anlægsprojekter, projektstyring, sikkerhed')

if __name__ == '__main__':
    print(build(os.path.join(ROOT, 'Shahram_Ajloo_Arkil_FormandSilkeborg.docx')))
