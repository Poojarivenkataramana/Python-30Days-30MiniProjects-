# ----------------------------------------------------
# Day 20: Tic-Tac-Toe Game (2-Player & Computer AI Mode)
# Concepts: 2D Grid / Lists, Win Matrix Verification, Game Loops, AI Minimax / Heuristic
# ----------------------------------------------------

import random

def print_board(board):
    print()
    print(f" {board[0]} │ {board[1]} │ {board[2]} ")
    print("───┼───┼───")
    print(f" {board[3]} │ {board[4]} │ {board[5]} ")
    print("───┼───┼───")
    print(f" {board[6]} │ {board[7]} │ {board[8]} ")
    print()

def check_winner(b, mark):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    return any(all(b[idx] == mark for idx in pattern) for pattern in win_patterns)

def is_board_full(b):
    return all(cell in ("X", "O") for cell in b)

def get_smart_ai_move(board, ai_mark, human_mark):
    available = [i for i in range(9) if board[i] not in ("X", "O")]

    # 1. Check if AI can win in the next move
    for move in available:
        temp = board[:]
        temp[move] = ai_mark
        if check_winner(temp, ai_mark):
            return move

    # 2. Check if Human could win next move and block them
    for move in available:
        temp = board[:]
        temp[move] = human_mark
        if check_winner(temp, human_mark):
            return move

    # 3. Take center if available
    if 4 in available:
        return 4

    # 4. Take corners
    corners = [i for i in [0, 2, 6, 8] if i in available]
    if corners:
        return random.choice(corners)

    # 5. Take any open spot
    return random.choice(available)

def play_game():
    print("=" * 45)
    print("⭕ ❌ TIC - TAC - TOE ❌ ⭕".center(45))
    print("=" * 45)
    print("1. Two Players (Pass & Play)")
    print("2. Single Player (vs Smart AI)")

    mode = input("\nSelect Mode (1/2): ").strip()
    vs_ai = (mode == "2")

    # Board indices 1-9
    board = [str(i) for i in range(1, 10)]
    current_player = "X"

    print("\nPositions are numbered from 1 to 9 as shown below:")
    print_board(board)

    while True:
        if vs_ai and current_player == "O":
            print("🤖 Computer is thinking...")
            move = get_smart_ai_move(board, "O", "X")
            board[move] = "O"
            print(f"Computer placed 'O' at spot {move + 1}")
        else:
            while True:
                try:
                    spot = int(input(f"Player '{current_player}', enter position (1-9): "))
                    if 1 <= spot <= 9 and board[spot - 1] not in ("X", "O"):
                        board[spot - 1] = current_player
                        break
                    else:
                        print("❌ Spot already taken or out of range! Try again.")
                except ValueError:
                    print("❌ Please enter a valid number (1-9).")

        print_board(board)

        # Check win
        if check_winner(board, current_player):
            print("*" * 45)
            if vs_ai and current_player == "O":
                print("💻 COMPUTER WON! Better luck next time! 🤖".center(45))
            else:
                print(f"🎉 PLAYER '{current_player}' WINS THE GAME! 🎉".center(45))
            print("*" * 45)
            break

        # Check draw
        if is_board_full(board):
            print("-" * 45)
            print("🤝 IT'S A TIE / DRAW! 🤝".center(45))
            print("-" * 45)
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

def main():
    while True:
        play_game()
        replay = input("\nPlay another round? (yes/no): ").strip().lower()
        if replay not in ("yes", "y"):
            print("\nThanks for playing Tic-Tac-Toe! 👋\n")
            break

if __name__ == "__main__":
    main()
