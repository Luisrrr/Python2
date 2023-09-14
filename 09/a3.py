import time
import random

password = ""
maxLength = 3
while len(password) != maxLength:
    password = input("Gib ein " + str(maxLength) + " Zeichen Passwort ein: ").upper()

symbols = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
           "V", "W", "X", "Y", "Z", "!", "$", "%", "&", "/", "(", ")", "{", "}", "[", "]", "=", "*", "_", "-", ".",
           "#", "+", "~", "<", ">"]

start = time.time()

rdStr = ""
while rdStr != password:
    rdStr = ""
    for x in range(0, maxLength):
        rdStr += symbols[random.randint(0, len(symbols) - 1)]
    print(rdStr)

end = time.time()
print("Passwort nach", end - start, " Sekunden gecrackt")

# Die Laufzeiten werden mega lang bei 4+ Zeichen
