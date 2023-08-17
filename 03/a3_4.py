# 3.
name = input("Wie heißt du?\n")
alter = input("Wie alt bist du?\n")
geld = input("Wie viel Geld hast du?\n")
print(name, "ist", alter, "Jahre alt und hat", geld, "€ in der Tasche")

# 4.
base_preis = float(input("Wie viel soll die Kleidung kosten?\n"))
rabatt = float(input("Wie viel % Rabatt soll es geben?\n"))
final_preis = base_preis * rabatt / 100
print("Der Preis ist wegen dem Rabatt von", base_preis, "€ auf", final_preis, "€ runtergegangen")