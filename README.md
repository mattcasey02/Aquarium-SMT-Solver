___________________________________________________________________________________________
Before encoding a board state or even running the program, you must download the z3 library.
This is found at : https://github.com/Z3Prover/z3
___________________________________________________________________________________________

How to use our SMT-Based Aquarium Solver:

First, go to the website: https://www.puzzle-aquarium.com/
Select a board size to solve. For simplicity, it is easiest to choose a 6x6 board as 
encoding it takes the least amount of time.

Then you must create a list of list of integers (loloi), as seen in image ____, to represent
an initial board state.

Creating this loloi is fairly convoluted and must be created correctly for the program to work

The general process of creating this loloi is adding in 1s or 0s to represent aquarium borders
or the lack thereof, respectfully. Thus, you must vertically transcribe these lists of integers
from the top to the bottom of the board.

1. The first list in your loloi will correspond to the column hints provided by the board.
   This means that for a 6x6 board, this first list will have a length of six whoose elements 
   correspond to the values at the top of the board.

2. The second list will be a list of 1s whose length corresponds to the width of the board.
   This represents the top border of the board which must be completely filled with aquarium borders.

3. The third list will correspond to the first row of the board. Thus, the first integer in the
   list will be the row's numerical hint value. The following integers in that list will correspond
   to vertical borders (1) or the lack thereof (0). It will have a size of the board's with + 2. 
   Additionally, the last integer in the list must be 1 as that represents the board's border 
   for that row.

4. The fourth list will correspond to the horizontal borders underneath the row we just transcribed.
   This will have a length that corresponds to the width of the board.

5. The following lists will be transcribed by following steps 3 and 4. They will represent either
   horizontal borders or vertical borders with a row hint as well.

6. Finally, the last list will be another list of 1s whose length corresponds to the width 
   of the board. This list represents the bottom border of the board.

7. ** To run the program, you must point the variable "instance" to the newly created loloi board

Qualitative Notes:
To Ensure your loloi is written correctly:

* the length of your loloi should be 2 * (h + 1), where h represents the height of the board.
  Thus, as a result of transcribing a 6x6 board, the length of your loloi should be 2 * (6 + 1) = 2 * 7 = 14
* Every list corresponding to horizontal boarders should start with a row's hint, be followed by 1, and
  end with 1 as well. These lists should also have a length of w + 2, where w represents the width of the board
* The second and last list in your loloi should be all 1s and should have a length of w
