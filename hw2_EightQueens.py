#Declare number of queens to be solved for on 8x8 chess board
global numberQueens

numberQueens = 8
#Function to print chess board
def printBoard(chessBoard): 
    i = 0
    j = 0
    
    for i in range(numberQueens): 
        for j in range(numberQueens): 
            print(chessBoard[i][j], end='  ') 
        print()
        
#Function to check if queen placement is safe
def isSafe(chessBoard, row, column): 
    i = 0
    j = 0
    for i in range(column): 
        if chessBoard[row][i] == 1: 
            return False
    #Note: only need to check left of placed queen for each queen
    #This is because each placed queen has no queens to the right of it when placed
    i = 0
    j = 0
    for i,j in zip(range(row,-1,-1), range(column,-1,-1)): 
        if chessBoard[i][j] == 1: 
            return False
    i = 0
    j = 0
    for i,j in zip(range(row,numberQueens,1), range(column,-1,-1)): 
        if chessBoard[i][j] == 1: 
            return False
  
    return True
    
#Solver function
def solveEightQueens(chessBoard, column): 
    #Base case
    if column == numberQueens: 
        return True
    
    i = 0
    #Check to see if queens are safe
    for i in range(numberQueens): 
  
        if isSafe(chessBoard, i, column): 
 
            chessBoard[i][column] = 1
  
            #Call function recursivly to place remaining queens.
            if solveEightQueens(chessBoard, column+1) == True: 
                return True
  
            chessBoard[i][column] = 0
            
    return False
    
def eightQueens(): 
    #Data structure (two dimensional list) to solve 8 queens problem

    chessBoard = [ [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0]] 
              
    #Call solver function       
    solveEightQueens(chessBoard, 0)

    
    print("Solution Found!")
    print("End board state:")
    printBoard(chessBoard) 

#Call our eight queens function, and we're done!
eightQueens() 
