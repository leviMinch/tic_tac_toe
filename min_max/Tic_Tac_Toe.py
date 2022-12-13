import random
#https://www.pico.net/kb/what-algorithm-for-a-tic-tac-toe-game-can-i-use-to-determine-the-best-move-for-the-ai/
#https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/
#https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/

#articles on minmax:
#1: https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/
#2: https://www.geeksforgeeks.org/introduction-to-evaluation-function-of-minimax-algorithm-in-game-theory/
#3: https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/?ref=rp

#simple grid display 

#creating grid:

Row0 = ["-", "-" , "-"]
Row1 = ["-", "-" , "-"] 
Row2 = ["-", "-" , "-"]
board = [Row0, Row1, Row2]

def print_board():
    print()
    print(board[0][0],"|",board[0][1], "|", board[0][2])
    print(board[1][0],"|",board[1][1], "|", board[1][2])
    print(board[2][0],"|",board[2][1], "|", board[2][2])
    print()


#checks to see if there is a tie by searching for any untaken spot which would have the value "-"
#if there is no remaining open spots then we know that the board is full
def tie():
    x=0
    y=0
    while y < 3:
        while x < 3:
            if board[y][x] == "-":
                return False
            x+=1
        x = 0
        y+=1
    return True

#checks to see if there is three in a row of the "input" which will be "X" or "O"
def win_con(input):
    #horizontal wins
    if board[0][0] == board[0][1] == board[0][2] == input:
        return True
    if board[1][0] == board[1][1] == board[1][2] == input:
        return True
    if board[2][0] == board[2][1] == board[2][2] == input:
        return True
    #vertical wins:
    if board[0][0] == board[1][0] == board[2][0] == input:
        return True
    if board[0][1] == board[1][1] == board[2][1] == input:
        return True 
    if board[0][2] == board[1][2] == board[2][2] == input:
        return True 
    #crisscross wins:
    if board[0][0] == board[1][1] == board [2][2] == input:
        return True
    if board[0][2] == board[1][1] == board [2][0] == input:
        return True
    return False
#prints the winning message
def winAnaly():
    print("game over...")
    print_board()
    if tie():
        print("Tie, good game!")
    elif win_con("O"):
        print("I won, good game!")
    elif win_con("X"):
        print("You won, good game!")
    else:
        print("error")

#function picks a random open spot to claim for the computer
def take_turn():
    x = random.randint(0,2)
    y = random.randint(0,2)
    #checks to see if spot is taken if it is not it takes it
    #if spot is taken it simply re-runs this program to try a new random spot
    if board[x][y] == "-":
        board[x][y] = "O"
    else:
        take_turn()




#minimax:
def gameOver():
    for y in range(3):
        for x in range(3):
            if board[y][x] == "-":
                return False
    return True

# def evaluate():
#     if win_con("O"):
#         return 10
#     if win_con("X"):
#         return -10
#     return 0
def evaluate():
    for row in range(3):
        if(board[row][0] == board[row][1] == board[row][2]):
            if board[row][0] == "O":
                return 10
                
        if(board[row][0] == board[row][1] == board[row][2]):
            if board[row][0] == "X":
                return -10
    for col in range(3) :
        if (board[0][col] == board[1][col] and board[1][col] == board[2][col]) :
            if (board[0][col] == "O") :
                return 10
            elif (board[0][col] == "X") :
                return -10
 
    # Checking for Diagonals for X or O victory.
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) :
        if (board[0][0] == "O") :
            return 10

        elif (board[0][0] == "X") :
            return -10
 
    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]) :
     
        if (board[0][2] == "O") :
            return 10
        elif (board[0][2] == "X") :
            return -10
    
def minimax(depth, ismax):
    score = evaluate()

    if score == 10:
        return score
    if score == -10:
        return score
    if gameOver():
        return 0
    
    if (ismax):
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j]== "-":
                    board[i][j] = "O"
                    best  = max(best, minimax(depth +1, not ismax))
                    board[i][j] ="-"
        return best
    
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] =="-":
                    board[i][j] = "O"
                    best = min(best, minimax(depth +1, not ismax))
                    board[i][j] = "-"
        return best

def makeMove():
    best_val = -1000
    best_move = (-1,-1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                board[i][j] = "O"
                move_val = minimax(0, False)
                board[i][j]= "-"

                if(move_val > best_val):
                    best_move = (i,j)
                    best_val = move_val
    board[i][j] = "O"
    #print("The best move is:", best_move, "with a value of:", best_val)

def main():
    print("-----------------------")
    print("Welcome to Tic Tac Toe")
    print("You will be X's and I will be O's")
    input()
    while not win_con("O") and not win_con("X") and not tie():
        print_board()
        print("input location for a new spot (1-3,1-3)")
        location = input()
        #check to see if input is valid
        if (location[0] == "1" or location[0] == "2" or location[0] == "3") and (location[2] == "1" or location[2] == "2" or location[2] == "3") :
            #converts input into correct location 
            location_x = int(location[0]) -1
            location_y = int(location[2]) -1
            #checks to see if spot is already taken 
            if board[location_x][location_y] == "-":
                board[location_x][location_y] = "X"
                #checks to see if taking this spot results in a tie
                if not tie() or not win_con("X"):
                    ##take_turn()
                    makeMove()
                else:
                    break
            else:
                print("this spot is already taken, please choose a new one")
                input()
        else:
            print("non valid spot, please choose a new one")
            input()
    
    winAnaly()

main()



