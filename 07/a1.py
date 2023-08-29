import random

count = -20
string = ""
while count < 21:
    string += str(count) + ", "
    count += 1
print("Von -20 bis 20 gezählt:", string, "...")

print("100 bis 0 Countdown:\n")
count = 100
while count > 0:
    print(count)
    count -= 1

print("7er Reihe:\n")
count = 7
while count < 100:
    print(count)
    count += 7

print("Quadratzahlen:\n")
count = 0
res = 0
while res < 1000:
    print(res)
    res = count * count
    count += 1

string = ""
while count != 7:
    count = random.randint(1, 10)
    string += str(count) + ", "
print("Zufallszahlen von 1 bis 10 bis 7 kommt:", string + "Ende")

string = ""
while string != "Exit":
    string = input("Gib irgendwas ein. \"Exit\" um weiter zu gehen.\n")

print("Würfeln bis zum Pasch:\n")
num1 = 1
num2 = 2
while num1 != num2:
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    print(num1, num2)

print("Alle möglichen Würfelkombinationen:\n")
num1 = 0
num2 = 1
while num2 != 7:
    while num1 != 6:
        num1 += 1
        print(num1, num2)
    num2 += 1
    num1 = 0
