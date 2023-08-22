#######################################
# Aufgabe Farblisten
#
# Implementiere die in den Kommentaren beschriebenen Aktionen
# jeweils unterhalb des entsprechenden Kommentars
# - den Kommentar bitte NICHT löschen -
# und gib zusätzlich jedes Mal den Inhalt der Liste mit einem print-Befehl in der Konsole aus
# damit kannst du testen, ob dein Code richtig ist.
#######################################
#
# - Lege eine leere Liste mit dem Namen farben an.
farben = []
# - Füge die Farben Blau, Grün, Gelb und Rot (Datentype String) in die Liste ein.
farben = ["Blau", "Grün", "Gelb", "Rot"]
print(farben)
# - Füge 3 Mal den String Blau hinten an die Liste an.
farben.append("Blau")
farben.append("Blau")
farben.append("Blau")
print(farben)
# - Gib aus, wie viele Elemente die Liste hat.
print("Länge:", len(farben))
# - Gib aus, wie oft Blau in der Liste vorkommt
print("Anzahl Blau:", farben.count("Blau"))
# - füge die Farbe Grün ganz vorne in die Liste ein
farben.insert(0, "Grün")
print(farben)
# - Gib aus, an welchem Index sich die Farbe gelb befindet und speicher diesen Wert in der Variable idx_gelb
idx_gelb = farben.index("Gelb")
print("Index von Gelb:", idx_gelb)
# - füge die Farben Blau, Grün, Lila, Grün und Blau hinter Gelb ein (benutze die Variable idx_gelb)
farben.insert(idx_gelb, "Blau")
farben.insert(idx_gelb, "Grün")
farben.insert(idx_gelb, "Lila")
farben.insert(idx_gelb, "Grün")
farben.insert(idx_gelb, "Blau")
farben.insert(idx_gelb, "Gelb")
print(farben)
# - Lösche die Farbe Gelb wieder aus der Liste.
farben.remove("Gelb")
# - Gib aus, an welchem Index sich die Farbe rot befindet und speichere diesen Wert in der Variable idx_rot
idx_rot = farben.index("Rot")
print("Index von Rot:", idx_rot)
# - Ersetze Rot durch Lila (benutze die Varialbe idx_rot)
farben.insert(idx_rot, "Lila")
farben.remove("Rot")
print(farben)
# - Gib aus, an welcher Position sich zum ersten Mal die Farbe Grün befindet
print("Erste Instanz von Grün:", farben.index("Grün"))
# - Lösche die zweite Farbe aus der Liste und gib aus, welche Farbe das war.
print(farben[1], "wurde entfernt")
farben.remove(farben[1])
print(farben)
# - Gib aus, welche Farbe jetzt die zweite Farbe in der Liste ist.
print("Neue zweite Farbe:", farben[1])
# - Gib aus, welche Farbe als Letztes in der Liste steht.
print("Letztes Element:", farben[len(farben) - 1])
# - Wenn es die Farbe Orange noch nicht in der Liste gibt, dann füge sie am Ende in die Liste ein
if farben.count("Orange") == 0:
    farben.append("Orange")
print(farben)
# - Sortiere die erste Liste.
farben.sort()
print("Sortierte Liste:", farben)
# - Lösche alle Elemente aus der Liste
farben.clear()
print(farben)
