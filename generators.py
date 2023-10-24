import math

def format(num, alwaysShowDecimals = True, notation = "MixedScientific"):
    if notation == "MixedScientific":
        if num < 1e33:
            return add_suffix(num, alwaysShowDecimals)
        else:
            return format_scientific(num, alwaysShowDecimals)
    elif notation == "Scientific":
        return format_scientific(num, alwaysShowDecimals)


def format_scientific(num, alwaysShowDecimals = True):
    if alwaysShowDecimals:
        return "{:.2E}".format(num).replace("E+", "e")
    else:
        return "{:.2E}".format(num).replace("E+", "e").replace(".00", "")


def add_suffix(num, alwaysShowDecimals = True):
    if num == 0:
        return alwaysShowDecimals if "0.00" else "0"
    if math.log10(num) <= 0:
        return str(num)

    exponent = math.log10(num)
    suffixIndex = math.floor(exponent / 3)

    mantissa = '{0:.2f}'.format(num / (1000 ** suffixIndex))
    mantissa = mantissa[0:mantissa.index(".") + 3]
    if not alwaysShowDecimals and mantissa.__contains__(".00"):
        mantissa = mantissa.split('.')[0]

    suffix = suffixes[suffixIndex]
    formatted = mantissa
    if suffix != "":
        formatted = mantissa + " " + suffix

    return formatted


suffixes = ["", "K", "M", "B", "T", "Qa", "Qt", "Sx", "Sp", "Oc", "No"]

generators = [0, 0, 0, 0, 0, 0, 0, 0]
mults = [1, 1, 1, 1, 1, 1, 1, 1]
number = 10

while True:
    generatorStrs = []
    multStrs = []
    for c in range(0, 7):
        generators[c] += generators[c + 1] * mults[c + 1]

        generatorStrs.append(format(generators[c]))
        multStrs.append(format(mults[c]))

    generatorStrs.append(format(generators[7]))
    multStrs.append(format(mults[7]))

    lastNumber = number
    number += generators[0] * mults[0]

    percentageGain = round(((number - lastNumber) + 1) / number * 100)
    print()
    print("Number:", format(number), "(+" + str(percentageGain) + "%)")
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