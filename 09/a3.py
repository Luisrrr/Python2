import time
import random

def crack_password():
    start = time.time()

    rdStr = ""
    while rdStr != password:
        rdStr = ""
        for x in range(0, maxLength):
            rdStr += symbols[random.randint(0, len(symbols) - 1)]
        print(rdStr)

    end = time.time()
    print("Passwort nach", end - start, " Sekunden gecrackt")
    return end - start


password = ""
maxLength = 3
while len(password) != maxLength:
    password = input("Gib ein " + str(maxLength) + " Zeichen Passwort ein: ").upper()

symbols = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
           "V", "W", "X", "Y", "Z", "!", "$", "%", "&", "/", "(", ")", "{", "}", "[", "]", "=", "*", "_", "-", ".",
           "#", "+", "~", "<", ">"]

times = []
sum = 0

for c in range(0, 100):
    times.append(crack_password())
    sum += times[c]
print("Durchschnittliche Zeit benötigt:", sum / 100, "Sekunden")

# 3 Zeichen Durchschnitt: 0.932s
# Bei 4+ Zeichen dauert es ewig bis das Passwort überhaupt einmal gecrackt wird
