board = ["1","2","3","4","5","6","7","8","9"]



def display_board():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

display_board()

input() # blank input
board[3] = "X"
board[4] = "X"
board[5] = "X"

display_board()


# To be used later maybe??
#class player:
#    def __init__(self, name, symbol):
#        name = ""
#        symbol = ""
