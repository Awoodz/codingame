# https://www.codingame.com/ide/puzzle/dungeons-and-maps

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


w, h = [int(i) for i in input().split()]
start_row, start_col = [int(i) for i in input().split()]
n = int(input())

map_stack = [[input() for j in range(h)] for i in range(n)]

testlist = []

def map_resolver(dungeon_map, start_row, start_col, w, h):

    x, y = start_col, start_row
    checker = ""
    count = 0
    while checker == "":
        rules = {
            ">": (x + 1, y),
            "<": (x - 1, y),
            "^": (x, y - 1),
            "v": (x, y + 1),
            ".": (x, y)
        }
        count += 1
        try:
            if count > (w * h):
                checker = "TRAP"
            elif dungeon_map[y][x] in rules:
                x, y = rules[dungeon_map[y][x]]
            elif dungeon_map[y][x] == "T":
                checker = "WIN"
        except IndexError:
            checker = "TRAP"

    return count, checker


for i in range(len(map_stack)):
    testlist.append(map_resolver(map_stack[i], start_row, start_col, w, h))

if all(status == "TRAP" for (_, status) in testlist):
    print("TRAP")
else:
    best = math.inf
    for i in range(len(testlist)):
        if testlist[i][0] < best and testlist[i][1] == "WIN":
            best = testlist[i][0]
            answer = i
    print(answer)


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
