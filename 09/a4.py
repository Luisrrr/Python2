import random


def x_beats_x(str1, str2):
    if str1 == "Schere":
        if str2 == "Papier":
            return True
    elif str1 == "Stein":
        if str2 == "Schere":
            return True
    elif str1 == "Papier":
        if str2 == "Stein":
            return True

    return False


def get_rd_object():
    rd = random.randint(1, 3)
    if rd == 1:
        return "Schere"
    elif rd == 2:
        return "Stein"
    else:
        return "Papier"


score1 = 0
score2 = 0
for x in range(0, 3):
    str1 = input("Schere, Stein, Papier: ")
    str2 = get_rd_object()
    print("Gegner:", str2)

    if x_beats_x(str1, str2):
        score1 += 1
        print("Du kriegst einen Punkt (" + str(score2) + ")")
    elif x_beats_x(str2, str1):
        score2 += 1
        print("Computer kriegt einen Punkt (" + str(score2) + ")")

print("Punkte:", str(score1) + ",", score2)
if score1 > score2:
    print("Du hat gewonnen")
elif score2 > score1:
    print("Computer hat gewonnen")
else:
    print("Unentschieden")
