hauptStaedte = ["Berlin", "Oslo", "Wien", "Paris", "London", "Madrid", "Rom"]  # Syntax error, semantischer Fehler
hauptStaedte.append("Bern")
anzahl = len(hauptStaedte)
print("Die Liste besteht aus anzahl europäischen Hauptstädten")
print("Die fünfte Hauptstadt in der Liste ist: " + hauptStaedte[4])
print("Die letzte Hauptstadt in der Liste ist: " + hauptStaedte[anzahl - 1])  # Exception
# 1. 3.
# Es sagt mir was falsch ist
