# https://www.codingame.com/ide/puzzle/defibrillators
import math

lona = float(input().replace(",", "."))
lata = float(input().replace(",", "."))
n = int(input())
nearest = float('inf')
for i in range(n):
    defib = input()
    defib = defib.replace(",", ".").split(";")
    lonb = float(defib[4])
    latb = float(defib[5])
    x = (lonb - lona) * math.cos((lata + latb)/2)
    y = latb - lata
    d = math.sqrt(math.pow(x, 2) + math.pow(y, 2)) * 6371
    if nearest >= d:
        nearest = d
        answer = defib[1]

print(answer)
