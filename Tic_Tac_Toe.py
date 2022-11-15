import random
#https://www.pico.net/kb/what-algorithm-for-a-tic-tac-toe-game-can-i-use-to-determine-the-best-move-for-the-ai/
#https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/

#simple grid display 
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





#creating grid:
Row0 = ["-", "-" , "-"]
Row1 = ["-", "-" , "-"] 
Row2 = ["-", "-" , "-"]
board = [Row0, Row1, Row2]

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
        #converts input into correction location 
        location_x = int(location[0]) -1
        location_y = int(location[2]) -1
        #checks to see if spot is already taken 
        if board[location_x][location_y] == "-":
            board[location_x][location_y] = "X"
            #checks to see if taking this spot results in a tie
            if not tie():
                take_turn()
            else:
                break
        else:
            print("this spot is already taken, please choose a new one")
            input()
    else:
        print("non valid spot, please choose a new one")
        input()


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