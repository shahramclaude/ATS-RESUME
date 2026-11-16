"""ELCON Junior Planlægger: dansk ansøgning og CV."""
import os
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

class LinearDoc:
    """Enkel ATS-læsbar Word-fil: afsnit i læserækkefølge, ingen tabeller."""
    def __init__(self, *_args, **_kwargs):
        self.doc = Document()
        sec = self.doc.sections[0]
        sec.top_margin = sec.bottom_margin = Cm(1.6)
        sec.left_margin = sec.right_margin = Cm(2)
        style = self.doc.styles['Normal']
        style.font.name = 'Calibri'
        style.font.size = Pt(10)
        lang = OxmlElement('w:lang'); lang.set(qn('w:val'), 'da-DK')
        style.element.get_or_add_rPr().append(lang)
    def _p(self, spacing_after=70, line=250, justify=False):
        p=self.doc.add_paragraph()
        p.paragraph_format.space_after=Pt(spacing_after/20)
        p.paragraph_format.line_spacing=Pt(line/20)
        return p
    def _run(self,p,text,bold=False,color=None,size=10):
        r=p.add_run(text); r.bold=bold; r.font.name='Calibri'; r.font.size=Pt(size)
        if color:r.font.color.rgb=RGBColor.from_string(color)
        return r
    def header_banner(self,name,title,contact):
        self._run(self._p(30,340),name,True,'173B57',18)
        self._run(self._p(25,260),title,True,'173B57',11)
        self._run(self._p(90,240),contact,size=9.5)
    def resume_header(self,name,title,contact,first_section):
        self.header_banner(name,title,contact);self.section(first_section)
    def meta(self,text,after=60):self._run(self._p(after,240),text,size=9.5)
    def para(self,text,after=70):self._run(self._p(after,255),text)
    def section(self,text):
        p=self._p(50,260);p.paragraph_format.space_before=Pt(4);p.paragraph_format.keep_with_next=True
        self._run(p,text,True,'173B57',10.5)
    def bullet(self,a,b,after=15):
        p=self._p(after,250);p.paragraph_format.left_indent=Cm(.25);p.paragraph_format.first_line_indent=Cm(-.25)
        self._run(p,'• '+a+': ',True);self._run(p,b)
    def job(self,title,meta,scope=None):
        p=self._p(15,250);p.paragraph_format.keep_with_next=True;self._run(p,title,True,'173B57')
        p=self._p(15,235);p.paragraph_format.keep_with_next=True;self._run(p,meta,False,None,9.5)
        if scope:
            p=self._p(30,235);p.paragraph_format.keep_with_next=True;self._run(p,scope,False,None,9.5)
    def edu(self,a,b):
        p=self._p(15,240);self._run(p,a+' — ',True);self._run(p,b)
    def page_break(self):self.doc.add_page_break()
    def save(self,path,**meta):
        self.doc.core_properties.title=meta.get('title','')
        self.doc.core_properties.subject=meta.get('subject','')
        self.doc.core_properties.keywords=meta.get('keywords','')
        self.doc.save(path);return path
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME='SHAHRAM AJLOO'
TITLE='Kundeservice | Planlægning | El-teknisk forståelse'
CONTACT='+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'

def build(path):
 m=LinearDoc()
 m.header_banner(NAME,TITLE,CONTACT);m.meta('ELCON · Kundecenter Glostrup · Att.: teamleder Therese Ring · Rekvisition 679')
 p=m._p(spacing_after=90,line=260,justify=False);m._run(p,'Junior Planlægger — en tryg vej fra bestilling til installation',bold=True,color='1A1A1A')
 for text in [
 'En ladestander bliver først en god kundeoplevelse, når bestillingen bliver til en aftale, kunden forstår, og en servicemontør kan gennemføre. ELCON beskriver sit landsdækkende kundecenter som forbindelsen mellem kunden og de lokale afdelinger. For juniorplanlæggeren er opgaven at holde det led sammen: besvare henvendelser, booke installationer og sørge for, at informationen følger opgaven.',
 'Fra ordre til booking: Kontrollér ordren og kontakt kunden på en imødekommende måde. Afklar kontaktoplysninger, adresse og de oplysninger om installationen, som ELCONs arbejdsgang kræver. Registrér det væsentlige i kundecentrets IT-systemer, og gør usikkerheder synlige for en kollega eller teknisk specialist. Kunden skal have en klar forklaring på næste skridt, ikke et teknisk svar eller en tidsaftale, der endnu ikke kan bekræftes.',
 'Fra booking til montør: Sammenhold kundens muligheder med ledig kapacitet og relevant afdeling efter teamets planlægningsregler. Bekræft tid og aftalte forudsætninger, og sørg for, at montøren kan se de nødvendige oplysninger. Hvis en aftale ændres, skal både kunden og montøren informeres, sagen opdateres, og en ny ansvarlig opfølgning aftales. Ved spørgsmål om selve ladeproduktet frem for installationen skal kunden hjælpes til den rette kontakt efter gældende procedure.',
 'Når det er travlt: Skeln mellem opgaver, der påvirker en nært forestående montøraftale, og spørgsmål, der kan få en aftalt tilbagemelding senere. En kort status med næste handling og ansvarlig hjælper kollegerne med at tage over og håndtere kundehenvendelser effektivt. Videndeling om tilbagevendende spørgsmål gør svarene mere ensartede på dansk og engelsk. Et team skal have plads til at spørge om hjælp og hjælpe andre, når belastningen skifter.',
 'ELCONs beskrivelse af digitale ordreprocesser viser, hvorfor kvaliteten af registreringen er vigtig i et landsdækkende flow: den næste kollega skal kunne handle på det, kunden allerede har fortalt. Målet er ikke flest mulige løfter, men aftaler, der kan holdes, og sager, der bliver fulgt til dørs — med kunden informeret hele vejen.'
 ]:m.para(text,after=90)
 m.meta('Med venlig hilsen',after=10);m.meta('Shahram Ajloo',after=0)
 m.page_break();m.resume_header(NAME,TITLE,CONTACT,'PROFIL')
 m.para('Elautoriseret maskinmester med erfaring i kundekontakt, planlægning af tekniske opgaver og koordinering af medarbejdere. Har fulgt installationer fra kundens behov til aflevering og er vant til at holde styr på aftaler, ressourcer og dokumentation.',after=70)
 m.section('KOMPETENCER — KUNDE, PLAN OG TEKNIK')
 for a,b in [
 ('Kunder og service','ELOHVAC: erhvervskundedialog, tilbud, serviceaftaler og koordinering fra opgave til aflevering. Klare aftaler, opfølgning, kvalitetssikring og afleveringsdokumentation.'),
 ('Planlægning og fremdrift','Daglig koordinering af 5 elektrikere og 3 lærlinge hos ELOHVAC; kapacitetsstyring af 11 samtidige projekter hos Ventek-Air. Materialer, underentreprenører og ressourcer på tværs.'),
 ('El-teknik og drift','Installation, tavler, styring og fejlfinding på el-, ventilations- og klimaanlæg. Biofos: pumper, HVAC, højspændingstavler og SCADA i døgnbemandet drift.'),
 ('Økonomi og opmåling','Fuldt P&L-ansvar, tilbud og beregning. Akkordbreve, opmåling, tildeling til sjak samt regulering og opgørelse af mer- og mindrearbejde.'),
 ('Digitale værktøjer','MS Office, Excel/Power Query, SAP ERP, Python og Claude API. Aktiv AI-/Claude-koder med værktøjer til planlægning, KS og KPI; investeringsmodeller med NPV, IRR og scenarier.'),
 ('Ledelse og forbedringer','PRINCE2-certificeret; tavlemøder, 1:1 og situationsbestemt ledelse. PDCA, A3, 5S, Standard Work, 5xHvorfor og flaskehalsanalyse anvendt i praksis; ikke Lean- eller Six Sigma-certificeret.')]:m.bullet(a,b,after=25)
 m.section('RESULTATER OG PRAKTISK INFORMATION')
 m.para('Over 40 % produktivitetsløft med AI-værktøjer hos ELOHVAC · 40 % lavere energiomkostninger via PDCA hos Novo Nordisk · Ingen kritiske afvigelser ved Novo-afleveringer. Dansk og persisk/farsi: modersmål; engelsk: professionelt. Måløv · Kørekort B · Tiltrædelse og arbejdstid aftales.',after=50)
 m.para('Erfaringen med kundedialog og el-teknisk planlægning er fra service- og projektarbejde; specifik callcenter- eller ladestandererfaring fremgår ikke af den dokumenterede historik.',after=40)
 m.page_break();m.section('ERHVERVSERFARING')
 jobs=[
 ('Indehaver / teknisk direktør / elautoriseret maskinmester','ELOHVAC ApS · København · maj 2023–nu','5 elektrikere og 3 lærlinge · fuldt P&L-ansvar',[
 ('Kundeaftaler og levering','Tilbud, beregning og kundedialog; planlægning af medarbejdere, materialer og underentreprenører, kvalitetssikring og dokumenteret aflevering af el-, ventilations- og klimaanlæg.'),
 ('Teknisk service','Installation, tavler, styring, fejlfinding og forebyggende vedligehold fra akutte udkald til afsluttet anlæg. Serviceaftaler fulgt på responstid, kvalitet og leveringsevne.'),
 ('Økonomi og personale','Fuld P&L, akkordbreve og opmåling; tildeling til sjak og opgørelse af mer- og mindrearbejde. 1:1, MUS, lærlingeoplæring, LOTO og risikovurdering.'),
 ('Digitale forbedringer','Python/Claude API til tilbudsberegning, tidsplaner, KS-tjeklister og KPI-dashboards; dokumenteret produktivitetsløft over 40 %.')]),
 ('Medejer og CTO / teknisk ansvarlig for AI-afdelingen','Data Power Consultant ApS · København · 2024–2026 · sideløbende med ELOHVAC','4–10 personer',[
 ('Fra behov til overdragelse','Kravafdækning, arkitektur og integration af tekniske og industrielle applikationer; idriftsættelse, dokumentation og overdragelse til kundens drift.'),
 ('AI og beslutningsstøtte','Ledte AI-/AI coding-afdelingen; LLM-API’er, AI-agenter og kodegenerering med review og test. Anvendte AI til rapportering, KPI-analyse og beslutningsoplæg.'),
 ('Planlægning på tværs','Prioriterede opgaver i to sideløbende virksomheder med fælles plan og skriftlige aftaler.')]),
 ('Senior idriftsættelsesingeniør / projektleder, elsystem','Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024','37 samtidige CAPEX-projekter · 25 specialister · 2–10 mio. kr. pr. projekt',[
 ('Styring og kommunikation','Fremdrift, økonomi, risici og ressourcer på tværs af engineering, indkøb og anlæg; månedlig rapportering til ledelse og bygherre og SAP ERP til aktiver og omkostninger.'),
 ('Teknik og kvalitet','Tavler og styring, UPS, nød- og panikbelysning samt ABA/ABV og PDS. FAT/SAT og IQ/OQ/PQ under GMP; ingen kritiske afvigelser ved aflevering.'),
 ('Energi og analyse','PDCA-program reducerede energiomkostninger med 40 %. A3, 5xHvorfor og Ishikawa til fejlfinding og forbedring.')]),
 ('Projekt- og værkstedsleder','Ventek-Air · København · jan. 2022–nov. 2022','14 medarbejdere · 11 samtidige projekter · 2–10 mio. kr. pr. projekt',[
 ('Plan og aflevering','Kapacitets- og fremdriftsstyring fra specifikation til aflevering; udbud, tilbud, aftalegrundlag, underentreprenører og sikkerhedsdokumentation.'),
 ('Daglig styring','Tavlemøder, flaskehalsanalyse og standardiserede arbejdsgange med forbedret leveringsevne.')]),
 ('Vedligeholdelses- og driftsleder / værkstedstekniker','Biofos, Lynetten · København · aug. 2017–jan. 2022','El- og mekaniske anlæg · døgnbemandet drift',[
 ('Drift og lager','Fejlfinding og forebyggende vedligehold af pumper, HVAC, højspændingstavler og SCADA. 5S, Standard Work og PDCA på værksted og reservedelslager.'),
 ('Sikkerhed','LOTO, APV, risikovurdering og opfølgning på nærved-hændelser i skifteholdsdrift.')]),
 ('Elektromekaniker / produktionsteamleder','ARJ Engineering · Teheran · dec. 2003–mar. 2010','12 mekanikere og teknikere',[
 ('Værksted','Vagtplanlægning, materialestyring, fejldiagnose og reparation af industrielle el- og mekaniske anlæg; rodårsagsanalyse og korrigerende handlinger.')])]
 for i,(title,meta,scope,bullets) in enumerate(jobs):
  if i == 3: m.page_break();m.section('ERHVERVSERFARING — FORTSAT')
  m.job(title,meta,scope=scope)
  for a,b in bullets:m.bullet(a,b,after=15)
 m.section('UDDANNELSE OG CERTIFICERING')
 for a,b in [('B.Tech, Technology Management & Mechanical Engineering — maskinmesterretningen','Maskinmesterskolen København · 2017–2022 · EQF 6'),('El- og maskinteknisk design, elteknik','Tehran Technical University · 2000–2003 · EQF 6'),('HF, matematik og fysik','VUC · 2012–2017'),('Elautoriseret maskinmester','Sikkerhedsstyrelsen · LV/MV/HV · 2023'),('PRINCE2-certificeret projektleder','AXELOS / PeopleCert'),('Køleteknik og klimaanlæg','AMU · Mercantec · 2021'),('STCW-certifikater','Maskinrumsvagt og udpegede sikkerhedsopgaver m.fl. · Søfartsstyrelsen · 2021–2023')]:m.edu(a,b)
 return m.save(path,title='Ansøgning og CV — Junior Planlægger, ELCON',subject='Kundeservice og montørplanlægning',keywords='kundeservice, planlægning, ladestander, Glostrup')
if __name__=='__main__':print(build(os.path.join(ROOT,'Shahram_Ajloo_ELCON_JuniorPlanlaegger_679.docx')))
