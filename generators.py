generators = [0, 0, 0, 0, 0, 0, 0, 0]
mults = [1, 1, 1, 1, 1, 1, 1, 1]
number = 0

while True:
    for c in range(0, 7):
        generators[c] += generators[c + 1] * mults[c]

    number += generators[0] * mults[0]

    print()
    print("Number:", number)
    print("Generators:", generators)
    print("Multipliers:", mults)

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
