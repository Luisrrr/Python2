import random

name = input("Gib deinen Namen ein\n")
print("Hallo", name + "!")
pick = input("Möchtest du...\n(1) - zum Piraten\n(2) - zur Prinzessin\n(3) - zum Bettler\n")
playerInput = ""

if pick == "1":
    print("Hei-Hei-Ho,", name + "!")
    print("Du darfst einmal würfeln, um dein Leben zu retten!")
    rd = random.randint(1, 6)
    print(rd, "gewürfelt")
    if rd >= 1 | rd <= 2:
        print("Verloren! Her mit deinem Gold!")
    elif rd >= 3 | rd <= 4:
        print("naja, kannst nicht mal würfeln, du armer Tropf! Hier, ich" +
              " schenke dir meine Augenklappe. Die bringt Glück.")
    elif rd >= 5 | rd <= 6:
        print("Gewonnen! Du bekommst das tausendfache deines Wurfs in Golddublonen!")

elif pick == "2":
    print("Ich grüße dich,", name, "!")
    print("Küsse einen dieser Gegenstände und du darfst ihn behalten.")
    playerInput = input("(a) - eine goldene Kugel\n(b) - einen grünen Frosch\n(c) eine silberne Krone\n")
    if playerInput == "a":
        print("Du gemeiner Dieb! Einfach meine Kugel klauen!! Verhaftet", name, "!")
    elif playerInput == "b":
        print("Igitt! Du ekelst dich auch vor gar nix! Du bist meiner nicht würdig. Nimm den Frosch und geh!")
    elif playerInput == "c":
        print("In dir fließt edles Blut! Du hast mein Herz gewonnen! Heirate mich und regiere mit mir dieses Land.")
elif pick == "3":
    print("Edler Herr, edle Dame! Ich bin so hungrig! Schenk mir bitte deinen Apfel!")
    playerInput = input("y/n\n")
    if playerInput == "y":
        print("Vielen Dank! Nimm meine Glückssocke als Dank!")
    else:
        print("Was machst du dann hier? Hau bloß ab!")
