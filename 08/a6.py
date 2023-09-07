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
# In Zeile 11 springt das Programm in die Funktion und die Ausführung wird fortgesetzt in Zeile 2
# Das war die letzte Anweisung in der Funktion und die Programmausführung wird fortgesetzt in Zeile im Hauptteil \ in
# Das war die letzte Anweisung im Hauptteil und das Programm beendet sich
