import random

def print_board(board):
    print("\n")
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])


def check_winner(board, player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


def computer_move(board):
    empty = [i for i in range(9) if board[i] == " "]
    return random.choice(empty)


def tic_tac_toe():
    board = [" "] * 9

    for turn in range(9):

        print_board(board)

        pos = int(input("Your move (1-9): ")) - 1

        if board[pos] != " ":
            print("Position already taken! Try again.")
            continue

        board[pos] = "X"

        if check_winner(board, "X"):
            print_board(board)
            print("You win!")
            return

        comp = computer_move(board)
        board[comp] = "O"
        print(f"Computer chose position {comp+1}")

        if check_winner(board, "O"):
            print_board(board)
            print("Computer wins!")
            return

    print_board(board)
    print("It's a draw!")

tic_tac_toe()