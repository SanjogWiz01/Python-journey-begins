import math

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    # Check rows, columns, diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)): return True
        if all(board[j][i] == player for j in range(3)): return True
    if all(board[i][i] == player for i in range(3)): return True
    if all(board[i][2 - i] == player for i in range(3)): return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Evaluate board score
def evaluate(board):
    if check_winner(board, "O"):
        return 1
    elif check_winner(board, "X"):
        return -1
    return 0

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    if score == 1 or score == -1:
        return score
    if is_full(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = " "
        return best

# Find best move for AI
def best_move(board):
    best_val = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("🎮 Tic Tac Toe (Unbeatable AI)")
    print("You are X | Computer is O")
    print("Made by Wizard 💙")
    print_board(board)

    while True:
        try:
            move = input("Enter your move (row col): ").split()
            if len(move) != 2:
                print("⚠️ Enter row and column like: 1 2")
                continue

            row, col = int(move[0]) - 1, int(move[1]) - 1
            if row not in range(3) or col not in range(3):
                print("❌ Invalid position! Try again.")
                continue

            if board[row][col] != " ":
                print("⚠️ That spot is taken! Try again.")
                continue

            board[row][col] = "X"
            print_board(board)

            if check_winner(board, "X"):
                print("🎉 You win! (Rare 😅)")
                break

            if is_full(board):
                print("😅 It's a draw!")
                break

            print("💻 Computer's turn...")
            move = best_move(board)
            if move:
                board[move[0]][move[1]] = "O"
            print_board(board)

            if check_winner(board, "O"):
                print("💀 Computer wins! Unstoppable 🤖")
                break

            if is_full(board):
                print("😅 It's a draw!")
                break

        except ValueError:
            print("⚠️ Please enter valid numbers!")

if __name__ == "__main__":
    main()
