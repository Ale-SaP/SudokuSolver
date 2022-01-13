tablero = [
     #        #        #
    [0, 0, 4, 7, 0, 0, 0, 0, 5],
    [0, 2, 0, 0, 0, 0, 0, 8, 4],
    [0, 0, 8, 0, 0, 0, 0, 0, 0],
    [2, 0, 3, 0, 7, 0, 0, 0, 0],
    [0, 0, 0, 5, 4, 8, 0, 0, 0],
    [6, 0, 0, 0, 2, 0, 0, 0, 0],
    [1, 9, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 9, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 5, 7, 0]
    ]

"""tablero = [
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

"""

def square(grid, vert, hor):
    unavailable = []

    #We need to find out which 3x3 we need to turn into a list of unavailable numbers
    #The grid will be cut up in y axis, only picking the 3 lists that make that square vertically, but we only need 3 numbers per list
    #If our target is at 0,2 , the first 3 lists will be picked

    if (vert in range(0,3)):
        grid = (grid[0], grid[1], grid[2])

    elif (vert in range(3,6)):           
        grid = (grid[3], grid[4], grid[5])

    elif (vert in range(6,9)):
        grid = (grid[6], grid[7], grid[8])

    else: pass

    #Now, only having 3 lists or a 3x9 grid, it will be necessary to only pick the right cells to make a 3x3 grid
    #If our target is at any of the first 3 cells, those 3 will be picked in each list.

    if (hor in range(0,3)): #0, 1, 2
        for list in grid:
            for number in range(0, 3):
                if (list[number] != 0): unavailable.append(list[number])
            #for each list in the grid, add cells 1 to 3 to unavailable (if not = 0)

    elif (hor in range(3, 6)): # 3, 4, 5
        for list in grid:
            for number in range(3, 6):
                if (list[number] != 0): unavailable.append(list[number])
                #for each list in the grid, add cells 3 to 6 to unavailable (if not = 0)

    elif (hor in range(6, 9)): # 6, 7, 8
        for list in grid: 
            for number in range(6, 9):
                if (list[number] != 0): unavailable.append(list[number])
                #for each list in the grid, add cells 6 to 9 to unavailable (if not = 0)

    else: print("error")
    return(unavailable)


def horizontal(grid, vert, hor):
    unavailable = []
    for cell in grid[vert]:
        if (cell != 0): unavailable.append(cell)
    #For cells in the horizontal grid, add to unavailable (if not = 0)
    return(unavailable)

def vertical(grid, vert, hor):
    unavailable = []
    for number in range(9):
        if (grid[number][hor] != 0): unavailable.append(grid[number][hor])
    #For cells in the horizontal grid, add to unavailable (if not = 0)
    return(unavailable)

def listOfUnavailables(grid, vert, hor):
    horizontalUnavailables = horizontal(grid, vert, hor)
    verticalUnavailables = vertical(grid, vert, hor)
    squareUnavailables = square(grid, vert, hor)
    completeUnavailables = []

    for element in (horizontalUnavailables + verticalUnavailables + squareUnavailables):
        if (completeUnavailables.count(element) < 1): completeUnavailables.append(element)
        else: pass
    return(completeUnavailables)

def check(grid):
    verticalCount = 0
    errors = 0
    emptyCells = 0
    for verticalList in grid:
        cellCount = 0
        for cell in verticalList:
            unavailables = listOfUnavailables(grid, verticalCount, cellCount)
            availables = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for x in unavailables: 
                availables.remove(x)
            if ((cell in unavailables) > 1): 
                grid[verticalCount][cellCount] = availables[1]
            else: pass
            if (cell == 0):  emptyCells += 1
            cellCount += 1
        verticalCount += 1
    print(emptyCells) 
    return(emptyCells)

def start(grid):
    timesDone = 0
    while ((check(grid) != 0) and (timesDone < 10)):
        timesDone += 1
        verticalCount = 0
        for verticalList in grid:
            cellCount = 0
            for cell in verticalList:
                if (cell == 0): 

                    unavailables = (listOfUnavailables(grid, verticalCount, cellCount))
                    availables = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    for x in unavailables: 
                        availables.remove(x)

                    if (len(availables) == 1): 
                        grid[verticalCount][cellCount] = availables[0]

                else: pass

                cellCount += 1
            verticalCount += 1
    print(grid, timesDone)


start(tablero)