import random

# 1
x = random.randint(-1000, 1000)
print("Zuffalszahl x von -1000 bis 1000: " + str(x))
y = random.randint(1, 50)
print("Zuffalszahl y von 1 bis 50: " + str(y))
z = random.randint(-10, 10)
print("Zuffalszahl z von -10 bis 10: " + str(x))

print("Summe von x, y, z: " + str(x + y + z))
print("Differenz von x und y: " + str(x - y))
print("Produkt von x, y, z: " + str(x * y * z))
print("Quotient von x, y: " + str(x / y))
print("y hoch z: " + str(y ** z))
print("y passt", str(round(x / y)), "mal in x, und der Rest ist", str(x % y))
print("y ** 2 / (x ** 0 - 1)  <--- Man kann nicht durch 0 teilen")
