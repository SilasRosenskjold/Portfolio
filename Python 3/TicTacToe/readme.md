## TicTacToe 2Player

**What it does**
This is a simple attempt at creating a TicTacToe game. 

**How it works**
More or less the actual "game" is a dictionary consisting of 9 keys starting with a value of " ". The players then choose a position to play by entering a number 1-9, and their piece is then added to that position. The board is printed out after each move is made, with strings referencing the dictionary.
To check for victories I have created a list for each possible victory, for example position 1-4-7. To check whether any possible victory has been achieved, I reference the master list of possible victories, and check whether the len(set) of the three corresponding keys in the dictionary is == 1 (which means they all contain the same character) and I include a: " " not in x(the 3 keys in the dictionary). I added this so that it can't count three empty positions as a victory.

The code is still performing poorly and I suspect it is running through the different functions far more than it needs to. So this is still very much a work in progress still.
On a positive note I'm quite proud of the result, seeing as this is my first project besides creating singular functions. I was recommended by a friend to have many functions instead of piling up several things in one function, because it makes the code easier to debug and easier to read. I think I found a good balance between functions and commands in this project.

Any comments and feedback are appreciated :)
