def draw_board():
    str = ""
    for c in range(0, 9):
        str += board[c] + "|"
        if (c + 1) % 3 == 0:
            print("|" + str)
            str = ""


def is_winner(char):
    # Horizontal
    if board[0] == char and board[1] == char and board[2] == char:
        return True
    if board[3] == char and board[4] == char and board[5] == char:
        return True
    if board[6] == char and board[7] == char and board[8] == char:
        return True
    # Vertical
    if board[0] == char and board[3] == char and board[6] == char:
        return True
    if board[1] == char and board[4] == char and board[7] == char:
        return True
    if board[2] == char and board[5] == char and board[8] == char:
        return True
    # Diagonal
    if board[0] == char and board[4] == char and board[8] == char:
        return True
    if board[2] == char and board[4] == char and board[6] == char:
        return True

    return False


def board_contains_number():
    for char in board:
        if char.isnumeric():
            return True
    return False


playerChars = ["X", "O"]
playerNum = 1

while True:

    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    gameEnded = False

    draw_board()

    while gameEnded == False:
        num = 0
        while True:
            num = int(input("Spieler " + str(playerNum) + " (" + playerChars[playerNum - 1] + ") ist dran:"))
            if board[num - 1].isnumeric() == True:
                break

        board[num - 1] = playerChars[playerNum - 1]

        print("\n")
        draw_board()

        if is_winner(playerChars[playerNum - 1]):
            print("Spieler", playerNum, "(" + playerChars[playerNum - 1] + ") hat gewonnen!")
            gameEnded = True
        elif board_contains_number() == False:
            print("Unentschieden!")
            gameEnded = True

        if playerNum == 1:
            playerNum = 2
        else:
            playerNum = 1

    if input("Nochmal spielen? (y/n) ") != "y":
        break
