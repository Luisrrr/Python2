hauptStaedte = ["Berlin", "Oslo", "Wien", "Paris", "London", "Madrid", "Rom"]  # Syntax error
hauptStaedte.append("Bern")
anzahl = len(hauptStaedte)
print("Die Liste besteht aus anzahl europäischen Hauptstädten")
print("Die fünfte Hauptstadt in der Liste ist: " + hauptStaedte[4])  # Semantischer Fehler?
print("Die letzte Hauptstadt in der Liste ist: " + hauptStaedte[anzahl - 1])  # Exception
# 3.
# Es sagt mir was falsch ist


