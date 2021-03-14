# https://www.codingame.com/ide/puzzle/a-childs-play

import math

w, h = [int(i) for i in input().split()]
n = int(input())
line = [input() for i in range(h)]

startcol, startrow = tuple(
    (i, j)
    for i in range(len(line))
    for j in range(len(line[i]))
    if line[i][j] == "O"
)[0]

direction = 0
moves = 0
pre_moves = 0
checker = False

left_moves = math.inf
x, y = startrow, startcol

while moves != left_moves:

    direction_dict = [
        (x, y - 1),
        (x + 1, y),
        (x, y + 1),
        (x - 1, y)
    ]

    if line[direction_dict[direction][1]][direction_dict[direction][0]] == "#":
        direction = direction + 1 if direction != 3 else 0
        if direction == 2 and checker is False:
            startrow, startcol = x, y

            pre_moves = moves
            moves = 0
            checker = True
        continue
    else:
        x, y = direction_dict[direction]
        moves += 1

    if x == startrow and y == startcol:
        left_moves = ((n - pre_moves) % moves)
        if moves + pre_moves == n:
            break
        moves = 0
    if moves + pre_moves == n:
        break

print(x, y)
