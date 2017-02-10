from random import randint
import os.path
import sys

# GLOBAL VARIABLES
grid = [] # BEFUNGE GRID
x = 0 # X COORDINATE OF POINTER
y = 0 # Y COORDINATE OF POINTER
direction = "right" # CURRENT DIRECTION OF MOTION
stack = [] # LIFO NUMBER STORAGE
directions = ["right", "left", "up", "down"] # ALL POSSIBLE DIRECTIONS
inQuotes = False; # WHETHER WE'RE IN STRING MODE

# RUN PROGRAM
def main():
    grid = readFile()
    while grid[y][x] != "@":
        step()

# READS THE FILE AND STORES BEFUNGE GRID
def readFile():
    # CONFIRM A FILENAME WAS GIVEN
    if len(sys.argv) < 2:
        print "ERROR: No input file specified!"
        sys.exit()
    filename = sys.argv[1]

    # CONFIRM VALID FILENAME
    if not os.path.isfile(filename):
        print "ERROR: Specified input file does not exist!"
        sys.exit()

    # GET GRID DIMENSIONS
    numLines = 0
    lineLength = 0
    with open(filename) as f:
        for line in f:
            numLines += 1
            lineLength = max(lineLength, len(line.rstrip('\n')))

    # GENERATE THE GRID
    for row in range(numLines):
        grid.append([])
        for col in range(lineLength):
            grid[row].append(" ")

    # POPULATE THE GRID
    with open(filename) as f:
        row = 0
        for line in f:
            col = 0
            for char in line:
                if char != "\n":
                    grid[row][col] = char
                col += 1
            row += 1

    return grid

# PRINTS THE CONTENTS OF A GIVEN GRID -- useful for debugging
def printGrid(grid):
    for row in grid:
        for col in row:
            print col,
        print

# ADVANCES BEFUNGE GRID ONE STEP
def step():
    processInstruction(grid[y][x])
    move()
    # time.sleep(0.5)

# PROCESSES THE CURRENT INSTRUCTION
def processInstruction(instruction):
    global direction

    # STRING MODE
    global inQuotes
    if inQuotes == True and instruction != "\"":
        stack.append(ord(instruction))
        return

    # NOT STRING MODE
    if instruction == " ":
        # NO-OP -- PLACED FIRST FOR OPTIMIZATION
        pass
    elif instruction == ">": # START MOVING RIGHT
        direction = "right"
    elif instruction == "<": # START MOVING LEFT
        direction = "left"
    elif instruction == "^": # START MOVING UP
        direction = "up"
    elif instruction == "v": # START MOVING DOWN
        direction = "down"
    elif instruction.isdigit(): # IF IT'S A DIGIT, POP THAT DIGIT ONTO THE STACK
        stack.append(int(instruction))
    elif instruction == "+": # ADDITION
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
    elif instruction == "-": # SUBTRACTION
        a = stack.pop()
        b = stack.pop()
        stack.append(b-a)
    elif instruction == "*": # MULTIPLICATION
        a = stack.pop()
        b = stack.pop()
        stack.append(a*b)
    elif instruction == "/": # INT DIVISION
        a = stack.pop()
        b = stack.pop()
        stack.append(b//a)
    elif instruction == "%": # MODULO
        a = stack.pop()
        b = stack.pop()
        stack.append(b%a)
    elif instruction == "!": # LOGICAL NOT
        value = stack.pop()
        if value == 0:
            stack.append(1)
        else:
            stack.append(0)
    elif instruction == "`": # GREATER THAN
        a = stack.pop()
        b = stack.pop()
        if b > a:
            stack.append(1)
        else:
            stack.append(0)
    elif instruction == "?": # START MOVING IN A RANDOM CARDINAL DIRECTION
        rand = randint(0, 3)
        direction = directions[rand]
    elif instruction == "_": # POP; RIGHT IF 0, LEFT OTHERWISE
        value = stack.pop()
        if value == 0:
            direction = "right"
        else:
            direction = "left"
    elif instruction == "|": # POP; DOWN IF 0, UP OTHERWISE
        value = stack.pop()
        if value == 0:
            direction = "down"
        else:
            direction = "up"
    elif instruction == "\"": # TOGGLE STRING MODE
        inQuotes = not inQuotes
    elif instruction == ":": # DUPLICATE VALUE ON TOP OF STACK
        stack.append(stack[-1])
    elif instruction == "\\": # SWAP TWO VALUES ON TOP OF STACK
        a = stack.pop()
        b = stack.pop()
        stack.append(a)
        stack.append(b)
    elif instruction == "$": # POP TOP AND DISCARD
        stack.pop()
    elif instruction == ".": # POP AND OUTPUT AS INTEGER FOLLOWED BY SPACE
        print stack.pop(), " ",
    elif instruction == ",": # POP AND OUTPUT AS ASCII CHARACTER
        print chr(stack.pop()),
    elif instruction == "#": # BRIDGE -- SKIP NEXT CELL
        move()
    elif instruction == "p": # PUT -- POP Y, X, AND V, THEN SET (X,Y) TO V
        y = stack.pop()
        x = stack.pop()
        v = stack.pop()
        grid[y][x] = chr(v)
    elif instruction == "g": # GET -- POP Y AND X, THEN PUSH ASCII VALUE AT (X,Y)
        y = stack.pop()
        x = stack.pop()
        stack.append(ord(grid[y][x]))
    elif instruction == "&": # PUSH USER-GIVEN NUMBER
        stack.append(int(input("Enter a number: ")))
    elif instruction == "~": # PUSH ASCII VALUE OF USER-GIVEN CHARACTER
        stack.append(ord(input("Enter a character: ")))

# MOVES THE POINTER
def move():
    global x
    global y
    if direction == "right":
        x += 1
    elif direction == "left":
        x -= 1
    elif direction == "up":
        y -= 1
    elif direction == "down":
        y += 1

    if x < 0:
        x += len(grid[0])
    elif x == len(grid[0]):
        x = 0
    if y < 0:
        y += len(grid)
    elif y == len(grid):
        y = 0

# ACTUALLY RUN THE STUFF
main()
