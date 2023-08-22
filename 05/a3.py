name = input("Hallo, wie ist dein Name?\n")
produkte = ["Äpfel", "Birnen", "Erdbeeren", "Kartoffeln", "Eier"]
print("Wir haben heute folgende Produkte im Angebot:", produkte)
wunsch = input("Welches Produkt willst du?\n")
if produkte.count(wunsch) > 0:
    print("Bitte schön, hier sind ihre", wunsch + ".")
    preise = [2.59, 2.79, 4.29, 5.99, 2.29]
    print("Das kostet", preise[produkte.index(wunsch)])
else:
    print("Schade, wir haben leider keine", wunsch + ".")

print("Tschüß, bis zum nächsten Mal,", name + "!")
