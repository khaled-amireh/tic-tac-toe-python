from random import randrange


def print_board(board):
    print("+-------" * 3 + "+")
    for r in range(3):
        print("|       " * 3 + "|")
        for c in range(3):
            print("|   " + str(board[r][c]) + "   ", end="")
        print("|")
        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")


def user_move(board):
    while True:
        move = input("Enter your move (1-9): ")

        if len(move) != 1 or move < '1' or move > '9':
            print("Invalid input, try again.")
            continue

        move = int(move) - 1
        row = move // 3
        col = move % 3

        if board[row][col] in ['X', 'O']:
            print("This position is already taken.")
            continue

        board[row][col] = 'O'
        break


def get_free_cells(board):
    free = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['X', 'O']:
                free.append((r, c))
    return free


def check_winner(board, symbol):
    if symbol == 'X':
        player = "computer"
    else:
        player = "player"

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == symbol:
            return player
        if board[0][i] == board[1][i] == board[2][i] == symbol:
            return player

    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return player

    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return player

    return None


def computer_move(board):
    free = get_free_cells(board)
    if free:
        r, c = free[randrange(len(free))]
        board[r][c] = 'X'


board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
board[1][1] = 'X'

free = get_free_cells(board)
player_turn = True
winner = None

while free:
    print_board(board)

    if player_turn:
        user_move(board)
        winner = check_winner(board, 'O')
    else:
        computer_move(board)
        winner = check_winner(board, 'X')

    if winner:
        break

    player_turn = not player_turn
    free = get_free_cells(board)

print_board(board)

if winner == "player":
    print("You won!")
elif winner == "computer":
    print("Computer won!")
else:
    print("Draw!")