# Gradual Insanity [Starter, revised]
# Sidhant Rastogi
# November 11, 2019

from copy import deepcopy
import random

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

game1 = game(board([[2,3,1],[4,5,6],[9,7,8]]),
             board([[1,2,3],[4,5,6],[7,8,9]]))

game2 = game(board([[X,O,X],[A,O,A],[A,X,O]]),
             board([[O,A,X],[O,A,X],[O,A,X]]))

game3 = game(board([[X,O,O,X],[X,O,X,X],[X,X,X,X],[X,O,X,X]]),
             board([[X,X,X,X],[X,O,O,X],[X,O,O,X],[X,X,X,X]]))

game4 = game(board([[O,O,O,O,X],[O,X,O,O,O],[O,O,O,X,O],[O,X,O,O,O],[O,O,O,O,X]]),
             board([[O,O,O,O,O],[O,O,O,O,O],[O,O,X,O,X],[O,O,O,O,X],[O,O,X,O,X]]))

game5 = game(board([[X,O,O,O,X],[O,X,O,O,X],[O,O,O,O,O],[O,O,X,X,O],[X,X,O,O,X]]),
             board([[X,O,O,O,X],[O,X,O,X,O],[O,O,X,O,O],[O,X,O,X,O],[X,O,O,O,X]]))

game6 = game(board([[O,O,X,X,X],[X,O,X,X,X],[O,O,X,X,X],[O,O,O,X,X],[O,O,O,O,X]]),
             board([[X,O,O,O,X],[X,O,O,O,X],[X,X,X,X,X],[X,O,O,O,X],[X,O,O,O,X]]))

game7 = game(board([[B,B,X,B],[O,O,B,O],[A,A,O,A],[X,X,X,A]]),
             board([[X,X,X,X],[B,B,B,B],[O,O,O,O],[A,A,A,A]]))

game8 = game(board([[O,A,B,X,O],[O,C,O,C,B],[A,B,X,B,C],[X,C,A,A,X],[X,C,O,A,B]]),
             board([[X,C,O,A,B],[X,C,O,A,B],[X,C,O,A,B],[X,C,O,A,B],[X,C,O,A,B]]))

game9 = game(board([[X,X,A,X,X,X],[X,O,O,A,A,X],[X,O,B,A,A,A],[B,B,A,A,O,B],[B,B,B,O,O,A],[B,B,X,O,O,O]]),
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

def moveRight(mod_game, row_num):
    mod_board = mod_game.state
    row = mod_board.rows[row_num]
    last = row.pop()
    row.insert(0, last)

def moveLeft(mod_game, row_num):
    mod_board = mod_game.state
    row = mod_board.rows[row_num]
    first = row.pop(0)
    row.append(first)

def moveUp(mod_game, col_num):
    mod_board = mod_game.state
    col = []
    for i in range(0, len(mod_board.rows)):
        col.append(mod_board.rows[i][col_num])
    first = col.pop(0)
    col.append(first)
    for i in range(0, len(mod_board.rows)):
        mod_board.rows[i][col_num] = col[i]

def moveDown(mod_game, col_num):
    mod_board = mod_game.state
    col = []
    for i in range(0, len(mod_board.rows)):
        col.append(mod_board.rows[i][col_num])
    last = col.pop()
    col.insert(0, last)
    for i in range(0, len(mod_board.rows)):
        mod_board.rows[i][col_num] = col[i]

##EXTRA CREDIT
def scramble(g):
    for i in range(0, len(g.state.rows) * len(g.state.rows)):
        direction = random.randint(0, 3)
        row_col_num = random.randint(0, len(g.state.rows) - 1)
        if (direction == 0):
            moveRight(g, row_col_num)
        if (direction == 1):
            moveLeft(g, row_col_num)
        if (direction == 2):
            moveUp(g, row_col_num)
        if (direction == 3):
            moveDown(g, row_col_num)

def hint(to_check):
    while (to_check != []):
        current = to_check.pop(0)

        for i in range(0, len(current.state.rows)):
            gR = copy(current)
            gL = copy(current)
            gU = copy(current)
            gD = copy(current)
            moveRight(gR, i)
            moveLeft(gL, i)
            moveUp(gU, i)
            moveDown(gD, i)
            to_check.append(gR)
            to_check.append(gL)
            to_check.append(gU)
            to_check.append(gD)

            if (solved(gR)):
                return current
            elif (solved(gL)):
                return current
            elif (solved(gU)):
                return current
            elif (solved(gD)):
                return current

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
            num = int(command[1])
            mod_game = copy(games[num])
            show(mod_game.state, games[num].goal)
        elif command[0] == "s":
            scramble(mod_game)
            show(mod_game.state, mod_game.goal)
        elif command[0] == "r":
            moveRight(mod_game, int(command[1]))
            show(mod_game.state, mod_game.goal)
            if (solved(mod_game)):
                print("Yay, solved!")
                break
        elif command[0] == "l":
            moveLeft(mod_game, int(command[1]))
            show(mod_game.state, mod_game.goal)
            if (solved(mod_game)):
                print("Yay, solved!")
                break
        elif command[0] == "u":
            moveUp(mod_game, int(command[1]))
            show(mod_game.state, mod_game.goal)
            if (solved(mod_game)):
                print("Yay, solved!")
                break
        elif command[0] == "d":
            moveDown(mod_game, int(command[1]))
            show(mod_game.state, mod_game.goal)
            if (solved(mod_game)):
                print("Yay, solved!")
                break
        elif command == "z":
            reverse_game = copy(mod_game)
            reverse_game.state = mod_game.goal
            reverse_game.goal = mod_game.state
            reverse_game = hint([reverse_game])

            mod_game.state = reverse_game.state
            show(mod_game.state, mod_game.goal)

            if (solved(mod_game)):
                print("Yay, solved!")
                break
        else:
            print("eh?")

def main():
    topLevel()

main()
