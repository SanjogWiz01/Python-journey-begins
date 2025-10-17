import random

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def computer_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    if empty_cells:
        return random.choice(empty_cells)
    return None

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    computer = "O"

    print("🎮 Welcome to Tic Tac Toe (Player vs Computer)")
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

            # Player move
            board[row][col] = player
            print_board(board)

            if check_winner(board, player):
                print("🎉 You win!")
                break

            if is_full(board):
                print("😅 It's a draw!")
                break

            # Computer move
            print("💻 Computer's turn...")
            r, c = computer_move(board)
            board[r][c] = computer
            print_board(board)

            if check_winner(board, computer):
                print("💀 Computer wins!")
                break

            if is_full(board):
                print("😅 It's a draw!")
                break

        except ValueError:
            print("⚠️ Please enter valid numbers!")

if __name__ == "__main__":
    main()
