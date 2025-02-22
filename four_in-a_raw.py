ROWS = 6
COLS = 7
board = [[" " for _ in range(COLS)] for _ in range(ROWS)]


def print_board():
    for row in board:
        print("|".join(row))
    print("-" * (COLS * 2 - 1))


def drop_piece(col, piece):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = piece
            return row
    return -1


def check_winner():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] != " ":
                if col + 3 < COLS and all(
                    board[row][col + i] == board[row][col] for i in range(4)
                ):
                    return True
                if row + 3 < ROWS and all(
                    board[row + i][col] == board[row][col] for i in range(4)
                ):
                    return True
                if (
                    row + 3 < ROWS
                    and col + 3 < COLS
                    and all(
                        board[row + i][col + i] == board[row][col] for i in range(4)
                    )
                ):
                    return True
                if (
                    row - 3 >= 0
                    and col + 3 < COLS
                    and all(
                        board[row - i][col + i] == board[row][col] for i in range(4)
                    )
                ):
                    return True
    return False


def play_game():
    turn = 0
    while True:
        print_board()
        col = int(
            input(f"Player {'1' if turn % 2 == 0 else '2'}: Choose a column (0-6): ")
        )
        if col < 0 or col >= COLS:
            print("Invalid column, try again.")
            continue
        piece = "X" if turn % 2 == 0 else "O"
        row = drop_piece(col, piece)
        if row == -1:
            print("Column is full, try again.")
            continue
        if check_winner():
            print_board()
            print(f"Player {'1' if turn % 2 == 0 else '2'} wins!")
            break
        turn += 1
        if all(board[0][col] != " " for col in range(COLS)):
            print_board()
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game()
