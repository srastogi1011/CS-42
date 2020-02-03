# Gradual Insanity [Starter]
# Robert M. Keller [Replace this with YOUR NAME.]
# November 6, 2019

from copy import deepcopy

class board(object):
    ''' A board represents a board in the Gradual Insanity Game      '''
    ''' rows is a list of lists, each inner list representing a      '''
    ''' row of the board. The elements can be characters or numbers. '''
    def __init__(self, rows):
        self.rows = rows

class game(object):
    ''' A game is a pair of boards: an initial board and a goal board. '''
    def __init__(self, initial, goal):
        self.state = initial
        self.goal = goal

def copy(board):
   ''' Make a deep copy of a board '''
   return deepcopy(board)

def copy(game):
   ''' Make a deep copy of a game '''
   return deepcopy(game)

def equal(board1, board2):
    ''' Test whether two boards are equal. '''
    ''' This assumes that all rows of each have the same length. '''
    numRows = len(board1.rows)
    if numRows != len(board2.rows):
        return False
    numCols = len(board1.rows[0])
    for i in range(0, numRows):
        for j in range(0, numCols):
            if board1.rows[i][j] != board2.rows[i][j]:
                return False
    return True
    
def solved(game):
    ''' Test whether a game is solved '''
    return equal(game.state, game.goal)

### Symbols used on various boards
X = "X"
O = "O"
A = "A"
B = "B"
C = "C"

### Sample Boards
game0 = game(board([[O,X,X],[X,X,O],[O,X,X]]),
             board([[X,O,O],[X,X,O],[X,X,X]]))

game1 = game(board([[O,O,O,O,X],[O,X,O,O,O],[O,O,O,X,O],[O,X,O,O,O],[O,O,O,O,X]]),
             board([[X,O,O,O,X],[O,O,O,O,O],[O,O,X,O,O],[O,O,O,O,O],[X,O,O,O,X]]))

game2 = game(board([[O,X,X,O],[O,X,X,X],[X,X,O,X],[X,X,X,X]]),
             board([[X,X,X,X],[X,O,O,X],[X,O,O,X],[X,X,X,X]]))

game3 = game(board([[O,O,O,O,O],[O,O,O,X,X],[O,O,X,X,O],[X,X,O,X,O],[O,O,X,O,X]]),
             board([[X,O,O,O,X],[O,X,O,X,O],[O,O,X,O,O],[O,X,O,X,O],[X,O,O,O,X]]))

game4 = game(board([[O,X,O,O,X],[X,O,X,X,O],[O,O,X,O,O],[O,X,X,O,X],[X,O,X,X,X]]),
             board([[X,O,O,O,X],[X,O,O,O,X],[X,X,X,X,X],[X,O,O,O,X],[X,O,O,O,X]]))

game5 = game(board([[3,6,8],[5,1,2],[7,4,9]]),
             board([[1,2,3],[4,5,6],[7,8,9]]))

game6 = game(board([[O,X,X],[A,O,A],[X,A,O]]),
             board([[O,A,X],[O,A,X],[O,A,X]]))

game7 = game(board([[B,O,O,A],[X,A,A,O],[B,A,X,B],[X,X,O,B]]),
             board([[X,X,X,X],[B,B,B,B],[O,O,O,O],[A,A,A,A]]))

game8 = game(board([[O,X,B,X,C],[B,O,C,X,A],[O,A,B,B,C],[A,O,A,A,C],[X,B,O,C,X]]),
             board([[X,C,O,A,B],[X,C,O,A,B],[X,C,O,A,B],[X,C,O,A,B],[X,C,O,A,B]]))

game9 = game(board([[O,B,X,X,B,O],[A,O,O,X,X,B],[X,B,A,A,B,A],[B,A,B,A,X,O],[X,X,O,O,B,O],[B,O,A,X,A,A]]),
             board([[X,X,X,O,O,O],[X,X,X,O,O,O],[X,X,X,O,O,O],[B,B,B,A,A,A],[B,B,B,A,A,A],[B,B,B,A,A,A]]))
        
### Array of boards for chooser
games = [game0, game1, game2, game3, game4, game5, game6, game7, game8, game9]

def show(board1, board2):
    ''' Print two boards side-by-side '''
    ''' This assumes that the boards have the same dimensions and '''
    ''' that all rows are of the same length. '''
    numRows = len(board1.rows)
    numCols = len(board1.rows[0])
    print("   ", end = '')
    for j in range(0, numRows):
       print(j, end = '')
       print(" ", end = '')
    print("    ", end = '')
    for j in range(0, numRows):
       print(j, end = '')
       print(" ", end = '')
    print("")
        
    for i in range(0, numRows):
        print(str(i) + "  ", end = '')
  
        for token in board1.rows[i]:
           print(token, end = '')
           print(" ", end = '')

        print(" |  ", end = '')

        for token in board2.rows[i]:
           print(token, end = '')
           print(" ", end = '')

        print("")

def help():
    print("Enter gN, where N is a number, to start a new game.")
    print("Enter q to Quit.")
    print("")
    print("A game shows as two grids of symbols side-by-side, separated by |.")
    print("The left grid is the current state, and the right grid is the goal.")
    print("The objective is to get from the current state to the goal by")
    print("executing one of the commands below.")              
    print("During game play, the commands are (where M is an index):")
    print("    rM to rotate row M to the Right")
    print("    lM to rotate row M to the Left")
    print("    uM to rotate column M Up")
    print("    dM to rotate column M Down")
    print("    z to obtain a hint for solving the puzzle")
    print("Typing q during the game will quit the current game.")

def topLevel():
    ''' This is a top level for the Gradual Insanity Game '''
    print("*** Welcome to Gradual Insanity. Type h for Help, q to Quit. ***")
    while True:
        command = input("?? ")
        if command == "h":
            help()
        elif command == "q":
            print("Quitting, as you asked.")
            break
        elif command[0] == "g":
            print("Unimplemented")
        else:
            print("eh?")

def main():
    topLevel()

main()
    
