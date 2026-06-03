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


