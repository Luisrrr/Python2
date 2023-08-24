name = input("Hallo, wie ist dein Name?\n")
produkte = ["Äpfel", "Birnen", "Erdbeeren", "Kartoffeln", "Eier"]
# 4 Äpfel, 1 Birne, 6 Erdbeeren, 10 Kartoffeln, 0 Eier
mengen = [4, 1, 6, 10, 0]
print("Wir haben heute folgende Produkte im Angebot:", produkte)
wunsch = input("Welches Produkt willst du?\n")
wunschIndex = produkte.index(wunsch)
wunschMenge = int(input("Wie viel willst du davon?\n"))
if produkte.count(wunsch) > 0:
    if wunschMenge <= mengen[wunschIndex]:
        print("Bitte schön, hier sind ihre", wunsch + ".")
        preise = [2.59, 2.79, 4.29, 5.99, 2.29]
        print("Das kostet", preise[wunschIndex])
    else:
        string = "Wir haben leider nur " + str(mengen[wunschIndex]) + " " + wunsch +\
                 ". Soll ich die fehlenden " + str(wunschMenge - mengen[wunschIndex]) + " für morgen bestellen?"
        input(string + "\n")
else:
    print("Schade, wir haben leider keine", wunsch + ".")

print("Tschüß, bis zum nächsten Mal,", name + "!")
