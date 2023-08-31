str = input("Den String will ich verschlüsseln:  ").upper()
schluessel = int(input("Gib den Schlüssel ein (1-26): "))
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]
indexes = []
count = 0
while count < len(str):
    indexes.append(alphabet.index(str[count]))
    count += 1
count = 0
while count < len(indexes):
    indexes[count] += schluessel
    if indexes[count] > 25:
        indexes[count] -= 26
    count += 1

res = ""
count = 0
while count < len(str):
    if str[count].isalpha():
        res += alphabet[indexes[count]]
    else:
        res += str[count]
    count += 1
print("Verschlüsselter String:", res)
