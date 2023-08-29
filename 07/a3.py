str = input("Gib was ein: ")
reversed = ""
num = len(str) - 1
while num >= 0:
    reversed += str[num]
    num -= 1
print(reversed)
