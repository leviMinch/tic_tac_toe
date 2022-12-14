This is a basic tic tac toe game where the user plays against the computer. 

How the computer makes its moves: 
the computer makes its moves by choosing a random spot and assing if the spot is empty, if the spot is empty it will then choose this spot. If the spot is not empty it re-calls the function (recursion) in order to choose a new random spot. This loop will continue until a random spot, which is empty, is chosed.

Win conditions:
In order asses win conditions the program sorts through all possible win conditions and then returns if any of them are true. 

Tie function:
The tie function will parse through every single box and return False if it detects an open box. If it does not detect an open box then we can deduct that the game is a tie, resulting in a return value of True. 

Coloring for win path:
In order to color the win path green or red I used the rich (child of the textualize library) library: https://www.textualize.io/

I plan on using this library in further projects as I think it is a very useful library that has the capability to display a wide range of information in a clean presentation.