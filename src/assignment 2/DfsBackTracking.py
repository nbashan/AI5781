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


# This of course is not necessary legal, so we'll write a simple DFS search with backtracking:
def solve_queen(size):
    columns.clear()
    number_of_moves = 0  # where do I change this so it counts the number of Queen moves?
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
            # if the row is safe so we can place the queen in the place and move on to the next row
            if next_row_is_safe(column, size):
                place_in_next_row(column)
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
            prev_column = remove_in_current_row()
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

# That we now have to define

def place_in_next_row(column):
    columns.append(column)


def remove_in_current_row():
    if len(columns) > 0:
        return columns.pop()
    return -1


def next_row_is_safe(column, size):
    row = len(columns)
    # check column
    for queen_column in columns:
        if column == queen_column:
            return False

    # check diagonal
    for queen_row, queen_column in enumerate(columns):
        if queen_column - queen_row == column - row:
            return False

    # check other diagonal
    for queen_row, queen_column in enumerate(columns):
        if ((size - queen_column) - queen_row
                == (size - column) - row):
            return False
    return True


# Things should be ok but we don't have the counters I asked for.
# That will be the first things you'll need to add.
# Either way, let's print what we have:

# size = int(input('Enter n: '))
# sum = 0, iter = 0
# for i in range(0, 100):
# columns = [] #columns is the locations for each of the queens


# Used for calling from Main
def start(size):
    place_n_queens(size)
    display(size)
    print(columns)
    iter, my_sum = solve_queen(size)
    print("# of iterations:", iter)
    print("# of queens placed + backtracks:", my_sum)
    print(columns)
    return iter, my_sum


start(4)
