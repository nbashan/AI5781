import copy
import alphaBetaPruning
import random

VICTORY = 10 ** 20  # The value of a winning board (for max)
LOSS = -VICTORY  # The value of a losing board (for max)
TIE = 0  # The value of a tie
SIZE = 4  # the length of winning seq.
COMPUTER = SIZE + 1  # Marks the computer's cells on the board
HUMAN = 1  # Marks the human's cells on the board


rows = 6
columns = 7

#initialize game with a board
#includes:
#   * 2 dimension array
#   * turn
class game:
    board = []
    size = rows * columns
    playTurn = HUMAN

    # Used by alpha-beta pruning to allow pruning

    '''
    The state of the game is represented by a list of 4 items:
        0. The game board - a matrix (list of lists) of ints. Empty cells = 0,
        the comp's cells = COMPUTER and the human's = HUMAN
        1. The heuristic value of the state.
        2. Whose turn is it: HUMAN or COMPUTER
        3. Number of empty cells
    '''

# initialize game
def create(s):
    # Returns an empty board. The human plays first.
    # create the board
    s.board = []
    for i in range(rows):
        s.board = s.board + [columns * [0]]

    s.playTurn = HUMAN
    s.size = rows * columns
    s.val = 0.00001

    # return [board, 0.00001, playTurn, r*c]     # 0 is TIE

#deep copy for a game
#when alpha beta pruning we don't want to change the board
def cpy(s1):
    # construct a parent DataFrame instance
    s2 = game()
    s2.playTurn = s1.playTurn
    s2.size = s1.size
    s2.board = copy.deepcopy(s1.board)
    # print("board ", s2.board)
    return s2

#sum of all huristic value of alpha beta pruning in matrix
def value(s):
    # Returns the heuristic value of s
    dr = [-SIZE + 1, -SIZE + 1, 0, SIZE - 1]  # the next lines compute the heuristic val.
    dc = [0, SIZE - 1, SIZE - 1, SIZE - 1]
    val = 0.00001
    #iterates over the matrix and for each
    #place checks 4 optional wins:
    #   * -1,0 | up
    #   * -1,1 / up
    #   * 0,1 | down
    #   * 1,1 \ down
    for row in range(rows):
        for col in range(columns):
            for i in range(len(dr)):
                t = checkSeq(s, row, col, row + dr[i], col + dc[i])
                if t in [LOSS, VICTORY]:
                    val = t #if loss or victory so matrix is at its
                    break
                else:
                    val += t # add huristic value
    if s.size == 0 and val not in [LOSS, VICTORY]:
        val = TIE # if size is equal to zero that means that
    return val

#returns huristic value of on of 4 optional postions \:down |:down /:up |:up
def checkSeq(s, r1, c1, r2, c2):
    # r1, c1 are in the board. if r2,c2 not on board returns 0.
    # Checks the seq. from r1,c1 to r2,c2. If all X returns VICTORY. If all O returns LOSS.
    # If empty returns 0.00001. If no Os returns 1. If no Xs returns -1.
    if r2 < 0 or c2 < 0 or r2 >= rows or c2 >= columns:
        return 0  # r2, c2 are illegal

    dr = (r2 - r1) // (SIZE - 1)  # the horizontal step from cell to cell
    dc = (c2 - c1) // (SIZE - 1)  # the vertical step from cell to cell

    sum = 0

    for i in range(SIZE):  # summing the values in the seq.
        sum += s.board[r1 + i * dr][c1 + i * dc]

    if sum == COMPUTER * SIZE:
        return VICTORY

    elif sum == HUMAN * SIZE:
        return LOSS

    elif sum > 0 and sum < COMPUTER:
#######################################################################################
#   we noticed that sum of chips is a big factor so we wanted to give it a value
##  we found that it is an exponnestial function with extrem point at 9.5
        return -1*(9.5**sum)
######################################################################################

    elif sum > 0 and sum % COMPUTER == 0:
#####################################################################################
##   we noticed that sum of chips is a big factor so we wanted to give it a value
##   we found that it is an exponnestial function with extrem point at 9.5
        return 9.5**(sum//5)
######################################################################################

    return 0.00001  # not 0 because TIE is 0


#prints the current state of the board and if they have victory tie or loss it prints it as well
def printState(s):
    # Prints the board. The empty cells are printed as numbers = the cells name(for input)
    # If the game ended prints who won.
    for r in range(rows):
        print("\n|", end="")
        for c in range(columns):
            if s.board[r][c] == COMPUTER:
                print("X|", end="")
            elif s.board[r][c] == HUMAN:
                print("O|", end="")
            else:
                print(" |", end="")
    print()

    for i in range(columns):  # For numbers on the bottom
        print(" ", i, sep="", end="")

    print()

    val = value(s)

    if val == VICTORY:
        print("I won!")
    elif val == LOSS:
        print("You beat me!")
    elif val == TIE:
        print("It's a TIE")

#game finishes if they have a loss or victory or tie
def isFinished(s):
    # Seturns True iff the game ended
    return value(s) in [LOSS, VICTORY, TIE] or s.size == 0

#if human turn returns true else returns false
def isHumTurn(s):
    # Returns True iff it is the human's turn to play
    return s.playTurn == HUMAN

#if input is 1 so computer starts else human starts
def decideWhoIsFirst(s):
    # The user decides who plays first
    if int(input("Who plays first? 1-me / anything else-you : ")) == 1:
        s.playTurn = COMPUTER
    else:
        s.playTurn = HUMAN
    return s.playTurn

# gets a boars and a collumn and puts the chip in the right column
def makeMove(s, c):
    # Puts mark (for human or computer) in col. c
    # and switches turns.
    # Assumes the move is legal.
    r = 0
    while r < rows and s.board[r][c] == 0:
        r += 1

    s.board[r - 1][c] = s.playTurn  # marks the board
    s.size -= 1  # one less empty cell

    #switch of turn
    if (s.playTurn == COMPUTER):
        s.playTurn = HUMAN
    else:
        s.playTurn = COMPUTER

#inputs a move if we use the option of someone really playing
def inputMove(s):
    # Reads, enforces legality and executes the user's move.
    flag = True
    while flag:
        c = int(input("Enter your next move: "))
        if c < 0 or c >= columns or s.board[0][c] != 0:
            print("Illegal move.")
        else:
            flag = False # to finish loop
            makeMove(s, c)

#option for computer to play randomly as human
def inputRandom(s):
    # See if the random should block one move ahead
    '''for i in range(0,columns):
        tmp=cpy(s)
        makeMove(tmp, i)
        if(value(tmp)==VICTORY):
            makeMove(s,i)'''
    #if there is an option for a win so it moves there
    for i in range(0, columns):  # this simple agent always plays min
        tmp = cpy(s)
        makeMove(tmp, i)
        if (value(tmp) == LOSS and s.board[0][i] == 0):  # so a "loss" is a win for this side
            makeMove(s, i)
            return
    # If no obvious move, than move random
    flag = True
    while flag:
        c = random.randrange(0, columns)
        if c < 0 or c >= columns or s.board[0][c] != 0:
            print("Illegal move.")
            printState(s)
            # break
        else:
            flag = False
            makeMove(s, c)

#returns a list of all optional moves
def getNext(s):
    # returns a list of the next states of s
    ns = []
    for c in list(range(columns)):
        # print("c=",c)
        if s.board[0][c] == 0:
            # print("possible move ", c)
            tmp = cpy(s)
            makeMove(tmp, c)
            # print("tmp board=",tmp.board)
            ns += [tmp]
            # print("ns=",ns)
    return ns

# make move according alpha beta pruning at depth of 2
def inputComputer(s):
    return alphaBetaPruning.go(s)
