# Prototipna dokumentacija (V2)

**Predmet:** Tehnologije za vseprisotne aplikacije  
**Projekt:** Smart Health Assistant  
**Študijsko leto:** 2025/2026  
**Vodja ekipe:** Tanej Buhin  
**Datum:** 21. 4. 2026

---

## 1. Uvod

Ta dokument je GitHub-ready različica prototipne dokumentacije za aplikacijo **Smart Health Assistant**.

Vsebuje:
- diagram primerov uporabe,
- E-R diagram podatkovne baze,
- prototipe zaslonskih mask (10 ločenih SVG zaslonov).

Aplikacija je namenjena podpori pri samonadzoru zdravja in ne nadomešča medicinske diagnoze.

---

## 2. Diagram primerov uporabe

![Use Case diagram](./usecase.svg)

Vir: `usecase.mmd`

---

## 3. E-R diagram podatkovne baze

![E-R diagram](./er.svg)

Vir: `er.mmd`

---

## 4. Navigacijski tok aplikacije

![Navigacijski tok](./navigation.svg)

Vir: `navigation.mmd`

---

## 5. Premium prototipi zaslonskih mask

Spodaj je 10 ločenih zaslonov, ki skupaj pokrijejo vse funkcionalnosti iz priprave projekta.

### 5.1 Registracija in zdravstveni profil
![Registracija in profil](./mockups-premium/screen01-onboarding.svg)

### 5.2 Nadzorna plošča
![Nadzorna plošča](./mockups-premium/screen02-dashboard.svg)

### 5.3 Beleženje simptomov in govorni vnos
![Simptomi in govorni vnos](./mockups-premium/screen03-symptom-voice.svg)

### 5.4 Vnos meritev
![Meritve](./mockups-premium/screen04-measurements.svg)

### 5.5 Upravljanje zdravil in opomniki
![Zdravila in opomniki](./mockups-premium/screen05-medications-reminders.svg)

### 5.6 Pridobivanje informacij iz zunanjega API
![API informacije](./mockups-premium/screen06-api-info.svg)

### 5.7 OCR skeniranje embalaže/navodil
![OCR skeniranje](./mockups-premium/screen07-ocr-scan.svg)

### 5.8 AI povzetek uporabniškega stanja
![AI povzetek](./mockups-premium/screen08-ai-summary.svg)

### 5.9 Zgodovina vnosov in offline predpomnjenje
![Zgodovina in offline](./mockups-premium/screen09-history-offline.svg)

### 5.10 Večjezični vmesnik in nastavitve
![Nastavitve in jeziki](./mockups-premium/screen10-settings-multilingual.svg)

---

## 6. Pokritost funkcionalnosti

V tej prototipni dokumentaciji so jasno pokrite naslednje funkcionalnosti:

1. Registracija uporabnika in urejanje zdravstvenega profila  
2. Beleženje simptomov, počutja in osnovnih meritev  
3. Upravljanje zdravil in opomniki za jemanje  
4. Lokalno shranjevanje podatkov (Room)  
5. Pridobivanje zdravstvenih informacij iz spletnega API  
6. Glasovni vnos simptomov (Speech-to-Text)  
7. OCR skeniranje embalaže/navodil zdravil  
8. AI povzetek uporabniškega stanja/priporočil  
9. Predpomnjenje podatkov in osnovno offline delovanje  
10. Večjezični uporabniški vmesnik in prilagodljive nastavitve

---

## 7. Tehnološki okvir

Predvidene tehnologije:
- `Kotlin`, `Android Studio`
- `Room` (lokalna baza)
- `Retrofit` (API komunikacija)
- `SpeechRecognizer` (glasovni vnos)
- `ML Kit OCR` (prepoznava besedila)
- zunanja AI/LLM storitev (AI povzetki)

---

## 8. Zaključek

Dokument predstavlja celovit prototipni paket (diagrami + zasloni) in je pripravljen za objavo v GitHub repozitoriju ali pretvorbo v PDF.
