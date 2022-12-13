player, computer, default = "O", "X", "-"
def board_print():
    for i in range(3):
        for j in range(3):
            print(board[i][j], end = "")
            if j < 2:
                print("|", end = "")
        print()

def evaluate(board):
    #checking for vertical win 
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            if board[row][0] == computer:
                return 1
            elif board[row][0] == player:
                return -1
    #checking for horizontal win
    for col in range(3):
        if board[0][col] == board[1][col] and board[row][1] == board[2][col]:
            if board[0][col] == computer:
                return 1
            elif board[0][col] == player:
                return -1
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == computer:
            return 1
        elif board[0][0] == player:
            return -1
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == computer:
            return 1 
        elif board[0][2] == player:
            return -1 

def game_over():
    for i in range(3):
        for j in range(3):
            if board[i][j] == default:
                return False
    return True

def min_max(board,depth, is_turn):
    score = evaluate(board)
    if score == 1:
        return score
    
    elif score == -1:
        return score
    
    elif game_over():
        return 0 
    if(is_turn):
        best = -1000

        for i in range(3):
            for j in range(3):

                if board[i][j] == default:
                    board[i][j] = computer
                    best = max(best, min_max(board, depth+1, not is_turn))
                    board[i][j] = default
        return best
    else: 
        best = 1000

        for i in range(3):
            for j in range(3):

                if board[i][j] == default:

                    board[i][j] = player
                    best = min(best, min_max(board, depth+1, not is_turn))
                    board[i][j] = default
        return best
def find_best_move():
    best_value = -1000
    best_move = (-1,-1)

    for i in range(3):
        for j in range(3):

            if board[i][j] == default:
                board[i][j] = computer
                move_val = min_max(board, 0, False)
                board[i][j] = default

                if move_val > best_value:
                    best_move = (i,j)
                    best_value = move_val
    
    print("The value of the best move is:", best_value)
    return best_move
    
board = [["X", "O", "X"],
         ["O", "X", "-"],
         ["-", "-", "O"]]

def main():
    board_print()
    best_move = find_best_move()
    print("the best move is:\n ROW:", best_move[0], "COL:", best_move[1])

main()