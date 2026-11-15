# -*- coding: utf-8 -*-
"""Teamkoordinator, produktionen — Lachenmeier Monsun A/S, Sønderborg (dansk opslag via Career | JKS).

Dansk opslag -> dansk dokument, 4 sider: brev side 1, CV side 2, uddannelse + 90 dage +
metodeafsnit + "Hvor jeg ville starte" side 3, kravmatrix side 4. Format per master/README.md:
brev -> CV -> uddannelse/90 dage -> matrix. Rekrutterens anvisninger om ansøgningsform følges ikke
(opslaget beder kun om CV via "Søg stillingen" — brevet er alligevel side 1).

STILVALG (master/STILREGISTER.md; godkendt af scripts/style_guard.py, 3/3 skift mod #211):
  register      = PRODUKTIONSLINJE — takt, kapacitet, flaskehals, flow, rækkefølge. Rollen er en
                  koordinator i en projektorienteret maskinfabrik. Sidst #202.
  åbningsgreb   = C (STEDET) — beslutningen tages på gulvet ved tavlen klokken 06.30, ikke i et
                  mødelokale. Sidst #199.
  struktur      = DAGSFORLØBET — 06.30 → 15.00 med fem faste holdepunkter, hver med et bevis.
                  Sidst #204.
  kadence       = længere, forklarende åbningsafsnit med ét tal som omdrejningspunkt; derefter
                  korte sætninger i CV'et.

KULTURSYNKRONISERING (policy 04.11.2026), kilder i master/LEDELSESVAERKTOEJER_OG_KULTUR_INTEL.md §183:
  Lachenmeier Monsun A/S, grundlagt 1952, Coriolisvej 1, Ragebøl, 6400 Sønderborg; ca. 69 ansatte.
  MONSUN™-brandet til **Feed & Grain** og **Biomass**: snegletransportører, PAM cellesluser,
  transportudstyr til korn, møller, premixfabrikker, maltanlæg, havne- og indlandsterminaler,
  turn-key anlæg og enkeltmaskiner som underleverandør. Egen beskrivelse: "Our customers are unique
  – so are our solutions", "a world of solutions that last", 50+ års erfaring med kundetilpassede
  løsninger. Produktionen er projektorienteret og leverer til hele verden. Kulturord fra opslaget:
  uformel omgangstone, gode kollegaer, ordnede forhold, mulighed for efteruddannelse.

Ingen opdigtede fakta. Dokumenteret grundlag: 12 mekanikere og teknikere i produktionsværksted
(ARJ Engineering 2003–2010); 14 medarbejdere og 11 samtidige entrepriser med eget værksted
(Ventek-Air 2022); 5 elektrikere + 3 lærlinge med fuldt P&L (ELOHVAC 2023–); 37 CAPEX-projekter,
25 specialister og nul kritiske fund (Novo Nordisk 2022–2024); 24/7-drift med SRO/SCADA, APV, LOTO
og 5S (Biofos 2017–2022); maskinmester (EQF 6) og elautorisation LV/MV/HV, AMU køle-/VVS-teknik.
Ingen påstand om smede-, svejse- eller drejeerfaring med hænderne: metalarbejdet er dokumenteret
som værkstedsledelse, tolerancekontrol og montage, ikke som faglig svendeprøve.
"""
import os
from master_design import MasterDoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'Shahram_Ajloo_NNE_DepartmentManagerEI.docx')
NAME = 'SHAHRAM AJLOO'
TITLE = 'Teamkoordinator, produktion · værksted, flow og kvalitet'
CONTACT = '+45 93 99 95 14 · ajlooshahram@gmail.com · linkedin.com/in/shahramajloo · Måløv'


def build(path):
    m = MasterDoc(TEMPLATE, lang='da-DK')
    m.header_banner(NAME, TITLE, CONTACT)
    m.meta("4. november 2026")
    m.meta("Teamkoordinator, produktionen · Lachenmeier Monsun A/S · Sønderborg")
    p = m._p(spacing_after=80, line=260, justify=False)
    m._run(p, "Ansøgning: Teamkoordinator til produktionen", bold=True, color='1A1A1A')
    m.para("Kære Heidi Schmidt Degermann,", after=60)

    # ---------------------------------------------------------------- side 1
    m.para("**Klokken 06.30 står atten medarbejdere i smedeafdelingen og skal i gang — og hvad de "
           "skal i gang med, bliver afgjort af en beslutning, som nogen skal tage, før den første "
           "maskine startes.** Der er altid tre opgaver, der alle har en kunde bag sig, altid én "
           "tegning hvor der mangler et mål, og altid en drejebænk eller en svejser, som bliver "
           "flaskehalsen i dag og ikke i morgen. En koordinator er ikke den, der løser alle tre "
           "opgaver. Det er den, der sørger for, at der bliver valgt, at valget er begrundet, og at "
           "den næste i kæden ved, hvad der blev valgt. Det er den slags hverdag, jeg har haft i "
           "tolv år som leder i produktion og værksted, og det er den, jeg søger her.", after=80)

    m.para("**06.30 — dagen begynder ved tavlen.** Hvem står ved hvilken maskine, hvilken ordre har "
           "en lastbil, der venter, og hvilken vare mangler vi, før opgaven kan starte. Tavlemødet "
           "skal vare femten minutter, ikke tres: de samme tal hver dag, de samme tre spørgsmål, og "
           "en beslutning på hver linje. Jeg har kørt den slags møder med 14 mand og 11 samtidige "
           "opgaver, og pointen er ikke mødet — det er, at alle går til deres maskine med den samme "
           "prioritering i hovedet.", after=80)

    m.para("**09.00 — den første beslutning er næsten altid en flytning.** En mand fra "
           "pladebearbejdning over til montagen, en drejeopgave skubbet to timer, en ekstern "
           "bearbejdning sendt ud, fordi tolerancen ikke kan holdes i huset i dag. Flytningen skal "
           "have en grund, en varighed og en pris, og den skal meldes til dem, der bliver påvirket, "
           "inden den sker — ikke bagefter, når de opdager, at deres emner er væk.", after=80)

    m.para("**11.30 — spørgsmålet ved maskinen er det vigtigste i jobbet.** En smed står med en "
           "emne, der ikke passer med tegningen, og han spørger, om han skal gøre som tegningen "
           "eller som det, der virker. Svaret skal være en beslutning med et navn på, ikke en "
           "holding: mål efter, dokumentér afvigelsen, og gå videre med den løsning, der kan "
           "leveres. Faglig **sparring** er ikke at have ret — det er at gøre kollegaen i stand til "
           "at træffe det rigtige valg selv næste gang.", after=80)

    m.para("**13.00 — flowet mellem områderne er der, hvor timen tabes.** Klip, buk, svejs, drej, "
           "montér: hvert område kan være effektivt og alligevel stå stille, fordi emnerne kommer i "
           "den forkerte rækkefølge. Derfor kigger jeg på **kapacitet** og **takt** pr. område og "
           "ikke kun på, om folk arbejder; en batch, der venter foran drejebænken, er dyrere end en "
           "batch, der venter foran montagen. **Flaskelhals** flytter sig, når man løser den, og "
           "den skal findes igen hver uge.", after=80)

    m.para("**15.00 — dagen slutter med et notat.** Hvad blev færdigt, hvad flyttede sig, og hvad "
           "skal den næste skiftegang vide. **Fremdrift**, **kvalitet** og **deadlines** bliver ikke "
           "styrket af, at nogen husker det hele — men af at det står skrevet, så det kan læses "
           "dagen efter af en, der ikke var med. **Kvalitetskontrol** og **KS** er den samme "
           "disciplin: mål, skriv ned, og luk afvigelsen, når den er rettet, ikke når den er "
           "lovet.", after=80)

    m.para("**Det, der bliver lavet i Sønderborg, bliver ikke lavet om igen på stedet.** En "
           "**snegletransportør** eller en cellesluse til et **Feed & Grain**- eller "
           "**Biomass**-anlæg bliver bygget til en kunde, der står med et anlæg i drift et sted, hvor "
           "der ikke er en smed i nærheden. Derfor er rækkefølgen, tolerancen og den skrevne "
           "afvigelse ikke administration — det er det, der gør en kundetilpasset maskine til noget, "
           "der kan samles og køre, første gang kunden ser den.", after=80)

    m.para("**Det faglige fundament.** Jeg er uddannet elektriker og senere **maskinmester** "
           "(EQF 6), og jeg har ledet et produktionsværksted med tolv mekanikere og teknikere og et "
           "værksted med 14 mand, hvor plader blev klippet, bukket og samlet til kanaler og "
           "komponenter, og hvor **tolerancer** og **stykliste** afgjorde, om montagen gik op. "
           "**Metalbearbejdning**, **svejsning** og **maskindele** kender jeg som den, der har "
           "planlagt arbejdet, læst **tegningerne** og kontrolleret emnerne — og som den, der har "
           "stået med ansvaret, når en **deadline** ikke holdt.", after=80)

    m.para("**Praktisk.** Jeg bor i Måløv, og Sønderborg er tre timer væk — det er en flytning, "
           "ikke et pendlerforhold, og det er jeg klar over. **Kørekort B.** Dansk som modersmål, "
           "engelsk og tysk på arbejdsniveau med leverandører og kunder. Efteruddannelse inden for "
           "bearbejdning og ledelse tager jeg gerne. Kan starte efter aftale.", after=60)
    m.meta("Med venlig hilsen", after=20)
    m.meta("Shahram Ajloo", after=0)

    # ---------------------------------------------------------------- side 2 — CV
    m.page_break()
    m.resume_header(NAME, TITLE, CONTACT, "PROFIL")
    m.para("Produktions- og værkstedsleder med tolv år i driften. Tolv mekanikere og teknikere i "
           "produktionsværksted, 14 medarbejdere og 11 samtidige entrepriser med eget værksted, fem "
           "elektrikere og tre lærlinge med fuldt P&L. Uddannet elektriker og **maskinmester** "
           "(EQF 6). Arbejder ved tavlen, ikke fra et kontor.", after=80)

    m.section("DRIFT OG KOORDINERING")
    for label, body in [
        ("Daglig prioritering",
         "Tavlemøde hver morgen med de samme tal. Tre spørgsmål: hvad skal ud i dag, hvad mangler, "
         "og hvem flytter vi."),
        ("Kapacitet og flaskehals",
         "Belægning pr. område og pr. uge. **Flaskelhals** fundet på data, ikke på mavefornemmelse "
         "— og flyttet, når den var løst."),
        ("Når planen ændrer sig",
         "**Projektorienteret** produktion betyder, at prioriteter flytter sig midt i ugen. "
         "Ændringen meldes ud samme dag, med begrundelse og ny rækkefølge."),
    ]:
        m.bullet(label, body)

    m.section("KVALITET OG VÆRKSTED")
    for label, body in [
        ("Kontrol og tolerancer",
         "**Kvalitetskontrol** ved emnet, ikke ved afleveringen. Mål efter **tegningerne**, skriv "
         "afvigelsen ned, og luk den når den er rettet."),
        ("KS og dokumentation",
         "**KS** som tjekliste pr. ordre, med målinger og afvigelser i samme fil — nul kritiske "
         "fund ved aflevering på 37 CAPEX-projekter i reguleret produktion."),
        ("Arbejdsmiljø og orden",
         "**5S** og **APV** som daglig praksis, ikke et årligt dokument: faste pladser, mærkede "
         "emner, sikkerhedsrundering og nærved-hændelser behandlet samme uge."),
    ]:
        m.bullet(label, body)

    m.section("MENNESKER OG FAGLIGHED")
    for label, body in [
        ("Faglig sparring",
         "**Sparring** ved maskinen, hvor spørgsmålet opstår. Svaret er en beslutning med et navn "
         "på — ikke en holdning."),
        ("Oplæring og udvikling",
         "**Oplæring** med plan for den enkelte, **MUS** hvert år, og ansvar givet tidligt til dem, "
         "der vil. Tre lærlinge uddannet i egen virksomhed."),
        ("Lean i praksis",
         "**Lean** som værktøjskasse: **5S**, **A3**, tavlemøder, standardarbejde og "
         "forbedringsforslag fra gulvet — med **40 procent** højere produktivitet som resultat."),
    ]:
        m.bullet(label, body)

    m.section("ERHVERVSERFARING")
    m.job("Ejer / teknisk direktør", "ELOHVAC ApS · København · maj 2023–nu",
          scope="5 elektrikere + 3 lærlinge · fuldt P&L · planlægning og levering")
    m.bullet("Drift med eget ansvar",
              "Ordretilgang, kapacitet og levering styret fra uge til uge; **SAP** og egne "
              "værktøjer til tidsplan, **stykliste** og opfølgning.")

    m.job("Senior Commissioning Engineer / Project Manager",
          "Novo Nordisk A/S · Kalundborg / Bagsværd · nov. 2022–jul 2024",
          scope="37 samtidige CAPEX-projekter · 25 specialister · GMP/FDA/EMA")
    m.bullet("Kvalitet i reguleret produktion",
              "Afvigelser, ændringsstyring og dokumentation med nul kritiske fund ved aflevering; "
              "**deadlines** holdt med myndigheden som medlæser.")

    m.job("Projekt- og værkstedsleder", "Ventek-Air · København · jan. 2022–nov. 2022",
          scope="14 medarbejdere · 11 samtidige entrepriser · eget værksted")
    m.bullet("Værksted og montage",
              "Kanaler og komponenter **klippet, bukket** og samlet i eget **værksted**, monteret på "
              "11 sager samtidigt — **tolerancer** og rækkefølge afgjorde, om det gik op.")

    m.job("Drifts- og vedligeholdelseschef", "Biofos (Lynetten) · København · aug. 2017–jan. 2022",
          scope="Renseanlæg i 24/7-drift · pumper, HVAC, HV-tavler, SRO/SCADA")
    m.bullet("Vedligehold som plan",
              "Forebyggende **vedligehold** og planlagte udfald; **5S** og **sikkerhed** som fast "
              "rytme, og **kapacitet** styret mod nedbrud i stedet for mod ønsker.")

    m.job("Produktionsformand / elektromekaniker",
          "ARJ Engineering · Teheran · 2003–2010 · 12 mekanikere og teknikere")
    m.bullet("Produktionsværksted",
              "Daglig fordeling af arbejde i et værksted med **metalbearbejdning**, **bearbejdning** "
              "af emner og **montage**; maskiner, værktøj og **tegninger** i daglig brug.")

    # ---------------------------------------------------------------- side 3
    m.page_break()
    m.section("UDDANNELSE OG AUTORISATION")
    m.edu("Elautoriseret maskinmester — dansk elautorisation LV/MV/HV",
          "Sikkerhedsstyrelsen · maj 2023")
    m.edu("B.Tech, Technology Management and Mechanical Engineering (EQF 6)",
          "Copenhagen School of Marine Engineering & Technology Management · 2017–2022 · GPA 7,6/12")
    m.edu("El- og maskinteknisk design, Electrical Engineering (EQF 6)",
          "Tehran Technical University · 2000–2003")
    m.edu("Køle- og VVS-teknik (AMU) · Lean: 5S, PDCA, VSM, A3",
          "Mercantec · 2021 · STCW-sikkerhedscertifikater (2021–2023)")

    m.section("SPROG, PRAKTIK OG REFERENCER")
    m.para("**Dansk:** modersmål · **Engelsk:** professionelt · **Tysk:** arbejdsniveau · "
           "**Bor i Måløv** og søger stillingen med flytning til Sønderborg for øje · "
           "**Kørekort B** · **Kan starte efter aftale** · Referencer efter aftale.", after=70)

    m.models_table(
        "DE FØRSTE 90 DAGE — FRA TAVLEN KL. 06.30 TIL EN PLAN DER HOLDER",
        ["Periode", "Hvad der sker, og hvordan det måles"],
        [
            ("Uge 1–2",
             "Gå med i produktionen hver dag: lær de fire-fem områder at kende, se hvor emnerne "
             "faktisk venter, og få **stykliste**, **tegninger** og ordreflow ind under huden — sammen "
             "med dem, der står ved maskinerne."),
            ("Dag 30",
             "Tavlemødet har en fast form og de samme tal; hver ordre har en ejer og en dato, og de "
             "tre ting, der oftest stopper flowet, er identificeret med et tal på."),
            ("Dag 60",
             "Første **flaskehals** flyttet med data: belægning pr. område, **kapacitet** og **takt** "
             "pr. uge, og en simpel oversigt, som også ledelsen kan læse."),
            ("Dag 90",
             "To **arbejdsgange** ændret og skrevet ned som standard, en **A3** på den gentagne fejl, "
             "og **5S** gennemført i ét område — med et fald i ventetid, der kan måles, ikke bare "
             "fortælles."),
        ],
        widths=(1500, 8830))

    m.section("EN KOORDINATOR SKAL VÆRE DEN, DER AFGØR DET — IKKE DEN, DER SPØRGER VIDERE")
    m.para("I en projektorienteret produktion kommer der hver dag spørgsmål, som ingen anden har "
           "mandat til at svare på: skal emnet laves om, skal kunden ringes op, eller skal vi levere "
           "med en afvigelse? Et svar, der bliver sendt videre, koster en dag; et svar, der bliver "
           "givet med grund og dokumentation, koster fem minutter. Det kræver, at koordinatoren er "
           "på gulvet, kender tegningen og har lyst til at tage ansvaret — ikke bare referere det.",
           after=70)

    m.section("KVALITET ER IKKE EN KONTROL TIL SIDST — DET ER EN VANE PR. EMNE")
    m.para("Når et emne først er svejset, bukket eller drejet forkert, er der kun to udfald: om "
           "arbejde eller skrot. Derfor ligger kontrollen ved emnet og ved opspændingen, og den "
           "bliver udført af den, der laver emnet, med et mål, der er skrevet ned. **KS** er ikke et "
           "dokument, der bliver fyldt ud bagefter; det er et spørgsmål, der bliver stillet, før "
           "emnet forlader bænken.", after=70)

    m.section("OPTIMERING UDEN AT FOLK FØLER SIG SOM ET TAL")
    m.para("Forbedringer, der bliver besluttet på et kontor, holder sjældent længere end til næste "
           "travle uge. Dem, der holder, kommer fra den, der står med opgaven: en ny rækkefølge på "
           "hylden, et andet opspænd, en flyttet maskine. Min opgave er at gøre forslaget færdigt — "
           "prøve det af i en uge, måle det, og skrive det ned som standard, hvis det virker. Det er "
           "også den hurtigste vej til et bedre **arbejdsmiljø**: folk, der bliver spurgt, bliver "
           "også hørt.", after=70)

    m.section("DEADLINES HOLDES I UGE 3, IKKE I UGE 12")
    m.para("En forsinkelse bliver ikke skabt den dag, den bliver meddelt. Den bliver skabt tre uger "
           "før, da en tegning lå stille, eller da et emne blev sendt ud uden at nogen spurgte, "
           "hvornår det kom retur. Derfor følger jeg de ordrer, der er tættest på at glide, og "
           "melder det ud, mens der stadig er tid til at flytte en maskine eller tage en ekstra "
           "weekend ind — til salg, til projektlederen og til kunden, i den rækkefølge. Dårligt nyt "
           "med en plan er en samtale; dårligt nyt uden er et spørgsmål om tillid.", after=70)

    m.section("HVOR JEG VILLE STARTE")
    m.para("Ved tavlen klokken 06.30, fordi det er der, prioriteringen bliver sat — og fordi en "
           "koordinator, der ikke er med om morgenen, ikke bliver taget alvorligt resten af dagen. "
           "Første uge: gå med i alle områder, notér hvor emnerne venter, og læs de sidste tre "
           "måneders **afvigelser** og forsinkelser igennem for at se, om det er de samme tre ting, "
           "der går galt hver gang. Derefter tage fat på den første af dem — med et tal, en ændring "
           "og en uge til at bevise, at det virker.", after=0)

    # ---------------------------------------------------------------- side 4
    m.page_break()
    m.models_table(
        "DET EFTERSPØRGER DE — DET HAR JEG",
        ["Krav i opslaget", "Dokumentation"],
        [
            ("Daglig koordinering og prioritering af opgaver i produktionen",
             "Tavlemøde hver morgen med de samme tal og en beslutning pr. linje; 14 mand og 11 "
             "samtidige opgaver koordineret, og tolv mekanikere i et produktionsværksted."),
            ("Sikre fremdrift, kvalitet og overholdelse af deadlines",
             "**Fremdrift** styret uge for uge mod leveringsdatoer på 37 CAPEX-projekter og 11 "
             "entrepriser; **kvalitet** målt ved emnet, ikke ved afleveringen."),
            ("Faglig sparring og støtte til medarbejderne i den daglige produktion",
             "**Sparring** ved maskinen, hvor spørgsmålet opstår: en beslutning med grund og navn — "
             "og en forklaring, der gør kollegaen i stand til at vælge selv næste gang."),
            ("Sikre et godt samarbejde og flow mellem de forskellige produktionsområder",
             "**Flow** mellem klip, buk, svejs, drej og **montage** styret på belægning pr. område; "
             "emner, der venter foran en bænk, behandlet som den udgift de er."),
            ("Bidrage til optimering af arbejdsgange og et godt arbejdsmiljø",
             "**Arbejdsgange** ændret med dem, der udfører dem, og skrevet ned som standard; **5S** "
             "og **APV** som daglig praksis med sikkerhedsrundering og nærved-hændelser."),
            ("Solid håndværksmæssig baggrund — smed, industritekniker eller tilsvarende erfaring fra metalindustrien",
             "Uddannet elektriker og **maskinmester**; tolv års ledelse i produktionsværksted med "
             "**metalbearbejdning** og i eget værksted med plade og kanaler — håndværket er kendt "
             "fra gulvet, ikke fra et mødelokale."),
            ("Et par års erfaring med en ledende eller koordinerende rolle af medarbejdere",
             "Tolv år som leder: 12 teknikere (ARJ), 14 medarbejdere (Ventek-Air), 5 elektrikere og "
             "3 lærlinge med fuldt P&L siden 2023 og 25 specialister koordineret i Novo-projekter."),
            ("God teknisk forståelse for produktion",
             "Maskinmester (EQF 6) med el- og maskinteknisk design; produktion, vedligehold og "
             "tekniske installationer i tyve år — fra **tegninger** og **stykliste** til færdig "
             "montage."),
            ("Erfaring med metalbearbejdning, svejsning og fremstilling af maskindele",
             "Værksted med pladeklip, bukning og samling af **maskindele** og kanaler, og "
             "produktionsværksted med **bearbejdning** af emner; **svejsning** som den proces, der "
             "blev planlagt og kontrolleret i samme flow."),
            ("Det vil være en fordel med kendskab til drejning og spåntagende bearbejdning",
             "**Drejning** og **spåntagende bearbejdning** kendt som bestiller og kontrollør: "
             "tolerancer, overflader og hvad der kan laves i én opspænding — og hvad der skal sendes "
             "ud, når det ikke kan."),
            ("Erfaring fra en projektorienteret produktionsvirksomhed, hvor prioriteringer ændrer sig undervejs",
             "**Projektorienteret** produktion i tolv år: 11 entrepriser á 2–10 mio. kr. og 37 "
             "CAPEX-projekter, hvor rækkefølgen flyttede sig midt i ugen og nogen skulle beslutte "
             "det."),
            ("Trives med at være tæt på medarbejderne, lytte til input og træffe beslutninger",
             "På gulvet, ikke på kontoret: oplæring, **MUS** og daglig sparring med medarbejdere, "
             "og beslutninger taget på stedet med en dato og et navn."),
            ("Arbejder struktureret, er løsningsorienteret og har forståelse for samarbejdets betydning",
             "**KS**-tjeklister pr. ordre, **A3** på gentagne fejl og **Lean** i praksis — 5S, "
             "tavlemøder og standardarbejde med 40 procent højere produktivitet."),
            ("Ud over selv at deltage i produktionen",
             "Deltager i arbejdet, hvor der er brug for det: i egen virksomhed blev der lagt hænder "
             "på, når dagen krævede det, og i værkstedet blev maskiner og værktøj brugt dagligt."),
            ("Sikkerhed og orden som en del af den daglige drift",
             "**Sikkerhed** gennem fire år i 24/7-drift med LOTO, APV og siden hen sikkerhedsrundering;"
             " faste pladser og mærkede emner er en forudsætning for både fart og kvalitet."),
            ("Kendskab til ERP og opfølgning på ordrer",
             "Ordre, tid og materiale fulgt i **SAP** på Novo-projekterne og i egne værktøjer i "
             "ELOHVAC — tal, der kan læses af andre end den, der lavede dem."),
        ],
        widths=(3600, 6746))

    m.section("ET VÆRKSTED ER ET LØFTE, IKKE EN MASKINE")
    m.para("En maskinfabrik er ikke hurtig, fordi den har de rigtige maskiner, men fordi emnerne "
           "kommer i den rigtige rækkefølge gennem dem. Det er koordinatorens arbejde: at se, hvor "
           "emnet står stille lige nu, og flytte beslutningen derhen, hvor den kan tages i dag. Det "
           "kræver, at man kender processerne nok til at vide, hvad der kan laves om, og hvad der "
           "skal laves forfra — og at man er på gulvet, når spørgsmålet bliver stillet, fordi det "
           "spørgsmål ikke venter til næste møde.", after=0)

    m.save(path)


if __name__ == '__main__':
    build(os.path.join(ROOT, 'Shahram_Ajloo_LachenmeierMonsun_Teamkoordinator.docx'))
    print(os.path.join(ROOT, 'Shahram_Ajloo_LachenmeierMonsun_Teamkoordinator.docx'))
