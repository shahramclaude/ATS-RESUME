# -*- coding: utf-8 -*-
"""Region Hovedstaden — Fagleder for projekter, Rigshospitalet, job 271227."""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Projekt- og personaleledelse · Byggeri, drift og tekniske anlæg'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta('16. november 2026')
    m.meta('Region Hovedstaden · Center for Ejendomme · Drift og Byg · Rigshospitalet · Job 271227')
    p = m._p(spacing_after=72, line=260, justify=False)
    m._run(p, 'Ansøgning: Fagleder for projekter', bold=True, color='1A1A1A')

    def para(text, after=48):
        return m.para(text, after=after, line=235)

    # Side 1 — opgaven og den ledelsesrytme, der skal få den til at lykkes.
    para('Et hospital kan ikke sætte driften på pause, mens der bygges om. **Den daglige drift fortsætter**, '
         'mens patientforløb, kliniske funktioner, teknisk forsyning og adgang skal fungere samtidig med, at '
         'projektet flytter vægge, føringsveje eller tekniske installationer. Derfor skal projektteamet kunne '
         'se både den enkelte byggeplads og den samlede portefølje: hvad der er kritisk nu, hvem der skal træffe '
         'næste beslutning, og hvor en forsinkelse får følger for hospitalet.', after=46)
    para('Som fagleder skal man skabe de rammer, der gør projektlederne i stand til at lykkes — uden at tage '
         'deres faglige ansvar fra dem. Jeg vil etablere en fast, let møderytme med projektlederne og '
         'fagkoordinatoren: gennemgå den samlede **projektportefølje** og de få sager, hvor økonomi, tidsplan, '
         'risiko eller driftsgrænse kræver opmærksomhed; aftale ejer og dato på næste handling; og løfte '
         'beslutninger til ejendomschefen eller viceejendomschefen med alternativer og konsekvenser, ikke blot '
         'en statusfarve. Projektlederne får et fælles, faktabaseret grundlag for at aftale prioriteringer.', after=46)
    para('En porteføljeoversigt skal være et arbejdsredskab, ikke endnu et rapporteringslag. For hvert projekt '
         'bør den vise formål, fase, økonomi, milepæle, risici, afhængigheder, ansvarlig projektleder og '
         'påvirkning af den daglige drift. Fagkoordinatoren kan hjælpe med at samle og kvalitetssikre data; '
         'faglederen bruger dem til at prioritere kapacitet, stille spørgsmål og få afklaret konflikter mellem '
         'projekter, drift og hospitalets øvrige interessenter. Det er også det datagrundlag, der gør det muligt '
         'at **skabe fremdrift** på tværs uden at miste blikket for lokale driftsbehov.', after=46)
    para('Før en sag går videre, skal projektleder, teknisk drift, brugerrepræsentant, rådgiver og entreprenør '
         'have samme billede af scope, beslutningsgrundlag, adgang, driftsafbrydelser, sikkerhed, risici og '
         'afleveringskrav. **Hospitalets interessenter** skal vide, hvem beslutter hvad, og hvornår en ændring '
         'skal løftes. I en hospitalsbygning er idriftsættelse og overdragelse ikke den sidste administrative '
         'øvelse; det er dér, det skal kunne dokumenteres, at installationen kan indgå i en fungerende drift. '
         'Fælles metoder skal give den nødvendige ensartethed, men kunne tilpasses projektets størrelse og '
         'kritikalitet.', after=46)
    para('Teamledelse skal kunne mærkes i hverdagen: **tydelige forventninger**, **faglig sparring** og '
         '**løbende opfølgning**, men også plads til at projektlederne selv vælger løsningen inden for aftalte '
         'rammer. Én-til-én-samtaler og projektgennemgange skal afdække både fremdrift og belastning. Når '
         'interesser støder sammen, skal uenigheden frem tidligt, så de rette fagligheder kan **samle forskellige '
         'perspektiver**, sammenligne muligheder og træffe en begrundet beslutning, før den bliver til en '
         'forsinkelse eller en driftsrisiko. Det handler om at udvikle **kompetencer, trivsel og faglig sparring** '
         'som en del af leverancen — med **tillid, åbenhed, helhedssyn og professionalisme**.', after=46)
    para('Center for Ejendomme vil være **den foretrukne samarbejdspartner inden for ejendomsdrift, byggeri '
         'og logistik** og levere **værdiskabende og bæredygtige løsninger i regionen**. På Rigshospitalet '
         'begynder det med **trygge rammer og værdi** for dem, der bruger bygningerne — mens arbejdet står på, '
         'ikke først ved projektets afslutning. En fælles porteføljerytme, klare beslutningsveje og faglig '
         'udvikling af projektlederne er den måde, jeg vil hjælpe Drift og Byg med at indfri det.', after=34)
    m.meta('Med venlig hilsen', after=8)
    m.meta('Shahram Ajloo', after=0)

    # Side 2 — CV, positionering og nyeste lederansvar.
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFIL')
    m.para('Projekt- og personaleleder med erfaring fra bygge- og renoveringsprojekter, tekniske anlæg, '
           'idriftsættelse og drift. Har ledet egne medarbejdere, projektteams og **projektledere** samt '
           'tværfaglige specialister; arbejdet med projektøkonomi, tidsplaner, risici, udbud, aftalegrundlag, '
           'underentreprenører og aflevering. PRINCE2-certificeret projektleder; Lean og Six Sigma anvendt i '
           'praksis. Skaber overblik med klare roller, regelmæssig opfølgning og beslutninger tæt på den '
           'faglighed, der skal føre arbejdet sikkert i mål.', after=44)
    m.section('PROJEKTER OG LEDELSE I TAL')
    m.para('37 samtidige CAPEX-projekter · 25 tværfaglige specialister · 11 parallelle anlægsprojekter · '
           '14-mands projektteam · 5 elektrikere og 3 lærlinge · 12 teknikere · DKK 2–10 mio. pr. projekt · '
           'nul kritiske afvigelser ved GMP-aflevering · 40 % lavere energiomkostninger gennem PDCA.', after=42)
    m.section('ERHVERVSERFARING')
    m.job('Ejer / teknisk direktør / elautoriseret maskinmester',
          'ELOHVAC ApS · København · maj 2023–nu',
          scope='5 elektrikere og 3 lærlinge · fuldt P&L-ansvar',)
    for a, b in [
        ('Projekt- og entrepriseansvar', 'Tilbud og beregning, planlægning, økonomi, materialer, underentreprenører, kvalitetssikring og aflevering af tekniske installationer for erhvervskunder.'),
        ('Personaleledelse', 'Daglig prioritering, 1:1 og MUS, arbejdsmiljøopfølgning og struktureret oplæring af elektrikere og lærlinge på skiftende byggepladser.'),
        ('Resultat og forbedring', 'Python- og Claude API-værktøjer til beregning, tidsplaner, KS og KPI; dokumenteret produktivitetsløft over 40 %.')]:
        m.bullet(a, b, after=17)

    m.job('Medejer og CTO / teknisk ansvarlig for AI-afdelingen',
          'Data Power Consultant ApS · København · 2024–nov. 2026 · sideløbende med ELOHVAC',
          scope='AI-afdeling på 4–10 personer · selskabet ophørt november 2026')
    for a, b in [
        ('Tekniske leverancer', 'Ledte kundeløsninger fra krav og arkitektur gennem integration og idriftsættelse til dokumentation og overdragelse til drift.'),
        ('Ledelse og matrix', 'Prioriterede leverancer på tværs af to sideløbende virksomheder; brugte LLM-API’er og AI-agenter i tekniske/industrielle løsninger, designarbejde og ledelsesrapportering.')]:
        m.bullet(a, b, after=17)

    # Side 3 — portefølje, projektledelse, drift og uddannelse.
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'PROFESSIONEL ERFARING — FORTSAT')
    m.job('Senior idriftsættelsesingeniør / projektleder, elsystem',
          'Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024',
          scope='37 samtidige CAPEX-projekter · 25 specialister · DKK 2–10 mio. pr. projekt')
    for a, b in [
        ('Portefølje og projektopfølgning', 'Fulgte økonomi, tidsplan, risiko og ressourcer på tværs af engineering, indkøb og anlæg; rapporterede månedligt til ledelse og bygherre via SAP ERP.'),
        ('Kvalitet og aflevering', 'Koordinerede commissioning og kvalifikation af tavler, styringer, UPS, brand- og sikkerhedssystemer under GMP. FAT/SAT og IQ/OQ/PQ; nul kritiske afvigelser ved aflevering.'),
        ('Forbedringsresultat', 'Ledte et struktureret PDCA-forløb, der reducerede energiomkostninger med 40 %; brugte A3, 5 Why og Ishikawa ved fejlfinding.')]:
        m.bullet(a, b, after=16)

    m.job('Projekt- og værkstedsleder, ventilation og HVAC',
          'Ventek-Air · København · jan. 2022–nov. 2022',
          scope='11 samtidige anlægsprojekter · 14 personer · DKK 2–10 mio. pr. projekt')
    for a, b in [
        ('Udbud og kontraktgrundlag', 'Udarbejdede tilbud og koordinerede udbud, underentreprenører, aftalegrundlag, sikkerhedsdokumentation og afleveringspakker.'),
        ('Fremdrift og kapacitet', 'Styrede bemanding og fremdrift fra specifikation til formel aflevering; brugte daglige tavlemøder og flaskehalsanalyse til at fordele ressourcer og løse grænseflader.')]:
        m.bullet(a, b, after=16)

    m.job('Vedligeholdelses- og driftsleder / værkstedstekniker',
          'Biofos, Lynetten · København · aug. 2017–jan. 2022', scope='24/7 kritisk forsyningsdrift')
    m.bullet('Teknisk drift og samarbejde', 'Planlagde forebyggende vedligehold og fejlretning på pumper, HVAC, højspændingstavler og SCADA; arbejdede med LOTO, risikovurderinger, APV og nærved-hændelser.', after=16)

    m.job('Elektromekaniker / produktionsteamleder',
          'ARJ Engineering · Teheran · dec. 2003–mar. 2010', scope='12 mekanikere og teknikere')
    m.bullet('Holdledelse og leverancer', 'Planlagde skift og materialer, fordelte opgaver og fulgte fejlretning og korrigerende handlinger i et industrielt værksted.', after=20)

    m.section('UDDANNELSE, AUTORISATION OG METODER')
    m.edu('B.Tech, Technology Management & Mechanical Engineering', 'Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · EQF 6')
    m.edu('El- og maskinteknisk design, elteknik', 'Tehran Technical University · 2000–2003 · EQF 6')
    m.edu('Elautoriseret maskinmester, LV/MV/HV', 'Sikkerhedsstyrelsen · 2023')
    m.edu('PRINCE2-certificeret projektleder', 'AXELOS / PeopleCert')
    m.edu('Lean og Six Sigma', 'Anvendt i praksis; ikke certificeret')
    m.para('Dansk og persisk/farsi: modersmål · Engelsk: professionelt · Kørekort B · Måløv, Danmark.', after=25)

    # Side 4 — komplet kravkortlægning og praktisk opstart.
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, 'KRAV OG LEDELSESPRAKSIS')
    m.models_table('FAGLEDERENS OPGAVE — OG DEN PRAKSIS, JEG BRINGER', ('Krav / ansvar i rollen', 'Dokumenteret tilgang og erfaring'), [
        ('Lede og udvikle projektteamet', 'Ledte 5 elektrikere og 3 lærlinge med 1:1, MUS og løbende opfølgning; desuden 14 medarbejdere og tværfaglig koordinering af 25 specialister. Arbejdede med teamets kompetencer, trivsel og faglig sparring.'),
        ('Kvalitet, fremdrift, økonomi, tid og risiko', 'Fulgte økonomi, tidsplan, risiko og ressourcer på 37 CAPEX-projekter; rapporterede månedligt og afleverede uden kritiske afvigelser.'),
        ('Prioritering og ressourcefordeling', 'Fordelte kapacitet på 11 samtidige anlæg med et 14-personers team; brugte tavlemøder og flaskehalsanalyse til at afstemme bemanding og milepæle.'),
        ('Samarbejde på tværs af projekt, drift og interessenter', 'Koordinerede engineering, indkøb, anlæg, kunder og underentreprenører; Biofos var kritisk 24/7-forsyning, hvor driftsvinduer og sikkerhed skulle hænge sammen.'),
        ('Fælles metoder, arbejdsgange og kvalitet', 'Brugte PRINCE2, Lean/Six Sigma, PDCA og A3; standardiseret KS og aflevering. PDCA sænkede energiomkostninger 40 %.'),
        ('Porteføljeoverblik med fagkoordinator', 'Saml fase, økonomi, milepæle, risici, afhængigheder og kapacitet i én status; aftal datagrundlag og kadence med fagkoordinatoren.'),
        ('Sparring med ejendomsledelsen', 'Beslutningsoplæg viser afvigelse, konsekvens, valg, anbefaling, ejer og dato; 37-projektstatus blev rapporteret månedligt via SAP.'),
        ('Byggeprojekter fra beslutning til aflevering', 'Ledte 11 tekniske anlægsprojekter fra tilbud og plan til commissioning og aflevering; fulgte også 37 CAPEX-projekter på tid, økonomi og kvalitet.'),
        ('Resultater gennem andre; konstruktiv faglig sparring', 'Ledte teams på 5–25 personer og oplærte lærlinge; afklarede ansvar, stillede faglige spørgsmål og fulgte aftaler til afslutning.'),
        ('Offentlig bygherrefunktion, udbud, kontrakter og projektopfølgning', 'Tilbud, udbud, aftalegrundlag og opfølgning er en fast del af projekterne; jeg har styret underentreprenører, økonomi, ændringer og formel aflevering.'),
        ('Retning, ansvar og faglig autonomi', 'Aftaler mål og mandat, så specialister kan handle selvstændigt; 1:1 og MUS bruges til faglig sparring, opfølgning og udviklingsmål.'),
        ('Modstridende interesser og hospitalets drift', 'Synliggør adgang, forsyningspåvirkning, sikkerhed og milepæle tidligt; samler drift, brugere, rådgivere og entreprenører om løsninger og beredskab.'),
        ('Prioritering og ressourcefordeling på tværs af projekterne', 'Fordelte bemanding på 11 samtidige anlæg og 14 personer; ugentlige tavlemøder fangede flaskehalse og gjorde det muligt at flytte kapacitet før milepæle blev påvirket.'),
        ('Porteføljeoverblik med fagkoordinatoren og koordineret prioritering', 'Sammen med fagkoordinatoren samles 37 projekters fase, økonomi, tidsplan og risiko; projektlederne bekræfter afhængigheder og beslutninger, så prioritering bygger på samme status.'),
        ('Sparringspartner for ejendomschefen og viceejendomschefen', 'Månedlig rapportering på 37 projekter viste økonomi, fremdrift og risici; ledelsen fik tydelige valg, konsekvenser, ansvarlig og næste beslutningsdato.'),
        ('Byggeri og renovering under fortsat hospitalsdrift', 'Ved byggeri og renovering planlægges adgang, tekniske installationer, sikkerhed og aflevering med driften; hvert hospitalindgreb knyttes til driftsvindue, beredskab og dokumenteret overdragelse.')
    ])
    m.section('DE FØRSTE 90 DAGE — PORTFØLJE, MANDAT, FÆLLES RYTME')
    m.para('**Dag 1–30:** Mød projektledere, fagkoordinator, teknisk drift og hospitalets interessenter; '
           'aftal mandat, beslutningsveje og fælles status. **Dag 31–60:** Start porteføljerytme for økonomi, '
           'milepæle, risiko, kapacitet og beslutninger; aftal 1:1 med projektlederne og vælg fælles '
           'arbejdsgange. **Dag 61–90:** Afstem prioritering med ejendomsledelsen, luk tværgående beslutninger '
           'og aftal teamets kompetence-, trivsels- og afleveringsopfølgning.', after=16, line=220)
    return m.save(path, title='Ansøgning og CV — Fagleder for projekter, Rigshospitalet',
                  subject='Bygge- og renoveringsportefølje · Teamledelse · Drift og Byg',
                  keywords='projektledelse, byggeprojekter, personaleledelse, portefølje, Region Hovedstaden')


if __name__ == '__main__':
    out = os.path.join(ROOT, 'Shahram_Ajloo_RegionH_FaglederProjekter_Rigshospitalet.docx')
    print(build(out))
