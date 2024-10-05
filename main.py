import random
import math

board = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(" ")
    board.append(row)


def print_board():
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-- -- -- -- -")


def player_move(mark):
    move = int(input(f"Enter player '{mark}' move (1-9): ")) - 1
    if move >= 6:
        i = 2
        j = move - 6
    elif move >= 3:
        i = 1
        j = move - 3
    else:
        i = 0
        j = move
    if board[i][j] == ' ':
        board[i][j] = mark
    else:
        print("Invalid move! Try again.")
        player_move(mark)


def normal_move(board):
    print("Computer Turn")
    possible_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                possible_moves.append([i, j])
    move = random.choice(possible_moves)
    i = move[0]
    j = move[1]
    board[i][j] = "O"


def check_winner(player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[2][0] == board[1][1] == board[0][2] == player:
            return True
    return False


def check_draw(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == " ":
                return False
    return True


def best_move():
    print("Computer Turn")
    best_score = -math.inf
    move = None
    # Check all cells to find the best move for the AI
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"  # AI plays as 'O'
                score = minimax(board, 0, False)
                board[i][j] = " "  # Undo the move
                if score > best_score:
                    best_score = score
                    move = (i, j)
    # Make the best move
    if move:
        board[move[0]][move[1]] = "O"


def minimax(board, depth, is_maximizing):
    if check_winner("O"):
        return 1
    elif check_winner("X"):
        return -1
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "  # Undo the move
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "  # Undo the move
                    best_score = min(score, best_score)
        return best_score


def play_match(match):
    if match == 1:
        normal_move(board)
    elif match == 2:
        best_move()
    else:
        player_move("O")


def play_game():
    print("Welcome to tic tac toe")
    print_board()
    match = int(input("What do you wanna play? 1.Normal match or 2.Impossible \
        match or 3.Two player(1/2/3)"))
    if match > 3:
        print("Wrong Input!! Try again")
        play_game()
    while True:
        player_move("X")
        print_board()
        if check_winner("X"):
            print("Player X wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break
        else:
            play_match(match)
            print_board()
            if check_winner("O"):
                print("Computer Wins!")
                break
            elif check_draw(board):
                print("It's a draw")
                break


play_game()
