def funktion_a():
    print("Hallo! Ich bin Funktion A!")
    funktion_b()


def funktion_b():
    print("Hallo! Ich bin Funktion B!")
    funktion_a()

# hier fängt der Hauptteil an
print("Anfang")
funktion_a()
print("Mitte")
funktion_b()
print("Ende")

# Die Ausführung des Programms beginnt in Zeile 10
# Danach wird die a-Funktion ausgeführt und
# "Hallo! Ich bin Funktion A!" wird in der Konsole angezeigt
# In Zeile 11 springt das Programm in die Funktion a und die Ausführung wird fortgesetzt in Zeile 2
# funktion_b() war die letzte Anweisung in der Funktion a und die Programmausführung wird fortgesetzt in Zeile
# nicht im Hauptteil, sondern Zeile 6
# Nichts war die letzte Anweisung im Hauptteil und das Programm beendet sich nicht

# Das Problem ist das die Methoden recursion verursachen und irgendwann das Programm keine Lust mehr hat
