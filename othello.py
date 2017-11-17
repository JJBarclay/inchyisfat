
import turtle
import math
import random

y_locations = {0:750,1:650,2:550,3:450,4:350,5:250,6:150,7:50} #global constant of y-locations of game board columns
x_locations = {0:60,1:160,2:260,3:360,4:460,5:560,6:660,7:760} #global constant of x-locations of game board rows

def square(size, pencolor, fillcolor):
    turtle.pendown
    turtle.color(pencolor)
    turtle.fillcolor(fillcolor)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup #helps make the game board sections

def make_board():
    turtle.speed(0)
    turtle.tracer(0,0)
    turtle.screensize(850,850)
    turtle.setworldcoordinates(0,0,850,850)
    turtle.penup()
    turtle.goto(10,0)
    for i in range (8):
        for x in range (8):
            square(90,'white','green')
            turtle.forward(100)
        turtle.forward(10)
        turtle.color('black')
        y_cor = turtle.ycor()
        turtle.goto(10,y_cor + 100)
    turtle.forward(50)
    for i in range(2):
        for num in '01234567':
            turtle.write(num, align = 'center')
            turtle.forward(100)
        turtle.right(180)
        turtle.forward(45)
        turtle.right(270)
        turtle.forward(75)
    turtle.update() #creates turtle graphical interface

def board_start():
    board_grid = [[0]*8for i in range(8)]
    upper_left = board_grid[0][0]
    lower_right = board_grid[7][7]
    board_grid[3][3] = 'W'
    board_grid[4][4] = 'W'
    board_grid[4][3] = 'B'
    board_grid[3][4] = 'B'#starting pieces set-up
    place_token(3,3,'white')
    place_token(4,4,'white')
    place_token(4,3,'black')
    place_token(3,4,'black')
    return(board_grid) #creates game board matrix #DO NOT FORGET TO MAKE GAME BOARD VARIABLE HERE TO PASS INTO THE FUNCTIONS

def place_token(x_loc,y_loc,color):
    turtle.goto((x_locations[x_loc]),(y_locations[y_loc]))
    turtle.shape('circle')
    turtle.shapesize(2.2,2.2)
    turtle.color(color)
    turtle.stamp() #uses global dictionaries to set down token of a player's say

def PC_turn(board):
    place = list(selectNextPlay(board))
    validity,to_flip = isValidMove(board, place[0],place[1], 'W')
    if validity == True:
        x_loc = int(place[0])
        y_loc = int(place[1])
        place_token(x_loc, y_loc, 'white')
        board[x_loc][y_loc] = 'W'
        for place in to_flip.keys():
            if place != 'validity':
                x_place = int(place[0])
                y_place = int(place[1])
                place_token(x_place, y_place, 'white')
                board[x_place][y_place] = 'W'
        return(board)

def on_board(x_loc, y_loc):
    if x_loc > -1 and x_loc < 8:
        if y_loc > -1 and y_loc < 8:
            return(True)
    else:
        return(False)

def neighborhood_watch(board,row,col): #identifies and returns a square's neighbors
    neighbor_list = {}
    for x_shift, y_shift in [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]: #location of neighbors relatively
        if on_board(x_shift + row,y_shift + col) == True:
            occupant = board[int(x_shift + row)][int(y_shift + col)]
            neighbor_list[int(x_shift + row),int(y_shift + col)] = occupant
    return(neighbor_list) #returns dictionary with locations as keys and occupants as values

def neighbor_check(board,row,col,color): #true or false for if there is an opponent in neighbors
    neighbors = neighborhood_watch(board, row, col)
    others = 0
    wanted_neighbors = {}
    wanted = ''
    if color == 'B': #get opposing color information
        wanted = 'W'
    if color == 'W':
        wanted = 'B'
    for location in neighbors:
        if neighbors[location] == wanted:
            wanted_neighbors[location] = wanted
            others += 1
    if others > 0:
        return(wanted_neighbors)
    else:
        return(False)

def youre_surrounded(board,row,col,color,wanted_neighbors):
    lets_flip = {} #dictionary to fill with locations to flip with what color to flip to
    if color == 'B': #get opposing color information
        opponent = 'W'
    else:
        opponent = 'B'
    for location in wanted_neighbors.keys(): #for each location that has an opponent's token
        for x_shift, y_shift in [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]: #for directional checking
            if (x_shift + row,y_shift + col) == location: #find which shift for directional checking
                    for multiplier in [1,2,3,4,5,6,7]: #max distance is 7 from initial
                        if on_board((multiplier*x_shift)+row,(multiplier*y_shift)+col):
                            if board[(multiplier*x_shift)+row][(multiplier*y_shift)+col] == opponent:
                                lets_flip[(multiplier*x_shift)+row,(multiplier*y_shift)+col] = color
                            if board[(multiplier*x_shift)+row][(multiplier*y_shift)+col] == color:
                                lets_flip['validity'] = True
                                break
                            else:
                                lets_flip['validity'] = False
    return(lets_flip)

def isValidMove(board, row, col, color): #checks if move is valid by calling helper functions
    x_val = int(row)
    y_val = int(col)
    neighbor_dict = neighborhood_watch(board, row, col)
    if board[x_val][y_val] != 'B'or 'W':
        if neighbor_check(board, row, col,color) !=False:
            wanted_ones = neighbor_check(board,row,col,color)
            if youre_surrounded(board,row,col,color,wanted_ones) != {}:
                lets_flip = youre_surrounded(board,row,col,color,wanted_ones)
                if lets_flip['validity'] == True:
                    return(True,lets_flip)
        return(False,None)

def getValidMoves(board, color):
    valid_moves = []
    for x in range(8):
        for y in range(8):
            validity,to_flip = isValidMove(board,x,y,color)
            if validity == True:
                valid_moves.append([x,y])
    return(valid_moves)

def human_turn(board):
    locs = list(turtle.textinput('Your Turn','Your Pieces are Black. Enter Row, Column Numbers'))
    if len(locs) != 3:
        locs = list(turtle.textinput('Your Turn','Enter Row, Column Numbers. Please ensure there is only a comma between numbers'))
    if len(locs) == 3:
        if locs == '':
            quit()
        validity,to_flip = isValidMove(board, int(locs[0]),int(locs[2]),'B')
        if validity == True:
            x_loc = int(locs[0])
            y_loc = int(locs[2])
            place_token(x_loc, y_loc, 'black')
            board[x_loc][y_loc] = 'B'
            for place in to_flip.keys():
                print(place)
                print(place[0])
                print(place[1])
                if place != 'validity':
                    x_place = int(place[0])
                    y_place = int(place[1])
                    place_token(x_place, y_place, 'black')
                    board[x_place][y_place] = 'B'
                return(board)
    if locs == []:
        quit()
    else:
        reply = turtle.textinput('Invalid Move', 'Type cont to continue, or nothing to quit.')
        if reply.lower() == 'cont':
            human_turn(board)
        else:
            quit()

def selectNextPlay(board):
    possibilities = getValidMoves(board,'W')
    return(random.choice(possibilities))

def whatdIGet(board):
    human_score = 0
    PC_score = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'B':
                human_score += 1
            if board[x][y] == 'W':
                PC_score += 1
    if human_score > PC_score:
        return("You have Won! Your Points: " + str(human_score) + " PC Points: " + str(PC_score))
    if human_score == PC_score:
        return("You have Tied. Your Points: " + str(human_score) + " PC Points: " + str(PC_score))
    else:
        return("You have Lost. Your Points: " + str(human_score) + " PC Points: " + str(PC_score))

def Lets_Bring_It_In():
    make_board() #turtle graphics
    le_board = board_start() #make board variable from function
    while getValidMoves(le_board,'W') and getValidMoves(le_board,'B') != []:
        le_board = human_turn(le_board)
        le_board = PC_turn(le_board)
    turtle.textinput('Game Over',str(whatdIGet(le_board)))
    quit()

def main():
    Lets_Bring_It_In()

if __name__ == '__main__':
    main()
