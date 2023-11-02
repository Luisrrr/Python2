import NumberFormatter


suffixes = ["", "K", "M", "B", "T", "Qa", "Qt", "Sx", "Sp", "Oc", "No"]

generators = [0, 0, 0, 0, 0, 0, 0, 0]
mults = [1, 1, 1, 1, 1, 1, 1, 1]
number = 10

while True:
    generatorStrs = []
    multStrs = []
    for c in range(0, 7):
        generators[c] += generators[c + 1] * mults[c + 1]

        generatorStrs.append(NumberFormatter.format(generators[c]))
        multStrs.append(NumberFormatter.format(mults[c]))

    generatorStrs.append(NumberFormatter.format(generators[7]))
    multStrs.append(NumberFormatter.format(mults[7]))

    lastNumber = number
    number += generators[0] * mults[0]

    percentageGain = round(((number - lastNumber) + 1) / number * 100)
    print()
    print("Number:", NumberFormatter.format(number), "(+" + str(percentageGain) + "%)")
    print("Generators:", generatorStrs)
    print("Multipliers:", multStrs)

    print()
    print("(1) Increase generator")
    print("(2) Increase multiplier")

    action = input("Enter for next tick\n")
    if action == "1":
        index = int(input("Generator index: "))
        amount = float(input("Amount: "))
        generators[index] += amount
    elif action == "2":
        index = int(input("Multiplier index: "))
        amount = float(input("Amount: "))
        mults[index] += amount
