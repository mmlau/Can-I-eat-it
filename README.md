# 📋 Template-Anleitung

> **Für Kursteilnehmer*innen:** Diese Sektion nach dem Setup deines Projekts löschen!

## So verwenden Sie dieses Template:
Dieses Template hilft dir, dein Data Science Projekt effizient zu organisieren und zu dokumentieren. Es bietet eine gängige Struktur, um deine Arbeit zu planen, durchzuführen und zu präsentieren.

### 1. Template verwenden
Templates können in GitHub über den Button **"Use this template" -> "Create a new repository"** in der oberen rechten Ecke in ein eigenes Repository überführt werden. Nutze diese Vorlage als Inspiration und passe sie an dein Projekt an! 

### 2. Projekt klonen
Danach kannst du dein neues Repository direkt über VS Code klonen. Dazu öffnest du in VS Code die Kommando-Palette (Strg+Shift+P) bzw. (Cmd+Shift+P) auf dem Mac und gibst **"Git: Clone"** ein. Wähle dann "Clone from GitHub..." und melde dich ggf. bei GitHub an. Suche nach deinem Repository und wähle einen lokalen Ordner aus, in dem das Projekt gespeichert werden soll.

### 3. Abhängigkeiten installieren
Nachdem du das Repository geklont hast, musst du die Abhängigkeiten installieren. Öffne dazu ein neues Terminal in VS Code über die Menüleiste "Terminal"->"Neues Terminal" und führe die folgenden Befehle aus:

```bash
uv sync
```

### 4. Erweiterungen hinzufügen
Für dieses Projekt empfehlen wir die Installation der folgenden VS Code Erweiterungen:
- **Python** (Microsoft) - Bietet Unterstützung für Python-Entwicklung.
- **Jupyter** (Microsoft) - Ermöglicht das Arbeiten mit Jupyter Notebooks direkt in VS Code.
- **Even Better TOML** (tamasfe) - Verbessert die Bearbeitung von TOML-Dateien.
- **Ruff** (Astral Software) - Ein schneller Linter für Python, der dir hilft, sauberen Code zu schreiben.
- **Material Icon Theme** (PKief) - Verbessert die Dateisymbole in VS Code für eine bessere Übersicht.

Dafür kannst du den Erweiterungs-Tab in VS Code öffnen (Symbol mit den vier Quadraten auf der linken Seitenleiste) und in die Suchleiste `@recommended` eingeben. Danach sollten dir die empfohlenen Erweiterungen angezeigt werden.

### Notebooks ausführen
Im Ordner `notebooks/` findest du ein Jupyter Notebook namens `01_exploration.ipynb`, das als Ausgangspunkt für deine Datenanalyse dient. Öffne das Notebook in VS Code und wähle oben rechts dein virtuelles Environment als Kernel aus. Führe die Zellen nacheinander aus. Wenn alles geklappt hat wird das Notebook einen Datensatz von Kaggle laden und im Ordner `data/` speichern.

Von hier an kannst du mit deinem Projekt starten und die Vorlagen nach belieben anpassen.

Schaue dir für weitere Informationen zum Template die Datei [docs/project.md](./docs/project.md) an.


Für dein Projekt kannst du die folgenden Abschnitte in der `README.md` Datei anpassen, um dein Projekt zu beschreiben und zu präsentieren. Lösche anschließend diese Anleitung.

---

# Can I eat it? 🍄

Entwicklung eines datengestützten Klassifikationsmodells auf Basis des UCI-Mushroom-Benchmarks, das rein kategoriale biologische Merkmale über gezielte Encoding-Verfahren verarbeitet. Das primäre Optimierungsziel liegt in der vollständigen Eliminierung falsch-negativer Vorhersagen (100 % Recall), um eine fehlerfreie Trennung zwischen essbaren und giftigen Proben zu garantieren.

## 📊 Projektübersicht

**Problemstellung:**
Das UCI-Pilzdatenset enthält ausschließlich kategoriale Merkmale (22 Attribute wie Hutform, Geruch, Sporenfarbe und Lebensraum) von 8.124 hypothetischen Proben aus den Gattungen *Agaricus* und *Lepiota*. Da es sich um computergenerierte, logische Kombinationen aus einem botanischen Feldführer handelt, liefert das Set eine fehlerfreie, perfekt balancierte Struktur für Benchmark-Tests. Die methodische Herausforderung besteht darin, dass diese qualitativen Daten keine mathematische Reihenfolge aufweisen und vor der Modellierung über geeignete Encodings transformiert werden müssen. Da eine Fehlklassifikation giftiger Pilze in der Realität lebensgefährlich ist, dürfen keine falsch-negativen Ergebnisse (False Negatives) auftreten. Das statistische Kriterium für die Modellgüte ist daher eine Sensitivität (Recall) von exakt 100 %.

**Ziel:**
Entwicklung und Validierung eines datengestützten Klassifikationsmodells zur Trennung von essbaren und giftigen Pilzen. Durch den gezielten Einsatz von kategorialen Encoding-Verfahren (z. B. One-Hot-Encoding) und Machine-Learning-Algorithmen wird eine Entscheidungsmatrix optimiert, deren primärer Fokus auf der Eliminierung falsch-negativer Vorhersagen auf diesem logischen Datensatz liegt.

*Hinweis: Da die Daten hypothetisch generiert wurden, dient dieses Projekt ausschließlich als Data-Science-Benchmark und ist nicht als Ratgeber für die reale Pilzbestimmung geeignet.*

**Methoden:** 
In Bearbeitung...
<!-- Welche Techniken/Algorithmen verwendest du? -->

## Setup

Klone das Repository
```bash
# Repository klonen
git clone [DEIN-REPO-LINK]
cd [REPO-NAME]
```

Installiere [uv](https://uv.dev) (falls noch nicht installiert) und synchronisiere die Abhängigkeiten
```bash
# Dependencies installieren
uv sync
```

### Ausführung

Notebooks in dieser Reihenfolge ausführen:
1. notebooks/01_exploration.ipynb
<!--
2. notebooks/02_preprocessing.ipynb
3. notebooks/03_modeling.ipynb
4. notebooks/04_results.ipynb
-->


