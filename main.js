// NOI – kleine Helfer: "Jetzt geöffnet?", heutiger Tag in der Tabelle,
// aktive Kategorie in der Speisekarte.
// Die Öffnungszeiten kommen aus build.py (script#zeiten), Schlüssel = Date.getDay().
(function () {
  "use strict";

  var DAYS = ["Sonntag", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag"];
  var hours = {};
  try { hours = JSON.parse(document.getElementById("zeiten").textContent); } catch (e) { return; }

  function berlinNow() {
    try {
      var parts = new Intl.DateTimeFormat("en-US", {
        timeZone: "Europe/Berlin", weekday: "short", hour: "numeric", minute: "numeric", hour12: false
      }).formatToParts(new Date());
      var get = function (t) { return parts.find(function (p) { return p.type === t; }).value; };
      var day = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"].indexOf(get("weekday"));
      return { day: day, min: (+get("hour")) % 24 * 60 + (+get("minute")) };
    } catch (e) {
      var d = new Date();
      return { day: d.getDay(), min: d.getHours() * 60 + d.getMinutes() };
    }
  }

  function toMin(t) { var p = t.split(":"); return +p[0] * 60 + +p[1]; }
  function clock(t) { return t.slice(3) === "00" ? t.slice(0, 2) : t; }

  // Nächster Tag mit Zeiten. Ein unbestätigter Tag unterwegs wird genannt statt übersprungen.
  function next(from) {
    for (var i = 1; i <= 7; i++) {
      var d = (from + i) % 7, h = hours[d];
      var when = i === 1 ? "morgen" : DAYS[d];
      if (h === "?") return "Zeiten für " + DAYS[d] + " bitte telefonisch erfragen";
      if (h) return when + " ab " + clock(h[0]) + " Uhr";
    }
    return "";
  }

  function status(now) {
    var h = hours[now.day];
    if (h === "?") return ["Heute bitte anrufen, Zeiten noch offen", ""];
    if (!h) return ["Heute Ruhetag, " + next(now.day), "is-closed"];
    if (now.min < toMin(h[0])) return ["Heute ab " + clock(h[0]) + " Uhr geöffnet", ""];
    if (now.min < toMin(h[1])) return ["Jetzt geöffnet bis " + clock(h[1]) + " Uhr", "is-open"];
    return ["Geschlossen, " + next(now.day), "is-closed"];
  }

  var now = berlinNow();
  var el = document.querySelector("[data-status]");
  if (el) {
    var s = status(now);
    el.textContent = s[0];
    if (s[1]) el.classList.add(s[1]);
  }
  var row = document.querySelector('.zeiten tr[data-day="' + now.day + '"]');
  if (row) row.classList.add("is-today");

  // Höhe der Kopfleiste für die klebende Kategorienleiste
  var kopf = document.querySelector(".kopf");
  function setKopf() {
    if (kopf) document.documentElement.style.setProperty("--kopf-h", kopf.offsetHeight + "px");
  }
  setKopf();
  window.addEventListener("resize", setKopf);

  // Aktive Kategorie markieren
  var links = document.querySelectorAll(".leiste a");
  if (!("IntersectionObserver" in window) || !links.length) return;
  var byId = {};
  links.forEach(function (a) { byId[a.getAttribute("href").slice(1)] = a; });
  var current = null;
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      var a = byId[e.target.id];
      if (!a || a === current) return;
      if (current) current.classList.remove("is-active");
      a.classList.add("is-active");
      current = a;
      var box = a.parentNode;
      box.scrollTo({ left: a.offsetLeft - box.clientWidth / 2 + a.clientWidth / 2, behavior: "smooth" });
    });
  }, { rootMargin: "-35% 0px -60% 0px" });
  document.querySelectorAll(".menu__sec").forEach(function (s) { io.observe(s); });
})();
