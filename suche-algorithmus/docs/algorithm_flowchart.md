```mermaid
graph TD
    Start --> Sortiert{Ist die Liste sortiert?}
    Sortiert -- Nein --> Fehler[Sortiere die Liste]
    Sortiert -- Ja --> Suche[Teile die Liste in der Mitte]
    Suche --> Vergleich{Ist mid = Zielwert?}
    Vergleich -- Ja --> Gefunden[Zielwert gefunden]
    Vergleich -- Nein --> Richtung{mid > Zielwert?}
    Richtung -- Ja --> Links[Suche in der linken Hälfte]
    Richtung -- Nein --> Rechts[Suche in der rechten Hälfte]
    Links --> Suche
    Rechts --> Suche