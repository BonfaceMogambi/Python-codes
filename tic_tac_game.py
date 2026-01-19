from random import randrange

# =========================
# Initialize the board
# =========================
board = [[str(3 * i + j + 1) for j in range(3)] for i in range(3)]
board[1][1] = 'X'  # Computer first move in the center

# =========================
# Display the board
# =========================
def display_board(board):
    for i in range(3):
        print("+-------+-------+-------+")
        for _ in range(3):
            print("|       |       |       |")
        print(f"|   {board[i][0]}   |   {board[i][1]}   |   {board[i][2]}   |")
        for _ in range(3):
            print("|       |       |       |")
    print("+-------+-------+-------+")

# =========================
# User move
# =========================
def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move: "))
            if move < 1 or move > 9:
                print("Invalid input! Must be 1-9.")
                continue
            row = (move-1)//3
            col = (move-1)%3
            if board[row][col] in ['X','O']:
                print("Square already occupied!")
                continue
            board[row][col] = 'O'
            break
        except ValueError:
            print("Invalid input! Enter an integer.")

# =========================
# List of free fields
# =========================
def make_list_of_free_fields(board):
    free = [(i,j) for i in range(3) for j in range(3) if board[i][j] not in ['X','O']]
    return free

# =========================
# Check for victory
# =========================
def victory_for(board, sign):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)):
            return True
        if all(board[j][i] == sign for j in range(3)):
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False

# =========================
# Computer move
# =========================
def draw_move(board):
    free = make_list_of_free_fields(board)
    if free:
        i,j = free[randrange(len(free))]
        board[i][j] = 'X'

# =========================
# Game loop
# =========================
display_board(board)

while True:
    # User move
    enter_move(board)
    display_board(board)
    if victory_for(board, 'O'):
        print("You won!")
        break
    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break

    # Computer move
    draw_move(board)
    display_board(board)
    if victory_for(board, 'X'):
        print("Computer wins!")
        break
    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break
