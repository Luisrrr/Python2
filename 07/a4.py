import random

while True:
    max = 0
    min = 0
    num = random.randint(0, 100)
    print(num)
    userInput = 100
    attempts = 0
    won = True

    while int(userInput) != num:
        if attempts == 5:
            print("Zu viele Versuche!")
            won = False
            break
        attempts += 1
        if int(userInput) > num:
            max = userInput
        if int(userInput) < num:
            min = userInput

        print("Zahl ist zwischen " + str(min) + " und " + str(max))
        userInput = input()

    if won:
        print("Richtig in " + str(attempts) + " Versuchen. Nochmal? y/n")
    else:
        print("Nochmal? y/n")
    userInput = input()
    if userInput == "n":
        break
