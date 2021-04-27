from z3 import *

#Corresponds to Instance1 Image
#6x6 easy
instance1 = ((3,5,3,3,3,5), #Column filling requirements
            (1,1,1,1,1,1), #Top row of horizontal walls
            (2,1,0,1,1,0,0,1), #Vertical walls in row 1
            (1,1,0,0,0,1), #Horizontal walls between rows 1&2
            (4,1,0,0,1,0,1,1), #Vertical walls in row 2
            (0,0,1,0,0,0), #Horizontal walls between rows 2&3
            (3,1,0,1,0,0,1,1), #Vertical walls in row 3
            (1,0,1,1,0,1), #Horizontal walls between rows 3&4
            (5,1,1,0,1,1,0,1), #Vertical walls in row 4
            (0,0,0,0,1,0), #Horizontal walls between rows 4&5
            (5,1,1,0,1,0,1,1), #Vertical walls in row 5
            (0,1,1,0,0,0), #Horizontal walls between rows 5&6
            (3,1,0,0,1,0,1,1), #Vertical walls in row 6
            (1,1,1,1,1,1)) #Bottom row of horizontal walls

#Corresponds to Instance2 Image
#6x6 Hard
instance2 = ((5,4,3,2,5,3),
            (1,1,1,1,1,1),
            (5,1,1,0,1,1,0,1),
            (0,1,1,0,1,1),
            (1,1,1,0,1,1,0,1),
            (1,1,1,1,1,1),
            (4,1,0,1,0,1,1,1),
            (1,1,1,1,1,0),
            (3,1,0,1,1,0,1,1),
            (0,0,1,1,1,1),
            (4,1,0,1,1,1,1,1),
            (1,1,0,1,0,0),
            (5,1,0,1,1,0,1,1),
            (1,1,1,1,1,1))

#Corresponds to Instance 3 Image
#6x6 Easy
instance3 = ((5,4,4,2,3,1),
            (1,1,1,1,1,1),
            (2,1,1,0,0,1,0,1),
            (0,0,0,0,1,1),
            (1,1,1,0,0,0,0,1),
            (0,0,0,1,1,1),
            (4,1,1,0,1,1,0,1),
            (0,1,1,0,1,0),
            (5,0,0,0,0,0,1,1),
            (1,0,1,1,0,0),
            (4,1,1,1,1,1,1,1),
            (0,1,0,0,1,0),
            (3,1,0,1,1,0,0,1),
            (1,1,1,1,1,1))

#Corresponds to Instance 4 Image
#15x15 Hard
instance4 = ((9,6,9,11,9,8,7,5,8,8,9,10,10,9,9),
            (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),
            (4,1,0,0,1,0,1,1,0,0,0,0,0,1,0,1,1),
            (0,0,0,1,1,0,1,1,1,1,0,0,0,0,0),
            (7,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,1),
            (0,1,1,0,1,1,1,1,1,0,1,1,0,1,1),
            (3,1,1,0,1,0,0,1,1,0,1,1,0,0,1,0,1),
            (1,0,0,1,1,0,0,1,0,1,0,1,1,0,0),
            (4,1,0,0,1,0,1,1,0,1,1,1,1,1,0,0,1),
            (0,0,1,0,0,1,1,0,1,0,0,0,1,1,0),
            (10,1,0,1,1,0,0,0,1,0,1,1,1,0,0,1,1),
            (1,1,0,0,1,1,1,1,0,0,0,1,0,0,0),
            (4,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,1),
            (0,1,0,1,0,1,1,1,1,0,1,1,1,1,1),
            (11,1,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1),
            (1,1,1,1,0,0,0,1,0,1,1,1,0,1,1),
            (10,1,0,1,0,1,1,0,0,1,0,0,0,1,1,0,1),
            (0,1,0,1,1,1,0,0,1,1,1,1,1,1,0),
            (6,1,1,1,1,0,1,1,0,1,0,1,1,0,1,1,1),
            (1,0,0,0,1,0,1,1,0,1,0,1,1,0,1),
            (9,1,0,1,1,1,1,0,0,1,1,0,0,0,1,1,1),
            (0,1,1,0,0,1,0,0,0,1,1,1,0,1,0),
            (9,1,1,1,0,1,0,1,0,1,0,0,1,1,1,1,1),
            (0,0,1,1,0,1,0,0,1,1,1,0,1,0,0),
            (12,1,1,1,0,1,1,1,0,0,1,1,0,0,0,1,1),
            (1,0,1,1,0,0,1,1,1,0,1,1,1,1,0),
            (13,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,1),
            (0,0,0,1,1,0,0,1,0,1,1,1,1,1,0),
            (14,1,0,1,1,1,0,0,1,1,1,0,1,0,1,1,1),
            (1,1,1,0,1,1,1,0,1,1,1,1,1,0,1),
            (11,1,0,0,1,1,0,0,1,0,0,0,1,0,1,0,1),
            (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))

# Change this assignment to correspond to the instance desired
instance = instance4

# Although all Aquarium game boards are square, this code generalizes
# to any rectangular game board
height = int((len(instance) -2) /2)
width = len(instance[0])

# Creates an array of integer variables the size of the game board
# Represents the solution to the game board
X = [ [ Int("x_%s_%s" % (i+1, j+1)) for j in range(width) ] for i in range(height) ]

# Ensures each cell is either a 1 or a 0 (filled or empty)
cells_c = [ Or(0 == X[i][j], X[i][j] == 1) for i in range(height) for j in range(width) ]

# Ensures each row has exactly the number of cells filled as the number dictated by
# the first number in that row
rows_c = [ Sum(X[i]) == instance[2*i+2][0] for i in range(height) ]

# Ensures each column has exactly the number of cells filled as the number dictated by
# the first number in that column
cols_c = [ (Sum([ X[i][j] for i in range(height) ]) == instance[0][j]) for j in range(width) ]

# Ensures each filled cell either has a wall below it or a filled cell below it
# Preserves the depth propert of aquariums (no floating water allowed)
depth_c = [ Or(X[i][j] == 0, instance[2*i+3][j] == 1, X[i+1][j] == 1) for i in range(height-1) for j in range(width) ]

# Ensures each filled cell either has a wall to the right of it or a filled cell to the right of it
# and either has a wall to the left of it or a filled cell to the left of it
# Provides a basic check that water level is consistent across a level in an aquarium
# Must be separated because these Or statements do not showrt circuit
rightwards_water_level_c = [ If(X[i][j] == 1, Or(instance[2*i+2][j+2] == 1, X[i][j+1] == 1), True) for i in range(height) for j in range(width-1) ]
leftwards_water_level_c = [ If(X[i][j] == 1, Or(instance[2*i+2][j+1] == 1, X[i][j-1] == 1), True) for i in range(height) for j in range(1, width) ]

# Helper function which looks for edge cases where two cells are on the same level but not physically
# connected. Instead they are connected by the aquarium level above them
def good_aquarium_level_above(row, col):
    k = col + 2
    good_aquarium = True
    # Walk to the right on the row above the given row until hitting a wall
    # Ensures that there is either a wall or filled cell below each cell in the above row
    while (instance[2*row][k] != 1):
        good_aquarium = And(good_aquarium, Or(instance[2*row+1][k-2] == 1,(X[row][k-2] == 1)))
        k = k+1
    return good_aquarium

# Ensures that water level in an aquarium is constant, even if two cells aren't physically connected.
# Accounts for cells being connected by the aquarium level above
aquarium_water_level_above_c = [If(And(X[i][j] == 1, instance[2*i+2][j+2] == 1, instance[2*i+1][j] == 0), good_aquarium_level_above(i,j), True)
                          for i in range(1,height) for j in range(width-1)]

# Helper function which looks for edge cases where two cells are on the same level but not physically
# connected. Instead they are connected by the aquarium level below them
def good_aquarium_level_below(row, col):
    k = col + 2
    good_aquarium = True
    # Walk to the right on the row below the given row until hitting a wall
    # Ensures that there is either a wall or filled cell below each cell in the above row
    while (instance[2*row+4][k] != 1):
        good_aquarium = And(good_aquarium, Or(instance[2*row+3][k-2] == 1,(X[row][k-2] == 1)))
        k = k+1
    return good_aquarium

# Ensures that water level in an aquarium is constant, even if two cells aren't physically connected.
# Accounts for cells being connected by the aquarium level below
aquarium_water_level_below_c = [If(And(X[i][j] == 1, instance[2*i+2][j+2] == 1, instance[2*i+3][j] == 0), good_aquarium_level_below(i,j), True)
                          for i in range(0,height-1) for j in range(width-1)]

# Collection of all restraints on the puzzle
puzzle_c = cells_c + rows_c + cols_c + depth_c + rightwards_water_level_c + leftwards_water_level_c + aquarium_water_level_above_c + aquarium_water_level_below_c

# Creates a new solver instance, adds the restraints, and attempts to solve the puzzle
s = Solver()
s.add(puzzle_c)
# To see all constraints written out, uncomment the next line
# print(s.to_smt2())
if s.check() == sat:
    m = s.model()
    r = [ [ m.evaluate(X[i][j]) for j in range(width) ] for i in range(height) ]
    print_matrix(r)
else:
    print("failed to solve")
