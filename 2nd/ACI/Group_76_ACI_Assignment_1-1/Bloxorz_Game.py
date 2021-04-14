#+======================================================================================+
# |Authors          : Kolli Hrudhay(2019AH04040),
#                     Narendrababu S(2019AH04022),
#                     Akshat Gupta(2019AH04001)

# |Package          : ACI Assignment 1 - Bloxorz Game
# |Module           : Bloxorz_Game.py
# |Language         : Python 3.7
# |Description      : This module is built to represent python implementation of 
#                     the Bloxorz Game.
#                     This is the main module(script file) to be executed which 
#                     will read input from "solveWithAlgo" parameter variable and call the 
#                     respective functions/methods.
#
# |Working          : The module(code) will run for BFS(Bread First Search), DFS(Depth
#                     First Search), BEST(Best-First Search) Search Algorithms.
#                     Please provide the algorithm you want to run the code with as the 
#                     input to paramater variable "solveWithAlgo".
#                     The code will print all the intermediate steps/nodes from start to 
#                     end goal including both start and end states and also provide the 
#                     output of number of steps it takes to reach the goal state/location  
#                     from start state/location.
#
#                     Ex Input  : solveWithAlgo = "BEST"
#                     Ex Output : REACHED DESTINATION !!!!!!
#                                 NUMBER OF STEPS TO REACH DESTINATION FROM SOURCE:  8
#+======================================================================================+

# -*- coding: utf-8 -*-

# import required modules.
import copy

class Bloxorz:

    def __init__(self, x, y, rot, parent, board, x1=None,y1=None):
        self.x      = x
        self.y      = y
        self.rot    = rot  
        self.parent = parent
        self.board  = copy.deepcopy(board)
        self.x1     = x1
        self.y1     = y1
    
    def move_up(self):
        newBloxorz = Bloxorz(self.x, self.y, self.rot, self, self.board)

        if self.rot == "STANDING":
            newBloxorz.y -= 2 
            newBloxorz.rot = "CHECKING_Y"

        elif newBloxorz.rot == "CHECKING_X":
            newBloxorz.y -= 1
        
        elif newBloxorz.rot == "CHECKING_Y":
            newBloxorz.y -= 1
            newBloxorz.rot = "STANDING"
        
        return newBloxorz 

    def move_down(self):
        newBloxorz = Bloxorz(self.x, self.y, self.rot, self, self.board)

        if newBloxorz.rot == "STANDING":
            newBloxorz.y += 1
            newBloxorz.rot = "CHECKING_Y"

        elif newBloxorz.rot == "CHECKING_X":
            newBloxorz.y += 1

        elif newBloxorz.rot == "CHECKING_Y":
            newBloxorz.y += 2
            newBloxorz.rot = "STANDING"
        return newBloxorz 

    def move_right(self):
        newBloxorz = Bloxorz(self.x, self.y, self.rot, self, self.board)
    
        if newBloxorz.rot == "STANDING":
            newBloxorz.x += 1
            newBloxorz.rot = "CHECKING_X"

        elif newBloxorz.rot == "CHECKING_X":
            newBloxorz.x += 2
            newBloxorz.rot = "STANDING"

        elif newBloxorz.rot == "CHECKING_Y":
             newBloxorz.x += 1
        return newBloxorz

    def move_left(self):
        newBloxorz = Bloxorz(self.x, self.y, self.rot, self, self.board)

        if newBloxorz.rot == "STANDING":
            newBloxorz.rot = "CHECKING_X"
            newBloxorz.x -= 2

        elif newBloxorz.rot == "CHECKING_X":
            newBloxorz.x -= 1
            newBloxorz.rot = "STANDING"

        elif newBloxorz.rot == "CHECKING_Y":
            newBloxorz.x -= 1

        return newBloxorz 

    # FOR CASE SPLIT
    def split_move_up(self):
        newBloxorz = Bloxorz(self.x, self.y, self.rot, self, self.board, self.x1, self.y1)
        newBloxorz.y -= 1
        return newBloxorz 

    def split_move_down(self):
        newBloxorz = Bloxorz(self.x, self.y, self.rot, self, self.board, self.x1, self.y1)
        newBloxorz.y += 1
        return newBloxorz 


    def split_move_left(self):
        newBloxorz = Bloxorz(self.x, self.y, self.rot, self, self.board, self.x1, self.y1)
        newBloxorz.x -= 1
        return newBloxorz 


    def split_move_right(self):
        newBloxorz = Bloxorz(self.x, self.y, self.rot, self, self.board, self.x1, self.y1)
        newBloxorz.x += 1
        return newBloxorz 

    def split1_move_up(self):
        newBloxorz = Bloxorz(self.x, self.y, self.rot, self, self.board, self.x1, self.y1)
        newBloxorz.y1 -= 1
        return newBloxorz 

    def split1_move_down(self):
        newBloxorz = Bloxorz(self.x, self.y, self.rot, self, self.board, self.x1, self.y1)
        newBloxorz.y1 += 1
        return newBloxorz 

    def split1_move_left(self):
        newBloxorz = Bloxorz(self.x, self.y, self.rot, self, self.board, self.x1, self.y1)
        newBloxorz.x1 -= 1
        return newBloxorz 

    def split1_move_right(self):
        newBloxorz = Bloxorz(self.x, self.y, self.rot, self, self.board, self.x1, self.y1)
        newBloxorz.x1 += 1
        return newBloxorz 

    def disPlayPosition(self):
        if self.rot != "SPLIT":
            print(self.rot, self.x, self.y)
        else:
            print(self.rot, self.x, self.y, self.x1, self.y1)
    
    def disPlayBoard(self):
        
        # local definition
        x   = self.x
        y   = self.y
        x1  = self.x1
        y1  = self.y1
        rot = self.rot
        board = self.board

        if rot != "SPLIT":
            
            for i in range(len(board)): # for ROW
                print("",end='  ')
                for j in range(len(board[i])): # for COL in a ROW

                    if (i==y and j==x and rot=="STANDING") or \
                            ((i==y and j==x) or (i==y and j==x+1) and rot=="CHECKING_X") or \
                            ((i==y and j==x) or (i==y+1 and j==x) and rot=="CHECKING_Y"):

                        print("x",end=' ')

                    elif(board[i][j]==0):
                        print(" ",end=' ')
                    else:
                        print(board[i][j], end=' ')
                print("")
        else: # CASE SPLIT
            for i in range(len(board)): # for ROW
                print("",end='  ')
                for j in range(len(board[i])): # for COL

                    if (i==y and j==x) or (i==y1 and j==x1):
                        print("x",end=' ')

                    elif(board[i][j]==0):
                        print(" ",end=' ')
                    else:
                        print(board[i][j], end=' ')
                print("")


# isValidBloxorz
def isValidBloxorz(bloxorz):
    
    if isFloor(bloxorz):
        
        # local definition
        x     = bloxorz.x
        y     = bloxorz.y
        x1    = bloxorz.x1
        y1    = bloxorz.y1
        rot   = bloxorz.rot
        board = bloxorz.board
        
        
        # Case 2: 
        if rot == "STANDING" and board[y][x] == 2:
            return False 
            
        return True
    else:
        return False


def isFloor(bloxorz):
    x = bloxorz.x
    y = bloxorz.y
    rot = bloxorz.rot
    board = bloxorz.board
    
    if x >= 0 and y >= 0 and \
            y < MAP_ROW and x < MAP_COL and \
            board[y][x] != 0:

        if rot == "STANDING":
            return True
        elif rot == "CHECKING_Y":
            if y+1 < MAP_ROW and board[y+1][x] != 0 :
                return True
        elif rot == "CHECKING_X":
            if x+1 < MAP_COL and board[y][x+1] != 0 :
                return True
        else: # case SPLIT
            x1 = bloxorz.x1
            y1 = bloxorz.y1

            if x1 >= 0 and y1 >= 0 and \
                y1 < MAP_ROW and x1 < MAP_COL and \
                board[y1][x1] != 0:
                    return True

    else:
        return False


def isGoal(bloxorz):
    x = bloxorz.x
    y = bloxorz.y
    rot = bloxorz.rot
    board = bloxorz.board

    if rot == "STANDING" and  \
        board[y][x] == 9:
        return True
    else:
        return False


def isVisited(bloxorz):
    if bloxorz.rot != "SPLIT":

        for item in passState:
            if item.x == bloxorz.x     and item.y == bloxorz.y and \
                item.rot == bloxorz.rot and item.board == bloxorz.board:
                return True

    else: # case SPLIT
        for item in passState:
            if item.x  == bloxorz.x     and item.y  == bloxorz.y and \
               item.x1 == bloxorz.x1    and item.y1 == bloxorz.y1 and \
                item.rot == bloxorz.rot and item.board == bloxorz.board:
                return True

    return False

def move(Stack, bloxorz, flag):

    if isValidBloxorz(bloxorz):
        if isVisited(bloxorz):
            return None

        Stack.append(bloxorz)
        passState.append(bloxorz)
        #print(flag)
        return True 

    return False   

def printSuccessRoad(bloxorz):
    
    print("\nTHIS IS SUCCESS ROAD")
    print("================================")
    
    successRoad = [bloxorz]
    temp = bloxorz.parent
    
    while temp != None:
        
        if temp.rot != "SPLIT":
            newBloxorz = Bloxorz(temp.x, temp.y, \
                    temp.rot, temp.parent, temp.board)
        else: # case SPLIT
            newBloxorz = Bloxorz(temp.x, temp.y, \
                    temp.rot, temp.parent, temp.board, temp.x1, temp.y1)

        successRoad = [newBloxorz] + successRoad
        
        temp = temp.parent
    
    step = 0
    for item in successRoad:
        step += 1
        print("\nStep:", step, end=' >>>   ')
        item.disPlayPosition()
        print("=============================")
        item.disPlayBoard()
    
    print("\nREACHED DESTINATION !!!!!!")
    print("NUMBER OF STEPS TO REACH DESTINATION FROM SOURCE: ",step)
    
# solve DFS
def DFS(bloxorz):

    board = bloxorz.board
    Stack = []
    Stack.append(bloxorz)
    passState.append(bloxorz)
    
    virtualStep = 0

    while Stack:
        current = Stack.pop()

        if isGoal(current):
            printSuccessRoad(current)
            return True
        else:
            if current.rot != "SPLIT":
                virtualStep += 4

                move(Stack,current.move_up(), "up")
                move(Stack,current.move_right(), "right")
                move(Stack,current.move_down(), "down")
                move(Stack,current.move_left(), "left")
            else: 
                virtualStep += 8

                move(Stack,current.split_move_left(), "left0")
                move(Stack,current.split_move_right(), "right0")
                move(Stack,current.split_move_up(), "up0")
                move(Stack,current.split_move_down(), "down0")
                
                move(Stack,current.split1_move_left(), "left1")
                move(Stack,current.split1_move_right(), "right1")
                move(Stack,current.split1_move_up(), "up1")
                move(Stack,current.split1_move_down(), "down1")
    return False

# solve BFS
def BFS(bloxorz):

    board = bloxorz.board
    Queue = []
    Queue.append(bloxorz)
    passState.append(bloxorz)

    virtualStep = 0

    while Queue:
        current = Queue.pop(0)

        if isGoal(current):
            printSuccessRoad(current)
            return True

        if current.rot != "SPLIT":
            virtualStep += 4

            move(Queue,current.move_up(), "up")
            move(Queue,current.move_right(), "right")
            move(Queue,current.move_down(), "down")
            move(Queue,current.move_left(), "left")
        else: 
            virtualStep += 8

            move(Queue,current.split_move_left(), "left0")
            move(Queue,current.split_move_right(), "right0")
            move(Queue,current.split_move_up(), "up0")
            move(Queue,current.split_move_down(), "down0")
            
            move(Queue,current.split1_move_left(), "left1")
            move(Queue,current.split1_move_right(), "right1")
            move(Queue,current.split1_move_up(), "up1")
            move(Queue,current.split1_move_down(), "down1")
    return False

def moveBest(BestQueue, bloxorz, flag):
    
    if isValidBloxorz(bloxorz):
        if isVisited(bloxorz):            
            return False
        
        EvalCur = evalFunction(bloxorz)
        BestQueue.append((EvalCur, bloxorz))
        passState.append(bloxorz)

        return True
    return False
            
# solve Best-First Search
def BEST(bloxorz):
    
    # create BestQueue as a list to be later considered as a priority queue.
    BestQueue = []

    startEval = evalFunction(bloxorz)

    # insert start node
    BestQueue.append((startEval, bloxorz))
    BestQueue.sort(key = lambda z : z[1].x) # Implement BestQueue as priority queue for the list to be always sorted with highest priority element first.
    passState.append(bloxorz)
    
    virtualStep = 0

    # until priority queue is empty
    while BestQueue:

        item = BestQueue[0] # fetch the first element as it has the highest priority.
        BestQueue.pop(0)
        iDista = item[0]
        iBloxorz = item[1]

        # if goal
        if isGoal(iBloxorz):
            printSuccessRoad(iBloxorz)
            return True

        # put all new operator to queue
        if iBloxorz.rot != "SPLIT":
            
            virtualStep += 4

            # try up
            moveBest(BestQueue, iBloxorz.move_up(), "up") 
            moveBest(BestQueue, iBloxorz.move_down(), "down") 
            moveBest(BestQueue, iBloxorz.move_right(), "right") 
            moveBest(BestQueue, iBloxorz.move_left(), "left") 
        else: 
           
            virtualStep += 8

            moveBest(BestQueue, iBloxorz.split_move_left(), "left0")
            moveBest(BestQueue, iBloxorz.split_move_right(), "right0")
            moveBest(BestQueue, iBloxorz.split_move_up(), "up0")
            moveBest(BestQueue, iBloxorz.split_move_down(), "down0")
            
            moveBest(BestQueue, iBloxorz.split1_move_left(), "left1")
            moveBest(BestQueue, iBloxorz.split1_move_right(), "right1")
            moveBest(BestQueue, iBloxorz.split1_move_up(), "up1")
            moveBest(BestQueue, iBloxorz.split1_move_down(), "down1")

def evalFunction(bloxorz):

    #  local definition
    x   = bloxorz.x
    y   = bloxorz.y
    x1  = bloxorz.x1
    y1  = bloxorz.y1
    rot = bloxorz.rot
    board = bloxorz.board

    # get goal
    (xGoal, yGoal) = (0, 0)
    for yG in range(len(board)):
        for xG in range(len(board[0])):
            if board[y][x] == '9':
                (xGoal, yGoal) = (xG, yG)

    # calc distance pos-goal
    distance = 0

    if rot == "SPLIT":

        distance1 = (x-xGoal)*(x-xGoal)+(y-yGoal)*(y-yGoal)
        distance2 = (x1-xGoal)*(x1-xGoal)+(y1-yGoal)*(y1-yGoal)
        distance = (distance1+distance2)/2

    else:
        # (x1 - x2)^2 + (y1 - y2) ^ 2
        distance = (x-xGoal)*(x-xGoal)+(y-yGoal)*(y-yGoal)

    return int(distance)


# START PROGRAM HERE
# Main
if __name__=="__main__":
    passState = []
    MAP_ROW = 6
    MAP_COL = 10
    xStart = 1
    yStart = 1

    sourceMap = [
                    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 1, 1, 9, 1, 1],
                    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0]
                    ]

    bloxorz = Bloxorz(xStart, yStart, "STANDING", None, sourceMap)
    solveWithAlgo = "BFS"


    if solveWithAlgo == "DFS":
        print("Solve DFS")  
        DFS(bloxorz)

    elif solveWithAlgo == "BFS":
        print("Solve BFS")
        BFS(bloxorz)

    elif solveWithAlgo == "BEST":
        print("Solve Best")
        BEST(bloxorz)

    else:
        print("Wrong algorithms argument!")