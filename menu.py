# Speisekarte des NOI – ENTWURF.
# Die aktuelle Karte fehlt noch (siehe FEHLT.md, Punkt 1). Bis dahin stehen hier nur
# die wenigen Gerichte, die öffentlich zu finden waren (daten/speisekarte-fragmente.json).
# Sie sind veraltet und dienen nur dazu, das Layout zu zeigen.
# Format wie im Projekt Collo: (Nummer, Name, Beschreibung, Preis)

# Monatskarte (oben auf der Seite)
SPECIALS_MONTH = "März 2024"
SPECIALS = [
    ("", "Bruschetta ai carciofi", "Gorgonzola, Sardellen, Artischocken und Mozzarella", "7,50"),
    ("", "Panino grande Arrabbiato", "Nduja, Burrata, Rucola und karamellisierte Zwiebeln", "15,50"),
    ("", "Panino grande Royal", "Salat, Pute, Zwiebeln, Schafskäse und Knoblauchsoße", "15,50"),
    ("", "Panino grande al Salmone", "Rucola, Lachs, Burrata und frische Zwiebeln", "15,50"),
]

# Stand der Karte, erscheint im Footer
MENU_DATE = "Entwurf mit Beispielgerichten von 2021"

# (Anker, Titel, Einleitung, Fußnote, Gerichte)
MENU = [
    ("pizza", "Pizza", None, None, [
        ("", "Pizza Fantasia", "Paprika, Salami, Mais, Schafskäse, Tomatensoße und Käse", "10,50"),
    ]),
    ("antipasti", "Antipasti", None, None, [
        ("", "Bruschetta", "mit Dattel-Curry-Paste, 4 Stück", "5,90"),
    ]),
    ("fritto-misto", "Fritto Misto", None, None, [
        ("", "Frittierte Calamari", "mit Scampi und selbstgemachten Pommes", "16,50"),
        ("", "Risotto di Mare", "Risotto mit Meeresfrüchten", "12,50"),
    ]),
]
