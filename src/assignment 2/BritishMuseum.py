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
        column = random.randrange(0, size)
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
def  solve_queen(size):
    number_of_iterations = 1
    place_n_queens(size)
    # iterate over rows of board
    while not solved(size):
        number_of_iterations += 1
        place_n_queens(size)
        display(size)
        print(columns)
    print("Solved:")
    display(size)
    print("iterations: ")
    print(number_of_iterations)
    return number_of_iterations


def solved(size):
    flag = True
    for i in range(1, size):
        if flag:
            flag = next_row_is_safe(columns[i], i, size)
    return flag


# This code is nice, but it uses three functions:

# place_in_next_row

# remove_in_current_row

# next_row_is_safe

# That we now have to define

def next_row_is_safe(column, index, size):
    # row = len(columns)
    # check column
    for i in range(index):
        if column == columns[i]:
            return False

    # check diagonal
    for i in range(index):
        if columns[i] - i == column - index:
            return False

    # check other diagonal
    for i in range(index):
        if ((size - columns[i]) - i
                == (size - column) - index):
            return False
    return True


def start(size):
    return solve_queen(size)
