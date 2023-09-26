def GetFromCSV(line):
    strs = []
    str = ""
    strs.append()
    strs.append(str)
    return strs


file = open("hofladen.csv", "r")
lines = file.readlines()

produkte = []
for line in lines:
    produkte.append(line.strip().split("t"))

print(lines[0])
print(GetFromCSV(lines[0]))