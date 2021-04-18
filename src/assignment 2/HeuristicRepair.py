# Netanel Bashan, 323056077, netanebashan12@gmail.com
# Elyasaf Dimant, 204006415, elyasafdi@gmail.com
import random

columns = []
number_of_iterations = 1


# Let's setup one iteration of the British Museum algorithm-- we'll put down 4 queens randomly.
def place_n_queens(size):
    columns.clear()
    row = 0
    while row < size:
        column = random.randrange(0, size)
        columns.append(column)
        row += 1


# main function to solve the queen

def solve_queen(size):
    global number_of_iterations
    place_n_queens(size)
    # iterate over rows of board

    # two lists to check if the hill climbing got
    # stuck and is doing the same thing on and on
    last_state_1 = []
    last_state_2 = []

    deep_copy(columns, last_state_1, size)
    flag_pos = True

    while not solved(size):
        number_of_iterations += 1

        ###################################################################################
        #######   OUR HEURISTIC IS TO MOVE THE QUEEN THAT THE DECREASE IS THE LARGEST
        ###################################################################################
        max_decrease_threat = 0

        row_max_decrease_threat = 0
        column_max_decrease_threat = (columns[0] + 1) % size

        for i in range(size):

            # the amount of threats the
            # current queen has in the current row
            queen_threat = amount_threatened(columns[i], i, size)

            # loop over all columns in certain row
            for j in range(size):
                if j != columns[i]:

                    # calls amount_threatened that accepts column and row
                    #  we add 3 because that the amount of threats that queen_threat
                    # equals three extra threats 2 on each diagonal and 1 in the column
                    queen_check = amount_threatened(j, i, size) + 3

                    # found a place to move
                    if queen_threat - queen_check >= max_decrease_threat:
                        max_decrease_threat = queen_threat - queen_check
                        row_max_decrease_threat = i
                        column_max_decrease_threat = j

        move_most_threatened_queen(row_max_decrease_threat, column_max_decrease_threat)
        if not flag_pos and columns == last_state_1:
            # this happens when going to moving the best queen doesn't
            # help and it is stuck doing the same thing on and on
            print("hill climbing got stuck################################################################")
            display(size)
            return False

        # each time we need to store two
        # matrix in last_state_1 and last_state_2
        if flag_pos:
            deep_copy(columns, last_state_2, size)
            flag_pos = False
        else:
            deep_copy(columns, last_state_1, size)
            flag_pos = True

        display(size)
        print(columns)
    print("Solved:")
    display(size)
    print("iterations: ")
    print(number_of_iterations)
    return number_of_iterations


# function for copying 1 list to another

def deep_copy(list1, list2, size):
    if len(list2) == 0:
        for i in range(size):
            list2.append(list1[i])
    else:
        for i in range(size):
            list2[i] = list1[i]


# moves most threatened queen in certain row to new_column

def move_most_threatened_queen(row, new_column):
    columns[row] = new_column


# function that returns true if the matrix is solved

def solved(size):
    flag = True
    for i in range(1, size):
        if flag:
            flag = next_row_is_safe(columns[i], i, size)
    return flag


# Now, we can print the result with a simple loop:
def display(size):
    for row in range(len(columns)):
        for column in range(size):
            if column == columns[row]:
                print('♛', end=' ')
            else:
                print(' .', end=' ')
        print()


# function to check if the row is safe

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


# function that gets the column and a row and returns the amount of threats the place has

def amount_threatened(column, row, size):
    counter = -3

    for queen_column in columns:
        if queen_column == column:
            counter += 1  # they have a threat

    # check diagonal
    for queen_row, queen_column in enumerate(columns):
        if queen_column - queen_row == column - row:
            counter += 1  # they have a threat

    # check other diagonal
    for queen_row, queen_column in enumerate(columns):
        if ((size - queen_column) - queen_row
                == (size - column) - row):
            counter += 1  # they have a threat

    return counter


# function to start the process

def start(size):
    a = solve_queen(size)
    while not a:
        a = solve_queen(size)
    return a


start(4)
