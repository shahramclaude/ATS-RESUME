#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cellerator · Teknisk driftsansvarlig · Lyngby.

Revideret ATS-sikkert dokument: dansk ansøgning (side 1), hard page break,
CV på højst to sider. Systemer og forhold, som kandidaten selv har bekræftet
for denne stilling (FMS, DALUX-FM, flydende engelsk, HVAC-parametre og
ugentlig tilkaldevagt), nævnes uden at opfinde konkrete produktnavne eller
opgaver i systemerne.
"""
from pathlib import Path
import sys

from docx.shared import Pt, RGBColor

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from ats_builder import Application

OUTPUT = ROOT / "Shahram_Ajloo_Cellerator_TekniskDriftsansvarlig_v2.docx"
NAME = "Shahram Ajloo"
TITLE = "Teknisk driftsansvarlig | teknisk drift, vedligehold og GMP-kvalificering"
CONTACT = "+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv"


def build(path=OUTPUT):
    a = Application(size=9.5)

    def job(title, details):
        p = a._p(before=4, after=0.5, line=11.6, keep=True)
        a._rich(p, f"**{title}**")
        r = p.add_run(" | " + details)
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

    # Brev, side 1
    a.name(NAME)
    a.meta(CONTACT)
    a.meta("Cellerator · Teknisk driftsansvarlig · Facility · Lyngby")
    a.subject("Ansøgning: Teknisk driftsansvarlig", before=4, after=4)
    a.para("Kære rekrutteringsteam hos Cellerator,", after=4)

    a.para(
        "Når Cellerators nye facilitet går fra kvalificering til de første produktionsforløb, "
        "skal forsyningsanlæg, alarmer, service og dokumentation fungere som ét driftsforløb. "
        "Cellerators offentliggjorte tidsplan lægger op til facility-IOQ i marts 2027, udstyrs-IOQ "
        "og indflytning i juni og de første kunder i september. Derfor skal ansvaret for hvert "
        "anlæg, alarm og serviceindgreb være tydeligt, før produktionsdriften begynder.", after=5)
    a.para(
        "I opstartsfasen vil jeg først samle anlægslisten, kritikalitet, gældende "
        "serviceaftaler og alarmgrænser for BMS og FMS. En løsningsorienteret reaktionsvej "
        "skal afklare, hvem der vurderer alarmen, hvornår der kræves fysisk eftersyn, hvem der "
        "kan tilkaldes, og hvornår QA eller Facility orienteres. Vagtinstruksen skal også "
        "fastlægge, hvilke selvstændige beslutninger den vagthavende kan træffe. Akut udbedring holdes adskilt "
        "fra planlagt vedligehold; hver serviceaftale skal beskrive opgave, adgang, sikkerhed "
        "og dokumenteret lukning.", after=5)
    a.para(
        "Forebyggende vedligeholdelse bør styres af kritikalitet, fejl- og servicehistorik og "
        "konsekvensen af uplanlagt nedetid. Første prioritering af black utilities omfatter "
        "varme, vand, el, pumper, rørsystemer og HVAC. Vedligeholdelse af tekniske installationer "
        "og bygningsvedligeholdelse planlægges ud fra samme risikovurdering, også for udstyr uden "
        "serviceaftale. Registrering i SAP og DALUX-FM skal give Facility og QA en sporbar "
        "historik, som understøtter planlægning, opfølgning på gentagne fejl og kommende "
        "beslutninger. Ved udstyrskvalificering kobles "
        "FAT/SAT og IQ/OQ/PQ til klare acceptkriterier, dokumentation og overdragelse til "
        "driften. Planlægningen skal være samarbejdsorienteret: Facility-teamet, Indkøb, QA, GMP "
        "og Process Development inddrages tidligt, så krav til service, adgang og ansvar er "
        "afklaret før opstart.", after=5)
    a.para(
        "Grundlaget er teknisk drift i 24/7-miljø med pumper, HVAC, højspændingstavler og "
        "SCADA, praktisk arbejde med BMS/CTS og FMS samt commissioning i medicinalindustrien, "
        "et reguleret miljø under GMP/FDA/EMA. Hos Novo Nordisk indgik FAT/SAT og IQ/OQ/PQ i "
        "37 CAPEX-projekter; ingen kritiske afvigelser stod åbne ved aflevering. SAP ERP og "
        "DALUX-FM indgår også i den praktiske værktøjskasse. Jeg kan indgå i vagtordningen med "
        "vagttelefon en uge ad "
        "gangen og føre den daglige dialog på flydende engelsk.", after=5)
    a.para(
        "Novo Nordisk Fonden har etableret Cellerator for at fremme celle- og genterapier og "
        "GMP-produktion af celleterapier. Det formål kræver stabil og dokumenteret infrastruktur. "
        "En tydelig "
        "dokumentationspraksis understøtter den kvalitetskultur, I beskriver. Det er den "
        "driftsdisciplin, jeg vil være med til at etablere fra opstarten.", after=3)
    a.meta("Med venlig hilsen", after=0.5)
    a.meta(NAME, after=0)

    # Hård sideskift: CV starter på ny side.
    a.page_break()

    # CV, side 2
    a.name(NAME)
    p = a._p(after=1, line=11.5)
    r = p.add_run(TITLE)
    r.font.size = Pt(9)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x00, 0x77, 0xC8)
    a.meta("Måløv · ajlooshahram@gmail.com · +45 93 99 95 14 · linkedin.com/in/shahramajloo")
    a.heading("Profil", before=4)
    a.para(
        "Elautoriseret maskinmester (LV/MV/HV) med erfaring fra teknisk drift, "
        "vedligehold og GMP-commissioning. Har arbejdet med 24/7-drift, BMS/CTS, FMS, "
        "SCADA, HVAC og tekniske forsyninger samt FAT/SAT og IQ/OQ/PQ. SAP ERP bruges "
        "dagligt; praktisk erfaring med DALUX-FM. Arbejder med forebyggende vedligehold, "
        "leverandørkoordinering, dokumentation og sikker overdragelse til drift.", after=2)

    a.heading("Faglige områder")
    a.bullet("Tekniske anlæg", "Pumper, HVAC, el og højspændingstavler, SCADA, procesrør og instrumentering.")
    a.bullet("Facility management", "BMS/CTS og FMS; SAP ERP og DALUX-FM.")
    a.bullet("Vedligehold", "Forebyggende og korrigerende vedligehold, CMMS, serviceleverandører, MTBF/MTTR, OEE og reservedele.")
    a.bullet("GMP og idriftsættelse", "FAT/SAT, IQ/OQ/PQ, protokoller, sporbar dokumentation og aflevering uden kritiske afvigelser.")
    a.bullet("HVAC", "Praktisk forståelse af luftmængde, temperatur, tryk og luftfugtighed.")

    a.heading("Erhvervserfaring")
    job("CTO for AI-afdelingen og elautoriseret maskinmester", "Data Power Consultant ApS · København · 2024–nu")
    a.bullet(None, "Ansvar for AI-afdelingen og el-teknik/ventilation; tekniske kundeopgaver fra kravafklaring og planlægning til idriftsættelse, dokumentation og overdragelse.")
    a.bullet(None, "SAP ERP og tekniske systemer indgår i den daglige opfølgning; el-tekniske service- og entrepriseaktiviteter videreført fra ELOHVAC i november 2026.")

    job("Ejer, teknisk direktør og elautoriseret maskinmester", "ELOHVAC ApS · København · maj 2023–nov. 2026")
    a.bullet(None, "Ledede fem elektrikere og tre lærlinge; planlagde service, installation og forebyggende vedligehold på el-, ventilations- og klimaanlæg.")
    a.bullet(None, "Koordinerede underentreprenører, materialer, sikkerhed, kvalitet og afleveringsdokumentation med fuldt P&L-ansvar.")

    job("Senior idriftsættelsesingeniør / projektleder, elsystem", "Novo Nordisk A/S · Kalundborg/Bagsværd · nov. 2022–jul. 2024")
    a.bullet(None, "Koordinerede 37 samtidige CAPEX-projekter på DKK 2–10 mio. og tværfagligt arbejde for 25 specialister.")
    a.bullet(None, "Gennemførte FAT/SAT og IQ/OQ/PQ under GMP/FDA/EMA; nul kritiske afvigelser ved aflevering. SAP ERP til økonomi, aktiver og omkostningsopfølgning.")

    # CV, side 3
    a.page_break()
    a.name(NAME)
    p = a._p(after=1, line=11.5)
    r = p.add_run("CV · fortsat")
    r.font.size = Pt(9)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x00, 0x77, 0xC8)

    job("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022")
    a.bullet(None, "Ledede 14 medarbejdere og fulgte 11 samtidige anlægsprojekter fra specifikation til aflevering; koordinerede underentreprenører og sikkerhedsdokumentation.")

    job("Vedligeholdelses- og driftsleder / værkstedstekniker", "Biofos (Lynetten) · København · aug. 2017–jan. 2022")
    a.bullet(None, "Vedligehold og akut fejlfinding i 24/7-drift på pumper, HVAC, højspændingstavler og SCADA.")
    a.bullet(None, "Arbejdede med drifts- og vedligeholdsplanlægning, reservedele og sikkerhedsprocedurer, herunder LOTO, APV og risikovurdering.")

    job("Elektromekaniker / produktionsteamleder", "ARJ Engineering · Teheran · dec. 2003–mar. 2010")
    a.bullet(None, "Ledede 12 mekanikere og teknikere i maskinværksted; fejldiagnose og reparation af industrielle elektriske og mekaniske anlæg.")

    a.heading("Uddannelse og autorisation")
    a.bullet(None, "B.Tech, teknologiledelse og maskinteknik (EQF 6), Copenhagen School of Marine Engineering & Technology Management, 2017–2022.")
    a.bullet(None, "Dansk elautorisation LV/MV/HV som elautoriseret maskinmester, Sikkerhedsstyrelsen, maj 2023.")
    a.bullet(None, "El- og maskinteknisk design, elteknik (EQF 6), Tehran Technical University, 2000–2003.")
    a.bullet(None, "Køleteknik og klimaanlæg (AMU), Mercantec, 2021; PRINCE2-certificeret projektleder.")

    a.heading("Sprog og arbejdsvilkår")
    a.para(
        "Dansk: modersmål. Engelsk: flydende i skrift og tale. Persisk: modersmål. "
        "Tilkaldevagt med vagttelefon en uge ad gangen: accepteret. Kørekort B.", after=1)

    a.save(str(path), title="Cellerator – Teknisk driftsansvarlig", subject="Ansøgning og CV")
    return path


if __name__ == "__main__":
    print(build())
