
    def findNextCellToFill(grid, i, j):
            for x in range(i,9):
                    for y in range(j,9):
                            if grid[x][y] == 0:
                                    return x,y
            for x in range(0,9):
                    for y in range(0,9):
                            if grid[x][y] == 0:
                                    return x,y
            return -1,-1

    def isValid(grid, i, j, e):
            rowOk = all([e != grid[i][x] for x in range(9)])
            if rowOk:
                    columnOk = all([e != grid[x][j] for x in range(9)])
                    if columnOk:
                            # finding the top left x,y co-ordinates of the section containing the i,j cell
                            secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here. 
                            for x in range(secTopX, secTopX+3):
                                    for y in range(secTopY, secTopY+3):
                                            if grid[x][y] == e:
                                                    return False
                            return True
            return False

    def solveSudoku(grid, i=0, j=0):
            i,j = findNextCellToFill(grid, i, j)
            if i == -1:
                    return True
            for e in range(1,10):
                    if isValid(grid,i,j,e):
                            grid[i][j] = e
                            if solveSudoku(grid, i, j):
                                    return True
                            # Undo the current cell for backtracking
                            grid[i][j] = 0
            return False




Here is my sudoku solver in python. It uses simple backtracking algorithm to solve the puzzle. For simplicity no input validations or fancy output is done. Its the bare minimum code which solves the problem.
Algorithm

    Find all legal values of a given cell
    For each legal value, Go recursively and try to solve the grid

Solution

It takes 9X9 grid partially filled with numbers. A cell with value 0 indicates that it is not filled.
Code



    def findNextCellToFill(grid, i, j):
            for x in range(i,9):
                    for y in range(j,9):
                            if grid[x][y] == 0:
                                    return x,y
            for x in range(0,9):
                    for y in range(0,9):
                            if grid[x][y] == 0:
                                    return x,y
            return -1,-1

    def isValid(grid, i, j, e):
            rowOk = all([e != grid[i][x] for x in range(9)])
            if rowOk:
                    columnOk = all([e != grid[x][j] for x in range(9)])
                    if columnOk:
                            # finding the top left x,y co-ordinates of the section containing the i,j cell
                            secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here. 
                            for x in range(secTopX, secTopX+3):
                                    for y in range(secTopY, secTopY+3):
                                            if grid[x][y] == e:
                                                    return False
                            return True
            return False

    def solveSudoku(grid, i=0, j=0):
            i,j = findNextCellToFill(grid, i, j)
            if i == -1:
                    return True
            for e in range(1,10):
                    if isValid(grid,i,j,e):
                            grid[i][j] = e
                            if solveSudoku(grid, i, j):
                                    return True
                            # Undo the current cell for backtracking
                            grid[i][j] = 0
            return False


Testing the code


>>> input = [[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]
>>> solveSudoku(input)