from pathlib import Path


WIDTH = 1080
HEIGHT = 1920


def header(title: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0b1220"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="phoneBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#111827"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="cta" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#06b6d4"/>
      <stop offset="100%" stop-color="#3b82f6"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#000000" flood-opacity="0.45"/>
    </filter>
    <style>
      .h1 {{ font: 700 44px Arial, sans-serif; fill: #e2e8f0; }}
      .h2 {{ font: 500 24px Arial, sans-serif; fill: #93c5fd; }}
      .h3 {{ font: 700 36px Arial, sans-serif; fill: #f8fafc; }}
      .label {{ font: 600 22px Arial, sans-serif; fill: #cbd5e1; }}
      .text {{ font: 20px Arial, sans-serif; fill: #cbd5e1; }}
      .small {{ font: 18px Arial, sans-serif; fill: #94a3b8; }}
      .btn {{ font: 700 21px Arial, sans-serif; fill: #ffffff; }}
      .phone {{ fill: url(#phoneBg); stroke: #334155; stroke-width: 4; rx: 48; filter: url(#shadow); }}
      .notch {{ fill: #0b1220; rx: 10; }}
      .card {{ fill: #0f172a; stroke: #334155; stroke-width: 2; rx: 20; }}
      .field {{ fill: #111827; stroke: #475569; stroke-width: 2; rx: 12; }}
      .chip {{ fill: #1e293b; stroke: #475569; stroke-width: 1; rx: 12; }}
      .cta {{ fill: url(#cta); rx: 16; }}
      .soft {{ fill: #13263b; stroke: #1d4ed8; stroke-width: 1; rx: 12; }}
      .warn {{ fill: #2a1a10; stroke: #f59e0b; stroke-width: 1; rx: 12; }}
      .ok {{ fill: #062a2e; stroke: #22d3ee; stroke-width: 1; rx: 12; }}
      .icon {{ fill: #38bdf8; }}
    </style>
  </defs>
  <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bg)"/>
  <text x="60" y="90" class="h1">Smart Health Assistant</text>
  <text x="60" y="126" class="h2">{title}</text>
  <rect x="270" y="160" width="540" height="1640" class="phone"/>
  <rect x="458" y="178" width="164" height="20" class="notch"/>
"""


def footer() -> str:
    return "</svg>\n"


def write(path: Path, title: str, body: str) -> None:
    path.write_text(header(title) + body + footer(), encoding="utf-8")


def main() -> None:
    out = Path("mockups-premium")
    out.mkdir(exist_ok=True)

    data = {
        "screen01-onboarding.svg": (
            "Premium 01 - Registracija in profil",
            """
  <text x="330" y="258" class="h3">Ustvari profil</text>
  <rect x="320" y="292" width="440" height="1280" class="card"/>
  <circle cx="380" cy="345" r="18" class="icon"/><text x="410" y="352" class="label">Osebni podatki</text>
  <rect x="350" y="380" width="380" height="58" class="field"/><text x="368" y="416" class="small">Ime in priimek</text>
  <rect x="350" y="452" width="182" height="58" class="field"/><text x="368" y="488" class="small">Starost</text>
  <rect x="548" y="452" width="182" height="58" class="field"/><text x="566" y="488" class="small">Spol</text>
  <rect x="350" y="524" width="182" height="58" class="field"/><text x="368" y="560" class="small">Višina</text>
  <rect x="548" y="524" width="182" height="58" class="field"/><text x="566" y="560" class="small">Teža</text>
  <rect x="350" y="596" width="380" height="58" class="field"/><text x="368" y="632" class="small">Alergije</text>
  <rect x="350" y="668" width="380" height="120" class="field"/><text x="368" y="706" class="small">Kronične težave</text>
  <rect x="350" y="804" width="380" height="90" class="field"/><text x="368" y="854" class="small">Trenutna zdravila (opcijsko)</text>
  <rect x="350" y="920" width="380" height="72" class="cta"/><text x="470" y="964" class="btn">Shrani profil</text>
  <rect x="350" y="1010" width="380" height="84" class="warn"/><text x="368" y="1060" class="small">Podpora uporabniku, ne diagnoza.</text>
""",
        ),
        "screen02-dashboard.svg": (
            "Premium 02 - Nadzorna plošča",
            """
  <text x="330" y="258" class="h3">Dobrodošel nazaj</text>
  <rect x="320" y="292" width="440" height="1300" class="card"/>
  <rect x="350" y="330" width="380" height="110" class="soft"/>
  <text x="370" y="372" class="text">2 aktivna opomnika</text><text x="370" y="404" class="small">Zadnji vnos: pred 3 urami</text>
  <rect x="350" y="458" width="180" height="82" class="card"/><text x="388" y="507" class="small">Dodaj simptom</text>
  <rect x="550" y="458" width="180" height="82" class="card"/><text x="592" y="507" class="small">Dodaj meritev</text>
  <rect x="350" y="554" width="180" height="82" class="card"/><text x="412" y="603" class="small">Zdravila</text>
  <rect x="550" y="554" width="180" height="82" class="card"/><text x="620" y="603" class="small">OCR</text>
  <rect x="350" y="654" width="380" height="260" class="field"/>
  <text x="370" y="694" class="label">Dnevni povzetek</text>
  <text x="370" y="730" class="small">Počutje: dobro</text>
  <text x="370" y="760" class="small">Temperatura: 36.8 C</text>
  <text x="370" y="790" class="small">Srčni utrip: 72 bpm</text>
  <text x="370" y="820" class="small">Predlog: odpri AI povzetek</text>
  <rect x="350" y="940" width="380" height="66" class="soft"/><text x="388" y="980" class="small">Domov  Zgodovina  Zdravila  Nastavitve</text>
""",
        ),
        "screen03-symptom-voice.svg": (
            "Premium 03 - Simptomi + govorni vnos",
            """
  <text x="330" y="258" class="h3">Vnos simptomov</text>
  <rect x="320" y="292" width="440" height="1300" class="card"/>
  <rect x="350" y="340" width="380" height="58" class="field"/><text x="368" y="376" class="small">Datum in čas</text>
  <rect x="350" y="412" width="380" height="156" class="field"/><text x="368" y="462" class="small">Opis simptomov...</text>
  <rect x="350" y="582" width="380" height="58" class="field"/><text x="368" y="618" class="small">Intenzivnost 1-10</text>
  <rect x="350" y="654" width="120" height="44" class="chip"/><text x="386" y="682" class="small">Slabo</text>
  <rect x="480" y="654" width="120" height="44" class="chip"/><text x="530" y="682" class="small">OK</text>
  <rect x="610" y="654" width="120" height="44" class="chip"/><text x="648" y="682" class="small">Dobro</text>
  <rect x="350" y="712" width="380" height="124" class="field"/><text x="368" y="762" class="small">Dodatne opombe...</text>
  <rect x="350" y="854" width="180" height="66" class="soft"/><text x="386" y="895" class="small">Govorni vnos</text>
  <rect x="550" y="854" width="180" height="66" class="cta"/><text x="614" y="895" class="btn">Shrani</text>
  <rect x="350" y="938" width="380" height="84" class="ok"/><text x="368" y="988" class="small">Speech-to-Text: aktivno</text>
""",
        ),
        "screen04-measurements.svg": (
            "Premium 04 - Meritve",
            """
  <text x="330" y="258" class="h3">Zdravstvene meritve</text>
  <rect x="320" y="292" width="440" height="1300" class="card"/>
  <rect x="350" y="340" width="380" height="58" class="field"/><text x="368" y="376" class="small">Temperatura (C)</text>
  <rect x="350" y="412" width="380" height="58" class="field"/><text x="368" y="448" class="small">Srčni utrip (bpm)</text>
  <rect x="350" y="484" width="380" height="58" class="field"/><text x="368" y="520" class="small">Krvni tlak</text>
  <rect x="350" y="556" width="380" height="58" class="field"/><text x="368" y="592" class="small">Počutje</text>
  <rect x="350" y="628" width="380" height="132" class="field"/><text x="368" y="678" class="small">Opombe...</text>
  <rect x="350" y="780" width="380" height="70" class="cta"/><text x="470" y="824" class="btn">Shrani meritev</text>
  <rect x="350" y="868" width="380" height="100" class="soft"/><text x="368" y="916" class="small">Shranjevanje v Room (offline).</text>
""",
        ),
        "screen05-medications-reminders.svg": (
            "Premium 05 - Zdravila in opomniki",
            """
  <text x="330" y="258" class="h3">Zdravila</text>
  <rect x="320" y="292" width="440" height="1300" class="card"/>
  <rect x="350" y="336" width="380" height="66" class="cta"/><text x="458" y="378" class="btn">+ Dodaj zdravilo</text>
  <rect x="350" y="420" width="380" height="180" class="field"/>
  <text x="370" y="462" class="label">Lekadol 500mg</text>
  <text x="370" y="492" class="small">1 tableta | 08:00, 20:00</text>
  <rect x="620" y="444" width="88" height="34" class="ok"/><text x="648" y="466" class="small">ON</text>
  <text x="370" y="528" class="small">Uredi  Izbrisi  Opomniki</text>
  <rect x="350" y="618" width="380" height="180" class="field"/>
  <text x="370" y="660" class="label">Vitamin D</text>
  <text x="370" y="690" class="small">1 kapsula | 09:00</text>
  <rect x="620" y="642" width="88" height="34" class="ok"/><text x="648" y="664" class="small">ON</text>
  <text x="370" y="726" class="small">Uredi  Izbrisi  Opomniki</text>
  <rect x="350" y="820" width="380" height="90" class="warn"/><text x="368" y="872" class="small">Odvisno od dovoljenj obvestil.</text>
""",
        ),
        "screen06-api-info.svg": (
            "Premium 06 - API informacije",
            """
  <text x="330" y="258" class="h3">Informacije o zdravilu</text>
  <rect x="320" y="292" width="440" height="1300" class="card"/>
  <rect x="350" y="338" width="280" height="56" class="field"/><text x="368" y="374" class="small">Išči zdravilo...</text>
  <rect x="640" y="338" width="90" height="56" class="cta"/><text x="658" y="374" class="btn">Išči</text>
  <rect x="350" y="412" width="380" height="360" class="field"/>
  <text x="370" y="452" class="label">OpenFDA rezultat</text>
  <text x="370" y="486" class="small">Učinkovina: paracetamol</text>
  <text x="370" y="516" class="small">Indikacije: bolečina, vročina</text>
  <text x="370" y="546" class="small">Opozorila: ne prekorači odmerka</text>
  <text x="370" y="576" class="small">Vir: api.fda.gov</text>
  <rect x="350" y="790" width="380" height="100" class="soft"/><text x="368" y="842" class="small">Repository: cache -> API fallback.</text>
  <rect x="350" y="908" width="380" height="90" class="warn"/><text x="368" y="960" class="small">Ob izpadu interneta: zadnji cache.</text>
""",
        ),
        "screen07-ocr-scan.svg": (
            "Premium 07 - OCR skeniranje",
            """
  <text x="330" y="258" class="h3">OCR skeniranje</text>
  <rect x="320" y="292" width="440" height="1300" class="card"/>
  <rect x="350" y="338" width="380" height="360" class="field"/>
  <text x="466" y="530" class="small">Predogled kamere</text>
  <rect x="350" y="716" width="380" height="66" class="cta"/><text x="470" y="758" class="btn">Zajemi sliko</text>
  <rect x="350" y="800" width="380" height="230" class="field"/>
  <text x="370" y="842" class="label">Prepoznano besedilo</text>
  <text x="370" y="878" class="small">LEKADOL 500 mg</text>
  <text x="370" y="906" class="small">Paracetamol</text>
  <text x="370" y="934" class="small">Zaupanje: 92%</text>
  <rect x="350" y="1048" width="180" height="64" class="soft"/><text x="410" y="1088" class="small">Ponovi</text>
  <rect x="550" y="1048" width="180" height="64" class="cta"/><text x="568" y="1088" class="btn">Ustvari zdravilo</text>
""",
        ),
        "screen08-ai-summary.svg": (
            "Premium 08 - AI povzetek",
            """
  <text x="330" y="258" class="h3">AI povzetek</text>
  <rect x="320" y="292" width="440" height="1300" class="card"/>
  <rect x="350" y="338" width="380" height="420" class="field"/>
  <text x="370" y="382" class="label">Povzetek zadnjih 7 dni</text>
  <text x="370" y="418" class="small">- Pogosti glavoboli (4 vnosi)</text>
  <text x="370" y="448" class="small">- Povprečna temperatura: 36.9 C</text>
  <text x="370" y="478" class="small">- Jemanje zdravil: 93%</text>
  <text x="370" y="522" class="label">Priporočilo</text>
  <text x="370" y="556" class="small">Nadaljuj z rednim spremljanjem.</text>
  <text x="370" y="584" class="small">V primeru poslabšanja kontaktiraj zdravnika.</text>
  <rect x="350" y="776" width="380" height="66" class="cta"/><text x="470" y="818" class="btn">Osveži povzetek</text>
  <rect x="350" y="860" width="380" height="96" class="warn"/><text x="368" y="914" class="small">AI je informativen, ni diagnoza.</text>
""",
        ),
        "screen09-history-offline.svg": (
            "Premium 09 - Zgodovina in offline",
            """
  <text x="330" y="258" class="h3">Zgodovina vnosov</text>
  <rect x="320" y="292" width="440" height="1300" class="card"/>
  <rect x="350" y="338" width="380" height="54" class="field"/><text x="368" y="372" class="small">Filter: Dan | Teden | Mesec</text>
  <rect x="350" y="406" width="380" height="54" class="field"/><text x="368" y="440" class="small">Iskanje...</text>
  <rect x="350" y="478" width="380" height="430" class="field"/>
  <text x="370" y="518" class="small">21.04 08:00  Simptom: glavobol (5/10)</text>
  <text x="370" y="548" class="small">21.04 08:05  Meritev: 36.8 C, 72 bpm</text>
  <text x="370" y="578" class="small">21.04 09:00  Zdravilo: Vitamin D</text>
  <text x="370" y="608" class="small">20.04 20:00  Zdravilo: Lekadol</text>
  <rect x="350" y="926" width="380" height="88" class="ok"/><text x="368" y="976" class="small">Offline način: aktiven</text>
  <rect x="350" y="1032" width="380" height="88" class="soft"/><text x="368" y="1082" class="small">API cache posodobljen 20:15</text>
""",
        ),
        "screen10-settings-multilingual.svg": (
            "Premium 10 - Nastavitve in jeziki",
            """
  <text x="330" y="258" class="h3">Nastavitve</text>
  <rect x="320" y="292" width="440" height="1300" class="card"/>
  <rect x="350" y="340" width="380" height="58" class="field"/><text x="368" y="376" class="small">Jezik: Slovenščina / English</text>
  <rect x="350" y="412" width="380" height="58" class="field"/><text x="368" y="448" class="small">Tema: Svetla / Temna</text>
  <rect x="350" y="484" width="380" height="58" class="field"/><text x="368" y="520" class="small">Obvestila: ON/OFF</text>
  <rect x="350" y="556" width="380" height="58" class="field"/><text x="368" y="592" class="small">Zasebni način: ON/OFF</text>
  <rect x="350" y="628" width="380" height="58" class="field"/><text x="368" y="664" class="small">Izvoz podatkov</text>
  <rect x="350" y="710" width="380" height="72" class="cta"/><text x="470" y="754" class="btn">Shrani spremembe</text>
  <rect x="350" y="800" width="380" height="96" class="ok"/><text x="368" y="854" class="small">Lokalizacija pripravljena za 2 jezika.</text>
""",
        ),
    }

    for name, (title, body) in data.items():
        write(out / name, title, body)

    print(f"Generated {len(data)} premium SVG mockups in {out}")


if __name__ == "__main__":
    main()
