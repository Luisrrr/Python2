import random

name = input("Gib deinen Namen ein")
print("Hallo", name + "!")
playerClass = input("Möchtest du...\n(1) - zum Piraten\n(2) - zur Prinzessin\n(3) - zum Bettler")

if playerClass == 1:
    print("Hei-Hei-Ho,", name + "!")
    print("Du darfst einmal würfeln, um dein Leben zu retten!")
    rd = random.randint(1, 6)
    if rd >= 1 || rd <= 2:

