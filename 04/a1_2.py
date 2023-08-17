# 1.
# 10: Zahl ist größer als 0 also wird msg auf "Die Zahl ist größer 0!" gesetzt
# -7: Zahl ist nicht größer als 0 also wird abgefragt, ob es kleiner ist, ist es also wird msg auf "Die Zahl ist kleiner
# 0!"
# 0: Zahl ist nicht größer als 0, also wird abgefragt ob kleiner als 0, ist es nicht also wird
# msg auf "Treffer" gesetzt
# 'Hallo': Error, weil es nicht zu int konvertiert werden kann

# 1.2
# Die condition ist immer false, deshalb wird der Inhalt vom if auch nie ausgeführt

# 1.3
wahl = input("Wähle aus: Apfel oder Birne")
if wahl == "Apfel":  # Vergleiche brauchen immer 2 =
    print("Du hast den Apfel gewählt")  # style fehler weil nur 2 Leertasten
elif wahl == "Birne":  # "Birne" allein gibt keinen boolean zurück, und das muss ein else if sein
    print("Du hast die Birne gewählt.")
else:   # Doppelpunkt muss hin
    print("Falsche Eingabe.")
    print("Nur Apfel oder Birne sind zulässig.")  # In python kann man nicht einfach tab machen,
                                                  # weil es einen Block kennzeichnet
                                                  # ich weiß nicht was der style Fehler heißt
