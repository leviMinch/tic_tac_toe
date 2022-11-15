This is a basic tic tac toe game where the user plays against the computer. 

How the computer makes its moves: 
the computer makes its moves by choosing a random spot and assing if the spot is empty, if the spot is empty it will then choose this spot. If the spot is not empty it re-calls the function (recursion) in order to choose a new random spot. This loop will continue until a random spot is chose.

Win Conditions Function: 
This function will check all possible win conditions for the given input (The input is always 'X' or 'O'). 

Tie function:
The tie function will parse through every single box and return False if it detects an open box. If it does not detect an open box then we can deduct that the game is a tie, resulting in a return value of True. 