sudoku = [
     #        #        #
    [5, 0, 0, 6, 0, 1, 0, 0, 0],
    [0, 3, 0, 0, 7, 5, 0, 4, 9],
    [0, 0, 0, 9, 4, 8, 0, 0, 0],
    [1, 5, 7, 0, 0, 0, 0, 0, 0],
    [0, 9, 6, 0, 0, 0, 2, 0, 8],
    [2, 0, 0, 1, 6, 9, 0, 5, 0],
    [4, 1, 0, 3, 0, 7, 0, 6, 0],
    [0, 2, 0, 5, 1, 0, 3, 7, 0],
    [7, 0, 3, 4, 0, 0, 1, 8, 0]
    ]
#Easy

sudokuH = [
     #        #        #
    [0, 0, 4, 7, 0, 0, 0, 0, 5],
    [0, 2, 0, 0, 0, 0, 0, 8, 4],
    [0, 0, 8, 0, 0, 0, 0, 0, 0],
    [2, 0, 3, 0, 7, 0, 0, 0, 0],
    [0, 0, 0, 5, 4, 8, 0, 0, 0],
    [6, 0, 0, 0, 2, 0, 0, 0, 0],
    [1, 9, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 9, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 5, 7, 0, 0]
    ]
#hard

sudokuVH = [
     #        #        #
    [0, 0, 0, 0, 3, 0, 0, 5, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 4, 2, 0, 0, 0, 0, 9],
    [0, 2, 0, 0, 0, 0, 0, 0, 6],
    [6, 0, 7, 0, 0, 5, 0, 9, 0],
    [0, 8, 0, 7, 0, 0, 0, 0, 0],
    [7, 0, 9, 4, 0, 0, 0, 0, 1],
    [0, 0, 8, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 4, 0, 0]
    ] 
#very hard

#Whole program explained at the end

def square(vert, hor):
    unavailable = []

    #We need to find out which 3x3 we need to turn into a list of unavailable numbers
    #The grid will be cut up in y axis, only picking the 3 lists that make that square vertically, but we only need 3 numbers per list
    #If our target is at 0,2 , the first 3 lists will be picked

    if (vert in range(0,3)):
        grid = (sudoku[0], sudoku[1], sudoku[2])

    elif (vert in range(3,6)):           
        grid = (sudoku[3], sudoku[4], sudoku[5])

    elif (vert in range(6,9)):
        grid = (sudoku[6], sudoku[7], sudoku[8])

    #Now, only having 3 lists with 9 cells each or a 3x9 grid, it will be necessary to only pick the right cells to make a 3x3 grid
    #If our target is at any of the first 3 cells, those 3 will be picked in each list.

    if (hor in range(0,3)): #0, 1, 2
        for list in grid:
            for number in range(0, 3):
                if (list[number] != 0): 
                    unavailable.append(list[number])
            #for each list in the grid, add cells 1 to 3 to unavailable (if not = 0)

    elif (hor in range(3, 6)): # 3, 4, 5
        for list in grid:
            for number in range(3, 6):
                if (list[number] != 0): 
                    unavailable.append(list[number])
                #for each list in the grid, add cells 3 to 6 to unavailable (if not = 0)

    elif (hor in range(6, 9)): # 6, 7, 8
        for list in grid: 
            for number in range(6, 9):
                if (list[number] != 0): 
                    unavailable.append(list[number])
                #for each list in the grid, add cells 6 to 9 to unavailable (if not = 0)

    return(unavailable)

def horizontal(vert, hor):
    unavailable = []
    for cell in sudoku[vert]:
        if (cell != 0): unavailable.append(cell)
    #For cells in the horizontal grid, add to unavailable (if not = 0)
    return(unavailable)

def vertical(vert, hor):
    unavailable = []
    for number in range(9):
        if (sudoku[number][hor] != 0): unavailable.append(sudoku[number][hor])
    #For cells in the horizontal grid, add to unavailable (if not = 0)
    return(unavailable)

def listOfAvailables(vert, hor):
    unavailables = []
    availables = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for element in (horizontal(vert, hor) + vertical(vert, hor) + square(vert, hor)):
        if (unavailables.count(element) < 1): 
            unavailables.append(element)
    #This is to avoid repeating the same numbers

    for each in unavailables: 
        availables.remove(each)
    #Removing the unavailables from the list

    return(availables)


def start(sudoku):
    for vert in range(9):
        for hor in range(9):
            if (sudoku[vert][hor] == 0): 
                availables = (listOfAvailables(vert, hor))
                for number in availables:
                    sudoku[vert][hor] = number
                    start(sudoku)
                    sudoku[vert][hor] = 0
                return 
    print(sudoku)  
    input("Is it the only answer?")


#Explaining everything: 

#When start gets called, the vertical axis (or vert) is iterated 9 times, to call all 9 lists that form a sudoku grid.
#Same thing happens with the horizontal axis (or hor), to call all 9 "cells" that form a list.

#If the value of the cell is 0, the listOfAvailables function will return what it indicates.
#listOfAvailables also calls the square, horizontal and vertical funtions.

#On the first empty cell, it'll set the first valid number as the result.
#After that, it will run the funtion until the whole sudoku is solved without errors.
#If there are no available numbers, it will backtrack to the cell before and try other possible combination.

start(sudoku)
