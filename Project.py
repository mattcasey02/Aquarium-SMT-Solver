from z3 import *

#6x6 easy
#instance = ((3,5,3,3,3,5),
#            (1,1,1,1,1,1),
#            (2,1,0,1,1,0,0,1),
#            (1,1,0,0,0,1),
#            (4,1,0,0,1,0,1,1),
#            (0,0,1,0,0,0),
#            (3,1,0,1,0,0,1,1),
#            (1,0,1,1,0,1),
#            (5,1,1,0,1,1,0,1),
#            (0,0,0,0,1,0),
#            (5,1,1,0,1,0,1,1),
#            (0,1,1,0,0,0),
#            (3,1,0,0,1,0,1,1),
#            (1,1,1,1,1,1))

#6x6 Easy
#instance = ((5,5,5,3,3,4),
#            (1,1,1,1,1,1),
#            (4,1,0,1,0,0,0,1),
#            (0,1,1,1,1,0),
#            (4,1,1,0,1,0,1,1),
#            (0,0,0,0,1,0),
#            (5,1,1,0,1,1,0,1),
#            (1,1,1,0,1,0),
#            (5,1,1,0,0,1,1,0),
#            (0,0,1,1,0,1),
#            (2,1,1,1,0,0,0,1),
#            (0,1,1,1,1,0),
#            (5,1,0,0,0,0,1,1),
#            (1,1,1,1,1,1))

#6x6 Hard
instance = ((5,4,3,2,5,3),
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

size = len(instance[0])

X = [ [ Int("x_%s_%s" % (i+1, j+1)) for j in range(size) ] for i in range(size) ]

# each cell is a 1 or a 0
cells_c = [ Or(0 == X[i][j], X[i][j] == 1) for i in range(size) for j in range(size) ]

# each row has exactly the number of cells filled as the number dictated by
# the first number in the corresponding row in the instance
rows_c = [ Sum(X[i]) == instance[2*i+2][0] for i in range(size) ]

# the ith column has exactly the number of cells filled as the number dictated by
# the ith number in the 0th row in instance
cols_c = [ (Sum([ X[i][j] for i in range(size) ]) == instance[0][j]) for j in range(size) ]

# each filled cell either has a wall below it or a filled cell below it
depth_c = [ Or(X[i][j] == 0, instance[2*i+3][j] == 1, X[i+1][j] == 1) for i in range(size-1) for j in range(size) ]

# each filled cell either has a wall to the right of it or a filled cell to the right of it
rightwards_water_level_c = [ Or(X[i][j] == 0, instance[2*i+2][j+2] == 1, X[i][j+1] == 1) for i in range(size) for j in range(size-1) ]

# each filled cell either has a wall to the left of it or a filled cell to the left of it
leftwards_water_level_c = [ Or(X[i][j] == 0, instance[2*i+2][j+1] == 1, X[i][j-1] == 1) for i in range(size) for j in range(1, size) ]

def good_aquarium_level(row, col):
    k = col + 2
    good_aquarium = True
    while (instance[2*row][k] != 1):
        good_aquarium = And(good_aquarium, Or(instance[2*row+1][k-2] == 1,(X[row][k-2] == 1)))
        k = k+1
    return good_aquarium

# ...
aquarium_water_level_c = [If(And(X[i][j] == 1, instance[2*i+2][j+2] == 1, instance[2*i+1][j] == 0), good_aquarium_level(i,j), True)
                          for i in range(1,size) for j in range(size-1)]

puzzle_c = cells_c + rows_c + cols_c + depth_c + rightwards_water_level_c + leftwards_water_level_c + aquarium_water_level_c

s = Solver()
s.add(puzzle_c)
# print(s.to_smt2())
if s.check() == sat:
    m = s.model()
    r = [ [ m.evaluate(X[i][j]) for j in range(size) ] for i in range(size) ]
    print_matrix(r)
else:
    print("failed to solve")
