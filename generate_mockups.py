from pathlib import Path


WIDTH = 1080
HEIGHT = 1920


def svg_header(title: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#e0f2fe"/>
      <stop offset="100%" stop-color="#f8fafc"/>
    </linearGradient>
    <linearGradient id="primaryGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0ea5e9"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#0f172a" flood-opacity="0.18"/>
    </filter>
    <style>
      .title {{ font: 700 44px Arial, sans-serif; fill: #0f172a; }}
      .subtitle {{ font: 500 24px Arial, sans-serif; fill: #334155; }}
      .screenTitle {{ font: 700 38px Arial, sans-serif; fill: #0f172a; }}
      .label {{ font: 600 22px Arial, sans-serif; fill: #1e293b; }}
      .text {{ font: 20px Arial, sans-serif; fill: #334155; }}
      .small {{ font: 18px Arial, sans-serif; fill: #475569; }}
      .btnText {{ font: 700 22px Arial, sans-serif; fill: #ffffff; }}
      .chipText {{ font: 600 18px Arial, sans-serif; fill: #0f172a; }}
      .card {{ fill: #ffffff; stroke: #dbeafe; stroke-width: 2; rx: 22; filter: url(#shadow); }}
      .field {{ fill: #f8fafc; stroke: #cbd5e1; stroke-width: 2; rx: 14; }}
      .chip {{ fill: #e2e8f0; stroke: #cbd5e1; stroke-width: 1; rx: 12; }}
      .phone {{ fill: #f8fafc; stroke: #0f172a; stroke-width: 4; rx: 46; }}
      .notch {{ fill: #0f172a; rx: 12; }}
      .cta {{ fill: url(#primaryGrad); rx: 16; }}
      .section {{ fill: #eef2ff; stroke: #bfdbfe; stroke-width: 1; rx: 14; }}
      .badge {{ fill: #dbeafe; stroke: #93c5fd; stroke-width: 1; rx: 10; }}
      .warn {{ fill: #fff7ed; stroke: #fdba74; stroke-width: 1; rx: 10; }}
      .ok {{ fill: #ecfeff; stroke: #67e8f9; stroke-width: 1; rx: 10; }}
    </style>
  </defs>
  <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bgGrad)"/>
  <text x="60" y="90" class="title">Smart Health Assistant</text>
  <text x="60" y="126" class="subtitle">{title}</text>
  <rect x="270" y="160" width="540" height="1640" class="phone"/>
  <rect x="455" y="178" width="170" height="22" class="notch"/>
"""


def svg_footer() -> str:
    return "</svg>\n"


def write_svg(path: Path, body: str, title: str) -> None:
    path.write_text(svg_header(title) + body + svg_footer(), encoding="utf-8")


def main() -> None:
    out_dir = Path("mockups")
    out_dir.mkdir(exist_ok=True)

    screens = {
        "screen01-onboarding.svg": (
            "01 - Registracija in zdravstveni profil",
            """
  <text x="330" y="260" class="screenTitle">Ustvari svoj profil</text>
  <rect x="320" y="300" width="440" height="1270" class="card"/>
  <text x="350" y="350" class="label">Ime in priimek</text>
  <rect x="350" y="365" width="380" height="60" class="field"/>
  <text x="350" y="455" class="label">Starost</text>
  <rect x="350" y="470" width="180" height="60" class="field"/>
  <text x="550" y="455" class="label">Spol</text>
  <rect x="550" y="470" width="180" height="60" class="field"/>
  <text x="350" y="560" class="label">Visina (cm)</text>
  <rect x="350" y="575" width="180" height="60" class="field"/>
  <text x="550" y="560" class="label">Teza (kg)</text>
  <rect x="550" y="575" width="180" height="60" class="field"/>
  <text x="350" y="665" class="label">Alergije</text>
  <rect x="350" y="680" width="380" height="60" class="field"/>
  <text x="350" y="770" class="label">Kronicne tezave</text>
  <rect x="350" y="785" width="380" height="140" class="field"/>
  <text x="350" y="965" class="label">Seznam zdravil (opcijsko)</text>
  <rect x="350" y="980" width="380" height="120" class="field"/>
  <rect x="350" y="1135" width="380" height="72" class="cta"/>
  <text x="465" y="1180" class="btnText">Shrani profil</text>
  <rect x="350" y="1230" width="380" height="82" class="warn"/>
  <text x="368" y="1268" class="small">Aplikacija ne postavlja diagnoz.</text>
""",
        ),
        "screen02-dashboard.svg": (
            "02 - Nadzorna plosca",
            """
  <text x="330" y="260" class="screenTitle">Pozdravljen, Tanej</text>
  <rect x="320" y="295" width="440" height="120" class="card"/>
  <rect x="345" y="325" width="190" height="34" class="badge"/>
  <text x="360" y="348" class="small">2 aktivna opomnika</text>
  <rect x="545" y="325" width="185" height="34" class="ok"/>
  <text x="560" y="348" class="small">Zadnji vnos pred 3h</text>
  <rect x="320" y="435" width="210" height="86" class="card"/>
  <text x="355" y="485" class="text">Dodaj simptom</text>
  <rect x="550" y="435" width="210" height="86" class="card"/>
  <text x="590" y="485" class="text">Dodaj meritev</text>
  <rect x="320" y="535" width="210" height="86" class="card"/>
  <text x="375" y="585" class="text">Zdravila</text>
  <rect x="550" y="535" width="210" height="86" class="card"/>
  <text x="615" y="585" class="text">OCR</text>
  <rect x="320" y="640" width="440" height="260" class="card"/>
  <text x="350" y="685" class="label">Dnevni povzetek</text>
  <text x="350" y="730" class="text">Pocutje: dobro</text>
  <text x="350" y="765" class="text">Temperatura: 36.8 C</text>
  <text x="350" y="800" class="text">Srcni utrip: 72 bpm</text>
  <text x="350" y="835" class="small">Predlog: osvezi AI povzetek</text>
  <rect x="320" y="920" width="440" height="74" class="section"/>
  <text x="365" y="965" class="small">Domov   Zgodovina   Zdravila   Nastavitve</text>
""",
        ),
        "screen03-symptom-voice.svg": (
            "03 - Belezenje simptomov in govorni vnos",
            """
  <text x="330" y="260" class="screenTitle">Nov vnos simptomov</text>
  <rect x="320" y="295" width="440" height="1220" class="card"/>
  <text x="350" y="345" class="label">Datum in cas</text>
  <rect x="350" y="360" width="380" height="60" class="field"/>
  <text x="350" y="450" class="label">Opis simptomov</text>
  <rect x="350" y="465" width="380" height="170" class="field"/>
  <text x="350" y="665" class="label">Intenzivnost (1-10)</text>
  <rect x="350" y="680" width="380" height="60" class="field"/>
  <text x="350" y="770" class="label">Pocutje</text>
  <rect x="350" y="785" width="110" height="46" class="chip"/><text x="385" y="814" class="chipText">Slabo</text>
  <rect x="475" y="785" width="110" height="46" class="chip"/><text x="520" y="814" class="chipText">OK</text>
  <rect x="600" y="785" width="130" height="46" class="chip"/><text x="636" y="814" class="chipText">Dobro</text>
  <text x="350" y="875" class="label">Opombe</text>
  <rect x="350" y="890" width="380" height="120" class="field"/>
  <rect x="350" y="1040" width="180" height="68" class="section"/>
  <text x="377" y="1080" class="text">Govorni vnos</text>
  <rect x="550" y="1040" width="180" height="68" class="cta"/>
  <text x="617" y="1080" class="btnText">Shrani</text>
  <rect x="350" y="1130" width="380" height="92" class="ok"/>
  <text x="370" y="1170" class="small">Mikrofon: aktiviran (Speech-to-Text)</text>
""",
        ),
        "screen04-measurements.svg": (
            "04 - Meritve in zdravstveni podatki",
            """
  <text x="330" y="260" class="screenTitle">Dodaj meritev</text>
  <rect x="320" y="295" width="440" height="1220" class="card"/>
  <text x="350" y="345" class="label">Telesna temperatura (C)</text>
  <rect x="350" y="360" width="380" height="60" class="field"/>
  <text x="350" y="450" class="label">Srcni utrip (bpm)</text>
  <rect x="350" y="465" width="380" height="60" class="field"/>
  <text x="350" y="555" class="label">Krvni tlak</text>
  <rect x="350" y="570" width="380" height="60" class="field"/>
  <text x="350" y="660" class="label">Razpolozenje</text>
  <rect x="350" y="675" width="380" height="60" class="field"/>
  <text x="350" y="765" class="label">Dodatne opombe</text>
  <rect x="350" y="780" width="380" height="170" class="field"/>
  <rect x="350" y="980" width="380" height="72" class="cta"/>
  <text x="500" y="1025" class="btnText">Shrani meritev</text>
  <rect x="350" y="1070" width="380" height="130" class="section"/>
  <text x="370" y="1110" class="small">Podatki se shranijo lokalno v Room DB.</text>
  <text x="370" y="1140" class="small">Zgodovina je na voljo tudi offline.</text>
""",
        ),
        "screen05-medications-reminders.svg": (
            "05 - Upravljanje zdravil in opomniki",
            """
  <text x="330" y="260" class="screenTitle">Zdravila in opomniki</text>
  <rect x="320" y="295" width="440" height="1220" class="card"/>
  <rect x="350" y="335" width="380" height="64" class="cta"/>
  <text x="460" y="376" class="btnText">+ Dodaj zdravilo</text>
  <rect x="350" y="420" width="380" height="180" class="field"/>
  <text x="372" y="462" class="label">Lekadol 500mg</text>
  <text x="372" y="495" class="text">Odmerek: 1 tableta</text>
  <text x="372" y="528" class="text">Ura: 08:00, 20:00</text>
  <rect x="610" y="445" width="100" height="34" class="badge"/><text x="628" y="468" class="small">ON</text>
  <text x="372" y="562" class="small">Uredi | Izbrisi | Dnevni opomnik</text>
  <rect x="350" y="620" width="380" height="180" class="field"/>
  <text x="372" y="662" class="label">Vitamin D</text>
  <text x="372" y="695" class="text">Odmerek: 1 kapsula</text>
  <text x="372" y="728" class="text">Ura: 09:00</text>
  <rect x="610" y="645" width="100" height="34" class="badge"/><text x="628" y="668" class="small">ON</text>
  <text x="372" y="762" class="small">Uredi | Izbrisi | Tedenski opomnik</text>
  <rect x="350" y="835" width="380" height="130" class="ok"/>
  <text x="370" y="875" class="small">Opomniki uporabljajo sistemska obvestila.</text>
  <text x="370" y="905" class="small">Delovanje je odvisno od dovoljenj naprave.</text>
""",
        ),
        "screen06-api-info.svg": (
            "06 - Pridobivanje informacij iz API",
            """
  <text x="330" y="260" class="screenTitle">Informacije o zdravilu (API)</text>
  <rect x="320" y="295" width="440" height="1220" class="card"/>
  <text x="350" y="345" class="label">Isci zdravilo</text>
  <rect x="350" y="360" width="280" height="60" class="field"/>
  <rect x="640" y="360" width="90" height="60" class="cta"/>
  <text x="658" y="397" class="btnText">Isci</text>
  <rect x="350" y="445" width="380" height="350" class="field"/>
  <text x="372" y="485" class="label">OpenFDA rezultat</text>
  <text x="372" y="520" class="small">Ucinkovina: paracetamol</text>
  <text x="372" y="550" class="small">Indikacije: blage bolecine, vrocina</text>
  <text x="372" y="580" class="small">Opozorila: ne prekoraci odmerka</text>
  <text x="372" y="610" class="small">Interakcije: preveri navodilo</text>
  <text x="372" y="640" class="small">Vir: api.fda.gov</text>
  <rect x="350" y="825" width="380" height="120" class="section"/>
  <text x="370" y="865" class="small">Repository: najprej lokalni cache, nato API.</text>
  <text x="370" y="895" class="small">Zadnja osvezitev: 21.04.2026 20:15</text>
  <rect x="350" y="970" width="380" height="90" class="warn"/>
  <text x="370" y="1010" class="small">Ce API ni dosegljiv, prikazi zadnje podatke.</text>
""",
        ),
        "screen07-ocr-scan.svg": (
            "07 - OCR skeniranje embalaze/navodil",
            """
  <text x="330" y="260" class="screenTitle">OCR skeniranje zdravila</text>
  <rect x="320" y="295" width="440" height="1220" class="card"/>
  <rect x="350" y="335" width="380" height="360" class="field"/>
  <text x="465" y="525" class="text">Kamera predogled</text>
  <rect x="350" y="720" width="380" height="64" class="cta"/>
  <text x="468" y="761" class="btnText">Zajemi sliko</text>
  <text x="350" y="825" class="label">Prepoznano besedilo</text>
  <rect x="350" y="840" width="380" height="220" class="field"/>
  <text x="372" y="880" class="small">LEKADOL 500 mg</text>
  <text x="372" y="910" class="small">Paracetamol</text>
  <text x="372" y="940" class="small">Navodilo: 1 tableta na 8 ur</text>
  <text x="372" y="970" class="small">Zaupanje OCR: 92%</text>
  <rect x="350" y="1085" width="180" height="64" class="section"/>
  <text x="387" y="1125" class="text">Ponovi</text>
  <rect x="550" y="1085" width="180" height="64" class="cta"/>
  <text x="570" y="1125" class="btnText">Ustvari zdravilo</text>
""",
        ),
        "screen08-ai-summary.svg": (
            "08 - AI povzetek stanja",
            """
  <text x="330" y="260" class="screenTitle">AI povzetek (7 dni)</text>
  <rect x="320" y="295" width="440" height="1220" class="card"/>
  <rect x="350" y="340" width="380" height="390" class="field"/>
  <text x="372" y="382" class="label">Povzetek</text>
  <text x="372" y="420" class="small">- Pogosti glavoboli (4 vnosi)</text>
  <text x="372" y="450" class="small">- Povprecna temperatura: 36.9 C</text>
  <text x="372" y="480" class="small">- Redno jemanje zdravil: 93%</text>
  <text x="372" y="530" class="label">Priporocilo</text>
  <text x="372" y="565" class="small">Nadaljuj z rednim vnosom simptomov.</text>
  <text x="372" y="595" class="small">V primeru poslabanja kontaktiraj zdravnika.</text>
  <rect x="350" y="755" width="380" height="64" class="cta"/>
  <text x="468" y="796" class="btnText">Osvezi povzetek</text>
  <rect x="350" y="840" width="380" height="110" class="warn"/>
  <text x="370" y="880" class="small">AI odgovor je informativen in ni diagnoza.</text>
  <text x="370" y="910" class="small">Model: zunanji LLM API</text>
""",
        ),
        "screen09-history-offline.svg": (
            "09 - Zgodovina in offline predpomnjenje",
            """
  <text x="330" y="260" class="screenTitle">Zgodovina vnosov</text>
  <rect x="320" y="295" width="440" height="1220" class="card"/>
  <rect x="350" y="335" width="380" height="54" class="field"/>
  <text x="372" y="368" class="small">Filter: Dan | Teden | Mesec</text>
  <rect x="350" y="405" width="380" height="54" class="field"/>
  <text x="372" y="438" class="small">Iskanje po simptomu ali zdravilu...</text>
  <rect x="350" y="480" width="380" height="420" class="field"/>
  <text x="372" y="520" class="small">21.04.2026 08:00  Simptom: glavobol (5/10)</text>
  <text x="372" y="550" class="small">21.04.2026 08:05  Meritev: 36.8 C, 72 bpm</text>
  <text x="372" y="580" class="small">21.04.2026 09:00  Zdravilo: Vitamin D</text>
  <text x="372" y="610" class="small">20.04.2026 20:00  Zdravilo: Lekadol</text>
  <text x="372" y="640" class="small">...</text>
  <rect x="350" y="925" width="380" height="90" class="ok"/>
  <text x="370" y="965" class="small">Offline nacin: aktiven (lokalni Room podatki)</text>
  <rect x="350" y="1035" width="380" height="90" class="section"/>
  <text x="370" y="1075" class="small">API cache: zadnja sinhronizacija 20:15</text>
""",
        ),
        "screen10-settings-multilingual.svg": (
            "10 - Vecjezicni vmesnik in nastavitve",
            """
  <text x="330" y="260" class="screenTitle">Nastavitve aplikacije</text>
  <rect x="320" y="295" width="440" height="1220" class="card"/>
  <text x="350" y="350" class="label">Jezik</text>
  <rect x="350" y="365" width="380" height="60" class="field"/>
  <text x="372" y="402" class="text">Slovenscina / English</text>
  <text x="350" y="470" class="label">Tema</text>
  <rect x="350" y="485" width="380" height="60" class="field"/>
  <text x="372" y="522" class="text">Svetla / Temna</text>
  <text x="350" y="590" class="label">Obvestila</text>
  <rect x="350" y="605" width="380" height="60" class="field"/>
  <text x="372" y="642" class="text">Opomniki vklopljeni</text>
  <text x="350" y="710" class="label">Zasebni nacin</text>
  <rect x="350" y="725" width="380" height="60" class="field"/>
  <text x="372" y="762" class="text">Skrij obcutljive podatke</text>
  <rect x="350" y="830" width="380" height="64" class="section"/>
  <text x="402" y="870" class="text">Izvoz uporabniskih podatkov</text>
  <rect x="350" y="925" width="380" height="72" class="cta"/>
  <text x="470" y="970" class="btnText">Shrani spremembe</text>
  <rect x="350" y="1020" width="380" height="110" class="ok"/>
  <text x="370" y="1060" class="small">UI prevodi pripravljeni za 2 jezika.</text>
""",
        ),
    }

    for filename, (title, body) in screens.items():
        write_svg(out_dir / filename, body, title)

    print(f"Generated {len(screens)} SVG mockups in {out_dir}")


if __name__ == "__main__":
    main()
