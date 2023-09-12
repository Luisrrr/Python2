# x = int(input("Eine Zahl bitte! "))
#
# i = 1
# while i <= 1000:
#   if i % x == 0:
#      print(i)
#   i += 1
# Der Code printed i, wenn der Rest einer division mit x, welche der Benutzer bestimmt,
# 0 ist und wiederholt das, solange i kleiner oder gleich 1000 ist.

x = int(input("Eine Zahl bitte! "))

i = 1
for c in range(0, 1000):
    if i % x == 0:
        print(i)
    i += 1

# autos = ["Volkswagen", "Mercedes", "Opel", "Ford", "Toyota", "Hyundai", "Dacia", "Kia"]
# for auto in autos:
#     print(auto)
# Dieser Code geht jedes Element in der Liste autos durch und printed den Wert.

autos = ["Volkswagen", "Mercedes", "Opel", "Ford", "Toyota", "Hyundai", "Dacia", "Kia"]
count = 0
while count < len(autos):
    print(autos[count])
    count += 1

# Vorteil von for Schleifen: man muss keine Zähler Variable for dem loop deklarieren
# For Schleifen sind nicht ideal, wenn man mit einer Bedingung loopen will.
