import random

def demand_guesses():
    num = 0
    while num < 6:
        guess = int(input("Gib eine Zahl zwischen 1 und 49 ein: "))
        while guess < 1 or guess > 49 or guesses.count(guess) != 0:
            guess = int(input("Ungültige oder doppelte Zahl. Gib eine Zahl zwischen 1 und 49 ein: "))
        guesses.append(guess)
        num += 1

    return guesses


def get_correct_guesses(lottoZahlen):
    num = 0
    richtig = []
    while num < 6:
        if lottoZahlen.count(guesses[num]) != 0:
            richtig.append(guesses[num])
        num += 1

    return richtig


def generate_lotto_zahlen():
    num = 0
    lottoZahlen = []
    while num < 6:
        neueZahl = random.randint(1, 12)
        while lottoZahlen.count(neueZahl) != 0:
            neueZahl = random.randint(1, 12)
        lottoZahlen.append(neueZahl)
        num += 1

    return lottoZahlen


while True:
    guesses = demand_guesses()
    print("Guesses:", guesses)

    lottoZahlen = generate_lotto_zahlen()
    print("Lottozahlen:", lottoZahlen)

    richtig = get_correct_guesses(lottoZahlen)
    if len(richtig) != 6:
        print("Du hattest die Zahlen", richtig, "richtig")
    else:
        print("Du hattest alles Richtig!! lets gooo")

    str = input("Nochmal? y/n: ")
    if str == "n":
        break
