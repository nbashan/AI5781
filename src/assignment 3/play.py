import alphaBetaPruning
import game

# A call to Python's library function
board = game.game()

# initialize game
game.create(board)
print("Initial Game")

# prints the board
game.printState(board)

# decides who is first (using input)
game.decideWhoIsFirst(board)

# Summarized the overall score
comp_count = 0

# This loops takes about 10 seconds on our computer!
for i in range(0, 100):
    while not game.isFinished(board):
        if game.isHumTurn(board):
            game.inputRandom(board)
            # game.inputMove(board)
        else:
            # The step of the computer according to our heuristic
            board = alphaBetaPruning.go(board)
        game.printState(board)
    if game.value(board) == 10**20:  # the computer (or smart agent) won
        comp_count += 1
    print("Start another game")
    game.create(board)
print("The agent beat you:", comp_count, " out of ", i+1)
print("Your grade in this section would be ", max(comp_count-90, 0)*2, " out of 20 ")

#################################################################################################

# Our strategy is very simple -
# we went through the existing code well and noticed that the heuristics are not perfect -
# the heuristic score can be improved by giving weight to the number of soldiers the player placed
# out of 4 soldiers who create a sequence
