board = ["1","2","3","4","5","6","7","8","9"]
WinCombination = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]


def display_board():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_winner():
    for i in WinCombination:
        if board[i[0]] == "X" and board[i[1]] == "X" and board[i[2]] == "X":
            print("X won")

def move(player):
    position = int(input("Where do you wanna place your marker? ")) 
    board[position - 1] = player

display_board()

move("X")

display_board()

check_winner()


# To be used later maybe??
#class player:
#    def __init__(self, name, symbol):
#        name = ""
#        symbol = ""
