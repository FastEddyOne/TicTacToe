import sys

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-"*5)

def check_winner(board, player):
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def get_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                moves.append((i, j))
    return moves

def player_move(board):
    move = None
    while move not in get_moves(board):
        user_input = input("Enter your move (row col): ")
        try:
            # Ensure input contains two space-separated values
            if len(user_input.split()) != 2:
                raise ValueError("Input must contain two numbers, separated by a space.")
            
            # Convert input to tuple of integers
            move = tuple(map(int, user_input.split()))
            
            # Ensure input is within valid range
            if not (0 <= move[0] < 3 and 0 <= move[1] < 3):
                raise ValueError("Indices must be between 0 and 2.")

            # Ensure chosen spot is available
            if board[move[0]][move[1]] != " ":
                raise ValueError("This spot is already taken.")

        except ValueError as ve:
            print(f"Invalid move: {ve}")
            continue
        
    board[move[0]][move[1]] = "X"


def minimax(board, depth, is_maximizing):
    if check_winner(board, "X"):
        return -10
    if check_winner(board, "O"):
        return 10
    if len(get_moves(board)) == 0:
        return 0
    
    if is_maximizing:
        max_eval = -sys.maxsize
        for move in get_moves(board):
            board[move[0]][move[1]] = "O"
            eval = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = " "
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = sys.maxsize
        for move in get_moves(board):
            board[move[0]][move[1]] = "X"
            eval = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = " "
            min_eval = min(min_eval, eval)
        return min_eval

def ai_move(board):
    best_val = -sys.maxsize
    best_move = ()
    for move in get_moves(board):
        board[move[0]][move[1]] = "O"
        move_val = minimax(board, 0, False)
        board[move[0]][move[1]] = " "
        if move_val > best_val:
            best_move = move
            best_val = move_val
    board[best_move[0]][best_move[1]] = "O"

def main():
    board = [[" "]*3 for _ in range(3)]
    while True:
        print_board(board)
        if len(get_moves(board)) == 0:
            print("It's a tie!")
            break
        player_move(board)
        if check_winner(board, "X"):
            print_board(board)
            print("You win!")
            break
        if len(get_moves(board)) == 0:
            print_board(board)
            print("It's a tie!")
            break
        ai_move(board)
        if check_winner(board, "O"):
            print_board(board)
            print("AI wins!")
            break

if __name__ == "__main__":
    main()
