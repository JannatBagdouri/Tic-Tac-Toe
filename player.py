def ask_for_player_move():
    "Prompts the current player to enter their move (row and column)."
    x = int(input("Enter x coordinate (0 to 2): "))
    y = int(input("Enter y coordinate (0 to 2): "))
    return x, y

def check_if_valid(x, y):
    "Returns True if the move is within bounds."
    return 0 <= x < 3 and 0 <= y < 3

def is_valid_move(board, x, y):
    "Returns True if the move is valid (within the board and on an empty spot)."
    return check_if_valid(x, y) and board[x][y] == "_"

def update_game_board(board, x, y, player_mark):
    "Places the player's mark on the board."
    board[x][y] = player_mark