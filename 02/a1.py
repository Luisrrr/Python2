import math

# 1.
wenn = "wenn"
Fliegen = "Fliegen"
hinter = "hinter"
fliegen = "fliegen"
her = "her"
print(wenn, Fliegen, hinter, Fliegen, fliegen, fliegen, Fliegen, hinter, Fliegen, her)

# 2., 3.
a = 21
b = 3
c = 17
d = 4
res = a * b + c * d
print(res)
print(a * 3 + 17 * 4)
print(21 * b + c * 4)

# 4. Natürlich

# 5.
a = 3736
b = 3
c = 9286
res = a / b + c
print(type(a), type(b), type(c), type(res))
# res hat den Datentyp float weil es wegen der Division Nachkommastellen bekommen hat

# 6. print(str(z) + " = " + str(x) + " + " + str(y))
# Die Variablen z, x und y waren vorher int und müssen deswegen zu einem string
# konvertiert werden damit sie mit anderen strings verbunden werden können
# Es wird "z = x + y" ausgegeben

# 7.
# Rechnung	Ergebnis	Wie wird der Rest berechnet?
# 18 % 4	2	        Der Rest ist 2, denn 18 = (4 x 4) + 2
# 21 % 3	0	        Der Rest ist 0, denn 21 = (7 x 3) + 0
# 10 % 6	4	        Der Rest ist 4, denn 10 = (6 x 1) + 4
# 0 % 12	12	        Der Rest ist 0, denn 0 = (0 x 0) + 12
# -4 % 4	0	        Der Rest ist 0, denn -4 = (4 x 0) + -2
# -6 % 4	0	        Der Rest ist 0, denn -6 = (4 x 0) + -6

# 8.
a = 10
print(str(a) + " - -")
b = 3
print(str(a), str(b) + " -")
c = a + b
print(a, b, c)
c = c + 2
print(a, b, c)
c = c * b
print(a, b, c)
a = 2 * b
print(a, b, c)
b = c
print(a, b, c)
c = a + b / c
print(a, b, c)
c = b % a
print(a, b, c)
b = c ** c
print(a, b, c)

# 9.
# Du hast 1357 Sekunden für den 5 km Lauf im Sportunterricht benötigt.
# Du möchtest die Zeit aber in Minuten und Sekunden wissen.
# Berechne die Minuten und Sekunden mit arithmetischen Operatoren!
totalSeconds = 1357
minutes = math.floor(totalSeconds / 60)
print(str(minutes) + " Minuten und " + str(totalSeconds % 60) + " Sekunden")
