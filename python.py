
print("hello there")

def print_board(board):
    """Prints the Tic Tac Toe board."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Checks if a player has won."""
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    """Checks if the board is full (draw)."""
    return all(cell != ' ' for row in board for cell in row)

def tic_tac_toe():
    """Main function to play Tic Tac Toe."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    while True:
        print_board(board)
        print(f"Player {players[current_player]}'s turn")

        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))

            if board[row][col] != ' ':
                print("Cell already occupied. Try again!")
                continue

            board[row][col] = players[current_player]

            if check_winner(board, players[current_player]):
                print_board(board)
                print(f"Player {players[current_player]} wins!")
                break

            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = 1 - current_player

        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")

if __name__ == "__main__":
    tic_tac_toe()
