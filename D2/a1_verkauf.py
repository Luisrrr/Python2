def get_lists_from_file():
    file = open("hofladen.csv", "r")
    for line in file.readlines():
        splits = line.split(",")
        produkte.append(splits[0])
        mengen.append(splits[1][:-1])


produkte = []
mengen = []
get_lists_from_file()

print(produkte)
print(mengen)