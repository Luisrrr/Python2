file = open("passwoerter.txt", "r")
topPasswords = file.readlines()
file.close()
file = open("passwoerter.txt", "r")
uniqpassPasswords = file.readlines()

while True:
    password = input("Passwort was du prüfen willst: ")

    existsInTop100 = False
    existsInUniqpass = False
    if topPasswords.count(password + "\n") != 0:
        existsInTop100 = True
    if uniqpassPasswords.count(password + "\n") != 0:
        existsInUniqpass = True

    if existsInTop100 or existsInUniqpass:
        print("\"" + password + "\" ist unsicher")
        if existsInTop100:
            print("Es existiert in den top 100")
        if existsInUniqpass:
            print("Es existiert in den uniqpass Passwörtern")
    else:
        print("Herzlichen Glückwunsch! Dein Passwort \"" + password + "\" scheint sicher zu sein.")
