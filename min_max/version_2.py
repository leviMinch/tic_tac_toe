import random
from os import system
from rich import print

player, computer, default = "o", "x", "-"
global one, two, three, winner

board = [
    [default, default, default],
    [default, default, default],
    [default, default, default]
    ]

def board_to_string():
    board_text = ""
    #runs through every positition on board
    for i in range(3):
        for j in range(3):
            board_text += board[i][j]
            #if its not the last posittion in a column add a "|" to seperate positions
            if j <2:
                board_text += " | "
        board_text += "\n"
    return board_text

def board_to_string_color():
    global one,two,three,winner
    if winner == "player" :
        for i in range(3):
            for j in range(3):
                #check to see if its a winning square:
                if (one[0] == i and one[1] == j) or (two[0] == i and two[1] == j) or (three[0] == i and three[1] == j):
                    #assigns color if it's a winning square 
                    print("[green]o", end="")
                else:
                    print(board[i][j], end="")
                #if its not the last posittion in a column add a "|" to seperate positions
                if j <2:
                    print(" | ", end="")
            print()
    
    if winner == "computer" :
        for i in range(3):
            for j in range(3):
                #check to see if its a winning square:
                if (one[0] == i and one[1] == j) or (two[0] == i and two[1] == j) or (three[0] == i and three[1] == j):
                    #assigns color if it's a winning square 
                    print("[red]x", end="")
                else:
                    print(board[i][j], end="")
                #if its not the last posittion in a column add a "|" to seperate positions
                if j <2:
                    print(" | ", end="")
            print()

#if the computer won return 1, if player won return -1, assigns one, two, and three to the win locations. Assigns winner with the correct winner
def evaluate():
    global one,two,three,winner
    #horizontal 
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == player:
                one = row,0
                two = row,1
                three = row,2
                winner = "player"
                return -1
            if board[row][0] == computer:
                one = row,0
                two = row,1
                three = row,2
                winner = "computer"
                return 1
    #vertical 
    for col in range (3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == player: 
                one = 0,col
                two = 1,col
                three = 2,col
                winner = "player"
                return -1
            if board[0][col] == computer:
                one = 0,col
                two = 1,col
                three = 2,col
                winner = "computer"
                return 1
    #diagonal:
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == player:
            one = 0,0
            two = 1,1
            three = 2,2
            winner = "player"
            return -1
        if board[0][0] == computer: 
            one = 0,0
            two = 1,1
            three = 2,2
            winner = "computer"
            return 1
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == player:
            one = 0,2
            two = 1,1
            three = 2,0
            winner = "player"
            return -1
        if board[0][2] == computer:
            one = 0,2
            two = 1,1
            three = 2,0
            winner = "computer"
            return 1

def game_over():
    int = evaluate()
    if int == 1 or int == -1:
        win_analy()
        return True
    for i in range(3):
        for j in range(3):
            #if there is a position not taken then the game is still going on
            if board[i][j] == default:
                return False
    #if every position is taken then the game must be over
    win_analy()
    return True


##MIN MAX
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
    
    x = best_move[0]
    y = best_move[1]
    board[x][y] = computer
##END OF MIN MAX
#function picks a random open spot to claim for the computer
def take_turn():
    x = random.randint(0,2)
    y = random.randint(0,2)
    #checks to see if spot is taken if it is not it takes it
    #if spot is taken it simply re-runs this program to try a new random spot
    if board[x][y] == default:
        board[x][y] = computer
    else:
        take_turn()

#prints message based on who won
def win_analy():
    system("clear")
    board_to_string_color()
    if evaluate() == 1:
        print("I won, Good Game!")
    elif evaluate() == -1:
        print("You won, Good Game!")
    elif evaluate() == 0:
        print("It's a tie, Good Game!")
    else:
        print("ERROR")

def user_turn():
    system('clear')
    print(board_to_string())
    print("Choose a location (1-3,1-3)")
    location = input()
    x = location[0]
    y = location[2]
    #check for valid input
    if x == "1" or x =="2" or x=="3" and y == "1" or y =="2" or y== "3":
        x = int(location[0])-1
        y = int(location[2])-1
        #check for valid spot
        if board[x][y] == default:
            board[x][y] = player
        else:
            user_turn_error()      
    else:
        user_turn_error()

#same as user_turn() but with an error message
def user_turn_error():
    system('clear')
    print(board_to_string())
    print("last location was invalid.")
    print("Choose a location (1-3,1-3)")
    location = input()
    x = location[0]
    y= location[2]
    if x == "1" or x =="2" or x=="3" and y == "1" or y =="2" or y== "3":
        x = int(location[0])-1
        y = int(location[2])-1
        if board[x][y] == default:
            board[x][y] = player
        else:
            user_turn_error()      
    else:
        user_turn_error()

while not game_over():
    take_turn()
    if not game_over():
        user_turn()