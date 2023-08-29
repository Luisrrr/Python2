import random

string = ""
num = 0
zufallszahlen = []
while string != "Stopp":
    num = random.randint(1, 6)
    zufallszahlen.append(num)
    print(num)
    string = input("Mache Zufallszahlen mit enter. \"Stopp\" um weiter zu gehen.\n")

print("Alle Zahlen:\n")
num = 0
while num < len(zufallszahlen):
    print(zufallszahlen[num])
    num += 1
print("Alle Zahlen aber rückwärts:\n")
num = len(zufallszahlen) - 1
while num >= 0:
    print(zufallszahlen[num])
    num -= 1
print("Summe von allen Zahlen:\n")
sum = 0
num = 0
while num < len(zufallszahlen):
    sum += zufallszahlen[num]
    num += 1
print(sum)
print("Alle dreien:\n")
indexes = []
num = 0
while num < len(zufallszahlen):
    if zufallszahlen[num] == 3:
        indexes.append(num)
    num += 1
print(indexes)
