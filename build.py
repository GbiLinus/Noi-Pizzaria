"""Erzeugt index.html aus template.html und menu.py.

Aufruf:  python3 build.py

Öffnungszeiten und Telefon stehen nur hier. Daraus entstehen die Zeiten-Tabelle,
die Kurzfassung im Hero, die Daten für "Jetzt geöffnet?" (main.js) und das JSON-LD.
"""
import json
from html import escape
from pathlib import Path

from menu import MENU, MENU_DATE, SPECIALS, SPECIALS_MONTH

ROOT = Path(__file__).parent

PHONE = "05424 3639168"
PHONE_TEL = "+4954243639168"

# Montag zuerst. None = Ruhetag, "?" = noch nicht bestätigt (FEHLT.md, Punkt 11).
HOURS = [
    ("Montag", "Mo", "Monday", None),
    ("Dienstag", "Di", "Tuesday", ("17:30", "23:00")),
    ("Mittwoch", "Mi", "Wednesday", ("17:30", "23:00")),
    ("Donnerstag", "Do", "Thursday", ("17:30", "23:00")),
    ("Freitag", "Fr", "Friday", ("17:30", "23:00")),
    ("Samstag", "Sa", "Saturday", ("17:30", "23:00")),
    ("Sonntag", "So", "Sunday", "?"),
]


def js_day(i):
    """Index Montag-zuerst -> Date.getDay() (0 = Sonntag)."""
    return (i + 1) % 7


def clock(t):
    h, m = t.split(":")
    return h if m == "00" else f"{h}:{m}"


def span(t):
    return f"{clock(t[0])}&ndash;{clock(t[1])}&nbsp;Uhr"


def groups():
    """Aufeinanderfolgende Tage mit gleichen Zeiten zusammenfassen."""
    out = []
    for i, (_, short, en, h) in enumerate(HOURS):
        if out and out[-1][3] == h:
            out[-1][1] = short
            out[-1][2].append(en)
        else:
            out.append([short, short, [en], h])
    return out


def hours_summary():
    parts = []
    for first, last, _, h in groups():
        days = first if first == last else f"{first}&ndash;{last}"
        if h is None:
            parts.append(f"{days} Ruhetag")
        elif h == "?":
            parts.append(f'{days} <span class="todo">noch offen</span>')
        else:
            parts.append(f"{days} {span(h)}")
    return "<br>".join(parts)


def hours_table():
    rows = []
    for i, (name, _, _, h) in enumerate(HOURS):
        if h is None:
            cell, cls = "Ruhetag", ' class="is-closed"'
        elif h == "?":
            cell, cls = '<span class="todo">noch zu bestätigen</span>', ""
        else:
            cell, cls = span(h), ""
        rows.append(f'          <tr data-day="{js_day(i)}"{cls}><th scope="row">{name}</th><td>{cell}</td></tr>')
    return "\n".join(rows)


def hours_json():
    return json.dumps({str(js_day(i)): h for i, (*_, h) in enumerate(HOURS)})


def jsonld_hours():
    spec = [
        {"@type": "OpeningHoursSpecification", "dayOfWeek": days, "opens": h[0], "closes": h[1]}
        for _, _, days, h in groups()
        if isinstance(h, tuple)
    ]
    return json.dumps(spec, ensure_ascii=False, indent=2).replace("\n", "\n  ")


def dish(no, name, desc, price):
    no_html = f'<span class="dish__no">{escape(no)}</span>' if no else ""
    desc_html = f'<p class="dish__desc">{escape(desc)}</p>' if desc else ""
    return (
        f'<li class="dish">{no_html}<div class="dish__row">'
        f'<h4 class="dish__name">{escape(name)}</h4>'
        f'<span class="dish__price">{price}&nbsp;&euro;</span></div>{desc_html}</li>'
    )


def build():
    specials = "\n".join("        " + dish(*i) for i in SPECIALS)
    chips = "\n".join(f'      <a href="#{sid}">{escape(title)}</a>' for sid, title, *_ in MENU)

    sections = []
    for sid, title, intro, note, items in MENU:
        intro_html = f'<p class="menu__sub">{escape(intro)}</p>' if intro else ""
        note_html = f'\n    <p class="menu__foot">{escape(note)}</p>' if note else ""
        dishes = "\n".join("      " + dish(*i) for i in items)
        sections.append(
            f'  <section id="{sid}" class="menu__sec" aria-labelledby="{sid}-t">\n'
            f'    <h3 id="{sid}-t" class="menu__title balken-rein">{escape(title)}</h3>{intro_html}\n'
            f'    <ul class="menu__list">\n{dishes}\n    </ul>{note_html}\n  </section>'
        )

    html = (ROOT / "template.html").read_text(encoding="utf-8")
    for key, val in {
        "SPECIALS": specials,
        "SPECIALS_MONTH": escape(SPECIALS_MONTH),
        "CHIPS": chips,
        "MENU": "\n\n".join(sections),
        "MENU_DATE": escape(MENU_DATE),
        "HOURS_SUMMARY": hours_summary(),
        "HOURS_TABLE": hours_table(),
        "HOURS_JSON": hours_json(),
        "JSONLD_HOURS": jsonld_hours(),
        "PHONE": PHONE.replace(" ", "&nbsp;"),
        "PHONE_TEL": PHONE_TEL,
    }.items():
        html = html.replace("{{" + key + "}}", val)
    assert "{{" not in html, "Platzhalter übrig"
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print("index.html geschrieben")


if __name__ == "__main__":
    build()
