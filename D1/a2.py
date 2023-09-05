exitProgram = False
while exitProgram == False: # Wie geht !bool?
    loggedIn = True
    login = input("Gib dein Name ein um dich einzuloggen: ")
    file = open(login + "_Merkzettel.txt", "a")
    filePath = login + "_Merkzettel.txt"
    file.close()
    while loggedIn:
        print("1 - Merkzettel anzeigen")
        print("2 - Neue Zeile zum Merkzettel hinzufügen")
        print("3 - Letzte Zeile vom Merkzettel entfernen")
        print("4 - Alle Zeilen vom Merkzettel entfernen")
        print("5 - Ausloggen")
        print("6 - Programm schließen")
        action = input("Was willst du machen?")
        if action == "1":
            file = open(filePath, "r")
            lines = file.readlines()
            c = 0
            while c < len(lines):
                print(str(c + 1), lines[c])
                c += 1
            file.close()
        elif action == "2":
            file = open(filePath, "a")
            file.write(input("Schreibe eine neue Zeile: ") + "\n")
            file.close()
        elif action == "3":
            file = open(filePath, "r")
            lines = file.readlines()
            file.close()
            file = open(filePath, "w")
            c = 0
            while c < len(lines) - 1:
                file.write(lines[c])
                c += 1
            file.close()
        elif action == "4":
            file = open(filePath, "w")
            file.close()
        elif action == "5":
            loggedIn = False
        elif action == "6":
            loggedIn = False
            exitProgram = True
