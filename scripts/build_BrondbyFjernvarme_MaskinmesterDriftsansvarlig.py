# -*- coding: utf-8 -*-
"""Brøndby Fjernvarme — Maskinmester / teknisk driftsansvarlig.
Dansk kombinationsdokument: jobfokuseret ansøgning først, CV og krav/evidensmatrix bagefter.
Style: AF; alarm-to-heat response chain; register Alarm-til-varme-loggen.
Bevidst åben om, at kandidatens praktiske kedelerfaring ikke omfatter de krævede certifikater
eller sikkerhedsgodkendelse, som han aktuelt ikke har.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Shahram_Ajloo_NNE_DepartmentManagerEI.docx")
OUTPUT = os.path.join(ROOT, "Shahram_Ajloo_BrondbyFjernvarme_MaskinmesterDriftsansvarlig.docx")
NAME = "SHAHRAM AJLOO"
TITLE = "Maskinmester · teknisk drift · vedligehold · forsyning"
CONTACT = "+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv"
DATE = "3. november 2026"

LETTER = [
    "Når vagthavende får en SMS om fejl under drift, er første beslutning ikke at genstarte et anlæg. Det er at fastslå, om alarmen handler om VEKS-leverancen, et netmålepunkt, en booster station eller en lokal central — og om temperatur, tryk og flow viser, at kunderne fortsat får varme, og forsyningssikkerheden er intakt.",
    "Brøndby Fjernvarmes SRO anlæg er fuldautomatisk under normal drift. Vagtberedskabet skal derfor være præcist: bekræft alarm og tidsforløb, se hvilket område og anlæg der er berørt, sammenhold trend og driftsdata, og aftal næste handling med den relevante kollega eller VEKS. SRO kan tilgås fra kontoret eller via bærbar PC'er med opkobling til SRO server; fjernadgang er et redskab til at vurdere situationen, ikke i sig selv en sikkerhedsgodkendelse af genstart. Ved risiko for anlæg eller forsyning følges proceduren for fysisk fremmøde og sikker afhjælpning.",
    "Den fælles alarm-til-varme-log skal gøre hændelsen efterprøvbar: tidspunkt og alarm, parameter og berørt område, leverance fra VEKS eller lokal drift, vurdering, beslutning, kontakt/ansvarlig, udført handling, genstartskriterium og bekræftet normalisering. En lukket alarm uden afklaret årsag er ikke en afsluttet driftsforstyrrelse. Gentagelser bliver til en vedligeholdsopgave, en ændret alarmgrænse eller en afprøvning af beredskabet — med ejer og frist.",
    "I den daglige drift samler en kort opgavegennemgang driftsmedarbejderen og den teknisk driftsansvarlige om sikkerhed, dagens fejl, planlagte eftersyn og nødvendige servicebesøg. En ugentlig gennemgang af åbne fejl, centraler, booster stationer, kritiske reservedele og VEKS-afhængigheder gør det muligt at prioritere forebyggende arbejde uden at miste blikket for varmeleverancen. Månedligt sammenholdes driftstimer, forbrug/brændsel, gentagne alarmer, udførte serviceeftersyn og dokumentationsfrister; afvigelser får en forklaring og opfølgning.",
    "Samarbejdet skal følge de reelle anlægsgrænser. Varmen i Brøndby Fjernvarmes net kommer normalt fra VEKS transmissionssystem, mens kedlerne bruges som spids- og reservelast. Det gør en tydelig kontakt- og eskalationsvej vigtig, især ved svigt i varmeforsyningen. Samtidig skal myndighedskrav, miljøindberetninger, serviceaftaler og beredskabsplaner have ansvarlige og faste datoer. En kort øvelse af alarmforløbet med VEKS og driftsmedarbejderen kan afprøve både beslutningsvej, vagttelefon og dokumentation.",
    "De første 30 dage bør bruges på at følge en erfaren kollega gennem anlæg, SRO, alarmhistorik, netmålepunkter, kedel- og serviceprocedurer samt snitfladerne til VEKS. Inden dag 60 kan alarmjournal, vedligeholdsoversigt og myndigheds-/miljøkalender samles i én prioriteret opfølgningsliste. Ved dag 90 bør de hyppigste alarmer, åbne vedligeholdspunkter, vagtrespons og beredskabsøvelse gennemgås med direktøren og driftsmedarbejderen, så forbedringer bygger på faktiske hændelser.",
    "Brøndby Fjernvarme er et andelsselskab, hvor andelshaverne er ejere af selskabet, og varmeforsyningen betyder noget for ca. 31.000 forbrugere. Jeg har praktisk kedelerfaring fra Biofos/Lynetten og erfaring fra 24/7 procesdrift; det fremgår nærmere af CV'et. Et formelt punkt skal samtidig stå åbent: Jeg har aktuelt ikke de nødvendige kedeldriftscertifikater, herunder olie-/gasfyring, og jeg har ikke den krævede sikkerhedsgodkendelse. Vil I oplyse de præcise certifikatkategorier og godkendelsesproces samt om begge forhold kan bringes på plads inden tiltrædelse? Jeg kan indgå i 14-dages rådighedsvagt (14 dages vagt) og bekræfter, at jeg kan møde på anlægget inden for 15–30 minutter fra Måløv."
]

PROFILE = (
    "Elautoriseret maskinmester (LV/MV/HV) med praktisk erfaring fra 24/7 teknisk procesdrift, "
    "der kan overføres til fjernvarmeforsyning; Biofos omfatter praktisk kedelarbejde, pumper, HVAC, "
    "højspændingstavler, SCADA, fejlfinding og forebyggende vedligeholdelse. "
    "Biofos/Lynetten: næsten 4½ år med kritisk el- og mekanisk drift; ELOHVAC: daglig planlægning "
    "og ledelse af 5 elektrikere og 3 lærlinge samt el-teknisk service; selvstændigt ansvar for ELOHVACs "
    "daglige drift og fuldt P&L. Supplerende "
    "idriftsættelses- og projektgrundlag fra 37 CAPEX-projekter hos Novo Nordisk. Dansk modersmål; "
    "praktisk rådighedsvagt og fremmøde i Brøndby inden for 15–30 minutter bekræftet."
)

BRONDBY_CONTEXT = (
    "Brøndby Fjernvarme er et andelsselskab; andelshaverne er ejere af selskabet. Forsyningen "
    "betjener ca. 31.000 forbrugere. Selskabets opgave omfatter drift og vedligehold af de 5 "
    "centraler og 2 booster stationer. Varmen i Brøndby Fjernvarmes net kommer normalt fra VEKS "
    "transmissionssystem; egne kedler udgør spids- og reservelast. Brøndby Fjernvarmes SRO anlæg "
    "er fuldautomatisk. Ved fejl under drift sendes der en SMS til Forsyningsafdelingen eller "
    "vagthavende. SRO kan tilgås fra kontoret eller via bærbar PC'er med opkobling til SRO server. Brøndbyvester-centralen er stedet, hvor varmeforsyningen styres; selskabet beskriver udviklingen som miljøvenlig energiforsyning. "
    "Det er den konkrete driftskontekst, ikke en påstand om at kandidaten allerede har arbejdet "
    "i Brøndbys system."
)

EVIDENCE = [
    ("Alarmvurdering og 24/7 drift", "Biofos/Lynetten: næsten 4½ år i kritisk 24/7-procesdrift med pumper, HVAC, højspændingstavler og SCADA. Praktisk kedelarbejde er særskilt bekræftet. Denne driftserfaring understøtter alarmvurdering; Brøndbys SRO-opsætning og alarmgrænser skal følges lokalt."),
    ("Kedler og varmeforsyning", "Kandidaten bekræfter praktisk arbejde med kedler på Biofos/Lynetten. Han har ikke oplyst kedeltype, brændsel, effekt eller brænderbeføjelse; derfor beskrives erfaringen ikke som olie-/gasfyring eller drift af en bestemt Brøndby-kedel."),
    ("Pumper, HVAC og tekniske anlæg", "Biofos dokumenterer pumper og HVAC i kritisk 24/7 drift samt forebyggende vedligehold og akut fejlfinding. ELOHVAC dokumenterer el-, tavle-, styrings-, ventilations- og klimaanlæg; erfaringen omsættes til systematisk opfølgning på centraler og boosterstationer."),
    ("Alarm og forsvarlig tilbageføring", "På et døgnbemandet procesanlæg har kandidaten håndteret akut teknisk fejlfinding og prioriteret kritiske anlæg. I Brøndby bør alarm, område, tryk/temperatur/flow og VEKS-snitflade verificeres før beslutning om fjernhandling, fremmøde eller sikker genstart."),
    ("Forebyggende vedligehold", "Biofos: forebyggende vedligehold på pumper, HVAC og el-/mekaniske anlæg, kritikalitetsforståelse og reservedelsflow. ELOHVAC: forebyggende el-service, planlægning, materialer og opfølgning. Vedligehold prioriteres efter forsyningsrisiko og dokumenterede anlægsintervaller."),
    ("Daglig prioritering og koordinering", "ELOHVAC: direkte daglig planlægning af 5 elektrikere og 3 lærlinge; Ventek-Air: daglig koordinering af et 14-personers team på 11 samtidige anlægsprojekter. Erfaringen passer til tydelig opgavefordeling for én driftsmedarbejder uden at overdrive stillingsniveauet."),
    ("Driftsdata og energi", "Novo Nordisk: SAP ERP, CAPEX-rapportering og PDCA-program, som reducerede energiomkostninger med 40 %. ELOHVAC: KPI-rapportering. Tallene er erfaring fra andre anlæg; de påstås ikke at være Brøndby-resultater. Etabler først en baseline for driftstimer, energiforbrug og brændsel."),
    ("Dokumentation og opfølgning", "ELOHVAC: KS-tjeklister, tidsplaner og afleveringsdokumentation; Novo: FAT/SAT, IQ/OQ/PQ, validerings- og afvigelsesdokumentation med nul kritiske fund ved aflevering. Det giver et grundlag for sporbare drifts- og vedligeholdsregistreringer."),
    ("VEKS og leverandørkoordinering", "Kandidaten har koordineret underentreprenører, specialister, indkøb og leverandører i ELOHVAC, Ventek-Air og Novo. Brøndbys forsyningsgrænse og procedure for kontakt med VEKS er lokal; de aftales og dokumenteres før selvstændig vagt."),
    ("Arbejdsmiljø og sikkerhed", "Biofos: LOTO, APV, risikovurdering og nærved-hændelser i 24/7 drift. ELOHVAC: LOTO og risikovurdering ved pladsopstart. Sikkerhedsgodkendelse er et særskilt ansættelseskrav og er ikke aktuelt i kandidatens besiddelse."),
]

EXPERIENCE = [
    ("Indehaver / Teknisk direktør / Elautoriseret maskinmester", "ELOHVAC ApS · København · maj 2023–nu", "5 elektrikere + 3 lærlinge · fuldt P&L-ansvar", [
        "Planlægger el-tekniske service- og entrepriseopgaver fra tilbud og materialer til udførelse, KS og aflevering; arbejder selv med fejlfinding, tavler, styring, ventilation og klima.",
        "Daglig ledelse og opgavefordeling for 5 elektrikere og 3 lærlinge, forebyggende vedligehold, risikovurdering, LOTO og kunde-/underentreprenørkoordinering.",
        "Python/Claude-værktøjer til tilbud, planlægning, KS-tjeklister og KPI-rapportering gav dokumenteret produktivitetsløft over 40 % i arbejdsgange — ikke et mål for varmeproduktion."
    ]),
    ("Medejer og CTO / teknisk ansvarlig for AI-afdelingen", "Data Power Consultant ApS · København · 2024–nov. 2026 (sideløbende med ELOHVAC)", "4–10 personer", [
        "Ledede tekniske og industrielle kundeløsninger fra krav og arkitektur til integration, idriftsættelse, dokumentation og overdragelse; LLM-API'er og AI-agenter.",
        "Indførte fælles standarder for AI-assisteret udvikling, review og test; anvendte AI i ledelsesrapportering og matrixledelse."
    ]),
    ("Senior idriftsættelsesingeniør / projektleder, elsystem", "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul. 2024", "37 CAPEX-projekter · 25 specialister · DKK 2–10 mio. pr. projekt", [
        "Koordinerede scope, fremdrift, omkostninger, risici og ressourcer på tværs af engineering, indkøb og anlæg; fulgte projektdata i SAP ERP.",
        "FAT/SAT, IQ/OQ/PQ, valideringsdokumentation og afvigelser; nul kritiske fund ved aflevering. PDCA-program reducerede energiomkostninger med 40 %."
    ]),
    ("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022", "11 samtidige anlægsprojekter · 14-personers team", [
        "Daglige tavlemøder og kapacitets-/flaskehalsstyring; koordinerede specifikation, produktion, installation, materialer, underentreprenører, kvalitet og formel aflevering."
    ]),
    ("Vedligeholdelses- og driftsleder / værkstedstekniker", "Biofos (Lynetten) · København · aug. 2017–jan. 2022", "Kritisk 24/7 procesdrift · pumper, HVAC, HV-tavler og SCADA", [
        "Forebyggende vedligehold og akut fejlfinding på elektriske og mekaniske anlæg, pumper, HVAC og højspændingstavler; overvågning med SCADA.",
        "Praktisk kedelerfaring (kandidaten bekræfter arbejde med kedler på Biofos); den konkrete kedeltype, brændsel og certifikatbeføjelse er ikke oplyst.",
        "LOTO, APV, risikovurdering, nærved-hændelser, 5S, Standard Work, PDCA og reservedelsflow i døgnbemandet drift."
    ]),
    ("Elektromekaniker / produktionsteamleder", "ARJ Engineering · Teheran · dec. 2003–mar. 2010", "12 mekanikere og teknikere", [
        "Fejldiagnose og reparation af industrielle el-/mekaniske anlæg, skiftplanlægning, materialestyring, rodårsagsanalyse og korrigerende handlinger."
    ]),
]

EDUCATION = [
    ("B.Tech (EQF 6), Technology Management & Mechanical Engineering", "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12"),
    ("El- og maskinteknisk design, elteknik (EQF 6)", "Tehran Technical University · 2000–2003"),
    ("HF — matematik og fysik", "VUC · 2012–2017"),
]

CREDENTIALS = [
    ("Danish electrical authorisation LV/MV/HV", "Sikkerhedsstyrelsen · maj 2023 · elautoriseret maskinmester (ikke elinstallatør)"),
    ("PRINCE2", "Certificeret projektleder · AXELOS / PeopleCert"),
    ("Lean og Six Sigma", "Anvendt i praksis; ikke certificeret"),
    ("Køleteknik og klimaanlæg (AMU)", "Mercantec · 2021"),
    ("STCW sikkerheds- og maskinrumskvalifikationer", "Søfartsstyrelsen · 2021–2023"),
]

TOOLS = [
    ("Forsynings- og procesdrift", "24/7 anlæg · pumper · HVAC · kedler (praktisk erfaring Biofos) · højspændingstavler · SCADA · fejlfinding · forebyggende vedligehold"),
    ("Styring og el", "Dansk LV/MV/HV-elautorisation · tavler og styring · el-fejlfinding · LOTO · APV · risikovurdering · PLC/SRO-erfaringens konkrete systemer og programmeringsomfang skal afklares"),
    ("Driftsplan og forbedringer", "Kritikalitet · forebyggende vedligehold · reservedelsflow · 5S · Standard Work · PDCA · A3 · tavlemøder · vagt-/hændelsesopfølgning"),
    ("Rapportering og værktøjer", "SAP ERP · CMMS · Microsoft Office / Excel · Power BI · Power Query · Python · Claude Code · drifts- og projektdata"),
    ("Sprog og rådighed", "Dansk modersmål · engelsk professionelt · persisk/farsi modersmål · kørekort B · Måløv · 14-dages rådighedsvagt og 15–30 min. fremmøde bekræftet"),
]

REQUIREMENTS = [
    ("Sikre kunderne stabil varmeforsyning", "Biofos dokumenterer næsten 4½ års 24/7-procesdrift, overvågning og akut fejlfinding på kritiske anlæg. Brøndby bør bruge alarm-til-varme-forløbet til at verificere leverance, berørt område og VEKS-snitflade, før anlæg eller kunder påvirkes."),
    ("Sikre stabil, sikker og effektiv drift af varmecentraler", "Biofos: forebyggende vedligehold, SCADA-overvågning og fejlfinding i 24/7 drift; ELOHVAC: LOTO, APV, planlagt service og opfølgning. Brøndbys centralprocedurer og sikkerhedskrav styrer enhver handling og tilbageføring."),
    ("Sikre drift af booster stationer", "Kandidaten har arbejdet med pumper og kritiske tekniske anlæg på Biofos. Brøndbys konkrete boosterstationer, trykzoner og driftsgrænser gennemgås med driftsmedarbejderen og VEKS, før selvstændig alarmhåndtering."),
    ("Sikre drift af øvrige tekniske installationer", "ELOHVAC omfatter fejlfinding og vedligehold på el, tavler, styring, ventilation og klima; Biofos omfatter pumper og HVAC. Samlet erfaring dækker tværgående tekniske installationer og praktisk vedligehold."),
    ("Overvåge varmevekslere", "Biofos- og ELOHVAC-erfaring med pumper, HVAC og procesudstyr giver en relevant systemforståelse. Brøndbys varmevekslere og normale driftskurver gennemgås konkret; alarmvurderingen kobles til temperatur, tryk og flow."),
    ("Overvåge pumper", "Pumper er dokumenteret som del af Biofos/Lynettens kritiske 24/7-procesdrift; kandidaten arbejdede med forebyggende vedligehold og akut fejlfinding. Brug driftstilstand, alarm og måledata sammen før indgreb."),
    ("Overvåge kedelcentraler", "Kandidaten bekræfter praktisk kedelarbejde på Biofos; konkret type og brændsel er ikke oplyst. Brøndbys kedler er spids-/reservelast, så sekvens, tilgængelighed og VEKS-ansvar afklares før driftshandlinger."),
    ("Følge temperatur, tryk og flow", "Brøndby bruger netmålepunkter til tryk- og temperaturstyring. Foreslået vagtpraksis sammenholder trend og målepunkt med flow/varmeleverance og berørt område, så et målersignal ikke forveksles med anlægsfejl."),
    ("Bruge SRO til styring, regulering og overvågning", "SCADA-overvågning i Biofos er dokumenteret; Brøndbys SRO er et specifikt system, som skal læres i introduktionen. Den lokale alarmmatrix, fjernadgang og grænse mellem automatisk regulering og manuel indgriben styrer betjeningen."),
    ("Vurdere alarmer og driftsforstyrrelser", "Kritisk 24/7-drift på Biofos og akut ELOHVAC-fejlfinding giver rutine i at prioritere signaler efter konsekvens. Log alarmtid, udvikling, berørt anlæg og varmeleverance, og skeln mellem straksreaktion og planlagt undersøgelse."),
    ("Fejlfinde på tekniske installationer, el og PLC-styringer", "Biofos og ELOHVAC dokumenterer elektrisk fejlfinding, tavler og styring; PLC-programmering eller konkrete PLC-platforme er ikke identificeret i master-CV'et. På Brøndbys anlæg følges godkendte procedurer og ændringer eskaleres til rette specialist."),
    ("Sikre forsvarlig genstart eller tilkalde hjælp", "Kandidatens erfaring fra kritisk drift støtter rolig fejlprioritering; sikker genstart forudsætter kendt årsag, kontrol af interlocks/værn og normaliserede procesværdier. Den lokale procedure og beslutningsret afklares før vagtansvar."),
    ("Planlægge og følge op på forebyggende vedligehold", "Biofos: forebyggende vedligehold og reservedelsflow; ELOHVAC: planlagte el-serviceopgaver, materialer og KS; kandidaten bruger kritikalitet og faste opfølgninger. Det omsættes til Brøndbys komponent- og serviceplan."),
    ("Følge op på serviceeftersyn og reparationer", "ELOHVAC følger serviceopgaver fra plan og materialer til KS og aflevering; Biofos fulgte vedligehold og akutte reparationer i 24/7 drift. Brøndbys serviceaftale, eftersynsfrist, udfører, rapport og lukning registreres samlet."),
    ("Prioritere driftsmedarbejderens daglige opgaver", "Direkte daglig opgavefordeling for 5 elektrikere og 3 lærlinge i ELOHVAC samt kapacitetsplanlægning for et 14-personers Ventek-team. Erfaringen overføres til en kort, synlig dagsplan for én driftsmedarbejder."),
    ("Følge driftstimer, brændselsforbrug og øvrige forbrugstal", "Novo Nordisk: SAP ERP og månedlig CAPEX-/økonomirapportering; ELOHVAC: KPI- og driftsrapportering. Etabler Brøndby-baseline for driftstimer, forbrug og brændsel; kandidatens tal fra andre virksomheder fremstilles ikke som Brøndby-data."),
    ("Sikre rettidige registreringer og teknisk dokumentation", "ELOHVAC: KS-tjeklister, tidsplaner og afleveringsfiler; Novo: test-, validerings- og afvigelsesregistre i reguleret miljø. En fælles alarm-/vedligeholdslog kan koble hændelse, beslutning, service og normal drift."),
    ("Medvirke til miljøindberetninger", "Novo dokumenterer myndighedslæst GMP/FDA/EMA-validering og kontrollerede projektregistre; miljøindberetning for varmeforsyning er ikke en specificeret tidligere leverance. Brøndbys målegrundlag, frister og godkendelsesansvar skal følges lokalt."),
    ("Koordinere driftsforhold med VEKS", "ELOHVAC og Novo dokumenterer tværgående leverandør- og specialistkoordinering. Brøndbys varme kommer normalt fra VEKS; kontaktveje, driftsgrænse og ansvar ved transmissionssvigt indarbejdes i alarm- og vagtrutinen."),
    ("Samarbejde med myndigheder, leverandører og entreprenører", "Novo koordinerede engineering, indkøb og site blandt 25 specialister; ELOHVAC håndterer kunder og underentreprenører. Myndighedsindberetninger og Brøndbys lokale tilladelser følges med frist, ansvarlig og dokumenteret kvittering."),
    ("Indhente tilbud og bestille serviceydelser", "ELOHVAC har tilbudsberegning, indkøb, materialer og leverandørkoordinering som del af fuldt P&L-ansvar. Brøndbys bestilling bør afgrænses med scope, pris, adgang, sikkerhed, forventet resultat og godkendt budget."),
    ("Følge op på eksternt udførte opgaver", "ELOHVAC og Ventek-Air følger eksterne udførende fra planlagt scope til kvalitet og aflevering; Novo dokumenterer test og lukning. Brøndbys servicebesøg lukkes først efter rapport, afprøvning og opdateret driftsdokumentation."),
    ("Afprøve og ajourføre beredskabsplaner", "Biofos' 24/7 drift omfattede risikovurdering, LOTO og nærved-hændelser. Brøndbys beredskab afprøves i samarbejde med den anden driftsmedarbejder og VEKS; øvelse, kontaktvej, alarm og læringspunkt dokumenteres."),
    ("Bidrage til forbedring og optimering", "Novo gennemførte PDCA, der reducerede energiomkostninger med 40 %; ELOHVAC har digitale værktøjer til planlægning og KPI-opfølgning. Dette er andre anlæg; Brøndby-forbedringer måles mod lokal baseline og varmeforsyningssikkerhed."),
    ("Maskinmester eller relevant teknisk uddannelse", "Kandidaten er elautoriseret maskinmester med B.Tech (EQF 6) i Technology Management & Mechanical Engineering samt el-/maskinteknisk designuddannelse (EQF 6). Dansk LV/MV/HV-elautorisation er angivet separat."),
    ("Praktisk erfaring med drift og vedligehold", "Biofos/Lynetten: næsten 4½ år i kritisk 24/7 drift med SCADA, pumper, HVAC, HV-tavler, forebyggende vedligehold og akut fejlfinding. Kandidaten bekræfter desuden praktisk arbejde med kedler på Biofos."),
    ("Selv håndtere driftsforstyrrelser og teknisk fejlfinding", "Biofos: akut fejlfinding på elektriske og mekaniske anlæg; ELOHVAC: fejlfinding på el, tavler og styring, fra akutte serviceopgaver til aflevering. Driftsforstyrrelser prioriteres efter forsynings- og personsikkerhed."),
    ("Vurdere fejl, sikker genstart eller behov for assistance", "Biofos' kritiske procesdrift og LOTO/APV-erfaring giver et sikkert beslutningsgrundlag, men Brøndbys anlægsprocedurer og beføjelser skal følges. Alarmens årsag og normaliserede procesværdier dokumenteres før genstart."),
    ("Systematisk vedligehold, dokumentation og opfølgning", "Biofos: forebyggende vedligehold, reservedelsflow, 5S og Standard Work; ELOHVAC: KS og afleveringsdokumentation; Novo: strukturerede test- og valideringsregistre. Opgaver lukkes med ejer, dato og resultat."),
    ("Olie- og gasfyrede kedelanlæg er en fordel", "Praktisk kedelerfaring fra Biofos er kandidatbekræftet, men type og brændsel er ikke oplyst. Olie-/gasfyringscertifikater har kandidaten ikke; han beder om præcisering af hvilke certifikater der skal foreligge inden ansættelsen."),
    ("Fjernvarme, forsyning, energi eller procesindustri er en fordel", "Biofos' 24/7 kritiske procesdrift er dokumenteret; Novo CAPEX dækkede energi og idriftsættelse. Direkte erfaring fra Brøndby eller VEKS hævdes ikke; den overførbare forsyningsdrift beskrives konkret."),
    ("Elektrisk fejlfinding er en fordel", "ELOHVAC: praktisk el-fejlfinding, installation, tavler og styring; Biofos: elektriske anlæg og højspændingstavler i kritisk drift. Arbejdet udføres inden for dansk autorisation, sikkerhedsprocedurer og konkret bemyndigelse."),
    ("El-diagrammer er en fordel", "El-/maskinteknisk designuddannelse (EQF 6), dansk LV/MV/HV-elautorisation samt arbejde med tavler og styring udgør relevant faglig baggrund. Brøndbys opdaterede diagrammer og tegningsrevisioner skal gennemgås før fejlsøgning."),
    ("PLC-styringer er en fordel", "Kandidaten oplyser praktisk erfaring med PLC-relateret anlægsarbejde; konkrete platforme, programmering og ændringsansvar er ikke nærmere specificeret. Ingen PLC-programmering eller Brøndby-systemejerskab påstås i CV'et."),
    ("SRO-anlæg er en fordel", "SCADA-overvågning er dokumenteret på Biofos; kandidaten har ikke identificeret Brøndbys SRO eller en anden specifik SRO-platform. Brøndbys fuldautomatiske SRO-system læres gennem introduktion og lokale alarminstrukser."),
    ("Kedeldrift er en fordel", "Kandidaten bekræfter praktisk arbejde med kedler på Biofos, men har ikke kedeldriftscertifikater og har ikke oplyst type, brændsel eller effekt. Han fremstiller derfor ikke erfaringen som olie-/gas-kedelbeføjelse."),
    ("Prioritere og koordinere uden krav om tidligere personaleledelse", "ELOHVAC dokumenterer daglig opgavefordeling for 8 medarbejdere i alt; Ventek-Air dokumenterer daglig koordinering af 14 medarbejdere. Erfaringen bruges praktisk, uden at påstå at jobbet kræver personaleansvar."),
    ("Nødvendige kedeldriftscertifikater ved ansættelsen", "Kandidaten har aktuelt ingen kedeldriftscertifikater, herunder certifikater for olie-/gasfyring. Det oplyses åbent; arbejdsgiveren bedes præcisere certifikatnavn, kedel-/brændstofkategori og hvornår beviset skal foreligge."),
    ("Nødvendig sikkerhedsgodkendelse ved ansættelsen", "Kandidaten har aktuelt ikke den krævede sikkerhedsgodkendelse. Ingen godkendelsesgrad eller behandlingstid påstås; spørgsmålet er, om godkendelsen kan gennemføres før ansættelse, og hvor tidligt processen skal starte."),
    ("Indgå i 14-dages rådighedsvagt", "Kandidaten bekræfter, at han kan indgå i 14-dages vagtrotation. Biofos' 24/7 drift er relevant baggrund; Brøndbys vagttelefon, alarmadgang og eskalationsprocedure indlæres ved introduktion."),
    ("Møde inden for 15–30 minutter", "Kandidaten bor i Måløv og bekræfter, at han kan møde på anlægget inden for opslagets 15–30 minutter under rådighedsvagt. Responstiden er kandidatbekræftet og må ikke forveksles med køretidsberegning."),
    ("Bevare roen under driftsfejl og træffe selvstændige beslutninger", "24/7 kritisk drift på Biofos og akut fejlfinding i ELOHVAC kræver prioritering, sikker isolering og rettidig eskalering. Brøndbys lokale beslutningsret og kriterier for genstart afklares før selvstændig vagt."),
    ("Arbejde grundigt, systematisk og følge op", "ELOHVAC: KS, checklister og afleveringsfiler; Novo: test- og valideringsdokumentation med nul kritiske fund; Biofos: vedligehold, reservedelsflow og Standard Work. Opgaver følges til verificeret lukning."),
    ("Samarbejde, videndeling og bede om hjælp", "Novo koordinerede 25 specialister på tværs af engineering, indkøb og site; ELOHVAC samarbejder med elektrikere og underentreprenører. Alarm- og driftsbeslutninger eskaleres til VEKS eller specialist ved behov."),
    ("Kommunikere tydeligt og prioritere samtidige opgaver", "Kandidaten bekræfter flydende dansk; daglig teamplanlægning, kundedialog, projektmøder og Novo-rapportering er dokumenteret. I vagten kobles præcis status, ansvarlig, næste handling og tidspunkt til alarmjournalen."),
    ("Fysisk arbejde i Brøndby", "Kandidaten bor i Måløv, har kørekort B og bekræfter, at han kan indgå i rådighedsvagten med 15–30 minutters fremmøde. Arbejdssted og fysisk anlægsopfølgning er dermed praktisk foreneligt."),
]


def add_jobs(m, jobs):
    for title, meta, scope, bullets in jobs:
        m.job(title, meta, scope)
        for text in bullets:
            m.bullet("", text, after=18, line=210)


def build(path=OUTPUT):
    m = MasterDoc(TEMPLATE, lang="da-DK")
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta(DATE)
    m.meta("Brøndby Fjernvarme · att. Gitte Hald, Hald HR Consulting · Maskinmester / teknisk driftsansvarlig")
    p = m._p(spacing_after=60, line=240, justify=False)
    m._run(p, "Motiveret ansøgning og CV · teknisk driftsansvarlig", bold=True)
    m.para("Kære Gitte Hald og Brøndby Fjernvarme,", after=32, justify=False)
    for text in LETTER:
        m.para(text, after=34, line=205)
    m.meta("Med venlig hilsen", after=8)
    m.meta("Shahram Ajloo", after=0)

    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "DRIFTSPROFIL")
    m.para(PROFILE, after=25, line=200)
    m.section("BRØNDBY FJERNVARMES DRIFTSKONTEKST")
    m.para(BRONDBY_CONTEXT, after=18, line=190)
    m.section("DOKUMENTERET DRIFTSEVIDENS")
    for label, detail in EVIDENCE:
        m.bullet(label, detail, after=12, line=195)
    m.section("ERHVERVSERFARING")
    add_jobs(m, EXPERIENCE[:2])

    m.page_break()
    m.resume_header(NAME, "Maskinmester · drift · vedligehold · fejlfinding", CONTACT, "ERFARING, UDDANNELSE OG FAGLIGE VÆRKTØJER")
    add_jobs(m, EXPERIENCE[2:])
    m.section("UDDANNELSE OG AUTORISATION")
    for title, detail in EDUCATION + CREDENTIALS:
        m.edu(title, detail)
    m.section("CERTIFIKATER OG FORMEL STATUS")
    m.para("Kedeldriftscertifikater, herunder olie-/gasfyring: ikke aktuelt i besiddelse. Nødvendig sikkerhedsgodkendelse: ikke aktuelt i besiddelse. Praktisk kedelerfaring fra Biofos er bekræftet, men erstatter ikke de certifikater, der kræves ved ansættelse. Kandidaten beder arbejdsgiveren præcisere krav og proces.", after=20, line=190)
    m.section("DRIFTSVÆRKTØJER OG PRAKTISKE FORHOLD")
    m.models_table("RELEVANT FAGLIGT GRUNDLAG", ("Område", "Erfaring / værktøjer"), TOOLS, widths=(2650, 7696), compact=True)

    m.page_break()
    m.resume_header(NAME, "Teknisk driftsansvarlig · drift og dokumentation", CONTACT, "DRIFTSDOKUMENTATION")
    m.para("Kravmatricen skelner mellem dokumenteret erfaring, foreslået arbejdsform og formelle forhold, som ikke aktuelt er opfyldt.", after=14, line=190)
    m.models_table("JOBOPSLAGETS KRAV OG KONKRET EVIDENS", ("Krav", "Dokumentation / afklaring"), REQUIREMENTS,
                   widths=(3550, 6796), compact=True)
    return m.save(path, title="Motiveret ansøgning og CV — Brøndby Fjernvarme, teknisk driftsansvarlig",
                  subject="Maskinmester / teknisk driftsansvarlig · fjernvarme · Brøndby",
                  keywords="Maskinmester; teknisk driftsansvarlig; Brøndby Fjernvarme; fjernvarme; kedler; drift; vedligehold; rådighedsvagt")


if __name__ == "__main__":
    print(build())
