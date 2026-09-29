# PLAN: Website für NOI Ristorante Pizzeria, Bad Rothenfelde

Stand: 29.09.2026 · Phase: **Gerüst gebaut** (Schritte 2, 4, 5, 6 als Entwurf erledigt; Schritte 1 und 3 warten auf das NOI)

## Ziel

Ein Website-Entwurf für das NOI (Birkenstraße 2, 49214 Bad Rothenfelde), gebaut nach dem Muster des Projekts **Collo** (Repository `GbiLinus/Collo`, live: https://gbilinus.github.io/Collo/).

Heute hat das NOI **keine eigene Website**. Gäste finden nur Instagram, Facebook und fremde Portale. Diese Portale zeigen veraltete oder widersprüchliche Daten (siehe `daten/restaurant.json`, Feld `widersprueche`).

Die Seite soll drei Dinge leisten:

1. **Tisch bekommen:** Anrufen mit einem Tipp, auf dem Handy.
2. **Speisekarte lesen:** aktuelle Karte als Text, mit Monatskarte oben.
3. **Richtige Fakten:** Öffnungszeiten, Adresse, Anfahrt aus einer Quelle.

## Nicht-Ziele (Version 1)

- Kein Shop, keine Bezahlung, keine eigene Lieferplattform.
- Kein CMS, kein Login. Pflege über `menu.py` und `template.html` wie bei Collo.
- Keine Fotos von fremden Seiten. Ohne eigene Fotos bleibt die Seite typografisch (wie Collo).

## Vorbild: Projekt Collo

Collo ist ein fertiger Entwurf für das spanisch-italienische Restaurant Collo im selben Ort. NOI übernimmt Technik, Aufbau und Arbeitsweise. Nur Inhalt und Gestaltung sind eigen.

### Was wir 1:1 übernehmen

| Collo | Zweck | NOI |
|---|---|---|
| `menu.py` | Speisekarte als Python-Daten: `SPECIALS` + `MENU` mit `(Nummer, Name, Beschreibung, Preis)` | gleich; `SPECIALS` = **Monatskarte** |
| `template.html` | Seitenaufbau mit Platzhaltern `{{SPECIALS}}`, `{{CHIPS}}`, `{{MENU}}`, `{{BAND}}`, `{{MENU_DATE}}` | gleich; `{{RESERVE}}` entfällt, solange nur telefonisch reserviert wird |
| `build.py` | Baut `index.html`, bricht ab, wenn ein Platzhalter übrig ist | gleich |
| `main.js` | „Jetzt geöffnet?“, heutiger Tag in der Tabelle, aktive Kategorie | angepasst: Öffnungszeiten **je Wochentag** (NOI hat Montag Ruhetag und evtl. andere Sonntagszeit) |
| `style.css` | Gestaltung, Farben als CSS-Variablen | eigene Farben und Schriften (siehe Design) |
| `fonts/` | Schriften lokal (DSGVO) | eigene Schriften, auch lokal |
| `impressum.html`, `datenschutz.html` | Pflichtseiten, fehlende Angaben gelb markiert | gleich |
| `FEHLT.md` | Was fehlt oder unsicher ist, nummeriert | gleich, schon angelegt |
| `favicon.svg`, `.nojekyll`, `.gitignore` | Kleinkram für GitHub Pages | gleich |
| JSON-LD `schema.org/Restaurant` im `<head>` | Google versteht Adresse und Zeiten | gleich |
| `<meta name="robots" content="noindex">` | Entwurf wird nicht von Google gefunden | gleich, bis NOI freigibt |

### Seitenaufbau (eine Seite, wie Collo)

| Abschnitt Collo | NOI |
|---|---|
| Kopfleiste: Name, Navigation, Knopf „Tisch reservieren“ | Name, Navigation (Speisekarte, Über uns, Anfahrt & Zeiten), Knopf **„Anrufen“** (`tel:+4954243639168`) |
| Hero + „Ticket“ (Status, Adresse, Telefon, Zeiten) | gleich. Slogan nach Absprache, z. B. „Make it Noi“ |
| Laufband mit Stichworten | Pizza, Pasta, Bruschetta, Panini, Fritto Misto, Tiramisu, Vino … |
| Tafel „Neu auf der Karte“ | **„Monatskarte“** mit Monat im Titel |
| Speisekarte mit Kategorien-Chips | gleich |
| „Am Herd“: Küchenchef Rafael Soto | **„Wir“**: Kevin und Mara (noi = „wir“ auf Italienisch). Nur mit Freigabe der beiden |
| Drei Punkte „I Frisch gekocht / II Für jeden Anlass / III Die Bar“ | z. B. „I Pizza wie in Italien / II Familiengeführt / III Altes Fachwerkhaus“. Nur, was die Inhaber bestätigen |
| Besuch: Öffnungszeiten, Adresse + „Route planen“, Reservieren | gleich; Reservieren = Telefon. Zusätzlich Parken, barrierefreier Eingang (wenn bestätigt) |
| Footer mit Social, Impressum, Datenschutz, Kartenstand | gleich |

### Was bei NOI anders sein muss

- **Öffnungszeiten nicht fest im Code:** Collo hat `OPEN = 17, CLOSE = 23, REST_DAY = 2`. NOI braucht eine Tabelle je Wochentag (`HOURS = {0: …, 1: None, 2: ["17:30", "23:00"], …}`), weil der Sonntag abweichen kann. Die Tabelle erzeugt `build.py` aus einer Stelle, auch für JSON-LD und die Zeitentabelle.
- **Reservierung:** Kein Online-Tool bekannt. Knöpfe führen zum Telefon. Falls NOI ein Tool will (z. B. resmio wie Collo), kommt `{{RESERVE}}` zurück.
- **Speisekarte fehlt fast ganz** (siehe `daten/speisekarte-fragmente.json`). Collo hatte eine vollständige Karte auf der eigenen Website. Bei NOI müssen wir sie vom Restaurant bekommen.
- **Kennzeichnung:** optional Felder für vegetarisch/scharf in `menu.py`, nur wenn NOI sie liefert.

## Design-Richtung

Collo: Creme + Tomatenrot, Bodoni Moda + Karla, Markise und Fliesen. NOI soll sich klar davon unterscheiden, da beide im selben Ort sind.

- **Motiv:** das alte Fachwerkhaus und die Deko mit Film- und Musikstars. Idee: dunkle Balkenlinien als grafisches Raster auf hellem Putz; Überschriften mit Kino-Charakter („Dolce Vita“, 50er/60er).
- **Farben (Vorschlag):** Putzweiß als Grund, Eichenbraun-Schwarz für Schrift und Balken, Basilikumgrün als Akzent, ein warmes Ocker für Knöpfe. Kein Tomatenrot als Hauptfarbe (das hat Collo).
- **Schriften (Vorschlag):** kontrastreiche Display-Schrift für Titel, ruhige serifenlose für Text. Beide mit freier Lizenz (SIL OFL), lokal in `fonts/`.
- **Logo:** vorhandenes NOI-Logo nutzen, falls es eins gibt; sonst Schriftzug wie bei Collo.

Endgültig nach dem Gespräch mit den Inhabern.

## Datensammlung

| Datei | Inhalt | Stand |
|---|---|---|
| `daten/restaurant.json` | Stammdaten, jede Angabe mit Quelle und Status (`bestaetigt`, `unsicher`, `fehlt`), Widersprüche, Wettbewerb | gesammelt 29.09.2026 |
| `daten/speisekarte-fragmente.json` | 8 öffentlich gefundene Gerichte (Stand 2021/2024), Kategorien-Vorschlag | Fragmente |
| `FEHLT.md` | Was fehlt oder unsicher ist, Fragen an die Inhaber, Datenschutz-Punkte | offen |

Regel wie bei Collo: **Was nicht sicher belegt ist, kommt nicht auf die Seite.**

## Bauablauf

1. **Gespräch mit Kevin und Mara** anhand `FEHLT.md`: Zeiten, Karte, Impressum-Angaben, Fotos, Logo.
2. **Gerüst von Collo übernehmen:** `build.py`, `main.js`, `.nojekyll`, `.gitignore`, Aufbau von `template.html`, `impressum.html`, `datenschutz.html`.
3. **`menu.py` füllen** mit der echten Karte. Monatskarte als `SPECIALS`.
4. **Öffnungszeiten je Tag** in `build.py`/`main.js` einbauen.
5. **Gestaltung:** `style.css`, Schriften, `favicon.svg`.
6. **Pflichtseiten:** Impressum und Datenschutz mit echten Angaben, Lücken gelb markiert.
7. **Prüfen:** Handy ab 320 px, keine Anfragen an fremde Server, Lighthouse, Kontrast, Tastatur.
8. **GitHub Pages** als Vorschau (`https://gbilinus.github.io/Noi-Pizzaria/`). Für den echten Betrieb eigene Domain und EU-Hosting (siehe `FEHLT.md`).

## Akzeptanzkriterien Version 1

- Anruf aus jedem Abschnitt mit einem Tipp erreichbar.
- Speisekarte vollständig als Text, Preise wie auf der Karte im Restaurant.
- Öffnungszeiten stehen an genau einer Stelle und stimmen in Tabelle, Status-Anzeige und JSON-LD überein.
- Impressum und Datenschutz vorhanden und im Footer verlinkt.
- Beim Laden keine Verbindung zu fremden Servern.
- Kein seitliches Scrollen ab 320 px Breite.
- `python3 build.py` läuft ohne Fehler, kein `{{…}}` übrig.

## Quellen (abgerufen am 29.09.2026)

- Vorbild Collo: https://github.com/GbiLinus/Collo · https://gbilinus.github.io/Collo/
- NOI Tripadvisor: https://www.tripadvisor.com/Restaurant_Review-g198417-d18782747-Reviews-Noi-Bad_Rothenfelde_Lower_Saxony.html
- NOI speisekarte.de: https://www.speisekarte.de/bad-rothenfelde/restaurant/noi/speisekarte
- NOI speisekartenweb.de: https://speisekartenweb.de/restaurants/rothenfelde/noi-ristorante-pizzeria-49410
- NOI mymenuweb: https://mymenuweb.com/de/restaurants/1811018/
- NOI placejoys: https://noi-ristorante-pizzeria.placejoys.com/
- NOI Restaurant Guru: https://restaurantguru.com/NOI-Bad-Rothenfelde
- NOI Instagram: https://www.instagram.com/makeitnoi/ · Facebook: https://www.facebook.com/MakeitNoi/
