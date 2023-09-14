def draw_board():
    str = ""
    for c in range(0, 9):
        str += board[c] + "|"
        if (c + 1) % 3 == 0:
            print("|" + str)
            str = ""


board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
playerNum = 1
playerChars = ["X", "O"]

draw_board()
