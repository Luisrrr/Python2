import random

while True:
    num = 0
    guesses = []
    guess = 0
    while num < 6:
        guess = int(input("Gib eine Zahl zwischen 1 und 49 ein: "))
        while guess < 1 or guess > 49 or guesses.count(guess) != 0:
            guess = int(input("Ungültige oder doppelte Zahl. Gib eine Zahl zwischen 1 und 49 ein: "))
        guesses.append(guess)
        num += 1
    print("Guesses:", guesses)

    lottoZahlen = []
    num = 0
    richtig = []
    while num < 6:
        neueZahl = random.randint(1, 49)
        while lottoZahlen.count(neueZahl) != 0:
            neueZahl = random.randint(1, 49)
        if guesses.count(neueZahl) != 0:
            richtig.append(neueZahl)
        lottoZahlen.append(neueZahl)
        num += 1
    print("Lottozahlen:", lottoZahlen)
    if len(richtig) != 6:
        print("Du hattest die Zahlen", richtig, "richtig")
    else:
        print("Du hattest alles Richtig!! lets gooo")
    str = input("Nochmal? y/n: ")
    if str == "n":
        break
