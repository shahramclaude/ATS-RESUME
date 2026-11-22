"""Tosidet, enkeltspaltet CV til Coor Property; kilder: master-CV og bekræftelser."""
from pathlib import Path
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT=Path(__file__).resolve().parent.parent
DOC=ROOT/'Shahram_Ajloo_Coor_Property_CV_Genopbygget.docx'
d=Document(); sec=d.sections[0]
sec.top_margin=Cm(1.65); sec.bottom_margin=Cm(1.6); sec.left_margin=Cm(1.85); sec.right_margin=Cm(1.85)
sec.page_width=Cm(21);sec.page_height=Cm(29.7)
normal=d.styles['Normal']; normal.font.name='Calibri';normal.font.size=Pt(10.5)
d.core_properties.author='Shahram Ajloo';d.core_properties.title='CV — Shahram Ajloo — Driftschef / Operations Manager'
NAVY='183650'; INK='263543'; MUTED='526675'; BLUE='16748B'

def para(parts, before=0, after=0, line=14, keep=False, indent=0):
 p=d.add_paragraph(); f=p.paragraph_format
 f.space_before=Pt(before);f.space_after=Pt(after);f.line_spacing=Pt(line);f.keep_with_next=keep
 if indent:f.left_indent=Pt(indent);f.first_line_indent=Pt(-indent)
 for text,size,color,bold in parts:
  r=p.add_run(text);r.bold=True if bold else None;r.font.name='Calibri';r.font.size=Pt(size);r.font.color.rgb=RGBColor.from_string(color)
  rp=r._element.get_or_add_rPr();lang=OxmlElement('w:lang');lang.set(qn('w:val'),'da-DK');rp.append(lang)
 return p

def text(s,after=5):para([(s,10.5,INK,False)],after=after,line=14)
def heading(s):para([(s.upper(),10,BLUE,True)],before=12,after=5,line=13,keep=True)
def job(title,company,period):
 para([(title,11,NAVY,True)],before=7,after=1,line=14,keep=True)
 para([(company+'  |  '+period,10,MUTED,False)],after=4,line=13,keep=True)
def bullet(s):para([('•  ',10.5,BLUE,True),(s,10.5,INK,False)],after=3,line=14,indent=13)
def header():
 para([('SHAHRAM AJLOO',24,NAVY,True)],after=3,line=28,keep=True)
 para([('DRIFTSCHEF / OPERATIONS MANAGER  ·  COOR PROPERTY',11,BLUE,True)],after=5,line=14,keep=True)
 para([('Måløv, Ballerup  |  +45 93 99 95 14  |  ajlooshahram@gmail.com',10,MUTED,False)],after=2,line=13,keep=True)
 para([('linkedin.com/in/shahramajloo',10,MUTED,False)],after=3,line=13)
header()
heading('Profil')
text('Elautoriseret maskinmester med erfaring i ejendomsdrift, teknisk service og vedligehold. Har ledet ledere og medarbejdere og arbejdet med kundekontakt, kontraktopfølgning og forecast. Kombinerer teknisk forståelse med personaleledelse og økonomisk ansvar. Erfaringen er relevant for Facility Management, hvor sikkerhed og kundeoplevelse går hånd i hånd.')
heading('Relevant ledelseserfaring')
bullet('Ledelse gennem andre: Personaleansvar for ledere, som selv leder medarbejdere, samt erfaring med et selvstyrende team.')
bullet('Kunde og drift: Ejendomsdrift og vedligehold på flere lokationer, tekniske serviceleverancer og opfølgning på aftaler og kontraktkrav.')
bullet('Økonomi og kvalitet: Erfaring med budget, forecast og kontraktopfølgning samt fuldt resultatansvar i ELOHVAC.')
heading('Erhvervserfaring')
job('Ejer / teknisk direktør / elautoriseret maskinmester','ELOHVAC ApS · København','maj 2023 – nu')
bullet('Leder fem elektrikere og tre lærlinge med ansvar for planlægning, medarbejdersamtaler, oplæring og arbejdsmiljø.')
bullet('Driver tekniske serviceopgaver for erhvervskunder: installation, fejlfinding og forebyggende vedligehold på el-, ventilations- og klimaanlæg.')
bullet('Har fuldt resultatansvar og styrer tilbud, materialer, underentreprenører, kvalitetssikring og afleveringsdokumentation.')
bullet('Udviklede digitale værktøjer til tilbud, tidsplaner og kvalitetstjek, som har bidraget til et produktivitetsløft på over 40 %.')
job('Medejer og CTO / teknisk ansvarlig for AI-afdelingen','Data Power Consultant ApS · København','2024 – nov. 2026')
bullet('Ansvarlig for en afdeling på 4–10 personer og tekniske løsninger fra kundens behov til dokumentation og overdragelse. Virksomheden er ophørt; rollen var sideløbende med ELOHVAC.')
p=d.add_paragraph();p.add_run().add_break(WD_BREAK.PAGE)
para([('SHAHRAM AJLOO',15,NAVY,True),('  |  CV',10,MUTED,False)],after=2,line=19)
heading('Erhvervserfaring  ·  fortsat')
job('Senior idriftsættelsesingeniør / projektleder, elsystem','Novo Nordisk A/S · Kalundborg / Bagsværd','nov. 2022 – jul. 2024')
bullet('Koordinerede 25 specialister og 37 samtidige CAPEX-projekter med opfølgning på fremdrift, økonomi, ressourcer og risiko.')
bullet('Samarbejdede på tværs af engineering, indkøb og anlæg; gennemførte FAT/SAT og IQ/OQ/PQ med nul kritiske afvigelser ved aflevering.')
job('Projekt- og værkstedsleder','Ventek-Air · København','jan. 2022 – nov. 2022')
bullet('Ledede et team på 14 og styrede kapacitet og fremdrift på 11 samtidige anlægsprojekter.')
bullet('Arbejdede med tilbud, aftalegrundlag, underentreprenører, sikkerhedsdokumentation og aflevering; brugte tavlemøder og flaskehalsanalyser i den daglige styring.')
job('Vedligeholdelses- og driftsleder / værkstedstekniker','BIOFOS, Lynetten · København','aug. 2017 – jan. 2022')
bullet('Arbejdede med kritisk el- og mekanisk drift, forebyggende vedligehold og akut fejlfinding på blandt andet pumper, HVAC og højspændingstavler.')
bullet('Anvendte LOTO, risikovurdering og APV samt standardarbejde og PDCA i skifteholdsdrift.')
job('Elektromekaniker / produktionsteamleder','ARJ Engineering · Teheran','dec. 2003 – mar. 2010')
bullet('Ledede 12 mekanikere og teknikere; vagtplanlægning, materialestyring samt fejldiagnose og reparation af industrielle anlæg.')
heading('Uddannelse og certificering')
text('B.Tech, Technology Management and Mechanical Engineering  |  Copenhagen School of Marine Engineering & Technology Management  |  2017–2022',after=3)
text('Elautoriseret maskinmester, LV/MV/HV  |  Sikkerhedsstyrelsen  |  2023',after=3)
text('PRINCE2 certificeret projektleder  |  AXELOS / PeopleCert',after=3)
text('Køleteknik og klimaanlæg  |  Mercantec AMU  |  2021',after=3)
text('El- og maskinteknisk design, elteknik  |  Tehran Technical University  |  2000–2003',after=3)
heading('Metoder, værktøjer og sprog')
text('Lean og Six Sigma anvendt i praksis. Excel, SAP ERP og digitale planlægningsværktøjer. Dansk, engelsk og persisk. Kørekort B.',after=0)
d.save(DOC)
