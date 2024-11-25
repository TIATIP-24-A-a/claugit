# Binäre Suche

## Beschreibung
Die Binäre Suche findet ein Element in einer sortierten Liste durch wiederholtes Teilen der Suchbereiche.

## Quellen
- [Wikipedia - Binäre Suche](https://de.wikipedia.org/wiki/Bin%C3%A4re_Suche)

## Pseudocode
1. Setze `low = 0` und `high = len(array) - 1`.
2. Wiederhole, solange `low <= high`:
   - Berechne `mid = (low + high) // 2`.
   - Vergleiche `array[mid]` mit dem Zielwert.
   - Falls `array[mid] == Zielwert`: Rückgabe `mid`.
   - Falls `array[mid] > Zielwert`: `high = mid - 1`.
   - Sonst: `low = mid + 1`.
3. Rückgabe: Element nicht gefunden.
