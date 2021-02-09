# https://www.codingame.com/ide/puzzle/horse-racing-duals
import math

resultlist = []

n = int(input())

pilist = [int(input()) for i in range(n)]

pilist.sort()

best = math.inf
for i in range(n - 1):
    result = abs(pilist[i] - pilist[i + 1])
    if result < best:
        best = result

print(best)
