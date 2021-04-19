# Netanel Bashan, 323056077, netanebashan12@gmail.com
# Elyasaf Dimant, 204006415, elyasafdi@gmail.com
import random

# As we did in class,
# we will represent the board as a one-dimensional array where each position
# in the array is the n'th queen's column value. So if the array is: [1, 3, 0, 2],
# then the first queen is in position 1 (from 0--3), the second queen is in position 3 (the last column),
# the third queen is in the first column and the last queen is the in the second position.

columns = []
# columns is the locations for each of the queens
# columns[r] is a number c if a queen is placed at row r and column c.


# Our method is as follows:
# we construct a matrix corresponding in size to the calendar of the queens.
# At first the whole matrix is filled with "0".
# Each queen we put on the board we mark all the places it threatens by changing their contents
# from 0 to the position of the matrix on the board.
# for example if in square [1,1] we put a queen
# then we mark all its diagonals (which marked with 0) and its column marked [1,1].
# In this way we will know to eliminate the specific threats
# that this queen has created when we remove the queen in the backtrack process.
matrix = []


# hint -- you will need this for the following code: column=random.randrange(0,size)
# Let's setup one iteration of the British Museum algorithm-- we'll put down 4 queens randomly.

def place_n_queens(size):
    columns.clear()
    row = 0
    while row < size:
        column = random.randrange(0, size - 1)
        columns.append(column)
        row += 1


# Now, we can print the result with a simple loop:
def display(size):
    for row in range(len(columns)):
        for column in range(size):
            if column == columns[row]:
                print('♛', end=' ')
            else:
                print(' .', end=' ')
        print()


# This of course is not necessary legal, so we'll write a simple Forward Checking::
def solve_queen(size):
    columns.clear()
    number_of_moves = 0
    number_of_iterations = 0
    row = 0
    column = 0
    # iterate over rows of board
    while True:
        # place queen in next row
        ''''print(columns)
        print("I have ", row, " number of queens put down")
        display()
        print(number_of_moves)'''
        while column < size:
            number_of_iterations += 1
            # if matrix[row][column] != 0 it's mean that this box is already threatened
            # so we will not put a queen in it and we will advance to the next column in the same row
            # until we reach the last column where column == size - 1
            while matrix[row][column] != 0 and column != size - 1:
                column += 1
                number_of_iterations += 1
            # if the row is safe so we can place the queen in the place and move on to the next row
            if next_row_is_safe(column):
                place_in_next_row(column, size)
                number_of_moves += 1
                row += 1
                column = 0
                break
            else:
                column += 1
        # if I could not find an open column or if board is full
        if column == size or row == size:
            number_of_iterations += 1
            # if board is full, we have a solution
            if row == size:
                print("I did it! Here is my solution")
                display(size)
                # print(number_of_moves)
                return number_of_iterations, number_of_moves
            # I couldn't find a solution so I now backtrack
            prev_column = remove_in_current_row(size)
            number_of_moves += 1
            if prev_column == -1:  # I backtracked past column 1
                print("There are no solutions")
                # print(number_of_moves)
                return number_of_iterations, number_of_moves
            # try previous row again
            row -= 1
            # start checking at column = (1 + value of column in previous row)
            column = 1 + prev_column


# This code is nice, but it uses three functions:
# place_in_next_row
# remove_in_current_row
# next_row_is_safe


# this func has 2 responsibilities:
# 1: add the queen to the board - the "append" command
# 2: add all the threats that the queen has made.

def place_in_next_row(column, size):
    row = len(columns) + 1
    # check diagonal
    for i in range(row, size):
        for j in range(size):
            # (j - i == column - row + 1) means first diagonal
            # (size - j - i == size - column - row + 1) means other diagonal
            if (column-row + 1 == j-i or size - j - i == size - column - row + 1 or j == column) and matrix[i][j] == 0:
                matrix[i][j] = row
    columns.append(column)


# helper function for backtracking when ever whe back track
# we need to take out all the threats that the backtracked queen has threatened
# and remove the current queen

def remove_in_current_row(size):
    if len(columns) > 0:
        row = len(columns)
        column = columns.pop()
        for i in range(size):
            for j in range(size):
                if matrix[i][j] == row:
                    matrix[i][j] = 0
        return column
    return -1


# if the place in matrix is equal to zero so it is safe
# other wise it has a threat and it is not safe!

def next_row_is_safe(column):
    row = len(columns)
    if matrix[row][column] != 0:
        return False

    return True


# initialize the matrix that will store the data of threats in columns

def init(size):
    for i in range(size):
        matrix.append([])
        for j in range(size):
            matrix[i].append(0)


# Things should be ok but we don't have the counters I asked for.
# That will be the first things you'll need to add.
# Either way, let's print what we have:

# size = int(input('Enter n: '))
# sum = 0, iter = 0
# for i in range(0, 100):
#    columns = [] #columns is the locations for each of the queens


# function to call from main that calls a function that solves the n queen problem

def start(size):
    init(size)
    iter, my_sum = solve_queen(size)
    print("# of iterations:", iter)
    print("# of queens placed + backtracks:", my_sum)
    print(columns)
    return iter, my_sum


start(4)
