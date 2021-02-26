# https://www.codingame.com/ide/puzzle/sudoku-validator


grid = []
cubeblock = []
checker = 0

for i in range(9):
    row = [int(j) for j in input().split()]
    grid.append(row)
    if (len(list(set(row))) != 9 or sum(row) != 45):
        checker += 1

for i in range(9):
    column = []
    for row in grid:
        column.append(row[i])
    if (len(list(set(column))) != 9 or sum(column) != 45):
        checker += 1

for i in range(0, 9, 3):
    cube = []
    for l in range(0, 9, 3):
        for j in range(3):
            for k in range(3):
                cube.append(grid[i+j][k+l])
    cubeblock.append(cube)

for j in range(3):
    for i in range(0, 27, 9):
        if (len(cubeblock[j][i:i+9]) != 9 or sum(cubeblock[j][i:i+9]) != 45):
            checker += 1
            
print("true") if checker == 0 else print("false")