betrag = int(input("Welchen Betrag willst du anlegen?\n"))
gebuehrEuro = 0
gebuehrProzent = 0
gebuehr = 0

if betrag < 1000:
    gebuehrEuro = 3
elif betrag < 2000:
    gebuehrEuro = 1.5
elif betrag > 50000:
    gebuehrProzent = 1.5

if betrag > 100000:
    gebuehrProzent += (betrag - 100000) * 0.05

gebuehr = gebuehrEuro + (betrag * gebuehrProzent / 100)

print((betrag - gebuehr), "€ | Gebühren:", gebuehr, "€ | Prozent:", gebuehrProzent)
