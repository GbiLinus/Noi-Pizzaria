# NOI – Ristorante Pizzeria, Bad Rothenfelde

Website-Entwurf für die NOI Ristorante Pizzeria, Birkenstraße 2, 49214 Bad Rothenfelde. Gebaut nach dem Muster des Projekts [Collo](https://github.com/GbiLinus/Collo).

Status: **Gerüst mit Design steht.** Speisekarte, Impressum-Angaben und einige Fakten fehlen noch; alles Unbestätigte ist gelb markiert (siehe `FEHLT.md`).

## Aufbau

| Datei | Inhalt |
|---|---|
| `menu.py` | Speisekarte: Monatskarte (`SPECIALS`) + Kategorien (`MENU`), Format `(Nummer, Name, Beschreibung, Preis)`. Zurzeit nur Beispielgerichte |
| `build.py` | Baut `index.html` aus Template und Karte. **Öffnungszeiten und Telefon stehen nur hier** (Tabelle, Kurzfassung, Status-Anzeige, JSON-LD) |
| `template.html` | Seitenaufbau mit Platzhaltern `{{…}}` |
| `style.css` | Gestaltung |
| `main.js` | „Jetzt geöffnet?“, heutiger Tag, aktive Kategorie |
| `impressum.html`, `datenschutz.html` | Rechtliche Seiten (von Hand gepflegt, fehlende Angaben gelb markiert) |
| `fonts/` | League Gothic und Alegreya, lokal (SIL Open Font License, keine externen Server) |
| `FEHLT.md` | Was noch fehlt oder unsicher ist |
| `PLAN.md` | Plan, Übernahme von Collo, Akzeptanzkriterien |
| `daten/` | Gesammelte Rohdaten mit Quellen |

Karte, Zeiten oder Texte ändern: `menu.py`, `build.py` bzw. `template.html` bearbeiten, dann

```
python3 build.py
```

Lokal ansehen: `python3 -m http.server` und `http://localhost:8000` öffnen.

## Gestaltung

Die Seite ist ein Fachwerkhaus. Der Kopf der Seite ist eine Fassade: Eichenbalken bilden das Raster, die Gefache aus Kalkputz enthalten Name, Öffnungszeiten, die Tür (Anrufen) und die Adresse. Unter dem Namen sitzt die Inschrift im Balken, wie an alten Fachwerkhäusern. Balken tauchen danach nur noch als Struktur auf: Kopfleiste, Rahmen der Monatskarte, Kategorienleiste, Linien über den Abschnitten, Fuß.

| Farbe | Wert | Einsatz |
|---|---|---|
| Kalk | `#e6e5dc` | Grund, Gefache |
| Eiche | `#2e2119` | Balken, Schrift |
| Ocker | `#c4892a` | Tür, Knöpfe, Inschrift |
| Salbei | `#4a6243` | „Jetzt geöffnet“, Fokus |
| Gelb | `#f3d34a` | nur für fehlende oder unbestätigte Angaben |

Schriften: **League Gothic** (schmale Grotesk alter Kinoplakate, passend zur Deko mit Film- und Musikstars) für Titel, **Alegreya** (Buchserife) für Karte und Text. Bewusst anders als Collo (Creme, Tomatenrot, Bodoni).

Einzige Animation: Beim Laden werden die Streben der Fassade eingesetzt. Bei „Bewegung reduzieren“ entfällt sie.

## Geprüft (29.09.2026)

- Kein seitliches Scrollen bei 1366, 375 und 320 px Breite.
- Keine Anfragen an fremde Server beim Laden.
- `python3 build.py` ohne übrige Platzhalter.

## Quellen

Siehe `PLAN.md` und `daten/restaurant.json` (Feld `quellen`). Abgerufen am 29.09.2026.
